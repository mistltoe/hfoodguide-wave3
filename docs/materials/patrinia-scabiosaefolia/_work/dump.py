import json,sys;d=json.load(open(sys.argv[1]))
n=int(sys.argv[2]) if len(sys.argv)>2 else 600
for a in d['articles']:
  i=a['identifiers']
  print('==',i.get('pmid'),i.get('pmc'),i.get('doi'),a['journal'] if isinstance(a['journal'],str) else a['journal'].get('iso_abbreviation',a['journal']),a['publication_date'].get('year'))
  print(a['title']); print((a.get('abstract') or '')[:n])
