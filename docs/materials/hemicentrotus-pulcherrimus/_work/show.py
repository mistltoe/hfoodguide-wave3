import json,sys
d=json.load(open(sys.argv[1]))
n=int(sys.argv[2]) if len(sys.argv)>2 else 1200
for a in d['articles']:
  i=a['identifiers']; j=a['journal']
  print('==',i.get('pmid'),i.get('pmc'),'|',a['title'],'|',j.get('iso_abbreviation') or j.get('title'),j.get('volume'),j.get('issue'),a.get('publication_date',{}).get('year'),'|',', '.join((x.get('last_name','') if isinstance(x,dict) else str(x)) for x in a['authors'][:1]))
  print(str(a.get('abstract'))[:n])
