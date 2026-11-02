import json,sys
d=json.load(open(sys.argv[1]))
for a in d['articles']:
    i=a['identifiers'];aff=(a.get('authors') or [{}])[0].get('affiliations',[''])
    print('##',i.get('pmid'),i.get('pmc',''),i.get('doi'),a['publication_date'].get('year'),a['journal']['iso_abbreviation'],'|',(aff[0] if aff else '')[-40:])
    print(a['title']); print(a.get('abstract','')[:int(sys.argv[2]) if len(sys.argv)>2 else 900]); print()
