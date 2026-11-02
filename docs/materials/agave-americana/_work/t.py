import json,sys
for f in sys.argv[1:]:
  d=json.load(open(f))
  for a in d['articles']:
    i=a['identifiers']; print(i.get('pmid'),i.get('pmc') or '-',a['publication_date'].get('year'),a['journal']['iso_abbreviation'],'|',a['title'][:150])
