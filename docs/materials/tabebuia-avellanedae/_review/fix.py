import json, re, sys
p = sys.argv[1]
d = json.load(open(p, encoding='utf-8'))
S = {s['key']: s for s in d['sections']}
changes = []
def rep(key, old, new, why):
    b = S[key]['body']
    assert old in b, (key, old[:40])
    S[key]['body'] = b.replace(old, new)
    changes.append({"where": f"sections.{key}", "before": old, "after": new, "why": why})

d['aliases'] = [a for a in d['aliases'] if a != '라파초']
changes.append({"where": "aliases", "before": "라파초", "after": "(삭제)", "why": "출처 없는 국문 별명"})

rep('overview', "라파콜을 고용량으로 먹인 쥐에서 태아 사망이 보고되었고 비타민 K 대사를 방해한다는 지적이 있어, 임신부와 항응고제 복용자는 주의가 필요하다[11, 4, 12].",
    "순수 라파콜을 임신한 쥐에게 먹인 실험(마리당 하루 10–20 mg, 임신 8–12일)에서 태아 사망이 보고되었고, 라파콜이 비타민 K 순환을 방해할 수 있다는 지적이 있다[11, 25, 4]. 사람에서 확인된 독성 근거는 아니지만, 임신부와 항응고제 복용자에게는 주의가 안내된다[12].",
    "[11]·[25] 투여량은 마리당 20·10 mg 으로 '고용량' 표현 근거 없음; 동물·순수 성분 결과임을 밝힘")
rep('overview', "또 건강기능식품(C코드) 쪽에는 개별인정형 원료 '타히보 추출물(기능성원료인정 제2022-2호)'이 따로 올라 있다[1].",
    "또 건강기능식품(C코드) 쪽에는 개별인정형 원료 '타히보 추출물(기능성원료인정 제2022-2호)'이 따로 올라 있다(학명 Tabebuia avellanedae)[1].",
    "I1020 원자료 행 확인(상표명은 적지 않음)")

rep('history', "그 결과 라파콜과 β-라파콘이 주요 생리활성 성분으로 분리되었다[4]. β-라파콘의 합성품은 췌장암 등을 대상으로 임상시험에 들어갔다[10].",
    "이 나무에서 분리된 주요 생리활성 성분으로는 라파콜과 β-라파콘이 꼽힌다[4]. β-라파콘은 췌장암 치료를 대상으로 2상 임상시험이 진행되었다고 정리되었다[10].",
    "[4] 는 NCI 조사의 '결과'로 분리됐다고 쓰지 않음; [10] 초록은 '합성품'이 임상에 쓰였다고 하지 않고 2상 임상만 언급")
rep('history', "한국에서는 식약처 「식품원료 목록」에 껍질을 쓰는 식품 원료로 올라 있고, 2022년 개별인정형 건강기능식품 원료(제2022-2호)가 인정되었다[1].",
    "한국에서는 식약처 「식품원료 목록」에 껍질을 쓰는 식품 원료로 올라 있고, 같은 목록에 인정번호 '제2022-2호'인 개별인정형 건강기능식품 원료 '타히보 추출물'도 올라 있다[1]. 이 원료의 인정일·기능성 내용은 식약처 원문으로 확인하지 못함.",
    "목록에는 인정번호만 있고 인정일·기능성은 원문 미확인")

rep('biology', "분홍~보라색 꽃이 화려해 유럽에서도 정원과 공공장소에 조경수로 심는다[14].",
    "꽃이 아름다운 나무로 꼽혀 유럽에서도 정원과 공공장소에 조경수로 널리 심는다[14].",
    "[14] 는 꽃 색을 적지 않음")
rep('biology', "목재는 '새로운 마호가니'로 불릴 만큼 비싸며,",
    "목재는 '새로운 마호가니'로 불리며 두 번째로 비싼 목재로 꼽히고,",
    "[13] 원문 표현에 맞춤")
rep('biology', "같은 속(Tabebuia·Handroanthus)에서는 이리도이드 36종, 페놀산 32종, 퀴논·나프토퀴논 50종 등 163개 화합물이 정리되었다[5].",
    "속 수준(여러 종)의 문헌 정리에서는 이리도이드 36종, 페놀산 32종, 퀴논·나프토퀴논 50종 등 163개 화합물이 집계되었는데, 이는 이 종 하나만의 값이 아니다[5].",
    "[5] 는 다른 연구(속 여러 종 집계)를 인용; 근연종 자료 섞임 방지")

rep('cultivation', " 이 등재는 24개월 유예를 거쳐 2024년 11월 25일 발효되었다[19].",
    " 이 등재의 유예 기간과 발효일은 CITES 원문을 열지 못해 확인하지 못함.",
    "[19] cites.org 가 이 환경에서 열리지 않아 날짜 대조 불가 — 단정 삭제")
rep('related_species', "2022년 CITES 제19차 당사국총회는 Handroanthus·Roseodendron·Tabebuia 세 속을 부속서 II에 함께 올렸다[18, 19].",
    "2022년 CITES 제19차 당사국총회는 Handroanthus·Roseodendron·Tabebuia 세 속을 부속서 II에 함께 올렸다[18].",
    "[19] 삭제에 따른 번호 정리")
rep('cultivation', "부속서 II에 등재되었고, 대상 품목은 주석 #17이다[18, 19].",
    "부속서 II에 등재되었고, 대상 품목은 주석 #17이다[18].", "[19] 삭제")
rep('cultivation', "묘목 단계에서는 이탈리아 양묘장에서 Rhizoctonia solani에 의한 모잘록병이 보고되는 등 병해가 알려져 있다[14].",
    "묘목 단계에서는 이탈리아 시칠리아의 양묘장에서 Rhizoctonia solani AG-4에 의한 모잘록병이 처음 보고되었다[14].",
    "[14] 원문 세부에 맞춤")

rep('processing', "생쥐 귀 부종을 줄였다[21].", "아라키돈산으로 유도한 생쥐 귀 부종을 줄였다(경구 100 mg/kg, 1주; 크로톤유 유도 부종에는 효과 없음)[21].",
    "[21] 초록: 아라키돈산 유도에만 효과")
rep('processing', "에탄올 추출물은 통증·염증 동물 모델에서 효과를 보였다[15].",
    "에탄올 추출물은 200 mg/kg에서 통증·염증 동물 모델의 반응을 30–50% 줄였으나 100 mg/kg에서는 유의하지 않았다[15].",
    "[15] 초록 수치·용량 추가(과장 방지)")
rep('processing', "체중·지방량을 줄였고, 지표로 1-dehydroxy-3,4-dihydroaucubigenin이 분리되었다[22].",
    "체중·지방량을 줄였고(사료 0.5%, 16주), 3T3-L1 세포 활성 추적 분리로 후보 성분 1-dehydroxy-3,4-dihydroaucubigenin을 얻었다[22].",
    "[22] 에서 이 성분은 '지표'가 아니라 활성 추적으로 얻은 후보 성분")
rep('processing', "2025년 약 1.87억 원으로 집계되었다[20].",
    "2025년 약 1.87억 원으로 집계되었고, 수출액은 2024년 77,761달러, 2025년 50,062달러였다[20]. 이는 동물·세포 결과와 별개로 제품 시장 규모를 보여 주는 값이다[20].",
    "production 배열의 제품 수출 실적을 본문으로 옮김(V 규칙)")

rep('genetics', "accD·clpP·rpoA·ycf1·ycf2 등에서 뉴클레오타이드 다양성 열점과 양성 선택 신호가 확인되었다[17].",
    "accD·clpP·rpoA·ycf1·ycf2에서 뉴클레오타이드 다양성 열점이 확인되었고, 여러 유전자에서 자리 수준 양성 선택 신호가 나왔다[17].",
    "[17] 초록: 열점 유전자와 양성 선택 유전자는 별개로 서술됨")

rep('safety', "빈혈 관련 검사치 이상이 두 명 넘게 나타나 모니터링이 필요하다고 정리되었다[23].",
    "검사치 이상 가운데 빈혈 관련 지표만 한 명 넘게 나타나 앞으로 모니터링이 필요하다고 정리되었다[23]. 12명 중 9명이 끝까지 참여했고, 2명은 견디기 어렵다며 중도 탈락했다[23].",
    "[23] 전문: 'more than one participant' — '두 명 넘게'는 오역")
rep('safety', "라파콜의 독성 근거는 주로 설치류 자료다[4, 25].",
    "라파콜의 독성 근거는 순수 라파콜을 쥐에게 먹인 실험 자료이며, 사람에서 같은 독성이 확인된 것은 아니다[4, 25].",
    "동물·순수 성분 근거임을 명시")
rep('safety', "임신한 쥐에게 라파콜을 임신 8–12일째 먹인 실험에서 태아·배아 사망률이 99–100%로 보고되었고, 임신 17–20일째 투여에서는 태아 성장 지연이 나타났다[11, 25, 26].",
    "임신한 쥐에게 라파콜을 임신 8–12일째 마리당 하루 20 mg 또는 10 mg 먹인 실험에서 어미에는 이상이 없었으나 태아·배아 사망률이 100%·99.2%였다[11, 25]. 임신 17–20일째 100 mg/kg 투여에서는 어미 독성 없이 태아 성장 지연이 나타났다[26].",
    "[11][25][26] 초록의 용량·결과로 구체화")
rep('safety', "수컷 쥐 단기 투여에서는 정낭 무게가 줄었다[27].",
    "수컷 쥐에 100 mg/kg을 5일 먹이자 정낭 무게가 줄었으나 정자 생산에는 유의한 변화가 없었다[27].", "[27] 용량·결과")
rep('safety', "라파콜 365 mg/kg 단회 경구 투여는 쥐 골수세포에서 소핵·염색체 이상을 늘렸다(클라스토젠 효과)[9].",
    "라파콜을 122·244·365 mg/kg 단회 경구 투여한 시험에서 가장 높은 용량(365 mg/kg)이 쥐 골수세포의 소핵·염색체 이상을 늘렸다(클라스토젠 효과)[9].",
    "[9] 용량 범위 명시")
rep('safety', "라파콜은 비타민 K 대사(에폭사이드·퀴논 환원효소 억제)를 방해해 와파린과 비슷하게 작용할 수 있다[4, 12].",
    "라파콜은 비타민 K 순환을 방해할 수 있다고 정리되며[4], 쥐 간 마이크로솜 시험관 실험에서 와파린·디쿠마롤처럼 비타민 K 에폭사이드·퀴논 환원을 억제했다[34]. 이것이 사람에서 출혈로 이어지는지는 불확실하다[12].",
    "효소 억제 근거는 [4][12] 가 아니라 시험관 연구 — 1차 출처 추가, 과장 완화")

# compounds
comps = d['compounds']
for c in comps:
    if c['name'] == 'Lapachol':
        c['part'] = "심재·껍질(속껍질 추출물에서는 검출 안 되거나 낮음)"
        c['content_text'] = "시판 속껍질 70% 에탄올 추출물에서 검출되지 않음(검출한계 미만 가능)⟦gil⟧; 껍질에서 모기 유충 살충 성분으로 분리, Culex pipiens pallens 유충 LC50 8.30 mg/L⟦larv⟧"
        c['activity_ko'] = "쥐 실험(순수 성분): 임신기 투여 시 태아 사망·성장 지연, 고용량(365 mg/kg) 단회 투여 시 골수세포 염색체 이상; 시험관에서 비타민 K 에폭사이드·퀴논 환원 억제⟦rep99,rep02,clast,vitk⟧"
        c['source'] = [5, 30, 11, 26, 9, 34]
        changes.append({"where": "compounds.Lapachol", "before": "비타민 K 대사 방해로 출혈 위험", "after": "시험관에서 비타민 K 환원 억제(동물·순수 성분 근거 명시)", "why": "출혈 위험 단정은 사람 근거 없음; [30] 중복 항목 병합"})
    if c['name'] == 'beta-Lapachone':
        c['activity_ko'] = "토포아이소머레이스 I 억제·NQO1 유도; 항암 등으로 연구되며 췌장암 2상 임상시험이 진행되었다고 정리됨⟦blap⟧"
        changes.append({"where": "compounds.beta-Lapachone", "before": "합성품이 췌장암 임상시험에 쓰임", "after": "췌장암 2상 임상시험이 진행되었다고 정리됨", "why": "[10] 초록에 '합성품' 언급 없음"})
    if c['name'] == 'Furanonaphthoquinones':
        c['part'] = "부위 확인하지 못함(초록에 부위 없음)"
        changes.append({"where": "compounds.Furanonaphthoquinones.part", "before": "속껍질", "after": "부위 확인하지 못함", "why": "[31] 초록에 부위 없음"})
    if c['name'] == '1-dehydroxy-3,4-dihydroaucubigenin':
        c['part'] = "n-뷰탄올 추출물(부위 미기재)"
dup = [c for c in comps if c['name'].startswith('2-Hydroxy-3-(3-methyl')]
for c in dup: comps.remove(c)
changes.append({"where": "compounds", "before": "2-Hydroxy-3-(3-methyl-2-butenyl)-1,4-naphthoquinone (lapachol) 별도 항목", "after": "Lapachol 항목에 병합", "why": "같은 화합물 중복"})

# assays
old = d['assays'][0]
d['assays'] = [a for a in d['assays'] if a['role'] != 'official']
changes.append({"where": "assays[official]", "before": old['rationale'], "after": "(삭제)", "why": "고시·공전 원문 없음(V2 규칙). '관절 건강·1일 600 mg'은 요약 사이트(ChemLinked) 검색 요약뿐이라 근거 불충분"})
for a in d['assays']:
    if a['compound'] == 'Veratric acid':
        a['conditions']['instrument'] = "LC-UV"
        a['conditions']['standard'] = "베라트르산(3,4-다이메톡시벤조산)"
        a['rationale'] = "속껍질 에탄올 추출물의 품질 관리용으로 베라트르산을 LC-UV로 정량하는 첫 간단·신뢰 방법으로 제안됨. 조건은 초록 기준이며 전문 확인 못함(검출·정량한계·주입량 비움)⟦aoac⟧."
        changes.append({"where": "assays[Veratric acid]", "before": "instrument 'LC-UV(가변파장/UV 검출)'·라파콜 함량이 낮아 지표로 어렵다는 근거", "after": "초록에 있는 값만 남김, '전문 확인 못함'", "why": "초록에 없는 기기·이유 서술"})

# production
pr = d['production']; d['production'] = []
changes.append({"where": "production", "before": json.dumps(pr, ensure_ascii=False), "after": "[] (processing 본문으로 이동)", "why": "제품 생산실적(hf_items.csv)은 production 에 넣지 않음"})

# sources
d['sources'] = [s for s in d['sources'] if s['n'] not in (19, 33)]
d['sources'].append({"n": 34, "title": "Preusch PC, Smalley DM. Vitamin K1 2,3-epoxide and quinone reduction: mechanism and inhibition. Free Radic Res Commun 1990;8(4-6):401-415 (PMID 2113031)",
    "url": "https://doi.org/10.3109/10715769009053374", "publisher": "Free Radical Research Communications (Taylor & Francis)", "accessed": "2026-11-02"})
# renumber
order = [s['n'] for s in d['sources']]
m = {o: i+1 for i, o in enumerate(order)}
for s in d['sources']: s['n'] = m[s['n']]
REF = re.compile(r"\[(\d+(?:\s*,\s*\d+)*)\]")
def rn(t):
    if not isinstance(t, str): return t
    return REF.sub(lambda mo: "[" + ", ".join(str(m[int(x)]) for x in re.split(r"\s*,\s*", mo.group(1))) + "]", t)
for s in d['sections']: s['body'] = rn(s['body'])
for arr in ('compounds','assays','production','world','gi','orgs','markers'):
    for x in d.get(arr) or []:
        x['source'] = [m[int(n)] for n in x.get('source', [])]
        for f in ('content_text','activity_ko','content','rationale','note'):
            if f in x: x[f] = rn(x[f])
json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(changes, open(p.replace('dossier.json','_review/changes.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(changes), m)
