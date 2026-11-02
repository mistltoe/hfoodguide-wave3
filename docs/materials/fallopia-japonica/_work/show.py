import json,sys
d=json.load(open(sys.argv[1]))
for a in d['articles']:
    ids=a.get('identifiers') or {}
    print('##',ids,a.get('citation'),'|',a.get('title'))
    j=a.get('journal') or {}
    print('  ',a.get('journal') if isinstance(j,str) else (j.get('title') or j.get('iso_abbreviation')), a.get('publication_date') or a.get('pub_date'), j.get('volume') if isinstance(j,dict) else '', j.get('issue') if isinstance(j,dict) else '', a.get('pages'))
    ab=a.get('abstract') or ''
    if isinstance(ab,dict): ab=' '.join(str(v) for v in ab.values())
    print('  ',str(ab)[:int(sys.argv[2]) if len(sys.argv)>2 else 1500])
