import json, csv
from pathlib import Path
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
ACC = "2026-11-02"
def pm(n, pmid, title, pub, pmc=None, note="초록 확인"):
    url = f"https://pmc.ncbi.nlm.nih.gov/articles/{pmc}/" if pmc else f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
    return {"n": n, "title": f"{title} (PMID {pmid}{', ' + pmc if pmc else ''}; {note})", "url": url, "publisher": pub, "accessed": ACC}
I1020 = "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020"
sources = [
 {"n": 1, "title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 독활 4개 원료명 행(학명 'Aralia cordata / Aralia continentalis Kitagawa', 다른 이름 땅두릅·땃두릅, 영문명 Manchurian angelica). 독활잎·독활잎분말은 사용가능, 조건 '사용가능부위 : 잎'; 독활뿌리·독활뿌리추출액은 제한적사용, 조건 '제한적사용가능부위 : 뿌리※(독활)'. 로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json", "url": I1020, "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
 {"n": 2, "title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 관련 행: Du Huo(Angelica pubescens, 다른 이름 '猪独活, 獨活(독활)') 사용불가; 땃두릅나무(Oplopanax elatus Nakai) 전체 사용불가, 땃두릅나무줄기추출물 사용가능(액상차·고형차 100 g당 60 mg 이하), 땃두릅 나무 줄기 열수추출물 분말 한시적인정(제한적사용); 두릅·두릅순·두릅잎 등(Aralia elata / Aralia canescens) 사용가능 '사용가능부위 : 순, 잎'; 같은 속 라케모사두릅(A. racemosa, 잎·열매)·Sakhalin spikenard잎(A. schmidtii)·Manchurian angelica tree잎(A. mandschurica)·애기두릅나무잎(A. elata var. canescens) 사용가능, Bristly sarsaparilla뿌리(A. hispida) 제한적사용 '제한적사용가능부위 : 뿌리'. 로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json", "url": I1020, "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
 {"n": 3, "title": "농림축산식품부 「특용작물 생산실적」(1995–2024) — 약용작물 '독활(땅두릅)' 연도별 재배면적·수확면적·10a당 수량·생산량(경작지), 1996–2024. 로컬 파싱본 docs/stats/special_crops_annual.csv", "url": "https://www.mafra.go.kr", "publisher": "농림축산식품부", "accessed": "2026-10-13"},
 {"n": 4, "title": "농림축산식품부 「2024 특용작물 생산실적」 — 독활(땅두릅) 경작지·임야 품목별 농가 수·면적·생산량과 시도별 표. 로컬 파싱본 docs/stats/special_crops_2024.csv, regional_crops.csv", "url": "https://www.mafra.go.kr", "publisher": "농림축산식품부", "accessed": "2026-10-13"},
 pm(5, "39124933", "A Comprehensive Review of Traditional Medicinal Uses, Geographical Distribution, Botanical Characterization, Phytochemistry, and Pharmacology of Aralia continentalis Kitag. Molecules 2024;29(15):3529, doi:10.3390/molecules29153529", "MDPI / PubMed Central", "PMC11313775", "전문 확인"),
 pm(6, "36754338", "Phylogenomics of Aralia sect. Aralia (Araliaceae): Signals of hybridization and insights into its species delimitations and intercontinental biogeography. Mol Phylogenet Evol 2023;181:107727, doi:10.1016/j.ympev.2023.107727", "Elsevier / PubMed"),
 pm(7, "12624934", "[Genetic relationships among Far Eastern species of the family Araliaceae inferred by RAPD analysis]. Genetika 2003;39(1):57-63 (러시아어, 영문 초록)", "PubMed"),
 pm(8, "26938512", "Rapid Authentication of the Herbal Medicine Plant Species Aralia continentalis Kitag. and Angelica biserrata C.Q. Yuan and R.H. Shan Using ITS2 Sequences and Multiplex-SCAR Markers. Molecules 2016;21(3):270, doi:10.3390/molecules21030270", "MDPI / PubMed Central", "PMC6273786", "전문 확인(전문 텍스트에서 학명 일부가 빠져 초록과 대조)"),
 pm(9, "37869529", "Development of real-time PCR-based markers for differentiation of Oplopanax elatus and Aralia cordata in commercial food products. Food Sci Biotechnol 2023;32(14):2153-2161, doi:10.1007/s10068-023-01313-1 (초록 확인; PubMed 메타데이터에 학명이 빠져 있어 두 종 이름은 WebSearch 요약으로만 확인)", "Springer / PubMed"),
 pm(10, "7718129", "[Pharmacognostical identification and investigation of commercial product of traditional Chinese drug jiuyanduhuo]. Zhongguo Zhong Yao Za Zhi 1994;19(12):707-9 (중국어, 영문 초록)", "PubMed"),
 pm(11, "41936451", "Diterpenes in Aralia cordata Rhizomes Suppress the Expression of Proinflammatory and Extracellular Matrix Degradation-Related Genes in ATDC5 Cells. Biol Pharm Bull 2026;49(4):636-644, doi:10.1248/bpb.b25-00741", "PubMed"),
 pm(12, "30754590", "First Report of Alternaria panax Causing Leaf Spot of Aralia cordata in Japan. Plant Dis 2009;93(11):1215, doi:10.1094/PDIS-93-11-1215B", "APS / PubMed"),
 pm(13, "31690022", "Continentalic Acid Rather Than Kaurenoic Acid Is Responsible for the Anti-Arthritic Activity of Manchurian Spikenard In Vitro and In Vivo. Int J Mol Sci 2019;20(21):5488, doi:10.3390/ijms20215488", "MDPI / PubMed Central", "PMC6861925", "전문 확인"),
 pm(14, "38140279", "Aralia continentalis Root Enhances Non-Rapid Eye Movement Sleep by Activating GABA-A Receptors. Nutrients 2023;15(24):5020, doi:10.3390/nu15245020 (제목의 학명은 메타데이터에서 빠져 있음)", "MDPI / PubMed Central", "PMC10745546", "전문 확인"),
 pm(15, "30513750", "Pharmacokinetic Profile of Kaurenoic Acid after Oral Administration of Araliae Continentalis Radix Extract Powder to Humans. Pharmaceutics 2018;10(4):253, doi:10.3390/pharmaceutics10040253", "MDPI / PubMed Central", "PMC6321364", "전문 확인"),
 pm(16, "35807656", "Aralia cordata Thunb. as a Source of Bioactive Compounds: Phytochemical Composition and Antioxidant Activity. Plants (Basel) 2022;11(13):1704, doi:10.3390/plants11131704", "MDPI / PubMed Central", "PMC9269114", "전문 확인"),
 pm(17, "28306202", "Ultra-performance convergence chromatography for the quantitative determination of bioactive compounds in Aralia continentalis Kitagawa as quality control markers. J Sep Sci 2017;40(9):2071-2079, doi:10.1002/jssc.201601261", "Wiley / PubMed"),
 pm(18, "32448886", "Optimization of Extraction Conditions of Continentalic and Kaurenoic Acids from Aralia continentalis by HPLC/UV and Their Validation. J Chromatogr Sci 2020;58(7):672-677, doi:10.1093/chromsci/bmaa019", "Oxford / PubMed"),
 pm(19, "24293061", "Optimization of ultrasonic-assisted extraction of continentalic acid from the root of Aralia continentalis by using the response surface methodology. Arch Pharm Res 2014;37(11):1437-44, doi:10.1007/s12272-013-0291-3", "Springer / PubMed"),
 pm(20, "2054865", "Analgesic principles from Aralia cordata Thunb. Chem Pharm Bull 1991;39(2):405-7, doi:10.1248/cpb.39.405", "PubMed"),
 pm(21, "15742804", "Inhibitory constituents against cyclooxygenases from Aralia cordata Thunb. Arch Pharm Res 2005;28(1):28-33, doi:10.1007/BF02975131", "Springer / PubMed"),
 pm(22, "16903073", "Cytotoxic and COX-2 inhibitory constituents from the aerial parts of Aralia cordata. Arch Pharm Res 2006;29(7):548-55, doi:10.1007/BF02969263", "Springer / PubMed"),
 pm(23, "19763045", "Aralia cordata protects against amyloid beta protein (25-35)-induced neurotoxicity in cultured neurons and has antidementia activities in mice. J Pharmacol Sci 2009;111(1):22-32, doi:10.1254/jphs.08271fp", "PubMed"),
 pm(24, "20717878", "Inhibitory effect of human breast cancer cell proliferation via p21-mediated G1 cell cycle arrest by araliadiol isolated from Aralia cordata Thunb. Planta Med 2011;77(2):164-8, doi:10.1055/s-0030-1250177", "Thieme / PubMed"),
 pm(25, "16619343", "Continentalic acid from Aralia continentalis shows activity against methicillin-resistant Staphylococcus aureus. Phytother Res 2006;20(6):511-4, doi:10.1002/ptr.1894", "Wiley / PubMed"),
 pm(26, "24283275", "Aralia cordata inhibits triacylglycerol biosynthesis in HepG2 cells. J Med Food 2013;16(12):1108-14, doi:10.1089/jmf.2012.2636", "PubMed"),
 pm(27, "18984026", "Protective effect of the Aralia continentalis root extract against carbon tetrachloride-induced hepatotoxicity in mice. Food Chem Toxicol 2009;47(1):75-81, doi:10.1016/j.fct.2008.10.011", "Elsevier / PubMed"),
 pm(28, "37175264", "GC-MS/MS Method for Determination of Polycyclic Aromatic Hydrocarbons in Herbal Medicines. Molecules 2023;28(9):3853, doi:10.3390/molecules28093853", "MDPI / PubMed"),
 pm(29, "20162037", "Genetic analysis of Aralia cordata Thunb by RAPD. Afr J Tradit Complement Altern Med 2008;6(1):17-22", "PubMed"),
 pm(30, "28701020", "The Identification of Araliaceae Species by ITS2 Genetic Barcoding and Pollen Morphology. Planta Med 2018;84(1):42-48, doi:10.1055/s-0043-114425", "Thieme / PubMed"),
 pm(31, "41463523", "Shifts in Dissolved Organic Matter and Microbial Communities Under Continuous Cropping of Aralia continentalis Kitag.: A Comparative Study of 2-, 6-, and 12-Year Durations. Biology (Basel) 2025;14(12):1750, doi:10.3390/biology14121750", "MDPI / PubMed"),
 pm(32, "41300412", "Organic Mulching Enhances Soil Health and Fungal Diversity to Promote Growth of Aralia continentalis Kitag. Biology (Basel) 2025;14(11):1624, doi:10.3390/biology14111624", "MDPI / PubMed"),
 pm(33, "26989992", "A hot water extract of Aralia cordata activates bone marrow-derived macrophages via a myeloid differentiation protein 88-dependent pathway and protects mice from bacterial infection. Microbiol Immunol 2016;60(5):343-55, doi:10.1111/1348-0421.12376", "Wiley / PubMed"),
 pm(34, "19898803", "Cholinesterase and BACE1 inhibitory diterpenoids from Aralia cordata. Arch Pharm Res 2009, doi:10.1007/s12272-009-2009-0", "Springer / PubMed"),
]

S = {}
S["overview"] = ("한눈에 보기",
"독활(Aralia cordata)은 두릅나무과(Araliaceae) 두릅나무속의 여러해살이풀로, 봄에는 산나물로 먹고 뿌리는 오래전부터 민간·전통 의약에 써 왔다[5]. 식약처 「식품원료 목록」에는 학명이 'Aralia cordata / Aralia continentalis Kitagawa'로 함께 적혀 있고, 다른 이름은 땅두릅·땃두릅, 영문명은 Manchurian angelica다[1].\n\n"
"식품원료로서 이 종은 부위에 따라 지위가 다르다[1]. 독활잎·독활잎분말은 '사용가능부위 : 잎' 조건의 사용가능 원료이고, 독활뿌리·독활뿌리추출액은 '제한적사용가능부위 : 뿌리※(독활)' 조건의 제한적사용 원료다[1]. 목록의 독활 행 4개에는 어린순(순)을 따로 적은 원료가 없다[1]. 같은 목록에서 중국 약재명 Du Huo(Angelica pubescens, 다른 이름 獨活(독활))는 사용불가로 따로 올라 있어, 이름이 같아도 다른 원료다[2].\n\n"
"성분 연구의 중심은 뿌리의 디테르펜산인 콘티넨탈산(continentalic acid)과 카우레노산(kaurenoic acid)이다[13, 14, 15]. 효과 보고는 대부분 세포·동물 실험이고, 사람 연구로는 건강한 남성 10명에게 독활 추출물 가루를 한 번 먹여 카우레노산의 혈중 농도를 잰 약동학 시험만 확인했다[15].")
S["history"] = ("이용의 역사",
"독활은 한국어로 Dokwhal, 중국어로 Changbaisongmu라 불리며 오래전부터 전통 의약에 쓰였다[5]. 리뷰에 따르면 뿌리와 뿌리껍질을 가을 이후 캐어 말려 쓰고, 성질은 따뜻하며 맛은 맵고 쓰다고 기술된다[5]. 풍한습으로 인한 관절통, 허리·다리의 류머티즘성 통증, 요통, 넘어지거나 삔 상처, 두통·치통 등에 썼고, 내복할 때는 3–10 g을 물에 달이거나 술에 담가 썼다[5]. 한국 전통 처방 인삼패독산에도 들어간다[5].\n\n"
"일본에서는 Aralia cordata를 udo라 부르는 전통 채소로 기르며[12], 뿌리줄기는 Dokukatsu라는 생약으로 골관절염 관련 관절통에 쓰는 독활탕(Dokkatsuto) 등 한방 처방에 들어간다[11]. 중국 약재 구안독활(Jiuyanduhuo)의 주된 기원도 A. cordata로 조사되었다[10].\n\n"
"'독활'이라는 약재명은 나라마다 기원 식물이 다르다[8]. 대한민국약전은 Aralia continentalis의 말린 뿌리(Araliae Continentalis Radix)만 독활로 싣고, 중국약전은 산형과 Angelica pubescens Maxim. f. biserrata Shan et Yuan(= Angelica biserrata)의 뿌리(Angelicae Pubescentis Radix)를 독활(Du-Huo)로 싣는다[8]. 중국산 수입 때문에 한국에서는 두 약재가 모두 독활로 유통되어 왔다[8].")
S["biology"] = ("식물학적 특징",
"리뷰에 정리된 형태(A. continentalis 기준)는 다음과 같다[5]. 땅속에 굵은 덩이 모양 뿌리줄기가 있고, 땅위줄기는 1 m까지 자라며 위쪽에 회색 잔털이 있다[5]. 잎은 2–3회 깃꼴겹잎으로 잎자루가 11.5–24.5 cm이고, 깃 조각마다 막질의 작은잎이 3–7장 달린다[5]. 원뿔꽃차례는 길이 55 cm까지 자라고, 지름 1.5–2 cm의 산형꽃차례에 꽃잎 5장·수술 5개·5실 씨방을 가진 작은 꽃이 많이 핀다[5]. 열매는 지름 약 3 mm의 자흑색으로 다섯 능선이 있고, 꽃은 7–8월, 열매는 8–9월에 맺는다[5].\n\n"
"분포는 중국 지린·랴오닝·헤이룽장·허베이·쓰촨 등과 남북한·러시아이며, 해발 800–3200 m의 숲속과 풀밭 비탈에서 자란다고 기술된다[5]. 리투아니아에서 재배한 A. cordata Thunb.의 부위별 분석에서 총페놀은 잎의 70% 에탄올 추출물이 2328.31 mg GAE/100 g DW로 가장 높았고, 안토시아닌은 장과(78.54 mg/100 g DW)에, 엽록소(7.45 mg/g DW)는 잎에 가장 많았다[16].")
S["related_species"] = ("근연종과 시료 종 확인",
"Aralia cordata와 A. continentalis의 관계는 분류 견해가 갈린다[1, 5, 6, 7]. 식약처 목록은 두 학명을 한 원료로 묶고[1], A. continentalis 리뷰는 이를 Aralia cordata var. continentalis (Kitag.) Y. C. Zhu와 같은 것으로 소개한다[5]. 반면 극동 두릅나무과 RAPD 분석은 둘을 다른 종으로 보았고[7], Aralia절 계통유전체 연구는 A. cordata를 일본·대만·울릉도·중국 중부·서남부·남부에, A. continentalis를 중국 동북부·러시아 동부·한반도 본토에 분포하는 종으로 좁혀 정의했다[6]. 그래서 한국 연구는 독활 뿌리를 대개 A. continentalis(Manchurian spikenard)로 적고 일본의 A. cordata(Japanese spikenard)와 구분하며[13], 이 문서도 논문마다 원문 학명을 그대로 적는다[13, 16].\n\n"
"같은 속의 두릅(A. elata)은 '사용가능부위 : 순, 잎'의 별도 원료이고, 라케모사두릅(A. racemosa)·A. schmidtii·A. mandschurica·애기두릅나무는 잎(라케모사두릅은 열매도) 사용가능, A. hispida 뿌리는 제한적사용이다[2]. 독활의 다른 이름 '땃두릅'과 비슷한 땃두릅나무(Oplopanax elatus)는 전체가 사용불가이고 줄기추출물만 조건부로 쓸 수 있으며, 두 식물이 함께 '두릅'으로 불려 식품에서 혼동될 수 있다[2, 9].")
S["cultivation"] = ("재배와 생산",
"농림축산식품부 「특용작물 생산실적」에서 독활(땅두릅) 경작지 재배면적은 1996년 339 ha에서 2007년 507 ha, 2009년 531 ha로 늘었다가 2011–2023년에는 250–309 ha였다[3]. 생산량은 2002년 3,532톤이 가장 많았고 2019–2023년에는 1,246–1,304톤이었다[3]. 2024년에는 경작지 161 ha(수확 153 ha)에서 527톤(10a당 343 kg)이 나와 2023년(283 ha, 1,304톤)보다 크게 줄었다[3]. 2024년 경작지 재배 농가는 1,370호였고, 이와 별도로 임야 재배가 108호·26 ha에서 93톤이었다[4]. 시도별 경작지 생산량은 경남 222톤, 전남 113톤, 충남 71톤, 전북 68톤 순이었다[4].\n\n"
"중국 동북부의 A. continentalis 재배지에서는 2·6·12년 이어짓기가 길어질수록 토양의 유효 질소·인·칼륨이 줄었다[31]. 5년 포장시험에서는 썩힌 낙엽 멀칭이 관행 시비보다 26.3%, 무처리보다 34.5% 많은 생체량을 냈다[32]. 일본에서는 소나무 아래에서 기르던 udo의 잎에 Alternaria panax에 의한 점무늬병이 40% 넘는 포기에 생긴 사례가 보고되었다[12]. 국내 재배 방식(연백 재배 등)에 대한 공공기관 자료는 확인하지 못함.")
S["processing"] = ("가공과 제품",
"식품원료 목록에 오른 독활 가공 원료는 독활잎분말(잎)과 독활뿌리추출액(뿌리)이다[1]. 약동학 연구에 쓰인 독활 추출물 가루는 대한민국약전 기준에 따라 뿌리 1 kg을 80–100 °C 물 10 L로 2–3시간 추출해 걸러 감압 건조한 것으로, 식약처 허가를 받은 시판 제품이며 통증·경련 환자에게 보통 0.72–1.09 g씩 하루 세 번 쓴다고 소개되었다[15].\n\n"
"추출 용매에 따라 지표성분 함량이 달라진다[13, 18, 19]. 50% 에탄올 추출물에서 콘티넨탈산·카우레노산이 가장 많았고, 100% 에탄올 추출물은 세포 독성이 컸다[13]. 다른 연구는 분쇄하지 않은 뿌리 3.75 g을 50% 에탄올 300 mL로 5시간 한 번 추출할 때 두 성분이 가장 많이 나왔다고 보고했다[18]. 초음파 추출에서는 100% 에탄올·33 °C·28분 조건에서 콘티넨탈산 추출률이 1.0138%로 가장 높았다[19]. 70% 에탄올로 80 °C에서 3시간 환류 추출해 동결건조한 추출물의 수율은 19.27%였다[14]. 추출물 형태별 동물·세포 보고로는, 뿌리 추출물이 생쥐 사염화탄소 간 손상 모델에서 혈청 ALT·AST 상승을 막았고[27], 열수 추출물이 대식세포를 활성화하고 생쥐의 리스테리아균 제거를 도왔으며[33], 지상부 에탄올 추출물에서는 3β,5α-dihydroxy-6β-methoxyergosta-7,22-diene 등 세포 독성 성분(암세포 IC50 11.7–15.1 μM)이 분리되었다[22]. 식약처 「식품 등의 생산실적」 건강기능식품 품목 자료에서 독활을 원료로 한 품목은 확인하지 못함.")
S["genetics"] = ("유전체와 종 판별",
"ITS2 염기서열을 바탕으로 독활(A. continentalis)과 Angelica biserrata, 그리고 같은 약재로 유통되는 Levisticum officinale·Heracleum moellendorffii 4종을 한 번에 가르는 종 특이 다중 SCAR 표지가 개발되었다[8]. 이 방법으로 한국·중국 시판 약재 20점을 조사한 결과 7점이 진품이 아니었고, 그중 6점은 다른 한 종의 뿌리만으로 되어 있었다[8].\n\n"
"식품 쪽에서는 함께 '두릅'으로 불리는 땃두릅나무(Oplopanax elatus)와 A. cordata를 가르는 실시간 PCR 표지 6쌍이 개발되었다[9]. 표지들은 상관계수 0.99 이상, 기울기 −3.33~−3.56을 보였고, 표적이 아닌 식물 14종과 시판 제품 10점으로 특이성과 실용성을 확인했다[9]. 러시아 연해주의 야생 두릅나무과 6종은 ITS2 바코드로 모두 종 구분이 되었으나, 같은 종 안의 산지 구분은 되지 않았다[30]. 중국 8개 성의 A. cordata를 RAPD 프라이머 12개로 본 연구에서는 161개 좌위가 검출되었고 다형성 비율이 34.78–63.35%였다[29]. 이 종의 전장 유전체 해독 자료는 확인하지 못함.")
S["safety"] = ("안전성과 사용 조건",
"식약처 「식품원료 목록」에서 독활 뿌리(독활뿌리·독활뿌리추출액)는 '제한적사용', 조건은 '제한적사용가능부위 : 뿌리※(독활)'이고, 잎(독활잎·독활잎분말)은 '사용가능부위 : 잎'의 사용가능 원료다[1]. 제한적사용 원료에 붙는 식품공전상 배합 한도 등 구체적 사용 조건은 원문을 열지 못해 확인하지 못함. 약재명이 같은 Du Huo(Angelica pubescens)는 사용불가이므로 '독활'이라는 이름만으로 원료를 판단하면 안 된다[2, 8]. 전통 의약 문헌을 정리한 리뷰는 음허·내열이 있거나 풍열 감기인 사람에게는 권하지 않는다고 적었다[5].\n\n"
"독성 자료는 많지 않다[13, 15]. 독활 뿌리 100% 에탄올 추출물은 생쥐 대식세포(RAW264.7)에서 100 μg/mL에서 세포 증식을 크게 억제했고, 50% 에탄올 추출물은 사람 연골세포에서 500 μg/mL 이상에서 독성을 보였다[13]. 약동학 논문은 카우레노산에 대해 다른 연구의 세포·배아 독성과 유전 독성 보고를 들어 조심해 써야 한다고 적었다[15]. 건강한 한국 남성 10명이 추출물 가루 1.0054 g(카우레노산 1.147 mg)을 한 번 먹었을 때 개인별 최고 혈중 농도는 10.24–34.29 μg/L였다[15]. 한약재 51종의 다환방향족탄화수소 8종 조사에서 독활(Araliae Continentalis Radix)의 평균 함량은 0.9 μg/kg으로 가장 낮았다[28]. 알레르기 등 식품 안전에 관한 공공기관 정보는 확인하지 못함.")

sections = [{"key": k, "title": v[0], "body": v[1]} for k, v in S.items()]

compounds = [
 {"name": "Continentalic acid", "name_ko": "콘티넨탈산(ent-피마라-8(14),15-디엔-19-오산)", "class": "피마란형 디테르펜산", "role": "marker", "part": "뿌리",
  "content_text": "70% 에탄올 뿌리 추출물 기준 28.9 ± 0.8 mg/g[14]; 50% 에탄올 추출물 100 μg/mL 속 1.90 μg/mL[13]; 초음파 추출 최대 추출률 1.0138%[19]",
  "activity_ko": "사람 골관절염 연골세포에서 IL-1β 유도 IL-6·IL-8·MMP-13·PGE2 억제, 쥐 골관절염 모델 연골 보호(세포·동물)[13]; 황색포도알균(MRSA 포함) MIC 약 8–16 μg/mL(시험관)[25]; 같은 화합물(ent-pimara-8(14),15-dien-19-oic acid)이 GPAT1 IC50 60.5 μM(세포)[26]", "source": [13, 14, 19, 25, 26]},
 {"name": "Kaurenoic acid", "name_ko": "카우레노산(ent-카우르-16-엔-19-오산)", "class": "카우란형 디테르펜산", "role": "marker", "part": "뿌리",
  "content_text": "70% 에탄올 뿌리 추출물 기준 18.6 ± 0.8 mg/g[14]; 열수 추출물 가루 기준 1.1408 ± 0.008 mg/g[15]; 50% 에탄올 추출물 100 μg/mL 속 0.07 μg/mL[13]",
  "activity_ko": "생쥐 경구 300 mg/kg에서 진통 효과(동물)[20]; 사람 단회 복용 약동학: 2구획 모델, CL/F 23.89 L/h[15]", "source": [13, 14, 15, 20]},
 {"name": "Pimaric acid", "name_ko": "피마르산", "class": "디테르펜산", "role": "bioactive", "part": "뿌리·뿌리줄기", "content_text": "함량 수치 확인하지 못함(분리 보고)[21, 11]",
  "activity_ko": "일본산 뿌리줄기 아세트산에틸 분획에서 피마라디엔산·카우레노산과 함께 확인(세포)[11]", "source": [11, 21]},
 {"name": "17-Hydroxy-ent-kaur-15-en-19-oic acid", "name_ko": "17-하이드록시-ent-카우르-15-엔-19-오산", "class": "카우란형 디테르펜산", "role": "bioactive", "part": "뿌리", "content_text": "함량 수치 확인하지 못함(분리 보고)[21, 34]",
  "activity_ko": "화합물 9–11의 BACE1 억제 IC50 18.58–24.10 μM(시험관)[34]", "source": [21, 34]},
 {"name": "Falcarindiol", "name_ko": "팔카린디올", "class": "폴리아세틸렌", "role": "bioactive", "part": "뿌리", "content_text": "함량 수치 확인하지 못함(분리 보고)[21]",
  "activity_ko": "COX-1 의존 PGE2 생성 억제 IC50 170 μM; 같은 분획의 dehydrofalcarindiol-8-acetate는 11.7 μM(시험관)[21]", "source": [21]},
 {"name": "Araliadiol", "name_ko": "아랄리아디올", "class": "폴리아세틸렌", "role": "bioactive", "part": "잎", "content_text": "함량 수치 확인하지 못함(잎에서 새로 분리)[24]",
  "activity_ko": "사람 유방암 세포 MCF-7 증식 억제 IC50 6.41 μg/mL, G1기 정지(세포)[24]", "source": [24]},
 {"name": "Oleanolic acid", "name_ko": "올레아놀산", "class": "트리테르펜", "role": "bioactive", "part": "지상부", "content_text": "함량 수치 확인하지 못함(지상부 에탄올 추출물에서 분리)[23]",
  "activity_ko": "배양 신경세포에서 아밀로이드 베타 유도 세포 사멸·칼슘 상승·활성산소 생성 억제(세포)[23]", "source": [23]},
 {"name": "Stigmasterol", "name_ko": "스티그마스테롤", "class": "식물스테롤", "role": "bioactive", "part": "뿌리", "content_text": "함량 수치 확인하지 못함(분리 보고)[21]",
  "activity_ko": "충치균(S. mutans)의 성장·산 생성·부착 억제 보고를 리뷰가 소개(시험관)[5]", "source": [5, 21]},
 {"name": "Lutein", "name_ko": "루테인", "class": "카로티노이드", "role": "nutrient", "part": "잎·꽃차례·장과·씨",
  "content_text": "잎 0.291, 꽃차례 0.271, 장과 0.012, 씨 0.011 mg/g DW(리투아니아 재배 A. cordata)[16]", "activity_ko": "잎·꽃차례·줄기의 주된 카로티노이드[16]", "source": [16]},
 {"name": "Anthocyanins", "name_ko": "안토시아닌(총량, 시아니딘-3-글루코사이드 당량)", "class": "플라보노이드 색소", "role": "bioactive", "part": "줄기·장과",
  "content_text": "18.27–78.54 mg/100 g DW, 장과 78.54 mg/100 g DW로 최고(pH 차이법)[16]", "activity_ko": "항산화 색소; 독활 부위별 항산화능은 잎이 가장 높음(시험관)[16]", "source": [16]},
 {"name": "Ascorbic acid", "name_ko": "아스코르브산(비타민 C)", "class": "비타민", "role": "nutrient", "part": "장과·잎·줄기·뿌리",
  "content_text": "22.3–146.0 mg/100 g DW; 장과 146.0, 줄기·잎·꽃차례 66.4–67.2 mg/100 g DW, 뿌리가 가장 적음[16]", "activity_ko": "영양 성분[16]", "source": [16]},
 {"name": "Total phenolics", "name_ko": "총페놀", "class": "페놀 화합물(총량)", "role": "bioactive", "part": "잎·뿌리 등",
  "content_text": "333.79–2328.31 mg GAE/100 g DW, 잎 70% 에탄올 추출물이 최고[16]; 에탄올 추출물 폴리페놀 12.88 mg/g·플라보노이드 4.54 mg/g(리뷰 인용)[5]",
  "activity_ko": "총페놀 함량과 ABTS·DPPH·FRAP 항산화능이 함께 높음(시험관)[16]", "source": [5, 16]},
]

assays = [
 {"role": "literature", "compound": "Continentalic acid", "compound_ko": "콘티넨탈산(카우레노산 동시 정량)", "part": "뿌리(제천 약재시장 구입 건조 뿌리) 70% 에탄올 추출물(KS-126)",
  "content": "추출물 기준 콘티넨탈산 28.9 ± 0.8 mg/g, 카우레노산 18.6 ± 0.8 mg/g; 머무름 시간 콘티넨탈산 20.48 ± 0.06분, 카우레노산 19.65 ± 0.07분[14]",
  "method": "HPLC-UV",
  "conditions": {"instrument": "JASCO PU-2080 Plus HPLC, UV 검출기 PU-2075 Plus", "column": "YMC Hydrosphere C18(4.6 mm × 250 mm, 3.0 μm)", "mobile_phase": "80%(v/v) 아세토니트릴 수용액", "gradient": "등용리, 25분",
   "flow": "1.0 mL/min", "temp": "30 °C", "detection": "205 nm", "injection": "10 μL",
   "sample_prep": "추출물 15 mg을 DMSO 100 μL에 녹인 뒤 메탄올/클로로포름(1:1)으로 15 mg/2 mL, 메탄올로 200 ppm 희석, 0.45 μm PTFE 여과",
   "standard": "콘티넨탈산·카우레노산 표준품을 DMSO 100 μL에 녹인 뒤 메탄올/클로로포름(1:1) 10 mg/mL 원액, 메탄올로 희석한 작업 용액", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "콘티넨탈산과 카우레노산은 독활 뿌리의 주된 디테르펜으로, 추출물(KS-126)의 성분 확인에 두 성분을 동시 정량했다[14]", "source": [14], "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10745546/", "source_kind": "paper"},
 {"role": "literature", "compound": "Kaurenoic acid", "compound_ko": "카우레노산", "part": "독활(Araliae Continentalis Radix) 열수 추출물 가루",
  "content": "추출물 가루 기준 1.1408 ± 0.008 mg/g(n=3); 1회 복용량 1.0054 g 속 1.147 mg[15]",
  "method": "HPLC-UV(대한민국약전 독활 추출물 가루 함량시험 방법, 2012)",
  "conditions": {"instrument": "", "column": "Waters Nova-Pak C18(3.9 mm × 150 mm, 4 μm)", "mobile_phase": "A: 0.1% 트리플루오로아세트산 수용액, B: 아세토니트릴",
   "gradient": "0–5분 10% B; 5–15분 10→60% B; 15–20분 60% B; 20–25분 60→10% B; 25–30분 10% B", "flow": "1.0 mL/min", "temp": "", "detection": "UV 208 nm", "injection": "20 μL",
   "sample_prep": "추출물 가루 1.0054 g에 100% 에탄올 50 mL를 넣어 30분 초음파 추출·여과, 잔사를 같은 방법으로 한 번 더 추출, 감압 농축 후 100% 에탄올 50 mL로 맞추고 0.45 μm 여과",
   "standard": "카우레노산 표준품(식약처, 순도 > 98.6%) 1.0 mg을 100% 에탄올에 녹여 1000 μg/mL", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "대한민국약전 독활 추출물 가루의 함량시험 대상 성분이 카우레노산이며, 사람 약동학 시험 전 투여 제품의 함량을 이 방법으로 확인했다[15]", "source": [15], "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC6321364/", "source_kind": "paper"},
 {"role": "literature", "compound": "Lutein", "compound_ko": "루테인(제아잔틴·β-카로틴 동시 분석)", "part": "잎(리투아니아 재배 A. cordata Thunb., 동결건조 분말)",
  "content": "잎 0.291 mg/g DW, 꽃차례 0.271 mg/g DW, 장과 0.012 mg/g DW, 씨 0.011 mg/g DW[16]",
  "method": "HPLC-UV/Vis",
  "conditions": {"instrument": "Waters 2695 분리 모듈, 2489 UV–vis 검출기", "column": "YMC 역상 칼럼(5 μm, 4.6 × 250 mm; 탄소 사슬 표기는 전문 텍스트에서 빠짐), 가드 칼럼(5 μm, 10 × 4.0 mm)",
   "mobile_phase": "A: 메틸-tert-부틸에테르, B: 메탄올", "gradient": "99% B로 주입(1분 유지) → 90분에 0% B → 5분 동안 99% B로 복귀(5분 유지)", "flow": "0.6 mL/min", "temp": "22 °C", "detection": "450 nm", "injection": "",
   "sample_prep": "동결건조 분말 500 mg을 80% 아세톤으로 추출, 10,000 rpm·4 °C에서 15분 원심, 0.45 μm PVDF 여과",
   "standard": "루테인·제아잔틴·all-trans-β-카로틴 표준품, 0.01–5.0 mg/100 mL", "linearity": "R² 0.099–0.996(원문 표기 그대로)", "lod": "0.015–0.035 mM", "loq": "0.022–0.067 mM", "recovery": ""},
  "rationale": "식품원료로 사용가능한 잎에서 가장 많은 카로티노이드가 루테인이어서 잎 원료의 지표 후보가 된다[16]", "source": [16], "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9269114/", "source_kind": "paper"},
 {"role": "literature", "compound": "Continentalic acid", "compound_ko": "콘티넨탈산(카우레노산 동시 정량)", "part": "뿌리(한국산 A. continentalis; 중국산 A. pubescens 시료도 함께 분석)",
  "content": "함량 수치는 초록에 없음[17]",
  "method": "UPC²(초고성능 수렴 크로마토그래피)",
  "conditions": {"instrument": "", "column": "Torus 1-aminoanthracene", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "", "injection": "", "sample_prep": "", "standard": "",
   "linearity": "r > 0.996", "lod": "콘티넨탈산 0.068 μg/mL, 카우레노산 0.097 μg/mL", "loq": "콘티넨탈산 0.207 μg/mL, 카우레노산 0.295 μg/mL", "recovery": "99.97–100.26%"},
  "rationale": "두 디테르펜산을 독활 품질관리 지표로 제안하고 8분 안에 분리하는 방법을 ICH 기준으로 검증했다; 전문 확인 못함(초록 값만 옮김)[17]", "source": [17], "url": "https://pubmed.ncbi.nlm.nih.gov/28306202/", "source_kind": "paper"},
]

# production: national series from special_crops_annual.csv
prod = []
for r in csv.DictReader((ROOT / "docs/stats/special_crops_annual.csv").open(encoding="utf-8")):
    if r["item"] != "독활(땅두릅)":
        continue
    y = int(r["year"])
    note = "농식품부 특용작물 생산실적 연도별 표 '독활(땅두릅)' 경작지 값" + (" (임야 26 ha·93톤 별도)" if y == 2024 else "")
    if r["area_ha"]:
        prod.append({"metric": "area_ha", "region": "대한민국", "year": y, "value": float(r["area_ha"]), "unit": "ha", "note": note, "source": [3]})
    if r["prod_t"]:
        prod.append({"metric": "production_t", "region": "대한민국", "year": y, "value": float(r["prod_t"]), "unit": "톤", "note": note, "source": [3]})
prod.append({"metric": "farms", "region": "대한민국", "year": 2024, "value": 1370, "unit": "호", "note": "경작지 재배 농가(임야 재배 108호 별도)", "source": [4]})

d = {"slug": "aralia-cordata", "name_ko": "독활", "name_en": "Udo / Manchurian spikenard (Manchurian angelica)",
     "scientific_name": "Aralia cordata Thunb. (식약처 목록: Aralia cordata / Aralia continentalis Kitagawa)",
     "aliases": ["땅두릅", "땃두릅", "獨活", "Aralia continentalis Kitag.", "Aralia cordata var. continentalis", "Araliae Continentalis Radix", "Manchurian angelica", "Manchurian spikenard", "Japanese spikenard", "udo"],
     "sections": sections, "compounds": compounds, "markers": [], "assays": assays, "nutrients": [], "production": prod, "world": [], "gi": [], "orgs": [], "sources": sources}
out = HERE.parent / "dossier.json"
out.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in sections:
    print(s["key"], len(s["body"]))
print("prod rows", len(prod))
