import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
A = "2026-11-02"
P = "PubMed"
def pm(n, title, doi, extra):
    return {"n": n, "title": f"{title} — {extra}", "url": f"https://doi.org/{doi}" if doi else extra, "publisher": P, "accessed": A}
sources = [
 {"n": 1, "title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 타임잎세이보리잎(Satureja thymbra L.; Thyme-leaved savory), 식품원료(A코드), 사용가능, 사용가능부위: 잎; 같은 속 여름세이보리잎·건조여름세이보리(S. hortensis), 겨울세이보리잎(S. montana), Creeping savory잎(S. spicigera), Wild basil잎(S. vulgaris [Clinopodium vulgare]) 및 식품첨가물(B코드) 천연향료(Savory, summer)·천연향료(Savory, winter) 행 대조 (로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json)", "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
 pm(2, "A Nano-Based Approach to Deliver Satureja thymbra Essential Oil to the Skin: Formulation and Characterization", "10.3390/molecules29051041", "Molecules 2024;29(5):1041 (PMID 38474551, PMC10933724, 전문 확인)"),
 pm(3, "Nanovesicles Loaded with Origanum onites and Satureja thymbra Essential Oils and Their Activity against Food-Borne Pathogens and Spoilage Microorganisms", "10.3390/molecules26082124", "Molecules 2021;26(8):2124 (PMID 33917147, PMC8067826, 전문 확인)"),
 pm(4, "Antimicrobial and Antioxidant Activities of Essential Oils of Satureja thymbra Growing Wild in Libya", "10.3390/molecules17054836", "Molecules 2012;17(5):4836-50 (PMID 22538487, PMC6268410, 전문 확인)"),
 pm(5, "Altitude impact on the chemical profile and biological activities of Satureja thymbra L. essential oil", "10.1186/s12906-020-02982-9", "BMC Complement Med Ther 2020 (PMID 32532265, PMC7290070, 전문 확인)"),
 pm(6, "Anti-plasmodial and insecticidal activities of the essential oils of aromatic plants growing in the Mediterranean area", "10.1186/1475-2875-11-219", "Malar J 2012;11:219 (PMID 22747579, PMC3441327, 전문 확인)"),
 pm(7, "Essential oil composition is related to the natural habitats: Coridothymus capitatus and Satureja thymbra in NATURA 2000 sites of Crete", "10.1016/j.phytochem.2005.09.020", "Phytochemistry 2005;66(22):2668-73 (PMID 16289149, 초록 확인)"),
 pm(8, "Analysis of essential oil of Satureja thymbra by hydrodistillation, thermal desorber, and headspace GC/MS techniques and its antimicrobial activity", "10.1080/14786410310001608145", "Nat Prod Res 2004;18(2):189-95 (PMID 14984095, 초록 확인)"),
 {"n": 9, "title": "Isolation of the volatile oil from Satureja thymbra by supercritical carbon dioxide extraction: chemical composition and biological activity — Nat Prod Commun 2011;6(10):1523-6 (PMID 22164799, 초록 확인, DOI 없음)", "url": "https://pubmed.ncbi.nlm.nih.gov/22164799/", "publisher": P, "accessed": A},
 pm(10, "Characterization of the essential oil volatiles of Satureja thymbra and Satureja parnassica: influence of harvesting time and antimicrobial activity", "10.1021/jf053183n", "J Agric Food Chem 2006;54(8):3139-45 (PMID 16608243, 초록 확인)"),
 pm(11, "The effect of temperature on the phenolic content and oxidative stability of o/w emulsions enriched with natural extracts from Satureja thymbra", "10.1016/j.foodchem.2021.129206", "Food Chem 2021 (PMID 33578245, 초록 확인)"),
 pm(12, "Nutrient antioxidants in oregano", "10.3109/09637489609031878", "Int J Food Sci Nutr 1996;47(6):493-7 (PMID 8933203, 초록 확인)"),
 pm(13, "Fatty acid composition of seeds of Satureja thymbra and S. cuneifolia", "10.1515/znc-2003-7-810", "Z Naturforsch C 2003;58(7-8):502-4 (PMID 12939035, 초록 확인)"),
 pm(14, "An ethnobotanical study of medicinal plants in Marmaris (Muğla, Turkey)", "10.1016/j.jep.2012.12.012", "J Ethnopharmacol 146(1):113-26 (PMID 23261486, 초록 확인)"),
 pm(15, "In vitro haemostatic efficacy of aqueous, methanol and ethanol plant extracts of three medicinal plant species in Palestine", "10.1590/1519-6984.219186", "Braz J Biol 2020 (PMID 31800761, 초록 확인)"),
 pm(16, "In vitro inhibitory activities of plants used in Lebanon traditional medicine against angiotensin converting enzyme (ACE) and digestive enzymes related to diabetes", "10.1016/j.jep.2008.06.003", "J Ethnopharmacol 2008;119(1):109-16 (PMID 18601990, 초록 확인)"),
 pm(17, "Antioxidant and Antiproliferative Properties of the Essential Oils of Satureja thymbra and Satureja parnassica and their Major Constituents", "10.21873/anticanres.11159", "Anticancer Res 2016;36(11):5757 (PMID 27793897, 초록 확인)"),
 pm(18, "Plastome diversity and phylogenomic analysis of Satureja (Lamiaceae): uncovering evolutionary patterns and diagnostic markers", "10.1007/s00425-025-04875-y", "Planta 2025;262(6):149 (PMID 41204963, 초록 확인)"),
 pm(19, "Molecular phylogeny of Menthinae (Lamiaceae, Nepetoideae, Mentheae) — Taxonomy, biogeography and conflicts", "10.1016/j.ympev.2010.01.016", "Mol Phylogenet Evol 2010;55(2):501-23 (PMID 20152913, 초록 확인)"),
 pm(20, "Composition of Essential Oils of Thymbra spicata and Satureja thymbra Chemotypes", "10.1055/s-2007-969506", "Planta Med 1985;51(4):337-8 (PMID 17340528, 초록 확인)"),
 pm(21, "Effect of Satureja thymbra essential oil on growth-no growth interfaces of Listeria monocytogenes Scott A and Salmonella Enteritidis PT4, at various temperatures, pH, and water activities", "10.4315/0362-028X.JFP-10-077", "J Food Prot 2011;74(1):45-54 (PMID 21219762, 초록 확인)"),
 pm(22, "Disinfectant test against monoculture and mixed-culture biofilms ...: bactericidal effect of essential oil and hydrosol of Satureja thymbra and comparison with standard acid-base sanitizers", "10.1111/j.1365-2672.2007.03694.x", "J Appl Microbiol 2008;104(6):1586-96 (PMID 18217930, 초록 확인)"),
 pm(23, "Insecticidal activity of plant essential oils against the vine mealybug, Planococcus ficus", "10.1673/031.013.14201", "J Insect Sci 2013;13:142 (PMID 24766523, PMC4015406, 초록 확인)"),
 pm(24, "Anthocyanin copigmentation and color of wine: The effect of naturally obtained hydroxycinnamic acids as cofactors", "10.1016/j.foodchem.2015.10.095", "Food Chem 2015 온라인 (PMID 26616922, 초록 확인)"),
 pm(25, "Chemical Composition and Antimicrobial Activity of Satureja, Thymus, and Thymbra Species Grown in Lebanon", "10.1002/cbdv.201600236", "Chem Biodivers 2017 (PMID 27584022, 초록 확인)"),
]

S = {}
S["overview"] = ("한눈에 보기", """타임잎세이보리(Satureja thymbra L.)는 꿀풀과 세이보리속의 여러해살이 작은 관목으로, 동지중해에서 사르데냐에 이르는 지역에 자란다[2, 4]. 영어로는 thyme-leaved savory 라고 부르며[1, 23], 리비아 논문은 pink savory 라는 이름도 소개한다[5].

식약처 「식품원료 목록」에는 '타임잎세이보리잎' 한 행이 식품원료(A코드)로 올라 있고, 상태는 '사용가능', 사용 조건은 '사용가능부위 : 잎'이다[1]. 즉 국내에서 식품 원료로 쓸 수 있는 부위는 잎뿐이며, 씨앗·줄기·뿌리는 이 목록의 사용 부위에 들어 있지 않다[1]. 같은 목록의 식품첨가물(B코드) 천연향료 행은 여름세이보리와 겨울세이보리만 있고, 이 종의 천연향료 행은 찾지 못했다[1]. 건강기능식품 고시형 원료의 원재료로 등록된 기록은 확인하지 못함.

향의 중심은 정유의 페놀성 모노테르펜인 카르바크롤과 티몰이며, 산지에 따라 카르바크롤이 많은 형과 티몰이 많은 형이 따로 보고된다[7, 20]. 크레타 시료에서는 카르바크롤이 최대 75.7%, 티몰이 최대 65.6%까지 나왔다[7]. 추출물에서는 로즈마린산이 주성분으로 보고되었다[11]. 사람 대상 임상시험은 확인하지 못함.""")
S["history"] = ("역사와 전통적 이용", """사르데냐에서는 이 풀을 소화제·진경제·지사제·이뇨제·소독제로, 그리고 상처 치유에 써 왔다고 소개된다[2]. 말라리아가 20세기 전반까지 남아 있던 사르데냐에서는 이 풀을 말라리아에 쓰던 민간 전통이 있었고, 그 정유가 시험관에서 열대열 말라리아 원충을 억제했다는 보고가 이 전통을 뒷받침하는 근거로 제시되었다[6]. 이탈리아에서는 '사르데냐 세이보리(Santoreggia sarda)'라는 이름으로 알려져 있다[9].

리비아 민간에서는 이 종의 정유를 소독제·강장제·위 진정제·이뇨제로 쓴다고 소개되며[4], 식품 향미·향수·가정 상비약으로 써 왔다는 서술도 있다[5]. 터키 남서부 마르마리스 지역 민족식물 조사에서는 이 종이 가장 흔히 쓰이는 약용식물 다섯 가지 가운데 하나로 꼽혔다[14]. 레바논에서는 당뇨에 전통적으로 쓰인다는 식물 9종 가운데 하나로 조사되었고[16], 레바논산 세이보리·백리향류 5종 정유의 항균 시험은 레바논 민간 의약에서의 이용을 뒷받침하는 근거로 제시되었다[25]. 팔레스타인에서는 지혈 효과를 보려고 잎 추출물의 혈액 응고 시험이 이루어졌다[15]. 이런 전통 용도를 사람에게서 시험한 임상 연구는 확인하지 못함.""")
S["biology"] = ("식물학적 특징", """타임잎세이보리는 가지가 많이 갈라지고 흔히 회색 잔털로 덮인 키 20–35 cm 의 왜성 관목이다[4]. 여러해살이 관목으로, 분포는 터키·그리스에서 서쪽 끝인 이탈리아 사르데냐까지 동지중해 분지에 걸친다[2]. 유럽에서는 남에게해 지역과 사르데냐 남쪽 해안에 분포하고, 리비아에서는 동부 녹색산지(Al Jabal Al Akhdar)에서만 자란다[4]. 사르데냐에서는 칼리아리의 산 미켈레 언덕 비탈에만 남아 있다고 보고되었다[9].

이 종과 Coridothymus capitatus 를 함께 분석한 크레타 연구에서는 저지대의 건조한 왜성 관목림에서 자란 개체가 카르바크롤형, 더 습한 숲이나 고지대에서 자란 개체가 티몰형 정유를 내는 경향이 있었다[7]. 이스라엘·레바논·터키·리비아 등지의 야생 개체에서도 정유 연구가 이어졌다[4, 8, 20, 25]. 꽃 피는 시기는 시료마다 달라 리비아 시료는 3월에, 사르데냐 시료는 6월에 꽃이 핀 상태로 채취되었다[2, 4].

식용 부위가 아닌 씨앗의 지방산 메틸에스터 분석에서는 올레산 43.9%, 리놀렌산 30.2%, 스테아르산 14.1%, 팔미트산 11.4%가 보고되었다[13].""")
S["related_species"] = ("이름과 가까운 종", """식약처 「식품원료 목록」에는 같은 세이보리속(Satureja) 원료로 여름세이보리(S. hortensis)의 잎과 건조품, 겨울세이보리(S. montana)의 잎, Creeping savory(S. spicigera)의 잎, Wild basil(S. vulgaris, 목록 표기 [Clinopodium vulgare])의 잎이 따로 올라 있다[1]. 이들은 이 종과 다른 원료이므로 성분·안전성 자료를 섞어 쓰면 안 된다[1]. 특히 식품첨가물 천연향료 행의 'Savory, summer'·'Savory, winter'는 여름세이보리와 겨울세이보리를 가리키며 이 종이 아니다[1].

이 종은 흔히 Thymbra spicata, Coridothymus capitatus 처럼 카르바크롤·티몰이 많은 이웃 속 식물과 함께 연구된다[7, 20, 25]. 그리스 고유종인 Satureja parnassica 와 정유 조성·항균력·세포 시험을 비교한 연구도 있다[10, 17]. 목록에는 이름에 '세이보리'가 들어간 원료가 이 종 말고도 여럿 있다[1].

분자계통 연구에서 박하아족(Menthinae)은 '세이보리'·'미크로메리아'·'클리노포디움' 세 큰 무리로 나뉘었고, 세이보리속의 두 종이 Thymbra 속 안에 들어가 세이보리속이 다계통군으로 드러났다[19]. 이 두 종이 어느 종인지는 초록에서 확인하지 못함.""")
S["cultivation"] = ("재배와 산지", """연구에 쓰인 시료는 대부분 그리스·크레타·터키·리비아·레바논·이스라엘·사르데냐의 야생 개체에서 채취되었다[2, 4, 7, 8, 20, 25]. 사르데냐 연구진은 이 종이 재배하기 쉽다고 적었으나[2], 상업 재배 면적이나 생산량 통계는 확인하지 못함. 국내 재배·생산 통계도 확인하지 못함.

정유 수율과 조성은 환경에 따라 크게 달라진다[5, 7]. 리비아 녹색산지에서 해발 150 m(초록 표기 156 m) 지점 시료의 2017년 정유 수율은 1.6 ± 0.03%(v/w, 건조 중량), 해발 661 m 지점은 1.4 ± 0.02%였고, 낮은 곳은 티몰, 높은 곳은 카르바크롤이 주성분이었다[5]. 그리스 시미섬 야생 시료의 정유 수율은 2.8%(v/w)였다[3].

채취 시기도 영향을 준다[6, 10]. 그리스 연구에서는 꽃 피는 시기의 정유가 항균력이 가장 강했다[10]. 사르데냐 칼리아리 시료는 꽃 피기 전 생 지상부 2.0 kg 에서 정유 5.4 g, 꽃 필 때 2.3 kg 에서 15.7 g, 꽃 진 뒤 1.1 kg 에서 8.0 g 을 얻었다[6]. 사르데냐 시료의 티몰 비율은 꽃 피기 전·중·후에 36.0%, 52.6%, 57.1%로 늘었다는 앞선 연구 수치가 인용되어 있다[2].""")
S["processing"] = ("가공과 이용", """정유는 주로 지상부를 물 증류나 수증기 증류해서 얻는다[2, 4]. 사르데냐에서는 꽃 핀 생 지상부 980 g 을 3시간 수증기 증류해 정유 8 mL 를 얻었다[2]. 초임계 이산화탄소 추출물과 물 증류 정유는 조성에서 큰 차이가 없었다[9]. 이 종은 향과 단맛 덕분에 의약품과 식품의 향미 성분으로 흔히 쓰인다고 소개된다[2].

식품 가공 연구로는 해바라기유 수중유적형 유화액에 이 종의 에틸아세테이트·에탄올 추출물, 로즈마린산, 퀘르세틴을 각각 넣은 실험이 있는데, 5 °C 에서 첨가물의 산화 보호율은 73–81% 였고 40 °C 에서는 에탄올 추출물이 약 53%로 높은 편이었다[11]. 로즈마린산과, 오레가노·이 종에서 얻은 하이드록시신남산이 풍부한 추출물을 메를로 포도주에 보조인자로 넣은 실험에서는 안토시아닌 공색소화로 색 강도가 15–50% 높아졌다[24].

정유는 식품 보존제 후보로도 시험되었다[21, 22]. 0.1%(v/v) 정유는 소금 농도와 pH 조건을 함께 바꿀 때 리스테리아와 살모넬라의 증식 시작을 크게 막았으나, 0.06% 이하는 효과가 거의 없었다[21]. 스테인리스 표면의 세균 생물막에는 정유 1%와 증류 부산물인 하이드로졸 100%가 강한 살균 효과를 보였다[22]. 정유를 인지질 나노소포에 넣어 안정성을 높인 제형 연구도 있다[2, 3]. 국내 제품 생산실적은 확인하지 못함.""")
S["genetics"] = ("유전 정보", """이 종의 정유는 카르바크롤형과 티몰형, 그리고 두 페놀이 비슷하게 섞인 형으로 나뉜다[7]. 이스라엘 야생 개체에서도 일찍이 화학형 차이가 보고되었다[20]. 사르데냐 시료는 티몰이 많고 카르바크롤이 적어, 카르바크롤이 많은 그리스 시료와 다른 화학형으로 설명된다[2]. 그리스 시미섬 시료는 카르바크롤 46.0%로 카르바크롤형이었다[3].

다만 같은 리비아 산지 안에서도 해발고도에 따라 주성분이 티몰과 카르바크롤로 갈렸고 두 해 동안 비슷한 경향이 유지되었다[5]. 따라서 화학형의 차이가 유전형 차이인지 서식지 영향인지는 원문들에서도 완전히 가려지지 않았다[5, 7].

세이보리속 엽록체 유전체 연구는 여름세이보리·겨울세이보리 등 세 종을 해독했고 크기는 151,777–151,924 bp 였으며, ndhF·ycf1 이 종 구분용 바코드 후보로 제시되었다[18]. 이 연구 전에는 겨울세이보리의 완전한 엽록체 유전체만 공개되어 있었다고 하며, 타임잎세이보리의 엽록체 유전체는 이 연구에 포함되지 않았다[18]. 이 종의 핵 유전체·염색체 수는 확인하지 못함.""")
S["safety"] = ("안전성", """식약처 「식품원료 목록」상 이 종은 잎만 식품원료로 쓸 수 있다[1]. 이 종에 대한 식약처·EFSA 등 공공기관의 독성 평가, 알레르기 정보, 1일 섭취 한도는 확인하지 못함. 사람을 대상으로 한 안전성 시험도 확인하지 못함.

세포 시험에서는 사르데냐 정유가 사람 섬유아세포에 24시간 동안 10–50 µg/mL 에서는 독성을 보이지 않았고, 100 µg/mL 에서는 일부 독성이 나타났다[6]. 이 시험에서는 카르바크롤 비율이 높은 분획에서 세포 독성이 커서 카르바크롤이 독성의 원인일 수 있다고 해석되었다[6]. 사람 피부 각질세포에서는 정유 용액 5 µg/mL 에서 생존율이 81%로 약간 떨어졌다[2]. 암세포주에서 세포 증식 억제가 관찰된 결과는 시험관 자료일 뿐 사람에게 항암 효과가 있다는 뜻이 아니다[5, 17].

팔레스타인 연구에서 이 종의 잎 물 추출물은 시험관에서 프로트롬빈 시간을 유의하게 늘렸다[15]. 이는 혈액 응고에 영향을 줄 수 있다는 시험관 신호일 뿐, 사람에서 출혈 위험이나 약물 상호작용이 확인된 것은 아니다[15]. 식용 부위가 아닌 씨앗과 정유 자체의 식품 지위는 확인하지 못함.""")

compounds = [
 {"name": "Carvacrol", "name_ko": "카르바크롤", "class": "페놀성 모노테르펜", "role": "marker", "part": "지상부(잎·꽃) 정유", "content_text": "크레타 13개 시료 정유 최대 75.7%[7]; 그리스 시미섬 정유 46.0%[3]; 터키 시료 정유 40.15%[8]; 리비아 해발 661 m 시료 정유 14.3%(최대 성분)[5]; 사르데냐 정유 7.08%(GC), HPLC-DAD 18.10 mg/L[2]", "activity_ko": "이 종 정유는 레바논산 5종 정유 가운데 항균력이 가장 컸음(시험관)[25]; 카르바크롤 비율이 높은 분획에서 사람 섬유아세포 독성이 커짐[6]", "source": [2, 3, 5, 6, 7, 8, 25]},
 {"name": "Thymol", "name_ko": "티몰", "class": "페놀성 모노테르펜", "role": "marker", "part": "지상부(잎·꽃) 정유", "content_text": "크레타 시료 정유 최대 65.6%[7]; 사르데냐 정유 23.88%(GC), HPLC-DAD 470.25 mg/L[2]; 리비아(바이다) 정유 25.16%[4]; 리비아 해발 150 m 시료 정유 29.6%(본문 표기; 초록은 26.69%)[5]", "activity_ko": "사르데냐 정유의 말라리아 원충 억제 활성에 기여하는 성분으로 제시됨(시험관)[6]", "source": [2, 4, 5, 6, 7]},
 {"name": "gamma-Terpinene", "name_ko": "γ-테르피넨", "class": "모노테르펜 탄화수소", "role": "bioactive", "part": "지상부 정유", "content_text": "리비아 정유 39.23%(초록; 본문 39.26%)[4]; 터키 정유 26.56%[8]; 사르데냐 정유 20.38%[2]; 그리스 시미섬 정유 19.7%[3]", "activity_ko": "카르바크롤의 생합성 전구체로 논의됨[3]", "source": [2, 3, 4, 8]},
 {"name": "p-Cymene", "name_ko": "p-시멘", "class": "모노테르펜 탄화수소", "role": "bioactive", "part": "지상부 정유", "content_text": "터키 정유 16.39%[8]; 그리스 시미섬 정유 7.6%[3]; 사르데냐 정유 7.27%[2]; 리비아 정유 7.17%[4]", "activity_ko": "카르바크롤의 생합성 전구체로 논의됨[3]", "source": [2, 3, 4, 8]},
 {"name": "beta-Caryophyllene", "name_ko": "β-카리오필렌", "class": "세스퀴테르펜 탄화수소", "role": "bioactive", "part": "지상부 정유·초임계 추출물", "content_text": "그리스 시미섬 정유 7.0%[3]; 사르데냐 초임계 CO2 추출물·물 증류 정유의 주성분 가운데 하나(수치는 초록에 없음)[9]", "activity_ko": "확인하지 못함", "source": [3, 9]},
 {"name": "alpha-Terpinene", "name_ko": "α-테르피넨", "class": "모노테르펜 탄화수소", "role": "bioactive", "part": "지상부 정유", "content_text": "그리스 시미섬 정유 5.1%[3]", "activity_ko": "확인하지 못함", "source": [3]},
 {"name": "Myrcene", "name_ko": "미르센", "class": "모노테르펜 탄화수소", "role": "bioactive", "part": "지상부 정유", "content_text": "그리스 시미섬 정유 2.5%[3]", "activity_ko": "확인하지 못함", "source": [3]},
 {"name": "alpha-Thujene", "name_ko": "α-투옌", "class": "모노테르펜 탄화수소", "role": "bioactive", "part": "지상부 정유", "content_text": "그리스 시미섬 정유 2.4%[3]", "activity_ko": "확인하지 못함", "source": [3]},
 {"name": "Borneol", "name_ko": "보르네올", "class": "모노테르펜 알코올", "role": "bioactive", "part": "지상부 정유·초임계 추출물", "content_text": "사르데냐 시료 추출물의 주성분 가운데 하나(수치는 초록에 없음)[9]", "activity_ko": "확인하지 못함", "source": [9]},
 {"name": "Isospathulenol", "name_ko": "이소스파툴레놀", "class": "세스퀴테르펜 알코올", "role": "bioactive", "part": "지상부 정유", "content_text": "리비아 해발 150 m 시료 정유 13.4%, 해발 661 m 시료 정유 2.1%[5]", "activity_ko": "확인하지 못함", "source": [5]},
 {"name": "Rosmarinic acid", "name_ko": "로즈마린산", "class": "하이드록시신남산 에스터(뎁시드)", "role": "bioactive", "part": "에틸아세테이트·에탄올 추출물(부위는 초록에 명시 없음)", "content_text": "HPLC 분석에서 두 추출물의 주성분(수치는 초록에 없음)[11]", "activity_ko": "유화액 저장 중 가장 많이 줄어든 페놀 성분, 단독 첨가 시 유화액 산화 보호 효과는 추출물보다 약함[11]", "source": [11]},
 {"name": "gamma-Tocopherol", "name_ko": "γ-토코페롤", "class": "토코페롤(비타민 E)", "role": "nutrient", "part": "헥산 추출물의 비비누화 분획", "content_text": "네 가지 '오레가노' 식물(이 종 포함) 모두에서 γ-동족체가 가장 많음; 총 토코페롤 288–672 ppm(네 종 범위, 이 종 단독 값은 초록에 없음)[12]", "activity_ko": "지용성 항산화 성분[12]", "source": [12]},
 {"name": "Oleic acid", "name_ko": "올레산", "class": "단일불포화 지방산", "role": "nutrient", "part": "씨앗(식품원료 사용 부위 아님)", "content_text": "씨앗 지방산 메틸에스터 43.9%; 리놀렌산 30.2%, 스테아르산 14.1%, 팔미트산 11.4%[13]", "activity_ko": "확인하지 못함", "source": [13]},
]

assays = [
 {"role": "literature", "compound": "Thymol", "compound_ko": "티몰(카르바크롤 동시 정량)", "part": "꽃 핀 지상부(사르데냐 칼리아리, 2021년 6월 채취) 생시료 수증기 증류 정유",
  "content": "티몰 470.25 mg/L, 카르바크롤 18.10 mg/L(HPLC-DAD, 원문 표기 그대로); GC 면적 백분율로는 티몰 23.88%, 카르바크롤 7.08%[2]",
  "method": "HPLC-DAD(외부표준법)",
  "conditions": {"instrument": "Agilent 1260 Infinity II HPLC(펌프 G7111A, 자동주입기 G7129A, 다이오드 배열 검출기 G4212B)", "column": "Phenomenex Kinetex EVO C18, 150 mm × 4.60 mm, 2.6 µm", "mobile_phase": "0.22 M 인산 : 아세토나이트릴 = 60 : 40 (v/v)", "gradient": "등용매(원문에 기울기 없음)", "flow": "0.8 mL/min", "temp": "30 °C", "detection": "DAD 200–600 nm 수집, 크로마토그램 210 nm", "injection": "10 µL", "sample_prep": "정유를 메탄올에 1:10 으로 녹인 뒤 메탄올 : 0.22 M 인산 = 80 : 20 혼합액으로 다시 1:10 희석", "standard": "티몰·카르바크롤 표준품(메탄올 원액, 0.22 M 인산으로 희석)", "linearity": "1–200 mg/L, R² ≥ 0.9993(두 성분)", "lod": "≥ 0.12 mg/L(두 성분)", "loq": "≥ 0.35 mg/L(두 성분)", "recovery": ""},
  "rationale": "티몰과 카르바크롤은 이 종 정유의 주된 페놀 성분이고 화학형(티몰형·카르바크롤형)을 가르는 기준이므로 두 성분을 함께 정량하는 것이 품질 지표로 적합하다; 전문 확인, 회수율은 원문에 없음[2, 7]",
  "source": [2], "url": "https://doi.org/10.3390/molecules29051041", "source_kind": "paper"},
 {"role": "literature", "compound": "Carvacrol", "compound_ko": "카르바크롤", "part": "건조 지상부(그리스 시미섬 야생, 2018년 여름 채취) 물 증류 정유",
  "content": "GC-MS 면적 백분율 카르바크롤 46.0%, γ-테르피넨 19.7%, p-시멘 7.6%, β-카리오필렌 7.0%; 정유 수율 2.8%(v/w)[3]. HPLC-DAD 는 나노소포에 담긴 정유의 정량에 쓰였고 정유 자체의 mg 단위 함량은 원문에 없음[3]",
  "method": "HPLC-DAD(나노소포 내 정유 정량), 정유 조성은 GC-MS 반정량",
  "conditions": {"instrument": "Agilent 1100 HPLC-DAD", "column": "Luna C18 100 Å, 250 × 4.6 mm, 5 µm", "mobile_phase": "A 아세토나이트릴, B 포름산/물(pH 3.2)", "gradient": "0–3분 B 30%, 3–10분 30→80%, 10–15분 80%, 15–20분 80→95%, 20–22분 95%, 22–27분 95→30%", "flow": "1 mL/min", "temp": "25 °C", "detection": "276 nm", "injection": "", "sample_prep": "건조 지상부 40.0 g 을 그리스 약전에 따라 변형 클레벤저 장치로 2시간 물 증류", "standard": "카르바크롤 0.001 µL/µL 메탄올 표준액과 단계 희석액", "linearity": "R² 0.9999", "lod": "", "loq": "", "recovery": ""},
  "rationale": "원문은 카르바크롤을 이 정유의 가장 많은 성분이자 지표 성분(marker constituent)으로 보고 HPLC 정량 대상으로 삼았다; 전문 확인, 검출·정량한계와 회수율은 원문에 없음[3]",
  "source": [3], "url": "https://doi.org/10.3390/molecules26082124", "source_kind": "paper"},
 {"role": "literature", "compound": "gamma-Terpinene", "compound_ko": "γ-테르피넨(티몰·p-시멘·카르바크롤 동시 분석)", "part": "꽃 필 때 채취한 건조 지상부(나무질 부분 제거, 리비아 바이다, 2010년 3월) 물 증류 정유",
  "content": "γ-테르피넨 39.23%(초록; 본문 39.26%), 티몰 25.16%, p-시멘 7.17%, 카르바크롤 4.18%(GC-FID 면적 백분율)[4]",
  "method": "GC-FID(정량) + GC-MS(동정)",
  "conditions": {"instrument": "HP-5890 II GC-FID; GC-MS 는 HP G1800C Series II GCD", "column": "GC-FID: HP-5, 25 m × 0.32 mm, 0.52 µm; GC-MS: HP-5MS, 30 m × 0.25 mm, 0.25 µm", "mobile_phase": "운반기체 수소", "gradient": "40 → 240 °C, 4 °C/min", "flow": "1 mL/min", "temp": "주입구 250 °C, 검출기 300 °C, GC-MS 전송관 260 °C", "detection": "FID; MS 는 EI 70 eV, m/z 40–400", "injection": "스플릿 1:30", "sample_prep": "그늘에서 10일 말린 지상부 100 g 을 영국약전에 따라 클레벤저 장치로 3시간 물 증류, 무수 황산나트륨 건조, 4 °C 암소 보관", "standard": "표준물질 머무름시간 대조와 Wiley 275 질량 스펙트럼 라이브러리, AMDIS 확인", "linearity": "", "lod": "", "loq": "", "recovery": "FID 면적 백분율 기준(감응 계수 보정 언급 없음)"},
  "rationale": "리비아 시료는 γ-테르피넨이 가장 많아 카르바크롤·티몰형과 다른 조성을 보였으므로, 페놀 두 성분과 그 전구체인 γ-테르피넨·p-시멘을 함께 보는 것이 산지 판별에 쓸모 있다; 전문 확인, 절대 정량이 아닌 면적 백분율이다[3, 4]",
  "source": [3, 4], "url": "https://doi.org/10.3390/molecules17054836", "source_kind": "paper"},
]

d = {
 "slug": "satureja-thymbra", "name_ko": "타임잎세이보리", "name_en": "Thyme-leaved savory",
 "scientific_name": "Satureja thymbra L.",
 "aliases": ["타임잎세이보리잎", "Thyme-leaved savory", "Pink savory", "Santoreggia sarda"],
 "sections": [{"key": k, "title": t, "body": b} for k, (t, b) in S.items()],
 "compounds": compounds, "markers": [], "nutrients": [], "assays": assays,
 "production": [], "world": [], "gi": [], "orgs": [], "sources": sources,
}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for k,(t,b) in S.items(): print(k, len(b))
