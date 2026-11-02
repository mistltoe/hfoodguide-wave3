import csv, json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
STATS = ROOT.parent.parent / "stats"
ACC = "2026-11-02"


def pm(pmid, title, journal):
    return {"title": title, "url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/", "publisher": f"{journal} (PubMed)", "accessed": ACC}


S = [
    {"title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 마뿌리(Dioscorea batatas Decaisne / Dioscorea japonica Thunberg / Dioscorea polystachya / Dioscorea opposita)", "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
    pm(32959173, "An underutilized orphan tuber crop—Chinese yam: a review. Planta 2020 (PMC7505826, doi:10.1007/s00425-020-03458-3)", "Planta"),
    pm(39725934, "Comparative plastomic analysis of cultivated Dioscorea polystachya and its close relatives provides insights on the inter- and intraspecific phylogenies and potential wild origins of domestication. BMC Plant Biol 2024 (PMC11670431, doi:10.1186/s12870-024-06003-6)", "BMC Plant Biology"),
    pm(41821685, "A haplotype-resolved chromosome-level genome assembly of autotetraploid Chinese yam elucidates dioscin biosynthesis and regulation. Hortic Res 2025 (PMC12977164, doi:10.1093/hr/uhaf344) — 초록", "Horticulture Research"),
    pm(20880931, "Understanding the germination of bulbils from an ecological perspective: a case study on Chinese yam (Dioscorea polystachya). Ann Bot 2010 (PMC2990661, doi:10.1093/aob/mcq189) — 초록", "Annals of Botany"),
    pm(25139563, "New and unusual forms of calcium oxalate raphide crystals in the plant kingdom. J Plant Res 2014 (doi:10.1007/s10265-014-0654-y) — 초록", "Journal of Plant Research"),
    pm(31717654, "Quantitative Analysis of Bioactive Phenanthrenes in Dioscorea batatas Decne Peel, a Discarded Biomass from Postharvest Processing. Antioxidants 2019;8:541 (PMC6912652, doi:10.3390/antiox8110541)", "Antioxidants (MDPI)"),
    pm(30104552, "Effects of Rhizome Extract of Dioscorea batatas and Its Active Compound, Allantoin, on the Regulation of Myoblast Differentiation and Mitochondrial Biogenesis in C2C12 Myotubes. Molecules 2018;23:2023 (PMC6222821, doi:10.3390/molecules23082023)", "Molecules (MDPI)"),
    pm(40617843, "Effects of different cooking methods and soil environment on the nutrition of Dioscorea opposita Thunb. NPJ Sci Food 2025 (PMC12228800, doi:10.1038/s41538-025-00499-4)", "npj Science of Food"),
    pm(26501316, "Antidiabetic Effects of Yam (Dioscorea batatas) and Its Active Constituent, Allantoin, in a Rat Model of Streptozotocin-Induced Diabetes. Nutrients 2015 (PMC4632431, doi:10.3390/nu7105411)", "Nutrients (MDPI)"),
    pm(15047697, "Characterization of the yam tuber storage proteins from Dioscorea batatas exhibiting unique lectin activities. J Biol Chem 2004;279:26028 (doi:10.1074/jbc.M402139200) — 초록", "Journal of Biological Chemistry"),
    pm(11600050, "Antioxidant activities of dioscorin, the storage protein of yam (Dioscorea batatas Decne) tuber. J Agric Food Chem 2001;49:4956 (doi:10.1021/jf010606m) — 초록", "Journal of Agricultural and Food Chemistry"),
    pm(18047799, "Induction of growth hormone release by dioscin from Dioscorea batatas DECNE. J Biochem Mol Biol 2007;40:1016 (doi:10.5483/bmbrep.2007.40.6.1016) — 초록", "Journal of Biochemistry and Molecular Biology"),
    pm(16756078, "Effect of ethanol extract of dried Chinese yam (Dioscorea batatas) flour containing dioscin on gastrointestinal function in rat model. Arch Pharm Res 2006;29:348 (doi:10.1007/BF02968583) — 초록", "Archives of Pharmacal Research"),
    pm(12494332, "Yam (Dioscorea batatas) tuber mucilage exhibited antioxidant activities in vitro. Planta Med 2002;68:1072 (doi:10.1055/s-2002-36356) — 초록", "Planta Medica"),
    pm(15036459, "Immune cell stimulating activity of mucopolysaccharide isolated from yam (Dioscorea batatas). J Ethnopharmacol 2004;91:1 (doi:10.1016/j.jep.2003.11.006) — 초록", "Journal of Ethnopharmacology"),
    pm(21720007, "Batatasin I, a naturally occurring phenanthrene derivative, isolated from tuberous roots of Dioscorea batatas suppresses eicosanoids generation and degranulation in bone marrow derived-mast cells. Biol Pharm Bull 2011;34:1021 (doi:10.1248/bpb.34.1021) — 초록", "Biological and Pharmaceutical Bulletin"),
    pm(34520827, "Anti-neuroinflammatory activity of 6,7-dihydroxy-2,4-dimethoxy phenanthrene isolated from Dioscorea batatas Decne partly through suppressing the p38 MAPK/NF-κB pathway in BV2 microglial cells. J Ethnopharmacol 2021 (doi:10.1016/j.jep.2021.114633) — 초록", "Journal of Ethnopharmacology"),
    pm(31342870, "Inhibitory effects of compounds isolated from Dioscorea batatas Decne peel on particulate matter-induced pulmonary injury in mice. J Toxicol Environ Health A 2019 (doi:10.1080/15287394.2019.1646174) — 초록", "Journal of Toxicology and Environmental Health, Part A"),
    pm(18303202, "Identification of Dioscorea batatas (sanyak) allergen as an inhalant and oral allergen. J Korean Med Sci 2008;23:72 (PMC2526494, doi:10.3346/jkms.2008.23.1.72) — 초록", "Journal of Korean Medical Science"),
    pm(7922777, "Occupational asthma caused by two herb materials, Dioscorea batatas and Pinellia ternata. Clin Exp Allergy 1994;24:575 (doi:10.1111/j.1365-2222.1994.tb00955.x) — 초록", "Clinical & Experimental Allergy"),
    pm(11345295, "Occupational asthma and rhinitis caused by multiple herbal agents in a pharmacist. Ann Allergy Asthma Immunol 2001;86:469 (doi:10.1016/S1081-1206(10)62498-2) — 초록", "Annals of Allergy, Asthma & Immunology"),
    pm(29423371, "Identification of a thermal stable allergen in yam to cause anaphylaxis (키워드 표기 'Dioscorea opposite'). Asia Pac Allergy 2018;8:e4 (PMC5796964, doi:10.5415/apallergy.2018.8.e4) — 초록", "Asia Pacific Allergy"),
    {"title": "농림축산식품부 「특용작물 생산실적」(1995–2024) — 약용작물 '산약(마)' 연도별 면적·단수·생산량(로컬 파싱본 special_crops_annual.csv)", "url": "https://www.mafra.go.kr", "publisher": "농림축산식품부", "accessed": "2026-10-12"},
    {"title": "농림축산식품부 「2024 특용작물 생산실적」 — 시도별·품목별 '산약(마)' 농가 수·면적·생산량(로컬 파싱본 regional_crops.csv, special_crops_2024.csv)", "url": "https://www.mafra.go.kr", "publisher": "농림축산식품부", "accessed": "2026-10-13"},
    pm(34357058, "Metabolome Profiling of Eight Chinese Yam (Dioscorea polystachya Turcz.) Varieties Reveals Metabolite Diversity and Variety Specific Uses. Life 2021;11:687 (PMC8308037, doi:10.3390/life11070687) — 초록", "Life (MDPI)"),
    pm(41112022, "Intraspecific Genetic Diversity Analyses of Yam (Dioscorea polystachya Turcz.) Based on DUS Traits and SSR Molecular Markers. Ecol Evol 2025 (PMC12530841, doi:10.1002/ece3.72295) — 초록", "Ecology and Evolution"),
    pm(33295037, "Organ- and Age-Specific Differences of Dioscorea polystachya Compounds Measured by UPLC-QTOF/MS. Chem Biodivers 2021 (doi:10.1002/cbdv.202000856) — 초록", "Chemistry & Biodiversity"),
    pm(38790726, "A Frontier Review of Nutraceutical Chinese Yam. Foods 2024;13:1426 (PMC11119861, doi:10.3390/foods13101426) — 초록", "Foods (MDPI)"),
    {"title": "식품의약품안전처 「대한민국약전」 산약(Dioscoreae Rhizoma) 항 — WebSearch 요약으로만 확인(원문 PDF는 이 환경에서 열지 못함)", "url": "https://www.mfds.go.kr/files/upload/herbmed/photo_data/KP_73.pdf", "publisher": "식품의약품안전처", "accessed": ACC},
    pm(25681821, "Dioscorea batatas extract attenuates high-fat diet-induced obesity in mice by decreasing expression of inflammatory cytokines. Med Sci Monit 2015 (PMC4335589, doi:10.12659/MSM.891306) — 초록", "Medical Science Monitor"),
    pm(22583650, "Suppression of adhesion molecule expression by phenanthrene-containing extract of bulbils of Chinese Yam in vascular smooth muscle cells through inhibition of MAPK, Akt and NF-κB. Food Chem Toxicol 2012 (doi:10.1016/j.fct.2012.05.005) — 초록", "Food and Chemical Toxicology"),
    pm(21975811, "Anti-inflammatory activity of 6-hydroxy-2,7-dimethoxy-1,4-phenanthraquinone from tuberous roots of yam (Dioscorea batatas). Arch Pharm Res 2011 (doi:10.1007/s12272-011-0911-8) — 초록", "Archives of Pharmacal Research"),
    pm(36427159, "Quantitative 1H NMR with global spectral deconvolution approach for the determination of gamma-aminobutyric acid in Chinese yam (Dioscorea polystachya Turczaninow). Anal Sci 2023 (doi:10.1007/s44211-022-00221-4) — 초록", "Analytical Sciences"),
    pm(34104726, "Characterization of the complete chloroplast genome of Dioscorea polystachya Turcz. Mitochondrial DNA B Resour 2021 (PMC8143605, doi:10.1080/23802359.2021.1927222) — 초록", "Mitochondrial DNA Part B"),
    pm(16568313, "Monascus fermentation of dioscorea for increasing the production of cholesterol-lowering agent—monacolin K and antiinflammation agent—monascin. Appl Microbiol Biotechnol 2006;72:1254 (doi:10.1007/s00253-006-0404-8) — 초록", "Applied Microbiology and Biotechnology"),
    pm(42352039, "Skin-Protective Activities of Dioscorea batatas Decne Peel Extracts with Differential Phenanthrene Contents. Antioxidants 2026;15:733 (PMC13295824, doi:10.3390/antiox15060733)", "Antioxidants (MDPI)"),
]
sources = [dict(n=i + 1, **s) for i, s in enumerate(S)]

sections = [
    {"key": "overview", "title": "한눈에 보기", "body": (
        "마(Dioscorea batatas Decaisne)는 마과(Dioscoreaceae) 마속의 덩굴성 여러해살이풀로, 땅속으로 곧게 자라는 덩이줄기(흔히 '마뿌리')와 잎겨드랑이의 주아(살눈)를 만든다[2]. 영어로는 East Asian mountain yam 또는 Chinese yam이라 하며, 국제 문헌에서는 같은 식물을 Dioscorea polystachya Turcz.나 Dioscorea opposita로도 적어 이름이 자주 엇갈린다[1][2].\n\n"
        "식품의약품안전처 「식품원료 목록」에서 마뿌리는 식품에 사용할 수 있는 원료(사용가능)이며, 사용 조건은 '사용가능부위 : 뿌리, 뿌리줄기※(산약), 주아(영여자)'이다[1]. 같은 목록에는 마뿌리·마뿌리농축액·마뿌리줄기·마뿌리줄기분말·마뿌리추출분말·마주아의 6개 원료명이 올라 있고, 학명 칸에는 D. batatas Decaisne와 함께 D. japonica Thunberg·D. polystachya·D. opposita가 한 줄로 묶여 있다[1]. 건강기능식품 고시형 원료의 원재료로 쓰인다는 기록은 확인하지 못함.\n\n"
        "덩이줄기는 녹말이 약 65%를 차지하고(품종에 따라 다름) 끈적한 점액과 저장단백질 디오스코린, 알란토인, 디오신 같은 성분을 함유한다[2][11]. 껍질에는 페난트렌류 폴리페놀이 모여 있고 속살에서는 검출한계 아래였다[7]."
    )},
    {"key": "history", "title": "역사", "body": (
        "중국 북부 싱룽거우(興隆溝) 유적 조사에서 마는 기원전 약 6200–5200년 신석기 시대에 이미 이용된 것으로 확인되었고, 수이둥거우(水洞溝) 유적에서는 그보다 훨씬 이른 구석기 시대 이용 흔적도 보고되었다[2]. 완전히 작물화된 것은 약 1000년 전으로 추정되며, 『신농본초경(神農本草經)』에는 처음 야생 식물로 실렸으나 최근 약 400년 동안은 거의 재배품만 약으로 써 왔다[2]. 엽록체 유전체 비교에서는 재배 마가 다볘산(大別山)과 타이항산(太行山)의 야생 마에서 적어도 두 번 따로 작물화되었다는 결과가 나와 역사 기록과도 맞았다[3].\n\n"
        "중국에서는 허난성 산지의 '화이산야오(懷山藥)'가 가장 좋은 품질로 꼽히고, 품종 '톄군(鐵棍)'은 2000년 넘게 설사·당뇨·천식에 써 왔다고 전한다[2][29]. 유럽에는 아일랜드 감자 기근 때 감자 대용 작물로 들어갔으나 지금은 프랑스 오를레앙 부근과 독일 보덴호 부근에서만 조금 재배한다[2].\n\n"
        "한국에서는 마의 뿌리줄기를 '산약(山藥)'이라 부르며 식품이자 한약재로 써 왔고, 국내 연구는 산약을 한국과 일본에 널리 자라는 마의 뿌리줄기로 소개한다[13][20]. 대한민국약전은 산약의 기원을 마(D. batatas Decaisne) 또는 참마(D. japonica Thunberg)의 뿌리줄기를 그대로 또는 쪄서 말린 것으로 정한 것으로 검색 요약에서 확인했다(원문 미열람)[30]. 한국 고문헌의 식용 기록은 원문으로 확인하지 못함."
    )},
    {"key": "biology", "title": "식물학적 특징", "body": (
        "마속 식물은 다른 식물을 감고 3 m 넘게 오르는 외떡잎 덩굴식물로 대부분 암수딴그루이고 꽃은 지름 2–4 mm로 작으며, 마는 6–9월에 꽃이 피고 7–11월에 열매(세 칸의 삭과)를 맺는다[2]. 자생지는 중국·한국·쿠릴열도·타이완이고 일본·미국 남동부·우루과이·서부 히말라야에는 들어가 퍼졌다고 정리되어 있다[2]. 자연에서는 숲·산비탈·강가·길가에서 자란다[2].\n\n"
        "덩이줄기는 뿌리나 줄기가 아니라 배축(胚軸)에서 생기며, 끝부분만 계속 자라 길이 1 m에 이르지만 굵기는 5–8 cm 정도로 가늘고 땅속으로 거의 수직으로 뻗는다[2]. 얇은 갈색 코르크 껍질 아래 흰 살이 있고, 바탕조직에는 길이 10–39 µm의 녹말 알갱이와 점액 속에 수산칼슘 결정을 담은 이형세포가 흩어져 있다[2]. 이 덩이줄기에서는 새로운 형태의 바늘 모양 수산칼슘 결정(라피드) 두 가지가 보고되었다[6].\n\n"
        "잎겨드랑이에 생기는 주아는 여름–가을에 떨어질 때 대부분 휴면 상태이며, 겨울의 저온을 거쳐야 이듬해 봄에 뿌리와 싹을 낸다[5]. 덩이줄기와 주아도 수확기에 휴면에 들어가 약 3개월간 깨지 않는다[2]."
    )},
    {"key": "related_species", "title": "학명과 가까운 종", "body": (
        "이 소재의 학명은 문헌마다 다르다[1][2]. 식품원료 목록은 D. batatas Decaisne를 대표로 D. japonica·D. polystachya·D. opposita를 함께 적었지만, 국제 총설은 Dioscorea polystachya Turcz.를 정명으로 쓰고 동아시아 문헌의 'D. opposita Thunb.'는 세계식물목록 기준으로 인도 원산 D. oppositifolia의 이명으로 본다고 정리했다[1][2]. 이 자료에서는 제목·본문에 D. batatas, D. polystachya, 또는 '중국 마(Chinese yam)'로서의 D. opposita를 쓴 논문을 같은 종으로 다루고, 그 학명 표기를 출처 목록에 그대로 남겼다[2][7][9].\n\n"
        "참마(D. japonica Thunb.)는 중국 남부·일본·한국·타이완 원산의 다른 종이며 일본에서는 '야마노이모'라 부른다[2]. 엽록체 유전체 계통에서 D. polystachya는 D. japonica와 자매군을 이루어 가장 가깝다[3]. 대한민국약전의 산약은 두 종을 모두 기원으로 인정하는 것으로 검색 요약에서 확인했으나, 이 자료의 성분·안전성 값에는 D. japonica만 다룬 논문을 넣지 않았다[30].\n\n"
        "마는 마속 Enantiophyllum 절에 속하며, 같은 절에 물마(D. alata)와 흰기니얌(D. rotundata) 같은 열대 주식 얌이 있다[2]. 중국에서는 마속 여러 종을 재배해 왔고 덩이줄기 모양이 비슷해 서로 혼동되기 쉽다[2][3]."
    )},
    {"key": "cultivation", "title": "재배와 생산", "body": (
        "북반구에서는 봄(3–4월)에 씨마(덩이줄기 조각이나 주아)를 심어 5–9월에 덩굴과 덩이줄기를 키우고, 10–11월에 잎이 시들면서 덩이줄기가 성숙해 휴면에 들어간다[2]. 주아에서 키운 덩이줄기는 작아서 이듬해 씨마로 쓰고, 큰 덩이줄기 조각을 심으면 길이 1 m·무게 3 kg이 넘게 자란다[2]. 덩이줄기가 깊이 곧게 자라 수확에 품이 많이 들며, 일본에서는 관을 눕혀 묻고 그 안에서 키워 캐기 쉽게 한다[2]. 흙이 무르고 미네랄이 많은 강가 퇴적토가 좋고, 모래땅은 덩이줄기의 다당류와 포도당 함량을 높인다고 보고되었다[2]. 재배 연수별 비교에서는 디오신이 2년생, 알란토인·아데노신이 4년생 덩이줄기에서 가장 많았고 알란토인은 속살보다 껍질 쪽에 많았다[28].\n\n"
        "농림축산식품부 「특용작물 생산실적」에서 약용작물 '산약(마)'의 전국 생산량은 1996년 2,788톤에서 2016년 11,768톤으로 정점을 찍은 뒤 2024년 재배면적 612 ha·생산량 7,742톤이었다[24]. 2024년 재배 농가는 986호이고, 경북이 면적 446 ha·생산량 6,061톤, 경남이 123 ha·1,225톤으로 두 도가 대부분을 차지했다[25]. 이 통계는 품목 '산약(마)'을 종 구분 없이 집계한 것이어서 참마 등 다른 마가 섞였는지는 확인하지 못함. 지리적 표시 등록은 공공데이터(gi.json)에서 이 종으로 연결된 항목을 확인하지 못함."
    )},
    {"key": "processing", "title": "가공과 이용", "body": (
        "식품원료 목록에는 생마 외에 마뿌리농축액·마뿌리줄기분말·마뿌리추출분말·마주아 같은 가공 형태의 원료명이 올라 있다[1]. 마는 다른 얌과 달리 날로 먹을 수 있고, 껍질을 벗긴 살의 끈적한 점액이 동아시아에서 국이나 요리의 식감을 내는 데 쓰인다[2]. 감자처럼 조리해 먹거나 녹말 가루를 빵·국수에 쓰기도 한다[2].\n\n"
        "마는 쉽게 상하기 때문에 수확한 덩이줄기 상당량을 껍질을 벗기고 열로 말려 '마 가루'로 만들며, 이때 버려지는 껍질에 페난트렌류가 모여 있어 가루 제품으로는 이 성분을 거의 섭취하지 못한다는 분석이 있다[7]. 껍질 추출물은 화장품 소재로 시험되었다[37]. 조리법 비교에서는 삶으면 알란토인이 물로 녹아 나와 줄었고(사질토 마 0.84%→0.79%, 황토 마 0.64%→0.55%), 찌거나 열풍 구이를 하면 오히려 늘었다[9]. 주아(영여자)의 메탄올 추출물에서는 페난트렌 성분이 확인되었고 혈관평활근세포의 부착분자 발현을 억제했다(시험관)[32]. 동물 연구에서는 마 추출물이 고지방식 생쥐의 체중·내장지방 증가를 억제하고[31] 당뇨 쥐의 혈당을 낮췄으나[10], 사람 대상 근거는 이번 조사에서 확인하지 못함. 마는 홍국균(Monascus purpureus) 발효 기질로 쓰였을 때 쌀보다 모나콜린 K를 5.37배 많이 만들었다(2,584 mg/kg)[36].\n\n"
        "식약처 「식품 등의 생산실적」 건강기능식품 품목표에서 마를 원료로 한 품목은 확인하지 못함."
    )},
    {"key": "genetics", "title": "유전체와 육종", "body": (
        "중국 마는 염색체 기본수 x = 10의 배수체로 2n = 100 또는 140이 보고되었고, 꽃이 드물고 영양번식을 주로 해 육종이 어렵다[2]. 2025년 발표된 일배체형 분리 염색체 수준 유전체는 크기 1.56 Gb, 4개 일배체형에 걸친 80개 염색체, 단백질 암호 유전자 95,668개로 동질4배체임을 보였다[4]. 이 종은 약 464만 년 전 가까운 종과 갈라진 뒤 약 142만 년 전 독자적인 전장 유전체 중복을 겪었고, 디오신 생합성 유전자가 2배체 종보다 많이 남아 있었다[4].\n\n"
        "엽록체 유전체는 약 153 kb로, 재배 마는 톄군·안핑·포서우·타이항 복합의 네 품종군으로 나뉘었다[3]. 허난성 자오쭤산 시료의 엽록체 유전체는 152,958 bp, 유전자 131개였다[35]. 중국 17개 성에서 모은 113개 계통은 DUS 형질 50개와 SSR 표지 19개로 모두 구별되었고, 이름만 다른 동종 10묶음과 같은 이름의 이종 13묶음이 드러났다[27]. 한국 품종·계통의 유전체 분석 자료는 확인하지 못함."
    )},
    {"key": "safety", "title": "안전성", "body": (
        "마는 식품원료 목록에서 제한 없이 '사용가능' 원료이고 사용 부위는 뿌리·뿌리줄기·주아로 정해져 있다[1]. 중국 마 덩이줄기는 다른 식용 얌과 달리 독성이 없어 날로 먹을 수 있다고 정리되어 있다[2].\n\n"
        "알레르기는 드물지만 보고가 있다[20][23]. 국내에서 마를 먹은 뒤 심한 두드러기·혈관부종을 겪은 환자와 산약 가루를 흡입해 직업성 천식이 생긴 환자 모두 27 kDa 저장단백질 디오스코린(DB3S)에 특이 IgE를 보였다[20]. 한약재를 다루는 작업자에서 산약 가루로 인한 직업성 천식·비염이 확인된 사례도 있다[21][22]. 중국에서는 삶은 마를 먹고 아나필락시스를 겪은 3명이 보고되었고, 원인 단백질 DB3S가 열에 안정해 익혀도 알레르기를 일으킬 수 있으므로 환자는 날것과 익힌 것을 모두 피해야 한다고 했다[23].\n\n"
        "덩이줄기 조직에는 바늘 모양의 수산칼슘 결정이 들어 있다[2][6]. 국내 공공기관의 잔류농약·중금속 등 마 안전 정보는 이번 조사에서 확인하지 못함."
    )},
]

compounds = [
    {"name": "Allantoin", "name_ko": "알란토인", "class": "요소 유도체(이우레이드)", "role": "marker", "part": "뿌리줄기(덩이줄기)",
     "content_text": "물 추출물 중 1.53%(0.36 mg/mL)[8]; 껍질 벗긴 덩이줄기 건조물 약 0.84%(사질토)·0.64%(황토)[9]; 건조중량의 0.8%(총설 인용)[2]",
     "activity_ko": "추출물의 활성 성분으로 정량됨; C2C12 근관세포 분화·미토콘드리아 생합성 촉진(시험관)[8], STZ 당뇨 쥐 혈당 저하(복강 투여)[10]", "source": [2, 8, 9, 10, 28]},
    {"name": "Dioscin", "name_ko": "디오신", "class": "스테로이드 사포닌", "role": "bioactive", "part": "뿌리줄기",
     "content_text": "건조중량의 0.077%(총설 인용)[2]; 마 가루 40% 에탄올 추출물 177 ± 58 µg/mL[14]",
     "activity_ko": "쥐 뇌하수체 세포 성장호르몬 분비 유도 ED50 1.14 × 10⁻⁵ M(시험관)[13]", "source": [2, 4, 13, 14]},
    {"name": "Diosgenin", "name_ko": "디오스게닌", "class": "스테로이드 사포게닌", "role": "bioactive", "part": "덩이줄기",
     "content_text": "중국 8개 품종 비교에서 허난 야생 마가 가장 높음(수치는 초록에 없음)[26]",
     "activity_ko": "품종 간 함량 차이 비교 대상으로 쓰임[26]", "source": [26]},
    {"name": "2,7-Dihydroxy-4,6-dimethoxyphenanthrene", "name_ko": "2,7-디하이드록시-4,6-디메톡시페난트렌", "class": "페난트렌", "role": "bioactive", "part": "뿌리줄기 껍질",
     "content_text": "껍질 47.35 ± 0.25 mg/100 g(건조중량), 6.76 ± 0.04 mg/100 g(생체중); 속살은 검출한계 미만[7]",
     "activity_ko": "미세먼지 유발 활성산소 소거·폐 손상 억제(쥐)[19]", "source": [7, 19]},
    {"name": "6,7-Dihydroxy-2,4-dimethoxyphenanthrene", "name_ko": "6,7-디하이드록시-2,4-디메톡시페난트렌", "class": "페난트렌", "role": "bioactive", "part": "뿌리줄기 껍질",
     "content_text": "껍질 29.29 ± 0.08 mg/100 g(건조중량), 4.18 ± 0.01 mg/100 g(생체중)[7]",
     "activity_ko": "BV2 미세아교세포의 염증 매개체 생성 억제(시험관)[18]", "source": [7, 18, 19]},
    {"name": "Batatasin I", "name_ko": "바타타신 I(6-하이드록시-2,4,7-트리메톡시페난트렌)", "class": "페난트렌", "role": "bioactive", "part": "뿌리줄기 껍질; 덩이줄기",
     "content_text": "껍질 35.85 ± 0.12 mg/100 g(건조중량), 5.12 ± 0.02 mg/100 g(생체중)[7]",
     "activity_ko": "비만세포 COX-2 의존 PGD2 생성 억제 IC50 1.78 µM, LTC4 생성 억제 IC50 1.56 µM(시험관)[17]", "source": [7, 17]},
    {"name": "6-Hydroxy-2,7-dimethoxy-1,4-phenanthrenequinone", "name_ko": "6-하이드록시-2,7-디메톡시-1,4-페난트라퀴논", "class": "페난트라퀴논", "role": "bioactive", "part": "덩이줄기",
     "content_text": "분리 성분(함량 수치 없음)[33]",
     "activity_ko": "COX-2 의존 PGD2 생성 억제 IC50 0.08 µM, 5-LOX 의존 LTC4 생성 억제 IC50 0.032 µM(시험관)[33]", "source": [33]},
    {"name": "Dioscorin", "name_ko": "디오스코린(저장단백질)", "class": "저장단백질(탄산탈수효소 유사)", "role": "bioactive", "part": "덩이줄기",
     "content_text": "주요 단백질 DB1:DB2:DB3:DB4 수율 비 20:50:20:10, 디오스코린 A(DB2)가 총단백의 50%[11]",
     "activity_ko": "32 kDa 디오스코린의 DPPH·하이드록실 라디칼 소거(시험관)[12]; DB3S는 주요 알레르겐[20][23]", "source": [11, 12, 20, 23]},
    {"name": "Yam mucilage polysaccharide", "name_ko": "점액 다당(뮤코다당)", "class": "다당류·당단백 복합체", "role": "bioactive", "part": "덩이줄기",
     "content_text": "정제 점액의 DPPH 소거 IC50 0.86 mg/mL, 하이드록실 라디칼 소거 IC50 22 µg/mL[15]",
     "activity_ko": "비장세포 IFN-γ 분비·대식세포 탐식능 증가(시험관)[16]", "source": [15, 16]},
    {"name": "Starch", "name_ko": "녹말", "class": "탄수화물", "role": "nutrient", "part": "덩이줄기",
     "content_text": "약 65%(품종에 따라 다름)[2]; 64.80 ± 0.96(사질토)·74.60 ± 1.34(황토) g/100 g 건조중량[9]",
     "activity_ko": "덩이줄기 비대기에 급히 쌓이는 주 저장 성분[2]", "source": [2, 9]},
    {"name": "Potassium", "name_ko": "칼륨", "class": "무기질", "role": "nutrient", "part": "덩이줄기",
     "content_text": "14.68 mg/g(사질토)·15.68 mg/g(황토) 건조중량[9]",
     "activity_ko": "덩이줄기에서 가장 많은 무기질로 측정됨[9]", "source": [9]},
    {"name": "Ascorbic acid", "name_ko": "비타민 C(아스코르브산)", "class": "비타민", "role": "nutrient", "part": "덩이줄기",
     "content_text": "0.092%(사질토)·0.095%(황토), 분광법(245 nm)[9]",
     "activity_ko": "조리 후 측정값이 늘었으나 분광법 간섭 가능성이 지적됨[9]", "source": [9]},
    {"name": "gamma-Aminobutyric acid", "name_ko": "가바(GABA)", "class": "아미노산", "role": "bioactive", "part": "덩이줄기",
     "content_text": "qNMR 정량법 개발(함량 수치는 초록에 없음)[34]",
     "activity_ko": "기능성 대사물로서 정량 대상이 됨[34]", "source": [34]},
    {"name": "Calcium oxalate", "name_ko": "수산칼슘", "class": "무기 결정(라피드)", "role": "bioactive", "part": "덩이줄기",
     "content_text": "점액 속 이형세포에 결정으로 존재(함량 수치 없음)[2]; 새로운 V·VI형 라피드 보고[6]",
     "activity_ko": "분류 형질로 쓰이는 결정 형태[6]", "source": [2, 6]},
]

E = {k: "" for k in ("instrument", "column", "mobile_phase", "gradient", "flow", "temp", "detection", "injection", "sample_prep", "standard", "linearity", "lod", "loq", "recovery")}
assays = [
    {"role": "literature", "compound": "Allantoin", "compound_ko": "알란토인", "part": "말린 뿌리줄기(산약) 물 추출물",
     "content": "물 추출물 중 1.53%(0.36 mg/mL)[8]", "method": "HPLC-DAD",
     "conditions": dict(E, instrument="Agilent 1260 Infinity II 4원 펌프, G7129A 바이알 샘플러, G7115A 다이오드 어레이 검출기",
                        column="ZORBAX NH2, 4.6 × 150 mm, 5 µm", mobile_phase="A: 물(HPLC 등급), B: 아세토니트릴(HPLC 등급)",
                        gradient="0분 25% B, 5분 17% B, 10분 17% B(원문 그대로)", flow="1.0 mL/min", temp="30 °C", detection="UV 200 nm",
                        injection="10 µL", sample_prep="말린 뿌리줄기 200 g을 물 2 L로 3시간 끓여 추출, 여과(Whatman 1호) → 60 °C 감압농축 → 동결건조(수율 11.4%)",
                        standard="알란토인 표준품(Sigma-Aldrich), 머무름 시간 비교",
                        linearity="y = 16039x − 16.79, 상관계수 > 0.9995; 정밀도 RSD 0.67%, 반복성 RSD 1.85%"),
     "rationale": "추출물의 활성 성분으로 알란토인을 표준품 머무름 시간으로 확인해 정량했다[8]. 알란토인 옆에 작은 피크가 함께 나와 아데노신 겹침 가능성을 저자가 언급했고, 검출·정량한계와 회수율은 본문에 없어 비워 둠.",
     "source": [8], "url": "https://pubmed.ncbi.nlm.nih.gov/30104552/", "source_kind": "paper"},
    {"role": "literature", "compound": "Allantoin", "compound_ko": "알란토인(조리·토양 비교)", "part": "껍질 벗긴 덩이줄기(60 °C 건조 분말)",
     "content": "사질토 마 약 0.84%, 황토 마 약 0.64%; 삶은 후 0.79%·0.55%[9]", "method": "HPLC-UV(VWD)",
     "conditions": dict(E, instrument="Agilent 1260 HPLC, 가변파장 검출기(VWD)", column="Eclipse XDB-C18, 4.6 × 250 mm, '0.5 μm'(원문 표기)",
                        mobile_phase="A: 물, B: 메탄올", gradient="10% B 7분 유지 → 1분간 10→100% B → 100% B 7분 유지",
                        flow="1 mL/min", temp="35 °C(같은 단락에 칼럼 온도 30 °C로도 적힘)", detection="210 nm",
                        sample_prep="분말 50 mg + 에탄올 10 mL·15% 메탄올 10 mL, 얼음으로 온도 유지하며 50 kHz 초음파 30분 → 8000 × g 5분 원심 → 0.45 µm 여과",
                        standard="알란토인 표준품(J&K Scientific), 머무름 시간으로 확인"),
     "rationale": "알란토인은 중국 마의 품질 평가에 널리 쓰이는 성분이라 조리법·재배 토양에 따른 변화를 이 성분으로 비교했다[9]. 논문 제목의 학명은 D. opposita Thunb.(중국 허난성 원양현 재배품)이며, 직선성·검출한계·회수율은 본문에 없어 비워 둠.",
     "source": [9], "url": "https://pubmed.ncbi.nlm.nih.gov/40617843/", "source_kind": "paper"},
    {"role": "literature", "compound": "Batatasin I", "compound_ko": "페난트렌 3종(2,7-디하이드록시-4,6-디메톡시페난트렌·6,7-디하이드록시-2,4-디메톡시페난트렌·바타타신 I)", "part": "덩이줄기 껍질·속살(동결건조 분말)",
     "content": "껍질 건조중량 기준 47.35 ± 0.25, 29.29 ± 0.08, 35.85 ± 0.12 mg/100 g(생체중 6.76·4.18·5.12 mg/100 g); 속살은 검출한계 미만[7]",
     "method": "HPLC-PDA(UV 260 nm)",
     "conditions": dict(E, instrument="Waters Alliance 2695 HPLC, Waters 2996 광다이오드 어레이 검출기", column="Hector-M-C18, 250 × 4.6 mm, 5 µm (RStech)",
                        mobile_phase="A: 0.1% 트리플루오로아세트산 수용액, B: 아세토니트릴", gradient="0–5분 5% B; 5–20분 5→100% B; 20–25분 100% B",
                        flow="1.0 mL/min", temp="40 °C", detection="260 nm", injection="10 µL",
                        sample_prep="동결건조 분말 1 g + 95% 에탄올 250 mL, 25 °C 12시간 추출 → 0.45 µm 여과 → 감압 농축 → 메탄올 10 mL에 녹임(시료당 3회 주입)",
                        standard="껍질에서 분리해 NMR로 동정한 페난트렌 3종, 메탄올 1 mg/mL 원액을 3.125–100 µg/mL로 희석",
                        linearity="3.125–100 µg/mL, 결정계수 > 0.9959", lod="< 0.58 µg/mL(S/N 3)", loq="< 1.94 µg/mL(S/N 10)"),
     "rationale": "페난트렌류는 마속에 특징적이고 일반 HPLC-UV로 분석하기 쉬워 마의 표준 지표 물질로 제안되었다[7]. 경북 안동산 마를 썼고, 같은 연구진의 2026년 후속 연구는 이 방법으로 껍질 추출물을 다시 정량했다(0.625–20 µg/mL, 결정계수 0.9973–0.9998)[37]. 회수율은 본문에 없어 비워 둠.",
     "source": [7, 37], "url": "https://pubmed.ncbi.nlm.nih.gov/31717654/", "source_kind": "paper"},
]

production = []
for r in csv.DictReader((STATS / "special_crops_annual.csv").open(encoding="utf-8")):
    if r["item"] != "산약(마)":
        continue
    y = int(r["year"])
    note = "약용작물 '산약(마)' 전국 값(종 구분 없음)"
    if r["area_ha"]:
        production.append({"metric": "area_ha", "region": "대한민국", "year": y, "value": float(r["area_ha"]), "unit": "ha", "note": note, "source": [24]})
    if r["prod_t"]:
        production.append({"metric": "production_t", "region": "대한민국", "year": y, "value": float(r["prod_t"]), "unit": "톤", "note": note, "source": [24]})
production.append({"metric": "farms", "region": "대한민국", "year": 2024, "value": 986, "unit": "호", "note": "약용작물 '산약(마)' 2024 농가 수", "source": [25]})
for p in production:
    if isinstance(p["value"], float) and p["value"].is_integer():
        p["value"] = int(p["value"])

d = {
    "slug": "dioscorea-batatas",
    "name_ko": "마뿌리",
    "name_en": "East Asian mountain yam (Chinese yam)",
    "scientific_name": "Dioscorea batatas Decaisne",
    "aliases": ["마", "산약(山藥)", "마주아", "영여자(주아)", "Dioscorea polystachya Turcz.", "Dioscorea opposita(동아시아 문헌 표기)", "Chinese yam", "Huai Shan Yao(懷山藥)", "nagaimo(長芋)"],
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
(ROOT / "dossier.json").write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(sources), len(compounds), len(assays), len(production))
for s in sections:
    print(s["key"], len(s["body"]))
