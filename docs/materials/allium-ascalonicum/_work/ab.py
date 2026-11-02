import json,sys,glob
want=sys.argv[1:]
for f in sorted(glob.glob('m*.json')):
  for a in json.load(open(f))['articles']:
    i=a['identifiers']
    if i.get('pmid') in want:
      au=a.get('authors') or []
      print('==',i.get('pmid'),i.get('pmc'),a.get('doi'),a['publication_date'],a['journal'].get('iso_abbreviation'),a.get('citation'))
      print(' ',(au[0].get('last_name','')+' '+au[0].get('initials','')) if au else '', a['title'])
      print(a.get('abstract'))
