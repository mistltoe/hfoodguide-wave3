import json, re
from pathlib import Path
P = Path(__file__).resolve().parent.parent / "dossier.json"
d = json.loads(P.read_text())
S = {s["key"]: s for s in d["sections"]}
changes = []
def rep(key, old, new, why):
    b = S[key]["body"]
    assert old in b, (key, old)
    S[key]["body"] = b.replace(old, new)
    changes.append({"where": f"sections.{key}", "before": old, "after": new, "why": why})

rep("history", "샤미를 쓰고 매운맛에 성질이 차고 떫으며 설사를 일으키는 약재로",
    "샤미를 쓰고(tikta) 매운맛(katu)에 성질이 차고 떫으며 설사를 일으키는 약재로",
    "[5] 원문은 tikta(쓴맛)·katu(매운맛)를 함께 적음 — 쓴맛 누락")
rep("history", "1899년 무렵 라지푸타나(지금의 라자스탄)에 큰 기근이 들었을 때 나무껍질을 먹을거리로 삼아 많은 사람이 살아났다고 전하며, 이 리뷰 원문에는 연도가 '1898-69'로 적혀 있다[5].",
    "라지푸타나(지금의 라자스탄)에 큰 기근이 들었을 때 나무껍질을 먹을거리로 삼아 많은 사람이 살아났다고 전한다. 기근 연도는 리뷰 원문에 '1898-69'로 적혀 있어 정확한 해는 확인하지 못함[5].",
    "[5]는 '1898-69'라고만 씀 — '1899년 무렵'은 출처에 없는 추정이라 뺌")
rep("history", "\n\n인도 라자스탄에서는 1730년 조드푸르 왕의 신하들이 케자를리 마을의 케즈리 나무를 베러 왔을 때 비슈노이 공동체가 이를 막다 많은 사람이 목숨을 잃은 일이 전한다(WebSearch 검색 요약으로만 확인)[26]. 케즈리는 라자스탄의 주 나무(state tree)이며, 2025년에는 태양광 발전 부지에서 이 나무가 베어지는 문제가 보도되었다(WebSearch 검색 요약으로만 확인)[27]. UAE는 2008년 Ghaf를 나라 나무로 정했다[15].",
    "",
    "[26]·[27]은 검색 요약뿐이고 원문이 열리지 않음(이번 검토에서도 접속 불가), PubMed 대체 출처 없음 → 삭제. [15] 전문에 '2008년 나라 나무 지정'이 없음 → 삭제(나라 나무 사실은 overview [3, 4]에 남음)")
rep("cultivation", " 인도 라자스탄에서는 태양광 발전 부지 조성으로 나무가 베어지는 일이 보도되었다(WebSearch 검색 요약으로만 확인)[27].", "",
    "[27] 원문 확인 불가(검색 요약만) → 삭제")
rep("cultivation", "Ghaf나무 밭은 토양 동물·유기탄소·미생물 활성이 높아 가장 좋은 토양 생태계로 평가되었다[25].",
    "Ghaf나무 밭이 가장 좋은 토양 생태계(pedoecosystem)로 평가되었다[25]. 다만 토양 동물에 대한 촉진 효과는 대추나무류(Ziziphus mauritiana) 밭이 가장 컸고, 유기탄소·미생물 활성은 나무 종이 아니라 '나무만 있는 밭'이 '나무+작물 밭'보다 높았다는 비교다[25].",
    "[25] 초록: 토양 동물 촉진 효과 최대는 Z. mauritiana, 유기탄소 등은 나무 단독 vs 나무+작물 비교 — Ghaf 밭이 토양 동물·유기탄소가 높다는 서술은 과장")
rep("cultivation", "파키스탄 건조 평야에서는 Ghaf나무와 Salvadora oleoides가",
    "건조 평야의 사례 연구(파키스탄 연구진)에서는 Ghaf나무와 Salvadora oleoides가",
    "[30] 초록에 조사지가 파키스탄이라고 명시되지 않음(저자 소속만 라호르)")
rep("related_species", "Ghaf나무와 메스키트 계통(Neltuma)은 약 2300만 년 전에 갈라진 것으로 추정되며, 두 유전체 사이의 동질 배열(synteny)은 약하다[3].",
    "유전체 비교에서 Ghaf나무는 남미 메스키트류 P. alba(지금의 Neltuma alba) 계통과 약 2300만 년 전에 갈라진 것으로 추정되었고, 두 유전체 사이의 동질 배열(synteny)은 약하다[3].",
    "[3]의 2300만 년 추정은 Neltuma 전체가 아니라 비교에 쓴 P. alba 유전체와의 분기")

for s in d["sources"]:
    if s["n"] == 29:
        old = s["title"]
        s["title"] = old.replace("27(8):1035", "27(10):1035-6")
        changes.append({"where": "sources[29].title", "before": old, "after": s["title"], "why": "PubMed 서지: 27권 10호 1035-6쪽"})
    if s["n"] == 12:
        old = s["title"]
        s["title"] = old.replace("(초록; PMC 전문 본문은 받지 못함)", "(초록; PMC12297156)")
        changes.append({"where": "sources[12].title", "before": old, "after": s["title"], "why": "PubMed 메타데이터에 PMC12297156 있음; 대조는 초록으로 함"})

# renumber sources: drop unused 26, 27 (and 15 if unused)
text = json.dumps({k: v for k, v in d.items() if k != "sources"}, ensure_ascii=False)
used = set()
for m in re.finditer(r"\[([\d,\s]+)\]", text):
    for x in m.group(1).split(","):
        x = x.strip()
        if x.isdigit(): used.add(int(x))
def collect(o):
    if isinstance(o, dict):
        for k, v in o.items():
            if k == "source" and isinstance(v, list): used.update(v)
            else: collect(v)
    elif isinstance(o, list):
        for v in o: collect(v)
collect({k: v for k, v in d.items() if k != "sources"})
keep = [s for s in d["sources"] if s["n"] in used]
mp = {s["n"]: i + 1 for i, s in enumerate(keep)}
print("removed sources:", sorted(set(s["n"] for s in d["sources"]) - used))
def renum_text(t):
    return re.sub(r"\[([\d,\s]+)\]", lambda m: "[" + ", ".join(str(mp[int(x)]) for x in m.group(1).split(",") if x.strip()) + "]", t)
def walk(o):
    if isinstance(o, dict):
        for k, v in list(o.items()):
            if k == "source" and isinstance(v, list): o[k] = [mp[x] for x in v]
            elif isinstance(v, str): o[k] = renum_text(v)
            else: walk(v)
    elif isinstance(o, list):
        for i, v in enumerate(o):
            if isinstance(v, str): o[i] = renum_text(v)
            else: walk(v)
for k in d:
    if k not in ("sources",): 
        if isinstance(d[k], (list, dict)): walk(d[k])
for s in keep: s["n"] = mp[s["n"]]
d["sources"] = keep
P.write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n")
json.dump(changes, open(Path(__file__).parent / "changes.json", "w"), ensure_ascii=False, indent=1)
print(len(changes), mp)
