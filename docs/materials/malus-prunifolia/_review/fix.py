import json,re
P='/home/user/hfoodguide-wave3/docs/materials/malus-prunifolia/'
d=json.load(open(P+'dossier.json'))
changes=[]
def sec(k): return next(s for s in d['sections'] if s['key']==k)
def rep(where,obj,key,old,new,why):
    assert old in obj[key],(where,old)
    obj[key]=obj[key].replace(old,new); changes.append({"where":where,"before":old,"after":new,"why":why})

rep('sections.overview',sec('overview'),'body',
 "열매 유래 다당류와 추출물의 항염증·지질 개선 효과는 세포·생쥐 실험 결과이며, 사람을 대상으로 한 임상시험은 확인하지 못함[6, 8, 9].",
 "꽃사과 효소 가수분해물에서 얻은 다당류의 항염증 효과(세포·생쥐)와, 벚잎꽃사과를 포함한 세 꽃사과 조추출물의 콜레스테롤 저하 효과(생쥐, 초록에서는 어느 종의 추출물인지 구분되지 않음)가 보고되었을 뿐이며, 사람을 대상으로 한 임상시험은 확인하지 못함[6, 8, 9].",
 "[8] 초록은 가수분해물의 원료 부위를 밝히지 않음('열매 유래' 근거 없음), [6] 은 M. 'Red jade'·M. hupehensis·M. prunifolia 추출물 중 '일부'가 효과를 냈다고만 씀")
rep('sections.safety',sec('safety'),'body',
 "꽃사과 추출물이 고지방식 비만 생쥐의 혈청 콜레스테롤을 낮춘 결과도 있다[6].",
 "M. 'Red jade'·M. hupehensis·벚잎꽃사과 세 꽃사과의 조추출물 가운데 일부가 고지방식 비만 생쥐의 혈청 콜레스테롤을 낮췄으나, 초록에서는 어느 종의 추출물인지 구분되지 않는다[6].",
 "[6] 은 세 종 추출물 중 'some of these extracts' 라고만 씀 — 벚잎꽃사과 효과로 읽히지 않게 고침")
rep('sections.cultivation',sec('cultivation'),'body',
 "잎에는 갈색무늬병(Marssonina apple blotch)이 생기며, 품종 '둥훙궈(Donghongguo)'에서 멜라토닌 전처리가 저항성을 높였다[27].",
 "품종 '둥훙궈(Donghongguo)'의 잎에 갈색무늬병(Marssonina apple blotch)균을 접종한 실험에서 멜라토닌 전처리가 저항성을 높였다[27].",
 "[27] 은 접종·전처리 실험이며 자연 발생 피해를 보고한 것이 아님")
rep('sections.related_species',sec('related_species'),'body',
 "문헌 검색에서 'Malus prunifolia'로 걸리는 논문 가운데에도 다른 종 자료가 있는데, 예를 들어 한 엽록체 유전체 논문은 키워드상 M. toringoides를 다룬 것이다[22]. ",
 "",
 "[22] 는 M. toringoides 엽록체 유전체 논문으로 이 종 자료가 아님 — 문장과 출처 삭제")
# compounds
for c in d['compounds']:
    if 6 in c['source'] and c['name']!='Hyperoside':
        old=c['activity_ko']
        if '[6]' in old and '세 꽃사과' not in old:
            new=old.replace('[6]','(M. \'Red jade\'·M. hupehensis·벚잎꽃사과 세 종 조추출물을 함께 분석, 생쥐 혈청 지질과의 통계적 상관과 기존 문헌 근거)[6]')
            changes.append({"where":f"compounds.{c['name']}.activity_ko","before":old,"after":new,"why":"[6] 은 세 꽃사과 혼합 분석이며 개별 화합물의 활성은 기존 문헌 인용"}); c['activity_ko']=new
    if c['name']=='Hyperoside':
        old=c['activity_ko']; new="꽃사과(M. 'Red jade'·M. hupehensis·벚잎꽃사과) 조추출물에서 콜레스테롤 저하 활성과 상관된 성분으로 분리·동정(생쥐 실험 기반, 종 구분 없음)[6]"
        changes.append({"where":"compounds.Hyperoside.activity_ko","before":old,"after":new,"why":"[6] 혼합 종 분석임을 명시"}); c['activity_ko']=new
    if c['name']=='Chlorogenic acid':
        old=c['activity_ko']; new="벚잎꽃사과에서 확인된 페놀산 중 하나(항산화능과 높은 상관은 갈산·EGCG에 대해 보고됨)[5]"
        changes.append({"where":"compounds.Chlorogenic acid.activity_ko","before":old,"after":new,"why":"[5] 초록은 클로로겐산을 항산화 성분으로 지목하지 않음"}); c['activity_ko']=new
# assays
a=d['assays'][2]
rep('assays[2].part',a,'part',"열매(신장 수집, 4개 성숙 단계, 씨 제거)","열매(신장 수집, 4개 성숙 단계; 일부 시료는 씨 제거, 대사체 분석 시료의 씨 제거 여부는 원문에 분명하지 않음)","[2] 방법: 'A portion of the sample was deseeded', 나머지는 통째 동결")
a=d['assays'][0]
rep('assays[0].content',a,'content',"말산이 유기산 중 우세하고 성숙하며 감소;","말산이 유기산 중 우세하고 성숙하며 감소(유기산 함량은 건물(DW) 기준으로 산출);","[3] 2.2.3: 'Organic-acid content (ng·g DW)' — 건물 기준 명시")
# aliases
old=list(d['aliases']); d['aliases']=[x for x in d['aliases'] if not x.startswith('Marubakaido')]
changes.append({"where":"aliases","before":"Marubakaido (var. ringo)","after":"(삭제)","why":"[28] 에서 Marubakaido 는 대목 품종명(cv.)이지 종의 별명이 아님"})
# remove source 22 & renumber
S=[s for s in d['sources'] if s['n']!=22]
mp={s['n']:i+1 for i,s in enumerate(S)}
for s in S: s['n']=mp[s['n']]
d['sources']=S
def rn(t):
    return re.sub(r'\[([\d,\s]+)\]',lambda m:'['+', '.join(str(mp[int(x)]) for x in m.group(1).split(','))+']',t)
for s in d['sections']: s['body']=rn(s['body'])
for lst in ('compounds','assays'):
    for c in d[lst]:
        for k,v in c.items():
            if isinstance(v,str): c[k]=rn(v)
            if k=='source': c[k]=[mp[x] for x in v]
            if k=='conditions':
                for kk,vv in v.items(): v[kk]=rn(vv)
json.dump(d,open(P+'dossier.json','w'),ensure_ascii=False,indent=1)
json.dump(changes,open(P+'_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
