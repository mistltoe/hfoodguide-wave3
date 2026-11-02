import json,sys
p='dossier.json'; d=json.load(open(p))
S={s['key']:s for s in d['sections']}
changes=[]
def rep(where,obj,key,old,new,why):
    v=obj[key]
    assert old in v,(where,old[:40])
    obj[key]=v.replace(old,new); changes.append({"where":where,"before":old,"after":new,"why":why})

rep("sections.overview",S['overview'],'body',
 "국내 「식품 등의 생산실적」에는 개별인정형 건강기능식품 원료 '수국잎열수추출물'이 집계되며[25], 산수국 잎 열수추출물은 12주 사람 시험에서 피부 지표가 연구되었다[8].",
 "국내 「식품 등의 생산실적」에는 개별인정형 건강기능식품 원료 '수국잎열수추출물'이 집계되나[25], 이 원료의 기원 종(수국·산수국 계통)과 인정 기능성은 식약처 인정 원문으로 확인하지 못함. 이와 별개로 산수국 잎 열수추출물은 12주 사람 시험에서 피부 지표가 연구되었다[8].",
 "생산실적[25]은 품목명·금액만 있어 산수국 추출물[8]과의 동일성·인정 기능성을 뒷받침하지 않음(언론·개발사 보도만 있음) — 추정 연결을 분리")
rep("sections.biology",S['biology'],'body',
 "잎의 다이하이드로아이소쿠마린은 페닐프로파노이드 한 분자와 아세트산 세 분자가 축합해 생긴다는 생합성 경로가 표지 실험으로 제시되었다[8].",
 "하이드랑게놀은 페닐프로파노이드 한 분자와 아세트산 세 분자가 축합해 생긴다는 생합성 경로가 13C 표지 실험으로 제시되었다고 소개된다[8].",
 "[8] 전문 서론은 하이드랑게놀에 한정해 선행 표지 연구를 인용함(직접 실험 아님)")
rep("sections.processing",S['processing'],'body',
 "하이드랑게놀이 많은 수국차 추출물 건강기능식품이 체중 관리용으로 나왔다는 국내 논문 서술이 있으나[9], 식약처 인정 기능성 원문은 확인하지 못함.",
 "하이드랑게놀이 많은 수국차 추출물 건강기능식품이 체중 관리용으로 나왔다는 국내 논문 서술이 있으나[9], 이 제품 원료와 위 개별인정형 '수국잎열수추출물'의 관계, 그리고 그 원료의 기원 종(수국 또는 산수국 계통)과 식약처 인정 기능성 원문은 확인하지 못함. 산수국 잎 열수추출물 사람 시험[8]의 원료가 이 개별인정형 원료와 같은지도 공식 자료로 확인하지 못함.",
 "개별인정형 원료–산수국 추출물 연결은 작성자 추정. 생산실적은 품목명만 제공")
old_saf="2008년 6월 일본 쓰쿠바시 음식점에서 장식용 수국 잎을 먹은 8명이 30분 뒤 구토·어지럼증을, 오사카시에서 1명이 40분 뒤 구토·안면 홍조를 보였다(WebSearch 요약)[26]. 후생노동성은 7월 통지에서 이를 청산 식중독으로 안내했다가, 8월에 시안배당체 함유 근거가 불충분하다며 앞 통지를 폐지하고 요리에 수국 잎·꽃을 곁들이지 말라고 요청했다(WebSearch 요약)[26]."
new_saf="이와 성격이 다른 사례로, 2008년 6월 일본 이바라키현 쓰쿠바시와 오사카시 음식점에서 요리 장식으로 곁들인 관상용 수국의 생잎을 먹은 사람들이 식후 30–40분에 구토·어지럼증 등을 보였다(통지 원문은 열지 못했고 WebSearch 요약으로만 확인, 환자 수는 확인하지 못함)[26]. 후생노동성은 2008년 7월 1일 통지에서 이를 청산 식중독으로 안내했다가, 8월 18일 통지에서 수국의 시안배당체 함유 지견이 충분하지 않다며 앞 통지를 폐지하고 수국 잎·꽃 같은 유독 식물을 요리 장식으로 제공·섭취하지 말라고 요청했으며, 유독 성분은 충분히 밝혀지지 않았다고 적었다(WebSearch 요약)[26]. 즉 단맛 수국잎 생약 달임액 사례[2]와 관상 수국 생잎 사례[26] 모두 원인 성분은 확정되지 않았다."
rep("sections.safety",S['safety'],'body',old_saf,new_saf,
 "WebSearch 재확인 결과 환자 수(8명·1명)와 '안면 홍조'는 확인되지 않아 지움. 통지 날짜·폐지 사유를 검색 요약 일치 내용으로 맞추고, 감차 생약 사례와 관상 수국 생잎 사례를 구분")
C={c['name']:c for c in d['compounds']}
rep("compounds.Phyllodulcin.content_text",C['Phyllodulcin'],'content_text',
 "단맛 수국잎 메탄올 가속 용매 추출 최고 21.28 mg/g",
 "단맛 수국잎(var. thunbergii) 분말 메탄올 가속 용매 추출 최고 21.28 mg/g(기준 무게는 초록에 명시 없음)",
 "[3] 초록은 'mg/g' 만 적고 건물·생물 기준을 밝히지 않음")
rep("compounds.Hydrangenol.content_text",C['Hydrangenol'],'content_text',
 "산수국 잎 열수추출물 0.63 ± 0.05%[7], 임상용 열수추출물 7.7 mg/g[8]",
 "산수국 잎 열수추출물(건조 추출물 기준) 0.63 ± 0.05%[7], 임상용 열수추출물 7.7 mg/g(추출물 기준)[8]",
 "기준(잎이 아니라 추출물)을 밝힘 — 원문 대조")
src={s['n']:s for s in d['sources']}
rep("sources[3].title",src[3],'title',"Efficient bioconversion, extraction, and isolation processes","The establishment of efficient bioconversion, extraction, and isolation processes","PubMed 서지 제목과 맞춤")
rep("sources[26].title",src[26],'title',"원문은 열지 못했고 WebSearch 요약으로만 확인","원문 PDF는 네트워크 허용 목록 밖이라 열지 못했고, WebSearch 요약(후생노동성 통지 사본·지자체 게시물 검색 결과)으로 날짜·번호·폐지 사유만 확인",
 "검토자 WebSearch로 날짜·통지번호·폐지 사유 재확인")
rep("sources[33].title",src[33],'title',"원문은 열지 못했고(네트워크 허용 목록 밖) WebSearch 요약으로만 확인","원문은 열지 못했고(네트워크 허용 목록 밖) WebSearch 요약으로만 확인 — 검토자 재검색에서도 독성 성분 하이드라시아노사이드 A·2009–2010년 꽃 축제 단맛 차 구토 사례 기재가 같게 요약됨",
 "검토자 WebSearch 재확인")
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
