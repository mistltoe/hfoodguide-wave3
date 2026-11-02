"""dossier 본문의 'N억 원' 이 식약처 「식품 등의 생산실적」(docs/stats/hf_items.csv, 천원 단위) 값과 맞는지 검사.
그 소재의 원료(materials.json ingredient_patterns)에 해당하는 행만 비교한다.
  맞음: N억 원 × 100,000 ≈ 천원 값
  10배 오류 의심: N × 10,000 ≈ 천원 값
사용: python3 check_units.py [slug ...]   (의심이 있으면 종료 코드 1)"""
import csv
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CSV = HERE.parent / "stats" / "hf_items.csv"
EOK = re.compile(r"([\d,]+(?:\.\d+)?)\s*억\s*원")


def rows_for(mat: dict, text: str) -> list[float]:
    """원료 패턴에 맞는 행 + 본문에 품목명이 그대로 나오는 행(제외어는 적용하지 않음: 복합 원료도 본문에 쓸 수 있다)"""
    pats = mat.get("ingredient_patterns") or []
    flat = text.replace(" ", "").replace("·", "").replace("․", "")
    out = []
    for r in csv.DictReader(CSV.open(encoding="utf-8")):
        it = r["item"]
        key = it.replace(" ", "").replace("·", "").replace("․", "")
        if any(p in it for p in pats) or (len(key) >= 4 and key in flat):
            for k in ("prod_value_k", "sales_k"):
                try:
                    out.append(float(r[k]))
                except ValueError:
                    pass
    return out


def near(vals, x, rel=0.06):
    return any(abs(v - x) <= max(rel * x, 1) for v in vals)


def check(mat: dict) -> list[str]:
    p = HERE / mat["slug"] / "dossier.json"
    if not p.exists():
        return []
    t = json.dumps(json.loads(p.read_text(encoding="utf-8")), ensure_ascii=False)
    vals = rows_for(mat, t)
    out = []
    for m in EOK.finditer(t):
        n = float(m.group(1).replace(",", ""))
        if near(vals, n * 1e4) and not near(vals, n * 1e5):
            out.append(f"{mat['slug']}: '{m.group(0)}' 는 10배 큰 값으로 보임(천원 → 억 원 환산 확인)")
    return out


if __name__ == "__main__":
    mats = json.loads((HERE / "materials.json").read_text(encoding="utf-8"))
    want = set(sys.argv[1:])
    tot = []
    for mt in mats:
        if not want or mt["slug"] in want:
            tot += check(mt)
    print("\n".join(tot) or "단위 의심 없음")
    sys.exit(1 if tot else 0)
