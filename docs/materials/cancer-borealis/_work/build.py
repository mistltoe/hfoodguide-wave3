import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
A = "2026-11-02"
E = {"instrument": "", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "", "injection": "", "sample_prep": "", "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""}

sections = [
 ("overview", "한눈에 보기",
  "북쪽은행게(Cancer borealis, 영어 Jonah crab)는 북아메리카 대서양 연안에 사는 단미류(Brachyura) 게로, 캐나다 노바스코샤에서 미국 플로리다까지 조간대부터 수심 800 m까지 분포한다[2]. "
  "식약처 「식품원료 목록」에는 '북쪽은행게'라는 이름의 수산물 원료로 올라 있고, 쓸 수 있는 부위는 따로 정하지 않았으며('-') 사용 조건 없이 '사용가능'이다[1]. "
  "같은 목록에 적힌 이명은 '조나게, Jonah crab'이다[1].\n\n"
  "예전에는 바다가재 통발 어업의 혼획물로 여겨졌으나, 남부 뉴잉글랜드의 바다가재 어획 감소와 새 시장 개척으로 값이 오르면서 이 게를 노리는 어업이 커졌다[2]. "
  "2025년 발표된 유전체 논문은 지난 10년간 미국 양륙량이 연평균 약 1,600만 파운드였다고 정리했다[2]. "
  "이 종은 위장 운동을 조절하는 구강위 신경계와 심장 신경절 연구에 오래 쓰인 신경과학 실험동물이기도 하지만, 이런 연구는 식품으로서의 효능 근거가 아니다[2, 19]. "
  "건강기능식품 고시형 원료의 원재료는 아니며, 국내 어획·수입 통계는 확인하지 못함."),
 ("history", "이용 역사",
  "미국 대서양 연안의 이 종 양륙량은 1990년대에 연 200만–300만 파운드 정도였고 2000년대 초부터 늘기 시작했다고 미국 대서양주해양수산위원회(ASMFC) 자료가 정리하고 있다(검색 요약으로만 확인, 원문 미열람)[24]. "
  "남부 뉴잉글랜드에서는 2000년 무렵부터 성체 수컷을 크기 기준으로 잡는 어업이 경제적으로 중요해졌다[3]. "
  "양륙량은 1996년 이후 꾸준히 늘었으며, 자원 상태가 밝혀지지 않은 채 어업이 빠르게 커져 남획 우려가 제기되었다[2]. "
  "이에 ASMFC는 2023년 미국 수역의 첫 자원평가를 실시했다[2]. "
  "주간 어업관리계획은 2015년 8월 승인되었고 메인주부터 버지니아주까지를 관리 구역으로 한다(검색 요약으로만 확인)[24].\n\n"
  "이 종은 1960년대에 이미 생화학 실험 재료로 쓰여, 정소뿐 아니라 근육·간·알에도 아데닌과 티민이 주를 이루는 특이한 DNA 중합체가 있음이 보고되었다[22]. "
  "이후 구강위 신경계의 리듬 생성 회로와 신경조절물질 연구의 대표 모델이 되었다[2, 19]. "
  "국내에 이 종이 들어와 먹기 시작한 시기와 경로는 확인하지 못함."),
 ("biology", "종·형태·생태",
  "북쪽은행게는 단미류 게로, 뉴펀들랜드에서 플로리다까지 수심 20–400 m, 수온 8–14 °C에서 산다는 서술도 있어 분포 범위 서술은 논문마다 조금 다르다[2, 3]. "
  "미국 북동부 대륙붕의 바닥 수온과 출현 자료를 맞춘 모형에서는 11–14 °C에서 가장 많이 나타났고 15 °C를 넘으면 출현 확률이 줄었다[6]. "
  "실험에서 심박수는 29 °C까지 오르다 멈췄고, 혈림프 산소는 7–20 °C에서 가장 높았으며 20 °C 위에서는 무산소 대사로 넘어가는 신호가 보였다[6].\n\n"
  "메인주 바위 해안에서는 밀물 때 조하대 개체가 조간대로 올라와 밀도가 썰물 때의 거의 두 배가 되었고, 육식성 고둥(Nucella lapillus)·초식성 고둥(Littorina littorea)·홍합류(Mytilus edulis)를 먹었다[13]. "
  "갈매기가 썰물 때 이 게를 잡아먹어 조간대 먹이그물에 연쇄 효과를 낸다는 실험 결과가 있다[13]. "
  "성게는 이 게의 냄새만으로도 작은 개체의 성장 속도가 40–42% 줄고 골격이 두꺼워졌다[14]. "
  "수컷 웅성선 호르몬(IAG) 발현은 가을에 가장 높고 겨울·봄에 낮아, 가을 짝짓기 활동과 겹칠 가능성이 제시되었다[3]. "
  "집게 안쪽의 이빨 모양 돌기는 바탕 큐티클보다 최대 10배 단단했다[15]."),
 ("related_species", "관련 종·이름",
  "식약처 「식품원료 목록」에는 같은 속 원료로 둥근은행게(C. pagurus, 이명 Brown crab·Edible crab), 던지네스게(C. magister, 이명 대짜은행게), 그리고 국문명 없이 'Atlantic rock crab'이라는 이름으로 올라 있는 C. irroratus가 있으며, 모두 조건 없는 '사용가능' 수산물이다[1]. "
  "같은 목록의 '은행게'는 학명이 Anatolikos japonicus로 적혀 있어 이 종과는 다른 원료다[1]. "
  "이 문서는 이들 근연종의 성분·안전 자료를 이 종의 자료로 옮기지 않았다[1].\n\n"
  "같은 해역에 사는 C. irroratus와 간췌장 소화효소를 비교한 1976년 연구가 있으나[12] 초록이 없어 결과는 확인하지 못함. "
  "익힌 게살의 열변성 단백질을 등전점 전기영동으로 비교한 연구에서는 북쪽은행게(Jonah)·rock crab(C. irroratus)·둥근은행게·던지네스게를 포함한 게 8종이 종마다 고유한 띠 무늬를 보였다[11]. "
  "이 띠 무늬는 성별·크기·성숙도·냉동 저장 기간·채취 부위가 달라도 바뀌지 않아 게살의 종 판별에 쓸 수 있었다[11]. "
  "구강위 신경 회로의 고온 반응을 던지네스게·유럽녹색게와 비교한 연구에서 신경펩타이드가 고온에서 리듬을 되살리는 효과는 공통이었지만 세포 수준의 기전은 다를 수 있었다[20]."),
 ("cultivation", "어획·자원 관리",
  "연구용 시료는 주로 상업 어선의 바다가재·농어류(black sea bass) 통발에 혼획된 성체 수컷에서 얻었다[3]. "
  "이 종의 양식 자료는 확인하지 못함. "
  "어업은 성체 수컷을 대상으로 하며, 주간 어업관리계획은 갑각폭 120.65 mm를 넘는 수컷을 잡도록 권고한다[3]. "
  "연구진은 수컷 번식 활동이 계절에 따라 달라지므로 수확 시기를 자원 관리에 고려해야 한다고 했다[3].\n\n"
  "2023년 벤치마크 자원평가는 자원을 네 단위로 나누었고, 남부 뉴잉글랜드 외해 자원이 2010–2021년 연안 전체 양륙량의 70–85%를 차지했다(검색 요약으로만 확인)[25]. "
  "같은 평가는 양륙량이 약 30배로 늘었다가 3년 새 51% 줄었고 자료가 부족해 자원 상태가 매우 불확실하다고 보았다(검색 요약으로만 확인)[25]. "
  "유전체 연구진은 참조 유전체가 저심도 전장유전체 분석으로 생물학적 자원 경계를 정하는 데 쓰일 수 있다고 했다[2]. "
  "간췌장에 감염하는 새 미포자충(Pseudohepatospora borealis)과 새 누디바이러스가 보고되어, 새로 생긴 어업의 잠재 위험으로 꼽혔다[4, 5]. "
  "수온 내성 연구진은 이 결과가 해양 온난화의 영향을 예측하는 데 필요하다고 했다[6]."),
 ("processing", "가공·이용",
  "이 종 가식부의 일반성분·영양성분을 정량한 논문은 PubMed에서 확인하지 못했으며, 국가표준식품성분표의 이 종 항목도 확인하지 못함. "
  "게 가공 공정에서 나오는 익힌 게살 다짐육은 기능성이 거의 없다고 여겨지던 값싼 부산물이다[10]. "
  "이 다짐육을 세척 횟수(물기만 뺌·1회·3회)와 소금 농도(0·2·4%)를 달리해 겔을 만든 결과, 세척한 시료가 물을 더 잘 붙잡았고 4% 소금은 보수력을 떨어뜨렸다[10]. "
  "3회 세척·소금 0% 조건이 가장 단단하고 보수력이 좋은 겔을 만들어 부가가치 제품 개발에 쓸 수 있다고 했다[10].\n\n"
  "익힌 게살은 등전점 전기영동 단백질 무늬로 종을 판별할 수 있어, 다른 게살과 섞이거나 바뀌는 것을 가리는 데 쓰일 수 있다[11]. "
  "같은 연구에서 두 가지 열처리 방식에 따라 단백질 무늬가 달랐다[11]. "
  "미국 연구진이 지역 시장에서 산 개체를 실험에 쓴 예가 여럿 있어, 산 채로 소매 유통되기도 함을 알 수 있다[8, 9]. "
  "국내에서 이 종을 원료로 한 제품의 생산실적은 확인하지 못함."),
 ("genetics", "유전 정보",
  "2025년 장문 해독과 근접 결합(Omni-C) 스캐폴딩으로 만든 염색체 수준 참조 유전체는 전체 691.19 Mb이며, 염색체 길이 스캐폴드 51개와 추가 콘티그 106개로 이루어졌다[2]. "
  "유전체 BUSCO 완전도는 90.8%였고, 예측된 단백질 암호 유전자는 24,830개(BUSCO 92.3%)였다[2]. "
  "반복서열은 1,649개 계열로, 초록에는 유전체의 48.27%, 본문에는 48.48%(333.66 Mb)로 적혀 있다[2]. "
  "해독 개체는 메인만에서 잡은 갑각폭 175 mm 수컷이었다[2]. "
  "신경계 관련 유전자 계열이 늘어나 있었고, 리간드 개폐 이온통로 374개를 비롯해 1,200개가 넘는 신경 관련 유전자 예측이 확인되었다[2].\n\n"
  "앞선 신경계 전사체 연구에서는 콘티그 42,766개, 고유 암호 서열 9,489개가 조립되었다[18]. "
  "DNA 재결합 속도 분석에서는 반복 수 2–100 범위의 반복 DNA가 검출되지 않아 무척추동물로는 드문 특징을 보였다[23]. "
  "웅성선 전사체에서 IAG 전장 cDNA는 928 nt였고, 눈자루 절제 뒤 가장 많이 발현된 유전자로 전사체의 최대 25%를 차지했다[3]. "
  "혈당상승호르몬(CHH)은 다른 게와 달리 한 가지 형태만 확인되었다[16]."),
 ("safety", "안전성",
  "식약처 「식품원료 목록」에서 북쪽은행게는 사용 조건 없는 '사용가능' 수산물 원료이며, 건강기능식품 고시형 원료가 아니어서 고시 섭취 시 주의사항은 없다[1]. "
  "이 종을 따로 다룬 국내 공공기관의 알레르기·잔류물질·중금속 안내는 확인하지 못함. "
  "갑각류 알레르기의 주요 원인 단백질인 트로포미오신 등 이 종의 알레르겐을 다룬 논문은 PubMed에서 확인하지 못함(검색어 'Cancer borealis' AND tropomyosin/allergen). "
  "마비성 패류독소·도모산이 이 종에서 검출되었다는 자료도 PubMed에서 확인하지 못했으며, 같은 속 다른 게의 자료는 옮기지 않았다(확인하지 못함).\n\n"
  "먹이 굴에 폴리에스터 미세섬유를 넣어 먹인 실험에서 이 게는 삼킨 섬유의 99%를 24시간 안에 내보냈고, 간췌장·생식소·혈림프로 옮겨 간 증거는 적었다[7]. "
  "반면 야외에서 잡은 개체에서는 아가미(5.2 ± 1.1)와 생식 조직(3.8 ± 1.5)에서 위(2.2 ± 0.8)·간췌장(0.6 ± 0.6)보다 미세플라스틱이 많았다(초록에 단위 표기 없음)[7]. "
  "간췌장 미포자충이 속한 무리(Enterocytozoonida)에는 사람을 감염하는 종도 있으나, 이 기생충 자체의 사람 감염 자료는 확인하지 못함[5]. "
  "누디바이러스의 사람 위해 자료도 확인하지 못함[4]. "
  "게를 구리 10 µM에 노출하자 2시간 뒤 혈림프 글루탐산이 줄었는데, 이는 게 자체의 독성 반응을 본 것으로 사람 섭취 안전성 자료가 아니다[8]."),
]

compounds = [
 dict(name="Glutamic acid", name_ko="글루탐산", **{"class": "아미노산"}, role="bioactive", part="혈림프", content_text="구리(10 µM CuCl2) 2시간 노출군 평균 11.8 µM; 대조군 수치는 본문에 따로 없음 [8]", activity_ko="글루타티온 합성의 전구물질로, 구리 노출 뒤 감소해 게의 구리 스트레스 초기 지표 후보로 제시되었다(게 생리 연구)[8]", source=[8]),
 dict(name="Taurine", name_ko="타우린", **{"class": "황 함유 아미노산"}, role="bioactive", part="혈림프", content_text="표지 없는 분석에서 동정(mzCloud 일치); 구리 노출군에서 유의하게 감소; 함량 수치는 확인하지 못함 [8]", activity_ko="연구진은 금속 해독·항산화와 관련된 물질로 해석했다(게 혈림프 관찰)[8]", source=[8]),
 dict(name="gamma-Aminobutyric acid", name_ko="감마아미노뷰티르산(GABA)", **{"class": "아미노산(신경전달물질)"}, role="bioactive", part="혈림프", content_text="표적 정량 대상 5종 중 하나; 대조군에서 1–2시간 사이 감소; 수치는 본문 텍스트에 없음 [8]", activity_ko="연구진은 감소 원인을 스트레스나 먹이 고갈 가능성으로 보았고 기전은 밝혀지지 않았다[8]", source=[8]),
 dict(name="Glutathione", name_ko="글루타티온", **{"class": "트라이펩타이드"}, role="bioactive", part="혈림프", content_text="표적 정량 대상 5종 중 하나(수치는 본문 텍스트에 없음) [8]", activity_ko="구리 이온을 결합해 환원 상태로 유지하는 해독 물질로 소개되었다(일반 설명)[8]", source=[8]),
 dict(name="Trigonelline", name_ko="트리고넬린", **{"class": "알칼로이드(삼투조절물질)"}, role="bioactive", part="혈림프", content_text="pH 7.8 해수 4시간 노출군/대조군 존재량 비 8.00배(p = 0.0035) — 절대 함량 아님 [9]", activity_ko="해양 생물에 흔한 삼투조절물질로 소개되었고, 해양 동물에서의 대사는 거의 밝혀지지 않았다[9]", source=[9]),
 dict(name="Pipecolic acid", name_ko="피페콜산", **{"class": "비표준 아미노산"}, role="bioactive", part="혈림프", content_text="pH 7.8 해수 4시간 노출 뒤 2.63배 감소(p = 0.0483) — 상대 존재량 [9]", activity_ko="해양 갑각류에서 대사 역할은 밝혀지지 않았다[9]", source=[9]),
 dict(name="Cyclo(prolylglycine)", name_ko="사이클로프롤릴글라이신", **{"class": "고리형 다이펩타이드"}, role="bioactive", part="혈림프", content_text="pH 7.8 해수 4시간 노출 뒤 2.26배 감소(p = 0.0166); 피크 면적이 커서 내인성 대사물 가능성 제기 [9]", activity_ko="쥐 뇌에서 알려진 내인성 펩타이드이며, 이 게에서의 기능은 확인되지 않았다(사람 효능 근거 아님)[9]", source=[9]),
 dict(name="Glycerophospholipids", name_ko="글리세로인지질", **{"class": "지질"}, role="nutrient", part="혈림프", content_text="이소프로판올 추출에서 지질 43종(산성 메탄올 추출 15종) 동정, 대조군 주석 화합물 324종 중 지질·지질 유사 분자 19.1% [9]", activity_ko="혈림프 지질의 상당 부분이 글리세로인지질과 지방산이었다[9]", source=[9]),
 dict(name="Chitin", name_ko="키틴", **{"class": "다당류(구조 성분)"}, role="nutrient", part="집게 큐티클(외골격)", content_text="키틴–단백질 섬유에 칼슘염이 박힌 구조; 돌기 쪽으로 갈수록 무기화 섬유 밀도 증가; 함량 수치는 확인하지 못함 [15]", activity_ko="집게 돌기의 경도는 바탕 큐티클보다 최대 10배 높았다(5종 공통 결과)[15]", source=[15]),
 dict(name="Calcium", name_ko="칼슘", **{"class": "무기질"}, role="nutrient", part="집게 큐티클(외골격)", content_text="에너지분산 X선 분광으로 원소 분포 측정; 경도와 칼슘·마그네슘 함량의 관계는 종마다 달랐고 인은 돌기 쪽으로 감소; 수치는 초록에 없어 확인하지 못함 [15]", activity_ko="외골격 무기화 성분으로 집게의 기계적 저항에 관여한다[15]", source=[15]),
 dict(name="Insulin-like androgenic gland hormone", name_ko="인슐린 유사 웅성선 호르몬(IAG)", **{"class": "펩타이드 호르몬"}, role="bioactive", part="웅성선(수컷)", content_text="가을 1.8 ± 0.5 × 10^8 copies/µg 총 RNA, 겨울 6.1 ± 2.2 × 10^6, 봄 6.2 ± 2.8 × 10^6, 여름 1.2 ± 0.7 × 10^8 (mRNA) [3]", activity_ko="수컷 성 성숙과 정자 형성에 관여하며, 웅성선에서만 발현되었다(게 생리 연구)[3]", source=[3]),
 dict(name="Crustacean hyperglycemic hormone", name_ko="갑각류 혈당상승호르몬(CHH)", **{"class": "신경펩타이드 호르몬"}, role="bioactive", part="눈자루 동샘", content_text="성체 수컷의 동샘에서 CHH·MIH·MOIH 가운데 가장 많은 형태; 수치는 초록에 없음 [16]", activity_ko="혈림프 포도당·탈피·이온 균형·생식을 조절하는 호르몬 계열이다[16]", source=[16]),
 dict(name="APSGFLGMRamide", name_ko="타키키닌 관련 펩타이드 Ia(CabTRP Ia)", **{"class": "신경펩타이드"}, role="bioactive", part="중장 상피 내분비세포·혈림프", content_text="며칠 굶긴 개체의 혈림프에서 검출, 먹이를 준 개체에서는 검출 안 됨 [17]", activity_ko="먹이 관련 행동을 호르몬처럼 조절할 가능성이 제시되었다(가설 단계)[17]", source=[17]),
 dict(name="alpha2-Macroglobulin", name_ko="알파2-마크로글로불린 유사 단백질", **{"class": "단백질분해효소 결합 단백질"}, role="bioactive", part="혈액(혈림프)", content_text="분자량 약 460 × 10^3(겔 여과 추정); 메틸아민에 비교적 둔감 [21]", activity_ko="트립신 활성 부위를 고분자 저해제로부터 보호하는 활성으로 확인되었다[21]", source=[21]),
]

assays = [
 {"role": "literature", "compound": "Glutamic acid", "compound_ko": "글루탐산", "part": "혈림프",
  "content": "구리 2시간 노출군 평균 11.8 µM [8]",
  "method": "동위원소 N,N-다이메틸 류신(iDiLeu) 유도체화 + DLLME·HLB 정제 후 UHPLC–Orbitrap MS/MS 절대 정량",
  "conditions": {"instrument": "UHPLC(Dionex UltiMate 3000) – Q-Exactive Orbitrap 질량분석기", "column": "Kinetex Polar C18, 2.6 µm, 100 Å, 100 × 4.6 mm", "mobile_phase": "A: 0.1% 폼산, B: 0.1% 폼산 함유 아세토나이트릴", "gradient": "0–7분 5–15% B, 7.1–10.5분 15–90% B, 10.5–12분 90% B, 12–12.5분 90–5% B, 12.5–15분 5% B", "flow": "", "temp": "", "detection": "양이온 모드, 유도체 m/z 200–500, 분해능 70K, 최대 주입 시간 100 ms, 포함 목록 기반 DDA, 충돌 에너지 30 eV, 분리 창 0.5 m/z", "injection": "", "sample_prep": "혈림프 400 µL를 산성 메탄올(메탄올:물:아세트산 90:9:1) 400 µL에 바로 넣어 18,000 rcf 15분 원심 후 상층 건조; 500 µg을 d0·d3 채널로 표지하고 내부표준 채널과 합친 뒤 DLLME(물 200 µL + 클로로폼/아세토나이트릴 1:10 200 µL, 2분 혼합, 4.5 × 1000 rcf 5분 원심)와 HLB 정제", "standard": "iDiLeu d6·d9·d12 채널 표지 표준품(각 10·1·0.5 µM)을 시료와 합쳐 내부 검량", "linearity": "3점 검량선(수치 적합도는 본문 텍스트에 없음)", "lod": "", "loq": "10 nM까지 검출·정량(도파민 예)", "recovery": "표지 GABA로 비교 시 HLB 적재 단계 손실 3% 미만, C18·SCX 총 손실 90% 초과"},
  "rationale": "구리 독성과 관련된 글루타티온 전구물질이라 게의 구리 스트레스 지표로 정량되었다. 가식부가 아닌 혈림프 생리 지표이며 식품 품질 지표는 아니다[8].",
  "source": [8], "url": "https://doi.org/10.3390/biom15091264", "source_kind": "paper"},
 {"role": "literature", "compound": "Trigonelline", "compound_ko": "트리고넬린(비표적 대사체 예)", "part": "혈림프",
  "content": "pH 7.8 해수 4시간 노출군/대조군 8.00배(p = 0.0035), 상대 존재량 [9]",
  "method": "단백질 침전(이소프로판올 또는 산성 메탄올) 후 HILIC LC–Q-TOF MS 비표적 대사체 분석",
  "conditions": {"instrument": "HPLC(Agilent 1290 Infinity II) – Agilent 6560 Q-TOF", "column": "Kinetex HILIC, 2.6 µm, 100 Å, 150 × 4.6 mm", "mobile_phase": "A: 25 mM 수산화암모늄 + 25 mM 아세트산암모늄 수용액, B: 아세토나이트릴", "gradient": "0–1분 95% B, 1–14분 95→65% B, 14–16분 65→40% B, 16–18분 40% B, 18–18.1분 40→95% B, 18.1–23분 95% B", "flow": "0.45 mL/min", "temp": "", "detection": "Dual AJS ESI 양이온 모드, m/z 50–1200, DDA로 MS2 수집", "injection": "2 µL", "sample_prep": "혈림프 200 µL + 찬 이소프로판올 또는 산성 메탄올 200 µL, −20 °C 하룻밤 뒤 16,000 × g 15분(4 °C) 원심, 상층 건조 후 아세토나이트릴/물(50:50) 300 µL로 재용해·17,000 × g 5분 원심", "standard": "표준품 검량 없음 — MS-DIAL 라이브러리로 주석, 총이온크로마토그램으로 정규화한 피크 면적 비교", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "해양 산성화 노출에 반응하는 혈림프 대사체를 찾는 비표적 분석에서 변화 폭이 가장 컸던 주석 화합물이다. 절대 함량이 아닌 상대 비이며, 식품 품질 지표는 아니다[9].",
  "source": [9], "url": "https://doi.org/10.1039/d5an00788g", "source_kind": "paper"},
 {"role": "literature", "compound": "Protein", "compound_ko": "단백질(익힌 게살 다짐육 겔)", "part": "익힌 게살 다짐육(가공 부산물)",
  "content": "세척 3회·NaCl 0% 처리에서 겔 강도·보수력 최고(수치는 초록에 없음) [10]",
  "method": "보수력·겔 강도·색·전기영동 단백질 양상 측정",
  "conditions": dict(E),
  "rationale": "가공 부산물인 익힌 다짐육의 겔 형성 능력을 보는 기능성 지표로 쓰였다. 전문 확인 못함 — 분석 조건 칸은 비워 두었다[10].",
  "source": [10], "url": "https://doi.org/10.1016/j.foodchem.2007.12.044", "source_kind": "paper"},
]

world = [
 {"country": "미국(북서대서양)", "metric": "landings_lb", "year": "최근 10년(2025년 발표 논문 기준)", "value": 16000000, "unit": "파운드", "note": "연평균 양륙량 약 1,600만 파운드; 논문 서론이 다른 자료를 인용한 값", "source": [2]},
 {"country": "미국(대서양 연안)", "metric": "landings_lb", "year": 2023, "value": 12400000, "unit": "파운드", "note": "약 1,240만 파운드, 어가 기준 1,410만 달러 — ASMFC 어업관리계획 검토 자료를 WebSearch 요약으로만 확인(원문 미열람)", "source": [24]},
]

S = lambda n, t, u, p, a=A: {"n": n, "title": t, "url": u, "publisher": p, "accessed": a}
sources = [
 S(1, "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 북쪽은행게(Cancer borealis) 1행(수산물, 부위 '-', 사용가능, 사용 조건 없음, 이명 '조나게, Jonah crab') 및 같은 속 둥근은행게(C. pagurus)·던지네스게(C. magister)·Atlantic rock crab(C. irroratus)과 은행게(Anatolikos japonicus) 행 — 로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json", "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "식품의약품안전처", "2026-10-13"),
 S(2, "Chromosome-level reference genome for the Jonah crab, Cancer borealis. G3 (Bethesda) 2025;15(1):jkae254", "https://doi.org/10.1093/g3journal/jkae254", "G3: Genes|Genomes|Genetics (PubMed 39501747, PMC11708212, 전문 확인)"),
 S(3, "Seasonal changes in the expression of insulin-like androgenic hormone (IAG) in the androgenic gland of the Jonah crab, Cancer borealis. PLoS One 2022;17(2):e0261206", "https://doi.org/10.1371/journal.pone.0261206", "PLoS One (PubMed 35113906, PMC8812979, 전문 확인)"),
 S(4, "A novel nudivirus from the Jonah crab (Cancer borealis: Brachyura). Virology 2026;626:111122", "https://doi.org/10.1016/j.virol.2026.111122", "Virology (PubMed 42966188, 초록만 확인)"),
 S(5, "Pseudohepatospora borealis n. gen. n. sp. (Microsporidia: Enterocytozoonida): A microsporidian pathogen of the Jonah crab (Cancer borealis). J Invertebr Pathol 2023;197:107886", "https://doi.org/10.1016/j.jip.2023.107886", "Journal of Invertebrate Pathology (PubMed 36646414, 초록만 확인)"),
 S(6, "Thermal boundaries of survival: A case study in a marine invertebrate. Comp Biochem Physiol A Mol Integr Physiol 2026;316:111994", "https://doi.org/10.1016/j.cbpa.2026.111994", "Comparative Biochemistry and Physiology Part A (PubMed 41825572, 초록만 확인)"),
 S(7, "Novel microplastic dosing approach of shellfish prey reveals highly efficient egestion rates by predatory crabs under environmentally realistic feeding scenarios. J Hazard Mater 2025;500:140480", "https://doi.org/10.1016/j.jhazmat.2025.140480", "Journal of Hazardous Materials (PubMed 41241977, 초록만 확인)"),
 S(8, "Isotopic N,N-Dimethyl Leucine-Based Mass Spectrometric Quantification of Metabolites Following Copper Exposure. Biomolecules 2025;15(9):1264", "https://doi.org/10.3390/biom15091264", "Biomolecules (PubMed 41008571, PMC12467339, 전문 확인)"),
 S(9, "Untargeted mass spectrometry to investigate ocean acidification in Cancer borealis using optimized metabolite extraction methods. Analyst 2026;151(5):1332-1341", "https://doi.org/10.1039/d5an00788g", "The Analyst (PubMed 41636650, PMC13050521, 전문 확인)"),
 S(10, "Gelation properties of previously cooked minced meat from Jonah crab (Cancer borealis) as affected by washing treatment and salt concentration. Food Chem 2008;109(2):332-9", "https://doi.org/10.1016/j.foodchem.2007.12.044", "Food Chemistry (PubMed 26003355, 초록만 확인)"),
 S(11, "Identification of species in cooked crabmeat by thin layer isoelectric focusing. J Assoc Off Anal Chem 1979;62(3):630-6", "https://pubmed.ncbi.nlm.nih.gov/39059/", "Journal of the AOAC (PubMed 39059, 초록만 확인)"),
 S(12, "A comparative study of the digestive enzymes in the hepatopancreas of Jonah crab (Cancer borealis) and Rock crab (Cancer irroratus). Comp Biochem Physiol B 1976;53(3):387-91", "https://doi.org/10.1016/0305-0491(76)90346-1", "Comparative Biochemistry and Physiology B (PubMed 3359, 초록 없음 — 제목만 확인)"),
 S(13, "Regulation of intertidal food webs by avian predators on New England rocky shores. Ecology 2007;88(4):853-63", "https://doi.org/10.1890/06-0593", "Ecology (PubMed 17536702, 초록만 확인)"),
 S(14, "Waterborne cues from crabs induce thicker skeletons, smaller gonads and size-specific changes in growth rate in sea urchins. Mar Biol 2009;156(5):1057-1071", "https://doi.org/10.1007/s00227-009-1150-0", "Marine Biology (PubMed 24489404, 초록만 확인)"),
 S(15, "Mechanical Resistance in Decapod Claw Denticles: Contribution of Structure and Composition. Acta Biomater 2020;110:196-207", "https://doi.org/10.1016/j.actbio.2020.04.037", "Acta Biomaterialia (PubMed 32438112, 초록만 확인)"),
 S(16, "Molecular cloning of crustacean hyperglycemic hormone (CHH) family members (CHH, molt-inhibiting hormone and mandibular organ-inhibiting hormone) and their expression levels in the Jonah crab, Cancer borealis. Gen Comp Endocrinol 2020;295:113522", "https://doi.org/10.1016/j.ygcen.2020.113522", "General and Comparative Endocrinology (PubMed 32492383, 초록만 확인)"),
 S(17, "Midgut epithelial endocrine cells are a rich source of the neuropeptides APSGFLGMRamide (Cancer borealis tachykinin-related peptide Ia) and GYRKPPFNGSIFamide (Gly1-SIFamide) in the crabs Cancer borealis, Cancer magister and Cancer productus. J Exp Biol 2007;210(Pt 4):699-714", "https://doi.org/10.1242/jeb.02696", "Journal of Experimental Biology (PubMed 17267655, 초록만 확인)"),
 S(18, "Deep sequencing of transcriptomes from the nervous systems of two decapod crustaceans to characterize genes important for neural circuit function and modulation. BMC Genomics 2016;17(1):868", "https://doi.org/10.1186/s12864-016-3215-z", "BMC Genomics (PubMed 27809760, PMC5096308, 초록만 확인)"),
 S(19, "How can motor systems retain performance over a wide temperature range? Lessons from the crustacean stomatogastric nervous system. J Comp Physiol A 2015;201(9):851-6", "https://doi.org/10.1007/s00359-014-0975-2", "Journal of Comparative Physiology A (PubMed 25552317, 초록만 확인)"),
 S(20, "Neuromodulator-induced temperature robustness in a motor pattern: a comparative study between two decapod crustaceans. J Exp Biol 2024;227(18):jeb247266", "https://doi.org/10.1242/jeb.247266", "Journal of Experimental Biology (PubMed 39211959, 초록만 확인)"),
 S(21, "An alpha 2-macroglobulinlike activity in the blood of chelicerate and mandibulate arthropods. J Exp Zool 1985;236(1):1-9", "https://doi.org/10.1002/jez.1402360102", "Journal of Experimental Zoology (PubMed 2414391, 초록만 확인)"),
 S(22, "Polymer similar to polydeoxyadenylate-thymidylate in various tissues of a marine crab. Science 1964;143(3613):1442-3", "https://doi.org/10.1126/science.143.3613.1442", "Science (PubMed 14107446, 초록만 확인)"),
 S(23, "DNA reassociation kinetics and chromosome structure in the crabs Cancer borealis and Libinia emarginata. Chromosoma 1975;50(3):243-57", "https://doi.org/10.1007/BF00283469", "Chromosoma (PubMed 1149573, 초록만 확인)"),
 S(24, "Atlantic States Marine Fisheries Commission — Jonah Crab FMP Review(FY2023) 및 Jonah Crab Interstate FMP(2015년 8월) — WebSearch 결과 요약으로만 확인(이 환경에서 asmfc.org 원문은 열지 못함)", "https://asmfc.org/uploads/file/672129d1JonahCrabFMPReview_FY2023.pdf", "Atlantic States Marine Fisheries Commission (WebSearch 요약만 확인)"),
 S(25, "Atlantic States Marine Fisheries Commission — Jonah Crab Stock Assessment Overview(2023년 10월) — WebSearch 결과 요약으로만 확인(원문 미열람)", "https://asmfc.org/wp-content/uploads/2025/01/JonahCrabStockAssmtOverview_Oct2023.pdf", "Atlantic States Marine Fisheries Commission (WebSearch 요약만 확인)"),
]

d = {
 "slug": "cancer-borealis", "name_ko": "북쪽은행게", "name_en": "Jonah crab", "scientific_name": "Cancer borealis",
 "aliases": ["조나게", "Jonah crab"],
 "sections": [{"key": k, "title": t, "body": b} for k, t, b in sections],
 "compounds": compounds, "markers": [], "assays": assays, "nutrients": [], "production": [], "world": world,
 "gi": [], "orgs": [], "sources": sources,
}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for k, t, b in sections:
    print(k, len(b))
