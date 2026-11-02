import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
PM = "https://pubmed.ncbi.nlm.nih.gov/{}/"
AC = "2026-11-02"
I1020 = "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020"
# key -> (title, url, publisher, accessed)
S = [
 ("mfds", "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 싸리나무(Lespedeza bicolor Turcz.): 싸리나무순·싸리나무잎·싸리나무추출액, 사용가능부위 : 순, 잎 (로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json)", I1020, "식품의약품안전처", "2026-10-13"),
 ("mfds2", "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 같은 속·비슷한 이름 행 대조: 비수리(Lespedeza cuneata G. Don, 사용가능부위 : 줄기, 잎), 비수리추출분말(건강기능식품 C코드 개별인정), 참싸리(Lespedeza cyrtobotrya Miq., 사용불가), 광대싸리(Securinega suffruticosa), 댑싸리(Kochia scoparia, 사용불가), 싸리버섯(Ramaria botrytis) (로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json)", I1020, "식품의약품안전처", "2026-10-13"),
 ("31370192", "Therapeutic Potential of Lespedeza bicolor to Prevent Methylglyoxal-Induced Glucotoxicity in Familiar Diabetic Nephropathy. J Clin Med. 2019;8(8):1138. doi:10.3390/jcm8081138 (PMC6723630 전문 확인)", PM.format("31370192"), "Journal of Clinical Medicine (PubMed)", AC),
 ("31795363", "Effects of Lespedeza bicolor Extract on Regulation of AMPK Associated Hepatic Lipid Metabolism in Type 2 Diabetic Mice. Antioxidants (Basel). 2019;8(12):599. doi:10.3390/antiox8120599 (PMC6943630 전문 확인)", PM.format("31795363"), "Antioxidants (PubMed)", AC),
 ("32050658", "Lespedeza bicolor Extract Ameliorated Renal Inflammation by Regulation of NLRP3 Inflammasome-Associated Hyperinflammation in Type 2 Diabetic Mice. Antioxidants (Basel). 2020;9(2):148. doi:10.3390/antiox9020148", PM.format("32050658"), "Antioxidants (PubMed)", AC),
 ("36638746", "Lespedeza bicolor extract supplementation reduced hyperglycemia-induced skeletal muscle damage by regulation of AMPK/SIRT/PGC1α-related energy metabolism in type 2 diabetic mice. Nutr Res. 2023;110:1-13. doi:10.1016/j.nutres.2022.12.007", PM.format("36638746"), "Nutrition Research (PubMed)", AC),
 ("29157823", "Lespedeza bicolor ameliorates endothelial dysfunction induced by methylglyoxal glucotoxicity. Phytomedicine. 2017;36:26-36. doi:10.1016/j.phymed.2017.09.005", PM.format("29157823"), "Phytomedicine (PubMed)", AC),
 ("36076382", "Kaempferol-3-O-galactoside as a marker for authenticating Lespedeza bicolor Turcz. monofloral honey. Food Res Int. 2022;160:111667. doi:10.1016/j.foodres.2022.111667 (초록만 확인)", PM.format("36076382"), "Food Research International (PubMed)", AC),
 ("37891888", "Antioxidant Polyphenols from Lespedeza bicolor Turcz. Honey: Anti-Inflammatory Effects on Lipopolysaccharide-Treated RAW 264.7 Macrophages. Antioxidants (Basel). 2023;12(10):1809. doi:10.3390/antiox12101809 (PMC10604429 전문 확인)", PM.format("37891888"), "Antioxidants (PubMed)", AC),
 ("39199146", "Lespedeza bicolor Turcz. Honey Prevents Inflammation Response and Inhibits Ferroptosis in DSS-Induced Human Caco-2 Cells. Antioxidants (Basel). 2024;13(8):900. doi:10.3390/antiox13080900", PM.format("39199146"), "Antioxidants (PubMed)", AC),
 ("26858533", "A potential anti-inflammation activity and depigmentation effect of Lespedeza bicolor extract and its fractions. Saudi J Biol Sci. 2016;23(1):9-14. doi:10.1016/j.sjbs.2015.01.016 (PMC4705262 전문 확인)", PM.format("26858533"), "Saudi Journal of Biological Sciences (PubMed)", AC),
 ("14693230", "New prenylated isoflavanones and other constituents of Lespedeza bicolor. Fitoterapia. 2004;75(1):95-7. doi:10.1016/j.fitote.2003.07.012", PM.format("14693230"), "Fitoterapia (PubMed)", AC),
 ("31004693", "Cytotoxic polyphenolic compounds from Lespedeza bicolor stem bark. Fitoterapia. 2019;135:64-72. doi:10.1016/j.fitote.2019.04.003", PM.format("31004693"), "Fitoterapia (PubMed)", AC),
 ("21911291", "Potent inhibition of bacterial neuraminidase activity by pterocarpans isolated from the roots of Lespedeza bicolor. Bioorg Med Chem Lett. 2011;21(20):6100-3. doi:10.1016/j.bmcl.2011.08.046", PM.format("21911291"), "Bioorganic & Medicinal Chemistry Letters (PubMed)", AC),
 ("31675225", "Antiproliferative Pterocarpans and Coumestans from Lespedeza bicolor. J Nat Prod. 2019;82(11):3025-3032. doi:10.1021/acs.jnatprod.9b00567", PM.format("31675225"), "Journal of Natural Products (PubMed)", AC),
 ("34990769", "Biologically active polyphenolic compounds from Lespedeza bicolor. Fitoterapia. 2022;157:105121. doi:10.1016/j.fitote.2021.105121", PM.format("34990769"), "Fitoterapia (PubMed)", AC),
 ("35453394", "Polyphenolic Compounds from Lespedeza bicolor Protect Neuronal Cells from Oxidative Stress. Antioxidants (Basel). 2022;11(4):709. doi:10.3390/antiox11040709", PM.format("35453394"), "Antioxidants (PubMed)", AC),
 ("32183314", "Polyphenolic Compounds from Lespedeza Bicolor Root Bark Inhibit Progression of Human Prostate Cancer Cells via Induction of Apoptosis and Cell Cycle Arrest. Biomolecules. 2020;10(3):451. doi:10.3390/biom10030451", PM.format("32183314"), "Biomolecules (PubMed)", AC),
 ("31618776", "Lespedeza bicolor Extract Improves Amyloid Beta25-35-Induced Memory Impairments by Upregulating BDNF and Activating Akt, ERK, and CREB Signaling in Mice. Planta Med. 2019;85(17):1363-1373. doi:10.1055/a-1018-5402", PM.format("31618776"), "Planta Medica (PubMed)", AC),
 ("15744086", "Evaluation of the estrogenic activity of Leguminosae plants. Biol Pharm Bull. 2005;28(3):538-40. doi:10.1248/bpb.28.538", PM.format("15744086"), "Biological & Pharmaceutical Bulletin (PubMed)", AC),
 ("2461730", "Effects of condensed tannins prepared from leaves of fodder plants on digestive enzymes in vitro and in the intestine of rats. Br J Nutr. 1988;60(2):275-85. doi:10.1079/bjn19880099", PM.format("2461730"), "British Journal of Nutrition (PubMed)", AC),
 ("18757448", "Phosphorus enhances Al resistance in Al-resistant Lespedeza bicolor but not in Al-sensitive L. cuneata under relatively high Al stress. Ann Bot. 2008;102(5):795-804. doi:10.1093/aob/mcn166", PM.format("18757448"), "Annals of Botany (PubMed)", AC),
 ("22847333", "LC-MS-based chemotaxonomic classification of wild-type Lespedeza sp. and its correlation with genotype. Plant Cell Rep. 2012;31(11):2085-97. doi:10.1007/s00299-012-1319-8", PM.format("22847333"), "Plant Cell Reports (PubMed)", AC),
 ("28051161", "ITS non-concerted evolution and rampant hybridization in the legume genus Lespedeza (Fabaceae). Sci Rep. 2017;7:40057. doi:10.1038/srep40057", PM.format("28051161"), "Scientific Reports (PubMed)", AC),
 ("35665174", "Complete Chloroplast Genomes Provide Insights Into Evolution and Phylogeny of Campylotropis (Fabaceae). Front Plant Sci. 2022;13:895543. doi:10.3389/fpls.2022.895543", PM.format("35665174"), "Frontiers in Plant Science (PubMed)", AC),
 ("40858786", "Morphological and biomechanical responses of Lespedeza bicolor Turcz. roots to long-term phosphorus addition at high altitudes. Sci Rep. 2025;15(1):31484. doi:10.1038/s41598-025-16807-7", PM.format("40858786"), "Scientific Reports (PubMed)", AC),
 ("37852480", "The effect of mixed forest identity on soil carbon stocks in Pinus massoniana mixed forests. Sci Total Environ. 2023;907:167889. doi:10.1016/j.scitotenv.2023.167889", PM.format("37852480"), "Science of the Total Environment (PubMed)", AC),
 ("40953051", "Mycelial traits and GRSP in enhancing soil stability on cold region highway slopes: Comparative effects of three shrub species. PLoS One. 2025;20(9):e0332483. doi:10.1371/journal.pone.0332483", PM.format("40953051"), "PLoS One (PubMed)", AC),
 ("39683112", "Flavonoids Derived from the Roots of Lespedeza bicolor Inhibit the Activity of SARS-CoV Papain-like Protease. Plants (Basel). 2024;13(23):3319. doi:10.3390/plants13233319", PM.format("39683112"), "Plants (PubMed)", AC),
 ("39417178", "Lespedeza bicolor root extract exerts anti-TNBC potential by regulating FAK-related signalling pathways. Am J Cancer Res. 2024;14(9):4265-4285. doi:10.62347/MYPG4066", PM.format("39417178"), "American Journal of Cancer Research (PubMed)", AC),
 ("37782374", "2-Geranyl-1-methoxyerythrabyssin II alleviates lipid accumulation and inflammation in hepatocytes through AMPK activation and AKT inhibition. Arch Pharm Res. 2023;46(9-10):808-824. doi:10.1007/s12272-023-01464-z", PM.format("37782374"), "Archives of Pharmacal Research (PubMed)", AC),
 ("32188202", "Methanolic extract from Lespedeza bicolor: potential candidates for natural antioxidant and anticancer agent. J Tradit Chin Med. 2017;37(4):444-451", PM.format("32188202"), "Journal of Traditional Chinese Medicine (PubMed)", AC),
 ("5974229", "[Substances contained in Lespedeza bicolor var. japonica, II]. Justus Liebigs Ann Chem. 1966;692:194-9. doi:10.1002/jlac.19666920122 (초록 없음, 서지만 확인)", PM.format("5974229"), "Justus Liebigs Annalen der Chemie (PubMed)", AC),
]
N = {k: i + 1 for i, (k, *_) in enumerate(S)}
def r(*ks): return "[" + ", ".join(str(N[k]) for k in ks) + "]"

sections = [
 ("overview", "한눈에 보기", f"""싸리(싸리나무, Lespedeza bicolor Turcz.)는 콩과(Fabaceae) 싸리속에 속하는 낙엽 관목으로, 아시아에서 관상용으로 널리 심는다{r('31795363')}. 영어 이름은 shrub lespedeza이며, 논문들은 염증·신장염·당뇨 증상 등에 써 온 전통 약용식물로 소개한다{r('mfds','31370192','29157823')}.

식품의약품안전처 「식품원료 목록」에서 싸리나무는 사용가능 원료이고, 사용 조건은 '사용가능부위 : 순, 잎'이다{r('mfds')}. 목록에는 싸리나무순·싸리나무잎·싸리나무추출액 3개 원료명과 다른 이름 '싸리나무', 영문명 Shrub lespedeza가 올라 있다{r('mfds')}. 같은 속의 비수리(L. cuneata)는 별개 원료로 따로 등재되어 있고 참싸리(L. cyrtobotrya)는 사용불가 원료이므로 서로 구별해야 한다{r('mfds2')}. 건강기능식품 고시형 원료의 원재료 기록은 확인하지 못함.

성분 연구는 주로 줄기·뿌리껍질·꽃과 싸리꿀을 대상으로 했고, 프레닐화 프테로카르판·쿠메스탄 같은 폴리페놀과 루틴·루테올린·다이드제인 같은 플라보노이드가 보고되었다{r('31370192','31004693','31675225')}. 식품으로 쓸 수 있는 순·잎만을 정량한 논문은 확인하지 못함. 뿌리·줄기껍질 폴리페놀은 전립선암 세포 증식 억제, 신경세포 산화 손상 보호, SARS-CoV 파파인 유사 단백분해효소 억제를 세포·효소 시험에서 보였다{r('32183314','35453394','39683112')}. 효능 근거는 세포·동물 시험에 머물러 있고, 사람 대상 시험은 확인하지 못함."""),
 ("history", "역사와 전통적 이용", f"""싸리속 식물은 중국 전통 의학에서 요로의 급성·만성 염증 치료에 쓰였다고 소개된다{r('26858533')}. 싸리속 식물은 신장염, 질소혈증, 염증, 기력 저하, 당뇨, 이뇨에 쓰였다고 하며, 26종을 비교한 연구가 이를 배경으로 들었다{r('29157823')}. 싸리 자체는 독소를 없애고 기력을 보충하며 당뇨 증상을 다스리는 데 썼다고 적혀 있다{r('31370192')}. 다른 논문은 싸리를 호주·북미·동아시아에서 쓰인 전통 약초로 소개하며 염증·신장염·색소침착·이뇨에 쓴다고 했다{r('31618776')}.

싸리꽃은 독소 제거와 기력 보충, 당뇨 증상 조절, 급·만성 신장염과 질소혈증 치료에 쓰였다고 소개된다{r('37891888')}. 중국에서는 싸리꿀이 귀하고 값이 높아 다른 꿀을 섞거나 대신한 위조품이 유통된다고 보고되었다{r('36076382')}. 1966년에는 일본 변종(L. bicolor var. japonica)의 함유 성분 연구가 독일 화학 학술지에 실렸다{r('5974229')}. 한국에서 순을 나물로 먹은 기록 등 식용 역사를 다룬 공공기관 자료는 확인하지 못함."""),
 ("biology", "식물학적 특징", f"""싸리는 콩과의 다년생 낙엽 관목이다{r('31795363')}. 척박한 산성 토양에서도 잘 자라는 콩과 사료 식물로 소개된다{r('18757448')}. 30일 수경 재배 실험에서 싸리는 같은 속 비수리보다 알루미늄 독성에 강했고, 인(P)을 주면 뿌리 끝의 알루미늄 축적이 줄어 저항성이 더 높아졌다{r('18757448')}. 고산 지대에서 7년 동안 인을 다섯 수준으로 준 시험에서는 연간 2 g/m² 수준에서 뿌리 생물량·길이·개수가 가장 컸다{r('40858786')}. 같은 시험에서 뿌리 인장강도는 셀룰로스 함량과 비례하고 리그닌 함량과 반비례했다{r('40858786')}.

잎에는 응축 탄닌이 많아, 사료식물 19종을 조사한 연구에서 탄닌이 많은 6종 가운데 하나였다{r('2461730')}. 꽃에서는 퀘르세틴·캠페롤의 3-O-루티노사이드와 3-O-글루코사이드가 분리되었다{r('34990769')}. 꽃은 꿀벌의 밀원이 되며, 중국 다싱안링 지역 싸리 재배지 양봉장의 꿀은 싸리 꽃가루가 약 70%로 단화밀 기준(45% 이상)을 넘었다{r('37891888')}. 꽃 색·키·개화기 같은 형태 기재는 공공 식물지 자료를 확인하지 못함."""),
 ("related_species", "가까운 종과 혼동 주의", f"""식품원료 목록에서 같은 속 비수리(L. cuneata)는 '사용가능부위 : 줄기, 잎'인 별개 원료이고, 비수리추출분말은 건강기능식품 개별인정형 원료(C코드)로 따로 올라 있다{r('mfds2')}. 따라서 비수리의 성분·기능성 자료를 싸리에 옮겨 쓰면 안 된다{r('mfds','mfds2')}. 참싸리(L. cyrtobotrya)는 목록에서 사용불가 원료이다{r('mfds2')}.

한국 야생 싸리속 4종(참싸리·싸리·L. maximowiczii·비수리) 39개 시료를 분석한 연구에서 참싸리와 싸리는 유전형으로는 한 가지에 섞일 만큼 가까웠다{r('22847333')}. 그러나 잎의 LC-MS 대사체 분석으로는 두 종을 구분할 수 있었고, 비수리는 나머지 세 종과 가장 멀었다{r('22847333')}. 싸리속 26종의 메틸글리옥살 독성 보호 효과를 비교한 연구에서는 싸리 시료가 가장 강했다{r('29157823')}.

이름에 '싸리'가 들어가도 광대싸리(Securinega suffruticosa)·댑싸리(Kochia scoparia)·싸리버섯(Ramaria botrytis)은 싸리속이 아닌 다른 생물이며, 식품원료 목록에서도 따로 관리된다{r('mfds2')}. 댑싸리는 목록에서 사용불가 원료이다{r('mfds2')}."""),
 ("cultivation", "재배와 생산", f"""싸리는 척박한 산성 토양에 잘 견디는 콩과 관목이라 사료·토양 보전용으로 소개된다{r('18757448')}. 중국 동북부 추운 지역의 고속도로 비탈면(30°·60°)에서 녹화용 관목 3종을 비교한 연구에 싸리가 포함되었으며, 토양 입단 안정성은 족제비싸리(Amorpha fruticosa)가 더 높았다{r('40953051')}. 마송소나무(Pinus massoniana) 혼효림 1,010쌍을 분석한 메타분석에서는 싸리와 섞어 심은 숲이 토양 깊이 전체에서 유기탄소 저장량을 크게 늘렸다{r('37852480')}. 고산 공사 교란지 시험에서는 인 공급 수준이 연간 2 g/m²일 때 싸리의 생장과 침식 저감 잠재력이 가장 좋았다{r('40858786')}.

꿀 생산지로는 중국 다싱안링 지역의 싸리 재배지 양봉장이 보고되었다{r('37891888')}. 싸리꿀의 지표 성분 연구에서는 중국에서 흔히 파는 싸리꿀·순비기나무꿀·아카시아꿀·대추꿀·피나무꿀을 비교했다{r('36076382')}. 국내 재배 면적·생산량(통계청 농작물생산조사, 농식품부 특용작물 생산실적)에서 싸리 항목은 확인하지 못함. 지리적 표시 등록이나 생산자 단체도 확인하지 못함."""),
 ("processing", "가공과 이용", f"""식품원료 목록의 원료명은 싸리나무순·싸리나무잎·싸리나무추출액이며, 세 행 모두 사용 조건이 '사용가능부위 : 순, 잎'이다{r('mfds')}. 추출액도 순과 잎으로 만든 것만 해당하는 것으로 읽힌다{r('mfds')}. 건강기능식품 생산실적에서 싸리나무 원료 품목은 확인하지 못함.

연구용 추출물은 지상부 또는 줄기를 70% 에탄올로 실온에서 하룻밤 추출한 뒤 여과·감압농축·동결건조해 만들었다{r('31370192','31795363')}. 이 추출물은 당뇨 생쥐 시험에서 물에 녹여 체중 1 kg당 100 mg과 250 mg을 12주 동안 먹였다{r('31795363','32050658','36638746')}. 말린 줄기 200 g을 70% 메탄올로 추출해 클로로포름·에틸아세테이트·부탄올·물 분획으로 나눈 연구에서는 에틸아세테이트 분획에서 비텍신과 하기닌 A·B·C가 동정되었다{r('26858533')}. 이 분획은 버섯 티로시네이스를 경쟁적으로 억제해 피부 미백 소재 가능성이 제시되었다{r('26858533')}. 파키스탄에서 채집한 지상부·뿌리 메탄올 추출물은 폐암 세포(LU-1)에 IC50 12.5·50 μg/mL를 보였다{r('32188202')}.

싸리꿀은 꿀 5 g을 물에 녹여 원심분리한 뒤 고체상 추출(SPE)로 폴리페놀을 모아 분석했다{r('37891888')}. 싸리꿀 추출물과 그 지표 성분 트리폴린은 장 세포 염증 모델에서 철 의존성 세포사(페롭토시스)를 억제했다{r('39199146')}."""),
 ("genetics", "유전체와 종 판별", f"""싸리속은 한 개체 안에서도 ITS 사본이 크게 다르고, 위유전자·재조합체가 섞여 있어 잡종화가 흔한 속으로 보고되었다{r('28051161')}. 따라서 ITS 서열 하나로 종을 가리거나 계통을 세울 때는 주의가 필요하다{r('28051161')}. 근연 속 Campylotropis의 엽록체 유전체 21개를 분석한 연구는 싸리속 등 근연 속과의 계통 관계를 함께 다루었다{r('35665174')}.

한국 야생 싸리속 39개 시료를 핵 ITS와 엽록체 trnL-trnF 서열로 분석하자 크게 세 유전형으로 나뉘었고, 참싸리와 싸리 시료는 한 가지에 섞였다{r('22847333')}. 같은 연구에서 잎의 대사체 분류는 줄기보다 유전형 분류와 더 잘 맞았다{r('22847333')}. 이는 싸리와 참싸리처럼 사용 가능 여부가 다른 종을 구별할 때 유전자와 성분 분석을 함께 써야 함을 보여 준다{r('mfds2','22847333')}.

싸리꿀은 꽃가루 형태(화분학) 특징과 캠페롤-3-O-갈락토사이드 지표로 진위를 판별하는 방법이 제안되었다{r('36076382')}. 싸리의 핵 유전체 해독이나 엽록체 유전체 단독 보고는 확인하지 못함."""),
 ("safety", "안전성과 주의", f"""식품원료 목록상 싸리나무는 순과 잎만 식품에 쓸 수 있고, 연구에 많이 쓰인 뿌리·뿌리껍질·줄기껍질은 사용가능부위가 아니다{r('mfds')}. 건강기능식품 고시의 섭취 시 주의사항, 알레르기·잔류농약 등 공공기관 안전 정보는 확인하지 못함. 사람 대상 독성·임상 시험도 확인하지 못함.

동물 시험에서 지상부 70% 에탄올 추출물을 당뇨 생쥐에 100·250 mg/kg/일로 12주 먹였을 때 체중과 사료 섭취량은 바뀌지 않았고, 낮은 용량 군의 간 수치(GOT·GPT)는 당뇨 대조군보다 낮았다{r('31795363')}. 세포 시험에서 줄기 추출물만 처리했을 때 신장 세포 독성은 보이지 않았다{r('31370192')}. 뿌리 추출물은 생쥐 이종이식 시험에서 뚜렷한 부작용 없이 항암 활성을 보였다고 보고되었다{r('39417178')}.

콩과 식물 추출물의 에스트로겐 활성 선별 시험에서 싸리는 EC50 10 μg/mL 미만의 강한 활성을 보인 종에 들었다{r('15744086')}. 이 결과가 사람 섭취에서 어떤 의미인지는 확인하지 못함. 잎에서 얻은 응축 탄닌은 시험관에서 트립신·α-아밀레이스·리파아제 활성을 억제했고, 중합도가 높을수록 단백질 침전력이 컸다{r('2461730')}. 줄기껍질의 일부 프테로카르판은 사람 암세포뿐 아니라 정상 세포주에도 세포독성을 보였다{r('31004693')}."""),
]

compounds = [
 dict(name="Rutin", name_ko="루틴", class_="플라보놀 배당체", role="marker", part="줄기(70% 에탄올 추출물 분말)", content_text="43.69 ± 0.02 µg/10 mg 추출물(HPLC)" + r('31370192'), activity_ko="AGEs 생성 억제 성분 후보로 정량됨; 꽃에서는 퀘르세틴·캠페롤 3-O-루티노사이드가 HSV-1 바이러스 직접 불활성(SI 12.5·14.6)" + r('31370192','34990769'), source=['31370192','34990769']),
 dict(name="Luteolin", name_ko="루테올린", class_="플라본", role="bioactive", part="줄기(70% 에탄올 추출물 분말)", content_text="47.79 ± 0.06 µg/10 mg 추출물(HPLC, 6개 정량 성분 중 최다)" + r('31370192'), activity_ko="항산화·항염 플라보노이드; 추출물 표준화 성분" + r('31370192'), source=['31370192']),
 dict(name="Daidzein", name_ko="다이드제인", class_="이소플라본", role="bioactive", part="줄기·지상부(70% 에탄올 추출물)", content_text="26.43 ± 0.06 µg/10 mg 추출물" + r('31370192') + "; 다른 보고 약 0.165 mg/g" + r('31795363'), activity_ko="콩과 특유의 이소플라본; 줄기 심재에서도 분리" + r('14693230'), source=['31370192','31795363','14693230']),
 dict(name="Catechin", name_ko="카테킨", class_="플라반-3-올", role="bioactive", part="줄기(70% 에탄올 추출물 분말)", content_text="23.51 ± 0.17 µg/10 mg 추출물" + r('31370192'), activity_ko="항산화 폴리페놀; 추출물 HPLC-DAD 동정 성분" + r('31370192','31618776'), source=['31370192','31618776']),
 dict(name="Genistein", name_ko="제니스테인", class_="이소플라본", role="bioactive", part="줄기·지상부(70% 에탄올 추출물)", content_text="11.54 ± 0.09 µg/10 mg 추출물" + r('31370192') + "; 다른 보고 약 0.053 mg/g" + r('31795363'), activity_ko="AGEs 생성 억제·AGEs 분해 활성(시험관)" + r('29157823'), source=['31370192','31795363','29157823']),
 dict(name="Quercetin", name_ko="퀘르세틴", class_="플라보놀", role="bioactive", part="지상부(70% 에탄올 추출물)", content_text="약 0.853 mg/g 추출물(연구진의 이전 HPLC 분석 인용)" + r('31795363'), activity_ko="AGEs 생성 억제·분해 활성 성분" + r('29157823'), source=['31795363','29157823']),
 dict(name="Naringenin", name_ko="나린제닌", class_="플라바논", role="bioactive", part="줄기·지상부(70% 에탄올 추출물)", content_text="1.19 ± 0.02 µg/10 mg 추출물" + r('31370192') + "; 다른 보고 약 0.08 mg/g" + r('31795363'), activity_ko="항산화·항염 플라보노이드" + r('31795363'), source=['31370192','31795363']),
 dict(name="Kaempferol 3-O-galactoside", name_ko="캠페롤-3-O-갈락토사이드(트리폴린)", class_="플라보놀 배당체", role="marker", part="싸리꿀(단화밀)", content_text="90.2–430.1 µg/kg 꿀; 비교한 다른 꿀에서는 검출 안 됨" + r('36076382'), activity_ko="싸리꿀 진위 판별 지표; 장 세포 염증·페롭토시스 억제(세포)" + r('36076382','39199146'), source=['36076382','39199146']),
 dict(name="Chlorogenic acid", name_ko="클로로겐산", class_="페놀산", role="bioactive", part="싸리꿀", content_text="16.3 ± 5.7 mg/kg(8개 양봉장 48개 시료, UHPLC-QQQ-MS/MS)" + r('37891888'), activity_ko="꿀의 주요 폴리페놀; 항산화" + r('37891888'), source=['37891888']),
 dict(name="Glycitein", name_ko="글리시테인", class_="이소플라본", role="bioactive", part="싸리꿀", content_text="17.3 ± 3.4 mg/kg(48개 시료)" + r('37891888'), activity_ko="O-메틸화 이소플라본; 라디칼 소거" + r('37891888'), source=['37891888']),
 dict(name="Vitexin", name_ko="비텍신", class_="플라본 C-배당체", role="bioactive", part="줄기(70% 메탄올 추출물의 에틸아세테이트 분획)", content_text="분획의 주성분으로 동정, 함량은 확인하지 못함" + r('26858533'), activity_ko="항염·티로시네이스 억제 활성 후보(분획 IC50 1.0 µg/mL)" + r('26858533'), source=['26858533']),
 dict(name="Lespedezol A", name_ko="레스페데졸 A", class_="프테로카르펜", role="bioactive", part="줄기껍질", content_text="분리 보고, 함량은 확인하지 못함" + r('31004693'), activity_ko="HSV-1 바이러스 직접 불활성(SI ≥ 10)" + r('34990769'), source=['31004693','34990769']),
 dict(name="1-Methoxyerythrabyssin II", name_ko="1-메톡시에리트라비신 II", class_="프테로카르판", role="bioactive", part="뿌리·뿌리껍질", content_text="분리 보고, 함량은 확인하지 못함" + r('21911291','31675225'), activity_ko="세균 뉴라미니데이스 억제(6종 IC50 0.09–3.25 μM 범위), 백혈병 세포 증식 억제" + r('21911291','31675225'), source=['21911291','31675225']),
 dict(name="2-Geranyl-1-methoxyerythrabyssin II", name_ko="2-게라닐-1-메톡시에리트라비신 II", class_="프레닐화 프테로카르판", role="bioactive", part="뿌리(싸리에서 분리)", content_text="분리 보고, 함량은 확인하지 못함" + r('37782374'), activity_ko="간세포 지질 축적·염증 억제(AMPK 활성화, 세포·동물)" + r('37782374'), source=['37782374']),
 dict(name="Condensed tannins", name_ko="응축 탄닌(프로안토시아니딘)", class_="탄닌", role="bioactive", part="잎", content_text="사료식물 19종 중 탄닌이 많은 6종에 속함; 정량값은 확인하지 못함" + r('2461730'), activity_ko="단백질 침전, 트립신·α-아밀레이스·리파아제 억제(시험관)" + r('2461730'), source=['2461730']),
]
for c in compounds:
    c["class"] = c.pop("class_")
    c["source"] = [N[k] for k in c["source"]]
compounds = [{k: c[k] for k in ("name","name_ko","class","role","part","content_text","activity_ko","source")} for c in compounds]

E = dict(instrument="", column="", mobile_phase="", gradient="", flow="", temp="", detection="", injection="", sample_prep="", standard="", linearity="", lod="", loq="", recovery="")
def cond(**kw):
    d = dict(E); d.update(kw); return d
assays = [
 {"role": "literature", "compound": "Rutin", "compound_ko": "루틴 등 6종(카테킨·다이드제인·루테올린·나린제닌·제니스테인)",
  "part": "줄기(stalk) 70% 에탄올 추출물 분말 — 식품원료 목록의 사용가능부위(순·잎)와 다름",
  "content": "추출물 10 mg당 카테킨 23.51 ± 0.17 µg, 루틴 43.69 ± 0.02 µg, 다이드제인 26.43 ± 0.06 µg, 루테올린 47.79 ± 0.06 µg, 나린제닌 1.19 ± 0.02 µg, 제니스테인 11.54 ± 0.09 µg" + r('31370192'),
  "method": "HPLC-PDA(283 nm)",
  "conditions": cond(instrument="Waters e2695 분리 모듈 + 포토다이오드 어레이 검출기, 자동시료주입기", column="C18, 250 × 4.6 mm, 5 µm(제조사 표기 없음)", mobile_phase="A 아세토니트릴, B 0.1% 인산", gradient="A 7→90%, 60분", flow="1 mL/min", temp="30 °C", detection="UV 283 nm", injection="10(원문에 단위 누락)", sample_prep="분말 시료를 70% 에탄올로 추출 → 여과 → 회전증발 건조, 4 °C 보관", standard="루틴·카테킨·제니스테인·다이드제인·나린제닌·루테올린 혼합 표준액(각 1 mg/mL), 머무름 시간으로 피크 확인(카테킨 10.18분, 루틴 17.45분, 다이드제인 28.83분, 루테올린 30.7분, 나린제닌 35.28분, 제니스테인 35.32분)"),
  "rationale": "연구진이 추출물 표준화를 위해 HPLC로 정량한 주성분이며, 제니스테인·퀘르세틴 등이 AGEs 생성 억제 성분으로 제시되었다" + r('31370192','29157823') + ". 같은 연구진의 다른 논문은 제니스테인 약 0.053 mg/g, 다이드제인 0.165 mg/g으로 달리 인용해 둘 다 적는다" + r('31795363') + ". 직선성·검출한계·회수율은 원문에 없다.",
  "source": [N['31370192']], "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC6723630/", "source_kind": "paper"},
 {"role": "literature", "compound": "Chlorogenic acid", "compound_ko": "클로로겐산·글리시테인 등 싸리꿀 폴리페놀 12종(루틴·미리시트린·워고닌 등)",
  "part": "싸리꿀(꽃꿀 유래 — 식품원료 목록의 싸리나무 원료와 다른 식품)",
  "content": "클로로겐산 16.3 ± 5.7 mg/kg, 글리시테인 17.3 ± 3.4 mg/kg(8개 양봉장 48개 시료)" + r('37891888'),
  "method": "UHPLC-QQQ-MS/MS(MRM, ESI)",
  "conditions": cond(instrument="Agilent UHPLC + 삼중사중극자 질량분석기(ESI); 동정은 Agilent 1290 + Q-TOF", column="Agilent Eclipse Plus C18, 2.1 × 100 mm, 1.8 µm", mobile_phase="A 물(0.1% 포름산), B 아세토니트릴(0.1% 포름산)", gradient="B 5%(0–1분) → 50%(2분) → 50%(5분) → 100%(5.1분) → 100%(6분), 후처리 2분", flow="0.35 mL/min", detection="MRM; 모세관 전압 3.5 kV, fragmentor 380 V, 건조 가스 200 °C·15 L/min, 시스 가스 330 °C·12 L/min, 네뷸라이저 45 psi(성분별 전이는 표에만 있음)", injection="2 µL(원문 이동상 문장 안에 표기)", sample_prep="꿀 5 g + 물 10 mL, 1분 볼텍스 → 8000 × g 5분 원심 → 상등액을 Bond Elut PPL C18 SPE(500 mg, 6 cc)에 농축 → 메탄올 용출 → 질소 건조 → 에탄올 1 mL에 녹임(200 mg/mL)", standard="클로로겐산·페룰산·비텍신·루틴·갈산·미리시트린·모린·글리시테인·워고닌·캠페롤-3-O-소포로사이드·리퀴리티게닌·부틴(순도 > 98%)"),
  "rationale": "싸리꿀의 항산화·항염 활성 근거 성분으로 정량했으며 클로로겐산과 글리시테인이 가장 많았다" + r('37891888') + ". 칼럼 온도·검출한계·회수율은 전문에서 확인하지 못함.",
  "source": [N['37891888']], "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10604429/", "source_kind": "paper"},
 {"role": "literature", "compound": "Kaempferol 3-O-galactoside", "compound_ko": "캠페롤-3-O-갈락토사이드(트리폴린)",
  "part": "싸리꿀(단화밀)",
  "content": "싸리꿀에서 90.2–430.1 µg/kg, 순비기나무·아카시아·대추·피나무 꿀에서는 검출 안 됨" + r('36076382'),
  "method": "질량분석 기반 비표적 분석(OPLS-DA)으로 지표 선정 후 정량",
  "conditions": dict(E),
  "rationale": "싸리꿀 위조를 가릴 지표로 제안되었다; 초록에 검출한계 0.002 mg/kg, 직선성 R ≥ 0.99, 회수율 90.2–110.6%가 적혀 있다" + r('36076382') + ". 전문 확인 못함(초록만 확인)이라 칼럼·이동상 등 조건 칸은 비워 둠.",
  "source": [N['36076382']], "url": "https://pubmed.ncbi.nlm.nih.gov/36076382/", "source_kind": "paper"},
]

src = [{"n": N[k], "title": t, "url": u, "publisher": p, "accessed": a} for k, t, u, p, a in S]
d = {
 "slug": "lespedeza-bicolor", "name_ko": "싸리나무", "name_en": "Shrub lespedeza (bush clover)",
 "scientific_name": "Lespedeza bicolor Turcz.",
 "aliases": ["싸리", "싸리나무순", "싸리나무잎", "싸리나무추출액", "Shrub lespedeza", "bush clover"],
 "sections": [{"key": k, "title": t, "body": b} for k, t, b in sections],
 "compounds": compounds, "markers": [], "assays": assays, "nutrients": [], "production": [], "world": [], "gi": [], "orgs": [],
 "sources": src,
}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in d["sections"]: print(s["key"], len(s["body"]))
print(len(src), len(compounds))
