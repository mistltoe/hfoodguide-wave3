import json,sys
d=json.load(open(sys.argv[1]))
for a in d['articles']:
    i=a['identifiers'];j=a.get('journal',{});p=a.get('publication_date',{});c=a.get('citation',{})
    print(i.get('pmid'),i.get('pmc',''),i.get('doi'),'|',j.get('iso_abbreviation'),p.get('year'),c.get('volume',''),c.get('issue',''),c.get('pages',''))
    print('  T:',a['title']); print('  A:',(a.get('abstract') or '')[:1100]); print()
