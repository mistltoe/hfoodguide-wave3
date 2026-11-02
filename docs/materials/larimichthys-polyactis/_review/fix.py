import json,re
p='dossier.json'; d=json.load(open(p))
ch=[]
def sec(k): return next(s for s in d['sections'] if s['key']==k)
def rep(obj,key,old,new,where,why):
    assert old in obj[key], (where,old)
    obj[key]=obj[key].replace(old,new); ch.append({"where":where,"before":old,"after":new,"why":why})
rep(sec('genetics'),'body','97.89%(663.13 Mb)','97.90%(663.13 Mb)','sections.genetics','[2] PubMed 초록은 97.90%로 적음')
rep(sec('processing'),'body','중국 연구에서 다진 조기 살을 진공 포장해 80 °C에서 180분 가열한 국물은 감칠맛 뉴클레오타이드인 이노신산이 50.64 mg/100 g으로 가장 많았고, 100 °C 20분 처리는 아미노산과 다가불포화지방산을 가장 잘 보존했다[5].',
 '중국 연구에서는 다진 조기 살을 진공 포장해 가열한 뒤 봉지 안에 흘러나온 액(물을 넣지 않음)을 \'국물\'로 정의해 분석했는데, 80 °C 180분 처리 국물은 감칠맛 뉴클레오타이드인 이노신산이 50.64 mg/100 g으로 다른 두 조건보다 많았고, 100 °C 20분 대조 처리는 아미노산과 다가불포화지방산 값이 수치상 가장 높았다(일부 비교는 유의하지 않음)[5].',
 'sections.processing','[5] Methods 2.2: 국물은 진공 포장 살에서 흘러나온 삼출액이고 100 °C 20분은 대조군; PUFA 차이는 일부 유의하지 않다고 본문이 씀')
rep(sec('safety'),'body','동중국해 시료 122마리 중 116마리(95.1%)에서 고래회충과 유충이 나왔고','세 어종을 합친 동중국해 시료 122마리 중 116마리(95.1%)에서 고래회충과(Anisakidae) 유충이 나왔고','sections.safety','[23] 95.1%는 조기만이 아니라 세 어종 합계(조기 표본은 20마리)')
rep(sec('history'),'body','Larimichthys 속과 Collichthys 속은 이 과에서 가장 젊은 계통으로','Larimichthys 속과 Collichthys 속은 분석한 민어과 종 가운데 가장 젊은 계통으로','sections.history','[6] 초록은 \'Within the studied species\'로 범위를 한정')
basis='국물 무게·건물·지방 가운데 어느 기준인지 논문이 밝히지 않음 — 생선 살 함량으로 옮겨 쓰지 말 것'
for c in d['compounds']:
    if c['name']=='Docosahexaenoic acid':
        rep(c,'part',c['part'],'진공 포장한 다진 조기 살을 가열할 때 흘러나온 액(논문이 \'국물\'로 정의, 물 첨가 없음)','compounds[DHA].part','[5] Methods 2.2')
        rep(c,'content_text','100 °C 20분 처리 1085.20 mg/100 g(논문 본문 표기)[5]','100 °C 20분(대조) 처리 1085.20 mg/100 g(논문 본문 표기; '+basis+')[5]','compounds[DHA].content_text','값의 기준이 원문에 없고 삼출액 값이라 생선 살 DHA로 오인될 수 있음')
    if c['name']=='Oleic acid':
        rep(c,'content_text','100 °C 20분 처리 1626.49 mg/100 g(C18:1n9c, 논문 본문 표기)[5]','100 °C 20분(대조) 처리 1626.49 mg/100 g(C18:1n9c, 논문 본문 표기; '+basis+')[5]','compounds[Oleic].content_text','DHA와 같은 기준 문제')
for a in d['assays']:
    if a['compound']=='Docosahexaenoic acid':
        rep(a,'part',a['part'],'진공 포장한 다진 조기 살을 가열할 때 흘러나온 액(물 첨가 없음, 저우산 시장 구입 약 60 g 개체)','assays[DHA].part','[5] Methods 2.1–2.2')
        rep(a,'content','100 °C 20분 처리 1085.20 mg/100 g(논문 본문 표기); Σn-3 PUFA 1642.87 mg/100 g[5]','100 °C 20분(대조) 처리 1085.20 mg/100 g; Σn-3 PUFA 1642.87 mg/100 g(논문 본문 표기, 기준 미표기)[5]','assays[DHA].content','기준 미표기를 값 옆에 밝힘')
        rep(a['conditions'],'instrument','Agilent 7890A GC, 불꽃이온화검출기(FID)','GC-FID(Agilent 7890A)','assays[DHA].conditions.instrument','원문 표기와 같게 정리(상표명은 기기 모델 표기로 유지)')
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(ch,open('_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(ch))
