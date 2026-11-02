import json
A="2026-11-02"
def P(n,t,url,pub="PubMed"): return {"n":n,"title":t,"url":url,"publisher":pub,"accessed":A}
sources=[
{"n":1,"title":"식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 아라자열매(Eugenia stipitata Mac Vaugh), 식품원료(A코드), 사용가능, 사용가능부위: 열매; 같은 속 브라질리언체리열매(Eugenia brasiliensis / Eugenia dombeyi)·Surinam-cherry열매(Eugenia uniflora) 행과 이름이 겹치는 Strawberry guave열매(Psidium cattleianum)·브라질구와바열매(Psidium araca 포함) 행 대조","url":"https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020","publisher":"식품의약품안전처","accessed":"2026-10-13"},
P(2,"Arazá: Eugenia stipitata Mc Vaught as a Potential Functional Food — Foods 2024 (체계적 리뷰, PMC 전문 확인) (PMID 39123500)","https://doi.org/10.3390/foods13152310"),
P(3,"Five Underutilized Ecuadorian Fruits and Their Bioactive Potential as Functional Foods and in Metabolic Syndrome: A Review — Molecules 2024 (PMC 전문 확인) (PMID 38930969)","https://doi.org/10.3390/molecules29122904"),
P(4,"Extract of Araçá-Boi and Its Major Phenolic Compound, Trans-Cinnamic Acid, Reduce Viability and Inhibit Migration of Human Metastatic Melanoma Cells — Nutrients 2024 (PMC 전문 확인) (PMID 39275245)","https://doi.org/10.3390/nu16172929"),
P(5,"Physicochemical Properties and Effects of Fruit Pulps from the Amazon Biome on Physiological Parameters in Rats — Nutrients 2021 (PMC 전문 확인, 표 수치는 본문에 없음) (PMID 33924791)","https://doi.org/10.3390/nu13051484"),
P(6,"Bioactive Potential of Arazá (Eugenia stipitata) Seeds: Hypoglycemic, Antiradical, and Nutritional Properties — Plants 2025 (PMC 전문 확인) (PMID 40508336)","https://doi.org/10.3390/plants14111662"),
P(7,"Determination of carotenoids, total phenolic content, and antioxidant activity of Arazá (Eugenia stipitata McVaugh), an Amazonian fruit — J Agric Food Chem 2012 (초록만 확인) (PMID 22519635)","https://doi.org/10.1021/jf205347f"),
P(8,"Chemical characterization of Eugenia stipitata: A native fruit from the Amazon rich in nutrients and source of bioactive compounds — Food Res Int 2021 (초록만 확인) (PMID 33509473)","https://doi.org/10.1016/j.foodres.2020.109904"),
P(9,"Comprehensive characterization of bioactive phenols from new Brazilian superfruits by LC-ESI-QTOF-MS, and their ROS and RNS scavenging effects and anti-inflammatory activity — Food Chem 2019 (초록만 확인) (PMID 30658745)","https://doi.org/10.1016/j.foodchem.2018.12.106"),
P(10,"Volatile composition of some Brazilian fruits: umbu-caja, camu-camu, Araça-boi (Eugenia stipitata), and Cupuaçu — J Agric Food Chem 2000 (초록만 확인) (PMID 10775382)","https://doi.org/10.1021/jf9900074"),
P(11,"Volatile Constituents of Some Myrtaceous Edible and Medicinal Fruits from the Brazilian Amazon — Foods 2024 (초록만 확인) (PMID 38790790)","https://doi.org/10.3390/foods13101490"),
P(12,"Analyses of several seed viability markers in individual recalcitrant seeds of Eugenia stipitata McVaugh with totipotent germination — Plant Biol 2016 (초록만 확인) (PMID 27094237)","https://doi.org/10.1111/plb.12466"),
P(13,"Diversity of Anastrepha spp. (Diptera: Tephritidae) and associated braconid parasitoids from native and exotic hosts in southeastern Bahia, Brazil — Environ Entomol 2010 (초록만 확인) (PMID 22546440)","https://doi.org/10.1603/EN10079"),
P(14,"Chemical composition and biological activities of the essential oil from Eugenia stipitata McVaugh leaves — Nat Prod Res 2022 (초록만 확인) (PMID 36469681)","https://doi.org/10.1080/14786419.2022.2151008"),
P(15,"Insecticidal activity of essential oil from leaves of Eugenia stipitata McVaugh against Aedes aegypti — Parasitol Int 2023 (초록만 확인) (PMID 37884077)","https://doi.org/10.1016/j.parint.2023.102820"),
P(16,"Essential oil from Eugenia stipitata McVaugh leaves exhibits antinociceptive effect via opioid receptor activation — Inflammopharmacology 2026 (초록만 확인) (PMID 41770502)","https://doi.org/10.1007/s10787-026-02148-y"),
P(17,"Araçá-Boi Extract and Gallic Acid Reduce Cell Viability and Modify the Expression of Tumor Suppressor Genes and Genes Involved in Epigenetic Processes in Ovarian Cancer — Plants 2025 (초록만 확인) (PMID 40508345)","https://doi.org/10.3390/plants14111671"),
P(18,"Understanding the gastrointestinal behavior of phytochemicals and antioxidants from araçá-boi (Eugenia stipitata McVaugh) extract: An in vitro and in silico approach — Food Chem 2025 (초록만 확인) (PMID 40220439)","https://doi.org/10.1016/j.foodchem.2025.144254"),
P(19,"Influence of high-intensity ultrasound on color, chemical composition and antioxidant properties of araçá-boi pulp — Food Chem 2021 (초록만 확인) (PMID 32858434)","https://doi.org/10.1016/j.foodchem.2020.127747"),
P(20,"Alcoholic beverages from araçá-boi fruit: quantification of antioxidant compounds by NMR ERETIC2 — J Food Sci Technol 2020 (초록만 확인) (PMID 33087984)","https://doi.org/10.1007/s13197-020-04721-x"),
P(21,"Microparticles of Eugenia stipitata pulp obtained by spray-drying guided by DSC: An analysis of bioactivity and in vitro gastrointestinal digestion — Food Chem 2021 (초록만 확인) (PMID 32712488)","https://doi.org/10.1016/j.foodchem.2020.127557"),
P(22,"Physical and Chemical Properties of 70% Cocoa Dark Chocolate Mixed with Freeze-Dried Arazá (Eugenia stipitata) Pulp — Prev Nutr Food Sci 2022 (초록만 확인) (PMID 36721755)","https://doi.org/10.3746/pnf.2022.27.4.474"),
P(23,"Wild Brazilian species of Eugenia genera (Myrtaceae) as an innovation hotspot for food and pharmacological purposes — Food Res Int 2019 (리뷰, 초록만 확인) (PMID 31108783)","https://doi.org/10.1016/j.foodres.2019.03.018"),
P(24,"First record of in vitro formation of ectomycorrhizae in Psidium cattleianum Sabine, a native Myrtaceae of the Brazilian Atlantic Forest — PLoS One 2018 (초록만 확인; 'Red Araza' 이름 확인용) (PMID 29738553)","https://doi.org/10.1371/journal.pone.0196984"),
P(25,"Valorization Alternatives of Tropical Forest Fruits Based on the Açai Processing in Small Communities — Foods 2023 (초록만 확인) (PMID 37297474)","https://doi.org/10.3390/foods12112229"),
P(26,"Nutritional and Phytochemical Profile and Potential Anticancer Benefits of Amazonian Exotic Fruits — Nutr Rev 2026 (리뷰, 초록만 확인) (PMID 41739529)","https://doi.org/10.1093/nutrit/nuaf307"),
]

S=[]
def sec(k,t,b): S.append({"key":k,"title":t,"body":b})
sec("overview","한눈에 보기",
"아라자(Eugenia stipitata McVaugh)는 도금양과(Myrtaceae) Eugenia 속의 작은 나무로, 아마존 지역이 원산인 노란 열매 과일이며 브라질에서는 araçá-boi, 에콰도르에서는 membrillo라고도 부른다[2]. 식약처 「식품원료 목록」에는 원료명 '아라자열매', 학명 'Eugenia stipitata Mac Vaugh'로 올라 있으며, 식품에 쓸 수 있는 원료(사용가능)이고 사용 조건은 '사용가능부위 : 열매'로 열매만 쓸 수 있다[1]. 이 종을 원재료로 하는 건강기능식품 고시형 원료는 확인하지 못함.\n\n"
"익은 열매는 껍질이 얇고 밝은 노란색이며, 과육은 즙이 많고 향이 강하지만 신맛이 매우 강해(pH 2.4) 날로 먹기보다 주스·아이스크림·젤리 등으로 가공해 먹는다[2]. 열매에는 비타민 C, 페놀 화합물, 루테인 같은 카로티노이드가 들어 있다고 정리되어 있다[2, 7]. 브라질 토착 과일 5종을 함께 분석한 연구는 아라자를 포함한 과일 추출물이 활성산소·활성질소를 없애고 생쥐에서 호중구 유입을 줄였다고 보고했다[9]. 아마존 과일의 항암 가능성을 다룬 리뷰도 아라자를 포함했지만 근거는 시험관·동물 연구에 머문다[26]. 사람 대상 임상시험은 확인하지 못함.")
sec("history","역사와 이름",
"아라자는 페루 아마존을 기원지로 보며, 오늘날 콜롬비아와 브라질 국경 지역에 사는 동부 투카노(Eastern Tucanos) 사람들이 재배화하고 퍼뜨린 것으로 보인다고 정리되어 있다[3]. 현재 에콰도르·콜롬비아·브라질·페루·볼리비아에서 재배된다[2]. 콜롬비아 아마존에서는 새롭고 독특한 맛 때문에 안데스 지역 경제에 가치가 큰 과일로 여겨졌다[7].\n\n"
"이름은 나라마다 달라 스페인어권에서는 arazá, 브라질에서는 araçá-boi, 에콰도르에서는 membrillo라고 부른다[2]. 다만 'araçá'라는 이름은 구아바 속(Psidium)의 다른 과일에도 쓰여 이름만으로 자료를 찾으면 섞일 수 있다[3]. 지역 공동체에서는 이 식물을 입·목의 염증, 복통, 상처, 열, 설사 등에 전통적으로 써 왔다고 하나, 이런 전통 이용을 다룬 연구는 주로 잎 정유를 대상으로 했다[16]. 에콰도르에서는 아라자가 식품 가공에서 경제적으로 중요한 과일로 소개된다[3].")
sec("biology","식물학적 특징",
"아라자는 높이 2.5–15.0 m로 자라고 가지가 많이 갈라진 수관을 가진 중간 크기 나무다[2]. 열매는 구형에서 둥근 장과로 평균 지름이 12 cm라고 정리되어 있고 무게는 최대 80 g까지 나가며, 다른 정리에서는 평균 30–80 g이라고 했다[2]. 껍질은 매끈하고 얇으며 덜 익으면 연녹색, 다 익으면 밝은 노란색이고, 속에는 씨가 4–10개 있으며 이를 흰색–노란색의 즙 많은 과육이 둘러싼다[2]. 열매 껍질에 잔털이 있고 과육 pH가 2.28이라고 보고한 연구도 있다[4].\n\n"
"열매는 후숙(클라이맥터릭)형이며 한 해에 세 번 수확한다고 정리되어 있다[2]. 과육은 수분이 90%를 넘고 지방이 0.4% 미만이며, 건물 기준으로 당이 49.2%이고 그중 과당 비중이 크다[2]. 씨는 열매 부피의 30%, 생중량의 22%, 건물의 84%를 차지한다[6]. 씨는 건조에 약한 난저장성(recalcitrant) 종자로, 분화가 덜 된 씨 하나를 여러 조각으로 잘라도 조각마다 싹이 터 묘가 된다[12].")
sec("related_species","이름과 가까운 종",
"Eugenia 속에는 약 400종이 기재되어 있으며, 그 가운데 Eugenia uniflora(피탕가) 등 여러 종이 열매와 이차대사산물 자원으로 연구되었다[2]. 브라질 야생 Eugenia 과일 리뷰는 E. uniflora, E. stipitata, E. brasiliensis, E. pyriformis, E. dysenterica를 함께 다루므로, 이 자료는 그중 E. stipitata 연구만 골라 썼다[23]. 식약처 목록에도 같은 속의 '브라질리언체리열매(Eugenia brasiliensis / Eugenia dombeyi)'와 'Surinam-cherry열매(Eugenia uniflora)'가 아라자열매와 별도 원료로 올라 있다[1].\n\n"
"'araçá'라는 이름은 구아바 속(Psidium) 과일에도 쓰인다[3]. 예를 들어 스트로베리 구아바(Psidium cattleianum)는 영어로 'Red Araza'라고 불리기도 한다[24]. 식약처 목록에는 이 종이 'Strawberry guave열매(Psidium littorale / Psidium cattleianum)'로, Psidium araca가 포함된 '브라질구와바열매'가 또 다른 원료로 올라 있어 아라자와 구분해야 한다[1]. 같은 아마존 도금양과 과일인 카무카무(Myrciaria dubia)도 향기 성분 비교 연구에서 아라자와 함께 다뤄졌으나 다른 속의 과일이다[11]. 식약처 목록의 학명 저자 표기 'Mac Vaugh'는 논문에서 흔히 'McVaugh'로 적는다[1, 16].")
sec("cultivation","재배와 산지",
"아라자는 아마존 원산으로 브라질·콜롬비아·페루·볼리비아·에콰도르에 분포하며, 이들 나라에서 재배된다[2]. 에콰도르 리뷰는 재배와 수확 후 처리에 세심한 관리가 필요한 약한 과일이라고 했고, 두 아종 가운데 하나가 재배에 더 알맞다고 적었다[3]. 열매 시장성은 일반 과일보다 낮아 주로 지역 상점과 소규모 가공업체에서 거래되며, 농촌 가구의 주요 소득원 가운데 하나라고 정리되어 있다[2]. 생과로는 잘 먹지 않고, 코스타리카와 콜롬비아 등에서 냉동 과육 형태로 가공·수출된다[6].\n\n"
"브라질에서는 아마존 밖인 바이아주 농장에서도 열매를 수확해 연구에 썼고[4], 혼도니아주의 가공업체가 냉동 과육을 생산했다[5]. 바이아주 조사에서는 Anastrepha fraterculus·A. sororcula·A. zenildae 세 종의 과실파리가 아라자 열매를 가해한 것이 브라질에서 처음 기록되었다[13]. 수확 후 12일 저장하는 동안 비타민 C가 껍질에서 약 80%, 과육에서 약 90% 줄었다는 보고가 있어 저장성이 낮다[2]. 국내 재배·생산 통계와 국내 지리적 표시 등록은 확인하지 못함.")
sec("processing","가공과 이용",
"과육은 신맛이 강해 날로 잘 먹지 않고 주스, 아이스크림, 젤리 등으로 만들며, 와인·건조 과육·분무건조 미세입자·동결건조 분말·과일 넥타·과자·초콜릿 등의 제품 연구가 있다[2]. 과육을 65·73·80 °C로 살균하면 비타민 C가 각각 2·4·12% 줄었고, 80 °C 처리 과육은 냉동 두 달 뒤에도 처음 비타민 C의 82.9%를 유지했다[2]. 고강도 초음파(7000 J/g)로 처리한 과육은 처리하지 않은 과육보다 비타민 C가 46.5% 늘었다고 보고되었다[19].\n\n"
"말토덱스트린(1:9)으로 100 °C에서 분무건조한 미세입자는 시험관 소화 뒤에도 총폴리페놀의 61%를 유지했다[21]. 효모로 발효한 아라자 술은 거르지 않았을 때 알코올 13.9 °GL, 거른 뒤 12.7 °GL이었다[20]. 다크초콜릿에 동결건조 과육을 2%까지 넣어도 초콜릿의 성질은 달라지지 않았다[22]. 과육 가공 뒤 남는 씨는 가공 과일 1톤당 약 220 kg 나오는 부산물로, 이를 이용하려는 연구가 있다[6]. 껍질 추출물은 총페놀 276.6 mg 갈산당량/100 g(원료 기준)으로 아사이·노니보다 높은 값을 보였다[25]. 국내 「식품 등의 생산실적」에서 아라자를 원료로 한 건강기능식품 품목은 확인하지 못함.")
sec("genetics","유전 정보",
"아라자의 염색체 수, 엽록체·핵 유전체 해독, 분자 표지 연구는 이번 조사에서 확인하지 못함. 에콰도르 리뷰는 이 종에 두 아종이 있고 그중 하나가 재배에 더 알맞다고 정리했다[3]. 열매 성분은 익은 정도, 토양·기후 조건, 산지에 따라 달라진다고 보고되어, 연구마다 함량 차이가 크다[2].\n\n"
"씨 하나를 네 조각으로 나눠 수분 함량·생존력·글루타티온을 함께 잰 연구는, 씨 수분이 높을 때 생존력이 유지되고 글루타티온 반쪽전지 환원전위가 −215 mV보다 덜 음의 값이었다고 보고했다[12]. 수분이 낮은 상태로 저장하면 글루타티온이 줄고 씨가 죽었으며, 연구진은 이 종을 난저장성 종자 연구 모델로 추천했다[12]. 콜롬비아산 열매는 루테인·β-크립토잔틴·제이녹산틴 위주의 독특한 카로티노이드 조성을 보여, 연구진은 이것이 원산지·진위 판별에 쓰일 수 있다고 제안했다[7].")
sec("safety","안전성",
"식약처 「식품원료 목록」에서 아라자는 열매에 한해 식품원료로 쓸 수 있으며, 잎 등 다른 부위는 허용 부위가 아니다[1]. 식약처·농촌진흥청 등 국내 공공기관의 아라자 알레르기·잔류·독성 정보는 확인하지 못함. 과육은 pH 2.4 정도로 산도가 매우 높아 보통 날로 먹지 않는다[2].\n\n"
"쥐(Wistar)에게 아라자 과육을 체중 100 g당 0.3214 mL씩 30일 동안 먹인 실험(성인이 45% 과육 주스 500 mL를 마시는 양에 해당)에서, 대조군과 비교해 적혈구용적률·혈당·콜레스테롤·간 효소(TGP)·크레아티닌·요소의 유의한 변화는 관찰되지 않았다[5]. 같은 실험에서 간 수치(TGO) 상승과 사망은 다른 과일(biri-biri) 군에서만 보고되었다[5]. 씨 추출물은 사람 혈액세포 생존율 84.29%로 뚜렷한 세포독성을 보이지 않았지만, 씨는 허용 부위가 아니다[1, 6]. 열매 추출물이 흑색종·난소암 세포 생존을 낮춘 결과는 세포 실험이며, 사람에서의 효과로 볼 수 없다[4, 17]. 잎 정유는 유데스몰 이성질체 두 종(15.28%·10.85%)과 엘레몰(10.21%)이 주성분이고[14], 모기 유충을 죽이는 활성(LC50 0.34 mg/mL)이 있어 식품 부위인 열매 자료와 구분해야 한다[15].")

C=[
{"name":"trans-Cinnamic acid","name_ko":"트랜스-신남산","class":"페놀산(하이드록시신남산 계열 모핵)","role":"marker","part":"열매 가식부(과육+껍질) 에탄올 추출물","content_text":"155.79 ± 0.32 µg/g 추출물(건물), HPLC-DAD로 정량한 11종 가운데 가장 많음[4]; 동결건조 과육 126.58 ± 2.54 mg/100 g 건물(리뷰 정리값)[2]","activity_ko":"흑색종 세포(SK-MEL-28) 생존·이동 억제, 세포 내 활성산소 감소(시험관)[4]; 소화 뒤 주성분으로 남아 NF-κB 등과 결합 예측(인실리코)[18]","source":[2,4,18]},
{"name":"Quercetin 3-O-galactoside","name_ko":"퀘르세틴-3-O-갈락토사이드(하이퍼로사이드)","class":"플라보놀 배당체","role":"bioactive","part":"열매 가식부 추출물","content_text":"151.32 ± 1.86 µg/g 추출물(건물)[4]","activity_ko":"추출물 항산화 성분의 하나(시험관)[4]","source":[4]},
{"name":"Quercitrin","name_ko":"퀘르시트린(퀘르세틴-3-O-람노사이드)","class":"플라보놀 배당체","role":"bioactive","part":"열매 가식부 추출물","content_text":"116.27 ± 0.27 µg/g 추출물(건물)[4]","activity_ko":"추출물 항산화 성분의 하나(시험관)[4]","source":[4]},
{"name":"Syringic acid","name_ko":"시링산","class":"페놀산(하이드록시벤조산)","role":"bioactive","part":"열매 가식부 추출물","content_text":"113.07 ± 0.74 µg/g 추출물(건물)[4]","activity_ko":"추출물 페놀산 가운데 두 번째로 많음[4]","source":[4]},
{"name":"Gallic acid","name_ko":"갈산","class":"페놀산(하이드록시벤조산)","role":"bioactive","part":"열매(과육)·발효주","content_text":"동결건조 과육 166.02 ± 3.39 mg/100 g 건물(리뷰 정리값)[2]; 아라자 발효주 최대 390.0 µM(NMR 정량)[20]","activity_ko":"난소암 세포(NCI/ADR-RES·OVCAR3) 생존 감소, 6–48 µg/mL(시험관)[17]","source":[2,17,20]},
{"name":"Lutein","name_ko":"루테인","class":"카로티노이드(잔토필)","role":"bioactive","part":"열매 껍질·과육","content_text":"총카로티노이드 껍질 2484 ± 421 µg/100 g, 과육 806 ± 348 µg/100 g(생중량); 루테인·β-크립토잔틴·제이녹산틴이 주성분[7]","activity_ko":"망막 건강과 관련된 카로티노이드 공급원으로 제시[7]","source":[7]},
{"name":"beta-Cryptoxanthin","name_ko":"β-크립토잔틴","class":"카로티노이드(잔토필, 프로비타민 A)","role":"bioactive","part":"열매 껍질·과육","content_text":"주요 카로티노이드의 하나(개별 함량은 초록에 없음)[7]; 동결건조 껍질 153 ± 32 µg/g, 과육 92 ± 38 µg/g(리뷰 정리값)[2]","activity_ko":"프로비타민 A 활성 카로티노이드[7]","source":[2,7]},
{"name":"Zeinoxanthin","name_ko":"제이녹산틴","class":"카로티노이드(잔토필)","role":"bioactive","part":"열매 껍질·과육","content_text":"잠정 동정, 주요 카로티노이드의 하나[7]; 동결건조 껍질 187 ± 24 µg/g, 과육 54 ± 22 µg/g(리뷰 정리값)[2]","activity_ko":"아라자 특유의 카로티노이드 조성을 이뤄 진위 판별 지표로 제안됨[7]","source":[2,7]},
{"name":"Ascorbic acid","name_ko":"비타민 C(아스코르브산)","class":"비타민","role":"nutrient","part":"과육·껍질","content_text":"과육 127.8 mg/100 g, 껍질 184.8 mg/100 g; 다른 보고는 과육 9.5 ± 0.8 mg/100 g(생중량) 등으로 차이가 큼(리뷰 정리값)[2]","activity_ko":"수확 후 12일 저장 중 껍질 약 80%, 과육 약 90% 감소[2]","source":[2]},
{"name":"Malic acid","name_ko":"사과산","class":"유기산","role":"nutrient","part":"과육","content_text":"244.5 ± 4.8 µmol/g; 숙신산 39.5 ± 3.2, 시트르산 3.3 ± 0.1 µmol/g(리뷰 정리값)[2]","activity_ko":"과육의 강한 신맛을 이루는 주된 유기산[2]","source":[2]},
{"name":"Sucrose","name_ko":"자당·과당","class":"당류","role":"nutrient","part":"열매 가식부","content_text":"자당 38.01 ± 2.94 mg/g, 과당 17.58 ± 0.80 mg/g, 말토테트라오스 1.63 ± 0.09 mg/g(건물)[8]","activity_ko":"과육 당 조성(과육 건물의 당 49.2%, 과당 비중 큼)[2, 8]","source":[2,8]},
{"name":"Potassium","name_ko":"칼륨","class":"무기질","role":"nutrient","part":"열매 가식부","content_text":"827.66 ± 14.51 mg/100 g(건물); 칼슘 107.16 ± 1.54, 마그네슘 75.65 ± 1.28 mg/100 g(건물)[8]","activity_ko":"가식부에 씨보다 무기질이 많음[8]","source":[8]},
{"name":"Myricetin","name_ko":"미리세틴","class":"플라보놀","role":"bioactive","part":"과육","content_text":"생과육 17 mg/100 g이라는 정리[3]; 산가수분해 과육 메탄올 추출물에서는 0.17 µg/g(생중량)으로 보고되어 값 차이가 큼[4]","activity_ko":"항산화 플라보노이드[3]","source":[3,4]},
{"name":"Germacrene D","name_ko":"저마크렌 D 등 향기 성분","class":"세스퀴테르펜(휘발성)","role":"bioactive","part":"열매","content_text":"아라자 휘발 성분 30종 가운데 세스퀴테르펜이 가장 많고 저마크렌 D 비율이 가장 높음[10]; 다른 시료 과육 농축물은 α-피넨 17.5%, 시트로넬릴 부타노에이트 15.6%, 포고스톨 13.5%[11]","activity_ko":"열매의 독특한 향을 이룸[10, 11]","source":[10,11]},
{"name":"Epicatechin gallate","name_ko":"에피카테킨 갈레이트(씨)","class":"플라반-3-올","role":"bioactive","part":"씨(허용 부위 아님)","content_text":"씨에서 정량한 페놀 7종 가운데 가장 많음, 2.3 mg/kg; 다음은 p-하이드록시벤조산 1.1 mg/kg(원문에 EGCG 표기 혼용)[6]","activity_ko":"씨 추출물 α-아밀레이스 억제 IC50 47.06 µg/mL, α-글루코시데이스 49.99 µg/mL(시험관)[6]","source":[6]},
]

nutrients=[
{"form":"과육","basis":"리뷰가 정리한 값(생·건물 기준 혼재, 원 출처별 차이); 국가표준식품성분표 수록 여부는 확인하지 못함","items":[
 {"name":"수분","value":">90","unit":"%"},{"name":"지방","value":"<0.4","unit":"%"},{"name":"당류(건물 기준)","value":49.2,"unit":"%"},{"name":"비타민 C","value":127.8,"unit":"mg/100 g"},{"name":"pH","value":2.4,"unit":""}],"source":[2]},
{"form":"열매 가식부(건물)","basis":"건물 100 g당(브라질 시료, 초록 값)","items":[
 {"name":"칼륨","value":827.66,"unit":"mg"},{"name":"칼슘","value":107.16,"unit":"mg"},{"name":"마그네슘","value":75.65,"unit":"mg"}],"source":[8]},
]

def cond(**k):
    base={x:"" for x in ["instrument","column","mobile_phase","gradient","flow","temp","detection","injection","sample_prep","standard","linearity","lod","loq","recovery"]}
    base.update(k); return base
assays=[
{"role":"literature","compound":"trans-Cinnamic acid (and 10 other phenolics)","compound_ko":"트랜스-신남산 등 페놀 화합물 11종","part":"열매 가식부(과육+껍질, 브라질 바이아주산, 동결건조)","content":"트랜스-신남산 155.79 ± 0.32 µg/g 추출물(건물); 11종 합계 766.44 ± 4.53 µg/g 추출물(건물)[4]","method":"HPLC-DAD","conditions":cond(
 instrument="Dionex UltiMate 3000(다이오드 어레이 검출기)",
 column="역상 C18, 120 Å, 250 × 4.6 mm, 입자 5 μm, 32 °C",
 mobile_phase="A: 0.1% 포름산 수용액, B: 아세토나이트릴(HPLC 등급)",
 gradient="B 5%(5분) → 5–29%(22분) → 35%(6분) → 35–50%(12분) → 95%(5분) → 5%(10분), 선형",
 flow="0.5 mL/min", temp="32 °C",
 detection="DAD 200–800 nm 기록, 정량은 화합물별 260·280·320·360 nm",
 injection="20 μL",
 sample_prep="동결건조·분쇄(24메시) 시료 1 g을 에탄올:물(80:20) 15 mL로 초음파(25 kHz, 120 W) 10분 추출, 4000×g 5분 원심분리, 3회 반복 후 합쳐 감압 농축·동결건조, −20 °C 보관",
 standard="페놀 표준품 33종(순도 ≥96%), 머무름 시간과 스펙트럼 비교로 동정·정량"),
 "rationale":"추출물에서 가장 많은 페놀 화합물이어서 연구진이 단독 비교 물질로 골랐고 열매 페놀 지표 후보가 됨; 검량선 범위·검출한계·회수율은 원문에 없음[4].","source":[4],"url":"https://doi.org/10.3390/nu16172929","source_kind":"paper"},
{"role":"literature","compound":"Lutein (total carotenoids)","compound_ko":"루테인 등 카로티노이드","part":"익은 열매 껍질·과육(콜롬비아산)","content":"총카로티노이드 껍질 2484 ± 421 µg/100 g, 과육 806 ± 348 µg/100 g(생중량); 루테인·β-크립토잔틴·제이녹산틴이 주성분[7]","method":"HPLC-PDA, APcI-MS/MS(동정)","conditions":cond(detection="광다이오드 어레이 검출기(PDA)와 대기압화학이온화(APcI) 질량분석(MS/MS)"),
 "rationale":"노란 열매색을 내는 주성분이고 조성이 독특해 진위 판별 지표로 제안됨; 전문 확인 못함(초록만)[7].","source":[7],"url":"https://doi.org/10.1021/jf205347f","source_kind":"paper"},
{"role":"literature","compound":"Total phenolics (gallic acid equivalents)","compound_ko":"총페놀(갈산 당량)","part":"냉동 과육(브라질 혼도니아주 가공업체, 2016년)","content":"아라자 과육 144.0(본문 표기 'g EAG/100 g', 분류 기준 100–500 mg GAE/100 g의 '중간' 군); DPPH 항산화능 6.09 μmol Trolox/g[5]","method":"Folin–Ciocalteu 분광광도법","conditions":cond(instrument="Beckman DU-640 분광광도계",detection="흡광도 720 nm",sample_prep="−18 °C 냉동 보관 과육에서 기존 방법(문헌)대로 페놀 추출, 3회 반복",standard="갈산, 검량선 72–200 μg/mL"),
 "rationale":"과육의 항산화 성분 수준을 비교하는 기본 지표로 쓰였음; 검출한계·회수율은 원문에 없음[5].","source":[5],"url":"https://doi.org/10.3390/nu13051484","source_kind":"paper"},
]

d={"slug":"eugenia-stipitata","name_ko":"아라자","name_en":"Arazá (araçá-boi)","scientific_name":"Eugenia stipitata McVaugh",
 "aliases":["아라자열매","Arazá","Araza","Araçá-boi","Araca-boi","Membrillo(에콰도르)","Eugenia stipitata Mac Vaugh"],
 "sections":S,"compounds":C,"markers":[],"nutrients":nutrients,"assays":assays,"production":[],"world":[],"gi":[],"orgs":[],"sources":sources}
# use [26]? ensure used
json.dump(d,open('/home/user/hfoodguide-wave3/docs/materials/eugenia-stipitata/dossier.json','w'),ensure_ascii=False,indent=1)
for s in S: print(s['key'],len(s['body']))
