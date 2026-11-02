import json,sys
d=json.load(open(sys.argv[1]))
for a in d['articles']:
  i=a['identifiers'];print(i.get('pmid'),i.get('pmc'),i.get('doi'),a.get('journal',{}).get('iso_abbreviation'),(a.get('publication_date') or {}).get('year'),'|',a['title']);print('   ',(a.get('abstract') or '')[:int(sys.argv[2]) if len(sys.argv)>2 else 700])
