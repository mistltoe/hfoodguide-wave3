import json,re,sys
p=sys.argv[1]
d=json.load(open(p,encoding='utf-8'))
S={s['key']:s for s in d['sections']}
changes=[]
def rep(key,old,new,why):
    b=S[key]['body']; assert old in b,(key,old); S[key]['body']=b.replace(old,new)
    changes.append({"where":f"sections.{key}","before":old,"after":new,"why":why})
rep('overview',"파나마 재배 열매의 과육 당도는 평균 14.9 °Brix로","파나마에서 2008년에 잰 열매(야생·재배 포함) 과육 당도는 평균 14.9 °Brix로",
    "[5] 전문: 14.9 °Brix는 2008년 전체 표본 평균이며 재배형만의 값이 아님(야생 13.6, 재배 16.6)")
rep('overview',"이 종을 원재료로 하는 건강기능식품 고시형 원료는 목록에서 확인되지 않는다[1].","이 종을 원재료로 하는 건강기능식품 고시형 원료는 확인하지 못함.",
    "[1]은 식품원료 목록(I1020)이라 건강기능식품 고시형 원료 여부를 뒷받침하지 않음")
rep('cultivation',"나무가 열매를 맺기까지 약 15년이 걸릴 수 있다고 적혀 있다[5]","나무는 약 15년 안에 열매를 맺기 시작한다고 적혀 있다[5]",
    "[5] 전문: 'may come into bearing within about 15 years'(15년 '안에')")
rep('related_species',"Chrysophyllum albidum(최근 Gambeya 속으로 다루기도 함)으로","Chrysophyllum albidum으로",
    "[23] 초록에 Gambeya 속 이동 언급 없음 — 출처 없는 분류 주장 삭제")
rep('related_species',"같은 사포타과의 다른 속 과일이다[24].","같은 사포타과의 다른 속 과일이다[24]. 식약처 목록에도 아비우는 'Abiu열매(Pouteria caimito; Yellow star apple, Caimito)'라는 별도 원료로 올라 있어, 영어 이름 'Caimito'만으로는 두 원료를 구분할 수 없다[1].",
    "I1020 원자료에서 Abiu열매 행의 영문명에 Yellow star apple·Caimito가 있어 이명 혼동 위험을 보탬")
rep('safety'," 미국 농무부 성분 데이터베이스에서 옮긴 후보 자료에도 씨의 같은 계열 배당체가 최대 12,000 ppm으로 기록되어 있다[2].","",
    "[2] USDA Duke DB 원 페이지를 이 환경에서 열 수 없어(호스트 접근 불가) 대조 불가 — 삭제(값 12,000 ppm=1.2%는 [3]의 루쿠민 1.2%와 같으므로 [3]으로 충분)")
# compounds
C=d['compounds']
for c in C:
    if c['name']=='Lucumin':
        old=c['content_text']; c['content_text']="씨 1.2%[3]"; c['source']=[1,3]
        changes.append({"where":"compounds.Lucumin.content_text","before":old,"after":c['content_text'],"why":"[2] 원문 미확인 — 데이터베이스 값 삭제"})
    if c['name']=='Gallic acid':
        old=c['content_text']; c['content_text']="열매에서 동정[4]; 유카탄산 열대과일 세 가지(자주색 스타애플·캐슈 2종)의 동결건조 껍질에서 페룰산·카페산·시납산·엘라그산·미리세틴과 함께 확인(과일별 구분은 초록에 없음)[11]"
        changes.append({"where":"compounds.Gallic acid.content_text","before":old,"after":c['content_text'],"why":"[11] 초록은 세 과일 껍질 전체에서 6종을 확인했다고만 씀 — 스타애플 단독 결과처럼 쓰지 않음"})
    if c['name']=='Citral':
        old=c['activity_ko']; c['activity_ko']="씨 정유 최소억제농도 12.5 mg/mL(황색포도상구균·대장균·폐렴막대균), 잎 정유(황색포도상구균 0.781251 mg/mL)보다 약함(시험관); 씨는 허용 부위 아님[22]"
        changes.append({"where":"compounds.Citral.activity_ko","before":old,"after":c['activity_ko'],"why":"시트랄은 씨 정유 성분인데 잎 정유의 MIC를 활성으로 붙였음 — [22] 초록의 씨 정유 값으로 바꿈"})
lys=[c for c in C if c['name']=='Lysine'][0]; C.remove(lys)
changes.append({"where":"compounds.Lysine","before":json.dumps(lys,ensure_ascii=False),"after":"(삭제)","why":"함량 670 ppm은 열지 못한 [2]에만 기대고, [3]은 라이신을 따로 말하지 않음"})
# sources: drop 2, renumber
src=[s for s in d['sources'] if s['n']!=2]
m={}
for i,s in enumerate(src,1): m[s['n']]=i; s['n']=i
for s in src:
    if '(PMID 29222687' in s['title']:
        old=s['title']; s['title']=s['title'].replace('Inflammopharmacology 2018','Inflammopharmacology 2019(온라인 2017)')
        changes.append({"where":"sources[13→12].title","before":old,"after":s['title'],"why":"PubMed: 27권 5호(2019), 온라인 2017-12"})
d['sources']=src
def rn(t):
    def f(mo):
        parts=re.split(r'(\s*,\s*)',mo.group(1))
        return '['+''.join(str(m[int(x)]) if x.strip().isdigit() else x for x in parts)+']'
    return re.sub(r'\[(\d+(?:\s*,\s*\d+)*)\]',f,t)
for s in d['sections']: s['body']=rn(s['body'])
for arr in ('compounds','nutrients','assays'):
    for x in d.get(arr) or []:
        if 'source' in x: x['source']=[m[n] for n in x['source']]
        for k in ('content_text','activity_ko','content','rationale','method','basis'):
            if isinstance(x.get(k),str): x[k]=rn(x[k])
json.dump(d,open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
json.dump(changes,open(p.replace('dossier.json','_review/changes.json'),'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print(len(changes))
