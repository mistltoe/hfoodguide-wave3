import json
p='dossier.json'; d=json.load(open(p))
S={s['key']:s for s in d['sections']}
changes=[]
def rep(key,old,new,why):
    b=S[key]['body']; assert old in b,(key,old); S[key]['body']=b.replace(old,new); changes.append({"where":f"sections.{key}","before":old,"after":new,"why":why})
rep('overview','바닷물과 민물을 오가는 광염성 어종이다[6]','염분 변화에 잘 견디는 광염성(euryhaline) 어종이다[6]',
    "[6] 초록은 euryhaline 이라고만 씀 — 바닷물·민물을 '오간다'(회유)는 표현은 출처에 없음")
rep('biology','하구처럼 염분이 크고 자주 바뀌는 연안에 사는 광염성 어종이다[7]','염분 변화가 크고 잦은 연안·하구에 사는 광염성 어종이다[6, 7]',
    "[7] 은 'coastal environments with large and frequent salinity fluctuation', 하구(estuarine)는 [6] 에 있음 — 출처 보강")
rep('biology',' 부화 직후 자어는 15일째까지 천천히 자라 4.7 mm에 이르고, 16–30일째에는 더 빨리 자라 7.5 mm가 되었다[17]. 이 시기 소화효소는 입이 열릴 때부터 검출되었지만 장의 성숙은 생후 한 달 안에 끝나지 않았다[17].','',
    "[17] 은 이란 페르시아만 연구소(부셰르)의 'A. latus' 자어 연구 — 2013년 분류 정리[2]로 페르시아만 개체는 A. arabicus·A. sheim 일 가능성이 커 새눈치 값에서 뺌(related_species 에 주석)")
rep('cultivation','종자 생산에서는 나노클로롭시스를 넣은 녹수 방식으로 자어를 기르고, 로티퍼에서 아르테미아, 미립자 사료 순으로 먹이를 바꿨다[17]. ','',
    "[17] 은 페르시아만(이란) 개체 연구로 다른 종일 수 있음 — 같은 이유로 삭제")
rep('related_species','이 문서는 그 수치를 새눈치 값으로 쓰지 않았다[2, 12, 13].',
    "이 문서는 그 수치를 새눈치 값으로 쓰지 않았다[2, 12, 13]. 2013년 이후에도 이란 페르시아만 연구진이 'A. latus'라는 이름으로 자어 사육·소화효소 연구를 냈으나, 채집 해역으로 보아 A. arabicus나 A. sheim일 수 있어 같은 이유로 새눈치 값으로 쓰지 않았다[2, 17].",
    "[17] 의 처리 근거를 밝힘(이란 부셰르 연구진, 페르시아만 개체)")
rep('processing','양식 사료 연구에서는 라이소자임을 100 mg/kg 넣은 사료가 살의 경도와 말산·EPA·DHA 축적을 높였다고 보고되었다[4].',
    '양식 사료 연구에서는 라이소자임을 넣은 사료(100·200 mg/kg)가 살의 경도를 높였고, 100 mg/kg군에서는 대사체 상대량으로 말산과 불포화 지질(PE 22:6 등)이 늘어 저자들은 EPA·DHA 축적이 늘었다고 해석했다[4].',
    "[4] 전문: 경도는 두 군 모두(200 mg/kg군이 더 높음) 상승, EPA·DHA 는 지방산을 직접 정량하지 않고 전구체·PE(22:6) 상대량으로 추정")
for c in d['compounds']:
    if c['name']=='Eicosapentaenoic acid':
        old=c['activity_ko']; c['activity_ko']='라이소자임 100 mg/kg 사료군에서 EPA·DHA 전구체와 PE(22:6)가 늘어 축적 증가가 시사되었고[4], GABA 0.01%군 근육의 EPA 비율은 0.10%군보다 높았다[5]'
        changes.append({"where":"compounds[EPA].activity_ko","before":old,"after":c['activity_ko'],"why":"[4] 는 EPA 를 직접 정량하지 않음(대사체 추정), [5] 는 0.01% vs 0.10% 비교만 유의"})
    if c['name']=='Phosphatidylcholine':
        old=c['activity_ko']; c['activity_ko']='라이소자임 사료군 근육에서 PC·PE가 많아졌다[4]'; c['source']=[4,5]
        changes.append({"where":"compounds[PC].activity_ko","before":old,"after":c['activity_ko'],"why":"이 문장은 [4] 만의 결과 — [5] 인용 제거(함량 값은 [5] 그대로)"})
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
