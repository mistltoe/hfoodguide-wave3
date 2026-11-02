import json,re,sys
p=sys.argv[1]; d=json.load(open(p))
changes=d.pop('_changes')
json.dump(changes,open('_review/changes.json','w'),ensure_ascii=False,indent=1)
txt=json.dumps(d,ensure_ascii=False)
used=set()
for m in re.finditer(r'\[(\d+(?:\s*,\s*\d+)*)\]',txt):
    used|={int(x) for x in m.group(1).split(',')}
def collect(o):
    if isinstance(o,dict):
        for k,v in o.items():
            if k=='source' and isinstance(v,list): used.update(v)
            else: collect(v)
    elif isinstance(o,list):
        for x in o: collect(x)
collect({k:v for k,v in d.items() if k!='sources'})
keep=[s for s in d['sources'] if s['n'] in used]
mp={s['n']:i+1 for i,s in enumerate(keep)}
print('dropped',[s['n'] for s in d['sources'] if s['n'] not in used])
def fixstr(s):
    return re.sub(r'\[(\d+(?:\s*,\s*\d+)*)\]',lambda m:'['+', '.join(str(mp[int(x)]) for x in m.group(1).split(','))+']',s)
def walk(o):
    if isinstance(o,dict):
        for k,v in list(o.items()):
            if k=='source' and isinstance(v,list): o[k]=[mp[x] for x in v]
            else: o[k]=walk(v)
        return o
    if isinstance(o,list): return [walk(x) for x in o]
    if isinstance(o,str): return fixstr(o)
    return o
srcs=d.pop('sources')
d=walk(d)
for s in keep: s['n']=mp[s['n']]
d['sources']=keep
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
