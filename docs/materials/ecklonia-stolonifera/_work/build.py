import json
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "dossier.json"
A = "2026-11-02"


def pm(n, title, doi, journal, pmid, pmc=None):
    pub = f"{journal} (PubMed {pmid}" + (f", {pmc})" if pmc else ")")
    url = f"https://doi.org/{doi}" if doi else f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
    return {"n": n, "title": title, "url": url, "publisher": pub, "accessed": A}


sources = [
    {"n": 1, "title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 곰피·곰피추출물분말·곰피추출액(Ecklonia stolonifera) 항목과 건강기능식품(C코드) '곰피추출물(기능성원료인정제2018-1호)' 항목",
     "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
    pm(2, "In-Depth Understanding of Ecklonia stolonifera Okamura: A Review of Its Bioactivities and Bioactive Compounds. Mar Drugs 2022;20(10):607", "10.3390/md20100607", "Marine Drugs", "36286432", "PMC9604725"),
    pm(3, "Protective Effects of Ecklonia stolonifera Extract on Ethanol-Induced Fatty Liver in Rats. Biomol Ther 2016;24(6):650–658", "10.4062/biomolther.2016.176", "Biomolecules & Therapeutics", "27795452", "PMC5098545"),
    pm(4, "Erratum to \"Protective Effects of Ecklonia stolonifera Extract on Ethanol-Induced Fatty Liver in Rats\". Biomol Ther 2017;25(2):222", "10.4062/biomolther.2017.222", "Biomolecules & Therapeutics", "28241405", "PMC5340548"),
    pm(5, "Ecklonia stolonifera Extract Suppresses Lipid Accumulation by Promoting Lipolysis and Adipose Browning in High-Fat Diet-Induced Obese Male Mice. Cells 2020;9(4):871", "10.3390/cells9040871", "Cells", "32252474", "PMC7226821"),
    pm(6, "Quantitative determination of major phlorotannins in Ecklonia stolonifera. Arch Pharm Res 2010;33(4):539–544", "10.1007/s12272-010-0407-y", "Archives of Pharmacal Research", "20422362"),
    pm(7, "A new phlorotannin from the brown alga Ecklonia stolonifera. Chem Pharm Bull 2003;51(8):1012–1014", "10.1248/cpb.51.1012", "Chemical & Pharmaceutical Bulletin", "12913249"),
    pm(8, "Inhibitory phlorotannins from the edible brown alga Ecklonia stolonifera on total reactive oxygen species (ROS) generation. Arch Pharm Res 2004;27(2):194–198", "10.1007/BF02980106", "Archives of Pharmacal Research", "15022722"),
    pm(9, "Tyrosinase inhibitors isolated from the edible brown alga Ecklonia stolonifera. Arch Pharm Res 2004;27(12):1226–1232", "10.1007/BF02975886", "Archives of Pharmacal Research", "15646796"),
    pm(10, "Hepatoprotective constituents of the edible brown alga Ecklonia stolonifera on tacrine-induced cytotoxicity in Hep G2 cells. Arch Pharm Res 2005;28(12):1376–1380", "10.1007/BF02977904", "Archives of Pharmacal Research", "16392671"),
    pm(11, "Antidiabetic and antioxidant effects of polyphenols in brown alga Ecklonia stolonifera in genetically diabetic KK-A(y) mice. Plant Foods Hum Nutr 2008;63(4):163–169", "10.1007/s11130-008-0098-4", "Plant Foods for Human Nutrition", "18958624"),
    pm(12, "Anti-hyperlipidemic effect of an edible brown algae, Ecklonia stolonifera, and its constituents on poloxamer 407-induced hyperlipidemic and cholesterol-fed rats. Arch Pharm Res 2008;31(12):1564–1571", "10.1007/s12272-001-2152-8", "Archives of Pharmacal Research", "19099225"),
    pm(13, "Isolation and identification of phlorotannins from Ecklonia stolonifera with antioxidant and anti-inflammatory properties. J Agric Food Chem 2009;57(9):3483–3489", "10.1021/jf900820x", "Journal of Agricultural and Food Chemistry", "19338274"),
    pm(14, "Protein tyrosine phosphatase 1B and α-glucosidase inhibitory phlorotannins from edible brown algae, Ecklonia stolonifera and Eisenia bicyclis. Biosci Biotechnol Biochem 2011;75(8):1472–1480", "10.1271/bbb.110137", "Bioscience, Biotechnology, and Biochemistry", "21821954"),
    pm(15, "The absolute configuration of ecklonialactones A, B, and E, novel oxylipins from brown algae of the genera Ecklonia and Egregia. J Nat Prod 1994;57(1):171–174", "10.1021/np50103a028", "Journal of Natural Products", "8158161"),
    pm(16, "Isolation and characterization of vanadium bromoperoxidase from a marine macroalga, Ecklonia stolonifera. J Inorg Biochem 1998;72(1-2):23–28", "10.1016/s0162-0134(98)10055-7", "Journal of Inorganic Biochemistry", "9861726"),
    pm(17, "A molecular investigation of the genus Ecklonia (Phaeophyceae, Laminariales) with special focus on the Southern Hemisphere. J Phycol 2015;51(2):236–246", "10.1111/jpy.12264", "Journal of Phycology", "26986519"),
    pm(18, "Comparison of Ecklonia cava, Ecklonia stolonifera and Eisenia bicyclis for phlorotannin extraction. J Environ Biol 2014;35(4):713–719", None, "Journal of Environmental Biology", "25004758"),
    pm(19, "Anti-adipogenic activity of the edible brown alga Ecklonia stolonifera and its constituent fucosterol in 3T3-L1 adipocytes. Arch Pharm Res 2014;37(6):713–720", "10.1007/s12272-013-0237-9", "Archives of Pharmacal Research", "24014306"),
    pm(20, "Hepaprotective Effect of Standardized Ecklonia stolonifera Formulation on CCl4-Induced Liver Injury in Sprague-Dawley Rats. Biomol Ther 2018;26(2):218–223", "10.4062/biomolther.2017.199", "Biomolecules & Therapeutics", "29129047", "PMC5839501"),
    pm(21, "Ecklonia stolonifera Okamura Extract Suppresses Myocardial Infarction-Induced Left Ventricular Systolic Dysfunction by Inhibiting p300-HAT Activity. Nutrients 2022;14(3):580", "10.3390/nu14030580", "Nutrients", "35276939", "PMC8838613"),
    pm(22, "Phlorotannins with Potential Anti-tyrosinase and Antioxidant Activity Isolated from the Marine Seaweed Ecklonia stolonifera. Antioxidants 2019;8(8):240", "10.3390/antiox8080240", "Antioxidants", "31344959", "PMC6720259"),
    pm(23, "The Suppressive Activity of Fucofuroeckol-A Derived from Brown Algal Ecklonia stolonifera Okamura on UVB-Induced Mast Cell Degranulation. Mar Drugs 2018;16(1):1", "10.3390/md16010001", "Marine Drugs", "29300311", "PMC5793049"),
    pm(24, "Impact of Ecklonia stolonifera extract on in vitro ruminal fermentation characteristics, methanogenesis, and microbial populations. Asian-Australas J Anim Sci 2019;32(12):1864–1872", "10.5713/ajas.19.0092", "Asian-Australasian Journal of Animal Sciences", "31208173", "PMC6819679"),
    pm(25, "Anti-glycation properties of the aqueous extract solutions of dried algae products and effect of lactic acid fermentation on the properties. Food Chem 2015;192:1109–1115", "10.1016/j.foodchem.2015.07.073", "Food Chemistry", "26304454"),
    {"n": 26, "title": "식품의약품안전처 「식품 등의 생산실적」 2019–2025년판 — 건강기능식품 품목 유형별 현황(개별인정형 '곰피추출물'), 앱 파싱본 docs/stats/hf_items.csv(금액 단위 천원)",
     "url": "https://www.mfds.go.kr", "publisher": "식품의약품안전처", "accessed": "2026-10-08"},
    pm(27, "Iodine intake from brown seaweed and the related nutritional risk assessment in Koreans. Nutr Res Pract 2024;18(3):412–424", "10.4162/nrp.2024.18.3.412", "Nutrition Research and Practice", "38854470", "PMC11156764"),
    {"n": 28, "title": "Algal Resources 16권 2호 85쪽 논문(츠루아라메 Ecklonia cava subsp. stolonifera 의 요오드 정량) — 원문을 열지 못하고 웹 검색 결과 요약으로만 확인함(J-STAGE 접속 불가)",
     "url": "https://www.jstage.jst.go.jp/article/jsap/16/2/16_85/_article/-char/en", "publisher": "J-STAGE 'Algal Resources'", "accessed": A},
    pm(29, "Phlorotannins from edible marine seaweed Ecklonia stolonifera disrupt USP5-Cav3.2 calcium channel interactions and reverse chronic inflammatory pain. Toxicol Appl Pharmacol 2025;502:117440", "10.1016/j.taap.2025.117440", "Toxicology and Applied Pharmacology", "40505820"),
    pm(30, "Collective Total Synthesis of Ecklonialactones, Eiseniachlorides and Analogs. Chemistry 2024;30(43):e202401632", "10.1002/chem.202401632", "Chemistry – A European Journal", "38770615"),
    pm(31, "Radical Scavenging-Linked Anti-Obesity Effect of Standardized Ecklonia stolonifera Extract on 3T3-L1 Preadipocytes and High-Fat Diet-Fed ICR Mice. J Med Food 2023;26(4):232–243", "10.1089/jmf.2022.K.0138", "Journal of Medicinal Food", "36897318"),
    pm(32, "Anti-inflammatory activities of an ethanol extract of Ecklonia stolonifera in lipopolysaccharide-stimulated RAW 264.7 murine macrophage cells. J Agric Food Chem 2012;60(36):9120–9129", "10.1021/jf3022018", "Journal of Agricultural and Food Chemistry", "22897701"),
    pm(33, "Protective effect of the edible brown alga Ecklonia stolonifera on doxorubicin-induced hepatotoxicity in primary rat hepatocytes. J Pharm Pharmacol 2014;66(8):1180–1188", "10.1111/jphp.12241", "Journal of Pharmacy and Pharmacology", "24628384"),
    pm(34, "Effects of Ecklonia stolonifera Extract on Metabolic Dysregulation in High-Fat Diet-Induced Obese Mice. J Med Food 2024;27(3):242–249", "10.1089/jmf.2023.K.0252", "Journal of Medicinal Food", "38354279"),
]

sections = [
    {"key": "overview", "title": "한눈에 보기", "body":
     "곰피(Ecklonia stolonifera Okamura)는 한국과 일본 연안에 사는 여러해살이 갈조류로, 오래전부터 먹어 온 해조다[2]. 우리나라에서는 동해안과 남해안의 수심 2–10 m 조하대에 널리 자라며 식재료로 흔히 쓰인다[3, 5]. 식약처 「식품원료 목록」에는 '곰피', '곰피추출물분말', '곰피추출액' 세 원료명이 수산물로 올라 있고, 세 항목 모두 사용 조건은 '사용가능', 사용 가능 부위는 '전체'다[1]. 같은 목록의 건강기능식품(C코드) 항목에는 '곰피추출물(기능성원료인정제2018-1호)'이 개별인정형 원료로 올라 있다[1]. 이 개별인정 원료의 인정 기능성, 1일 섭취량, 지표성분 기준은 공식 원문으로 확인하지 못함.\n\n"
     "곰피에는 디엑콜(dieckol)·에콜(eckol)·플로로푸코푸로에콜 A 같은 플로로탄닌이 많아, 이 성분들이 여러 약리 작용의 주성분으로 꼽힌다[2, 6]. 70% 에탄올 추출물을 다룬 연구들은 디엑콜을 추출물의 지표성분으로 삼았다[2, 5]. 효능 연구는 대부분 세포·동물 실험이며, 사람을 대상으로 한 시험은 PubMed에서 확인하지 못함. 갈조류는 요오드가 많은 식품군이지만, 곰피 자체의 요오드 함량은 공공 성분표나 PubMed 논문에서 확인하지 못함."},
    {"key": "history", "title": "이용 역사", "body":
     "곰피는 한국에서 흔히 식재료로 쓰이는 갈조류로 소개된다[8]. 총설은 이 해조가 한국과 일본에서 자연산 채취와 양식으로 얻어지고, 많은 사람이 건강식품처럼 먹는다고 정리했다[2]. 일본 연구는 곰피를 '츠루아라메(tsuruarame)'라는 이름의 말린 해조 제품으로 다뤘다[25]. 일본의 당뇨 쥐 연구도 곰피를 '흔히 건강식품으로 쓰이는 해조'로 소개했다[11].\n\n"
     "과학 연구는 2000년대 초 부산 지역 연구진을 중심으로 본격화되었다[7, 8, 9]. 2003년에는 곰피 메탄올 추출물에서 새로운 플로로탄닌인 엑스톨로놀(eckstolonol)이 분리·명명되었다[7]. 2004년에는 해조 17종 추출물 가운데 곰피만이 높은 티로시나아제 억제 활성을 보였다는 보고가 나왔다[9]. 이후 간 보호, 항비만, 항염증 연구가 이어졌고, 2018년에는 곰피추출물이 건강기능식품 개별인정형 원료로 인정되었다[1, 10, 19]. 곰피를 먹어 온 구체적인 문헌 기록이나 시작 시기는 공공기관 자료로 확인하지 못함."},
    {"key": "biology", "title": "생물학적 특징·생태", "body":
     "곰피는 다시마목(Laminariales)에 속하는 여러해살이 저서성 갈조류로, 한국과 일본의 태평양 중부 연안에 분포한다[2]. 보통 수심 2–10 m에서 자라며, 곧게 선 엽상체의 길이는 자라는 수심과 관련이 있어 2 m에서 자란 개체가 1.0–1.5 m나 2.5–3.0 m에서 자란 개체보다 훨씬 길었다[2]. 잎의 길이는 45.2–96.5 cm, 너비는 13.7–28.6 cm로 보고되었고, 3–7월에 잎이 길고 11월에 폭이 좁았다[2].\n\n"
     "총설에 따르면 곰피는 번식력이 강하고 환경 변화에 잘 적응하며, 다른 갈조류와 달리 여름철 수온이 올라도 계속 자란다[2]. 세포벽 다당류로는 셀룰로스·후코이단·라미나란이 확인되었고, 물 추출물에는 저분자 다당류인 라미나린이 들어 있었다[2]. 곰피에서는 바나듐을 활성 중심으로 쓰는 브로모퍼옥시다아제(83 kDa)가 분리되었으며, 이 효소는 열(Tm 68 °C)과 유기용매에 강했다[16]. 이 종에서 처음 분리된 에클로니아락톤(ecklonialactone)류 옥실리핀은 다불포화지방산이 리폭시게나아제로 산화되어 만들어지는 물질이다[15, 30]."},
    {"key": "related_species", "title": "관련 종·이름", "body":
     "곰피의 학명은 Ecklonia stolonifera Okamura이며, 일본에서는 츠루아라메(tsuruarame)라고 부른다[23, 25]. 식약처 목록에는 곰피의 영어 이름과 별칭이 비어 있다[1]. 예전 논문들은 이 종을 다시마과(Laminariaceae)로 적었으나, 분자계통 연구에서 감태속(Ecklonia)은 레소니아과(Lessoniaceae)로 옮겨졌다[3, 17]. 감태속은 북반구 4종, 남반구 3종으로 이루어지며, 감태(E. cava)·구로메(E. kurome)·곰피 같은 동아시아 종은 남반구 종들과 구별되는 별개의 계통을 이룬다[17]. 같은 연구는 대황속(Eisenia)과 Eckloniopsis가 감태속과 매우 가까워 별도 속으로 둘 필요가 없을 수 있다고 보았다[17].\n\n"
     "같은 속의 감태(E. cava)도 식약처 식품원료 목록과 건강기능식품 원료 목록에 따로 올라 있으므로, 원료명과 학명을 구별해 봐야 한다[1]. 세 갈조류(감태·곰피·대황)의 플로로탄닌을 함께 비교한 연구가 많지만, 이 자료의 성분 값은 곰피 시료에서 얻은 것만 옮겼다[14, 18]. 일본 웹 자료에는 곰피를 감태의 아종(E. cava subsp. stolonifera)으로 다룬 예가 있다고 하나, 이 분류 처리의 원문은 확인하지 못함."},
    {"key": "cultivation", "title": "양식·채취", "body":
     "총설에 따르면 곰피는 한국과 일본에서 자연산 채취와 양식 두 가지 방식으로 얻는다[2]. 한 연구는 2012년 8월 부산 연안에서 채취한 곰피를 바닷물과 수돗물로 씻은 뒤 공기 중에서 말려 가루로 만들어 썼다[3]. 곰피는 전복 양식의 먹이 후보로도 높이 평가되는데, 여름철 수온이 올라도 계속 자라 먹이를 꾸준히 공급할 수 있고 전복 껍데기 색을 시장이 선호하는 짙은 갈색으로 만든다고 한다[2].\n\n"
     "곰피 추출물은 반추가축의 사료 첨가물로도 시험되었으며, 시험관 반추위 발효에서 발효 특성과 미생물 군집에 해로운 영향은 없었으나 메탄 발생은 오히려 늘었다[24]. 해양수산부·통계청 어업생산통계에서 곰피의 양식·채취 생산량을 따로 집계한 값은 확인하지 못함. 곰피의 양식 방법(채묘·가이식 시기 등)을 다룬 공공기관 자료도 확인하지 못함."},
    {"key": "processing", "title": "가공·이용 연구", "body":
     "시판 곰피 말린 제품 4종과 데친 제품 2종을 비교한 연구에서 데친 제품은 항균 활성이 없었고, 데치는 과정에서 플로로탄닌과 알긴산·후코이단 같은 수용성 성분이 빠져나간 것으로 해석되었다[2]. 반면 감태·곰피·대황을 끓는 물로 추출한 비교 연구에서 곰피의 디엑콜은 유기용매 추출의 93%, 플로로푸코푸로에콜 A는 86%가 회수되었다[18]. 기능성 소재용 추출물은 주로 말린 곰피 가루를 70% 에탄올로 환류 추출한 뒤 감압 농축·동결건조해 만든다[3, 5]. 한 연구는 곰피 가루 3 kg을 70% 에탄올 27 L로 9시간 환류 추출했다[3].\n\n"
     "이런 추출물에서 디엑콜은 23.7 ± 0.21 mg/g 또는 27.42 ± 0.66 mg/g으로 정량되었다[2, 5]. 지방간 연구는 2017년 정오표로 혈청 유리지방산 표의 값 일부를 바로잡았다[4]. 동물 실험에서는 추출물이 알코올성 지방간, 사염화탄소 간 손상, 고지방식 비만을 줄였고, 심근경색 쥐의 수축 기능 저하도 억제했다[3, 5, 20, 21, 31]. 고지방식 생쥐에게 약 5 mg/kg/일의 저용량을 16주간 준 연구에서도 체중 증가와 지방량이 줄었다[34]. 건강기능식품 개별인정형 원료 '곰피추출물'의 생산실적은 2025년판 보고서에서 생산량 2톤, 생산액 129,143천원(약 1.3억 원), 국내 판매액 459,849천원(약 4.6억 원)이었다[26]. 2019년판에서는 생산액 61,244천원(약 0.6억 원), 판매액 428,517천원(약 4.3억 원)이었다[26]."},
    {"key": "genetics", "title": "유전 정보", "body":
     "곰피는 감태속(Ecklonia) 계통 연구에 동아시아 대표 종의 하나로 포함되었다[17]. 이 연구는 핵·미토콘드리아·엽록체 DNA 서열을 함께 분석해, 감태·구로메·곰피로 이루어진 동아시아 무리가 남반구 종(E. radiata·E. maxima)과 구별되는 계통이라고 밝혔다[17]. 또 대황속과 Eckloniopsis가 감태속과 매우 가까운 자매 관계로 나타나 두 속을 따로 둘 필요가 없을 수 있다고 보았다[17].\n\n"
     "곰피에서 처음 분리된 에클로니아락톤 A·B·E의 절대 입체배치는 미국 해조 Egregia menziesii에서 다시 분리한 물질로 결정되었다[15]. 2024년에는 에클로니아락톤 A–D를 화학적으로 합성하는 통합 방법이 보고되었다[30]. 이 물질들은 이 종을 포함한 소수의 갈조류에서만 알려진 특이 대사물이다[15, 30]. 곰피의 전체 유전체, 엽록체·미토콘드리아 전체 유전체 해독 결과는 PubMed에서 확인하지 못함. 국내 품종 등록이나 육종 기록도 확인하지 못함."},
    {"key": "safety", "title": "안전성", "body":
     "곰피는 식약처 식품원료 목록에 '사용가능'으로 올라 있으며, 전체를 식품 원료로 쓸 수 있다[1]. 갈조류는 요오드가 많은 식품군으로, 한국인의 갈조류(미역·다시마) 섭취로 인한 평균 요오드 섭취량은 559.16 ± 13.15 µg/일이었고 성인 상한섭취량은 2,400 µg/일이다[27]. 같은 연구에서 말린 다시마의 요오드는 1,484.08 ± 257.12 mg/kg, 말린 미역은 204.09 ± 39.31 mg/kg이었으며, 물에 1시간 불리면 크게 줄었다[27].\n\n"
     "곰피 자체의 요오드 함량은 국가표준식품성분표와 PubMed 논문에서 확인하지 못함. 웹 검색 결과 요약에 따르면 일본 학술지의 한 논문은 츠루아라메(E. cava subsp. stolonifera)의 요오드를 4.43 mg/g(비색법)·4.84 mg/g(GC)으로 보고했으나, 원문은 열지 못했다[28]. 세포 실험에서는 곰피 추출물 200 μg/mL와 디엑콜 100 μM에서 세포독성이 나타났다[5]. 사람 대상 독성·알레르기 자료와 중금속·무기비소 잔류 자료는 공공기관 자료로 확인하지 못함."},
]

compounds = [
    {"name": "Dieckol", "name_ko": "디엑콜", "class": "플로로탄닌(에콜 이량체)", "role": "marker", "part": "엽상체 추출물(70% 에탄올)",
     "content_text": "70% 에탄올 추출물 23.7 ± 0.21 mg/g[5], 27.42 ± 0.66 mg/g[2]; 에틸아세테이트 분획 30.1 ± 0.7 µg/mg[2]; 전문 표기상 추출물 145–149 'g/g'(단위 기호 손실로 보임, 총설은 147.44 ± 2.27 μg/g으로 인용) [2, 3]",
     "activity_ko": "추출물의 지표성분으로 쓰임; 버섯 티로시나아제 IC50 2.16 µg/mL[9]; 고지혈 쥐에서 혈청 TG·TC·LDL-C 감소[12]; 지방세포 지질 축적 억제[5]",
     "source": [2, 3, 5, 9, 12]},
    {"name": "Eckol", "name_ko": "에콜", "class": "플로로탄닌", "role": "bioactive", "part": "엽상체 추출물",
     "content_text": "에틸아세테이트 분획 3.2 ± 0.2 µg/mg; 70% 에탄올 추출물 12.59 ± 0.52 μg/g(총설 인용값) [2]",
     "activity_ko": "독소루비신 처리 쥐 간세포 보호 EC50 8.3 μg/mL[33]; 고지혈 쥐 혈청 지질 감소[12]; 티로시나아제 IC50 33.2 µg/mL[9]",
     "source": [2, 9, 12, 33]},
    {"name": "Phlorofucofuroeckol A", "name_ko": "플로로푸코푸로에콜 A", "class": "플로로탄닌", "role": "bioactive", "part": "엽상체 추출물",
     "content_text": "에틸아세테이트 분획 17.7 ± 0.5 µg/mg; 70% 에탄올 추출물 12.48 ± 1.06 μg/g(총설 인용값) [2]",
     "activity_ko": "LPS 자극 대식세포의 NO·PGE2 생성 억제[13]; 쥐 염증성 통증 모델에서 진통 효과(30 mg/kg 경구)[29]",
     "source": [2, 13, 29]},
    {"name": "Phlorofucofuroeckol B", "name_ko": "플로로푸코푸로에콜 B", "class": "플로로탄닌", "role": "bioactive", "part": "엽상체 에탄올 추출물",
     "content_text": "에탄올 추출물의 주요 항염증 성분으로 확인(정량값은 초록에 없음) [32]",
     "activity_ko": "추출물의 NO 생성 억제(IC50 72 ± 1.9 μg/mL)에 기여하는 주성분 [32]",
     "source": [32]},
    {"name": "Eckstolonol", "name_ko": "엑스톨로놀", "class": "플로로탄닌(신규 화합물)", "role": "bioactive", "part": "엽상체 메탄올 추출물의 에틸아세테이트 분획",
     "content_text": "2003년 이 종에서 처음 분리·명명(함량은 초록에 없음) [7]",
     "activity_ko": "DPPH 라디칼 소거[7]; 타크린 간세포 독성 보호 EC50 62.0 µg/mL[10]",
     "source": [7, 10]},
    {"name": "Dioxinodehydroeckol", "name_ko": "다이옥시노디하이드로에콜", "class": "플로로탄닌", "role": "bioactive", "part": "엽상체 추출물",
     "content_text": "메탄올 추출물 에틸아세테이트 분획에서 7 mg 분리(정량 함량 아님) [2]",
     "activity_ko": "DPPH 소거 EC50 8.8 ± 0.4 μM이나 세포 내 ROS는 억제하지 못함 [2, 13]",
     "source": [2, 13]},
    {"name": "Phloroglucinol", "name_ko": "플로로글루시놀", "class": "페놀(플로로탄닌 단위체)", "role": "bioactive", "part": "엽상체 추출물",
     "content_text": "메탄올 추출물 에틸아세테이트 분획에서 28 mg 분리(정량 함량 아님) [2]",
     "activity_ko": "신장 균질액의 총 ROS 생성 억제(IC50 30.82 ± 2.53 μM)[2, 8]; 경쟁적 티로시나아제 억제[9]",
     "source": [2, 8, 9]},
    {"name": "7-Phloroeckol", "name_ko": "7-플로로에콜", "class": "플로로탄닌", "role": "bioactive", "part": "엽상체 메탄올 추출물",
     "content_text": "에틸아세테이트 분획(4.2 g)에서 8 mg 분리 [2]",
     "activity_ko": "PTP1B·α-글루코시다아제 억제(디엑콜·플로로푸코푸로에콜 A와 함께 α-글루코시다아제 IC50 1.37–6.13 µM) [2, 14]",
     "source": [2, 14]},
    {"name": "974-A", "name_ko": "974-A(분자량 974 플로로탄닌)", "class": "플로로탄닌(신규)", "role": "bioactive", "part": "엽상체 에탄올 추출물",
     "content_text": "에틸아세테이트 분획 63.8 g에서 24.5 mg 분리 [2]",
     "activity_ko": "버섯 티로시나아제 경쟁적 억제(L-티로신 IC50 1.57 ± 0.08 µM) [22]",
     "source": [2, 22]},
    {"name": "Fucofuroeckol A", "name_ko": "푸코푸로에콜 A", "class": "플로로탄닌", "role": "bioactive", "part": "엽상체 추출물",
     "content_text": "이 종에서 분리(함량은 초록에 없음) [23]",
     "activity_ko": "50 μM에서 UVB 유도 비만세포 탈과립·히스타민 방출 억제 [23]",
     "source": [23]},
    {"name": "Fucosterol", "name_ko": "푸코스테롤", "class": "스테롤", "role": "bioactive", "part": "엽상체(디클로로메탄·헥산 분획)",
     "content_text": "동결건조 가루 500 g의 메탄올 추출물에서 1,390 mg 분리; 갈조류 스테롤의 83–97% [2]",
     "activity_ko": "3T3-L1 지방세포의 지질 축적·PPARγ·C/EBPα 발현 억제 [19]",
     "source": [2, 19]},
    {"name": "Ecklonialactone A", "name_ko": "에클로니아락톤 A", "class": "옥실리핀(거대고리 락톤)", "role": "bioactive", "part": "엽상체",
     "content_text": "이 종에서 처음 분리; 절대배치 11S,12R,13S,15R,16S(함량 미보고) [15]",
     "activity_ko": "생물활성은 아직 충분히 밝혀지지 않음 [30]",
     "source": [15, 30]},
    {"name": "Laminarin", "name_ko": "라미나린", "class": "β-글루칸(저장 다당)", "role": "nutrient", "part": "엽상체 물 추출물",
     "content_text": "물 추출물의 저분자 다당으로 확인(정량값 없음) [2]",
     "activity_ko": "갈조류의 저장 다당; 데치기로 빠져나감 [2]",
     "source": [2]},
    {"name": "Iodine", "name_ko": "요오드", "class": "할로겐 무기원소", "role": "nutrient", "part": "엽상체",
     "content_text": "곰피 자체 값은 공공 성분표·PubMed에서 확인하지 못함; 웹 검색 요약상 일본 논문은 츠루아라메 4.43 mg/g(비색법)·4.84 mg/g(GC) 보고(원문 미확인) [28]",
     "activity_ko": "갑상선 호르몬 성분인 필수 미량원소지만 갈조류는 과잉 섭취 우려가 있음; 한국인 성인 상한섭취량 2,400 µg/일 [27]",
     "source": [27, 28]},
]

assays = [
    {"role": "literature", "compound": "Eckol, dieckol, phlorofucofuroeckol A", "compound_ko": "에콜·디엑콜·플로로푸코푸로에콜 A",
     "part": "엽상체 70% 에탄올 추출물(동결건조 분말)",
     "content": "에콜 12.0–13.0, 디엑콜 145–149, 플로로푸코푸로에콜 A 11.3–13.5(전문 텍스트 단위 'g/g', 기호 손실로 보임; 총설은 μg/g으로 인용) [2, 3]",
     "method": "HPLC-UV",
     "conditions": {
         "instrument": "PerkinElmer series 225 자동시료주입기 + 200EP 이중흡광 UV 검출기, Chromera 소프트웨어",
         "column": "Capcell Pak C18 (Shiseido) 250 × 4.6 mm, 5 μm",
         "mobile_phase": "A: 0.1% 포름산 수용액, B: 0.1% 포름산 아세토니트릴",
         "gradient": "0–7분 B 15%; 7–9분 18%; 9–35분 20%; 35–45분 25%; 45–60분 26%; 60–74분 28%; 74–79분 28%",
         "flow": "0.8 mL/min",
         "temp": "",
         "detection": "UV 254 nm",
         "injection": "10 μL",
         "sample_prep": "추출물 4 mg을 20% 메탄올 1 mL에 녹이고 0.45 μm 주사기 필터로 여과",
         "standard": "에콜 5–100 μg/mL; 에콜·디엑콜·플로로푸코푸로에콜 A 메탄올 원액 희석으로 검량선",
         "linearity": "결정계수 0.999",
         "lod": "",
         "loq": "",
         "recovery": "정밀도 RSD < 5.0%(3회 반복), 회수율은 보고 없음"},
     "rationale": "디엑콜은 곰피 추출물의 지표성분으로 쓰이며, 이 연구는 동물 실험에 쓴 추출물의 주요 플로로탄닌 3종을 정량했다; 전문(Methods) 확인 [3, 5].",
     "source": [2, 3, 5], "url": "https://doi.org/10.4062/biomolther.2016.176", "source_kind": "paper"},
    {"role": "literature", "compound": "Eckol, dieckol, phlorofucofuroeckol A", "compound_ko": "에콜·디엑콜·플로로푸코푸로에콜 A",
     "part": "엽상체 에탄올 추출물·에틸아세테이트 분획",
     "content": "디엑콜이 두 추출물 모두에서 가장 많음[6]; 에틸아세테이트 분획 플로로푸코푸로에콜 A 17.7 ± 0.5, 디엑콜 30.1 ± 0.7, 에콜 3.2 ± 0.2 µg/mg(총설 인용) [2]",
     "method": "역상 HPLC-UV(LC-MS로 확인)",
     "conditions": {
         "instrument": "",
         "column": "Thermo Hypersil Gold C18, 250 × 4.6 mm i.d., 5 μm",
         "mobile_phase": "0.1% 포름산을 넣은 아세토니트릴·물",
         "gradient": "선형 기울기(세부 시간표는 초록에 없음)",
         "flow": "",
         "temp": "",
         "detection": "UV 254 nm; 피크 확인은 LC-MS",
         "injection": "",
         "sample_prep": "",
         "standard": "",
         "linearity": "r² > 0.998",
         "lod": "0.06–0.30 μg/mL",
         "loq": "정량하한 0.2–1.0 μg/mL",
         "recovery": "정확도 93.9–108.7%, 정밀도 1.4–9.5%"},
     "rationale": "곰피의 주요 플로로탄닌 3종을 동시에 정량하는 밸리데이션된 방법을 처음 제시했다; 전문 확인 못함(초록 기준) [6].",
     "source": [2, 6], "url": "https://doi.org/10.1007/s12272-010-0407-y", "source_kind": "paper"},
    {"role": "literature", "compound": "Dieckol, phlorofucofuroeckol A", "compound_ko": "디엑콜·플로로푸코푸로에콜 A",
     "part": "엽상체 끓는 물 추출물·유기용매 추출물",
     "content": "곰피 끓는 물 추출의 회수율(유기용매 대비) 디엑콜 93%, 플로로푸코푸로에콜 A 86% [18]",
     "method": "역상 HPLC(피크 높이 검량)",
     "conditions": {
         "instrument": "", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "",
         "injection": "", "sample_prep": "끓는 물 추출과 유기용매 추출 비교",
         "standard": "디엑콜: 농도(mg/mL) = 16.56 × 피크 높이(cm) + 0.44; 플로로푸코푸로에콜 A: 20.60 × 피크 높이 + 0.11",
         "linearity": "상관계수 0.996(디엑콜), 0.999(플로로푸코푸로에콜 A)",
         "lod": "", "loq": "", "recovery": ""},
     "rationale": "감태·곰피·대황 세 종의 주요 플로로탄닌 2종을 일상적으로 정량하려고 개발한 방법이며, 여기에는 곰피 값만 옮겼다; 전문 확인 못함(초록 기준) [18].",
     "source": [18], "url": "https://pubmed.ncbi.nlm.nih.gov/25004758/", "source_kind": "paper"},
]

d = {
    "slug": "ecklonia-stolonifera",
    "name_ko": "곰피",
    "name_en": "Ecklonia stolonifera (gompi; tsuruarame)",
    "scientific_name": "Ecklonia stolonifera Okamura",
    "aliases": ["곰피추출물", "Tsuruarame", "ツルアラメ"],
    "sections": sections,
    "compounds": compounds,
    "markers": [],
    "assays": assays,
    "nutrients": [],
    "production": [],
    "gi": [],
    "orgs": [],
    "world": [],
    "sources": sources,
}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("ok", len(sources), len(compounds))
