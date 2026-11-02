import json, pathlib
HERE = pathlib.Path(__file__).resolve().parent.parent
A = "2026-11-02"
def pm(n, title, doi, pmid, note):
    url = f"https://doi.org/{doi}" if doi else f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
    return {"n": n, "title": f"{title} (PMID {pmid}, {note})", "url": url, "publisher": "PubMed", "accessed": A}
S = [
 {"n": 1, "title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 루로열매·루로페이스트(Solanum quitoense, Lulo, Naranjilla) 사용가능·사용가능부위: 열매 (로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json)", "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
 pm(2, "Nutrients, Phytochemicals, and In Vitro Antioxidant and Antimicrobial Activities of Lulo (Solanum quitoense Lam.) Fruit Pulp, Peel, and Seeds — Foods 2025;14(12):2083", "10.3390/foods14122083", "40565691", "PMC12191578, 전문 확인"),
 pm(3, "Phytochemical Characterisation of Naranjilla (Solanum quitoense Lam.) Segregants from Interspecific Crosses Within Section Lasiocarpa — Molecules 2026;31(13):2217", "10.3390/molecules31132217", "42451587", "PMC13362583, 전문 확인"),
 pm(4, "Genetic Assessment in the Andean Tropical Fruits Solanum quitoense Lam. and Solanum betaceum Cav.: Efforts Towards a Molecular Breeding Approach — Plants (Basel) 2025;14(6):874", "10.3390/plants14060874", "40265758", "PMC11944818, 전문 확인"),
 pm(5, "Foliar brassinosteroid analogue (DI-31) sprays increase drought tolerance by improving plant growth and photosynthetic efficiency in lulo plants — Heliyon 2022;8(2):e08977", "10.1016/j.heliyon.2022.e08977", "35243095", "PMC8873547, 전문 확인"),
 pm(6, "Identifying carotenoids and phenolic compounds in naranjilla (Solanum quitoense Lam. var. Puyo hybrid), an Andean fruit — J Agric Food Chem 2008;56(24):11890-11899", "10.1021/jf801515p", "19053383", "초록 확인"),
 pm(7, "Chemical characterization, antioxidant properties, and volatile constituents of naranjilla (Solanum quitoense Lam.) cultivated in Costa Rica — Arch Latinoam Nutr 2009;59(1):88-94", None, "19480350", "초록 확인"),
 pm(8, "Spermidine Derivatives in Lulo (Solanum quitoense Lam.) Fruit: Sensory (Taste) versus Biofunctional (ACE-Inhibition) Properties — J Agric Food Chem 2016;64(26):5375-5383", "10.1021/acs.jafc.6b01631", "27292771", "초록 확인"),
 pm(9, "Chemical and sensory comparison of fresh and dried lulo (Solanum quitoense Lam.) fruit aroma — Food Chem 2015;169:85-91", "10.1016/j.foodchem.2014.07.111", "25236202", "초록 확인"),
 pm(10, "Identification of volatile compound markers during the ripening and senescence of lulo (Solanum quitoense Lam.) — J Food Sci Technol 2018;55(1):437-442", "10.1007/s13197-017-2924-x", "29358838", "초록 확인"),
 pm(11, "C13-Norisoprenoid glucoconjugates from lulo (Solanum quitoense L.) leaves — J Agric Food Chem 1999;47(4):1641-1645", "10.1021/jf9807364", "10564031", "초록 확인"),
 pm(12, "Specialized Metabolism in a Nonmodel Nightshade: Trichome Acylinositol Biosynthesis — Plant Physiol 2020;183(3):915-924", "10.1104/pp.20.00276", "32354879", "초록 확인"),
 pm(13, "Identification of BAHD acyltransferases associated with acylinositol biosynthesis in Solanum quitoense (naranjilla) — Plant Direct 2022;6(6):e415", "10.1002/pld3.415", "35774622", "초록 확인"),
 pm(14, "Characterization of a New Tymovirus Causing Stunting and Chlorotic Mosaic in Naranjilla (Solanum quitoense) — Plant Dis 2018;102(5):911-918", "10.1094/PDIS-10-17-1534-RE", "30673388", "초록 확인"),
 pm(15, "A New Tymovirus Isolated From Solanum quitoense: Characterization and Prevalence in Two Solanaceous Crops in Ecuador — Plant Dis 2019;103(9):2246-2251", "10.1094/PDIS-01-19-0113-RE", "31287777", "초록 확인"),
 pm(16, "Genitalic Differentiations in Neoleucinodes elegantalis (Lepidoptera: Crambidae) Associated with Solanaceae Crops in Ecuador — Insects 2017;8(3):91", "10.3390/insects8030091", "28858224", "초록 확인"),
 pm(17, "Application of Mycorrhiza and Soil from a Permaculture System Improved Phosphorus Acquisition in Naranjilla — Front Plant Sci 2017;8:1263", "10.3389/fpls.2017.01263", "28769964", "초록 확인"),
 pm(18, "Micropropagation of Solanum quitoense var. quitoense by apical bud, petiole and hypocotyl culture — Plant Biotechnol (Tokyo) 2019;36(2):91-97", "10.5511/plantbiotechnology.19.0317a", "31768109", "초록 확인"),
 pm(19, "Heritability of yield and fruit characteristics in Solanum quitoense Lam. — Braz J Biol 2024;84:e285691", "10.1590/1519-6984.285691", "39292140", "초록 확인"),
 pm(20, "Genetic variation in the Solanaceae fruit bearing species lulo and tree tomato revealed by Conserved Ortholog (COSII) markers — Genet Mol Biol 2010;33(2):271-278", "10.1590/S1415-47572010005000016", "21637482", "초록 확인"),
 pm(21, "Preliminary assessment of COSII gene diversity in lulo and a relative species: initial identification of genes potentially associated with domestication — Gene 2010;458(1-2):27-36", "10.1016/j.gene.2010.03.005", "20302924", "초록 확인"),
 pm(22, "Characterization of Powdered Lulo (Solanum quitoense) Bagasse as a Functional Food Ingredient — Foods 2020;9(6):723", "10.3390/foods9060723", "32498370", "초록 확인"),
 pm(23, "Potential Use of Vacuum Impregnation and High-Pressure Homogenization to Obtain Functional Products from Lulo Fruit (Solanum quitoense Lam.) — Foods 2021;10(4):817", "10.3390/foods10040817", "33918871", "초록 확인"),
 pm(24, "Sensory Characterization and Acceptability of a New Lulo (Solanum quitoense Lam.) Powder-Based Soluble Beverage Using Rapid Evaluation Techniques with Consumers — Foods 2022;11(19):3129", "10.3390/foods11193129", "36230204", "초록 확인"),
 pm(25, "Kinetic Modeling of Vitamin C Degradation for Predicting Shelf Life in Tropical Juices Made from Camu Camu and Naranjilla Under Accelerated Storage Conditions — Foods 2026;15(10):1722", "10.3390/foods15101722", "42195926", "초록 확인"),
 pm(26, "Determination of pesticides in dried minor tropical fruits from Colombia using the QuEChERS method-gas chromatography-tandem mass spectrometry — J Sep Sci 2020;43(5):929-935", "10.1002/jssc.201900698", "31833186", "초록 확인"),
 pm(27, "High-Performance Liquid Chromatography-Mass Spectrometry Analysis of Glycoalkaloids from Underexploited Solanum Species and Their Acetylcholinesterase Inhibition Activity — Plants (Basel) 2022;11(3):269", "10.3390/plants11030269", "35161249", "PMC8839269, 전문 확인; 어린 식물의 잎·줄기·뿌리만 분석"),
 pm(28, "Media preferences, micro-morphometric analysis, and cardinal growth temperature determination for Phytophthora infestans sensu lato isolated from different hosts in Colombia — Braz J Biol 2020;80(1):167-179", "10.1590/1519-6984.206460", "31017243", "초록 확인"),
 pm(29, "Native Colombian Fruits and Their by-Products: Phenolic Profile, Antioxidant Activity and Hypoglycaemic Potential — Foods 2019;8(3):89", "10.3390/foods8030089", "30832443", "초록 확인"),
 pm(30, "Edible Fruits from the Ecuadorian Amazon: Ethnobotany, Physicochemical Characteristics, and Bioactive Components — Plants (Basel) 2023;12(20):3635", "10.3390/plants12203635", "37896098", "초록 확인"),
 pm(31, "Potato Virus Y (PVY) Isolates from Solanum betaceum Represent Three Novel Recombinants Within the PVYN Strain Group and Are Unable to Systemically Spread in Potato — Phytopathology 2020;110(9):1588-1596", "10.1094/PHYTO-04-20-0111-R", "32370660", "초록 확인"),
 pm(32, "Diversity and plant growth-promoting functions of diazotrophic/N-scavenging bacteria isolated from the soils and rhizospheres of two species of Solanum — PLoS One 2020;15(1):e0227422", "10.1371/journal.pone.0227422", "31923250", "초록 확인"),
]

sec = {}
sec["overview"] = ("한눈에 보기",
"루로(Solanum quitoense Lam.)는 가지과(Solanaceae) 가지속의 여러해살이 관목으로, 안데스에서 신선 과일과 주스용으로 재배되며 에콰도르에서는 '나란히야(naranjilla, 작은 오렌지)', 콜롬비아에서는 '루로(lulo)'라고 부른다[4, 14]. "
"식약처 「식품원료 목록」에는 '루로열매'와 '루로페이스트' 두 행이 영문명 'Lulo, Naranjilla'로 올라 있고, 두 행 모두 상태는 '사용가능', 사용 조건은 '사용가능부위 : 열매'이다[1]. "
"이 종을 원재료로 하는 건강기능식품 고시형 원료는 확인하지 못함.\n\n"
"콜롬비아산 열매를 부위별로 나눈 2025년 분석에서 과육·껍질·씨는 생과 무게의 75.8%·12.4%·11.8%였고, 가식부(과육과 씨) 100 g의 에너지는 약 56 kcal, 식이섬유는 4.5 g으로 계산되었다[2]. "
"과육은 구연산(4.22 g/100 g 생과)이 많아 신맛이 강하고, 껍질에는 비타민 C(25.2 mg/100 g 생과)와 플라보노이드가, 씨에는 스페르미딘 유도체(페놀아마이드)가 많았다[2]. "
"같은 가지속의 감자·가지·까마중 등은 식약처 목록에서 별도 원료이므로, 이 문서의 수치는 S. quitoense 열매(일부는 Lasiocarpa 절 종간교잡 후대)를 분석한 자료만 옮겼다[1–3].")

sec["history"] = ("역사와 쓰임",
"루로는 안데스에서 기원한 과수로, 에콰도르·콜롬비아와 남아메리카 북부 산지에서 재배된다[3]. "
"에콰도르에서는 국내 생산의 최대 93%가 아마존 지역에 있어 이 지역의 경제적 잠재력이 큰 작물로 소개된다[4]. "
"에콰도르 아마존의 식용 과일 55종을 정리한 2023년 체계적 문헌고찰에서 루로는 이화학 특성과 생리활성 성분이 정리된 9종 가운데 하나였고, 이 지역 과일의 흔한 쓰임은 생식·전통 음식·민간약이었다[30]. "
"콜롬비아에서는 주로 가정에서 주스로 만들어 마시며, 고혈압에 쓰는 민간요법으로도 소개되었다[23].\n\n"
"유럽에서는 아직 잘 알려지지 않은 과일이지만, 신맛과 상쾌한 향 때문에 원산지에서는 주스·칵테일·잼·디저트로 널리 가공된다[2]. "
"2009년 코스타리카산 열매 연구도 좋은 향과 색 때문에 주스·넥타·잼 원료로서 잠재력이 크다고 평가했다[7]. "
"최근에는 북아메리카·일본·유럽 시장용 새 음료 향미의 기반이 될 수 있다는 전망이 있으나, 병해충으로 생산성이 떨어져 야생 근연종과의 교잡 육종이 진행되고 있다[3, 4]. "
"국내 재배·수입 이력은 확인하지 못함.")

sec["biology"] = ("식물학적 특징",
"루로는 여러해살이 관목이며, 분류학적으로 11–13종을 포함하는 가지속 Lasiocarpa 절에 속한다[4, 14]. "
"재배 루로는 자가수분 성향과 작물화 과정 때문에 유전적 기반이 좁고 동형접합성이 높은 것으로 보고된다[4]. "
"식물체의 분비 털(선모)에는 방어 물질인 아실당이 쌓이는데, 루로의 아실당은 가지과에서 흔한 자당 대신 마이오이노시톨을 골격으로 하는 아실이노시톨이다[12, 13].\n\n"
"열매는 익으면서 초록에서 주황으로 색이 바뀌며, 에콰도르 육종 재료는 아주심기 후 270일에 색 변화가 75%일 때 수확했다[3]. "
"종간교잡 후대 21개 재료의 과일 무게는 41.48–114.81 g, 과육 수율은 92% 이상, 당도는 7.0–13.0 °Brix, pH는 3.02–3.54였다[3]. "
"루로는 호흡 급등형 과일로, 익는 동안 (Z)-3-헥센-1-올 같은 알코올이 (Z)-3-헥센일 아세테이트 같은 에스터로 바뀌었고, 18 °C 저장 중 노화가 진행되자 뷰탄산메틸이 전체 휘발성분의 0.9%(2일)에서 76.4%(8일)로 늘었다[10]. "
"신선 과육의 핵심 향 성분은 (Z)-3-헥세날, 뷰탄산에틸, 3-설파닐헥실 아세테이트, 헥산산에틸이었다[9].")

sec["related_species"] = ("이름과 가까운 종",
"Lasiocarpa 절의 야생 근연종은 선충·시들음병 같은 토양 병해 저항성의 공급원으로 루로 육종에 쓰인다[3, 4]. "
"에콰도르 국립농업연구소 육종 재료를 대상으로 한 SSR 분석에서 루로용 프라이머 41개가 Lasiocarpa 6종으로 옮겨 쓰였고, 야생종의 대립유전자 다양성이 재배 루로보다 높았다[4]. "
"야생 근연종 Solanum hirtum은 COSII 유전자 염기 다양성이 재배 루로보다 유의하게 높았다[21].\n\n"
"같은 안데스 가지속 과수인 나무토마토(Solanum betaceum)와는 바이러스와 해충을 공유하는데, 나란히야 퇴록모자이크바이러스(NarCMV)는 나무토마토·가지에 전신 감염되었지만 감자와 담배에는 감염되지 못했다[14]. "
"열매 해충 Neoleucinodes elegantalis는 루로와 나무토마토 모두를 가해하며, 기주에 따라 생식기 형태가 달랐다[16]. "
"식약처 목록에서 감자(Solanum tuberosum)·가지(Solanum melongena)·까마중(Solanum nigrum)·코코나(Solanum sessiliflorum) 등은 각각 별도 원료로 올라 있어, 이 문서는 그 자료를 섞지 않았다[1].")

sec["cultivation"] = ("재배와 생산",
"루로는 콜롬비아·에콰도르·파나마·코스타리카의 해발 1000–1990 m에서 재배되며, 콜롬비아의 2018년 재배 면적은 8,821 ha, 평균 수량은 10.1 t/ha로 인용되었다[5]. "
"에콰도르에서는 기존 재배 방식이 산림 벌채와 대규모 토양 황폐화를 일으키고 식물을 병해충에 약하게 만든다는 지적이 있다[17]. "
"주요 병해충으로는 푸사리움병, 선충, 과실 천공충(Neoleucinodes elegantalis)이 꼽히고, 콜롬비아에서는 Phytophthora infestans 계열 역병이 유행했다[4, 16, 28]. "
"에콰도르에서는 티모바이러스 NarCMV와 NarMMV가 새로 보고되었고, NarMMV는 잡종 품종을 재배하는 지역에서 특히 흔했다[14, 15]. "
"나무토마토에서 분리한 감자Y바이러스(PVY)도 나란히야에 전신 감염되었다[31].\n\n"
"균근균 접종이나 퍼머컬처 밭 흙 접종은 인 흡수를 최대 104% 높였고, 근권 질소고정 세균 일부도 루로 생장을 늘렸다[17, 32]. "
"가뭄 스트레스는 광합성을 크게 낮췄으며, 브라시노스테로이드 유사체(DI-31) 4–8 mL/L 엽면 살포가 이를 완화했다[5]. "
"반형매 50가계를 4개 지역에서 평가한 결과 당도의 유전력은 높았고 수량·과중의 유전력은 낮았다[19]. "
"국내 생산 통계는 확인하지 못함.")

sec["processing"] = ("가공과 제품",
"루로는 주로 주스와 스무디로 소비되며 넥타·잼·아이스크림·농축액·발효 음료·리큐어로도 가공된다[2]. "
"과육을 착즙하거나 말리면 쓴맛이 강해지는데, 그 원인 물질로 N1,N4,N8-트리스(다이하이드로카페오일)스페르미딘과 N1,N8-비스(다이하이드로카페오일)스페르미딘이 분리되었다[8]. "
"말토덱스트린을 넣어 말린 과육 분말 가운데 동결건조품이 생과에 가장 가까운 향을 유지했고, 열풍건조는 향을 나쁘게 바꿨다[9]. "
"주스를 짜고 남은 박을 말린 분말은 식이섬유가 약 50%였고, 동결건조 분말의 카로티노이드는 60 µg/g 건물 이상, 60 °C 열풍건조의 카로티노이드 손실은 10%였다[22].\n\n"
"고압 균질화(50–150 MPa)는 주스의 항라디칼 능력과 폴리페놀 다양성을 높였다[23]. "
"동결건조 분말 음료는 소비자에게 받아들여졌으나 스테비아만 넣은 배합의 선호도가 가장 낮았다[24]. "
"나란히야 주스의 비타민 C는 35–55 °C 가속 저장에서 온도가 높을수록 빠르게 줄었다[25]. "
"껍질과 씨는 식이섬유·광물질·페놀 성분이 많아 부산물 활용 대상으로 제안되었다[2]. "
"식약처 목록에는 '루로페이스트'가 원료명으로 올라 있으나, 국내 제품 생산실적은 확인하지 못함.")

sec["genetics"] = ("유전과 육종",
"COSII 마커 연구에서 루로 32개 수집종은 6개 다형성 마커에서 47개 대립유전자를 보였고, 집단 분화가 매우 컸다(FST 0.90 초과)[20]. "
"재배 루로의 COSII 염기 다양성은 토마토와 비슷했고 야생 S. hirtum보다 낮았으며, 비생물 스트레스·병 저항성 관련 유전자 일부는 높은 변이를 유지했다[21]. "
"차세대 염기서열 분석으로 찾은 SSR 가운데 14개가 재배 루로 7개 지방품종에서 다형성을 보였지만, 재배종만의 평균 다형성 정보량(PIC)은 0.178로 낮았다[4].\n\n"
"선모의 아실이노시톨 생합성에서는 트라이아실이노시톨을 아세틸화하는 효소가 토마토 아실자당 경로의 마지막 단계와 상동으로 밝혀졌다[12]. "
"이어 선모에서 발현되는 BAHD 아실전이효소 3개를 바이러스 유도 유전자 침묵으로 억제하자 아실이노시톨 축적이 달라졌다[13]. "
"반형매 가계 연구는 수량·과중·당도·성숙지수에서 선발로 높은 유전 이득을 얻을 만한 유전 분산이 있다고 결론지었다[19]. "
"생장점·잎자루·배축 조직배양 증식법도 보고되었다[18]. "
"루로의 염색체 수와 전장 유전체 해독 결과는 확인하지 못함.")

sec["safety"] = ("안전성",
"식약처 「식품원료 목록」에서 루로는 열매만 사용가능부위로 적혀 있고, 잎 등 다른 부위의 행은 목록에 없다[1]. "
"에콰도르 국립농업연구소의 종간교잡 후대 21개 재료 과육을 HPLC로 분석한 결과 α-솔라닌은 0.16–4.35 mg/100 g, α-차코닌은 최고 19.60 mg/100 g이었다[3]. "
"저자들은 나란히야의 글리코알칼로이드 최대 기준이 없고 측정값이 감자에서 보고된 한도 200 mg/kg보다 낮다고 해석했으나, 결과의 생·건물 기준은 원문에 밝혀져 있지 않다[3]. "
"야생종에서 유래한 후대는 재배 품종보다 글리코알칼로이드가 많을 수 있어 교잡 육종에서 함량을 감시해야 한다고 했다[3]. "
"순수 재배 루로 열매의 글리코알칼로이드 정량 자료는 확인하지 못함. "
"파종 6주 어린 식물을 쓴 가지속 7종(나란히야 포함) 비교에서는 잎·줄기·뿌리에서 글리코알칼로이드가 검출되었으나 열매는 분석 대상이 아니었다[27].\n\n"
"콜롬비아산 건조 열대과일 20점의 농약 38종 분석에서 잔류(테부코나졸)는 우추바(Physalis peruviana) 2점에서만 검출되었고 루로 시료에서는 검출 보고가 없었다[26]. "
"껍질·과육·씨 추출물의 항산화·항균 효과와 스페르미딘 유도체의 ACE 억제 효과는 컴퓨터 모의·시험관 시험 결과로, 사람에서의 효과는 연구되지 않았다[2, 8]. "
"루로에 대한 식품 알레르기 보고와 국내 잔류농약 기준 등 공공기관 안전 정보는 확인하지 못함.")

KEYS = ["overview","history","biology","related_species","cultivation","processing","genetics","safety"]
sections = [{"key": k, "title": sec[k][0], "body": sec[k][1]} for k in KEYS]

def c(name, ko, cls, role, part, content, act, src):
    return {"name": name, "name_ko": ko, "class": cls, "role": role, "part": part, "content_text": content, "activity_ko": act, "source": src}
compounds = [
 c("Citric acid", "구연산(시트르산)", "유기산", "nutrient", "열매(과육·껍질·씨)", "과육 4.22 g/100 g 생과(총 유기산 4.74 g/100 g 생과); 모든 부위에서 주된 유기산", "루로의 강한 신맛을 내는 주성분이며, 가식부 당산비(감미지수)는 1.5로 계산되었다[2]", [2]),
 c("Ascorbic acid", "비타민 C(아스코르브산)", "수용성 비타민", "nutrient", "열매", "껍질 25.2 mg/100 g 생과, 과육 9.7 mg/100 g 생과, 가식부 약 8.4 mg/100 g 생과(콜롬비아산, UFLC-PDA)[2]; 코스타리카산 12.5 mg/100 g[7]; 종간교잡 후대 과육 18.28–79.11 mg/100 g 생과(반사측정기)[3]", "가식부 100 g이 성인 권장 섭취량의 약 9–10%를 채운다고 계산되었고, 주스 가속 저장에서는 온도가 높을수록 빨리 분해되었다[2, 25]", [2, 3, 7, 25]),
 c("alpha-Tocopherol", "α-토코페롤(비타민 E)", "지용성 비타민", "nutrient", "열매(껍질·과육)", "껍질 7.9 mg/100 g 생과, 과육 0.37 mg/100 g 생과; 씨는 γ-토코페롤 1.7 mg/100 g 생과가 주된 이성질체", "껍질에는 δ-토코페롤(5.12 mg/100 g 생과)도 함께 있어 껍질의 비타민 E 원료 가능성이 제시되었다[2]", [2]),
 c("Chlorogenic acid", "클로로겐산(5-O-카페오일퀸산)", "페놀산", "bioactive", "열매(과육·껍질)", "5-O-카페오일퀸산: 과육 추출물 12.1 mg/g, 껍질 8.6 mg/g, 씨 1.15 mg/g 추출물(80% 에탄올 추출물 기준)", "과육·태좌 조직에 주로 분포하는 주된 페놀산이며, 루로를 포함한 콜롬비아 가지과 과일 시료에서도 주된 페놀로 보고되었다[2, 6, 29]", [2, 6, 29]),
 c("N1,N4,N8-Tris(dihydrocaffeoyl)spermidine", "N1,N4,N8-트리스(다이하이드로카페오일)스페르미딘", "페놀아마이드(스페르미딘 유도체)", "marker", "열매(과육·씨)", "합성 표준품으로 생과·건조 과일에서 정량(초록에 수치 없음 — 확인하지 못함)[8]; 씨 추출물의 스페르미딘 유도체 합계 37.8 mg/g 추출물[2]", "가공 중 커지는 쓴맛의 원인 물질로 분리되었고, 컴퓨터 모의와 시험관 시험에서 ACE 억제 활성을 보였다(사람 시험 없음)[8]", [2, 8]),
 c("N1,N8-Bis(dihydrocaffeoyl)spermidine", "비스(다이하이드로카페오일)스페르미딘", "페놀아마이드(스페르미딘 유도체)", "bioactive", "열매(씨·과육)", "씨 추출물 10.7 mg/g(씨에서 가장 많은 단일 페놀 성분; 결합 위치 이성질체는 잠정 동정)[2]", "과육에서 쓴맛 물질로 분리되었고, 씨 추출물의 항진균 효과에 기여할 것으로 추정되었다(시험관 시험)[2, 8]", [2, 8]),
 c("beta-Carotene", "β-카로틴", "카로티노이드", "bioactive", "열매", "코스타리카산 총 카로티노이드 통째 열매 33.3 µg/g, 과육 7.2 µg/g(β-카로틴이 주성분)[7]; 박 동결건조 분말 총 카로티노이드 60 µg/g 건물 이상[22]; 종간교잡 후대 최고 94.30 µg β-카로틴 당량/g 건물[3]", "all-trans·13-cis·9-cis β-카로틴과 루테인이 동정되었고, β-카로틴은 비타민 A 전구체로 소개된다[3, 6]", [3, 6, 7, 22]),
 c("Sucrose", "자당(수크로스)", "당류", "nutrient", "열매(과육)", "가식부 자당 2.64·과당 2.23·포도당 0.97 g/100 g 생과[2]; 코스타리카산 자당 1.6·포도당 0.68·과당 0.7 g/100 g[7]", "과육에서 가장 많은 당이며, 껍질과 씨에서는 과당이 더 많았다[2]", [2, 7]),
 c("Rutin", "루틴(퀘르세틴-3-O-루티노사이드)", "플라보노이드(플라보놀 배당체)", "bioactive", "열매(껍질)", "개별 함량 확인하지 못함; 껍질 추출물의 플라보노이드 합계 14.2 mg/g(과육 1.88, 씨 0.20 mg/g 추출물)", "껍질의 플라보노이드는 퀘르세틴·아이소람네틴·캠페롤 배당체가 중심이며, 껍질 추출물의 산화 용혈 억제가 가장 오래 유지되었다(시험관 시험)[2, 6]", [2, 6]),
 c("Sinapic acid", "시나프산(시나프산 헥소사이드로 검출)", "페놀산", "bioactive", "열매(씨·과육)", "시나프산 헥소사이드: 씨 추출물 7.0 mg/g, 과육 1.70 mg/g; 페룰산 헥소사이드: 씨 7.1 mg/g, 과육 1.69 mg/g 추출물", "루로 열매 조직에서 시나프산·페룰산 유도체를 처음 보고한 결과다[2]", [2]),
 c("Methyl butanoate", "뷰탄산메틸", "휘발성 에스터", "bioactive", "열매(과육)", "코스타리카산 과육 휘발성분 10종 가운데 주성분[7]; 노화 중 전체 휘발성분의 0.9%(2일) → 76.4%(8일)[10]", "노화 과일의 이취(off-flavor)에 기여할 것으로 추정되었다[10]", [7, 10]),
 c("Ethyl butanoate", "뷰탄산에틸", "휘발성 에스터", "bioactive", "열매(과육)", "정량값은 초록에 없음(확인하지 못함); GC-O·GC-MS로 핵심 향 성분 판정", "(Z)-3-헥세날, 3-설파닐헥실 아세테이트, 헥산산에틸과 함께 루로 향의 핵심 성분이다[9]", [9]),
 c("Citroside A", "시트로사이드 A", "C13-노르아이소프레노이드 배당체", "bioactive", "잎(식품원료 사용부위 아님)", "잎의 배당체 혼합물에서 순수 분리(함량 확인하지 못함)", "효소 처리로 껍질 향 성분인 3-하이드록시-7,8-다이디하이드로-β-이오논을 만들고, 이는 화학 처리 후 β-다마세논으로 바뀐다[11]", [11]),
 c("alpha-Solanine", "α-솔라닌", "스테로이드 글리코알칼로이드", "bioactive", "열매(과육, 종간교잡 후대)", "0.16(P29)–4.35(P17) mg/100 g(동결건조 과육 분석, 생·건물 기준 원문에 없음)", "가지속 특유의 방어 물질로 고농도에서는 독성이 있으며, 순수 재배 루로 열매의 함량은 확인하지 못함[3]", [3]),
 c("alpha-Chaconine", "α-차코닌", "스테로이드 글리코알칼로이드", "bioactive", "열매(과육, 종간교잡 후대)", "재료 간 차이가 컸고 최고 19.60 mg/100 g(TP 재료; 생·건물 기준 원문에 없음)", "야생종 유래 후대는 함량이 높을 수 있어 육종에서 감시 대상으로 제시되었다[3]", [3]),
]

assays = [
 {"role": "literature", "compound": "Organic acids (citric acid, ascorbic acid)", "compound_ko": "유기산(구연산·아스코르브산)", "part": "열매(과육·껍질·씨)",
  "content": "구연산 과육 4.22 g/100 g 생과; 아스코르브산 껍질 25.2·과육 9.7 mg/100 g 생과[2]",
  "method": "UFLC-PDA(초고속 액체크로마토그래피-광다이오드어레이)",
  "conditions": {"instrument": "UFLC-PDA", "column": "역상 칼럼(제조사·규격은 본문에서 확인하지 못함)", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "245 nm(아스코르브산), 215 nm(그 밖의 유기산)", "injection": "", "sample_prep": "동결건조·분쇄(약 20 mesh) 시료를 메타인산 용액으로 추출", "standard": "유기산 표준품 검량선(검량식은 보충 표)", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "구연산은 루로 신맛의 주성분이고 비타민 C는 영양 지표로 쓰인다[2]. PMC 전문(Methods) 확인 — 칼럼·이동상 세부는 표·이전 논문으로 넘겨 본문에서 확인하지 못함[2].",
  "source": [2], "url": "https://doi.org/10.3390/foods14122083", "source_kind": "paper"},
 {"role": "literature", "compound": "Phenolic compounds and spermidine derivatives (5-O-caffeoylquinic acid, bis/tris(dihydrocaffeoyl)spermidines)", "compound_ko": "페놀 화합물·스페르미딘 유도체", "part": "열매(과육·껍질·씨)",
  "content": "5-O-카페오일퀸산 과육 12.1 mg/g 추출물; 씨 스페르미딘 유도체 합계 37.8 mg/g 추출물, 비스(다이하이드로카페오일)스페르미딘 10.7 mg/g 추출물[2]",
  "method": "HPLC-DAD-ESI/MS",
  "conditions": {"instrument": "HPLC-DAD-ESI/MS", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "DAD(UV-Vis) + ESI-MS(음이온 [M-H]⁻, MS² 조각 이온)", "injection": "", "sample_prep": "동결건조 분말 약 1 g을 에탄올/물(80:20, v/v) 30 mL로 실온 1시간씩 2회 추출 → 여과(Whatman No. 4) → 회전증발(150 mbar, 40 °C) → 동결건조 → 에탄올/물(20:80) 5 mg/mL로 녹여 0.22 µm 여과", "standard": "클로로겐산·페룰산·시나프산·에피카테킨·나린제닌·퀘르세틴-3-O-글루코사이드 검량선(표준품 없는 성분은 가장 비슷한 표준품 당량)", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "씨의 스페르미딘 유도체와 과육·껍질의 클로로겐산·플라보놀 배당체가 부위를 가르는 특징 성분이다[2]. PMC 전문 확인 — 칼럼·기울기는 이전 방법을 인용해 본문에서 확인하지 못함[2].",
  "source": [2], "url": "https://doi.org/10.3390/foods14122083", "source_kind": "paper"},
 {"role": "literature", "compound": "Tocopherols", "compound_ko": "토코페롤(α·γ·δ)", "part": "열매(껍질·과육·씨)",
  "content": "껍질 α-토코페롤 7.9·δ-토코페롤 5.12 mg/100 g 생과; 과육 α 0.37·γ 0.197 mg/100 g 생과; 씨 γ 1.7 mg/100 g 생과[2]",
  "method": "정상상 HPLC-형광",
  "conditions": {"instrument": "정상상 HPLC-형광검출기", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "형광(여기 290 nm, 방출 330 nm)", "injection": "", "sample_prep": "동결건조 분말", "standard": "토콜(tocol) 내부표준법, 표준품 머무름 시간으로 동정", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "껍질은 비타민 E가 많은 부위로 제시되었다[2]. PMC 전문 확인 — 칼럼·이동상은 본문에서 확인하지 못함; 본문의 껍질 총 토코페롤 '13.0 g/100 g fw'는 mg 단위의 오기로 보인다[2].",
  "source": [2], "url": "https://doi.org/10.3390/foods14122083", "source_kind": "paper"},
 {"role": "literature", "compound": "Glycoalkaloids (alpha-solanine, alpha-chaconine)", "compound_ko": "글리코알칼로이드(α-솔라닌·α-차코닌)", "part": "열매 과육(Lasiocarpa 절 종간교잡 후대 21개 재료)",
  "content": "α-솔라닌 0.16–4.35 mg/100 g, α-차코닌 최고 19.60 mg/100 g(생·건물 기준 원문에 없음)[3]",
  "method": "HPLC-UV",
  "conditions": {"instrument": "HPLC-UV/Vis 검출기", "column": "Hypersil GOLD C18(5 µm, 4.6 × 250 mm)", "mobile_phase": "아세토나이트릴/2차 증류수/인산 완충액 pH 7.6 (60/30/10)", "gradient": "등용매", "flow": "1.25 mL/min", "temp": "", "detection": "UV 202 nm", "injection": "", "sample_prep": "동결건조 분말 5 g + 메탄올/물/아세트산(73/18/9) 200 mL, 400 rpm 15분·900 rpm 1시간 교반 → 여과(Whatman No. 41) → 약 20 mL로 농축 → 메탄올 75 mL·25% 수산화암모늄 75 mL로 침전(5 °C, 45분) → 6000 rpm 원심 → 침전을 메탄올 5 mL에 녹여 0.22 µm 여과", "standard": "α-솔라닌·α-차코닌 표준품 피크 비교", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "가지속 열매의 식품 안전 지표로, 야생종을 교잡한 후대에서 함량 감시가 필요하다고 제시되었다[3]. PMC 전문(Methods) 확인 — 검출·정량한계와 회수율은 본문에 없음[3].",
  "source": [3], "url": "https://doi.org/10.3390/molecules31132217", "source_kind": "paper"},
]

nutrients = [
 {"form": "생과 가식부(과육+씨, 부위 비율로 계산한 값; 콜롬비아산)", "basis": "100 g 생과", "items": [
   {"name": "수분", "value": 82, "unit": "g"}, {"name": "에너지", "value": 56, "unit": "kcal"},
   {"name": "이용가능 탄수화물", "value": 7.9, "unit": "g"}, {"name": "식이섬유", "value": 4.5, "unit": "g"},
   {"name": "자당", "value": 2.64, "unit": "g"}, {"name": "과당", "value": 2.23, "unit": "g"}, {"name": "포도당", "value": 0.97, "unit": "g"},
   {"name": "비타민 C", "value": 8.4, "unit": "mg"}, {"name": "마그네슘", "value": 29, "unit": "mg"}, {"name": "칼슘", "value": 5.4, "unit": "mg"}], "source": [2]},
 {"form": "생과 과육(콜롬비아산)", "basis": "100 g 생과", "items": [
   {"name": "수분", "value": 87, "unit": "g"}, {"name": "단백질", "value": 1.22, "unit": "g"}, {"name": "지방", "value": 0.098, "unit": "g"},
   {"name": "회분", "value": 1.22, "unit": "g"}, {"name": "구연산", "value": 4.22, "unit": "g"}, {"name": "칼륨", "value": 459, "unit": "mg"},
   {"name": "비타민 C", "value": 9.7, "unit": "mg"}, {"name": "α-토코페롤", "value": 0.37, "unit": "mg"}], "source": [2]},
 {"form": "익은 열매(코스타리카산)", "basis": "100 g", "items": [
   {"name": "자당", "value": 1.6, "unit": "g"}, {"name": "포도당", "value": 0.68, "unit": "g"}, {"name": "과당", "value": 0.7, "unit": "g"},
   {"name": "적정산도(구연산 당량)", "value": 2.63, "unit": "g"}, {"name": "비타민 C", "value": 12.5, "unit": "mg"},
   {"name": "총 폴리페놀(갈산 당량)", "value": 48, "unit": "mg"}], "source": [7]},
]

world = [
 {"country": "콜롬비아", "metric": "area_ha", "year": 2018, "value": 8821, "unit": "ha", "note": "논문 서론의 인용값(원 통계 자료는 확인하지 못함); 같은 해 평균 수량 10.1 t/ha", "source": [5]},
]

d = {"slug": "solanum-quitoense", "name_ko": "루로", "name_en": "Lulo (Naranjilla)", "scientific_name": "Solanum quitoense Lam.",
     "aliases": ["루로", "루로열매", "루로페이스트", "나란히야", "Lulo", "Naranjilla"],
     "sections": sections, "compounds": compounds, "markers": [], "assays": assays, "nutrients": nutrients,
     "production": [], "world": world, "gi": [], "orgs": [], "sources": S}
(HERE / "dossier.json").write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in sections: print(s["key"], len(s["body"]))
