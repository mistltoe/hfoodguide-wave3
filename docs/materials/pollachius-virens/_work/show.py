import json,sys
d=json.load(open(sys.argv[1]))
for a in d['articles']:
  i=a.get('identifiers') or {}
  print(i.get('pmid'), i.get('pmc'), a.get('doi'),'|', a.get('title'),'|', (a.get('journal') or {}).get('title') if isinstance(a.get('journal'),dict) else a.get('journal'), (a.get('publication_date') or {}).get('year'))
