import json,sys
for f in sys.argv[1:]:
  for a in json.load(open(f))['articles']:
    i=a['identifiers']; print(i.get('pmid'),i.get('pmc') or '-',a['publication_date'].get('year'),'|',str((a.get('journal') or {}).get('title') if isinstance(a.get('journal'),dict) else a.get('journal'))[:40],'|',a['title'][:150])
