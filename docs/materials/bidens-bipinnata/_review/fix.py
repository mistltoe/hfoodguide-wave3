import json
p='/home/user/hfoodguide-wave3/docs/materials/bidens-bipinnata/dossier.json'
d=json.load(open(p))
changes=[]
def sec(key): return next(s for s in d['sections'] if s['key']==key)
def rep(key,old,new,why):
    s=sec(key); assert old in s['body'],(key,old); s['body']=s['body'].replace(old,new)
    changes.append({"where":f"sections.{key}","before":old,"after":new,"why":why})
rep('biology',"한국에서도 광주와 남한 대부분 지역에서 흔히 자라며, 2011–2012년 7–10월 잎·줄기에 흰가루병(Podosphaera xanthii)이 퍼진 것이 처음 보고되었다[8].",
 "한국에서는 2011–2012년 7–10월 광주와 남한 대부분 지역의 도깨비바늘 잎·줄기에 흰가루병(Podosphaera xanthii)이 널리 발생한 것이 처음 보고되었다[8].",
 "[8] 초록에서 '광주와 남한 대부분 지역에 널리 퍼졌다'는 것은 식물이 아니라 흰가루병이다")
rep('biology',"중국에서 수집한 개체의 핵형은","중국 산둥의 연구진이 보고한 핵형은","[7] 초록에 시료 채집지가 없고 저자 소속(산둥)만 있음")
rep('genetics',"중국에서 채집한 도깨비바늘의 핵형은","중국 산둥의 연구진이 보고한 도깨비바늘의 핵형은","[7] 초록에 시료 채집지가 없음")
rep('safety',"전초 분리 성분 5종이 백혈병 세포주를 억제했다는 보고(IC50 ≤ 60 μg/ml)도 시험관 결과다[35].",
 "분리 성분 5종이 백혈병 세포주(HL-60, U937)를 억제했고 U937에 대한 IC50이 60 μg/ml 이하였다는 보고도 시험관 결과다[35].",
 "[35] 초록은 분리 부위(전초)를 밝히지 않고, IC50 ≤ 60 μg/ml 은 U937(원문 표기 V937) 세포에 대한 값")
rep('processing',"연구용 가공은 주로 전초 추출물에서 플라보노이드를 농축하는 방식으로,",
 "연구용 가공은 주로 추출물에서 총플라보노이드를 농축하는 방식으로(두 연구 모두 초록에 사용 부위를 밝히지 않음),",
 "[32]·[16] 초록에 '전초'라는 부위가 없음")
rep('cultivation',"브라질에서는 밭의 잡초로 다루어져","브라질에서는 잡초로 다루어져","[33] 은 '잡초(weed)'라고만 하고 밭을 특정하지 않음")
# compounds
cs=d['compounds']
for c in cs:
    if c['name']=='Kaempferol 3-O-rutinoside':
        o=c['activity_ko']; c['activity_ko']="잎에서 줄기·열매보다 많이 쌓이는 플라보노이드 배당체로 보고(추정 동정)[3]"
        changes.append({"where":"compounds[Kaempferol 3-O-rutinoside].activity_ko","before":o,"after":c['activity_ko'],"why":"[3] 은 잎에 '더 많다(enriched)'고 했지 잎 특이적이라고 하지 않음"})
    if c['name']=='Luteolin':
        o=c['activity_ko']; c['activity_ko']=o.replace("(흰쥐 조직 분포)","(조직 분포 연구)")
        changes.append({"where":"compounds[Luteolin].activity_ko","before":o,"after":c['activity_ko'],"why":"[17] 초록에 실험 동물 종이 적혀 있지 않음"})
    if c['name']=='Hyperoside':
        o=c['activity_ko']; c['activity_ko']=o.replace("고지혈증 지표 7종 중 하나(흰쥐)","고지혈증 지표 7종 중 하나")
        changes.append({"where":"compounds[Hyperoside].activity_ko","before":o,"after":c['activity_ko'],"why":"[17] 초록에 실험 동물 종이 적혀 있지 않음"})
    if c['name']=='16-Dehydropregnenolone':
        o=json.dumps({k:c[k] for k in ('name','name_ko','activity_ko')},ensure_ascii=False)
        c['name']='16-Pregnenolone (as reported)'
        c['name_ko']="16-프레그네놀론(원문 표기, GC-MS 라이브러리 대조로 추정 동정)"
        c['content_text']="분리 성분(함량 미보고), GC-MS 라이브러리(NIST) 대조로 동정[27]"
        c['activity_ko']="잎 헥산 추출물에서 분리, 시험관 항균 활성 보고; 다만 MIC 값이 초록(72 μg/mL)과 본문 결과(>250 mg/mL, 72 mg/mL 은 함께 분리된 올레산 메틸에스터)에서 서로 달라 수치는 확정할 수 없음[27]"
        changes.append({"where":"compounds[16-Pregnenolone]","before":o,"after":json.dumps({k:c[k] for k in ('name','name_ko','activity_ko')},ensure_ascii=False),"why":"[27] 원문은 '16-Pregnenolone'(3β-하이드록시·20-옥소, 즉 프레그네놀론 구조 설명)이라 16-Dehydropregnenolone 으로 바꿀 근거가 없고, PMC 전문 결과 절은 MIC 를 초록과 반대로(16-Pregnenolone >250 mg/mL) 적음"})
before=len(cs)
iso=[c for c in cs if c['name']=='Isoquercitrin']
d['compounds']=[c for c in cs if c['name']!='Isoquercitrin']
changes.append({"where":"compounds[Isoquercitrin]","before":json.dumps(iso[0],ensure_ascii=False),"after":"(삭제)","why":"유일한 근거 [26] 이 PubMed 에서 Retracted Publication 으로 표시된 철회 논문 — 성분 항목의 근거로 쓸 수 없음(safety 절의 철회 언급은 유지)"})
# sources
S={s['n']:s for s in d['sources']}
def st(n,old,new,why):
    o=S[n]['title']; assert old in o,(n,old); S[n]['title']=o.replace(old,new)
    changes.append({"where":f"sources[{n}].title","before":o,"after":S[n]['title'],"why":why})
st(27,"(초록 확인)","(PMC8716870 전문 확인 — 시료는 파키스탄 아자드카슈미르 채집, MIC 값이 초록과 본문에서 다름)","전문 대조 결과 반영")
st(29,"Zhongguo Zhong Yao Za Zhi 2021.","Zhongguo Zhong Yao Za Zhi 2021;46(15):3893-3899.","권호·쪽 보충(PubMed)")
st(31,"Environ Pollut 2019.","Environ Pollut 2019;253:141-151.","권·쪽 보충(PubMed)")
st(33,"Sci Rep 2022.","Sci Rep 2022;12(1):13476. (브라질 피아우이 연방대학)","권호·쪽 보충, 브라질 연구 근거(저자 소속) 명시")
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('/home/user/hfoodguide-wave3/docs/materials/bidens-bipinnata/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
