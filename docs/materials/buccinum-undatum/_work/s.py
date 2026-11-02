import json,sys
d=json.load(open(sys.argv[1]))
for a in d['articles']:
  i=a['identifiers']
  print(i.get('pmid'),i.get('pmc'),a.get('doi'),'|',a.get('title'),'|',a['journal']['iso_abbreviation'],a.get('publication_date'),a.get('article_types'))
  print('   ',(a.get('abstract') or '')[:int(sys.argv[2]) if len(sys.argv)>2 else 250])
