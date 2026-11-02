import json, re, sys
P='/home/user/hfoodguide-wave3/docs/materials/auricularia-cornea/'
d=json.load(open(P+'dossier.json'))
changes=[]
def sec(k): return next(s for s in d['sections'] if s['key']==k)
def rep(where, obj, key, old, new, why):
    v=obj[key]
    assert old in v, (where, old)
    obj[key]=v.replace(old,new,1)
    changes.append({"where":where,"before":old,"after":new,"why":why})

o=sec('overview')
rep('sections.overview',o,'body',
 "식품의약품안전처 「식품원료 목록」에는 원료명 '뿔목이', 학명 Auricularia cornea Ehrenb.로 올라 있고, 상태는 '사용가능', 사용 조건과 부위는 '자실체'이다[1].",
 "식품의약품안전처 「식품원료 목록」(I1020, 2026-10-13 받은 원자료)에는 대표원료명 '뿔목이', 학명 'Auricularia cornea Ehrenb.', 사용조건 '사용가능', 사용조건기준 '자실체', 부위 '자실체'로 한 항목이 올라 있고 이명(별칭) 칸은 비어 있다[1].",
 "I1020 원자료 행(RPRSNT_RAWMTRL_NM·SCNM·USE_CND_NM·USE_CND_STDR_CN·REGN_CD_NM·RAWMTRL_NCKNM)과 대조해 필드값을 그대로 밝힘")
rep('sections.overview',o,'body',
 "반면 식약처 목록에는 학명 칸이 'Auricularia polytricha Sacc. / Auricularia nigricans (Sw.) Birkebak'인 털목이버섯이 뿔목이와 별도 항목으로 올라 있다[1].",
 "반면 식약처 목록에는 대표원료명 '털목이버섯'(이명 '털목이'), 학명 칸 'Auricularia polytricha Sacc. / Auricularia nigricans (Sw.) Birkebak'인 항목이 뿔목이와 별도로 올라 있어, 목록상 A. polytricha는 뿔목이가 아니라 털목이버섯의 학명으로 쓰인다[1].",
 "I1020 원자료로 털목이버섯 행의 이명·학명 처리를 확인해 명시")
rep('sections.overview',o,'body',
 "연구는 흰 자실체 계통(위무얼, A. cornea var. Li.)과",
 "연구는 흰 자실체 계통(위무얼, 'var. Li.' 등)과",
 "[2]의 위무얼과 [12]의 var. Li.가 같은 계통이라고 밝힌 출처가 없어 등치 표현을 완화")

h=sec('history')
rep('sections.history',h,'body',
 "2021년 분류 연구는 이 종의 학명 아래에 1822년 「Systema mycologicum」에 실린 다른 속의 조합과 1942년·1985년·1991년에 발표된 이름들을 이명으로 모았다[2].",
 "2021년 분류 연구는 이 종의 학명 아래에 1822년 Fries의 「Systema mycologicum」에 실린 동일 기준 이름과 1942년·1985년·1991년에 발표된 이름들을 이명으로 모았다[2].",
 "[2] 전문(학명 제거된 텍스트)에서 1822년 조합이 '다른 속'이라는 점은 확인되지 않아 '≡(Ehrenb.) Fr.' 표기대로 동일 기준 이름으로 고침")
rep('sections.history',h,'body',
 "\n\n국내에서는 2021년 국립수목원이 목이속 분류 결과를 발표하며 '털목이'로 알려진 종 가운데 뿔목이가 있다고 알렸다는 검색 요약이 있으나, 원문은 열어 보지 못했다[30].",
 "\n\n국명 '뿔목이'의 근거로 이번에 확인한 것은 식약처 「식품원료 목록」의 원료명뿐이며, 국내 명명 경위를 밝힌 공식 원문은 확인하지 못함[1].",
 "[30] 국립수목원 보도자료는 검색 요약뿐이고 원문을 열지 못해(차단, 재시도 금지) 내용을 삭제하고 확인하지 못함으로 바꿈")

b=sec('biology')
rep('sections.biology',b,'body',"자실체는 물을 머금으면 젤라틴질이고","자실체는 신선할 때 젤라틴질이고",
 "[2] 원문은 'Gelatinous when fresh'")

r=sec('related_species')
rep('sections.related_species',r,'body',
 "2021년 분류 연구는 A. cornea를 털이 빽빽하고 수층이 있는 종들의 복합군에 넣었다[2].",
 "2021년 분류 연구는 A. cornea의 특징으로 신선한 자실체 색의 변이, 윗면의 빽빽한 털, 뚜렷한 수층을 들었다[2].",
 "[2] 전문에서 '털이 빽빽하고 수층이 있는 종들의 복합군' 정의를 확인할 수 없어 Notes 원문(특징 기술)으로 바꿈")

c=sec('cultivation')
rep('sections.cultivation',c,'body',
 "국내 흰색 뿔목이 품종 '새얀'이 2024년 보고되었다는 검색 요약이 있으나 원문은 확인하지 못했고, 국내 생산 면적·생산량 공식 통계도 확인하지 못함[31].",
 "국내 품종 등록 현황과 생산 면적·생산량 공식 통계는 확인하지 못함[1].",
 "[31] 한국버섯학회지 논문은 검색 요약뿐이고 KCI 원문을 열지 못해(차단) 품종명 언급을 삭제")

g=sec('genetics')
rep('sections.genetics',g,'body',"A. cornea 균주 AC1을 PacBio로 해독해","A. cornea 균주 AC1을 단일분자 장판독 서열 22.37 Gbp(304배)로 해독해",
 "[8] 전문·초록에서 플랫폼명 'PacBio'는 확인되지 않음(이름이 빠진 텍스트), 원문의 'single-molecule long reads 22.37 Gbp (304×)'로 바꿈")

s=sec('safety')
rep('sections.safety',s,'body',"봉크렉산은 무색·무미하고 열에 안정하며 보통 식품에서 검출되지 않는다[20].",
 "봉크렉산은 무색·무미하고 열에 안정하며 대개 식품 속에서 알아차리기 어렵다(원문 'usually not detectable in food')[20].",
 "원문 뜻(감지가 어렵다)과 달리 '검출되지 않는다'로 읽혀 오해 소지가 있어 고침")
rep('sections.safety',s,'body',"이 세균을 A. cornea var. Li. 조각에 접종한 실험에서 펄스광(35.4 J/cm²)은 약 4 로그를 줄였다[20].",
 "이 세균을 멸균 후 불린 A. cornea var. Li. 조각에 접종한 실험에서 펄스광(35.4 J/cm²)은 약 3.9–4.2 로그를 줄였다[20].",
 "[20] 전문 3.2절: AC에서 3.92 ± 0.16(초기 7 Log), 4.16 ± 0.15(초기 6 Log) 로그 감소")
rep('sections.safety',s,'body',"당뇨 생쥐에 다당체를 100·400 mg/kg씩 30일 먹인 실험에서 장기 지수와 간·신장 조직에 뚜렷한 이상이 없었다[12].",
 "당뇨 모델 생쥐에 다당체를 100·400 mg/kg씩 30일 먹인 효능 실험에서 장기 지수와 간·신장 조직에 뚜렷한 이상이 없었다고 했으나, 독성 시험 설계는 아니다[12].",
 "[12]는 당뇨 모델 효능 실험이며 독성 시험이 아님 — 안전성 근거 과장 방지")
rep('sections.safety',s,'body',"[22, 23]","[22, 23]","")  # noop marker
changes.pop()

# compounds
cp=next(x for x in d['compounds'] if x['name']=='Polysaccharide')
rep('compounds[Polysaccharide].content_text',cp,'content_text',
 "총다당(페놀-황산법) 37.63 ± 4.3–215.88 ± 2.4 mg/g,",
 "총다당(페놀-황산법, 조다당 시료를 녹여 측정 — 결과는 '자실체 총다당'으로 표기되어 기준이 모호) 37.63 ± 4.3–215.88 ± 2.4 mg/g,",
 "[7] Methods: 총다당은 조다당 1 mg을 물 10 mL에 녹여 측정 — 자실체 건물 기준인지 조다당 기준인지 원문이 모호함을 밝힘")
rep('compounds[Polysaccharide].activity_ko',cp,'activity_ko',"조다당 1.50 mg/mL에서","7개 균주 조다당 1.50 mg/mL에서",
 "[7] 항산화 시험은 50개 중 7개 균주만 수행")
fe=next(x for x in d['compounds'] if x['name']=='Iron')
zn=next(x for x in d['compounds'] if x['name']=='Zinc')
rep('compounds[Zinc].content_text',zn,'content_text',"(원자흡광)[7]","(35 °C 건조 시료, 원자흡광)[7]","[7] 시료는 35 °C 24시간 건조 분말 — 건물 기준 명시")
rep('compounds[Iron].content_text',fe,'content_text',"(원자흡광, 본문 표 기준;","(35 °C 건조 시료, 원자흡광, 본문 표 기준;","같은 이유")

# assays
a0=d['assays'][0]
rep('assays[0].content',a0,'content',"37.63 ± 4.3 mg/g(Ac6)–215.88 ± 2.4 mg/g(Ac1)[7]",
 "37.63 ± 4.3 mg/g(Ac6)–215.88 ± 2.4 mg/g(Ac1); 측정 시료는 조다당이고 결과 표기는 '자실체 총다당'이라 기준(조다당 g당 또는 자실체 g당)이 원문에서 모호함[7]",
 "생/건·기준 확인: 원문 Methods와 Results 표기 불일치")
a1=d['assays'][1]
rep('assays[1].content',a1,'content',"구리 0.133–8.40 mg/kg[7]","구리 0.133–8.40 mg/kg(35 °C 건조 시료 기준)[7]","[7] Methods: 35 °C 24시간 건조 후 분석")
a2=d['assays'][2]
rep('assays[2].conditions.sample_prep',a2['conditions'],'sample_prep',
 "선행 방법으로 열수 추출 후 Sevag법으로 제단백(세부 조건은 인용 문헌에 미룸)",
 "인용 문헌의 방법으로 추출(추출 용매·온도는 원문에 없음) 후 Sevag법으로 제단백",
 "[12] 전문 2.2절은 'extracted using the method of []'뿐이며 '열수 추출'이라는 말이 없음")
rep('assays[2].conditions.instrument',a2['conditions'],'instrument',
 "6890-5975 가스크로마토그래프-질량분석기(원문 표기)",
 "6890-5975 가스크로마토그래프-질량분석기(원문 표기, 공급처 Thermo Fisher Scientific(상하이)로 적힘)",
 "[12] 원문 표기 그대로 보완")

# history citation fix
rep('sections.history',h,'body',"골라 길들인 것이 'A. cornea var. Li.'로 소개된다[2, 12].","골라 길들인 것이 'A. cornea var. Li.'로 소개된다[12].",
 "[2]에는 var. Li. 언급이 없음 — 출처를 [12]만 남김")

# sources: drop 30,31 and renumber
src=[x for x in d['sources'] if x['n'] not in (30,31)]
m={x['n']:i+1 for i,x in enumerate(src)}
for x in src: x['n']=m[x['n']]
for x in src:
    if 'BMC Genomics 2026;27:(1)' in x['title']:
        x['title']=x['title'].replace('BMC Genomics 2026;27:(1)','BMC Genomics 2026;27(1)')
d['sources']=src
def remap_text(t):
    def f(mo):
        nums=[int(n) for n in re.split(r',\s*',mo.group(1))]
        for n in nums: assert n in m, n
        return '['+', '.join(str(m[n]) for n in nums)+']'
    return re.sub(r'\[(\d+(?:,\s*\d+)*)\]',f,t)
def walk(o):
    if isinstance(o,dict):
        for k,v in o.items():
            if k=='sources': continue
            if k=='source' and isinstance(v,list): o[k]=[m[n] for n in v]
            elif isinstance(v,str): o[k]=remap_text(v)
            else: walk(v)
    elif isinstance(o,list):
        for i,v in enumerate(o):
            if isinstance(v,str): o[i]=remap_text(v)
            else: walk(v)
walk(d)
json.dump(d,open(P+'dossier.json','w'),ensure_ascii=False,indent=1)
json.dump(changes,open(P+'_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
