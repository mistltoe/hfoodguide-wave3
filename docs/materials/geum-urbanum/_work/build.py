import json
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "dossier.json"
ACC = "2026-11-02"
I1020 = "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020"


def pm(pmid):
    return f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"


def pmc(p):
    return f"https://pmc.ncbi.nlm.nih.gov/articles/{p}/"


S = [
    (1, "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 허브베니트뿌리·허브베니트잎(Geum urbanum), 영문명 'Wood avens, Herb bennet', 사용가능, 사용가능부위 : 뿌리,잎 (로컬 원자료 I1020_20261013.json)", I1020, "식품의약품안전처", "2026-10-13"),
    (2, "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 같은 속 원료 행: 뱀무순(Geum japonicum, 'Asian herb bennet', 순), 큰뱀무잎·큰뱀무순(Geum aleppicum, 잎·순), Water avens뿌리(Geum rivale, 영문명 'Herb Robert, Old-mans-whiskers', 뿌리), White avens뿌리(Geum canadense, 뿌리) (로컬 원자료 I1020_20261013.json)", I1020, "식품의약품안전처", "2026-10-13"),
    (3, "Ellagitannins and Other Polyphenols Along with Dietary Components of the Rosaceae Medicinal Plants (Molecules 2025;30(23):4574, doi:10.3390/molecules30234574; PMC 전문 확인)", pmc("PMC12693333"), "Molecules (PubMed Central)", ACC),
    (4, "Avens Root (Geum urbanum L.) Extract Discovered by Target-Based Screening Exhibits Antidiabetic Activity in the Hen's Egg Test Model and Drosophila melanogaster (Front Pharmacol 2021;12:794404, doi:10.3389/fphar.2021.794404; PMC 전문 확인)", pmc("PMC8715001"), "Frontiers in Pharmacology (PubMed Central)", ACC),
    (5, "Composition of essential oil from aerial and underground parts of Geum rivale and G. urbanum growing in Poland (Nat Prod Commun 2013;8(4):505-8; 초록만 확인)", pm("23738465"), "Natural Product Communications (PubMed)", ACC),
    (6, "The genome sequence of wood avens, Geum urbanum L., 1753 (Wellcome Open Res 2024, doi:10.12688/wellcomeopenres.19664.2; PMC 전문 확인)", pmc("PMC11327653"), "Wellcome Open Research (PubMed Central)", ACC),
    (7, "In Vitro Antineoplastic and Antiviral Activity and In Vivo Toxicity of Geum urbanum L. Extracts (Molecules 2021;27(1):245, doi:10.3390/molecules27010245; PMC 전문 확인)", pmc("PMC8747043"), "Molecules (PubMed Central)", ACC),
    (8, "Antimicrobial and antioxidant potential of different solvent extracts of the medicinal plant Geum urbanum L. (Chem Cent J 2017;11(1):113, doi:10.1186/s13065-017-0343-8; 초록 확인)", pmc("PMC5676587"), "Chemistry Central Journal (PubMed Central)", ACC),
    (9, "Effects of Geum urbanum L. root extracts and its constituents on polymorphonuclear leucocytes functions. Significance in periodontal diseases (J Ethnopharmacol 2016;188:1-12, doi:10.1016/j.jep.2016.04.030; 초록만 확인)", pm("27139570"), "Journal of Ethnopharmacology (PubMed)", ACC),
    (10, "Evaluation of Geum urbanum L. Extracts with Respect to Their Antimicrobial Potential (Chem Biodivers 2022, doi:10.1002/cbdv.202100850; 초록만 확인)", pm("34882948"), "Chemistry & Biodiversity (PubMed)", ACC),
    (11, "Chemical constituents of Geum urbanum L. roots (Nat Prod Res 2018;32(21):2529-34, doi:10.1080/14786419.2018.1425844; 초록만 확인)", pm("29363330"), "Natural Product Research (PubMed)", ACC),
    (12, "Insight into the Secondary Metabolites of Geum urbanum L. and [같은 속 다른 1종] Seeds (Rosaceae) (Plants 2021;10(6):1219, doi:10.3390/plants10061219; 초록 확인 — 함께 분석한 종의 학명은 PubMed 초록 표기에서 확인하지 못함)", pmc("PMC8232588"), "Plants (PubMed Central)", ACC),
    (13, "Maintaining their genetic distance: Little evidence for introgression between widely hybridizing species of Geum with contrasting mating systems (Mol Ecol 2018;27(5):1214-28, doi:10.1111/mec.14426; 초록 확인)", pmc("PMC5900869"), "Molecular Ecology (PubMed Central)", ACC),
    (14, "Early evolution in a hybrid swarm between outcrossing and selfing lineages in Geum (Heredity 2011;107(3):246-55, doi:10.1038/hdy.2011.9; 초록 확인)", pmc("PMC3183954"), "Heredity (PubMed Central)", ACC),
    (15, "The consequences of mating over a range of parental genetic similarity in a selfing allopolyploid plant species (J Evol Biol 2011;24(12):2750-8, doi:10.1111/j.1420-9101.2011.02390.x; 초록만 확인)", pm("21955301"), "Journal of Evolutionary Biology (PubMed)", ACC),
    (16, "Landscape genetics of the self-compatible forest herb Geum urbanum: effects of habitat age, fragmentation and local environment (Mol Ecol 2007;16(19):4171-9, doi:10.1111/j.1365-294X.2007.03473.x; 초록만 확인)", pm("17784918"), "Molecular Ecology (PubMed)", ACC),
    (17, "A comparative study of Geum rivale L. and G. urbanum L. to determine those factors controlling their altitudinal distribution II. Photosynthesis and respiration (New Phytol 1988;108(3):297-304, doi:10.1111/j.1469-8137.1988.tb04166.x; 초록만 확인)", pm("33873938"), "New Phytologist (PubMed)", ACC),
    (18, "A model of the seasonal pattern of carbon acquisition in two woodland herbs, Mercurialis perennis L. and Geum urbanum L. (Oecologia 1990;83(4):479-84, doi:10.1007/BF00317198; 초록만 확인)", pm("28313181"), "Oecologia (PubMed)", ACC),
    (19, "Evaluation of anti-inflammatory activity of some Swedish medicinal plants. Inhibition of prostaglandin biosynthesis and PAF-induced exocytosis (J Ethnopharmacol 1995;48(2):61-76, doi:10.1016/0378-8741(95)01285-l; 초록만 확인)", pm("8583796"), "Journal of Ethnopharmacology (PubMed)", ACC),
    (20, "Scientific basis for the industrialization of traditionally used plants of the Rosaceae family (Food Chem 2020;330:127197, doi:10.1016/j.foodchem.2020.127197; 초록만 확인)", pm("32540521"), "Food Chemistry (PubMed)", ACC),
    (21, "Evaluation of a guideline for supportive anthroposophic therapies for hospitalised children with acute gastroenteritis - A prospective case series study (Complement Ther Med 2024, doi:10.1016/j.ctim.2024.103042; 초록만 확인)", pm("38636719"), "Complementary Therapies in Medicine (PubMed)", ACC),
    (22, "[An indigenous tonic, the benoite (Geum urbanum L.)] (Presse Med 1947;55(68):796; 프랑스어, 초록 없음 — 서지 정보만 확인)", pm("18933111"), "La Presse médicale (PubMed)", ACC),
    (23, "[The heredity pattern of eugenol glycoside in crossbreeding of Geum urbanum and Geum rivale] (Pharm Weekbl 1952;87(37-38):641-6; 초록 없음 — 서지 정보만 확인)", pm("13013796"), "Pharmaceutisch weekblad (PubMed)", ACC),
    (24, "[Determination of geoside in the roots of various species of Geum] (Pharm Weekbl 1953;88(23-24):385-8; 초록 없음 — 서지 정보만 확인)", pm("13088260"), "Pharmaceutisch weekblad (PubMed)", ACC),
    (25, "Vicianose from the root of Geum urbanum (Planta Med 1972;22(1):93-6, doi:10.1055/s-0028-1099588; 초록 없음 — 서지 정보만 확인)", pm("5083254"), "Planta Medica (PubMed)", ACC),
    (26, "Role of human gut microbiota metabolism in the anti-inflammatory effect of traditionally used ellagitannin-rich plant materials (J Ethnopharmacol 2014;155(1):801-9, doi:10.1016/j.jep.2014.06.032; 초록만 확인)", pm("24969824"), "Journal of Ethnopharmacology (PubMed)", ACC),
    (27, "Antioxidant and anti-inflammatory activities of Geranium robertianum L. decoctions (Food Funct 2017;8(9):3355-65, doi:10.1039/c7fo00881c; 초록만 확인 — 'Herb Robert' 영명의 근거)", pm("28858365"), "Food & Function (PubMed)", ACC),
    (28, "Inhibition of the MRSA Biofilm Formation and Skin Antineoplastic Activity of Ethyl Acetate Roots and Aerial Parts Extracts from Geum urbanum L. (Antibiotics 2025;14(7):627, doi:10.3390/antibiotics14070627; 초록 확인)", pmc("PMC12291766"), "Antibiotics (PubMed Central)", ACC),
    (29, "Dose-response effects of woody and herbaceous forage plants on in vitro ruminal methane and ammonia formation, and their short-term palatability in lactating cows (Animal 2020;14(3):538-48, doi:10.1017/S1751731119002076; 초록만 확인)", pm("31576794"), "Animal (PubMed)", ACC),
    (30, "Conservation of Non-Pest Whiteflies and Natural Enemies of the Cabbage Whitefly on Perennial Plants for Use in Non-Crop Habitats (Insects 2021;12(9):774, doi:10.3390/insects12090774; 초록 확인)", pmc("PMC8468402"), "Insects (PubMed Central)", ACC),
    (31, "Polyherbal mixture ameliorates hyperglycemia, hyperlipidemia and histopathological changes of pancreas, kidney and liver in a rat model of type 1 diabetes (J Ethnopharmacol 2020, doi:10.1016/j.jep.2020.113210; 초록만 확인 — 5종 혼합물)", pm("32795501"), "Journal of Ethnopharmacology (PubMed)", ACC),
    (32, "Inhibitory potential of some Romanian medicinal plants against enzymes linked to neurodegenerative diseases and their antioxidant activity (Pharmacogn Mag 2015;11(Suppl 1):S110-6, doi:10.4103/0973-1296.157709; 초록 확인)", pmc("PMC4461949"), "Pharmacognosy Magazine (PubMed Central)", ACC),
    (33, "Interspecies differences in the preference of ammonium and nitrate in vascular plants (Oecologia 1995;102(3):305-11, doi:10.1007/BF00329797; 초록만 확인)", pm("28306841"), "Oecologia (PubMed)", ACC),
    (34, "Temperature effects on forest understorey plants in hedgerows: a combined warming and transplant experiment (Ann Bot 2021, doi:10.1093/aob/mcab064; 초록 확인)", pmc("PMC8389467"), "Annals of Botany (PubMed Central)", ACC),
]

sections = [
    ("overview", "한눈에 보기",
     "허브베니트(Geum urbanum L.)는 장미과 뱀무속의 여러해살이풀로, 영어로는 wood avens 또는 herb bennet이라 부른다[1, 6]. "
     "유럽에 널리 자라며 서아시아·서시베리아·아프리카 북서 해안까지 분포한다[6]. "
     "식품의약품안전처 「식품원료 목록」에는 '허브베니트뿌리'와 '허브베니트잎' 두 원료가 '사용가능'으로 올라 있고, 사용 조건은 '사용가능부위 : 뿌리,잎'이다[1]. "
     "따라서 식품으로 쓸 수 있는 부위는 뿌리와 잎이며, 꽃·씨앗은 목록의 사용 부위에 들어 있지 않다[1]. "
     "'허브베니트'는 목록의 원료명이며, 국가표준식물목록의 국명은 확인하지 못함. "
     "이 종을 원재료로 하는 건강기능식품 고시형 원료는 확인하지 못함.\n\n"
     "뿌리줄기에는 탄닌이 약 20% 들어 있고 그 대표가 엘라지타닌인 제민 A(gemin A)이며, 유제놀 배당체(gein)와 정유(0.1%)도 들어 있다고 정리되어 있다[3]. "
     "폴란드산 시료의 땅속 부위 정유에서는 유제놀이 69.2%로 주성분이었다[5]. "
     "뿌리 에탄올 추출물에서는 새 디하이드로디갈산 유도체 1종과 페놀 6종·스테로이드 2종·트리테르페노이드 11종이 분리되었다[11]. "
     "5월에 딴 어린 생잎의 총 폴리페놀은 생체 100 g당 2.1 g이었고, 그중 72%가 제민 A였다[3]. "
     "효능 연구는 대부분 세포·효소 시험이나 초파리·달걀 모델 단계이며, 사람을 대상으로 한 임상시험은 확인하지 못함."),
    ("history", "이용의 역사",
     "허브베니트는 유럽 민간요법에서 오래 쓰였으며, 특히 불가리아 전통 의학에서 출혈과 점막 염증을 줄이는 위장 약초로 쓰였다[7]. "
     "지상부·뿌리·뿌리줄기를 달이거나 우려서 설사·이질·소화불량·위장염·발열 등에 권했다는 기록이 정리되어 있다[7]. "
     "뿌리 우린 물과 달인 물은 잇몸 출혈·염증(치은염)과 점막 염증에 바깥으로 쓰였고[9], 뿌리와 뿌리줄기 제제는 입·위·장 점막의 궤양과 자극에 써 왔다[10]. "
     "스웨덴 전통 의학에서 염증·상처에 쓰던 식물을 모은 연구에도 포함되었고[19], 스페인 갈리시아 전통 의학에서 쓰는 장미과 식물 6종 가운데 하나로도 꼽혔다[20].\n\n"
     "1947년 프랑스 의학지에는 이 식물을 '토착 강장제'로 소개한 글이 실렸다(원문 확인하지 못함)[22]. "
     "1950년대에는 뿌리의 유제놀 배당체를 다룬 연구가 이어졌는데, 허브베니트와 Geum rivale 교잡에서 이 배당체의 유전 양상을 다룬 보고(1952년)와 여러 뱀무속 뿌리의 배당체 정량 보고(1953년)가 있다(모두 초록 없음)[23, 24]. "
     "독일의 인지학 의학 병원에서는 급성 위장염으로 입원한 어린이 62명의 증례 연구에서 허브베니트가 가장 자주 쓰인 처방 가운데 하나였다[21]. "
     "다만 이 연구는 증례 관찰로서 효과를 대조군과 비교한 시험이 아니다[21]."),
    ("biology", "식물학적 특징",
     "허브베니트는 연갈색 수염뿌리가 많은 굵은 뿌리줄기를 지닌 여러해살이풀로, 줄기는 1 m까지 자라고 잎에는 퍼진 털과 톱니가 있다[3]. "
     "작은 노란 꽃은 꽃잎이 5장이고 6–8월에 핀다[3]. "
     "열매(수과)에는 갈고리가 하나씩 있어 동물 몸에 붙어 퍼진다[6]. "
     "주로 제꽃가루받이를 하며, 자연 집단의 타가수분율은 0.058–0.177로 보고되었다[6].\n\n"
     "숲·덤불·산울타리처럼 물 빠짐이 좋은 그늘진 곳에 흔하고, 교란지·정원·공원에도 자란다[6]. "
     "낙엽수림 하층의 초본으로, 같은 속 Geum rivale보다 환경에 따른 형태·생리 변화(표현형 가소성)가 컸다[17]. "
     "겨울을 나는 잎이 있고 낮은 온도에서도 광합성을 유지해, 나무 잎이 우거지기 직전의 밝은 봄빛을 잘 이용한다[18]. "
     "숲과 산울타리에 옮겨 심은 실험에서는 숲에서 더 크고 무겁게 자랐고, 북쪽으로 옮겼을 때 키·생물량·종자 생산·생존이 더 좋았다[34]. "
     "질소 요구가 큰 편으로, 23종을 비교한 수경 실험에서 가장 질소를 많이 요구했고 질산태와 암모늄태 질소를 함께 줄 때 더 잘 자랐다[33]."),
    ("related_species", "근연종과 구별",
     "식약처 목록에는 같은 속 원료로 뱀무(Geum japonicum, 순), 큰뱀무(Geum aleppicum, 잎·순), Water avens(Geum rivale, 뿌리), White avens(Geum canadense, 뿌리)가 따로 올라 있다[2]. "
     "종마다 쓸 수 있는 부위가 다르므로, 허브베니트의 '뿌리·잎' 조건이나 성분 자료를 다른 종에 옮겨 쓰면 안 된다[1, 2]. "
     "특히 뱀무의 영문명은 'Asian herb bennet'로 허브베니트(herb bennet)와 비슷하다[1, 2].\n\n"
     "목록의 Geum rivale 행에는 영문명이 'Herb Robert, Old-mans-whiskers'로 적혀 있다[2]. "
     "그러나 'Herb Robert'는 쥐손이풀과의 Geranium robertianum을 가리키는 흔한 영명이므로, 영명만으로 원료를 찾으면 다른 과의 식물과 혼동할 수 있다[27]. "
     "Geum rivale은 허브베니트와 같은 곳에 자라며 잡종을 만드는 가까운 종으로, 더 높은 고도와 북쪽에 분포한다[17]. "
     "약초로는 G. rivale 뿌리줄기를 허브베니트와 같은 원료로 보기도 한다[3]. "
     "하지만 뿌리 정유의 주성분은 허브베니트가 유제놀(69.2%), G. rivale이 cis-미르타날(53.3%)로 달랐다[5]. "
     "따라서 두 종의 자료를 섞어 이 종의 값처럼 쓰지 않는다[5]."),
    ("cultivation", "재배와 생육 환경",
     "국내 재배 면적·생산량 통계는 확인하지 못함. "
     "유럽에서는 숲·덤불·산울타리에 흔히 자라고 교란지·정원·공원에도 나며, 영국 큐 왕립식물원의 유전체 표본도 화단 가장자리 잡초 사이에서 채집했다[6]. "
     "약초용 뿌리줄기는 10–11월이나 3월에 캐서 씻고 초록 부분을 떼어 낸 뒤 35 °C 이하에서 말린다[3]. "
     "식용 연구에 쓴 잎은 생육 초기인 5월에 땄다[3]. "
     "이 연구는 이 식물이 곰팡이병·병원균에 강해 농약 없이 기를 수 있다고 적었으나, 잔류 농약을 직접 측정한 결과는 본문에서 확인하지 못함[3].\n\n"
     "생육 연구에 따르면 허브베니트는 그늘진 숲 하층에 적응했지만 빛과 질소가 충분할 때 더 잘 자란다[18, 33]. "
     "위도 860 km에 걸친 이식·가온 실험에서 성체는 실험적 가온에서 대체로 더 잘 자랐다[34]. "
     "한 야외 연구에서는 이 식물이 해충이 아닌 가루이의 겨울나기 장소가 되어 양배추 가루이의 천적을 늘리는 식물로 시험되었다(번데기 1 m²당 평균 166.22개)[30]. "
     "잎은 젖소 사료 첨가물로도 시험되었으며, 시험관 반추위 발효에서 메탄과 암모니아 생성을 줄였다[29]."),
    ("processing", "가공과 이용",
     "전통적으로는 뿌리·뿌리줄기와 지상부를 달이거나 우려 마시고, 입 헹굼·외용에도 썼다[3, 7, 9]. "
     "뿌리줄기 추출물·달임액은 위장 질환에 안으로 쓰고, 생원료로 만든 달임액 등은 상처·입 헹굼·피부염 등에 바깥으로 쓴다고 정리되어 있다[3]. "
     "보완의학에서는 발효로 뿌리 추출물을 얻기도 하며, 생뿌리와 발효 뿌리 추출물에서 드문 엘라지타닌 황산 결합체가 확인되었다[10]. "
     "어린 잎은 샐러드·요리·음료 재료로 쓸 수 있다는 제안이 있다[3].\n\n"
     "가공 원료의 성분 연구로, 독일에서 산 말린 뿌리를 끓는 물로 우린 추출물의 총 페놀은 7,249 mg GAE/L였고 엘라그산 유도체와 페둔쿨라긴·카수아리닌·제민 A 등 엘라지타닌이 많았다[4]. "
     "이 추출물은 시험관에서 α-글루코시다아제를 아카보스보다 강하게 억제했고(IC50 3.76 μg/mL 대 493 μg/mL), α-아밀라아제는 300 μg/mL까지 억제하지 않았다[4]. "
     "달걀(닭 배아) 모델에서 혈당을 3.9% 낮췄고, 녹말 먹이를 먹인 초파리의 중성지방을 줄였다[4]. "
     "뿌리 우린 물을 사람 대변 미생물과 배양하면 유로리틴 A·B·C가 생겼다[26]. "
     "지상부를 섞은 5종 혼합 처방의 쥐 실험도 있으나 혼합물 결과이므로 이 종의 효과로 볼 수 없다[31]. "
     "이 종을 원료로 한 국내 제품 생산실적은 확인하지 못함."),
    ("genetics", "유전체와 유전 다양성",
     "허브베니트는 오래된 6배체(2n = 42)이지만 유전적으로는 대체로 2배체처럼 행동한다[6]. "
     "영국 큐 왕립식물원에서 채집한 개체의 유전체 크기(1C)는 유세포 분석으로 1.64 pg(약 1,610 Mb)로 추정되었다[6]. "
     "조립된 유전체는 1,304.9 Mb이며 99.95%가 염색체 21개에 배정되었고, 단백질 암호 유전자 50,336개가 주석되었다[6]. "
     "미토콘드리아 유전체는 335.5 kb, 엽록체 유전체는 156.1 kb였다[6]. "
     "이 종은 다른 종의 교잡으로 생긴 이질 6배체로 다뤄지며, 632개체 실험에서 자가수분 자손과 타가수분 자손의 성적 차이가 거의 없었다[15].\n\n"
     "타가수분을 하는 Geum rivale과 제꽃가루받이를 하는 허브베니트는 약 200만–300만 년 전에 갈라졌고, 잡종이 생겨도 두 종 사이 유전자 흐름은 극히 적었다[13]. "
     "두 종이 함께 자라는 곳의 잡종 집단에는 F1과 G. rivale 쪽 역교잡 개체만 있었고, F1의 꽃가루 임성은 부모 종보다 30% 낮았다[14]. "
     "숲 조각들에 흩어진 집단의 미세위성 분석에서는 집단 크기와 경관 연결성이 집단 내 유전 다양성을 가장 잘 설명했다[16]."),
    ("safety", "안전성과 주의",
     "식약처 「식품원료 목록」상 허브베니트는 '사용가능' 원료로, 사용 부위는 뿌리와 잎으로 한정된다[1]. "
     "식품의약품안전처·EFSA 등 공공기관의 이 종에 대한 별도 안전성 평가나 알레르기·잔류 정보는 확인하지 못함. "
     "EU 신규식품 목록상 지위도 확인하지 못함.\n\n"
     "동물 독성 자료로는, 불가리아산 지상부 에틸아세테이트 추출물을 OECD 423 지침에 따라 생쥐에 20·70·210 mg/kg 먹였을 때 급성 독성 징후와 간·신장 조직 변화가 없었다[7]. "
     "다른 연구에서는 지상부 에틸아세테이트 추출물을 항균 최소 농도의 10배로 써도 생체 피부 자극 시험의 1차 자극 지수가 0이었다[28]. "
     "이 결과는 추출물 단회 투여·외용 시험이므로, 잎·뿌리를 오래 먹었을 때의 안전성을 보여 주지는 않는다[7, 28]. "
     "뿌리줄기는 탄닌이 약 20%로 많고[3], 땅속 부위 정유의 주성분이 유제놀이다[5]. "
     "탄닌이 많은 약초의 장기 섭취나 유제놀 섭취량에 관한 이 종의 자료는 확인하지 못함. "
     "세포 독성·항균·항산화 결과(예: 방광암 세포 IC50 21.33–25.28 μg/mL)는 시험관 결과로, 사람에서의 효과나 안전성을 뜻하지 않는다[7, 8, 32]. "
     "임신·수유부, 약물 상호작용에 관한 자료는 확인하지 못함."),
]

compounds = [
    dict(name="Gemin A", name_ko="제민 A", class_="엘라지타닌(2량체)", role="marker", part="어린 생잎(5월 채취); 뿌리",
         content_text="생잎 총 폴리페놀(생체 100 g당 2.1 g)의 72%[3]; 뿌리 원료에서 가장 많은 성분(수치는 초록에서 확인하지 못함)[9]",
         activity_ko="자극된 사람 호중구에서 CD11b 발현과 활성산소 방출을 줄임(시험관)[9]", source=[3, 9]),
    dict(name="Eugenol", name_ko="유제놀", class_="페닐프로파노이드(정유 성분)", role="marker", part="땅속 부위(뿌리·뿌리줄기) 정유",
         content_text="정유의 69.2%(폴란드산, 주성분)[5]",
         activity_ko="뿌리 특유의 정향 비슷한 냄새 성분; G. rivale 뿌리 정유(cis-미르타날 53.3%)와 가르는 성분[5]", source=[5]),
    dict(name="Gein", name_ko="게인(유제놀 배당체)", class_="페놀 배당체", role="bioactive", part="뿌리줄기",
         content_text="함량 수치는 확인하지 못함; 뿌리줄기 성분으로 정리됨[3]",
         activity_ko="1950년대에 교잡 유전·정량 연구가 있으나 원문을 확인하지 못함[23, 24]", source=[3, 23, 24]),
    dict(name="Pedunculagin", name_ko="페둔쿨라긴", class_="엘라지타닌", role="bioactive", part="뿌리",
         content_text="함량 수치는 확인하지 못함; 뿌리 물 추출물의 주요 성분으로 동정(HPLC-MS)[4, 9]",
         activity_ko="뿌리 추출물의 α-글루코시다아제 억제와 관련된 후보 성분(단독 시험은 없음)[4]", source=[4, 9]),
    dict(name="Casuarinin", name_ko="카수아리닌", class_="엘라지타닌(C-배당체형)", role="bioactive", part="뿌리",
         content_text="함량 수치는 확인하지 못함; 뿌리 추출물에서 동정[4, 9]",
         activity_ko="이 종에서 단독 활성 자료는 확인하지 못함[4]", source=[4, 9]),
    dict(name="Stachyurin", name_ko="스타키우린", class_="엘라지타닌(C-배당체형)", role="bioactive", part="뿌리",
         content_text="함량 수치는 확인하지 못함; 뿌리 추출물에서 동정[4, 9]",
         activity_ko="이 종에서 단독 활성 자료는 확인하지 못함[4]", source=[4, 9]),
    dict(name="Ellagic acid", name_ko="엘라그산", class_="페놀산(엘라지타닌 가수분해물)", role="bioactive", part="뿌리",
         content_text="함량 수치는 확인하지 못함; 뿌리 물 추출물에 엘라그산과 메틸 유도체가 많음[4]",
         activity_ko="엘라지타닌이 장내 미생물에 의해 유로리틴으로 바뀌는 중간 단계 물질[26]", source=[4, 26]),
    dict(name="Chlorogenic acid", name_ko="클로로겐산류", class_="하이드록시신남산 에스터", role="bioactive", part="어린 생잎",
         content_text="생잎 총 폴리페놀의 8%(클로로겐산류 합계)[3]",
         activity_ko="이 종에서 단독 활성 자료는 확인하지 못함[3]", source=[3]),
    dict(name="(Z)-3-Hexen-1-ol", name_ko="(Z)-3-헥센올", class_="지방족 알코올(녹엽 휘발 성분)", role="bioactive", part="지상부 정유",
         content_text="지상부 정유의 38.4%(주성분)[5]",
         activity_ko="풀 냄새 성분; 생리활성 자료는 확인하지 못함[5]", source=[5]),
    dict(name="Tormentic acid", name_ko="토멘틱산", class_="트리테르펜산", role="bioactive", part="뿌리·지상부 메탄올 추출물의 에틸아세테이트 분획",
         content_text="함량 수치는 확인하지 못함; 이 종에서 새로 확인[8]",
         activity_ko="분리 성분의 개별 활성은 초록에서 확인하지 못함[8]", source=[8]),
    dict(name="Niga-ichigoside F1", name_ko="니가이치고사이드 F1", class_="트리테르펜 배당체", role="bioactive", part="뿌리·지상부 메탄올 추출물의 에틸아세테이트 분획",
         content_text="함량 수치는 확인하지 못함; 이 종에서 새로 확인[8]",
         activity_ko="분리 성분의 개별 활성은 초록에서 확인하지 못함[8]", source=[8]),
    dict(name="Vicianose", name_ko="비시아노스", class_="이당류", role="bioactive", part="뿌리",
         content_text="함량 수치는 확인하지 못함(초록 없음)[25]",
         activity_ko="뿌리에서 분리 보고(1972년); 활성은 확인하지 못함[25]", source=[25]),
    dict(name="Ascorbic acid", name_ko="비타민 C", class_="수용성 비타민", role="nutrient", part="어린 생잎(5월 채취)",
         content_text="생체 100 g당 0.1 g(함께 분석한 3종 모두 같은 값으로 보고)[3]",
         activity_ko="영양 성분[3]", source=[3]),
    dict(name="Linoleic acid", name_ko="리놀레산", class_="불포화 지방산", role="nutrient", part="씨앗(식품 사용 부위 아님)",
         content_text="함량 수치는 초록에서 확인하지 못함; 같은 속 다른 1종과 함께 분석한 두 종 씨앗 모두에서 지방산 중 리놀레산·리놀렌산이 가장 많음[12]",
         activity_ko="씨앗은 식약처 목록의 사용 부위가 아님[1, 12]", source=[12, 1]),
]
for c in compounds:
    c["class"] = c.pop("class_")
compounds = [{k: c[k] for k in ("name", "name_ko", "class", "role", "part", "content_text", "activity_ko", "source")} for c in compounds]

EMPTY = {k: "" for k in ("instrument", "column", "mobile_phase", "gradient", "flow", "temp", "detection", "injection",
                         "sample_prep", "standard", "linearity", "lod", "loq", "recovery")}

assays = [
    dict(role="literature", compound="Gemin A", compound_ko="제민 A", part="잎(어린 생잎, 5월 채취)",
         content="총 폴리페놀 생체 100 g당 2.1 g 중 72%(엘라지타닌은 아그리모닌 표준물질로 환산)[3]",
         method="UHPLC-DAD-MS(Orbitrap)",
         conditions=dict(EMPTY, instrument="Dionex Ultimate 3000 UHPLC, DAD + Q Exactive Orbitrap(H-ESI, 음이온 모드)",
                         column="Phenomenex Luna C18(2) 100 Å, 250 × 4.6 mm, 5 µm(같은 재질 전처리 칼럼 4 × 3 mm)",
                         mobile_phase="A: 1% 포름산 수용액, B: 아세토니트릴/메탄올/물(83/20/17)",
                         gradient="0–6분 5% B; 6–36분 5–28% B; 36–73분 28–73% B; 48–54분 73% B; 54–60분 73–5% B; 60–70분 5% B(원문 그대로, 구간 겹침 있음)",
                         flow="1 mL/min", temp="35 °C", detection="250·280·320·360 nm; MS m/z 200–2000",
                         injection="20 µL",
                         sample_prep="70% 메탄올(0.1% 포름산)로 초음파 3회, 이어 70% 아세톤(0.1% 포름산)으로 3회 추출 후 합침",
                         standard="아그리모닌(엘라지타닌 환산), 엘라그산, 클로로겐산, 퀘르세틴 배당체 등"),
         rationale="잎 폴리페놀의 72%를 차지하는 대표 엘라지타닌이며 뿌리에서도 가장 많은 성분으로 보고되어 이 종의 지표로 쓸 만하다[3, 9]. 직선성·검출한계·회수율은 원문에 없음.",
         source=[3, 9], url=pmc("PMC12693333"), source_kind="paper"),
    dict(role="literature", compound="Ellagitannins and ellagic acid derivatives (total phenolics)", compound_ko="엘라지타닌·엘라그산 유도체(총 페놀)",
         part="뿌리(말린 시판 원료, 끓는 물 추출)",
         content="총 페놀 7,249 ± 132 mg GAE/L(Folin-Ciocalteu, 추출물 기준); 개별 성분은 동정만 하고 정량하지 않음[4]",
         method="HPLC-DAD/HRMS(LTQ Orbitrap)",
         conditions=dict(EMPTY, instrument="Thermo Surveyor HPLC, DAD + LTQ Orbitrap Velos(ESI·APCI, 양·음이온)",
                         column="Thermo Accucore C18, 150 × 3.0 mm, 2.6 µm",
                         mobile_phase="A: 0.1% 포름산 수용액, B: 0.1% 포름산 아세토니트릴",
                         gradient="시작 95% A; 17분에 80% B로 3분 유지; 20분에 B 5%로 낮춰 25분까지(원문 그대로)",
                         flow="0.5 mL/min", temp="40 °C", detection="260 nm; MS m/z 100–1,000, 분해능 30,000",
                         injection="1 µL",
                         sample_prep="분쇄한 말린 뿌리 3 g + 끓는 증류수 30 mL, 1분 교반·1분 초음파, 2,000 × g 원심분리 후 여과",
                         standard="총 페놀은 갈산 검량선; 개별 성분은 고분해능 질량과 문헌 비교로 동정"),
         rationale="뿌리 물 추출물의 주요 페놀(갈산, 페둔쿨라긴, 스테노필라닌 A, 스타키우린, 카수아리닌, 제민 A, 엘라그산과 메틸 유도체)을 피크별로 동정해 품질 확인용 지문으로 쓸 수 있다[4]. 개별 정량값·검출한계·회수율은 원문에 없음.",
         source=[4], url=pmc("PMC8715001"), source_kind="paper"),
    dict(role="literature", compound="Eugenol", compound_ko="유제놀", part="뿌리(땅속 부위) 정유",
         content="정유의 69.2%[5]", method="GC-MS(초록 기준; 세부 조건 확인 못함)",
         conditions=dict(EMPTY),
         rationale="땅속 부위 정유의 주성분이고 근연종 G. rivale 뿌리 정유(cis-미르타날 주성분)와 구별되는 성분이다[5]. 전문 확인 못함 — 분석 조건은 비워 둠.",
         source=[5], url=pm("23738465"), source_kind="paper"),
]

nutrients = [
    dict(form="어린 생잎(5월 채취; 총 식이섬유는 초록 8.2 g, 본문 8 g)", basis="생체 100 g당",
         items=[dict(name="건물(dry weight)", value=18.7, unit="g"),
                dict(name="총 식이섬유", value=8.2, unit="g"),
                dict(name="비타민 C", value=0.1, unit="g"),
                dict(name="총 폴리페놀", value=2.1, unit="g")],
         source=[3]),
]

d = dict(
    slug="geum-urbanum",
    name_ko="허브베니트",
    name_en="Wood avens (Herb bennet)",
    scientific_name="Geum urbanum L.",
    aliases=["허브베니트뿌리", "허브베니트잎", "Wood avens", "Herb bennet", "St. Benedict's herb", "avens root(뿌리 생약명)"],
    sections=[dict(key=k, title=t, body=b) for k, t, b in sections],
    compounds=compounds,
    markers=[],
    assays=assays,
    nutrients=nutrients,
    production=[],
    world=[],
    gi=[],
    orgs=[],
    sources=[dict(n=n, title=t, url=u, publisher=p, accessed=a) for n, t, u, p, a in S],
)
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in d["sections"]:
    print(s["key"], len(s["body"]))
