import json
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "dossier.json"
ACC = "2026-11-02"
PM = "https://pubmed.ncbi.nlm.nih.gov/{}/"
PMC = "https://pmc.ncbi.nlm.nih.gov/articles/{}/"

sources = [
    (1, "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 퉁퉁마디(Salicornia herbacea L. / Salicornia europaea var. herbacea L.)", "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "식품의약품안전처", "2026-10-13"),
    (2, "Chemical Structure and Biological Activities of Secondary Metabolites from Salicornia europaea L. Molecules. 2021;26(8):2252", PMC.format("PMC8069253"), "MDPI (PMC)", ACC),
    (3, "Protective Effect of Salicornia europaea Extracts on High Salt Intake-Induced Vascular Dysfunction and Hypertension. Int J Mol Sci. 2016;17(7):1176", PMC.format("PMC4964547"), "MDPI (PMC)", ACC),
    (4, "Desalted Salicornia europaea powder and its active constituent, trans-ferulic acid, exert anti-obesity effects by suppressing adipogenic-related factors. Pharm Biol. 2018;56(1):183-191", PMC.format("PMC6130585"), "Taylor & Francis (PMC)", ACC),
    (5, "Effect of desalted Salicornia europaea L. ethanol extract (PM-EE) on the subjects complaining memory dysfunction without dementia: a 12 week, randomized, double-blind, placebo-controlled clinical trial. Sci Rep. 2020;10:19914", PMC.format("PMC7670404"), "Springer Nature (PMC)", ACC),
    (6, "Water Extract of Desalted Salicornia europaea L. Inhibits RANKL-Induced Osteoclast Differentiation and Prevents Bone Loss in Ovariectomized Mice. Nutrients. 2023;15(23):4968", PMC.format("PMC10708358"), "MDPI (PMC)", ACC),
    (7, "Spherical Granule Production from Micronized Saltwort (Salicornia herbacea) Powder as Salt Substitute. Prev Nutr Food Sci. 2013;18(1):60-66", PMC.format("PMC3867153"), "한국식품영양과학회 (PMC)", ACC),
    (8, "Iodine-induced thyrotoxic hypokalemic paralysis after ingestion of Salicornia herbacea. Ren Fail. 2014;36(3):461-463", PM.format("24344747"), "PubMed", ACC),
    (9, "Neuroprotective Effect of Halophyte Salicornia herbacea L. Is Mediated by Activation of Heme Oxygenase-1 in Mouse Hippocampal HT22 Cells. J Med Food. 2017;20(2):140-151", PM.format("28146411"), "PubMed", ACC),
    (10, "Flavanones and Chromones from Salicornia herbacea Mitigate Septic Lethality via Restoration of Vascular Barrier Integrity. J Agric Food Chem. 2015;63(46):10121-10130", PM.format("26522440"), "PubMed", ACC),
    (11, "Evaluation of Salicornia herbacea as a potential antioxidant and anti-inflammatory agent. J Med Food. 2009;12(3):661-668", PM.format("19627218"), "PubMed", ACC),
    (12, "Flavonoid glycosides isolated from Salicornia herbacea inhibit matrix metalloproteinase in HT1080 cells. Toxicol In Vitro. 2008;22(7):1742-1748", PM.format("18715546"), "PubMed", ACC),
    (13, "3-Caffeoyl, 4-dihydrocaffeoylquinic acid from Salicornia herbacea attenuates high glucose-induced hepatic lipogenesis in human HepG2 cells through activation of the LKB1 and SIRT1/AMPK-dependent pathway. Mol Nutr Food Res. 2013", PM.format("23349077"), "PubMed", ACC),
    (14, "Evaluation of novel antioxidant triterpenoid saponins from the halophyte Salicornia herbacea. Bioorg Med Chem Lett. 2012;22(13):4318-4322", PM.format("22652051"), "PubMed", ACC),
    (15, "Two new noroleanane-type triterpene saponins from the methanol extract of Salicornia herbacea. Food Chem. 2014;151:101-109", PM.format("24423508"), "PubMed", ACC),
    (16, "Pentadecyl ferulate, a potent antioxidant and antiproliferative agent from the halophyte Salicornia herbacea. Food Chem. 2013;141(3):2066-2074", PM.format("23870929"), "PubMed", ACC),
    (17, "Salicornia herbacea prevents weight gain and hepatic lipid accumulation in obese ICR mice fed a high-fat diet. J Sci Food Agric. 2015;95(15):3150-3159", PM.format("25523516"), "PubMed", ACC),
    (18, "Hypolipidemic effect of Salicornia herbacea in animal model of type 2 diabetes mellitus. Nutr Res Pract. 2007;1(4):371-375", PMC.format("PMC2849048"), "한국영양학회 (PMC)", ACC),
    (19, "Determination of organic acids in Salicornia herbacea by solid-phase extraction combined with liquid chromatography. Nat Prod Commun. 2013;8(2):203-206", PM.format("23513729"), "PubMed", ACC),
    (20, "A T2T gap-free genome provides insights into tetraploid Salicornia europaea evolution and aquaporin function in stress tolerance. Plant Physiol. 2025;199(3)", PM.format("41206564"), "PubMed", ACC),
    (21, "Chromosome-scale genomes and population resequencing resolve subgenome diversity and halophyte adaptation in Salicornia. Nat Commun. 2026;17", PMC.format("PMC13569856"), "Springer Nature (PMC)", ACC),
    (22, "Multiple compartmentalization of sodium conferred salt tolerance in Salicornia europaea. Plant Physiol Biochem. 2012;51:47-52", PM.format("22153239"), "PubMed", ACC),
    (23, "Effects of red glasswort as sodium chloride substitute on the physicochemical properties of pork loin ham. Asian-Australas J Anim Sci. 2020;33(4):662-669", PMC.format("PMC7054613"), "아시아태평양축산학회 (PMC)", ACC),
    (24, "Effect of glasswort (Salicornia herbacea L.) on the texture of frankfurters. Meat Sci. 2014;97(4):513-517", PM.format("24769151"), "PubMed", ACC),
    (25, "Evaluating the Feasibility of Using Salicornia herbacea Powder as a Salt Substitute in Sausage Production. Food Sci Anim Resour. 2025;45(5):1478", PMC.format("PMC12965255"), "한국축산식품학회 (PMC)", ACC),
    (26, "Effect of encapsulated edible halophyte Salicornia herbacea with different biopolymers on the inhibition of sodium absorption in mouse. Food Sci Nutr. 2021", PMC.format("PMC8020925"), "Wiley (PMC)", ACC),
    (27, "Subacute feeding toxicity of low-sodium sausages manufactured with sodium substitutes and biopolymer-encapsulated saltwort (Salicornia herbacea) in a mouse model. J Sci Food Agric. 2020", PM.format("31612484"), "PubMed", ACC),
    (28, "Production of novel vinegar having antioxidant and anti-fatigue activities from Salicornia herbacea L. J Sci Food Agric. 2016;96(4):1085-1092", PM.format("25800973"), "PubMed", ACC),
    (29, "Ameliorative potential of desalted Salicornia europaea L. extract in multifaceted Alzheimer's-like scopolamine-induced amnesic mice model. Sci Rep. 2018;8:7174", PMC.format("PMC5940894"), "Springer Nature (PMC)", ACC),
    (30, "Synergistic activation of monocytes by polysaccharides isolated from Salicornia herbacea and interferon-gamma. J Ethnopharmacol. 2007;111(2):365-370", PM.format("17204386"), "PubMed", ACC),
    (31, "Extraction, preliminary characterization and antioxidant properties of polysaccharides from the testa of Salicornia herbacea. Carbohydr Polym. 2017;176:99-106", PM.format("28927632"), "PubMed", ACC),
    (32, "Four New Dicaffeoylquinic Acid Derivatives from Glasswort (Salicornia herbacea L.) and Their Antioxidative Activity. Molecules. 2016;21(8):1097", PMC.format("PMC6274184"), "MDPI (PMC)", ACC),
    (33, "Female sex pheromone of the Gelechiid moth Scrobipalpa salinella (Zeller). J Chem Ecol. 2011;37(11):1216-1221", PM.format("22037791"), "PubMed", ACC),
    (34, "Inhibitory effect of 3-caffeoyl-4-dicaffeoylquinic acid from Salicornia herbacea against phorbol ester-induced cyclooxygenase-2 expression in macrophages. Chem Biol Interact. 2009", PM.format("19931518"), "PubMed", ACC),
    (35, "Salicornia herbacea prevents high fat diet-induced hyperglycemia and hyperlipidemia in ICR mice. Arch Pharm Res. 2006;29(3):256-264", PM.format("16597000"), "PubMed", ACC),
]

sections = [
    ("overview", "한눈에 보기", """퉁퉁마디(함초)는 바닷가 갯벌과 염습지에서 자라는 한해살이 염생식물로, 줄기가 마디마디 통통하게 이어지고 잎은 비늘처럼 작게 붙는다[2, 7]. 한국에서는 서해안과 남해안의 염습지에 자라며, 여름까지는 초록색이다가 가을에 붉게 물든다[2, 7]. 맛이 짜서 바닷가 주민들이 양념 채소로 먹어 왔고[35], 분말·환·추출물·식초 같은 가공품으로도 만들어진다[28].

식품의약품안전처 「식품원료 목록」에서 퉁퉁마디는 식품에 사용할 수 있는 원료(사용가능)이며, 사용 조건은 '사용가능부위 : 줄기, 잎'이다[1]. 목록에는 퉁퉁마디잎·퉁퉁마디분말·퉁퉁마디추출액 등 원료명 9개와 이명 '함초', 영문명 Marshfire glasswort가 적혀 있다[1]. 같은 목록 자료에 다른 나라 목록이나 건강기능식품 고시형 원료의 원재료로 표시된 기록은 없다[1].

학명은 목록에 'Salicornia herbacea L. / Salicornia europaea var. herbacea L.'로 함께 적혀 있다[1]. 국내 연구는 같은 식물을 S. herbacea 또는 S. europaea로 적으며, 이 속은 종 구분이 어려워 비슷한 퉁퉁마디류를 S. europaea로 묶어 부르는 경우가 많다[2, 6]. 이 문서는 한국에서 채취·재배한 '함초' 연구를 학명 표기와 함께 인용했고, 같은 속의 S. bigelovii 등 다른 식품원료 자료는 섞지 않았다[1, 2].

가장 큰 특징은 소금이다[4]. 말린 분말은 염화나트륨이 25–35%에 이르러, 탈염 공정을 거친 분말과 추출물이 따로 개발되었다[4, 6].""")
    ,
    ("history", "역사", """퉁퉁마디는 해안 지역 주민이 양념 채소처럼 먹어 온 식물로 소개된다[35]. 한국 서해안 염습지에 자라는 이 식물은 장 질환·신장 질환·간염에 쓰는 민간약으로도 알려졌다[9]. 다른 연구는 변비·비만·당뇨·암 같은 질환에 민간약으로 쓰였다고 적었다[34].

아시아에서는 변비·신장 질환·간염·설사·비만·당뇨에 전통 약재로 쓰였고, 지상부는 샐러드·절임·발효식품·소금 대용으로 이용되었다[2]. 영어로는 glasswort·sea bean·sea asparagus·samphire로 불리며, 식용 외에 유리 제조에도 쓰였다고 소개된다[2]. 두통과 괴혈병에 쓰는 민간약으로 소개한 연구도 있다[3, 6].

열수추출물에서 정제한 다당류가 인터페론-γ와 함께 단핵구 세포를 대식세포로 분화·활성화한다는 연구처럼, 소금 이외 성분의 생리활성도 일찍부터 주목받았다(세포 실험)[30]. 성분 연구는 1978년 일본 홋카이도 노토로 호숫가 시료에서 크로몬을 분리한 보고로 시작해, 2019년까지 89종의 2차 대사산물이 보고되었다[2]. 2005년 부산 해안 시료에서 새 클로로겐산 유도체가 분리되어 퉁퉁마디의 한국 이름을 딴 '퉁퉁마딕산(tungtungmadic acid)'으로 이름 붙었다[2].

국내에서는 높은 염도 때문에 음료로 가공하기 어렵다는 점을 넘기 위해 분말·환·김·추출물 같은 가공품이 개발되었다[28]. 퉁퉁마디가 언제부터 식용으로 기록되었는지에 대한 국내 고문헌 기록은 이번 조사에서 확인하지 못함.""")
    ,
    ("biology", "식물학적 특징", """퉁퉁마디는 비름과(옛 분류 명아주과)에 속하는 한해살이 다육성 염생식물이다[2, 6]. 식품원료 목록은 과명을 명아주과(Chenopodiaceae)로 적고 있고, 최근 논문은 비름과(Amaranthaceae)로 적는다[1, 4]. 줄기는 마디가 이어진 모양이고 잎은 비늘처럼 작아, 계절에 따른 색 변화와 함께 다른 염생식물과 쉽게 구별된다고 소개된다[2].

이 식물은 염도 3%까지 견디며 온대와 아열대의 염습지와 진흙 해안에 널리 자란다[2]. 같은 계열로 묶이는 S. europaea는 염화나트륨 1000 mM 이상을 견디는 가장 내염성이 강한 식물 가운데 하나로, 200–400 mM에서 오히려 생장과 광합성이 가장 좋았다[22]. 이때 나트륨은 뿌리보다 지상부에 훨씬 많이 쌓였고, 주로 지상부 내피 조직 세포의 액포에 격리되었다[22].

이렇게 쌓인 소금 때문에 지상부를 그대로 말린 분말은 염화나트륨이 25–35%에 이른다[4]. 무기질도 많아 한 연구는 마그네슘 1.9 mg/g, 칼슘 1.1 mg/g, 철 0.2 mg/g, 칼륨 5.6 mg/g, 나트륨 10 mg/g을 소개했다[7]. 다만 이 수치의 기준(생체·건물)은 원문에 밝혀 있지 않다[7].

종자 껍질(종피)에서 다당류를 추출해 구성 당과 항산화 활성을 조사한 연구도 있다[31].""")
    ,
    ("related_species", "가까운 종", """퉁퉁마디속(Salicornia)은 형태가 단순하고 변이가 커서 종을 구분하기 어렵다[2]. 그래서 많은 연구가 비슷한 퉁퉁마디류를 S. europaea로 묶어 부르며, 같은 이름의 논문이라도 실제 종이 다를 수 있다는 점을 염두에 두어야 한다[2].

한국 함초 연구의 학명 표기는 두 갈래다[2, 6]. 국내 연구의 다수는 S. herbacea로 적고[9, 10, 11], 서해안이나 신안산 시료를 S. europaea로 적은 논문도 있다[3, 4, 6]. 2021년 리뷰는 'S. europaea L.(S. herbacea L.로도 알려짐)'이라고 적어 두 이름을 같은 식물로 다루었고, 2023년 논문도 같은 방식으로 적었다[2, 6]. 식품원료 목록도 S. herbacea와 S. europaea var. herbacea를 함께 적는다[1].

2026년 연구는 퉁퉁마디속 6종의 염색체 수준 유전체를 해독하고 전 세계 318개 계통을 다시 분석해 종 사이 관계를 정리했다[21]. 이 연구는 기존 참조 유전체인 S. ramosissima(영국)와 S. europaea(중국)의 염색체 번호와 방향도 바로잡았다[21].

식품원료 목록에는 같은 속의 S. bigelovii·S. rubra·S. quinqueflora·S. utahensis·S. virginica가 별도 원료로 올라 있어, 이 문서는 그 종들의 자료를 섞지 않았다[1]. 영어 이름 glasswort는 비슷한 퉁퉁마디류를 두루 가리키는 경우가 많으므로, 이름만으로 같은 종이라고 보아서는 안 된다[2].""")
    ,
    ("cultivation", "재배와 채취", """퉁퉁마디는 서해안과 남해안의 염습지, 간척지, 염전 주변에서 자란다[2, 9]. 성분 연구에 쓰인 국내 시료는 부산·영광·무안·목포·해남(버려진 염전) 등에서 채취한 야생 개체와 신안에서 재배한 개체가 섞여 있다[2]. 신안에서 재배한 함초의 지상부에서 플라바논과 크로몬을 분리한 연구도 있다[2, 10].

가공 연구의 원료 구입처로는 전남 증도와 신안군 업체가 적혀 있다[6, 7]. 퉁퉁마디를 먹는 나방 Scrobipalpa salinella는 갯벌 염습지에서 퉁퉁마디의 중요한 해충으로 소개되었고, 농촌진흥청 연구진이 이 나방의 성페로몬을 밝혀 예찰·방제에 쓸 수 있다고 보고했다[33].

재배 조건에 따라 생장이 달라진다[22]. S. europaea는 염화나트륨 200–400 mM에서 생장과 광합성 속도가 가장 좋았으므로, 바닷물 수준의 염분이 생육을 돕는다[22]. 바닷물로 관개하며 비료·농약 없이 재배할 수 있는 상업 작물로 떠올랐다는 소개도 있다[4].

국내 생산량·재배면적에 대한 공식 통계(통계청·해양수산부)는 이번 조사에서 확인하지 못함. 지리적 표시 등록 자료(국립농산물품질관리원·국립수산물품질관리원)에서도 퉁퉁마디 항목은 확인하지 못함.""")
    ,
    ("processing", "가공과 이용", """퉁퉁마디는 생채·무침으로 먹고, 분말·환·김·추출물·식초로 가공된다[2, 28]. 그러나 염도가 높아 음료로 만들기 어렵다는 문제가 있어, 현미를 이용한 2단 발효로 유기산과 무기질이 많은 함초 식초를 만든 연구가 있다[28].

탈염 가공이 핵심 공정이다[4]. 한 연구는 원물 20.0 kg을 동결건조·분쇄한 분말 3.6 kg을 물로 추출·원심분리해 염분을 빼고, 침전물을 동결건조·미분쇄해 탈염 분말 2.4 kg을 얻었다[4]. 이 탈염 분말은 식이섬유 74.27%, 조단백 9.13%, 조지방 4.36%, 회분 6.23%, 나트륨 0.71%였다[4]. 다른 연구는 신안산 건조 지상부 1.3 kg을 상온의 물 52 L에 1시간 담갔다가 물을 빼서 염분을 줄인 뒤, 95 °C 열수 19.5 L로 5시간 추출·농축·분무건조했다[6]. 70% 에탄올 추출 후 100% 에탄올로 탈염한 추출물[18], 탈염 뒤 효소 처리한 에탄올 추출물[29]도 쓰였다.

반대로 짠맛을 살려 소금 대용으로 쓰는 연구도 많다[7, 24]. 미분쇄 분말을 유동층 코팅기로 구형 과립으로 만든 함초 과립의 상대 짠맛은 소금 대비 0.39였다[7]. 소시지에 소금 0.75%와 함초 1.5%를 쓰면 소금 1.5% 대조군과 조직감이 비슷했다[24]. 붉은 함초 분말로 햄의 소금을 대신하면 염 농도와 전단력이 줄고 연도·다즙성 점수는 높았다[23]. 2025년 연구는 세 종류 소시지 모두에서 함초 분말을 소금 대용으로 쓸 수 있다고 보았다[25].

식약처 「식품 등의 생산실적」에서 퉁퉁마디 원료 항목의 생산실적은 이번 조사에서 확인하지 못함.""")
    ,
    ("genetics", "유전체와 육종", """퉁퉁마디속은 2배체와 4배체가 섞여 있다[20, 21]. 중국 S. europaea는 2n = 4x = 36인 4배체로, 2025년 텔로미어에서 텔로미어까지 끊김 없는(T2T) 유전체가 984.58 Mb, 단백질 암호화 유전자 41,963개로 해독되었다[20]. 이 유전체의 70.11%가 반복서열이었고 그중 전이인자가 가장 많았다[20].

같은 연구는 액포막 수분통로 유전자 SeTIP2;1·SeTIP2;2·SeTIP2;4를 애기장대에 넣으면 염분·가뭄 내성이 높아진다고 보고했다[20]. 나트륨을 액포에 격리하는 데에는 SeNHX1·SeVHA-A·SeVP1 유전자의 발현 증가가 관여한다[22].

2026년에는 퉁퉁마디속 6종의 염색체 수준 유전체와 318개 계통의 재분석으로 네 가지 아유전체가 구분되었다[21]. 북미 계통은 Gypsy 레트로트랜스포존 증가로 유전체가 커졌고, 6A 염색체의 OSCA 칼슘 통로 유전자가 삼투 적응 후보로 제시되었다[21]. 연구진은 이 자료를 바탕으로 앞으로의 작물 육종에 쓸 유전자원 수집도 정리했다[21].

한국 함초 집단의 배수성과 유전체 정보, 국내 품종 등록 여부는 이번 조사에서 확인하지 못함.""")
    ,
    ("safety", "안전성", """가장 먼저 짚어야 할 점은 나트륨이다[4]. 탈염하지 않은 분말은 염화나트륨이 25–35%이고, 열수추출 후 정제·분무건조한 추출 분말은 염화나트륨이 55.6%였다[3, 4]. 따라서 함초 분말을 소금 대신 쓰더라도 나트륨 섭취는 줄지 않을 수 있으며, 탈염 분말의 나트륨은 0.71%로 크게 낮았다[4].

동물 연구에서 같은 양의 나트륨을 함초 추출 분말로 준 정상혈압 쥐는 정제염을 준 쥐보다 수축기 혈압과 평균 동맥압이 낮았고, 고혈압 쥐에서는 평균 동맥압만 낮았다[3]. 키토산으로 감싼 함초는 생쥐에서 나트륨 흡수를 19% 줄였다는 보고도 있다[26]. 이 결과들은 동물 실험이며 사람에서 확인된 것은 아니다[3, 26].

요오드 과다에 주의가 필요하다[8]. 당뇨와 고혈압 치료 목적으로 함초를 먹던 56세 한국인 남성이 요오드로 인한 갑상선중독성 저칼륨 주기마비로 응급실을 찾았고, 함초를 끊은 지 8개월 뒤 갑상선 기능이 정상으로 돌아왔다[8]. 저자들은 이 사례에서 함초를 요오드 과량 섭취원으로 보았다[8].

탈염 함초 에탄올 추출물을 하루 600 mg씩 12주 먹은 무작위 이중맹검 시험에서 이상반응은 섭취군 12.5%, 위약군 12.9%로 차이가 없었고 모두 경미했다[5]. 함초 염과 대체염을 넣은 저나트륨 소시지를 4주 먹인 생쥐 아급성 독성 시험에서도 독성 지표가 정상 범위였다[27]. 탈염 열수추출물 연구진은 비소·수은 같은 중금속 분석과 비임상 연구가 더 필요하다고 밝혔다[6].

식약처 등 공공기관의 퉁퉁마디 알레르기·잔류농약·중금속 기준이나 경고 정보는 이번 조사에서 확인하지 못함.""")
    ,
]

compounds = [
    dict(name="Tungtungmadic acid", name_ko="퉁퉁마딕산(3-카페오일-4-디하이드로카페오일퀸산)", **{"class": "카페오일퀸산 유도체"}, role="marker", part="지상부",
         content_text="함량 수치 확인하지 못함; 2005년 부산 시료에서 처음 분리[2]",
         activity_ko="다른 생물에서는 보고되지 않아 이 식물의 식별 지표로 제안됨[2]; HepG2 세포에서 고포도당에 의한 지방 축적 억제(세포 실험)[13]",
         source=[2, 13]),
    dict(name="Isorhamnetin 3-O-beta-D-glucoside", name_ko="이소람네틴 3-O-β-D-글루코사이드", **{"class": "플라보놀 배당체"}, role="bioactive", part="지상부",
         content_text="정량값 확인하지 못함; 탈염 분말 HPLC에서 소량 성분으로 확인[4]",
         activity_ko="n-부탄올 분획의 퍼옥시나이트라이트 소거 주성분, 대식세포 NO·염증 사이토카인 억제(세포 실험)[11]; MMP-9·MMP-2 억제(세포 실험)[12]",
         source=[4, 11, 12]),
    dict(name="Isoquercitrin", name_ko="퀘르세틴 3-O-β-D-글루코사이드(이소퀘르시트린)", **{"class": "플라보놀 배당체"}, role="bioactive", part="지상부",
         content_text="분리 보고, 함량 수치 확인하지 못함[12]",
         activity_ko="섬유육종 세포에서 MMP-9·MMP-2 발현과 활성 억제(세포 실험)[12]",
         source=[12]),
    dict(name="trans-Ferulic acid", name_ko="트랜스-페룰산", **{"class": "하이드록시신남산"}, role="marker", part="지상부 열수추출 분말; 탈염 분말",
         content_text="추출 분말 2.60 ± 0.33 µg/g(HPLC)[3]; 탈염 분말에서 가장 많은 저분자 성분(정량값 없음)[4]",
         activity_ko="고염에 의한 관상동맥 기능 저하를 eNOS 경로로 회복(돼지 관상동맥 실험)[3]; 3T3-L1 지방세포 분화 억제(세포 실험)[4]",
         source=[3, 4]),
    dict(name="p-Coumaric acid", name_ko="p-쿠마르산", **{"class": "하이드록시신남산"}, role="bioactive", part="지상부 열수추출 분말",
         content_text="3.19 ± 0.47 µg/g(HPLC)[3]",
         activity_ko="고농도에서 약한 혈관 이완(0.1 mmol/L에서 10.92%)[3]",
         source=[3, 4]),
    dict(name="Caffeic acid", name_ko="카페산", **{"class": "하이드록시신남산"}, role="bioactive", part="지상부(함초 전초)",
         content_text="SPE-HPLC 정량법 개발(직선성 0.2–400 µg/mL), 시료 함량 수치는 초록에 없어 확인하지 못함[19]",
         activity_ko="해남 시료에서 프로토카테큐산·페룰산과 함께 DPPH·슈퍼옥사이드·하이드록실 라디칼 소거(시험관)[2]",
         source=[2, 19]),
    dict(name="Protocatechuic acid", name_ko="프로토카테큐산", **{"class": "하이드록시벤조산"}, role="bioactive", part="지상부(함초 전초)",
         content_text="SPE-HPLC 정량법 개발(직선성 0.1–200 µg/mL), 시료 함량 수치는 초록에 없어 확인하지 못함[19]",
         activity_ko="항산화 활성 유도 분리에서 활성 성분으로 확인(시험관)[2]",
         source=[2, 19]),
    dict(name="3,5-Dicaffeoylquinic acid", name_ko="3,5-디카페오일퀸산", **{"class": "카페오일퀸산 유도체"}, role="bioactive", part="건조 지상부 열수추출물(탈염)",
         content_text="열수추출물에서 분리(순도 > 95%), 함량 수치 확인하지 못함[6]",
         activity_ko="3,4-·4,5-이성질체와 함께 RANKL 유도 파골세포 분화와 활성산소 생성 억제(세포 실험)[6]",
         source=[2, 6, 32]),
    dict(name="Gypsogenin 3-O-beta-D-glucuronopyranosyl-28-O-beta-D-glucopyranoside", name_ko="집소게닌 3-O-글루쿠로나이드-28-O-글루코사이드", **{"class": "올레아난계 트리테르페노이드 사포닌"}, role="bioactive", part="지상부(n-부탄올 분획)",
         content_text="분리 보고, 함량 수치 확인하지 못함[14]",
         activity_ko="DPPH·퍼옥시나이트라이트 소거 평가 대상 사포닌 4종 중 하나(시험관)[14]; 퉁퉁마디에서 20종 이상의 올레아난계 사포닌이 보고됨[2]",
         source=[2, 14]),
    dict(name="Salbige A", name_ko="살비지 A(30-노르올레아난 사포닌)", **{"class": "노르올레아난계 트리테르펜 사포닌"}, role="bioactive", part="지상부",
         content_text="신규 화합물로 분리, 함량 수치 확인하지 못함[15]",
         activity_ko="A549 폐암세포 증식 억제 IC50 52.35 μM(세포 실험)[15]",
         source=[15]),
    dict(name="Pentadecyl ferulate", name_ko="펜타데실 페룰레이트", **{"class": "페룰산 에스터"}, role="bioactive", part="전초(에틸아세테이트 추출물)",
         content_text="신규 천연물로 분리, 함량 수치 확인하지 못함[16]",
         activity_ko="에틸아세테이트 추출물의 주 항산화 성분, HepG2·A549 세포 증식 억제(세포 실험)[16]",
         source=[16]),
    dict(name="Sodium chloride", name_ko="염화나트륨(소금)", **{"class": "무기염"}, role="nutrient", part="지상부 분말; 열수추출 분말; 탈염 분말",
         content_text="일반 분말 NaCl 25–35%[4]; 열수추출 정제 분말 NaCl 55.6%[3]; 탈염 분말 나트륨 0.71%[4]; 원물 나트륨 10 mg/g(기준 미기재)[7]",
         activity_ko="짠맛의 원천으로 소금 대용 연구의 근거; 탈염 공정의 제거 대상[4, 7]",
         source=[3, 4, 7]),
    dict(name="Potassium", name_ko="칼륨", **{"class": "무기질"}, role="nutrient", part="열수추출 분말; 원물",
         content_text="열수추출 분말 3.1%[3]; 원물 5.6 mg/g(기준 미기재)[7]",
         activity_ko="함초가 정제염보다 무기질이 많다는 근거로 제시됨[3]",
         source=[3, 7]),
    dict(name="Dietary fiber", name_ko="식이섬유", **{"class": "탄수화물(섬유)"}, role="nutrient", part="탈염 분말",
         content_text="74.27%[4]",
         activity_ko="고지방식 생쥐에서 소금 대신 함초 분말을 주면 체중 증가·간 지방 축적이 줄었고, 저자들은 식이섬유를 원인 중 하나로 봄[17]",
         source=[4, 17]),
    dict(name="Iodine", name_ko="요오드", **{"class": "무기질"}, role="nutrient", part="섭취 제품(형태 미기재)",
         content_text="함량 수치 확인하지 못함[8]",
         activity_ko="함초 장기 섭취 후 요오드 유발 갑상선중독성 저칼륨 주기마비 증례 1건[8]",
         source=[8]),
]

assays = [
    {
        "role": "literature", "compound": "trans-Ferulic acid", "compound_ko": "트랜스-페룰산(p-쿠마르산·5-하이드록시메틸푸르푸랄 동시 정량)",
        "part": "생 지상부 열수추출 → 활성탄 정제 → 분무건조 분말(논문 표기 Salicornia europaea, 서해안 채취)",
        "content": "trans-페룰산 2.60 ± 0.33, p-쿠마르산 3.19 ± 0.47, 5-하이드록시메틸푸르푸랄 18.20 ± 1.80 µg/g(같은 분말의 NaCl 55.6%)[3]",
        "method": "HPLC-PDA",
        "conditions": {
            "instrument": "Agilent 1260 Infinity(4원 펌프, 자동시료주입기, 칼럼 오븐, PDA 검출기)",
            "column": "Thermo Acclaim RSLC, 2.1 × 100 mm, 2.2 µm",
            "mobile_phase": "0.1% 포름산 함유 물 / 아세토니트릴",
            "gradient": "아세토니트릴 2→12%(0–6분), 12→35%(6–7분), 35→50%(7–15분)",
            "flow": "0.3 mL/min",
            "temp": "상온",
            "detection": "PDA 210–400 nm, 크로마토그램 305 nm 추출",
            "injection": "2 µL",
            "sample_prep": "분말 200 mg + 메탄올 1 mL, 초음파 5분 추출; 3회 주입",
            "standard": "Acros Organics 표준품, 메탄올 1.0 mg/mL 원액을 1·2·5·10·20·50 µg/mL로 희석",
            "linearity": "trans-페룰산 r = 0.9998, p-쿠마르산 r = 0.9998, 5-HMF r = 0.9990(피크 면적-농도 검량선)",
            "lod": "", "loq": "", "recovery": ""
        },
        "rationale": "추출 분말에서 확인된 주요 페놀산 가운데 고염에 의한 혈관 기능 저하를 막는 활성 성분으로 지목되었다[3]. 저자들은 염분이 많아 추출 과정에서 손실이 있을 수 있다고 적었고, 검출한계·정량한계·회수율은 본문에 없어 비워 둠.",
        "source": [3], "url": PMC.format("PMC4964547"), "source_kind": "paper"
    },
    {
        "role": "literature", "compound": "trans-Ferulic acid", "compound_ko": "트랜스-페룰산(탈염 분말 효소 분해 추출물의 HPLC 확인)",
        "part": "잎·가지·줄기 동결건조 후 물 추출·원심분리로 탈염한 분말(논문 표기 Salicornia europaea, 서해안 채취)",
        "content": "정량값 없음 — 탈염 분말의 가장 많은 저분자 성분; 카페산·p-쿠마르산·이소람네틴-3-글루코사이드는 소량 성분[4]",
        "method": "HPLC-DAD(동정), 분취 HPLC·ESI-MS 확인",
        "conditions": {
            "instrument": "Agilent HPLC(1260 4원 펌프, 1260 ALS 자동시료주입기, 1260 DAD, 1260 TCC 칼럼 항온조)",
            "column": "Agilent Zorbax Eclipse Plus C18, 4.6 × 150 mm, 3.5 µm",
            "mobile_phase": "메탄올 / 물",
            "gradient": "메탄올-물 기울기 용리(구간 수치는 본문에 없음)",
            "flow": "1.0 mL/min",
            "temp": "25 °C",
            "detection": "DAD 300 nm(참조 360 nm), UV 스펙트럼 190–400 nm",
            "injection": "3 µL(10 mg/mL)",
            "sample_prep": "탈염 분말 10 g을 아밀레이스·프로테에이스 함유 증류수 100 mL에 37 °C 6시간 → 10,000 g 25분 원심분리 → 상등액 감압 농축(950 mg) → 메탄올 가용분으로 시료 조제",
            "standard": "Sigma 표준품과 머무름 시간·UV 극대흡수 비교; 분취 HPLC(YMC Triart C18 20 × 250 mm, 5 µm)로 순수 분리 후 ESI-MS m/z 195.2 [M+H]+, 193.4 [M-H]-",
            "linearity": "", "lod": "", "loq": "", "recovery": ""
        },
        "rationale": "탈염 공정 뒤에도 남는 주성분으로, 탈염 분말의 항비만 효과를 설명하는 활성 성분으로 쓰였다[4]. 정량 검량선·검출한계·회수율은 본문에 없어 비워 둠.",
        "source": [4], "url": PMC.format("PMC6130585"), "source_kind": "paper"
    },
    {
        "role": "literature", "compound": "Protocatechuic acid", "compound_ko": "프로토카테큐산(카페산·페룰산 동시 정량)",
        "part": "함초 전초(Salicornia herbacea L.)",
        "content": "시료 중 함량 수치는 초록에 없어 확인하지 못함[19]",
        "method": "고상추출(SPE)-HPLC",
        "conditions": {
            "instrument": "", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "", "injection": "",
            "sample_prep": "C18 SPE 카트리지; 에탄올로 세척, 아세토니트릴/물/트리플루오로아세트산으로 용출",
            "standard": "",
            "linearity": "프로토카테큐산 0.1–200, 카페산 0.2–400, 페룰산 0.3–600 µg/mL(r > 0.999), 상대표준편차 3.6% 미만",
            "lod": "프로토카테큐산 0.02, 카페산 0.01, 페룰산 0.04 µg/mL(S/N = 3)",
            "loq": "",
            "recovery": "세 성분 평균 79.2% 이상"
        },
        "rationale": "함초의 항산화 페놀산 세 가지를 짠 시료 기질에서 방해 물질을 줄여 정량하려고 개발된 방법이다[19]. 전문 확인 못함 — 초록의 직선성·검출한계·회수율만 옮기고 칼럼·이동상·검출 조건은 비워 둠.",
        "source": [19], "url": PM.format("23513729"), "source_kind": "paper"
    },
]

nutrients = [
    {"form": "탈염 퉁퉁마디 분말(동결건조 원물을 물 추출·원심분리로 탈염, 논문 표기 S. europaea)", "basis": "분말 100 g(원문 % 값을 g으로 표기)",
     "items": [{"name": "열량", "value": 224.89, "unit": "kcal"}, {"name": "식이섬유", "value": 74.27, "unit": "g"}, {"name": "조단백질", "value": 9.13, "unit": "g"},
               {"name": "조지방", "value": 4.36, "unit": "g"}, {"name": "회분", "value": 6.23, "unit": "g"}, {"name": "나트륨", "value": 0.71, "unit": "g"}], "source": [4]},
    {"form": "퉁퉁마디 열수추출·활성탄 정제·분무건조 분말(비탈염, 논문 표기 S. europaea)", "basis": "분말 100 g(원문 % 값을 g으로 표기)",
     "items": [{"name": "염화나트륨", "value": 55.6, "unit": "g"}, {"name": "탄수화물", "value": 17.9, "unit": "g"}, {"name": "단백질", "value": 9.8, "unit": "g"},
               {"name": "지방", "value": 0.4, "unit": "g"}, {"name": "칼륨", "value": 3.1, "unit": "g"}, {"name": "칼슘", "value": 0.7, "unit": "g"}, {"name": "마그네슘", "value": 1, "unit": "g"}], "source": [3]},
    {"form": "퉁퉁마디(원물, 생체·건물 기준 미기재; 논문 서론의 인용 값)", "basis": "1 g",
     "items": [{"name": "나트륨", "value": 10, "unit": "mg"}, {"name": "칼륨", "value": 5.6, "unit": "mg"}, {"name": "마그네슘", "value": 1.9, "unit": "mg"},
               {"name": "칼슘", "value": 1.1, "unit": "mg"}, {"name": "철", "value": 0.2, "unit": "mg"}], "source": [7]},
]

d = {
    "slug": "salicornia-herbacea",
    "name_ko": "퉁퉁마디",
    "name_en": "Glasswort (Marshfire glasswort)",
    "scientific_name": "Salicornia herbacea L.",
    "aliases": ["함초", "퉁퉁마디잎", "퉁퉁마디줄기", "퉁퉁마디분말", "퉁퉁마디추출액", "퉁퉁마디발효액",
                "Salicornia europaea var. herbacea", "Salicornia europaea (국내 논문 표기)", "Marshfire glasswort", "Glasswort", "Hamcho", "Tungtungmadi"],
    "sections": [{"key": k, "title": t, "body": b} for k, t, b in sections],
    "compounds": compounds,
    "markers": [],
    "assays": assays,
    "nutrients": nutrients,
    "production": [],
    "world": [],
    "gi": [],
    "orgs": [],
    "sources": [{"n": n, "title": t, "url": u, "publisher": p, "accessed": a} for n, t, u, p, a in sources],
}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in d["sections"]:
    print(s["key"], len(s["body"]))
