import json
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "dossier.json"
ACC = "2026-11-02"


def pm(title, doi, pmid, kind):
    url = f"https://doi.org/{doi}" if doi else f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
    return {"title": f"{title} ({kind}) (PMID {pmid})", "url": url, "publisher": "PubMed", "accessed": ACC}


S = [
    {"title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 레이디스맨틀잎(Alchemilla vulgaris L., Ladys mantle), 사용가능부위: 잎, 사용가능; 같은 목록의 Ladys mantle잎(Alchemilla xanthochlora Rothm.)·고산알케밀라잎(Alchemilla alpina L.)·Parsley piert잎(Alchemilla arvensis (Scop.) / Aphanes arvensis (L.)) 행 포함",
     "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
    pm("Alchemilla vulgaris agg. (Lady's mantle) from central Balkan: antioxidant, anticancer and enzyme inhibition properties — RSC Adv 2019;9(64):37474-37483", "10.1039/c9ra08231j", "35542286", "전문 PMC9075513"),
    pm("Optimization of Deep Eutectic Solvent Extraction of Phenolic Acids and Tannins from Alchemilla vulgaris L. — Plants 2022;11(4):474", "10.3390/plants11040474", "35214807", "전문 PMC8876725"),
    pm("In vitro biotransformation of lady's mantle extracts via the human gut microbiota: the formation of phenolic metabolites and their impact on human normal and colon cancer cell lines — Front Pharmacol 2025;16:1504787", "10.3389/fphar.2025.1504787", "39911846", "전문 PMC11794788"),
    pm("Phenolic constituents from Alchemilla vulgaris L. and Alchemilla mollis (Buser) Rothm. at different dates of harvest — Z Naturforsch C 2012;67(11-12):529-40", None, "23413745", "초록"),
    pm("A review of the traditional uses, phytochemistry, pharmacology, and clinical evidence for the use of the genus Alchemilla (Rosaceae) — J Ethnopharmacol 2024;320:117439", "10.1016/j.jep.2023.117439", "37981119", "초록"),
    pm("Identification of a Collagenase-Inhibiting Flavonoid from Alchemilla vulgaris Using NMR-Based Metabolomics — Planta Med 2018;84(12-13):941-946", "10.1055/a-0630-2079", "29797306", "초록"),
    pm("Alchemilla vulgaris cytoprotection against methyl methanesulfonate by experimental and molecular docking approaches — Sci Rep 2026;16:4184", "10.1038/s41598-025-34304-9", "41484223", "전문 PMC12859078"),
    pm("Beyond Traditional Use of Alchemilla vulgaris: Genoprotective and Antitumor Activity In Vitro — Molecules 2022;27(23):8113", "10.3390/molecules27238113", "36500205", "초록"),
    pm("Vasorelaxant and blood pressure lowering effects of Alchemilla vulgaris: A comparative study of methanol and aqueous extracts — Pharmacogn Mag 2015;11(41):163-9", "10.4103/0973-1296.149733", "25709228", "초록"),
    pm("Endothelium-dependent vasorelaxant effect of Alchemilla vulgaris methanol extract: a comparison with the aqueous extract in rat aorta — Nat Prod Res 2014;28(23):2182-5", "10.1080/14786419.2014.926352", "24938755", "초록"),
    pm("Antimicrobial activity of bark extracts of Syzygium jambos (L.) Alston (Myrtaceae) — J Ethnopharmacol 2000;71(1-2):307-13 (A. vulgaris 추출물 탄닌 함량 비교 포함)", "10.1016/s0378-8741(99)00186-5", "10904178", "초록"),
    pm("Correlation between the in vitro antioxidant activity and polyphenol content of aqueous extracts from Bulgarian herbs — Phytother Res 2006;20(11):961-5", "10.1002/ptr.1985", "16906640", "초록"),
    pm("Analysis of Paralogs in Target Enrichment Data Pinpoints Multiple Ancient Polyploidy Events in Alchemilla s.l. (Rosaceae) — Syst Biol 2021;71(1):190-207", "10.1093/sysbio/syab032", "33978764", "초록"),
    pm("Initial Complete Chloroplast Genomes of Alchemilla (Rosaceae): Comparative Analysis and Phylogenetic Relationships — Front Genet 2020;11:560368", "10.3389/fgene.2020.560368", "33362846", "초록"),
    pm("Plastid phylogenomics of the tribe Potentilleae (Rosaceae) — Mol Phylogenet Evol 2023;190:107961", "10.1016/j.ympev.2023.107961", "37918684", "초록"),
    pm("Inflorescence preformation prior to winter: a surprisingly widespread strategy that drives phenology of temperate perennial herbs — New Phytol 2020;229(1):620-630", "10.1111/nph.16880", "32805759", "초록"),
    pm("Analysis of medium-term impact of multifunctional living mulches on soil biological fertility of an organic apple orchard — Sci Rep 2025;15:22422", "10.1038/s41598-025-06246-9", "40594971", "초록"),
    pm("Microbiological and toxicological quality of dried herbs — Lett Appl Microbiol 2011;52(6):573-80", "10.1111/j.1472-765X.2011.03040.x", "21375549", "초록"),
    pm("Treatment of Aphthous Stomatitis with topical Alchemilla vulgaris in glycerine — Clin Drug Investig 2006;26(10):567-73", "10.2165/00044011-200626100-00003", "17163290", "초록"),
    pm("Comparison of prophylactic effect of topical Alchemilla vulgaris in glycerine versus that of dexamethasone on postoperative sore throat after tracheal intubation using a double-lumen endobronchial tube: a randomized controlled study — Anesth Pain Med 2021;16(2):163-170", "10.17085/apm.20082", "33866772", "초록"),
    pm("Towards a modern approach to traditional use: in vitro and in vivo evaluation of Alchemilla vulgaris L. gel wound healing potential — J Ethnopharmacol 2019;238:111789", "10.1016/j.jep.2019.03.016", "30904703", "초록"),
    pm("Weight loss in animals and humans treated with 'weighlevel', a combination of four medicinal plants used in traditional Arabic and Islamic medicine — Evid Based Complement Alternat Med 2011:874538", "10.1093/ecam/nen067", "18952688", "초록"),
    pm("Beneficial Effects of Alchemilla vulgaris in DHEA-Induced Rat Model of Polycystic Ovary Syndrome — Reprod Sci 2025;32(7):2453-2466", "10.1007/s43032-025-01885-9", "40550985", "초록"),
    pm("Alchemilla vulgaris modulates isoproterenol-induced cardiotoxicity: interplay of oxidative stress, inflammation, autophagy, and apoptosis — Front Pharmacol 2024;15:1394557", "10.3389/fphar.2024.1394557", "39170697", "초록"),
    pm("Antimelanoma Effects of Alchemillae vulgaris herba: A Comprehensive In Vitro and In Vivo Study — Diseases 2024;12(6):125", "10.3390/diseases12060125", "38920557", "초록"),
    pm("Traditional plant treatments for diabetes. Studies in normal and streptozotocin diabetic mice — Diabetologia 1990;33(8):462-4", "10.1007/BF00405106", "2210118", "초록"),
    pm("Presence of Alchemilla alpina L. together with Alchemilla vulgaris L. in a tea for high blood pressure — J Pharm Belg 1950;5(11-12):335-8", None, "14804274", "서지 정보만, 초록 없음"),
    pm("Ethnoveterinary medicines used for ruminants in British Columbia, Canada — J Ethnobiol Ethnomed 2007;3:11", "10.1186/1746-4269-3-11", "17324258", "초록"),
    pm("Smoke water and smoke-derived karrikinolide, KAR1, improved germination in some medicinal and aromatic plants — Sci Rep 2026;16:865 (Alchemilla xanthochlora 포함)", "10.1038/s41598-025-30823-7", "41495119", "초록"),
    pm("Powdered Herbal Extracts by Freeze and Spray Drying: Formulation Design, Processing, and Physicochemical and Antiglycation Properties — Foods 2026;15(19):3371", "10.3390/foods15193371", "42883478", "초록"),
    pm("Protective effects of Aronia melanocarpa juices either alone or combined with extracts from Rosa canina or Alchemilla vulgaris in a rat model of indomethacin-induced gastric ulcers — Food Chem Toxicol 2019;132:110739", "10.1016/j.fct.2019.110739", "31374297", "초록"),
    pm("Effects of Alchemilla vulgaris and glycerine on epithelial and myofibroblast cell growth and cutaneous lesion healing in rats — Phytother Res 2007;21(4):369-73", "10.1002/ptr.2060", "17236169", "초록"),
    pm("Flavonoids extracted from Ribes nigrum L. and Alchemilla vulgaris L.: in vitro inhibitory activities on elastase, trypsin and chymotrypsin; angioprotective activities compared in vivo — J Pharmacol 1986;17(1):21-7", None, "3635653", "초록(프랑스어 논문 영문 초록)"),
    pm("Effect of 158 herbal remedies on human TRPV1 and the two-pore domain potassium channels KCNK2, 3 and 9 — J Tradit Complement Med 2020;10(5):446-453 (Alchemilla xanthochlora herba 포함)", "10.1016/j.jtcme.2020.04.005", "32953560", "초록"),
    pm("Prospects for the use of the herb lady's mantle in geriatrics — Adv Gerontol 2019;32(1-2):180-184 (러시아어 논문 영문 초록)", None, "31228386", "초록"),
]
for i, s in enumerate(S, 1):
    s["n"] = i
SOURCES = [{"n": s["n"], "title": s["title"], "url": s["url"], "publisher": s["publisher"], "accessed": s["accessed"]} for s in S]

SECTIONS = [
    ("overview", "한눈에 보기",
     "레이디스맨틀(Alchemilla vulgaris L.)은 장미과(Rosaceae) 알케밀라속의 여러해살이풀로, 영어로는 lady's mantle이라 부른다[1, 2]. 식약처 「식품원료 목록」에는 학명 Alchemilla vulgaris L., 영어 이름 Ladys mantle로 '레이디스맨틀잎'이 올라 있고, 사용 조건이 '사용가능부위 : 잎'인 사용가능 원료다[1]. 따라서 식품에는 잎만 쓸 수 있다[1]. 이 종을 원재료로 하는 건강기능식품 고시형 원료는 확인하지 못함. 같은 목록에는 Alchemilla xanthochlora Rothm.(Ladys mantle잎), 고산알케밀라(A. alpina), Parsley piert(A. arvensis / Aphanes arvensis)가 각각 별도 원료로 올라 있으며, 이 자료에는 그 종들의 값을 섞지 않았다[1].\n\n"
     "A. vulgaris는 생김새가 비슷한 여러 소종(microspecies)을 묶은 집합종(agg.)으로 다루는 경우가 많다[2]. 잎과 지상부의 대표 성분은 아그리모닌·페둔쿨라진 같은 엘라기타닌, 갈산·엘라그산, 퀘르세틴 글루쿠로나이드 등의 플라보노이드다[4, 5]. 세르비아 시료의 에탄올 추출물에서는 UHPLC-HRMS로 45개 화합물이 검출되었다[9]. 잎(잎자루 포함)만 따로 분석한 연구로는 독일의 LC-MS/MS 연구가 있고, 나머지 연구 대부분은 꽃 핀 지상부 전체를 시료로 썼다[2, 3, 5, 8]."),
    ("history", "역사와 이용",
     "레이디스맨틀은 유럽 민간요법에서 생리통·월경과다 같은 부인과 질환, 설사, 상처·궤양·습진 같은 피부 질환에 써 온 약초다[3, 6]. 발칸 지역 기록에는 수렴·지사 작용과 외음부 가려움, 자궁 출혈, 생리통에 쓴 예가 있고, 세르비아에는 '성모의 망토'라는 뜻의 민간 이름이 전한다[2]. 러시아에서는 이 풀이 노인의학에서 항염·혈당강하·혈압강하·가벼운 이뇨 등의 예방·유지 요법 원료로 소개되었다[36]. 캐나다 브리티시컬럼비아의 가축 민간요법 조사에서는 반추가축의 태반 정체에 이 풀을 먹인다는 보고가 있었다[29].\n\n"
     "전통적으로는 마른 풀 2–4 g을 뜨거운 물 150 mL에 10분 우려 하루 세 번 마시는 우림차로 먹는다고 소개되었고, 유럽약전에도 생약 모노그래프가 있다[4]. 1950년 벨기에에서는 고혈압용 차에 A. vulgaris와 함께 고산알케밀라(A. alpina)가 섞여 있던 사례가 보고되었다[28]. 1980년대 프랑스 연구에서는 이 풀의 플라보노이드 분획이 돼지 췌장 엘라스테이스 활성을 0.16 mg/mL에서 50% 억제했다[34]. 유럽 의약품청(EMA) 약초위원회와 ESCOP 모노그래프 원문은 이 환경에서 사이트가 열리지 않아 확인하지 못함. 우리나라에서 이 풀을 먹어 온 전통 기록은 확인하지 못함."),
    ("biology", "식물학적 특징",
     "알케밀라속은 약 1000종으로 이루어지며 유럽에서만 300종 넘게 기재되었다[6]. 레이디스맨틀은 높이 30–50 cm의 반로제트형 풀로, 주름지고 얕게 갈라진 콩팥 모양–반원형 잎과 노란빛 도는 녹색의 작은 꽃 무리를 가진다[2]. 세르비아에서는 6–9월에 꽃이 피고 길가·초지·산비탈에서 자라며, 한 연구의 채집지는 해발 1234 m의 습한 초지였다[2]. 분포는 유럽 거의 전역과 유럽 러시아·시베리아, 서아시아, 북아메리카에 걸친다고 정리되었다[3]. 북반구 온대, 특히 서늘한 아한대의 유럽·아시아에 주로 분포한다는 설명도 있다[4].\n\n"
     "알케밀라속은 가을에 겨울눈 안에 꽃차례를 미리 만들어 두는 종이 흔한 속으로 꼽혔고, 이런 종은 그렇지 않은 종보다 평균 38일 일찍 꽃을 피웠다[17]. 잎의 페놀 성분은 개화 초기인 5월보다 개화 말기인 8월에 더 많이 쌓였고, 특히 엘라기타닌이 늘었다[5]. 국내 자생 여부는 확인하지 못함."),
    ("related_species", "이름과 가까운 종",
     "A. vulgaris는 분류 지위가 완전히 정리되지 않아 대개 여러 소종의 집합으로 다루며, 이 소종들은 아종이나 변종으로 취급되기도 했다[2]. 세르비아 식물지는 A. vulgaris L.를 유효한 이름으로 보고 3개 아종을 인정한다[2]. 그래서 논문 속 'A. vulgaris' 시료가 정확히 어느 소종인지는 대부분 확인하지 못함. 식약처 목록은 A. vulgaris(레이디스맨틀잎)와 A. xanthochlora(Ladys mantle잎)를 별개 원료로 올렸고 둘 다 잎이 사용가능 부위다[1]. A. xanthochlora 약초는 사람 이온통로(TRPV1·KCNK) 검색 연구 등에서 따로 다뤄졌으며 이 자료의 성분 값에는 넣지 않았다[35]. 스위스에서 시험한 A. xanthochlora 종자는 연기 유래 발아촉진물질 KAR1에 반응하지 않았다[30].\n\n"
     "정원용으로 흔한 A. mollis의 잎에서는 카테킨, 프로시아니딘 삼량체, 켐페롤 글루쿠로나이드가 검출되어 A. vulgaris와 구별되었다[5]. 고산알케밀라(A. alpina)와 Parsley piert(Aphanes arvensis)도 식약처 목록에 별도 원료로 있다[1]. 엽록체 유전체 계통 연구에서 넓은 뜻의 알케밀라속은 Potentilleae 족 Fragariinae 아족에 속하며 Sibbaldianthe·Comarum·Farinopsis와 한 무리를 이룬다[16]."),
    ("cultivation", "재배와 산지",
     "국내 재배 면적·생산량 통계(통계청·농식품부 특용작물 생산실적)에서 레이디스맨틀 품목은 확인하지 못함. 논문 시료는 대부분 야생 채취품이거나 약초상·약국에서 산 마른 풀이었다[2, 3, 8]. 세르비아 연구진은 자국과 주변 시장에 약초를 공급하는 야생 채취지의 개체군을 골라 분석했다[2]. 이탈리아 몰리세 지방의 가족 농장에서 재배·건조한 약초 51점을 조사한 연구에는 A. vulgaris도 포함되었다[19].\n\n"
     "폴란드의 유기농 사과 과수원에서는 A. vulgaris를 나무 밑 살아 있는 피복식물(living mulch)로 4년간 길렀는데, 토양 양분 수준은 달라지지 않았고 토양 세균 군집 구성은 바뀌었다[18]. 수확 시기에 따라 성분이 달라져, 개화 말기인 8월에 거둔 잎에서 페놀 성분, 특히 엘라기타닌이 더 많았다[5]. 지리적 표시 등록과 생산자 단체는 확인하지 못함."),
    ("processing", "가공과 이용",
     "식약처 목록상 이 종은 잎을 식품원료로 쓸 수 있고, 흔한 섭취 형태는 마른 풀을 뜨거운 물에 우린 차다[1, 4]. 불가리아 약초 23종의 물 추출물 가운데 레이디스맨틀의 ABTS 항산화능(4.79 mM)이 가장 높았다[13]. 추출 용매에 따라 성분이 크게 달라져, 세르비아 시료에서는 에틸아세테이트 추출물에서만 갈산(2465.79 µg/g)과 퀘르세틴(4541.70 µg/g)이 정량한계 이상으로 나왔다[2]. 메탄올 추출물에는 퀘르세틴이, 물 추출물에는 갈산이 많았다[11].\n\n"
     "물로 30 °C에서 90분 추출하면 갈산이 2.21 µg/mg 나와 염화콜린:요소(1:2) 공융용매보다 많았지만, 엘라그산(12.08 µg/mg)과 가수분해성 탄닌(178.02 µg TAE/mg)은 공융용매가 더 많이 뽑아냈다[3]. 레이디스맨틀을 포함한 추출물 분말 비교에서 분무건조 분말은 수분 1.13–4.18%로 동결건조 분말(4.32–10.49%)보다 낮았고, 부형제를 넣지 않은 분말이 총페놀과 항산화능이 더 높았다[31]. 아로니아 주스에 이 풀 추출물을 섞은 음료는 쥐 위궤양 모델에서 시험한 네 가지 주스 가운데 보호 효과가 가장 컸다[32]. 사람 장내 미생물과 배양하면 엘라그산이 우로리틴 C로 바뀌고 플라보노이드 배당체가 사라졌다[4]. 국내 건강기능식품 생산실적에서 이 원료 품목은 확인하지 못함."),
    ("genetics", "유전 정보",
     "알케밀라속은 잡종 형성, 수정 없이 씨를 맺는 자율 무수정생식(apomixis), 배수성 때문에 종을 가르기가 어렵다[15]. 68종을 표적 유전자 포획으로 분석한 연구는 넓은 뜻의 알케밀라 전체가 동질배수화로 생겨났고, 그 안의 주요 4개 무리는 다시 이질배수화로 생겨났다고 추정했다[14]. 알케밀라속 최초의 엽록체 전체 유전체는 아프리카산 2종에서 해독되었으며 길이 152,438 bp와 152,427 bp, 고유 유전자 114개였다[15]. 이 2종은 A. vulgaris가 아니어서, A. vulgaris 자체의 엽록체·핵 유전체와 염색체 수는 확인하지 못함.\n\n"
     "플라스티드 유전체 계통 연구는 알케밀라속이 속한 Potentilleae 족이 에오세 중기에 기원했다고 추정했다[16]. 무수정생식 집합종이라는 특성 때문에, 연구마다 다른 성분 결과를 해석할 때는 시료의 소종 동정과 채집지를 함께 봐야 한다[2, 15]. 시판 약재는 유럽약전 방법(현미경 검사·박층크로마토그래피)으로 동정한 예가 있다[4]."),
    ("safety", "안전성",
     "식약처 「식품원료 목록」에서 레이디스맨틀은 잎만 쓸 수 있는 사용가능 원료이며 다른 부위는 사용 부위로 올라 있지 않다[1]. 국내 공공기관의 알레르기·잔류물질·독성 성분 정보는 확인하지 못함. 이탈리아 건조 약초 조사에서 A. vulgaris를 포함한 시료들은 아플라톡신 B1 기준을 넘지 않았지만, 시료 전체로는 29.4%가 중온성 세균 권고 한계를 넘었다[19]. 유럽약전 방법으로 잰 이 풀 추출물의 탄닌은 46%였다[12].\n\n"
     "쥐 다낭성 난소 증후군 모델(체중 100 g당 50 mg, 35일)과 생쥐 심장 손상 모델(100·200 mg/kg)에서는 먹인 추출물의 보호 효과가 보고되었다[24, 25]. 생쥐 흑색종 모델에서는 전신 독성이 관찰되지 않았다[26]. 메탄올 추출물은 고혈압 쥐의 혈압을 낮췄으나 물 추출물은 그렇지 않았다[10]. 정상 생쥐에 사료의 6.25%로 12일 먹였을 때 섭식·체중·혈당·인슐린은 변하지 않았다[27]. 이 풀을 포함한 4종 식물 혼합 정제는 쥐 LD50이 15.3 g/kg이었고 성인 66명이 3개월 먹는 동안 부작용이 보고되지 않았다[23].\n\n"
     "사람 연구는 주로 바르는 제제였다[20–22]. 3% 추출물 글리세린 겔을 입안 아프타 궤양 환자 48명에게 바른 공개 시험에서 내약성이 좋았다[20]. 기관 삽관 후 인후통 예방 무작위 시험(94명 등록)에서는 이 글리세린 제제를 뿌린 군과 덱사메타손 군의 차이가 없었다[21]. 쥐 피부 상처에서는 3% 제제가 치유를 하루 앞당겼다[33]. 먹는 형태의 단독 임상시험, 임신·수유 중 안전성, 약물 상호작용은 확인하지 못함."),
]

COMPOUNDS = [
    ("Agrimoniin", "아그리모닌", "엘라기타닌(이량체)", "marker", "잎(잎자루 포함)·지상부",
     "잎 아세톤/물 추출물의 주요 페놀 성분(LC-MS/MS, 함량 수치는 초록에 없음)[5]; 지상부 공융용매 추출물에서 [M-H]- m/z 1870.158로 검출(정량 안 함)[4]",
     "이 속의 대표 가수분해성 탄닌; 장내 미생물에 의해 엘라그산·우로리틴으로 분해되는 전구체", [4, 5]),
    ("Pedunculagin", "페둔쿨라진", "엘라기타닌", "marker", "잎(잎자루 포함)·지상부",
     "아그리모닌과 함께 주요 페놀 성분(함량 수치는 초록에 없음)[5]; α·β 이성질체 검출, m/z 783.07[4]",
     "엘라기타닌 구성 성분", [4, 5]),
    ("Sanguiin H-10", "산귀인 H-10", "엘라기타닌(이량체)", "bioactive", "잎·지상부",
     "잎 추출물에서 검출(함량 수치는 초록에 없음)[5]; 지상부 공융용매 추출물에서 이성질체 m/z 1567.15 검출[4]",
     "엘라기타닌 구성 성분", [4, 5]),
    ("Ellagic acid", "엘라그산", "페놀산(엘라기타닌 가수분해물)", "marker", "지상부(마른 풀)",
     "0.74–12.76 µg/mg(염화콜린:요소 공융용매, 교반·가열); 최적 조건 12.08 µg/mg; 30% 에탄올 70 °C 30분 7.44 µg/mg(HPLC-UV)[3]",
     "사람 장내 미생물 배양에서 우로리틴 C로 전환됨[4]", [3, 4]),
    ("Gallic acid", "갈산", "페놀산", "marker", "지상부(마른 풀)",
     "에틸아세테이트 추출물 2465.79 ± 0.01 µg/g 건조중량(메탄올·에탄올·물 추출물은 정량한계 미만)[2]; 공융용매 0.00–1.89 µg/mg, 물 30 °C 90분 2.21 µg/mg(HPLC-UV)[3]",
     "물 추출물에 많은 페놀산[11]", [2, 3, 11]),
    ("Catechin", "카테킨", "플라반-3-올", "bioactive", "지상부(개화기)",
     "에틸아세테이트 추출물 8144.98 ± 0.01 µg/g, 메탄올 704.55 ± 0.54 µg/g, 에탄올 396.16 ± 0.01 µg/g 건조중량(LC-MS/MS)[2]; 독일 시료 잎에서는 검출되지 않고 A. mollis에서만 검출[5]",
     "에틸아세테이트 추출물의 최다 성분; 시료(소종·산지)에 따라 검출 여부가 다름", [2, 5, 8]),
    ("Quercetin", "퀘르세틴", "플라보놀", "bioactive", "지상부",
     "에틸아세테이트 추출물 4541.70 ± 0.04 µg/g 건조중량(다른 용매 추출물은 정량한계 미만)(LC-MS/MS)[2]",
     "메탄올 추출물에 많고 혈관 이완 작용과 관련지어짐[11]", [2, 11]),
    ("Quercetin 3-O-glucuronide", "퀘르세틴-3-O-글루쿠로나이드", "플라보놀 배당체", "marker", "잎(잎자루 포함)·지상부",
     "잎 추출물 플라보노이드 분획의 주성분(함량 수치는 초록에 없음)[5]",
     "생물활성 유도 분획으로 분리; 시험관에서 독시사이클린보다 강한 콜라게네이스 억제[7]", [5, 7]),
    ("Luteolin 7-O-glucoside", "루테올린-7-O-글루코사이드", "플라본 배당체", "bioactive", "지상부",
     "에탄올 추출물 1186.34 ± 0.24 µg/g, 메탄올 903.94 ± 0.03 µg/g 건조중량(LC-MS/MS)[2]",
     "알코올 추출물의 주요 플라보노이드 배당체", [2]),
    ("Kaempferol 3-O-glucoside", "켐페롤-3-O-글루코사이드", "플라보놀 배당체", "bioactive", "지상부",
     "에틸아세테이트 추출물 1038.52 ± 1.01 µg/g, 메탄올 195.55 ± 0.33 µg/g 건조중량(LC-MS/MS)[2]",
     "플라보노이드 배당체 구성 성분", [2]),
    ("Chlorogenic acid", "클로로겐산", "하이드록시신남산 에스터", "bioactive", "잎·지상부",
     "에탄올 추출물 510.43 ± 1.66 µg/g, 메탄올 258.01 ± 1.05 µg/g 건조중량(LC-MS/MS)[2]; 잎 추출물에서도 검출[5]",
     "페놀산 구성 성분", [2, 5]),
    ("Caffeic acid", "카페산", "하이드록시신남산", "bioactive", "지상부",
     "에틸아세테이트 추출물 1138.54 ± 0.30 µg/g, 에탄올 69.19 ± 1.11 µg/g 건조중량(LC-MS/MS)[2]",
     "에틸아세테이트 추출물의 주요 페놀산", [2, 8]),
    ("Rutin", "루틴", "플라보놀 배당체", "bioactive", "지상부",
     "메탄올 추출물 71.06 ± 0.05 µg/g, 물 32.66 ± 2.05 µg/g 건조중량(에틸아세테이트는 정량한계 미만)(LC-MS/MS)[2]",
     "터키 시료 70% 에탄올 추출물의 주요 페놀 성분 가운데 하나로 보고[8]", [2, 8]),
    ("Urolithin C", "우로리틴 C", "엘라그산 장내 대사체", "bioactive", "(식물에는 없음) 장내 미생물 대사체",
     "지상부 추출물을 사람 분변(공여자 1명)과 24시간 배양한 시료에서만 검출(정량 안 함)[4]",
     "엘라기타닌이 장에서 분해되어 생기는 대사체; 원래 추출물에는 없음", [4]),
]

ASSAYS = [
    {"role": "literature", "compound": "Gallic acid; Ellagic acid", "compound_ko": "갈산·엘라그산",
     "part": "지상부(마른 풀, 보스니아헤르체고비나 약초상 2018년 봄 구입; 부위 세부는 본문에 없음)",
     "content": "갈산 0.00–1.89 µg/mg, 엘라그산 0.00–12.76 µg/mg(추출 조건별); 물 30 °C 90분 갈산 2.21 µg/mg",
     "method": "HPLC-UV",
     "conditions": {"instrument": "Agilent 1260 Infinity II", "column": "ZORBAX Eclipse Plus C18, 4.6 × 100 mm, 5 µm",
                    "mobile_phase": "A: 0.25% H3PO4 + 1.5% 테트라하이드로퓨란(초순수), B: 메탄올",
                    "gradient": "0–5분 A 100%; 5–10분 A 100→85%; 10–20분 85→70%; 20–40분 70→50%; 40–45분 50%; 45–47분 50→0%; 47–55분 A 0%",
                    "flow": "2 mL/min", "temp": "25 °C(실온)", "detection": "UV 220·270 nm(머무름시간 갈산 2.693분, 엘라그산 24.829분)",
                    "injection": "35 µL",
                    "sample_prep": "분쇄·체질한 마른 풀 50 mg + 용매(염화콜린 기반 공융용매+물 또는 물·에탄올·메탄올) 1 mL; 자석교반(1500 rpm)·초음파·비드밀 추출",
                    "standard": "갈산(≥98.0%), 엘라그산(≥95.0%) 외부 검량, 메탄올 저장액 7농도(10–500 mg/L)",
                    "linearity": "R² 0.99964(갈산), 0.99909(엘라그산)", "lod": "", "loq": "", "recovery": ""},
     "rationale": "갈산·엘라그산은 이 풀에 많은 가수분해성 탄닌의 구성 단위여서 탄닌 추출 효율의 지표로 쓰였다. 전문(Methods)에서 조건을 옮겼으며 검출·정량한계와 회수율은 원문에 없다[3].",
     "source": [3], "url": "https://doi.org/10.3390/plants11040474", "source_kind": "paper"},
    {"role": "literature", "compound": "Agrimoniin; Pedunculagin; Quercetin glucuronide", "compound_ko": "아그리모닌·페둔쿨라진·퀘르세틴 글루쿠로나이드",
     "part": "지상부(마른 풀, 폴란드 시판품, 유럽약전 11판 모노그래프 방법으로 동정)",
     "content": "",
     "method": "LC-PDA-ESI-TOF/MS",
     "conditions": {"instrument": "Agilent 1260 Infinity LC(PDA) + Agilent 6230 TOF/MS(ESI)",
                    "column": "Poroshell 120 EC-C18, 250 × 2.1 mm(입자 크기 원문 표기 '4 mm')",
                    "mobile_phase": "A: 0.1% 포름산, B: 아세토니트릴/물(9:1)",
                    "gradient": "0–5분 B 0%; 5–40분 0→12.5%; 40–105분 12.5→25%; 105–110분 25→100%; 110–115분 100%; 이후 초기 조건 재평형",
                    "flow": "0.350 mL/min", "temp": "25 °C",
                    "detection": "PDA 280 nm(탄닌)·360 nm(플라보노이드); ESI 음·양이온, 캐필러리 2500·4000 V, 건조가스(N2) 9 L/min, 분무 35 psi, 365 °C, m/z 50–2000",
                    "injection": "10 µL",
                    "sample_prep": "염화콜린:요소(1:2) 공융용매 + 물 30%로 초음파 추출(40 °C, 30분), 20 mg/mL",
                    "standard": "엘라그산·브레비폴린카복실산(시판), 3-O-카페오일퀸산·페둔쿨라진(분리 표준품); 나머지는 문헌·분절 양상으로 잠정 동정",
                    "linearity": "", "lod": "", "loq": "", "recovery": ""},
     "rationale": "아그리모닌·페둔쿨라진 같은 엘라기타닌과 퀘르세틴 글루쿠로나이드는 이 풀의 특징 성분으로 반복 보고되었다. 전문(Methods)에서 조건을 옮겼으나 정성 분석이라 함량은 없다[4, 5].",
     "source": [4], "url": "https://doi.org/10.3389/fphar.2025.1504787", "source_kind": "paper"},
    {"role": "literature", "compound": "Catechin; Quercetin; Gallic acid (phenolics)", "compound_ko": "카테킨·퀘르세틴·갈산 등 페놀 성분",
     "part": "지상부(세르비아 블라시나 호수 자생지, 2017년 개화기 채집, 자연 건조)",
     "content": "에틸아세테이트 추출물 카테킨 8144.98 µg/g, 퀘르세틴 4541.70 µg/g, 갈산 2465.79 µg/g 건조중량",
     "method": "LC-MS/MS(dynamic MRM)",
     "conditions": {"instrument": "", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "",
                    "detection": "dynamic MRM, 화합물별 최적화 조건(세부값은 본문에 없음)", "injection": "",
                    "sample_prep": "마른 풀을 80% 메탄올·70% 에탄올·70% 에틸아세테이트·증류수로 실온 24시간 침지, 여과·건조 후 DMSO에 10 mg/mL로 녹임",
                    "standard": "45종 페놀 표준물질 검량선(정량 26종)", "linearity": "", "lod": "", "loq": "", "recovery": ""},
     "rationale": "용매별 추출물에서 페놀 성분을 정량해 활성(항산화·효소 억제·세포독성)과 연결한 연구다. 전문을 확인했으나 크로마토그래피 조건은 이전 논문을 인용해 본문에 없어 칸을 비웠다[2].",
     "source": [2], "url": "https://doi.org/10.1039/c9ra08231j", "source_kind": "paper"},
]

d = {
    "slug": "alchemilla-vulgaris",
    "name_ko": "레이디스맨틀",
    "name_en": "Lady's mantle",
    "scientific_name": "Alchemilla vulgaris L.",
    "aliases": ["레이디스맨틀잎", "Ladys mantle", "lady's mantle", "Alchemilla vulgaris agg.", "Alchemillae herba"],
    "sections": [{"key": k, "title": t, "body": b} for k, t, b in SECTIONS],
    "compounds": [{"name": a, "name_ko": b, "class": c, "role": r, "part": p, "content_text": ct, "activity_ko": act, "source": s}
                  for a, b, c, r, p, ct, act, s in COMPOUNDS],
    "markers": [],
    "assays": ASSAYS,
    "nutrients": [],
    "production": [],
    "world": [],
    "gi": [],
    "orgs": [],
    "sources": SOURCES,
}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
for s in d["sections"]:
    print(s["key"], len(s["body"]))
