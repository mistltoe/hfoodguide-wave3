import json,sys
for f in sys.argv[1:]:
  d=json.load(open(f))
  for a in d['articles']:
    i=a['identifiers']; print(i.get('pmid'), i.get('pmc'), i.get('doi'), a['publication_date'].get('year'), '|', a['title'], '|', a['journal'] if not isinstance(a['journal'],dict) else a['journal'].get('title'))
    print('   ', (a.get('abstract') or '')[:600].replace('\n',' '))
