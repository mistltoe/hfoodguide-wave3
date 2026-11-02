import json
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "dossier.json"
PM = "PubMed"
A = "2026-11-02"


def pm(n, title, pmid, publisher="PubMed"):
    return {"n": n, "title": title, "url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/", "publisher": publisher, "accessed": A}


sources = [
    {"n": 1, "title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 닥나무가지·닥나무잎·닥나무농축액·닥나무추출액 행(Broussonetia kazinoki Sieb.; 다른 이름 저상·딱나무·꾸지닥나무; 영문 Korean paper tree, Small paper mulberry; 사용가능, 사용 조건 '사용가능부위 : 가지, 잎'). 로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json", "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
    {"n": 2, "title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 같은 속·이름이 비슷한 원료 행: 꾸지나무(Broussonetia papyrifera (L.) Ventenat, 전체, 사용불가), 민꾸지나무잎·열매(Broussonetia papyrifera f. lucida (Hatus.) T. B. Lee, 잎·열매, 사용가능), 마주잎꾸지나무잎·열매(Broussonetia papyrifera f. oppositifolia Nakai, 잎·열매, 사용가능), 닥풀잎 등(Hibiscus manihot L. / Broussonetia kaempferi Siebold / Abelmoschus manihot, 다른 이름 딱나무·금화규, 잎, 사용가능), 꾸지뽕나무(Cudrania tricuspidata, 줄기·가지·잎·열매 사용가능), 예덕나무(Mallotus japonicus, 다른 이름 비닥나무·예닥나무, 사용불가), 위생용품(E코드) '닥나무 섬유'(Mulberry fiber, 일회용 기저귀(안감) 성분으로 사용 가능). 로컬 원자료 I1020_20261013.json", "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
    {"n": 3, "title": "농림축산식품부 「특용작물 생산실적」(1995–2024) — '닥나무' 연도별 면적·10a당 수량·생산량(2009–2024) 및 2024 품목별 농가 수(로컬 파싱본 docs/stats/special_crops_annual.csv, special_crops_2024.csv)", "url": "https://www.mafra.go.kr", "publisher": "농림축산식품부", "accessed": "2026-10-12"},
    {"n": 4, "title": "농림축산식품부 「2024 특용작물 생산실적」 시도별·품목별 표 — 닥나무(기타특용작물) 2024년 시도별 농가 수·면적·생산량·10a당 수량(로컬 파싱본 docs/stats/regional_crops.csv, 원 표기 'KOSIS 특용작물생산현황')", "url": "https://www.mafra.go.kr", "publisher": "농림축산식품부", "accessed": "2026-10-13"},
    pm(5, "Plastome phylogenomics of Allaeanthus, Broussonetia and Malaisia (Dorstenieae, Moraceae) and the origin of B. × kazinoki. J Plant Res 2022;135(2):203-220 (PMID 35080694, doi:10.1007/s10265-022-01369-w; 초록 확인)", "35080694", "Springer / PubMed"),
    pm(6, "Molecular recircumscription of Broussonetia (Moraceae) and the identity and taxonomic status of B. kaempferi var. australis. Bot Stud 2017;58(1):11 (PMID 28510194, doi:10.1186/s40529-017-0165-y; 초록 확인)", "28510194", "Springer / PubMed"),
    pm(7, "Molecular identification of Korean Broussonetia × kazinoki using cleaved amplified polymorphic sequence (CAPS) marker. Genetica 2026;154(1) (PMID 42967270, doi:10.1007/s10709-026-00302-6; 초록 확인)", "42967270", "Springer / PubMed"),
    pm(8, "Broussonetia × hanjiana (Moraceae) microsatellite markers for species and ploidy determination developed using next-generation sequencing. Mol Biol Rep 2022;49(9):9089-9094 (PMID 35804215, doi:10.1007/s11033-022-07659-9; 초록 확인)", "35804215", "Springer / PubMed"),
    pm(9, "The complete chloroplast genome sequences of three Broussonetia species and comparative analysis within the Moraceae. PeerJ 2022;10:e14293 (PMID 36340196, doi:10.7717/peerj.14293; 초록 확인)", "36340196", "PeerJ / PubMed"),
    pm(10, "Genetic Diversity on Farm in Japanese Paper Mulberry. Ecol Evol 2025;15(1):e70828 (PMID 39803197, doi:10.1002/ece3.70828; 초록 확인)", "39803197", "Wiley / PubMed"),
    pm(11, "The Genus Broussonetia: An Updated Review of Phytochemistry, Pharmacology and Applications. Molecules 2022;27(16):5344 (PMID 36014582, doi:10.3390/molecules27165344; 초록 확인)", "36014582", "MDPI / PubMed"),
    pm(12, "Genome-Wide Analysis of the UGT Gene Family and Identification of Flavonoids in Broussonetia papyrifera. Molecules 2021;26(11):3449 (PMID 34204142, PMC8200958, doi:10.3390/molecules26113449; PMC 전문 확인 — 받은 전문 텍스트에서 종 학명이 빠져 있어 종별 값 대응은 확인하지 못함)", "34204142", "MDPI / PubMed"),
    pm(13, "The Leaves of Broussonetia kazinoki Siebold Inhibit Atopic Dermatitis-Like Response on Mite Allergen-Treated Nc/Nga Mice. Biomol Ther (Seoul) 2014;22(5):438-44 (PMID 25414775, PMC4201232, doi:10.4062/biomolther.2014.023; PMC 전문 확인)", "25414775", "한국응용약물학회 / PubMed"),
    pm(14, "Studies on the constituents of Broussonetia species. II. Six new pyrrolidine alkaloids, broussonetine A, B, E, F and broussonetinine A and B, as inhibitors of glycosidases from Broussonetia kazinoki Sieb. Chem Pharm Bull 1997;45(4):700-5 (PMID 9145506, doi:10.1248/cpb.45.700; 초록 확인)", "9145506", "일본약학회 / PubMed"),
    pm(15, "Studies on the constituents of Broussonetia species. VII. Four new pyrrolidine alkaloids, broussonetines M, O, P, and Q, as inhibitors of glycosidase, from Broussonetia kazinoki SIEB. Chem Pharm Bull 2000;48(9):1281-5 (PMID 10993225, doi:10.1248/cpb.48.1281; 초록 확인)", "10993225", "일본약학회 / PubMed"),
    pm(16, "Studies on the constituents of Broussonetia species X. Six new alkaloids from Broussonetia kazinoki Sieb. Chem Pharm Bull 2001;49(11):1487-91 (PMID 11724246, doi:10.1248/cpb.49.1487; 초록 확인)", "11724246", "일본약학회 / PubMed"),
    pm(17, "Five new diprenylated flavonols from the leaves of Broussonetia kazinoki. J Nat Prod 2001;64(9):1206-9 (PMID 11575957, doi:10.1021/np010283o; 초록 확인)", "11575957", "ACS / PubMed"),
    pm(18, "Flavans and diphenylpropanes with PTP1B inhibition from Broussonetia kazinoki. Fitoterapia 2018;130:37-42 (PMID 30086333, doi:10.1016/j.fitote.2018.08.001; 초록 확인)", "30086333", "Elsevier / PubMed"),
    pm(19, "Prenylated Polyphenols from Broussonetia kazinoki as Inhibitors of Nitric Oxide Production. Molecules 2018;23(3):639 (PMID 29534539, PMC6017281, doi:10.3390/molecules23030639; PMC 전문 확인)", "29534539", "MDPI / PubMed"),
    pm(20, "Microbial Transformation and Biological Activities of the Prenylated Aromatic Compounds from Broussonetia kazinoki. Molecules 2022;27(6):1879 (PMID 35335241, PMC8954733, doi:10.3390/molecules27061879; PMC 전문 확인)", "35335241", "MDPI / PubMed"),
    pm(21, "Antihyperglycemic effect of stem bark powder from paper mulberry (Broussonetia kazinoki Sieb.) in type 2 diabetic Otsuka Long-Evans Tokushima fatty rats. J Med Food 2008;11(3):499-505 (PMID 18800898, doi:10.1089/jmf.2007.0028; 초록 확인)", "18800898", "Mary Ann Liebert / PubMed"),
    pm(22, "Inhibitory effects of heartwood extracts of Broussonetia kazinoki Sieb on the development of atopic dermatitis in NC/Nga mice. Biosci Biotechnol Biochem 2010;74(9):1802-6 (PMID 20834170, doi:10.1271/bbb.100138; 초록 확인)", "20834170", "Taylor & Francis / PubMed"),
    pm(23, "Tyrosinase inhibitory effects of 1,3-diphenylpropanes from Broussonetia kazinoki. Bioorg Med Chem 2009;17(1):35-41 (PMID 19046886, doi:10.1016/j.bmc.2008.11.022; 초록 확인)", "19046886", "Elsevier / PubMed"),
    pm(24, "New estrogenic compounds isolated from Broussonetia kazinoki. Bioorg Med Chem Lett 2010;20(12):3764-7 (PMID 20493686, doi:10.1016/j.bmcl.2010.04.064; 초록 확인)", "20493686", "Elsevier / PubMed"),
    pm(25, "Marmesin is a novel angiogenesis inhibitor: Regulatory effect and molecular mechanism on endothelial cell fate and angiogenesis. Cancer Lett 2015;369(2):323-30 (PMID 26455771, doi:10.1016/j.canlet.2015.09.021; 초록 확인)", "26455771", "Elsevier / PubMed"),
    pm(26, "Broussoflavonol B from Broussonetia kazinoki Siebold Exerts Anti-Pancreatic Cancer Activity through Downregulating FoxM1. Molecules 2020;25(10):2328 (PMID 32429421, doi:10.3390/molecules25102328; 초록 확인)", "32429421", "MDPI / PubMed"),
    pm(27, "Prevention of Oxidative Stress-Induced Pancreatic Beta Cell Damage by Broussonetia kazinoki Siebold Fruit Extract Via the ERK-Nox4 Pathway. Antioxidants 2020;9(5):406 (PMID 32397640, doi:10.3390/antiox9050406; 초록 확인)", "32397640", "MDPI / PubMed"),
    pm(28, "Therapeutic effects of a liquid bandage prepared with cellulose powders from Styela clava tunics and Broussonetia kazinoki bark: Healing of surgical wounds on the skin of Sprague Dawley rats. Mol Med Rep 2019;19(1):452-460 (PMID 30483728, doi:10.3892/mmr.2018.9668; 초록 확인)", "30483728", "Spandidos / PubMed"),
    pm(29, "Performance of Handmade Ultra-Lightweight Hanji Treated with Wet-Strength Agents for Paper-Based Cultural Heritage Conservation. Materials 2026;19(18):3986 (PMID 42795204, doi:10.3390/ma19183986; 초록 확인)", "42795204", "MDPI / PubMed"),
    pm(30, "New criteria for the characterization of traditional East Asian papers. Environ Sci Pollut Res Int 2017;24(3):2166-2181 (PMID 27059501, doi:10.1007/s11356-016-6545-0; 초록 확인)", "27059501", "Springer / PubMed"),
    pm(31, "Characterization of bionanocomposite films prepared with agar and paper-mulberry pulp nanocellulose. Carbohydr Polym 2014;110:480-8 (PMID 24906782, doi:10.1016/j.carbpol.2014.04.056; 초록 확인)", "24906782", "Elsevier / PubMed"),
    pm(32, "The complete chloroplast genome of an economic and ecological plant, paper mulberry (Broussonetia kazinoki × Broussonetia papyrifera). Mitochondrial DNA B Resour 2017;3(1):28-29 (PMID 33474054, doi:10.1080/23802359.2017.1419088; 초록 확인)", "33474054", "Taylor & Francis / PubMed"),
    pm(33, "Distinct physiological and transcriptional responses of leaves of paper mulberry (Broussonetia kazinoki × B. papyrifera) under different nitrogen supply levels. Tree Physiol 2020;40(5):667-682 (PMID 32211806, doi:10.1093/treephys/tpaa021; 초록 확인)", "32211806", "Oxford / PubMed"),
    pm(34, "First total synthesis of (+)-broussonetine W: glycosidase inhibition of natural product & analogs. Org Biomol Chem 2016;14(22):5157-74 (PMID 27184090, doi:10.1039/c6ob00720a; 초록 확인)", "27184090", "RSC / PubMed"),
    {"n": 35, "title": "닥나무 추출물의 Marmesin 성분 분석법 검증(국내 학술지, 2016; KoreaScience JAKO201608259724440) — 이 환경에서 원문을 열지 못했고 WebSearch 검색 결과 요약으로만 확인함(분석 조건 미확인)", "url": "https://koreascience.kr/article/JAKO201608259724440.page", "publisher": "KoreaScience(한국과학기술정보연구원) — WebSearch 요약", "accessed": A},
    pm(36, "Inhibition of nitric oxide production on LPS-activated macrophages by kazinol B from Broussonetia kazinoki. Fitoterapia 2003;74(4):350-4 (PMID 12781805, doi:10.1016/s0367-326x(03)00062-5; 초록 확인)", "12781805", "Elsevier / PubMed"),
    pm(37, "Inhibitory effects of plant extracts on tyrosinase, L-DOPA oxidation, and melanin synthesis. J Toxicol Environ Health A 2007;70(5):393-407 (PMID 17454565, doi:10.1080/10937400600882871; 초록 확인)", "17454565", "Taylor & Francis / PubMed"),
]

sections = [
    {"key": "overview", "title": "한눈에 보기", "body":
     "닥나무는 뽕나무과(Moraceae) 닥나무속의 잎지는 나무로, 식약처 「식품원료 목록」에는 학명 Broussonetia kazinoki Sieb., 다른 이름 저상·딱나무·꾸지닥나무, 영문명 Korean paper tree·Small paper mulberry로 올라 있다[1]. 한국과 일본에서 닥나무(daknamu)·고조(kōzo)로 불리는 나무는 전통 종이인 한지와 와시의 주원료다[5].\n\n"
     "식품원료로서 닥나무는 '사용가능' 원료이며 사용 조건은 '사용가능부위 : 가지, 잎'이다[1]. 목록에는 닥나무가지(부위 가지)·닥나무잎(부위 잎)·닥나무농축액·닥나무추출액(부위 표기 '-') 4개 원료명이 모두 같은 조건으로 올라 있다[1]. 따라서 식품에 쓸 수 있는 부위는 가지와 잎뿐이며, 뿌리·뿌리껍질·열매·심재는 이 목록의 사용 부위에 들어 있지 않다[1]. 이 종을 원재료로 하는 건강기능식품 고시형 원료는 확인하지 못함.\n\n"
     "닥나무속 세 종에서 지금까지 338개 화합물이 분리되었을 만큼 성분 연구는 많지만, 부위가 섞여 있다[11]. 가지에서는 당분해효소를 억제하는 피롤리딘 알칼로이드(브로우소네틴류)가[14, 15, 16], 잎에서는 프레닐화 플라보놀(브로우소놀 A–E)이[17], 잔가지에서는 PTP1B를 억제하는 플라반과 1,3-디페닐프로판이 분리되었다[18]. 반면 카지놀류 등 많이 연구된 프레닐 폴리페놀은 주로 뿌리껍질에서 얻은 것이고[19, 20], 심재 추출물[22]과 열매 추출물[27] 연구도 있어 식품원료 부위(가지·잎)의 자료로 그대로 옮기면 안 된다."},
    {"key": "history", "title": "이용의 역사", "body":
     "닥나무속 식물은 종이 만드는 기술의 발달에 꼭 필요한 나무였고, 한국과 일본에서는 닥나무가 지금도 한지와 와시의 주원료다[5]. 일본에서는 우량 계통을 꺾꽂이 등 영양번식으로 퍼뜨려 와시 원료로 재배해 왔다[10]. 전통 한지는 닥나무 인피섬유를 식물을 태운 재의 잿물로 삶아 만든 펄프를 손으로 떠서 만들며, 매우 얇은 한지는 종이 문화재 보존 처리용으로도 시험되었다[29]. 고조(닥나무)로 만든 전통 수제 종이는 열분해 기체크로마토그래피로 다른 섬유 식물 종이와 구별할 수 있다고 보고되었다[30].\n\n"
     "한국 전통 의학에서는 닥나무를 화상과 여드름 같은 피부 질환에 써 왔다고 소개된다[13, 20]. 잎·가지·뿌리·열매가 시력 개선과 부종 완화 등에 쓰였다고 정리한 논문도 있다[20]. 닥나무 추출물은 미백 효과로 식약처(당시 식품의약품안전청)에 화장품 미백 원료로 등록되었다고 한 논문이 소개했다(등록 원문은 확인하지 못함)[20]. 식품으로 닥나무 잎·가지를 먹어 온 구체적인 기록과 시기는 확인하지 못함."},
    {"key": "biology", "title": "식물학적 특징과 분류", "body":
     "닥나무는 뽕나무과 닥나무속에 속한다[1]. 최근의 분류 연구는 일본·한국의 고조·닥나무를 Broussonetia monoica와 꾸지나무(B. papyrifera) 사이의 잡종, 곧 B. × kazinoki로 본다[5]. 일본 닥나무속 재검토에서는 B. kaempferi·B. monoica·B. papyrifera 세 종과 잡종 B. × kazinoki가 인정되었다[6]. B. monoica의 암수한그루 성질은 암수딴그루인 B. kaempferi(♀)와 꾸지나무(♂)의 교잡에서 생긴 파생 형질일 가능성이 제시되었다[5].\n\n"
     "국내 각지에서 모은 닥나무속 89개체를 분자표지로 가린 결과 B. monoica 6개체, 꾸지나무 4개체, B. × kazinoki 79개체였고, 현장에서 형태로 동정한 결과와 어긋나 다시 분류한 개체도 있었다[7]. 이 연구는 꽃이 없는 시기에는 형태만으로 잡종과 부모 종을 구별하기 어렵다고 밝혔다[7]. 따라서 식품원료 목록의 학명 표기(B. kazinoki Sieb.)와 논문 속 'B. kazinoki'가 같은 식물 집단을 가리키는지는 논문마다 확인해야 한다[1, 6, 7]. 공식 기관의 형태 기재(잎 모양·꽃차례·개화기)는 이 환경에서 열지 못해 확인하지 못함."},
    {"key": "related_species", "title": "가까운 종과 구별", "body":
     "식약처 목록에서 꾸지나무(Broussonetia papyrifera (L.) Ventenat)는 '전체' 부위가 '사용불가'로 올라 있어, 닥나무(사용가능, 가지·잎)와 지위가 정반대다[1, 2]. 꾸지나무의 품종으로 적힌 민꾸지나무(B. papyrifera f. lucida)와 마주잎꾸지나무(B. papyrifera f. oppositifolia)는 각각 '사용가능부위 : 잎, 열매'로 따로 올라 있다[2]. 쓸 수 있는 부위가 닥나무와 다르므로 자료를 섞으면 안 된다[1, 2].\n\n"
     "이름 혼동도 주의해야 한다. 닥나무의 다른 이름 '딱나무'는 닥풀잎(Hibiscus manihot 등)의 다른 이름으로도 목록에 적혀 있고, 그 학명 칸에는 닥나무속의 Broussonetia kaempferi Siebold가 함께 적혀 있다[2]. 그러나 B. kaempferi는 닥나무속의 독립된 종으로 다뤄지므로[6], 닥풀과 닥나무는 다른 식물이다. 이름이 비슷한 예덕나무(다른 이름 비닥나무·예닥나무)는 다른 과의 식물로 '사용불가'다[2].\n\n"
     "중국 논문의 'hybrid paper mulberry(B. kazinoki × B. papyrifera)'는 중국에서 교배로 만든 사료·생태복원용 잡종으로[12, 32, 33], 한국·일본 재래 닥나무(B. × kazinoki)와 같은 재료로 단정할 근거는 확인하지 못함. 국내 식물 추출물 101종 비교 연구는 B. kazinoki var. humilis(잎·줄기)와 꾸지나무(잎·나무껍질)를 따로 시험했으므로[37], 변종·근연종 표기도 원문대로 구별해 읽어야 한다."},
    {"key": "cultivation", "title": "재배와 원료 수급", "body":
     "농림축산식품부 「특용작물 생산실적」에서 닥나무는 2024년 전국 11농가, 재배면적 2 ha, 생산량 6 t, 10a당 수량 235 kg으로 집계되었다[3, 4]. 2024년 시도별로는 충북이 7농가·2 ha·4 t(10a당 215 kg), 경북이 4농가·1 t(10a당 330 kg)이었고 나머지 시도는 0이었다[4]. 연도별로는 2009년 11 ha·36 t, 2012년 6 ha·148 t이었다가 2014년 이후 2–5 ha, 6–10 t 수준으로 줄었다[3]. 통계표에는 수확한 부위(껍질·가지·잎)가 적혀 있지 않아 식품원료로 쓰인 양인지는 확인하지 못함.\n\n"
     "일본의 와시용 닥나무는 우량 계통을 영양번식으로 퍼뜨려 재배하므로 재배 품종 사이의 유전적 이질성이 크다고 보고되었다[10]. 국내 연구에 쓰인 원료는 전북의 한지 회사가 기증한 생잎[13], 충북 괴산에서 채집한 뿌리껍질[19], 전주의 농장에서 채집한 뿌리껍질[20] 등이었다. 지리적 표시 등록, 생산자 단체, 수출입 통계는 확인하지 못함."},
    {"key": "processing", "title": "가공과 제품", "body":
     "식품원료 목록에는 닥나무농축액·닥나무추출액이 원료명으로 올라 있어 가지·잎을 농축액·추출액 형태로도 쓸 수 있다[1]. 추출 용매나 방법은 목록에 적혀 있지 않다[1]. 한 국내 연구는 바람에 말린 잎 4.5 kg을 70% 에탄올 15 L로 4시간 환류 추출해 추출물 512 g을 얻었고, 이 추출물에 플라보노이드와 탄닌이 많다고 보고했다[13]. 같은 연구진은 닥나무 잎에 알려진 지표성분이 없어 HPLC 성분 프로파일을 확인하지 못했다고 밝혔다[13].\n\n"
     "닥나무의 가장 큰 가공 용도는 인피섬유로 만드는 종이다[5, 29]. 인피 펄프에서 뽑은 나노셀룰로스는 한천 필름의 인장 강도를 높여 생분해 식품 포장재 소재로 시험되었다[31]. 식약처 목록에는 위생용품 원료로 '닥나무 섬유'가 일회용 기저귀 안감 성분으로 사용 가능하다고 따로 올라 있다[2]. 닥나무 추출물은 화장품 미백 원료로도 쓰인다고 소개된다[20]. 식약처 「식품 등의 생산실적」에서 닥나무 원료 제품의 생산 통계는 확인하지 못함."},
    {"key": "genetics", "title": "유전과 분류 연구", "body":
     "닥나무속 엽록체 유전체는 전형적인 네 부분 구조이고, 6개 종의 크기는 160,121–162,594 bp로 매우 보존되어 있었다[5]. 같은 연구는 변이가 큰 ndhF-rpl32 구간을 이용해 B. × kazinoki의 기원을 추적했다[5]. 중국 연구진이 해독한 닥나무속 세 종의 엽록체 유전체는 160,239–160,841 bp였다[9]. 일본 와시용 닥나무 세 계통의 엽록체 유전체는 160,861·160,868·160,878 bp였고, 25개 삽입·결실 변이가 확인되었다[10].\n\n"
     "국내 닥나무속 89개체를 26S rDNA 기반 CAPS 표지(제한효소 BstN1)로 구별한 연구에서 B. × kazinoki 79개체는 2배체 49개체와 3배체 30개체로 이루어져 있었다[7]. 꾸지나무와 닥나무의 중간 형태를 보이는 B. × hanjiana를 위해 미세위성 표지 24개가 개발되었고, 이 표지로 부모 두 종의 유전형과 2배체·3배체를 판별할 수 있었다[8]. 중국 교배 잡종(B. kazinoki × B. papyrifera)의 엽록체 유전체는 160,903 bp로 보고되었다[32]. B. × kazinoki 자체의 전체 핵 유전체 해독 결과와 국내 품종 등록 기록은 확인하지 못함."},
    {"key": "safety", "title": "안전성과 사용 조건", "body":
     "닥나무는 식약처 「식품원료 목록」에서 '사용가능' 원료이며 사용 조건은 '사용가능부위 : 가지, 잎'이므로, 가지와 잎 외의 부위(뿌리·뿌리껍질·심재·열매)는 식품원료로 쓸 근거가 없다[1]. 꾸지나무(B. papyrifera)는 전체가 '사용불가'이므로 꾸지나무를 닥나무로 잘못 쓰지 않도록 원료 동정이 중요하다[2, 7].\n\n"
     "사람에게 먹였을 때의 안전성·독성 자료와 공공기관의 알레르기·잔류 정보는 확인하지 못함. 비만 당뇨 흰쥐에게 줄기껍질 가루를 사료에 5%(50 g/kg) 섞어 8주 먹인 효능 시험에서 혈청 ALT는 오히려 낮아졌으나, 이는 독성 시험이 아니다[21]. 나무껍질 셀룰로스로 만든 액상 밴드를 흰쥐 피부에 바른 시험에서는 간·신장 독성이 관찰되지 않았다[28]. 잎 추출물은 200–1000 μg/mL에서 사람 각질세포(HaCaT)에 세포독성을 보이지 않았다[13].\n\n"
     "가지의 브로우소네틴류는 시험관에서 여러 당분해효소를 억제하고[14, 15], 일부 프레닐 화합물은 세포 실험에서 에스트로겐 수용체 활성을 보였다[24]. 이는 세포·효소 수준 결과이며 사람에서 같은 작용이 있는지는 확인하지 못함."},
]

compounds = [
    {"name": "Broussonetine A", "name_ko": "브로우소네틴 A(브로우소네틴 B·E·F 포함)", "class": "피롤리딘 알칼로이드(이미노당)", "role": "bioactive", "part": "가지", "content_text": "가지에서 분리(함량 확인하지 못함)[14]", "activity_ko": "브로우소네틴 E·F는 α-·β-글루코시다아제, β-갈락토시다아제, β-만노시다아제를 강하게 억제(효소 시험)[14]", "source": [14]},
    {"name": "Broussonetine M", "name_ko": "브로우소네틴 M(O·P·Q 포함)", "class": "피롤리딘 알칼로이드", "role": "bioactive", "part": "가지", "content_text": "가지에서 분리(함량 확인하지 못함)[15]", "activity_ko": "β-글루코시다아제·β-갈락토시다아제·β-만노시다아제 억제(효소 시험)[15]", "source": [15]},
    {"name": "Broussonetine W", "name_ko": "브로우소네틴 W", "class": "피롤리딘 알칼로이드", "role": "bioactive", "part": "가지(미량 성분)", "content_text": "가지에서 미량 성분으로 분리(함량 확인하지 못함)[16]", "activity_ko": "합성한 (+)-브로우소네틴 W가 β-갈락토시다아제 IC50 0.03 μM(효소 시험)[34]", "source": [16, 34]},
    {"name": "Broussonol A", "name_ko": "브로우소놀 A(B–E 포함)", "class": "디프레닐 플라보놀", "role": "bioactive", "part": "잎", "content_text": "잎 에탄올 추출물에서 새 화합물 5종으로 분리(함량 확인하지 못함)[17]", "activity_ko": "여러 암세포주에 대한 세포독성 평가(세포)[17]", "source": [17]},
    {"name": "Luteolin", "name_ko": "루테올린", "class": "플라본", "role": "bioactive", "part": "잎", "content_text": "중국 재배 닥나무속 세 분류군 잎(건조중량) 비교: 교배 잡종 27.4 ± 2.4 μg/g, 나머지 두 종 2.6 ± 0.1·3.4 ± 0.4 μg/g(UPLC-ESI-MS/MS, 루틴 환산 반정량; 어느 값이 B. kazinoki인지는 확인하지 못함)[12]", "activity_ko": "이 연구에서는 항산화 지표(DPPH·FRAP·ABTS)를 추출물 단위로만 비교[12]", "source": [12]},
    {"name": "Chlorogenic acid", "name_ko": "클로로겐산", "class": "페놀산", "role": "nutrient", "part": "잎", "content_text": "닥나무속 잎 19개 성분 중 교배 잡종 잎에서 함량이 가장 높은 성분으로 보고(B. kazinoki 잎 값은 확인하지 못함)[12]", "activity_ko": "확인하지 못함(이 종 대상 시험 없음)[12]", "source": [12]},
    {"name": "Kazinol C", "name_ko": "카지놀 C", "class": "1,3-디페닐프로판(프레닐 폴리페놀)", "role": "bioactive", "part": "뿌리껍질(식품원료 사용 부위 아님); 잔가지에서도 1,3-디페닐프로판류 분리", "content_text": "뿌리껍질 650 g 에탄올 추출 분획에서 110 mg 분리[20]; 뿌리껍질 0.6 kg에서 260 mg 분리[19]", "activity_ko": "대식세포 NO 생성 억제 IC50 10 μM 미만(세포)[19]; 버섯 티로시나아제 억제(효소)[23]", "source": [19, 20, 23]},
    {"name": "Kazinol F", "name_ko": "카지놀 F", "class": "1,3-디페닐프로판", "role": "bioactive", "part": "뿌리껍질(식품원료 사용 부위 아님)", "content_text": "뿌리껍질 주요 성분의 하나로 분리(함량 확인하지 못함)[20]", "activity_ko": "티로시나아제 억제 IC50 2.12 μM(효소)[20]; 디페놀라아제 억제 IC50 1.7 μM(효소)[23]", "source": [20, 23]},
    {"name": "Kazinol U", "name_ko": "카지놀 U", "class": "프레닐 플라반", "role": "bioactive", "part": "뿌리껍질(식품원료 사용 부위 아님)", "content_text": "뿌리껍질 0.6 kg에서 139 mg 분리[19]", "activity_ko": "NO 생성 억제(세포)[19]; 에스트로겐 수용체 결합·전사 활성(세포)[24]", "source": [19, 24]},
    {"name": "Kazinol B", "name_ko": "카지놀 B", "class": "프레닐 플라반", "role": "bioactive", "part": "부위 초록에 없음", "content_text": "에틸아세테이트 분획의 활성 성분으로 확인(함량 확인하지 못함)[36]", "activity_ko": "LPS 자극 대식세포 NO 생성 억제 IC50 21.6 μM(세포)[36]", "source": [36]},
    {"name": "Broussonin A", "name_ko": "브로우소닌 A", "class": "1,3-디페닐프로판", "role": "bioactive", "part": "뿌리껍질(식품원료 사용 부위 아님)", "content_text": "뿌리껍질 0.6 kg에서 17 mg 분리[19]", "activity_ko": "에스트로겐 활성 성분의 하나(세포)[24]", "source": [19, 24]},
    {"name": "Marmesin", "name_ko": "마르메신", "class": "쿠마린", "role": "marker", "part": "추출물(부위 확인하지 못함)", "content_text": "닥나무 추출물의 지표성분으로 HPLC 정량법이 검증되었다고 검색 요약에서 확인(원문·함량 확인하지 못함)[35]", "activity_ko": "VEGF-A 자극 혈관내피세포 증식·이동 억제(세포)·대동맥 고리 혈관 신생 억제(생체 외)[25]", "source": [25, 35]},
    {"name": "Broussoflavonol B", "name_ko": "브로우소플라보놀 B", "class": "프레닐 플라보놀", "role": "bioactive", "part": "줄기껍질", "content_text": "줄기껍질에서 분리(함량 확인하지 못함)[26]", "activity_ko": "췌장암 세포(PANC-1) 증식·이동 억제(세포)[26]", "source": [26]},
]

assays = [
    {"role": "literature", "compound": "Marmesin", "compound_ko": "마르메신", "part": "닥나무 추출물(부위 확인하지 못함)", "content": "확인하지 못함[35]",
     "method": "HPLC(검출기 확인하지 못함)",
     "conditions": {"instrument": "", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "", "injection": "", "sample_prep": "", "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""},
     "rationale": "국내 연구가 마르메신을 닥나무 추출물의 지표성분으로 삼아 HPLC 분석법을 검증했다고 WebSearch 요약에서만 확인함 — 원문은 이 환경에서 열지 못해 분석 조건 칸을 비움(전문 확인 못함)[35]", "source": [35], "url": "https://koreascience.kr/article/JAKO201608259724440.page", "source_kind": "paper"},
    {"role": "literature", "compound": "Luteolin", "compound_ko": "루테올린(및 클로로겐산 등 잎 페놀 19종)", "part": "잎(동결건조 분말)", "content": "교배 잡종 잎 27.4 ± 2.4 μg/g DW, 나머지 두 종 2.6 ± 0.1·3.4 ± 0.4 μg/g DW(어느 값이 B. kazinoki인지 확인하지 못함)[12]",
     "method": "UPLC-PDA / UPLC-ESI-MS/MS(삼중사중극자)",
     "conditions": {"instrument": "Waters UPLC + XEVO-TQ 삼중사중극자 질량분석기(ESI)", "column": "ZORBAX Eclipse Plus C18, 150 mm × 3.0 mm, 1.8 µm", "mobile_phase": "A: 0.1% 포름산, B: 아세토니트릴", "gradient": "0–1분 5% B; 1–8분 5–40% B; 8–12분 40–95% B; 16–17분 95–100% B; 17–21분 100% B; 21–25분 5% B", "flow": "1.0 mL/min", "temp": "40 °C", "detection": "UV 350 nm(PDA 200–800 nm); ESI 양이온, 모세관 3.00 kV, 콘 30 V, 충돌에너지 15 eV, m/z 100–1000", "injection": "1 µL", "sample_prep": "동결건조 잎 가루 20 mg에 0.1% 아세트산 메탄올 1 mL, 30초 혼합 후 실온 초음파 1시간, 12,000 rpm 10분 원심, 0.22 µm 여과", "standard": "루틴(플라보노이드 반정량)·trans-5-카페오일퀸산(클로로겐산류) 환산", "linearity": "루틴 Y = 0.0041X + 0.0032(r = 0.9991); 클로로겐산 Y = 0.0021X + 0.0058(r = 0.9982)", "lod": "", "loq": "", "recovery": ""},
     "rationale": "닥나무속 세 분류군의 잎(식품원료 사용 부위)을 같은 조건으로 정량 비교한 유일하게 확인한 자료다; 다만 시료는 중국 베이징에서 재배한 나무이고 받은 전문 텍스트에서 종 이름이 빠져 B. kazinoki 값을 특정하지 못했다[12]", "source": [12], "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8200958/", "source_kind": "paper"},
]

annual = [(2009, 11, 36), (2010, 10, 33), (2011, 14, 132), (2012, 6, 148), (2013, 2, 107), (2014, 4, 7), (2015, 5, 10), (2016, 5, 9), (2017, 5, 9), (2018, 3, 6), (2019, 3, 7), (2020, 3, 6), (2021, 3, 6), (2022, 2, 6), (2023, 2, 6), (2024, 2, 6)]
production = []
NOTE = "특용작물 '닥나무' 전국 값(수확 부위 미기재)"
for y, a, p in annual:
    production.append({"metric": "area_ha", "region": "대한민국", "year": y, "value": a, "unit": "ha", "note": NOTE, "source": [3]})
    production.append({"metric": "production_t", "region": "대한민국", "year": y, "value": p, "unit": "톤", "note": NOTE, "source": [3]})
production.append({"metric": "farms", "region": "대한민국", "year": 2024, "value": 11, "unit": "호", "note": NOTE, "source": [3, 4]})
RN = "2024 특용작물 생산실적 시도별 표(기타특용작물 '닥나무')"
production += [
    {"metric": "farms", "region": "충청북도", "year": 2024, "value": 7, "unit": "호", "note": RN, "source": [4]},
    {"metric": "area_ha", "region": "충청북도", "year": 2024, "value": 2, "unit": "ha", "note": RN, "source": [4]},
    {"metric": "production_t", "region": "충청북도", "year": 2024, "value": 4, "unit": "톤", "note": RN, "source": [4]},
    {"metric": "farms", "region": "경상북도", "year": 2024, "value": 4, "unit": "호", "note": RN + "; 면적은 0 ha로 표기(반올림 추정)", "source": [4]},
    {"metric": "production_t", "region": "경상북도", "year": 2024, "value": 1, "unit": "톤", "note": RN, "source": [4]},
]

d = {
    "slug": "broussonetia-kazinoki",
    "name_ko": "닥나무",
    "name_en": "Korean paper tree (Small paper mulberry)",
    "scientific_name": "Broussonetia kazinoki Sieb.",
    "aliases": ["저상", "딱나무", "꾸지닥나무", "닥나무가지", "닥나무잎", "닥나무농축액", "닥나무추출액", "Korean paper tree", "Small paper mulberry", "kōzo", "Broussonetia × kazinoki Siebold"],
    "sections": sections,
    "compounds": compounds,
    "markers": [],
    "assays": assays,
    "nutrients": [],
    "production": production,
    "world": [],
    "gi": [],
    "orgs": [],
    "sources": sources,
}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in sections:
    print(s["key"], len(s["body"]))
