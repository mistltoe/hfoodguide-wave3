"""통계청 「농작물생산조사(농작물생산통계)」·농식품부 「특용작물 생산실적」 텍스트(pdftotext -layout) → 시도별 품목 생산 표(CSV)
- 농작물생산통계: '연도별, 시·도별 농작물 생산량'(5개년) 표. 열 머리 = 연도 줄, 위의 글자 줄 = 품목, 행 = 시도. 값: 재배면적(ha)·10a당 생산량(kg)·생산량(톤)
- 특용작물 생산실적: '시도별·품목별 생산실적'(그해 1년) 표. 열 머리 = 농가수·전체면적·수확면적·단수·생산량 묶음, 위의 글자 줄 = 품목
- 스캔본(글자 없음)은 건너뛴다. 같은 연도·품목·시도가 여러 책에 있으면 최신 책 값을 쓴다.
사용: python -I docs/stats/parse_regional.py <텍스트 폴더> docs/stats [<KOSIS xlsx 폴더>]
- KOSIS 통계표(xlsx, 시도별)를 함께 주면 그 값을 가장 앞에 둔다(책보다 최신 수정치)
결과: regional_crops.csv (source,book_year,item,category,region,year,metric,value,unit)"""
from __future__ import annotations

import csv
import re
import sys
import unicodedata
from pathlib import Path

REGIONS = ["전국", "계", "서울", "부산", "대구", "인천", "광주", "대전", "울산", "세종", "경기", "강원", "충북", "충남", "전북", "전남", "경북", "경남", "제주"]
NUM = re.compile(r"-?[\d,]+(?:\.\d+)?|-|…|x|X")
YEAR = re.compile(r"\b(19[6-9]\d|20[0-4]\d)\b")
HANGUL = re.compile(r"[가-힣ㆍ･·()（）]+")


def _w(ch: str) -> int:
    return 2 if unicodedata.east_asian_width(ch) in ("W", "F") else 1


def disp(line: str) -> list[int]:
    """글자 위치 → 화면 칸 위치(한글은 두 칸). 글자 줄과 숫자 줄의 열을 맞추려면 칸으로 재야 한다"""
    out, x = [], 0
    for ch in line:
        out.append(x)
        x += _w(ch)
    out.append(x)
    return out


def toks(line: str, pat=re.compile(r"\S+")):
    d = disp(line)
    return [(d[m.start()], d[m.end()], m.group()) for m in pat.finditer(line)]


def num(v: str):
    if v in ("-", "…", "x", "X"):
        return None
    try:
        return float(v.replace(",", ""))
    except ValueError:
        return None


def region_of(line: str) -> tuple[str | None, str]:
    """행의 시도 이름(왼쪽이나 오른쪽, 글자 사이 공백 허용)과 숫자 부분"""
    ko = "".join(re.findall(r"[가-힣]", line))
    for r in REGIONS:
        if ko == r:
            rest = re.sub(r"\s*".join(r), " ", line, count=1)
            return ("전국" if r == "계" else r), rest
    return None, line


def measure_of(line: str):
    s = re.sub(r"\s+", "", line)
    if s.startswith("재배면적"):
        return "area_ha", "ha"
    if s.startswith("10a당생산량") or s.startswith("10a당수량"):
        return "yield_kg10a", "kg/10a"
    if s.startswith("생산량"):
        return "prod_t", "t"
    return None


def assign(spans, a, b):
    """글자 토큰(a~b)을 열 묶음(spans=[(시작,끝)])에 배정: 묶음 사이 빈칸은 가운데에서 나눈다"""
    c = (a + b) / 2
    for q in range(len(spans) - 1):
        if c < (spans[q][1] + spans[q + 1][0]) / 2:
            return q
    return len(spans) - 1


def label_line(lines, i, stop=6):
    """i 줄 위로 가장 가까운 '품목 이름' 줄(한글만, 제목·단위 줄 제외)"""
    for j in range(i - 1, max(-1, i - stop), -1):
        s = lines[j].strip()
        if not s:
            continue
        if re.search(r"\d|\(|\)|단위|통계|생산량|^[가-하]\.|^\d\)", s):
            return None
        if re.fullmatch(r"[가-힣ㆍ･·\s]+", s):
            return lines[j]
        return None
    return None


def parse_crop_book(text: str, src: str, book_year: int) -> list[dict]:
    """농작물생산통계 5개년 시도별 표"""
    out = []
    start = None
    for k, l in enumerate(text.split("\n")):
        if re.search(r"연\s*도\s*별\s*,?\s*시\s*[ㆍ･·․]?\s*도\s*별|최근\s*5개년\s*시\s*[ㆍ･·․]?\s*도별", l) and "··" not in l:
            start = k
    if start is None:
        return out
    pages = "\n".join(text.split("\n")[start:]).split("\f")
    prev = None          # 앞쪽에서 이어지는 품목
    for pg in pages:
        lines = pg.split("\n")
        groups, metric, unit = None, None, None
        for i, l in enumerate(lines):
            ys = toks(l, YEAR)
            if len(ys) >= 2 and not re.search(r"[가-힣]", l) and len(re.sub(r"[\d\s]", "", l)) == 0:
                # 연도 줄 → 묶음(연도 순서가 다시 작아지면 새 묶음)
                gs, cur = [], []
                for t in ys:
                    if cur and int(t[2]) <= int(cur[-1][2]):
                        gs.append(cur)
                        cur = []
                    cur.append(t)
                gs.append(cur)
                first = min(int(g[0][2]) for g in gs)
                lab = label_line(lines, i)
                names = [[] for _ in gs]
                if lab and "생산량" not in re.sub(r"\s", "", lab):
                    spans = [(g[0][0], g[-1][1]) for g in gs]
                    for a, b, w in toks(lab):
                        names[assign(spans, a, b)].append(w)
                groups = []
                for q, g in enumerate(gs):
                    nm = "".join(names[q]).replace("ㆍ", "·") or None
                    cont = int(g[0][2]) > first or (q == 0 and prev is not None and nm is None)
                    if cont and prev is not None:
                        ref = prev
                        if nm and (not ref["name"] or ref.get("partial")):
                            ref["name"] = (ref["name"] or "") + nm     # 쪽을 넘어가며 이름이 나뉜 경우(논 | 벼)
                        ref["partial"] = False
                    else:
                        ref = {"name": nm}
                    ref["partial"] = q == len(gs) - 1 and int(g[-1][2]) < max(int(t[2]) for t in ys)
                    groups.append((ref, [int(t[2]) for t in g]))
                prev = groups[-1][0]
                metric = None
                continue
            mu = measure_of(l.strip())
            if mu:
                metric, unit = mu
                continue
            if not groups or not metric:
                continue
            reg, rest = region_of(l)
            if not reg:
                continue
            vals = [t[2] for t in toks(rest, NUM)]
            cols = [(ref, y) for ref, yrs in groups for y in yrs]
            if len(vals) != len(cols):
                continue
            for (ref, y), v in zip(cols, vals):
                out.append({"source": src, "book_year": book_year, "ref": ref, "category": None, "region": reg, "year": y,
                            "metric": metric, "value": num(v), "unit": unit})
    for r in out:
        r["item"] = r.pop("ref")["name"]
    return [r for r in out if r["item"]]


FIELD = re.compile(r"농가수|전체면적|재배면적|수확면적|단\s*수|생산량")
FKEY = {"농가수": ("farms", "호"), "전체면적": ("area_ha", "ha"), "재배면적": ("area_ha", "ha"), "수확면적": ("harvest_ha", "ha"),
        "단수": ("yield_kg10a", "kg/10a"), "생산량": ("prod_t", "t")}


def parse_special_book(text: str, src: str, year: int) -> list[dict]:
    """특용작물 생산실적 시도별·품목별 표(1년)"""
    out = []
    starts = [k for k, l in enumerate(text.split("\n")) if re.search(r"시도별\s*[·･․]?\s*품목별\s*생산실적", l) and "··" not in l and "·  ·" not in l]
    if not starts:
        return out
    lines_all = text.split("\n")
    body = lines_all[starts[-1]:]
    end = next((k for k, l in enumerate(body) if re.match(r"\s*(다|라)\.\s|\s*0?3\s+|\s*연도별\s*생산실적", l) and k > 5), len(body))
    cat = None
    pages = "\n".join(body[:end]).split("\f")
    for pg in pages:
        lines = pg.split("\n")
        groups = None
        for i, l in enumerate(lines):
            mcat = re.match(r"\s*\d\)\s*([가-힣]+)", l)
            if mcat:
                cat = mcat.group(1)
                continue
            fs0 = list(FIELD.finditer(l))
            if len(fs0) >= 3 and "농가수" in l:
                d = disp(l)
                fs = [(d[f.start()], d[f.end()], re.sub(r"\s", "", f.group())) for f in fs0]
                starts_x = [a for a, b, g in fs if g == "농가수"]
                fields = []
                for a, b, g in fs:
                    gi = max([q for q, x in enumerate(starts_x) if x <= a] or [0])
                    fields.append((gi, FKEY[g]))
                lab = None
                for j in range(i - 1, max(-1, i - 5), -1):
                    if lines[j].strip():
                        lab = lines[j] if re.fullmatch(r"[가-힣()（）·･,\-\s]+", lines[j].strip()) else None
                        break
                names = [[] for _ in starts_x]
                if lab:
                    spans = [(min(f[0] for f, (g, _) in zip(fs, fields) if g == q), max(f[1] for f, (g, _) in zip(fs, fields) if g == q))
                             for q in range(len(starts_x))]
                    words = []                     # 간격 2칸 이하 토큰은 한 이름(예: '들 깨', '길경(도라지)-경작지')
                    for a, b, w in toks(lab):
                        if words and a - words[-1][1] <= 2:
                            words[-1] = (words[-1][0], b, words[-1][2] + w)
                        else:
                            words.append((a, b, w))
                    for a, b, w in words:
                        names[assign(spans, a, b)].append(w)
                groups = ["".join(n) or None for n in names], fields
                continue
            if not groups:
                continue
            reg, rest = region_of(l)
            if not reg:
                continue
            vals = [t[2] for t in toks(rest, NUM)]
            names, fields = groups
            if len(vals) != len(fields):
                continue
            for (gi, (metric, unit)), v in zip(fields, vals):
                nm = names[gi]
                if not nm:
                    continue
                if nm == "계":
                    nm = f"{cat} 계" if cat else "계"
                out.append({"source": src, "book_year": year, "item": nm, "category": cat, "region": reg, "year": year,
                            "metric": metric, "value": num(v), "unit": unit})
    return out


# ── KOSIS 내려받기(xlsx) ─────────────────────────────────────────────
KOSIS_SKIP = re.compile(r"조곡|현미|백미__?90\.4|성과수미과수|주산지시군|시군별|표본오차|포기수|볏짚|식량작물_생산량")
REGION_FULL = {"서울특별시": "서울", "부산광역시": "부산", "대구광역시": "대구", "인천광역시": "인천", "광주광역시": "광주", "대전광역시": "대전",
               "울산광역시": "울산", "세종특별자치시": "세종", "경기도": "경기", "강원도": "강원", "강원특별자치도": "강원", "충청북도": "충북",
               "충청남도": "충남", "전라북도": "전북", "전북특별자치도": "전북", "전라남도": "전남", "경상북도": "경북", "경상남도": "경남",
               "제주도": "제주", "제주특별자치도": "제주", "계": "전국", "전국": "전국"}
KMET = [(r"재배면적|^면적|전체면적", "area_ha", "ha"), (r"수확면적", "harvest_ha", "ha"), (r"10a당|단수", "yield_kg10a", "kg/10a"),
        (r"생산량", "prod_t", "t"), (r"농가수", "farms", "호")]


def _kmetric(s: str):
    s = re.sub(r"\s*\(.*?\)\s*$", "", s).strip()
    return next(((k, u) for pat, k, u in KMET if re.search(pat, s)), None)


def parse_kosis(d: Path) -> list[dict]:
    """KOSIS 통계표 내려받기(xlsx). 넓은 표: 1행 = 연도(합친 칸), 2행 = '품목:지표 (단위)', 1열(또는 2열 '소계') = 시도.
    긴 표(특용작물생산현황): 시점·품명(1)·품명(2)·시도(1)·지표 열"""
    import openpyxl
    out = []
    for f in sorted(d.glob("*.xlsx")):
        if KOSIS_SKIP.search(f.name):
            continue
        dl = re.search(r"_(20\d{2})\d{10}\.xlsx$", f.name)
        src = f"KOSIS {re.sub(r'_+\d{14}$', '', f.stem).replace('_', ' ').strip()}"
        try:
            rows = list(openpyxl.load_workbook(f, data_only=True).active.iter_rows(values_only=True))
        except Exception as e:      # noqa: BLE001
            print("  읽기 실패:", f.name, e)
            continue
        n0 = len(out)
        if rows and rows[0][0] == "시점":                       # 긴 표
            hdr = rows[0]
            y = c1 = c2 = None
            for r in rows[1:]:
                y, c1, c2 = (r[0] or y), (r[1] or c1), (r[2] or c2)
                reg = REGION_FULL.get((r[3] or "").strip())
                if not reg or not y or c2 in ("소계",):
                    continue
                for j in range(4, len(hdr)):
                    mu = _kmetric(str(hdr[j]))
                    v = r[j]
                    if mu and isinstance(v, (int, float)):
                        out.append({"source": src, "book_year": 9000 + int(dl.group(1)) if dl else 9000, "item": c2, "category": c1,
                                    "region": reg, "year": int(y), "metric": mu[0], "value": float(v), "unit": mu[1]})
        else:                                                   # 넓은 표
            years, cur = [], None
            for x in rows[0]:
                if x and re.fullmatch(r"\d{4}", str(x).strip()):
                    cur = int(str(x).strip())
                years.append(cur)
            heads = rows[1]
            rice = "미곡" in f.name
            for r in rows[2:]:
                reg = REGION_FULL.get(str(r[0] or "").strip())
                if not reg or (str(rows[0][1] or "").startswith("시도별(2)") and r[1] != "소계"):
                    continue
                for j, h in enumerate(heads):
                    if not h or ":" not in str(h) or years[j] is None:
                        continue
                    item, met = str(h).split(":", 1)
                    if item == "합계":
                        if not rice:
                            continue
                        item = "미곡"
                    mu = _kmetric(met)
                    v = r[j]
                    if mu and isinstance(v, (int, float)):
                        out.append({"source": src, "book_year": 9000 + int(dl.group(1)) if dl else 9000, "item": item.replace(",", "·"),
                                    "category": None, "region": reg, "year": years[j], "metric": mu[0], "value": float(v), "unit": mu[1]})
        print(f"  {f.name}: {len(out) - n0}행")
    return out


def main(d: str, outdir: str, xdir: str | None = None) -> None:
    rows = []
    if xdir:
        rows += parse_kosis(Path(xdir))
    files = sorted(Path(d).glob("*.txt"))
    sp = [f for f in files if "특용" in f.name and len(f.read_bytes()) > 10000]
    latest_sp = max(sp, key=lambda f: int(re.search(r"(20\d\d)", f.name).group(1))) if sp else None
    for f in files:
        if "특용" in f.name and f != latest_sp:
            continue      # 특용작물 시도별 표는 해마다 판이 달라 옛 책은 열 이름이 어긋난다 → 최신 책만(연도별 전국 값은 special_crops_annual.csv)
        t = f.read_text(encoding="utf-8", errors="replace")
        if len(t) < 10000:
            print("  글자 없음(스캔본):", f.name)
            continue
        y = int(re.search(r"(20\d\d)", f.name).group(1))
        if "특용" in f.name:
            r = parse_special_book(t, f.stem, y)
        else:
            r = parse_crop_book(t, f.stem, y)
        print(f"  {f.name}: {len(r)}행, 품목 {len({x['item'] for x in r})}")
        rows += r
    best = {}
    for r in rows:   # 같은 연도·품목·시도·지표: 최신 책
        k = (r["item"], r["region"], r["year"], r["metric"])
        if k not in best or r["book_year"] > best[k]["book_year"]:
            best[k] = r
    keys = ["source", "book_year", "item", "category", "region", "year", "metric", "value", "unit"]
    p = Path(outdir) / "regional_crops.csv"
    with open(p, "w", newline="", encoding="utf-8-sig") as fp:
        w = csv.DictWriter(fp, keys)
        w.writeheader()
        for r in sorted(best.values(), key=lambda r: (r["item"], r["year"], r["metric"], REGIONS.index(r["region"]) if r["region"] in REGIONS else 99)):
            w.writerow({k: r.get(k) for k in keys})
    print(p, len(best), "행")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None)
