import json,sys
p='/home/user/hfoodguide-wave3/docs/materials/rumex-japonicus/dossier.json'
d=json.load(open(p))
changes=[]
def sec(k): return next(s for s in d['sections'] if s['key']==k)
def rep(where,obj,key,old,new,why):
    assert old in obj[key], (where,old)
    obj[key]=obj[key].replace(old,new); changes.append({"where":where,"before":old,"after":new,"why":why})

# aliases
i=d['aliases'].index("양제(羊蹄, Yang Ti)")
d['aliases'][i]="양제(羊蹄, Yang Ti; 식품원료 목록에서는 소리쟁이 R. crispus 의 다른 이름으로 올라 있음)"
changes.append({"where":"aliases","before":"양제(羊蹄, Yang Ti)","after":d['aliases'][i],"why":"I1020 원자료에서 '양제'는 소리쟁이(R. crispus) 행의 RAWMTRL_NCKNM 에 있음 — 이름 혼동 주의 표시"})

o=sec('overview')
rep('sections.overview',o,'body',"중국에서는 '양제(羊蹄, Yang Ti)'라 부르는 민간 약초다[1][10].",
 "중국에서는 '양제(羊蹄, Yang Ti)'라 부르는 민간 약초다[10]. 다만 식약처 식품원료 목록에서 '양제'는 소리쟁이(R. crispus)의 다른 이름으로 올라 있어, 이 이름만으로 원료를 가리키면 두 종이 섞일 수 있다[1].",
 "[1] 원자료에는 Yang Ti 가 없고 '양제'는 R. crispus 행 별칭임 — 출처 분리·혼동 경고 추가")

h=sec('history')
rep('sections.history',h,'body',"이처럼 전통 쓰임새의 기록은 주로 뿌리를 약으로 쓴 것이다[15][16][31].","이처럼 전통 쓰임새의 기록은 주로 뿌리를 약으로 쓴 것이다[15][16].",
 "[31] 초록은 옴·황달 전통 쓰임만 말하고 부위를 밝히지 않음")
rep('sections.history',h,'body',"지상부는 가축 사료로도 영양가가 높다고 소개되었다[2].","이 식물은 가축 사료로도 영양가가 높다고 소개되었다(부위는 밝히지 않음)[2].",
 "[2] 전문은 사료 가치를 말하지만 '지상부'라고 특정하지 않음")

b=sec('biology')
rep('sections.biology',b,'body',"분포 지역에서는 소리쟁이(R. crispus)나 돌소리쟁이(R. obtusifolius)와 따로, 또는 셋이 한곳에 함께 자라기도 한다[7].",
 "분포 지역에서는 소리쟁이(R. crispus)나 돌소리쟁이(R. obtusifolius) 가운데 한 종과 자주 섞여 자라고, 때로는 세 종이 한곳에 함께 자란다[7].",
 "[7] 'frequently cooccurs with either ... separately or occasionally together' — '따로'는 오해 소지")
rep('sections.biology',b,'body',"지상부 생물량도 줄지 않았다[2].",
 "지상부 생물량도 줄지 않았다[2]. 다만 두 흙은 pH 말고도 총질소·유기물·수분 함량이 달라, 연구진도 pH 하나의 효과로 보지 않았다[2].",
 "[2] 표 1·고찰: 두 자연 토양의 기초 성질이 달라 단일 요인 실험이 아님 — 과장 방지")
rep('sections.biology',b,'body',"구리 광산 등 금속 오염지에 사는 집단은","금속이 많은 흙(metalliferous soil)에 사는 집단은",
 "[21] 초록은 '구리 광산'을 말하지 않고 metalliferous/non-metalliferous soils 로만 씀")

r=sec('related_species')
rep('sections.related_species',r,'body',"국내 소리쟁이×돌소리쟁이 잡종 연구에서 참소리쟁이의 핵 DNA(pgiC) 클론은 2–3가지 서열형을 지녔고 그중 하나를 소리쟁이와 공유했다[7]. 연구진은 이를 근거로",
 "국내 소리쟁이×돌소리쟁이 잡종 연구에서 참소리쟁이는 혼생 집단에서 7개체만 표본으로 들어갔고, 그중 클론한 5개체의 핵 DNA(pgiC)는 2–3가지 서열형을 지녔으며 그 가운데 N2 하나를 소리쟁이와 공유했다[7]. 엽록체 단상형 2개 중 C1도 소리쟁이와 공유했다[7]. 연구진은 이 두 가지를 근거로",
 "[7] 전문: 참소리쟁이는 7개체(클론 5개체)뿐이고, 잡종 기원 추론은 핵 N2·엽록체 C1 공유 두 근거에 기댐 — 표본 규모와 근거를 밝힘")
rep('sections.related_species',r,'body',"같은 연구는 참소리쟁이의 고유 단상형 상당수가 잡종 개체에서 나오지 않아, 참소리쟁이가 그 잡종의 부모였을 가능성은 낮다고 판단했다[7].",
 "같은 연구는 참소리쟁이의 엽록체 단상형 2개 중 1개, 핵 단상형 4개 중 3개가 고유해 잡종 개체에서 나오지 않았으므로, 참소리쟁이가 소리쟁이×돌소리쟁이 잡종의 부모였을 가능성은 낮고 돌소리쟁이가 부모라고 판단했다[7].",
 "[7] 고찰 원문 수치(1/2, 3/4)로 구체화하고 '그 잡종'을 명시")

c=sec('cultivation')
rep('sections.cultivation',c,'body',"17일 간격 8단계로 시료를 거두었다[2].","심기 전(S0)부터 17일 간격으로 8개 시점(S0–S7)을 두고 S1–S7에 식물 시료를 거두었다[2].",
 "[2] Methods: S0 은 심기 전 흙 상태라 식물 시료는 7회")
rep('sections.cultivation',c,'body',"알칼리성 흙에서 S7 뿌리의 피스시온 함량은 58.21% 늘었다[2].","알칼리성 흙에서는 S7 단계 피스시온 함량이 58.21% 늘었는데, 피스시온은 지하부(뿌리)에서만 비교된 값이다[2].",
 "[2] 초록은 부위를 밝히지 않음; 본문 PBA(지하부)로만 비교 — 잎 결과로 읽히지 않게 명시")

pr=sec('processing')
rep('sections.processing',pr,'body',"다이클로로메테인 추출물을 고속 역류 크로마토그래피로 분리하면 시료 500 mg에서",
 "중국 지린성에서 채집한 뿌리 가루의 다이클로로메테인 조추출물을 고속 역류 크로마토그래피로 분리하면 조추출물 500 mg에서",
 "[25] 전문(PMC6259845) 확인: 시료는 뿌리, 500 mg 은 조추출물")
rep('sections.processing',pr,'body',"이런 뿌리 추출물의 대장염·파킨슨병·아토피 피부염 모델 결과는 모두 동물·세포 실험이며, 식품인 잎과는 부위가 다르다[15][16][17][28].",
 "뿌리 추출물(대장염 연관 대장암 연구는 초록에 부위가 없음)의 대장염·대장암·파킨슨병·아토피 피부염 모델 결과는 모두 동물·세포 실험이며, 식품인 잎과는 부위가 다르다[15][16][17][28].",
 "[17] 초록은 추출 부위를 밝히지 않음 — 확인 범위를 밝힘")

# compounds
for cp in d['compounds']:
    if cp['name']=='Chrysophanol':
        old=cp['content_text']; cp['content_text']=old.replace("다이클로로메테인 추출물 500 mg에서 24.1 mg 분리[25]","뿌리 다이클로로메테인 조추출물 500 mg에서 24.1 mg 분리(순도 98.8%)[25]")
        changes.append({"where":"compounds.Chrysophanol.content_text","before":old,"after":cp['content_text'],"why":"[25] 전문: 뿌리 시료·조추출물·순도"})

# sources
for s in d['sources']:
    if s['n']==25:
        s['title']=s['title'].replace("(초록 확인)","(전문 확인)"); changes.append({"where":"sources[25]","before":"(초록 확인)","after":"(전문 확인)","why":"PMC6259845 전문 대조"})
    if s['n']==8 and '440' not in s['title']:
        s['title']=s['title'].replace("2020;5(1)","2020;5(1):439-440"); changes.append({"where":"sources[8]","before":"2020;5(1)","after":"2020;5(1):439-440","why":"PubMed 서지 쪽수"})
    if s['n']==3:
        s['title']=s['title'].replace("J Mycol Med 2024:101513","J Mycol Med 2024;34(4):101513"); changes.append({"where":"sources[3]","before":"J Mycol Med 2024:101513","after":"J Mycol Med 2024;34(4):101513","why":"PubMed 서지"})
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open(p.replace('dossier.json','_review/changes.json'),'w'),ensure_ascii=False,indent=1)
print(len(changes))
