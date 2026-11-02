import json
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "dossier.json"
ACC = "2026-11-02"


def pm(title, cit, pmid, doi, note):
    return {"title": f"{title} — {cit} (PMID {pmid}, {note})", "url": f"https://doi.org/{doi}", "publisher": "PubMed", "accessed": ACC}


S = [
    {"title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 타히티라임열매(Citrus latifolia; 영어명 Tahiti Lime), 사용가능, 사용가능부위: 열매; 같은 목록의 라임·라임껍질 등(Citrus aurantifolia), 카피르라임(Citrus hystrix), 핑거라임(Microcitrus australasica), 라임블로섬(Tilia) 행과 개별인정 라임과피추출물(제2025-26호, Citrus aurantifolia) 행 대조 (로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json)",
     "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
    pm("Phylogenetic origin of limes and lemons revealed by cytoplasmic and nuclear markers", "Ann Bot 2016", "26944784", "10.1093/aob/mcw005", "PMC4817432, 초록 확인"),
    pm("Origin of C. latifolia and C. aurantiifolia triploid limes: the preferential disomic inheritance of doubled-diploid 'Mexican' lime is consistent with an interploid hybridization hypothesis", "Ann Bot 2018", "29293884", "10.1093/aob/mcx179", "PMC5838810, 초록 확인(전문 본문 제공 안 됨)"),
    pm("Preferential Disomic Segregation and Interspecific Recombination in Tetraploid 'Giant Key' Lime; Outlook for Triploid Lime Breeding", "Front Plant Sci 2020", "32670332", "10.3389/fpls.2020.00939", "PMC7330052, 전문 확인"),
    pm("Analysis of molecular variability of 'Tahiti' acid lime selections", "Braz J Biol 2025", "41172524", "10.1590/1519-6984.295629", "초록 확인"),
    pm("Phototoxic coumarins in limes", "Food Chem Toxicol 1993", "8505017", "10.1016/0278-6915(93)90187-4", "초록 확인"),
    pm("Coumarins from the peel of citrus grown in Colombia: composition, elicitation and antifungal activity", "Heliyon 2019;e01937", "31245648", "10.1016/j.heliyon.2019.e01937", "PMC6582165, 전문 확인"),
    pm("Coumarins, psoralens, and quantitative 1H-NMR spectroscopy for authentication of lemon (Citrus limon) and Persian lime (Citrus × latifolia) juices", "Food Chem 2021;129804", "34015560", "10.1016/j.foodchem.2021.129804", "초록 확인"),
    pm("Targeted Analysis of the Concentration Changes of Phenolic Compounds in Persian Lime (Citrus latifolia) during Fruit Growth", "J Agric Food Chem 2018", "29400054", "10.1021/acs.jafc.7b05535", "초록 확인"),
    pm("Effect of Tahiti lime (Citrus latifolia) juice on the Production of the PGF2α/PGE2 and Pro-Inflammatory Cytokines involved in Menstruation", "Sci Rep 2020", "32341436", "10.1038/s41598-020-63477-8", "PMC7184590, 전문 확인"),
    pm("Antimycotic Activity and Genotoxic Evaluation of Citrus sinensis and Citrus latifolia Essential Oils", "Sci Rep 2016;6:25371", "27137128", "10.1038/srep25371", "PMC4853807, 초록 확인"),
    pm("The Effect of Foliar Application of Melatonin on Changes in Secondary Metabolite Contents in Two Citrus Species Under Drought Stress Conditions", "Front Plant Sci 2021", "34567024", "10.3389/fpls.2021.692735", "PMC8455919, 초록 확인"),
    pm("Extraction of potential bioactive compounds from industrial Tahiti lime (Citrus latifolia Tan.) by-product using pressurized liquids and ultrasound-assisted extraction", "Food Res Int 2022;111381", "35761637", "10.1016/j.foodres.2022.111381", "초록 확인"),
    pm("Antioxidant capacity and mineral content of pulp and peel from commercial cultivars of citrus from Brazil", "Food Chem 2012;134(4):1892-8", "23442635", "10.1016/j.foodchem.2012.03.090", "초록 확인"),
    pm("The technology life cycle of Persian lime. A patent based analysis", "Heliyon 2022;e11781", "36458301", "10.1016/j.heliyon.2022.e11781", "PMC9706162, 전문 확인"),
    pm("Occurrence and Multiplex PCR Detection of Citrus Yellow Vein Clearing Virus in Korea", "Plant Pathol J 2024", "38606443", "10.5423/PPJ.OA.09.2023.0136", "PMC11016552, 전문 확인"),
    pm("First Report of 'Candidatus Liberibacter asiaticus' Associated with Huanglongbing on Citrus latifolia in Martinique and Guadeloupe, French West Indies", "Plant Dis 2014", "30708512", "10.1094/PDIS-08-13-0879-PDN", "초록 확인"),
    pm("Metabolomic Investigation of Citrus latifolia and the Putative Role of Coumarins in Resistance to Black Spot Disease", "Front Mol Biosci 2022", "35813812", "10.3389/fmolb.2022.934401", "PMC9263546, 초록 확인"),
    pm("Improving the storage quality of Tahitian limes (Citrus latifolia) by pre-storage UV-C irradiation", "J Food Sci Technol 2019;56(3):1438-1444", "30956323", "10.1007/s13197-019-03623-x", "PMC6423171, 초록 확인"),
    pm("Combined postharvest UV-C and 1-methylcyclopropene (1-MCP) treatment, followed by storage continuously in low level of ethylene atmosphere improves the quality of Tahitian limes", "J Food Sci Technol 2018;55(7):2467-2475", "30042562", "10.1007/s13197-018-3164-4", "PMC6033800, 초록 확인"),
    pm("Hot water treatment and insecticidal coatings for disinfesting limes of mealybugs (Homoptera: Pseudococcidae)", "J Econ Entomol 2000;93(3):1017-20", "10902365", "10.1603/0022-0493-93.3.1017", "초록 확인"),
    pm("Innovation in a Continuous System of Distillation by Steam to Obtain Essential Oil from Persian Lime Juice (Citrus latifolia Tanaka)", "Molecules 2021;26(14):4172", "34299446", "10.3390/molecules26144172", "PMC8306374, 초록 확인"),
    pm("Evaluation of Tahiti lemon shell flour (Citrus latifolia Tanaka) as a fat mimetic", "J Food Sci Technol 2021;58(2):720-730", "33568866", "10.1007/s13197-020-04588-y", "PMC7847908, 초록 확인"),
    pm("Integral valorization of whole Tahiti lime by spray drying: process-formulation optimization and physicochemical attributes", "J Sci Food Agric 2026", "42839340", "10.1002/jsfa.71148", "초록 확인"),
    pm("Margarita Dermatitis Revisited: A Case Report and Literature Review of Lime-Associated Phytophotodermatitis", "Cureus 2026;18(9):e116249", "42889495", "10.7759/cureus.116249", "PMC13669559, 초록 확인; 라임 종 미기재"),
    pm("Asymptomatic Hyperpigmentation without Preceding Inflammation as a Clinical Feature of Citrus Fruits-Induced Phytophotodermatitis", "Ann Dermatol 2018;30(1):75-78", "29386836", "10.5021/ad.2018.30.1.75", "PMC5762480, 초록 확인; 라임 종 미기재"),
    pm("Bergamottin, lime juice, and red wine as inhibitors of cytochrome P450 3A4 activity: comparison with grapefruit juice", "Clin Pharmacol Ther 2003;73(6):529-37", "12811362", "10.1016/S0009-9236(03)00051-1", "초록 확인; 라임 종 미기재"),
    pm("Evaluation of Anti-Inflammatory Activity of Citrus latifolia Tanaka Essential Oil and Limonene in Experimental Mouse Models", "Evid Based Complement Alternat Med 2013;2013:859083", "23762165", "10.1155/2013/859083", "PMC3671226, 초록 확인"),
    pm("Antimutagenic and antioxidant activity of the essential oils of Citrus sinensis and Citrus latifolia", "Sci Rep 2017;7:11479", "28904369", "10.1038/s41598-017-11818-5", "PMC5597616, 초록 확인"),
    pm("Multidimensional enantio gas chromatography/mass spectrometry and gas chromatography-combustion-isotopic ratio mass spectrometry for the authenticity assessment of lime essential oils (C. aurantifolia Swingle and C. latifolia Tanaka)", "J Chromatogr A 2011;1226:87-95", "22088669", "10.1016/j.chroma.2011.10.038", "초록 확인"),
    pm("Effect of supercritical CO2 fractionation of Tahiti lemon (Citrus latifolia Tanaka) essential oil on its antifungal activity against predominant molds from pan bread", "Food Res Int 2022;162:111900", "36461176", "10.1016/j.foodres.2022.111900", "초록 확인"),
]
sources = [dict(n=i + 1, **s) for i, s in enumerate(S)]

sections = [
    {"key": "overview", "title": "한눈에 보기", "body":
     "타히티라임(Citrus latifolia)은 영어로 'Tahiti lime' 또는 'Persian lime'이라 부르는 신맛 라임으로, 세계 라임 수출 시장의 대부분을 차지하는 씨 없는 3배체 품종군이다[3, 4]. "
     "식약처 「식품원료 목록」에는 원료명 '타히티라임열매'(영어명 Tahiti Lime)로 한 행이 올라 있고, 식품에 쓸 수 있는 원료(사용가능)이며 사용 조건은 '사용가능부위 : 열매'다[1]. "
     "목록에서 '라임', '라임껍질', '라임주스' 등은 멕시칸 라임(Citrus aurantifolia)으로 따로 올라 있어 이 종과 구별되며, 이 종을 원재료로 하는 건강기능식품 고시형 원료는 확인하지 못함.\n\n"
     "과즙은 열매 무게의 약 50%이고 산도는 약 6%다[15]. "
     "껍질에는 리메틴·베르갑텐·이소핌피넬린 같은 쿠마린과 푸로쿠마린이 많아, 콜롬비아산 껍질에서 총 쿠마린 932 μg/g, 총 푸로쿠마린 734 μg/g이 측정되었다[7]. "
     "베르갑텐 등 푸로쿠마린은 햇빛과 함께 피부 광독성 반응을 일으킬 수 있는 성분으로 지목되며, 1993년 연구는 퍼시안 라임이 키 라임보다 광독성 잠재력이 클 수 있다고 보았다[6]. "
     "과즙의 주된 플라보노이드는 헤스페리딘이고[10, 12], 정유의 주성분은 리모넨이다[11]."},
    {"key": "history", "title": "역사와 이름", "body":
     "학명 Citrus latifolia는 다나카(Tanaka)의 감귤 분류 체계에서 온 이름으로, 논문에서는 'Citrus latifolia (Yu. Tanaka) Tanaka' 또는 'Citrus × latifolia'로 적는다[4, 8]. "
     "'타히티' 형 라임에는 'Bearss'와 'Persian' 같은 품종이 들어가며, 품종 사이 분자 다형성은 매우 낮아 하나의 3배체화 사건에서 퍼진 영양계로 본다[2, 4]. "
     "라임과 레몬은 무배생식과 접목 같은 영양번식으로 퍼져 왔다[2]. "
     "타히티 섬을 거친 전파 경로와 처음 재배된 연대는 공식·학술 1차 자료로 확인하지 못함.\n\n"
     "오늘날 라임 수출 시장은 대부분 타히티형 라임에 기대고 있어 유전적 기반이 매우 좁다는 점이 육종의 과제로 꼽힌다[4]. "
     "세계지식재산기구(WIPO)에 PCT로 낸 퍼시안 라임 관련 특허를 분석한 연구에서는 미국이 34%로 가장 많았고 한국(9%)과 일본(6%)이 뒤를 이었다[15]. "
     "같은 연구는 특허는 미국·한국·일본이 주도하지만 감귤 생산은 인도·멕시코·브라질·스페인이 이끈다고 정리했다[15]."},
    {"key": "biology", "title": "식물학적 특징", "body":
     "타히티라임은 운향과(Rutaceae) 감귤속 과수다[15]. "
     "열매는 중간에서 큰 크기의 타원형으로 아래쪽이 둥글고, 씨가 거의 없거나 없다[15]. "
     "껍질은 얇고 매끈하며 익으면 옅은 노란색이 된다[15]. 녹색 열매의 저장 연구에서는 껍질 녹색 유지와 꽃받침 탈락 억제를 품질 지표로 썼다[19, 20]. "
     "3배체여서 암수 생식력이 낮고, 단위결과와 함께 씨 없는 열매를 맺는다[4].\n\n"
     "멕시코산 열매를 14주 동안 추적한 연구에서 플라바논이 측정 페놀의 70% 이상을 차지했고, 플라바논·플라본 농도는 약 12주째에 가장 높았다[9]. "
     "껍질 추출물에서는 오렌지와 달리 폴리메톡시플라본보다 쿠마린·푸로쿠마린이 주성분이었고, 오후에 딴 열매와 아침에 딴 열매의 크로마토그램 모양이 달랐다[7]. "
     "껍질 정유는 d-리모넨(51.64%), β-투옌(14.85%), β-피넨(12.79%), γ-테르피넨(12.8%)이 주성분으로 보고되었다[11]. "
     "레몬과 달리 감귤 흑점병 피해가 관찰된 적이 없으며, 병원균 접종 뒤 프레닐화·메톡시 쿠마린이 강하게 유도되었다[18]."},
    {"key": "related_species", "title": "이름과 가까운 종", "body":
     "타히티라임은 레몬(Citrus limon)의 반수체 밑씨에 멕시칸 라임(Citrus aurantifolia)의 2배체 꽃가루가 수정되어 생긴 3배체로 해석된다[2, 4]. "
     "멕시칸 라임은 Citrus micrantha와 시트론(Citrus medica)의 직접 잡종이고, 같은 3배체라도 'Tanepao' 형은 멕시칸 라임 계열에 시트론이 되교잡된 것으로 보아 C. aurantifolia로 분류한다[2, 3]. "
     "이렇게 타히티라임에는 포멜로·시트론·C. micrantha·만다린의 네 조상 유전체가 섞여 있다[4].\n\n"
     "식약처 목록의 '라임'·'라임껍질'·'라임주스' 등과 개별인정형 '라임과피추출물'은 모두 학명 Citrus aurantifolia로 올라 있어 타히티라임과 다른 원료다[1]. "
     "'카피르라임'은 Citrus hystrix, '핑거라임'은 Microcitrus australasica, '라임블로섬'은 피나무속(Tilia) 식물이므로 이름에 '라임'이 있어도 이 종이 아니다[1]. "
     "성분으로도 구별되어, 키 라임 껍질에서는 프소랄렌과 잔토톡신이 검출되지 않았지만 퍼시안 라임 껍질에서는 검출되었다[6]. "
     "과즙에서는 이소핌피넬린과 베르갑텐이 레몬과 구별되는 라임 특이 지표로 제안되었고[8], 정유는 광학이성질체 비율과 탄소 동위원소비로 키 라임 정유와 구별할 수 있다[30]."},
    {"key": "cultivation", "title": "재배와 산지", "body":
     "감귤은 아열대 식물이지만 열대 조건에도 잘 적응해 수확량이 괜찮은 작물로 소개된다[15]. "
     "타히티라임은 브라질의 주요 과수 가운데 하나이고[5], 멕시코에서는 과수원과 수출업체 사이 공급망 문제가 연구될 만큼 산업 규모가 크다[15]. "
     "국내 생산 통계(통계청 농작물생산조사, 특용작물 생산실적)에는 라임 항목이 없어 재배 면적과 생산량은 확인하지 못함. "
     "2024년 국내 논문은 레몬·라임·칼라만시가 새 소득 작물로 전국에서 재배되기 시작했지만, 레몬을 빼면 아직 대량 재배가 아니라 주로 시설(하우스)에서 일부 재배된다고 썼다[16]. "
     "같은 연구는 충남 공주의 퍼시안 라임 잎에서 감귤 황화엽맥투명바이러스(CYVCV)를 국내 처음 확인했고, 잎맥 투명·잎 뒤틀림 증상을 보고했다[16].\n\n"
     "카리브해 프랑스령 마르티니크·과들루프에서는 C. latifolia에서 황룡병(HLB) 병원균이 확인되었다[17]. "
     "수확 뒤에는 UV-C 10.5 kJ/m² 처리 후 10 °C에서 28일 저장한 열매의 수용도가 60%로 무처리(39%)보다 높았다[19]. "
     "1-MCP와 UV-C를 함께 쓰면 에틸렌 생성이 줄고 껍질 황변이 늦어졌다[20]. "
     "미국 연구에서는 49 °C 물에 20분 담가 깍지벌레를 모두 죽이면서 품질에는 유의한 영향이 없었다[21]."},
    {"key": "processing", "title": "가공과 이용", "body":
     "퍼시안 라임은 주로 과즙과 정유를 만드는 데 쓰이고, 과즙과 정유는 식품·화학·의약·향료 산업에서 쓰인다[15, 22]. "
     "과즙을 증기 증류해 정유를 얻는 연속식 공정은 회수율이 최대 90%였고 공정 시간을 8시간에서 4시간으로 줄였다[22]. "
     "정유를 초임계 이산화탄소로 분획한 연구에서도 주성분은 리모넨이었고, 녹는 분획이 빵 곰팡이 억제력이 더 컸다[31].\n\n"
     "착즙 뒤 남는 박(퍼미스)에서는 가압 액체 추출(110 °C)에서 수율·총 페놀·항산화능(ORAC)이 가장 높았고, 헤스페리딘과 나리루틴도 함께 추출되었다[13]. "
     "껍질 가루는 식이섬유가 85.30 g/100 g으로, 케이크 지방의 10%를 대신했을 때 지방이 19.16% 줄었다[23]. "
     "열매 전체를 분무건조한 가루는 수분 약 3.6%, 수분활성도 약 0.25, 총 페놀 약 522 mg GAE/100 g(건물)이었다[24]. "
     "식약처 생산실적에 오른 '라임과피추출물'은 개별인정형 원료로 학명이 Citrus aurantifolia여서 이 종의 제품 생산실적으로 볼 수 없다[1]. "
     "이 종만을 원료로 한 국내 제품 생산실적은 확인하지 못함."},
    {"key": "genetics", "title": "유전 정보", "body":
     "감귤속의 기본 염색체 수는 x = 9이고, 타히티라임은 3배체다[4]. "
     "133개 감귤 계통을 엽록체·미토콘드리아 표지와 123개 핵 표지로 분석한 연구는 C. latifolia가 레몬의 반수체 밑씨와 C. aurantifolia의 2배체 생식세포가 만나 생겼다고 결론지었다[2]. "
     "'멕시칸' 라임을 배수화한 4배체의 감수분열을 분석한 연구에서 이배체 생식세포의 부모 이형접합성 복원율은 83–99%였고, 이 구조가 타히티라임 유전체와 맞아 배수성 간 교잡 기원 가설을 뒷받침했다[3].\n\n"
     "'Giant Key' 4배체 라임을 꽃가루 친으로 써서 3배체 잡종 272개를 만든 연구는 SNP 131개로 9개 연관군, 272.8 cM의 유전 지도를 만들고, 이배체 생식세포가 부모 이형접합성의 평균 91.17%를 전달함을 보였다[4]. "
     "연구진은 이런 배수성 간 교잡으로 타히티형 라임을 다시 만들어 다양화하는 '재구성 육종'이 가능하다고 보았다[4]. "
     "브라질에서 형태가 다른 선발 계통 12개를 SSR 표지 12쌍으로 분석했을 때 띠 19개가 모두 단형이었고 DNA 메틸화 정도만 달라, 표현형 차이를 후성유전 변화로 해석했다[5]. "
     "이 종의 참조 유전체 조립 정보는 확인하지 못함."},
    {"key": "safety", "title": "안전성", "body":
     "식약처 목록은 이 종의 열매만 식품원료로 허용한다[1]. "
     "공공기관의 알레르기·잔류농약 정보는 확인하지 못함. "
     "퍼시안 라임 껍질의 쿠마린은 리메틴 > 베르갑텐 > 이소핌피넬린 > 잔토톡신 > 프소랄렌 순이었고, 과육의 쿠마린은 껍질보다 13–182배 낮았다[6]. "
     "연구진은 베르갑텐을 라임 광피부염의 주원인 후보로 보았다[6].\n\n"
     "라임 과즙이나 껍질이 피부에 묻은 채 햇빛(자외선 A)을 쬐면 홍반·물집이나 색소침착이 생기는 '마르가리타 피부염'이 보고되며, 증상 없는 색소침착 사례 14건은 주로 음료나 음식을 만들다 손등에 생겼다[25]. "
     "국내 연구진도 감귤류(라임)를 만진 뒤 강한 햇빛을 쬔 환자 2명에서 염증 없이 색소침착만 나타난 사례가 보고되었으나, 이 사례들은 라임의 종을 밝히지 않았다[25, 26]. "
     "종을 밝히지 않은 라임 주스의 베르가모틴 농도는 자몽 주스의 4배였지만, 1/4 농도 라임 주스는 펠로디핀의 평균 체내 노출을 바꾸지 않았고 2명에서만 2배 넘게 높였다[27]. "
     "브라질 여성 15명이 이틀간 타히티라임 과즙(1회 약 20–30 mL)을 마신 시험에서는 해나 원치 않은 영향이 보고되지 않았다[10]. "
     "껍질 정유는 에임스 시험에서 돌연변이를 일으키지 않았지만 사람 구강 상피세포에는 21.8 μg에서 독성을 보였다[11]."},
]

compounds = [
    dict(name="Limettin", name_ko="리메틴(5,7-다이메톡시쿠마린)", **{"class": "쿠마린"}, role="marker", part="열매 껍질·과육",
         content_text="퍼시안 라임 껍질 쿠마린 중 가장 많음, 과육에서는 이소핌피넬린 다음[6]; 타히티라임 껍질에서 분리·정량(총 쿠마린 932 ± 47 μg/g)[7]",
         activity_ko="탄저병균(Colletotrichum sp.) 균사 생장·포자 발아 억제, 베르갑텐과 섞으면 억제 상승(시험관)[7]", source=[6, 7]),
    dict(name="Bergapten", name_ko="베르갑텐(5-메톡시프소랄렌)", **{"class": "푸로쿠마린"}, role="marker", part="열매 껍질·과즙",
         content_text="퍼시안 라임 껍질 쿠마린 중 리메틴 다음[6]; 타히티라임 껍질 이소핌피넬린·베르갑텐 합 168 μg/g[7]; 과즙에서 레몬과 구별되는 라임 특이 지표[8]",
         activity_ko="라임 광피부염의 주원인 후보[6]; 탄저병균 억제(시험관)[7]", source=[6, 7, 8]),
    dict(name="Isopimpinellin", name_ko="이소핌피넬린", **{"class": "푸로쿠마린"}, role="marker", part="열매 껍질·과육·과즙",
         content_text="퍼시안 라임 과육 쿠마린 중 가장 많음[6]; 타히티라임 껍질 이소핌피넬린·베르갑텐 합 168 μg/g[7]; 과즙의 라임 특이 지표[8]",
         activity_ko="광독성 푸로쿠마린 계열(활성 정량 자료 확인하지 못함)[6]", source=[6, 7, 8]),
    dict(name="Xanthotoxin", name_ko="잔토톡신(8-메톡시프소랄렌)", **{"class": "푸로쿠마린"}, role="bioactive", part="열매 껍질·과육; 흑점병균 접종 조직",
         content_text="퍼시안 라임 껍질·과육에서 검출, 키 라임에서는 검출되지 않음[6]; 흑점병균 접종 뒤 유도된 쿠마린으로 분리[18]",
         activity_ko="광독성 푸로쿠마린[6]; 쿠마린 혼합 분획이 흑점병균에 항진균 활성(단일 성분은 유의하지 않음)[18]", source=[6, 18]),
    dict(name="Psoralen", name_ko="프소랄렌", **{"class": "푸로쿠마린"}, role="bioactive", part="열매 껍질·과육",
         content_text="퍼시안 라임 껍질·과육 쿠마린 중 가장 적음, 키 라임에서는 검출되지 않음[6]",
         activity_ko="광독성 푸로쿠마린[6]", source=[6]),
    dict(name="Bergamottin", name_ko="베르가모틴(5-게라닐옥시프소랄렌)", **{"class": "푸로쿠마린"}, role="bioactive", part="열매 껍질",
         content_text="타히티라임 껍질에서 분리, 게라닐옥시 유도체가 주성분[7]",
         activity_ko="탄저병균 억제는 리메틴·베르갑텐보다 약함(시험관)[7]", source=[7]),
    dict(name="5-Geranyloxy-7-methoxycoumarin", name_ko="5-게라닐옥시-7-메톡시쿠마린", **{"class": "쿠마린"}, role="bioactive", part="열매 껍질; 흑점병균 접종 조직",
         content_text="타히티라임 껍질에서 분리, 게라닐옥시 유도체가 주성분[7]; 흑점병균 접종 뒤 유도[18]",
         activity_ko="탄저병균 억제 약함(시험관)[7]", source=[7, 18]),
    dict(name="Oxypeucedanin hydrate", name_ko="옥시퓨세다닌 하이드레이트", **{"class": "푸로쿠마린"}, role="bioactive", part="열매 껍질",
         content_text="타히티라임 껍질에서 분리(함량 확인하지 못함)[7]",
         activity_ko="확인하지 못함[7]", source=[7]),
    dict(name="Hesperidin", name_ko="헤스페리딘", **{"class": "플라바논 배당체"}, role="marker", part="과즙·착즙박",
         content_text="라임 1개 과즙(40 mL)에 약 20 mg[10]; 온실 재배 퍼시안 라임 묘목의 주 폴리페놀(조직 확인 못함)[12]; 착즙박에서 추출[13]",
         activity_ko="과즙 시험의 주 플라보노이드로 제시(직접 효과 미입증)[10]", source=[10, 12, 13]),
    dict(name="Eriocitrin", name_ko="에리오시트린", **{"class": "플라바논 배당체"}, role="bioactive", part="과즙",
         content_text="타히티라임 과즙에서 UPLC-MS/MS로 확인(함량 확인하지 못함)[10]",
         activity_ko="확인하지 못함[10]", source=[10]),
    dict(name="Narirutin", name_ko="나리루틴", **{"class": "플라바논 배당체"}, role="bioactive", part="착즙박",
         content_text="산업용 착즙박 추출물에서 정량(수치 확인하지 못함)[13]",
         activity_ko="확인하지 못함[13]", source=[13]),
    dict(name="Limonene", name_ko="리모넨", **{"class": "모노테르펜"}, role="bioactive", part="껍질 정유",
         content_text="껍질 정유의 51.64%(d-리모넨)[11]; 정유 주성분[12, 31]",
         activity_ko="생쥐 지모산 복막염에서 백혈구 침윤·TNF-α 감소(500 mg/kg)[28]", source=[11, 12, 28, 31]),
    dict(name="gamma-Terpinene", name_ko="γ-테르피넨", **{"class": "모노테르펜"}, role="bioactive", part="껍질 정유",
         content_text="껍질 정유의 12.8%[11]",
         activity_ko="정유 전체로 칸디다균 억제·항돌연변이 활성(단일 성분 효과 아님)[11, 29]", source=[11, 29]),
    dict(name="beta-Pinene", name_ko="β-피넨", **{"class": "모노테르펜"}, role="bioactive", part="껍질 정유",
         content_text="껍질 정유의 12.79%[11]",
         activity_ko="확인하지 못함(정유 전체 활성만 보고)[11]", source=[11]),
    dict(name="Ascorbic acid", name_ko="비타민 C(아스코르브산)", **{"class": "비타민"}, role="nutrient", part="열매 껍질",
         content_text="타히티라임 껍질 8 mg/100 g(비교한 감귤 가운데 가장 낮음)[14]",
         activity_ko="항산화능과 상관[14]", source=[14]),
]

assays = [
    {"role": "literature", "compound": "Bergapten", "compound_ko": "베르갑텐(리메틴·이소핌피넬린·베르가모틴·5-게라닐옥시-7-메톡시쿠마린 동시 정량)",
     "part": "열매 껍질(플라베도+알베도, 콜롬비아 안티오키아산)",
     "content": "타히티라임 껍질 총 쿠마린 932 ± 47 μg/g, 총 푸로쿠마린 734 ± 36 μg/g, 이소핌피넬린·베르갑텐 합 168 μg/g[7]",
     "method": "HPLC-DAD",
     "conditions": {"instrument": "Shimadzu Prominence HPLC, DAD(SPD-M20A), LabSolutions Lite 1.22 SP1",
                    "column": "Phenomenex Luna RP-C18, 150 mm × 4.6 mm, 5 μm",
                    "mobile_phase": "아세토니트릴(HPLC 등급)·탈이온수",
                    "gradient": "아세토니트릴 5→34%(10분), 34→70%(26분), 70→87%(17분), 87→90%(5분), 이후 7분 유지",
                    "flow": "0.7 mL/min", "temp": "칼럼 33 °C",
                    "detection": "쿠마린 254 nm, 푸로쿠마린 272 nm(DAD 200–800 nm로 피크 확인)",
                    "injection": "10 μL",
                    "sample_prep": "껍질 5 g을 잘게 잘라 HPLC 등급 메탄올 15 mL로 3회, 어두운 곳에서 초음파 30분 추출 → Whatman No. 1 여과 → 메탄올로 50 mL 정용 → −20 °C 보관",
                    "standard": "타히티라임 껍질에서 분리한 표준품(순도 > 95%), 각 4 mg을 아세토니트릴 10 mL에 녹인 뒤 이동상으로 희석",
                    "linearity": "0.5–10 mg/L 5농도, R² > 0.99",
                    "lod": "원문 표에 제시(값 확인 못함)", "loq": "원문 표에 제시(값 확인 못함)", "recovery": ""},
     "rationale": "푸로쿠마린은 라임 껍질의 대표 2차 대사산물이자 광독성 원인 성분이어서 껍질 품질·안전 지표가 됨; 전문 확인, 회수율은 원문에 없음, 개별 화합물 번호와 함량의 대응은 표가 빠져 확인 못함[7].",
     "source": [7], "url": "https://doi.org/10.1016/j.heliyon.2019.e01937", "source_kind": "paper"},
    {"role": "literature", "compound": "Bergapten", "compound_ko": "베르갑텐(리메틴·이소핌피넬린·잔토톡신·프소랄렌)",
     "part": "열매 껍질(rind)·과육(pulp), 퍼시안 라임과 키 라임 비교",
     "content": "퍼시안 라임 껍질: 리메틴 > 베르갑텐 > 이소핌피넬린 > 잔토톡신 > 프소랄렌; 과육 쿠마린은 껍질의 1/13–1/182[6]",
     "method": "정량 방법 원문 확인 못함",
     "conditions": {"instrument": "", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "", "injection": "", "sample_prep": "", "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""},
     "rationale": "라임 광피부염의 원인 후보 성분을 품종(퍼시안·키)과 부위별로 비교하려고 정량함; 전문 확인 못함[6].",
     "source": [6], "url": "https://doi.org/10.1016/0278-6915(93)90187-4", "source_kind": "paper"},
    {"role": "literature", "compound": "Isopimpinellin", "compound_ko": "이소핌피넬린·베르갑텐(과즙 진위 판별 지표)",
     "part": "열매 부위별(플라베도·알베도·내과피)과 착즙 과즙",
     "content": "수치 확인하지 못함; 이소핌피넬린·베르갑텐·5-게라닐옥시-8-메톡시프소랄렌(잠정)이 라임 특이 지표[8]",
     "method": "HPLC(쿠마린·프소랄렌) 및 정량 1H-NMR",
     "conditions": {"instrument": "", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "", "injection": "", "sample_prep": "", "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""},
     "rationale": "레몬 과즙에 라임 과즙을 섞는 위조를 가리는 지표로, 강한 착즙에도 레몬에서 나오지 않는 라임 특이 성분을 골랐음; 전문 확인 못함[8].",
     "source": [8], "url": "https://doi.org/10.1016/j.foodchem.2021.129804", "source_kind": "paper"},
    {"role": "literature", "compound": "Hesperidin", "compound_ko": "플라바논(헤스페리딘 등) 20종·페놀산 4종",
     "part": "열매(생육 14주 동안 시기별)",
     "content": "플라바논이 측정 페놀의 70% 이상, 약 12주째 최대(개별 수치 확인하지 못함)[9]",
     "method": "LC-QqQ MS/MS(삼중 사중극자), 초음파 추출",
     "conditions": {"instrument": "", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "", "injection": "", "sample_prep": "초음파 보조 추출(세부 조건 확인 못함)", "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""},
     "rationale": "생육 단계별 페놀 변화를 표적 정량해 수확 시기 판단 지표를 찾으려 함; 쿠마르산 유도체가 성숙 단계 구분에 가장 큰 영향; 전문 확인 못함[9].",
     "source": [9], "url": "https://doi.org/10.1021/acs.jafc.7b05535", "source_kind": "paper"},
]

d = {
    "slug": "citrus-latifolia",
    "name_ko": "타히티라임",
    "name_en": "Tahiti lime (Persian lime)",
    "scientific_name": "Citrus latifolia (Yu. Tanaka) Tanaka",
    "aliases": ["타히티라임열매", "퍼시안라임", "페르시안라임", "Tahiti lime", "Persian lime", "Tahiti acid lime", "Bearss lime", "Citrus × latifolia"],
    "sections": sections,
    "compounds": compounds,
    "markers": [],
    "nutrients": [],
    "assays": assays,
    "production": [],
    "world": [],
    "gi": [],
    "orgs": [],
    "sources": sources,
}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
for s in sections:
    print(s["key"], len(s["body"]))
