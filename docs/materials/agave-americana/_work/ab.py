import json,sys,glob
ids=sys.argv[1:]
seen=set()
for f in sorted(glob.glob('meta*.json')):
  for a in json.load(open(f))['articles']:
    p=a['identifiers']['pmid']
    if p in ids and p not in seen:
      seen.add(p)
      print('==',p,a['identifiers'].get('pmc'),a.get('doi'),a['journal']['iso_abbreviation'],a['publication_date'].get('year'),a.get('citation'))
      print(a['title']); print(a.get('abstract'))
