import json,sys
d=json.load(open(sys.argv[1]))
n=int(sys.argv[2]) if len(sys.argv)>2 else 400
for a in d['articles']:
    j=a.get('journal',{}); i=a.get('identifiers',{})
    print(i.get('pmid'),i.get('pmc'),i.get('doi'),'|',a['title'],'|',j.get('iso_abbreviation') or j.get('title'),(a.get('publication_date') or {}).get('year'),j.get('volume'),j.get('issue'),a.get('pages'))
    print('   ',(a.get('abstract') or '')[:n].replace('\n',' '))
