import json
p='suillus-bovinus/dossier.json'
d=json.load(open(p))
ch=[]
def rep(where,obj,key,old,new,why):
    s=obj[key]; assert old in s,(where,old); obj[key]=s.replace(old,new); ch.append({"where":where,"before":old,"after":new,"why":why})
S={s['key']:s for s in d['sections']}
rep('sections.overview',S['overview'],'body',"'European Cow Bolete'라는 이름으로도 불린다[5, 22]","'European Cow Bolete'라는 이름으로도 불린다[5]","[22] 전문에는 이 영명이 없고 [5] 본문에만 있음")
rep('sections.biology',S['biology'],'body',"이 기재는 명명자(L.) Roussel·1796년과 검색표로 이 종의 것이라 판단했다[4]","이 기재는 기재 순서(학명 알파벳순)와 검색표(관공에 젖빛 방울이 없고 갓과 대가 같은 색)로 이 종의 것이라 판단했다[4]","명명자 '(L.) Roussel, 1796'은 S. granulatus 와도 같아 종 귀속 근거로 약함 — 원문 검색표 7항·비고로 근거 교체")
rep('sections.related_species',S['related_species'],'body',"대사체 조성은 이 종이 비단그물버섯과 더 비슷했다[22]","대사체 조성은 이 종이 G. roseus보다 함께 비교한 같은 속의 다른 한 종과 더 비슷했다(추출본에 학명이 빠져 그 종이 어느 종인지는 확인하지 못함)[22]","[22] 전문·초록 추출본에서 비교 Suillus 종의 학명이 빠져 '비단그물버섯(S. luteus)'임을 확인할 수 없음")
rep('sections.cultivation',S['cultivation'],'body',"영국 구주소나무 조림지 16년 관찰에서는","영국 연구진의 구주소나무 조림지 16년 관찰에서는","[30] 초록은 조림지 위치를 밝히지 않고 저자 소속만 영국")
rep('sections.safety',S['safety'],'body',"1993/94년 폴란드 조사에서도 이 종의 수은은 갓 29–65 µg/kg 건조중으로 조사한 13종 가운데 가장 낮은 축이었다[6]","1993/94년 폴란드 조사에서도 이 종은 Chroogomphus rutilus·Armillariella mellea와 함께 조사한 13종 가운데 수은이 가장 낮은 3종에 들었고, 이 3종의 평균은 갓 29–65 µg/kg, 대 23–49 µg/kg 건조중이었다(종별 값은 초록에서 구분되지 않음)[6]","[6] 초록의 29–65 µg/kg 은 이 종 단독 값이 아니라 3종을 묶은 범위")
C={c['name']:c for c in d['compounds']}
rep('compounds.Bovinalkaloid A.activity_ko',C['Bovinalkaloid A'],'activity_ko',"분리한 4종 가운데 1 mg/mL에서 인삼 뿌리썩음병균(Fusarium solani) 균사 생장을 100% 억제한 화합물이 있었고 MIC 2.08 mM — 본문 추출본에 화합물 번호가 빠져 어느 화합물인지는 확인하지 못함(시험관)[12]","1 mg/mL에서 인삼 뿌리썩음병균(Fusarium solani) 균사 생장을 100% 억제해 분리한 4종 가운데 가장 강했고, MIC 2.08 mM, 4.16 mM에서 포자 발아 94.37% 억제(시험관; 표 1의 화합물 1 NMR 자료가 이 구조와 일치하고 억제율은 화합물 1–4 순서로 제시됨)[12]","[12] 전문 표 1(화합물 1 = 1-아세틸-3,7-다이하이드록시-β-카볼린)과 억제율 순서로 가장 강한 화합물이 보비날칼로이드 A 임을 확인")
rep('compounds.9-Hydroxycanthin-6-one.activity_ko',C['9-Hydroxycanthin-6-one'],'activity_ko',"네 화합물은 1 mg/mL에서 F. solani 균사 생장을 각각 100.00%·22.31%·37.59%·59.29% 억제(시험관)[12]","네 화합물(보비날칼로이드 A·B·C, 9-하이드록시칸틴-6-온)은 1 mg/mL에서 F. solani 균사 생장을 각각 100.00%·22.31%·37.59%·59.29% 억제했고, 이 화합물은 59.29%였다(시험관)[12]","화합물 순서를 원문(1–4)대로 밝힘")
A=d['assays']
a=[x for x in A if x['compound'].startswith('Monosaccharides')][0]
rep('assays[다당 Y-1].rationale',a,'rationale',"0.2 M 질산나트륨+0.01 M 인산이수소나트륨","0.2 M 질산나트륨+0.01 M 인산나트륨염(추출본에서 화학식 일부가 깨져 정확한 염은 확인하지 못함)","원문 추출본 'NaHPO' — 인산이수소나트륨인지 확정 불가")
a=[x for x in A if x['compound'].startswith('Widely')][0]
rep('assays[광범위 대사체].content',a,'content',"이 종·Gomphidius roseus·비단그물버섯 자실체에서","이 종·Gomphidius roseus·같은 속의 다른 1종(추출본에서 학명 확인 못함) 자실체에서","비교종 학명이 추출본에서 빠져 S. luteus 로 확정 불가")
a=[x for x in A if x['compound'].startswith('Mercury')][0]
rep('assays[총수은].conditions.detection',a['conditions'],'detection',"원자흡광 296 nm","원자흡광 296 nm(원문 표기)","원문이 296 nm 로 적음(통상 수은선 253.7 nm 와 다름) — 원문대로 두고 표기 명시")
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(ch,open('suillus-bovinus/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(ch))
