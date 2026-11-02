import json,re,sys
p=sys.argv[1]
d=json.load(open(p))
S={s['key']:s for s in d['sections']}
def rep(k,a,b):
    t=S[k]['body']; assert a in t,(k,a[:40]); S[k]['body']=t.replace(a,b)
rep('overview',"바닥에 사는 대형 어종으로 동북아시아 연안에 분포하며","난온대 바다의 바닥에 사는 대형 어종으로 동북아시아에 분포하며")
rep('overview'," 국내에서는 주로 서해안과 남해 서부 연안에 분포한다고 기록된 국내 논문이 있으나, 원문을 열지 못해 검색 요약으로만 확인했다[25].","")
rep('overview',"이 원료는 건강기능식품 고시형 원료의 원재료가 아니어서 고시 지표성분은 없다[1].","건강기능식품 고시형 원료로는 이번 조사에서 확인하지 못해 고시 지표성분은 적지 않는다.")
rep('history',"국내에서는 1990년대 참서대과 분포 연구와 2010년 서해에서 잡은 개체로 암컷 성숙·산란을 조사한 2012년 연구가 있으나, 두 논문 모두 원문을 열지 못해 검색 요약으로만 확인했다[24, 25].","국내 연안의 분포·성숙·산란 연구는 원문을 열지 못해 이번 조사에서 확인하지 못함.")
rep('biology',"박대는 온대 바다의 바닥에 사는 큰 저서성 넙치류로","박대는 난온대 바다의 바닥에 사는 큰 저서성 넙치류로")
rep('biology'," 국내 서해 개체를 조사한 연구에서 암컷의 생물학적 최소형은 전장 46.87 cm였다는 내용은 검색 요약으로만 확인했다[24].","")
rep('related_species',"참서대과 어류는 겉모습이 비슷해 유통 어종을 가리는 다중 PCR 판별법이 국내에서 개발되었고 박대도 대상에 들어 있다는 내용은 검색 요약으로만 확인했다[26].","참서대과 어류의 국내 유통 어종 판별(유전자 판별법) 연구는 원문을 열지 못해 이번 조사에서 확인하지 못함.")
rep('safety',"이 원료는 건강기능식품 고시형 원료가 아니어서 고시 섭취 시 주의사항은 없다[1].","건강기능식품 고시형 원료로는 이번 조사에서 확인하지 못해 고시 섭취 시 주의사항은 적지 않는다.")
d['aliases']=[a for a in d['aliases'] if a!='Tongue sole']
for c in d['compounds']:
    if c['name']=='Pyroglutamic acid': c['part']='근육(양식어)'
# renumber sources: drop 24,25,26
drop={24,25,26}
keep=[s for s in d['sources'] if s['n'] not in drop]
m={s['n']:i+1 for i,s in enumerate(keep)}
for s in keep: s['n']=m[s['n']]
d['sources']=keep
def remap(t):
    def f(mo):
        nums=[int(x) for x in re.split(r'\s*,\s*',mo.group(1))]
        return '['+', '.join(str(m[n]) for n in nums)+']'
    return re.sub(r'\[(\d+(?:\s*,\s*\d+)*)\]',f,t)
def walk(x):
    if isinstance(x,dict):
        for k,v in x.items():
            if k=='source' and isinstance(v,list): x[k]=[m[n] for n in v]
            else: x[k]=walk(v)
        return x
    if isinstance(x,list): return [walk(y) for y in x]
    if isinstance(x,str): return remap(x)
    return x
for k in ('sections','compounds','markers','assays','nutrients','production','world','gi','orgs'):
    d[k]=walk(d[k])
src9=[s for s in d['sources'] if 'microsatellite' in s['title']][0]; src9['publisher']='Marine Genomics 9:17-23, 2013(온라인 2012)'
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
