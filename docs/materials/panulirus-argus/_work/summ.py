import json,sys
d=json.load(open(sys.argv[1]))
for a in d['articles']:
    i=a['identifiers']; j=a.get('journal',{})
    pd=a.get('publication_date') or a.get('pub_date') or ''
    print('##',i.get('pmid'),i.get('pmc',''),i.get('doi',''),'|',j.get('iso_abbreviation'),json.dumps(pd)[:40])
    print(a['title']); print((a.get('abstract') or '')[:int(sys.argv[2]) if len(sys.argv)>2 else 900]); print()
