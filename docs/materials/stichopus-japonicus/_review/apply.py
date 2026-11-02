import json, re
from pathlib import Path
P = Path(__file__).resolve().parent.parent
d = json.load(open(P/'dossier.json'))
changes = []
def sec(key): return next(s for s in d['sections'] if s['key']==key)
def rep(where, obj, field, old, new, why):
    v = obj[field]
    assert old in v, (where, old)
    obj[field] = v.replace(old, new)
    changes.append({"where": where, "before": old, "after": new, "why": why})

rep("sections.overview", sec('overview'), 'body',
    "동물 원료에 버섯·식물 부위 이름이 붙은 것은 원문 그대로 둔 것이며, 실제로는 원료명(알·창자)이 가리키는 부위로 읽는 것이 맞아 보인다[1].",
    "동물 원료에 버섯·식물 부위 이름('균핵'·'열매')이 붙은 것은 원자료(2026-10-13 받은 I1020 15행)에 실제로 그렇게 적혀 있으며, 원료명(알·창자)과 맞지 않지만 목록에는 그 이유에 대한 설명이 없다[1].",
    "[1] 원자료는 부위 칸 값만 있고 '원료명 부위로 읽는 것이 맞다'는 해석은 출처에 없음 — 원자료 15행을 대조해 사실만 남김")
rep("sections.history", sec('history'), 'body',
    "돌기해삼이 속한 Stichopodidae과 해삼의 내장은 전통적으로 위장 질환 관리에 쓰였다고 소개되었다[24].",
    "중국 본초 문헌에는 돌기해삼을 포함한 Stichopodidae과 몇 종의 내장이 위·십이지장 궤양 같은 위장 질환에 쓰인다고 기록되어 있으며, 한 연구는 칭다오에서 채집한 돌기해삼 내장으로 추출물을 만들어 분석했다[24].",
    "[24] 전문: 'Stichopodidae Viscus'는 이 종과 같은 과의 다른 종(Brandt·Semper 명명 종)을 함께 가리키는 과 단위 약재명 — 다른 종과 섞이지 않게 범위를 밝히고, 실험 시료가 이 종(Selenka)임을 적음")
rep("sections.biology", sec('biology'), 'body',
    "먹이 섭취는 콜레시스토키닌 계열 신경펩타이드가 뒤쪽 장을 수축시키는 방식으로 억제된다고 보고되었다[25].",
    "콜레시스토키닌 계열 신경펩타이드를 오래 주사하면 먹이 섭취가 줄었고, 그 효과의 일부는 뒤쪽 장을 수축시켜 장 비움을 늦추는 데서 온다고 보고되었다[25].",
    "[25] 초록은 'in part by selectively contracting the posterior intestine'(주사 실험, 일부 기전)이라 씀 — 단정 표현 완화")
rep("sections.processing", sec('processing'), 'body',
    "해삼 추출물의 지용성(헥세인) 분획은 쥐 천식 모델에서 기도 염증을 줄였다[16][17].",
    "해삼 추출물을 먹인 쥐에서 알레르기성 기도 염증이 줄었고[17], 그 지용성(헥세인) 분획도 쥐 천식 모델에서 기도 염증을 줄였다[16].",
    "[17]은 헥세인 분획이 아닌 전체 추출물을 경구 투여한 연구 — 두 출처의 내용을 나눔")

C = {c['name']: c for c in d['compounds']}
for nm in ["Fucosylated chondroitin sulfate", "Fucoidan"]:
    rep(f"compounds[{nm}].part", C[nm], 'part', "체벽", "원문 초록에 부위 명시 없음",
        "[11][12] 초록에 부위(체벽) 언급 없음, [11] PMC 전문 없음 — assays 항목과 같게 맞춤")
for nm in ["Eicosapentaenoic acid", "Arachidonic acid", "Palmitoleic acid"]:
    rep(f"compounds[{nm}].part", C[nm], 'part', "체벽 추출물(헥세인 분획)", "해삼 추출물의 헥세인 분획(초록에 부위 명시 없음)",
        "[16] 초록은 'sea cucumber extract'라고만 쓰고 체벽이라 하지 않음")
h = C["Holotoxin A1"]
rep("compounds[Holotoxin A1].content_text", h, 'content_text',
    "사포닌 풍부 분획(SSC) 총함량: 서해 산 15.5 mg/g(최고), 남해 산 8 mg/g(최저)",
    "사포닌 풍부 분획(SSC) 총함량: 서해 산 15.5 mg/g(최고), 남해 산 8 mg/g(최저) — 건물·생물 기준은 초록에 없음",
    "[10] 초록에 mg/g 의 기준(건/생) 표기 없음, 전문 열리지 않음 — 기준 불명 표시")
rep("compounds[Holotoxin A1].activity_ko", h, 'activity_ko',
    "SSC의 주 사포닌으로 확인되었고 항종양 성분으로 추정되었다(세포 실험)[10]",
    "초록은 SSC의 주 사포닌을 Holotoxin A로 적고(키워드는 Holotoxin A1) 항종양 성분일 수 있다고 추정했다(암세포주 실험)[10]",
    "[10] 초록 본문은 'Holotoxin A', 키워드는 'Holotoxin A1' — 원문 표기를 그대로 밝히고 세포 실험임을 명시")
A = d['assays'][2]
rep("assays[Holotoxin].content", A, 'content',
    "SSC 총함량 서해 15.5 mg/g(최고), 남해 8 mg/g(최저)",
    "SSC 총함량 서해 15.5 mg/g(최고), 남해 8 mg/g(최저) (건물·생물 기준은 초록에 없음)",
    "[10] 초록에 함량 기준(건/생) 표기 없음")
json.dump(d, open(P/'dossier.json','w'), ensure_ascii=False, indent=1)
json.dump(changes, open(Path(__file__).parent/'changes.json','w'), ensure_ascii=False, indent=1)
print(len(changes))
