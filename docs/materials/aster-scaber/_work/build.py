import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
A = "2026-11-02"
def pm(pmid, pmc=None):
    return f"https://pmc.ncbi.nlm.nih.gov/articles/{pmc}/" if pmc else f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
S = [
 (1, "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 참취잎·건조참취·절임참취(Aster scaber Thunberg, 식품원료 A코드, 사용가능, '사용가능부위 : 잎') 행과 같은 속·다른 '취' 원료 행(로컬 원자료 I1020_20261013)", "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "식품의약품안전처", "2026-10-13"),
 (2, "The complete chloroplast genome of Aster scaber Thunb. 1784 (Asteraceae). Mitochondrial DNA B Resour 2024;10(1):57-62 (PMID 39776575, doi:10.1080/23802359.2024.2447744)", pm(0,"PMC11703284"), "Mitochondrial DNA Part B (PMC 전문)", A),
 (3, "World Flora Online 분류 스냅숏(2023년 12월) — Aster scaber Thunb.(Fl. Jap. 316, 1784) 정명, Doellingeria scabra (Thunb.) Nees(Gen. Sp. Aster. 183, 1832) 이명 처리. ※ 원문 페이지는 이 작업 환경에서 열지 못했고 WebSearch 검색 요약으로만 확인함", "https://list.worldfloraonline.org/wfo-0000095645", "World Flora Online(WebSearch 요약으로만 확인)", A),
 (4, "Radical Scavenging-Linked Anti-Adipogenic Activity of Aster scaber Ethanolic Extract and Its Bioactive Compound. Antioxidants 2020;9(12):1290 (PMID 33339396, doi:10.3390/antiox9121290)", pm(0,"PMC7766398"), "Antioxidants (MDPI, PMC 전문)", A),
 (5, "Astragalin and Isoquercitrin Isolated from Aster scaber Suppress LPS-Induced Neuroinflammatory Responses in Microglia and Mice. Foods 2022;11(10):1505 (PMID 35627075, doi:10.3390/foods11101505)", pm(0,"PMC9141956"), "Foods (MDPI, PMC 전문)", A),
 (6, "The Effect of Pectinase-Assisted Extraction on the Physicochemical and Biological Properties of Polysaccharides from Aster scaber. Int J Mol Sci 2018;19(9):2839 (PMID 30235870, doi:10.3390/ijms19092839)", pm(0,"PMC6164288"), "International Journal of Molecular Sciences (PMC 전문)", A),
 (7, "Insecticides chlorantraniliprole and flubendiamide in Aster scaber: Dissipation kinetics, processing effects, and risk assessment. Heliyon 2024;10(12):e33216 (PMID 39022020, doi:10.1016/j.heliyon.2024.e33216)", pm(0,"PMC11252733"), "Heliyon (PMC 전문)", A),
 (8, "Dissipation Kinetics and Risk Assessment of Spirodiclofen and Tebufenpyrad in Aster scaber Thunb. Foods 2023;12(2):242 (PMID 36673334, doi:10.3390/foods12020242)", pm(0,"PMC9858338"), "Foods (MDPI, 초록 확인)", A),
 (9, "A new caffeoyl quinic acid from Aster scaber and its inhibitory activity against human immunodeficiency virus-1 (HIV-1) integrase. Chem Pharm Bull 2000;48(11):1796-8 (PMID 11086919, doi:10.1248/cpb.48.1796)", pm(11086919), "Chemical & Pharmaceutical Bulletin (PubMed 초록)", A),
 (10, "Neuroprotective and neurotrophic effects of quinic acids from Aster scaber in PC12 cells. Biol Pharm Bull 2001;24(8):921-4 (PMID 11510486, doi:10.1248/bpb.24.921)", pm(11510486), "Biological & Pharmaceutical Bulletin (PubMed 초록)", A),
 (11, "(-)-3,5-Dicaffeoyl-muco-quinic acid isolated from Aster scaber contributes to the differentiation of PC12 cells: through tyrosine kinase cascade signaling. Biochem Biophys Res Commun 2004;313(4):948-53 (PMID 14706634, doi:10.1016/j.bbrc.2003.11.178)", pm(14706634), "BBRC (PubMed 초록)", A),
 (12, "Protective effects of quinic acid derivatives on tetrahydropapaveroline-induced cell death in C6 glioma cells. Biol Pharm Bull 2003;26(6):803-7 (PMID 12808290, doi:10.1248/bpb.26.803)", pm(12808290), "Biological & Pharmaceutical Bulletin (PubMed 초록)", A),
 (13, "Two new monoterpene peroxide glycosides from Aster scaber. Chem Pharm Bull 2001;49(7):912-4 (PMID 11456102, doi:10.1248/cpb.49.912)", pm(11456102), "Chemical & Pharmaceutical Bulletin (PubMed 초록)", A),
 (14, "Cytoprotective and anti-inflammatory effects of spinasterol via the induction of heme oxygenase-1 in murine hippocampal and microglial cell lines. Int Immunopharmacol 2010;10(12):1587-94 (PMID 20933625, doi:10.1016/j.intimp.2010.09.013)", pm(20933625), "International Immunopharmacology (PubMed 초록)", A),
 (15, "Qualitative and quantitative determination of the caffeoylquinic acids on the Korean mountainous vegetables used for chwinamul and their peroxynitrite-scavenging effect. Arch Pharm Res 2009;32(10):1361-7 (PMID 19898797, doi:10.1007/s12272-009-2003-6)", pm(19898797), "Archives of Pharmacal Research (PubMed 초록)", A),
 (16, "Polyphenol composition and antioxidant capacity from different extracts of Aster scaber. Acta Biol Hung 2014;65(2):144-55 (PMID 24873908, doi:10.1556/ABiol.65.2014.2.3)", pm(24873908), "Acta Biologica Hungarica (PubMed 초록)", A),
 (17, "Studies on the constituents of Aster scaber Thunb. IV. Structures of four new echinocystic acid glycosides isolated from the herb. Chem Pharm Bull 1993;41(4):659-65 (PMID 8508469, doi:10.1248/cpb.41.659)", pm(8508469), "Chemical & Pharmaceutical Bulletin (PubMed 초록)", A),
 (18, "Studies on the constituents of Aster scaber Thunb. V. Structures of six new echinocystic acid glycosides isolated from the herb. Chem Pharm Bull 1993;41(9):1562-6 (PMID 8221969, doi:10.1248/cpb.41.1562)", pm(8221969), "Chemical & Pharmaceutical Bulletin (PubMed 초록)", A),
 (19, "Studies on the constituents of Aster scaber Thunb. III. Structures of scaberosides B7, B8 and B9, minor oleanolic acid glycosides isolated from the root. Chem Pharm Bull 1992;40(4):886-8 (PMID 1525944, doi:10.1248/cpb.40.886)", pm(1525944), "Chemical & Pharmaceutical Bulletin (PubMed 초록)", A),
 (20, "Cerebrosides and terpene glycosides from the root of Aster scaber. Arch Pharm Res 2003;26(2):132-7 (PMID 12643589, doi:10.1007/BF02976658)", pm(12643589), "Archives of Pharmacal Research (PubMed 초록)", A),
 (21, "Effects of Aster scaber Seed Oil Containing trans-Δ3 Fatty Acids on Lipid Profiles of Hamsters and Rats. J Oleo Sci 2015;64(12):1321-7 (PMID 26582157, doi:10.5650/jos.ess15196)", pm(26582157), "Journal of Oleo Science (PubMed 초록)", A),
 (22, "Neuroprotective effects of phytosterols and flavonoids from Cirsium setidens and Aster scaber in human brain neuroblastoma SK-N-SH cells. Life Sci 2016;148:173-82 (PMID 26874034, doi:10.1016/j.lfs.2016.02.035)", pm(26874034), "Life Sciences (PubMed 초록)", A),
 (23, "Antioxidant activity and anti-adipogenic effects of wild herbs mainly cultivated in Korea. Molecules 2013;18(10):12937-50 (PMID 24141244, doi:10.3390/molecules181012937)", pm(0,"PMC6270600"), "Molecules (MDPI, 초록 확인)", A),
 (24, "Antioxidant activity and cytotoxicity of methanol extracts from aerial parts of Korean salad plants. BioFactors 2007;30(2):79-89 (PMID 18356580, doi:10.1002/biof.5520300202)", pm(18356580), "BioFactors (PubMed 초록)", A),
 (25, "Neuroprotective effect of rough aster butanol fraction against oxidative stress in the brain of mice challenged with kainic acid. J Agric Food Chem 2003;51(16):4570-5 (PMID 14705879, doi:10.1021/jf034251d)", pm(14705879), "Journal of Agricultural and Food Chemistry (PubMed 초록)", A),
 (26, "Paeonia japonica, Houttuynia cordata, and Aster scaber water extracts induce nitric oxide and cytokine production by lipopolysaccharide-activated macrophages. J Med Food 2009;12(2):365-73 (PMID 19459739, doi:10.1089/jmf.2008.1013)", pm(19459739), "Journal of Medicinal Food (PubMed 초록)", A),
 (27, "In vitro plant regeneration of Aster scaber via somatic embryogenesis. Biosci Biotechnol Biochem 2015;79(5):725-31 (PMID 25640866, doi:10.1080/09168451.2014.996202)", pm(25640866), "Bioscience, Biotechnology, and Biochemistry (PubMed 초록)", A),
 (28, "Dasineura asteriae Reprograms the Flower Gene Expressions of Vegetative Organs to Create Flower-Like Gall in Aster scaber. Plant Cell Environ 2025;48(11):8217-8231 (PMID 40810459, doi:10.1111/pce.70127)", pm(0,"PMC12502024"), "Plant, Cell & Environment (초록 확인)", A),
 (29, "Pesticide residue monitoring in Korean agricultural products, 2003-05. Food Addit Contam Part B 2009;2(1):27-37 (PMID 24784964, doi:10.1080/02652030902783350)", pm(24784964), "Food Additives & Contaminants Part B (PubMed 초록)", A),
 (30, "Pesticide residues in leafy vegetables, stalk and stem vegetables from South Korea: a long-term study on safety and health risk assessment. Food Addit Contam Part A 2016;33(1):105-18 (PMID 26571090, doi:10.1080/19440049.2015.1108524)", pm(26571090), "Food Additives & Contaminants Part A (PubMed 초록)", A),
 (31, "Health risk associated with pesticide residues in vegetables from Incheon region of Korea. Environ Sci Pollut Res Int 2022;29(43):65860-65872 (PMID 35488156, doi:10.1007/s11356-022-20481-x)", pm(35488156), "Environmental Science and Pollution Research (PubMed 초록)", A),
 (32, "Comparison of analytical methods and residue patterns of pymetrozine in Aster scaber. Bull Environ Contam Toxicol 2011;87(6):649-52 (PMID 21922281, doi:10.1007/s00128-011-0407-8)", pm(21922281), "Bulletin of Environmental Contamination and Toxicology (PubMed 초록)", A),
 (33, "1,5-dicaffeoylquinic acid protects primary neurons from amyloid β 1-42-induced apoptosis via PI3K/Akt signaling pathway. Chin Med J 2011;124(17):2628-35 (PMID 22040415)", pm(22040415), "Chinese Medical Journal (PubMed 초록)", A),
 (34, "Chemistry and pharmacological action of caffeoylquinic acid derivatives and pharmaceutical utilization of chwinamul (Korean Mountainous vegetable). Arch Pharm Res 2010;33(11):1703-20 (PMID 21116772, doi:10.1007/s12272-010-1101-9)", pm(21116772), "Archives of Pharmacal Research (PubMed 초록, 총설)", A),
 (35, "Oh SH 외. Neuroprotective effects of butterbur and rough aster against kainic acid-induced oxidative stress in mice. J Med Food 2005;8(2):169-76 (PMID 16117608, doi:10.1089/jmf.2005.8.169)".replace("Oh SH 외. ", ""), pm(16117608), "Journal of Medicinal Food (PubMed 초록)", A),
]
sources = [dict(n=n, title=t, url=u, publisher=p, accessed=a) for n,t,u,p,a in S]

sec = {}
sec["overview"] = ("한눈에 보기",
"참취(Aster scaber Thunb.)는 국화과(Asteraceae)의 여러해살이풀로, 중국·한국·일본과 러시아 동시베리아에 분포하며 골짜기·비탈·풀밭·덤불에서 자란다[2]. 한국에서는 산에서 자라기도 하고 재배도 하는 산나물로, 잎을 '취나물'로 흔히 먹는다[4][5].\n\n"
"식품의약품안전처 「식품원료 목록」에는 참취잎·건조참취·절임참취 세 행이 식품원료(A코드)로 올라 있고, 세 행 모두 사용 여부는 '사용가능', 사용 조건은 '사용가능부위 : 잎'이다[1]. 같은 목록에는 이명으로 취·취나물·동풍채, 영문명으로 Edible aster가 적혀 있다[1]. 이 목록에서 참취를 원재료로 한 건강기능식품 고시형·개별인정형 원료 행은 찾지 못했다[1]. 따라서 국내에서 식품으로 쓸 수 있는 부위는 잎이며, 연구에 쓰인 뿌리·씨앗은 사용 부위가 아니다[1][19][21].\n\n"
"잎과 지상부에는 클로로젠산과 여러 디카페오일퀸산 같은 카페오일퀸산류, 아스트라갈린·이소퀘르시트린 같은 플라보노이드가 들어 있다[4][5][9]. 학명은 Aster scaber가 널리 쓰이지만, Doellingeria scabra라는 이름으로 다루는 분류도 있다[3]. 효능 연구는 대부분 세포·동물 실험이고, 사람 대상 임상시험은 확인하지 못함.")
sec["history"] = ("이용의 역사",
"참취는 한국과 중국의 전통의학에서 타박상·뱀에 물린 상처·두통·어지럼에 쓰였다고 소개된다[10][11]. '취나물'은 국화과 여러 종을 함께 부르는 이름이며, 한국에서 반찬이나 약초로 써 왔고 고콜레스테롤혈증·당뇨·감기 등에 쓰였다고 정리되어 있다[34]. 취나물 분석 연구에는 참취와 함께 쑥부쟁이류(Kalimeris yomena)·미역취류(Solidago)·서덜취(Saussurea grandifolia)·단풍취(Ainsliaea acerifolia)가 시료로 들어갔다[15]. 국내 식품원료 목록에서도 '취'라는 이름은 곰취(Ligularia fischeri)·수리취(Synurus deltoides)·단풍취 같은 다른 속 식물에 붙어 있어, 이름만으로는 종을 알 수 없다[1].\n\n"
"성분 연구는 1990년대 초 일본 연구진이 뿌리와 지상부의 트리테르펜 사포닌(스카베로사이드) 구조를 밝히면서 시작되었다[17][18][19]. 2000년대에는 한국 연구진이 지상부에서 카페오일퀸산류와 모노테르펜 과산화물 배당체를 새로 분리했다[9][13]. 2000년대 이후에는 항산화·신경 보호·면역·비만과 관련한 세포·동물 연구가 이어졌다[4][5][6][24][25][26][35]. 참취를 먹어 온 역사를 다룬 공공기관 문헌은 확인하지 못함.")
sec["biology"] = ("식물학적 특징",
"참취는 수염뿌리를 내는 여러해살이풀로, 뿌리줄기는 짧고 굵으며 줄기는 곧게 서고 털이 없다[2]. 잎은 위로 갈수록 작아지고, 잎몸은 달걀꼴에 밑이 심장 모양이며 가장자리에 톱니가 있다[2]. 위쪽 잎은 피침형이고 잎자루가 없다[2]. 머리모양꽃차례가 고른꽃차례(산방상)로 모여 달리고, 꽃차례마다 흰 혀꽃이 4–9개 있으며 총포는 종 모양이다[2]. 열매(수과)는 거꿀달걀꼴로 털이 없고 능선이 있으며, 흰빛이 도는 갓털이 붙는다[2]. 이 형태 기재는 중국 랴오닝성 다롄에서 채집한 표본을 바탕으로 한 것이다[2].\n\n"
"말린 참취는 탄수화물이 건조 중량의 약 70%를 차지한다고 인용되어 있다[6]. 온실에서 기른 잎의 수분은 시험 포장에 따라 약 82%와 약 92%였다[7]. 혹파리의 일종(Dasineura asteriae) 애벌레는 참취의 영양기관에 꽃처럼 생긴 장미꽃 모양 벌레혹을 만든다[28]. 씨앗 기름에는 Δ3-트랜스 지방산이 상당량 들어 있다[21]. 한국 샐러드용 식물 11종을 비교한 연구에서 참취 지상부 메탄올 추출물의 총페놀은 생중량 100 g당 17.1 mg으로 가장 높았다[24].")
sec["related_species"] = ("근연종과 혼동 주의",
"국내 식품원료 목록에는 참취 외에도 같은 Aster 속의 벌개미취(A. koraiensis, 잎)·까실쑥부쟁이(A. ageratoides, 잎)·개미취(A. tataricus, 순)·쑥부쟁이(A. yomena, 잎)·옹굿나물(A. fastigiatus, 순)·섬쑥부쟁이(A. glehni, 순)가 사용 부위를 달리해 각각 따로 올라 있으므로 참취 자료와 섞으면 안 된다[1]. 같은 목록의 개별인정형 원료인 쑥부쟁이추출분말·해국추출물도 참취와는 다른 종의 원료다[1].\n\n"
"'취'가 붙은 다른 산나물인 곰취(Ligularia fischeri)·수리취(Synurus deltoides)·단풍취(Ainsliaea acerifolia)·미역취(Solidago virgaurea)는 아예 다른 속이다[1]. 다섯 가지 산나물을 비교한 연구에서 총플라보노이드는 참취(103.9 mg RE/g), 총페놀은 곰취(215.8 mg GAE/g)가 가장 많아 종마다 성분 특성이 달랐다[23].\n\n"
"학명은 국내 목록이 Aster scaber Thunberg를 쓴다[1]. 2023년 World Flora Online 분류는 Aster scaber Thunb.(1784)를 정명으로, Doellingeria scabra (Thunb.) Nees(1832)를 이명으로 두었으나, 이는 검색 요약으로만 확인한 것이다[3]. Aster 속을 좁게 보는 분류에서는 참취를 Doellingeria 속으로 옮겨 다룬다[3]. 엽록체 유전체 계통수에서 참취는 다른 Aster 종들과 한 무리로 묶였다[2]. Kew POWO 원문의 현재 처리는 확인하지 못함.")
sec["cultivation"] = ("재배와 생산",
"참취는 한국에서 온실 재배도 하는 잎채소이며, 한 번 심어 여러 차례 나누어 수확한다[7]. 충남 부여·태안 온실 시험에서는 파종 5–8개월 뒤인 2–3월에 시험했고, 시험 기간 온실 평균기온은 10.5 °C와 11.5 °C였다[7]. 충남 태안과 전남 광양 온실에서도 농약 잔류 시험이 이루어졌다[8]. 국내에는 참취에 쓰도록 등록된 농약이 61종, 376개 제품이라고 보고되었다[7]. 연구용 시료는 강원 양양(시장 구입, 6월 채취)과 전남 고흥 재배품 등에서 얻었다[4][5][6].\n\n"
"조직배양으로는 잎·잎자루·뿌리 절편을 써서 체세포배 발생을 거쳐 식물체를 재생하는 방법이 확립되었다[27]. 배발생 캘러스에는 NAA 5.0 μM과 BA 0.05 μM이 알맞았고, 새싹 재생에는 NAA 25 μM과 BA 25 μM처럼 높은 농도가 적합했다[27]. 뿌리내림은 생장조절물질이 없는 배지가 더 나았다[27].\n\n"
"참취의 국내 재배 면적·생산량 공식 통계는 확인하지 못함. 산림청 임산물 생산 통계의 '취나물' 품목은 여러 종을 함께 집계할 수 있어 참취만의 값으로 보기 어렵다는 점도 원문으로 확인하지 못함.")
sec["processing"] = ("가공과 이용",
"식품원료 목록에는 생잎(참취잎) 외에 건조참취와 절임참취가 따로 올라 있어, 말리거나 절여 유통하는 형태가 원료로 인정된다[1]. 온실 참취를 80 °C에서 24시간 말리자 수분이 빠지면서 잔류 농약 농도는 2–6배 높아졌고(가공계수 2.0–5.7), 수분 손실을 보정하면 열분해·증발로 약 46–52%가 줄었다[7]. 집에서 씻는 방법을 비교했을 때 클로란트라닐리프롤 제거율은 흐르는 물 63.7%, 받아 둔 물 75.5%, 중성세제 86.5%였다[7]. 플루벤디아마이드는 같은 방법에서 29.5–66.2%가 제거되었다[7].\n\n"
"연구용 추출에서는 동결건조한 참취 분말을 70% 에탄올로 80 °C에서 3시간 추출했고, 이 추출물의 클로로젠산은 10.98 mg/g이었다[4]. 펙틴 분해효소로 다당류를 추출하면 수율이 3.8%로 뜨거운 물 추출(3.3%)보다 높았다[6]. 참취를 원료로 한 건강기능식품 생산실적은 확인하지 못함.")
sec["genetics"] = ("유전체와 육종",
"참취의 엽록체 유전체는 전체 길이 152,778 bp이며, 큰 단일복제 구역 84,517 bp, 작은 단일복제 구역 18,277 bp, 역위반복 구역 두 곳(각 24,992 bp)으로 이루어진다[2]. GC 함량은 37.31%이고, 단백질 암호 유전자 88개, rRNA 유전자 8개, tRNA 유전자 37개 등 모두 133개 유전자가 주석되었다[2]. 시료는 중국 다롄의 생잎으로, Illumina 플랫폼으로 읽어 조립했고 평균 읽기 깊이는 1336.03×였다[2]. 최대우도 계통수에서 참취는 다른 Aster 종과 가까운 무리를 이루었다[2].\n\n"
"벌레혹 연구에서는 유전체 해독과 전사체 분석으로, 혹파리 애벌레가 참취의 꽃 발생 유전자를 켜고 심피 발생 유전자는 억제해 꽃처럼 생긴 혹을 만든다고 보고했다[28]. 체세포배 발생을 통한 재생 체계는 형질전환이나 대량 증식의 기초 기술로 쓰일 수 있다[27]. 참취의 핵 유전체 참조 서열이나 등록 품종 정보는 확인하지 못함.")
sec["safety"] = ("안전성",
"참취는 건강기능식품 고시형 원료가 아니어서 고시된 섭취 시 주의사항은 없다[1]. 식약처·농촌진흥청 등 공공기관의 참취 알레르기 안내는 확인하지 못함.\n\n"
"가장 많이 보고된 안전 문제는 잔류 농약이다[29][30][31]. 2003–05년 국내 농산물 잔류 농약 감시에서 참취의 기준 초과율은 8.2%로 파슬리·머위 다음으로 높았다[29]. 2010–14년 광주·전남 잎채소 조사와 2019년 인천 채소 조사에서도 참취는 잔류허용기준을 넘은 품목에 들었지만, 두 조사 모두 조사한 채소 전체의 추정 섭취량은 일일섭취허용량의 100% 미만으로 평가되었다[30][31]. 국내 참취의 잔류허용기준은 클로란트라닐리프롤 7 mg/kg, 플루벤디아마이드 20 mg/kg이며, 안전사용기준(수확 7일 전)을 지키면 두 성분 모두 기준 아래였다[7]. 스피로디클로펜은 살포 당일(0일)을 빼면 위해지수가 100% 미만이었다[8]. 피메트로진의 생물학적 반감기는 권장량 4.2일, 배량 3.5일이었다[32]. 먹기 전에 물이나 중성세제로 씻으면 잔류 농약을 상당 부분 줄일 수 있다[7].\n\n"
"생쥐에 참취 부탄올 분획 0.4–1.0 g/kg을 4일 먹였을 때 체중·뇌 무게에 의미 있는 변화는 없었다[25]. 씨앗 기름을 4주 먹인 쥐에서도 뚜렷한 생물학적 손상은 없었으나, 씨앗은 식품 사용 부위가 아니다[1][21]. 사람 대상 안전성 자료는 확인하지 못함.")

sections = [dict(key=k, title=v[0], body=v[1]) for k, v in sec.items()]

compounds = [
 dict(name="Chlorogenic acid", name_ko="클로로젠산(5-O-카페오일퀸산)", class_="페놀산(카페오일퀸산)", role="marker", part="지상부(잎 포함) 70% 에탄올 추출물",
      content_text="추출물 10.98 ± 0.04 mg/g(HPLC-PDA)[4]; 선행 연구 인용값 9.34 ± 0.11 mg/g 건조중량[4][15]", activity_ko="3T3-L1 지방세포에서 활성산소·지방 축적 억제(세포)[4]", source=[4, 15]),
 dict(name="3,5-Dicaffeoylquinic acid", name_ko="3,5-디카페오일퀸산", class_="페놀산(디카페오일퀸산)", role="bioactive", part="지상부",
      content_text="지상부에서 분리(함량 미보고)[9]", activity_ko="PC12 세포에서 아밀로이드 β 독성 완화·신경돌기 생성(세포)[10]", source=[9, 10]),
 dict(name="4,5-Dicaffeoylquinic acid", name_ko="4,5-디카페오일퀸산", class_="페놀산(디카페오일퀸산)", role="bioactive", part="지상부",
      content_text="지상부에서 분리(함량 미보고)[9]", activity_ko="네 가지 퀸산 유도체 가운데 아밀로이드 β·테트라하이드로파파베롤린 세포독성 보호 효과가 가장 큼(세포)[10][12]", source=[9, 10, 12]),
 dict(name="3,5-Dicaffeoyl-muco-quinic acid", name_ko="(-)-3,5-디카페오일-무코-퀸산", class_="페놀산(디카페오일퀸산 이성질체)", role="bioactive", part="지상부",
      content_text="참취에서 처음 보고된 새 화합물(함량 미보고)[9]", activity_ko="HIV-1 통합효소 억제 IC50 7.0 ± 1.3 μg/mL(시험관)[9]; PC12 세포 신경돌기 생성 촉진(세포)[11]", source=[9, 11]),
 dict(name="1,5-Dicaffeoylquinic acid", name_ko="1,5-디카페오일퀸산", class_="페놀산(디카페오일퀸산)", role="bioactive", part="확인하지 못함",
      content_text="참취에서 분리된 성분으로 소개(함량 미보고)[33]", activity_ko="쥐 대뇌피질 신경세포에서 아밀로이드 β42 유도 세포사멸 억제(세포)[33]", source=[33]),
 dict(name="Astragalin", name_ko="아스트라갈린(캠페롤-3-O-글루코사이드)", class_="플라보노이드(플라보놀 배당체)", role="bioactive", part="70% 에탄올 추출물의 에틸아세테이트 분획",
      content_text="분리(함량 미보고)[5][22]", activity_ko="LPS 자극 미세아교세포·생쥐 해마의 염증성 사이토카인 감소(세포·동물, 복강 주사)[5]; SK-N-SH 세포 산화 손상 보호(세포)[22]", source=[5, 22]),
 dict(name="Isoquercitrin", name_ko="이소퀘르시트린(퀘르세틴-3-O-글루코사이드)", class_="플라보노이드(플라보놀 배당체)", role="bioactive", part="70% 에탄올 추출물의 에틸아세테이트 분획",
      content_text="분리(함량 미보고)[5][22]", activity_ko="5 μg/mL에서 DPPH 라디칼 소거 83.5%(시험관); LPS 유도 신경염증 지표 감소(세포·동물)[5]", source=[5, 22]),
 dict(name="Myricetin", name_ko="미리세틴", class_="플라보노이드(플라보놀)", role="bioactive", part="잎",
      content_text="잎 추출물 4850.45 μg/g(UHPLC, 플라보놀 가운데 최다)[16]", activity_ko="확인하지 못함", source=[16]),
 dict(name="Caffeic acid", name_ko="카페산", class_="페놀산(하이드록시신남산)", role="bioactive", part="잎",
      content_text="잎 추출물 104.20 μg/g(UHPLC, 페놀산 가운데 최다)[16]", activity_ko="확인하지 못함", source=[16]),
 dict(name="alpha-Spinasterol", name_ko="α-스피나스테롤", class_="피토스테롤", role="bioactive", part="지상부",
      content_text="지상부에서 분리(함량 미보고)[13][14]", activity_ko="HT22·BV2 세포에서 HO-1 유도로 산화 손상·염증 매개물질 억제(세포)[14]", source=[13, 14]),
 dict(name="(3S)-3-O-(3',4'-Diangeloyl-beta-D-glucopyranosyloxy)-7-hydroperoxy-3,7-dimethylocta-1,5-diene", name_ko="모노테르펜 과산화물 배당체(새 화합물 2종 중 하나)", class_="모노테르펜 배당체", role="bioactive", part="지상부",
      content_text="지상부에서 새로 분리(함량 미보고)[13]", activity_ko="확인하지 못함", source=[13]),
 dict(name="Echinocystic acid", name_ko="에키노시스트산 배당체(스카베로사이드 Ha–Hi)", class_="트리테르펜 사포닌", role="bioactive", part="지상부(herb)",
      content_text="3,28-O-비스데스모사이드 10종을 메틸에스터로 분리(함량 미보고)[17][18]", activity_ko="확인하지 못함", source=[17, 18]),
 dict(name="Oleanolic acid", name_ko="올레아놀산 배당체(스카베로사이드 B7–B9)", class_="트리테르펜 사포닌", role="bioactive", part="뿌리(식품 사용 부위 아님)",
      content_text="뿌리에서 미량 사포닌으로 분리(함량 미보고)[19]; 뿌리에서 올레아놀산 글루쿠로나이드 메틸에스터·세레브로사이드 3종도 분리[20]", activity_ko="확인하지 못함", source=[19, 20]),
 dict(name="Galacturonic acid", name_ko="펙틴성 산성 다당류(갈락투론산 주성분)", class_="다당류", role="bioactive", part="말린 참취(부위 표기 없음)",
      content_text="펙틴 분해효소 추출 수율 3.8%; 람노스·아라비노스·갈락토스·글루코스·갈락투론산이 주 단당류[6]", activity_ko="RAW264.7 대식세포 활성화, 생쥐 100–200 mg/kg 경구 투여 시 면역 지표 개선(세포·동물)[6]", source=[6]),
 dict(name="trans-3-Hexadecenoic acid", name_ko="Δ3-트랜스 헥사데센산(16:1 Δ3t)", class_="지방산", role="nutrient", part="씨앗 기름(식품 사용 부위 아님)",
      content_text="씨앗 기름 지방산의 11.4%; Δ3t,9c-18:2 4.6%, Δ3t,9c,12c-18:3 11.3%[21]", activity_ko="햄스터에서 콩기름보다 혈청 LDL/HDL 비율을 더 개선(동물)[21]", source=[21]),
]
for c in compounds:
    c["class"] = c.pop("class_")
compounds = [{k: c[k] for k in ("name","name_ko","class","role","part","content_text","activity_ko","source")} for c in compounds]

assays = [
 {"role": "literature", "compound": "Chlorogenic acid", "compound_ko": "클로로젠산", "part": "참취(2019년 양양 시장 구입) 동결건조 분말의 70% 에탄올 추출물",
  "content": "추출물 중 10.98 ± 0.04 mg/g[4]",
  "method": "HPLC-PDA(확인은 HPLC-Q/TOF-MS)",
  "conditions": {"instrument": "Waters 2695 Separation Module + 996 PDA 검출기(확인 분석: Agilent 1260 Infinity HPLC + 6550 Q-TOF)",
                 "column": "Capcell Pak C18 MG(4.6 × 250 mm, 5.0 μm)",
                 "mobile_phase": "0.05% 포름산 수용액과 메탄올",
                 "gradient": "등용매(isocratic) 용리(혼합비는 원문 표에 있어 확인하지 못함)",
                 "flow": "0.8 mL/min", "temp": "실온", "detection": "280 nm",
                 "injection": "50 µL",
                 "sample_prep": "동결건조 후 20–30메시 분쇄한 분말 30 g + 70% 에탄올 600 mL, 80 °C 3시간 추출 → 여과(Whatman No. 2) → 50 °C 감압 농축 → 동결건조; 메탄올에 녹여 0.45 μm PET 주사기 필터로 거름",
                 "standard": "클로로젠산 표준품(Sigma); 머무름 시간·PDA 스펙트럼 대조",
                 "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "HPLC-Q/TOF-MS에서 면적이 가장 큰 두 봉우리가 퀸산과 클로로젠산이었고, 선행 연구에서 참취의 카페오일퀸산 가운데 클로로젠산이 가장 많았기 때문에 저자들이 추출물의 대표 생리활성 성분으로 정했다[4]. 검량선·검출한계·회수율은 원문에 보고되지 않았다[4].",
  "source": [4], "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC7766398/", "source_kind": "paper"},
 {"role": "literature", "compound": "Caffeoylquinic acids", "compound_ko": "카페오일퀸산 7종(3,4-·3,5-·4,5-디카페오일퀸산, 3,5-디카페오일-에피-퀸산, 5-·3-카페오일퀸산, 3-p-쿠마로일-카페오일퀸산)",
  "part": "취나물로 쓰는 국화과 산나물(참취 포함)의 건조 식물체와 추출물",
  "content": "추출물 중 카페오일퀸산 비율 20.25–38.35%(여러 취나물 종 전체 범위)[15]; 참취 5-O-카페오일퀸산 9.34 ± 0.11 mg/g 건조중량(다른 논문이 인용한 값)[4]",
  "method": "HPLC(동시 정량)",
  "conditions": {"instrument": "", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "", "injection": "", "sample_prep": "", "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "취나물류에 많은 카페오일퀸산 7종을 한 번에 정량하는 HPLC 법으로, 참취의 대표 성분군을 비교하는 지표로 쓸 수 있다[15][34]. 전문 확인 못함 — 초록만 보았으므로 분석 조건을 비워 두었고, 20.25–38.35%는 참취만의 값이 아니다[15].",
  "source": [15, 4], "url": "https://pubmed.ncbi.nlm.nih.gov/19898797/", "source_kind": "paper"},
 {"role": "literature", "compound": "Myricetin", "compound_ko": "미리세틴 등 폴리페놀 23종", "part": "잎(용매별 추출물)",
  "content": "미리세틴 4850.45 μg/g, 카페산 104.20 μg/g, 젠티스산 84.50 μg/g, 갈산 61.05 μg/g, 호모젠티스산 55.65 μg/g; 총페놀·총플라보노이드는 에틸아세테이트 추출물에서 각각 322.43·6.51 mg/g으로 가장 높음[16]",
  "method": "UHPLC",
  "conditions": {"instrument": "", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "", "injection": "", "sample_prep": "석유에테르·에틸아세테이트·메탄올·부탄올·물 추출(세부 조건 확인하지 못함)", "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "참취 잎의 폴리페놀 23종을 동정·정량한 연구로, 플라보놀 가운데 미리세틴이 가장 많다고 보고했다[16]. 전문 확인 못함 — 초록만 보았고, 함량의 기준(건조 잎인지 추출물인지)은 확인하지 못함.",
  "source": [16], "url": "https://pubmed.ncbi.nlm.nih.gov/24873908/", "source_kind": "paper"},
]

d = {
 "slug": "aster-scaber", "name_ko": "참취", "name_en": "Edible aster",
 "scientific_name": "Aster scaber Thunb.",
 "aliases": ["참취잎", "건조참취", "절임참취", "취", "취나물", "동풍채", "Edible aster", "Rough aster", "chamchwi", "Doellingeria scabra (Thunb.) Nees"],
 "sections": sections, "compounds": compounds, "markers": [], "assays": assays,
 "nutrients": [], "production": [], "world": [], "gi": [], "orgs": [], "sources": sources,
}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in sections: print(s["key"], len(s["body"]))
