import json
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "dossier.json"
ACC = "2026-11-02"
I1020 = "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020"


def pm(pmid):
    return f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"


S = [
    (1, "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 황소비단그물버섯(Suillus bovinus (Pers.) Roussel), 사용가능, 사용가능부위 : 자실체 (로컬 원자료 I1020_20261013.json 대조)", I1020, "식품의약품안전처", "2026-10-13"),
    (2, "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 같은 속 항목: 큰비단그물버섯(Suillus grevillei)·비단그물버섯자실체(Suillus luteus)·좀황금비단그물버섯(Suillus pictus / Boletinus pictus)·녹슬은비단그물버섯(Suillus viscidus / S. laricinus) 사용가능, 평원비단그물버섯(Suillus placidus) 사용불가 (로컬 원자료 대조)", I1020, "식품의약품안전처", "2026-10-13"),
    (3, "통계청 「농작물생산조사」·농림축산식품부 「특용작물 생산실적」(1995–2024) 로컬 파싱본(docs/stats/regional_crops.csv·special_crops_annual.csv·special_crops_2024.csv)과 식약처 「식품 등의 생산실적」 파싱본(hf_items.csv) — '황소비단그물버섯' 품목 없음 확인('버섯류'로만 집계)", "https://www.mafra.go.kr", "농림축산식품부·통계청·식품의약품안전처", ACC),
    (4, "Molecular Taxonomical Re-classification of the Genus Suillus Micheli ex S. F. Gray in South Korea (Mycobiology, 2014; PMC4206787 전문; PMID 25346598)", pm(25346598), "Mycobiology (PubMed)", ACC),
    (5, "Mercury bioaccumulation by Suillus bovinus mushroom and probable dietary intake with the mushroom meal (Environ Sci Pollut Res Int, 2016; PMC4943988 전문; PMID 27068912)", pm(27068912), "Environmental Science and Pollution Research (PubMed)", ACC),
    (6, "Mercury in edible mushrooms from the area of Kościersk forests and from the Vistula peninsula (Rocz Panstw Zakl Hig, 1996; 폴란드어 논문, 영문 초록; PMID 9064742)", pm(9064742), "Roczniki Panstwowego Zakladu Higieny (PubMed)", ACC),
    (7, "Radioactive Contamination of Wild Mushrooms from Ukraine under Conditions of Contrasting Radiation Loads: 36 Years after the Chernobyl Nuclear Power Plant Catastrophe (Int J Med Mushrooms, 2022; 초록; PMID 36004707)", pm(36004707), "International Journal of Medicinal Mushrooms (PubMed)", ACC),
    (8, "Levels of platinum group elements and rare-earth elements in wild mushroom species growing in Poland (Food Addit Contam Part A, 2016; 초록; PMID 26515437)", pm(26515437), "Food Additives & Contaminants: Part A (PubMed)", ACC),
    (9, "Extraction Optimization and Characterization of Antioxidant Polysaccharides From Suillus bovinus (Food Sci Nutr, 2025; PMC12447242 전문; PMID 40979573)", pm(40979573), "Food Science & Nutrition (PubMed)", ACC),
    (10, "In vitro inhibitory effects of pulvinic acid derivatives isolated from Chinese edible mushrooms, Boletus calopus and Suillus bovinus, on cytochrome P450 activity (Biosci Biotechnol Biochem, 2009; 초록; PMID 19352038)", pm(19352038), "Bioscience, Biotechnology, and Biochemistry (PubMed)", ACC),
    (11, "Meroterpenoids with BACE1-inhibitory activity from the fruiting bodies of Suillus bovinus and Boletinus cavipes (J Nat Med, 2025; 초록; PMID 39614969)", pm(39614969), "Journal of Natural Medicines (PubMed)", ACC),
    (12, "Bioassay-guided isolation of three new alkaloids from Suillus bovinus and preliminary mechanism against ginseng root rot (Front Microbiol, 2024; PMC11096550 전문; PMID 38756729)", pm(38756729), "Frontiers in Microbiology (PubMed)", ACC),
    (13, "Antioxidant capacities, phenolic compounds and polysaccharide contents of 49 edible macro-fungi (Food Funct, 2012; 초록; PMID 22868715)", pm(22868715), "Food & Function (PubMed)", ACC),
    (14, "Non-targeted and targeted analysis of wild toxic and edible mushrooms using gas chromatography-ion trap mass spectrometry (Talanta, 2014; 초록; PMID 24274300)", pm(24274300), "Talanta (PubMed)", ACC),
    (15, "Fatty Acid Determination and Activity Evaluation of Wild Higher Fungi from Southern Sichuan, China (Int J Med Mushrooms, 2025; 초록; PMID 40743717)", pm(40743717), "International Journal of Medicinal Mushrooms (PubMed)", ACC),
    (16, "Constituents of the higher fungi. IX. Bovinone, 2,5-dihydroxy-3-geranylgeranyl-1,4-benzoquinone from Boletus (Suillus) bovinus (Linn. ex Fr.) Kuntze (J Chem Soc Perkin 1, 1969; 서지만; PMID 5391288)", pm(5391288), "Journal of the Chemical Society (PubMed)", ACC),
    (17, "Constituents of the higher fungi. XI. Boviquinone-3, diboviquinone-3,4, methylenediboviquinone-3,3, and xerocomic acid from Gomphidius rutilus Fr. and diboviquinone-4,4 from Boletus (Suillus) bovinus (Linn ex Fr.) Kuntze (J Chem Soc Perkin 1, 1971; 서지만; PMID 5167257)", pm(5167257), "Journal of the Chemical Society (PubMed)", ACC),
    (18, "Negative ion tandem mass spectrometry of prenylated fungal metabolites and their derivatives (Anal Bioanal Chem, 2013; 초록; PMID 23090652)", pm(23090652), "Analytical and Bioanalytical Chemistry (PubMed)", ACC),
    (19, "Chromosome-Level Assembly and Comparative Genomic Analysis of Suillus bovinus Provides Insights into the Mechanism of Mycorrhizal Symbiosis (J Fungi, 2024; 초록; PMID 38535219)", pm(38535219), "Journal of Fungi (PubMed)", ACC),
    (20, "Two phylogenetically highly distinct beta-tubulin genes of the basidiomycete Suillus bovinus (Curr Genet, 2005; 초록; PMID 15770509)", pm(15770509), "Current Genetics (PubMed)", ACC),
    (21, "Genetic diversity and interrelationships among common European Suillus species based on ribosomal DNA sequences (FEMS Microbiol Lett, 2001; 초록; PMID 11682189)", pm(11682189), "FEMS Microbiology Letters (PubMed)", ACC),
    (22, "Unravelling the complex relationship between Suillus bovinus and Gomphidius roseus through investigation of their sporocarps in Pinus massoniana forests (BMC Microbiol, 2025; PMC11938738 전문; PMID 40133810)", pm(40133810), "BMC Microbiology (PubMed)", ACC),
    (23, "Population structure and dynamics in Suillus bovinus as indicated by spatial distribution of fungal clones (New Phytol, 1990; 초록; PMID 33874270)", pm(33874270), "New Phytologist (PubMed)", ACC),
    (24, "Size, distribution and biomass of genets in populations of Suillus bovinus (L.: Fr.) Roussel revealed by somatic incompatibility (New Phytol, 1994; 초록; PMID 33874369)", pm(33874369), "New Phytologist (PubMed)", ACC),
    (25, "Flavonoids induce germination of basidiospores of the ectomycorrhizal fungus Suillus bovinus (Mycorrhiza, 2007; 초록; PMID 17516095)", pm(17516095), "Mycorrhiza (PubMed)", ACC),
    (26, "Effects of four bolete species on ectomycorrhizae formation and development in Pinus thunbergii and Quercus acutissima (BMC Ecol Evol, 2024; 초록; PMID 38664655)", pm(38664655), "BMC Ecology and Evolution (PubMed)", ACC),
    (27, "Ectomycorrhizal fungi as an alternative to the use of chemical fertilisers in nursery production of Pinus pinaster (J Environ Manage, 2010; 초록; PMID 20702021)", pm(20702021), "Journal of Environmental Management (PubMed)", ACC),
    (28, "A zinc-adapted fungus protects pines from zinc stress (New Phytol, 2004; 초록; PMID 33873519)", pm(33873519), "New Phytologist (PubMed)", ACC),
    (29, "Zinc export results in adaptive zinc tolerance in the ectomycorrhizal basidiomycete Suillus bovinus (Metallomics, 2013; 초록; PMID 23715468)", pm(23715468), "Metallomics (PubMed)", ACC),
    (30, "Effects of thinning treatment on an ectomycorrhizal succession under Scots pine (Mycol Res, 2003; 초록; PMID 12825501)", pm(12825501), "Mycological Research (PubMed)", ACC),
    (31, "T-DNA transfer and integration in the ectomycorrhizal fungus Suillus bovinus using hygromycin B as a selectable marker (Curr Genet, 2002; 초록; PMID 12174821)", pm(12174821), "Current Genetics (PubMed)", ACC),
    (32, "Terpenoids are associated with cytokinin and auxin signaling during mycorrhiza formation in the Suillus bovinus-Pinus yunnanensis symbiosis (Plant Physiol Biochem, 2026; 초록; PMID 41352302)", pm(41352302), "Plant Physiology and Biochemistry (PubMed)", ACC),
    (33, "Effect of cadmium on growth and glucose utilisation of ectomycorrhizal fungi in vitro (Mycorrhiza, 2003; 초록; PMID 12687448)", pm(12687448), "Mycorrhiza (PubMed)", ACC),
]

sections = [
    ("overview", "한눈에 보기",
     "황소비단그물버섯(Suillus bovinus)은 소나무류 뿌리와 공생하는 외생균근성 그물버섯류로, 영문 논문에서는 'European Cow Bolete'라는 이름으로도 불린다[5, 22]. "
     "식품의약품안전처 「식품원료 목록」에는 원료명 '황소비단그물버섯', 학명 'Suillus bovinus (Pers.) Roussel'로 올라 있고, 상태는 '사용가능', 사용 조건은 '사용가능부위 : 자실체'이다[1]. "
     "따라서 일반 식품의 원료로는 자실체(버섯 몸체)만 쓸 수 있으며, 건강기능식품 고시형 원료의 원재료 목록에는 없어 고시된 지표성분과 기준은 확인하지 못함.\n\n"
     "같은 목록에는 큰비단그물버섯(S. grevillei)·비단그물버섯(S. luteus)·좀황금비단그물버섯(S. pictus)·녹슬은비단그물버섯(S. viscidus)이 별도 원료로 올라 있고 평원비단그물버섯(S. placidus)은 '사용불가'이므로, 이 문서는 그 종들의 자료를 섞지 않는다[2]. "
     "국내 표본을 유전자로 다시 동정한 연구에서 이 종은 한국에 실제로 분포하는 비단그물버섯속 8종 가운데 하나로 확인되었다[4]. "
     "연구는 소나무류와의 공생·중금속 내성, 자실체의 퀴논·풀빈산류·알칼로이드·다당류, 수은과 방사성 세슘 축적에 모여 있다[5, 7, 9–12, 28]. "
     "사람 대상 임상시험은 확인하지 못함."),
    ("history", "이름과 이용의 역사",
     "1969년과 1971년의 성분 연구는 이 버섯을 'Boletus (Suillus) bovinus (Linn. ex Fr.) Kuntze'로 적어, 예전에는 그물버섯속(Boletus)에 넣어 다루었음을 보여 준다[16, 17]. "
     "명명자 표기는 문헌마다 달라 식약처 목록은 '(Pers.) Roussel', 국내 분류 재검토 논문은 '(L.) Roussel(1796)', 다른 논문들은 '(L.: Fr.) Roussel'이나 '(L. ex Fr.) O. Kuntze'를 쓴다[1, 4, 23, 24]. "
     "국내 재검토 논문에 따르면 비단그물버섯속이라는 속명은 1959년부터 국내 종에 쓰였고, 그 전에는 일부 종이 다른 속으로 분류되었다[4]. "
     "같은 논문은 1988–2013년 국내 표본 117점 가운데 51점(43%)이 처음에 잘못 동정되었다고 보고해, 옛 기록의 종명은 조심해서 읽어야 한다[4]. "
     "중국에서는 이 버섯과 이 버섯 곁에서 나는 Gomphidius roseus 모두 식용 자실체로 널리 채취되어 판매되거나 집에서 소비된다[22]. "
     "중국 허베이성 스자좡의 시장에서 산 자실체로 다당류를 연구한 사례가 있고, 일본 연구는 이 버섯을 중국의 식용버섯으로 소개했다[9, 10]. "
     "국내에서 식용으로 이용된 역사 기록은 확인하지 못함."),
    ("biology", "균학적 특징",
     "국내 표본 기재에 따르면 갓은 지름 30–100 mm로 어릴 때 가장자리가 안으로 말린 둥근 산 모양이다가 자라면 편평해지며, 표면은 매끈하고 약간 끈적이며 갈색빛 주황~적갈색이다[4]. "
     "살은 흰색~황백색으로 단단하고 잘라도 색이 변하지 않으며, 대는 길이 30–75 mm, 굵기 5–10 mm이고 갓과 비슷한 색이다[4]. "
     "관공은 회황색이고 구멍은 방사상으로 늘어선 불규칙한 다각형이며, 포자는 7.2–10.2 × 3–4.4 µm의 매끈한 타원형이다[4]. "
     "국내 재검토 논문은 이 종이 젖빛 방울을 내지 않는 점으로 비슷한 종과 구별된다고 적었으나, 추출된 본문에는 학명이 빠져 있어 이 기재는 명명자(L.) Roussel·1796년과 검색표로 이 종의 것이라 판단했다[4]. "
     "중국 마미송림 연구는 이 종을 무리 지어 나는 그물버섯으로, 갓은 연노랑~짙은 주황, 대에 턱받이가 없고 포자문은 갈색이라고 기재했다[22]. "
     "자실체 밑의 균근은 산호 모양의 노란빛이며 균사가 멀리 뻗는 '장거리 탐색형'이다[22]. "
     "스웨덴 구주소나무 숲에서는 숲이 오래될수록 한 유전 개체(genet)의 크기가 커지고 수는 줄어, 어린 숲 1 ha당 700–5,700개에서 오래된 숲 30–120개로 줄었다[24]."),
    ("related_species", "가까운 종과 혼동",
     "비단그물버섯속은 자실체 모양만으로 종을 가리기 어려워, 국내 표본 117점 가운데 51점이 같은 속의 다른 종으로 잘못 동정되어 있었다[4]. "
     "유럽 비단그물버섯속 7종의 ITS 염기서열 비교에서 황소비단그물버섯은 다른 모든 종과의 차이가 11.4–13.3으로 가장 컸다[21]. "
     "식약처 목록에서 같은 속의 큰비단그물버섯·비단그물버섯·좀황금비단그물버섯·녹슬은비단그물버섯은 각각 별도의 사용가능 원료이고, 평원비단그물버섯은 사용불가 원료이다[2]. "
     "따라서 같은 속의 다른 종에서 나온 성분·안전성 자료를 이 종에 옮겨 쓰면 안 된다[2, 4]. "
     "이 종의 자실체는 Gomphidius roseus와 함께 나는 일이 잘 알려져 있는데, 중국 연구에서 이 버섯은 늘 황소비단그물버섯 곁에서만 발견되었다[22]. "
     "두 버섯의 자실체와 균근에는 서로의 균사가 섞여 있었지만, 대사체 조성은 이 종이 비단그물버섯과 더 비슷했다[22]. "
     "일본 연구는 풀빈산 유도체를 이 종과 다른 그물버섯(Boletus calopus)에서 함께 분리했으므로, 그 결과를 이 종만의 것으로 읽어서는 안 된다[10]."),
    ("cultivation", "발생과 채취",
     "이 버섯은 살아 있는 나무뿌리와 공생해야 자실체를 맺는 외생균근균으로, 소나무류와 균근을 만든다[19, 22]. "
     "국내에서는 여름부터 가을에 홀로 또는 무리 지어 난다[4]. "
     "중국 구이저우의 마미송 순림 조사에서는 1–5년생부터 30년 넘은 숲까지 모든 숲에서 자실체가 났고, 숲 나이에 따라 2–12월 사이에 발생했고 대체로 봄(3–5월)과 가을(9–11월)에 많이 기록되었다[22]. "
     "영국 구주소나무 조림지 16년 관찰에서는 50% 간벌 뒤 이 종의 자실체 수가 늘었다[30]. "
     "포자는 실험실에서 잘 싹트지 않지만 헤스페리딘·모린·루틴 등 일부 플라보노이드가 발아를 촉진했다[25]. "
     "곰솔·상수리나무 묘목에 이 종을 포함한 그물버섯류 4종을 접종하면 3개월 뒤 균근 감염률이 40–55%였고, 해안소나무(Pinus pinaster) 묘목 생산에서 이 종·Laccaria laccata·Lactarius deterrimus 균사를 섞어 접종하면 비료 없이 생장과 양분 상태가 좋아졌다[26, 27]. "
     "아연 오염지에서 온 이 종의 계통은 아연을 세포 밖으로 내보내 내성을 보였고, 이를 접종한 소나무도 아연 스트레스를 덜 받았다[28, 29]. 반면 시험관 배양에서 카드뮴에 대한 건물 생산 감수성은 함께 시험한 균근균 3종 가운데 이 종이 가장 컸다[33]. "
     "버섯 자체를 인공 재배해 생산한다는 공식 자료는 확인하지 못함."),
    ("processing", "가공과 이용",
     "식약처 목록상 식품 원료로 쓸 수 있는 부위는 자실체뿐이다[1]. "
     "다당류 연구에서는 자실체를 물로 추출해 액체 대 고체 28 mL/g, 46 ℃, 4시간 조건에서 조다당 수율 22.29 ± 0.44%를 얻었다[9]. "
     "이를 정제한 네 분획(분자량 47.34–97.07 kDa) 가운데 Y-1(97.07 kDa)만 간암세포(HepG2)의 산화 스트레스 모델에서 활성을 보였고, 50 µg/mL에서 활성산소를 34.73 ± 1.31% 줄였다[9]. "
     "Y-1은 만노스(40.78%)와 포도당(24.17%)이 주를 이루는 헤테로다당이었다[9]. "
     "알칼로이드 연구에서는 9월에 채집한 생자실체를 48시간 공기 건조한 뒤 95% 에탄올로 추출했다[12]. "
     "수은 조사에서는 자실체를 갓과 대로 나눠 65 ℃에서 항량이 될 때까지 말린 뒤 분쇄했다[5]. "
     "이 결과들은 모두 시험관·세포 수준이며 식품 가공 공정이나 제품에 대한 자료는 아니다[9, 12]. "
     "식약처 「식품 등의 생산실적」 파싱본에는 이 원료 이름의 품목이 없고 농작물·특용작물 통계에도 이 종은 따로 집계되지 않아, 국내 제품·원료 생산 규모는 확인하지 못함[3]."),
    ("genetics", "유전체와 유전 다양성",
     "중국 연구진은 일루미나·HiFi·Hi-C 기술로 염색체 수준 유전체를 조립했으며, 12개 염색체에 총 43.03 Mb, GC 함량 46.58%, 콘티그 N50 3.78 Mb였다[19]. "
     "예측된 단백질 암호 유전자는 11,199개였고, 소형 분비 단백질과 탄수화물 관련 효소, 테르페노이드·옥신 관련 유전자가 많아 공생에 관여할 것으로 보았다[19]. "
     "이 종의 β-튜불린 유전자 두 개는 서로 60%만 같아 한 균류 종 안에서 알려진 가장 낮은 일치도였고, 그중 tubb2에는 인트론이 최소 21개 있었다[20]. "
     "아그로박테리움을 이용해 이 종의 이핵 균사에 외래 유전자를 넣는 형질전환법도 개발되었다[31]. "
     "스웨덴 소나무숲 연구는 체세포 불화합성 시험으로 개체를 구분해, 교란된 숲에서는 포자로 새 개체가 자리 잡는 것이, 교란이 적은 숲에서는 균사 확장이 중요하다고 보았다[23]. "
     "아연 오염지 집단은 비오염지 집단보다 아연 내성이 높아, 같은 종 안에서도 서식지에 따른 유전적 적응이 있다[29]. "
     "유전체에서 찾은 테르페노이드 관련 유전자와 관련해, 이 종의 테르페노이드가 운남송(Pinus yunnanensis) 뿌리의 사이토키닌·옥신 신호 변화와 연관된다는 보고도 있으나 직접 기능 검증은 남아 있다[19, 32]. "
     "국내 집단의 유전 다양성 자료는 확인하지 못함."),
    ("safety", "안전성",
     "식약처 「식품원료 목록」에서 자실체는 '사용가능' 원료이다[1]. "
     "알레르기·중독 사례나 국내 공공기관의 이 종에 대한 별도 안전 정보는 확인하지 못함.\n\n"
     "폴란드 13개 비오염 지역(1993–2013년, 자실체 586개)에서 수은은 갓 0.10–0.79 mg/kg, 대 0.083–0.51 mg/kg(건조중 평균)이었고, 수분 90%·체중 60 kg을 가정할 때 갓 300 g 한 끼의 수은 섭취량은 참고용량의 1.4–10%로 위해 우려가 없다고 평가되었다[5]. "
     "1993/94년 폴란드 조사에서도 이 종의 수은은 갓 29–65 µg/kg 건조중으로 조사한 13종 가운데 가장 낮은 축이었다[6]. "
     "체르노빌 사고 지역의 심하게 오염된 보호구역에서는 이 종의 세슘-137이 건조중 kg당 최대 118 kBq에 이르렀다[7]. "
     "폴란드 큰길가 자실체의 백금족 원소는 0.37 ± 0.03 mg/kg 건조중으로 땅에서 나는 조사 10종 가운데 두 번째로 높았다[8]. "
     "따라서 오염 지역에서 채취한 야생 자실체는 중금속·방사성 물질을 확인해야 한다[5, 7]. "
     "이 버섯 등에서 분리한 풀빈산 유도체는 시험관에서 약물대사효소(CYP3A4 등)를 억제해, 식품-약물 상호작용 가능성이 제기되었으나 사람 자료는 확인하지 못함[10]."),
]

compounds = [
    dict(name="Bovinone", name_ko="보비논(2,5-다이하이드록시-3-제라닐제라닐-1,4-벤조퀴논)", cls="프레닐화 벤조퀴논(메로테르페노이드)", role="marker", part="자실체",
         content_text="이 종에서 분리·구조 결정(1969); 함량은 서지 정보만 확인해 확인하지 못함[16]",
         activity_ko="이 문헌에서 활성은 확인하지 못함[16]", source=[16]),
    dict(name="Diboviquinone-4,4", name_ko="다이보비퀴논-4,4", cls="프레닐화 벤조퀴논 이량체", role="marker", part="자실체",
         content_text="이 종에서 분리 보고(1971); 함량 확인하지 못함[17]",
         activity_ko="활성 확인하지 못함[17]", source=[17]),
    dict(name="Boviquinone-4", name_ko="보비퀴논-4", cls="프레닐화 벤조퀴논(메로테르페노이드)", role="bioactive", part="자실체",
         content_text="자실체 성분으로 LC-ESI-MS/MS 분해 경로 분석에 쓰임[18]; 함량 확인하지 못함",
         activity_ko="이 종 클로로폼 추출물에서 분리한 메로테르페노이드 3종이 BACE1(베타-세크레타아제)을 억제(IC50 21.2·17.8·1.0 µM, 효소 시험관)했으며 보비퀴논-4가 핵심어로 제시됨 — 화합물별 대응은 초록에서 확인하지 못함[11]", source=[11, 18]),
    dict(name="Variegatic acid", name_ko="바리에가트산", cls="풀빈산 유도체(색소)", role="bioactive", part="자실체",
         content_text="B. calopus와 이 종에서 분리(어느 종에서 얻었는지는 초록에서 구분 안 됨); 함량 확인하지 못함[10]",
         activity_ko="CYP3A4 억제 IC50 2.2 ± 0.1 µM(시험관), CYP1A2·2C9·2D6도 비특이적으로 억제[10]", source=[10]),
    dict(name="Xerocomic acid", name_ko="제로콤산", cls="풀빈산 유도체(색소)", role="bioactive", part="자실체",
         content_text="B. calopus와 이 종에서 분리(종 구분 안 됨); 함량 확인하지 못함[10]",
         activity_ko="CYP3A4 억제 IC50 2.4 ± 0.1 µM(시험관)[10]", source=[10]),
    dict(name="Atromentic acid", name_ko="아트로멘트산", cls="풀빈산 유도체(색소)", role="bioactive", part="자실체",
         content_text="B. calopus와 이 종에서 분리(종 구분 안 됨); 함량 확인하지 못함[10]",
         activity_ko="CYP3A4 억제 IC50 65.1 ± 3.9 µM(시험관, 세 화합물 가운데 가장 약함)[10]", source=[10]),
    dict(name="Bovinalkaloid A", name_ko="보비날칼로이드 A(1-아세틸-3,7-다이하이드록시-β-카볼린)", cls="β-카볼린 알칼로이드", role="bioactive", part="자실체(중국 허베이성 청더, 2022년 9월 채집)",
         content_text="에틸아세테이트 분획에서 신규 화합물로 분리, 반분취 HPLC로 화합물당 19.6–32.5 mg 분리(원료 대비 함량은 확인하지 못함)[12]",
         activity_ko="분리한 4종 가운데 1 mg/mL에서 인삼 뿌리썩음병균(Fusarium solani) 균사 생장을 100% 억제한 화합물이 있었고 MIC 2.08 mM — 본문 추출본에 화합물 번호가 빠져 어느 화합물인지는 확인하지 못함(시험관)[12]", source=[12]),
    dict(name="9-Hydroxycanthin-6-one", name_ko="9-하이드록시칸틴-6-온", cls="칸틴-6-온 알칼로이드", role="bioactive", part="자실체",
         content_text="기지 화합물로 함께 분리; 신규 유사체 보비날칼로이드 B(9-하이드록시-5-메틸칸틴-6-온)·C(9-하이드록시-4,5-다이메틸칸틴-6-온)와 같은 골격[12]",
         activity_ko="네 화합물은 1 mg/mL에서 F. solani 균사 생장을 각각 100.00%·22.31%·37.59%·59.29% 억제(시험관)[12]", source=[12]),
    dict(name="Mannose", name_ko="만노스(다당 Y-1 구성당)", cls="다당류 구성 단당", role="bioactive", part="자실체 열수 추출 다당 Y-1(97.07 kDa)",
         content_text="Y-1 단당 조성: 만노스 40.78%, 포도당 24.17%, 자일로스 15.37%, 푸코스 13.21%, 갈락토스 3.54%(HPAEC)[9]",
         activity_ko="Y-1 50 µg/mL가 t-BHP 처리 HepG2 세포의 활성산소를 34.73 ± 1.31% 줄이고 SOD·CAT·GSH-Px를 회복시킴(세포 실험)[9]", source=[9]),
    dict(name="Xylitol", name_ko="자일리톨(또는 아도니톨, 잠정 동정)", cls="5탄당 당알코올", role="marker", part="자실체",
         content_text="GC-MS 비표적 분석에서 이 종을 구별하는 종 표지 후보로 잠정 동정(자일리톨 또는 아도니톨); 함량 확인하지 못함[14]",
         activity_ko="종 판별 표지 후보이며 생리활성 시험은 없음[14]", source=[14]),
    dict(name="Phenolic compounds", name_ko="총페놀 화합물", cls="페놀류", role="bioactive", part="자실체",
         content_text="중국 식용버섯 49종 가운데 항산화능·총페놀 함량이 가장 높은 종에 속함(수치는 초록에서 확인하지 못함)[13]",
         activity_ko="TEAC·FRAP 항산화능과 총페놀 함량이 양의 상관(시험관)[13]; 쓰촨 야생버섯 29종 조사에서도 DPPH·ABTS 소거능이 좋았음[15]", source=[13, 15]),
]

assays = [
    {"role": "literature", "compound": "Mercury (total Hg)", "compound_ko": "총수은", "part": "자실체 갓·대(폴란드 13개 비오염 지역, 1993–2013년, 586개체)",
     "content": "갓 0.10 ± 0.06 – 0.79 ± 0.40 mg/kg 건조중, 대 0.083 ± 0.028 – 0.51 ± 0.22 mg/kg 건조중(지역별 평균); 개체별 갓 0.015–1.7 mg/kg 건조중[5]",
     "method": "CV-AAS(열분해–금 아말감 포집 냉증기 원자흡광)",
     "conditions": {"instrument": "수은 분석기 MA-2000(자동시료주입기, 저·고 모드)", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "",
                    "detection": "원자흡광 296 nm", "injection": "", "sample_prep": "갓·대 분리 후 65 ℃에서 항량 건조, 자기 막자사발로 분쇄, 폴리에틸렌 봉투 보관",
                    "standard": "공시료와 Hg 표준용액 100·150·200 µL 주입으로 검량선(매주 새로 작성)",
                    "linearity": "", "lod": "0.003 mg/kg 건조중", "loq": "0.005 mg/kg 건조중",
                    "recovery": "인증표준물질(건조 버섯 분말) CS-M-1 표시값 0.174 ± 0.018, 측정 0.185 ± 0.011 mg/kg(n=13); CS-M-2 표시값 0.164 ± 0.004, 측정 0.165 ± 0.005 mg/kg(n=8)"},
     "rationale": "야생 식용버섯의 대표적 위해 원소로, 이 종의 생물농축계수(갓 6.4–45)와 한 끼 섭취 위해도 평가에 쓰였다. PMC 전문 Methods에서 조건을 옮겼다[5].",
     "source": [5], "url": pm(27068912), "source_kind": "paper"},
    {"role": "literature", "compound": "Monosaccharides of polysaccharide Y-1 (mannose, glucose, xylose, fucose, galactose)", "compound_ko": "다당 Y-1의 구성 단당(만노스 등)",
     "part": "자실체 열수 추출 조다당의 정제 분획 Y-1(97.07 kDa; 중국 스자좡 시장 구입, ITS로 종 확인)",
     "content": "만노스 40.78%, 포도당 24.17%, 자일로스 15.37%, 푸코스 13.21%, 갈락토스 3.54%[9]",
     "method": "HPAEC(이온크로마토그래피)",
     "conditions": {"instrument": "이온크로마토그래피 시스템 ICS 5000+", "column": "CarboPac PA20(150 × 3.0 mm, 10 µm)", "mobile_phase": "", "gradient": "", "flow": "", "temp": "",
                    "detection": "", "injection": "",
                    "sample_prep": "Y-1을 2 M 트라이플루오로아세트산(TFA)으로 121 ℃ 2시간 가수분해, 질소로 건조, 메탄올로 반복 건조해 TFA 제거 후 멸균수에 용해",
                    "standard": "단당 13종 혼합 표준품(푸코스·람노스·아라비노스·갈락토스·포도당·자일로스·만노스·과당·리보스·갈락투론산·글루쿠론산·만누론산·굴루론산)을 시료와 같이 처리",
                    "linearity": "", "lod": "", "loq": "", "recovery": ""},
     "rationale": "세포 실험에서 항산화 활성을 보인 유일한 다당 분획의 조성 지표다. 전문을 확인했으나 이동상·유속·검출기 조건은 적혀 있지 않아 비웠다. 분자량은 겔투과크로마토그래피(Aquagel-OH MIXED-H 7.8 × 300 mm, 0.2 M 질산나트륨+0.01 M 인산이수소나트륨, 30 ℃, 1 mL/min, 10 µL)로 측정했다. 이 논문은 방법 절에는 0 M NaCl 용출분을 Y, 결과 절에는 S라고 적어 표기가 서로 다르다[9].",
     "source": [9], "url": pm(40979573), "source_kind": "paper"},
    {"role": "literature", "compound": "Widely targeted metabolites (lipids, amino acids, phenolic acids, organic acids)", "compound_ko": "광범위 표적 대사체(지질·아미노산·페놀산·유기산 등)",
     "part": "자실체(중국 구이저우 마미송 순림, 2021년 5월 채집, 동결건조)",
     "content": "이 종·Gomphidius roseus·비단그물버섯 자실체에서 모두 683종 검출, 574종은 세 종 공통(상대량; 절대 함량 없음)[22]",
     "method": "UHPLC-ESI-MS/MS(MRM)",
     "conditions": {"instrument": "UHPLC–전기분무 삼중사중극자 질량분석", "column": "Agilent SB-C18(규격은 본문에 없음)",
                    "mobile_phase": "A: 0.1% 개미산 물, B: 0.1% 개미산 아세토니트릴", "gradient": "95% A → 95% B, 9분", "flow": "0.35 mL/min", "temp": "40 ℃",
                    "detection": "양이온 모드 다중반응검출(MRM)", "injection": "4 µL",
                    "sample_prep": "동결건조 분말 100 mg을 70% 메탄올 1.2 mL에 녹여 주기적으로 교반하고 냉장 하룻밤, 원심 분리 후 여과",
                    "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""},
     "rationale": "이 종의 영양·풍미 관련 대사체를 근연 식용균과 비교한 자료다. 전문 Methods에서 옮겼으나 추출본에 학명이 빠져 있어 종별 검출 수(629·622·632종)는 어느 종의 값인지 확인하지 못함[22].",
     "source": [22], "url": pm(40133810), "source_kind": "paper"},
    {"role": "literature", "compound": "Cesium-137", "compound_ko": "세슘-137(방사성)", "part": "자실체(우크라이나 지토미르 폴리시아 드레블랸스키 자연보호구역, 2013년 이후)",
     "content": "최대 118 kBq/kg 건조중(토양 표면 세슘-137 오염 555–1,480 kBq/m² 지역)[7]",
     "method": "방사능 측정(측정 방법은 초록에 없음)",
     "conditions": {"instrument": "", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "", "injection": "", "sample_prep": "", "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""},
     "rationale": "원전 사고 오염지에서 야생 식용버섯 섭취의 주된 위해 지표다. 초록만 확인했고 전문 확인 못함[7].",
     "source": [7], "url": pm(36004707), "source_kind": "paper"},
]

d = {
    "slug": "suillus-bovinus",
    "name_ko": "황소비단그물버섯",
    "name_en": "European cow bolete",
    "scientific_name": "Suillus bovinus (Pers.) Roussel",
    "aliases": ["Suillus bovinus", "Boletus bovinus", "European cow bolete", "황소비단그물버섯"],
    "sections": [{"key": k, "title": t, "body": b} for k, t, b in sections],
    "compounds": [{"name": c["name"], "name_ko": c["name_ko"], "class": c["cls"], "role": c["role"], "part": c["part"],
                   "content_text": c["content_text"], "activity_ko": c["activity_ko"], "source": c["source"]} for c in compounds],
    "markers": [],
    "assays": assays,
    "nutrients": [],
    "production": [],
    "world": [],
    "gi": [],
    "orgs": [],
    "sources": [{"n": n, "title": t, "url": u, "publisher": p, "accessed": a} for n, t, u, p, a in S],
}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in d["sections"]:
    print(s["key"], len(s["body"]))
