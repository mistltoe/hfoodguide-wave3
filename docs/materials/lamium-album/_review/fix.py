import json
p='dossier.json'; d=json.load(open(p))
S={s['key']:s for s in d['sections']}
def rep(key,a,b):
    s=S[key]; assert a in s['body'],(key,a); s['body']=s['body'].replace(a,b)
rep('safety','당뇨 쥐에 수알코올 추출물(부위는 초록에 없음) 100 mg/kg을 투여하자 혈당이 내려갔고',
    '당뇨 쥐에 지상부 수알코올 추출물 100 mg/kg을 28일 투여하자 혈당이 내려갔고')
rep('safety','사람 각막 상피세포에서는 125 µg/mL까지 생존율이 80%로 유지되었으나, 꽃 추출물은 밀도가 낮은 피부 섬유모세포에서 125 µg/mL를 넘으면 독성을 보였다[24, 34].',
    '사람 각막 상피세포에서는 추출물(초록에 부위 표기 없음) 125 µg/mL에서 생존율이 80%로 유지되었으나, 꽃의 메탄올·에틸아세테이트 추출물은 밀도가 낮은 피부 섬유모세포에서 125 µg/mL를 넘으면 독성을 보였다[34, 24].')
rep('processing','초임계 이산화탄소로 뽑은 꽃 추출물은 배지에서 푸사리움균의 성장과 곰팡이독소 합성을 줄여 곡물 보호제 후보로 시험되고 있다[33].',
    '초임계 이산화탄소로 뽑은 꽃 추출물은 배지에서 푸사리움균의 성장과 곰팡이독소 합성을 줄였고, 연구진은 곡물 보호용 제제로 쓸 수 있는지 추가 시험을 계획했다[33].')
C={c['name']:c for c in d['compounds']}
k=C['Potassium']
k['content_text']="잎가루 마그네슘 42.3, 칼륨 278.0, 인 44.07 mg/g(초록 표기 그대로, 전문 확인 못함). 칼륨 278.0 mg/g은 잎가루 무게의 27.8%에 해당하는 값이어서 단위 표기(예: mg/100 g) 오류 가능성이 있으므로 수치를 그대로 쓰지 말 것[5]"
k['activity_ko']="잎가루의 무기질로 보고됨(단위 확인 필요)"
for n in ('Sinapic acid','Rosmarinic acid'):
    c=C[n]; c['content_text']=c['content_text'].replace('다른 연구진의 지상부 분석에서는 검출되지 않았다고 함[2]','[2]의 저자들은 이전 분석에서 검출하지 못했다고 밝힘[2]')
o=C['Oleanolic acid']
o['content_text']=o['content_text'].replace('꽃 메탄올 추출물 76.0 ± 2.7 µg/g(UHPLC-ELSD)[14]','꽃 메탄올 추출물을 산가수분해한 뒤 사포게닌으로 76.0 ± 2.7 µg/g(UHPLC-ELSD)[14]')
a=d['assays'][2]
a['rationale']=a['rationale'].replace('다른 연구진은 지상부에서 로즈마린산·시납산을 검출하지 못했다고 보고해 결과가 엇갈린다[2, 4].','[2]의 저자들은 이전 분석에서 로즈마린산·시납산을 검출하지 못했다고 밝혀 결과가 엇갈린다[2, 4].')
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
