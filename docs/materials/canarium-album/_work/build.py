import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
A = "2026-11-02"
PM = "PubMed (National Library of Medicine)"

def pm(title, doi, pmid, note):
    url = f"https://doi.org/{doi}" if doi else f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
    return {"title": f"{title} (PMID {pmid}; {note})", "url": url, "publisher": PM, "accessed": A}

S = [
 {"title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 감람나무열매(Canarium album (Lour.) Raeusch., 이명 감람수, 영명 Chinese white olive, Kan Lan, Pak Laam), 사용가능부위: 열매, 사용가능",
  "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
 {"title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 이름이 비슷한 다른 행: 빈랑·빈랑나무열매(Areca catechu, 이명에 '감람자', 사용불가), 월계수잎·월계수열매(Laurus nobilis, 이명에 '감람', 사용가능), 필리너트과육·씨앗·싹·종자유(Canarium ovatum, 사용가능)",
  "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
 pm("Chinese olive (Canarium album Rauesch.): a critical review on its nutritional value, phytochemical composition, health benefits, and practical applications. Front Pharmacol 2023;14:1275113", "10.3389/fphar.2023.1275113", "38094884", "PMC10716235 전문 확인"),
 pm("Chinese Olive (Canarium album L.) Fruit Extract Attenuates Metabolic Dysfunction in Diabetic Rats. Nutrients 2017;9(10):1123", "10.3390/nu9101123", "29036927", "PMC5691739 전문 확인"),
 pm("Polyphenol-rich Chinese olive extracts attenuate lipid accumulation in HepG2 cells, accompanied by AMPK phosphorylation and miRNA alterations. Front Nutr 2026;13:1749622", "10.3389/fnut.2026.1749622", "41756637", "PMC12932180 전문 확인"),
 pm("Study on Quality Characteristic of Chebulae Fructus and Its Adulterants and Degradation Pathway of Hydrolyzable Tannins. Molecules 2024;29(10):2399", "10.3390/molecules29102399", "38792262", "PMC11123712 전문 확인"),
 pm("[Main chemical components for clearing heat and relieving sore throat in different germplasm of Canarium album]. Zhongguo Zhong Yao Za Zhi 2010;35(6):669-72", "10.4268/cjcmm20100601", "20545183", "중국어 논문, 영문 초록만 확인"),
 pm("Physicochemical Properties and Antioxidant Capacity of Chinese Olive (Canarium album L.) Cultivars. J Food Sci 2017;82(6):1369-1377", "10.1111/1750-3841.13740", "28494096", "초록만 확인"),
 pm("A Review of Chinese olive (Canarium album) Polyphenols: From Efficient Extraction to Mechanistic Understanding and Functional Food Development. Foods 2026;15(13):2410", "10.3390/foods15132410", "42450528", "초록만 확인"),
 pm("Comprehensive quality profiling and comparative metabolic characterization of seven dominant fresh-eating Chinese olive (Canarium album Lour.) cultivars. Food Chem 2026;525:150441", "10.1016/j.foodchem.2026.150441", "42462307", "초록만 확인"),
 pm("In-vitro anti-Helicobacter pylori activity and preliminary mechanism of action of Canarium album Raeusch. fruit extracts. J Ethnopharmacol 2021;283:114578", "10.1016/j.jep.2021.114578", "34464702", "초록만 확인"),
 pm("Rapid discriminate and determination of chemical constituents of Canarii Fructus (Chinese olive) and Chebulae Fructus Immaturus using digital image-based analytical system. Talanta 2025;297:128720", "10.1016/j.talanta.2025.128720", "40857766", "초록만 확인"),
 pm("The complete chloroplast genome sequence of Canarium album. Mitochondrial DNA B Resour 2019;4(2):3471-3472", "10.1080/23802359.2019.1674711", "33366044", "초록만 확인"),
 pm("Genetic analysis of Canarium album in different areas of China by improved RAPD and ISSR. C R Biol 2017;340(11-12):558-564", "10.1016/j.crvi.2017.09.006", "29100782", "초록만 확인"),
 pm("Development and significance of SCAR marker QG12-5 for Canarium album (Lour.) Raeusch by molecular cloning from improved RAPD amplification. Genet Mol Res 2016;15(3)", "10.4238/gmr.15038347", "27706623", "초록만 확인"),
 pm("De novo transcriptome assembly and comparative transcriptomic analysis provide molecular insights into low temperature stress response of Canarium album. Sci Rep 2021;11:10561", "10.1038/s41598-021-90011-1", "34006894", "초록만 확인"),
 pm("Identification and Characterization of Glucosyltransferase That Forms 1-Galloyl-β-d-Glucogallin in Canarium album L. Molecules 2021;26(15):4650", "10.3390/molecules26154650", "34361803", "초록만 확인"),
 pm("Integrated Metabolomic and Transcriptomic Analysis Reveals Differential Flavonoid Accumulation and Its Underlying Mechanism in Fruits of Distinct Canarium album Cultivars. Foods 2022;11(16):2527", "10.3390/foods11162527", "36010527", "초록만 확인"),
 pm("Responses of Chinese olives to low-temperature storage at different harvest dates involve the metabolisms of ROS, membrane lipids, and phenolics. Food Chem 2025;497:146565", "10.1016/j.foodchem.2025.146565", "41260933", "초록만 확인"),
 pm("γ-Aminobutyric acid treatment reduces chilling injury and improves quality maintenance of cold-stored Chinese olive fruit. Food Chem X 2022;13:100208", "10.1016/j.fochx.2022.100208", "35498988", "초록만 확인"),
 pm("Comprehensive analyses of membrane lipids and phenolics metabolisms reveal the developments of chilling injury and browning in Chinese olives during cold storage. Food Chem 2023;416:135754", "10.1016/j.foodchem.2023.135754", "36871509", "초록만 확인"),
 pm("Investigation of Effects of Cushioning Packaging on the Physiological and Quality Changes in Chinese Olive Fruits During Cold Chain Transportation. Foods 2024;13(24):4133", "10.3390/foods13244133", "39767075", "초록만 확인"),
 pm("Anti-Inflammatory Benzofuran Neolignans from the Fruits of Canarium album (Chinese Olive). J Agric Food Chem 2022;70(4):1122-1133", "10.1021/acs.jafc.1c06457", "35049305", "초록만 확인"),
 pm("Chemical constituents from Canarium album Raeusch and their anti-influenza A virus activities. J Nat Med 2018;72(3):808-815", "10.1007/s11418-018-1208-8", "29623508", "초록만 확인"),
 pm("Isocorilagin, isolated from Canarium album (Lour.) Raeusch, as a potent neuraminidase inhibitor against influenza A virus. Biochem Biophys Res Commun 2019;523(1):183-189", "10.1016/j.bbrc.2019.12.043", "31843192", "초록만 확인"),
 pm("Methyl brevifolincarboxylate, a novel influenza virus PB2 inhibitor from Canarium Album (Lour.) Raeusch. Chem Biol Drug Des 2020;96(5):1280-1291", "10.1111/cbdd.13740", "32519462", "초록만 확인"),
 pm("Hepatoprotective compounds from Canarium album and Euphorbia nematocypha. Chem Pharm Bull (Tokyo) 1990;38(8):2201-3", "10.1248/cpb.38.2201", "2279282", "초록만 확인"),
 pm("[Studies on chemical constituents in the fruit of Canarium album Raeusch]. Zhongguo Zhong Yao Za Zhi 1999;24(7):421-3, 447", None, "12205877", "중국어 논문, 영문 초록만 확인"),
 pm("Identification of Scoparone from Chinese Olive Fruit as a Modulator of Macrophage Polarization. J Agric Food Chem 2023;71(13):5195-5207", "10.1021/acs.jafc.2c08132", "36947736", "초록만 확인"),
 pm("Safety pharmacology and subchronic toxicity of jinqing granules in rats. BMC Vet Res 2017;13(1):179", "10.1186/s12917-017-1095-3", "28623915", "초록만 확인"),
 pm("Effects of Chinese herbal medicines on lifespan in Drosophila. Exp Gerontol 2021;154:111514", "10.1016/j.exger.2021.111514", "34400294", "초록만 확인"),
 pm("Protective Effects of Canarium album Against Cigarette Smoke-Induced Cytotoxicity in Beas-2B Cells: Bioactive Components Screening and Mechanism Exploration. Mol Nutr Food Res 2026;70(1):e70381", "10.1002/mnfr.70381", "41543327", "초록만 확인"),
 pm("Urolithin M5 from the Leaves of Canarium album (Lour.) DC. Inhibits Influenza Virus by Targeting Neuraminidase. Molecules 2022;27(17):5724", "10.3390/molecules27175724", "36080488", "초록만 확인"),
 pm("qPCR-Based Reference Gene Validation in Canarium album: Stability Across Varieties and Developmental Stages. Curr Issues Mol Biol 2025;47(11):903", "10.3390/cimb47110903", "41296407", "초록만 확인"),
 {"title": "World Flora Database — Canarium album (Lour.) Raeusch. 종 정보(키·꽃·열매 시기·열매 크기; Flora of China 를 인용한 2차 데이터베이스) — 이 환경에서 페이지를 열지 못해 WebSearch 요약으로만 확인",
  "url": "https://www.worldfloradb.net/plants/canarium-album-leenh", "publisher": "World Flora Database", "accessed": A},
]
for i, s in enumerate(S, 1):
    s["n"] = i
src = [{"n": s["n"], "title": s["title"], "url": s["url"], "publisher": s["publisher"], "accessed": s["accessed"]} for s in S]

sections = [
 {"key": "overview", "title": "한눈에 보기", "body":
  "감람나무(Canarium album)는 감람과(Burseraceae)에 속하는 과일나무로, 열매는 영어로 Chinese olive 또는 Chinese white olive라고 부른다[1, 3]. 이름에 olive가 들어가지만 기름을 짜는 올리브(Olea europaea)와는 다른 식물이며, 열매 살을 그대로 먹거나 차·절임으로 먹는 과일이다[3, 5]. 식약처 「식품원료 목록」에는 원료명 '감람나무열매', 이명 '감람수', 학명 Canarium album (Lour.) Raeusch.로 올라 있다[1]. 이 목록에서 감람나무열매는 사용가능 원료이고 사용 조건은 '사용가능부위 : 열매'여서 열매만 식품에 쓸 수 있다[1]. 이 종을 원재료로 하는 건강기능식품 고시형 원료는 확인하지 못함.\n\n"
  "중국에서는 감람 열매가 중국 약전에 실린 약재이자 국가위생건강위원회의 '약식동원(약이면서 음식인 물질)' 목록에 오른 과일로 소개된다[3]. 열매의 주성분은 갈산·엘라그산 같은 페놀산과 가수분해형 탄닌이며, 신선한 열매 100 g에 페놀 화합물이 1174.0–1799.6 mg 들어 있다고 보고되었다[3, 8]. 항산화·항염·간 지질 축적 억제·항인플루엔자 작용은 세포와 동물 실험에서 보고되었고, 사람을 대상으로 한 임상시험은 확인하지 못함."},
 {"key": "history", "title": "역사와 이용", "body":
  "감람나무는 중국 남부가 원산이며 2,000년이 넘게 재배·소비되어 온 과일로 소개된다[3, 17]. 중국 전통의학에서는 익은 열매를 '청과(青果, Qing Guo)'라고 부르며 인후통·기침과 생선·게를 먹고 생긴 중독에 써 왔다[11]. 종설 논문은 감람이 과일로서는 가장 먼저 중국 약전에 실린 것 가운데 하나라고 적었다[3]. 중국 약전에는 감람과 다른 약재 7가지를 섞어 만든 청과환(Qingguo Wan)이 실려 있고, 목이 붓고 아플 때와 마른기침에 쓴다[3].\n\n"
  "잎은 '감람엽(Ganlanye)'이라는 이름으로 온병(溫病) 치료에 쓰였다고 기록되어 있으나, 국내 식품원료 목록에서 쓸 수 있는 부위는 열매뿐이다[1, 33]. 과일로는 생으로 먹는 것 말고도 물에 우려 과일차로 마시고, 국·찜의 양념이나 잼·설탕절임·사탕·과일주 원료로 쓴다[3]. 국내에서 감람나무열매가 언제부터 수입·유통되었는지는 확인하지 못함."},
 {"key": "biology", "title": "식물학적 특징", "body":
  "감람나무는 감람과 Canarium속의 늘푸른 큰키나무로, 키가 약 7–25 m, 큰 것은 약 35 m까지 자란다고 WebSearch 요약으로만 확인했다[35]. 같은 요약에 따르면 꽃은 4–5월에 피고 열매는 10–12월에 익으며, 열매는 길이 25–35 mm의 달걀꼴 또는 방추형 핵과다[35]. 열매 껍질은 익으면서 초록에서 황록색으로 바뀌고, 과육은 은은한 향과 신맛이 나고 뒷맛이 오래 남는다[3].\n\n"
  "씨(핵)는 방추형이고 세로로 골이 있으며, 세 개의 방에 각각 기름이 많은 씨가 들어 있다[3]. 씨알맹이 100 g에는 단백질 29.5 g, 조지방 52.8 g이 들어 있고 지방산의 73.3%가 불포화지방산이라고 보고되었다[3]. 과육의 주된 유기산은 사과산(말산)으로 신선중량 100 g당 463.6–766.1 mg이며, 당은 주로 포도당과 과당이다[3, 8]. 열매의 떫은맛은 가수분해형 탄닌에서 오며, 이 탄닌 함량은 탄닌이 많은 베리류보다 2.3–13배 높다고 보고되었다[17]. 열매에서는 벤조퓨란형 네오리그난 거울상 이성질체 9쌍이 새로 분리되었고, 이들은 대식세포의 LPS 유도 산화질소 생성을 IC50 6.0–30.2 μM로 억제했다[23]."},
 {"key": "related_species", "title": "이름과 가까운 종", "body":
  "감람나무(Canarium album)는 이름에 '올리브'가 붙지만 물푸레나무과의 올리브(Olea europaea)와는 과가 다른 식물이다[3, 5]. 같은 Canarium속의 필리너트(Canarium ovatum)는 식품원료 목록에 따로 올라 있으며 과육·씨앗·싹·종자유를 쓸 수 있어, 열매만 쓸 수 있는 감람나무와 조건이 다르다[1, 2].\n\n"
  "식품원료 목록에서 '감람'이라는 말은 다른 종의 이명에도 나온다[2]. 월계수(Laurus nobilis)의 이명에 '감람'이 있고, 사용불가 원료인 빈랑(Areca catechu)의 이명에는 '감람자'가 있으므로 원료명은 학명으로 확인해야 한다[2]. 약재 시장에서는 청과(Canarii Fructus)가 이름과 효능이 비슷한 가자 미숙과(藏青果, Chebulae Fructus Immaturus)와 자주 혼동되어, 디지털 이미지 분석으로 둘을 가리는 방법이 개발되었다[12]. 가자(Chebulae Fructus)의 혼입품 연구에서도 청과가 대상에 포함되었고, 12가지 페놀·탄닌 성분 가운데 청과에서는 갈산·케불라그산·엘라그산 3가지만 검출되어 함량 양상으로 구별되었다[6]."},
 {"key": "cultivation", "title": "재배와 산지", "body":
  "감람나무는 중국 남부의 해안 가까운 낮은 숲, 산비탈, 낮은 구릉지에서 자란다[3]. 주산지는 중국이며 특히 푸젠(福建)성의 재배 면적이 14만 에이커(원문 단위)를 넘는다고 보고되었다[3]. 광둥·광시·윈난과 대만에서도 재배하고, 베트남·일본·라오스·미얀마·태국·필리핀·말레이시아·인도네시아·인도·스리랑카 등 아시아 여러 나라에서도 기른다[3, 4, 5]. 국내 재배와 생산 통계는 확인하지 못함.\n\n"
  "품종 간 차이가 크다[8, 10]. 10개 품종을 비교한 연구에서 탄터우(Tantou)·탄샹(Tanxiang)은 페놀 함량과 항산화력이 높았고, 창잉(Changying) 등은 당이 많고 페놀이 적어 생식용으로 알맞았다[8]. 푸젠·광둥의 주요 생식용 7품종 연구에서는 '링펑(Lingfeng)'이 당이 많고 산이 적은 반면 '산링(Sanleng)'은 페놀 성분이 많았다[10]. 감람나무는 온도에 민감한 과수로, 4 °C 냉해와 −3 °C 동해 처리에서 각각 수천 개 유전자의 발현이 바뀌었다[16]. 과실이 강한 햇볕에 데는 일소 피해도 품질을 떨어뜨리는 주요 환경 스트레스로 꼽힌다[19]."},
 {"key": "processing", "title": "가공과 이용", "body":
  "감람 열매는 생과로 먹는 것 말고도 말린 과일, 생즙, 씹어 먹는 정제, 설탕절임·사탕 같은 간식으로 가공되고, 비스킷·빵·죽·주스에 영양 첨가 원료로 넣기도 한다[3]. 페놀 추출에는 70% 에탄올, 초음파·마이크로파를 함께 쓰는 방법이 쓰였다[5, 9]. 열매 페놀은 가수분해형 탄닌이 많아 말리거나 가열하는 동안 갈산·엘라그산 같은 단순 페놀산으로 분해될 수 있다고 가자 연구가 보고했다[6].\n\n"
  "수확 뒤에는 껍질이 갈색으로 변하는 갈변과 저온 장해가 품질을 떨어뜨린다[20, 21]. 2 °C에 저장한 열매는 8 °C에 저장한 것보다 냉해 지수와 갈변이 심했다[21]. 1.0 mM 가바(γ-아미노부티르산) 처리는 2 °C에서 100일 저장한 열매의 냉해를 줄였다[20]. 수확 시기를 비교한 연구는 입동(11월 7일) 무렵 수확한 열매가 저온 저장 중 냉해가 가장 적었다고 보고했다[19]. 저온 유통 중 완충 포장을 한 열매는 유통 20일째 부패율이 완충 포장을 하지 않은 열매보다 75% 낮았다[22]. 국내 건강기능식품 생산실적에서 감람나무 원료 품목은 확인하지 못함."},
 {"key": "genetics", "title": "유전 정보", "body":
  "감람나무의 엽록체 전체 유전체는 163,347 bp이며, 대단일복사영역 87,838 bp, 소단일복사영역 13,935 bp, 한 쌍의 역위반복영역 각 30,787 bp로 이루어져 있다[13]. 이 엽록체 유전체에는 단백질 유전자 84개, rRNA 유전자 8개, tRNA 유전자 37개 등 129개 유전자가 있고 GC 함량은 37.5%다[13]. 핵 전체 유전체 해독 보고는 확인하지 못함.\n\n"
  "중국 여러 지역의 시료 10개를 RAPD와 ISSR로 분석한 결과 다형성 띠의 비율은 각각 82.3%와 83.5%였다[14]. 같은 연구진은 개량 RAPD 띠를 클로닝해 510 염기로 된 SCAR 표지 QG12-5를 개발했다[15]. 저온 스트레스 전사체 분석에서는 109,439개의 유니진이 조립되었다[16]. 탄닌 생합성의 첫 단계인 β-글루코갈린을 만드는 UDP-포도당전이효소(UGT) 유전자는 140개가 확인되었다[17]. 품종별 열매에서는 플라보노이드 생합성 유전자와 MYB·bHLH 전사인자의 발현 차이가 대사체 차이를 이끈다고 보고되었다[18]. 품종과 발달 단계에 걸쳐 쓸 수 있는 qPCR 기준 유전자도 선발되었다[34]."},
 {"key": "safety", "title": "안전성", "body":
  "감람나무열매는 식약처 「식품원료 목록」에서 열매에 한해 사용가능한 원료다[1]. 이 종에 대한 식약처 등 국내 공공기관의 알레르기·잔류·독성 정보는 확인하지 못함. 중국에서는 약식동원 목록에 올라 있어 전통적으로 식품으로 먹어 온 물질로 다뤄진다[3, 31].\n\n"
  "청과와 다른 약재를 섞은 진칭 과립을 쥐에게 30일 동안 먹인 시험에서는 8 g/kg 이하 용량에서 뚜렷한 부작용이 없었으나 16 g/kg에서는 체중 증가 둔화와 혈청 AST·빌리루빈 상승이 나타났다[30]. 이 결과는 복합 제제에 대한 것이어서 감람 열매 단독의 독성 자료로 볼 수는 없다[30]. 초파리 수명 시험에서는 감람을 포함한 약식동원 약재 12종의 추출물이 수명에 서로 다른 영향을 보였고 일부는 수명을 줄였다[31]. 사람을 대상으로 한 안전성 시험과 알레르기 보고는 확인하지 못함. 이름이 비슷한 '감람자'는 사용불가 원료인 빈랑의 이명이므로 원료를 고를 때 학명을 확인해야 한다[2]."},
]

compounds = [
 {"name": "Gallic acid", "name_ko": "갈산", "class": "페놀산", "role": "marker", "part": "열매",
  "content_text": "신선 열매 166 mg/100 g FW(총페놀의 32.9%)[3]; 열매 에틸아세테이트 분획 11.2 mg/g 추출물(HPLC)[4]; 총페놀의 약 38.8%[9]; 'Tanxiang No.1' 추출물 UPLC-MS/MS 피크 면적 15.39%로 가장 큼[5]",
  "activity_ko": "열매의 주된 페놀 성분; 청열·인후통 관련 지표 후보로 정량됨[7]; 마이크로파 추출물의 주성분으로 확인[3]",
  "source": [3, 4, 5, 7, 9]},
 {"name": "Ellagic acid", "name_ko": "엘라그산", "class": "페놀산(탄닌 분해산물)", "role": "marker", "part": "열매",
  "content_text": "신선 열매 87.8 mg/100 g FW(총페놀의 17.4%)[3]; 에틸아세테이트 분획 7.8 mg/g 추출물(HPLC)[4]; 총페놀의 약 14.3%[9]",
  "activity_ko": "쥐 간세포·생쥐 CCl4 간 손상 모델에서 간 보호 작용[27]; 갈산과 함께 당뇨 쥐 대사 개선 분획의 주성분[4]",
  "source": [3, 4, 9, 27]},
 {"name": "Scopoletin", "name_ko": "스코폴레틴", "class": "쿠마린", "role": "marker", "part": "열매",
  "content_text": "열매에서 분리(함량은 초록에 없어 확인하지 못함)[28]; 생식질별 HPLC 정량 대상[7]",
  "activity_ko": "MDCK 세포에서 A형 인플루엔자 억제(IC50 22.9 ± 3.7 μg/mL)[3, 24]; 청열·인후통 효능 성분 후보[7]",
  "source": [3, 7, 24, 28]},
 {"name": "Scoparone", "name_ko": "스코파론", "class": "쿠마린", "role": "marker", "part": "열매",
  "content_text": "열매에서 분리(함량 확인하지 못함)[28]; 생식질별 HPLC 정량 대상[7]",
  "activity_ko": "RAW264.7 대식세포에서 LPS 유도 염증 억제, 대식세포 분극 조절[29]",
  "source": [7, 28, 29]},
 {"name": "Isocorilagin", "name_ko": "이소코릴라긴", "class": "가수분해형 탄닌(엘라지탄닌)", "role": "bioactive", "part": "열매",
  "content_text": "열매에서 분리(함량 확인하지 못함)[24, 25]",
  "activity_ko": "A형 인플루엔자 뉴라미니다아제 억제(H1N1 IC50 9.19 ± 1.99 μM, H3N2 23.72 ± 2.51 μM)[25]",
  "source": [24, 25]},
 {"name": "Methyl brevifolincarboxylate", "name_ko": "메틸 브레비폴린카복실레이트", "class": "페놀산(엘라그산 유도체)", "role": "bioactive", "part": "열매",
  "content_text": "UPLC-MS/MS 피크 면적 9.48%(두 번째로 큼)[5]; 에틸아세테이트 추출물에서 분리[26]",
  "activity_ko": "인플루엔자 PB2 cap 결합 부위 억제(H1N1 IC50 27.16 ± 1.39 μM, H3N2 33.41 ± 2.34 μM)[26]",
  "source": [5, 26]},
 {"name": "3-O-Galloylquinic acid", "name_ko": "3-O-갈로일퀸산", "class": "페놀산 에스터", "role": "bioactive", "part": "열매",
  "content_text": "10품종 UPLC-MS/MS 정량에서 게라닌 이성질체와 함께 가장 많은 성분(수치는 초록에 없어 확인하지 못함)[8]",
  "activity_ko": "열매 총페놀(1174.0–1799.6 mg GAE/100 g FW)과 항산화력의 주요 기여 성분 후보[8]",
  "source": [8]},
 {"name": "Geraniin", "name_ko": "게라닌", "class": "가수분해형 탄닌(엘라지탄닌)", "role": "bioactive", "part": "열매",
  "content_text": "10품종 정량에서 주요 성분(수치 확인하지 못함)[8]; UPLC-MS/MS 피크 면적 0.90%[5]",
  "activity_ko": "떫은맛을 내는 가수분해형 탄닌의 하나[3, 8]",
  "source": [3, 5, 8]},
 {"name": "Chebulagic acid", "name_ko": "케불라그산", "class": "가수분해형 탄닌", "role": "bioactive", "part": "열매",
  "content_text": "청과(Canarii Fructus) 3배치에서 검출(함량은 표에 있어 확인하지 못함)[6]; UPLC-MS/MS 피크 면적 0.27%[5]",
  "activity_ko": "가열·건조 중 코릴라긴·케불산·엘라그산으로 분해될 수 있음(가자 연구)[6]",
  "source": [5, 6]},
 {"name": "Hyperoside", "name_ko": "히페로사이드(하이페린)", "class": "플라보놀 배당체", "role": "bioactive", "part": "열매",
  "content_text": "열매에서 분리(함량 확인하지 못함)[27]; UPLC-MS/MS 피크 면적 1.17%[5]",
  "activity_ko": "간세포 보호(항산화) 성분으로 분리[27]; 품종 간 맛 차이에 관여하는 성분 후보[3]",
  "source": [3, 5, 27]},
 {"name": "Catechin", "name_ko": "(+)-카테킨", "class": "플라반-3-올", "role": "bioactive", "part": "열매",
  "content_text": "8품종에서 페놀 15종 정량 대상(수치 확인하지 못함)[32]",
  "activity_ko": "담배 연기 처리 기관지 상피세포(Beas-2B)에서 염증 억제와 상관성이 높은 성분 후보[32]",
  "source": [32]},
 {"name": "Malic acid", "name_ko": "사과산(말산)", "class": "유기산", "role": "nutrient", "part": "과육",
  "content_text": "463.6–766.1 mg/100 g FW[3]; 10품종 모두에서 주된 유기산[8]",
  "activity_ko": "열매의 신맛을 내는 주된 유기산[3]",
  "source": [3, 8]},
 {"name": "Linoleic acid", "name_ko": "리놀레산", "class": "다가불포화지방산", "role": "nutrient", "part": "씨알맹이",
  "content_text": "씨알맹이 지방산의 41.8%(올레산 30.5%, 팔미트산 18.0%, 스테아르산 7.8%)[3]",
  "activity_ko": "씨알맹이 기름의 주 지방산[3]",
  "source": [3]},
]

assays = [
 {"role": "literature", "compound": "Gallic acid; Ellagic acid", "compound_ko": "갈산·엘라그산", "part": "열매(대만 신주현산) 메탄올 추출물의 에틸아세테이트 분획",
  "content": "갈산 11.2 mg/g 추출물, 엘라그산 7.8 mg/g 추출물[4]",
  "method": "HPLC-PDA",
  "conditions": {"instrument": "HPLC, 광다이오드배열검출기(PDA, Thermo Fisher Scientific)", "column": "C18 역상 칼럼 250 × 4.6 mm, 5 μm (MACHEREY-NAGEL)",
   "mobile_phase": "A: 0.5% 아세트산, B: 메탄올", "gradient": "0분 A 94%/B 6% → 30분 A 38%/B 62% → 60분 A 10%/B 90%(직선 기울기)",
   "flow": "0.6 mL/min", "temp": "", "detection": "200–600 nm UV-Vis 스펙트럼 기록; 머무름시간 갈산 17.31분, 엘라그산 53.22분", "injection": "",
   "sample_prep": "열매를 100% 메탄올로 추출 → 물에 1:10으로 재현탁 → n-헥산·에틸아세테이트·n-부탄올로 차례로 분배해 에틸아세테이트 분획을 −20 °C 보관", "standard": "갈산·엘라그산 표준품과 머무름시간 비교",
   "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "에틸아세테이트 분획의 두 주봉이 갈산과 엘라그산이어서 이 분획의 조성 지표로 정량했다[4]. 전문(Methods)에서 조건을 옮겼으며, 칼럼 온도·주입량·검량선·검출한계·회수율은 논문에 없어 확인하지 못함.",
  "source": [4], "url": "https://doi.org/10.3390/nu9101123", "source_kind": "paper"},
 {"role": "literature", "compound": "Gallic acid; Chebulagic acid; Ellagic acid", "compound_ko": "갈산·케불라그산·엘라그산", "part": "청과(Canarii Fructus, 시장 구입 건조 열매 3배치)",
  "content": "청과에서 12개 대상 성분 중 3개(갈산·케불라그산·엘라그산) 검출; 배치별 함량은 표에 있어 확인하지 못함[6]",
  "method": "UPLC-PDA",
  "conditions": {"instrument": "Waters ACQUITY UPLC H-class plus", "column": "COSMOSIL PBr 2.1 × 100 mm, 2.6 μm (Nacalai Tesque)",
   "mobile_phase": "A: 0.1% 포름산 수용액, B: 메탄올", "gradient": "0–5분 0–5% B; 5–9분 5–30% B; 9–12분 30–33% B; 12–19분 33–50% B; 19–28분 50–81% B; 28–30분 81–100% B; 30–33분 100% B",
   "flow": "0.3 mL/min", "temp": "30 °C", "detection": "270 nm", "injection": "2 μL",
   "sample_prep": "시료 분말 0.2 g을 50 mL 부피 플라스크에 넣고 메탄올로 초음파 추출(600 W, 20분), 식힌 뒤 메탄올로 표선, 13,700 rpm 10분 원심분리한 상등액",
   "standard": "갈산·케불라그산·엘라그산 등 순도 98% 이상 표준품 혼합액(갈산 0.211 mg/mL, 케불라그산 0.186 mg/mL, 엘라그산 0.175 mg/mL)을 희석해 검량선",
   "linearity": "12개 성분 결정계수 > 0.9998", "lod": "0.0998–0.9779 μg/mL(S/N 3)", "loq": "0.3992–1.956 μg/mL(S/N 10)", "recovery": "97.41–113.4%(RSD < 6.5%)"},
  "rationale": "가자(Chebulae Fructus)와 혼입품을 구별하려고 만든 12성분 동시 정량법으로, 청과도 같은 조건으로 정량해 HCA·PCA로 가자와 구별했다[6]. 전문에서 조건을 옮겼고, 밸리데이션(직선성·한계·회수율)은 가자 시료로 수행한 값이다[6].",
  "source": [6], "url": "https://doi.org/10.3390/molecules29102399", "source_kind": "paper"},
 {"role": "literature", "compound": "Scopoletin; Scoparone; Gallic acid", "compound_ko": "스코폴레틴·스코파론·갈산", "part": "열매(광둥·쓰촨산 큰 열매·작은 열매 생식질)",
  "content": "", "method": "HPLC-UV", "conditions": {},
  "rationale": "문헌 검토와 정성 실험으로 청열·인후통 효능 성분으로 고른 세 성분을 품질 규격 기초를 위해 정량했다[7]. 초록에 적힌 조건은 C18 칼럼(4.6 mm × 250 mm, 5 μm), 아세토니트릴-물-아세트산(16:84:0.5), 345 nm, 35 °C, 1.0 mL/min이고 갈산은 중국 약전의 오배자 시험법을 따랐으며 평균 회수율은 100.22%·101.22%·100.42%였다[7]. 전문 확인 못함.",
  "source": [7], "url": "https://doi.org/10.4268/cjcmm20100601", "source_kind": "paper"},
]

nutrients = [
 {"form": "씨알맹이(kernel, 신선)", "basis": "100 g", "items": [
   {"name": "단백질", "value": 29.5, "unit": "g"}, {"name": "조지방", "value": 52.8, "unit": "g"},
   {"name": "회분", "value": 4.9, "unit": "g"}, {"name": "탄수화물", "value": 0.2, "unit": "g"},
   {"name": "수분", "value": 5.2, "unit": "g"}, {"name": "칼륨", "value": 587, "unit": "mg"},
   {"name": "칼슘", "value": 226, "unit": "mg"}, {"name": "나트륨", "value": 40.1, "unit": "mg"},
   {"name": "마그네슘", "value": 186, "unit": "mg"}, {"name": "철", "value": 12.4, "unit": "mg"},
   {"name": "망간", "value": 2.5, "unit": "mg"}, {"name": "아연", "value": 1.8, "unit": "mg"},
   {"name": "구리", "value": 0.9, "unit": "mg"}], "source": [3]},
]

d = {
 "slug": "canarium-album", "name_ko": "감람나무", "name_en": "Chinese olive (Chinese white olive)",
 "scientific_name": "Canarium album (Lour.) Raeusch.",
 "aliases": ["감람나무열매", "감람수", "감람", "청과(青果)", "Chinese white olive", "Kan Lan", "Pak Laam", "Canarii Fructus", "Canarium album (Lour.) DC."],
 "sections": sections, "compounds": compounds, "markers": [], "nutrients": nutrients, "assays": assays,
 "production": [], "world": [], "gi": [], "orgs": [], "sources": src,
}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in sections: print(s["key"], len(s["body"]))
