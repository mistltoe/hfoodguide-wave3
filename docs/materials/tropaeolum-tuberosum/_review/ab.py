import json,sys
arts={}
for f in ['_work/meta1.json','_work/meta2.json']:
  for a in json.load(open(f))['articles']:
    arts[a['identifiers'].get('pmid')]=a
for p in sys.argv[1:]:
  a=arts.get(p)
  if not a: print(p,'MISSING');continue
  print('=====',p,a.get('title'),a.get('journal'),a.get('pubDate') or a.get('year'),a['identifiers'].get('doi'))
  print(a.get('abstract'));print()
