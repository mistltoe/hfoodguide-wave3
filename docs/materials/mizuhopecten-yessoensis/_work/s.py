import json,sys
for f in sys.argv[1:]:
  d=json.load(open(f))
  for a in d['articles']:
    i=a['identifiers']; c=a.get('citation',{})
    print(f"## {i['pmid']} | {a['title']} | {a['journal']['iso_abbreviation']} {a['publication_date'].get('year')};{c.get('volume')}:{c.get('pages')} | doi {a.get('doi')} | pmc {i.get('pmc')}")
    print(a.get('abstract','')); print()
