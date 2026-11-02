import json,sys
d=json.load(open(sys.argv[1]))
for a in d['articles']:
    i=a['identifiers']; j=a.get('journal',{})
    print(i.get('pmid'),i.get('pmc'),i.get('doi'),'|',a['title'],'|',j.get('iso_abbreviation'),a.get('pub_date'), a.get('volume'),a.get('issue'),a.get('pages'))
    print('  ',(a.get('abstract') or '')[:1300])
