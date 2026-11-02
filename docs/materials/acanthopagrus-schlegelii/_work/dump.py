import json,sys
d=json.load(open(sys.argv[1]))
out=json.load(open('meta.json')) if __import__('os').path.exists('meta.json') else {}
for a in d['articles']:
    i=a['identifiers']; out[i.get('pmid')]={'pmid':i.get('pmid'),'pmc':i.get('pmc'),'doi':a.get('doi'),'title':a['title'],'journal':a.get('journal'),'date':a.get('publication_date'),'citation':a.get('citation'),'abstract':a.get('abstract')}
json.dump(out,open('meta.json','w'),ensure_ascii=False,indent=1)
for a in d['articles']:
    i=a['identifiers']; print(i.get('pmid'),i.get('pmc'),'|',a['title'][:150])
