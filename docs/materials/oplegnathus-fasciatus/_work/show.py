import json,sys
d=json.load(open(sys.argv[1]))
for a in d['articles']:
  i=a['identifiers'];pd=a['publication_date']
  print('##',i.get('pmid'),i.get('pmc',''),i.get('doi'),'|',a['title'],'|',a['journal']['iso_abbreviation'],pd.get('year'))
  ab=a.get('abstract') or ''
  if isinstance(ab,dict): ab=json.dumps(ab,ensure_ascii=False)
  print(ab[:int(sys.argv[2]) if len(sys.argv)>2 else 1500]);print()
