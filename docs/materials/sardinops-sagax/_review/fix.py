import json
from pathlib import Path
P=Path(__file__).resolve().parent.parent/"dossier.json"
d=json.loads(P.read_text())
changes=[]
def rep(where,obj,key,old,new,why):
    s=obj[key]
    assert old in s,(where,old)
    obj[key]=s.replace(old,new,1)
    changes.append({"where":where,"before":old,"after":new,"why":why})
sec={s["key"]:s for s in d["sections"]}
rep("sections.overview",sec["overview"],"body",
 "S. sagax melanostictus(아종)로 적힌다[1, 7, 11].",
 "S. sagax melanostictus(아종)로 적힌다[7, 11].",
 "[1](식약처 목록)은 세 학명을 함께 적을 뿐 종·아종 처리를 말하지 않음 — 근거는 [7]·[11]")
rep("sections.biology",sec["biology"],"body",
 "걸러 먹는 습성 때문에 태평양정어리는 실험에서 바닷물 속 톡소포자충(Toxoplasma gondii) 난포낭을 걸러 들였고, 노출 개체의 66%(40/61)가 PCR 양성이었다[35].",
 "걸러 먹는 습성 때문에 태평양정어리는 실험에서 바닷물 속 톡소포자충(Toxoplasma gondii) 난포낭을 걸러 들였고, 함께 실험한 북방멸치(Engraulis mordax)를 합친 노출 개체의 66%(40/61)가 PCR 양성이었다[35].",
 "[35] 초록의 66%(40/61)는 멸치와 정어리를 합친 전체 노출 어류 수치 — 정어리만의 값이 아님")
rep("sections.safety",sec["safety"],"body",
 "정어리는 고시형 원료가 아니어서 식약처가 종 단위로 정한 섭취 주의사항은 없다[1, 3]. 검색 요약으로만 확인한 정책브리핑 기사에 따르면 정어리 같은 등푸른생선을 냉동·염장·건조 등으로 처리한 경우 히스타민 기준은 200 mg/kg 이하이다[31]. 일본산 정어리(Japanese pilchard) 생살을 10 °C에 두면",
 "정어리는 고시형 원료가 아니어서 식약처가 종 단위로 정한 섭취 주의사항은 없다[1, 3]. 다만 정어리 기름을 원재료로 만든 'EPA 및 DHA 함유 유지' 건강기능식품에는 고시 주의사항(항응고제·항혈소판제·혈압강하제 등 의약품 복용 시 전문가 상담, 개인에 따라 피부 관련 이상반응 가능, 이상사례 시 섭취 중단)이 붙는다[3]. 옛 식약청 시기의 「식품의 기준 및 규격」 개정 행정예고를 다룬 정책브리핑 기사는 정어리 등 등푸른생선을 통조림·냉동·염장·건조·절단한 경우 히스타민 기준을 200 mg/kg 이하로 둔다고 적었으나, 이는 검색 요약으로만 본 것이고 현행 고시 원문 조문은 확인하지 못함[31]. 일본 슈퍼마켓에서 산 정어리(영명 Japanese pilchard, 원문 학명은 도구 출력에서 빠져 확인 못함) 생살을 10 °C에 두면",
 "[31]은 원문을 열지 못한 검색 요약·행정예고 시기 기사라 현행 기준처럼 단정할 수 없음; [18] 시료는 도코로자와 슈퍼마켓 구입품으로 '일본산'은 원문에 없음; 고시 2-16 주의사항 보강")
for c in d["compounds"]:
    if c["name"]=="Histamine":
        rep("compounds.Histamine.content_text",c,"content_text","국내 기준 200 mg/kg 이하(검색 요약)[31]","국내 기준 200 mg/kg 이하라는 정책브리핑 기사(검색 요약만, 현행 고시 원문 미확인)[31]","[31] 지위 약화")
    if c["name"]=="Eicosapentaenoic acid":
        rep("compounds.EPA.content_text",c,"content_text","오스트레일리아 정어리 살과 내장 각각 1,000 mg/100 g 조직 이상[14]","오스트레일리아 정어리(영명 'Australian sardine'만 확인, 학명은 도구 출력에서 빠짐) 살과 내장 각각 1,000 mg/100 g 조직 이상[14]","[14] 학명 미확인 — 영명 귀속임을 표시")
    if c["name"]=="Docosahexaenoic acid":
        rep("compounds.DHA.content_text",c,"content_text","오스트레일리아 정어리 살과 내장 각각 1,000 mg/100 g 조직 이상[14]","오스트레일리아 정어리(영명만 확인) 살과 내장 각각 1,000 mg/100 g 조직 이상[14]","[14] 학명 미확인 — 영명 귀속임을 표시")
a0,a1=d["assays"][0],d["assays"][1]
rep("assays[0].part",a0,"part","오스트레일리아 정어리 4마리","오스트레일리아 정어리(Australian sardine) 4마리, 발리나 수산협동조합 구입 — 학명은 도구 출력에서 빠져 영명으로만 확인","[14] 원문 학명 미확인")
rep("assays[0].conditions.sample_prep",a0["conditions"],"sample_prep","0.5 M 메탄올 용액 1.5 mL","0.5 M NaCl-메탄올 용액 1.5 mL","원문 'NaCl in methanol solution (0.5 M, 1.5 mL)'")
rep("assays[1].part",a1,"part","일본산 정어리(Japanese pilchard)","일본 슈퍼마켓에서 산 정어리(Japanese pilchard)","원문은 사이타마현 도코로자와 슈퍼마켓 구입이라고만 적음 — 산지 미기재")
for s in d["sources"]:
    if s["n"]==31:
        old=s["title"]
        s["title"]="옛 식품의약품안전청 「식품의 기준 및 규격」 개정 행정예고 관련 정책브리핑 기사 — 고등어·참치·연어·꽁치·청어·멸치·삼치·정어리 등 등푸른생선을 통조림·냉동·염장·건조·절단한 경우 히스타민 200 mg/kg 이하 (WebSearch 검색 결과 요약으로만 확인, 이 환경에서 원문 페이지와 현행 고시 원문은 열지 못함)"
        changes.append({"where":"sources[31].title","before":old,"after":s["title"],"why":"검색 요약상 옛 식약청 시기 행정예고 기사 — 발행 기관·성격을 바로 적음"})
P.write_text(json.dumps(d,ensure_ascii=False,indent=1))
json.dump(changes,open(Path(__file__).parent/"changes.json","w"),ensure_ascii=False,indent=1)
print(len(changes))
