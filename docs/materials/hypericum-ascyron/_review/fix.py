import json
p='dossier.json'; d=json.load(open(p))
S={s['key']:s for s in d['sections']}
def rep(key,a,b):
    s=S[key]; assert a in s['body'],(key,a); s['body']=s['body'].replace(a,b)
rep('history','중국 논문들은 물레나물이 중국에서 2,000년 넘게','한 중국 논문은 물레나물이 중국에서 2,000년 넘게')
rep('related_species','총설은 물레나물을 하이퍼포린 대신 다른 아실플로로글루시놀이 많아 항균·세포독성 활성을 보일 가능성이 있는 종으로 분류했다[15].',
    '총설은 물레나물을 하이퍼포린 외의 다른 아실플로로글루시놀 유도체를 상당량 함유해 항균·세포독성 활성을 보일 가능성이 있는 종 가운데 하나로 꼽았다(총설 초록 기준)[15].')
rep('genetics','2025년 물레나물과 14종 비교에서','2025년 물레나물과 3개 족 12종과 외군 2종의 엽록체 유전체 비교에서')
rep('genetics','같은 연구의 엽록체 유전체는 163,564 bp로, 한국 개체 값(162,286 bp)과 다르다[3, 4].',
    '같은 연구에서 물레나물로 대응되는 엽록체 유전체는 163,564 bp로, 한국 개체 값(162,286 bp)과 약 1.3 kb 다르다[3, 4]. 이 논문은 물레나물과 서양고추나물의 값을 \'각각\' 순서로만 적어, 물레나물 값은 미토콘드리아 유전체(물레나물 411,519 bp, 서양고추나물 485,128 bp의 두 염색체)와 같은 순서·그림 설명(물레나물 패널)으로 대응한 것이다[4].')
for c in d['compounds']:
    if c['name'].startswith('Kaempferol 3-O'):
        c['activity_ko']='이 성분과 퀘르세틴이 든 항균 분획 8이 세균의 아폽토시스 유사 사멸 유도(시험관, 단일 성분 시험 아님)[9]'
for s in d['sources']:
    if s['n']==4:
        s['title']=s['title'].replace('본문 PMC 변환에서 학명이 빠져 그림 설명으로 종을 대응함','본문 PMC 변환에서 학명이 빠짐 — 미토콘드리아 411,519 bp·MTPT 22개(Ha_MTPT 접두어)는 그림 설명과 접두어로 물레나물에 대응, 엽록체 163,564 bp는 같은 \'respectively\' 순서로 대응')
    if s['n']==5:
        s['title']=s['title'].replace('BMC Plant Biol 2025;26(1):222','BMC Plant Biol 2025;26(1):222 (12종 신규 서열+외군 2종)')
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
