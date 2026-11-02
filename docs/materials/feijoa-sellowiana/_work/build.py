import json
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "dossier.json"
ACC = "2026-11-02"


def pm(n, title, doi, cite, pmid, pmc=None, full=False, url=None):
    tag = f"PMID {pmid}" + (f", {pmc}" if pmc else "") + (", 전문 확인" if full else ", 초록 확인")
    return {"n": n, "title": f"{title} — {cite} ({tag})",
            "url": url or f"https://doi.org/{doi}", "publisher": "PubMed", "accessed": ACC}


S = [
    {"n": 1, "title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 파인애플구아바열매·파인애플구아바주스(Feijoa sellowiana Berg; 이명 페이조아(Feijoa); Feijoa, Pineapple Guava), 사용가능, 사용가능부위: 열매; 별도 행 Feijoa열매·Feijoa꽃(Acca sellowiana (O.Berg) Burret; Pineapple guava), 사용가능, 사용가능부위: 꽃, 열매; 구아바(Psidium guajava)·Strawberry guave·Costa Rican Guava·브라질구와바·구아바잎 추출물(고시형) 행 대조 (로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json)",
     "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
    pm(2, "Nutritional Characteristics and Antimicrobial Activity of Australian Grown Feijoa (Acca sellowiana)", "10.3390/foods8090376", "Foods 2019;8(9):376", "31480592", "PMC6770449", True),
    pm(3, "Extraction Optimization, Antioxidant Capacity and Phenolic Profiling of Extracts from Flesh, Peel and Whole Fruit of New Zealand Grown Feijoa Cultivars", "10.3390/antiox8050141", "Antioxidants (Basel) 2019;8(5):141", "31117250", "PMC6562890", True),
    pm(4, "Evaluating Whole Fruit Feijoa Powder for Type 2 Diabetes Risk Prevention: A Randomised Controlled Trial", "10.1111/dom.71270", "Diabetes Obes Metab 2026;28(11):10709-10724", "42677597", "PMC13646332", True),
    pm(5, "Construction of a High-Density Genetic Map of Acca sellowiana (Berg.) Burret, an Outcrossing Species, Based on Two Connected Mapping Populations", "10.3389/fpls.2021.626811", "Front Plant Sci 2021;12:626811", "33708232", "PMC7940835", True),
    pm(6, "The ecological footprint of Acca sellowiana domestication maintains the residual vertebrate diversity in threatened highlands of Atlantic Forest", "10.1371/journal.pone.0195199", "PLoS One 2018;13(4):e0195199", "29617455", "PMC5884537", True),
    pm(7, "A first de novo transcriptome assembly of feijoa (Acca sellowiana [Berg] Burret) reveals key genes involved in flavonoid biosynthesis", "10.1002/tpg2.20501", "Plant Genome 2024;17(3):e20501", "39162148", "PMC12807317", True),
    pm(8, "Comparison of Different Green Extraction Techniques Used for the Extraction of Targeted Flavonoids from Edible Feijoa (Acca sellowiana (O.Berg) Burret) Flowers", "10.3390/plants12071461", "Plants (Basel) 2023;12(7):1461", "37050087", "PMC10096538", True),
    pm(9, "Phylogenomic relationship of feijoa (Acca sellowiana (O.Berg) Burret) with other Myrtaceae based on complete chloroplast genome sequences", "10.1007/s10709-017-9954-1", "Genetica 2017;145(2):163-174", "28185042"),
    pm(10, "Characterization of phenolic compounds and aroma active compounds in feijoa juice from four New Zealand grown cultivars by LC-MS and HS-SPME-GC-O-MS", "10.1016/j.foodres.2019.108873", "Food Res Int 2020;129:108873", "32036883"),
    pm(11, "Sensory approach and chiral analysis for determination of odour active compounds from feijoa (Acca sellowiana)", "10.1016/j.foodchem.2020.126383", "Food Chem 2020;317:126383", "32078992"),
    pm(12, "Volatilome study of the feijoa fruit [Acca sellowiana (O. Berg) Burret.] with headspace solid phase microextraction and gas chromatography coupled with mass spectrometry", "10.1016/j.foodchem.2020.127109", "Food Chem 2020;328:127109", "32454261"),
    pm(13, "Compositional Analysis and Aroma Evaluation of Feijoa Essential Oils from New Zealand Grown Cultivars", "10.3390/molecules24112053", "Molecules 2019;24(11):2053", "31146480", "PMC6600377"),
    pm(14, "Micropropagation systems of Feijoa (Acca sellowiana (O. Berg) Burret)", "10.1007/978-1-62703-074-8_4", "Methods Mol Biol 2013;11013:45-62", "23179689"),
    pm(15, "Subtropical and flower crops breeding at the Subtropical Scientific Centre", "10.18699/VJ21.047", "Vavilovskii Zhurnal Genet Selektsii 2021;25(4):420-432", "35088014", "PMC8765774"),
    pm(16, "First Report of Phytophthora citrophthora Causing Fruit Brown Rot of Feijoa in Italy", "10.1094/PDIS.2001.85.1.97A", "Plant Dis 2001;85(1):97", "30832086"),
    pm(17, "The effects of Feijoa sellowiana fruits on the antioxidant defense system, lipid peroxidation, and tissue morphology in rats", "10.3109/13880209.2011.608074", "Pharm Biol 2012;50(3):318-325", "22133107"),
    {"n": 18, "title": "[Juice from feijoa fruit] — Aptechn Delo 1964;13:24-6 (PMID 14316128, 러시아어, 초록 없음: 제목과 MeSH·키워드(Azerbaijan, Iodides, Iodine)만 확인)",
     "url": "https://pubmed.ncbi.nlm.nih.gov/14316128/", "publisher": "PubMed", "accessed": ACC},
    pm(19, "Chemical characterization, in vivo safety profile and effects of the extract from unconventional food plant Acca sellowiana (O. BERG) Burret on endothelial cells under glucose overload", "10.1016/j.jpba.2024.116304", "J Pharm Biomed Anal 2024;248:116304", "38906070"),
    pm(20, "Anti-inflammatory and anti-nociceptive activities of polyphenols from Feijoa fruit and leaves", None, "Pak J Pharm Sci 2021;34(4):1445-1448", "34799320", url="https://pubmed.ncbi.nlm.nih.gov/34799320/"),
    pm(21, "The fate of Salmonella enterica and Listeria monocytogenes in the pulp of eight native Brazilian and exotic fruits", "10.1016/j.ijfoodmicro.2024.110783", "Int J Food Microbiol 2024;420:110783", "38851046"),
    pm(22, "Exploring matrix effects in liquid chromatography-tandem mass spectrometry determination of pesticide residues in tropical fruits", "10.1007/s00216-015-8586-5", "Anal Bioanal Chem 2015;407(13):3667-3681", "25772561"),
    pm(23, "Three new flavonoids, proanthocyanidin, and accompanying phenolic constituents from Feijoa sellowiana", "10.1080/09168451.2017.1412246", "Biosci Biotechnol Biochem 2018;82(1):31-41", "29297255"),
    pm(24, "Characterization of physicochemical properties, flavor volatiles and phenolic compounds of feijoa fruit varieties", "10.1016/j.foodchem.2023.136074", "Food Chem 2023;419:136074", "37044055"),
    pm(25, "Morphoanatomy, patterns of development and types of feijoa (Acca sellowiana) flower buds in tropical and subtropical climates", "10.1007/s00425-025-04825-8", "Planta 2025;262(5):113", "41032104"),
    pm(26, "Evaluation of Antioxidant Systems and Ascorbate-Glutathione Cycle in Feijoa Edible Flowers at Different Flowering Stages", "10.3390/foods9010095", "Foods 2020;9(1):95", "31963228", "PMC7022405"),
    pm(27, "Evaluation of bioactive compounds and antioxidant capacity of edible feijoa (Acca sellowiana (O. Berg) Burret) flower extracts", "10.1007/s13197-020-04239-2", "J Food Sci Technol 2020;57(6):2051-2060", "32431331", "PMC7230090"),
    pm(28, "Characterization of 10 new nuclear microsatellite markers in Acca sellowiana (Myrtaceae)", "10.3732/apps.1400020", "Appl Plant Sci 2014;2(6):1400020", "25202632", "PMC4103439"),
    pm(29, "Structural characteristics, functional properties, antioxidant and hypoglycemic activities of pectins from feijoa (Acca sellowiana) peel", "10.1016/j.foodchem.2023.136819", "Food Chem 2023;428:136819", "37437357"),
    pm(30, "Feijoa sellowiana derived natural Flavone exerts anti-cancer action displaying HDAC inhibitory activities", "10.1016/j.biocel.2007.05.010", "Int J Biochem Cell Biol 2007;39(10):1902-1914 (2024년 정정문 PMID 39013695 있음)", "17604209"),
    pm(31, "Polyphenolic Profile and Biological Activities in HT29 Intestinal Epithelial Cells of Feijoa sellowiana Fruit Extract", "10.3390/ijms26167851", "Int J Mol Sci 2025;26(16):7851", "40869171", "PMC12386295"),
    pm(32, "Feijoa [Acca sellowiana (Berg) Burret] accessions characterization and discrimination by chemometrics", "10.1002/jsfa.10585", "J Sci Food Agric 2020;100(15):5373-5384", "32542666"),
    pm(33, "Morphophysiological changes of Acca sellowiana (Myrtaceae: Myrtoideae) saplings under shade gradient", "10.1590/1519-6984.252364", "Braz J Biol 2022;84:e252364", "35019092"),
    pm(34, "Microbial and Sensory Effects of Combined High Hydrostatic Pressure and Dense Phase Carbon Dioxide Process on Feijoa Puree", "10.1111/1750-3841.13083", "J Food Sci 2015;80(11):E2478-2485", "26444875"),
    pm(35, "Integrating the use of feijoa pulp and peel (Acca sellowiana) in kombucha fermentation: a sustainable approach to promote functionality and sensory acceptability", "10.1016/j.foodres.2026.118781", "Food Res Int 2026;231(Pt 2):118781", "41819930"),
    pm(36, "The Potential of Universal Primers for Barcoding of Subtropical Crops: Actinidia, Feijoa, Citrus, and Tea", "10.3390/ijms26146921", "Int J Mol Sci 2025;26(14):6921", "40725170", "PMC12295962"),
]

sections = [
    {"key": "overview", "title": "한눈에 보기", "body":
     "파인애플구아바(페이조아, Feijoa sellowiana)는 도금양과(Myrtaceae)에 속하는 늘푸른 작은 과일나무로, 지금은 학명을 Acca sellowiana로 쓰는 경우가 많다[5, 7]. 원산지는 브라질 남부와 우루과이 북부이며, 향이 강한 열매와 달고 도톰한 꽃잎을 먹는다[7]. "
     "식약처 「식품원료 목록」에는 '파인애플구아바열매'와 '파인애플구아바주스'(학명 Feijoa sellowiana Berg, 이명 페이조아) 두 행이 '사용가능' 원료로 올라 있고, 사용 조건은 '사용가능부위 : 열매'다[1]. "
     "같은 목록에는 현재 학명 Acca sellowiana (O.Berg) Burret로 된 'Feijoa열매'·'Feijoa꽃' 행이 따로 있으며, 이 행의 사용 조건은 '사용가능부위 : 꽃, 열매'다[1]. 따라서 열매는 두 학명 모두로 식품원료이고, 꽃은 Acca sellowiana 행으로 식품원료이며, 잎·가지는 목록에서 사용 가능 부위로 확인하지 못함. "
     "이 종을 원재료로 하는 건강기능식품 고시형 원료는 없다[1].\n\n"
     "익은 열매 100 g(껍질 포함, 호주산)에는 비타민 C 63 mg, 식이섬유 6.8 g, 칼륨 255 mg이 들어 있었다[2]. 과육에는 카테킨과 프로시아니딘 B1이, 껍질에는 플라본(flavone)이 특히 많다[3]. "
     "특유의 향은 메틸 벤조에이트가 주로 낸다[10, 11]. "
     "사람 대상 연구로는 껍질째 동결건조한 열매 가루를 하루 1150 mg씩 6개월 먹인 무작위 대조시험이 있으나, 체중과 공복혈당에서는 위약과 차이가 없었다[4].",
     },
    {"key": "history", "title": "역사", "body":
     "페이조아는 브라질 남부와 우루과이 북부가 원산지이며, 브라질에서는 해발 800 m 이상의 아라우카리아(Araucaria angustifolia) 혼합림 고원에 주로 자란다[6]. "
     "콜럼버스 이전 원주민(Xokleng·Kaingang)이 이 숲을 넓히면서 페이조아도 함께 퍼졌고, 현지 주민의 가지치기·옮겨심기·번식으로 일부 집단은 열매가 커지는 초기 작물화를 겪었다[6]. "
     "20세기 초부터 여러 나라에 들어갔고, 지금은 미국·이탈리아·콜롬비아·뉴질랜드·호주에서 주로 열매용, 일부는 관상용으로 재배한다[7]. "
     "이탈리아 시칠리아에는 20세기 초에 들어와 관상수와 과일나무로 심겼다[16].\n\n"
     "옛 소련 아제르바이잔에서는 1960년대에 페이조아 열매즙을 약국 제제로 다룬 보고가 있으며, 이 논문은 요오드를 주제어로 달고 있다[18]. "
     "터키 민간요법에서는 열매를 갑상샘종 치료에 썼다고 소개된다[17]. "
     "브라질에서는 1990년에 시작한 육종 사업으로 상업 품종 4개가 나왔고, 1996년부터 유전자원 평가 시험이 이어졌다[14, 32]. "
     "우루과이는 국립 연구기관과 대학이 함께하는 자생과수 육종 사업으로 2008년 교배 집단을 만들었다[5]. "
     "러시아 아열대과학센터가 육성한 페이조아 3품종은 러시아 국가 품종 등록부에 올라 있다[15].",
     },
    {"key": "biology", "title": "식물학적 특징", "body":
     "페이조아는 도금양과 도금양족(Myrteae)의 늘푸른 작은 나무다[7]. 염색체는 2n = 22인 2배체이고, 게놈 크기는 약 245 Mb로 작으며, 다른 그루의 꽃가루를 받아 열매를 맺는 타가수정 식물이다[5]. "
     "꽃은 새와 벌이 꽃가루를 옮기며, 열매는 20–250 g으로 크고 씨는 약 3 mm로 작다[6]. "
     "아열대 원산지에서는 봄에 꽃이 피지만 콜롬비아 같은 열대에서는 일 년 내내 꽃이 피며, 기후에 따라 꽃눈이 생기는 방식도 다르다[25].\n\n"
     "열매는 매끄럽고 부드러운 초록 껍질 안에 투명한 젤리 같은 씨 부분과, 껍질 가까이의 조금 까슬한 불투명 과육이 있다[2]. "
     "껍질은 먹을 수 있으며, 폴리페놀과 비타민 C가 과육보다 유의하게 많다[2]. 13개 품종 비교에서 열매 전체의 당도는 10.1–18.0 °Brix로 품종 차이가 컸다[24]. "
     "꽃잎은 도톰하고 달아 샐러드나 우려 마시는 차 재료로 쓰인다[7]. 꽃 전체 추출물에는 안토시아닌이 115.3 mg/L 들어 있어 붉은색을 띤다[27]. "
     "꽃은 꽃잎이 완전히 펴진 단계에서 생리활성 성분이 많아 이 무렵 따는 것이 좋다고 제안되었다[26]. "
     "원산지 숲에서는 20종의 척추동물이 열매를 먹었고, 아라우카리아 씨앗이 없는 철에 중요한 먹이가 된다[6].",
     },
    {"key": "related_species", "title": "이름과 가까운 종", "body":
     "페이조아는 같은 도금양과의 구아바속(Psidium)과 가까워 '파인애플구아바' 또는 '구아바스틴'으로도 불리지만 다른 속이다[2]. "
     "현재 학명은 Acca sellowiana (O.Berg) Burret이고 Feijoa sellowiana는 그 이명이며, 원산지에서는 'Guayabo del país'라고 부른다[7, 14]. "
     "식약처 목록에도 두 학명이 서로 다른 행으로 올라 있어, Feijoa sellowiana 행은 열매만, Acca sellowiana 행은 꽃과 열매를 허용한다[1].\n\n"
     "식약처 목록의 구아바(Psidium guajava)는 잎과 열매를 모두 쓸 수 있고, 구아바잎 추출물은 건강기능식품 고시형 원료다[1]. 이와 달리 파인애플구아바의 잎은 목록에서 사용 가능 부위로 확인하지 못함. "
     "같은 목록의 Strawberry guave(Psidium cattleianum)·Costa Rican Guava(Psidium friedrichsthalianum)·브라질구와바(Psidium guineense 등)는 열매만 쓸 수 있다[1]. "
     "엽록체 게놈 비교에서 페이조아와 가장 가까운 종은 피탕가(Eugenia uniflora)였다[9]. "
     "이름에 '구아바'가 들어가 혼동하기 쉬우므로, 원료를 고를 때는 학명(Acca sellowiana 또는 Feijoa sellowiana)과 부위를 함께 확인해야 한다[1, 7].",
     },
    {"key": "cultivation", "title": "재배와 산지", "body":
     "원산지 브라질에서는 해발 800 m 이상 고원에 자라며, 서늘한 겨울과 건조한 여름이 열매 품질에 좋다고 알려져 있다[3, 6]. "
     "브라질은 상업 재배지가 적고 가공 잠재력이 높은 작물로 보고 1996년부터 유전자원을 평가해 왔다[32]. "
     "묘목은 햇빛을 그대로 받거나 30% 이하로 그늘을 줄 때 키와 굵기가 가장 잘 자랐다[33]. "
     "꺾꽂이와 접붙이기는 효율이 낮아, 기관 형성과 체세포배 발생을 이용한 조직배양 대량 번식법이 개발되었다[14].\n\n"
     "뉴질랜드에서는 Apollo·Unique·Opal Star·Wiki Tu 같은 품종을 북섬에서 상업 재배하며, 품종에 따라 페놀 함량과 향이 다르다[3, 10]. "
     "열대인 콜롬비아에서도 재배하며, 이곳 열매의 휘발성 성분이 따로 분석되었다[12, 25]. "
     "이탈리아 시칠리아에서는 Phytophthora 균에 의한 열매 갈색썩음병이 보고되었다[16]. "
     "국내 재배 면적·생산량 통계는 확인하지 못함. "
     "국가 생산 통계(FAOSTAT 등)에서 페이조아를 따로 집계한 값도 확인하지 못함.",
     },
    {"key": "processing", "title": "가공과 이용", "body":
     "식약처 목록에는 생열매 외에 '파인애플구아바주스'가 원료명으로 따로 올라 있다[1]. "
     "페이조아 퓌레(pH 3.2)는 600 MPa 고압 처리에 이산화탄소를 더하면 미생물을 더 잘 줄이면서 단맛을 더한 제품의 관능 품질을 지킬 수 있었다[34]. "
     "과육과 껍질 차를 넣은 콤부차는 시트르산·말산과 플라보노이드가 늘었고 전반적 기호도 7.2점을 받았다[35]. "
     "주스 가공 뒤 남는 껍질은 향기 성분이 풍부한 정유와 펙틴의 원료로 연구되며, 껍질 펙틴은 주로 갈락투론산·아라비노스·갈락토스·람노스로 이루어져 있다[13, 29].\n\n"
     "페놀 성분을 뽑을 때 과육과 열매 전체는 70% 에탄올·50 °C·30분, 껍질은 50% 에탄올·50 °C·60분이 가장 좋았다[3]. "
     "꽃은 초음파 추출로 플라보놀을, 초임계 이산화탄소(300 bar) 추출로 플라본을 선택적으로 얻을 수 있었다[8]. "
     "뉴질랜드 임상시험에서는 껍질째 동결건조한 열매 가루 1150 mg을 미세결정셀룰로스와 섞은 분말을 매일 먹였으며, 이 가루의 알려진 폴리페놀의 약 60%가 카테킨류였다[4]. "
     "국내에서 파인애플구아바를 원료로 한 건강기능식품 생산실적은 식약처 「식품 등의 생산실적」 자료에서 확인하지 못함.",
     },
    {"key": "genetics", "title": "유전 정보", "body":
     "페이조아는 염색체 2n = 22의 2배체이며, 도금양과에서 널리 보존된 기본수 x = 11을 가진다[5]. "
     "우루과이의 두 교배 집단(160·184개체)을 GBS(염기서열 기반 유전형 분석)로 분석해 SNP 1,897개, 총 길이 1,314 cM의 고밀도 통합 유전자 지도를 만들었다[5]. "
     "엽록체 게놈은 159,370 bp의 고리 모양으로, 큰 단일복제 부위 88,028 bp, 작은 단일복제 부위 18,598 bp, 역반복 부위 26,372 bp로 이루어진다[9].\n\n"
     "잎과 꽃 조직 11개 시료로 만든 첫 전사체는 221,649개 전사체를 담고 있고, 이 가운데 107,612개에 기능이 주석되었다[7]. "
     "전사인자 후보는 4068개였고, 꽃이 자라는 동안 플라보노이드 경로 효소 14종에 해당하는 71개 전사체의 발현이 달라졌다[7]. "
     "핵 SSR 표지 10개는 좌위당 대립유전자 4–27개를 보여 집단 유전 연구와 육종에 쓰인다[28]. "
     "지역 육성 품종·계통 비교에서는 엽록체 표지 5개로 페이조아에서 SNP 5개와 InDel 4개를 찾아 품종 식별 가능성을 보였다[36]. "
     "브라질과 우루과이 집단 사이에 꽃눈 발달 방식이 달라 초기 종분화 신호일 수 있다는 해석도 있다[25].",
     },
    {"key": "safety", "title": "안전성", "body":
     "식약처 목록은 Feijoa sellowiana 이름으로는 열매만, Acca sellowiana 이름으로는 꽃과 열매만 식품원료로 허용한다[1]. "
     "과체중·당뇨 전단계 성인 97명을 대상으로 한 6개월 무작위 대조시험에서 열매 가루(하루 1150 mg) 군과 위약 군에 이상사례가 1건씩 보고되었고, 열매 가루 군의 1건은 식사대용 제품에 대한 불내성이었다[4]. "
     "쥐에 열매 추출물 50 mg/kg을 4주간 먹였을 때 주요 장기의 조직 손상은 보이지 않았다[17]. "
     "생쥐 실험에서 열매·잎 폴리페놀 추출물은 1 g/kg까지 해로운 증상을 보이지 않았다[20]. 껍질 물 추출물은 브라인슈림프 독성 시험에서 독성이 없었다[19].\n\n"
     "호주산 열매에서 알루미늄은 0.25 mg/kg(생중량), 납·비소·크롬은 0.005 mg 미만, 수은·카드뮴은 0.002 mg 미만으로 상한 섭취량보다 훨씬 낮았다[2]. "
     "요오드는 '100 g당 3 mg'이라는 2차 인용이 있으나[5], 호주산 실측에서는 검사한 7가지 무기질 가운데 요오드가 가장 적어 두 자료가 크게 다르다[2]. "
     "과육(pH 3.3 미만)에 넣은 살모넬라·리스테리아는 10–20 °C에서 1 log 미만으로만 줄어 살아남을 수 있으므로, 생과즙은 위생 관리가 필요하다[21]. "
     "콜롬비아에서는 페이조아를 포함한 열대과일 12종의 잔류농약 다성분 분석법(LC-MS/MS)이 개발되었다[22]. 국내외 실제 잔류 실태 값은 확인하지 못함. "
     "공공기관의 알레르기 정보와 사람 알레르기 사례 보고도 확인하지 못함.",
     },
]

compounds = [
    {"name": "Flavone", "name_ko": "플라본(2-페닐크로몬)", "class": "플라본", "role": "marker", "part": "열매 껍질·열매 전체·꽃",
     "content_text": "껍질 3302.30–5871.10 μg/g dw, 열매 전체 602.61–1025.49 μg/g dw(뉴질랜드 4품종, LC-ESI-MS/MS); 과육보다 껍질에 최대 1000배 많음[3]; 꽃 초임계 CO2(300 bar) 추출물 12.69 mg/g dm, 초음파 추출 114.02–183.69 μg/g dm[8]",
     "activity_ko": "열매 아세톤 추출물의 활성 성분으로 분리됨; 사람 골수성 백혈병 세포에서 HDAC 억제와 함께 세포자멸사 유도[30]", "source": [3, 8, 30]},
    {"name": "Catechin", "name_ko": "카테킨", "class": "플라반-3-올", "role": "marker", "part": "과육·열매 전체·주스",
     "content_text": "과육 370.48–1375.87 μg/g dw, 열매 전체 328.07–1436.49 μg/g dw[3]; 주스 (+)-카테킨 121.80–472.75 μg/mL[10]",
     "activity_ko": "과육의 주된 페놀 성분; 임상시험 열매 가루의 알려진 폴리페놀 약 60%가 카테킨류[3, 4]", "source": [3, 10, 4]},
    {"name": "Procyanidin B1", "name_ko": "프로시아니딘 B1", "class": "프로안토시아니딘(이량체)", "role": "bioactive", "part": "과육·열매 전체·주스",
     "content_text": "과육 305.69–776.18 μg/g dw, 열매 전체 203.01–721.87 μg/g dw[3]; 주스 209.78–511.07 μg/mL로 가장 많음[10]",
     "activity_ko": "과육·주스의 주요 항산화 페놀[3, 10]", "source": [3, 10]},
    {"name": "Procyanidin B2", "name_ko": "프로시아니딘 B2", "class": "프로안토시아니딘(이량체)", "role": "bioactive", "part": "과육",
     "content_text": "과육 19.86–64.71 μg/g dw[3]; 13품종 비교에서 B형 사량체·이량체, C형 삼량체가 모든 부위에서 가장 많음[24]",
     "activity_ko": "응축형 탄닌으로 과육 폴리페놀의 한 축[3, 24]", "source": [3, 24]},
    {"name": "Epicatechin", "name_ko": "에피카테킨", "class": "플라반-3-올", "role": "bioactive", "part": "과육",
     "content_text": "과육 29.33–76.16 μg/g dw[3]", "activity_ko": "과육 항산화 성분[3]", "source": [3]},
    {"name": "Ellagic acid", "name_ko": "엘라그산", "class": "페놀산(엘라지탄닌 구성단위)", "role": "bioactive", "part": "과육·꽃",
     "content_text": "과육 17.66–47.47 μg/g dw, 열매 전체 엘라그산의 절반 이상이 과육에 있음[3]; 꽃 전체 추출물 7.9 mg/L[27]",
     "activity_ko": "과육·꽃의 가수분해형 탄닌 계열 항산화 성분[3, 27]", "source": [3, 27]},
    {"name": "Pedunculagin", "name_ko": "페둔쿨라긴", "class": "엘라지탄닌", "role": "bioactive", "part": "과육(수용성 알코올 추출물)",
     "content_text": "HHDP-포도당·페둔쿨라긴 등 가수분해형 탄닌이 풍부(개별 함량 초록에 미기재), 추출물 총폴리페놀 8.07 mg/g GAE[31]",
     "activity_ko": "장 상피세포(HT29)에서 160 µg/mL까지 세포독성 없이 사이토카인 손상을 줄임[31]", "source": [31]},
    {"name": "Gossypetin", "name_ko": "고시페틴 배당체", "class": "플라보놀 배당체", "role": "bioactive", "part": "열매·꽃눈·잎",
     "content_text": "새 고시페틴 배당체 3종을 포함한 페놀 21종 분리(함량 초록에 미기재)[23]",
     "activity_ko": "버섯 티로시나아제 억제 시험에서 억제 효과[23]", "source": [23]},
    {"name": "Cyanidin 3-glucoside", "name_ko": "시아니딘-3-글루코사이드(크리산테민)", "class": "안토시아닌", "role": "bioactive", "part": "꽃",
     "content_text": "꽃 DES 추출물 90.81 µg/g dm[8]; 꽃 전체 추출물 총안토시아닌 115.3 mg/L[27]",
     "activity_ko": "꽃잎의 붉은 색소이자 주요 안토시아닌[8]", "source": [8, 27]},
    {"name": "Ascorbic acid", "name_ko": "비타민 C(아스코르브산)", "class": "비타민", "role": "nutrient", "part": "열매(껍질 포함)",
     "content_text": "63 mg/100 g FW(62.8 mg, 호주산, UPLC-PDA, 총 비타민 C)[2]; 2차 인용값 28 mg/100 g[5]",
     "activity_ko": "100 g이 호주 성인 권장량(45 mg/일)의 140%[2]", "source": [2, 5]},
    {"name": "Methyl benzoate", "name_ko": "메틸 벤조에이트", "class": "에스터(향기 성분)", "role": "marker", "part": "열매·주스",
     "content_text": "주스 13.62–52.62 μg/g[10]; 콜롬비아산 열매 휘발성 성분의 50%를 메틸·에틸·(Z)-3-헥세닐 벤조에이트가 차지[12]",
     "activity_ko": "특유의 '페이조아 같은' 향; 향기 재조합·생략 시험에서 핵심 향기 성분[10, 11]", "source": [10, 11, 12]},
    {"name": "Ethyl butanoate", "name_ko": "에틸 부타노에이트", "class": "에스터(향기 성분)", "role": "bioactive", "part": "열매",
     "content_text": "향기 활성값(OAV)이 높은 성분으로 정량(수치 초록에 미기재)[11]",
     "activity_ko": "과일 향 기여[11]", "source": [11]},
    {"name": "Linalool", "name_ko": "리날룰", "class": "모노테르펜 알코올", "role": "bioactive", "part": "열매·껍질 정유",
     "content_text": "R형이 주(Quimba 품종 R:S 75:25, Mammoth 95:5)[11]; 껍질 정유의 핵심 향기 성분 중 하나[13]",
     "activity_ko": "꽃 향 기여[11]", "source": [11, 13]},
    {"name": "Abscisic acid", "name_ko": "앱시스산", "class": "식물호르몬(세스퀴테르페노이드)", "role": "bioactive", "part": "열매(특히 껍질)",
     "content_text": "임상시험 열매 가루 하루 1150 mg에서 54 μg/일 공급[4]",
     "activity_ko": "혈당 조절 후보 성분으로 제시되었으나 임상시험에서 공복혈당 차이는 없음[4]", "source": [4]},
    {"name": "Potassium", "name_ko": "칼륨", "class": "무기질", "role": "nutrient", "part": "열매(껍질 포함)",
     "content_text": "255 mg/100 g FW(호주산; 이전 보고 172 mg/100 g FW)[2]",
     "activity_ko": "검사한 무기질 7종 중 가장 많음[2]", "source": [2]},
]

nutrients = [{"form": "생과(껍질 포함, 호주 빅토리아산, 동결건조 분말 분석값의 생중량 환산 포함)", "basis": "100 g 생중량(FW)",
              "items": [{"name": "비타민 C", "value": 63, "unit": "mg"},
                        {"name": "식이섬유", "value": 6.8, "unit": "g"},
                        {"name": "칼륨", "value": 255, "unit": "mg"},
                        {"name": "단백질", "value": 0.73, "unit": "g"},
                        {"name": "지방", "value": 0.43, "unit": "g"},
                        {"name": "판토텐산", "value": 0.2, "unit": "mg"}],
              "source": [2]}]

E = {k: "" for k in ["instrument", "column", "mobile_phase", "gradient", "flow", "temp", "detection", "injection", "sample_prep", "standard", "linearity", "lod", "loq", "recovery"]}

assays = [
    {"role": "literature", "compound": "Flavone", "compound_ko": "플라본(카테킨·프로시아니딘 B1 등 페놀 15종 동시 정량)",
     "part": "열매 과육·껍질·열매 전체(뉴질랜드 Apollo·Unique·Opal Star·Wiki Tu, 동결건조 분말)",
     "content": "플라본 껍질 3302.30–5871.10 μg/g dw, 열매 전체 602.61–1025.49 μg/g dw; 카테킨 과육 370.48–1375.87 μg/g dw[3]",
     "method": "LC-ESI-MS/MS(MRM, 삼중사중극자)",
     "conditions": {**E,
                    "instrument": "UHPLC(DAD 부착)–삼중사중극자 질량분석기, ESI",
                    "column": "역상 Poroshell 120 EC-C18, 2.1 × 100 mm, 4 μm (Agilent)",
                    "mobile_phase": "A 0.2% 포름산 수용액, B 0.2% 포름산 아세토니트릴",
                    "gradient": "0분 5% B; 2분 6%; 12분 7%; 16분 9%; 26분 10%; 27분 11%; 28분 15%; 30분 20%; 40분 60%; 45분 5%",
                    "flow": "0.5 mL/min", "temp": "35 °C",
                    "detection": "MRM(표준품별 충돌에너지 최적화); 모세관 전압 3.5 kV, 분무기 45 psi, 건조가스 250 °C·10 L/min, 시스가스 280 °C·11 L/min",
                    "injection": "3 μL",
                    "sample_prep": "동결건조 분말; 과육·열매 전체는 70% 에탄올, 1:30, 50 °C, 30분; 껍질은 50% 에탄올, 1:30, 50 °C, 60분",
                    "standard": "갈산·카페산·엘라그산·퀘르세틴·플라본·카테킨·에피카테킨·에피갈로카테킨·에피카테킨 갈레이트·EGCG·퀘르세틴-3-갈락토사이드·퀘르세틴-3-람노사이드·미리세틴 배당체 2종·프로시아니딘 B1·B2 (16종)",
                    "linearity": "모든 성분 R² > 0.99",
                    "lod": "최저 퀘르세틴-3-람노사이드 0.02 μg/L, 최고 EGCG 0.099 μg/mL(원문 표기 그대로)",
                    "loq": "최저 퀘르세틴-3-람노사이드 0.086 μg/L, 최고 EGCG 0.4 μg/mL(원문 표기 그대로)",
                    "recovery": "90–110%"},
     "rationale": "플라본은 껍질에 몰려 있고 카테킨·프로시아니딘 B1은 과육의 주성분이라 부위·품종 구별 지표가 됨; 일·간 정밀도도 검증됨; 전문 확인, 성분별 LOD·LOQ 표는 본문에 없어 범위만 옮김[3].",
     "source": [3], "url": "https://doi.org/10.3390/antiox8050141", "source_kind": "paper"},
    {"role": "literature", "compound": "Ascorbic acid", "compound_ko": "비타민 C(L-아스코르브산 + 디하이드로아스코르브산 환원)",
     "part": "열매 전체(껍질 포함)·과육·껍질(호주산, 동결건조 분말)",
     "content": "열매 전체 63 mg/100 g FW(62.8 mg); 껍질이 과육보다 유의하게 많음[2]",
     "method": "UPLC-PDA",
     "conditions": {**E,
                    "instrument": "UPLC-PDA (Waters)",
                    "column": "HSS-T3, 100 × 2.1 mm, 1.8 μm (Waters)",
                    "mobile_phase": "0.1% 포름산 수용액",
                    "gradient": "등용매",
                    "flow": "0.3 mL/min", "temp": "25 °C",
                    "sample_prep": "분말 200 mg을 3% 메타인산·8% 아세트산·1 mM EDTA 용액으로 추출, 디하이드로아스코르브산을 L-AA로 환원 후 분석(총 비타민 C)",
                    "standard": "L-아스코르브산 외부 검량선"},
     "rationale": "비타민 C는 열매 영양 가치의 대표 지표로, 이 연구에서 이전 보고보다 높게 측정됨; 전문 확인, 검출 파장·주입량·검출한계·회수율은 원문에 없음[2].",
     "source": [2], "url": "https://doi.org/10.3390/foods8090376", "source_kind": "paper"},
    {"role": "literature", "compound": "Flavone", "compound_ko": "플라본(하이퍼로사이드·이소퀘르시트린·퀘르세틴·크리산테민 동시 정량)",
     "part": "꽃(이탈리아 사르데냐 재배, 동결건조 분말)",
     "content": "플라본 초임계 CO2 300 bar 12.69 mg/g dm; 초음파 추출 114.02–183.69 µg/g dm; 크리산테민 최고 90.81 µg/g dm[8]",
     "method": "HPLC-PDA",
     "conditions": {**E,
                    "instrument": "HPLC(4원 펌프·자동주입기·다이오드 배열 검출기)",
                    "column": "Zorbax Eclipse Plus C18, 100 × 4.6 mm, 5 µm (Agilent)",
                    "mobile_phase": "A 0.2 M 인산, B 아세토니트릴",
                    "gradient": "A 90%→85%(1.40분)→65%(12.63분)→50%(21.05분)→90%(30분); 주입 전 초기 조건 10분 안정화",
                    "flow": "1.0 mL/min",
                    "detection": "플라본 280 nm, 퀘르세틴 유도체 360 nm, 안토시아닌 520 nm(320 nm 함께 기록)",
                    "injection": "6.70 μL",
                    "sample_prep": "초음파(에탄올 수용액 20–60%, 30–70 °C, 30분)·초임계 CO2(40 °C, 100·300 bar, 90분)·아임계수(130·180 °C, 15분)·공융용매 추출 후 0.45 μm 여과",
                    "standard": "하이퍼로사이드·이소퀘르시트린·퀘르세틴·크리산테민·플라본 외부 표준법",
                    "linearity": "20–200 ppm, 상관계수 0.99847–0.99995"},
     "rationale": "식약처 목록에서 꽃(Acca sellowiana 행)도 식품원료이고, 플라본은 꽃·열매 껍질에 공통으로 많은 특징 성분이라 지표가 됨; 전문 확인, 칼럼 온도·검출한계·회수율은 원문에 없음[8, 1].",
     "source": [8, 1], "url": "https://doi.org/10.3390/plants12071461", "source_kind": "paper"},
]

d = {
    "slug": "feijoa-sellowiana",
    "name_ko": "파인애플구아바",
    "name_en": "Feijoa (pineapple guava)",
    "scientific_name": "Feijoa sellowiana O.Berg (현재 학명 Acca sellowiana (O.Berg) Burret)",
    "aliases": ["페이조아", "파인애플구아바열매", "파인애플구아바주스", "Feijoa", "Pineapple guava", "Guavasteen", "Guayabo del país", "Acca sellowiana"],
    "sections": sections,
    "compounds": compounds,
    "markers": [],
    "nutrients": nutrients,
    "assays": assays,
    "production": [],
    "world": [],
    "gi": [],
    "orgs": [],
    "sources": S,
}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
print("ok", len(S))
