import json,sys
p='/home/user/hfoodguide-wave3/docs/materials/cyphomandra-betacea/dossier.json'
d=json.load(open(p))
changes=[]
def sec(k): return [s for s in d['sections'] if s['key']==k][0]
def rep(where,obj,key,old,new,why):
    v=obj[key]
    assert v.count(old)==1,(where,old)
    obj[key]=v.replace(old,new); changes.append({"where":where,"before":old,"after":new,"why":why})
o=sec('overview')
rep('sections.overview',o,'body',"사용 조건은 '사용가능부위 : 열매'라서 잎·줄기·뿌리는 이 목록으로 쓸 수 없다[1]",
 "사용 조건은 '사용가능부위 : 열매'이며, 잎·줄기 등 열매 외 부위는 이 목록에 올라 있지 않다[1]",
 "I1020 원자료에는 열매(및 페이스트) 두 행만 있고 잎·줄기·뿌리 '사용불가' 행은 없음 — 목록에 없음으로 정확히 씀")
b=sec('biology')
rep('sections.biology',b,'body',"한 꽃송이에서 1–6개의 타원형 열매","1–6개의 타원형 열매",
 "[2] 원문은 'It produces between 1 and 6 elliptical fruits'로 꽃송이당이라고 하지 않음")
r=sec('related_species')
rep('sections.related_species',r,'body',"Cocona(Solanum sessiliflorum)도 열매를 쓸 수 있는 원료로",
 "Cocona(Solanum sessiliflorum, 잎·열매)도 쓸 수 있는 원료로",
 "I1020 원자료에서 Cocona 사용가능부위는 '잎, 열매'")
g=sec('genetics')
rep('sections.genetics',g,'body',"나무토마토의 참조 유전체는 아직 공개되지 않았고, 2022년 중국 쓰촨농업대학 연구진이 PacBio 장독 서열분석으로",
 "2022년 논문 시점에 나무토마토의 참조 유전체는 공개되지 않았고, 그해 중국 쓰촨농업대학 연구진이 단일분자 실시간(SMRT) 장독 서열분석으로",
 "[6]은 2022년 시점 서술 — 시점을 밝힘; 상표명(PacBio) 대신 일반명")
# compounds
C={c['name']:c for c in d['compounds']}
rep('compounds.Delphinidin 3-rutinoside',C['Delphinidin 3-rutinoside'],'content_text',"열매 총 안토시아닌 8.5 mg/100 g 중 주요 안토시아닌[8]; 껍질(동결건조) Amber",
 "열매 총 안토시아닌 8.5 mg/100 g(생/건 기준 초록 미기재) 중 주요 안토시아닌[8]; 껍질 건물 기준 Amber",
 "[2] 원문은 'mg/100 g dry weight'(동결건조라고 하지 않음); [8] 초록은 기준을 밝히지 않음")
rep('compounds.Cyanidin 3-rutinoside',C['Cyanidin 3-rutinoside'],'content_text',"껍질(동결건조) Amber","껍질 건물 기준 Amber",
 "[2] 원문은 'mg/100 g dry weight'")
rep('compounds.beta-Cryptoxanthin',C['beta-Cryptoxanthin'],'content_text',"열매 총 카로티노이드 4.4 mg/100 g 중","열매 총 카로티노이드 4.4 mg/100 g(생/건 기준 초록 미기재) 중",
 "[8] 초록은 생/건 기준을 밝히지 않음")
rep('compounds.Ascorbic acid',C['Ascorbic acid'],'content_text',"에콰도르 육종 집단 90개체에서 78.29–420.16 mg/100 g(반사광도법, 시료 상태는 초록에 명확하지 않음)[10]",
 "에콰도르 육종 집단 90개체에서 78.29–420.16 mg/100 g 생과육(반사광도법; 결과 본문에는 상한이 428.19로 적혀 있음)[10]",
 "[10] 전문 Methods: 비타민 C는 생과육(FW) 100 g당으로 표시; 초록 420.16과 본문 428.19 불일치 병기")
d['sources'][9]['title']=d['sources'][9]['title'].replace("PMC8838755, 초록 확인","PMC8838755, 전문 확인")
assert '전문 확인' in d['sources'][9]['title']
# nutrients basis
n=d['nutrients'][0]
old=n['basis']; n['basis']="과육 100 g당(초록 숫자 그대로, 생/건 기준 초록 미기재)"
changes.append({"where":"nutrients[0].basis","before":old,"after":n['basis'],"why":"[28] 초록은 생/건 기준을 밝히지 않음(스페인어 원문 전문 확인 불가)"})
# processing animal dose
pr=sec('processing')
rep('sections.processing',pr,'body',"열매 추출물은 고지방식 비만 쥐에서","열매 추출물은 고지방식 비만 쥐에서 150–300 mg/kg 경구 투여 시",
 "[18] 초록의 용량 조건을 밝혀 동물 결과 일반화 방지")
# world notes
for w in d['world']:
    if w['country']=='에콰도르':
        w['note']=w['note'].replace("(논문이 인용한 값)","(논문 [5]가 카르치·임바부라 등 산지 주 기준으로 다른 문헌 2편을 인용한 2차 값, 원 통계 미확인)")
    else:
        w['note']=w['note'].replace("(리뷰가 인용한 값)","(리뷰 [2] 본문 서술, 원 통계 출처 미표기·미확인)")
changes.append({"where":"world[0-3].note","before":"(논문/리뷰가 인용한 값)","after":"2차 인용임과 원 통계 미확인을 명시","why":"[5] 전문은 4,500→7,600 ha(2015→2017, 70%)를 다른 문헌 인용으로, [2] 전문은 2019년 약 622 t·약 100 ha·40 농가를 출처 표기 없이 서술 — 값은 일치, 원 통계는 열 수 없음"})
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('/home/user/hfoodguide-wave3/docs/materials/cyphomandra-betacea/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
