import json,sys
p='/home/user/hfoodguide-wave3/docs/materials/sargassum-siliquastrum/dossier.json'
d=json.load(open(p))
changes=[]
def rep(where,obj,key,old,new,why):
    s=obj[key]
    assert s.count(old)==1,(where,old)
    obj[key]=s.replace(old,new); changes.append({"where":where,"before":old,"after":new,"why":why})
S={s['key']:s for s in d['sections']}
rep('sections.overview',S['overview'],'body','한국 고유의 모자반과(Sargassaceae) 갈조류로 소개된다[28]','한국 자생(원문 \'Korean indigenous\') 모자반과(Sargassaceae) 갈조류로 소개된다[28]','[28] 원문은 indigenous(자생)이며 고유종(endemic)이라는 뜻이 아님. 이 종은 일본·중국·홍콩·홍해에서도 채집됨')
rep('sections.history',S['history'],'body','빵에 6% 넣는 방식을 제안했다[35]','모자반속 알긴산 제제를 빵에 6% 넣는 방식을 제안했다[35]','[35] 초록은 빵 6% 첨가를 \'Sargassum species 유래 알긴산 제제\'로 적음 — 꽈배기모자반 한 종으로 한정되지 않음')
rep('sections.biology',S['biology'],'body','중국 하이난섬 맹그로브 연구에서는','중국 하이난 소재 연구진의 맹그로브 먹이그물 연구(초록에 조사지 세부 없음)에서는','[36] 초록에 하이난섬이라는 조사지가 없고 저자 소속만 하이난임')
rep('sections.biology',S['biology'],'body','홍콩 해역의 갈조 3종(꽈배기모자반 포함) 조사에서 건조중량 기준 총 브로모페놀 함량은 계절에 따라 40.9–7030 ng/g으로 크게 달랐고, 겨울에 높고 여름에 낮았다[33].','홍콩 해역의 갈조 3종(Padina arborescens·꽈배기모자반·Lobophora variegata) 조사에서 건조중량 기준 총 브로모페놀 함량은 3종을 합쳐 계절에 따라 40.9–7030 ng/g으로 크게 달랐고, 겨울에 높고 여름에 낮았다[33]. 이 범위는 3종을 합친 값이며 대체로 Lobophora variegata가 가장 높았으므로 꽈배기모자반만의 값이 아니다(초록에 종별 값 없음)[33].','여러 종을 합친 범위가 이 종 값처럼 읽히지 않게 함. [33] 초록: L. variegata 의 TBC 가 대체로 가장 높음')
rep('sections.safety',S['safety'],'body','1991년 연구에서 꽈배기모자반 알긴산나트륨은 쥐의 스트론튬 체내 부담을 3.3–4.2배 줄였고, 사람 자원자에서 위장 기능 이상이나 칼슘·철·구리·아연 대사 변화는 관찰되지 않았다[35].','1991년 연구에서 꽈배기모자반 알긴산나트륨은 쥐의 스트론튬 체내 부담을 3.3–4.2배 줄였고, 동물과 사람 자원자 시험에서 위장 기능 이상이나 칼슘·철·구리·아연 대사 변화는 관찰되지 않았다[35]. 다만 이는 정제한 알긴산나트륨 제제의 결과로, 꽈배기모자반 엽체 자체를 먹은 안전성 자료가 아니며 사람 시험에 쓴 제제의 원료 종은 초록에 명시되지 않았다[35].','정제 알긴산 결과를 해조 섭취 안전성으로 과대 해석하지 않게 함; 초록상 사람 시험 제제의 종 불명')
C={c['name']:c for c in d['compounds']}
rep('compounds.Sodium alginate',C['Sodium alginate'],'activity_ko','사람 자원자에서 안정 스트론튬 흡수를 78%(±8.9) 줄였다[35]','사람 자원자에서 안정 스트론튬 흡수를 78%(±8.9) 줄였다(사람 시험에 쓴 제제의 원료 종은 초록에 명시 없음)[35]','[35] 초록 범위로 한정')
b=C['2,4,6-Tribromophenol']
old=dict(name=b['name'],name_ko=b['name_ko'],content_text=b['content_text'])
b['name']='Bromophenols (total)'
b['name_ko']='브로모페놀류(총량; 2,4,6-트라이브로모페놀 등 5종)'
b['class']='브로모페놀(향미 성분)'
b['content_text']='갈조 3종(Padina arborescens·꽈배기모자반·Lobophora variegata)을 합친 계절별 범위 40.9–7030 ng/g(건조중량)이며 Lobophora가 대체로 가장 높음; 꽈배기모자반만의 값은 초록에 없음'
changes.append({"where":"compounds.2,4,6-Tribromophenol","before":json.dumps(old,ensure_ascii=False),"after":json.dumps({k:b[k] for k in old},ensure_ascii=False),"why":"[33] 은 5종 브로모페놀의 총량(TBC)을 3종 합친 범위로 보고 — 단일 성분 2,4,6-TBP 값처럼 보이던 이름·함량을 총량·3종 합산으로 바로잡음"})
A=[a for a in d['assays'] if a['compound'].startswith('Bromophenols')][0]
rep('assays.Bromophenols',A,'content','갈조 3종(꽈배기모자반 포함) 총 브로모페놀 40.9–7030 ng/g(건조중량, 계절별 범위; 겨울 높고 여름 낮음); 30% 꽈배기모자반 사료 340 ng/g','갈조 3종(Padina arborescens·꽈배기모자반·Lobophora variegata)을 합친 총 브로모페놀 40.9–7030 ng/g(건조중량, 계절별 범위; 겨울 높고 여름 낮음; Lobophora가 대체로 가장 높음 — 꽈배기모자반만의 값 아님); 꽈배기모자반 30% 첨가 사료 자체의 함량 340 ng/g(사료 기준, 대조 사료 8.9 ng/g)','3종 합산 범위와 사료 기준 값을 명시')
src={s['n']:s for s in d['sources']}
o=src[26]['title']; src[26]['title']=o.replace('Food Res Int 201:115566','Food Res Int 2025;201:115566')
changes.append({"where":"sources[26].title","before":o,"after":src[26]['title'],"why":"PubMed 서지: 2025;201:115566(2024-12 온라인)"})
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open(p.replace('dossier.json','_review/changes.json'),'w'),ensure_ascii=False,indent=1)
print(len(changes))
