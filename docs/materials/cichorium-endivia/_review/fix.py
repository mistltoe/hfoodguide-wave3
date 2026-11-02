import json,re,sys
P='/home/user/hfoodguide-wave3/docs/materials/cichorium-endivia/dossier.json'
d=json.load(open(P))
S={s['key']:s for s in d['sections']}
def rep(key,old,new):
    b=S[key]['body']; assert old in b,(key,old); S[key]['body']=b.replace(old,new)
# history
S['history']['body']=("앤디브의 기원은 아직 확실히 정리되지 않았다[5, 37]. 치커리속은 널리 재배되는 치커리(C. intybus)와 앤디브(C. endivia), 야생종 C. bottae·C. spinosum·C. calvum·C. pumilum으로 이루어지며, AFLP 분석에서 앤디브는 C. pumilum·C. calvum과 한 무리로 묶였다[37]. 2022년 유전체 비교 연구는 치커리가 앤디브의 조상이라는 기존 가설을 받아들이지 않았다[5]. 2025년 ddRAD 분석에서도 제꽃가루받이를 하는 앤디브·C. pumilum은 자가불화합성인 치커리·C. spinosum과 유전적으로 구분되었다[38].\n\n"
 "약용 전통도 남아 있다[35]. 이집트 시나이 사막 베두인 전통 의학에서 쓰는 식물 61종을 조사한 연구에서 앤디브 메탄올 추출물은 사람 림프종 세포에 비교적 강한 세포독성을 보인 식물 가운데 하나였다(시험관 결과)[35]. 앤디브는 지중해 지역에서 널리 먹는 식용 식물로도 소개된다[17].\n\n"
 "이탈리아 캄파니아주에서는 에스카롤 재배가 지역 경제의 중요한 활동으로 소개된다[10]. 한국에 언제 들어왔는지와 국내 고문헌 기록은 이번 조사에서 확인하지 못함.")
rep('related_species',"치커리속(Cichorium)의 대표 재배종은 앤디브와 치커리(C. intybus)이고, 지중해 지역에는 야생 근연종인 C. pumilum과 C. calvum이 자란다[2].",
    "치커리속(Cichorium)은 재배종인 치커리(C. intybus)·앤디브와 야생종 C. bottae·C. spinosum·C. calvum·C. pumilum으로 이루어지며, 앤디브는 C. pumilum·C. calvum과 유전적으로 가깝다[37].")
rep('related_species',"앤디브(C. endivia)와는 다른 종이다[32].","앤디브(C. endivia)와는 다른 종이다[32, 38].")
rep('cultivation',"이탈리아의 곱슬잎형·넓은잎형 앤디브 재배 면적은 6,800 ha가 넘고 생산량은 152,800 톤이 넘으며, 캄파니아주가 27,895 톤으로 가장 많이 생산한다[10].",
    "이탈리아 캄파니아주는 에스카롤의 주요 생산지로 소개되지만, 해당 논문이 인용한 재배 면적·생산량 수치는 기준 연도와 원 통계가 밝혀져 있지 않아 싣지 않는다[10].")
rep('safety',"생쥐 급성 경구 독성시험에서 앤디브 추출물의 LD50은 5,000 mg/kg보다 커 사실상 독성이 없다고 평가되었다[16].",
    "전초 에탄올 추출물의 60% 에탄올 용출 분획을 생쥐에 5,000 mg/kg 한 번 먹인 급성 경구 독성시험에서 LD50은 5,000 mg/kg보다 커 사실상 독성이 없다고 평가되었으나, 저자들은 추가 독성 연구로 확인해야 한다고 밝혔다[16].")
rep('safety',"식용 국화과 가운데 상추와 앤디브는 국화과 알레르기 환자의 20–30%에서 감작원으로 보고되었다[20].",
    "국화과 접촉 알레르기를 정리한 총설은 식용 국화과 가운데 상추와 앤디브의 감작 비율을 20–30%로 제시했다[20].")
d['world']=[]
for c in d['compounds']:
    if c['name']=='Lactucopicrin':
        c['activity_ko']="앤디브 쓴맛 지각에 지배적 영향[3, 13]; 순수 화합물이 생쥐 대식세포의 거품세포 형성을 억제하고 고지방식 ApoE 결손 생쥐 동맥경화반의 거품세포를 줄임(세포·동물, 앤디브 섭취 연구 아님)[15]"
    if c['name']=='Astragalin':
        c['activity_ko']="ORAC 항산화 활성(시험관); 이 화합물을 분리한 추출물(CEE)은 간세포·생쥐 산화 손상을 줄임[16]"
a=d['assays']
a[1]['part']="잎(에스카롤, 세균 비료 접종 후 60일 온실 재배) 동결건조물"
a[1]['conditions']['standard']="외부표준법: 프로토카테쿠산 유도체는 갈산 당량, 카페산 유도체는 카페산 당량, 캠페롤·퀘르세틴 유도체는 각각 'kaempferol 3-O-glucuoside'(원문 표기, 글루쿠로나이드/글루코사이드 불분명)·퀘르세틴 3-O-글루코사이드 당량"
a[2]['conditions']['detection']="고분해능 질량분석(Q Exactive); 정량 이온·모드는 본문에 없음. 정성 분석(양·음이온 모드)에서 락투신 [M+H]+ m/z 277.1070, 락투코피크린 [M+H]+ m/z 411.1448"
a[2]['rationale']="세스퀴테르펜 락톤은 치커리속 특유 성분으로, 이 성분이 가장 많은 'Leonida' 추출물이 세포 항산화·항염 효과도 가장 컸다고 저자들이 해석했다[10]. 정량 조건의 유속(정성 분석은 0.2 mL/min)·칼럼 온도·주입량·검출한계·정량한계·회수율은 본문에 없어 비워 둠."
# sources: drop 2, add 37,38
src=[s for s in d['sources'] if s['n']!=2]
src.append({"n":37,"title":"A search for diagnostic AFLP markers in Cichorium species with emphasis on endive and chicory cultivar groups. Genome. 2000","url":"https://pubmed.ncbi.nlm.nih.gov/10902710/","publisher":"PubMed","accessed":"2026-11-02"})
src.append({"n":38,"title":"A pioneering genotypic and phylogenetic characterisation of Cichorium crops through a genome-scale sequencing for future breeding innovations. BMC Plant Biol. 2025","url":"https://pubmed.ncbi.nlm.nih.gov/40610864/","publisher":"PubMed","accessed":"2026-11-02"})
old=[s['n'] for s in src]; m={o:i+1 for i,o in enumerate(old)}
for s in src: s['n']=m[s['n']]
d['sources']=src
def rn(x):
    if isinstance(x,str):
        def f(mo):
            nums=[int(t) for t in re.split(r',\s*',mo.group(1))]
            assert all(n in m for n in nums),mo.group(0)
            return '['+', '.join(str(m[n]) for n in nums)+']'
        return re.sub(r'\[(\d+(?:,\s*\d+)*)\]',f,x)
    if isinstance(x,list): return [rn(i) for i in x]
    if isinstance(x,dict):
        return {k:([m[i] for i in v] if k=='source' and isinstance(v,list) else rn(v)) for k,v in x.items()}
    return x
for k in list(d):
    if k not in('sources',): d[k]=rn(d[k])
json.dump(d,open(P,'w'),ensure_ascii=False,indent=1)
print(m)
