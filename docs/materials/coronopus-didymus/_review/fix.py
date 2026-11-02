import json
p='dossier.json'; d=json.load(open(p))
FLAG="원문 수치 그대로; 같은 표의 6개 성분 합이 1,756 mg/g으로 1,000을 넘어 단위·기준 오류가 의심되므로 검증 필요"
ch=[]
def rep(where, obj, key, old, new):
    v=obj[key]; assert old in v, (where, old); obj[key]=v.replace(old,new); ch.append({"where":where,"before":old,"after":new})
cs=d['compounds']
for c in cs:
    n=c['name']
    if n=="Chrysoeriol 4'-O-(6''-acetyl)-glucoside":
        rep("compounds.Chrysoeriol 4'-O-(6''-acetyl)-glucoside.content_text",c,'content_text',"전초 유래로 보고[15]","냄새냉이에서 추출한 성분으로 보고(부위는 초록에 없음, 원문 표기 chrysoeriol-6-O-acetyl-4'-β-D-glucoside)[15]")
    if n=="Quercetin":
        rep("compounds.Quercetin.content_text",c,'content_text',"(원문 표기 그대로; 단위·기준이 비현실적이어서 검증 필요)","("+FLAG+")")
        rep("compounds.Quercetin.activity_ko",c,'activity_ko',"냄새냉이·님 추출물·쿼세틴 병용이 당뇨 생쥐에서 혈당과 간 효소(ALT·AST)를 낮춤(동물 시험, 개별 성분 효과 아님)[28]","당뇨 유발 생쥐에서 냄새냉이 추출물·님 추출물·쿼세틴을 각각 주어도 혈당이 낮아졌고, 셋을 함께 준 군에서 간 효소(ALT·AST) 감소가 더 컸다는 보고(동물 시험; 냄새냉이 추출물 속 쿼세틴의 기여는 따로 확인되지 않음)[28]")
    if n=="Chlorogenic acid":
        rep("compounds.Chlorogenic acid.content_text",c,'content_text',"(원문 표기 그대로, 검증 필요)","("+FLAG+")")
    if n=="Ferulic acid":
        rep("compounds.Ferulic acid.content_text",c,'content_text',"메탄올 추출물 23.33 mg/g 건조중량[9]","메탄올 추출물 23.33 mg/g 건조중량("+FLAG+")[9]")
    if n=="Kaempferol":
        rep("compounds.Kaempferol.content_text",c,'content_text',"메탄올 추출물 11.5 mg/g 건조중량[9]","메탄올 추출물 11.5 mg/g 건조중량("+FLAG+")[9]")
before=len(cs)
d['compounds']=[c for c in cs if c['name']!="Benzoic acid"]
assert len(d['compounds'])==before-1
ch.append({"where":"compounds.Benzoic acid","before":"벤조산 — 메탄올 추출물 428 mg/g 건조중량(원문 표기 그대로, 검증 필요)[9]","after":"(삭제)"})
for a in d['assays']:
    if a['compound']=="Quercetin":
        rep("assays.Quercetin.content",a,'content',"(원문 표기 그대로)","("+FLAG+")")
    if a['compound']=="Chrysoeriol":
        rep("assays.Chrysoeriol.conditions.sample_prep",a['conditions'],'sample_prep',"→ 메탄올:물 7:3에 녹여 Sephadex LH-20","→ 메탄올:물 7:3에 녹인 페놀 추출물(0.67 g)을 Sephadex LH-20")
S={s['key']:s for s in d['sections']}
rep("sections.processing",S['processing'],'body',"브라질에서는 잎을 우리거나 달이거나 음식에 넣어 먹는다고 보고되었다[4].","브라질에서는 이 풀을 우리거나 달이거나 음식으로 먹는다고 보고되었다(부위는 초록에 없음)[4].")
rep("sections.history",S['history'],'body',"남아시아 쪽 연구는 해열·거담","지상부 플라보노이드 연구는 해열·거담")
rep("sections.overview",S['overview'],'body',"메톡시 플라본인 크리소에리올(chrysoeriol)과 그 배당체가 분리·정량되었다[6, 7, 15].","메톡시 플라본인 크리소에리올(chrysoeriol)과 그 배당체가 분리되었고, 크리소에리올은 말린 지상부 10 g당 약 1.60 mg으로 정량되었다[6, 7, 15]. 한 논문은 전초 메탄올 추출물의 폴리페놀 함량을 보고했지만 수치 합이 1,000 mg/g을 넘어 신뢰하기 어렵다[9].")
src={s['n']:s for s in d['sources']}
for n,old,new in [(19,"2018;20(5) (PMID","2018;20(5):483-489 (PMID"),(27,"Microsc Res Tech 2019 (PMID","Microsc Res Tech 2019;82(10):1779-1786 (PMID"),(29,"Chemosphere 2022 (PMID","Chemosphere 2022;303(Pt 2):135138 (PMID")]:
    rep(f"sources[{n}].title",src[n],'title',old,new)
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(ch,open('_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(ch))
