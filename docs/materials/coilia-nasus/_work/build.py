import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
A = "2026-11-02"
def pm(pmid): return f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
def pmc(p): return f"https://pmc.ncbi.nlm.nih.gov/articles/{p}/"
S = [
 (1, "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — Coilia nasus 행 1개(원료명 '웅어', 영문 'Japanese grenadier anchovy', 수산물, 부위 '-', 사용가능, 이명·사용조건 칸 비어 있음)와 같은 속 Coilia mystus 행(원료명 '싱어', 영문 'Osbecks grenadier anchovy', 수산물, 사용가능) (2026-10-13 수집본 data/raw/mfds_rawmtrl/I1020_20261013.json)", "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "식품의약품안전처", "2026-10-13"),
 (2, "Gap-free genome assembly of anadromous Coilia nasus. Sci Data 2023;10:360. doi:10.1038/s41597-023-02278-w (PMC 전문 확인)", pmc("PMC10244340"), "Scientific Data (Springer Nature)", A),
 (3, "Multi-omics analysis provides new insights into the interplay between gut microbiota, fatty acid metabolism, and immune response in cultured and wild Coilia nasus from the Yangtze River area in China. Microorganisms 2025;13(7):1711. doi:10.3390/microorganisms13071711 (PMC 전문 확인 — 수치 표는 전문 텍스트에 없음)", pmc("PMC12300613"), "Microorganisms (MDPI)", A),
 (4, "Differences in muscle cellularity and flesh quality between wild and farmed Coilia nasus (Engraulidae). J Sci Food Agric 2012;92(7):1504-10. doi:10.1002/jsfa.4734 (PubMed 초록 확인)", pm("22189958"), "Journal of the Science of Food and Agriculture (Wiley)", A),
 (5, "[Fatty acid composition of edible marine fish in Zhoushan, Zhejiang province]. Zhonghua Yu Fang Yi Xue Za Zhi 2013;47(6):552-5 (중국어 논문, PubMed 영문 초록 확인)", pm("24113107"), "중화예방의학잡지(中华预防医学杂志)", A),
 (6, "Probiotics enhance Coilia nasus growth performance and nutritional value by regulating glucolipid metabolism via the gut–liver axis. Int J Mol Sci 2024;25(22):12196. doi:10.3390/ijms252212196 (PMC 전문 확인 — 수치 표는 전문 텍스트에 없음)", pmc("PMC11594500"), "International Journal of Molecular Sciences (MDPI)", A),
 (7, "Risk to humans of consuming metals in anchovy (Coilia sp.) from the Yangtze River Delta. Environ Geochem Health 2009;31(6):727-40. doi:10.1007/s10653-009-9258-1 (PubMed 초록 확인)", pm("19267247"), "Environmental Geochemistry and Health (Springer)", A),
 (8, "Anisakidae parasitism activated immune response and induced liver fibrosis in wild anadromous Coilia nasus. J Fish Biol 2022;100(4):958-969. doi:10.1111/jfb.15027 (PubMed 초록 확인)", pm("35229303"), "Journal of Fish Biology (Wiley)", A),
 (9, "Seasonal occurrence of helminths in the anadromous fish Coilia nasus (Engraulidae): parasite indicators of fish migratory movements. J Parasitol 2011;97(2):192-6. doi:10.1645/GE-2621.1 (PubMed 초록 확인)", pm("21506780"), "Journal of Parasitology", A),
 (10, "Richness and diversity of helminth communities in the Japanese grenadier anchovy, Coilia nasus, during its anadromous migration in the Yangtze River, China. J Parasitol 2012;98(3):449-52. doi:10.1645/GE-2983.1 (PubMed 초록 확인)", pm("22257179"), "Journal of Parasitology", A),
 (11, "Population genomics provides novel insights into evolutionary relationships and local adaptation of two Coilia nasus ecotypes. Ecol Evol 2025;15(12):e72815. doi:10.1002/ece3.72815 (PubMed 초록 확인 — 초록 색인에서 담수형의 학명 표기가 빠져 있음)", pm("41446387"), "Ecology and Evolution (Wiley)", A),
 (12, "Whole-genome resequencing of three Coilia nasus population reveals genetic variations in genes related to immune, vision, migration, and osmoregulation. BMC Genomics 2021;22:878. doi:10.1186/s12864-021-08182-0 (PubMed 초록 확인)", pm("34872488"), "BMC Genomics (Springer Nature)", A),
 (13, "Discovery of natural hybridization and development of an efficient identification marker between Coilia nasus and Coilia brachygnathus. Mar Biotechnol 2026;28(3). doi:10.1007/s10126-026-10612-7 (PubMed 초록 확인)", pm("42018195"), "Marine Biotechnology (Springer)", A),
 (14, "The possible physical barrier and coastal dispersal strategy for Japanese grenadier anchovy, Coilia nasus in the East China Sea and Yellow Sea: evidence from AFLP markers. Int J Mol Sci 2015;16(2):3283-97. doi:10.3390/ijms16023283 (PubMed 초록 확인)", pm("25654225"), "International Journal of Molecular Sciences (MDPI)", A),
 (15, "Evolutionary mechanisms shaping the genetic population structure of coastal fish: insight from populations of Coilia nasus in Northwestern Pacific. Mitochondrial DNA 2014;25(6):464-72. doi:10.3109/19401736.2013.814109 (PubMed 초록 확인)", pm("23901916"), "Mitochondrial DNA (Taylor & Francis)", A),
 (16, "Molecular characterization and differential expression of the myostatin gene in Coilia nasus. Gene 2014;543(1):153-60. doi:10.1016/j.gene.2014.03.016 (PubMed 초록 확인)", pm("24630960"), "Gene (Elsevier)", A),
 (17, "Genetic distances and variations of three clupeid species determined by PCR technique. Dev Reprod 2014;18(4):287-92. doi:10.12717/devrep.2014.18.4.287 (PubMed 초록 확인)", pm("25949199"), "Development & Reproduction (한국발생생물학회)", A),
 (18, "Spatial and sex-specific growth variations of migratory Coilia nasus in the middle and lower Yangtze, China. Biology (Basel) 2025;14(9):1211. doi:10.3390/biology14091211 (PubMed 초록 확인)", pm("41007356"), "Biology (MDPI)", A),
 (19, "Reproductive status monitoring of Coilia nasus across four Yangtze River sections during the fishing ban period. Environ Monit Assess 2026;198(11). doi:10.1007/s10661-026-16060-z (PubMed 초록 확인)", pm("42886281"), "Environmental Monitoring and Assessment (Springer)", A),
 (20, "Tracing monomethylmercury origins in planktivorous migratory fish in the coastal East China Sea: evidences from mercury and carbon stable isotopes. J Hazard Mater 2026;503:141179. doi:10.1016/j.jhazmat.2026.141179 (PubMed 초록 확인)", pm("41548311"), "Journal of Hazardous Materials (Elsevier)", A),
 (21, "Causes of low mercury levels in fish from the Three Gorges Reservoir, China. J Hazard Mater 2024;464:132930. doi:10.1016/j.jhazmat.2023.132930 (PubMed 초록 확인)", pm("37980829"), "Journal of Hazardous Materials (Elsevier)", A),
 (22, "Concentration and bioaccumulation of cyanobacterial bioactive and odorous metabolites occurred in a large, shallow Chinese lake. Bull Environ Contam Toxicol 2014;93(5):643-8. doi:10.1007/s00128-014-1350-2 (PubMed 초록 확인 — 시료 학명은 'Coilia ectenes'로 표기)", pm("25194695"), "Bulletin of Environmental Contamination and Toxicology (Springer)", A),
 (23, "Multi-tissue quantitative lipidomics reveals ovarian phospholipid remodeling across female reproductive states in anadromous Coilia nasus. Fish Physiol Biochem 2026;52(4). doi:10.1007/s10695-026-01744-7 (PubMed 초록 확인)", pm("42489807"), "Fish Physiology and Biochemistry (Springer)", A),
 (24, "Digestive enzyme activity of the Japanese grenadier anchovy Coilia nasus during spawning migration: influence of the migration distance and the water temperature. J Fish Biol 2019;95(5):1311-1319. doi:10.1111/jfb.14136 (PubMed 초록 확인)", pm("31513288"), "Journal of Fish Biology (Wiley)", A),
 (25, "A proteomics approach reveals digestive and nutritional responses to food intake in anadromous Coilia nasus. Comp Biochem Physiol Part D 2022;43:100995. doi:10.1016/j.cbd.2022.100995 (PubMed 초록 확인)", pm("35594610"), "Comparative Biochemistry and Physiology Part D (Elsevier)", A),
 (26, "Transcriptome analysis gene expression in the liver of Coilia nasus during the stress response. BMC Genomics 2014;15:558. doi:10.1186/1471-2164-15-558 (PubMed 초록 확인)", pm("24996224"), "BMC Genomics (Springer Nature)", A),
 (27, "Physiological effects of dietary protein and its optimal requirement for early juvenile Chinese tapertail anchovy (Coilia nasus). Animals (Basel) 2026;16(12):1887. doi:10.3390/ani16121887 (PubMed 초록 확인)", pm("42353496"), "Animals (MDPI)", A),
 (28, "Dynamic structural adaptation and molecular response of the digestive organs during feed domestication in Coilia nasus. Animals (Basel) 2026;16(10):1518. doi:10.3390/ani16101518 (PMC 전문 확인)", pmc("PMC13203724"), "Animals (MDPI)", A),
 (29, "Genomic insights into genetic diversity of Coilia nasus across wild ecotypes and farmed populations in China. Mar Biotechnol 2026;28(3). doi:10.1007/s10126-026-10654-x (PubMed 초록 확인)", pm("42287482"), "Marine Biotechnology (Springer)", A),
 (30, "The complete mitochondrial genome of Coilia nasus (Clupeiformes: Engraulidae) from Ariake Sea. Mitochondrial DNA A 2016;27(2):1518-9. doi:10.3109/19401736.2014.953119 (PubMed 초록 확인)", pm("25231710"), "Mitochondrial DNA Part A (Taylor & Francis)", A),
 (31, "한국민족문화대백과사전 「웅어」 항목 — 원문 페이지는 이 작업 환경에서 열리지 않아(네트워크 허용 목록 밖) WebSearch 결과 요약으로만 확인함, 원문 대조 필요", "https://encykorea.aks.ac.kr/Contents/Item/E0040549", "한국학중앙연구원", A),
 (32, "고리 주변해역에서 출현하는 웅어(Coilia nasus)의 위내용물 조성(한국어류학회지 게재 논문) — 원문 페이지는 이 작업 환경에서 열리지 않아 WebSearch 결과 요약으로만 확인함(2005년 107개체, 새우류·요각류 위주 육식성), 원문 대조 필요", "https://koreascience.kr/article/JAKO201125247231928.page", "한국어류학회", A),
 (33, "한강 하구역 강화 갯벌 조간대 건간망에 어획된 유영생물 군집구조(국립수산과학원 연구진 논문) — 원문 페이지는 이 작업 환경에서 열리지 않아 WebSearch 결과 요약으로만 확인함(웅어를 기수성 주거종으로 분류), 원문 대조 필요", "https://koreascience.kr/article/JAKO201014435571981.page", "KoreaScience(한국과학기술정보연구원) 색인 논문", A),
]
sources = [{"n": n, "title": t, "url": u, "publisher": p, "accessed": a} for n, t, u, p, a in S]

sections = [
 {"key": "overview", "title": "한눈에 보기", "body":
  "웅어(학명 Coilia nasus)는 청어목 멸치과(Engraulidae)에 속하는 작은~중간 크기의 회유성 물고기로, 영어로는 Japanese grenadier anchovy, Chinese tapertail anchovy 등으로 불린다[1, 2, 18]. 북서태평양의 중국·일본·한국 연안에서 양쯔강·황허 같은 강으로 이어지는 물길에 걸쳐 살며, 봄마다 바다에서 강으로 거슬러 올라가 알을 낳는 소하성 어종이다[2]. 중국에서는 지방이 많고 살이 부드러우며 맛이 독특해 '양쯔강 3대 진미'의 하나로 꼽혀 왔다[2, 3].\n\n"
  "식약처 「식품원료 목록」에는 이 학명이 원료명 '웅어', 영문 'Japanese grenadier anchovy'로 1행 올라 있으며, 분류는 수산물, 사용 부위 칸은 '-', 상태는 '사용가능'이고 사용 조건 칸은 비어 있다[1]. 같은 속의 싱어(Coilia mystus)는 목록에 따로 '싱어'로 올라 있는 다른 원료이므로, 이 글은 웅어(C. nasus) 자료만 다룬다[1]. 웅어는 건강기능식품 고시형 원료의 원재료가 아니어서 고시 지표성분은 없다[1].\n\n"
  "양쯔강의 웅어 어획량은 1973년 4,142톤에서 2012년 57.5톤까지 줄었고, 2018년 세계자연보전연맹(IUCN) 적색목록에서 위기(EN) 종으로 평가되었다[2]. 이 때문에 중국은 2018년부터 양쯔강 웅어의 상업 어획을 금지하고 2021년부터 10년 동안의 전면 금어를 시행하고 있으며, 인공 번식과 양식도 늘고 있다[2, 3, 4, 29]."},
 {"key": "history", "title": "이름과 이용의 역사", "body":
  "학명 Coilia nasus 는 Temminck와 Schlegel(1846)이 붙인 이름으로 정리되어 있다[31]. 중국 연구에서는 같은 물고기를 Coilia ectenes 로 적은 경우가 있으나, 한 논문은 C. ectenes 를 C. nasus 의 후행 동물이명(junior synonym)이라고 밝혔다[16]. 따라서 'C. ectenes'로 표기된 옛 자료는 웅어 자료일 수 있지만, 태호 같은 호수에 사는 담수형 개체를 가리키는 경우도 있어 시료의 출처를 함께 확인해야 한다[11, 16, 22].\n\n"
  "한국민족문화대백과사전은 웅어의 옛 이름을 위어(葦魚)로 적고, 갈대 사이에 알을 낳는 습성에서 '위(葦)' 자가 붙었다는 설과 '제어(鱭魚)'라는 다른 이름을 소개한다[31]. 같은 사전은 조선 시대에 한강 하류 고양에 웅어를 잡아 궁중에 올리던 위어소(葦魚所)가 있었다고 서술한다[31]. 다만 이 사전 항목은 원문을 직접 열어 보지 못하고 검색 요약으로만 확인한 내용이다[31].\n\n"
  "중국에서는 2000년대 이전까지 양쯔강 웅어가 풍부해 이 지역에서 경제적으로 가장 중요한 어업 자원이었으나, 남획으로 자원이 크게 줄었다[3]. 그 뒤 인공 번식이 성공하면서 양식 생산이 크게 늘었고, 야생 자원을 보충하기 위한 방류 사업도 시작되었다[3, 4, 29]."},
 {"key": "biology", "title": "어종과 생태", "body":
  "웅어는 몸이 가늘고 옆으로 납작하며 은백색이고, 길이는 30 cm 정도까지 자란다고 소개된다[31]. 산란철이 되면 바다에서 강 하구를 지나 양쯔강 중·하류와 이어진 호수까지 거슬러 오르며, 예전에는 하구에서 1,000 km 넘게 떨어진 둥팅호까지 올라간 개체도 있었다[2]. 알을 낳은 어미와 새끼는 다시 바다로 돌아간다[2].\n\n"
  "양쯔강을 600 km 넘게 거슬러 오르는 동안 웅어는 대체로 먹이를 끊으며, 소수만 먹이를 먹는 것으로 보고되었다[25]. 회유 중 펩신 활성은 굶주림이 길어지며 줄었고, 지방 분해 효소(리파아제) 활성은 충밍(하구에서 약 20 km)에서 안칭(약 620 km)까지 늘어 저장 지방을 꺼내 쓰는 것으로 해석되었다[24]. 2024년 산란철 양쯔강 네 지점에서 잡은 1,119마리를 분석한 연구에서 암컷이 수컷보다 크고 나이가 많았으며, 상류로 갈수록 큰 개체가 잡혔다[18]. 같은 조사에서 2–3세 개체가 실험실 표본의 90.3%를 차지했다[19].\n\n"
  "한국 고리 주변 해역의 웅어 위 내용물을 조사한 국내 연구는 새우류와 요각류를 주로 먹는 육식성 어류라고 보고했다[32]. 국립수산과학원 연구진의 한강 하구 강화 갯벌 조사에서는 웅어를 기수역에 머물러 사는 종(기수성 주거종)으로 분류했다[33]. 두 국내 논문은 원문을 열지 못해 검색 요약으로만 확인한 내용이다[32, 33]."},
 {"key": "related_species", "title": "가까운 종과 혼동", "body":
  "같은 속의 싱어(Coilia mystus)는 식약처 식품원료 목록에 '싱어', 영문 'Osbecks grenadier anchovy'로 따로 올라 있어 웅어와 다른 원료다[1]. AFLP 분석 연구는 C. mystus 를 비교군으로 써서, 중국 연안 웅어와 일본 아리아케해 웅어 사이의 유전적 차이가 웅어–싱어 사이의 종간 차이에 크게 못 미쳐 같은 종 안의 격리 집단 수준이라고 보고했다[14]. 따라서 싱어의 성분·어획 자료를 웅어 값으로 옮겨 쓰면 안 된다[1, 14].\n\n"
  "양쯔강 유역에는 웅어와 겉모양이 거의 같은 자매종 Coilia brachygnathus 가 사는데, 유전적으로는 크게 다르고 경제적 가치는 훨씬 낮다[13]. 2026년 연구는 포양호에서 두 종의 자연 잡종을 처음 확인하고, 37 bp 삽입·결실 차이를 이용한 PCR 판별 표지를 개발했다[13]. 이 표지는 양식 현장의 인위적 교잡을 막는 데에도 쓸 수 있다고 제안되었다[13].\n\n"
  "웅어에는 바다–강을 오가는 소하형 외에 평생 호수에 사는 정착형과 평생 바다에 사는 정착형 집단이 보고되어 있다[12]. 태호의 담수형은 논문에 따라 C. nasus taihuensis 로 따로 불리기도 했다[7]. 12개 지역 집단의 전장 유전체를 비교한 연구는 이 담수형이 독립 아종이 아니라 웅어의 담수 생태형이며, 두 생태형은 태호 형성 시기와 맞는 약 4,600년 전에 갈라졌다고 결론지었다[11]. 태호에서 'Coilia ectenes'로 표기된 시료의 자료는 이 담수형일 가능성이 있어, 바다에서 올라오는 웅어 값과 구분해 읽어야 한다[11, 22]."},
 {"key": "cultivation", "title": "어획과 양식", "body":
  "양쯔강 웅어 어획량은 1973년 4,142톤에서 남획·서식지 훼손 등으로 계속 줄어 2012년에는 57.5톤에 그쳤다[2]. 중국은 2018년부터 양쯔강 웅어의 상업 어획을 금지했고, 2021년부터는 양쯔강 전체에 10년 금어를 시행하고 있다[2]. 금어 기간 중인 2024년 5–6월 네 구간 조사에서는 유자망으로 9,455마리를 잡아 번식 상태의 기준 자료를 마련했다[19].\n\n"
  "웅어는 그물에 걸리거나 옮길 때 스트레스 반응이 강해 조직이 손상되거나 죽는 일이 잦고, 이것이 인공 번식과 대량 양식의 큰 걸림돌로 지적되었다[2, 26]. 한 연구는 운반 스트레스에 의한 폐사를 물에 소금(NaCl)을 넣어 줄일 수 있었다고 보고했다[16]. 양식 환경에서는 성장이 매우 느린 것도 실용상의 문제로 꼽힌다[16].\n\n"
  "웅어 양식은 오랫동안 살아 있는 먹이(자연 먹이)에 의존해 왔고, 배합사료로 바꾸는 순치 과정에서 소화기관 구조와 장내 미생물이 달라지는 것이 관찰되었다[28]. 어린 웅어(초기 체중 0.87 g)의 8주 사육 실험에서 증체율과 사료효율로 계산한 최적 사료 단백질 수준은 각각 44.31%와 46.56%였다[27]. 2b-RAD 유전체 분석에서는 양식 집단과 야생 집단 사이에 중간 정도의 유전적 분화(Fst 0.082–0.091)가 확인되었고, 둘을 가르는 SNP 12개가 검증되었다[29].\n\n"
  "국내 웅어의 어획량·양식 생산 통계는 이번 작업에서 확인하지 못했다[1]."},
 {"key": "processing", "title": "가공과 이용", "body":
  "식약처 식품원료 목록에서 웅어는 원료명 '웅어' 한 가지로만 올라 있고, 가공 원료명(살·알·추출물 등)으로 따로 등재된 행은 없다[1]. 한국민족문화대백과사전은 웅어를 박달나무 연기로 훈제해 먹기도 했고 궁중음식 기록에 3월 식재료로 나온다고 서술하지만, 원문을 직접 확인하지 못한 검색 요약이다[31].\n\n"
  "중국 연구들은 웅어가 지방이 많고 살이 부드러워 영양과 맛의 가치가 높다고 평가한다[3, 26]. 양쯔강 야생 웅어와 연못 양식 웅어를 비교한 2025년 연구에서 야생 개체는 근육 지방과 DHA 함량, 오메가-3/오메가-6 비율이 더 높았고 오메가-6 지방산은 더 낮았다[3]. 야생 개체의 오메가-3/오메가-6 비율은 양식 개체의 약 6배였으나, 총 오메가-3 지방산 함량 자체는 두 집단 간 유의한 차이가 없었다[3].\n\n"
  "2012년 연구에서는 양식 웅어가 야생보다 수분·하이드록시프롤린·콜라겐 함량이 높고 지방은 낮았으며, 포화·다가불포화·오메가-6 지방산은 양식이, 단일불포화지방산은 야생이 더 높았다[4]. 저장성 저우산 시장에서 산 해산어 31종의 가식부를 분석한 연구에서는 웅어의 단일불포화지방산 합계가 3,335.7 ± 383.5 mg/100 g 가식부로 31종 가운데 가장 높았다[5]. 이 값들은 중국산 개체의 측정값이며, 한국산 웅어의 국가표준식품성분표 값은 확인하지 못했다[3–5]."},
 {"key": "genetics", "title": "유전체와 유전 다양성", "body":
  "2021년 4월 양쯔강 타이저우 구간에서 잡은 소하형 암컷(체중 211.8 g)의 근육으로 틈(gap) 없는 염색체 수준 유전체가 조립되어 2023년에 발표되었다[2]. 조립 크기는 약 851.67 Mb, 염색체는 24개, 단백질 암호화 유전자는 21,971개로 예측되었고 반복 서열이 전체의 38.26%를 차지했다[2]. BUSCO 완전성은 92.5%였으며, 청어목 유전체 가운데 처음으로 틈이 없는 조립이라고 보고되었다[2].\n\n"
  "일본 아리아케해 웅어의 미토콘드리아 유전체는 16,900 bp 길이로 13개 단백질 유전자, 2개 rRNA, 22개 tRNA와 조절 부위를 가진다[30]. 미토콘드리아 조절 부위 분석에서는 플라이스토세 해수면 하강기에 갈라진 것으로 보이는 두 계통이 확인되었고, 중국 집단과 아리아케해 집단 사이에 유의한 유전적 구조가 있었다[15]. AFLP 분석도 아리아케해 집단이 중국 연안 집단과 유전적으로 분화된 격리 집단임을 지지했다[14].\n\n"
  "소하형·호수 정착형·바다 정착형 세 집단의 전장 재분석에서는 집단마다 약 318만–331만 개의 SNP가 나왔고, 면역·시각·회유·삼투조절 관련 유전자가 선택 흔적을 보였다[12]. 12개 지역 집단 비교에서는 소하형에서 에너지 대사·삼투조절 유전자, 담수형에서 삼투·이온 균형 유전자의 선택 흔적이 보고되었다[11]. 국내에서는 황해 웅어를 'Korean anchovy'로 표기해 청어(Clupea pallasii)·Harengula zunashi 와 PCR 유전 거리를 비교한 연구가 있다[17]."},
 {"key": "safety", "title": "안전성", "body":
  "식약처 「식품원료 목록」에서 웅어는 별도 사용 조건이 없는 '사용가능' 수산물 원료다[1]. 웅어에 대한 식약처의 알레르기·잔류 기준 등 개별 안전 정보는 이번 작업에서 확인하지 못했다[1].\n\n"
  "야생 소하형 웅어에는 고래회충과(Anisakidae) 선충 유충 기생이 흔하며, 감염 개체의 간에서 손상과 섬유화가 관찰되었다[8]. 양쯔강 하구와 동중국해 연안에서 잡은 웅어 775마리에서는 Anisakis simplex 와 Contracaecum 속 유충을 포함한 기생충 6종이 확인되었다[9]. 다른 조사에서도 회유 중 웅어 224마리에서 기생충 6종이 나왔다[10]. 이 연구들은 물고기 건강과 회유 생태를 본 것으로, 사람 감염 위험을 직접 평가한 것은 아니다[8–10].\n\n"
  "양쯔강 삼각주의 웅어속 4종을 분석한 2009년 연구에서 근육의 납은 0.015–0.13 mg/kg, 카드뮴은 0.0007–0.0036 mg/kg(습중량)이었고, 중국 기준을 넘은 것은 태호 담수형 시료의 크롬뿐이었다[7]. 메틸수은은 동중국해 웅어에서 안정동위원소로 주요 유입원을 추적한 연구와, 싼샤댐 저수지에서 느리게 자라는 웅어의 축적 요인을 모델로 분석한 연구가 있으나 함량 기준 초과 여부는 초록에서 확인하지 못했다[20, 21]. 태호의 'C. ectenes' 시료에서는 남조류 유래 냄새 물질 β-이오논이 최대 25.5 µg/kg(습중량) 검출되었다[22]."},
]

comp = [
 ("Docosahexaenoic acid", "도코사헥사엔산(DHA)", "오메가-3 지방산", "nutrient", "등 근육(양쯔강 야생 vs 연못 양식)", "야생 개체의 주요 다가불포화지방산이며 양식보다 유의하게 높음 — 수치는 표에 있어 전문 텍스트에서 확인 못함[3]", "야생 웅어 근육에서 항산화 효소 활성(T-SOD·T-AOC)과 양의 상관을 보였다고 보고(상관관계일 뿐)[3]", [3]),
 ("Linoleic acid", "리놀레산", "오메가-6 지방산", "nutrient", "등 근육(연못 양식)", "양식 개체의 주요 다가불포화지방산(C18:2n6c), 야생과 유의한 차이 — 수치 확인 못함[3]", "양식 사료의 영향으로 오메가-6 비중이 커진 것으로 해석[3]", [3]),
 ("Oleic acid", "올레산", "단일불포화지방산", "nutrient", "등 근육", "야생·양식 모두에서 가장 많은 단일불포화지방산(C18:1n9c), 야생이 더 높음 — 수치 확인 못함[3]", "웅어 근육 지방산의 주성분[3]", [3]),
 ("Palmitic acid", "팔미트산", "포화지방산", "nutrient", "등 근육", "두 집단 모두에서 가장 많은 포화지방산(C16:0), 야생이 더 높음 — 수치 확인 못함[3]", "웅어 근육 포화지방산의 주성분[3]", [3]),
 ("Arachidonic acid", "아라키돈산", "오메가-6 지방산", "nutrient", "등 근육", "양식 개체에서 유의하게 높음(C20:4n6) — 수치 확인 못함[3]", "오메가-6 유래 에이코사노이드의 전구체로 논문이 서술[3]", [3]),
 ("Eicosapentaenoic acid", "에이코사펜타엔산(EPA)", "오메가-3 지방산", "nutrient", "근육(연못 양식, 프로바이오틱스 급여 실험)", "프로바이오틱스 급여·수중 첨가군에서 60·90일째 대조군보다 유의하게 높음 — 수치는 그림·표에 있어 확인 못함[6]", "양식 웅어의 영양 가치 지표로 쓰임[6]", [6]),
 ("Monounsaturated fatty acids", "단일불포화지방산 합계", "지방산 군", "nutrient", "가식부(저우산 시장 구입, 2011년 9–10월)", "3,335.7 ± 383.5 mg/100 g 가식부(조사한 해산어 31종 중 최고)[5]", "웅어 지방의 특징적인 높은 단일불포화지방산 비중[5]", [5]),
 ("L-Arginine", "아르지닌", "아미노산", "nutrient", "근육(가수분해 아미노산)", "프로바이오틱스 급여·수중 첨가군에서 60·90일째 대조군보다 유의하게 높음 — 수치 확인 못함[6]", "글루탐산과 함께 감칠맛 관련 아미노산으로 논문이 서술[6]", [6]),
 ("L-Lysine", "라이신", "필수아미노산", "nutrient", "근육(가수분해 아미노산)", "프로바이오틱스 급여군에서 90·120일째 대조군보다 유의하게 높음 — 수치 확인 못함[6]", "제한 아미노산으로 논문이 언급[6]", [6]),
 ("Hydroxyproline", "하이드록시프롤린", "아미노산(콜라겐 지표)", "nutrient", "근육(야생 vs 양식)", "양식 개체에서 야생보다 높음(콜라겐도 높음) — 수치는 초록에 없음[4]", "근육 콜라겐 함량의 지표[4]", [4]),
 ("Phosphatidylcholine", "포스파티딜콜린(DHA 함유)", "인지질", "bioactive", "난소(성숙 중 암컷)", "성숙 중 암컷 난소에서 DHA 함유 포스파티딜콜린 분율이 유의하게 증가(정량 지질 1,188종 분석) — 함량 수치 초록에 없음[23]", "난소 성숙에 따른 인지질 재편의 주요 지질[23]", [23]),
 ("beta-Ionone", "β-이오논", "노르이소프레노이드(냄새 물질)", "bioactive", "근육(태호 시료, 'Coilia ectenes' 표기 — 담수형일 수 있음)", "최대 25.5 µg/kg 습중량[22]", "남조류에서 온 이취 성분; 지방 함량과 양의 상관[22]", [22]),
]
compounds = [{"name": a, "name_ko": b, "class": c, "role": r, "part": p, "content_text": ct, "activity_ko": act, "source": s} for a, b, c, r, p, ct, act, s in comp]

def cond(**kw):
    keys = ["instrument","column","mobile_phase","gradient","flow","temp","detection","injection","sample_prep","standard","linearity","lod","loq","recovery"]
    return {k: kw.get(k, "") for k in keys}

assays = [
 {"role": "literature", "compound": "Docosahexaenoic acid (fatty acid methyl esters)", "compound_ko": "도코사헥사엔산(DHA, 지방산 메틸에스터)", "part": "등 근육(양쯔강 타이저우 야생 5마리 vs 양저우 연못 양식 5마리, 2023년 6–11월)",
  "content": "야생이 양식보다 유의하게 높음; 오메가-3/오메가-6 비는 야생이 약 6배 — 개별 수치는 표에 있어 확인 못함[3]", "method": "GC(지방산 메틸에스터, 내부표준 C11:0 메틸에스터)",
  "conditions": cond(instrument="Agilent 6890N GC", column="HP-FFAP 모세관 칼럼(CD-2560으로 표기, 100 m × 0.25 mm × 0.2 μm)",
    sample_prep="클로로폼:메탄올(2:1, v/v)로 지질 추출 → 메탄올성 NaOH(8 mg/mL)로 10분 환류 가수분해 → 3% 황산-메탄올을 넣고 90 °C에서 10분 더 환류해 메틸화 → 포화 NaCl로 2회 세척 → 헥산 추출",
    standard="37종 FAME 혼합 표준품, 5–35 mg/mL 5점 검량선; 내부표준 C11:0 메틸에스터(RSD < 5%)"),
  "rationale": "웅어의 영양 가치 평가에서 핵심으로 본 오메가-3 지방산으로, 야생과 양식 웅어를 가르는 지표로 쓰였다[3]. 전문(2.2.3) 확인 — 검출기 종류·온도 조건·검출·정량한계·회수율은 본문에 없음[3].",
  "source": [3], "url": pmc("PMC12300613"), "source_kind": "paper"},
 {"role": "literature", "compound": "Amino acids (acid hydrolysate)", "compound_ko": "아미노산(산 가수분해, 세린·프롤린 등)", "part": "등 근육(야생 vs 양식)",
  "content": "필수아미노산 9종은 차이 없음, 세린·프롤린은 양식이 유의하게 높음 — 수치 확인 못함[3]", "method": "아미노산 자동분석기(산 가수분해)",
  "conditions": cond(instrument="Hitachi L-8900 아미노산 자동분석기",
    sample_prep="시료 약 0.1 g + 6 mol/L 염산 5 mL, 130 °C 7시간 가수분해 → 증류수로 100 mL 정용 → 1 mL 동결건조 후 0.02 mol/L HCl 1 mL에 재용해 → 0.22 µm 막 여과"),
  "rationale": "근육 단백질의 질을 보는 기본 지표로 야생·양식 비교에 쓰였다[3]. 전문(2.2.2) 확인 — 칼럼·완충액·검출 조건·검출한계는 본문에 없음[3].",
  "source": [3], "url": pmc("PMC12300613"), "source_kind": "paper"},
 {"role": "literature", "compound": "L-Lysine (hydrolyzed amino acids)", "compound_ko": "라이신 등 가수분해 아미노산 19종", "part": "근육(연못 양식, 프로바이오틱스 120일 급여 실험, 군당 10마리)",
  "content": "19종 검출(비필수 11·필수 8); 라이신은 급여군에서 90·120일째 유의하게 높음 — 수치 확인 못함[6]", "method": "UPLC-MS/MS(ESI 양이온, MRM)",
  "conditions": cond(column="ACQUITY UPLC BEH C18(2.1 × 100 mm, 1.7 μm)", detection="ESI 양이온 모드, 다중반응검지(MRM)",
    sample_prep="시료 + 10% 포름산 메탄올-물(1:1) 600 μL, 30초 혼합·55 Hz 90초 분쇄 → 12,000 rpm 4 °C 5분 원심 → 상등액 100 μL + Trp-d3 내부표준(20 ng/mL) 100 μL → 0.22 μm 여과",
    standard="아미노산 표준 혼합액을 10% 포름산 메탄올-물(1:1)로 희석한 작업 표준액; 동위원소 내부표준 Trp-d3(원액 1000 ng/mL)"),
  "rationale": "양식 웅어 근육의 영양 가치(필수아미노산) 변화를 보는 지표로 쓰였다[6]. 전문(4.5) 확인 — 이동상·기울기·유속·검출한계·회수율은 본문에 없음[6].",
  "source": [6], "url": pmc("PMC11594500"), "source_kind": "paper"},
 {"role": "literature", "compound": "Eicosapentaenoic acid (fatty acid methyl esters)", "compound_ko": "에이코사펜타엔산(EPA) 등 지방산 35종", "part": "근육(연못 양식, 프로바이오틱스 급여 실험)",
  "content": "지방산 35종 검출(포화 16·단일불포화 9·다가불포화 10); EPA는 급여군에서 60·90일째 유의하게 높음 — 수치 확인 못함[6]", "method": "GC-MS(EI)",
  "conditions": cond(instrument="Thermo Trace 1300 GC + ISQ 7000 질량분석기", detection="전자충격 이온화(EI) 질량분석",
    sample_prep="시료 + 클로로폼:메탄올(2:1) 1 mL, 55 Hz 1분 분쇄 → 12,000 rpm 4 °C 5분 원심 → 상등액을 1% 황산-메탄올 2 mL에 넣어 80 °C 30분 메틸화 → n-헥산 1 mL·차가운 물 5 mL로 추출·세척 → 3500 rpm 5분 원심 → 상등액 700 μL에 무수황산나트륨 100 mg",
    standard="내부표준 살리실산메틸(500 ppm) 15 μL"),
  "rationale": "양식 웅어의 오메가-3 영양 가치 지표로 쓰였다[6]. 전문(4.5) 확인 — 칼럼·승온 조건·검출한계·회수율은 본문에 없음[6].",
  "source": [6], "url": pmc("PMC11594500"), "source_kind": "paper"},
]

world = [
 {"country": "중국", "metric": "production_t", "year": 1973, "value": 4142, "unit": "t", "note": "양쯔강 웅어 연간 생산(어획)량, 논문 서론 서술", "source": [2]},
 {"country": "중국", "metric": "production_t", "year": 2012, "value": 57.5, "unit": "t", "note": "양쯔강 웅어 연간 생산(어획)량, 논문 서론 서술; 2018년 상업 어획 금지, 2021년부터 10년 금어", "source": [2]},
]

d = {"slug": "coilia-nasus", "name_ko": "웅어", "name_en": "Japanese grenadier anchovy",
     "scientific_name": "Coilia nasus",
     "aliases": ["위어(葦魚, 옛 이름)", "제어(鱭魚)", "Japanese grenadier anchovy", "Chinese tapertail anchovy", "Estuarine tapertail anchovy", "Coilia ectenes(후행 동물이명으로 보고)"],
     "sections": sections, "compounds": compounds, "markers": [], "assays": assays, "nutrients": [],
     "production": [], "world": world, "gi": [], "orgs": [], "sources": sources}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in sections: print(s["key"], len(s["body"]))
