import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
A = "2026-11-02"
def pm(n, title, doi, pmid, pmc=None, url=None):
    t = f"{title} (PMID {pmid}" + (f", {pmc}" if pmc else "") + ")"
    return {"n": n, "title": t, "url": url or (f"https://doi.org/{doi}" if doi else f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"), "publisher": "PubMed", "accessed": A}
S = [
 {"n": 1, "title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 판다누스(Pandanus amaryllifolius Roxb. / Pandanus latifolius Hassk., Pandanus, Pandan) 판다누스잎·판다누스잎추출물·판다누스주스, 사용가능부위: 잎; 같은 속의 아단(Pandanus odoratissimus) 열매, 부아메라(Pandanus conoideus Lam.) 열매", "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
 pm(2, "Botany, phytochemistry, pharmacology, and applications of Pandanus amaryllifolius Roxb.: A review — Fitoterapia 2024 (초록만 확인)", "10.1016/j.fitote.2024.106144", "39053743"),
 pm(3, "Nutritional and functional innovations of Pandanus amaryllifolius Roxb.: From aroma to health-promoting bioactive — J Sci Food Agric 2026 (초록만 확인)", "10.1002/jsfa.70754", "42244025"),
 pm(4, "Profiling of phenolic compounds and their antioxidant and anticancer activities in pandan (Pandanus amaryllifolius Roxb.) extracts from different locations of Malaysia — BMC Complement Altern Med 2013;13:341", "10.1186/1472-6882-13-341", "24289290", "PMC4220543"),
 pm(5, "Ultrasound-Assisted Extraction of Squalene and 2-Acetyl-1-Pyrroline from Pandan Leaf: The Effects of Drying Methods and Extraction Conditions — Foods 2024;13(24):4010", "10.3390/foods13244010", "39766953", "PMC11728351"),
 pm(6, "Fragrance in Pandanus amaryllifolius Roxb. Despite the Presence of a Betaine Aldehyde Dehydrogenase 2 — Int J Mol Sci 2021;22(13):6968", "10.3390/ijms22136968", "34203477", "PMC8269274"),
 pm(7, "The complete chloroplast genome of Pandanus amaryllifolius Roxb. ex Lindl. (Pandanaceae) and its phylogenetic relationship — Mitochondrial DNA B Resour 2024", "10.1080/23802359.2024.2345773", "38665928", "PMC11044763"),
 pm(8, "Changes in key volatile components associated with leaf quality of Pandanus amaryllifolius Roxb. alongside growth duration — Food Chem X 2024", "10.1016/j.fochx.2024.102126", "39829996", "PMC11741041"),
 pm(9, "Comprehensive Characterization of Aroma Profile of \"Glutinous Rice\" Flavor in Pandanus amaryllifolius Using HS-SPME-GC-O-MS and HS-GC-IMS Technology Coupled with OAV — Foods 2025;14(6):935 (초록만 확인)", "10.3390/foods14060935", "40231908", "PMC11941618"),
 pm(10, "Identification and quantitation of the rice aroma compound, 2-acetyl-1-pyrroline, in bread flowers (Vallaris glabra Ktze) — J Agric Food Chem 2003;51(2):457-62 (초록만 확인)", "10.1021/jf025856x", "12517110"),
 pm(11, "[Chemical components from essential oil of Pandanus amaryllifolius leaves] — Zhong Yao Cai 2014 (중국어 논문, 초록만 확인)", None, "25345137"),
 pm(12, "Isolation and characterization of two new alkaloids, norpandamarilactonine-A and -B, from Pandanus amaryllifolius by spectroscopic and synthetic methods — J Nat Prod 2001;64(9):1224-5 (초록만 확인)", "10.1021/np010213h", "11575961"),
 pm(13, "Alkaloids from Pandanus amaryllifolius: Isolation and Their Plausible Biosynthetic Formation — J Nat Prod 2015 (초록만 확인)", "10.1021/acs.jnatprod.5b00252", "26461164"),
 pm(14, "New alkaloids from Pandanus amaryllifolius — J Nat Prod 2004;67(1):54-7 (초록만 확인)", "10.1021/np0303310", "14738386"),
 pm(15, "Recent Progress in the Chemistry of Pandanus Alkaloids — Alkaloids Chem Biol 2019 (초록만 확인)", "10.1016/bs.alkal.2018.12.001", "30850030"),
 pm(16, "Purification and characterization of a new antiviral protein from the leaves of Pandanus amaryllifolius (Pandanaceae) — Int J Biochem Cell Biol 2004;36(8):1440-6 (초록만 확인)", "10.1016/j.biocel.2004.01.015", "15147723"),
 pm(17, "Antihyperglycemic effects of Pandanus amaryllifolius Roxb. leaf extract — Pharmacogn Mag 2015 (초록만 확인)", "10.4103/0973-1296.149724", "25709220", "PMC4329610"),
 pm(18, "The effects of Pandanus amaryllifolius (Roxb.) leaf water extracts on fructose-induced metabolic syndrome rat model — BMC Complement Altern Med 2019 (초록만 확인)", "10.1186/s12906-019-2627-0", "31462242", "PMC6714300"),
 pm(19, "Pandanus amaryllifolius Roxb. Leaves Ethanol Extract Ameliorates Lipid and Proinflammatory Cytokines Profiles in a Rat Model of Dyslipidemia — J Pharmacopuncture 2024 (초록만 확인)", "10.3831/KPI.2024.27.2.101", "38948314", "PMC11194525"),
 pm(20, "Uricosuric, antioxidant, and anti-inflammatory properties of Pandanus amaryllifolius Roxb. extract against potassium oxonate-induced hyperuricemia in rats — Sci Rep 2025 (초록만 확인)", "10.1038/s41598-025-27933-7", "41449191", "PMC12753778"),
 pm(21, "Retraction Note: In vitro evaluation of Pandanus amaryllifolius ethanol extract for induction of cell death on non-hormone dependent human breast adenocarcinoma MDA-MB-231 cell via apoptosis — BMC Complement Med Ther 2026 (원 논문 PMID 22909149, 2012)", "10.1186/s12906-026-05454-8", "42365283", "PMC13310430"),
 pm(22, "Effect of drying conditions on drying kinetics and quality of aromatic Pandanus amaryllifolius leaves — J Food Sci Technol 2010 (초록만 확인)", "10.1007/s13197-010-0114-1", "23572703", "PMC3551131"),
 pm(23, "Ultrasonic Extraction of 2-Acetyl-1-Pyrroline (2AP) from Pandanus amaryllifolius Using Ethanol as Solvent — Molecules 2022;27(15):4906 (초록만 확인)", "10.3390/molecules27154906", "35956856", "PMC9370269"),
 pm(24, "Antioxidative properties of Pandanus amaryllifolius leaf extracts in accelerated oxidation and deep frying studies — Food Chem 2008;110(2):319-27 (초록만 확인)", "10.1016/j.foodchem.2008.02.004", "26049222"),
 pm(25, "Understanding the Molecular Interactions Between Pandan Pigment and Food Components for Enhanced Thermal Stability — Foods 2024;13(21):3361 (초록만 확인)", "10.3390/foods13213361", "39517144", "PMC11545325"),
 pm(26, "Genome characterization and complete sequence of a new badnavirus from Pandanus amaryllifolius — Arch Virol 2022 (초록만 확인)", "10.1007/s00705-022-05480-0", "35610515"),
 pm(27, "Effects of Hevea brasiliensis Intercropping on the Volatiles of Pandanus amaryllifolius Leaves — Foods 2023;12(4):888 (초록만 확인)", "10.3390/foods12040888", "36832964", "PMC9957087"),
 pm(28, "Drought Stress Induces Morpho-Physiological and Proteome Changes of Pandanus amaryllifolius — Plants (Basel) 2022;11(2):221 (초록만 확인)", "10.3390/plants11020221", "35050109", "PMC8778612"),
 pm(29, "Remediation of nutrient-rich waters using the terrestrial plant, Pandanus amaryllifolius Roxb. — J Environ Sci (China) 2014 (초록만 확인)", "10.1016/s1001-0742(13)60426-x", "25076532"),
 pm(30, "Pandanus plastomes decoded: When climate mirrors morphology and phylogenetic relationships — Am J Bot 2025 (초록만 확인)", "10.1002/ajb2.16461", "39887358"),
 pm(31, "Functional Drink Containing the Extracts of Purple Corn Cob and Pandan Leaves ... in Ovariectomized Rats — Rejuvenation Res 2018 (초록만 확인)", "10.1089/rej.2017.2009", "29847217"),
 pm(32, "Ultrasound-assisted encapsulation of Pandan (Pandanus amaryllifolius) extract — Ultrason Sonochem 2021;79:105793 (초록만 확인)", "10.1016/j.ultsonch.2021.105793", "34673338", "PMC8560631"),
 pm(33, "Carotenoid-cleavage activities of crude enzymes from Pandanous amryllifolius — Chem Biodivers 2014 (초록만 확인)", "10.1002/cbdv.201400029", "25408328"),
 pm(34, "Innovative enhancement of flavor profiles and functional metabolites composition in Pandanus amaryllifolius through lactic acid bacteria fermentation — Food Chem X 2024 (초록만 확인)", "10.1016/j.fochx.2024.101964", "39582657", "PMC11582449"),
 pm(35, "Isolation and structure elucidation of two new alkaloids, pandamarilactonine-C and -D, from Pandanus amaryllifolius and revision of relative stereochemistry of pandamarilactonine-A and -B by total synthesis — Chem Pharm Bull 2002;50(9):1303-4 (초록만 확인)", "10.1248/cpb.50.1303", "12237561"),
]

sec = []
def add(k, t, b): sec.append({"key": k, "title": t, "body": b})

add("overview", "한눈에 보기",
"판다누스(Pandanus amaryllifolius Roxb.)는 판다누스과(Pandanaceae)에 속하는 열대 식물로, 동남아시아에서 예부터 음식과 약으로 써 왔다[2]. 식약처 「식품원료 목록」에는 학명 Pandanus amaryllifolius Roxb. / Pandanus latifolius Hassk., 영어 이름 Pandanus, Pandan으로 올라 있다[1]. 이 목록에서 판다누스는 식품에 사용할 수 있는 원료(사용가능)이고, 사용 조건은 '사용가능부위 : 잎'이며 원료명은 판다누스잎·판다누스잎추출물·판다누스주스 세 가지다[1]. 이 종을 원재료로 하는 건강기능식품 고시형 원료는 확인하지 못함.\n\n"
"잎에서 찹쌀밥이나 향미(香米) 같은 냄새가 나며, 그 핵심 향 성분은 2-아세틸-1-피롤린(2AP)이다[9, 10]. 이 종은 식물계에서 2AP를 가장 높은 농도로 쌓는 식물로 보고된다[6]. 잎은 밥·디저트·코코넛잼·아이스크림에 향을 내고, 엽록소가 많아 초록 색소로도 쓰인다[4]. 잎에서는 100가지가 넘는 성분이 확인되었으며 2AP와 판다누스 알칼로이드가 특징 성분이다[2]. 잎은 식이섬유가 많고 에너지 밀도가 낮으며 플라보노이드·페놀산·카로티노이드·토코페롤 등을 함유한다고 정리되어 있다[3]. 시험관·동물 연구에서 항산화·혈당 조절·항균 작용이 보고되었으나[2, 18], 사람 대상 연구는 30명 규모의 단회 시험 정도만 확인했다[17].")

add("history", "역사",
"판다누스는 예부터 식품과 약으로 쓰여 왔다고 정리되어 있다[2]. 동남아시아에서는 잎을 향신료로 쓰고 민간 의학에도 써 왔다[13]. 인도네시아에서는 이 관목을 '판단 왕이(pandan wangi)'라 부르며, 속 이름 Pandanus 자체가 인도네시아 말 'pandan'에서 왔다[33]. 인도네시아에서 잎은 천연 색소·향료와 전통 치료에 두루 쓰였다[33]. 전통 의학에서는 당뇨병 치료에도 잎을 썼다[17]. 중국 연구진은 이 식물을 '동양의 바닐라'라고 소개하며, 신선한 잎을 동남아시아 사람들이 오래 먹어 왔다고 적었다[8].\n\n"
"인도에는 1798년 콜카타 식물원을 거쳐 들어왔고, 그 뒤 인도 반도 곳곳의 텃밭에서 향신료로 길러졌다[6]. 2000년대 들어 잎에서 새로운 피롤리딘계 알칼로이드가 잇달아 분리되었고[12, 14], 2015년에는 지상부 에탄올 추출물에서 새 화합물 9가지가 보고되었다[13]. 2012년에 나온 유방암 세포 연구 한 편은 2026년에 철회되었다[21]. 한국에 들어온 시기와 경로, 유럽연합 신규식품 목록에서의 지위는 확인하지 못함.")

add("biology", "식물학적 특징",
"판다누스는 여러해살이 열대 초본성 향신 식물로 소개된다[8]. 길고 좁은 잎이 나선형으로 돌려나고, 줄기 아래쪽 마디에서 공기뿌리가 나와 아래로 뻗는다[7]. 잎이 파인애플처럼 나선형으로 달린 긴 띠 모양이어서 'screw pine'이라고도 부른다[4]. 판다누스속의 약 600종 가운데 잎에 향이 있는 종은 이 종뿐이라고 정리되어 있다[4, 7].\n\n"
"잎 뒷면 표피에는 '표피 유두(epidermal papillae)'라는 주머니 모양 구조가 있어 2AP를 저장하는 곳으로 알려져 있다[6]. 생잎의 수분 함량은 82–85%였다[5]. 한 포기에 잎이 25장 넘게 달리며, 꼭대기의 어린잎일수록 2AP가 많고 아래쪽 늙은 잎일수록 스쿠알렌이 많았다[8]. 이 식물은 중간 정도의 가뭄 내성을 지녀 토양 수분이 적어도 살아남는다[28]. 육상 식물이지만 물에 잠긴 조건에서도 잘 자라 질산태 질소를 14일 만에 모두 제거한 실험도 있다[29]. 꽃과 열매(암수 개체 여부) 정보는 확인하지 못함.")

add("related_species", "이름과 가까운 종",
"식약처 목록은 이 종의 학명으로 Pandanus amaryllifolius Roxb.와 Pandanus latifolius Hassk.를 함께 적고 있다[1]. 엽록체 유전체 논문은 명명자를 'Roxb. ex Lindl.'로 표기했다[7]. 판다누스속은 열대·아열대에 널리 퍼진 큰 속으로, 종 수는 약 600종[4, 7], 약 700종[15], 750종[6] 등 출처마다 다르게 적혀 있다.\n\n"
"같은 속 식물 50종의 엽록체 유전체를 분석한 2025년 연구는 일곱 개 아속 가운데 Coronata 아속만 단계통이어서 아속 분류를 다시 손봐야 한다고 결론지었다[30]. 판다누스과는 판다누스목 안에서 키클란투스과(Cyclanthaceae)와 가깝다[7]. 판다누스 알칼로이드는 이 종 말고도 P. utilis, P. dubius에서 연구되었다[15].\n\n"
"식약처 목록에는 같은 속의 아단(Pandanus odoratissimus) 열매와 부아메라(Pandanus conoideus Lam.) 열매가 판다누스와 따로 올라 있다[1]. 판다누스는 잎만 쓸 수 있는 반면 이 두 원료는 열매를 쓰므로 서로 다른 원료다[1]. 이 자료는 P. amaryllifolius 잎 연구만 모았고 두 원료의 자료는 섞지 않았다[1].")

add("cultivation", "재배와 산지",
"국내 재배 면적·생산량 통계는 확인하지 못함. 판다누스는 쉽게 번식하고 향신 식물로 재배된다[7]. 태국 농민들은 중금속 축적을 줄이고 소득을 얻으려고 이 식물을 기른다[7]. 중국 하이난성 완닝의 시험 포장은 연평균 기온 22 °C, 연강수량 2100–2200 mm인 열대 계절풍 기후였고, 잎은 대개 심은 뒤 10개월이 지나 거둔다[8]. 현재 수확 기준은 주로 잎 길이 40 cm 이상이며, 여러 위치의 잎을 섞어 거두어 품질이 고르지 않다는 지적이 있다[8].\n\n"
"같은 연구는 2AP를 얻으려면 위에서 4–8번째 잎, 스쿠알렌을 얻으려면 11번째 아래 잎을 거두도록 제안했다[8]. 하이난에서는 고무나무 숲 아래에 판다누스를 섞어 심는 방식이 널리 쓰이며, 이때 잎의 피롤류 향 성분 비율이 8.83% 늘었다[27]. 말레이시아 세 지역(바초크·클랑·폰티안) 잎을 비교하면 북부 바초크산이 총페놀(6.72 mg/g 건조중량)과 총플라보노이드(1.87 mg/g)가 가장 많았다[4]. 인도 반도 여러 지역 집단 가운데 2AP가 가장 많은 우량 집단(12.2 ppm)이 골라졌다[6]. 잎에 모자이크·황화 증상을 일으키는 새 바드나바이러스가 보고되었다[26].")

add("processing", "가공과 이용",
"판다누스잎은 밥을 지을 때 향을 내거나 디저트·과자·코코넛잼·아이스크림을 만들 때 쓰이며, 초록 색소로도 인기가 있다[4]. 말레이시아에서는 허브를 날로 샐러드처럼 먹는 경우가 많다[4]. 열대 바깥으로 수출할 때는 휘발성 향 성분이 운송·보관 중에 날아가는 것이 걸림돌이어서, 초음파로 추출물을 미세 캡슐에 담는 방법이 연구되었다[32].\n\n"
"35 °C·상대습도 27%의 열펌프 건조는 45 °C 열풍 건조보다 2AP가 더 많이 남고 관능 점수도 높았다[22]. 동결 건조는 2AP 보존에, 50 °C 열풍 건조는 스쿠알렌 추출에 유리했다[5]. 에탄올 초음파 추출로 얻은 추출물의 2AP는 1.43 ppm이었다[23]. 판다누스 색소는 열에 약하지만 쌀 전분을 함께 넣으면 가장 잘 보호되었다[25]. 잎 추출물을 팜올레인에 0.2% 넣으면 180 °C 튀김에서 합성 항산화제 BHT 0.02%와 비슷하게 산화를 늦췄다[24]. 젖산균으로 발효하면 총페놀이 13–21%, 플라보노이드가 33–53% 늘었다[34]. 국내 건강기능식품 원료 생산실적은 확인하지 못함.")

add("genetics", "유전 정보",
"판다누스의 엽록체 유전체는 157,839 bp 길이로, 유전자 133개(단백질 암호 87개, tRNA 38개, rRNA 8개)를 담고 GC 함량은 37.7%다[7]. 두 역위 반복 구간(각 26,951 bp)과 큰 단일 복사 구간(85,746 bp), 작은 단일 복사 구간(18,191 bp)으로 이루어진 전형적인 4분 구조다[7]. 이 연구 전까지 이 종의 유전 연구는 DNA 지문 분석 한 건뿐이었다[7].\n\n"
"인도 연구진은 잎 전사체를 새로 조립해(BioProject PRJNA692823) 34,672개 전사체를 얻었다[6]. 향미 쌀과 다른 향 식물에서는 BADH2 유전자가 망가져야 2AP가 쌓이지만, 판다누스에서는 503개 아미노산으로 된 온전한 BADH2(PaBADH2)가 발현되고 효소 활성도 있었다[6]. 그런데도 잎의 2AP는 4.38 ppm으로 바스마티 쌀(0.20 ppm)보다 20–22배 많았다[6]. 연구진은 프롤린(8.01 µmol/g)과 메틸글리옥살이 많아 BADH2와 무관한 경로로 2AP가 만들어질 수 있다고 보았다[6]. 핵 유전체 전체 서열은 확인하지 못함.")

add("safety", "안전성",
"식약처 「식품원료 목록」에서 판다누스는 잎에 한해 식품에 사용할 수 있는 원료다[1]. 이 종을 원재료로 하는 건강기능식품 고시형 원료는 확인하지 못해, 고시된 섭취 시 주의사항도 확인하지 못함. 식약처·농촌진흥청 등 공공기관의 알레르기·잔류농약·독성 정보는 확인하지 못함.\n\n"
"건강한 성인 30명에게 75 g 포도당 부하 15분 뒤 판다누스차 또는 뜨거운 물을 마시게 한 시험에서 평균 혈당은 대조군 5.55, 판다누스차군 6.16 mmol/L로 통계적으로 달랐다[17]. 쥐 실험에서는 잎 추출물을 0.5–2 g/kg으로 14일간 먹였고[20], 잎 물추출물을 마시는 물에 10% 섞어 8주간 주었다[18]. 판다누스잎과 자색 옥수수 속대 추출물을 섞은 음료의 급성 독성 시험에서 쥐 반수치사량은 2000 mg/kg 체중을 넘었다[31]. 잎에서 분리한 렉틴(판다닌)은 토끼 적혈구를 응집시키는 성질이 있다[16].\n\n"
"MDA-MB-231 유방암 세포에 대한 2012년 시험관 연구는 2026년에 철회되었으므로 근거로 쓰지 않는다[21]. 사람에게서 장기간 먹었을 때의 안전성 자료는 확인하지 못함.")

C = [
 dict(name="2-Acetyl-1-pyrroline", name_ko="2-아세틸-1-피롤린(2AP)", **{"class": "피롤린계 휘발성 향 성분"}, role="marker", part="잎", content_text="생잎 10.3 mg/kg[10]; 1년생 잎 4.38 ppm(HS-SPME-GC-MS)[6]; 건조 잎 초음파 추출 80.72 µg/g 건조중량[5]", activity_ko="찹쌀밥·향미 같은 특유의 향을 내는 핵심 성분[9]", source=[5, 6, 9, 10]),
 dict(name="Squalene", name_ko="스쿠알렌", **{"class": "트리테르펜"}, role="bioactive", part="잎", content_text="열풍 건조 잎 1229.98 µg/g 건조중량[5]; 25번째(가장 아래) 잎 5427.33 µg/g[8]; 정유의 16.81%[11]", activity_ko="추출물에서 α-글루코시데이스·α-아밀레이스 억제(시험관)[5]", source=[5, 8, 11]),
 dict(name="Phytol", name_ko="피톨", **{"class": "다이테르펜 알코올"}, role="bioactive", part="잎(정유)", content_text="수증기 증류 정유의 42.15%(GC-MS 면적비)[11]; 잎 위치에 따른 함량 차이 없음[8]", activity_ko="", source=[8, 11]),
 dict(name="Neophytadiene", name_ko="네오피타다이엔", **{"class": "다이테르펜"}, role="bioactive", part="잎", content_text="15번째 잎에서 최고 613.53 µg/g[8]", activity_ko="판다누스의 '상쾌한 향'을 내는 성분으로 소개됨[8]", source=[8]),
 dict(name="Catechin", name_ko="카테킨", **{"class": "플라반-3-올"}, role="bioactive", part="잎", content_text="0.153–0.613 mg/g 건조중량(말레이시아 3개 지역, HPLC)[4]", activity_ko="분석한 플라보노이드 가운데 가장 많음[4]", source=[4]),
 dict(name="Naringin", name_ko="나린진", **{"class": "플라바논 배당체"}, role="bioactive", part="잎", content_text="바초크 0.325, 클랑 0.223 mg/g 건조중량, 폰티안 불검출[4]", activity_ko="", source=[4]),
 dict(name="Kaempferol", name_ko="캠페롤", **{"class": "플라보놀"}, role="bioactive", part="잎", content_text="클랑 0.278, 바초크 0.158 mg/g 건조중량, 폰티안 불검출[4]", activity_ko="", source=[4]),
 dict(name="Rutin", name_ko="루틴", **{"class": "플라보놀 배당체"}, role="bioactive", part="잎", content_text="바초크산에서만 0.082 mg/g 건조중량[4]", activity_ko="", source=[4]),
 dict(name="Gallic acid", name_ko="갈산", **{"class": "페놀산"}, role="bioactive", part="잎", content_text="0.214–0.423 mg/g 건조중량[4]", activity_ko="분석한 페놀산 가운데 가장 많음[4]", source=[4]),
 dict(name="Ferulic acid", name_ko="페룰산", **{"class": "페놀산"}, role="bioactive", part="잎", content_text="바초크산에서만 0.281 mg/g 건조중량[4]", activity_ko="", source=[4]),
 dict(name="Norpandamarilactonine A", name_ko="노르판다마릴락토닌 A", **{"class": "피롤리딘 알칼로이드"}, role="bioactive", part="잎", content_text="잎에서 새로 분리(함량 확인하지 못함)[12]", activity_ko="", source=[12]),
 dict(name="Pandamarilactonine A", name_ko="판다마릴락토닌 A", **{"class": "피롤리딘 알칼로이드"}, role="bioactive", part="잎", content_text="잎 에탄올 추출물에서 확인(함량 확인하지 못함)[19]", activity_ko="고지방식 쥐에서 지질 개선 작용의 후보 활성 성분으로 제시됨[19]", source=[19, 35]),
 dict(name="beta-Ionone", name_ko="β-이오논", **{"class": "노르이소프레노이드"}, role="bioactive", part="잎(효소 반응 산물)", content_text="잎 조효소가 β-카로틴을 분해해 만드는 주 휘발 산물[33]", activity_ko="향 성분[33]", source=[33]),
 dict(name="L-Proline", name_ko="프롤린", **{"class": "아미노산(2AP 전구체)"}, role="nutrient", part="잎", content_text="유리 프롤린 8.01 µmol/g[6]", activity_ko="2AP 합성의 전구체[6]", source=[6]),
 dict(name="gamma-Aminobutyric acid", name_ko="가바(GABA)", **{"class": "아미노산"}, role="nutrient", part="잎", content_text="10.1 µg/g[6]", activity_ko="", source=[6]),
]

E = lambda: {k: "" for k in ["instrument","column","mobile_phase","gradient","flow","temp","detection","injection","sample_prep","standard","linearity","lod","loq","recovery"]}
c1 = E(); c1.update(instrument="Agilent HPLC(Model 1100 펌프, L-7400 UV 검출기)", column="Agilent C18, 4.6 × 250 mm, 5 µm", mobile_phase="A: 2% 아세트산, B: 0.5% 아세트산–아세토니트릴(50:50, v/v)", gradient="A:B 0분 95:5 → 10분 90:10 → 40분 60:40 → 55분 45:55 → 60분 20:80 → 65분 0:100", flow="1 mL/min", temp="실온", detection="UV 260–360 nm", sample_prep="그늘에서 말려 간 잎 0.25 g을 메탄올 20 mL로 2시간 진탕 추출, 6 M HCl 5 mL 넣고 90 °C 2시간 환류 가수분해, 0.45 µm 여과", standard="(+)-카테킨·(−)-에피카테킨·나린진·루틴·캠페롤(Sigma-Aldrich); 머무름 시간·UV 스펙트럼·공동 주입으로 동정")
c2 = E(); c2.update(instrument="Agilent HPLC(Model 1100 펌프, L-7400 UV 검출기)", column="Agilent C18, 4.6 × 250 mm, 5 µm", mobile_phase="A: 인산 수용액, B: 아세토니트릴", gradient="A:B 0분 85:15 → 12분 75:25 → 20분 75:25 → 22분 85:15 → 30분 85:15", flow="1 mL/min", temp="실온", detection="UV 220–360 nm", injection="20 µL", sample_prep="잎 0.25 g을 인산 용액 20 mL로 추출, 6 M HCl 5 mL 넣어 50% 메탄올 중 1.2 M HCl로 만든 뒤 90 °C 2시간 환류, 0.45 µm 여과", standard="갈산·trans-신남산·trans-페룰산(Sigma-Aldrich)")
c3 = E(); c3.update(instrument="Hitachi HPLC(DAD 검출기, 5110)", column="ZORBAX Eclipse C18(원문 표기 'C'), 4.6 × 250 mm, 5 µm", mobile_phase="메탄올 100%", flow="1 mL/min", detection="DAD 210 nm", injection="10 µL", sample_prep="50 °C 열풍 건조 잎 분말(60메시)을 에탄올:n-헥산(1:1) 1:5 g/mL로 50 °C·300 W 초음파 60분 추출, 원심분리 후 여과", standard="스쿠알렌 표준품(Sigma-Aldrich)")
c4 = E(); c4.update(instrument="Waters UPLC + SCIEX 탠덤 질량분석기(UPLC-MS/MS)", column="역상 칼럼 150 × 2.1 mm, 1.7 µm(제조사 미기재)", mobile_phase="0.1% 포름산 수용액:아세토니트릴 = 95:5(v/v)", temp="40 °C", detection="양이온 모드 MS/MS", injection="1 µL", sample_prep="건조 잎 분말을 에탄올:n-헥산(1:1)으로 초음파 추출(스쿠알렌과 같은 추출액)", standard="2-AP 표준품(Toronto Research Chemicals)")
AS = [
 {"role": "literature", "compound": "Catechin, epicatechin, naringin, rutin, kaempferol", "compound_ko": "카테킨·에피카테킨·나린진·루틴·캠페롤", "part": "잎(말레이시아 3개 지역, 그늘 건조)", "content": "카테킨 0.153–0.613, 나린진 ND–0.325, 캠페롤 ND–0.278, 루틴 ND–0.082, 에피카테킨 0.008–0.035 mg/g 건조중량[4]", "method": "RP-HPLC-UV", "conditions": c1, "rationale": "산지별 플라보노이드 조성과 항산화력을 비교해 판다누스 추출물 표준화 자료로 제시함. 전문(Methods)에서 조건을 옮겼고 검출·정량한계·회수율은 원문에 없음[4].", "source": [4], "url": "https://doi.org/10.1186/1472-6882-13-341", "source_kind": "paper"},
 {"role": "literature", "compound": "Gallic acid, cinnamic acid, ferulic acid", "compound_ko": "갈산·신남산·페룰산", "part": "잎(말레이시아 3개 지역)", "content": "갈산 0.214–0.423, 신남산 ND–0.084, 페룰산 ND–0.281 mg/g 건조중량[4]", "method": "RP-HPLC-UV", "conditions": c2, "rationale": "갈산이 가장 많은 페놀산이고 산지에 따라 함량 차이가 커 품질 비교에 쓰임. 전문 확인, 인산 농도는 원문에 적혀 있지 않음[4].", "source": [4], "url": "https://doi.org/10.1186/1472-6882-13-341", "source_kind": "paper"},
 {"role": "literature", "compound": "Squalene", "compound_ko": "스쿠알렌", "part": "잎(열풍 건조)", "content": "1229.98 ± 13.09 µg/g 건조중량(최적 조건)[5]", "method": "HPLC-DAD", "conditions": c3, "rationale": "잎에 많은 지용성 생리활성 성분으로, 건조 방법·용매 최적화의 반응 변수로 정량함. 전문 확인, 유속 외 칼럼 온도·검량 범위·검출한계는 원문에 없음[5].", "source": [5], "url": "https://doi.org/10.3390/foods13244010", "source_kind": "paper"},
 {"role": "literature", "compound": "2-Acetyl-1-pyrroline", "compound_ko": "2-아세틸-1-피롤린(2AP)", "part": "잎(열풍 건조)", "content": "80.72 ± 0.88 µg/g 건조중량(최적 조건)[5]", "method": "UPLC-MS/MS", "conditions": c4, "rationale": "판다누스 특유의 향을 내는 성분으로 향 품질의 주 지표로 쓰임[8]. 전문 확인했으나 MRM 전이·유속·검출한계는 원문에 없음; 다른 연구는 HS-SPME-GC-MS(외부 표준 2,4,6-트라이메틸피리딘)로 4.38 ppm을 보고함[5, 6].", "source": [5, 6, 8], "url": "https://doi.org/10.3390/foods13244010", "source_kind": "paper"},
]

d = {"slug": "pandanus-amaryllifolius", "name_ko": "판다누스", "name_en": "Pandan (Pandanus)", "scientific_name": "Pandanus amaryllifolius Roxb.",
     "aliases": ["판다누스잎", "Pandan", "Pandanus", "Pandanus latifolius Hassk.", "Pandanus amaryllifolius Roxb. ex Lindl.", "pandan wangi", "fragrant pandan grass"],
     "sections": sec, "compounds": C, "markers": [], "nutrients": [], "assays": AS, "production": [], "world": [], "gi": [], "orgs": [], "sources": S}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in sec: print(s["key"], len(s["body"]))
