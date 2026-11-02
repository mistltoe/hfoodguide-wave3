import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
A = "2026-11-02"
def pm(n, title, pmid, pub, pmc=None):
    url = f"https://pmc.ncbi.nlm.nih.gov/articles/{pmc}/" if pmc else f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
    return {"n": n, "title": title, "url": url, "publisher": pub, "accessed": A}
sources = [
 {"n": 1, "title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 바디나물순(Angelica decursiva (Miq.) Franch. & Sav. / Angelica decursiva f. albiflora Nakai, 식품원료 A코드, 사용가능부위: 순) 행 및 전호잎·처녀바디잎·잔잎바디잎·참반디잎·당귀속 원료 행", "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
 pm(2, "Ethnobotany, phytochemistry, pharmacology and quality control of Peucedanum decursivum (Miq.) Maxim: A critical review. J Ethnopharmacol 2024;334:118542 (PMID 38992404, doi:10.1016/j.jep.2024.118542) — 초록", "38992404", "Journal of Ethnopharmacology (PubMed)"),
 pm(3, "Chemotaxonomic Classification of Peucedanum japonicum and Its Chemical Correlation with Peucedanum praeruptorum, Angelica decursiva, and Saposhnikovia divaricata by Liquid Chromatography Combined with Chemometrics. Molecules 2022;27(5):1675 (PMID 35268776, doi:10.3390/molecules27051675)", "35268776", "Molecules (MDPI, PMC)", "PMC8911569"),
 pm(4, "Development of SCAR markers for the discrimination of three species of medicinal plants, Angelica decursiva (Peucedanum decursivum), Peucedanum praeruptorum and Anthricus sylvestris. Biol Pharm Bull 2009;32(1):24-30 (PMID 19122275, doi:10.1248/bpb.32.24) — 초록", "19122275", "Biological & Pharmaceutical Bulletin (PubMed)"),
 pm(5, "[Study on molecular evidence of revision of taxonomic placement of Peucedanum decursivum]. Zhongguo Zhong Yao Za Zhi 2006;31(18):1488-90 (PMID 17144462) — 영문 초록", "17144462", "China Journal of Chinese Materia Medica (PubMed)"),
 pm(6, "Complete chloroplast genome sequencing support Angelica decursiva is an independent species from Peucedanum praeruptorum. Physiol Mol Biol Plants 2021 (PMID 34924707, doi:10.1007/s12298-021-01097-w) — 초록", "34924707", "Physiology and Molecular Biology of Plants (PMC)", "PMC8639966"),
 pm(7, "The complete chloroplast genome of the medicinal plant Angelica decursiva (Apiaceae) in Peucedani Radix. Mitochondrial DNA B Resour 2016;1(1):210-211 (PMID 33473454, doi:10.1080/23802359.2016.1155089) — 초록", "33473454", "Mitochondrial DNA Part B (PMC)", "PMC7799925"),
 pm(8, "[Discussion on efficacy of traditional Chinese medicine \"Zi-hua Qianhu\" in Chinese Pharmacopoeia (2010 Edition)]. Zhongguo Zhong Yao Za Zhi 2015;40(12):2464-9 (PMID 26591544) — 영문 초록", "26591544", "China Journal of Chinese Materia Medica (PubMed)"),
 pm(9, "Identification of Anti-Inflammatory Compounds from Peucedanum praeruptorum Roots by Using Nitric Oxide-Producing Rat Hepatocytes Stimulated by Interleukin 1β. Molecules 2023;28(13):5076 (PMID 37446738, doi:10.3390/molecules28135076) — 초록", "37446738", "Molecules (MDPI, PMC)", "PMC10343554"),
 pm(10, "Ultrasonic-Assisted Efficient Extraction of Coumarins from Peucedanum decursivum (Miq.) Maxim Using Deep Eutectic Solvents Combined with an Enzyme Pretreatment. Molecules 2022;27(17):5715 (PMID 36080482, doi:10.3390/molecules27175715)", "36080482", "Molecules (MDPI, PMC)", "PMC9458171"),
 pm(11, "Simultaneous Determination of Five Coumarins in Peucedanum Decursivum Radix by UPLC. J Chromatogr Sci 2022;60(2) (PMID 34021565, doi:10.1093/chromsci/bmab055) — 초록", "34021565", "Journal of Chromatographic Science (PubMed)"),
 pm(12, "[Studies on chemical constituents from the herb of Peucedanum decursivum (Miq.) Maxim]. Zhongguo Zhong Yao Za Zhi 2001;26(3):178-80 (PMID 12525036) — 영문 초록·MeSH(Plant Leaves, Plant Stems)", "12525036", "China Journal of Chinese Materia Medica (PubMed)"),
 pm(13, "In vitro antioxidant and anti-inflammatory activities of Angelica decursiva. Arch Pharm Res 2012;35(1):179-92 (PMID 22297757, doi:10.1007/s12272-012-0120-0) — 초록", "22297757", "Archives of Pharmacal Research (PubMed)"),
 pm(14, "Mechanism of anti-inflammatory activity of umbelliferone 6-carboxylic acid isolated from Angelica decursiva. J Ethnopharmacol 2012;144(1):175-81 (PMID 22981803, doi:10.1016/j.jep.2012.08.048) — 초록", "22981803", "Journal of Ethnopharmacology (PubMed)"),
 pm(15, "Inhibition of airway inflammation by the roots of Angelica decursiva and its constituent, columbianadin. J Ethnopharmacol 2014;155(2):1353-61 (PMID 25068578, doi:10.1016/j.jep.2014.07.033) — 초록", "25068578", "Journal of Ethnopharmacology (PubMed)"),
 pm(16, "Angiotensin-I-Converting Enzyme Inhibitory Activity of Coumarins from Angelica decursiva. Molecules 2019;24(21):3937 (PMID 31683604, doi:10.3390/molecules24213937)", "31683604", "Molecules (MDPI, PMC)", "PMC6864762"),
 pm(17, "Angelica decursiva exerts antihypertensive activity by inhibiting L-type calcium channel. J Ethnopharmacol 2023 (PMID 37088236, doi:10.1016/j.jep.2023.116527) — 초록", "37088236", "Journal of Ethnopharmacology (PubMed)"),
 pm(18, "Two O-methyltransferases are responsible for multiple O-methylation steps in the biosynthesis of furanocoumarins from Angelica decursiva. Plant Physiol Biochem 2023 (PMID 39492167, doi:10.1016/j.plaphy.2023.108142) — 초록", "39492167", "Plant Physiology and Biochemistry (PubMed)"),
 pm(19, "Evaluation of Angelica decursiva reference genes under various stimuli for RT-qPCR data normalization. Sci Rep 2021;11:18993 (PMID 34556773, doi:10.1038/s41598-021-98434-6) — 초록", "34556773", "Scientific Reports (PMC)", "PMC8460625"),
 pm(20, "[Dominant selecting culture medium of Peucedanum decursivum by orthogonal design]. Zhong Yao Cai 2001;24(7):471-2 (PMID 11668734) — 영문 초록", "11668734", "Journal of Chinese Medicinal Materials (PubMed)"),
 pm(21, "New Insights Concerning Phytophotodermatitis Induced by Phototoxic Plants. Life (Basel) 2024;14(8):1019 (PMID 39202761, doi:10.3390/life14081019) — 초록", "39202761", "Life (MDPI, PMC)", "PMC11355232"),
 pm(22, "Studies on coumarins of a chinese drug \"Qian-Hu\". Planta Med 1982;44(4):199-203 (PMID 17402118, doi:10.1055/s-2007-971446) — 초록", "17402118", "Planta Medica (PubMed)"),
 pm(23, "The effects of nodakenin on airway inflammation, hyper-responsiveness and remodeling in a murine model of allergic asthma. Immunopharmacol Immunotoxicol 2014;36(5):341-8 (PMID 25090633, doi:10.3109/08923973.2014.947035) — 초록", "25090633", "Immunopharmacology and Immunotoxicology (PubMed)"),
 pm(24, "Decursin: a cytotoxic agent and protein kinase C activator from the root of Angelica gigas. Planta Med 1996;62(1):7-9 (PMID 8720379, doi:10.1055/s-2006-957785) — 초록", "8720379", "Planta Medica (PubMed)"),
 pm(25, "Dihydroxanthyletin-type coumarins from Angelica decursiva that inhibits the formation of advanced glycation end products and human recombinant aldose reductase. Arch Pharm Res 2018;41(2):196-207 (PMID 29230690, doi:10.1007/s12272-017-0999-6) — 초록", "29230690", "Archives of Pharmacal Research (PubMed)"),
 pm(26, "An Efficient Extraction, Characterization and Antioxidant Study of Polysaccharides from Peucedani Decursivi Radix. Plants (Basel) 2025;14(14):2188 (PMID 40733425, doi:10.3390/plants14142188) — 초록", "40733425", "Plants (MDPI, PMC)", "PMC12298027"),
 pm(27, "Forming coumarin C-glycosides via biocatalysis: Characterization of a C-glycosyltransferase from Angelica decursiva. Biochem Biophys Res Commun 2022 (PMID 35569380, doi:10.1016/j.bbrc.2022.05.008) — 초록", "35569380", "Biochemical and Biophysical Research Communications (PubMed)"),
 pm(28, "[Identification of peucedani radix, peucedani decursivi radix and its adulterants using ITS2 sequence]. Zhongguo Zhong Yao Za Zhi 2014;39(21):4186-90 (PMID 25775791) — 영문 초록", "25775791", "China Journal of Chinese Materia Medica (PubMed)"),
 pm(29, "Specific PCR Identification between Peucedanum praeruptorum and Angelica decursiva and Identification between Them and Adulterant Using DNA Barcode. Pharmacogn Mag 2017;13(49):38-45 (PMID 28216881, doi:10.4103/0973-1296.197658) — 초록", "28216881", "Pharmacognosy Magazine (PMC)", "PMC5307912"),
 pm(30, "Reduced allergic lung inflammation by root extracts from two species of Peucedanum through inhibition of Th2 cell activation. J Ethnopharmacol 2017;196:75-83 (PMID 27965051, doi:10.1016/j.jep.2016.12.015) — 초록", "27965051", "Journal of Ethnopharmacology (PubMed)"),
 pm(31, "Coumarins from \"Zi-Hua Qian-Hu\" (supplement). Planta Med 1984;50(2):117-20 (PMID 17340276, doi:10.1055/s-2007-969646) — 초록", "17340276", "Planta Medica (PubMed)"),
 pm(32, "Study on the Anti-Inflammatory Mechanism of Coumarins in Peucedanum decursivum Based on Spatial Metabolomics Combined with Network Pharmacology. Molecules 2024;29(14):3346 (PMID 39064924, doi:10.3390/molecules29143346) — 초록", "39064924", "Molecules (MDPI, PMC)", "PMC11280318"),
]

S = {}
S["overview"] = ("한눈에 보기",
"바디나물(Angelica decursiva (Miq.) Franch. & Sav.)은 산형과(Apiaceae)의 여러해살이풀로, 한국·중국·일본에 자란다[16]. 꽃이 자주색이어서 뿌리 약재 이름으로는 '자화전호(紫花前胡)'라 부르며, 흰 꽃이 피는 백화전호(Peucedanum praeruptorum)와 구별된다[3]. 예전 학명 Peucedanum decursivum (Miq.) Maxim.은 같은 식물을 가리키는 이명으로 쓰인다[3, 5].\n\n"
"식품의약품안전처 「식품원료 목록」에서 바디나물은 '바디나물순'이라는 원료명으로 식품원료(A코드)에 '사용가능'으로 올라 있고, 사용 조건은 '사용가능부위 : 순'이다[1]. 같은 행의 학명에는 흰 꽃 품종인 Angelica decursiva f. albiflora Nakai도 함께 적혀 있고, 영어 이름은 Purple-flower angelica로 적혀 있다[1]. 따라서 이 목록에서 식품으로 쓸 수 있는 부위는 순이며, 약재로 쓰는 뿌리는 허용 부위에 들어 있지 않다[1].\n\n"
"지금까지의 연구는 대부분 약재로 쓰는 말린 뿌리를 다루며, 쿠마린류가 주요 성분이자 약리 작용의 주된 원인으로 정리되어 있다[2]. 잎·줄기를 포함한 지상부에서도 임페라토린·콜룸비아나딘·스코폴레틴 같은 쿠마린이 분리되었다[12]. 그러나 식용하는 순의 성분 함량을 정량한 논문은 확인하지 못함.")
S["history"] = ("역사와 전통 이용",
"바디나물의 말린 뿌리는 중국 전통의학에서 '자화전호'라는 약재로 쓰였고, 가래와 열을 동반한 기침, 두통, 발열 등에 처방되었다고 정리된다[2]. 한국 전통의학에서는 진해·진통·해열 약으로 쓰였다고 보고되었다[16]. 일본에서는 1980년대에 자화전호 뿌리의 쿠마린 연구가 이어졌고, 시장에서 '사전호(Si-Qian-Hu)'라는 이름으로 팔리던 약재가 성분상 자화전호로 판정되었다[22, 31].\n\n"
"약재 '전호(前胡, Peucedani Radix)'의 기원 식물은 나라마다 달랐다[3]. 한국 약전은 전호를 바디나물과 Peucedanum praeruptorum의 뿌리로 규정한다고 보고되었고, 한국에서는 이 뿌리를 가래를 삭이고 기침을 멎게 하는 데 오래 써 왔다[4, 30]. 일본약전도 두 종의 뿌리를 전호로 정한다[9]. 중국에서는 바디나물이 오랫동안 당귀(Angelica sinensis 뿌리)의 대용으로 쓰였고, 근대 기원 연구 과정에서 '전호'로 잘못 쓰이기도 했다[8]. 2010년판 중국약전에는 '자화전호'가 별도 품목으로 실려 있으며, 전호(P. praeruptorum)와는 임상 용도와 화학 조성이 뚜렷이 다르다는 지적이 있다[8].\n\n"
"한국에서는 다른 산형과 식물인 Anthriscus sylvestris가 우리말 이름 '전호'와 같다는 이유로 약재 전호로 시장에 유통된 일이 보고되었다[4]. 바디나물순을 나물로 먹어 온 내력은 공식 문헌으로 확인하지 못함.")
S["biology"] = ("식물학적 특징",
"바디나물은 산형과 당귀속(Angelica)의 여러해살이풀이다[16]. '자화(紫花)'라는 약재 이름처럼 꽃이 자주색이며, 식품원료 목록에는 흰 꽃 품종(f. albiflora)도 같은 원료의 학명으로 함께 올라 있다[1, 3]. 지상부와 약재의 생김새가 Peucedanum praeruptorum·Anthriscus sylvestris와 비슷해 뿌리를 정확히 가려내기 어렵다고 보고되었다[4]. 키·잎 모양·개화기 같은 형태 기재와 국내 자생지 정보는 공식 자료로 확인하지 못함.\n\n"
"성분 면에서는 쿠마린을 많이 만드는 식물로, 쿠마린·테르펜·정유·페놀산·지방산 등 234개 화합물이 보고되었다[2]. 뿌리에는 노다케닌 같은 쿠마린 배당체, 데쿠르시딘 같은 디하이드로잔틸레틴형 피라노쿠마린, 베르갑텐 같은 푸라노쿠마린이 함께 들어 있다[22, 23]. 질량분석 이미징으로 본 뿌리 단면에서는 쿠마린 27종이 확인되었고, 주로 피층·주피·체관부에 몰려 있었다[32]. 잎·줄기를 포함한 지상부에서는 임페라토린·델토인·콜룸비아나딘·스코폴레틴·(+)-trans-데쿠르시디놀 등이 분리되었다[12]. 뿌리와 지상부의 성분 구성은 같지 않으므로, 뿌리 자료를 순에 그대로 옮겨 쓸 수 없다[2, 12].")
S["related_species"] = ("분류와 근연종",
"바디나물은 오랫동안 Peucedanum decursivum (Miq.) Maxim.이라는 이름으로도 불려, 문헌에서 두 학명이 같은 식물을 가리킨다[3]. 핵 리보솜 ITS 염기서열 계통 분석에서 이 종은 Peucedanum 무리가 아니라 Angelica 무리에 들어가, 학명을 Angelica로 바로잡아야 한다는 결과가 나왔다[5]. 엽록체 유전체 비교에서도 바디나물과 P. praeruptorum은 서로 다른 속의 독립된 종으로 나타났다[6]. DNA 바코드와 HPLC 성분 프로필을 함께 본 연구에서 바디나물 시료는 갯기름나물·P. praeruptorum·방풍 시료와 뚜렷이 떨어진 무리를 이루었다[3].\n\n"
"이름이 비슷한 다른 식품원료와 섞지 않도록 주의해야 한다[1]. 식약처 목록의 '전호잎'은 다른 속의 Anthriscus sylvestris이고, '처녀바디잎'(Angelica cartilagino-marginata, 별칭 흰바디나물)과 '잔잎바디잎'(Angelica czernaevia, 별칭 선바디나물)도 별개의 원료다[1]. '참반디잎'의 별칭 '참바디나물'은 Sanicula chinensis를 가리킨다[1]. 같은 당귀속의 참당귀·중국당귀·왜당귀·명일엽·안젤리카·와일드안젤리카도 목록에 따로 올라 있어 이 종의 자료와 구분해야 한다[1]. 피라노쿠마린인 데쿠르신은 처음 바디나물에서 밝혀졌지만 참당귀 뿌리에서도 분리되므로, 성분 이름만으로 종을 판단해서는 안 된다[24].")
S["cultivation"] = ("재배와 생산",
"바디나물의 국내 재배 면적과 생산량은 통계청 농작물생산조사와 특용작물 생산실적 자료에서 품목으로 확인하지 못함. 순을 거두는 시기나 재배 방법에 관한 공식 재배 지침도 확인하지 못함.\n\n"
"성분 연구에 쓰인 시료는 한국과 중국의 재배지·자생지·시장에서 모은 것이었고[3], 중국 구이저우성 더장현에서 사들인 말린 뿌리가 쓰이기도 했다[10]. 약재 품질 관리에는 현미경 감별, HPLC 지문 분석, 유전자 감별이 주로 쓰인다[2]. 자화전호와 전호(P. praeruptorum) 및 위품은 ITS2 바코드나 종 특이 PCR로 구별된다고 보고되어, 원료를 모을 때 종을 확인하는 데 쓸 수 있다[28, 29].\n\n"
"조직배양 연구에서는 MS 기본 배지에 2,4-D 1 mg/L를 넣은 조건이 캘러스 배양에 가장 좋았고, 캘러스에서 쿠마린이 예비적으로 검출되었다[20]. 유전자 발현 연구를 위해 여러 외부 처리 조건에서 안정적인 기준 유전자로 SAND·PP2A·PTBP가 선정되었다[19].")
S["processing"] = ("가공과 이용",
"식품으로는 순만 쓸 수 있으므로, 뿌리 추출물이나 뿌리 쿠마린 연구 결과를 순 식품에 그대로 적용할 수는 없다[1, 2]. 순을 데치거나 말리는 등 식품 가공에 관한 공식 자료와, 식약처 「식품 등의 생산실적」에서 이 종을 원료로 한 품목은 확인하지 못함.\n\n"
"연구용 가공은 주로 뿌리를 대상으로 한다[2]. 말린 뿌리(60 °C에서 24시간 건조, 40메시 분쇄)를 셀룰레이스로 전처리한 뒤 염화콜린·1,4-부탄디올(1:4) 공융용매로 초음파 추출하자 총 쿠마린 추출 수율이 2.65%였다[10]. 같은 연구에서 HPLC-MS로 잰 뿌리 쿠마린은 베르갑텐 2.806 mg/g, 크산토톡신 1.651 mg/g, 움벨리페론 0.707 mg/g, 임페라토린 0.570 mg/g, 데쿠르신 0.449 mg/g, 노다케닌 0.085 mg/g이었다[10]. 뿌리 다당류는 효소 전처리와 천연 공융용매 초음파 추출로 수율 19.93%를 얻었다[26]. 뿌리 쿠마린 정량에는 노다케닌·움벨리페론·소랄렌·크산토톡신·베르갑텐을 동시에 재는 UPLC법도 보고되었다[11]. 전초 메탄올 추출물은 국내 식물추출물은행에서 공급받아 효소 억제 시험에 쓰였다[16].")
S["genetics"] = ("유전 정보",
"바디나물의 엽록체 유전체는 146,719 bp의 원형으로, 큰 단일복사 영역 93,256 bp, 작은 단일복사 영역 17,497 bp, 역반복 영역 17,983 bp 두 개로 이루어지고 GC 함량은 37.56%다[7]. 유전자는 rRNA 4개, tRNA 29개, 단백질 암호 유전자 80개를 합쳐 113개다[7]. P. praeruptorum과 엽록체 유전체를 비교하면 역반복 영역의 반복서열, 큰 단일복사 영역, SSR에서 차이가 커 분자 표지로 쓸 수 있다[6].\n\n"
"감별 표지로는 ITS와 RAPD를 바탕으로 바디나물·P. praeruptorum·A. sylvestris를 한 번의 다중 PCR로 가르는 SCAR 표지가 개발되었다[4]. 자화전호의 ITS2 서열은 227 bp로 시료 사이에 변이가 없었고, 종 사이 거리가 종 안 거리보다 커서 감별에 쓸 수 있었다[28].\n\n"
"쿠마린 생합성 유전자 연구도 진행 중이다[18]. 전사체 분석으로 고른 O-메틸전이효소 14개 후보 가운데 AdOMT1·AdOMT2가 베르갑톨·잔토톡솔 등의 O-메틸화를 맡는 것으로 밝혀졌다[18]. 쿠마린에 C-당을 붙이는 다기능 당전이효소(AdCGT)도 특성이 밝혀졌다[27].")
S["safety"] = ("안전성",
"바디나물순에 대한 식약처·공공기관의 알레르기·잔류농약·독성 정보는 확인하지 못함. 식품원료 목록에서 허용된 부위는 순이며, 뿌리 등 다른 부위는 이 목록상 식품 사용 부위가 아니다[1].\n\n"
"바디나물에는 푸라노쿠마린이 들어 있다[10, 12]. 말린 뿌리에서는 베르갑텐·크산토톡신·임페라토린이 mg/g 단위로 정량되었고[10], 지상부에서도 임페라토린이 분리되었다[12]. 푸라노쿠마린(소랄렌류)은 식물에 닿은 피부가 햇빛의 자외선을 받을 때 홍반·물집·부종·색소침착을 일으키는 식물광피부염의 원인 물질로 알려져 있고, 산형과는 이런 광독성 식물이 많은 과로 꼽힌다[21]. 식용 순에 들어 있는 푸라노쿠마린 함량은 확인하지 못함.\n\n"
"약재 뿌리에 대해서는 카드뮴·납 등 중금속 오염을 엄격히 관리해야 하며, 사람에서의 체내 동태와 독성 연구가 필요하다는 지적이 있다[2]. 이 종의 효능 연구는 대부분 세포·동물 실험이고, 사람 대상 임상 근거는 찾지 못했다[2, 15, 23].")

order = ["overview","history","biology","related_species","cultivation","processing","genetics","safety"]
sections = [{"key": k, "title": S[k][0], "body": S[k][1]} for k in order]

def C(name, ko, cls, role, part, content, act, src):
    return {"name": name, "name_ko": ko, "class": cls, "role": role, "part": part, "content_text": content, "activity_ko": act, "source": src}
compounds = [
 C("Nodakenin","노다케닌","쿠마린 배당체(디하이드로푸라노쿠마린)","marker","뿌리·전초",
   "말린 뿌리 0.085 mg/g(공융용매 초음파 추출 후 HPLC-MS)[10]; 뿌리의 주요 쿠마린 배당체로 소개[23]; 전초 메탄올 추출물 에틸아세테이트 분획에서 분리[13]",
   "난알부민 천식 생쥐에 5–20 mg/kg 경구 투여 시 기도 염증·과민성·재형성 억제(동물 실험)[23]", [10,13,23]),
 C("Nodakenetin","노다케네틴(마르메신)","디하이드로푸라노쿠마린","bioactive","뿌리·전초",
   "뿌리에서 분리[15, 22]; 전초에서 분리[13]", "", [13,15,22]),
 C("Umbelliferone","움벨리페론","단순 쿠마린","bioactive","뿌리·전초",
   "말린 뿌리 0.707 mg/g(HPLC-MS)[10]; 전초에서 분리[13]", "", [10,13]),
 C("Umbelliferone 6-carboxylic acid","움벨리페론-6-카복실산","단순 쿠마린","bioactive","전초",
   "전초에서 처음 분리(함량 보고 없음)[13]",
   "RAW 264.7 세포에서 LPS 유도 NO 생성 억제 IC50 72.98 μg/mL(세포 실험)[13]; 카라기난 발부종 생쥐 50·25 mg/kg에서 각각 70.40·60.20% 억제(동물 실험)[14]", [13,14]),
 C("Bergapten","베르갑텐","선형 푸라노쿠마린","bioactive","뿌리",
   "말린 뿌리 2.806 mg/g(HPLC-MS)[10]; 자화전호 뿌리에서 확인[22]", "광독성 푸라노쿠마린 계열(식물광피부염 원인 물질군)[21]", [10,21,22]),
 C("Xanthotoxin","크산토톡신(메톡살렌)","선형 푸라노쿠마린","bioactive","뿌리",
   "말린 뿌리 1.651 mg/g(HPLC-MS)[10]", "광독성 푸라노쿠마린 계열(식물광피부염 원인 물질군)[21]", [10,21]),
 C("Imperatorin","임페라토린","선형 푸라노쿠마린","bioactive","뿌리·지상부(잎·줄기)",
   "말린 뿌리 0.570 mg/g(HPLC-MS)[10]; 지상부에서 분리[12]", "", [10,12]),
 C("Decursin","데쿠르신","피라노쿠마린","bioactive","뿌리",
   "말린 뿌리 0.449 mg/g(HPLC-MS)[10]; 처음 바디나물에서 밝혀진 성분[24]", "", [10,24]),
 C("Columbianadin","콜룸비아나딘","디하이드로푸라노쿠마린(안굴라형)","bioactive","뿌리·지상부(잎·줄기)",
   "뿌리에서 분리[15]; 지상부에서 분리[12]",
   "LPS 급성 폐 염증 생쥐에 20–60 mg/kg 경구 투여 시 염증 억제(동물 실험)[15]", [12,15]),
 C("Decursidin","데쿠르시딘","디하이드로잔틸레틴형 피라노쿠마린","bioactive","뿌리",
   "자화전호 뿌리에서 확인[22]",
   "사람 재조합 알도스 환원효소·최종당화산물 생성 억제(시험관 실험, 7종 IC50 각각 1.03–21.31·0.41–5.56 μM)[25]", [22,25]),
 C("Scopoletin","스코폴레틴","단순 쿠마린","bioactive","지상부(잎·줄기)",
   "지상부에서 분리[12]", "", [12]),
 C("Demethylsuberosin","데메틸수베로신","프레닐 쿠마린","bioactive","뿌리",
   "뿌리 에탄올 추출물에서 분리[17]",
   "L-NAME 고혈압 생쥐 모델과 혈관 수축 실험에서 강압 작용의 주요 성분으로 제시, 표적은 L형 칼슘 통로 Cav1.2로 추정(동물·세포 실험)[17]", [17]),
 C("Vanillic acid","바닐산","페놀산","bioactive","전초",
   "전초에서 처음 분리[13]", "분리 성분 가운데 시험관 항산화 활성이 가장 높음(시험관 실험)[13]", [13]),
 C("Psoralen","소랄렌","선형 푸라노쿠마린","bioactive","뿌리",
   "뿌리 UPLC 동시 정량 대상 성분(초록에 함량 수치 없음)[11]", "광독성 푸라노쿠마린 계열(식물광피부염 원인 물질군)[21]", [11,21]),
]

E = {k: "" for k in ["instrument","column","mobile_phase","gradient","flow","temp","detection","injection","sample_prep","standard","linearity","lod","loq","recovery"]}
a1 = dict(E); a1.update({
 "instrument": "Agilent 1290-6460 삼중사중극자 질량분석기(HPLC-MS)",
 "column": "Agilent Eclipse Plus-C18, 150 mm × 2.1 mm, 1.8 μm",
 "mobile_phase": "A: 0.1% 포름산, B: 메탄올",
 "gradient": "0–0.5분 5→15% B, 0.5–0.8분 15→28%, 0.8–1.0분 28→32%, 1.0–1.2분 32→38%, 1.2–1.5분 38→45%, 1.5–4.5분 45→65%, 4.5–5.5분 65→95%, 5.5–6.0분 95→5%, 6.0–8.0분(원문 표기 '95%~5% B')",
 "flow": "0.3 mL/min",
 "temp": "35 °C",
 "detection": "ESI 양이온 모드, 다중반응검지(MRM); 건조 가스 질소 295 °C·11 L/min, 분무기 압력 15 psi, 분무 전압 −4.0 kV(원문 표기)",
 "injection": "10.0 μL",
 "sample_prep": "뿌리를 60 °C에서 24시간 건조 후 40메시 분쇄; 분말 2.0 g을 염화콜린/1,4-부탄디올(몰비 1:4, 수분 30%) 공융용매로 셀룰레이스 0.2%·pH 5.0·45 °C 효소 전처리 후 초음파 추출(최적 조건 액고비 14:1 mL/g, 60 °C, 50분); 0.22 μm 막 여과",
 "standard": "움벨리페론·노다케닌·크산토톡신·베르갑텐·임페라토린·데쿠르신 표준품(순도 ≥ 98%), 메탄올 1 mg/mL 원액을 희석한 혼합 표준용액, 외부표준 검량선",
 "linearity": "6개 농도 3반복 검량선, R² > 0.9941(농도 범위는 본문에 없음)",
 "lod": "",
 "loq": "",
 "recovery": "첨가 회수 시험 RSD 1.49%(움벨리페론)·1.40%(노다케닌)·0.68%(크산토톡신)·1.56%(베르갑텐)·1.38%(임페라토린)·2.04%(데쿠르신); 회수율 % 값은 본문에서 확인하지 못함"})
a2 = dict(E); a2.update({
 "column": "Symmetry C18, 4.6 mm × 250 mm, 5 μm",
 "mobile_phase": "아세토니트릴–물",
 "gradient": "기울기 용리(세부 시간표는 초록에 없음)",
 "flow": "1.0 mL/min",
 "temp": "30 °C",
 "detection": "UV 325 nm(움벨리페론·노다케닌), 259 nm(소랄렌·크산토톡신·베르갑텐)",
 "injection": "10 μL",
 "linearity": "R² ≥ 0.9998",
 "recovery": "평균 회수율 101.31·105.27·90.85·106.42·90.19%(RSD 3.07·3.17·1.62·2.53·4.54%), 순서는 초록의 성분 나열 순(움벨리페론·노다케닌·소랄렌·크산토톡신·베르갑텐)"})
assays = [
 {"role": "literature", "compound": "Nodakenin", "compound_ko": "노다케닌(쿠마린 6종 동시 정량)",
  "part": "뿌리(말린 약재 분말) — 식용 부위인 순이 아님",
  "content": "움벨리페론 0.707, 노다케닌 0.085, 크산토톡신 1.651, 베르갑텐 2.806, 임페라토린 0.570, 데쿠르신 0.449 mg/g[10]",
  "method": "HPLC-MS/MS(MRM)", "conditions": a1,
  "rationale": "논문은 노다케닌을 약전 규정상 이 약재 쿠마린의 검출 지표로 소개했다[10]. 정량 대상은 뿌리이며, 식용 부위인 순의 쿠마린 정량 논문은 찾지 못해 뿌리 자료를 참고용으로 둔다. HPLC-MS의 검출·정량한계는 본문에서 확인하지 못함(같은 논문의 총 쿠마린 UV법 LOD 0.2360 μg/mL·LOQ 0.7453 μg/mL은 다른 방법임).",
  "source": [10], "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9458171/", "source_kind": "paper"},
 {"role": "literature", "compound": "Nodakenin", "compound_ko": "노다케닌 등 쿠마린 5종(UPLC 동시 정량)",
  "part": "뿌리(Peucedanum Decursivum Radix) — 식용 부위인 순이 아님",
  "content": "", "method": "UPLC-UV", "conditions": a2,
  "rationale": "약재 품질관리 기준으로 쓰기 위해 노다케닌·움벨리페론·소랄렌·크산토톡신·베르갑텐을 동시에 재는 방법이다[11]. 전문 확인 못함 — 초록에 적힌 조건만 옮겼고 함량·기기 정보는 비워 둠.",
  "source": [11], "url": "https://pubmed.ncbi.nlm.nih.gov/34021565/", "source_kind": "paper"},
]

d = {
 "slug": "angelica-decursiva", "name_ko": "바디나물", "name_en": "Purple-flower angelica",
 "scientific_name": "Angelica decursiva (Miq.) Franch. & Sav.",
 "aliases": ["바디나물순", "자화전호(紫花前胡)", "Peucedanum decursivum (Miq.) Maxim.", "Angelica decursiva f. albiflora Nakai", "Zi-hua Qianhu"],
 "sections": sections, "compounds": compounds, "markers": [], "assays": assays,
 "nutrients": [], "production": [], "world": [], "gi": [], "orgs": [], "sources": sources,
}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in sections: print(s["key"], len(s["body"]))
