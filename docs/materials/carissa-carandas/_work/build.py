import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
A = "2026-11-02"
PM = "PubMed"
def doi(x): return "https://doi.org/" + x
S = [
 (1, "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 카란다열매(Carissa carandas L. / Carissa congesta Wight; Sri Lankan Damson, Kala, Mahakaramba, Karanda), 사용가능, 사용가능부위: 열매; 같은 속의 Heen karamba열매(Carissa spinarum)·나탈플럼열매(Carissa grandiflora (E.May.) A.DC, Natal plum) 행 대조", "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "식품의약품안전처", "2026-10-13"),
 (2, "Plants of the World Online — Carissa carandas L. (승인명, 원산지·도입 지역, 이명) (POWO 페이지는 이 환경에서 열지 못해 WebSearch 요약으로만 확인)", "https://powo.science.kew.org/results?q=Carissa%20carandas", "Royal Botanic Gardens, Kew", A),
 (3, "Phytochemistry, Traditional Uses, Pharmacology, Nutritional Composition, and Agrotechnology of Underutilized Wild Fruit Plant Carissa carandas L. — Chem Biodivers 2025 (PMID 40192261, 초록만 확인)", doi("10.1002/cbdv.202402193"), PM, A),
 (4, "Carissa carandas L. - phyto-pharmacological review — J Pharm Pharmacol 2020 (PMID 32729204, 초록만 확인)", doi("10.1111/jphp.13328"), PM, A),
 (5, "Effects of Carissa carandas Linn. Fruit, Pulp, Leaf, and Seed on Oxidation, Inflammation, Tyrosinase, Matrix Metalloproteinase, Elastase, and Hyaluronidase Inhibition — Antioxidants (Basel) 2021;10(9):1345 (PMID 34572978, PMC8470603, 전문 확인)", doi("10.3390/antiox10091345"), PM, A),
 (6, "Bioactivity Profiling and Phytochemical Analysis of Carissa carandas Extracts: Antioxidant, Anti-Inflammatory, and Anti-Urinary Tract Infection Properties — Antioxidants (Basel) 2024;13(9):1037 (PMID 39334696, PMC11429228, 전문 확인)", doi("10.3390/antiox13091037"), PM, A),
 (7, "Determination of the Phytochemical Components, Nutritional Content, Biological Activities, and Cytotoxicity of Ripening Karanda (Carissa carandas) Fruit Extract for Functional Food Development — Prev Nutr Food Sci 2024;29(4):454 (PMID 39759816, PMC11699567, 전문 확인; 정오표 PMID 42079862)", doi("10.3746/pnf.2024.29.4.454"), PM, A),
 (8, "Carissa carandas L. and Its Methanol Extracts Promote Hematopoiesis and Thrombocytopoiesis: A Sub-Acute Toxicological Study in Experimental Rats — Food Sci Nutr 2026 (PMID 42016262, PMC13093303, 전문 확인)", doi("10.1002/fsn3.71647"), PM, A),
 (9, "Exploring the nutritional and sensory potential of karonda fruit: Physicochemical properties, jam production, and quality evaluation — Food Sci Nutr 2023 (PMID 37970398, PMC10630836, 전문 확인)", doi("10.1002/fsn3.3619"), PM, A),
 (10, "Synergistic Effects of Microencapsulated Polyphenols and Concurrent Training on Metabolic Health and Fitness in Overweight/Obese Adults with Prediabetes — Nutrients 2025;17(21):3358 (PMID 41228432, PMC12608511, 전문 확인; 받아 본 본문에서 karonda의 학명 표기는 빠져 있음)", doi("10.3390/nu17213358"), PM, A),
 (11, "Characterization and Phylogenetic Analysis of the Chloroplast Genome of Carissa spinarum L. (Rauvolfioideae, Apocynaceae) — Ecol Evol 2025 (PMID 40823053, PMC12354977, 전문 확인; 카란다가 아닌 같은 속 다른 종 연구로, 속의 유전체 현황 확인에만 사용)", doi("10.1002/ece3.71988"), PM, A),
 (12, "Antidiabetic potential of unripe Carissa carandas Linn. fruit extract — J Ethnopharmacol 2011 (PMID 21439367, 초록만 확인)", doi("10.1016/j.jep.2011.03.036"), PM, A),
 (13, "Pharmacological basis for the medicinal use of Carissa carandas in constipation and diarrhea — J Ethnopharmacol 2014 (PMID 24583104, 초록만 확인)", doi("10.1016/j.jep.2014.02.024"), PM, A),
 (14, "Biosynthesis of carissol and carissic acid — Pak J Pharm Sci 1993 (PMID 16414732, 초록만 확인)", "https://pubmed.ncbi.nlm.nih.gov/16414732/", PM, A),
 (15, "Role of dried fruits of Carissa carandas as anti-inflammatory agents and the analysis of phytochemical constituents by GC-MS — Biomed Res Int 2014:512369 (PMID 24877106, PMC4022248, 초록만 확인)", doi("10.1155/2014/512369"), PM, A),
 (16, "Triterpenoidal constituents of the leaves of Carissa carandas — Nat Prod Res 2003 (PMID 12737397, 초록만 확인)", doi("10.1080/1478641031000104109"), PM, A),
 (17, "Activity-guided investigation of Carissa carandas (L.) roots for anti-inflammatory constituents — Nat Prod Res 2015 (PMID 25496183, 초록만 확인)", doi("10.1080/14786419.2014.989846"), PM, A),
 (18, "Anti-inflammatory and antioxidant activities of naringin isolated from Carissa carandas L.: In vitro and in vivo evidence — Phytomedicine 2018 (PMID 29655678, 초록만 확인)", doi("10.1016/j.phymed.2018.03.051"), PM, A),
 (19, "A novel carissic acid from fruits of Carissa carandas induced apoptotic cell death in A-549 cells following the activation of caspases — Nat Prod Res 2023 (PMID 37449969, 초록만 확인)", doi("10.1080/14786419.2023.2232082"), PM, A),
 (20, "Hydrophilic antioxidant capacities and total phenol content of seasonal fruits of Bangladesh — Malays J Nutr 2012 (PMID 24568076, 초록만 확인)", "https://pubmed.ncbi.nlm.nih.gov/24568076/", PM, A),
 (21, "Antimicrobial polyphenols from small tropical fruits, tea and spice oilseeds — Food Sci Technol Int 2014 (PMID 23703103, 초록만 확인)", doi("10.1177/1082013213482476"), PM, A),
 (22, "Colorimetric indicator films based on carboxymethyl cellulose and anthocyanins as a visual indicator for shrimp freshness tracking — Heliyon 2024 (PMID 38828285, PMC11140613, 초록만 확인)", doi("10.1016/j.heliyon.2024.e31527"), PM, A),
 (23, "Phytonutritional and Sensorial Assessment of a Novel Functional Beverage Formulated from an Underutilized Fruit of Carissa carandas L. — ACS Omega 2023 (PMID 37720775, PMC10500662, 초록만 확인)", doi("10.1021/acsomega.3c03386"), PM, A),
 (24, "Effect of karwanda (Carissa congesta Wight) and sugar addition on physicochemical characteristics of ash gourd and bottle gourd based beverages — J Food Sci Technol 2019 (PMID 30906061, PMC6400749, 초록만 확인)", doi("10.1007/s13197-019-03570-7"), PM, A),
 (25, "Adaptational strategy of a tropical shrub Carissa carandas L. to urban air pollution — Environ Monit Assess 1996 (PMID 24193899, 초록만 확인)", doi("10.1007/BF00394453"), PM, A),
 (26, "Spatial assessment of soil organic carbon and physicochemical properties in a horticultural orchard at arid zone of India using geostatistical approaches — Environ Monit Assess 2016 (PMID 27553943, 초록만 확인)", doi("10.1007/s10661-016-5522-x"), PM, A),
 (27, "Data on the cost effective surface sterilization method for C. carandas (L.) seeds and callus induction from aseptic seedling — Data Brief 2016 (PMID 27222851, PMC4865676, 초록만 확인)", doi("10.1016/j.dib.2016.04.047"), PM, A),
 (28, "Foliar micromorphology and its role in identification of the Apocynaceae taxa — Microsc Res Tech 2020 (PMID 32118344, 초록만 확인)", doi("10.1002/jemt.23466"), PM, A),
 (29, "Evaluation of Phytochemical and Pharmacological Activity of Carissa carandas L. Fruits at Three Different Stages of Maturation — Drug Res (Stuttg) 2019 (PMID 31801160, 초록만 확인)", doi("10.1055/a-0815-4832"), PM, A),
 (30, "Bioactivities of Karanda (Carissa carandas Linn.) fruit extracts for novel cosmeceutical applications — J Adv Pharm Technol Res 2021 (PMID 34159148, PMC8177143, 초록만 확인)", doi("10.4103/japtr.JAPTR_254_20"), PM, A),
 (31, "Optimizing conditions for microwave-assisted solvent extraction of polar compounds from Carissa carandas — J Food Sci 2024 (PMID 39668115, 초록만 확인)", doi("10.1111/1750-3841.17577"), PM, A),
 (32, "Pharmacodynamic study on acute hypotensive activities of Carissa carandas extract in normal rats — Pak J Pharm Sci 2012 (PMID 22713944, 초록만 확인)", "https://pubmed.ncbi.nlm.nih.gov/22713944/", PM, A),
 (33, "Indigenous underutilized fruits in Bangladesh as future resilient foods: insight into the nutritional value, bioactive compounds, and health benefits — Crit Rev Food Sci Nutr 2026 (PMID 42287183, 초록만 확인)", doi("10.1080/10408398.2026.2686872"), PM, A),
]
sources = [dict(n=n, title=t, url=u, publisher=p, accessed=a) for n, t, u, p, a in S]

sections = [
 dict(key="overview", title="한눈에 보기", body=
 "카란다는 협죽도과(Apocynaceae) 카리사속의 가시 많은 상록 관목으로, 작은 장과(베리)를 맺는다[4]. 식약처 「식품원료 목록」에는 원료명 '카란다열매', 학명 'Carissa carandas L. / Carissa congesta Wight', 영어 이름 Sri Lankan Damson·Kala·Mahakaramba·Karanda로 올라 있다[1]. 이 목록에서 카란다는 식품에 쓸 수 있는 원료(사용가능)이며, 사용 조건은 '사용가능부위 : 열매'로 열매만 쓸 수 있다[1]. 이 종을 원재료로 하는 건강기능식품 고시형 원료는 목록에서 확인되지 않는다[1].\n\n"
 "인도·파키스탄 등 남아시아에서는 덜 익은 열매를 피클로, 익은 열매를 젤리·잼·음료로 만들어 먹는다[4, 9]. 열매에는 비타민 C, 안토시아닌, 클로로겐산 같은 페놀산, 우르솔산 같은 트라이테르페노이드가 들어 있다고 보고되었다[5, 6, 9]. 항산화·항염·항균 작용은 주로 시험관·동물 연구에서 나왔고, 사람 연구는 감 추출물과 섞은 제형을 쓴 소규모 예비 시험 정도다[3, 10]. 방글라데시 여름 과일 15종 가운데 카란다의 항산화 용량이 4.882 μmol TE/g(생중량)으로 가장 높았고, 방글라데시의 덜 활용된 토종 과일 가운데 유망한 종으로 꼽힌다[20, 33]."),
 dict(key="history", title="역사", body=
 "카란다는 인도 여러 부족의 전통 의학과 아유르베다·우나니·싯다·동종요법 체계에서 쓰여 온 식물로 정리되어 있다[3]. 여러 부위를 달여서 이질·열·감기 등에 썼다고 기록되어 있다[3]. 북인도에서는 열매를 피클의 재료나 향신료로 써 왔다[4]. 인도 카르나타카 서고츠 지역의 부족 치료사들은 이 식물을 간 보호와 혈당 저하 목적으로 썼다고 한다[12].\n\n"
 "파키스탄에서는 'Karaunda'로 불리며 변비·설사 같은 장 운동 장애에 민간약으로 널리 쓰였다[13]. 1993년 논문은 파키스탄에서 이 관목을 'Kakronda'라 부르며 산울타리로 흔히 심고, 옛 문헌에 하제·건위제·구충제·뱀독 해독제로 적혀 있다고 소개했다[14]. 같은 논문은 뿌리에서 강심 작용이 보고되었다는 옛 연구도 인용했다[14]. 민간에서는 식욕 부진·천식·기침·열·말라리아·옴 등 여러 증상에 쓰였다는 기록이 있다[5]. 한국에 들어온 시기와 경로는 확인하지 못함."),
 dict(key="biology", title="식물학적 특징", body=
 "카란다는 키 3 m까지 자라는 작은 관목으로, 작은 흰 꽃을 피우고 붉거나 검은 열매를 맺는다[9]. 열매는 둥글거나 타원형이며 체리만 한 크기로 여름에 익고 신맛이 난다[9]. 익는 동안 열매 색은 흰색·분홍색(덜 익음)에서 붉은색(반쯤 익음), 자주색(완숙)으로 바뀐다[7]. 열매의 약 75%가 먹을 수 있는 과육이다[8]. 익은 열매를 익히면 끈적한 유액이 나오지만 식으면 붉은 즙이 나온다[9].\n\n"
 "Kew의 POWO는 Carissa carandas L.(1767년 발표)을 승인명으로 두고, 원산지를 인도와 방글라데시 남동부로, 주된 생육지를 계절적으로 건조한 열대로 적는다(WebSearch 요약으로 확인)[2]. 같은 자료는 스리랑카·태국·베트남·필리핀·모리셔스 등을 도입 지역으로 적는다(WebSearch 요약)[2]. 논문들은 파키스탄·인도·아프가니스탄·스리랑카·미얀마·방글라데시·네팔 등 열대·아열대 아시아에 널리 분포한다고 쓴다[6]. 상록성이라 잎을 한 해 내내 얻을 수 있다[18]. 잎 윗면에는 불규칙형·부등형·환상형 기공이 함께 나타난다[28]."),
 dict(key="related_species", title="이름과 가까운 종", body=
 "영어권과 남아시아에서는 karonda, karanda, karaunda로 부르며, Crane berry(영어), Karamcha(벵골어), Ci-Huang-Guo(중국어) 같은 이름도 쓰인다[6, 13]. 파키스탄 일부 지역에서는 'Christ thorn'이라고도 부른다[9]. 식약처 목록은 Carissa congesta Wight를 함께 적어 같은 원료로 다룬다[1]. 인도 연구에는 C. congesta Wight를 'karwanda'로 부르며 음료 재료로 쓴 예가 있다[24]. POWO 검색 요약에서는 Jasminonerium carandas와 J. salicinum이 이명으로 나왔고, C. congesta의 이명 여부는 확인하지 못함.\n\n"
 "카리사속의 종 수는 자료마다 달라, 약 25종이라는 논문과 POWO를 인용해 약 15종이라는 논문이 있다[9, 11]. 식약처 목록에는 같은 속의 Heen karamba열매(Carissa spinarum)와 나탈플럼열매(Carissa grandiflora, Natal plum)가 카란다와 따로 올라 있으므로, 이 자료에는 그 두 종의 성분·안전성 자료를 섞지 않았다[1]. 파키스탄에서 'Jungli karonda'라고 부르는 것은 C. spinarum으로, 이름이 비슷해 혼동하기 쉽다[11]."),
 dict(key="cultivation", title="재배와 산지", body=
 "카란다는 건조하고 메마른 땅에서도 잘 견디는 야생 과일 식물로 소개된다[3]. 인도 건조 지대의 과수원 연구에는 카란다 구획이 따로 있었고, 이 구획의 토양 유기탄소 저장 밀도(0–30 cm)는 9.01 Mg/ha로 과수원 안에서 가장 낮았다[26]. 인도 바라나시에서 2년 동안 화분에 키운 묘목은 도시 대기오염으로 키·줄기 굵기·잎 면적이 줄었지만 광합성 산물을 지상부에 많이 배분하며 적응했다[25].\n\n"
 "연구용 열매는 태국 사뭇송크람(5월)·빠툼타니, 파키스탄 물탄(7월 말, 8–9월), 파키스탄령 카슈미르 하지라(3–8월 조사) 등에서 거두었다[5, 6, 7, 8, 9]. 파키스탄령 카슈미르에서는 가정 텃밭에 흔히 심고 일부 지역에서는 상업적으로 재배한다[9]. 종자를 소독해 무균 묘를 키우고 캘러스를 유도한 조직배양 자료도 있다[27]. 국내 재배 면적·생산량 통계와 세계 생산 통계는 확인하지 못함."),
 dict(key="processing", title="가공과 이용", body=
 "덜 익은 열매는 주로 피클로 저장하고, 익은 열매는 펙틴이 많아 젤리·잼·스쿼시·소스·처트니 등으로 만든다[9]. 카란다와 사과 과육을 섞은 잼을 4개월 냉장 보관하며 품질을 평가한 연구가 있다[9]. 과육 20·30·40%로 만든 음료를 10주 동안 냉장 보관하며 성분을 측정한 연구도 있다[23]. 동아·박 주스에 karwanda를 넣으면 총폴리페놀과 항산화 활성이 높아졌다[24].\n\n"
 "생과를 말리면 비타민 C는 100 g당 72 mg에서 49 mg으로 줄었고, 총페놀은 17.20에서 52.50 mg GAE/g로 높게 측정되었다[9]. 극성 성분 추출에는 에탄올:물 49:51(v/v)이 가장 알맞았고, 마이크로파 추출은 180 W·3분 조건이 당과 폴리페놀 추출에 유리했다[31]. 냉수 초음파 추출물에 펙티나아제를 처리하면 탁도가 줄었고 항산화 활성은 유지되었다[7]. 말린 열매 메탄올 추출물에서는 GC-MS로 11가지 성분이 확인되었다[15]. 열매 폴리페놀 분획은 항균 작용을 보였으나 안토시아닌 분획은 그렇지 않았다[21]. 열매 안토시아닌은 새우 신선도를 색으로 보여 주는 지시 필름 재료로도 연구되었다[22]. 태국 연구진은 감 추출물 70%와 karonda 추출물 30%를 섞어 말토덱스트린으로 미세캡슐화한 제형을 만들었다[10]. 국내에서 카란다를 원료로 한 식품·건강기능식품 생산실적은 확인하지 못함."),
 dict(key="genetics", title="유전 정보", body=
 "2025년 논문은 카리사속에서 엽록체 유전체가 공개된 종으로 C. macrocarpa와 그 연구의 C. spinarum만 들었으며, 카란다 자체의 엽록체·핵 유전체 해독 보고는 확인하지 못함[11]. 같은 논문의 계통 분석은 카리사속을 협죽도과 Rauvolfioideae 아과의 Carisseae 족에 두었다[11]. 염색체 수는 확인하지 못함.\n\n"
 "열매 성분은 익는 단계에 따라 크게 달라진다[29, 30]. 세 성숙 단계를 비교한 연구에서 페놀·플라보노이드·아스코르브산은 성숙 열매의 아세톤 추출물에, 탄수화물은 완숙 열매에 가장 많았다[29]. 다른 연구에서는 총페놀이 완숙 생과 추출물에서 100.31 mg GAE/g 추출물로 가장 높았고, 덜 익은 생과는 DPPH 소거 IC50 29.11 μg/mL로 항산화력이 가장 강했다[30]. 파키스탄 연구는 열매를 거둔 뒤 품종 감정을 거쳤다고 적었으나 품종 이름은 밝히지 않았다[6]. 종자에서 키운 무균 묘로 캘러스를 유도한 조직배양 자료는 대량 증식 연구의 기초가 된다[27]."),
 dict(key="safety", title="안전성", body=
 "식약처 목록에서 카란다는 열매에 한해 사용가능한 원료이며, 건강기능식품 고시형 원료가 아니어서 고시 섭취 시 주의사항은 없다[1]. 국내 공공기관의 알레르기·잔류농약·독성 성분 정보는 확인하지 못함.\n\n"
 "수컷 쥐에게 열매 건조 분말 또는 메탄올 추출물을 사료의 5–10%로 28일 동안 먹인 시험에서 죽은 개체는 없었고 혈액·혈청 지표는 정상 범위였다[8]. 다만 추출물 10% 군에서는 간세포 핵 농축과 신세뇨관 확장 같은 가벼운 조직 변화가 보였다[8]. 사람 말초혈액 단핵세포에서 완숙 열매 물 추출물은 2.5 mg/mL 이하에서는 독성이 없었으나 5.0 mg/mL 이상에서 생존율이 50% 밑으로 떨어졌고, 10.0 mg/mL에서는 적혈구 용혈이 50%를 넘었다[7]. 같은 추출물의 GC-MS 분석에서는 5-하이드록시메틸푸르푸랄(HMF)도 검출되었다[7].\n\n"
 "쥐 정맥에 에탄올 추출물을 주사하면 용량에 따라 혈압과 심박수가 떨어졌다[32]. 옛 연구에서 뿌리의 강심 작용이 보고된 바 있으며[14], 식약처 목록이 식품에 쓰도록 허용한 부위는 열매뿐이다[1]. 종자 추출물 일부는 사람 각질세포 성장을 억제했다[5]. 임신·수유부, 약물 상호작용에 관한 자료는 확인하지 못함."),
]

compounds = [
 dict(name="Ursolic acid", name_ko="우르솔산", class_="트라이테르페노이드", role="marker", part="열매·과육(잎에 가장 많음)", content_text="에틸아세테이트 추출물 기준 열매 253.32 mg/g, 과육 256.34 mg/g, 잎 411.8 mg/g, 종자 3.4 mg/g(HPLC)[5]", activity_ko="티로시나아제·엘라스타아제 억제, 항염 작용의 핵심 성분으로 제안됨(시험관)[5]", source=[5]),
 dict(name="Chlorogenic acid", name_ko="클로로겐산", class_="페놀산", role="bioactive", part="열매 과육(메탄올 추출물의 에틸아세테이트 분획)", content_text="17.6 µg/mg(건조중량 기준, HPLC)[6]", activity_ko="항산화·항염·요로감염균 항균 활성 분획의 성분[6]", source=[6]),
 dict(name="Ellagic acid", name_ko="엘라그산", class_="페놀산", role="bioactive", part="열매 과육(같은 분획)", content_text="5.90 µg/mg(건조중량 기준, HPLC)[6]", activity_ko="활성 분획의 성분으로 추정 동정 후 정량[6]", source=[6]),
 dict(name="Quinic acid", name_ko="퀸산", class_="유기산", role="bioactive", part="열매 과육(같은 분획)", content_text="3.30 µg/mg(건조중량 기준, HPLC)[6]", activity_ko="활성 분획의 성분으로 추정 동정 후 정량[6]", source=[6]),
 dict(name="Cyanidin 3-galactoside", name_ko="시아니딘-3-갈락토사이드 등 안토시아닌", class_="안토시아닌", role="bioactive", part="열매 과육", content_text="LC-ESI-MS/MS로 시아니딘-3-갈락토사이드·피오니딘-3-아라비노사이드·델피니딘-3-갈락토사이드·델피니딘-3-루티노사이드 추정 동정; 메탄올 추출물 총안토시아닌 112 mg/kg[6]", activity_ko="열매의 자주색 색소로, pH 지시 필름 재료로 연구됨[6, 22]", source=[6, 22]),
 dict(name="Ascorbic acid", name_ko="아스코르브산(비타민 C)", class_="비타민", role="nutrient", part="열매", content_text="생과 72.00 mg/100 g, 건조 열매 49.00 mg/100 g[9]; 완숙 열매 냉수 추출물 0.01%(AOAC 967.21)[7]", activity_ko="항산화 활성에 기여[7]", source=[7, 9]),
 dict(name="Carissic acid", name_ko="카리스산", class_="트라이테르페노이드", role="bioactive", part="열매", content_text="열매 메탄올 추출물의 클로로폼 분획에서 새 화합물로 분리(함량 보고 없음)[19]", activity_ko="폐암 A-549 세포 IC50 3.47 µM 등 세포독성(시험관)[19]", source=[19, 14]),
 dict(name="Carissone", name_ko="카리손", class_="세스퀴테르페노이드", role="bioactive", part="뿌리(열매에도 있다고 보고)", content_text="뿌리 메탄올 추출물에서 분리(함량 보고 없음)[17]; 열매에 카리손·카린돈이 있다고 정리됨[5]", activity_ko="NO 생성 억제 IC50 20.1 μg/mL(시험관)[17]", source=[17, 5]),
 dict(name="Scopoletin", name_ko="스코폴레틴", class_="쿠마린", role="bioactive", part="뿌리", content_text="뿌리에서 분리(함량 보고 없음)[17]", activity_ko="NO 생성 억제 IC50 24.6 μg/mL(시험관)[17]", source=[17]),
 dict(name="Oleanolic acid", name_ko="올레아놀산", class_="트라이테르페노이드", role="bioactive", part="잎·뿌리", content_text="잎 메탄올 추출물 HPLC 지문에서 검출[13]; 뿌리에서 분리[17]", activity_ko="장 운동 관련 약리 연구 추출물의 구성 성분[13]", source=[13, 17]),
 dict(name="Lupeol", name_ko="루페올", class_="트라이테르페노이드", role="bioactive", part="뿌리", content_text="뿌리에서 분리(함량 보고 없음)[17]", activity_ko="항염 활성 유도 분리로 얻은 성분[17]", source=[17]),
 dict(name="Naringin", name_ko="나린진", class_="플라보노이드", role="bioactive", part="잎", content_text="잎 80% 메탄올 추출물에서 높은 수율로 분리(수율 수치는 초록에서 확인하지 못함)[18]", activity_ko="LPS 자극 대식세포 NO 생성 억제 IC50 6.4 μM, 쥐 발 부종 억제[18]", source=[18]),
 dict(name="Carissin", name_ko="카리신", class_="트라이테르페노이드", role="bioactive", part="잎", content_text="생잎에서 새 화합물로 분리(3β-hydroxy-27-E-feruloyloxyurs-12-en-28-oic acid)[16]", activity_ko="구조 규명 연구(활성은 이 논문에서 다루지 않음)[16]", source=[16]),
 dict(name="5-Hydroxymethylfurfural", name_ko="5-하이드록시메틸푸르푸랄(HMF)", class_="퓨란 화합물", role="bioactive", part="완숙 열매 물 추출물", content_text="GC-MS 피크 면적 1% 넘는 주요 성분 목록에 포함(정량값 없음)[7]", activity_ko="고농도 추출물의 세포독성과 관련이 있을 수 있다고 저자들이 논의[7]", source=[7]),
]
for c in compounds: c["class"] = c.pop("class_")

nutrients = [
 dict(form="생과(파키스탄령 카슈미르 하지라산)", basis="원문 표 2 값(%는 원문 단위; 단백질은 검출되지 않았다고 보고)", items=[
   dict(name="수분", value=66.5, unit="%"), dict(name="조지방", value=2.57, unit="%"), dict(name="조섬유", value=1.01, unit="%"),
   dict(name="회분", value=1.81, unit="%"), dict(name="탄수화물", value=28.165, unit="%"), dict(name="총당", value=5.9, unit="%"),
   dict(name="비타민 C", value=72.0, unit="mg/100 g"), dict(name="적정산도", value=1.87, unit="%")], source=[9]),
 dict(form="건조 열매(같은 산지)", basis="원문 표 2 값", items=[
   dict(name="수분", value=36.0, unit="%"), dict(name="조지방", value=19.0, unit="%"), dict(name="조섬유", value=4.905, unit="%"),
   dict(name="회분", value=4.985, unit="%"), dict(name="탄수화물", value=35.0, unit="%"), dict(name="총당", value=8.05, unit="%"),
   dict(name="비타민 C", value=49.0, unit="mg/100 g")], source=[9]),
]

def cond(**kw):
    keys = ["instrument","column","mobile_phase","gradient","flow","temp","detection","injection","sample_prep","standard","linearity","lod","loq","recovery"]
    return {k: kw.get(k, "") for k in keys}

assays = [
 dict(role="literature", compound="Ursolic acid", compound_ko="우르솔산", part="열매·과육(태국 사뭇송크람산 완숙 열매, 50 °C 건조)",
  content="에틸아세테이트 추출물 기준 열매 253.32 mg/g, 과육 256.34 mg/g; n-헥산 추출물 열매 2.54 mg/g, 과육 1.60 mg/g[5]",
  method="HPLC-UV(등용매)",
  conditions=cond(instrument="Hitachi HPLC series L, UV 검출기 Hitachi L-7420",
   column="Phenomenex Luna 5 μm C18(2) 100A, 250 × 2.0 mm",
   mobile_phase="HPLC용 에탄올:탈이온수 = 90:10", gradient="등용매(isocratic)", flow="0.5 mL/min",
   detection="UV 210 nm(우르솔산 머무름 시간 약 9.3분)", injection="20 μL",
   sample_prep="건조 분말을 n-헥산 → 에틸아세테이트 → 95% 에탄올로 각 24시간씩 3회 연속 냉침, 감압 농축; 0.2 μm 나일론 필터 여과",
   standard="우르솔산(Sigma-Aldrich)", linearity="우르솔산 1–500 μg/mL로 검량선 작성"),
  rationale="우르솔산이 추출물 크로마토그램의 주 피크이고 항염·항종양·항균 작용이 보고되어 저자들이 정량 지표로 제안함; 칼럼 온도·검출·정량한계·회수율은 원문에 없음[5].",
  source=[5], url=doi("10.3390/antiox10091345"), source_kind="paper"),
 dict(role="literature", compound="Chlorogenic acid, ellagic acid, quinic acid", compound_ko="클로로겐산·엘라그산·퀸산", part="열매 과육(파키스탄 물탄산, 메탄올 추출물의 에틸아세테이트 분획 B)",
  content="클로로겐산 17.6 µg/mg, 엘라그산 5.90 µg/mg, 퀸산 3.30 µg/mg(건조중량 기준)[6]",
  method="HPLC-DAD(추정 동정은 직접주입 LC-ESI-MS/MS)",
  conditions=cond(instrument="Agilent 1100/1200 HPLC, 다이오드 배열 검출기(DAD)",
   column="Agilent Zorbax SB-C18, 4.6 × 150 mm, 5 μm",
   mobile_phase="A: 0.1% 트라이플루오로아세트산 수용액, B: 0.1% 트라이플루오로아세트산 함유 아세토니트릴",
   gradient="B 15%(0–10분) → 15–30%(11–15분) → 30–60%(15–22분) → 60–90%(22–27분) → 100%(27–30분)",
   flow="0.5 mL/min", detection="354, 280, 310, 520 nm",
   injection="정량 시 시료·표준액 100 μL(분획 조건 설정 시 10 μL)",
   sample_prep="씨를 뺀 과육을 헥산(탈지) → 다이클로로메탄 → 메탄올 → 50% 메탄올로 순차 추출; 메탄올 추출물을 액-액 분배해 얻은 분획 B 60 mg을 메탄올 1 mL에 녹임(분획 조건 설정 시 0.45 μm 여과)",
   standard="클로로겐산·엘라그산·퀸산 표준액 각 250 µg/mL(외부 표준, UV 스펙트럼·머무름 시간 비교)"),
  rationale="항산화·항염·요로감염균 항균 활성이 가장 높은 분획에서 동정된 페놀산을 표준품으로 정량함; 직선성·검출·정량한계·회수율과 칼럼 온도는 원문에 없음[6].",
  source=[6], url=doi("10.3390/antiox13091037"), source_kind="paper"),
 dict(role="literature", compound="Ascorbic acid", compound_ko="아스코르브산(비타민 C)", part="완숙 열매(태국 빠툼타니산) 냉수 초음파 추출물(Fresh-RKF)",
  content="0.01%(w/w); 같은 추출물 총당 0.27%(환원당 0.25%, 비환원당 0.02%)[7]",
  method="AOAC 967.21(총당은 Lane-Eynon, AOAC 923.09)",
  conditions=cond(sample_prep="씨를 뺀 완숙 열매를 차가운 탈이온수와 1:1(w/v)로 균질화한 뒤 45 kHz·4 °C에서 1시간씩 초음파 추출을 4회 반복, 합친 추출액을 60 °C 10분 살균 후 동결건조"),
  rationale="완숙 열매 추출물의 항산화 활성과 관련된 영양 성분으로 측정됨; AOAC 공정법 번호만 적혀 있고 세부 기기 조건은 원문에 없음. 같은 논문의 C18 HPLC(Agilent Eclipse Plus C18 3.5 μm 4.6 × 100 mm, 1.0 mL/min, 272 nm, 10 μL)는 머무름 시간 비교에 의한 정성 분석뿐이라 정량 조건으로 쓰지 않음[7].",
  source=[7], url=doi("10.3746/pnf.2024.29.4.454"), source_kind="paper"),
]

d = dict(slug="carissa-carandas", name_ko="카란다", name_en="Karanda (karonda)", scientific_name="Carissa carandas L.",
 aliases=["카란다열매", "Karonda", "Karanda", "Karaunda", "Sri Lankan Damson", "Kala", "Mahakaramba", "Carissa congesta Wight", "Crane berry", "Karamcha", "Kakronda", "Karwanda"],
 sections=sections, compounds=compounds, markers=[], nutrients=nutrients, assays=assays,
 production=[], world=[], gi=[], orgs=[], sources=sources)
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in sections: print(s["key"], len(s["body"]))
