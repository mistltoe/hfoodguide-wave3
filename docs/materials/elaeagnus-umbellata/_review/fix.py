import json, sys
from pathlib import Path
P = Path(__file__).resolve().parent.parent / "dossier.json"
d = json.loads(P.read_text())
changes = []
def sec(key):
    return next(s for s in d["sections"] if s["key"] == key)
def rep(where, obj, field, old, new, why):
    v = obj[field]
    assert v.count(old) == 1, (where, old)
    obj[field] = v.replace(old, new)
    changes.append({"where": where, "before": old, "after": new, "why": why})

o = sec("overview")
rep("sections.overview", o, "body",
    "가을에 붉게 익는 지름 7 mm 안팎의 작은 열매는 새콤달콤하며 날로 먹거나 잼·주스·건과로 만든다[6, 7].",
    "가을에 붉게 익는 길이 7 mm 안팎의 작은 열매는 새콤달콤하며 날로 먹거나 소스·과일 롤·주스로 가공하고, 설탕 시럽 삼투 탈수로 건과를 만드는 연구도 있다[6, 7].",
    "[6]은 열매 '길이 7 mm'라 쓰고 용도로 소스·fruit roll·주스를 듦(잼은 [6]에 없음); 건과는 [7]의 삼투 탈수 연구")

h = sec("history")
rep("sections.history", h, "body",
    "파키스탄 히말라야 지역에서도 민간 약용 식물로 쓰이며, 이 지역 연구진이 열매 추출물과 정유의 효능 연구를 많이 냈다[6, 28].",
    "인도·파키스탄 히말라야 지역에서도 약용 식물로 쓰이며, 파키스탄 연구진이 열매 추출물과 정유의 효능 연구를 냈다[6, 19, 28].",
    "[6]은 인도 북서 히말라야(Pir Panjal) 리뷰이고, 파키스탄 히말라야 분포·전통 사용은 [19]·[28] 초록에 있음; '많이 냈다'는 근거 없음")
rep("sections.history", h, "body",
    "국내에서는 경남 합천에서 기른 열매가 시장에서 거래되어 연구용 시료로 쓰였다[3, 8].",
    "국내 연구에서는 합천 시장에서 산 열매[8]와 합천에서 재배한 열매[3]가 시료로 쓰였다.",
    "[8]은 합천 지역 시장 구입, [3]은 합천 재배 열매를 업체가 제공 — 두 출처 서술을 구분")
rep("sections.history", h, "body",
    "열매를 물로 추출해 분무건조한 추출물은 피부 광노화 동물 연구에 쓰였고, 같은 열매 추출물이 2025년 건강기능식품 개별인정 원료 목록(제2025-59호)에 올랐다[1, 4].",
    "열매를 물로 추출해 분무건조한 추출물은 피부 광노화 동물 연구에 쓰였고[4], 식약처 목록에는 원료 표기가 이 연구 시료와 같은 건강기능식품 개별인정 원료 '보리수나무열매추출물(제2025-59호)'(사용부위 열매)이 올라 있다[1]. 두 원료가 같은 제조 공정인지는 원문에서 확인하지 못함.",
    "[4]는 개별인정을 언급하지 않음; 목록 행 원료명 괄호 표기가 [4] 시료명과 같다는 것만 확인되며 동일 원료·공정 여부는 근거 없음")

b = sec("biology")
rep("sections.biology", b, "body",
    "열매는 둥근 위핵과로 지름이 7 mm 안팎이며",
    "열매는 둥근 위핵과로 길이가 7 mm 안팎이며",
    "[6] 원문은 'spherical in shape with a length of 7 mm'")

c = sec("cultivation")
rep("sections.cultivation", c, "body",
    "미국 농무부의 유전자형 비교에서도 'Brilliant Rose'와 'Jewel'의 항산화 능력이 가장 높아 품종 간 차이가 컸다[12].",
    "미국 농무부의 유전자형 6종 비교에서는 'Brilliant Rose'와 'Jewel'의 항산화 능력이 가장 높아 유전자형에 따라 차이가 있었다[12].",
    "[12] 초록은 6개 유전자형 중 두 품종이 가장 높았다고만 씀; '차이가 컸다'는 과장")
rep("sections.cultivation", c, "body",
    "국내 연구 시료는 경남 합천산 열매였다[3, 8].",
    "국내 연구 시료는 합천산 열매였다[3, 8].",
    "원문은 Hapcheon만 적음(도 표기는 [3] 저자 주소식 'Gyeongsangsam-do' 오기) — 지명만 남김")

p = sec("processing")
rep("sections.processing", p, "body",
    "개별인정 원료와 같은 이름의 열매 추출물(동물 연구 시료)은",
    "개별인정 원료와 표기가 같은 열매 추출물(동물 연구 시료)은",
    "상표형 명칭 언급을 피하고, 같은 원료라는 단정을 피함")

s = sec("safety")
rep("sections.safety", s, "body",
    "보리수나무 잎과 열매는 식약처 「식품원료 목록」에서 제한 없는 사용가능 원료이다[1].",
    "보리수나무 잎과 열매는 식약처 「식품원료 목록」에서 '사용가능부위 : 잎, 열매' 조건의 사용가능 원료이다[1].",
    "I1020 원자료에 사용부위 조건이 있어 '제한 없는'은 부정확")

# compounds
cm = {x["name"]: x for x in d["compounds"]}
rep("compounds.Lycopene.content_text", cm["Lycopene"], "content_text",
    "동결건조 시료, 헥산:아세톤:메탄올 추출 후 분광광도법)[2]",
    "동결건조·분쇄 시료를 헥산:메탄올:아세톤 2:1:1로 추출해 분광광도법 정량, 생/건 기준은 원문에 명시 없음; 초록 하한 35.25는 표의 해안 최솟값 33.15와 다름)[2]",
    "원문 표 단위는 'mg/100 g'뿐이고 기준 표기가 없음; 초록 범위와 표 범위 불일치 명시")
rep("compounds.Catechin.activity_ko", cm["Catechin"], "activity_ko",
    "열매 물 추출물의 주된 페놀 성분; 선충에서 지방 축적 억제(daf-16·atgl-1 의존)[3]",
    "열매 물 추출물의 주된 페놀 성분; 카테킨이 주성분인 동결건조 열매 추출물이 선충에서 지방 축적 억제(daf-16·atgl-1 의존, 카테킨 단독 시험은 아님)[3]",
    "[3]은 추출물(FAOB)로 시험; 카테킨 단독 효과로 읽히지 않게 함")
rep("compounds.Chlorogenic acid.content_text", cm["Chlorogenic acid"], "content_text",
    "열매 클로로포름 분획에서 분리; 함량은 확인하지 못함[19]",
    "열매 추출물에서 분리(초록상 분리 분획은 명시 없음); 함량은 확인하지 못함[19]",
    "[19] 초록은 클로로포름 분획(CHF)과 분리 화합물 I(CGA)을 나란히 적을 뿐 CGA가 그 분획에서 나왔다고 쓰지 않음")
rep("compounds.Rutin.activity_ko", cm["Rutin"], "activity_ko",
    "열매·잎 추출물의 항산화·콜린에스테라아제 억제 활성과 관련[16]",
    "루틴이 검출된 열매·잎 추출물에서 항산화·콜린에스테라아제 억제 활성이 보고됨(루틴 단독 시험 아님, 시험관)[16]",
    "[16] 초록은 추출물 활성과 성분 함량의 일치만 언급; 루틴에 활성을 귀속하지 않음")
rep("compounds.Kaempferol 3-rutinoside.activity_ko", cm["Kaempferol 3-rutinoside"], "activity_ko",
    "사람 각질세포(HaCaT) 증식 실험에 쓰인 잎 성분[14]",
    "사람 각질세포(HaCaT) 증식 실험에 쓰였으나, 증식 촉진은 함께 분리한 다른 화합물 1–5에서만 보고됨[14]",
    "[14] 초록: 화합물 1–6을 시험해 1–5만 증식 촉진; 캠페롤-3-O-루티노사이드는 6번")
rep("compounds.Triterpenoid saponins.activity_ko", cm["Triterpenoid saponins"], "activity_ko",
    "사람 잇몸 섬유모세포에서 활성산소 감소·증식 촉진(세포 실험)[15]",
    "사포닌 자체의 효과는 보고되지 않음; 같은 논문에서 함께 분리한 플라보놀 배당체 1종이 사람 잇몸 섬유모세포에서 활성산소 감소·증식 촉진을 보임(이탈리아 재배 열매, 세포 실험)[15]",
    "[15] 전문: 활성 화합물은 '드문 플라보노이드 배당체(flavonol derivate)'이고 사포닌이 아님")

# assays
a_el = next(x for x in d["assays"] if x["compound"] == "Ellagic acid")
rep("assays.Ellagic acid.rationale", a_el, "rationale",
    "개별인정 원료와 같은 방식의 열매 물 추출물을",
    "개별인정 원료와 표기가 같은 열매 물 추출물을",
    "같은 제조 방식이라는 근거 없음")
a_ly = next(x for x in d["assays"] if x["compound"] == "Lycopene")
old = a_ly["conditions"]["recovery"]
a_ly["conditions"]["recovery"] = ""
changes.append({"where": "assays.Lycopene.conditions.recovery", "before": old, "after": "",
                "why": "85.76%·86.36%는 해바라기유 초음파 추출 수율이지 분석법 회수율이 아님(원문에 회수율 없음); 근거 문장은 rationale로 옮김"})
rep("assays.Lycopene.rationale", a_ly, "rationale",
    "정량은 흡광도법이며 검량·검출한계 값은 원문에 없음[2].",
    "정량은 흡광도법이며 검량·검출한계·회수율 값은 원문에 없음; 해바라기유 초음파 추출 수율은 용매 추출 대비 85.76%·86.36%[2].",
    "recovery 칸에서 옮김")

P.write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n")
Path(__file__).with_name("changes.json").write_text(json.dumps(changes, ensure_ascii=False, indent=1))
print(len(changes))
