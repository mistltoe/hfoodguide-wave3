import json,sys
d=json.load(open(sys.argv[1]))
for a in d['articles']:
  j=a.get('journal'); j=j.get('title') if isinstance(j,dict) else j
  print(a['identifiers'].get('pmid'),'|',a.get('title'),'|',j,a.get('publication_date',{}).get('year'),'|',a['identifiers'].get('pmc'),a['identifiers'].get('doi'))
  print('   ',(a.get('abstract') or '')[:int(sys.argv[2]) if len(sys.argv)>2 else 700])
