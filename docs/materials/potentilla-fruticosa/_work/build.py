import json
from pathlib import Path
A="2026-11-02"
def pm(n,title,journal,pmid,pmc=None):
    url=f"https://pmc.ncbi.nlm.nih.gov/articles/{pmc}/" if pmc else f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
    pub=f"{journal} (PubMed PMID {pmid}"+(f", {pmc} 전문)" if pmc else ")")
    return {"n":n,"title":title,"url":url,"publisher":pub,"accessed":A}
S=[
 {"n":1,"title":"식품원료 목록(흰물싸리잎, Potentilla fruticosa / Dasiphora fruticosa var. coreana Nakai)","url":"https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020","publisher":"식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020)","accessed":"2026-10-13"},
 {"n":2,"title":"백두대간 동식물 — 식물종 정보 목록(흰물싸리 | Potentilla fruticosa var. mandshurica Maxim.) — 원문 페이지는 열지 못하고 WebSearch 요약으로만 확인","url":"https://www.forest.go.kr/kfsweb/kfi/kfs/bkmnt/selectPlantBioList.do?mn=AR03_05_05_02","publisher":"산림청(WebSearch 요약)","accessed":A},
 {"n":3,"title":"신품종출원 품종목록 식물검색(물싸리 | Dasiphora fruticosa (L.) Rydb.) — 원문 페이지는 열지 못하고 WebSearch 요약으로만 확인","url":"https://nfsv.forest.go.kr/kfsweb/mer/nvm/search/selectSearchCropsList.do?mn=UKFV_01_05_01","publisher":"산림청 국립산림품종관리센터(WebSearch 요약)","accessed":A},
 pm(4,"A high-quality genome assembly of the shrubby cinquefoil (Dasiphora fruticosa) (2024)","Scientific Data","39214997","PMC11364759"),
 pm(5,"Genomic analysis of Dasiphora on the Qinghai-Tibet Plateau provides insights into genetic divergence and flower color variation (2025)","The Plant Journal","41169030"),
 pm(6,"Signatures of Adaptation and Purifying Selection in Highland Populations of Dasiphora fruticosa (2024)","Molecular Biology and Evolution","38768215","PMC11156201"),
 pm(7,"The coexistence of hermaphroditic and dioecious plants is associated with polyploidy and gender dimorphism in Dasiphora fruticosa (2019)","Plant Diversity","31934677","PMC6951273"),
 pm(8,"Range shifts of Potentilla fruticosa on the Qinghai-Tibetan Plateau during glacial and interglacial periods revealed by chloroplast DNA sequence variation (2009)","Heredity","19920855"),
 pm(9,"Phytochemical profiles, antioxidant and antimicrobial activities of three Potentilla species (2013)","BMC Complementary and Alternative Medicine","24252124","PMC3840622"),
 pm(10,"Quality Evaluation of Potentilla fruticosa L. by High Performance Liquid Chromatography Fingerprinting Associated with Chemometric Methods (2016)","PLoS ONE","26890416","PMC4758616"),
 pm(11,"Influence of Environmental Factors on the Active Substance Production and Antioxidant Activity in Potentilla fruticosa L. and Its Quality Assessment (2016)","Scientific Reports","27373366","PMC4931507"),
 pm(12,"Phenolic profiles and antioxidant capacities of crude extracts and subsequent fractions from Potentilla fruticosa L. leaves (2015)","Natural Product Research","26371751"),
 pm(13,"Phenolic Compounds and Antioxidant Activity of Different Organs of Potentilla fruticosa L. from Two Main Production Areas of China (2016)","Chemistry & Biodiversity","27450426"),
 pm(14,"Effects of Growing Location on the Contents of Main Active Components and Antioxidant Activity of Dasiphora fruticosa (L.) Rydb. by Chemometric Methods (2018)","Chemistry & Biodiversity","29772109"),
 pm(15,"High-Pressure Extraction of Antioxidant-Rich Fractions from Shrubby Cinquefoil (Dasiphora fruticosa L. Rydb.) Leaves: Process Optimization and Extract Characterization (2020)","Antioxidants","32466350","PMC7346160"),
 pm(16,"A new methylene bisflavan-3-ol from the branches and leaves of Dasiphora fruticosa (2019)","Natural Product Research","30663382"),
 pm(17,"Investigation of free amino acid, total phenolics, antioxidant activity and purine alkaloids to assess the health properties of non-Camellia tea (2016)","Acta Pharmaceutica Sinica B","27006902","PMC4788713"),
 pm(18,"Synergistic Effects of Potentilla fruticosa L. Leaves Combined with Green Tea Polyphenols in a Variety of Oxidation Systems (2016)","Journal of Food Science","27061936"),
 pm(19,"Synergistic effects and related bioactive mechanism of Potentilla fruticosa L. leaves combined with Ginkgo biloba extracts studied with microbial test system (MTS) (2016)","BMC Complementary and Alternative Medicine","27905920","PMC5134079"),
 pm(20,"Variation in total polyphenolics contents of aerial parts of Potentilla species and their anticariogenic activity (2010)","Molecules","20657382","PMC6257586"),
 pm(21,"Antimicrobial activity of Potentilla species (2008)","Fitoterapia","18664379"),
 pm(22,"Investigation of the antimicrobial activity of Rhaponticum (Rhaponticum carthamoides D.C. Iljin) and shrubby cinquefoil (Potentilla fruticosa L.) (2011)","Medicina (Kaunas)","21822040"),
 pm(23,"Hepatoprotective properties of aqueous extract from Pentaphylloides fruticosa during chronic toxic hepatitis (2001)","Bulletin of Experimental Biology and Medicine","11550056"),
 pm(24,"[Experimental therapy of Coxsackie B3 virus infection with immunomodulator contained in water-soluble Penthaphylloides fruticosa extract] (2005)","Zhurnal Mikrobiologii, Epidemiologii i Immunobiologii","16028531"),
 pm(25,"[Effect of course intake of a bio-active flavonoid-containing plant preparation (Pentaphylloides fruticosa water-soluble extract) on the level of anxiety and sensorimotor reactivity in rats] (2014)","Patologicheskaia Fiziologiia i Eksperimental'naia Terapiia","25980224"),
 pm(26,"Effect of several flavonoid-containing plant preparations on activity of mitochondrial ATP-dependent potassium channel (2008)","Bulletin of Experimental Biology and Medicine","19145325"),
 pm(27,"The influence of aqueous extracts of selected Potentilla species on normal human colon cells (2013)","Acta Poloniae Pharmaceutica","23757943"),
 pm(28,"Ultrasound-Assisted Extraction of Flavonoids from Potentilla fruticosa L. Using Natural Deep Eutectic Solvents (2022)","Molecules","36144529","PMC9504222"),
 pm(29,"Evaluation of antioxidative properties of Geranium macrorrhizum and Potentilla fruticosa extracts in Dutch style fermented sausages (2007)","Meat Science","22061961"),
 pm(30,"Proteomic analysis of Potentilla fruticosa L. leaves by iTRAQ reveals responses to heat stress (2017)","PLoS ONE","28829780","PMC5568749"),
 pm(31,"Leaf Stoichiometry of Potentilla fruticosa Across Elevations in China's Qilian Mountains (2022)","Frontiers in Plant Science","35283932","PMC8907977"),
 pm(32,"Assessing facilitative responses to a nurse shrub at the community level: the example of Potentilla fruticosa in a sub-alpine grassland of northwest China (2010)","Plant Biology","20701701"),
 pm(33,"First Report of Powdery Mildew Caused by Podosphaera aphanis var. aphanis on Potentilla fruticosa in Italy (2005)","Plant Disease","30791328"),
 pm(34,"Assessment of anti-oxidant activity of plant extracts using microbial test systems (2009)","Journal of Applied Microbiology","19187149"),
]
sec=[]
def add(k,t,b): sec.append({"key":k,"title":t,"body":b})
add("overview","한눈에 보기",
"흰물싸리는 장미과(Rosaceae)의 키 작은 낙엽 떨기나무로, 식약처 「식품원료 목록」에는 학명 'Potentilla fruticosa / Dasiphora fruticosa var. coreana Nakai', 다른 이름 '은물싸리', 영어 이름 'Yellow gem, Shrubby cinquefoil'로 '흰물싸리잎'이 올라 있다[1]. 사용 조건은 '사용가능부위 : 잎'인 사용가능 원료이므로 식품에는 잎만 쓸 수 있다[1]. 이 종을 원재료로 하는 건강기능식품 고시형 원료는 확인하지 못함.\n\n"
"학계에서는 이 식물을 Potentilla 속에 두기도 하고 따로 떼어 Dasiphora 속(Dasiphora fruticosa)으로 다루기도 한다[4, 16]. 중국에서는 잎을 차로 널리 마시고 '진라오메이(금로매)' 차가 시판된다는 보고가 있다[18]. 잎의 대표 성분은 하이퍼로사이드(퀘르세틴 갈락토사이드)·(+)-카테킨·엘라그산 같은 폴리페놀이며, 중국 칭하이 시료 잎에서는 하이퍼로사이드가 8.86 mg/g으로 정량된 성분 가운데 가장 많았다[9]. 다만 이런 연구는 대부분 중국·유럽의 노란 꽃 개체를 시료로 했고, 국내 자생 흰물싸리 잎을 분석한 논문은 확인하지 못함.")
add("history","역사와 전통적 이용",
"중국에서 이 식물은 '진라오메이'·'거상화'로 불리며 티베트 전통의학에서 염증·상처·설사·당뇨 등에 쓰는 민간 약초로 소개된다[19]. 잎은 중국에서 차로 널리 쓰이고 여러 '진라오메이' 차 제품이 시장에 있다는 보고가 있다[18]. 차나무가 아닌 식물로 만든 민간차 33종을 비교한 연구에서도 이 종의 차가 포함되었다[17]. 정원 관상수로도 쓰이고, 잎은 식품 첨가물과 화장품 원료로도 쓰인다는 설명이 있다[9, 10].\n\n"
"서시베리아에서 자라는 약초 20종을 비교한 연구에서도 이 종(Pentaphylloides fruticosa) 추출물은 항산화 활성이 높은 축에 들었다[34]. 러시아에서는 Pentaphylloides fruticosa라는 이름으로 이 식물의 수용성 추출물을 만들어 쥐·생쥐 실험을 한 보고가 2000년대에 여럿 나왔다[23, 24, 26]. 리투아니아에서는 이 식물의 극성 추출물을 발효 소시지의 산화 방지에 시험한 연구가 있었다[29]. 한국에서 흰물싸리 잎을 전통적으로 먹거나 약으로 쓴 기록은 확인하지 못함.")
add("biology","생물학적 특징",
"Dasiphora fruticosa는 북반구의 서늘한 온대·아한대에 널리 자라는 떨기나무이며, 칭하이-티베트 고원에서는 해발 400–5,000 m에 분포한다[4]. 같은 속에는 노란 꽃잎의 D. fruticosa와 흰 꽃잎의 D. glabra 두 종이 있다는 설명이 있다[4]. 티베트 고원 시료에서 D. fruticosa의 노란 꽃잎은 플라보놀(퀘르세틴) 축적, D. glabra의 흰 꽃잎은 프로안토시아니딘 합성과 관련된 것으로 분석되었다[5].\n\n"
"칭하이-티베트 고원 일부 집단에는 수꽃·암꽃·양성화 개체가 함께 자라며, 암수딴그루 개체의 DNA 양이 양성화 개체의 약 2배였다[7]. 치롄산맥 해발 2,400–3,800 m에서 잎의 질소 농도는 3,500 m에서 27.33 g/kg으로 가장 높았고, 인 농도는 3,800 m에서 0.60 g/kg으로 가장 낮았다[31]. 3년생 개체를 42 °C에 3일 두면 잎의 엽록체 틸라코이드 구조가 손상되었다[30].")
add("related_species","근연종과 혼동 주의",
"식약처 목록은 이 원료의 학명을 'Potentilla fruticosa / Dasiphora fruticosa var. coreana Nakai'로 적고 다른 이름을 '은물싸리'로 둔다[1]. 산림청 백두대간 식물종 목록에는 흰물싸리가 Potentilla fruticosa var. mandshurica Maxim.으로 올라 있다는 검색 요약이 있으나 원문 페이지는 열지 못했다[2]. 국립산림품종관리센터 목록에서는 '물싸리'의 학명을 Dasiphora fruticosa (L.) Rydb.로 적는다는 검색 요약이 있다[3]. 따라서 국명 흰물싸리와 물싸리가 같은 종의 변종 관계인지, 흰 꽃 근연종(D. glabra 등)에 가까운지는 공식 자료로 확인하지 못함.\n\n"
"티베트 고원 연구에서는 4배체 D. fruticosa와 D. glabra가 함께 묶이고 2배체 D. fruticosa가 따로 갈라져, 이 무리의 분류가 아직 불확실하다고 보고했다[5]. 잎 성분을 비교한 연구에서 P. glabra와 P. parvifolia는 하이퍼로사이드·루틴 함량이 이 종과 크게 달랐으므로 값을 섞으면 안 된다[9]. 같은 목록에는 딱지꽃(P. chinensis)·물양지꽃(P. cryptotaeniae)·Silverweed(P. anserina)·가락지나물(P. anemonefolia)·털딱지꽃(P. chinensis var. concolor)·솜양지꽃(P. discolor)이 별도 원료로 있으며, 이 자료에는 그 종들의 값을 쓰지 않았다[1].")
add("cultivation","재배와 채취",
"국내에서 흰물싸리를 식품용으로 재배·채취한 생산 통계는 확인하지 못함. 이 종은 관상 가치가 높은 꽃나무로 정원과 공원에 심으며[4, 33], 이탈리아 정원에서는 흰가루병(Podosphaera aphanis var. aphanis)이 처음 보고되었다[33]. 중국 서북부 아고산 초지에서는 다른 풀의 생장을 돕는 우점 떨기나무로 연구되었다[32].\n\n"
"중국 8개 지역에서 7월에 성숙한 잎을 따서 40 °C 진공 건조한 시료를 비교한 연구에서는 쓰촨성 캉딩 시료가 탄닌·총플라보노이드·총페놀 함량과 항산화 활성이 가장 높았다[10]. 같은 연구진은 해발고도·연간 일조시간이 플라보노이드·루틴 함량과 양(+)의 상관을, 해발고도가 탄닌 함량과 음(−)의 상관을 보였다고 보고했다[11]. 중국 5개 주산지 시료에서는 탄닌 7.65–10.69%, 총플라보노이드 2.30–5.39%, 루틴 0.18–0.81%로 산지에 따라 달랐고, 토양의 유효 인 함량이 주요 요인으로 꼽혔다[14].")
add("processing","가공과 추출",
"연구에서는 잎을 그늘이나 저온에서 말린 뒤 가루로 만들어 썼다[9, 10, 15]. 성분 분석용 추출은 80% 차가운 아세톤(4 °C, 1시간, 3회)[9]이나 70% 에탄올(45 °C, 2시간, 3회, 액고비 15:1)[10]을 썼다. 리투아니아 잎 시료는 초임계 이산화탄소로 지용성 분획 2.46 g/100 g을 얻은 뒤 아세톤·에탄올·물 가압액체추출로 단계별 분획을 만들었고, 에탄올 분획의 수율(15.3 g/100 g)과 총페놀(148.4 mg GAE/g)이 가장 높았다[15]. 천연 공융용매와 초음파로 플라보노이드를 추출하는 조건도 연구되었다[28].\n\n"
"잎 추출물과 녹차 폴리페놀을 3:1로 섞으면 시험관 항산화 시험에서 상승 효과가 가장 컸다는 보고가 있어 혼합차 활용이 제안되었다[18]. 발효 소시지에 넣은 극성 추출물은 아스코르브산과 함께 쓸 때 약간의 산화 억제 효과를 보였으나 표준 향신료 혼합물보다 약했다[29]. 이 원료로 만든 국내 건강기능식품 생산실적은 확인하지 못함.")
add("genetics","유전·계통",
"중국 쿤밍 식물원 개체의 유전체는 2배체로 판정되었고, 유세포 분석으로 추정한 크기는 264.18 Mb, 염색체 수준 조립에서 249.23 Mb가 7개 의사염색체에 배치되었다[4]. 이 유전체에는 단백질 암호화 유전자 32,613개가 예측되었고, 늘어난 유전자군은 산화 스트레스·자외선·저온 반응과 관련되었다[4]. 다른 연구는 4배체 D. fruticosa(929.99 Mb)와 2배체 D. glabra(450.89 Mb)의 반수체 수준 유전체를 조립했다[5].\n\n"
"592개체를 다시 분석한 연구는 고지대 집단에서 근친교배로 쌓인 해로운 변이가 더 강하게 제거된 흔적을 찾았다[6]. 칭하이-티베트 고원 23개 집단 508개체의 엽록체 matK 서열로는 고원 내부가 빙하기 피난처였다고 추정했다[8]. 한 지역 안에도 배수성이 다른 개체가 섞여 있어 유전체 연구 시료의 배수성을 꼭 확인해야 한다[4, 7]. 국내 흰물싸리 개체의 배수성·염색체 수는 확인하지 못함.")
add("safety","안전성",
"식약처 「식품원료 목록」에서 흰물싸리는 잎만 쓸 수 있는 사용가능 원료다[1]. 사람에게 먹인 임상시험이나 공공기관의 독성·알레르기·섭취 주의 정보는 확인하지 못함.\n\n"
"동물·세포 결과는 사람에게 그대로 옮길 수 없다[23, 25, 27]. 러시아 연구에서 수용성 추출물은 사염화탄소로 만든 쥐 만성 간염 모델에서 간 효소(ALT)와 빌리루빈을 정상화했다[23]. 같은 계열의 수용성 추출물 제제를 쥐에 하루 40 mg/kg씩 1개월 먹인 연구는 놀람 반응을 줄였지만, 불안하지 않은 쥐에서 일시적인 감각운동 변화가 나타나 부작용 가능성을 언급했다[25]. 사람 정상 대장 세포 실험에서는 25–250 µg/mL 추출물이 근섬유모세포의 대사를 억제했다[27]. 잎 추출물의 항균 활성은 시험관에서 MIC 0.78–6.25 mg/mL 수준이었다[9]. 리투아니아산 잎 에탄올 추출물도 시험관에서 세균과 칸디다균에 항균 활성을 보였다[22]. 폴란드 연구에서 지상부(잎만이 아님)는 탄닌 167.3 ± 2.0 mg/g 건조중량을 함유했고 충치균 바이오필름 형성을 억제했다[20]. 지상부 물 추출물 9종을 함께 시험한 연구의 헬리코박터균 MIC 0.1/0.5 mg/mL는 여러 종을 묶은 결과라 이 종만의 값으로 볼 수 없다[21]. 이런 결과는 모두 시험관 수준이며 먹었을 때의 효과를 뜻하지 않는다[20–22].")
comp=[
 {"name":"Hyperoside","name_ko":"하이퍼로사이드","class":"플라보놀 배당체(퀘르세틴-3-O-갈락토사이드)","role":"marker","part":"잎","content_text":"잎 80% 아세톤 추출물 8.86 ± 0.08 mg/g(RP-HPLC, 칭하이 후주 시료; 정량한 6개 성분 중 최다)[9]; 잎 17.67 mg/g(초록, 기준 명시 없음)[12]","activity_ko":"잎의 주성분이며 (+)-카테킨·엘라그산과 함께 품질 평가 지표로 제안됨[12, 13]","source":[9,12,13]},
 {"name":"Catechin","name_ko":"(+)-카테킨","class":"플라반-3-올","role":"marker","part":"잎·꽃","content_text":"잎 추출물 0.60 ± 0.03 mg/g(RP-HPLC)[9]; 잎·꽃의 주요 페놀 성분(함량 수치는 초록에 없음)[13]","activity_ko":"항산화 활성과 상관을 보여 품질 지표로 제안됨[12, 13]","source":[9,12,13]},
 {"name":"Ellagic acid","name_ko":"엘라그산","class":"페놀산(엘라기타닌 가수분해물)","role":"marker","part":"잎","content_text":"잎 추출물 0.29 ± 0.01 mg/g(RP-HPLC)[9]; 잎 가압액체추출물에서 m/z 300.9987로 잠정 동정(정량 안 함)[15]","activity_ko":"잎에 많은 페놀 성분으로 품질 지표 후보[12]","source":[9,12,15]},
 {"name":"Rutin","name_ko":"루틴","class":"플라보놀 배당체","role":"bioactive","part":"잎","content_text":"잎 추출물 0.05 ± 0.00 mg/g(칭하이 시료)[9]; 중국 8개 지역 잎 0.11 ± 0.01–1.79 ± 0.01%(RP-HPLC, 원문 % 기준 명시 없음)[10]; 5개 주산지 0.18–0.81%(부위는 초록에 없음)[14]","activity_ko":"산지에 따라 함량 차이가 큼[10, 14]","source":[9,10,14]},
 {"name":"Quercetin","name_ko":"퀘르세틴","class":"플라보놀","role":"bioactive","part":"잎","content_text":"중국 8개 지역 잎 0.21 ± 0.01–1.85 ± 0.03%(RP-HPLC, 원문 % 기준 명시 없음)[10]","activity_ko":"HPLC 지문 분석의 기준 피크(머무름시간 11.68분)로 쓰임[10]; 노란 꽃잎 색의 원인 성분으로 분석됨[5]","source":[5,10]},
 {"name":"Kaempferol","name_ko":"켐페롤","class":"플라보놀","role":"bioactive","part":"잎","content_text":"중국 8개 지역 잎 0.022 ± 0.003–0.676 ± 0.02%(RP-HPLC, 원문 % 기준 명시 없음)[10]","activity_ko":"퀘르세틴과 함께 예전부터 이 종의 HPLC 지표로 쓰였다는 설명[10]","source":[10]},
 {"name":"Caffeic acid","name_ko":"카페산","class":"하이드록시신남산","role":"bioactive","part":"잎","content_text":"잎 추출물 0.19 ± 0.00 mg/g(RP-HPLC)[9]","activity_ko":"정량한 6개 페놀 성분 중 하나","source":[9]},
 {"name":"Ferulic acid","name_ko":"페룰산","class":"하이드록시신남산","role":"bioactive","part":"잎","content_text":"잎 추출물 0.02 ± 0.00 mg/g(RP-HPLC)[9]","activity_ko":"함량이 매우 낮은 미량 페놀산","source":[9]},
 {"name":"Theanine","name_ko":"테아닌","class":"유리 아미노산","role":"nutrient","part":"차(시판 민간차, 부위 세부는 초록에 없음)","content_text":"1.16 ± 0.81 mg/g(UHPLC)[17]","activity_ko":"차나무가 아닌 민간차에서 검출되어 주목됨; 카페인·테오브로민·테오필린은 이들 민간차에서 검출되지 않음[17]","source":[17]},
 {"name":"alpha-Linolenic acid","name_ko":"알파-리놀렌산","class":"오메가-3 다가불포화지방산","role":"nutrient","part":"잎(초임계 CO2 추출 지용성 분획)","content_text":"지방산 조성의 29.40%(GC-FID, 리투아니아 식물원 개화기 잎)[15]","activity_ko":"지용성 분획(2.46 g/100 g 건조중량)의 주요 지방산[15]","source":[15]},
 {"name":"Linoleic acid","name_ko":"리놀레산","class":"오메가-6 다가불포화지방산","role":"nutrient","part":"잎(초임계 CO2 추출 지용성 분획)","content_text":"지방산 조성의 14.94%(GC-FID)[15]","activity_ko":"불포화지방산이 전체 지방산의 약 70%[15]","source":[15]},
 {"name":"Oleic acid","name_ko":"올레산","class":"단일불포화지방산","role":"nutrient","part":"잎(초임계 CO2 추출 지용성 분획)","content_text":"지방산 조성의 5.79%(GC-FID)[15]","activity_ko":"지용성 분획의 구성 지방산","source":[15]},
 {"name":"Tormentic acid","name_ko":"토르멘트산","class":"오탄고리 트리테르페노이드","role":"bioactive","part":"잎","content_text":"잎 가압액체추출물에서 m/z 487.3431로 잠정 동정(정량 안 함)[15]","activity_ko":"UPLC-QTOF-MS로 추정한 트리테르페노이드; 표준품 대조 확인은 하지 않음[15]","source":[15]},
 {"name":"Methylene 6,8-bis(7-O-glucosyl)catechin","name_ko":"메틸렌 6,8-비스(7-O-글루코실)카테킨","class":"메틸렌 결합 플라반-3-올 이량체 배당체","role":"bioactive","part":"가지와 잎","content_text":"가지·잎에서 새 화합물로 분리(함량 수치는 초록에 없음)[16]","activity_ko":"함께 분리된 메틸렌 비스플라반-3-올류가 이 종에서 처음 보고됨[16]","source":[16]},
]
assays=[
 {"role":"literature","compound":"Hyperoside; (+)-Catechin; Rutin; Ellagic acid; Caffeic acid; Ferulic acid","compound_ko":"하이퍼로사이드·(+)-카테킨·루틴·엘라그산·카페산·페룰산","part":"잎(중국 칭하이 후주 북산 채집, 그늘 건조)","content":"하이퍼로사이드 8.86 ± 0.08 mg/g, (+)-카테킨 0.60 ± 0.03 mg/g, 엘라그산 0.29 ± 0.01 mg/g, 카페산 0.19 ± 0.00 mg/g, 루틴 0.05 ± 0.00 mg/g, 페룰산 0.02 ± 0.00 mg/g(합계 10.01 mg/g; 원문 '추출물 함량' mg/g, 건조 잎 기준인지 명시 없음)",
  "method":"RP-HPLC-UV(가변파장 검출기)",
  "conditions":{"instrument":"Agilent 1260 시리즈 액체크로마토그래프 + 가변파장 검출기","column":"SB-C18 역상, 4.6 × 250 mm, 5 µm","mobile_phase":"A: 물(0.2% 트라이플루오로아세트산), B: 메탄올(0.2% 트라이플루오로아세트산)","gradient":"B 5%(0분); 20%(0–10분); 25%(10–15분); 25%(15–20분); 30%(20–25분); 30%(25–35분); 35%(35–40분); 45%(40–50분); 100%(50–60분); 100%(60–65분)","flow":"0.8 mL/min","temp":"실온","detection":"UV 320·360 nm(머무름시간: 카테킨 17.96, 카페산 26.29, 페룰산 41.34, 하이퍼로사이드 51.09, 루틴 53.77, 엘라그산 56.61분)","injection":"20 µL","sample_prep":"그늘 건조 잎 가루 2 g + 80% 차가운 아세톤 50 mL, 4 °C 1시간 추출·여과, 3회 반복; 45 °C 감압 건조 후 메탄올에 녹여 −20 °C 보관","standard":"(+)-카테킨·카페산·페룰산·하이퍼로사이드·루틴·엘라그산 시판 표준품","linearity":"하이퍼로사이드 y = 66172x + 37.96(R² 0.9986); 카테킨 R² 0.9973; 루틴 R² 0.9964; 엘라그산 R² 0.9999; 카페산·페룰산 R² 0.9998","lod":"","loq":"","recovery":"평균 94.81 ± 0.66 – 105.95 ± 2.44%(하이퍼로사이드 105.72 ± 1.56%, n = 6)"},
  "rationale":"하이퍼로사이드는 이 종 잎에서 정량한 페놀 성분 중 가장 많아 근연종(P. glabra·P. parvifolia)과 구별하는 지문 피크로도 쓰였다. 전문(Methods)에서 조건을 옮겼고 검출·정량한계는 원문에 없다[9].",
  "source":[9],"url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC3840622/","source_kind":"paper"},
 {"role":"literature","compound":"Rutin; Quercetin; Kaempferol","compound_ko":"루틴·퀘르세틴·켐페롤","part":"성숙 잎(중국 8개 지역, 2014년 7월 채집, 40 °C 진공 건조)","content":"루틴 0.11 ± 0.01–1.79 ± 0.01%, 퀘르세틴 0.21 ± 0.01–1.85 ± 0.03%, 켐페롤 0.022 ± 0.003–0.676 ± 0.02%(8개 지역 범위, 원문 % 기준 명시 없음)",
  "method":"RP-HPLC-UV(가변파장 검출기) + HPLC 지문 분석",
  "conditions":{"instrument":"Agilent 1260 시리즈(4원 기울기 펌프, 가변파장 검출기)","column":"Agilent SB-C18 역상, 4.6 × 250 mm, 5 µm","mobile_phase":"A: 물(0.5% 아세트산), B: 메탄올(0.5% 아세트산)","gradient":"0–15분 B 25→35%; 15–30분 35→60%; 30–40분 60→100%; 40–45분 100% 유지","flow":"1 mL/min","temp":"실온","detection":"UV 360 nm(머무름시간: 루틴 6.24, 퀘르세틴 11.68, 켐페롤 31.57분)","injection":"20 µL","sample_prep":"잎 가루를 70% 에탄올, 45 °C, 2시간, 3회, 액고비 15:1로 추출; 40 °C 감압 농축; 시료액 1 mg/mL를 0.22 µm 막으로 여과","standard":"루틴·퀘르세틴·켐페롤(중국 국가 의약품·생물제품 검정기관 표준품)","linearity":"루틴 1.0–100.0 µg/mL(y = 59142.31x − 135.4, r 0.9998); 퀘르세틴 10.0–500.0 µg/mL(r 0.9999); 켐페롤 5.0–500.0 µg/mL(r 0.9997)","lod":"루틴 2.89, 퀘르세틴 1.87, 켐페롤 3.04 ng/mL(S/N = 3)","loq":"루틴 9.98, 퀘르세틴 8.14, 켐페롤 10.33 ng/mL(S/N = 10)","recovery":"루틴 99.85 ± 0.02%, 퀘르세틴 102.91 ± 0.01%, 켐페롤 96.36 ± 0.02%(n = 6)"},
  "rationale":"퀘르세틴·켐페롤은 예전부터 이 종의 HPLC 지표로 쓰였고, 이 연구는 루틴을 더해 정량하고 퀘르세틴 피크를 지문 분석의 기준 피크로 삼았다. 전문(Methods)에서 조건을 옮겼다[10].",
  "source":[10],"url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC4758616/","source_kind":"paper"},
]
d={"slug":"potentilla-fruticosa","name_ko":"흰물싸리","name_en":"Shrubby cinquefoil","scientific_name":"Potentilla fruticosa L. (syn. Dasiphora fruticosa (L.) Rydb.)",
 "aliases":["흰물싸리잎","은물싸리","Yellow gem","Shrubby cinquefoil","Dasiphora fruticosa","Dasiphora fruticosa var. coreana Nakai","Pentaphylloides fruticosa","금로매(진라오메이)"],
 "sections":sec,"compounds":comp,"markers":[],"assays":assays,"nutrients":[],"production":[],"world":[],"gi":[],"orgs":[],"sources":S}
Path(__file__).resolve().parents[1].joinpath("dossier.json").write_text(json.dumps(d,ensure_ascii=False,indent=1),encoding="utf-8")
for s in sec: print(s['key'],len(s['body']))
