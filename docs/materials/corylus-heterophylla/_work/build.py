import json
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "dossier.json"
PM = "PubMed (National Library of Medicine)"
ACC = "2026-11-02"


def pm(title, doi, pmid=None):
    return {"title": title, "url": f"https://doi.org/{doi}" if doi else f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/", "publisher": PM, "accessed": ACC}


sources = [
    {"title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 개암·개암가루·개암나무열매·개암농축·개암분태·개암주스·개암추출물·개암페이스트·볶은개암·볶은개암분말·통헤이즐넛 11행, 학명 'Corylus heterophylla Fisch. ex Trautv.', 이명 '헤이즐넛, 진자', 사용조건 '사용가능부위 : 열매', 사용가능",
     "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
    {"title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 개암나무속 다른 행: Filbert씨앗(Corylus maxima / Corylus avellana, 영명 Filbert Giant, European hazel, 사용가능부위 씨앗), 참개암나무열매(Corylus sieboldiana / Corylus heterophylla var. sieboldiana, 이명 헤이즐넛), 물개암나무열매(C. sieboldiana var. mandshurica / C. mandshurica), 병개암나무열매(C. hallaisanensis), 콜루르나개암열매(C. colurna), 코르누타개암열매(C. cornuta), American hazelnut열매(C. americana), Chinese hazel열매(C. chinensis) 등 — 모두 사용가능",
     "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
    pm("Kernel Nutrient Composition and Antioxidant Ability of Corylus spp. in China. Front Plant Sci 2021;12:690966 (PMID 34249062; PMC8261296 전문 확인)", "10.3389/fpls.2021.690966"),
    pm("A chromosome-level reference genome of the hazelnut, Corylus heterophylla Fisch. GigaScience 2021;10(4):giab027 (PMID 33871007; PMC8054262 전문 확인)", "10.1093/gigascience/giab027"),
    pm("Genomic evidence of high gene flow and weak population structure in Siberian hazel (Corylus heterophylla). Front Plant Sci 2026;17:1844461 (PMID 42293021; PMC13253746 전문 확인)", "10.3389/fpls.2026.1844461"),
    pm("Predicting the potential distribution of Corylus heterophylla in China under future climate change using an optimized MaxEnt model. Front Plant Sci 2025;16:1668828 (PMID 41334201; 초록 확인)", "10.3389/fpls.2025.1668828"),
    pm("Species divergence and phylogeography of Corylus heterophylla Fisch complex (Betulaceae): Inferred from molecular, climatic and morphological data. Mol Phylogenet Evol 2022;168:107413 (PMID 35031460; 초록 확인)", "10.1016/j.ympev.2022.107413"),
    pm("Population genomics reveals demographic history and selection signatures of hazelnut (Corylus). Hortic Res 2023;10(5):uhad065 (PMID 37249951; 초록 확인)", "10.1093/hr/uhad065"),
    pm("Pistillate flower development and pollen tube growth mode during the delayed fertilization stage in Corylus heterophylla Fisch. Plant Reprod 2014;27(3):145-52 (PMID 25073757; 초록 확인)", "10.1007/s00497-014-0248-9"),
    pm("Comparison of ultrastructure, pollen tube growth pattern and starch content in developing and abortive ovaries during the progamic phase in hazel. Front Plant Sci 2014;5:528 (PMID 25339969; 초록 확인)", "10.3389/fpls.2014.00528"),
    pm("Transcriptome analysis and gene expression profiling of abortive and developing ovules during fruit development in hazelnut. PLoS One 2015;10(4):e0122072 (PMID 25836368; 초록 확인)", "10.1371/journal.pone.0122072"),
    pm("Transcriptome sequencing and identification of cold tolerance genes in hardy Corylus species (C. heterophylla Fisch) floral buds. PLoS One 2014;9(9):e108604 (PMID 25268521; 초록 확인)", "10.1371/journal.pone.0108604"),
    pm("Expression and Functional Analysis of WRKY Transcription Factors in Chinese Wild Hazel, Corylus heterophylla Fisch. PLoS One 2015;10(8):e0135315 (PMID 26270529; 초록 확인)", "10.1371/journal.pone.0135315"),
    pm("Visual and auditory cues facilitate cache pilferage of Siberian chipmunks (Tamias sibiricus) under indoor conditions. Integr Zool 2019;14(4):354-365 (PMID 30585411; 초록 확인)", "10.1111/1749-4877.12373"),
    pm("Exploration of the molecular interactions between angiotensin-I-converting enzyme (ACE) and the inhibitory peptides derived from hazelnut (Corylus heterophylla Fisch.). Food Chem 2018;245:471-480 (PMID 29287398; 초록 확인)", "10.1016/j.foodchem.2017.10.095"),
    pm("Novel anti-obesity peptide (RLLPH) derived from hazelnut (Corylus heterophylla Fisch) protein hydrolysates inhibits adipogenesis in 3T3-L1 adipocytes. J Biosci Bioeng 2020;129(3):259-268 (PMID 31630942; 초록 확인)", "10.1016/j.jbiosc.2019.09.012"),
    pm("In vivo assessment of immunomodulatory activity of hydrolysed peptides from Corylus heterophylla Fisch. J Sci Food Agric 2016;96(10):3508-14 (PMID 26585315; 초록 확인)", "10.1002/jsfa.7535"),
    pm("Protective role of hazelnut peptides on oxidative stress injury in human umbilical vein endothelial cells. J Food Biochem 2019;43(3):e12722 (PMID 31353565; 초록 확인)", "10.1111/jfbc.12722"),
    pm("From Microbiota to Metabolomics: How Corylus heterophylla Fisch. Male Flower Extract Shields Mice from Cognitive Decline. Nutrients 2025;17(24):3958 (PMID 41470904; 초록 확인)", "10.3390/nu17243958"),
    pm("Optimisation of the flash extraction process for male catkins of Corylus heterophylla and evaluation of their oxidative stress resistance. Nat Prod Res 2025 (PMID 41118558; 초록 확인)", "10.1080/14786419.2025.2570895"),
    {"title": "[Cloning and expression of a fragment of Corylus heterophylla 1 and identifying its immunologic competence]. Xi Bao Yu Fen Zi Mian Yi Xue Za Zhi 2011;27(1):4-6 (PMID 21208553; 초록 확인)",
     "url": "https://pubmed.ncbi.nlm.nih.gov/21208553/", "publisher": PM, "accessed": ACC},
    pm("Hazelnut allergome overview and Cor a gRNAs identification. BMC Plant Biol 2025;25(1):661 (PMID 40389868; PMC12087118 전문 확인)", "10.1186/s12870-025-06685-6"),
    pm("A dataset-calibrated multi-module model for evaluating plant oil similarity to human milk lipids. Food Chem 2026;532:151519 (PMID 42887246; 초록 확인)", "10.1016/j.foodchem.2026.151519"),
    pm("Comparative analysis of flavor profiles in Chinese hybrid hazelnut (Corylus heterophylla × Corylus avellana) under different roasting conditions using HS-SPME-GC-MS and UPLC-MS/MS. Food Chem 2025;493:145779 (PMID 40780167; 초록 확인)", "10.1016/j.foodchem.2025.145779"),
    pm("Feeding and attraction of Agelastica coerulea (Coleoptera: Chrysomelidae) to Betulaceae plants. J Econ Entomol 2004;97(6):1978-82 (PMID 15666753; 초록 확인)", "10.1093/jee/97.6.1978"),
    {"title": "Proteomic analysis of Corylus heterophylla fisch in Changbai Mountain by shotgun approach. Pak J Pharm Sci 2015;28(4 Suppl):1449-56 (PMID 26431657; 초록 확인)",
     "url": "https://pubmed.ncbi.nlm.nih.gov/26431657/", "publisher": PM, "accessed": ACC},
    pm("Stigmatic Transcriptome Analysis of Self-Incompatible and Compatible Pollination in Corylus heterophylla Fisch. × Corylus avellana L. Front Plant Sci 2022;13:800768 (PMID 35300011; 초록 확인)", "10.3389/fpls.2022.800768"),
    pm("Diaporthe and Diplodia Species Associated With Hazelnut Canker and Dieback in Beijing, China. Front Cell Infect Microbiol 2021;11:664366 (PMID 34408987; 초록 확인)", "10.3389/fcimb.2021.664366"),
]
for i, s in enumerate(sources, 1):
    s["n"] = i

S = {}
S["overview"] = """개암(Corylus heterophylla Fisch. ex Trautv.)은 자작나무과(Betulaceae) 개암나무속의 갈잎떨기나무로, 영어로는 Siberian hazel 또는 Asian hazel이라 부르며 동아시아에 널리 자라고 열매(견과)를 먹는다[4, 5]. 중국 북부·중부, 시베리아 남동부, 몽골 동부, 한국, 일본 등에 자생한다[6]. 영하 30–40 °C의 추위와 가뭄을 견디는 성질 때문에 유럽개암(C. avellana)과의 교잡 육종 재료로도 쓰인다[4].

식약처 「식품원료 목록」에는 개암·개암가루·개암나무열매·볶은개암·개암페이스트 등 이 학명을 단 11개 행이 있고, 모두 '사용가능' 원료이며 사용조건은 '사용가능부위 : 열매'다[1]. 목록은 '헤이즐넛'과 '진자'를 이명으로 적고 있지만, 흔히 헤이즐넛으로 유통되는 유럽개암(C. avellana)은 'Filbert씨앗'이라는 별도 행(C. maxima / C. avellana, 사용부위 씨앗)으로 올라 있다[1, 2]. 이 문서는 C. heterophylla 자료만 다루며, 유럽개암과 교잡종 자료는 따로 표시한다[3]. 이 종을 원재료로 하는 건강기능식품 고시형 원료는 확인하지 못함.

중국 랴오닝성 야생 개암 알맹이는 건물 100 g당 기름 50.23 g을 담고, 지방산의 71.32%가 올레산, 24.36%가 리놀레산이었다[3]. 알맹이 단백질 가수분해물에서 얻은 펩타이드의 효소 억제·세포·동물 실험 결과가 있으나, 사람 대상 임상시험은 확인하지 못함."""

S["history"] = """중국에서 개암은 자생 개암나무속 가운데 가장 가치 있고 널리 이용되어 온 종이며, 주로 북부와 동북부에 분포한다[3]. 근래에는 현지 주민이 직접 가꾸는 경우가 늘어 수확량이 꾸준히 늘고 있다고 보고되었다[3]. 한국 집단 유전체 연구는 이 종이 약 5,000년 동안 사람에게 이용되어 왔다는 앞선 연구를 인용했다[5].

1980년대부터 중국에서는 동북부의 개암을 어미로, 이탈리아에서 들여온 유럽개암 실생묘들의 꽃가루를 아비로 교배해 교잡 개암(핑어우, C. heterophylla × C. avellana)을 만들었다[3]. 약 15개 품종이 선발되어 2000–2010년 사이에 차례로 보급되었고, 주력 품종 '다웨이'를 포함한 교잡 개암 재배 면적은 약 50,000 ha로 중국 재배 면적의 절반 이상을 차지한다고 적혀 있다[3]. 이 면적은 교잡종의 값이며 순수한 개암의 재배 면적이 아니다[3].

한반도는 이 종이 대륙에서 분포하는 남동쪽 끝이며, 오래전부터 먹는 견과를 얻으려고 채취해 왔다[5]. 한국에서는 농가 부수입원과 도시공원 녹화 수종으로 정부 사업을 통해 재배가 장려되어 전국에 관리 집단이 흩어져 있다고 보고되었다[5]."""

S["biology"] = """개암은 암꽃과 수꽃이 한 그루에 피는(자웅동주) 떨기나무로 높이 약 7 m까지 자라고, 뿌리에서 움돋이가 많이 나와 퍼진다[5]. 염색체 수는 2n = 22이다[5]. 견과는 크기가 들쭉날쭉하고 한 송이에 1–7개씩 달리며, 각각 잎 모양의 총포에 싸인다[5]. 꽃가루는 바람으로 옮겨지고, 씨앗은 주로 작은 포유류가 퍼뜨린다[5]. 실험실 조건에서 다람쥐(Tamias sibiricus)가 개암 씨앗을 저장하고 훔치는 행동이 연구되었다[14].

개암나무속은 꽃가루받이 뒤 수정까지 2–3.5개월이 걸리는 '지연 수정'을 한다[9]. 개암에서는 꽃이 필 때 씨방과 밑씨가 보이지 않고, 개화 후 15–20일에 원기가 생기며 55일째에 성숙한 배낭이 분화했다[9]. 꽃가루관은 암술대 밑부분 공간에서 약 26일 머문 뒤 씨방으로 들어갔다[9]. 개암의 꽃차례당 암꽃 수는 5.8–6.2개, 송이당 열매 수는 3.5개였다[10]. 중국 동북부에서는 속이 빈 열매(쭉정이) 비율이 높아 수확 손실이 크다[11].

중국 내 야생 개암의 분포 범위는 북위 36.78–51.73°, 동경 100.57–132.20°로 주로 온대 기후다[4]. 최적화 MaxEnt 모델에서 분포를 가장 크게 좌우한 요인은 가장 습한 분기 강수량(39.5%)과 가장 건조한 분기 평균기온(22.2%)이었다[6]."""

S["related_species"] = """식약처 「식품원료 목록」에는 유럽개암(Filbert씨앗, C. maxima / C. avellana), 참개암나무, 물개암나무, 병개암나무, 콜루르나개암, 코르누타개암, American hazelnut 등 개암나무속 원료가 따로 올라 있다[2]. 참개암나무열매 행은 학명 칸에 'Corylus heterophylla var. sieboldiana'를 함께 적고 이명도 '헤이즐넛'이어서, 원료명과 학명을 함께 확인해야 개암과 섞이지 않는다[2].

한국에서는 개암과 참개암나무(Asian beaked hazel)의 분포가 크게 겹치며, 연구진은 견과를 덮는 총포의 정도로 두 종을 구별할 수 있는 여름철에 시료를 모았다[2, 5]. 곤충 먹이 선호 연구에서는 'C. heterophylla var. thunbergii'라는 변종명이 쓰였다[25]. 국가표준식물목록에서 이 변종명과 국명의 대응은 확인하지 못함.

중국 남부의 C. kweichowensis, C. yunnanensis와 함께 'C. heterophylla 복합군'을 이루며, 분자 자료로 C. yunnanensis가 먼저 갈라졌고 C. heterophylla와 C. kweichowensis는 거의 구분되지 않았다[7]. 교잡 개암(C. heterophylla × C. avellana) '다웨이'는 어미인 개암보다 올레산이 많고(85.19% 대 71.32%) 총페놀은 절반 이하였다(66.53 대 141.23 mg GAE/100 g DW)[3]. 따라서 교잡종과 유럽개암의 성분·알레르기 연구 값은 이 종의 값으로 옮겨 쓰지 않는다[3, 22]."""

S["cultivation"] = """중국에서는 야생 개암을 현지 주민이 관리·재배하는 사례가 늘고 있다[3]. 개암은 대규모 농장보다 저집약적인 혼농임업 방식으로 관리되어 넓은 지역에 흩어진 집단을 이룬다고 보고되었다[5]. 한국에서는 정부 사업으로 농가 소득 작물과 녹화 수종으로 재배가 장려되었다[5].

추위(영하 30–40 °C)와 가뭄에 강해 유럽개암이 겨울을 나지 못하는 중국 북부·내륙에서도 자랄 수 있다[4]. 1970–2000년 기후에서 중국 내 기후 적지 면적은 약 210.85 × 10⁴ km²(초록에서 지수 표기가 빠져 국토 비율로 환산 대조)로 국토의 21.96%였고, 미래 기후 시나리오에서는 적지가 북쪽으로 옮겨 갈 것으로 예측되었다[6]. 베이징의 야생 개암에서는 가지마름·궤양병을 일으키는 곰팡이 51균주가 분리되었다[28]. 동북부에서는 암꽃 씨방의 낙과와 쭉정이 열매가 수량을 떨어뜨리는 주요 문제다[10, 11].

이 종의 국내 재배 면적·생산량 통계는 확인하지 못함. 지리적 표시 등록도 확인하지 못함."""

S["processing"] = """식약처 「식품원료 목록」의 원료명으로 보아 개암은 가루, 농축, 분태(잘게 부순 것), 주스, 추출물, 페이스트, 볶은 개암, 볶은 개암 분말, 통 견과 형태로 식품에 쓰인다[1]. 식약처 「식품 등의 생산실적」에서 개암 원료 건강기능식품 실적은 확인하지 못함.

알맹이 기름은 Soxhlet 추출로 건물 100 g당 50.23 g이 얻어졌다[3]. 기름을 짜고 남은 개암 박(찌꺼기)은 단백질 가수분해 펩타이드의 원료로 연구되었다[17]. 20가지 식물성 기름을 사람 젖 지질과 비교한 모델에서 개암 기름은 초유와 가장 비슷한 기름으로 꼽혔지만, 이는 자료 기반 선별 단계의 결과다[23]. 장백산 개암 단백질의 산탄총 프로테오믹스에서는 303개 단백질이 확인되었다[26].

볶음 조건(110 °C 150분, 130 °C 50분, 150 °C 35분)과 향미 성분 147종 연구는 교잡 개암 '다웨이' 대상이어서 이 종에 그대로 적용할 수 없다[24]. 견과를 얻은 뒤 남는 수꽃차례는 82% 에탄올, 53초, 액고비 33 mL/g 조건의 순간 추출법이 최적화되었으나 식품원료 목록의 사용 부위(열매)가 아니다[1, 20]."""

S["genetics"] = """개암의 염색체 수준 기준 유전체는 나노포어 장독 서열과 Hi-C로 조립되었고, 전체 길이 370.75 Mb 중 361.90 Mb(97.61%)가 11개 염색체에 배치되었다[4]. 단백질 암호 유전자는 27,591개이고 BUSCO 완전성은 93.47%, 반복서열은 56.71%였다[4]. 계통 분석에서 개암은 Ostrya japonica와 가까우며 약 5,279만 년 전에 공통 조상에서 갈라졌다고 추정되었다[4].

한국 20개 집단 161개체의 4,378개 SNP 분석에서 평균 기대 이형접합도는 0.28, 평균 FST는 0.05로 집단 간 분화가 낮았고 거리에 따른 격리도 나타나지 않았다[5]. 연구진은 약 8만 년 전과 4만 년 전 두 차례 유효 집단 크기 감소를 추정했고, 높은 유전자 흐름이 사람의 이동·재배와 관련 있을 수 있다고 보았다[5]. 유라시아 개암나무속 125개 계통의 전장 재분석에서는 유럽 계통과 아시아 계통이 뚜렷이 나뉘었다[8]. C. heterophylla 복합군의 두 큰 갈래는 약 1,289만 년 전 쓰촨 분지 형성 시기에 갈라졌다[7].

추위 내성 연구로 꽃눈 전사체에서 40,941개 유전자 단위가 확인되었고[12], WRKY 전사인자 30개 가운데 23개가 추위·가뭄·염분 스트레스에 모두 발현이 늘었다[13]. 교잡 개암의 자가불화합성 연구도 진행되었다[27]."""

S["safety"] = """개암 11개 행은 식약처 「식품원료 목록」에서 모두 사용가능 원료이며, 사용조건은 '사용가능부위 : 열매'다[1]. 이 종에 대한 식약처 등 국내 공공기관의 잔류·독성 정보와 국내 알레르기 표시 대상 여부는 확인하지 못함. 사람을 대상으로 한 섭취 안전성 시험도 확인하지 못함.

[이 종 근거] 개암의 Cor h 1 유전자 조각(243 bp, 81개 아미노산)을 발현 벡터에 넣어 만든 재조합 단백질은 IgE와 잘 결합했다고 보고되었다[21]. 개암 유전체에서도 유럽개암 알레르겐 13종(Cor a 1·2·6·8–16과 Cor a TLP)의 상동 유전자가 모두 확인되었다[22]. 그러나 개암 견과를 먹은 사람의 알레르기 사례 보고는 확인하지 못함.

[개암나무속 일반] 유럽개암(C. avellana)에서는 알레르겐 13종이 보고되었고(이 가운데 Cor a TLP는 WHO/IUIS 명명 데이터베이스 미등록), 헤이즐넛은 유럽에서 견과 알레르기의 주요 원인으로 꼽힌다[22]. 씨앗 저장단백질과 지질전달단백질은 전신 반응 위험을 높이고, PR-10 계열 단백질은 열에 약하며 가벼운 국소 반응과 관련된다고 정리되었다[22]. 네 종 사이 알레르겐 상동 단백질의 아미노산 일치도는 평균 90% 이상이어서 교차 반응 가능성을 생각해야 한다[22].

펩타이드 6종은 사람 제대정맥 내피세포에서 독성을 보이지 않았고[18], 생쥐에게 펩타이드를 200–800 mg/kg로 30일 먹인 시험은 면역 지표만 보고했다[17]. 이 결과들은 세포·동물 실험이므로 사람의 안전성 근거로 볼 수 없다[17, 18]."""

titles = {"overview": "한눈에 보기", "history": "역사와 이용", "biology": "식물학적 특징", "related_species": "이름과 가까운 종",
          "cultivation": "재배와 산지", "processing": "가공과 이용", "genetics": "유전 정보", "safety": "안전성"}

compounds = [
    {"name": "Oleic acid", "name_ko": "올레산", "class": "단일불포화지방산(C18:1)", "role": "nutrient", "part": "열매(알맹이) 기름",
     "content_text": "지방산 조성의 71.32 ± 0.23%(중국 랴오닝성 톄링 야생, 2017년 9월 채취, GC-FID 면적 백분율)[3]",
     "activity_ko": "다섯 시료(야생 4종·교잡 1품종) 가운데 가장 낮은 올레산 비율로, 교잡 개암 '다웨이'(85.19%)와 구별된다[3]", "source": [3]},
    {"name": "Linoleic acid", "name_ko": "리놀레산", "class": "다가불포화지방산(C18:2, n-6)", "role": "nutrient", "part": "열매(알맹이) 기름",
     "content_text": "지방산 조성의 24.36 ± 0.23%(다섯 시료 중 최고)[3]",
     "activity_ko": "필수지방산; 개암 기름의 특징으로 '낮은 기름 함량·높은 리놀레산'이 보고됨[3]", "source": [3]},
    {"name": "Palmitic acid", "name_ko": "팔미트산", "class": "포화지방산(C16:0)", "role": "nutrient", "part": "열매(알맹이) 기름",
     "content_text": "지방산 조성의 2.06 ± 0.02%; 총포화지방산 3.08%, 총불포화지방산 96.36%[3]",
     "activity_ko": "개암 기름의 주된 포화지방산; 불포화/포화 비율 31.29로 다섯 시료 중 가장 높음[3]", "source": [3]},
    {"name": "alpha-Linolenic acid", "name_ko": "알파-리놀렌산", "class": "다가불포화지방산(C18:3, n-3)", "role": "nutrient", "part": "열매(알맹이) 기름",
     "content_text": "지방산 조성의 0.29 ± 0.00%(PMC 본문 변환에서 표 머리글이 빠져, 다가불포화지방산 합계 24.66% = 리놀레산 24.36% + 0.29%로 대조해 판단)[3]",
     "activity_ko": "n-3 필수지방산; 이 종 기름에서의 생리활성 시험은 확인하지 못함", "source": [3]},
    {"name": "alpha-Tocopherol", "name_ko": "알파-토코페롤", "class": "비타민 E", "role": "nutrient", "part": "열매(알맹이) 기름",
     "content_text": "23.54 ± 0.73 mg/100 g 기름; 총토코페롤 29.75 mg/100 g 기름(HPLC-UV 284 nm)[3]",
     "activity_ko": "지용성 항산화 비타민; 이 연구에서 기름의 총토코페롤과 ABTS·DPPH 소거능은 유의한 상관이 없었음[3]", "source": [3]},
    {"name": "gamma-Tocopherol", "name_ko": "감마-토코페롤(베타+감마 합산)", "class": "비타민 E", "role": "nutrient", "part": "열매(알맹이) 기름",
     "content_text": "베타+감마-토코페롤 합산 6.21 ± 0.04 mg/100 g 기름(두 성분을 분리 정량하지 않음); 델타-토코페롤은 검출되지 않음[3]",
     "activity_ko": "비타민 E 동족체; 교잡 개암 '다웨이'(2.09 mg/100 g 기름)보다 많음[3]", "source": [3]},
    {"name": "Ascorbic acid", "name_ko": "비타민 C(아스코르브산)", "class": "수용성 비타민", "role": "nutrient", "part": "열매(알맹이)",
     "content_text": "11.50 ± 0.38 mg/100 g DW(몰리브덴 청 비색법)[3]",
     "activity_ko": "탈지 가루의 ABTS 소거능과 양의 상관(r = 0.924, 다섯 시료 합산 분석)[3]", "source": [3]},
    {"name": "L-Arginine", "name_ko": "아르지닌", "class": "아미노산", "role": "nutrient", "part": "열매(알맹이)",
     "content_text": "가수분해 아미노산 2.69 ± 0.02 g/100 g DW, 유리 아미노산 10.29 ± 0.76 mg/100 g DW(다섯 시료 중 최고); 가수분해 아미노산 총량 15.32 g/100 g DW[3]",
     "activity_ko": "개암 알맹이 단백질에 많은 아미노산; 생리활성 시험은 확인하지 못함", "source": [3]},
    {"name": "L-Glutamic acid", "name_ko": "글루탐산", "class": "아미노산", "role": "nutrient", "part": "열매(알맹이)",
     "content_text": "가수분해 아미노산 2.24 ± 0.04 g/100 g DW, 유리 아미노산 6.10 ± 0.18 mg/100 g DW[3]",
     "activity_ko": "알맹이 단백질의 주요 아미노산; 유리 트립토판은 검출되지 않음[3]", "source": [3]},
    {"name": "Tyr-Leu-Val-Arg", "name_ko": "YLVR 펩타이드", "class": "단백질 가수분해 펩타이드(4개 아미노산)", "role": "bioactive", "part": "열매(알맹이) 단백질 가수분해물",
     "content_text": "가수분해물에서 이온교환·겔여과·역상 HPLC로 정제하고 LC-ESI-MS/MS로 동정(함량 확인하지 못함)[15]",
     "activity_ko": "ACE 억제 IC50 15.42 μM, 비경쟁적 억제(효소 실험); 같은 연구의 AVKVL 73.06 μM, TLVGR 249.3 μM[15]", "source": [15]},
    {"name": "Arg-Leu-Leu-Pro-His", "name_ko": "RLLPH 펩타이드", "class": "단백질 가수분해 펩타이드(5개 아미노산)", "role": "bioactive", "part": "열매(알맹이) 단백질 가수분해물",
     "content_text": "가수분해물 C3 분획에서 LC-MS/MS로 동정 후 합성해 시험(함량 확인하지 못함)[16]",
     "activity_ko": "3T3-L1 지방세포에서 PPARγ·C/EBPα 등 지방생성 유전자 발현을 낮추고 AMPK 인산화를 높임(세포 실험)[16]", "source": [16]},
    {"name": "Glu-Trp", "name_ko": "EW 펩타이드(항산화 펩타이드 6종 중 하나)", "class": "단백질 가수분해 펩타이드", "role": "bioactive", "part": "열매(알맹이) 단백질 가수분해물",
     "content_text": "야생 개암 단백질 가수분해물의 항산화 펩타이드 6종(EW, DWDPK, ADGF, SGAF, ETTL, AGGF) 가운데 하나(함량 확인하지 못함)[18]",
     "activity_ko": "EW·ADGF·DWDPK가 안지오텐신 II로 산화 손상을 준 사람 제대정맥 내피세포에서 ROS·말론다이알데하이드를 낮추고 NOX4·p22phox를 줄임(세포 실험)[18]", "source": [18]},
    {"name": "Luteolin", "name_ko": "루테올린", "class": "플라본", "role": "bioactive", "part": "수꽃(식품원료 목록의 사용 부위 아님)",
     "content_text": "수꽃 추출물의 주된 플라보노이드로 UHPLC-MS에서 확인(함량 수치는 초록에 없어 확인하지 못함)[19]",
     "activity_ko": "BV2 미세아교세포에서 M1형을 M2형 쪽으로 바꿈(세포 실험); 수꽃 추출물 200 mg/kg을 먹인 LPS 생쥐에서 인지 저하 완화(동물 실험)[19]", "source": [19]},
    {"name": "Kaempferol", "name_ko": "캠페롤", "class": "플라보놀", "role": "bioactive", "part": "수꽃(식품원료 목록의 사용 부위 아님)",
     "content_text": "수꽃 추출물의 주된 플라보노이드로 UHPLC-MS에서 확인(함량 확인하지 못함)[19]",
     "activity_ko": "BV2 미세아교세포의 M1→M2 극성 전환(세포 실험)[19]", "source": [19]},
]

nutrients = [
    {"form": "개암 알맹이(중국 랴오닝성 톄링 야생, 2017년 9월 채취; 10일 바람 건조 후 80 °C 항량 건조) — 논문 정량값, 국가표준식품성분표 값 아님; 초록의 기름 범위(52.97–60.88 g/100 g DW)는 표 2의 개암 값 50.23과 맞지 않아 표 값을 씀",
     "basis": "건물(DW) 100 g; 토코페롤은 기름 100 g",
     "items": [
         {"name": "지방(기름)", "value": 50.23, "unit": "g"},
         {"name": "가수분해 아미노산 총량", "value": 15.32, "unit": "g"},
         {"name": "비타민 C", "value": 11.5, "unit": "mg"},
         {"name": "총토코페롤(기름 100 g당)", "value": 29.75, "unit": "mg"},
         {"name": "총페놀(갈산 당량)", "value": 141.23, "unit": "mg"},
         {"name": "총플라보노이드(루틴 당량)", "value": 252.82, "unit": "mg"}],
     "source": [3]},
]

common_prep = "알맹이 10일 바람 건조(수분 6.20%) 후 80 ± 2 °C 항량 건조·분쇄; Soxhlet(에테르, 50 °C, 8시간)로 기름과 탈지 가루 분리"
assays = [
    {"role": "literature", "compound": "Fatty acids (oleic, linoleic, palmitic acid 등 8종)", "compound_ko": "지방산 조성",
     "part": "열매(알맹이) 기름", "content": "올레산 71.32%, 리놀레산 24.36%, 팔미트산 2.06%; 기름 50.23 g/100 g DW[3]",
     "method": "GC-FID(지방산 메틸에스터)",
     "conditions": {"instrument": "Agilent GC 7890A, 분할/비분할 주입구, FID", "column": "AB-FFAP 30 m × 0.25 mm × 0.25 μm",
                    "mobile_phase": "운반기체 질소(압력 20 PSI)", "gradient": "50 °C 1분 유지 → 15 °C/min으로 200 °C, 45분 유지",
                    "flow": "", "temp": "주입구 250 °C, 검출기 270 °C", "detection": "FID; 머무름 시간을 표준품 FAME와 비교, 면적 내부정규화(%)",
                    "injection": "분할 20:1, 1 mL(원문 표기 그대로)",
                    "sample_prep": common_prep + "; 기름 100 μL + 0.5 mol/L KOH-메탄올 1 mL + 에테르 2 mL로 실온 3시간 이상 메틸화, 무수 황산나트륨 탈수, 0.2 μm 나일론 필터",
                    "standard": "지방산 메틸에스터 표준품(머무름 시간 대조)", "linearity": "", "lod": "", "loq": "", "recovery": ""},
     "rationale": "개암 기름은 낮은 기름 함량과 높은 리놀레산이 특징이어서 교잡 개암·다른 종과 구별하는 지표가 된다[3]. 전문(Methods)에서 조건을 옮겼고 검출·정량한계와 회수율은 논문에 없어 확인하지 못함.",
     "source": [3], "url": "https://doi.org/10.3389/fpls.2021.690966", "source_kind": "paper"},
    {"role": "literature", "compound": "alpha-Tocopherol; (beta+gamma)-Tocopherol; delta-Tocopherol", "compound_ko": "토코페롤(비타민 E)",
     "part": "열매(알맹이) 기름", "content": "알파 23.54, 베타+감마 6.21, 델타 불검출, 총 29.75 mg/100 g 기름[3]",
     "method": "RP-HPLC-UV",
     "conditions": {"instrument": "Waters 2695, 자외선 검출기", "column": "Sunfire C18 4.6 × 250 mm, 5 μm", "mobile_phase": "메탄올",
                    "gradient": "", "flow": "1.2 mL/min", "temp": "", "detection": "UV 284 nm", "injection": "20 μL",
                    "sample_prep": "기름 250 mg을 다이에틸에테르 0.2 mL에 녹임", "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""},
     "rationale": "견과 기름의 대표 항산화 영양성분으로 종 간 비교에 쓰였다[3]. 전문에서 조건을 옮겼으며 표준품·검량선·검출한계는 원문(인용 방법)에 적혀 있지 않아 확인하지 못함.",
     "source": [3], "url": "https://doi.org/10.3389/fpls.2021.690966", "source_kind": "paper"},
    {"role": "literature", "compound": "Amino acids (free and hydrolysed; arginine, glutamic acid 등 17종)", "compound_ko": "아미노산(유리·가수분해)",
     "part": "열매(알맹이)", "content": "가수분해 아미노산 총 15.32 g/100 g DW(아르지닌 2.69, 글루탐산 2.24), 유리 아미노산 총 30.86 mg/100 g DW[3]",
     "method": "RP-HPLC-형광(AccQ Taq 유도체화)",
     "conditions": {"instrument": "Waters 2695, 2475 형광검출기", "column": "AccQ Taq 아미노산 칼럼 3.9 × 150 mm",
                    "mobile_phase": "A: 140 mmol/L 아세트산나트륨 완충액(17 mmol/L 트라이에틸아민, pH 4.95); B: 60% 아세토나이트릴 수용액",
                    "gradient": "A→B 단계적 기울기(세부 시간표는 원문에 없음)", "flow": "1.0 mL/min", "temp": "",
                    "detection": "형광 Ex 250 nm / Em 395 nm", "injection": "", "sample_prep": common_prep,
                    "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""},
     "rationale": "개암 알맹이는 비교한 다섯 시료 가운데 가수분해 아미노산 총량이 가장 많아 단백질 품질 비교 지표로 쓰였다[3]. 전문에서 조건을 옮겼고 가수분해 조건·검출한계·회수율은 원문에 없어 확인하지 못함.",
     "source": [3], "url": "https://doi.org/10.3389/fpls.2021.690966", "source_kind": "paper"},
]

d = {
    "slug": "corylus-heterophylla",
    "name_ko": "개암",
    "name_en": "Siberian hazel (Asian hazel)",
    "scientific_name": "Corylus heterophylla Fisch. ex Trautv.",
    "aliases": ["개암나무열매", "개암가루", "볶은개암", "개암페이스트", "통헤이즐넛", "진자", "헤이즐넛(식품원료 목록 이명)", "Siberian hazel", "Asian hazel", "Corylus heterophylla Fisch."],
    "sections": [{"key": k, "title": titles[k], "body": S[k]} for k in titles],
    "compounds": compounds,
    "markers": [],
    "nutrients": nutrients,
    "assays": assays,
    "production": [],
    "world": [],
    "gi": [],
    "orgs": [],
    "sources": sources,
}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
print("ok", len(sources), len(compounds))
