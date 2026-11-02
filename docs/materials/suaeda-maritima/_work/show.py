import json,sys
d=json.load(open(sys.argv[1]))
ids=set(sys.argv[2:])
for a in d['articles']:
  i=a['identifiers']
  if ids and i['pmid'] not in ids: continue
  print('##',i['pmid'],i.get('pmc'),a.get('doi'),a['citation'] if 'citation' in a else '')
  print(a['title']);print(a['abstract']);print()
