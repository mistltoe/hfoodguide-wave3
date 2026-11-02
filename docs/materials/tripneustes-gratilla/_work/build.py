import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
PM = "https://pubmed.ncbi.nlm.nih.gov/%s/"
PMC = "https://pmc.ncbi.nlm.nih.gov/articles/%s/"
A = "2026-11-02"
I1020 = "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020"

src = [
 ("식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 흰수염성게(Tripneustes gratilla) 1행", I1020, "식품의약품안전처", "2026-10-13"),
 ("식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 다른 성게류 행(보라성게·새치성게·흰꼭지성게·분지성게·말똥성게·Heliocidaris erythrogramma·성게·성게알·성게살·성게추출물)과 소브산·소브산칼륨·소브산칼슘 사용 기준 행(성게젓)", I1020, "식품의약품안전처 (로컬 원자료 I1020_20261013.json)", "2026-10-13"),
 ("Dinh TK et al. Component and Content of Lipid Classes and Phospholipid Molecular Species of Eggs and Body of the Vietnamese Sea Urchin. Molecules 2023;28(9):3721", PMC % "PMC10180406", "Molecules (PMC 전문)", A),
 ("Bilan MI et al. Chemical Structure of a Branched α-d-Glucan from the Eggs of Sea Urchin. Int J Mol Sci 2025;26(21):10326", PMC % "PMC12609645", "International Journal of Molecular Sciences (PMC 전문)", A),
 ("Darius HT et al. Toxicological Investigations on the Sea Urchin Tripneustes gratilla from Anaho Bay (Nuku Hiva, French Polynesia): Evidence for the Presence of Pacific Ciguatoxins. Mar Drugs 2018;16(4):122", PMC % "PMC5923409", "Marine Drugs (PMC 전문)", A),
 ("Aljohani AKB et al. Antidiabetic Potential of Sea Urchin Nanosuspension Based on In Vitro Enzyme Inhibition, In Vivo Evaluation, and Chemical Profiling Approaches. Curr Issues Mol Biol 2025;48(1):8", PMC % "PMC12839668", "Current Issues in Molecular Biology (PMC 전문)", A),
 ("Mebs D. A toxin from the sea urchin Tripneustes gratilla. Toxicon 1984;22(2):306-307", PM % "6729846", "Toxicon (PubMed 초록)", A),
 ("Nakagawa H et al. Biochemical and physiological properties of pedicellarial lectins from the toxopneustid sea urchins. J Nat Toxins 1999;8(3):297-308", PM % "10591033", "Journal of Natural Toxins (PubMed 초록)", A),
 ("Satoh F et al. Fishing for bioactive substances from scorpionfish and some sea urchins. J Nat Toxins 2002;11(4):297-304", PM % "12503872", "Journal of Natural Toxins (PubMed 초록)", A),
 ("Yoshino K et al. Identification of a novel amino acid, o-bromo-L-phenylalanine, in egg-associated peptides that activate spermatozoa. Biochemistry 1991;30(25):6203-6209", PM % "2059627", "Biochemistry (PubMed 초록)", A),
 ("Vidyalakshmi D et al. Heavy metal accumulation analysis using bivalve, sponge, sea urchin, and gastropod species as bioindicators. Mar Pollut Bull 2024;202:116374", PM % "38663344", "Marine Pollution Bulletin (PubMed 초록)", A),
 ("Hédouin L et al. Ecotoxicological approach for assessing the contamination of a Hawaiian coral reef ecosystem (Honolua Bay, Maui) by metals and a metalloid. Mar Environ Res 2011;71(3):149-161", PM % "21277629", "Marine Environmental Research (PubMed 초록)", A),
 ("Lessios HA et al. Phylogeography of the pantropical sea urchin Tripneustes: contrasting patterns of population structure between oceans. Evolution 2003;57(9):2026-2036", PM % "14575324", "Evolution (PubMed 초록)", A),
 ("Zigler KS, Lessios HA. Evolution of bindin in the pantropical sea urchin Tripneustes: comparisons to bindin of other genera. Mol Biol Evol 2003;20(2):220-231", PM % "12598689", "Molecular Biology and Evolution (PubMed 초록)", A),
 ("Bronstein O et al. Do genes lie? Mitochondrial capture masks the Red Sea collector urchin's true identity (Echinodermata: Echinoidea: Tripneustes). Mol Phylogenet Evol 2016;104:1-13", PM % "27475495", "Molecular Phylogenetics and Evolution (PubMed 초록)", A),
 ("Bronstein O et al. Cryptic speciation in pan-tropical sea urchins: a case study of an edge-of-range population of Tripneustes from the Kermadec Islands. Sci Rep 2017;7(1):5948", PM % "28729611", "Scientific Reports (PubMed 초록)", A),
 ("McLaren E et al. Hidden in plain sight: Tripneustes kermadecensis is a junior synonym of the eastern Australian sea urchin Evechinus australiae described in 1878. Invertebr Syst 2023;37(11):741-754", PM % "41123014", "Invertebrate Systematics (PubMed 초록)", A),
 ("Wang H et al. The complete mitochondrial genome of the tropical sea urchin Tripneustes gratilla (Linnaeus, 1758) with two spine colors. Mitochondrial DNA B Resour 2024;9(1):15-19", PM % "38187012", "Mitochondrial DNA Part B (PubMed 초록)", A),
 ("Láruson ÁJ et al. Gene expression across tissues, sex, and life stages in the sea urchin Tripneustes gratilla. Mar Genomics 2018;41:12-18", PM % "30064945", "Marine Genomics (PubMed 초록)", A),
 ("Láruson ÁJ. Rates and relations of mitochondrial genome evolution across the Echinoidea, with special focus on the superfamily Odontophora. Ecol Evol 2017;7(13):4543-4551", PM % "28690785", "Ecology and Evolution (PubMed 초록)", A),
 ("Mos B et al. Do cues matter? Highly inductive settlement cues don't ensure high post-settlement survival in sea urchin aquaculture. PLoS One 2011;6(12):e28054", PM % "22162755", "PLoS One (PubMed 초록)", A),
 ("Mos B et al. Biogenic acidification reduces sea urchin gonad growth and increases susceptibility of aquaculture to ocean acidification. Mar Environ Res 2015;113:39-48", PM % "26595392", "Marine Environmental Research (PubMed 초록)", A),
 ("Dworjanyn SA, Byrne M. Impacts of ocean acidification on sea urchin growth across the juvenile to mature adult life-stage transition is mitigated by warming. Proc Biol Sci 2018;285(1876):20172684", PM % "29643209", "Proceedings of the Royal Society B (PubMed 초록)", A),
 ("Westbrook CE et al. Survivorship and feeding preferences among size classes of outplanted sea urchins, Tripneustes gratilla, and possible use as biocontrol for invasive alien algae. PeerJ 2015;3:e1235", PM % "26401450", "PeerJ (PubMed 초록)", A),
 ("Neilson BJ et al. Herbivore biocontrol and manual removal successfully reduce invasive macroalgae on coral reefs. PeerJ 2018;6:e5332", PM % "30123695", "PeerJ (PubMed 초록)", A),
 ("Westbrook CE et al. Cryopreservation of the collector urchin embryo, Tripneustes gratilla. Cryobiology 2024;115:104865", PM % "38367796", "Cryobiology (PubMed 초록)", A),
 ("Brink M et al. Metagenomic assessment of body surface bacterial communities of the sea urchin, Tripneustes gratilla. Mar Genomics 2019;47:100675", PM % "30962029", "Marine Genomics (PubMed 초록)", A),
 ("Bessey C et al. Diel movement patterns and abundance of the sea urchin Tripneustes gratilla with comparisons to Echinometra mathaei and their associated ecology at Ningaloo Reef, north-western Australia. Mar Environ Res 2025;212:107528", PM % "40945098", "Marine Environmental Research (PubMed 초록)", A),
 ("Liu Z et al. Ontogenetic and spatial variation in the feeding habits of Tripneustes gratilla. Mar Environ Res 2026;220:108170", PM % "42263421", "Marine Environmental Research (PubMed 초록)", A),
 ("Zhao X et al. Habitat preference and physiological characteristics of sea urchins: the case of Tripneustes gratilla. Mar Environ Res 2025;215:107814", PM % "41447984", "Marine Environmental Research (PubMed 초록)", A),
 ("Zhao X et al. Effects of Light Color on the Growth, Feeding, Digestion, and Antioxidant Enzymes of Tripneustes gratilla (Linnaeus, 1758). Biology (Basel) 2024;13(2)", PM % "38392284", "Biology (PubMed 초록)", A),
 ("Vazquez LC et al. Effect of sperm cell density on measured toxicity from the sea urchin Tripneustes gratilla fertilization bioassay. Environ Toxicol Chem 2003;22(9):2191-2194", PM % "12959550", "Environmental Toxicology and Chemistry (PubMed 초록)", A),
 ("Work TM et al. Mass mortality of collector urchins Tripneustes gratilla in Hawai`i. Dis Aquat Organ 2023;153:17-29", PM % "36727688", "Diseases of Aquatic Organisms (PubMed 초록)", A),
 ("한국산 성게류 미기록 Tripneustes gratilla 보고 논문(2008, 한국어 학술지) — 웹 검색 요약으로만 확인, 원문 미확인", "https://koreascience.kr/article/JAKO200801440597419.pdf", "koreascience (원문 열람 불가 — 웹 검색 결과 요약만 확인)", A),
 ("Rahman MS et al. Effects of temperature on gamete longevity and fertilization success in two sea urchin species, Echinometra mathaei and Tripneustes gratilla. Zoolog Sci 2009;26(1):1-8", PM % "19267606", "Zoological Science (PubMed 초록)", A),
]
sources = [{"n": i+1, "title": t, "url": u, "publisher": p, "accessed": a} for i, (t, u, p, a) in enumerate(src)]

S = {}
S["overview"] = ("한눈에 보기",
"흰수염성게(Tripneustes gratilla)는 Toxopneustidae 과에 속하는 성게로, 식약처 「식품원료 목록」에 '흰수염성게'라는 이름의 수산물 원료로 실려 있다[1]. 목록에서 이 종은 '사용가능' 원료이고, 쓸 수 있는 부위 칸은 '-'로 적혀 있으며 따로 붙은 사용 조건은 없다[1]. 영문명 칸은 비어 있다[1]. 이 종을 원재료로 하는 건강기능식품 고시형 원료는 확인하지 못함.\n\n"
"영어권에서는 몸에 모래·돌 조각을 덮는 습성 때문에 '콜렉터 성게(collector urchin)'로 불리며, 인도-태평양의 따뜻한 바다에 널리 사는 빠르게 자라는 종이다[5]. 생식소 품질이 좋아 호주·일본·필리핀·남아프리카공화국 등에서 상업적으로 중요한 성게로 소개되고, 태평양 섬나라에서는 자급 식량이기도 하다[5].\n\n"
"식품 성분 연구로는 베트남산 개체의 알(생식소)과 몸의 지질 조성, 알의 글리코겐 유사 α-글루칸 구조가 보고되었다[3, 4]. 한편 프랑스령 폴리네시아에서는 날 생식소를 먹고 시가테라 유사 중독이 생긴 사례가 있어 독소 축적에 주의가 필요하다[5]. 이 종만의 국가표준식품성분표 값과 국내 어획·양식 통계는 확인하지 못함.")
S["history"] = ("이용 역사",
"이 종은 태평양 섬나라에서 썰물 때 산호초에서 줍거나 얕은 물에서 잠수해 채집하는 귀한 먹거리로, 생식소를 날로 먹는 일이 많다고 원문이 설명했다[5]. 프랑스령 폴리네시아 모레아섬에서는 1950년대 말에 이미 일부 해안의 이 성게가 독이 있다고 주민들에게 알려져 있었고, 2009년 루루투섬에서 6명이 먹고 중독된 일이 있었다[5]. 국제 수요 때문에 자연 개체군이 남획되었다는 지적도 있다[5].\n\n"
"하와이에서는 이 종이 식량으로 쓰였을 뿐 아니라 외래 침입 해조류를 줄이는 생물 방제에도 쓰였다[26]. 양식장에서 기른 어린 성게는 침입 해조류 네 종을 모두 먹었고, 큰 개체일수록 가리지 않고 먹었다[24]. 하와이 카네오헤만에서는 잠수부가 침입 해조류 약 19,000 kg을 걷어 낸 뒤 양식한 어린 성게 약 99,000마리를 풀어, 2년 동안 처리 산호초의 침입 해조류 피복을 85% 줄였다[25]. 성게 정자 수정 시험은 미국 환경보호청(EPA)이 승인한 수질 생물감시 방법이며, 하와이에서는 이 종에 맞춘 방법이 쓰였다[32].\n\n"
"국내에서는 2008년 한국어 논문이 이 종을 제주 서귀포 앞바다(수심 약 25 m)에서 채집해 속(Tripneustes)까지 포함한 국내 첫 기록으로 보고했다는 내용을 웹 검색 요약으로만 확인했으며, 원문은 확인하지 못함[34]. 국내에서 이 종을 언제부터 식용해 왔는지를 다룬 공공기관 자료는 확인하지 못함.")
S["biology"] = ("생물학적 특징·생태",
"베트남 나트랑만 개체는 지름 8–10 cm의 반구형 껍데기에 짧고 촘촘한 가시(주황·검은 띠)를 가지며 생식소가 주황색이라고 기술되었다[4]. 이 종은 해조류와 해초를 주로 뜯어 먹는 초식자로, 산호초와 해초밭 생태계에서 핵심종으로 다뤄진다[5]. 중국 하이난 우즈저우섬 개체의 위 내용물 분석에서는 홍조류와 절지동물이 큰 비중을 차지했고, 500–600 g의 큰 개체는 홍조류 등 진핵생물이 80%를 넘게 먹었다[29].\n\n"
"서호주 닝갈루 산호초에서는 밀도가 1 m²당 4.29·6.02마리였고 대부분 지름 60–70 mm였다[28]. 아침에 잡은 개체의 위 내용물이 더 많아 밤에 더 많이 먹는 것으로 보였고, 밤이나 저녁에 가장 많이 움직였다[28]. 수조 실험에서는 모자반 서식처를 가장 좋아했고 그다음이 산호 암반이었다[30]. 순환여과 양식에서 청색 LED 빛을 준 무리가 체중 증가율 39.26%로 더 잘 자랐고 적색광 무리는 26%에 그쳤다[31].\n\n"
"수온 실험에서 이 종의 묽은 정자는 25·30 °C에서 생존력이 빠르게 떨어졌고 알은 약 6시간까지 수정 가능했다[35]. 하와이 개체를 조사한 원문은 체벽 염증과 궤양으로 대량 폐사한 사례를 보고했으나 원인은 밝히지 못했다[33].")
S["related_species"] = ("관련 종·이름",
"식약처 「식품원료 목록」에는 같은 속의 다른 원료가 없고, 성게류로는 말똥성게·보라성게·새치성게·흰꼭지성게·분지성게, 국문명 없이 학명으로만 실린 Heliocidaris erythrogramma, 그리고 학명 없는 '성게'·'성게알'·'성게살'·'성게추출물' 행이 따로 실려 있다[2]. 이 문서는 흰수염성게 자료만 다루며 말똥성게 등 다른 성게의 성분 값을 섞지 않았다[1, 2]. 목록상 국문명 '흰수염성게'의 유래를 설명한 공공기관 자료는 확인하지 못함.\n\n"
"같은 속에는 대서양의 T. ventricosus, 동태평양의 T. depressus 가 알려져 있는데, 형태·COI·바인딘(bindin) 자료로 보면 T. depressus 와 서태평양의 T. gratilla 는 같은 종이라고 결론 내린 연구가 있다[13, 14]. 홍해 개체군은 아종 T. gratilla elatensis 로 구분되며, 핵 유전자로는 다른 무리와 갈라지지만 미토콘드리아 유전자는 필리핀 개체와 거의 같아 미토콘드리아 유입으로 해석되었다[15]. 이 때문에 지금의 T. gratilla 가 여러 은밀종의 복합체일 수 있다는 의견이 나왔다[15].\n\n"
"2017년 케르마데크제도 개체가 새 종 T. kermadecensis 로 기재되었으나[16], 2023년 연구는 이 종이 1878년 시드니항 표본으로 기재된 Evechinus australiae 와 같아 Tripneustes australiae 가 올바른 이름이라고 정리했다[17].")
S["cultivation"] = ("어획·양식",
"이 종은 야생에서 채집하는 것 외에 양식 대상으로도 연구되며, 남아프리카공화국에서는 신흥 양식 산업으로 소개되었다[27]. 상업 양식에서 쓰던 자연 생물막 부착판은 착저율이 2% 미만이었고, 실험실에서는 모자반·산호말 같은 해조류와 그 해조류를 담갔던 바닷물이 착저율을 90% 이상으로 높였다[21]. 다만 착저 뒤 생존율이 낮은 것이 양식 효율의 큰 걸림돌로 남았다[21]. 착저 후 생존에 알맞은 수온은 24–28 °C였다[21].\n\n"
"성숙 개체를 기를 때 밀도를 1 m²당 9마리에서 43마리로 높이고 물 교환을 시간당 3.0회에서 0.3회로 줄이면 성장·생식소 생산·섭식이 최대 67%까지 줄었고, 주된 원인은 성게 자신이 낮춘 pH와 방해석 포화도였다[22]. 어린 개체부터 기른 장기 실험에서 수온 상승은 생식소 지수를 높였지만 pH 7.6에서는 수온과 관계없이 생식소가 거의 생기지 않았다[23].\n\n"
"하와이에서는 양식 종묘를 연중 확보하려고 배아 동결보존을 시험해, 낭배기 배아를 1 M 다이메틸설폭사이드로 처리했을 때 해동 후 생존율이 최대 85.5%였다[26]. 이 종의 국내 어획량·양식 생산 통계는 확인하지 못함.")
S["processing"] = ("가공·성분 연구",
"베트남산 개체의 총지질은 생물 무게 기준 알 4.41%, 몸 1.32%였고 두 부위 모두 트라이아실글리세롤이 총지질의 76–78%를 차지했다[3]. 지방산 가운데 EPA는 알 6.42%, 몸 13.39%, 아라키돈산은 알 10.95%, 몸 30.96%였고, 인지질 분자종은 고분해능 액체크로마토그래피-질량분석으로 137종이 확인되었다[3].\n\n"
"알을 동결건조한 가루 16 g에서 단백질 분해효소(파파인) 처리와 에탄올 침전으로 중성 다당 2 g을 얻었으며, 포도당이 95.7–96.7%였다(본문과 방법 절의 값이 다름)[4]. 이 다당은 곁사슬이 약 5개 포도당 길이로 매우 촘촘히 가지 친 글리코겐 유사 α-글루칸이었고, 생리활성은 아직 발표되지 않았다[4].\n\n"
"홍해산 개체 300 g을 70% 에탄올로 우려 얻은 알코올 추출물은 시험관에서 α-아밀레이스를 IC50 5.31 µg/mL로 억제했고, 이를 나노현탁액으로 만들어 알록산 당뇨 쥐에 하루 200 mg/kg씩 21일 먹이자 혈당이 내려갔다(세포·동물 결과)[6]. 사람에서 확인한 연구는 확인하지 못함.\n\n"
"식품첨가물 소브산·소브산칼륨·소브산칼슘은 성게젓에 소브산으로서 2.0 g/kg 이하로 쓸 수 있다고 식약처 목록에 적혀 있다[2].")
S["genetics"] = ("유전 정보",
"붉은 가시와 흰 가시 개체의 미토콘드리아 유전체는 각각 15,774 bp와 15,723 bp였고, 모두 단백질 유전자 13개, rRNA 2개, tRNA 22개를 가졌으며 두 색 개체의 유사도는 98.91%였다[18]. 미토콘드리아 유전체 계통 분석은 만두성게과를 포함하는 상과 Odontophora 를 지지했다[20].\n\n"
"성체 수컷·암컷과 약 1,000마리의 플루테우스 유생으로 전사체 초안이 만들어졌고, 생식소·신경환·관족과 차극(pedicellariae)에서 유전자 발현이 비교되었다[19]. 이 전사체에서는 종양 억제 유전자 DMBT1 무리가 Strongylocentrotus purpuratus 의 주석 유전체보다 늘어나 있었다[19].\n\n"
"전 세계 187개체의 COI 염기서열을 본 연구에서 인도양과 태평양 개체군 사이에 뚜렷한 유전적 구분이 없었고, 이 속의 인도-태평양 집단은 두 대양에 걸친 하나의 큰 메타개체군처럼 보였다[13]. 다만 홍해 아종처럼 핵 유전자로는 구분되는 무리가 있어 미토콘드리아 표지만으로 종을 가르기는 어렵다[15]. 염색체 수준 핵 유전체 공개 여부는 확인하지 못함.")
S["safety"] = ("안전성",
"가장 중요한 위험은 시가테라 독소 축적이다[5]. 2015년 프랑스령 폴리네시아 누쿠히바섬에서 3명이 이 성게의 날 생식소를 먹고 1시간 안에 구토·설사와 찬 것에 닿을 때의 통증 같은 신경 증상을 보였다[5]. 같은 만에서 잡은 개체의 전체 조직에서 태평양 시가톡신이 2015년 7월 약 20 ng P-CTX-3C 당량/g으로 측정되어, 원문이 인용한 미국 FDA·EFSA 권고 수준(0.01 ng P-CTX-1B 당량/g)을 크게 넘었다[5]. 16개월 뒤에도 독소는 줄었지만 권고 수준보다 높았다[5].\n\n"
"차극에서는 생쥐 복강 주사 LD50 0.85 mg/kg인 25 kDa 열에 약한 독성 단백질이 분리되었다[7]. 이는 주사 실험 결과로, 먹었을 때의 독성과는 다르다[7]. 네 종의 저서생물을 같은 곳에서 비교한 조사에서 이 성게는 크롬 16.98 µg/g, 납 4.80 µg/g으로 높은 축적을 보였고, 조사한 생물 전반에서 단단한 부위의 금속 농도가 조직보다 낮았다[11]. 하와이 호놀루아만 조사에서는 퇴적물의 코발트·크롬·망간·니켈·바나듐이 높았지만 망간을 빼면 이 성게 등 생물에서는 그만큼 높지 않았다[12].\n\n"
"성게 알레르기·잔류 기준에 관한 국내 공공기관 정보는 확인하지 못함. 날 생식소를 먹는 경우 시가테라가 잦은 열대 해역 개체는 피하라는 경고가 원문에 있다[5].")

sections = [{"key": k, "title": v[0], "body": v[1]} for k, v in S.items()]

def c(name, ko, cls, role, part, content, act, s):
    return {"name": name, "name_ko": ko, "class": cls, "role": role, "part": part, "content_text": content, "activity_ko": act, "source": s}
compounds = [
 c("Triacylglycerol", "트라이아실글리세롤", "중성지질", "nutrient", "알·몸", "총지질 중 알 78.37 ± 0.64%, 몸 76.10 ± 0.57%(총지질은 생물 무게 기준 알 4.41%, 몸 1.32%)", "베트남산 개체에서 가장 많은 지질 종류였다[3]", [3]),
 c("Eicosapentaenoic acid", "에이코사펜타엔산(EPA)", "오메가-3 다가불포화지방산", "nutrient", "알·몸", "총지방산 중 알 6.42%, 몸 13.39%", "알과 몸의 두 주요 다가불포화지방산 가운데 하나였다[3]", [3]),
 c("Arachidonic acid", "아라키돈산", "오메가-6 다가불포화지방산", "nutrient", "알·몸", "총지방산 중 알 10.95%, 몸 30.96%", "몸의 오메가-6 비율(39.83%)을 높인 주성분이며, 인지질 PI·PE·PC 분자종에 많이 붙어 있었다[3]", [3]),
 c("Palmitic acid", "팔미트산", "포화지방산", "nutrient", "알·몸", "총지방산 중 알 25.10%, 몸 11.74%", "알의 포화지방산(41.74%) 가운데 가장 많았다[3]", [3]),
 c("Myristic acid", "미리스트산", "포화지방산", "nutrient", "알·몸", "총지방산 중 알 14.50%, 몸 3.59%", "알에서 팔미트산 다음으로 많은 포화지방산이었다[3]", [3]),
 c("Phosphatidylinositol 18:0/20:4", "포스파티딜이노시톨 18:0/20:4", "글리세로인지질", "marker", "알·몸", "PI 분자종 중 알 38.65%, 몸 48.19%", "PI 무리에서 가장 많은 분자종으로, 이 연구에서 확인한 인지질 137종 가운데 대표 성분이다[3]", [3]),
 c("Phosphatidylserine 20:1/20:1", "포스파티딜세린 20:1/20:1", "글리세로인지질", "bioactive", "알·몸", "PS 분자종 중 알 42.48%, 몸 44.41%", "PS 무리에서 가장 많은 분자종이었다[3]", [3]),
 c("alpha-D-Glucan (glycogen-like)", "글리코겐 유사 α-글루칸", "저장 다당", "marker", "알", "동결건조 알 16 g에서 2 g 분리; 포도당 95.7–96.7%(본문·방법 절 값 다름)", "말단:4-결합:4,6-분지 포도당이 1:8:1이고 평균 사슬 길이 약 5인 매우 촘촘히 가지 친 구조로, 생리활성은 아직 발표되지 않았다[4]", [4]),
 c("Ciguatoxin P-CTX-3B", "태평양 시가톡신 P-CTX-3B", "폴리에테르 해양 독소(축적 오염물)", "contaminant", "전체 조직", "2015년 7월 시료 독소 조성의 44%(LC-MS/MS); 총량 21.5 ng P-CTX-3C 당량/g", "와편모조류 Gambierdiscus 에서 먹이사슬로 옮겨 온 독소로, 시가테라 유사 중독의 원인으로 확인되었다[5]", [5]),
 c("Ciguatoxin P-CTX-3C", "태평양 시가톡신 P-CTX-3C", "폴리에테르 해양 독소(축적 오염물)", "contaminant", "전체 조직", "2015년 7월 조성의 20%, 2016년 11월 58%; 총량 1.48 ng P-CTX-3C 당량/g(2016년 11월, LC-MS/MS)", "정량 기준 물질로 쓰였고, 2016년 시료에서도 검출되었다[5]", [5]),
 c("Pedicellarial toxin (25 kDa protein)", "차극 독성 단백질(25 kDa)", "단백질 독소", "bioactive", "차극(pedicellariae)", "생쥐 복강 주사 LD50 0.85 mg/kg(함량 수치는 초록에 없음)", "열에 약한 단백질로, 항히스타민제 전처리로도 독성이 막히지 않았다(동물 주사 결과)[7]", [7]),
 c("TGL-I lectin", "차극 렉틴 TGL-I", "헤파린 결합 렉틴", "bioactive", "차극(globiferous pedicellariae)", "분자량 23 kDa(함량 수치는 초록에 없음)", "칼슘과 무관하게 헤파린에 붙는 렉틴으로, 생쥐 비장세포 분열은 일으키지 않았다(세포 결과)[8]", [8]),
 c("Coelomic hemolytic lectin (29 kDa)", "체강액 용혈 렉틴(29 kDa)", "렉틴", "bioactive", "체강액", "분자량 29 kDa(함량 수치는 초록에 없음)", "칼슘 농도에 따라 용혈 활성을 보였고 젖당으로 억제되었다(시험관 결과)[9]", [9]),
 c("o-Bromo-L-phenylalanine", "o-브로모-L-페닐알라닌", "브롬화 아미노산(펩타이드 구성)", "bioactive", "알 젤리", "정자 활성화 펩타이드 8종의 구성 아미노산(함량 수치는 초록에 없음)", "이 종의 알 젤리에서 새로 확인된 아미노산으로, 정자를 활성화하는 펩타이드에 들어 있다[10]", [10]),
 c("Total phenolics", "총페놀 함량", "페놀성 화합물(총량)", "bioactive", "전체(부위 명시 없음) 알코올 추출물", "54.26 ± 1.27 mg GAE/g 추출물", "원문은 추출물의 항산화·당 분해효소 억제 효과에 기여했을 것으로 추정했다(세포·동물 결과)[6]", [6]),
]

def cond(**kw):
    keys = ["instrument","column","mobile_phase","gradient","flow","temp","detection","injection","sample_prep","standard","linearity","lod","loq","recovery"]
    return {k: kw.get(k, "") for k in keys}
assays = [
 {"role": "literature", "compound": "Phosphatidylinositol 18:0/20:4 (phospholipid molecular species)", "compound_ko": "인지질 분자종(PI 18:0/20:4 등)", "part": "알·몸",
  "content": "PI 분자종 중 알 38.65%, 몸 48.19%(상대 함량)", "method": "HPLC-ESI-IT-TOF-MS(고분해능 질량분석)",
  "conditions": cond(instrument="Shimadzu LCMS-IT-TOF(LC-20AD 펌프 2대, CTO-20A 오븐, SIL-20A 자동주입기)", column="Shim-Pack diol, 50 mm × 4.6 mm, 5 μm",
     mobile_phase="A: n-헥산/2-프로판올/포름산/트라이에틸아민(82:17:1:0.08), B: 2-프로판올/물/포름산/트라이에틸아민(85:14:1:0.08)",
     gradient="B 5% → 80%(25분), 1분 유지, 5%로 복귀(10분 이상), 5%에서 4분 유지(총 40분)", flow="0.2 mL/min",
     detection="ESI 양·음이온, m/z 200–1600, 이온원 200 °C, −3.5/4.5 kV, 건조가스 200 kPa, 분무가스 1.5 L/min",
     sample_prep="Bligh–Dyer 법(클로로폼–메탄올 1:2, 초음파 2시간 × 3회), 시료 300 g", standard="Avanti Polar Lipids 인지질 표준품(PC·PE·PS 16:0–20:4, PI 18:0–20:4 등)",
     linearity="추출이온크로마토그램 피크 면적으로 무리 안 상대 함량 계산(검량선 없음)"),
  "rationale": "이 종의 알·몸 극성지질을 분자종 수준으로 처음 정량한 연구로, 인지질 137종의 상대 함량을 같은 조건에서 비교할 수 있다[3]. PMC 전문 Methods 확인[3].", "source": [3], "url": PMC % "PMC10180406", "source_kind": "paper"},
 {"role": "literature", "compound": "Pacific ciguatoxins (P-CTX-3B, P-CTX-3C, 51-OH-P-CTX-3C, P-CTX-4A, P-CTX-4B)", "compound_ko": "태평양 시가톡신", "part": "전체 조직(동결건조)",
  "content": "21.5 ng P-CTX-3C 당량/g(2015년 7월), 1.48 ng P-CTX-3C 당량/g(2016년 11월)", "method": "LC-MS/MS(MRM)",
  "conditions": cond(instrument="Shimadzu UFLC XR Nexera + Sciex API-4000 QTrap(turboV 이온원)", column="Zorbax Eclipse Plus C18, 50 × 2.1 mm, 1.8 µm(Agilent)",
     mobile_phase="A: 물, B: 메탄올(둘 다 2 mM 포름산암모늄·50 mM 포름산)", gradient="B 78% → 88%(10분), 4분 유지, 5분 재평형", flow="400 µL/min", temp="40 °C",
     detection="ESI 양이온 MRM, 전구이온 [M+NH4]+·[M+H]+, 커튼가스 25, 이온스프레이 5500 V, 300 °C, gas1 40·gas2 60 psi, EP 10 V, DP 105 V",
     sample_prep="동결건조 조직을 아세톤으로 2회 추출 → 90% 메탄올/헥산 분배 → 에틸아세테이트/메탄올(90/10) → 실리카 SPE(Florisil) → 메탄올",
     standard="P-CTX-3C 표준품(정량), 기타 P-CTX 혼합 표준(동정)", linearity="P-CTX-3C 선형 검량선(범위는 원문에 없음)",
     lod="LC-MS/MS 검출한계는 원문에 없음(세포시험 CBA-N2a 검출한계 0.02 ng P-CTX-3C 당량/g 생물 무게)"),
  "rationale": "시가테라 중독의 원인 독소로, 이 종을 먹을 때 가장 중요한 안전 지표다[5]. PMC 전문 Methods 확인[5].", "source": [5], "url": PMC % "PMC5923409", "source_kind": "paper"},
 {"role": "literature", "compound": "alpha-D-Glucan (glucose composition)", "compound_ko": "α-글루칸(구성 단당)", "part": "알(동결건조)",
  "content": "건조 알 16 g에서 다당 2 g; 포도당 95.7–96.7%, 만노스 1.0%", "method": "산 가수분해 후 알디톨 아세테이트 GC-FID",
  "conditions": cond(instrument="Agilent 8860 GC, 불꽃이온화검출기", column="HP-5 모세관 칼럼(30 m × 0.32 mm, 0.25 μm)", detection="FID",
     sample_prep="2 M 트라이플루오로아세트산, 100 °C, 8시간 가수분해 후 알디톨 아세테이트 유도체화; 다당은 탈지·파파인(60 °C, 24시간)·CTAB 처리·투석·에탄올 침전으로 분리",
     standard="내부표준 myo-이노시톨 1 mg/mL; 분자량은 풀루란 표준(805–6.2 kDa), TSK G3000SW+G5000PWXL, 0.5 mL/min, 굴절률 검출"),
  "rationale": "알(생식소)에 쌓이는 주요 저장 다당으로, 다른 성게의 면역 활성 α-글루칸과 구조를 비교하는 기준이 된다[4]. PMC 전문 Methods 확인[4].", "source": [4], "url": PMC % "PMC12609645", "source_kind": "paper"},
 {"role": "literature", "compound": "Volatile/semi-volatile constituents (germacrene, cholesterol, EPA methyl ester etc.)", "compound_ko": "GC-MS 성분 프로파일", "part": "전체(부위 명시 없음) 70% 에탄올 추출물의 알코올 분획",
  "content": "정량값 없음(라이브러리 대조 동정); 총페놀 54.26 ± 1.27 mg GAE/g 추출물", "method": "GC-MS(EI)",
  "conditions": cond(instrument="Agilent 7890B GC / 5977B MSD", column="DB-5MS(30 m × 0.25 mm, 0.25 μm)", mobile_phase="운반가스 헬륨", injection="1 µL, 주입구 300 °C",
     detection="EI 70 eV, m/z 50–800, 용매 지연 7.3분", sample_prep="70% 에탄올 냉침 후 Diaion HP-20으로 탈염, 메탄올 분획 사용", standard="Wiley·NIST 질량 스펙트럼 라이브러리 대조"),
  "rationale": "홍해산 개체 추출물의 성분 계열(테르펜·스테로이드·지방산)을 보여 주지만 정량 연구가 아니며 온도 프로그램은 원문에 적혀 있지 않다[6]. PMC 전문 Methods 확인[6].", "source": [6], "url": PMC % "PMC12839668", "source_kind": "paper"},
]

d = {"slug": "tripneustes-gratilla", "name_ko": "흰수염성게", "name_en": "", "scientific_name": "Tripneustes gratilla",
     "aliases": ["흰수염성게", "Tripneustes gratilla"], "sections": sections, "compounds": compounds, "markers": [], "nutrients": [],
     "production": [], "world": [], "assays": assays, "gi": [], "orgs": [], "sources": sources}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in sections: print(s["key"], len(s["body"]))
