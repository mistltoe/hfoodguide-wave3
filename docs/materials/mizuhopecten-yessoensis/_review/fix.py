import json,re
p='dossier.json'; d=json.load(open(p))
S={s['key']:s for s in d['sections']}
changes=[]
def rep(key,old,new,why):
    s=S[key]; assert old in s['body'],(key,old[:30]); s['body']=s['body'].replace(old,new); changes.append({"where":"sections."+key,"before":old,"after":new,"why":why})
rep('history'," 국내에서는 강원 연안에서 수하식으로 기르는 2–3년생 참가리비를 대상으로 생식주기를 조사한 1997년 국내 학술 논문이 있다(WebSearch 결과로만 확인)[36].","",
    "[36]은 WebSearch 요약으로만 본 국내 논문으로 원문을 열 수 없어(사이트가 허용 목록 밖) 확인 불가 — 문장과 출처 삭제")
rep('cultivation',"국내에서는 강원 연안에서 수하식으로 기른 개체를 조사한 연구가 있으나, 국내 생산량 통계는 확인하지 못함[36].","국내 양식 현황과 생산량 통계는 확인하지 못함.",
    "[36] 원문 미확인 — 국내 연구 언급 삭제, 확인하지 못함으로 표기")
rep('safety',"국내 기준은 마비성 0.8 mg/kg, 설사성 0.16 mg/kg으로 알려져 있다(WebSearch 결과로만 확인)[35].","코덱스가 제안한 오카다산·디노피시스톡신류 규제값은 0.16 mg/kg이다[4]. 국내 패류독소 기준 원문은 이 작업에서 확인하지 못함.",
    "[35]는 WebSearch 요약만 본 출처로 원문 미확인 — 삭제. 0.16 mg/kg은 [4] 전문 서론의 코덱스 값으로 대체")
rep('safety',"간췌장을 포함한 가식부 전체의 마비성 독소가 4–9월에 코덱스 기준(800 µg STX 당량/kg)을 넘었으나","간췌장 독소량을 가식부 전체 무게로 나눈 추정치에서 마비성 독소가 4월 초–9월 초에 코덱스 기준(800 µg STX 당량/kg)을 넘었으나",
    "[5] 전문: 4월 4일–9월 4일, 간췌장 값으로 계산한 추정치")
rep('safety',"중국 연안 세 가리비 종 조사에서 시료의 96%가 카드뮴 기준을 넘어, 관자만 먹을 것을 권고했다[19].","중국 연안 세 가리비 종(이 종 포함)을 합친 조사에서 시료의 96%가 카드뮴 기준을 넘어, 관자만 먹을 것을 권고했다(세 종 합친 비율)[19].",
    "[19] 96%는 세 종 합친 시료 비율임을 밝힘")
rep('safety',"캐나다 태평양 연안 조사에서 이 종을 포함한 가리비 4종은 습중량 4.97–8.98 µg/g의 카드뮴을 보였다[20].","캐나다 태평양 연안 조사에서 이 종을 포함한 가리비 4종의 카드뮴은 습중량 기준 4.97–8.98 µg/g이었다(4종을 합친 범위로, 최고값은 다른 종 Crassadoma gigantea; 이 종만의 값은 초록에 없음)[20].",
    "[20] 범위는 4종 합친 값, 최고는 C. gigantea — 이 종 값처럼 읽히지 않게 고침(기준은 습중량 맞음)")
rep('processing',"관자와 생식소·외투막의 지질은 인지질 비율(총지질의 54.99–78.26%)과 고도불포화지방산 비율(총지방산의 20.44–58.81%)이 높고 EPA·DHA를 지닌 인지질이 많다(두 가리비 종을 합친 범위)[23].",
    "이 종과 비단가리비(Chlamys farreri)의 관자·생식소·외투막을 함께 분석한 연구에서 지질은 인지질(총지질의 54.99–78.26%)과 고도불포화지방산(총지방산의 20.44–58.81%)이 많고 주요 인지질 분자종 대부분이 EPA·DHA를 지녔다; 이 범위는 두 종·세 부위를 합친 것이며 이 종만의 값은 초록에 없다[23].",
    "[23] 범위는 두 종(C. farreri 포함)·세 부위를 합친 값 — 이 종 값으로 읽히지 않게 명시")
rep('processing',"생쥐 단회·28일·13주 반복 투여 시험에서 독성 변화가 관찰되지 않았다[31].","생쥐 단회(5,000 mg/kg)·28일·13주 반복 투여 시험에서 독성학적으로 의미 있는 변화가 관찰되지 않았다[31].",
    "[31] 초록 표현(no toxicologically significant changes)과 단회 용량 반영")
rep('biology',"소화샘의 카드뮴 함량이 나이와 껍데기 무게에 비례해 늘었다[21].","소화샘의 카드뮴 농도와 총량이 나이가 들수록 늘었고, 소화샘 전체의 카드뮴 양은 껍데기 무게와 강한 양의 상관을 보였다[21].",
    "[21] 초록: 나이에 따라 증가, 껍데기 무게와는 상관 — '비례' 과장 수정")
rep('cultivation',"해역별 카드뮴 농도 차이도 소화샘 축적에 영향을 준다[19, 21].","중국 연안 조사에서는 보하이해 가리비가 황해 가리비보다 중금속 오염이 심했다[19].",
    "[21]은 중간 정도 오염이 카드뮴-껍데기 관계에 영향이 없다고 씀 — [21] 인용 빼고 [19] 내용으로 고침")
# compounds/EPA lipid note
for c in d['compounds']:
    if c['name']=='Eicosapentaenoic acid':
        old=c['content_text']; c['content_text']="이 종과 비단가리비(Chlamys farreri) 두 종·세 부위를 합친 지질의 PUFA 20.44–58.81%(총지방산 대비, 이 종만의 값은 초록에 없음); 주요 글리세로인지질 분자종 대부분이 EPA·DHA를 함유 [23]"
        changes.append({"where":"compounds.Eicosapentaenoic acid.content_text","before":old,"after":c['content_text'],"why":"두 종 합친 범위임을 명시"})
        c['activity_ko']="이 종을 포함한 가리비 지질의 주요 고도불포화지방산이다[23]"
    if c['name']=='Phosphatidylcholine':
        old=c['content_text']; c['content_text']="인지질 중 41.39–51.86 mol% (이 종과 비단가리비 두 종·세 부위를 합친 범위) [23]"
        changes.append({"where":"compounds.Phosphatidylcholine.content_text","before":old,"after":c['content_text'],"why":"두 종 합친 범위임을 명시"})
# renumber sources: drop 35, 36
drop={35,36}
keep=[s for s in d['sources'] if s['n'] not in drop]
m={s['n']:i+1 for i,s in enumerate(keep)}
for s in keep: s['n']=m[s['n']]
d['sources']=keep
def fixcite(t):
    def f(mo):
        nums=[int(x) for x in re.split(r',\s*',mo.group(1))]
        nums=[m[x] for x in nums if x in m]
        return '['+', '.join(map(str,nums))+']' if nums else ''
    return re.sub(r'\[(\d+(?:,\s*\d+)*)\]',f,t)
for s in d['sections']: s['body']=fixcite(s['body'])
for arr in ('compounds','assays'):
    for c in d[arr]:
        for k,v in list(c.items()):
            if isinstance(v,str): c[k]=fixcite(v)
        c['source']=[m[x] for x in c['source'] if x in m]
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
