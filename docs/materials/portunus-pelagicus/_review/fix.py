import json, re, sys
p = sys.argv[1]
d = json.load(open(p, encoding='utf-8'))
sec = {s['key']: s for s in d['sections']}
changes = []
def rep(key, old, new, why):
    b = sec[key]['body']
    assert old in b, (key, old)
    sec[key]['body'] = b.replace(old, new)
    changes.append({"where": f"sections.{key}", "before": old, "after": new, "why": why})

rep('overview', "건강기능식품 고시형 원료의 원재료가 아니어서 식약처가 정한 지표성분은 없다[1].",
    "이 목록 행에는 지표성분·기능성 정보가 없으며, 이 종을 원재료로 한 건강기능식품 고시형 원료는 이번 조사에서 확인하지 못함.",
    "[1] 식품원료 목록(I1020) 행은 고시형 원료 여부를 말하지 않음 — 출처가 뒷받침하지 않는 단정을 약하게 바꿈")
rep('related_species', "미토콘드리아 유전체 13개 단백질 유전자를 이은 계통 분석",
    "미토콘드리아 유전체 단백질 유전자 12개를 이은 계통 분석",
    "[3] 초록은 'Phylogenetic analyses based on 12 concatenated protein-coding genes'")
rep('safety', "식약처 「식품원료 목록」에서 이 종은 별도 조건 없이 '사용가능' 원료이며, 건강기능식품 고시형 원료가 아니어서 고시 섭취 시 주의사항은 없다[1].",
    "식약처 「식품원료 목록」에서 이 종은 별도 사용 조건 없이 '사용가능' 원료로 올라 있고, 목록 행에 주의 문구는 없다[1]. 이 종에 해당하는 건강기능식품 고시 원료와 그 섭취 시 주의사항은 이번 조사에서 확인하지 못함.",
    "[1] 은 고시형 원료 여부를 말하지 않음 — 확인 가능한 범위(목록 행)로 좁힘")
rep('safety', "갑각류 알레르기 환자 24명의 혈청 실험에서",
    "새우 특이 IgE 양성인 갑각류·패류(shellfish) 알레르기 환자 24명의 혈청 실험에서",
    "[13] 대상자는 shellfish-allergic 이며 새우 특이 IgE(ImmunoCAP) 양성으로 선정됨")
rep('safety', "인도 남동 해안 조사에서는 구리와 카드뮴이 기준을 넘었고, 보르네오 조사에서는 근육이 안전한 수준이었다[21, 22].",
    "인도 남동 해안 조사에서는 이 종의 아가미·간췌장·근육 모두에서 구리와 카드뮴이 식품 안전 기준을 넘었다[21].",
    "[22] 보르네오 연구는 점박이꽃게·Scylla 등과 묶어 결과를 내 이 종만의 값이 초록에 없음(다른 종 자료 섞임) — 삭제; [21] 은 이 종의 모든 기관 Cu·Cd 초과로 명시")
rep('processing', "이 게에서 얻은 헤파란황산 함유 글리코사미노글리칸 추출물은 BACE1을 억제했으나 항응고 작용은 약했다[27].",
    "이 게에서 얻은 헤파란황산 함유 글리코사미노글리칸 추출물은 시험관 효소 실험에서 BACE1을 억제했으나 항응고 작용은 약했다[27].",
    "[27] 은 재조합 효소 시험관 실험 — 과장 방지로 실험 수준 명시")
rep('processing', "극초단파와 공융 용매로 뽑은 키틴은 쥐의 에탄올 위궤양 지수를 낮췄다[26].",
    "극초단파와 공융 용매(염화콜린·DL-말산)로 뽑은 키틴은 쥐 동물실험에서 에탄올 위궤양 지수를 낮췄다[26].",
    "[26] 은 Wistar 쥐 동물실험 — 실험 수준 명시, 용매는 초록대로")
# compounds
for c in d['compounds']:
    if c['name'] == 'Heparan sulfate':
        old = c['activity_ko']
        c['activity_ko'] = "시험관 효소 실험에서 알츠하이머병 관련 BACE1을 헤파린과 비슷하게 억제하면서 항응고 작용은 크게 약했다[27]"
        changes.append({"where": "compounds.Heparan sulfate.activity_ko", "before": old, "after": c['activity_ko'], "why": "시험관 결과임을 명시"})
    if c['name'] == 'Glycogen':
        old = c['content_text']
        c['content_text'] = old + " (원문 단위 그대로)"
        changes.append({"where": "compounds.Glycogen.content_text", "before": old, "after": c['content_text'], "why": "μg/mg 값이 1000을 넘어 단위가 비정상적이나 [35] 초록 표기 그대로임을 밝힘"})
# aliases
old = list(d['aliases'])
d['aliases'] = [a for a in d['aliases'] if a != 'Blue crab']
changes.append({"where": "aliases", "before": json.dumps(old, ensure_ascii=False), "after": json.dumps(d['aliases'], ensure_ascii=False), "why": "'Blue crab' 는 [15] 한 곳의 표기이고 Callinectes sapidus 의 영문명과 겹쳐 다른 종과 혼동 — 삭제"})
# remove source 22 and renumber
used_old = [s['n'] for s in d['sources'] if s['n'] != 22]
d['sources'] = [s for s in d['sources'] if s['n'] != 22]
m = {o: i+1 for i, o in enumerate(used_old)}
for s in d['sources']: s['n'] = m[s['n']]
REF = re.compile(r"\[(\d+(?:\s*,\s*\d+)*)\]")
def rn(t):
    if not isinstance(t, str): return t
    return REF.sub(lambda mo: "[" + ", ".join(str(m[int(x)]) for x in re.split(r"\s*,\s*", mo.group(1))) + "]", t)
for s in d['sections']: s['body'] = rn(s['body'])
for arr in ('compounds','assays','world','markers','nutrients','production','gi','orgs'):
    for x in d.get(arr) or []:
        if 'source' in x: x['source'] = [m[int(n)] for n in x['source']]
        for k, v in list(x.items()):
            if isinstance(v, str): x[k] = rn(v)
            elif isinstance(v, dict):
                for kk, vv in v.items(): v[kk] = rn(vv)
json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(changes, open(p.replace('dossier.json', '_review/changes.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(changes))
