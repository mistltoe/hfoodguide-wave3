import json,sys
p='/home/user/hfoodguide-wave3/docs/materials/cyclopia-intermedia/dossier.json'
d=json.load(open(p))
changes=[]
def rep(where,old,new,why):
    global d
    s=json.dumps(d,ensure_ascii=False)
    o=json.dumps(old,ensure_ascii=False)[1:-1]; n=json.dumps(new,ensure_ascii=False)[1:-1]
    assert s.count(o)==1,(old,s.count(o))
    d=json.loads(s.replace(o,n)); changes.append({"where":where,"before":old,"after":new,"why":why})
rep("sections.overview","키클로피아속의 늘푸른 떨기나무로","키클로피아속의 떨기나무로","[3]·[5] 초록은 'shrubs'라고만 하고 늘푸른(상록) 여부는 말하지 않음")
rep("sections.overview","남아공 시판·연구소 제조 '발효'(고온 산화) C. intermedia 차 6시료를 우린 물에서는","남아공 시판·연구소 제조 '발효'(고온 산화) C. intermedia 차 6시료를 탈이온수로 우린 물(잎 12.5 g/물 1 kg, 5분)에서는","[10] 표 3의 값은 W1(탈이온수) 열이며 다른 물에서는 값이 달라 기준을 밝힘")
rep("sections.history","가장 흔한 원료종이 C. intermedia다[5]","이 속에서 가장 흔한 종이 C. intermedia이며 C. subternata·C. sessiliflora 등과 함께 차 원료로 쓰인다[5]","[5] 초록은 'The most common of these plants is C. intermedia ... used together with other Cyclopia species'라고 씀(원료종 순위가 아니라 속 안에서 흔한 종)")
rep("sections.history","1998년과 2003년에 가공·비가공 잎·줄기에서 이소플라본·플라바논·쿠메스탄·크산톤 등이 보고되었다[3, 4]","1998년에는 가공한 잎·줄기에서 이소플라본·플라바논·쿠메스탄·크산톤 등이, 2003년에는 '발효' 잎·줄기에서 티로솔 유도체·플라보놀 배당체 등이 보고되었다[3, 4]","[3]은 processed, [4]는 fermented 잎·줄기를 썼고 비가공 시료는 두 초록에 없음; 쿠메스탄·크산톤은 [3]만 보고")
rep("sections.history","비발효·발효 허니부쉬 차를 루이보스·녹차·홍차와 나란히 놓고 항돌연변이·발암 촉진 억제를 비교한 동물·시험관 연구가 이어졌다[14, 15, 17]","비발효·발효 허니부쉬 차를 루이보스·녹차·홍차와 나란히 놓고 항돌연변이(시험관), 쥐 간 해독효소·산화 상태, 생쥐 피부 발암 촉진 억제를 비교한 연구가 이어졌다[14, 15, 17]","[15]는 항돌연변이·발암 연구가 아니라 쥐 간의 약물대사효소·산화 상태 연구이고, [14]는 살모넬라 시험관 실험")
rep("sections.processing","발효하지 않은 '그린' 허니부쉬도 있으며","발효하지 않은(비발효) 허니부쉬도 있으며","'그린'이라는 이름은 인용 출처 [18]·[19]에 없음(unfermented)")
rep("sections.processing","물 추출물을 유산균(Streptococcus thermophilus)으로 37 °C에서 발효시킨 것이다[20, 22]","물 추출물을 우유·당(유당)과 섞어 유산균으로 37 °C에서 발효시킨 것이다[20, 22]. 개별인정 원료 구성에는 그 유산균이 Streptococcus thermophilus 배양액으로 적혀 있다[1]","[20]·[22] 전문(PMC 본)에서 균 이름은 확인되지 않고 37 °C 발효(1일·48시간)만 확인; 균종은 식약처 목록 행[1]에 있음")
rep("sections.processing","이 구성은 C. intermedia 물 추출물(20 brix)로 만든 시험 원료 HU-018의 제조법과 같다[1, 22]","이 발효액 배합(추출물 23%·유당 3%·전지분유 0.5%·정제수 63.5%·유산균 10%)은 C. intermedia 물 추출물(20 brix, 고형분 약 20%)로 만든 시험 원료 HU-018의 제조법과 같아, 개별인정 원료가 이 종 유래로 추정된다[1, 22]. 다만 이는 배합 일치에 근거한 추정이며, 식약처 목록 행에는 학명이 없고 덱스트린 50% 비율은 논문에 나오지 않는다[1, 22]","[22]는 배합 비율이 같음을 보여 주나 덱스트린 비율은 없고, 식약처 행 학명 칸이 비어 있어 종 동일성은 추정 수준임을 밝힘")
rep("sections.safety","이 추출물은 쥐와 비글견 독성시험을 거쳤다고 적혀 있으나 결과 수치는 논문에 실리지 않았다[21, 22]","이 추출물은 쥐(Sprague Dawley)와 비글견에서 독성이 없음을 확인했다고 적혀 있으나 결과 수치는 논문에 실리지 않았다[22]","[22] 전문에서 확인; [21]은 이 문장의 출처로 확인하지 못해 뺌")
rep("sections.safety","건강한 수컷 쥐에 7주간 우린 물을 먹인 연구는 정자 운동성과 정상 형태가 줄고 농도는 늘었다고 보고했다[25]","건강한 수컷 쥐에 7주간 우린 물을 먹인 연구는 총·전진 운동성이 줄었으나(통계적으로 유의하지 않음) 정상 형태는 줄고 정자 농도는 늘었다고 보고했다[25]","[25] 초록: 운동성 감소는 non-significant")
rep("sections.safety","쥐 간 마이크로솜 실험에서 비발효 허니부쉬는 2-아세틸아미노플루오렌의 돌연변이 반응을 오히려 높였다[16]","비발효 허니부쉬를 10주간 마신 쥐의 간 마이크로솜 분획은 2-아세틸아미노플루오렌의 돌연변이 반응을 오히려 높였다(녹차·홍차군도 같음; 세포질 분획은 반대로 보호)[16]","[16] 초록: ex vivo, 녹차·홍차도 증가, 세포질 분획은 보호 — 맥락을 보탬")
rep("compounds.Mangiferin.content_text","비발효 잎·줄기 부탄올 분획(CPEF)에서 크산톤·플라바논이 각각 2 g/100 g 이상[12]","비발효 잎·줄기 40% 메탄올 추출물의 부탄올 분획(CPEF) 기준으로 크산톤·플라바논이 각각 2 g/100 g 이상(원료 잎 기준 아님)[12]","[12] 4.1절: '≥ 2 g/100 g CPEF' — 분획 기준임을 밝힘")
rep("compounds.Hesperidin.content_text","시험관 배양 미세줄기(식물체 아님) 0.9%[13]","C. intermedia 시험관 배양 미세줄기(식물체 아님) 0.9%, 같은 논문의 C. subternata 값과 구분[13]","[13] 초록: C. intermedia 0.9%, C. subternata 0.87% — 종 구분 명시")
rep("compounds.Hesperetin.activity_ko","허니부쉬 추출물 속 헤스페레틴이 쓴맛을 가리는 향미 조절 작용을 보임(관능 시험)[27]","헤스페레틴의 알려진 향미 조절 작용(쓴맛 가림 등)이 허니부쉬 추출물 속에서도 확인됨(관능 시험)[27]","[27] 초록은 기존에 보고된 향미 조절 작용이 복합 혼합물 속에서도 확인되었다고 씀")
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('/home/user/hfoodguide-wave3/docs/materials/cyclopia-intermedia/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
