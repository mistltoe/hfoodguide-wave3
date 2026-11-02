import json,sys
p='/home/user/hfoodguide-wave3/docs/materials/stellaria-media/dossier.json'
d=json.load(open(p))
changes=[]
def sec(k): return next(s for s in d['sections'] if s['key']==k)
def rep(where,obj,key,old,new,why):
    v=obj[key]
    assert v.count(old)==1,(where,old)
    obj[key]=v.replace(old,new); changes.append({"where":where,"before":old,"after":new,"why":why})
o=sec('overview')
rep('sections.overview',o,'body',"별꽃(Stellaria media)은 석죽과(Caryophyllaceae) 별꽃속의 한해살이 풀로, 영어로 chickweed라 불리며 온대·한대 지역에 널리 퍼져 있다[2].",
 "별꽃(Stellaria media)은 석죽과(Caryophyllaceae) 별꽃속의 풀로, 영어로 chickweed라 불리며 추운 지역과 온대 지역에 널리 퍼져 있다[2]. 미국 노스캐롤라이나 잡초 조사에서는 한해살이 종으로 분류되었다[28].",
 "[2] 리뷰는 '여러해살이(perennial)'라고 써서 '한해살이'를 뒷받침하지 않음; 한해살이 분류는 [28] 초록에 있음")
rep('sections.overview',o,'body',"어린 순만 식품에 쓸 수 있다[1]","순만 식품원료로 쓸 수 있다[1]","[1] 조건은 '사용가능부위 : 순'뿐이고 '어린'은 원문에 없음")
rep('sections.overview',o,'body',"등 동물·세포 실험이다[4, 30–33]","등 동물·세포·시험관(효소) 실험이다[4, 30–33]","[31] COX-2 억제는 무세포 효소 시험")
h=sec('history')
rep('sections.history',h,'body',"17세기 영국의 한 약초서는 옴(mange) 치료에 권했다고","17세기 영국의 한 약초학자가 옴(mange) 치료에 권했다고","[5] 원문은 약초학자(herbalist)가 권했다고 씀")
r=sec('related_species')
rep('sections.related_species',r,'body',"water chickweed(Myosoton aquaticum)가 속한 Myosoton 속을","Myosoton 속을","[13] 초록에 종명·영명이 없어 출처 없는 보충 삭제")
c=sec('cultivation')
rep('sections.cultivation',c,'body',"헝가리 연구는 한 협회가 2017년에 수확한 지상부를 말려 썼고","헝가리 연구는 한 협회가 2017년에 수확한 풀(부위 구분 없음)을 말려 썼고","[6] 원문은 'herb'·'drug'라고만 쓰고 지상부라고 하지 않음")
rep('sections.cultivation',c,'body',"수경 재배에서는 용액 pH 5에서 새싹의 아연이 1640 μg/g 건조중량, pH 6.5에서 니켈이 250 μg/g 건조중량까지 쌓였다[24].",
 "수경 재배(용액 아연 0.55 mM 또는 니켈 0.1 mM)에서는 pH 5에서 지상부의 아연이 평균 1640 μg/g 건조중량, pH 6.5에서 니켈이 평균 250 μg/g 건조중량까지 쌓였다[24].",
 "[24] 원문 'shoots'는 새싹이 아니라 지상부; 평균값·처리 농도 조건 보충")
pr=sec('processing')
rep('sections.processing',pr,'body',"헝가리 연구는 말린 지상부를 끓는 물(1:10)로","헝가리 연구는 말린 풀을 끓는 물(1:10)로","[6] 원문은 지상부라고 하지 않음")
rep('sections.processing',pr,'body',"중국 연구는 생즙을 거대다공성 수지와 한외여과로 나눠 플라보노이드·다당·단백질 분획을 만들었다[5].",
 "중국 연구는 생풀 즙을 거대다공성 수지와 한외여과로 처리해 시료 7개(SM-1~7)를 만들었고, 활성이 가장 컸던 SM-3에는 플라보노이드 C-배당체·다당·단백질이 함께 들어 있었다[5].",
 "[5] 전문: 성분별 분획이 아니라 제법이 다른 시료 7개이며 SM-3이 세 성분을 함께 포함")
s=sec('safety')
rep('sections.safety',s,'body',"질산염이 47–597 mg/100 g 범위라고 했으나, 초록에","질산염이 47–597 mg/100 g 범위라고 했으나[9], 초록에","출처 표시 누락 보완([9] 초록 확인)")
rep('sections.safety',s,'body',"쥐에게 별꽃차 100 mg/kg을 먹였을 때 간·신장 기능과 심장 형태·기능은 변하지 않았다[7].",
 "고콜레스테롤 식이를 먹인 쥐에게 별꽃차 100 mg/kg을 먹였을 때 간·신장 기능과 심장 형태·기능은 변하지 않았다[7]. 인도 연구의 생즙 동결건조물에서 카드뮴·납·비소는 WHO 허용 기준보다 낮았고 아플라톡신은 5 ppb 미만이었다[4].",
 "[7] 실험 조건 보충, [4] 전문의 중금속·아플라톡신 품질 결과 추가")
for x in d['compounds']:
    if x['name']=='Vitexin':
        rep('compounds.Vitexin',x,'part',"지상부(생즙 분획)","전초 생즙 분획(SM-3)","[5] 시료는 생풀 전체(fresh chickweed)")
    if x['name']=='Gypsogenin':
        rep('compounds.Gypsogenin',x,'activity_ko',"(쥐)","(생쥐)","[4] 실험동물은 Swiss albino 생쥐")
        rep('compounds.Gypsogenin',x,'content_text',"생즙 동결건조물 총사포닌 1.19 μg/g","생즙 동결건조물 총사포닌(집소게닌 개별 정량 아님) 1.19 μg/g","총사포닌을 집소게닌 함량으로 오해하지 않게")
    if x['name']=='Oleanolic acid':
        rep('compounds.Oleanolic acid',x,'activity_ko',"올레아난형 사포닌의 기본 골격[4]","별꽃의 올레아난형 트라이테르페노이드 사포닌이 리파아제 억제 후보로 인용됨(생쥐 연구의 고찰)[4]","[4] 는 올레아놀산을 '기본 골격'이라 쓰지 않음; 원문 고찰 내용으로 바꿈")
    if x['name']=='Potassium':
        rep('compounds.Potassium',x,'part',"생잎","생잎·연한 줄기","[3] 무기질은 잎과 연한 줄기 생중량 기준")
n=d['nutrients'][0]
rep('nutrients[0].form',n,'form',"생잎(스페인","생잎·연한 줄기(스페인","[3] 'leaves and tender stems' 생중량 기준")
a=d['assays']
rep('assays[0].part',a[0],'part',"지상부 생풀 착즙 동결건조물(인도 하리아나주 채취)","생풀(전초) 착즙 동결건조물(인도 하리아나주 히사르 채취)","[4] 원문은 'fresh herb/fresh plant'로 지상부라 하지 않음")
rep('assays[2].part',a[2],'part',"지상부 생즙의 거대다공성 수지·한외여과 분획 SM-3","생풀(전초) 즙의 거대다공성 수지·한외여과 시료 SM-3","[5] 원문은 'fresh chickweed' 전체")
for src in d['sources']:
    if src['n']==2:
        rep('sources[2]',src,'title',"전문 확인; 2차 문헌(리뷰))","전문 확인; 2차 문헌(리뷰); 원문은 여러해살이라고 씀)","리뷰의 생활형 표기 오류 메모")
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('/home/user/hfoodguide-wave3/docs/materials/stellaria-media/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
