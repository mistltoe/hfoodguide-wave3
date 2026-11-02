import json
A="2026-11-02"
def pm(n,title,doi,pmid,extra=""):
    return {"n":n,"title":f"{title} (PMID {pmid}{extra})","url":f"https://doi.org/{doi}" if doi else f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/","publisher":"PubMed","accessed":A}
S=[
{"n":1,"title":"식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 필리핀오렌지열매(Citrus nobilis Lour.), 영문명 'Dalandan', 사용가능, 사용가능부위: 열매 (로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json)","url":"https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020","publisher":"식품의약품안전처","accessed":"2026-10-13"},
{"n":2,"title":"식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 같은 속 대조 행: 감귤(Citrus unshiu / Citrus reticulata; 열매·열매껍질 사용가능), 광귤(Citrus aurantium L.; 열매 '지각' 제한적사용), 당귤나무(Citrus sinensis), 필리핀레몬열매(Citrus microcarpa, Calamansi), 여름밀감열매(Citrus natsudaidai; 제한적사용), 한라봉 (로컬 원자료 I1020_20261013.json)","url":"https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020","publisher":"식품의약품안전처","accessed":"2026-10-13"},
pm(3,"Hybrid origins of citrus varieties inferred from DNA marker analysis of nuclear and organelle genomes — PLoS One 2016;11(11):e0166969","10.1371/journal.pone.0166969","27902727",", PMC5130255, 전문 확인: King(A054) 세포질형 C12, 쿠넨보 계통과의 불일치 마커 수, King 을 부모로 하는 품종 표"),
pm(4,"Parental diagnosis of satsuma mandarin (Citrus unshiu Marc.) revealed by nuclear and cytoplasmic markers — Breed Sci 2016;66(5)","10.1270/jsbbs.16060","28163584",", 초록 확인"),
pm(5,"Distinguishing citrus varieties based on genetic and compositional analyses — PLoS One 2022;17(4):e0267007","10.1371/journal.pone.0267007","35436309",", PMC9015143, 전문 확인: 필리핀산 'Dalandan' 시료의 SSR·LC-QTOF/MS·GC-MS 결과; 전문 텍스트에서 시료별 학명 표기가 빠져 있어 논문이 붙인 학명은 확인하지 못함"),
pm(6,"HL-60 differentiating activity and flavonoid content of the readily extractable fraction prepared from citrus juices — J Agric Food Chem 1999;47(1):128-135","10.1021/jf9805101","10563860",", 초록 확인"),
pm(7,"Antiproliferative effects of the readily extractable fractions prepared from various citrus juices on several cancer cell lines — J Agric Food Chem 1999;47(7)","10.1021/jf9812228","10552518",", 초록 확인"),
pm(8,"Quantitative study of fruit flavonoids in citrus hybrids of King (C. nobilis) and Mukaku Kishu (C. kinokuni) — J Agric Food Chem 2001;49(8):3982-3986","10.1021/jf0100292","11513699",", 초록 확인"),
pm(9,"Effect of citrus flavonoids on HL-60 cell differentiation — Anticancer Res 1999;19(2A):1261-1269","","10368686",", 초록 확인"),
pm(10,"Antiproliferative activity of flavonoids on several cancer cell lines — Biosci Biotechnol Biochem 1999;63(5):896-899","10.1271/bbb.63.896","10380632",", 초록 확인"),
pm(11,"Inhibitory effect of flavonoids from citrus plants on Epstein-Barr virus activation and two-stage carcinogenesis of skin tumors — Cancer Lett 2000;154(1):101-105","10.1016/s0304-3835(00)00386-4","10799745",", 초록 확인"),
pm(12,"Relationship between structure and antiproliferative activity of polymethoxyflavones towards HL60 cells — Anticancer Res 2012;32(12):5239-5244","","23225422",", 초록 확인"),
pm(13,"Characterization of a caffeic acid 8-O-methyltransferase from citrus and its function in nobiletin biosynthesis — J Agric Food Chem 2022;70(2):543-553","10.1021/acs.jafc.1c06513","34964635",", 초록 확인"),
pm(14,"Genetic diversity among mandarins in fruit-quality traits — J Agric Food Chem 2014;62(21):4938-4946","10.1021/jf5002414","24828369",", 초록 확인"),
pm(15,"Diversity among mandarin varieties and natural sub-groups in aroma volatiles compositions — J Sci Food Agric 2016;96(1):57-65","10.1002/jsfa.7191","25824867",", 초록 확인"),
pm(16,"Diversity in sensory quality and determining factors influencing mandarin flavor liking — J Food Sci 2015","10.1111/1750-3841.12742","25559381",", 초록 확인"),
pm(17,"Effective use of neonicotinoids for protection of citrus seedlings from invasion by Diaphorina citri (Hemiptera: Psyllidae) — J Econ Entomol 2010","10.1603/ec09218","20214377",", 초록 확인"),
pm(18,"Unreliable pesticide control of the vector psyllid Diaphorina citri for the reduction of microorganism disease transmission — J Environ Sci Health B 2010;45(5):466-472","10.1080/03601231003800263","20512737",", 초록 확인"),
pm(19,"Two previously unknown Phytophthora species associated with brown rot of pomelo (Citrus grandis) fruits in Vietnam — PLoS One 2017;12(2):e0172085","10.1371/journal.pone.0172085","28208159",", 초록 확인"),
pm(20,"Identification of pathogens causing anthracnose on king oranges (Citrus nobilis var. typica Hassk) — Pak J Biol Sci 2022;25(2):137-143","10.3923/pjbs.2022.137.143","35234002",", 초록 확인"),
pm(21,"Utilization of biomass waste from citrus fruits for the production of essential oils — Foods 2026;15(8):1446","10.3390/foods15081446","42073335",", PMC13115153, 전문 확인: 에콰도르 볼리바르주산 Citrus nobilis Loureiro(CNL) 껍질; 결론 절에 이 연구와 무관한 사과 건조 내용이 실려 있음"),
pm(22,"Evaluation of adding natural gum to pectin extracted from Ecuadorian citrus peels as an eco-friendly corrosion inhibitor for carbon steel — Molecules 2022;27(7):2111","10.3390/molecules27072111","35408511",", 초록 확인"),
pm(23,"Volatile constituents of wild citrus Mangshanyegan (Citrus nobilis Lauriro) peel oil — J Agric Food Chem 2012","10.1021/jf2039197","22352344",", 초록 확인"),
pm(24,"Chemotaxonomic study of Citrus, Poncirus and Fortunella genotypes based on peel oil volatile compounds — deciphering the genetic origin of Mangshanyegan — PLoS One 2013;8(3):e58411","10.1371/journal.pone.0058411","23516475",", 초록 확인"),
pm(25,"Evaluation of aroma-active compounds in Pontianak orange peel oil (Citrus nobilis Lour. var. microcarpa Hassk.) — J Agric Food Chem 2009","10.1021/jf801070r","19061307",", 초록 확인"),
pm(26,"The effect of drying methods on the physicochemical and antioxidant properties of Bintangor orange (Citrus nobilis) powders — Acta Sci Pol Technol Aliment 2022;21(1):111-122","10.17306/J.AFS.0901","35174693",", 초록 확인"),
pm(27,"Pattern of phenolic content, antioxidant activity and senescence-related enzymes in granulated vs non-granulated juice-sacs of 'Kinnow' mandarin (Citrus nobilis x C. deliciosa) — J Food Sci Technol 2016;53(3):1525-1530","10.1007/s13197-015-2112-9","27570277",", 초록 확인"),
pm(28,"Genetic background of Citrus nobilis Lour. 'Gonggan' based on the chloroplast trnL gene — Genet Mol Res 2013","10.4238/2013.January.30.7","23408451",", 초록 확인"),
pm(29,"Nobiletin alleviates cerebral ischemic-reperfusion injury via MAPK signaling pathway — Am J Transl Res 2019;11(9):5967-5977","","31632564",", PMC6789284, 초록 확인"),
pm(30,"Characterization of Citrus nobilis peel methanolic extract for antioxidant, antimicrobial, and anti-inflammatory activity — Molecules 2021;26(14):4310","10.3390/molecules26144310","34299584",", PMC8306028, 전문 확인: 시료는 인도 펀자브산 'Daisy' 품종"),
{"n":31,"title":"LOTUS 천연물 출현 데이터베이스 — Citrus nobilis 보고 성분(citrunobin, natsudaidain 등; hfoodguide card.json 의 지표성분 후보 경유, 원 논문은 확인하지 못함)","url":"https://lotus.naturalproducts.net/","publisher":"LOTUS (Wikidata 기반 천연물 DB)","accessed":A},
]
sec=[
("overview","한눈에 보기",
"필리핀오렌지(Citrus nobilis Lour.)는 운향과 귤속의 과일로, 식품의약품안전처 「식품원료 목록」에는 '필리핀오렌지열매' 한 원료명으로 올라 있고 영문명은 'Dalandan'으로 적혀 있다[1]. 학계에서는 같은 학명을 'King' 만다린(킹오렌지)에 붙여 쓰며, 이스라엘 연구진은 만다린의 자연 아군 7개 가운데 하나로 'King mandarin(C. nobilis Loureiro)'을 따로 구분했다[14][16]. 국문명 '필리핀오렌지'와 학명의 대응은 식약처 목록 원자료로만 확인했고, 국가표준식물목록 국명은 확인하지 못함.\n\n"
"식품원료로서의 지위는 '사용가능'이며 사용 조건은 '사용가능부위 : 열매'이다[1]. 같은 목록의 감귤(C. unshiu/C. reticulata)이 열매껍질(진피·청피)을 사용 부위에 따로 적은 것과 달리, 이 원료는 '열매'만 적혀 있다[1][2]. 영문명 'Dalandan'으로 팔리는 필리핀 과일 시료는 SSR 분석에서 만다린 쪽에 가깝게 묶였지만, 그 논문이 시료에 붙인 학명은 확인하지 못함[5].\n\n"
"'King' 과즙에서는 노빌레틴·탄게레틴·나츠다이다인·헵타메톡시플라본 같은 폴리메톡시플라본이 다른 귤류보다 많이 검출되었다[6]. 이 성분들의 효과는 세포·동물 실험 결과이며, 이 종을 먹인 사람 시험은 확인하지 못함."),
("history","역사와 전통적 이용",
"학명의 명명자 'Lour.'는 식약처 목록 학명란에 그대로 적혀 있다[1]. 베트남 메콩 삼각주에서는 'King' 만다린(C. nobilis)을 새로 심은 과수원 다섯 곳이 감귤 그린닝병(황룡병) 매개충 연구의 대상이 되었다[17]. 베트남 빈롱(Vinh Long) 지역의 킹오렌지(C. nobilis var. typica Hassk.) 과수원에서는 탄저병이 과일 수량과 품질을 크게 떨어뜨리는 주요 원인으로 보고되었다[20].\n\n"
"'King'은 육종 부모로 널리 쓰였다[3]. 일본 연구에서 'Kinnow'는 King × 윌로우리프 만다린, 'Kara'는 온주밀감 × King, '농 6호'는 King × 기슈(Kishu)에서 나온 품종으로 DNA 부모 검정과 맞았다[3]. 'Kinnow'는 미국 캘리포니아에서 육성되었으나 그곳에서는 성공하지 못했고, 인도·파키스탄·방글라데시의 감귤 산업을 바꾸어 놓았다고 기술된다[27].\n\n"
"일본에서 '쿠넨보(Kunenbo)'로 불리는 계통은 다나카 분류에서 C. nobilis var. kunep로 다루어지며, 쿠넨보형 만다린이 온주밀감의 부모 후보로 제시되었다[4]. 다만 'King' 자체는 쿠넨보 계통들과 DNA 마커가 크게 달라 서로 다른 기원으로 판정되었다[3]. 필리핀에서 'Dalandan'을 먹어 온 전통 이용과 한국에서의 소비 역사는 확인하지 못함."),
("biology","식물학적 특징",
"필리핀오렌지는 운향과 귤속의 과수이며, 식약처 목록은 이 종을 '식물'로 분류하고 열매만 식용 부위로 정했다[1]. 'King'은 일본 국립 과수연구소 보존 계통(A054)으로 분석되었고, 엽록체 표지로 본 세포질형은 만다린형(C12)이었다[3]. 이스라엘의 만다린 46품종 비교에서 'King'은 독립된 자연 아군으로 다뤄졌으며, 크기·모양·색·껍질 두께·씨 수·익는 시기·껍질 벗기기 등 과실 특성이 아군마다 크게 달랐다[14].\n\n"
"향기 성분을 보면 'King'은 탄골·탄젤로와 함께 휘발 성분 종류와 양이 많고, 특히 세스퀴테르펜과 에스테르가 많아 보통 만다린·클레멘타인·온주밀감과 구별되었다[15]. 필리핀산 'Dalandan' 시료는 평균 무게 77 g, 상업적 수확기에도 연한 녹색 껍질이었다[5]. 그 껍질 정유에서는 리모넨이 휘발 성분의 약 86%였고, 만다린과 오렌지를 가르는 지표인 α-시넨살이 일곱 시료 가운데 가장 많았다(약 70 µg/mL)[5].\n\n"
"잎·꽃·열매 모양을 적은 공식 식물지 기재는 확인하지 못함."),
("related_species","가까운 종과 혼동 주의",
"같은 학명 C. nobilis가 나라마다 다른 과일에 쓰여 혼동이 크다[23][25][26][28]. 중국의 야생 만다린 '망산예간(Mangshanyegan)'은 논문에서 'Citrus nobilis Lauriro'로 적혔지만 껍질 정유가 리모넨 85.75%·β-미르센 10.89%로 이루어진 별개 야생형이다[23]. 같은 연구진은 망산예간이 유전적으로는 만다린이지만 향 성분은 포멜로와 비슷하다고 보고했다[24]. 인도네시아 '폰티아낙 오렌지'는 C. nobilis var. microcarpa, 말레이시아 '빈탕고르 오렌지'와 중국 '공간(Gonggan)'도 C. nobilis로 적힌다[25][26][28].\n\n"
"'Kinnow'(C. nobilis × C. deliciosa)는 King 의 잡종 품종이므로 그 과즙·과수 연구 수치는 이 종의 값으로 옮기지 않았다[27][3]. 인도 펀자브산 'Daisy' 품종 껍질을 C. nobilis로 적은 추출물 연구도 있으나, 품종 정체를 확인할 수 없어 수치를 쓰지 않았다[30].\n\n"
"식약처 목록에는 감귤(C. unshiu/C. reticulata), 광귤(C. aurantium, 열매 '지각' 제한적사용), 당귤나무(C. sinensis), 필리핀레몬(C. microcarpa, 'Calamansi')이 각각 다른 원료로 올라 있다[2]. 필리핀오렌지의 영문명 'Dalandan'이 어느 종을 가리키는지 필리핀 공식 자료로는 확인하지 못함. 이름이 비슷한 필리핀레몬(칼라만시)이나 제한적사용 원료인 광귤과 섞지 않아야 한다[2]."),
("cultivation","재배와 생산",
"베트남 메콩 삼각주의 새 King 만다린 과수원 다섯 곳에서는 묘목을 심은 뒤 2주 만에 아시아감귤나무이(Diaphorina citri)가 나타났고, 두 달 동안 나무의 2~60%가 감염되었다[17]. 연구진은 묘목을 심기 전에 침투성 살충제를 처리하면 이 기간의 위험을 크게 줄일 수 있다고 보고했다[17]. 다 자란 나무에서는 잎 살포·줄기 주입 모두 약 1개월 동안 50~70% 수준의 방제에 그쳐 기대보다 효과가 낮았다[18].\n\n"
"메콩 삼각주에서는 볼카메리아나 레몬 대목에 접목한 'King' 만다린의 잔뿌리에서도 새로운 역병균(Phytophthora) 분리주가 나왔다[19]. 빈롱 지역 킹오렌지 열매의 탄저병은 Colletotrichum gloeosporioides 로 동정되었다[20].\n\n"
"한국 내 재배·생산 통계는 확인하지 못함. 세계 생산량 통계(FAOSTAT 등)도 확인하지 못함."),
("processing","가공과 이용",
"에콰도르 볼리바르주 감귤 10품종의 껍질 정유를 비교한 연구에서 C. nobilis Loureiro 껍질은 정유 수율이 가장 높았고(2.91%), 정유의 리모넨 비율이 92.98%, γ-테르피넨이 2.47%였다[21]. 이 논문은 결론 절에 연구와 무관한 사과 건조 내용이 실려 있어 수치를 인용할 때 본문 결과 절의 값만 썼다[21]. 같은 에콰도르산 King 만다린 껍질에서는 pH 1, 85 °C, 2시간 조건에서 펙틴 수율 38.10%를 얻었다[22].\n\n"
"'King' 과즙은 HP-20 수지에 흡착시킨 뒤 에탄올·아세톤으로 녹여 낸 '쉽게 추출되는 분획'으로 만들어 플라보노이드 배당체를 걷어 내고 분석했다[6][7]. 말레이시아 빈탕고르 오렌지(C. nobilis로 표기) 퓨레를 다섯 가지로 건조한 실험에서는 동결건조 분말이 비타민 C 18.31 mg/g, 총 카로티노이드 91.32 µg/g으로 가장 많이 남았다[26].\n\n"
"한국에서 필리핀오렌지열매를 원료로 한 제품 생산실적은 확인하지 못함."),
("genetics","유전 정보와 종 판별",
"일본 국립 과수연구소 계통의 DNA 마커 분석에서 'King'(A054)은 쿠넨보 A·쿠넨보 B·트우쿠니와 각각 99·110·107개 마커가 맞지 않아 서로 다른 기원으로 판정되었다[3]. 같은 연구에서 'King'의 세포질형은 만다린형(C12)이었고, 쿠넨보 A는 스위트오렌지형(C07)이었다[3]. 'Kinnow'·'Kara'·'Encore'·'Honey'·'농 6호'의 부모로 King 이 확인되었다[3].\n\n"
"필리핀산 'Dalandan' 시료는 16개 SSR 마커로 본 계통수에서 만다린 무리 가까이에 놓였고, 현지에서 오렌지로 불리지만 유전적으로는 만다린에 더 가깝다고 결론지어졌다[5]. 중국 '공간'(C. nobilis 'Gonggan')은 엽록체 trnL 유전자 서열 변이로 다른 귤속 9종과 함께 계통 분석되었다[28]. King × 무카쿠기슈 잡종 24개체 중 2개체(G-155, G-156)는 부모보다 나츠다이다인이 많았고, 나머지는 부모의 중간 성질이었다[8]. King 계통 잡종 '농 6호'는 노빌레틴이 많고, 노빌레틴 생합성 효소 유전자 CitOMT2 발현이 높았다[13]."),
("safety","안전성",
"식약처 「식품원료 목록」에서 필리핀오렌지열매는 '사용가능' 원료이고, 사용 부위는 열매로 정해져 있다[1]. 같은 속의 광귤(C. aurantium) 열매는 '지각'으로 제한적사용, 여름밀감 열매도 제한적사용이므로, 원료 표시의 학명을 확인해야 한다[2]. 이 종에 대한 알레르기·독성 성분에 관한 공공기관 안전 정보는 확인하지 못함.\n\n"
"푸라노쿠마린인 베르가프텐·시트롭텐·베르가모틴은 필리핀산 'Dalandan' 껍질과 과즙에서 검출되지 않았고, 같은 연구의 라임 두 시료에서는 검출되었다[5]. 다만 이는 시료 한 산지의 결과이며, 이 종의 약물 상호작용을 직접 시험한 연구는 확인하지 못함.\n\n"
"King 과즙 분획이 암세포 증식을 억제하고 정상 세포에는 덜 독성이었다는 결과는 시험관 세포 실험이다[7]. 킹오렌지 껍질에서 분리한 폴리메톡시플라본도 HL60 백혈병 세포의 구조-활성 관계 연구에 쓰였을 뿐 사람 효과를 보인 것은 아니다[12]. 노빌레틴의 뇌허혈 보호 효과는 쥐 실험 결과이고, 섭취 효과로 옮길 수 없다[29]. 베트남 재배지에서는 매개충 방제를 위해 네오니코티노이드 계열 침투성 살충제를 쓰지만[17][18], 열매의 잔류 농약 자료는 확인하지 못함."),
]
comp=[
{"name":"Nobiletin","name_ko":"노빌레틴","class":"폴리메톡시플라본","role":"marker","part":"과즙·열매껍질","content_text":"King 과즙의 '쉽게 추출되는 분획'에서 HL-60 분화 활성 성분으로 분리, 다른 귤류보다 많음(수치는 초록에 없음)[6]; 필리핀산 'Dalandan' 껍질 메탄올 추출물 4601.533 ± 48.065 µg/mL[5]","activity_ko":"HL-60 세포 분화 유도(세포)[9]; 쥐 뇌허혈-재관류 손상 완화(동물)[29]","source":[5,6,9,29]},
{"name":"Tangeretin","name_ko":"탄게레틴","class":"폴리메톡시플라본","role":"marker","part":"과즙·열매껍질","content_text":"King 과즙 분획에서 분리[6]; 'Dalandan' 껍질 추출물 1374.067 ± 12.055 µg/mL(7개 시료 중 최고)[5]","activity_ko":"HL-60 세포 분화 유도·암세포 증식 억제(세포)[9][10]","source":[5,6,9,10]},
{"name":"Natsudaidain","name_ko":"나츠다이다인","class":"폴리메톡시플라본(3-하이드록시)","role":"bioactive","part":"과즙·가식부","content_text":"King 과즙 분획에서 분리[6]; King × 무카쿠기슈 잡종 G-155·G-156 가식부에서 부모보다 많음(수치는 초록에 없음)[8]","activity_ko":"시험한 감귤 플라보노이드 27종 중 HL-60 분화 유도 1위(세포)[9]; 암세포 증식 억제(세포)[10]","source":[6,8,9,10]},
{"name":"3,3',4',5,6,7,8-Heptamethoxyflavone","name_ko":"3,3',4',5,6,7,8-헵타메톡시플라본","class":"폴리메톡시플라본","role":"bioactive","part":"과즙","content_text":"King 과즙 분획에서 분리(함량은 초록에 없음)[6]","activity_ko":"감귤 껍질 유래 시료로 EBV-EA 활성화 억제(시험관)·생쥐 피부 2단계 발암 억제(동물)[11] — 이 종 껍질에서 얻은 시료인지는 확인하지 못함","source":[6,11]},
{"name":"Sinensetin","name_ko":"시넨세틴","class":"폴리메톡시플라본","role":"bioactive","part":"열매껍질","content_text":"'Dalandan' 껍질 추출물 31.867 ± 0.147 µg/mL(7개 시료 중 최저)[5]","activity_ko":"확인하지 못함","source":[5]},
{"name":"Hesperidin","name_ko":"헤스페리딘","class":"플라바논 배당체","role":"nutrient","part":"열매껍질","content_text":"'Dalandan' 껍질 추출물 252.463 ± 8.734 µg/mL[5]","activity_ko":"이 종에서의 활성 연구는 확인하지 못함","source":[5]},
{"name":"Narirutin","name_ko":"나리루틴","class":"플라바논 배당체","role":"bioactive","part":"열매껍질","content_text":"'Dalandan' 껍질 추출물 184.603 ± 15.461 µg/mL[5]","activity_ko":"확인하지 못함","source":[5]},
{"name":"Neohesperidin","name_ko":"네오헤스페리딘","class":"플라바논 배당체","role":"bioactive","part":"열매껍질","content_text":"'Dalandan' 껍질 추출물 26.783 ± 0.476 µg/mL(7개 시료 중 최고)[5]","activity_ko":"확인하지 못함","source":[5]},
{"name":"Limonin","name_ko":"리모닌","class":"리모노이드","role":"bioactive","part":"열매껍질","content_text":"'Dalandan' 껍질 추출물 96.883 ± 7.278 µg/mL; 오바쿠논 3.051 ± 0.083 µg/mL은 만다린 잡종 3품종 껍질에서만 검출[5]","activity_ko":"확인하지 못함","source":[5]},
{"name":"Limonene","name_ko":"리모넨","class":"모노테르펜","role":"bioactive","part":"열매껍질(정유)","content_text":"에콰도르산 C. nobilis 껍질 정유의 92.98%[21]; 'Dalandan' 껍질 디클로로메탄 추출 휘발 성분의 약 86%(8285.298 ± 774.947 µg/mL)[5]","activity_ko":"이 종 정유의 생리활성 시험은 확인하지 못함","source":[5,21]},
{"name":"gamma-Terpinene","name_ko":"γ-테르피넨","class":"모노테르펜","role":"bioactive","part":"열매껍질(정유)","content_text":"에콰도르산 C. nobilis 껍질 정유의 2.47%[21]","activity_ko":"확인하지 못함","source":[21]},
{"name":"alpha-Sinensal","name_ko":"α-시넨살","class":"세스퀴테르펜 알데하이드","role":"marker","part":"열매껍질(휘발 성분)","content_text":"'Dalandan' 껍질 약 70 µg/mL(7개 시료 중 최고)[5]","activity_ko":"만다린(≥0.7%)과 오렌지(<0.05%)를 가르는 향 지표로 쓰임[5]","source":[5]},
{"name":"Citrunobin","name_ko":"시트루노빈","class":"아크리돈 알칼로이드로 추정(원 논문 확인 못함)","role":"marker","part":"확인하지 못함","content_text":"LOTUS 에 C. nobilis 보고 성분으로 1건 등재, 함량은 확인하지 못함[31]","activity_ko":"확인하지 못함","source":[31]},
]
assays=[
{"role":"literature","compound":"Nobiletin","compound_ko":"노빌레틴(탄게레틴·시넨세틴·헤스페리딘·나리루틴 등 39성분 동시 정량)","part":"열매껍질(필리핀산 'Dalandan' 시료)","content":"껍질 메탄올 추출물 중 노빌레틴 4601.533 ± 48.065 µg/mL, 탄게레틴 1374.067 ± 12.055 µg/mL, 시넨세틴 31.867 ± 0.147 µg/mL[5]",
 "method":"LC-QTOF/MS(All-ion MS/MS)","conditions":{"instrument":"Agilent 1290 Infinity II LC + 6550 iFunnel Q-TOF","column":"","mobile_phase":"A: 0.1% 포름산 수용액, B: 아세토니트릴(0.1% 포름산)","gradient":"0–2분 ACN 5%, 2–12분 5→25%, 12–22분 25→95%, 22–25분 95%, 이후 5%로 5분 재평형","flow":"","temp":"40 °C","detection":"Q-TOF MS, All-ion MS/MS 모드(조건은 선행 논문 준용)","injection":"1 µL","sample_prep":"껍질(알베도 제거) 100.00 g 을 LC-MS 등급 메탄올 200.0 mL로 3시간 추출, 무수황산나트륨 40.0 g 으로 탈수 후 여과·회전증발 농축; 생물학적 반복 3회","standard":"순도 95% 이상 표준품(노빌레틴·탄게레틴·시넨세틴 등)","linearity":"성분별 선형 범위 안 5점 이상 검량선","lod":"","loq":"","recovery":""},
 "rationale":"폴리메톡시플라본(특히 노빌레틴·탄게레틴)이 이 시료를 다른 만다린 잡종과 구별하는 지표로 제시되었다; 칼럼·유속은 선행 논문 준용이라 전문에 없고, 이 시료가 C. nobilis 로 동정되었는지는 확인하지 못함[5]","source":[5],"url":"https://doi.org/10.1371/journal.pone.0267007","source_kind":"paper"},
{"role":"literature","compound":"Limonene","compound_ko":"리모넨(γ-테르피넨 등 정유 조성)","part":"열매껍질 정유(에콰도르산 C. nobilis Loureiro)","content":"정유 중 리모넨 92.98%, γ-테르피넨 2.47%(면적 %)[21]",
 "method":"GC-MS","conditions":{"instrument":"Thermo TRACE 1300 GC + ISQ 7000 단일 사중극자 MS","column":"DB-5MS, 30 m × 0.25 mm, 0.25 µm","mobile_phase":"","gradient":"오븐 50 °C → 230 °C, 3 °C/min(총 66분)","flow":"","temp":"주입구 230 °C","detection":"EI-MS, NIST 라이브러리 대조(유사도 80% 초과)와 n-알케인 머무름 지수","injection":"1 µL, 분할 주입","sample_prep":"껍질을 물·0.7% 탄산수소나트륨과 8–12시간 침지 후 분별증류(78–85 °C, 120분); 정유 3 µL 에 노난 표준 용액(사이클로헥산) 1 mL 첨가","standard":"노난(내부 기준)","linearity":"","lod":"","loq":"","recovery":""},
 "rationale":"리모넨이 모든 감귤 정유의 주성분이어서 정유 품질 지표로 쓰였다; 전문에서 조건을 옮겼으나 결론 절이 다른 연구 내용으로 잘못 실려 있어 해석에 주의[21]","source":[21],"url":"https://doi.org/10.3390/foods15081446","source_kind":"paper"},
{"role":"literature","compound":"Natsudaidain","compound_ko":"나츠다이다인(노빌레틴·탄게레틴·헵타메톡시플라본과 함께)","part":"과즙(King)","content":"King 과즙에 이 폴리메톡시플라본들이 시험한 귤류 과즙 가운데 많이 들어 있음(수치는 초록에 없음)[6]",
 "method":"역상 HPLC","conditions":{},
 "rationale":"King 과즙의 HL-60 분화 활성 성분으로 분리·동정된 폴리메톡시플라본으로, 34종 과즙 비교에서 King 의 특징 성분이었다; 전문 확인 못함[6]","source":[6],"url":"https://doi.org/10.1021/jf9805101","source_kind":"paper"},
]
d={"slug":"citrus-nobilis","name_ko":"필리핀오렌지","name_en":"King mandarin (King orange); 식약처 목록 영문명 Dalandan","scientific_name":"Citrus nobilis Lour.",
"aliases":["필리핀오렌지열매","킹만다린","킹오렌지","Dalandan","King mandarin","King orange","Citrus × nobilis"],
"sections":[{"key":k,"title":t,"body":b} for k,t,b in sec],
"compounds":comp,"markers":[],"assays":assays,"nutrients":[],"production":[],"world":[],"gi":[],"orgs":[],"sources":S}
json.dump(d,open('/home/user/hfoodguide-wave3/docs/materials/citrus-nobilis/dossier.json','w'),ensure_ascii=False,indent=1)
for k,t,b in sec: print(k,len(b))
