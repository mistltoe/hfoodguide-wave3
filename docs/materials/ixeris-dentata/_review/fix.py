import json, re
P='/home/user/hfoodguide-wave3/docs/materials/ixeris-dentata/dossier.json'
d=json.load(open(P))
changes=[]
def rep(where, obj, key, old, new, why):
    s=obj[key]
    assert old in s, (where, old)
    obj[key]=s.replace(old,new)
    changes.append({"where":where,"before":old,"after":new,"why":why})
S={s['key']:s for s in d['sections']}
rep("sections.related_species",S['related_species'],'body',
 "산씀바귀는 Lactuca raddeana로 왕고들빼기속이다[1]",
 "산씀바귀는 학명이 Lactuca raddeana인 Lactuca 속 원료다[1]",
 "[1] 원자료는 학명만 적고 국문 속명(왕고들빼기속)은 없음")
rep("sections.related_species",S['related_species'],'body',
 "씀바귀·흰씀바귀·고들빼기(Ixeris sonchifolia로 표기)를 비교한 연구에서 총페놀 함량은 각각 30, 35.33, 43.79 mg/g GAE였다[4]. 같은 연구에서 루테올린 7-O-글루코사이드가 씀바귀(8.76 mg/g 건조중량)와 흰씀바귀(10.35 mg/g 건조중량)의 주성분이었고, 고들빼기에서는 루테올린 7-O-글루쿠로나이드(34.66 mg/g 건조중량)가 주성분이었다[4].",
 "씀바귀(Ixeris dentata)·흰씀바귀(var. albiflora)·Ixeris sonchifolia를 비교한 연구에서 총페놀 함량은 씀바귀 30 mg/g GAE, 흰씀바귀 35.33 mg/g GAE였고, Ixeris sonchifolia가 43.79 mg/g GAE로 가장 높았다[4]. 같은 연구에서 루테올린 7-O-글루코사이드가 씀바귀(8.76 mg/g 건조중량)와 흰씀바귀(10.35 mg/g 건조중량)의 주성분이었고, Ixeris sonchifolia에서는 루테올린 7-O-글루쿠로나이드(34.66 mg/g 건조중량)가 주성분이었다[4]. Ixeris sonchifolia는 흔히 고들빼기로 불리지만 식약처 목록의 고들빼기 학명(Crepidiastrum sonchifolium / Youngia sonchifolia)에는 이 이름이 없어, 이 출처만으로 같은 원료인지는 확인하지 못함이며 고들빼기 자료로 옮겨 쓰지 않는다[1, 4].",
 "[4] 초록은 'Ixeris sonchifolia'로만 적음 — 고들빼기로 단정한 부분을 원 표기로 되돌리고 고들빼기 자료와 섞이지 않게 함")
rep("sections.cultivation",S['cultivation'],'body',
 " 2019년 국내 학술지 논문은 2015년 10월 초 흰씀바귀의 주 재배지로 경기 양평·충남 당진·강원 춘천·충북 괴산의 4개 지역을 들고 그곳에서 1년생 재래종을 모아 생육 특성을 조사했다고 하나, 이는 검색 요약으로만 확인했고 원문은 확인하지 못함[27].",
 " 흰씀바귀의 국내 주 재배지는 원문으로 확인한 자료가 없어 확인하지 못함.",
 "[27]은 WebSearch 요약으로만 확인되고 원문(koreascience)이 허용 목록 밖이라 열 수 없음 — 재배지·연도 주장을 덜어냄")
rep("sections.cultivation",S['cultivation'],'body',
 "새 바이러스 두 종이 분리된 보고가 있다[20]",
 "새 바이러스 두 종(폴레로바이러스속·움브라바이러스속으로 분류 제안)이 분리된 보고가 있다[20]",
 "[20] 초록 내용 보강(맞는 문장, 표현만 구체화)")
rep("sections.processing",S['processing'],'body',
 "변종을 밝히지 않은 씀바귀 연구에서는 물·에탄올·메탄올 추출물과 녹즙(green sap)이 시험 재료로 쓰였다[6, 15, 23].",
 "변종을 밝히지 않은 씀바귀 연구에서는 물·에탄올 추출물, 메탄올 추출물의 물 분획, 녹즙(green sap)이 시험 재료로 쓰였다[6, 15, 23, 29].",
 "[6]·[15]·[23]에는 메탄올 추출물이 없음 — 메탄올 추출물의 물 분획을 쓴 [29]를 붙임")
rep("sections.processing",S['processing'],'body',
 "비피도박테리움이나 락토바실루스로 발효한 씀바귀 추출물이 쥐에서 발효하지 않은 것보다 알레르기 반응을 더 억제했다는 동물 결과가 있다[22].",
 "비피도박테리움 브레베나 락토바실루스 아시도필루스로 발효한 씀바귀 추출물이 생쥐에서 발효하지 않은 것보다 수동 피부 아나필락시스와 긁기 행동을 더 억제했다는 세포·동물 결과가 있다[22].",
 "[22] 초록: 실험동물은 생쥐(mice), 지표는 PCA 반응·긁기 행동, 세포 실험(RBL-2H3) 병행")
rep("sections.genetics",S['genetics'],'body',
 "일본의 Ixeridium dentatum ssp. dentatum은 무수정 생식을 하는 3배체로 보고되었으며",
 "동아시아 저지대에 분포하는 Ixeridium dentatum ssp. dentatum은 무수정 생식을 하는 3배체로 보고되었으며(표지 개발에는 일본 개체를 씀)",
 "[18] 초록은 분포를 동아시아 저지대로 적고, 일본은 시료 출처임")
rep("sections.safety",S['safety'],'body',
 "씀바귀 물 분획 1.0 g/kg을 4일 먹인 생쥐에서",
 "씀바귀 메탄올 추출물의 물 분획 1.0 g/kg을 4일 연속 투여한 생쥐에서",
 "[29] 초록은 '메탄올 추출물의 물 분획'이며 투여 경로를 적지 않음")
rep("sections.safety",S['safety'],'body',
 "씀바귀 성분 이소류실락투신의 폐 대식세포 염증 억제도 세포 결과다[17].",
 "씀바귀 잎에서 분리한 성분 이소류실락투신이 생쥐 폐포 대식세포주에서 석탄 비산재로 유발한 염증을 억제한 것도 세포 결과다[17].",
 "[17] 전문: 잎 메탄올 추출물에서 분리, MH-S(생쥐 폐포 대식세포주), 석탄 비산재 자극")
# compounds
C={c['name']:c for c in d['compounds']}
for nm in ["Ixerin M","Ixerisoside A","8-Epidesacylcynaropicrin 3-O-glucoside"]:
    c=C[nm]
    for k in ['part','content_text']:
        if '전초' in c[k]:
            old=c[k]; c[k]=old.replace('씀바귀 전초 추출물','씀바귀 전체 추출물(부위 미기재)').replace('씀바귀 전초','씀바귀 전체 추출물(부위 미기재)')
            changes.append({"where":f"compounds[{nm}].{k}","before":old,"after":c[k],"why":"[8] 초록은 'whole extract of Ixeris dentata'로 부위(전초)를 밝히지 않음"})
# sources
src={s['n']:s for s in d['sources']}
old=src[20]['title']; src[20]['title']=old.replace('(Arch Virol 2017, PMID 28905257, 초록)','(Arch Virol 2017;162(12):3893-3897, PMID 28905257, 초록)')
changes.append({"where":"sources[20].title","before":old,"after":src[20]['title'],"why":"권·쪽 보강(PubMed)"})
# remove source 27 and renumber
used=set()
def refs(s):
    for m in re.finditer(r'\[([0-9,\s–\-]+)\]',s):
        for part in m.group(1).split(','):
            part=part.strip()
            if re.match(r'^\d+[–-]\d+$',part):
                a,b=re.split('[–-]',part); used.update(range(int(a),int(b)+1))
            elif part.isdigit(): used.add(int(part))
txt=json.dumps(d,ensure_ascii=False)
refs(txt)
for x in ['compounds','assays']:
    for c in d[x]:
        used.update(c.get('source',[]))
print('unused',[s['n'] for s in d['sources'] if s['n'] not in used])
d['sources']=[s for s in d['sources'] if s['n'] in used]
mp={s['n']:i+1 for i,s in enumerate(d['sources'])}
print(mp)
def sub(s):
    def f(m):
        out=[]
        for part in m.group(1).split(','):
            p=part.strip()
            mm=re.match(r'^(\d+)([–-])(\d+)$',p)
            if mm: out.append(f"{mp[int(mm.group(1))]}{mm.group(2)}{mp[int(mm.group(3))]}")
            else: out.append(str(mp[int(p)]))
        return '['+', '.join(out)+']'
    return re.sub(r'\[(\d+(?:[–-]\d+)?(?:,\s*\d+(?:[–-]\d+)?)*)\]',f,s)
for s in d['sections']: s['body']=sub(s['body'])
for x in ['compounds','assays']:
    for c in d[x]:
        for k,v in c.items():
            if isinstance(v,str): c[k]=sub(v)
        c['source']=[mp[n] for n in c['source']]
        if x=='assays': c['rationale']=sub(c['rationale'])
for s in d['sources']: s['n']=mp[s['n']]
json.dump(d,open(P,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('/home/user/hfoodguide-wave3/docs/materials/ixeris-dentata/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
