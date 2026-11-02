import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
ACC = "2026-11-02"
MF = "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020"
def pm(pmid): return f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
def pmc(p): return f"https://pmc.ncbi.nlm.nih.gov/articles/{p}/"
S = [
 (1, "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 솜대 3개 원료명 행(학명 'Phyllostachys nigra Munro var. henonis Stapf', 다른 이름 '대나무, 분죽, 담죽'): 솜대순(부위 순)·솜대잎(부위 잎) 사용가능, 솜대줄기(부위 줄기) 사용불가, 조건 '사용가능부위 : 순, 잎'. 로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json", MF, "식품의약품안전처", "2026-10-13"),
 (2, "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 오죽 3개 원료명 행(학명 'Phyllostachys nigra (Lodd. ex Lindl.) Munro', 다른 이름 '검정대, 흑죽, 분죽'): 오죽잎(부위 잎)·오죽죽순(부위 새순(죽순)) 사용가능, 오죽줄기(부위 줄기) 사용불가, 조건 '사용가능부위 : 죽순, 잎'. 로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json", MF, "식품의약품안전처", "2026-10-13"),
 (3, "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 죽력 행(학명 'Phyllostachys nigra Munro var. henonis Stapf / Phyllostachys bambusoides Sieb. et Zucc.', 다른 이름 '솜대, 왕대', 부위 '마디줄기를 태울 때 유출되는 즙액', 제한적사용, 조건 '제한적사용가능부위 : 마디줄기를 태울 때 유출되는 즙액※(죽력), 주류의 원료로만 사용'). 로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json", MF, "식품의약품안전처", "2026-10-13"),
 (4, "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 관련 행: 왕대(Phyllostachys bambusoides Siebold & Zucc.) 왕대죽순·왕대잎·왕대수액 사용가능, 왕대줄기 사용불가, 조건 '사용가능부위 : 죽순(줄기 제외), 잎, 수액'; 죽순대(Phyllostachys pubescens / P. heterocycla f. pubescens) 죽순·잎·수액 사용가능, 조건 '사용가능부위 : 죽순, 잎, 수액'; 마디대순(Phyllostachys bambusoides var. aurea) 사용가능, 조건 '사용가능부위 : 순'; Bambusoidae 대나무죽순·건조죽순·대나무죽순잎주스 등 사용가능, 조건 '사용가능부위 : 새순(죽순), 잎, 수액'; 조릿대(Sasa borealis) 제한적사용, 조건 '제한적사용가능부위 : 잎, 침출차에 한함'. 로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json", MF, "식품의약품안전처", "2026-10-13"),
 (5, "Does monocarpic Phyllostachys nigra var. henonis regenerate after flowering in Japan? Insights from 3 years of observation after flowering. PLoS One 2023;18(6):e0287114 (PMID 37307263, PMC10259779, 전문 확인)", pmc("PMC10259779"), "PLoS One (PubMed Central)", ACC),
 (6, "Henon bamboo flowering recorded first time in 120 years revealed how [fungus] affects the floral organs of the host. Mycoscience 2024;65(5):228-234 (PMID 39720017, 초록 확인)", pm("39720017"), "Mycoscience (PubMed)", ACC),
 (7, "Antioxidant and Compositional HPLC Analysis of Three Common Bamboo Leaves. Molecules 2020;25(2):409 (PMID 31963759, PMC7024249, 전문 확인 — 표 수치는 전문 텍스트에 없음)", pmc("PMC7024249"), "Molecules (PubMed Central)", ACC),
 (8, "The compound isolated from the leaves of Phyllostachys nigra protects oxidative stress-induced retinal ganglion cells death. Food Chem Toxicol 2010;48(6):1721-7 (PMID 20381571, 초록 확인)", pm("20381571"), "Food and Chemical Toxicology (PubMed)", ACC),
 (9, "Aldose reductase and advanced glycation endproducts inhibitory effect of Phyllostachys nigra. Biol Pharm Bull 2007;30:1569 (PMID 17666823, 초록 확인)", pm("17666823"), "Biological & Pharmaceutical Bulletin (PubMed)", ACC),
 (10, "Evaluation of antioxidant and prooxidant activities of bamboo Phyllostachys nigra var. Henonis leaf extract in vitro. J Agric Food Chem 2000;48(8):3170-6 (PMID 10956087, 초록 확인)", pm("10956087"), "Journal of Agricultural and Food Chemistry (PubMed)", ACC),
 (11, "[Comparison study on total flavonoid content and anti-free radical activity of the leaves of bamboo, Phyllostachys nigra, and Ginkgo biloba]. 中国中药杂志 2002;27(4):254-7 (PMID 12774365, 초록 확인)", pm("12774365"), "China Journal of Chinese Materia Medica (PubMed)", ACC),
 (12, "Optimisation of pressurised liquid extraction of antioxidants from black bamboo leaves. Food Chem 2014;154:164-70 (PMID 24518329, 초록 확인)", pm("24518329"), "Food Chemistry (PubMed)", ACC),
 (13, "In vitro inhibition of the transcription factor NF-κB and cyclooxygenase by bamboo extracts. Phytother Res 2014;28(2):224-30 (PMID 23559516, 초록 확인)", pm("23559516"), "Phytotherapy Research (PubMed)", ACC),
 (14, "Anti-oxidative, anti-inflammatory and whitening effects of phenolic compounds from Bambusae Caulis in Liquamen. Nat Prod Res 2012;26(18):1687-91 (PMID 21985061, 초록 확인)", pm("21985061"), "Natural Product Research (PubMed)", ACC),
 (15, "Cytoprotective Effect of Bambusae Caulis in Liquamen by Blocking Oxidative Stress in Hepatocytes. Molecules 2023;28(15):5862 (PMID 37570831, PMC10421324, 전문 확인 — 원료 대나무의 종은 본문에서 확인하지 못함)", pmc("PMC10421324"), "Molecules (PubMed Central)", ACC),
 (16, "Effects of Bambusae caulis in Liquamen on the development of atopic dermatitis-like skin lesions in hairless mice. J Ethnopharmacol 2009;123(2):195-200 (PMID 19429362, 초록 확인)", pm("19429362"), "Journal of Ethnopharmacology (PubMed)", ACC),
 (17, "Bambusae caulis in Liquamen Suppresses the Expression of Thymus and Activation-Regulated Chemokine and Macrophage-Derived Chemokine in Human Keratinocytes due to Antioxidant Effect. Evid Based Complement Alternat Med 2012:617494 (PMID 21785648, PMC3137989, 초록 확인)", pmc("PMC3137989"), "eCAM (PubMed Central)", ACC),
 (18, "Vasodilatation produced by orientin and its mechanism study. Biol Pharm Bull 2005;28:37 (PMID 15635160, 초록 확인)", pm("15635160"), "Biological & Pharmaceutical Bulletin (PubMed)", ACC),
 (19, "Anti-apoptotic effect and the mechanism of orientin on ischaemic/reperfused myocardium. J Asian Nat Prod Res 2006 (PMID 16864433, 초록 확인)", pm("16864433"), "Journal of Asian Natural Products Research (PubMed)", ACC),
 (20, "Dose-Response Effects of Bamboo Leaves on Rumen Methane Production, Fermentation Characteristics, and Microbial Abundance In Vitro. Animals 2022;12(17):2222 (PMID 36077942, PMC9454597, 전문 확인)", pmc("PMC9454597"), "Animals (PubMed Central)", ACC),
 (21, "PnMYB4a, a R2R3 transcription factor, modulates coumarin biosynthesis during melanization in the culms of Phyllostachys nigra. New Phytol 2026 (PMID 42870315, 초록 확인)", pm("42870315"), "New Phytologist (PubMed)", ACC),
 (22, "Integrative transcriptome and metabolome evaluation of melanin biosynthesis in [Phyllostachys nigra] during low-temperature growth. Forestry Research 2025;5:e020 (PMID 41019230, PMC12464485, 초록 확인)", pmc("PMC12464485"), "Forestry Research (PubMed Central)", ACC),
 (23, "Integrated Transcriptome and Metabolome Analyses Reveal Bamboo Culm Color Formation Mechanisms Involved in Anthocyanin Biosynthetic in [Phyllostachys nigra]. Int J Mol Sci 2024;25(3):1738 (PMID 38339012, PMC10855043, 초록 확인)", pmc("PMC10855043"), "International Journal of Molecular Sciences (PubMed Central)", ACC),
 (24, "Bamboo germplasm screening with nuclear restriction fragment length polymorphisms. Theor Appl Genet 1991 (PMID 24213443, 초록 확인)", pm("24213443"), "Theoretical and Applied Genetics (PubMed)", ACC),
 (25, "Rational metabolic-flow switching for the production of exogenous secondary metabolites in bamboo suspension cells. Sci Rep 2018;8 (PMID 30181615, PMC6123407, 초록 확인)", pmc("PMC6123407"), "Scientific Reports (PubMed Central)", ACC),
 (26, "Transcriptional alterations during proliferation and lignification in Phyllostachys nigra cells. Sci Rep 2018;8 (PMID 30054534, PMC6063902, 초록 확인)", pmc("PMC6063902"), "Scientific Reports (PubMed Central)", ACC),
 (27, "High-transcriptional activation ability of bamboo SECONDARY WALL NAC transcription factors is derived from C-terminal domain. Plant Biotechnol (Tokyo) 2022 (PMID 36349231, PMC9592943, 초록 확인)", pmc("PMC9592943"), "Plant Biotechnology (PubMed Central)", ACC),
 (28, "Bamboo shoots: a novel source of nutrition and medicine. Crit Rev Food Sci Nutr 2013;53(5):517-34 (PMID 23391018, 초록 확인 — 대나무 죽순 전반의 총설, 이 종의 측정값 아님)", pm("23391018"), "Critical Reviews in Food Science and Nutrition (PubMed)", ACC),
 (29, "Original Research: Extract of Bambusae Caulis in Taeniam inhibits cigarette smoke-induced pulmonary and intestinal inflammation. Exp Biol Med 2017;242(1):102-112 (PMID 27590499, PMC5206982, 초록 확인)", pmc("PMC5206982"), "Experimental Biology and Medicine (PubMed Central)", ACC),
 (30, "Hypolipidemic effect of MeOH extract of Bambusae Caulis in Taeniam in hyperlipidemia induced by Triton WR-1339 and high cholesterol diet in rats. Immunopharmacol Immunotoxicol 2009;31(3):439-45 (PMID 19267283, 초록 확인)", pm("19267283"), "Immunopharmacology and Immunotoxicology (PubMed)", ACC),
 (31, "Bamboo Stems (Phyllostachys nigra variety henosis) Containing Polyphenol Mixtures Activate Nrf2 and Attenuate Phenylhydrazine-Induced Oxidative Stress and Liver Injury. Nutrients 2019;11(1):114 (PMID 30626086, PMC6357197, 초록 확인)", pmc("PMC6357197"), "Nutrients (PubMed Central)", ACC),
 (32, "Protective effects of the pyrolyzates derived from bamboo against neuronal damage and hematoaggregation. J Ethnopharmacol 2010;128(3):594-9 (PMID 20117201, 초록 확인)", pm("20117201"), "Journal of Ethnopharmacology (PubMed)", ACC),
 (33, "Phyllostachys nigra (Lodd. ex Lindl.) derived polysaccharide with enhanced glycolipid metabolism regulation and mice gut microbiome. Int J Biol Macromol 2024;257:128588 (PMID 38048922, 초록 확인)", pm("38048922"), "International Journal of Biological Macromolecules (PubMed)", ACC),
 (34, "Phyllostachys nigra Munro var. henonis alleviates inflammatory chemokine expression and DNCB-induced atopic-like dermatitis in BALB/c mice. J Ethnopharmacol 2023;318:116953 (PMID 37506780, 초록 확인)", pm("37506780"), "Journal of Ethnopharmacology (PubMed)", ACC),
]
sources = [dict(n=n, title=t, url=u, publisher=p, accessed=a) for n, t, u, p, a in S]

sec = {}
sec["overview"] = ("한눈에 보기",
"솜대(Phyllostachys nigra var. henonis)는 벼과(Poaceae) 왕대속의 대나무로, 줄기 안쪽 층은 한국과 중국에서 약재(죽여, Bambusae Caulis in Taeniam)로 써 왔다[29]. 식약처 「식품원료 목록」에는 솜대(학명 'Phyllostachys nigra Munro var. henonis Stapf', 다른 이름 대나무·분죽·담죽)와 오죽(학명 'Phyllostachys nigra (Lodd. ex Lindl.) Munro', 다른 이름 검정대·흑죽·분죽)이 따로 올라 있다[1, 2].\n\n"
"식품원료로서 솜대순·솜대잎은 '사용가능부위 : 순, 잎' 조건의 사용가능 원료이고, 솜대줄기는 사용불가다[1]. 오죽잎·오죽죽순은 '사용가능부위 : 죽순, 잎' 조건의 사용가능 원료이고, 오죽줄기는 사용불가다[2]. 죽력은 학명이 솜대와 왕대(Phyllostachys bambusoides)로 함께 적힌 제한적사용 원료로, 조건은 '제한적사용가능부위 : 마디줄기를 태울 때 유출되는 즙액※(죽력), 주류의 원료로만 사용'이다[3].\n\n"
"성분 연구는 잎의 플라보노이드 C-배당체(이소오리엔틴·오리엔틴·이소비텍신 등)와 클로로겐산에 모여 있다[7, 8]. 효과 보고는 대부분 세포·동물·시험관 실험이고, 이 종의 잎이나 죽순을 사람에게 먹여 효과를 본 임상시험은 확인하지 못했다[7, 8, 13].")

sec["history"] = ("역사와 쓰임",
"중국에서 이 종(논문 약칭 PN)의 잎은 한나라 때 『명의별록』에 처음 나오며 '담죽엽(Dan Zhu Ye)'으로 기록되었다고 한다[7]. 같은 논문은 중국에서 약으로 쓰는 세 가지 대나무 잎이 서로 비슷해 쓰임에서 혼동되기 쉽다고 적었다[7]. 줄기의 겉껍질을 벗긴 안쪽 층(죽여)은 한국과 중국에서 열·설사·가슴의 염증을 다스리는 데 써 왔다고 보고되었다[29]. 마디줄기를 가열해 얻는 즙(죽력, Bambusae Caulis in Liquamen)은 동아시아에서 기침과 천식에 쓰던 전통 약재로 소개된다[16].\n\n"
"일본에서 솜대는 오래전에 중국에서 들여온 외래종이며, 9세기 기록을 근거로 개화 주기가 약 120년으로 추정된다[5]. 일본에서는 주로 1908년(1903–1912년 사이 일부)에 꽃이 피었고, 다음 대규모 개화는 2028년 무렵으로 예상된다[5]. 2020년대에 일본에서 솜대 개화가 관찰되었고, 연구진은 이를 120년 만의 첫 기록으로 추정했다[6]. 한국에서 솜대를 재배·이용해 온 역사를 다룬 공공기관 자료는 확인하지 못했다.")

sec["biology"] = ("생물학적 특징",
"일본 자료에서 솜대의 줄기(稈)는 지름 6–10 cm, 높이 약 15 m에 이른다[5]. 옆으로 길게 뻗는 땅속줄기(leptomorph rhizome)로 무성번식해 줄기가 빽빽한 큰 군락(클론)을 이루며, 새 줄기는 5월에 땅속줄기에서 올라와 8월까지 빠르게 자란다[5]. 꽃은 일본에서 5–6월에 피고, 작은이삭마다 2–3개의 낱꽃이 있어 약 4 mm의 씨앗으로 자랄 수 있으며, 보통 크기의 줄기는 대개 15–20년 산다[5].\n\n"
"솜대는 한 번 꽃피고 죽는 일회결실성 대나무다[5]. 히로시마현의 한 군락에서 3년 동안 줄기 334개 중 83%가 꽃을 피웠지만 씨앗은 하나도 맺히지 않았고, 2022년 10월까지 꽃이 핀 줄기와 피지 않은 줄기가 모두 죽었다[5]. 2020년대 개화 군락에서는 균류의 자좌가 꽃눈 끝의 흔적 낱꽃에서 생기고 씨방에는 침입하지 않는 것이 관찰되었다[6].\n\n"
"오죽(검은 대나무)의 검은 줄기 색소는 표피와 피층에 쌓이는 멜라닌으로 확인되었고, 낮은 온도에서 세로토닌 등 인돌 화합물이 늘었다[22]. 다른 연구는 어린 줄기가 녹색이고 성숙하면 자흑색이 되며, 색소가 표피 아래 1–4층 세포에만 쌓이고 페투니딘 3-O-글루코사이드가 최대 9.36배 늘었다고 보고했다[23].")

sec["related_species"] = ("근연종과 혼동",
"같은 속의 다른 식품원료로 왕대(Phyllostachys bambusoides)는 왕대죽순·왕대잎·왕대수액이 '사용가능부위 : 죽순(줄기 제외), 잎, 수액' 조건의 사용가능 원료이고, 왕대줄기는 사용불가다[4]. 죽순대(Phyllostachys pubescens)는 '사용가능부위 : 죽순, 잎, 수액', 마디대(Phyllostachys bambusoides var. aurea)의 마디대순은 '사용가능부위 : 순' 조건이다[4]. 이 밖에 학명을 Bambusoidae(대나무아과)로만 적은 대나무죽순·건조죽순 등이 '사용가능부위 : 새순(죽순), 잎, 수액' 조건으로 올라 있다[4].\n\n"
"죽력 행은 솜대와 왕대를 함께 적었고, 다른 이름에도 '솜대, 왕대'가 들어 있어 두 종을 구분하지 않는다[3]. 약재 죽여도 솜대 또는 왕대의 줄기에서 얻는다고 적은 연구가 있다[30]. 그래서 죽력·죽여를 쓴 연구 결과는 솜대만의 자료로 단정하기 어렵다[3, 30].\n\n"
"중국에서는 이 종의 잎과 다른 두 가지 대나무 잎 약재의 모양이 비슷해 혼용되며, 세 잎은 성분 구성이 달랐다[7]. 조릿대속의 얼룩조릿대(Sasa veitchii) 잎 추출물은 COX-2를 선택적으로 억제한 반면 이 종의 잎 추출물은 NF-κB 유도 유전자 발현을 강하게 억제해, 작용 방식이 다르다고 보고되었다[13]. 같은 대나무류의 조릿대(Sasa borealis)는 '침출차에 한함' 조건의 제한적사용 원료로 따로 올라 있다[4].")

sec["cultivation"] = ("재배와 분포",
"일본에서 솜대는 3대 우점 대나무 가운데 하나로 전국에 널리 퍼져 있으며, 먹는 죽순과 공예 재료가 되는 줄기를 얻으려고 심어 왔다[5]. 일본의 대나무 숲 면적은 약 17만 ha로, 솜대를 포함한 세 종이 주를 이룬다[5]. 옆으로 길게 뻗는 땅속줄기로 빠르게 퍼져 숲과 농경지로 번지는 일이 일본에서 토지 관리 문제로 지적된다[5]. 개화 뒤 군락이 죽으면 회복이 느릴 것으로 보여, 비료 주기나 개화하지 않은 군락에서 옮겨 심기가 대책으로 제안되었다[5].\n\n"
"국내에서는 한 연구진이 솜대 잎을 5–6월 두 달에 걸쳐 따서 동결건조해 성분을 분석했다[20]. P. nigra 잎의 총 플라보노이드를 같은 밭에서 매달 따서 잰 결과 건물 기준 0.67–1.71%였고, 6월에 가장 낮고 7월에 가장 높았다[11]. 국내 솜대·오죽의 재배 면적과 죽순 생산량 통계는 농식품부 특용작물 생산실적과 통계청 농작물생산조사 로컬 자료에서 확인하지 못했다.")

sec["processing"] = ("가공과 제품",
"죽력은 솜대(P. nigra var. henosis로 표기)를 태울 때 응축된 증류물로 설명되며, 이 액에서 2,6-디메톡시페놀·카테콜(1,2-디하이드록시벤젠)·레조르시놀(1,3-디하이드록시벤젠)·프탈산류 화합물이 분리되었다[14]. 다른 연구는 죽력을 '열처리한 신선한 대나무 줄기에서 뽑은 액'으로 적었다[16]. 국내 담양군에서 산 시판 죽력을 분석한 연구는 LC-MS/MS로 벤조산이 23.14 mg/g으로 가장 많았고 총폴리페놀 274.13 mg GAE/g이라고 보고했지만, 원료 대나무의 종은 본문에서 확인하지 못했다[15]. 식품원료 목록에서 죽력은 주류의 원료로만 쓸 수 있다[3].\n\n"
"잎은 중국 시장에서 산 건조 약재를 가루(65 mesh)로 내어 메탄올로 초음파 추출해 분석한 예가 있다[7]. 검은 대나무(P. nigra) 잎의 가압 용매 추출에서는 50% 에탄올·200 °C(정치 25분)에서 총페놀 회수와 항산화 활성이 가장 좋았다[12]. 약재 죽여는 줄기 겉껍질을 벗기고 녹색 중간층을 끈 모양으로 그늘에 말려 만든다고 한다[30]. 다만 식품원료 목록에서 솜대줄기·오죽줄기는 사용불가다[1, 2]. Phyllostachys nigra·왕대·죽순대 세 대나무의 열분해물은 배양 신경세포의 NMDA 유도 세포 사멸을 줄였고, P. nigra 열분해물은 항플라스민 작용을 보였다(세포·시험관)[32]. P. nigra(Lodd. ex Lindl.) 뿌리에서 얻은 자일란 계열 다당류(PNS2A)는 당뇨 생쥐의 혈당·콜레스테롤을 낮췄지만, 뿌리는 목록의 사용 가능 부위가 아니다[1, 2, 33].")

sec["genetics"] = ("유전과 분자 연구",
"이 종의 PstI 유전체 라이브러리로 만든 탐침으로 왕대속 대나무 유전자원을 RFLP 분석한 결과, 핵 DNA 변이는 풍부해 종 특이적 양상을 얻었지만 엽록체 DNA 변이는 적었다[24]. 솜대 현탁 배양세포는 퍼트레신의 하이드록시신남산 아마이드를 주된 2차 대사산물로 쌓으며, 외래 화합물 생산 숙주로 연구되었다[25]. 같은 세포에서 옥신(2,4-D)과 사이토키닌(BA) 처리에 따른 증식·목질화 관련 전사체 변화도 분석되었다[26]. 솜대(Hachiku)의 2차 세포벽 NAC 전사인자(PnSWN)는 C-말단 영역 덕분에 전사 활성화 능력이 높았다[27].\n\n"
"오죽 줄기의 검은색과 관련해 전사인자 PnMYB4a가 쿠마린 생합성을 조절하고, 쿠마린이 멜라닌화의 전구물질로 작용한다는 결과가 나왔다[21]. 낮은 온도에서는 PnWRKY19-3이 세로토닌 생합성을 높여 멜라닌 형성에 관여할 가능성이 제시되었다[22]. 안토시아닌 쪽에서는 PnMYB6이 수크로스 축적과 함께 생합성 유전자 발현을 높인다고 제안되었다[23]. 일본 솜대는 씨앗을 맺지 못하는데, 연구진은 유전 다양성이 매우 낮아 자가불화합성이 원인일 수 있다는 가설을 냈지만 직접 증거는 아직 없다[5]. 이 종의 유전체 크기·염색체 수는 확인하지 못했다.")

sec["safety"] = ("안전성과 사용 조건",
"식약처 「식품원료 목록」에서 솜대와 오죽은 순(죽순)과 잎만 쓸 수 있고, 줄기는 사용불가다[1, 2]. 죽력은 제한적사용 원료로 '마디줄기를 태울 때 유출되는 즙액※(죽력), 주류의 원료로만 사용' 조건이 붙어 있어, 주류가 아닌 식품에는 쓸 수 없다[3]. 이 종에 대한 식약처 등 공공기관의 알레르기·잔류·독성 정보는 확인하지 못했다.\n\n"
"대나무 죽순 전반에 대해서는 날 죽순에 시안 배당체인 탁시필린이 들어 있어 이를 없애는 가공이 필요하다는 총설이 있다[28]. 다만 이 총설은 대나무 죽순 전반을 다룬 것이고, 솜대·오죽 죽순의 탁시필린 함량은 확인하지 못했다.\n\n"
"솜대 잎 추출물은 시험관에서 항산화 작용과 함께, 구리 이온이 있을 때 지질 과산화를 돕는 약한 산화촉진 작용도 보였다[10]. 시판 죽력 농축액은 사람 간세포(HepG2)에서 30 μg/mL까지 세포독성을 보이지 않았다[15]. 죽력·죽여·잎 추출물의 항염·피부염 완화 결과는 세포와 생쥐 실험이며(죽력은 피부에 바른 실험), 사람에게서 확인된 효과가 아니다[16, 17, 29, 34].")

sections = [dict(key=k, title=v[0], body=v[1]) for k, v in sec.items()]

compounds = [
 dict(name="Chlorogenic acid", name_ko="클로로겐산", class_="페놀산", role="marker", part="잎", content_text="이 종 잎의 클로로겐산이 다른 두 대나무 잎 약재의 약 4배(개별 수치는 원문 표, 전문 텍스트에서 확인 못함)[7]; 솜대 잎 추출물의 성분으로 보고[10]", activity_ko="잎 추출물 항산화 활성과 상관(시험관)[7]; 솜대 줄기 추출 분획(PN3)의 주요 폴리페놀로 HepG2 세포 산화 스트레스 완화(세포)[31]", source=[7, 10, 31]),
 dict(name="Isoorientin", name_ko="이소오리엔틴(루테올린 6-C-글루코사이드)", class_="플라보노이드 C-배당체", role="marker", part="잎", content_text="세 대나무 잎 가운데 이 종 잎에서 함량이 가장 높음(개별 수치 확인 못함)[7]; 잎 에틸아세테이트 분획에서 분리[8]", activity_ko="DPPH 라디칼 소거 IC50 0.81 µM(시험관)[7]", source=[7, 8]),
 dict(name="Orientin", name_ko="오리엔틴(루테올린 8-C-글루코사이드)", class_="플라보노이드 C-배당체", role="bioactive", part="잎", content_text="잎에서 분리·정량[7, 8]", activity_ko="DPPH IC50 0.84 µM(시험관)[7]; 토끼 흉부대동맥 고리 이완 IC50 2.28 µM(내피 있음, 적출 조직)[18]; 쥐 허혈/재관류 심근 세포자멸 감소(동물, 정맥 주사)[19]", source=[7, 8, 18, 19]),
 dict(name="Isovitexin", name_ko="이소비텍신(아피제닌 6-C-글루코사이드)", class_="플라보노이드 C-배당체", role="bioactive", part="잎", content_text="세 대나무 잎 가운데 이 종 잎에서 함량이 가장 높음(개별 수치 확인 못함)[7]", activity_ko="", source=[7]),
 dict(name="Vitexin", name_ko="비텍신", class_="플라보노이드 C-배당체", role="bioactive", part="잎", content_text="잎 에틸아세테이트 분획에서 분리[8]", activity_ko="", source=[8]),
 dict(name="Luteolin 6-C-(6''-O-trans-caffeoylglucoside)", name_ko="루테올린 6-C-(6''-O-트랜스-카페오일글루코사이드)", class_="아실화 플라보노이드 C-배당체", role="bioactive", part="잎", content_text="잎에서 분리[8, 9]", activity_ko="쥐 수정체 알도스 환원효소·최종당화산물 생성 억제(시험관)[9]; 망막 신경절세포(RGC-5) 산화 손상 완화(세포)[8]", source=[8, 9]),
 dict(name="Tricin", name_ko="트리신", class_="플라본", role="bioactive", part="잎", content_text="잎 에틸아세테이트 분획에서 분리[8]", activity_ko="", source=[8]),
 dict(name="p-Coumaric acid", name_ko="p-쿠마르산", class_="하이드록시신남산", role="bioactive", part="잎·줄기", content_text="잎에서 분리[8]; 줄기 추출 분획(PN3)의 구성 성분[31]", activity_ko="", source=[8, 31]),
 dict(name="Caffeic acid", name_ko="카페산", class_="하이드록시신남산", role="bioactive", part="잎·줄기", content_text="솜대 잎 추출물의 성분[10]; 줄기 추출 분획(PN3)의 구성 성분[31]", activity_ko="", source=[10, 31]),
 dict(name="Cynaroside", name_ko="루테올린 7-O-글루코사이드(시나로사이드)", class_="플라보노이드 O-배당체", role="bioactive", part="잎", content_text="솜대 잎 추출물의 성분[10]; 세 대나무 잎 HPLC 동시 정량 대상 7성분 중 하나[7]", activity_ko="DPPH IC50 0.43 µM(시험관)[7]", source=[7, 10]),
 dict(name="2,6-Dimethoxyphenol", name_ko="2,6-디메톡시페놀(시린골)", class_="페놀(열분해 산물)", role="bioactive", part="죽력(마디줄기를 태울 때 나오는 즙액)", content_text="죽력에서 활성 유도 분리[14]", activity_ko="", source=[14]),
 dict(name="Catechol", name_ko="카테콜(1,2-디하이드록시벤젠)", class_="페놀(열분해 산물)", role="bioactive", part="죽력", content_text="죽력에서 분리[14]", activity_ko="DPPH 라디칼 소거, 대식세포 NO 생성 억제, 티로시나아제·멜라닌 생성 억제(시험관·세포)[14]", source=[14]),
 dict(name="Resorcinol", name_ko="레조르시놀(1,3-디하이드록시벤젠)", class_="페놀(열분해 산물)", role="bioactive", part="죽력", content_text="죽력에서 분리[14]", activity_ko="DPPH 라디칼 소거, 대식세포 NO 생성 억제, 티로시나아제·멜라닌 생성 억제(시험관·세포)[14]", source=[14]),
 dict(name="Petunidin 3-O-glucoside", name_ko="페투니딘 3-O-글루코사이드", class_="안토시아닌", role="bioactive", part="줄기 표피 아래 세포층(오죽)", content_text="줄기 착색 과정에서 최대 9.36배 증가(말비딘 헥소사이드는 13.23배)[23]", activity_ko="오죽 줄기 자흑색의 주된 색소 대사물[23]", source=[23]),
 dict(name="Serotonin", name_ko="세로토닌", class_="인돌 아민", role="bioactive", part="줄기(오죽)", content_text="저온 생육에서 유의하게 증가(비표적 대사체 분석)[22]", activity_ko="줄기 멜라닌 형성과 관련된 인돌 전구물질로 제안[22]", source=[22]),
]
for c in compounds:
    c["class"] = c.pop("class_")
compounds = [{k: c[k] for k in ("name","name_ko","class","role","part","content_text","activity_ko","source")} for c in compounds]

cond = {"instrument": "Agilent 1260 Infinity 펌프(4원), 1260 Infinity II UV 검출기", "column": "Diamonsil Plus C18(4.6 × 250 mm, 5 µm)", "mobile_phase": "A: 0.1% 포름산 수용액(pH 2.8), B: 아세토니트릴", "gradient": "0–2분 10% B; 2–30분 10→30% B; 30–45분 30→70% B; 55–60분 70→10% B", "flow": "1.0 mL/min", "temp": "30 °C", "detection": "UV 350 nm", "injection": "10 µL", "sample_prep": "건조 잎 가루(65 mesh) 1.0 g을 메탄올 25 mL로 30분 초음파 추출, 원심분리 후 0.22 µm 막 여과", "standard": "7개 표준품(순도 98% 이상)을 메탄올(일부 DMSO 선용해)에 녹인 원액을 50% 메탄올로 희석, 7개 농도 검량선", "linearity": "상관계수 > 0.9996(7개 농도)", "lod": "0.11–1.04 µg/mL(원문 값 그대로)", "loq": "0.06–0.35 µg/mL(원문 값 그대로)", "recovery": "92.90–122.32%"}
assays = [
 dict(role="literature", compound="Chlorogenic acid", compound_ko="클로로겐산(이소오리엔틴·오리엔틴·이소비텍신·시나로사이드·루테올린·아피제닌과 동시 정량)", part="잎(중국 시장 구입 건조 약재, 26개 시료 중 이 종 포함)", content="이 종 잎의 클로로겐산이 다른 두 대나무 잎의 약 4배; 개별 함량은 원문 표에 있어 전문 텍스트에서 확인 못함[7]", method="HPLC-UV", conditions=dict(cond), rationale="세 가지 대나무 잎 약재를 구별하는 품질관리용 동시 정량법으로, 이 종 잎은 클로로겐산이 특히 많아 구별 지표가 된다[7]. 방법 검증(직선성·검출한계·회수율)은 다른 종(PA) 시료로 했다[7]", source=[7], url=pmc("PMC7024249"), source_kind="paper"),
 dict(role="literature", compound="Isoorientin", compound_ko="이소오리엔틴", part="잎(중국 시장 구입 건조 약재)", content="세 대나무 잎 가운데 이 종 잎에서 가장 높음; 개별 함량은 전문 텍스트에서 확인 못함[7]", method="HPLC-UV", conditions=dict(cond), rationale="이 종 잎에서 가장 많은 플라보노이드 C-배당체로 보고되고, 잎 추출물에서 분리된 주요 성분이다[7, 8]. 조건은 클로로겐산과 같은 동시 정량법이다[7]", source=[7, 8], url=pmc("PMC7024249"), source_kind="paper"),
]

d = dict(slug="phyllostachys-nigra", name_ko="솜대", name_en="Henon bamboo (var. henonis) / black bamboo (P. nigra)",
         scientific_name="Phyllostachys nigra (Lodd. ex Lindl.) Munro",
         aliases=["오죽", "분죽", "담죽", "검정대", "흑죽", "Phyllostachys nigra var. henonis"],
         sections=sections, compounds=compounds, markers=[], assays=assays, nutrients=[], production=[], world=[], gi=[], orgs=[], sources=sources)
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in sections: print(s["key"], len(s["body"]))
