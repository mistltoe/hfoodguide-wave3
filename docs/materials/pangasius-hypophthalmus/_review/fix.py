import json,re
from pathlib import Path
P=Path(__file__).resolve().parent.parent/'dossier.json'
d=json.load(open(P))
changes=[]
def sec(k): return next(s for s in d['sections'] if s['key']==k)
def rep(where,obj,key,old,new,why):
    assert old in obj[key],(where,old)
    obj[key]=obj[key].replace(old,new); changes.append({"where":where,"before":old,"after":new,"why":why})
# sections
rep("sections.processing",sec('processing'),'body'," 언론 보도로는 피부 보습 등 피부 건강 기능성으로 인정받았다[31].","","[31]은 기사 본문을 열지 않고 검색 요약만 본 업체 발표 보도라 근거가 약하고, 인정 기능성 원문(식약처)을 이 환경에서 확인하지 못해 삭제")
rep("sections.processing",sec('processing'),'body',"1 kDa 미만 효소 분해 분획은 ACE 저해 활성을 보였다[27]","1 kDa 미만 효소 분해 분획은 시험관에서 ACE 저해 활성을 보였다[27]","[27]은 시험관(in vitro) 결과임을 명시")
rep("sections.biology",sec('biology'),'body',"다만 수출용 필레는 지방이 1.1–3.0%로","다만 이탈리아에 유통된 베트남산 필레는 지방이 1.1–3.0%로","[7]은 이탈리아 시장 유통 필레를 분석")
rep("sections.safety",sec('safety'),'body',"브라질 유통 필레 40점 중 5점에서 항균제가 나왔다[9].","브라질 유통 베트남산 필레 40점 중 5점에서 엔로플록사신이 낮은 농도로 나왔다[9].","[9] 초록: 검출 성분은 엔로플록사신")
rep("sections.safety",sec('safety'),'body',"인도 유통 시료의 농약 잔류는 허용 섭취량보다 낮았다[12].","인도에서 국내산·베트남 수입산 148점을 조사한 결과 일부 농약이 검출됐지만 섭취 노출량은 최대 허용 섭취량보다 낮았다[12].","[12] 초록: 148점, 38%에서 농약 검출, 노출량은 허용치 미만")
# compounds
C={c['name']:c for c in d['compounds']}
for old,new,why in [("Palmitic acid","Saturated fatty acids","[7]은 팔미트산이 아니라 포화지방산 총량(41.1–47.8%)만 보고; name_ko와 맞춤"),
                    ("Hydroxyproline","Imino acids (proline + hydroxyproline)","[28]의 17.37 g/100 g은 이미노산(프롤린+하이드록시프롤린) 합계; name_ko와 맞춤"),
                    ("Sodium tripolyphosphate","Polyphosphates (pyrophosphate + tripolyphosphate)","[4]는 피로인산염+삼인산염 합계로 측정")]:
    C[old]['name']=new; changes.append({"where":f"compounds[{old}].name","before":old,"after":new,"why":why})
c=C["Collagen tripeptide"]
o=c['activity_ko']; c['activity_ko']="1일 1,000 mg 12주 섭취 시 피부 수분·탄력 개선(광노화 피부 여성 대상 무작위 대조 시험, 78명 완료; 비타민 C 등이 든 음료 형태)[25]"
changes.append({"where":"compounds[Collagen tripeptide].activity_ko","before":o,"after":c['activity_ko'],"why":"[25] 전문: 대상은 35–60세 여성, 시험 음료에 비타민 C 0.2%·과일 농축액 함유"})
# assay 4
a=d['assays'][3]; o=a['content']; a['content']="브라질 유통 베트남산 필레 40점 중 5점에서 엔로플록사신 저농도 검출(수치는 초록에 없음) [9]"
changes.append({"where":"assays[3].content","before":o,"after":a['content'],"why":"[9] 초록: 검출 성분은 엔로플록사신"})
# sources citation fixes
S={s['n']:s for s in d['sources']}
fx={4:("Food Sci Nutr 2016;4(4)","Food Sci Nutr 2016;4(3):398-408"),
    5:("Chemosphere 2018;196:9-14","Chemosphere 2018;196:53-57"),
    6:("2012;29(8)","2012;29(7):1046-51"),
    8:("J Sci Food Agric 2015;95(13)","J Sci Food Agric 2016;96(4):1373-9"),
    20:("2014;49(1)","2014;49(2):187-92"),
    21:("J Food Sci Technol 2020;57(3)","J Food Sci Technol 2020;57(4):1320-1330"),
    28:("J Food Sci Technol 2014;51(10)","J Food Sci Technol 2014;51(11):3104-13")}
for n,(o,nw) in fx.items():
    assert o in S[n]['title'],n
    S[n]['title']=S[n]['title'].replace(o,nw); changes.append({"where":f"sources[{n}].title","before":o,"after":nw,"why":"PubMed 서지(권·호·쪽) 불일치"})
# remove source 31 and renumber
used=set()
def refs(x):
    if isinstance(x,dict):
        for k,v in x.items():
            if k=='source' and isinstance(v,list): used.update(v)
            else: refs(v)
    elif isinstance(x,list):
        for v in x: refs(v)
    elif isinstance(x,str):
        for m in re.finditer(r'\[([\d,\s–-]+)\]',x):
            for t in re.split(r',\s*',m.group(1)):
                if t.strip().isdigit(): used.add(int(t))
refs({k:v for k,v in d.items() if k!='sources'})
assert 31 not in used
old=[s['n'] for s in d['sources'] if s['n'] in used]
mp={o:i+1 for i,o in enumerate(old)}
def remap(x):
    if isinstance(x,dict):
        return {k:([mp[i] for i in v] if k=='source' and isinstance(v,list) else remap(v)) for k,v in x.items()}
    if isinstance(x,list): return [remap(v) for v in x]
    if isinstance(x,str):
        def f(m):
            parts=re.split(r'(,\s*)',m.group(1))
            return '['+''.join(str(mp[int(p)]) if p.strip().isdigit() else p for p in parts)+']'
        return re.sub(r'\[(\d+(?:,\s*\d+)*)\]',f,x)
    return x
srcs=[dict(s,n=mp[s['n']]) for s in d['sources'] if s['n'] in used]
d={k:(remap(v) if k!='sources' else v) for k,v in d.items()}
d['sources']=srcs
json.dump(d,open(P,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open(Path(__file__).parent/'changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes),mp)
