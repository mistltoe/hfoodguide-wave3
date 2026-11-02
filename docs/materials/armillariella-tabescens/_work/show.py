import json,sys
d=json.load(open(sys.argv[1]))
for a in d['articles']:
  print('##',a['identifiers'],a.get('title'),'|',a['journal'] if not isinstance(a['journal'],dict) else a['journal'].get('title'),a['publication_date'].get('year'), a.get('article_types'))
  print((a.get('abstract') or '')[:int(sys.argv[2]) if len(sys.argv)>2 else 700])
