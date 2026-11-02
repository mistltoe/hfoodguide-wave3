import json
p='/home/user/hfoodguide-wave3/docs/materials/rubus-suavissimus/dossier.json'
d=json.load(open(p))
ch=[]
def rep(where,obj,key,old,new,why):
    assert old in obj[key], (where,old)
    b=obj[key]; obj[key]=b.replace(old,new); ch.append({"where":where,"before":old,"after":new,"why":why})
S={s['key']:s for s in d['sections']}
rep('sections.related_species',S['related_species'],'body',
 "복분자·산딸기·라즈베리·블랙베리 같은 다른 산딸기속 원료는 주로 열매를 쓰는 원료이므로 첨차 잎의 성분·효능 자료와 섞지 않아야 한다[1].",
 "복분자·라즈베리는 열매, 산딸기·블랙베리는 잎·열매를 사용가능부위로 하는 별개 종의 원료이므로, 첨차 잎의 성분·효능 자료와 섞지 않아야 한다[1].",
 "I1020 원자료: 산딸기(Rubus crataegifolius)·블랙베리(Rubus fruticosus 등)는 '사용가능부위 : 잎, 열매'로 올라 있어 '주로 열매'는 부정확")
rep('sections.related_species',S['related_species'],'body',
 "예를 들어 디하이드로칼콘 감미 성분 트릴로바틴을 내는 '중국 전통 단차' 식물은 루부소사이드를 내는 첨차와 다른 감미 원료로 연구된다[33].",
 "예를 들어 디하이드로칼콘 감미 성분 트릴로바틴은 'Chinese sweet tea'로도 불리는 Lithocarpus polystachyus의 잎에서 나오는 성분으로, 루부소사이드를 내는 첨차와는 다른 식물이다[33].",
 "기존 [33](PMID 38338387) 초록은 식물 학명이 빠져 있어 '다른 식물'임을 직접 보이지 못함 — 트릴로바틴의 기원 식물을 Lithocarpus polystachyus 로 명시한 PMID 36150533 로 출처 교체")
for c in d['compounds']:
    if c['name']=='Steviolmonoside':
        old=c['content_text']
        c['content_text']="잎 평균 0.71% w/w, 시료 간 변동 29%(HPLC-PDA, 논문 본문 수치; 같은 논문의 조성비 '다섯 지표성분 합계 5.9%의 1.4%'로 환산하면 약 0.08%여서 원문 안에서 값이 맞지 않음)[2]"
        ch.append({"where":"compounds[Steviolmonoside].content_text","before":old,"after":c['content_text'],"why":"[2] 전문: 본문은 평균 0.71% w/w 라 쓰지만 같은 논문 조성비(5.9% 중 1.4%)로는 약 0.08% — 원문 내부 불일치를 밝힘"})
for a in d['assays']:
    if a['compound']=='Steviolmonoside':
        old=a['content']
        a['content']="잎 평균 0.71% w/w(논문 본문 수치; 조성비 5.9%의 1.4%로 환산하면 약 0.08%로 원문 안에서 불일치), 변동 29%[2]"
        ch.append({"where":"assays[Steviolmonoside].content","before":old,"after":a['content'],"why":"위와 같음"})
for s in d['sources']:
    if s['n']==33:
        old=s['title']
        s['title']="Trilobatin alleviates non-alcoholic fatty liver disease in high-fat diet plus streptozotocin-induced diabetic mice by suppressing NLRP3 inflammasome activation. Eur J Pharmacol 2022;933:175291 (PMID 36150533, doi:10.1016/j.ejphar.2022.175291)"
        s['url']="https://pubmed.ncbi.nlm.nih.gov/36150533/"
        s['publisher']="European Journal of Pharmacology (PubMed)"
        ch.append({"where":"sources[33]","before":old,"after":s['title'],"why":"트릴로바틴 기원 식물(Lithocarpus polystachyus)을 초록에 명시한 출처로 교체"})
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(ch,open('/home/user/hfoodguide-wave3/docs/materials/rubus-suavissimus/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(ch))
