import json
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "dossier.json"
ACC = "2026-11-02"

def pm(title, doi, extra):
    return {"title": f"{title} ({extra})", "url": f"https://doi.org/{doi}", "publisher": "PubMed", "accessed": ACC}

S = [
    {"title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 포포나무열매(Asimina triloba Dunal / Annona triloba (L.); 이명 파파·번려지·아시마나; Papaw), 사용가능, 사용가능부위: 열매; 같은 과 가시여지(Annona muricata)·아테모야·커스터드애플 행 대조 (로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json)",
     "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
    pm("A review of the postharvest biochemical, biophysical and biological properties of 61 cultivars of North American pawpaw (Asimina triloba) fruit — J Sci Food Agric 2025", "10.1002/jsfa.70115", "PMID 40879350, PMC12872236, 전문 확인"),
    pm("First genome and transcription factor profile for Asimina triloba, a native North American fruit tree — Plant Genome 2026", "10.1002/tpg2.70181", "PMID 41782323, PMC12961255, 전문 확인"),
    pm("The role of anthropogenic dispersal in shaping the distribution and genetic composition of a widespread North American tree species — Ecol Evol 2021;11(16):11515-11532", "10.1002/ece3.7944", "PMID 34429937, PMC8366864, 전문 확인"),
    pm("Annonacin in Asimina triloba fruit: implication for neurotoxicity — Neurotoxicology 2012;33(1):53-58", "10.1016/j.neuro.2011.10.009", "PMID 22130466, 초록 확인"),
    pm("Determination of Neurotoxic Acetogenins in Pawpaw (Asimina triloba) Fruit by LC-HRMS — J Agric Food Chem 2015;63(4):1053-1056 (미국 FDA Total Diet and Pesticide Research Center 연구진)", "10.1021/jf504500g", "PMID 25594104, 초록 확인"),
    pm("Identification of annonaceous acetogenins in the ripe fruit of the North American pawpaw (Asimina triloba) — J Agric Food Chem 2009;57(18):8339-8343", "10.1021/jf9018239", "PMID 19711911, 초록 확인"),
    pm("Annonacin, a lipophilic inhibitor of mitochondrial complex I, induces nigral and striatal neurodegeneration in rats: possible relevance for atypical parkinsonism in Guadeloupe — J Neurochem 2004;88(1):63-69", "10.1046/j.1471-4159.2003.02138.x", "PMID 14675150, 초록 확인"),
    pm("Paw paw and cancer: annonaceous acetogenins from discovery to commercial products — J Nat Prod 2008", "10.1021/np800191t", "PMID 18598079, 초록 확인"),
    pm("Asimin, asiminacin, and asiminecin: novel highly cytotoxic asimicin isomers from Asimina triloba — J Med Chem 1994", "10.1021/jm00039a009", "PMID 8027979, 초록 확인"),
    pm("Evaluation of various parts of the paw paw tree, Asimina triloba (Annonaceae), as commercial sources of the pesticidal annonaceous acetogenins — J Econ Entomol 1992;85(6):2353", "10.1093/jee/85.6.2353", "PMID 1464691, 초록 확인"),
    pm("Polysaccharide from Asimina triloba fruits alleviates DSS-induced ulcerative colitis by modulating inflammatory signaling and gut microbiota — NPJ Sci Food 2025", "10.1038/s41538-025-00587-5", "PMID 41266375, PMC12635153, 전문 확인"),
    pm("Phytochemical analysis of ten varieties of pawpaw (Asimina triloba [L.] Dunal) fruit pulp — Food Chem 2014", "10.1016/j.foodchem.2014.07.018", "PMID 25172760, 초록 확인"),
    pm("Phenolic Profiles, Antioxidant and Antimicrobial Activities of Pawpaw Pulp (Asimina triloba [L.] Dunal) at Different Ripening Stages — J Food Sci 2018", "10.1111/1750-3841.14414", "PMID 30557901, 초록 확인"),
    pm("Correlation Between Acetogenin Content and Antiproliferative Activity of Pawpaw (Asimina triloba [L.] Dunal) Fruit Pulp Grown in Korea — J Food Sci 2018;83(5):1430-1435", "10.1111/1750-3841.14144", "PMID 29660776, 초록 확인"),
    pm("Antioxidant Activities and Phenolic Compounds of Several Tissues of Pawpaw (Asimina triloba [L.] Dunal) Grown in Korea — J Food Sci 2017;82(8):1827-1833", "10.1111/1750-3841.13806", "PMID 28715604, 초록 확인"),
    pm("Lipids of the pawpaw fruit: Asimina triloba — Lipids 1999", "10.1007/s11745-999-0461-x", "PMID 10580337, 초록 확인"),
    pm("Targeted and non-targeted analysis of annonaceous alkaloids and acetogenins from Asimina and Annona species using UHPLC-QToF-MS — J Pharm Biomed Anal 2018;159:548-566", "10.1016/j.jpba.2018.07.030", "PMID 30077947, 초록 확인"),
    pm("Isoquinoline alkaloids from Asimina triloba — Nat Prod Res 2018", "10.1080/14786419.2018.1504045", "PMID 30453785, 초록 확인"),
    pm("Pawpaw (Asimina triloba) Seed Extract Suppresses High-Fat Diet-Induced Obesity in Mice — Int J Mol Sci 2025;26(16):7719", "10.3390/ijms26167719", "PMID 40869040, PMC12386974, 전문 확인"),
    pm("Development of the embryo and ruminate endosperm in an early-divergent angiosperm, Asimina triloba (Annonaceae) — Ann Bot 2025;136(2):297-308", "10.1093/aob/mcaf026", "PMID 40045477, 초록 확인"),
    pm("Late-acting self-incompatibility in Asimina triloba: implications for the evolution of self-incompatibility in angiosperms — BMC Plant Biol 2025;26(1):77", "10.1186/s12870-025-07681-6", "PMID 41372756, 초록 확인"),
    pm("Pollen-pistil interaction in pawpaw (Asimina triloba), the northernmost species of the mainly tropical family Annonaceae — Am J Bot 2017;104(12):1891-1903", "10.3732/ajb.1700319", "PMID 29217674, 초록 확인"),
    pm("Historical biogeography and ecological niche modelling of the Asimina-Disepalum clade (Annonaceae) — BMC Evol Biol 2017;17(1):188", "10.1186/s12862-017-1038-4", "PMID 28806923, 초록 확인"),
    pm("Guinea pig maximization test of the bark extract from pawpaw, Asimina triloba (Annonaceae) — Contact Dermatitis 1993", "10.1111/j.1600-0536.1993.tb04533.x", "PMID 8365150, 초록 확인"),
    pm("Loss of ripening capacity of pawpaw fruit with extended cold storage — J Agric Food Chem 2008", "10.1021/jf801857g", "PMID 18983162, 초록 확인"),
    pm("Physical characterization of frozen fruits from eight cultivars of the North American pawpaw (Asimina triloba) — Front Nutr 2022;9:936192", "10.3389/fnut.2022.936192", "PMID 36330137, 초록 확인"),
    pm("Identification and analysis of cell wall glycan epitopes and polyphenol oxidase in pawpaw fruit pulp as affected by high pressure processing and refrigerated storage — Food Sci Technol Int 2019", "10.1177/1082013219856769", "PMID 31291761, 초록 확인"),
    pm("High-Throughput Sequencing Reveals Tobacco and Tomato Ringspot Viruses in Pawpaw — Plants (Basel) 2022;11(24):3565", "10.3390/plants11243565", "PMID 36559676, 초록 확인"),
    pm("Chemical defense in the zebra swallowtail butterfly, Eurytides marcellus, involving annonaceous acetogenins — J Nat Prod 1999", "10.1021/np980308s", "PMID 9917274, 초록 확인"),
    pm("Method development for quantification of the environmental neurotoxin annonacin in Rat plasma by UPLC-MS/MS and application to a pharmacokinetic study — J Chromatogr B 2015", "10.1016/j.jchromb.2015.09.039", "PMID 26444335, 초록 확인"),
    pm("The alternative medicine pawpaw and its acetogenin constituents suppress tumor angiogenesis via the HIF-1/VEGF pathway — J Nat Prod 2010", "10.1021/np100228d", "PMID 20423107, PMC2890309, 초록 확인"),
    pm("Agrobacterium rhizogenes mediated-transformation of Asimina triloba L. cuttings — Pak J Biol Sci 2007", "10.3923/pjbs.2007.132.136", "PMID 19069999, 초록 확인"),
]
sources = [dict(n=i + 1, **s) for i, s in enumerate(S)]

sections = [
 {"key": "overview", "title": "한눈에 보기", "body":
  "포포나무(Asimina triloba)는 열대 과일이 많은 포포나무과(Annonaceae)에서 드물게 온대에 사는 속의 나무로, 북미에 자생하는 과일 가운데 가장 큰 열매를 맺는다[2]. 식약처 「식품원료 목록」에는 원료명 '포포나무열매'(학명 Asimina triloba Dunal / Annona triloba (L.), 영어명 Papaw, 이명 파파·번려지·아시마나)로 한 행이 올라 있다[1]. 이 행은 식품에 쓸 수 있는 원료(사용가능)이고 사용 조건은 '사용가능부위 : 열매'라서 열매 말고 잎·가지·껍질·씨는 이 목록으로 쓸 수 없다[1]. 이 종을 원재료로 하는 건강기능식품 고시형 원료는 확인하지 못함.\n\n"
  "열매는 바나나·망고·파인애플을 섞은 듯한 맛을 내며, 먹는 부분은 과육뿐이고 껍질과 씨는 먹지 않는다[2, 4]. 과육에는 에피카테킨과 프로시아니딘 같은 폴리페놀, 카로티노이드, 비타민 C가 들어 있다[2, 13]. 한편 이 식물은 미토콘드리아 복합체 I을 막는 아세토게닌(아시미신·아노나신 등)을 만들며, 익은 과육에서도 아노나신이 검출되어 신경독성 우려가 제기되었다[5, 7, 10]. 이 우려는 안전성 절에 따로 정리했다[5, 6, 8]."},
 {"key": "history", "title": "역사", "body":
  "포포 열매는 북미 원주민이 귀하게 여긴 식량이었고, 섬유질 나무껍질로는 밧줄과 천을 만들었다[4]. 미시시피강·오하이오강 유역과 아칸소·일리노이·켄터키 등 여러 고고학 유적에서 씨나 탄화된 잔해가 나왔다[4]. 문헌 기록은 1541년 에르난도 데 소토 원정대가 동남부 원주민이 이 나무를 널리 심었다고 적은 것이 처음이다[4]. 미시간 대학 연구진은 미세위성 표지 분석으로 원주민 거주지 주변 집단이 수백 km 떨어진 야생 집단과 희귀 대립유전자를 공유한다는 것을 보여, 사람이 씨를 옮겼다는 가설과 맞는 결과를 냈다[4].\n\n"
  "품종 기록은 1890년대 'Uncle Tom'이 첫 이름 붙은 품종으로 소개된 데서 시작되고, 1916년 미국 유전학회가 연 '가장 좋은 포포 찾기' 대회의 우승 품종 'Ketter'는 지금 전하지 않는다[2]. 1980년대에 상업화 노력이 되살아나 이름 붙은 품종이 크게 늘었다[2]. 1994년부터 켄터키 주립대학이 미국 국가식물유전자원 체계의 포포 보존 기관으로 지정되어 야생·재배 계통 1,700점을 보존한다[3]. 의약 분야에서는 퍼듀 대학이 고등식물 3,500종을 선별한 연구에서 포포 추출물이 가장 강한 활성을 보인 축에 들었고, 50종이 넘는 아세토게닌이 분리되었다[9]."},
]
# fix wording: dispersal paper is University of Georgia
sections[1]["body"] = sections[1]["body"].replace("미시간 대학 연구진은", "조지아 대학 연구진은")

sections += [
 {"key": "biology", "title": "식물학적 특징", "body":
  "포포나무는 숲 아래층에서 자라는 작은 낙엽 교목으로, 북쪽 플로리다에서 캐나다 온타리오 남부, 서쪽으로 네브래스카까지 퍼져 있다[3, 4]. 뿌리에서 새 줄기(근맹아)가 올라와 오래 유지되는 무리를 이루며, 지름 11.4 cm 줄기에서 나이테 32개가 확인된 예가 있다[4]. 꽃은 4–5월에 피고 암술이 먼저 성숙하는 웅예선숙이 강하며, 파리·딱정벌레·작은 나방 같은 약하게 나는 곤충이 꽃가루를 옮긴다[3, 4]. 암술머리가 꽃가루를 받을 수 있는 기간이 같은 과의 다른 종보다 길다[23]. 자기 꽃가루로는 수정은 되지만 배가 첫 분열에서 멈추고 수분 20일 뒤 어린 열매가 대량으로 떨어지는 '늦게 작용하는 자가불화합성'이 있다[22]. 일리노이 한 집단에서는 꽃의 0.4%만 열매를 맺었다[4].\n\n"
  "열매는 한 송이에 1–13개 달리고 무게 50–1,000 g, 과육은 주황·노랑·흰색이며 씨는 15–25 mm로 크다[3]. 61개 품종을 정리한 리뷰에서 과육 당도는 13.9–28.0 °Brix, pH 5.5–6.8, 수분 71.1–78.0%였다[2]. 씨 속 배젖에는 주름진 '반추 배젖'이 있고 배는 작고 덜 자란 상태로 남는다[21]. 아세토게닌 때문에 잎을 먹는 초식동물이 적지만, 얼룩무늬호랑나비(Eurytides marcellus) 애벌레는 잎을 먹고 몸에 아세토게닌을 지닌다[30]."},
 {"key": "related_species", "title": "이름과 가까운 종", "body":
  "포포나무속(Asimina)은 포포나무과에서 추운 기후에 적응한 종을 가진 유일한 속이다[23]. 같은 속에는 털포포(woolly pawpaw), 큰꽃포포, 작은꽃포포, 난쟁이포포 등 여러 종과 잡종이 있으나 열매가 크고 맛이 좋아 재배되는 종은 A. triloba다[3]. 분자 연대 추정에서 북미의 포포나무속과 동남아시아의 Disepalum속은 약 4,000만 년 전 갈라진 자매 계통이다[24]. 같은 과에는 체리모야·슈가애플·가시여지(그라비올라) 같은 열대 과수가 있다[2, 3].\n\n"
  "식약처 목록에서 가시여지(Annona muricata)는 열매는 사용가능이지만 가지·잎은 '제한적사용'으로 따로 분류되어 있다[1]. 아테모야(Annona cherimola × A. squamosa)는 열매만 쓰고 씨는 사용불가, 커스터드애플(목록 표기 Annona reticulate L.)은 열매가 사용가능이다[1]. 영어 'pawpaw'는 파파야(Carica papaya)를 가리키기도 해서 문헌을 찾을 때 섞이기 쉽고, 리뷰도 두 과일을 혼동하지 말라고 적었다[2]. 식약처 목록의 이명 '파파'도 파파야와 헷갈릴 수 있으니 학명으로 확인하는 것이 안전하다[1]."},
 {"key": "cultivation", "title": "재배와 산지", "body":
  "미국에서 포포는 농무부 내한성 구역 5–9에서 자라며, 수확은 한여름에서 가을 중순 사이 1년에 한 번이다[2]. 대부분의 재배자는 나무 몇 그루로 해마다 수백 파운드를 거두는 소규모이고, 생과나 냉동 과육을 직접 팔거나 맥주·아이스크림용 도매로 넘긴다[2]. 심은 뒤 본격적인 수확까지 5–7년이 걸리고, 상업 품종 수는 2009년 45개에서 2020년 140개로 늘었다[3]. 미국 밖으로는 유럽 18개국과 아시아 4개국에 도입되었다고 정리되며, 한국도 재배 국가로 꼽힌다[2, 3]. 국내 연구는 포포가 한국에서 널리 재배된다고 적었고, 2025년 연구는 전라남도의 포포 생산자 조합에서 열매를 구했다[12, 15, 16].\n\n"
  "가장 흔한 병은 잎과 열매에 반점을 만드는 곰팡이 병이며, 열매에 흠과 갈라짐을 남겨 상품성을 떨어뜨린다[3]. 미국 뉴욕에서는 담배둥근무늬바이러스와 토마토둥근무늬바이러스가 위축·모자이크 증상 나무에서 확인되었다[29]. 꺾꽂이로는 뿌리가 잘 내리지 않아, 실험에서 Agrobacterium rhizogenes 처리를 한 실생묘 삽수만 뿌리를 내렸다[33]. 국내 재배 면적과 생산량은 확인하지 못함."},
 {"key": "processing", "title": "가공과 이용", "body":
  "포포 열매는 상온에서 약 5일이면 물러지고, 냉장하면 한 달 정도로 늘지만 다른 저장 연장법은 잘 듣지 않았다[3]. 2–4 °C에서 4주까지 둔 열매는 정상적으로 익었으나 6주가 지나면 냉해로 과육이 갈변했다[26]. 과육 pH가 6.07–6.47로 거의 중성이라 공기에 닿으면 빨리 갈변하며, 냉동 과일 연구는 과육 가공에 'Susquehanna', 주스에 'Overleese' 품종이 알맞다고 보았다[27]. 갈변 효소인 폴리페놀산화효소는 pH 6.5–7.0에서 가장 활발하고 과육의 pH 범위에서도 작동한다[2]. 고압 처리와 냉장 보관이 세포벽과 이 효소에 주는 영향도 연구되었다[28].\n\n"
  "국내 연구진은 전남산 열매를 80 °C 물로 추출해 포도당·아라비노스가 주성분인 다당류(분자량 164,504 g/mol)를 얻었고, 생쥐 대장염 모델에서 증상을 줄였다고 보고했다[12]. 씨 에탄올 추출물을 고지방 사료에 섞은 생쥐 실험에서는 체중과 내장지방 증가가 줄었으나, 연구진은 추출물 성분을 분석하지 않았다고 밝혔다[20]. 미국에서는 잔가지 추출물을 넣은 제품이 대체의학용 항암 제품으로 팔렸고, 한 시판 보충제는 잔가지와 비슷한 성분 양상을 보였다[18, 32]. 식약처 「식품 등의 생산실적」에서 포포나무를 원료명으로 한 품목은 확인하지 못함."},
 {"key": "genetics", "title": "유전 정보", "body":
  "2026년 'Mango' 품종 잎으로 PacBio HiFi 서열을 읽어 첫 포포 유전체를 공개했다[3]. 조립 길이는 851.7 Mbp, 68개 콘티그, N50 28.6 Mbp, GC 함량 37.1%였고 반복 서열이 74.8%를 차지했다[3]. 단백질 암호화 유전자 41,468개가 예측되었고, 병 저항성과 익음에 관여하는 WRKY 전사인자 47개와 NAC 전사인자 43개가 확인되었다[3]. 자료는 NCBI BioProject PRJNA1211107로 공개되었으며, 이배체 종을 반수체로 합친 조립본이다[3].\n\n"
  "북미 전역 야생 집단 62곳과 원주민 거주지 주변 집단 20곳을 미세위성 표지 9개로 분석한 연구에서, 거주지 주변 집단은 유전 다양성이 낮고 이형접합 과잉과 클론 번식 비율이 높았다[4]. 이 집단들은 평균 723 km 떨어진 야생 집단과 희귀 대립유전자를 공유했다[4]. 'Mango' 유전체에서도 이형접합 변이가 많아 야생에서 고른 품종의 특성이 드러났다[3]. 포포나무과 유전체와 비교한 계통 분석에서 이 종은 다른 포포나무과 유전체들의 바깥 무리에 놓였다[3]. 늦게 작용하는 자가불화합성은 수분 8일째부터 유전자 발현 차이로 나타났다[22]."},
 {"key": "safety", "title": "안전성", "body":
  "포포나무는 아세토게닌이라는 지방산 유래 고리 화합물을 만든다[9]. 대표 성분 아시미신(asimicin)과 이성질체들은 미토콘드리아 NADH-유비퀴논 산화환원효소(복합체 I)를 강하게 막는다[10]. 같은 계열의 아노나신은 쥐에 정맥 투여하자 뇌로 들어가 흑질 도파민 신경세포를 31.7% 줄였다[8]. 이 연구는 과들루프에서 가시여지 열매와 잎차 섭취가 비정형 파킨슨증과 관련된 역학 자료를 배경으로 했다[8]. 포포 과육에서는 아노나신이 평균 0.0701 mg/g 검출되었고, 정제 아노나신(30.07 μg/mL)과 과육 추출물은 배양 피질 신경세포의 절반을 죽였다[5]. 미국 FDA 연구진은 동결건조 과육에서 아노나신 7.72 mg/g, 스쿼모신 0.162 mg/g을 보고해 값이 연구마다 크게 다르다[5, 6]. 익은 과육에서도 아시미신·불라타신·불라탈리신이 확인되어 과다 섭취의 위험 평가가 필요하다고 제안되었다[7]. 아노나신은 쥐 혈장 정량법이 따로 개발될 만큼 환경성 신경독소로 다뤄진다[31]. 사람에서 포포 섭취와 신경질환의 관계를 직접 조사한 연구는 확인하지 못함.\n\n"
  "씨·덜 익은 열매·잔가지·뿌리·나무껍질은 아세토게닌이 특히 많아 살충 추출물 원료로 평가되었다[11]. 아세토게닌은 척추동물에서 구토를 일으킨다고 보고되었다[30]. 나무껍질 추출물은 기니피그 시험에서 약한 피부 감작제였다[25]. 식약처 목록은 열매만 식품원료로 허용한다[1]. 식약처 등 공공기관의 알레르기·잔류 정보는 확인하지 못함."},
]
# note: [30] = zebra swallowtail paper (emetic mention), [29]=virus. fix biology ref
compounds = [
 {"name": "Annonacin", "name_ko": "아노나신", "class": "모노-THF 아세토게닌", "role": "bioactive", "part": "열매 과육",
  "content_text": "과육 평균 0.0701±0.0305 mg/g[5]; 동결건조 과육 7.72 mg/g(100 °C 가압 메탄올 추출, LC-HRMS)[6]",
  "activity_ko": "미토콘드리아 복합체 I 억제; 쥐에서 흑질·선조체 신경세포 손실[8]; 배양 피질 신경세포 독성[5]", "source": [5, 6, 8]},
 {"name": "Squamocin", "name_ko": "스쿼모신", "class": "비스-THF 아세토게닌", "role": "bioactive", "part": "열매 과육(동결건조)",
  "content_text": "0.162 mg/g[6]", "activity_ko": "신경독성 우려 아세토게닌으로 정량됨[6]", "source": [6]},
 {"name": "Asimicin", "name_ko": "아시미신", "class": "비스-THF 아세토게닌", "role": "bioactive", "part": "익은 과육·줄기껍질",
  "content_text": "익은 과육 추출물에서 HPLC-MS로 확인(함량 미기재)[7]", "activity_ko": "NADH-유비퀴논 산화환원효소(복합체 I) 강력 억제, 세포독성·살충[10]", "source": [7, 10]},
 {"name": "Bullatacin", "name_ko": "불라타신", "class": "비스-THF 아세토게닌", "role": "bioactive", "part": "익은 과육",
  "content_text": "익은 과육 추출물의 주요 아세토게닌 3종 중 하나(함량 미기재)[7]", "activity_ko": "브라인슈림프 치사 활성의 원인 성분군[7]", "source": [7]},
 {"name": "Bullatalicin", "name_ko": "불라탈리신", "class": "비스-THF 아세토게닌", "role": "bioactive", "part": "익은 과육",
  "content_text": "익은 과육 추출물에서 확인(함량 미기재)[7]", "activity_ko": "아세토게닌 활성 성분[7]", "source": [7]},
 {"name": "Epicatechin", "name_ko": "(-)-에피카테킨", "class": "플라반-3-올", "role": "marker", "part": "열매 과육",
  "content_text": "10개 품종 모두에서 확인된 주요 플라보노이드[13]; 'Davis' 품종에서 표준품 정량 성분 중 가장 많음[2]",
  "activity_ko": "과육 항산화 성분, 갈변 효소의 기질 후보[2]", "source": [13, 2]},
 {"name": "Procyanidin B2", "name_ko": "B형 프로시아니딘(이량체·삼량체)", "class": "프로안토시아니딘", "role": "bioactive", "part": "열매 과육",
  "content_text": "질량분석으로 B형 이량체·삼량체 확인(함량 미기재)[13]", "activity_ko": "에피카테킨 중합체로 과육 폴리페놀의 한 축[2]", "source": [13, 2]},
 {"name": "Protocatechuic acid", "name_ko": "프로토카테큐산 헥소사이드", "class": "페놀산 배당체", "role": "bioactive", "part": "열매 과육",
  "content_text": "과육의 주된 페놀산 3종 중 하나(헥소사이드 형태, 함량 미기재)[13]", "activity_ko": "과육 항산화 성분[13]", "source": [13]},
 {"name": "Epigallocatechin", "name_ko": "에피갈로카테킨", "class": "플라반-3-올", "role": "bioactive", "part": "열매 과육(국내 재배)",
  "content_text": "17개 페놀 성분 중 주성분, 익을수록 모든 성분이 크게 감소[14]", "activity_ko": "덜 익은 열매 추출물의 높은 항산화 활성과 관련[14]", "source": [14]},
 {"name": "Ascorbic acid", "name_ko": "비타민 C(아스코르브산)", "class": "비타민", "role": "nutrient", "part": "열매 과육",
  "content_text": "'Taytwo' 약 4.4 mg/100 g, 'Davis' 7.3 mg/100 g; 무명 품종 1.0·7.6 mg/100 g[2]", "activity_ko": "수용성 항산화 비타민; 냉장 8주 동안 총량 감소[2]", "source": [2]},
 {"name": "beta-Carotene", "name_ko": "베타카로틴", "class": "카로티노이드", "role": "nutrient", "part": "열매 과육",
  "content_text": "국내 재배 무명 품종 과육 82 μg/100 g; 8개 품종 총카로티노이드 1.5–6.1 μg/g[2]", "activity_ko": "프로비타민 A, 과육의 노란·주황색[2]", "source": [2]},
 {"name": "Octanoic acid", "name_ko": "옥탄산(카프릴산)", "class": "중쇄지방산", "role": "nutrient", "part": "열매",
  "content_text": "열매 트라이글리세라이드 지방산의 20%[17]", "activity_ko": "열매 지질의 특이한 중쇄지방산 구성[17]", "source": [17]},
 {"name": "Methyl octanoate", "name_ko": "옥탄산 메틸(메틸 옥타노에이트)", "class": "에스터(향기 성분)", "role": "marker", "part": "열매",
  "content_text": "수확 시와 저장 중 우세한 향기 성분 4종 중 하나(메틸·에틸 옥타노에이트, 에틸·메틸 헥사노에이트)[2]", "activity_ko": "포포 특유의 열대과일 향[2]", "source": [2]},
 {"name": "Malic acid", "name_ko": "말산(사과산)", "class": "유기산", "role": "nutrient", "part": "열매 과육",
  "content_text": "미국 조지아산 322 mg/100 g; 국내산은 31 mg/100 g(아세트산 62 mg/100 g이 가장 많음)[2]", "activity_ko": "과육의 신맛 성분[2]", "source": [2]},
 {"name": "Magnoflorine", "name_ko": "마그노플로린", "class": "아포르핀 알칼로이드", "role": "bioactive", "part": "잔가지",
  "content_text": "잔가지의 주된 알칼로이드(함량 미기재)[18]", "activity_ko": "포포나무속 종 구별 표지 후보; 잔가지에는 리리오데닌 등 아포르핀 알칼로이드도 있음[18, 19]", "source": [18, 19]},
]

assays = [
 {"role": "literature", "compound": "Glucose", "compound_ko": "포도당(다당류 ATP-W-1의 단당 조성: 만노스·람노스·포도당·갈락토스·아라비노스)",
  "part": "열매(껍질째, 전남산; 열수 추출 후 정제한 중성 다당류)",
  "content": "몰비 만노스 2.23, 람노스 6.43, 포도당 50.12, 갈락토스 8.36, 아라비노스 31.91; 조다당 수율 18.43%[12]",
  "method": "HPLC-UV(PMP 유도체화)",
  "conditions": {"instrument": "", "column": "Phenomenex C18, 250 × 10 mm",
   "mobile_phase": "0.05 M 인산완충액(pH 6.70)–아세토니트릴 80:20 (v/v)", "gradient": "고정 비율(기울기 기재 없음)",
   "flow": "1.0 mL/min", "temp": "30 °C", "detection": "UV 250 nm", "injection": "",
   "sample_prep": "ATP-W-1 5 mg + 2 M TFA 2 mL, 110 °C 4시간 가수분해 → 메탄올로 TFA 제거 → 0.5 M PMP 메탄올 용액, 알칼리 조건 70 °C 30분 유도체화 → 0.3 M HCl로 정지 → 클로로포름 2회 세척 → 0.22 µm 여과",
   "standard": "만노스·람노스·갈락투론산·글루쿠론산·포도당·갈락토스·자일로스·아라비노스·푸코스 혼합 표준품(PMP 유도체화)",
   "linearity": "2.5–500 µg/mL, 모든 당 > 0.995", "lod": "0.72–1.13 µg/mL", "loq": "1.75–3.45 µg/mL", "recovery": ""},
  "rationale": "열매 다당류의 구조(포도당·아라비노스 주성분, 산성당 없음)를 규정하는 성분 분석으로, 대장염 모델 효과를 보인 정제 분획의 품질 지표가 됨; 전문 확인, 기기 모델·주입량·회수율은 원문에 없음[12].",
  "source": [12], "url": "https://doi.org/10.1038/s41538-025-00587-5", "source_kind": "paper"},
 {"role": "literature", "compound": "Annonacin", "compound_ko": "아노나신(스쿼모신 동시 정량)",
  "part": "열매 과육(동결건조)", "content": "아노나신 7.72 mg/g, 스쿼모신 0.162 mg/g(100 °C 추출 최적)[6]",
  "method": "LC-HRMS",
  "conditions": {"instrument": "", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "", "injection": "",
   "sample_prep": "", "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "신경독성이 보고된 아세토게닌이라 식품 안전성 평가의 지표로 정량됨; 초록상 건조 메탄올로 100 °C·10 MPa 밀폐 용기에서 추출했으며 이성질체는 분리만 하고 정량하지 않음; 전문 확인 못함[6].",
  "source": [6], "url": "https://doi.org/10.1021/jf504500g", "source_kind": "paper"},
 {"role": "literature", "compound": "Annonacin", "compound_ko": "아노나신",
  "part": "열매 과육", "content": "평균 0.0701±0.0305 mg/g[5]",
  "method": "컬럼 크로마토그래피 분리 후 MS·NMR·IR 확인(정량법 세부 확인 못함)",
  "conditions": {"instrument": "", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "", "injection": "",
   "sample_prep": "", "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "과육에 신경독성 아세토게닌이 있는지 확인하려고 분리·정량함; 초록상 메탄올 추출 후 에틸아세테이트 분배로 조추출물을 만들었고 합성·천연 아노나신과 스펙트럼을 대조함; 전문 확인 못함[5].",
  "source": [5], "url": "https://doi.org/10.1016/j.neuro.2011.10.009", "source_kind": "paper"},
]

d = {
 "slug": "asimina-triloba", "name_ko": "포포나무", "name_en": "Pawpaw (North American pawpaw, papaw)",
 "scientific_name": "Asimina triloba (L.) Dunal",
 "aliases": ["포포나무열매", "포포", "파파", "번려지", "아시마나", "Papaw", "Pawpaw", "Paw paw", "Indian banana", "Annona triloba"],
 "sections": sections, "compounds": compounds, "markers": [], "nutrients": [], "assays": assays,
 "production": [], "world": [], "gi": [], "orgs": [], "sources": sources,
}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
print("written", len(sources))
