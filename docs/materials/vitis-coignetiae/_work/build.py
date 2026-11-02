import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
A = "2026-11-02"
def pm(n, title, doi, pmid, extra, pmc=None):
    t = f"{title} (PMID {pmid}" + (f", {pmc}" if pmc else "") + f", {extra})"
    return {"n": n, "title": t, "url": f"https://doi.org/{doi}", "publisher": "PubMed", "accessed": A}
S = [
 {"n": 1, "title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 머루·머루열매·머루씨앗·건조머루·머루주스·산머루농축액·머루발효액·머루발효농축액(Vitis coignetiae Pulliat ex Planch / Vitis amurensis var. coignetii (Pulliat) Nakai; 이명 산포도, 산머루; Crimson glory vine, Crimson grapevine), 사용가능, 사용가능부위: 열매, 씨앗; 같은 속·과의 다른 행(왕머루열매 V. amurensis, 새머루열매 V. flexuosa, 까마귀머루열매 V. ficifolia var. sinuata, 산머루원액 V. kaempferi, 개머루 Ampelopsis brevipedunculata 사용불가) 대조 (로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json)", "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
 pm(2, "Differences in the phenolic composition and antioxidant properties between Vitis coignetiae and Vitis vinifera seeds extracts — Molecules 2013", "10.3390/molecules18033410", "23493104", "전문 확인; 본문 일부 문장과 표의 종 배정이 엇갈려 표 값을 따름", "PMC6270441"),
 pm(3, "Analysis and tentative structure elucidation of new anthocyanins in fruit peel of Vitis coignetiae Pulliat (meoru) using LC-MS/MS — J Sep Sci 2010", "10.1002/jssc.200900748", "20187032", "초록만 확인"),
 pm(4, "Stability of meoru (Vitis coignetiea) anthocyanins under photochemically produced singlet oxygen by riboflavin — N Biotechnol 2010", "10.1016/j.nbt.2010.01.003", "20085831", "초록만 확인"),
 pm(5, "Induction of apoptosis and inhibition of invasion in human hepatoma cells by anthocyanins from meoru — Ann N Y Acad Sci 2009", "10.1111/j.1749-6632.2009.04689.x", "19723048", "초록만 확인; 안토시아닌 조성비는 정정본 값"),
 pm(6, "The involvement of AMPK/GSK3-beta signals in the control of metastasis and proliferation in hepato-carcinoma cells treated with anthocyanins extracted from Korea wild berry Meoru — BMC Complement Altern Med 2014", "10.1186/1472-6882-14-109", "24666969", "전문 확인", "PMC3974438"),
 pm(7, "Inhibition of adipocyte differentiation by anthocyanins isolated from the fruit of Vitis coignetiae Pulliat is associated with the activation of AMPK signaling pathway — Toxicol Res 2018", "10.5487/TR.2018.34.1.013", "29371997", "전문 확인", "PMC5776908"),
 pm(8, "Retraction notice: Anthocyanins derived from Vitis coignetiae Pulliat contributes anti-cancer effects by suppressing NF-κB pathways in Hep3B human hepatocellular carcinoma cells and in vivo (Molecules 2020;25:5445, PMID 33233701 철회) — Molecules 2026", "10.3390/molecules31203778", "42908393", "철회 공지 초록 확인", "PMC13687675"),
 pm(9, "Anti-genotoxic activity of Vitis coignetiae Pulliat towards heterocyclic amines and isolation and identification of caftaric acid as an antimutagenic component from the juice — Mutat Res 2011", "10.1016/j.mrgentox.2011.05.001", "21601008", "초록만 확인"),
 pm(10, "2,6-Dimethoxy-1,4-benzoquinone, isolation and identification of anti-carcinogenic, anti-mutagenic and anti-inflammatory component from the juice of Vitis coignetiae — Food Chem Toxicol 2018", "10.1016/j.fct.2018.10.028", "30316843", "초록만 확인"),
 pm(11, "Chemopreventive effects and anti-tumorigenic mechanisms of 2,6-dimethoxy-1,4-benzoquinone, a constituent of Vitis coignetiae Pulliat, toward NNK-induced lung tumorigenesis in A/J mice — Food Chem Toxicol 2021", "10.1016/j.fct.2021.112319", "34087405", "초록만 확인"),
 pm(12, "Chemopreventive effects of the juice of Vitis coignetiae Pulliat on two-stage mouse skin carcinogenesis — Nutr Cancer 2013", "10.1080/01635581.2013.767916", "23530644", "초록만 확인"),
 pm(13, "Pterostilbene from Vitis coignetiae protect H2O2-induced inhibition of gap junctional intercellular communication in rat liver cell line — Food Chem Toxicol 2008(온라인)", "10.1016/j.fct.2008.11.038", "19101604", "초록만 확인; 분석 부위는 초록에 없음"),
 pm(14, "Resveratrol, purified from the stem of Vitis coignetiae Pulliat, inhibits food intake in C57BL/6J mice — Arch Pharm Res 2010", "10.1007/s12272-010-0518-5", "20512477", "초록만 확인"),
 pm(15, "Protective effects of Vitis coignetiae vine stem extract against carbon tetrachloride-induced acute liver injury in mice — Antioxidants (Basel) 2026", "10.3390/antiox15050651", "42193272", "전문 확인", "PMC13203357"),
 pm(16, "Powerful hepatoprotective and hepatotoxic plant oligostilbenes, isolated from the Oriental medicinal plant Vitis coignetiae (Vitaceae) — Experientia 1995", "10.1007/BF01964921", "7843333", "초록만 확인; 추출 부위는 초록에 없음"),
 pm(17, "Rhapontigenin inhibited hypoxia inducible factor 1 alpha accumulation and angiogenesis in hypoxic PC-3 prostate cancer cells — Biol Pharm Bull 2011", "10.1248/bpb.34.850", "21628883", "초록만 확인"),
 pm(18, "Beneficial effects of Vitis coignetiae Pulliat leaves on nonalcoholic steatohepatitis in a rat model — Acta Med Okayama 2009", "10.18926/AMO/31835", "19404342", "초록만 확인"),
 pm(19, "A novel resistance locus from an unexploited East Asian Vitis coignetiae confers resistance to grapevine downy mildew — Theor Appl Genet 2026", "10.1007/s00122-026-05273-y", "42223657", "전문 확인", "PMC13226344"),
 pm(20, "Native fruit tree genetic resources in Japan — Breed Sci 2016 (리뷰)", "10.1270/jsbbs.66.82", "27069393", "초록 확인; PMC 전문은 학명이 빠진 형태라 초록 서술만 사용", "PMC4780805"),
 pm(21, "Characterization and quantification of anthocyanins in grape juices obtained from the grapes cultivated in Korea by HPLC/DAD, HPLC/MS, and HPLC/MS/MS — J Food Sci 2008", "10.1111/j.1750-3841.2008.00756.x", "18576983", "초록만 확인; 시료는 머루×V. labrusca 교잡 품종"),
 pm(22, "Antihypertensive angiotensin I-converting enzyme inhibitory activity and antioxidant activity of Vitis hybrid-Vitis coignetiae red wine made with Saccharomyces cerevisiae — Mycobiology 2011", "10.4489/MYCO.2011.39.2.137", "22783093", "초록만 확인", "PMC3385101"),
 pm(23, "Analytical features of MP-AES for the quantitation of manganese in wild grape (Vitis coignetiae) red wines: comparison with ICP-OES — Food Chem 2018(온라인)", "10.1016/j.foodchem.2018.08.114", "30372927", "초록만 확인"),
 pm(24, "Inhibitory effects of the phenolic fraction from the pomace of Vitis coignetiae on biofilm formation by Streptococcus mutans — Arch Oral Biol 2012", "10.1016/j.archoralbio.2012.01.001", "22284343", "초록만 확인"),
 pm(25, "Endothelium-dependent vasorelaxant effects of dealcoholized wine powder of wild grape (Vitis coignetiae) in the rat thoracic aorta — Evid Based Complement Alternat Med 2016", "10.1155/2016/6846084", "27840653", "초록만 확인", "PMC5093294"),
 pm(26, "Narthecium asiaticum Maxim. poisoning of grazing cattle: observations on spontaneous and experimental cases — Cornell Vet 1985", "https://pubmed.ncbi.nlm.nih.gov/3987297/", "3987297", "초록만 확인"),
 pm(27, "The endophytic microbiome of wild grapevines Vitis amurensis Rupr. and Vitis coignetiae Pulliat growing in the Russian Far East — Plants (Basel) 2023", "10.3390/plants12162952", "37631163", "초록만 확인", "PMC10460016"),
 pm(28, "High-throughput sequencing indicates novel virus infections (provisionally Vitis varicosavirus, Vitis emaravirus, Vitis crypticvirus) in Vitis coignetiae — Viruses 2021", "10.3390/v13050827", "34063722", "초록만 확인", "PMC8147796"),
 pm(29, "Antimutagenic, anti-inflammatory, and antioxidative activities of the juice of Vitis ficifolia var. ganebu, in comparison with the juice of Vitis coignetiae — Genes Environ 2021", "10.1186/s41021-021-00225-y", "34772463", "초록만 확인", "PMC8588599"),
 pm(30, "Pretreatment of anthocyanin from the fruit of Vitis coignetiae acts as a potent inhibitor of TNF-α effect by inhibiting NF-κB-regulated genes in human breast cancer cells — Molecules 2020", "10.3390/molecules25102396", "32455624", "초록만 확인", "PMC7287973"),
 pm(31, "Optimisation of microwave-assisted extraction for functional properties of Vitis coignetiae extract by response surface methodology — J Sci Food Agric 2012", "10.1002/jsfa.5546", "22227835", "초록만 확인; 원료 부위는 초록에 없음"),
 pm(32, "Characterization of a profile of the anthocyanins isolated from Vitis coignetiae Pulliat and their anti-invasive activity on HT-29 human colon cancer cells — Food Chem Toxicol 2010", "10.1016/j.fct.2009.12.031", "20060025", "초록만 확인"),
 pm(33, "Intra-specific trends of lumen and wall resistivities of vessels within the stem xylem vary among three woody plants — Tree Physiol 2018", "10.1093/treephys/tpx114", "29036681", "초록만 확인"),
]
for s in S:
    if s["url"].startswith("https://doi.org/https://"):
        s["url"] = s["url"][len("https://doi.org/"):]
sections = [
 ("overview", "한눈에 보기", """머루(Vitis coignetiae Pulliat ex Planch.)는 포도속의 덩굴식물로 동아시아(주로 일본·한국·러시아 일부)가 원산이며, 영어로 crimson glory vine이라 부른다[19]. 식약처 「식품원료 목록」에는 머루·머루열매·머루씨앗·건조머루·머루주스·산머루농축액·머루발효액·머루발효농축액 등 8개 원료명이 같은 학명(이명 Vitis amurensis var. coignetii (Pulliat) Nakai)으로 올라 있고, 목록의 이명은 산포도·산머루다[1]. 8행 모두 식품원료(A코드)이며 상태는 '사용가능', 사용 조건은 '사용가능부위 : 열매, 씨앗'이다[1]. 부위 칸은 머루열매 행이 '열매', 머루씨앗 행이 '씨앗', 나머지 6행이 '-'로 적혀 있다[1]. 이 종을 원재료로 하는 건강기능식품 고시형 원료는 확인하지 못함.

열매는 한국 민간요법에서 염증성 질환 등에 쓰였다고 소개되고[30], 일본에서는 폴리페놀·안토시아닌이 많아 건강 주스와 와인으로 쓰인다[18]. 열매 껍질에서 안토시아닌 18종이 동정되었고[3], 주스에서는 카프타르산·페르타르산·2,6-다이메톡시-1,4-벤조퀴논이 항돌연변이·항염 성분으로 분리되었다[9, 10]. 효과 근거는 거의 모두 세포·동물 실험이며, 사람에게 먹여 효과를 본 임상시험은 PubMed에서 찾지 못해 확인하지 못함."""),
 ("history", "역사", """일본 국립 과수연구기관 소속 저자의 2016년 리뷰는 머루를 근래 소규모 재배에 들어간 일본 자생 과수의 하나로 꼽았다[20]. 일본에서 머루(야마부도)는 열매에 폴리페놀과 안토시아닌이 많아 건강 주스와 와인 원료로 쓰여 왔다[18]. 2026년 육종 논문은 머루가 원산지에서 관상용으로, 그리고 그보다 적게 와인 양조용으로 재배되지만 상업적 중요성은 유럽포도나 교잡종보다 작다고 적었다[19].

한국에서는 머루 열매가 염증성 질환과 암 치료에 쓰인 민간 약재로 소개되며[30], 2007년 9월 중순 지리산에서 채집한 열매가 안토시아닌 연구의 재료로 쓰였다[6]. 국내 연구진은 한국에서 야생으로 자란 머루의 열매 껍질 안토시아닌을 LC-MS/MS로 분석했다[3]. 일본에서는 1985년 방목 소 집단 폐사를 조사하면서, 소가 많이 먹었을 것으로 추정된 풀의 하나로 머루를 소에게 먹이는 시험을 했다[26]. 한국에서 머루를 먹어 온 역사와 옛 문헌 기록은 공공기관 자료로 확인하지 못함."""),
 ("biology", "식물학적 특징", """머루는 포도과(Vitaceae) 포도속(Vitis)에 속하는 목본 덩굴식물이다[16, 33]. 동아시아, 주로 일본·한국과 러시아 일부에 자생하며[19], 러시아 극동에서는 왕머루와 함께 야생으로 자라는 개체가 미생물 연구에 쓰였다[27]. 일본 온대림 연구에서는 뽕나무류·단풍나무류와 함께 줄기 물관의 수리 저항을 비교한 덩굴성 수종으로 다뤄졌다[33].

열매 껍질에는 안토시아닌이 모여 있어, 국내 야생 머루 껍질에서 말비딘·페오니딘·페투니딘·시아니딘 계열을 포함한 18종이 동정되었다[3]. 머루 열매 안토시아닌은 델피니딘·시아니딘·페투니딘·말비딘·페오니딘의 3-글루코사이드와 3,5-다이글루코사이드로 구성된다고 보고되었다[5]. 씨앗에는 탄닌과 갈산이 많고 카테킨·p-쿠마르산·페룰산·카페산이 들어 있다[2]. 머루와 유럽 품종을 교잡한 계통(COxGT2)은 잎 뒷면 털 밀도가 최고 등급(9)이었다[19]. 꽃·잎 모양, 암수 구분, 개화·결실 시기 같은 형태 정보는 공공기관 자료로 확인하지 못함."""),
 ("related_species", "이름과 가까운 종", """식약처 목록에는 포도속 원료가 여럿 있어 머루와 구분해야 한다[1]. 왕머루(V. amurensis Ruprecht)는 '왕머루열매', 새머루(V. flexuosa Thunberg)는 '새머루열매', 까마귀머루(V. ficifolia var. sinuata 등)는 '까마귀머루열매'로 따로 올라 있고, 셋 다 열매만 사용가능하다[1]. '산머루원액'은 이름과 달리 학명이 Vitis kaempferi K. Koch.로 적힌 별도 행이고, 새머루의 이명도 '산포도'여서 이름만으로는 머루와 헷갈리기 쉽다[1]. 포도과의 개머루(Ampelopsis brevipedunculata)는 '사용불가'다[1].

목록은 머루의 이명으로 V. amurensis var. coignetii를 함께 적었지만, 2026년 육종 연구는 머루와 왕머루를 다른 동아시아 종으로 다뤘고 머루 유래 저항성 좌위 Rpv32가 왕머루 유래 Rpv10·Rpv12와 SSR 대립유전자 크기가 달라 공통 조상이 아니라고 보고했다[1, 19]. 한국에서 '머루' 이름이 붙은 포도 품종 Oll-Meoru·Neut-Meoru는 머루와 V. labrusca의 교잡종이어서 순수 머루 자료와 섞으면 안 된다[21]. 일본 류큐의 V. ficifolia var. ganebu 주스는 머루 주스와 활성 성분이 다르다고 보고되었다[29]. 유럽포도(V. vinifera) 씨앗과 비교하면 머루 씨앗은 총페놀·탄닌·카테킨이 더 적었다[2]."""),
 ("cultivation", "재배와 산지", """2016년 리뷰는 머루를 일본에서 근래 소규모 재배가 시작된 자생 과수의 하나로 꼽았고, 이런 자생 과수는 틈새시장용이어서 재배 면적과 생산량이 작고 변동이 크다고 적었다[20]. 국내 연구에 쓰인 열매는 지리산에서 9월 중순에 채집되었다[6].

머루는 포도 노균병(Plasmopara viticola)에 강해, 잎 원판 접종 5일 뒤 포자낭 수가 감수성 품종은 약 40,000개/mL였으나 머루 유래 계통을 포함한 저항성 유전형들은 약 2,000–5,700개/mL였다[19]. 일본 북부 여러 곳에서 채집한 머루 시료에서는 여러 RNA 바이러스의 혼합 감염과 새로운 바이러스 3종이 확인되었다[28]. 러시아 극동 야생 머루의 내생 세균·곰팡이 군집도 분석되어, 재배 포도의 생물적 방제 자원 후보로 제시되었다[27].

국내 재배 면적·생산량은 통계청 농작물생산조사와 특용작물 생산실적의 로컬 표에 머루 품목이 없어 확인하지 못함."""),
 ("processing", "가공과 이용", """식약처 목록에 오른 원료 형태는 건조머루·머루주스·산머루농축액·머루발효액·머루발효농축액·머루씨앗 등으로, 말리거나 즙·농축액·발효액으로 가공해 쓴다[1]. 머루 주스는 Ames 시험에서 헤테로고리아민의 돌연변이성을 억제했고, 그 성분으로 카프타르산이 분리되었다[9]. 주스는 생쥐 2단계 피부 발암 모델에서 먹이거나 바를 때 종양 발생을 줄였다[12].

동결건조 머루 1 kg에는 안토시아닌 179.98 mg이 들어 있었고, 빛과 리보플래빈이 만든 일중항산소에 의해 분해되었으며 다이글루코사이드가 모노글루코사이드보다 안정했다[4]. 마이크로파 추출 최적화 연구에서 총폴리페놀은 102.36 W, 에탄올 42.62%, 12.35분 조건에서 최대 415.74 mg/100 g이었다[31]. 야생 머루 레드와인의 망간 농도는 502–3627 μg/L였다[23]. 교잡종 포도와 머루를 섞은 즙을 효모로 25 ℃에서 10일 발효한 와인은 ACE 저해 활성 67.8%, 항산화 활성 76.7%를 보였고, 발효 뒤 기간을 30일로 늘리자 항산화 활성이 40.5%로 떨어졌다[22]. 알코올을 뺀 머루 와인 분말은 쥐 대동맥 고리를 0.1–1 mg/mL에서 내피 의존적으로 이완시켰다[25]. 착즙 찌꺼기의 페놀 분획은 충치균의 생물막 형성을 줄였고 최소억제농도는 7.50 mg/mL였다[24]. 식약처 건강기능식품 생산실적에서 머루 원료 항목은 확인하지 못함."""),
 ("genetics", "유전 정보", """2026년 연구는 육성 품종 'Morio Muskat'과 머루 × 'Gewürztraminer' 교잡 계통 COxGT2를 교배한 F1 496개체로 rhAmpSeq 표지 639개(19개 연관군, 1147.36 cM)의 유전지도를 만들었다[19]. 이 지도로 14번 염색체에서 노균병 저항성 QTL을 찾아 Rpv32라 이름 붙였고, 이 좌위는 3년 시험에서 표현형 변이의 최대 28.16%를 설명했다[19]. 5번 염색체에서는 잎털 밀도 QTL(변이의 24.23–25.36%)이 나왔지만 노균병 저항성과의 상관계수는 −0.08~−0.12로 약했다[19].

Rpv32 구간 안의 SSR 표지 3개가 표지 이용 선발에 바로 쓸 수 있게 제시되었고, 저항성 공여체의 유전체 해독은 진행 중이라고 했다[19]. 14번 염색체 윗팔에서는 기준 유전체(PN40024)와 표지 순서가 맞지 않아 재조합 억제나 구조 변이가 있을 것으로 보았다[19]. 일본 북부 머루 시료의 바이러스체 분석에서는 Vitis varicosavirus·Vitis emaravirus·Vitis crypticvirus로 잠정 명명된 새 바이러스 3종이 제안되었다[28]. 머루 자체의 전체 유전체 서열과 염색체 수는 확인하지 못함."""),
 ("safety", "안전성", """식약처 목록에서 머루는 열매와 씨앗만 사용가능한 식품원료이며, 잎·줄기·뿌리는 허용 부위에 없다[1]. 건강기능식품 고시형 원료가 아니어서 고시 섭취 시 주의사항은 확인하지 못함.

1995년 연구에서 머루 메탄올 추출물의 올리고스틸벤 가운데 ε-비니페린은 배양 간세포와 사염화탄소 간손상 생쥐에서 간 보호 작용을 보였으나, 암펠롭신 C와 비티신 A·cis-비티신 A 혼합물은 배양 간세포에서 강한 간독성을 보였다[16]. 이 추출물이 어느 부위에서 왔는지는 초록에 없어 확인하지 못함. 일본 방목 소 폐사 조사의 먹이 시험에서 머루를 먹인 소는 일시적 식욕부진과 저체온 외에 뚜렷한 전신 증상이 없었다[26]. 식용 부위가 아닌 줄기의 열수 추출물을 생쥐에 7일간 100–400 mg/kg 먹인 시험에서 사망이나 뚜렷한 이상은 없었지만, 저자들은 정상 생쥐 단독 투여군이 없어 반복 투여 독성시험이 더 필요하다고 적었다[15].

머루 안토시아닌의 항암 효과 보고는 대부분 세포 실험이며, 이 가운데 간암 세포·이종이식 생쥐 연구(Molecules 2020)는 2026년 10월 학술지가 철회했다[8]. 머루 알레르기와 잔류농약에 관한 국내 공공기관 정보는 확인하지 못함."""),
]
def c(name, ko, cls, role, part, content, act, src):
    return {"name": name, "name_ko": ko, "class": cls, "role": role, "part": part, "content_text": content, "activity_ko": act, "source": src}
compounds = [
 c("Malvidin 3,5-diglucoside", "말비딘-3,5-다이글루코사이드", "안토시아닌", "marker", "열매(동결건조)", "동결건조 머루의 안토시아닌(총 179.98 mg/kg) 가운데 가장 많음[4]; 다른 연구의 정제 안토시아닌 조성비에서는 2.21(시아니딘-3,5-다이글루코사이드 63)[5]", "일중항산소에서 모노글루코사이드보다 안정[4]", [4, 5]),
 c("Cyanidin 3,5-diglucoside", "시아니딘-3,5-다이글루코사이드", "안토시아닌", "bioactive", "열매", "정제 안토시아닌(AIM) 조성비 63으로 가장 큼[5]; 동결건조 머루에서도 검출[4]", "AIM 혼합물로 간암 세포 증식 억제(400 µg/mL, 48시간 75% 억제; 세포 실험)[5]", [5, 4]),
 c("Delphinidin 3,5-diglucoside", "델피니딘-3,5-다이글루코사이드", "안토시아닌", "bioactive", "열매", "정제 안토시아닌 조성비 27[5]", "AIM 혼합물로 대장암 세포 침윤·MMP-2/9 억제(세포 실험)[32]", [5, 32]),
 c("Cyanidin 3-glucoside", "시아니딘-3-글루코사이드", "안토시아닌", "bioactive", "열매", "동결건조 머루 안토시아닌 가운데 가장 적음[4]; 정제 안토시아닌 조성비 6.7[5]", "AIM 혼합물이 3T3-L1 지방세포 분화를 AMPK 활성화와 함께 억제(200 µg/mL에서 지질 약 60% 감소; 세포 실험)[7]", [4, 5, 7]),
 c("Caftaric acid", "카프타르산", "하이드록시신남산(타르타르산 에스터)", "bioactive", "열매 주스", "주스에서 항돌연변이 지표로 분리(함량은 초록에 없음)[9]", "헤테로고리아민의 돌연변이성 억제(Ames 시험), 주스는 생쥐 장기의 DNA 부가물 형성 감소[9]", [9]),
 c("Fertaric acid", "페르타르산", "하이드록시신남산(타르타르산 에스터)", "bioactive", "열매 주스", "주스에서 항염 성분으로 분리(함량은 초록에 없음)[10]", "LPS 자극 대식세포의 산화질소 생성 억제를 지표로 분리(세포 실험)[10]", [10]),
 c("2,6-Dimethoxy-1,4-benzoquinone", "2,6-다이메톡시-1,4-벤조퀴논(DBQ)", "벤조퀴논", "bioactive", "열매 주스", "주스에서 항염 성분으로 분리(함량은 초록에 없음)[10]", "생쥐 피부 발암 촉진 단계에서 바르면 종양 감소[10]; 먹이면 NNK 유발 폐 종양 감소(생쥐)[11]", [10, 11]),
 c("Pterostilbene", "프테로스틸벤", "스틸베노이드", "bioactive", "부위 확인 못함(초록에 없음)", "HPLC로 측정한 스틸베노이드 7종 합계 127.37±19.29 mg/100 g 건조중량 중 주성분[13]", "0.5–5.0 µM 전처리로 과산화수소가 막은 쥐 간세포 간극결합 통신 회복(세포 실험)[13]", [13]),
 c("Resveratrol", "레스베라트롤", "스틸베노이드", "bioactive", "줄기(식품 허용 부위 아님)", "줄기 열수 추출물 1.12 mg/g(HPLC, 품질 지표)[15]", "NPY·AgRP 프로모터 활성 억제 IC50 8.9·8.0 µM, 복강 100 mg/kg 1회로 24·48시간 섭식 20.0%·17.2% 감소(생쥐)[14]", [15, 14]),
 c("epsilon-Viniferin", "ε-비니페린", "올리고스틸벤(이량체)", "bioactive", "부위 확인 못함(메탄올 추출물)", "간세포 보호 활성으로 분리(함량은 초록에 없음)[16]", "배양 쥐 간세포와 사염화탄소 간손상 생쥐에서 간 보호[16]", [16]),
 c("Vitisin A", "비티신 A", "올리고스틸벤(사량체)", "bioactive", "부위 확인 못함", "cis-비티신 A와의 혼합물로 분리[16]; 스틸베노이드 7종 분석 대상('vitisin')[13]", "배양 간세포에서 강한 간독성(암펠롭신 C도 같음)[16]", [16, 13]),
 c("Rhapontigenin", "라폰티게닌", "스틸베노이드", "bioactive", "부위 확인 못함(초록에 없음)", "머루에서 분리(함량은 초록에 없음)[17]", "저산소 전립선암 세포에서 HIF-1α 축적·혈관신생 억제(세포 실험)[17]", [17]),
 c("Catechin", "(+)-카테킨", "플라반-3-올", "bioactive", "씨앗", "(+)-카테킨 0.32 mg/g(80% 메탄올)·0.38 mg/g(80% 아세톤), (−)-에피카테킨 0.29·0.36 mg/g, 합계 0.61·0.74 mg/g 생중량(HPLC)[2]", "유럽포도 씨앗(합계 0.98·1.07 mg/g)보다 적음; 씨앗 추출물의 항산화력과 관련[2]", [2]),
 c("Gallic acid", "갈산", "페놀산", "bioactive", "씨앗", "총 0.25 mg/g(80% 메탄올)·0.44 mg/g(80% 아세톤) 생중량, 대부분 에스터 결합형(0.18·0.35 mg/g)[2]", "씨앗 페놀산의 주성분; 유럽포도 씨앗(0.77·1.06 mg/g)보다 적음[2]", [2]),
 c("Caffeic acid", "카페산", "하이드록시신남산", "bioactive", "씨앗", "에스터 결합형 3.78 µg/g(80% 메탄올)·3.36 µg/g(80% 아세톤) 생중량[2]", "분석한 페놀산 가운데 유일하게 유럽포도 씨앗(2.73·2.35 µg/g)보다 많음[2]", [2]),
]
E = lambda **k: {**{f: "" for f in ["instrument","column","mobile_phase","gradient","flow","temp","detection","injection","sample_prep","standard","linearity","lod","loq","recovery"]}, **k}
prep = "분쇄 씨앗을 헥세인으로 속슬렛 탈지(50 °C, 6시간) → 80% 아세톤 또는 80% 메탄올(고체:용매 1:10), 질소 하 80 °C 15분 추출을 3회 → 여과·합침, 45 °C 감압 농축 후 동결건조"
assays = [
 {"role": "literature", "compound": "Catechin", "compound_ko": "(+)-카테킨·(−)-에피카테킨", "part": "씨앗(프랑스 종자 업체에서 구입한 머루 씨앗)",
  "content": "(+)-카테킨 0.32·0.38 mg/g, (−)-에피카테킨 0.29·0.36 mg/g 생중량(80% 메탄올·80% 아세톤 추출)[2]", "method": "HPLC-PDA",
  "conditions": E(instrument="Shimadzu HPLC(LC-10ADVP 펌프, SPD-M10AVP 광다이오드 배열 검출기, CTO-10ASVP 오븐, SCL-10AVP 제어기)",
    column="Phenomenex LUNA C 계열(원문 아래첨자 숫자 누락) 5 µm, 4.6 × 250 mm", mobile_phase="A: 물–아세토니트릴–아세트산(93:5:2, v/v/v); B: 물–아세토니트릴–아세트산(58:40:2, v/v/v)",
    gradient="B 0→100% 선형, 50분", flow="1 mL/min", temp="20 °C", detection="280 nm", injection="20 µL", sample_prep=prep, standard="(+)-카테킨, (−)-에피카테킨(시약 회사 표준품)"),
  "rationale": "씨앗 플라반-3-올 단량체이자 탄닌(프로안토시아니딘)의 구성 단위로, 머루와 유럽포도 씨앗을 구별·비교하는 지표로 정량됨; 전문 확인, 검량선·검출한계·정량한계·회수율은 본문에 없음[2].",
  "source": [2], "url": "https://doi.org/10.3390/molecules18033410", "source_kind": "paper"},
 {"role": "literature", "compound": "Gallic acid", "compound_ko": "갈산(p-쿠마르산·카페산·페룰산 동시 정량)", "part": "씨앗",
  "content": "총 갈산 0.25·0.44 mg/g 생중량(80% 메탄올·80% 아세톤 추출), 에스터 결합형 0.18·0.35 mg/g[2]", "method": "HPLC-PDA(등용매)",
  "conditions": E(instrument="Shimadzu HPLC(LC-10ADVP 펌프, SPD-M10AVP 광다이오드 배열 검출기, CTO-10ASVP 오븐, SCL-10AVP 제어기)",
    column="Phenomenex LUNA C 계열(원문 아래첨자 숫자 누락) 5 µm, 4.6 × 250 mm", mobile_phase="물–아세토니트릴–아세트산(88:10:2, v/v/v)", gradient="등용매",
    flow="1 mL/min", temp="20 °C", detection="280 nm, 320 nm", injection="20 µL",
    sample_prep=prep + "; 메탄올 추출물 200 mg/물 20 mL를 pH 2에서 다이에틸 에터로 5회 추출(유리형) → 2 M NaOH 4시간 질소 하 가수분해 후 에터 추출(에스터 결합형) → 6 M HCl 끓는 물 1시간 가수분해 후 에터 추출(배당체 결합형); 잔사를 메탄올 2 mL에 녹여 0.45 µm 나일론 필터 여과",
    standard="갈산, 카페산, p-쿠마르산, 페룰산(시약 회사 표준품)"),
  "rationale": "씨앗 추출물에서 가장 많은 페놀산이며 결합 형태(유리·에스터·배당체)별로 나눠 정량됨; 전문 확인, 검량선·검출한계·회수율은 본문에 없음(표 4의 단위 'mg/g'은 본문 값과 1000배 어긋나 본문 값을 따름)[2].",
  "source": [2], "url": "https://doi.org/10.3390/molecules18033410", "source_kind": "paper"},
 {"role": "literature", "compound": "Anthocyanins", "compound_ko": "안토시아닌 18종(새로 동정 9종 포함)", "part": "열매 껍질(한국 야생 머루)",
  "content": "18종 동정; 정량값은 초록에 없음[3]", "method": "HPLC-ESI-MS/MS(양이온 모드)",
  "conditions": E(column="C18 역상", mobile_phase="0.5% 포름산을 넣은 물–메탄올", gradient="메탄올 0→80%, 50분", detection="ESI-MS/MS 양이온 모드"),
  "rationale": "열매 색소이자 주요 항산화 성분으로, 열매 껍질에서 말비딘 헥소스·페오니딘 3-갈락토사이드 등 9종이 새로 동정됨; 전문 확인 못함, 조건은 초록 서술만 옮김[3].",
  "source": [3], "url": "https://doi.org/10.1002/jssc.200900748", "source_kind": "paper"},
 {"role": "literature", "compound": "Pterostilbene", "compound_ko": "프테로스틸벤(아스트린진·피세이드·비티신·라폰티신·레스베라트롤·라폰티게닌 동시 분석)", "part": "부위 확인 못함(초록에 없음)",
  "content": "스틸베노이드 7종 합계 127.37±19.29 mg/100 g 건조중량[13]", "method": "HPLC-DAD/UV",
  "conditions": E(),
  "rationale": "7종 스틸베노이드 가운데 주성분으로 활성 시험에 쓰임; 전문 확인 못함[13].",
  "source": [13], "url": "https://doi.org/10.1016/j.fct.2008.11.038", "source_kind": "paper"},
]
d = {"slug": "vitis-coignetiae", "name_ko": "머루", "name_en": "Crimson glory vine (crimson grapevine)",
 "scientific_name": "Vitis coignetiae Pulliat ex Planch.",
 "aliases": ["산머루", "산포도", "머루열매", "머루씨앗", "건조머루", "머루주스", "산머루농축액", "머루발효액", "머루발효농축액", "Crimson glory vine", "Crimson grapevine", "Vitis amurensis var. coignetii (Pulliat) Nakai", "meoru", "yamabudo"],
 "sections": [{"key": k, "title": t, "body": b} for k, t, b in sections],
 "compounds": compounds, "markers": [], "nutrients": [], "assays": assays,
 "production": [], "world": [], "gi": [], "orgs": [], "sources": S}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for k, t, b in sections: print(k, len(b))
