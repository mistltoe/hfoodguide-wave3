import json,sys,glob
arts={}
for f in glob.glob('_work/meta*.json'):
    for a in json.load(open(f)).get('articles',[]):
        arts[a['identifiers']['pmid']]=a
for p in sys.argv[1:]:
    a=arts.get(p)
    if not a: print(p,'MISSING');continue
    print('##',p,a['identifiers'].get('doi'),a.get('title'))
    print(a.get('journal') if isinstance(a.get('journal'),str) else json.dumps({k:a.get(k) for k in ('journal','publication_date','volume','issue','pages','pubdate') if k in a},ensure_ascii=False))
    print(a.get('abstract'));print()
