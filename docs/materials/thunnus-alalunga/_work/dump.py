import json,sys
want=set(sys.argv[1:])
for f in ['meta1.json','meta2.json','meta3.json','meta4.json']:
  for a in json.load(open(f))['articles']:
    i=a['identifiers']
    if i['pmid'] in want:
      print('=== ',i,a.get('citation') or '', '\n', a['title'],'\n',a.get('abstract'),'\n')
