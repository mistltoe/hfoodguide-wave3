import json
p='docs/materials/thunnus-alalunga/dossier.json'
d=json.load(open(p))
ch=[]
def rep(where,obj,key,old,new,why):
    assert old in obj[key], (where,old)
    obj[key]=obj[key].replace(old,new); ch.append({"where":where,"before":old,"after":new,"why":why})
sec={s['key']:s for s in d['sections']}
s=sec['safety']
rep('sections.safety',s,'body','국내에서는 다랑어류에 메틸수은 1.0 ppm 기준을 적용한다고 알려져 있으나, 이 조사에서는 검색 결과 요약으로만 확인했다[36, 37]. ',
    '국내 식품 기준(식품공전)의 다랑어류 메틸수은·히스타민 기준 원문은 이 조사에서 열지 못해 확인하지 못함. ',
    '[36]·[37] 은 WebSearch 요약뿐이고 mfds.go.kr·korea.kr 은 이 환경 망 밖이라 원문 대조 불가 — 근거 없는 기준치 문장을 확인하지 못함으로 바꿈(눈다랑어 V2 처리와 같은 방식)')
rep('sections.safety',s,'body','지중해 개체는 총수은이 평균 1.17 mg/kg이고 그 약 91.3%가 메틸수은이었다[17].',
    '지중해 개체는 근육 총수은이 0.84–1.45 mg/kg 습중량(평균 1.17)으로 78.6%가 EU 기준 1 mg/kg 습중량을 넘었고, 수은의 77–100%(평균 91.3%)가 메틸수은이었다[17].',
    '[17] 초록: 날개다랑어 값은 w.w.(습중량) 기준이고 78.6% 가 EU 기준 초과 — 기준(습중량)과 초과율을 밝힘(참다랑어 값과 구분)')
rep('sections.safety',s,'body','히스타민은 냉장 보관 중 30 °C에 하루 2시간씩 노출하면 67–382 mg/kg까지 생겼다[21]. 등푸른생선 히스타민 200 mg/kg 기준도 검색 요약으로만 확인했다[37]. ',
    '히스타민은 0–2 °C 냉장 보관 중 30 °C에 하루 2시간씩 노출한 로인에서 67–382 mg/kg, 6–7 °C 보관 시 544.5–4156.6 mg/kg까지 생겼다[21]. ',
    '[21] 초록: 67–382 mg/kg 는 0–2 °C 보관 조건 값 — 보관 온도를 밝히고, [37](검색 요약뿐) 기준 문장은 앞 문장에 합쳐 확인하지 못함으로 처리')
rep('sections.safety',s,'body','근육에서 Kudoa thunni 포자낭이 보고되었다[31].','일본 시판 날개다랑어 1마리의 근육에서 신종 Kudoa thunni 포자낭이 보고되었다[31].',
    '[31] 초록: 태평양산 날개다랑어 1마리에서 신종으로 기재 — 표본 수를 밝혀 일반화 방지')
sec['overview']['body']  # unchanged
pr=sec['processing']
rep('sections.processing',pr,'body','살균을 길게 하면 유리아미노산이 원료 대비 약 12–34% 줄었다[26].',
    '115 °C 살균을 60분·100분 하면 유리아미노산이 원료 대비 각각 약 12%·34% 줄었다[26].',
    '[26] 초록: 12% 는 60분, 34% 는 100분(115 °C) — 범위가 아니라 조건별 값')
for c in d['compounds']:
    if c['name']=='Cadmium':
        old=c['content_text']; c['content_text']=old.replace('남동 지중해 간 평균 9.22 μg/g [18]','남동 지중해 간 평균 9.22 μg/g 습중량(살 평균 0.05) [18]')
        ch.append({"where":"compounds[Cadmium].content_text","before":old,"after":c['content_text'],"why":"[18] 초록: wet wt 기준, 살 값 0.05 함께 표기"})
    if c['name']=='Methylmercury':
        old=c['content_text']; c['content_text']=old.replace('지중해 개체 총수은의 77–100%(평균 91.3%) [17]','지중해 개체 총수은(0.84–1.45, 평균 1.17 mg/kg 습중량)의 77–100%(평균 91.3%) [17]')
        ch.append({"where":"compounds[Methylmercury].content_text","before":old,"after":c['content_text'],"why":"[17] 초록 — 기준 총수은 값·습중량 명시"})
d['sources']=[x for x in d['sources'] if x['n'] not in (36,37)]
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(ch,open('docs/materials/thunnus-alalunga/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(ch))
