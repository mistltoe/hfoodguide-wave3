import json
from pathlib import Path
P = Path(__file__).resolve().parent.parent / "dossier.json"
d = json.loads(P.read_text())
changes = []
def sec(key):
    return next(s for s in d["sections"] if s["key"] == key)
def rep(obj, field, old, new, where, why):
    assert obj[field].count(old) == 1, (where, old)
    obj[field] = obj[field].replace(old, new)
    changes.append({"where": where, "before": old, "after": new, "why": why})

rep(sec("overview"), "body", "연구자들은 몸길이별로 섭취 횟수를 조절하라고 권고했다[5, 15].",
    "연구자들은 몸길이별로 섭취 횟수를 조절하라고 권고했다[5].", "sections.overview",
    "[15](2003 리뷰) 초록에는 몸길이별 섭취 횟수 권고가 없음 — 권고는 [5]만의 내용")
rep(sec("history"), "body", "농어류·그루퍼 같은 비싼 생선과 혼동되거나 대체될 수 있어",
    "그루퍼 같은 비싼 생선의 대체어로 쓰일 수 있어", "sections.history",
    "[24]·[25]는 그루퍼·난파선고기와의 판별만 다룸 — '농어류'는 근거 없음")
rep(sec("cultivation"), "body", "나일선농어의 최대 몸길이가 56.1% 줄었다[14].",
    "나일선농어의 몸길이 생활사 지표가 56.1% 줄었다[14].", "sections.cultivation",
    "[14] 초록(PubMed)에서 감소한 지표의 아래첨자가 깨져 평균·최대 몸길이 중 어느 것인지 확인할 수 없음 — '최대'를 지움")
rep(sec("processing"), "body", "얼음에 저장해 상한 생선에서는 분리균의 90%를 차지한 슈도모나스가 주된 원인 세균으로 지목되었다[21].",
    "얼음에 저장해 상한 생선에서는 분리균의 90%가 슈도모나스였으나, 그중 부패 냄새를 낸 균주는 74주 중 13주였다[21].",
    "sections.processing", "[21] 초록: 얼음 저장 분리균 90%가 슈도모나스지만 부패취 생성은 일부(13/74)뿐이고 부패균을 생화학적으로 구별 못함 — '주된 원인'은 과장")
rep(sec("processing"), "body", "비늘에서는 탈아세틸화도 77.8–79.1% 범위의 키토산이 분리되었다[32].",
    "비늘에서도 키토산이 분리되었으며, 이 연구에서 버섯·비늘·바구미로 얻은 키토산의 탈아세틸화도는 77.8–79.1%였다[32].",
    "sections.processing", "[32] 초록의 77.8–79.1%는 세 원료 키토산 전체 범위이며 비늘만의 값이 아님")
rep(sec("genetics"), "body", "원산지인 이집트 개체 서열과 99% 일치해",
    "모식 산지(type locality)인 이집트에서 채집된 개체의 부분 유전자 서열과 99% 일치해", "sections.genetics",
    "[11] 전문: 'Egypt, the type locality' — 원산지가 아니라 모식 산지, 비교 대상은 부분 유전자")
rep(sec("safety"), "body", "앨버트호에서는 뱃살 지방에 수은이 더 많이 쌓였고 취약군 위해지수가 2.05였다[19].",
    "앨버트호 어촌의 작은 개체를 조사한 연구에서는 나일선농어 근육 수은 중앙값이 0.024 mg/kg(습중량)이었고, 근육 시료의 15%와 뱃살 시료의 22%가 이 연구가 비교한 FAO/WHO 값(0.05 mg/kg)을 넘었다[19].",
    "sections.safety", "[19] 전문(PMC5059776)에 위해지수 2.05가 없고, 뱃살 수은은 틸라피아보다 많았으나 유의차 없음 — 원문 표 4와 본문 값으로 교체")
rep(sec("safety"), "body", "생선 알레르기 환자 12명 중 7명이 에놀레이스 3에 감작되어 있었다[20].",
    "생선 알레르기 환자 12명 중 7명이 에놀레이스 3에 감작되어 있었다(아토피 대조군에서도 감작이 관찰됨)[20].",
    "sections.safety", "[20] 초록: 아토피 대조군도 감작 — 단서 추가")

C = {c["name"]: c for c in d["compounds"]}
rep(C["Lysine"], "activity_ko", "곡류에 부족한 필수아미노산으로, 비교 어종 중 가장 높았다[2]",
    "비교한 다섯 어종 중 가장 높았다[2]", "compounds.Lysine.activity_ko", "'곡류에 부족' 은 [2]에 없는 내용")
for n in ["Eicosapentaenoic acid", "Docosahexaenoic acid", "alpha-Linolenic acid", "Linoleic acid", "Oleic acid", "Palmitic acid"]:
    old = C[n]["content_text"]
    new = old.replace("mg/g(나세르호", "mg/g(기준(습·건·지질) 원문 미기재, 나세르호", 1)
    assert new != old, n
    C[n]["content_text"] = new
    changes.append({"where": f"compounds.{n}.content_text", "before": old, "after": new,
                    "why": "[2] 표 3 단위는 mg/g 뿐이고 기준이 없음(총지방산 90.15 mg/g 가 지방 3.47%보다 커서 습중량 기준일 수 없음)"})
rep(C["Mercury"], "content_text", "나세르호 0.016 ± 0.001 μg/g[2]", "나세르호 0.016 ± 0.001 μg/g 습중량[2]",
    "compounds.Mercury.content_text", "[2] 표 5 는 습중량 기준")

A = {a["compound"]: a for a in d["assays"]}
rep(A["Total mercury"]["conditions"], "standard", "시료 10개마다 인증표준물질(DORM-3, DOLT-4)과 중복 시료 분석",
    "시료 10개마다 인증표준물질(DORM-3, DOLT-4) 분석, 중복 시료 4쌍", "assays.Total mercury.conditions.standard",
    "[5] 전문: 중복 시료는 런 전체에 4쌍, 10개마다는 인증표준물질")

N = d["nutrients"][1]
rep(N, "basis", "습중량 100 g당, 논문 표 2·표 3의 0일 값[3]",
    "근성분은 습중량 g/100 g(표 2), 무기질은 mg/100 g(표 3, 기준 미기재), 모두 0일 값[3]",
    "nutrients[1].basis", "[3] 표 3 무기질은 기준(습·건) 표기가 없음")

P.write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n")
Path(__file__).with_name("changes.json").write_text(json.dumps(changes, ensure_ascii=False, indent=1))
print(len(changes))
