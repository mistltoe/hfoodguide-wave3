import json,sys
d=json.load(open(sys.argv[1]))
for a in d['articles']:
    ids=a.get('identifiers') or {}
    j=a.get('journal'); j=j.get('title') if isinstance(j,dict) else j
    print(ids.get('pmid'),'|',a.get('title'),'|',j,(a.get('publication_date') or {}).get('year'),'|',ids.get('pmc'),a.get('doi'))
