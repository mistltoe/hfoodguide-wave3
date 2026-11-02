import json
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "dossier.json"
ACC = "2026-11-02"

S = [
    # n, title, url, publisher
    ("식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — '코토니' 두 행: 학명 Eucheuma cottonii(분류 식물, 사용가능, 사용 조건 '사용가능부위 : 전체')와 Kappaphycus alvarezii (Doty) Dotyex P.C. Silva.(분류 수산물, 별칭 카파피쿠스 알바레지아이, 영명 Cottonii, 사용가능, '사용가능부위 : 전체'); 같은 목록의 '스피노숨'(Eucheuma denticulatum / Eucheuma spinosum) 행과 식품첨가물(B코드) '카라기난' 행 (로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json)",
     "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "식품의약품안전처", "2026-10-13"),
    ("Re-evaluation of carrageenan (E 407) and processed Eucheuma seaweed (E 407a) as food additives. EFSA Journal 2018;16(4):e05238 (전문)",
     "https://doi.org/10.2903/j.efsa.2018.5238", "EFSA Journal, 유럽식품안전청 식품첨가물 패널 (PubMed 32625873, PMC7009739)", ACC),
    ("Carrageenans. 8. Repeating structures of galactan sulphates from Furcellaria fastigiata, … Eucheuma cottonii, Eucheuma spinosum, …. J Chem Soc Perkin 1 1973;19:2177-82 (서지 정보만; 초록 없음)",
     "https://doi.org/10.1039/p19730002177", "Journal of the Chemical Society, Perkin Transactions 1 (PubMed 4796666)", ACC),
    ("Carrageenans. VII. Polysaccharides from Eucheuma spinosum and Eucheuma cottonii. The covalent structure of iota-carrageenan. J Chem Soc Perkin 1 1973;19:2173-6 (서지 정보만; 초록 없음)",
     "https://doi.org/10.1039/p19730002173", "Journal of the Chemical Society, Perkin Transactions 1 (PubMed 4796665)", ACC),
    ("Anaerobic Degradation of Carrageenan from the Red Macroalga Eucheuma cottonii. Appl Environ Microbiol 1985;49(3):588-92 (초록)",
     "https://doi.org/10.1128/aem.49.3.588-592.1985", "Applied and Environmental Microbiology (PubMed 16346752, PMC373554)", ACC),
    ("Comparison of cardiovascular protective effects of tropical seaweeds, Kappaphycus alvarezii, Caulerpa lentillifera, and Sargassum polycystum, on high-cholesterol/high-fat diet in rats. J Med Food 2010;13(4):792-800 (초록)",
     "https://doi.org/10.1089/jmf.2008.1212", "Journal of Medicinal Food (PubMed 20482284)", ACC),
    ("Changes in rats' breast tumor ultrastructure and immune and messenger RNA responses caused by dietary seaweed (Eucheuma cottonii) extract. J Microsc Ultrastruct 2017;5(2):70-81 (전문; 추출본에서 학명 이탤릭이 빠짐)",
     "https://doi.org/10.1016/j.jmau.2016.08.001", "Journal of Microscopy and Ultrastructure (PubMed 30023239, PMC6025758)", ACC),
    ("Comparison of tamoxifen with edible seaweed (Eucheuma cottonii L.) extract in suppressing breast tumor. Nutr Cancer 2013;65(2):255-62 (초록)",
     "https://doi.org/10.1080/01635581.2013.756528", "Nutrition and Cancer (PubMed 23441613)", ACC),
    ("Dietary polysaccharide-rich extract from Eucheuma cottonii modulates the inflammatory response and suppresses colonic injury on dextran sulfate sodium-induced colitis in mice. PLoS One 2018;13(10):e0205252 (전문; 추출본에서 학명 이탤릭이 빠짐)",
     "https://doi.org/10.1371/journal.pone.0205252", "PLoS ONE (PubMed 30289911, PMC6173412)", ACC),
    ("A dietary polysaccharide from Eucheuma cottonii downregulates proinflammatory cytokines and ameliorates osteoarthritis-associated cartilage degradation in obese rats. Food Funct 2019 (초록)",
     "https://doi.org/10.1039/c9fo01342c", "Food & Function (PubMed 31435629)", ACC),
    ("Eucheuma cottonii Sulfated Oligosaccharides Decrease Food Allergic Responses in Animal Models by Up-regulating Regulatory T (Treg) Cells. J Agric Food Chem 2017;65(15):3212-22 (초록)",
     "https://doi.org/10.1021/acs.jafc.7b00389", "Journal of Agricultural and Food Chemistry (PubMed 28359154)", ACC),
    ("Effects of Alkaline Solvent Type and pH on Solid Physical Properties of Carrageenan from Eucheuma cottonii. Gels 2023;9(5):397 (전문; 추출본에서 학명 이탤릭이 빠졌으며 PubMed 검색어 \"Eucheuma cottonii\"[tiab]로 찾음)",
     "https://doi.org/10.3390/gels9050397", "Gels (PubMed 37232989, PMC10217466)", ACC),
    ("Antioxidant Peptides From Protein Hydrolysate of Marine Red Algae Eucheuma cottonii: Preparation, Identification, and Cytoprotective Mechanisms on H2O2 Oxidative Damaged HUVECs. Front Microbiol 2022;13:791248 (전문; 추출본에서 학명 이탤릭이 빠졌으며 PubMed 검색어 \"Eucheuma cottonii\"[tiab]로 찾음)",
     "https://doi.org/10.3389/fmicb.2022.791248", "Frontiers in Microbiology (PubMed 35531284, PMC9069057)", ACC),
    ("Potential of seaweed (Eucheuma cottonii) supplementation to reduce methane production, improve fermentation, and modulate the microbial composition of forages and crop by-products during in vitro rumen fermentation. Front Vet Sci 2025;12:1607879 (전문; 추출본에서 학명 이탤릭이 일부 빠짐)",
     "https://doi.org/10.3389/fvets.2025.1607879", "Frontiers in Veterinary Science (PubMed 41064259, PMC12501642)", ACC),
    ("The effectiveness of dried seaweed Eucheuma cottonii on in vitro rumen fermentation and enteric methane production. Braz J Biol 2024;84:e286929 (초록)",
     "https://doi.org/10.1590/1519-6984.286929", "Brazilian Journal of Biology (PubMed 39570159)", ACC),
    ("Phenotypic and mtDNA variation in Philippine Kappaphycus cottonii (Gigartinales, Rhodophyta). Mitochondrial DNA A 2018;29(6):951-963 (초록)",
     "https://doi.org/10.1080/24701394.2017.1398745", "Mitochondrial DNA Part A (PubMed 29117751)", ACC),
    ("Assessment of four molecular markers as potential DNA barcodes for red algae Kappaphycus Doty and Eucheuma J. Agardh (Solieriaceae, Rhodophyta). PLoS One 2012;7(12):e52905 (전문; 추출본에서 학명 이탤릭이 빠짐)",
     "https://doi.org/10.1371/journal.pone.0052905", "PLoS ONE (PubMed 23285223, PMC3527623)", ACC),
    ("Mitochondrial phylogenomics of eucheumatoids (Solieriaceae, Rhodophyta) from the Indo-Pacific. J Appl Phycol 2026;38(2):1771-1782 (전문; 추출본에서 학명 이탤릭이 빠짐)",
     "https://doi.org/10.1007/s10811-026-03784-1", "Journal of Applied Phycology (PubMed 42110568, PMC13156119)", ACC),
    ("Contrasting plastid and mitochondrial genome evolution in the Solieriaceae (Rhodophyta) reveals lineage-specific plastid gene loss in Kappaphycus. Mol Phylogenet Evol 2026;224:108688 (초록)",
     "https://doi.org/10.1016/j.ympev.2026.108688", "Molecular Phylogenetics and Evolution (PubMed 42425252)", ACC),
    ("The complete mitochondrial genome of a wild-collected Kappaphycus malesianus (Solieriaceae, Rhodophyta). Mitochondrial DNA B Resour 2023;8(3):359-363 (전문; 표 1의 K. alvarezii 비교값 인용)",
     "https://doi.org/10.1080/23802359.2023.2183728", "Mitochondrial DNA Part B (PubMed 36926639, PMC10013388)", ACC),
    ("In silico discovery and anti-tumor bioactivities validation of an algal lectin from Kappaphycus alvarezii genome. Int J Biol Macromol 2024;275:133311 (초록)",
     "https://doi.org/10.1016/j.ijbiomac.2024.133311", "International Journal of Biological Macromolecules (PubMed 38909728)", ACC),
    ("Iodine identification in major edible seaweed Kappaphycus alvarezii and establishment of an iodine reduction method for its protein extract for utilization as a protein source. Food Chem 2024;460:140723 (초록)",
     "https://doi.org/10.1016/j.foodchem.2024.140723", "Food Chemistry (PubMed 39128366)", ACC),
    ("Bioaccessibility of toxic heavy metals/metalloids in edible seaweeds: Exposure and health risk assessment. Food Res Int 2024;182:114135 (초록)",
     "https://doi.org/10.1016/j.foodres.2024.114135", "Food Research International (PubMed 38519158)", ACC),
    ("The properties of red seaweed (Kappaphycus alvarezii) and its effect on mammary carcinogenesis. Biomed Pharmacother 2017;87:296-301 (초록)",
     "https://doi.org/10.1016/j.biopha.2016.12.092", "Biomedicine & Pharmacotherapy (PubMed 28063411)", ACC),
    ("Plantlet Regeneration from Callus Cultures of Kappaphycus alvarezii for Cultivation in Coastal Waters at Myeik Archipelago, Myanmar. Pak J Biol Sci 2024;27(9):479-486 (초록)",
     "https://doi.org/10.3923/pjbs.2024.479.486", "Pakistan Journal of Biological Sciences (PubMed 39415556)", ACC),
    ("Dataset of a complete genome sequence of Vibrio owensii v2 isolated from diseased Sabah's red algae seaweed. Data Brief 2025;59:111447 (초록; 추출본에서 해조 학명이 빠짐)",
     "https://doi.org/10.1016/j.dib.2025.111447", "Data in Brief (PubMed 40160521, PMC11951041)", ACC),
    ("Non-starch polysaccharides extracted from seaweed can modulate intestinal absorption of glucose and insulin response in the pig. Reprod Nutr Dev 2000;40(1):33-47 (초록)",
     "https://doi.org/10.1051/rnd:2000118", "Reproduction, Nutrition, Development (PubMed 10737549)", ACC),
    ("The Potency of Red Seaweed (Eucheuma cottonii) Extracts as Hepatoprotector on Lead Acetate-induced Hepatotoxicity in Mice. Pharmacognosy Res 2017;9(3):282-286 (초록)",
     "https://doi.org/10.4103/pr.pr_69_16", "Pharmacognosy Research (PubMed 28827971, PMC5541486)", ACC),
    ("In vitro evaluation of antioxidant and antibacterial activities of Eucheuma cottonii extract and its in vivo evaluation of the wound-healing activity in mice. J Cosmet Dermatol 2020 (초록)",
     "https://doi.org/10.1111/jocd.13624", "Journal of Cosmetic Dermatology (PubMed 32659861)", ACC),
    ("Effects of plasticizers on the physicochemical properties of kappa-carrageenan films extracted from Eucheuma cottonii. Int J Biol Macromol 2017;103:721-732 (초록)",
     "https://doi.org/10.1016/j.ijbiomac.2017.05.105", "International Journal of Biological Macromolecules (PubMed 28528954)", ACC),
    ("Disk-shaped cellulose fibers from red algae, Eucheuma cottonii and its use for high oxygen barrier. Int J Biol Macromol 2022 (초록)",
     "https://doi.org/10.1016/j.ijbiomac.2022.04.232", "International Journal of Biological Macromolecules (PubMed 35523360)", ACC),
    ("Ultrasonic-assisted molten salt hydrates pretreated Eucheuma cottonii residues as a greener precursor for third-generation L-lactic acid production. Bioresour Technol 2022 (초록)",
     "https://doi.org/10.1016/j.biortech.2022.128136", "Bioresource Technology (PubMed 36257523)", ACC),
    ("Valorization of Kappaphycus alvarezii through extraction of high-value compounds employing green approaches and assessment of the therapeutic potential of κ-carrageenan. Int J Biol Macromol 2023;250:126230 (초록)",
     "https://doi.org/10.1016/j.ijbiomac.2023.126230", "International Journal of Biological Macromolecules (PubMed 37558033)", ACC),
    ("The Effects of Eucheuma cottonii on Signaling Pathway Inducing Mucin Synthesis in Rat Lungs Chronically Exposed to Particulate Matter 10 (PM10) Coal Dust. J Toxicol 2013;2013:528146 (초록)",
     "https://doi.org/10.1155/2013/528146", "Journal of Toxicology (PubMed 24228027, PMC3817679)", ACC),
]

sections = [
 ("overview", "한눈에 보기",
  "코토니(Eucheuma cottonii)는 동남아시아 열대 바다에서 기르는 κ-카라기난 원료 홍조류다[2, 5]. "
  "식약처 「식품원료 목록」에는 '코토니'가 두 행으로 올라 있는데, 하나는 학명 Eucheuma cottonii(분류 식물)이고 다른 하나는 Kappaphycus alvarezii(분류 수산물, 별칭 카파피쿠스 알바레지아이, 영명 Cottonii)다[1]. "
  "두 행 모두 상태는 '사용가능'이고 사용 조건은 '사용가능부위 : 전체'다[1]. "
  "카라기난은 같은 목록에 식품첨가물(B코드)로 따로 올라 있고, 건강기능식품 고시형 원료 표시는 없다[1].\n\n"
  "유럽식품안전청(EFSA)의 카라기난 재평가 표에는 E. cottonii가 카라기난(E 407)과 가공 유케마 해조(E 407a)의 원료이고 주된 카라기난형이 κ로 적혀 있다[2]. "
  "효능 연구는 추출물을 쓴 세포·동물 실험이 대부분이며, 사람 대상 임상시험은 확인하지 못함. "
  "동물 실험에서 다당류가 많은 추출물은 대장염 생쥐의 염증성 사이토카인과 대장 손상을 줄였고, 비만 골관절염 쥐의 연골 손상 지표를 낮췄다[9, 10]. "
  "납 투여 생쥐에서는 에탄올 추출물 800 mg/kg에서만 간 효소 상승이 억제되었다[28]. "
  "석탄 분진에 노출된 쥐에서 에탄올 추출물 300 mg/kg은 폐의 말론디알데히드를 낮췄고, 수용성 추출물 겔(10%)은 생쥐 피부 상처의 수축을 빠르게 했다[29, 34]. "
  "말린 E. cottonii를 건물 기준 4%까지 넣은 반추위 시험관 발효에서는 메탄 생성이 줄었다[15]. "
  "이는 사람에게 같은 효과가 있다는 근거가 아니다[9, 10, 28]."),
 ("history", "이용 역사",
  "1973년 발표된 카라기난 구조 연구들은 E. spinosum과 E. cottonii의 다당류를 비교했고, 여러 홍조류 갈락탄의 반복 구조를 다룬 논문에도 E. cottonii가 포함되었다[3, 4]. "
  "1985년 미국 연구는 E. cottonii 생물량의 61%가 카라기난이었다고 보고하고, 혐기 소화로 메탄과 하이드로콜로이드를 함께 얻는 방식은 경제성이 없다고 결론지었다[5]. "
  "EFSA 보고서는 가공 유케마 해조(E 407a)가 '필리핀 천연 등급(PNG) 카라기난', '반정제 카라기난(SRC)'이라는 이름으로도 불린다고 적었다[2].\n\n"
  "미얀마에서는 2004년부터 메익 군도에서 K. alvarezii 양식이 시작되었는데, 자생종이 아니어서 필리핀·인도네시아에서 들여왔다[25]. "
  "말레이시아 연구진은 이 해조를 '열대의 식용 홍조류'로 소개하며 사바에서 연중 재배한 원료로 실험했다[7, 8]. "
  "우리나라에서 이 해조를 식품으로 먹어 온 기록은 확인하지 못함."),
 ("biology", "생물학적 특징·생태",
  "코토니는 돌가사리목(Gigartinales) 솔리에리아과(Solieriaceae)에 속하는 이른바 유케마류(eucheumatoids) 홍조류다[16, 19]. "
  "유케마류는 겉모습이 환경에 따라 크게 달라 형태만으로 종을 가리기 어렵고, 상업명과 지역명이 뒤섞여 쓰여 혼란이 크다[18]. "
  "필리핀 Kappaphycus cottonii 연구에서는 여섯 가지 겉모습 유형이 유전 변이와 맞지 않아, 형태는 환경 요인의 영향을 크게 받는 것으로 해석되었다[16].\n\n"
  "말레이시아 사바의 재배 원료는 심은 뒤 45일에 거두며, 적도 해역이라 계절 구분 없이 일 년 내내 기른다[7]. "
  "세포벽의 주된 다당류는 κ-카라기난이며, 1985년 분석에서 원래 생물량의 61%가 카라기난이었고 평균 분자량은 510,000이었다[2, 5]. "
  "카라기난을 뽑고 남은 잔사를 표백하면 대부분 포도당으로 이루어지고 결정화도가 50% 이상인 셀룰로스 I형 원판 모양 섬유가 얻어진다[31]. "
  "사바의 카라기난 원료 홍조류 양식장에서는 병든 엽상체에서 Vibrio owensii가 분리되었고, 이 세균은 수확량과 품질을 떨어뜨리는 기회감염 병원체로 소개되었다[26]."),
 ("related_species", "근연종·혼동 주의",
  "'코토니'라는 이름은 한 종에만 쓰이지 않는다[1, 16]. "
  "식약처 목록은 같은 국문명 '코토니' 아래 Eucheuma cottonii와 Kappaphycus alvarezii를 따로 올려 두고, 후자의 영명을 Cottonii로 적었다[1]. "
  "학술 문헌에서도 'Kappaphycus alvarezii(또는 Eucheuma cottonii)'처럼 두 이름을 같은 해조에 함께 쓰거나, 실험에 쓴 E. cottonii를 KA라는 약칭으로도 부른다고 적은 예가 있다[6, 9]. "
"\n\n"
  "반면 Kappaphycus cottonii라는 종은 mtDNA(COI-5P, cox2-3 간격 부위) 분석에서 K. alvarezii·K. inermis·K. malesianus·K. striatus 네 종과 갈라진 별도 계통을 이루었고, 엽상체가 완전한 원통형이 아니며 돌기가 있고 중심부 균사가 없다는 점에서도 달랐다[16]. "
  "그러므로 논문 속 'E. cottonii'가 재배 품종인지 야생 K. cottonii인지는 원문의 시료 출처로 확인해야 하며, 학명의 명명 이력은 공식 분류 데이터베이스에서 확인하지 못함. "
  "EFSA 표에서 E. cottonii는 κ형, E. spinosum은 ι형 카라기난 원료로 구분되며, 식약처 목록에서 E. spinosum은 별도 원료 '스피노숨'(E. denticulatum)의 이명이다[1, 2]. "
  "엽록체 유전체 비교에서 pbsA·ycf57 유전자는 K. alvarezii·K. striatus에는 없고 E. denticulatum에는 있었다[19]."),
 ("cultivation", "양식·산지",
  "인도네시아와 필리핀은 카라기난 원료 해조의 최대 생산국이며, 이 해조들은 'cottonii'와 'spinosum'이라는 상업명으로 거래된다[17, 18]. "
  "유케마류 양식은 개발도상국 연안 마을의 생계 수단이지만, 최근 업계에서는 생장 저하·수확 감소·카라기난 품질 저하·병해충 증가가 보고되고 있다[18].\n\n"
  "인도네시아 반텐주 세랑의 양식장에서는 심은 지 45일 된 E. cottonii를 건기(2021년 7월)에 거두어 연구에 썼다[14]. "
  "미얀마에서는 종묘를 안정적으로 대기 위해 K. alvarezii 캘러스 조직배양으로 소식물체를 만들었고, 이 소식물체의 하루 평균 생장률은 9.70±0.25%였다[25]. "
  "배양 조건은 22–25 °C, 12시간 명암 주기, pH 8, 염분 30 PSU였다[25]. "
  "국내 양식·생산 통계는 확인하지 못함. "
  "세계 생산량은 FAO 통계를 이번 조사에서 열어 보지 못해 확인하지 못함."),
 ("processing", "가공·제품",
  "상업적으로 이 해조는 말려서 정제 카라기난(E 407)을 뽑거나, 알칼리로만 처리한 가공 유케마 해조(E 407a)로 만든다[2]. "
  "EU 규격에서 E 407a는 해조를 고온의 수산화칼륨 수용액으로 처리한 뒤 민물로 씻고 말린 것이며, 알코올 세척은 메탄올·에탄올·2-프로판올만 허용된다[2]. "
  "E 407a에는 조류 셀룰로스가 15%까지 들어 있을 수 있고 포름알데히드는 5 mg/kg 이하여야 한다[2].\n\n"
  "인도네시아 술라웨시산 E. cottonii를 NaOH·KOH·Ca(OH)2 용액(pH 9·11·13, 80 °C, 3시간)으로 추출한 실험에서 모든 시료가 FAO 규격을 충족했고, KOH pH 13 추출물은 분자량 289.80 kDa, 황산기 20.64%였다[12]. "
  "E. cottonii에서 뽑은 κ-카라기난 필름은 소르비톨을 가소제로 넣었을 때 수증기 투과도가 가장 낮았다[30]. "
  "카라기난을 뽑고 남은 잔사는 산소 차단 셀룰로스 섬유, 젖산 발효 원료 등으로 연구되었다[31, 32]. "
  "식약처 「식품 등의 생산실적」에서 코토니를 원료로 한 제품 생산실적은 확인하지 못함."),
 ("genetics", "유전·유전체",
  "E. cottonii라는 학명으로 해독된 핵 유전체는 확인하지 못함. "
  "같은 국문명 아래 묶인 K. alvarezii의 미토콘드리아 유전체는 25,198 bp, GC 함량 29.86%, 유전자 50개(단백질 24, tRNA 24, rRNA 2)로 보고되었다[20]. "
  "2026년 연구는 인도·태평양 유케마류의 완전한 미토콘드리아 유전체 26개를 해독해 크기가 25.1–25.5 kb이고 유전자 배열이 매우 잘 보존되어 있음을 보였다[18]. "
  "이 연구에는 상업 'cottonii' 품종과 비교한 동남아 야생 유전형이 포함되었다[18].\n\n"
  "엽록체 단백질 유전자 197개를 이어 붙인 계통 분석은 cox1·rbcL 같은 단일 표지보다 해상도가 높았고, K. alvarezii에서 pbsA·ycf57 유전자 소실이 처음 함께 확인되었다[19]. "
  "DNA 바코드 비교에서는 cox2 표지가 종 안 변이 없이 종 사이 차이를 보였으나, 전체적으로는 cox2-3 간격 부위가 더 적합하다고 평가되었다[17]. "
  "필리핀 K. cottonii는 지금까지 Kappaphycus 종 가운데 가장 많은 일배체형을 보였다[16]. "
  "K. alvarezii 유전체에서는 새 렉틴 'Siye'가 찾아졌고, 사람 암세포 4종에 IC50 0.11–3.95 μg/mL의 세포독성을 보였다[21]."),
 ("safety", "안전성·주의",
  "식약처 목록에서 코토니(두 행 모두)는 '사용가능' 원료이고 사용 조건은 '사용가능부위 : 전체'다[1]. "
  "국내 공공기관의 코토니 알레르기·잔류물질·중금속 정보는 확인하지 못함.\n\n"
  "카라기난 일반에 대한 평가로, EFSA는 2018년 카라기난(E 407)과 가공 유케마 해조(E 407a)를 함께 재평가해 기존 그룹 1일섭취허용량 75 mg/kg 체중/일을 '잠정'으로 두고, 저분자량 분획을 정량할 검증된 분석법을 요구했다[2]. "
  "EFSA는 노출 추정이 일부 집단의 95백분위에서 잠정 허용량을 최대 약 10배 넘어 안전 우려가 될 수 있다고 보았다[2]. "
  "JECFA는 2015년 영아용 조제식에 카라기난을 1,000 mg/L까지 쓰는 것은 우려가 없다고 결론지었다[2]. "
  "이들은 식품첨가물 규격 카라기난·가공 해조에 대한 평가이며, 코토니 해조 자체를 먹는 경우를 평가한 것이 아니다[2].\n\n"
  "이 종 자체 자료로는, 말레이시아산 메탄올 추출물이 쥐에서 150 mg/kg 체중에서 독성을 보이지 않았다는 보고가 있다[7]. "
  "K. alvarezii로 표기된 추출물을 쥐에 2000 mg/kg 체중씩 아만성 투여한 시험에서 혈액·생화학 값의 유의한 차이는 없었다[24]. "
  "K. alvarezii의 요오드는 거의 모두 요오드화 단백질 형태로 들어 있었다[22]. "
  "인도 연안의 K. alvarezii 등 식용 해조 3종의 중금속은 EC·WHO/FAO 권고치보다 낮았고, 표적위해지수(TTHQ)는 1 미만이었다[23]."),
]

compounds = [
 dict(name="kappa-Carrageenan", name_ko="카파(κ)-카라기난", cls="황산화 갈락탄 다당류", role="marker", part="엽상체 전체(건조)",
      content_text="원래 생물량의 61%(혐기 소화 10주 뒤 남은 생물량에서는 51%), 평균 분자량 510,000[5]; KOH pH 13 추출 카라기난 분자량 289.80 kDa[12]",
      activity_ko="겔화·증점 식품첨가물(E 407·E 407a)의 주성분[2]; 가소제를 넣은 포장 필름 소재[30]", source=[2, 5, 12, 30]),
 dict(name="3,6-Anhydro-D-galactose", name_ko="3,6-안하이드로갈락토스", cls="카라기난 구성 단당", role="marker", part="엽상체 70% 에탄올 추출물",
      content_text="약 43.74 ± 6.30 μmol/L(레조르시놀법, 추출물 시험액 기준)[9]; K. alvarezii 초임계 추출 잔사의 κ-카라기난에서 약 24%[33]",
      activity_ko="κ-카라기난 반복 단위의 구성당으로 겔 형성에 관여[2, 9]", source=[2, 9, 33]),
 dict(name="Galactose", name_ko="갈락토스", cls="단당류", role="marker", part="엽상체 κ-카라기난(K. alvarezii 표기)",
      content_text="약 53%(초음파 보조 회수 κ-카라기난, 황산기 28.5 ± 1.9%)[33]",
      activity_ko="카라기난 골격의 주 구성당[2, 33]", source=[2, 33]),
 dict(name="Sulfate", name_ko="황산기(카라기난 황산 에스터)", cls="음이온성 작용기", role="marker", part="알칼리 추출 카라기난",
      content_text="KOH pH 13 20.64%, NaOH pH 9 23.43%, Ca(OH)2 pH 13 21.72%[12]",
      activity_ko="점도·팽윤성에 관여하며 FTIR 1218–1223 cm⁻¹(S=O)에서 확인[12]", source=[12]),
 dict(name="Cellulose", name_ko="셀룰로스", cls="구조 다당류", role="bioactive", part="카라기난 추출 잔사",
      content_text="함량 수치는 초록에 없음; 표백 섬유는 대부분 포도당이고 결정화도 50% 이상(셀룰로스 I형)[31]; E 407a에는 조류 셀룰로스가 최대 15%[2]",
      activity_ko="두께 100 nm 미만의 원판형 섬유로 투명·산소 차단 막 소재 연구[31]", source=[2, 31]),
 dict(name="Protein", name_ko="조단백질", cls="영양 성분", role="nutrient", part="엽상체 건조물",
      content_text="84.2 g/kg DM(인도네시아 세랑, 45일 재배)[14]; 9.76 ± 1.33% dw(선행연구 인용값), 수용성 조단백 추출 수율 10.77 ± 0.42%[13]",
      activity_ko="효소 가수분해로 항산화 펩타이드 원료[13]", source=[13, 14]),
 dict(name="Tyr-Leu-Leu", name_ko="항산화 펩타이드 YLL(EP5)", cls="트리펩타이드", role="bioactive", part="조단백 파파인 가수분해물",
      content_text="분자량 407.51 Da, DPPH EC50 0.52 ± 0.19 mM[13]",
      activity_ko="H2O2로 손상시킨 사람 제대정맥 내피세포에서 ROS·MDA 감소(세포 실험)[13]", source=[13]),
 dict(name="Tyr-Ala-Val-Thr", name_ko="항산화 펩타이드 YAVT(EP4)", cls="테트라펩타이드", role="bioactive", part="조단백 파파인 가수분해물",
      content_text="분자량 452.51 Da, 수산기 라디칼 EC50 1.24 ± 0.10 mM, 초과산화 음이온 EC50 0.56 ± 0.16 mM[13]",
      activity_ko="세포 실험에서 산화 손상 내피세포의 세포자멸 비율 감소[13]", source=[13]),
 dict(name="Dietary fiber", name_ko="식이섬유", cls="탄수화물", role="nutrient", part="엽상체 건조물",
      content_text="26.49 ± 3.01% dw, 탄수화물 25.05 ± 0.99% dw(선행연구 인용값)[13]; NDF 116.9 g/kg DM, ADF 117.7 g/kg DM[14]",
      activity_ko="돼지 실험에서 E. cottonii 섬유 5% 첨가 시 인슐린 반응 감소, 포도당 흡수량은 변화 없음[27]", source=[13, 14, 27]),
 dict(name="Calcium", name_ko="칼슘", cls="무기질", role="nutrient", part="엽상체 건조물",
      content_text="0.5 g/kg DM(인으로도 0.5 g/kg DM), 유기물 599.2 g/kg DM[14]",
      activity_ko="사료 원료 영양 평가 지표[14]", source=[14]),
 dict(name="Gallic acid", name_ko="총 페놀(갈산 당량)", cls="페놀 화합물 지표", role="bioactive", part="엽상체 50% 메탄올 추출물",
      content_text="건조 시료 100(단위 기호는 추출본에서 빠짐)당 총페놀 49 mg 갈산 당량, 총플라보노이드 15 mg 카테킨 당량, 추출 수율 10.1%[7]",
      activity_ko="쥐 유방종양 모델에서 항산화 지표 개선(동물 실험)[7, 8]", source=[7, 8]),
 dict(name="Iodine", name_ko="요오드", cls="미량 원소", role="nutrient", part="엽상체 알칼리 추출물(K. alvarezii 표기)",
      content_text="함량 수치는 초록에 없음; 알칼리 추출물의 요오드는 거의 모두 요오드화 단백질 형태[22]",
      activity_ko="단백질 원료로 쓸 때 요오드를 줄이는 처리로 단백질당 요오드를 약 절반으로 줄임[22]", source=[22]),
 dict(name="Carrageenan oligosaccharide", name_ko="코토니 황산화 올리고당(ESO)", cls="황산화 올리고당", role="bioactive", part="효소 분해 카라기난",
      content_text="함량 수치 없음; 효소 분해·칼럼 정제로 제조[11]",
      activity_ko="생쥐 식품알레르기 모델에서 특이 IgE 77.7% 억제, Treg 세포 22.2–97.1% 증가(동물 실험)[11]", source=[11]),
 dict(name="Lectin", name_ko="렉틴", cls="탄수화물 결합 단백질", role="bioactive", part="50% 메탄올 추출물; K. alvarezii 유전체",
      content_text="함량 수치 없음; FTIR로 추출물의 주 활성 성분을 렉틴 펩타이드로 추정[7]",
      activity_ko="유전체에서 찾은 렉틴 Siye는 사람 암세포 4종에 IC50 0.11–3.95 μg/mL(세포 실험)[21]", source=[7, 21]),
]

assays = [
 {"role": "literature", "compound": "3,6-Anhydro-D-galactose", "compound_ko": "3,6-안하이드로갈락토스",
  "part": "엽상체 건조 분말의 70% 에탄올 추출물(말레이시아 사바산)",
  "content": "약 43.74 ± 6.30 μmol/L; 추출 수율 17.79 ± 0.09%[9]",
  "method": "레조르시놀 비색법(마이크로플레이트)",
  "conditions": {"instrument": "마이크로플레이트 흡광도 측정기", "column": "", "mobile_phase": "", "gradient": "", "flow": "",
                 "temp": "얼음물 3분 혼합 후 80 °C 수욕 10분 발색", "detection": "520 nm",
                 "injection": "96웰 마이크로플레이트",
                 "sample_prep": "건조 분말 40 g + 70% 에탄올 200 mL, 50 °C 3시간 교반 추출을 3회 반복; 감압농축(40 °C) 후 동결건조",
                 "standard": "D-프럭토스 250 μmol/L(용액의 55%를 같은 몰의 3,6-안하이드로-α-D-갈락토피라노사이드로 환산)",
                 "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "3,6-안하이드로갈락토스는 κ-카라기난 반복 단위의 구성당으로 이 종의 다당류 함량을 보는 지표로 쓰였다; 전문 확인[9].",
  "source": [9], "url": "https://doi.org/10.1371/journal.pone.0205252", "source_kind": "paper"},
 {"role": "literature", "compound": "kappa-Carrageenan (sulfate content, molecular weight)", "compound_ko": "κ-카라기난(황산기·분자량)",
  "part": "엽상체 건조물(인도네시아 술라웨시산)의 알칼리 추출 카라기난",
  "content": "황산기 20.64%(KOH pH 13)·23.43%(NaOH pH 9)·21.72%(Ca(OH)2 pH 13); 분자량 289.80·170.58·71.79 kDa[12]",
  "method": "FAO 규격 항목 시험(황산기·회분·점도·겔 강도), 고유점도법 분자량, ATR-FTIR",
  "conditions": {"instrument": "ATR-FTIR 분광기(ZnSe ATR 셀)", "column": "", "mobile_phase": "", "gradient": "", "flow": "",
                 "temp": "추출 80 °C", "detection": "FTIR 흡수대: S=O 1218–1223 cm⁻¹, 3,6-안하이드로갈락토스 919–920 cm⁻¹, 갈락토스-4-황산 840–842 cm⁻¹",
                 "injection": "",
                 "sample_prep": "건조 해조 50 g을 1% 과산화수소·아세트산(pH 3.5) 1500 mL에 12시간 담금; 알칼리 용액(NaOH·KOH·Ca(OH)2, pH 9·11·13) 1500 mL, 80 °C, 150 rpm, 3시간 추출; 추출액 100 mL에 7.5% 황산칼륨 첨가 30분 교반, 뜨거울 때 여과, 8시간 상온 겔화, 압착·50 °C 15–20시간 건조, 80메시 분쇄",
                 "standard": "κ-카라기난 표준품(시판 시약)",
                 "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "황산기 함량과 분자량은 카라기난의 FAO 식품첨가물 규격·물성 판정 항목이다; 전문 확인했으나 황산기·겔 강도·점도 시험 조건은 인용 논문을 따른다고만 적혀 있어 비움[12].",
  "source": [12], "url": "https://doi.org/10.3390/gels9050397", "source_kind": "paper"},
 {"role": "literature", "compound": "Antioxidant peptides (Tyr-Ala-Val-Thr, Tyr-Leu-Leu)", "compound_ko": "항산화 펩타이드(YAVT·YLL 등)",
  "part": "엽상체 분말의 수용성 단백질(황산암모늄 60% 침전 분획) 파파인 가수분해물",
  "content": "조단백 추출 수율 10.77 ± 0.42%, 60% 침전 분획 52.77 ± 1.42 g/100 g 조단백, 파파인 가수분해물 수율 36.31 ± 2.53 g/100 g[13]",
  "method": "역상 HPLC 분취 후 N-말단 서열분석·ESI-Q-TOF MS",
  "conditions": {"instrument": "HPLC 시스템(분취), 단백질 서열분석기, ESI-Q-TOF 질량분석기",
                 "column": "C18(SB), 4.6 mm × 250 mm, 5 μm(방법 절에는 4.6 mm × 25 mm로 적혀 있어 원문 표기가 엇갈림)",
                 "mobile_phase": "0.05% 트리플루오로아세트산 함유 아세토니트릴",
                 "gradient": "아세토니트릴 0–50%(0–30분) 선형",
                 "flow": "0.8 mL/min", "temp": "", "detection": "UV 214 nm, 280 nm", "injection": "",
                 "sample_prep": "분말:탈이온수 1:40(g/mL) 26 °C 12시간 교반 후 초음파(53 kHz, 100 W) 30분; 황산암모늄 10%·60% 포화 침전, 투석·동결건조; 파파인 1%(55 °C, pH 7) 4시간 가수분해; 1·3 kDa 한외여과; Sephadex G-25 겔여과(0.6 mL/min, 280 nm)",
                 "standard": "글루타티온(라디칼 소거 양성 대조)",
                 "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "단백질 가수분해 펩타이드를 분리·동정한 연구로 정량 분석법은 아니다; 원료는 시판 건조품이며 종 동정 방법은 적혀 있지 않음; 전문 확인[13].",
  "source": [13], "url": "https://doi.org/10.3389/fmicb.2022.791248", "source_kind": "paper"},
]

body_extra = []

sources = [{"n": i + 1, "title": t, "url": u, "publisher": p, "accessed": a} for i, (t, u, p, a) in enumerate(S)]

d = {
 "slug": "eucheuma-cottonii",
 "name_ko": "코토니",
 "name_en": "Cottonii (Eucheuma cottonii)",
 "scientific_name": "Eucheuma cottonii",
 "aliases": ["Cottonii", "Kappaphycus alvarezii (Doty) Doty ex P.C. Silva(식약처 목록에 같은 국문명으로 따로 오른 원료)", "카파피쿠스 알바레지아이"],
 "sections": [{"key": k, "title": t, "body": b} for k, t, b in sections],
 "compounds": [{"name": c["name"], "name_ko": c["name_ko"], "class": c["cls"], "role": c["role"], "part": c["part"],
                "content_text": c["content_text"], "activity_ko": c["activity_ko"], "source": c["source"]} for c in compounds],
 "markers": [],
 "assays": assays,
 "nutrients": [],
 "production": [],
 "gi": [],
 "orgs": [],
 "world": [],
 "sources": sources,
}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in d["sections"]:
    print(s["key"], len(s["body"]))
print(len(sources))
