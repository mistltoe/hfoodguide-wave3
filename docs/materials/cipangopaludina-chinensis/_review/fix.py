import json,sys
p='/home/user/hfoodguide-wave3/docs/materials/cipangopaludina-chinensis/dossier.json'
d=json.load(open(p))
S={s['key']:s for s in d['sections']}
changes=[]
def rep(key,old,new,why):
    b=S[key]['body']
    assert b.count(old)==1,(key,old)
    S[key]['body']=b.replace(old,new)
    changes.append({"where":"sections."+key,"before":old,"after":new,"why":why})
rep('overview',"이 종은 건강기능식품 고시형 원료의 원재료로는 확인되지 않았다[1].",
 "건강기능식품 고시형 원료의 원재료로 쓰인 기록은 확인하지 못함.",
 "[1](식품원료 목록 I1020)은 건강기능식품 고시형 원료를 다루지 않아 이 주장의 출처가 될 수 없음")
rep('overview',"중국에서는 경제적 가치가 큰 식용·양식 고둥으로 소개되며, 벼와 우렁이를 함께 기르는 체계에서도 연구된다[18, 30].",
 "중국에서는 경제적 가치가 큰 고둥으로 소개되며 벼와 우렁이를 함께 기르는 체계에서도 연구되고[18, 30], 오늘날에도 사람이 먹는 고둥으로 기록된다[13].",
 "[18]·[30] 초록은 '경제적·약용 가치'만 말하고 식용·양식 종이라고 쓰지 않음; 식용은 [13]('currently food for humans')로 뒷받침")
rep('overview',"한국산 개체에서는 사람 장흡충을 포함한 극구흡충류의 피낭유충이 흔히 검출되어, 이 종이 사람 감염원이 될 수 있다고 보고되었다[5, 4].",
 "한국산 개체에서 사람 장흡충 Echinostoma cinetorchis의 피낭유충이 일부 지역 개체에서 검출되어 사람 감염원이 될 수 있다고 보고되었고[5], 극구흡충 E. macrorchis의 피낭유충은 흔히 검출되었다[4].",
 "[5]는 12곳 중 3곳 개체에서만 E. cinetorchis 검출; '흔히 감염'은 [4]의 E. macrorchis 이며 [4]는 국내 사람 감염을 확인하지 않음 — 두 결과를 섞어 과장")
rep('history',"한국에서는 1990년 충주호 일대 조사에서 이미 논우렁이(C. chinensis malleata)가 기생충 매개 패류 조사 대상에 포함되었다[33].",
 "한국에서는 1990년 충주호 일대 조사에서 이미 논우렁이(C. chinensis malleata)가 기생충 매개 패류 조사 대상에 포함되었는데, 검사한 56마리에서 극구흡충 유미유충은 나오지 않았고 E. hortense 유미유충 실험 감염도 되지 않았다[33].",
 "[33] 초록: 56마리 음성, C. chinensis 실험 감염 실패 — 결과를 함께 적어 기생충 서술 균형")
rep('biology',"주로 돌·수초 표면의 부착조류를 긁어 먹고, 체내",
 "부착조류를 먹이로 삼으며, 체내",
 "[12] 초록에 '돌·수초 표면'·'긁어 먹음'이 없음(먹이 경로·grazing 만 언급)")
rep('biology',"부착조류량을 줄이고 인 배설이 적어 물의 질소:인 비를 높였다[32].",
 "부착조류량을 줄이고 물의 질소:인 비를 높였는데, 연구진은 인 배설이 적기 때문일 수 있다고 보았다[32].",
 "[32]는 인 배설 저하를 'possibly' 로 추정만 함")
rep('cultivation',"중국에서 논우렁이는 경제적 가치가 큰 양식 종으로 다루어지며,",
 "중국에서 논우렁이는 경제적 가치가 큰 종으로 다루어지며,",
 "[30] 초록은 양식 종이라고 명시하지 않음(rice snail system 만 언급)")
rep('processing',"ApoE 결손 생쥐에 12주간 고지방식과 함께 먹이자",
 "ApoE 결손 수컷 생쥐에 12주간 고지방식과 함께 투여하자",
 "[25] 초록은 투여 경로를 밝히지 않음('intervened'), 수컷 생쥐")
rep('processing',"살과 내장에서는 1,382개 단백질",
 "연체부(원문 carcass)에서는 1,382개 단백질",
 "[28]은 'carcasses' 로만 적어 '살과 내장' 구분 근거 없음")
rep('genetics',"논우렁이는 2017년 중국 논우렁이과 8종과 함께 미토콘드리아 전체 유전체가 해독되었다[15].",
 "2017년 중국 논우렁이과 8종의 미토콘드리아 전체 유전체가 해독될 때 논우렁이도 그 가운데 하나로 포함되었다[15].",
 "[15]의 8종에 C. chinensis 자체가 들어 있음('8종과 함께'는 9종으로 읽힘)")
rep('safety',"한국산 논우렁이는 사람 장흡충인 Echinostoma cinetorchis의 제2중간숙주로 처음 확인되었고 사람 감염원이 될 수 있다고 보고되었다[5].",
 "한국 12곳 조사에서 3곳의 논우렁이가 사람 장흡충인 Echinostoma cinetorchis 피낭유충에 감염되어 있었고, 논우렁이속이 이 흡충의 제2중간숙주로 확인된 첫 보고로서 사람 감염원이 될 수 있다고 했다[5].",
 "[5] 초록: 12곳 중 3곳에서만 검출 — 범위를 밝힘")
rep('safety',"감염 개체당 19–183개였다[4].",
 "감염 개체당 19–183개였으나, 이 흡충의 국내 사람 감염은 아직 확인되지 않아 추가 조사가 필요하다고 했다[4].",
 "[4] 전문 Discussion: 국내 사람 감염 추적이 필요하다고만 함 — 과장 방지")
rep('safety',"대만에서는 광동주혈선충(Angiostrongylus cantonensis) 감염의 추가적인 주요 감염원으로 논우렁이가 꼽혔다[7].",
 "1991년 대만 총설은 광동주혈선충(Angiostrongylus cantonensis) 감염의 주원인인 아프리카왕달팽이 외에 논우렁이를 추가적인 주요 감염원으로 꼽았다[7].",
 "[7] 초록: 주 감염원은 Achatina fulica, 논우렁이는 'additional important sources' — 맥락 보완")
rep('safety',"미국 비소 오염 호수의 가식부 총비소는 호수 평균 2.9–46.4 μg/g이었고 그 가운데 평균 58%가 무기비소였다[2].",
 "미국 워싱턴주 얕은 호수 3곳의 개체(북미 문헌명 Bellamya chinensis) 가식부(껍데기 뺀 몸 전체) 총비소는 호수별 평균 2.9–46.4 μg/g(건조한 조직을 분해해 측정)이었고, 비소가 가장 많았던 두 호수 개체에서는 비소의 평균 58%가 무기비소였다[2].",
 "[2] 전문: 오븐 건조 조직으로 측정(생중량 아님), 58%는 Killarney·Steel 두 호수 개체만의 값, 우렁이 화학종 추출 효율 36%")
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('/home/user/hfoodguide-wave3/docs/materials/cipangopaludina-chinensis/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
