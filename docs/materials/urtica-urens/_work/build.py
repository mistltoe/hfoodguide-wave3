import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
PM = "https://pubmed.ncbi.nlm.nih.gov/{}/"
PMC = "https://pmc.ncbi.nlm.nih.gov/articles/{}/"
A = "2026-11-02"
S = [
 ("식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — '서양잎'(학명란 'Urtica urens / Cuscuta japonica var. thyroidea Engelm. / Cuscuta japonica var. thyroidea Kom.', 이명 '쐐기풀', 영명 Annual nettle, 제한적사용, '제한적사용가능부위 : 잎') 행과 같은 속 스팅잉네틀(Urtica dioica L.)·가는잎쐐기풀·카바니아쐐기풀·쐐기풀(Urtica thunbergiana) 행, 새삼(Cuscuta japonica Choisy) 행 (로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json)", "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "식품의약품안전처", "2026-10-13"),
 ("EFSA FEEDAP Panel. Safety and efficacy of a feed additive consisting of a tincture derived from the leaves of Urtica urens L. (dwarf nettle tincture) for use in all animal species. EFSA Journal 2026;24(10):e10345 (PMID 42840537, doi:10.2903/j.efsa.2026.10345) — 전문 확인", PMC.format("PMC13639844"), "European Food Safety Authority (EFSA Journal, PMC)", A),
 ("The genome sequence of the small nettle, Urtica urens L. (Urticaceae). Wellcome Open Research 2024;9:639 (PMID 39629216, doi:10.12688/wellcomeopenres.23187.1) — 전문 확인", PMC.format("PMC11612553"), "Wellcome Open Research (PMC)", A),
 ("Antioxidant and Tyrosinase Inhibitory Potential of Urtica urens: a source for skin whitening agents. Journal of Pharmacopuncture 2026;29(2):185-193 (PMID 42368509, doi:10.3831/KPI.2026.29.2.185) — 전문 확인", PMC.format("PMC13303475"), "Journal of Pharmacopuncture (PMC)", A),
 ("Anti-Inflammatory Effect of Urtica urens on LPS-Challenged Keratinocytes. Journal of Pharmacopuncture 2025;28(4):311-320 (PMID 41477277, doi:10.3831/KPI.2025.28.4.311) — 초록", PM.format("41477277"), "Journal of Pharmacopuncture (PubMed)", A),
 ("Comprehensive study of Algerian nettles: Phenolic content and multifunctional activities of Urtica pilulifera and Urtica urens. Animal Models and Experimental Medicine 2025 (PMID 41220369, doi:10.1002/ame2.70084) — 전문 확인", PMC.format("PMC12660493"), "Animal Models and Experimental Medicine (PMC)", A),
 ("Phytochemical characterization, nutritional profile and biological activities of Urtica urens L. plant organs. Scientific Reports 2026 (PMID 42331956, doi:10.1038/s41598-026-58771-w) — 초록", PM.format("42331956"), "Scientific Reports (PubMed)", A),
 ("Phytochemical Characterization ... and In Vivo Assessment of the Antioxidant and Anti-Arthritic Activities of Urtica urens L. Ethanolic Extract. Plants 2026;15(19):3018 (PMID 42884882, doi:10.3390/plants15193018) — 전문 일부 확인", PMC.format("PMC13666801"), "Plants (MDPI, PMC)", A),
 ("Therapeutic potential of Urtica urens L. extract: phytochemical characterization and evaluation of antioxidant and antiproliferative properties. Natural Product Research 2026 (PMID 42157773, doi:10.1080/14786419.2026.2675473) — 초록", PM.format("42157773"), "Natural Product Research (PubMed)", A),
 ("Urtica spp.: Phenolic composition, safety, antioxidant and anti-inflammatory activities. Food Research International 2017 (PMID 28784509, doi:10.1016/j.foodres.2017.06.008) — 초록", PM.format("28784509"), "Food Research International (PubMed)", A),
 ("Phytochemical, phylogenetic, and anti-inflammatory evaluation of 43 Urtica accessions (stinging nettle) based on UPLC-Q-TOF-MS metabolomic profiles. Phytochemistry 2013;96:170-83 (PMID 24169378, doi:10.1016/j.phytochem.2013.09.016) — 초록", PM.format("24169378"), "Phytochemistry (PubMed)", A),
 ("Evaluation of antinociceptive, antinflammatory activities and phytochemical analysis of aerial parts of Urtica urens L. Phytotherapy Research 2010 (PMID 20564509, doi:10.1002/ptr.3188) — 초록", PM.format("20564509"), "Phytotherapy Research (PubMed)", A),
 ("Antioxidant and antimicrobial activities of ethanol and aqueous extracts from Urtica urens. Pharmaceutical Biology 2017 (PMID 28084125, doi:10.1080/13880209.2016.1275025) — 전문 확인", PMC.format("PMC6130501"), "Pharmaceutical Biology (PMC)", A),
 ("Chemical composition, phytochemical constituents, antioxidant and anti-inflammatory activities of Urtica urens L. leaves. Archives of Physiology and Biochemistry 2017;123(2):93-104 (PMID 27960552, doi:10.1080/13813455.2016.1255899) — 초록", PM.format("27960552"), "Archives of Physiology and Biochemistry (PubMed)", A),
 ("Nutritional quality of some wild leafy vegetables in South Africa. International Journal of Food Sciences and Nutrition 2009;60(5):424-31 (PMID 19037794, doi:10.1080/09637480701777928) — 초록", PM.format("19037794"), "International Journal of Food Sciences and Nutrition (PubMed)", A),
 ("Nutritional and antioxidant properties of wild edible plants and their use as potential ingredients in the modern diet. International Journal of Food Sciences and Nutrition 2013;64(8):944-52 (PMID 23944868, doi:10.3109/09637486.2013.821695) — 초록", PM.format("23944868"), "International Journal of Food Sciences and Nutrition (PubMed)", A),
 ("Polyphenolic and biological activities of leaves extracts of Argemone subfusiformis (Papaveraceae) and Urtica urens (Urticaceae). Revista de Biología Tropical 2010;58(4):1517-31 (PMID 21247003, doi:10.15517/rbt.v58i4.5428) — 초록", PM.format("21247003"), "Revista de Biología Tropical (PubMed)", A),
 ("Antioxidant evaluation for Urtica urens, Rumex cyprius and Borago officinalis edible wild plants in Palestine. Pakistan Journal of Pharmaceutical Sciences 2016 (PMID 27005499) — 초록", PM.format("27005499"), "Pakistan Journal of Pharmaceutical Sciences (PubMed)", A),
 ("Immunoreactive leukotrienes in nettle plants (Urtica urens). International Archives of Allergy and Applied Immunology 1990;91(1):43-6 (PMID 2155878, doi:10.1159/000235087) — 초록", PM.format("2155878"), "International Archives of Allergy and Applied Immunology (PubMed)", A),
 ("Misuse of a herb: stinging nettle (Urtica urens) induced severe tongue oedema. Complementary Therapies in Medicine 2004;12(1):57-8 (PMID 15130574, doi:10.1016/j.ctim.2003.12.001) — 제목·서지만 확인(초록 없음)", PM.format("15130574"), "Complementary Therapies in Medicine (PubMed)", A),
 ("Drug interaction potential of the seed extract of Urtica urens L. (dwarf nettle). Phytotherapy Research 2009;23(12):1763-70 (PMID 19441062, doi:10.1002/ptr.2848) — 초록", PM.format("19441062"), "Phytotherapy Research (PubMed)", A),
 ("In vivo effects of Urtica urens (dwarf nettle) on the expression of CYP1A in control and 3-methylcholanthrene-exposed rats. Xenobiotica 2008 (PMID 18098063, doi:10.1080/00498250701713968) — 초록", PM.format("18098063"), "Xenobiotica (PubMed)", A),
 ("Growth, reproduction and defence in nettles: responses to herbivory modified by competition and fertilization. Oecologia 1995;104(4):487-495 (PMID 28307664, doi:10.1007/BF00341346) — 초록", PM.format("28307664"), "Oecologia (PubMed)", A),
 ("An ethnobotanical study of medicinal plants used by the local people of Alaşehir (Manisa) in Turkey. Journal of Ethnopharmacology 2013;150(3):860-74 (PMID 24126062, doi:10.1016/j.jep.2013.09.040) — 초록", PM.format("24126062"), "Journal of Ethnopharmacology (PubMed)", A),
 ("Individualized homeopathic medicines and Urtica urens mother tincture in treatment of hyperuricemia: an open, randomized, pragmatic, pilot trial. Journal of Complementary and Integrative Medicine 2020;18(3):599-608 (PMID 33079705, doi:10.1515/jcim-2020-0129) — 초록", PM.format("33079705"), "Journal of Complementary and Integrative Medicine (PubMed)", A),
 ("Effects of Urtica urens in the Feed of Broilers on Performances, Digestibility, Carcass Characteristics and Blood Parameters. Animals 2023;13(13):2092 (PMID 37443890, doi:10.3390/ani13132092) — 초록", PM.format("37443890"), "Animals (MDPI, PubMed)", A),
 ("Evaluation of anxiolytic activity of methanolic extract of Urtica urens in a mice model. Behavioral and Brain Functions 2015;11:19 (PMID 25902868, doi:10.1186/s12993-015-0063-y) — 초록", PM.format("25902868"), "Behavioral and Brain Functions (PubMed)", A),
 ("Comparison between the effect of ethanolic extract of Urtica urens L. and bisphosphonate in the treatment of induced osteoporosis in rats. Biomedicine & Pharmacotherapy 2025;187:118112 (PMID 40339227, doi:10.1016/j.biopha.2025.118112) — 초록", PM.format("40339227"), "Biomedicine & Pharmacotherapy (PubMed)", A),
 ("Protective effect of ethanolic extract of Urtica urens L. against the toxicity of imidacloprid on bone remodeling in rats and antioxidant activities. Biomedicine & Pharmacotherapy 2017 (PMID 28531918, doi:10.1016/j.biopha.2017.05.023) — 초록", PM.format("28531918"), "Biomedicine & Pharmacotherapy (PubMed)", A),
 ("Effects of the antirheumatic remedy hox alpha — a new stinging nettle leaf extract — on matrix metalloproteinases in human chondrocytes in vitro. Histology and Histopathology 2002;17(2):477-85 (PMID 11962753, doi:10.14670/HH-17.477) — 초록", PM.format("11962753"), "Histology and Histopathology (PubMed)", A),
 ("Streptomyces urticae sp. nov., isolated from rhizosphere soil of Urtica urens L. Antonie van Leeuwenhoek 2018 (PMID 29582193, doi:10.1007/s10482-018-1072-2) — 초록", PM.format("29582193"), "Antonie van Leeuwenhoek (PubMed)", A),
 ("Insecticides and arable weeds: effects on germination and seedling growth. Ecotoxicology 2005 (PMID 16385742, doi:10.1007/s10646-004-1353-6) — 초록", PM.format("16385742"), "Ecotoxicology (PubMed)", A),
 ("Conservation biological control in strawberry: effect of different pollen on development, survival, and reproduction of Neoseiulus californicus. Experimental and Applied Acarology 2015 (PMID 26459375, doi:10.1007/s10493-015-9971-7) — 초록", PM.format("26459375"), "Experimental and Applied Acarology (PubMed)", A),
]
sources = [{"n": i+1, "title": t, "url": u, "publisher": p, "accessed": a} for i,(t,u,p,a) in enumerate(S)]

sec = {}
sec["overview"] = ("한눈에 보기",
"이 소재는 쐐기풀과(Urticaceae) 쐐기풀속의 한해살이풀 Urtica urens L.로, 영어로는 dwarf nettle·small nettle·annual nettle 등으로 불린다[1][2][3]. 식품의약품안전처 「식품원료 목록」에는 대표 원료명 '서양잎', 이명 '쐐기풀', 영명 'Annual nettle'로 한 행만 올라 있고, 앱의 국문명 '서양'은 이 원료명에서 부위명 '잎'을 뺀 것이다[1]. '서양쐐기풀' 같은 완전한 국문 정명이 따로 있는지는 국가표준식물목록 등 국내 원자료로 확인하지 못함.\n\n"
"식품원료로서의 지위는 '제한적사용'이고 사용 조건은 '제한적사용가능부위 : 잎'이어서, 잎만 식품에 제한적으로 쓸 수 있다[1]. 제한적 사용 원료에 적용되는 식품공전의 구체적인 사용량·사용 방법 기준은 원문으로 확인하지 못함. 같은 목록의 학명란에는 Urtica urens와 함께 새삼의 변종 학명(Cuscuta japonica var. thyroidea)이 나란히 적혀 있는데, 새삼(Cuscuta japonica Choisy)은 씨앗만 제한적으로 쓰는 별도 원료로 따로 올라 있어 이 병기는 목록 자료의 오기로 보인다[1].\n\n"
"잎 추출물에서는 클로로겐산이 주된 폴리페놀로 정량되었고[4][5], 유럽식품안전청(EFSA)이 평가한 잎 팅크(사료용 향미 첨가물)는 p-쿠마르산을 표지 성분으로 규격화했다[2]. 잎과 줄기의 쐐기털에는 히스타민·류코트리엔 같은 자극 물질이 들어 있어 맨손으로 만지면 따끔거림과 두드러기를 일으킨다[3][19].")
sec["history"] = ("역사와 전통 이용",
"남아메리카 민간의학에서는 지상부를 이뇨·정화·당뇨·류머티즘 등에 써 왔고, 영양가가 있다고 여겨 여러 음식에도 넣어 먹는다고 소개된다[4]. 튀니지에서는 여러 용도의 약초로 널리 쓰인다고 하며[13], 튀르키예 알라셰히르 지역 민족식물학 조사에서는 이 지역에서 가장 흔히 쓰이는 약용식물 가운데 하나로 꼽혔다[24]. 팔레스타인·지중해 지역과 남아프리카에서도 야생 식용 채소로 먹는 식물로 연구되었다[15][16][17][18].\n\n"
"영국에서는 유럽 본토에서 오래전에 들어온 귀화식물(고귀화식물)로 보며, 다른 쐐기풀처럼 어린잎을 익혀 나물로 먹을 수 있다[3]. 유럽에서는 쐐기풀 잎(Urticae folium)의 기원 식물로 Urtica dioica와 함께 이 종이 유럽약전과 유럽의약품청(EMA) 단행본에 올라 있으나, EMA 평가 보고서는 '충분히 확립된 약리적 사용'은 인정하지 않았다[2]. EMA 단행본 원문은 이번 조사에서 직접 확인하지 못함.\n\n"
"동종요법에서는 이 식물의 모팅크(mother tincture)가 쓰이며, 인도에서 고요산혈증 환자 90명을 대상으로 한 공개 무작위 예비시험이 있었으나 연구진은 확정적 결론을 내리지 못했다고 밝혔다[25]. 쐐기털의 따끔거림을 일으키는 물질에 대한 연구는 1990년 류코트리엔 분석 등으로 이어져 왔다[19].")
sec["biology"] = ("식물학적 특징",
"Urtica urens는 키가 대개 60 cm 이하인 작은 한해살이풀로, 한 그루에 암꽃과 수꽃이 함께 피는 자웅동주이며 암꽃 쪽으로 치우친 성비를 보인다[3]. EFSA는 키를 약 0.5 m로, 씨앗으로만 번식한다고 정리했다[2]. 잎은 큰쐐기풀(U. dioica)보다 절반 정도로 작고 더 둥글며 톱니가 거칠고 깊다[3].\n\n"
"줄기와 잎 표면의 쐐기털은 개미산 등 통증을 일으키는 물질로 채워진 큰 세포이고, 피부에 닿으면 끝이 부러지며 내용물을 주입해 접촉성 두드러기를 일으킨다[3]. 쐐기털과 전초 추출물에서는 높은 수준의 류코트리엔 B4·C4와 히스타민이 검출되었다[19]. 핀란드 연구에서는 잎을 잘라 내는 모의 섭식 피해 뒤 쐐기털 밀도를 늘리는 방어 반응이 여러해살이인 U. dioica보다 이 한해살이 종에서 약했다[23].\n\n"
"원산지는 유라시아 온대와 북아프리카이며 지금은 여섯 대륙 모두에 귀화해 있다[2][3]. 밭·텃밭·도시 공터처럼 자주 교란되는 곳, 특히 모래질 경작지처럼 건조한 곳을 좋아한다[3]. 중국 랴오닝성 안산에서 채집한 이 종의 뿌리 주변 흙에서 새로운 방선균 종이 분리되기도 했다[31]. 꽃가루는 딸기밭 주변 잡초 식생에서 포식성 응애의 먹이원으로 시험되었다[33].")
sec["related_species"] = ("근연종과 혼동 주의",
"가장 혼동하기 쉬운 종은 큰쐐기풀(스팅잉네틀, Urtica dioica)이다[2][3]. U. dioica는 암수딴그루의 여러해살이풀로 땅속줄기로 퍼지고 키가 1–2 m에 이르는 반면, U. urens는 자웅동주의 한해살이풀로 씨앗으로만 번식한다[2].\n\n"
"식품원료 목록에서도 두 종은 따로 다뤄진다[1]. 스팅잉네틀은 잎·잎추출물·잎분말이 '제한적사용', 뿌리와 주스는 '사용불가'이고, 국내 자생 쐐기풀(Urtica thunbergiana)과 그 분말·추출물·주스는 '사용불가'다[1]. 이 원료의 목록 이명이 '쐐기풀'이어서 사용불가 원료인 쐐기풀(U. thunbergiana)과 이름만으로 섞이기 쉬우므로 학명으로 구분해야 한다[1]. 가는잎쐐기풀(U. angustifolia)·카바니아쐐기풀(U. cannabina)과 Urtica breweri, Urtica gracilis 등 다른 쐐기풀속 원료도 각각 별도 행으로 올라 있다[1].\n\n"
"43개 쐐기풀속 계통을 비교한 연구에서 U. urens는 계통적으로 멀지만 대사체 조성은 유럽 U. dioica 무리와 비슷한 군집에 묶였다[11]. 반면 유럽 연구는 U. urens에서 4-카페오일-5-p-쿠마로일퀸산을 처음 확인했고, 항염 효과는 U. dioica보다 강하게 나왔다고 보고했다[10]. 유럽 약용 자료의 성분 수치 대부분은 U. dioica 잎에서 나온 것이어서, EFSA도 U. urens의 조성은 '비슷할 것으로 추정'한다고만 적었다[2]. 시판 쐐기풀 잎 추출물 가운데에는 두 종을 섞은 원료도 있으므로 연구 결과를 볼 때 기원 종을 확인해야 한다[30].")
sec["cultivation"] = ("자생과 재배",
"이 종은 경작지·텃밭·폐기물 처리장 같은 교란지에 흔한 잡초성 한해살이풀이다[3]. 북유럽 경작지 잡초 감소 원인을 살핀 연구에서는 살충제 두 가지를 함께 처리했을 때 이 종의 유묘 생장이 줄었다[32]. 경쟁 밀도와 비료 수준을 달리한 실험에서는 낮은 밀도·높은 시비 조건에서 섭식 피해에 따른 키 생장 감소가 덜했다[23].\n\n"
"연구용 시료는 대부분 야생 개체를 채집해 썼다[4][6][13]. 아르헨티나 연구는 11월에 지상부를 채집했고[4], 알제리 연구는 1월과 3월(개화기)에 잎을 채집했으며[6][8], 튀니지 연구는 12월에 지상부를 채집했다[13]. 한겨울에 채집한 시료는 페놀 함량이 낮게 나올 수 있다고 연구진은 해석했다[6].\n\n"
"국내 재배 면적·생산량 통계와 국내 자생 여부는 이번 조사에서 확인하지 못함. 상업 재배 체계나 품종에 관한 공식 자료도 확인하지 못함.")
sec["processing"] = ("가공·이용과 효능 연구",
"식품으로는 다른 쐐기풀처럼 어린잎을 익혀 나물로 먹으며, 익히면 쐐기털의 자극이 사라지는 것으로 알려져 있다[3]. 국내 식품원료 목록에서 쓸 수 있는 부위는 잎뿐이다[1].\n\n"
"EFSA가 평가한 '왜성쐐기풀 팅크'는 말린 잎을 물·에탄올 혼합 용매로 실온에서 장시간 우려낸 뒤 압착해 고형분과 액체를 나누고 여과해 만든다[2]. 이 팅크는 건조물 0.50–0.80%(w/w), p-쿠마르산 0.9–1.8 mg/L로 규격화되었고, 5배치 분석에서 건조물 평균 0.65%, 용매 99.35%였다[2]. 유럽연합 사료첨가물 등록부에는 기존 첨가물로 올라 있으나, EFSA는 향을 내는 효과를 입증한 자료가 없어 효능은 결론 내리지 못했다[2].\n\n"
"가축 사료 연구에서는 말린 잎을 육계 사료에 1%·2% 섞어 먹였고, 1% 군에서 체중 증가가 더 컸다[26]. 국내 건강기능식품 생산실적에서 이 원료 품목은 확인하지 못함.\n\n"
"효능 연구는 대부분 세포·동물 실험이다[8][14][27][28][29]. 잎 에탄올 추출물은 쥐의 카라기난 발부종을 줄였고[14], 보조제 유발 관절염 쥐에서 300 mg/kg 투여 시 발·관절 부종이 줄었다[8]. 메탄올 추출물은 생쥐 불안 행동 시험에서 항불안 효과를 보였고[27], 에탄올 추출물은 난소 절제 쥐의 골다공증 모델과 살충제(이미다클로프리드) 독성 모델에서 보호 효과를 보였다[28][29]. 사람에게서 이런 효과가 확인된 임상시험은 이번 조사에서 확인하지 못함.")
sec["genetics"] = ("유전체",
"2024년 영국 다윈 생명의 나무(Darwin Tree of Life) 사업은 큐 왕립식물원에서 채집한 개체로 이 종의 첫 염색체 수준 유전체를 공개했고, 이는 쐐기풀과 전체에서도 처음이다[3]. 조립 길이는 339.60 Mb, 스캐폴드 N50은 24.8 Mb이며 서열의 95.89%가 12개 염색체에 배정되었다[3]. 유세포 분석으로 추정한 1C 값은 0.51 pg(약 500 Mb)였다[3].\n\n"
"미토콘드리아 유전체는 335.02 kb, 엽록체 유전체는 147.51 kb로 조립되었다[3]. Ensembl 주석에서 단백질 암호화 유전자 18,378개와 비암호화 유전자 6,146개가 확인되었고, BUSCO 완전성은 91.1%였다[3]. 조립체 번호는 GCA_958296335.1이다[3].\n\n"
"영국 개체는 지금까지 모두 2n = 24의 이배체로 보고되어, 대개 사배체인 큰쐐기풀과 구별된다[3]. 43개 쐐기풀속 계통의 분자 계통에서는 U. dioica가 측계통·다계통으로 나타났고 U. urens는 그와 멀리 떨어진 계통으로 놓였다[11].")
sec["safety"] = ("안전성",
"국내에서는 잎만 '제한적사용' 원료로 쓸 수 있고, 뿌리·씨앗 등 다른 부위는 이 원료의 사용 가능 부위에 들어 있지 않다[1]. 날잎과 줄기의 쐐기털은 개미산·히스타민·류코트리엔 등을 피부에 주입해 따가움과 두드러기를 일으키므로 손질할 때 장갑을 쓰는 것이 좋다[3][19]. 이 종의 잎을 잘못 사용한 뒤 심한 혀 부종이 생긴 사례 보고가 있다[20]. 다만 초록이 없어 섭취 경위와 용량은 확인하지 못함.\n\n"
"EFSA는 잎 팅크를 사료에 말 600 mg/kg, 그 밖의 동물 50 mg/kg까지 넣는 것은 안전하고 소비자·환경에도 문제가 없다고 보았지만, 작업자에게는 피부·눈 자극성과 피부·호흡기 감작성이 있는 것으로 간주했다[2]. 같은 의견서는 EFSA 식물 성분 목록이 이 종의 잎에서 항영양소인 피트산(4730 mmol/kg 건조물)을 우려 성분으로 적었다고 전한다[2]. 남아프리카 연구는 이 종을 포함한 야생 채소의 피트산·알칼로이드·사포닌 수준이 비교적 낮다고 보고했다[15].\n\n"
"쥐에 씨앗 추출물을 복강 주사한 실험에서는 여러 간 약물대사효소(CYP2C6·CYP2E1·CYP3A1 등) 발현과 활성이 바뀌어, 함께 먹는 약의 대사에 영향을 줄 가능성이 제기되었다[21][22]. 이는 씨앗 추출물의 동물 실험으로, 잎을 먹는 사람에게 같은 효과가 있는지는 확인하지 못함. 유럽 연구에서는 지상부 추출물이 생리활성 농도(200·350 μg/mL)에서 대식세포와 간세포에 독성을 보이지 않았다[10]. 임신·수유부, 소아 섭취에 관한 공공기관의 안전 정보는 확인하지 못함. 국내 식품 알레르기·잔류 농약 관련 공공기관 정보도 확인하지 못함.")

order = ["overview","history","biology","related_species","cultivation","processing","genetics","safety"]
sections = [{"key": k, "title": sec[k][0], "body": sec[k][1]} for k in order]

def C(name, ko, cls, role, part, content, act, src):
    return {"name": name, "name_ko": ko, "class": cls, "role": role, "part": part, "content_text": content, "activity_ko": act, "source": src}
compounds = [
 C("Chlorogenic acid", "클로로겐산(5-O-카페오일퀸산)", "히드록시신남산 유도체(카페오일퀸산)", "marker", "지상부·잎",
   "지상부 80% 에탄올 추출물 3.31 mg/100 mg 추출물(HPLC)[4]; 지상부 에탄올 추출물의 주성분 670 mg/1000 g 건조중량[12]",
   "추출물의 주된 폴리페놀; 버섯 티로시나아제 억제·자외선 유도 지질 과산화 억제(시험관)[4]; 진통·항염 활성의 일부를 설명하는 성분으로 추정(동물 실험)[12]", [4,5,12]),
 C("p-Coumaric acid", "p-쿠마르산", "히드록시신남산", "marker", "잎(물·에탄올 팅크)",
   "잎 팅크 5배치 평균 1.28 μg/mL(1.10–1.47 μg/mL); 규격 0.9–1.8 mg/L[2]",
   "EFSA 평가 사료용 팅크의 표지 성분(HPLC-DAD 정량)[2]", [2]),
 C("4-Caffeoyl-5-p-coumaroylquinic acid", "4-카페오일-5-p-쿠마로일퀸산", "히드록시신남산 유도체", "bioactive", "지상부",
   "함량 확인하지 못함(HPLC-PDA-ESI/MS로 이 종에서 처음 확인)[10]",
   "U. urens에서 처음 보고된 성분[10]", [10]),
 C("Polyphenols", "총폴리페놀", "페놀성 화합물(총량)", "bioactive", "잎·지상부",
   "잎 물 추출물 47.83 mg GAE/g DW[7]; 잎 70% 에탄올 추출물 31.41 mg GAE/g[13]; 잎 에탄올 추출물 16.86 mg GAE/g DW[8]; 지상부 80% 에탄올 추출물 4.18 mg GAE/100 mg 추출물[4]; 잎 물 추출물 19.20 mg GAE/g 생체중[6]; 잎 팅크 72 μg/mL(69–77, 갈산 당량)[2]",
   "DPPH·ABTS 등 시험관 항산화 활성[7][8][13]", [2,4,6,7,8,13]),
 C("Flavonoids", "총플라보노이드", "플라보노이드(총량)", "bioactive", "잎·지상부",
   "잎 물 추출물 10.30 mg RE/g DW[7]; 잎 70% 에탄올 추출물 6.81 mg 퀘르세틴/g[13]; 잎 에탄올 추출물 2.46 mg RE/g[8]; 지상부 80% 에탄올 추출물 1.87 mg QE/100 mg 추출물[4]; 잎 물 추출물 18.3 mg QE/g 생체중[6]",
   "시험관 항산화 활성에 기여하는 성분군으로 추정[6][13]", [4,6,7,8,13]),
 C("Rutin", "루틴", "플라보놀 배당체", "bioactive", "잎(에틸아세테이트 추출물)",
   "함량 확인하지 못함(LC-MS/MS 성분 목록에 포함)[9]",
   "에틸아세테이트 추출물의 페놀 성분 가운데 하나[9]", [9]),
 C("Histamine", "히스타민", "생체 아민", "bioactive", "쐐기털·전초",
   "쐐기털과 전초 추출물에서 검출(수치는 초록에 없음)[19]",
   "쐐기털에 찔렸을 때 가려움·두드러기를 일으키는 매개 물질[19]", [19]),
 C("Leukotriene B4", "류코트리엔 B4", "에이코사노이드", "bioactive", "쐐기털·전초",
   "RIA·역상 HPLC로 높은 수준 검출(수치는 초록에 없음)[19]",
   "시험관에서 호중구 주화성 활성 확인; 쐐기털 자극 기전에 관여[19]", [19]),
 C("Leukotriene C4", "류코트리엔 C4", "에이코사노이드", "bioactive", "쐐기털·전초",
   "RIA로 높은 수준 검출(수치는 초록에 없음)[19]",
   "쐐기털 자극 매개 물질의 하나[19]", [19]),
 C("Formic acid", "개미산(포름산)", "유기산", "bioactive", "쐐기털",
   "함량 확인하지 못함[3]",
   "쐐기털 속 통증 유발 물질의 하나로 소개[3]", [3]),
 C("Calcium", "칼슘", "무기질", "nutrient", "잎",
   "잎 물 추출물 23354.44 ppm(꽃·줄기보다 높음)[7]; 남아프리카 야생 채소 4종 중 최고 농도[15]; 지중해 야생 식용식물 13종 중 칼슘 함량이 높은 종[16]",
   "야생 채소로서의 무기질 공급원[15][16]", [7,15,16]),
 C("Ascorbic acid", "비타민 C(아스코르브산)", "수용성 비타민", "nutrient", "잎",
   "에탄올 추출물 238 mg/100 g, 물 추출물 160.55 mg/100 g(원문 표 제목은 '잎의 수준', 추출물 기준인지 잎 기준인지 원문이 모호함)[13]",
   "영양 성분[13]", [13]),
 C("Phytic acid", "피트산", "항영양소(이노시톨 인산)", "bioactive", "잎",
   "4730 mmol/kg 건조물(EFSA 식물 성분 목록 인용값)[2]; 남아프리카 야생 채소 비교에서 비교적 낮은 수준[15]",
   "무기질 흡수를 방해할 수 있는 항영양소로 EFSA 목록에 우려 성분으로 기재[2]", [2,15]),
]

assays = [
 {"role": "literature", "compound": "Chlorogenic acid", "compound_ko": "클로로겐산",
  "part": "지상부(2007년 11월 아르헨티나 부에노스아이레스 채집), 80% 에탄올 추출물",
  "content": "3.31 mg/100 mg 추출물(머무름 시간 10.5분)[4]",
  "method": "HPLC-DAD(UV 335 nm), 외부표준법",
  "conditions": {"instrument": "Varian 9000, 다이오드 배열 검출기", "column": "C18(Gemini 5 μm, 150 × 4.6 mm)",
   "mobile_phase": "A: 물/아세트산(98:2, v/v), B: 메탄올/아세트산(98:2, v/v)",
   "gradient": "15% B → 40% B(30분), 40% B → 75% B(10분), 75% B → 85% B(5분)",
   "flow": "1.2 mL/min", "temp": "", "detection": "335 nm", "injection": "Rheodyne 주입기, 20 μL 루프",
   "sample_prep": "건조 분쇄 지상부 20 g을 80% 에탄올로 실온에서 24시간씩 4회 냉침, 합쳐 농축·동결건조(수율 16.2%)",
   "standard": "클로로겐산 표준품(시판 시약, 외부표준법)", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "추출물의 주된 폴리페놀이어서 총폴리페놀·총플라보노이드와 함께 추출물 표준화 지표로 쓰였다[4]. 전문 확인함: 직선성·검출한계·정량한계·회수율은 본문에 없어 비워 둠.",
  "source": [4], "url": PMC.format("PMC13303475"), "source_kind": "paper"},
 {"role": "literature", "compound": "p-Coumaric acid", "compound_ko": "p-쿠마르산",
  "part": "잎 물·에탄올 팅크(사료용 향미 첨가물)",
  "content": "5배치 평균 1.28 μg/mL(1.10–1.47 μg/mL), 규격 0.9–1.8 mg/L[2]",
  "method": "HPLC-DAD(유럽연합 참조실험실 권고법)",
  "conditions": {"instrument": "", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "다이오드 배열 검출", "injection": "", "sample_prep": "", "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "신청자가 표지 성분으로 정했고, 유럽연합 참조실험실(EURL)이 총폴리페놀 분광법·HPTLC 지문과 함께 이 성분의 HPLC-DAD 정량을 공식 관리 방법으로 권고했다[2]. EFSA 의견서 전문을 확인했으나 칼럼·이동상 등 세부 조건은 의견서에 없어 비워 둠.",
  "source": [2], "url": PMC.format("PMC13639844"), "source_kind": "paper"},
]

d = {"slug": "urtica-urens", "name_ko": "서양", "name_en": "Annual nettle (dwarf nettle, small nettle)",
     "scientific_name": "Urtica urens L.",
     "aliases": ["서양잎", "쐐기풀(식품원료 목록 이명)", "Annual nettle", "Dwarf nettle", "Small nettle", "Burning nettle"],
     "sections": sections, "compounds": compounds, "markers": [], "assays": assays, "nutrients": [],
     "production": [], "world": [], "gi": [], "orgs": [], "sources": sources}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in sections: print(s["key"], len(s["body"]))
