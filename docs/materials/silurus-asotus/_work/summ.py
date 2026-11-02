import json,sys
d=json.load(open(sys.argv[1]))
if isinstance(d,list): d=d[0]
if 'text' in d and isinstance(d['text'],str): d=json.loads(d['text'])
for a in d['articles']:
    i=a['identifiers'];j=a.get('journal',{})
    print('##',i.get('pmid'),i.get('pmc'),i.get('doi'),'|',a['title'],'|',j.get('iso_abbreviation'),a.get('publication_date') or a.get('pub_date') or '', a.get('publication_types',''))
    print((a.get('abstract') or '')[:1500]);print()
