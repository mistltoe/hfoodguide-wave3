import json,sys
for f in sys.argv[1:]:
  d=json.load(open(f))
  for a in d['articles']:
    i=a['identifiers']; c=a.get('citation',{})
    print('##',i.get('pmid'),i.get('pmc'),i.get('doi'),a['journal']['iso_abbreviation'],a['publication_date'].get('year'),c.get('volume'),c.get('issue'),c.get('pages'))
    print(a['title']); print(a.get('abstract','')); print()
