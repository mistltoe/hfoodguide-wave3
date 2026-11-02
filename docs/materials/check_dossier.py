"""dossier.json 형식 검사: 필수 키·절 8개·문장마다 [n]·출처 번호 일치·위키 출처 금지·고시 기준 일치(notice.json).
사용: python3 check_dossier.py <slug> [<slug> ...]   (오류가 있으면 종료 코드 1)"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
KEYS = ["overview", "history", "biology", "related_species", "cultivation", "processing", "genetics", "safety"]
REF = re.compile(r"\[(\d+(?:\s*[,–-]\s*\d+)*)\]")
BANNED = re.compile(r"wikipedia|namu\.wiki|나무위키|위키백과|blog\.naver|tistory", re.I)


def refs(text: str) -> set[int]:
    out = set()
    for m in REF.finditer(text or ""):
        for part in re.split(r"\s*,\s*", m.group(1)):
            if re.search(r"[–-]", part):
                a, b = [int(x) for x in re.split(r"\s*[–-]\s*", part)]
                out |= set(range(a, b + 1))
            else:
                out.add(int(part))
    return out


def sentences(body: str) -> list[str]:
    s = re.split(r"(?<=[\]가-힣)])[.!?]\s+|\n\n", body or "")     # 'C.A.' 'P.' 같은 약어에서는 자르지 않음
    return [x.strip() for x in s if x and len(x.strip()) > 15]


def check(slug: str) -> list[str]:
    p = HERE / slug / "dossier.json"
    if not p.exists():
        return [f"{slug}: dossier.json 없음"]
    try:
        d = json.loads(p.read_text(encoding="utf-8"))
    except ValueError as e:
        return [f"{slug}: JSON 오류 {e}"]
    errs = []
    for k in ("slug", "name_ko", "scientific_name", "sections", "compounds", "markers", "sources"):
        if k not in d:
            errs.append(f"키 없음: {k}")
    secs = {s.get("key"): s for s in d.get("sections") or []}
    for k in KEYS:
        if k not in secs:
            errs.append(f"절 없음: {k}")
        elif len(secs[k].get("body") or "") < 120:
            errs.append(f"절이 너무 짧음: {k}")
    used = set()
    for s in d.get("sections") or []:
        for sent in sentences(s.get("body")):
            if not REF.search(sent) and "확인하지 못" not in sent:
                errs.append(f"[{s.get('key')}] 출처 번호 없는 문장: {sent[:50]}")
        used |= refs(s.get("body"))
    for arr in ("compounds", "markers", "nutrients", "production", "world", "assays", "gi", "orgs"):
        for x in d.get(arr) or []:
            src = x.get("source") or []
            if arr != "nutrients" and not src:
                errs.append(f"{arr}: source 없음 — {str(x)[:60]}")
            used |= set(int(n) for n in src if str(n).isdigit())
            for f in ("content_text", "activity_ko", "spec", "daily_intake", "note", "content", "rationale"):
                used |= refs(x.get(f))
    for a in d.get("assays") or []:
        if a.get("role") not in ("official", "literature"):
            errs.append(f"assays: role 은 official·literature — {a.get('compound')}")
        if not a.get("compound"):
            errs.append("assays: compound 없음")
        cond = a.get("conditions") or {}
        if not isinstance(cond, dict):
            errs.append(f"assays: conditions 는 객체 — {a.get('compound')}")
    srcs = {int(s["n"]): s for s in d.get("sources") or [] if str(s.get("n")).isdigit()}
    for n in sorted(used - set(srcs)):
        errs.append(f"쓴 번호가 sources 에 없음: [{n}]")
    for n in sorted(set(srcs) - used):
        errs.append(f"sources 의 [{n}] 을 어디에도 쓰지 않음")
    for n, s in srcs.items():
        if BANNED.search((s.get("url") or "") + (s.get("title") or "") + (s.get("publisher") or "")):
            errs.append(f"쓰지 않기로 한 출처 [{n}]: {s.get('url')}")
        if not s.get("url"):
            errs.append(f"[{n}] url 없음")
    nt = HERE / slug / "notice.json"
    if nt.exists():
        items = json.loads(nt.read_text(encoding="utf-8"))["items"]
        mk = " ".join(json.dumps(m, ensure_ascii=False) for m in d.get("markers") or [])
        for it in items:
            if it["marker"] and it["marker"].replace(" ", "")[:6] not in mk.replace(" ", ""):
                errs.append(f"markers 에 고시 지표성분이 없음: {it['ingredient']} · {it['marker']}")
    return [f"{slug}: {e}" for e in errs]


if __name__ == "__main__":
    tot = []
    for s in sys.argv[1:]:
        e = check(s)
        tot += e
        print(f"{s}: 오류 {len(e)}")
        for x in e[:30]:
            print("  ", x)
    sys.exit(1 if tot else 0)
