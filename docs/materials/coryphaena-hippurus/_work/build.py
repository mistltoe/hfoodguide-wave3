"""만새기(Coryphaena hippurus) dossier.json 생성. 본문의 [@key] 를 첫 등장 순서대로 번호로 바꾼다."""
import json
import re
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "dossier.json"
ACC = "2026-11-02"


def pm(title, doi, journal, pmid, note="초록 확인"):
    url = f"https://doi.org/{doi}" if doi else f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
    return {"title": f"{title} ({note})", "url": url, "publisher": f"{journal}, PMID {pmid}", "accessed": ACC}


S = {
    "mfds": {"title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — Coryphaena hippurus 1행: 원료명 '만새기', 영문 Common dolphinfish, 분류 수산물, 대분류 식품원료(A코드), 부위 '-', 사용조건 기준 없음, 상태 사용가능, 별명 없음; 같은 속 다른 종(C. equiselis) 행 없음; 고시형 원료 원재료 목록(KR_NOTICE) 없음 — 로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json, docs/materials/coryphaena-hippurus/card.json",
             "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
    "dryage": pm("From Fresh to Aged: Dynamics of Lipid Stability, Fatty Acid Profile, and Meat Quality of Dry-Aged Dorsal Epaxial Muscle of Mahi-Mahi (Coryphaena hippurus). J Food Sci 2026;91(5):e71074", "10.1111/1750-3841.71074", "Journal of Food Science", "42089280", "PMC13147317 전문 확인"),
    "chileFA": pm("Fatty acid profiles of highly migratory resources from the Southeastern Pacific Ocean, Chile: a potential tool for biochemical and nutritional traceability. PeerJ 2025;13:e19101", "10.7717/peerj.19101", "PeerJ", "40124606", "PMC11930215 전문 확인"),
    "adams": pm("Consistently low mercury concentrations in dolphinfish, Coryphaena hippurus, an oceanic pelagic predator. Environ Res 2009;109(6):697-701", "10.1016/j.envres.2009.05.004", "Environmental Research", "19539279"),
    "choy": pm("The influence of depth on mercury levels in pelagic fishes and their prey. Proc Natl Acad Sci U S A 2009;106(33):13865-9", "10.1073/pnas.0900711106", "PNAS", "19666614"),
    "kojad": pm("Mercury content in commercial pelagic fish and its risk assessment in the Western Indian Ocean. Sci Total Environ 2006;366(2-3):688-700", "10.1016/j.scitotenv.2006.02.006", "Science of the Total Environment", "16580709"),
    "teffer": pm("Trophic influences on mercury accumulation in top pelagic predators from offshore New England waters of the northwest Atlantic Ocean. Mar Environ Res 2014;101:124-134", "10.1016/j.marenvres.2014.09.008", "Marine Environmental Research", "25440782"),
    "ecuador": pm("Heavy metals in yellowfin tuna (Thunnus albacares) and common dolphinfish (Coryphaena hippurus) landed on the Ecuadorian coast. Sci Total Environ 2015;541:149-154", "10.1016/j.scitotenv.2015.09.090", "Science of the Total Environment", "26406109"),
    "lapaz": pm("Selenium and mercury in dolphinfish (Coryphaena hippurus) from the Gulf of California: inter-annual variations and selenium health benefit value. Environ Sci Pollut Res Int 2019;27(2):2311-2318", "10.1007/s11356-019-06795-3", "Environmental Science and Pollution Research", "31776904"),
    "segc": pm("Patterns of mercury and selenium in tissues and stomach contents of the dolphinfish Coryphaena hippurus from the SE Gulf of California, Mexico. Mar Pollut Bull 2018;138:84-92", "10.1016/j.marpolbul.2018.11.023", "Marine Pollution Bulletin", "30660317"),
    "longisl": pm("Relationship between trace element concentrations and body length in dolphinfish (Coryphaena hippurus) in the northwest Atlantic Ocean. Environ Sci Pollut Res Int 2023;30(37):87757-87767", "10.1007/s11356-023-28465-1", "Environmental Science and Pollution Research", "37432573"),
    "medit": pm("Wild fish and seafood species in the western Mediterranean Sea with low safe mercury concentrations. Environ Pollut 2022;314:120274", "10.1016/j.envpol.2022.120274", "Environmental Pollution", "36167168"),
    "nwmex": pm("Risk and Benefit Analysis of Fish Consumption in NW Mexico: Mercury, Selenium, and Fatty Acids. Arch Environ Contam Toxicol 2022;83(1):36-46", "10.1007/s00244-022-00939-2", "Archives of Environmental Contamination and Toxicology", "35690954"),
    "weqatl": pm("Ecological drivers of mercury accumulation in oceanic apex predators: A human consumption advisory. Sci Total Environ 2025;970:178994", "10.1016/j.scitotenv.2025.178994", "Science of the Total Environment", "40043652"),
    "baran90": pm("Decomposition and Histamine Content in Mahimahi (Coryphaena hippurus). J Food Prot 1990;53(3):217-222", "10.4315/0362-028X-53.3.217", "Journal of Food Protection", "31018389"),
    "starus": pm("Effects of on-board and dockside handling on the formation of biogenic amines in mahimahi (Coryphaena hippurus), skipjack tuna (Katsuwonus pelamis), and yellowfin tuna (Thunnus albacares). J Food Prot 2004;67(1):134-41", "10.4315/0362-028x-67.1.134", "Journal of Food Protection", "14717363"),
    "antoine04": pm("Chemical analysis and sensory evaluation of mahi-mahi (Coryphaena hippurus) during chilled storage. J Food Prot 2004;67(10):2255-62", "10.4315/0362-028x-67.10.2255", "Journal of Food Protection", "15508638"),
    "antoine02": pm("Gas chromatographic analysis of histamine in mahi-mahi (Coryphaena hippurus). J Agric Food Chem 2002;50(17):4754-9", "10.1021/jf020148x", "Journal of Agricultural and Food Chemistry", "12166956"),
    "raoult": pm("Histamine production by Raoultella ornithinolytica in mahi-mahi meat at various storage temperatures. J Food Drug Anal 2015;24(2):305-310", "10.1016/j.jfda.2014.06.010", "Journal of Food and Drug Analysis", "28911583"),
    "photob": pm("Histamine Production by Photobacterium spp. in Tuna and Mahi-Mahi under Various Storage Temperatures. J Food Prot 2026;89(5):100752", "10.1016/j.jfp.2026.100752", "Journal of Food Protection", "41850657"),
    "kim79": pm("Flushing syndrome due to mahimahi (scombroid fish) poisoning. Arch Dermatol 1979;115(8):963-5", "", "Archives of Dermatology", "572660"),
    "pancr": pm("Scombroid pancreatitis from mahi-mahi consumption. BMJ Case Rep 2021;14(2):e240261", "10.1136/bcr-2020-240261", "BMJ Case Reports", "33619144"),
    "taylor89": pm("Histamine poisoning (scombroid fish poisoning): an allergy-like intoxication. J Toxicol Clin Toxicol 1989;27(4-5):225-40", "10.3109/15563658908994420", "Journal of Toxicology: Clinical Toxicology", "2689658"),
    "rasff": pm("[Analysis of notifications on exceeding of the acceptable level of histamine according to the RASFF reports]. Rocz Panstw Zakl Hig 2011;62(4):365-9", "", "Roczniki Panstwowego Zakladu Higieny", "22435289", "영문 초록 확인"),
    "toda": pm("[Histamine food poisonings in Japan and other countries]. Kokuritsu Iyakuhin Shokuhin Eisei Kenkyusho Hokoku 2009;(127):31-8", "", "Bulletin of National Institute of Health Sciences(일본 국립의약품식품위생연구소)", "20306704", "영문 초록 확인"),
    "pottier": pm("[Evaluation of Antilles fish ciguatoxicity by mouse and chick bioassays]. Bull Soc Pathol Exot 2003;96(1):24-8", "", "Bulletin de la Société de pathologie exotique", "12784589", "영문 초록 확인"),
    "ncciguat": pm("Ciguatera fish poisoning: an outbreak associated with fish caught from North Carolina coastal waters. South Med J 1990;83(4):379-82", "", "Southern Medical Journal", "2321066"),
    "parv": pm("Immunological cross-reactivity between four distant parvalbumins-Impact on allergen detection and diagnostics. Mol Immunol 2014;63(2):437-48", "10.1016/j.molimm.2014.09.019", "Molecular Immunology", "25451973"),
    "genome": pm("The draft genome assembly of the cosmopolitan pelagic fish dolphinfish Coryphaena hippurus. G3 (Bethesda) 2025;15(5):jkaf059", "10.1093/g3journal/jkaf059", "G3: Genes|Genomes|Genetics", "40102961"),
    "globalgen": pm("Global genome-wide patterns of genetic diversity and population structure in Coryphaena hippurus. Mol Phylogenet Evol 2026;224:108694", "10.1016/j.ympev.2026.108694", "Molecular Phylogenetics and Evolution", "42471037"),
    "mitog": pm("Complete mitogenome of two dolphinfishes (Coryphaena 2종) from South China sea. Mitochondrial DNA B Resour 2018;3(2):1098-1099", "10.1080/23802359.2018.1516120", "Mitochondrial DNA Part B", "33474431"),
    "chromo": pm("Chromosomal distribution of two multigene families and the unusual occurrence of an X1X1X2X2/X1X2Y sex chromosome system in the dolphinfish (Coryphaenidae). Genet Mol Res 2014;13(2):2470-9", "10.4238/2014.April.3.19", "Genetics and Molecular Research", "24782001"),
    "tep": pm("Genetic divergence at species boundaries of the dolphinfish (Coryphaena hippurus) in the Tropical Eastern Pacific. PeerJ 2022;10:e14389", "10.7717/peerj.14389", "PeerJ", "36415864"),
    "medrad": pm("RAD SNP markers as a tool for conservation of dolphinfish Coryphaena hippurus in the Mediterranean Sea. Mar Genomics 2016;28:57-62", "10.1016/j.margen.2016.07.003", "Marine Genomics", "27450636"),
    "transc": pm("Novel transcriptome assembly and comparative toxicity pathway analysis in mahi-mahi (Coryphaena hippurus) embryos and larvae exposed to Deepwater Horizon oil. Sci Rep 2017;7:44546", "10.1038/srep44546", "Scientific Reports", "28295044"),
    "lifedev": pm("Mahi-mahi (Coryphaena hippurus) life development: morphological, physiological, behavioral and molecular phenotypes. Dev Dyn 2019;248(5):337-350", "10.1002/dvdy.27", "Developmental Dynamics", "30884004"),
    "cadiz": pm("Common dolphinfish, Coryphaena hippurus, spawn at their easternmost Atlantic range adjacent to the Mediterranean Sea. J Fish Biol 2020;97(2):409-415", "10.1111/jfb.14379", "Journal of Fish Biology", "32402108"),
    "phenol": pm("Predicting fish spawning phenology for adaptive management: Integrating thermal drivers and fishery constraints. Mar Environ Res 2024;202:106713", "10.1016/j.marenvres.2024.106713", "Marine Environmental Research", "39226782"),
    "warming": pm("Projected effects of ocean warming on an iconic pelagic fish and its fishery. Sci Rep 2021;11(1):8803", "10.1038/s41598-021-88171-1", "Scientific Reports", "33888813"),
    "vertical": pm("Vertical distributions of dolphinfish (Coryphaena hippurus) in the Eastern Pacific Ocean suggest variability in potential associations with floating objects. PLoS One 2022;17(11):e0276873", "10.1371/journal.pone.0276873", "PLoS One", "36318582"),
    "energy": pm("Vertical energy seascapes and diving behaviour modulate metabolic scope in a pelagic predator. Proc Biol Sci 2025;292(2045):20250200", "10.1098/rspb.2025.0200", "Proceedings of the Royal Society B", "40237086"),
    "tehuan": pm("[Variability in the relative abundance, size structure and sex ratio of the dolphinfish Coryphaena hippurus in the Gulf of Tehuantepec, México]. Rev Biol Trop 2014;62(2):611-26", "", "Revista de Biología Tropical", "25102644", "영문 초록 확인"),
    "maldiv": pm("Bycatch in the Maldivian pole-and-line tuna fishery. PLoS One 2017;12(5):e0177391", "10.1371/journal.pone.0177391", "PLoS One", "28542258"),
    "collagen": pm("Biochemical study of type I collagen purified from skin of warm sea teleost Mahi mahi (Coryphaena hippurus), with a focus on thermal and physical stability. J Food Biochem 2019;43(11):e13013", "10.1111/jfbc.13013", "Journal of Food Biochemistry", "31407365"),
    "cpep": pm("Collagen Peptide Upregulates Osteoblastogenesis from Bone Marrow Mesenchymal Stem Cells through MAPK-Runx2. Cells 2019;8(5):446", "10.3390/cells8050446", "Cells", "31083501"),
    "print3d": pm("Nutritional quality and benefit-risk ratio of 3D-printed fish developed from canned Mahi mahi (Coryphaena hippurus). J Sci Food Agric 2025;105(14):8223-8232", "10.1002/jsfa.70067", "Journal of the Science of Food and Agriculture", "40682566"),
    "brine": pm("The effect of combined traditional and novel treatments on oxidative status of dolphinfish (Coryphaena hippurus) and sardine (Sardina pilchardus) muscle lipids. Food Sci Technol Int 2014;20(6):431-40", "10.1177/1082013213489307", "Food Science and Technology International", "23751550"),
    "mislabel": pm("DNA barcoding reveals global and local influences on patterns of mislabeling and substitution in the trade of fish in Mexico. PLoS One 2022;17(4):e0265960", "10.1371/journal.pone.0265960", "PLoS One", "35421106"),
    "surimi": pm("DNA metabarcoding unveils the hidden species composition in fish surimi. Heliyon 2024;10(16):e36287", "10.1016/j.heliyon.2024.e36287", "Heliyon", "39247285"),
    "sda": pm("Nutritional physiology of mahi-mahi (Coryphaena hippurus): Postprandial metabolic response to different diets and metabolic impacts on swim performance. Comp Biochem Physiol A 2018;215:28-34", "10.1016/j.cbpa.2017.10.016", "Comparative Biochemistry and Physiology Part A", "29054806"),
    "fukushima": pm("Impact of the Fukushima Dai-ichi Nuclear Power Plant Accident on dolphin fishes in the Northwest Pacific. Chemosphere 2020;257:127267", "10.1016/j.chemosphere.2020.127267", "Chemosphere", "32534298"),
    "urocan": pm("Low-Temperature Production of Urocanic Acid by Spoilage Bacteria Isolated from Mahimahi (Coryphaena hippurus). Appl Environ Microbiol 1985;50(2):546-7", "10.1128/aem.50.2.546-547.1985", "Applied and Environmental Microbiology", "16346871"),
    "opa": pm("HPLC method for analysis of free amino acids in fish using o-phthaldialdehyde precolumn derivatization. J Agric Food Chem 1999;47(12):5100-7", "10.1021/jf990032+", "Journal of Agricultural and Food Chemistry", "10606579"),
    "aoac97": pm("Gas chromatographic method for putrescine and cadaverine in canned tuna and mahimahi and fluorometric method for histamine (minor modification of AOAC Official Method 977.13): collaborative study. J AOAC Int 1997;80(3):591-602", "", "Journal of AOAC International", "9170656"),
    "aoac15": pm("Modification and Single-Laboratory Validation of AOAC Official Method 977.13 for Histamine in Seafood to Improve Sample Throughput. J AOAC Int 2015;98(3):622-627", "10.5740/jaoacint.14-194", "Journal of AOAC International", "26086251"),
    "oilwild": pm("Brief Oil Exposure Reduces Fitness in Wild Gulf of Mexico Mahi-Mahi (Coryphaena hippurus). Environ Sci Technol 2022;56(18):13019-13028", "10.1021/acs.est.2c01783", "Environmental Science & Technology", "36053064"),
    "strip": pm("Development of a rapid colorimetric strip method for determination of volatile bases in mahi-mahi and tuna. J Food Sci 2021;86(6):2398-2409", "10.1111/1750-3841.15737", "Journal of Food Science", "33928640"),
    "ako": pm("Omega-3 fatty acids in Hawaii seafood. Hawaii Med J 1994;53(5):142-5", "", "Hawaii Medical Journal", "8050896"),
    "ncbact": pm("Detection and identification of histamine-producing bacteria associated with harvesting and processing mahimahi and yellowfin tuna. J Food Prot 2005;68(8):1676-82", "10.4315/0362-028x-68.8.1676", "Journal of Food Protection", "21132978"),
}

sections = [
 ("overview", "한눈에 보기", """만새기(Coryphaena hippurus)는 식약처 「식품원료 목록」에 '만새기'(영문 Common dolphinfish)라는 원료명으로 올라 있는 수산물이다[@mfds]. 이 목록에서 만새기는 학명 1행뿐이며 상태는 '사용가능', 부위 칸은 '-'이고 따로 정한 사용 조건이나 별명은 없다[@mfds]. 건강기능식품 고시형 원료의 원재료 목록에는 없으므로 식약처가 정한 지표성분도 없다[@mfds].

만새기는 전 세계 열대·아열대 바다의 표층에 사는 대양성 포식어로, 멀리 이동하며 멕시코·에콰도르·페루·중앙아메리카에서 상업·유어 어업의 대상이다[@tehuan]. 영어로는 마히마히(mahi-mahi) 또는 돌핀피시(dolphinfish)라고 부른다[@dryage]. 살은 지방이 적은 편이어서 갓 잡은 등쪽 살의 수분은 76.9%, 단백질 20.9%, 지질 1.3%였다[@dryage]. 수은은 다른 대형 회유어보다 대체로 낮게 측정되지만, 상온에 두면 히스타민이 쌓여 히스타민(스콤브로이드) 식중독을 일으킬 수 있는 대표 어종으로 꼽힌다[@adams, @taylor89, @starus]. 국가표준식품성분표의 만새기 성분값과 국내 어획 통계는 이번 조사에서 확인하지 못함."""),
 ("history", "이용·연구 역사", """만새기는 하와이에서 일찍부터 히스타민 식중독의 원인 생선으로 알려졌다[@kim79]. 1979년 보고는 스콤브로이드 식중독이 보통 고등어과 생선에서 생기지만 하와이에서는 만새기가 가장 흔한 원인이라고 적었다[@kim79]. 1985년에는 만새기 부패균이 저온에서 히스티딘을 유로칸산으로 바꾼다는 연구가 나왔다[@urocan]. 1990년 하와이 연구는 바닷물 온도별 보관 실험으로 부패와 히스타민 생성 속도를 비교했다[@baran90].

1997년에는 통조림 다랑어와 생 만새기 시료로 히스타민 형광법(AOAC 977.13) 변경안과 푸트레신·카다베린 가스크로마토그래피법을 16개·14개 실험실이 함께 검증했다[@aoac97]. 2004년 미국 식품의약국 연구는 배 위와 부두에서의 취급 온도가 만새기 히스타민 생성에 주는 영향을 정리했다[@starus]. 2010년 멕시코만 원유 유출 뒤에는 만새기 배아·자어와 야생 개체가 원유 독성 연구의 모델로 쓰였다[@transc, @oilwild]. 2015년에는 AOAC 977.13 형광법을 줄인 변형법이 다랑어·만새기·삼치류 시료에서 회수율 92–105%, 검출한계 0.2–0.5 ppm으로 검증되었다[@aoac15]. 2025년에는 만새기 전장 유전체 초안이 처음 발표되었다[@genome]."""),
 ("biology", "어종·생태·번식", """만새기는 열대·아열대 바다 표층에 사는 빠른 대형 포식어로, 멕시코 테우안테펙만 어획물은 가랑이체장 20.5–152 cm였다[@tehuan]. 수명이 짧고 빨리 자라는 종으로 소개되며, 이런 생활사가 서식지와 관계없이 비슷해 수은 농도를 좌우하는 요인도 전 세계에서 비슷할 것으로 추정되었다[@adams]. 대사율과 성장 속도가 높은 종으로, 야생 개체는 끊임없이 오르내리는 잠수를 하며 밤에는 더 깊이, 낮에는 더 활발히 움직였다[@energy]. 동태평양 원격 추적 23마리(678일)에서는 떠다니는 물체 주변에 머무는 행동이 지역에 따라 달랐다[@vertical].

여러 위도의 집단을 분석한 결과 연평균 수온과 산란기 폭 사이에 직접적인 관계가 있었고, 산란 정점은 수온 정점보다 약 49일 앞섰다[@phenol]. 스페인 카디스만에서는 여름에 잡힌 20마리 가운데 가장 작은 암컷을 뺀 모두가 산란 단계였다[@cadiz]. 사육한 만새기의 수정란부터 성어까지의 발달 단계표가 만들어졌는데, 많은 발달 지표가 제브라피시 같은 온수성 경골어와 비슷했다[@lifedev]. 국내 연안의 출현 시기와 분포는 이번 조사에서 공식 자료로 확인하지 못함."""),
 ("related_species", "관련 종·이름", """만새기과(Coryphaenidae)는 만새기속 하나에 만새기와 Coryphaena equiselis 두 종만 있다[@mitog, @chromo]. 남중국해산 두 종의 미토콘드리아 전장 유전체는 16,731 bp와 16,690 bp로 해독되었다[@mitog]. 염색체 연구에서 만새기 암컷은 2n = 48이었고, C. equiselis 수컷은 2n = 47로 X1X1X2X2/X1X2Y 다중 성염색체 체계를 보였다[@chromo]. 식약처 「식품원료 목록」에는 이 과에서 만새기 1종만 올라 있다[@mfds].

시장에서는 다른 생선과 바뀌어 팔리는 일이 있다[@mislabel]. 멕시코 세 도시에서 생선 376점을 DNA 바코드로 조사한 결과 전체 오표기율은 30.8%, 마히마히 상품명의 오표기율은 39%였다[@mislabel]. 대만 어묵(수리미) 제품 120점을 메타바코딩으로 분석했을 때 돌핀피시(dolphinfish)가 밀크피시 등과 함께 주요 원료 어종으로 나왔다(초록에서 학명은 확인하지 못함)[@surimi]."""),
 ("cultivation", "어획·양식", """만새기는 세계 여러 바다에서 상업 어업과 유어 낚시의 대상이다[@warming, @tehuan]. 테우안테펙만에서는 소규모 연안 어업에 혼획되며, 2000–2007년 6개 양륙지에서 암컷 3,494마리와 수컷 3,877마리가 조사되었다[@tehuan]. 몰디브 장대낚시 다랑어 어업에서는 혼획물의 93%를 레인보러너(Elagatis bipinnulata)와 만새기가 차지했고, 혼획물의 95%는 이용되었다[@maldiv]. 개체 기반 모형은 해양 열파 조건에서 어획 평균 체장이 현재보다 13.2% 커질 것으로 예측했다[@warming].

미국 연구진은 사육한 만새기의 수정란부터 성어까지 발달을 기록했고, 사육 성어로 영양 생리 실험을 했다[@lifedev, @sda]. 사육 성어(평균 706 g)를 배부르게 먹였을 때 먹은 양은 먹이의 무게가 아니라 열량으로 정해졌고, 먹이에 따라 체중의 2.9–16.2%를 먹었다[@sda]. 상업 양식 생산 규모, 국내 어획량과 원양 생산 통계는 해양수산부·통계청 원자료를 이 환경에서 열지 못해 확인하지 못함."""),
 ("processing", "가공·저장·품질", """만새기 살의 품질과 안전은 잡은 뒤 온도 관리에 크게 좌우된다[@baran90, @starus]. 바닷물에 담가 26 °C에 두면 히스타민 50 ppm까지 12시간 넘게 걸렸지만 35 °C에서는 9시간 안에 도달했고, 그 뒤 3시간 안에 500 ppm을 넘었다[@starus]. 7 °C 냉장 필레는 3일째 히스타민 5 mg/100 g, 휘발성염기질소 30 mg/100 g에 이르렀다[@antoine04]. Raoultella ornithinolytica를 접종한 살은 25 °C·37 °C에서 12시간 안에 히스타민 50 mg/100 g을 넘었지만 4 °C 이하에서는 억제되었다[@raoult]. 미리 −20 °C에 얼려 두면 이후의 히스타민 생성 속도가 느려졌으나, 이미 생긴 히스타민은 굽거나 쪄도 거의 줄지 않았다[@baran90]. 부패도를 빨리 보는 색 변화 시험지와 가스크로마토그래피 분석법도 만새기로 개발되었다[@strip, @antoine02].

3 °C·상대습도 83%에서 42일 건식 숙성한 등쪽 살은 수분이 76.9%에서 61.5%로 줄고 단백질은 35.4%로 늘었으며, 연구진은 27일 무렵을 최적점으로 보았다[@dryage]. 오레가노·로즈마리 추출물 염지와 훈연은 염지·고압 처리로 생기는 지질 산화를 처리와 어종(만새기·정어리)에 따라 6.6–69.8% 줄였다[@brine]. 부산물로는 껍질 콜라겐의 변성 온도가 해산 경골어 가운데 높았고, 뼈에서 얻은 콜라겐 펩타이드가 세포 실험에서 조골 분화를 높였다[@collagen, @cpep]. 통조림 만새기 살로 만든 3D 프린팅 식품 연구도 있다[@print3d]."""),
 ("genetics", "유전 정보", """2025년 발표된 만새기 유전체 초안은 일루미나와 나노포어 염기서열을 함께 써 497.8 Mb, 6,044개 콘티그(N50 200.9 kb)로 조립되었고 BUSCO 완성도는 89%였다[@genome]. 870만 개 SNP와 미토콘드리아 전장 유전체를 쓴 2026년 세계 집단 분석에서는 대서양·태평양·인도양·지중해의 네 집단이 처음으로 구분되었다[@globalgen]. 지중해 집단은 지브롤터 해협을 사이에 둔 역사적 고립으로 뚜렷한 유전 특징을 보였으나, 대양 사이의 과거 유전자 흐름 신호도 함께 나타났다[@globalgen].

지중해 8곳 140마리를 RAD 방식 3,324개 SNP로 분석한 연구에서는 성별과 연관된 좌위 311개가 확인되어 집단의 성비 추정에 쓰였다[@medrad]. 열대 동태평양에서는 미토콘드리아 유전자로는 차이가 없었지만, 핵 미세부수체 14개 좌위로는 네 유전 집단이 구분되었다[@tep]. 원유 노출 배아·자어로 만든 첫 전사체에는 60,842개 전사물이 조립되었다[@transc]."""),
 ("safety", "안전성", """만새기는 상온에 방치되면 살 속 히스티딘이 세균에 의해 히스타민으로 바뀌어 히스타민(스콤브로이드) 식중독을 일으키는 대표 비고등어과 생선이다[@taylor89, @kim79]. 증상은 햇볕에 탄 듯한 홍조, 두통, 두드러기, 구역 같은 알레르기 비슷한 반응이며 항히스타민제로 대개 빨리 가라앉는다[@kim79, @taylor89]. 유럽 신속경보시스템(RASFF) 2003–2009년 통보에서는 만새기 히스타민이 허용치의 17배가 넘는 3,490 mg/kg까지 나왔다[@rasff]. 미국 식품의약국 지침은 히스타민 200 ppm 이상을 건강 위해, 35 ppm 이상을 부패 증거로 본다[@photob]. 국내 식품공전의 만새기 히스타민 기준은 이번 조사에서 원문으로 확인하지 못함.

시구아테라는 과들루프·생바르텔레미 근해 생선 178마리(26종) 생물검정에서 만새기가 독성 없는 어종으로 분류되었고, 노스캐롤라이나 집단 발병 때도 원인은 함께 먹은 바라쿠다로 추정되었다[@pottier, @ncciguat].

근육 총수은은 플로리다 385마리 평균 0.10 mg/kg(습중량)이었다[@adams]. 그러나 캘리포니아만 라파스 개체 평균은 0.61 μg/g이었고, 에콰도르 양륙 개체는 근육 시료의 약 절반이 카드뮴·수은의 유럽연합 기준을 넘어 성인 주당 178 g 이하 섭취가 제안되었다[@lapaz, @ecuador]. 롱아일랜드 16마리는 모두 셀레늄/수은 몰비가 1을 넘었다[@longisl].

파브알부민 검출 항체 연구에서 생 만새기 추출물은 파브알부민이 검출되지 않았으나 이는 해당 항체의 반응 결과이다[@parv]. 식약처 등 국내 공공기관의 만새기 알레르기 정보는 확인하지 못함."""),
]

compounds = [
 dict(name="Histamine", name_ko="히스타민", class_="생체아민(부패 지표·식중독 원인)", role="marker", part="살(필레·등살)",
      content_text="7 °C 냉장 3일째 5 mg/100 g[@antoine04]; 35 °C 바닷물 9시간 안에 50 ppm, 이후 3시간 안에 500 ppm 초과[@starus]; RASFF 통보 최고 3,490 mg/kg[@rasff]",
      activity_ko="히스타민(스콤브로이드) 식중독의 원인 물질이며 신선도 지표로 쓰인다[@taylor89, @antoine02]", src=["antoine04", "starus", "rasff", "taylor89", "antoine02"]),
 dict(name="Histidine", name_ko="히스티딘", class_="아미노산(히스타민 전구체)", role="nutrient", part="살",
      content_text="함량 수치는 초록에서 확인하지 못함",
      activity_ko="세균의 탈탄산으로 히스타민이 되며, 만새기·눈다랑어·가자미 살에서 OPA 유도체화 HPLC로 정량되었다[@opa, @kim79]", src=["opa", "kim79"]),
 dict(name="Cadaverine", name_ko="카다베린", class_="생체아민", role="marker", part="필레",
      content_text="7 °C 냉장 3일째 3 mg/100 g[@antoine04]",
      activity_ko="히스타민보다 먼저 늘어나는 부패 지표로 보고되었다[@starus, @antoine04]", src=["antoine04", "starus"]),
 dict(name="Putrescine", name_ko="푸트레신", class_="생체아민", role="marker", part="필레",
      content_text="7 °C 냉장 3일째 0.5 mg/100 g[@antoine04]",
      activity_ko="냄새 점수와 상관(r = 0.75)을 보인 부패 지표[@antoine04]", src=["antoine04"]),
 dict(name="Urocanic acid", name_ko="유로칸산", class_="히스티딘 대사물", role="marker", part="얼음 저장 살에서 분리한 세균 배양액",
      content_text="분리균 166주 중 58주 양성, 활성 상위 8주는 약 10 mg/100 mL 생성(10 °C 4일 배양)[@urocan]",
      activity_ko="저온 저장 생선에서 히스타민을 대신할 부패 지표 후보로 제안되었다[@urocan]", src=["urocan"]),
 dict(name="Palmitic acid", name_ko="팔미트산", class_="포화지방산", role="nutrient", part="등쪽 살(지질)",
      content_text="신선 살 31.21±2.06%(지방산 조성), 숙성 27일 25.36%[@dryage]; 칠레산 근육 0.02±0.002 mg/20 mg 건물[@chileFA]",
      activity_ko="칠레산 시료 지방산 유사도의 29.33%를 설명한 주 성분[@chileFA]", src=["dryage", "chileFA"]),
 dict(name="Oleic acid", name_ko="올레산", class_="단일불포화지방산(ω-9)", role="nutrient", part="등쪽 살(지질)",
      content_text="신선 살 17.87±2.30%, 건식 숙성 27일 30.00±1.55%[@dryage]; 칠레산 근육 0.02±0.003 mg/20 mg 건물[@chileFA]",
      activity_ko="건식 숙성 초기 지방 분해로 늘었다가 산화로 다시 줄었다[@dryage]", src=["dryage", "chileFA"]),
 dict(name="Stearic acid", name_ko="스테아르산", class_="포화지방산", role="nutrient", part="등쪽 살(지질)",
      content_text="신선 살 17.10±1.17%, 숙성 42일 19.25±1.01%[@dryage]; 칠레산 근육 0.01±0.001 mg/20 mg 건물[@chileFA]",
      activity_ko="불포화지방산이 산화로 줄면서 상대 비율이 높아졌다[@dryage]", src=["dryage", "chileFA"]),
 dict(name="Docosahexaenoic acid", name_ko="도코사헥사엔산(DHA)", class_="n-3 고도불포화지방산", role="nutrient", part="근육",
      content_text="칠레산 8마리 근육 0.01±0.003 mg/20 mg 건물(EPA 불검출)[@chileFA]",
      activity_ko="하와이 수산물 조사에서 만새기 알은 오메가-3 함량이 중간 수준으로 분류되었다[@ako]", src=["chileFA", "ako"]),
 dict(name="Malondialdehyde", name_ko="말론다이알데하이드(TBARS)", class_="지질 과산화 산물", role="marker", part="등쪽 살",
      content_text="신선 0.15, 15일 0.21, 27일 0.56, 42일 0.53 mg MDA/kg(3 °C 건식 숙성)[@dryage]",
      activity_ko="지질 산화 정도를 보는 지표로, 숙성 최적 기간 판단에 쓰였다[@dryage]", src=["dryage"]),
 dict(name="Mercury", name_ko="수은(총수은·메틸수은)", class_="유해 중금속", role="bioactive", part="근육",
      content_text="플로리다 385마리 평균 0.10 mg/kg(범위 0.012–0.55, 습중량)[@adams]; 서적도대서양 190.7±82.8 ng/g, 메틸수은 비율 80% 초과[@weqatl]; 라파스 평균 0.61 μg/g[@lapaz]",
      activity_ko="체장이 클수록 높아지는 경향이 있으나 다른 대양성 포식어보다 낮은 편[@adams, @teffer]", src=["adams", "weqatl", "lapaz", "teffer"]),
 dict(name="Selenium", name_ko="셀레늄", class_="미량 무기질", role="nutrient", part="근육·신장",
      content_text="남동 캘리포니아만 근육 0.60±0.01 μg/g, 신장 5.60±0.40 μg/g[@segc]",
      activity_ko="셀레늄/수은 몰비가 1을 넘어 수은 독성을 줄일 수 있다고 해석되었다[@longisl, @lapaz]", src=["segc", "longisl", "lapaz"]),
 dict(name="Collagen type I", name_ko="제1형 콜라겐", class_="구조 단백질", role="bioactive", part="껍질",
      content_text="펩신 가용성 콜라겐의 프롤린+하이드록시프롤린 185/1,000 잔기, 변성 온도 산 가용성 29.5 °C·펩신 가용성 28.8 °C[@collagen]",
      activity_ko="조사된 해산 경골어 콜라겐 가운데 열안정성이 가장 높았다[@collagen]", src=["collagen"]),
 dict(name="Collagen peptide", name_ko="콜라겐 펩타이드", class_="단백질 가수분해물", role="bioactive", part="뼈",
      content_text="약 1 kDa 펩타이드를 분자량 차단막으로 분리[@cpep]",
      activity_ko="골수 중간엽 줄기세포의 조골 분화를 p38 MAPK–Runx2 경로로 높였다(세포 실험)[@cpep]", src=["cpep"]),
]

assays = [
 {"role": "literature", "compound": "Fatty acid methyl esters (C16:0, C18:0, C18:1 ω-9 etc.)", "compound_ko": "지방산 조성",
  "part": "등쪽 살(dorsal epaxial muscle)",
  "content": "신선(0일) C16:0 31.21±2.06%, C18:0 17.10±1.17%, C18:1 ω-9 17.87±2.30%, ω-6 1.27±0.62%, C14:0 12.46±1.09%(원문 표 4; 표에 EPA·DHA 항목 없음)[@dryage]",
  "method": "GC-FID",
  "conditions": {"instrument": "가스크로마토그래프(Perkin Elmer), 불꽃이온화검출기",
                 "column": "Omegawax-320 모세관 칼럼, 30 m × 0.32 mm i.d., 막 두께 0.25 μm(Supelco)",
                 "mobile_phase": "운반 기체 초고순도 헬륨",
                 "gradient": "110 °C → 40 °C/분 233 °C(2분 유지) → 1 °C/분 240 °C → 21분 등온",
                 "flow": "1.8 mL/min(헬륨, 정유량)",
                 "temp": "주입구 260 °C, 검출기 280 °C",
                 "detection": "FID",
                 "injection": "1 μL, split 1:20(10 psi)",
                 "sample_prep": "메탄올:클로로포름:물(2:1:0.8, v/v/v) 냉용매로 지질 추출 → 10% 메탄올성 HCl로 산 촉매 메틸화",
                 "standard": "37종 FAME 표준 혼합물(Supelco 18919-1AMP)과 머무름 시간 비교, 내부표준 면적 정규화·감응계수로 정량",
                 "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "지방산 조성과 동맥경화지수·혈전지수 같은 영양 지표가 건식 숙성 중 품질 변화를 판단하는 기준으로 쓰였다[@dryage]. 전문(Methods) 확인 — 검출·정량한계·회수율은 본문에 없음[@dryage].",
  "src": ["dryage"], "url": "https://doi.org/10.1111/1750-3841.71074", "source_kind": "paper"},
 {"role": "literature", "compound": "Fatty acid methyl esters (total lipid)", "compound_ko": "지방산 조성(총지질)",
  "part": "근육(1·2 등지느러미 사이 몸통)",
  "content": "8마리 평균 총 지방산 0.06±0.004 mg/20 mg 건물; C16:0 0.02±0.002, C18:0 0.01±0.001, C18:1n9 0.02±0.003, DHA 0.01±0.003 mg/20 mg 건물, EPA 불검출[@chileFA]",
  "method": "GC(FAME)",
  "conditions": {"instrument": "가스크로마토그래프 Agilent 7890A, ChemStation",
                 "column": "DB-225, 30 m × 0.25 mm i.d., 막 두께 0.25 μm(J&W Scientific)",
                 "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "", "injection": "",
                 "sample_prep": "−80 °C 동결건조·초음파 처리 → 건물 20 mg에서 다이클로로메테인:메탄올(2:1) 중량법 지질 추출 → 메탄올성 황산으로 70 °C 1시간 에스터화 → n-헥세인 6·3·3 mL로 3회 세척, 질소 농축",
                 "standard": "내부표준 C23:0, 해양 유래 지방산 인증 표준물(Supelco 37 FAME mix 47885-U)과 비교 동정",
                 "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "종별 지방산 조성을 회유성 어종의 종·산지 추적과 영양 상태 판단 지표로 제안했다[@chileFA]. 전문(Methods) 확인 — 원문에 검출기 종류·온도 프로그램·유속·검출한계·회수율이 적혀 있지 않음[@chileFA].",
  "src": ["chileFA"], "url": "https://doi.org/10.7717/peerj.19101", "source_kind": "paper"},
 {"role": "literature", "compound": "Histamine", "compound_ko": "히스타민", "part": "살",
  "content": "초록에 시료 함량 값 없음; 방법 성능은 rationale 참조[@antoine02]",
  "method": "GC(가스크로마토그래피, 유도체화)",
  "conditions": {"instrument": "", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "",
                 "injection": "", "sample_prep": "", "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "히스타민은 스콤브로이드 식중독의 공통 요인이자 생선 품질의 화학 지표여서 만새기 정량법이 개발되었다[@antoine02]. 초록 기준으로 평균 회수율은 GC 67%, AOAC 형광법 90%였고 두 방법의 상관은 0.96, 히스타민 머무름 시간은 8.2분이었다[@antoine02]. 전문 확인 못함 — 칼럼·온도 조건은 비워 둠.",
  "src": ["antoine02"], "url": "https://doi.org/10.1021/jf020148x", "source_kind": "paper"},
 {"role": "literature", "compound": "Free amino acids (histidine, lysine, ornithine)", "compound_ko": "유리아미노산(히스티딘·라이신·오르니틴)", "part": "살",
  "content": "초록에 만새기 함량 값 없음[@opa]",
  "method": "HPLC-FLD(OPA 전처리 유도체화)",
  "conditions": {"instrument": "", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "",
                 "injection": "", "sample_prep": "", "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "히스티딘·라이신·오르니틴은 각각 히스타민·카다베린·푸트레신의 전구체여서 생선 품질·안전 지표로 쓰인다[@opa]. 초록 기준으로 75% 메탄올 추출, Ultrasphere ODS 칼럼·형광검출, 최소 검출농도 히스티딘·라이신 40 pmol/mL, 평균 회수율 히스티딘 93%였다[@opa]. 전문 확인 못함 — 조건 칸은 비워 둠.",
  "src": ["opa"], "url": "https://doi.org/10.1021/jf990032+", "source_kind": "paper"},
]

# ---- 번호 매기기
order = []
KEYRE = re.compile(r"\[(@[^\]]+)\]")


def use(k):
    if k not in S:
        raise KeyError(k)
    if k not in order:
        order.append(k)
    return order.index(k) + 1


def conv(text):
    def rep(m):
        keys = [x.strip().lstrip("@") for x in m.group(1).split(",")]
        return "[" + ", ".join(str(use(k)) for k in keys) + "]"
    return KEYRE.sub(rep, text)


secs = [{"key": k, "title": t, "body": conv(b)} for k, t, b in sections]
comps = []
for c in compounds:
    ct, ak = conv(c["content_text"]), conv(c["activity_ko"])
    comps.append({"name": c["name"], "name_ko": c["name_ko"], "class": c["class_"], "role": c["role"], "part": c["part"],
                  "content_text": ct, "activity_ko": ak, "source": sorted({use(k) for k in c["src"]})})
asy = []
for a in assays:
    a = dict(a)
    a["content"] = conv(a["content"]); a["rationale"] = conv(a["rationale"])
    a["source"] = sorted({use(k) for k in a.pop("src")})
    asy.append({k: a[k] for k in ("role", "compound", "compound_ko", "part", "content", "method", "conditions", "rationale", "source", "url", "source_kind")})

unused = [k for k in S if k not in order]
if unused:
    print("쓰지 않은 출처(제외):", unused)
sources = [{"n": i + 1, **S[k]} for i, k in enumerate(order)]

d = {"slug": "coryphaena-hippurus", "name_ko": "만새기", "name_en": "Common dolphinfish",
     "scientific_name": "Coryphaena hippurus Linnaeus, 1758",
     "aliases": ["만새기", "Common dolphinfish", "dolphinfish", "mahi-mahi"],
     "sections": secs, "compounds": comps, "markers": [], "assays": asy, "nutrients": [],
     "production": [], "world": [], "gi": [], "orgs": [], "sources": sources}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in secs:
    print(s["key"], len(s["body"]))
print("sources", len(sources), "compounds", len(comps), "assays", len(asy))
