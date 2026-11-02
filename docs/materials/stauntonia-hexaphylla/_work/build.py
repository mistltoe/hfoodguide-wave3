import json
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "dossier.json"
ACC = "2026-11-02"


def pm(pmid, title, journal, pmc=None):
    url = f"https://pmc.ncbi.nlm.nih.gov/articles/{pmc}/" if pmc else f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
    pub = f"{journal} (PMC 전문)" if pmc else f"{journal} (PubMed 초록)"
    return {"title": f"{title} (PMID {pmid})", "url": url, "publisher": pub, "accessed": ACC}


S = [
    {"title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 멀꿀열매(Stauntonia hexaphylla (Thunb.) Decne. / Rajania hexaphylla Thunb., 식품원료 A코드, 사용가능, '사용가능부위 : 열매', 이명 야모과) 행과 같은 과 으름덩굴속(Akebia) 행(로컬 원자료 I1020_20261013)",
     "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
    pm("29361789", "Anti-Inflammatory Effects of a Stauntonia hexaphylla Fruit Extract in Lipopolysaccharide-Activated RAW-264.7 Macrophages and Rats by Carrageenan-Induced Hind Paw Swelling. Nutrients 2018;10(1):110 (doi:10.3390/nu10010110)", "Nutrients", "PMC5793338"),
    pm("40943332", "Steam-Processed Stauntonia hexaphylla (Thunb.) Decne Fruit Stimulates Osteoblast Differentiation in MC3T3-E1 Cells and Inhibits Osteoclastogenesis in RAW 264.7 Cells. Int J Mol Sci 2025;26(17):8411 (doi:10.3390/ijms26178411)", "International Journal of Molecular Sciences", "PMC12428769"),
    pm("40563484", "Synergistic Effect of Stauntonia hexaphylla (Thunb.) Decne Fruit and Leaf on RAW 264.7 Osteoclast and MC3T3-E1 Osteoblast Differentiation. Biomolecules 2025;15(6):844 (doi:10.3390/biom15060844)", "Biomolecules", "PMC12190245"),
    pm("31301930", "Bioactive triterpene glycosides from the fruit of Stauntonia hexaphylla and insights into the molecular mechanism of its inflammatory effects. Bioorg Med Chem Lett 2019;29(16):2085-2089 (doi:10.1016/j.bmcl.2019.07.010)", "Bioorganic & Medicinal Chemistry Letters"),
    pm("42606560", "A Comprehensive Review of Phytochemical Constituents and Biological Activities of Stauntonia hexaphylla (Thunb.) Decne. J AOAC Int 2026 (doi:10.1093/jaoacint/qsag079)", "Journal of AOAC International"),
    pm("33796658", "Complete chloroplast genome sequence of Stauntonia hexaphylla (Ranunculales: Lardizabalaceae), a species endemic to Korea. Mitochondrial DNA B Resour 2021;6(3):860-861 (doi:10.1080/23802359.2021.1885320)", "Mitochondrial DNA Part B", "PMC7971286"),
    pm("27069393", "Native fruit tree genetic resources in Japan. Breed Sci 2016;66(1):82-9 (doi:10.1270/jsbbs.66.82)", "Breeding Science"),
    pm("30808589", "Isolation, structural elucidation, and insights into the anti-inflammatory effects of triterpene saponins from the leaves of Stauntonia hexaphylla. Bioorg Med Chem Lett 2019;29(8):965-969 (doi:10.1016/j.bmcl.2019.02.022)", "Bioorganic & Medicinal Chemistry Letters"),
    pm("32823787", "Enhancement of an In Vivo Anti-Inflammatory Activity of Oleanolic Acid through Glycosylation Occurring Naturally in Stauntonia hexaphylla. Molecules 2020;25(16):3699 (doi:10.3390/molecules25163699)", "Molecules"),
    pm("31305145", "The chemical constituents of ethanolic extract from Stauntonia hexaphylla leaves and their anti-inflammatory effects. Nat Prod Res 2021;35(11):1852-1855 (doi:10.1080/14786419.2019.1638385)", "Natural Product Research"),
    pm("28326319", "Inhibitory Activities of Stauntonia hexaphylla Leaf Constituents on Rat Lens Aldose Reductase and Formation of Advanced Glycation End Products and Antioxidant. Biomed Res Int 2017;2017:4273257 (doi:10.1155/2017/4273257)", "BioMed Research International"),
    pm("26271279", "Stauntonia hexaphylla (Lardizabalaceae) leaf methanol extract inhibits osteoclastogenesis and bone resorption activity via proteasome-mediated degradation of c-Fos protein and suppression of NFATc1 expression. BMC Complement Altern Med 2015;15:280 (doi:10.1186/s12906-015-0801-6)", "BMC Complementary and Alternative Medicine"),
    pm("34776829", "Stauntonia hexaphylla leaf extract (YRA-1909) suppresses inflammation by modulating Akt/NF-κB signaling in lipopolysaccharide-activated peritoneal macrophages and rodent models of inflammation. Food Nutr Res 2021;65 (doi:10.29219/fnr.v65.7666)", "Food & Nutrition Research"),
    pm("30200538", "Simultaneous Determination of Chlorogenic Acid Isomers and Metabolites in Rat Plasma Using LC-MS/MS and Its Application to A Pharmacokinetic Study Following Oral Administration of Stauntonia hexaphylla Leaf Extract (YRA-1909) to Rats. Pharmaceutics 2018;10(3):143 (doi:10.3390/pharmaceutics10030143)", "Pharmaceutics"),
    pm("33505932", "Anti-Fatigue Activity of a Mixture of Stauntonia hexaphylla (Thunb.) Decaisne and Vaccinium bracteatum Thunb. Fruit Extract. Prev Nutr Food Sci 2020;25(4):380-388 (doi:10.3746/pnf.2020.25.4.380)", "Preventive Nutrition and Food Science"),
    pm("33240033", "Antipostmenopausal effects of Stauntonia hexaphylla and Vaccinium bracteatum fruit combination in estrogen-deficient rats. Food Nutr Res 2020;64 (doi:10.29219/fnr.v64.5233)", "Food & Nutrition Research"),
    pm("32790676", "Protective effects of combination of Stauntonia hexaphylla and Cornus officinalis on testosterone-induced benign prostatic hyperplasia through inhibition of 5α-reductase type 2 and induced cell apoptosis. PLoS One 2020;15(8):e0236879 (doi:10.1371/journal.pone.0236879)", "PLoS One"),
    pm("31812646", "The therapeutic effects of Stauntonia hexaphylla in benign prostate hyperplasia are mediated by the regulation of androgen receptors and 5α-reductase type 2. J Ethnopharmacol 2020;250:112446 (doi:10.1016/j.jep.2019.112446)", "Journal of Ethnopharmacology"),
    pm("36896319", "Stauntonia hexaphylla Extract Ameliorates Androgenic Alopecia by Inhibiting Androgen Signaling in Testosterone-induced Alopecia Mice. Iran J Pharm Res 2023;21(1):e133333 (doi:10.5812/ijpr-133333)", "Iranian Journal of Pharmaceutical Research"),
    pm("7763949", "Triterpenoid glycosides from Stauntonia hexaphylla (staunosides A, B). Phytochemistry 1993;33(6):1469-73 (doi:10.1016/0031-9422(93)85113-6)", "Phytochemistry"),
    pm("7764286", "Triterpenoid glycosides from Stauntonia hexaphylla (staunosides D, E). Phytochemistry 1993;34(5):1389-94 (doi:10.1016/0031-9422(91)80035-y)", "Phytochemistry"),
    pm("1367653", "A saponin from callus tissue of Stauntonia hexaphylla. Phytochemistry 1991;30(7):2425-7 (doi:10.1016/0031-9422(91)83672-8)", "Phytochemistry"),
    pm("40635208", "The Genus Stauntonia DC.: Botany, Phytochemistry, Bioactivity, and Application. Comb Chem High Throughput Screen 2026;29(10):1469-1490 (doi:10.2174/0113862073390090250625111201)", "Combinatorial Chemistry & High Throughput Screening"),
    pm("33676415", "The complete chloroplast genome of Stauntonia chinensis and compared analysis revealed adaptive evolution of subfamily Lardizabaloideae species in China. BMC Genomics 2021;22(1):161 (doi:10.1186/s12864-021-07484-7)", "BMC Genomics"),
    pm("42633707", "Botany, extraction methods, chemical constituents, pharmacological activities, and food applications of Stauntonia chinensis. Nat Prod Res 2026 (doi:10.1080/14786419.2026.2720789)", "Natural Product Research"),
    pm("36657852", "A novel Stauntonia leucantha fruits arabinogalactan: isolation and structural characterization. Carbohydr Polym 2023;303:120481 (doi:10.1016/j.carbpol.2022.120481)", "Carbohydrate Polymers"),
]
for i, s in enumerate(S, 1):
    s["n"] = i
S = [{"n": s["n"], "title": s["title"], "url": s["url"], "publisher": s["publisher"], "accessed": s["accessed"]} for s in S]

sections = [
    {"key": "overview", "title": "한눈에 보기", "body":
     "멀꿀(Stauntonia hexaphylla (Thunb.) Decne.)은 으름덩굴과(Lardizabalaceae) 멀꿀속에 속하는 늘푸른 덩굴식물로, 손바닥 모양의 겹잎과 작은 종 모양 꽃, 먹을 수 있는 열매를 맺는다[2]. 한국·일본·중국에 널리 분포한다고 보고되며, 한국에서는 'Mulkul', 일본에서는 'Mube', 중국에서는 'Ye-mu-gua'라는 이름으로 건강식품 시장에 알려졌다고 한다[2][3].\n\n"
     "식품의약품안전처 「식품원료 목록」에는 '멀꿀열매' 한 행이 식품원료(A코드)로 올라 있고, 사용 여부는 '사용가능', 사용 조건은 '사용가능부위 : 열매'이다[1]. 같은 행에는 이명 '야모과', 영문명 'Japanese staunton vine, Stauntonia vine', 이명 학명 Rajania hexaphylla Thunb.가 적혀 있다[1]. 이 목록에서 멀꿀의 잎·줄기·뿌리 행은 찾지 못했으므로, 국내에서 식품으로 쓸 수 있는 부위는 열매뿐이다[1].\n\n"
     "열매에는 네오클로로젠산·클로로젠산·크립토클로로젠산 같은 카페오일퀸산과 트리테르펜 배당체가 들어 있다고 보고되었다[2][4][5]. 연구 상당수는 열매가 아닌 잎 추출물로 이루어졌고, 효능 연구는 세포·동물 실험 수준이며 열매로 한 사람 임상시험은 확인하지 못했다."},
    {"key": "history", "title": "이용의 역사", "body":
     "멀꿀 열매는 한국·일본·중국에서 전통적으로 구충제로 쓰여 왔다고 한 연구는 소개한다[2]. 열매·잎·줄기·뿌리 등 여러 부위가 동양 의학에서 진통·진정·이뇨 목적으로 쓰였다고 보고된다[3][4]. 멀꿀은 한국·일본·중국에서 류머티즘·골다공증과 진통·진정·이뇨 목적의 전통 약재로 널리 쓰였다는 기술도 있다[14].\n\n"
     "일본의 토착 과수 자원을 정리한 총설은 사람들이 선사시대부터 반세기 전쯤까지 야생 과실을 먹어 왔고, 최근 머루류·으름덩굴류·다래 등과 함께 멀꿀이 소규모 재배에 들어갔다고 적었다[8]. 한국에서는 전라남도 장흥에서 집약적으로 재배된다고 보고되었다[7].\n\n"
     "근래에는 열매를 증숙(찌기)하는 가공이 약효를 높이려는 목적으로 흔히 쓰인다고 소개되며, 증숙은 전통 한약 수치법(법제)의 하나로 설명된다[3]. 2017년 4월부터 멀꿀 잎 추출물이 류머티즘 관절염 환자 대상 2상 임상시험에 들어갔다는 기술이 있으나, 이는 식품원료 부위가 아닌 잎으로 만든 의약품 후보에 관한 것이다[15][1]."},
    {"key": "biology", "title": "식물학적 특징", "body":
     "멀꿀은 손바닥 모양 잎과 작은 종 모양 꽃을 가진 늘푸른 덩굴식물이며, 열매를 먹을 수 있다[2]. 아열대성 덩굴로 소개되며, 한국에서는 고흥·해남 등 남해안 지역에 자생한다고 보고되었다[3][7]. 같은 엽록체 유전체 논문의 제목은 '한국 고유종'이라 했지만, 다른 논문들은 한국·일본·중국에 분포한다고 적어 서로 다르다[7][2][13].\n\n"
     "국내 연구용 열매는 장흥의 재배 농가에서 11월 하순부터 12월 초순 사이에 완숙과로 수확되었다[3][4]. 열매 추출물(열수)은 페놀산이 많고 플라보노이드는 거의 검출되지 않은 반면, 잎에는 루틴·나린진·루테올린-7-O-글루코사이드 같은 플라보노이드가 다양하게 들어 있어 부위별 성분이 크게 달랐다[4]. 총페놀 함량은 열매 1.02 ± 0.04 mg GAE/g, 잎 7.66 ± 0.07 mg GAE/g으로 잎이 약 7배 높았다[4].\n\n"
     "식물 전체에서는 지금까지 트리테르페노이드 25종, 사포닌 47종, 플라보노이드 21종, 페놀 화합물 14종, 리그난 3종 등 2차 대사산물 115종이 보고되었고, 사포닌이 주요 성분군으로 정리되었다[6]. 이 숫자는 잎·줄기·열매 등 여러 부위를 합친 것이다[6]."},
    {"key": "related_species", "title": "근연종과 혼동 주의", "body":
     "멀꿀과 같은 으름덩굴과에는 으름덩굴속(Akebia)이 있으며, 식약처 「식품원료 목록」에서 으름덩굴(Akebia quinata)과 삼엽으름덩굴(Akebia trifoliata), Five-leaf akebia(Akebia x pentaphylla)는 잎과 열매가 사용가능 원료이다[1]. 반면 으름덩굴의 줄기·뿌리와 '목통줄기'는 사용불가로 되어 있어, 멀꿀과 으름덩굴은 사용 가능 부위가 다르다[1]. 이 문서의 성분·효능 자료는 멀꿀(S. hexaphylla)로 학명이 밝혀진 논문만 썼고, 으름덩굴 자료는 섞지 않았다[1][2].\n\n"
     "멀꿀속 식물에서는 오각 트리테르페노이드와 그 배당체, 페닐프로파노이드, 플라보노이드 등 267개 화합물이 보고되었고, 열매는 먹을 수 있고 씨앗은 기름을 짜는 데 쓸 수 있다고 정리되었다[24]. 중국 남부 고유종인 Stauntonia chinensis 는 2025년판 중국약전의 유일한 공식 기원종으로 소개되므로, 중국 약재 이름으로 유통되는 원료가 멀꿀과 같은 종이라고 단정하지 않는 것이 좋다[26][3]. Stauntonia leucantha 열매에서는 아라비노갈락탄 다당류가 분리되었으나, 이는 다른 종의 결과이다[27].\n\n"
     "멀꿀 열매를 정금나무(Vaccinium bracteatum) 열매나 산수유(Cornus officinalis)와 섞은 복합 추출물 연구도 있으며, 이 결과를 멀꿀 열매 단독의 효과로 읽어서는 안 된다[16][17][18]."},
    {"key": "cultivation", "title": "재배와 생산", "body":
     "국내에서 멀꿀은 전라남도 장흥에서 집약적으로 재배된다고 보고되었다[7]. 연구용 열매는 장흥의 GAP(우수농산물관리) 재배 농가와 장흥군 영농조합에서 수확한 것이었다[4][3]. 2018년 연구에서도 열매를 전남 장흥의 재배지에서 채취했다[2].\n\n"
     "일본에서는 멀꿀이 으름덩굴·삼엽으름덩굴·다래 등과 함께 최근 소규모 재배에 들어간 토착 과수로 분류되었고, 이들 토착 과수 유전자원의 현지 내·외 보전은 불안정하다고 평가되었다[8]. 수확 시기는 국내 연구에서 11월 하순~12월 초순이었다[4].\n\n"
     "통계청·농림축산식품부 생산 통계와 로컬 특용작물 통계에서 멀꿀 품목을 확인하지 못해 재배 면적·생산량은 확인하지 못함. 지리적 표시 등록 자료에서도 멀꿀 항목은 확인하지 못함."},
    {"key": "processing", "title": "가공과 제품", "body":
     "연구에서 열매는 1~2 cm 두께로 썰어 45~50 °C에서 24시간 말린 뒤, 정제수로 90 ± 3 °C에서 6시간씩 두 번 추출해 농축하는 방식으로 가공되었다[3][4]. 다른 연구는 열매 10 kg을 10배 부피의 증류수로 100 °C에서 3시간씩 세 번 추출한 뒤 감압 농축·동결건조했다[2].\n\n"
     "말린 열매를 110~114 °C, 70~80 kPa에서 2시간 찌는 증숙을 거듭하면 열매와 추출물이 짙은 갈색으로 변했고, 고형분 수율은 무처리 440 mg/g에서 2회 증숙 506 mg/g으로 늘었다가 3회 증숙에서 415 mg/g으로 줄었다[3]. 총페놀은 1회 증숙에서 61%, 총플라보노이드는 1~2회 증숙에서 7배 이상 늘었고, 클로로젠산류는 2회 증숙까지 변하지 않다가 3회째에 크게 줄었다[3]. 가열 갈변 지표로 쓰이는 5-하이드록시메틸푸르푸랄(5-HMF)은 무처리 열매 217 µg/g에서 1회 증숙 약 2배, 2회 증숙 약 4배로 늘었다[3].\n\n"
     "식약처 「식품 등의 생산실적」 품목 자료에서 멀꿀 원료 제품의 생산실적은 확인하지 못함. 열매·잎 혼합 추출물을 건강 보조 소재로 제안한 연구가 있으나 세포 실험 단계이다[4]."},
    {"key": "genetics", "title": "유전체와 계통", "body":
     "전남 장흥 안양면에서 채집한 멀꿀 잎으로 엽록체 유전체 전체가 해독되었으며, 크기는 158,390 bp이다[7]. 큰 단일복사 영역(LSC) 87,115 bp, 작은 단일복사 영역(SSC) 18,927 bp(초록에는 18,928 bp), 역반복 영역(IR) 26,174 bp 한 쌍으로 이루어지고, 전체 GC 함량은 37.8%이다[7]. 유전자는 모두 117개로 적혀 있으며, 단백질 암호 79개·tRNA 38개·rRNA 8개라는 세부 숫자는 원문 그대로 옮긴 것으로 합계가 117과 맞지 않는다[7].\n\n"
     "으름덩굴과 10개 엽록체 유전체로 만든 최대우도 계통수에서 멀꿀은 같은 과의 한 아종과 가장 가깝게 묶였고, 기존 DNA 계통 연구와 일치했다[7]. 그 아종의 학명은 받은 전문에서 이탤릭 표기가 빠져 확인하지 못함. 중국의 Stauntonia chinensis 엽록체 유전체 비교 연구는 으름덩굴아과(Lardizabaloideae) 8종의 엽록체 유전체가 대체로 보존적이지만 변이가 큰 구간이 있어 DNA 바코드·종 판별에 쓸 수 있다고 보았다[25].\n\n"
     "멀꿀 캘러스(배양 조직)에서는 새로운 30-노르트리테르페노이드 사포닌(무베노사이드 A)이 분리되어, 조직 배양으로도 사포닌이 만들어짐이 보고되었다[23]."},
    {"key": "safety", "title": "안전성과 주의", "body":
     "멀꿀 열매는 식약처 「식품원료 목록」에서 열매에 한해 사용가능한 식품원료이며, 잎·줄기·뿌리는 이 목록에서 확인하지 못했다[1]. 따라서 잎 추출물 연구(항염증, 골 대사, 당뇨 합병증 관련 효소 억제 등)의 결과와 안전성 자료를 열매 식품에 그대로 적용해서는 안 된다[9][12][13][14].\n\n"
     "열매 열수 추출물은 RAW 264.7 세포에서 50~200 µg/mL 범위에서 세포 생존율을 바꾸지 않았고, 쥐에 50~200 mg/kg을 3일간 투여한 부종 시험(투여 경로는 원문에 명시 없음)에서 별도의 독성 평가는 확인하지 못했다[2]. 증숙 열매 추출물은 RAW 264.7 세포에서 48시간 처리 시 125 µg/mL를 넘으면 생존율이 유의하게 떨어졌다[3]. 증숙으로 늘어나는 5-HMF는 생체에서 이로운 작용과 해로운 작용을 함께 보일 수 있는 물질로 소개되었다[3].\n\n"
     "효능 자료는 모두 세포·동물 실험이며, 열매 단독 섭취에 대한 사람 임상시험은 확인하지 못했다. 열매와 정금나무 열매 1:1 복합 추출물의 항피로·갱년기 동물 연구는 복합물 결과이다[16][17]. 공공기관의 알레르기·잔류 농약·독성 성분 정보는 확인하지 못함."},
]

compounds = [
    {"name": "Chlorogenic acid", "name_ko": "클로로젠산", "class": "페놀산(카페오일퀸산)", "role": "marker", "part": "열매",
     "content_text": "열매 열수 추출물 약 9.4 mg/g(추출물 기준, HPLC)[2]; 무증숙 열매 100 µg/g(건조 과실·추출물 중 어느 기준인지 원문에 명시 없음)[3]; 네오·크립토 이성질체를 합한 클로로젠산류 열매 360 ± 12 µg/g, 잎 2395 ± 20 µg/g[4]",
     "activity_ko": "클로로젠산류가 멀꿀의 지표로 쓰인다고 기술[4]; 열매 추출물 항염 작용의 후보 성분으로 제시(세포·동물)[2]; 단일 성분으로 ALP 활성·유전자 발현을 높임(세포)[4]",
     "source": [2, 3, 4]},
    {"name": "Neochlorogenic acid", "name_ko": "네오클로로젠산", "class": "페놀산(카페오일퀸산)", "role": "marker", "part": "열매",
     "content_text": "열매 열수 추출물 약 5.8 mg/g(추출물 기준)[2]; 무증숙 열매 120 µg/g(기준 원문에 명시 없음)[3]",
     "activity_ko": "열매 추출물 표준화 기준 성분 중 하나[2]; 단일 성분으로 ALP 활성을 높임(세포)[4]",
     "source": [2, 3, 4]},
    {"name": "Cryptochlorogenic acid", "name_ko": "크립토클로로젠산", "class": "페놀산(카페오일퀸산)", "role": "marker", "part": "열매",
     "content_text": "열매 열수 추출물 약 8.1 mg/g(추출물 기준)[2]; 무증숙 열매 108 µg/g(기준 원문에 명시 없음), 2회 증숙까지 비율 변화 없음[3]",
     "activity_ko": "열매 추출물 표준화 기준 성분 중 하나[2]; ALP 증가 효과는 네오클로로젠산·클로로젠산보다 약함(세포)[4]",
     "source": [2, 3, 4]},
    {"name": "5-Hydroxymethylfurfural", "name_ko": "5-하이드록시메틸푸르푸랄(5-HMF)", "class": "푸란 알데하이드(가열 갈변 산물)", "role": "bioactive", "part": "열매(증숙 열매)",
     "content_text": "무증숙 열매 217 µg/g, 1회 증숙 약 2배, 2회 증숙 약 4배, 3회 증숙은 무증숙 수준으로 감소[3]; 열매에서만 검출되고 잎에서는 불검출[4]",
     "activity_ko": "10 µg/mL에서 ALP 활성 21% 증가, TRAP 활성 억제(세포)[3]",
     "source": [3, 4]},
    {"name": "Hexaphyloside A", "name_ko": "헥사필로사이드 A·B", "class": "트리테르펜 사포닌", "role": "bioactive", "part": "열매",
     "content_text": "열매 에탄올 추출물에서 분리한 26개 화합물 중 새 화합물 2종(함량 미보고)[5]",
     "activity_ko": "같은 연구의 분리 화합물 6·10이 LPS 자극 RAW264.7 세포 NO 생성 억제 IC50 1.33·1.10 µM(세포; 두 화합물의 이름은 초록에서 확인하지 못함)[5]",
     "source": [5]},
    {"name": "Staunoside A", "name_ko": "스타우노사이드 A·B(헤데라게닌 배당체)", "class": "트리테르페노이드 배당체(3,28-이중 배당체)", "role": "bioactive", "part": "부위 표기 확인하지 못함",
     "content_text": "새 화합물로 분리(함량 미보고); A는 3-O-글루코실 헤데라게닌 28-O-글루코실(1→6)글루코실 에스터[21]",
     "activity_ko": "확인하지 못함", "source": [21]},
    {"name": "Staunoside D", "name_ko": "스타우노사이드 D·E", "class": "트리테르페노이드 배당체", "role": "bioactive", "part": "부위 표기 확인하지 못함",
     "content_text": "새 이중 배당체 2종 분리(함량 미보고), 알려진 배당체 3종과 함께 보고[22]",
     "activity_ko": "확인하지 못함", "source": [22]},
    {"name": "Hederagenin", "name_ko": "헤데라게닌", "class": "트리테르펜(올레아난형 사포게닌)", "role": "bioactive", "part": "부위 표기 확인하지 못함",
     "content_text": "스타우노사이드 A·D 등 배당체의 아글리콘(유리형 함량 미보고)[21][22]",
     "activity_ko": "확인하지 못함", "source": [21, 22]},
    {"name": "Oleanolic acid", "name_ko": "올레아놀산", "class": "트리테르펜(올레아난형 사포게닌)", "role": "bioactive", "part": "잎(식품 사용 부위 아님)",
     "content_text": "잎에서 분리한 올레아놀산 배당체 사포닌 2종의 아글리콘(함량 미보고)[10]",
     "activity_ko": "먹였을 때 배당체 사포닌이 아글리콘보다 생체 내 항염 효과가 훨씬 컸고, 세포에서는 비슷함(동물·세포)[10]",
     "source": [10]},
    {"name": "Stauntonoside A", "name_ko": "스타운토노사이드 A·B", "class": "트리테르펜 사포닌", "role": "bioactive", "part": "잎(식품 사용 부위 아님)",
     "content_text": "잎 에탄올 추출물에서 분리한 사포닌 23종 중 새 화합물 2종(함량 미보고)[9]",
     "activity_ko": "같은 연구의 화합물 13이 NO 생성 억제 IC50 0.59 µM(세포; 화합물 이름은 초록에서 확인하지 못함)[9]",
     "source": [9]},
    {"name": "Rutin", "name_ko": "루틴", "class": "플라보노이드(플라보놀 배당체)", "role": "bioactive", "part": "잎(당년생 어린 줄기 포함, 식품 사용 부위 아님)",
     "content_text": "잎에서 검출, 열매에서는 검출되지 않음(정성 비교)[4]",
     "activity_ko": "단일 성분으로 ALP 활성·유전자 발현을 높임(세포)[4]", "source": [4]},
    {"name": "Luteolin 7-O-glucoside", "name_ko": "루테올린-7-O-글루코사이드", "class": "플라보노이드(플라본 배당체)", "role": "bioactive", "part": "잎(식품 사용 부위 아님)",
     "content_text": "잎에서 검출, 열매에서는 검출되지 않음[4]; 잎 아세트산에틸 분획에서 분리[12]",
     "activity_ko": "쥐 수정체 알도스 환원효소 억제(IC50 7.34–23.99 µM 범위의 5성분 중 하나, 시험관)[12]", "source": [4, 12]},
    {"name": "Calceolarioside B", "name_ko": "칼세올라리오사이드 B", "class": "페닐에타노이드 배당체", "role": "bioactive", "part": "잎(식품 사용 부위 아님)",
     "content_text": "잎 아세트산에틸 분획에서 분리한 7개 화합물 중 하나(함량 미보고)[12]",
     "activity_ko": "쥐 수정체 알도스 환원효소 억제(IC50 7.34–23.99 µM 범위의 5성분 중 하나, 시험관)[12]", "source": [12]},
    {"name": "Mubenoside A", "name_ko": "무베노사이드 A", "class": "30-노르트리테르페노이드 사포닌", "role": "bioactive", "part": "캘러스(배양 조직, 식품 사용 부위 아님)",
     "content_text": "캘러스 조직에서 새 화합물로 분리(함량 미보고)[23]",
     "activity_ko": "확인하지 못함", "source": [23]},
]

assays = [
    {"role": "literature", "compound": "Chlorogenic acid", "compound_ko": "클로로젠산(네오·크립토 이성질체와 동시 정량)", "part": "열매(전남 장흥 재배지)",
     "content": "열매 열수 추출물 1 g 당 네오클로로젠산 약 5.8 mg, 클로로젠산 약 9.4 mg, 크립토클로로젠산 약 8.1 mg[2]",
     "method": "HPLC-PDA",
     "conditions": {
         "instrument": "Waters HPLC(1525 이원 펌프, 2998 PDA 검출기, 2707 자동주입기)",
         "column": "Sunfire C18(250 mm × 4.6 mm, 5 µm, Waters)",
         "mobile_phase": "A 메탄올, B 0.1% 포름산 함유 물",
         "gradient": "0–15분 25% A; 15–25분 25–40% A; 25–35분 40% A; 35–45분 40–50% A; 45–55분 50–60% A; 55–68분 60–100% A; 68–76분 100% A; 76–81분 100–25% A; 81–85분 25% A",
         "flow": "1 mL/min", "temp": "35 °C", "detection": "254·320 nm", "injection": "10 µL",
         "sample_prep": "열매 10 kg 을 10배 부피 증류수로 100 °C 3시간 3회 추출, 여액 합쳐 40 °C 감압 농축 후 −50 °C 동결건조",
         "standard": "네오클로로젠산·클로로젠산·크립토클로로젠산(Sigma-Aldrich)",
         "linearity": "", "lod": "", "loq": "", "recovery": ""},
     "rationale": "열매 추출물을 이 세 이성질체로 표준화했고 항염 활성 후보 성분으로 제시했다[2]. PMC 전문 Methods 확인, 검량선·검출한계·회수율은 원문에 없음.",
     "source": [2], "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5793338/", "source_kind": "paper"},
    {"role": "literature", "compound": "Chlorogenic acid", "compound_ko": "클로로젠산류(네오·크립토 포함 합계)", "part": "열매(완숙과, 45~50 °C 건조) 및 잎 비교",
     "content": "열매 360 ± 12 µg/g, 잎 2395 ± 20 µg/g[4]",
     "method": "HPLC-UV(가변파장 검출기)",
     "conditions": {
         "instrument": "Agilent 1260 Infinity(G1311B 사원 펌프, G1329B 자동주입기, G1316A 칼럼 항온기, G1314F 가변파장 검출기)",
         "column": "ZORBAX Eclipse Plus C18(원문 표기 4.6 mm × 10 mm, 5 µm)",
         "mobile_phase": "A 0.4% 인산, B 아세토나이트릴",
         "gradient": "0–10분 5–9% B; 10–30분 9% B; 30–60분 9–30% B; 60–62분 30–50% B",
         "flow": "1 mL/min", "temp": "35 °C", "detection": "260 nm", "injection": "5 µL",
         "sample_prep": "건조 열매를 10배 부피 정제수로 90 ± 3 °C 6시간 2회 추출, 여과 후 30 brix 로 농축",
         "standard": "클로로젠산·네오클로로젠산·크립토클로로젠산·루틴·루테올린-7-O-글루코사이드 등(Sigma-Aldrich), 5-HMF(Wuhan ChemFaces)",
         "linearity": "", "lod": "", "loq": "", "recovery": ""},
     "rationale": "논문은 클로로젠산류를 멀꿀의 지표로 쓴다고 적었고, 열매와 잎의 함량 차이를 보였다[4]. PMC 전문 Methods 확인, 검증 값은 원문에 없음.",
     "source": [4], "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12190245/", "source_kind": "paper"},
    {"role": "literature", "compound": "5-Hydroxymethylfurfural", "compound_ko": "5-하이드록시메틸푸르푸랄(5-HMF)", "part": "열매(증숙·무증숙)",
     "content": "무증숙 열매 217 µg/g, 1회 증숙 약 2배, 2회 증숙 약 4배[3]",
     "method": "HPLC-UV(가변파장 검출기)",
     "conditions": {
         "instrument": "Agilent 1260 Infinity(G1311B 사원 펌프, G1329B 자동주입기, G1316A 칼럼 항온기, G1314F 가변파장 검출기)",
         "column": "ZORBAX Eclipse Plus C18(원문 표기 4.6 mm × 10 mm, 5 µm)",
         "mobile_phase": "A 0.4% 인산, B 아세토나이트릴",
         "gradient": "0–10분 5–9% B; 10–30분 9% B; 30–60분 9–30% B; 60–62분 30–50% B",
         "flow": "1 mL/min", "temp": "35 °C", "detection": "260 nm", "injection": "5 µL",
         "sample_prep": "45~50 °C 24시간 건조(필요 시 110~114 °C 2시간 증숙) 열매를 1:10 정제수로 90 ± 3 °C 6시간 2회 추출, 감압 건조 후 시료 1 g 당 1 mL 로 재용해, 5배 희석",
         "standard": "5-HMF·클로로젠산류 표준품(순도 98% 초과, Sigma-Aldrich·Wuhan ChemFaces)",
         "linearity": "", "lod": "", "loq": "", "recovery": ""},
     "rationale": "증숙으로 크게 늘어나는 가공 지표 성분으로, 분취 HPLC·NMR 로 확인했다[3]. PMC 전문 Methods 확인, 검증 값은 원문에 없음.",
     "source": [3], "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12428769/", "source_kind": "paper"},
]

# 사용 출처 보강: 6,11,15,19,20 등은 본문에서 쓴다
sections[7]["body"] += ("\n\n추가로, 열매가 아닌 추출물(부위가 초록에 명시되지 않음)로 한 전립선비대 쥐 실험과 탈모 생쥐 실험이 있으나 모두 동물·세포 단계이다[19][20]. "
                        "잎 에탄올 추출물과 그 분리 성분은 세포에서 COX-2·iNOS 발현을 줄였다는 보고가 있지만 이 역시 잎 결과이다[11].")
sections[2]["body"] += " 2026년 총설은 항염·골다공증 억제 등의 활성을 정리했으나 대부분 잎·전초 연구에 바탕을 둔다[6]."

d = {
    "slug": "stauntonia-hexaphylla", "name_ko": "멀꿀", "name_en": "Japanese staunton vine",
    "scientific_name": "Stauntonia hexaphylla (Thunb.) Decne.",
    "aliases": ["멀꿀열매", "야모과", "Stauntonia vine", "Japanese staunton vine", "Rajania hexaphylla Thunb.", "Mube(일본)", "Ye-mu-gua(중국)"],
    "sections": sections, "compounds": compounds, "markers": [], "nutrients": [], "assays": assays,
    "production": [], "world": [], "gi": [], "orgs": [], "sources": S,
}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in sections:
    print(s["key"], len(s["body"]))
