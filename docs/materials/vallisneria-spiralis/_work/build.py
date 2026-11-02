import json
A="2026-11-02"
def pm(n,title,doi,pmid,extra=""):
    url=f"https://doi.org/{doi}" if doi else f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
    return {"n":n,"title":f"{title} (PMID {pmid}{extra})","url":url,"publisher":"PubMed","accessed":A}
S=[
{"n":1,"title":"식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 밸리스네리아잎(Vallisneria spiralis), 영문명 Eel grass, Vallisneria, 식물, 사용가능, 사용가능부위: 잎; 같은 속 Water celery잎(Vallisneria americana, 사용가능부위: 잎) 행 대조 (로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json)","url":"https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020","publisher":"식품의약품안전처","accessed":"2026-10-13"},
pm(2,"Isolation and identification of antialgal compounds from the leaves of Vallisneria spiralis L. by activity-guided fractionation — Environ Sci Pollut Res Int 2006;13(4):233-7 (초록만 확인)","10.1065/espr2006.06.314","16910120"),
pm(3,"Effects of Rising Temperature on the Growth, Stoichiometry, and Palatability of Aquatic Plants — Front Plant Sci 2019;9:1947","10.3389/fpls.2018.01947","30671079",", PMC6331454, 전문 확인"),
pm(4,"The interaction of CO2 concentration and spatial location on O2 flux and mass transport in the freshwater macrophytes Vallisneria spiralis and V. americana — J Exp Biol 2007;210(Pt 3):522-32","10.1242/jeb.02679","17234622"),
{"n":5,"title":"Systematics of Vallisneria (Hydrocharitaceae) — Systematic Botany 2008;33(1):49-65 (원문 미열람: 네트워크 허용 목록 밖, 웹 검색 요약으로만 확인)","url":"https://www.ingentaconnect.com/content/aspt/sb/2008/00000033/00000001/art00008","publisher":"American Society of Plant Taxonomists","accessed":A},
{"n":6,"title":"한국산 미기록 식물: 낙동나사말(자라풀과) / An Unrecorded Species from Korean Flora: Vallisneria spinulosa (Hydrocharitaceae) — 2008 (원문 미열람: 네트워크 허용 목록 밖, 웹 검색 요약으로만 확인)","url":"https://koreascience.kr/article/JAKO200810103496763.page","publisher":"한국과학기술정보연구원(KoreaScience)","accessed":A},
pm(7,"Extensive Fouling of Eelgrass (Zostera marina L.) Reproductive Shoots by Invasive Tunicates — Ecol Evol 2025;15(12):e72663","10.1002/ece3.72663","41409089",", PMC12706531"),
pm(8,"Comparative studies on accumulation of Cr from metal solution and tannery effluent under repeated metal exposure by aquatic plants: its toxic effects — Environ Monit Assess 2002;80(1):17-31","10.1023/a:1020357427074","12437061"),
pm(9,"Cadmium-induced biochemical responses of Vallisneria spiralis — Protoplasma 2010;245(1-4):97-103","10.1007/s00709-010-0146-4","20446007"),
pm(10,"Cadmium toxicity and phytochelatin production in a rooted-submerged macrophyte Vallisneria spiralis exposed to low concentrations of cadmium — Environ Toxicol 2009;24(3):271-8","10.1002/tox.20429","18655189"),
pm(11,"Comparative assessment of Azolla pinnata and Vallisneria spiralis in Hg removal from G.B. Pant Sagar of Singrauli Industrial region, India — Environ Monit Assess 2008;148(1-4):75-84","10.1007/s10661-007-0140-2","18210204"),
pm(12,"Chromium accumulation in submerged aquatic plants treated with tannery effluent at Kanpur, India — J Environ Biol 2011;32(5):591-7","","22319874"),
pm(13,"A combined study on Vallisneria spiralis and lanthanum modified bentonite to immobilize arsenic in sediments — Environ Res 2023;216(Pt 3):114689","10.1016/j.envres.2022.114689","36323350"),
pm(14,"Phyto-accumulation potential of Vallisneria spiralis L. on F- contaminated water in hydroponic culture — Int J Phytoremediation 2026;28(12):2920-2929","10.1080/15226514.2026.2668615","42150754"),
pm(15,"Chlorobenzenes in waterweeds from the Xijiang River (Guangdong section) of the Pearl River — J Environ Sci (China) 2007;19(10):1171-7","10.1016/s1001-0742(07)60191-0","18062413"),
pm(16,"[Bio-toxic effect of pyrene on Vallisneria spiralis] — Ying Yong Sheng Tai Xue Bao 2007;18(7):1528-33 (중국어, 영문 초록)","","17886646"),
pm(17,"Diet Shift and Its Impact on Foraging Behavior of Siberian Crane (Grus leucogeranus) in Poyang Lake — PLoS One 2013;8(6):e65843","10.1371/journal.pone.0065843","23823943",", PMC3688820"),
pm(18,"Native and non-native plants provide similar refuge to invertebrate prey, but less than artificial plants — PLoS One 2015;10(4):e0124455","10.1371/journal.pone.0124455","25885967",", PMC4401678"),
pm(19,"Quantitative imaging of radial oxygen loss from Vallisneria spiralis roots with a fluorescent planar optode — Sci Total Environ 2016;569-570:1232-1240","10.1016/j.scitotenv.2016.06.198","27387799"),
pm(20,"[Experimental study on the environmental fate of nitrogen in snail-macrophyte ecosystem for water purification] — Huan Jing Ke Xue 2012;33(12):4307-15 (중국어, 영문 초록)","","23379157"),
pm(21,"[Bioremediation efficiency of applying Daphnia magna and submerged plants: a case study in Dishui Lake of Shanghai, China] — Ying Yong Sheng Tai Xue Bao 2010;21(2):495-9 (중국어, 영문 초록)","","20462026"),
pm(22,"[Effects of plant species combination and water body nutrient level on the biomass accumulation and allocation of three kinds functional plants] — Ying Yong Sheng Tai Xue Bao 2009;20(10):2370-6 (중국어, 영문 초록)","","20077692"),
pm(23,"Biogas production from water hyacinth and channel grass used for phytoremediation of industrial effluents — Bioresour Technol 2003;86(3):221-5","10.1016/s0960-8524(02)00178-5","12688463"),
pm(24,"Cytotoxicity and molecular docking analysis of phytochemicals from Vallisneria spiralis with protein target 3CZH in breast cancer management — Bioinformation 2024;20(12):2062-2068","10.6026/9732063002002062","40230925",", PMC11993420, 전문 확인(본문의 학명 표기가 빠져 있어 PubMed 검색 결과로 종을 판단)"),
pm(25,"Comparison of different plants in screening for Mn clastogenicity — Mutat Res 1990;242(2):157-61","10.1016/0165-1218(90)90042-z","2233832"),
pm(26,"Bioaccumulation and toxicity of Cu and Cd in Vallisneria spiralis (L.) — Environ Monit Assess 1994;33(1):75-84","10.1007/BF00546664","24201704"),
pm(27,"Occurrence of microcystin-LR in vegetated lagoons used for urban runoff management — Toxicon 2019;160:23-28","10.1016/j.toxicon.2019.02.004","30772435"),
pm(28,"Can we predict community-wide effects of herbicides from toxicity tests on macrophyte species? — Aquat Toxicol 2010;101(1):49-56","10.1016/j.aquatox.2010.08.017","20926143"),
pm(29,"The role of CO2 uptake by roots and CAM in acquisition of inorganic C by plants of the isoetid life-form — New Phytol 1988;108(2):125-148","10.1111/j.1469-8137.1988.tb03690.x","33874162"),
pm(30,"Changes in the Activities of Ribulose 1,5-Bisphosphate and Phosphoenolpyruvate Carboxylases in Submersed Aquatic Angiosperms during Aging — Plant Physiol 1982;70(4):1125-7","10.1104/pp.70.4.1125","16662625",", PMC1065837"),
pm(31,"Differences in bacterial community structure on Hydrilla verticillata and Vallisneria americana in a freshwater spring — Microbes Environ 2014;29(1):67-73","10.1264/jsme2.me13064","24553106",", PMC4041241"),
pm(32,"Multiple stressors unpredictably affect primary producers and decomposition in a model freshwater ecosystem — Environ Pollut 2024;347:123680","10.1016/j.envpol.2024.123680","38467363"),
pm(33,"Blood biochemistry profile of Qihe crucian carp Carassius auratus in different aquaponic systems — Environ Sci Pollut Res Int 2020;27(34):42898-42907","10.1007/s11356-020-10214-3","32725569"),
pm(34,"Involvement and interaction of microbial communities in the transformation and stabilization of chromium during the composting of tannery effluent treated biomass of Vallisneria spiralis L. — Bioresour Technol 2009;100(7):2198-203","10.1016/j.biortech.2008.10.036","19081715"),
pm(35,"Vallisneria invasion into Myriophyllum community: differential responses of complete ammonia oxidation (Comammox) community in changing rhizosphere environment — J Appl Microbiol 2026;137(3)","10.1093/jambio/lxag038","41637059"),
]

sections=[
{"key":"overview","title":"한눈에 보기","body":
"밸리스네리아(Vallisneria spiralis)는 자라풀과(Hydrocharitaceae) 나사말속에 속하는 물속 식물로, 식약처 「식품원료 목록」에는 원료명 '밸리스네리아잎', 영문명 'Eel grass, Vallisneria'로 한 행이 올라 있다[1]. 이 행의 상태는 '사용가능'이고 사용 조건은 '사용가능부위 : 잎'이어서, 이 목록으로 식품에 쓸 수 있는 부위는 잎뿐이다[1]. 같은 목록에는 같은 속의 Vallisneria americana가 'Water celery잎'이라는 별도 원료로 올라 있으므로 두 종의 자료는 구별해야 한다[1]. 이 종을 원재료로 하는 건강기능식품 고시형 원료는 확인하지 못함.\n\n"
"영어 이름 eelgrass는 바다에 사는 거머리말(Zostera marina)과 북미의 V. americana에도 쓰여 이름만으로 자료를 찾으면 다른 식물과 섞이기 쉽다[7, 31]. 인도 문헌에서는 channel grass라는 이름도 쓴다[23]. PubMed에 실린 이 종의 연구는 대부분 수질 정화, 중금속·유기오염물질 축적, 퇴적물 개선 같은 환경 분야이다[8–15, 19]. 잎에서 조류 성장을 억제하는 카로티노이드 분해산물과 말레이미드 화합물이 분리된 보고가 있으나 함량은 제시되지 않았다[2]. 잎의 일반 영양성분(단백질·무기질 등)을 이 종에서 직접 분석한 1차 자료는 확인하지 못함. 오염된 물에서 자란 개체는 카드뮴·크로뮴·수은 같은 중금속을 잎에도 많이 쌓을 수 있어, 식품으로 쓸 때는 자란 물의 수질이 중요하다[8–11]."},
{"key":"history","title":"이름과 이용의 역사","body":
"학명 Vallisneria spiralis L.은 인도·중국·프랑스 등지의 생태·독성 연구에서 널리 쓰여 왔다[8, 15, 28]. 식약처 목록에는 이 종의 잎이 식품원료로 올라 있으나, 어느 지역에서 어떤 방식으로 먹어 왔는지를 보여 주는 1차 자료는 확인하지 못함.\n\n"
"이 종은 수족관·정원 연못용 수초로도 유통되며, 네덜란드의 실험에서는 원예점에서 산 모종을 시험재료로 썼다[3]. 네덜란드 연구진은 같은 나라에서 이 종을 외래(비토착) 수생식물로 분류했다[18]. 2008년 나사말속 분류 연구는 미국 텍사스에서 구대륙산 V. spiralis를 북미 최초의 확실한 기록으로 보고했다고 정리된다(원문 미열람)[5].\n\n"
"중국 포양호에서는 겨울마다 전 세계 시베리아흰두루미의 95% 이상이 모여 V. spiralis의 덩이(괴경)를 주로 먹는다고 보고되었다[17]. 2011년 겨울에는 이 덩이가 극도로 부족해 두루미들이 습초지에서 다른 식물을 먹는 모습이 처음 관찰되었다[17]. 인도에서는 1990년대부터 이 종의 구리·카드뮴 축적 연구가 있었고[26], 폐수 정화에 쓴 바이오매스로 바이오가스를 만드는 연구도 나왔다[23]."},
{"key":"biology","title":"식물학적 특징","body":
"밸리스네리아는 뿌리를 물 밑 퇴적물에 내리고 잎이 물속에 잠겨 자라는 침수식물이며, 짧은 줄기에서 잎이 뭉쳐 나는 로제트형이다[3]. 중국 연구에서는 뿌리가 긴 침수식물로 분류해, 뿌리가 짧은 이삭물수세미(Myriophyllum spicatum) 군락에 침입하는 실험을 했다[35]. 뿌리는 전 길이에서 산소를 내보내며, 산소 누출은 뿌리 밑동에서 가장 강하고(표면 포화도 약 80%) 뿌리 끝으로 갈수록 약해진다(약 10%)[19]. 퇴적물 실험에서는 이 종이 녹는 비소를 철 산화물에 붙은 덜 움직이는 형태로 바꾸는 데 기여했다[13].\n\n"
"잎의 최대 산소 발생 속도는 CO2 17.1 mmol m⁻³ 조건에서 근연종 V. americana보다 높았으나, CO2를 10분의 1로 낮추면 두 종이 비슷해졌다[4]. 이 종은 CAM 같은 야간 탄소 고정을 하지 않는 것으로 확인되었고, 잎이 늙으면 RuBP 카복실화효소 활성이 줄어든다[29, 30]. 질소 동위원소 실험에서 이 식물은 물보다 퇴적물에서 주로 양분을 얻었고, 기르는 동안 생체중이 580% 늘고 포기(라멧)가 6.6개 늘어 영양번식으로 퍼졌다[20]. 네덜란드 실험에서 세 종 수생식물을 15·20·25 °C에서 16주 길렀을 때 온도가 높을수록 모든 종이 더 자랐고, 이 종은 세 종 가운데 잎의 질소 함량이 가장 낮고 인 함량이 가장 높았다[3]. 포양호 개체군은 겨울에 덩이를 만들어 물새의 먹이가 된다[17]."},
{"key":"related_species","title":"근연종과 혼동 주의","body":
"나사말속(Vallisneria)은 자라풀과에 속하며, 2008년 분자계통 연구는 분자 자료로 12종을 나누고 V. australis와 V. erecta 2종을 새로 기재했다고 정리된다(원문 미열람)[5]. 이 때문에 과거 여러 대륙에서 V. spiralis라는 이름으로 기록된 개체군 가운데 일부는 다른 종일 수 있으며, 호주 연못 실험처럼 지금도 V. spiralis라는 이름을 쓰는 연구가 있다[5, 32]. 동아시아 논문 속 'V. spiralis'가 엄밀히 어느 종인지는 이 자료로 확인하지 못함.\n\n"
"식약처 목록에는 V. americana의 잎이 'Water celery잎'이라는 별도 원료로 올라 있으므로, 이 종의 자료와 섞어 쓰면 안 된다[1]. 두 종은 같은 조건에서 잎의 산소 발생 속도가 달라 생리적으로도 구별된다[4]. 국내에는 나사말과 2008년 미기록종으로 보고된 낙동나사말(V. spinulosa) 같은 근연 자생종이 문헌에 오르며, 이 내용은 웹 검색 요약으로만 확인했다[6].\n\n"
"영어 이름 eelgrass는 바다 거머리말(Zostera marina)에도 쓰이는데, 거머리말은 해초로서 민물 수초인 이 종과 서식지가 전혀 다르다[7]. 미국 플로리다 연구는 V. americana를 eelgrass라고 불렀다[31]. 따라서 'eel grass'로 찾은 자료는 학명을 반드시 확인해야 한다[1, 7, 31]."},
{"key":"cultivation","title":"재배와 분포","body":
"이 종을 식용 작물로 재배하는 통계나 재배 기술 자료는 확인하지 못함. 국내 생산 통계(통계청·농림축산식품부)에서도 이 종에 해당하는 품목은 확인하지 못함.\n\n"
"대신 호수 생태 복원용으로 심는 연구가 많다[21]. 상하이 디수이호에서는 물벼룩을 먼저 넣은 뒤 이 종을 포함한 침수식물 5종을 옮겨 심었고, 10개월 관측에서 총질소·총인 농도가 유의하게 낮아지고 투명도가 평균 3.4–3.7 m에 이르렀다[21]. 물의 영양 수준을 네 단계로 높인 실험에서 이 종의 생물량은 높은 두 단계에서 낮은 두 단계보다 평균 45.88% 적어, 부영양화된 물에서는 오히려 잘 자라지 못했다[22]. 우렁이(Bellamya)와 함께 기르면 이 종의 생장과 질소 제거가 촉진되었다[20].\n\n"
"프랑스의 제초제 실험에서는 수생식물 6종 가운데 이 종이 가장 내성이 강했다[28]. 중국에서는 붕어를 기르는 아쿠아포닉스 시스템에 이 종을 함께 기른 시험도 있다[33]. 수족관·연못용 수초로는 원예점에서도 모종을 구할 수 있다[3]."},
{"key":"processing","title":"가공과 이용","body":
"이 종의 잎을 식품으로 가공·조리하는 방법이나 제품 생산실적은 확인하지 못함. 식약처 「식품 등의 생산실적」 건강기능식품 품목에서도 이 종에 해당하는 원료는 확인하지 못함.\n\n"
"비식품 이용으로는, 펄프·제지 폐수와 주정 폐수 정화에 쓴 뒤 이 식물을 바이오가스 원료로 쓰는 연구가 있으며, 바이오가스는 6–9일에 최대로 나와 부레옥잠보다 빨랐다[23]. 무두질 공장 폐수를 14일 정화한 바이오매스는 뿌리에 크로뮴 358 µg/g 건물, 잎·줄기에 62 µg/g 건물을 쌓았고, 이를 퇴비화하는 과정에서 6가 크로뮴이 3가로 바뀌었다[34]. 이렇게 정화에 쓴 바이오매스는 식품 용도가 아니다[23, 34].\n\n"
"잎 에탄올 추출물을 활성 유도 분획하면 남조류(Microcystis aeruginosa) 성장을 억제하는 분획 2개를 얻을 수 있었고, 주된 타감물질은 엽록소의 광산화 부산물인 2-에틸-3-메틸말레이미드였다[2]. 이 종의 추출물로 은·산화철 나노입자를 만들어 유방암 세포(MCF-7)에 처리한 시험관 연구가 있으나, 이는 나노입자에 대한 세포 실험일 뿐 식품 섭취 효과의 근거가 아니다[24]."},
{"key":"genetics","title":"유전과 분자 연구","body":
"이 종의 핵 참조 유전체나 엽록체 전체 유전체 해독 논문은 PubMed 검색에서 확인하지 못함. 나사말속 전체의 분자계통 연구(2008)는 분자 자료로 12종을 구분하고, 분자상 차이가 없는 일부 무리 안에서도 형태 차이로 2–3종을 더 인정했다고 정리된다(원문 미열람)[5].\n\n"
"세포유전학 쪽에서는 이 종이 망간 염의 염색체 손상(염색체 이상)을 보는 시험 식물로 쓰였다[25]. 황산망간 같은 양이온 망간 염은 양파 비늘줄기나 완두 씨앗보다 물속 식물인 이 종에서 장기 노출 때 더 강한 염색체 이상을 일으켰다[25]. 카드뮴 노출에서는 해독 펩타이드인 피토켈라틴이 잎과 뿌리 모두에서 유도되었고, 그 농도는 카드뮴 독성과 직선 관계를 보여 오염 지표로 제안되었다[10].\n\n"
"이 종 자체의 전사체·유전자 발현 연구는 확인하지 못함."},
{"key":"safety","title":"안전성","body":
"식약처 목록에서 이 종의 잎은 '사용가능' 원료이며, 별도의 섭취 시 주의사항은 이 목록에서 확인하지 못함[1]. 이 종에 대한 알레르기·중독 사례나 공공기관의 잔류·독성 성분 안내는 확인하지 못함.\n\n"
"가장 주의할 점은 오염물질 축적으로, 실험실에서 크로뮴 8 mg/L에 9일 노출하면 잎에 크로뮴이 1,378 µg/g 건물까지 쌓였다[8]. 카드뮴을 처리하면 뿌리 5,542 µg/g 건물, 잎 4,368 µg/g 건물까지 쌓였다[9]. 0.01–0.64 µM의 낮은 카드뮴 농도에서는 잎의 축적량이 뿌리보다 유의하게 많아, 먹는 부위인 잎이 취약할 수 있다[10]. 수은 0.1–3.0 mg/L 용액에서는 6일 동안 수은의 70–84%를 제거했고, 건물 축적량은 처리 농도와 높은 상관(R² = 0.99)을 보였다[11]. 불소 10 mg/L 수경 재배에서는 20일 뒤 지상부에 0.98 mg/g 건물이 쌓였다[14]. 퇴적물의 녹는 비소는 이 종을 심으면 48.81% 줄었으나[13], 식물체의 비소 함량 수치는 확인하지 못함.\n\n"
"유기오염물질도 쌓여, 중국 시장강 조사에서 잎에는 저분자 클로로벤젠이, 뿌리에는 PCB·HCB가 더 많았다[15]. 피렌 0.01–0.1 mg/L에 10일 노출하면 잎에 피렌이 많이 쌓였고, 0.01 mg/L부터 스트레스 영향이 나타났다[16]. 이 종이 우점한 도시 빗물 연못 물에서는 남조류 독소 마이크로시스틴-LR이 검출되었다[27]. 따라서 정화용으로 오염된 물에서 기른 개체는 먹지 말고 수질이 확인된 것만 써야 한다는 판단은 이 축적 연구들에서 나온 추론이다[8–11, 27]."},
]
comp=[
{"name":"2-Ethyl-3-methylmaleimide","name_ko":"2-에틸-3-메틸말레이미드","class":"말레이미드(엽록소 광산화 산물)","role":"marker","part":"잎","content_text":"잎 95% 에탄올 추출물의 항조류 활성 1분획에서 HRGC-MS로 동정, 함량 미기재[2]","activity_ko":"주된 타감물질로 남조류 Microcystis aeruginosa 성장 억제(시험관)[2]","source":[2]},
{"name":"Dihydroactinidiolide","name_ko":"디하이드로악티니디올라이드","class":"노르이소프레노이드(카로티노이드 분해산물)","role":"bioactive","part":"잎","content_text":"항조류 활성 1분획에서 동정, 함량 미기재[2]","activity_ko":"남조류 성장 억제 분획의 구성 성분(시험관)[2]","source":[2]},
{"name":"4-Oxo-beta-ionone","name_ko":"4-옥소-베타-이오논","class":"노르이소프레노이드(이오논 유도체)","role":"bioactive","part":"잎","content_text":"항조류 활성 1분획에서 동정, 함량 미기재[2]","activity_ko":"잠재적 타감물질(남조류 억제, 시험관)[2]","source":[2]},
{"name":"3-Hydroxy-5,6-epoxy-beta-ionone","name_ko":"3-하이드록시-5,6-에폭시-베타-이오논","class":"노르이소프레노이드(이오논 유도체)","role":"bioactive","part":"잎","content_text":"항조류 활성 2분획에서 동정, 함량 미기재[2]","activity_ko":"잠재적 타감물질(남조류 억제, 시험관)[2]","source":[2]},
{"name":"Loliolide","name_ko":"롤리올라이드","class":"모노테르페노이드 락톤(카로티노이드 분해산물)","role":"bioactive","part":"잎","content_text":"항조류 활성 2분획에서 동정, 함량 미기재[2]","activity_ko":"남조류 성장 억제 분획의 구성 성분(시험관)[2]","source":[2]},
{"name":"6-Hydroxy-3-oxo-alpha-ionone","name_ko":"6-하이드록시-3-옥소-알파-이오논","class":"노르이소프레노이드(이오논 유도체)","role":"bioactive","part":"잎","content_text":"항조류 활성 2분획에서 동정, 함량 미기재[2]","activity_ko":"잠재적 타감물질(남조류 억제, 시험관)[2]","source":[2]},
{"name":"Glutathione","name_ko":"글루타티온(환원형)","class":"트라이펩타이드 항산화물질","role":"bioactive","part":"잎·뿌리","content_text":"카드뮴 농도·노출 시간에 따라 잎·뿌리에서 증가(수치는 초록에 없음)[10]; 피렌 노출 시 감소[16]","activity_ko":"중금속·유기오염물질 스트레스에 대한 해독·항산화 반응 지표[10, 16]","source":[10,16]},
{"name":"Phytochelatin","name_ko":"피토켈라틴","class":"금속 결합 펩타이드","role":"bioactive","part":"잎·뿌리","content_text":"카드뮴 0.01–0.64 µM 모든 농도에서 유도, 잎이 뿌리보다 높음(수치는 초록에 없음)[10]","activity_ko":"카드뮴 해독; 농도가 카드뮴 독성과 직선 관계여서 오염 지표로 제안[10]","source":[10]},
{"name":"Cysteine","name_ko":"시스테인","class":"황 함유 아미노산","role":"bioactive","part":"잎·뿌리","content_text":"카드뮴 낮은 농도에서 증가 후 높은 농도에서 감소(수치는 초록에 없음)[9]; 카드뮴 스트레스에서 합성이 구리보다 많음[26]","activity_ko":"금속 해독 물질의 전구체로 스트레스 반응 지표[9, 26]","source":[9,26]},
{"name":"Chlorophyll a","name_ko":"엽록소 a","class":"광합성 색소","role":"bioactive","part":"잎","content_text":"무두질 폐수 100%·9일 노출에서 총 엽록소 최대 67.4% 감소[12]; 수은 농도에 따라 엽록소 a 감소[11]","activity_ko":"광합성 색소; 오염 독성의 생리 지표[11, 12]","source":[11,12]},
{"name":"Nitrogen","name_ko":"질소","class":"다량 원소","role":"nutrient","part":"지상부","content_text":"15·20·25 °C 16주 재배에서 비교한 3종(E. nuttallii·P. lucens·V. spiralis) 가운데 가장 낮음(수치는 그림에만)[3]","activity_ko":"단백질 함량과 관련된 영양 지표; 이 종은 퇴적물에서 주로 질소를 얻음[3, 20]","source":[3,20]},
{"name":"Phosphorus","name_ko":"인","class":"다량 원소","role":"nutrient","part":"지상부","content_text":"같은 실험 3종 가운데 가장 높음(수치는 그림에만)[3]","activity_ko":"무기질 영양 지표[3]","source":[3]},
]
assays=[
{"role":"literature","compound":"Total phenolics","compound_ko":"총 페놀(탄닌산 당량)","part":"지상부(건조 분쇄)","content":"그래프로만 제시, 본문 수치 미기재[3]",
 "method":"FeCl3 환원 비색법(분광광도)","conditions":{"instrument":"Synergy HT 마이크로플레이트 리더(분광광도)","column":"","mobile_phase":"","gradient":"","flow":"","temp":"추출 80 °C","detection":"510 nm","injection":"","sample_prep":"60 °C 48시간 건조·Tissuelyser II 분쇄 시료 2–4 mg + 80% 에탄올 1 mL, 80 °C에서 10분 추출 후 SDS 용액과 FeCl3 시약 첨가","standard":"탄닌산 검량선(mg 탄닌산 당량/g 건물)","linearity":"","lod":"","loq":"","recovery":""},
 "rationale":"수생식물의 초식 방어·기호성과 연결해 보는 2차 대사산물 총량 지표; 전문 확인, 직선성·검출한계·회수율은 원문에 없음[3].","source":[3],"url":"https://doi.org/10.3389/fpls.2018.01947","source_kind":"paper"},
{"role":"literature","compound":"Phosphorus","compound_ko":"인(식물체 총인)","part":"지상부(건조 분쇄)","content":"비교 3종 가운데 가장 높음, 수치는 그림에만[3]",
 "method":"회화·분해 후 인산염 자동분석(연속흐름 분석기)","conditions":{"instrument":"QuAAtro 자동분석기(Seal Analytical); 탄소·질소는 FLASH 2000 원소분석기","column":"","mobile_phase":"","gradient":"","flow":"","temp":"","detection":"","injection":"","sample_prep":"60 °C 48시간 건조·분쇄 시료를 회화·분해한 뒤 인산염 농도 측정","standard":"","linearity":"","lod":"","loq":"","recovery":""},
 "rationale":"잎의 무기질 영양과 온도·양분 조건에 따른 화학량(C:N:P) 변화를 보는 지표; 전문 확인, 검량·회수율 정보는 원문에 없음[3].","source":[3],"url":"https://doi.org/10.3389/fpls.2018.01947","source_kind":"paper"},
{"role":"literature","compound":"2-Ethyl-3-methylmaleimide","compound_ko":"2-에틸-3-메틸말레이미드","part":"잎(풍건)","content":"정량값 미기재(동정만)[2]",
 "method":"HRGC-MS(고분해능 가스크로마토그래피-질량분석), 유도체화로 구조 확인","conditions":{"instrument":"","column":"","mobile_phase":"","gradient":"","flow":"","temp":"","detection":"","injection":"","sample_prep":"잎을 씻어 풍건 후 95% 에탄올로 환류 추출, 칼럼 크로마토그래피와 항조류 활성 유도 분획[2]","standard":"","linearity":"","lod":"","loq":"","recovery":""},
 "rationale":"이 종 잎의 주된 타감물질로 보고된 성분; 초록만 확인, 전문 확인 못함[2].","source":[2],"url":"https://doi.org/10.1065/espr2006.06.314","source_kind":"paper"},
]
d={"slug":"vallisneria-spiralis","name_ko":"밸리스네리아","name_en":"Eel grass, Vallisneria (channel grass)","scientific_name":"Vallisneria spiralis L.",
 "aliases":["밸리스네리아잎","Eel grass","Vallisneria","Channel grass"],
 "sections":sections,"compounds":comp,"markers":[],"nutrients":[],"assays":assays,"production":[],"world":[],"gi":[],"orgs":[],"sources":S}
json.dump(d,open('/home/user/hfoodguide-wave3/docs/materials/vallisneria-spiralis/dossier.json','w'),ensure_ascii=False,indent=1)
for s in sections: print(s['key'],len(s['body']))
