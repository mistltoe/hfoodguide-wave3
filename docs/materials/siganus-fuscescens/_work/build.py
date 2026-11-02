import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
A = "2026-11-02"
def pm(n, title, doi, pub, pmid=None):
    url = f"https://doi.org/{doi}" if doi else f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
    return {"n": n, "title": title, "url": url, "publisher": pub, "accessed": A}
sources = [
 {"n": 1, "title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — Siganus fuscescens 행(독가시치, 이명 따치, Mottled spinefoot·Dusky spinefoot, 수산물, 부위 '-', 사용가능, 사용 조건 없음; 같은 속 벌레무늬독가시치 Siganus vermiculatus는 별도 행 '사용불가'; docs/materials/siganus-fuscescens/card.json, data/raw/mfds_rawmtrl/I1020_20261013.json)", "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
 pm(2, "Year-round high arachidonic acid levels in herbivorous rabbit fish Siganus fuscescens tissues. Lipids 2006;41(5):473-89 (PubMed 초록)", "10.1007/s11745-006-5121-7", "Lipids, PMID 16933792"),
 pm(3, "High Arachidonic Acid Levels in the Tissues of Herbivorous Fish Species (Siganus fuscescens, Calotomus japonicus and Kyphosus bigibbus). Lipids 2017;52(4):363-373 (PubMed 초록)", "10.1007/s11745-017-4244-3", "Lipids, PMID 28332043"),
 pm(4, "Feeding containing the aerial part of Scutellaria baicalensis promotes the growth and nutritive value of rabbit fish (학명 표기는 도구 출력에서 빠짐; 같은 기록이 PubMed 'Siganus fuscescens' 검색에 걸림). Food Sci Nutr 2021 (PMC 전문 확인)", "10.1002/fsn3.2410", "Food Science & Nutrition, PMC8441375"),
 pm(5, "Occurrence of a stonefish toxin-like toxin in the venom of the rabbitfish Siganus fuscescens. Toxicon 2017 (PubMed 초록)", "10.1016/j.toxicon.2017.10.015", "Toxicon, PMID 29055787"),
 pm(6, "De Novo Assembly and Annotation of the Siganus fuscescens (Houttuyn, 1782) Genome: Marking a Pioneering Advance for the Siganidae Family. Mar Biotechnol 2024 (PubMed 초록)", "10.1007/s10126-024-10325-9", "Marine Biotechnology, PMID 38850360"),
 pm(7, "Complete mitochondrial genome of the rabbitfish Siganus fuscescens (Perciformes, Siganidae). DNA Seq 2007 (PubMed 초록)", "10.1080/10425170701248525", "DNA Sequence, PMID 17541835"),
 pm(8, "Two spinefoot colour morphs: mottled spinefoot Siganus fuscescens and white-spotted spinefoot Siganus canaliculatus are synonyms. J Fish Biol 2011 (PubMed 초록)", "10.1111/j.1095-8649.2011.03104.x", "Journal of Fish Biology, PMID 22026611"),
 pm(9, "Phylogenetic relationships and natural hybridization in rabbitfishes (Teleostei: Siganidae) inferred from mitochondrial and nuclear DNA analyses. Mol Phylogenet Evol 2007;45(1):69-80 (PubMed 초록)", "10.1016/j.ympev.2007.04.018", "Molecular Phylogenetics and Evolution, PMID 17590356"),
 pm(10, "Cryptic genetic diversity in the mottled rabbitfish Siganus fuscescens with mitochondrial introgression at a contact zone in the South China Sea. PLoS One 2018 (PubMed 초록)", "10.1371/journal.pone.0193220", "PLoS One, PMC5821360"),
 pm(11, "Phylogeography of the mottled spinefoot Siganus fuscescens: Pleistocene divergence and limited genetic connectivity across the Philippine archipelago. Mol Ecol 2010 (PubMed 초록)", "10.1111/j.1365-294X.2010.04803.x", "Molecular Ecology, PMID 20875063"),
 pm(12, "Maximization of fitness by phenological and phenotypic plasticity in range expanding rabbitfishes (Siganidae). J Anim Ecol 2022 (PMC 전문 확인; S. fuscescens와 S. canaliculatus 자료를 동의어로 합쳐 분석)", "10.1111/1365-2656.13739", "Journal of Animal Ecology, PMC9546425"),
 pm(13, "Climate-assisted persistence of tropical fish vagrants in temperate marine ecosystems. Commun Biol 2021 (PubMed 초록)", "10.1038/s42003-021-02733-7", "Communications Biology, PMC8553944"),
 pm(14, "Feeding preferences of range-shifting and native herbivorous fishes in temperate ecosystems. Mar Environ Res 2021 (PubMed 초록)", "10.1016/j.marenvres.2021.105508", "Marine Environmental Research, PMID 34710739"),
 pm(15, "Overwintering tropical herbivores accelerate detritus production on temperate reefs. Proc Biol Sci 2019 (PubMed 초록)", "10.1098/rspb.2019.2046", "Proceedings of the Royal Society B, PMC6892040"),
 pm(16, "Identification of seagrasses in the gut of a marine herbivorous fish using DNA barcoding and visual inspection techniques. J Fish Biol 2011 (PubMed 초록)", "10.1111/j.1095-8649.2011.02999.x", "Journal of Fish Biology, PMID 21722114"),
 pm(17, "Allometric Growth of Feeding and Locomotor Structures During Early Ontogeny of Rabbitfish (Siganus fuscescens). Animals 2026;16(5):777 (PMC 전문 확인)", "10.3390/ani16050777", "Animals (MDPI), PMC12984535"),
 pm(18, "Comparative assessment of thermal tolerance in rabbitfish (Siganus fuscescens) following acclimation to two different temperatures. Fish Physiol Biochem 2026 (PubMed 초록)", "10.1007/s10695-026-01816-8", "Fish Physiology and Biochemistry, PMID 42867556"),
 pm(19, "Seaweed dietary supplements enhance the innate immune response of the mottled rabbitfish, Siganus fuscescens. Fish Shellfish Immunol 2021 (PubMed 초록)", "10.1016/j.fsi.2021.03.018", "Fish & Shellfish Immunology, PMID 33823246"),
 pm(20, "Biotransformation of inorganic arsenic in a marine herbivorous fish Siganus fuscescens after dietborne exposure. Chemosphere 2016 (PubMed 초록)", "10.1016/j.chemosphere.2015.12.121", "Chemosphere, PMID 26766368"),
 pm(21, "Comparison of Bioavailability and Biotransformation of Inorganic and Organic Arsenic to Two Marine Fish. Environ Sci Technol 2016 (PubMed 초록)", "10.1021/acs.est.5b06307", "Environmental Science & Technology, PMID 26835720"),
 pm(22, "Are there risks induced by novel and legacy poly- and perfluoroalkyl substances in coastal aquaculture base in South China? Sci Total Environ 2021 (PubMed 초록)", "10.1016/j.scitotenv.2021.146539", "Science of the Total Environment, PMID 34030277"),
 pm(23, "Residues of fluoroquinolones in marine aquaculture environment of the Pearl River Delta, South China. Environ Geochem Health 2011 (PubMed 초록)", "10.1007/s10653-011-9420-4", "Environmental Geochemistry and Health, PMID 21881861"),
 pm(24, "[Anisakis simplex larvae: infection status in marine fishes for sale in Shantou]. Zhongguo Ji Sheng Chong Xue Yu Ji Sheng Chong Bing Za Zhi 2014 (PubMed 초록)", None, "PubMed, PMID 25223058", pmid="25223058"),
 pm(25, "Morphological and molecular identification of Hysterothylacium longilabrum sp. nov. (Nematoda: Anisakidae) and larvae of different stages from marine fishes in the South China Sea. Parasitol Res 2012 (PubMed 초록)", "10.1007/s00436-012-2897-7", "Parasitology Research, PMID 22461007"),
 pm(26, "Microplastics in marine sediments and rabbitfish (Siganus fuscescens) from selected coastal areas of Negros Oriental, Philippines. Mar Pollut Bull 2019 (PubMed 초록)", "10.1016/j.marpolbul.2019.110685", "Marine Pollution Bulletin, PMID 31706727"),
 pm(27, "Development of novel polymorphic microsatellite markers in Siganus fuscescens. Genet Mol Res 2016 (PubMed 초록)", "10.4238/gmr.15037515", "Genetics and Molecular Research, PMID 27525874"),
 pm(28, "The Microbiome of the Gastrointestinal Tract of a Range-Shifting Marine Herbivorous Fish. Front Microbiol 2018 (PubMed 초록)", "10.3389/fmicb.2018.02000", "Frontiers in Microbiology, PMC6121097"),
 {"n": 29, "title": "Age and growth of rabbit fish, Siganus fuscescens in the coast of Jeju island, Korea. 한국어업기술학회지 2014;50(2):169-175 — 원문 사이트가 이 환경에서 막혀 WebSearch 결과 요약으로만 확인(원문 미열람)", "url": "https://koreascience.kr/article/JAKO201417048539550.page", "publisher": "한국수산해양기술학회(WebSearch 요약)", "accessed": A},
 {"n": 30, "title": "제주 연안 독가시치(Siganus fuscescens)의 생식생태. 수산해양기술연구 2019 — 원문 사이트가 이 환경에서 막혀 WebSearch 결과 요약으로만 확인(원문 미열람)", "url": "https://koreascience.or.kr/article/JAKO201907750244088.page", "publisher": "한국수산해양기술학회(WebSearch 요약)", "accessed": A},
 pm(31, "Radiocesium uptake, trophic transfer, and exposure in three estuarine fish with contrasting feeding habits. Chemosphere 2016 (PubMed 초록)", "10.1016/j.chemosphere.2016.08.066", "Chemosphere, PMID 27565318"),
 pm(32, "[Morphology of the venom-apparatus of Japanese fish. XI. The venom-apparatus of the Siganus fuscescens (Houttuyn)]. Yokohama Med Bull 1955;6(2):115-22 (PubMed 서지만, 초록 없음)", None, "PubMed, PMID 13257271", pmid="13257271"),
 pm(33, "Characterization of a macrophagic-like cell line derived from rabbit fish (Siganus fuscescens). Fish Shellfish Immunol Rep 2021 (PubMed 초록)", "10.1016/j.fsirep.2021.100036", "Fish and Shellfish Immunology Reports, PMC9680100"),
]

S = {}
S["overview"] = ("독가시치(Siganus fuscescens)는 독가시치과(Siganidae) Siganus속의 바닷물고기로, 식약처 「식품원료 목록」에 '독가시치'(이명 '따치', 영문 Mottled spinefoot·Dusky spinefoot)라는 원료명의 수산물로 올라 있다[1]. "
 "이 목록에서 상태는 '사용가능'이고, 사용 부위 칸은 원자료대로 '-'로 적혀 있으며 별도의 사용 조건은 없다[1]. "
 "건강기능식품 고시형 원료의 원재료 목록에는 없어 식약처가 정한 지표성분도 없다[1].\n\n"
 "해조류와 해초를 주로 먹는 초식성 어종이며, 등지느러미 가시에 독이 있어 사람이 찔리는 사고가 잦은 독어로 알려져 있다[5, 16]. "
 "일본 연구에서는 근육과 내장 지질에 아라키돈산(ARA)이 일반 해산어보다 많고 DHA도 비교적 많아 영양 지질 공급원으로 쓸 가능성이 제안되었다[2]. "
 "중국 남부·호주·인도네시아에서 양식되거나 먹는 어종으로 소개되며[4], 필리핀에서도 상업적으로 중요한 식용 어종으로 다루어졌다[26]. "
 "국내 공공기관의 독가시치 식품성분표 값은 이번 조사에서 확인하지 못함.")
S["history"] = ("독가시치의 독 기관은 1955년 일본 어류 독 기관 형태 연구 연재에서 이미 따로 다루어졌다[32]. "
 "일본 연안에서 가장 흔한 독가시치과 어종으로 소개되며, 사람에게 찔림 사고를 자주 일으키는 독어로 알려져 있다[5].\n\n"
 "최근에는 온난화로 서식 범위가 넓어지는 어종으로 주목받는다[12]. "
 "서호주에서는 2011년 해양 열파 때 레이우인 해류가 강해지며 온대 해역으로 퍼졌고, 일본에서는 쿠로시오 해류의 점진적 온난화와 함께 북쪽으로 분포가 넓어졌다[12]. "
 "서호주 온대 암초에서 겨울을 나며 다시마류와 해조류를 먹어, 해조 숲의 해조가 찌꺼기(쇄설물)로 바뀌는 속도를 약 5배 높였다는 보고가 있다[15]. "
 "열대 계통 개체가 온대로 옮겨 가도 유전적 차이가 거의 없었고 해조류를 포함한 다양한 먹이를 먹어 2100년까지 분포가 더 넓어질 수 있다고 예측되었다[13].\n\n"
 "국내 제주 연안에서는 2012년 2–12월 매달 채집한 표본으로 나이와 성장을 조사한 연구가 있다고 검색 결과 요약에 나오나, 원문은 열지 못해 세부 수치는 확인하지 못함[29].")
S["biology"] = ("독가시치는 초식성 어종으로, 호주 모턴만의 어린 개체 위장에서는 해초 4종과 조류 1종이 육안으로 확인되었다[16]. "
 "서호주 실험에서는 어린 다시마보다 잔디처럼 깔린 소형 해조(turf)를 더 즐겨 먹었다[14]. "
 "서호주 2,000 km에 걸친 조사에서 후장 미생물 군집은 개체군마다 달랐지만 20개 OTU가 모든 시료에 공통으로 나타나 '핵심 미생물군'을 이루었다[28].\n\n"
 "S. canaliculatus와 합쳐 분석한 메타분석에서 성숙 최소 체장은 열대 120 ± 14 mm, 아열대 150 ± 10 mm, 온대 199 ± 31 mm로 추운 곳일수록 컸다[12]. "
 "같은 분석에서 최대 수명은 열대 3살, 아열대 8살, 온대 13살로 늘었고, 산란기는 열대에서 최대 7개월, 온대에서 2개월이었다[12]. "
 "23 ℃와 29 ℃에 순치한 개체의 반수 치사 상한 수온(UILT)은 각각 33.4 ℃, 33.6 ℃였다[18]. "
 "해조류나 이매패를 먹였을 때 먹이 속 방사성 세슘(137Cs) 동화율은 51–55%로 육식성 어종 두 종(70–79%)보다 낮았다[31].\n\n"
 "제주 연안 연구는 생식소 지수가 7–8월에 높고 주 산란기가 7–8월이며 연 1회 산란한다고 보고했다고 검색 결과 요약에 나오나, 원문은 확인하지 못함[30].")
S["related_species"] = ("식약처 「식품원료 목록」에는 같은 속의 벌레무늬독가시치(Siganus vermiculatus)가 별도 행으로 있고, 그 상태는 '사용불가'여서 독가시치와 지위가 다르다[1]. "
 "이 문서는 벌레무늬독가시치와 다른 Siganus 종의 자료를 섞지 않았다[1].\n\n"
 "독가시치(mottled spinefoot)와 S. canaliculatus(영문 white-spotted spinefoot)는 색과 형태가 조금 다를 뿐이어서, AFLP 분석에서 형태가 아니라 지역에 따라 묶여 서로 교배하는 색깔 형태로 보아야 한다는 주장이 있다[8]. "
 "미토콘드리아·핵 DNA 분석에서도 두 종의 개체가 유전적 모자이크를 이루어 한 생물학적 종 안의 색깔 형태로 제안되었다[9]. "
 "반대로 남중국해 북부에서는 독가시치 안에 유전·형태가 다른 은둔종 두 무리가 있다는 결과가 나와, 미토콘드리아 표지만으로 종을 가리지 말라고 권고되었다[10].\n\n"
 "영어로는 rabbitfish·mottled spinefoot·dusky spinefoot 등으로 부르는데, 'rabbitfish'는 독가시치과 전체를 가리키는 말이기도 해서 학명이 없는 자료는 이 종의 자료로 쓰지 않았다[12]. "
 "'독가시치'라는 국문명의 유래를 적은 공식 자료는 확인하지 못함.")
S["cultivation"] = ("독가시치는 초식성이고 비교적 빨리 자라며 소비자 선호가 좋아 양식 대상으로 관심을 받지만, 초기 자어 단계의 종묘 생산이 여전히 어렵다[17]. "
 "한 연구 시설에서는 어미 14마리에서 얻은 수정란 8,000개를 1톤 원형 수조 5개에 나누어 부화 후 2–30일 동안 로티퍼를 1 mL당 10–30마리 먹이며 길렀다[17]. "
 "이 연구는 몸길이 약 5 mm, 7–9 mm, 17–19 mm에서 성장 양상이 바뀌는 세 단계를 찾아 먹이 공급과 조명 관리를 단계에 맞추라고 제안했다[17].\n\n"
 "새로운 양식 대상종으로서 사료에 해조류 11종을 3%씩 넣은 실험에서는 홍조류 Asparagopsis taxiformis와 갈조류 Dictyota intermedia가 선천 면역 지표를 가장 크게 높였다[19]. "
 "중국 선전 다펑의 해상 양식장 실험에서는 황금(Scutellaria baicalensis) 지상부 추출물을 사료에 1% 넣자 4주 뒤 몸길이와 체중이 대조군보다 늘었다[4].\n\n"
 "서호주에서는 독가시치가 주로 겨냥되지 않고 부수어획으로 잡히며, FAO 통계는 독가시치과 단위로만 어획량을 집계해 종별 어획량을 알기 어렵다[12]. "
 "국내 독가시치의 연도별 어획·양식 생산 통계는 확인하지 못함.")
S["processing"] = ("독가시치 근육 지질의 주요 지방산은 16:0, 18:0, 16:1n-7, 18:1n-9, 아라키돈산(ARA), DHA였고, 조지방 함량은 겨울에 높고 여름에 낮았다[2]. "
 "근육 총지질 중 ARA는 5월 말–8월에 4.6–13.1%, 그 밖의 계절에 4.3–9.5%로 한 해 내내 비교적 높았다[2]. "
 "근육·간·내장 모두 중성지질보다 극성지질(인지질)에 ARA가 더 많았다[2].\n\n"
 "2017년 일본 연구는 독가시치를 포함한 초식성 어류 세 종의 주요 지질이 트라이아실글리세롤·포스파티딜에탄올아민·포스파티딜콜린이라고 보고했다[3]. "
 "이 연구는 위 내용물에서도 ARA가 주된 고도불포화지방산이어서 높은 ARA가 먹이에서 온다고 보았다[3].\n\n"
 "양식 독가시치 등살의 아미노산을 LC-MS/MS로 잰 연구에서 대조군은 류신이 20.02 ± 0.05 mg/100 g으로 가장 많았고 알라닌이 13.92 ± 0.11 mg/100 g으로 뒤를 이었다[4]. "
 "가공·저장 방법(건조·염장·냉장 등)을 이 종에서 따로 다룬 연구는 이번 조사에서 확인하지 못함.")
S["genetics"] = ("2024년 처음 발표된 독가시치 초안 유전체는 독가시치과 첫 전장 유전체로, 반수체 크기 498 Mb에 추정 크기의 99.6%를 담았다[6]. "
 "이 유전체는 콘티그 164개(N50 7.2 Mb), GC 함량 42.9%, BUSCO 완성도 99.5%였고, 반복 서열은 17.43%, 주석된 유전자는 28,351개였다[6]. "
 "연구진은 장쇄 고도불포화지방산 합성과 독 분비에 관련된 유전체 특성도 살폈다[6].\n\n"
 "미토콘드리아 전장 유전체는 16,491 bp로 단백질 유전자 13개, rRNA 2개, tRNA 22개를 가졌다[7]. "
 "필리핀 군도의 미토콘드리아 조절 영역 분석에서는 플라이스토세에 갈라진 세 계통이 나왔고, 그 가운데 하나는 S. canaliculatus로 판정되었다[11]. "
 "남중국해 북부 373개체 분석에서는 핵 유전자형 무리 두 개 사이의 유전자 흐름이 거의 없었고(FST = 0.241), 20.5%의 개체에서 미토콘드리아 유입 흔적이 보였다[10]. "
 "자연산 30개체에서 개발한 미세부수체 10개는 좌위당 대립유전자 3–5개, 관찰 이형접합도 0.3333–0.8462였다[27]. "
 "머리콩팥에서 만든 대식세포 유사 세포주(RFM)는 50대 넘게 계대되었고 20% 혈청, 28 ℃에서 가장 잘 자랐다[33].")
S["safety"] = ("식약처 「식품원료 목록」에서 독가시치는 별도 조건 없이 '사용가능' 원료이며, 건강기능식품 고시형 원료가 아니어서 고시 섭취 시 주의사항은 없다[1]. "
 "독가시치를 따로 다룬 국내 공공기관의 알레르기·잔류물질·식중독 정보는 이번 조사에서 확인하지 못함.\n\n"
 "독은 등지느러미 가시에 있고, 가시 추출물은 쑤기미류 독소와 닮은 단백질 독소(α 703, β 699 아미노산)를 가지며 생쥐 치사·용혈·부종·통증 활성을 보였다[5]. "
 "이는 손질 중 가시에 찔리는 자상의 문제이며, 이 종의 살을 먹어서 생기는 시가테라 독소 검출 보고는 PubMed에서 확인하지 못함.\n\n"
 "중국 산터우 시장 조사에서 독가시치의 아니사키스 유충 감염 강도는 마리당 2마리 미만으로 낮은 편이었고, 52종 전체에서 유충은 근육에서 나오지 않았다[24]. "
 "남중국해 독가시치의 장과 위에서는 회충류 Hysterothylacium longilabrum이 새로 기재되었다[25]. "
 "중국 김 양식 거점의 독가시치 과불화화합물(PFAS)은 7.17–25.43 ng/g(건중량)이었고, 김과 독가시치를 통한 주민 섭취 노출량은 제시된 허용 일일 섭취량보다 훨씬 낮았다[22]. "
 "사료로 무기비소를 먹인 실험에서 근육 비소의 79.0–95.2%가 독성이 낮은 아르세노베타인으로 바뀌었다[20]. "
 "중국 주강 삼각주 양식장 어류 9종 가운데 하이링섬 독가시치 간의 노르플록사신이 254.58 ng/g(습중량)으로 가장 높았으나, 연구진은 근육·간의 플루오로퀴놀론 잔류가 건강 위험 수준은 아니라고 보았다[23].")

compounds = [
 {"name": "Arachidonic acid", "name_ko": "아라키돈산(ARA, 20:4n-6)", "class": "n-6 지방산", "role": "nutrient", "part": "근육·간·내장", "content_text": "근육 총지질 중 4.6–13.1%(5월 말–8월), 4.3–9.5%(그 밖의 계절); 간 4.5–9.1% / 3.6–8.4%; 기타 내장 2.0–10.7%", "activity_ko": "일반 해산어보다 많고 먹이(해조류)에서 유래하는 것으로 보았다[2, 3]", "source": [2, 3]},
 {"name": "Docosahexaenoic acid", "name_ko": "DHA(22:6n-3)", "class": "n-3 지방산", "role": "nutrient", "part": "근육", "content_text": "근육 총지질의 주요 지방산(개별 수치는 초록에 없음); 1% 황금 지상부 추출물 사료군에서 대조군보다 2배 넘게 증가", "activity_ko": "ARA와 함께 비교적 많아 영양 지질 공급원으로 제안되었다[2, 4]", "source": [2, 4]},
 {"name": "Eicosapentaenoic acid", "name_ko": "EPA(20:5n-3)", "class": "n-3 지방산", "role": "nutrient", "part": "근육·내장", "content_text": "주요 지방산의 하나(초식성 3종 연구, 독가시치 개별 수치는 초록에서 확인하지 못함)", "activity_ko": "인지질에 고도불포화지방산이 더 많았다[3]", "source": [3]},
 {"name": "Docosapentaenoic acid", "name_ko": "DPA(22:5n-3)", "class": "n-3 지방산", "role": "nutrient", "part": "근육·내장", "content_text": "주요 지방산의 하나(초식성 3종 연구, 독가시치 개별 수치는 초록에서 확인하지 못함)", "activity_ko": "고도불포화지방산 가운데 하나로 보고되었다[3]", "source": [3]},
 {"name": "Palmitic acid", "name_ko": "팔미트산(16:0)", "class": "포화지방산", "role": "nutrient", "part": "근육·간·내장", "content_text": "총지질의 주요 지방산(수치는 초록에 없음)", "activity_ko": "독가시치 지질의 주된 포화지방산으로 보고되었다[2]", "source": [2]},
 {"name": "Stearic acid", "name_ko": "스테아르산(18:0)", "class": "포화지방산", "role": "nutrient", "part": "근육·간·내장", "content_text": "총지질의 주요 지방산(수치는 초록에 없음)", "activity_ko": "주요 지방산의 하나로 보고되었다[2]", "source": [2]},
 {"name": "Palmitoleic acid", "name_ko": "팔미톨레산(16:1n-7)", "class": "단일불포화지방산", "role": "nutrient", "part": "근육·간·내장", "content_text": "총지질의 주요 지방산(수치는 초록에 없음)", "activity_ko": "주요 단일불포화지방산의 하나로 보고되었다[2]", "source": [2]},
 {"name": "Oleic acid", "name_ko": "올레산(18:1n-9)", "class": "단일불포화지방산", "role": "nutrient", "part": "근육·간·내장", "content_text": "총지질의 주요 지방산(수치는 초록에 없음)", "activity_ko": "주요 단일불포화지방산의 하나로 보고되었다[2]", "source": [2]},
 {"name": "Leucine", "name_ko": "류신", "class": "아미노산", "role": "nutrient", "part": "등살(양식, 대조 사료군)", "content_text": "20.02 ± 0.05 mg/100 g", "activity_ko": "측정한 12종 아미노산 중 가장 많았고, 황금 지상부 추출물 사료군에서는 약 40% 줄었다[4]", "source": [4]},
 {"name": "Alanine", "name_ko": "알라닌", "class": "아미노산", "role": "nutrient", "part": "등살(양식, 대조 사료군)", "content_text": "13.92 ± 0.11 mg/100 g", "activity_ko": "류신 다음으로 많은 아미노산이었다[4]", "source": [4]},
 {"name": "Glutamic acid", "name_ko": "글루탐산", "class": "아미노산", "role": "nutrient", "part": "등살(양식, 대조 사료군)", "content_text": "약 2.4 mg/100 g", "activity_ko": "감칠맛 관련 아미노산으로, 사료군 사이에 거의 변하지 않았다[4]", "source": [4]},
 {"name": "Threonine", "name_ko": "트레오닌", "class": "아미노산", "role": "nutrient", "part": "등살(양식)", "content_text": "1% 황금 지상부 추출물 사료군에서 50% 넘게 증가(절대 수치는 본문에서 확인하지 못함)", "activity_ko": "단맛 관련 아미노산으로 설명되었다[4]", "source": [4]},
 {"name": "Arsenobetaine", "name_ko": "아르세노베타인", "class": "유기비소 화합물", "role": "bioactive", "part": "근육·간(무기비소 사료 노출 실험)", "content_text": "근육 비소의 79.0–95.2%, 간 63.3–91.3%", "activity_ko": "독성이 높은 무기비소를 독성이 낮은 형태로 바꾼 결과물이다[20, 21]", "source": [20, 21]},
 {"name": "Stonefish toxin-like toxin", "name_ko": "쑤기미류 독소 유사 단백질 독소", "class": "단백질 독소", "role": "bioactive", "part": "등지느러미 가시", "content_text": "α 소단위 703 아미노산, β 소단위 699 아미노산(cDNA 클로닝으로 1차 구조 규명)", "activity_ko": "가시 추출물이 생쥐 치사·용혈·부종·통증 활성을 보였다(가시 자상 관련, 섭취 독성 아님)[5]", "source": [5]},
]

lc_cond = lambda col, mp, grad, flow, temp, det: {"instrument": "LC-MS(질량분석기 PerkinElmer Qsight 220, MRM 양이온 모드)" if "MRM" in det else "LC-MS(전자분무 이온화, 양·음이온 모드)", "column": col, "mobile_phase": mp, "gradient": grad, "flow": flow, "temp": temp, "detection": det, "injection": "", "sample_prep": "등살 100 mg + 다이클로로메테인:메탄올(2:1, v/v) 1 mL 균질 → 물 0.4 mL 넣고 30초 교반·10분 정치 → 850×g 4 °C 10분 원심 → 위층(약 0.4 mL)은 아미노산, 아래층(약 0.4 mL)은 지방산 분석용으로 농축", "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""}
assays = [
 {"role": "literature", "compound": "Amino acids (leucine etc.)", "compound_ko": "아미노산(류신 등 12종)", "part": "등살(양식)", "content": "대조군 류신 20.02 ± 0.05 mg/100 g, 알라닌 13.92 ± 0.11 mg/100 g, 글루탐산 약 2.4 mg/100 g[4]", "method": "UPLC-MS/MS(MRM)",
  "conditions": lc_cond("Waters ACQUITY UPLC HSS T3, 2.1 × 150 mm, 1.8 μm", "A: 10 mM 폼산암모늄·0.1% 폼산 수용액, B: 아세토나이트릴", "0–2분 95% A; 2–4분 95→72% A; 4–20분 72% A; 20–22분 72→60% A; 22–35분 60% A; 35–45분 60→5% A; 45–50분 5% A; 50–50.1분 5→95% A; 50.1–55분 95% A", "", "", "MRM, 양이온(+) 전자분무 5500 V, 분무 가스 180"),
  "rationale": "근육 아미노산은 맛(단맛·쓴맛·감칠맛)과 영양을 함께 보여 주는 지표로 쓰였다[4]. 전문(Methods) 확인 — 유속·칼럼 온도·표준품·검출·정량한계·회수율은 본문에 없음[4].", "source": [4], "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8441375/", "source_kind": "paper"},
 {"role": "literature", "compound": "Docosahexaenoic acid", "compound_ko": "DHA 등 지방산·인지질·중성지질", "part": "등살(양식)", "content": "1% 황금 지상부 추출물 사료군에서 DHA 2배 넘게 증가, 트라이글리세라이드 4종 3배 넘게 감소(상대량)[4]", "method": "UPLC-MS(ESI, 양·음이온)",
  "conditions": lc_cond("Waters Acquity BEH C18, 2.1 × 100 mm, 1.7 μm", "A: 물:아세토나이트릴(40:60, v/v)+5 mM 폼산암모늄·0.1% 폼산, B: 아이소프로판올:아세토나이트릴(90:10, v/v)+5 mM 폼산암모늄·0.1% 폼산", "0–13분 70→20% A; 13–20분 20→10% A; 20–21분 10→0% A; 21–26분 0% A; 26–27분 0→70% A; 27–30분 70% A", "0.2 mL/min", "55 °C", "전자분무 양·음이온, 주사 범위 m/z 150–1,050"),
  "rationale": "지방산 조성은 이 종의 영양 가치(n-3 지방산)를 보여 주는 지표로 쓰였다[4]. 전문 확인 — 절대 함량이 아닌 상대량 비교이며 표준품·검출·정량한계·회수율은 본문에 없음[4].", "source": [4], "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8441375/", "source_kind": "paper"},
 {"role": "literature", "compound": "Arachidonic acid", "compound_ko": "아라키돈산(ARA)", "part": "근육·간·내장", "content": "근육 총지질 중 4.6–13.1%(5월 말–8월), 4.3–9.5%(그 밖의 계절)[2]", "method": "가스크로마토그래피(GC, GC-MS)",
  "conditions": {"instrument": "", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "", "injection": "", "sample_prep": "", "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "독가시치 지질의 특징이 일반 해산어보다 높은 ARA이고 연중 높게 유지되어 이 종을 대표하는 지방산으로 쓰였다[2, 3]. 전문 확인 못함(초록과 MeSH의 GC-MS 표기만 확인)[2].", "source": [2, 3], "url": "https://doi.org/10.1007/s11745-006-5121-7", "source_kind": "paper"},
]

d = {"slug": "siganus-fuscescens", "name_ko": "독가시치", "name_en": "Mottled spinefoot",
 "scientific_name": "Siganus fuscescens (Houttuyn, 1782)",
 "aliases": ["독가시치", "따치", "Mottled spinefoot", "Dusky spinefoot", "Rabbitfish", "Black rabbitfish"],
 "sections": [], "compounds": compounds, "markers": [], "assays": assays, "nutrients": [], "production": [], "world": [], "gi": [], "orgs": [], "sources": sources}
TITLES = {"overview": "한눈에 보기", "history": "이용·연구 역사", "biology": "어종·생태", "related_species": "관련 종·이름", "cultivation": "어획·양식", "processing": "성분·가공", "genetics": "유전 정보", "safety": "안전성"}
for k in TITLES:
    d["sections"].append({"key": k, "title": TITLES[k], "body": S[k]})
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in d["sections"]: print(s["key"], len(s["body"]))
