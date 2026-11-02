"""2024 특용작물 생산실적(농식품부) 텍스트 → 품목별 연도별 면적·생산량 CSV.

입력: pdftotext -layout 결과(docs/refs/_text/★+2024+특용작물+생산실적_….pdf.txt)
출력: docs/stats/special_crops_annual.csv  (category,item,year,area_ha,harvest_ha,yield_kg10a,prod_t)
      docs/stats/special_crops_2024.csv    (category,item,farms,area_ha,harvest_ha,prod_t)  ← '품목별 생산실적' 표
방법: '연도별 생산실적' 쪽마다 머리글(’YY)과 단위 줄(ha ha kg/10a M/T)의 글자 위치로 열을 정하고,
      오른쪽 정렬된 숫자를 가장 가까운 열 끝에 붙인다(빈 칸이 있어도 열이 밀리지 않게).
사용: python -I docs/stats/parse_special_crops.py <텍스트파일> [출력폴더]
"""
import csv
import re
import sys
from pathlib import Path

NUM = re.compile(r"(?<![\w.])-?[\d,]+(?:\.\d+)?(?![\w.])")
FIELDS = ("area_ha", "harvest_ha", "yield_kg10a", "prod_t")


def num(s):
    s = s.replace(",", "")
    return float(s) if s not in ("", "-") else None


def name_of(line):
    m = NUM.search(line)
    raw = line[: m.start()] if m else line
    return re.sub(r"\s+", "", raw).lstrip("-")


def section_cat(line, cur):
    for key, cat in (("유지작물", "유지"), ("섬유작물", "섬유"), ("기호작물", "기호"), ("약용작물", "약용"), ("버섯", "버섯"), ("기타특용", "기타")):
        if key in line.replace(" ", ""):
            return cat
    return cur


def parse_annual(lines):
    out, i, cat = [], 0, None
    start = next(k for k, l in enumerate(lines) if l.strip() == "2. 연도별 생산실적")
    end = next(k for k, l in enumerate(lines) if k > start and "가격동향" in l.replace(" ", "") and len(l.strip()) < 30)
    i = start
    while i < end:
        l = lines[i]
        years = re.findall(r"’(\d\d)", l)
        if years and not NUM.sub("", l).replace("’", "").strip():
            ys = [2000 + int(y) if int(y) < 50 else 1900 + int(y) for y in years]
            # 단위 줄 찾기(머리글 아래 6줄 안)
            unit_line = next((lines[j] for j in range(i + 1, min(i + 8, end)) if re.search(r"kg/(10a|㎡)", lines[j])), None)
            if not unit_line:
                i += 1
                continue
            rights = [mt.end() for mt in re.finditer(r"ha|kg/10a|kg/㎡|M\s*/?\s*T|/T", unit_line)]
            # 'M' 과 '/T' 가 두 줄로 갈린 경우 '/T' 위치만 남는다 → 열 수 = 4×연수 가 되도록 정리
            if len(ys) > 1 and ys[-1] - ys[0] != len(ys) - 1:      # 책 머리글 오타(’20 ’21 ’23) → 연속 연도로
                ys = list(range(ys[0], ys[0] + len(ys)))
            if not ys or len(rights) % len(ys) or len(rights) // len(ys) not in (3, 4):
                i += 1
                continue
            per = len(rights) // len(ys)
            fields = FIELDS if per == 4 else ("area_ha", "yield_kg10a", "prod_t")
            j = i + 1
            while j < end and not re.search(r"’\d\d", lines[j]) and "- " not in lines[j][-12:]:
                row = lines[j]
                if re.search(r"kg/(10a|㎡)", row) or "전체면적" in row or not row.strip():
                    j += 1
                    continue
                cat = section_cat(row, cat)
                nm = name_of(row)
                if not nm or nm.startswith("(") or nm.startswith("*"):
                    j += 1
                    continue
                toks = [(mt.end(), mt.group()) for mt in NUM.finditer(row) if mt.start() > len(row) - len(row.lstrip()) + 2]
                vals = [[None] * per for _ in ys]
                if len(toks) == per * len(ys):       # 빈 칸 없는 줄은 순서대로
                    for k, (e, t) in enumerate(toks):
                        vals[k // per][k % per] = num(t)
                    toks = []
                for e, t in toks:
                    k = min(range(len(rights)), key=lambda c: abs(rights[c] - e))
                    if abs(rights[k] - e) <= 6:
                        vals[k // per][k % per] = num(t)
                for y, v in zip(ys, vals):
                    if any(x is not None for x in v):
                        out.append({"category": cat, "item": nm, "year": y, **dict(zip(fields, v))})
                j += 1
            i = j
            continue
        i += 1
    return out


def parse_2024(lines):
    out, cat = [], None
    for l in lines[:2860]:
        if l.strip().startswith("▹"):
            cat = section_cat(l, cat)
        m = re.match(r"\s*(\S.*?)\s{2,}([\d,]+)\s+([\d,]+)\s+([\d,]+)\s+([\d,]+)\s*$", l)
        if m and cat and not re.search(r"\d", m.group(1)):
            out.append({"category": cat, "item": re.sub(r"\s+", "", m.group(1)), "farms": num(m.group(2)), "area_ha": num(m.group(3)),
                        "harvest_ha": num(m.group(4)), "prod_t": num(m.group(5))})
        if "시도별" in l.replace(" ", "") and out:
            break
    return out


def main(src, outdir):
    lines = Path(src).read_text(encoding="utf-8").splitlines()
    ann = parse_annual(lines)
    now = parse_2024(lines)
    od = Path(outdir)
    for name, rows, cols in (("special_crops_annual.csv", ann, ("category", "item", "year") + FIELDS),
                             ("special_crops_2024.csv", now, ("category", "item", "farms", "area_ha", "harvest_ha", "prod_t"))):
        with open(od / name, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=cols)
            w.writeheader()
            w.writerows(rows)
    print(len(ann), "annual rows,", len({r["item"] for r in ann}), "items; 2024 table", len(now))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else Path(__file__).parent)
