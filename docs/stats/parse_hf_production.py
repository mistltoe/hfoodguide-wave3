"""식약처 「식품 등의 생산실적」(건강기능식품 편) PDF 텍스트 → 원료(품목)별 연도 통계 CSV.

입력: docs/refs/_text/*.txt (pdftotext -layout 결과)
출력: docs/stats/hf_items.csv  (year, kind, item, cap_t, prod_t, prod_value_k, sales_t, sales_k, export_t, export_usd, src)
      docs/stats/hf_items_rank.csv (2013–2017 보고서의 '품목별 생산액(억원)' 순위표: year, kind, item, prod_value_100m, share, src)
사용: python -I docs/stats/parse_hf_production.py <텍스트 폴더>
"""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

NUM = r"(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?|-"
ROW7 = re.compile(r"^\s*(?P<name>\S.*?)\s{2,}(?P<n>(?:" + NUM + r")(?:\s+(?:" + NUM + r")){6})\s*$")
ROW2 = re.compile(r"^\s*(?P<name>\S.*?)\s{2,}(?P<v>\d{1,3}(?:,\d{3})*(?:\.\d+)?)\s+(?P<s>\d+(?:\.\d+)?)\s*$")
SKIP = re.compile(r"품목명|생산현황|매출현황|생산능력|소\s*계|합\s*계|^\s*계\s|구\s*분|단위|▌|주\)|^\s*\d\)|^\s*[가-하]\.")


def f(x: str):
    return None if x == "-" else float(x.replace(",", ""))


def year_of(name: str) -> int | None:
    m = re.search(r"(20\d\d)", name)
    return int(m.group(1)) if m else None


def parse7(lines: list[str], kind: str, year: int, src: str) -> list[dict]:
    out, pend = [], ""
    for i, ln in enumerate(lines):
        m = ROW7.match(ln)
        if not m:
            t = ln.strip()
            # 숫자 없는 이름 조각(다음 줄 이름의 앞부분이거나 앞 줄 이름의 뒷부분)
            if t and not SKIP.search(t) and not re.search(r"\d{2,},", t) and len(t) < 60:
                if out and out[-1]["_open"]:
                    out[-1]["item"] += " " + t
                    it = out[-1]["item"]
                    out[-1]["_open"] = it.count("(") > it.count(")") or it.endswith(("의", "와", "과", ",", "및", "등", "-"))
                else:
                    pend = (pend + " " + t).strip() if pend else t
            elif not t:
                pend = ""
            continue
        name = m.group("name").strip()
        if SKIP.search(name):
            pend = ""
            continue
        if pend and (name.startswith(("(", ")")) or name[:1].islower() or (")" in name and "(" not in name)):
            name = pend + " " + name
        pend = ""
        n = [f(x) for x in m.group("n").split()]
        is_open = name.count("(") > name.count(")") or name.endswith(("의", "와", "과", ",", "및", "등", "-"))
        out.append({"year": year, "kind": kind, "item": name, "cap_t": n[0], "prod_t": n[1], "prod_value_k": n[2], "sales_t": n[3],
                    "sales_k": n[4], "export_t": n[5], "export_usd": n[6], "src": src, "_open": is_open})
    for r in out:
        r.pop("_open")
        r["item"] = re.sub(r"\s+", " ", r["item"]).strip()
    return out


def sections_7col(text: str):
    """(kind, lines) — '고시형'·'개별인정형' 품목 표 구간"""
    L = text.splitlines()
    heads = [(i, "고시형" if "고시형" in ln else "개별인정형") for i, ln in enumerate(L)
             if re.search(r"(품목 유형별 현황\s*–\s*(고시형|개별인정형)|□\s*(고시형|개별인정형)\s*품목\s*(\d\))?\s*$)", ln)]
    res = []
    for k, (i, kind) in enumerate(heads):
        end = heads[k + 1][0] if k + 1 < len(heads) else min(len(L), i + 1500)
        seg = L[i:end]
        # 다음 큰 절(2-3-3 / 2-4 / 2.3.2 …)에서 끊는다
        for j, ln in enumerate(seg[1:], 1):
            if re.match(r"\s*(2-3-[3-9]|2-4|2\.3\.[2-9]|2\.4|□\s*(기능성|지역))", ln):
                seg = seg[:j]
                break
        res.append((kind, seg))
    return res


TOT = re.compile(r"^\s*(20\d\d)\s+(\d{3})\s+((?:[\d,]+\s+){7}[\d,]+)\s*$")
TOT_KEYS = ["firms", "prod_value_100m", "prod_t", "sales_100m", "sales_t", "dom_sales_100m", "dom_sales_t", "export_100m", "export_t"]


def totals(text: str, src_year: int, src: str) -> list[dict]:
    """총괄 현황 표: 연도 · 업체 수 · 생산액 · 생산량 · 총 매출액 · 총 매출량 · 내수 판매액·량 · 수출 판매액·량 (억원·톤)"""
    out = []
    i = text.find("건강기능식품")
    for ln in text.splitlines():
        m = TOT.match(ln)
        if m:
            vals = [float(x.replace(",", "")) for x in [m.group(2)] + m.group(3).split()]
            if len(vals) == 9 and 2000 < int(m.group(1)) <= src_year:
                out.append({"year": int(m.group(1)), **dict(zip(TOT_KEYS, vals)), "src_year": src_year, "src": src})
    return out


OLD = re.compile(r"^\s*(20(?:0\d|1[0-3]))\s+([\d,]+)\s+([\d,]+)\s+([\d,]+)\s+([\d,]+)\s+([\d,]+)\s+([\d,]+)\s+([\d,]+)\s*$")


def old_totals(text: str, src: str) -> list[dict]:
    """2013 보고서 '3.2.1 연도별 추이': 생산능력 · 총 생산액(억원) · 총 생산량 · 내수용 생산액·량 · 수출용 생산액·량 (2009–2013)"""
    out = []
    for ln in text.splitlines():
        m = OLD.match(ln)
        if m:
            v = [float(x.replace(",", "")) for x in m.groups()[1:]]
            out.append({"year": int(m.group(1)), "cap_t": v[0], "prod_value_100m": v[1], "prod_t": v[2], "dom_prod_value_100m": v[3],
                        "dom_prod_t": v[4], "export_prod_value_100m": v[5], "export_prod_t": v[6], "src": src})
    return out


def main(folder: str) -> None:
    items, ranks, tots = [], [], []
    for p in sorted(Path(folder).glob("*.txt")):
        name = p.name
        if not ("생산실적" in name or "건강기능식품" in name) or "축산물" in name or "(1)" in name or "시장현황" in name or "기획분석" in name:
            continue
        y = year_of(name)
        if not y:
            continue
        text = p.read_text(encoding="utf-8", errors="ignore")
        if "건강기능식품" not in text:
            continue
        got = 0
        tots += totals(text, y, name)
        if y == 2013 and "국내시장" in name:
            olds = old_totals(text, name)
            if olds:
                with open(Path(__file__).parent / "hf_totals_2009_2013.csv", "w", newline="", encoding="utf-8-sig") as fh:
                    w = csv.DictWriter(fh, fieldnames=list(olds[0].keys()))
                    w.writeheader()
                    w.writerows(olds)
        for kind, seg in sections_7col(text):
            rows = parse7(seg, kind, y, name)
            items += rows
            got += len(rows)
            if not rows:   # 2013–2017: '구분 / 생산액(억원) / 비율(%)' 순위표
                for ln in seg[:200]:
                    m = ROW2.match(ln)
                    if m and not SKIP.search(m.group("name")):
                        ranks.append({"year": y, "kind": kind, "item": m.group("name").strip(), "prod_value_100m": f(m.group("v")),
                                      "share": float(m.group("s")), "src": name})
        print(y, name[:50], "7열", got, file=sys.stderr)
    # 같은 해에 여러 파일(통계집·분석보고서)이 있으면 하나만
    seen, uniq = set(), []
    for r in items:
        k = (r["year"], r["kind"], r["item"])
        if k not in seen:
            seen.add(k)
            uniq.append(r)
    out = Path(__file__).parent
    with open(out / "hf_items.csv", "w", newline="", encoding="utf-8-sig") as fh:
        w = csv.DictWriter(fh, fieldnames=list(uniq[0].keys()))
        w.writeheader()
        w.writerows(uniq)
    seen, ru = set(), []
    for r in ranks:
        k = (r["year"], r["kind"], r["item"])
        if k not in seen:
            seen.add(k)
            ru.append(r)
    if ru:
        with open(out / "hf_items_rank.csv", "w", newline="", encoding="utf-8-sig") as fh:
            w = csv.DictWriter(fh, fieldnames=list(ru[0].keys()))
            w.writeheader()
            w.writerows(ru)
    best = {}
    for t in tots:                       # 같은 연도는 가장 최근 보고서 값(수정 반영)
        if t["year"] not in best or t["src_year"] > best[t["year"]]["src_year"]:
            best[t["year"]] = t
    with open(out / "hf_totals.csv", "w", newline="", encoding="utf-8-sig") as fh:
        w = csv.DictWriter(fh, fieldnames=["year"] + TOT_KEYS + ["src_year", "src"])
        w.writeheader()
        w.writerows(sorted(best.values(), key=lambda r: r["year"]))
    print("items", len(uniq), "rank rows", len(ru), "totals", sorted(best), file=sys.stderr)


if __name__ == "__main__":
    main(sys.argv[1])
