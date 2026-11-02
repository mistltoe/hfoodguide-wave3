import json,sys,glob
want=sys.argv[1].split(',')
A={}
for f in glob.glob('meta*.json'):
  for a in json.load(open(f))['articles']: A[a['identifiers']['pmid']]=a
for p in want:
  a=A.get(p)
  if not a: print(p,'MISSING');continue
  j=a['journal'];j=j.get('title') if isinstance(j,dict) else j
  print('##',p,a['identifiers'].get('pmc',''),a['identifiers'].get('doi'),'|',a['title'],'|',j,'|',a.get('citation',''))
  print(a.get('abstract'));print()
