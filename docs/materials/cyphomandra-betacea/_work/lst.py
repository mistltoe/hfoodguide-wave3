import json,sys
for f in sys.argv[1:]:
  for a in json.load(open(f))['articles']:
    i=a['identifiers'];j=a['journal'];j=j.get('title') if isinstance(j,dict) else j
    print(i.get('pmid'),a['publication_date'].get('year'),i.get('pmc',''),'|',a['title'],'|',j)
