import json,sys
for f in sys.argv[1:]:
  d=json.load(open(f))
  for a in d['articles']:
    i=a['identifiers'];j=a.get('journal',{});c=a.get('citation',{});p=a.get('publication_date',{})
    print('PMID',i.get('pmid'),i.get('pmc'),i.get('doi'),'|',p.get('year'),j.get('iso_abbreviation'),c, a.get('article_types'))
    print('T:',a['title'])
    print('A:',(a.get('abstract') or '')[:2000]);print()
