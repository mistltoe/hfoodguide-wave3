import json,sys
d=json.load(open(sys.argv[1]))
if isinstance(d,list): d=d[0]
for a in d['articles']:
    i=a['identifiers']; j=a.get('journal',{})
    print(i.get('pmid'),i.get('pmc',''),i.get('doi',''),'|',a.get('pub_date',a.get('publication_date','')),j.get('iso_abbreviation'),'|',a['title'])
    if len(sys.argv)>2: print('   ',(a.get('abstract') or '')[:int(sys.argv[2])])
