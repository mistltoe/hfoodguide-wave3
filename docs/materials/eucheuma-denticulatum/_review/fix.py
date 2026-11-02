import json,sys
p='dossier.json'; d=json.load(open(p))
S={s['key']:s for s in d['sections']}
changes=[]
def rep(where,obj,key,old,new,why):
    v=obj[key]
    assert old in v,(where,old)
    obj[key]=v.replace(old,new,1)
    changes.append({"where":where,"before":old,"after":new,"why":why})
rep('sections.biology',S['biology'],'body',
 '물살이 적당히 센 열대·아열대 산호초에서 자연적으로 자란다[3, 9]',
 '물살이 적당히 센 열대·아열대 산호초에서 자연적으로 자란다[9]',
 '서식지 서술은 [9] 초록에만 있고 [3]에는 없음')
rep('sections.biology',S['biology'],'body',
 '마다가스카르 생트마리섬 시료에서는 성숙기에 이오타형 카라기난이 주를 이루고, 어린 시기에는 카파·뉴 카라기난이 일부 섞였다[3].',
 '마다가스카르 생트마리섬 시료는 성숙기(여름, 12–3월)에 이오타형 카라기난이 주를 이루었고, 생장기(겨울, 6–9월)에는 3,6-안하이드로갈락토스 함량이 높았다[3].',
 "[3] 전문에 '어린 시기 카파·뉴 카라기난 혼재' 서술이 없음(FTIR 띠 해석만 있음); 원문의 계절 서술로 바꿈")
rep('sections.biology',S['biology'],'body',
 '실험실 배양에서 이 종은 낮과 밤 모두',
 '낮·밤 영양염 흡수 비교에서 이 종은 낮과 밤 모두',
 '[23] 초록은 실험실 배양이라고 밝히지 않음')
rep('sections.cultivation',S['cultivation'],'body',
 '이 논문은, 마다가스카르 논문은 2019년 이 속 해조 생산량이 18만 톤이고 주로 잔지바르와 필리핀에서 나왔다고 2차 인용했다[3]. 이 수치는 원문 추출본에서 학명 표기가 빠져 종 단위인지 속 단위인지 확인하지 못함.',
 '같은 논문은 다른 문헌을 인용해 2019년 생산량이 18만 톤으로 2015년보다 줄었고 주로 잔지바르와 필리핀에서 나왔다고 적었다[3]. 이는 1차 통계가 아닌 2차 인용이며, 원문 추출본에서 학명 표기가 빠져 이 수치가 이 종 단위인지 속 단위인지는 확인하지 못함.',
 "문장이 중복·비문('이 논문은, 마다가스카르 논문은')이고 '이 속'이라 단정한 뒤 다시 확인 못함이라 적어 모순; 원문의 2015년 대비 감소 내용 추가, 2차 인용임을 명시")
rep('sections.processing',S['processing'],'body',
 '이는 세포 실험과 생쥐 모델 수준의 결과다[32].',
 '이는 세포 실험과 동물(수동 피부 아나필락시스) 모델 수준의 결과다[32].',
 '[32] 초록은 동물 종을 밝히지 않음(생쥐 단정 불가)')
rep('sections.safety',S['safety'],'body',
 'E. spinosum 유래 분해 카라기난을 기니피그에 먹이면 대장 궤양이, 쥐에 최장 24개월 먹이면 대장·직장 종양이 생겼다[17, 18, 19]. 이 결과는 식품용 카라기난이나 해조 자체가 아니라 분해한 저분자 카라기난의 동물 실험이다[2, 17, 18].',
 'E. spinosum 유래 분해 카라기난을 마시는 물에 넣어 기니피그에 주면 대장 궤양이, 쥐에 사료·물·위관으로 최장 24개월 주면 대장·직장 종양이 생겼다[17, 18, 19]. 같은 계열 기니피그 실험에서는 분해하지 않은 이 종 유래 카라기난 1%를 마시는 물로 주었을 때도 주로 맹장에 궤양이 생겼다[19]. 이들은 정제 카라기난을 고농도로 준 동물 실험이며 해조 자체를 먹인 시험이 아니고, 식품첨가물 규격 카라기난에 대한 EFSA의 판단과는 따로 읽어야 한다[2, 17, 18, 19].',
 "[19] 초록은 비분해 카라기난 1%로도 기니피그 맹장 궤양을 보고해 '분해 저분자 카라기난만의 결과'라는 서술이 원문과 어긋남; 투여 경로를 원문대로 적고 [2]를 이 실험들 해석의 근거로 쓴 부분을 바로잡음")
rep('sections.safety',S['safety'],'body',
 '이 종 자체 자료로는, 에탄올 추출물을 수컷 쥐에 28일 동안 300–1000 mg/kg 먹인 시험에서 생화학 지표에 유의한 변화가 없었으나 1000 mg/kg에서 간·신장 조직에 가벼운 변화가 보였다[6].',
 '이 종 자체 자료로는, 생 원료 에탄올 추출물을 수컷 쥐(군당 6마리)에 28일 동안 300–1000 mg/kg 먹인 시험에서 ALT·크레아티닌·총단백·요소는 유의한 차이가 없었고 AST는 1000 mg/kg에서 오히려 낮았으며, 적혈구용적·호염기구·MCHC가 정상 범위 안에서 조금 달랐고 1000 mg/kg에서 간·신장 조직에 가벼운 변화(염증세포 침윤 등)가 보였다[6]. 저자들은 고용량 장기 사용에 주의가 필요하다고 결론지었다[6].',
 '[6] 전문: AST는 최고 용량에서 유의하게 감소, 혈액 지표 3개 차이, 조직 변화 내용과 저자 결론을 원문대로 보충')
# compounds
for c in d['compounds']:
    if c['name']=='Galactose':
        old=c['content_text']
        c['content_text']='총당 대비 43.2–55.2% TS(총단당이 가장 낮은·높은 달 시료, 2022년 10·11월; 2021년 12·8월은 47.1·49.5% TS)[3]; 추출물 가수분해 갈락토스 수율 50.7%[34]'
        changes.append({"where":"compounds[Galactose].content_text","before":old,"after":c['content_text'],"why":"[3]은 월별 전체 범위가 아니라 최저·최고 총단당 달의 값만 제시; 같은 원문 다른 곳은 '60% TS 이상'이라 적어 원문 안에서 엇갈림"})
for a in d['assays']:
    if a['compound'].startswith('Galactose'):
        old=a['rationale']
        a['rationale']=old.replace('비움[3].',"비움; 원문 결과 절의 '갈락토스 60% TS 이상' 서술은 표 값(43.2–55.2% TS)과 엇갈림[3].")
        changes.append({"where":"assays[Galactose].rationale","before":old,"after":a['rationale'],"why":"원문 안의 수치 불일치를 밝힘"})
for s in d['sources']:
    if s['n']==6:
        old=s['title']
        s['title']=old.replace("PubMed 학명 검색과 'spinosum' 표기로 이 종 논문임을 확인","PubMed에서 'Eucheuma denticulatum' 검색으로 이 서지 레코드가 잡혀 이 종 논문임을 확인; 본문의 'spinosum'은 탄자니아 도입 역사 서술에만 나옴")
        changes.append({"where":"sources[6].title","before":old,"after":s['title'],"why":"종 판단 근거를 실제로 확인한 근거로 고침"})
    if s['n']==19:
        s['title']=s['title']
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
