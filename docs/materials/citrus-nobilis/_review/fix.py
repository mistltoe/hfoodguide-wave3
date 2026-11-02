import json
p='/home/user/hfoodguide-wave3/docs/materials/citrus-nobilis/dossier.json'
d=json.load(open(p))
changes=[]
def rep(where,obj,key,old,new,why):
    s=obj[key]
    assert s.count(old)==1,(where,old)
    obj[key]=s.replace(old,new); changes.append({"where":where,"before":old,"after":new,"why":why})
S={s['key']:s for s in d['sections']}
rep('sections.overview',S['overview'],'body',
 "영문명 'Dalandan'으로 팔리는 필리핀 과일 시료는 SSR 분석에서 만다린 쪽에 가깝게 묶였지만, 그 논문이 시료에 붙인 학명은 확인하지 못함[5].",
 "필리핀산 'Dalandan' 시료는 SSR 분석에서 만다린 쪽에 가깝게 묶였지만, 그 논문은 Dalandan 이 인도 'Nagpur'와 비슷한 종명을 공유한다고만 적었고 시료에 붙인 학명은 전문 텍스트에서 빠져 있어 확인하지 못함[5]. 따라서 이 시료 값을 C. nobilis 의 값으로 단정할 수 없다.",
 "[5] 전문은 시료 구입처를 'Philippines'로만 적었고 '팔린다'는 기술이 없음; 'Dalandan and Nagpur both share a similar species name' 문장을 반영해 종 대응을 과장하지 않게 고침")
rep('sections.biology',S['biology'],'body',
 "그 껍질 정유에서는 리모넨이 휘발 성분의 약 86%였고, 만다린과 오렌지를 가르는 지표인 α-시넨살이 일곱 시료 가운데 가장 많았다(약 70 µg/mL)[5].",
 "그 껍질을 디클로로메탄으로 추출한 휘발 성분에서는 리모넨이 약 86%였고, 만다린과 오렌지를 가르는 지표인 α-시넨살이 일곱 시료 가운데 가장 많았다(추출액 기준 약 70 µg/mL)[5].",
 "[5] 의 휘발 성분은 정유(증류·압착)가 아니라 껍질 디클로로메탄 추출물이며 값은 추출액 µg/mL 기준")
rep('sections.cultivation',S['cultivation'],'body',
 "다 자란 나무에서는 잎 살포·줄기 주입 모두 약 1개월 동안 50~70% 수준의 방제에 그쳐 기대보다 효과가 낮았다[18].",
 "다 자란 나무에서는 잎 살포가 약 1개월 동안 50~70%, 줄기 주입이 약 50%의 매개충 치사율에 그쳐 기대보다 효과가 낮았다[18].",
 "[18] 초록: 잎 살포 50~70%, 줄기 주입 약 50%로 구분됨")
rep('sections.processing',S['processing'],'body',
 "C. nobilis Loureiro 껍질은 정유 수율이 가장 높았고(2.91%)",
 "C. nobilis Loureiro 껍질은 정유 수율이 가장 높았고(2.91%, 생껍질 무게 대비 분별증류 정유 부피 기준)",
 "[21] 수율 식이 정유 mL/껍질 g 이므로 기준을 밝힘")
rep('sections.processing',S['processing'],'body',
 "같은 에콰도르산 King 만다린 껍질에서는",
 "에콰도르산 'King 만다린' 껍질(초록의 학명 표기는 확인하지 못함)에서는",
 "[22] 초록은 'King mandarin (… L.)'로만 적혀 학명이 C. nobilis 인지 확인되지 않음")
rep('sections.genetics',S['genetics'],'body',
 "현지에서 오렌지로 불리지만 유전적으로는 만다린에 더 가깝다고 결론지어졌다[5].",
 "현지에서 오렌지로 불리지만 유전적으로는 만다린에 더 가깝다고 결론지어졌다[5]. 이 시료가 C. nobilis 인지는 논문에서 확인하지 못함.",
 "Dalandan 시료의 종 대응을 과장하지 않도록 단서 추가")
C={c['name']:c for c in d['compounds']}
rep('compounds.Sinensetin',C['Sinensetin'],'content_text',"(7개 시료 중 최저)","(폴리메톡시플라본이 검출된 5개 시료 중 최저; 라임 2시료는 흔적량)",
 "[5] 표 1에서 라임 2시료(Chanh Giay·Ma Nao Pan)는 'Trace'로 더 낮음; 본문도 'other five peels' 중 최저라고 씀")
rep('compounds.alpha-Sinensal',C['alpha-Sinensal'],'content_text',"'Dalandan' 껍질 약 70 µg/mL","'Dalandan' 껍질 디클로로메탄 추출액 69.937 ± 5.208 µg/mL",
 "[5] 표 3 원값과 추출 기준을 밝힘")
rep('compounds.Citrunobin',C['Citrunobin'],'class',"아크리돈 알칼로이드로 추정(원 논문 확인 못함)","확인하지 못함",
 "근거 없는 추정 분류 삭제")
A=d['assays']
rep('assays[1].conditions.detection',A[1]['conditions'],'detection',"EI-MS, NIST","단일 사중극자 MS, NIST",
 "[21] 전문에 EI 이온화 표기 없음")
rep('assays[2].method',A[2],'method',"역상 HPLC","HPLC","[6] 초록은 'HPLC analysis'로만 적음(역상은 [8] 의 표현)")
old=list(d['aliases'])
d['aliases']=[a for a in d['aliases'] if a!='Citrus × nobilis']
changes.append({"where":"aliases","before":"Citrus × nobilis","after":"(삭제)","why":"출처 없는 학명 표기; 식약처 목록은 Citrus nobilis Lour."})
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('/home/user/hfoodguide-wave3/docs/materials/citrus-nobilis/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
