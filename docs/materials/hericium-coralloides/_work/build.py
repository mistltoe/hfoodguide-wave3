import json
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "dossier.json"
A = "2026-11-02"


def pm(pmid, title, journal, year, pmc=None):
    t = f"{title} ({journal}, {year}; PMID {pmid}" + (f"; {pmc} 전문)" if pmc else "; 초록)")
    return {"title": t, "url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/", "publisher": f"{journal} (PubMed)", "accessed": A}


S = [
    {"title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 산호침버섯(Hericium coralloides (Scop.) Pers. / Hericium ramosum (Bull.) Letell), 산호침버섯아재비(Hericium laciniatum Banker), 노루궁뎅이버섯(Hericium erinaceus) 항목",
     "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
    pm("41295165", "Domestication Cultivation and Nutritional Analysis of Hericium coralloides", "Journal of Fungi", 2025, "PMC12653868"),
    pm("37686830", "Hericium coralloides Ameliorates Alzheimer's Disease Pathologies and Cognitive Disorders by Activating Nrf2 Signaling and Regulating Gut Microbiota", "Nutrients", 2023, "PMC10489620"),
    pm("39452656", "Chromosome-Scale Genome and Transcriptomic Analyses Reveal Differential Regulation of Terpenoid Secondary Metabolites in Hericium coralloides", "Journal of Fungi", 2024, "PMC11508549"),
    pm("35141329", "Genome Sequencing of Hericium coralloides by a Combination of PacBio RS II and Next-Generation Sequencing Platforms", "International Journal of Genomics", 2022),
    pm("33473835", "The complete mitochondrial genome of Hericium coralloides (Hericiaceae, Basidiomycota)", "Mitochondrial DNA Part B", 2017, "PMC7800198"),
    pm("39719598", "Yield increment and transcriptome response caused by blue light treatment in Hericium coralloides", "BMC Genomics", 2024, "PMC11668087"),
    pm("41683239", "Dietary Use of Hericium coralloides for NAFLD Prevention (review)", "Nutrients", 2026, "PMC12899011"),
    pm("40649339", "Polysorbate 80 Differentially Impacts Erinacine Production Profiles in Submerged Cultures of Hericium", "Molecules", 2025, "PMC12251483"),
    pm("27588730", "Corallocins A-C, Nerve Growth and Brain-Derived Neurotrophic Factor Inducing Metabolites from the Mushroom Hericium coralloides", "Journal of Natural Products", 2016),
    pm("33246107", "Neurotrophic isoindolinones from the fruiting bodies of Hericium erinaceus", "Bioorganic & Medicinal Chemistry Letters", 2020),
    pm("39019356", "Structural characterization of Hericium coralloides polysaccharide and its neuroprotective function in Alzheimer's disease", "International Journal of Biological Macromolecules", 2024),
    pm("41679818", "Structural characterization and hypoglycemic mechanisms of a Hericium coralloides heteropolysaccharide (HCP-2b) via gut microbiota modulation and PI3K/Akt signaling", "Carbohydrate Polymers", 2026),
    pm("41251781", "Structure Characterization and Anti-Aging Activities of a Polysaccharide Derived from Hericium coralloides Using the Three-Phase Partitioning Method", "International Journal of Medicinal Mushrooms", 2026),
    pm("38368701", "Effects of different extraction methods on the structural and biological properties of Hericium coralloides polysaccharides", "Food Chemistry", 2024),
    pm("42235777", "Targeting 2-hydroxyglutarate mediates the antidepressant effects of Hericium coralloides polysaccharide in hyperlipidemia-associated depression", "International Journal of Biological Macromolecules", 2026),
    pm("41135149", "Identification of new selenium compounds produced by edible mushrooms", "Food Chemistry", 2025),
    pm("5111996", "Molecular structure of starch-type polysaccharides from Hericium ramosum and Hericium coralloides", "Science", 1971),
    pm("22367940", "Purification and characterization of a novel laccase from the edible mushroom Hericium coralloides", "Journal of Microbiology", 2012),
    pm("26672458", "Characterization and cloning of laccase gene from Hericium coralloides NBRC 7716 suitable for production of epitheaflagallin 3-O-gallate", "Enzyme and Microbial Technology", 2015),
    pm("15939270", "Comparative study of mycelial growth and basidiomata formation in seven different species of the edible mushroom genus Hericium", "Bioresource Technology", 2005),
    pm("29773898", "New antioxidants from the culture broth of Hericium coralloides", "The Journal of Antibiotics", 2018),
    pm("8202563", "Fatty acids and other compounds with nematicidal activity from cultures of Basidiomycetes", "Planta Medica", 1994),
    pm("31679228", "Antioxidant and Anti-Aging Activities of Ethyl Acetate Extract of the Coral Tooth Mushroom, Hericium coralloides", "International Journal of Medicinal Mushrooms", 2019),
    pm("33822496", "Effect of Cytokinin-Containing Extracts from Some Medicinal Mushroom Mycelia on HepG2 Cells In Vitro", "International Journal of Medicinal Mushrooms", 2021),
    pm("36325705", "Antiproliferative activities of extracts from mycelial biomass of some medicinal Basidiomycetes in human colon cancer cells Colo 205", "Experimental Oncology", 2022),
    pm("37432355", "Medicinal Mushroom Extracts from Hericium coralloides and Trametes versicolor Exert Differential Immunomodulatory Effects on Immune Cells from Older Adults", "Nutrients", 2023),
    pm("25954959", "Effects of Comb Tooth Cap Medicinal Mushroom, Hericium ramosum, Mycelia on DPPH Radical Scavenging Activity and Nerve Growth Factor Synthesis", "International Journal of Medicinal Mushrooms", 2015),
    pm("9918390", "Erinacine E as a kappa opioid receptor agonist and its new analogs from a basidiomycete, Hericium ramosum", "The Journal of Antibiotics", 1998),
    pm("24801292", "Radionuclides in some edible and medicinal macrofungal species from Tara Mountain, Serbia", "Environmental Science and Pollution Research", 2014),
    pm("41724293", "Multiscale interaction of Hericium coralloides polysaccharide with maize starch: Impact on structural properties and digestibility", "International Journal of Biological Macromolecules", 2026),
    pm("25376797", "Application of micro-computed tomography to microstructure studies of the medicinal fungus Hericium coralloides", "Mycologia", 2014),
]
for i, s in enumerate(S, 1):
    s["n"] = i
SOURCES = [{"n": s["n"], "title": s["title"], "url": s["url"], "publisher": s["publisher"], "accessed": s["accessed"]} for s in S]

sections = [
 {"key": "overview", "title": "한눈에 보기", "body":
  "산호침버섯(Hericium coralloides)은 죽거나 썩은 활엽수 줄기에서 자라는 흰색 담자균 버섯으로, 가늘게 갈라진 산호 모양 가지에 짧은 침(가시)이 촘촘히 달린다[2, 8]. "
  "식품의약품안전처 「식품원료 목록」에는 원료명 '산호침버섯', 학명 Hericium coralloides (Scop.) Pers. / Hericium ramosum (Bull.) Letell, 별칭 '수실노루궁뎅이'로 올라 있고, 상태는 '사용가능', 사용 조건은 '사용가능부위 : 자실체'이다[1]. "
  "따라서 일반 식품의 원료로 쓸 수 있는 부위는 자실체(버섯 몸체)이며, 균사체는 이 원료의 사용 가능 부위로 적혀 있지 않다[1]. "
  "건강기능식품 고시형 원료의 원재료 목록에는 없어 고시된 지표성분과 기준은 확인하지 못함.\n\n"
  "같은 속의 노루궁뎅이버섯(H. erinaceus)은 목록에서 별도 원료로 다뤄지고 연구도 훨씬 많으므로, 이 문서는 학명이 H. coralloides(또는 이명 H. ramosum)로 밝혀진 자료만 쓴다[1, 8]. "
  "연구는 자실체 다당체의 구조와 동물·세포 실험, 신경영양인자 유도 물질 '코랄로신(corallocin)', 유전체 해독, 재배 조건에 모여 있다[4, 7, 10, 12]. "
  "효능 연구는 대부분 세포·동물 수준이며, 사람을 대상으로 한 임상시험은 2026년 종설에서도 찾지 못했다고 보고되었다[8]."},
 {"key": "history", "title": "이름의 역사", "body":
  "종소명 coralloides는 '산호를 닮은'이라는 뜻으로, 영어권에서는 coral tooth(산호이빨버섯) 또는 comb tooth로 불린다[8, 24, 28]. "
  "식약처 목록은 Hericium ramosum (Bull.) Letell.을 같은 원료의 학명으로 함께 적고 있으며, 일본 연구에서는 H. ramosum이라는 이름으로 균사체 연구가 보고되었다[1, 28]. "
  "1971년 Science 논문은 H. ramosum과 H. coralloides를 나란히 다루어, 당시에는 두 이름이 따로 쓰였음을 보여 준다[18]. "
  "세르비아 연구는 Hericium clathroides라는 이름으로 이 무리의 버섯을 보고했으나, 이 이름이 H. coralloides의 이명인지는 공식 분류 DB에서 확인하지 못함[30].\n\n"
  "국내 목록의 별칭 '수실노루궁뎅이'는 노루궁뎅이버섯과 닮았으나 술(수실)처럼 갈라진 모양을 가리키는 이름으로 보이나, 명명 유래를 적은 공식 자료는 확인하지 못함. "
  "러시아에서는 자연 상태에서 드물어져 46개 행정구역의 적색목록(Red Data Book)에 올라 있다고 2026년 종설이 적었다[8]. "
  "같은 종설은 이 종을 다룬 첫 논문이 1983년에 나왔다고 정리했다[8]."},
 {"key": "biology", "title": "균학적 특징", "body":
  "산호침버섯은 무당버섯목(Russulales) 산호침버섯과(Hericiaceae)에 속하는 목재부후균으로, 리그노셀룰로스를 영양원으로 쓴다[2, 4]. "
  "중국에서는 동북·서북·서남 지역 활엽수 줄기나 썩은 나무에서 자라며, 티베트 보미현에서 채집한 야생 균주(SH001)는 ITS 서열이 기존 H. coralloides 서열과 98.93% 일치했다[2]. "
  "이 야생 자실체는 흰색이고 굵은 대에서 산호 모양 가지가 갈라지며, 너비 10 cm·높이 5 cm 크기였다[2]. "
  "균사는 15 ℃에서 자라지 않았고 30 ℃에서 하루 8.40 mm로 가장 빨리 자랐으며, 탄소원은 과당, 질소원은 효모추출물에서 가장 잘 자랐다[2].\n\n"
  "청색광(430–470 nm) 아래에서 자란 자실체는 우윳빛이 돌고 지름 150–230 mm로 커졌으며 가지당 침이 90–110개였고, 적색광에서는 누렇고 작아졌다[7]. "
  "자실체의 침 표면에서 포자가 만들어지며, 마이크로 CT·현미경 영상으로 조직 투자량과 포자 생산 효율을 추정하려는 연구가 이어졌다[32]. "
  "자실체에서는 분자량 65 kDa의 락케이스(산화효소)가 정제되었고, 일본 균주 NBRC 7716은 67.2 kDa의 다른 분비형 락케이스를 만든다[19, 20]. "
  "배양 균사는 선충을 쫓고 죽이는 지방산 혼합물(리놀레산·올레산·팔미트산이 주성분)을 만든다[23]. "
  "1971년 연구는 이 버섯의 녹말형 다당이 포도당 32–45개짜리 짧은 아밀로스 사슬로만 이뤄져 식물 녹말과 다르다고 보고했다[18]."},
 {"key": "related_species", "title": "가까운 종과 혼동", "body":
  "식약처 「식품원료 목록」에서 같은 속의 노루궁뎅이버섯(Hericium erinacium / H. erinaceus)은 자실체·균사체 원료(균사체추출물·균사체발효추출물 등)로 따로 올라 있고, 산호침버섯아재비(Hericium laciniatum Banker)는 '사용불가'이다[1]. "
  "따라서 산호침버섯과 이름이 비슷한 두 종의 자료는 이 문서에 섞지 않으며, 특히 산호침버섯아재비는 식품원료로 쓸 수 없다[1]. "
  "ITS 서열 비교에서 북미의 H. americanum과 H. coralloides는 H. erinaceus와 가까운 종으로 묶인다[9].\n\n"
  "자료가 섞이기 쉬운 사례가 실제로 있다[11, 31]. "
  "신경영양 물질 코랄로신 A는 산호침버섯에서 처음 분리되었지만 노루궁뎅이버섯 자실체에서도 분리되어, 이 성분만으로 종을 가를 수는 없다[10, 11]. "
  "2026년 한 논문은 제목에 H. coralloides 다당체를 내세우면서 초록에서는 '산호 모양 H. erinaceus 다당체'라고 적어, 이 문서는 그 수치를 산호침버섯 값으로 쓰지 않는다[31]. "
  "또한 7종 비교 재배 연구는 H. erinaceus와 H. erinaceum을 다른 계통으로 구분해 다뤘다[21]. "
  "노루궁뎅이버섯 균사체의 에리나신 연구 결과를 산호침버섯 자실체 효능으로 옮겨 적어서는 안 된다[9]."},
 {"key": "cultivation", "title": "재배와 생산", "body":
  "산호침버섯은 톱밥 봉지·병 재배로 인공 재배된다[2, 3, 7]. "
  "중국 지린농업대 균주(JLAU_857)는 톱밥 37%·목화씨 껍질 24%·밀기울 20%·옥수수가루 19% 등의 배지(수분 65%, pH 5.6)에서 25 ℃로 23–25일 균사를 키운 뒤, 10 ℃·습도 90%로 2일 두어 원기를 유도했다[7]. "
  "원기가 나온 뒤 8일이면 자실체가 다 자랐고, 하루 6시간 청색광을 비추면 평균 수량이 189.03 g으로 백색광(137.39 g)보다 37.58% 많았다[7]. "
  "티베트 야생 균주는 활엽수 톱밥 60%·목화씨 껍질 20%·밀기울 18% 배지에서 28일 만에 균사가 다 찼고, 1차 수확 자실체 생체중은 봉지당 평균 249.07 g이었다[2].\n\n"
  "2005년 7종 비교 연구에서 참나무 톱밥에 쌀겨 20%를 더한 배지로 H. coralloides·H. americanum·H. erinaceus 등을 재배했을 때 생물학적 효율은 종과 균주에 따라 26–70%였다[21]. "
  "같은 연구에서 H. coralloides 균사 생장에 가장 좋은 첨가물은 콩가루였다[21]. "
  "국내 생산량·재배 면적 통계(통계청·농림축산식품부 특용작물 생산실적)에서 산호침버섯 항목은 확인하지 못함. "
  "러시아 종설은 자연산이 드물므로 산업 이용에는 인공 배양 생물량을 써야 한다고 제안했다[8]."},
 {"key": "processing", "title": "가공과 이용", "body":
  "국내 식품원료로는 자실체만 쓸 수 있으므로, 말린 자실체나 그 가공품이 대상이다[1]. "
  "건조 분말 성분 분석에서 총당 33.40%, 조단백 16.00%, 회분 11.70%, 조지방 6.30%, 조섬유 4.60%, 총 트라이테르페노이드 3.32%가 보고되었다[3]. "
  "티베트 균주 자실체는 건물 100 g당 단백질 15.4 g, 식이섬유 34.7 g, 지방 3.5 g, 유리당 1.6 g, 나트륨 10.0 mg으로, 저당·저지방 식품 원료로 제안되었다[2]. "
  "단백질을 이루는 아미노산 가운데 글루탐산이 가장 많고 아스파르트산이 다음이어서 감칠맛에 기여한다[2].\n\n"
  "다당체는 열수 환류·산·알칼리·효소·초음파·냉수 등 아홉 가지 방법으로 추출했을 때 수율·단당 조성·분자량이 크게 달랐다[15]. "
  "아셀렌산염을 넣은 배지에서 키우면 흡수한 셀레늄의 98.5% 넘게 유기 형태로 바뀌었고, 셀레노메싸이오닌은 흡수 셀레늄의 15–18%였다[17]. "
  "일본 균주의 락케이스는 홍차의 미량 폴리페놀(에피테아플라갈린 3-O-갈레이트) 합성에 시판 효소보다 2배 효율을 보여 효소 원천으로도 연구된다[20]. "
  "해외 시판 보충제는 대부분 이 버섯의 균사체나 추출물을 쓴다고 종설이 적었으나, 국내에서 균사체는 이 원료의 사용 가능 부위가 아니다[1, 8]."},
 {"key": "genetics", "title": "유전체와 성분 생합성", "body":
  "2022년 PacBio RS II와 차세대 염기서열 분석으로 처음 해독된 핵 유전체(ASM367540v1)는 약 55.9 Mb, 콘티그 307개, 단백질 암호 유전자 11,736개였다[5]. "
  "2024년에는 중국 푸젠 균주 '77'의 단핵 균사로 HiFi·Hi-C 해독을 해 13개 염색체, 약 43.6–43.7 Mb, 콘티그 N50 3.6 Mb의 염색체 수준 유전체를 얻었다(BUSCO 완성도는 초록 96.9%, 본문 96.3%로 다르게 적힘)[4]. "
  "이 유전체에서 유전자 약 11,690개가 예측되었고, 반복서열은 전체의 16.52%였다[4]. "
  "13번 염색체에는 GGPP 합성효소·다이테르펜 고리화효소·사이토크롬 P450 3개 등 10개 유전자로 된 다이테르페노이드 생합성 유전자 무리가 예측되었다[4].\n\n"
  "테르페노이드 골격 생합성 유전자는 자실체보다 2핵 균사에서 더 많이 발현되어, 테르페노이드가 균사에 더 많을 것으로 추정되었다[4]. "
  "다만 이 연구의 '에리나신' 측정은 바이칼린 표준으로 210 nm 흡광을 잰 것이어서 에리나신 정량으로는 부정확하다는 비판이 있다[9]. "
  "미토콘드리아 유전체는 72,961 bp, GC 함량 17.96%로 단백질 유전자 14개와 tRNA 27개를 가졌다[6]. "
  "청색광·적색광 처리는 발현 유전자의 61.11–67.81%를 바꿔, 빛이 이 버섯의 거의 모든 생명 과정에 영향을 준다고 보고되었다[7]. "
  "H. ramosum이라는 이름의 균주 배양액에서는 κ-오피오이드 수용체에 작용하는 다이테르페노이드 에리나신 E가 분리되어, 이 무리도 사이아테인 다이테르페노이드를 만든다는 근거가 된다[29]."},
 {"key": "safety", "title": "안전성", "body":
  "식품의약품안전처 목록상 자실체는 식품원료로 '사용가능'이며, 별도의 섭취량 제한이나 주의 문구는 목록에 적혀 있지 않다[1]. "
  "산호침버섯에 대한 공공기관(식약처·농촌진흥청 등)의 알레르기·독성 안전성 정보는 확인하지 못함. "
  "건조 자실체 분석에서 측정한 중금속 6종(크롬·카드뮴·비소·납·수은 등)의 농도는 낮다고 보고되었으나, 원문 표의 수치는 확인하지 못함[3].\n\n"
  "생쥐에 자실체 분말 500 mg/kg을 7주 먹인 실험에서 심장·간·비장·신장의 무게 지수와 조직 소견에 이상이 없었으나, 이는 독성시험 기준에 따른 평가가 아니다[3]. "
  "세르비아 산지 조사에서는 H. clathroides라는 이름의 시료가 살이 많은 버섯 무리로서 방사성 핵종(세슘-137 등)을 상대적으로 많이 쌓은 종에 들었으므로, 오염 지역 야생 채취품에는 주의가 필요하다[30]. "
  "세포 실험에서 균사체 추출물의 대장암 세포 증식 억제(IC50 0.17 μg/mL)나 다당체의 간암·유방암 세포 억제가 보고되었으나, 모두 시험관 결과로 사람의 효능·안전성을 뜻하지 않는다[2, 26]. "
  "고령자 말초혈액 면역세포 실험에서 추출물은 바이러스 자극 시 인터페론을 줄이고 염증성 사이토카인을 늘려, 면역 반응에 미치는 영향이 한 방향이 아님이 관찰되었다[27]. "
  "고지혈증·우울 복합 모델 생쥐에서 다당체가 혈중 지질과 우울 유사 행동을 개선했다는 보고도 동물 실험 단계이다[16]."},
]

compounds = [
 {"name": "Corallocin A", "name_ko": "코랄로신 A", "class": "메로테르페노이드(벤조퓨라논)", "role": "bioactive", "part": "자실체(에틸아세테이트 추출물)",
  "content_text": "조추출물 7.88 g에서 2.8 mg 분리(분리 수량이며 함량이 아님)[8]", "activity_ko": "사람 성상세포(1321N1)에서 NGF·BDNF 발현 유도(세포 실험)[10]; 노루궁뎅이버섯 자실체에서도 분리됨[11]", "source": [8, 10, 11]},
 {"name": "Corallocin B", "name_ko": "코랄로신 B", "class": "아이소인돌리논", "role": "bioactive", "part": "자실체(에틸아세테이트 추출물)",
  "content_text": "조추출물 7.88 g에서 29.4 mg 분리(분리 수량)[8]", "activity_ko": "NGF·BDNF 발현 유도, HUVEC·MCF-7·KB-3-1 세포 증식 억제(세포 실험)[10]", "source": [8, 10]},
 {"name": "Corallocin C", "name_ko": "코랄로신 C", "class": "인돌-아이소인돌리논", "role": "bioactive", "part": "자실체(에틸아세테이트 추출물)",
  "content_text": "조추출물 7.88 g에서 3.4 mg 분리(분리 수량)[8]", "activity_ko": "NGF·BDNF 발현 유도(세포 실험)[10]", "source": [8, 10]},
 {"name": "Galactan", "name_ko": "갈락탄 다당체(HCP)", "class": "다당체", "role": "bioactive", "part": "자실체(열수 추출·정제)",
  "content_text": "주사슬 →6)-α-D-Galp-(1→, O-2 일부에 α-L-푸코스 곁사슬, 분자량 16.06 kDa; 함량 확인하지 못함[12]", "activity_ko": "APP/PS1 알츠하이머 모델 생쥐에서 인지 저하·아밀로이드 β 침착 완화(동물 실험)[12]", "source": [12]},
 {"name": "Heteropolysaccharide HCP-2b", "name_ko": "헤테로다당체 HCP-2b", "class": "다당체", "role": "bioactive", "part": "자실체",
  "content_text": "분자량 9.93 kDa, 갈락토스·포도당 잔기로 된 비결정성 다당; 함량 확인하지 못함[13]", "activity_ko": "α-글루코시데이스·α-아밀레이스 억제, 제브라피시 고혈당 개선(세포·동물 실험)[13]", "source": [13]},
 {"name": "beta-(1,6)-Glucan", "name_ko": "β-(1→6)-글루칸 헤테로다당체", "class": "다당체", "role": "bioactive", "part": "자실체(3상 분배 추출)",
  "content_text": "조추출물 대비 수율 58.4%; 단당 조성 만노스 6.6%·포도당 73.0%·갈락토스 20.4%, Mw 1.57 × 10^5 Da[14]", "activity_ko": "예쁜꼬마선충 평균 수명 16.36% 연장(500 μg/mL)[14]", "source": [14]},
 {"name": "Amylose", "name_ko": "짧은 사슬 아밀로스(녹말형 다당)", "class": "다당체", "role": "nutrient", "part": "자실체",
  "content_text": "포도당 32–45개 길이의 짧은 아밀로스 분자로만 구성(함량 확인하지 못함)[18]", "activity_ko": "식물 녹말과 구조가 다름[18]", "source": [18]},
 {"name": "Protein", "name_ko": "단백질", "class": "다량영양소", "role": "nutrient", "part": "자실체(건조)",
  "content_text": "15.4 g/100 g 건물(티베트 균주 SH001)[2]; 조단백 16.00%(재배 자실체 건조 분말)[3]", "activity_ko": "필수아미노산/총아미노산 비 0.32[2]", "source": [2, 3]},
 {"name": "Dietary fiber", "name_ko": "식이섬유", "class": "탄수화물", "role": "nutrient", "part": "자실체(건조)",
  "content_text": "34.7 g/100 g 건물(효소-중량법)[2]; 조섬유 4.60%(건조 분말)[3]", "activity_ko": "", "source": [2, 3]},
 {"name": "L-Glutamic acid", "name_ko": "글루탐산(감칠맛 아미노산)", "class": "아미노산", "role": "nutrient", "part": "자실체(건조, 산 가수분해)",
  "content_text": "검출 아미노산 15종 중 가장 많음; 감칠맛 아미노산 합계 2.56 g/100 g 건물, 시스테인·메싸이오닌·트립토판 불검출[2]", "activity_ko": "감칠맛 기여[2]", "source": [2]},
 {"name": "Triterpenoids", "name_ko": "총 트라이테르페노이드", "class": "테르페노이드", "role": "bioactive", "part": "자실체(건조 분말)",
  "content_text": "3.32%(UV 분광법); 총 플라보노이드 0.88%, 총 알칼로이드 0.57%, 총 스테롤 0.43%[3]", "activity_ko": "", "source": [3]},
 {"name": "Erinacine P", "name_ko": "에리나신 P(·A·C)", "class": "사이아테인 다이테르페노이드", "role": "bioactive", "part": "균사체(액체 배양, 북미 균주) — 식품원료 사용 부위 아님",
  "content_text": "북미 H. coralloides 균주 균사체에서 에리나신 A·C·P 검출(UPLC-ESI-MS/MS); 종별 정량값은 전문에서 종명이 빠져 확인하지 못함[9]", "activity_ko": "노루궁뎅이버섯에서 연구된 신경 관련 성분으로, 이 종 자실체에서의 함량은 확인하지 못함[9]", "source": [9]},
 {"name": "Selenomethionine", "name_ko": "셀레노메싸이오닌", "class": "유기 셀레늄", "role": "nutrient", "part": "자실체(셀레늄 첨가 재배)",
  "content_text": "흡수한 셀레늄의 15–18%(셀레늄 강화 재배 조건)[17]", "activity_ko": "셀레노네인 유도체 등 수용성 셀레늄 대사물이 함께 확인됨[17]", "source": [17]},
 {"name": "trans-Zeatin", "name_ko": "트랜스-제아틴(사이토키닌)", "class": "식물호르몬류(사이토키닌)", "role": "bioactive", "part": "균사체 생물량(시험관 배양)",
  "content_text": "조사한 7종 가운데 H. coralloides 균사에서 트랜스-제아틴이 가장 많은 축(수치 확인하지 못함)[26]", "activity_ko": "균사체 조추출물 IC50 0.17 μg/mL로 Colo 205 대장암 세포 증식 억제(세포 실험)[26]; HepG2 세포독성은 정제 분획에서만[25]", "source": [25, 26]},
 {"name": "Spirobenzofuran", "name_ko": "스파이로벤조퓨란 및 신규 항산화 물질", "class": "벤조퓨란 유도체", "role": "bioactive", "part": "배양액(균사 배양)",
  "content_text": "배양액에서 신규 화합물 3종과 함께 분리(함량 확인하지 못함)[22]", "activity_ko": "ABTS 라디칼 소거 IC50 29–66 μM[22]", "source": [22]},
]

assays = [
 {"role": "literature", "compound": "Free sugars (glucose, fructose, sucrose, maltose, lactose)", "compound_ko": "유리당(총당)",
  "part": "자실체(티베트 균주 SH001 재배품, 분쇄 후 80메시)", "content": "1.6 g/100 g 건물(유리 단당·이당만, 다당 제외)[2]",
  "method": "HPLC-ELSD(GB 5009.8-2016 제1법)",
  "conditions": {"instrument": "", "column": "당 분석용 아미노 칼럼 250 × 4.6 mm, 5 μm", "mobile_phase": "아세토나이트릴–물(70:30)", "gradient": "등용매",
                 "flow": "1.0 mL/min", "temp": "40 ℃", "detection": "ELSD(드리프트관 85 ℃, 질소 350 kPa)", "injection": "",
                 "sample_prep": "시료 5 g + 물 50 mL → 석유에터 탈지 → 아세트산아연·페로사이안화칼륨 각 5 mL 침전, 30분 교반 → 100 mL 정용 → 여과 후 0.45 μm 막 여과",
                 "standard": "포도당·과당·자당·맥아당·젖당(0–10 mg/mL) 검량선", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "버섯의 당 조성은 맛과 영양 표시의 기본 값이며, 이 방법은 산 가수분해를 하지 않아 다당체를 제외한 유리당만 잰다[2]. 검출·정량한계와 회수율은 원문에 없다[2].",
  "source": [2], "url": "https://pubmed.ncbi.nlm.nih.gov/41295165/", "source_kind": "paper"},
 {"role": "literature", "compound": "Amino acids (acid hydrolysate)", "compound_ko": "구성 아미노산",
  "part": "자실체(티베트 균주 SH001 재배품)", "content": "15종 검출, 글루탐산 > 아스파르트산; 감칠맛 아미노산 2.56 g/100 g 건물, 단맛 아미노산 2.81 g/100 g 건물[2]",
  "method": "자동 아미노산 분석기(이온교환 크로마토그래피·닌하이드린 후컬럼 유도체화)",
  "conditions": {"instrument": "자동 아미노산 분석기(기종 원문 미기재)", "column": "이온교환 칼럼", "mobile_phase": "", "gradient": "", "flow": "", "temp": "",
                 "detection": "닌하이드린 후컬럼 유도체화 피크 면적", "injection": "",
                 "sample_prep": "6 mol/L 염산, 110 ℃ 24시간 가수분해 → 정용 → 원심 → 여과", "standard": "표준 아미노산 용액 검량선",
                 "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "글루탐산·아스파르트산 같은 감칠맛 아미노산과 필수아미노산 비율은 버섯 단백질의 품질과 맛을 평가하는 지표다[2]. 산 가수분해 조건이라 시스테인·메싸이오닌·트립토판은 검출되지 않았다[2].",
  "source": [2], "url": "https://pubmed.ncbi.nlm.nih.gov/41295165/", "source_kind": "paper"},
 {"role": "literature", "compound": "Erinacines A, C, P", "compound_ko": "에리나신 A·C·P",
  "part": "균사체(PDB 진탕 배양 14일, 북미 균주) — 국내 식품원료 사용 부위(자실체)가 아님",
  "content": "북미 H. coralloides 균주 균사체에서 세 성분 모두 검출; 종별 정량값은 확인하지 못함[9]",
  "method": "UPLC-ESI-MS/MS(Orbitrap, 음이온 모드)",
  "conditions": {"instrument": "Vanquish Flex 이성분 UPLC + Q-Exactive Orbitrap 질량분석기", "column": "Kinetex XB-C18 100 Å, 100 mm × 4.6 mm, 2.6 μm",
                 "mobile_phase": "A: 물/폼산 99.9:0.1, B: 메탄올/아세토나이트릴/폼산 94.9:5:0.1",
                 "gradient": "0–8분 B 5→70%, 8–15분 70→100%, 15–20분 100%, 20–24분 100→5%, 24–28분 5%", "flow": "0.7 mL/min", "temp": "30 ℃",
                 "detection": "음이온 ESI, 폼산 부가이온 [M+HCOOH−H]− m/z 537.3(P)·477.3(A)·479.3(C); 분무 전압 3.6 kV", "injection": "2 μL",
                 "sample_prep": "동결 균사 분말 100 mg에 에틸아세테이트 5배 부피로 3회 추출 → 질소 건조 → 메탄올 200 μL(내부표준 지베렐린산 2 μM)에 재용해 → 0.45 μm PTFE 여과",
                 "standard": "에리나신 A(0.013–80 pmol), C·P(0.0196–80 pmol) 표준품", "linearity": "",
                 "lod": "최소 검출량 A 0.013 pmol, C·P 0.0196 pmol(폼산 부가이온 기준)", "loq": "", "recovery": ""},
  "rationale": "에리나신은 노루궁뎅이버섯 균사체의 대표 신경 관련 성분으로, 이 연구가 북미 산호침버섯 균주 균사에서 처음으로 질량분석 근거를 제시했다[9]. 자실체 함량이 아니므로 국내 식품원료(자실체) 품질 지표로 바로 쓸 수 없다[1, 9].",
  "source": [9], "url": "https://pubmed.ncbi.nlm.nih.gov/40649339/", "source_kind": "paper"},
]

d = {
 "slug": "hericium-coralloides", "name_ko": "산호침버섯", "name_en": "Coral tooth fungus",
 "scientific_name": "Hericium coralloides (Scop.) Pers.",
 "aliases": ["Hericium ramosum (Bull.) Letell.", "수실노루궁뎅이", "Coral tooth", "Comb tooth"],
 "sections": sections, "compounds": compounds, "markers": [], "assays": assays, "nutrients": [],
 "production": [], "world": [], "gi": [], "orgs": [], "sources": SOURCES,
}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
print("ok", len(SOURCES))
