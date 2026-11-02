import json,sys
d=json.load(open(sys.argv[1]))
n=int(sys.argv[2]) if len(sys.argv)>2 else 500
for a in d['articles']:
    i=a['identifiers']
    print('##',i.get('pmid'),i.get('pmc',''),i.get('doi',''),'|',a['title'],'|',a['journal'].get('iso_abbreviation'),a.get('publication_date',a.get('pub_date','')))
    print((a.get('abstract') or '')[:n]);print()
