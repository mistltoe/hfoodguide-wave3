import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
PM = "https://pubmed.ncbi.nlm.nih.gov/{}/"
PMC = "https://pmc.ncbi.nlm.nih.gov/articles/{}/"
A = "2026-11-02"
I1020 = "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020"
sources = [
 (1, "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 땃두릅나무(사용불가)·땃두릅나무줄기추출물(사용가능)", I1020, "식품의약품안전처", "2026-10-13"),
 (2, "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 땃두릅 나무 줄기 열수추출물 분말(식품원료 한시기준 제2022-1호, 한시적인정·제한적사용)", I1020, "식품의약품안전처", "2026-10-13"),
 (3, "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 독활(이명 땅두릅·땃두릅, Aralia cordata)·두릅(Aralia elata) 항목", I1020, "식품의약품안전처", "2026-10-13"),
 (4, "Progress in Oplopanax elatus research: Resources, propagation, traditional uses, phytochemistry, pharmacology, pharmacokinetics, quality control, and toxicity (J Ethnopharmacol 2025;346:119650, PMID 40107473)", PM.format(40107473), "Journal of Ethnopharmacology", A),
 (5, "Oplopanax elatus (Nakai) Nakai: chemistry, traditional use and pharmacology (Chin J Nat Med 2014;12(10):721-9, PMID 25443364)", PM.format(25443364), "Chinese Journal of Natural Medicines", A),
 (6, "Inhibitory Mechanisms of Water Extract of Oplopanax elatus on Lipopolysaccharide-Induced Inflammatory Responses in RAW 264.7 Murine Macrophage Cells (Chin J Integr Med 2020;26(9):670-676, PMID 31970677)", PM.format(31970677), "Chinese Journal of Integrative Medicine", A),
 (7, "Oploxynes A and B, polyacetylenes from the stems of Oplopanax elatus (J Nat Prod 2010;73(5):801-5, PMID 20387902)", PM.format(20387902), "Journal of Natural Products", A),
 (8, "The phenolic acids from Oplopanax elatus Nakai stems and their potential photo-damage prevention activity (J Nat Med 2022;76(1):39-48, PMID 34345982)", PM.format(34345982), "Journal of Natural Medicines", A),
 (9, "Sesquiterpenes From Oplopanax elatus Stems and Their Anti-Photoaging Effects by Down-Regulating Matrix Metalloproteinase-1 Expression via Anti-Inflammation (Front Chem 2021;9:766041, PMC8600134)", PMC.format("PMC8600134"), "Frontiers in Chemistry", A),
 (10, "Anticancer Activity of an Oplopanax elatus Stem Extract and Biologically Active Isolated Compounds (Curr Pharm Biotechnol 2018;19(3):258-264, PMID 29766799)", PM.format(29766799), "Current Pharmaceutical Biotechnology", A),
 (11, "[Chemical constituents from stems of Oplopanax elatus Nakai] (Zhongguo Zhong Yao Za Zhi 1993;18(2):104-5, PMID 8323692)", PM.format(8323692), "China Journal of Chinese Materia Medica", A),
 (12, "Studies on the anti-psoriasis constituents of Oplopanax elatus Nakai (Nat Prod Res 2009;23(4):334-42, PMID 19296374)", PM.format(19296374), "Natural Product Research", A),
 (13, "Falcarindiol and dichloromethane fraction are bioactive components in Oplopanax elatus: Colorectal cancer chemoprevention via induction of apoptosis and G2/M cell cycle arrest mediated by cyclin A upregulation (J Appl Biomed 2021, PMC8575125)", PMC.format("PMC8575125"), "Journal of Applied Biomedicine", A),
 (14, "Determination of six polyynes in Oplopanax horridus and Oplopanax elatus using polyethylene glycol modified reversed migration microemulsion electrokinetic chromatography (Electrophoresis 2014;35(20):2959-64, PMID 25070635)", PM.format(25070635), "Electrophoresis", A),
 (15, "The Oplopanax elatus genome reveals dammaradienol synthase evolution enabling reconstruction of RK type ginsenosides biosynthesis (Nat Commun 2026;17, PMC13444123)", PMC.format("PMC13444123"), "Nature Communications", A),
 (16, "Development of real-time PCR-based markers for differentiation of Oplopanax elatus and Aralia cordata in commercial food products (Food Sci Biotechnol 2023;32(14):2153-2161, PMC10582000)", PMC.format("PMC10582000"), "Food Science and Biotechnology", A),
 (17, "Improvement of somatic embryogenesis and plantlet conversion in Oplopanax elatus, an endangered medicinal woody plant (SpringerPlus 2013;2:428, PMC3766505)", PMC.format("PMC3766505"), "SpringerPlus", A),
 (18, "Shifts in rhizosphere microbial communities in Oplopanax elatus Nakai are related to soil chemical properties under different growth conditions (Sci Rep 2022;12:11485, PMC9262954)", PMC.format("PMC9262954"), "Scientific Reports", A),
 (19, "[Genetic variation of Oplopanax elatus (Nakai) Nakai (Araliaceae)] (Genetika 2010;46(5):631-9, PMID 20583598)", PM.format(20583598), "Genetika", A),
 (20, "The Identification of Araliaceae Species by ITS2 Genetic Barcoding and Pollen Morphology (Planta Med 2018;84(1):42-48, PMID 28701020)", PM.format(28701020), "Planta Medica", A),
 (21, "The pollen metamorphosis phenomenon in Panax ginseng, Aralia elata and Oplopanax elatus (Zygote 2009;17(1):1-17, PMID 19025728)", PM.format(19025728), "Zygote", A),
 (22, "Structures of four new triterpenoid saponins from the leaves of Oplopanax elatus Nakai (Yao Xue Xue Bao 2004;39(5):354-8, PMID 15338878)", PM.format(15338878), "Acta Pharmaceutica Sinica", A),
 (23, "[Textual study of ginseng in Wupu Bencao] (Zhongguo Zhong Yao Za Zhi 2010;35(12):1630-2, PMID 20815223)", PM.format(20815223), "China Journal of Chinese Materia Medica", A),
 (24, "Integrated transcriptomic and targeted triterpenoid profiling reveals key enzymes in triterpenoid biosynthesis of Oplopanax elatus (Sci Rep 2026;16, PMC13046990)", PMC.format("PMC13046990"), "Scientific Reports", A),
 (25, "Pharmacokinetic profiles of falcarindiol and oplopandiol in rats after oral administration of polyynes extract of Oplopanax elatus (Chin J Nat Med 2016;14(9):714-720, PMID 27667518)", PM.format(27667518), "Chinese Journal of Natural Medicines", A),
 (26, "Adventitious root cultures of Oplopanax elatus inhibit LPS-induced inflammation via suppressing MAPK and NF-κB signaling pathways (In Vitro Cell Dev Biol Anim 2019, PMID 31529418)", PM.format(31529418), "In Vitro Cellular & Developmental Biology - Animal", A),
 (27, "Polyyne-Enriched Extract from Oplopanax elatus Significantly Ameliorates the Progression of Colon Carcinogenesis in Apc(Min/+) Mice (Molecules 2017;22(10):1593, PMC6151504)", PMC.format("PMC6151504"), "Molecules", A),
 (28, "Comparative analysis of the transcriptomes from regenerated plants and root explants of endangered Oplopanax elatus (Genes Genomics 2024;46(12):1387-1398, PMID 39320642)", PM.format(39320642), "Genes & Genomics", A),
 (29, "Adventitial root extract of Oplopanax elatus alleviates rheumatoid arthritis via inhibiting NETosis (Clin Rheumatol 2026, PMID 42461565)", PM.format(42461565), "Clinical Rheumatology", A),
 (30, "Improving Flavonoid Accumulation of Bioreactor-Cultured Adventitious Roots in Oplopanax elatus Using Yeast Extract (Plants (Basel) 2023, PMC10255709)", PMC.format("PMC10255709"), "Plants", A),
]

S = {}
S["overview"] = ("개요", """땃두릅나무(Oplopanax elatus (Nakai) Nakai)는 인삼과 같은 두릅나무과(Araliaceae)에 속하는 낙엽성 목본으로, 한국·중국 동북부·러시아 극동에 자라며 이들 지역에서 신경쇠약·심혈관 질환 등에 민간약으로 써 왔다[4, 5, 13]. 야생 자원이 줄고 종자 번식이 어려워 논문에서는 '멸종위기(endangered)' 약용식물로 소개된다[4, 17, 28].

식약처 「식품원료 목록」에서 '땃두릅나무'(전체) 항목은 '사용불가'이고, 식품원료로 쓸 수 있는 것은 줄기를 원료로 한 '땃두릅나무줄기추출물'뿐이다[1]. 이 원료는 건조·분쇄·물 추출·여과·농축·건조·분쇄로 만들어야 하며, 식품 100 g 당 액상차 60 mg 이하, 고형차 60 mg 이하로만 쓸 수 있다[1]. 같은 목록에는 '땃두릅 나무 줄기 열수추출물 분말'이 식품원료 한시기준 제2022-1호(2022.4.4.)로 인정된 기록도 남아 있으며, 여기서는 총아플라톡신과 오크라톡신 A 기준이 함께 정해졌다[2].

줄기에서는 폴리아세틸렌(오플록신·팔카린디올 등)·페닐프로파노이드 배당체(시린긴)·페놀산·세스퀴테르펜이 분리되었다[6–9, 11]. 추출물·성분의 항염증·항암·광노화 억제 효과가 보고되었지만 모두 세포·동물 실험 결과이며, 사람을 대상으로 효과를 확인한 연구는 확인하지 못함.""")
S["history"] = ("역사와 전통적 이용", """땃두릅나무는 중국·한국·러시아에서 오랫동안 민간약으로 쓰였고, 주로 신경쇠약, 조현병, 심혈관 질환 등에 쓰였다고 정리되어 있다[4]. 러시아에서는 '고전적 적응원(adaptogen)'으로 지정되었다고 한다[5]. 중국 문헌 연구에서는 『오보본초(吳普本草)』에 '인삼'으로 기록된 식물 일부가 실제로는 땃두릅나무를 가리킨다고 해석하기도 했다[23].

연구 대상이 된 전통 약재 부위는 주로 뿌리·뿌리껍질이며, 신경쇠약·조현병·류마티스·심혈관 질환 등이 적응증으로 소개된다[13, 4]. 한 연구는 당뇨, 우울, 류마티스 관절염, 세균·곰팡이 감염에 긍정적이었다는 사람 자료를 인용했으나, 그 원 자료의 설계와 규모는 확인하지 못함.

국내에서 줄기를 식품원료로 쓰게 된 것은 2022년 한시적 인정(제2022-1호)을 거쳐 '땃두릅나무줄기추출물'이 목록에 오른 뒤의 일이다[1, 2].""")
S["biology"] = ("생물학적 특징", """땃두릅나무는 두릅나무과 땃두릅나무속(Oplopanax)의 목본으로, 세계에 세 종(O. elatus·O. horridus·O. japonicus)만 있는 작은 속에 속한다[13]. 동아시아(중국 동북부, 러시아 극동, 한국)에 분포한다[13]. 클론을 형성하는 유존(relict) 희귀종으로 기술되며, 알로자임 분석에서 유전 다양성 지수는 낮았지만(P = 25%, He = 0.113) 유전자형 다양성(D = 0.97)은 영양번식 종 평균보다 높아 종자 번식도 기여하는 것으로 해석되었다[19].

꽃가루는 성숙하면서 크기가 줄어드는 변형을 거쳐 최종적으로 한쪽에 돌기가 있는 달걀꼴(평균 지름 약 18 µm)이 되며, 이는 인삼(둥근 꼴, 약 16 µm)·두릅나무(돌기 하나 둥근 꼴, 약 15 µm)와 구별된다[21]. 남한의 4개 산에서 모은 13개체의 종자로 체세포배 발생을 연구한 결과가 있어 국내 자생이 확인된다[17]. 나무 높이·잎 모양·개화기 등 세부 형태는 접근 가능한 공식 식물지에서 확인하지 못함.""")
S["related_species"] = ("근연종과 혼동 주의", """같은 속에는 북미 태평양 연안의 O. horridus(데빌스 클럽)와 일본의 O. japonicus가 있으며, 세 종은 분류상 가깝지만 화학 성분과 약리 작용이 다르다[13]. 두 종의 폴리아인 6종을 함께 정량한 연구에서도 성분의 종류와 양이 뚜렷이 달랐으므로, O. horridus 자료를 땃두릅나무에 옮겨 쓰면 안 된다[14].

이름 혼동이 특히 크다. 식약처 목록에서 독활(Aralia cordata, 땅두릅)의 이명에 '땃두릅'이 올라 있고, 두릅(Aralia elata)도 별개 원료로 실려 있다[3]. 땃두릅나무와 독활은 국내에서 모두 '두릅'으로 불리고 뿌리 모양이 비슷해 비싼 땃두릅나무 대신 값싼 독활을 섞는 위조 가능성이 지적되었고, 이를 가리기 위한 종 특이 실시간 PCR 표지가 개발되어 시판 제품 10건에 적용되었다[16]. 러시아 연해주의 두릅나무과 6종은 ITS2 바코드와 꽃가루 최종 형태로 구별할 수 있었다[20].

식품원료 지위도 서로 다르다: 땃두릅나무는 줄기 추출물만 사용가능이고, 독활은 잎이 사용가능·뿌리가 제한적사용이며, 두릅은 순·잎이 사용가능이다[1, 3].""")
S["cultivation"] = ("재배와 채취", """땃두릅나무는 원료 대부분을 야생에서 얻어 왔으나, 야생 자원 고갈과 인공 재배 기술 부족으로 상업적 이용이 제한된다[4]. 종자로 번식하기 어려워 대량 재배가 힘들다는 점도 여러 연구에서 지적되었다[28, 17].

국내에서는 산림 연구기관이 4개 산에서 채집한 종자를 이용해 체세포배 발생 조건을 최적화했고, 5% 자당 배지에서 체세포배가 가장 많이 유도되었으며 인공 토양에 옮긴 묘의 80%가 순화에 성공했다[17]. 뿌리 조직에서 식물체를 재분화시킨 연구와 그 전사체 비교도 이루어졌다[28, 24].

중국 장백산 지역에서는 자생지에서 재배지로 옮겨 심은 개체의 근권 토양을 비교한 결과, 재배지 토양이 pH가 높고 유기물·유효 질소가 적었으며 미생물 군집도 달라져 유기질 비료 관리가 필요하다고 제안되었다[18]. 생물반응기에서 부정근(adventitious root)을 배양해 원료를 얻는 방법도 연구되며, 효모 추출물 100 mg/L 처리가 플라보노이드 축적을 높였다고 보고되었다[30, 4]. 국내 재배 면적·생산량 통계는 확인하지 못함.""")
S["processing"] = ("가공과 추출", """국내 식품원료인 '땃두릅나무줄기추출물'은 줄기를 건조·분쇄한 뒤 물로 추출·여과·농축·건조·분쇄하는 공정으로 만들도록 정해져 있다[1]. 한시적 인정 당시의 '줄기 열수추출 분말'은 세척·건조 → 분쇄 → 추출 → 여과 → 농축 → 동결건조 → 분쇄 → 금속성 이물 제거 순서였고, 곰팡이독소류를 줄이기 위해 제조 단계별로 관리하도록 했다[2]. 사용 용도는 액상차·고형차로, 둘 다 100 g 당 60 mg 이하이다[1, 2].

연구에서는 줄기 열수추출물에서 시린긴을 주성분으로 분리했고, 그 함량은 건조 식물 기준 214.0 µg/g이었다[6]. 줄기 추출물의 에틸아세테이트 분획에서는 폴리아세틸렌인 팔카린디올·오플로판디올이 얻어졌다[10]. 뿌리껍질 메탄올 추출물에서는 두 폴리아인이 각각 141.6 mg/g, 169.7 mg/g으로 추출물의 72.7%를 차지했고, 디클로로메탄 분획에서 81.2%까지 높아졌다[13].

이처럼 물 추출물은 배당체·페놀성 성분 중심이고, 유기용매 분획은 폴리아인 중심이어서 추출 용매에 따라 조성이 크게 달라진다[6, 13]. 건강기능식품 원료 생산실적은 확인하지 못함.""")
S["genetics"] = ("유전·계통", """2026년 발표된 염색체 수준 유전체 분석에서 땃두릅나무는 이질사배체(2n = 4x = 48)로, 반수체 유전체 크기는 약 762 Mb로 추정되었고 이형접합률은 8.5%로 높았다[15]. 두 반수체형이 24개 의사염색체에 1.45 Gb로 배열되었고(BUSCO 99.38%), 단백질 암호 유전자 61,842개가 예측되었다[15]. 두 아유전체는 약 2,320만 년 전에 갈라진 것으로 추정되었다[15].

같은 연구는 땃두릅나무 잎이 RK형 진세노사이드의 전구 골격인 담마라디엔올을 쌓지만 RK형 진세노사이드는 만들지 않으며, 그 이유가 C-12 수산화효소의 기능 상실 때문이라고 보고했다[15]. 담마라디엔올 합성효소(OeOSC14)는 다기능 트리테르펜 합성효소가 중복·신기능화되어 생겼다고 설명되었다[15].

재분화 조직의 전사체 분석에서는 베타-아미린 합성효소와 루페올 합성효소 발현이 각각 약 3배, 30배 높아 트리테르펜 축적과 연결되었다[24]. 러시아 자생 개체의 알로자임 분석도 수행되었고, ITS2 바코드는 종 구별에는 충분했으나 지역 구별에는 부족했다[19, 20].""")
S["safety"] = ("안전성", """식약처 목록에서 땃두릅나무 전체는 '사용불가'이며, 식품에는 정해진 제조 조건으로 만든 줄기 물 추출물만 액상차·고형차 100 g 당 60 mg 이하로 쓸 수 있다[1]. 한시적 인정 기준에는 총아플라톡신 15.0 µg/kg 이하(B1·B2·G1·G2 합, B1은 10.0 µg/kg 이하), 오크라톡신 A 5.0 µg/kg 이하가 포함되어 곰팡이독소 관리가 핵심 안전 요건임을 보여 준다[2]. 뿌리·잎 등 다른 부위는 식품원료로 인정되지 않았다[1].

2025년 총설은 독성 연구를 함께 정리했으나, 줄기 물 추출물의 반복투여 독성·유전독성 수치는 초록만으로 확인하지 못함. 쥐에 폴리아인 추출물을 먹인 약동학 연구는 팔카린디올·오플로판디올이 혈장에 나타남을 보였으나 독성 평가는 아니었다[25].

항염증(생쥐 귀 부종, 경구 50–300 mg/kg), 대장암 억제(Apc 변이 생쥐, 사료 0.2%), 급성 폐 손상 억제(부정근 추출물 200 mg/kg), 관절염 억제(부정근 추출물) 같은 결과는 모두 동물·세포 실험이며 사람 효능 근거가 아니다[6, 27, 26, 29]. 팔카린디올은 강한 세포 증식 억제 활성을 보인 폴리아인이므로, 뿌리껍질·유기용매 분획처럼 폴리아인이 농축된 원료를 식품용 줄기 물 추출물과 같은 것으로 보면 안 된다[13]. 이름이 비슷한 독활(땅두릅)과 섞이지 않도록 원료 확인이 필요하다[16]. 사람 대상 부작용·상호작용 보고와 공공기관 알레르기 정보는 확인하지 못함.""")

compounds = [
 dict(name="Syringin", name_ko="시린긴", **{"class":"페닐프로파노이드 배당체"}, role="marker", part="줄기", content_text="줄기 열수추출물 기준 건조 식물 214.0 µg/g(w/w)[6]; 줄기에서 분리[11]", activity_ko="줄기 열수추출물이 RAW 264.7 대식세포에서 NO·PGE2 생성 억제(PGE2 IC50 135.2 µg/mL), 생쥐 귀 부종 억제 — 추출물의 세포·동물 결과[6]", source=[6, 11]),
 dict(name="Falcarindiol", name_ko="팔카린디올", **{"class":"폴리아세틸렌(폴리아인)"}, role="bioactive", part="줄기; 뿌리껍질", content_text="뿌리껍질 메탄올 추출물 141.6 mg/g, 디클로로메탄 분획 165.7 mg/g[13]; 줄기에서 분리(함량 미보고)[7, 10]", activity_ko="대장암세포 HCT-116 증식 억제 IC50 1.7 µM — 세포 결과[13]; LPS 자극 대식세포 NO·PGE2 생성 억제 — 세포 결과[7]", source=[7, 10, 13]),
 dict(name="Oplopandiol", name_ko="오플로판디올", **{"class":"폴리아세틸렌(폴리아인)"}, role="bioactive", part="줄기; 뿌리껍질", content_text="뿌리껍질 메탄올 추출물 169.7 mg/g, 디클로로메탄 분획 204.4 mg/g[13]; 줄기에서 분리(함량 미보고)[7, 10]", activity_ko="HCT-116 IC50 15.5 µM로 팔카린디올보다 약함 — 세포 결과[13]; NO·PGE2 생성 억제 — 세포 결과[7]", source=[7, 10, 13]),
 dict(name="Oploxyne A", name_ko="오플록신 A", **{"class":"폴리아세틸렌"}, role="bioactive", part="줄기", content_text="줄기에서 새로 분리(9,10-epoxyheptadeca-4,6-diyne-3,8-diol), 함량 미보고[7]", activity_ko="LPS 자극 대식세포 NO·PGE2 생성 억제 — 세포 결과[7]", source=[7]),
 dict(name="Oploxyne B", name_ko="오플록신 B", **{"class":"폴리아세틸렌"}, role="bioactive", part="줄기", content_text="줄기에서 새로 분리(10-methoxyheptadeca-4,6-diyne-3,8,9-triol), 함량 미보고[7]", activity_ko="초록에 활성 보고 없음[7]", source=[7]),
 dict(name="Oplodiol", name_ko="오플로디올", **{"class":"세스퀴테르펜(유데스만형)"}, role="bioactive", part="줄기", content_text="줄기 70% 에탄올 추출물에서 분리한 기지 세스퀴테르펜 10종 중 하나, 함량 미보고[9]", activity_ko="줄기 세스퀴테르펜 일부가 UVB 조사 각질세포(HaCaT)에서 MMP-1 감소·콜라겐 증가 — 세포 결과[9]", source=[9]),
 dict(name="Eurylophenoside A", name_ko="유릴로페노사이드 A", **{"class":"페놀산 배당체"}, role="bioactive", part="줄기", content_text="줄기에서 분리한 페놀산 25종 중 신규 화합물, 함량 미보고[8]", activity_ko="UVB 조사 HaCaT 세포 생존율 저하를 농도 의존적으로 억제 — 세포 결과[8]", source=[8]),
 dict(name="5-Methoxylariciresinol 4-O-glucoside", name_ko="5-메톡시라리시레시놀 4-O-글루코사이드", **{"class":"리그난 배당체"}, role="bioactive", part="뿌리·줄기", content_text="뿌리와 줄기에서 분리한 신규 리그난, 함량 미보고[12]", activity_ko="초록에 활성 수치 없음[12]", source=[12]),
 dict(name="Daucosterol", name_ko="다우코스테롤", **{"class":"스테롤 배당체"}, role="bioactive", part="줄기", content_text="줄기에서 분리, 함량 미보고[11]", activity_ko="이 종에서의 활성은 확인하지 못함[11]", source=[11]),
 dict(name="beta-Sitosterol", name_ko="베타-시토스테롤", **{"class":"식물스테롤"}, role="nutrient", part="줄기", content_text="줄기에서 분리, 함량 미보고[11]", activity_ko="이 종에서의 활성은 확인하지 못함[11]", source=[11]),
 dict(name="Dammaradienol", name_ko="담마라디엔올", **{"class":"트리테르펜(담마란형)"}, role="bioactive", part="잎(줄기·뿌리 등 조직별 GC-MS 비교)", content_text="잎에 축적, 수치는 본문 그림에만 있음[15]", activity_ko="RK형 진세노사이드의 전구 골격; 이 종은 C-12 수산화효소 기능 상실로 RK형을 만들지 않음[15]", source=[15]),
 dict(name="Lupeol", name_ko="루페올", **{"class":"트리테르펜"}, role="bioactive", part="뿌리·재분화 조직", content_text="재분화 8주 조직에서 뿌리(0주)보다 현저히 높음(HPLC 정량, 수치는 초록에 없음)[24]", activity_ko="생합성 연구 대상 — 활성 시험 아님[24]", source=[24]),
 dict(name="Oleanolic acid", name_ko="올레아놀산", **{"class":"트리테르펜"}, role="bioactive", part="뿌리·재분화 조직", content_text="재분화 8주 조직에서 뿌리(0주)보다 현저히 높음(수치는 초록에 없음)[24]", activity_ko="생합성 연구 대상 — 활성 시험 아님[24]", source=[24]),
 dict(name="Cirenshenoside S", name_ko="시렌셰노사이드 S", **{"class":"트리테르펜 사포닌(루판형)"}, role="bioactive", part="잎", content_text="잎에서 새로 분리, 함량 미보고[22]", activity_ko="초록에 활성 보고 없음[22]", source=[22]),
]

assays = [
 {"role":"literature","compound":"Syringin","compound_ko":"시린긴","part":"줄기(열수추출물)","content":"건조 식물 기준 214.0 µg/g(w/w)[6]","method":"",
  "conditions":{k:"" for k in ["instrument","column","mobile_phase","gradient","flow","temp","detection","injection","sample_prep","standard","linearity","lod","loq","recovery"]},
  "rationale":"식품원료와 같은 부위·같은 추출(물)에서 주성분으로 분리·정량된 성분이다[6]. 전문 확인 못함 — 분석 기기·칼럼·이동상 등은 초록에 없어 비워 둠[6]","source":[6],"url":PM.format(31970677),"source_kind":"paper"},
 {"role":"literature","compound":"Falcarindiol","compound_ko":"팔카린디올(오플로판디올 동시 정량)","part":"뿌리껍질(메탄올 추출물) — 식품원료 부위(줄기)와 다름","content":"추출물 141.6 mg/g, 오플로판디올 169.7 mg/g; 디클로로메탄 분획 165.7·204.4 mg/g[13]","method":"HPLC-PDA",
  "conditions":{"instrument":"Waters 2960 HPLC(사원 펌프, 자동주입기), Waters 996 광다이오드 배열 검출기","column":"","mobile_phase":"A: 아세토니트릴, B: 물","gradient":"A 36%(0–10분) → 50%(20분) → 65%(35분) → 75%(40분) → 100%(45–50분) → 36%(53–60분)","flow":"1 ml/min","temp":"","detection":"UV 202 nm","injection":"10 µl","sample_prep":"건조 뿌리껍질 분말을 메탄올로 환류 추출(2회), 감압 농축·동결건조","standard":"추출물에서 분취 HPLC로 분리하고 NMR·MS로 확인한 팔카린디올·오플로판디올","linearity":"","lod":"","loq":"","recovery":""},
  "rationale":"폴리아인 두 성분이 추출물의 72.7%를 차지하는 주성분이고 팔카린디올이 활성 성분으로 지목되어 표준화 지표로 제안되었다(전문 확인)[13]. 두 성분은 줄기에도 있으나[7], 줄기 물 추출물의 정량값은 확인하지 못함; 칼럼 규격·검출한계·회수율은 원문에 없음[13]","source":[13, 7],"url":PMC.format("PMC8575125"),"source_kind":"paper"},
]

d = dict(slug="oplopanax-elatus", name_ko="땃두릅나무", name_en="Oplopanax elatus", scientific_name="Oplopanax elatus (Nakai) Nakai",
  aliases=["땃두릅나무줄기추출물", "Oplopanax elatus Nakai"],
  sections=[{"key":k,"title":v[0],"body":v[1]} for k,v in S.items()],
  compounds=compounds, markers=[], nutrients=[], assays=assays, production=[], world=[], gi=[], orgs=[],
  sources=[dict(n=n,title=t,url=u,publisher=p,accessed=a) for n,t,u,p,a in sources])
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in d["sections"]: print(s["key"], len(s["body"]))
