import json,sys,glob
want=sys.argv[1:]
for f in glob.glob('meta*.json'):
  for a in json.load(open(f))['articles']:
    i=a['identifiers']
    if i.get('pmid') in want:
      print('==',i.get('pmid'),i.get('pmc'),i.get('doi'),a['title'],a.get('citation')); print(a['abstract']); print()
