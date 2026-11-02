import json,sys
d=json.load(open(sys.argv[1]))
n=int(sys.argv[2]) if len(sys.argv)>2 else 300
for a in d['articles']:
  i=a['identifiers'];print('==',i.get('pmid'),i.get('pmc'),a['journal'].get('title') if isinstance(a['journal'],dict) else a['journal'],a['publication_date'].get('year'),'|',a['title'])
  print('  ',(a.get('abstract') or '')[:n])
