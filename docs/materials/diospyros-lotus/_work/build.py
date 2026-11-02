import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
A = "2026-11-02"
PM = lambda p: f"https://pubmed.ncbi.nlm.nih.gov/{p}/"
PMC = lambda p: f"https://pmc.ncbi.nlm.nih.gov/articles/{p}/"
S = [
 (1, "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 고욤나무(Diospyros lotus L.)", "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "식품의약품안전처", "2026-10-13"),
 (2, "A rare cause of gastrointestinal phytobezoars: diospyros lotus. World J Emerg Surg. 2012", PMC("PMC3438099"), "World Journal of Emergency Surgery (PubMed Central)", A),
 (3, "Systematic review: Coca-Cola can effectively dissolve gastric phytobezoars as a first-line treatment. Aliment Pharmacol Ther. 2013", PM("23252775"), "Alimentary Pharmacology & Therapeutics (PubMed)", A),
 (4, "Drying date plum (Diospyros lotus L.) fruit: Assessing rehydration properties, antioxidant activity, and phenolic compounds. J Food Sci. 2022", PMC("PMC9826110"), "Journal of Food Science (PubMed Central)", A),
 (5, "Antioxidant activities and phenolic compounds of date plum persimmon (Diospyros lotus L.) fruits. J Food Sci Technol. 2011 (PMC 전문 본문은 도구로 받지 못해 초록만 확인)", PM("24803703"), "Journal of Food Science and Technology (PubMed)", A),
 (6, "Antioxidant and antiproliferative activity of Diospyros lotus L. extract and isolated compounds. Plant Foods Hum Nutr. 2009", PM("19731038"), "Plant Foods for Human Nutrition (PubMed)", A),
 (7, "Osteogenic Effects of the Diospyros lotus L. Leaf Extract on MC3T3-E1 Pre-Osteoblasts and Ovariectomized Mice via BMP2/4 and TGF β Pathways. Nutrients. 2024", PMC("PMC11053699"), "Nutrients (PubMed Central)", A),
 (8, "Enhanced Antioxidant and Anti-Inflammatory Activities of Diospyros lotus Leaf Extract via Enzymatic Conversion of Rutin to Isoquercitrin. Antioxidants (Basel). 2025", PMC("PMC12382970"), "Antioxidants (PubMed Central)", A),
 (9, "Diospyros lotus leaf extract and its main component, myricitrin, inhibit both histamine-dependent and histamine-independent itching. Exp Ther Med. 2025", PMC("PMC12035596"), "Experimental and Therapeutic Medicine (PubMed Central)", A),
 (10, "Diospyros lotus leaf extract and its main component myricitrin inhibit itch-related IL-6 and IL-31 by suppressing microglial inflammation and microglial-mediated astrocyte activation. Mol Med Rep. 2024", PMC("PMC11338241"), "Molecular Medicine Reports (PubMed Central)", A),
 (11, "Ameliorative effects of Diospyros lotus leaf extract against UVB-induced skin damage in BALB/c mice. Biomed Pharmacother. 2017", PM("28850926"), "Biomedicine & Pharmacotherapy (PubMed)", A),
 (12, "Anti-obesity effects of Diospyros lotus leaf extract in mice with high-fat diet-induced obesity. Int J Mol Med. 2018", PM("30365061"), "International Journal of Molecular Medicine (PubMed)", A),
 (13, "Dual Mechanistic Anti-Obesity Effects of Red Okra and Diospyros lotus Mixture via Fat Binding and AMPK-Mediated Lipid Metabolism. J Microbiol Biotechnol. 2025", PMC("PMC12535863"), "Journal of Microbiology and Biotechnology (PubMed Central)", A),
 (14, "Clinical evidence for fat-binding-mediated fecal fat excretion by RODL (Red Okra-botanical combination) under a prescribed restricted diet: a randomized, double-blind, placebo-controlled trial. Food Nutr Res. 2026", PMC("PMC13366810"), "Food & Nutrition Research (PubMed Central)", A),
 (15, "Anti-nociceptive, anti-inflammatory and sedative activities of the extracts and chemical constituents of Diospyros lotus L. Phytomedicine. 2014", PM("24703326"), "Phytomedicine (PubMed)", A),
 (16, "Novel Anticancer Dimeric Naphthoquinones from Diospyros lotus having Anti-Tumor, Anti-Inflammatory and Multidrug Resistance Reversal Potential. Anticancer Agents Med Chem. 2021", PM("33438565"), "Anti-Cancer Agents in Medicinal Chemistry (PubMed)", A),
 (17, "In vivo analgesic, anti-inflammatory, and sedative activity and a molecular docking study of dinaphthodiospyrol G isolated from Diospyros lotus. BMC Complement Med Ther. 2020", PMC("PMC7382863"), "BMC Complementary Medicine and Therapies (PubMed Central)", A),
 (18, "Muscle relaxant and antipyretic effects of pentacyclic triterpenes isolated from the roots of Diospyros lotus L. Heliyon. 2024", PMC("PMC11079251"), "Heliyon (PubMed Central)", A),
 (19, "Structural Characterization of Water-Soluble Pectin from the Fruit of Diospyros lotus and Its Protective Effects against DSS-Induced Colitis in Mice. J Agric Food Chem. 2025", PM("39742427"), "Journal of Agricultural and Food Chemistry (PubMed)", A),
 (20, "Antioxidant and hypoglycemic effects of Diospyros lotus fruit fermented with Microbacterium flavum and Lactobacillus plantarum. J Biosci Bioeng. 2018", PM("29395958"), "Journal of Bioscience and Bioengineering (PubMed)", A),
 (21, "Chromosome-level genomes of seeded and seedless date plum based on third-generation DNA sequencing and Hi-C analysis. For Res (Fayettev). 2021", PMC("PMC11524226"), "Forestry Research (PubMed Central)", A),
 (22, "Plant genetics. A Y-chromosome-encoded small RNA acts as a sex determinant in persimmons. Science. 2014", PM("25359977"), "Science (PubMed)", A),
 (23, "Random epigenetic inactivation of the X-chromosomal HaMSter gene causes sex ratio distortion in persimmon. Nat Plants. 2024", PM("39333352"), "Nature Plants (PubMed)", A),
 (24, "Accumulation of numerous cellular T-DNA sequences in the genus Diospyros by multiple rounds of natural transformation. Plant J. 2025", PM("40359552"), "The Plant Journal (PubMed)", A),
 (25, "Population Analysis of Diospyros lotus in the Northwestern Caucasus Based on Leaf Morphology and Multilocus DNA Markers. Int J Mol Sci. 2022", PMC("PMC8877681"), "International Journal of Molecular Sciences (PubMed Central)", A),
 (26, "Genetic variation among date plum (Diospyros lotus) genotypes in Turkey. Genet Mol Res. 2010", PM("20506085"), "Genetics and Molecular Research (PubMed)", A),
 (27, "In vitro propagation of persimmon (Diospyros kaki Thunb.). Methods Mol Biol. 2013", PM("23179692"), "Methods in Molecular Biology (PubMed)", A),
 (28, "Cloning of the DlERF10 gene from Diospyros lotus L. and cold tolerance analysis of the DlERF10 gene in transgenic tobacco plants. PLoS One. 2025", PMC("PMC11875332"), "PLoS One (PubMed Central)", A),
 (29, "Low-Molecular-Weight Organic Acid as an Alternative to Promote the Rooting of Persimmon Rootstock Shoot Cuttings. Plants (Basel). 2024", PMC("PMC11644523"), "Plants (PubMed Central)", A),
 (30, "Influences of arbuscular mycorrhizal fungi on Diospyros lotus seedlings under salinity stress. Front Plant Sci. 2025", PMC("PMC12325204"), "Frontiers in Plant Science (PubMed Central)", A),
 (31, "Conflicting selection pressures on seed size and germination caused by carnivorous seed dispersers. Integr Zool. 2023", PM("37394984"), "Integrative Zoology (PubMed)", A),
 (32, "Ethnobotanical survey of medicinally important wild edible fruits species used by tribal communities of Lesser Himalayas-Pakistan. J Ethnopharmacol. 2013", PM("23665057"), "Journal of Ethnopharmacology (PubMed)", A),
 (33, "Diospyros lotus L. fruit extract protects G6PD-deficient erythrocytes from hemolytic injury in vitro and in vivo: prevention of favism disorder. Eur Rev Med Pharmacol Sci. 2011", PM("22195359"), "European Review for Medical and Pharmacological Sciences (PubMed)", A),
 (34, "Rapid Characterization and Action Mechanism of the Antidiabetic Effect of Diospyros lotus L Using UHPLC-Q-Exactive Orbitrap MS and Network Pharmacology. J Anal Methods Chem. 2022", PMC("PMC9825215"), "Journal of Analytical Methods in Chemistry (PubMed Central)", A),
 (35, "A high-quality chromosomal genome assembly of Diospyros oleifera Cheng. GigaScience. 2020", PMC("PMC6964648"), "GigaScience (PubMed Central)", A),
 (36, "Flora of Korea — 고욤나무 Diospyros lotus L. (WebSearch 검색 요약으로만 확인, 페이지는 네트워크 허용 목록 밖이라 열지 못함)", "https://florakorea.myspecies.info/ko/taxonomy/term/5194", "Flora of Korea", A),
 (37, "Gastric Diospyrobezoar Dissolution with Ingestion of Diet Soda and Cellulase Enzyme Supplement. ACG Case Rep J. 2017", PMC("PMC5519403"), "ACG Case Reports Journal (PubMed Central)", A),
 (38, "고욤나무·감나무 실생묘 생육 비교(한국토양비료학회지, 2013; 경상남도농업기술원) — WebSearch 검색 요약으로만 확인, 원문은 네트워크 허용 목록 밖이라 열지 못함", "https://koreascience.kr/article/JAKO201307954672036.pdf", "한국토양비료학회(KoreaScience)", A),
]
sources = [dict(n=n, title=t, url=u, publisher=p, accessed=a) for n, t, u, p, a in S]

sections = [
 dict(key="overview", title="한눈에 보기", body=
"고욤나무(Diospyros lotus L.)는 감나무과(Ebenaceae) 감나무속에 속하는 나무로, 영어로는 date plum 또는 Caucasian persimmon이라 부른다[4][22]. 열매는 먹을 수 있으며 중국과 아시아가 원산지로 소개되고, 여러 나라에서 열매를 얻으려고 기른다[4].\n\n"
"식품의약품안전처 「식품원료 목록」에서 고욤나무는 식품에 사용할 수 있는 원료(사용가능)이며, 사용 조건은 '사용가능부위 : 잎, 열매'이다[1]. 같은 목록에는 고욤나무열매·고욤나무열매분말·고욤나무잎·고욤나무잎추출물·고욤나무잎추출물농축액·고욤나무잎추출물분말 6개 원료명이 올라 있고, 다른 이름 '고양나무'와 영문명 Date-plum, 학명 표기 'Diospyros lotus L. / Diospyros kaki var. glabra A.DC.'가 함께 적혀 있다[1]. 건강기능식품 고시형 원료의 원재료로 쓰인다는 기록은 확인하지 못함.\n\n"
"잎에는 미리시트린(myricitrin)·퀘르시트린 같은 플라보노이드 배당체가[7], 열매에는 갈산(gallic acid)을 비롯한 페놀산이 많다고 보고되었다[4][5]. 뿌리에서는 디오스피린 같은 이량체 나프토퀴논이 분리되었다[15][16]. UHPLC-Orbitrap 질량분석 연구는 고욤나무 시료에서 159개 성분을 동정했고 그 가운데 140개가 처음 보고된 것이었다[34]. 사람 대상 연구는 붉은 오크라와 고욤나무를 섞은 배합물(RODL)의 2일 시험 하나만 확인되었다[14]. 열매(생과·말린 것)를 많이 먹은 뒤 위장관 위석이 생긴 터키 증례 보고가 있다[2]."),
 dict(key="history", title="역사와 전통적 이용", body=
"고욤나무 열매는 터키 흑해 지역과 북동 아나톨리아에서 널리 먹는 전통 과일로, 그곳에서는 'Trabzon의 야생 대추야자'라고도 부른다[2]. 중국에서는 오래전부터 진정제로 써 왔다고 소개된다[20]. 동아시아 전통 의학에서도 오래 써 왔다고 소개된다[8].\n\n"
"파키스탄 소히말라야 지역의 야생 식용 과일 조사에서 고욤나무는 문화적 중요도 상위 10종 안에 들었다[32]. 이란에서는 열매 추출물을 민간에서 쓰며, 이를 근거로 누에콩(잠두) 중독(favism)에 대한 보호 효과를 시험한 연구가 있다[33]. 전통적으로 진정·해열·진통·설사·당뇨 등에 써 왔다는 기록을 바탕으로 뿌리 추출물의 동물 실험이 이어졌다[15][17].\n\n"
"고욤나무는 추위에 강해 감나무속 과수의 대목(접붙이는 밑나무)으로 널리 쓰여 왔다[27][28]. 한국에서 고욤을 먹거나 약으로 쓴 역사 기록은 이 자료에서 확인하지 못함."),
 dict(key="biology", title="식물학적 특징", body=
"고욤나무는 갈잎 큰키나무로 높이 10 m까지 자라고, 잎은 길이 6–12 cm, 너비 5–7 cm로 소개된다[36]. 암수딴그루 식물이며 수그루가 XY 성염색체를 가진다[22]. 성 결정에는 Y 염색체의 OGI 유전자가 만드는 작은 RNA가 상염색체의 MeGI 유전자를 억제하는 방식이 관여한다[22].\n\n"
"터키 삼순산 열매는 거의 공 모양으로 너비 19.90 mm, 길이 18.06 mm였고, 과육/씨 비율 2.81, 1 kg당 약 220개였다[4]. 같은 열매의 건물 함량은 44.60%, 가용성 고형분 13.66%, pH 6.82였다[4]. 중국 아열대 숲에서는 사향고양이·담비·흑곰 등 육식 동물 다섯 종이 열매를 먹고 씨를 퍼뜨렸으며, 몸 크기에 따라 고르는 씨 크기가 달랐다[31].\n\n"
"감나무속 가운데 서리에 가장 강한 종의 하나로, 추운 지역에서 대목으로 쓰인다[25]. 반면 염분에는 약해, 온실 시험에서 고욤나무 실생묘는 수지상균근균 없이 잘 자라지 못했고 균근 의존도가 염류 조건에서 70%를 넘었다[30]."),
 dict(key="related_species", title="가까운 종", body=
"감나무속에는 약 795종이 있으며, 감(D. kaki)·고욤나무(D. lotus)·미국감(D. virginiana) 같은 과수와 흑단류가 포함된다[24]. 감·유시(D. oleifera)·고욤나무·미국감 네 종은 한 계통군에 속하고, 이들 유전체에서 아그로박테리움 유래 T-DNA 서열 15종이 확인되었다[24].\n\n"
"유시(D. oleifera)와 고욤나무는 약 900만 년 전에 갈라진 것으로 추정되며, 두 종 모두 오래된 γ 사건 뒤에 전체 유전체 중복을 한 번 더 겪었다[35]. 고욤나무는 이배체 감나무속 식물로 소개되며[23], 수그루 특이 OGI 유전자의 보존 양상은 감나무속 여러 종에서 비교되었다[22].\n\n"
"감나무 접목 묘목은 감·고욤나무·미국감 실생 대목에 접붙여 만드는 것이 전통 방식이다[27]. 고욤나무 대목은 튼튼하고 서리에 강해 많이 쓰이지만, 단감(떫지 않은 감) 품종 대부분과는 접목 친화성이 없다[27]. 「식품원료 목록」은 'Diospyros kaki var. glabra A.DC.'를 고욤나무와 같은 원료의 학명으로 함께 적고 있다[1]. 이 이명의 현재 분류학적 지위는 이 자료에서 확인하지 못함."),
 dict(key="cultivation", title="재배와 생산", body=
"고욤나무는 실생묘의 생존력이 높고 추위에 강하며 감과 접목 친화성이 좋아 감나무속의 대목으로 자주 쓰인다[28]. 중국 북부에서는 겨울 저온 피해가 감 산업의 큰 제약이어서, 고욤나무의 내한성 유전자 연구가 이루어졌다[28]. 북서 캅카스 지방의 자연 개체군 5곳을 조사한 연구는 추운 지역으로 감 재배를 넓히기 위한 자료로 쓰일 수 있다고 보았다[25].\n\n"
"감나무류는 꺾꽂이로 뿌리 내리기가 어려워 대목을 주로 씨로 번식한다[27]. 고욤나무 대목의 꺾꽂이에서 말산·타르타르산(각 4,000 mg/L) 처리가 발근율과 생존율을 크게 높였다는 보고가 있다[29]. 국내 시험에서 고욤나무 실생묘는 감나무 실생묘보다 줄기 길이·굵기·잎 수가 더 빨리 자랐다는 결과가 검색 요약으로 확인되었다[38].\n\n"
"통계청 농작물생산조사와 농림축산식품부 특용작물 생산실적 파싱본에는 고욤 항목이 없어 국내 재배 면적·생산량은 확인하지 못함. 고욤나무의 지리적 표시 등록과 세계 생산 통계도 확인하지 못함."),
 dict(key="processing", title="가공과 이용", body=
"열매는 생으로 먹거나 말려 두고 먹으며, 터키에서는 말린 고욤을 수확기 뒤 봄철까지 먹는다[2]. 대류식 건조 시험에서 70 °C 건조가 총페놀·총플라보노이드·갈산·카테킨을 가장 잘 지켰고, 풍속(0.5–1.5 m/s)은 항산화 성분에 유의한 영향을 주지 않았다[4]. 건조 곡선은 Midilli 모델, 재수화는 Weibull 모델이 가장 잘 맞았다[4].\n\n"
"열매를 Microbacterium flavum과 Lactobacillus plantarum으로 발효하면 24시간 만에 탄닌산·카테킨산·엘라그산 함량이 크게 늘었고, α-글루코시다아제 억제 활성은 발효 전보다 2.06–4.73배 높았다[20]. 열매의 수용성 펙틴은 분자량 8.93–153.95 kDa의 네 분획으로 나뉘었다[19].\n\n"
"잎은 50% 에탄올 추출물로 만들어 미리시트린 함량을 확인한 연구가 있다[7]. 잎 물 추출물은 고지방식 생쥐의 체중 증가·내장지방·혈중 중성지방을 줄였다(동물 실험)[12]. 잎 추출물에 α-L-람노시다아제를 처리해 루틴을 이소퀘르시트린으로 바꾸면 DPPH 소거능 IC50이 107.4에서 72.8 μg/mL로 좋아졌다[8]. 붉은 오크라와 고욤나무 잎 추출물을 4:1로 섞은 배합물이 동물에서 지방 흡수를 줄였고[13], 사람 시험에서 하루 1.5 g을 2일 먹은 군의 대변 지방 배출이 위약군보다 많았다[14]. 「식품원료 목록」에는 잎추출물·잎추출물농축액·잎추출물분말·열매분말이 원료명으로 올라 있다[1]. 식약처 건강기능식품 생산실적 품목에서 고욤나무 원료는 확인하지 못함."),
 dict(key="genetics", title="유전체와 육종", body=
"씨 있는 고욤과 씨 없는 고욤의 염색체 수준 유전체가 조립되었으며, 15개 염색체에 크기는 각각 647.31 Mb와 617.66 Mb였다[21]. 단백질 암호 유전자는 씨 있는 쪽 22,844개, 씨 없는 쪽 20,689개가 주석되었고, 8번 염색체에서 역위와 전좌가 관찰되었다[21].\n\n"
"고욤나무는 식물 성 결정 연구의 모델로 쓰인다[22]. 수그루 특이 서열로 찾아낸 Y 염색체의 OGI 유전자는 MeGI 유전자를 겨냥하는 작은 RNA를 만든다[22]. 고욤나무의 성 연관 영역에 있는 HaMSter 유전자는 X 대립유전자만 발현되며, 배젖에서 무작위 후성유전적 불활성화가 일어나 씨의 성비가 치우친다[23]. 감나무속 4종 유전체에는 300만–1,200만 년 전에 들어간 세포성 T-DNA가 남아 있다[24].\n\n"
"터키 코루흐 계곡의 11개 유전형을 RAPD로 분석했을 때 다형성 밴드 비율은 58%, 유사도는 0.48–0.76이었다[26]. 북서 캅카스 개체군 연구에서는 ISSR·SCoT 표지로 가장 북쪽 개체군이 형태와 유전 모두에서 떨어져 있었다[25]. 고욤나무 잎에서 클로닝한 DlERF10 유전자를 담배에 넣으면 저온 피해가 줄었다[28]. 고욤나무 자체를 과수로 개량한 국내 품종 정보는 확인하지 못함."),
 dict(key="safety", title="안전성", body=
"고욤나무의 잎과 열매는 「식품원료 목록」에서 사용가능 원료로 분류되어 있다[1]. 건강기능식품 고시형 원료가 아니어서 고시 섭취 시 주의사항은 없다는 점을 확인했으나, 식약처 등 공공기관의 알레르기·잔류농약·독성 성분 정보는 확인하지 못함.\n\n"
"터키 뒤즈제의 한 병원에서 2008–2011년 위장관 식물 위석으로 수술한 13명은 모두 고욤을 먹은 이력이 있었다[2]. 10명(76.9%)은 수확기인 11–12월에, 말린 고욤을 먹은 3명은 3–6월에 입원했다[2]. 위석은 식물 섬유로 이루어졌고 가운데에 고욤 씨가 있었으며, 위 수술 이력(30.7%)·당뇨(30.7%)·틀니(23%)가 함께 있었다[2]. 저자들은 고욤 같은 식품에 소화되지 않는 섬유와 과일 탄닌이 많다고 설명하며, 위 수술을 받았거나 씹는 힘이 약한 사람은 많이 먹지 말라고 권했다[2].\n\n"
"감류 열매(종 구분 없는 'persimmon')는 탄닌이 많고, 이로 생긴 위석(diospyrobezoar)은 다른 식물 위석보다 단단해 녹이기 어렵다고 보고된다[37]. 콜라 용해 치료 성공률도 감 위석은 23%로 일반 식물 위석(60.6%)보다 낮았다[3]. 다만 고욤 덜 익은 열매의 탄닌 함량이나 익은 정도에 따른 위석 위험 차이를 이 종에서 직접 잰 자료는 확인하지 못함.\n\n"
"생쥐 급성 독성 시험에서 뿌리 클로로포름 분획(50–150 mg/kg)과 디오스피린(5·10 mg/kg)은 안전한 것으로 보고되었다[15]. 붉은 오크라 배합물의 사람 시험(2일)에서는 안전성 지표에 문제가 없었다[14]. 장기 섭취 안전성 자료는 확인하지 못함."),
]

compounds = [
 dict(name="Myricitrin", name_ko="미리시트린(미리세틴-3-O-람노사이드)", class_="플라보놀 배당체", role="marker", part="잎(50% 에탄올 추출물)",
      content_text="추출물 1 g당 122 mg(0.122 mg/mL)[7]", activity_ko="잎 추출물의 주성분으로, 생쥐 가려움 모델에서 긁는 행동·혈청 히스타민·비만세포 침윤을 줄였다[9]; 미세아교세포의 IL-6·IL-31 생성을 억제했다(세포)[10]; 잎 추출물의 HPLC 주요 활성 성분으로 확인되었고 추출물 바르기가 UVB 피부 손상을 줄였다(생쥐)[11]", source=[7, 9, 10, 11]),
 dict(name="Rutin", name_ko="루틴", class_="플라보놀 배당체", role="marker", part="잎(건조)",
      content_text="2.57 mg/g(건조 잎, 경북 안동 2023년 9월 채집)[8]", activity_ko="α-L-람노시다아제로 이소퀘르시트린으로 바뀌는 기질; 루틴 단독 LOX 억제 20.1%(50 μM)[8]", source=[8]),
 dict(name="Isoquercitrin", name_ko="이소퀘르시트린", class_="플라보놀 배당체", role="bioactive", part="잎(건조)",
      content_text="0.64 mg/g(건조 잎)[8]; 효소 전환 뒤 추출물 내 9.8 → 39.8 mM[8]", activity_ko="단독 LOX 억제 30.6%; 전환 추출물 DPPH IC50 72.8 μg/mL(미처리 107.4 μg/mL)[8]", source=[8]),
 dict(name="Quercitrin", name_ko="퀘르시트린", class_="플라보놀 배당체", role="bioactive", part="잎(50% 에탄올 추출물)",
      content_text="HPLC 주요 피크 2(머무름 31.1분); 추출물 40 mg 안에 100 µg 이하[7]", activity_ko="잎 추출물 주성분의 하나로 확인되었으나 이 연구의 용량에서는 단독으로 골형성 효과를 내기에 부족하다고 보았다[7]", source=[7]),
 dict(name="Kaempferol 7-O-rhamnoside", name_ko="캠페롤-7-O-람노사이드", class_="플라보놀 배당체", role="bioactive", part="잎(50% 에탄올 추출물)",
      content_text="HPLC 주요 피크 3(머무름 34.6분, [M–H]⁻ m/z 431.1034); 함량 수치는 확인하지 못함[7]", activity_ko="잎 추출물의 3대 주성분으로 동정됨[7]", source=[7]),
 dict(name="Gallic acid", name_ko="갈산", class_="페놀산(가수분해형 탄닌 구성단위)", role="marker", part="열매",
      content_text="건조 시료 45.49–287.47 μg/g(추출 용매별, HPLC-ECD)[5]; 생과 169.18 mg/kg, 70 °C 건조 시 최고 341.79 mg/kg(LC-MS/MS)[4]", activity_ko="열매 페놀 가운데 가장 많음[5]; 분리 갈산이 CaCo-2 세포에 IC50 2.6 μg/mL의 세포독성을 보임[6]", source=[4, 5, 6]),
 dict(name="Myricetin", name_ko="미리세틴", class_="플라보놀", role="bioactive", part="열매",
      content_text="건조 시료 2.75 μg/g(아세톤 추출)–5.28 μg/g(물 추출)[5]", activity_ko="열매 추출물의 주된 플라보노이드[5]; 고욤나무에서 얻은 미리세틴이 대식세포의 NO·iNOS·COX-2 생성을 억제했다는 보고가 있다(PMID 27068250, 이 문서 출처 목록 밖)[6]", source=[5, 6]),
 dict(name="Ellagic acid", name_ko="엘라그산", class_="페놀산(가수분해형 탄닌)", role="bioactive", part="부위 초록 미기재 추출물; 열매 발효물",
      content_text="함량 수치는 확인하지 못함; 열매 발효 24시간에 유의하게 증가[20]", activity_ko="C32·A375 세포 증식 억제 IC50 0.8·4.1 μg/mL(시험관)[6]", source=[6, 20]),
 dict(name="Sinapic acid", name_ko="시납산", class_="페놀산", role="bioactive", part="열매(생과)",
      content_text="134.53 mg/kg(생과); 건조 후 4.35–14.70 mg/kg로 감소[4]", activity_ko="생과에서 갈산 다음으로 많은 페놀산으로 측정됨[4]", source=[4]),
 dict(name="Catechin", name_ko="카테킨", class_="플라반-3-올", role="bioactive", part="열매",
      content_text="생과 28 mg/kg; 70 °C·1.0 m/s 건조 시 65.80 mg/kg[4]", activity_ko="70 °C 건조에서 가장 잘 보존됨[4]", source=[4]),
 dict(name="Diospyrin", name_ko="디오스피린", class_="이량체 나프토퀴논", role="bioactive", part="뿌리",
      content_text="함량 수치는 확인하지 못함", activity_ko="생쥐 아세트산 몸비틀기 40.87% 억제, 카라기난 부종 80.54% 억제[15]; 세포독성 IC50 47.40 ppm[16]", source=[15, 16]),
 dict(name="7-Methyljuglone", name_ko="7-메틸주글론", class_="나프토퀴논", role="bioactive", part="뿌리",
      content_text="함량 수치는 확인하지 못함", activity_ko="뿌리에서 처음 분리 보고된 7종 성분의 하나[15]", source=[15]),
 dict(name="Dinaphthodiospyrol G", name_ko="디나프토디오스피롤 G", class_="이량체 나프토퀴논", role="bioactive", part="뿌리(클로로포름 분획)",
      content_text="함량 수치는 확인하지 못함", activity_ko="카라기난·히스타민 부종을 55.23%·78.34% 줄이고 진통·진정 효과를 보임(생쥐)[17]", source=[17]),
 dict(name="Oleanolic acid", name_ko="올레아놀산", class_="오각고리 트리테르펜", role="bioactive", part="뿌리",
      content_text="함량 수치는 확인하지 못함", activity_ko="10 mg/kg 복강 투여 시 침니 시험 근이완 66.72%, 해열 71.59%(생쥐)[18]", source=[18]),
 dict(name="Pectin", name_ko="수용성 펙틴(DRP)", class_="다당", role="bioactive", part="열매",
      content_text="분획 DRP-1 153.95 kDa, DRP-2 61.22 kDa, DRP-3 22.80 kDa, DRP-4 8.93 kDa; DRP-4의 RG-I 영역 43.25%[19]", activity_ko="DSS 대장염 생쥐에서 점막·밀착연접 단백질을 지키고 장내 미생물 구성을 개선[19]", source=[19]),
]
for c in compounds:
    c["class"] = c.pop("class_")
# fix: myricetin activity should not cite an unlisted PMID
compounds[6]["activity_ko"] = "열매 추출물의 주된 플라보노이드[5]; 분리 성분으로서 항산화·항증식 활성에 관련된 페놀 화합물로 보고됨[6]"

def cond(**kw):
    keys = ["instrument","column","mobile_phase","gradient","flow","temp","detection","injection","sample_prep","standard","linearity","lod","loq","recovery"]
    return {k: kw.get(k, "") for k in keys}

assays = [
 dict(role="literature", compound="Myricitrin", compound_ko="미리시트린", part="잎(시판 건조 원료, 50% 에탄올 추출물)",
      content="추출물 1 g당 122 mg(0.122 mg/mL)[7]", method="HPLC-UV(280 nm); 동정은 UHPLC-Q-TOF MS",
      conditions=cond(instrument="Agilent 1260 Infinity HPLC; 동정용 Agilent 1290 Infinity UHPLC + Q-TOF(Agilent G6550A)",
                      column="YMC-Triart C18, 150 × 4.6 mm, S-5 μm, 12 nm(동정용: Agilent RRHD Eclipse Plus C18, 2.1 × 50 mm, 1.8 μm)",
                      mobile_phase="A 0.1% 포름산 수용액, B 아세토니트릴",
                      gradient="B 5–10%(10분) → 10–40%(40분) → 40–100%(4분)",
                      flow="1 mL/min(동정용 0.3 mL/min)", temp="30 °C", detection="UV 280 nm(MS: m/z 80–1700, 1 spectra/s)",
                      injection="10 μL(10 mg/mL)", sample_prep="건조 원료 50 g을 50% 에탄올로 실온 72시간 추출 → 여과 → SpeedVac 농축 건고",
                      standard="미리시트린 표준품(머무름 시간·질량 대조)"),
      rationale="잎 추출물의 3대 주성분(미리시트린 27.2분, 퀘르시트린 31.1분, 캠페롤-7-O-람노사이드 34.6분) 가운데 표준품을 구할 수 있는 미리시트린만 정량했고, 같은 연구진이 이를 '주성분'으로 삼아 효능을 비교했다[7][9]. 직선성·검출한계·회수율은 전문에 없어 비워 둠.",
      source=[7, 9], url=PMC("PMC11053699"), source_kind="paper"),
 dict(role="literature", compound="Rutin", compound_ko="루틴·이소퀘르시트린", part="잎(경북 안동 2023-09-19 채집, 15 °C·상대습도 15%에서 1주 건조)",
      content="루틴 2.57 mg/g, 이소퀘르시트린 0.64 mg/g(건조 잎)[8]", method="HPLC-UV(205 nm), 외부 표준 검량",
      conditions=cond(instrument="Agilent 1260(UV 검출기)", column="Waters AccQ-Tag 역상, 150 × 3.9 mm",
                      mobile_phase="I: 0.1% TFA/아세토니트릴, II: 0.1% TFA/증류수",
                      gradient="I:II 10:90 → 40:60(40분) → 90:10(5분)", flow="1.0 mL/min", temp="30 °C", detection="UV 205 nm",
                      sample_prep="반응액에 같은 부피 n-부탄올 → 부탄올층 건고 → 메탄올 재용해(추출물은 건조 잎 분말 100 g + 95% 에탄올 1 L, 45 °C 초음파 3시간 × 3회, Diaion HP-20로 당 제거)",
                      standard="루틴(머무름 7.3분)·이소퀘르시트린(7.7분) 등 표준품(Chemfaces, Sigma-Aldrich)"),
      rationale="이 조건에서 다른 주요 플라보노이드는 검출되지 않아 루틴과 이소퀘르시트린만 정량했다[8]. 연구진은 고욤나무를 루틴이 많은 식물로 보고 효소 전환 원료로 골랐다[8]. 직선성·검출한계·회수율은 전문에 없어 비워 둠.",
      source=[8], url=PMC("PMC12382970"), source_kind="paper"),
 dict(role="literature", compound="Gallic acid", compound_ko="갈산 등 페놀 13종", part="열매(터키 삼순 2019년 겨울 수확, 생과·건조과)",
      content="생과 갈산 169.18 mg/kg, 시납산 134.53 mg/kg, 바닐산 52.68 mg/kg, 카테킨 28 mg/kg; 70 °C·0.5 m/s 건조과 갈산 341.79 mg/kg[4]", method="LC-MS/MS(ESI)",
      conditions=cond(instrument="Shimadzu LC-MS 8040(LC-30AD 펌프 2대, CTO-10AS VP 칼럼 오븐, SIL-30AC 자동주입기)",
                      column="ODS Hypersil C18, 4.6 × 250 mm, 5 µm", mobile_phase="A 물:포름산 99.9:0.1(v/v), B 메탄올",
                      gradient="0–1분 A 100% → 22분 A 5%/B 95% → 25분 A 5% → 30분 B 100%(총 34분)", flow="0.7 mL/min", temp="30 °C",
                      detection="ESI MS/MS; 모세관 300 °C, 기화기 350 °C, 분무전압 +4000 V/−2500 V", injection="20 μL(0.45 µm 나일론 필터)",
                      sample_prep="분쇄 시료 1 g + 80% 메탄올 20 mL, 25 °C 12시간 침지 후 여과·희석",
                      standard="갈산·카테킨·푸마르산·퀘르세틴 혼합 외부 표준 0–200 ppm"),
      rationale="갈산은 이 종 열매에서 가장 많은 페놀로 반복 보고되어(다른 연구에서도 최다)[5], 건조 조건이 기능성 성분 보존에 미치는 영향을 보는 지표로 쓰였다[4]. 검출·정량한계와 회수율은 전문에 없어 비워 둠.",
      source=[4, 5], url=PMC("PMC9826110"), source_kind="paper"),
 dict(role="literature", compound="Gallic acid", compound_ko="갈산·미리세틴", part="열매(건조 시료; 물·메탄올·아세톤 추출물)",
      content="갈산 45.49–287.47 μg/g, 미리세틴 2.75–5.28 μg/g(건조 시료)[5]", method="HPLC-ECD(전기화학 검출)",
      conditions=cond(),
      rationale="갈산이 가장 많은 페놀 화합물이고 미리세틴이 모든 추출물의 주된 플라보노이드였으며, 항산화 활성이 총페놀·총플라보노이드와 잘 상관했다[5]. 전문 확인 못함 — PMC 전문 본문을 도구로 받지 못해 분석 조건 칸을 모두 비워 둠.",
      source=[5], url=PM("24803703"), source_kind="paper"),
]

d = dict(slug="diospyros-lotus", name_ko="고욤나무", name_en="Date-plum (Caucasian persimmon)", scientific_name="Diospyros lotus L.",
         aliases=["고욤", "고양나무", "고욤나무열매", "고욤나무잎", "Date-plum", "date plum", "Caucasian persimmon", "Diospyros kaki var. glabra A.DC."],
         sections=sections, compounds=compounds, markers=[], assays=assays, nutrients=[], production=[], world=[], gi=[], orgs=[], sources=sources)
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
print("written", OUT)
