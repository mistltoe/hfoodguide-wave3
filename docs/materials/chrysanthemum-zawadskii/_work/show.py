import json,sys
d=json.load(open(sys.argv[1]))
n=int(sys.argv[2]) if len(sys.argv)>2 else 500
for a in d['articles']:
  i=a['identifiers'];j=a.get('journal');j=j.get('title') if isinstance(j,dict) else j
  print(i.get('pmid'),i.get('pmc'),i.get('doi'),'|',a['title'],'|',j,(a.get('publication_date') or {}).get('year'),'|',(a.get('citation') or '')[:120])
  print('   ',(a.get('abstract') or '')[:n])
