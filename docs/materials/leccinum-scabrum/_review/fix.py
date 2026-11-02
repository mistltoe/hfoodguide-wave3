import json,sys
p='dossier.json'; d=json.load(open(p))
changes=[]
def rep(where,old,new,why):
    global d
    s=json.dumps(d,ensure_ascii=False)
    o=json.dumps(old,ensure_ascii=False)[1:-1]; n=json.dumps(new,ensure_ascii=False)[1:-1]
    c=s.count(o)
    if c!=1: print('MISS',c,old[:60]); sys.exit(1)
    d=json.loads(s.replace(o,n)); changes.append({"where":where,"before":old,"after":new,"why":why})
S='sections.'
rep(S+'cultivation',"폴란드 북서부 조사에서는 이 종이 산성 아레노솔 토양에서 자랐고, 흙의 산도가 칼륨·마그네슘 흡수에 영향을 주었다[34].",
 "폴란드 북서부 조사에서 이 종(birch bolete)은 강산성 포드졸 토양에서 자랐고(산성 아레노솔에서 자란 것은 그물버섯), 세 종 전체로 흙의 산도가 칼륨·마그네슘 흡수와 관련됐다[34].",
 "[34] 전문 3.1절: Podzols 은 bay bolete·birch bolete 아래, Arenosols 는 다른 종(그물버섯) — 이 종을 아레노솔로 쓴 것은 오류; 산도 영향은 세 종 공통 결과")
rep(S+'cultivation',"벨라루스 조사에서 이 종의 137Cs 이행계수는 (15–20) × 10^-3 m2/kg으로 그물버섯(약 10 × 10^-3 m2/kg)보다 높았다[20].",
 "벨라루스 조사(1994·2012년)에서 이 종과 L. aurantiacum의 137Cs 이행계수는 함께 (15–20) × 10^-3 m2/kg으로 묶여 보고되었고, 그물버섯(약 10 × 10^-3 m2/kg)보다 높았다[20].",
 "[20] 초록은 L. scabrum 과 L. aurantiacum 을 한 범위로 묶어 제시 — 이 종 단독 값처럼 쓴 것을 바로잡음")
rep(S+'cultivation',"실험실 순수 배양에서 이 종의 균사는 DDT(5 mg/L)를 15일 동안 거의 없애고 DDD 등으로 분해했다[29].",
 "실험실 순수 배양에서 이 종을 포함한 외생균근균 4종(그물버섯·Gomphidius viscidus·Laccaria bicolor와 함께)은 배지의 DDT(5 mg/L)를 15일 동안 거의 없앴고, 남은 DDT는 DDD 등으로 분해되었다(4종을 묶은 결과)[29].",
 "[29] 초록은 4종 공통 결과로 서술 — 이 종 단독 결과처럼 쓴 것을 바로잡음")
rep(S+'processing',"방사성 세슘(137Cs)이 블랜칭으로 15 ± 13%, 블랜칭 뒤 절임으로 55 ± 8% 줄었다(이 종을 포함한 그물버섯류 3종 결과)[21].",
 "방사성 세슘(137Cs)이 블랜칭으로 15 ± 13%, 블랜칭 뒤 절임으로 55 ± 8%, 건조 분말 침지로 38 ± 11% 줄었다(그물버섯·L. versipelle와 이 종 3종을 묶은 결과로 이 종 단독 값이 아님; 2015년 그단스크 부근 시료)[21].",
 "[21] 초록: 3종(B. edulis·L. scabrum·L. versipelle) 공통 수치임을 명시, 침지 값 보충")
rep(S+'processing',"초파리에게 먹인 예비 실험에서 포도당 수치를 최대 약 43% 낮췄다[4].",
 "수컷 초파리에게 24시간 설탕물에 섞어 먹인 예비 실험에서 몸 전체 균질액의 포도당이 대조군보다 최대 약 43% 낮았다(같은 실험에서 아카보스 200 µM은 47%)[4]. 저자들은 혈당 강하 효과가 확인되었다고 썼으나 초파리 예비 실험 1건이고, 사람의 혈당에 대한 효과는 아니다[4].",
 "[4] 전문 2.6·3.1절: 수컷 초파리·24시간·전신 균질액 포도당, 아카보스 47% 비교 — 시험관·초파리 결과의 과장 방지 문구 추가")
rep(S+'biology',"영국 실험에서 이 종의 균근은 다 자란 자작나무 근처에 심은 묘목에는 잘 생겼으나, 도랑이나 흙 기둥으로 큰 나무와 뿌리를 끊은 묘목에는 거의 생기지 않았다[28]. 연구자는 Leccinum 균이",
 "영국(에든버러 남쪽) 실험에서 이 종과 L. roseofracta 등 Leccinum 균근은 다 자란 자작나무 근처에 심은 묘목에는 잘 생겼으나, 도랑이나 흙 기둥으로 큰 나무와 뿌리를 끊은 묘목에는 대개 매우 적게 생겼다[28]. 연구자는 Leccinum 균이",
 "[28] 초록: L. scabrum 과 L. roseofracta 를 함께 'Leccinum mycorrhizas' 로 서술, '거의 생기지 않음'→'대개 매우 적음'")
rep(S+'biology',"상처가 나면 색이 변하는 버섯류로서, 아세톤 분말이 메틸메르캅탄을 잘 붙잡는 성질도 보고되었다[25].",
 "33종 비교에서 이 종은 메틸메르캅탄을 잘 붙잡는 11종 가운데 하나였고, 이 버섯들은 상처가 나면 색이 변하는 공통점이 있었다[25].",
 "[25] 초록: 포착능은 버섯 자체 측정값이고 아세톤 분말 실험은 여러 종 혼합 — 서술을 원문에 맞춤")
rep(S+'related_species',"폴란드 연구에서는 한 지역의 Leccinum 3종(L. aurantiacum·L. scabrum·L. versipelle)을 칼륨·나트륨·마그네슘 등 원소 조성으로 구별할 수 있었다[31].",
 "폴란드 연구에서는 한 지역(아우구스투프 또는 모롱크)의 꾀꼬리버섯·그물버섯·B. pinophilus·L. aurantiacum·L. scabrum·L. versipelle 6종을 칼륨·나트륨·마그네슘·카드뮴 등 원소 조성으로 구별할 수 있었다[31].",
 "[31] 초록: 판별 대상은 Leccinum 3종만이 아니라 6종")
rep(S+'related_species',"이 문서의 수치는 L. scabrum으로 명시된 시료만 옮겼다[7, 11].",
 "이 문서의 수치는 L. scabrum으로 명시된 시료에서 옮겼고, 여러 종을 묶어 낸 결과는 그렇다고 밝혔다[7, 11, 20, 21].",
 "[20]·[21]·[29] 는 여러 종 묶음 결과여서 문장을 사실에 맞춤")
rep(S+'safety',"수은은 보레츠카 숲 갓 1,200 ± 740 ng/g 건조중, 다른 숲 갓 290 ± 100–370 ± 330 µg/kg 건조중으로 보고되었다[16, 17].",
 "수은은 폴란드 북동부 보레츠카 숲과 주변 지역(1998년) 조사에서 갓 1,200 ± 740 µg/kg 건조중(대 1,100 ± 380 µg/kg 건조중), 폴란드 북부 코시치에지나 숲·비스와 사주(1993–94년) 조사에서 갓 290 ± 100–370 ± 330 µg/kg 건조중으로 보고되었다[16, 17].",
 "[16] 은 보레츠카 숲과 주변 지역을 함께 조사(이 종 값을 숲 안 값으로 한정할 근거 없음); 단위 ng/g→µg/kg 통일(같은 값); [17] 산지 명시")
rep(S+'safety',"2025년 3종 비교 연구는 측정한 카드뮴·납·니켈이 모두 EU 식품 기준 이내였다고 했다[6].",
 "2025년 폴란드 북서부 3종 비교 연구는 측정한 카드뮴·납·니켈이 모두 EU 식품 기준 이내였다고 했고, 카드뮴을 가장 많이 쌓아 주간 섭취 한계 초과를 경고받은 종은 이 종이 아니라 그물버섯(B. edulis)이었다[6].",
 "[6] PMC 전문은 종명이 빠져 있어 WebSearch 요약으로 카드뮴 축적 종이 B. edulis 임을 확인(출처에 밝힘)")
rep(S+'safety',"스웨덴 비오염지 10종 조사는 버섯 한 끼에서 올 수 있는 카드뮴 최대량이 주간 섭취 한계를 조금 밑돈다고 평가했다[32].",
 "스웨덴 우메오 비오염지 10종 조사는 버섯 한 끼에서 올 수 있는 카드뮴 최대량이 주간 섭취 한계를 조금 밑돈다고 평가했다(10종 전체 평가로 이 종만의 값은 아님)[32].",
 "[32] 초록은 10종 전체 평가")
rep(S+'safety',"방사성 세슘은 체르노빌 오염지(우크라이나)에서 최대 117 kBq/kg 건조중까지 검출되었다[19].",
 "방사성 세슘은 체르노빌 오염지인 우크라이나 지토미르 폴리시아의 드레블랸스키 자연보호구역(토양 137Cs 555–1480 kBq/m2)에서 이 종에서 최대 117 kBq/kg 건조중까지 검출되었다[19].",
 "[19] 초록: 시료 산지·오염도 명시")
# aliases
for a in ["brown birch bolete","rough-stemmed bolete"]:
    d['aliases'].remove(a); changes.append({"where":"aliases","before":a,"after":"(삭제)","why":"인용 출처 어디에도 없는 별명"})
# source 6 title note
for s in d['sources']:
    if s['n']==6:
        old=s['title']; s['title']=old.replace("(PMC12348591 전문 확인)","(PMC12348591 전문 확인; 전문에 종명이 빠져 카드뮴 최다 축적 종(B. edulis)은 WebSearch 요약으로만 확인)")
        changes.append({"where":"sources[6].title","before":old,"after":s['title'],"why":"WebSearch 요약 의존 표시"})
    if s['n']==2:
        old=s['title']; s['title']=old.replace("Leccinnum extremiorientale","Leccinnum extremiorientale(원자료 표기 그대로)")
        changes.append({"where":"sources[2].title","before":old,"after":s['title'],"why":"원자료 철자 오기를 그대로 옮긴 것임을 표시"})
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
