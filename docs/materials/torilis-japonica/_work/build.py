import json
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "dossier.json"
MF = "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020"


def pm(pmid, pmc=None):
    return f"https://pmc.ncbi.nlm.nih.gov/articles/{pmc}/" if pmc else f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"


S = [
    (1, "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 사상자열매·사상자분말·사상자열매추출분말·사상자추출액·사상자농축액 행(학명 Torilis japonica (Houtt.) DC., 영문명 Erect hedgeparsley, 부위 열매, '제한적사용', 사용 조건 '제한적사용가능부위 : 열매※(사상자)'). 로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json", MF, "식품의약품안전처", "2026-10-13"),
    (2, "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 이름이 비슷하거나 혼동될 수 있는 원료 행: 벌사상자열매(학명 칸 비어 있음, 영문명 Monniers snowparsley, 열매, '사용가능', '사용가능부위 : 열매'), 천궁(Cnidium officinale Makino, 뿌리줄기, '제한적사용가능부위 : 뿌리줄기※(천궁)'). 로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json", MF, "식품의약품안전처", "2026-10-13"),
    (3, "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 건강기능식품(C코드) 행 '홍삼, 사상자, 산수유 복합추출물(기능성원료인정제2008-67호)', 영문명 Red ginseng, Torolis japonica, Cornus officinalis complex extract, 분류 개별인정, '사용가능'. 로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json", MF, "식품의약품안전처", "2026-10-13"),
    (4, "A Review on Torilis japonica: Ethnomedicinal, Phytochemical, and Biological Features. Chem Biodivers 2023;20(5):e202201071 (PMID 37073927, doi:10.1002/cbdv.202201071; 총설, 초록만 확인)", pm(37073927), "Wiley / PubMed", "2026-11-02"),
    (5, "Effect of Torilis japonica Fruit Extract for Endothelium-Independent Vasorelaxation and Blood Pressure Lowering in Rats. Int J Mol Sci 2024;25(15):8101 (PMID 39125672, PMC11311312, doi:10.3390/ijms25158101; 전문 확인)", pm(39125672, "PMC11311312"), "MDPI / PubMed Central", "2026-11-02"),
    (6, "Torilis japonica Extract Suppresses the Induction of Atopic Inflammation. Int J Mol Sci 2023;24(3):2102 (PMID 36768424, PMC9916524, doi:10.3390/ijms24032102; 전문 확인, HPLC 조건 표는 본문에 없음)", pm(36768424, "PMC9916524"), "MDPI / PubMed Central", "2026-11-02"),
    (7, "A Torilis japonica Extract–GHK-Cu Complex Attenuates Th2 Cytokines and Promotes Keratinocyte Recovery. Antioxidants (Basel) 2026;15(7):818 (PMID 42510549, PMC13405852, doi:10.3390/antiox15070818; 전문 확인)", pm(42510549, "PMC13405852"), "MDPI / PubMed Central", "2026-11-02"),
    (8, "Five New Sesquiterpenoids From the Fruits of Torilis japonica With Nitric Oxide Inhibitory Activity. Chem Biodivers 2026;23(4):e71205 (PMID 42008758, doi:10.1002/cbdv.71205; 초록만 확인)", pm(42008758), "Wiley / PubMed", "2026-11-02"),
    (9, "Sesquiterpenes from fruits of Torilis japonica with inhibitory activity on melanin synthesis in B16 cells. J Nat Med 2018;72(1):155-160 (PMID 28823078, doi:10.1007/s11418-017-1123-4; 초록만 확인)", pm(28823078), "Springer / PubMed", "2026-11-02"),
    (10, "New Guaiane Sesquiterpenes from the Fruits of Torilis japonica. Chem Pharm Bull 2008;56(10):1483-1485 (PMID 18827397, doi:10.1248/cpb.56.1483; 초록만 확인)", pm(18827397), "日本薬学会 / PubMed", "2026-11-02"),
    (11, "Guaiane sesquiterpenoids from Torilis japonica and their cytotoxic effects on human cancer cell lines. Arch Pharm Res 2006;29(2):131-134 (PMID 16526276, doi:10.1007/BF02974273; 초록만 확인)", pm(16526276), "Springer / PubMed", "2026-11-02"),
    (12, "Sesquiterpenoids of Torilis japonica fruit. Phytochemistry 2002;59(8):811-815 (PMID 11937159, doi:10.1016/s0031-9422(02)00025-0; 초록만 확인)", pm(11937159), "Elsevier / PubMed", "2026-11-02"),
    (13, "A new guaiane type sesquiterpene from Torilis japonica. Arch Pharm Res 2001;24(6):532-535 (PMID 11794530, doi:10.1007/BF02975160; 초록만 확인)", pm(11794530), "Springer / PubMed", "2026-11-02"),
    (14, "[On the components of essential oils of Torilis japonica (Houtt.) DC.] Yakugaku Zasshi 1990;110(10):771-775 (PMID 2074533, doi:10.1248/yakushi1947.110.10_771; 일본어 논문, 영문 초록만 확인)", pm(2074533), "日本薬学会 / PubMed", "2026-11-02"),
    (15, "Torilin from Torilis japonica inhibits melanin production in alpha-melanocyte stimulating hormone-activated B16 melanoma cells. Planta Med 2009;75(14):1505-1508 (PMID 19533579, doi:10.1055/s-0029-1185803; 초록만 확인)", pm(19533579), "Thieme / PubMed", "2026-11-02"),
    (16, "Torilin from Torilis japonica, as a new inhibitor of testosterone 5 alpha-reductase. Planta Med 2003;69(5):459-461 (PMID 12802730, doi:10.1055/s-2003-39717; 초록만 확인)", pm(12802730), "Thieme / PubMed", "2026-11-02"),
    (17, "Torilin from Torilis japonica (Houtt.) DC. blocks hKv1.5 channel current. Arch Pharm Res 2006;29(10):834-839 (PMID 17121176, doi:10.1007/BF02973902; 초록만 확인)", pm(17121176), "Springer / PubMed", "2026-11-02"),
    (18, "Antimicrobial activity of torilin isolated from Torilis japonica fruit against Bacillus subtilis. J Food Sci 2008;73(2):M37-46 (PMID 18298734, doi:10.1111/j.1750-3841.2007.00639.x; 초록만 확인)", pm(18298734), "Wiley / PubMed", "2026-11-02"),
    (19, "Torilin Inhibits Inflammation by Limiting TAK1-Mediated MAP Kinase and NF-κB Activation. Mediators Inflamm 2017;2017:7250968 (PMID 28316375, PMC5337842, doi:10.1155/2017/7250968; 초록 확인)", pm(28316375, "PMC5337842"), "Hindawi / PubMed Central", "2026-11-02"),
    (20, "Anti-inflammatory effect of torilidis fructus ethanol extract through inhibition of Src. Pharm Biol 2017;55(1):2074-2082 (PMID 28832235, PMC6130681, doi:10.1080/13880209.2017.1362011; 초록 확인)", pm(28832235, "PMC6130681"), "Taylor & Francis / PubMed Central", "2026-11-02"),
    (21, "Anti-angiogenic activity of torilin, a sesquiterpene compound isolated from Torilis japonica. Int J Cancer 2000;87(2):269-275 (PMID 10861486; 초록만 확인)", pm(10861486), "Wiley / PubMed", "2026-11-02"),
    (22, "Torilin, a sesquiterpene from Torilis japonica, reverses multidrug-resistance in cancer cells. Planta Med 1998;64(4):332-334 (PMID 9619115, doi:10.1055/s-2006-957445; 초록만 확인)", pm(9619115), "Thieme / PubMed", "2026-11-02"),
    (23, "Sesquiterpenes with hepatoprotective activity from Cnidium monnieri on tacrine-induced cytotoxicity in Hep G2 cells. Planta Med 2002;68(8):748-749 (PMID 12221602, doi:10.1055/s-2002-33796; 초록만 확인)", pm(12221602), "Thieme / PubMed", "2026-11-02"),
    (24, "Attenuating effect of a traditional Korean formulation, Paeng-Jo-Yeon-Nyeon-Baek-Ja-In-Hwan (PJBH), on hydrogen peroxide-induced injury in PC12 cells. Phytother Res 2004;18(6):488-493 (PMID 15287076, doi:10.1002/ptr.1457; 초록만 확인)", pm(15287076), "Wiley / PubMed", "2026-11-02"),
    (25, "Phytochemical, Geographical, and Pharmacological Retrospect of Genus Torilis. Curr Top Med Chem 2023;23(24):2300-2331 (PMID 37518999, doi:10.2174/1568026623666230727163658; 총설, 초록만 확인)", pm(37518999), "Bentham / PubMed", "2026-11-02"),
    (26, "The complete chloroplast genome of Torilis scabra (Apiaceae). Mitochondrial DNA B Resour 2019;4(2):2914-2915 (PMID 33365789, PMC7706797, doi:10.1080/23802359.2019.1661303; 초록 확인)", pm(33365789, "PMC7706797"), "Taylor & Francis / PubMed Central", "2026-11-02"),
    (27, "Inactivation effect of extracts of gardenia fruit, licorice and Torilis japonica fruit against Bacillus subtilis spores. Food Sci Biotechnol 2025;34(3):637-644 (PMID 39958170, PMC11822175, doi:10.1007/s10068-024-01679-w; 초록 확인)", pm(39958170, "PMC11822175"), "Springer / PubMed Central", "2026-11-02"),
    (28, "Anti-Biofilm Effects of Torilis japonica Ethanol Extracts against Staphylococcus aureus. J Microbiol Biotechnol 2022;32(2):220-227 (PMID 34866130, PMC9628846, doi:10.4014/jmb.2107.07053; 초록 확인)", pm(34866130, "PMC9628846"), "KMB / PubMed Central", "2026-11-02"),
    (29, "Anti-protozoal efficacy of medicinal herb extracts against Toxoplasma gondii and Neospora caninum. Vet Parasitol 2003;116(1):7-14 (PMID 14519322, doi:10.1016/s0304-4017(03)00154-7; 초록만 확인)", pm(14519322), "Elsevier / PubMed", "2026-11-02"),
    (30, "Antiproliferative constituents in Umbelliferae plants II. Screening for polyacetylenes in some Umbelliferae plants. Biol Pharm Bull 1998;21(3):257-261 (PMID 9556156, doi:10.1248/bpb.21.257; 초록만 확인)", pm(9556156), "日本薬学会 / PubMed", "2026-11-02"),
    (31, "A Torilis japonica extract exerts anti-proliferative activities on the U87MG human glioblastoma cell line. Mol Med Rep 2010;3(6):1041-1045 (PMID 21472352, doi:10.3892/mmr.2010.376; 초록만 확인)", pm(21472352), "Spandidos / PubMed", "2026-11-02"),
    (32, "GC/MS analysis of high-performance liquid chromatography fractions from Sophora flavescens and Torilis japonica extracts and their in vitro anti-neosporal effects on Neospora caninum. J Vet Sci 2013;14(3):241-248 (PMID 23820198, PMC3788148, doi:10.4142/jvs.2013.14.3.241; 초록 확인)", pm(23820198, "PMC3788148"), "KSVS / PubMed Central", "2026-11-02"),
    (33, "Torilis japonica extract-generated intracellular ROS induces apoptosis ... in HCT116 colon cancer. Int J Oncol 2016;49(3):1088-1098 (PMID 27314881, doi:10.3892/ijo.2016.3578; 초록만 확인)", pm(27314881), "Spandidos / PubMed", "2026-11-02"),
    (34, "[WebSearch 요약으로만 확인, 원문 열람 못함] 사상자(Torilis japonica)와 벌사상자(Cnidium monnieri) 열매의 형태·ITS 염기서열·맛 비교 연구(생약학회지 계열, koreascience JAKO201336161062913). 검색 요약: 한국은 蛇床子를 벌사상자 또는 사상자의 열매로 규정하고 중국·일본은 벌사상자만 인정, 두 종 ITS 유사도 85%", "https://koreascience.kr/article/JAKO201336161062913.page", "koreascience(원문 미확인)", "2026-11-02"),
    (35, "First Report of Powdery Mildew Caused by Erysiphe heraclei on Curled Dock (Rumex crispus) in South Korea. Plant Dis 2013;97(3):427 (PMID 30722391, doi:10.1094/PDIS-10-12-0904-PDN; 초록만 확인)", pm(30722391), "APS / PubMed", "2026-11-02"),
]

sections = [
    ("overview", "한눈에 보기", """사상자(Torilis japonica (Houtt.) DC.)는 산형과(Apiaceae) 사상자속의 두해살이풀로, 동아시아에 분포한다[1, 9]. 영문명은 Erect hedgeparsley이며, 식약처 「식품원료 목록」에는 사상자열매·사상자분말·사상자열매추출분말·사상자추출액·사상자농축액 다섯 원료명이 같은 학명으로 올라 있다[1].

식품원료로서의 지위는 '제한적사용'이다[1]. 사용 부위는 열매 한 가지이고, 사용 조건은 원문 그대로 '제한적사용가능부위 : 열매※(사상자)'다[1]. 이 목록 행에는 사용량 한도나 식품 유형 제한 같은 세부 조건이 더 적혀 있지 않아, 그 밖의 조건은 확인하지 못함. 열매 외의 부위(잎·줄기·뿌리)는 이 목록에 사용 부위로 올라 있지 않다[1].

열매에는 구아이안형 세스퀴테르펜인 토릴린(torilin)이 많아 연구에서 지표성분으로 쓰인다[4, 5, 6]. 50% 에탄올 추출물의 토릴린 함량은 2.84 ± 0.02%, 물 추출물은 0.35 ± 0.01%로 보고되었다[5]. 건강기능식품 쪽에서는 '홍삼, 사상자, 산수유 복합추출물'이 개별인정형 원료(기능성원료인정 제2008-67호)로 목록에 있다[3]. '사상자'라는 이름은 벌사상자(Cnidium monnieri) 열매와 혼동되기 쉬워 원료의 학명 확인이 중요하다[2, 14]."""),
    ("history", "이용의 역사", """한 총설은 사상자 열매가 민간에서 이질, 열, 치질, 경련, 류머티즘, 발기부전, 불임, 부인병, 만성 설사 등에 쓰였다고 정리했다[4]. 한 연구는 열매가 한국·중국·일본에서 성 기능 장애, 특히 발기부전에 쓰여 왔다고 소개한다[5]. 염증, 피부병, 발기부전의 전통 약재로 쓰였다는 기술도 있다[31]. 한 연구는 열매(torilidis fructus)가 살충제, 수렴제, 여러 염증성 질환의 약으로 전통적으로 쓰였다고 적었다[20].

이름의 역사에는 혼동이 섞여 있다[14, 24]. 일본의 정유 연구는 사상자 열매가 중국 약재 '사상자(蛇床子, Cnidii Monnieri Fructus)'의 대용품으로 일본에서 쓰였다고 기록했다[14]. 한국 전통 처방을 다룬 한 연구는 구성 약재를 'Fructus Torilis seu cnidii'(사상자 또는 벌사상자 열매)로 적었다[24]. 검색 요약으로만 확인한 한 국내 연구에 따르면 한국은 蛇床子를 벌사상자 또는 사상자의 열매로 규정하고 중국·일본은 벌사상자만 인정한다고 하나, 원문은 확인하지 못함[34].

식품 쪽에서는 열매 에탄올 추출물이 한국과 중국에서 예부터 항균 목적으로 쓰였다는 설명과 함께 식품 보존용 천연 항균 소재로 연구되었다[18, 27]."""),
    ("biology", "식물학적 특징", """사상자는 동아시아에 분포하는 두해살이풀이며, 열매가 이 식물에서 약재·식품원료로 쓰이는 부위다[1, 9]. 야생에서 자라는 두해살이 초본으로도 소개된다[31]. 한 연구는 사상자 열매가 산형과의 다른 '가시 있는 열매'와 형태가 비슷해 유통 과정에서 혼동될 수 있으므로 실험 전에 판별이 필요하다고 지적했다[5].

사상자속은 전 세계에 11–13종이 있으며 '헤지파슬리(hedge parsley)'로 불린다[25]. 이 속의 식물에서는 페놀성 성분과 테르펜 성분이 다양하게 보고되었고, 테르펜류는 항진균·항균·세포독성·항염 활성으로 자주 연구되었다[25].

사상자 열매의 화학적 특징은 세스퀴테르펜, 특히 구아이안형인 토릴린이 많다는 점이다[4]. 생풀 전체와 열매에서 얻은 정유에서는 53개 성분이 확인되었고, 주성분은 게르마크렌 D(정유의 57.9–71.8%)였다[14]. 열매 메탄올 추출물에서는 폴리아세틸렌 성분의 존재도 시사되었다[30].

사상자는 국내에서 흰가루병균(Erysiphe heraclei)의 기주 식물 가운데 하나로 기록되어 있다[35]."""),
    ("related_species", "가까운 종과 구별", """가장 주의할 혼동은 벌사상자(Cnidium monnieri)다[2, 14]. 식약처 목록에는 '벌사상자열매'가 별도 원료로 올라 있고, 영문명은 Monniers snowparsley, 지위는 '사용가능', 사용 조건은 '사용가능부위 : 열매'이며 학명 칸은 비어 있다[2]. 반면 사상자(Torilis japonica)의 열매는 '제한적사용'이다[1]. 이름과 부위가 같아도 지위가 다르므로, 사상자 원료는 학명으로 확인해야 한다[1, 2].

중국 약재 '사상자(蛇床子)'는 벌사상자 열매를 가리키며, 일본에서는 사상자(T. japonica) 열매가 그 대용품으로 쓰였다[14]. 반대로 벌사상자 에탄올 추출물에서 토릴린을 분리했다는 보고도 있어, 토릴린 하나만으로 두 원료를 가르기는 어렵다[23]. 이 연구의 시료가 실제로 어느 종이었는지는 확인하지 못함.

한 2026년 연구는 사상자 추출물 성분으로 오스톨·임페라토린·베르갑텐 같은 쿠마린을 인용했으나, 그 연구에서 이 성분들을 정량하지는 않았다[7]. 같은 연구진의 앞선 연구는 토릴린과 오스톨을 HPLC 기준물질로 썼다[6]. 산형과 '천궁(Cnidium officinale)'도 이름에 같은 속명이 있으나 뿌리줄기 원료로 사상자와 다르다[2]. 같은 속의 T. scabra는 엽록체 유전체가 따로 해독되어 있으며, 그 자료를 사상자 자료로 옮겨 쓰면 안 된다[26]."""),
    ("cultivation", "자생·재배와 원료 수급", """연구에 쓰인 국내 시료를 보면, 한 연구는 경상북도 문경산 사상자를 2023년 2월에 약재 유통업체에서 사서 DNA 바코드(ITS·matK·rbcL·trnL)로 종을 확인한 뒤 썼다[5]. 다른 연구는 경상북도에서 재배·건조한 열매 전체를 약국에서 구입했다[6]. 2026년 연구는 경상북도 영천에서 재배한 말린 열매를 썼다[7].

재배 면적·생산량에 관한 공식 통계는 확인하지 못함(통계청 농작물생산조사와 농림축산식품부 특용작물 생산실적의 로컬 파싱본에 사상자 항목 없음). 지리적 표시 등록 항목도 확인하지 못함.

수입 원료와 국산 원료의 비중, 표준 재배법·수확 시기에 관한 공공기관 자료도 확인하지 못함. 산형과 열매는 서로 모양이 비슷해 유통 중 섞일 수 있으므로, 연구진은 실험 전 유전자 판별을 권했다[5]."""),
    ("processing", "가공과 제품", """식품원료 목록에는 열매 자체 외에 분말, 열매추출분말, 추출액, 농축액 형태의 원료명이 올라 있으며, 모두 같은 '제한적사용' 조건을 따른다[1]. 건강기능식품 원료로는 '홍삼, 사상자, 산수유 복합추출물'이 개별인정형으로 목록에 있다[3]. 이 복합추출물의 기능성 내용과 1일 섭취량은 확인하지 못함.

연구에서 쓴 추출 조건은 다음과 같다[5, 6, 7]. 분쇄한 열매 40 g을 물 400 mL로 97 ± 3 °C에서 2시간 추출했을 때 수율은 7.08%, 50% 에탄올 400 mL로 75 ± 3 °C에서 2시간 추출했을 때 수율은 3.88%였다[5]. 토릴린은 물 추출물보다 50% 에탄올 추출물에 약 8배 많았다(3.51 mg/g 대 28.37 mg/g)[5]. 다른 연구들은 열매를 정제수로 120 °C·1.5기압에서 2시간 추출한 뒤 동결건조했다[6, 7].

식품 보존 연구에서는 열매 75% 에탄올 추출물 1%(w/v)가 고초균 포자를 3 log 줄였다[18]. 열매 에탄올 추출물 0.01%는 2–48시간 안에 고초균 포자와 영양세포를 2–4 log CFU/g 줄였다[27]. 식약처 「식품 등의 생산실적」 로컬 파일에서 사상자 단일 품목의 생산실적은 확인하지 못함."""),
    ("genetics", "유전과 분류", """사상자는 산형과 사상자속에 속하며, 이 속은 11–13종으로 이루어진다[25]. 국내 연구는 시료의 진위를 ITS, matK, rbcL, trnL 네 유전자 표지로 확인했고, 염기서열을 NCBI BLASTn으로 대조해 사상자로 동정했다[5].

같은 속의 T. scabra 엽록체 유전체는 157,855 bp이며, 큰 단일복사 영역 85,362 bp, 작은 단일복사 영역 17,993 bp, 역위반복 영역 27,250 bp 한 쌍으로 이루어졌다[26]. 이 유전체에서는 단백질 암호 유전자 82개, tRNA 유전자 37개, rRNA 유전자 8개 등 모두 127개 유전자가 예측되었다[26]. 사상자(T. japonica) 자체의 엽록체 유전체 논문은 확인하지 못함.

벌사상자와의 구별에 관해서는 ITS 영역 염기서열 유사도가 85%에 그쳤다는 국내 연구가 있다고 검색 요약에 나오지만, 원문 수치는 확인하지 못함[34]. 같은 요약에 따르면 사상자 열매는 갈고리 모양 가시가 촘촘하고, 벌사상자 열매는 분과 뒷면에 얇은 세로 모서리가 있어 형태로도 구별된다[34]."""),
    ("safety", "안전성과 사용 조건", """식약처 목록에서 사상자는 '제한적사용' 원료이며 사용 조건은 '제한적사용가능부위 : 열매※(사상자)'다[1]. 열매 이외 부위는 식품원료로 쓸 수 없고, 이 목록 행에는 사용량 한도가 적혀 있지 않다[1]. 이름이 비슷한 벌사상자열매는 별개의 '사용가능' 원료이므로 두 원료를 바꿔 쓰거나 섞어 표시하면 안 된다[1, 2].

공공기관의 사상자 독성·알레르기·잔류 평가 자료는 확인하지 못함. 쥐 연구에서 50% 에탄올 추출물 1,000 mg/kg를 한 번 먹였을 때 24시간 안에 이상 반응은 없었지만, 연구진은 동물과 사람의 안전한 용량이 알려져 있지 않으며 혈압약과 함께 쓸 때 상호작용에 주의해야 한다고 적었다[5]. 같은 연구가 체표면적으로 환산한 사람 상당량은 60 kg 성인 기준 약 9.73 g이었으나, 사람에서 효과와 안전성은 검증되지 않았다[5].

세포 실험에서는 추출물이 150 μg/mL까지 피부세포 독성을 보이지 않았고[6], 다른 연구에서는 200 μg/mL까지 생존율 80% 이상, 250 μg/mL 이상에서 생존율이 떨어졌다[7]. 기생충 실험에서는 625 ng/mL를 넘으면 숙주세포 독성이 나타났다[29]. 토릴린은 사람 심장 칼륨 통로(hKv1.5) 전류를 IC50 2.51 μM로 막았고(세포 실험)[17], 5α-환원효소를 억제했다(시험관)[16]. 이 밖에 추출물의 황색포도상구균 생물막 억제[28], 암세포 증식 억제와 이식 종양 동물 실험[31, 33] 결과도 시험관·세포·동물 수준이다[28, 31, 33]. 이들 결과의 사람에서의 의미는 확인하지 못함."""),
]

compounds = [
    dict(name="Torilin", name_ko="토릴린", **{"class": "구아이안형 세스퀴테르펜"}, role="marker", part="열매",
         content_text="열매 50% 에탄올 추출물 2.84 ± 0.02%(28.37 mg/g), 물 추출물 0.35 ± 0.01%(3.51 mg/g), HPLC[5]",
         activity_ko="열매의 주요 세스퀴테르펜으로 지표성분에 쓰임[4, 5, 6]; B16 세포 멜라닌 생성 억제 IC50 25 μM(세포 실험)[15]; 5α-환원효소 억제 IC50 31.7 ± 4.23 μM(시험관)[16]; hKv1.5 전류 억제 IC50 2.51 ± 0.34 μM(세포 실험)[17]; 고초균 영양세포 5–6 log 감소[18]; 대식세포 염증 매개물질 억제(세포 실험)[19]; 쥐 대동맥 이완 EC50 210 ± 1.07 μM(적출 혈관)[5]; 혈관신생 억제(병아리 배·쥐 매트리겔)[21]; 다제내성 암세포 감작(세포 실험)[22]",
         source=[4, 5, 6, 15, 16, 17, 18, 19, 21, 22]),
    dict(name="1beta-Hydroxytorilin", name_ko="1β-하이드록시토릴린", **{"class": "구아이안형 세스퀴테르펜"}, role="bioactive", part="열매",
         content_text="", activity_ko="열매 메탄올 추출물의 염화메틸렌 분획에서 새로 분리; 사람 암세포주 4종 세포독성(세포 실험)[11]", source=[11]),
    dict(name="1alpha-Hydroxytorilin", name_ko="1α-하이드록시토릴린", **{"class": "구아이안형 세스퀴테르펜"}, role="bioactive", part="열매",
         content_text="", activity_ko="열매에서 토릴린과 함께 분리; 사람 암세포주 세포독성(세포 실험)[11]", source=[11]),
    dict(name="Deangeloyloxytorilin", name_ko="데안젤로일옥시토릴린(11-아세톡시-구아이-4-엔-3-온)", **{"class": "구아이안형 세스퀴테르펜"}, role="bioactive", part="열매",
         content_text="", activity_ko="열매에서 처음 분리된 구아이안형 세스퀴테르펜[13]", source=[13]),
    dict(name="11-Acetoxy-8-isobutyryl-4-guaien-3-one", name_ko="11-아세톡시-8-이소부티릴-4-구아이엔-3-온", **{"class": "구아이안형 세스퀴테르펜"}, role="bioactive", part="열매",
         content_text="", activity_ko="열매 메탄올 추출물에서 새로 분리된 3개 성분 중 하나; 대식세포 NO 생성 억제(세포 실험)[10]", source=[10]),
    dict(name="Torijapolide A", name_ko="토리자폴라이드 A", **{"class": "게르마크란형 세스퀴테르페노이드"}, role="bioactive", part="열매",
         content_text="", activity_ko="열매에서 새로 분리; 대식세포 NO 생성 억제 IC50 8.38 ± 0.06 μM(세포 실험)[8]", source=[8]),
    dict(name="Epoxytorilinol", name_ko="에폭시토릴리놀", **{"class": "구아이안형 세스퀴테르펜"}, role="bioactive", part="열매",
         content_text="", activity_ko="열매에서 새로 분리된 3개 세스퀴테르펜 중 하나; 함께 분리된 일부 성분이 B16 세포 멜라닌 생성 억제 IC50 72.9–191.0 μM(세포 실험)[9]", source=[9]),
    dict(name="4(15)-Eudesmene-1beta,5alpha-diol", name_ko="4(15)-유데스멘-1β,5α-디올", **{"class": "유데스만형 세스퀴테르페노이드"}, role="bioactive", part="열매",
         content_text="", activity_ko="열매 메탄올 추출물에서 새로 분리[12]", source=[12]),
    dict(name="Germacrene D", name_ko="게르마크렌 D", **{"class": "세스퀴테르펜(정유)"}, role="bioactive", part="생풀 전체·열매(정유)",
         content_text="정유의 57.9–71.8%[14]", activity_ko="정유의 주성분[14]", source=[14]),
    dict(name="alpha-Humulene", name_ko="α-휴물렌", **{"class": "세스퀴테르펜(정유)"}, role="bioactive", part="생풀 전체·열매(정유)",
         content_text="정유의 2.4–13.2%[14]", activity_ko="정유의 주요 성분[14]", source=[14]),
    dict(name="Bicyclogermacrene", name_ko="비시클로게르마크렌", **{"class": "세스퀴테르펜(정유)"}, role="bioactive", part="생풀 전체·열매(정유)",
         content_text="정유의 1.9–5.4%[14]", activity_ko="정유의 주요 성분[14]", source=[14]),
    dict(name="beta-Caryophyllene", name_ko="β-카리오필렌", **{"class": "세스퀴테르펜(정유)"}, role="bioactive", part="생풀 전체·열매(정유)",
         content_text="정유의 1.5–4.6%[14]", activity_ko="정유의 주요 성분[14]", source=[14]),
    dict(name="Furanodiene", name_ko="푸라노디엔", **{"class": "세스퀴테르펜"}, role="bioactive", part="부위 미기재(추출물 HPLC 분획)",
         content_text="", activity_ko="GC/MS로 확인한 항네오스포라 활성 분획 성분(세포 배양 실험)[32]", source=[32]),
]

assays = [
    {"role": "literature", "compound": "Torilin", "compound_ko": "토릴린", "part": "열매(50% 에탄올·물 추출물)",
     "content": "50% 에탄올 추출물 2.84 ± 0.02%(28.37 mg/g), 물 추출물 0.35 ± 0.01%(3.51 mg/g); 머무름 시간 7.51분[5]",
     "method": "HPLC-PDA",
     "conditions": {"instrument": "Waters e2695 Alliance HPLC + PDA 검출기 2998, Empower2",
                    "column": "FORTIS C18 역상, 250 × 4.6 mm, 5 μm",
                    "mobile_phase": "메탄올:물 = 80:20 (v/v)", "gradient": "등용매, 분석 시간 15분",
                    "flow": "1.0 mL/min", "temp": "25 °C", "detection": "254 nm·230 nm",
                    "injection": "30 μL(3회 반복)",
                    "sample_prep": "추출물 30 mg을 메탄올 1 mL에 녹여 0.45 μm PVDF 주사기 필터로 두 번 거름",
                    "standard": "토릴린 표준품(HPLC 순도 ≥98.0%, CAS 13018-10-5), 0.0625–1 mg/mL 5단계 희석",
                    "linearity": "결정계수 0.9997(최소제곱법)", "lod": "", "loq": "", "recovery": ""},
     "rationale": "열매의 주요 생리활성 세스퀴테르펜으로 추출 용매별 함량 차이를 보여 주는 지표다; 검출·정량한계와 회수율은 본문에 없다[5]",
     "source": [5], "url": pm(39125672, "PMC11311312"), "source_kind": "paper"},
    {"role": "literature", "compound": "Torilin", "compound_ko": "토릴린(오스톨과 함께 기준물질)", "part": "열매(열수 추출물)",
     "content": "함량 수치 없음; 기준물질과 비교해 토릴린 피크를 확인하고 25–31분 사이 특징 피크로 지문 프로필을 제시[7]",
     "method": "HPLC-UV",
     "conditions": {"instrument": "Agilent 1200 series", "column": "YMC J'sphere ODS-H80(규격 본문 미기재)",
                    "mobile_phase": "A: 0.05% 트리플루오로아세트산 수용액, B: 메탄올",
                    "gradient": "0분 A:B = 80:20 → 30분 0:100", "flow": "1 mL/min", "temp": "",
                    "detection": "254 nm", "injection": "",
                    "sample_prep": "경북 영천 재배 말린 열매를 정제수로 120 °C·1.5기압에서 2시간 열수 추출 후 동결건조",
                    "standard": "토릴린·오스톨 기준물질", "linearity": "", "lod": "", "loq": "", "recovery": ""},
     "rationale": "토릴린을 추출물의 특징적 지표성분으로 보고 배치 간 품질 관리용 지문 분석에 쓸 수 있다고 제안했다; 크로마토그램은 앞선 연구에서 가져온 것이다[6, 7]",
     "source": [6, 7], "url": pm(42510549, "PMC13405852"), "source_kind": "paper"},
]

d = {
    "slug": "torilis-japonica",
    "name_ko": "사상자",
    "name_en": "Erect hedgeparsley",
    "scientific_name": "Torilis japonica (Houtt.) DC.",
    "aliases": ["사상자열매", "사상자분말", "사상자열매추출분말", "사상자추출액", "사상자농축액", "Erect hedgeparsley", "Torilidis Fructus"],
    "sections": [{"key": k, "title": t, "body": b} for k, t, b in sections],
    "compounds": compounds,
    "markers": [],
    "assays": assays,
    "nutrients": [],
    "production": [],
    "world": [],
    "gi": [],
    "orgs": [],
    "sources": [{"n": n, "title": t, "url": u, "publisher": p, "accessed": a} for n, t, u, p, a in S],
}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in d["sections"]:
    print(s["key"], len(s["body"]))
