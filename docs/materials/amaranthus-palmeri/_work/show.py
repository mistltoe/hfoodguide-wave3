import json,sys
for f in sys.argv[1:]:
  d=json.load(open(f))
  for a in d['articles']:
    i=a['identifiers']; print(i.get('pmid'),i.get('pmc'),a.get('doi'),'|',a['title'][:140],'|',a['journal'].get('title') if isinstance(a['journal'],dict) else a['journal'],a['publication_date'].get('year'))
