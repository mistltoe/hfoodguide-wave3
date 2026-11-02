import json,sys
p='/home/user/hfoodguide-wave3/docs/materials/shorea-robusta/dossier.json'
d=json.load(open(p))
changes=[]
def rep(where,obj,key,old,new,why):
    s=obj[key]
    assert s.count(old)==1,(where,old)
    obj[key]=s.replace(old,new); changes.append({"where":where,"before":old,"after":new,"why":why})
S={s['key']:s for s in d['sections']}
rep('sections.overview',S['overview'],'body',
 '같은 Shorea 속의 다른 종에서 얻는 일리페 버터와는 다른 원료이며, 이 자료는 S. robusta만 다룬다[22].',
 '같은 Shorea 속의 다른 종에서 얻는 일리페 버터와는 다른 원료로, 「식품원료 목록」에도 일리페오일(Shorea spp., 사용가능부위 : 씨앗)이 따로 올라 있으며, 이 자료는 S. robusta만 다룬다[1, 22].',
 '일리페와 구분하는 근거를 국내 식품원료 목록(별도 항목 일리페오일, Shorea spp.)으로 보강; [22]는 원문 미확인')
rep('sections.history',S['history'],'body',
 '쥐 실험에서 수지 추출물 연고가 상처 회복을 앞당겼다[15]',
 '랫드 실험에서 수지 메탄올 추출물의 분획과 수지 정유를 10% 넣은 연고가 절개·절제 상처 회복을 앞당겼다(동물 실험)[15]',
 '[15] 초록: 효과가 뚜렷한 것은 석유에테르·벤젠 불용 분획(SRPEBIME)과 정유(SREO)이며 Wistar 랫드 실험 — 대상·제제를 정확히 하고 동물 결과임을 밝힘')
rep('sections.biology',S['biology'],'body',
 '인도 동부 숲 870개 방형구 조사에서는 연구 지역의 약 12.13%가 사라수의 적합 서식지로 가장 넓었다[13].',
 '인도 동부(자르칸드·비하르·서벵골) 숲 870개 방형구 조사 자료로 만든 서식지 모형(MaxEnt)에서는 현재 기후에서 연구 지역의 약 12.13%가 사라수의 적합 서식지로, 조사한 6종 중 가장 넓었다[13].',
 '[13] 초록: 12.13%는 방형구 실측이 아니라 MaxEnt 모형의 적합 서식지 면적')
rep('sections.biology',S['biology'],'body',
 '잎은 탄닌 함량이 높아 타사르누에(Antheraea mylitta)를 키우면 성적이 나빴고,',
 '잎은 타사르누에(Antheraea mylitta)의 다른 먹이식물보다 탄닌과 산화환원 금속이 많았고, 이 잎으로 키우면 애벌레 성적이 나쁘며 애벌레 조직에 산화 스트레스가 커졌다(탄닌이 원인이라고 확정한 것은 아님)[21].',
 '[21] 초록은 성적 저하의 이유가 밝혀지지 않았다고 하고 탄닌·금속과 산화 스트레스의 연관만 제시 — 인과 표현 완화')
rep('sections.biology',S['biology'],'body',
 ' 네팔에서는 아시아코끼리 먹이의 6.3%를 차지했다[21, 24].',
 ' 네팔 파르사 야생동물보호구역·치트완 국립공원에서는 아시아코끼리 먹이의 6.3%를 차지했다[24].',
 '출처 분리 및 조사 지역 명시([24] 초록)')
rep('sections.cultivation',S['cultivation'],'body',
 '사라수 지방은 재배 농장보다 천연 사라수 숲에서 모은 씨앗으로 만든다[2]. 인도 데라둔(우타라칸드) 연구에서는',
 '사라수 씨앗과 기름을 짜고 남은 깻묵은 숲에서 나는 임산 자원(forest-based)으로 다뤄진다[19]. 인도 데라둔(우타라칸드) 연구에서도 씨앗을 숲에서 모았으며,',
 '[2]는 재배 농장과의 비교를 말하지 않음 — 일반화를 빼고 [19]의 forest-based 표현과 [2]의 채집 사실로 한정')
rep('sections.cultivation',S['cultivation'],'body',
 '5–6월에 숲에서 씨앗을 모아 햇볕에 말린 뒤 냉장 보관했다[2].',
 '5–6월에 모은 씨앗을 햇볕에 말린 뒤 냉장 보관했다[2].','위 문장과 합치며 중복 제거')
C={c['name']:c for c in d['compounds']}
rep('compounds.Palmitic acid.activity_ko',C['Palmitic acid'],'activity_ko',
 '코코아버터보다 적은 편이라고 비교됨[2]',
 '팔미트산이 많은 팜유와 달리 사라수 기름은 스테아르산이 주성분이라는 점이 대비됨[2]',
 '[2] 전문에 팔미트산을 코코아버터와 비교한 문장 없음(팜유와 대비)')
rep('compounds.gamma-Linolenic acid.content_text',C['gamma-Linolenic acid'],'content_text',
 '총지방산의 6.86%(한 연구, GC 머무름 시간 대조로 동정)[2]',
 '총지방산의 6.86%(한 연구, GC 머무름 시간 대조로 동정; 같은 논문이 ω-6 지방산 합계를 1.95%로 적어 수치가 서로 맞지 않음)[2]',
 '[2] 전문 결과 절: GLA 6.86%와 ω-6 합계 1.95%가 함께 적혀 있어 내부 불일치 — 독자 주의')
rep('compounds.Germacrene D.content_text',C['Germacrene D'],'content_text',
 '심재·수지 정유의 주성분(정유 중 확인 성분 각각 80.35%·78.43% 차지)[17]',
 '심재·수지 정유 모두의 주성분(함량 수치는 초록에 없음; 확인된 9종·17종 성분이 각 정유의 80.35%·78.43%)[17]',
 '[17] 초록: 80.35%·78.43%는 확인된 성분 전체의 비율이지 게르마크렌 D 함량이 아님')
for s in d['sources']:
    if s['n']==16:
        old=s['title']; s['title']=old.replace('Biomed Pharmacother 2018 (초록)','Biomed Pharmacother 2018;99:286-289 (초록)')
        changes.append({"where":"sources[16].title","before":old,"after":s['title'],"why":"권·쪽 보완(PubMed 서지)"})
old=list(d['aliases']); d['aliases']=[a for a in d['aliases'] if a!='sal butter']
changes.append({"where":"aliases","before":"sal butter 포함","after":"sal butter 삭제","why":"인용 출처([2][3])는 Sal fat·Sal oil·sal seed oil 만 씀 — 출처 없는 별명"})
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open(p.replace('dossier.json','_review/changes.json'),'w'),ensure_ascii=False,indent=1)
print(len(changes))
