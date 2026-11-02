import json, pathlib
P = pathlib.Path(__file__).resolve().parent.parent
A = "2026-11-02"
def pm(n, title, pmid=None, pmc=None, pub="PubMed"):
    url = f"https://pmc.ncbi.nlm.nih.gov/articles/{pmc}/" if pmc else f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
    return {"n": n, "title": title, "url": url, "publisher": pub, "accessed": A}
sources = [
 {"n": 1, "title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 톱니모자반(Sargassum serratifolium) 1행 및 같은 속 원료 행(2026-10-13 받은 원자료)", "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
 pm(2, "Ali MY et al. α-Glucosidase and Protein Tyrosine Phosphatase 1B Inhibitory Activity of Plastoquinones from Marine Brown Alga Sargassum serratifolium. Mar Drugs 2017;15(12):368", pmc="PMC5742828", pub="Marine Drugs (PMC)"),
 pm(3, "Kim D et al. Hypothalamic administration of sargahydroquinoic acid elevates peripheral thermogenic signaling and ameliorates high fat diet-induced obesity through the sympathetic nervous system. Sci Rep 2021;11(1):21315", pmc="PMC8556287", pub="Scientific Reports (PMC)"),
 pm(4, "Lim S et al. Meroterpenoid-Rich Fraction of the Ethanolic Extract from Sargassum serratifolium Suppressed Oxidative Stress Induced by tert-Butyl Hydroperoxide in HepG2 Cells. Mar Drugs 2018;16(10):374", pmc="PMC6213136", pub="Marine Drugs (PMC)"),
 pm(5, "Lim S et al. Hepatoprotective Effect of Meroterpenoid-Rich Fraction from the Ethanolic Extract of Sargassum serratifolium on tert-Butyl Hydroperoxide-Induced Mice. J Microbiol Biotechnol 2025;35:e2501014", pmc="PMC12149404", pub="Journal of Microbiology and Biotechnology (PMC)"),
 pm(6, "Lim S et al. Evaluation of antioxidant activities of various solvent extract from Sargassum serratifolium and its major antioxidant components. Food Chem 2019;278:178-184 (초록)", pmid="30583359"),
 pm(7, "Baek SH et al. A comparative study of extraction methods for recovery of bioactive components from brown algae. Food Sci Biotechnol 2025;34(1):237-244 (초록; PMC 전문 본문은 도구로 받지 못함)", pmid="39758719"),
 pm(8, "Kim MJ et al. The beneficial effects of ethanolic extract of Sargassum serratifolium in DNCB-induced mouse model of atopic dermatitis. Sci Rep 2024;14(1):12874", pmc="PMC11150456", pub="Scientific Reports (PMC)"),
 pm(9, "Ryu H et al. Modulation of macrophage transcript and secretion profiles by Sargassum serratifolium extract is associated with the suppression of muscle atrophy. Sci Rep 2024;14(1):13282 (초록)", pmid="38858416"),
 pm(10, "Seo J et al. Inhibitory Effects of Extracellular Vesicles Derived from Sargassum serratifolium on Melanogenesis Partially by Suppressing Melanin Transport. Mar Drugs 2026;24(10):344", pmc="PMC13706142", pub="Marine Drugs (PMC)"),
 pm(11, "Siboro SAP et al. Nanoemulsion advancements for effective Sargassum serratifolium delivery in cosmetics: extraction, characterisation, and molecular docking. Nat Prod Res 2026;40(10):2802-2810 (초록)", pmid="42133840"),
 pm(12, "Joung EJ et al. Meroterpenoid-Rich Fraction of the Ethanol Extract of Sargassum serratifolium Suppresses Collagen-Induced Rheumatoid Arthritis in DBA/1J Mice Via Inhibition of Nuclear Factor κB Activation. Mol Nutr Food Res 2020;64(3):e1900373 (초록)", pmid="31900972"),
 pm(13, "Kwon M et al. Effects of Sargaquinoic Acid in Sargassum serratifolium on Inducing Brown Adipocyte-like Phenotype in Mouse Adipocytes In Vitro. Planta Med 2020;86(1):45-54 (초록)", pmid="31663108"),
 pm(14, "Azam MS et al. Sargaquinoic acid ameliorates hyperpigmentation through cAMP and ERK-mediated downregulation of MITF in α-MSH-stimulated B16F10 cells. Biomed Pharmacother 2018;104:582-589 (초록)", pmid="29803170"),
 pm(15, "Seong SH et al. BACE1 inhibitory activity and molecular docking analysis of meroterpenoids from Sargassum serratifolium. Bioorg Med Chem 2017;25(15):3964-3970 (초록)", pmid="28576634"),
 pm(16, "Oh SJ et al. Anti-Inflammatory Effect of Ethanolic Extract of Sargassum serratifolium in Lipopolysaccharide-Stimulated BV2 Microglial Cells. J Med Food 2016;19(11):1023-1031 (초록)", pmid="27845863"),
 pm(17, "Gwon WG et al. Sargaquinoic Acid Inhibits TNF-α-Induced NF-κB Signaling, Thereby Contributing to Decreased Monocyte Adhesion to Human Umbilical Vein Endothelial Cells (HUVECs). J Agric Food Chem 2015;63(41):9053-61 (초록)", pmid="26437568"),
 pm(18, "Kang CW et al. Hexane extract from Sargassum serratifolium inhibits the cell proliferation and metastatic ability of human glioblastoma U87MG cells. Oncol Rep 2015;34(5):2602-8 (초록)", pmid="26323587"),
 pm(19, "Yoon JH et al. Protective effect of sargahydroquinoic acid against Aβ-evoked damage via PI3K/Akt mediated Nrf2 antioxidant defense system. Biomed Pharmacother 2021;144:112271 (초록)", pmid="34619494"),
 pm(20, "Seong Choi K et al. Sargahydroquinoic acid isolated from Sargassum serratifolium as inhibitor of cellular basophils activation and passive cutaneous anaphylaxis in mice. Int Immunopharmacol 2022;105:108567 (초록)", pmid="35114442"),
 pm(21, "Kim HJ et al. Sargassum serratifolium attenuates RANKL-induced osteoclast differentiation and oxidative stress through inhibition of NF-κB and activation of the Nrf2/HO-1 signaling pathway. Biosci Trends 2018;12(3):257-265 (초록)", pmid="30012915"),
 pm(22, "Park C et al. Activation of the Nrf2/HO-1 Signaling Pathway Contributes to the Protective Effects of Sargassum serratifolium Extract against Oxidative Stress-Induced DNA Damage and Apoptosis in SW1353 Human Chondrocytes. Int J Environ Res Public Health 2018;15(6):1173 (초록)", pmid="29874784"),
 pm(23, "Park C et al. Sargassum serratifolium Extract Attenuates Interleukin-1β-Induced Oxidative Stress and Inflammatory Response in Chondrocytes ... Int J Mol Sci 2018;19(8):2308 — 철회된 논문(Retracted Publication)", pmid="30087236"),
 pm(24, "Int J Mol Sci 2026;27(13):5928 — 위 논문(Int J Mol Sci 2018;19(8):2308)의 철회 공지(Retraction Notice)", pmid="42450366"),
 pm(25, "Lee YJ et al. Complete organellar genomes of six Sargassum species and development of species-specific markers. Sci Rep 2022;12(1):20981", pmc="PMC9722929", pub="Scientific Reports (PMC)"),
 pm(26, "Kim J, Hong SK. Isolation and characterization of an agarase-producing bacterial strain, Alteromonas sp. GNUM-1, from the West Sea, Korea. J Microbiol Biotechnol 2012;22(12):1621-8 (초록)", pmid="23221523"),
 {"n": 27, "title": "국내 학술지 논문(KoreaScience JAKO202111065910087) — 톱니모자반 분포 서술. 웹 검색 결과 요약으로만 확인, 원문은 열지 못함(허용 목록 밖)", "url": "https://koreascience.kr/article/JAKO202111065910087.pdf", "publisher": "KoreaScience(웹 검색 요약)", "accessed": A},
 {"n": 28, "title": "국내 학술지 논문(KoreaScience JAKO201713056892852) — 톱니모자반 형태 서술. 웹 검색 결과 요약으로만 확인, 원문은 열지 못함(허용 목록 밖)", "url": "https://koreascience.kr/article/JAKO201713056892852.pdf", "publisher": "KoreaScience(웹 검색 요약)", "accessed": A},
]

S = {}
S["overview"] = ("톱니모자반(Sargassum serratifolium (C. Agardh) C. Agardh)은 모자반목(Fucales) 모자반과(Sargassaceae)에 속하는 갈조류로, 한국과 일본 연안에 널리 분포한다고 소개된다[2][3].\n\n"
 "식품원료로서의 지위: 식품의약품안전처 「식품원료 목록」에는 '톱니모자반' 1행이 식품원료(A코드)로 올라 있고, 상태는 '사용가능', 사용 조건은 '사용가능부위 : 전체'다[1]. 같은 목록에서 이 종을 건강기능식품 고시형 원료의 원재료로 연결한 기록은 없다[1].\n\n"
 "연구는 메로테르페노이드(플라스토퀴논류)에 모여 있으며, 사가하이드로퀴노익산(SHQA)·사가크로메놀(SCM)·사가퀴노익산(SQA)이 주성분으로 보고되었다[2][4][6]. 에탄올 추출물의 메로테르페노이드 농축 분획(MES)은 100 g당 이 세 성분을 합쳐 45.7 ± 2.2 g 담고 있었다[4]. 항산화·항염·혈당 효소 억제 등 효과 보고는 대부분 세포·효소·생쥐 실험이며, 사람 대상 임상시험은 확인하지 못함.")
S["history"] = ("한 논문은 톱니모자반이 아시아 연안에서 오래전부터 식품과 약재의 재료로 쓰여 왔다고 소개했고[21], 다른 논문은 아시아에서 식품이자 전통 약재로 먹어 왔다고 적었다[3]. 반면 2024년 논문은 아시아에서 먹을 수 있는 해조이지만 흔히 쓰이지는 않는 종이라고 적었다[8].\n\n"
 "근래의 연구 동기로는 모자반속 해조의 과잉 번식·해안 퇴적 문제가 자주 언급된다[8][10]. 이들 논문은 유엔환경계획(UNEP)이 모자반속을 과잉 축적 때문에 해양 오염원으로 지목했다고 쓰며, 이는 톱니모자반 한 종이 아니라 모자반속 전체에 대한 서술이다[8][10]. 그래서 버려지는 해조 자원을 기능성 소재로 쓰자는 취지의 연구가 이어졌다[8][10].\n\n"
 "국내 연구는 2015년 무렵부터 부산 지역 대학 연구진을 중심으로 메로테르페노이드의 항염·항산화 활성 보고가 이어졌다[16][17][18]. 이후 콜라겐 유도 관절염 생쥐에 MES를 먹인 실험[12], 대식세포 분비 인자를 통한 근위축 억제 실험[9], 사람 연골세포의 산화 스트레스 보호 실험[22] 등으로 범위가 넓어졌으며, 모두 세포·동물 실험이다[9][12][22]. 한국에서 이 종을 식품으로 먹어 온 지역 기록이나 전통 문헌 기록은 공공기관 자료로 확인하지 못함.")
S["biology"] = ("톱니모자반은 갈조강 모자반목 모자반과의 해조로, 한국과 일본 연안 전역에 분포한다고 기술된다[2]. 한 논문은 주로 한국과 일본 연안에 산다고 적었다[3]. 국내 학술지 논문은 국내에서는 제주 해역과 남해에, 국외에서는 중국·일본 등에 분포한다고 정리했다고 웹 검색 결과에 요약되어 있으나 원문은 열지 못했다[27].\n\n"
 "형태: 다른 모자반류처럼 공기주머니(기낭)가 있어 수면 가까이 떠오르고, 부착기는 납작한 원반 모양(반상형)이며 줄기 가장자리에 끝이 뭉툭한 가시가 난다고 웹 검색 결과에 요약되어 있으나 원문은 열지 못했다[28]. 이 종의 성숙 시기·수온 범위 같은 생태 자료는 확인하지 못함.\n\n"
 "연구 시료로는 2014년 4월[2]과 2017년 5월[4][5] 부산 연안에서 채집한 개체가 쓰였다. 서해에서 채집한 톱니모자반 시료에서는 한천 분해 효소를 내는 세균 Alteromonas sp. GNUM-1이 분리되었다[26]. 표본 하나는 국내 갈조류 자원 은행에 증거표본(TC18835)으로 기탁되었다[10].")
S["related_species"] = ("식약처 「식품원료 목록」에는 같은 속의 톳(S. fusiforme)·모자반(S. fulvellum)·괭생이모자반(S. horneri)·꽈배기모자반(S. siliquastrum)·비틀대모자반(S. sagamianum)·알쏭이모자반(S. confusum)·지충이(S. thunbergii)가 학명이 다른 별도 원료로 올라 있다[1]. 이 글은 이들 종의 자료를 톱니모자반 자료로 옮겨 쓰지 않았다[1].\n\n"
 "모자반속 종들은 겉모양 차이가 작고 환경·생장 단계에 따라 형태가 달라져 형태만으로 구분하기 어렵다[25]. 같은 논문은 가공 과정에서 여러 갈조류 원료가 섞일 수 있다고 지적하고, 톱니모자반을 포함한 국내 모자반속 6종을 구별하는 실시간 PCR 표지를 만들었다[25].\n\n"
 "주성분인 SHQA는 톱니모자반에만 있는 물질이 아니라 다른 모자반속 종에서도 발견되는 이소프레노이드 퀴논이다[3]. 학명 저자는 (C. Agardh) C. Agardh로 적은 논문[3]과 C. Agardh로 적은 논문[2][21]이 있다. 영어 일반명은 공공기관 자료에서 확인하지 못함.")
S["cultivation"] = ("톱니모자반의 국내 양식·채취 생산 통계(해양수산부·통계청)는 확인하지 못함. 연구에 쓰인 시료는 양식이 아니라 자연 군락에서 채집한 것이었다[2][4][26].\n\n"
 "2017년 논문 시료는 2014년 4월 부산 연안에서 채집해 말린 3.5 kg이었고, 해조 분류 전문가가 종을 확인했다[2]. 2018년·2025년 논문 시료는 2017년 5월 부산 연안에서 채집해 바람에 말리고 갈아서 썼다[4][5]. 2026년 논문의 시료도 같은 채집분에서 나왔고 증거표본이 기탁되었다[10].\n\n"
 "국내 모자반속 6종의 세포 소기관 유전체 연구에서는 해양수산부의 채집 허가를 받아 제주·전남·전북의 섬 연안에서 시료를 채집했으나, 원문 텍스트에서 학명이 빠져 톱니모자반이 어느 곳에서 채집되었는지는 확인하지 못함. 채취 시기에 따른 성분 변화 자료도 확인하지 못함.")
S["processing"] = ("에탄올 추출이 가장 많이 쓰였다[2][4][6]. 말린 시료 3.5 kg을 95% 에탄올(6 L씩)로 70°C에서 3시간씩 두 번 추출해 추출물 250.3 g을 얻었고, 이를 물에 풀어 헥산(86.5 g)·클로로폼(36 g)·에틸아세테이트(22.6 g)·부탄올(37.2 g) 분획으로 나눴다[2]. 세 메로테르페노이드는 헥산 분획에서 분리했고 순도는 HPLC-Q-TOF-MS로 99% 이상이었다[2].\n\n"
 "메로테르페노이드 농축 분획(MES)은 말린 시료 1.5 kg을 70% 에탄올(6 L씩)로 70°C 3시간씩 두 번 추출한 뒤 분자량 50 kDa 한외여과로 염과 수용성 당을 걸러 내고 수분 5.5% 미만까지 농축해 120 g을 얻었다[4][5]. 용매 비교에서는 에탄올 추출물의 SHQA·SCM·SQA 합계가 227 ± 6.31 mg/g으로 가장 높았다[6]. 추출법 비교에서는 100°C 가압 용매 추출의 총수율·페놀 함량이 가장 높았으나 SHQA·SCM 회수율은 메탄올 고-액 추출이 가장 높았다[7].\n\n"
 "세포밖 소포를 먼저 분리하고 남은 해조에서 에탄올 추출물을 얻는 이중 이용법도 보고되었다[10]. 화장품용 나노에멀전(약 20 nm)에 메로테르페노이드 분획을 담는 연구도 있다[11]. 톱니모자반 원료 건강기능식품 생산실적은 확인하지 못함.")
S["genetics"] = ("2022년 연구는 국내 모자반속 6종의 엽록체·미토콘드리아 유전체를 해독했으며, 톱니모자반의 엽록체와 미토콘드리아 유전체 전체 서열은 이 연구에서 처음 보고되었다[25]. 6종의 엽록체 유전체는 124,175–124,517 bp의 사분 구조 원형으로 GC 함량 30.3–30.6%였고, 모두 단백질 암호 유전자 139개를 가졌다[25].\n\n"
 "같은 6종의 미토콘드리아 유전체는 34,620–34,793 bp, GC 함량 36.2–36.6%였고 단백질 암호 유전자 37개와 rRNA 유전자 3개를 가졌다[25]. 엽록체 유전체 서열 유사도는 종 사이 93.36–99.95%, 미토콘드리아는 87.91–99.81%였다[25]. 이 값들은 6종 전체의 범위이며, 원문 텍스트에서 종 이름이 빠져 톱니모자반 한 종의 정확한 길이는 확인하지 못함.\n\n"
 "연구진은 단일염기 변이를 바탕으로 엽록체 표지 13개, 미토콘드리아 표지 14개를 만들어 6종을 실시간 PCR로 구별할 수 있게 했다[25]. 이는 값싼 다른 갈조류가 섞이는 것을 막는 원료 판별 도구로 제안되었다[25]. 톱니모자반의 핵 유전체 해독 자료는 확인하지 못함.")
S["safety"] = ("식약처 「식품원료 목록」에서 톱니모자반은 '사용가능' 원료이며 사용 조건은 '사용가능부위 : 전체'다[1]. 이 종에 대한 식약처 개별 기준(무기비소·요오드 등)은 확인하지 못함. 톱니모자반의 무기비소·총비소·요오드·중금속 함량을 측정한 공공기관 자료나 논문 수치도 확인하지 못함. 같은 속의 톳·모자반 등 다른 종의 비소·요오드 값은 이 종에 옮겨 쓰지 않았다[1].\n\n"
 "세포 실험의 독성 범위: MES는 HepG2 간세포에서 10.0 μg/mL까지 세포 독성이 없었다[4]. 에탄올 추출물은 RAW 264.7 대식세포에서 5 ppm, HaCaT 각질세포에서 2.5 ppm까지 생존율에 영향을 주지 않았다[8]. 헥산 추출물은 뇌종양 세포(U87MG)에 14–16 μg/mL에서 독성을 보였으나 사람 배아 신장 세포(HEK293)에서는 그런 효과가 없었다[18].\n\n"
 "동물 실험에서 MES 7·14 mg/kg을 생쥐에 5일 먹인 간 보호 실험이 있으나 독성 평가가 목적은 아니었다[5]. 사람 대상 섭취 안전성 시험과 약물 상호작용 자료는 확인하지 못함. 2018년 연골세포 논문[23]은 2026년 학술지가 철회했으므로 이 글의 근거로 쓰지 않았다[24]. 알레르기·잔류농약 등 공공기관 안전 정보는 확인하지 못함.")

titles = {"overview":"한눈에 보기","history":"이용 역사","biology":"생물학적 특징·생태","related_species":"관련 종·이름","cultivation":"서식·채취","processing":"가공·추출 연구","genetics":"유전 정보","safety":"안전성"}
sections = [{"key": k, "title": titles[k], "body": S[k]} for k in titles]

compounds = [
 {"name": "Sargahydroquinoic acid", "name_ko": "사가하이드로퀴노익산(SHQA)", "class": "메로테르페노이드(플라스토퀴논류)", "role": "marker", "part": "엽상체 전체(건조, 에탄올 추출물)",
  "content_text": "MES 100 g당 37.6 ± 2.1 g[4]", "activity_ko": "PTP1B 억제 IC50 5.14 ± 0.07 µM(효소)[2]; BACE1 4.3 µM·BChE 15.1 µM(효소)[15]; Aβ 손상 PC12 세포 보호(세포)[19]; 호염기구 활성화 억제·생쥐 피부 아나필락시스 완화(세포·동물)[20]; 시상하부 주입 생쥐에서 체중 증가 억제(동물)[3]", "source": [2, 3, 4, 15, 19, 20]},
 {"name": "Sargachromenol", "name_ko": "사가크로메놀(SCM)", "class": "메로테르페노이드(크로메놀)", "role": "bioactive", "part": "엽상체 전체(건조, 에탄올 추출물)",
  "content_text": "MES 100 g당 6.23 ± 0.36 g(원문 표기 'sargachromanol')[4]", "activity_ko": "α-글루코시다아제 억제 IC50 42.41 ± 3.09 µM, PTP1B 11.80 ± 3.35 µM(효소)[2]; BChE 9.4 µM·BACE1 6.9 µM(효소)[15]", "source": [2, 4, 15]},
 {"name": "Sargaquinoic acid", "name_ko": "사가퀴노익산(SQA)", "class": "메로테르페노이드(플라스토퀴논류)", "role": "bioactive", "part": "엽상체 전체(건조, 에탄올 추출물)",
  "content_text": "MES 100 g당 1.89 ± 0.10 g[4]", "activity_ko": "PTP1B IC50 14.15 µM, α-글루코시다아제 96.17 µM(효소)[2]; 멜라닌 생성 억제(B16F10 세포)[14]; TNF-α 자극 혈관내피세포의 단핵구 부착 억제(세포)[17]; 10 µM에서 지방세포 지질 축적 약 23% 감소(세포)[13]", "source": [2, 13, 14, 17]},
 {"name": "Sargaquinal", "name_ko": "사가퀴날", "class": "메로테르페노이드(플라스토퀴논류)", "role": "bioactive", "part": "엽상체",
  "content_text": "이전 성분 연구에서 분리된 플라스토퀴논으로 소개됨; 함량 확인하지 못함[2]", "activity_ko": "이 종 시료에서의 활성 수치는 확인하지 못함[2]", "source": [2]},
 {"name": "Sargachromanol C", "name_ko": "사가크로마놀 C", "class": "메로테르페노이드(크로마놀)", "role": "bioactive", "part": "엽상체 유래 세포밖 소포",
  "content_text": "비표적 UPLC-MS/MS로 동정(음이온 모드), 정량하지 않음[10]", "activity_ko": "개별 활성은 이 종 논문에서 확인하지 못함[10]", "source": [10]},
 {"name": "Sargachromanol D", "name_ko": "사가크로마놀 D", "class": "메로테르페노이드(크로마놀)", "role": "bioactive", "part": "엽상체 유래 세포밖 소포",
  "content_text": "비표적 UPLC-MS/MS로 동정, 정량하지 않음(같은 분석에서 사가크로마놀 H·J·L·N도 동정)[10]", "activity_ko": "개별 활성은 이 종 논문에서 확인하지 못함[10]", "source": [10]},
 {"name": "Sargachromanol J", "name_ko": "사가크로마놀 J", "class": "메로테르페노이드(크로마놀)", "role": "bioactive", "part": "엽상체 유래 세포밖 소포",
  "content_text": "비표적 UPLC-MS/MS로 동정, 정량하지 않음[10]", "activity_ko": "개별 활성은 이 종 논문에서 확인하지 못함[10]", "source": [10]},
 {"name": "Catechol", "name_ko": "카테콜", "class": "페놀", "role": "bioactive", "part": "엽상체 유래 세포밖 소포",
  "content_text": "비표적 UPLC-MS/MS(양이온 모드)로 동정, 정량하지 않음[10]", "activity_ko": "개별 활성은 이 종 논문에서 확인하지 못함[10]", "source": [10]},
]

assays = [
 {"role": "literature", "compound": "Sargahydroquinoic acid", "compound_ko": "사가하이드로퀴노익산(SHQA)", "part": "엽상체 전체(건조) — 70% 에탄올 추출 메로테르페노이드 농축 분획(MES)",
  "content": "MES 100 g당 37.6 ± 2.1 g(SHQA·SCM·SQA 합계 45.7 ± 2.2 g)",
  "method": "분리·정량(원문은 선행 논문의 방법을 인용; 기기 조건은 이 논문에 없음)",
  "conditions": {"instrument": "", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "", "injection": "",
   "sample_prep": "2017년 5월 부산 연안 채집 → 바람 건조·분쇄; 건조물 1.5 kg + 70% 에탄올 6 L, 70°C 3시간 2회 추출 → 50 kDa 한외여과 → 지용성 분획 분리 → 45°C 감압 농축(수분 5.5% 미만), MES 120 g",
   "standard": "분리한 SHQA", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "MES에서 가장 많은 메로테르페노이드이며 함량과 IC50으로 보아 주된 항산화 성분으로 평가되었다[4]. 전문 확인; 분석 기기 조건은 원문이 선행 논문을 인용해 확인하지 못함.",
  "source": [4], "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC6213136/", "source_kind": "paper"},
 {"role": "literature", "compound": "Sargachromenol", "compound_ko": "사가크로메놀(SCM)", "part": "엽상체 전체(건조) — MES",
  "content": "MES 100 g당 6.23 ± 0.36 g(원문 표기 sargachromanol)",
  "method": "분리·정량(원문은 선행 논문의 방법을 인용; 기기 조건은 이 논문에 없음)",
  "conditions": {"instrument": "", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "", "injection": "",
   "sample_prep": "SHQA 항목과 같은 MES", "standard": "분리한 SCM", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "SHQA·SQA와 함께 이 종의 3대 메로테르페노이드로 꼽힌다[4][6]. 전문 확인; 분석 기기 조건은 확인하지 못함.",
  "source": [4, 6], "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC6213136/", "source_kind": "paper"},
 {"role": "literature", "compound": "Sargahydroquinoic acid + sargachromenol + sargaquinoic acid", "compound_ko": "SHQA·SCM·SQA 합계", "part": "엽상체 전체(용매별 추출물)",
  "content": "에탄올 추출물에서 합계 227 ± 6.31 mg/g(비교한 용매 추출물 가운데 최고)",
  "method": "확인하지 못함(초록만 확인)",
  "conditions": {"instrument": "", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "", "injection": "", "sample_prep": "헥산·에틸아세테이트·에탄올·메탄올 등 용매별 추출", "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "세 성분이 이 종의 주된 항산화 성분으로 제시되었다[6]. 전문 확인 못함.",
  "source": [6], "url": "https://pubmed.ncbi.nlm.nih.gov/30583359/", "source_kind": "paper"},
]

d = {"slug": "sargassum-serratifolium", "name_ko": "톱니모자반", "name_en": "Sargassum serratifolium (brown seaweed)",
     "scientific_name": "Sargassum serratifolium", "aliases": ["Sargassum serratifolium (C. Agardh) C. Agardh"],
     "sections": sections, "compounds": compounds, "markers": [], "nutrients": [], "production": [], "world": [],
     "assays": assays, "gi": [], "orgs": [], "sources": sources}
for s in sections:
    print(s["key"], len(s["body"]))
(P / "dossier.json").write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
