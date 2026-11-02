import json,sys
d=json.load(open(sys.argv[1]))
full=len(sys.argv)>2
for a in d['articles']:
    ids=a.get('identifiers',{}) 
    print('##',a.get('pmid'),a.get('title'),'|',a.get('journal',{}).get('title') if isinstance(a.get('journal'),dict) else a.get('journal'),a.get('publication_date') or a.get('pub_date'),'|',json.dumps(ids))
    ab=a.get('abstract') or ''
    if isinstance(ab,dict): ab=json.dumps(ab,ensure_ascii=False)
    print(ab if full else ab[:400]); print()
