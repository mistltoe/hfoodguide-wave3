import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
A = "2026-11-02"
def pm(n, title, doi, pmid, pmc=None, note=""):
    ids = f"PMID {pmid}" + (f", {pmc}" if pmc else "")
    return {"n": n, "title": f"{title} ({ids}{note})", "url": f"https://doi.org/{doi}" if doi else f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/", "publisher": "PubMed", "accessed": A}
S = [
 {"n": 1, "title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 캥거루지육·캥거루식용부산물: 식품원료(A코드)·축,수산물 외 동물·사용가능, 학명 칸 'Macropus giganteus / Macropus rufus / Macropus fuliginosus / Macropus robustus / Macropus rufogriseus rufogriseus', 부위 칸 '씨앗'(캥거루지육)·'꽃꿀'(캥거루식용부산물), 사용 조건 '사용가능부위 : 지육(꼬리포함)'; 대조: 낙타고기('수액')·낙타식용부산물('꽃꿀') 행 (로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json)", "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
 pm(2, "Effects on plasma lipids and fatty acid composition of very low fat diets enriched with fish or kangaroo meat — Lipids 1987;22(7):523-9", "10.1007/BF02540369", "3626779", note=", 초록만 확인"),
 pm(3, "The effects of very low fat diets enriched with fish or kangaroo meat on cold-induced vasoconstriction and platelet function — Prostaglandins Leukot Essent Fatty Acids 1990;39(3):221-6", "10.1016/0952-3278(90)90076-w", "2110678", note=", 초록만 확인"),
 pm(4, "The effects of low-fat diets rich in arachidonic acid on the composition of plasma fatty acids and bleeding time in Australian aborigines — J Nutr Sci Vitaminol 1985;31(4):441-53", "10.3177/jnsv.31.441", "3935761", note=", 초록만 확인"),
 pm(5, "Short-term diets rich in arachidonic acid influence plasma phospholipid polyunsaturated fatty acid levels and prostacyclin and thromboxane production in humans — J Nutr 1996;126(4 Suppl):1110S-4S", "10.1093/jn/126.suppl_4.1110S", "8642442", note=", 초록만 확인"),
 pm(6, "[The biological function of L-carnitine and its content in the particular food examples] — Przegl Lek 2013;70(2):85-91 (폴란드어 리뷰, 영문 초록)", None, "23879010", note=", 초록만 확인"),
 pm(7, "Vitamin D composition of Australian game products — Food Chem 2022;387:132965", "10.1016/j.foodchem.2022.132965", "35429940", note=", 초록만 확인"),
 pm(8, "Vitamin D content of wild-caught traditional foods collected on Nyoongar Country in Western Australia — Food Chem 2025;496:146938", "10.1016/j.foodchem.2025.146938", "41197327", note=", 초록만 확인"),
 pm(9, "Use of histidine dipeptides and myoglobin to monitor adulteration of cooked beef with meat from other species — Aust Vet J 1985;62(8):272-6", "10.1111/j.1751-0813.1985.tb14250.x", "4062740", note=", 초록만 확인"),
 pm(10, "Differentiation of meat according to species by the electrophoretic separation of muscle lactate dehydrogenase and esterase isoenzymes and isoelectric focusing of soluble muscle proteins — Aust Vet J 1983;60(2):47-51", "10.1111/j.1751-0813.1983.tb05861.x", "6838437", note=", 초록만 확인"),
 pm(11, "Evaluation of post-polymerase chain reaction melting temperature analysis for meat species identification in mixed DNA samples — J Agric Food Chem 2006;54(21):7973-8", "10.1021/jf0615045", "17031997", note=", 초록만 확인"),
 pm(12, "Polymerase chain reaction-restriction fragment length polymorphism analysis: a simple method for species identification in food — J AOAC Int 1995;78(6):1542-51", None, "8664595", note=", 초록만 확인"),
 pm(13, "Toxoplasma gondii in Australian macropods (Macropodidae) and its implication to meat consumption — Int J Parasitol Parasites Wildl 2021;16:153-162 (문헌 리뷰, 회색문헌 포함)", "10.1016/j.ijppaw.2021.09.004", "34567970", "PMC8449172", note=", 전문 확인"),
 pm(14, "An outbreak of Salmonella Muenchen gastroenteritis after consuming wild hunted kangaroo, Northern Territory, Australia, 2024 — Commun Dis Intell 2025;49", "10.33321/cdi.2025.49.010", "39965608", note=", 초록만 확인"),
 pm(15, "Microbial profiles of carcasses and minced meat from kangaroos processed in South Australia — Int J Food Microbiol 2007;123(1-2):88-92", "10.1016/j.ijfoodmicro.2007.12.007", "18234385", note=", 초록만 확인"),
 pm(16, "A survey of the microbiological quality of kangaroo carcasses processed for human consumption in two processing plants in Queensland, Australia — J Food Prot 2007;70(5):1249-51", "10.4315/0362-028x-70.5.1249", "17536688", note=", 초록만 확인"),
 pm(17, "Prevalence of Salmonella in fecal samples of western grey kangaroos (Macropus fuliginosus) — J Wildl Dis 2011;47(4):880-7", "10.7589/0090-3558-47.4.880", "22102658", note=", 초록만 확인"),
 pm(18, "Seroprevalence of Toxoplasma gondii in wild kangaroos using an ELISA — Parasitol Int 2009;58(2):161-5", "10.1016/j.parint.2009.01.008", "19567231", "PMC2784248", note=", 초록만 확인"),
 pm(19, "Changing patterns of meat consumption and greenhouse gas emissions in Australia: Will kangaroo meat make a difference? — PLoS One 2017;12(2):e0170130", "10.1371/journal.pone.0170130", "28196141", "PMC5308823", note=", 전문 확인"),
 pm(20, "Decreasing methane yield with increasing food intake keeps daily methane emissions constant in two foregut fermenting marsupials, the western grey kangaroo and red kangaroo — J Exp Biol 2015;218(Pt 21):3425-34", "10.1242/jeb.128165", "26538176", note=", 초록만 확인"),
 pm(21, "Genome sequence of an Australian kangaroo, Macropus eugenii, provides insight into the evolution of mammalian reproduction and development — Genome Biol 2011;12(8):R81", "10.1186/gb-2011-12-8-r81", "21854559", "PMC3277949", note=", 초록만 확인"),
 pm(22, "The complete mitochondrial genome of the eastern grey kangaroo (Macropus giganteus) — Mitochondrial DNA A 2016;27(2):1366-7", "10.3109/19401736.2014.947583", "25103427", note=", 초록만 확인"),
 pm(23, "Inferring kangaroo phylogeny from incongruent nuclear and mitochondrial genes — PLoS One 2013;8(2):e57745", "10.1371/journal.pone.0057745", "23451266", "PMC3579791", note=", 초록만 확인"),
 pm(24, "Diversification of kangaroos and broader turnover among marsupial terrestrial herbivores coincided with emerging aridification then incipient grasslands — Mol Phylogenet Evol 2026;217:108543", "10.1016/j.ympev.2026.108543", "41519248", note=", 초록만 확인"),
 pm(25, "Differences in postprandial inflammatory responses to a 'modern' v. traditional meat meal: a preliminary study — Br J Nutr 2010;104(5):724-8", "10.1017/S0007114510001042", "20377925", note=", 초록만 확인"),
 pm(26, "Anaphylaxis to kangaroo meat: identification of a new marsupial allergen — Allergy 2007;62(2):209-11 (증례 보고, 초록 없음·제목만 확인)", "10.1111/j.1398-9995.2006.01274.x", "17298433"),
 pm(27, "Weathering the storm: Most maternal and environmental drivers of individual reproductive success do not scale up to population recruitment in a large herbivore — J Anim Ecol 2026", "10.1111/1365-2656.70341", "42687635", note=", 초록만 확인"),
 pm(28, "Aerobic characteristics of red kangaroo skeletal muscles — J Exp Biol 2004;207(Pt 16):2811-21", "10.1242/jeb.01115", "15235010", note=", 초록만 확인"),
 pm(29, "Microbiological conditions of meats from large game animals and birds — Meat Sci 2007;77(2):149-60 (리뷰)", "10.1016/j.meatsci.2007.03.007", "22061585", note=", 초록만 확인"),
 pm(30, "Meat quality attributes of Agile Wallabies — Meat Sci 2017;133:173-179", "10.1016/j.meatsci.2017.06.016", "28697421", note=", 초록만 확인"),
 pm(31, "Scaling of the ankle extensor muscle-tendon units and the biomechanical implications for bipedal hopping locomotion in the post-pouch kangaroo Macropus fuliginosus — J Anat 2017;231(6):921-930", "10.1111/joa.12715", "29034479", "PMC5696142", note=", 초록만 확인"),
 pm(32, "The isolation of Salmonella from kangaroos and feral pigs processed for human consumption — Aust Vet J 1991;68(3):106-7", "10.1111/j.1751-0813.1991.tb00766.x", "2043082", note=", 초록만 확인"),
 pm(33, "Where is the game? Wild meat products authentication in South Africa: a case study — Investig Genet 2013;4(1):6", "10.1186/2041-2223-4-6", "23452350", "PMC3621286", note=", 초록만 확인"),
 pm(34, "Shedding light on the microbial community of the macropod foregut using 454-amplicon pyrosequencing — PLoS One 2013;8(4):e61463", "10.1371/journal.pone.0061463", "23626688", "PMC3634081", note=", 초록만 확인"),
 pm(35, "Effectiveness of inactivation of foodborne pathogens during simulated home pan frying of steak, hamburger or meat strips — Int J Food Microbiol 2015;206:118-29", "10.1016/j.ijfoodmicro.2015.04.014", "26004267", note=", 초록만 확인"),
 pm(36, "Digastric muscle of the kangaroo: a comparative anatomical study — Anat Rec 1998;251(3):346-50 (common wallaroo, Macropus robustus 표기)", "10.1002/(SICI)1097-0185(199807)251:3<346::AID-AR10>3.0.CO;2-O", "9669762", note=", 초록만 확인"),
]

secs = [
("overview", "한눈에 보기", """캥거루식용은 식약처 「식품원료 목록」에 오른 캥거루 고기 원료이고, 대표 학명은 동부회색캥거루(Macropus giganteus)다[1]. 목록에는 '캥거루지육'과 '캥거루식용부산물' 두 행이 식품원료(A코드)·축,수산물 외 동물·사용가능으로 실려 있다[1]. 두 행 모두 학명 칸에 Macropus giganteus, M. rufus, M. fuliginosus, M. robustus, M. rufogriseus rufogriseus 다섯 이름이 함께 적혀 있어, 한 종이 아니라 여러 캥거루·왈라비의 고기를 묶은 원료로 읽힌다[1]. 사용 조건 칸은 두 행 모두 '사용가능부위 : 지육(꼬리포함)'이다[1]. 원자료 부위 칸에는 캥거루지육 행에 '씨앗', 캥거루식용부산물 행에 '꽃꿀'이 적혀 있는데, 같은 목록의 낙타고기('수액')·낙타식용부산물('꽃꿀') 같은 다른 동물 행에도 식물 부위 낱말이 보이므로 여기서는 표기를 그대로 옮기고 실제 사용 범위는 사용 조건 칸('지육(꼬리포함)')을 함께 본다[1].

호주에서는 야생 캥거루를 상업적으로 사냥해 사람 식용과 반려동물 사료로 쓰고, 지방이 적은 붉은 고기로 사람 소비가 늘고 있다[13, 19]. 1980년대 식이 연구에서 캥거루 고기는 리놀레산과 아라키돈산이 많은 지방원으로 쓰였다[2, 3]. 이 원료를 원재료로 하는 건강기능식품 고시형 원료는 확인하지 못함."""),
("history", "역사", """캥거루는 호주 원주민의 전통 식량이며, 서호주 원주민이 전통·현대 방식으로 손질한 캥거루 고기와 내장을 분석한 연구가 2025년에 나왔다[8]. 1985년 연구에서는 원주민 참여자가 열대 해산물 식단 2주 뒤 캥거루와 민물고기를 주 지방원으로 하는 저지방 식단을 3주 먹었다[4]. 1987년과 1990년에는 하루 500 g의 캥거루 고기를 넣은 초저지방 식단을 생선 식단·채식 식단과 비교한 소규모 시험이 발표됐다[2, 3]. 2010년 건강한 성인 10명의 교차 예비시험에서는 캥거루 고기 100 g을 먹은 뒤 1–2시간의 혈중 중성지방·IL-6·TNF-α가 와규 소고기를 먹은 뒤보다 낮았으나, 섭취 열량을 맞추지 않은 예비 연구였다[25].

1980년대 호주에서는 소고기 제품에 다른 고기가 섞이는 문제가 있어, 전기영동으로 붉은캥거루와 회색캥거루 고기를 구별하거나 히스티딘 디펩타이드 비율로 캥거루 고기 혼입을 가려내는 방법이 개발됐다[9, 10]. 과거에는 캥거루 고기가 주로 반려동물 사료로 쓰였지만, 지방이 적은 붉은 고기로 인정받으면서 사람 소비가 늘어 많은 대형마트에 따로 진열대가 생겼다고 2017년 논문은 적는다[19]. 2020년 11월 개정된 호주 상업 사냥 규약에서는 상업 목적 사냥 대상이 일곱 번째 종까지 늘었다[13]. 국내 수입·유통 이력은 확인하지 못함."""),
("biology", "동물학적 특징", """캥거루는 캥거루과(Macropodidae)에 속하는 유대류로, 새끼가 어미 주머니에서 자란다[21, 27]. 동부회색캥거루 개체군을 18년 동안 추적한 연구에서는 번식 시기가 개체마다 달라(비동시 번식) 주머니 안에서는 어미의 특성이, 주머니를 나온 뒤에는 환경 조건이 새끼 생존에 더 크게 작용했다[27]. 큰 캥거루는 두 뒷다리로 뛰면서 발목 힘줄에 탄성 에너지를 저장해 이동 효율을 높이며, 주머니를 나온 서부회색캥거루의 체중 범위는 5.8–70.5 kg로 보고됐다[31].

붉은캥거루의 골격근은 체중의 약 50%를 차지하고 골반과 허리 둘레에 몰려 있으며, 주요 이동 근육의 미토콘드리아 부피 밀도는 8.8–10.6%였다[28]. 캥거루는 앞위(전위)에서 먹이를 발효하는 초식동물이고, 서부회색·붉은캥거루의 체중당 메테인 생성량은 반추동물의 약 27% 수준으로 측정됐다[20]. 붉은캥거루·동부회색캥거루·왈라루의 앞위 세균 군집은 종마다 유의하게 달랐다[34]."""),
("related_species", "가까운 종·혼동", """식품원료 목록의 학명 칸에는 동부회색캥거루(M. giganteus)와 함께 붉은캥거루(M. rufus), 서부회색캥거루(M. fuliginosus), 왈라루(M. robustus), M. rufogriseus rufogriseus가 적혀 있다[1, 20, 36]. 붉은캥거루·서부회색캥거루의 영문 이름은 메테인 연구에서, 왈라루(common wallaroo)는 해부 연구에서 확인했다[20, 36]. M. rufogriseus rufogriseus의 일반명은 이 조사에서 원문으로 확인하지 못함.

분류는 바뀌는 중이다: 2013년 연구는 큰 초식 캥거루와 왈라루를 Macropus 속 안의 아속 M. (Macropus)·M. (Osphranter)로, 작은 왈라비를 M. (Notamacropus)로 나눴다[23]. 2026년 연구는 Macropus, Osphranter, Wallabia, Notamacropus를 따로 이름 붙인 'Macropus' 무리로 다뤄, 목록의 옛 학명과 최근 논문의 학명이 다를 수 있다[24]. 어느 종이 어느 속으로 옮겨졌는지는 초록만으로 종별로 확인하지 못함.

게놈 연구에 쓰인 태머왈라비(M. eugenii)와 고기 품질이 연구된 아자일왈라비(M. agilis)는 목록에 없는 종이므로 그 자료를 이 원료에 그대로 옮기지 않는다[21, 30]."""),
("cultivation", "사냥·수급", """캥거루 고기는 사육이 아니라 야생 개체를 사냥해서만 얻는다[29]. 호주는 개체 수가 많아 목초지와 생태계에 부담이 되는 일부 캥거루 종의 사냥을 허용하고, 상업 사냥 규약에서 대상 종을 정하며, '판매용 사체나 가죽을 얻기 위해 쏘는 것'을 상업 목적으로 정의한다[13]. 모든 종이 모든 주에서 사냥되는 것은 아니며, 대부분은 외딴 지역이 아니라 목축지 등 사람 거주지 가까이에서 잡힌다[13].

사냥 고기는 총알 위치, 현장 내장 제거, 상온 숙성 때문에 미생물 상태가 나빠질 수 있다[29]. 남호주와 퀸즐랜드의 가공장에서 사체와 다진 고기의 위생 상태가 조사됐다[15, 16]. 2021년 리뷰는 회색문헌을 인용해 해마다 약 3,000톤의 캥거루 고기가 60개국으로 수출되고 그중 75%가 반려동물 사료로 쓰인다고 적었다[13]. 2017년 논문은 호주 1인당 캥거루 고기 소비량을 2020년 0.77 kg, 2025년 0.99 kg로 추정했다[19]. 연도별 사냥 할당량·실제 사냥 수는 공식 원문을 열지 못해 확인하지 못함. 국내 생산 통계는 해당 없음을 포함해 확인하지 못함."""),
("processing", "가공·제품", """남호주 가공장 조사에서 사체 표면 총균수 평균은 2002년 2.3 log10 cfu/cm², 2004년 1.2 log10 cfu/cm²였다[15]. 같은 조사에서 다진 캥거루 고기의 총균수 평균은 3.9 log10 cfu/g였고 살모넬라가 50건 중 9건(18%)에서 나왔다[15]. 복강은 오염이 심해 대장균이 46%, 살모넬라가 12%에서 검출됐다[15]. 퀸즐랜드 두 가공장의 근육 836건에서는 호기성 세균 평균 2.8 log CFU/g, 대장균 검출 13.9%, 살모넬라 0.84%였다[16]. 1991년 조사에서는 캥거루 사체의 약 11%가 살모넬라에 오염돼 있었다[32].

가정에서 팬에 굽는 실험에서 캥거루를 포함한 스테이크는 '완전히 익힘'에서도 18%, 덜 익힌 경우 90%에서 접종한 병원균이 살아남았다[35]. 수출 고기는 냉동 상태로 나가 위험이 크게 줄지만, 소비자는 냉동육을 덜 선호한다고 2021년 리뷰는 적었다[13].

캥거루 고기 판별에는 근육 안세린·카르노신 비율 HPLC, 전기영동, 사이토크롬 b 유전자 PCR-RFLP, 실시간 PCR이 쓰였다[9–12]. 남아프리카 야생고기 제품 조사에서는 다른 종으로 표시된 제품에서 캥거루가 검출됐다[33]."""),
("genetics", "유전체·종 판별", """캥거루과에서 처음 해독된 핵게놈은 태머왈라비(M. eugenii)이며, Sanger 방식 2배 깊이에 차세대 염기서열과 물리·연관 지도를 더해 조립했다[21]. 이 종은 식품원료 목록의 학명 칸에 없으므로 동부회색캥거루의 게놈으로 보지 않는다[1, 21]. 동부회색캥거루는 미토콘드리아 전체 게놈(등록번호 LK995454)이 해독됐고, 단백질 유전자 13개, tRNA 유전자 22개, rRNA 유전자 2개를 가진다[22].

미토콘드리아와 핵 유전자의 계통이 서로 어긋나는 사례가 있어, 2013년 연구는 불완전 계통 분류와 왈라루에서 흑장갑왈라비로의 미토콘드리아 유입을 설명으로 들었다[23]. 2026년 연구는 캥거루아과의 분화가 약 850만 년 전부터 건조화와 함께 일어났다고 추정했다[24].

고기 종 판별에서는 사이토크롬 b 유전자 PCR-RFLP가 양념·가열 제품 속 캥거루를 다른 사냥고기와 구별했다[12]. 실시간 PCR 융해곡선 분석에서 왈라루 DNA 검출한계는 0.04 pg였다[11]. 붉은캥거루와 회색캥거루 고기는 등전점 전기영동으로도 구별됐다[10]."""),
("safety", "안전성", """식약처 「식품원료 목록」은 이 원료를 사용가능으로 분류하고 사용 부위를 '지육(꼬리포함)'으로 정한다[1]. 식약처의 캥거루 고기 알레르기·잔류물질 안전정보는 확인하지 못함.

톡소포자충은 사냥되는 모든 캥거루 종에서 항체 양성이 보고됐다[13]. 서호주 퍼스 지역 서부회색캥거루 219마리 중 15.5%가 항체 양성이었다[18]. 1995년에는 덜 익힌 캥거루 고기와 관련된 것으로 보이는 톡소포자충증 12건(선천 감염 1건 포함)이 보고됐다고 2021년 리뷰는 적었다[13]. 같은 리뷰는 호주 공식 기준에 캥거루 고기의 병원체 검사가 포함되지 않는다고 적었다[13].

2024년 호주 노던준주에서는 사냥한 캥거루 한 마리를 나눠 먹은 7명이 모두 살모넬라 위장염에 걸렸고 2명이 입원했다[14]. 원인은 위생적이지 않은 도축·보관·운반과 덜 익힌 조리로 추정됐다[14]. 야생 서부회색캥거루 분변의 살모넬라 검출률은 3.6%였고, 연구진은 위생적인 내장 제거와 충분한 가열을 권했다[17]. 캥거루 고기 섭취 뒤 아나필락시스가 생긴 증례에서 새로운 유대류 알레르겐이 보고됐다[26]."""),
]
sections = [{"key": k, "title": t, "body": b} for k, t, b in secs]

compounds = [
 {"name": "Arachidonic acid", "name_ko": "아라키돈산", "class": "지방산(n-6 장쇄 다중불포화)", "role": "nutrient", "part": "근육(생고기)", "content_text": "생고기 500 g/일 식단이 아라키돈산 305 mg/일 제공[5]; 캥거루 고기는 리놀레산·아라키돈산이 많음[2, 3]", "activity_ko": "이 식단을 먹은 사람의 혈장 인지질 아라키돈산 비율이 올라감(소규모 식이 시험)[2, 5]", "source": [2, 3, 5]},
 {"name": "Linoleic acid", "name_ko": "리놀레산", "class": "지방산(n-6 다중불포화)", "role": "nutrient", "part": "근육", "content_text": "함량 수치 확인하지 못함; '리놀레산과 아라키돈산이 많은' 고기로 기술[2, 3]", "activity_ko": "필수지방산", "source": [2, 3]},
 {"name": "Eicosapentaenoic acid", "name_ko": "에이코사펜타엔산(EPA)", "class": "지방산(n-3 장쇄)", "role": "nutrient", "part": "근육(생고기)", "content_text": "생고기 500 g/일 식단의 n-3 장쇄 다중불포화지방산 합계 325 mg/일(개별 EPA 값 확인하지 못함)[5]", "activity_ko": "식단 뒤 혈청 인지질 EPA 증가[5]", "source": [5]},
 {"name": "Docosapentaenoic acid", "name_ko": "도코사펜타엔산(DPA, 22:5 n-3)", "class": "지방산(n-3 장쇄)", "role": "nutrient", "part": "근육(생고기)", "content_text": "개별 함량 확인하지 못함; n-3 장쇄 합계 325 mg/500 g 생고기[5]", "activity_ko": "식단 뒤 혈청 인지질 22:5(n-3) 증가[5]", "source": [5]},
 {"name": "Levocarnitine", "name_ko": "L-카르니틴", "class": "아미노산 유도체", "role": "bioactive", "part": "고기", "content_text": "637 mg/100 g 건물(말고기 423 mg, 소고기 139 mg과 비교)[6]", "activity_ko": "장쇄 지방산을 미토콘드리아로 운반(일반 생리 기능)[6]", "source": [6]},
 {"name": "Cholecalciferol", "name_ko": "비타민 D3", "class": "비타민", "role": "nutrient", "part": "생고기·내장", "content_text": "2022년 생고기: 검출되지 않음[7]; 2025년 서호주 고기·내장: 평균 0.1 μg/100 g 초과 없음[8]", "activity_ko": "캥거루 고기는 비타민 D 공급원으로 보기 어려움[7, 8]", "source": [7, 8]},
 {"name": "Ergocalciferol", "name_ko": "비타민 D2", "class": "비타민", "role": "nutrient", "part": "생고기", "content_text": "일부 캥거루 시료에서 검출(수치 확인하지 못함)[7]", "activity_ko": "", "source": [7]},
 {"name": "Calcifediol", "name_ko": "25-하이드록시비타민 D3", "class": "비타민 대사체", "role": "nutrient", "part": "생고기", "content_text": "캥거루만 검출되지 않음(다른 사냥고기는 검출)[7]", "activity_ko": "", "source": [7]},
 {"name": "25-Hydroxyergocalciferol", "name_ko": "25-하이드록시비타민 D2", "class": "비타민 대사체", "role": "nutrient", "part": "생고기", "content_text": "일부 낙타·캥거루 시료에서 미량[7]", "activity_ko": "", "source": [7]},
 {"name": "Anserine", "name_ko": "안세린", "class": "히스티딘 디펩타이드", "role": "marker", "part": "골격근", "content_text": "함량 수치 확인하지 못함; 안세린/카르노신 비율이 양·소·말·캥거루 사이에서 크게 다름[9]", "activity_ko": "고기 종 판별(혼입 검사) 지표[9]", "source": [9]},
 {"name": "Carnosine", "name_ko": "카르노신", "class": "히스티딘 디펩타이드", "role": "marker", "part": "골격근", "content_text": "함량 수치 확인하지 못함[9]", "activity_ko": "안세린과의 비율로 종 판별[9]", "source": [9]},
 {"name": "Myoglobin", "name_ko": "미오글로빈", "class": "근육 단백질", "role": "marker", "part": "골격근", "content_text": "함량 확인하지 못함; SDS 겔 전기영동 이동도로 혼입 종 확정[9]", "activity_ko": "종 판별 보조 지표[9]", "source": [9]},
]

assays = [
 {"role": "literature", "compound": "Anserine/carnosine ratio", "compound_ko": "안세린·카르노신 비율", "part": "조리한 고기(골격근)", "content": "비율만 보고, 함량 수치 확인하지 못함[9]", "method": "HPLC(양이온교환)",
  "conditions": {"instrument": "", "column": "Partisil-10 SCX", "mobile_phase": "0.2 M lithium formate, pH 2.9", "gradient": "", "flow": "", "temp": "", "detection": "", "injection": "", "sample_prep": "", "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "두 히스티딘 디펩타이드의 비율이 양·소·말·캥거루 사이에서 크게 달라 소고기 제품의 캥거루 고기 혼입을 빠르게 가려낸다; 칼럼·이동상은 초록에서 확인, 전문 확인 못함[9]", "source": [9], "url": "https://doi.org/10.1111/j.1751-0813.1985.tb14250.x", "source_kind": "paper"},
 {"role": "literature", "compound": "Vitamin D3, 25-hydroxyvitamin D3, vitamin D2, 25-hydroxyvitamin D2", "compound_ko": "비타민 D3·D2와 25-하이드록시 대사체", "part": "생고기", "content": "D3·25(OH)D3 검출되지 않음, D2 일부 시료 검출, 25(OH)D2 일부 미량[7]", "method": "LC-QQQ(액체크로마토그래피-삼중사중극자 질량분석)",
  "conditions": {"instrument": "LC-QQQ", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "삼중사중극자 질량분석", "injection": "", "sample_prep": "", "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "사냥고기의 비타민 D 자료가 부족해 원주민 식품 영양 평가용으로 정량했다; 전문 확인 못함[7]", "source": [7], "url": "https://doi.org/10.1016/j.foodchem.2022.132965", "source_kind": "paper"},
 {"role": "literature", "compound": "Mitochondrial cytochrome b DNA (wallaroo)", "compound_ko": "미토콘드리아 사이토크롬 b DNA(왈라루)", "part": "고기·식품", "content": "검출한계 0.04 pg(단일 반응); 소·왈라루 혼합에서 각 5%까지 융해 피크 구별[11]", "method": "실시간 PCR(SYBR Green I) 융해곡선 분석",
  "conditions": {"instrument": "", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "SYBR Green I 형광, 융해온도(Tm) 피크", "injection": "", "sample_prep": "", "standard": "정제 DNA 연속 희석", "linearity": "", "lod": "0.04 pg DNA", "loq": "", "recovery": ""},
  "rationale": "고기 성분이 아니라 종 판별 지표다; 초록의 'wallaroo'가 목록의 어느 학명인지는 밝혀지지 않음; 전문 확인 못함[11]", "source": [11], "url": "https://doi.org/10.1021/jf0615045", "source_kind": "paper"},
]

d = {
 "slug": "macropus-giganteus", "name_ko": "캥거루식용",
 "name_en": "Kangaroo meat (eastern grey kangaroo and other harvested kangaroos)",
 "scientific_name": "Macropus giganteus (식품원료 목록 학명 칸: M. giganteus / M. rufus / M. fuliginosus / M. robustus / M. rufogriseus rufogriseus)",
 "aliases": ["캥거루지육", "캥거루식용부산물", "캥거루 고기", "동부회색캥거루", "eastern grey kangaroo", "kangaroo meat"],
 "sections": sections, "compounds": compounds, "markers": [], "nutrients": [], "assays": assays,
 "production": [], "world": [], "gi": [], "orgs": [], "sources": S,
}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in sections: print(s["key"], len(s["body"]))
