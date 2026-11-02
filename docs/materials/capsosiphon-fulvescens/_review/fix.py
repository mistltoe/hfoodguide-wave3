import json, sys
from pathlib import Path
P = Path(__file__).resolve().parent.parent / "dossier.json"
d = json.loads(P.read_text(encoding="utf-8"))
changes = []
def sec(k): return next(s for s in d["sections"] if s["key"] == k)
def rep(where, obj, key, old, new, why):
    v = obj[key]
    assert old in v, (where, old)
    obj[key] = v.replace(old, new)
    changes.append({"where": where, "before": old, "after": new, "why": why})

rep("sections.overview", sec("overview"), "body",
    "엽록소 분해물(페오포바이드 a), 당단백질이 분리되었다[12–15, 22]",
    "엽록소 분해물(페오포바이드 a), 단백질(OEE1)·당단백질이 분리되었다[12–15, 21, 22]",
    "[15] 는 당단백질이 아니라 산소 발생 촉진 단백질 1(OEE1)을 정제한 연구 — 당단백질 근거는 [21]·[22]")
rep("sections.history", sec("history"), "body",
    "목·과 수준의 분류가 오랫동안 논란이었다[3]",
    "목 아래(과·속) 수준의 분류와 계통 관계가 논란이었다[3]",
    "[3] 원문은 'classification and phylogenetic relationships ... below the order level are controversial'")
rep("sections.safety", sec("safety"), "body",
    "쥐 먹이에 매생이를 1–2% 섞어 먹인 실험에서는 체중이 대조군과 다르지 않았다[28].",
    "아족시메테인으로 대장 전암 병변을 유도한 쥐에게 매생이를 먹이의 1–2%로 섞어 먹인 실험에서 군 간 체중 차이는 없었으나, 이는 독성 시험이 아니다[28].",
    "[28] 은 AOM 유도 대장암 모델 실험으로 체중 비교만 보고 — 안전성 근거로 읽히지 않게 조건을 밝힘")
rep("sections.safety", sec("safety"), "body",
    "무작위·이중눈가림·위약대조 교차시험이 있다[27].",
    "무작위·이중눈가림·위약대조 교차시험이 있다[27]. 이 논문은 앞서 수행한 시험 자료를 건강 점수 모델로 다시 분석한 것이다[27].",
    "[27] Methods: 'The study has been described in detail previously' — 2차 분석임을 밝힘")
c = next(x for x in d["compounds"] if x["name"].startswith("Glycoprotein"))
rep("compounds[Glycoprotein].activity_ko", c, "activity_ko",
    "노화 쥐에 15 mg/kg/일 4주 경구 투여 시 공간 기억 저하 완화(동물) [22, 23]",
    "노화 쥐[22]와 사회적 고립을 겪은 노화 쥐[23]에 Cf-hGP 15 mg/kg/일 4주 경구 투여 시 공간 기억 저하 완화(동물) [22, 23]",
    "[23] 은 사회적 고립 유발 인지 저하 모델 — 모델 차이를 밝힘")
c = next(x for x in d["compounds"] if x["name"] == "24-Methylenecholesterol")
rep("compounds[Chalinasterol].activity_ko", c, "activity_ko",
    "생쥐에 37.5 µg/kg 복강 주사 시",
    "생쥐에 37.5 µg/kg 격일 복강 주사 시",
    "[16] Methods: 'once every 2 days' i.p.")
a = d["assays"][0]
cond = a["conditions"]
for k, new in (("column", "COSMOSIL Sugar-D(Nacalai Tesque) — D-만노스·D-자일로스"),
               ("mobile_phase", "80%(v/v) 아세토니트릴 수용액"),
               ("flow", "1.0 mL/min"), ("temp", "30 °C")):
    changes.append({"where": f"assays[0].conditions.{k}", "before": cond[k], "after": new,
                    "why": "[6] 에서 Aminex HPX-87H(5 mM H₂SO₄, 0.6 mL/min, 35 °C)는 유기산(젖산·아세트산) 정량 조건 — 단당 분석 항목에서 뺌"})
    cond[k] = new
a2 = d["assays"][1]
changes.append({"where": "assays[1].conditions.sample_prep", "before": a2["conditions"]["sample_prep"], "after": "",
                "why": "[7] 초록의 TFA 가수분해는 2010년 [8] 분석 방법 서술 — 2015년 재분석의 전처리는 전문 미확인"})
a2["conditions"]["sample_prep"] = ""
o = d["orgs"][0]
changes.append({"where": "orgs[0].url", "before": o["url"], "after": "",
                "why": "국립수산물품질관리원 첫 화면일 뿐 단체 누리집이나 등록 기록 페이지가 아님 — 단체 존재 근거는 [2] 지리적표시 등록 현황(로컬 gi.json: 제11호, 등록 단체)으로만 확인"})
o["url"] = ""
P.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
json.dump(changes, open(Path(__file__).parent / "changes.json", "w"), ensure_ascii=False, indent=1)
print(len(changes))
