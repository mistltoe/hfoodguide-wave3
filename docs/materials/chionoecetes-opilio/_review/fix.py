import json,re
from pathlib import Path
P=Path(__file__).resolve().parent.parent/'dossier.json'
d=json.load(open(P))
S={s['key']:s for s in d['sections']}
changes=[]
def rep(key,old,new,why):
    b=S[key]['body']; assert old in b,(key,old[:30]); S[key]['body']=b.replace(old,new)
    changes.append({"where":f"sections.{key}","before":old,"after":new,"why":why})

rep('overview',"대게(Chionoecetes opilio, 영어 snow crab·queen crab)는 Oregoniidae과에 드는 단미류 게로, 식약처",
 "대게(Chionoecetes opilio, 영어 snow crab·queen crab)는 Oregoniidae과에 드는 단미류 게로[17], 식약처",
 "과 소속은 [1] 원자료에 없음 — 미토콘드리아 유전체 논문[17] 제목·분류로 근거 보강")
rep('overview',"'어린자실체'(대게껍질)로 적혀 있는데, 게에 맞지 않는 식물·버섯 부위 용어여서 원자료 입력상의 오류로 보이며 의도한 부위는 확인하지 못함.",
 "'어린자실체'(대게껍질)로 적혀 있다[1]. 같은 목록의 다른 수산물 행에도 알에는 '균핵', 내장에는 '어린순', 살에는 '죽순', 껍질에는 '어린자실체'가 같은 방식으로 붙어 있다(예: 홍게살 '죽순', 홍게내장 '어린순')[1].",
 "원자료 I1020 확인: 수산물 행 가운데 '균핵' 50행(…알), '어린순' 49행(…내장), '죽순' 92행(…살), '어린자실체' 24행(…껍질)에 같은 부위어가 붙어 있음 — '입력 오류'로 단정하지 않고 원자료 표기 그대로라는 사실 서술로 낮춤")
rep('related_species',"국내 시판 게맛살 가운데 '게살 함유' 제품에 들어간 게살은 대게가 아니라 홍게 다리살(6%)이었다[10].",
 "이 연구가 부산에서 구입해 비교한 고급 게맛살 가운데 게살을 넣은 제품은 대게가 아니라 홍게 다리살을 썼다(제조사 표기 6%)[10].",
 "[10] 전문: 시판 제품 1종(PS-RC)의 제조사 표기값 — 국내 시판품 일반으로 넓히지 않도록 범위 한정")
rep('related_species',"왕게에는 대게 등 참게류에는 없는 왕게 특이 알레르기 항원(말산 탈수소효소, Para c 11)이 있어 두 무리의 알레르기 양상이 다를 수 있다[4].",
 "왕게(이각하목 Anomura)에는 대게를 포함한 단미류(진짜 게, Brachyura) 5종에서는 IgE 반응이 보이지 않은 왕게 특이 알레르기 항원(말산 탈수소효소, Para c 11)이 있어 두 무리의 알레르기 양상이 다를 수 있다[4].",
 "[4] 전문은 'true crabs(Brachyura)'와 비교 — '참게류'는 다른 무리(참게 Eriocheir)를 가리키는 말이라 잘못된 용어")
rep('processing',"간췌장 가수분해물의 펩타이드 분획은 시험관에서 리스테리아 등 세균 증식을 억제했지만[26], 이는 실험실 결과로 사람에게서 확인된 효과가 아니다[26, 27].",
 "여러 부위 가수분해물 가운데 간췌장 분획만 시험관에서 리스테리아(Listeria innocua) 증식을 억제(정균)했고[26], 부산물 효소 분해 펩타이드 분획도 시험관에서 비브리오·리스테리아 등 여러 세균을 억제했다[27]. 이는 실험실 결과로 사람에게서 확인된 효과가 아니며, 연구진도 식품 보존제 후보로만 제안했다[26].",
 "[26] 초록: 정균 활성은 L. innocua 에만 확인('리스테리아 등'은 과장) — [27] 초록 내용(여러 세균 억제)을 따로 밝힘")
rep('safety',"동해산 대게의 카드뮴·코발트·구리·철·납은 간췌장이 근육보다 10–100배 높았으나, 근육 섭취 기준 추정 일일섭취량은 모두 잠정 허용 섭취량의 0.1% 미만이었고, 대게의 하루 최대 허용 섭취량은 약 410 g으로 추산되었다[7].",
 "동해산 대게·홍게를 함께 본 연구에서 두 종의 카드뮴·코발트·구리·철·납 평균은 간췌장이 근육보다 10–100배 높았으나, 근육 섭취 기준 추정 일일섭취량은 모두 잠정 허용 섭취량의 0.1% 미만이었고, 하루 최대 허용 섭취량은 대게 약 410 g(홍게 약 240 g)으로 추산되었다[7].",
 "[7] 초록: 간췌장/근육 10–100배와 EDI<0.1%는 Chionoecetes 두 종을 합친 결과 — 대게 단독 수치처럼 쓴 것을 바로잡음(홍게 자료 섞임 방지)")
rep('safety',"1996–2007년 일본 주변 대게의 세슘-137 등 인공 방사성 핵종은 증가 추세가 없었고 과거 핵실험 낙진에서 온 것으로 해석되었다[8].",
 "1996–2007년 일본 주변에서 잡은 대게와 홍게(C. japonicus)의 세슘-137 등 인공 방사성 핵종은 증가 추세가 없었고 과거 핵실험 낙진에서 온 것으로 해석되었다[8].",
 "[8] 은 두 종을 함께 측정 — 대게 단독 결과처럼 쓰지 않도록 밝힘")
rep('cultivation',"국내 법령은 「수산자원관리법 시행령」 별표 2에서 대게의 포획·채취 금지 체장을 9 cm 이하로 정하고 있다고 검색 요약에서 확인했으나, 원문은 열지 못했다[30]. 금어기·암컷 포획 금지 등 세부 규정의 원문과 국내 연도별 어획량은 확인하지 못함.",
 "국내 법령(「수산자원관리법 시행령」)의 대게 포획 금지 체장·금어기·암컷 포획 금지 등 세부 규정은 원문을 열지 못해 확인하지 못함. 국내 연도별 어획량도 확인하지 못함.",
 "[30] 은 WebSearch 검색 요약만으로 확인한 것이고 법령 원문(law.go.kr)은 이 환경에서 열 수 없어 대조 불가 — 수치 문장과 출처 삭제")
# compounds
for c in d['compounds']:
    if c['name']=='Astaxanthin':
        o=c['activity_ko']; c['activity_ko']="게 껍질의 붉은 색을 내는 주 색소로, 등딱지에서는 주로 다이에스터·모노에스터 형태이고 다른 껍질 부위에서는 에스터가 총 카로티노이드의 4분의 1에 못 미쳤다[11]. 항산화 성분으로 알려져 부산물 회수 대상이 된다[11, 12]."
        changes.append({"where":"compounds.Astaxanthin.activity_ko","before":o,"after":c['activity_ko'],"why":"[11] 전문: 에스터 우세는 등딱지(와 새우 껍질)에 한함, 다른 부위는 에스터 < 1/4"})
# sources: drop 30, renumber
src=[s for s in d['sources'] if s['n']!=30]
fix={17:("Mitochondrial DNA B Resour 2020;5(3):2596-7","Mitochondrial DNA B Resour 2020;5(3):2550-2"),
     19:("Sci Rep 2023;13:7197","Sci Rep 2023;13:7204"),
     25:("J Sci Food Agric 2019","J Sci Food Agric 2020;100(1):384-93"),
     26:("Probiotics Antimicrob Proteins 2019","Probiotics Antimicrob Proteins 2019;11(3):1023-33")}
for s in src:
    if s['n'] in fix:
        a,b=fix[s['n']]; assert a in s['title']; s['title']=s['title'].replace(a,b)
        changes.append({"where":f"sources[{s['n']}].title","before":a,"after":b,"why":"PubMed 서지(쪽·논문번호·권호)와 대조해 바로잡음"})
m={31:30,32:31}
for s in src:
    s['n']=m.get(s['n'],s['n'])
d['sources']=src
def renum(txt):
    def f(mo):
        nums=[int(x) for x in re.split(r',\s*',mo.group(1))]
        assert 30 not in nums
        return '['+', '.join(str(m.get(n,n)) for n in nums)+']'
    return re.sub(r'\[(\d+(?:,\s*\d+)*)\]',f,txt)
def walk(o):
    if isinstance(o,dict):
        for k,v in o.items():
            if k=='source' and isinstance(v,list): o[k]=[m.get(n,n) for n in v]
            else: o[k]=walk(v)
        return o
    if isinstance(o,list): return [walk(x) for x in o]
    if isinstance(o,str): return renum(o)
    return o
srcs=d.pop('sources'); d=walk(d); d['sources']=srcs
json.dump(d,open(P,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open(P.parent/'_review'/'changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
