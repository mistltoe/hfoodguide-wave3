import json,sys
d=json.load(open(sys.argv[1]))
print(json.dumps(d['articles'][0],ensure_ascii=False)[:600]) if len(sys.argv)>2 else None
for a in d['articles']:
    ids=a.get('identifiers') or {}
    print('##',ids.get('pmid'),'|',a.get('title'),'|',a.get('journal',{}) if not isinstance(a.get('journal'),dict) else a['journal'].get('title'),a.get('publication_date') or a.get('pub_date'),'|',ids.get('doi'),ids.get('pmc'))
    ab=a.get('abstract')
    if isinstance(ab,dict): ab=' '.join(str(v) for v in ab.values())
    print((ab or '')[:1400])
