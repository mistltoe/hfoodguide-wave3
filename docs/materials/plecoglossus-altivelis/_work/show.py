import json,sys
d=json.load(open(sys.argv[1]))
for a in d['articles']:
    j=a.get('journal',{})
    print('PMID',a['identifiers'].get('pmid'),a['identifiers'].get('pmc'),a['identifiers'].get('doi'),'|',j.get('iso_abbreviation'),a.get('pub_date') or a.get('publication_date') or '')
    print(' T:',a['title'])
    print(' A:',(a.get('abstract') or '')[:int(sys.argv[2]) if len(sys.argv)>2 else 1500])
    print()
