import json,re,sys
st=json.load(open(sys.argv[1])); d=st['d']
drop={33}
txt=json.dumps(d,ensure_ascii=False)
keep=[s['n'] for s in d['sources'] if s['n'] not in drop]
m={o:i+1 for i,o in enumerate(keep)}
def fixbr(mo):
    parts=[p.strip() for p in mo.group(1).split(',')]
    assert all(p.isdigit() for p in parts),mo.group(0)
    new=[str(m[int(p)]) for p in parts if int(p) not in drop]
    return '['+', '.join(new)+']' if new else ''
def walk(o):
    if isinstance(o,dict):
        for k,v in o.items():
            if k=='source' and isinstance(v,list): o[k]=[m[x] for x in v if x not in drop]
            elif k=='sources': continue
            else: o[k]=walk(v)
        return o
    if isinstance(o,list): return [walk(x) for x in o]
    if isinstance(o,str): return re.sub(r'\[(\d+(?:\s*,\s*\d+)*)\]',fixbr,o)
    return o
walk(d)
d['sources']=[dict(s,n=m[s['n']]) for s in d['sources'] if s['n'] not in drop]
json.dump(d,open('dossier.json','w'),ensure_ascii=False,indent=1)
json.dump(st['changes'],open('_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(d['sources']))
