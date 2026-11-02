import json,sys
for f in sys.argv[1:]:
    d=json.load(open(f))
    if isinstance(d,list): d=json.loads(d[0]['text'])
    for a in d['articles']:
        i=a['identifiers']; pd=a.get('publication_date') or a.get('pub_date') or {}
        print(i.get('pmid'),i.get('pmc'),i.get('doi'),'|',a['title'][:150],'|',a['journal']['iso_abbreviation'],json.dumps(pd)[:40])
        print('   ',(a.get('abstract') or '')[:400])
