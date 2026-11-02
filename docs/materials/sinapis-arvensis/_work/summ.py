import json,sys
for f in sys.argv[1:]:
    d=json.load(open(f))
    if isinstance(d,list): d=json.loads(d[0]['text'])
    for a in d['articles']:
        i=a['identifiers']; j=a.get('journal',{})
        print('##',i.get('pmid'),i.get('pmc'),i.get('doi'),'|',a.get('pub_date',a.get('publication_date','')),'|',j.get('iso_abbreviation'),'|',a['title'])
        print('   ',(a.get('abstract') or '')[:int(sys.argv[0] and 700)])
