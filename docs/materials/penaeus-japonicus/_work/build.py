import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
A = "2026-11-02"
def src(n, title, doi, pub, pmid, pmc=None):
    p = f"{pub} (PubMed {pmid}" + (f", {pmc})" if pmc else ")")
    return {"n": n, "title": title, "url": f"https://doi.org/{doi}", "publisher": p, "accessed": A}
sources = [
 {"n": 1, "title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 보리새우·건보리새우·건보리새우분해농축액(Penaeus japonicus) 항목(원자료 I1020_20261013.json)", "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
 src(2, "Molecular cloning and allergenicity of Pen j 1, a major allergen of kuruma prawn, Penaeus japonicus. Biosci Biotechnol Biochem 2009;73(4):840-8", "10.1271/bbb.80751", "Bioscience, Biotechnology, and Biochemistry", "19352041"),
 src(3, "Contribution of structural reversibility to the heat stability of the tropomyosin shrimp allergen. Biosci Biotechnol Biochem 2013;77(5):948-53", "10.1271/bbb.120887", "Bioscience, Biotechnology, and Biochemistry", "23649255"),
 src(4, "Gastrointestinal digestion and absorption of Pen j 1, a major allergen from Kuruma prawn, Penaeus japonicus. Biosci Biotechnol Biochem 2011;75(7):1249-58", "10.1271/bbb.110021", "Bioscience, Biotechnology, and Biochemistry", "21737942"),
 src(5, "Thermodynamic characterization of muscle tropomyosins from marine invertebrates. Comp Biochem Physiol B 2011;160(2-3):64-71", "10.1016/j.cbpb.2011.06.001", "Comparative Biochemistry and Physiology Part B", "21722747"),
 src(6, "Sarcoplasmic calcium-binding protein: identification as a new allergen of the black tiger shrimp Penaeus monodon. Int Arch Allergy Immunol 2008", "10.1159/000113512", "International Archives of Allergy and Immunology", "18204275"),
 src(7, "Genome and transcriptome assemblies of the kuruma shrimp, Marsupenaeus japonicus. G3 (Bethesda) 2021;11(11):jkab268", "10.1093/g3journal/jkab268", "G3: Genes|Genomes|Genetics", "34515781", "PMC8527471"),
 src(8, "A chromosome-level genome of the kuruma shrimp (Marsupenaeus japonicus) provides insights into its evolution and cold-resistance mechanism. Genomics 2022;114(3):110373", "10.1016/j.ygeno.2022.110373", "Genomics", "35460816"),
 src(9, "Chromosome-level genome assembly and annotation of the kuruma shrimp Marsupenaeus japonicus. Sci Data 2025;12:2028", "10.1038/s41597-025-06317-6", "Scientific Data", "41387735", "PMC12748559"),
 src(10, "The complete mitochondrial genome of the cryptic species (Form II) in kuruma shrimp Marsupenaeus japonicus (Decapoda: Penaeidae). Mitochondrial DNA B 2018;3(1):184-186", "10.1080/23802359.2018.1437835", "Mitochondrial DNA Part B", "33490495", "PMC7800321"),
 src(11, "Genetic Diversity and Core Germplasm Identification in Penaeus japonicus Using Whole-Genome Resequencing. Animals 2025;15(18):2759", "10.3390/ani15182759", "Animals (Basel)", "41008004", "PMC12466631"),
 src(12, "Construction of a high-density linkage map and detection of sex-specific markers in Penaeus japonicus. PeerJ 2021;9:e12390", "10.7717/peerj.12390", "PeerJ", "34760384", "PMC8559604"),
 src(13, "Sexual dimorphic eyestalk transcriptome of kuruma prawn Marsupenaeus japonicus. Gene 2023;885:147700", "10.1016/j.gene.2023.147700", "Gene", "37572801"),
 src(14, "Dietary β-Hydroxy-β-Methylbutyrate Supplementation Affects Growth Performance, Digestion, TOR Pathway, and Muscle Quality in Kuruma Shrimp Fed a Low Protein Diet. Aquac Nutr 2023:9889533", "10.1155/2023/9889533", "Aquaculture Nutrition", "36860981", "PMC9973151"),
 src(15, "Preparation, Purification and Characterization of Antibacterial and ACE Inhibitory Peptides from Head Protein Hydrolysate of Kuruma Shrimp. Molecules 2023;28(2):894", "10.3390/molecules28020894", "Molecules", "36677951", "PMC9861681"),
 src(16, "Lipid Profiles of the Heads of Four Shrimp Species by UPLC-Q-Exactive Orbitrap/MS and Their Cardiovascular Activities. Molecules 2022;27(2):350", "10.3390/molecules27020350", "Molecules", "35056663", "PMC8781101"),
 src(17, "HPLC determination of the distribution of D-amino acids and effects of ecdysis on alanine racemase activity in kuruma prawn Marsupenaeus japonicus. J Chromatogr B 2011;879(29):3283-8", "10.1016/j.jchromb.2011.04.026", "Journal of Chromatography B", "21592870"),
 src(18, "Changes in free amino acid concentrations and associated gene expression profiles in the abdominal muscle of kuruma shrimp acclimated at different salinities. J Exp Biol 2018;221(Pt 11)", "10.1242/jeb.168997", "Journal of Experimental Biology", "29674374"),
 src(19, "A study of the lipids and carotenoprotein in the prawn, Penaeus japonicus. J Biochem 1993;114(2):223-9", "10.1093/oxfordjournals.jbchem.a124158", "Journal of Biochemistry", "8262903"),
 src(20, "Structures of Yellow Xanthophylls and Metabolism of Astaxanthin in the Prawn Penaeus japonicus. J Oleo Sci 2018;67(11):1425-1433", "10.5650/jos.ess18103", "Journal of Oleo Science", "30404963"),
 src(21, "Improvement of red color development on the surface of kuruma prawn Marsupenaeus japonicus under various conditions. J Food Sci 2014;79(2):E202-7", "10.1111/1750-3841.12353", "Journal of Food Science", "24456388"),
 src(22, "Extension of the shelf life of prawns (Penaeus japonicus) by vacuum packaging and high-pressure treatment. J Food Prot 2000;63(10):1381-8", "10.4315/0362-028x-63.10.1381", "Journal of Food Protection", "11041138"),
 src(23, "Change in the Contents of Arginine, Ornithine, and Urea in the Muscle of Marine Invertebrates Stored in Ice. Biosci Biotechnol Biochem 1992;56(6):863-6", "10.1271/bbb.56.863", "Bioscience, Biotechnology, and Biochemistry", "27280809"),
 src(24, "Sand Substrate Thickness Regulates Growth Performance, Intestinal Antioxidant Defense, and Gut Microbiota in an Experimental Culture of Kuruma Shrimp. Animals 2026;16(4):586", "10.3390/ani16040586", "Animals (Basel)", "41751047", "PMC12937321"),
 src(25, "Crustacean cardioactive peptide (CCAP) negatively regulates sand-diving behaviour in kuruma shrimp, Penaeus japonicus. Comp Biochem Physiol B 2025:111143", "10.1016/j.cbpb.2025.111143", "Comparative Biochemistry and Physiology Part B", "40812679"),
 src(26, "Development of a polymerase chain reaction (PCR) procedure for the detection of baculovirus associated with white spot syndrome (WSBV) in penaeid shrimp. J Fish Dis 1998;21(1):11-17", "10.1046/j.1365-2761.1998.00324.x", "Journal of Fish Diseases", "29739168"),
 src(27, "Primary culture of lymphoid organ cells and haemocytes of kuruma shrimp, Penaeus japonicus. Methods Cell Sci 1999;21(4):237-44", "10.1023/a:1009845103353", "Methods in Cell Science", "10627678"),
 src(28, "Characterization of a non-occluded baculovirus-like agent pathogenic to penaeid shrimp. Dis Aquat Organ 1998;33(3):221-9", "10.3354/dao033221", "Diseases of Aquatic Organisms", "9745719"),
 src(29, "Comparative genomics of Photobacterium damselae from Penaeus (Marsupenaeus) japonicus: insights into pathogenicity and adaptation. Dis Aquat Organ 2026;168:1-17", "10.3354/dao03936", "Diseases of Aquatic Organisms", "42847339"),
 src(30, "The first crystal structure of crustacean ferritin that is a hybrid type of H and L ferritin. Protein Sci 2018;27(11):1955-1960", "10.1002/pro.3495", "Protein Science", "30099791", "PMC6201719"),
 src(31, "Utility of Stable Isotope and Cytochrome Oxidase I Gene Sequencing Analyses in Inferring Origin and Authentication of Hairtail Fish and Shrimp. J Agric Food Chem 2015;63(22):5548-56", "10.1021/acs.jafc.5b01469", "Journal of Agricultural and Food Chemistry", "25980806"),
 src(32, "Relationship closeness of tolerance to two neonicotinoids with their internal body burden in two estuarine resident marine crustaceans. Comp Biochem Physiol C 2023;268:109613", "10.1016/j.cbpc.2023.109613", "Comparative Biochemistry and Physiology Part C", "36933630"),
 src(33, "Maturation-related variations in prostaglandin and fatty acid content of ovary in the kuruma prawn (Marsupenaeus japonicus). Comp Biochem Physiol A 2004;137(4):631-7", "10.1016/j.cbpb.2003.12.005", "Comparative Biochemistry and Physiology Part A", "15123170"),
 src(34, "Scanning electron microscopy, morphometric and energy dispersive X-Ray analysis of cephalothoracic structures exploring defensive and sensory features in kuruma shrimp (Marsupenaeus japonicus Spence Bate, 1888). BMC Zool 2024;9(1):29", "10.1186/s40850-024-00219-7", "BMC Zoology", "39533391", "PMC11558839"),
 src(35, "The Effect of an Alternating Magnetic Field-Assisted Freezing Process on the Quality of Frozen Penaeus Japonicus. Foods 2025;14(23):4112", "10.3390/foods14234112", "Foods", "41376049", "PMC12692254"),
]

sections = [
 {"key": "overview", "title": "한눈에 보기", "body":
  "보리새우(Penaeus japonicus, 영문 Kuruma prawn·Kuruma shrimp)는 보리새우과(Penaeidae)에 드는 바다 새우다[1]. 최근 논문에서는 같은 종을 Marsupenaeus japonicus라는 학명으로도 많이 쓰며, 이 조사에서는 두 학명의 자료를 같은 종으로 보았다[7, 13]. 인도-서태평양의 얕고 따뜻한 바다에 넓게 살고, 맛이 좋고 값이 비싸 세계적으로 중요한 양식 새우로 꼽힌다[7, 13, 14].\n\n"
  "식약처 「식품원료 목록」에는 이 학명으로 '보리새우', '건보리새우', '건보리새우분해농축액' 세 줄이 올라 있고, 모두 분류는 수산물, 상태는 '사용가능'이다[1]. 사용 부위는 보리새우·건보리새우가 '-'(따로 정하지 않음), 건보리새우분해농축액이 '전체'로 적혀 있으며 별도의 사용 조건 문구는 없다[1].\n\n"
  "건강기능식품 고시형 원료의 원재료가 아니어서 식약처가 정한 지표성분과 기능성은 없다[1]. 국내 생산 통계와 국가표준식품성분표의 이 종 성분값은 이 조사에서 확인하지 못함."},
 {"key": "history", "title": "이용 역사", "body":
  "보리새우는 일본에서 가장 중요한 수산 자원 가운데 하나였으나 1990년대부터 어획량이 크게 줄었고, 이를 메우려고 종자 생산과 양식이 시도되었다[13]. 자연산 어획이 줄면서 양식이 시장 수요를 맞추는 주된 길이 되었다는 평가가 있다[14]. 한 논문은 FAO 통계를 인용해 2018년 세계 보리새우 생산량을 약 58,000톤으로 소개했다(FAO 원자료는 직접 확인하지 못함)[15].\n\n"
  "1990년대에는 흰반점병 계열 바이러스가 양식 산업의 큰 문제가 되었다[26, 27, 28]. 일본에서는 보리새우의 '펜에이드 막대형 DNA 바이러스(PRDV)'를 림프기관 세포 배양에 접종하면 8일 안에 세포변성이 나타났다[27]. 중국에서 들여온 빈사 상태의 보리새우에서는 흰반점증후군과 같은 계열의 바이러스(CBV)가 분리되어 그 구조가 분석되었다[28]. 국내에서도 흰반점증후군에 걸린 보리새우에서 원인 바이러스를 정제하고 이를 검출하는 PCR 방법을 개발한 연구가 1998년에 발표되었다[26].\n\n"
  "중국 저장·푸젠의 양식 집단에는 일본에서 들여온 계통도 섞여 있어, 양식 역사가 나라 사이의 종묘 이동과 이어져 있음을 보여 준다[11]."},
 {"key": "biology", "title": "종·형태·생태", "body":
  "보리새우는 바닥에 사는 십각목 갑각류로 인도-서태평양에 넓게 분포한다[13]. 1888년 Spence Bate가 기재한 종이며, 머리가슴 부분에는 더듬이·제1더듬이·비늘 모양 판(scaphocerite)·위아래 가시가 있는 이마뿔이 있고 감각과 방어에 쓰이는 털이 나 있다[34]. 에너지분산 X선 분석에서는 비늘판·이마뿔·더듬이의 창 모양 구조에 칼슘과 인 비율이 높았다[34].\n\n"
  "이 종은 모래 속으로 파고드는 습성이 뚜렷하며, 갑각류 심장활성 펩타이드(CCAP) 유전자를 RNA 간섭으로 줄이거나 과발현시키면 6시간 뒤 모래 파고들기 비율이 달라져 CCAP가 이 행동의 음성 조절자일 가능성이 제시되었다[25]. 이 CCAP 유전자는 근육에서 가장 많이 발현되었다[25]. 암컷이 수컷보다 빨리, 크게 자라는 암수 차이가 있다[12].\n\n"
  "연안에 살아 염분 변화를 견디는 능력이 있으며, 염분 1.7%·3.4%·4.0%에 적응시키면 24시간 뒤부터 복부 근육의 유리아미노산이 달라지고 염분이 높을수록 글루타민과 알라닌이 크게 늘었다[18]. 조직에는 D-알라닌이 들어 있어 총 알라닌 가운데 18.7–43.7%를 차지했고, 근육·심장·아가미에 비교적 많았다[17]."},
 {"key": "related_species", "title": "관련 종·이름", "body":
  "식약처 「식품원료 목록」에는 보리새우속(Penaeus)의 여러 종이 각각 별도 원료로 올라 있으며, 보리새우는 그중 학명 Penaeus japonicus만 가리킨다[1]. 같은 목록에는 대하(P. chinensis), 범보리새우(P. esculentus), 지중해보리새우(P. kerathurus), 바나나새우(P. merguiensis), 얼룩새우(P. monodon), 홍다리얼룩새우(P. semisulcatus)가 따로 있다[1]. 이름이 비슷한 갈색보리새우(Farfantepenaeus aztecus), 인도보리새우(Fenneropenaeus indicus), 흰다리새우(Litopenaeus vannamei)도 다른 학명의 별도 원료다[1]. 따라서 원료를 확인할 때는 국명보다 학명을 함께 보아야 한다[1].\n\n"
  "보리새우는 형태로 가려내기 어려운 두 숨은 종(Form I, Form II)으로 이루어진 종 복합체로 보고되며, 중국 베이부만의 Form II 미토콘드리아 유전체는 15,966 bp로 두 형 사이에 1,029개의 변이 자리가 있었다[10]. 유전체 비교에서는 흰다리새우·얼룩새우와 가까운 관계이며 공통 조상에서 갈라진 시기가 약 8,833만 년 전으로 추정되었다[9].\n\n"
  "국내 연구진의 연구에서는 새우 시료의 cox1 유전자 서열로 보리새우(M. japonicus)를 대하·흰다리새우·얼룩새우 등과 구별할 수 있었고, 안정동위원소로 원산지와 자연산·양식산도 나눌 수 있었다[31]."},
 {"key": "cultivation", "title": "양식·어획", "body":
  "보리새우는 다른 새우보다 사료 단백질 요구량이 높은 편으로, 약 500 g/kg이 요구량으로 인용되며 단백질을 줄이면 성장이 나빠진다[14]. 사료 실험은 수온 25.0 ± 1.0 °C, 염분 28.0 ± 1.2 조건에서 바닥에 모래를 약 20 mm 깔고 진행되었다[14]. 모래 파고들기 습성 때문에 양식장 바닥 모래가 중요하며, 120일 실험에서 모래가 없으면 성장과 생존이 크게 떨어졌고 모래층 10 cm가 성장·장 건강·장내 미생물 안정성의 균형이 가장 좋았다[24].\n\n"
  "저온에 비교적 강한 것도 양식 대상종으로서의 장점으로 꼽히며, 10 °C 저온 스트레스와 28 °C 정상 수온의 눈자루 전사체를 비교해 저온 내성 관련 유전자를 찾은 연구가 있다[8, 14]. 질병으로는 흰반점증후군 바이러스가 대표적이며[26, 27], 일본 여러 지역의 병든 보리새우에서 분리한 세균 Photobacterium damselae subsp. damselae 균주들의 유전체도 분석되었다[29].\n\n"
  "중국 양식 집단에서는 유전 다양성 저하와 질병 저항성 감소가 지속 가능한 양식의 과제로 지적되어 핵심 종질 선발이 시도되었다[11]. 국내 어획·양식 생산량의 공식 통계는 이 조사에서 확인하지 못함."},
 {"key": "processing", "title": "가공·이용", "body":
  "보리새우는 익혔을 때 껍데기가 붉게 변하는 정도가 품질 지표로 쓰인다[21]. 평균 15.4 cm, 25.2 g의 산 보리새우를 100 °C에서 1분 익힐 때, 5 °C·20 °C에 24시간 보관한 개체는 갓 죽여 익힌 개체보다 붉은색 발현율이 유의하게 낮았다[21]. 60 °C에서는 색이 거의 나지 않았고, 80 °C로 익힐 때는 1% 탄산나트륨 처리가 부족한 발색을 보완했다[21].\n\n"
  "냉장 꼬리살의 저장 기간은 공기 포장 1주에서 진공 포장 21일, 200 MPa 고압 처리 28일, 400 MPa 처리 35일로 늘었으며, 진공 포장은 흑변을 늦췄지만 고압 처리는 흑변을 오히려 키웠다[22]. 얼음 보관 중에는 요소가 늘어 보리새우의 선도 지표로 요소가 제안되었다[23]. 40 G 교번 자기장을 건 냉동은 동결 시간과 해동·가열 손실을 줄였다[35].\n\n"
  "머리 부산물은 파파인으로 50 °C에서 4시간 분해하면 항균·ACE 저해 활성을 보였고, 정제한 펩타이드 ARL/I의 ACE 저해 IC50은 125.58 µM이었다[15]. 머리 지질은 글리세로인지질이 대부분(91.36%)이었다[16]. 식품원료 목록에 오른 '건보리새우분해농축액'의 제조 방법과 이 연구들의 관계는 확인하지 못함."},
 {"key": "genetics", "title": "유전 정보", "body":
  "2021년 일본 연구진은 일루미나와 나노포어 서열로 1.70 Gbp 초안 유전체(스캐폴드 N50 234.9 kbp, BUSCO 93.4%)와 15,969 bp의 미토콘드리아 유전체를 발표했고, 단백질 암호 유전자 모델은 26,381개, 단순 반복 서열은 27.4%였다[7]. 2022년 중국 연구진은 Hi-C로 약 1.54 Gb를 42개 유사 염색체에 올리고 유전자 24,317개, 반복 서열 61.56%를 보고했다[8]. 2025년 다른 조립에서는 1.64 Gb 중 97.83%를 43개 염색체에 고정했고 유전자 21,172개, BUSCO 91.0%였다[9]. 이처럼 조립마다 염색체 수(42·43)와 유전자 수가 다르게 보고되었다[8, 9].\n\n"
  "유전체 분석 기반 연관 지도는 길이 3,481.98 cM에 SNP 29,757개가 41개 연관군에 놓였으며, 제1연관군에서 성별과 연관된 SNP 5개를 담은 일배체형이 찾아졌다[12]. 중국과 일본 도입 계통 20개 집단을 재분석한 연구에서는 SNP 9,146,248개가 확인되었고, 푸젠과 일본 도입 집단이 인공 육종 배경을 공유해 가깝게 묶였다[11]. 숨은 종 Form II의 미토콘드리아 유전체는 15,966 bp였다[10]."},
 {"key": "safety", "title": "안전성", "body":
  "식약처 「식품원료 목록」에서 보리새우와 그 원료들은 별도 조건 없는 '사용가능' 수산물이며, 건강기능식품 고시형 원료가 아니어서 고시 섭취 시 주의사항은 없다[1]. 이 종을 따로 다룬 국내 공공기관의 알레르기·잔류물질·독성 안내는 이 조사에서 확인하지 못함.\n\n"
  "보리새우의 주요 알레르겐은 근육 단백질 트로포미오신(Pen j 1)이다[2]. 성숙 단백질은 284개 아미노산으로 이루어지고, 새우 알레르기 환자 혈청의 IgE 결합 부위는 서열 전체에 흩어져 있으며 특히 C-말단 쪽을 강하게 인식했다[2]. 정제한 약 35 kDa의 Pen j 1은 80 °C에서 구조가 풀렸다가 25 °C로 식으면 원래 구조로 돌아와 가열 뒤에도 항원성을 유지했다[3]. 보리새우 트로포미오신의 겉보기 녹는 온도는 47.3 °C로 오징어·전복보다 열에 안정했다[5].\n\n"
  "Pen j 1은 장 단백질 분해효소로 빠르게 분해되었지만, 쥐에게 먹이면 소장보다 위에 오래 남아 위 점막으로 흡수될 수 있다는 결과가 나왔다[4]. 다른 연구의 면역블롯에서는 보리새우에서도 IgE와 반응하는 20 kDa 근형질 칼슘결합단백질이 검출되었다[6]. 보리새우는 네오니코티노이드 살충제에 대한 내성이 모래새우보다 낮았고 탈피 중에 체내 농축이 커졌다[32]."},
]

compounds = [
 {"name": "Tropomyosin", "name_ko": "트로포미오신(Pen j 1)", "class": "근육 구조 단백질(알레르겐)", "role": "bioactive", "part": "꼬리(복부) 근육",
  "content_text": "정제 단백질 약 35 kDa; 성숙 단백질 284 잔기(리더 펩타이드 9 잔기 제거) [2, 3]",
  "activity_ko": "갑각류 알레르기의 주요 원인 단백질로, 가열 뒤 다시 접혀 항원성이 유지되고 녹는 온도 47.3 °C로 열에 안정했다[2, 3, 5]", "source": [2, 3, 5]},
 {"name": "Sarcoplasmic calcium-binding protein", "name_ko": "근형질 칼슘결합단백질", "class": "칼슘결합 단백질(알레르겐)", "role": "bioactive", "part": "근육",
  "content_text": "보리새우에서 IgE 반응성 20 kDa 띠로 검출(함량 값 없음) [6]",
  "activity_ko": "새우·가재류에 한정되어 나타나는 새로운 갑각류 알레르겐으로 보고되었다[6]", "source": [6]},
 {"name": "Astaxanthin", "name_ko": "아스타잔틴", "class": "케토카로티노이드", "role": "bioactive", "part": "표피(껍데기 아래)·근육·머리",
  "content_text": "표피의 청색 카로테노프로테인(분자량 약 280,000, 흡수 극대 640 nm)의 발색단, all-trans형이 주성분 [19]",
  "activity_ko": "가열하면 단백질에서 떨어져 붉은색(470 nm)을 띠며, 익힌 새우의 붉은 색 발현과 관련된다[19, 21]; 사료로 준 아스타잔틴 양에 따라 껍데기·근육·머리의 총 카로티노이드가 늘었다[20]", "source": [19, 20, 21]},
 {"name": "Penaeusxanthin", "name_ko": "페네우스잔틴", "class": "황색 잔토필", "role": "bioactive", "part": "껍데기·근육·머리",
  "content_text": "이 종에서 처음 분리한 새 카로티노이드(함량 값은 초록에 없음) [20]",
  "activity_ko": "아스타잔틴이 몸 안에서 대사되어 생기는 황색 잔토필로 해석되었다[20]", "source": [20]},
 {"name": "Eicosapentaenoic acid", "name_ko": "에이코사펜타엔산(EPA)", "class": "n-3 다가불포화지방산", "role": "nutrient", "part": "근육·간췌장",
  "content_text": "총지질의 주요 지방산(함량 값은 초록에 없음) [19]",
  "activity_ko": "근육 지질은 주로 인지질이며, EPA는 팔미트산·올레산·DHA와 함께 주요 지방산이었다[19]", "source": [19]},
 {"name": "Docosahexaenoic acid", "name_ko": "도코사헥사엔산(DHA)", "class": "n-3 다가불포화지방산", "role": "nutrient", "part": "근육·간췌장",
  "content_text": "총지질의 주요 지방산(함량 값은 초록에 없음) [19]",
  "activity_ko": "근육과 간췌장 총지질의 지방산 조성은 다른 해양 동물과 비슷했다[19]", "source": [19]},
 {"name": "Glycerophospholipids", "name_ko": "글리세로인지질", "class": "인지질", "role": "nutrient", "part": "머리",
  "content_text": "머리 지질의 91.36%(상대 피크 면적, UPLC-Orbitrap MS) [16]",
  "activity_ko": "머리 지질 추출물은 제브라피시 모델에서 혈관 생성 촉진·항염증·심장 보호 활성을 보였다(동물 모델 결과)[16]", "source": [16]},
 {"name": "D-Alanine", "name_ko": "D-알라닌", "class": "D-아미노산(유리)", "role": "bioactive", "part": "근육·심장·아가미 등",
  "content_text": "총 알라닌 중 D-알라닌 18.7–43.7%(조직별) [17]",
  "activity_ko": "탈피 뒤 근육의 알라닌 라세미화효소 활성이 두 배로 늘어 탈피 때 근육에서 역할이 있을 것으로 보였다[17]", "source": [17]},
 {"name": "Glutamine", "name_ko": "글루타민(유리)", "class": "유리아미노산", "role": "nutrient", "part": "복부 근육",
  "content_text": "염분 상승 시 농도가 크게 증가(구체 값은 초록에 없음) [18]",
  "activity_ko": "알라닌과 함께 삼투 조절에 쓰이며, 높은 염분에서 글루타민 합성 효소 유전자 발현 증가와 연관되었다[18]", "source": [18]},
 {"name": "Urea", "name_ko": "요소", "class": "질소 대사물", "role": "bioactive", "part": "근육",
  "content_text": "얼음 보관 15일 동안 보리새우 근육에서 상당히 증가(구체 값은 초록에 없음) [23]",
  "activity_ko": "보리새우의 선도 지표로 제안되었다[23]", "source": [23]},
 {"name": "Ala-Arg-Leu", "name_ko": "ACE 저해 펩타이드 ARL/I", "class": "트라이펩타이드", "role": "bioactive", "part": "머리(파파인 가수분해물)",
  "content_text": "ACE 저해 IC50 125.58 µM, 경쟁적 저해, Ki 36.19 ± 0.28 µg/mL [15]",
  "activity_ko": "시험관 ACE 저해 활성을 보였고 토끼 적혈구 용혈은 없었다(사람 연구 아님)[15]", "source": [15]},
 {"name": "Val-Thr-Val-Pro", "name_ko": "항균 펩타이드 VTVP", "class": "테트라펩타이드", "role": "bioactive", "part": "머리(파파인 가수분해물)",
  "content_text": "시험 균주에 대한 MIC 1.62–8.03 mM [15]",
  "activity_ko": "그람양성균에 상대적으로 강한 시험관 항균 활성을 보였다[15]", "source": [15]},
 {"name": "Ferritin", "name_ko": "페리틴(MjFer)", "class": "철 저장 단백질", "role": "bioactive", "part": "세포질형",
  "content_text": "결정 구조 해상도 1.16 Å, 24량체 [30]",
  "activity_ko": "척추동물 H·L 사슬의 특징을 함께 지닌 혼성형으로, 갑각류 페리틴의 첫 결정 구조다[30]", "source": [30]},
 {"name": "Arachidonic acid", "name_ko": "아라키돈산", "class": "n-6 다가불포화지방산", "role": "bioactive", "part": "난소",
  "content_text": "난소 발달 I·II기에 V기보다 유의하게 낮음(P<0.01) [33]",
  "activity_ko": "프로스타글란딘의 전구체로 난소 성숙과 관련된 것으로 해석되었다[33]", "source": [33]},
 {"name": "Prostaglandin F2alpha", "name_ko": "프로스타글란딘 F2α", "class": "에이코사노이드", "role": "bioactive", "part": "난소",
  "content_text": "난소 I기 약 20 pg/mg, IV·V기에 크게 감소 [33]",
  "activity_ko": "난소 발달 단계에 따라 변해 성숙 조절과 관련될 것으로 보였다[33]", "source": [33]},
]

E = {k: "" for k in ["instrument","column","mobile_phase","gradient","flow","temp","detection","injection","sample_prep","standard","linearity","lod","loq","recovery"]}
def cond(**kw):
    c = dict(E); c.update(kw); return c
assays = [
 {"role": "literature", "compound": "Ala-Arg-Leu/Ile (ACE inhibitory peptide)", "compound_ko": "ACE 저해 펩타이드 ARL/I", "part": "머리(파파인 단백질 가수분해물)",
  "content": "ARL/I IC50 125.58 µM; 2단계 정제 분획 IC50 0.045 ± 0.005 mg/mL; 가수분해물 IC50 1.90 ± 0.03 mg/mL, 5,000 Da 미만 펩타이드 68.89% [15]",
  "method": "2단계 RP-HPLC 분취 + UPLC-ESI-MS/MS 동정",
  "conditions": cond(
    instrument="분취: Shimadzu LC-20AD HPLC; 동정: Waters ACQUITY UPLC + TQ 검출기(ESI)",
    column="1단계 TSKgel ODS-80TM (250 × 4.6 mm, Tosoh); 2단계 Mightysil RP-18 (150 × 4.6 mm, 5 µm, Kanto Chemical); 동정 TSKgel Amide-80 (3 µm, 2.0 mm × 15 cm)",
    mobile_phase="분취: A 물(0.1% TFA), B 아세토니트릴(0.1% TFA); 동정: A Milli-Q 물, B 아세토니트릴",
    gradient="분취: B 선형 기울기(구간 값은 원문에 없음, A로 10분 평형); 동정: 90% B 5분 유지 후 20분에 걸쳐 50% B로 선형 감소",
    flow="1.0 mL/min(1단계), 0.5 mL/min(2단계), 0.2 mL/min(UPLC)",
    detection="UV 220 nm; ESI 양이온 full scan m/z 100–2000 후 MS/MS로 서열 동정",
    injection="20 µL(1단계 HPLC), 10 µL(UPLC, 0.5 mg/mL)",
    sample_prep="머리를 4 °C에서 분쇄해 물과 1:2(W:V)로 균질화, 파파인 10,000 U/g·pH 7.0·50 °C·4시간 분해, 95 °C 10분 불활성화, 12,000×g 20분(4 °C) 원심분리 후 상층액 동결건조",
    standard="ACE 저해 활성은 HHL 기질·228 nm 흡광으로 측정"),
  "rationale": "이 종 머리 부산물 가수분해물에서 활성을 대표하는 펩타이드로 정제·동정되었다. 함량이 아니라 활성(IC50) 값만 보고되었고, 검출·정량한계와 회수율은 원문에 없다[15].",
  "source": [15], "url": "https://doi.org/10.3390/molecules28020894", "source_kind": "paper"},
 {"role": "literature", "compound": "Glycerophospholipids", "compound_ko": "글리세로인지질", "part": "머리",
  "content": "머리 지질 중 글리세로인지질 91.36%, 스핑고지질 7.73%(총 피크 면적 대비 상대값) [16]",
  "method": "UPLC-Q-Exactive Orbitrap MS 지질체 분석",
  "conditions": cond(
    instrument="Thermo Vanquish UPLC + Q Exactive Orbitrap MS",
    column="Thermo Accucore C30",
    mobile_phase="A: 아세토니트릴/물(6/4) + 10 mM 아세트산암모늄 + 0.1% 포름산; B: 아세토니트릴/이소프로판올(1/9) + 10 mM 아세트산암모늄 + 0.1% 포름산",
    gradient="30% B(0분) → 43% B(8분) → 50% B(8.1분) → 70% B(17분) → 99% B(24분) → 30% B(27.1분) → 30% B(31분), 이후 30% B로 5분 재평형",
    flow="0.35 mL/min", temp="40 °C",
    detection="ESI 양·음이온, 분무 전압 3 kV, 모세관 350 °C, full scan 분해능 120,000(m/z 114–1700), Top20 MS/MS 분해능 30,000, NCE 25·30(음이온 20·24·28)",
    sample_prep="머리 균질화 후 Bligh–Dyer법으로 총지질 추출; 지질 100 mg에 메탄올 0.75 mL·MTBE 2.5 mL 가해 1시간 진탕, 물 0.625 mL로 상분리, 유기층 건조 후 이소프로판올/메탄올/물(60:30:4.5) 100 µL에 재용해",
    standard="외부 표준물질 없이 총 지질 피크 면적 대비 상대 정량(Lipidmaps·Lipidblast 대조)"),
  "rationale": "머리 지질의 대부분을 차지하는 성분군이다. 원문은 종을 약어 PJ로 표기하며 이 도구의 본문에서는 학명 기울임 글자가 빠져 PJ가 Penaeus japonicus임을 문맥(중국 산둥 시장의 해산 새우 4종 중 하나)으로만 판단했다. 검출·정량한계와 회수율은 원문에 없다[16].",
  "source": [16], "url": "https://doi.org/10.3390/molecules27020350", "source_kind": "paper"},
 {"role": "literature", "compound": "D-Alanine", "compound_ko": "D-알라닌", "part": "근육·심장·아가미 등 여러 조직",
  "content": "총 알라닌 중 D-알라닌 18.7–43.7%(조직별) [17]",
  "method": "HPLC(D/L-아미노산 분리)",
  "conditions": cond(),
  "rationale": "갑각류 조직의 주요 삼투조절 물질로, 이 종 여러 조직에서 D형 비율을 정량했다. 전문 확인 못함(초록만 확인)이라 분석 조건 칸은 비워 두었다[17].",
  "source": [17], "url": "https://doi.org/10.1016/j.jchromb.2011.04.026", "source_kind": "paper"},
]

d = {
 "slug": "penaeus-japonicus", "name_ko": "보리새우", "name_en": "Kuruma prawn",
 "scientific_name": "Penaeus japonicus",
 "aliases": ["Kuruma prawn", "Kuruma shrimp", "Marsupenaeus japonicus", "건보리새우", "건보리새우분해농축액"],
 "sections": sections, "compounds": compounds, "markers": [], "assays": assays,
 "nutrients": [], "production": [], "world": [], "gi": [], "orgs": [], "sources": sources,
}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
for s in sections: print(s["key"], len(s["body"]))
