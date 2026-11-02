import json, re, sys
P = sys.argv[1]
d = json.load(open(P, encoding="utf-8"))
S = {x["key"]: x for x in d["sections"]}

def rep(key, old, new):
    b = S[key]["body"]
    assert old in b, (key, old[:40])
    S[key]["body"] = b.replace(old, new)

# history
rep("history", "1983년에는 하와이 근해 황다랑어·눈다랑어의 총수은 함량을 다룬 논문이 나왔다[61]. ", "")
rep("history", "생식소자극호르몬 두 종류(GTH I·II)를 정제해 경골어류 생식소자극호르몬이 두 가지임을 확인했다[58]",
    "생식소자극호르몬 두 종류(GTH I·II)를 정제해, 고등한 해산 경골어류인 다랑어에서도 생식소자극호르몬이 두 가지임을 확인했다[58]")
rep("history", "몸 전체 열전도도를 100배(두 자릿수) 바꿀 수 있음을 보여, 체온 조절 연구의 대표 사례가 되었다[2]",
    "몸 전체 열전도도를 두 자릿수(약 100배) 바꿀 수 있음을 보였다[2]")
# genetics
rep("genetics", "중부 태평양의 자어·준성어 348마리를 2bRAD 염기서열로 분석한 2026년 연구에서는 눈다랑어 안에서 집단 구조가 나타나지 않았다[19]",
    "중부 태평양에서 7년간 채집한 가다랑어·황다랑어·눈다랑어 자어·준성어 348마리(세 종 합계)를 2bRAD 염기서열로 분석한 2026년 연구에서는 눈다랑어 안에서 집단 구조가 나타나지 않았다[19]")
# cultivation
rep("cultivation", "국내에서는 원양어업으로 눈다랑어를 잡으며, 해양수산부·통계청 발표를 인용한 보도에 따르면 2023년 약 2.5만 톤, 2024년(잠정) 약 2만2000톤이었다(검색 결과 요약으로만 확인)[44, 45]. 해양수산부·통계청 원자료(KOSIS 어업생산동향조사)는 이 환경에서 열 수 없어 확인하지 못함.",
    "국내 원양어업의 눈다랑어 생산량은 해양수산부·통계청 원자료(어업생산동향조사)를 이번 대조에서 열지 못해 확인하지 못함.")
# safety
rep("safety", "눈다랑어는 깊은 수층의 먹이를 먹어 수은이 많이 쌓이는 종이다[8].",
    "눈다랑어는 깊은 수층의 먹이를 먹어 수은이 많이 쌓이는 종이다[8, 27].")
rep("safety", "이 논문들은 성인 주 145–170 g 이하 섭취를 제안했다[25, 26]. 국내에서는 다랑어류의 메틸수은을 1.0 ppm으로 관리한다(검색 결과 요약으로만 확인)[43].",
    "이 논문들은 주당 섭취 상한으로 체중 60 kg 성인 150 g[25], 대만 성인 남녀 170 g·145 g[26]을 제안했다. 국내 식품 기준의 다랑어류 메틸수은 기준 원문은 이번 대조에서 열지 못해 확인하지 못함.")
rep("safety", "다랑어는 히스타민 식중독 위험 어종이며, 눈다랑어 흰살에서는 저장 중 히스타민이 늘어 히스티딘과 상관을 보였다[24, 32].",
    "눈다랑어 흰살에서는 저장 중 히스타민 등 생체아민이 늘었고 히스타민은 히스티딘과 상관을 보였다[24]. 12 °C에 저장한 눈다랑어 살에서는 히스타민 생성균이 자라고 히스타민이 쌓일 수 있어, 이를 막는 처리가 연구되었다[33].")
rep("safety", "눈다랑어 근육 콜라겐은 환자 혈청 8개 중 5개와 반응한 어류 알레르겐이고, 살 속 고래회충 알레르겐(Ani s 4)은 통조림 가열 뒤에도 일부 남았다[34, 35].",
    "눈다랑어 근육 콜라겐은 환자 혈청 8개 중 5개와 반응한 어류 알레르겐이다[34]. 고래회충 유충을 인위로 감염시킨 눈다랑어·황다랑어 살에서는 고래회충 알레르겐(Ani s 4)이 통조림 가열 뒤에도 일부 남았다[35].")

# compounds
for c in d["compounds"]:
    if c["name"] == "Docosahexaenoic acid":
        c["activity_ko"] = "인도양 열대 다랑어 3종(눈다랑어·황다랑어·가다랑어) 조직의 극성·중성 지질 모두에서 주 지방산이었다(3종 공통 결과)[22]"
    if c["name"] == "Histamine":
        c["activity_ko"] = "히스타민 식중독 원인 물질 — 눈다랑어 흰살에서 히스티딘과 상관[24]"
        c["source"] = [24, 53]
    if c["name"] == "Anserine":
        c["activity_ko"] = "눈다랑어 흰살과 붉은살의 안세린 함량이 달랐다(수치는 초록에 없음)[24]"
        c["source"] = [24]
        c["content_text"] = "수치는 초록에 없음(흰살·붉은살 함량 차이 보고)[24]"
# assays
for a in d["assays"]:
    if a["compound"] == "Histamine":
        a["rationale"] = a["rationale"].replace("[31, 32]", "[31]").replace("다랑어 등 붉은살 생선의", "붉은살 생선의")
# production
d["production"] = []

# renumber sources
drop = {23, 32, 43, 44, 45, 61}
keep = [s for s in d["sources"] if s["n"] not in drop]
m = {s["n"]: i + 1 for i, s in enumerate(keep)}
for s in keep:
    s["n"] = m[s["n"]]
d["sources"] = keep
REF = re.compile(r"\[(\d+(?:\s*,\s*\d+)*)\]")
def fix(t):
    if not isinstance(t, str):
        return t
    def r(mo):
        nums = [int(x) for x in re.split(r"\s*,\s*", mo.group(1))]
        for n in nums:
            assert n in m, ("dropped ref still used", n, t[:60])
        return "[" + ", ".join(str(m[n]) for n in nums) + "]"
    return REF.sub(r, t)
for sec in d["sections"]:
    sec["body"] = fix(sec["body"])
for arr in ("compounds", "markers", "assays", "nutrients", "production", "world", "gi", "orgs"):
    for x in d.get(arr) or []:
        if "source" in x:
            x["source"] = [m[n] for n in x["source"]]
        for f in ("content_text", "activity_ko", "note", "content", "rationale", "spec"):
            if f in x:
                x[f] = fix(x[f])
json.dump(d, open(P, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("ok", len(keep))
