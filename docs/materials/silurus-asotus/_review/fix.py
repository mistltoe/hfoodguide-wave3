import json,sys
p='/home/user/hfoodguide-wave3/docs/materials/silurus-asotus/dossier.json'
d=json.load(open(p))
changes=[]
def sec(k): return [s for s in d['sections'] if s['key']==k][0]
def rep(where,obj,key,old,new,why):
    v=obj[key]; assert old in v,(where,old); obj[key]=v.replace(old,new,1)
    changes.append({"where":where,"before":old,"after":new,"why":why})
o=sec('overview')
rep('sections.overview',o,'body','국내 연구에서는 양식 메기 살의 지방산 조성이','국내 연구에서는 대학 연구실 순환여과 수조에서 기른 2년생 메기 살의 지방산 조성이','[3] 시료는 상업 양식장이 아니라 대학 연구실 순환여과 수조에서 기른 2년생 어미')
h=sec('history')
rep('sections.history',h,'body','등살과 난소의 DHA 비율이 산란·계절·먹이에 따라 변한다고 보고되었다[4, 5]','등살 DHA 비율은 먹이 지방산의 영향을 받고 n-6 지방산 비율은 계절에 따라 달랐으며[4], 난소 인지질(PC·PE)의 DHA 비율은 산란기에 산란 후보다 높았다고 보고되었다[4, 5]','[4] 초록: DHA는 먹이 영향, 계절 변동은 n-6·AA; [5]: 난소 PC·PE의 DHA가 산란기에 높음. 등살 DHA가 산란·계절로 변한다는 근거는 없음')
b=sec('biology')
rep('sections.biology',b,'body','메기는 육식성 어종으로, 한국 갑천 조사에서','한국 갑천 조사에서','[10] 초록에는 식성 분류 표현이 없고 영양 단계 수치만 있음')
rep('sections.biology',b,'body','국내 전국 조사에서도 하천·호수의 육식성 어종일수록 수은을 더 많이 축적하는 경향이 보고되었다[6].','국내 전국 조사에서는 민물의 어식성(물고기를 먹는) 어종이 육식·잡식성 어종보다 약 2배, 플랑크톤식 어종보다 약 4배 많은 수은을 축적했으나, 이 차이에는 몸 크기 차이도 작용했을 수 있다고 하였다[6].','[6] 초록은 piscivorous 를 carnivorous 와 구분하며 크기 영향 가능성을 함께 적음')
s=sec('safety')
rep('sections.safety',s,'body','개별 시료 최고 수은 농도 1,720 μg/kg이 메기 한 마리에서 측정되었고','조사한 78종 전체의 개별 시료 가운데 최고 수은 농도 1,720 μg/kg(초록에 습·건중량 기준 표기 없음)이 메기 한 마리에서 측정되었고(메기 종 평균값은 초록에 없음)','[6] 초록 대조 — 최고값은 전체 시료 중 1건이며 기준(습/건) 표기 없음을 명시')
rep('sections.safety',s,'body','광산 영향 하천(샹강) 조사에서도 근육 섭취로 인한 건강 위해는 뚜렷하지 않다고 평가되었다[9]','광산 영향 하천(샹강) 조사에서도 근육의 미량원소 16종(수은은 분석 대상 아님) 섭취로 인한 건강 위해는 뚜렷하지 않다고 평가되었다[9]','[9] 초록: 분석 원소 16종에 Hg 없음')
rep('sections.safety',s,'body','메기 필레의 중간 극성 분획에서 다환방향족탄화수소 등 AhR 활성 물질의 작용이 높게 나타났다[10]','메기 필레의 중간 극성 분획에서 AhR 매개 활성이 높게 나타났고, 조사 시료 전체에서 알려진 AhR 작용 물질 가운데 주된 기여 물질은 다환방향족탄화수소(벤조[b]안트라센)였다[10]','[10] PAH 기여 분석은 메기 필레만이 아니라 전체 시료 대상')
rep('sections.safety',s,'body','초록에서 유충이 나온 어종으로 명시된 것은 가물치와 드렁허리뿐이었다[13]','초록에서 유충이 나온 어종으로 명시된 것은 가물치와 드렁허리뿐이었다(1989년 내장 소화로 얻은 유충 34마리의 어종별 내역은 초록에 없음)[13]','[13] 1989년 내장은 종별로 모아 소화했고 어종별 유충 수가 초록에 없어 메기 음성으로 단정 못함')
for c in d['compounds']:
    if c['part']=='난소(알)':
        old=c['content_text']; new='난소 지질의 DHA 12.3±0.5% (총 지방산 중); 산란기 야생 메기 난소의 지질 함량은 7.3±1.6 g/100 g(습중량)'
        c['content_text']=new; changes.append({"where":"compounds[DHA 난소].content_text","before":old,"after":new,"why":"[5] 초록: DHA 12.3% 는 시료 조건(야생·산란기)이 명시되지 않음; 7.3 g/100 g 만 야생 산란기"})
    if c['name']=='Docosahexaenoic acid' and c['part']=='살(flesh)':
        old=c['content_text']; new=old.replace('양식 2년생','실험실 수조 사육 2년생, 원문 표 기준 평균±표준오차')
        c['content_text']=new; changes.append({"where":"compounds[DHA 살].content_text","before":old,"after":new,"why":"[3] 표4: mean±standard error, 시료는 대학 연구실 순환여과 수조 사육"})
a=d['assays'][0]
old=a['content']; a['content']=old.replace('(총 지방산 중)[3]','(총 지방산 중, 평균±표준오차)[3]')
changes.append({"where":"assays[0].content","before":old,"after":a['content'],"why":"[3] 표4 각주: 평균±표준오차"})
ttl={8:" 101(1):26-32",9:" 25(9):8861-8870",19:" 112(3):2603-2614",20:" 26(5):641-7",26:" 1472(3):668-75",28:" 106:480-490",15:" 115(4):1547-56",30:" (Pt 2)"}
for src in d['sources']:
    n=src['n']
    if n in (8,9,19,20,26,28,15):
        t=src['title']; i=t.rfind(' (초록만 확인)')
        src['title']=t[:i]+';'+ttl[n].strip()+t[i:]
changes.append({"where":"sources[8,9,15,19,20,26,28].title","before":"권·호·쪽 없음","after":"PubMed 서지로 권·호·쪽 보충","why":"PubMed 메타데이터 대조"})
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('/home/user/hfoodguide-wave3/docs/materials/silurus-asotus/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
