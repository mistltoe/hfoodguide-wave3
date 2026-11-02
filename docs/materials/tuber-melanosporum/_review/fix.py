import json
p='/home/user/hfoodguide-wave3/docs/materials/tuber-melanosporum/dossier.json'
d=json.load(open(p))
S={s['key']:s for s in d['sections']}
changes=[]
def rep(key,old,new,why):
    b=S[key]['body']; assert b.count(old)==1,(key,old); S[key]['body']=b.replace(old,new)
    changes.append({"where":f"sections.{key}","before":old,"after":new,"why":why})
rep('overview','실온에서는 5–7일이면 품질이 떨어질 만큼 저장성이 낮아 포장·건조 연구가 많다[18].',
    '실온에서는 최대 5–7일이면 품질이 떨어질 만큼 저장성이 낮아 저장 기간을 늘리는 포장 연구가 이어졌다[18].',
    '[18]은 실온 최대 5–7일과 포장(MAP·감압) 연구를 말하며 건조 연구는 다루지 않음')
rep('history',"오늘날 균근 묘목을 얻는 '모수(mother plant) 기법'은 19세기 초 프랑스에서 트러플 재배를 개척할 때 쓴 방법을 고친 것이다[26].",
    "균근이 붙은 뿌리를 접종원으로 쓰는 '모수(mother plant) 기법'은 19세기 초 프랑스에서 트러플 재배를 개척할 때 쓴 방법을 고친 것이다[26].",
    "[26]은 모수 기법을 식용 균근균 일반의 접종원 확보법으로 설명하며 오늘날 트러플 균근 묘목의 표준법이라고 하지 않음")
rep('biology','프랑스 재배원 조사에서는 모체(암) 유전형과 부체(수) 유전형이 대부분 따로 나타났고',
    '한 재배원의 5년 조사에서는 모체(암) 유전형과 부체(수) 유전형이 대부분 따로 나타났고',
    '[5] 초록은 재배원 1곳(an orchard)의 5년 조사라고만 쓰고 나라는 밝히지 않음')
rep('safety','자투리 자실체 추출물은 중금속 함량이 낮고 Caco-2 세포에서 세포독성이 없었다[32].',
    '자투리 자실체 추출물은 중금속 함량이 낮고 Caco-2 세포에서 세포독성이 없었으나, 이는 세포 실험 결과로 사람 안전성 자료는 아니다[32].',
    '세포 실험 결과임을 밝혀 과장 방지([32] 초록은 Caco-2 세포 독성 시험만 보고)')
C={c['name']:c for c in d['compounds']}
e=C['Ergosterol']; old=e['activity_ko']
e['activity_ko']='스테롤 비율이 유럽·중국 트러플 판별에 쓰임[10]'
changes.append({"where":"compounds.Ergosterol.activity_ko","before":old,"after":e['activity_ko'],"why":"[20] 초록에서 IL-1β 40%·IL-6 60% 감소는 다당을 침전·분석한 최적 PLE 추출물(EP)의 결과이며 에르고스테롤(에탄올) 분획의 결과로 특정되지 않음"})
b=C['beta-Glucan']; old=b['activity_ko']
b['activity_ko']='NMR로 (1→3)-β-글루칸 구조 확인; 최적 PLE 추출물(EP)이 THP-1 세포에서 IL-1β 40%·IL-6 60% 분비 감소(세포 실험, 사람 효과 아님)[20]'
changes.append({"where":"compounds.beta-Glucan.activity_ko","before":old,"after":b['activity_ko'],"why":"[20] 초록의 세포 실험 결과를 추출물 단위로 옮기고 세포 실험임을 밝힘"})
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('/home/user/hfoodguide-wave3/docs/materials/tuber-melanosporum/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
