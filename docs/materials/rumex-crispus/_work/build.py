import json
from pathlib import Path
OUT = Path(__file__).resolve().parents[1] / "dossier.json"
A = "2026-11-02"
def pm(pmid): return f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
def doi(d): return f"https://doi.org/{d}"
S = [
 ("식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 소리쟁이(Rumex crispus L.)", "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "식품의약품안전처", "2026-10-13"),
 ("Rumex crispus L.: A comprehensive review on botany, traditional uses, phytochemistry, pharmacology, and safety. Int Immunopharmacol 2024;143:113569 (초록 확인)", doi("10.1016/j.intimp.2024.113569"), "Elsevier (PubMed PMID 39520965)", A),
 ("Comparison of the Proximate Composition, Vitamins, Anti-Nutrients (Phytate and Oxalate) and the GC-MS Analysis of the Essential Oil of the Root and Leaf of Rumex crispus L. Plants (Basel) 2019;8(3):51 (PMC6473742)", doi("10.3390/plants8030051"), "MDPI (PubMed Central)", A),
 ("Acute oxalate poisoning attributable to ingestion of curly dock (Rumex crispus) in sheep. J Am Vet Med Assoc 1990;196(12):1981-4", pm("2365622"), "PubMed (PMID 2365622)", A),
 ("Fatal poisoning by Rumex crispus (curled dock): pathological findings and application of scanning electron microscopy. Vet Hum Toxicol 1990;32(5):468-70", pm("2238449"), "PubMed (PMID 2238449)", A),
 ("EFSA ANS Panel. Safety of hydroxyanthracene derivatives for use in food. EFSA Journal 2018;16(1):e05090 (PMC7009633)", doi("10.2903/j.efsa.2018.5090"), "유럽식품안전청(EFSA)", A),
 ("More Than Just a Weed: An Exploration of the Antimicrobial Activity of Rumex crispus using a Multivariate Data Analysis Approach. Planta Med 2022;88(9-10):753-761 (PMC9035478)", doi("10.1055/a-1652-1547"), "Thieme (PubMed Central)", A),
 ("In Vitro Antioxidant, Antiinflammation, and Anticancer Activities and Anthraquinone Content from Rumex crispus Root Extract and Fractions. Antioxidants (Basel) 2020;9(8):726 (PMC7464605)", doi("10.3390/antiox9080726"), "MDPI (PubMed Central)", A),
 ("Hydrolytical instability of hydroxyanthraquinone glycosides in pressurized liquid extraction. Anal Bioanal Chem 2014;406(13):3219-27 (PMC3992226)", doi("10.1007/s00216-014-7744-5"), "Springer (PubMed Central)", A),
 ("Water extract of Rumex crispus prevents bone loss by inhibiting osteoclastogenesis and inducing osteoblast mineralization. BMC Complement Altern Med 2017;17:483 (PMC5657118)", doi("10.1186/s12906-017-1986-7"), "BioMed Central (PubMed Central)", A),
 ("Genetic Diversity and Population Structure of Rumex crispus in South Korea Based on Genome-Derived Microsatellite Markers. Plants (Basel) 2025;14(24):3806 (PMC12736510)", doi("10.3390/plants14243806"), "MDPI (PubMed Central)", A),
 ("Molecular evidence for natural hybridization between Rumex crispus and R. obtusifolius (Polygonaceae) in Korea. Sci Rep 2022;12:5423 (PMC8971494)", doi("10.1038/s41598-022-09292-9"), "Nature Portfolio (PubMed)", A),
 ("The complete chloroplast genome of a medicinal resource plant (Rumex crispus). Mitochondrial DNA B Resour 2019;4(2):2800-2801 (PMC7706888)", doi("10.1080/23802359.2019.1660254"), "Taylor & Francis (PubMed)", A),
 ("First Report of Powdery Mildew Caused by Erysiphe heraclei on Curled Dock (Rumex crispus) in South Korea. Plant Dis 2013;97(3):427", doi("10.1094/PDIS-10-12-0904-PDN"), "American Phytopathological Society (PubMed)", A),
 ("Evaluation of α-Glucosidase Inhibition and Antihyperglycemic Activity of Extracts Obtained from Leaves and Flowers of Rumex crispus L. Molecules 2023;28(15):5760 (PMC10420655)", doi("10.3390/molecules28155760"), "MDPI (PubMed Central)", A),
 ("Variation in Phenolic Compounds Content and Antioxidant Activity of Different Plant Organs from Rumex crispus L. and Rumex obtusifolius L. at Different Growth Stages. Antioxidants (Basel) 2019;8(7):237 (PMC6680865)", doi("10.3390/antiox8070237"), "MDPI (PubMed Central)", A),
 ("Antimalarial activity of nepodin isolated from Rumex crispus. Arch Pharm Res 2013", pm("23440579"), "PubMed (PMID 23440579)", A),
 ("Molecular mechanisms of anti-inflammatory effect of chrysophanol, an active component of AST2017-01 on atopic dermatitis in vitro models. Int Immunopharmacol 2018", doi("10.1016/j.intimp.2017.11.019"), "Elsevier (PubMed PMID 29161660)", A),
 ("Anti-inflammatory effects of Beopje curly dock (Rumex crispus L.) in LPS-induced RAW 264.7 cells and its active compounds. J Food Biochem 2020;44(7):e13291", doi("10.1111/jfbc.13291"), "Wiley (PubMed PMID 32458452)", A),
 ("Preventive effect of Rumex crispus L. on surgically induced intra-abdominal adhesion model in rats. Daru 2021;29(1):101-115 (PMC8149542)", doi("10.1007/s40199-021-00387-8"), "Springer (PubMed)", A),
 ("Determination of antioxidant and antimicrobial activities of Rumex crispus L. extracts. J Agric Food Chem 2001;49(8):4083-9", doi("10.1021/jf0103572"), "American Chemical Society (PubMed PMID 11513714)", A),
 ("Correlation between the magnitude of skin prick test reactivity and pollen-specific serum IgE levels in patients with respiratory allergy. Rev Alerg Mex 2014;61(1):3-8", pm("24912996"), "PubMed (PMID 24912996)", A),
 ("Screening extracts of Achyranthes japonica and Rumex crispus for activity against various plant pathogenic fungi and control of powdery mildew. Pest Manag Sci 2004;60(8):803-8", doi("10.1002/ps.811"), "Wiley (PubMed PMID 15307672)", A),
 ("EFSA NDA Panel. Scientific Opinion on additional scientific data related to the safety of preparations of Rheum, Cassia, Rhamnus and Frangula (hydroxyanthracene derivatives). EFSA Journal 2024;22(5):e8766 (PMC11112454)", doi("10.2903/j.efsa.2024.8766"), "유럽식품안전청(EFSA)", A),
 ("New seco-anthraquinone glucoside from the roots of Rumex crispus. Nat Prod Bioprospect 2022 (PMC9346041)", doi("10.1007/s13659-022-00350-3"), "Springer (PubMed)", A),
 ("Consequences of incongruency in diurnally varying resources for seedlings of Rumex crispus (Polygonaceae). Am J Bot 1998;85(9):1216-23", pm("21685006"), "PubMed (PMID 21685006)", A),
 ("Complete chloroplast genome sequence determination of Rheum species and comparative chloroplast genomics for the members of Rumiceae. Plant Cell Rep 2020;39(6):811-824", doi("10.1007/s00299-020-02532-0"), "Springer (PubMed PMID 32221666)", A),
 ("First Report of Colletotrichum destructivum on Curly Dock. Plant Dis 2002;86(11):1271", doi("10.1094/PDIS.2002.86.11.1271A"), "American Phytopathological Society (PubMed)", A),
 ("Rumex crispus and Cordyceps militaris Mixture Ameliorates Production of Pro-Inflammatory Cytokines Induced by Lipopolysaccharide in C57BL/6 Mice Splenocytes. Prev Nutr Food Sci 2018;23(4):374-381 (PMC6342531)", doi("10.3746/pnf.2018.23.4.374"), "한국식품영양과학회 (PubMed Central)", A),
 ("Cloning and characterization of dispersed repetitive DNA derived from microdissected sex chromosomes of Rumex acetosa. Genome 2006;49(2):114-21", doi("10.1139/g05-089"), "Canadian Science Publishing (PubMed PMID 16498461)", A),
 ("Aero-allergens in canine atopic dermatitis in southeastern Australia based on 1000 intradermal skin tests. Aust Vet J 2000;78(6):392-9", doi("10.1111/j.1751-0813.2000.tb11824.x"), "Wiley (PubMed PMID 10920777)", A),
 ("Evaluation of the Bioactivities of Rumex crispus L. Leaves and Root Extracts Using Toxicity, Antimicrobial, and Antiparasitic Assays. Evid Based Complement Alternat Med 2019:6825297 (PMC6885263)", doi("10.1155/2019/6825297"), "Hindawi (PubMed Central)", A),
]
sources = [{"n": i+1, "title": t, "url": u, "publisher": p, "accessed": a} for i,(t,u,p,a) in enumerate(S)]

sections = [
{"key":"overview","title":"한눈에 보기","body":
"소리쟁이(Rumex crispus L.)는 마디풀과(Polygonaceae) 소리쟁이속의 여러해살이풀로, 영어로는 curly dock 또는 yellow dock이라 부른다[1][2]. 유럽과 서아시아가 원산이지만 지금은 온대 지역 곳곳에 귀화해 길가·강둑·농경지·빈터에서 흔히 자란다[11][14].\n\n"
"식품의약품안전처 「식품원료 목록」에서 소리쟁이는 식품에 사용할 수 있는 원료(사용가능)이며, 사용 조건은 '사용가능부위 : 잎'이다[1]. 목록에는 소리쟁이분말·소리쟁이어린잎·소리쟁이잎·소리쟁이추출물·소리쟁이추출액의 5개 원료명과 긴소루쟁이·긴잎소루쟁이·야대황·양제라는 다른 이름이 올라 있다[1]. 건강기능식품 고시형 원료의 원재료로 쓰인다는 기록은 확인하지 못함.\n\n"
"어린잎은 샐러드·수프·나물로 먹는데, 다 자란 잎은 옥살산이 더 많아 더 쓰다고 한다[3]. 뿌리에는 에모딘·크리소파놀·피스시온 같은 안트라퀴논이 많아 민간에서 완하제(설사약)로 쓰였고, 유럽식품안전청(EFSA)은 이 계열(하이드록시안트라센 유도체)에 유전독성·발암 우려가 있다고 판단했다[2][6][8]. 소리쟁이를 먹은 사람과 양이 옥살산 중독으로 숨진 사례도 보고되어 있어, 허용 부위인 잎만 적은 양으로 먹는 것이 안전하다는 점을 기억할 필요가 있다[1][4][5]."},
{"key":"history","title":"역사","body":
"소리쟁이는 여러 나라에서 수렴제·완하제·이뇨제·강장제·혈액 정화제·진경제·이담제로 쓰인 오랜 민간 약초다[2]. 뿌리는 습포나 말린 가루로 만들어 종기·궤양·상처 같은 피부병에 붙였다고 전한다[7]. 열매(씨)는 이질에 썼고, 어린잎은 특히 봄철 채소로 먹었다[16]. 멕시코 등에서는 어린잎을 수프와 샐러드로 먹고 씨를 과자에 넣거나 커피 대용으로 썼다고 정리되어 있다[15].\n\n"
"터키에서는 'Labada'라 부르며 산후 합병증·불임 같은 부인과 질환에 썼다고 보고된다[20]. 아시아에서는 소화불량과 피부병에 민간약으로 널리 쓰였다[14]. 한국 전통의학에서도 뿌리를 출혈과 피부병 치료에 써 왔다고 소개된다[10]. 최근 한국에서는 소리쟁이와 동충하초(Cordyceps militaris)를 섞은 소재가 한약재나 기능성 식품으로 소비되어 왔다는 연구 보고가 있다[18].\n\n"
"식품원료 목록의 다른 이름 '양제'는 한약명 羊蹄와 같지만, 한국 고문헌의 '양제'가 소리쟁이(R. crispus)를 가리키는지는 이번 조사에서 원문으로 확인하지 못함."},
{"key":"biology","title":"식물학적 특징","body":
"소리쟁이는 여러해살이풀로, 뿌리잎(로제트 잎)이 땅 가까이 붙어 자란다[26]. 6–7월에 꽃이 피며 바람으로 꽃가루받이를 하고, 제꽃가루받이(자가수정)도 할 수 있다[11]. 한 포기가 휴면하지 않는 씨를 수백에서 수천 개 맺고, 땅에 묻힌 씨는 수십 년 동안 살아 있기도 하며, 흙의 비옥도에 따라 생장 차이가 크다[11].\n\n"
"한국에서는 귀화식물 또는 외래종으로 분류되며, 국내 전문기관은 개항기부터 1921년 사이 또는 1945년 이후에 들어온 것으로 본다[11]. 다만 국제 식물 데이터베이스와 일부 국내 학자는 빙하기 이후 자생했을 가능성도 제기한다[11].\n\n"
"이 종에서는 안트라퀴논·나프탈렌 유도체·플라보노이드·정유·쿠마린·스틸벤 등 약 224종의 성분이 분리·확인되었다[2]. 남아프리카공화국 야생 개체를 분석한 연구에서 말린 잎은 조단백질 26.37%, 회분 15.35%로 뿌리(단백질 3.75%, 회분 6.22%)보다 높았고, 뿌리는 탄수화물(57.74%)과 칼슘이 더 많았다[3]. 같은 연구에서 생잎의 비타민 C(아스코르브산 당량)는 100 g당 159.73 mg이었다[3]. 터키 시료에서는 잎과 씨의 열수 추출물이 리놀레산 과산화를 각각 96%와 94% 억제했고, 총페놀은 씨 에탄올 추출물에 가장 많았다[21]."},
{"key":"related_species","title":"근연종","body":
"소리쟁이속(Rumex)에는 약 200종이 있으며, 대황속(Rheum)과 함께 하이드록시안트라퀴논을 특징적으로 만드는 무리로 꼽힌다[7][9]. 소리쟁이·대황속 식물과 산소리쟁이속(Oxyria)의 엽록체 유전체를 비교한 연구에서 이들 마디풀과 식물은 같은 무리로 묶였다[27].\n\n"
"한국에서는 소리쟁이와 돌소리쟁이(R. obtusifolius)의 중간 형태를 띤 개체가 두 종의 자연 잡종임이 핵 DNA(pgiC)와 엽록체 DNA 5개 구간 분석으로 처음 확인되었고, 교잡은 양방향으로 일어났다[12]. 같은 연구는 한국의 참소리쟁이(R. japonicus) 집단이 잡종에서 유래했을 가능성이 크며 소리쟁이가 그 부모 종 가운데 하나일 수 있다고 보았다[12]. 소리쟁이와 돌소리쟁이는 서로 교잡하는 경향이 강해 시료를 멀리 떨어진 곳에서 따로 채집했다는 보고도 있다[16].\n\n"
"식품원료 목록에는 수영(R. acetosa)·참소리쟁이·애기수영·돌소리쟁이·금소리쟁이·Rumex patientia 같은 같은 속 원료가 따로 올라 있으며, 이 자료에는 그 종들의 성분·안전성 값을 섞지 않았다[1]. 근연 약용식물인 대황속 뿌리 제제에 대해 EFSA는 2024년에도 유전독성 우려 때문에 안전성을 확립할 수 없다고 판단했다[24]."},
{"key":"cultivation","title":"재배와 채취","body":
"소리쟁이를 작물로 재배한 국내 생산 통계(면적·생산량)는 확인하지 못함. 주로 길가·강둑·농경지·교란지에서 자라는 야생 개체를 채취하며, 한국에서는 강가(하천 둔치) 집단이 널리 퍼져 있다[11]. 흙의 수분과 양분에 민감해, 부영양화된 하천 둔치에서 빠르게 자라고 휴면 없는 씨로 다시 퍼지는 것으로 해석된다[11].\n\n"
"넓은 생태적 적응력과 높은 확산력 때문에 여러 나라에서 유해 잡초나 관리 대상 종으로 지정되어 있다[11]. 확산을 막으려면 번식기나 꽃이 피기 전에 베어 내는 관리가 효과적일 수 있다고 제안된다[11]. 하천 골재 준설 과정에서 씨나 뿌리 조각이 다른 지역으로 옮겨졌을 가능성도 제기되었다[11].\n\n"
"국내에서는 충남 서해안 구릉지의 소리쟁이 잎에서 탄저병(Colletotrichum destructivum)이, 광주 하천변 개체에서 흰가루병(Erysiphe heraclei)이 처음 보고되었다[28][14]. 한편 소리쟁이 뿌리 메탄올 추출물은 보리 흰가루병을 효과적으로 억제해 식물 병 방제 소재로도 연구되었다[23]. 먹을 잎은 봄철 어린잎을 쓰는데, 잎이 자랄수록 옥살산이 늘고 쓴맛이 강해진다[3][16]."},
{"key":"processing","title":"가공과 이용","body":
"식품원료 목록에 오른 소리쟁이 원료는 분말·어린잎·잎·추출물·추출액 형태이며, 사용 부위는 잎으로 한정된다[1]. 말리면 잎의 비타민 C가 100 g당 159.73 mg(생잎)에서 26.73 mg(건조 잎)으로 크게 줄었다[3]. 남아프리카 연구진은 말린 잎과 뿌리의 수분이 각각 7.57%와 7.59%로 낮아 저장성이 좋다고 보았다[3].\n\n"
"한국에서는 독성을 줄이고 효과를 높이는 전통 가공법인 '법제(Beopje)'를 소리쟁이에 적용한 연구가 있으며, 법제한 추출물이 세포 실험에서 더 강한 항염 효과를 보였다[19]. 소리쟁이와 동충하초를 6:4로 섞은 혼합물과 이를 넣은 시판 건강음료를 쥐 비장세포에 처리한 연구도 있다[29]. 뿌리 물 추출물은 말린 소리쟁이 50 g을 물 1 L에 넣고 3시간 끓인 뒤 걸러 동결건조해 만들었다[10].\n\n"
"분석·가공 때 물이 많은 용매나 높은 온도를 쓰면 안트라퀴논 배당체가 에모딘·크리소파놀·피스시온 같은 아글리콘으로 가수분해된다[9]. 소리쟁이속 식물의 옥살산이 추출액을 산성으로 만들어 이 가수분해를 돕는 것으로 추정된다[9]. 식약처 「식품 등의 생산실적」에서 소리쟁이 원료 품목의 생산 기록은 확인하지 못함."},
{"key":"genetics","title":"유전체와 유전 다양성","body":
"소리쟁이의 엽록체 유전체는 158,851 bp이며, 단백질 암호화 유전자 77개·tRNA 30개·rRNA 4개를 합해 111개의 고유 유전자가 예측되었다[13]. 한국 개체의 전장 유전체 조립본(NCBI BioSample SAMN50897494)을 바탕으로 이 종 전용 마이크로새틀라이트(SSR) 표지 19개가 개발되었다[11].\n\n"
"이 표지로 금강·낙동강 유역 등 6개 하천변 집단 120개체를 분석한 결과 대립유전자 166개, 평균 다형정보량(PIC) 0.637이 확인되었다[11]. 관측 이형접합도(Ho 0.304)가 기대 이형접합도(He 0.588)보다 낮고 근교계수(F)가 0.456–0.559여서 근친 교배 경향이 뚜렷했다[11]. 집단 간 유전적 분화는 AMOVA 기준 10%로 낮았지만, 공간 베이즈 군집 분석에서는 6개 집단이 각각 독립된 유전 단위로 나뉘었다[11].\n\n"
"소리쟁이속은 종 사이와 종 안에서 배수성(ploidy) 변이가 크고 잡종이 흔하며, 소리쟁이도 지역마다 배수성이 다르다고 보고된다[11]. 이 종의 정확한 염색체 수는 이번 조사에서 확인하지 못함. 성염색체 관련 반복 DNA 연구에서 소리쟁이는 암수딴그루가 아닌 종으로 분류되어, 수영(R. acetosa)의 반복 DNA가 덜 보존된 종 가운데 하나였다[30]."},
{"key":"safety","title":"안전성","body":
"소리쟁이는 건강기능식품 고시형 원료가 아니어서 고시에 따른 섭취 시 주의사항은 확인하지 못함. 식품원료 목록상 사용할 수 있는 부위는 잎뿐이며, 안트라퀴논이 많은 뿌리는 식품원료로 허용되지 않았다[1][8].\n\n"
"가장 큰 위험은 옥살산이다[4][5]. 미국에서 소리쟁이가 무성한 우리에 들어간 암양 100마리 가운데 10마리가 40시간 안에 급성 옥살산 중독(저칼슘혈증·질소혈증)을 일으켰고, 채취한 소리쟁이속 시료의 옥살산은 건조중량의 6.6–11.1%였다[4]. 스페인에서는 소리쟁이를 먹은 53세 남성이 위장 증상·심한 저칼슘혈증·대사성 산증·급성 간부전 끝에 72시간 만에 숨졌고, 간과 신장에서 옥살산 결정이 확인되었다[5]. 반면 남아프리카 연구는 잎의 옥살산을 0.15 mg/g으로 낮게 보고해, 측정법과 시료에 따라 값이 크게 다르다[3].\n\n"
"EFSA는 에모딘·알로에에모딘이 유전독성을 보인다며 하이드록시안트라센 유도체를 반대 근거가 없는 한 유전독성·발암성 물질로 보아야 하고, 안전한 1일 섭취량을 정할 수 없다고 결론지었다[6]. 종설은 소리쟁이가 독성이 있고 알레르기와 증상성 혈소판감소증 같은 이상반응이 보고되었다고 정리했다[2]. 꽃가루는 호흡기 알레르기의 원인으로 검사되며, 개의 아토피 피부염 피내 검사에서도 15% 넘게 반응했다[22][31]. 뿌리 추출물은 잎 추출물보다 브라인슈림프·HeLa 세포 독성이 컸다[32]. 국내 공공기관의 알레르기·잔류농약 정보는 확인하지 못함."},
]

compounds = [
 {"name":"Emodin","name_ko":"에모딘","class":"안트라퀴논(하이드록시안트라센 유도체)","role":"marker","part":"뿌리(에탄올 추출물 분획)","content_text":"디클로로메탄 분획 1 g당 160.43 mg, 헥산 분획 1 g당 14.64 mg[8]","activity_ko":"MRSA 억제 활성을 보이는 대표 성분(MIC 200 µg/mL)[7]; EFSA가 유전독성을 지적한 성분[6]","source":[7,8,6]},
 {"name":"Chrysophanol","name_ko":"크리소파놀","class":"안트라퀴논","role":"marker","part":"뿌리(에탄올 추출물 분획)","content_text":"디클로로메탄 분획 1 g당 66.96 mg, 헥산 분획 1 g당 48.64 mg[8]","activity_ko":"소리쟁이·동충하초 혼합물의 활성 성분으로 비만세포·각질세포 염증 반응 억제(세포)[18]","source":[8,18]},
 {"name":"Physcion","name_ko":"피스시온","class":"안트라퀴논","role":"bioactive","part":"뿌리(에탄올 추출물 분획)","content_text":"디클로로메탄 분획 1 g당 34.90 mg, 헥산 분획 1 g당 15.43 mg[8]","activity_ko":"뿌리 물 추출물에서 HPLC로 확인, 파골세포 분화 억제(세포)[10]","source":[8,10]},
 {"name":"Emodin 8-glucoside","name_ko":"에모딘-8-O-글루코사이드","class":"안트라퀴논 배당체","role":"bioactive","part":"뿌리","content_text":"정량값은 본문에서 확인하지 못함; 물이 많은 용매·고온 추출에서 에모딘으로 가수분해됨[9]","activity_ko":"배당체가 장에서 완하 작용을 하는 하이드록시안트라퀴논의 주된 형태[9]","source":[9]},
 {"name":"Chrysophanol 8-glucoside","name_ko":"크리소파놀-8-O-글루코사이드","class":"안트라퀴논 배당체","role":"bioactive","part":"뿌리","content_text":"정량값은 본문에서 확인하지 못함; 메탄올–물(80:20) 10분 가압추출에서도 크리소파놀이 생성됨[9]","activity_ko":"뿌리에서 분리해 표준품으로 사용(순도 95% 이상)[9]","source":[9]},
 {"name":"Physcion 8-glucoside","name_ko":"피스시온-8-O-글루코사이드","class":"안트라퀴논 배당체","role":"bioactive","part":"뿌리","content_text":"정량값은 본문에서 확인하지 못함[9]","activity_ko":"75 °C 넘는 추출 온도에서 빠르게 줄어드는 불안정한 배당체[9]","source":[9]},
 {"name":"Nepodin","name_ko":"네포딘","class":"나프탈렌 유도체","role":"bioactive","part":"전초(70% 에탄올 추출물)","content_text":"함량은 확인하지 못함; 활성 유도 분획으로 분리[17]","activity_ko":"말라리아 원충 PfNDH2 효소 억제·항말라리아 활성[17]","source":[17,16]},
 {"name":"Crispuside A","name_ko":"크리스푸사이드 A","class":"세코-안트라퀴논 배당체","role":"bioactive","part":"뿌리","content_text":"신규 성분으로 분리(함량 미보고)[25]","activity_ko":"피부 진균 대상 항진균·항염 활성은 대부분 약했음[25]","source":[25]},
 {"name":"Oxalic acid","name_ko":"옥살산(수산)","class":"유기산(항영양소)","role":"bioactive","part":"잎·지상부","content_text":"잎 0.15 ± 0.019 mg/g, 뿌리 0.11 ± 0.0033 mg/g(남아프리카 시료)[3]; 소리쟁이속 시료 건조중량의 6.6–11.1%(미국 중독 현장)[4]","activity_ko":"칼슘과 결합해 저칼슘혈증·신장 손상(옥살산 중독)을 일으킴[4][5]","source":[3,4,5]},
 {"name":"Phytic acid","name_ko":"피트산","class":"항영양소","role":"bioactive","part":"잎·뿌리(건조 분말)","content_text":"잎 1.15 ± 0.74%, 뿌리 1.38 ± 0.27%[3]","activity_ko":"무기질과 결합해 흡수를 낮출 수 있는 항영양소[3]","source":[3]},
 {"name":"Ascorbic acid","name_ko":"비타민 C(아스코르브산)","class":"비타민","role":"nutrient","part":"잎","content_text":"생잎 100 g당 159.73 ± 26.77 mg, 건조 잎 26.73 ± 4.46 mg[3]","activity_ko":"수용성 항산화 비타민; 건조하면 크게 줄어듦[3]","source":[3]},
 {"name":"alpha-Tocopherol","name_ko":"비타민 E(α-토코페롤)","class":"비타민","role":"nutrient","part":"잎","content_text":"생잎 100 g당 53.87 ± 0.21 mg, 건조 잎 54.71 ± 0.38 mg(비색법)[3]","activity_ko":"지용성 항산화 비타민[3]","source":[3]},
 {"name":"Quercitrin","name_ko":"퀘르시트린","class":"플라보놀 배당체","role":"bioactive","part":"잎 메탄올 추출물","content_text":"UHPLC-MS 상대 피크 면적 21.06%(잎 추출물 최대 피크)[15]","activity_ko":"α-글루코시다아제 억제 추출물의 주요 성분으로 추정[15]","source":[15]},
 {"name":"Quercetin 7-glucuronide","name_ko":"퀘르세틴-7-글루쿠로나이드","class":"플라보놀 배당체","role":"bioactive","part":"잎 메탄올 추출물","content_text":"UHPLC-MS 상대 피크 면적 8.77%[15]","activity_ko":"잎 추출물의 두 번째 주요 피크[15]","source":[15]},
 {"name":"Epicatechin 3-O-gallate","name_ko":"(-)-에피카테킨-3-O-갈레이트","class":"플라반-3-올","role":"bioactive","part":"꽃·잎 메탄올 추출물","content_text":"꽃 추출물 11.22%, 잎 추출물 0.33%(상대 피크 면적)[15]","activity_ko":"α-글루코시다아제 억제 활성과 관련된 성분으로 제안[15]","source":[15]},
]

assays = [
 {"role":"literature","compound":"Oxalic acid","compound_ko":"옥살산(옥살레이트)","part":"잎·뿌리(건조 분말)",
  "content":"잎 0.15 ± 0.019 mg/g(결과 본문 표기는 mg/mg), 뿌리 0.11 ± 0.0033 mg/g[3]",
  "method":"과망간산칼륨(KMnO4) 적정법",
  "conditions":{"instrument":"","column":"","mobile_phase":"","gradient":"","flow":"","temp":"","detection":"0.05 M KMnO4 적정, 적갈색이 지속될 때를 종말점으로 함",
   "injection":"","sample_prep":"분말 시료 1 g(3반복)을 3 M 황산 75 mL에 넣어 1시간 자석 교반 후 여과, 여액 5 mL를 적정","standard":"0.05 M KMnO4 1 mL = 옥살레이트 2.2 mg","linearity":"","lod":"","loq":"","recovery":""},
  "rationale":"식품 부위인 잎의 안전성 지표(항영양소·중독 원인 물질)로, 같은 종의 잎과 뿌리를 직접 정량한 자료다[3]. 다른 보고(건조중량의 6.6–11.1%)와 수천 배 차이가 나서 측정법·시료 차이를 감안해 읽어야 한다[4].",
  "source":[3,4],"url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC6473742/","source_kind":"paper"},
 {"role":"literature","compound":"Chrysophanol","compound_ko":"크리소파놀·에모딘·피스시온(안트라퀴논 5종 동시)","part":"뿌리 에탄올 추출물과 용매 분획",
  "content":"디클로로메탄 분획 1 g당 크리소파놀 66.96 mg, 에모딘 160.43 mg, 피스시온 34.90 mg; 헥산 분획 1 g당 48.64·14.64·15.43 mg; 물 분획 불검출[8]",
  "method":"HPLC-PDA",
  "conditions":{"instrument":"Shimadzu Prominence HPLC-PDA","column":"YMC Triart C18, 250 × 4.6 mm, 5 µm","mobile_phase":"A: 0.1% TFA 수용액, B: 0.1% TFA 메탄올",
   "gradient":"0–5분 20% B; 5–15분 20→80%; 15–30분 80→90%; 30–35분 90→100%; 35–40분 100% B","flow":"1.0 mL/min","temp":"40 °C","detection":"450 nm (머무름 시간: 알로에에모딘 22.2, 레인 23.7, 에모딘 27.3, 크리소파놀 29.9, 피스시온 33.2분)",
   "injection":"","sample_prep":"말린 뿌리 분말을 10배량 에탄올로 12시간 환류 추출(3회), 감압 농축 후 물에 현탁해 헥산·디클로로메탄·에틸아세테이트·부탄올·물로 차례로 분획","standard":"알로에에모딘·크리소파놀·에모딘·피스시온·레인 표준품","linearity":"","lod":"","loq":"","recovery":""},
  "rationale":"뿌리의 주요 안트라퀴논 3종을 표준품으로 정량해 분획별 함량을 비교했다[8]. 검출·정량한계와 회수율은 본문에 없어 비워 둠.",
  "source":[8],"url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC7464605/","source_kind":"paper"},
 {"role":"literature","compound":"Emodin 8-glucoside","compound_ko":"에모딘·크리소파놀·피스시온의 8-O-글루코사이드와 아글리콘(6종 동시)","part":"뿌리(풍건, 40–70 mesh)",
  "content":"개별 함량은 그림으로만 제시되어 본문 숫자는 확인하지 못함[9]",
  "method":"HPLC-PDA (HPLC/ESI/MS로 동정 확인)",
  "conditions":{"instrument":"Dionex 액체크로마토그래프(GP50 펌프, AD25 흡광 검출기, PDA100)","column":"Prodigy ODS-3, 250 × 4.6 mm, 5 µm (Phenomenex) + 보호 칼럼","mobile_phase":"A: 아세트산 수용액(빙초산 0.5 mL/100 mL), B: 메탄올",
   "gradient":"0–30분 B 45→85%; 85% B 10분 유지; 2분간 85→45%; 45% B 5분 재평형","flow":"1 mL/min (LC-MS는 0.5 mL/min)","temp":"30 °C","detection":"UV 254 nm, PDA 190–750 nm; ESI(−) 이온트랩 MS, m/z 100–1,000",
   "injection":"25 µL 루프","sample_prep":"뿌리 분말 2.0 g을 끓는 메탄올로 30분씩 3회 환류 추출해 200 mL로 정용; 또는 0.5 g을 중성 유리와 섞어 가압액체추출(PLE)","standard":"에모딘·크리소파놀·피스시온(시판), 세 가지 8-O-글루코사이드(뿌리에서 분리, 순도 95% 이상)",
   "linearity":"2.5–100.0 µg/mL, 5농도, r > 0.997","lod":"0.0623–0.1624 µg/mL","loq":"","recovery":"PLE 1회 추출 회수율 98.5% 초과(RSD < 7%, n = 5)"},
  "rationale":"완하 작용과 부작용의 중심인 배당체·아글리콘을 함께 재는 방법이며, 물이 많은 용매·고온에서 배당체가 가수분해되어 결과가 왜곡된다는 점을 보여 준다[9].",
  "source":[9],"url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC3992226/","source_kind":"paper"},
 {"role":"literature","compound":"Emodin","compound_ko":"에모딘","part":"뿌리 메탄올 추출물(에틸아세테이트 분배층)과 분획",
  "content":"추출물·분획별 정량값은 표로만 제시되어 본문 숫자는 확인하지 못함; 분획 3에서 가장 많았음[7]",
  "method":"UPLC-HRMS(Orbitrap)",
  "conditions":{"instrument":"Waters Acquity UPLC + Thermo Q-Exactive Plus 질량분석기","column":"Acquity BEH C18, 2.1 × 50 mm, 1.7 µm (Waters)","mobile_phase":"A: 0.1% 포름산 수용액, B: 0.1% 포름산 아세토니트릴",
   "gradient":"0–0.5분 A:B 90:10; 0.5–8.0분 0:100까지; 100% B 0.5분 유지; 0.5분간 초기 조건 복귀; 9.0–10.0분 유지","flow":"0.3 mL/min","temp":"","detection":"ESI(−), m/z 150–1,500, 분무 전압 3.20 kV, 모세관 256 °C; 에모딘 [M−H]− m/z 269.0457, 머무름 시간 5.23분",
   "injection":"3 µL (메탄올 1 mg/mL)","sample_prep":"생뿌리를 37 °C에서 24시간 건조·분쇄, 메탄올(160 g/L) 24시간 침지 3회, 헥산 분배 후 에틸아세테이트 분배, 1% NaCl로 세척해 탄닌 제거, 실리카 플래시 크로마토그래피로 분획","standard":"에모딘(순도 97% 이상) 메탄올 검량선, R² = 0.9961",
   "linearity":"R² = 0.9961","lod":"검량선에서 잔차 25% 미만인 최저 농도로 정의(수치는 본문에 없음)","loq":"","recovery":""},
  "rationale":"뿌리의 알려진 항균 성분인 에모딘을 정량해 분획별 항MRSA 활성을 예측하는 지표로 썼다[7]. 정량한계·회수율은 본문에 없어 비워 둠.",
  "source":[7],"url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC9035478/","source_kind":"paper"},
]

nutrients = [{"form":"소리쟁이 잎(남아프리카공화국 야생, 상온 건조 분말)","basis":"건조 분말 100 g(일반성분은 %)","items":[
 {"name":"수분","value":7.57,"unit":"%"},{"name":"회분","value":15.35,"unit":"%"},{"name":"조지방","value":2.01,"unit":"%"},
 {"name":"조단백질","value":26.37,"unit":"%"},{"name":"중성세제섬유(NDF)","value":46.02,"unit":"%"},{"name":"비섬유 탄수화물","value":10.25,"unit":"%"},
 {"name":"에너지","value":688.72,"unit":"kJ"},{"name":"칼륨","value":5600.0,"unit":"mg"},{"name":"칼슘","value":635.0,"unit":"mg"},
 {"name":"마그네슘","value":445.0,"unit":"mg"},{"name":"인","value":515.0,"unit":"mg"},{"name":"나트륨","value":280.0,"unit":"mg"},
 {"name":"철","value":28.70,"unit":"mg"},{"name":"아연","value":4.10,"unit":"mg"},{"name":"구리","value":1.15,"unit":"mg"},{"name":"망간","value":10.95,"unit":"mg"}],
 "source":[3]}]

d = {"slug":"rumex-crispus","name_ko":"소리쟁이","name_en":"Curly dock (yellow dock)","scientific_name":"Rumex crispus L.",
 "aliases":["긴소루쟁이","긴잎소루쟁이","야대황","양제","Curly dock","Curled dock","Yellow dock","Lapathum crispum Scop.","Rumex coreanus Nakai"],
 "sections":sections,"compounds":compounds,"markers":[],"assays":assays,"nutrients":nutrients,
 "production":[],"world":[],"gi":[],"orgs":[],"sources":sources}
OUT.write_text(json.dumps(d,ensure_ascii=False,indent=1),encoding="utf-8")
for s in sections: print(s["key"], len(s["body"]))
print(len(sources))
