import json
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "dossier.json"
ACC = "2026-11-02"
PM = "https://pubmed.ncbi.nlm.nih.gov/{}/"
PMC = "https://pmc.ncbi.nlm.nih.gov/articles/{}/"

sources = [
    (1, "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 한삼덩굴잎·한삼덩굴순·한삼덩굴추출분말(Humulus japonicus Siebold et Zucc, 식품원료 A코드, 제한적사용, '제한적사용가능부위 : 잎, 순') 행, 건강기능식품(C코드) 개별인정 '한삼덩굴추출분말(HSy2)(제2025-41호)' 행, 같은 속 호프(Humulus lupulus L., 사용가능) 행 (로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json)",
     "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "식품의약품안전처", "2026-10-13"),
    (2, "식품의약품안전처 「식품 등의 생산실적」 2025년판 — 건강기능식품 개별인정형 '한삼덩굴추출분말(HSy2)' 행(앱 파싱본 docs/stats/hf_items.csv, 금액 천원 단위)",
     "https://www.mfds.go.kr", "식품의약품안전처", "2026-10-12"),
    (3, "Dereplication of Components Coupled with HPLC-qTOF-MS in the Active Fraction of Humulus japonicus and It's Protective Effects against Parkinson's Disease Mouse Model. Molecules 2019;24(7):1435 (PMID 30979037, doi:10.3390/molecules24071435) — 전문 확인",
     PMC.format("PMC6480934"), "Molecules (MDPI, PMC)", ACC),
    (4, "[Study on quality standard for Humulus scandens]. Zhongguo Zhong Yao Za Zhi 2014;39(20):3986-90 (PMID 25751951) — 초록",
     PM.format("25751951"), "China Journal of Chinese Materia Medica (PubMed)", ACC),
    (5, "LC-MS/MS profiling of polyphenol-enriched leaf, stem and root extracts of Korean Humulus japonicus Siebold & Zucc and determination of their antioxidant effects. Biomed Chromatogr 2018;32(5):e4171 (PMID 29240230, doi:10.1002/bmc.4171) — 초록",
     PM.format("29240230"), "Biomedical Chromatography (PubMed)", ACC),
    (6, "LC determination of luteolin-7-O-β-D-glucoside and apigenin-7-O-β-D-glucoside in rat plasma after administration of Humulus scandens extract and its application to pharmacokinetic studies. Nat Prod Res 2012;26(6):530-9 (PMID 21756194, doi:10.1080/14786419.2010.532127) — 초록",
     PM.format("21756194"), "Natural Product Research (PubMed)", ACC),
    (7, "Glycosyl flavones from Humulus japonicus suppress MMP-1 production via decreasing oxidative stress in UVB irradiated human dermal fibroblasts. BMB Rep 2020;53(7):379-384 (PMID 32317077, doi:10.5483/BMBRep.2020.53.7.253) — 초록",
     PMC.format("PMC7396918"), "BMB Reports (PMC)", ACC),
    (8, "Characterization of tyrosinase inhibitory constituents from the aerial parts of Humulus japonicus using LC-MS/MS coupled online assay. Bioorg Med Chem 2018;26(2):509-515 (PMID 29254897, doi:10.1016/j.bmc.2017.12.011) — 초록",
     PM.format("29254897"), "Bioorganic & Medicinal Chemistry (PubMed)", ACC),
    (9, "Two new phenolic constituents of Humulus japonicus and their cytotoxicity test in vitro. Arch Pharm Res 2007;30(11):1471-5 (PMID 18087817, doi:10.1007/BF02977373) — 초록",
     PM.format("18087817"), "Archives of Pharmacal Research (PubMed)", ACC),
    (10, "[A new dihydrochalcone from Humulus scandens]. Zhongguo Zhong Yao Za Zhi 2023;48(7):1885-1891 (PMID 37282964, doi:10.19540/j.cnki.cjcmm.20221231.201) — 초록",
     PM.format("37282964"), "China Journal of Chinese Materia Medica (PubMed)", ACC),
    (11, "Prenylflavonoid variation in Humulus lupulus: distribution and taxonomic significance of xanthogalenol and 4'-O-methylxanthohumol. Phytochemistry 2000;53(7):759-75 (PMID 10783982, doi:10.1016/s0031-9422(00)00005-4) — 초록",
     PM.format("10783982"), "Phytochemistry (PubMed)", ACC),
    (12, "The Extract of Humulus japonicus Inhibits Lipogenesis and Promotes Lipolysis via PKA/p38 Signaling. Obes Facts 2024;17(5):513-523 (PMID 39102791, doi:10.1159/000540699) — 전문 확인",
     PMC.format("PMC11458159"), "Obesity Facts (PMC)", ACC),
    (13, "Humulus japonicus Extract Ameliorates Hepatic Steatosis Through the PPAR-Mediated Suppression of Alcohol-Induced Oxidative Stress. J Med Food 2023;26(3):193-200 (PMID 36827085, doi:10.1089/jmf.2022.K.0093) — 초록",
     PM.format("36827085"), "Journal of Medicinal Food (PubMed)", ACC),
    (14, "Humulus japonicus inhibits the progression of Alzheimer's disease in a APP/PS1 transgenic mouse model. Int J Mol Med 2017;39(1):21-30 (PMID 28004107, doi:10.3892/ijmm.2016.2804) — 초록",
     PMC.format("PMC5179182"), "International Journal of Molecular Medicine (PMC)", ACC),
    (15, "Humulus scandens exhibits immunosuppressive effects in vitro and in vivo by suppressing CD4(+) T cell activation. Am J Chin Med 2014;42(4):921-34 (PMID 25004883, doi:10.1142/S0192415X1450058X) — 초록",
     PM.format("25004883"), "The American Journal of Chinese Medicine (PubMed)", ACC),
    (16, "Application potential of Humulus Scandens in livestock husbandry. J Anim Physiol Anim Nutr 2023;107(6):1392-1401 (PMID 37277943, doi:10.1111/jpn.13847) — 초록",
     PM.format("37277943"), "Journal of Animal Physiology and Animal Nutrition (PubMed)", ACC),
    (17, "Assessing the Invasion Risk of Humulus japonicus Using Ensemble Species Distribution Modeling and Habitat Connectivity Analysis. Plants 2022;11(7):857 (PMID 35406837, doi:10.3390/plants11070857) — 전문 확인",
     PMC.format("PMC9002559"), "Plants (MDPI, PMC)", ACC),
    (18, "Sex chromosome differentiation in Humulus japonicus Siebold & Zuccarini, 1846 (Cannabaceae) revealed by fluorescence in situ hybridization of subtelomeric repeat. Comp Cytogenet 2012;6(3):239-47 (PMID 24260665, doi:10.3897/CompCytogen.v6i3.3261) — 초록",
     PMC.format("PMC3833800"), "Comparative Cytogenetics (PMC)", ACC),
    (19, "C-Banding/DAPI and in situ hybridization reflect karyotype structure and sex chromosome differentiation in Humulus japonicus Siebold & Zucc. Cytogenet Genome Res 2011;132(3):203-11 (PMID 21079383, doi:10.1159/000321584) — 초록",
     PM.format("21079383"), "Cytogenetic and Genome Research (PubMed)", ACC),
    (20, "Genome-wide analysis of transposable elements and satellite DNA in Humulus scandens, a dioecious plant with XX/XY1Y2 chromosomes. Front Plant Sci 2023;14:1230250 (PMID 37908838, doi:10.3389/fpls.2023.1230250) — 전문 확인",
     PMC.format("PMC10614002"), "Frontiers in Plant Science (PMC)", ACC),
    (21, "Allergenic Pollen Calendar in Korea Based on Probability Distribution Models and Up-to-Date Observations. Allergy Asthma Immunol Res 2020;12(2):259-273 (PMID 32009321, doi:10.4168/aair.2020.12.2.259) — 전문 확인",
     PMC.format("PMC6997285"), "Allergy, Asthma & Immunology Research (PMC)", ACC),
    (22, "Allergens of Regional Importance in Korea. Front Allergy 2021;2:652275 (PMID 35386990, doi:10.3389/falgy.2021.652275) — 초록",
     PMC.format("PMC8974691"), "Frontiers in Allergy (PMC)", ACC),
    (23, "Identification and characterization of the major allergen of the Humulus japonicus pollen. Clin Exp Allergy 1999;29(8):1080-6 (PMID 10457112, doi:10.1046/j.1365-2222.1999.00615.x) — 초록",
     PM.format("10457112"), "Clinical & Experimental Allergy (PubMed)", ACC),
    (24, "Characterization of Hum j 6, a Major Allergen From Humulus japonicus Pollen, the Primary Cause of Weed Pollinosis in East Asia. Allergy Asthma Immunol Res 2023;15(6):767-778 (PMID 37957794, doi:10.4168/aair.2023.15.6.767) — 초록",
     PMC.format("PMC10643856"), "Allergy, Asthma & Immunology Research (PMC)", ACC),
    (25, "A novel recognition of the major allergen, Hum j 1, from Humulus japonicus pollen. World Allergy Organ J 2025;18(8):101104 (PMID 40822751, doi:10.1016/j.waojou.2025.101104) — 초록",
     PMC.format("PMC12355532"), "World Allergy Organization Journal (PMC)", ACC),
    (26, "Characterization of the clinical relevance and hypoallergenic peptides of the newly evidenced major allergen Hum j 1. Front Immunol 2025;16:1588870 (PMID 40625753, doi:10.3389/fimmu.2025.1588870) — 초록",
     PMC.format("PMC12230049"), "Frontiers in Immunology (PMC)", ACC),
    (27, "IgE Cross-Reactivity between Humulus japonicus and Humulus lupulus. Yonsei Med J 2018;59(7):852-856 (PMID 30091318, doi:10.3349/ymj.2018.59.7.852) — 초록",
     PMC.format("PMC6082984"), "Yonsei Medical Journal (PMC)", ACC),
    (28, "Sensitization of common allergens and co-sensitization patterns in the Korean population (2019 국민건강영양조사 자료). Sci Rep 2025;15:13664 (PMID 40258970, doi:10.1038/s41598-025-98470-6) — 전문 확인",
     PMC.format("PMC12012044"), "Scientific Reports (PMC)", ACC),
    (29, "Prevalence of sensitization to weed pollens of Humulus scandens, Artemisia vulgaris, and Ambrosia artemisiifolia in northern China. J Zhejiang Univ Sci B 2013;14(3):240-6 (PMID 23463767, doi:10.1631/jzus.B1200185) — 초록",
     PMC.format("PMC3596575"), "Journal of Zhejiang University Science B (PMC)", ACC),
    (30, "Identification and characterization of natural PR-1 protein as major allergen from Humulus japonicus pollen. Mol Immunol 2023;153:170-180 (PMID 36525884, doi:10.1016/j.molimm.2022.11.023) — 초록",
     PM.format("36525884"), "Molecular Immunology (PubMed)", ACC),
    (31, "Emerging Hop Japanese Pollinosis in Asia. Curr Protein Pept Sci 2022;23(11):714-720 (PMID 35658882, doi:10.2174/1389203723666220603155320) — 초록",
     PM.format("35658882"), "Current Protein & Peptide Science (PubMed)", ACC),
    (32, "Humulus japonicus Enhances Bone Growth and Microarchitecture in Rats: Potential Involvement of IGF-1 Signaling. J Med Food 2025;28(6):542-552 (PMID 40372960, doi:10.1089/jmf.2025.k.0002) — 초록",
     PM.format("40372960"), "Journal of Medicinal Food (PubMed)", ACC),
    (33, "Long-term nonferrous metal smelting affects metal accumulation/transfer in a soil-plant-woodlouse system. J Environ Qual 2025;54(6):2014-2024 (PMID 40754860, doi:10.1002/jeq2.70065) — 초록",
     PM.format("40754860"), "Journal of Environmental Quality (PubMed)", ACC),
    (34, "Cloning, expression, and characterization of pollen allergens from Humulus scandens (Lour) Merr and Ambrosia artemisiifolia L. Acta Pharmacol Sin 2005;26(10):1225-32 (PMID 16174439, doi:10.1111/j.1745-7254.2005.00194.x) — 초록",
     PM.format("16174439"), "Acta Pharmacologica Sinica (PubMed)", ACC),
    (35, "Water extract of Humulus japonicus improves age-related cognitive decline by inhibiting acetylcholinesterase activity and the acetylcholine signaling pathway. Mol Med Rep 2025;31(5) (PMID 40116124, doi:10.3892/mmr.2025.13496) — 초록",
     PMC.format("PMC11938412"), "Molecular Medicine Reports (PMC)", ACC),
]

sections = [
    ("overview", "한눈에 보기",
     "한삼덩굴(Humulus japonicus Siebold & Zucc.)은 삼과(Cannabaceae)에 속하는 덩굴성 풀로, 중국·일본·한국 등 아시아 여러 지역에서 자라며 Humulus scandens라는 이명으로도 불린다[3]. 영어로는 Japanese hop, 중국어로는 lü cao, 일본어로는 kanamugura라고 부른다[16]. 학술 문헌에서는 H. japonicus와 H. scandens 두 학명이 함께 쓰이지만 같은 종을 가리킨다[3][16].\n\n"
     "식품의약품안전처 「식품원료 목록」에서 한삼덩굴은 '한삼덩굴잎'·'한삼덩굴순'·'한삼덩굴추출분말'이라는 원료명으로 식품원료(A코드)에 올라 있다[1]. 세 원료 모두 '제한적사용' 원료이고 사용 조건은 '제한적사용가능부위 : 잎, 순'이어서, 잎과 순만 식품에 제한적으로 쓸 수 있다[1]. 제한적 사용 원료에 적용되는 식품공전의 구체적인 사용 방법·사용량 기준은 원문으로 확인하지 못함. 같은 목록의 건강기능식품(C코드)에는 개별인정형 원료 '한삼덩굴추출분말(HSy2)(제2025-41호)'이 올라 있다[1]. 이 원료의 인정 기능성 문구와 1일 섭취량은 원문으로 확인하지 못함.\n\n"
     "잎과 지상부의 주요 성분은 루테올린-7-O-글루코사이드와 아피제닌-7-O-글루코사이드 같은 플라본 배당체다[3][4]. 한편 한삼덩굴 꽃가루는 한국의 가을철(8–10월) 꽃가루 알레르기를 일으키는 대표적인 원인으로 꼽힌다[21][22]."),
    ("history", "역사와 전통 이용",
     "한삼덩굴은 한국 전통의학에서 폐결핵·이질·만성 대장염·고혈압 치료에 쓰였다고 소개된다[3]. 다른 연구는 한국에서 폐 질환·피부 질환·고혈압 환자에게 써 왔다고 적었고[14], 한국에서 잎을 폐결핵·경부 림프절염·고혈압 치료에 이용했다고 정리했다[12]. 같은 논문은 한삼덩굴을 설사·고혈압·폐렴·나병 등에 써 온 전통 식품 겸 약용 식물로 소개했다[12].\n\n"
     "중국에서도 결핵·이질·만성 대장염 치료에 널리 쓰는 전통 약재로 소개된다[15]. 중국에서는 약재 품질을 관리하려고 중국약전(2010년판) 부록 방법에 따른 수분·회분 검사와 박층크로마토그래피(TLC)·HPLC 확인 시험을 담은 품질 기준안이 2014년에 제안되었다[4]. 빨리 자라고 수확량이 많은 점 때문에 항생제를 대신할 가축 사료 첨가 원료로도 검토되고 있다[16].\n\n"
     "꽃가루 알레르기 연구의 역사도 길다[23][25]. 1999년 국내 연구는 환자 29명의 혈청으로 10 kDa 단백질을 한삼덩굴 꽃가루의 주요 알레르겐 후보로 제시했다[23]. 이 단백질은 N-말단 서열만 알려져 있다가 2025년 중국 연구에서 성숙 단백질 서열의 98.9%가 확인되어 Hum j 1로 확정되었다[25].\n\n최근에는 기능성 소재로서의 동물 연구가 이어지고 있다[32][35]. 어린 쥐에게 추출물을 4주 먹이자 고용량(292 mg/kg/일) 군에서 대퇴골·경골 길이가 늘었고[32], 늙은 생쥐에게 물 추출물을 먹이자 기억·학습 시험 성적이 좋아졌다[35]. 사람 대상 효과는 이번 조사에서 확인하지 못함."),
    ("biology", "식물학적 특징",
     "한삼덩굴은 빨리 자라는 덩굴성 풀로, 원산지는 동부 구북구(동아시아 일대)이며 유럽과 북아메리카에 들어가 침입종이 되었다[17]. 한해살이풀로 소개되지만[3] 일부 문헌은 여러해살이풀로 적었고[7], 침수 같은 스트레스를 받으면 막뿌리를 내어 여러해살이처럼 살기도 한다[17]. 잎·줄기·꽃의 크기 등 형태 수치는 공공기관 자료로 확인하지 못함.\n\n"
     "암그루와 수그루가 따로 있는 암수딴그루 식물이다[18][20]. 염색체 수는 암그루 2n = 16(상염색체 14 + XX), 수그루 2n = 17(상염색체 14 + XY1Y2)이다[18]. 꽃가루는 한국에서 8월부터 10월 사이에 날린다[21].\n\n"
     "번식은 씨앗으로 하며, 씨앗은 흙 속에서 약 3년 살아남고 물에 실려 쉽게 퍼진다[17]. 씨앗은 이른 봄에 싹트며, 발아하려면 겨울의 저온을 거쳐야 한다[17]. 강가·범람원 같은 습한 곳의 양토·식양토를 좋아하고, 길가·철로변·숲 가장자리 같은 교란된 곳에도 자리 잡는다[17]. 한번 자리 잡으면 빽빽한 덤불을 이뤄 다른 식물의 빛을 가린다[17]. 잎의 분비샘에서는 호프(H. lupulus)의 프레닐 플라보노이드가 만들어지지 않았다[11]."),
    ("related_species", "같은 속·혼동 주의 식물",
     "같은 Humulus 속의 호프(Humulus lupulus L.)는 양조에 쓰이는 식물로, 한삼덩굴과는 다른 종이다[1][5]. 「식품원료 목록」에서 호프는 순·꽃봉오리·꽃·열매를 쓸 수 있는 '사용가능' 원료인 반면, 한삼덩굴은 잎·순만 쓰는 '제한적사용' 원료다[1]. 호프 암꽃의 대표 성분인 잔토휴몰 계열 프레닐 플라보노이드는 호프 120여 그루에서 모두 검출되었지만 한삼덩굴 잎 분비샘에서는 만들어지지 않았다[11]. 다만 한삼덩굴 지상부 분석에서 휴물론·루풀론 같은 쓴맛산으로 추정되는 피크가 질량 분석으로 예측된 바 있다[3].\n\n"
     "두 종은 유전체 구성도 다르다[20]. 반복 서열 비율은 한삼덩굴 암그루 68.30%, 수그루 66.78%로 호프(59.45%)보다 높았다[20]. 꽃가루 알레르겐도 겹치지 않는 편이어서, 한삼덩굴에 대한 IgE 반응은 호프 꽃가루로 최대 16.7%만 억제되었고 한삼덩굴의 12 kDa 주요 반응 성분은 호프에 없었다[27].\n\n"
     "가을철 꽃가루 알레르기를 함께 일으키는 쑥·돼지풀과도 구별된다[21][29]. 중국 북부 연구에서 한삼덩굴과 쑥, 한삼덩굴과 돼지풀의 특이 IgE 사이에는 상관이 없어 서로 독립적인 감작원으로 해석되었다[29]. 반면 범알레르겐인 프로필린은 한삼덩굴과 돼지풀 사이에 교차반응이 확인되었다[34]."),
    ("cultivation", "자생·재배",
     "한삼덩굴은 대부분 야생에서 자라는 잡초성 식물이며, 국내 재배 면적·생산량 통계는 통계청·농림축산식품부 자료에서 확인하지 못함. 연구용 시료로는 2014년 강원도에서 채취한 지상부가 쓰였고[3], 중국 연구에서는 대학 정원 포장에서 길러 암수를 꽃 모양으로 구별했다[20].\n\n"
     "생태적으로는 씨앗이 흙 속에서 약 3년 살아남고, 이른 봄 3월에 1 m²당 약 35개체까지 싹이 터 빠르게 자란다[17]. 자갈 운반에 섞인 씨앗이 새 서식지로 퍼지는 경로로 지목되며, 유럽에서는 장식용 식물로 판매되는 것도 확산 요인이다[17]. 루마니아 연구에서는 1942년 처음 야생에서 관찰된 뒤 강줄기를 따라 퍼져, 큰 강 유역 전체가 침입 위험 지역으로 평가되었다[17]. 이 논문은 한삼덩굴을 유럽연합 침입외래종 목록에 최근 포함된 종으로 소개했다[17].\n\n"
     "생장이 빠르고 수확량이 많아 가축 사료 자원으로 활용하려는 연구가 이어지고 있다[16]. 재배 기술(파종 시기·수확 시기)에 관한 국내 공공기관 자료는 확인하지 못함."),
    ("processing", "가공·제품",
     "「식품원료 목록」에 오른 형태는 잎(한삼덩굴잎), 순(한삼덩굴순), 추출분말(한삼덩굴추출분말)이다[1]. 연구에 쓰인 추출물 제조 예를 보면, 잎 1.2 kg에 30% 에탄올 10배량을 넣고 85 °C에서 3시간씩 두 번 추출해 감압 농축·건조한 결과 수율이 8.58%였다[12]. 지상부 1 kg을 70% 에탄올로 60 °C 초음파 추출한 뒤 합성흡착수지(HP-20)로 분획하자, 루테올린-7-O-글루코사이드가 13.4 μg/mg에서 168.4 μg/mg으로, 아피제닌-7-O-글루코사이드가 6.5 μg/mg에서 62.8 μg/mg으로 농축되었다[3].\n\n"
     "건강기능식품 개별인정형 원료 '한삼덩굴추출분말(HSy2)'은 식약처 「식품 등의 생산실적」 2025년판에 생산량 4.0톤, 생산액 121,767천원(약 1.22억 원), 판매량 4.0톤, 판매액 153,602천원(약 1.54억 원)으로 집계되었다[2]. 이 원료의 제조 기준과 지표성분 규격은 원문으로 확인하지 못함.\n\n"
     "품질 관리용 분석법으로는 중국 약재의 루테올린-7-O-글루코사이드·아피제닌-7-O-글루코사이드 HPLC 정량법[4]과 국내산 잎·줄기·뿌리의 폴리페놀 26종 LC-MS/MS 분석법[5]이 보고되었다. 가축 사료로 쓸 때의 가공 방법도 따로 정리되어 있다[16]."),
    ("genetics", "유전·유전체",
     "한삼덩굴은 X염색체와 상염색체의 비율(X:A)로 성이 정해지는 암수딴그루 식물로, 암그루는 X:A 비율 1.0, 수그루는 0.5다[20]. 수그루는 Y염색체를 두 개(Y1, Y2) 가지며, 아텔로미어 반복 서열(HJSR) 형광 표지는 X염색체 한쪽 팔과 Y1의 양쪽 팔에는 붙지만 Y2에는 붙지 않는다[18]. C-밴딩/DAPI 염색에서 X염색체는 AT가 많은 밝은 말단 부위가 하나, Y1은 둘이며 Y2는 DAPI 신호가 전혀 없었다[19]. 5S·45S rDNA 표지를 이용해 가장 큰 두 쌍을 뺀 모든 상염색체를 구별하는 핵형도가 만들어졌다[19].\n\n"
     "2023년 차세대 염기서열 분석에서 반복 서열은 암그루 유전체의 68.30%, 수그루 유전체의 66.78%를 차지했다[20]. 그중 LTR 레트로트랜스포존이 유전체의 약 60%로 가장 많았고, Ty3/gypsy 계열이 Ty1/copia 계열보다 30배 이상 많았으며 Tekay·Retand 계통이 특히 불어났다[20]. Athila 계통은 X염색체나 상염색체보다 두 Y염색체에서 신호가 뚜렷이 강했다[20]. 새로 찾은 위성 DNA 3종의 분포로 보아 XY1Y2 성염색체는 동원체 분열에서 생겼을 가능성이 제기되었다[20]. 전체 유전체 크기와 참조 유전체 조립 결과는 확인하지 못함."),
    ("safety", "안전성·주의",
     "한삼덩굴은 「식품원료 목록」에서 '제한적사용' 원료이며 잎과 순만 쓸 수 있다[1]. 제한적 사용 원료의 구체적인 사용량·사용 방법 기준과 국내 공공기관의 잔류농약·중금속·독성 정보는 확인하지 못함. 사람을 대상으로 한 독성·임상 시험 논문은 PubMed 검색에서 확인하지 못함. 제련소 주변 오염 지역 조사에서 한삼덩굴의 토양 중금속 생물농축계수는 모두 1 미만이었다[33].\n\n"
     "가장 분명한 위험은 꽃가루 알레르기다[21][31]. 한국에서 한삼덩굴 꽃가루는 8–10월에 날리며, 2007–2017년 전국 8개 관측소 모두에서 가을철 알레르기를 강하게 일으키는 꽃가루로 꼽혔다[21]. 이 논문은 한국의 천식·비염·결막염 환자 6.1–14%가 한삼덩굴 꽃가루에 반응한다고 인용했다[21]. 2019년 국민건강영양조사에서 혈청 검사를 받은 2,397명 중 167명이 한삼덩굴에 감작되어 있었다[28]. 대기오염과 지구온난화로 감작률·꽃가루 수·알레르기 유발성이 늘고 있다는 지적이 있다[31].\n\n"
     "주요 알레르겐으로는 Hum j 1(환자 93명 중 74.2% 반응), Hum j 6(22명 중 86.4%), Hum j PR-1(30명 중 76.6%)이 보고되었다[24][26][30]. Hum j 1에 감작된 환자는 천식 동반 위험이 더 높았다(오즈비 3.98)[26]. 꽃가루 알레르기 환자가 잎·순을 먹을 때의 교차 반응과 임신·수유 중 안전성은 확인하지 못함."),
]

def ref(*n):
    return [*n]

compounds = [
    {"name": "Luteolin 7-O-glucoside", "name_ko": "루테올린-7-O-글루코사이드(시나로사이드, 루테올로사이드)", "class": "플라본 배당체", "role": "marker", "part": "지상부·잎",
     "content_text": "지상부 70% 에탄올 추출물 13.4 μg/mg, HP-20 활성 분획 168.4 μg/mg[3]; 중국 약재(H. scandens) 16배치 0.015–0.651%(평균 0.148%)[4]",
     "activity_ko": "지방세포에서 지방 축적 억제·지방 분해 촉진(세포 실험)[12]; 에탄올로 유도한 간세포 지방 축적·산화 스트레스 완화(세포 실험)[13]; UVB 조사 섬유아세포에서 MMP-1 생성 억제[7]", "source": ref(3, 4, 7, 12, 13)},
    {"name": "Apigenin 7-O-glucoside", "name_ko": "아피제닌-7-O-글루코사이드(코스모신)", "class": "플라본 배당체", "role": "marker", "part": "지상부",
     "content_text": "지상부 70% 에탄올 추출물 6.5 μg/mg, HP-20 활성 분획 62.8 μg/mg[3]; 중국 약재(H. scandens) 0.003–0.118%(평균 0.036%)[4]",
     "activity_ko": "활성 분획(HJF)의 주성분으로 파킨슨병 생쥐 모델의 운동 기능 개선에 기여하는 성분으로 추정[3]; 쥐 혈장 약동학 정량 대상[6]", "source": ref(3, 4, 6)},
    {"name": "Vitexin", "name_ko": "비텍신(아피제닌-8-C-글루코사이드)", "class": "플라본 C-배당체", "role": "bioactive", "part": "지상부",
     "content_text": "70% 에탄올 추출물 1.90 μg/mg, 활성 분획 10.4 μg/mg[3]",
     "activity_ko": "20 μM에서 아피제닌·루테올린과 함께 MAO-B를 58–79% 억제(효소 실험)[3]; UVB 조사 섬유아세포 MMP-1 억제[7]", "source": ref(3, 7)},
    {"name": "Orientin", "name_ko": "오리엔틴(루테올린-8-C-글루코사이드)", "class": "플라본 C-배당체", "role": "bioactive", "part": "지상부(에틸아세테이트 분획)",
     "content_text": "함량 확인하지 못함(분리 보고)[7]",
     "activity_ko": "분리한 플라본 배당체 3종 가운데 UVB 유도 광노화 억제가 가장 강함(세포 실험)[7]", "source": ref(7)},
    {"name": "Luteolin", "name_ko": "루테올린", "class": "플라본", "role": "bioactive", "part": "지상부",
     "content_text": "70% 에탄올 추출물 0.24 μg/mg, 활성 분획 0.50 μg/mg[3]",
     "activity_ko": "MAO-B 억제 활성이 가장 강한 성분 가운데 하나(효소 실험)[3]", "source": ref(3)},
    {"name": "Apigenin", "name_ko": "아피제닌", "class": "플라본", "role": "bioactive", "part": "지상부",
     "content_text": "70% 에탄올 추출물 0.29 μg/mg, 활성 분획 0.40 μg/mg[3]",
     "activity_ko": "MAO-B 억제 활성이 가장 강한 성분 가운데 하나(효소 실험)[3]", "source": ref(3)},
    {"name": "Eugenyl beta-D-glucopyranoside", "name_ko": "유제닐-β-D-글루코피라노사이드", "class": "페닐프로파노이드 배당체", "role": "bioactive", "part": "지상부",
     "content_text": "70% 에탄올 추출물 0.40 μg/mg, 활성 분획 2.70 μg/mg[3]",
     "activity_ko": "지상부 메탄올 추출물에서도 분리됨[9]", "source": ref(3, 9)},
    {"name": "N-trans-Coumaroyltyramine", "name_ko": "트랜스-N-쿠마로일티라민", "class": "페놀 아마이드", "role": "bioactive", "part": "지상부",
     "content_text": "함량 확인하지 못함(주요 성분으로 분리)[8]",
     "activity_ko": "티로시나아제 억제 IC50 40.6 μM, 시스 이성질체 36.4 μM(효소 실험)[8]", "source": ref(8)},
    {"name": "Methyl ferulate", "name_ko": "메틸 페룰레이트", "class": "페놀산 에스터", "role": "bioactive", "part": "지상부",
     "content_text": "함량 확인하지 못함(분리 보고)[9]",
     "activity_ko": "사람 암세포주 2종(SK-OV-3, HCT15)에 중등도 세포독성, ED50 약 8.8 μM(시험관 실험)[9]", "source": ref(9)},
    {"name": "Casticin", "name_ko": "카스티신", "class": "폴리메톡시 플라보놀", "role": "bioactive", "part": "줄기·잎",
     "content_text": "함량 확인하지 못함(분리 보고)[10]",
     "activity_ko": "H. scandens 줄기·잎에서 처음 분리된 13종 가운데 하나[10]", "source": ref(10)},
    {"name": "Humulone", "name_ko": "휴물론(추정)", "class": "쓴맛산(아실플로로글루시놀)", "role": "bioactive", "part": "지상부",
     "content_text": "HPLC-qTOF-MS 질량 패턴으로만 추정, 함량 확인하지 못함[3]",
     "activity_ko": "호프 쓴맛산과 같은 m/z 361 이온과 프레닐기 소실 패턴으로 예측됨, 표준품 분리 확인은 아님[3]; 잎 분비샘은 호프형 프레닐 플라보노이드를 만들지 않음[11]", "source": ref(3, 11)},
    {"name": "Lupulone", "name_ko": "루풀론(추정)", "class": "쓴맛산(아실플로로글루시놀)", "role": "bioactive", "part": "지상부",
     "content_text": "HPLC-qTOF-MS 질량 패턴으로만 추정, 함량 확인하지 못함[3]",
     "activity_ko": "분자량 414와 프레닐기 소실 패턴으로 예측됨[3]", "source": ref(3)},
]

EMPTY = {k: "" for k in ("instrument", "column", "mobile_phase", "gradient", "flow", "temp", "detection", "injection",
                         "sample_prep", "standard", "linearity", "lod", "loq", "recovery")}

assays = [
    {"role": "literature", "compound": "Luteolin 7-O-glucoside", "compound_ko": "루테올린-7-O-글루코사이드·아피제닌-7-O-글루코사이드",
     "part": "지상부(2014년 강원도 채취), 70% 에탄올 추출물·HP-20 분획",
     "content": "70% 에탄올 추출물 루테올린-7-O-글루코사이드 13.4 μg/mg, 아피제닌-7-O-글루코사이드 6.5 μg/mg; 활성 분획 168.4·62.8 μg/mg[3]",
     "method": "HPLC-qTOF-MS(성분 확인) / HPLC 정량",
     "conditions": {**EMPTY,
         "instrument": "Agilent 1260 HPLC(이원 펌프·탈기기·자동시료주입기·칼럼 항온조) + Agilent 6530 qTOF-MS(ESI)",
         "mobile_phase": "A: 0.1% 포름산 함유 아세토니트릴, B: 0.1% 포름산 함유 물",
         "gradient": "0–3분 10% A, 3–43분 10→90% A, 43–55분 100% A, 55–60분 10% A",
         "flow": "0.3 mL/min",
         "detection": "ESI 음이온 모드; 가스 온도 350 °C, 건조 가스 10 L/min, 프래그멘터 180 V, 분무기 30 psi, 스키머 60 V, 시스 가스 350 °C·12 L/min, 모세관 전압 4000 V, MS/MS 충돌 에너지 10 V",
         "injection": "0.1 mg/mL 시료 10 μL",
         "sample_prep": "지상부 1 kg을 70% 에탄올 6 L로 60 °C 초음파 추출 3회, 농축 건조물(105 g)을 30% 에탄올에 녹여 Diaion HP-20 칼럼으로 분획(90% 에탄올 분획 = HJF)",
         "standard": "같은 시료에서 분리·NMR로 구조 확인한 화합물을 표준품으로 사용",
         "linearity": "루테올린-7-O-글루코사이드 y = 2291.5884x + 85.4579(상관 0.9999), 아피제닌-7-O-글루코사이드 y = 1804.6794x − 0.7846(상관 1)"},
     "rationale": "두 플라본 배당체는 지상부 추출물과 활성 분획의 주성분이어서 함량 지표로 쓰였다[3]. 전문 확인함: 정량에 쓴 HPLC의 칼럼·검출 파장은 본문에 따로 적혀 있지 않아, 위 기기·이동상 조건은 같은 논문의 HPLC-qTOF-MS 성분 확인 조건이다. 검출·정량한계와 회수율은 본문에 없어 비워 둠.",
     "source": [3], "url": PMC.format("PMC6480934"), "source_kind": "paper"},
    {"role": "literature", "compound": "Luteolin 7-O-glucoside", "compound_ko": "루테올로사이드(루테올린-7-O-글루코사이드)·코스모신(아피제닌-7-O-글루코사이드)",
     "part": "약재 Humulus scandens 16배치(부위는 초록에 명시되지 않음)",
     "content": "루테올로사이드 0.015–0.651%(평균 0.148%), 코스모신 0.003–0.118%(평균 0.036%)[4]",
     "method": "HPLC-UV",
     "conditions": {**EMPTY,
         "mobile_phase": "아세토니트릴 – 0.2% 인산 용액",
         "gradient": "기울기 용리(세부 프로그램은 초록에 없음)",
         "flow": "1.0 mL/min",
         "detection": "UV 350 nm",
         "linearity": "루테올로사이드 0.011–0.364 g/L(r = 1.0000), 코스모신 0.003–0.096 g/L(r = 1.0000)",
         "recovery": "평균 100.5%(루테올로사이드), 98.5%(코스모신)"},
     "rationale": "중국 약재 품질 기준안에서 확인·정량 지표로 정한 두 성분이다[4]. 전문 확인 못함 — 초록에 나온 조건만 옮겼고 칼럼·온도·주입량은 비워 둠.",
     "source": [4], "url": PM.format("25751951"), "source_kind": "paper"},
    {"role": "literature", "compound": "Polyphenols", "compound_ko": "폴리페놀(26종 구조 확인, 총량)",
     "part": "국내산 잎·줄기·뿌리 에틸아세테이트 추출물",
     "content": "총 폴리페놀 잎 3089.9 ± 6.4 mg/kg, 줄기 1313.9 ± 6.4 mg/kg, 뿌리 655.2 ± 2.7 mg/kg(생시료 기준)[5]",
     "method": "LC-ESI-MS/MS",
     "conditions": {**EMPTY,
         "linearity": "결정계수 ≥ 0.9812",
         "lod": "0.017–0.573 mg/L",
         "loq": "0.056–1.834 mg/L",
         "recovery": "50 mg/L에서 71.4–99.7%(RSD 1.5–7.3%), 100 mg/L에서 75.1–105.1%(RSD 0.8–4.1%)"},
     "rationale": "식품원료로 쓰는 잎의 폴리페놀이 줄기·뿌리보다 많아 부위 비교 지표로 쓰였다[5]. 전문 확인 못함 — 칼럼·이동상·질량 조건은 초록에 없어 비워 둠.",
     "source": [5], "url": PM.format("29240230"), "source_kind": "paper"},
]

d = {
    "slug": "humulus-japonicus",
    "name_ko": "한삼덩굴",
    "name_en": "Japanese hop",
    "scientific_name": "Humulus japonicus Siebold & Zucc.",
    "aliases": ["Humulus scandens", "Japanese hop", "한삼덩굴잎", "한삼덩굴순", "한삼덩굴추출분말"],
    "sections": [{"key": k, "title": t, "body": b} for k, t, b in sections],
    "compounds": compounds,
    "markers": [],
    "assays": assays,
    "nutrients": [],
    "production": [],
    "world": [],
    "gi": [],
    "orgs": [],
    "sources": [{"n": n, "title": t, "url": u, "publisher": p, "accessed": a} for n, t, u, p, a in sources],
}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for k, t, b in sections:
    print(k, len(b))
