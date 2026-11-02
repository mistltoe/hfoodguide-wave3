import json
from pathlib import Path
OUT = Path("/home/user/hfoodguide-wave3/docs/materials/rubus-chamaemorus/dossier.json")
A = "2026-11-02"
def pm(n, title, doi=None, pmid=None):
    url = f"https://doi.org/{doi}" if doi else f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
    return {"n": n, "title": title, "url": url, "publisher": "PubMed", "accessed": A}
sources = [
 {"n": 1, "title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 진들딸기열매(Rubus chamaemorus L. / Chamaemorus norwegica Greene; 이명 장지딸기; Cloudberry, Baked-apple berry), 식품원료(A코드), 사용가능, 사용가능부위: 열매 (로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json)", "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
 pm(2, "Gold from nature's pantry: a diachronic study of Rubus chamaemorus L. (Rosaceae) in Swedish gastronomy and economy — J Ethnobiol Ethnomed 2025 (PMID 41457281, PMC12859927, 전문 확인)", "10.1186/s13002-025-00843-8"),
 pm(3, "The origin of the octoploid cloudberry (Rubus chamaemorus) genome is the result of multiple and complex polyploidization events — J Hered 2026 (PMID 41879285, PMC13326439, 전문 확인)", "10.1093/jhered/esag028"),
 pm(4, "Genetic differentiation of Rubus chamaemorus populations in the Czech Republic and Norway after the last glacial period — Ecol Evol 2018 (PMID 29938086, PMC6010844, 전문 서론·초록 확인)", "10.1002/ece3.4101"),
 pm(5, "Comprehensive Characterization of Secondary Metabolites in Fruits and Leaves of Cloudberry (Rubus chamaemorus L.) — Metabolites 2023 (PMID 37233639, PMC10222136, 전문 확인)", "10.3390/metabo13050598"),
 pm(6, "Ellagitannin-rich cloudberry inhibits hepatocyte growth factor induced cell migration and PI3K/AKT activation in colon carcinoma cells and tumors in Min mice — Oncotarget 2016 (PMID 27270323, PMC5190067, 전문 확인)", "10.18632/oncotarget.9724"),
 pm(7, "Alaskan wild berry resources and human health under the cloud of climate change — J Agric Food Chem 2010 (PMID 20025229, PMC2850959, 전문 확인)", "10.1021/jf902693r"),
 pm(8, "Determination of Carotenoids and Their Antioxidant Activity in Fruits of Selected Species from the Genus Rubus and Their Cultivars and Hybrids from Poland Versus Other Regions of the World — Antioxidants 2025 (PMID 41462639, PMC12729337, 전문 확인)", "10.3390/antiox14121438"),
 pm(9, "Northern berries as a source of carotenoids — Acta Biochim Pol 2012;59(1):133-4 (PMID 22428126, 초록만 확인)", pmid="22428126"),
 pm(10, "Analysis of pentacyclic triterpenoids and phytosterols in cloudberry (Rubus chamaemorus) by LC-MS/MS — Nat Prod Res 2024 (PMID 39428696, 초록만 확인)", "10.1080/14786419.2024.2417837"),
 pm(11, "Antioxidant activity of isolated ellagitannins from red raspberries and cloudberries — J Agric Food Chem 2012 (PMID 22229937, 초록만 확인)", "10.1021/jf203431g"),
 pm(12, "Differential effectiveness of berry polyphenols as anti-giardial agents — Parasitology 2011 (PMID 21813029, PMC3196466, 전문 확인)", "10.1017/S0031182011000825"),
 pm(13, "Identification and quantification of phenolic compounds in berries of Fragaria and Rubus species (family Rosaceae) — J Agric Food Chem 2004 (PMID 15453684, 초록만 확인)", "10.1021/jf049450r"),
 pm(14, "Contents of anthocyanins and ellagitannins in selected foods consumed in Finland — J Agric Food Chem 2007 (PMID 17261015, 초록만 확인)", "10.1021/jf062897a"),
 pm(15, "Cloudberry (Rubus chamaemorus L.) Supplementation Attenuates the Development of Metabolic Inflammation in a High-Fat Diet Mouse Model of Obesity — Nutrients 2022 (PMID 36145221, PMC9503149, 전문 확인)", "10.3390/nu14183846"),
 pm(16, "Changes in intestinal immunity, gut microbiota, and expression of energy metabolism-related genes explain adenoma growth in bilberry and cloudberry-fed Apc(Min) mice — Nutr Res 2016 (PMID 27865612, 초록만 확인)", "10.1016/j.nutres.2016.10.003"),
 pm(17, "Ellagic acid and natural sources of ellagitannins as possible chemopreventive agents against intestinal tumorigenesis in the Min mouse — Nutr Cancer 2006 (PMID 16800775, 초록만 확인)", "10.1207/s15327914nc5401_9"),
 pm(18, "Sanguiin H-6 Fractionated from Cloudberry (Rubus chamaemorus) Seeds Can Prevent the Methicillin-Resistant Staphylococcus aureus Biofilm Development during Wound Infection — Antibiotics 2021 (PMID 34943693, 초록만 확인)", "10.3390/antibiotics10121481"),
 pm(19, "Effects of ellagitannin-rich berries on blood lipids, gut microbiota, and urolithin production in human subjects with symptoms of metabolic syndrome — Mol Nutr Food Res 2013 (PMID 23934737, 초록만 확인)", "10.1002/mnfr.201300280"),
 pm(20, "Pollination ecology of the high latitude, dioecious cloudberry (Rubus chamaemorus; Rosaceae) — Am J Bot 2009 (PMID 21628260, 초록만 확인)", "10.3732/ajb.0800102"),
 pm(21, "Pollination by deceit, floral sex ratios and seed set in dioecious Rubus chamaemorus L. — Oecologia 1986 (PMID 28311917, 초록만 확인)", "10.1007/BF00379493"),
 pm(22, "Carbon allocation during fruiting in Rubus chamaemorus — Ann Bot 2009 (PMID 19520701, PMC2729635, 초록 확인)", "10.1093/aob/mcp142"),
 pm(23, "Limited carbohydrate availability as a potential cause of fruit abortion in Rubus chamaemorus — Physiol Plant 2001 (PMID 11473695, 초록만 확인)", "10.1034/j.1399-3054.2001.1120311.x"),
 pm(24, "Habitat Characteristics and Mineral Nutrition Status of Rubus chamaemorus L. in Latvia — Plants 2023 (PMID 36771613, PMC9920050, 초록 확인)", "10.3390/plants12030528"),
 pm(25, "Assessing the influence of genotype and temperature on polyphenol composition in cloudberry (Rubus chamaemorus L.) using a novel mass spectrometric method — J Agric Food Chem 2011 (PMID 21916411, 초록만 확인)", "10.1021/jf202083b"),
 pm(26, "Chemical composition of ripe fruits of Rubus chamaemorus L. grown in different habitats — J Sci Food Agric 2012 (PMID 22083544, 초록만 확인)", "10.1002/jsfa.4705"),
 pm(27, "The Impacts of Climate and Social Changes on Cloudberry (Bakeapple) Picking: a Case Study from Southeastern Labrador — Hum Ecol 2018 (PMID 30613123, PMC6302063, 초록 확인)", "10.1007/s10745-018-0038-3"),
 pm(28, "Sorbitol, Rubus fruit, and misconception — Food Chem 2015 (PMID 25053101, 초록만 확인)", "10.1016/j.foodchem.2014.06.073"),
 pm(29, "Contact allergy to styrene and related chemicals — Contact Dermatitis 1984 (PMID 6713846, 초록만 확인)", "10.1111/j.1600-0536.1984.tb00342.x"),
 pm(30, "The influence of heat on the aroma of cloudberries (Rubus chamaemorus L.) — Z Lebensm Unters Forsch 1977 (PMID 835340, 초록만 확인)", "10.1007/BF01123552"),
 pm(31, "Fermentation and dry fractionation increase bioactivity of cloudberry (Rubus chamaemorus) — Food Chem 2016 (PMID 26617039, 초록만 확인)", "10.1016/j.foodchem.2015.11.061"),
 pm(32, "Storage stability of microencapsulated cloudberry (Rubus chamaemorus) phenolics — J Agric Food Chem 2008 (PMID 18989975, 초록만 확인)", "10.1021/jf801868h"),
 pm(33, "Antibiofilm, Antimicrobial, and Anti-inflammatory Potential of Rubus chamaemorus Rhizome, Leaf, and Fruit Extracts — Chem Biodivers 2026 (PMID 42424107, PMC13348868, 초록 확인)", "10.1002/cbdv.71479"),
 pm(34, "Berry phenolics selectively inhibit the growth of intestinal pathogens — J Appl Microbiol 2005 (PMID 15752346, 초록만 확인)", "10.1111/j.1365-2672.2005.02547.x"),
 pm(35, "Nutraceutical Potential of High-latitude and High-altitude Berries Rich in Ellagitannins — Curr Med Chem 2023 (PMID 35209815, 초록만 확인)", "10.2174/0929867329666220224151938"),
]

S = {}
S["overview"] = ("한눈에 보기",
"진들딸기(Rubus chamaemorus)는 장미과 산딸기속의 여러해살이 풀로, 영어로 클라우드베리(cloudberry)라 부르며 북반구 한대·아한대의 습지와 이탄지에 둘레극지적으로 자란다[2, 3]. "
"식약처 「식품원료 목록」에는 원료명 '진들딸기열매'(학명 Rubus chamaemorus L. / Chamaemorus norwegica Greene, 이명 장지딸기, 영명 Cloudberry·Baked-apple berry)가 한 행으로 올라 있다[1]. "
"대분류는 '식품원료(A코드)', 상태는 '사용가능'이며, 사용 조건이 '사용가능부위 : 열매'여서 열매만 식품에 쓸 수 있다[1]. "
"이 종을 원재료로 하는 건강기능식품 고시형 원료는 확인하지 못함.\n\n"
"익은 열매는 호박색에서 주황색을 띠고 비타민 C·A·E와 엘라지탄닌이 많아 북유럽에서 잼·디저트·리큐어로 귀하게 쓰인다[2, 3]. "
"폴리페놀의 대부분이 엘라지탄닌(산귀인 H-6·람베르티아닌 C)이고 안토시아닌은 매우 적다는 점이 다른 붉은 산딸기속 열매와 다르다[7, 11, 12]. "
"효과 근거는 대부분 쥐 실험과 시험관 연구이며, 사람 연구는 딸기·라즈베리와 섞은 베리 식이 시험 정도다[15, 16, 19].")
S["history"] = ("이용의 역사",
"둘레극지 지역에서 진들딸기는 산업화 이전 사회의 가장 중요한 베리였을 것으로 보이며, 캐나다·알래스카 이누이트와 시베리아 극동 주민에게 비타민 C 공급원이었다[2]. "
"스웨덴에서 저장한 진들딸기의 가장 오래된 기록은 1549년 성의 회계 문서이고, 17세기에는 의사들이 괴혈병 예방 효과를 알고 있었다[2]. "
"사미족은 열매를 즙에 천천히 끓여 소금을 조금 뿌린 뒤 자작나무 껍질 상자에 담아 땅에 묻어 두었다가 겨울에 꺼내 먹었다[2]. "
"스웨덴에서 처음 출판된 진들딸기 절임 조리법은 1743년이며, 19세기에 설탕이 흔해지면서 잼 조리법이 늘었다[2]. "
"제2차 세계대전 때 감귤 수입이 줄자 스웨덴 당국은 진들딸기·로즈힙 같은 비타민 C 열매의 소비를 권했다[2]. "
"1960년대까지 북부 농촌에서는 직접 딴 진들딸기를 파는 것이 중요한 수입원이었고, 2000년대 이후 상업 채집은 주로 동남아시아 출신 계절 노동자가 맡는다[2]. "
"캐나다 래브라도 남동부에서는 '베이크애플(bakeapple)'이라 부르며, 영구동토·식생·물 환경의 변화가 열매의 양·품질·익는 시기에 영향을 준다고 보고됐다[27].")
S["biology"] = ("식물학적 특징",
"진들딸기는 키 15–30 cm의 낮은 여러해살이 풀로 기는 뿌리줄기가 있고, 잎은 콩팥 모양에 5–7갈래로 갈라지며 꽃은 크고 하나씩 피는 흰색이다[2]. "
"암수딴그루여서 수꽃과 암꽃이 다른 개체에 피고, 스스로 꽃가루받이를 하지 못한다[2, 3]. "
"암꽃은 수꽃보다 작고 꽃가루가 없으며 꿀도 매우 적어, 꽃등에와 뒤영벌이 수꽃을 더 선호한다[21]. "
"3년 조사에서 43개 과의 곤충이 꽃을 찾았고, 그중 꽃등에과·집파리과 같은 파리목이 가장 중요한 꽃가루받이 곤충이었다[20]. "
"주로 넓게 뻗는 뿌리줄기로 무성 번식하며, 열매 발달에는 뿌리줄기에 저장된 탄수화물이 필요해 뿌리줄기가 짧은 줄기는 열매가 작거나 떨어지기 쉽다[22, 23]. "
"영하 40 °C까지 견디지만 꽃이 서리에 약해 해마다 수확량을 예측하기 어렵다[2]. "
"유라시아에서는 북위 78°에서 남쪽으로 약 54°(드물게 44°)까지 분포하고, 빙하기 유존 개체군이 북한·스코틀랜드·폴란드·체코 등에도 있다[2, 4]. "
"남한의 자생 여부는 확인하지 못함.")
S["related_species"] = ("이름과 가까운 종",
"진들딸기는 장미과 장미아과 산딸기속(Rubus)에 속하며, 이 속은 250–1,000종으로 추정되고 남극을 뺀 모든 대륙에 있다[3]. "
"식약처 목록의 학명 칸에는 이명으로 Chamaemorus norwegica Greene이 함께 적혀 있다[1]. "
"계통 연구는 복잡한 잡종 기원을 시사하며, 일부 분석은 이 종을 산딸기속 주 계통 바깥의 이른 갈래로 둔다[3]. "
"라즈베리·블랙베리 같은 다른 산딸기속 열매에 엘라지탄닌과 함께 프로안토시아니딘이 많은 것과 달리, 진들딸기는 엘라지탄닌과 페놀산이 주를 이룬다[5]. "
"적색 라즈베리(Rubus idaeus)와 주된 엘라지탄닌은 같지만 라즈베리에는 안토시아닌도 함께 들어 있다[11]. "
"북극딸기(arctic bramble, Rubus arcticus)는 엘라지탄닌 봉우리가 대부분 같으나 추정 엘라지탄닌 비율이 44.1%로 진들딸기(72.0%)보다 낮다[12, 35]. "
"핀란드 식품 조사에서 엘라지탄닌은 진들딸기·라즈베리·로즈힙·딸기·비타민나무 열매 5종에서만 검출됐다[14]. "
"붉은 산딸기속 열매는 안토시아닌 배당 형태로 서로 구별되며, 진들딸기에서는 하이드록시신남산이 유리형으로 있다는 점이 특징이다[13].")
S["cultivation"] = ("재배와 산지",
"진들딸기는 수요가 많지만 재배는 흔하지 않고 주로 야생에서 채집한다[3]. "
"스웨덴에서는 1990년대부터 작물화를 시도해 2000년대에 몇 품종이 나왔으나 아직 성공했다고 보기 어렵다[2]. "
"교배 계통 연구에서는 모본('Nyby' 또는 'Fjellgull')과 재배 온도에 따라 열매의 폴리페놀 조성이 달랐다[25]. "
"라트비아 18개 자생지 조사에서는 분해가 덜 된 유기물이 많은 산성 이탄토가 재배에 가장 알맞았고, 인·황·붕소·몰리브덴 관리가 과제로 꼽혔다[24]. "
"핀란드 북부 10개 서식지 조사에서 햇빛이 드는 개방지 열매는 그늘진 곳보다 시트르산이 많고 α-토코페롤이 적었으며, 따뜻한 여름에 수확량이 많았다[26]. "
"스웨덴 숲에서는 보통 해에 약 8만 톤의 진들딸기가 익는 것으로 추정되지만, 베리 전체의 수확 비율은 최근 수십 년 평균 4–6%였고 2024년에는 2%로 떨어졌다[2]. "
"채집 계절 노동자 수도 5,000명에서 2024년 1,200명으로 줄어 2025년에는 열매와 일손이 모두 모자랐다[2]. "
"국내 재배·생산 통계는 확인하지 못함.")
S["processing"] = ("가공과 이용",
"예전에는 나무통에 저장했으나 지금은 주로 냉동하거나 잼 등 가공품으로 만든다[2]. "
"잼·마멀레이드·파르페·시럽·리큐어·소스로 쓰고, 잎은 차로 우리며, 씨 기름은 화장품에 들어간다[2]. "
"가열하면 4-비닐페놀·푸르푸랄·5-하이드록시메틸푸르푸랄 같은 향 성분이 크게 늘고, 생 착즙액에서는 81개 휘발 성분의 농도가 보고됐다[30]. "
"착즙박을 발효하면 고분자 엘라지탄닌이 일부 엘라그산 유도체로 분해되고, 씨 부분을 건식 분획하면 탄닌은 고운 분획에, 플라보놀은 굵은 분획에 모였다[31]. "
"엘라지탄닌이 많은 추출물은 말토덱스트린(DE5–8)으로 동결건조 미세캡슐화했을 때 저장 안정성이 좋아졌다[32]. "
"동물 실험에 쓰인 공기건조 분말은 생과 약 700 g에서 약 100 g이 나왔다[15]. "
"잎 추출물은 총폴리페놀이 열매 추출물의 26배였고 잎 메탄올 추출물은 시험관에서 5-리폭시게나아제를 강하게 억제했지만, 식약처 목록에서 쓸 수 있는 부위는 열매뿐이다[1, 5, 33]. "
"국내 건강기능식품 생산실적에서 이 원료는 확인하지 못함.")
S["genetics"] = ("유전 정보",
"진들딸기는 염색체 2n = 8x = 56인 팔배체이며, 유전체 크기는 2.46 pg/2C(약 3.8 Gbp)로 추정됐다[4]. "
"수컷 한 개체의 HiFi 장독 서열과 Hi-C로 염색체 수준의 반수체 분리 유전체가 처음 조립되었고, 두 반수체는 1,198 Mb와 1,161 Mb로 각각 28개 유사 염색체로 묶였다[3]. "
"예측된 단백질 암호 유전자는 74,132개와 70,692개, 반복 서열은 약 60%, BUSCO 완성도는 99.2%였다[3]. "
"적색 라즈베리 유전체와 4:1로 염색체가 대응해 팔배체 기원을 뒷받침했고, 7개 염색체 한 벌(β)이 나머지 21개(α)와 뚜렷이 달라 이질·동질 배수화가 섞인 기원으로 해석됐다[3]. "
"체코 크르코노셰 산지·노르웨이 본토·스발바르 184개체의 SSR 분석에서는 162개 유전형이 나왔고, 집단 간 분화 지수는 0.45로 높았으며 변이의 70.8%는 집단 안에 있었다[4]. "
"유럽 최남단인 체코 집단은 위급 멸종위기종으로 보호 대상이다[4].")
S["safety"] = ("안전성",
"진들딸기열매는 식약처 목록에서 열매에 한해 '사용가능'인 식품원료이며, 부위 외의 사용 조건은 적혀 있지 않다[1]. "
"건강기능식품 고시의 섭취 시 주의사항과 국내 공공기관의 알레르기·잔류·독성 성분 정보는 확인하지 못함. "
"열매 향 성분인 4-비닐페놀은 스타이렌 접촉 알레르기 환자에게서 교차 반응을 보였으며, 이 물질은 진들딸기 등 여러 식품에 들어 있다[29, 30]. "
"산딸기속 열매에 당알코올이 많다는 통념과 달리 진들딸기 시료의 당알코올은 0.01 g/100 g이었다[28]. "
"고지방 식이 쥐에 공기건조 분말을 사료 무게의 20%로 먹인 실험에서 체중 증가는 막지 못했지만 SAA·ALT 상승과 고콜레스테롤혈증·고혈당 진행이 억제됐다[15]. "
"Min 쥐에서 동결건조 열매 10% 식이는 종양 수를 줄였으나, 씨·과육 식이는 선종 형성에 영향이 없었고 순수 엘라그산은 십이지장 선종 크기를 키웠다[6, 16, 17]. "
"대사증후군 증상이 있는 사람의 베리 혼합 식이 시험에서는 엘라지탄닌 생체이용률이 장내 미생물 구성에 따라 달랐다[19].")

KEYS = ["overview","history","biology","related_species","cultivation","processing","genetics","safety"]
sections = [{"key": k, "title": S[k][0], "body": S[k][1]} for k in KEYS]

def c(name, ko, cls, role, part, content, act, src):
    return {"name": name, "name_ko": ko, "class": cls, "role": role, "part": part, "content_text": content, "activity_ko": act, "source": src}
compounds = [
 c("Sanguiin H-6","산귀인 H-6","엘라지탄닌(이량체)","marker","열매·씨","열매 페놀 분리물의 80%가 엘라지탄닌이며 이량체 산귀인 H-6과 삼량체 람베르티아닌 C가 주성분[11]; 재배 온도에 따른 조성 차이를 이끄는 주요 성분[25]","씨에서 분획한 산귀인 H-6이 MRSA 생물막 형성을 억제하고 쥐 상처 감염 모델에서도 효과[18]; 베리 페놀 중 엘라지탄닌은 포도상구균을 강하게 억제했고 진들딸기·라즈베리가 가장 좋은 억제제였음[34]",[11,25,18,34]),
 c("Lambertianin C","람베르티아닌 C","엘라지탄닌(삼량체)","bioactive","열매·씨","산귀인 H-6과 함께 주된 엘라지탄닌[11]","시험관 MRSA 생물막 억제는 보였으나 쥐 상처 모델에서 항MRSA 효과 없음[18]",[11,18]),
 c("Pedunculagin","페둔쿨라긴","엘라지탄닌(단량체)","bioactive","열매","진들딸기의 단량체 엘라지탄닌으로 확인[11]","확인하지 못함",[11]),
 c("Ellagic acid","엘라그산","페놀산(엘라지탄닌 가수분해물)","marker","열매·씨","동결건조 열매 메탄올 추출물 1067 μg/mL(엘라지탄닌 7251 μg/mL, 엘라그산 당량)[6]; 과육 5.3% 식이의 유리 엘라그산 34 mg/kg[17]","순수 엘라그산(식이 1,564 mg/kg)은 Min 쥐 선종 수에 영향이 없고 십이지장 선종 크기를 키움[17]",[6,17]),
 c("beta-Carotene","β-카로틴","카로티노이드","nutrient","열매","전체 카로티노이드 2840 μg/100 g 건조중량 중 83%(HPLC)[9]; TLC에서 β-카로틴 표준품으로 존재 확인[8]","확인하지 못함",[9,8]),
 c("Lutein","루테인","카로티노이드(잔토필)","bioactive","열매·잎","열매 카로티노이드로 네오잔틴·비올라잔틴·안테라잔틴·루테인·제아잔틴·β-카로틴과 지방산 에스터형 잔토필이 보고됨(문헌 정리)[8]; 잎 저극성 분획에서도 검출[5]","확인하지 못함",[8,5]),
 c("Cyanidin 3-glucoside","시아니딘-3-글루코사이드","안토시아닌","bioactive","열매","알래스카 열매 전체 안토시아닌 0.01 mg/g 생중량(시아니딘-3-글루코사이드 당량), 4종 확인[7]; 동결건조 열매 추출물 안토시아닌 3 μg/mL[6]","확인하지 못함",[7,6]),
 c("Quercetin 3-O-glucuronide","퀘르세틴-3-글루쿠로나이드(미켈리아닌)","플라보놀 배당체","bioactive","열매·잎","딸기속·산딸기속 열매에 공통된 대표 플라보놀 배당체[13]; 잎 폴리페놀 분획의 주성분[5]","잎 폴리페놀 분획은 초과산화 음이온 소거능이 트롤록스보다 60% 높음(혼합물)[5]",[13,5]),
 c("p-Coumaric acid","p-쿠마르산","하이드록시신남산","bioactive","열매","진들딸기에서는 하이드록시신남산이 유리형으로 존재[13]; 폴리페놀 추출물에서 상당량 확인[12]","지아르디아 살충 효과에 기여할 가능성이 제기됨(시험관)[12]",[13,12]),
 c("Benzoic acid","벤조산","페놀산(방향족 카복실산)","bioactive","열매","열매 추출물 2D NMR에서 강한 신호[5]; 폴리페놀 추출물에서 상당량 확인[12]","확인하지 못함",[5,12]),
 c("Tormentic acid","토르멘트산","오환성 트라이테르페노이드산","bioactive","잎·꽃받침·열매","부위별 약 190–1800 μg/g 건조중량(LC-MS/MS)[10]","확인하지 못함",[10]),
 c("beta-Sitosterol","β-시토스테롤","피토스테롤","bioactive","잎·꽃받침·열매","비극성 분획 62–750 µg/g 건조중량[10]","확인하지 못함",[10]),
 c("Ascorbic acid","아스코르브산(비타민 C)","비타민","nutrient","열매","함량이 높다고 보고됨(수치는 확인하지 못함)[5]","북극권 주민의 비타민 C 공급원이며 17세기 괴혈병 예방에 쓰임[2]",[5,2]),
 c("alpha-Tocopherol","α-토코페롤(비타민 E)","비타민","nutrient","열매","서식지 간 차이가 크고 개방지 열매가 그늘진 곳보다 적음(수치는 초록에 없음)[26]","확인하지 못함",[26]),
 c("4-Vinylphenol","4-비닐페놀","휘발성 페놀(향 성분)","bioactive","열매","가열하면 크게 늘어나는 향 성분[30]","스타이렌 접촉 알레르기 환자에서 교차 반응[29]",[30,29]),
]
E = lambda **k: {**{f:"" for f in ["instrument","column","mobile_phase","gradient","flow","temp","detection","injection","sample_prep","standard","linearity","lod","loq","recovery"]}, **k}
assays = [
 {"role":"literature","compound":"Ellagic acid","compound_ko":"엘라지탄닌(엘라그산 당량)·유리 엘라그산 등 페놀 7개 군","part":"열매(동결건조, 씨·껍질 포함)",
  "content":"메탄올 추출물(동결건조 열매 6 g → 4.5 mL) 기준 엘라지탄닌 7251 μg/mL, 엘라그산 1067 μg/mL, 플라반올 3822 μg/mL, 하이드록시신남산 1757 μg/mL, 안토시아닌 3 μg/mL[6]",
  "method":"UPLC-PDA/FLR",
  "conditions":E(instrument="Waters ACQUITY UPLC, 광다이오드 배열(PDA)·형광(FLR) 검출기", column="Waters HSS T3 C18, 1.7 μm, 2.1 × 150 mm", mobile_phase="물/0.5% 포름산, 아세토니트릴/0.5% 포름산", gradient="기울기 프로그램(세부는 선행 방법 인용, 확인 못함)", flow="0.5 mL/min", detection="엘라그산 365 nm; 엘라지탄닌은 엘라그산으로 280 nm; 안토시아닌 520 nm(시아니딘-3-글루코사이드); 플라보놀 365 nm(루틴); 하이드록시신남산 320 nm(클로로겐산); 하이드록시벤조산 280 nm(갈산); 플라반-3-올 FLR(프로시아니딘 B2)", injection="5 μL", sample_prep="동결건조 열매 6 g 분쇄(씨·껍질 포함) → 메탄올 25 mL로 2회 추출(1분 교반, 10분 원심분리) → 30 °C 감압 농축 → 물 4.5 mL; 분석 전 20% 메탄올에 녹여 0.2 μm 여과; 3반복·이중 주입", standard="군별 대표 표준물질 당량(엘라그산·시아니딘-3-글루코사이드·루틴·클로로겐산·갈산·프로시아니딘 B2)"),
  "rationale":"엘라지탄닌이 진들딸기 폴리페놀의 주된 군이어서 엘라그산 당량으로 지표화함; 전문 확인, 검량·검출한계·회수율은 본문에 없음[6].",
  "source":[6],"url":"https://doi.org/10.18632/oncotarget.9724","source_kind":"paper"},
 {"role":"literature","compound":"Cyanidin 3-glucoside","compound_ko":"총 안토시아닌(시아니딘-3-글루코사이드 당량)","part":"열매(알래스카 포인트호프 야생, 냉동)",
  "content":"0.01 mg/g 생중량; 시아니딘-3-글루코사이드·시아니딘-3-아라비노사이드·페투니딘-3-글루코사이드·말비딘-3-갈락토사이드 확인[7]",
  "method":"HPLC-UV/Vis(520 nm)",
  "conditions":E(instrument="Agilent 1100 HPLC", column="Supelcosil LC-18, 250 × 4.6 mm, 5 μm(Supelco)", mobile_phase="A: 5% 포름산 수용액, B: 100% 메탄올", gradient="B 10→15→20→25→30→60→10→10%(0, 5, 15, 20, 25, 45, 47, 60분)", flow="1 mL/min", detection="520 nm", sample_prep="냉동 열매를 산성 메탄올(0.3% TFA, 2:1 v/w)로 균질화·여과 → 감압 농축 → 에틸아세테이트 분배 → Amberlite XAD-7 흡착 후 산성 메탄올 용출 → 동결건조(페놀 풍부 추출물); 5 mg/mL 메탄올, 0.45 μm 나일론 여과", standard="시아니딘-3-글루코사이드 당량(총 봉우리 면적 합)"),
  "rationale":"노란 열매라 안토시아닌이 조사한 알래스카 베리 중 가장 적어 붉은 산딸기속 열매와 구별되는 특징이 됨; 전문 확인, 검량·검출한계·회수율은 본문에 없음[7].",
  "source":[7],"url":"https://doi.org/10.1021/jf902693r","source_kind":"paper"},
 {"role":"literature","compound":"beta-Carotene","compound_ko":"총 카로티노이드(분광법; β-카로틴은 TLC 표준품으로 확인)","part":"열매(핀란드 시판·폴란드 재배, 동결건조 분말)",
  "content":"분광법 46.01–46.27 mg/100 g 건조중량; TLC(β-크립토잔틴으로 환산) 54.78–54.88 mg/100 g[8]",
  "method":"UV-Vis 분광법(450 nm)·TLC 정량",
  "conditions":E(instrument="Shimadzu 분광광도계; TLC: Camag TLC Visualizer·winCATS", column="TLC Si60 판(Merck), 5 × 20 cm로 잘라 120 °C에서 20분 활성화", mobile_phase="TLC: n-헵탄–에틸아세테이트–아세톤(65:20:20)", temp="TLC 전개 4 ± 1 °C, 습도 60–65%, 차광", detection="450 nm(비흡광계수 A1cm% 2500으로 계산)", sample_prep="분말 0.5 g + 헥산–아세톤(1:1) 25 mL(TBHQ 첨가 또는 무첨가), 차광 초음파 15분 → 3000 rpm 5분 원심분리 → 실온 감압 건고 → 에틸아세테이트 1 mL → 0.22 µm 여과", standard="TLC: 제아잔틴·루테인·β-크립토잔틴·β-카로틴(Extrasynthese)"),
  "rationale":"조사한 산딸기속 열매 중 카로티노이드 함량이 가장 높아 노란색 열매의 특징 성분임; 전문 확인, 검출한계·회수율은 확인 못함[8].",
  "source":[8],"url":"https://doi.org/10.3390/antiox14121438","source_kind":"paper"},
 {"role":"literature","compound":"Tormentic acid","compound_ko":"토르멘트산(오환성 트라이테르페노이드산)·β-시토스테롤","part":"잎·꽃받침·열매",
  "content":"토르멘트산 약 190–1800 μg/g 건조중량, 그 수산화 유도체 약 3.1–470 μg/g, 아미린 0.76–110 μg/g, β-시토스테롤 62–750 µg/g(부위별)[10]",
  "method":"HPLC-MS/MS(MRM 정량 및 전구이온 스캔)",
  "conditions":E(),
  "rationale":"중간 극성 분획에서 가장 많은 트라이테르페노이드산; 초록만 확인해 분석 조건은 전문 확인 못함[10].",
  "source":[10],"url":"https://doi.org/10.1080/14786419.2024.2417837","source_kind":"paper"},
]
d = {"slug":"rubus-chamaemorus","name_ko":"진들딸기","name_en":"Cloudberry","scientific_name":"Rubus chamaemorus L.",
     "aliases":["장지딸기","진들딸기열매","클라우드베리","Cloudberry","Baked-apple berry","Bakeapple","Chamaemorus norwegica Greene"],
     "sections":sections,"compounds":compounds,"markers":[],"nutrients":[],"assays":assays,"production":[],"world":[],"gi":[],"orgs":[],"sources":sources}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in sections: print(s["key"], len(s["body"]))
