import json,re
p='/home/user/hfoodguide-wave3/docs/materials/agaricus-campestris/dossier.json'
d=json.load(open(p))
S={s['key']:s for s in d['sections']}
changes=[]
def rep(key,old,new,why):
    b=S[key]['body']; assert old in b,(key,old); S[key]['body']=b.replace(old,new)
    changes.append({"where":f"sections.{key}","before":old,"after":new,"why":why})
rep('biology','피라노스 탈수소효소는 낙엽을 분해하는 주름버섯과 일부 균에만 있는 효소로',
    '피라노스 탈수소효소는 낙엽을 분해하는 주름버섯과(Agaricaceae)의 일부 균에만 있는 효소로',
    '[17] 전문: "limited to litter-decomposing fungi of the family Agaricaceae" — 과(科) 이름임을 분명히 함')
rep('biology','자실체 균사벽은 탄수화물 78.3–79.2%, 지질 9.9–10.1%, 단백질 8.7–10.2%였고',
    '양송이와 함께 분석한 자실체 균사벽은 두 종을 합쳐 탄수화물 78.3–79.2%, 지질 9.9–10.1%, 단백질 8.7–10.2%였고',
    '[23] 초록의 범위는 양송이·주름버섯 두 종을 함께 보고한 값 — 양송이 자료 섞임 방지')
rep('genetics','1960년대에는 DNA가 많은 미토콘드리아를 가진 모델 버섯으로 연구되었다[19].',
    '1965년 논문은 주름버섯의 DNA가 많은 미토콘드리아의 구조와 기능을 다뤘다(제목만 확인)[19].',
    '[19]는 초록 없는 1편의 제목뿐이라 "모델 버섯"이라는 일반화를 뒷받침하지 않음')
rep('safety','카드뮴 평균은 갓 3.23, 대 2.24 mg/kg으로 10종 중 가장 높았다[26].',
    '카드뮴 평균은 갓 3.23, 대 2.24 mg/kg(건조중·생중 기준은 초록에 표기 없음)으로 10종 중 가장 높았다[26].',
    '[26] 초록에 기준(건/생) 표기가 없어 명시')
rep('safety','니켈 3.62, 크롬 3.01, 카드뮴 2.67 mg/kg이 10종 중 최고였다[27].',
    '니켈 3.62, 크롬 3.01, 카드뮴 2.67 mg/kg(기준 표기 없음)이 10종 중 최고였다[27].',
    '[27] 초록에 기준(건/생) 표기가 없어 명시')
rep('safety','포자 추출물은 천식·비염 환자 피부시험에 쓰였다[37].',
    '미국 동부 연구에서는 주름버섯 포자 추출물이 다른 6가지 추출물과 함께 천식·비염 환자 200명의 피내 피부시험에 쓰였으나, 종별 양성률은 초록에 없다[37].',
    '[37] 초록: 7종 추출물을 함께 시험, 종별 결과 미제시 — 이 종의 알레르기 위험으로 읽히지 않게 범위를 밝힘')
a=d['assays'][0]['conditions']
old=a['sample_prep']
a['sample_prep']='속슬렛 추출(40–70 ℃, 3–9시간, 0.5–2 mg/mL 범위 64회 실험) 뒤 인공신경망·유전 알고리즘으로 최적화한 조건(주름버섯 단일 목적 약 50 ℃·4.6시간·1.95 mg/mL)으로 추출; 용매는 에탄올(회전증발기로 제거)'
changes.append({"where":"assays[0].conditions.sample_prep","before":old,"after":a['sample_prep'],"why":"[5] 전문 Methods: 'ethanol used as a solvent was removed with the Buchi R100 Rotary Evaporator', 최적 조건 50.002 °C·4.615 h·1.952 mg/mL"})
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open(p.replace('dossier.json','_review/changes.json'),'w'),ensure_ascii=False,indent=1)
# counts
n=sum(len(re.findall(r'\[\d+(?:,\s*\d+)*\]',s['body'])) for s in d['sections'])
items=len(d['compounds'])+len(d['assays'])+len(d['sources'])+len(d['aliases'])
print(n,items,[len(s['body']) for s in d['sections']])
