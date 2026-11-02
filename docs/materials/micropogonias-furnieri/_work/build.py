import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
A = "2026-11-02"
def pm(n, title, pmid, pub, note=""):
    return {"n": n, "title": title + (" " + note if note else ""), "url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/", "publisher": pub + " (PubMed)", "accessed": A}
S = [
 {"n": 1, "title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — Micropogonias furnieri 행(대서양통꼬마민어, 영문·이명 White mouth croaker·Whitemouth croaker, 식품원료(A코드)·수산물, 부위 '-', 사용가능, 사용조건 없음) 및 같은 목록의 대서양꼬마민어(Micropogonias undulatus)·Bigeye croaker(Micropogonias megalops)·민어(Miichthys miiuy) 행; 로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json·docs/materials/micropogonias-furnieri/card.json", "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
 pm(2, "Complete mitochondrial genome for the whitemouth croaker (Perciformes: Sciaenidae). Mitochondrial DNA B Resour 2021;6(12):3454-3455. doi:10.1080/23802359.2021.1997112", "34869872", "Mitochondrial DNA Part B", "(PMC8635664 전문 확인)"),
 pm(3, "Identification and Authentication of Commercial Mi-iuy Croaker (Miichthys miiuy) Products by Two PCR-Based Methods. J Food Prot 2021;84(3):463-471. doi:10.4315/JFP-20-143", "33003192", "Journal of Food Protection", "(초록 확인)"),
 pm(4, "Genetic evidence of two stocks of the whitemouth croaker Micropogonias furnieri in the Río de la Plata and oceanic front in Uruguay. J Fish Biol 2009;75(2):321-31. doi:10.1111/j.1095-8649.2009.02321.x", "20738541", "Journal of Fish Biology", "(초록 확인)"),
 pm(5, "Identifying Whitemouth Croaker (Micropogonias furnieri) Populations along the Rio de Janeiro Coast, Brazil, through Microsatellite and Otolith Analyses. Biology (Basel) 2023;12(3):360. doi:10.3390/biology12030360", "36979052", "Biology (Basel)", "(초록 확인)"),
 pm(6, "Metazoan parasites as biological tags for stock discrimination of whitemouth croaker Micropogonias furnieri. J Fish Biol 2010;76(3):591-600. doi:10.1111/j.1095-8649.2009.02515.x", "20666899", "Journal of Fish Biology", "(초록 확인)"),
 pm(7, "Leave forever or return home? The case of the whitemouth croaker Micropogonias furnieri in coastal systems of southeastern Brazil indicated by otolith microchemistry. Mar Environ Res 2018;144:28-35. doi:10.1016/j.marenvres.2018.11.015", "30527444", "Marine Environmental Research", "(초록 확인)"),
 pm(8, "Trophic ecology and food consumption of fishes in a hypersaline tropical lagoon. J Fish Biol 2015;86(6):1781-95. doi:10.1111/jfb.12689", "26033293", "Journal of Fish Biology", "(초록 확인)"),
 pm(9, "Relationship between ecomorphology and trophic segregation in four closely related sympatric fish species (Teleostei, Sciaenidae). C R Biol 2016;339(11-12):498-506. doi:10.1016/j.crvi.2016.07.003", "27562196", "Comptes Rendus Biologies", "(초록 확인)"),
 pm(10, "Fishing strategies among prehistoric populations at Saquarema Lagoonal Complex, Rio de Janeiro, Brazil. An Acad Bras Cienc 2013;85(1):415-29. doi:10.1590/s0001-37652013005000005", "23460437", "Anais da Academia Brasileira de Ciências", "(초록 확인)"),
 pm(11, "The freshwater artisanal fishery of Patos Lagoon. J Fish Biol 2016;89(1):337-54. doi:10.1111/jfb.13004", "27250698", "Journal of Fish Biology", "(초록 확인)"),
 pm(12, "DNA Barcode reveals mislabelling in the identification of marine fish swimming bladders for commercialization. Forensic Sci Int 2019;299:41-43. doi:10.1016/j.forsciint.2019.03.001", "30954626", "Forensic Science International", "(초록 확인)"),
 pm(13, "Steroid metabolism in vitro during final oocyte maturation in white croaker Micropogonias furnieri (Pisces: Sciaenidae). Braz J Biol 2004;64(2):211-20. doi:10.1590/s1519-69842004000200005", "15462293", "Brazilian Journal of Biology", "(초록 확인)"),
 pm(14, "Diagnosis of lymphocystis disease in a novel host, the whitemouth croaker Micropogonias furnieri, associated with a putatively novel Lymphocystivirus species (LCDV-WC). Dis Aquat Organ 2020;137(3):185-193. doi:10.3354/dao03438", "31942864", "Diseases of Aquatic Organisms", "(초록 확인)"),
 pm(15, "Assessing the quality of fresh Whitemouth croaker (Micropogonias furnieri) meat based on micro-organism and histamine analysis using NGS, qPCR and HPLC-DAD. J Appl Microbiol 2020;128(5):1448-1459. doi:10.1111/jam.14566", "31883415", "Journal of Applied Microbiology", "(초록 확인, 전문 확인 못함)"),
 pm(16, "Green Marine Collagen-Chitosan Composites with Biocompatible, Hemostatic, and Pro-Healing Performance. ACS Appl Bio Mater 2026;9(6):3015-3028. doi:10.1021/acsabm.5c02493", "41744062", "ACS Applied Bio Materials", "(PMC12997167 전문 확인; 전문 텍스트에서 학명 표기가 빠져 있어 종 귀속은 PubMed 'Micropogonias furnieri' 색인에 근거)"),
 pm(17, "In vitro and in vivo biological performance of hydroxyapatite from fish waste. J Mater Sci Mater Med 2021;32(9):109. doi:10.1007/s10856-021-06591-x", "34453621", "Journal of Materials Science: Materials in Medicine", "(PMC8403112 전문 확인)"),
 pm(18, "Croaker Fish Bone-Derived Hydroxyapatite as a Sustainable Source for 3D-Printed Scaffolds for Bone Regeneration. Mar Drugs 2026;24(8):260. doi:10.3390/md24080260", "42646460", "Marine Drugs", "(PMC13514607 전문 확인; 전문 텍스트에서 학명 표기가 빠져 있어 종 귀속은 PubMed 'Micropogonias furnieri' 색인에 근거)"),
 pm(19, "Biological activities of the protein hydrolysate obtained from two fishes common in the fisheries bycatch. Food Chem 2021;342:128361. doi:10.1016/j.foodchem.2020.128361", "33077277", "Food Chemistry", "(초록 확인)"),
 pm(20, "Films based on protein isolated from croaker (Micropogonias furnieri) and palm oil. J Sci Food Agric 2016;96(7):2478-85. doi:10.1002/jsfa.7368", "26250365", "Journal of the Science of Food and Agriculture", "(초록 확인)"),
 pm(21, "Chemical modification and structural analysis of protein isolates to produce hydrogel using Whitemouth croaker (Micropogonias furnieri) wastes. Appl Biochem Biotechnol 2011;165(1):279-89. doi:10.1007/s12010-011-9250-y", "21505805", "Applied Biochemistry and Biotechnology", "(초록 확인)"),
 pm(22, "The relationships between mercury and selenium in plankton and fish from a tropical food web. Environ Sci Pollut Res Int 2009;16(1):10-24. doi:10.1007/s11356-008-0038-8", "18751748", "Environmental Science and Pollution Research", "(구조화 초록 확인, 전문 확인 못함)"),
 pm(23, "Selenium and mercury in widely consumed seafood from South Atlantic Ocean. Ecotoxicol Environ Saf 2013;93:156-62. doi:10.1016/j.ecoenv.2013.03.034", "23628606", "Ecotoxicology and Environmental Safety", "(초록 확인)"),
 pm(24, "Total Mercury in Carnivorous Fish from Brazilian Southeast. Bull Environ Contam Toxicol 2015;95(1):18-24. doi:10.1007/s00128-015-1470-3", "25666565", "Bulletin of Environmental Contamination and Toxicology", "(초록 확인)"),
 pm(25, "Human health risks assessment of the fluctuations in mercury levels in seafood from different key regions of Rio de Janeiro, Brazil. Environ Sci Pollut Res Int 2024;31(21):30467-30483. doi:10.1007/s11356-024-33267-0", "38607486", "Environmental Science and Pollution Research", "(초록 확인)"),
 pm(26, "Potentially toxic trace elements in the muscle of coastal South American fish: Implications for human consumption and health risk assessment. Mar Pollut Bull 2024;202:116384. doi:10.1016/j.marpolbul.2024.116384", "38643585", "Marine Pollution Bulletin", "(초록 확인)"),
 pm(27, "Arsenic Speciation, an Evaluation of Health Risk Due to the Consumption of Two Fishes from Coastal Marine Areas of the Southwestern Atlantic Ocean (SWAO). Arch Environ Contam Toxicol 2025;88(3):253-276. doi:10.1007/s00244-025-01123-y", "40097815", "Archives of Environmental Contamination and Toxicology", "(초록 확인)"),
 pm(28, "Heavy metal levels in fish from coastal waters of Uruguay. Arch Environ Contam Toxicol 2005;48(4):530-7. doi:10.1007/s00244-004-0100-6", "15883670", "Archives of Environmental Contamination and Toxicology", "(초록 확인)"),
 pm(29, "Polycyclic aromatic hydrocarbons in wild and farmed whitemouth croaker and meagre from different Atlantic Ocean fishing areas: Concentrations and human health risk assessment. Food Chem Toxicol 2020;146:111797. doi:10.1016/j.fct.2020.111797", "33027612", "Food and Chemical Toxicology", "(초록 확인)"),
 pm(30, "Occurrence of legacy and emerging organic pollutants in whitemouth croakers from Southeastern Brazil. Sci Total Environ 2019;682:719-728. doi:10.1016/j.scitotenv.2019.05.213", "31129551", "Science of the Total Environment", "(초록 확인)"),
 pm(31, "Residues of legacy organochlorine pesticides and DDT metabolites in highly consumed fish from the polluted Guanabara Bay, Brazil: distribution and assessment of human health risk. J Environ Sci Health B 2020;55(1):30-41. doi:10.1080/03601234.2019.1654808", "31496395", "Journal of Environmental Science and Health, Part B", "(초록 확인)"),
 pm(32, "Nematode parasites of commercially important fish from the southeast coast of Brazil: Morphological and genetic insight. Int J Food Microbiol 2018;267:29-41. doi:10.1016/j.ijfoodmicro.2017.12.014", "29278825", "International Journal of Food Microbiology", "(초록 확인)"),
 pm(33, "Allergenic response induced by Pterobothrium crassicolle (Cestoda: Trypanorhyncha) extracts in murine model. Rev Bras Parasitol Vet 2024;33(3):e002624. doi:10.1590/S1984-29612024039", "39046076", "Revista Brasileira de Parasitologia Veterinária", "(초록 확인)"),
 pm(34, "Ability of Vibrio vulnificus isolated from fish of the Lagoa dos Patos estuary in south Brazil to form biofilms after sublethal stress and bacterial resistance to antibiotics and sanitizers. Int J Food Microbiol 2019;303:19-25. doi:10.1016/j.ijfoodmicro.2019.05.007", "31112793", "International Journal of Food Microbiology", "(초록 확인)"),
 {"n": 35, "title": "IUCN Red List — Micropogonias furnieri 평가(T195076A86367413, 2021 공개). 원문 PDF는 이 환경에서 열지 못했고 WebSearch 요약으로만 확인함(범주 '관심대상(LC)'과 평가 번호·연도만 사용)", "url": "https://www.iucnredlist.org/species/195076/86367413", "publisher": "IUCN", "accessed": A},
 pm(36, "Permanent genetic resources added to Molecular Ecology Resources Database 1 December 2011-31 January 2012. Mol Ecol Resour 2012;12(3):570-2. doi:10.1111/j.1755-0998.2012.03133.x", "22448966", "Molecular Ecology Resources", "(초록 확인)"),
 pm(37, "Adaptative features of enzymes from family sciaenidae--II. Studies on phosphoglucose isomerase (PGI) of fishes from the south coast of Uruguay. Comp Biochem Physiol B 1987;88(1):211-8. doi:10.1016/0305-0491(87)90102-7", "3677600", "Comparative Biochemistry and Physiology B", "(초록 확인)"),
 pm(38, "Complete genome sequence and analysis of a novel lymphocystivirus detected in whitemouth croaker (Micropogonias furnieri): lymphocystis disease virus 4. Arch Virol 2020;165(5):1215-1218. doi:10.1007/s00705-020-04570-1", "32140836", "Archives of Virology", "(초록 확인)"),
 pm(39, "Distribution and human health risk assessment of PAHs in four fish species from a SW Atlantic estuary. Environ Sci Pollut Res Int 2017;24(23):18979-18990. doi:10.1007/s11356-017-9394-6", "28656579", "Environmental Science and Pollution Research", "(초록 확인)"),
]

sec = []
def add(k, t, b): sec.append({"key": k, "title": t, "body": b})

add("overview", "한눈에 보기",
"대서양통꼬마민어(Micropogonias furnieri)는 민어과(Sciaenidae)에 속하는 바닷물고기로, 영어로는 whitemouth croaker라 부른다[1, 2]. 남미 대서양 연안에서 상업적으로 가장 중요한 어종 가운데 하나로, 주로 브라질과 아르헨티나에서 잡혀 한국을 포함한 여러 나라로 수출된다[2, 30]. 한국 연구진이 미토콘드리아 유전체를 해독할 때 쓴 시료도 아르헨티나 앞바다에서 잡혀 냉동 상태로 수입된 것을 국내 수입업체에서 산 것이었다[2].\n\n"
"식약처 「식품원료 목록」에는 원료명 '대서양통꼬마민어'(영문 White mouth croaker, Whitemouth croaker)가 식품원료(A코드) 수산물로 올라 있고 상태는 '사용가능'이다[1]. 부위 칸은 '-'이고 따로 정한 사용 조건은 없으며, 건강기능식품 고시형 원료의 원재료도 아니어서 고시 지표성분이나 1일 섭취량 기준은 없다[1]. 같은 목록에서 같은 속의 대서양꼬마민어(Micropogonias undulatus)와 Bigeye croaker(Micropogonias megalops), 그리고 민어(Miichthys miiuy)는 각각 다른 원료로 올라 있다[1]. 국내 수입량 통계는 이번 조사에서 확인하지 못함.")

add("history", "이름과 이용의 역사",
"브라질 리우데자네이루주 사콰레마 석호 일대의 패총 유적에서는 다듬은 물고기 가시로 만든 도구가 이 종을 잡는 데 쓰였고, 이 기술은 약 6,726년 전부터 3,699년 전(보정 연대)까지 우세했다[10]. 오늘날 이 종은 우루과이 해역에서 가장 중요한 연안 수산 자원으로 꼽히고, 라플라타강과 그 바깥 전선 해역에서 상업적 중요성이 가장 크다[4]. 다른 연구는 이 종을 우루과이의 두 번째 수산 자원으로 소개했다[13].\n\n"
"브라질에서는 대서양통꼬마민어가 가장 많이 양륙되는 어종으로 소개되었다[15]. 리우데자네이루주에서는 정어리·숭어와 함께 가장 많이 소비되는 상업 어종 세 가지에 든다[31]. 파투스 석호의 민물 구역 소규모 어업에서도 숭어·바다메기류와 함께 허용 그물코 자망의 주된 대상이었다[11].\n\n"
"한국에서는 맛과 생김새가 다른 민어과 어류와 비슷해 불법 판매를 막기 위한 종 판별 표지가 필요하다는 점이 연구 동기로 제시되었다[2]. 국내 시판 '민어' 제품 43건을 조사한 연구에서도 1건이 이 종으로 바뀌어 있었다[3]. 국내 도입 시기에 관한 공식 기록은 확인하지 못함.")

add("biology", "어종과 생태",
"한국 연구진은 이 종의 분포를 멕시코만에서 아르헨티나 연안까지의 대서양으로 기술했다[2]. 수명이 길고 연안에서 먹이를 먹으며 먹이사슬에서 높은 위치에 있어, 연안 오염을 감시하는 지표종으로 쓰인다[30]. 하구는 어린 고기가 자라는 곳이고 바깥 대륙붕은 산란장이며, 이석(귀돌) 미량원소 분석으로 하구를 떠나 돌아오지 않는 유형, 하구와 대륙붕을 오가는 유형, 하구 영향권 연안에 머무는 유형 세 가지가 확인되었다[7].\n\n"
"브라질 아라루아마 고염 석호에서는 주로 밤에 작은 갑각류를 먹었고, 하루 먹이 섭취량은 몸무게 1 g당 0.031 g과 0.027 g(두 차례 조사)이었다[8]. 아르헨티나의 같은 해역에 사는 민어과 4종 비교에서 이 종을 포함한 성어들은 공간이 완전히 겹치면서도 몸 형태 차이에 따라 먹이를 나눠 먹었다[9]. 우루과이 개체의 난소 조직은 시험관 실험에서 17,20β-디히드록시-4-프레그넨-3-온 등 난모세포 최종 성숙을 유도하는 스테로이드를 만들었다[13]. IUCN 적색목록에서는 '관심대상(LC)'으로 평가되었다(원문 미확인, 검색 요약)[35].")

add("related_species", "가까운 종과 혼동",
"같은 속의 대서양꼬마민어(Micropogonias undulatus)와 Bigeye croaker(Micropogonias megalops)는 식약처 목록에서 별도 원료이므로, 이 종의 성분·안전 자료와 섞어 쓰면 안 된다[1]. 한국 시판 민어(Miichthys miiuy) 제품 43건을 DNA 바코드와 민어 특이 이중 PCR로 검사한 연구에서 21%가 표시와 달랐다[3]. 대체된 종은 law croaker(Pseudotolithus senegallus) 4건, Bigeye croaker 3건, 대서양통꼬마민어 1건, tigertoothed croaker(Otolithes ruber) 1건이었다[3].\n\n"
"브라질에서 메기류로 신고되어 거래되던 부레를 COI 바코드로 확인한 결과 실제로는 블랙드럼(Pogonias cromis)과 이 종이었다[12]. 아르헨티나 해역에서는 이 종이 Cynoscion guatucupa·Pogonias cromis·Menticirrhus americanus 같은 민어과 어류와 같은 곳에 산다[9]. 우루과이 남부 연안의 민어과 3종(Cynoscion striatus, Macrodon ancylodon, 이 종) 연구에서는 포스포글루코스 이성화효소가 세 개의 유전자 자리에서 만들어지는 것으로 보였다[37]. 이 종용으로 개발된 미세위성 표지는 Cynoscion 여러 종과 Macrodon ancylodon 등 다른 민어과 어류에서도 교차 시험되었다[36].")

add("cultivation", "어획과 자원",
"우루과이 해역에서는 미토콘드리아 조절 영역 분석으로 라플라타강 자원과 대륙붕 자원 두 무리가 구분되었고, 대륙붕 쪽은 약 4만 년 전부터 개체군이 늘어난 흔적을 보였다[4]. 브라질 연안 248마리의 기생충 41종을 표지로 쓴 분석에서는 북부(세아라·바이아), 남동부(리우데자네이루·산타카타리나), 남부(히우그란지두술) 세 자원이 구분되었다[6]. 리우데자네이루 연안에서는 미세위성으로 두 집단, 이석 형태·원소 조성으로는 북·중·남 세 집단이 나뉘어, 지역별 관리가 필요하다는 결론이 나왔다[5].\n\n"
"이 종은 새우 저인망의 혼획물에서 가장 많이 나오는 두 어종 가운데 하나다[19]. 브라질에서는 이 종의 부레가 메기류로 신고되어 거래된 사례가 보고되었고, 저자들은 이 종이 위협 상태여서 어획이 금지되어 있다고 적었다[12]. 2015년 우루과이에서는 자연산과 양식 개체 모두에서 피부에 혹이 생기는 림포시스티스병이 발견되었고, 새로운 림포시스티스바이러스 종(LCDV-WC)이 원인으로 제시되었다[14]. 이 바이러스의 전체 유전체는 211,086 bp로 해독되었다[38]. 세계 어획 통계(FAO)는 이 환경에서 원문을 열지 못해 확인하지 못함.")

add("processing", "가공과 이용",
"살은 주로 신선·냉동 생선으로 유통되며, 한국에는 냉동 상태로 수입된 기록이 있다[2]. 브라질 남부의 신선 대서양통꼬마민어 살에서는 히스타민이 258.52–604.62 mg/kg 검출되어 모든 시료가 국제식품규격(Codex) 허용치를 넘었고, 저자들은 취급·가공 개선이 필요하다고 했다[15].\n\n"
"가공 부산물 활용 연구가 많다[16, 17, 18]. 껍질에서 0.5 M 아세트산으로 뽑은 I형 콜라겐은 건조 껍질 기준 수율 11.4 ± 2.7%였고, 키토산과 섞은 막은 섬유아세포 실험에서 독성을 보이지 않았다[16]. 뼈를 800 °C에서 구워 얻은 수산화인회석은 쥐 두개골 결손 실험에서 30일 뒤 염증이 사라지고 새 뼈가 생겼다(동물실험)[17]. 뼈 유래 수산화인회석은 결정화도 80.2%, 칼슘/인 비 1.96(반정량 EDS)으로 시판품(35.0%, 1.56)과 달랐다[18].\n\n"
"살과 껍질을 효소로 분해한 단백질 가수분해물은 시험관에서 항산화 활성을 보였고 16 mg/mL 미만에서는 세포 생존에 영향이 없었다[19]. 가공 찌꺼기에서 분리한 단백질로 생분해성 필름과 물을 잘 빨아들이는 하이드로겔을 만든 연구도 있다[20, 21]. 사람 대상 효능 근거는 확인하지 못함.")

add("genetics", "유전체와 유전 다양성",
"이 종의 미토콘드리아 전체 유전체는 16,496 bp이고, 단백질 암호화 유전자 13개, 리보솜 RNA 유전자 2개, 운반 RNA 유전자 22개와 조절 영역으로 이루어진다[2]. 염기 조성은 A 27.26%, T 25.65%, G 16.46%, C 30.63%로 A+T 비율이 52.91%였다[2]. 16S rRNA는 1,697 bp, 12S rRNA는 954 bp였고, 15종의 단백질 암호화 유전자로 최대우도 계통수를 만들었다[2]. 해독 목적은 국내에서 다른 민어과 어류와 구별하는 종 판별 표지를 만들기 위한 것이었다[2].\n\n"
"우루과이 연구에서는 대륙붕 시료가 라플라타강 시료보다 유전 다양성이 높고, 유효 암컷 수도 약 10배(한 자릿수) 더 컸다[4]. 이 종용 미세위성 표지가 분자생태 자원 데이터베이스에 등록되었다[36]. 리우데자네이루 연안 연구는 미세위성으로 두 집단의 분화를 확인했다[5]. 우루과이 개체에서는 포스포글루코스 이성화효소 유전자 자리 Pgi-A에서 유전 변이가 발견되었다[37]. 핵 유전체 전체 해독 보고는 확인하지 못함.")

add("safety", "안전성과 주의",
"고시형 원료가 아니어서 식약처가 정한 섭취 주의사항은 없다[1]. 이타이푸 하구 개체 근육의 총수은은 0.110 mg/kg으로 낮았으나 먹는 양에 따라 위험이 있을 수 있다고 했다[24]. 과나바라만 개체 근육의 총수은과 셀레늄은 각각 2.9, 15.3 nmol/g이었고 근육 수은은 거의 모두(약 100%) 메틸수은이었다[22]. 남동 브라질 해산물 비교에서 이 종의 셀레늄:수은 몰비는 21이었다[23]. 리우데자네이루 조사에서는 수은이 기준 아래였으나 아이가 먹을 때 위해지수가 1을 넘는 경우가 많았다[25].\n\n"
"근육 총비소는 현지 권고치(습중량 1 mg/kg)를 넘었으나 독성 비소 형태는 그 아래였다[27]. 다만 무기비소 비율을 5%로 가정하면 어민 집단의 위해지수가 1을 넘어 형태별 분석이 필요하다고 했다[26]. 우루과이 연구는 간과 큰 개체를 먹지 말 것을 권했다[28]. 자연산 개체의 다환방향족탄화수소 합계는 습중량 1.32–5.41 μg/kg이었다[29]. 아르헨티나 바이아블랑카 하구 4종 중 이 종만 섭취 경고 수준에 이르지 않았다[39]. 과나바라만 개체의 유기염소 농약 합계는 습중량 7.5 ng/g으로 기준 이하였다[31].\n\n"
"근육에서 Hysterothylacium 선충 유충이 나와 공중보건 우려가 제기되었고, Anisakis typica도 이 종에서 처음 기록되었다[32]. 이 종에서 얻은 촌충 유충 추출물은 생쥐에서 IgE 반응을 일으켰다(동물실험)[33]. Vibrio vulnificus도 분리되었다[34]. 국내 공공기관의 이 종 알레르기·잔류 정보는 확인하지 못함.")

comp = [
 {"name": "Collagen type I", "name_ko": "I형 콜라겐", "class": "단백질", "role": "bioactive", "part": "껍질", "content_text": "산가용성 콜라겐 수율 11.4 ± 2.7%(건조 껍질 기준)[16]", "activity_ko": "키토산 복합막이 L929 섬유아세포 대사 활성·증식을 높이고 유전독성 없음(세포실험)[16]", "source": [16]},
 {"name": "Hydroxyapatite", "name_ko": "수산화인회석", "class": "무기질(인산칼슘)", "role": "bioactive", "part": "뼈", "content_text": "800 °C 소성 뼈 유래, 결정화도 80.2%, Ca/P 1.96(반정량 EDS)[18]", "activity_ko": "쥐 두개골 결손 30일 뒤 새 뼈 형성(동물실험)[17]; 10% 배합 지지체가 전조골세포 증식 촉진(세포실험)[18]", "source": [17, 18]},
 {"name": "Fish protein hydrolysate", "name_ko": "어류 단백질 가수분해물", "class": "펩타이드 혼합물", "role": "bioactive", "part": "살·껍질", "content_text": "16 mg/mL 미만에서 세포 생존에 영향 없음[19]", "activity_ko": "퍼옥실 라디칼·DPPH 등 시험관 항산화 활성[19]", "source": [19]},
 {"name": "Histamine", "name_ko": "히스타민", "class": "생체아민", "role": "marker", "part": "살(신선육)", "content_text": "258.52–604.62 mg/kg(HPLC-DAD)[15]", "activity_ko": "선도 저하 지표; 전 시료가 Codex 허용치 초과[15]", "source": [15]},
 {"name": "Mercury", "name_ko": "수은(총수은)", "class": "중금속", "role": "bioactive", "part": "근육", "content_text": "0.110 mg/kg(이타이푸 하구)[24]; 2.9 nmol/g(과나바라만)[22]", "activity_ko": "오염 지표; 아이 섭취 시 위해지수 1 초과 사례 많음[25]", "source": [22, 24, 25]},
 {"name": "Methylmercury", "name_ko": "메틸수은", "class": "유기수은", "role": "bioactive", "part": "근육·간", "content_text": "근육 MeHg/THg 약 100%, 간 31%[22]", "activity_ko": "간에서 셀레늄과 역상관(길항 시사)[22]", "source": [22]},
 {"name": "Selenium", "name_ko": "셀레늄", "class": "무기질(미량원소)", "role": "nutrient", "part": "근육", "content_text": "15.3 nmol/g(과나바라만)[22]; Se:Hg 몰비 21[23]", "activity_ko": "Se:Hg 몰비 1 초과로 수은 독성 상쇄 가능성[23]", "source": [22, 23]},
 {"name": "Arsenic", "name_ko": "비소(총비소)", "class": "준금속", "role": "bioactive", "part": "근육", "content_text": "총비소가 현지 권고치(습중량 1 mg/kg)를 넘었으나 독성 형태는 그 미만[27]", "activity_ko": "무기비소 섭취량은 국제 권고치 이내로 평가[27]; 무기비소를 총비소의 5%로 가정하면 어민 집단의 총 위해지수가 1을 넘음[26]", "source": [26, 27]},
 {"name": "Polycyclic aromatic hydrocarbons", "name_ko": "다환방향족탄화수소(합계)", "class": "환경오염물질", "role": "bioactive", "part": "가식부(근육)", "content_text": "자연산 습중량 1.32–5.41 μg/kg[29]", "activity_ko": "나프탈렌·플루오렌·페난트렌이 주성분[29]", "source": [29]},
 {"name": "Polybrominated diphenyl ethers", "name_ko": "폴리브롬화디페닐에테르(PBDEs)", "class": "브롬계 난연제", "role": "bioactive", "part": "근육", "content_text": "습중량 7.6–879.7 pg/g[30]", "activity_ko": "연안 오염 감시 지표[30]", "source": [30]},
 {"name": "Polychlorinated dibenzo-p-dioxins and dibenzofurans", "name_ko": "다이옥신·퓨란(TEQ)", "class": "잔류성 유기오염물질", "role": "bioactive", "part": "근육", "content_text": "습중량 <LOD–1.7 pg/g, TEQ 0.1–0.2 pg/g[30]", "activity_ko": "독성등가량 기준 평가[30]", "source": [30]},
 {"name": "Organochlorine pesticides", "name_ko": "유기염소 농약(합계)", "class": "잔류 농약", "role": "bioactive", "part": "근육", "content_text": "습중량 7.5 ng/g[31]", "activity_ko": "최대 잔류 기준 초과 없음[31]", "source": [31]},
]

E = {k: "" for k in ["instrument","column","mobile_phase","gradient","flow","temp","detection","injection","sample_prep","standard","linearity","lod","loq","recovery"]}
def C(**kw):
    d = dict(E); d.update(kw); return d
assays = [
 {"role": "literature", "compound": "Collagen type I (acid-soluble)", "compound_ko": "산가용성 I형 콜라겐", "part": "껍질", "content": "수율 11.4 ± 2.7%(건조 껍질 기준)[16]", "method": "산 추출·중량법(FTIR·편광현미경으로 I형 확인)",
  "conditions": C(sample_prep="신선 껍질을 0.1 M NaOH(1:15 w/v), 4 °C 6시간(2시간마다 교체) → 10% 부탄올(1:20 w/v) 24시간 탈지 → 3% 과산화수소(1:10 w/v) 15분 탈색 → −80 °C 동결·48시간 동결건조 → 0.5 M 아세트산(1:50 w/v), 4 °C 48시간 교반 추출 후 여과", detection="FTIR(아마이드 I·II·III 띠), 피크로시리우스 염색 편광현미경"),
  "rationale": "껍질은 버려지는 부산물이며 I형 콜라겐이 주된 활용 성분이다[16]. 전문(Methods) 확인 — 추출 조건만 있고 히드록시프롤린 정량·회수율은 없음[16].", "source": [16], "url": "https://pubmed.ncbi.nlm.nih.gov/41744062/", "source_kind": "paper"},
 {"role": "literature", "compound": "Hydroxyapatite (Ca/P ratio)", "compound_ko": "수산화인회석(칼슘/인 비)", "part": "뼈", "content": "Ca/P 1.96(이론값 1.67), 결정화도 80.2%[18]", "method": "SEM-EDS(반정량)·XRD",
  "conditions": C(instrument="탁상 SEM TM4000Plus II(EDS 검출기 장착)·LEO 1550 SEM, 가속전압 15 kV", sample_prep="살 제거 → 증류수 1시간 끓임 → 1 M NaOH 24시간(2회) → 증류수 세척 → 30% 과산화수소 24시간 표백 → 머플로 800 °C(승온 5 °C/분, 5시간 유지) 소성 → 습식 볼밀(15분, 300 rpm)", standard="시판 수산화인회석(순도 >90%)과 비교; 결정화도는 Landi 등의 방법"),
  "rationale": "뼈 유래 수산화인회석의 순도·조성 지표로 Ca/P 비를 쓴다[18]. 전문(Results·Methods) 확인 — EDS 반정량이라 비가 높게 나온 것은 생물 유래 조성 변동으로 해석됨[18].", "source": [18], "url": "https://pubmed.ncbi.nlm.nih.gov/42646460/", "source_kind": "paper"},
 {"role": "literature", "compound": "Histamine", "compound_ko": "히스타민", "part": "살(신선육)", "content": "258.52–604.62 mg/kg[15]", "method": "HPLC-DAD", "conditions": C(),
  "rationale": "히스타민은 생선 선도와 히스타민 식중독 위험의 지표다[15]. 초록만 확인 — 전문 확인 못함, 조건 칸 비움[15].", "source": [15], "url": "https://pubmed.ncbi.nlm.nih.gov/31883415/", "source_kind": "paper"},
 {"role": "literature", "compound": "Total mercury / Methylmercury", "compound_ko": "총수은·메틸수은", "part": "근육·간", "content": "근육 총수은 2.9 nmol/g, 근육 MeHg/THg 약 100%[22]", "method": "총수은 CV-AAS(수소화붕소나트륨 환원), 메틸수은 GC-ECD",
  "conditions": C(sample_prep="메틸수은: 알코올성 수산화칼륨 분해 → 디티존-톨루엔 추출 → 톨루엔층 분석", detection="총수은 냉증기 원자흡광; 메틸수은 전자포획검출기; 셀레늄은 Zeeman 배경보정 흑연로 원자흡광"),
  "rationale": "육식성 저서어인 이 종은 연안 수은 오염과 섭취 위해 평가의 대표 지표다[22]. 구조화 초록의 방법만 확인 — 전문 확인 못함[22].", "source": [22], "url": "https://pubmed.ncbi.nlm.nih.gov/18751748/", "source_kind": "paper"},
]

d = {"slug": "micropogonias-furnieri", "name_ko": "대서양통꼬마민어", "name_en": "Whitemouth croaker", "scientific_name": "Micropogonias furnieri",
     "aliases": ["대서양통꼬마민어", "Whitemouth croaker", "White mouth croaker"],
     "sections": sec, "compounds": comp, "markers": [], "assays": assays, "nutrients": [], "production": [], "world": [], "gi": [], "orgs": [], "sources": S}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in sec: print(s["key"], len(s["body"]))
