import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
A = "2026-11-02"
I1020 = "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020"
def pm(pmid, title, pub, extra=""):
    return {"title": f"{title} (PMID {pmid}{extra})", "url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/", "publisher": pub, "accessed": A}
S = [
 {"title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 구절초 12개 원료명 행(구절초·건조구절초·구절초분말·구절초원액·구절초농축액·구절초추출분말·구절초추출물·구절초추출액·구절초추출농축고형분·구절초꽃·구절초잎·구절초줄기). 학명 'Chrysanthemum zawadskii Herbich var. latilobum (Maxim.) Kitamura / Chrysanthemum zawadskii var. coreanum', 식품원료(A코드)·식물, 12행 모두 제한적사용, 조건 '제한적사용가능부위 : 전초※(구절초)'. 로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json", "url": I1020, "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
 {"title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 관련 행: 건강기능식품(C코드) 개별인정 '구절초추출물(기능성원료인정제2021-12호)'(Chrysanthemum Extract; Chrysanthemum zawadskii Herbich var. latilobum (Maxim.) Kitamura; 사용부위 : 잎, 줄기; 사용가능); 같은 속 식품원료 국화꽃·국화전초 등(Chrysanthemum morifolium Ramat. / 감국 Chrysanthemum indicum L.; '사용가능부위 : 꽃※(감국), 전초'; 사용가능), 산국·산국꽃·산국순(Chrysanthemum boreale (Makino) Makino / Dendranthema boreale; '사용가능부위 : 순, 꽃'; 사용가능), 제충국(Chrysanthemum cinerariaefolium)·피버퓨(Chrysanthemum parthenium) 사용불가. 로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json", "url": I1020, "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
 {"title": "식품의약품안전처 「식품 등의 생산실적」 2022·2023·2024·2025년판 품목 유형별 현황(개별인정형) — 구절초추출물 행(생산능력·생산량 톤, 생산액·국내판매액 천원). 파싱본 docs/stats/hf_items.csv", "url": "https://www.mfds.go.kr", "publisher": "식품의약품안전처", "accessed": A},
 pm("34190191", "Efficacy of GCWB106 (Chrysanthemum zawadskii var. latilobum extract) in osteoarthritis of the knee: A 12-week randomized, double-blind, placebo-controlled study. Medicine (Baltimore) 2021;100(26):e26542", "Wolters Kluwer / PubMed", ", PMC8257904, doi:10.1097/MD.0000000000026542; PMC 전문 확인"),
 pm("33321982", "Anti-Osteoarthritic Mechanisms of Chrysanthemum zawadskii var. latilobum in MIA-Induced Osteoarthritic Rats and Interleukin-1β-Induced SW1353 Human Chondrocytes. Medicina (Kaunas) 2020;56(12):685", "MDPI / PubMed", ", PMC7762971, doi:10.3390/medicina56120685; PMC 전문 확인"),
 pm("35023382", "Osteoarthritis improvement effect of Chrysanthemum zawadskii var. latilobum extract in relation to genotype. Int J Vitam Nutr Res 2023;93(5):410-419", "Hogrefe / PubMed", ", doi:10.1024/0300-9831/a000745; 초록 확인"),
 pm("35070943", "Evaluation of the acute, sub-chronic and chronic oral toxicity, genetic toxicity, and safety of a Lomens-P0 (Hordeum vulgare·Chrysanthemum zawadskii 추출물 혼합물). Toxicol Res 2022;38(1):69-90", "Springer / PubMed", ", PMC8748590, doi:10.1007/s43188-021-00090-5; 초록 확인"),
 pm("34858550", "Lomens-P0 (mixed extracts of Hordeum vulgare and Chrysanthemum zawadskii) regulate the expression of factors affecting premenstrual syndrome symptoms. Nutr Res Pract 2021;15(6):715-731", "KNS·KSCN / PubMed", ", PMC8601943, doi:10.4162/nrp.2021.15.6.715; 초록 확인"),
 pm("41526154", "Chrysanthemum zawadskii Flower Extract Rescues Inflammatory Cognitive Impairment. Exp Neurobiol 2026", "KSBNS / PubMed", ", PMC12977228, doi:10.5607/en25035; PMC 전문 확인"),
 pm("40531892", "Chrysanthemum zawadskii ethanol extract inhibits the replication of alpha-coronavirus and beta-coronavirus. PLoS One 2025;20(6):e0326225", "PLOS / PubMed", ", PMC12176134, doi:10.1371/journal.pone.0326225; PMC 전문 확인"),
 pm("31638961", "Ethanol extract of Chrysanthemum zawadskii Herbich induces autophagy and apoptosis in mouse colon cancer cells through the regulation of reactive oxygen species. BMC Complement Altern Med 2019;19(1):274", "BMC / PubMed", ", PMC6805551, doi:10.1186/s12906-019-2688-0; PMC 전문 확인(정량 표 값은 본문에 없음)"),
 pm("36845948", "Ethanol extract of Chrysanthemum zawadskii inhibits the NLRP3 inflammasome by suppressing ASC oligomerization in macrophages. Exp Ther Med 2023;25(3):128", "Spandidos / PubMed", ", PMC9947581, doi:10.3892/etm.2023.11827; PMC 전문 확인"),
 pm("40259245", "Cytogenetic diversity of the diploid Korean wild Chrysanthemum (Asteraceae) inferred from genome size variations and chromosomal distributions of 5S and 18S rDNAs. BMC Plant Biol 2025", "BMC / PubMed", ", PMC12013073, doi:10.1186/s12870-025-06550-6; PMC 전문 확인"),
 pm("19367445", "Syncyte formation in the microsporangium of Chrysanthemum (Asteraceae): a pathway to infraspecific polyploidy. J Plant Res 2009;122(4):439-44", "Springer / PubMed", ", doi:10.1007/s10265-009-0232-x; 초록 확인"),
 pm("34179479", "The complete chloroplast genome of Chrysanthemum zawadskii Herbich (Asteraceae) isolated in Korea. Mitochondrial DNA B Resour 2021;6(7):1956-1958", "Taylor & Francis / PubMed", ", PMC8205035, doi:10.1080/23802359.2021.1934148; 초록 확인"),
 pm("34250234", "Complete chloroplast genome sequence of Dendranthema zawadskii Herbich. Mitochondrial DNA B Resour 2021;6(8):2117-2119", "Taylor & Francis / PubMed", ", PMC8245063, doi:10.1080/23802359.2021.1942261; 초록 확인"),
 pm("35766338", "Hyb-Seq provides new insights into the phylogeny and evolution of the Chrysanthemum zawadskii species complex in China. Cladistics 2022;38(6):663-683", "Wiley / PubMed", ", doi:10.1111/cla.12514; 초록 확인"),
 pm("23133665", "Phylogeny of the genus Chrysanthemum L.: evidence from single-copy nuclear gene and chloroplast DNA sequences. PLoS One 2012;7(11):e48970", "PLOS / PubMed", ", PMC3486802, doi:10.1371/journal.pone.0048970; 초록 확인"),
 pm("22382409", "Sesquiterpenes and other constituents from Dendranthema zawadskii var. latilobum. Chem Pharm Bull 2012;60(3):306-14", "Pharmaceutical Society of Japan / PubMed", ", doi:10.1248/cpb.60.306; 초록 확인"),
 pm("17691057", "Dendrazawaynes A and B, antifungal polyacetylenes from Dendranthema zawadskii (Asteraceae). Planta Med 2007;73(10):1089-94", "Thieme / PubMed", ", doi:10.1055/s-2007-981576; 초록 확인"),
 pm("18087803", "Antimicrobial phenolic derivatives from Dendranthema zawadskii var. latilobum Kitamura (Asteraceae). Arch Pharm Res 2007;30(11):1374-9", "Springer / PubMed", ", doi:10.1007/BF02977359; 초록 확인"),
 pm("24471090", "Volatiles of Chrysanthemum zawadskii var. latilobum K. Prev Nutr Food Sci 2012;17(3):234-8", "KSFN / PubMed", ", PMC3866737, doi:10.3746/pnf.2012.17.3.234; 초록 확인"),
 pm("39942657", "Chrysanthemum zawadskii var. latilobum Flower Essential Oil Reduces MRSA Pathogenicity by Inhibiting Virulence Gene Expression. Molecules 2025;30(3):553", "MDPI / PubMed", ", PMC11820971, doi:10.3390/molecules30030553; 초록 확인"),
 pm("22561855", "6-Methoxyluteolin from Chrysanthemum zawadskii var. latilobum suppresses histamine release and calcium influx via down-regulation of FcεRI α chain expression. J Microbiol Biotechnol 2012;22(5):622-7", "KMB / PubMed", ", doi:10.4014/jmb.1111.11060; 초록 확인"),
 pm("32102220", "Inhibitory Effects of Eriodictyol-7-O-β-d-glucuronide and 5,7-Dihydroxy-4-chromene Isolated from Chrysanthemum zawadskii var. latilobum in FcεRI-Mediated Human Basophilic KU812F Cell Activation. Molecules 2020;25(4):994", "MDPI / PubMed", ", PMC7070965, doi:10.3390/molecules25040994; 초록 확인"),
 pm("12009031", "The effect of linarin on LPS-induced cytokine production and nitric oxide inhibition in murine macrophages cell line RAW264.7. Arch Pharm Res 2002;25(2):170-7", "Springer / PubMed", ", doi:10.1007/BF02976559; 초록 확인"),
 pm("30263427", "Linarin down-regulates phagocytosis, pro-inflammatory cytokine production, and activation marker expression in RAW264.7 macrophages. Food Sci Biotechnol 2016;25(5):1437-1442", "Springer / PubMed", ", PMC6049292, doi:10.1007/s10068-016-0223-3; 초록 확인"),
 pm("40265676", "Dendranthema oreastrum (Hance) Y.Ling Attenuates Oxidative Stress and Airway Inflammation in a Murine Model of Lipopolysaccharide-Induced Acute Lung Injury. Environ Toxicol 2025;40(10):1220-1232", "Wiley / PubMed", ", PMC12432812, doi:10.1002/tox.24520; 초록 확인"),
 pm("23645034", "Ethylene promotes induction of aerenchyma formation and ethanolic fermentation in waterlogged roots of Dendranthema spp. Mol Biol Rep 2013;40(7):4581-90", "Springer / PubMed", ", doi:10.1007/s11033-013-2550-2; 초록 확인"),
 pm("33485066", "Chrysanthemum zawadskil Herbich attenuates dexamethasone-induced muscle atrophy through the regulation of proteostasis and mitochondrial function. Biomed Pharmacother 2021;136:111226", "Elsevier / PubMed", ", doi:10.1016/j.biopha.2021.111226; 초록 확인"),
 pm("24174976", "Inhibitory Effect of Chrysanthemum zawadskii Herbich var. latilobum Kitamura Extract on RANKL-Induced Osteoclast Differentiation. Evid Based Complement Alternat Med 2013;2013:509482", "Hindawi / PubMed", ", PMC3794617, doi:10.1155/2013/509482; 초록 확인"),
 pm("27840652", "The Extract of Chrysanthemum zawadskii var. latilobum Ameliorates Collagen-Induced Arthritis in Mice. Evid Based Complement Alternat Med 2016;2016:3915013", "Hindawi / PubMed", ", PMC5093284, doi:10.1155/2016/3915013; 초록 확인"),
 pm("36278130", "Comparison of CATA and napping to identify sensory properties and drivers of liking for novel blended teas using Dendranthema zawadskii var. latilobum. Food Sci Biotechnol 2022;31(12):1559-1570", "Springer / PubMed", ", PMC9582088, doi:10.1007/s10068-022-01149-1; 초록 확인"),
 pm("31872587", "[Application of ITS2 secondary structure phylogenetic information in DNA barcode identification of Chrysanthemum indicum and its related plants]. Zhongguo Zhong Yao Za Zhi 2019;44(22):4813-4819", "China Journal of Chinese Materia Medica / PubMed", ", doi:10.19540/j.cnki.cjcmm.20190829.110; 초록 확인"),
 pm("38728922", "Exercise-induced signaling activation by Chrysanthemum zawadskii and its active compound, linarin, ameliorates age-related sarcopenia through Sestrin 1 regulation. Phytomedicine 2024;129:155695", "Elsevier / PubMed", ", doi:10.1016/j.phymed.2024.155695; 초록 확인"),
]
for i, s in enumerate(S, 1):
    s["n"] = i
src = [{"n": s["n"], "title": s["title"], "url": s["url"], "publisher": s["publisher"], "accessed": s["accessed"]} for s in S]

sections = [
{"key": "overview", "title": "한눈에 보기", "body":
"구절초는 국화과(Asteraceae) 국화속(Chrysanthemum)의 여러해살이풀로, 한국·일본·중국에 널리 자란다[5, 9]. 식약처 「식품원료 목록」에는 학명이 'Chrysanthemum zawadskii Herbich var. latilobum (Maxim.) Kitamura / Chrysanthemum zawadskii var. coreanum'으로 두 변종이 함께 적혀 있다[1]. 논문에서는 같은 식물을 Dendranthema zawadskii(var. latilobum)라는 이명으로도 쓰고, 영문 논문은 한국 이름을 'Gu-Jeol-Cho'·'Gu-Jul-Cho'·'Gujulcho' 등으로 옮긴다[19, 10, 26, 31].\n\n"
"식품원료로서 구절초는 '제한적사용' 원료다[1]. 목록의 구절초 원료명 12개 행이 모두 '제한적사용가능부위 : 전초※(구절초)' 조건을 달고 있다[1]. 건강기능식품 쪽에는 줄기·잎을 쓰는 개별인정 원료 '구절초추출물(기능성원료인정제2021-12호)'이 사용가능으로 올라 있고, 고시형 원료는 없다[2]. 이 개별인정 원료의 인정 기능성 문구는 원문을 열지 못해 확인하지 못함.\n\n"
"연구의 대표 지표성분은 리나린(linarin)이고, 클로로겐산 같은 페놀산도 보고된다[5, 10, 12]. 사람 대상으로는 가벼운 무릎 골관절염 환자 121명의 12주 무작위 위약대조 시험이 있으며, 같은 시험 참가자의 유전형 분석에서는 골관절염 관련 유전자의 SNP 3개가 통증 점수 변화와 관련되었다[6]. 그 밖의 효과 보고는 대부분 세포·동물 실험이다[4, 9, 30]."},
{"key": "history", "title": "이용의 역사", "body":
"구절초는 한국에서 폐렴·기관지염·기침·감기·인두염·방광 질환·위장 질환·고혈압 등에 쓰던 민간 약초로 소개된다[26, 25]. 아시아에서 차로 마셔 왔고, 간을 보호하고 혈액순환을 돕는 용도, 특히 부인과 용도로 이용되었다는 기술도 있다[5]. 음료·차와 여러 염증성 질환의 민간요법으로 쓰였다는 설명도 같은 맥락이다[32]. '구절초'라는 이름의 유래를 설명한 공공기관 자료는 확인하지 못함.\n\n"
"성분 연구는 2000년대 초에 시작되어, 2002년 논문은 리나린을 이 식물의 주요 활성 성분으로 보고 대식세포에서의 작용을 살폈다[26]. 2007년에는 뿌리에서 폴리아세틸렌과 페놀 화합물이, 2012년에는 지상부에서 새로운 세스퀴테르펜 락톤(zawadskinolide A–F)이 분리되었다[20, 21, 19]. 2013년 이후에는 파골세포 분화 억제, 콜라겐 유도 관절염 억제 같은 관절·뼈 관련 동물·세포 연구가 이어졌다[31, 32].\n\n"
"이 흐름은 줄기·잎 70% 에탄올 추출물을 쓴 2021년 무릎 골관절염 인체시험으로 이어졌다[4]. 같은 해 식약처 목록에 개별인정 원료 '구절초추출물(기능성원료인정제2021-12호)'이 올라 있어, 인정번호로 보아 2021년에 개별인정을 받은 것으로 읽힌다[2]. 구절초를 넣은 블렌딩 차의 소비자 기호도 연구도 나와 있다[33]."},
{"key": "biology", "title": "식물학적 특징", "body":
"구절초는 국화과의 여러해살이풀이다[5]. 한국 자생 이배체 집단 연구에서 구절초(C. zawadskii)는 흰 혀꽃(설상화)을 피워 노란 혀꽃을 피우는 산국(C. boreale)·감국(C. indicum)과 구별되었다[13]. 국화속의 기본 염색체 수는 x = 9이고, 한국 이배체 구절초는 2n = 18이다[13].\n\n"
"구절초에는 이배체(2x)부터 4x·6x·8x·10x까지 배수성 계열이 알려져 있다[14]. 이배체 개체의 꽃밥 속에서 이웃한 꽃가루 어미세포 두 개가 1.1–1.3% 빈도로 합쳐져 2n 꽃가루를 만들며, 이것이 종 안에서 배수체가 생기는 경로로 제안되었다[14]. 중국에 분포하는 C. zawadskii 종복합체는 형태 변이가 큰 7종으로 이루어지며, 초기 플라이오세에 친링–다바산 일대에서 기원해 북쪽으로 퍼진 것으로 추정되었다[17].\n\n"
"꽃 연구용 시료는 9월에 수확한 생화를 썼고, 다른 연구는 8월에 지상부를 채취해 말렸다[9, 10]. 물에 잠긴 조건에서 D. zawadskii는 근연종 D. nankingense보다 침수에 강했으며, 에틸렌 신호로 통기조직을 만드는 반응이 확인되었다[29]. 꽃을 수증기 증류하면 정유가 0.12%(w/w) 얻어지고 색은 연한 녹색이다[22]."},
{"key": "related_species", "title": "근연종과 시료 종 확인", "body":
"같은 속의 다른 식품원료와는 식약처 목록상 지위가 다르다[1, 2]. 국화(C. morifolium)·감국(C. indicum)은 '사용가능부위 : 꽃※(감국), 전초', 산국(C. boreale, 이명 Dendranthema boreale)은 '사용가능부위 : 순, 꽃'의 사용가능 원료인 반면, 구절초는 전초가 제한적사용이다[1, 2]. 제충국·피버퓨는 사용불가다[2].\n\n"
"식약처 목록은 var. latilobum과 var. coreanum을 함께 적고, 개별인정 원료 행은 var. latilobum만 적는다[1, 2]. 아시아의 국화속 식물은 한때 Dendranthema 속으로 나뉘었다가 다시 Chrysanthemum으로 합쳐졌기 때문에, Dendranthema zawadskii와 Chrysanthemum zawadskii는 같은 식물을 가리킨다[13]. 이 문서는 두 변종과 이명을 모두 구절초로 묶어 다루되, 논문 시료가 변종까지 밝힌 경우에는 그대로 적는다[1, 5].\n\n"
"2025년 한 논문은 Dendranthema oreastrum을 'Gu-Jeol-Cho'라고 불렀는데, 이는 식약처 목록의 구절초와 다른 분류군이다[28, 1]. 또 리나린은 구절초뿐 아니라 감국에도 들어 있어 이 성분만으로 종을 가릴 수 없다[27]. ITS2 바코드 연구에서는 C. zawadskii와 C. morifolium이 구별되지 않았다[34]. 반면 흰 꽃의 한국 이배체 구절초는 산국·감국보다 핵 게놈 크기가 대체로 작고 5S rDNA 위치가 달라 세포유전학적으로 구별되었다[13]."},
{"key": "cultivation", "title": "재배와 생산", "body":
"구절초는 농림축산식품부 「특용작물 생산실적」과 통계청 농작물생산통계의 품목 표에 따로 나오지 않아, 국내 재배 면적·생산량 통계는 확인하지 못함. 지리적 표시 등록 품목도 확인하지 못함.\n\n"
"연구 시료의 산지는 국내 여러 곳이다[5, 9, 10, 11]. 관절 연구용 70% 에탄올 추출물의 원료는 전북 정읍산이었고, 꽃 추출물 연구는 정읍의 판매처에서 9월에 수확한 생화를 샀다[5, 9]. 충북에서 2021년 8월에 지상부를 채취해 건조한 시료도 있고, 경북 영천 한약재 시장에서 산 건조 구절초를 쓴 연구도 있다[10, 11].\n\n"
"재배 생리와 관련해서는 침수 반응 연구가 있다[29]. 뿌리가 물에 잠기면 D. zawadskii는 에틸렌이 더 많이 생기고 세포 예정사와 통기조직 형성이 빨라져, 같은 조건의 D. nankingense보다 침수 내성이 컸다[29]. 번식·시비·수확 시기 같은 재배 기술 지침은 공공기관 원문을 열지 못해 확인하지 못함."},
{"key": "processing", "title": "가공과 제품", "body":
"식약처 목록에는 건조구절초·구절초분말·구절초원액·구절초농축액·구절초추출물·구절초추출액·구절초추출분말·구절초추출농축고형분처럼 말리거나 우려 농축한 형태의 원료명이 올라 있다[1]. 꽃·잎·줄기 단위 원료명도 따로 있으나 모두 같은 제한적사용 조건이다[1].\n\n"
"인체시험에 쓴 원료는 구절초 줄기와 잎을 50 °C에서 70% 에탄올로 추출해 감압 농축하고, 말토덱스트린을 더해 50 °C에서 진공 건조한 분말이다[4]. 이 분말을 1일 1정(600 mg, 구절초 추출물 250 mg 함유)으로 12주간 먹게 했다[4]. 전초를 같은 조건으로 추출한 연구용 추출물은 원료 무게 대비 수율이 약 20%였다[5]. 꽃은 에탄올 초음파 추출이나 수증기 증류로 정유를 얻는 연구에 쓰였다[9, 22].\n\n"
"식약처 「식품 등의 생산실적」의 개별인정형 '구절초추출물' 행은 2022년판에서 생산량 8톤·생산액 약 18.6억 원·국내판매액 약 30.6억 원이었다[3]. 2023년판은 생산량 17톤·생산액 약 10.0억 원·국내판매액 약 11.5억 원, 2024년판은 9톤·약 1.4억 원·약 2.0억 원이었다[3]. 2025년판은 생산량 52톤·생산액 약 7.3억 원·국내판매액 약 10.7억 원으로 다시 늘었다[3]."},
{"key": "genetics", "title": "유전체와 종 판별", "body":
"한국에서 채집한 C. zawadskii의 엽록체 게놈은 151,137 bp이고, 대단일복사 영역 83,041 bp, 소단일복사 영역 18,350 bp, 역반복 영역 24,873 bp로 이루어진다[15]. 이 게놈에는 133개 유전자(단백질 암호 87, rRNA 8, tRNA 37, 위유전자 1)가 있고, 앞서 공개된 엽록체 게놈 3개와 비교해 SNP 65–152개가 확인되었다[15]. 중국 시료(Dendranthema zawadskii Herbich)의 엽록체 게놈은 150,995 bp, 유전자 112개로 보고되었다[16].\n\n"
"한국 자생 이배체 구절초 4개 집단의 1C 핵 DNA 양은 2.84–2.94 pg(게놈 크기 약 5.56–5.75 Gbp)로, 산국(3.16–3.44 pg)·감국(2.90–3.41 pg)보다 대체로 작았다[13]. 구절초 집단은 모두 5S rDNA가 6번 염색체 긴팔에, 18S rDNA가 2번·8번 염색체 짧은팔에 있는 같은 유형(cytotype I)이었다[13]. 반면 핵형(염색체 모양 구성)은 같은 집단 안에서도 개체마다 달라 종 판별에 쓰기 어려웠다[13].\n\n"
"국화속 전체 계통 연구에서 중국 종들은 북쪽의 C. zawadskii 무리와 남쪽의 C. indicum 무리로 나뉘었다[18]. 중국 C. zawadskii 종복합체에는 종 분화가 진행 중인 계통이 섞여 있는 것으로 해석되었다[17]. ITS2 바코드로는 C. zawadskii와 C. morifolium을 나누지 못해, 진위 확인에는 여러 표지를 함께 보는 것이 좋다[34, 13]."},
{"key": "safety", "title": "안전성과 사용 조건", "body":
"구절초는 식약처 「식품원료 목록」에서 12개 원료명 행 모두 '제한적사용' 원료이고, 조건 원문은 '제한적사용가능부위 : 전초※(구절초)'이다[1]. 제한적사용 원료의 배합 한도 등 식품공전상 구체적 사용 조건은 원문을 열지 못해 확인하지 못함. 건강기능식품 개별인정 원료 '구절초추출물(기능성원료인정제2021-12호)'은 사용부위가 잎·줄기로 정해져 있다[2]. 이 원료의 1일 섭취량과 섭취 시 주의사항 원문은 확인하지 못함.\n\n"
"사람 대상 안전성 자료는 가벼운 무릎 골관절염(40–75세) 121명의 12주 시험이 대표적이다[4]. 이상사례는 구절초 추출물군 60명 중 3명(5.00%), 위약군 61명 중 4명(6.56%)으로 차이가 없었고, 약물이상반응과 중대한 이상사례는 두 군 모두 없었다[4]. 이 시험은 임신·수유부, 위염·궤양 치료 중인 사람, 시험 원료에 알레르기가 있는 사람을 제외했다[4].\n\n"
"독성 시험은 구절초 단독이 아니라 보리 추출물과 섞은 혼합물로 이루어졌으며, 유전독성이 없었고 설치류 무독성량(NOAEL)은 2000 mg/kg 체중/일이었다[7]. 제브라피시에 꽃 에탄올 추출물을 복강 주사로 3일간 주자 치사 독성이 나타났다는 보고가 있으나, 먹는 경우와 투여 경로가 다르다[9]. 구절초 자체의 알레르기·잔류농약에 관한 공공기관 정보는 확인하지 못함."},
]

compounds = [
 {"name": "Linarin", "name_ko": "리나린(아카세틴-7-O-루티노사이드)", "class": "플라보노이드 배당체(플라본)", "role": "marker", "part": "전초·줄기·잎", "content_text": "건조 전초 70% 에탄올 추출물 기준 22.8 mg/g(3배치, HPLC)[5]; 다른 연구의 HPLC 분석 4성분 중 acacetin-7-O-β-D-rutinoside 농도가 가장 높음(수치는 초록에 없음)[30]", "activity_ko": "논문이 추출물의 지표성분으로 사용[5]; 사람 연골육종세포(SW1353)에서 MMP·ADAMTS 감소(세포)[5]; 대식세포 NO 생성 억제(세포)[26]; 노화 생쥐 근육에서 Sestrin 1 활성화(동물)[35]", "source": [5, 30, 26, 35]},
 {"name": "Chlorogenic acid", "name_ko": "클로로겐산", "class": "페놀산(카페오일퀸산)", "role": "bioactive", "part": "지상부·전초", "content_text": "70% 에탄올 추출물에서 HPLC로 동정·정량(정량값 표는 전문 본문에 없어 확인하지 못함)[11]; 전초 추출물 HPLC 5개 피크 중 하나[5]", "activity_ko": "추출물의 주요 성분 3가지 중 하나로, 대식세포에서 IL-1β 분비 감소(세포)[12]; 보리 추출물과의 혼합물 연구에서 프로락틴 분비를 억제하는 구절초 쪽 성분으로 지목(세포·동물)[8]", "source": [11, 5, 12, 8]},
 {"name": "3,5-Dicaffeoylquinic acid", "name_ko": "3,5-디카페오일퀸산(이소클로로겐산 A)", "class": "페놀산(디카페오일퀸산)", "role": "bioactive", "part": "지상부·전초", "content_text": "70% 에탄올 추출물에서 HPLC로 동정·정량(정량값 확인하지 못함)[11]; 전초·지상부 추출물 HPLC에서 검출[5, 10]", "activity_ko": "대식세포에서 ATP·요산결정에 의한 IL-1β 분비 감소(세포)[12]", "source": [11, 5, 10, 12]},
 {"name": "3,4-Dicaffeoylquinic acid", "name_ko": "3,4-디카페오일퀸산(이소클로로겐산 B)", "class": "페놀산(디카페오일퀸산)", "role": "bioactive", "part": "지상부·전초", "content_text": "전초 70% 에탄올 추출물 HPLC에서 검출(함량 미기재)[5]; 지상부 에탄올 추출물 340 nm HPLC에서 검출[10]", "activity_ko": "확인하지 못함", "source": [5, 10]},
 {"name": "Luteolin", "name_ko": "루테올린", "class": "플라본", "role": "bioactive", "part": "꽃·지상부", "content_text": "지상부 70% 에탄올 추출물에서 HPLC 정량(365 nm, 정량값 확인하지 못함)[11]; 꽃 에탄올 추출물의 주요 플라보노이드 3종 중 하나[9]", "activity_ko": "미세아교세포에서 NO·IL-1β·iNOS 감소, 신경세포 글루탐산 독성 완화(세포)[9]", "source": [11, 9, 10]},
 {"name": "Quercetin", "name_ko": "퀘르세틴", "class": "플라보놀", "role": "bioactive", "part": "꽃", "content_text": "꽃 에탄올 추출물의 주요 플라보노이드 3종 중 하나(함량 미기재)[9]", "activity_ko": "DPPH IC50 9.24 μM·ABTS IC50 6.72 μM, 미세아교세포 염증 매개체 감소(세포)[9]", "source": [9]},
 {"name": "Apigenin", "name_ko": "아피제닌", "class": "플라본", "role": "bioactive", "part": "지상부", "content_text": "지상부에서 분리[19]; 지상부 에탄올 추출물 HPLC에서 검출[10]", "activity_ko": "대식세포 NO 생성 억제 IC50 66.15 μM(세포)[19]", "source": [19, 10]},
 {"name": "Nepetin", "name_ko": "네페틴(6-메톡시루테올린)", "class": "플라본", "role": "bioactive", "part": "지상부", "content_text": "지상부에서 분리[19, 24]", "activity_ko": "대식세포 NO 생성 억제 IC50 35.44 μM(세포)[19]; 호염기구 세포에서 히스타민 방출·칼슘 유입 억제(세포)[24]", "source": [19, 24]},
 {"name": "Acacetin", "name_ko": "아카세틴", "class": "플라본", "role": "bioactive", "part": "뿌리·지상부", "content_text": "뿌리에서 분리[21]; 지상부 에탄올 추출물 HPLC에서 검출[10]", "activity_ko": "항균·항진균 활성을 원판 확산법으로 평가(시험관)[21]", "source": [21, 10]},
 {"name": "Eriodictyol 7-O-glucuronide", "name_ko": "에리오딕티올-7-O-β-D-글루쿠로나이드", "class": "플라바논 배당체", "role": "bioactive", "part": "확인하지 못함(원문 초록에 부위 없음)", "content_text": "var. latilobum에서 분리(함량 미기재)[25]", "activity_ko": "사람 호염기구 세포(KU812F)에서 FcεRI 발현과 Syk·Lyn·ERK 신호 억제(세포)[25]", "source": [25]},
 {"name": "Zawadskinolide F", "name_ko": "자와드스키놀라이드 F", "class": "세스퀴테르펜 락톤(게르마크라놀라이드)", "role": "bioactive", "part": "지상부", "content_text": "지상부에서 새로 분리된 zawadskinolide A–F 6종 중 하나[19]", "activity_ko": "대식세포 NO 생성 억제 IC50 91.32 μM(세포)[19]", "source": [19]},
 {"name": "Dendrazawayne A", "name_ko": "덴드라자웨인 A", "class": "C14 폴리아세틸렌", "role": "bioactive", "part": "뿌리", "content_text": "뿌리에서 새로 분리[20]", "activity_ko": "백선균(Trichophyton)에 MIC 5–10 μg/mL(시험관)[20]", "source": [20]},
 {"name": "Borneol", "name_ko": "보르네올", "class": "모노테르펜 알코올(정유 성분)", "role": "bioactive", "part": "꽃(정유)", "content_text": "꽃 정유(수율 0.12% w/w) 휘발 성분 중 12.96%로 가장 많음(GC/MS)[22]", "activity_ko": "확인하지 못함", "source": [22]},
 {"name": "Camphor", "name_ko": "캠퍼(장뇌)", "class": "모노테르펜 케톤(정유 성분)", "role": "bioactive", "part": "꽃(정유)", "content_text": "꽃 정유 휘발 성분 중 10.54%(GC/MS)[22]; 다른 꽃 정유 분석에서는 88성분 중 모노테르펜이 68.82%[23]", "activity_ko": "꽃 정유 전체로 MRSA 생장·바이오필름 형성 억제(시험관)[23]", "source": [22, 23]},
]

assays = [
 {"role": "literature", "compound": "Linarin", "compound_ko": "리나린", "part": "구절초(var. latilobum) 건조 전초 70% 에탄올 추출물(전북 정읍산 원료)",
  "content": "추출물 기준 22.8 mg/g, 3배치 유사도 0.99 이상[5]", "method": "HPLC",
  "conditions": {"instrument": "Agilent 1260 HPLC", "column": "Phenomenex Kinetex C18(4.6 × 250 mm, 5 μm)", "mobile_phase": "A: 0.025 M KH2PO4 수용액(인산으로 pH 3.0), B: 아세토니트릴", "gradient": "0–12분 15–25% B; 12–20분 25–41% B; 20–30분 41–90% B; 이후 15% B로 5분 평형", "flow": "1.0 mL/min", "temp": "", "detection": "", "injection": "", "sample_prep": "추출물을 50% 에탄올에 녹여 분석", "standard": "리나린 표준품(순도 97.63%); 함께 쓴 표준품: 클로로겐산(96.67%)·이소클로로겐산 A·B(98.0%)·C(98%)", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "논문이 리나린을 추출물의 지표성분(marker compound)으로 명시하고 배치 간 일관성 확인에 썼다; 검출 파장·검량선·검출한계는 전문에 적혀 있지 않음[5]",
  "source": [5], "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC7762971/", "source_kind": "paper"},
 {"role": "literature", "compound": "Chlorogenic acid", "compound_ko": "클로로겐산(같은 조건에서 3,5-디카페오일퀸산·루테올린 동시 분석)", "part": "구절초 건조물(시장 구입, 전문가 감정) 70% 에탄올 추출물",
  "content": "정량값은 논문 표에 있으나 본문에서 확인하지 못함; 머무름 시간 9.46분(클로로겐산)·19.89분(3,5-디카페오일퀸산)·27.87분(루테올린)[11]", "method": "HPLC-DAD",
  "conditions": {"instrument": "Dionex UltiMate 3000(이원 펌프·자동주입기·칼럼 오븐·DAD)", "column": "Waters XBridge C18(250 × 4.60 mm, 5 μm)", "mobile_phase": "A: 0.1% 포름산 수용액, B: 아세토니트릴", "gradient": "5–12% B 0–5분; 12–15% B 5–7분; 15% B 7–12분; 15–20% B 12–14분; 20% B 14–20분; 20–60% B 20–35분; 60–90% B 35–40분; 90% B 40–45분; 90–95% B 45–46분; 5% B 46–60분", "flow": "1.0 mL/min", "temp": "40 °C", "detection": "320 nm(클로로겐산·3,5-디카페오일퀸산), 365 nm(루테올린)", "injection": "5 μL", "sample_prep": "건조 구절초 30 g을 70% 에탄올 300 mL로 40 °C·100 rpm 24시간 진탕 추출, 여과·농축·동결건조(수율 13.83%)", "standard": "메탄올 저장액 1 mg/mL; 검량 범위 클로로겐산·3,5-디카페오일퀸산 25–400 μg/mL, 루테올린 1.25–20.00 μg/mL", "linearity": "r² ≥ 0.9997(5농도, 3반복)", "lod": "", "loq": "", "recovery": ""},
  "rationale": "구절초 추출물의 주요 성분으로 클로로겐산·3,5-디카페오일퀸산이 반복 보고되어 품질 지표 후보가 된다[11, 12]; 정량 결과 표 값은 전문 본문에서 확인하지 못함",
  "source": [11, 12], "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC6805551/", "source_kind": "paper"},
]

d = {
 "slug": "chrysanthemum-zawadskii",
 "name_ko": "구절초",
 "name_en": "Chrysanthemum zawadskii (Korean name Gu-Jeol-Cho)",
 "scientific_name": "Chrysanthemum zawadskii Herbich var. latilobum (Maxim.) Kitam.",
 "aliases": ["구절초", "Gu-Jeol-Cho", "Gu-Jul-Cho", "Gujulcho", "Chrysanthemum zawadskii Herbich", "Chrysanthemum zawadskii var. latilobum", "Chrysanthemum zawadskii var. coreanum", "Dendranthema zawadskii", "Dendranthema zawadskii var. latilobum"],
 "sections": sections,
 "compounds": compounds,
 "markers": [],
 "assays": assays,
 "nutrients": [],
 "production": [],
 "world": [],
 "gi": [],
 "orgs": [],
 "sources": src,
}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
print("ok", len(src))
