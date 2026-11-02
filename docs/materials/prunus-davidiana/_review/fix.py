import json,re,sys
p='/home/user/hfoodguide-wave3/docs/materials/prunus-davidiana/dossier.json'
d=json.load(open(p))
S={s['key']:s for s in d['sections']}
def rep(key,old,new):
    b=S[key]['body']; assert old in b,(key,old); S[key]['body']=b.replace(old,new)
rep('overview',"논문에서는 주로 Amygdalus davidiana라는 이명이 쓰인다[1, 15, 17, 18]","일부 논문에서는 Amygdalus davidiana라는 이명이 쓰인다[1, 15, 17, 18]")
rep('overview',"자생 범위는 중국에서 한국까지로 정리되어 있으나, 이는 검색 요약으로만 확인한 내용이다[6].","자생 범위는 공공 식물 목록 원문으로 확인하지 못함. 중국 북부 난온대 낙엽수림에서 시베리아살구와 함께 자라는 집단을 다룬 연구가 있다[18].")
rep('overview',"식용 부위인 열매의 성분 연구는 적다[4, 10, 21]","식용 부위인 열매의 성분 연구는 적다[4, 5, 9, 10, 21]")
rep('processing',"열매에서 우르솔산·코로솔산·α-아미린 같은 트리테르페노이드를 분리했다는 국내 보고가 있으나, 원문은 열지 못하고 검색 요약으로만 확인했다[7].","열매에서 트리테르페노이드를 분리했다는 국내 학술지 보고가 있다는 검색 요약이 있으나, 원문과 PubMed 어디에서도 확인하지 못해 성분 이름과 함량은 적지 않는다(확인하지 못함)[7].")
rep('safety',"줄기 추출물·프루닌의 혈당·지질 개선 결과는 대부분 흰쥐 복강 주사나 세포 실험이어서 열매 섭취 효과의 근거가 되지 않는다[10, 11, 12, 14].","줄기 추출물·프루닌의 혈당·지질 개선 결과는 모두 흰쥐 복강 주사 또는 효소·세포 실험이어서, 경구 섭취 결과도 아니고 열매 섭취 효과의 근거도 되지 않는다[10, 11, 12, 14].")
d['compounds']=[c for c in d['compounds'] if c['name'] not in ('Ursolic acid','Corosolic acid','alpha-Amyrin')]
for c in d['compounds']:
    if c['name']=='Kaempferol':
        c['activity_ko']="신장 균질액의 총 ROS·하이드록실 라디칼 계에서 억제 활성 평가(개별 화합물 결과는 초록에 없음) — 시험관 결과[13]"
    if c['name']=='Arabinogalactan':
        c['activity_ko']="인간화 노화 변비 모델에서 장내 세균·트립타민·5-HT 신호를 통해 변비 완화(초록에 모델 종 명시 없음) — 생체 모델 결과[16]"
for s in d['sources']:
    if s['n']==7:
        s['title']="산복사나무 열매의 트리테르페노이드 분리 보고 — 국내 학술지 논문(koreascience 원문은 열지 못했고 PubMed 에도 없어 WebSearch 검색 요약으로만 존재를 확인; 성분·함량은 확인하지 못함)"
# remove source 6, renumber
old=[s['n'] for s in d['sources'] if s['n']!=6]
m={o:i+1 for i,o in enumerate(old)}
d['sources']=[s for s in d['sources'] if s['n']!=6]
for s in d['sources']: s['n']=m[s['n']]
def fixtxt(t):
    def f(mo):
        ns=[int(x) for x in re.split(r',\s*',mo.group(1))]
        assert 6 not in ns,t
        return '['+', '.join(str(m[x]) for x in ns)+']'
    return re.sub(r'\[(\d+(?:,\s*\d+)*)\]',f,t)
def walk(o):
    if isinstance(o,dict):
        for k,v in o.items():
            if k=='source' and isinstance(v,list): o[k]=[m[x] for x in v]
            elif k in ('sources',): continue
            else: o[k]=walk(v)
        return o
    if isinstance(o,list): return [walk(x) for x in o]
    if isinstance(o,str): return fixtxt(o)
    return o
for k in list(d):
    if k!='sources': d[k]=walk(d[k])
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
print('ok')
