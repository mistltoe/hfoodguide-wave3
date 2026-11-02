import json
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "dossier.json"
ACC = "2026-11-02"


def pm(pmid, title, journal, year):
    return {"title": f"{title} ({journal}, {year}; PMID {pmid})", "url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
            "publisher": f"{journal} (PubMed)", "accessed": ACC}


S = [
    {"title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 버들송이(Agrocybe cylindracea (DC. ex Fr.) Maire)",
     "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},  # 1
    pm("33046967", "Multilocus phylogeny- and fruiting feature-assisted delimitation of European Cyclocybe aegerita from a new Asian species complex and related species (PMC7541202 전문)", "Mycological Progress", 2020),  # 2
    pm("32561469", "Genome Assembly and Pathway Analysis of Edible Mushroom Agrocybe cylindracea (PMC7801210 전문)", "Genomics, Proteomics & Bioinformatics", 2020),  # 3
    pm("42894792", "White Agrocybe cylindracea outperforms the brown strain in nutritional value, flavor profile, and anticancer activity (PMC13676911 전문)", "Food Chemistry: X", 2026),  # 4
    pm("31150766", "Isolation and structural elucidation of a novel brunnein-type antioxidant β-carboline alkaloid from Cyclocybe cylindracea (초록)", "Fitoterapia", 2019),  # 5
    pm("25173078", "Lethal protein in mass consumption edible mushroom Agrocybe aegerita linked to strong hepatic toxicity (초록)", "Toxicon", 2014),  # 6
    pm("33917246", "Ageritin from Pioppino Mushroom: The Prototype of Ribotoxin-Like Proteins, a Novel Family of Specific Ribonucleases in Edible Mushrooms (초록)", "Toxins", 2021),  # 7
    pm("38978692", "Risk assessment of multiple pesticide residues in Agrocybe aegerita: Based on a 3-year monitoring survey (PMC11228446 전문)", "Food Chemistry: X", 2024),  # 8
    pm("32506407", "Metal concentration and health risk assessment of fifteen wild mushrooms collected from the Ankara University Campus (Turkey) (초록)", "Environmental Science and Pollution Research", 2020),  # 9
    pm("33436255", "Comprehensive evaluation of alkali-extracted polysaccharides from Agrocybe cylindracea: Comparison on structural characterization (초록)", "Carbohydrate Polymers", 2021),  # 10
    pm("35460750", "Polysaccharide from Agrocybe cylindracea prevents diet-induced obesity through inhibiting inflammation mediated by gut microbiota and associated metabolites (초록)", "International Journal of Biological Macromolecules", 2022),  # 11
    pm("37567726", "Agrocybe cylindracea fucoglucogalactan induced lysosome-mediated apoptosis of colorectal cancer cell through H3K27ac-regulated cathepsin D (초록)", "Carbohydrate Polymers", 2023),  # 12
    pm("36496591", "Anti-Aging Effect of Agrocybe aegerita Polysaccharide through Regulation of Oxidative Stress and Gut Microbiota (초록)", "Foods", 2022),  # 13
    pm("25117221", "Fungal lectins: a growing family (초록)", "Methods in Molecular Biology", 2014),  # 14
    pm("33473982", "The complete mitochondrial genome of the Agrocybe aegerita, an edible mushroom (초록)", "Mitochondrial DNA Part B", 2017),  # 15
    pm("37831510", "Hydrophilic Metabolite Composition of Fruiting Bodies and Mycelia of Edible Mushroom Species (Agaricomycetes) (초록)", "International Journal of Medicinal Mushrooms", 2023),  # 16
    pm("39997426", "The Influence of the Divergent Substrate on Physicochemical Properties and Metabolite Profiling of Agrocybe cylindracea Cultivation (PMC11856532 전문)", "Journal of Fungi", 2025),  # 17
    pm("32045347", "Volatilomes of Cyclocybe aegerita during different stages of monokaryotic and dikaryotic fruiting (초록)", "Biological Chemistry", 2020),  # 18
    pm("39541680", "Formation of key aroma compounds in Agrocybe aegerita during hot air drying: Amino acids and reducing sugars identified as flavor precursors (초록)", "Food Chemistry", 2025),  # 19
    pm("38833867", "Quantification- and structural-taste intensity of umami peptides from Agrocybe aegerita through quantitative structure-activity relationship (초록)", "Food Chemistry", 2024),  # 20
    pm("26002742", "Fungal unspecific peroxygenases: heme-thiolate proteins that combine peroxidase and cytochrome P450 properties (초록)", "Advances in Experimental Medicine and Biology", 2015),  # 21
    pm("32392710", "Elemental Content in Pleurotus ostreatus and Cyclocybe cylindracea Mushrooms: Correlations with Concentrations in Cultivation Substrates and Effects on the Production Process (PMC7249068 전문)", "Molecules", 2020),  # 22
    pm("32916827", "Chemical Characterization, Antioxidant, Enzyme Inhibition and Antimutagenic Properties of Eight Mushroom Species: A Comparative Study (PMC7559241 전문)", "Journal of Fungi", 2020),  # 23
    pm("39380157", "Cylindracin, a Cys-rich protein expressed in the fruiting body of Cyclocybe cylindracea, inhibits growth of filamentous fungi but not yeasts or bacteria (초록)", "FEBS Open Bio", 2024),  # 24
    pm("39330362", "Telomere-to-Telomere Haplotype-Resolved Genomes of Agrocybe chaxingu Reveals Unique Genetic Features and Developmental Insights (PMC11433599 전문)", "Journal of Fungi", 2024),  # 25
    pm("33947322", "Transcriptome of different fruiting stages in the cultivated mushroom Cyclocybe aegerita suggests a complex regulation of fruiting and reveals enzymes putatively involved in fungal oxylipin biosynthesis (초록)", "BMC Genomics", 2021),  # 26
    {"title": "볏짚버섯속 ASI1 9003(버들송이)과 ASI1 9016(차신고)의 배양 및 재배적 특성 (한국버섯학회지, 2008) — WebSearch 요약으로만 확인, 원문 미열람",
     "url": "https://koreascience.kr/article/JAKO200814364646160.page", "publisher": "한국버섯학회", "accessed": ACC},  # 27
    {"title": "Methods of Agrocybe cylindracea simultaneous cultivation for small scale bottle cultivation farmers of Pleurotus eryngii (한국버섯학회지, 2011) — WebSearch 요약으로만 확인, 원문 미열람",
     "url": "https://koreascience.kr/article/JAKO201114364645189.page", "publisher": "한국버섯학회", "accessed": ACC},  # 28
    pm("30597318", "Subcellular distribution, chemical forms and physiological responses involved in cadmium tolerance and detoxification in Agrocybe aegerita (초록)", "Ecotoxicology and Environmental Safety", 2019),  # 29
    pm("35121327", "Characterization of cheesy odor formed during fermentation of soy drink with Agrocybe aegerita (초록)", "Food Chemistry", 2022),  # 30
    pm("27532123", "Optimization of Mycelia Selenium Polysaccharide Extraction from Agrocybe cylindracea SL-02 and Assessment of their Antioxidant and Anti-Ageing Activities (초록)", "PLoS ONE", 2016),  # 31
    pm("31676068", "Critical role of IL-1β in the pathogenesis of Agrocybe aegerita galectin-induced liver injury through recruiting T cell to liver (초록)", "Biochemical and Biophysical Research Communications", 2019),  # 32
]
for i, s in enumerate(S, 1):
    s["n"] = i
sources = [{"n": s["n"], "title": s["title"], "url": s["url"], "publisher": s["publisher"], "accessed": s["accessed"]} for s in S]

sections = [
    {"key": "overview", "title": "한눈에 보기", "body":
     "버들송이(Agrocybe cylindracea)는 주로 활엽수의 죽은 나무를 분해하며 자라는 담자균류 식용버섯으로, 영어로는 black poplar mushroom이라 부르고 이탈리아에서는 pioppino로 알려져 있다[2, 7]. "
     "식품의약품안전처 「식품원료 목록」에는 원료명 '버들송이', 학명 Agrocybe cylindracea (DC. ex Fr.) Maire로 올라 있고, 상태는 '사용가능', 사용 조건은 '사용가능부위 : 자실체'이다[1]. "
     "따라서 일반 식품의 원료로는 자실체(버섯 몸체)를 쓸 수 있다[1]. "
     "건강기능식품 고시형 원료의 원재료 목록에는 없어, 고시된 지표성분과 기준은 확인하지 못함.\n\n"
     "논문에서는 Agrocybe aegerita, Cyclocybe cylindracea, Cyclocybe aegerita 같은 이름이 함께 쓰이며, 2014년 독성 연구도 A. aegerita가 A. cylindracea로도 알려져 있다고 적었다[2, 6]. "
     "이 문서는 이 이름들로 보고된 자료를 같은 종으로 다루되, 같은 속의 다른 식품원료인 볏짚버섯·이끼볏짚버섯·황토볏짚버섯 자료는 섞지 않는다[1]. "
     "연구는 자실체 다당체, 맛 성분(유리아미노산·5′-뉴클레오타이드), 향기 성분, 그리고 렉틴·리보톡신 같은 방어 단백질에 모여 있다[4, 7, 10, 18]. "
     "생물학 연구에서는 자실체 형성 과정을 연구하는 모델 버섯이자, 2004년 처음 보고된 비특이적 퍼옥시제네이스(UPO) 효소의 원천으로도 알려져 있다[2, 21]."},
    {"key": "history", "title": "이름의 역사", "body":
     "이 버섯의 학명에는 두 계보가 있다[2]. "
     "A. cylindracea는 1815년 De Candolle의 기재에, A. aegerita는 1837년 Brigantì의 기재에 바탕을 두며, 2020년 다유전자 계통 연구는 Index Fungorum에서 두 이름이 모두 유효하게 올라 있고 둘이 같은 종인지는 기준표본 연구로 따로 가려야 한다고 적었다[2]. "
     "리보솜 RNA 유전자 서열 분석에서 이 버섯은 볏짚버섯속(Agrocybe)의 기준종보다 Tubariaceae 쪽 버섯에 가깝게 나와, 부활한 속 Cyclocybe로 옮겨졌다[2]. "
     "그 결과 유럽 쪽 이름은 Cyclocybe aegerita (V. Brig.) Vizzini가 되었으나, 식약처 목록은 지금도 Agrocybe cylindracea (DC. ex Fr.) Maire라는 이름을 쓴다[1, 2].\n\n"
     "이탈리아에서는 '피오피노(pioppino)'라는 이름으로 알려져 있다[7]. "
     "국내 학회지 논문은 상품명 '버들송이'와 함께 '버들볏짚버섯'이라는 이름을 소개하고 일본 이름을 '야나기마쓰타케'로 적었다고 하나, 이 내용은 원문을 열지 못하고 WebSearch 요약으로만 확인했다[27]. "
     "2004년 이 버섯에서 처음 보고된 분비 효소는 과산화수소로 다양한 유기물에 산소 원자를 붙이는 새 효소군으로 밝혀져 '비특이적 퍼옥시제네이스(UPO, EC 1.11.2.1)'로 분류되었다[21]. "
     "2014년에는 이 버섯의 물 추출물에서 간 독성을 일으키는 렉틴(AAL)이 보고되어, 식용버섯의 안전성 평가가 필요하다는 논의가 나왔다[6]."},
    {"key": "biology", "title": "균학적 특징", "body":
     "버들송이는 활엽수의 죽은 나무를 주로 분해하며 중간 정도의 백색부후를 일으키는 주름버섯목 버섯이다[2]. "
     "재배 버섯은 한 배지에서 여러 차례 연이어 자실체를 내며, 한천 배지에서도 자실체를 만들 수 있어 자실체 형성 연구의 모델로 쓰인다[2]. "
     "중국 푸젠성 우이산의 야생 균주에서 선발한 AC9 균주의 유전체에는 탄수화물 분해 관련 효소 유전자 439개와 리그닌 분해에 관여하는 퍼옥시데이스(AA2) 5개(망가니즈 퍼옥시데이스 4개)가 있어, 셀룰로스·헤미셀룰로스·리그닌을 모두 분해하는 능력을 보여 준다[3]. "
     "짝짓기 방식은 두 개의 짝짓기형 유전자좌로 정해지는 4극성 이형접합성이며, 짝짓기형을 바꾸는 2차 동형접합성 기작도 있을 것으로 분석되었다[3].\n\n"
     "유럽 균주 AAE-3의 자실체 발달 단계별 휘발성 성분을 보면, 초기에는 1-옥텐-3-올 같은 알코올·케톤이, 포자를 퍼뜨리는 시기에는 Δ6-프로토일루덴 같은 세스퀴테르펜이 주를 이룬다[18]. "
     "어린 자실체의 갓 표면 다당층에는 실모양 곰팡이의 생장을 막는 시스테인이 풍부한 단백질 '실린드라신(cylindracin)'이 분비된다[24]. "
     "자실체에는 리보솜 RNA를 자르는 리보톡신 유사 단백질 '아게리틴(Ageritin)'이 100 g당 2.5 mg 넘게 들어 있으며, 항진균·살충 작용으로 보아 방어 기능을 하는 것으로 추정된다[7]."},
    {"key": "related_species", "title": "가까운 종과 혼동", "body":
     "식약처 「식품원료 목록」에는 같은 볏짚버섯속의 볏짚버섯(Agrocybe praecox), 이끼볏짚버섯(Agrocybe paludosa), 황토볏짚버섯(Agrocybe semiorbicularis)이 각각 따로 올라 있으며 모두 자실체만 쓸 수 있다[1]. "
     "이들은 버들송이와 다른 원료이므로 이 문서의 성분·안전성 자료와 섞지 않는다[1].\n\n"
     "2020년 네 유전자 표지(ITS·LSU·tef1-α·rpb2)를 쓴 계통 분석에서 넓은 뜻의 '아게리타' 버섯은 유럽 계통과 아시아 계통의 두 무리로 뚜렷이 갈라졌다[2]. "
     "아시아 계통은 여러 종을 포함할 수 있는 종 복합체로 잠정 구분되었고 뉴질랜드의 태평양 종과 자매 관계를 이루었으며, 중국에서 기재된 A. chaxingu는 오히려 유럽 계통과 가깝게 묶였다[2]. "
     "같은 조건에서 키웠을 때 아시아 계통 균주는 갓이 크고 대가 긴 자실체를, 유럽 계통 균주는 더 작고 많은 자실체를 내는 경향이 있었다[2]. "
     "중국에서 널리 재배되는 A. chaxingu는 아게리타 종 복합체에 속하는 가까운 종으로, 2022년 중국 생산량이 882,300톤이었다는 보고가 있으나 이는 A. chaxingu의 값이어서 버들송이 통계로 쓰지 않는다[25]. "
     "유전체 비교에서 버들송이는 독버섯과 염기서열 배열이 많이 겹치지만, 그 독버섯이 가진 α-아마니틴 독소 유전자는 버들송이 유전체에서 찾을 수 없었다[3]."},
    {"key": "cultivation", "title": "재배와 생산", "body":
     "중국에서 쓰는 AC9 균주는 1999년 푸젠성 우이산의 썩은 나무뿌리에서 채집한 야생 균주를 여러 해 선발한 것으로, 생물학적 효율(배지 건물 대비 생버섯 무게)이 75%에 이른다[3]. "
     "재배 배지로는 목화씨 껍질, 밀짚, 톱밥이 쓰인다[3]. "
     "2025년 중국 연구에서 목화씨 껍질 78%에 밀기울 20%·석회 2%를 섞은 배지의 생물학적 효율은 35.8%로, 거대 쥔차오 풀 혼합 배지(31.5%)와 버린 찻잎·톱밥 배지(28.7%)보다 높았다[17]. "
     "같은 논문은 장시성 리촨현 한 곳에서만 해마다 생버섯 약 1만 톤이 생산된다고 적었다[17]. "
     "농약 잔류 조사는 푸젠성과 장시성을 주산지로 소개했다[8]. "
     "2026년 연구에 따르면 시장과 재배는 갈색 계통이 주도하고, 흰색 계통은 2022년에 새 품종으로 인정되어 최근에야 산업 재배가 시작되었다[4]. "
     "이 연구는 균사를 20–22 ℃에서 배양한 뒤 25 ℃ 발이실로 옮겨 재배했다[4].\n\n"
     "국내 학회지에는 850 mL 병재배에서 버들송이 균주의 병당 수량이 114 g이었다는 보고와, 미송 톱밥 75%·밀기울 25%·수분 70% 배지를 고른 보고가 있으나 원문을 열지 못하고 WebSearch 요약으로만 확인했다[27, 28]. "
     "국내 생산량·재배 면적 통계(통계청·농림축산식품부 특용작물 생산실적)에서 버들송이 항목은 확인하지 못함."},
    {"key": "processing", "title": "가공과 이용", "body":
     "중국 산지에서는 주로 생버섯으로 팔리거나 말린 제품으로 가공되어 대도시로 유통된다[17]. 그대로 요리해 먹을 뿐 아니라 버섯 소스와 즉석 수프 베이스 같은 조미 제품에도 널리 쓰인다[4]. "
     "열풍 건조하면 날버섯 냄새와 흙냄새가 줄고 고소한 향·구운 향·고기 향이 늘며, 메싸이오닌과 리보스의 마이야르 반응이 다이메틸 트라이설파이드와 3-메틸싸이오프로판알을 만드는 주된 경로로 확인되었다[19]. "
     "감칠맛 펩타이드 11종은 5 mg/mL에서 MSG 4.457–5.240 mg/mL 수준의 감칠맛을 냈고, pH 6–7에서 가장 강했다[20]. "
     "두유를 이 버섯 균사로 발효하면 짧은사슬 지방산 때문에 파르메산 치즈와 비슷한 향이 생겨, 식물성 치즈 향료 소재로 연구되었다[30].\n\n"
     "자실체 알칼리 추출 다당에서는 α-(1→6)-갈락토스 주사슬의 푸코글루코갈락탄과 β-(1→6)-글루칸 분획이 분리되었다[10]. "
     "이 푸코글루코갈락탄은 대장암 세포(HCT-116)에서 24시간 IC50 490 μg/mL로 증식을 억제했고, 다당은 고지방식 생쥐의 체중 증가를 줄였다는 동물·세포 실험이 있다[11, 12]. "
     "다당체는 노화 모델 동물에서 항산화 효소 활성을 높였고, 셀레늄을 넣어 키운 균사체 다당도 연구되었다[13, 31]. "
     "사람 대상 임상시험과 식약처 「식품 등의 생산실적」의 버들송이 품목은 확인하지 못함."},
    {"key": "genetics", "title": "유전체와 유전 다양성", "body":
     "2020년 발표된 AC9 균주의 유전체 초안은 56.5 Mb, 3,790개 스캐폴드로 이루어지며 단백질 유전자 15,384개가 예측되었다[3]. "
     "이형접합도가 높아 단일염기 변이 등 871,977개 변이가 확인되었고, 반복서열은 유전체의 12.54%였다[3]. "
     "2차 대사 유전자 무리는 모두 28개로, 테르펜 합성 무리 15개와 인돌 생합성 관련 무리 2개가 포함되었다[3]. "
     "갓에서는 불포화지방산·N-글리칸 합성이, 대에서는 트레할로스·글리코젠 같은 저장 탄수화물 합성이 더 활발했다[3].\n\n"
     "미토콘드리아 유전체는 116,329 bp, GC 27.6%로 단백질 유전자 17개, 리보솜 단백질 유전자 2개, rRNA 유전자 2개, tRNA 유전자 32개를 가진다[15]. "
     "유럽 균주 AAE-3의 유전체는 2018년에 공개되었고, 이를 바탕으로 유전자 기능 연구 도구가 마련되었다[2, 25]. "
     "자실체 발달 7단계의 전사체 분석은 버섯 특유의 C8 향기 성분을 만드는 리폭시제네이스·다이옥시제네이스 같은 효소 후보를 찾아냈다[26]. "
     "다유전자 계통 분석은 유럽과 아시아 균주가 서로 다른 계통임을 보여, 육종에 쓸 균주의 출처를 따로 기록할 필요가 있음을 시사한다[2]."},
    {"key": "safety", "title": "안전성", "body":
     "식약처 「식품원료 목록」에서 버들송이는 '사용가능' 원료이며 쓸 수 있는 부위는 자실체이다[1]. "
     "식약처 등 국내 공공기관의 버들송이 알레르기·잔류·독성 정보는 확인하지 못함.\n\n"
     "2014년 중국 연구에서 물 추출물은 생쥐에서 반수치사량 8.77 g/kg을 보였고, 체중 1 kg당 25 mg과 250 mg을 6일 동안 주었을 때 강한 간 독성이 관찰되었다[6]. "
     "원인 성분은 렉틴 AAL로 확인되었으며, 이 렉틴은 소화효소로 잘 분해되지 않았다[6]. "
     "같은 계열 갈렉틴(AAGL)은 생쥐 정맥 주사로 급성 간 손상 모델을 만드는 데 쓰였다[32]. "
     "자실체에는 리보톡신 유사 단백질 아게리틴이 100 g당 2.5 mg 넘게 들어 있다[7].\n\n"
     "2021–2023년 푸젠·장시산 건조 버섯 174점에서 28종의 농약이 0.005–3.610 mg/kg 검출되었고, 54.0%가 중국 채소 기준 잔류허용기준을 넘었으며 대부분 클로르피리포스 때문이었다[8]. "
     "다만 만성·급성·누적 노출 위험은 허용 범위로 평가되었다[8]. "
     "튀르키예 앙카라의 야생 시료는 조사한 금속 모두에서 기준 용량 이내였고, 재배 시료 연구는 버들송이·느타리 섭취로 카드뮴 섭취가 내용섭취량의 최대 27–31%에 이를 수 있다고 계산했다[9, 22]. "
     "카드뮴을 넣은 배지에서는 대보다 갓에 카드뮴이 더 많이 쌓였다[29]. "
     "메탄올 추출물은 에임스 시험에서 돌연변이를 일으키지 않았다[23]."},
]

compounds = [
    {"name": "L-Glutamine", "name_ko": "유리아미노산(글루타민 등)", "class": "아미노산", "role": "nutrient", "part": "자실체(중국 재배 흰색 계통 BC·갈색 계통 CS, 분말)",
     "content_text": "총 유리아미노산 BC 15.18 ± 0.18 mg/g, CS 10.78 ± 0.19 mg/g(20종 중 18종 검출, 시스테인·아이소류신 불검출)[4]",
     "activity_ko": "되첨가 실험에서 글루타민·트립토판이 감칠맛에, 아스파르트산·글루타민·트립토판·라이신이 신맛에 기여[4]", "source": [4]},
    {"name": "Cytidine 5'-monophosphate", "name_ko": "5′-뉴클레오타이드(5′-CMP 등)", "class": "뉴클레오타이드", "role": "nutrient", "part": "자실체(분말)",
     "content_text": "총 5′-뉴클레오타이드 BC 1.39 ± 0.04 mg/g, CS 0.93 ± 0.05 mg/g(6종 중 5종 검출, 5′-IMP 불검출); 등가 감칠맛 농도 BC 7.5681 ± 0.1833 g MSG/100 g[4]",
     "activity_ko": "5′-CMP는 신맛에 기여, 뉴클레오타이드가 아미노산과 함께 감칠맛을 상승[4]", "source": [4]},
    {"name": "Fucoglucogalactan", "name_ko": "푸코글루코갈락탄(알칼리 추출 다당 JACP-30·ACP)", "class": "다당체", "role": "bioactive", "part": "자실체",
     "content_text": "α-(1→6)-갈락토피라노실 주사슬의 푸코글루코갈락탄 분획으로 동정(함량 수치는 초록에 없음)[10]",
     "activity_ko": "대장암 세포 HCT-116 증식 억제 IC50 490 μg/mL(24시간), 리소좀 매개 세포사멸 유도(세포 실험)[12]", "source": [10, 12]},
    {"name": "beta-1,6-Glucan", "name_ko": "β-(1→6)-글루칸(JACP-50p·JACP-80r·JACP-80)", "class": "다당체", "role": "bioactive", "part": "자실체",
     "content_text": "β-(1→6) 주사슬에 O-3 위치 곁사슬, JACP-80은 β-(1→6):β-(1→3,6) 결합 4:1[10]",
     "activity_ko": "다당(ACP) 9주 투여로 고지방식 생쥐의 체중·지방 축적·인슐린 저항성 감소(동물 실험)[11]", "source": [10, 11]},
    {"name": "Brunnein B", "name_ko": "브루네인 B(C1-S 부분입체이성질체, β-카볼린 알칼로이드)", "class": "β-카볼린 알칼로이드", "role": "marker", "part": "동결건조 자실체 및 부위별",
     "content_text": "자실체 36.2 ± 2.8 ng/g DW, 껍질 94.7 ± 1.9, 갓 안쪽 90.5 ± 1.3, 주름 71.5 ± 0.6, 대 162.2 ± 1.7 ng/g DW(HPLC-MS)[5]",
     "activity_ko": "라디칼 소거 EC50 119.1 ± 1.2 μg/mL, 이 종에서 처음 보고된 화합물[5]", "source": [5]},
    {"name": "1-Octen-3-one", "name_ko": "1-옥텐-3-온", "class": "C8 휘발성 케톤", "role": "marker", "part": "자실체(분말 헤드스페이스)",
     "content_text": "BC·CS 모두에서 상대 향기 활성값(ROAV)이 가장 큰 향기 성분(정규화 상대 함량)[4]",
     "activity_ko": "버섯 특유의 향을 내는 핵심 향기 성분[4]", "source": [4]},
    {"name": "1-Octen-3-ol", "name_ko": "1-옥텐-3-올", "class": "C8 휘발성 알코올", "role": "bioactive", "part": "배양 중 헤드스페이스·자실체",
     "content_text": "자실체 발달 초기 헤드스페이스의 주성분(2-메틸뷰탄-1-올·사이클로펜탄온과 함께)[18]; 갈색 계통 CS의 주요 향기 기여 성분[4]",
     "activity_ko": "버섯 향·풀 향 기여[4]", "source": [4, 18]},
    {"name": "Delta6-protoilludene", "name_ko": "Δ6-프로토일루덴(세스퀴테르펜)", "class": "세스퀴테르펜", "role": "bioactive", "part": "포자 형성기 배양 헤드스페이스",
     "content_text": "이핵체 AAE-3 포자 형성기 헤드스페이스의 우세 성분(α-큐베벤·δ-카디넨과 함께)[18]",
     "activity_ko": "포자 형성기 휘발성 프로필의 표지 성분[18]", "source": [18]},
    {"name": "Dimethyl trisulfide", "name_ko": "다이메틸 트라이설파이드", "class": "황 함유 휘발성 성분", "role": "bioactive", "part": "열풍 건조 자실체",
     "content_text": "열풍 건조 중 메싸이오닌·리보스 마이야르 반응으로 생성, 함량 수치는 초록에 없음[19]",
     "activity_ko": "건조 버들송이의 '고기 향' 핵심 성분[19]", "source": [19]},
    {"name": "Trehalose", "name_ko": "트레할로스", "class": "이당류", "role": "nutrient", "part": "자실체",
     "content_text": "1H NMR로 극성 대사체 54종을 동정했고, 대부분 시료에서 트레할로스가 주된 당(버들송이 균사체만 포도당이 주된 당)[16]",
     "activity_ko": "자실체의 주요 저장 당[16]", "source": [16]},
    {"name": "Ergothioneine", "name_ko": "에르고티오네인", "class": "황 함유 아미노산 유도체", "role": "bioactive", "part": "자실체",
     "content_text": "대사체 분석에서 검출, 버린 찻잎·톱밥 배지에서 목화씨 껍질 배지보다 많음(절대 함량 확인하지 못함)[17]",
     "activity_ko": "배지에 따라 함량이 달라지는 대사체로 단백질·식이섬유 함량과 양의 상관[17]", "source": [17]},
    {"name": "Asp-Asp-Leu", "name_ko": "감칠맛 펩타이드(DDL 등 11종)", "class": "펩타이드", "role": "bioactive", "part": "자실체",
     "content_text": "EV·EG·EY·ENG·ECG·DEL·DDL·PEG·PEEL·DGPL·EDCS 11종, 5 mg/mL에서 감칠맛 MSG 4.457–5.240 mg/mL 상당(DDL 최고)[20]",
     "activity_ko": "버들송이 감칠맛의 주요 성분, EY·ENG는 70 ℃에서도 감칠맛 유지[20]", "source": [20]},
    {"name": "Ageritin", "name_ko": "아게리틴(리보톡신 유사 단백질)", "class": "단백질(리보뉴클레이스)", "role": "bioactive", "part": "자실체",
     "content_text": "자실체 100 g당 2.5 mg 넘게 들어 있음[7]",
     "activity_ko": "rRNA의 α-사르신 고리를 잘라 단백질 합성 억제, 항진균·살충 활성(방어 단백질로 추정)[7]", "source": [7]},
    {"name": "Agrocybe aegerita lectin", "name_ko": "버들송이 렉틴(AAL, 갈렉틴)", "class": "단백질(렉틴)", "role": "bioactive", "part": "자실체",
     "content_text": "물 추출물의 단백 분획에서 LC-MS/MS로 간 독성 원인 성분으로 동정(함량 수치는 초록에 없음)[6]",
     "activity_ko": "생쥐 간 독성, 소화효소에 잘 분해되지 않음[6]; 시알산 특이 렉틴으로 당사슬 연구 도구로 쓰임[14]", "source": [6, 14]},
]

assays = [
    {"role": "literature", "compound": "Free amino acids (CNBF derivatives)", "compound_ko": "유리아미노산 20종(CNBF 유도체)",
     "part": "자실체(흰색 계통 BC '바이차 1호', 갈색 계통 CS '구차 2호', -80 ℃ 보관 후 분말)",
     "content": "총 유리아미노산 BC 15.18 ± 0.18 mg/g, CS 10.78 ± 0.19 mg/g[4]",
     "method": "HPLC-DAD(CNBF 사전 유도체화)",
     "conditions": {"instrument": "Agilent 1260 Infinity, DAD", "column": "Welch Ultimate Amino Acid, 4.6 × 250 mm, 5 μm",
                    "mobile_phase": "A: 아세트산나트륨–트라이에틸아민 용액(pH 6.20), B: 64% 아세토나이트릴",
                    "gradient": "0–11분 B 35→46%, 11–30분 46→80%, 30–35분 80→100%, 35–40분 100%, 40–42분 100→35%, 42–47분 35%",
                    "flow": "0.8 mL/min", "temp": "40 ℃", "detection": "254 nm", "injection": "10 μL",
                    "sample_prep": "분말 2.000 g에 붕산 완충액(pH 9.0) 5 mL, 4 ℃ 하룻밤 → 초음파 1시간 → 10,000 r/min 15분 원심 → 10 mL 정용; CNBF 용액 600 μL 넣고 붕산 완충액으로 2 mL, 60 ℃ 30분 유도체화 → 0.22 μm 여과",
                    "standard": "아미노산 20종 표준품(HPLC ≥98%), 각 1 mg/mL 혼합 희석 검량선",
                    "linearity": "", "lod": "", "loq": "", "recovery": ""},
     "rationale": "유리아미노산은 버섯 맛의 중심 성분으로, 이 연구는 맛 활성값과 전자혀 되첨가 실험으로 글루타민·트립토판이 감칠맛에 기여함을 보였다[4]. 검출·정량한계와 회수율은 원문에 없다[4].",
     "source": [4], "url": "https://pubmed.ncbi.nlm.nih.gov/42894792/", "source_kind": "paper"},
    {"role": "literature", "compound": "5'-Nucleotides", "compound_ko": "5′-뉴클레오타이드 6종(5′-CMP·5′-AMP·5′-UMP·5′-GMP·5′-XMP·5′-IMP)",
     "part": "자실체(BC·CS 분말)",
     "content": "총 5′-뉴클레오타이드 BC 1.39 ± 0.04 mg/g, CS 0.93 ± 0.05 mg/g, 5′-IMP 불검출[4]",
     "method": "HPLC-DAD",
     "conditions": {"instrument": "Agilent 1260 Infinity, DAD", "column": "Eclipse XDB-C18, 4.6 × 250 mm, 5 μm",
                    "mobile_phase": "A: 메탄올, B: 10 mM KH2PO4",
                    "gradient": "0–3분 B 95→96%, 3–8분 96→97%, 8–15분 97→100%, 15–18분 100→95%, 18–23분 95%",
                    "flow": "1 mL/min", "temp": "30 ℃", "detection": "254 nm", "injection": "10 μL",
                    "sample_prep": "분말 2.000 g에 초순수 5 mL, 100 ℃ 10분 끓임 → 10,000 r/min 10분 원심 → 10 mL 정용 → 0.22 μm 여과",
                    "standard": "5′-뉴클레오타이드 6종 표준품(HPLC ≥98%), 각 1 mg/mL 혼합 희석 검량선",
                    "linearity": "", "lod": "", "loq": "", "recovery": ""},
     "rationale": "5′-뉴클레오타이드는 감칠맛 아미노산과 상승 작용을 해 등가 감칠맛 농도(EUC) 계산에 쓰인다[4]. 검출·정량한계와 회수율은 원문에 없다[4].",
     "source": [4], "url": "https://pubmed.ncbi.nlm.nih.gov/42894792/", "source_kind": "paper"},
    {"role": "literature", "compound": "Brunnein B (C1-S diastereomer)", "compound_ko": "브루네인 B(β-카볼린 알칼로이드)",
     "part": "재배 자실체(동결건조, 메탄올 추출) 및 껍질·갓 안쪽·주름·대",
     "content": "자실체 36.2 ± 2.8 ng/g DW, 대 162.2 ± 1.7 ng/g DW[5]",
     "method": "HPLC-MS",
     "conditions": {"instrument": "", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "",
                    "injection": "", "sample_prep": "", "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""},
     "rationale": "라디칼 소거 활성을 따라 분리한 이 종 특유의 새 β-카볼린 알칼로이드로, 부위별 함량이 정량되어 있다[5]. 전문 확인 못함: 초록만 보아 분석 조건 칸은 비워 둔다[5].",
     "source": [5], "url": "https://pubmed.ncbi.nlm.nih.gov/31150766/", "source_kind": "paper"},
]

d = {
    "slug": "agrocybe-cylindracea", "name_ko": "버들송이", "name_en": "Black poplar mushroom (poplar mushroom)",
    "scientific_name": "Agrocybe cylindracea (DC. ex Fr.) Maire",
    "aliases": ["버들볏짚버섯", "Agrocybe aegerita", "Cyclocybe cylindracea", "Cyclocybe aegerita", "Poplar mushroom", "Pioppino"],
    "sections": sections, "compounds": compounds, "markers": [], "assays": assays, "nutrients": [],
    "production": [], "world": [], "gi": [], "orgs": [], "sources": sources,
}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in sections:
    print(s["key"], len(s["body"]))
