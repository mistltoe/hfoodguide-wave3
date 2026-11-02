import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
A = "2026-11-02"
def pm(n, title, doi, note):
    return {"n": n, "title": f"{title} ({note})", "url": f"https://doi.org/{doi}", "publisher": "PubMed", "accessed": A}
sources = [
 {"n": 1, "title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 브라질구와바열매(Psidium guineense Sw. / Psidium molle Bertol / Psidium schiedeanum Berg. / Psidium araca Raddi; Brazilian Guava), 사용가능, 사용가능부위: 열매; 같은 속 구아바(Psidium guajava L., 잎·열매)·Costa Rican Guava열매(Psidium friedrichsthalianum)·Strawberry guave열매(Psidium littorale / P. cattleianum) 행과 파인애플구아바(Feijoa sellowiana) 행 대조 (로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json)", "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
 pm(2, "Volatile Constituents of Some Myrtaceous Edible and Medicinal Fruits from the Brazilian Amazon — Foods 2024;13(10):1490", "10.3390/foods13101490", "PMID 38790790, PMC11119775, 전문 확인"),
 pm(3, "Phenolic constituents and antioxidant capacity of four underutilized fruits from the Amazon region — J Agric Food Chem 2011;59(14):7688-7699", "10.1021/jf201039r", "PMID 21662239, 초록 확인"),
 pm(4, "Chemical variability in the essential oil of leaves of Araçá (Psidium guineense Sw.), with occurrence in the Amazon — Chem Cent J 2018;12(1):52", "10.1186/s13065-018-0428-z", "PMID 29748791, PMC5945564, 전문 확인"),
 pm(5, "DNA Barcode, chemical analysis, and antioxidant activity of Psidium guineense from Ecuador — PLoS One 2025;20(3):e0319524 (참고문헌 1 조판 오류 정정 재게재: PMID 40472314)", "10.1371/journal.pone.0319524", "PMID 40106513, PMC11922285, 전문 확인"),
 pm(6, "Refinement of the karyological aspects of Psidium guineense (Swartz, 1788): a comparison with Psidium guajava (Linnaeus, 1753) — Comp Cytogenet 2016;10(1):117-128", "10.3897/CompCytogen.v10i1.6462", "PMID 27186342, PMC4856930, 초록 확인"),
 pm(7, "Genomic and epigenomic variation in Psidium species and their outcome under the yield and composition of essential oils — Sci Rep 2023;13(1):1385", "10.1038/s41598-023-27912-w", "PMID 36697447, PMC9876884, 초록 확인"),
 pm(8, "Genetic Diversity and Population Structure of Psidium Species from Restinga: A Coastal and Disturbed Ecosystem of the Brazilian Atlantic Forest — Biochem Genet 2022;60(6):2503-2514", "10.1007/s10528-022-10222-7", "PMID 35577994, 초록 확인"),
 pm(9, "Genetic divergence among Psidium accessions based on single nucleotide polymorphisms developed for Eucalyptus — Genet Mol Res 2017;16(2)", "10.4238/gmr16029566", "PMID 28481401, 초록 확인"),
 pm(10, "Local knowledge as a tool for prospecting wild food plants: experiences in northeastern Brazil — Sci Rep 2021;11(1):594", "10.1038/s41598-020-79835-5", "PMID 33436748, PMC7804287, 초록 확인"),
 pm(11, "The chemopreventive effects of native Brazilian plants on stomach cancer: A review of the last 25 years — Oncoscience 2025;12:36-51", "10.18632/oncoscience.618", "PMID 40343252, PMC12060929, 전문 확인"),
 pm(12, "Chemical analysis and antioxidant, anti-inflammatory and toxicological evaluations of the hydromethanolic extract of Psidium guineense Swartz leaves — J Ethnopharmacol 2021;281:114492", "10.1016/j.jep.2021.114492", "PMID 34380066, 초록 확인"),
 pm(13, "Phytochemical characterization, safety assessment and antinociceptive activity of Psidium guineense Sw. leaf extract — J Ethnopharmacol 2026;374(Pt 2):122409", "10.1016/j.jep.2026.122409", "PMID 42790555, 초록 확인"),
 pm(14, "Antioxidant, anti-inflammatory, antiproliferative and antimycobacterial activities of the essential oil of Psidium guineense Sw. and spathulenol — J Ethnopharmacol 2017;210:351-358", "10.1016/j.jep.2017.08.030", "PMID 28844678, 초록 확인"),
 pm(15, "Therapeutic indications, chemical composition and biological activity of native Brazilian species from Psidium genus (Myrtaceae): A review — J Ethnopharmacol 2021;278:114248", "10.1016/j.jep.2021.114248", "PMID 34058313, 초록 확인"),
 pm(16, "Screening of plants used in Argentine folk medicine for antimicrobial activity — J Ethnopharmacol 1993;39(2):119-128", "10.1016/0378-8741(93)90027-3", "PMID 8412245, 초록 확인"),
 pm(17, "In vitro synergistic effect of Psidium guineense (Swartz) in combination with antimicrobial agents against methicillin-resistant Staphylococcus aureus strains — ScientificWorldJournal 2012:158237", "10.1100/2012/158237", "PMID 22619603, PMC3349319, 초록 확인"),
 pm(18, "Optimization of the green synthesis of gold nanorods using aqueous extract of peeled sour guava as a source of antioxidants — PLoS One 2025;20(1):e0313485 (PubMed 초록 표기 학명 Psidium araca)", "10.1371/journal.pone.0313485", "PMID 39775354, PMC11709274, 전문 확인"),
 pm(19, "Targeted Metabolomic Analysis of Polyphenols with Antioxidant Activity in Sour Guava (Psidium friedrichsthalianum Nied.) Fruit — Molecules 2016;22(1):11", "10.3390/molecules22010011", "PMID 28025550, PMC6155605, 초록 확인"),
 pm(20, "First Report of Psittacanthus angustifolius on Psidium guineense and Pinus tecunumanii in Honduras — Plant Dis 2001;85(10):1120", "10.1094/PDIS.2001.85.10.1120A", "PMID 30823291, 초록 확인"),
 pm(21, "Antidepressant-Like Effect and Phenolic Profile of Brazilian Native and Exotic Species from Psidium Genus — Chem Biodivers 2022;19(11):e202200242", "10.1002/cbdv.202200242", "PMID 36227271, 초록 확인"),
 pm(22, "Seasonal variation of phytochemicals, antioxidant and photoprotective activities from Psidium guineense Sw aqueous leaves extracts — Nat Prod Res 2025;40(14):4060-4067", "10.1080/14786419.2025.2498074", "PMID 40323676, 초록 확인"),
 pm(23, "Araçain, a tyrosol derivative and other phytochemicals from Psidium guineense Sw. — Nat Prod Res 2021;35(14):2424-2428", "10.1080/14786419.2019.1672683", "PMID 31581838, 초록 확인"),
 pm(24, "First complete NMR data and theoretical study of an antimicrobial formylated dihydrochalcone from Psidium guineense Sw. — Nat Prod Res 2022;36(1):419-423", "10.1080/14786419.2020.1771709", "PMID 32525709, 초록 확인"),
 pm(25, "Contribution of spathulenol to the anti-nociceptive effects of Psidium guineense — Nutr Neurosci 2022;25(4):812-822", "10.1080/1028415X.2020.1815330", "PMID 32912110, 초록 확인"),
 pm(26, "The antimosquito properties of extracts from flowering plants in South Africa — Trop Biomed 2013;30(4):559-569", "10.1016/j.jep.2017.08.030", "PMID 24522123, 초록 확인"),
]
# 26 has no DOI: use PubMed URL
sources[25]["url"] = "https://pubmed.ncbi.nlm.nih.gov/24522123/"

sections = [
 {"key": "overview", "title": "한눈에 보기", "body":
  "브라질구와바(Psidium guineense)는 도금양과(Myrtaceae) 구아바속의 작은 나무로, 멕시코와 서인도제도에서 브라질을 거쳐 아르헨티나까지 자란다[2]. 식약처 「식품원료 목록」에는 원료명 '브라질구와바열매'(학명 Psidium guineense Sw. / Psidium molle Bertol / Psidium schiedeanum Berg. / Psidium araca Raddi, 영어명 Brazilian Guava)로 한 행이 올라 있다[1]. 이 행은 사용가능 원료이고 사용 조건이 '사용가능부위 : 열매'라서 잎은 이 목록으로 식품에 쓸 수 없다[1]. 같은 속 구아바(P. guajava)는 잎과 열매를 모두 쓸 수 있게 따로 올라 있으니 두 종을 섞어 읽지 않아야 한다[1]. 원료 카드에는 EU 신규식품(Novel Food) 목록 표시가 있으나, EU 원문에서 그 지위와 조건은 확인하지 못함.\n\n"
  "열매는 지름 약 4 cm의 노란빛 도는 흰 장과로 과육이 꽤 시고, 날로 먹거나 청량음료·아이스크림·과자·리큐어에 쓴다[2]. 과육 향기는 리모넨과 에틸 부타노에이트가 주를 이루고, 열매에는 가수분해형 탄닌과 플라보놀이 들어 있다[2, 3]. 이 종의 약리 연구는 대부분 잎과 잎 정유로 한 것이어서, 식품원료인 열매의 효과로 옮겨 읽을 수 없다[11, 12, 15]."},
 {"key": "history", "title": "역사", "body":
  "종소명 guineense(기니의)는 스와르츠가 이 식물이 아프리카에서 앤틸리스 제도로 들어왔다고 잘못 여겨 붙인 이름이며, 실제로는 아메리카 원산이다[2]. 브라질에서는 아라사(araçá)·아라사두캄푸(araçá-do-campo)·아라사베르다데이루(araçá-verdadeiro) 등으로 부르고, 에콰도르에서는 과야비야(guayabilla)라고 부른다[4, 5, 11, 25]. 브라질 민간에서는 잎을 소화 장애·감염·염증·설사에 써 왔고, 열매와 잎을 함께 염증과 통증에 쓴다는 기록도 있다[13, 23, 25]. 아르헨티나 민간약 132종 추출물을 조사한 1993년 연구에는 이 종의 열매 껍질이 들어 있었다[16].\n\n"
  "브라질 토착 구아바속 13종을 정리한 리뷰는 그중 6종이 민간약으로 쓰이고 소화기 질환이 주된 쓰임이라고 정리했다[15]. 브라질 북동부 한 농촌 정착지의 주민 지식을 조사한 연구에서는 야생 식용식물 가운데 이 종이 보급 가능성이 가장 높은 종에 들었다[10]. 한국에서 이 열매를 먹어 온 기록이나 유통 역사는 확인하지 못함."},
 {"key": "biology", "title": "식물학적 특징", "body":
  "아마존 시료를 기재한 연구에 따르면 키는 0.7–6.0 m로 다양하고, 잎은 타원형이나 거꿀달걀형으로 길이 8–15 cm, 너비 4–7 cm이며 뒷면에 털이 더 많다[2]. 꽃은 잎겨드랑이에 홀로 피거나 3송이까지 모여 피고, 흰 꽃잎에 수술이 약 200개다[2]. 아마존에서는 6–12월에 꽃이 피고 10–3월에 열매가 익는다[2]. 열매는 지름 약 4 cm의 둥근 장과로 2–3 mm의 단단한 씨가 많고 과육은 크림빛 흰색이다[2].\n\n"
  "에콰도르 건조림 개체는 키 5 m까지의 관목이나 소교목이었고, 잎 7–11 × 3–7 cm, 측맥 7–11쌍, 수술 150–300개, 열매 지름 1–3 cm, 외과피 두께 1–2.5 mm로 기재되었다[5]. 같은 논문의 서론은 열매를 노란 껍질과 연노랑 과육을 가진 지름 1.0–2.5 cm 열매로, 맛은 약간 시고 수지 향이 나며 씨는 새와 포유류가 퍼뜨린다고 소개했다[5]. 아마존 잎 정유 연구는 열매 껍질이 노랑·빨강·자주색이고 과육은 희다고 적었다[4]. 열매 크기가 연구마다 1–4 cm로 다르게 적혀 있어 산지와 개체에 따른 차이로 보인다[2, 5]."},
 {"key": "related_species", "title": "이름과 가까운 종", "body":
  "식약처 목록에는 구아바속 원료가 여럿 있다: 구아바(P. guajava)는 잎·열매, Costa Rican Guava열매(P. friedrichsthalianum)와 Strawberry guave열매(P. littorale / P. cattleianum)는 열매만 사용가능이다[1]. '파인애플구아바'는 구아바속이 아니라 Feijoa sellowiana(페이조아) 행이다[1]. 브라질구와바는 4배체(2n = 44)로 2배체 구아바(2n = 22)와 염색체 수가 다르지만, 미세위성 표지의 종간 전이성이 98.6%로 높아 계통적으로 가깝다[6].\n\n"
  "이름 혼동에 주의해야 한다. 식약처 행의 이명 Psidium araca로 적힌 콜롬비아 열매는 영어로 'sour guava'라 불렸는데, 같은 영어 이름이 Costa Rican Guava인 P. friedrichsthalianum에도 쓰인다[18, 19]. 브라질에서 '아라사'는 여러 구아바속 종을 두루 가리키며, 한 리뷰는 P. cattleyanum Sabine과 P. guineense Sw.를 별개 종으로 다룬다[15]. 한 논문은 P. guineense의 명명자를 'Sabine', P. cattleianum을 'Sw.'로 적어 다른 문헌과 반대였으므로 학명과 명명자를 함께 확인하는 것이 좋다[15, 21]. 남아프리카 연구는 이 종을 구아바·딸기구아바·잡종 P. × durbanensis와 나란히 시험했다[26]."},
 {"key": "cultivation", "title": "재배와 산지", "body":
  "브라질구와바는 아마존 전역의 개활지·초지·목초지에서 저절로 자라기도 하고 재배되기도 한다[2]. 브라질에서는 모든 생물군계에서 자라는 토착 관목 또는 소교목으로 정리되며, 에스피리투산투 해안 사구 식생(restinga)에도 집단이 있다[4, 8]. 에콰도르에서는 과야킬 인근 열대 건조림에서 채집되었고, 온두라스에서는 해발 1,800 m의 야생 개체가 겨우살이(Psittacanthus angustifolius)의 드문 숙주로 보고되었다[5, 20]. 남아프리카에서 채집한 식물 추출물 연구에도 이 종이 포함되었다[26].\n\n"
  "에콰도르 논문 서론은 이 종이 23–28 °C에서 잘 자라고 서리에 약해 어린 나무는 −3 °C 아래에서 피해를 입으며, 여러 토양과 해안부터 고지대까지 적응한다고 소개했다[5]. 아마존에서는 산타렝 등 하류 지역의 장터에서 열매가 팔린다[2]. 품종 육성이나 재배 지침, 세계 생산 통계는 확인하지 못함. 국내 재배·생산 통계(통계청 농작물생산조사, 특용작물 생산실적)에서 이 작물은 확인하지 못함."},
 {"key": "processing", "title": "가공과 이용", "body":
  "브라질에서 열매는 날로 먹거나 디저트·음료·아이스크림·리큐어에 쓰인다[2, 11]. 아마존 장터에서 산 열매의 과육(씨와 껍질 제거) 30 g을 동시 증류-추출해 얻은 향기 농축물에서는 리모넨 25.2%, 에틸 부타노에이트 12.1%, epi-β-비사볼올 9.8%, α-피넨 9.2%, 에틸 헥사노에이트 5.9%가 주성분이었다[2]. 같은 연구에서 구아바 과육은 (2E)-헥세날과 헥사날이 주성분이어서 두 열매의 향기 성분 구성이 뚜렷이 갈렸다[2]. 아마존 과일 4종 비교 연구에서 이 열매는 가수분해형 탄닌과 플라보놀의 좋은 공급원이었고, 항산화능은 4종 가운데 세 번째였다[3].\n\n"
  "학명 P. araca로 적힌 콜롬비아 열매를 물로 추출한 연구에서 총페놀은 과육 515.5 mg, 껍질 575.8 mg 갈산당량/생과 100 g(첫날)이었고, 동결건조 추출물은 7일이 지나면 항산화능이 떨어졌다[18]. 이 연구는 그 껍질 추출물을 금 나노막대 합성의 환원제로 쓴 재료 연구다[18]. 식약처 「식품 등의 생산실적」에서 이 종을 원료명으로 한 품목은 확인하지 못함."},
 {"key": "genetics", "title": "유전 정보", "body":
  "유세포 분석에서 브라질구와바의 핵 DNA 양은 2C = 1.85 pg, 염색체는 2n = 4x = 44로 기본수 x = 11의 4배체였고, 구아바는 2C = 0.95 pg, 2n = 2x = 22였다[6]. 구아바속 여러 종을 비교한 연구에서 이 종의 GC 함량은 34.33%로 가장 낮았고, 한 테르펜 합성효소 유전자를 구아바(2개)의 두 배인 4개 지녔다[7]. 이 연구는 배수성에 따른 유전자 수 차이가 잎 정유의 수율·조성과 관련된다고 보았다[7].\n\n"
  "브라질 해안 사구 집단을 미세위성 표지로 본 연구에서 이 종은 대립유전자 81개, 유전 다양도 0.74였고 변이는 집단 안에서 더 컸다(집단 간 분화 Ø 0.21)[8]. 유칼립투스용 SNP 칩으로 구아바속 53점을 분석하자 이 종 3점은 구아바·딸기구아바와 다른 무리를 이루었다[9]. 에콰도르 개체로 엽록체 7개·핵 2개 유전자 부위의 DNA 바코드를 처음 읽었고, 종 수준 구별에는 ITS1·ITS2가 나았다[5]. 아마존 개체 12점의 잎 정유는 세 화학형으로 나뉘었고, 스파툴레놀형을 더해 적어도 네 화학형이 있다[4]. 전체 유전체 해독은 확인하지 못함."},
 {"key": "safety", "title": "안전성", "body":
  "식약처 목록은 이 종의 열매만 식품원료로 허용하므로 잎·잎 추출물·정유는 이 목록으로 식품에 쓸 수 없다[1]. 공공기관(식약처·EFSA 등)이 낸 이 종 열매의 알레르기·잔류농약·독성 성분 정보는 확인하지 못함. 열매 자체의 독성시험이나 사람 섭취 연구는 확인하지 못함.\n\n"
  "확인한 독성 자료는 모두 잎 추출물로 한 동물 시험이다[12, 13]. 잎 수메탄올 추출물을 암컷 쥐에 500·2,000 mg/kg 먹인 급성(14일)·아급성(28일) 시험에서 독성 징후가 없었다[12]. 잎 메탄올 추출물 2,000 mg/kg를 생쥐에 한 번 먹인 OECD 급성독성 시험에서도 사망·행동·혈액·생화학 변화가 없었다[13]. 잎 정유와 그 주성분 스파툴레놀은 세포 실험에서 일부 암세포 증식을 억제했고, 잎 정유는 위암 세포(AGP01)에 IC50 8.2·15.7 μg/mL를 보였으나 모두 세포·동물 결과다[11, 14]. 열매 껍질 열수 추출물과 부위를 밝히지 않은 수추출물의 항균 결과도 시험관 실험이다[16, 17]. 이런 결과를 열매를 먹었을 때의 효과나 안전성으로 옮겨 읽어서는 안 된다[11, 15]."},
]

def c(name, ko, cls, role, part, content, act, src):
    return {"name": name, "name_ko": ko, "class": cls, "role": role, "part": part, "content_text": content, "activity_ko": act, "source": src}
compounds = [
 c("Limonene", "리모넨", "모노테르펜 탄화수소", "marker", "열매 과육(향기 농축물)", "향기 농축물 피크 면적의 25.2%(GC-FID 면적 정규화)[2]", "열매 향기의 최대 성분; 구아바 과육 향기와 구별되는 특징[2]", [2]),
 c("Ethyl butanoate", "에틸 부타노에이트", "지방산 유래 에스터", "bioactive", "열매 과육(향기 농축물)", "12.1%(피크 면적)[2]", "과일 향 에스터; 콜롬비아산 열매에서도 확인됨[2]", [2]),
 c("epi-beta-Bisabolol", "epi-β-비사볼올", "산소화 세스퀴테르펜", "bioactive", "열매 과육(향기 농축물)", "9.8%(피크 면적)[2]", "열매 향기 주성분; 잎 정유 화학형(β-비사볼렌/epi-β-비사볼올형)의 지표이기도 함[2, 4]", [2, 4]),
 c("alpha-Pinene", "α-피넨", "모노테르펜 탄화수소", "bioactive", "열매 과육(향기 농축물)", "9.2%(피크 면적)[2]; 잎 정유 0.1–35.6%(아마존 12개체)[4]", "열매·잎 공통 향기 성분[2, 4]", [2, 4]),
 c("Ethyl hexanoate", "에틸 헥사노에이트", "지방산 유래 에스터", "bioactive", "열매 과육(향기 농축물)", "5.9%(피크 면적)[2]", "과일 향 에스터[2]", [2]),
 c("Hydrolyzable tannins", "가수분해형 탄닌", "폴리페놀(탄닌)", "bioactive", "열매", "개별 함량은 초록에 없음(HPLC/DAD-ESI-MSn 동정)[3]", "열매의 주요 폴리페놀군(플라보놀과 함께); 항산화능은 비교 4종 가운데 세 번째[3]", [3]),
 c("Total phenolics (gallic acid equivalents)", "총페놀(갈산당량)", "폴리페놀 합계", "bioactive", "열매 과육·껍질(수추출물; 학명 P. araca로 기재)", "과육 515.5±193.8, 껍질 575.8±22.8 mg 갈산/생과 100 g(첫날, Folin-Ciocalteu)[18]", "항산화능(ABTS·FRAP·DPPH) 측정; 동결건조 추출물은 7일 뒤 항산화능 감소[18]", [18]),
 c("Ascorbic acid", "비타민 C(아스코르브산)", "수용성 비타민", "nutrient", "열매", "수치 확인하지 못함(원문은 과육이 비타민 C와 페놀 화합물이 풍부하다고만 기술)[4]", "영양 성분; 이 종 열매의 정량값은 확인하지 못함[4]", [4]),
 c("Spathulenol", "스파툴레놀", "산소화 세스퀴테르펜", "bioactive", "잎(정유) — 식품원료 부위 아님", "잎 정유의 80.7%(브라질 도라두스 시료)[14]", "생쥐 부종·흉막염 모델에서 염증 억제, 세포 실험에서 항증식[14]; 생쥐 통증 모델에서 진통[25]", [14, 25]),
 c("Quercetin", "퀘르세틴", "플라보놀", "bioactive", "잎(수추출물) — 식품원료 부위 아님", "잎 수추출물의 주 페놀 성분(함량 초록에 없음)[21]", "생쥐 우울 유사 행동 모델 연구의 주성분으로 제시[21]; 잎 추출물 성분의 계절 변화 연구 대상[22]", [21, 22]),
 c("Gallic acid", "갈산", "페놀산", "bioactive", "잎(수메탄올 추출물) — 식품원료 부위 아님", "UHPLC-MS/MS로 동정(함량 초록에 없음)[12]", "잎 추출물 항산화 성분으로 제시[12, 13]", [12, 13]),
 c("Corilagin", "코릴라긴", "엘라기탄닌", "bioactive", "잎(수메탄올 추출물) — 식품원료 부위 아님", "UHPLC-MS/MS로 동정(함량 초록에 없음)[12]", "잎 추출물 구성 성분[12]", [12]),
 c("Ursolic acid", "우르솔산", "트리테르펜산", "bioactive", "잎 — 식품원료 부위 아님", "분리·동정(함량 초록에 없음)[12, 23]", "잎 추출물 구성 성분[12, 23]", [12, 23]),
 c("3'-Formyl-2',4',6'-trihydroxy-5'-methyldihydrochalcone", "3'-포르밀-2',4',6'-트리하이드록시-5'-메틸다이하이드로칼콘", "포르밀화 다이하이드로칼콘", "bioactive", "잎 추출물(부위는 [12]에서 잎으로 확인)", "분리·동정(함량 초록에 없음)[12, 24]", "녹농균에 대한 시험관 항균 활성[24]", [12, 24]),
 c("Aracain", "아라사인", "티로솔 유도체(2-(4-하이드록시페닐)에틸 헥사노에이트)", "bioactive", "잎 — 식품원료 부위 아님", "천연물로 처음 분리(함량 초록에 없음)[23]", "잎 추출물이 폐렴막대균에 중등도 이상 항균 활성[23]", [23]),
]

assays = [
 {"role": "literature", "compound": "Limonene", "compound_ko": "리모넨(과육 향기 성분 전체 프로파일)", "part": "열매 과육(씨·껍질 제거, 냉동 보관)",
  "content": "향기 농축물 피크 면적의 25.2%; 에틸 부타노에이트 12.1%, epi-β-비사볼올 9.8%, α-피넨 9.2%, 에틸 헥사노에이트 5.9%[2]",
  "method": "GC-MS(동정)·GC-FID(면적 정규화 정량)",
  "conditions": {"instrument": "Shimadzu GCMS-QP2010 Ultra(AOC-20i 자동주입기); 정량은 GC2010 계열 GC-FID", "column": "Rxi-5ms, 30 m × 0.25 mm, 막 두께 0.25 μm (Restek)", "mobile_phase": "운반기체 헬륨, 선속도 36.5 cm/s(1.0 mL/min)", "gradient": "오븐 60–240 °C, 3 °C/min", "flow": "1.0 mL/min", "temp": "주입구 250 °C; 이온원 200 °C, 전달선 250 °C", "detection": "EI 70 eV, m/z 35–400, 0.3초 주사; FID", "injection": "분할 주입 1:20, n-펜탄 용액 1.0–2.0 μL", "sample_prep": "과육 30 g을 Likens–Nickerson형 장치로 2시간 동시 증류-추출(n-펜탄 3 mL), 2회 반복", "standard": "C8–C40 n-알케인으로 머무름 지수 계산, 질량 스펙트럼 라이브러리 대조(외부 표준 정량 아님)", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "열매 향기의 최대 성분이고 구아바 과육(헥세날·헥사날 주성분)과 구별되는 지표라 품질·진위 판별의 실마리가 됨; 면적 백분율이며 절대 함량은 아님; 전문 확인[2].",
  "source": [2], "url": "https://doi.org/10.3390/foods13101490", "source_kind": "paper"},
 {"role": "literature", "compound": "Total phenolics (gallic acid equivalents)", "compound_ko": "총페놀(갈산당량)", "part": "열매 과육·껍질 수추출물(콜롬비아 몬텔리바노산; 학명 Psidium araca로 기재)",
  "content": "과육 515.5±193.8, 껍질 575.8±22.8 mg 갈산/생과 100 g(첫날)[18]",
  "method": "Folin–Ciocalteu 비색법(마이크로플레이트)",
  "conditions": {"instrument": "Multiskan GO 분광광도계(Thermo Scientific)", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "37 °C에서 2시간 반응", "detection": "흡광도 737 nm", "injection": "96웰 플레이트 웰당 250 μL, 3반복", "sample_prep": "과육·껍질 각 50 g + 증류수 200 mL 10분 균질화 → 50–60 °C 20분(400 rpm) → 상온 2시간·4 °C 24시간 → 9000 rpm 10분 원심분리 상등액 → 동결건조; 고형 추출물 120 mg/mL로 녹여 물 7.5 mL·Folin-Ciocalteu 2 N 500 μL·시료 500 μL·20% 탄산나트륨 1.5 mL 혼합", "standard": "갈산 검량선 40–200 mg/mL(원문 단위 그대로)", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "열매 부위별 항산화 물질 양을 비교한 유일한 열매 정량 자료로, 껍질이 과육보다 높았음; 성분 개별 정량이 아닌 합계값이며 식약처 행의 이명 P. araca로 적힌 시료임; 전문 확인[18].",
  "source": [18], "url": "https://doi.org/10.1371/journal.pone.0313485", "source_kind": "paper"},
]

d = {
 "slug": "psidium-guineense",
 "name_ko": "브라질구와바",
 "name_en": "Brazilian guava (araçá, guayabilla)",
 "scientific_name": "Psidium guineense Sw.",
 "aliases": ["브라질구와바열매", "브라질구아바", "Brazilian Guava", "araçá", "araçá-do-campo", "araçá-verdadeiro", "guayabilla", "Psidium molle", "Psidium schiedeanum", "Psidium araca"],
 "sections": sections,
 "compounds": compounds,
 "markers": [],
 "assays": assays,
 "nutrients": [],
 "production": [],
 "world": [],
 "gi": [],
 "orgs": [],
 "sources": sources,
}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in sections: print(s["key"], len(s["body"]))
