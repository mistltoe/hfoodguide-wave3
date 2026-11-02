import json
p='dossier.json'; d=json.load(open(p))
S={s['key']:s for s in d['sections']}
ch=[]
def rep(where,obj,key,old,new,why):
    assert old in obj[key], (where,old)
    obj[key]=obj[key].replace(old,new); ch.append({"where":where,"before":old,"after":new,"why":why})
rep('sections.overview',S['overview'],'body','동남아시아 열대 바다에서 기르는 κ-카라기난 원료 홍조류다[2, 5]','열대 바다에서 카라기난을 얻으려고 기르는 κ-카라기난 원료 홍조류다[2, 7]','[5](1985 미국 혐기소화 연구)는 재배 지역을 말하지 않음; [7] 초록이 "열대 바다에서 카라기난 생산용으로 상업 재배"라고 씀')
rep('sections.overview',S['overview'],'body','카라기난은 같은 목록에 식품첨가물(B코드)로 따로 올라 있고, 건강기능식품 고시형 원료 표시는 없다[1].','카라기난은 같은 목록에 식품첨가물(B코드)로 따로 올라 있다[1]. 건강기능식품 기능성 원료로 고시된 근거는 확인하지 못함.','I1020 식품원료 목록에는 건강기능식품 고시 여부 항목이 없어 [1]이 뒷받침하지 못함')
rep('sections.history',S['history'],'body','E. spinosum과 E. cottonii의 다당류를 비교했고','E. spinosum과 E. cottonii의 다당류를 다루었고','[4]는 초록이 없어 서지(제목)만 확인됨 — 제목은 두 종의 다당류와 ι-카라기난 구조를 다룬다고만 함')
rep('sections.related_species',S['related_species'],'body','학명의 명명 이력은 공식 분류 데이터베이스에서 확인하지 못함.','명명상으로는 Eucheuma cottonii Weber-van Bosse(1913)가 Kappaphycus cottonii의 기초이명이고, 상업명 \'cottonii\'는 대개 K. alvarezii를 가리킨다는 정리가 있으나, 공식 분류 데이터베이스 원문은 열지 못하고 웹 검색 요약으로만 확인했다[35]. 따라서 K. alvarezii로 표기된 자료를 학명 E. cottonii 원료와 같은 생물의 자료로 단정할 수는 없다.','학명 E. cottonii 와 K. alvarezii 관계의 근거 보강(웹 검색 요약 출처 명시), K. alvarezii 표기 자료를 동일종으로 과장하지 않도록 함')
rep('sections.safety',S['safety'],'body','JECFA는 2015년 영아용 조제식에 카라기난을 1,000 mg/L까지 쓰는 것은 우려가 없다고 결론지었다[2].','JECFA는 2015년 영아용 조제식이나 특수의료용 조제식에 카라기난을 1,000 mg/L까지 쓰는 것은 우려가 없다고 결론지었다고 EFSA 보고서가 인용했다[2].','[2] 원문은 "infant formula or formula for special medical purposes"이며 JECFA 결론을 인용한 것')
rep('sections.safety',S['safety'],'body','EFSA는 노출 추정이 일부 집단의 95백분위에서 잠정 허용량을 최대 약 10배 넘어 안전 우려가 될 수 있다고 보았다[2].','EFSA는 정제된 상표 충성(brand-loyal) 노출 시나리오에서 모든 연령군의 95백분위 노출과 영아·노인을 뺀 연령군의 평균 노출이 잠정 허용량을 넘고, 일부는 최대 약 10배에 이른다고 보았다[2].','[2] 원문: 95백분위는 모든 집단, 평균은 영아·노인 제외 모든 집단에서 초과, 일부 경우 최대 약 10배 — "일부 집단의 95백분위"는 원문과 다름')
rep('sections.safety',S['safety'],'body','인도 연안의 K. alvarezii 등 식용 해조 3종의 중금속은','인도 연구진이 분석한 K. alvarezii 등 식용 해조 3종(K. alvarezii로 표기)의 중금속은','[23] 초록은 채집 지역을 적지 않음(소속 기관만 인도); 이 종이 아닌 K. alvarezii 표기 자료임을 명시')
# aliases
a=d['aliases']; i=a.index('카파피쿠스 알바레지아이'); a[i]='카파피쿠스 알바레지아이(식약처 K. alvarezii 행의 별칭)'
ch.append({"where":"aliases","before":"카파피쿠스 알바레지아이","after":a[i],"why":"[1] 로컬 원자료에서 이 별칭은 학명 E. cottonii 행이 아니라 K. alvarezii 행(수산물)에만 있음"})
# sources
src={s['n']:s for s in d['sources']}
upd={10:("Food Funct 2019 (초록)","Food Funct 2019;10(9):5697-706 (초록)"),29:("J Cosmet Dermatol 2020 (초록)","J Cosmet Dermatol 2021;20(3):993-1001 (초록)"),31:("Int J Biol Macromol 2022 (초록)","Int J Biol Macromol 2022;210:752-8 (초록)"),32:("Bioresour Technol 2022 (초록)","Bioresour Technol 2022;364:128136 (초록)")}
for n,(o,nw) in upd.items():
    if o in src[n]['title']:
        src[n]['title']=src[n]['title'].replace(o,nw); ch.append({"where":f"sources[{n}]","before":o,"after":nw,"why":"PubMed 서지와 대조해 권·쪽 보충"})
d['sources'].append({"n":35,"title":"Kappaphycus (PROSEA) 및 분류 정리 페이지 — Eucheuma cottonii Weber-van Bosse 1913 = Kappaphycus cottonii 기초이명, 상업명 'Cottonii'는 대개 K. alvarezii (WebSearch 요약으로만 확인; 원문 미열람, AlgaeBase 직접 확인 못함)","url":"https://uses.plantnet-project.org/en/Kappaphycus_(PROSEA)","publisher":"PROSEA(Plant Resources of South-East Asia) — 웹 검색 요약","accessed":"2026-11-02"})
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(ch,open('_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(ch))
