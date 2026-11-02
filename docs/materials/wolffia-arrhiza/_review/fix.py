import json,sys
p='dossier.json'; d=json.load(open(p))
S={s['key']:s for s in d['sections']}
changes=[]
def rep(where,obj,key,old,new,why):
    v=obj[key]; assert old in v,(where,old); obj[key]=v.replace(old,new); changes.append({"where":where,"before":old,"after":new,"why":why})
rep('sections.history',S['history'],'body',"분개구리밥속 식물은 태국 채소 시장에서 팔리며 샐러드·오믈렛·커리 등에 생으로 쓰인다고 소개되었다[2].","분개구리밥속 식물은 태국 채소 시장에서 팔리며, 신선한 엽상체로 샐러드·오믈렛·채소 커리 등을 만든다고 소개되었다[2].","[2] 원문은 'fresh plants are used to prepare ... salads, omelets or vegetable curries' — 커리는 익히는 요리이므로 '생으로 쓰인다'는 과장")
rep('sections.history',S['history'],'body',"1990년대 말~2000년대 초에는 우주 정거장의 생물재생 생명유지장치 연구에서 동남아시아에서 채소로 기르는 수생식물로 소개되며, 물고기·달팽이와 함께 닫힌 수조에서 기르는 식량 생산 모듈의 후보가 되었다[18].","2001년 우주용 생물재생 생명유지장치(C.E.B.A.S.) 연구는 분개구리밥을 동남아시아에서 채소로 기르는 수생식물로 소개하고, 이를 바탕으로 한 개방·폐쇄 수생 식량 생산 모듈과 국제우주정거장용 소형 모듈 최적화에 썼다[18].","[18] 초록: 물고기·달팽이와 함께 기른 원래 식물은 붕어마름(Ceratophyllum demersum)이고, 분개구리밥은 별도 수생 모듈·소형 모듈 최적화에 쓰였다")
rep('sections.cultivation',S['cultivation'],'body',"이처럼 물속 물질을 잘 빨아들이므로 식용 재배에서는 물 환경 관리가 안전성과 직결된다는 점이 유럽 평가에서도 지적되었다[7].","이처럼 물속 물질을 잘 빨아들이므로 식용 재배에서는 물 환경 관리가 안전성과 직결되며, 유럽연합 허가의 근거가 된 유럽식품안전청 기술 보고서도 실내 수직 재배 조건에서 기른 생엽상체를 대상으로 했다고 요약된다(웹 검색 요약)[7].","[7] 원문을 열지 못했고, 웹 검색 요약에서 확인되는 것은 '수직 재배 조건에서 안전성 우려 없음'까지임 — '유럽 평가에서 지적' 표현을 확인 가능한 범위로 줄임")
rep('sections.processing',S['processing'],'body',"태국 연구는 열풍 건조 조건을 비교해 50 °C·6시간에서 수분활성도 0.374–0.382 수준으로 낮추면서 총페놀·플라보노이드·엽록소가 잘 보존된다고 보고했다[3].","태국 연구는 열풍 건조 조건을 비교해 6시간 건조(50·60·70 °C)에서 수분활성도가 0.374–0.382로 가장 낮았고, 그 가운데 50 °C·6시간이 총페놀·플라보노이드·엽록소 보존에 가장 알맞다고 보고했다[3].","[3] 본문: 0.374–0.382 는 50·60·70 °C 6시간 시료 전체 범위")
rep('sections.safety',S['safety'],'body',"남조류 독소 마이크로시스틴-LR 15 µg/mL에서는 5일 만에 엽상체 수 증가가 줄었으나, 체내 축적량은 같은 실험의 좀개구리밥에서만 측정되었다[22].","남조류 독소 마이크로시스틴-LR 15 µg/mL에서는 5일 만에 엽상체 수 증가가 줄었다[22]. 같은 논문 초록의 축적량(생체중 1 mg당 0.288 ng)은 좀개구리밥 값이며, 분개구리밥 축적량은 초록에 제시되지 않아 이 종 값으로 쓰지 않았다[22].","[22] 초록: 축적량은 L. minor·C. fracta 값만 제시 — 다른 종 값이 이 종 값으로 읽히지 않게 분명히 함")
rep('sections.safety',S['safety'],'body',"(표에 단위가 빠져 있어 본문 범위로 보면 µg/kg 동결건조중량으로 추정)였다[2]","(표 8 머리말에 단위가 없으나, 본문의 카드뮴 범위 0.009–0.59 mg/kg 동결건조중량과 맞추면 표 값은 µg/kg 동결건조중량으로 읽힌다)였다[2]","[2] 본문 카드뮴 최솟값 0.009 mg/kg = 표 최솟값 8.7(µg/kg) — 추정 근거를 명시")
C={c['name']:c for c in d['compounds']}
c=C['p-Coumaric acid']
old=c['content_text']; c['content_text']="시료 6·10·12·14(14는 시판품) 11.95·76.72·54.77·78.59 mg/g 원료로 보고되었으나, 같은 논문의 총페놀이 51.7–58.3 µg GAE/g 건조중량이어서 단위·자릿수가 서로 맞지 않는 이상값이다(원문 값 그대로 옮기되 함량 근거로 쓰지 않음)[3]"
changes.append({"where":"compounds.p-Coumaric acid.content_text","before":old,"after":c['content_text'],"why":"[3] 원문 대조: mg/g(5–8% 건조중량 수준)은 같은 논문 총페놀(µg GAE/g)과 약 1000배 어긋남; 시료 14가 시판품임을 밝힘"})
old=c['activity_ko']; c['activity_ko']="원문은 정량한 페놀산 가운데 가장 많다고 했으나 수치 단위 신뢰성이 낮음[3]"
changes.append({"where":"compounds.p-Coumaric acid.activity_ko","before":old,"after":c['activity_ko'],"why":"이상값 경고"})
c=C['Chlorophyll']; old=c['activity_ko']; c['activity_ko']="70 °C 건조에서 줄어드는 경향[3]"
changes.append({"where":"compounds.Chlorophyll.activity_ko","before":old,"after":c['activity_ko'],"why":"[3] 본문: 50·60 °C보다 70 °C에서 감소, 6시간 넘는 건조에서는 오히려 늘었다고 함 — '온도가 높을수록' 일반화 축소"})
a=d['assays'][0]
old=a['content']; a['content']="시료 4종 11.95–78.59 mg/g 원료(원문 단위 그대로; 같은 논문 총페놀 µg GAE/g 값과 맞지 않는 이상값)[3]"
changes.append({"where":"assays[0].content","before":old,"after":a['content'],"why":"이상값 표시"})
old=a['rationale']; a['rationale']="분개구리밥 건조 분말에서 정량한 페놀산 가운데 가장 많다고 보고된 성분이다[3]. 다만 mg/g 값은 같은 논문의 총페놀(51.7–58.3 µg GAE/g)보다 약 1000배 커서 단위 오류 가능성이 높으므로 함량 근거로 쓰지 말고 분석 조건 참고용으로만 본다[3]. 유속·검출한계·회수율은 전문에서 확인하지 못했다[3]."
changes.append({"where":"assays[0].rationale","before":old,"after":a['rationale'],"why":"이상값 처리 명시"})
s=[x for x in d['sources'] if x['n']==7][0]
old=s['title']; s['title']="Commission Implementing Regulation (EU) 2021/2191 — fresh plants of Wolffia arrhiza and/or Wolffia globosa as a traditional food from a third country (원문 열람 못함; 웹 검색 요약으로만 허가·규격 항목(중금속·마이크로시스틴·구리·몰리브덴·아연·붕소·망간 최대치, 총균수) 확인, 수치는 미확인)"
changes.append({"where":"sources[7].title","before":old,"after":s['title'],"why":"V2 웹 검색 요약으로 규정 번호·대상 종·규격 항목 재확인, 원문 미열람 명시"})
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
