import json,sys,glob
want=sys.argv[1].split(',')
for f in sorted(glob.glob(sys.argv[2]+'/m*.json')):
  for a in json.load(open(f))['articles']:
    i=a['identifiers']
    if i.get('pmid') in want:
      j=a.get('journal'); j=j.get('title') if isinstance(j,dict) else j
      print('##',i.get('pmid'),i.get('pmc'),i.get('doi'),a['publication_date'],j,a.get('citation'),'\n',a['title'],'\n',a.get('abstract'),'\n')
