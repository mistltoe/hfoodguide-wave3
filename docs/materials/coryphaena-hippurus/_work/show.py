import json,sys
for f in sys.argv[1:]:
    d=json.load(open(f))
    for a in d['articles']:
        i=a['identifiers']; c=a.get('citation',{})
        print(f"=== {i.get('pmid')} {i.get('pmc','')} doi:{i.get('doi','')} | {a['journal'].get('iso_abbreviation')} {a['publication_date'].get('year')};{c.get('volume')}({c.get('issue')}):{c.get('pages')}")
        print(a['title']); print((a.get('abstract') or '(no abstract)')); print()
