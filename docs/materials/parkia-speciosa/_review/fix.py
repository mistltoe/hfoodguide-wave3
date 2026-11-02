import json,sys
p='/home/user/hfoodguide-wave3/docs/materials/parkia-speciosa/dossier.json'
d=json.load(open(p,encoding='utf-8'))
S={s['key']:s for s in d['sections']}
changes=[]
def rep(where,obj,key,old,new,why):
    v=obj[key]
    assert v.count(old)==1,(where,old)
    obj[key]=v.replace(old,new)
    changes.append({"where":where,"before":old,"after":new,"why":why})
rep('sections.overview',S['overview'],'body',
 "bitter bean으로 불리고 말레이시아·인도네시아에서는 petai, 태국에서는 sator(sataw)라고 부른다[2, 3].",
 "bitter bean으로 불리고 말레이시아·인도네시아에서는 petai, 태국에서는 sator(sataw)라고 부른다[2, 3, 4].",
 "'bitter bean'은 [2]·[3]에 없고 [4](제목·서론)에 있어 출처 추가")
rep('sections.overview',S['overview'],'body',
 "사용 조건은 '사용가능부위 : 열매'라서 잎·뿌리·나무껍질은 이 목록으로 쓸 수 없다[1].",
 "사용 조건은 '사용가능부위 : 열매'로, 잎·뿌리·나무껍질은 이 행의 사용가능부위에 들어 있지 않다[1].",
 "I1020 원자료(세이터열매 행)는 사용가능부위만 적음 — 다른 부위의 금지를 단정하지 않도록 원문 범위로 좁힘")
rep('sections.history',S['history'],'body',
 "빈 꼬투리 메탄올 추출물은 L-NAME으로 고혈압을 유발한 쥐에서 혈압 상승을 막았다는 동물실험이 있다[25].",
 "빈 꼬투리 메탄올 추출물(800 mg/kg)은 L-NAME으로 고혈압을 유발한 쥐에서 혈압 상승을 막았다는 동물실험이 있다[25].",
 "[25] 초록: 경구 800 mg/kg — 동물실험 용량 명시로 과장 방지")
rep('sections.biology',S['biology'],'body',
 "꽃은 긴 꽃대 끝에 공 모양으로 매달려 아래로 처지며",
 "꽃은 꽃대 끝에 공 모양으로 매달려 아래로 처지며",
 "[3]은 'bulb-shaped and droop at the stalk ends'라고만 씀 — '긴'은 원문에 없음")
rep('sections.biology',S['biology'],'body',
 "표고버섯 같은 독특한 풍미가 있다고 설명된다[3].",
 "표고버섯 같은 독특한 풍미가 있다고 설명된다[3, 4].",
 "'납작한(flattened) 타원형'은 [4] 서론에 있고 [3]은 'elliptical'만 씀 — 출처 추가")
rep('sections.biology',S['biology'],'body',
 "이 박쥐는 식물 종마다 몸의 다른 부위에 꽃가루를 묻혀 다른 종 사이의 꽃가루 이동을 줄인다[16].",
 "이 박쥐를 함께 쓰는 식물들은 꽃 구조에 따라 박쥐 몸의 서로 다른 부위에 꽃가루를 묻혀 다른 종 사이의 꽃가루 이동을 줄인다[16].",
 "[16] 초록: 꽃가루 위치를 달리하는 주체는 식물(꽃 구조)이지 박쥐가 아님")
rep('sections.processing',S['processing'],'body',
 "이 발효에는 Lactobacillus plantarum이 우세했고,",
 "이 발효에는 Lactobacillus plantarum과 L. sanfranciscensis가 우세했고, L. plantarum KJ03을",
 "[18] 초록: 두 종이 함께 우세 — 한 종만 적은 것을 원문대로 고침")
rep('sections.processing',S['processing'],'body',
 "이를 종균으로 넣으면 5일 안에",
 "종균으로 넣으면 5일 안에",
 "위 수정에 따른 문장 정리")
rep('sections.processing',S['processing'],'body',
 "용매 추출 680 ppm, 수증기 증류 444 ppm으로 달랐다[8].",
 "용매 추출 680 ppm, 물 증류(hydrodistillation) 444 ppm으로 달랐다[8].",
 "[8] 초록은 hydrodistilled — 수증기 증류가 아니라 물 증류")
rep('sections.safety',S['safety'],'body',
 "씨앗 단백질(렉틴 포함)은 적혈구 응집과 림프구 분열 촉진 활성을 보였다[28, 33].",
 "시험관 실험에서 씨앗 단백질(렉틴 포함)은 적혈구 응집과 림프구 분열 촉진 활성을 보였다[28, 33].",
 "[28]·[33]은 분리 단백질의 시험관 실험 — 실험 조건 명시")
rep('sections.safety',S['safety'],'body',
 "그러나 신부전 사례(96건 중 4명 사망)가 정리된 젠콜중독은 젠콜콩(Archidendron) 섭취로 보고된 것이다[22].",
 "그러나 문헌 검토로 96건이 정리되고 그중 4명이 급성 신부전으로 사망한 젠콜중독은 젠콜콩(Archidendron pauciflorum) 섭취로 보고된 것이다[22].",
 "[22] 초록: 96건 전체가 젠콜중독 사례이고 4명이 급성 신부전으로 사망 — 96건을 '신부전 사례'로 쓴 것을 바로잡음, 학명은 [22] 표기")
rep('sections.safety',S['safety'],'body',
 "세이터 섭취로 인한 젠콜중독 사례 보고는 확인하지 못함.",
 "2025년 연구는 젠콜산 결정화를 일으키는 콩으로 세이터와 젠콜콩을 함께 들었지만, 세이터 섭취로 인한 젠콜중독 사례 보고는 확인하지 못함[21].",
 "[21] 초록이 세이터도 젠콜산 공급원으로 언급 — 반대 근거를 함께 적음")
C={c['name']:c for c in d['compounds']}
rep('compounds.Quercetin.content_text',C['Quercetin'],'content_text',
 "꼬투리 추출물 0.19±0.47 g/kg[12]",
 "꼬투리 추출물 0.19±0.47 g/kg[12]; 씨앗 메탄올 추출물에서는 역상 HPLC로 검출되지 않았다는 이전 보고도 있음[2]",
 "출처끼리 다름 — [2] 총설은 메탄올 추출물에서 퀘르세틴 등 미검출을 인용")
C['Quercetin']['source']=sorted(set(C['Quercetin']['source']+[2]))
rep('compounds.Quercetin.activity_ko',C['Quercetin'],'activity_ko',
 "씨앗 추출물의 항산화 활성과 상관[4]",
 "씨앗 추출물의 항산화 활성과 유의한 상관(가장 높은 상관은 총플라보노이드)[4]",
 "[4] 본문: DPPH·FRAP와 가장 높은 상관은 TFC")
rep('compounds.Gallic acid.activity_ko',C['Gallic acid'],'activity_ko',
 "씨앗 추출물의 항균 활성과 가장 높은 상관[4]",
 "씨앗 추출물의 항균 활성과 높은 상관(초록; 본문 상관표에서 가장 높은 것은 총페놀)[4]",
 "[4] 초록은 갈산과 높은 상관, 본문은 TPC(R²=0.933)가 최고 — '가장 높은'을 원문대로 고침")
A=d['assays']
rep('assays[0].compound_ko',A[0],'compound_ko',
 "퀘르세틴(갈산·루틴·캠페롤·카테킨·루테올린·미리세틴, 페놀산 5종 동시 확인)",
 "퀘르세틴(루틴·캠페롤·카테킨·루테올린·미리세틴과 함께 플라보노이드 6종, 갈산 등 페놀산 5종 동시 확인)",
 "[4] 본문: 갈산은 페놀산 5종에 속함 — 플라보노이드 목록에 넣은 오류")
rep('assays[0].conditions.standard',A[0]['conditions'],'standard',
 "Sigma-Aldrich 표준품; 머무름",
 "시판 표준품; 머무름",
 "상표(공급사)명 대신 일반명")
rep('assays[0].rationale',A[0],'rationale',
 "씨앗의 항산화 활성과 가장 높은 상관을 보인 플라보노이드 성분으로 산지 비교 지표로 쓰임;",
 "갈산과 함께 씨앗에서 가장 많은 성분이며 플라보노이드(총량)가 항산화 활성과 가장 높은 상관을 보여 산지 비교에 쓰임;",
 "[4] 본문: 최고 상관은 개별 퀘르세틴이 아니라 TFC")
d['_changes']=changes
json.dump(d,open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=2)
