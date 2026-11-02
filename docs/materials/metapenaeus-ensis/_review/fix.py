import json
p='/home/user/hfoodguide-wave3/docs/materials/metapenaeus-ensis/dossier.json'
d=json.load(open(p))
changes=[]
def rep(where,obj,key,old,new,why):
    s=obj[key]
    assert old in s,(where,old)
    obj[key]=s.replace(old,new)
    changes.append({"where":where,"before":old,"after":new,"why":why})
S={s['key']:s for s in d['sections']}
rep('sections.overview',S['overview'],'body',"사용 부위는 '-'(따로 정하지 않음)이고 별도 사용 조건이나 이명은 적혀 있지 않다[1].","사용 부위 칸은 원자료에 '-'로 적혀 있고, 사용 조건이나 이명은 적혀 있지 않다[1].","원자료(I1020) 부위 칸은 '-' 표기뿐이라 '따로 정하지 않음'이라는 해석은 원자료에 없음 — 원자료 표기 그대로 적음")
rep('sections.processing',S['processing'],'body',"이 종은 생새우로 유통되며 신선도와 미생물 저감 연구의 대상이 되었다[30, 31].","이 종은 날로 먹는 수산물의 미생물 안전성과 냉장 저장 중 신선도를 다룬 연구의 대상이 되었다[30, 31].","[30]·[31] 초록은 유통 형태(생새우 유통)를 말하지 않음 — [30]은 '날 수산물 섭취의 미생물 안전성', [31]은 냉장 저장 TVB-N")
rep('sections.processing',S['processing'],'body',"다만 이 결과는 정제 단백질과 쥐 실험 결과로, 실제 새우 제품의 알레르기 위험이 없어진다는 뜻은 아니다[18, 19].","다만 [18]은 정제 트로포미오신의 항체·환자 혈청 결합 시험, [19]는 세포(RBL-2H3·KU812)와 쥐 실험 결과로, 실제 새우 제품의 알레르기 위험이 없어진다는 뜻은 아니다[18, 19].","[18]은 쥐 실험이 아니라 토끼 다클론항체·환자 혈청 웨스턴블롯·ELISA, [19]는 세포주와 쥐 모델 — 시험 종류를 원문대로 구분")
rep('sections.safety',S['safety'],'body',"식약처는 새우 껍질 원료 건강기능식품에 '게 또는 새우에 알레르기가 있는 사람은 섭취에 주의' 문구를 정했다[2].","식약처 고시는 글루코사민·N-아세틸글루코사민·키토산의 섭취 시 주의사항으로 '게 또는 새우에 알레르기가 있는 사람은 섭취에 주의'(게 또는 새우를 원재료로 사용한 경우)를 정하고 있다[2].","고시 원문(2-30·2-31·2-49)은 해당 품목에 한정되고 '게 또는 새우를 원재료로 사용한 경우' 조건이 붙음 — 원문대로")
rep('sections.safety',S['safety'],'body',"Met e 1을 쓴 면역요법 연구는 모두 쥐 실험이다[14, 15, 16, 17]. 저알레르기 변이체, T세포 에피토프 펩타이드, 저용량 재조합 단백질 투여가 쥐의 알레르기 반응을 줄였으나 사람에서의 효과는 확인되지 않았다[15, 16, 17].","재조합 새우 트로포미오신을 먹여 쥐(BALB/c) 새우 알레르기 모델을 만든 연구가 있고(초록에는 새우 종이 적혀 있지 않음)[14], Met e 1을 쓴 면역요법의 효과 검증은 모두 쥐 실험이다[15, 16, 17]. 저알레르기 변이체, T세포 에피토프 펩타이드, 저용량 재조합 단백질 투여가 쥐의 알레르기 반응을 줄였으나 사람에서의 효과는 확인되지 않았다[15, 16, 17].","[14]는 면역요법이 아니라 감작 모델 확립 연구이고 초록에 종명(Met e 1) 표기가 없음; [15]는 환자 혈청 시험관 시험도 포함하므로 '효과 검증'으로 한정")
rep('sections.safety',S['safety'],'body',"홍콩 마이포 연못 조사에서 이 종 조직의 중금속 농도는 사람이 먹기에 안전한 수준으로 평가되었다[22]. 주강 하구 조사에서 이 종과 M. affinis를 함께 묶은 새우 시료의 PBDE(10종 합)는 지질 기준 49.0–239.1 ng/g이었다[23].","홍콩 마이포 연못 조사에서 이 종 조직의 중금속 농도는 사람이 먹기에 안전한 수준으로 평가되었다(초록에는 이 종의 금속별 수치가 없음)[22]. 주강 하구 조사의 PBDE(10종 합)는 새우 2종(이 종과 M. affinis)을 묶어 지질 기준 49.0–239.1 ng/g의 범위로만 보고되어, 이 종 단독 값은 확인하지 못함[23].","[23] 초록의 49.0–239.1 ng/g(지질 기준)은 M. ensis·M. affinis 두 종을 합친 범위 — 이 종 단독 값이 아님을 분명히 함; [22] 초록에 이 종의 수치 없음을 밝힘")
rep('sections.safety',S['safety'],'body',"미세플라스틱이 마리당 2.5 ± 0.5개(습중량 g당 0.7 ± 0.3개) 나왔고,","미세플라스틱이 마리당 2.5 ± 0.5개(습중량 g당 0.7 ± 0.3개; 근육 조직과 소화관 합산) 나왔고,","전문: 마리당 수치는 조직과 소화관(GT) 시료를 합한 값 — 가식부(조직) 값으로 오해되지 않게 밝힘")
# compounds
for c in d['compounds']:
    if c['name']=='Vitellogenin':
        old=c['part']; c['part']='간췌장(MeVg2 발현 부위)'
        changes.append({"where":"compounds.Vitellogenin.part","before":old,"after":c['part'],"why":"[33] 초록은 MeVg2가 간췌장에서만 발현된다고 하며 난소 발현은 초록에서 확인되지 않음"})
# assays
a=d['assays'][0]
old=a['conditions']['sample_prep']
a['conditions']['sample_prep']='지역별 양식 개체 근육(일반 성분은 탈피 간기 3마리; 별도로 5마리에서 근육 1 g씩 −80 °C 보관) — 아미노산 분석 시료 수는 원문에 따로 적혀 있지 않음'
changes.append({"where":"assays[0].conditions.sample_prep","before":old,"after":a['conditions']['sample_prep'],"why":"전문 2.2·2.3절: 3마리(탈피 간기)는 일반 성분 분석, −80 °C 보관은 5마리 근육 1 g — 두 내용이 섞여 있었음"})
a=d['assays'][1]
old=a['conditions']['sample_prep']
a['conditions']['sample_prep']='지역별 양식 개체 근육 — 지방산 분석 시료 수는 원문에 따로 적혀 있지 않음'
changes.append({"where":"assays[1].conditions.sample_prep","before":old,"after":a['conditions']['sample_prep'],"why":"전문 2.4절은 지방산 분석의 시료 수를 적지 않음(탈피 간기 3마리는 2.3절 일반 성분 분석)"})
# sources
src={s['n']:s for s in d['sources']}
for n,o,nw,why in [(18,'Food Chem 2016;219:215-222','Food Chem 2017;219:215-222','219권은 2017년 호(2016년은 온라인 선공개)'),
                   (19,'Food Chem 2020;340:127948','Food Chem 2021;340:127948','340권은 2021년 호(2020년은 온라인 선공개)'),
                   (33,'Biol Reprod 2004;71 (초록 확인)','Biol Reprod 2004;71(3):863-870 (초록 확인)','PubMed 서지: 71(3):863-70')]:
    assert o in src[n]['title']
    src[n]['title']=src[n]['title'].replace(o,nw)
    changes.append({"where":f"sources[{n}].title","before":o,"after":nw,"why":why})
src[7]['title']=src[7]['title'].replace('(전문 확인)','(전문 확인; PubMed 색인상 Metapenaeus ensis)')
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('/home/user/hfoodguide-wave3/docs/materials/metapenaeus-ensis/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
