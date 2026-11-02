import json,sys
p='/home/user/hfoodguide-wave3/docs/materials/glechoma-hederacea/dossier.json'
d=json.load(open(p))
changes=[]
def rep(where,obj,key,old,new,why):
    s=obj[key]
    assert old in s,(where,old)
    obj[key]=s.replace(old,new,1)
    changes.append({"where":where,"before":old,"after":new,"why":why})
S={s['key']:s for s in d['sections']}
rep('sections.overview',S['overview'],'body',
 '잎에는 우르솔산이 건조중량 1 g당 7.1–7.5 mg 들어 있다[11].',
 '병꽃풀과 G. hirsuta의 잎에는 우르솔산이 건조중량 1 g당 7.1–7.5 mg 들어 있다(두 종을 함께 보고한 값)[11].',
 '[11] 초록의 7.1–7.5 mg/g DW 는 병꽃풀과 G. hirsuta 두 종의 잎을 함께 말한 값임')
rep('sections.biology',S['biology'],'body',
 '암꽃만 피는 포기와 양성화 포기가 함께 있는 자웅이주성(gynodioecy) 식물이다[17].',
 '암꽃만 피는 포기와 양성화 포기가 따로 있는 자성양성이주(gynodioecy) 식물이다[17].',
 'gynodioecy 는 자웅이주(dioecy)가 아니라 자성양성이주')
rep('sections.related_species',S['related_species'],'body',
 'var. longituba에서는 로즈마린산 유사체가, var. grandis 잎차에서는 아피제닌·루테올린이 주요 활성 성분으로 보고되었다[29][30].',
 'var. longituba에서는 로즈마린산 유사체가, var. grandis 잎차에서는 아피제닌·루테올린이 주요 활성 성분으로 보고되었다[29][30]. 대만·한국에서 수행된 일부 연구는 학명을 G. hederacea로 적었지만, 시료가 어느 변종(var. longituba·var. grandis 포함)인지는 초록에서 확인하지 못했다[13][14][16][23][34].',
 '동아시아 시료 연구의 변종 불확실성(긴병꽃풀 자료 섞임 가능성)을 밝힘')
rep('sections.safety',S['safety'],'body',
 '정상 피부세포(HaCaT)와 간세포(HepG2)에 독성을 보이지 않았다[2].',
 '정상 피부 각질세포(HaCaT)와 정상 간세포의 성질을 지닌 간암 유래 세포(HepG2)에 독성을 보이지 않았다[2].',
 '[2] 에서 HepG2 는 간암 유래(hepatocellular carcinoma) 세포주임')
rep('sections.safety',S['safety'],'body',
 '반면 메탄올 추출물과 분획은 사람 말초혈액 단핵세포의 생존율을 24시간 뒤 최대 약 65%까지 낮췄고',
 '반면 70% 메탄올 추출물과 분획은 사람 말초혈액 단핵세포의 생존율을 24시간 뒤 약 65% 수준까지 낮췄고',
 '[5] 는 70% 메탄올 추출, 생존율이 최대 약 65%로 떨어졌다는 뜻')
rep('sections.safety',S['safety'],'body',
 '간암세포(HepG2)의 증식을 억제하고 세포자멸사를 일으켰다[34].',
 '배양 간암세포(HepG2)의 증식을 억제하고 세포자멸사를 일으켰다(시험관)[34].',
 '세포 실험임을 명시(과장 방지)')
C={c['name']:c for c in d['compounds']}
rep('compounds.Rosmarinic acid',C['Rosmarinic acid'],'content_text',
 '60% 분획 101.52 ± 5.76 mg/g[5]; 꽃줄기 5105 ± 362 µg/g, 영양줄기 3218 ± 592 µg/g(2021년)[4]',
 '60% 분획 101.52 ± 5.76 mg/g(분획 무게 기준)[5]; 70% 에탄올 추출물 분석에서 꽃줄기 5105 ± 362 µg/g, 영양줄기 3218 ± 592 µg/g(2021년, 기준 무게는 본문에서 확인하지 못함)[4]',
 '[5] 값은 분획 1 g당, [4] 페놀산 값은 건조물/추출물 기준이 본문에 명시되지 않음')
rep('compounds.Chlorogenic acid',C['Chlorogenic acid'],'content_text',
 '60% 분획 31.77 ± 4.03 mg/g[5]; 꽃줄기 3390 ± 461 µg/g, 영양줄기 1461 ± 363 µg/g[4]',
 '60% 분획 31.77 ± 4.03 mg/g(분획 무게 기준)[5]; 꽃줄기 3390 ± 461 µg/g, 영양줄기 1461 ± 363 µg/g(2021년, 기준 무게는 본문에서 확인하지 못함)[4]',
 '기준(분획/건조물) 명시')
rep('compounds.Rutin',C['Rutin'],'content_text',
 '60% 분획 62.31 ± 0.98 mg/g[5]','60% 분획 62.31 ± 0.98 mg/g(분획 무게 기준)[5]','기준 명시')
rep('compounds.Apigenin',C['Apigenin'],'content_text',
 '85% 분획 26.17 ± 1.44 mg/g[5]; 꽃줄기 97.0 µg/g 건조물, 7월 영양줄기는 검출 안 됨[4]',
 '85% 분획 26.17 ± 1.44 mg/g(분획 무게 기준)[5]; 2021년 6월 꽃줄기 97.0 µg/g 건조물, 2021년 7월 영양줄기는 검출 안 됨[4]',
 '기준·연월 명시')
rep('compounds.Luteolin',C['Luteolin'],'content_text',
 '꽃줄기 39.5 µg/g 건조물, 7월 영양줄기는 검출 안 됨[4]',
 '2021년 6월 꽃줄기 39.5 µg/g 건조물, 2021년 7월 영양줄기는 검출 안 됨[4]','연월 명시')
k="Apigenin 7-O-(6''-O-malonylglucoside)"
rep('compounds.'+k,C[k],'activity_ko',
 'LC-MS/MS와 산가수분해로 확인됨[3][5]',
 'LC-MS/MS와 산가수분해로 확인됨[3]; 다른 연구에서도 주요 플라보노이드로 잠정 동정됨(UHPLC-QTOF-MS)[5]',
 '[5] 는 산가수분해를 하지 않았고 질량분석으로 잠정 동정만 함')
rep('compounds.Ursolic acid',C['Ursolic acid'],'content_text',
 '잎 7.1–7.5 mg/g 건조중량; 지상부 디클로로메탄 가열 환류 건조 추출물 17–25%(w/w)[11]',
 '병꽃풀·G. hirsuta 잎 7.1–7.5 mg/g 건조중량(두 종을 함께 보고); 지상부 디클로로메탄 가열 환류 건조 추출물 17–25%(w/w)(어느 종의 값인지 초록에서 확인하지 못함)[11]',
 '[11] 초록은 두 종을 함께 보고하며 17–25% 는 종명이 빠져 있음')
rep('compounds.Ursolic acid',C['Ursolic acid'],'activity_ko',
 '생쥐 피부 종양 촉진을 억제함[12]','생쥐 피부 종양 촉진을 억제함(동물)[12]','동물 실험 명시')
A=[a for a in d['assays'] if a['compound']=='Ursolic acid'][0]
rep('assays.Ursolic acid.content',A,'content',
 '잎 7.1–7.5 mg/g 건조중량; 지상부 디클로로메탄 가열 환류 건조 추출물 우르솔산 17–25%(w/w)[11]',
 '병꽃풀·G. hirsuta 잎 7.1–7.5 mg/g 건조중량(두 종 함께 보고); 지상부 디클로로메탄 가열 환류 건조 추출물 우르솔산 17–25%(w/w)(종명은 초록에서 확인하지 못함)[11]',
 '두 종 값이 섞여 있음을 명시')
A['part']='잎·지상부(병꽃풀·G. hirsuta)'
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('/home/user/hfoodguide-wave3/docs/materials/glechoma-hederacea/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
