import json,re
p='dossier.json'; d=json.load(open(p))
S={s['key']:s for s in d['sections']}
b=S['safety']['body']
old=" 다른 41건 분석에서는 80%가 증상이 없었고, 빅토리아주 조사에서는 사고의 74%가 집 안 증기흡입기를 통해 일어났다[26, 27]."
assert old in b; b=b.replace(old,"")
b=b.replace("JECFA는 2003년 유칼립톨을 향료로서 현재 섭취 수준에서 안전성 우려 없음으로 평가했다고 WebSearch 요약으로만 확인했다[29].","JECFA는 2003년 유칼립톨을 향료로서 현재 섭취 수준에서 안전성 우려 없음으로 평가했다고 WebSearch 요약으로만 확인했다[29].")
S['safety']['body']=b
# renumber: drop 26,27
used=set()
def refs(t): 
    for m in re.finditer(r'\[([\d,\s]+)\]',t):
        for x in m.group(1).split(','): used.add(int(x))
blob=json.dumps(d,ensure_ascii=False)
for s in d['sections']: refs(s['body'])
for k in ('compounds','assays'):
    for it in d[k]:
        used.update(it.get('source',[]))
        for v in it.values():
            if isinstance(v,str): refs(v)
            if isinstance(v,dict):
                for vv in v.values():
                    if isinstance(vv,str): refs(vv)
keep=[s for s in d['sources'] if s['n'] in used]
mp={s['n']:i+1 for i,s in enumerate(keep)}
print('dropped',[s['n'] for s in d['sources'] if s['n'] not in used])
def sub(t): return re.sub(r'\[([\d,\s]+)\]',lambda m:'['+', '.join(str(mp[int(x)]) for x in m.group(1).split(','))+']',t)
for s in d['sections']: s['body']=sub(s['body'])
for k in ('compounds','assays'):
    for it in d[k]:
        it['source']=[mp[x] for x in it['source']]
        for kk,v in it.items():
            if isinstance(v,str): it[kk]=sub(v)
            if isinstance(v,dict):
                for k2,vv in v.items():
                    if isinstance(vv,str): v[k2]=sub(vv)
for s in keep: s['n']=mp[s['n']]
d['sources']=keep
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
print(len(S['safety']['body']))
