import json,sys
d=json.load(open(sys.argv[1]))
print(list(d['articles'][0].keys()))
for a in d['articles']:
    ids=a.get('identifiers') or {}
    print(a.get('pmid'),'|',a.get('title'),'|',a.get('journal') if isinstance(a.get('journal'),str) else (a.get('journal') or {}).get('title'),a.get('publication_date') or a.get('pub_date'),'|',ids if not isinstance(ids,dict) else {k:ids.get(k) for k in ('pmc','doi')})
