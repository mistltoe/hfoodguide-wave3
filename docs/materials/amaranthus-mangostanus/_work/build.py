import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
A = "2026-11-02"
MF = "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020"
def pm(pmid, t, j, doi, pmc=None, note="초록 확인"):
    url = f"https://pmc.ncbi.nlm.nih.gov/articles/{pmc}/" if pmc else f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
    d = f", doi:{doi}" if doi else ""
    return {"title": f"{t}. {j} (PMID {pmid}{d}; {note})", "url": url, "publisher": "PubMed" + (" / PMC" if pmc else ""), "accessed": A}
S = [
 {"title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 비름 4개 원료명 행: 비름순(부위 순)·비름분말(부위 순)·비름오일(부위 순)·절임비름나물(부위 '-'). 대분류 식품원료(A코드), 중분류 식물, 학명 'Amaranthus mangostanus L. / Amaranthus inamoenus Willd. / Amaranthus inamoenus f. viridis Makino', 영문명 Edible amaranth, 다른 이름 '비름나물, 새비름, 참비름, 개비름', 사용 조건 '사용가능', 조건 내용 '사용가능부위 : 순'. 로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json", "url": MF, "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
 {"title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 같은 속(Amaranthus) 다른 원료 행: 개비름잎(A. lividus L.; 다른 이름 '비름'; 사용가능부위 : 잎)·눈비름순(A. deflexus L.; 순)·아마란스(A. hypochondriacus / A. cruentus / A. caudatus / A. edulis / A. hybridus L.; 다른 이름 '색비름'; 잎, 씨앗)·청비름(A. viridis; 다른 이름 '푸른비름, 비름'; 잎, 씨앗)·가시비름(A. spinosus L.)·긴털비름(A. hybridus L.)·미국비름(A. albus)·Amaranthus dubius 등, 모두 사용가능. 로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json", "url": MF, "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
 pm("32089716", "Amaranthus mangostanus L. Inhibits the Differentiation of Osteoclasts and Prevents Ovariectomy-Induced Bone Loss", "Evid Based Complement Alternat Med 2020;2020:1927017", "10.1155/2020/1927017", "PMC7029261", "전문 확인"),
 pm("27849041", "Stage-dependent stoichiometric homeostasis and responses of nutrient resorption in Amaranthus mangostanus to nitrogen and phosphorus addition", "Sci Rep 2016;6:37219", "10.1038/srep37219", "PMC5110967", "전문 확인"),
 pm("30861100", "Effects of body size and root to shoot ratio on foliar nutrient resorption efficiency in Amaranthus mangostanus", "Am J Bot 2019;106(3):363-370", "10.1002/ajb2.1246"),
 pm("23442611", "The effects of host defence elicitors on betacyanin accumulation in Amaranthus mangostanus seedlings", "Food Chem 2012;134(4):1715-1718", "10.1016/j.foodchem.2012.03.129"),
 pm("19016328", "Total phenolics level, antioxidant activities and cytotoxicity of young sprouts of some traditional Korean salad plants", "Plant Foods Hum Nutr 2009;64(1):25-31", "10.1007/s11130-008-0092-x"),
 pm("28918593", "Decline patterns and risk assessment of 10 multi-class pesticides in young sprout amaranth (Amaranthus mangostanus) under greenhouse growing conditions", "Environ Sci Pollut Res Int 2017;24(32):24880-24895", "10.1007/s11356-017-0135-7"),
 pm("31115806", "Cellular distribution of cadmium in two amaranth (Amaranthus mangostanus L.) cultivars differing in cadmium accumulation", "Environ Sci Pollut Res Int 2019;26(22):22147-22158", "10.1007/s11356-019-05390-w"),
 pm("28043071", "Use of low-calcium cultivars to reduce cadmium uptake and accumulation in edible amaranth (Amaranthus mangostanus L.)", "Chemosphere 2017;171:588-594", "10.1016/j.chemosphere.2016.12.085"),
 pm("29860158", "Response of edible amaranth cultivar to salt stress led to Cd mobilization in rhizosphere soil: A metabolomic analysis", "Environ Pollut 2018;241:422-431", "10.1016/j.envpol.2018.05.018"),
 pm("32179214", "Biological mechanisms of cadmium accumulation in edible Amaranth (Amaranthus mangostanus L.) cultivars promoted by salinity: A transcriptome analysis", "Environ Pollut 2020;262:114304", "10.1016/j.envpol.2020.114304"),
 pm("24785711", "Sodium chloride salinity reduces Cd uptake by edible amaranth (Amaranthus mangostanus L.) via competition for Ca channels", "Ecotoxicol Environ Saf 2014;105:59-64", "10.1016/j.ecoenv.2014.04.005"),
 pm("38366045", "Assessment of health risks associated with prediction of vegetable inorganic arsenic concentrations given different soil properties", "Environ Geochem Health 2024;46(3):71", "10.1007/s10653-023-01843-x"),
 pm("29043585", "Evaluation of leafy vegetables as bioindicators of gaseous mercury pollution in sewage-irrigated areas", "Environ Sci Pollut Res Int 2018;25(1):413-421", "10.1007/s11356-017-0438-8"),
 pm("20355105", "Stability of hydroperoxide lyase activity from Amaranthus tricolor (Amaranthus mangostanus L.) leaves: influence of selected additives", "J Sci Food Agric 2010;90(5):729-734", "10.1002/jsfa.3874"),
 pm("36473054", "Chromosome-scale Amaranthus tricolor genome provides insights into the evolution of the genus Amaranthus and the mechanism of betalain biosynthesis", "DNA Res 2023;30(1)", "10.1093/dnares/dsac050", None, "초록 확인 — A. tricolor 자료"),
 pm("36933838", "Effects of exogenous calcium on cadmium accumulation in amaranth", "Chemosphere 2023;326:138435", "10.1016/j.chemosphere.2023.138435", None, "초록 확인 — 재료 Amaranthus tricolor L."),
 pm("34206088", "Amaranth Supplementation Improves Hepatic Lipid Dysmetabolism and Modulates Gut Microbiota in Mice Fed a High-Fat Diet", "Foods 2021;10(6):1259", "10.3390/foods10061259", "PMC8229566", "전문 확인 — 페루산 곡물(유사곡류) 아마란스 분말, 이 종 자료 아님"),
 pm("24314897", "Enhancement of Cd phytoextraction by two Amaranthus species with endophytic Rahnella sp. JN27", "Chemosphere 2014;103:99-104", "10.1016/j.chemosphere.2013.11.040"),
 pm("30889400", "Mineral elements uptake and physiological response of Amaranthus mangostanus (L.) as affected by biochar", "Ecotoxicol Environ Saf 2019;175:58-65", "10.1016/j.ecoenv.2019.03.039"),
 pm("36529009", "Three typical microplastics affect the germination and growth of amaranth (Amaranthus mangostanus L.) seedlings", "Plant Physiol Biochem 2023;194:589-599", "10.1016/j.plaphy.2022.12.007"),
 pm("33609242", "Nitrogen fertilizer management affects remobilization of the immobilized cadmium in soil and its accumulation in crop tissues", "Environ Sci Pollut Res Int 2021;28(24):31640-31652", "10.1007/s11356-021-12868-z", None, "초록 확인 — 재료 edible amaranth 'Liuye'"),
 pm("22325338", "Phytoavailability of heavy metals in tidal flat soils after fresh water leaching", "Ecotoxicol Environ Saf 2012;79:22-27", "10.1016/j.ecoenv.2012.01.015"),
 pm("23431799", "[Transfer characteristics of cadmium in soil-vegetable-insect food chain]", "Ying Yong Sheng Tai Xue Bao 2012;23(11):3116-3122", None, None, "중국어 논문, 영문 초록 확인"),
 pm("31679873", "Cadmium absorption and translocation of amaranth (Amaranthus mangostanus L.) affected by iron deficiency", "Environ Pollut 2019;256:113410", "10.1016/j.envpol.2019.113410"),
 pm("11495019", "Dissipation of epoxiconazole in the paddy field under subtropical conditions of Taiwan", "J Environ Sci Health B 2001;36(4):409-420", "10.1081/PFC-100104185"),
]
for i, s in enumerate(S, 1):
    s["n"] = i
sources = [{"n": s["n"], "title": s["title"], "url": s["url"], "publisher": s["publisher"], "accessed": s["accessed"]} for s in S]

sections = [
 {"key": "overview", "title": "한눈에 보기", "body":
  "비름(Amaranthus mangostanus L.)은 비름과 비름속의 한해살이 잎채소로, 영어로는 edible amaranth라 부르고 우리나라에서는 어린순을 데쳐 나물로 먹는다[1, 3]. 한국에서 'bireum'으로 알려져 있고, 빨리 자라고 영양가가 있어 아시아에서 널리 재배된다는 기술이 있다[3]. 중국 연구에서는 비타민·칼슘·인·철이 풍부해 흔히 먹는 채소라고 소개했다[4].\n\n"
  "식약처 「식품원료 목록」에는 비름순·비름분말·비름오일·절임비름나물 네 원료명이 식품원료(A코드)로 올라 있고, 사용 조건은 모두 '사용가능', 조건 내용은 '사용가능부위 : 순'이다[1]. 따라서 일반 식품에 쓸 수 있는 부위는 순이며, 같은 목록에서 잎·씨앗을 함께 허용하는 아마란스와는 별개의 원료다[1, 2]. 목록의 학명란에는 A. inamoenus Willd.와 A. inamoenus f. viridis Makino가 이명으로 함께 적혀 있다[1]. 건강기능식품 고시형 원료가 아니어서 지표성분 기준은 없다[1].\n\n"
  "연구는 식품 기능성보다 카드뮴 흡수·축적, 중금속·농약 잔류 같은 재배 안전 쪽이 많다[9, 10, 14]. 세포·동물 실험에서 파골세포 분화 억제가 보고되었으나 사람 자료는 확인하지 못함."},
 {"key": "history", "title": "이용의 역사", "body":
  "비름을 나물로 먹어 온 국내 전통 이용의 시기·문헌 기록은 1차 출처로 확인하지 못함. 식약처 목록에는 비름나물·새비름·참비름·개비름이 이 원료의 다른 이름으로 적혀 있어, 여러 지역 이름으로 불려 온 것을 엿볼 수 있다[1]. 소금에 절인 '절임비름나물'이 별도 원료명으로 올라 있는 것도 나물로 먹는 관행을 반영한다[1].\n\n"
  "국내 연구에서는 비름 어린순을 전통 한국 샐러드 식물 11종의 하나로 다루었다[7]. 국내 시장에서 산 말린 비름으로 추출물을 만든 동물 연구도 있어, 말린 비름이 유통되고 있음을 보여 준다[3]. 시설 재배한 어린순 비름의 농약 잔류를 국내에서 조사하고 한국 소비자 기준으로 위해성을 평가한 연구도 있다[8].\n\n"
  "중국에서는 흔한 채소로 소개되며, 대만에서는 벼 수확 뒤 뒷그루로 공심채와 함께 비름을 심어 잔류 농약을 조사했다[4, 27]. 원산지와 전파 경로에 관한 1차 자료는 확인하지 못함."},
 {"key": "biology", "title": "식물학적 특징", "body":
  "비름은 비름과에 속하는 한해살이풀이다[4]. 중국 온실 시험에서 씨앗 한 알의 무게는 평균 0.5–1.0 mg으로 매우 작았고, 천립중은 0.7 g으로 계산에 쓰였다[4]. 같은 시험에서 발아 뒤 65일까지를 유묘기, 104일까지를 개화기, 122일 무렵을 종자 성숙기로 나누었다[4].\n\n"
  "잎의 질소 농도는 생육 단계와 관계없이 건물 1 g당 24.4–25.7 mg으로 비슷했으나, 인 농도는 유묘기 2.55 mg에서 개화기 9.17 mg으로 크게 달라졌다[4]. 개화기에는 늙은 잎의 질소 51.3%와 인 55.9%를, 종자 성숙기에는 인 82.6%를 회수해 다시 썼다[4]. 몸집이 큰 개체일수록 잎 양분 회수 효율이 높고, 뿌리 비중이 클수록 낮았다[5].\n\n"
  "붉은 색소 베타시아닌은 빛에서 더 많이 쌓였고, 메틸자스모네이트와 에틸렌 처리로 늘었다[6]. 잎은 13-히드로퍼옥시드 분해효소(HPL) 활성이 특히 높은 재료로 보고되었다[16]. 꽃·열매 형태와 국내 근연종을 가르는 검색 형질은 확인하지 못함."},
 {"key": "related_species", "title": "같은 속의 다른 종", "body":
  "식약처 목록에는 비름속 여러 종이 각각 다른 원료명으로 올라 있다[2]. 아마란스(A. hypochondriacus·A. cruentus·A. caudatus 등)는 잎·씨앗, 눈비름(A. deflexus)은 순, 개비름(A. lividus)은 잎이 사용가능 부위다[2]. 비름(A. mangostanus)은 순만 허용된다[1].\n\n"
  "이름이 겹치는 점에 주의해야 한다[1, 2]. 비름의 다른 이름에 '개비름'이 있지만 목록에는 학명이 다른 개비름잎(A. lividus)이 따로 있고, 그 원료의 다른 이름은 '비름'이다[1, 2]. 청비름(A. viridis)도 다른 이름에 '비름'이 들어 있어, 이름만으로 원료를 판단하면 섞일 수 있다[2].\n\n"
  "A. tricolor와의 관계는 문헌마다 다르다[16, 18]. 한 논문은 제목에 'Amaranthus tricolor (Amaranthus mangostanus L.)'라고 써 두 이름을 같은 식물로 다루었다[16]. 그러나 식약처 목록의 이명란에는 A. tricolor가 없고, 국제 식물명 목록에서의 이명 처리는 확인하지 못함. 이 문서에서 A. tricolor 자료는 그 이름을 밝혀 따로 적었다[17, 18].\n\n"
  "곡물 아마란스 분말을 고지방 식이 생쥐에 먹인 연구는 페루산 유사곡류를 쓴 것이어서 비름 잎채소 자료로 볼 수 없다[19]. 카드뮴 정화 연구에서는 A. hypochondriacus와 비름을 함께 고축적 식물로 시험했다[20]."},
 {"key": "cultivation", "title": "재배와 생산", "body":
  "비름의 국내 재배면적·생산량 통계는 통계청·농식품부 자료에서 확인하지 못함. 국내에서는 온실에서 어린순 비름을 길러 농약 10종의 감소 양상을 조사했고, 수확 3·7·10일 시료를 분석했다[8].\n\n"
  "중국에서는 품종 간 카드뮴 축적 차이를 이용한 재배 연구가 많다[10, 11]. 오염 토양에서 15개 품종의 카드뮴 농도는 약 6배 차이가 났고, 칼슘·아연 농도가 높을수록 카드뮴도 높았다[10]. 저축적 품종 'Quanhong'과 고축적 품종 'Liuye'를 비교한 연구에서 염분 처리는 뿌리권의 이동성 카드뮴을 각각 2.78배, 4.36배 늘렸다[11]. 'Liuye'에 암모늄태 질소를 주면 질산태보다 줄기·잎 카드뮴이 높아져(건물 기준 6.92→14.92 mg/kg) 질산태 질소 사용이 권장되었다[23].\n\n"
  "염분이 남은 간척지 토양 시험에서는 내염성 비름 품종을 썼고, 염분이 가장 낮은 두 처리에서 먹는 부위의 중금속은 식품 허용 기준보다 낮았다[24]. 바이오차를 양액에 2.6 g/L 넘게 넣으면 뿌리 세포막·DNA 손상이 나타났다[21]. 미세플라스틱은 종류·농도에 따라 싹과 뿌리 생장을 억제했다[22]. 수경 재배에서 뿌리의 카드뮴 흡수는 처음 150분 안에 90–93%가 일어났고, 철 결핍은 흡수를 높였다[26]."},
 {"key": "processing", "title": "가공과 이용", "body":
  "식약처 목록에는 생순 외에 비름분말·비름오일·절임비름나물이 가공 원료명으로 올라 있으며, 모두 사용가능부위는 순이다[1]. 비름오일의 제조 방법이나 국내 유통 실태는 확인하지 못함. 식약처 「식품 등의 생산실적」 품목 표에서 비름을 원료로 한 건강기능식품 생산 기록은 찾지 못했다(확인하지 못함).\n\n"
  "연구용 가공 사례로, 국내 시장의 말린 비름을 50% 에탄올로 1:10(무게/부피) 24시간 추출해 동결건조한 추출물이 있다[3]. 이 추출물의 UPLC-MS 분석에서 플라보놀인 캠페롤이 확인되었다[3]. 어린순 메탄올 추출물은 다른 샐러드 식물과 함께 총 페놀·항산화 활성을 비교받았다[7].\n\n"
  "잎에서 얻은 HPL 효소는 향료 산업용으로 연구되었다[16]. 미세소체 HPL에 자당·트레할로스를 100 g/L 넣고 동결건조하면 활성이 거의 100% 남았지만, 넣지 않으면 약 20%만 남았다[16]. 자당을 넣은 동결건조품은 −20 °C에서 40일 동안 활성을 유지했다[16]."},
 {"key": "genetics", "title": "유전체와 성분 조절", "body":
  "A. mangostanus라는 이름으로 발표된 유전체 해독 자료는 확인하지 못함. 비름과 같은 식물로 다루기도 하는 A. tricolor는 장독 서열과 염색질 접촉 지도(Hi-C)를 함께 써서 염색체 수준 유전체가 만들어졌다[17]. 이 유전체는 520 Mb이며 콘티그의 99.58%가 17개 염색체에 고정되었고, 단백질 암호 유전자 27,813개가 주석되었다[17]. A. tricolor는 Albersia 아속의 첫 참조 유전체이며, 전장 유전체 중복을 겪은 것으로 추정되었다[17]. 붉은 잎에서는 베타레인 합성 유전자 DODAα1과 CYP76ADα1이 녹색 잎보다 많이 발현되었다[17].\n\n"
  "비름(A. mangostanus) 자체로는 카드뮴과 염분에 대한 유전자 발현 연구가 있다[12]. 고축적 품종 'Liuye'는 염분 처리에서 차등 발현 유전자 3,224개(뿌리 1,119, 잎 2,105)를 보여 저축적 품종 'Quanhong'(848개)보다 훨씬 많았다[12]. 고축적 품종 뿌리에서는 유기산 운반체(ALMT) 유전자 발현이 2.71–3.94배 늘었다[12]. 염분은 칼슘 통로 경쟁을 통해 카드뮴 흡수를 32–36% 줄이기도 했다[13]."},
 {"key": "safety", "title": "안전성과 사용 조건", "body":
  "식약처 목록에서 비름은 '사용가능' 원료이며 조건은 '사용가능부위 : 순'이다[1]. 건강기능식품 고시형 원료가 아니어서 고시 섭취 시 주의사항은 없다[1]. 국내 공공기관의 알레르기 경고 자료는 확인하지 못함.\n\n"
  "[중금속] 비름은 카드뮴을 잘 쌓는 채소로 연구된다[9, 20]. 수경 재배에서 고축적 품종은 뿌리 950, 줄기 305, 잎 205 mg/kg까지, 저축적 품종은 각각 269, 62.9, 74.8 mg/kg까지 카드뮴을 쌓았다(초록에 생·건물 기준 명시 없음)[9]. 토양 시험에서 기관별 카드뮴은 줄기 > 뿌리 > 잎 순이었다[25]. 대만 연구는 비름을 무기비소 노출 위험이 큰 채소로 보았고, 토양 총비소와 점토 함량이 주요 예측 인자였다[14]. 하수 관개지에서는 잎이 대기 중 기체 수은을 흡수할 수 있음이 보고되었다[15].\n\n"
  "[농약] 국내 시설 재배 어린순 비름에서 조사한 농약의 이론적 최대 일일섭취량은 일일섭취허용량 대비 기준(80%) 이하였고, 디페노코나졸만 80.92%로 약간 넘었다[8].\n\n"
  "[질산염·옥살산] 이 종의 먹는 부위에서 질산염·옥살산 함량을 정량한 자료는 확인하지 못함. 'Liuye' 품종 뿌리가 옥살산 등 유기산을 분비한다는 보고는 있으나 먹는 부위 함량은 아니다[23]. A. tricolor는 칼슘옥살산 결정이 많은 채소로 보고되었으나 다른 학명 자료다[18].\n\n"
  "[세포·동물] 비름 추출물은 세포에서 파골세포 분화를 억제하고 난소절제 생쥐의 골 손실을 줄였으나 사람 효과는 확인하지 못함[3]."},
]

compounds = [
 {"name": "Betacyanin", "name_ko": "베타시아닌", "class": "베타레인 색소", "role": "bioactive", "part": "유묘(어린 싹)", "content_text": "초록에 절대 함량 없음; 빛에서 증가, 메틸자스모네이트 농도 의존적 증가, 에테폰 5 mM 처리로 증가, 살리실산·H2O2 영향 없음[6]", "activity_ko": "붉은 색을 내는 질소 함유 색소; 방어 신호 물질로 합성이 조절됨[6]", "source": [6]},
 {"name": "Kaempferol", "name_ko": "캠페롤", "class": "플라보놀", "role": "bioactive", "part": "말린 비름(부위 명시 없음) 50% 에탄올 추출물", "content_text": "UPLC-MS로 확인(정량값 보고 없음)[3]", "activity_ko": "추출물의 파골세포 분화 억제에 관여할 후보 성분으로 저자가 제시(세포·동물 실험, 사람 근거 없음)[3]", "source": [3]},
 {"name": "Nitrogen", "name_ko": "질소(잎 전질소)", "class": "다량 원소", "role": "nutrient", "part": "성숙 녹색 잎", "content_text": "건물 기준 24.4 mg/g(유묘기), 25.2 mg/g(개화기), 25.7 mg/g(종자 성숙기); 단계 간 유의차 없음[4]", "activity_ko": "단백질의 원천 원소; 개화기 늙은 잎에서 51.3% 회수[4]", "source": [4]},
 {"name": "Phosphorus", "name_ko": "인(잎 전인)", "class": "다량 원소", "role": "nutrient", "part": "성숙 녹색 잎", "content_text": "건물 기준 2.55 mg/g(유묘기, 최저)–9.17 mg/g(개화기, 최고)[4]", "activity_ko": "개화·결실기에 수요가 커지며 종자 성숙기 늙은 잎에서 82.6% 회수[4]", "source": [4]},
 {"name": "Calcium", "name_ko": "칼슘", "class": "무기질", "role": "nutrient", "part": "지상부", "content_text": "정량값은 초록에 없음; 15개 품종에서 칼슘·아연 농도가 높을수록 카드뮴 농도도 높음[10]; 바이오차 2.6 g/L 처리로 뿌리 칼슘 증가[21]", "activity_ko": "카드뮴이 칼슘 통로로 흡수되어 저칼슘 품종이 저카드뮴 재배에 제안됨[10, 13]", "source": [10, 13, 21]},
 {"name": "Potassium", "name_ko": "칼륨", "class": "무기질", "role": "nutrient", "part": "뿌리·지상부", "content_text": "정량값은 초록에 없음; 바이오차 26.6 g/L 처리로 뿌리·지상부 칼륨이 크게 증가[21]", "activity_ko": "양이온 흡수 균형에 관여; 고염분에서 흡수 감소[13, 21]", "source": [13, 21]},
 {"name": "Total phenolics", "name_ko": "총 페놀(어린순 메탄올 추출물)", "class": "페놀성 화합물군", "role": "bioactive", "part": "어린순", "content_text": "비름 값은 초록에 없음(확인하지 못함); 추출물의 위암세포 SNU-601 IC50 303.1 µg/mL(시험관)[7]", "activity_ko": "총 페놀과 DPPH 소거능의 상관이 높다고 보고(11종 전체 분석)[7]", "source": [7]},
 {"name": "Oxalic acid", "name_ko": "옥살산", "class": "유기산", "role": "bioactive", "part": "뿌리 분비물('Liuye' 품종)", "content_text": "먹는 부위 함량은 확인하지 못함; 암모늄태 질소 처리에서 뿌리 분비 증가[23]", "activity_ko": "뿌리권 카드뮴 이동성을 높이는 분비 유기산의 하나[23]", "source": [23]},
 {"name": "Hydroperoxide lyase", "name_ko": "13-히드로퍼옥시드 분해효소(HPL)", "class": "효소(단백질)", "role": "bioactive", "part": "잎(미세소체 분획)", "content_text": "활성이 특히 높은 재료로 보고(수치 초록에 없음); 자당·트레할로스 100 g/L 첨가 동결건조 시 활성 거의 100% 유지, 무첨가 약 20%[16]", "activity_ko": "녹색 잎 향(풋내) 성분을 만드는 효소로 향료 생산에 응용 연구[16]", "source": [16]},
 {"name": "Cadmium", "name_ko": "카드뮴(오염 원소)", "class": "유해 중금속", "role": "bioactive", "part": "뿌리·줄기·잎", "content_text": "수경 재배 최고값 고축적 품종 뿌리 950, 줄기 305, 잎 205 mg/kg; 저축적 품종 269, 62.9, 74.8 mg/kg(기준 초록에 명시 없음)[9]; 'Liuye' 지상부 건물 기준 6.92–14.92 mg/kg(질소 형태 시험)[23]", "activity_ko": "식품 안전 관리 대상; 품종·염분·질소 형태에 따라 축적이 크게 달라짐[9, 11, 23]", "source": [9, 11, 23]},
 {"name": "Arsenic", "name_ko": "무기비소(오염 원소)", "class": "유해 원소", "role": "bioactive", "part": "먹는 부위", "content_text": "농도 수치는 초록에 없음; 토양 총비소·점토 함량이 주요 예측 인자[14]", "activity_ko": "발암물질; 비름을 노출 위험이 큰 채소로 평가[14]", "source": [14]},
]

assays = [
 {"role": "literature", "compound": "Kaempferol", "compound_ko": "캠페롤(플라보놀 동정)", "part": "말린 비름(국내 시장 구입, 부위 명시 없음)", "content": "정량값 보고 없음 — 주요 성분 동정만[3]", "method": "UPLC-MS(ESI 음이온)",
  "conditions": {"instrument": "Agilent 1290 Infinity II UPLC + AB SCIEX TripleTOF 5600 plus", "column": "YMC-Triart C18(4.6 mm × 250 mm, 5 µm)", "mobile_phase": "A: 0.1% 포름산 수용액, B: 0.1% 포름산 아세토니트릴", "gradient": "B 25%(0분) → 40%(25분) → 90%(30분)", "flow": "", "temp": "", "detection": "ESI 음이온 모드, 탈용매 온도 400 °C", "injection": "", "sample_prep": "말린 비름을 50% 에탄올로 1:10(w/v) 20–25 °C에서 24시간 진탕 추출, 여과·감압 농축 후 동결건조", "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "이 종 추출물에서 확인된 플라보놀로, 저자가 파골세포 억제 활성의 후보 성분으로 제시했다; 공인 지표성분은 아니다[3]", "source": [3], "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC7029261/", "source_kind": "paper"},
 {"role": "literature", "compound": "Nitrogen", "compound_ko": "잎 전질소·전인", "part": "성숙 녹색 잎·노화 잎(온실 화분 재배)", "content": "녹색 잎 질소 건물 기준 24.4–25.7 mg/g, 인 2.55–9.17 mg/g[4]", "method": "켈달 분해–자동분석기 비색(질소), 바나도몰리브덴 황색 비색법(인)",
  "conditions": {"instrument": "켈달 증류 장치(Kjeltec System 1026) 및 자동분석기", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "비색법", "injection": "", "sample_prep": "70 °C 48시간 건조, 막자로 분말화, H2SO4–H2O2 분해", "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "생육 단계별 양분 항상성과 회수 효율을 보기 위한 측정으로 영양 표시용 지표는 아니다[4]", "source": [4], "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5110967/", "source_kind": "paper"},
 {"role": "literature", "compound": "Difenoconazole", "compound_ko": "잔류 농약 10종(디페노코나졸 등)", "part": "어린순(시설 재배)", "content": "정량한계 0.002 mg/kg, 검출한계 0.0007 mg/kg, 회수율 78.1–131.6%(RSD < 11%), 결정계수 0.9817–0.9999 — 초록 수치[8]", "method": "QuEChERS(구연산 완충) 추출·정제 후 LC-ESI-MS/MS(양이온 모드)",
  "conditions": {"instrument": "", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "", "injection": "", "sample_prep": "", "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "국내 시설 재배 비름의 잔류 감소 양상과 섭취 위해성을 평가하려고 정량했다; 성분 지표가 아닌 안전 지표이며 전문 확인 못함(검증 수치는 초록 값)[8]", "source": [8], "url": "https://pubmed.ncbi.nlm.nih.gov/28918593/", "source_kind": "paper"},
]

d = {"slug": "amaranthus-mangostanus", "name_ko": "비름", "name_en": "Edible amaranth", "scientific_name": "Amaranthus mangostanus L.",
     "aliases": ["비름나물", "새비름", "참비름", "개비름(목록상 다른 이름; 개비름잎 A. lividus 와 다른 원료)", "비름순", "Edible amaranth", "Amaranthus inamoenus Willd.", "Amaranthus inamoenus f. viridis Makino"],
     "sections": sections, "compounds": compounds, "markers": [], "assays": assays, "nutrients": [], "production": [], "world": [], "gi": [], "orgs": [], "sources": sources}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in sections: print(s["key"], len(s["body"]))
