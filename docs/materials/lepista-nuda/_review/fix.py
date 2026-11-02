import json,re
P='/home/user/hfoodguide-wave3/docs/materials/lepista-nuda/dossier.json'
d=json.load(open(P))
changes=[]
def sec(k): return next(s for s in d['sections'] if s['key']==k)
def rep(where,obj,key,old,new,why):
    assert old in obj[key], (where,old)
    obj[key]=obj[key].replace(old,new); changes.append({"where":where,"before":old,"after":new,"why":why})

# aliases / name_en
d['aliases']=[a for a in d['aliases'] if a!='wood blewit']
changes.append({"where":"aliases","before":"wood blewit","after":"(삭제)","why":"출처([6]·[8])는 blewit(s)만 씀 — 출처 없는 별명"})
d['name_en']='Blewit'; changes.append({"where":"name_en","before":"Wood blewit","after":"Blewit","why":"[8] 'commonly known as blewit', [6] 'blewits'"})

h=sec('history')
rep('sections.history',h,'body','유럽에서는 오래전부터 야생에서 채취해 먹는 버섯으로, 포르투갈·스페인·폴란드·튀르키예 등의 야생 식용버섯 조사에 빠짐없이 포함된다[7, 23, 28, 29].',
 '포르투갈·스페인·폴란드·튀르키예의 야생 버섯 성분·원소 조사에 이 종이 포함되었다[7, 23, 28, 29].',
 "출처들은 각국 조사에 포함됐다는 것만 보임 — '오래전부터'·'빠짐없이'는 근거 없음")
rep('sections.history',h,'body','튀김·국물 요리에 널리 쓰이며','기름에 조리한 요리(fried dishes)와 국물 요리에 널리 쓰이며',"[4] 원문은 'fried dishes and soups' — 튀김으로 한정하지 않음")
rep('sections.history',h,'body',' 국내에서는 한국버섯학회지에 국내외 균주의 교배 그룹을 나누고 인공재배용 품종을 육성하려는 연구가 실렸다(검색 요약으로만 확인)[34].',
 ' 국내 교배·재배 연구가 한국버섯학회지에 실린 것으로 검색되나 원문을 열지 못해 내용은 확인하지 못함.',
 "[34]는 WebSearch 요약뿐이고 원문 사이트가 허용 목록 밖 — 두 논문(교배군 연구·우량계통 선발 연구)을 한 출처로 묶었음. 출처 삭제")

b=sec('biology')
rep('sections.biology',b,'body',' 국내에서는 늦가을부터 초겨울에 혼합림의 습한 그늘에서 나는 저온성 버섯으로 소개되었다(검색 요약으로만 확인)[34].',
 ' 국내 발생 시기·생태에 대한 원문 자료는 확인하지 못함.',"[34] 검색 요약 출처 — 원문 확인 불가, 이번 검색 요약에도 이 내용 없음")
rep('sections.biology',b,'body',"구리 이온이 없는 분자량 56 kDa의 '흰색 락카아제'","제1형 구리(type I copper)가 없는 분자량 56 kDa의 '흰색 락카아제'","[14] 초록은 'without type I copper' — 구리 이온 전체가 없다는 뜻이 아님(오히려 Cu2+ 1.5 mM이 생산을 늘림)")

c=sec('cultivation')
rep('sections.cultivation',c,'body','바크 퇴비와 쌀겨를 10:2로','바크 퇴비와 겨(bran)를 10:2로',"[4] 원문은 'bran'만 씀 — 쌀겨로 특정할 근거 없음")
rep('sections.cultivation',c,'body','국내 연구에서는 볏짚 발효배지 상자 재배로 교배 모본을 고르고, 온도 14 ℃·상대습도 95% 이상·밤 6 ℃ 저온 자극으로 발생을 유도해 자실체가 나오기까지의 기간을 대조 100일에서 45일까지 줄였다고 한다(검색 요약으로만 확인)[34]. ',
 '국내에서도 볏짚 발효배지 상자 재배와 교배 육종 연구가 있는 것으로 검색되나, 원문을 열지 못해 재배 조건·기간 수치는 확인하지 못함. ',
 "[34] 검색 요약만으로 수치를 적음 — 원문 확인 불가. URL(JAKO201307954512221)은 교배군 연구이고 재배 수치는 다른 논문(우량계통 선발)의 것이라 출처도 어긋남")

p=sec('processing')
rep('sections.processing',p,'body','후쿠시마 연구는 이 버섯이 튀김과 국물 요리에 널리 쓰인다고 적었다[4].','후쿠시마 연구는 이 버섯이 기름에 조리한 요리(fried dishes)와 국물 요리에 널리 쓰인다고 적었다[4].',"[4] 'fried dishes and soups'")
rep('sections.processing',p,'body','생 버섯과 냉동·통조림 가공품을 비교한 스페인 연구에서 냉동은 항산화 활성이 조금 줄었지만 생것과 유의한 차이가 없었고, 통조림은 항산화 활성이 줄었다[31].',
 '이 버섯을 포함한 트러플·버섯 7종의 생것과 냉동·통조림 가공품을 비교한 스페인 연구에서, 냉동은 라디칼 소거 활성이 조금 줄었지만 생것과 유의한 차이가 없었고 통조림은 항산화 활성을 일부 잃었다(초록은 7종을 묶어 서술해 이 종만의 결과는 확인하지 못함)[31]. 생것의 트롤록스 환산 항산화 능력 순위에서 이 종은 7종 가운데 여섯 번째였다[31].',
 "[31] 초록의 냉동·통조림 결과는 7종 전체에 대한 서술 — 종별 결과처럼 쓰지 않게 고침, 이 종 순위(Lepista 6위) 추가")
rep('sections.processing',p,'body','균주에서 얻은 락카아제는','균주 LN07에서 얻은 락카아제는','[14] 균주명 명시')

# compounds
for cpd in d['compounds']:
    if cpd['name'] in ('Catechin','Ellagic acid','Chlorogenic acid'):
        old=cpd['activity_ko']; cpd['activity_ko']='단일 성분 활성은 이 논문에서 시험하지 않음 — 메탄올 추출물의 항산화 활성을 페놀 함량과 연관 지어 논의함(시험관)[6]'
        changes.append({"where":f"compounds.{cpd['name']}.activity_ko","before":old,"after":cpd['activity_ko'],"why":"[6]은 추출물만 시험 — 개별 성분 항산화로 쓰면 과장"})
    if cpd['name']=='4-Hydroxybenzoic acid':
        cpd['activity_ko']='단일 성분 활성은 이 논문에서 시험하지 않음 — 메탄올 추출물의 항산화 활성과 연관 지어 논의됨(시험관)[6]'
a=d['assays'][0]
a['conditions']['column']='Acclaim 120 역상 C18(3 µm, 150 × 4.6 mm)'
old=a['rationale']
a['rationale']=("이 종 자실체에서 정량된 페놀 화합물 가운데 가장 많은 성분이다. PMC 전문 텍스트에서 학명이 빠져 있어 종 귀속을 따로 대조했다: 제목의 종 순서(Paralepista flaccida (Sowerby) Vizzini, Lepista nuda (Bull.) Cooke)와 초록·본문의 'respectively', 서론의 L. nuda 단락(blewits, 프랑스·네덜란드·영국·대만 재배), 그리고 두 번째 종의 총페놀 25.52 mg을 이전 모로코 L. nuda 연구값과 비교한 서술이 서로 맞아 587.90 µg/g·카테킨 400.20 µg/g 등은 L. nuda 값으로 판단했다. 함께 분석된 Paralepista flaccida(옛 Lepista flaccida·L. inversa)의 값(p-하이드록시벤조산 138.50 µg/g 등)과 섞지 않는다. 기울기·유속·주입량은 저자들의 이전 논문을 따랐다고만 적혀 있어 확인하지 못함.")
changes.append({"where":"assays[0].rationale","before":old[:60]+'…',"after":a['rationale'][:80]+'…',"why":"모로코 논문 [6] 종 귀속 근거 보강, 함께 분석된 Paralepista flaccida(옛 Lepista 속) 혼입 주의 명시, 상표 기호 제거"})

# drop source 34 and renumber
src=[s for s in d['sources'] if s['n']!=34]
mp={}
for i,s in enumerate(src,1): mp[s['n']]=i; s['n']=i
d['sources']=src
def renum(text):
    def f(m):
        inner=m.group(1)
        parts=[]
        for tok in re.split(r',\s*',inner):
            if '–' in tok:
                x,y=tok.split('–'); parts.append(f"{mp[int(x)]}–{mp[int(y)]}")
            else: parts.append(str(mp[int(tok)]))
        return '['+', '.join(parts)+']'
    return re.sub(r'\[(\d+(?:[–,]\s*\d+)*(?:,\s*\d+(?:–\d+)?)*)\]',f,text)
def walk(o):
    if isinstance(o,dict):
        for k,v in o.items():
            if k=='source' and isinstance(v,list): o[k]=[mp[x] for x in v]
            elif isinstance(v,str): o[k]=renum(v)
            else: walk(v)
    elif isinstance(o,list):
        for i,v in enumerate(o):
            if isinstance(v,str): o[i]=renum(v)
            else: walk(v)
for k in ('sections','compounds','assays'): walk(d[k])
assert '[34]' not in json.dumps(d['sections'],ensure_ascii=False) or True
json.dump(d,open(P,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('/home/user/hfoodguide-wave3/docs/materials/lepista-nuda/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
