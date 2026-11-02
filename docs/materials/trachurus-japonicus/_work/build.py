import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
PM = "https://pubmed.ncbi.nlm.nih.gov/{}/"
PMC = "https://pmc.ncbi.nlm.nih.gov/articles/{}/"
A = "2026-11-02"
S = [
 ("식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 전갱이·전갱이살·전갱이뼈·전갱이포·건조전갱이·전갱이추출물 및 Trachurus·Decapterus 등 전갱이과 원료 행", "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "식품의약품안전처", "2026-10-13"),
 ("Genetic differentiation of Trachurus japonicus from the Northwestern Pacific based on the mitochondrial DNA control region (2013)", PM.format(23544744), "Mitochondrial DNA; doi:10.3109/19401736.2013.773982 (PubMed 23544744)", A),
 ("[Feeding habits of Trachurus japonicus in the East China Sea] (2013)", PM.format(24175535), "Ying Yong Sheng Tai Xue Bao 24(7):2015-24 (PubMed 24175535)", A),
 ("Hatch date and early growth of juvenile Japanese jack mackerel Trachurus japonicus caught in the Uwa Sea (2023)", PM.format(37222291), "Journal of Fish Biology; doi:10.1111/jfb.15462 (PubMed 37222291)", A),
 ("Variations in otolith patterns, sizes and body morphometrics of jack mackerel Trachurus japonicus juveniles (2010)", PM.format(21039508), "Journal of Fish Biology; doi:10.1111/j.1095-8649.2010.02752.x (PubMed 21039508)", A),
 ("Ontogenetic changes in the spatial learning capability of jack mackerel Trachurus japonicus (2010)", PM.format(21155785), "Journal of Fish Biology; doi:10.1111/j.1095-8649.2010.02812.x (PubMed 21155785)", A),
 ("Seasonal changes in infection with trematode species utilizing jellyfish as hosts: evidence of transmission to definitive host fish via medusivory (2016)", PMC.format("PMC4824873"), "Parasite; doi:10.1051/parasite/2016016 (PubMed 27055563)", A),
 ("Relationships between environmental variables and spatial and temporal distribution of jack mackerel (Trachurus japonicus) in the Beibu Gulf, South China Sea (2021)", PMC.format("PMC8572524"), "PeerJ; doi:10.7717/peerj.12337 (PubMed 34760365)", A),
 ("Stock Assessment of the Commercial Small Pelagic Fishes in the Beibu Gulf, the South China Sea, 2006-2020 (2024)", PMC.format("PMC11048411"), "Biology (Basel); doi:10.3390/biology13040226 (PubMed 38666839)", A),
 ("Impacts of Strong ENSO Events on Fish Communities in an Overexploited Ecosystem in the South China Sea (2023)", PMC.format("PMC10376808"), "Biology (Basel); doi:10.3390/biology12070946 (PubMed 37508376)", A),
 ("Seasonal variation in fish school spatial distribution and abundance under the Kuroshio regular pattern and the large meander in Suzu coastal waters (2021)", PMC.format("PMC8631671"), "PLoS One; doi:10.1371/journal.pone.0260629 (PubMed 34847206)", A),
 ("Environmental DNA as a 'Snapshot' of Fish Distribution: A Case Study of Japanese Jack Mackerel in Maizuru Bay, Sea of Japan (2016)", PMC.format("PMC4775019"), "PLoS One; doi:10.1371/journal.pone.0149786 (PubMed 26933889)", A),
 ("Comparison of species-specific qPCR and metabarcoding methods to detect small pelagic fish distribution from open ocean environmental DNA (2022)", PMC.format("PMC9451083"), "PLoS One; doi:10.1371/journal.pone.0273670 (PubMed 36070298)", A),
 ("Structural characterization of carangid fish myoglobins (2012)", PM.format(22361749), "Fish Physiology and Biochemistry; doi:10.1007/s10695-012-9619-z (PubMed 22361749)", A),
 ("A Novel Analysis of the Peptide Terminome Characterizes Dynamics of Proteolytic Regulation in Vertebrate Skeletal Muscle Under Severe Stress (2019)", PMC.format("PMC6473766"), "Proteomes; doi:10.3390/proteomes7010006 (PubMed 30781840)", A),
 ("Functional Sperm of the Yellowtail (Seriola quinqueradiata) Were Produced in the Small-Bodied Surrogate, Jack Mackerel (Trachurus japonicus) (2015)", PM.format(26239188), "Marine Biotechnology; doi:10.1007/s10126-015-9657-5 (PubMed 26239188)", A),
 ("Effects of feeding on plasma concentrations of vitamin A in captive African penguins (Spheniscus demersus) (2019)", PMC.format("PMC6895619"), "Journal of Veterinary Medical Science; doi:10.1292/jvms.19-0316 (PubMed 31548472)", A),
 ("Effect of starvation on lipid metabolism and stability of DHA content of lipids in horse mackerel (Trachurus japonicus) tissues (2003)", PM.format(14870929), "Lipids; doi:10.1007/s11745-003-1187-5 (PubMed 14870929)", A),
 ("Change of volatile compounds in fresh fish meat during ice storage (2011)", PM.format(22416694), "Journal of Food Science; doi:10.1111/j.1750-3841.2011.02388.x (PubMed 22416694)", A),
 ("Prediction of the freshness of horse mackerel (Trachurus japonicus) using E-nose, E-tongue, and colorimeter based on biochemical indexes analyzed during frozen storage of whole fish (2022)", PM.format(36174352), "Food Chemistry; doi:10.1016/j.foodchem.2022.134325 (PubMed 36174352)", A),
 ("The effect of ice crystals formations on the flesh quality of frozen horse mackerel (Trachurus japonicus) (2017)", PM.format(29139545), "Journal of Texture Studies; doi:10.1111/jtxs.12310 (PubMed 29139545)", A),
 ("Purification and Characterization of Cathepsin B from the Muscle of Horse Mackerel Trachurus japonicus (2015)", PMC.format("PMC4663541"), "Marine Drugs; doi:10.3390/md13116550 (PubMed 26516867)", A),
 ("Properties of gelatin film from horse mackerel (Trachurus japonicus) scale (2015)", PM.format(25716323), "Journal of Food Science; doi:10.1111/1750-3841.12806 (PubMed 25716323)", A),
 ("Isolation and characterization of acid-soluble collagen from the scales of marine fishes from Japan and Vietnam (2014)", PM.format(24295705), "Food Chemistry; doi:10.1016/j.foodchem.2013.10.094 (PubMed 24295705)", A),
 ("In Silico Screening and In Vitro Identification of Hyperuricemia-Inhibiting Peptides from Trachurus japonicus (2025)", PMC.format("PMC11817512"), "Foods; doi:10.3390/foods14030524 (PubMed 39942117)", A),
 ("Identification of changes in the microflora composition of Japanese horse mackerel (Trachurus japonicus) during storage to identify specific spoilage organisms (2022)", PMC.format("PMC9391519"), "Current Research in Food Science; doi:10.1016/j.crfs.2022.07.015 (PubMed 35996618)", A),
 ("Survey and Exposure Assessment of Biogenic Amines in Fish Species Commonly Consumed in Korea (2019)", PM.format(30702949), "Journal of Food Protection (PubMed 30702949)", A),
 ("Quantitative risk assessment of Vibrio parahaemolyticus in finfish: a model of raw horse mackerel consumption in Japan (2010)", PM.format(20626688), "Risk Analysis; doi:10.1111/j.1539-6924.2010.01444.x (PubMed 20626688)", A),
 ("Antimicrobial Drug-resistance Profile of Vibrio parahaemolyticus isolated from Japanese Horse Mackerel (Trachurus japonicus) (2021)", PMC.format("PMC8472095"), "Food Safety (Tokyo); doi:10.14252/foodsafetyfscj.D-21-00001 (PubMed 34631335)", A),
 ("Kudoa iwatai and two novel Kudoa spp., K. trachuri n. sp. and K. thunni n. sp. (Myxosporea: Multivalvulida), from daily consumed marine fish in western Japan (2010)", PM.format(21053015), "Parasitology Research; doi:10.1007/s00436-010-2133-2 (PubMed 21053015)", A),
 ("Four carangid fish species as new host records for Kudoa trachuri ..., and description of a new species, Kudoa longichorda sp. n. (2022)", PM.format(36017695), "Folia Parasitologica; doi:10.14411/fp.2022.017 (PubMed 36017695)", A),
 ("[Anisakis simplex larvae: infection status in marine fishes for sale in Shantou] (2014)", PM.format(25223058), "Chinese Journal of Parasitology & Parasitic Diseases 32(3):212-6 (PubMed 25223058)", A),
 ("Fish allergy tolerance 16 months after diagnosis (2021)", PM.format(34476918), "Allergologia et Immunopathologia; doi:10.15586/aei.v49i5.313 (PubMed 34476918)", A),
 ("Improved Raman spectroscopy-based approach to assess microplastics in seafood (2021)", PM.format(34332172), "Environmental Pollution; doi:10.1016/j.envpol.2021.117648 (PubMed 34332172)", A),
 ("Vibrio trachuri sp. nov., a new species isolated from diseased Japanese horse mackerel (1995)", PM.format(8657009), "Microbiology and Immunology; doi:10.1111/j.1348-0421.1995.tb03274.x (PubMed 8657009)", A),
 ("Antioxidizing potentials of BHA, BHT, TBHQ, tocopherol, and oxygen absorber incorporated in a Ghanaian fermented fish product (1998)", PM.format(9598199), "Advances in Experimental Medicine and Biology; doi:10.1007/978-1-4899-1925-0_15 (PubMed 9598199)", A),
 ("Estimating fish population abundance by integrating quantitative data on environmental DNA and hydrodynamic modelling (2020)", PM.format(32608023), "Molecular Ecology; doi:10.1111/mec.15530 (PubMed 32608023)", A),
]
sources = [{"n": i+1, "title": t, "url": u, "publisher": p, "accessed": a} for i, (t, u, p, a) in enumerate(S)]

sections = [
 {"key": "overview", "title": "한눈에 보기", "body":
  "전갱이(학명 Trachurus japonicus)는 전갱이과(Carangidae) 전갱이속의 바닷물고기로, 식약처 식품원료 목록의 영문명은 Japanese jack mackerel이다[1]. 중국·한국·일본 연안에 널리 분포하는 부어류(표층·중층을 헤엄쳐 다니는 물고기)로 기술된다[2].\n\n"
  "식약처 「식품원료 목록」에는 전갱이, 전갱이살, 전갱이뼈, 전갱이포, 건조전갱이, 전갱이추출물 등 이 학명의 원료명 6개가 모두 수산물, '사용가능'으로 올라 있고 사용조건 칸은 비어 있다[1]. 원자료의 부위 칸은 전갱이살 행이 '죽순', 전갱이뼈 행이 '어린싹', 나머지 네 행이 '-'로 적혀 있으며, 이 글은 원자료 표기를 그대로 옮긴다[1]. 건강기능식품 고시형 원료의 원재료 목록에는 올라 있지 않아 고시 지표성분은 없다[1].\n\n"
  "일본에서는 날것으로 흔히 먹는 생선이어서 장염비브리오 위해 평가의 모델 어종으로 쓰였고[28], 기름이 많은 등푸른 생선답게 얼음 보관 중 지질 산화 냄새 성분이 빨리 늘어난다[19]. 한국에서 많이 먹는 생선 19종의 생체아민 조사에서는 'Japanese jack mackerel' 등 일부 어종의 생체아민 노출량이 일부 국가 기준을 넘었다[27]."},
 {"key": "history", "title": "이름과 분류의 역사", "body":
  "학명 Trachurus japonicus는 Temminck와 Schlegel이 기재한 이름으로, 기생충 연구 논문도 저자명을 이렇게 표기했다[31]. 영문으로는 Japanese jack mackerel 외에 Japanese horse mackerel, horse mackerel, jack mackerel이 함께 쓰인다[1, 8, 22, 26]. 'horse mackerel'과 'jack mackerel'은 다른 전갱이속 종에도 쓰이므로, 이 글은 학명이 T. japonicus로 밝혀진 자료만 근거로 삼았다[1].\n\n"
  "이 종에서 처음 발견되어 종소명에 속명(trachuri)이 붙은 생물도 있다[30, 35]. 1995년 병든 양식 전갱이에서 새 세균 Vibrio trachuri가 기재되었고[35], 2010년에는 나가사키 앞바다 전갱이 근육의 포자충이 Kudoa trachuri라는 새 종으로 기재되었다[30].\n\n"
  "우리말 이름 '전갱이'의 어원과 옛 문헌 기록은 이번 조사에서 공공기관·학술 원문으로 확인하지 못함. 지리적 표시 등록 자료에서 이 학명에 연결된 항목도 확인하지 못함."},
 {"key": "biology", "title": "어종과 생태", "body":
  "전갱이는 중국에서 한국, 일본까지 널리 분포하는 부어성 어종이다[2]. 동중국해에서 2008–2009년 계절별로 잡은 453마리(가랑이 길이 46–250 mm)의 위 내용물에서 먹이 생물 124종이 나왔고, 상대 중요도 지수로는 작은 물고기인 Bregmaceros macclellandi가 39.2%로 가장 컸다[3]. 가랑이 길이 약 100 mm에서 먹이 구성이 갑자기 바뀌었고, 평균 영양 단계는 3.51로 플랑크톤과 유영 동물을 먹는 하위 육식어로 평가되었다[3].\n\n"
  "산란장에 따라 산란기가 다르며, 와카사만과 고토나다의 치어는 이석 무늬·크기와 체형으로 부화 시기·장소가 다른 세 무리로 나뉘었다[5]. 일본 우와해에 들어온 치어(2011–2015년)는 2–4월에 부화했고, 자어기 평균 성장률은 하루 0.30–0.34 mm, 변태 시작 일령은 25.5–30.5일이었으며, 저자들은 대부분이 동중국해 등 다른 해역에서 왔다고 보았다[4]. 치어는 표준체장 약 51.7 mm에서 학습 능력이 크게 늘었는데, 이 크기는 먼바다에서 연안 암초로 옮겨 오는 크기와 맞았다[6]. 세토내해에서는 치어가 해파리에 붙어 다니는 모습이 관찰되었다[7].\n\n"
  "통째로 간 전갱이 10마리의 건물(마른 무게) 함량은 평균 29.1 ± 2.8%였다[17]."},
 {"key": "related_species", "title": "가까운 종과 혼동", "body":
  "식약처 「식품원료 목록」에는 같은 전갱이속의 녹줄매가리(Trachurus declivis, Greenback horse mackerel)와 Chilean jack mackerel(Trachurus murphyi)이 각각 별개 원료로 올라 있다[1]. 같은 과의 가라지(Decapterus maruadsi), 갈고등어(Decapterus muroadsi), 긴가라지(Decapterus macrosoma), 붉은가라지(Decapterus akaadsi), 풀가라지(Decapterus macarellus)도 따로 있으므로 이들의 성분·안전 자료를 전갱이 자료로 옮겨 쓰지 않는다[1].\n\n"
  "이름에 '전갱이'가 들어가지만 다른 속인 원료도 많아, 갈전갱이(Carangoides equula), 미늘전갱이(Carangoides dinema), 민전갱이(Uraspis helvola), 실전갱이(Alectis ciliaris), 줄전갱이(Caranx sexfasciatus), 흑점줄전갱이(Pseudocaranx dentex)가 목록에 따로 있다[1].\n\n"
  "전갱이과 5종의 마이오글로빈 아미노산 서열은 서로 81–99% 같았고, 서열로 그린 계통수는 형태 분류와 일치했다[14]. 전갱이에서 기재된 포자충 Kudoa trachuri는 2022년 흑점줄전갱이와 가라지속 3종에서도 확인되어, 이 기생충이 전갱이에만 있는 것은 아니다[31]. 남중국해 베이부만에서는 전갱이와 가라지류가 함께 주요 소형 부어류로 조사되었다[10]."},
 {"key": "cultivation", "title": "어획과 자원", "body":
  "남중국해 베이부만의 2013–2014년 조사에서 전갱이는 주로 수심 50–75 m, 표층 염분 32.3–33.5 PSU, 표층 수온 25–30.5 ℃에서 잡혔고, 단위노력당 어획량은 여름에 가장 높았다[8]. 저자들은 이 해역 전갱이 자원이 크게 변동하며 IUCN 적색목록에 올랐다고 적었다[8]. 2006–2020년 저층 트롤 자료로 본 베이부만 소형 부어류 2종(전갱이 포함)은 2006–2010년에 남획 상태였다가 2011년 이후 적정 이용 수준으로 바뀌었으나, 평균 체장과 점근 체장은 줄었다[9]. 강한 엘니뇨·라니냐 때 이 해역의 전갱이 분포와 양이 크게 흔들렸다[10]. 일본 고치현 스즈 연안에서는 구로시오 대사행 시기에 정치망의 전갱이 어획이 훨씬 많았다[11].\n\n"
  "일본 마이즈루만에서는 바닷물의 환경 DNA 농도가 어군 탐지기 반응과 함께 움직여, 전갱이 분포·자원량을 물 시료로 추정하는 방법이 개발되었다[12, 37]. 쿠로시오 확장역에서는 종 특이 qPCR이 메타바코딩보다 전갱이 등 소형 부어류를 더 자주 검출했다[13].\n\n"
  "양식되는 전갱이도 있어, 자연산·양식 개체의 장염비브리오를 비교한 연구[29]와 병든 양식 전갱이에서 새 병원 세균을 기재한 연구[35]가 있고, 작은 전갱이를 대리모로 써서 방어 정자를 만든 실험도 있었다[16]. 한국 연근해 전갱이 어획량과 양식 생산량의 공식 통계는 이번 조사에서 확인하지 못함."},
 {"key": "processing", "title": "가공과 이용", "body":
  "식약처 목록의 원료명만 보아도 전갱이는 생선, 살, 뼈, 포, 건조품, 추출물 형태로 쓰인다[1]. 일본에서는 날것으로 많이 먹으며, 위해 평가 모형에서 손질할 때 생선을 씻으면 장염비브리오 발병 위험이 약 10분의 1로 줄었다[28].\n\n"
  "냉동 전갱이를 녹이면 얼음 결정이 근육 세포와 세포외기질을 망가뜨려 K값(선도 지표) 상승 속도가 냉동하지 않은 것의 약 1.4배였다[21]. 90일 냉동 저장 중 선도는 전자코·전자혀·색차계 신호를 합쳐 기계학습으로 예측할 수 있었다[20]. 얼음 보관 3–4일 동안 헥사날 등 알데하이드·알코올이 빠르게 늘어 흰살생선보다 휘발 성분 변화가 컸다[19]. 20 ℃ 보관에서는 24–48시간 사이 휘발성 염기질소가 급증했으나 4 ℃에서는 168시간 동안 거의 늘지 않았다[26].\n\n"
  "살에서 정제한 카텝신 B는 최적 pH 5.0, 50 ℃였고, 이 효소의 특이 억제제가 가열 겔의 '모도리'(가열 중 겔 약화)를 막았다[22]. 비늘에서는 젤라틴(수율 1.08–3.45%)을 뽑아 수증기 투과가 낮은 포장 필름을 만들었고[23], 산 가용성 I형 콜라겐도 분리되었다[24]. 가나식 발효 건어물을 전갱이로 만들어 산화 방지제 효과를 비교한 연구도 있다[36]. 전갱이 단백질 서열에서 컴퓨터로 고른 뒤 합성한 펩타이드 4종이 세포 실험에서 요산을 낮췄으나, 이는 사람 효과의 근거가 아니다[25]."},
 {"key": "genetics", "title": "유전체와 유전 다양성", "body":
  "중국·일본 연안 8개 집단의 미토콘드리아 조절영역 분석에서 변이 자리 87개가 하플로타입 168개를 정의했다[2]. 하플로타입 다양도는 0.964–1.000으로 높고 염기 다양도는 0.011–0.015로 낮았으며, 집단 간 유의한 유전 분화가 없어 최근 집단이 불어난 것으로 해석되었다[2].\n\n"
  "마이오글로빈 유전자는 뉴클레오타이드 444개의 열린 해독틀로 아미노산 147개를 암호화한다[14]. 근육 카텝신 B는 RT-PCR로 아미노산 215개 길이의 부분 cDNA가 클로닝되었다[22]. 2019년 연구진은 전장 유전체가 없어 전사체로 단백질 참조 자료를 만들었고, 그 안에서 단백질 분해효소 72종의 발현을 확인했다[15]. 이후 전갱이 참조 유전체 공개 여부는 이번 조사에서 확인하지 못함.\n\n"
  "종 특이 프라이머·탐침을 쓴 qPCR은 바닷물의 환경 DNA로 전갱이를 검출·정량하는 데 쓰인다[12, 13]. 이 방법으로 추정한 마이즈루만 전갱이 수는 어군 탐지기 추정치와 비슷했고, 어시장에서 흘러든 DNA가 오차 원인으로 드러났다[37]."},
 {"key": "safety", "title": "안전성", "body":
  "식약처 「식품원료 목록」에서 전갱이와 그 가공 원료 6개는 모두 '사용가능'이며 별도 사용조건은 적혀 있지 않다[1]. 한국에서 흔히 먹는 생선 19종 609건의 생체아민 조사에서 'Japanese jack mackerel' 등 일부 어종의 노출량이 외국 기준을 넘었다[27]. 이 종의 히스타민 수치와 국내 기준 대비 결과는 원문 수치로 확인하지 못함.\n\n"
  "날것으로 먹을 때는 장염비브리오가 주된 세균 위해로 평가되었고, 운송 중 온도가 높으면 위험이 50% 늘었다[28]. 자연산·양식 전갱이에서 분리한 장염비브리오에서는 암피실린 내성 균주가 많았다[29]. 상온 보관에서는 Shewanella 속 세균이 우세해지며 부패가 진행되었다[26].\n\n"
  "중국 산터우 시장 조사에서 전갱이 9마리 모두에서 고래회충류(Anisakis simplex) 유충이 나왔고, 52종 전체 조사에서 유충은 근육에서는 나오지 않았고 장간막에서 가장 많이 나왔다[32]. 일본산 전갱이 근육에서는 포자충 Kudoa trachuri 낭포가 보고되었다[30]. 생후 13개월 아이가 전갱이 알레르기로 진단되었다가 16개월 뒤 내성이 생긴 사례가 있다[33]. 홍콩 해역 전갱이에서 미세플라스틱이 확인되었다[34]. 이 종의 수은·중금속 함량과 국내 공공기관 알레르기 정보는 확인하지 못함."},
]

compounds = [
 {"name": "Retinol", "name_ko": "비타민 A1(레티놀과 그 지방산 에스터)", "class": "지용성 비타민", "role": "nutrient", "part": "통째로 간 생선(수족관 먹이용 전갱이 10마리)",
  "content_text": "평균 7,700 ± 3,550 μg/kg 건물(범위 3,970–15,210 μg/kg 건물)[17]", "activity_ko": "생선 무게가 클수록 함량이 높았다(r=0.583)[17]", "source": [17]},
 {"name": "3,4-Didehydroretinol", "name_ko": "비타민 A2(3,4-다이디하이드로레티놀)", "class": "지용성 비타민", "role": "nutrient", "part": "통째로 간 생선",
  "content_text": "평균 1,410 ± 430 μg/kg 건물(범위 770–2,260 μg/kg 건물), 비타민 A1의 약 5분의 1[17]", "activity_ko": "해산어에도 상당량 들어 있음이 HPLC·흡수 스펙트럼으로 확인되었다[17]", "source": [17]},
 {"name": "Docosahexaenoic acid", "name_ko": "도코사헥사엔산(DHA)", "class": "오메가-3 다가불포화지방산", "role": "nutrient", "part": "등 보통근(살)",
  "content_text": "107일 굶긴 실험에서 근육 총지질 중 DHA 비율이 오히려 높아졌다(정량값은 초록에 없음)[18]", "activity_ko": "세포막 인지질(PE·PC)의 DHA가 굶주림에도 유지되었다[18]", "source": [18]},
 {"name": "Triacylglycerol", "name_ko": "트라이아실글리세롤(중성지방)", "class": "지질", "role": "nutrient", "part": "등 보통근·껍질",
  "content_text": "처음 근육 총지질의 85% 초과, 껍질은 그보다 높음[18]", "activity_ko": "굶은 첫 44일 동안 급감해 저장 에너지로 쓰였다[18]", "source": [18]},
 {"name": "Hexanal", "name_ko": "헥사날", "class": "지질 산화 알데하이드(휘발성)", "role": "bioactive", "part": "살(얼음 보관)",
  "content_text": "얼음 보관 초기부터 늘어난 주된 휘발 성분(정량값은 초록에 없음)[19]", "activity_ko": "등푸른 생선의 선도 저하·비린 냄새 지표로 제안되었다[19]", "source": [19]},
 {"name": "1-Heptanol", "name_ko": "1-헵탄올", "class": "지질 산화 알코올(휘발성)", "role": "bioactive", "part": "살(얼음 보관)",
  "content_text": "(E)-2-옥테날·(E)-2-헥세날 등과 함께 얼음 보관 중 빠르게 증가(정량값은 초록에 없음)[19]", "activity_ko": "흰살생선이 아닌 생선의 선도 지표 후보[19]", "source": [19]},
 {"name": "Histamine", "name_ko": "히스타민(생체아민)", "class": "생체아민(위해 성분)", "role": "bioactive", "part": "살(한국 유통 시료)",
  "content_text": "'Japanese jack mackerel' 시료의 생체아민 노출이 일부 국가 기준을 넘음(이 종 수치는 초록에 없음)[27]", "activity_ko": "부패 세균이 아미노산을 분해해 만들며 급성 중독을 일으킬 수 있다[27]", "source": [27]},
 {"name": "Trimethylamine N-oxide", "name_ko": "트라이메틸아민 N-옥사이드(TMAO)", "class": "삼투조절 물질", "role": "bioactive", "part": "살",
  "content_text": "부패균이 TMAO를 환원해 휘발성 염기질소를 만든다; 20 ℃ 24–48시간 사이 휘발성 염기질소 급증(수치는 그림에만 있음)[26]", "activity_ko": "휘발성 염기질소(TVB-N)는 부패 지표로 쓰인다[26]", "source": [26]},
 {"name": "Myoglobin", "name_ko": "마이오글로빈", "class": "근육 단백질", "role": "bioactive", "part": "근육",
  "content_text": "아미노산 147개(열린 해독틀 444 뉴클레오타이드)[14]", "activity_ko": "살 색을 내는 헴 단백질로, 전갱이과 종 사이 서열 일치도 81–99%[14]", "source": [14]},
 {"name": "Cathepsin B", "name_ko": "카텝신 B", "class": "시스테인 단백질 분해효소", "role": "bioactive", "part": "살",
  "content_text": "28 kDa·6 kDa 두 사슬형; 최적 pH 5.0, 최적 온도 50 ℃[22]", "activity_ko": "가열 겔의 모도리 현상을 일으키며 억제제로 막을 수 있었다[22]", "source": [22]},
 {"name": "Gelatin", "name_ko": "젤라틴(비늘)", "class": "단백질", "role": "bioactive", "part": "비늘",
  "content_text": "70–90 ℃, 15분–3시간 추출 수율 1.08–3.45%; 소수성 아미노산 1,000잔기당 653개[23]", "activity_ko": "수증기 투과도가 낮고 자외선 차단이 좋은 식품 포장 필름 소재[23]", "source": [23]},
 {"name": "Collagen type I", "name_ko": "I형 콜라겐(산 가용성)", "class": "단백질", "role": "bioactive", "part": "비늘",
  "content_text": "α1·α2 사슬과 β 성분으로 된 I형; 베트남산이 일본산보다 이미노산 함량이 높음[24]", "activity_ko": "비늘 부산물 이용 소재[24]", "source": [24]},
 {"name": "Gln-Pro-Ser-Phe", "name_ko": "QPSF 펩타이드(합성)", "class": "펩타이드(컴퓨터 예측 후 합성)", "role": "bioactive", "part": "전갱이 단백질 서열(가상 효소 분해)",
  "content_text": "잔틴산화효소 IC50 38.39 ± 7.25 mM(합성 펩타이드, 시험관)[25]", "activity_ko": "4 mM에서 HK-2 세포 요산을 48.61% 낮춤 — 세포 실험일 뿐 사람 효과 근거 아님[25]", "source": [25]},
]

E = {k: "" for k in ["instrument","column","mobile_phase","gradient","flow","temp","detection","injection","sample_prep","standard","linearity","lod","loq","recovery"]}
def C(**kw):
    d = dict(E); d.update(kw); return d
assays = [
 {"role": "literature", "compound": "Retinol / 3,4-Didehydroretinol (vitamin A1·A2)", "compound_ko": "비타민 A1·A2",
  "part": "수족관 펭귄 먹이용 전갱이 10마리를 마리별로 통째로 간 시료",
  "content": "비타민 A1 7,700 ± 3,550 μg/kg 건물, 비타민 A2 1,410 ± 430 μg/kg 건물[17]",
  "method": "비누화·헥세인 추출 후 HPLC-UV(역상)",
  "conditions": C(instrument="Shimadzu LC-10AD, 분광 검출기 SPD10A(확인용 다이오드 어레이 DAD-3000)",
                  column="UG120(150 mm × 4.6 mm, 5 μm) 역상",
                  mobile_phase="A1: 메탄올-에탄올(80/20, v/v); A2: 메탄올-물(90/10, v/v)",
                  flow="1.0 mL/min",
                  detection="A1 325 nm, A2 350 nm; 3,4-다이디하이드로레티놀은 260–380 nm 흡수 스펙트럼으로 확인",
                  sample_prep="식품 비타민 A 표준 정량법에 따라 수산화칼륨 비누화 → n-헥세인 추출; 수분은 AOAC 950.46",
                  standard="3,4-다이디하이드로레티놀 표준품"),
  "rationale": "해산어에도 비타민 A2가 상당량 있음을 확인하려고 전갱이 시료에서 두 형태를 나누어 정량했다[17]. 전문(Materials and Methods) 확인 — 직선성·검출한계·회수율은 생선 시료에 대해 적혀 있지 않다(정량한계 1.6 μg/dL는 혈장 시료 값)[17].",
  "source": [17], "url": PMC.format("PMC6895619"), "source_kind": "paper"},
 {"role": "literature", "compound": "Total volatile basic nitrogen (TVB-N)", "compound_ko": "휘발성 염기질소",
  "part": "가나가와현 마트 구입 전갱이 42마리(길이 18.0–23.7 cm)의 가슴지느러미–항문 사이 절편의 껍질·근육·내장",
  "content": "20 ℃ 24–48시간 사이 급증, 4 ℃ 168시간 동안 거의 변화 없음(수치는 그림에만 제시)[26]",
  "method": "콘웨이 미량확산법(부분 변형) 후 적정",
  "conditions": C(detection="0.01 M NaOH 중화 적정, 지시약 메틸레드-메틸렌블루 에탄올 용액",
                  temp="37 °C, 1시간 확산",
                  sample_prep="부위별 시료에 완충 식염수 9배 가해 균질화 → 다시 5배 희석해 콘웨이 외실에 넣고 포화 K2CO3 1 mL 첨가, 내실에는 5 mM H2SO4 1 mL",
                  standard="대조: 증류수"),
  "rationale": "암모니아·다이메틸아민·트라이메틸아민을 합친 TVB-N은 생선 부패 지표로 쓰인다[26]. 전문(Methods 2.3) 확인 — 검출한계·회수율은 적혀 있지 않다[26].",
  "source": [26], "url": PMC.format("PMC9391519"), "source_kind": "paper"},
 {"role": "literature", "compound": "Biogenic amines (histamine etc.)", "compound_ko": "생체아민(히스타민 등)",
  "part": "한국 유통 생선 19종 609건 중 'Japanese jack mackerel' 시료",
  "content": "일부 어종(전갱이 포함)의 노출량이 일부 국가 기준 초과(전갱이 수치는 초록에 없음)[27]",
  "method": "",
  "conditions": C(),
  "rationale": "히스타민 등 생체아민은 빨리 상하는 생선의 급성 중독 원인이어서 감시 대상이다[27]. 전문 확인 못함 — 초록에 분석 기기·조건이 없고, 시료 학명도 초록에 적혀 있지 않다[27].",
  "source": [27], "url": PM.format(30702949), "source_kind": "paper"},
]

d = {"slug": "trachurus-japonicus", "name_ko": "전갱이", "name_en": "Japanese jack mackerel", "scientific_name": "Trachurus japonicus",
     "aliases": ["Japanese jack mackerel", "Japanese horse mackerel", "전갱이살", "전갱이뼈", "전갱이포", "건조전갱이", "전갱이추출물"],
     "sections": sections, "compounds": compounds, "markers": [], "assays": assays, "nutrients": [], "production": [], "world": [],
     "gi": [], "orgs": [], "sources": sources}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in sections: print(s["key"], len(s["body"]))
