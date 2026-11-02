import json
rows=json.load(open('data/raw/mfds_rawmtrl/I1020_20261013.json'))['rows']
keys=['호장근','Fallopia','Reynoutria','cuspidatum','싱아','Polygonum','Persicaria','하수오','Rumex acetosa','수영','마디풀']
for r in rows:
    s=json.dumps(r,ensure_ascii=False)
    if any(k in s for k in keys):
        print(r['RPRSNT_RAWMTRL_NM'],'|',r['USE_CND_STDR_CN'][:80],'|',r['RAWMTRL_NCKNM'],'|',r['SCNM'][:80],'|',r['ENG_NM'][:40],'|',r['USE_CND_NM'],'|',r['LCLAS_NM'])
