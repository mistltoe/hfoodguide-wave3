import json
p='/home/user/hfoodguide-wave3/docs/materials/patrinia-scabiosaefolia/dossier.json'
d=json.load(open(p))
S={s['key']:s for s in d['sections']}
changes=[]
def rep(key,old,new,why):
    b=S[key]['body']; assert old in b,(key,old); S[key]['body']=b.replace(old,new)
    changes.append({"where":f"sections.{key}","before":old,"after":new,"why":why})
rep('overview',"원료명 '패장'만으로 된 항목은 목록 원자료에서 확인하지 못함. 건강기능식품 고시형 원료의 원재료로 쓰인다는 기록도 목록 자료에서 확인하지 못함.",
 "같은 목록 원자료(2026-10-13 내려받음)에는 원료명 '패장'만으로 된 항목이 없고, 건강기능식품 고시형 원료의 원재료라는 표시도 없다[1].",
 "로컬 I1020_20261013.json 전수 검색: '패장'은 '패장근'(뿌리, 사용불가) 한 행뿐이고 고시형 원료 표시 없음 — 출처 없는 문장에 [1] 근거 부여")
rep('history',"1974년 일본 연구진이 마타리에서","1974년 일본약학회 학술지(Chem Pharm Bull)에 마타리에서",
 "[21]은 초록·소속이 없어 '일본 연구진'은 확인 불가 — 학술지 발행처로만 서술")
rep('history',"이리도이드 배당체 '파트리노사이드'를 새 화합물로 보고했다[21]","이리도이드 배당체 '파트리노사이드'가 새 화합물로 보고되었다[21]","위 수정에 맞춘 문장 정리")
rep('processing',"패장(두 기원 종)의 연한 줄기와 잎은 산에서 오염 없이 자라는 질 좋은 채소로 소개되며, 중국 후베이·푸젠성에서는 패장 차도 만든다[2].",
 "정리 논문은 패장(두 기원 종)의 연한 줄기와 잎을 산에서 자라는 질 좋은 채소로 소개하고, 후베이·푸젠성에 차 제품이 많다고 적었으나 차의 원료가 어느 종인지는 전문 텍스트에서 확인하지 못함[2].",
 "[2] 전문에서 차 원료의 종명이 빠져 있어 마타리·뚝갈 중 어느 종인지 확인 불가 — 뚝갈 자료 섞임 방지")
rep('cultivation',"마타리에서는 새 엄브라바이러스 후보인 'patrinia mild mottle virus'(유전체 4,214 nt)가 분리되어, 재배 중 바이러스 병해가 생길 수 있다[28].",
 "국내 연구진은 마타리에서 새 엄브라바이러스 후보인 'patrinia mild mottle virus'(유전체 4,214 nt)를 분리해 보고했으나, 재배지 피해 정도는 초록에서 확인하지 못함[28].",
 "[28] 초록은 유전체 분석만 보고 — '재배 중 병해가 생길 수 있다'는 확대 해석이라 약화")
rep('genetics',"마타리 기준 표본은 홍콩중문대학 표본관(CUHK)에 수집번호 M. C. Li 083으로 보관되었다[4].",
 "이 연구의 마타리 참조 증거표본(기준표본(type)이 아님)은 홍콩중문대학 Shiu-Ying Hu 표본관(CUHK)에 수집번호 M. C. Li 083으로 보관되었다[4].",
 "[4]의 M. C. Li 083은 연구용 참조(voucher) 표본 — '기준 표본'은 분류학의 type 으로 오해될 수 있음")
rep('safety',"일부 환자는 입마름·위 불편을 겪었다[2].","일부 환자는 입마름·위 불편을 겪었다고 하나, 이 임상 기록이 어느 종에 대한 것인지는 전문 텍스트에서 확인하지 못함[2].",
 "[2] 전문에서 해당 문장의 종명이 빠져 있음 — 뚝갈 자료일 가능성 배제 못 함")
rep('safety',"대장암 이식 생쥐에 마타리 에탄올 추출물을 먹인 실험에서는","대장암 이식 생쥐에 마타리 에탄올 추출물을 투여한 실험에서는",
 "[26] 초록에 투여 경로가 없음")
rep('safety',"마타리 추출물에 진정 효과가 보고되었으므로[29][30], 진정제나 항암제를 쓰는 사람은 마타리 제품을 먹기 전에 의료진과 상의하는 것이 안전하며 사람 대상 임상 안전성 자료는 확인하지 못함.",
 "동물실험에서 마타리 건조 추출물의 항불안·진정 효과가 보고되었고 1986년 뿌리줄기·뿌리의 진정·수면 효과 연구도 있으나[29][30], 약물 상호작용과 사람 대상 임상 안전성 자료는 확인하지 못함.",
 "'진정제·항암제 복용자는 의료진 상의' 권고는 출처가 뒷받침하지 않음(항암제 상호작용 근거 없음) — 사실 서술로 바꿈")
for c in d['compounds']:
    if c['name'] in ('Chlorogenic acid','Isochlorogenic acid A','Isochlorogenic acid C'):
        c['part']='약재(부위는 초록에 없음)'
changes.append({"where":"compounds[클로로겐산·이소클로로겐산 A·C].part","before":"약재(전초)","after":"약재(부위는 초록에 없음)","why":"[7] 초록에 사용 부위가 적혀 있지 않음"})
for a in d['assays']:
    if a['compound']=='Chlorogenic acid':
        a['part']='약재(16배치, 부위는 초록에 없음)'
    if a['compound']=='Oleanolic acid':
        old=a['rationale']
        a['rationale']="루테올로사이드와 함께 패장(마타리·뚝갈)의 주요 생리활성 성분 2종 가운데 하나로 골라 원소 조성과의 상관을 보려고 정량했다[3]. 분석법은 마타리(PSF2013-1~4)와 뚝갈 시료에 공통으로 썼고, 원액 농도(μg/mL)와 검량 범위(mg/mL) 단위가 원문에서 서로 맞지 않아 그대로 옮김."
        a['source']=[3]
        changes.append({"where":"assays[Oleanolic acid].rationale","before":old,"after":a['rationale'],"why":"[3]은 '두 주요 생리활성 성분'이라고만 함 — '사포닌이 많은 마타리 특성을 반영하는 지표'는 원문에 없는 해석"})
    if a['compound']=='Luteoloside':
        a['rationale']+=" 분석법은 마타리와 뚝갈 시료에 공통으로 썼다."
changes.append({"where":"assays[Chlorogenic acid].part","before":"약재(전초, 16배치)","after":"약재(16배치, 부위는 초록에 없음)","why":"[7] 초록에 부위 없음"})
src={s['n']:s for s in d['sources']}
def srep(n,old,new,why):
    t=src[n]['title']; assert old in t; src[n]['title']=t.replace(old,new)
    changes.append({"where":f"sources[{n}].title","before":old,"after":new,"why":why})
srep(2,"2020;262:113264","2020;265:113264","PubMed 서지: J Ethnopharmacol 265:113264")
srep(3,"2015;11(44):S441","2015;11(44):756-63","PubMed 서지: Pharmacogn Mag 11(44):756-63")
srep(28,"Arch Virol. 2019 (","Arch Virol. 2019;164(9):2375-2378 (","PubMed 서지 권·호·쪽 보충")
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('/home/user/hfoodguide-wave3/docs/materials/patrinia-scabiosaefolia/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
