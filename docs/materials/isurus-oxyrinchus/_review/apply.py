import json
p='/home/user/hfoodguide-wave3/docs/materials/isurus-oxyrinchus/dossier.json'
d=json.load(open(p))
S={s['key']:s for s in d['sections']}
changes=[]
def rep(where,obj,key,old,new,why):
    assert old in obj[key], (where,old)
    obj[key]=obj[key].replace(old,new); changes.append({"where":where,"before":old,"after":new,"why":why})
rep('sections.history',S['history'],'body',
 "2019년 CITES 제18차 당사국총회에서 청상아리와 긴지느러미청상아리가 부속서 II에 올랐고 2019년 11월 26일 발효되었다고 하나, 이는 검색 요약으로만 확인했다[7].",
 "청상아리가 CITES 부속서 II에 올라 있다는 점은 동료 심사 논문으로 확인된다[4, 6]. 2019년 제18차 당사국총회 제안 42로 긴지느러미청상아리와 함께 등재되어 2019년 11월 26일 발효되었다는 날짜는 검색 요약으로만 확인했다[7].",
 "부속서 II 등재 사실은 [4] 전문(Introduction)·[6] 초록이 직접 적고 있어 근거를 보강; 발효일은 [7] 원문(asmfc.org)·ccsbt.org 사본이 이 환경에서 열리지 않아 검색 요약 수준 유지")
rep('sections.history',S['history'],'body',"대만 시장·식당의 상어 살코기 548점","대만 시장·식당의 상어 살코기·지느러미 548점",
 "[27] 초록: 548점은 'shark filets and fins' 표본")
rep('sections.related_species',S['related_species'],'body',
 "Lamna nasus는 '비악상어'라는 이름으로는 '사용불가', 영문 'Porbeagle'이라는 이름으로는 '사용가능'으로 두 줄이 엇갈려 적혀 있다[1].",
 "Lamna nasus는 '비악상어'라는 이름으로는 '사용불가'(사유: 「식품의 기준 및 규격」 개정고시 제2018-8호로 멸종위기 야생생물의 식품원료 사용 금지), 영문 'Porbeagle'이라는 이름으로는 '사용가능'으로 두 줄이 엇갈려 적혀 있다[1].",
 "I1020_20261013.json 비악상어 행 USE_CND_STDR_CN 원문을 반영(지위 근거 명시)")
rep('sections.cultivation',S['cultivation'],'body',"자원은 주로 주낙(연승) 어업의 부수어획으로 잡히며","주낙(연승) 어업에 부수어획으로 자주 잡히며",
 "[10] 초록은 'frequently caught as bycatch in longline fisheries'라고만 함('주로'는 과장)")
rep('sections.biology',S['biology'],'body',"척추 나이테는 성숙한 수컷에서 해마다 한 쌍씩 생기는 것이 확인되었다[21].",
 "북동태평양에서 옥시테트라사이클린 표지 6년 뒤 다시 잡힌 성숙 수컷 1마리로 척추 띠쌍이 해마다 한 쌍씩 생기는 것이 검증되었고, 같은 해역 어린 개체는 해마다 두 쌍으로 검증된 바 있다[21].",
 "[21] 초록: 표본은 성숙 수컷 1마리, 어린 개체는 연 2쌍 — 일반화 방지")
rep('sections.biology',S['biology'],'body',"수은 동위원소 분석은 북동태평양 개체가 주로 중층(중심해) 먹이에 기대고 있음을 보였다[35].",
 "북동태평양의 청상아리·청새리상어·귀상어 근육 수은 동위원소(Δ199Hg 1.40–2.13‰)는 세 종이 주로 중층(중심해) 먹이에 기댐을 시사했고, 근육 총수은은 먹이 깊이가 깊을수록 높았다[35].",
 "[35] 초록 결과는 상어 3종을 묶은 것 — 청상아리 단독 결과처럼 쓰지 않도록 수정")
rep('sections.safety',S['safety'],'body',"미국 뉴잉글랜드 앞바다 개체도 2.65 ± 1.16 ppm이었다[11, 12].",
 "미국 뉴잉글랜드 앞바다 개체도 2.65 ± 1.16 ppm이었다(두 값 모두 초록에 건·습 기준 표기 없음)[11, 12].",
 "기준(생/건) 미표기를 명시; [14]의 건중량 값과 직접 비교하지 않도록")
rep('sections.processing',S['processing'],'body',
 "「건강기능식품의 기준 및 규격」의 알콕시글리세롤 함유 상어간유는 원재료를 '상어 간'으로만 적고 종을 정하지 않아, 청상아리 간이 실제로 쓰이는지는 확인하지 못함[32].",
 "「건강기능식품의 기준 및 규격」에서 스쿠알렌(2-19)과 알콕시글리세롤 함유 상어간유(2-21)는 원재료를 '상어 간'으로, 뮤코다당·단백(2-32)은 '상어' 등의 연골조직으로만 적고 종을 정하지 않아, 청상아리가 실제로 쓰이는지는 확인하지 못함[32].",
 "로컬 고시 원문 대조: '상어 간'은 2-19 스쿠알렌(1756행)·2-21(1811행) 두 곳, 상어 연골은 2-32(2165·2168행)")
C={c['name']:c for c in d['compounds']}
rep('compounds.Mercury',C['Mercury'],'content_text',
 "서적도대서양 2173.6 ± 1521.5 ng/g[11]; 미국 뉴잉글랜드 2.65 ± 1.16 ppm[12]; 북동대서양 0.74 ± 0.56 mg/kg(0.12–2.57)[3]",
 "서적도대서양 2173.6 ± 1521.5 ng/g(기준 미표기)[11]; 미국 뉴잉글랜드 2.65 ± 1.16 ppm(기준 미표기)[12]; 북동대서양 0.74 ± 0.56 mg/kg 습중량(0.12–2.57, n = 48; 총설 표 2가 [13]의 값을 인용)[3]",
 "[3] 표 2: 북동대서양 n = 48, 습중량 기준, 원 연구는 [13]; [11]·[12]는 초록에 기준 미표기")
n=d['nutrients'][0]
old=n['basis']; n['basis']="100 g당, 총설 표 1(스페인 자료 정리, 청상아리 열; 원 표는 g/100 g로만 적고 생·조리 상태를 밝히지 않음)[3]"
changes.append({"where":"nutrients[0].basis","before":old,"after":n['basis'],"why":"[3] 표 1에 생/조리 구분이 없음을 명시"})
s32=[s for s in d['sources'] if s['n']==32][0]
old=s32['title']
s32['title']="식약처 고시 제2026-43호 「건강기능식품의 기준 및 규격」 제3 — 2-19 스쿠알렌·2-21 알콕시글리세롤 함유 상어간유(원재료 '상어 간', 종 지정 없음), 2-32 뮤코다당·단백(상어 등 연골조직), 고시형 원료 전체에서 청상아리·Isurus 원재료 여부 대조(로컬 원문 docs/refs/MFDS/건강기능식품의기준및규격_2026-43_제1~제3.txt)"
changes.append({"where":"sources[32].title","before":old,"after":s32['title'],"why":"본문 수정에 맞춰 대조 범위 반영"})
s7=[s for s in d['sources'] if s['n']==7][0]
old=s7['title']; s7['title']=old.replace("cites.org 원문은 이 환경에서 열지 못함","cites.org·asmfc.org·ccsbt.org 원문은 이 환경에서 열지 못함(검토자 V2 재확인: 검색 요약에서 같은 날짜·제안 42 범위 확인)")
changes.append({"where":"sources[7].title","before":old,"after":s7['title'],"why":"검토 시 WebSearch 1회로 같은 요약 재확인, 원문은 네트워크 차단"})
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('/home/user/hfoodguide-wave3/docs/materials/isurus-oxyrinchus/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
