import json,sys
d=json.load(open(sys.argv[1]))
for a in d['articles']:
  i=a['identifiers']; j=a['journal']
  print(i.get('pmid'), i.get('pmc'), a['publication_date'].get('year'), (j.get('title') if isinstance(j,dict) else j), a.get('doi'),'|', a.get('title'))
  print('   ', (a.get('abstract') or '')[:int(sys.argv[2]) if len(sys.argv)>2 else 300].replace('\n',' '))
