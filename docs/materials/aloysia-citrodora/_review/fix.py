import json,re,sys
P='dossier.json'
d=json.load(open(P))
changes=[]
def sec(k): return next(s for s in d['sections'] if s['key']==k)
def rep(where,obj,key,old,new,why):
    assert old in obj[key],(where,old)
    obj[key]=obj[key].replace(old,new); changes.append({"where":where,"before":old,"after":new,"why":why})
rep('sections.overview',sec('overview'),'body',"따라서 일반 식품에는 잎만 쓸 수 있고, 줄기·꽃·뿌리는","따라서 이 목록에서 식품원료로 쓸 수 있는 부위는 잎이며, 줄기·꽃·뿌리는","표현 정리(목록의 사용 조건 원문 '사용가능부위 : 잎' 범위로)")
rep('sections.biology',sec('biology'),'body',"물에 녹는 성분으로는 이리도이드 배당체","정유 외의 성분으로는 이리도이드 배당체","출처 [4] 는 'apart from the volatile fraction' 이라 썼고 수용성이라고 하지 않음")
rep('sections.biology',sec('biology'),'body',"잎에 생긴 균은 Oidium aloysiae","이 식물에 생긴 균은 Oidium aloysiae","출처 [20] 초록은 부위(잎)를 밝히지 않음")
rep('sections.related_species',sec('related_species'),'body',"레몬 향 허브인 레몬밤(Melissa officinalis)과 레몬그라스(Cymbopogon citratus)는 다른 과의 식물로, 식품원료 목록에 따로 올라 있다[1].","레몬 향 허브인 레몬밤(Melissa officinalis)과 레몬그라스(Cymbopogon citratus)는 레몬버베나와 다른 종으로, 식품원료 목록에 따로 올라 있다[1].","출처 [1](I1020)에는 과(科) 정보가 없음; 레몬밤잎·레몬그라스잎 등 별도 행 존재는 확인")
rep('sections.cultivation',sec('cultivation'),'body',"0.4–2.1%(v/w)로 집단마다 크게 달랐지만 대부분 유럽약전 규격을 충족했고","0.4–2.1%(v/w)로 집단마다 크게 달랐지만 대부분의 시료가 유럽약전 규격을 충족했고","출처 [5] 는 '대부분의 시료'가 규격을 충족했다고 씀(수율만의 규격으로 한정하지 않음)")
rep('sections.cultivation',sec('cultivation'),'body',"포르투갈의 차 회사가 고른 '리저브' 로트는","차 회사들이 내놓은 '리저브' 로트는","출처 [25] 초록에 회사 국적(포르투갈) 언급 없음")
rep('sections.processing',sec('processing'),'body',"장 단계에서 20.8% 줄었고, 그만큼 이소베르바스코사이드와 카페산이 늘었다[2].","장 단계에서 20.8% 줄었고, 대신 이소베르바스코사이드(마른 잎 1 g당 2.5→4.10 mg)와 카페산(흔적량→1.0 mg)이 늘었다[2].","출처 [2] 는 감소량과 증가량이 같다고 하지 않음('그만큼' 과장) — 원문 수치로 바꿈")
rep('sections.safety',sec('safety'),'body',"잎에 한해 '사용가능' 원료이므로 잎 외의 부위는 식품에 쓸 수 없다[1].","'사용가능' 원료로 올라 있지만 사용가능부위는 잎뿐이라, 잎 외의 부위는 이 목록에서 식품원료로 확인되지 않는다[1].","출처 [1] 의 사용 조건 원문 범위로 표현을 맞춤")
rep('sections.safety',sec('safety'),'body',"EMA 약초위원회 모노그래프는 잎 허브차를 다루며 이상반응을 '알려진 바 없음'으로 적었고, 초안에서는 어린이 사용을 권하지 않았다(원문 미확인, 검색 요약)[23].","EMA 약초위원회의 최종 EU 모노그래프는 이상반응을 '알려진 바 없음'으로 적고, 자료가 부족하다는 이유로 어린이와 임신·수유 중 사용을 권하지 않는다(원문은 열지 못하고 검색 요약으로만 확인)[23].","검토자 WebSearch 요약에서 최종판 기준으로 어린이 비권장·임신수유 비권장·이상반응 알려진 바 없음 확인('초안' 한정 아님); 원문 미확인")
# compounds
c=next(x for x in d['compounds'] if x['name']=='Verbascoside')
old=c['content_text']
c['content_text']=old.replace("; 버베나·레몬버베나 수성 제제의 페닐프로파노이드 16–120 mg/g 건조 추출물 중 최대 97%(두 식물 제제를 함께 보고)[8]","")
assert c['content_text']!=old
changes.append({"where":"compounds[Verbascoside].content_text","before":"…; 버베나·레몬버베나 수성 제제의 페닐프로파노이드 16–120 mg/g 건조 추출물 중 최대 97%(두 식물 제제를 함께 보고)[8]","after":"(삭제)","why":"[8] 의 수치는 버베나(Verbena officinalis)와 레몬버베나 제제를 합친 범위라 이 종 값으로 쓸 수 없음 — 다른 종 자료 섞임"})
c['source']=[s for s in c['source'] if s!=8]
a=d['assays'][0]
old=a['rationale']
a['rationale']="잎을 우린 물에서 가장 많은 페놀이 베르바스코사이드이고, 소화 뒤 시료의 DPPH·MGO 사전 반응 HPLC에서 베르바스코사이드와 그 이성질체가 라디칼 소거·메틸글리옥살 포착의 주된 기여 성분으로 확인되어 지표로 쓰임(루테올린-7-O-이글루쿠로나이드는 반응성이 낮았음); 전문 확인, LOD·LOQ·회수율은 본문에 없음[2]."
changes.append({"where":"assays[0].rationale","before":old,"after":a['rationale'],"why":"출처 [2] 는 L7DG 의 라디칼 포착 활성이 낮다고 썼음 — '플라본 이글루쿠로나이드와 함께 활성을 설명' 은 원문과 다름"})
# remove source 8 and renumber
srcs=[s for s in d['sources'] if s['n']!=8]
mp={s['n']:i+1 for i,s in enumerate(srcs)}
for i,s in enumerate(srcs): s['n']=i+1
d['sources']=srcs
def renum(text):
    return re.sub(r'\[(\d+(?:\s*,\s*\d+)*)\]',lambda m:'['+', '.join(str(mp[int(x)]) for x in re.split(r'\s*,\s*',m.group(1)))+']',text)
for s in d['sections']: s['body']=renum(s['body'])
for k in ['compounds','assays']:
    for x in d[k]:
        for f in list(x):
            if isinstance(x[f],str): x[f]=renum(x[f])
        x['source']=[mp[n] for n in x['source']]
s23=next(s for s in d['sources'] if 'European Medicines Agency' in s['publisher'])
s23['title']=s23['title'].replace("WebSearch 결과 요약으로만 확인함","WebSearch 결과 요약으로만 확인함(최종 모노그래프 PDF: final-european-union-herbal-monograph-aloysia-citrodora-palau…folium_en.pdf)")
json.dump(d,open(P,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
