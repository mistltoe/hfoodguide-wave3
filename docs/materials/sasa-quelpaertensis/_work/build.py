import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
A = "2026-11-02"
def pm(n, title, doi, extra):
    return {"n": n, "title": f"{title} — {extra}", "url": f"https://doi.org/{doi}", "publisher": "PubMed", "accessed": A}
sources = [
 {"n": 1, "title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 제주조릿대순·제주조릿대잎·제주조릿대추출농축액(Sasa quelpaertensis Nakai / Sasa palmata; 이명 산죽, 탐라세; 영명 Broad-leaf bamboo), 사용가능, 사용가능부위: 순, 잎; 같은 목록의 조릿대(Sasa borealis, 제한적사용)·갓대(Sasa chiisanensis)·섬조릿대(Sasa kurilensis)·얼룩조릿대(Sasa veitchii)·신이대(Sasa coreana)·난쟁이조릿대(Sasa nipponica)·Sasa senanensis 행 대조 (로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json)", "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
 pm(2, "A Review on Sasa quelpaertensis's Phytochemical Profiles and Pharmacological Activities", "10.3390/plants15020319", "Plants (Basel) 2026;15(2):319 (PMID 41600126, PMC12844733, 전문 확인; 종설이라 표 1 수치의 원 논문은 추출본에서 참고문헌 번호가 빠져 확인하지 못함)"),
 pm(3, "Sasa quelpaertensis Leaf Extract Ameliorates Dyslipidemia, Insulin Resistance, and Hepatic Lipid Accumulation in High-Fructose-Diet-Fed Rats", "10.3390/nu12123762", "Nutrients 2020;12(12):3762 (PMID 33297496, PMC7762336, 전문 확인)"),
 pm(4, "Sasa quelpaertensis Leaf Extract Inhibits Colon Cancer by Regulating Cancer Cell Stemness in Vitro and in Vivo", "10.3390/ijms16059976", "Int J Mol Sci 2015;16(5):9976-97 (PMID 25941936, PMC4463628, 전문 확인)"),
 pm(5, "Comprehensive analysis of the chloroplast genome and phylogenetic relationships of Sasa quelpaertensis Nakai", "10.1080/23802359.2023.2301017", "Mitochondrial DNA B Resour 2024;9(1):88-93 (PMID 38222981, PMC10786426, 전문 확인)"),
 pm(6, "Evaluating feed value of native Jeju bamboo (Sasa quelpaertensis Nakai) for beef cattle", "10.5713/ab.22.0160", "Anim Biosci 2023;36(2):238-247 (PMID 36108698, PMC9834733, 전문 확인; 성분표는 추출본에 없음)"),
 pm(7, "Impact of different partitioned solvents on chemical composition and bioavailability of Sasa quelpaertensis Nakai leaf extract", "10.1016/j.jfda.2016.08.006", "J Food Drug Anal 2017;25(2):316-326 (PMID 28911673, PMC9332518, 전문 확인)"),
 pm(8, "Comparison of the improving embryo development effects of Sasa quelpaertensis Nakai extract, p-coumaric acid, and myricetin on porcine oocytes according to their antioxidant capacities", "10.1016/j.theriogenology.2022.03.009", "Theriogenology 2022;185:97-108 (PMID 35395590, 초록만 확인)"),
 pm(9, "p-Coumaric acid, a constituent of Sasa quelpaertensis Nakai, inhibits cellular melanogenesis stimulated by alpha-melanocyte stimulating hormone", "10.1111/j.1365-2133.2008.08653.x", "Br J Dermatol 2008;159(2):292-9 (PMID 18544081, 초록만 확인)"),
 pm(10, "Sasa quelpaertensis phenylpropanoid derivative suppresses lipopolysaccharide-induced nitric oxide synthase and cyclo-oxygenase-2 expressions in RAW 264.7 cells", "10.1248/yakushi.131.961", "Yakugaku Zasshi 2011;131(6):961-7 (PMID 21628985, 초록만 확인)"),
 pm(11, "Anti-obesity properties of a Sasa quelpaertensis extract in high-fat diet-induced obese mice", "10.1271/bbb.110868", "Biosci Biotechnol Biochem 2012;76(4):755-61 (PMID 22484945, 초록만 확인)"),
 pm(12, "Sasa quelpaertensis Nakai extract and its constituent p-coumaric acid inhibit adipogenesis in 3T3-L1 cells through activation of the AMPK pathway", "10.1016/j.fct.2013.06.033", "Food Chem Toxicol 2013;59:380-5 (PMID 23810795, 초록만 확인)"),
 pm(13, "Sasa quelpaertensis leaf extract suppresses dextran sulfate sodium-induced colitis in mice by inhibiting the proinflammatory mediators and mitogen-activated protein kinase phosphorylation", "10.1016/j.nutres.2014.09.002", "Nutr Res 2014;34(10):894-905 (PMID 25287291, 초록만 확인)"),
 pm(14, "Sasa quelpaertensis leaf extract improves high fat diet-induced lipid abnormalities and regulation of lipid metabolism genes in rats", "10.1089/jmf.2013.2916", "J Med Food 2014;17(5):571-81 (PMID 24738745, 초록만 확인)"),
 pm(15, "Sasa quelpaertensis Induced Antidepressant-Like Effect in Ovariectomized Rats", "10.1155/2019/5815604", "Biomed Res Int 2019:5815604 (PMID 31380432, PMC6657632, 초록 확인)"),
 pm(16, "Phenolic acid and flavonoid-rich fraction of Sasa quelpaertensis Nakai leaves prevent alcohol induced fatty liver through AMPK activation", "10.1016/j.jep.2018.06.008", "J Ethnopharmacol 2018;224:335-348 (PMID 29906537, 초록만 확인)"),
 pm(17, "Sasa quelpaertensis leaf extract mitigates fatigue and regulates the transcriptome profile in mice", "10.1007/s13258-018-0765-2", "Genes Genomics 2019;41(3):317-324 (PMID 30448902, 초록만 확인)"),
 pm(18, "Effect of Sasa quelpaertensis Nakai extract on gut microbiota and production performance in pigs", "10.5187/jast.2024.e84", "J Anim Sci Technol 2024;66(4):740-748 (PMID 39165746, PMC11331370, 초록 확인)"),
 pm(19, "Sasa quelpaertensis Nakai extract suppresses porcine reproductive and respiratory syndrome virus replication and modulates virus-induced cytokine production", "10.1007/s00705-015-2469-0", "Arch Virol 2015;160(8):1977-88 (PMID 26047649, 초록 확인)"),
 pm(20, "Effects of green tea or Sasa quelpaertensis bamboo leaves on plasma and liver lipids, erythrocyte Na efflux, and platelet aggregation in ovariectomized rats", "10.4162/nrp.2012.6.2.106", "Nutr Res Pract 2012;6(2):106-12 (PMID 22586498, PMC3349031, 초록 확인)"),
 pm(21, "Sasa quelpaertensis leaf extract regulates microbial dysbiosis by modulating the composition and diversity of the microbiota in dextran sulfate sodium-induced colitis mice", "10.1186/s12906-016-1456-7", "BMC Complement Altern Med 2016;16(1):481 (PMID 27884149, PMC5123288, 초록 확인)"),
 pm(22, "Sasa quelpaertensis Nakai extract induces p53-independent apoptosis via the elevation of nitric oxide production in human HCT116 colon cancer cells", "10.3892/ol.2020.11379", "Oncol Lett 2020;19(4):3027-3034 (PMID 32218860, PMC7068647, 초록 확인)"),
 pm(23, "Sasa quelpaertensis and p-coumaric acid attenuate oleic acid-induced lipid accumulation in HepG2 cells", "10.1271/bbb.130167", "Biosci Biotechnol Biochem 2013;77(7):1595-8 (PMID 23832345, 초록만 확인)"),
]

sections = [
 {"key": "overview", "title": "한눈에 보기", "body":
  "제주조릿대(Sasa quelpaertensis Nakai)는 벼과(Poaceae) 조릿대속의 키 작은 여러해살이 대나무로, 제주도 한라산에만 자라는 한국 특산종이다[5, 6]. 식약처 「식품원료 목록」에는 '제주조릿대순'·'제주조릿대잎'·'제주조릿대추출농축액' 세 행이 모두 '사용가능' 원료로 올라 있고, 사용 조건은 '사용가능부위 : 순, 잎'이다[1]. 같은 목록은 학명을 'Sasa quelpaertensis Nakai / Sasa palmata'로 함께 적고, 이명으로 '산죽, 탐라세', 영명으로 'Broad-leaf bamboo'를 적었다[1]. 건강기능식품 고시형 원료의 원재료로는 올라 있지 않다[1].\n\n"
  "제주 지역에서는 예부터 잎을 말려 차로 달여 당뇨·위염 등에 민간요법으로 써 왔다[2, 7]. 잎 추출물에서는 p-쿠마르산과 트리신이 주성분이자 지표성분으로 정량되어 왔고, 이소오리엔틴·바닐산 같은 페놀 성분도 보고되었다[2, 3, 4]. 잎 추출물의 항비만·장염 완화·간 보호 효과는 대부분 세포와 쥐 실험에서 나온 결과로, 사람에서 확인된 효과로 보기는 어렵다[2, 11, 13]."},
 {"key": "history", "title": "이름과 이용의 역사", "body":
  "학명은 명명자 Nakai 가 한라산 식생을 조사하면서 모은 표본을 바탕으로 붙인 것이다[2]. 2008년 논문은 국문명을 'Jeju-Joritdae'로 소개했고, 이후 학술 문헌도 이 표기를 쓴다[5, 9]. 식약처 목록에 적힌 이명 '산죽'은 같은 목록의 갓대(Sasa chiisanensis)에도 붙어 있어, 이름만으로는 종을 구분할 수 없다[1].\n\n"
  "제주 지역 주민들은 잎을 말려 대나무 잎차로 마시며 항염·항당뇨·위염 완화·이뇨 목적의 민간요법으로 써 왔다[2, 7, 14]. 2000년대 후반부터 잎과 줄기 추출물의 미백·항염 성분 연구가 이어졌고, 2010년대에는 항비만·장염·간 보호에 관한 동물 실험이 많이 나왔다[9, 10, 11, 13]. 이 밖에 장내 미생물 조절, 알코올성 지방간 억제, 폐경 모델 쥐의 우울 유사 행동 완화, 돼지 바이러스 복제 억제, 대장암 세포 사멸 유도 등이 보고되었으나 모두 세포·동물 수준이다[15, 16, 19, 21, 22]. 폐경 모델 쥐에게 잎 가루를 사료의 10% 로 4주 먹인 비교 실험에서는 녹차와 달리 체중·간 중성지방 감소가 뚜렷하지 않았다[20]. 최근에는 한라산 북사면을 뒤덮을 만큼 퍼진 제주조릿대를 줄이면서 자원으로 쓰기 위해 소·돼지 사료로 이용하는 연구도 진행되었다[6, 18]."},
 {"key": "biology", "title": "식물학적 특징", "body":
  "제주조릿대는 땅속줄기로 퍼지며 빽빽한 무리를 이루는 여러해살이 대나무풀로, 키는 1 m 정도까지 자란다[5]. 줄기(稈)는 곧고 굵으며 속이 차 있고 평균 지름은 1.5 cm 이다[5]. 잎은 긴 타원상 피침형으로 길이 7–20 cm, 너비 2.5–5.0 cm 이며, 짙은 녹색 잎에 가장자리가 크림색으로 바랜다[5]. 잎집에는 뻣뻣한 털이 빽빽하여 거칠고, 꽃차례는 원추꽃차례로 잎겨드랑이에서 나오는 작은이삭이 처음에 적갈색 포에 싸여 있다[5].\n\n"
  "새순은 4월에 나기 시작해 8월에 생물량이 가장 많고, 9월 무렵부터 잎 가장자리가 하얗게 바랜다[6]. 늘푸른 잎을 가진 여러해살이풀로 땅속줄기가 흙 속에서 뻗는다[6]. 한라산국립공원 북사면의 약 76%를 덮을 만큼 세력이 커서, 빛·온도·습도·토양을 바꾸어 다른 식물의 다양성을 떨어뜨리는 것으로 지적된다[6]. 번식력이 강해 일부 희귀 자생식물을 멸종 위기로 몰고 있다는 보고도 있다[7]."},
 {"key": "related_species", "title": "근연종과 혼동 주의", "body":
  "식약처 「식품원료 목록」에는 조릿대속 원료가 여럿 있고 종마다 지위와 부위가 다르다[1]. 조릿대(Sasa borealis)는 '제한적사용'으로 '잎, 침출차에 한함' 조건이 붙어 있어, 순·잎이 '사용가능'인 제주조릿대와 다르다[1]. 갓대(Sasa chiisanensis)는 순·잎 사용가능, 섬조릿대(Sasa kurilensis)는 순, 얼룩조릿대(Sasa veitchii)와 신이대(Sasa coreana)는 잎, 난쟁이조릿대(Sasa nipponica)는 순·씨앗이 사용가능 부위다[1]. Sasa senanensis 는 싹·씨앗이 사용가능이고 잎 행은 '사용불가'로 올라 있다[1]. 따라서 다른 조릿대 종의 성분·효능 자료를 제주조릿대에 그대로 옮겨 쓰면 안 된다[1, 7].\n\n"
  "식약처 목록은 Sasa palmata 를 제주조릿대 학명과 함께 적었지만, 학계에서는 제주조릿대를 다른 조릿대 종의 이명으로 보는 견해와 잎·줄기 형태로 구분되는 독립 종으로 보는 견해가 엇갈려 왔다[1, 5]. 엽록체 유전체 분석은 제주조릿대가 비교한 다른 종과 DNA 변이가 있어 별개 종이라는 가설을 지지한다고 보고했다[5]. 이 논문의 계통수에서 가장 가까운 두 종의 학명은 내려받은 전문 추출본에서 빠져 있어 확인하지 못함."},
 {"key": "cultivation", "title": "자생지와 채취", "body":
  "제주조릿대는 재배 작물이라기보다 한라산 중산간에서 고산지대에 걸쳐 숲 아래층을 이루는 자생 식물이다[2, 5]. 연구에 쓰인 잎은 대부분 한라산에서 채취했으며, 2019년 9월 한라산에서 모은 잎을 60 °C 에서 말려 쓴 사례가 있다[3, 4]. 사료 연구에서는 한라산의 2 ha 유기 채취지에서 생장이 가장 왕성한 7월 초에 새로 난 제주조릿대 700 kg 을 손으로 베어 썼다[6].\n\n"
  "채취 시기에 따라 성분이 달라, 계절별 분석에서 p-쿠마르산은 잎보다 줄기에 많고 9월 줄기 추출물에서 가장 높았으며 트리신은 줄기보다 잎에 많았다[2]. 총페놀과 총플라보노이드는 잎이 줄기보다 많았고 12월 에탄올 추출물에서 가장 높았다[2]. 한라산 생태계를 지키려면 퍼짐을 억제하면서 자원으로 쓰는 방안이 필요하다는 지적이 있다[6, 7]. 국내 재배 면적·생산량 같은 공식 생산 통계는 확인하지 못함."},
 {"key": "processing", "title": "가공과 이용", "body":
  "전통적으로는 잎을 말려 차로 우려 마신다[2, 7]. 식약처 목록에는 순·잎 외에 '제주조릿대추출농축액'이 별도 원료명으로 올라 있다[1]. 연구용 추출물은 말린 잎을 70% 에탄올로 실온에서 48시간 우려낸 뒤 농축·동결건조하거나, 90 °C 물로 4시간 추출한 찌꺼기를 다시 70% 에탄올로 추출하는 방식으로 만들었다[3, 4]. 열수 추출물, 80% 에탄올 추출물과 그 용매 분획도 연구에 쓰였다[7, 17].\n\n"
  "추출 용매에 따라 성분과 활성이 크게 달라, 80% 에탄올 추출물을 나눈 분획 가운데 에틸아세테이트 분획의 항산화·티로시나아제 억제 활성이 가장 높았다[7]. 줄기 에탄올 추출물은 잎 추출물보다 멜라닌 생성을 더 강하게 억제했고, 그 주된 활성 성분은 p-쿠마르산이었다[9]. 소 사료로는 사일리지로 만들어 완전혼합사료(TMR)에 섞어 줄 때 기호성이 볏짚보다 좋았다[6]. 돼지 사료에 추출물을 넣은 시험에서는 장내 미생물 구성이 바뀌고 등지방 두께가 줄었다[18]. 건강기능식품 고시형 원료가 아니어서 식약처 「식품 등의 생산실적」의 해당 품목 통계는 확인하지 못함."},
 {"key": "genetics", "title": "유전체와 분류", "body":
  "제주조릿대의 엽록체 유전체 전체 서열은 2024년에 처음 보고되었다[5]. 길이는 139,730 bp 이고, 큰 단일복사 영역(LSC) 83,351 bp, 작은 단일복사 영역(SSC) 12,788 bp, 역반복 영역(IR) 두 개(각 21,796 bp)로 이루어진다[5]. 전체 GC 함량은 38.86% 이며, 유전자 131개(단백질 암호 86개, tRNA 37개, rRNA 8개)를 담고 있다[5].\n\n"
  "시료는 제주시 조천읍의 자생 집단에서 채취했고, 증거 표본은 국립산림과학원에 기탁되었다[5]. 온대 목본성 대나무 족(Arundinarieae) 26종의 엽록체 유전체와 비교한 최대우도 계통수에서 제주조릿대는 두 종과 함께 높은 지지도의 한 무리를 이루었다[5]. 다른 표본의 엽록체 DNA 조각과 맞춘 결과 평균 일치도는 99.83%, 최저 99.21% 였다[5]. 저자들은 핵 유전체를 포함한 추가 분자 분류 연구가 있어야 근연종과의 관계를 확정할 수 있다고 보았다[5]."},
 {"key": "safety", "title": "안전성과 주의", "body":
  "제주조릿대는 식약처 「식품원료 목록」에서 순·잎을 쓸 수 있는 '사용가능' 원료이며, 제한적사용 조건은 붙어 있지 않다[1]. 건강기능식품 고시형 원료가 아니므로 고시 섭취 시 주의사항은 없다[1]. 반면 이름이 비슷한 조릿대(Sasa borealis)는 잎을 침출차로만 쓸 수 있는 제한적사용 원료이므로 혼동하지 않아야 한다[1]. 알레르기·잔류 농약·독성 성분에 관한 공공기관 안전 정보는 확인하지 못함.\n\n"
  "동물 실험에서는 잎 추출물을 체중 1 kg 당 하루 100–300 mg 을 먹이거나 500 mg 을 16주 동안 마시는 물에 타서 주었고, 저자들은 이 범위를 독성 없는 범위로 여겼지만 별도의 독성 시험 결과는 아니다[3, 13]. 2026년 종설은 약동학·안전성 연구와 임상시험이 부족하며 300 mg/kg 같은 고용량 사용은 안전성 우려를 남긴다고 지적했다[2]. 같은 종설은 한국인 비만 성인 대상 임상 연구에서 허리둘레·복부 지방·중성지방이 조금 줄었다고 소개했으나, 원 논문은 확인하지 못함. 세포 실험에서 분리 성분 ESQ10 은 사람 각질형성세포와 피부섬유아세포에 독성을 보이지 않았다[10]."},
]

compounds = [
 {"name": "p-Coumaric acid", "name_ko": "p-쿠마르산", "class": "히드록시신남산(페놀산)", "role": "marker", "part": "잎·줄기", "content_text": "잎 70% 에탄올 추출물(SQE) 1.13 mg/g[4]; 물 추출 후 70% 에탄올 추출물 2.69 mg/g[3]; 추출물 1 mg 당 3.92 μg(LC-MS/MS)[8]; 종설 표 1: 잎 열수 추출물 5090 µg/g, 줄기 6450 µg/g(본문은 9월 줄기 물 추출물, 표는 70% 에탄올 추출물로 적어 서로 다름)[2]", "activity_ko": "줄기 추출물의 주된 멜라닌 생성 억제 성분(세포 실험)[9]; 3T3-L1 지방세포 분화 억제·AMPK 활성화(세포 실험)[12]; HepG2 세포 지방 축적 감소(세포 실험)[23]", "source": [2, 3, 4, 8, 9, 12, 23]},
 {"name": "Tricin", "name_ko": "트리신", "class": "플라본", "role": "marker", "part": "잎", "content_text": "잎 70% 에탄올 추출물 0.82 mg/g[4]; 물 추출 후 70% 에탄올 추출물 7.43 mg/g[3]; 종설 표 1: 잎 70% 에탄올 추출물 1970 µg/g, 줄기 560 µg/g[2]", "activity_ko": "대장암 줄기세포 마커 발현 억제(세포 실험, 추출물보다 약함)[4]", "source": [2, 3, 4]},
 {"name": "Myricetin", "name_ko": "미리세틴", "class": "플라보놀", "role": "bioactive", "part": "잎", "content_text": "추출물 1 mg 당 0.19 μg(LC-MS/MS)[8]; 종설 표 1: 물 추출물의 에틸아세테이트 분획 59.96 µg/g[2]", "activity_ko": "돼지 난자 체외 성숙·배아 발달 개선(항산화, 세포 실험)[8]", "source": [2, 8]},
 {"name": "Vanillic acid", "name_ko": "바닐산", "class": "히드록시벤조산", "role": "bioactive", "part": "잎", "content_text": "종설 표 1: 잎 물 추출물 2100 µg/g(5월 채취 잎 물 추출물에서 가장 높음)[2]", "activity_ko": "", "source": [2]},
 {"name": "Isoorientin", "name_ko": "이소오리엔틴", "class": "플라본 C-배당체", "role": "bioactive", "part": "잎", "content_text": "종설 표 1: 잎 물 추출물 1560 µg/g; 메탄올 추출물 에틸아세테이트 분획 49.84 µg/g[2]", "activity_ko": "", "source": [2]},
 {"name": "Lutein", "name_ko": "루테인", "class": "카로티노이드", "role": "nutrient", "part": "잎", "content_text": "종설 표 1: 잎 추출물 에틸아세테이트 분획 76.92 µg/g[2]", "activity_ko": "", "source": [2]},
 {"name": "N-Feruloylserotonin", "name_ko": "N-페룰로일세로토닌", "class": "세로토닌 유도체(히드록시신남산 아마이드)", "role": "bioactive", "part": "잎", "content_text": "종설 표 1: 잎 메탄올 추출물 에틸아세테이트 분획 28.18 µg/g[2]", "activity_ko": "분리 성분 가운데 세로토닌 유도체의 티로시나아제 억제 활성이 가장 높음(효소 시험)[2]", "source": [2]},
 {"name": "N-p-Coumaroylserotonin", "name_ko": "N-p-쿠마로일세로토닌", "class": "세로토닌 유도체(히드록시신남산 아마이드)", "role": "bioactive", "part": "잎", "content_text": "종설 표 1: 잎 메탄올 추출물 에틸아세테이트 분획 7.6 µg/g[2]", "activity_ko": "티로시나아제 억제(효소 시험)[2]", "source": [2]},
 {"name": "3-O-p-Coumaroyl-1-(4-hydroxy-3,5-dimethoxyphenyl)-1-O-beta-D-glucopyranosylpropanol", "name_ko": "ESQ10(페닐프로파노이드 배당체)", "class": "페닐프로파노이드 배당체", "role": "bioactive", "part": "잎", "content_text": "종설 표 1: 잎 메탄올 추출물 에틸아세테이트 분획 82.91 µg/g[2]", "activity_ko": "LPS 자극 대식세포의 NO·PGE2·IL-6 생성과 iNOS·COX-2 발현 억제(세포 실험)[10]", "source": [2, 10]},
 {"name": "Taxifolin", "name_ko": "탁시폴린", "class": "디히드로플라보놀", "role": "bioactive", "part": "잎", "content_text": "종설 표 1: 물 추출물 에틸아세테이트 분획 27.91 µg/g[2]", "activity_ko": "", "source": [2]},
 {"name": "Rutin", "name_ko": "루틴", "class": "플라보놀 배당체", "role": "bioactive", "part": "잎", "content_text": "종설 표 1: 물 추출물 에틸아세테이트 분획 24.84 µg/g[2]", "activity_ko": "", "source": [2]},
 {"name": "Daucosterol", "name_ko": "다우코스테롤", "class": "스테롤 배당체", "role": "bioactive", "part": "잎", "content_text": "종설 표 1: 잎 추출물 에틸아세테이트 분획 20.76 µg/g[2]", "activity_ko": "", "source": [2]},
 {"name": "Saikochromone A", "name_ko": "사이코크로몬 A", "class": "크로몬 유도체", "role": "bioactive", "part": "잎", "content_text": "종설 표 1: 잎 추출물 에틸아세테이트 분획 9.84 µg/g[2]", "activity_ko": "", "source": [2]},
]

E = lambda: {k: "" for k in ["instrument","column","mobile_phase","gradient","flow","temp","detection","injection","sample_prep","standard","linearity","lod","loq","recovery"]}
c1 = E(); c1.update({
 "instrument": "Waters 2695 Alliance HPLC + 광다이오드 배열 검출기(PDA)",
 "column": "XBridge BEH C 계열 4.6 × 250 mm, 5 µm (C 뒤 숫자는 전문 추출본에서 빠짐)",
 "mobile_phase": "A 0.5% 아세트산 수용액, B 0.5% 아세트산 아세토니트릴",
 "gradient": "0.0분 A 85.0%·B 15.0% → 40.0분 A 57.5%·B 42.5% → 40.1–45.0분 B 100% → 45.0–55분 A 85.5%(원문 그대로)",
 "flow": "0.8 mL/min", "temp": "40 °C", "detection": "PDA 320 nm", "injection": "10 µL",
 "sample_prep": "말린 잎(60 °C 24시간, 200 mesh 분말)을 90 °C 물로 4시간 추출해 수용성 부분을 버리고, 남은 찌꺼기를 말려 70% 에탄올로 추출·농축·동결건조; 분석 시료 20 mg/mL"})
c2 = E(); c2.update({"instrument": "HPLC 2695 Alliance System (Waters)", "sample_prep": "말린 잎(60 °C 건조) 1 kg 을 70% 에탄올로 실온 48시간 추출, 여과·감압농축·동결건조"})
c3 = E(); c3.update({"instrument": "LC-MS/MS(기종은 초록에 없음)"})
assays = [
 {"role": "literature", "compound": "Tricin", "compound_ko": "트리신·p-쿠마르산(동시 지표성분)", "part": "잎(한라산 채취, 2019년 9월)", "content": "잎 추출물(SQE) 1 g 당 트리신 7.43 mg, p-쿠마르산 2.69 mg[3]", "method": "HPLC-PDA", "conditions": c1, "rationale": "저자들이 추출물의 주성분인 트리신과 p-쿠마르산을 지표성분(indicator components)으로 정해 정량했다; 검량선·검출한계·회수율은 본문에 없음[3]", "source": [3], "url": "https://doi.org/10.3390/nu12123762", "source_kind": "paper"},
 {"role": "literature", "compound": "p-Coumaric acid", "compound_ko": "p-쿠마르산·트리신", "part": "잎(한라산 채취)", "content": "잎 70% 에탄올 추출물 1 g 당 p-쿠마르산 1.13 mg, 트리신 0.82 mg[4]", "method": "HPLC", "conditions": c2, "rationale": "추출물의 두 주요 성분으로 정량해 세포 실험의 대조 농도(300 μg/mL 추출물에 해당하는 p-쿠마르산 1.8 μM·트리신 0.7 μM)를 정하는 데 썼다; 칼럼·이동상 등은 이전 논문을 따른다고만 적혀 있어 확인하지 못함[4]", "source": [4], "url": "https://doi.org/10.3390/ijms16059976", "source_kind": "paper"},
 {"role": "literature", "compound": "p-Coumaric acid", "compound_ko": "p-쿠마르산·미리세틴", "part": "추출물(부위·용매는 초록에 없음)", "content": "추출물 1 mg 당 p-쿠마르산 3.92 μg, 미리세틴 0.19 μg[8]", "method": "LC-MS/MS", "conditions": c3, "rationale": "항산화 활성 비교를 위해 추출물 속 두 성분을 정량했다; 초록만 확인했고 전문 확인 못함[8]", "source": [8], "url": "https://doi.org/10.1016/j.theriogenology.2022.03.009", "source_kind": "paper"},
]

d = {
 "slug": "sasa-quelpaertensis", "name_ko": "제주조릿대", "name_en": "Jeju dwarf bamboo",
 "scientific_name": "Sasa quelpaertensis Nakai",
 "aliases": ["제주조릿대순", "제주조릿대잎", "제주조릿대추출농축액", "산죽", "탐라세", "Broad-leaf bamboo", "Jeju dwarf bamboo", "Jeju-Joritdae"],
 "sections": sections, "compounds": compounds, "markers": [], "nutrients": [], "assays": assays,
 "production": [], "world": [], "gi": [], "orgs": [], "sources": sources,
}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
print("ok")
