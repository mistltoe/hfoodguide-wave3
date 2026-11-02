import json,sys
p='/home/user/hfoodguide-wave3/docs/materials/conyza-canadensis/dossier.json'
d=json.load(open(p))
S={s['key']:s for s in d['sections']}
def rep(key,old,new):
    b=S[key]['body']; assert old in b,(key,old); S[key]['body']=b.replace(old,new)
rep('overview','잎·꽃의 추출물에서는 디카페오일퀸산 같은 페놀산과 로즈마린산, 아피제닌 배당체 등 플라보노이드가 정량되었다[2][4].',
 '잎·꽃 추출물에서는 디카페오일퀸산 같은 페놀산이, 지상부 메탄올 추출물에서는 로즈마린산과 아피제닌 배당체 등 플라보노이드가 정량되었다[2][4].')
rep('history','\n\n한국 한의학 처방 도인승기탕을 다룬 연구는 구성 약재 하나를 Conyza canadensis로 표기했다[29]. 다만 이 처방의 \'망초\'가 식물 망초를 뜻하는지는 이번 조사에서 확인하지 못함. 망초가','\n\n망초가')
rep('related_species','국내에 자라는 큰망초·실망초 등과의 식별 기준은 이번 조사에서 확인하지 못함.',
 '「식품원료 목록」은 \'큰망초\'를 망초의 다른 이름으로 적었으나[1], 이 이름이 국내에서 다른 망초속 종을 가리키는지와 근연종(실망초 등)과의 식별 기준은 이번 조사에서 확인하지 못함.')
rep('related_species','옛 망초속 종들은 개망초속 안에 묻혀 들어가, 두 속을 따로 나누기 어렵다는 결과가 나왔다[22].',
 '옛 망초속 종들은 개망초속 안에 묻혀 들어가는 결과가 나왔다[22].')
rep('cultivation','망초는 재배 작물이 아니라 경작지·길가·빈터에 저절로 나는 잡초로 다뤄진다[14]. 콩·목화 같은 주요 밭작물에서 해마다 28–68%의 수량 손실을 일으키는 것으로 정리되었고, 경운을 하지 않는 보전 농업 밭에서 특히 많다[14].',
 '망초는 재배 작물이 아니라 농경지의 문제 잡초로 다뤄진다[14]. 한 종설은 망초와 C. bonariensis 두 종이 함께 콩·목화 같은 주요 밭작물에서 해마다 28–68%의 수량 손실을 일으킨다고 정리했고, 두 종 모두 경운을 하지 않는 보전 농업 밭에서 특히 많다고 했다[14].')
rep('processing','모로코에서는 잎과 꽃을 말려 차로 우려 마시며, 말린 잎·꽃 50 g을',
 '모로코에서는 신선한 잎과 꽃을 차로 우려 마시며, 그늘에 말린 잎·꽃 가루 50 g을')
rep('processing','정유는 사람 병원성 진균에 중간에서 강한 억제 작용을 보였지만 시험한 세균에는 효과가 없었다[5].',
 '정유는 Aspergillus fumigatus를 뺀 사람 병원성 진균에 중간에서 강한 억제 작용을 보였지만 시험한 세균에는 효과가 없었다(시험관)[5].')
rep('safety','오염된 땅이나 길가에서 자란 개체는 중금속을 많이 담을 수 있다[25][26].',
 '오염된 땅에서 자란 개체는 중금속을 많이 담을 수 있다(오염 토양·카드뮴 용액 처리 재배 실험)[25][26].')
rep('safety','꽃 부분의 폴리페놀-다당 성분은 생체 내 항응고 작용과 혈소판 억제 작용을 보였다[9].',
 '망초에서 분리한 폴리페놀-다당 제제는 쥐에서 항응고 작용을 보였고, 아라키돈산으로 유도한 혈소판 응집도 억제했다[9].')
C={c['name']:c for c in d['compounds']}
c=C['Nerolidol']; c['content_text']=c['content_text'].replace('(E)-네롤리돌','네롤리돌(입체 표기는 원문 기호가 깨져 확인하지 못함)')
c=C['Epicatechin']; c['activity_ko']='물 추출물(100·200 mg/kg 복강 투여)의 스코폴라민 유발 쥐 항불안·항우울 유사 작용과 항산화 작용에 관련된 성분 후보로 제시됨[3]'
c=C['3,5-Dicaffeoylquinic acid']; c['activity_ko']='카페오일퀸산류가 추출물의 혈관 이완 작용(적출 쥐 대동맥)에 적어도 일부 기여할 것으로 추정됨[4]'
c=C['Arabinogalactan']; c['activity_ko']='기니피그에서 코데인에 가까운 진해 작용[8]; 다른 제제(다당 부분은 주로 헥수론산)는 쥐에서 항응고 작용[9]'
A={a['compound']:a for a in d['assays']}
a=A['Limonene']['conditions']; a['sample_prep']=a['sample_prep'].replace('유럽약전 6.0 방법으로 2시간 수증기 증류','유럽약전 6.0 방법으로 2시간 수증류(hydrodistillation), 수율은 건조 중량 기준')
a=A['Epicatechin']['conditions']; a['gradient']='A 0–10% 4분, 10–15% 4분, 이후 4분 linear(원문 표현), 15분 동안 85%까지, 마지막 3분 10% A로 복귀'
# drop source 29
d['sources']=[s for s in d['sources'] if s['n']!=29]
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
print('ok')
