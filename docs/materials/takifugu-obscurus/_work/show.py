import json,sys
d=json.load(open(sys.argv[1]))
for a in d['articles']:
  i=a['identifiers'];c=a.get('citation',{})
  print(i.get('pmid'),i.get('pmc'),i.get('doi'),a['publication_date'].get('year'),a['journal']['iso_abbreviation'],c)
  print('  T:',a['title']); print('  A:',(a.get('abstract') or '')[:int(sys.argv[2]) if len(sys.argv)>2 else 900]);print()
