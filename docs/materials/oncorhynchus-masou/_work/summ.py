import json,sys
d=json.load(open(sys.argv[1]))
for a in d['articles']:
  i=a['identifiers'];c=a.get('citation',{})
  print(i.get('pmid'),i.get('pmc',''),'|',a['title'],'|',a['journal']['iso_abbreviation'],a['publication_date'].get('year'),c.get('volume'),c.get('issue'),c.get('pages'),'|',a.get('doi'))
  print('  ',(a.get('abstract') or '')[:int(sys.argv[2]) if len(sys.argv)>2 else 900]);print()
