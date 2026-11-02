import json
p='/home/user/hfoodguide-wave3/docs/materials/hippocampus-abdominalis/dossier.json'
d=json.load(open(p))
changes=[]
def rep(where,obj,key,old,new,why):
    s=obj[key]
    assert old in s,(where,old)
    obj[key]=s.replace(old,new,1)
    changes.append({"where":where,"before":old,"after":new,"why":why})
S={s['key']:s for s in d['sections']}
rep('sections.overview',S['overview'],'body','연구가 이어지고 있으나 모두 세포·동물 단계다[3, 5, 7].','연구가 이어지고 있으나 모두 세포·동물 단계다[3, 5, 6, 7].',
    '[3]은 조단백질 근거일 뿐 펩타이드 연구가 아님 — 쥐 혈압 시험 [6]을 더해 세포·동물 단계 근거를 맞춤')
rep('sections.biology',S['biology'],'body','양식장에서 12개월 자란 개체는 한 마리 약 15 g, 몸길이 약 15 cm였다[3].','중국 르자오의 양식장에서 산 12개월령 개체는 한 마리 약 15 g, 몸길이 약 15 cm였다[3].',
    '[3] 2.1: 시료는 중국 르자오(Rizhao) 양식업체에서 구입 — 산지를 밝힘')
rep('sections.biology',S['biology'],'body','육아낭은 배 쪽 피부 양옆이 길게 자라 가운데에서 맞붙으며 만들어진다[31].','육아낭은 몸 배 쪽 양옆의 상피가 줄 모양으로 돋아 배 가운데선 쪽으로 자라 맞붙으며 만들어진다[31].',
    '[31] 초록: linear projections of epithelia on both ventrolateral sides … elongated toward the ventral midline, fused — 피부가 아니라 상피 돌기')
rep('sections.related_species',S['related_species'],'body','해마 8종을 비교한 연구에서도 종과 성별에 따라','해마 여러 종의 암·수 시료 8개(논문 표기는 \'8종\', 이 종 포함)를 비교한 연구에서도 종과 성별에 따라',
    '[4] 2.1: \'Eight species … including both genders of\' 네 종의 암·수 — 실제로는 4종×암수 8개 시료')
rep('sections.cultivation',S['cultivation'],'body',"제주에서 산 양식 '식용 해마'가 뉴질랜드에서 들여온 계통이라는 기록도 있으나, 이 논문의 학명은 텍스트에서 직접 확인하지 못함.","제주에서 산 양식 '식용 해마'가 뉴질랜드에서 들여온 계통이라는 기록도 있으나, 이 논문 본문에서는 학명이 빠져 있어 종명은 확인하지 못함[8].",
    '출처 번호가 없던 문장 — [8] 4.1 원문(Center for Ornamental, Reef and Aquariums, Jeju; originated from New Zealand)으로 확인해 번호를 붙임')
rep('sections.cultivation',S['cultivation'],'body','어미에게는 냉동 곤쟁이(mysis)를 주는데, 이 먹이에 셀레늄이 습중량 0.97 mg/kg 들어 있었다[28].','셀레늄 사료 시험의 기본 먹이는 냉동 곤쟁이(mysis)였고, 이 먹이에 셀레늄이 습중량 기준 0.97 mg/kg 들어 있었다[28].',
    "[28] 초록은 시험 개체를 '어미'로 적지 않음 — 과장된 대상 표현 수정")
rep('sections.safety',S['safety'],'body','식용양식해마의 식품원료 상태는 \'제한적사용\'이다[1]. 그러나 식약처 원자료의 사용조건 칸이 세 줄 모두 비어 있어, 사용할 수 있는 식품 유형이나 섭취량 같은 제한 내용은 확인하지 못함.',
    "식약처 「식품원료 목록」 원자료(I1020)에서 식용양식해마·식용양식해마분말·해마추출액 세 줄은 모두 식품원료(A코드)·수산물이며 사용 상태가 '제한적사용'이다[1]. 그러나 사용조건 칸(USE_CND_STDR_CN)이 세 줄 모두 비어 있고, 부위 칸만 '-'·'-'·'전체'로 적혀 있어, 사용할 수 있는 식품 유형이나 섭취량 같은 구체적 제한 내용은 이 원자료로 확인하지 못함[1]. 같은 목록의 불가사리껍질처럼 조건('칼슘보충용 원료에 한함')이 적힌 제한적사용 수산물과 달리 조건 문구가 없으므로, 실제 사용 전에는 식약처 고시 원문이나 관할 기관 확인이 필요하다[1].",
    '과제 지시: 제한적사용 상태·조건을 원자료 칸 이름과 함께 분명히 적음(I1020 로컬 원자료로 재확인)')
rep('sections.safety',S['safety'],'body','펩타이드 IGTGIPGIW는 내피세포에서 50–400 μg/mL 범위에서 세포독성을 보이지 않았다[5]. 같은 펩타이드를 고혈압 쥐에 50 mg/kg씩 8주 먹였을 때 혈압이 내려갔다[6].',
    '펩타이드 IGTGIPGIW는 내피세포에서 50–400 μg/mL 범위(24시간)에서 세포독성을 보이지 않았으나, 이는 세포 실험이어서 사람의 섭취 안전성 근거가 되지는 않는다[5]. 같은 펩타이드를 고혈압 쥐에 한 번 먹인 시험에서는 100 mg/kg에서만 수축기 혈압이 유의하게 내려갔고(50 mg/kg는 유의하지 않음), 50 mg/kg씩 8주 먹인 후속 시험에서 혈압이 내려갔다[5, 6].',
    '[5] 2.4: 단회 투여 50 mg/kg는 유의하지 않고 100 mg/kg에서 유의 — 세포·동물 결과의 과장을 막고 조건을 원문대로 적음')
rep('sections.safety',S['safety'],'body','수족관에서 기른 개체의 사인으로는 세균성 피부염·근육병증·마이코박테리아증이 많았다[29].','캐나다 한 동물원의 실고기과 부검 172건(노랑해마 133건, 이 종 35건, 해룡 4건)을 묶은 분석에서는 세균성 피부염(24%)·근육병증(17%)·마이코박테리아증(15%)이 흔한 사인이었는데, 이 종만 따로 낸 비율은 아니다[29].',
    '[29] 초록: 세 종 합산 결과(대부분 H. kuda) — 다른 종 자료가 이 종 결과처럼 쓰였던 것을 바로잡음')
# assays [4]
a=d['assays'][2]
rep('assays[2].part',a,'part','전체(해마 분말, 8종 비교 중 이 종 암·수 포함)','전체(해마 분말; 4종 암·수 8개 시료 중 이 종 암·수 포함, 논문 표기 \'8종\')','[4] 2.1 원문: 네 종의 암·수')
rep('assays[2].content',a,'content','8종 전체 총지질 수율','8개 시료 전체 총지질 수율','[4] 시료 수 표현 정정')
# nutrients basis
for i in (1,2):
    n=d['nutrients'][i]
    rep(f'nutrients[{i}].basis',n,'basis','건조물 100 g당[3]','건조 시료(분말 그대로) 100 g당, 건조 후 잔류 수분은 보고되지 않음[3]','[3]은 건조 분말 그대로의 값이며 무수물 환산이 아님 — 생/건 기준 명확화')
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('/home/user/hfoodguide-wave3/docs/materials/hippocampus-abdominalis/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
