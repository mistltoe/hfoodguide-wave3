import json
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "dossier.json"
ACC = "2026-11-02"


def pmc(n):
    return f"https://pmc.ncbi.nlm.nih.gov/articles/{n}/"


def pm(n):
    return f"https://pubmed.ncbi.nlm.nih.gov/{n}/"


S = [
    (1, "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 뚝갈잎(Patrinia villosa)·마타리·마타리순·패장근(Patrinia scabiosaefolia) 항목", "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "식품의약품안전처", "2026-10-13"),
    (2, "The Herba Patriniae (Caprifoliaceae): A review on traditional uses, phytochemistry, pharmacology and quality control. J Ethnopharmacol. 2020;262:113264 (doi:10.1016/j.jep.2020.113264)", pmc("PMC7443212"), "Elsevier (PubMed Central 전문, PubMed 도구로 열람)", ACC),
    (3, "[Research progress on chemical constituents, pharmacological activities, and quality control of Patrinia villosa]. Zhongguo Zhong Yao Za Zhi. 2022 (doi:10.19540/j.cnki.cjcmm.20220323.201) — 초록", pm("36471951"), "China Journal of Chinese Materia Medica (PubMed)", ACC),
    (4, "Can Patrinia villosa water extract be taken during FOLFOX treatment in colon cancer? Front Pharmacol. 2026 (doi:10.3389/fphar.2026.1756234)", pmc("PMC13080248"), "Frontiers (PubMed Central 전문, PubMed 도구로 열람)", ACC),
    (5, "Species classification and bioactive ingredients accumulation of BaiJiangCao based on characteristic inorganic elements analysis by ICP-MS and multivariate analysis. Pharmacogn Mag. 2015;11(44):S441 (doi:10.4103/0973-1296.165577)", pmc("PMC4621645"), "Wolters Kluwer Medknow (PubMed Central 전문, PubMed 도구로 열람)", ACC),
    (6, "Optimizing the Extraction and Enrichment of Luteolin from Patrinia villosa and Its Anti-Pseudorabies Virus Activity. Molecules. 2023;28(13):5005 (doi:10.3390/molecules28135005)", pmc("PMC10343258"), "MDPI (PubMed Central 전문, PubMed 도구로 열람)", ACC),
    (7, "Discovery of a heat-generated compound DHD derived from Patrinia villosa water extract with inhibitory effects on colon cancer cells viability and migration. Front Chem. 2023;11:1195883 (doi:10.3389/fchem.2023.1195883)", pmc("PMC10272523"), "Frontiers (PubMed Central 전문, PubMed 도구로 열람)", ACC),
    (8, "Anti-Melanogenic Effects of Ethanol Extracts of the Leaves and Roots of Patrinia villosa (Thunb.) Juss through Their Inhibition of CREB and Induction of ERK and Autophagy. Molecules. 2020;25(22):5375 (doi:10.3390/molecules25225375)", pmc("PMC7698407"), "MDPI (PubMed Central 전문, PubMed 도구로 열람)", ACC),
    (9, "Two Species Origins Comparison of Herba Patriniae Based on Their Ingredients Profile by UPLC-QTOF/MS/MS and OPLS-DA. Chem Biodivers. 2022 (doi:10.1002/cbdv.202100961) — 초록", pm("35979749"), "Wiley (PubMed)", ACC),
    (10, "Glycosides from the aerial parts of Patrinia villosa. Chem Pharm Bull (Tokyo). 2013 (doi:10.1248/cpb.c13-00306) — 초록", pm("23800854"), "The Pharmaceutical Society of Japan (PubMed)", ACC),
    (11, "Preparative isolation of four new and two known flavonoids from the leaf of Patrinia villosa Juss. by counter-current chromatography and evaluation of their anticancer activities in vitro. J Chromatogr A. 2006;1115:103-111 (doi:10.1016/j.chroma.2006.02.079) — 초록", pm("16545824"), "Elsevier (PubMed)", ACC),
    (12, "A New Biphenyl Neolignan from Leaves of Patrinia villosa (Thunb.) Juss. Pharmacogn Mag. 2016 (doi:10.4103/0973-1296.175988) — 초록", pm("27019553"), "Wolters Kluwer Medknow (PubMed)", ACC),
    (13, "A Cytotoxic Natural Product from Patrinia villosa Juss. Anticancer Agents Med Chem. 2019 (doi:10.2174/1871520619666190416101014) — 초록", pm("31038075"), "Bentham Science (PubMed)", ACC),
    (14, "[Studies on anti-inflammation chemical constitutes of Patrinia villosa]. Zhong Yao Cai. 2008;31(1):51-3 — 초록", pm("18589750"), "Journal of Chinese Medicinal Materials (PubMed)", ACC),
    (15, "Preparative separation of isovitexin and isoorientin from Patrinia villosa Juss by high-speed counter-current chromatography. J Chromatogr A. 2005;1074:111-115 (doi:10.1016/j.chroma.2005.03.067) — 초록", pm("15941046"), "Elsevier (PubMed)", ACC),
    (16, "Chemical composition and antioxidant activity of volatiles from Patrinia villosa Juss obtained by optimized supercritical fluid extraction. J Pharm Biomed Anal. 2008;48(3):796-801 (doi:10.1016/j.jpba.2008.08.004) — 초록", pm("18801633"), "Elsevier (PubMed)", ACC),
    (17, "The anti-inflammatory and anti-nociceptive activities of Patrinia villosa and its mechanism on the proinflammatory cytokines of rats with pelvic inflammation. Afr J Tradit Complement Altern Med. 2012;9(3):295-302 (doi:10.4314/ajtcam.v9i3.1) — 초록", pm("23983359"), "AJTCAM (PubMed)", ACC),
    (18, "Mechanistic insights into the anti-tumor and anti-metastatic effects of Patrinia villosa aqueous extract in colon cancer. Phytomedicine. 2023 (doi:10.1016/j.phymed.2023.154900) — 초록", pm("37269754"), "Elsevier (PubMed)", ACC),
    (19, "Patrinia villosa (Thunb.) Juss alleviates CCl4-induced acute liver injury by restoring bile acid levels and inhibiting apoptosis/autophagy. Front Pharmacol. 2024 (doi:10.3389/fphar.2024.1409971) — 초록", pm("38841374"), "Frontiers (PubMed)", ACC),
    (20, "[Studies on the constituents of Patrinia villosa Juss]. Yakugaku Zasshi. 1973;93(5):607-11 (doi:10.1248/yakushi1947.93.5_607) — 서지 정보만(초록 없음)", pm("4738257"), "The Pharmaceutical Society of Japan (PubMed)", ACC),
    (21, "Complete chloroplast genome sequence of Patrinia saniculifolia Hemsl. (Dipsacales: Caprifoliaceae), an endemic plant in Korea. Mitochondrial DNA B Resour. 2017;3(1):60-61 (doi:10.1080/23802359.2017.1419098) — 초록", pm("33474065"), "Taylor & Francis (PubMed)", ACC),
    (22, "Preliminary phylogeny of Valerianaceae (Dipsacales) inferred from nuclear and chloroplast DNA sequence data. Mol Phylogenet Evol. 2004;31(1):340-50 (doi:10.1016/j.ympev.2003.07.006) — 초록", pm("15019629"), "Elsevier (PubMed)", ACC),
    (23, "Study on the new anti-atherosclerosis activity of different Herba patriniae through down-regulating lysophosphatidylcholine of the glycerophospholipid metabolism pathway. Phytomedicine. 2021 (doi:10.1016/j.phymed.2021.153833) — 초록", pm("34798520"), "Elsevier (PubMed)", ACC),
    (24, "Analysis of plasma migration components in Patrinia villosa (Thunb.) Juss. effective parts by UPLC-Q-TOF-MS. Biomed Chromatogr. 2019 (doi:10.1002/bmc.4701) — 초록", pm("31596954"), "Wiley (PubMed)", ACC),
    (25, "Aqueous extract of the medicinal plant Patrinia villosa Juss. induces angiogenesis via activation of focal adhesion kinase. Microvasc Res. 2010;80(3):303-9 (doi:10.1016/j.mvr.2010.05.009) — 초록", pm("20594998"), "Elsevier (PubMed)", ACC),
    (26, "Inhibitory effects of methanol extracts of herbal medicines on substance P-induced itch-scratch response. Biol Pharm Bull. 2000;23(5):599-601 (doi:10.1248/bpb.23.599) — 초록", pm("10823672"), "The Pharmaceutical Society of Japan (PubMed)", ACC),
    (27, "Antitumor effects of saponin extract from Patrinia villosa (Thunb.) Juss on mice bearing U14 cervical cancer. Phytother Res. 2008;22(5):640-5 (doi:10.1002/ptr.2354) — 초록", pm("18350512"), "Wiley (PubMed)", ACC),
    (28, "New flavonoid from Patrinia villosa. Pharm Biol. 2015 (doi:10.3109/13880209.2015.1064449) — 초록", pm("26155822"), "Taylor & Francis (PubMed)", ACC),
    (29, "Efficient new method for extraction and isolation of three flavonoids from Patrinia villosa Juss. by supercritical fluid extraction and high-speed counter-current chromatography. J Chromatogr A. 2005;1102:44-50 (doi:10.1016/j.chroma.2005.10.045) — 초록", pm("16288764"), "Elsevier (PubMed)", ACC),
    (30, "Villosol reverses 5-FU resistance in colorectal cancer by inhibiting the CDKN2A gene regulated TP53-PI3K/Akt signaling axis. J Ethnopharmacol. 2024 (doi:10.1016/j.jep.2024.117907) — 초록", pm("38342156"), "Elsevier (PubMed)", ACC),
    (31, "[Studies on chemical constituents of Patrinia villosa]. Zhong Yao Cai. 2007;30(4):415-7 — 초록", pm("17674792"), "Journal of Chinese Medicinal Materials (PubMed)", ACC),
]

sections = [
    {"key": "overview", "title": "한눈에 보기", "body": (
        "뚝갈(Patrinia villosa (Thunb.) Juss.)은 마타리속의 여러해살이풀로, 식품의약품안전처 「식품원료 목록」에는 원료명 '뚝갈잎', 다른 이름 '뚜갈', 영어 이름 White-flower golden lace로 올라 있다[1]. "
        "같은 목록에서 이 원료의 지위는 '사용가능'이고 사용 조건은 '사용가능부위 : 잎'이어서, 식품원료로 쓸 수 있는 부위는 잎뿐이다[1]. "
        "같은 속의 마타리(Patrinia scabiosaefolia)는 '마타리순'(순, 사용가능)과 '패장근'(뿌리, 사용불가)으로 따로 올라 있으므로 뚝갈잎과 섞어 쓰면 안 된다[1]. "
        "건강기능식품 고시형 원료의 원재료로 쓰인다는 기록은 목록 자료에서 확인하지 못함.\n\n"
        "중국에서는 뚝갈과 마타리 두 종을 함께 한약재 '패장(敗醬, Herba Patriniae, 바이장차오)'으로 쓰며, 연한 줄기와 잎은 나물로도 먹는다[2][3]. "
        "두 종의 성분을 견준 연구들은 뚝갈에 플라보노이드가 많고 마타리에는 트리테르펜 사포닌과 휘발 성분이 많다고 보고했다[2][9]. "
        "뚝갈 잎에서는 루테올린 배당체(루테올로사이드)와 올레아놀산이 HPLC로 정량되었고, 물 추출물에서는 클로로겐산이 11.795 mg/g 추출물로 가장 많았다[4][5]. 잎에서는 프레닐기가 붙은 플라바논 등 플라보노이드 6종(새 화합물 4종), 바이페닐 네오리그난, 임페실론 A 같은 성분도 분리되었다[11][12][13]."
    )},
    {"key": "history", "title": "역사와 전통적 이용", "body": (
        "패장은 중국의 『신농본초경』에 중품 약재로 처음 실렸고, 한국의 『동의보감』에도 약효가 적혀 있어 한국에서 400년 넘게 쓰였다고 정리되어 있다[2]. "
        "1977년판 중국약전과 여러 성(省)의 약재 규격은 마타리와 뚝갈 두 종을 모두 패장의 기원 식물로 인정했다[2]. "
        "전통적으로 장옹(腸癰, 맹장염 같은 장의 고름집), 이질·장염, 간염, 산후 복통, 종기 등에 썼고, 율무·부자와 함께 쓰는 '의이부자패장산'은 『금궤요략』의 대표 처방이다[2]. "
        "중국약전(1977년판)과 지방 규격의 하루 임상 용량은 생약 9–15 g으로 인용되어 있다[4].\n\n"
        "뚝갈은 중국 민간에서 2000년 가까이 먹어 온 산나물이기도 하며, 아미노산·비타민·가용성 당을 함유한다고 소개된다[3]. "
        "국내 연구는 뚝갈이 『동의보감』(1613년)에서 염증을 다스리는 약으로 쓰였다고 소개했다[8]. "
        "1973년 일본 연구진이 일본산 뚝갈에서 이리도이드 3종을 처음 분리한 것이 이 종의 성분 연구의 시작으로 꼽힌다[3][20]. "
        "현대 동물실험에서는 골반염 모델 쥐의 IL-6·IL-8·TNF-α 감소, 대장암 모델의 종양 성장·전이 억제, 사염화탄소 간 손상 쥐의 ALT·AST 감소, 사포닌 추출물의 자궁경부암 종양 무게 35.1%·57.1% 감소가 보고되었다[17–19, 27]. 국내 식품 섭취 역사나 전통 조리법, 사람 임상 근거는 확인하지 못함."
    )},
    {"key": "biology", "title": "식물학적 특징", "body": (
        "뚝갈은 길가, 풀밭, 덤불, 숲 가장자리나 숲속의 해발 100–2000 m에서 자라는 키 50–120 cm의 여러해살이풀이다[2]. "
        "뿌리줄기는 옆으로 길게 뻗고, 줄기는 황록색이며 아래를 향한 흰 거친 털이 있다[2]. "
        "뿌리잎은 로제트로 모여 나며 잎자루가 길고 달걀꼴에서 긴 피침꼴이며, 잎몸은 4–25 cm × 2–18 cm이고 가장자리는 톱니가 있거나 1–2(–4)쌍으로 깃꼴로 갈라진다[2]. "
        "줄기잎은 마주나고 잎자루는 1–3 cm이며, 윗면은 짙은 녹색, 뒷면은 흰빛이 도는 녹색이다[2].\n\n"
        "꽃은 흰색이고 원뿔·우산 모양의 취산꽃차례로 피며, 곁가지는 보통 5–6쌍이고 털이 빽빽하다[2]. "
        "통꽃은 종 모양이고 깊게 5갈래로 갈라지며 수술 4개는 보통 꽃부리 밖으로 나온다[2]. "
        "꽃은 8–10월, 열매는 9–11월에 맺고 열매는 거꿀달걀꼴 수과이다[2]. "
        "흰 꽃은 노란 꽃이 피는 마타리 등 같은 속의 다른 종과 구분하는 특징으로 쓰인다[2][7]. "
        "식물분류에서는 마타리과(Valerianaceae)로 다뤄 왔고, 최근 문헌에서는 인동과(Caprifoliaceae)로 넓게 묶기도 한다[2][28]."
    )},
    {"key": "related_species", "title": "가까운 종과 구분", "body": (
        "가장 가까운 비교 대상은 마타리(Patrinia scabiosaefolia)로, 노란 꽃이 7–9월에 피고 키가 30–100(–200) cm이며 줄기잎이 깃꼴로 깊게 갈라진다[2]. "
        "마타리는 식품원료 목록에서 순만 쓸 수 있고 뿌리(패장근)는 '사용불가'이므로, 뚝갈잎(잎, 사용가능)과 부위·지위가 다르다[1]. "
        "중국 시장에서는 두 종이 같은 이름 '패장'으로 섞여 유통되어 임상 사용이 혼란스럽다는 지적이 있다[5][3].\n\n"
        "두 종을 가르는 방법으로 UPLC-QTOF-MS 성분 프로파일이 쓰였는데, 164개 성분 중 뚝갈에서 127개, 마타리에서 107개가 확인되었고 플라보노이드 비율은 45.45% 대 28.46%, 사포닌은 12.61% 대 32.09%였다[9]. "
        "잎의 Na·Mg·K·Fe 네 원소 함량으로도 두 종과 가짜 약재가 주성분분석·군집분석에서 갈렸다[5]. "
        "동맥경화 모델 쥐에서는 뚝갈 에틸아세테이트 추출물이 마타리 추출물보다 효과가 좋았다고 보고되어, 두 종을 같은 원료로 다루기 어렵다[23]. "
        "가려움 억제(뿌리 추출물)[26]와 혈관 신생 촉진(물 추출물)[25]은 뚝갈에서만 보고되고 마타리에서는 보고가 없다[2]. 한국 고유종인 금마타리(Patrinia saniculifolia)도 같은 속이며 엽록체 유전체가 따로 해독되었다[21]."
    )},
    {"key": "cultivation", "title": "재배와 산지", "body": (
        "뚝갈은 동아시아에 널리 자라는 풀로, 마타리속 식물은 동아시아와 북아메리카에 분포하고 중국에는 10종 이상이 자란다[2][5]. "
        "패장의 연한 줄기와 잎은 산에서 오염 없이 자라는 질 좋은 채소로 소개되며, 중국 후베이·푸젠성에서는 패장 차도 만든다[2]. "
        "새로 일군 차밭에 패장을 섞어 심어 빗물에 의한 토양 유실을 줄이는 데 쓴 사례도 소개되었다[2].\n\n"
        "논문에 쓰인 시료의 산지는 중국 간쑤성 룽난시 리현에서 10월에 채취한 전초, 홍콩 약재상에서 산 건조 약재, 중국 여러 성에서 모은 잎 등이다[4][5][6]. "
        "국내 연구에서는 국립생물자원관이 제공한 뚝갈 잎·뿌리의 95% 에탄올 추출물이 쓰였고, 한국산 지상부에서는 새 플라보노이드 배당체 2종·이리도이드 배당체 1종·사포닌 2종이 분리되었다[8][10]. "
        "자란 환경·생육 시기·수확 시기에 따라 성분 함량과 약리 활성이 달라진다는 정리가 있어, 원료의 산지와 채취 시기를 기록할 필요가 있다[2]. "
        "통계청 농작물생산조사와 농림축산식품부 「특용작물 생산실적」에서 뚝갈 품목의 국내 재배 면적·생산량은 확인하지 못함. "
        "국내 재배 기술(파종·수확 시기)을 정리한 공공기관 자료도 확인하지 못함."
    )},
    {"key": "processing", "title": "가공과 이용", "body": (
        "식품원료로는 잎만 쓸 수 있으며, 중국에서는 연한 줄기와 잎을 나물로 먹고 차 제품으로도 가공한다[1][2]. "
        "약재로는 전초를 물에 달여 먹는 것이 전통 방법이며, 건조 약재 500 g을 물 5 L로 두 번 끓여 얻은 물 추출물의 수율은 20.8%(w/w)였다[4]. "
        "같은 연구진의 다른 실험에서는 건조 약재 400 g을 물로 두 번 끓여 15.3%(w/w)의 물 추출물을, 75% 에탄올로 두 번 환류해 9.2%(w/w)의 에탄올 추출물을 얻었다[7].\n\n"
        "가공 방법에 따라 성분이 바뀐다는 점이 중요하다[7]. "
        "생약에 있는 이리도이드 배당체 발레로시데이트는 80 °C부터 분해되기 시작해 100 °C에서 약 1시간이면 거의 다 분해되고, 그 대신 열분해 산물 DHD(8,9-didehydro-7-hydroxydolichodial)가 생긴다[7]. "
        "그래서 상온에서 우린 물 추출물에는 발레로시데이트만, 끓인 물 추출물에는 DHD만 검출되었다[7]. 초임계 이산화탄소로 뽑은 휘발 성분에서는 46종이 확인되었고 탄화수소 49.65%, 지방산 22.38%, 알데하이드 16.66%, 테르펜 9.04%였다[16]. "
        "패장의 총플라보노이드는 잎 47.9–57.4 mg/g, 줄기 18.1–29.2 mg/g으로 부위 차이가 컸다는 보고가 정리되어 있으나, 어느 종의 값인지는 전문 텍스트에서 확인하지 못함[2]. "
        "식약처 「식품 등의 생산실적」에서 뚝갈 원료 건강기능식품의 생산실적은 확인하지 못함."
    )},
    {"key": "genetics", "title": "유전 정보와 종 확인", "body": (
        "뚝갈 자체의 엽록체·핵 유전체를 해독한 논문은 PubMed에서 확인하지 못함. "
        "같은 속에서는 한국 고유종 금마타리의 엽록체 유전체가 153,775 bp(LSC 87,529 bp, SSC 17,236 bp, IR 23,806 bp 2개, GC 38.48%)로 보고되었다[21]. "
        "핵 ITS와 엽록체 DNA 계통 분석에서 히말라야의 마타리속(Patrinia)과 나르도스타키스속은 마타리과 계통의 밑동에 놓여, 이 과가 아시아에서 처음 분화했음을 시사했다[22].\n\n"
        "패장은 두 종이 섞여 유통되므로 논문마다 시료 종을 어떻게 확인했는지가 중요하다[3][5]. "
        "홍콩 연구진은 형태·화학·분자 감별을 함께 써서 뚝갈을 확인하고 표본(No. 3705)을 보관했다[4]. "
        "중국 하얼빈의 연구는 뚝갈(PVJ2013-1~9)과 마타리(PSF2013-1~4) 표본을 따로 보관하고 잎의 원소 조성으로 두 종을 구분했다[5]. "
        "국내 연구 시료는 국립생물자원관에서 받은 뚝갈 잎과 뿌리 추출물이었다[8]. "
        "품종 육성이나 등록 품종 정보는 확인하지 못함."
    )},
    {"key": "safety", "title": "안전성", "body": (
        "식품원료 목록에서 뚝갈은 잎만 '사용가능'이므로, 뿌리나 전초를 식품에 쓰는 것은 이 목록의 조건 밖이다[1]. "
        "건강기능식품 고시형 원료가 아니어서 식약처 고시의 섭취 시 주의사항은 없다[1]. "
        "뚝갈에 대한 알레르기·농약 잔류·독성 성분 정보는 식약처 등 공공기관 자료에서 확인하지 못함.\n\n"
        "문헌 정리에 따르면 패장은 통상 용량에서는 거의 독성이 없지만, 많이 먹으면 일시적 백혈구 감소, 어지럼, 메스꺼움 같은 가벼운 부작용이 보고되었고 일부 환자는 입마름·위 불편을 겪었다[2]. "
        "같은 정리는 사람에게서 부작용이 나타난 용량을 하루 4–12 g으로 적었는데, 두 기원 종을 함께 다룬 것이어서 뚝갈만의 값인지는 확인하지 못함[2]. "
        "대장암 이식 쥐에게 뚝갈 물 추출물 1.6 g/kg을 3주간 먹였을 때 몸무게 변화는 없었고, 항암제 FOLFOX의 대사 효소 수치에도 영향이 없었다[4]. "
        "B16F10 세포에서 잎 에탄올 추출물은 400–800 μg/mL에서 독성이 없었지만 뿌리 추출물은 약 400 μg/mL에서 약 75%의 세포독성을 보였다[8]. "
        "열분해 산물 DHD는 정상 섬유아세포에도 독성을 보였다(IC50 9.4 μM)[7]. "
        "항암 치료 중이거나 약을 먹는 사람은 패장 제품을 쓰기 전에 의료진과 상의하는 것이 안전하며, 사람 대상 임상 안전성 자료는 확인하지 못함."
    )},
]

compounds = [
    {"name": "Luteoloside", "name_ko": "루테올로사이드(루테올린-7-O-글루코사이드)", "class": "플라보노이드 배당체", "role": "marker", "part": "잎",
     "content_text": "잎 80% 메탄올 추출, HPLC-UV 350 nm로 산지별 정량(산지별 값 표는 전문 텍스트에서 확인하지 못함)[5]",
     "activity_ko": "잎의 Na·Mg·K 함량과 높은 양의 상관을 보인 주요 생리활성 성분으로 정량됨[5]", "source": [5]},
    {"name": "Oleanolic acid", "name_ko": "올레아놀산", "class": "트리테르펜", "role": "marker", "part": "잎",
     "content_text": "잎 에탄올 추출, HPLC-UV 210 nm로 산지별 정량(값은 확인하지 못함)[5]",
     "activity_ko": "패장의 대표 트리테르펜 비당체로 항종양·항균·항바이러스 활성이 보고됨(정리 논문)[2]", "source": [2, 5]},
    {"name": "Chlorogenic acid", "name_ko": "클로로겐산", "class": "페놀산", "role": "marker", "part": "건조 약재(줄기·잎) 물 추출물",
     "content_text": "11.795 ± 0.043 mg/g 추출물(HPLC-DAD, n = 3)[4]",
     "activity_ko": "물 추출물의 항산화(라디칼 소거) 활성 성분으로 꼽힘[2]", "source": [2, 4]},
    {"name": "Protocatechuic acid", "name_ko": "프로토카테쿠산", "class": "페놀산", "role": "bioactive", "part": "건조 약재 물 추출물",
     "content_text": "2.580 ± 0.009 mg/g 추출물[4]", "activity_ko": "항산화·항염 등 건강 관련 활성이 정리됨[2]", "source": [2, 4]},
    {"name": "Isochlorogenic acid A", "name_ko": "이소클로로겐산 A(3,5-다이카페오일퀸산)", "class": "페놀산", "role": "bioactive", "part": "건조 약재 물 추출물",
     "content_text": "1.998 ± 0.007 mg/g 추출물[4]", "activity_ko": "물 추출물 표준화 지표 5종 가운데 하나[4]", "source": [4]},
    {"name": "Caffeic acid", "name_ko": "카페산", "class": "페놀산", "role": "bioactive", "part": "건조 약재 물 추출물·전초",
     "content_text": "1.009 ± 0.002 mg/g 추출물[4]; 전초에서 trans-카페산 분리[28]", "activity_ko": "총플라보노이드 투여 쥐 혈장에서 원형 성분으로 검출됨[24]", "source": [4, 24, 28]},
    {"name": "Orotinin", "name_ko": "오로티닌(외 오로티닌-5-메틸에터·리코아그로칼콘 B)", "class": "프레닐 플라보노이드", "role": "bioactive", "part": "전초",
     "content_text": "초임계 추출(25 MPa, 45 °C, 메탄올 20%) 시 세 성분 합계 0.82 mg/g 건조 시료[29]",
     "activity_ko": "같은 계열 프레닐 플라바논들이 K562 등 암세포 증식 억제(IC50 < 7 μg/mL)[11]", "source": [11, 29]},
    {"name": "Luteolin", "name_ko": "루테올린", "class": "플라보노이드(플라본)", "role": "bioactive", "part": "전초",
     "content_text": "최적 조건 환류 추출 시 0.265 ± 0.03 mg/g(HPLC 350 nm)[6]",
     "activity_ko": "루테올린 농축물이 돼지 오제스키병 바이러스(PRV)를 세포에서 억제(IC50 0.04 ± 0.012 mg/mL)[6]", "source": [6]},
    {"name": "Isovitexin", "name_ko": "이소비텍신", "class": "플라보노이드(C-배당체)", "role": "bioactive", "part": "전초",
     "content_text": "조추출물 250 mg에서 42.9 mg 분리(순도 99.3%)[15]", "activity_ko": "패장 특유의 C-배당 플라본으로 정리됨[2]", "source": [2, 15]},
    {"name": "Isoorientin", "name_ko": "이소오리엔틴", "class": "플라보노이드(C-배당체)", "role": "bioactive", "part": "전초",
     "content_text": "조추출물 250 mg에서 20.1 mg 분리(순도 98.5%)[15]", "activity_ko": "총플라보노이드 투여 쥐 혈장에서 원형 성분으로 검출됨[24]", "source": [15, 24]},
    {"name": "Valerosidate", "name_ko": "발레로시데이트", "class": "이리도이드 배당체", "role": "bioactive", "part": "건조 약재(뿌리·줄기·잎)",
     "content_text": "75% 에탄올 추출물에서 약 60 mg 분리(함량 값은 확인하지 못함); 80 °C부터 분해[7]",
     "activity_ko": "HCT116 대장암 세포 생존 억제 IC50 22.2 ± 1.1 μM, 정상 섬유아세포 IC50 71.3 ± 1.1 μM[7]", "source": [7]},
    {"name": "8,9-Didehydro-7-hydroxydolichodial", "name_ko": "DHD(발레로시데이트 열분해 산물)", "class": "이리도이드 분해물", "role": "bioactive", "part": "끓인 물 추출물",
     "content_text": "생약·에탄올 추출물에는 없고 끓인 물 추출물에서만 검출[7]",
     "activity_ko": "HCT116 세포 IC50 6.1 ± 2.2 μM, 정상 섬유아세포 IC50 9.4 ± 4.4 μM(선택성 낮음)[7]", "source": [7]},
    {"name": "Villosol", "name_ko": "빌로솔", "class": "이 종에서 처음 보고된 성분", "role": "bioactive", "part": "전초",
     "content_text": "에틸아세테이트·부탄올 분획에서 분리(함량은 확인하지 못함)[14]",
     "activity_ko": "5-FU 내성 대장암 세포에서 CDKN2A를 억제해 감수성을 되살림(세포·동물)[30]", "source": [14, 30]},
    {"name": "Ursolic acid", "name_ko": "우르솔산", "class": "트리테르펜", "role": "bioactive", "part": "전초",
     "content_text": "석유에테르·에틸아세테이트 추출물에서 분리(함량은 확인하지 못함)[31]",
     "activity_ko": "MTT 시험 항암 활성 IC50 15.0 μg/mL[31]", "source": [31]},
    {"name": "Kaempferol", "name_ko": "캠페롤", "class": "플라보노이드(플라보놀)", "role": "bioactive", "part": "뿌리",
     "content_text": "뿌리 95% 에탄올 추출물에서 약 0.009%(HPLC)[8]",
     "activity_ko": "뿌리 추출물의 멜라닌 생성 억제에 기여할 성분으로 제시됨[8]", "source": [8]},
]

assays = [
    {"role": "literature", "compound": "Luteoloside", "compound_ko": "루테올로사이드", "part": "잎(건조 분말)",
     "content": "산지별 μg/g 값(Table 4)은 전문 텍스트에서 확인하지 못함[5]", "method": "HPLC-UV",
     "conditions": {"instrument": "Agilent 1100 series HPLC(G1314A VWD)", "column": "Agilent 역상 TC-C 칼럼(아래첨자 표기가 전문 텍스트에서 빠짐, C18로 추정), 4.6 × 250 mm, 5 µm, 같은 회사 보호 칼럼",
                    "mobile_phase": "A: 물-인산(100:0.5), B: 아세토니트릴", "gradient": "등용매 B 17%", "flow": "1 mL/min", "temp": "30 °C",
                    "detection": "UV 350 nm", "injection": "20 µL",
                    "sample_prep": "잎 분말 약 2 g + 80% 메탄올 50 mL, 1시간 환류 2회 → 여과·건고 → 메탄올 10 mL 정용 → 0.45 µm 막 여과",
                    "standard": "루테올로사이드 표준품, 메탄올 원액 40.0 μg/mL", "linearity": "2–40 μg/mL(0.04–0.8 μg), r = 0.9999, n = 6; 일내 변동계수 0.16%",
                    "lod": "", "loq": "", "recovery": "평균 102.47%(RSD 1.71%, 표준첨가법)"},
     "rationale": "뚝갈과 마타리 잎의 주요 생리활성 성분 2종 가운데 하나로 골라 원소 조성과의 상관을 보려고 정량했다[5]. 시료는 표본 번호로 뚝갈(PVJ2013)과 마타리를 구분했다. 검출·정량한계는 본문에 없어 비워 둠.",
     "source": [5], "url": pmc("PMC4621645"), "source_kind": "paper"},
    {"role": "literature", "compound": "Oleanolic acid", "compound_ko": "올레아놀산", "part": "잎(건조 분말)",
     "content": "산지별 μg/g 값(Table 4)은 전문 텍스트에서 확인하지 못함[5]", "method": "HPLC-UV",
     "conditions": {"instrument": "Agilent 1100 series HPLC(G1314A VWD)", "column": "Agilent 역상 TC-C 칼럼(C18로 추정), 4.6 × 250 mm, 5 µm",
                    "mobile_phase": "A: 물-인산(100:0.5), B: 아세토니트릴", "gradient": "등용매 B 73%", "flow": "1 mL/min", "temp": "30 °C",
                    "detection": "UV 210 nm", "injection": "20 µL",
                    "sample_prep": "잎 분말 약 2 g + 에탄올 25 mL, 2시간 환류 2회 → 여과·건고 → 메탄올 10 mL 정용 → 0.45 µm 막 여과",
                    "standard": "올레아놀산 표준품, 메탄올 원액 50.0 μg/mL", "linearity": "0.6–12.0 μg(본문 표기 0.3–6.0 mg/mL), r = 0.9998, n = 6; 일내 변동계수 0.18%",
                    "lod": "", "loq": "", "recovery": "평균 101.05%(RSD 1.62%)"},
     "rationale": "패장 잎의 대표 트리테르펜으로 루테올로사이드와 함께 정량했다[5]. 본문의 검량 범위 단위(mg/mL)는 주입량(μg)과 맞지 않아 둘 다 적음.",
     "source": [5], "url": pmc("PMC4621645"), "source_kind": "paper"},
    {"role": "literature", "compound": "Chlorogenic acid", "compound_ko": "클로로겐산(외 갈산·프로토카테쿠산·카페산·이소클로로겐산 A)", "part": "건조 약재(줄기·잎) 열수 추출물",
     "content": "클로로겐산 11.795 ± 0.043, 프로토카테쿠산 2.580 ± 0.009, 이소클로로겐산 A 1.998 ± 0.007, 카페산 1.009 ± 0.002, 갈산 0.680 ± 0.001 mg/g 추출물(n = 3)[4]",
     "method": "HPLC-DAD",
     "conditions": {"instrument": "Agilent 1100 series HPLC, DAD 검출기", "column": "Grace Alltech Alltima C18, 250 × 4.6 mm, 5 µm",
                    "mobile_phase": "A: 0.1% 포름산 수용액(Milli-Q), B: 0.1% 포름산 아세토니트릴",
                    "gradient": "0–4분 B 2%; 4–25분 2→15%; 25–35분 15→30%; 35–40분 30%; 40–48분 30→98%; 48–55분 98%",
                    "flow": "0.8 mL/min", "temp": "", "detection": "190–400 nm 스펙트럼 기록, 크로마토그램 254 nm",
                    "injection": "원문 표기 '3 mL'(μL 오기로 보이나 확인하지 못함)",
                    "sample_prep": "물 추출물 분말 50 mg + 70% 메탄올 1 mL, 실온 초음파 30분 → 14,000 rpm 15분 원심 → 상등액 주입",
                    "standard": "갈산·클로로겐산·카페산(시판 표준품), 프로토카테쿠산·이소클로로겐산 A(시판 표준품)", "linearity": "", "lod": "", "loq": "", "recovery": ""},
     "rationale": "전통 복용 형태인 열수 추출물을 표준화하려고 대표 페놀산 5종을 화학 지표로 정량했다[4]. 시료는 형태·화학·분자 감별로 뚝갈임을 확인했다. 부위는 잎만이 아니라 줄기·잎이 섞인 건조 약재이며, 검량선·검출한계·회수율은 본문에 없어 비워 둠.",
     "source": [4], "url": pmc("PMC13080248"), "source_kind": "paper"},
]

d = {
    "slug": "patrinia-villosa",
    "name_ko": "뚝갈",
    "name_en": "White-flower golden lace",
    "scientific_name": "Patrinia villosa (Thunb.) Juss.",
    "aliases": ["뚝갈잎", "뚜갈", "Fedia villosa (Thunb.) Vahl", "패장(敗醬, 마타리와 공용 약재명)", "Herba Patriniae", "Baijiangcao", "white patrinia"],
    "sections": sections,
    "compounds": compounds,
    "markers": [],
    "assays": assays,
    "nutrients": [],
    "production": [],
    "world": [],
    "gi": [],
    "orgs": [],
    "sources": [{"n": n, "title": t, "url": u, "publisher": p, "accessed": a} for n, t, u, p, a in S],
}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in sections:
    print(s["key"], len(s["body"]))
