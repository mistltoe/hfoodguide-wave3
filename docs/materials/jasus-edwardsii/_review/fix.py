import json,re,sys
p='/home/user/hfoodguide-wave3/docs/materials/jasus-edwardsii/dossier.json'
d=json.load(open(p))
S={s['key']:s for s in d['sections']}
changes=[]
def rep(key,old,new,why):
    b=S[key]['body']; assert old in b,(key,old[:30]); S[key]['body']=b.replace(old,new); changes.append({"where":f"sections.{key}","before":old,"after":new,"why":why})
safety_old=S['safety']['body']
S['safety']['body']="""식약처 「식품원료 목록」에서 붉은남방닭새우는 사용 조건 없는 '사용가능' 수산물 원료이며, 건강기능식품 고시형 원료가 아니어서 고시 섭취 시 주의사항은 없다[1]. 이 종에 대한 국내 공공기관의 알레르기·잔류물질·중금속 안내는 확인하지 못함.

가장 잘 연구된 위해 요인은 마비성 패류독소다. 2012–2020년 태즈메이니아 간췌장 시료 496개 중 86개(17%)가 이매패류 기준 0.8 mg STX 당량/kg을 넘었고 최고값은 10.9 mg STX 당량/kg이었다[12]. 독소는 간췌장에만 문제 수준으로 쌓이고 꼬리 살에서는 검출되지 않았으며, 삶거나 쪄도 간췌장의 독소 농도는 줄지 않았다[13, 14]. 독소 먹이를 끊으면 하루 약 7%씩 빠졌고, 조류 세포에 직접 노출만으로는 쌓이지 않았다[15, 16]. 태즈메이니아에서 이 독소 관련 질병 보고는 없었다[12].

이 종의 간(간췌장)에서는 비소 240 mg/kg, 카드뮴 8 mg/kg이 보고되었다(생·건 기준·비소 형태 표기 없음)[17]. 빅토리아 연안 가식부의 비소·카드뮴·수은·납 평균은 FSANZ 기준 이하였고[18], 말린 머리의 무기비소는 0.2 mg/kg, 카드뮴은 0.1 mg/kg이었다[19].

이 종의 알레르겐(트로포미오신 등)을 직접 다룬 논문은 PubMed에서 확인하지 못함(검색어 Jasus·rock lobster AND allergen·tropomyosin). 다른 닭새우·바닷가재의 알레르겐 자료는 이 종 값으로 옮기지 않았다."""
changes.append({"where":"sections.safety","before":"(806자) … 다른 속 닭새우(Panulirus stimpsoni)·아메리카바다가재의 트로포미오신이 갑각류 알레르기 환자 IgE와 반응했다는 보고는 이 종 자료가 아니다[34].","after":"(%d자) 같은 내용을 줄이고 Panulirus stimpsoni·Homarus americanus 알레르겐 문장과 출처 [34]를 뺌"%len(S['safety']['body']),"why":"지시: 안전성 800자 이하, 다른 닭새우·랍스터(Panulirus·Homarus) 자료 섞지 않기. PubMed 재검색(Jasus/rock lobster AND allergen/tropomyosin)에서 이 종 알레르겐 논문 없음(남아공 rock lobster=J. lalandii 직업성 알레르기 조사만)"})
rep('processing',"가공 부산물인 머리는 전체 무게의 절반 이상을 차지하며, 오스트레일리아에서 해마다 약 3,000톤이 나온다[19].",
 "가공 부산물인 머리는 전체 무게의 절반 이상을 차지하며, 오스트레일리아의 닭새우류 머리는 해마다 약 3,000톤이 나오는 것으로 추산되었다(종을 구분하지 않은 값)[19].",
 "[19] 전문: 'Australia produces about 3,000 tons of rock lobster heads' — 세계 최대 rock lobster 생산국 오스트레일리아 전체 값으로, 서부 닭새우(Panulirus cygnus) 등이 섞였을 수 있어 이 종 값으로 단정하지 않음")
rep('processing',"이 종과 민물가재를 함께 시험한 연구에서 탁상형 전기 기절 장치는 받아들일 만한 방법으로 평가되었으나 아주 큰 개체(1.76 kg) 하나는 기절시키지 못했다[29]. 초록에서 종 이름이 빠져 있어 종별 결과는 확인하지 못함.",
 "피오르드랜드산 붉은 닭새우 10마리와 민물가재 10마리를 시험한 연구에서 탁상형 전기 기절 장치는 민물가재를 모두 즉사시켰고, 닭새우는 9마리를 기절시켜 그중 3마리가 즉사했으나 가장 큰 개체(1.76 kg)에는 전류가 걸리지 않았다[29]. 연구진은 아주 큰 개체를 빼면 받아들일 만한 방법으로 평가했다[29].",
 "[29] PMC 전문 확인: 종별 결과(닭새우 10마리 중 1마리 1,760 g 실패, 9마리 중 3마리 즉사; 민물가재 10마리 모두 즉사)가 원문에 있어 '확인하지 못함'을 채움")
rep('cultivation',"세계 어획량(톤)과 뉴질랜드 어획 할당량은 확인하지 못함.",
 "뉴질랜드에서는 붉은 닭새우가 가장 가치 큰 연안 상업 어업으로 해마다 2,500–3,000톤이 잡히고 2022년 가치는 3억 4,000만 뉴질랜드달러라고, 한 논문 서론이 업계 단체 자료를 인용해 적었다[29]. 세계 어획량(톤)과 뉴질랜드 어획 할당량은 확인하지 못함.",
 "[29] PMC 전문 서론의 뉴질랜드 생산량·가치(2차 인용)로 '확인하지 못함' 일부 보강")
# sources: drop 34, renumber 35-37
mp={}
new=[]
for s in d['sources']:
    if s['n']==34: continue
    mp[s['n']]=len(new)+1; s['n']=len(new)+1; new.append(s)
d['sources']=new
def renum(t):
    return re.sub(r'\[([0-9 ,–-]+)\]',lambda m:'['+', '.join(str(mp[int(x)]) for x in re.split(r'\s*,\s*',m.group(1)))+']' if all(x.strip().isdigit() for x in m.group(1).split(',')) else m.group(0),t)
for s in d['sections']: s['body']=renum(s['body'])
def walk(o):
    if isinstance(o,dict):
        for k,v in o.items():
            if k=='source' and isinstance(v,list): o[k]=[mp[x] for x in v]
            elif isinstance(v,str): o[k]=renum(v)
            else: walk(v)
    elif isinstance(o,list):
        for x in o: walk(x)
for k in ['compounds','assays','world','markers','nutrients','production','gi','orgs']:
    walk(d.get(k,[]))
json.dump(d,open(p,'w'),ensure_ascii=False,indent=2)
json.dump(changes,open('/home/user/hfoodguide-wave3/docs/materials/jasus-edwardsii/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(S['safety']['body']), mp)
