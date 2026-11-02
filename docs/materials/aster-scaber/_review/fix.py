import json
p='dossier.json'; d=json.load(open(p))
S={s['key']:s for s in d['sections']}
changes=[]
def rep(key,old,new,why):
    b=S[key]['body']; assert old in b,(key,old); S[key]['body']=b.replace(old,new)
    changes.append({"where":f"sections.{key}","before":old,"after":new,"why":why})
rep('overview',"한국에서는 산에서 자라기도 하고 재배도 하는 산나물로, 잎을 '취나물'로 흔히 먹는다[4][5].",
 "한국에서는 산지에서 자라기도 하고 나물용 채소로 널리 재배하기도 한다[4][5]. '취나물'은 참취를 포함한 국화과 여러 종을 함께 부르는 이름이다[15][34].",
 "[4][5]는 '한국에서 재배하는 산채·나물용 채소'라고만 쓰고 '잎을 취나물로 먹는다'는 표현은 없음. '취나물'이 여러 종을 부르는 이름이라는 것은 [15][34]가 말함")
rep('overview',"잎과 지상부에는 클로로젠산과","참취(지상부 등)에는 클로로젠산과",
 "[4]·[5]는 시료 부위를 밝히지 않았고 [9]는 지상부라 '잎'으로 한정할 근거가 없음")
rep('overview',"학명은 Aster scaber가 널리 쓰이지만, Doellingeria scabra라는 이름으로 다루는 분류도 있다[3].",
 "학명은 Aster scaber가 널리 쓰이며 World Flora Online도 이를 정명으로 두는 것으로 검색 요약에서 확인했다[3]. 같은 종을 Doellingeria scabra (Thunb.) Nees라는 이름으로 함께 적는 논문도 있다[8].",
 "[3]은 원문을 열지 못한 검색 요약이고, 요약에 D. scabra 이명 처리는 나오지 않음. D. scabra 이름 사용은 [8](키워드 'Doellingeria scabra (Thunb.) Nees')로 뒷받침")
rep('history',"성분 연구는 1990년대 초 일본 연구진이 뿌리와 지상부의 트리테르펜 사포닌(스카베로사이드) 구조를 밝히면서 시작되었다[17][18][19].",
 "1990년대 초 일본 연구진은 뿌리와 지상부의 트리테르펜 사포닌(스카베로사이드) 구조를 잇달아 보고했다[17][18][19].",
 "[17][18][19]는 연작 III–V 편이어서 성분 연구의 '시작'을 뒷받침하지 않음(I·II편은 확인하지 못함)")
rep('related_species',"사용 부위를 달리해 각각 따로 올라 있으므로 참취 자료와 섞으면 안 된다[1].",
 "각각 따로 올라 있으므로(사용가능부위: 벌개미취·까실쑥부쟁이·쑥부쟁이는 잎, 개미취·옹굿나물·섬쑥부쟁이는 순) 참취 자료와 섞으면 안 된다[1].",
 "I1020 원자료에서 벌개미취·까실쑥부쟁이·쑥부쟁이는 참취와 같은 '잎'이라 '사용 부위를 달리해'는 틀림")
rep('related_species',"다섯 가지 산나물을 비교한 연구에서","다섯 가지 산채의 메탄올 추출물을 비교한 연구에서",
 "[23]은 메탄올 추출물 기준이고 비교 대상에 음나무·더덕 등 '취'가 아닌 산채도 들어 있음")
rep('related_species',"학명은 국내 목록이 Aster scaber Thunberg를 쓴다[1]. 2023년 World Flora Online 분류는 Aster scaber Thunb.(1784)를 정명으로, Doellingeria scabra (Thunb.) Nees(1832)를 이명으로 두었으나, 이는 검색 요약으로만 확인한 것이다[3]. Aster 속을 좁게 보는 분류에서는 참취를 Doellingeria 속으로 옮겨 다룬다[3].",
 "학명은 국내 목록이 Aster scaber Thunberg를 쓴다[1]. 2023년 12월 World Flora Online 스냅숏은 Aster scaber Thunb.를 정명으로 둔 것으로 검색 요약에서 확인했으나, 원문을 열지 못해 Doellingeria scabra의 처리 방식은 확인하지 못함[3]. 참취 농약 잔류 논문 가운데에는 Doellingeria scabra (Thunb.) Nees를 같은 종의 이름으로 키워드에 함께 적은 것이 있다[8].",
 "WFO 원문은 이 환경에서 열리지 않았고, 검색 요약에 나온 WFO 이명 목록에는 D. scabra가 없었음. 'Aster 속을 좁게 보는 분류' 설명은 [3]이 말하지 않음. 대신 [8] 키워드로 D. scabra 병기 사실만 남김")
rep('cultivation',"연구용 시료는 강원 양양(시장 구입, 6월 채취)과 전남 고흥 재배품 등에서 얻었다[4][5][6].",
 "연구용 시료는 강원 양양 시장에서 산 2019년 수확품[4], 2017년 6월 양양에서 채집한 시료[5], 2016년 전남 고흥 재배품[6] 등이었다.",
 "[4](2019년 양양 시장 구입)와 [5](2017년 6월 양양 채집, 시장 구입 아님)를 한 시료처럼 섞어 씀")
rep('genetics',"체세포배 발생을 통한 재생 체계는 형질전환이나 대량 증식의 기초 기술로 쓰일 수 있다[27]. ","",
 "[27] 초록은 재생 체계 확립만 말하고 형질전환·대량 증식 활용은 말하지 않음")
rep('safety',"참취의 기준 초과율은 8.2%로 파슬리·머위 다음으로 높았다[29].",
 "참취의 기준 초과율은 8.2%로 파슬리(23.1%)·Petasites hybridus(12.6%) 다음으로 높았다[29].",
 "[29] 원문은 Petasites hybridus로 적어 국내 머위(P. japonicus)와 같다고 단정할 수 없음 — 원문 학명과 수치로 바꿈")
rep('safety',"두 조사 모두 조사한 채소 전체의 추정 섭취량은 일일섭취허용량의 100% 미만으로 평가되었다[30][31].",
 "기준을 넘거나 검출된 농약의 추정 섭취량은 일일섭취허용량 대비 0.003–30.4%[30], 0.002–90.6%[31]로 모두 100% 미만이었다.",
 "[30]은 기준 초과 농약만, [31]은 검출 농약의 위해지수를 평가했으며 '채소 전체 섭취량' 평가가 아님 — 원문 범위로 바꿈")
# compounds
for c in d['compounds']:
    if c['name']=='Chlorogenic acid':
        old=dict(part=c['part'],content_text=c['content_text'])
        c['part']="시장 구입 참취(부위 표기 없음)의 70% 에탄올 추출물"
        c['content_text']="추출물 10.98 ± 0.04 mg/g(HPLC-PDA)[4]; 선행 연구(Arch Pharm Res 2009) 인용값 9.34 ± 0.11 mg/g — [4] 안에서 '건조중량'과 '메탄올 추출물' 기준이 함께 쓰여 기준이 불분명[4]"
        c['source']=[4]
        changes.append({"where":"compounds[Chlorogenic acid]","before":json.dumps(old,ensure_ascii=False),"after":json.dumps(dict(part=c['part'],content_text=c['content_text']),ensure_ascii=False),"why":"[4]는 시료를 'herb'라고만 써 지상부·잎을 밝히지 않음. 9.34 mg/g은 [15] 초록에 없고 [4]가 인용한 값이며, [4] 안에서 건조중량·메탄올 추출물 두 기준으로 따로 적힘"})
for a in d['assays']:
    if a['compound']=='Chlorogenic acid':
        o=a['part']; a['part']="참취(2019년 수확, 양양 시장 구입; 부위 표기 없음) 동결건조 분말의 70% 에탄올 추출물"
        changes.append({"where":"assays[Chlorogenic acid].part","before":o,"after":a['part'],"why":"[4] 원문은 부위를 밝히지 않음(herb); 2019년은 구입 연도가 아니라 수확 연도"})
    if a['compound']=='Caffeoylquinic acids':
        o=a['content']; a['content']="추출물 중 카페오일퀸산 비율 20.25–38.35%(조사한 7종 취나물 전체 범위, 참취만의 값 아님)[15]; 참취 5-O-카페오일퀸산 9.34 ± 0.11 mg/g(다른 논문이 인용한 값, 건조중량·추출물 기준 불분명)[4]"
        changes.append({"where":"assays[Caffeoylquinic acids].content","before":o,"after":a['content'],"why":"여러 종 범위 값임을 분명히 하고 인용값의 기준 불확실성 표시"})
for s in d['sources']:
    if s['n']==3:
        o=s['title']
        s['title']="World Flora Online 분류 스냅숏(2023년 12월) — Aster scaber Thunb. 정명 처리. ※ 원문 페이지는 이 작업 환경에서 열지 못했고 WebSearch 검색 요약으로만 확인함(Doellingeria scabra 처리는 확인하지 못함)"
        changes.append({"where":"sources[3].title","before":o,"after":s['title'],"why":"검색 요약으로 D. scabra 이명 처리·출판 정보(Fl. Jap. 316, Gen. Sp. Aster. 183)를 확인할 수 없음"})
    if s['n']==8:
        s['publisher']="Foods (MDPI, PubMed 초록·키워드 확인)"
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
