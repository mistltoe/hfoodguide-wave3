import json
from pathlib import Path
P = Path(__file__).resolve().parent.parent / "dossier.json"
d = json.loads(P.read_text())
sec = {s["key"]: s for s in d["sections"]}
changes = []
def rep(where, obj, key, old, new, why):
    assert old in obj[key], (where, old)
    obj[key] = obj[key].replace(old, new, 1)
    changes.append({"where": where, "before": old, "after": new, "why": why})

rep("sections.overview", sec["overview"], "body",
    "재배 딸기의 야생 근연종으로 소개된다[1][17]",
    "재배 딸기의 야생 근연종으로 소개된다[17]",
    "[1] 식품원료 목록 행에는 근연종 설명이 없음; [17] 초록이 'wild species related to the cultivated strawberry'로 씀")
rep("sections.biology", sec["biology"], "body",
    "중국의 해발 400–1600 m 실험에서는",
    "해발 400·800·1200·1600 m 네 고도에서 한 실험에서는",
    "[21] 초록에 실험 지역(중국)이 적혀 있지 않음; 고도 4수준만 명시")
rep("sections.cultivation", sec["cultivation"], "body",
    "화분 실험에서 빛과 양분이 늘면 생물량·잎·라멧 수·기는줄기와 꽃 생산이 늘었고, 다른 식물과 경쟁하면 생장이 크게 줄었다[18].",
    "슬로베니아의 화분 실험에서는 빛이 생장에 가장 큰 영향을 주어, 그늘(광합성 유효광 약 10%)에서는 생물량과 라멧·기는줄기 수가 크게 줄었으나 양분을 두 배로 늘린 효과는 유의하지 않았다[18]. 다른 식물과 경쟁하면 지상부 생물량과 잎 수가 줄었지만 라멧·기는줄기·열매 수는 달라지지 않았다[18].",
    "[18] 전문: 양분 증가는 생장을 유의하게 높이지 않았고(Discussion), 경쟁은 지상부·잎 수만 줄이고 라멧·기는줄기·열매 수에는 영향 없음 — 원문보다 과장된 서술 수정")
rep("sections.genetics", sec["genetics"], "body",
    "자외선-B 를 강하게 쬔 어미의 자손에서 총 DNA 메틸화 수준이 25.94% 에서 27.15% 로 높아졌다[25].",
    "자외선-B 를 쬔 어미(UV10 군)의 자손에서 총 DNA 메틸화 수준이 대조군 25.94% 에 비해 27.15% 로 높았다[25]. 초록은 UV10 군을 '낮은' 처리로 적으면서 이 변화가 '높은' 처리 자손에서만 보였다고 써, 처리 강도 표기는 원문에서도 엇갈린다[25].",
    "[25] 초록은 UV5=high, UV10=low 로 정의하면서 27.15% 를 UV10 값으로 제시 — '강하게 쬔' 단정은 원문과 맞지 않아 군 이름으로 바꾸고 불일치를 밝힘")
rep("sections.safety", sec["safety"], "body",
    "동물 연구에서 생쥐에게 메탄올 추출물 100–200 mg/kg 을 먹인 불안·우울 모델 시험이 있으나, 초록에는 안전성 결과가 수치로 제시되지 않았다[34].",
    "파키스탄에서 채집한 전초의 메탄올 추출물을 생쥐 복강에 50–200 mg/kg 주사한 불안·우울 모델 시험이 있고, 같은 논문의 급성 독성 시험에서는 메탄올 추출물 500–2000 mg/kg(투여 경로 명시 없음)에서 24시간 동안 사망·독성 징후가 없었다고 보고했다[34]. 먹여서 한 시험이 아니고 열매 시료도 아니어서 식품 섭취 안전성 근거로 삼기는 어렵다.",
    "[34] 전문: 추출물은 복강(intra-peritoneal) 투여였고 시료는 전초, 투여량 50·100·200 mg/kg; 급성 독성 시험 결과(2000 mg/kg 까지 독성 없음)가 전문에 있음 — '먹인'은 틀림")
rep("sections.processing", sec["processing"], "body",
    "열매는 히말라야 지역에서 생과로 먹는 야생 과일로 분석되었다[6][7].",
    "열매는 히말라야 지역에서 생과로 먹는 야생 과일로 분석되었다[6][7]. 반면 유럽의 생태 연구는 열매가 딸기를 닮았지만 맛이 없다(not palatable)고 적었다[18].",
    "[18] 전문 4.1.1 의 열매 서술을 보태 식용 맥락의 균형을 맞춤")
# compound
for c in d["compounds"]:
    if c["name"] == "Pedunculagin":
        old = c["activity_ko"]; new = "전초 엘라지타닌(합계 252.98 mg/100 g DW) 가운데 가장 많은 7개 피크를 차지하는 무리[3]"
        c["activity_ko"] = new
        changes.append({"where": "compounds[Pedunculagin].activity_ko", "before": old, "after": new,
                        "why": "[3] 은 '기본 구성 단위'를 galloyl-bis-HHDP-glucose 에 대해 썼고, bis-HHDP-glucose 는 7개 피크(1,2,3,11,12,17,18)로 동정됨"})
# source citations
cite = {6: "J Sep Sci. 2021;44(23):4237-54", 13: "Acta Pharm Sin B. 2020;10(10):1846-55",
        15: "Biosci Biotechnol Biochem. 2015;79(8):1246-56", 17: "Plant Dis. 2012;96(5):765",
        25: "Funct Plant Biol. 2022;49(7):600-12", 26: "Pak J Pharm Sci. 2012;25(1):51-8",
        33: "Curr Microbiol. 2025;82(12):554", 34: "PHYTOnutrients. 2022;1(1):48-56"}
short = {6: "J Sep Sci. 2021", 13: "Acta Pharm Sin B. 2020", 15: "Biosci Biotechnol Biochem. 2015",
         17: "Plant Dis. 2012", 25: "Funct Plant Biol. 2022", 26: "Pak J Pharm Sci. 2012",
         33: "Curr Microbiol. 2025", 34: "PHYTOnutrients. 2022"}
for s in d["sources"]:
    n = s["n"]
    if n in cite and s["title"].endswith(short[n]):
        old = s["title"]; s["title"] = old[: -len(short[n])] + cite[n]
        changes.append({"where": f"sources[{n}].title", "before": short[n], "after": cite[n], "why": "PubMed 서지(권·호·쪽) 보충"})
P.write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n")
json.dump(changes, open(Path(__file__).parent / "changes.json", "w"), ensure_ascii=False, indent=1)
print(len(changes))
