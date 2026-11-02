import json,sys,html,re
d=json.load(open(sys.argv[1]))
for a in d['articles']:
  ab=re.sub('<[^>]+>','',html.unescape(a.get('abstract') or ''))
  print('##',a['identifiers'],a.get('title'),'|',a.get('journal'),a.get('publication_date'))
  print(ab[:int(sys.argv[2]) if len(sys.argv)>2 else 900])
