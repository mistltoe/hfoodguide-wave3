import json,sys
d=json.load(open(sys.argv[1]))
if isinstance(d,list): d=d[0]
if 'text' in d and 'articles' not in d: d=json.loads(d['text'])
for a in d['articles']:
    print('###',a['identifiers'].get('pmid'),a['identifiers'].get('doi'),a.get('pub_date') or a.get('journal',{}).get('pub_date'))
    print(a['title']); print(a.get('abstract','')); print()
