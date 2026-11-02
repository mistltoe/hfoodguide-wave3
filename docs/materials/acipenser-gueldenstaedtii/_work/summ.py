import json,sys
d=json.load(open(sys.argv[1]))
if isinstance(d,list): d=d[0]
if 'text' in d and 'articles' not in d: d=json.loads(d['text'])
n=int(sys.argv[2]) if len(sys.argv)>2 else 500
for a in d['articles']:
    i=a.get('identifiers',{})
    print('##',i.get('pmid'),i.get('pmc'),i.get('doi'),a.get('publication_date') or a.get('pub_date'),a['journal'].get('iso_abbreviation'))
    print('T:',a['title']); print('A:',(a.get('abstract') or '')[:n]); print('PT:',a.get('publication_types'))
