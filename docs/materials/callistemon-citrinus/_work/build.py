import json
from pathlib import Path
OUT = Path("/home/user/hfoodguide-wave3/docs/materials/callistemon-citrinus/dossier.json")
A = "2026-11-02"
def pm(n, title, doi, pmid, pmc=None, note=""):
    t = f"{title} (PMID {pmid}{', ' + pmc if pmc else ''}){note}"
    return {"n": n, "title": t, "url": f"https://doi.org/{doi}" if doi else f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/", "publisher": "PubMed", "accessed": A}
S = [
 {"n":1,"title":"식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 병솔나무(Callistemon citrinus (Curtis) Skeels / Callistemon lanceolatus, Bottlebrush Crimson) 병솔나무잎, 사용가능부위: 잎, 사용가능","url":"https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020","publisher":"식품의약품안전처","accessed":"2026-10-13"},
 pm(2,"In silico and in vitro studies of isolated constituents from Callistemon citrinus leaves: Anti-microbial potential and inhibition of iNOS activity — Phytochemistry 2021;112745 (초록)","10.1016/j.phytochem.2021.112745","33845184"),
 pm(3,"Phenolic profiling unravels the chemopreventive components of Melaleuca citrina (Curtis) Dum.Cours. fruits by integrating LC-MS/MS, in vitro studies, docking and molecular dynamic simulation — Nat Prod Res 2025 (초록)","10.1080/14786419.2025.2552974","40857134"),
 {"n":4,"title":"Australian Native Plants Society (Australia) — Callistemon citrinus (syn. Melaleuca citrina) 식물 정보; Craven의 Callistemon → Melaleuca 이전(Novon 2006)과 기관별 수용 여부 (이 환경에서 페이지를 열지 못해 WebSearch 요약으로만 확인)","url":"https://anpsa.org.au/plant_profiles/callistemon-citrinus-syn-melaleuca-citrina/","publisher":"Australian Native Plants Society (Australia)","accessed":A},
 pm(5,"Phylogeny of Melaleuca, Callistemon, and Related Genera of the Beaufortia Suballiance (Myrtaceae) Based on 5S and ITS-1 Spacer Regions of nrDNA — Cladistics 1999;15(2):151-172 (초록)","10.1111/j.1096-0031.1999.tb00257.x","34902912"),
 pm(6,"Chemopreventive effect of Callistemon citrinus (Curtis) Skeels against colon cancer induced by 1,2-dimethylhydrazine in rats — J Cancer Res Clin Oncol 2019 (초록)","10.1007/s00432-019-02905-3","30923945","PMC11810365"),
 pm(7,"Development and validation of a high performance thin layer chromatographic method for determination of 1,8-Cineole in Callistemon Citrinus — Pharmacognosy Res 2014;6(2):143-7 (전문)","10.4103/0974-8490.129034","24761119","PMC3996751"),
 pm(8,"Evaluation of the toxicology, anti-lipase, and antioxidant effects of Callistemon citrinus in rats fed with a high fat-fructose diet — Pharm Biol 2022 (전문)","10.1080/13880209.2022.2099907","35938503","PMC9361760"),
 pm(9,"Development and Evaluation of Phytosomes Containing Callistemon citrinus Leaf Extract: A Preclinical Approach for the Treatment of Obesity in a Rodent Model — Pharmaceutics 2023;15(9):2178 (전문)","10.3390/pharmaceutics15092178","37765149","PMC10535757"),
 pm(10,"Chemical Composition and In Vitro Cytotoxicity of Essential Oils from Leaves and Flowers of Callistemon citrinus from Western Himalayas — PLoS One 2015;10(8):e0133823 (초록)","10.1371/journal.pone.0133823","26308916","PMC4550473"),
 pm(11,"Terpene constituents of the aerial parts, phenolic content, antibacterial potential, free radical scavenging and antioxidant activity of Callistemon citrinus (Curtis) Skeels from Eastern Cape Province of South Africa — BMC Complement Altern Med 2017 (초록)","10.1186/s12906-017-1804-2","28583128","PMC5460465"),
 pm(12,"Comparative Studies of Essential Oil Composition and Biological Activities of Callistemon citrinus from Western Himalaya — Chem Biodivers 2023 (초록)","10.1002/cbdv.202301129","37728015"),
 pm(13,"Monthly changes in contents and compositions of oil of Callistemon citrinus: a comparison study — Nat Prod Res 2020 (초록)","10.1080/14786419.2020.1729149","32081037"),
 pm(14,"Essential oil composition of Callistemon citrinus (Curtis) and its protective efficacy against Tribolium castaneum — PLoS One 2022;17(8):e0270084 (초록)","10.1371/journal.pone.0270084","35984810","PMC9390898"),
 pm(15,"Chemical composition of Callistemon citrinus (Curtis) Skeels aerial part essential oil and its pharmacological applications, neurodegenerative inhibitory, and genotoxic efficiencies — J Food Biochem 2021 (초록)","10.1111/jfbc.13767","34028046"),
 pm(16,"Analytical and bioactivity-based evaluation of Callistemon citrinus: HPTLC fingerprinting, marker quantification, and antioxidant potential of hydroalcoholic extracts — J Chromatogr B 2026;125065 (초록)","10.1016/j.jchromb.2026.125065","41999711"),
 pm(17,"Alkylphloroglucinol derivatives and triterpenoids with soluble epoxide hydrolase inhibitory activity from Callistemon citrinus — Fitoterapia 2015 (초록)","10.1016/j.fitote.2015.10.013","26548595"),
 pm(18,"Evaluation of Anthocyanin Profile, Antioxidant, Cytoprotective, and Anti-Angiogenic Properties of Callistemon citrinus Flowers — Plants (Basel) 2020;9(8):1045 (초록)","10.3390/plants9081045","32824448","PMC7465370"),
 pm(19,"Role of the major terpenes of Callistemon citrinus against the oxidative stress during a hypercaloric diet in rats — Biomed Pharmacother 2022 (초록)","10.1016/j.biopha.2022.113505","36076512"),
 pm(20,"Long-term effect of salinity on plant quality, water relations, photosynthetic parameters and ion distribution in Callistemon citrinus — Plant Biol (Stuttg) 2013 (초록)","10.1111/plb.12106","24118672"),
 pm(21,"Callistemon citrinus and Cistus salvifolius, Two New Hosts of Phytophthora taxon niederhauserii in Italy — Plant Dis 2009 (초록)","10.1094/PDIS-93-10-1075A","30754367"),
 pm(22,"Transferability of simple sequence repeat (SSR) markers developed in guava (Psidium guajava L.) to four Myrtaceae species — Mol Biol Rep 2013 (초록)","10.1007/s11033-013-2608-1","23657599"),
 pm(23,"The complete chloroplast genome and characteristics analysis of Callistemon rigidus R.Br. — Mol Biol Rep 2020;47(7):5013-5024 (초록)","10.1007/s11033-020-05567-4","32515001"),
 pm(24,"Acute toxicity, brine shrimp cytotoxicity and relaxant activity of fruits of Callistemon citrinus Curtis — BMC Complement Altern Med 2011;11:99 (초록)","10.1186/1472-6882-11-99","22024247","PMC3216858"),
 pm(25,"Clinical effects and management of eucalyptus oil ingestion in infants and young children — Med J Aust 1995;163(4):177-80 (초록)","10.5694/j.1326-5377.1995.tb124516.x","7651249"),
 pm(26,"Eucalyptus oil poisoning in childhood: 41 cases in south-east Queensland — J Paediatr Child Health 1993;29(5):368-71 (초록)","10.1111/j.1440-1754.1993.tb00537.x","8240865"),
 pm(27,"Eucalyptus oil poisoning among young children: mechanisms of access and the potential for prevention — Aust N Z J Public Health 1997;21(3):297-302 (초록)","10.1111/j.1467-842x.1997.tb01703.x","9270157"),
 {"n":28,"title":"European Medicines Agency HMPC — Community herbal monograph on Eucalyptus globulus / E. polybractea / E. smithii aetheroleum (유칼립투스 정유; 30개월 미만 소아 금기·후두경련 사유) (EMA 사이트는 이 환경에서 열리지 않아 WebSearch 요약으로만 확인)","url":"https://www.ema.europa.eu/en/documents/herbal-monograph/final-community-herbal-monograph-eucalyptus-globulus-labill-eucalyptus-polybractea-rt-baker-or-eucalyptus-smithii-rt-baker-aetheroleum-superseded_en.pdf","publisher":"European Medicines Agency","accessed":A},
 {"n":29,"title":"JECFA 평가 데이터베이스 — Eucalyptol(1,8-cineole), JECFA No. 1234, 2003년 평가(향료로 현재 섭취 수준에서 안전성 우려 없음), WHO Food Additives Series 52 (원문을 열지 못해 WebSearch 요약으로만 확인)","url":"https://apps.who.int/food-additives-contaminants-jecfa-database/Home/Chemical/4089","publisher":"FAO/WHO Joint Expert Committee on Food Additives","accessed":A},
 {"n":30,"title":"병솔꽃나무(Callistemon citrinus (Curt.) Skeels)의 개화결실 및 증식특성 (2002, 국내 학술지 논문; koreascience 는 이 환경에서 열리지 않아 WebSearch 요약으로만 확인)","url":"https://koreascience.kr/article/JAKO200211921163971.page?lang=ko","publisher":"KoreaScience(한국과학기술정보연구원)","accessed":A},
 pm(31,"DES/Ultrasonic-Assisted Extraction and Process Optimization of Callistemon citrinus (Curtis) Skeels Essential Oil — Molecules 2026;31(5):819 (초록)","10.3390/molecules31050819","41828806","PMC12985494"),
 pm(32,"Low-Dose, Long-Term Callistemon citrinus and Its Main Compounds Alter Hepatic Fatty Acid Profiles and Protect Liver Histology in Rats Fed a High-Fat-Sucrose Diet — Int J Mol Sci 2026 (초록)","10.3390/ijms27167255","42653264","PMC13513202"),
 pm(33,"Inhibitory effects of the volatile oils of Callistemon citrinus (Curtis) Skeels and Eucalyptus citriodora Hook (Myrtaceae) on the acetylcholine induced contraction of rat isolated ileum — Pak J Pharm Sci 2012 (초록)",None,"22459474"),
 pm(34,"Insecticidal and repellent activities of the essential oil of Callistemon citrinus (Myrtaceae) against Callosobruchus maculatus — Neotrop Entomol 2012 (초록)","10.1007/s13744-012-0087-z","23949717"),
 pm(35,"Biological Activities of Callistemon citrinus and Callistemon viminalis Essential Oils: EMT-Linked Antitumor, Antioxidant, and Antibacterial Effects — Chem Biodivers 2026 (초록)","10.1002/cbdv.202502563","41518656","PMC13420218"),
]

sections = [
 {"key":"overview","title":"한눈에 보기","body":
"병솔나무는 도금양과(Myrtaceae)에 속하는 늘푸른 떨기나무 또는 작은 나무로, 원산지는 오스트레일리아다[6, 7, 21]. 식약처 「식품원료 목록」에는 학명 Callistemon citrinus (Curtis) Skeels(이명 Callistemon lanceolatus), 영어 이름 Bottlebrush Crimson, 원료명 '병솔나무잎'으로 올라 있다[1]. 이 목록에서 병솔나무는 사용가능 원료이며 사용 조건은 '사용가능부위 : 잎'이어서 잎만 식품에 쓸 수 있다[1]. 이 종을 원재료로 하는 건강기능식품 고시형 원료는 확인하지 못함.\n\n"
"논문에서는 같은 종을 Callistemon lanceolatus (Sm.) Sweet 또는 Melaleuca citrina (Curtis) Dum.Cours.라는 이름으로도 부르며, 이 자료는 세 이름으로 나온 연구를 함께 모았다[2, 3]. 잎에서 얻은 정유의 주성분은 1,8-시네올(유칼립톨)이고, α-피넨·리모넨·α-테르피네올이 함께 많다[10, 11, 19]. 잎 추출물에서는 갈산·엘라그산·p-쿠마르산 같은 페놀산과 퀘르세틴, 아실플로로글루시놀, 트리테르펜도 확인되었다[9, 16, 17]. 항산화·항비만·항균 작용은 세포와 쥐 실험에서 보고되었고, 사람을 대상으로 한 임상시험은 확인하지 못함."},
 {"key":"history","title":"역사와 이용","body":
"병솔나무는 오스트레일리아가 원산인 떨기나무로, 멕시코에서는 주로 관상수로만 심는다고 보고되었다[6]. 한 논문은 병솔나무를 이 속에서 가장 널리 재배되는 종으로 소개한다[7]. 같은 논문은 인도의 부족 공동체가 이 식물을 위장 질환·통증·감염병 치료에 써 왔다고 적었다[7]. 남아프리카 연구는 병솔나무가 기관지염·기침·염증 치료와 항균용 허브로 전통적으로 쓰인다고 소개한다[11]. 멕시코 연구진은 오스트레일리아 원주민이 이 식물을 전통 음식으로 썼다는 선행 보고를 인용했다[8].\n\n"
"분류학적으로는 큰 변화가 있었다[4, 5]. 1999년 핵 리보솜 DNA 분석은 오스트레일리아의 Callistemon 종들이 하나의 무리를 이루며 대부분의 오스트레일리아 Melaleuca 종과 같은 큰 갈래에 묶인다는 결과를 냈다[5]. 그 뒤 Craven이 2006년 Novon 논문에서 Callistemon을 Melaleuca에 합쳤고, 큐 왕립식물원은 이를 받아들였지만 뉴사우스웨일스 국립식물표본관 등은 받아들이지 않았다고 WebSearch 요약으로만 확인했다[4]. 그래서 최근 논문에는 Melaleuca citrina라는 이름도 나온다[3]. 국내에서는 2002년에 '병솔꽃나무'라는 이름으로 이 종의 개화·결실과 증식 특성을 다룬 연구가 나왔다고 WebSearch 요약으로만 확인했다[30]."},
 {"key":"biology","title":"식물학적 특징","body":
"병솔나무는 키 약 5–7 m까지 자라는 중간 크기 떨기나무에서 큰 나무까지의 모습을 보이며, 꽃차례가 병을 닦는 솔처럼 생겨 병솔(bottlebrush)이라는 이름이 붙었다[7]. 영어로는 crimson bottlebrush 또는 lemon bottlebrush라고 부른다[7, 18]. 꽃은 진한 붉은색·자주색을 띠며, 꽃에서는 시아니딘-3,5-O-다이글루코사이드 등 안토시아닌 4종이 확인되었다[18].\n\n"
"잎·꽃·줄기·열매 모두 정유를 품는다[11, 12]. 서히말라야 시료에서는 지상부의 정유 수율이 0.90%로 열매·잎보다 높았다[12]. 이란에서 한 해 동안 매달 거둔 시료는 말린 시료의 정유 함량이 생시료보다 크게 높았고, 3월에 거둔 말린 시료가 1.10%로 가장 높고 8월 생시료가 0.16%로 가장 낮았다[13]. 생잎 200 g을 수증기 증류한 실험에서는 수율이 0.5%였다[33].\n\n"
"이 종은 염분에 비교적 강하다[20]. 온실에서 56주 동안 4 dS/m의 염수로 키운 결과 지상부 생장은 줄었지만 개화와 잎 색은 변하지 않았다[20]. 2002년 국내 연구는 삭과(열매)가 가지에 최대 4년간 남아 있다고 보고했다고 WebSearch 요약으로만 확인했다[30]."},
 {"key":"related_species","title":"이름과 가까운 종","body":
"Callistemon속은 모두 오스트레일리아 고유종인 떨기나무 34종으로 이루어진다고 소개된다[7]. 핵 리보솜 DNA 5S·ITS-1 분석에서 오스트레일리아의 Callistemon은 단계통(한 조상에서 나온 무리)으로 나타났고, 대부분의 오스트레일리아 Melaleuca와 한 갈래를 이루었다[5]. 이 때문에 병솔나무를 Melaleuca citrina로 옮겨 부르는 분류도 있으며, 논문에서는 C. citrinus의 이명으로 C. lanceolatus와 M. citrina를 함께 적는다[2, 4].\n\n"
"식약처 목록의 이 행에는 C. citrinus와 C. lanceolatus가 같은 원료로 함께 적혀 있다[1]. 같은 속의 Callistemon viminalis 정유는 병솔나무 정유보다 총페놀 함량이 높았고(562.42 대 277.57 mg GAE/L), 폐암 세포 독성도 더 강했다(IC50 121 대 183 µg/mL)[35]. 중국에서 약용으로 쓰는 Callistemon rigidus는 엽록체 유전체가 해독된 가까운 종이다[23].\n\n"
"병솔나무 정유의 주성분인 1,8-시네올은 같은 도금양과의 유칼립투스 정유에도 많다[25, 33]. 그래서 병솔나무 정유 연구는 Eucalyptus citriodora 정유와 나란히 비교되기도 했다[33]. 병솔나무 잎이 아닌 유칼립투스 정유에서 나온 안전 정보는 safety 절에 따로 적었다[25, 28]."},
 {"key":"cultivation","title":"재배와 산지","body":
"병솔나무는 원산지인 오스트레일리아 밖에서도 관상수로 널리 심으며, 멕시코·남아프리카·인도·이란·이탈리아 등에서 자란 시료로 연구가 이루어졌다[6, 11, 12, 13, 21]. 꽃 안토시아닌 연구진은 이 식물이 세계 곳곳에 퍼진 관상수이며 재배가 쉽고 튼튼하며 여러 환경에 잘 적응한다고 적었다[18]. 온실 염분 시험 연구는 약 4 dS/m의 염수로도 상업적 재배가 가능하지만, 11개월 넘게 쓰면 광합성과 물 이용 효율이 떨어진다고 보고했다[20].\n\n"
"수확 시기와 나무 나이는 정유 성분에 영향을 준다[9, 13]. 이란 연구에서 1,8-시네올 비율은 1월에 거둔 말린 시료에서 60.01%, 8월 생시료에서 33.92%로 달랐고, 여름에는 α-피넨 비율이 올라갔다[13]. 멕시코 연구진은 주요 성분 함량과 항산화력을 높이려면 4년생 나무의 잎을 쓰라고 권했다[9].\n\n"
"병해로는 이탈리아 시칠리아 묘포장에서 12개월 된 화분 묘의 약 2%가 Phytophthora taxon niederhauserii에 의한 뿌리·줄기 밑동 썩음을 보였다는 보고가 있다[21]. 국내 재배 면적·생산량 통계와 지리적 표시 등록은 확인하지 못함."},
 {"key":"processing","title":"가공과 이용","body":
"식약처 「식품원료 목록」에서 식품에 쓸 수 있는 부위는 잎뿐이므로, 꽃·열매·줄기를 다룬 연구는 식품 원료와 부위가 다르다는 점에 주의해야 한다[1, 18, 24]. 연구용 정유는 보통 잎을 그늘에 말려 가루 낸 뒤 클레벤저 장치로 3시간 수증기 증류해 얻는다[7]. 초음파 보조 수증기 증류 조건을 최적화한 연구에서는 가열 57분, 가열 출력 563 W, 초음파 처리 23분일 때 건조 중량 기준 0.8 mL/kg의 정유를 얻었다[31].\n\n"
"동물 실험용 잎 추출물은 생잎을 95% 에탄올에 1:10으로 넣어 실온에서 5일간 우린 뒤 45 °C에서 감압 농축해 만들었다[8]. 같은 연구진의 추출 수율은 20%였다[9]. 흡수율을 높이려고 잎 추출물을 대두 포스파티딜콜린과 1:1로 묶은 피토좀(평균 입자 크기 129.98 nm, 봉입 효율 80.49%)도 만들어졌고, 20 °C에서 3개월 반 동안 입자 크기가 안정했다[9].\n\n"
"정유는 1,8-시네올(유칼립톨)의 값싼 공급원으로 향료·향수 산업에 쓸 수 있다는 제안이 있다[15]. 국내 건강기능식품·식품 생산실적에서 병솔나무 원료 품목은 확인하지 못함."},
 {"key":"genetics","title":"유전 정보","body":
"병솔나무 자체의 핵 유전체나 엽록체 유전체 해독 결과는 확인하지 못함. 같은 속의 Callistemon rigidus 엽록체 유전체는 길이 158,961 bp, GC 함량 36.78%이고, 26,671 bp 역반복 부위 한 쌍이 87,162 bp 대단일복사 부위와 18,457 bp 소단일복사 부위를 나눈다[23]. 이 유전체에는 단백질 유전자 86개, tRNA 37개, rRNA 8개 등 모두 131개 유전자가 있다[23].\n\n"
"구아바에서 만든 SSR(단순반복서열) 표지 23쌍을 C. lanceolatus에 적용하자 17쌍(73.9%)이 증폭되었고, 좌위당 평균 대립유전자 수는 4.5개였다[22]. 이 연구는 그때까지 C. lanceolatus에 대한 EST 유래나 유전체 SSR 정보가 없었다고 적었다[22]. 계통 연구에서는 핵 리보솜 DNA 5S·ITS-1 구간이 Callistemon과 Melaleuca의 관계를 밝히는 데 쓰였다[5].\n\n"
"정유 성분은 산지에 따라 크게 달라 화학형 차이를 보인다[10, 11, 12]. 남아프리카 잎 정유는 1,8-시네올이 48.98%로 가장 많았지만, 2015년 서히말라야 잎 정유는 α-피넨(32.3%)이 가장 많고 1,8-시네올은 꽃 정유(36.6%)에서 주성분이었다[10, 11]. 2023년 서히말라야 시료에서는 1,8-시네올이 58.3–85.1%였다[12]. 이런 차이가 유전형 때문인지 환경 때문인지는 확인하지 못함."},
 {"key":"safety","title":"안전성","body":
"식약처 「식품원료 목록」에서 병솔나무는 잎을 식품에 쓸 수 있는 사용가능 원료다[1]. 국내 공공기관의 병솔나무 알레르기·잔류물질·독성 성분 정보는 확인하지 못함.\n\n"
"쥐에 잎 에탄올 추출물을 100–4000 mg/kg 한 번 먹인 급성 독성 시험에서 죽거나 이상을 보인 동물이 없었고, 1000 mg/kg을 28일간 매일 먹인 아급성 시험에서도 간 효소(AST·ALT·LDH)와 간 조직에 변화가 없었다[8]. 지상부 정유는 양파 뿌리 시험에서 유전독성이 거의 없었다[15]. 열매 추출물 독성 연구도 있으나 열매는 식품 사용 부위가 아니다[1, 24].\n\n"
"정유의 주성분 1,8-시네올은 따로 주의가 필요하다[8, 25]. 위 쥐 논문은 1,8-시네올이 간·신장 조직에 심한 변화를 일으킬 수 있다는 보고를 인용했다[8]. 1,8-시네올이 많은 유칼립투스 정유를 어린이가 삼킨 109건 분석에서 5 mL 이상이면 의식 저하가, 2–3 mL에서도 가벼운 의식 저하가 생길 수 있었다[25]. 다른 41건 분석에서는 80%가 증상이 없었고, 빅토리아주 조사에서는 사고의 74%가 집 안 증기흡입기를 통해 일어났다[26, 27]. 유럽 의약품청은 1,8-시네올 함유 정유가 후두경련을 일으킬 수 있어 30개월 미만 소아에게 금기로 정했다고 WebSearch 요약으로만 확인했다[28]. JECFA는 2003년 유칼립톨을 향료로서 현재 섭취 수준에서 안전성 우려 없음으로 평가했다고 WebSearch 요약으로만 확인했다[29]. 병솔나무 잎이나 정유를 사람이 먹은 임상 안전성 자료는 확인하지 못함."},
]

compounds = [
 {"name":"Eucalyptol","name_ko":"1,8-시네올(유칼립톨)","class":"모노테르펜 산화물","role":"marker","part":"잎·꽃·지상부 정유","content_text":"잎 정유 48.98%(남아프리카); 꽃 정유 36.6%(서히말라야 2015); 열매·잎·지상부 정유 58.3–85.1%(서히말라야 2023); 지상부 정유 55.40%; 정유 40.44%; 월별 33.92–60.01%(이란)","activity_ko":"정유의 품질 지표 성분으로 제안됨; 쥐 고열량 식이 모델에서 0.88 mg/kg 투여로 체중 증가·산화 스트레스 지표 감소","source":[10,11,12,13,14,15,19]},
 {"name":"alpha-Pinene","name_ko":"α-피넨","class":"모노테르펜","role":"bioactive","part":"잎·줄기 정유","content_text":"잎 정유 32.3%(서히말라야 2015); 잎 정유 29.0%; 줄기 정유 31.03%; 정유 11.8–24.7%(서히말라야 2023)","activity_ko":"1,8-시네올과 함께 정유의 주요 성분; 여름 수확 시 비율 증가","source":[10,11,12,13,34]},
 {"name":"Limonene","name_ko":"리모넨","class":"모노테르펜","role":"bioactive","part":"잎","content_text":"잎 정유 13.1%(서히말라야 2015)","activity_ko":"쥐 고열량 식이 모델에서 0.43 mg/kg 투여로 체중 증가·혈당·중성지방 감소, 항염 작용","source":[10,19,32]},
 {"name":"alpha-Terpineol","name_ko":"α-테르피네올","class":"모노테르펜 알코올","role":"bioactive","part":"잎","content_text":"잎 정유 14.6%(서히말라야 2015); 잎 정유 8.01%(남아프리카)","activity_ko":"쥐 고열량 식이 모델에서 0.32 mg/kg 투여로 항염 작용; 잎 추출물 GC-MS에서 1,8-시네올과 함께 주성분","source":[9,10,11,19]},
 {"name":"Gallic acid","name_ko":"갈산","class":"페놀산","role":"marker","part":"잎·꽃","content_text":"잎 에탄올 추출물에서 HPLC-DAD로 확인(함량은 표에 있어 본문에서 확인하지 못함); HPTLC 정량에서는 주로 꽃 추출물에서 검출","activity_ko":"잎 추출물의 주요 화합물로 보고; 쥐 고지방·고당 식이 모델에서 23주 투여 시 간 지방산 조성 개선","source":[9,16,32]},
 {"name":"Ellagic acid","name_ko":"엘라그산","class":"페놀산","role":"bioactive","part":"잎","content_text":"잎 에탄올 추출물에서 이 식물 최초로 확인(HPLC-DAD)","activity_ko":"쥐 고지방·고당 식이 모델에서 간 지방산 조성 개선","source":[9,32]},
 {"name":"p-Coumaric acid","name_ko":"p-쿠마르산","class":"페놀산","role":"bioactive","part":"잎","content_text":"잎 에탄올 추출물에서 HPLC-DAD로 확인","activity_ko":"쥐 고지방·고당 식이 모델에서 간 보호 효과가 다른 성분보다 약함","source":[9,32]},
 {"name":"Quercetin","name_ko":"퀘르세틴","class":"플라보놀","role":"marker","part":"잎·꽃","content_text":"잎·꽃 하이드로알코올 추출물 모두에서 검출, 잎에서 농도가 더 높음(HPTLC)","activity_ko":"잎 추출물의 항산화력(DPPH·ABTS·FRAP)이 꽃보다 강한 것과 일치","source":[16]},
 {"name":"Pulverulentone A","name_ko":"풀베룰렌톤 A","class":"아실플로로글루시놀","role":"bioactive","part":"잎","content_text":"잎에서 분리(함량 확인하지 못함)","activity_ko":"MRSA에 중간 정도 항균 작용(IC50 22.2 µM), Cryptococcus neoformans 항진균 작용","source":[2]},
 {"name":"Corosolic acid","name_ko":"코로솔산","class":"트리테르펜","role":"bioactive","part":"잎","content_text":"잎에서 분리(함량 확인하지 못함)","activity_ko":"반코마이신 내성 장알균(VRE)에 강한 항균 작용(IC50 15.9 µM)","source":[2]},
 {"name":"Myrtucommulone B","name_ko":"미르투코물론 B","class":"아실플로로글루시놀","role":"bioactive","part":"잎·줄기","content_text":"잎·줄기에서 분리(칼리스테논 B와 혼합물로 시험, 함량 확인하지 못함)","activity_ko":"수용성 에폭사이드 가수분해효소(sEH) 강한 억제(혼합물 IC50 0.7 µM)","source":[17]},
 {"name":"Ursolic acid","name_ko":"우르솔산","class":"트리테르펜","role":"bioactive","part":"잎·줄기","content_text":"잎·줄기에서 분리(함량 확인하지 못함)","activity_ko":"sEH 억제(IC50 11.2 µM)","source":[17]},
 {"name":"Betulinic acid","name_ko":"베툴린산","class":"트리테르펜","role":"bioactive","part":"잎·줄기","content_text":"잎·줄기에서 분리(함량 확인하지 못함)","activity_ko":"함께 분리된 트리테르펜 중 하나로 sEH 억제 시험 대상","source":[17]},
 {"name":"Cyanin","name_ko":"시아닌(시아니딘-3,5-O-다이글루코사이드)","class":"안토시아닌","role":"bioactive","part":"꽃(식품 사용 부위 아님)","content_text":"꽃 산성 메탄올 추출 분획에서 처음 확인(RP-HPLC-DAD-ESI-MS/MS)","activity_ko":"안토시아닌 분획이 DPPH·ABTS 라디칼 소거, 사람 단핵구 산화 손상 보호, 혈관신생 억제","source":[18]},
]

assays = [
 {"role":"literature","compound":"1,8-Cineole (eucalyptol)","compound_ko":"1,8-시네올","part":"잎 정유(그늘에 말린 잎, 수증기 증류)","content":"",
  "method":"HPTLC(흡광 밀도측정, 아니스알데하이드-황산 유도체화)",
  "conditions":{"instrument":"CAMAG HPTLC(Linomat V 시료 도포기, 트윈 트로프 전개조, TLC Scanner, WinCATS 1.4.6)","column":"Merck 알루미늄 판 실리카겔 60F254, 0.2 mm(20 × 10 cm, 10 × 10 cm), 사전 세척 없음","mobile_phase":"톨루엔:에틸아세테이트:메탄올:포름산 = 9:0.5:0.5:0.5","gradient":"상승 전개 80 mm, 전개조 포화 10분, 25 ± 5 °C, 상대습도 50–60%","flow":"","temp":"25 ± 5 °C(전개)","detection":"아니스알데하이드-황산 유도체화 후 100 °C 가열, 540 nm 흡광 모드 스캔(슬릿 6.00 × 0.45 mm); Rf 0.52","injection":"8 mm 띠로 도포","sample_prep":"잎 가루 100 g을 클레벤저 장치로 3시간 수증기 증류, 무수 황산나트륨으로 건조; 정유 15 mg을 메탄올 10 mL에 녹임(1500 µg/mL)","standard":"1,8-시네올(순도 > 99%) 15 mg/메탄올 10 mL","linearity":"3–12 µg/spot, r = 0.999","lod":"","loq":"","recovery":"98%(80·100·120% 표준 첨가)"},
  "rationale":"이 종 잎 정유의 주성분이 1,8-시네올이라 품질 관리용 정량 대상으로 삼은 ICH 밸리데이션 방법이다. 전문(Methods)에서 조건을 옮겼고, 검출·정량한계 값은 표에 있어 본문에서 확인하지 못함[7].",
  "source":[7],"url":"https://doi.org/10.4103/0974-8490.129034","source_kind":"paper"},
 {"role":"literature","compound":"Gallic acid, p-coumaric acid, ellagic acid","compound_ko":"갈산·p-쿠마르산·엘라그산","part":"잎 에탄올 추출물(4년생 나무, 멕시코 모렐리아)","content":"",
  "method":"HPLC-DAD",
  "conditions":{"instrument":"Agilent 1260 Infinity(4원 펌프, 자동시료주입기, 칼럼 오븐, DAD)","column":"Express 90 Å C18, 250 × 4.6 mm, 5 µm","mobile_phase":"A: 메탄올, B: 1% 포름산","gradient":"0–5분 A 2%; 5–15분 2→15%; 15–30분 15→25%; 30–35분 25→35%; 35–45분 35→55%; 40–50분 55%(원문 표기 그대로); 50–55분 55→2%; 55–60분 2%; 후시간 5분","flow":"0.7 mL/min","temp":"40 °C","detection":"DAD 255·270·280·310·322·355·370 nm","injection":"5 µL","sample_prep":"생잎을 96% 에탄올에 1:10(w/v)으로 실온 5일 침지, 45 °C 회전증발 농축(수율 20%)","standard":"HPLC 등급 페놀 표준물질(갈산·4-하이드록시벤조산·클로로겐산·카페인산·시링산·p-쿠마르산·페룰산·엘라그산·t-신남산·퀘르세틴·루틴 등) 머무름 시간 비교","linearity":"","lod":"","loq":"","recovery":""},
  "rationale":"잎 추출물의 생리활성 성분으로 이 세 페놀산을 확인했고, 후속 동물 연구가 이를 잎 추출물의 주요 화합물로 삼아 따로 시험했다[9, 32]. 전문(Methods)에서 조건을 옮겼으나 성분별 함량은 표에 있어 본문에서 확인하지 못함[9].",
  "source":[9,32],"url":"https://doi.org/10.3390/pharmaceutics15092178","source_kind":"paper"},
 {"role":"literature","compound":"1,8-Cineole, alpha-terpineol (terpenes)","compound_ko":"1,8-시네올·α-테르피네올 등 테르펜","part":"잎 에탄올 추출물과 피토좀","content":"",
  "method":"GC-MS(EI)",
  "conditions":{"instrument":"Agilent 7890A GC + Hewlett Packard 5975C 사중극자 MS(EI 70 eV)","column":"HP-5MS(5% 페닐 폴리실페닐렌-실록산), 30 m × 0.25 mm × 0.25 µm","mobile_phase":"헬륨 운반기체","gradient":"오븐 60 °C 1분 → 8 °C/min으로 280 °C","flow":"1 mL/min(정유량)","temp":"주입구 230 °C, 이온원 230 °C, 사중극자 150 °C","detection":"EI 70 eV, m/z 50–500; Wiley 275·NIST 라이브러리 대조","injection":"","sample_prep":"생잎 96% 에탄올 1:10 침지 5일 후 농축","standard":"1,8-시네올 검량선(1–0.2 mg/mL)으로 테르펜 정량","linearity":"","lod":"","loq":"","recovery":""},
  "rationale":"잎 추출물과 피토좀의 주성분이 1,8-시네올과 α-테르피네올로 나타나 제형 전후 테르펜 보존을 확인하는 지표로 썼다. 전문(Methods)에서 조건을 옮겼고, 함량은 표에 있어 본문에서 확인하지 못함[9].",
  "source":[9],"url":"https://doi.org/10.3390/pharmaceutics15092178","source_kind":"paper"},
 {"role":"literature","compound":"Quercetin, gallic acid","compound_ko":"퀘르세틴·갈산","part":"잎·꽃 하이드로알코올 추출물","content":"잎 추출물 총페놀 18.19 ± 0.10 mg GAE/g, 총플라보노이드 16.35 ± 3.91 mg QE/g; 퀘르세틴은 잎에서 더 높고 갈산은 주로 꽃에서 검출[16]",
  "method":"HPTLC(ICH Q2(R1) 밸리데이션)",
  "conditions":{"instrument":"","column":"","mobile_phase":"","gradient":"","flow":"","temp":"","detection":"","injection":"","sample_prep":"","standard":"","linearity":"","lod":"","loq":"","recovery":""},
  "rationale":"잎·꽃 추출물의 표준화를 위해 퀘르세틴과 갈산을 지표 성분으로 정량했다. 초록만 확인해 분석 조건은 비웠다(전문 확인 못함)[16].",
  "source":[16],"url":"https://doi.org/10.1016/j.jchromb.2026.125065","source_kind":"paper"},
]

d = {"slug":"callistemon-citrinus","name_ko":"병솔나무","name_en":"Crimson bottlebrush (lemon bottlebrush)",
 "scientific_name":"Callistemon citrinus (Curtis) Skeels",
 "aliases":["병솔나무잎","병솔꽃나무","Bottlebrush Crimson","crimson bottlebrush","lemon bottlebrush","Callistemon lanceolatus (Sm.) Sweet","Melaleuca citrina (Curtis) Dum.Cours."],
 "sections":sections,"compounds":compounds,"markers":[],"nutrients":[],"assays":assays,
 "production":[],"world":[],"gi":[],"orgs":[],"sources":S}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in sections: print(s["key"], len(s["body"]))
