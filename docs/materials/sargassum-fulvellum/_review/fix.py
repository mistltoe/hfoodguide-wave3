import json,re
p='/home/user/hfoodguide-wave3/docs/materials/sargassum-fulvellum/dossier.json'
d=json.load(open(p,encoding='utf-8'))
S={s['key']:s for s in d['sections']}
def rep(key,old,new):
    b=S[key]['body']; assert old in b,(key,old); S[key]['body']=b.replace(old,new)
# [32] species not confirmed
rep('cultivation',"\n\n해변에 밀려온 해조로도 나온다[32]. 부산 광안리 해변에 쌓인 폐해조 바이오매스의 72%가 모자반(초록 표기 'Mojaban')이었다[32]. 모자반 양식 방법(종묘·가이식 등)은 공공기관 원문으로 확인하지 못함.",
    "\n\n모자반 양식 방법(종묘·가이식 등)은 공공기관 원문으로 확인하지 못함.")
# [15] first-complete claim not confirmable for this species
rep('related_species',"2022년 연구는 한국에서 식품·의약 원료로 쓰이는 모자반속 6종의 엽록체·미토콘드리아 유전체를 해독했고, 이 가운데 모자반의 엽록체와 미토콘드리아 전체 유전체는 처음 보고된 것이다[15].",
    "2022년 연구는 한국에서 식품·의약 원료로 쓰이는 모자반속 6종(모자반 포함)의 엽록체·미토콘드리아 유전체를 해독했다[15]. 이 연구는 6종 가운데 일부 종의 유전체를 처음 완전 해독했다고 밝혔으나, 모자반이 그에 해당하는지는 확인하지 못함.")
rep('biology',"모자반 표면에서는 새로운 세균도 분리되었다[31]. 한국 남해에서 채집한 모자반에서 분리한 세균은",
    "모자반에서는 새로운 세균도 분리되었다[31]. 한국 남해에서 채집한 모자반에서 분리한 세균은")
rep('safety',"비산염(As(V))이 38 ± 2 µg/g 검출되었다(초록에 건조·생 기준 표기 없음)[18].",
    "비산염(As(V))이 38 ± 2 µg/g 검출되었다(초록에 건조·생 기준 표기 없음, 총비소가 아닌 As(V) 한 화학종의 값)[18]. 같은 논문의 톳 시료 값(46 µg/g)은 다른 종의 값이므로 모자반 값으로 쓰지 않는다[18].")
for c in d['compounds']:
    if c['name']=='Fucoidan':
        c['activity_ko']=c['activity_ko'].replace("LPS 자극 대식세포(RAW 264.7)와 제브라피시에서 NO·염증성 사이토카인을 줄였다(세포·동물 실험)[11]",
            "LPS 자극 대식세포(RAW 264.7)에서 NO·PGE2·염증성 사이토카인을, LPS 자극 제브라피시에서 NO·활성산소·세포 사멸을 줄였다(세포·동물 실험)[11]")
        c['activity_ko']=c['activity_ko'].replace("생쥐에서는 장 상피 장벽에 미치는 영향이 조사되었다(동물 실험)[35]",
            "생쥐에서는 고당 식이로 손상된 회장 상피 장벽과 장 호르몬 분비를 완화했다(동물 실험)[35]")
        assert '회장' in c['activity_ko'] and 'PGE2' in c['activity_ko']
for a in d['assays']:
    if a['compound'].startswith('Arsenate'):
        a['part']="모자반 시료(초록에 건조·생 기준 표기 없음)"
# renumber: drop 32
old=[s['n'] for s in d['sources'] if s['n']!=32]
m={o:i+1 for i,o in enumerate(old)}
d['sources']=[s for s in d['sources'] if s['n']!=32]
for s in d['sources']: s['n']=m[s['n']]
def rn(t): return re.sub(r'\[(\d+)\]',lambda x:'['+str(m[int(x.group(1))])+']',t)
def walk(o):
    if isinstance(o,dict):
        for k,v in o.items():
            if k=='source' and isinstance(v,list): o[k]=[m[i] for i in v]
            elif k=='sources': continue
            elif isinstance(v,str): o[k]=rn(v)
            else: walk(v)
    elif isinstance(o,list):
        for i,v in enumerate(o):
            if isinstance(v,str): o[i]=rn(v)
            else: walk(v)
walk({k:v for k,v in d.items() if k!='sources'})
json.dump(d,open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
