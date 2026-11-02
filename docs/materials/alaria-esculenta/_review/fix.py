import json, sys
p='/home/user/hfoodguide-wave3/docs/materials/alaria-esculenta/dossier.json'
d=json.load(open(p))
S={s['key']:s for s in d['sections']}
changes=[]
def rep(key, old, new, why):
    b=S[key]['body']
    assert b.count(old)==1, (key, old)
    S[key]['body']=b.replace(old,new)
    changes.append({"where":f"sections.{key}","before":old,"after":new,"why":why})

rep('overview',
 "배더락스(Alaria esculenta (L.) Greville)는 북대서양 찬 바다에 사는 갈조류(다시마목)로, 영어로는 dabberlocks, winged kelp, babberlocks라고 부른다[1].",
 "배더락스(Alaria esculenta (L.) Greville)는 북대서양의 찬 바다에 사는 다시마목 갈조류다[3, 5, 14]. 식약처 목록에 적힌 영어 이름은 dabberlocks, winged kelp, babberlocks다[1].",
 "[1](I1020 행)에는 영어명만 있고 분포·분류(다시마목) 정보가 없음; 분포는 [5]·[14], 다시마목(Laminariales) 소속은 [3] 결론부로 옮김")

rep('history',
 "아일랜드와 노르웨이가 유럽에서 이 종을 가장 많이 기르는 나라로 꼽힌다[4].",
 "아일랜드와 노르웨이가 유럽에서 이 종을 가장 많이 기르는 나라로 꼽히며, 한 논문은 선행 문헌을 인용해 연간 생산량을 각각 생중량 24톤·44톤으로 적었으나 기준 연도와 원 통계는 밝히지 않았다[4].",
 "world[] 의 연도 없는 생산값을 본문으로 옮기며 [4] 서론이 2차 인용이고 연도가 없음을 밝힘")

rep('biology',
 "배우체는 강한 빛과 자외선에 플로로탄닌을 더 만들어 대응한다[21].",
 "어린 개체(배우체)를 강한 빛·자외선에 20일 노출한 실험에서 세포 밖 플로로탄닌은 10일 뒤 늘었고 세포 안 플로로탄닌은 UV-A 처리에서 늘었으나 UV-B 포함 처리에서는 줄어, 광보호 역할이 제시되었다[21].",
 "[21] 초록: 세포 안 플로로탄닌은 PA(UV-A)에서 늘고 PAB(UV-B 포함)에서 줄었음 — '자외선에 더 만든다'는 단정은 과장")

rep('cultivation',
 "2019년 10–11월에 길이 110 m 줄 11개를 바다에 내었다[4].",
 "2019년 10–12월에 길이 110 m 줄 11개를 바다에 내었다[4].",
 "[4] 3.1절: 11개 줄은 2019년 10월–12월 사이에 투입(분석한 2·7번 줄만 10월 15일·11월 28일)")

rep('safety',
 "발효 연구의 대조 시료에서 갑각류 알레르기 단백질인 트로포미오신이 15.92 mg/kg 검출되었다[30].",
 "발효 전처리 연구에서는 전처리하지 않은 대조 시료에서 갑각류 알레르기 단백질로 알려진 트로포미오신이 가장 많이(15.92 mg/kg) 검출되었다[30].",
 "[30] 초록: 대조 시료가 트로포미오신 최고치(15.92 mg/kg), 이어 HPP 시료 — 다른 시료에서도 검출됐음을 반영")

C={c['name']:c for c in d['compounds']}
def cset(name, field, new, why):
    old=C[name][field]; C[name][field]=new
    changes.append({"where":f"compounds[{name}].{field}","before":old,"after":new,"why":why})
cset('Arsenosugar','activity_ko',
 "무기비소보다 덜 해로운 유기비소로 여겨져 왔으나 비소당·비소지질의 독성 정보는 아직 없다고 지적됨; 총비소 47.9 ± 2.7 mg/kg 건조중량 중 무기비소는 정량한계 미만 [2, 3]",
 "[2] 3.4절은 비소당·비소지질의 독성 정보가 없다고 씀 — '독성이 낮은 유기비소'로 단정할 수 없음")
cset('Arsenosugar phospholipid','part',"포자엽(생식 조직)에 상대적으로 많음",
 "[3]: '어린 조직'에 많다는 경향은 S. latissima(young frond) 쪽 서술이고, 이 종은 생식 조직에 더 많다고만 씀")
cset('Arsenosugar phospholipid','content_text',
 "두 종(이 종·S. latissima) 부위 사이 최대 약 4배 차이; 이 종의 정량은 기기 문제로 결과가 덜 명확했다고 원문이 밝힘(수치는 원문 보충자료에만 있음) [3]",
 "[3] 결론의 '약 4배'는 두 종을 합친 서술이고 이 종 정량은 'more ambiguous due to instrumental problems'")
cset('Eicosapentaenoic acid','content_text',
 "총지질 1.8–2.3 g/100 g(동결건조 시료 분석, 원문 표기 'per 100 g of biomass') 중 PUFA가 가장 많고 EPA가 풍부, DHA는 1% 미만(EPA 비율 수치는 원문 표에만 있음) [4]",
 "[4]는 지질을 'g per 100 g of biomass'로 표기 — 건조중량 기준이라 명시하지 않음")
cset('Phlorotannin','content_text',
 "알칼라제 추출물 총페놀(Folin–Ciocalteu, 플로로탄닌만의 값 아님) 57.4 ± 1.9–120.0 ± 1.8 mg GAE/g 건조 추출물(3월 수확이 가장 높음) [4]",
 "[4] 값은 총페놀(TPC)이며 플로로탄닌 단독 정량이 아님")

A=d['assays']
old=A[1]['content']
A[1]['content']="AsSugSO3가 가장 많은 비소 형태; 비소인지질은 두 종 부위 사이 약 4배 차이(이 종 정량은 기기 문제로 덜 명확); 개별 수치는 원문 표·보충자료에만 있음 [3]"
changes.append({"where":"assays[1].content","before":old,"after":A[1]['content'],"why":"[3]: 4배 차이는 두 종 합친 결론, 이 종 정량 불확실"})
old=A[2]['rationale']
A[2]['rationale']="이 종을 기능성 식품 소재로 평가하며 고부가 성분으로 지방산 조성(EPA·AA 등)을 분석했다; 전문(Methods) 확인 [4]."
changes.append({"where":"assays[2].rationale","before":old,"after":A[2]['rationale'],"why":"[4]는 EPA를 '품질 지표'로 정하지 않음 — 과장 완화"})
old=A[2]['content']
A[2]['content']="총지질 2.3 ± 0.2(10월 투입 줄)·1.8 ± 0.2(11월 투입 줄) g/100 g 바이오매스; PUFA가 가장 많고 EPA 풍부, DHA 1% 미만 [4]"
changes.append({"where":"assays[2].content","before":old,"after":A[2]['content'],"why":"11월 줄 표기 보충·기준 원문대로"})

old=json.dumps(d['world'],ensure_ascii=False)
d['world']=[]
changes.append({"where":"world","before":old,"after":"[]","why":"[4] 서론은 아일랜드 24 t·노르웨이 44 t(생중량/년)를 선행 문헌 인용으로만 적고 기준 연도·원 통계가 없음. FAO 등 원 통계로 확인 불가(GBIF·doi.org 등 접근 불가) → 배열에서 빼고 history 본문에 단서와 함께 옮김"})
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('/home/user/hfoodguide-wave3/docs/materials/alaria-esculenta/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
