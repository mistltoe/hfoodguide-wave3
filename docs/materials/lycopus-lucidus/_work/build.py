import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
A = "2026-11-02"
def pm(pmid): return f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
def pmc(p): return f"https://pmc.ncbi.nlm.nih.gov/articles/{p}/"
S = [
 (1, "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 쉽싸리지상부(Lycopus lucidus Turcz. ex Benth.)·애기쉽싸리·개차즈기잎 항목", "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "식품의약품안전처", "2026-10-13"),
 (2, "Lycopus lucidus Extract Attenuates Testosterone Propionate-Induced Benign Prostatic Hyperplasia in Rats. Pharmaceuticals (Basel). 2026 (doi:10.3390/ph19091478)", pmc("PMC13610609"), "MDPI (PMC)", A),
 (3, "Lactobacillus HY7015 and Lycopus lucidus Turcz. Extract Promotes Human Dermal Papilla Cell Cytoprotective Effect and Hair Regrowth Rate in C57BL/6 Mice. Molecules. 2022 (doi:10.3390/molecules27238235)", pmc("PMC9738319"), "MDPI (PMC)", A),
 (4, "Chemical identification and quality evaluation of Lycopus lucidus Turcz by UHPLC-Q-TOF-MS and HPLC-MS/MS and hierarchical clustering analysis. Biomed Chromatogr. 2016 (doi:10.1002/bmc.3867) — 초록", pm("27739081"), "Wiley (PubMed)", A),
 (5, "Strategies for quantitative analysis and preparation of hepatoprotective rosmarinic acid of Lycopus lucidus aerial parts. Fitoterapia. 2026 (doi:10.1016/j.fitote.2026.107364) — 초록", pm("42386097"), "Elsevier (PubMed)", A),
 (6, "Antioxidative constituents from Lycopus lucidus. Arch Pharm Res. 2004 (doi:10.1007/BF02980102) — 초록", pm("15022718"), "Springer (PubMed)", A),
 (7, "Human ACAT-1 and ACAT-2 inhibitory activities of pentacyclic triterpenes from the leaves of Lycopus lucidus TURCZ. Biol Pharm Bull. 2006 (doi:10.1248/bpb.29.382) — 초록", pm("16462051"), "일본약학회 (PubMed)", A),
 (8, "Inhibitory activities of phenylpropanoids from Lycopus lucidus on amyloid aggregation related to Alzheimer's disease and type 2 diabetes. J Nat Med. 2020 (doi:10.1007/s11418-020-01398-6) — 초록", pm("32219646"), "Springer (PubMed)", A),
 (9, "Hyaluronidase inhibitors from Takuran, Lycopus lucidus. Chem Pharm Bull. 2010 (doi:10.1248/cpb.58.394) — 초록", pm("20190448"), "일본약학회 (PubMed)", A),
 (10, "Hydrophilic interaction liquid chromatography for the separation, purification, and quantification of raffinose family oligosaccharides from Lycopus lucidus Turcz. J Sep Sci. 2015 (doi:10.1002/jssc.201500316) — 초록", pm("26011699"), "Wiley (PubMed)", A),
 (11, "Isolation, characterization, and immunological effects of alpha-galacto-oligosaccharides from a new source, the herb Lycopus lucidus Turcz. J Agric Food Chem. 2010 (doi:10.1021/jf101217f) — 초록", pm("20583842"), "ACS (PubMed)", A),
 (12, "Evaluation of clinical safety and beneficial effects of stachyose-enriched α-galacto-oligosaccharides on gut microbiota and bowel function in humans. Food Funct. 2017 (doi:10.1039/c6fo01290f) — 초록", pm("28001151"), "RSC (PubMed)", A),
 (13, "Composition and systemic immune activity of the polysaccharides from an herbal tea (Lycopus lucidus Turcz). J Agric Food Chem. 2010 (doi:10.1021/jf101061y) — 초록", pm("20438133"), "ACS (PubMed)", A),
 (14, "Acaricidal activities of the active component of Lycopus lucidus oil and its derivatives against house dust and stored food mites. Pest Manag Sci. 2012 (doi:10.1002/ps.2295) — 초록", pm("22500291"), "Wiley (PubMed)", A),
 (15, "Anticancer, antioxidant and antimicrobial activities of the essential oil of Lycopus lucidus Turcz. var. hirtus Regel. Food Chem. 2011 (doi:10.1016/j.foodchem.2010.12.027) — 초록", pm("25213932"), "Elsevier (PubMed)", A),
 (16, "Optimization of the Isolation and Purification of Formononetin from Lycopus lucidus Turcz. var. hirtus Regel ... in TNF-α-Induced HFLS-RA Cells. Plants (Basel). 2026 (doi:10.3390/plants15172654) — 초록", pm("42739419"), "MDPI (PubMed)", A),
 (17, "Genomic and population analyses reveal asymmetric subgenome evolution and local adaptation in the polyploid Lycopus lucidus. Commun Biol. 2026 (doi:10.1038/s42003-026-10373-y)", pmc("PMC13434203"), "Springer Nature (PMC)", A),
 (18, "Pan-Plastome Insights Into Genetic Adaptation and Future Distribution of Lycopus lucidus Under Climate Change. Physiol Plant. 2026 (doi:10.1111/ppl.70861) — 초록", pm("41933464"), "Wiley (PubMed)", A),
 (19, "The complete chloroplast genomes of Lycopus lucidus and another Mentheae species. Mitochondrial DNA B Resour. 2021 (doi:10.1080/23802359.2020.1847617)", pmc("PMC7819123"), "Taylor & Francis (PMC)", A),
 (20, "Lycopus lucidus Turcz Inhibits the Osteoclastogenesis in RAW 264.7 Cells and Bone Loss in Ovariectomized Rat Model. Evid Based Complement Alternat Med. 2019 (doi:10.1155/2019/3231784)", pmc("PMC6409043"), "Hindawi (PMC)", A),
 (21, "Lycopus lucidus Turcz ameliorates DNCB-induced atopic dermatitis in BALB/c mice. Mol Med Rep. 2021 (doi:10.3892/mmr.2021.12467)", pmc("PMC8503738"), "Spandidos (PMC)", A),
 (22, "Lycopus lucidus Turcz. Water Extract Ameliorates the Metabolic Disorder by Up-Regulated Major Urinary Protein Expression in High-Fat Diet-Induced Obesity. Curr Issues Mol Biol. 2022 (doi:10.3390/cimb44050165)", pmc("PMC9164051"), "MDPI (PMC)", A),
 (23, "Ethanol Extract of Lycopus lucidus Turcz. ex Benth Inhibits Metastasis by Downregulation of Runx-2 in Mouse Colon Cancer Cells. Evid Based Complement Alternat Med. 2018 (doi:10.1155/2018/9513290)", pmc("PMC6076976"), "Hindawi (PMC)", A),
 (24, "Anti-allergic effects of Lycopus lucidus on mast cell-mediated allergy model. Toxicol Appl Pharmacol. 2005 (doi:10.1016/j.taap.2005.04.011) — 초록", pm("15936049"), "Elsevier (PubMed)", A),
 (25, "Screening and identification of the metabolites in rat urine and feces after oral administration of Lycopus lucidus Turcz extract by UHPLC-Q-TOF-MS. J Chromatogr B. 2016 (doi:10.1016/j.jchromb.2016.05.020) — 초록", pm("27262082"), "Elsevier (PubMed)", A),
 (26, "Ethnopharmacological relevance and anti-inflammatory mechanisms of Lycopi Herba in diabetic nephropathy: Integrated chemical profiling and pharmacological evaluation. J Ethnopharmacol. 2026 (doi:10.1016/j.jep.2026.121505) — 초록", pm("41802508"), "Elsevier (PubMed)", A),
 (27, "식품의약품안전처 한약 공정서 '택란(Lycopi Herba)' 항목 PDF(KP_153) — 원문을 열지 못하고 웹 검색(WebSearch) 결과 요약으로만 확인함", "https://www.mfds.go.kr/files/upload/herbmed/photo_data/KP_153.pdf", "식품의약품안전처", A),
 (28, "Lycopus europaeus (Gypsywort): effects on the thyroidal parameters and symptoms associated with thyroid function. Phytomedicine. 2008 (doi:10.1016/j.phymed.2007.11.001) — 초록", pm("18083505"), "Elsevier (PubMed)", A),
 (29, "Extract of Lycopus europaeus L. reduces cardiac signs of hyperthyroidism in rats. Life Sci. 2005 (doi:10.1016/j.lfs.2005.06.014) — 초록", pm("16150466"), "Elsevier (PubMed)", A),
 (30, "A Highly Rearranged Nor-Abietane Diterpenoid ... and Three Other Diterpenoids from Lycopus lucidus var. hirtus and Antineuroinflammatory Activities. J Org Chem. 2026 (doi:10.1021/acs.joc.6c00266) — 초록", pm("42014362"), "ACS (PubMed)", A),
 (31, "Variation in nutritional compositions, antioxidant activity and microstructure of Lycopus lucidus Turcz. root at different harvest times. Food Chem. 2015 (doi:10.1016/j.foodchem.2015.03.033) — 초록", pm("25863615"), "Elsevier (PubMed)", A),
 (32, "Study on optimization of extraction and purification processes for total flavonoids from Lycopi herba roots and their anti-proliferative effects on fibrous synoviocytes in human rheumatoid arthritis. Ultrason Sonochem. 2024 (doi:10.1016/j.ultsonch.2024.107164)", pmc("PMC11625243"), "Elsevier (PMC)", A),
 (33, "Lycopus lucidus Turcz. ex Benth. Attenuates free fatty acid-induced steatosis in HepG2 cells and non-alcoholic fatty liver disease in high-fat diet-induced obese mice. Phytomedicine. 2019 (doi:10.1016/j.phymed.2018.07.008) — 초록", pm("30668424"), "Elsevier (PubMed)", A),
]
sources = [{"n": n, "title": t, "url": u, "publisher": p, "accessed": a} for n, t, u, p, a in S]

sections = [
 {"key": "overview", "title": "한눈에 보기", "body":
  "쉽싸리(Lycopus lucidus Turcz. ex Benth.)는 꿀풀과(Lamiaceae) 쉽싸리속의 여러해살이풀이고, 꽃이 피기 전의 지상부를 말린 한약재를 택란(Lycopi Herba)이라 부른다[1][2][20]. 식품의약품안전처 「식품원료 목록」에는 원료명 '쉽싸리지상부', 다른 이름 '택란', 영어 이름 Shiny bugleweed로 올라 있다[1].\n\n"
  "이 원료의 식품원료 지위는 '사용가능'이고, 사용 조건은 '사용가능부위 : 지상부※(택란)'이어서 목록에 적힌 사용 부위는 지상부뿐이다[1]. 같은 속의 애기쉽싸리(Lycopus maackianus)는 '전체'를 쓸 수 있는 별개의 원료로 따로 올라 있으므로 서로 구분해야 한다[1]. 건강기능식품 고시형 원료의 원재료로 쓰인다는 기록은 목록 자료에서 확인하지 못함.\n\n"
  "지상부에서는 로즈마린산·메틸 로즈마리네이트 같은 페놀산, 루테올린 같은 플라보노이드, 우르솔산·올레아놀산·베툴린산 같은 트리테르펜이 분리되었다[6][7]. 70% 에탄올 지상부 추출물의 로즈마린산은 추출물 1 g당 22.03 mg이었고, 잎 추출물은 정량 핵자기공명(qHNMR)으로 3.92 ± 0.02%(w/w)였다[2][5]. 한국·중국·일본에서 부종, 상처, 생리불순 같은 부인과 질환에 전통적으로 써 왔다[9][20][24]."},
 {"key": "history", "title": "역사와 전통적 이용", "body":
  "아시아에서는 꽃이 피기 전에 잎과 줄기를 거두어 말린 뒤 부종, 상처, 통증, 생리불순·생리통 같은 부인과 질환에 써 왔다[20]. 일본에서는 같은 약재를 Takuran이라 부르며 여성 질환에 쓰는 전통 생약으로 소개한다[9]. 한국에서도 전통 의약으로 써 왔고 항염증 작용이 있는 약으로 알려져 있다[24].\n\n"
  "동아시아 전통의학에서 지상부(Lycopi Herba)는 어혈과 관련된 무월경·생리통에 써 왔고, 여러 동아시아 나라의 공식 약전에 실려 있다[2]. 같은 논문은 한약재 권장 용량을 하루 생약 6–12 g으로 인용하고, 하루 20 g을 쓰는 전통 처방도 기록되어 있다고 적었다[2]. 중국에서는 혈을 돌게 하고 어혈을 풀며 소변을 잘 나오게 해 부종을 줄이는 약으로 처방해 왔다[26].\n\n"
  "식약처 한약 공정서에도 '택란' 항목이 있고 기원을 쉽싸리의 꽃이 피기 전 지상부로 정한다는 내용은 웹 검색 요약으로만 확인했으며 원문 PDF는 열지 못했다[27]. 잎은 약초차로도 마셔 왔고, 중국에서는 뿌리를 지순(地笋, Di shen)이라 부르며 먹는다[13][17]. 털이 많은 변종(var. hirtus)의 잎과 뿌리도 달여 먹거나 다른 음식과 함께 먹는 식용·약용 자원으로 소개된다[30]."},
 {"key": "biology", "title": "식물학적 특징", "body":
  "쉽싸리속(Lycopus)은 동반구 온대와 북아메리카에 약 14종이 있고, 중국에는 4종이 자생한다[17]. 쉽싸리는 중국 북부에 널리 퍼져 있으며 추위·더위·가뭄·침수·그늘 같은 여러 환경 스트레스에 잘 견디는 종으로 보고되었다[17].\n\n"
  "한약재 공정서의 성상 기재는 줄기가 네모진 기둥 모양으로 길이 50–100 cm, 지름 2–6 mm이고 잎이 마주나며, 냄새가 없고 맛이 담담하다는 것이다(웹 검색 요약으로만 확인)[27]. 잎과 줄기는 꽃이 피기 전에 거둔다[20]. 뿌리에는 라피노스·스타키오스·베르바스코스·아주고스 같은 라피노스족 올리고당이 1 g당 모두 686.5 mg 들어 있었지만, 지상부에서는 이 올리고당이 검출되지 않았다[10].\n\n"
  "중국 60개 엽록체 유전체 분석과 종 분포 모형에서 쉽싸리에게 알맞은 서식지는 랴오닝성과 양쯔강 유역에 몰려 있었고, 강수량이 현재 분포를 정하는 가장 큰 요인이었다[18]. 중국 논문에서는 털이 많은 변종 var. hirtus Regel을 재료로 쓴 경우가 많다[15][16][30]. 한반도 안의 분포·개화기 같은 국내 공공기관 식물 정보는 이번 조사에서 확인하지 못함."},
 {"key": "related_species", "title": "가까운 종", "body":
  "식약처 「식품원료 목록」에는 같은 속의 애기쉽싸리(Lycopus maackianus, 이명 L. angustus)가 사용 부위 '전체'인 별도 원료로 있고, 다른 이름으로 애기쉽사리·애기택란이 적혀 있다[1]. 또 개차즈기(Amethystea caerulea)는 학명 이명에 Lycopus amethystinus가 함께 적혀 있으며 잎을 쓰는 별도 원료다[1].\n\n"
  "털쉽싸리로 불리는 변종 var. hirtus는 중국 연구에 자주 쓰이며, 그 정유는 배양 암세포 증식 억제와 중간 정도의 항산화·항균 작용을 보였다[15]. 이 변종에서는 포르모노네틴이 주요 플라보노이드로 분리되었고, 아비에탄형 다이테르펜 19종도 분리되었다[16][30]. 변종의 자료가 국내 식품원료인 쉽싸리지상부와 같은 품질이라고 볼 근거는 확인하지 못함.\n\n"
  "유럽의 Lycopus europaeus 추출물은 가벼운 갑상선기능항진 증상에 써 온 약초다[29]. L. europaeus 제제를 쓴 개방 연구에서 소변의 T4 배설이 늘고 아침 심박수 증가 같은 증상이 줄었으며, 갑상선호르몬을 준 쥐에서는 추출물이 심박수와 혈압 상승을 줄였다[28][29]. 쉽싸리 지상부에도 이런 갑상선 관련 작용이 있는지는 확인하지 못함."},
 {"key": "cultivation", "title": "재배와 생산", "body":
  "국내 재배 면적·생산량 통계는 로컬 특용작물·농작물 생산 통계에서 쉽싸리·택란 품목을 찾지 못해 확인하지 못함. 지리적 표시 등록 자료에서도 이 종의 항목은 확인하지 못함.\n\n"
  "국내 연구에 쓰인 택란은 경북 영천의 한약재 시장이나 한약재 업체에서 구입한 것이 많았다[2][22][23]. 약재로 쓸 잎과 줄기는 꽃이 피기 전에 거두어 말린다[20]. 약재로는 지상부를 쓰고 뿌리는 흔히 버려졌으나, 최근 뿌리도 플라보노이드 추출 원료로 연구되었다[32].\n\n"
  "중국에서 뿌리를 2013년 11월, 12월, 2014년 1월에 캐어 비교한 연구에서는 늦게 캘수록 전분이 크게 줄고 조지방이 늘었으며, 단백질과 총 아미노산은 마지막 수확에서 가장 많았다[31]. 같은 연구에서 뿌리의 무기질은 칼륨이 가장 많고 칼슘·철·마그네슘 순이었다[31]. 기후변화 예측 모형은 앞으로 알맞은 서식지가 넓어지되 중국 북부와 양쯔강 이남에서 더 조각날 것으로 보았다[18]."},
 {"key": "processing", "title": "가공과 이용", "body":
  "연구용 지상부 추출물은 주로 물 달임이나 에탄올 추출로 만든다[2][20][22]. 말린 약재 500 g을 끓는 물 5 L에 2시간 달여 동결건조한 물 추출물의 수율은 11.4%였다[20][21]. 70% 에탄올 10배 부피로 80 °C에서 3시간 환류 추출한 추출물의 수율은 9.84%였다[2]. 105 °C에서 5시간씩 두 번 가압 열수 추출한 추출물은 수율 15.44%였다[22].\n\n"
  "잎을 우린 약초차의 수용성 다당류는 갈락토스 50.1 mol%, 갈락투론산 14.2 mol%로 이루어져 있었다[13]. 뿌리에서 얻은 α-갈락토올리고당은 스타키오스 51.8%(w/w), 라피노스 26.5%, 베르바스코스 10.1%였고 생 뿌리 무게의 약 20%가 이 올리고당이었다[11]. 뿌리 올리고당을 과립으로 만든 제품은 사람 시험에도 쓰였지만, 이는 식품원료 목록의 사용 부위인 지상부가 아니다[1][12].\n\n"
  "정유의 살비 성분으로 1-옥텐-3-올이 분리되었다[14]. 쥐에 추출물을 먹인 뒤 소변에서 19종, 대변에서 17종의 대사체가 확인되었고 주된 대사는 글루쿠론산·황산 포합이었다[25]. 식약처 「식품 등의 생산실적」의 건강기능식품 원료 품목에서 쉽싸리지상부 항목은 확인하지 못함."},
 {"key": "genetics", "title": "유전체와 육종", "body":
  "2026년 중국 연구진이 쉽싸리의 염색체 수준 유전체를 해독했으며, 크기는 1.18 Gb이고 최근의 전장 유전체 3배화(WGT)로 생긴 세 하위유전체(A, B, C)로 이루어져 있었다[17]. 이 유전체에서 단백질 암호화 유전자 74,127개와 위유전자 534개가 주석되었다[17]. 하위유전체 B는 강한 정화 선택으로 안정되었고, A와 C는 유전자 교체와 위유전자화가 빨랐다[17].\n\n"
  "중국 13개 집단 60개체의 재서열 분석에서 고품질 SNP 14,478,124개가 나왔고, 지역에 따른 네 계통과 후기 홀로세 냉각기와 겹치는 집단 병목이 확인되었다[17]. 환경 연관 분석으로 찾은 적응 변이 9,496개는 스트레스 반응, 2차 대사, 왁스 생합성 경로에 많았고 강수량이 지역 적응의 주된 요인이었다[17].\n\n"
  "엽록체 유전체 60개로 만든 범엽록체유전체에서는 산둥반도 계통과 양쯔강 이남 계통이 갈렸고, 산둥 계통의 psbD 유전자에 고온·가뭄 적응 신호가 있었다[18]. 2021년에는 쉽싸리를 포함한 박하족(Mentheae) 두 종의 엽록체 유전체가 각각 152,096 bp와 151,922 bp로 보고되었다[19]. 국내 품종 등록이나 육종 기록은 확인하지 못함."},
 {"key": "safety", "title": "안전성", "body":
  "식약처·EFSA 등 공공기관의 쉽싸리 안전성 평가, 알레르기·잔류 기준 정보는 이번 조사에서 확인하지 못함. 식약처 한약 공정서의 택란 기준은 건조감량 10.0% 이하, 회분 5.0% 이하, 산불용성회분 2.0% 이하, 묽은에탄올엑스 20.0% 이상인 것으로 웹 검색 요약에서 확인했으며 원문은 열지 못했다[27].\n\n"
  "쥐 전립선비대 모델에서 70% 에탄올 추출물을 하루 100–200 mg/kg씩 28일 먹였을 때 죽거나 이상 증상을 보인 동물은 없었지만, 저자들은 전신 안전성은 평가하지 않았다고 밝혔다[2]. 같은 연구에서 추출물은 혈청 테스토스테론을 높이고 DHT/테스토스테론 비율을 낮춰 성호르몬 대사에 영향을 줄 수 있음을 보였다[2]. 고지방 식이 생쥐에게 체중 1 kg당 100–200 mg의 에탄올 추출물을 먹인 연구도 있으나 독성 평가가 목적은 아니었다[33].\n\n"
  "사람 시험은 지상부가 아닌 뿌리 유래 스타키오스 과립 하루 5 g으로, 건강한 성인 100명(14일)과 변비 환자 103명(30일)에서 유의한 이상반응이 없었다[12]. 같은 속 L. europaeus는 갑상선 기능 지표에 영향을 준다는 연구가 있으나, 쉽싸리 섭취와 갑상선 질환·임신·수유에 관한 공식 주의사항은 확인하지 못함[28]."},
]

compounds = [
 {"name": "Rosmarinic acid", "name_ko": "로즈마린산", "class": "페놀산(카페산 에스터)", "role": "marker", "part": "지상부·잎",
  "content_text": "70% 에탄올 지상부 추출물 22.03 mg/g 추출물(HPLC-DAD)[2]; 잎 추출물 3.92 ± 0.02%(w/w, qHNMR)[5]; 지상부 열수 추출물 용액 67.64 μg/mL[3]",
  "activity_ko": "NBT 슈퍼옥사이드 소거 IC50 2.59 µg/mL(시험관)[6]; HepG2 세포에서 활성산소 소거, 간 보호 활성의 주성분으로 제시됨[5]", "source": [2, 3, 5, 6]},
 {"name": "Methyl rosmarinate", "name_ko": "메틸 로즈마리네이트", "class": "페놀산 에스터", "role": "bioactive", "part": "지상부",
  "content_text": "지상부에서 분리(함량은 초록에 없음, 확인하지 못함)[6]", "activity_ko": "슈퍼옥사이드 소거 IC50 1.42 µg/mL(시험관)[6]", "source": [6]},
 {"name": "Ethyl rosmarinate", "name_ko": "에틸 로즈마리네이트", "class": "페놀산 에스터", "role": "bioactive", "part": "지상부",
  "content_text": "지상부에서 분리(함량 확인하지 못함)[6]", "activity_ko": "슈퍼옥사이드 소거 IC50 0.78 µg/mL(시험관)[6]", "source": [6]},
 {"name": "Luteolin", "name_ko": "루테올린", "class": "플라본", "role": "bioactive", "part": "지상부·잎",
  "content_text": "지상부에서 분리[6]; 잎 물 추출물의 주성분으로 서술됨(정량값은 본문에서 확인하지 못함)[22]",
  "activity_ko": "슈퍼옥사이드 소거 IC50 2.83 µg/mL(시험관)[6]", "source": [6, 22]},
 {"name": "Luteolin 7-O-glucuronide methyl ester", "name_ko": "루테올린-7-O-β-D-글루쿠로나이드 메틸에스터", "class": "플라본 배당체", "role": "bioactive", "part": "지상부",
  "content_text": "지상부에서 분리(함량 확인하지 못함)[6]", "activity_ko": "슈퍼옥사이드 소거 IC50 3.05 µg/mL(시험관)[6]", "source": [6]},
 {"name": "Caffeic acid", "name_ko": "카페산", "class": "페놀산", "role": "marker", "part": "지상부 물 추출물",
  "content_text": "물 추출물 HPLC 분석의 지표 성분(표준품)으로 사용(함량 확인하지 못함)[21]; 70% 에탄올 추출물에서 정성 확인[23]",
  "activity_ko": "추출물의 지표 성분으로 쓰임[21]", "source": [21, 23]},
 {"name": "Rutin", "name_ko": "루틴", "class": "플라보놀 배당체", "role": "bioactive", "part": "지상부 70% 에탄올 추출물",
  "content_text": "HPLC로 정성 확인(머무름 시간 46.28분, 정량값 없음)[23]", "activity_ko": "프로토카테큐산·카페산·로즈마린산과 함께 추출물 확인 성분[23]", "source": [23]},
 {"name": "Ursolic acid", "name_ko": "우르솔산", "class": "펜타사이클릭 트리테르펜", "role": "marker", "part": "잎·지상부",
  "content_text": "잎 메탄올 추출물에서 분리[7]; 지상부 조추출물에서 함량이 높은 성분으로 HPLC 정량(값은 초록에 없음, 확인하지 못함)[26]; 공정서 확인시험(박층크로마토그래피) 표준품(웹 검색 요약)[27]",
  "activity_ko": "NF-κB/TNF-α/STAT3 염증 축을 조절해 당뇨병성 신증 모델에서 주된 항염 성분으로 제시됨(동물·세포)[26]", "source": [7, 26, 27]},
 {"name": "Oleanolic acid", "name_ko": "올레아놀산", "class": "펜타사이클릭 트리테르펜", "role": "bioactive", "part": "잎",
  "content_text": "잎 메탄올 추출물에서 분리(함량 확인하지 못함)[7]", "activity_ko": "인간 ACAT 억제 활성 평가 대상(베툴린산보다 약함)[7]", "source": [7]},
 {"name": "Betulinic acid", "name_ko": "베툴린산", "class": "루판형 트리테르펜", "role": "bioactive", "part": "잎",
  "content_text": "잎 메탄올 추출물에서 분리(함량 확인하지 못함)[7]", "activity_ko": "인간 ACAT-1·ACAT-2 억제 IC50 16.2 ± 0.6·28.8 ± 1.3 µM(시험관)[7]", "source": [7]},
 {"name": "Schizotenuin A", "name_ko": "스키조테누인 A", "class": "페닐프로파노이드", "role": "bioactive", "part": "부위 확인하지 못함",
  "content_text": "리코프산 A·B와 함께 분리(함량 확인하지 못함)[8]", "activity_ko": "아밀로이드 β와 사람 섬 아밀로이드 폴리펩타이드의 섬유화 억제(시험관)[8]", "source": [8]},
 {"name": "Lycopic acid A", "name_ko": "리코프산 A", "class": "페닐프로파노이드", "role": "bioactive", "part": "부위 확인하지 못함",
  "content_text": "쉽싸리에서 분리(부위·함량은 초록에서 확인하지 못함)[8]", "activity_ko": "아밀로이드 섬유화 억제(시험관)[8]; 택란에서 분리된 다른 페닐프로파노이드 5종은 로즈마린산과 비슷한 히알루로니다제 억제[9]", "source": [8, 9]},
 {"name": "Stachyose", "name_ko": "스타키오스", "class": "라피노스족 올리고당", "role": "nutrient", "part": "뿌리(지상부에는 없음)",
  "content_text": "뿌리 289.0 mg/g(라피노스 66.5, 베르바스코스 212.4, 아주고스 118.6 mg/g; 합계 686.5 mg/g), 지상부에서는 검출 안 됨[10]; 정제 뿌리 올리고당의 51.8%(w/w)[11]",
  "activity_ko": "뿌리 올리고당 과립 5 g/일이 사람 장내 비피더스균·젖산균을 늘리고 변비 환자의 배변을 개선(사람, 뿌리 유래)[12]", "source": [10, 11, 12]},
 {"name": "1-Octen-3-ol", "name_ko": "1-옥텐-3-올", "class": "지방족 알코올(정유)", "role": "bioactive", "part": "정유",
  "content_text": "정유의 살비 활성 성분으로 분리(함량 확인하지 못함)[14]", "activity_ko": "집먼지진드기(D. farinae) 훈증 LD50 0.25 µg/cm²로 DEET(36.84 µg/cm²)보다 강함[14]", "source": [14]},
 {"name": "Formononetin", "name_ko": "포르모노네틴", "class": "이소플라본", "role": "bioactive", "part": "변종 var. hirtus",
  "content_text": "변종 var. hirtus의 주요 플라보노이드로 분리(함량 확인하지 못함)[16]", "activity_ko": "TNF-α로 자극한 류머티즘 관절 활막세포의 IL-6·IL-8·IL-1β 분비 억제(시험관)[16]", "source": [16]},
]

assays = [
 {"role": "literature", "compound": "Rosmarinic acid", "compound_ko": "로즈마린산", "part": "지상부(택란) 70% 에탄올 추출물",
  "content": "22.03 mg/g 추출물(추출 수율 9.84%)[2]", "method": "HPLC-DAD",
  "conditions": {"instrument": "Agilent 1260 Infinity III HPLC(G7111A 4원 펌프, G7129A 자동주입기, G7115A 다이오드 배열 검출기)",
   "column": "SunFire C18, 4.6 × 250 mm, 5 µm (Waters)", "mobile_phase": "A: 0.1% 트리플루오로아세트산 수용액, B: 아세토니트릴",
   "gradient": "B 23% 0–20분 유지 → 5분간 100%로 → 100% 10분 유지", "flow": "1.0 mL/min", "temp": "실온", "detection": "330 nm",
   "injection": "10 µL", "sample_prep": "추출물 10 mg + 메탄올 1 mL, 초음파 5분 → 0.2 µm PTFE 주사기 필터 여과",
   "standard": "로즈마린산(순도 98.5%), 메탄올 2 mg/mL 원액 → 0.0625·0.125·0.25·0.5·1 mg/mL 5점 검량선, 3반복",
   "linearity": "0.0625–1 mg/mL, r = 0.9981", "lod": "", "loq": "", "recovery": ""},
  "rationale": "앞선 연구들에서 이 종의 대표 성분으로 동정·정량된 로즈마린산을 지표 성분으로 골랐다[2]. 검출·정량한계와 회수율은 본문에 없어 비워 둠.",
  "source": [2], "url": pmc("PMC13610609"), "source_kind": "paper"},
 {"role": "literature", "compound": "Rosmarinic acid", "compound_ko": "로즈마린산", "part": "지상부 열수 추출물(95–98 °C, 6–8시간)",
  "content": "67.64 μg/mL(추출물 용액 기준, 시료 농도 조건은 확인하지 못함)[3]", "method": "HPLC-DAD",
  "conditions": {"instrument": "", "column": "CAPCELL PAK C18 UG120, 4.6 × 250 mm, 5 µm (OSAKA SODA)",
   "mobile_phase": "A: 0.1% 포름산 수용액, B: 아세토니트릴", "gradient": "0–11분 B 25→95%, 11–15분 B 95→25%",
   "flow": "1.0 mL/min", "temp": "25 °C", "detection": "330 nm", "injection": "10 µL",
   "sample_prep": "시료 약 0.5 g + 메탄올-물(7:3) 10 mL, 실온 초음파 30분 → 원심 후 70% 메탄올로 25 mL 정용 → 0.22 µm 주사기 필터 여과",
   "standard": "로즈마린산 표준품", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "모발 보호·성장과 관련이 알려진 로즈마린산을 추출물의 함량 지표로 정량했다[3]. 기기 모델·검량선 범위·검출한계·회수율은 본문에 없어 비워 둠.",
  "source": [3], "url": pmc("PMC9738319"), "source_kind": "paper"},
 {"role": "literature", "compound": "Phenolic acids and flavonoids (11 compounds)", "compound_ko": "페놀산·플라보노이드 등 11종(성분명은 초록에 없음)", "part": "쉽싸리(부위는 초록에서 확인하지 못함)",
  "content": "UHPLC-Q-TOF-MS로 37종(페놀산 15, 플라보노이드 12, 트리테르펜 3, 유기산 7) 동정, 그중 11종 MRM 정량(함량값은 초록에 없음)[4]", "method": "HPLC-MS/MS(MRM)",
  "conditions": {"instrument": "", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "음이온 모드(동정), 다중반응검지(MRM, 정량)",
   "injection": "", "sample_prep": "", "standard": "", "linearity": "r > 0.9959; 반복성 RSD < 2.6%, 일내·일간 정밀도 RSD < 3.2%", "lod": "", "loq": "정량 하한 5–50 ng/mL", "recovery": "93.1–104.9%"},
  "rationale": "쉽싸리의 성분 동정과 품질 평가(계층적 군집 분석)를 위해 개발된 다성분 정량법이다[4]. 전문 확인 못함 — 칼럼·이동상·정량 성분명은 초록에 없어 비워 둠.",
  "source": [4], "url": pm("27739081"), "source_kind": "paper"},
 {"role": "literature", "compound": "Rosmarinic acid", "compound_ko": "로즈마린산", "part": "잎(지상부) 추출물",
  "content": "3.92 ± 0.02%(w/w)[5]", "method": "qHNMR(정량 ¹H 핵자기공명)",
  "conditions": {"instrument": "", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "¹H NMR",
   "injection": "", "sample_prep": "", "standard": "카페인을 범용 내부 검정 물질로 사용", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "로즈마린산이 HepG2 세포의 활성산소 소거와 간 보호 효과의 주된 활성 성분으로 제시되어 지표로 정량했다[5]. 전문 확인 못함 — 초록에 있는 내부 표준만 적음.",
  "source": [5], "url": pm("42386097"), "source_kind": "paper"},
]

d = {
 "slug": "lycopus-lucidus", "name_ko": "쉽싸리지상부", "name_en": "Shiny bugleweed",
 "scientific_name": "Lycopus lucidus Turcz. ex Benth.",
 "aliases": ["쉽싸리", "택란", "Lycopi Herba", "Takuran", "shiny bugleweed"],
 "sections": sections, "compounds": compounds, "markers": [], "assays": assays,
 "nutrients": [], "production": [], "world": [], "gi": [], "orgs": [], "sources": sources,
}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in sections: print(s["key"], len(s["body"]))
