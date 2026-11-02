import json,re
P='/home/user/hfoodguide-wave3/docs/materials/nypa-fruticans/'
d=json.load(open(P+'dossier.json'))
changes=[]
def rep(where,old,new,why):
    for s in d['sections']:
        if s['key']==where:
            assert old in s['body'],(where,old)
            s['body']=s['body'].replace(old,new); changes.append({'where':'sections.'+where,'before':old,'after':new,'why':why}); return
    raise Exception(where)
rep('overview',"니파야자추출액 6행이 모두 '사용가능'으로 올라 있다[1].",
 "니파야자추출액 6행이 모두 '사용가능'으로 올라 있고, 복합원료(U코드)로 '니파야자순혼합추출물' 1행도 '사용가능'이다[1].",
 "I1020 원자료에 복합원료 행이 있으나 본문에 빠져 있어 보탬")
rep('history',"방글라데시 남부에서는 잎과 줄기를 여러 질환에 쓰는 전통 용법이 있고, 동남아시아에서는 잎을 염증·간 질환에 써 왔다고 한다[23, 31].",
 "방글라데시 남부에서는 이 식물을 여러 질환에 쓰는 전통 용법이 알려져 있고[23], 동남아시아에서는 염증·간 질환에 써 왔다고 한다[31].",
 "[23]·[31] 초록은 전통 용도의 부위를 잎·줄기로 특정하지 않음(잎·줄기는 실험 시료 부위)")
rep('history',"싱가포르에서는 열매 배젖을 'attap chee'라는 이름으로 먹는다[14].",
 "싱가포르 의학 보고에서는 니파야자 배젖을 흔히 'attap chee'라고 부른다고 적었다[14].",
 "[14] 초록은 배젖의 통칭이 attap chee라고만 하고, 싱가포르에서 먹는다는 내용은 없음(전문 본문 비어 있음)")
rep('biology',"생육에 알맞은 최고 기온은 32–35 °C, 기후는 아습윤–습윤으로 보고되었다[4].",
 "니파야자 자생지의 평균 최고 기온은 32–35 °C, 알맞은 기후는 아습윤–습윤으로 인용되었다[4].",
 "[4] 원문은 'average maximum temperature 32–35°C, optimal climate subhumid to humid'로 '생육 최적 최고 기온'이 아님")
rep('related_species',"국내 한 연구 논문은 니파야자를 천남성과(Araceae)로 적었으나, 다른 문헌과 식약처 목록 체계에서 이 종은 야자과 식물이다[1, 17, 23].",
 "국내 한 연구 논문은 니파야자를 천남성과(Araceae)로 적었으나, 다른 문헌에서 이 종은 야자과(Arecaceae) 식물이다[6, 17, 23].",
 "I1020 [1] 행에는 과(科) 정보가 없음; 야자과 근거는 [6]·[23]")
rep('related_species',"한편 같은 목록에서 빈랑자(Areca catechu)는 '사용불가'로 분류되어 있어, 야자과라도 지위가 다르다[1].",
 "한편 같은 목록에서 빈랑(Areca catechu)은 빈랑·빈랑나무열매·빈랑나무열매껍질 행이 '사용불가'이고 건강기능식품 원료 '빈랑자'도 사용할 수 없는 원료로 올라 있어, 야자과라도 지위가 다르다[1].",
 "I1020 원자료: 빈랑 A코드 행 3개 사용불가, '빈랑자'는 C코드(건강기능식품 제조에 사용할 수 없는 원료)")
rep('related_species',"니파야자를 해치는 해충 Octodonta nipae는 중국 남동부에서 다른 관상 야자에도 큰 피해를 주며 침입했다[24].",
 "'니파야자 잎벌레(nipa palm hispid)'라는 이름의 해충 Octodonta nipae는 중국 남동부에 침입해 관상 야자에 큰 피해를 주며, 실험에서는 당종려·카나리야자 등에서 잘 자랐다[24].",
 "[24]는 니파야자 피해를 다루지 않고 다른 야자 기주 실험만 보고함")
rep('cultivation',"해충으로는 니파야자 잎벌레(Octodonta nipae)가 알려져 있고, 방글라데시 해안에서는",
 "니파야자 잎벌레(Octodonta nipae)는 이름과 달리 [24]에서 다른 관상 야자 피해로 연구되었고, 방글라데시 해안에서는",
 "[24]는 니파야자에서의 피해를 보고하지 않음")
rep('safety',"열매 배젖은 단단해 잘 씹지 않고 삼키면 위험할 수 있으며, 싱가포르에서 attap chee와 닮은 위석(덩어리)이 소장을 막아 수술한 사례가 있다[14].",
 "싱가포르에서는 단단하고 둥근 attap chee(니파야자 배젖)와 닮은 위석(덩어리)이 60세 남성의 소장을 막아 수술한 사례가 보고되었다[14].",
 "[14] 초록에 '잘 씹지 않고 삼키면 위험' 같은 일반화는 없음; 사례 1건만 기술")
rep('safety',"항영양 성분이 있으나 사람에게 위험한 농도는 넘지 않는다는 문헌이 인용되었다[16].",
 "항영양 성분이 있으나 사람에게 치명적인 중독 수준(2.5 g/100 g)은 넘지 않는다는 문헌이 인용되었다[16].",
 "[16] 원문은 'do not exceed lethal poisoning for humans (2.5 g/100 g)'로, '위험한 농도'보다 좁은 기준(치사 수준)")
# compounds
for c in d['compounds']:
    if c['name']=='Pengxianencin A':
        old=c['activity_ko']
        c['activity_ko']="저자들이 추출물 항광노화 활성의 주성분으로 추정했으나, 어떤 성분이 활성을 내는지는 확정하지 못했다고 함(세포·쥐 피부 도포 실험)[25]"
        changes.append({'where':'compounds.Pengxianencin A.activity_ko','before':old,'after':c['activity_ko'],'why':"[25] 고찰: 'we cannot determine exactly which compounds exert activity' — 과장 완화"})
for a in d['assays']:
    if a['compound']=='Gallic acid':
        old=a['rationale']
        a['rationale']="식초에서 가장 많은 페놀로 지질 소화효소 억제 활성(시험관)의 후보 성분; 전문 확인, 칼럼·이동상·유속은 원문에 없고 외부 분석기관 의뢰 방법을 인용만 함[5]."
        changes.append({'where':'assays.Gallic acid.rationale','before':old,'after':a['rationale'],'why':"[5] Methods에 이온화 모드 언급은 있으므로 '이온화 방식은 원문에 없음'을 빼고 확인된 결손 칸만 적음"})
json.dump(d,open(P+'dossier.json','w'),ensure_ascii=False,indent=1)
json.dump(changes,open(P+'_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
