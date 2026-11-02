import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
PM = "https://pubmed.ncbi.nlm.nih.gov/{}/"
ACC = "2026-11-02"
def pm(n, pmid, title, pub):
    return {"n": n, "title": title, "url": PM.format(pmid), "publisher": pub, "accessed": ACC}
I1020 = "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020"
sources = [
 {"n":1,"title":"식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 거친껄껄이그물버섯(Leccinum scabrum (Bull.:Fr.) S.F.Gray) (로컬 원자료 I1020_20261013.json 대조)","url":I1020,"publisher":"식품의약품안전처","accessed":"2026-10-13"},
 {"n":2,"title":"식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 비교 항목: 왕그물버섯자실체(Leccinum rugosiceps)·접시껄껄이그물버섯(Leccinnum extremiorientale, 이명 껄껄이그물버섯)·껄껄이그물버섯자실체(Boletus impolitus)·그물버섯자실체(Boletus edulis) (로컬 원자료 I1020_20261013.json)","url":I1020,"publisher":"식품의약품안전처","accessed":"2026-10-13"},
 pm(3,"40083412","Nutritional contents and antimicrobial activity of the culinary-medicinal mushroom Leccinum scabrum. Mycology 2024;16(1):402-412 (PMC11899239 전문 확인)","Taylor & Francis (PubMed)"),
 pm(4,"39452670","Hypoglycemic Properties of Leccinum scabrum Extracts — An In Vitro Study on α-Glucosidase and α-Amylase Inhibition and Metabolic Profile Determination. J Fungi 2024;10(10):718 (PMC11508548 전문 확인)","MDPI (PubMed)"),
 pm(5,"32116361","The effect of drying temperature on bioactive compounds and antioxidant activity of Leccinum scabrum (Bull.) Gray and Hericium erinaceus (Bull.) Pers. J Food Sci Technol 2020;57(2):513-525 (PMC7016157 전문 확인)","Springer (PubMed)"),
 pm(6,"40807452","Bioactive Compounds and Antioxidant Activity of Boletus edulis, Imleria badia, Leccinum scabrum in the Context of Environmental Conditions and Heavy Metals Bioaccumulation. Molecules 2025;30(15):3277 (PMC12348591 전문 확인)","MDPI (PubMed)"),
 pm(7,"29719194","Mineral constituents in Leccinum scabrum from lowland locations in the central Europe and their relation to concentration in forest topsoil. J Environ Sci Health B 2018;53(8):546-560","Taylor & Francis (PubMed)"),
 pm(8,"30388922","Inorganic elemental concentrations in birch bolete mushroom (Leccinum scabrum) and top soil: contamination profiles, bioconcentration and annual variations. J Environ Sci Health B 2018;53(12):831-839","Taylor & Francis (PubMed)"),
 pm(9,"33691593","Distribution and bioconcentration of some elements in the edible mushroom Leccinum scabrum from locations in Poland. J Environ Sci Health B 2021;56(4):396-414","Taylor & Francis (PubMed)"),
 pm(10,"32531137","Accumulation of Minerals by Leccinum scabrum from Two Large Forested Areas in Central Europe: Notecka Wilderness and Tuchola Forest. Chem Biodivers 2020;17(8):e2000264","Wiley (PubMed)"),
 pm(11,"34268685","Detrimental and essential elements in fruiting bodies of mushrooms with ecological relationship to birch (Betula sp.) collected in the Bohemian Forest, the Czech Republic. Environ Sci Pollut Res 2021;28(47):67852-67862","Springer (PubMed)"),
 pm(12,"33297091","Toxicological risks and nutritional value of wild edible mushroom species — a half-century monitoring study. Chemosphere 2021;263:128095","Elsevier (PubMed)"),
 pm(13,"25602154","Bioaccumulation of elements in three selected mushroom species from southwest Poland. J Environ Sci Health B 2015;50(3):207-216","Taylor & Francis (PubMed)"),
 pm(14,"18074278","Selected elements in Brown Birch Scaber Stalk Leccinum scabrum. J Environ Sci Health A 2007;42(14):2081-2088","Taylor & Francis (PubMed)"),
 pm(15,"14755851","Selenium in selected species of mushrooms from Poland (폴란드어, 초록). Rocz Panstw Zakl Hig 2003;54(3):249-254","Roczniki PZH (PubMed)"),
 pm(16,"11815805","Total mercury in mushrooms and underlying soil substrate from the Borecka Forest, Northeastern Poland. Arch Environ Contam Toxicol 2002;42(2):145-154","Springer (PubMed)"),
 pm(17,"9064742","Mercury in edible mushrooms from the area of Kościerzyna forests and from the Vistula peninsula (폴란드어, 영문 초록). Rocz Panstw Zakl Hig 1996;47(2):205-210","Roczniki PZH (PubMed)"),
 pm(18,"9260308","The concentrations and bioconcentration factors of mercury in mushrooms from the Mierzeja Wiślana sand-bar, northern Poland. Sci Total Environ 1997;203(3):221-228","Elsevier (PubMed)"),
 pm(19,"36004707","Radioactive Contamination of Wild Mushrooms from Ukraine under Conditions of Contrasting Radiation Loads: 36 Years after the Chernobyl Nuclear Power Plant Catastrophe. Int J Med Mushrooms 2022;24(9):25-40","Begell House (PubMed)"),
 pm(20,"25764823","The assessment of the content of 137Cs of the global and Chernobyl origin in forest soils and some types of edible fungi (러시아어, 영문 초록). Radiats Biol Radioecol 2014;54(2):201-208","Radiatsionnaia biologiia, radioecologiia (PubMed)"),
 pm(21,"34338984","Effect of drying, blanching, pickling and maceration on the fate of 40K, total K and 137Cs in bolete mushrooms and dietary intake. Environ Sci Pollut Res 2022;29(1):742-754","Springer (PubMed)"),
 pm(22,"22164763","Comparative study of wild edible mushrooms as sources of antioxidants. Int J Med Mushrooms 2011;13(4):335-341","Begell House (PubMed)"),
 pm(23,"11231270","Glycoinositolphosphosphingolipids (basidiolipids) of higher mushrooms. Eur J Biochem 2001;268(5):1190-1205","FEBS/Wiley (PubMed)"),
 pm(24,"11465669","Human heterophile antibodies recognizing distinct carbohydrate epitopes on basidiolipids from different mushrooms. Immunol Invest 2001;30(2):115-129","Taylor & Francis (PubMed)"),
 pm(25,"11714352","Mercaptan-capturing properties of mushrooms. J Agric Food Chem 2001;49(11):5509-5514","American Chemical Society (PubMed)"),
 pm(26,"17604144","Phylogeographic patterns in Leccinum sect. Scabra and the status of the arctic-alpine species L. rotundifoliae. Mycol Res 2007;111(Pt 6):663-672","Elsevier (PubMed)"),
 pm(27,"31900053","Revision of leccinoid fungi, with emphasis on North American taxa, based on molecular and morphological data. Mycologia 2020;112(1):197-211","Taylor & Francis (PubMed)"),
 pm(28,"29681110","Effects of soil trenching and coring on the formation of ectomycorrhizas on birch seedlings grown around mature trees. New Phytol 1984;98(1):143-153","Wiley (PubMed)"),
 pm(29,"17707073","Uptake and biodegradation of DDT by 4 ectomycorrhizal fungi. Sci Total Environ 2007;385(1-3):235-241","Elsevier (PubMed)"),
 pm(30,"41590482","The Genus Leccinum: Global Advances in Taxonomy, Ecology, Nutritional Value, and Environmental Significance. J Fungi 2026;12(1):70 (PMC12842815 전문 확인)","MDPI (PubMed)"),
 pm(31,"30784799","Elemental composition of selected species of mushrooms based on a chemometric evaluation. Ecotoxicol Environ Saf 2019;173:353-365","Elsevier (PubMed)"),
 pm(32,"28494204","Bio- and toxic elements in mushrooms from the city of Umeå and outskirts, Sweden. J Environ Sci Health B 2017;52(8):577-583","Taylor & Francis (PubMed)"),
 pm(33,"32497838","Multiannual monitoring (1974-2019) of rare earth elements in wild growing edible mushroom species in Polish forests. Chemosphere 2020;257:127173","Elsevier (PubMed)"),
 pm(34,"34444630","Bioaccumulation of Macronutrients in Edible Mushrooms in Various Habitat Conditions of NW Poland — Role in the Human Diet. Int J Environ Res Public Health 2021;18(16):8881","MDPI (PubMed)"),
]
# fix author-less titles: remove person names per rule (no personal names) -> keep only titles
import re


sections = [
 {"key":"overview","title":"한눈에 보기","body":
  "거친껄껄이그물버섯(Leccinum scabrum)은 그물버섯과(Boletaceae) 껄껄이그물버섯속의 외생균근 버섯으로, 영어 논문에서는 birch bolete 또는 brown birch scaber stalk라 부른다[4, 14]. 주로 자작나무 아래에서 나며 스칸디나비아와 중·동부 유럽에서 즐겨 먹는 야생 식용버섯이다[3, 4]. 식품의약품안전처 「식품원료 목록」에는 원료명 '거친껄껄이그물버섯', 학명 Leccinum scabrum (Bull.:Fr.) S.F.Gray로 올라 있고, 상태는 '사용가능', 사용 조건은 '사용가능부위 : 자실체'이다[1]. 따라서 일반 식품의 원료로는 자실체(버섯 몸체)만 쓸 수 있다[1]. 건강기능식품 고시형 원료의 원재료 목록에는 없어 고시된 지표성분과 기준은 확인하지 못함.\n\n같은 목록에는 같은 속의 왕그물버섯자실체(L. rugosiceps)와 접시껄껄이그물버섯(L. extremiorientale)이 따로 올라 있으므로 이 문서는 그 종들의 자료를 섞지 않는다[2]. 이 종의 연구는 대부분 폴란드 등 유럽 야생 시료의 무기질·중금속·방사성 세슘 축적에 모여 있고, 영양 성분과 추출물 활성 연구는 최근에야 나왔다[7, 19, 3, 4]."},
 {"key":"history","title":"이름과 이용의 역사","body":
  "이 종은 1783년 프랑스 박물학자 불리아르가 Boletus scaber라는 이름으로 처음 기재했고, 1821년 그레이가 Leccinum 속으로 옮겼다[3]. 식약처 목록의 학명 표기 'Leccinum scabrum (Bull.:Fr.) S.F.Gray'도 이 명명 경과를 반영한다[1]. 영어권 논문은 brown birch scaber stalk, common scaber stalk, birch bolete, red birch boletus 등 여러 일반명을 써 왔다[14, 16, 4, 23].\n\n이 버섯은 스칸디나비아와 중·동부 유럽에서 맛과 영양 때문에 가장 널리 즐기는 야생 버섯 가운데 하나로 꼽힌다[4]. 폴란드 연구는 이 종을 가장 흔히 먹는 야생 버섯 가운데 하나로 소개했고, 어린 자실체와 갓이 가장 맛있으며 바로 먹거나 말리거나 가공해 먹는다고 적었다[5]. 수확 뒤 상온 보관 기간이 며칠에 불과해 말린 제품으로도 유통된다[5]. 국내에서의 이용 역사와 국문명 '거친껄껄이그물버섯'의 유래는 확인하지 못함."},
 {"key":"biology","title":"균학적 특징","body":
  "거친껄껄이그물버섯은 자작나무와 외생균근을 맺는 공생균이며, 낙엽수림을 좋아하고 너도밤나무 아래에서도 난다[4]. 발생 시기는 초여름부터 가을까지로, 풀밭·낮은 덤불·숲 가장자리의 트인 곳에서 볼 수 있다[3]. 폴란드·벨라루스 국경의 비아워비에자 원시림 시료는 갓 지름이 최대 15 cm로 흰빛~연회색에 노란 기가 돌았고, 대는 약 15 cm × 2 cm로 길며 짙은 회색의 작은 비늘(껄껄이)로 덮여 있었다[3]. 살은 흰색이며 만지거나 익히면 검게 변했고, 포자는 13–21 × 4–6 µm의 좁은 타원형~방추형이었다[3]. 같은 연구는 형태 동정을 ITS 염기서열 계통 분석으로 확인했다[3].\n\n영국 실험에서 이 종의 균근은 다 자란 자작나무 근처에 심은 묘목에는 잘 생겼으나, 도랑이나 흙 기둥으로 큰 나무와 뿌리를 끊은 묘목에는 거의 생기지 않았다[28]. 연구자는 Leccinum 균이 묘목 뿌리를 감염하려면 큰 나무에서 오는 광합성 산물 공급이 계속 필요하다고 해석했다[28]. 상처가 나면 색이 변하는 버섯류로서, 아세톤 분말이 메틸메르캅탄을 잘 붙잡는 성질도 보고되었다[25]."},
 {"key":"related_species","title":"가까운 종과 혼동","body":
  "Leccinum 절 Scabra에 속하는 종은 모두 자작나무(Betula)하고만 공생하며 북반구 전역에 분포한다[26]. 이 절의 Gapdh 유전자와 5.8S-ITS2 분석에서 L. scabrum과 L. holopus는 대륙을 넘나드는 계통지리 양상을 보였고, 종간 교잡이 여러 번 일어났다는 신호도 나왔다[26]. 북미 중심의 2020년 재분류는 28S·tef1·rpb2 염기서열로 껄껄이그물버섯류(leccinoid fungi)가 다섯 큰 계통군 가운데 네 곳에 흩어져 있음을 보였다[27].\n\n국문명이 비슷한 식약처 목록 항목에 주의해야 한다[2]. '껄껄이그물버섯자실체'는 Boletus impolitus이고, '접시껄껄이그물버섯'(Leccinum extremiorientale)은 이명이 '껄껄이그물버섯'이며, '왕그물버섯자실체'는 Leccinum rugosiceps이다[2]. 체코 연구에서 함께 조사한 L. versipelle도 은·루비듐을 가장 많이 농축하는 비슷한 경향을 보였으나, 카드뮴 생물농축계수는 이 종(4.7)이 L. versipelle(1.6)보다 높았다[11]. 폴란드 연구에서는 한 지역의 Leccinum 3종(L. aurantiacum·L. scabrum·L. versipelle)을 칼륨·나트륨·마그네슘 등 원소 조성으로 구별할 수 있었다[31]. 속 전체로는 60개가 넘는 목본 숙주 속과 외생균근을 맺는다고 정리되지만, 이 종은 자작나무와의 관계가 가장 뚜렷하다[30, 26]. 이 문서의 수치는 L. scabrum으로 명시된 시료만 옮겼다[7, 11]."},
 {"key":"cultivation","title":"채취와 생산","body":
  "거친껄껄이그물버섯은 살아 있는 자작나무와 균근을 맺어야 하는 외생균근균이어서, 연구에 쓰인 시료는 모두 숲에서 채집한 야생 자실체였다[3, 28]. 상업적 인공 재배 방법은 확인하지 못함. 국내 채취량·생산 통계와 지리적 표시 등록도 확인하지 못함.\n\n채집지의 흙이 성분을 좌우한다[7, 10]. 폴란드 북부 다섯 지역 조사에서 숲 겉흙의 원소 농도는 지역마다 크게 달랐고, 자실체의 축적 정도도 채집지에 따라 달랐다[7]. 폴란드 두 대형 숲(노테츠카·투홀라) 비교에서도 갓의 칼륨·마그네슘·은·니켈·아연 등 일부 원소는 숲에 따라 차이가 났다[10]. 폴란드 북서부 조사에서는 이 종이 산성 아레노솔 토양에서 자랐고, 흙의 산도가 칼륨·마그네슘 흡수에 영향을 주었다[34]. 폴란드 남서부 비교에서 이 종의 마그네슘(312 mg/kg 건조중)과 망가니즈(10 mg/kg 건조중)는 함께 조사한 그물버섯(B. edulis)·B. badius보다 낮았고 철·아연도 가장 낮았다[13]. 벨라루스 조사에서 이 종의 137Cs 이행계수는 (15–20) × 10^-3 m2/kg으로 그물버섯(약 10 × 10^-3 m2/kg)보다 높았다[20]. 세 번의 발생 철을 이어 본 연구는 같은 장소에서도 해마다 원소 농도가 달라졌다고 보고했다[8]. 실험실 순수 배양에서 이 종의 균사는 DDT(5 mg/L)를 15일 동안 거의 없애고 DDD 등으로 분해했다[29]."},
 {"key":"processing","title":"가공과 이용","body":
  "말리기는 성분을 바꾼다. 폴란드 연구는 생 자실체와 20·40·70 ℃에서 말린 시료를 비교했는데, 두 버섯(이 종과 노루궁뎅이) 모두 건조 온도가 높을수록 총페놀·에르고스테롤·항산화 활성이 줄었고 70 ℃에서 가장 많이 줄었다[5]. 70 ℃ 건조 시 에르고스테롤은 두 종에서 각각 약 50%와 48% 줄었다[5]. DPPH 라디칼 소거능은 생시료 > 자연 건조 > 40 ℃ > 70 ℃ 순이었다[5]. 블랜칭·식초 절임·건조 분말 침지 실험에서는 방사성 세슘(137Cs)이 블랜칭으로 15 ± 13%, 블랜칭 뒤 절임으로 55 ± 8% 줄었다(이 종을 포함한 그물버섯류 3종 결과)[21].\n\n효능 연구는 시험관·하등동물 수준이다[4, 3]. 마이크로파로 얻은 에틸아세테이트 추출물은 α-글루코시데이스를 IC50 0.42 ± 0.02 μg/mL로 억제해 기준물질 DNJ(25.4 ± 0.6 μg/mL)보다 강했고, 초파리에게 먹인 예비 실험에서 포도당 수치를 최대 약 43% 낮췄다[4]. 물 추출물은 시험한 병원성 세균 4종의 생장을 모두 억제했고, 70%를 넘는 높은 억제는 25–100 mg/mL 농도에서 나타났다[3]. 사람 대상 시험은 확인하지 못함."},
 {"key":"genetics","title":"유전체와 분자 연구","body":
  "PubMed 검색에서 거친껄껄이그물버섯의 전체 핵 유전체나 미토콘드리아 유전체 해독 보고는 확인하지 못함. 분자 연구는 주로 종 판별과 계통 분석에 쓰였다[26, 27, 3]. 절 Scabra 연구는 단일 사본 핵 유전자 Gapdh와 다중 사본 5.8S-ITS2를 함께 분석했고, 유전자 계통수끼리 어긋나는 점을 근거로 종간 교잡을 제시했다[26]. 같은 연구에서 북극·고산형 L. rotundifoliae만 추운 지역에 한정된 계통이었고, 이 종은 대륙 간 계통지리 양상을 보였다[26].\n\n껄껄이그물버섯류 재분류는 약 270개 표본의 28S rDNA, 번역 신장 인자(tef1), RNA 중합효소 II 둘째 큰 소단위(rpb2) 염기서열을 최대우도법과 베이즈 추론으로 분석했다[27]. 비아워비에자 시료 연구는 ITS1F·ITS4 시발체로 ITS 구간을 증폭해 이웃결합 계통수로 종을 확인했고, 새 서열을 GenBank에 등록했다[3]. 생화학적으로는 이 종의 바시디오리피드 Ls1이 3-α-만노실화된 α-푸코스라는 특이한 당 구조를 가진다고 보고되었다[23]."},
 {"key":"safety","title":"안전성","body":
  "식약처 목록에서 거친껄껄이그물버섯은 자실체에 한해 '사용가능'이다[1]. 국내 공공기관의 알레르기·잔류·독성 정보는 확인하지 못함. 이 종을 날로 또는 덜 익혀 먹은 뒤의 위장 증상 사례는 PubMed에서 확인하지 못함.\n\n중금속 농도는 채집지에 따라 다르다[7, 9]. 폴란드 저지대 다섯 곳의 말린 갓 중앙값은 카드뮴 1.0–5.8, 수은 0.36–0.59, 납 0.20–0.91 mg/kg(건조중)이었고 저자들은 독성 원소가 낮은 편이라고 보았다[7]. 반면 고지대 두 곳의 갓 카드뮴 중앙값은 5.6–6.6 mg/kg 건조중, 개별 최댓값은 14 mg/kg 건조중이었다[9]. 체코 시료의 카드뮴 생물농축계수는 4.7이었다[11]. 폴란드 모래톱 시료에서도 이 종은 수은을 많이 쌓는 쪽이어서 갓의 생물농축계수가 11–35 범위에 든 3종 가운데 하나였다[18]. 수은은 보레츠카 숲 갓 1,200 ± 740 ng/g 건조중, 다른 숲 갓 290 ± 100–370 ± 330 µg/kg 건조중으로 보고되었다[16, 17]. 46년 모니터링 연구는 자주 규칙적으로 먹는 것을 권하지 않았다[12]. 2025년 3종 비교 연구는 측정한 카드뮴·납·니켈이 모두 EU 식품 기준 이내였다고 했다[6]. 스웨덴 비오염지 10종 조사는 버섯 한 끼에서 올 수 있는 카드뮴 최대량이 주간 섭취 한계를 조금 밑돈다고 평가했다[32].\n\n방사성 세슘은 체르노빌 오염지(우크라이나)에서 최대 117 kBq/kg 건조중까지 검출되었다[19]. 희토류는 식이 노출이 크지 않은 수준이었다[33]."},
]

compounds = [
 {"name":"Linoleic acid","name_ko":"리놀레산","class":"다가불포화 지방산","role":"nutrient","part":"자실체(건조 분말, 마이크로파 에틸아세테이트 추출물)","content_text":"추출물 GC-MS 상대 피크 면적 28.4%로 가장 많은 성분(절대 함량 아님)[4]","activity_ko":"저자들은 지방산이 관찰된 α-글루코시데이스 억제에 기여할 것으로 추정했다(시험관)[4]","source":[4]},
 {"name":"Oleic acid","name_ko":"올레산","class":"단일불포화 지방산","role":"nutrient","part":"자실체(에틸아세테이트 추출물)","content_text":"세 분획 모두에서 검출(GC-MS·HRMS), 리놀레산 다음으로 많음; 정량값은 확인하지 못함[4]","activity_ko":"지방산 조성의 주요 성분[4]","source":[4]},
 {"name":"Palmitic acid","name_ko":"팔미트산","class":"포화 지방산","role":"nutrient","part":"자실체(에틸아세테이트 추출물)","content_text":"세 분획 모두에서 검출; 정량값은 확인하지 못함[4]","activity_ko":"지방산 조성의 주요 성분[4]","source":[4]},
 {"name":"Ergosterol","name_ko":"에르고스테롤","class":"스테롤(프로비타민 D2)","role":"bioactive","part":"자실체","content_text":"에틸아세테이트 추출물 LS3 분획에서 유사체(ergosta-7,22-dien-3-ol)와 합쳐 약 14%(상대 피크 면적)[4]; 70 ℃ 건조 시 약 50%·48% 감소(두 종 결과, 절대값은 그림으로만 제시)[5]","activity_ko":"자외선을 받으면 비타민 D2로 바뀌는 전구체[5]","source":[4,5]},
 {"name":"Leccinine A","name_ko":"레시닌 A","class":"피롤 알칼로이드","role":"marker","part":"자실체(에틸아세테이트 추출물)","content_text":"HRMS-ESI로 잠정 동정(정량하지 않음)[4]","activity_ko":"Leccinum 속에 특징적인 2차 대사산물로 소개됨; 소포체 스트레스 세포사 보호 활성은 문헌 인용(이 종 시료로 확인한 것 아님)[4]","source":[4]},
 {"name":"Pyrrolezanthine","name_ko":"피롤레잔틴","class":"피롤 알칼로이드","role":"bioactive","part":"자실체(에틸아세테이트 추출물)","content_text":"HRMS-ESI로 잠정 동정(정량하지 않음)[4]","activity_ko":"저자들은 피롤 알칼로이드가 α-글루코시데이스 억제의 주된 원인일 것으로 추정했다(가설)[4]","source":[4]},
 {"name":"Basidiolipid","name_ko":"바시디오리피드 Ls1(당-이노시톨-인-스핑고지질)","class":"스핑고당지질","role":"bioactive","part":"자실체","content_text":"구조만 규명: Galα-6(Manα-3Fucα-2)Galα-6Galβ-6Manα- 당사슬, 세라마이드는 t18:0 트리히드록시스핑가닌과 α-히드록시 장쇄 지방산; 함량 수치는 초록에 없음[23]","activity_ko":"사람 정상 혈청의 이종친화 항체(IgG2·IgM)가 이 종의 일부 바시디오리피드와 반응했다[24]","source":[23,24]},
 {"name":"Potassium","name_ko":"칼륨","class":"무기질","role":"nutrient","part":"자실체 갓(말린 것)","content_text":"폴란드 저지대 다섯 곳 갓 중앙값 27,000–44,000 mg/kg 건조중[7]","activity_ko":"필수 다량 무기질; 갓·대 모두 생물농축됨[7, 8]","source":[7,8]},
 {"name":"Phosphorus","name_ko":"인","class":"무기질","role":"nutrient","part":"자실체 갓(말린 것)","content_text":"갓 중앙값 6,200–9,100 mg/kg 건조중[7]","activity_ko":"필수 무기질[7]","source":[7]},
 {"name":"Copper","name_ko":"구리","class":"무기질","role":"nutrient","part":"자실체 갓(말린 것)","content_text":"갓 중앙값 15–27 mg/kg 건조중[7]; 체코 시료 생물농축계수 1.7[11]","activity_ko":"46년 모니터링 연구에서 구리의 식이 공급원으로 평가됨[12]","source":[7,11,12]},
 {"name":"Zinc","name_ko":"아연","class":"무기질","role":"nutrient","part":"자실체 갓(말린 것)","content_text":"갓 중앙값 130–270 mg/kg 건조중[7]","activity_ko":"필수 미량 무기질[7]","source":[7]},
 {"name":"Rubidium","name_ko":"루비듐","class":"무기질(알칼리 금속)","role":"bioactive","part":"자실체 갓(말린 것)","content_text":"갓 중앙값 90–320 mg/kg 건조중[7]; 체코 시료 생물농축계수 5.5[11]","activity_ko":"칼륨과 함께 많이 쌓이는 원소[7, 11]","source":[7,11]},
 {"name":"Selenium","name_ko":"셀레늄","class":"무기질","role":"nutrient","part":"자실체(갓·대)","content_text":"폴란드 시료에서 그물버섯(B. edulis)·큰갓버섯·광대버섯보다 훨씬 적었다는 비교만 초록에 있음; 수치는 확인하지 못함[15]; 체코 시료 생물농축계수 2.0[11]","activity_ko":"필수 미량 무기질[15]","source":[15,11]},
 {"name":"Polyphenols","name_ko":"총폴리페놀","class":"페놀 화합물(총량)","role":"bioactive","part":"자실체(생것)","content_text":"100 mg/100 g 생중량을 넘는 5종 가운데 하나; TEAC 2.3 mmol/100 g 생중량 초과, FRAP 1 mmol/100 g 초과[22]","activity_ko":"야생 식용버섯 16종 비교에서 항산화능이 높은 편(시험관)[22]","source":[22]},
]

assays = [
 {"role":"literature","compound":"Ergosterol","compound_ko":"에르고스테롤","part":"자실체(폴란드 비엘코폴스카 야생 시료, 생것과 20·40·70 ℃ 건조물)",
  "content":"생시료에서 가장 높고 70 ℃ 건조 시 약 50%·48% 감소(이 종과 노루궁뎅이 두 종의 값; 절대 함량은 그림으로만 제시되어 확인하지 못함)[5]",
  "method":"UPLC-PDA",
  "conditions":{"instrument":"ACQUITY UPLC H-Class System + PDA eλ 검출기(Waters)","column":"ACQUITY UPLC HSS T3 C18, 150 mm × 2.1 mm, 1.8 µm (전처리 칼럼 ACQUITY UPLC BEH C18 VanGuard, 1.7 µm)","mobile_phase":"메탄올:아세토니트릴:물 = 85:10:5 (v/v/v)","gradient":"등용매(isocratic)","flow":"0.5 mL/min","temp":"","detection":"PDA(검출 파장 원문에 없음)","injection":"","sample_prep":"시료에 메탄올과 2 M NaOH를 넣어 마이크로파로 15초씩 2회 조사, 식힌 뒤 1 M HCl로 중화하고 펜테인으로 3회 추출","standard":"","linearity":"","lod":"","loq":"","recovery":""},
  "rationale":"버섯 세포막의 주된 스테롤이자 비타민 D2 전구체로, 건조 조건에 따른 품질 변화를 보여 주는 지표로 쓰였다[5]. 원문 텍스트에서 종 이름이 빠져 두 감소율 중 어느 쪽이 이 종인지 확인하지 못함.",
  "source":[5],"url":"https://pubmed.ncbi.nlm.nih.gov/32116361/","source_kind":"paper"},
 {"role":"literature","compound":"Phenolic acids (gallic, caffeic, chlorogenic, ferulic, 4-hydroxybenzoic, syringic, vanillic acid 등)","compound_ko":"페놀산(갈산·카페산·클로로젠산·페룰산·4-히드록시벤조산·시링산·바닐산 등)","part":"자실체(생것과 건조물)",
  "content":"건조 온도가 오를수록 대부분의 페놀산이 2–37배 줄었다는 결과가 보고됨; 원문 텍스트에서 종 이름이 빠져 이 종의 개별 함량은 확인하지 못함[5]",
  "method":"UPLC-PDA",
  "conditions":{"instrument":"ACQUITY UPLC H-Class System + PDA eλ 검출기(Waters)","column":"Acquity UPLC BEH C18, 2.1 mm × 150 mm, 1.7 µm","mobile_phase":"물과 아세토니트릴(둘 다 0.1% 폼산, pH 2)","gradient":"기울기 용리(세부 프로그램 원문에 없음)","flow":"0.4 mL/min","temp":"35 ℃","detection":"PDA 280 nm·320 nm","injection":"","sample_prep":"생시료는 균질화, 건조 시료는 분쇄 후 80% 메탄올로 12시간 진탕 추출, 3000 rpm 원심분리, 40 ℃ 감압 건고 후 80% 메탄올 1 mL에 재용해","standard":"외부 표준법(표준품 머무름 시간 비교·첨가 확인)","linearity":"","lod":"","loq":"","recovery":""},
  "rationale":"이 종의 페놀 조성과 건조에 따른 손실을 정량한 분석이다[5]. 검출한계·정량한계·회수율은 원문에 없다[5].",
  "source":[5],"url":"https://pubmed.ncbi.nlm.nih.gov/32116361/","source_kind":"paper"},
 {"role":"literature","compound":"Fatty acids and sterols (linoleic acid, ergosterol 등 GC-MS 프로파일)","compound_ko":"지방산·스테롤(리놀레산·에르고스테롤 등 GC-MS 프로파일)","part":"자실체 건조 분말(비아워비에자 숲 시료)",
  "content":"리놀레산 28.4%, 3,5-비스(1,1-디메틸에틸)-4-히드록시벤젠프로판산 옥타데실 에스터 19%, 에르고스테롤+유사체 약 14%(LS3 분획) — 모두 상대 피크 면적[4]",
  "method":"GC-MS (EI)",
  "conditions":{"instrument":"GC-MS(제조사·모델 원문 텍스트에 없음)","column":"HP-5MS 모세관 칼럼, 30 m × 0.25 mm, 막 두께 0.25 μm (Agilent)","mobile_phase":"운반 기체 헬륨","gradient":"70 ℃ 3분 유지 → 3 ℃/min로 280 ℃ → 20분 유지","flow":"1.5 mL/min(일정 유량)","temp":"주입구 250 ℃, 검출부 230 ℃","detection":"EI 70 eV, m/z 30–400","injection":"1 μL, 분할비 1:100","sample_prep":"분말 70 mg을 에틸아세테이트 2.1 mL(1:30)에 넣고 80 ℃에서 5분 마이크로파 추출, 여과·원심분리(8000 rpm, 10분)·감압 건고; 조추출물 65.6 mg을 실리카겔 칼럼(에틸아세테이트/헥세인 2:8)으로 세 분획(LS1–LS3)으로 나눔","standard":"NIST 11 질량 스펙트럼 라이브러리와 비교(유사도 80% 이상만 채택)","linearity":"","lod":"","loq":"","recovery":""},
  "rationale":"가장 강한 α-글루코시데이스 억제를 보인 추출물의 성분 조성을 밝히려 쓴 정성·반정량 분석이다[4]. 표준품 정량이 아니어서 직선성·검출한계·회수율은 없다[4].",
  "source":[4],"url":"https://pubmed.ncbi.nlm.nih.gov/39452670/","source_kind":"paper"},
 {"role":"literature","compound":"Mercury and other elements (Ag, Cd, Cu, Hg, K, P, Pb, Rb, Zn 등)","compound_ko":"수은 및 무기 원소","part":"자실체 갓·대(말린 것)",
  "content":"세 발생 철에 걸쳐 Cd·Cu·Hg·K·Mg·Na·P·Rb·Zn은 생물농축계수 1 초과, Al·Ba·Ca·Co·Fe·Mn·Ni·Pb·Sr은 뚜렷한 축적 없음[8]",
  "method":"ICP-OES(초음파 교차흐름 분무기), 총수은은 냉증기 원자흡광법(CV-AAS)",
  "conditions":{},
  "rationale":"이 종은 수은·카드뮴 축적이 식품 안전의 핵심 문제여서 원소 분석이 가장 많이 쓰였다[8, 9]. 전문 확인 못함 — 장비 조건은 비워 둠[8].",
  "source":[8,9],"url":"https://pubmed.ncbi.nlm.nih.gov/30388922/","source_kind":"paper"},
]

nutrients = [
 {"form":"자실체 건조 분말(비아워비에자 숲 야생 시료, 이탈리아 시험기관 분석; 국가표준식품성분표 값 아님)","basis":"건조 시료(본문 값; 원문 표는 확인하지 못해 기준량은 본문 표기대로)","items":[
   {"name":"에너지","value":1361,"unit":"kJ"},
   {"name":"총당류","value":2.964,"unit":"g/100 g"},
   {"name":"총 유리 아미노산","value":5.31,"unit":"g/100 g"},
   {"name":"다가불포화 지방산","value":1.98,"unit":"g/100 g"},
   {"name":"포화 지방산","value":0.523,"unit":"g/100 g"}],"source":[3]},
 {"form":"자실체 갓(폴란드 저지대 다섯 곳, 말린 것)","basis":"건조중 1 kg당 중앙값 범위","items":[
   {"name":"칼륨","value":"27,000–44,000","unit":"mg/kg"},
   {"name":"인","value":"6,200–9,100","unit":"mg/kg"},
   {"name":"마그네슘","value":"880–1,000","unit":"mg/kg"},
   {"name":"칼슘","value":"48–210","unit":"mg/kg"},
   {"name":"철","value":"38–140","unit":"mg/kg"},
   {"name":"아연","value":"130–270","unit":"mg/kg"},
   {"name":"구리","value":"15–27","unit":"mg/kg"},
   {"name":"망가니즈","value":"5.3–27","unit":"mg/kg"}],"source":[7]},
]

d = {
 "slug":"leccinum-scabrum","name_ko":"거친껄껄이그물버섯","name_en":"Birch bolete (brown birch scaber stalk)",
 "scientific_name":"Leccinum scabrum (Bull.) Gray",
 "aliases":["Leccinum scabrum (Bull.:Fr.) S.F.Gray","Boletus scaber Bull.","birch bolete","brown birch bolete","brown birch scaber stalk","common scaber stalk","rough-stemmed bolete"],
 "sections":sections,"compounds":compounds,"markers":[],"assays":assays,"nutrients":nutrients,
 "production":[],"world":[],"gi":[],"orgs":[],"sources":sources}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
print("ok")
