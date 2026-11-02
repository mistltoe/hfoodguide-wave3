import json,sys
d=json.load(open(sys.argv[1]))
full='-f' in sys.argv
for a in d['articles']:
    ids=a.get('identifiers') or {}
    print('PMID',ids.get('pmid'),'|',ids.get('pmc'),'|',a.get('doi'))
    print(' ',a.get('title'))
    print(' ',a.get('citation'))
    ab=a.get('abstract') or ''
    if not isinstance(ab,str): ab=json.dumps(ab,ensure_ascii=False)
    print('  AB:',ab if full else ab[:500]); print()
