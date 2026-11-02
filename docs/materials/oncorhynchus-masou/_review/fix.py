import json
p='docs/materials/oncorhynchus-masou/dossier.json'
d=json.load(open(p))
S={s['key']:s for s in d['sections']}
changes=[]
def rep(key,old,new,why):
    b=S[key]['body']; assert old in b,(key,old); S[key]['body']=b.replace(old,new)
    changes.append({"where":"sections."+key,"before":old,"after":new,"why":why})
rep('related_species','일본에서는 비와송어·아마고·야마메(육봉형 송어)·무지개송어의 살을 미토콘드리아 ND4–ND5, ND1 유전자 PCR-RFLP로 구별했고, 가열 가공한 시료에서도 구별되었다[31].',
 '일본에서는 비와송어·아마고·야마메(육봉형 송어)·무지개송어의 살을 미토콘드리아 ND4–ND5, ND1 유전자 PCR-RFLP로 구별했고, 가열 가공한 비와송어 시료에서도 판별되었다[31].',
 '[31] 초록: 가열 가공 시료 판별은 비와송어(biwa trout) 시료에 한해 보고됨')
rep('processing','가공품의 종 판별에는 가열 뒤에도 쓸 수 있는 PCR-RFLP 방법이 제시되었다[31].',
 '가공품의 종 판별에는 PCR-RFLP 방법이 제시되었으나, 가열 시료로 확인한 것은 비와송어였다[31].',
 '[31] 초록: 가열 시료 검증은 비와송어 시료만')
rep('genetics','ND5 일배체형 20개가 나왔고, 일본·한국 집단의 다양성이 러시아보다 높았다[19].',
 'ND5 일배체형 20개가 나왔고, ND5 기준 일배체형·염기 다양성은 일본·한국 집단이 러시아보다 높았으나 미세위성 이형접합도는 세 지역이 비슷했다[19].',
 '[19] 초록: 다양성 차이는 ND5에서만, 미세위성은 비슷하다고 씀')
rep('safety','일본 야생 연어류 조사에서 송어는 82마리 중 12.2%에서 유충이 나왔고, 송어 유충은 분자 분석으로 동해긴촌충으로 확인되었다[9].',
 '일본 야생 연어류 조사에서 송어는 82마리 중 12.2%(10마리)에서 유충이 나왔고(마리당 평균 0.45개), 송어 유충은 분자 분석으로 동해긴촌충으로 확인되었다[9]. 다만 저자들은 일본의 주된 감염원은 송어가 아니라 봄철 연어(O. keta)로 보았다[9].',
 '[9] 초록: 10/82, 평균 0.45개/마리, 주 감염원은 O. keta라고 결론 — 송어 위험 과대 해석 방지')
rep('safety','살 속 미포자충(Kabatana takedai) 감염도 보고되었다[15, 16].',
 '살 속 미포자충(Kabatana takedai) 감염도 보고되었고, 사할린 하천의 송어 감염률은 9.0–45.6%였다[15, 16].',
 '[16] 초록 수치 보강(이 종 값)')
for c in d['compounds']:
    if c['name']=='Carotenoids':
        old=c['activity_ko']
        c['activity_ko']='송어 알에서는 리포비텔린 분획에 주로 분포했다; 난황 형성 중 결합 과정 해석은 연어(O. keta) 알 비교에서 나온 것으로 송어 자료가 아니다[35]'
        changes.append({"where":"compounds.Carotenoids.activity_ko","before":old,"after":c['activity_ko'],"why":"[35] 초록: 난황 형성 중 결합은 chum salmon(O. keta) 결과 — 다른 종 자료 섞임 분리"})
for s in d['sources']:
    if s['n']==8: s['title']=s['title'].replace('2025;44(5)','2025;44(5):1228-1234')
    if s['n']==32: s['title']=s['title'].replace('2016;1(1)','2016;1(1):295-296')
    if s['n']==34: s['title']=s['title'].replace('2022;24(3)','2022;24(3):513-523')
changes.append({"where":"sources[8,32,34]","before":"쪽수 없음","after":"PubMed 쪽수 추가","why":"PubMed 서지 대조"})
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('docs/materials/oncorhynchus-masou/_review/changes.json','w'),ensure_ascii=False,indent=1)
