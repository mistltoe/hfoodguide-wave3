import json
p='/home/user/hfoodguide-wave3/docs/materials/ribes-rubrum/dossier.json'
d=json.load(open(p))
changes=[]
def rep(where, old, new, why):
    global d
    if where.startswith('sections.'):
        k=where.split('.')[1]
        s=[x for x in d['sections'] if x['key']==k][0]
        assert old in s['body'], (where, old)
        s['body']=s['body'].replace(old,new)
    changes.append({"where":where,"before":old,"after":new,"why":why})

rep('sections.overview',
 "까치밥나무과(Grossulariaceae) 까치밥나무속의 낙엽 관목으로, 영어로 레드커런트(red currant)라 부르며 식약처 목록에는 학명 이명으로 Ribes sativum Syme.와 Ribes triste Pall.도 함께 적혀 있다[1].",
 "까치밥나무과(Grossulariaceae) 까치밥나무속의 낙엽 관목으로, 영어로 레드커런트(red currant)라 부르며 식약처 목록에는 학명 이명으로 Ribes sativum Syme.와 Ribes triste Pall.도 함께 적혀 있다[1, 6]. 다만 Ribes triste Pall.은 같은 목록에 '눈까치밥나무열매'라는 별도 원료로도 올라 있어, 이 이름의 자료를 루브룸까치밥 자료로 옮겨 쓰면 안 된다[1].",
 "과·속·낙엽관목 정보는 I1020 원자료에 없어 [6] 추가; I1020 원자료에서 Ribes triste Pall.이 '눈까치밥나무열매'로 따로 등재됨을 확인해 다른 종 혼입 주의 문장 추가")
rep('sections.overview',
 "열매는 신맛이 강한 붉은 장과로, 생과로 먹기도 하지만 대부분 잼·젤리·주스·시럽·퓌레 같은 가공품으로 소비된다[22].",
 "열매는 신맛이 강한 붉은 장과로, 생과로 먹기도 하지만 대부분 잼·젤리·주스·시럽·퓌레 같은 가공품으로 소비된다[2, 22].",
 "[22]는 신맛을 말하지 않음; [2] 서론의 'sour taste' 추가")
rep('sections.biology',
 "마케도니아산 두 품종에서는 안토시아닌이 총페놀의 85% 넘게 차지했고 하이드록시신남산 유도체는 1–6%였다[12].",
 "붉은커런트와 블랙커런트를 함께 분석한 마케도니아 연구에서는 커런트류에서 안토시아닌이 총페놀의 85% 넘게 차지했고 하이드록시신남산 유도체는 1–6%였다[12].",
 "[12] 초록의 Rosenthal·Rovada 는 붉은·검은 커런트 각 품종이고 >85%·1–6% 는 커런트류 전체 값 — 붉은커런트 두 품종 값으로 쓴 것은 블랙커런트 혼입")
rep('sections.related_species',
 "성분으로 보면 블랙커런트는 델피니딘 배당체가 많아 보라색이 진하지만, 붉은커런트의 핵심 안토시아닌은 시아니딘 배당체이다[10].",
 "성분으로 보면 블랙커런트의 핵심 안토시아닌에는 델피니딘-3-O-루티노사이드 등 델피니딘·펠라르고니딘·페투니딘 배당체가 함께 들어 있지만, 붉은커런트의 핵심 안토시아닌은 시아니딘 배당체이다[10].",
 "[10] 초록은 블랙커런트 핵심 안토시아닌으로 델피니딘·펠라르고니딘·시아니딘·페투니딘 배당체를 나열할 뿐 '델피니딘이 많다'고 하지 않음")
rep('sections.related_species',
 "현대 분류 데이터베이스(POWO·WFO)는 이 가운데 일부를 R. rubrum 의 이명이나 아종으로 처리한다[5].",
 "현대 분류 데이터베이스(POWO·WFO)는 정원커런트를 R. rubrum 의 이명으로 보는 등 이 가운데 일부를 다른 종의 이명이나 아종으로 처리한다[5].",
 "[5]: 정원커런트(Lam.)만 R. rubrum 이명, 팔체브스키커런트 등은 다른 종의 아종 이명 — 모두 R. rubrum 쪽으로 쓴 것은 과장")
rep('sections.cultivation',
 "가뭄 때는 꽃·어린 열매 떨어짐이 잠재 수량의 30–40%에 이를 수 있었다[7].",
 "붉은커런트의 씨방(어린 열매) 떨어짐은 잠재 수량의 30–40%에 이를 수 있다고 정리되었다[7].",
 "[7]은 30–40%를 가뭄 조건 값이 아니라 일반적 낙과 범위로 씀")
rep('sections.cultivation',
 "수확기는 유럽에서 7월이며, 수확 7일 전 열매는 적정 수확기보다 비타민 C가 적었다[4].",
 "폴란드 남동부 유기농장 연구에서는 7월 상순(적정 수확 7일 전)과 7월 중순(적정 수확기)에 수확했으며, 수확 7일 전 열매는 적정 수확기보다 비타민 C가 적었다[4].",
 "[4]는 한 농장의 2022년 수확 시기만 말함 — '유럽에서 7월' 일반화 수정")
rep('sections.processing',
 "가공품으로 소비되며, 기능성 식품과 식이보충제 원료로도 쓰인다[22].",
 "가공품으로 소비되며, 기능성 식품과 식이보충제 원료로도 쓰일 수 있다[22].",
 "[22]는 'could be an important ingredient'로 가능성만 말함")
rep('sections.genetics',
 "러시아에서는 'Jonkheer van Tets'와 'Chulkovskaya'를 바탕으로 가뭄·고온·겨울 추위에 강한 계통을 골라 품종으로 등록하였다[7].",
 "러시아에서는 'Jonkheer van Tets'와 'Chulkovskaya'를 바탕으로 가뭄·고온·겨울 추위에 강한 계통을 골랐고, 그 가운데 'Chulkovskaya' 계열 44-5-2 계통이 'Podarok Pobediteliam' 품종으로 러시아 국가 품종시험·보호위원회에 넘겨졌다[7].",
 "[7]은 품종 등록 완료가 아니라 국가위원회에 품종으로 '제출(transferred)'했다고 씀")
rep('sections.safety',
 "건강기능식품 고시형 원료가 아니어서 고시 섭취 시 주의사항은 없다[1].",
 "고시 제2026-43호에서 이 종을 원재료로 하는 건강기능식품 고시형 원료는 찾지 못했으므로(블랙커런트 종자만 감마리놀렌산 함유 유지 원재료로 올라 있음) 고시 섭취 시 주의사항은 확인하지 못함.",
 "[1](I1020)은 고시형 원료 여부를 말하지 않음; 로컬 고시 원문 검색 결과로 바꾸고 출처 없는 단정 제거")
rep('sections.safety',
 "2013년 이탈리아의 A형 간염 유행에서는 폴란드산 비포장 냉동 붉은커런트에서 유행주와 같은 바이러스가 검출되어 주요 전파 경로로 지목되었으므로, 냉동 열매는 가열 등 위생 관리가 필요하다[20].",
 "2013년 이탈리아 A형 간염 유행과 관련해 폴란드산 비포장 냉동 붉은커런트에서 유행주와 계통적으로 매우 가까운 바이러스가 검출되어, 냉동 붉은커런트가 이 유행의 주요 전파 매개체였다는 근거가 더해졌다[20].",
 "[20] 초록은 '같은'이 아니라 'clustered tightly'; 가열 권고는 출처에 없음")
rep('sections.safety',
 "동물 실험에서는 당뇨 쥐에 열매 에탄올 추출물을 14일간 100·500 mg/kg 먹였을 때 염증·혈소판 지표가 개선되었으나",
 "동물 실험에서는 당뇨 쥐에 열매 에탄올 추출물을 14일간 100·500 mg/kg 투여했을 때 염증·혈소판 지표가 개선되었으나",
 "[15] 초록은 투여 경로를 밝히지 않음(administered)")

# compounds
C={c['name']:c for c in d['compounds']}
def crep(name, field, new, why):
    old=C[name][field]; C[name][field]=new
    changes.append({"where":f"compounds[{name}].{field}","before":old,"after":new,"why":why})
crep('Cyanidin 3-glucoside','activity_ko',"이 연구에서 주 안토시아닌으로 확인; 적출한 쥐 회장(시험관 조건)의 자발 수축을 농도 의존적으로 억제(EC50 7.17 mg/mL)[2]","생체 내 효과로 읽히지 않도록 적출 조직 실험임을 밝힘")
crep('Cyanidin 3-xylosylrutinoside','activity_ko',"붉은 열매 색소 성분[10]","'까치밥나무속 외에서는 거의 보고되지 않음'은 [10]에 없고 생물자원 DB 규칙 결과일 뿐")
crep('Fructose','name_ko',"과당","전화당(포도당+과당)과 과당은 다름")
crep('Fructose','content_text',"세르비아 11개 품종 생과 전화당(포도당+과당 합계) 6.0–9.0%[8]; 주된 당은 포도당·과당[4]","[8] 값은 과당 단독이 아닌 전화당; 생과 기준 명시")
crep('gamma-Linolenic acid','activity_ko',"인도메타신 위궤양 쥐에서 기름 10·15 mL/kg 투여가 염증 지표를 낮춤(동물 실험; 기름의 원료 부위·조성 근거는 초록에 없음)[16]","부위·출처 불명확한 기름의 쥐 실험임을 명시")

# aliases
old=list(d['aliases'])
d['aliases']=[a for a in d['aliases'] if a!='Ribes triste Pall.']
changes.append({"where":"aliases","before":"… 'Ribes triste Pall.'","after":"(삭제)","why":"I1020 원자료에서 Ribes triste Pall.은 '눈까치밥나무열매'로 따로 등재된 다른 종 — 별명으로 두면 다른 종 자료가 섞임"})
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('/home/user/hfoodguide-wave3/docs/materials/ribes-rubrum/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
