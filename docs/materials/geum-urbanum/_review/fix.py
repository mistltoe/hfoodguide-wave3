import json
p='dossier.json'; d=json.load(open(p))
S={s['key']:s for s in d['sections']}
def rep(key,a,b):
    s=S[key]; assert a in s['body'],(key,a); s['body']=s['body'].replace(a,b)
rep('safety','생쥐에 20·70·210 mg/kg 먹였을 때 급성 독성 징후와 간·신장 조직 변화가 없었다[7].',
 '생쥐에 20·70·210 mg/kg 먹이고 14일 관찰했을 때 사망·체중·행동 변화 등 급성 독성 징후는 없었다[7]. 간에서는 세 투여군 모두 5% 미만의 미세 지방 변화와 경미한 간세포 풍선 변성 등이 일부 보였으나 저자들은 병리적 변화로 보지 않았고, 신장은 정상 구조였다[7].')
rep('cultivation','잎은 젖소 사료 첨가물로도 시험되었으며','지상부(원문 \'herb\')는 젖소 사료 첨가물로도 시험되었으며')
rep('cultivation','해충이 아닌 가루이의 겨울나기 장소가 되어 양배추 가루이의 천적을 늘리는 식물로 시험되었다(번데기 1 m²당 평균 166.22개)[30]',
 '해충이 아닌 가루이(Aleyrodes lonicerae)의 겨울나기 장소가 되어 양배추 가루이의 천적을 늘리는 식물로 시험되었다(이 가루이 번데기 1 m²당 평균 166.22개)[30]')
rep('processing','뿌리 우린 물을 사람 대변 미생물과 배양하면','뿌리·뿌리줄기 물 추출물을 사람 대변 미생물과 배양하면')
for c in d['compounds']:
    if c['name']=='Pedunculagin':
        c['activity_ko']='이 종에서 단독 활성 자료는 확인하지 못함; 뿌리 추출물의 α-글루코시다아제 억제에 어느 성분이 기여하는지는 밝혀지지 않음[4]'
    if c['name'] in ('Tormentic acid','Niga-ichigoside F1'):
        c['part']='메탄올 추출물의 에틸아세테이트 분획(뿌리·지상부 중 분리 부위는 초록에서 확인하지 못함)'
    if c['name']=='Ellagic acid':
        c['activity_ko']='엘라지타닌의 가수분해 산물로, 장내 미생물이 유로리틴으로 바꾼다[3]; 이 종 뿌리·뿌리줄기 물 추출물에서도 사람 대변 배양 시 유로리틴 A·B·C가 생김[26]'
        c['source']=[4,3,26]
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
