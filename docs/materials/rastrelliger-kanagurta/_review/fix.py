import json,re
P='/home/user/hfoodguide-wave3/docs/materials/rastrelliger-kanagurta/dossier.json'
d=json.load(open(P))
S={s['key']:s for s in d['sections']}
ch=[]
def rep(obj,key,old,new,why,where):
    v=obj[key]; assert old in v,(where,old); obj[key]=v.replace(old,new); ch.append({"where":where,"before":old,"after":new,"why":why})
rep(S['biology'],'body',"벵골만 비사카파트남 개체에서는 기생충 15종이 나왔고, 대부분 이 종에만 붙는 전문 기생충이어서 플랑크톤 식성을 반영한다고 해석되었다[9].",
 "벵골만 비사카파트남 개체에서는 기생충 15종이 나왔고 2종을 뺀 나머지는 이 종에만 붙는 전문 기생충이었으며, 기생충상 전체는 플랑크톤 식성을 반영한다고 해석되었다[9].",
 "[9] 초록: 숙주 특이성과 플랑크톤 식성 반영은 별개 서술(인과 연결 아님), 예외 2종 명시","sections.biology")
rep(S['related_species'],'body',"줄무늬고등어속에는 줄무늬고등어(R. kanagurta), 짧은고등어(R. brachysoma), 섬고등어(R. faughni) 세 종이 있다[2].",
 "줄무늬고등어속에는 줄무늬고등어(R. kanagurta)와 R. brachysoma(영명 short mackerel), R. faughni(영명 island mackerel) 세 종이 있다[2].",
 "'짧은고등어'·'섬고등어' 국문명은 식약처 목록·출처 어디에도 없음 — 출처 [2]의 영명으로 바꿈","sections.related_species")
rep(S['related_species'],'body'," 베트남 히스타민 연구처럼 'sp.'로만 적힌 자료는 속 수준 자료로만 다루었다[23]."," 'sp.'로만 적혀 종을 확정할 수 없는 자료(예: 베트남 히스타민 연구)는 이 문서에 넣지 않았다.",
 "지시: 히스타민은 이 종 자료로만 — 종 미확정(Rastrelliger sp.) 출처 [23] 제외","sections.related_species")
rep(S['cultivation'],'body',"짧은고등어와 줄무늬고등어가","R. brachysoma와 줄무늬고등어가","출처 없는 국문명 '짧은고등어' 제거","sections.cultivation")
rep(S['genetics'],'body',"짧은고등어와 줄무늬고등어의 유전체 크기","R. brachysoma와 줄무늬고등어의 유전체 크기","출처 없는 국문명 제거","sections.genetics")
rep(S['genetics'],'body',"짧은고등어(8.30%)","R. brachysoma(8.30%)","출처 없는 국문명 제거","sections.genetics")
rep(S['safety'],'body'," 베트남에서 2024년 고등어과 생선으로 인한 히스타민 식중독 4건(입원 400명 이상)이 있었고, 시장의 구운 줄무늬고등어속 생선은 최고 319 mg/kg으로 1만 회 섭취당 3–6건의 위험이 추정되었다[23].",
 " 인도 연안 조사에서는 바실루스(Bacillus)균이 이 생선에서 히스타민을 더 많이 만들었고[25], −18 °C 냉동 저장에서는 송풍 냉동 시료가 판냉동 시료보다 히스타민이 유의하게 더 생겼다[24].",
 "[23]은 학명이 'sp.'로만 남아 종 미확정 — 지시(히스타민은 이 종 자료로만)에 따라 삭제. 또한 319 mg/kg 은 '시장'이 아닌 슈퍼마켓 구운 제품 값이었음. 같은 문단을 이 종 자료([25]·[24])로 채움","sections.safety")
rep(S['safety'],'body'," 인도 연안 조사에서는 바실루스(Bacillus)균이 이 생선에서 히스타민을 더 많이 만들었다[25]. 태국"," 태국","[25] 문장을 히스타민 문단으로 옮김(중복 제거)","sections.safety")
C={c['name']:c for c in d['compounds']}
h=C['Histamine']; old=h['content_text']; h['content_text']="갓 잡은 살에서 검출되지 않음, 0–23 °C 저장 중 모두 유의하게 증가(23 °C에서 가장 두드러짐)[17]"; h['source']=[17]; h['activity_ko']="고등어형(스콤브로이드) 식중독에 관여하는 물질로 저장 온도가 높을수록 두드러지게 늘었다[17]"
ch.append({"where":"compounds.Histamine","before":old,"after":h['content_text'],"why":"[23] 종 미확정(sp.) 자료 제거; 319 mg/kg 은 슈퍼마켓 구운 제품이었음"})
c=C['Calcium']; old=c['activity_ko']; c['activity_ko']="필수 무기질로 함께 정량되었고, 연구진은 시료 무게의 상당 부분이 뼈라고 설명했다(칼륨-40 값 해석에서)[14]"
ch.append({"where":"compounds.Calcium.activity_ko","before":old,"after":c['activity_ko'],"why":"[14] 원문의 '뼈가 시료 무게에 기여' 설명은 칼륨(K-40) 해석이며 칼슘 설명이 아님"})
c=C['Selenium']; old=c['content_text']; c['content_text']="말라카 해협 지점 평균 0.035–0.0938 mg/kg(어체 건조 분말, 건중량)[14]; 인도 하이데라바드 시판품 0.01 mg/kg(초록, 생/건 기준 미기재)[32]"
ch.append({"where":"compounds.Selenium.content_text","before":old,"after":c['content_text'],"why":"[32] 값은 다른 시료·기준(초록에 생/건 미기재) — 건조 분말 값과 기준 구분"})
c=C['Parvalbumin']; old=c['content_text']; c['content_text']=old.replace("다른 고등어류 파브알부민과","다른 고등어류 2종의 파브알부민과"); ch.append({"where":"compounds.Parvalbumin.content_text","before":old,"after":c['content_text'],"why":"[19] 초록: '2 other mackerel species'"})
A=d['assays']
a=A[0]['conditions']; ch.append({"where":"assays[0].conditions.detection","before":a['detection'],"after":"","why":"원문에 없는 칸은 지움(V2 규칙)"}); a['detection']=""
a=A[2]['conditions']; ch.append({"where":"assays[2].conditions.gradient","before":a['gradient'],"after":"","why":"원문에 없는 칸은 지움"}); a['gradient']=""
ch.append({"where":"assays[2].conditions.detection","before":a['detection'],"after":"다이오드 배열 검출기(DAD)","why":"원문에 있는 것만 남김"}); a['detection']="다이오드 배열 검출기(DAD)"
# drop source 23 and renumber
used=set()
txt=json.dumps({k:v for k,v in d.items() if k!='sources'},ensure_ascii=False)
for m in re.finditer(r'\[([\d,\s]+)\]',txt):
    for x in m.group(1).split(','):
        x=x.strip()
        if x: used.add(int(x))
def walk(o):
    if isinstance(o,dict):
        for k,v in o.items():
            if k=='source' and isinstance(v,list): used.update(v)
            else: walk(v)
    elif isinstance(o,list):
        for v in o: walk(v)
walk({k:v for k,v in d.items() if k!='sources'})
print('unused',[s['n'] for s in d['sources'] if s['n'] not in used])
keep=[s for s in d['sources'] if s['n'] in used]
mp={s['n']:i+1 for i,s in enumerate(keep)}
def rn(s):
    return re.sub(r'\[([\d,\s]+)\]',lambda m:'['+', '.join(str(mp[int(x)]) for x in m.group(1).split(',') if x.strip())+']',s)
def walk2(o):
    if isinstance(o,dict):
        for k in list(o):
            v=o[k]
            if k=='source' and isinstance(v,list): o[k]=[mp[x] for x in v]
            elif isinstance(v,str): o[k]=rn(v)
            else: walk2(v)
    elif isinstance(o,list):
        for i,v in enumerate(o):
            if isinstance(v,str): o[i]=rn(v)
            else: walk2(v)
for k in d:
    if k!='sources': walk2(d[k])
for s in keep: s['n']=mp[s['n']]
d['sources']=keep
json.dump(d,open(P,'w'),ensure_ascii=False,indent=1)
json.dump(ch,open(P.replace('dossier.json','_review/changes.json'),'w'),ensure_ascii=False,indent=1)
print(len(ch))
