import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
A = "2026-11-02"
def pm(n, title, doi, note):
    return {"n": n, "title": f"{title} ({note})", "url": f"https://doi.org/{doi}", "publisher": "PubMed", "accessed": A}
sources = [
 {"n": 1, "title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — Anu덩이줄기(Tropaeolum tuberosum), 사용가능, 사용가능부위: 덩이줄기; 같은 속 한련꽃·한련잎·한련순(Tropaeolum majus L., 이명 금련), Dwarf nasturtium잎(T. minus), T. brachyceras·T. patagonicum·T. sessilifolium·T. tricolor 덩이줄기, T. leptophyllum 뿌리, 한련초(Eclipta prostrata) 행 대조 (로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json)", "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
 pm(2, "Reference Genome Assembly of a Tetraploid Accession of the Tuber Crop Tropaeolum tuberosum — Genome Biol Evol 2026;18(5)", "10.1093/gbe/evag115", "PMID 42090564, PMC13190279, 전문 확인"),
 pm(3, "Tropaeolum tuberosum (Ruiz & Pavón): Nutritional Composition, Bioactive Compounds, and Functional Potential as an Andean Natural Ingredient — Foods 2025;14(24):4198", "10.3390/foods14244198", "PMID 41464904, PMC12731326, 전문 확인"),
 pm(4, "From Ethnobotany to Food Innovation: Applications and Functional Potential of Tropaeolum tuberosum — Foods 2025;14(23):4091", "10.3390/foods14234091", "PMID 41376028, PMC12692520, 전문 확인"),
 pm(5, "Characterization of Nutritional and Bioactive Compound in Three Genotypes of Mashua (Tropaeolum tuberosum Ruiz and Pavón) from Different Agroecological Areas in Puno — Int J Food Sci 2022:7550987", "10.1155/2022/7550987", "PMID 35368805, PMC8967561, 전문 확인"),
 pm(6, "Assessing the Nutritional Value of Root and Tuber Crops from Bolivia and Peru — Foods 2019;8(11):526", "10.3390/foods8110526", "PMID 31652880, PMC6915682, 전문 확인"),
 pm(7, "Glucosinolate composition of Colombian accessions of mashua (Tropaeolum tuberosum Ruíz & Pavón), structural elucidation of the predominant glucosinolate and assessment of its antifungal activity — J Sci Food Agric 2016;96(14):4702-4712", "10.1002/jsfa.7689", "PMID 26919585, 초록 확인"),
 pm(8, "HPLC-DAD/HPLC-MS profiling of anthocyanins from Andean mashua tubers (Tropaeolum tuberosum Ruíz and Pavón) and their contribution to the overall antioxidant activity — J Agric Food Chem 2006;54(19):7089-97", "10.1021/jf0614140", "PMID 16968067, 초록 확인"),
 pm(9, "Anti-reproductive and other medicinal effects of Tropaeolum tuberosum — J Ethnopharmacol 1982;5(2):149-61", "10.1016/0378-8741(82)90040-x", "PMID 7057655, 초록 확인"),
 pm(10, "Tropaeolum tuberosum (Mashua) reduces testicular function: effect of different treatment times — Andrologia 2008;40(6):352-7", "10.1111/j.1439-0272.2008.00868.x", "PMID 19032684, 초록 확인"),
 pm(11, "Evaluation of different doses of mashua (Tropaeolum tuberosum) on the reduction of sperm production, motility and morphology in adult male rats — Andrologia 2011;44 Suppl 1:205-12", "10.1111/j.1439-0272.2011.01165.x", "PMID 21651603, 초록 확인"),
 pm(12, "Local/traditional uses, secondary metabolites and biological activities of Mashua (Tropaeolum tuberosum Ruíz & Pavón) — J Ethnopharmacol 2019;247:112152", "10.1016/j.jep.2019.112152", "PMID 31421183, 초록 확인"),
 pm(13, "Alkamides from Tropaeolum tuberosum inhibit inflammatory response induced by TNF-α and NF-κB — J Ethnopharmacol 2019;235:199-205", "10.1016/j.jep.2019.02.015", "PMID 30753883, 초록 확인"),
 pm(14, "Identification of TRPV1 Ion Channels Agonists of Tropaeolum tuberosum in Human Skin Keratinocytes — Planta Med 2020;87(5):383-394", "10.1055/a-1264-0572", "PMID 33007786, 초록 확인"),
 pm(15, "Alkaloids isolated from Tropaeolum tuberosum with cytotoxic activity and apoptotic capacity in tumour cell lines — Phytochemistry 2020;177:112435", "10.1016/j.phytochem.2020.112435", "PMID 32562919, 초록 확인"),
 pm(16, "Antimicrobial compounds isolated from Tropaeolum tuberosum — Nat Prod Res 2020;35(22):4698-4702", "10.1080/14786419.2019.1710700", "PMID 31913056, 초록 확인"),
 pm(17, "Letter to the editor on 'Antimicrobial compounds isolated from Tropaeolum tuberosum' — Nat Prod Res 2023;38(10):1812", "10.1080/14786419.2023.2219817", "PMID 37309098, 초록 확인"),
 pm(18, "In vitro and in vivo biotransformation of glucosinolates from mashua (Tropaeolum tuberosum) by lactic acid bacteria — Food Chem 2022;404(Pt A):134631", "10.1016/j.foodchem.2022.134631", "PMID 36444024, 초록 확인"),
 pm(19, "Proteomic analysis of mashua (Tropaeolum tuberosum) tubers subjected to postharvest treatments — Food Chem 2019;305:125485", "10.1016/j.foodchem.2019.125485", "PMID 31522126, 초록 확인"),
 pm(20, "Bioengineering potato plants to produce benzylglucosinolate for improved broad-spectrum pest and disease resistance — Transgenic Res 2021;30(5):649-660", "10.1007/s11248-021-00255-w", "PMID 33956271, PMC8478770, 초록 확인"),
 pm(21, "Occurrence and Partial Characterization of a New Mechanically Transmissible Virus in Mashua from the Ecuadorian Highlands — Plant Dis 1998;82(1):69-73", "10.1094/PDIS.1998.82.1.69", "PMID 30857072, 초록 확인"),
 pm(22, "Other Natural Hosts of Potato virus T — Plant Dis 2000;84(7):736-738", "10.1094/PDIS.2000.84.7.736", "PMID 30832100, 초록 확인"),
 pm(23, "Complete Genomic Sequence of the Potyvirus Mashua virus Y, Obtained from a 33-Year-Old Mashua (Tropaeolum tuberosum) Sample — Microbiol Resour Announc 2018;7(15)", "10.1128/MRA.01064-18", "PMID 30533729, PMC6256436, 초록 확인"),
 pm(24, "Nutritional, Thermal, and Energetic Characterization of Two Morphotypes of Andean Mashua (Tropaeolum tuberosum Ruiz & Pavón) Flours from Peru — Molecules 2025;30(17):3560", "10.3390/molecules30173560", "PMID 40942082, PMC12430478, 초록 확인"),
 pm(25, "Effect of Blanching Pretreatment on Bioactive Compounds and Surface Color in Underutilized Andean Tuber Tropaeolum tuberosum (Cubio) — Plant Foods Hum Nutr 2025;80(3):132", "10.1007/s11130-025-01377-w", "PMID 40488974, 초록 확인"),
 pm(26, "Non-conventional starch from cubio tuber (Tropaeolum tuberosum): physicochemical, structural, morphological, thermal characterization and the evaluation of its potential as a packaging material — Int J Biol Macromol 2022;221:954-964", "10.1016/j.ijbiomac.2022.09.092", "PMID 36108747, 초록 확인"),
 pm(27, "Relationships among molecular, physicochemical and digestibility characteristics of Andean tuber starches — Int J Biol Macromol 2021;182:472-481", "10.1016/j.ijbiomac.2021.04.039", "PMID 33848547, 초록 확인"),
 pm(28, "Physicochemical, Bioactive and Technofunctional Properties of Instant Black Mashua Flour Processed by Extrusion and Drum Drying — Foods 2026;15(14):2486", "10.3390/foods15142486", "PMID 42511232, PMC13409576, 초록 확인"),
 pm(29, "Wound healing activity of Tropaeolum tuberosum-based topical formulations in mice — Vet World 2022;15(2):390-396", "10.14202/vetworld.2022.390-396", "PMID 35400960, PMC8980398, 초록 확인"),
 pm(30, "Phenolic compounds from Andean mashua (Tropaeolum tuberosum) tubers display protection against soybean oil oxidation — Food Sci Technol Int 2012;18(3):271-80", "10.1177/1082013211427794", "PMID 22701060, 초록 확인"),
 pm(31, "Insecticidal Properties of Capsaicinoids and Glucosinolates Extracted from Capsicum chinense and Tropaeolum tuberosum — Insects 2019;10(5):132", "10.3390/insects10050132", "PMID 31064092, PMC6572632, 초록 확인"),
]

S = {}
S["overview"] = ("한눈에 보기",
"Anu덩이(Tropaeolum tuberosum)는 안데스 고산지대에서 덩이줄기를 먹으려고 기르는 한련과(Tropaeolaceae) 여러해살이 덩굴풀로, 현지에서는 마슈아(mashua)라는 이름으로 가장 널리 불린다[3, 5]. 페루·에콰도르에서는 마슈아, 콜롬비아에서는 쿠비오(cubio), 볼리비아에서는 이사뇨(isaño) 또는 아뉴(añu)라고 부른다[5]. 식약처 「식품원료 목록」에는 원료명 'Anu덩이줄기'(학명 Tropaeolum tuberosum)로 한 행이 올라 있고, 상태는 '사용가능', 사용 조건은 '사용가능부위 : 덩이줄기'다[1]. 따라서 이 목록으로 식품에 쓸 수 있는 부위는 덩이줄기뿐이고, 잎·꽃·줄기는 이 행에 포함되지 않는다[1]. 이 종을 원재료로 하는 건강기능식품 고시형 원료는 확인하지 못함.\n\n"
"덩이줄기는 건물 기준으로 탄수화물(주로 전분)이 대부분이고 단백질이 6.9–15.7 g/100 g 정도이며, 비타민 C와 칼륨이 비교적 많다[3, 5]. 이 종을 특징짓는 성분은 톡 쏘는 맛을 내는 방향족 글루코시놀레이트로, 재배종에서는 4-메톡시벤질 글루코시놀레이트(글루코오브리에틴)가 주성분이다[3, 6, 7]. 자주색·검은색 덩이줄기에는 델피니딘 계열 안토시아닌이 많아 항산화 연구가 활발하다[8]. 한편 수컷 쥐에 먹인 실험에서 테스토스테론·정자 수가 줄었다는 보고가 있어, 안전성 절에 따로 정리했다[9, 10, 11].")
S["history"] = ("역사와 전통적 이용",
"마슈아는 스페인 정복 이전부터 페루·볼리비아·에콰도르·콜롬비아에서 길러 온 작물이다[3]. 페루 하우하 계곡의 우아추마차이 동굴 고고학 자료를 근거로 재배화가 7,500년 이상 거슬러 올라간다고 정리되며, 에콰도르 키토에서는 2,500년 넘은 토기에서 마슈아 전분 알갱이가 확인되었다[3]. 전통적으로는 감자·오카·울루코 같은 다른 덩이줄기와 함께 삶거나 굽거나 스튜로 끓여 먹었다[3]. 쓴맛을 줄이려고 캐낸 덩이줄기를 며칠 햇볕에 두었다가 조리하는 관습이 있다[19].\n\n"
"안데스 민간요법에서는 신장·방광 통증을 덜고 상처·성병·폐와 피부 질환을 다스리는 데 썼다고 기록된다[12]. 또 성욕을 누르는 식물로 여겨져, 수도사나 병사에게 권했다는 전승이 전한다[3]. 이 생식 관련 믿음은 오늘날까지 이어지며, 1982년 연구는 이를 쥐 먹이 실험으로 확인하려 했다[9]. 최근에는 페루·볼리비아·에콰도르의 고급 식당이 안데스 토종 식재료로 다시 쓰고 있다[3]. 다만 시장 유통이 적고 쓴맛 때문에 소비자 수용이 낮아 여전히 덜 이용되는 작물로 분류된다[4].")
S["biology"] = ("식물학적 특징",
"마슈아는 덩굴지는 줄기와 잎자루가 잎 한가운데 붙는 둥근 방패 모양 잎을 가진 여러해살이 풀이다[3]. 잎은 어긋나고 가장자리가 밋밋하며 잎자루는 길고 털이 있다[3]. 꽃은 주황빛이 도는 붉은색이고 길고 붉은 꿀주머니(거)가 있어 관상용 한련과 닮았다[2]. 염색체는 2n = 4x = 52인 동질4배체로, 유전체 분석도 같은 기원을 지지했다[2].\n\n"
"덩이줄기는 길쭉한 원통형부터 원뿔형·달걀형까지 모양이 다양하고, 겉면에 얕은 눈이 흩어져 있다[3, 4]. 껍질과 속살 색은 노랑·흰색·분홍·자주·검정과 두 색이 섞인 형태까지 있고, 일부 계통은 길이가 10 cm를 넘는다[4]. 해발 2,800–4,100 m의 추운 기후와 척박한 땅에서 자라며, 4,300 m까지 분포한다고도 정리된다[3, 4]. 낮은 기온·강한 자외선 같은 고산 환경에 대한 방어로 글루코시놀레이트·페놀 화합물을 쌓는다고 해석된다[4]. 색이 짙은 계통일수록 안토시아닌과 페놀 함량, 항산화 값이 높은 경향이 있다[3, 5].")
S["related_species"] = ("이름과 가까운 종",
"한련속(Tropaeolum)은 약 90종의 신열대구 초본으로 이루어지며, 관상용 한련류와 덩이줄기를 만드는 여러 종을 포함한다[2]. 한련과는 배추목(Brassicales)에 속해 글루코시놀레이트를 만들지만, 십자화과 밖에서의 다양성은 아직 잘 밝혀지지 않았다[2]. 야생 아종은 재배 아종(subsp. tuberosum)과 달리 벤질·2-프로필·2-부틸 이소티오시아네이트도 내어, 같은 종 안에서도 화학형이 다르다[3, 9].\n\n"
"식약처 목록에는 같은 속 원료가 여럿 있으므로 학명과 부위로 구분해야 한다[1]. 한련(T. majus, 이명 금련)은 잎·꽃·순, Dwarf nasturtium(T. minus)은 잎이 사용가능하며, 이들은 덩이줄기를 먹는 마슈아와 다른 종이다[1]. T. brachyceras·T. patagonicum·T. sessilifolium·T. tricolor는 덩이줄기, T. leptophyllum은 뿌리가 각각 별도 행으로 올라 있다[1]. 이름이 비슷한 '한련초'는 국화과 Eclipta prostrata로, 한련속과 관계없는 제한적사용 원료다[1]. 페루 고산지에서 감자와 함께 작은 밭에 기르는 오카(Oxalis tuberosa)·울루코(Ullucus tuberosus)는 마슈아와 다른 종의 안데스 덩이줄기 작물이며, 자료를 볼 때 학명으로 구분해야 한다[3, 22].")
S["cultivation"] = ("재배와 산지",
"마슈아는 주로 페루·볼리비아·에콰도르·콜롬비아에서 기르고, 아르헨티나와 칠레에서도 적은 양이 재배된다[3]. 고산지대의 작은 밭에서 감자·오카·울루코와 섞어 기르기 때문에 생산량을 파악하기 어렵다[5]. 안데스 소농은 감자 밭에 마슈아를 함께 심는데, 마슈아의 벤질글루코시놀레이트가 해충과 병을 막아 준다고 믿는다[20]. 덩이줄기 글루코시놀레이트 추출물은 진딧물 실험에서 살충 효과를 보여 생물농약 재료로도 연구되었다[31].\n\n"
"주로 덩이줄기로 번식시키지만, 체세포 돌연변이와 농민의 선발·교환으로 유전 다양성이 높게 유지된다[4]. 콜롬비아 보야카의 25개 계통은 해발 2,800–3,200 m, 연평균 11–14 °C, 연강수량 1,000 mm 이상에서 수집되었다[4]. 생육 기간은 계통과 환경에 따라 달라, 에콰도르 자료에서 169일부터 282일까지 보고되었다[4]. 에콰도르 고산지 재배 개체에서는 잎맥 사이 황화·잎 말림·위축 같은 바이러스 증상이 흔했고, 포티바이러스류가 검출되었다[21]. 감자 T 바이러스도 마슈아에서 자연 감염이 확인되었다[22]. 1984년 분리된 시료에서는 새 포티바이러스(마슈아 바이러스 Y)의 전체 유전체가 해독되었다[23]. 국내 재배 면적과 생산량은 확인하지 못함.")
S["processing"] = ("가공과 이용",
"생 덩이줄기는 톡 쏘고 쓴맛이 있어, 전통적으로 햇볕에 며칠 두었다가 익혀 먹는다[19]. 9일간 햇볕에 둔 덩이줄기에서는 열충격 단백질과 방어 관련 단백질이 늘어, 햇볕 처리가 스트레스 반응을 일으킨다는 것이 확인되었다[19]. 삶기·전자레인지·굽기는 미로시나아제를 완전히 불활성화하며, 삶을 때는 물에 녹아 나가는 글루코시놀레이트 손실이 생긴다고 정리된다[4]. 12 °C 냉장 저장 뒤 말려 가루로 만들면 총 글루코시놀레이트가 26.6에서 3.6 µmol/g(건물)로 줄었다[3].\n\n"
"가루와 전분 가공 연구가 많다[3, 26, 27]. 페루 아야쿠초산 가루는 검은 계통이 노란 계통보다 단백질(17.6% 대 14.8%)과 지방(8.0% 대 6.7%)이 많았다[24]. 콜롬비아산 전분은 아밀로스 31.2%, B형 결정 구조를 보였고 생분해성 필름 재료로 검토되었다[26]. 전자레인지 데치기(900 W, 25초)는 건조 전 페놀·안토시아닌·카로티노이드를 늘리고 건조 중 안토시아닌 손실을 가장 적게 했다[25]. 압출 성형한 즉석 가루는 드럼 건조보다 페놀·글루코시놀레이트가 많았지만 비타민 C와 안토시아닌은 줄었다[28]. 에탄올 추출 페놀 분획(아세트산에틸 분획)은 대두유 저장·튀김 시험에서 산화를 늦췄다[30]. 과자·요구르트·발효주 시험도 대부분 실험실 규모다[3]. 식약처 「식품 등의 생산실적」에서 이 원료명의 품목은 확인하지 못함.")
S["genetics"] = ("유전 정보",
"2026년 독일 하이델베르크 식물원 소장 4배체 계통을 PacBio HiFi로 읽어 첫 마슈아 참조 유전체가 공개되었다[2]. 1차 조립본은 1,805개 콘티그, 총 1.30 Gb, 콘티그 N50 32.2 Mb, 가장 긴 콘티그 60 Mb였다[2]. BUSCO 완전성은 98.5%였고 그중 76.8%가 중복 유전자로 나타나 4배체 구조와 맞았다[2]. 반복 서열은 71.3%로 Gypsy·Copia 계열 LTR 레트로트랜스포존이 주를 이뤘고, 단백질 암호화 유전자 56,354개가 예측되었다[2].\n\n"
"유세포 분석의 2C 값은 2.48 Gb로, 4배체로 보면 단위 유전체가 약 620 Mb다[2]. 콜롬비아 보야카 농가 계통(B15)의 나노포어 리드를 이 참조에 맞추자 99.7%가 정렬되어, 지역이 다른 재래종 연구에도 쓸 수 있음이 확인되었다[2]. 엽록체 유전체는 약 150 kb, 미토콘드리아 유전체는 550,896 bp 스캐폴드로 조립되었다[2]. 페루 9개 주의 68개 계통은 북부·중부·남동부 세 유전 집단으로 나뉘었다[4]. 페루 우아누코 지역 비교에서는 ISSR 표지로 본 유전 다양성이 오카·울루코보다 높았다[4].")
S["safety"] = ("안전성",
"마슈아는 안데스에서 오래 먹어 온 식품이지만, 생식 기능 관련 동물 결과가 있어 주의 깊게 볼 필요가 있다[9, 10, 11]. 1982년 연구에서 덩이줄기를 먹인 수컷 쥐는 교미·수태 능력은 대조군과 같았으나 혈중 테스토스테론·디하이드로테스토스테론이 45% 낮았고, 연구진은 이소티오시아네이트와 관련된다고 보았다[9]. 동결건조 추출물 1 g/kg을 먹인 쥐에서는 12일째부터 정세포 수와 1일 정자 생산이 줄었으나 42일 뒤 혈청 테스토스테론 차이는 없었다[10]. 0.01–2 g/kg 용량 실험에서는 정자 수·운동성이 줄었고, 투여를 멈추고 24일 뒤에는 회복되었다[11]. 사람에서 이 효과를 확인한 연구는 확인하지 못함.\n\n"
"글루코시놀레이트가 분해되어 생기는 티오시아네이트는 요오드 섭취를 방해할 수 있지만, 전통적 마슈아 섭취와 갑상선 영향의 관련은 보고되지 않았다고 정리된다[4]. 에탄올 추출물을 생쥐에 2,000 mg/kg까지 준 급성 독성 시험에서는 사망이나 뚜렷한 이상이 없었다고 요약된다[4]. 항염·항암·항균 성분 연구는 세포 실험 수준이고, 검은 계통 추출물 1% 젤을 생쥐 상처에 바른 시험도 국소 적용 결과일 뿐이며[29], 항균 성분으로 보고된 비스포스포네이트는 오염물일 가능성이 크다는 지적을 받았다[13, 15, 16, 17]. 식약처 목록은 덩이줄기만 식품원료로 허용하며[1], 공공기관의 알레르기·잔류 정보는 확인하지 못함.")

KEYS = ["overview","history","biology","related_species","cultivation","processing","genetics","safety"]
sections = [{"key": k, "title": S[k][0], "body": S[k][1]} for k in KEYS]

def C(name, ko, cls, role, part, ct, act, src):
    return {"name": name, "name_ko": ko, "class": cls, "role": role, "part": part, "content_text": ct, "activity_ko": act, "source": src}
compounds = [
 C("Glucoaubrietin", "글루코오브리에틴(4-메톡시벤질 글루코시놀레이트)", "방향족 글루코시놀레이트", "marker", "덩이줄기",
   "콜롬비아 65계통에서 주성분으로 동정, 총 글루코시놀레이트 최고 25.8 µmol/g 건물[7]; 페루·볼리비아 시료에서 동정된 유일한 피크(탈황산형)[6]",
   "재배 아종의 주된 2차 대사산물; 가수분해 산물이 매운맛과 항균·항진균 활성의 근원[7, 9]", [6, 7, 9]),
 C("Glucosinalbin", "글루코시날빈(4-하이드록시벤질 글루코시놀레이트)", "방향족 글루코시놀레이트", "bioactive", "덩이줄기",
   "콜롬비아 계통에서 존재가 추정됨(함량 미기재)[7]; 주요 방향족 글루코시놀레이트 3종 중 하나로 정리[3]",
   "젖산균(L. rhamnosus GG)이 시험관에서 전량 대사[18]", [3, 7, 18]),
 C("Glucotropaeolin", "글루코트로패올린(벤질 글루코시놀레이트)", "방향족 글루코시놀레이트", "bioactive", "덩이줄기",
   "동결건조 추출물 3.7 g/100 g(벤질 글루코시놀레이트로 표기)[10]",
   "감자 혼작 시 병해충 억제 역할을 한다고 여겨지는 성분[20]; 젖산균이 시험관에서 전량 대사[18]", [10, 18, 20]),
 C("4-Methoxybenzyl isothiocyanate", "4-메톡시벤질 이소티오시아네이트", "이소티오시아네이트", "bioactive", "덩이줄기(가수분해 산물)",
   "재배 아종의 주된 가수분해 산물(함량 미기재)[3]",
   "매운맛 성분; 쥐의 테스토스테론 감소와 관련이 제기됨[9]", [3, 9]),
 C("N,N'-Bis(4-methoxybenzyl)thiourea", "N,N'-다이(4-메톡시벤질)티오우레아", "티오우레아 유도체", "bioactive", "덩이줄기",
   "덩이줄기에서 검출(함량 미기재)[3]",
   "예비 실험에서 에스트라디올 결합을 경쟁적으로 억제[9]", [3, 9]),
 C("Delphinidin 3-glucoside-5-acetylrhamnoside", "델피니딘 3-글루코사이드-5-아세틸람노사이드", "안토시아닌", "bioactive", "자주색 덩이줄기",
   "자주색 3개 유전형의 주요 색소 2종(델피니딘 3-소포로사이드-5-아세틸람노사이드 포함)이 520 nm 면적의 56.4–73.0%; 총 안토시아닌 45.5–131.9 mg 시아니딘-3-글루코사이드 당량/100 g 생것[8]",
   "덩이줄기 항산화 활성에 기여[8]", [8]),
 C("Cyanidin 3-sophoroside", "시아니딘 3-소포로사이드", "안토시아닌", "bioactive", "자주색 덩이줄기",
   "HPLC-DAD/MS로 확인된 11종 안토시아닌 중 하나(함량 미기재)[8]",
   "자주색 계통의 색과 항산화 활성에 기여[8]", [8]),
 C("Epicatechin", "(-)-에피카테킨", "플라반-3-올", "bioactive", "덩이줄기",
   "9.2 µg/g 건물[3]", "페놀 항산화 성분[3]", [3]),
 C("Ascorbic acid", "비타민 C(아스코르브산)", "비타민", "nutrient", "덩이줄기",
   "자주색 1.21–4.46, 노란색 0.53–1.54 mg/g 건물(HPLC)[5]; 에콰도르 고전 자료 77.37 mg/100 g 생것[3]",
   "수용성 항산화 비타민; 저장·냉동·조리 중 쉽게 손실[5]", [3, 5]),
 C("beta-Carotene", "베타카로틴", "카로티노이드", "nutrient", "덩이줄기",
   "노란 유전형 18.10–715.95 µg/g 건물, 자주색 5.65 µg/g 건물(HPLC)[5]",
   "프로비타민 A[5]", [5]),
 C("N-Oleoyldopamine", "N-올레오일도파민", "알카마이드", "bioactive", "자주색 덩이줄기",
   "생물활성 유도 분리로 얻음(함량 미기재)[13]",
   "세포 실험에서 TNF-α 억제 IC50 3.12 µM[13]; TRPV1 수용체 작용제(IC50 7.9 µM)[14]", [13, 14]),
 C("N-(2-Hydroxyethyl)-7Z,10Z,13Z,16Z-docosatetraenamide", "N-(2-하이드록시에틸)도코사테트라엔아마이드", "알카마이드", "bioactive", "검은색·자주색 덩이줄기",
   "검은 덩이줄기에서 분리(함량 미기재)[13]",
   "세포 실험에서 TNF-α 억제 IC50 1.56 µM, NF-κB 억제 1.77 µM[13]; TRPV1 작용제(IC50 3.2 µM)[14]", [13, 14]),
 C("Potassium", "칼륨", "무기질", "nutrient", "덩이줄기",
   "1,723.42–2,021.15 mg/100 g 건물(푸노 3개 유전형)[5]", "덩이줄기에서 가장 많은 무기질[5]", [5]),
 C("Amylose", "아밀로스", "전분 다당", "nutrient", "덩이줄기 전분",
   "분리 전분 27.44%[3]; 콜롬비아 쿠비오 전분 31.2%[26]", "전분의 호화·노화·필름 형성 특성을 좌우[3, 26]", [3, 26]),
]

nutrients = [
 {"form": "생 덩이줄기(가식부)", "basis": "100 g 생것 기준, 고전 문헌 평균값(리뷰 표 2 재인용)",
  "items": [{"name": "수분", "value": 85, "unit": "%"}, {"name": "탄수화물", "value": 9.7, "unit": "g"}, {"name": "단백질", "value": 1.5, "unit": "g"}, {"name": "지방", "value": 0.1, "unit": "g"}, {"name": "조섬유", "value": 0.8, "unit": "g"}],
  "source": [3]},
]

assays = [
 {"role": "literature", "compound": "Ascorbic acid", "compound_ko": "비타민 C(아스코르브산)", "part": "덩이줄기(동결건조 후 재수화)",
  "content": "자주색 1.21–4.46, 노란색-자주색 0.90–3.36, 노란색 0.53–1.54 mg/g 건물[5]", "method": "HPLC-UV",
  "conditions": {"instrument": "Agilent 1200 Series HPLC, 가변파장 검출기", "column": "Zorbax Eclipse XDB-C18, 250 × 4.6 mm, 5 µm (가드 칼럼 XDB-C18 12.5 × 4.6 mm, 5 µm)",
   "mobile_phase": "100 mM 아세트산암모늄 완충액–아세토니트릴 90:10 (v/v), 인산으로 pH 6.3", "gradient": "고정 비율", "flow": "1.0 mL/min", "temp": "25 °C",
   "detection": "UV 270 nm", "injection": "1.0 µL", "sample_prep": "시료 0.5 g + 4.5% 인산 1.5 mL 막자 균질 → 물 1.5 mL → 4000 × g 10분 원심 → 0.45 µm 여과·초음파 탈기(4 °C)",
   "standard": "L-아스코르브산 0.5–10.0 µg/mL", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "마슈아가 다른 덩이줄기보다 비타민 C가 많다는 영양 특성을 정량하는 지표로, 유전형·재배지에 따른 차이를 보여 줌; 전문 확인, 직선성·검출한계·회수율은 원문에 없음[5].",
  "source": [5], "url": "https://doi.org/10.1155/2022/7550987", "source_kind": "paper"},
 {"role": "literature", "compound": "beta-Carotene", "compound_ko": "베타카로틴", "part": "덩이줄기(동결건조 후 재수화)",
  "content": "노란색 18.10–715.95, 노란색-자주색 6.91–336.21, 자주색 5.65 µg/g 건물[5]", "method": "HPLC-UV/Vis",
  "conditions": {"instrument": "Agilent 1200 Series HPLC, 가변파장 검출기", "column": "Zorbax Eclipse SB-C18, 75 × 4.6 mm, 3.5 µm (가드 칼럼 XDB-C18 12.5 × 4.6 mm, 5 µm)",
   "mobile_phase": "메탄올–2-프로판올 50:50 (v/v)", "gradient": "고정 비율", "flow": "1.0 mL/min", "temp": "25 °C", "detection": "450 nm", "injection": "1.0 µL",
   "sample_prep": "시료 1 g + 2-프로판올 3 mL, 어두운 곳 200 rpm 30분(20 °C) → 2000 × g 10분(4 °C) 원심, 3회 재추출 → 0.45 µm 여과·초음파 탈기",
   "standard": "베타카로틴(헥산에 녹인 400 mg/L 원액)", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "속살 색(노란 계통)과 프로비타민 A 함량을 연결하는 지표; 전문 확인, 직선성·검출한계·회수율은 원문에 없음[5].",
  "source": [5], "url": "https://doi.org/10.1155/2022/7550987", "source_kind": "paper"},
 {"role": "literature", "compound": "Glucoaubrietin", "compound_ko": "글루코오브리에틴(4-메톡시벤질 글루코시놀레이트, 탈황산형으로 측정)", "part": "덩이줄기(껍질 벗겨 동결건조)",
  "content": "콜롬비아 65계통 총 글루코시놀레이트 최고 25.8 µmol/g 건물, 4-메톡시벤질 글루코시놀레이트가 주성분[7]; 페루·볼리비아 시료는 검출한계 근처부터 높은 값까지 변이(탈황산 글루코오브리에틴 단일 피크)[6]",
  "method": "역상 HPLC(효소 탈황산 추출물; AOCS 공정법)",
  "conditions": {"instrument": "", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "", "injection": "",
   "sample_prep": "효소로 탈황산한 추출물을 분석[7]", "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "재배 마슈아에서 거의 유일하게 검출되는 글루코시놀레이트로 이 종의 매운맛·생리활성의 대표 지표; [6]은 전문에서 AOCS 공정법에 따랐다고만 적었고, [7]은 전문 확인 못함이라 칼럼·이동상 조건은 비워 둠.",
  "source": [6, 7], "url": "https://doi.org/10.1002/jsfa.7689", "source_kind": "paper"},
]

d = {"slug": "tropaeolum-tuberosum", "name_ko": "Anu덩이", "name_en": "Mashua (añu, isaño, cubio)",
     "scientific_name": "Tropaeolum tuberosum Ruiz & Pav.",
     "aliases": ["Anu덩이줄기", "마슈아", "Mashua", "Añu", "Isaño", "Cubio"],
     "sections": sections, "compounds": compounds, "markers": [], "nutrients": nutrients, "assays": assays,
     "production": [], "world": [], "gi": [], "orgs": [], "sources": sources}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in sections: print(s["key"], len(s["body"]))
