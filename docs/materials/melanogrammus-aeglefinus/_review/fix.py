import json,re,sys
p='dossier.json'; d=json.load(open(p))
changes=[]
def sec(k): return next(s for s in d['sections'] if s['key']==k)
def rep(k,old,new,why):
    s=sec(k); assert old in s['body'],(k,old); s['body']=s['body'].replace(old,new)
    changes.append({"where":f"sections.{k}","before":old,"after":new,"why":why})
rep('overview','살은 지방이 적은 흰살생선으로, 노르웨이에서 산 필레의 지방은 0.7 g/100 g이었다[5]. 영국 소매점에서 산 해산물 95종 가운데 요오드 평균값이 가장 높은 종이기도 했다[4].',
 '살은 지방이 적은 흰살생선(대구목)에 속하며, 영국 소매점에서 산 해산물 95종 가운데 요오드 평균값이 가장 높은 종이었다[4].',
 '[5]의 필레 지방 0.7 g/100 g은 원문 표에만 있고 PMC 본문 텍스트에 없어 대조할 수 없음 — 수치 삭제, [4] 본문(흰살생선·대구목 상위 8종)으로 대체')
rep('history','노르웨이에서는 해덕대구 같은 흰살생선을 갈아 만든 생선 케이크가 전통적으로 쓰여 왔고, 해덕대구 100% 케이크는 시판 제품에 해당하는 대조군으로 쓰였다[5].',
 '노르웨이 등 유럽에서는 생선 케이크를 전통적으로 먹어 왔고, 스칸디나비아에서는 보통 대구·해덕대구 같은 흰살생선으로 만든다[5]. 한 연구는 해덕대구 100% 배합을 기준으로 고등어를 섞은 케이크를 비교했다[5].',
 "[5] 원문에 '시판 제품에 해당하는 대조군' 표현 없음; 본문은 '스칸디나비아에서 대구·해덕대구 같은 흰살생선으로 만든다'고 씀")
rep('biology',"미국 해양대기청 보관 자료 요약에 따르면 몸 양옆의 검은 '엄지 자국' 무늬로 대구와 구별되며, 몸길이는 약 1–3.3피트이고 미국 해역 최대 기록은 30파운드이다[2]. 이 값은 웹 검색 결과 요약으로만 확인한 것이다[2]. ",
 '', '출처 [2](NOAA 보관본)는 작성자가 웹 검색 요약으로만 보았고 이 환경에서 원문(webarchive·fisheries.noaa.gov 모두)을 열 수 없어 대조 불가 — 문장과 출처 삭제')
rep('related_species','가공하면 겉모습으로 구별하기 어려워, Cytb 유전자를 표적으로',
 '원료·가공품 속 대구류를 가려내기 위해 12S rDNA(대구과 판별)와 Cytb 유전자(종 판별)를 표적으로',
 "[20] 초록에 '겉모습으로 구별하기 어렵다'는 내용 없음; 12S rDNA·Cytb 두 계통 검사였고 시판 가공품 13점에 적용")
rep('cultivation','해덕대구의 상업 어획은 자연산을 잡는 방식이며, 바렌츠해 남부 연구 시료는 덴마크식 후릿그물과 연승으로 잡은 것이었다[3].',
 '바렌츠해 남부 연구 시료는 2019년 겨울·봄에 현지 어민이 덴마크식 후릿그물과 연승으로 잡은 것이었다[3].',
 "[3]은 '상업 어획은 자연산' 일반론을 말하지 않음 — 원문(시료 2019년 어획) 그대로 좁힘")
rep('cultivation','8일 노출 실험에서 총 다환방향족탄화수소 0.1 μg/L는 성장·생존에 해가 없었다[32].',
 '8일 노출 실험에서 총 다환방향족탄화수소 0.1 μg/L는 성장·생존에는 해가 없었으나 난황 자어의 심실 발달이 줄어, 저자들은 이 농도를 위해성 평가의 영향 기준치로 권고했다[32].',
 '[32] 초록: 0.1 μg TPAH/L에서도 심실 성장 감소가 있어 영향 기준치로 권고 — 무해로만 읽히지 않게 보완')
rep('processing','노르웨이에서 산 해덕대구 필레는 지방 0.7 g/100 g, EPA+DHA 199 mg/100 g이었고, 유채기름에 지진 해덕대구 100% 생선 케이크의 지방은 2.0 g/100 g이었다[5]. 해덕대구 살 일부를 고등어로 바꾸면 EPA·DHA가 늘었고, 소비자 수용도는 해덕대구 케이크와 유의한 차이가 없었다[5].',
 '노르웨이 소매점에서 산 해덕대구 필레를 갈아 소금·감자전분·우유를 섞고 유채기름에 지진 생선 케이크에서, 살 일부를 고등어로 바꾸면 EPA·DHA가 늘었고 고등어를 섞어도 소비자 수용도는 떨어지지 않았다[5]. 필레·케이크의 지방과 EPA+DHA 수치는 원문 표에만 있어 이번 대조에서 확인하지 못함.',
 '[5] 지방·EPA+DHA 수치(0.7·199·2.0)는 표에만 있어 PMC 본문 텍스트로 대조 불가 — 수치 삭제, 초록 결론만 남김')
rep('processing','필레에 200–300 MPa 고압 처리를 하면 이노신이 하이포잔틴으로 바뀌는 속도가 늦춰졌으나 단백질 함량은 줄었다[22].',
 '필레에 200–300 MPa 고압 처리를 한 연구는 고압 처리가 이노신이 하이포잔틴으로 바뀌는 속도를 늦춘다고 결론지었으나, 해덕대구에서는 하이포잔틴 자체가 유의하게 줄지 않았고 단백질 함량은 줄었다[22].',
 '[22] 초록: Hx 감소는 청어에서만 유의, 해덕대구는 비유의 — 종별 결과 구분')
rep('genetics','1999년에는 집단 연구용 미세위성 표지가 개발되었다[9].','1999년에는 해덕대구의 미세위성 표지가 분리·보고되었다[9].',
 "[9]는 초록이 없어 제목만 확인 — '집단 연구용'은 제목에 없는 해석이라 뺌")
# compounds
C=d['compounds']; byname={c['name']:c for c in C}
def cset(n,field,val,why):
    old=byname[n][field]; byname[n][field]=val
    changes.append({"where":f"compounds[{n}].{field}","before":old,"after":val,"why":why})
TAB='[5]의 해덕대구 필레 수치는 원문 표에만 있고 PMC 본문 텍스트로 대조할 수 없음'
cset('Eicosapentaenoic acid + Docosahexaenoic acid','content_text','함량 수치는 원문 표에만 있어 이번 대조에서 확인하지 못함[5]',TAB)
cset('Eicosapentaenoic acid + Docosahexaenoic acid','activity_ko','해덕대구 살 일부를 고등어로 바꾸면 케이크의 EPA·DHA가 늘어남[5]',TAB)
cset('Anserine','content_text','236 ± 36 mg/100 g(필레; 고등어에서는 검출되지 않음)[5]','본문 값 확인, 습중량 표기는 원문에 없는 해석이라 뺌')
cset('Trimethylamine N-oxide','content_text','해덕대구 필레 수치는 원문 표에만 있어 확인하지 못함; 원문은 흰살생선 문헌값(대구 340–380 mg/100 g)과 맞는다고 씀[5]',TAB)
cset('Trimethylamine N-oxide','activity_ko','흰살생선의 주요 저분자 대사물; 미생물이 분해하면 비린내 성분 TMA가 생김(생 필레 TMA 0.1 mg/100 g)[5]','본문 확인(미생물 분해로 기술)')
cset('Inosine monophosphate','content_text','IMP 수치는 원문 표에만 있어 확인하지 못함; 생 필레 신선도 K값 40 ± 14%[5]',TAB)
cset('beta-Alanine','content_text','함량 수치는 원문 표에만 있어 확인하지 못함[5]',TAB+"; '고등어에서 불검출'도 본문에 없음")
cset('beta-Alanine','activity_ko','고등어를 섞으면 케이크 속 함량이 줄어듦(초록)[5]','초록 확인')
for n in ['Taurine','Creatine','Lactic acid']:
    c=byname[n]; C.remove(c)
    changes.append({"where":f"compounds[{n}]","before":c['content_text'],"after":"(삭제)","why":TAB+' — 수치 외에 해덕대구 고유 근거가 없어 항목 삭제'})
# assays
A=d['assays']
a=A[0]
for f in ['sample_prep']:
    o=a['conditions'][f]; a['conditions'][f]=o.replace(' (Fecher 등 방법)',' (선행 문헌 방법)')
    changes.append({"where":"assays[0].conditions.sample_prep","before":"(Fecher 등 방법)","after":"(선행 문헌 방법)","why":"사람 이름 금지"})
a=A[1]
o=a['content']; a['content']='해덕대구 필레·케이크의 EPA+DHA·총 지질 수치는 원문 표에만 있어 이번 대조에서 확인하지 못함; 고등어를 섞으면 EPA·DHA 증가(초록)[5]'
changes.append({"where":"assays[1].content","before":o,"after":a['content'],"why":TAB})
o=a['conditions']['sample_prep']; a['conditions']['sample_prep']=o.replace('(Kristinova 등 방법)','(선행 문헌 방법)')
changes.append({"where":"assays[1].conditions.sample_prep","before":"(Kristinova 등 방법)","after":"(선행 문헌 방법)","why":"사람 이름 금지"})
a=A[2]
o=a['content']; a['content']='안세린 236 ± 36 mg/100 g(필레, 본문 값); 생 필레 TMA 0.1 mg/100 g, K값 40 ± 14%; TMAO·타우린·크레아틴·IMP 수치는 원문 표에만 있어 확인하지 못함(추출은 3반복)[5]'
changes.append({"where":"assays[2].content","before":o,"after":a['content'],"why":TAB})
a['compound']='Anserine / Trimethylamine N-oxide / IMP (1H NMR)'; a['compound_ko']='안세린·TMAO·IMP 등 저분자 대사물'
# nutrients
N=d['nutrients']; rm=[x for x in N if x['source']==[5]]
for x in rm: N.remove(x)
changes.append({"where":"nutrients[생 필레(노르웨이)]","before":"총 지질 0.7 g, EPA+DHA 199 mg [5]","after":"(삭제)","why":TAB})
# sources
S=d['sources']
for s in S:
    if s['n']==32: s['title']=s['title'].replace('2023;189:114843','2023;190:114843')
    if s['n']==29: s['title']=s['title'].replace('J Protozool 1976;23(4).','J Protozool 1976;23(4):564-71.')
changes.append({"where":"sources[32].title","before":"2023;189:114843","after":"2023;190:114843","why":"PubMed 서지: 190권"})
changes.append({"where":"sources[29].title","before":"1976;23(4)","after":"1976;23(4):564-71","why":"PubMed 서지 쪽수 보완"})
S[:]=[s for s in S if s['n']!=2]
changes.append({"where":"sources[2]","before":"NOAA FishWatch Haddock(2008 보관본, 웹 검색 요약만)","after":"(삭제)","why":"원문을 열지 못한 출처"})
mp={}
for i,s in enumerate(S,1): mp[s['n']]=i; s['n']=i
def fixtxt(t):
    return re.sub(r'\[(\d+(?:\s*,\s*\d+)*)\]',lambda m:'['+', '.join(str(mp.get(int(x),int(x))) for x in re.split(r'\s*,\s*',m.group(1)))+']',t)
def walk(o):
    if isinstance(o,dict):
        for k,v in o.items():
            if k=='source' and isinstance(v,list): o[k]=[mp[x] for x in v]
            elif k=='sources': continue
            else: o[k]=walk(v)
        return o
    if isinstance(o,list): return [walk(x) for x in o]
    if isinstance(o,str): return fixtxt(o)
    return o
for k in list(d.keys()):
    if k!='sources': d[k]=walk(d[k])
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
