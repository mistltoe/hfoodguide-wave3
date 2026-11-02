import json, pathlib
HERE = pathlib.Path(__file__).resolve().parent.parent
ACC = "2026-11-02"
def pm(pmid): return f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
S = [
 ("식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 첨차잎·첨차추출물·첨차추출분말", "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "식품의약품안전처", "2026-10-13"),
 ("Quantitative and fingerprint analyses of Chinese sweet tea plant (Rubus suavissimus S. Lee). J Agric Food Chem 2009;57(3):1076-83 (PMID 19138116, PMC2680688, doi:10.1021/jf8029397)", pm(19138116), "Journal of Agricultural and Food Chemistry (PubMed)", ACC),
 ("Purification of a water extract of Chinese sweet tea plant (Rubus suavissimus S. Lee) by alcohol precipitation. J Agric Food Chem 2009 (PMID 19419169, PMC2711552, doi:10.1021/jf900269r)", pm(19419169), "Journal of Agricultural and Food Chemistry (PubMed)", ACC),
 ("Rubus chingii var. suavissimus alleviates high-fat diet-induced lipid metabolism disorder via modulation of the PPARs/SREBP pathway in Syrian golden hamsters. J Nat Med 2021 (PMID 34120311, doi:10.1007/s11418-021-01536-8)", pm(34120311), "Journal of Natural Medicines (PubMed)", ACC),
 ("Assembly and comparative analysis of the complete mitogenome of Rubus chingii var. suavissimus. Front Plant Sci 2024;15:1504687 (PMID 39764230, PMC11701164, doi:10.3389/fpls.2024.1504687)", pm(39764230), "Frontiers in Plant Science (PubMed)", ACC),
 ("[Comparative analysis of plastomes of Rubus chingii and R. chingii var. suavissimus]. Zhongguo Zhong Yao Za Zhi 2024;49(6):1506-1516 (PMID 38621934, doi:10.19540/j.cnki.cjcmm.20231115.105)", pm(38621934), "China Journal of Chinese Materia Medica (PubMed)", ACC),
 ("Comparative metabolome and transcriptome analysis revealed the accumulative mechanism of rubusoside in Chinese sweet tea. J Agric Food Chem 2024;72(44):24539-24551 (PMID 39442010, doi:10.1021/acs.jafc.4c07127)", pm(39442010), "Journal of Agricultural and Food Chemistry (PubMed)", ACC),
 ("Diterpenoid UDP-glycosyltransferases from Chinese sweet tea and Ashitaba complete the biosynthesis of rubusoside. Mol Plant 2018;11(10):1308-1311 (PMID 29885474, doi:10.1016/j.molp.2018.05.010)", pm(29885474), "Molecular Plant (PubMed)", ACC),
 ("Analysis of rubusoside and related compounds in tenryocha extract sweetener. Shokuhin Eiseigaku Zasshi 2002;43(4):250 (PMID 12436720, doi:10.3358/shokueishi.43.250)", pm(12436720), "Journal of the Food Hygienic Society of Japan (PubMed)", ACC),
 ("A randomized, double-blind, placebo-controlled study of ten-cha (Rubus suavissimus) on house dust mite allergic rhinitis. Auris Nasus Larynx 2011;38(5):600-7 (PMID 21216122, doi:10.1016/j.anl.2010.11.017)", pm(21216122), "Auris Nasus Larynx (PubMed)", ACC),
 ("Rubusuaviins A-F, monomeric and oligomeric ellagitannins from Chinese sweet tea and their alpha-amylase inhibitory activity. Chem Pharm Bull 2007;55(9):1325 (PMID 17827756, doi:10.1248/cpb.55.1325)", pm(17827756), "Chemical & Pharmaceutical Bulletin (PubMed)", ACC),
 ("New ellagitannins from Tiencha and their inhibitory activity against dental plaque. J Nat Med 2017 (PMID 28455553, doi:10.1007/s11418-017-1090-9)", pm(28455553), "Journal of Natural Medicines (PubMed)", ACC),
 ("[Studies on the chemical constituents of Rubus suavissimus S. Lee]. Zhong Yao Cai 2007 (PMID 17944189)", pm(17944189), "Zhong Yao Cai (PubMed)", ACC),
 ("Uncovering the phytochemical diversity and anti-diabetic potential of Rubus suavissimus leaf using conventional and novel extraction strategies. Food Chem 2026;513:148983 (PMID 41904866, doi:10.1016/j.foodchem.2026.148983)", pm(41904866), "Food Chemistry (PubMed)", ACC),
 ("Characterization and purification of hypoglycemic components from Rubus suavissimus leaf by affinity ultrafiltration, molecular docking, and macroporous resin. J Chromatogr B 2025;1268:124830 (PMID 41175510, doi:10.1016/j.jchromb.2025.124830)", pm(41175510), "Journal of Chromatography B (PubMed)", ACC),
 ("Microwave-assisted extraction of rubusoside from Rubus chingii var. suavissimus leaves using a recyclable ternary deep eutectic solvent. Foods 2026;15(14):2545 (PMID 42511291, PMC13408828, doi:10.3390/foods15142545)", pm(42511291), "Foods (PubMed)", ACC),
 ("Improvement of obesity phenotype by Chinese sweet leaf tea (Rubus suavissimus) components in high-fat diet-induced obese rats. J Agric Food Chem 2010 (PMID 21138267, doi:10.1021/jf103497p)", pm(21138267), "Journal of Agricultural and Food Chemistry (PubMed)", ACC),
 ("Gallic acid is partially responsible for the antiangiogenic activities of Rubus leaf extract. Phytother Res 2006 (PMID 16835875, doi:10.1002/ptr.1966)", pm(16835875), "Phytotherapy Research (PubMed)", ACC),
 ("Effect of rubusoside, a natural sucrose substitute, on Streptococcus mutans biofilm cariogenic potential and virulence gene expression. Appl Environ Microbiol 2020 (PMID 32503907, PMC7414950, doi:10.1128/AEM.01012-20)", pm(32503907), "Applied and Environmental Microbiology (PubMed)", ACC),
 ("Anti-cariogenic characteristics of rubusoside. Biotechnol Bioprocess Eng 2019 (PMID 32218683, PMC7090897, doi:10.1007/s12257-018-0408-0)", pm(32218683), "Biotechnology and Bioprocess Engineering (PubMed)", ACC),
 ("Inhibition of human GLUT1 and GLUT5 by plant carbohydrate products; insights into transport specificity. Sci Rep 2015;5:12804 (PMID 26306809, PMC4549712, doi:10.1038/srep12804)", pm(26306809), "Scientific Reports (PubMed)", ACC),
 ("Identification of plants that inhibit lipid droplet formation in liver cells: Rubus suavissimus leaf extract protects mice from high-fat diet-induced fatty liver. Evid Based Complement Alternat Med 2016 (PMID 27429636, PMC4939186, doi:10.1155/2016/4282758)", pm(27429636), "eCAM (PubMed)", ACC),
 ("Chinese sweet leaf tea (Rubus suavissimus) mitigates LPS-induced low-grade chronic inflammation and reduces the risk of metabolic disorders in a C57BL/6J mouse model. J Agric Food Chem 2020;68(1):138-146 (PMID 31873011, doi:10.1021/acs.jafc.9b05975)", pm(31873011), "Journal of Agricultural and Food Chemistry (PubMed)", ACC),
 ("Mechanistic insights into myricetin-regulated autophagy via the PI3K/Akt and PINK1/Parkin pathway in diabetic kidney disease treatment. J Ethnopharmacol 2025 (PMID 40957544, doi:10.1016/j.jep.2025.120613)", pm(40957544), "Journal of Ethnopharmacology (PubMed)", ACC),
 ("[Anti-allergic effects of Rubus suavissimus extract]. Zhong Yao Cai 2008 (PMID 18826149)", pm(18826149), "Zhong Yao Cai (PubMed)", ACC),
 ("Development of a multifunction set yogurt using Rubus suavissimus S. Lee (Chinese sweet tea) extract. Foods 2020;9(9):1163 (PMID 32846883, PMC7555928, doi:10.3390/foods9091163)", pm(32846883), "Foods (PubMed)", ACC),
 ("Rubusoside: a natural and functional sweetener — an integrated review of phytochemistry, bioactivities, and solubilization. Nat Prod Res 2026 (PMID 42800069, doi:10.1080/14786419.2026.2737994)", pm(42800069), "Natural Product Research (PubMed)", ACC),
 ("Dynamic characteristics of sweetness and bitterness and their correlation with chemical structures for six steviol glycosides. Food Res Int 2021 (PMID 34980386, doi:10.1016/j.foodres.2021.110848)", pm(34980386), "Food Research International (PubMed)", ACC),
 ("De novo biosynthesis of rubusoside and rebaudiosides in engineered yeasts. Nat Commun 2022 (PMID 35650215, PMC9160076, doi:10.1038/s41467-022-30826-2)", pm(35650215), "Nature Communications (PubMed)", ACC),
 ("Characterization of a lactic acid bacterium-derived β-glucosidase for the production of rubusoside from stevioside. Enzyme Microb Technol 2021 (PMID 34798448, doi:10.1016/j.enzmictec.2021.109939)", pm(34798448), "Enzyme and Microbial Technology (PubMed)", ACC),
 ("Inhibitions of histamine release and prostaglandin E2 synthesis by mangosteen, a Thai medicinal plant. Biol Pharm Bull 2002;25:1137 (PMID 12230104, doi:10.1248/bpb.25.1137)", pm(12230104), "Biological & Pharmaceutical Bulletin (PubMed)", ACC),
 ("Rubus suavissimus S. Lee extract increases early adipogenesis in 3T3-L1 preadipocytes. J Nat Med 2010 (PMID 21082272, doi:10.1007/s11418-010-0480-z)", pm(21082272), "Journal of Natural Medicines (PubMed)", ACC),
 ("Optimizing trilobatin production via screening and modification of glycosyltransferases. Molecules 2024;29(3):643 (PMID 38338387, PMC10856287, doi:10.3390/molecules29030643)", pm(38338387), "Molecules (PubMed)", ACC),
 ("Non-sugar sweetener rubusoside alleviates lipid metabolism disorder in vivo and in vitro by targeting PPARγ/α, Lgals3, and Mknk2. J Agric Food Chem 2024 (PMID 39508235, doi:10.1021/acs.jafc.4c06018)", pm(39508235), "Journal of Agricultural and Food Chemistry (PubMed)", ACC),
]
sources = [{"n": i+1, "title": t, "url": u, "publisher": p, "accessed": a} for i,(t,u,p,a) in enumerate(S)]

sections = [
 {"key":"overview","title":"한눈에 보기","body":
 "첨차(Rubus suavissimus S. Lee)는 장미과 산딸기속의 떨기나무로, 잎을 우린 차가 단맛을 내기 때문에 중국에서 톈차(甜茶) 또는 Chinese sweet tea라 불린다[2, 3]. 여러 논문은 이 식물을 Rubus chingii var. suavissimus (S. K. Lee) L. T. Lu라는 변종 이름과 같은 것으로 함께 적는다[4, 16].\n\n"
 "식품원료로서 첨차는 식약처 「식품원료 목록」에 첨차잎·첨차추출물·첨차추출분말 3개 원료명(이명 '텐차')으로 올라 있고, 모두 '사용가능' 원료다[1]. 사용 조건은 '사용가능부위 : 잎'이어서 잎과 그 추출물만 식품에 쓸 수 있다[1]. 이 종을 원재료로 하는 건강기능식품 고시형 원료는 목록에서 확인하지 못했다[1].\n\n"
 "잎의 단맛은 디테르펜 배당체 루부소사이드에서 오며, 잎 무게의 약 5%를 차지한다고 보고되었다[2]. 효과 연구는 대부분 세포·동물 실험이고, 사람 시험으로는 집먼지진드기 알레르기 비염 환자에게 4주간 추출물을 먹인 무작위 대조 시험이 있으나 위약과 유의한 차이가 없었다[10]."},
 {"key":"history","title":"이용의 역사","body":
 "첨차 잎은 중국 광시·구이저우 지역 주민이 끓는 물에 우려 음료로 마셔 온 재료다[3]. 중국 남부에서는 고혈압·당뇨·동맥경화 완화, 신장 건강 유지, 기침 완화를 위한 민간요법으로도 쓰였다고 한다[3]. 광시 지역의 전통 민족의학에서 당뇨와 그 합병증 관리에 써 왔다는 기술도 있다[24].\n\n"
 "일본에서는 텐차(ten-cha)가 알레르기 비염에 가장 흔히 쓰이는 보완대체요법으로 소개되었고, 물 추출물이 항알레르기 생약으로 쓰여 왔다는 기록이 있다[10, 31]. 체중 관리를 위해 칼로리 섭취를 줄이는 음료로 쓰인다는 기술도 있다[32]. 일본에서는 첨차 잎 추출물이 천연 감미료(텐료차 추출물)로 유통되어, 식품첨가물로서 품질·안전성을 평가하는 연구가 2002년에 보고되었다[9].\n\n"
 "주된 단맛 성분 루부소사이드는 최근 설탕 대체 감미료이자 파클리탁셀·커큐민 같은 물에 잘 녹지 않는 물질의 가용화제로 함께 검토되고 있다[27]."},
 {"key":"biology","title":"식물학적 특징","body":
 "첨차는 장미과 산딸기속에 속하며, 중국 남부 광시성의 언덕과 비탈에 주로 분포한다고 기술된다[5]. 중국 남서부에 널리 재배되는 떨기나무로 소개되며, 잎이 차와 약재로 쓰인다[2]. 같은 종(Rubus chingii)의 기본 변종과는 잎의 성질이 크게 다르며, 첨차 잎에는 단맛이 강하고 열량이 낮은 성분이 들어 있다[5].\n\n"
 "잎의 화학 성분은 갈로탄닌·엘라지탄닌·플라보노이드·디테르펜 네 무리가 주를 이룬다[2]. 단맛을 내는 디테르펜 배당체로는 루부소사이드 외에 수아비오사이드 A·B·G·H·I·J가 있고, 쓴맛을 내는 수아비오사이드 C1·D2·F도 함께 들어 있다[3]. 구이저우의 한 재배 농장에서 한 해 동안 거둔 잎 14점의 크로마토그램 지문은 서로 0.98 이상 비슷했으며, 루부소사이드 함량은 계절에 따라 비교적 안정적이었고 6–7월 잎이 약간 높았다[2].\n\n"
 "꽃·열매의 형태와 정확한 자생 범위는 공식 식물지 원문을 열지 못해 확인하지 못함."},
 {"key":"related_species","title":"근연종과 혼동 주의","body":
 "논문에서 첨차는 Rubus suavissimus S. Lee와 Rubus chingii var. suavissimus (S. K. Lee) L. T. Lu 두 이름으로 함께 쓰인다[4]. 엽록체 유전체 비교에서 첨차와 R. chingii 기본 변종은 100% 지지도로 함께 묶였고, 가장 가까운 다른 종은 R. trianthus였다[6]. 두 분류군의 엽록체 유전체에서 rps16-trnQ-psbK, trnR-atpA, trnT-trnL 세 구간이 변이가 커서 식별 표지 후보로 제시되었다[6].\n\n"
 "식약처 「식품원료 목록」은 첨차(잎)와 별도로 Rubus chingii Hu를 '장엽복분자열매'(사용가능부위 : 열매)로 올려 두고 있어, 같은 종 계열이라도 식품원료로 쓰는 부위와 원료명이 다르다[1]. 복분자·산딸기·라즈베리·블랙베리 같은 다른 산딸기속 원료는 주로 열매를 쓰는 원료이므로 첨차 잎의 성분·효능 자료와 섞지 않아야 한다[1].\n\n"
 "영어 'sweet tea'나 한자 '甜茶'는 다른 식물에도 쓰인다[33]. 예를 들어 디하이드로칼콘 감미 성분 트릴로바틴을 내는 '중국 전통 단차' 식물은 루부소사이드를 내는 첨차와 다른 감미 원료로 연구된다[33]. 일본의 텐료차 추출물 연구도 제품의 TLC·HPLC 양상을 첨차 잎 열수 추출물과 비교해 원료가 첨차 잎임을 확인했다[9]."},
 {"key":"cultivation","title":"재배와 생산","body":
 "중국에서는 첨차가 대규모로 재배되고 있으며, 그 제품이 일본·미국 등으로 퍼졌다고 보고되었다[5]. 성분 연구에 쓰인 잎은 구이저우성의 재배 농장에서 한 생육기 동안 거둔 것이었고, 같은 장소에서 거둔 잎은 성분 지문이 매우 비슷해 품질이 안정적이었다[2]. 저장성 이우의 산딸기 재배 기지에서 첨차 잎을 채취해 유전체를 분석한 연구도 있다[5].\n\n"
 "수확 시기에 따라 잎 성분이 달라지는데, 같은 농장 잎 14점에서 갈산은 약 12%, 스테비올모노사이드는 29%의 변동을 보였다[2]. 갈산을 최대로 얻으려면 3월 잎이 전체 혼합 잎보다 약 23% 높았다는 보고가 있다[2].\n\n"
 "국내 재배 면적·생산량은 통계청·농림축산식품부 자료에서 확인하지 못함. 국내 지리적 표시 등록도 확인하지 못함."},
 {"key":"processing","title":"가공과 제품","body":
 "전통적으로 첨차 잎은 끓는 물에 우리거나 달여 마신다[3]. 산업용 조추출물은 말린 잎을 물(약 1:15 w/v)에 1시간 불린 뒤 60분 끓여 거르고 농축·분무건조해 만든다[3]. 이 물 추출물에는 다당류가 약 11% 들어 있으며, 에탄올 70–80%로 침전시키면 다당류를 없애면서 다섯 지표성분을 정제할 수 있었다[3].\n\n"
 "루부소사이드를 더 많이 얻기 위한 추출법도 연구되었다[15, 16]. 최적화한 친환경 추출에서 폴리페놀 91.89 ± 2.39 mg/g, 루부소사이드 47.03 ± 1.45 mg/g을 얻었고, 흡착수지 정제 후 각각 2.63배·2.32배로 높아졌다[15]. 마이크로파와 3성분 공융용매를 함께 쓴 추출에서는 루부소사이드 수율이 7.89 ± 0.25%였다[16]. 일본에서 유통된 텐료차 추출 감미료 제품의 루부소사이드 농도는 8.65%였다[9].\n\n"
 "식품 응용으로는 요구르트에 첨차 추출물을 0.25–1% 넣은 연구가 있으며, 0.5% 첨가가 향과 전반적 기호도에서 가장 높은 점수를 받았다[26]. 루부소사이드는 식물 추출 외에 스테비오사이드를 효소로 바꾸거나 효모에서 새로 합성하는 방법으로도 만들어진다[29, 30]. 국내 건강기능식품 생산실적에서 첨차 원료 품목은 확인하지 못함."},
 {"key":"genetics","title":"유전체와 단맛 생합성","body":
 "첨차의 미토콘드리아 유전체는 PacBio HiFi 서열로 처음 조립되었으며, 길이 432,483 bp의 고리 구조에 단백질 암호 유전자 34개·tRNA 20개·rRNA 3개가 있었다[5]. GC 함량은 43.89%였고, 엽록체에서 옮겨 온 서열 55쌍(총 56,913 bp)이 미토콘드리아 유전체의 13.16%를 차지했다[5]. 엽록체 유전체는 큰 단일복사 구역·작은 단일복사 구역·역반복 구역 두 개의 전형적 네 부분 구조였다[6].\n\n"
 "루부소사이드 생합성에서는 스테비올에 포도당을 붙이는 UDP-당전이효소가 핵심이며, 첨차와 신선초에서 찾은 디테르펜 당전이효소로 루부소사이드 생합성 경로를 완성했다는 보고가 있다[8]. 단맛 잎과 쓴맛 잎을 가진 두 산딸기속 분류군을 비교한 연구에서는 서로 매우 비슷한 당전이효소 유전자 세 쌍이 모두 스테비올을 배당화할 수 있어, 첨차의 루부소사이드 축적은 이 유전자들의 전사 조절 차이에서 비롯된 것으로 보였다[7]. 이 연구에서 단맛 잎에는 스테비올 배당체가, 쓴맛 잎에는 고쇼노사이드가 주로 쌓였다[7]."},
 {"key":"safety","title":"안전성과 주의","body":
 "식약처 「식품원료 목록」은 첨차를 잎에 한해 '사용가능' 원료로 분류하며, 제한적 사용 조건은 없다[1]. 이 종에 대한 식약처 고시형 원료의 섭취 시 주의사항은 없다[1]. 첨차에 대한 공공기관의 알레르기·잔류농약·독성 성분 정보는 확인하지 못함.\n\n"
 "사람 시험으로는 집먼지진드기 알레르기 비염 환자 89명(첨차군 47명, 위약군 42명)이 첨차 추출물 400 mg 또는 위약을 하루 3캡슐로 4주간 매일 먹은 무작위 이중맹검 시험이 있다[10]. 첨차군에서 재채기·콧물·코막힘 점수가 더 나아지는 경향은 있었으나 위약과 유의한 차이가 없었고, 삶의 질 점수도 유의하게 좋아지지 않았다[10]. 이 시험의 이상반응 내용은 초록에서 확인하지 못함.\n\n"
 "루부소사이드는 쓴 뒷맛이 있어 스테비오사이드와 함께 즉각적인 쓴맛과 오래 남는 뒷맛을 보였다[28]. 혈당·지질 개선, 충치균 억제 같은 보고는 세포·동물 실험 결과이므로 사람에게 같은 효과가 있다고 볼 수 없다[17, 19, 22, 34]. 잎 추출물의 항알레르기 작용(생쥐 귀 부종·모세혈관 투과성 감소)과 저농도 내독소로 유발한 만성 염증 완화도 동물 실험 결과다[23, 25]. 장기 섭취 독성 시험 결과는 확인하지 못함."},
]

def C(name, ko, cls, role, part, content, act, src):
    return {"name":name,"name_ko":ko,"class":cls,"role":role,"part":part,"content_text":content,"activity_ko":act,"source":src}
compounds = [
 C("Rubusoside","루부소사이드","디테르펜 배당체(스테비올 배당체)","marker","잎",
   "잎 평균 약 5%(구이저우 재배 잎 14점, HPLC-PDA; 다섯 지표성분 합계 5.9% w/w 중 82.5%)[2]; 최적 추출 47.03 ± 1.45 mg/g[15]; 마이크로파·공융용매 추출 7.89 ± 0.25%[16]; 일본 텐료차 추출 감미료 제품 8.65%[9]",
   "0.025% 농도에서 설탕보다 약 115배 달다[3]; 시험관에서 충치균(S. mutans) 바이오필름 형성과 산 생성 억제[19, 20]; 사람 GLUT1·GLUT5 억제(시험관)[21]; 고지방식 생쥐에서 체중 증가·지질 이상 완화(동물)[34]",
   [2,3,9,15,16,19,20,21,34]),
 C("Steviolmonoside","스테비올모노사이드","디테르펜 배당체","marker","잎",
   "잎 평균 0.71% w/w, 시료 간 변동 29%(HPLC-PDA)[2]",
   "루부소사이드와 함께 잎의 단맛을 내는 성분으로 지표성분에 포함됨[2]",[2]),
 C("Gallic acid","갈산","페놀산","marker","잎",
   "잎 평균 0.13% w/w, 시료 간 변동 약 12%(HPLC-PDA)[2]",
   "첨차 잎 물 추출물의 혈관신생 억제 활성 성분의 하나로 확인됨(사람 조직 기반 시험관 시험)[18]",[2,18]),
 C("Ellagic acid","엘라그산","페놀산(엘라지탄닌 구성 단위)","marker","잎",
   "다섯 지표성분 합계(평균 5.9% w/w)의 12.0%(HPLC-PDA)[2]",
   "갈산·루부소사이드와 함께 비만 쥐 시험에 쓰인 정제 성분 혼합물(GER)의 하나로, 혼합물이 체중 증가를 22% 줄임(동물)[17]",[2,17]),
 C("Rutin","루틴","플라보놀 배당체","marker","잎",
   "다섯 지표성분 합계(평균 5.9% w/w)의 1.9%(HPLC-PDA)[2]",
   "잎 추출물에서 α-글루코시데이스 억제 후보 성분으로 동정됨(시험관)[15]",[2,15]),
 C("Steviol","스테비올","디테르펜(카우렌계)","bioactive","잎",
   "잎에서 ent-13-hydroxy-kaur-16-en-19-oic acid로 분리(함량 확인하지 못함)[13]; 잎 추출물에서 동정[15]",
   "α-글루코시데이스 억제 후보 성분으로 제시됨(시험관)[15]",[13,15]),
 C("Panicloside IV","파니클로사이드 IV","디테르펜 배당체","bioactive","잎 추출 감미료",
   "텐료차 추출 감미료 제품에서 분리(함량 확인하지 못함)[9]",
   "제품의 미량 성분으로 확인됨, 활성 시험은 확인하지 못함[9]",[9]),
 C("Corilagin","코릴라진","엘라지탄닌","bioactive","잎",
   "비표적 대사체 분석에서 주요 성분으로 처음 확인(함량 확인하지 못함)[14]",
   "추출물이 α-글루코시데이스 억제와 INS-1E 세포 인슐린 분비 촉진을 보임(시험관)[14]",[14]),
 C("Rubusuaviin A","루부수아비인 A","엘라지탄닌","bioactive","말린 잎",
   "잎 수성 아세톤 추출물에서 분리된 신규 화합물(함량 확인하지 못함)[11]",
   "엘라지탄닌들의 α-아밀레이스 억제 비교에서 C-1 β-갈로일기를 가진 화합물의 억제가 강함(시험관)[11]",[11]),
 C("Brambliin A","브람블리인 A","GOD형 엘라지탄닌","bioactive","잎",
   "잎에서 분리된 신규 화합물(브람블리인 A–D, 함량 확인하지 못함)[12]",
   "치태(덴탈 플라크) 형성 억제(시험관)[12]",[12]),
 C("Myricetin","미리세틴","플라보놀","bioactive","잎(폴리페놀 추출물)",
   "폴리페놀 추출물에서 UPLC-MS/MS로 확인(함량 확인하지 못함)[24]",
   "고혈당·고지질 조건의 신장 족세포에서 자가포식 조절(시험관)[24]",[24]),
 C("Kaempferol 3-rutinoside","캠페롤-3-O-루티노사이드","플라보놀 배당체","bioactive","잎",
   "잎 추출물에서 UPLC-ESI-qTOF-MS/MS로 동정(함량 확인하지 못함)[15]",
   "α-글루코시데이스 억제 후보 성분으로 제시됨(시험관)[15]",[15]),
]

chou = "https://pmc.ncbi.nlm.nih.gov/articles/PMC2680688/"
base_cond = {
 "instrument":"Waters 600 펌프, 717 자동시료주입기, 2996 PDA 검출기",
 "column":"Alltech Prevail C18(250 mm × 4.6 mm, 5 μm) + YMC C18 가드 칼럼(7.5 mm × 4.6 mm, 5 μm)(C18 표기는 같은 연구진 후속 논문[3]의 같은 조건으로 확인)",
 "mobile_phase":"A: 0.17% 인산 아세토나이트릴, B: 0.17% 인산 수용액",
 "gradient":"0–65분 A 5→30%; 65–85분 30→60%; 85–90분 60→70%; 90–100분 70% 등용매",
 "flow":"1.0 mL/min",
 "temp":"25 °C",
 "injection":"10 μL",
 "sample_prep":"잎을 60 °C에서 12시간 말려 100 mesh 분말; 1 g에 물 100 mL를 넣고 2시간 환류 추출, 10,000 × g 10분 원심분리, 상등액 25 mL를 감압 건고한 뒤 메탄올 10 mL에 녹여 0.2 μm 필터로 여과",
 "linearity":"5개 농도 외부표준 검량선, 상관계수(r) > 0.999",
 "recovery":"다섯 성분 평균 회수율 93.08–97.50%(RSD 2.35–4.90%); 일내 정밀도 RSD 3.14%, 일간 3.01%",
}
def cond(**kw):
    c = dict(base_cond); c.update(kw); return c
assays = [
 {"role":"literature","compound":"Rubusoside","compound_ko":"루부소사이드","part":"잎(중국 구이저우 재배, 14점)",
  "content":"잎 평균 약 5%(다섯 지표성분 합계 5.9% w/w의 82.5%), 변동 약 16%[2]","method":"HPLC-PDA",
  "conditions":cond(detection="205 nm(디테르펜 배당체), PDA 200–400 nm; 254 nm 크로마토그램과 합쳐 처리", standard="실험실에서 분리한 루부소사이드(HPLC-PDA 순도 98% 초과), 저장용액 1.404 mg/mL(메탄올)", lod="11.36 μg/mL(S/N 3)", loq="37.86 μg/mL(S/N 10)"),
  "rationale":"단맛을 내는 이 종의 특징 성분으로, 논문이 루부소사이드 등 디테르펜 배당체를 첨차 원료의 화학적 확인에 쓸 수 있는 표지 성분이라고 밝혔다[2]","source":[2,3],"url":chou,"source_kind":"paper"},
 {"role":"literature","compound":"Steviolmonoside","compound_ko":"스테비올모노사이드","part":"잎(중국 구이저우 재배, 14점)",
  "content":"잎 평균 0.71% w/w, 변동 29%[2]","method":"HPLC-PDA",
  "conditions":cond(detection="205 nm, PDA 200–400 nm", standard="실험실에서 분리한 스테비올모노사이드(순도 98% 초과), 저장용액 0.120 mg/mL", lod="3.85 μg/mL(S/N 3)", loq="11.09 μg/mL(S/N 10)"),
  "rationale":"루부소사이드와 함께 잎의 단맛을 내는 디테르펜 배당체로 다섯 지표성분에 포함되었다[2]","source":[2],"url":chou,"source_kind":"paper"},
 {"role":"literature","compound":"Gallic acid","compound_ko":"갈산","part":"잎(중국 구이저우 재배, 14점)",
  "content":"잎 평균 0.13% w/w, 변동 약 12%[2]","method":"HPLC-PDA",
  "conditions":cond(detection="254 nm, PDA 200–400 nm", standard="Sigma 표준품, 저장용액 0.05 mg/mL", lod="1.24 μg/mL(S/N 3)", loq="3.45 μg/mL(S/N 10)"),
  "rationale":"갈로탄닌 무리를 대표하고 잎 추출물의 혈관신생 억제 활성 성분으로 밝혀져 지표성분으로 골랐다[2, 18]","source":[2,18],"url":chou,"source_kind":"paper"},
 {"role":"literature","compound":"Rubusoside","compound_ko":"루부소사이드","part":"잎 추출 감미료 제품(일본 텐료차 추출물)",
  "content":"8.65%[9]","method":"TLC·HPLC",
  "conditions":{},
  "rationale":"식품첨가물로서 품질·안전성 평가의 일부로 주 단맛 성분을 정량하고 원료가 첨차 잎임을 확인했다[9]; 전문 확인 못함(초록만 확인)","source":[9],"url":pm(12436720),"source_kind":"paper"},
]

d = {"slug":"rubus-suavissimus","name_ko":"첨차","name_en":"Chinese sweet tea","scientific_name":"Rubus suavissimus S. Lee",
 "aliases":["텐차","첨차잎","첨차추출물","첨차추출분말","甜茶(Tiancha)","Chinese sweet leaf tea","ten-cha","Rubus chingii var. suavissimus (S. K. Lee) L. T. Lu"],
 "sections":sections,"compounds":compounds,"markers":[],"assays":assays,"nutrients":[],"production":[],"world":[],"gi":[],"orgs":[],"sources":sources}
(HERE/"dossier.json").write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in sections: print(s["key"], len(s["body"]))
