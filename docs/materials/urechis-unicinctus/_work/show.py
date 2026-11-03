import json,sys
arts=[]
for f in ['meta1.json','meta2.json']+sys.argv[2:]:
    try: arts+=json.load(open(f))['articles']
    except Exception: pass
want=sys.argv[1].split(',')
for a in arts:
    p=a['identifiers'].get('pmid') or ''
    t=a['title']
    if any(w in p or w.lower() in t.lower() for w in want):
        print('###',p,a['identifiers'].get('doi'),a['identifiers'].get('pmc'),a['publication_date'],a.get('citation'));print(t);print(a.get('abstract'));print()
