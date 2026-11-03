import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
A = "2026-11-02"
def pm(n, title, cite, pmid, doi, journal, note):
    return {"n": n, "title": f"{title} {cite} — {note}(PMID {pmid})", "url": f"https://doi.org/{doi}", "publisher": journal, "accessed": A}
S = [
 {"n": 1, "title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — Urechis unicinctus 1행(원료명 '개불', 식품원료(A코드), 수산물, 부위(REGN_CD_NM) '-', 상태 '사용가능', 사용조건·영문명·이명 칸 비어 있음); card.json lists 비어 있음(건강기능식품 고시형 원료 아님); 같은 원자료에서 학명 Urechis 가 들어간 다른 행 없음(docs/materials/urechis-unicinctus/card.json, data/raw/mfds_rawmtrl/I1020_20261013.json)", "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
 {"n": 2, "title": "식품의약품안전처 「식품 등의 생산실적」 건강기능식품 품목 유형별 현황 — 로컬 파싱본 docs/stats/hf_items.csv 에서 '개불' 품목 검색(해당 행 없음)", "url": "https://www.mfds.go.kr", "publisher": "식품의약품안전처", "accessed": A},
 pm(3, "Unusual polyunsaturated fatty acids in edible marine worms identified by covalent adduct chemical ionization mass spectrometry.", "Food Chem 2025;463(Pt 2):141287", "39298850", "10.1016/j.foodchem.2024.141287", "Food Chemistry", "PubMed 초록만 확인, 전문 미열람"),
 pm(4, "Functional study on alanine aminotransferase: The synthetase of key umami compound alanine in Urechis unicinctus.", "Int J Biol Macromol 2026;346:150626", "41621519", "10.1016/j.ijbiomac.2026.150626", "International Journal of Biological Macromolecules", "PubMed 초록만 확인"),
 pm(5, "Quality changes in the physiology, behaviour, nutrition, and taste of Urechis unicinctus during waterless live transportation.", "Food Chem 2025;483:144298", "40220437", "10.1016/j.foodchem.2025.144298", "Food Chemistry", "PubMed 초록만 확인"),
 pm(6, "Antioxidant, aroma, and sensory characteristics of Maillard reaction products from Urechis unicinctus hydrolysates: development of food flavorings.", "Front Nutr 2024;11:1325886", "38379540", "10.3389/fnut.2024.1325886", "Frontiers in Nutrition", "PMC 전문 확인(PMC10876865; 2.2 시료, 2.4.1 HPLC 조건, 표 1)"),
 pm(7, "Extraction and Identification of Three New Urechis unicinctus Visceral Peptides and Their Antioxidant Activity.", "Mar Drugs 2022;20(5):293", "35621944", "10.3390/md20050293", "Marine Drugs", "PMC 전문 확인(PMC9145011; 3.2 가수분해, 3.5 LC-MS/MS)"),
 pm(8, "Polysaccharides from the Coelomic Fluid of Urechis unicinctus: Extraction, Structural Diversity, and Potential Against Hypoxia.", "Polymers 2026;18(10):1203", "42198144", "10.3390/polym18101203", "Polymers", "PMC 전문 확인(PMC13210939; 2.1–2.6 방법, 3장 수율·황산기 함량)"),
 pm(9, "Genetic diversity and population structure of penis fish (Urechis unicinctus) based on mitochondrial and nuclear gene markers.", "Mitochondrial DNA A 2018;29(8):1261-1268", "29482423", "10.1080/24701394.2018.1444039", "Mitochondrial DNA Part A", "PubMed 초록 확인"),
 pm(10, "Analysis of the relationship between geography and body color with the genetic diversity in the Echiura worm Urechis unicinctus based on the mitochondrial COI and D-loop sequences.", "Mitochondrial DNA B 2021;6(4):1380-1386", "33969186", "10.1080/23802359.2021.1910082", "Mitochondrial DNA Part B", "PubMed 초록 확인"),
 pm(11, "Transcriptional response to sulfide in the Echiuran Worm Urechis unicinctus by digital gene expression analysis.", "BMC Genomics 2015;16:829", "26487380", "10.1186/s12864-015-2094-z", "BMC Genomics", "PubMed 초록 확인"),
 pm(12, "Sulfide:quinone oxidoreductase from echiuran worm Urechis unicinctus.", "Mar Biotechnol 2011;13(1):93-107", "20419499", "10.1007/s10126-010-9273-3", "Marine Biotechnology", "PubMed 초록 확인"),
 pm(13, "Characteristics and function of sulfur dioxygenase in Echiuran worm Urechis unicinctus.", "PLoS One 2013;8(12):e81885", "24312599", "10.1371/journal.pone.0081885", "PLoS One", "PubMed 초록 확인"),
 pm(14, "Swimming behavior of the spoon worm Urechis unicinctus (Annelida, Echiura).", "Zoology 2014;117(3):216-23", "24698400", "10.1016/j.zool.2013.12.001", "Zoology", "PubMed 초록 확인"),
 pm(15, "Molecular Detection of Eukaryotic Diets and Gut Mycobiomes in Two Marine Sediment-Dwelling Worms, Sipunculus nudus and Urechis unicinctus.", "Microbes Environ 2018;33(3):290-300", "30146540", "10.1264/jsme2.ME18065", "Microbes and Environments", "PubMed 초록 확인"),
 pm(16, "Identification of the principal neuropeptide MIP and its action pathway in larval settlement of the echiuran worm Urechis unicinctus.", "BMC Genomics 2024;25(1):337", "38641568", "10.1186/s12864-024-10228-y", "BMC Genomics", "PubMed 초록 확인"),
 pm(17, "Transcriptome Analysis of Larval Segment Formation and Secondary Loss in the Echiuran Worm Urechis unicinctus.", "Int J Mol Sci 2019;20(8):1806", "31013695", "10.3390/ijms20081806", "International Journal of Molecular Sciences", "PubMed 초록 확인"),
 pm(18, "A chromosome-level genome assembly of the Echiura Urechis unicinctus.", "Sci Data 2024;11(1):90", "38238346", "10.1038/s41597-023-02885-7", "Scientific Data", "PubMed 초록 확인"),
 pm(19, "Draft genome sequence data of Urechis unicinctus, a marine echiuroid worm.", "Data Brief 2021;36:107032", "33981817", "10.1016/j.dib.2021.107032", "Data in Brief", "PubMed 초록 확인"),
 pm(20, "Analysis of chromosome karyotype and genome size in echiuran Urechis unicinctus Drasche, 1880 (Polychaeta, Urechidae).", "Comp Cytogenet 2019;13(1):75-85", "30918599", "10.3897/CompCytogen.v13i1.31448", "Comparative Cytogenetics", "PubMed 초록 확인"),
 pm(21, "Phylogenetic analyses of complete mitochondrial genome of Urechis unicinctus (Echiura) support that echiurans are derived annelids.", "Mol Phylogenet Evol 2009;52(2):558-62", "19306935", "10.1016/j.ympev.2009.03.009", "Molecular Phylogenetics and Evolution", "PubMed 서지 확인(초록 없음, 제목 내용만 인용)"),
 pm(22, "Echiuran Hox genes provide new insights into the correspondence between Hox subcluster organization and collinearity pattern.", "Proc Biol Sci 2022;289(1982):20220705", "36264643", "10.1098/rspb.2022.0705", "Proceedings of the Royal Society B", "PubMed 초록 확인"),
 pm(23, "Efficient Microinjection and CRISPR/Cas9 Mediated Genome Editing in Urechis unicinctus.", "Mar Biotechnol 2026;28(5)", "42684483", "10.1007/s10126-026-10702-6", "Marine Biotechnology", "PubMed 초록 확인"),
 pm(24, "Biochemical and enzymatic properties of a novel marine fibrinolytic enzyme from Urechis unicinctus.", "Appl Biochem Biotechnol 2007;136(3):251-64", "17625232", "10.1007/s12010-007-9024-8", "Applied Biochemistry and Biotechnology", "PubMed 초록 확인"),
 pm(25, "Purification and characterization of a new serine protease with fibrinolytic activity from the marine invertebrate, Urechis unicinctus.", "Appl Biochem Biotechnol 2013;170(3):525-40", "23553102", "10.1007/s12010-013-0168-4", "Applied Biochemistry and Biotechnology", "PubMed 초록 확인"),
 pm(26, "UFEIII, a fibrinolytic protease from the marine invertebrate, Urechis unicinctus.", "Biotechnol Lett 2013;35(7):1115-20", "23515896", "10.1007/s10529-013-1187-5", "Biotechnology Letters", "PubMed 초록 확인"),
 pm(27, "Antithrombotic effects of a newly purified fibrinolytic protease from Urechis unicinctus.", "Thromb Res 2013;132(2):e135-44", "23891134", "10.1016/j.thromres.2013.07.001", "Thrombosis Research", "PubMed 초록 확인(투여 경로는 초록에 없음)"),
 pm(28, "Two novel tachykinin-related neuropeptides in the echiuroid worm, Urechis unicinctus.", "Biochem Biophys Res Commun 1993;192(1):1-6", "8476410", "10.1006/bbrc.1993.1373", "Biochemical and Biophysical Research Communications", "PubMed 초록 확인"),
 pm(29, "Urechistachykinin I induced ferroptosis by accumulating reactive oxygen species in Vibrio vulnificus.", "Appl Microbiol Biotechnol 2023;107(24):7571-7580", "37796305", "10.1007/s00253-023-12802-y", "Applied Microbiology and Biotechnology", "PubMed 초록 확인"),
 pm(30, "Improvement of erectile dysfunction by the active pepide from Urechis unicinctus by high temperature/pressure and ultra-wave assisted lysis in Streptozotocin Induced Diabetic Rats.", "Int Braz J Urol 2016;42(4):825-37", "27564297", "10.1590/S1677-5538.IBJU.2015.0606", "International Braz J Urol", "PubMed 초록 확인"),
 pm(31, "Toxic effect of chromium on nonspecific immune, bioaccumulation, and tissue structure of Urechis unicinctus.", "Environ Sci Pollut Res 2024;31(15):23077-23090", "38416356", "10.1007/s11356-024-32441-8", "Environmental Science and Pollution Research", "PubMed 초록 확인"),
 pm(32, "Nonspecific immune, histology and accumulation of marine worm, Urechis unicinctus in response to bisphenol A (BPA).", "Ecotoxicol Environ Saf 2024;271:115993", "38271890", "10.1016/j.ecoenv.2024.115993", "Ecotoxicology and Environmental Safety", "PubMed 초록 확인"),
 pm(33, "D-galactoside-specific lectins from the body wall of an echiuroid (Urechis unicinctus) and two annelids (Neanthes japonica and Marphysa sanguinea).", "Comp Biochem Physiol B 1997;118(1):1-6", "9417987", "10.1016/s0305-0491(97)00014-x", "Comparative Biochemistry and Physiology Part B", "PubMed 초록 확인"),
 pm(34, "Lophotrochozoan relationships and parasites. A snap-shot.", "Parasite 2008;15(3):329-32", "18814703", "10.1051/parasite/2008153329", "Parasite", "PubMed 초록 확인(총설)"),
 pm(35, "Effects of Aged Polymethylmethacrylate Microplastics on Physiological Biochemistry and Intestinal-Sediment Microbial Communities of Urechis unicinctus (von Drasche, 1881).", "Animals 2026;16(18):2829", "42791686", "10.3390/ani16182829", "Animals", "PubMed 초록 확인"),
]

sections = [
 {"key": "overview", "title": "한눈에 보기", "body":
  "개불(Urechis unicinctus)은 개불과(Urechidae)에 속하는 바다 무척추동물로, 연안 갯벌의 부드러운 퇴적물에 U자 모양 굴을 파고 사는 소시지 모양의 의충동물(Echiura)이다[11, 18]. 의충동물은 분자계통 분석에서 환형동물 안에 포함되는 무리로 정리된다[21, 34]. 식약처 「식품원료 목록」에는 이 학명으로 '개불' 한 줄이 수산물 식품원료(A코드)로 올라 있고 상태는 '사용가능'이다[1]. 부위 칸은 원자료 표기 그대로 '-'이고 사용조건·영문명·이명 칸은 비어 있어, 목록상 특정 부위나 조건으로 제한되어 있지 않다[1]. 건강기능식품 고시형 원료의 원재료가 아니어서 식약처가 정한 지표성분은 없고, 「식품 등의 생산실적」 건강기능식품 품목에서도 개불 원료 품목은 찾지 못했다[1, 2].\n\n"
  "개불은 주로 중국·한국·일본 일부 지역에서 먹는 비전통 수산물로 소개된다[3]. 감칠맛은 다른 수산물과 달리 유리아미노산 가운데 알라닌이 많은 데서 비롯한다고 보고되었고, 지방산은 n-6/n-3 비가 0.15로 낮았다[3, 4]. 학술적으로는 황화물 내성, 유생 발달, 피브린 분해효소 등이 많이 연구되었다[12, 16, 24]. 다만 효소·펩타이드 연구는 정제 물질의 시험관·동물 실험이어서 개불을 먹었을 때의 효과를 보여 주지 않는다[26, 27, 30]."},
 {"key": "history", "title": "이용과 연구의 역사", "body":
  "개불의 학명에 붙는 명명 연도는 문헌에 따라 1880년 또는 1881년으로 다르게 적혀 있다[20, 35]. 영문으로는 'spoon worm', 'penis fish' 등으로 불리고, 중국 문헌은 '바다 창자(sea intestine)', '벌거벗은 해삼(naked sea cucumber)' 같은 별칭을 소개한다[3, 6, 9]. 중국 연구진은 개불 이용이 아직 주로 요리 형태에 머물러 있고 조미료 같은 가공 연구는 적다고 적었다[6].\n\n"
  "1990년대 초에는 개불의 배쪽 신경삭에서 체벽 근육을 수축시키는 타키키닌 유사 신경펩타이드 우레키스타키키닌 I·II 가 분리되었다[28]. 2007년에는 개불 피브린 분해효소(UFE)의 효소 성질이 보고되었고, 2013년에는 UFEII·UFEIII 가 정제되었다[24–26]. 2010년 무렵부터는 갯벌 퇴적물의 독성 물질인 황화물을 견디는 기전이 연구되었다[11–13]. 일본 미야기현 연안에서는 겨울밤 썰물 때 개불이 헤엄치거나 해변에 밀려 올라오는 현상이 오래 알려져 폭풍 탓으로 여겨졌으나, 2012–2013년 관찰에서는 번식과 관련된 행동일 가능성이 제시되었다[14]. 2020년대에는 유전체 해독과 유전자 편집 방법이 갖춰졌고, 연구진은 이를 분자 육종의 기반으로 소개했다[18, 23]."},
 {"key": "biology", "title": "종의 특징·생태", "body":
  "개불은 중국 보하이만과 한국·일본 연안에 분포한다고 기술되며, 보하이만에서는 개불속(Urechis)의 유일한 종이다[9, 10]. 연안 갯벌에 U자 굴을 파고 사는 저서동물로, 북동아시아에서 상업적·생태적으로 중요한 무척추동물로 소개된다[11]. 장 내용물의 18S rRNA 분석에서는 섬모충·규조류·와편모조류·해조류·육상식물 등 다양한 진핵생물이 검출되었고, 소화관 구간에 따라 조성이 달라 점진적 소화를 반영했다[15].\n\n"
  "갯벌 퇴적물에는 독성 물질인 황화물이 많은데, 개불은 높은 농도의 황화물을 견디며 미토콘드리아의 황화물:퀴논 산화환원효소(SQR)와 황 이산소화효소(SDO)로 황화물을 산화해 해독한다[12, 13]. SQR 유전자는 중장에서 가장 많이 발현되었고 항문낭·체강액 세포, 체벽·후장 순이었다[12]. 일본 연안에서 겨울밤 헤엄치거나 좌초한 개체는 모두 생식세포가 없어 산란을 마친 상태로 보였고, 같은 시기 플랑크톤에서 담륜자 유생이 함께 나타났다[14]. 유생은 체절이 생겼다가 다시 사라지는 단계를 거쳐 벌레 모양 유생이 되며, 이 체절의 이차 소실은 의충동물과 환형동물의 관계를 보여 주는 특징으로 여겨진다[17]. 유생이 바닥에 내려앉는 착저는 신경펩타이드 MIP2 가 섬모 관련 유전자를 억제해 유도하는 것으로 보고되었다[16]."},
 {"key": "related_species", "title": "관련 종·이름", "body":
  "식약처 「식품원료 목록」 원자료에서 학명 Urechis 로 올라 있는 원료는 개불(U. unicinctus) 한 줄뿐이다[1]. 따라서 Urechis caupo 등 다른 개불속 종은 목록에 없으며, 이 문서에는 그 종들의 자료를 넣지 않았다[1]. 의충동물은 한때 독립된 문으로 다뤄졌으나 분자계통 분석에서 환형동물 안에 들어가는 것으로 나타났고, 개불 미토콘드리아 유전체 분석도 이를 지지했다[21, 34].\n\n"
  "개불과 함께 먹는 갯벌 동물로 비교되는 땅콩벌레류(peanut worm, Sipunculus nudus)는 개불과 다른 무리이며, 지방산 조성도 달라 곁가지지방산이 약 3%(wt/wt)로 많았다[3]. 두 종은 장 속 먹이 조성 연구에서도 따로 분석되었다[15]. 개불 체벽의 D-갈락토사이드 결합 렉틴은 환형동물 Neanthes japonica·Marphysa sanguinea 의 렉틴과 면역학적으로 비슷했지만 척추동물 갈렉틴과는 달랐다[33]. 중국 별칭에 '해삼'이 들어 있지만 개불은 극피동물인 해삼과 다른 동물이다[6, 18]. 영문명 'penis fish'는 집단유전 논문 제목에도 쓰였다[9]."},
 {"key": "cultivation", "title": "어획·양식", "body":
  "중국에서는 남획으로 야생 집단이 급감했고, 일본에서도 야생 집단이 크게 줄었다고 보고된다[9, 10]. 중국 연구진은 개불을 경제적으로 중요한 양식 대상종으로 소개하며, 실험 시료를 산둥성 옌타이의 종묘(양식) 기지나 칭다오·옌타이의 수산시장에서 구했다[6–8, 23]. 양식 집단 사이 알라닌 함량 차이는 알라닌 아미노기전이효소(GPT)의 활성·유전자 발현과 관련될 수 있다고 보고되었다[4]. 양식 수질 관리의 참고 자료로 6가 크롬·비스페놀 A 노출 실험이 이루어졌다[31, 32].\n\n"
  "활어 유통에는 저온 무수(물 없이) 운송이 알맞은 방법으로 제시되었고, 최적 운송 시간은 48시간이었다[5]. 이보다 길어지면 산화 스트레스·대사 이상·지질 변성·조직 손상이 생기고 올레산에틸 같은 해로운 대사산물이 늘어 무게 감소와 관능 품질 저하로 이어졌다[5]. 국내 어획량·양식 생산량에 관한 해양수산부·통계청 공식 통계는 확인하지 못함. 국내 인공종자 생산과 양식 현황도 공공기관 원문으로 확인하지 못함."},
 {"key": "processing", "title": "가공·이용·성분", "body":
  "식품으로서의 조리·가공에 관한 공공기관 자료는 확인하지 못함. 내장을 뺀 개불을 동결건조·분쇄한 뒤 트립신·알칼리 단백질분해효소로 가수분해한 시료는 총아미노산이 486.65 mg 으로, 글루탐산 72.810 mg/g, 글리신 68.025 mg/g, 알라닌 60.785 mg/g, 아스파르트산 56.540 mg/g 순으로 많았다[6]. 이 가수분해물을 포도당과 120 °C 에서 2시간 메일라드 반응시키자 비린내와 관련된 알데하이드 비율이 14.21%에서 3.33%로 줄었고, 연구진은 이를 원료로 해산물 조미료 시제품을 만들었다[6]. 같은 논문 서론은 개불 단백질이 건조중량의 약 71.01%라고 다른 문헌을 인용해 적었다[6].\n\n"
  "가공 때 버려지는 내장은 초음파 보조 효소 가수분해로 가수분해도 79.32%의 단백질 가수분해물이 되었고, 여기서 펩타이드 3종(VTSALVGPR 등)이 분리되었다[7]. 이 펩타이드의 항산화 효과는 세포 실험까지만 확인되었다[7]. 먹지 않는 부산물인 체강액에서는 황산화 다당이 추출되었고, 수율은 체강액 습중량 기준 1.51–3.80‰ 였다[8]. 고온·고압·초음파로 얻은 개불 펩타이드를 당뇨 쥐에 8주간 100·500 mg/kg/일 경구 투여한 동물 실험도 있으나 동물 결과일 뿐이다[30]. 건강기능식품 원료로 생산된 실적은 찾지 못했다[2]."},
 {"key": "genetics", "title": "유전 정보", "body":
  "2021년 첫 초안 유전체가 공개되었고, 2024년에는 PacBio 장독 서열·Illumina 단독 서열·Hi-C 를 결합한 염색체 수준 유전체가 발표되었다[18, 19]. 이 유전체는 약 1,138.6 Mb, scaffold N50 68.3 Mb 이며 1,113.8 Mb(97.82%)가 17개 유사염색체에 배치되었다[18]. 단백질 암호 유전자 21,524개와 반복서열 482.1 Mb 가 주석되었다[18]. 유세포 분석으로 잰 2C DNA 양은 1.85 pg(약 904.58 Mbp)이고 핵형은 2n = 30 으로, 조립 유전체 크기와는 측정법에 따라 차이가 있다[18, 20]. 미토콘드리아 유전체 전체도 해독되어 계통 분석에 쓰였다[21].\n\n"
  "중국 보하이만과 한국 연안 105개체의 COI 분석에서 반수체형 다양도는 0.9595로 높았고 지역 간 분화는 낮아, 중국·일본·한국 연안 개체를 하나의 집단으로 보전해야 한다고 제안되었다[9]. 보하이만 150여 개체의 COI·D-loop 분석에서도 지역이나 몸 색에 따른 뚜렷한 무리는 없었다[10]. Hox 유전자는 비Hox 유전자로 나뉜 네 개의 하위 군집을 이룬다[22]. 2026년에는 미세주입을 이용한 CRISPR/Cas9 유전자 편집 방법이 확립되었다[23]. 식품 진위 판별용 표준 DNA 바코드 기준은 확인하지 못함."},
 {"key": "safety", "title": "안전성과 사용 조건", "body":
  "식약처 「식품원료 목록」에서 개불은 부위·사용조건 제한 없이 '사용가능' 수산물 원료로 분류되어 있다[1]. 개불에 관한 공공기관의 알레르기·잔류물질·식중독 정보는 확인하지 못함. 활어로 유통할 때 저온 무수 운송이 48시간을 넘으면 올레산에틸 같은 해로운 대사산물이 늘고 품질이 떨어진다고 보고되었다[5].\n\n"
  "실험실 노출 시험에서 개불은 물속 6가 크롬을 근육에 농도에 비례해 축적했고, 비스페놀 A 도 노출 시간이 길수록 근육에 많이 쌓였다[31, 32]. 노화된 미세플라스틱(PMMA)도 21일 노출 시험에서 체벽과 장에 축적되었다[35]. 이는 인위적으로 노출시킨 실험이어서 시판 개불의 오염 수준을 뜻하지 않으며, 시판품 모니터링 자료는 확인하지 못함. 피브린 분해효소 UFEIII 는 정제 효소를 쥐·토끼에 투여했을 때 혈액 응고 시간을 늘리고 피브리노겐을 줄였으나, 정제 효소의 약리 실험이라 식품 섭취와는 다르다[27]. UFEII 는 출혈 작용을 보이지 않았다고 보고되었으나, 이 역시 정제 효소의 시험 결과다[25]."},
]

compounds = [
 {"name": "L-Alanine", "name_ko": "알라닌", "class": "아미노산", "role": "marker", "part": "근육(유리아미노산); 체벽 가수분해물",
  "content_text": "유리아미노산 중 고농도로 감칠맛의 주원인(초록에 수치 없음)[4]; 내장 제거 체벽 효소 가수분해물 60.785 ± 5.936 mg/g[6]",
  "activity_ko": "개불 감칠맛의 핵심 성분으로 보고(맛 성분, 효능 아님)[4]", "source": [4, 6]},
 {"name": "L-Glutamic acid", "name_ko": "글루탐산", "class": "아미노산", "role": "nutrient", "part": "체벽 효소 가수분해물(동결건조 분말)",
  "content_text": "72.810 ± 8.481 mg/g(가수분해물), 메일라드 반응 후 47.111 ± 6.178 mg/g[6]", "activity_ko": "감칠맛 아미노산[6]", "source": [6]},
 {"name": "Glycine", "name_ko": "글리신", "class": "아미노산", "role": "nutrient", "part": "체벽 효소 가수분해물(동결건조 분말)",
  "content_text": "68.025 ± 1.152 mg/g(가수분해물)[6]", "activity_ko": "단맛 아미노산(맛 성분)[6]", "source": [6]},
 {"name": "L-Aspartic acid", "name_ko": "아스파르트산", "class": "아미노산", "role": "nutrient", "part": "체벽 효소 가수분해물(동결건조 분말)",
  "content_text": "56.540 ± 3.852 mg/g(가수분해물)[6]", "activity_ko": "감칠맛 아미노산[6]", "source": [6]},
 {"name": "L-Leucine", "name_ko": "류신", "class": "필수아미노산", "role": "nutrient", "part": "체벽 효소 가수분해물(동결건조 분말)",
  "content_text": "29.416 ± 3.407 mg/g(가수분해물), 메일라드 반응 후 18.724 ± 2.705 mg/g[6]", "activity_ko": "쓴맛 아미노산으로 메일라드 반응 중 크게 줄어듦[6]", "source": [6]},
 {"name": "Omega-3 fatty acids", "name_ko": "n-3 다중불포화지방산", "class": "다중불포화지방산", "role": "nutrient", "part": "몸(부위 초록에 명시 없음)",
  "content_text": "n-6/n-3 PUFA 비 0.15(개별 함량은 초록에 없어 확인하지 못함)[3]", "activity_ko": "저자들은 n-6/n-3 불균형을 보완할 잠재 식품으로 해석(효능 시험 아님)[3]", "source": [3]},
 {"name": "Docosatrienoic acid (22:3, 7Z,13Z,16Z)", "name_ko": "도코사트리엔산(22:3, 7Z,13Z,16Z)", "class": "폴리메틸렌 단속형 PUFA", "role": "marker", "part": "몸(부위 초록에 명시 없음)",
  "content_text": "개불·땅콩벌레류 분석에서 새로 동정된 시아돈산 유래 PUFA, 함량과 어느 종에서 나왔는지는 초록으로 확인하지 못함[3]", "activity_ko": "특이 지방산 구조로 보고(생리 기능 미상)[3]", "source": [3]},
 {"name": "Ethyl oleate", "name_ko": "올레산에틸", "class": "지방산 에스터(대사산물)", "role": "marker", "part": "몸 전체(활어 운송 중)",
  "content_text": "저온 무수 운송 48시간 초과 시 증가(수치는 초록에 없음)[5]", "activity_ko": "저자들이 품질 저하와 함께 늘어나는 해로운 대사산물로 지목[5]", "source": [5]},
 {"name": "Sulfated polysaccharide (coelomic fluid)", "name_ko": "체강액 황산화 다당", "class": "황산화 헤테로다당", "role": "bioactive", "part": "체강액(먹지 않는 부산물)",
  "content_text": "수율 1.51–3.80‰(체강액 습중량 기준), 분획별 황산기 3.77–24.26%[8]", "activity_ko": "라디칼 소거와 SH-SY5Y 세포 저산소·재산소화 모델 보호(시험관·세포 실험)[8]", "source": [8]},
 {"name": "VTSALVGPR", "name_ko": "내장 항산화 펩타이드 P1(VTSALVGPR)", "class": "펩타이드", "role": "bioactive", "part": "내장(효소 가수분해물)",
  "content_text": "분자량 898.5 Da, 함량 확인하지 못함[7]", "activity_ko": "H2O2 손상 RAW264.7 세포 생존율 회복(세포 실험)[7]", "source": [7]},
 {"name": "Urechistachykinin I", "name_ko": "우레키스타키키닌 I", "class": "신경펩타이드(LRQSQFVGSR-NH2)", "role": "bioactive", "part": "배쪽 신경삭",
  "content_text": "배쪽 신경삭에서 분리, 함량 확인하지 못함[28]", "activity_ko": "체벽 내환근 수축 작용[28]; 합성 펩타이드가 Vibrio vulnificus 에 항균 작용(시험관)[29]", "source": [28, 29]},
 {"name": "Urechis unicinctus fibrinolytic enzyme UFEIII", "name_ko": "개불 피브린 분해효소(UFEIII)", "class": "세린 단백질분해효소(약 20.8 kDa)", "role": "bioactive", "part": "몸(정제 효소)",
  "content_text": "총 섬유소 분해 활성 1.46 × 10^3 U(유로키나아제 단위)/mg 단백질[26]", "activity_ko": "정제 효소를 쥐·토끼에 투여 시 혈전 용해·응고 시간 연장(동물 실험, 식품 섭취 효과 아님)[27]", "source": [26, 27]},
 {"name": "Urechis unicinctus fibrinolytic enzyme UFEII", "name_ko": "개불 피브린 분해효소(UFEII)", "class": "키모트립신 유사 세린 단백질분해효소(26.7 kDa)", "role": "bioactive", "part": "몸(정제 효소)",
  "content_text": "정제 효소의 성질만 보고, 몸속 함량 확인하지 못함[25]", "activity_ko": "피브린·피브리노겐 직접 분해와 플라스미노겐 활성화(시험관), 출혈 작용 없음으로 보고(정제 효소 시험)[25]", "source": [25]},
 {"name": "D-galactoside-binding lectin", "name_ko": "체벽 D-갈락토사이드 결합 렉틴", "class": "렉틴(36 kDa 주성분)", "role": "bioactive", "part": "체벽",
  "content_text": "주 단백질 36 kDa, 부 단백질 40·14 kDa; 함량 확인하지 못함[33]", "activity_ko": "당 결합 활성(시험관)[33]", "source": [33]},
]

def cond(**kw):
    keys = ["instrument","column","mobile_phase","gradient","flow","temp","detection","injection","sample_prep","standard","linearity","lod","loq","recovery"]
    return {k: kw.get(k, "") for k in keys}

assays = [
 {"role": "literature", "compound": "Amino acids (Glu, Gly, Ala, Asp 등 18종)", "compound_ko": "아미노산 조성",
  "part": "체벽(내장 제거) 효소 가수분해물 동결건조 분말",
  "content": "총 486.65 mg; Glu 72.810, Gly 68.025, Ala 60.785, Asp 56.540 mg/g(가수분해물)[6]",
  "method": "HPLC-UV(C18)",
  "conditions": cond(instrument="HPLC(제조사 기재 없음)", column="C18 칼럼(5 μm, 4.6 × 250 mm)",
    mobile_phase="A: 0.1 mol/L 아세트산나트륨(pH 6.50):아세토니트릴 = 93:7, B: 물:아세토니트릴 = 20:80",
    gradient="0–0.01분 100% A; 0.01–35분 A 100→0%; 35–42분 100% B; 42–45분 A 0→100%; 총 60분",
    flow="1.0 mL/min", temp="40 °C", detection="254 nm", injection="10 μL",
    sample_prep="내장 제거 → −80 °C 저장 → 24시간 동결건조·분쇄 → 트립신:알칼리 단백질분해효소 21.2:8.8 복합효소, 초음파 54.95분, 액체:시료 52:1, 효소 3.17%, pH 8.58, 50.48 °C, 3.16시간 가수분해 → 95 °C 효소 불활성화 → 원심분리 상등액 동결건조",
    standard="아미노산 혼합 표준용액"),
  "rationale": "개불 맛(감칠맛·단맛)과 단백질 영양 특성을 보여 주는 성분군이며, 같은 논문에서 메일라드 반응 전후 비교 지표로 썼다; 선형성·검출한계·회수율은 원문에 없음[6]",
  "source": [6], "url": "https://doi.org/10.3389/fnut.2024.1325886", "source_kind": "paper"},
 {"role": "literature", "compound": "Sulfate groups of coelomic fluid polysaccharides", "compound_ko": "체강액 다당의 황산기",
  "part": "체강액(다당 분획 12종)",
  "content": "분획별 황산기 3.77–24.26%(U18P 24.26 ± 1.19%, U68P 18.47%); 다당 수율 1.51–3.80‰(체강액 습중량 기준)[8]",
  "method": "염화바륨–젤라틴 비탁법(황산기), HPLC-RID(분자량), HPAEC-PAD(단당 조성)",
  "conditions": cond(instrument="황산기: 마이크로플레이트 리더 360 nm; 분자량: HPLC(RID); 단당: HPAEC-PAD",
    column="분자량: TSKgel G3000SWXL(7.5 mm × 300 mm); 단당: CarboPac PA20(가드칼럼 포함)",
    mobile_phase="분자량: 50 mmol/L Na2SO4; 단당: 초순수, 200 mM NaOH, 200 mM NaOH + 500 mM 아세트산나트륨 기울기",
    flow="분자량: 0.6 mL/min", temp="분자량: 40 °C", detection="황산기: 360 nm 탁도; 분자량: 굴절률 검출기; 단당: 펄스 전류 검출",
    sample_prep="체강액 1:3 희석·균질 → 60 °C 또는 100 °C 6시간 열수 추출 3회 → 트립신·파파인·중성·알칼리 단백질분해효소(각 0.2%) 순차 처리 → 에탄올 30·50·80% 분획 침전 → 투석·동결건조 → DEAE-52 음이온교환(물, 0–0.5 mol/L NaCl). 황산기: 1 mol/L HCl, 100 °C 6시간 가수분해; 단당: 4 mol/L TFA, 115 °C 4시간",
    standard="황산기: K2SO4; 분자량: 덱스트란 계열 표준(원문 'Dextrorotatory glycoside'); 총당: D-글루코스"),
  "rationale": "체강액 다당의 구조적 특징(황산화 정도)이 항산화·세포 보호 활성과 관련된다고 저자들이 해석한 지표; 체강액은 먹지 않는 부산물이라고 원문에 적혀 있다[8]",
  "source": [8], "url": "https://doi.org/10.3390/polym18101203", "source_kind": "paper"},
 {"role": "literature", "compound": "Antioxidant peptides (VTSALVGPR, IGLGDEGLRR, TKIRNEISDLNER)", "compound_ko": "내장 항산화 펩타이드",
  "part": "내장 단백질 가수분해물(<10 kDa, Sephadex G-25 분획)",
  "content": "정성 동정(분자량 898.5, 1084.6, 1586.8 Da), 함량 정량 없음[7]",
  "method": "LC-MS/MS(나노 C18, 양이온 모드) 서열 동정",
  "conditions": cond(instrument="LC-MS/MS(고분해능 질량분석, 제조사 기재 없음)", column="Acclaim PepMap 100 C18 트랩",
    mobile_phase="A: 물 + 0.1% 포름산; B: 아세토니트릴 + 0.1% 아세트산(원문 표기)",
    gradient="0–6분 B 5–8%; 6–40분 8–30%; 40–45분 30–60%; 45–48분 60–80%; 48–56분 80%; 56–58분 80–5%; 58–65분 5%",
    flow="0.4 μL/min", detection="양이온 모드, 이온원 전압 1800 V, 모세관 360 °C; MS1 350–20,000(원문 'DA'), 분해능 70,000; MS2 분해능 17,500",
    injection="10 μL",
    sample_prep="내장 에틸아세테이트 탈지·건조·분쇄 → 물 27:1(mL/g), pH 7 → 파파인 0.6%·트립신 1.44%·알칼리 단백질분해효소 0.96%, 초음파 675 W 33분 → 50.0 °C 2.0시간 → 95 °C 15분 불활성화 → 원심 → 활성탄 탈색 → 동결건조 → 한외여과(10·30 kDa) → Sephadex G-25(물, 0.5 mL/min, 280 nm) → 탈염·0.22 μm 여과"),
  "rationale": "버려지는 내장의 이용 가능성을 보인 성분이지만 정량이 아닌 서열 동정이며, 활성은 세포 실험 결과다[7]",
  "source": [7], "url": "https://doi.org/10.3390/md20050293", "source_kind": "paper"},
 {"role": "literature", "compound": "Fatty acids (n-6/n-3 PUFA, PMI-PUFA)", "compound_ko": "지방산 조성",
  "part": "몸(부위 초록에 명시 없음)",
  "content": "n-6/n-3 PUFA 비 0.15; 22:3(7Z,13Z,16Z) 등 폴리메틸렌 단속형 PUFA 동정[3]",
  "method": "공유결합 부가물 화학이온화(CACI) 탠덤 질량분석",
  "conditions": cond(),
  "rationale": "개불 지질의 영양적 특징으로 저자들이 강조한 지표; 전문 확인 못함(초록만 열람)[3]",
  "source": [3], "url": "https://doi.org/10.1016/j.foodchem.2024.141287", "source_kind": "paper"},
]

d = {
 "slug": "urechis-unicinctus", "name_ko": "개불", "name_en": "Spoon worm", "scientific_name": "Urechis unicinctus",
 "aliases": ["개불", "Spoon worm", "Penis fish", "Sea intestine", "Naked sea cucumber"],
 "sections": sections, "compounds": compounds, "markers": [], "assays": assays, "nutrients": [],
 "production": [], "world": [], "gi": [], "orgs": [], "sources": S,
}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in sections: print(s["key"], len(s["body"]))
