import json,re
p='/home/user/hfoodguide-wave3/docs/materials/micropogonias-furnieri/dossier.json'
d=json.load(open(p))
changes=[]
def rep(where,obj,key,old,new,why):
    assert old in obj[key],(where,old)
    obj[key]=obj[key].replace(old,new)
    changes.append({"where":where,"before":old,"after":new,"why":why})
S={s['key']:s for s in d['sections']}
rep('sections.history',S['history'],'body',
 "리우데자네이루주에서는 정어리·숭어와 함께 가장 많이 소비되는 상업 어종 세 가지에 든다[31].",
 "리우데자네이루주 과나바라만에서 많이 소비되는 어종으로 정어리·숭어와 함께 잔류 농약 조사 대상이 되었다[31].",
 "[31] 초록은 '많이 소비되는 어종(highly consumed fish)' 3종을 조사했다고만 쓰며, 가장 많이 소비되는 세 어종이라는 순위는 없음")
rep('sections.biology',S['biology'],'body',
 "우루과이 개체의 난소 조직은 시험관 실험에서 17,20β-디히드록시-4-프레그넨-3-온 등 난모세포 최종 성숙을 유도하는 스테로이드를 만들었다[13].",
 "우루과이 개체의 난소 조직을 방사성 프로게스테론과 배양한 시험관 실험에서, 다른 경골어류에서 난모세포 최종 성숙 유도 스테로이드로 알려진 17,20β-디히드록시-4-프레그넨-3-온·20β-S와 크로마토그래피 성질이 같은 대사물이 만들어졌고, 저자들은 이 종에서 20β-S가 성숙 유도 스테로이드로 작용한다고 추정했다[13].",
 "[13] 초록은 '크로마토그래피 성질이 같은' 유도체로 확인했고 성숙 유도 작용은 다른 경골어류 근거·추정이라 표현을 맞춤")
rep('sections.biology',S['biology'],'body',
 " IUCN 적색목록에서는 '관심대상(LC)'으로 평가되었다(원문 미확인, 검색 요약)[35].",
 " IUCN 적색목록 평가는 원문을 열지 못해 이번 조사에서 확인하지 못함.",
 "[35] IUCN 은 WebSearch 요약으로만 확인한 출처이고 이 환경에서 iucnredlist.org 가 허용 목록 밖이라 원문 대조 불가 — 문장과 출처 삭제")
rep('sections.processing',S['processing'],'body',
 "브라질 남부의 신선 대서양통꼬마민어 살에서는",
 "브라질의 신선 대서양통꼬마민어 살에서는",
 "[15] 초록에 시료 채취 지역(남부)이 나오지 않음(저자 소속만 남부)")
rep('sections.processing',S['processing'],'body',
 "뼈를 800 °C에서 구워 얻은 수산화인회석은 쥐 두개골 결손 실험에서 30일 뒤 염증이 사라지고 새 뼈가 생겼다(동물실험)[17].",
 "뼈를 800 °C에서 구워 얻은 수산화인회석을 쥐 두개골 결손에 넣은 실험에서는 30일 뒤 염증이 사라지고 재료가 줄며 새 뼈가 생겼으나, 대조 결손도 30일 안에 스스로 메워졌고 뼈 부피는 대조와 차이가 없었으며 7일째 조골세포 수는 오히려 적었다(동물실험)[17].",
 "[17] 전문(PMC8403112): 대조군도 30일 내 자가 수복, BV/TV 차이 없음, 7일째 N.Ob/T.Ar·Ob.S/BS 는 대조가 높음 — 새 뼈 형성을 재료 효과로 읽히지 않게 함")
rep('sections.genetics',S['genetics'],'body',
 "15종의 단백질 암호화 유전자로 최대우도 계통수를 만들었다[2].",
 "15종의 단백질 암호화 유전자 13개 서열로 최대우도 계통수를 만들었다[2].",
 "[2] 전문: 15종의 13개 PCG 서열로 계통수 작성 — '15종의 유전자'로 오독될 표현 수정")
rep('sections.safety',S['safety'],'body',
 "리우데자네이루 조사에서는 수은이 기준 아래였으나 아이가 먹을 때 위해지수가 1을 넘는 경우가 많았다[25].",
 "이 종을 포함한 리우데자네이루 수산물 조사에서는 수은 농도가 허용치 아래였으나 조사 종 대부분이 위해지수 1을 넘었고 특히 아이가 먹을 때 그러했으며, 이 종의 수은 농도는 계절에 따라 달랐다[25].",
 "[25] 초록의 HQ>1 은 조사 종 전체(most species)에 대한 진술 — 이 종 단독 결과로 읽히지 않게 함, 계절 영향은 이 종에 명시")
rep('sections.safety',S['safety'],'body',
 "다만 무기비소 비율을 5%로 가정하면 어민 집단의 위해지수가 1을 넘어 형태별 분석이 필요하다고 했다[26].",
 "다만 이 종과 Urophycis brasiliensis 근육 자료로 무기비소를 총비소의 5%로 가정하면 어민 집단의 총 위해지수가 1을 넘어 형태별 분석이 필요하다고 했다[26].",
 "[26] 은 두 종을 함께 평가 — 범위 명시")
rep('sections.safety',S['safety'],'body',
 "근육에서 Hysterothylacium 선충 유충이 나와 공중보건 우려가 제기되었고, Anisakis typica도 이 종에서 처음 기록되었다[32].",
 "리우데자네이루 연안 개체에서는 Cucullanus genypteri 선충(유병률 98.3%)과 Hysterothylacium deardorffoverstreetorum(3.3%)이 나왔다[32]. 저자들은 이 종을 Anisakis typica의 새 숙주로 적었으나 같은 초록의 종별 목록에는 A. typica가 다른 어종에서만 나와 있어 확인이 필요하다[32]. 조사한 3종에서 근육 속 Hysterothylacium 유충 6개체가 나와 공중보건 우려가 제기되었으나, 어느 어종의 근육인지는 초록에 나오지 않는다[32].",
 "[32] 초록: 근육 Hysterothylacium 은 3종 통틀어 6개체로 종 미지정, 이 종의 기생 선충은 C. genypteri·H. deardorffoverstreetorum, A. typica 기록은 초록 내 서술이 엇갈림")
C={c['name']:c for c in d['compounds']}
rep('compounds.Hydroxyapatite.activity_ko',C['Hydroxyapatite'],'activity_ko',
 "쥐 두개골 결손 30일 뒤 새 뼈 형성(동물실험)[17]",
 "쥐 두개골 결손 30일 뒤 염증 소실·새 뼈 형성, 단 뼈 부피는 자가 수복한 대조와 차이 없음(동물실험)[17]",
 "[17] 전문 대조 — 대조군도 30일 내 수복")
rep('compounds.Mercury.activity_ko',C['Mercury'],'activity_ko',
 "아이 섭취 시 위해지수 1 초과 사례 많음[25]",
 "조사 수산물 대부분이 위해지수 1 초과, 특히 아이 섭취 시(이 종 포함 여러 종 통틀어)[25]",
 "[25] HQ 진술은 여러 종 통틀어")
# sources
for s in d['sources']:
    if s['n']==16:
        old=s['title']; s['title']=old.replace("전문 텍스트에서 학명 표기가 빠져 있어 종 귀속은 PubMed 'Micropogonias furnieri' 색인에 근거","전문 추출본에는 이탤릭 학명이 빠져 '껍질 of ( )'처럼 비어 있으나, PubMed 초록 필드 검색 \"Micropogonias furnieri\"[Title/Abstract] 에 이 PMID 가 걸려 원문 초록의 학명이 M. furnieri 임을 확인; 같은 연구 집단(산투스)의 [17] 도 이 종 뼈를 씀")
        changes.append({"where":"sources[16].title","before":old,"after":s['title'],"why":"종 귀속 근거 재확인"})
    if s['n']==18:
        old=s['title']; s['title']=old.replace("전문 텍스트에서 학명 표기가 빠져 있어 종 귀속은 PubMed 'Micropogonias furnieri' 색인에 근거","전문 추출본에는 이탤릭 학명이 빠져 있으나, PubMed 초록 필드 검색 \"Micropogonias furnieri\"[Title/Abstract] 에 이 PMID 가 걸려 원문 초록의 'croaker fish bones ( )' 학명이 M. furnieri 임을 확인; 시료는 산투스 수산시장 구입")
        changes.append({"where":"sources[18].title","before":old,"after":s['title'],"why":"종 귀속 근거 재확인"})
# remove source 35, renumber
d['sources']=[s for s in d['sources'] if s['n']!=35]
mp={}
for i,s in enumerate(d['sources'],1):
    mp[s['n']]=i; s['n']=i
def renum(txt):
    def f(m):
        nums=[int(x) for x in re.split(r',\s*',m.group(1))]
        return '['+', '.join(str(mp[x]) for x in nums)+']'
    return re.sub(r'\[(\d+(?:,\s*\d+)*)\]',f,txt)
def walk(o):
    if isinstance(o,dict):
        for k,v in o.items():
            if k=='source' and isinstance(v,list): o[k]=[mp[x] for x in v]
            elif k=='source' and isinstance(v,int): o[k]=mp[v]
            else: o[k]=walk(v)
        return o
    if isinstance(o,list): return [walk(x) for x in o]
    if isinstance(o,str): return renum(o)
    return o
srcs=d.pop('sources'); d=walk(d); d['sources']=srcs
changes.append({"where":"sources","before":"[35] IUCN(검색 요약), [36]–[39]","after":"[35] 삭제, [36]–[39] → [35]–[38]","why":"WebSearch 요약만 있는 출처 제거 후 번호 정리"})
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('/home/user/hfoodguide-wave3/docs/materials/micropogonias-furnieri/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
