import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
A = "2026-11-02"
def pm(n, title, pmid, journal, pmc=None):
    url = f"https://pmc.ncbi.nlm.nih.gov/articles/{pmc}/" if pmc else f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
    pub = f"{journal} ({'PubMed Central' if pmc else 'PubMed'})"
    return {"n": n, "title": title, "url": url, "publisher": pub, "accessed": A}
S = [
 {"n": 1, "title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 신갈나무(Quercus mongolica Fisch. ex Ledeb.)", "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
 pm(2, "A chromosome-scale genome assembly of the Mongolian oak (Quercus mongolica). Mol Ecol Resour. 2022", "35377556", "Molecular Ecology Resources"),
 pm(3, "Characterization of a Major Allergen from Mongolian Oak, Quercus mongolica, a Dominant Species of Oak in Korea. Int Arch Allergy Immunol. 2017", "29065418", "International Archives of Allergy and Immunology"),
 pm(4, "Neglected but Clinically Relevant Allergens in Korea. Curr Allergy Asthma Rep. 2024", "38980649", "Current Allergy and Asthma Reports"),
 pm(5, "Rapid migration of Mongolian oak into the southern Asian boreal forest. Glob Chang Biol. 2023", "37916481", "Global Change Biology"),
 pm(6, "Dispersal as a result of asymmetrical hybridization between two closely related oak species in China. Mol Phylogenet Evol. 2020", "32956798", "Molecular Phylogenetics and Evolution"),
 pm(7, "A comparison of reproductive isolation between two closely related oak species in zones of recent and ancient secondary contact. BMC Evol Biol. 2019", "30841907", "BMC Evolutionary Biology", "PMC6404273"),
 pm(8, "Different population size change and migration histories created genetic diversity of three oaks in Tokai region, central Japan. J Plant Res. 2021", "34155542", "Journal of Plant Research"),
 pm(9, "Role of tannin-binding salivary proteins and tannase-producing bacteria in the acclimation of the Japanese wood mouse to acorn tannins. J Chem Ecol. 2006 (초록만 확인)", "16770711", "Journal of Chemical Ecology"),
 pm(10, "Effects of tannins on population dynamics of sympatric seed-eating rodents: the potential role of gut tannin-degrading bacteria. Oecologia. 2018 (초록만 확인)", "29736862", "Oecologia"),
 pm(11, "Selective predation on acorn weevils by seed-caching Siberian chipmunk Tamias sibiricus in a tripartite interaction. Oecologia. 2018", "29777342", "Oecologia"),
 pm(12, "Incorporating cache management behavior into seed dispersal: the effect of pericarp removal on acorn germination. PLoS One. 2014", "24647670", "PLoS One", "PMC3960254"),
 pm(13, "Acorns containing deeper plumule survive better: how white oaks counter embryo excision by rodents. Ecol Evol. 2013", "24455161", "Ecology and Evolution", "PMC3894888"),
 pm(14, "Effects of relative abundance of Quercus mongolica acorns on five tree species seed dispersal in Xiaoxing'an Mountains, Northeast China. Ying Yong Sheng Tai Xue Bao. 2013 (초록만 확인)", "24066536", "Ying Yong Sheng Tai Xue Bao"),
 pm(15, "An intercontinental comparison of insect seed predation between introduced and native oaks. Integr Zool. 2021", "34796655", "Integrative Zoology"),
 pm(16, "Retention of cotyledons is crucial for resprouting of clipped oak seedlings. Sci Rep. 2014", "24888417", "Scientific Reports", "PMC4042119"),
 pm(17, "Catechin, rutin and quercetin in Quercus mongolica Fisch leaves exert inhibitory effects on multiple cancer cells. J Food Biochem. 2022 (초록만 확인)", "36351050", "Journal of Food Biochemistry"),
 pm(18, "Inhibition of matrix metalloproteinase-1 and type-I procollagen expression by phenolic compounds isolated from the leaves of Quercus mongolica in ultraviolet-irradiated human fibroblast cells. Arch Pharm Res. 2015", "24627338", "Archives of Pharmacal Research"),
 pm(19, "Anti-Inflammatory Effects of Phenolic Compounds Isolated from Quercus mongolica Fisch. ex Ledeb. on UVB-Irradiated Human Skin Cells. Molecules. 2019", "31454971", "Molecules", "PMC6749265"),
 pm(20, "Anti-Acne Vulgaris Effects of Pedunculagin from the Leaves of Quercus mongolica by Anti-Inflammatory Activity and 5α-Reductase Inhibition. Molecules. 2020", "32380665", "Molecules", "PMC7249114"),
 pm(21, "[Studies on the chemical constituents of Quercus mongolica]. Zhong Yao Cai. 1998 (초록만 확인)", "12567947", "Zhong Yao Cai"),
 pm(22, "[Chemical constituents of Quercus mongolica Fisch]. Zhongguo Zhong Yao Za Zhi. 1998 (초록만 확인)", "11599387", "Zhongguo Zhong Yao Za Zhi"),
 pm(23, "Polyamine derivatives from the bee pollen of Quercus mongolica with tyrosinase inhibitory activity. Bioorg Chem. 2018", "30118984", "Bioorganic Chemistry"),
 pm(24, "Antioxidant and Tyrosinase-Inhibitory Activities and Biological Bioactivities of Flavonoid Derivatives from Quercus mongolica Pollen. Molecules. 2025", "40005106", "Molecules", "PMC11858624"),
 pm(25, "Yeast Associated with the Ambrosia Beetle, Platypus koryoensis, the Pest of Oak Trees in Korea. Mycobiology. 2015", "26839506", "Mycobiology", "PMC4731651"),
 pm(26, "Male-produced aggregation pheromone blend in Platypus koryoensis. J Agric Food Chem. 2009", "19170509", "Journal of Agricultural and Food Chemistry"),
 pm(27, "Exploration and characterization of flavor compounds in Chinese whiskies: Qingke whisky and Mongolian oak barrel aging via GC × GC and multivariate analysis. Food Chem. 2025", "40318341", "Food Chemistry"),
 pm(28, "Carbon allocation to defense, storage, and growth in seedlings of two temperate broad-leaved tree species. Oecologia. 2009", "19763628", "Oecologia"),
 pm(29, "Isolation and characterization of biologically active lectin from Korean mistletoe, Viscum album var. Coloratum. Cell Mol Life Sci. 1999", "10357236", "Cellular and Molecular Life Sciences", "PMC11146893"),
 pm(30, "Integrated physiological and transcriptomic analyses reveal the molecular mechanism behind the response to cultivation in Quercus mongolica. Front Plant Sci. 2022", "36003809", "Frontiers in Plant Science", "PMC9393570"),
 pm(31, "Molecular Networking-Guided Annotation of Flavonoid Glycosides from Quercus mongolica Bee Pollen. Int J Mol Sci. 2025", "40869251", "International Journal of Molecular Sciences", "PMC12386960"),
 pm(32, "Recent demographic histories of temperate deciduous trees inferred from microsatellite markers. BMC Ecol Evol. 2021", "34006219", "BMC Ecology and Evolution", "PMC8130339"),
 pm(33, "Genome-Wide Identification and Expression Analysis of the bHLH Transcription Factor Family and Its Response to Abiotic Stress in Mongolian Oak (Quercus mongolica). Curr Issues Mol Biol. 2023", "36826020", "Current Issues in Molecular Biology", "PMC9955707"),
 pm(34, "Selection and validation of reference genes for quantitative real-time PCR of Quercus mongolica Fisch. ex Ledeb under abiotic stresses. PLoS One. 2022", "35482686", "PLoS One", "PMC9049516"),
 pm(35, "Effects of seed size and emergence time on tree seedling establishment: importance of developmental constraints. Oecologia. 2000", "28308725", "Oecologia"),
]
sections = [
 ("overview", "한눈에 보기",
  "신갈나무(Quercus mongolica Fisch. ex Ledeb.)는 참나무과(Fagaceae) 참나무속의 갈잎 큰키나무로, 영어로는 Mongolian oak라 부른다[1][2]. 동아시아 온대에 널리 자라는 백참나무(white oak) 무리의 대표 종이며, 한국 숲에서 가장 많은 참나무로 소개된다[2][3].\n\n"
  "식품의약품안전처 「식품원료 목록」에서 신갈나무는 식품에 사용할 수 있는 원료(사용가능)이고, 사용 조건은 '사용가능부위 : 열매'이다[1]. 목록의 원료명은 '신갈나무열매' 하나이며, 다른 이름으로 돌참나무·물갈나무, 학명 표기로 'Quercus mongolica Fisch. ex Ledeb. / Quercus crispula var. mandshurica Koidz.'가 함께 적혀 있다[1]. 건강기능식품 고시형 원료의 원재료로 쓰인다는 기록은 확인하지 못함.\n\n"
  "열매(도토리)는 탄닌이 많은 씨앗으로 다뤄지며, 같은 종 복합체인 일본산 Q. crispula 도토리의 탄닌은 건조 중량의 9.9%로 보고되었다[9][10]. 성분 연구는 주로 잎에서 이루어져 페둔쿨라긴 같은 엘라기탄닌과 카테킨·엘라그산이 확인되었다[17][18]. 꽃가루의 주요 알레르겐 Que m 1이 밝혀져 있다[3]."),
 ("history", "역사와 전통적 이용",
  "신갈나무는 한국·중국·몽골에서 구강·생식기·항문 점막의 염증과 피부 염증을 다스리는 전통 약재로 써 왔다고 소개된다[20]. 다른 연구진도 치질·열·장염을 덜어 주는 동양 전통 약으로 써 왔다고 적었다[19]. 이런 전통 용도를 근거로 잎 추출물과 분리 성분의 세포 실험이 이어졌다[18][19][20].\n\n"
  "도토리를 먹어 온 역사는 이 자료의 PubMed 문헌으로는 확인하지 못함. 한국에서 신갈나무 도토리만 따로 묵 등으로 가공해 먹었다는 공식 기록도 확인하지 못함. 「식품원료 목록」은 오늘날 열매만 식품 원료로 쓸 수 있게 정하고 있다[1].\n\n"
  "목재로서는 중국에서 건축·조경용 나무로 상업·생태적 가치가 크다고 소개된다[30]. 최근 중국에서는 신갈나무 목재로 만든 오크통에 위스키를 숙성해, 미국·유럽 오크통과 다른 폴리페놀과 리그닌 유래 향 성분이 들어간다는 분석이 나왔다[27]. 한국산 겨우살이 연구에서는 신갈나무에 붙어 자란 겨우살이에서 렉틴을 분리했다[29]."),
 ("biology", "식물학적 특징",
  "신갈나무는 동아시아 온대에 자생하는 백참나무 무리의 종이며, 중국 동북부와 북부의 침엽수·활엽수 혼효림을 이루는 주요 수종이다[2][34]. 대싱안링 산맥 북부에서는 지난 100년 동안 기후 온난화에 맞춰 10년에 평균 12.0 ± 1.0 km 속도로 북방림 쪽으로 퍼져 나갔다[5]. 이 속도는 이주하는 온대 나무들의 평균(10년에 4.0 ± 1.0 km)보다 훨씬 빨랐다[5].\n\n"
  "도토리는 다람쥐·쥐 같은 설치류가 먹고 땅에 묻어 퍼뜨린다[11][14]. 샤오싱안링 산림에서 바닥에 떨어진 도토리 수는 2009년 1 m²당 6.2 ± 2.1개, 2010년 26.7 ± 10.2개로 해마다 크게 달랐다[14]. 백참나무류 가운데 신갈나무 도토리는 배(씨눈)가 떡잎 속 가장 깊이 있어, 끝을 4 mm 잘라 내도 발아율이 떨어지지 않았다[13]. 줄무늬다람쥐는 껍질(과피)을 벗겨 바구미가 든 도토리를 가려 먹고 성한 도토리를 저장했다[11][12]. 한 해 자란 어린 묘목은 떡잎이 붙어 있어야 줄기를 잘린 뒤에도 다시 싹을 틔웠다[16]."),
 ("related_species", "가까운 종",
  "유전체 비교에서 신갈나무는 유럽의 Q. robur와 가장 가깝고, 두 종은 약 1,180만 년 전 공통 조상에서 갈라졌다[2]. 중국에서는 가까운 종 Q. liaotungensis와 자연 잡종을 이루며, 중국 동북부의 Q. liaotungensis 집단은 신갈나무에서 비대칭 잡종화로 생겨났다고 추정되었다[6]. 두 종의 개화기는 겹치고, 오래된 접촉 지대에서는 씨가 익는 단계의 생식 격리가 더 강했다[7].\n\n"
  "일본의 변종 Q. mongolica var. crispula와 var. mongolicoides 사이에는 갈라진 뒤에도 유전자 흐름이 이어졌다[8]. 「식품원료 목록」은 'Quercus crispula var. mandshurica Koidz.'를 신갈나무와 같은 원료의 학명으로 함께 적는다[1]. 이 이명의 현재 분류학적 지위는 이 자료에서 확인하지 못함.\n\n"
  "일본의 변종(var. grosseserrata) 어린 묘목은 같은 참나무과의 밤나무(Castanea crenata) 묘목보다 축합형 탄닌과 총페놀 농도가 높아, 방어 물질에 탄소를 더 많이 썼다[28]. 신갈나무 꽃가루 알레르겐 Que m 1은 상수리나무의 Que ac 1처럼 수입 진단 시약의 알레르겐과 교차 반응이 강하다[4]."),
 ("cultivation", "재배와 생산",
  "신갈나무는 주로 자연림에서 자라며, 도토리 결실량은 해마다 크게 달라진다[14]. 중국 동북부 산림의 10년 자료에서 신갈나무 종자 결실량은 줄무늬다람쥐 개체 수와 음의 상관을 보였다[10]. 공동 정원 시험에서 중국의 토착 참나무 도토리는 도입종 Q. rubra보다 곤충 피해율이 높았다[15].\n\n"
  "중국에서 높은 산에서 옮겨 심은 묘목이 평지에서 잘 자라지 못하고 잎이 누렇게 되는 문제가 있어, 가지치기·물주기·비료 처리를 비교한 연구가 있다[30]. 가지치기는 항산화 효소 체계를, 물주기와 비료는 가용성 당 축적을 더 잘 끌어올렸다[30]. 일본산 변종 연구에서는 큰 씨에서 나온 묘목이 키 생장과 생존에서 앞섰다[35].\n\n"
  "한국에서는 2004년부터 광릉긴나무좀(Platypus koryoensis)과 공생 곰팡이 Raffaelea quercus-mongolicae가 일으키는 참나무시들음병으로 신갈나무가 많이 죽었다[25][26]. 신갈나무 도토리만의 국내 채취량·생산량 통계는 확인하지 못함. 지리적 표시 등록과 세계 생산 통계도 확인하지 못함."),
 ("processing", "가공과 이용",
  "「식품원료 목록」에 오른 원료명은 '신갈나무열매' 하나이며, 추출물·분말 같은 가공 원료명은 올라 있지 않다[1]. 신갈나무 도토리의 떫은맛(탄닌)을 빼는 가공 방법이나 그 효과를 정량한 논문은 PubMed에서 확인하지 못함.\n\n"
  "같은 종 복합체인 일본산 Q. crispula 도토리는 탄닌이 건조 중량의 9.9%였고, 이 도토리만 먹인 생쥐는 적응 기간이 없으면 14마리 가운데 8마리가 죽었다[9]. 미리 조금씩 먹여 적응시킨 생쥐는 12마리 가운데 1마리만 죽었고, 침의 프롤린 풍부 단백질과 탄닌 분해 장내 세균이 늘었다[9]. 신갈나무 씨앗은 물개암나무(Corylus mandshurica)보다 탄닌이 많은 먹이로 분류되었고, 고탄닌 먹이는 두 설치류의 체중을 줄였다[10]. 이는 동물 실험 결과이며 사람의 섭취량 기준은 확인하지 못함.\n\n"
  "잎은 에탄올로 추출해 100 g에서 플라보노이드 5.06 g을 얻은 연구가 있다[17]. 꿀벌이 모은 신갈나무 꽃가루(비폴렌)에서는 폴리아민 유도체와 플라보노이드가 분리되었다[23][24][31]. 식약처 건강기능식품 생산실적 품목에서 신갈나무 원료는 확인하지 못함."),
 ("genetics", "유전체와 육종",
  "신갈나무의 염색체 수준 유전체는 아시아 참나무로는 처음 조립되었으며, PacBio 초안 유전체 크기는 809.84 Mb였다[2]. Hi-C로 774.59 Mb(초안의 95.65%)를 12개 유사 염색체에 배치했고, contig N50은 2.64 Mb, scaffold N50은 66.74 Mb였다[2]. 단백질 암호 유전자 36,553개가 예측되었고, 반복 서열이 유전체의 53.75%(435.34 Mb)를 차지했다[2]. 병 저항성과 관련된 NBS 유전자족은 줄어든 반면, 표피 왁스 합성에 관여하는 CER1 상동 유전자는 늘어났다[2].\n\n"
  "이 유전체를 바탕으로 bHLH 전사인자 89개가 21개 하위군으로 분류되었고, 그 가운데 12개는 염·추위·약광·가뭄에 반응했다[33]. 스트레스 조건의 정량 PCR에는 CYP18·ACT97·RPS13이 가장 안정한 기준 유전자로 꼽혔다[34]. 마이크로새틀라이트 19개를 쓴 연구는 신갈나무가 마지막 빙하 최대기 뒤 개체 수가 알맞게 늘고 안정되었다고 추정했다[32]. 도토리 품질이나 탄닌 함량을 목표로 한 육종 품종은 확인하지 못함."),
 ("safety", "안전성과 주의",
  "신갈나무는 「식품원료 목록」에서 열매에 한해 사용가능 원료이며, 잎·나무껍질 등 다른 부위는 식품 원료로 올라 있지 않다[1]. 건강기능식품 고시형 원료가 아니어서 고시된 섭취 시 주의사항은 없다[1].\n\n"
  "신갈나무 꽃가루에서 PR-10 계열 주요 알레르겐 Que m 1이 클로닝되었고, 한국 수목 꽃가루 알레르기 환자 혈청 50개 가운데 92.0%가 재조합 Que m 1에 특이 IgE를 보였다[3]. Que m 1은 자작나무 Bet v 1과 교차 반응을 보였다[3]. 꽃가루-식품 알레르기 증후군을 일으키는 국내 과일·채소 알레르겐도 더 밝혀야 한다는 지적이 있다[4]. 도토리 자체의 식품 알레르기 증례는 확인하지 못함.\n\n"
  "탄닌이 많은 도토리를 적응 없이 많이 먹인 생쥐에서 체중 감소와 높은 치사율이 나타났다[9]. 사람에서 신갈나무 도토리 섭취의 독성·잔류농약·중금속에 관한 공공기관 정보는 확인하지 못함."),
]
compounds = [
 {"name": "Tannins", "name_ko": "탄닌(도토리 총 탄닌)", "role": "marker", "part": "열매(도토리; 일본산 Q. crispula)", "content_text": "건조 중량 기준 9.9%[9]; 신갈나무 씨앗은 고탄닌 먹이로 분류[10]", "activity_ko": "적응하지 않은 생쥐에서 체중 감소·치사, 적응하면 침 프롤린 풍부 단백질과 탄닌 분해 세균 증가(동물)[9]; 설치류 체중 감소(동물)[10]", "source": [9, 10], "class": "폴리페놀(탄닌)"},
 {"name": "Pedunculagin", "name_ko": "페둔쿨라긴", "role": "bioactive", "part": "잎", "content_text": "함량 수치는 확인하지 못함; 잎 80% 아세톤 추출물에서 분리[18]", "activity_ko": "UVB 섬유아세포 MMP-1 억제·제1형 프로콜라겐 증가(세포)[18]; IL-6·IL-13·MCP-1 mRNA 억제(세포)[19]; 5α-환원효소 1형 억제(세포)[20]", "source": [18, 19, 20], "class": "엘라기탄닌"},
 {"name": "Ellagic acid", "name_ko": "엘라그산", "role": "bioactive", "part": "잎(에탄올 추출 플라보노이드 분획)", "content_text": "분획의 34.9%[17]", "activity_ko": "여러 암세포 증식 억제, 세포자멸사 외 기전 추정(세포)[17]", "source": [17], "class": "페놀산"},
 {"name": "Catechin", "name_ko": "카테킨", "role": "bioactive", "part": "잎", "content_text": "에탄올 추출 플라보노이드 분획의 18.4%[17]; (+)-카테킨 분리[18]", "activity_ko": "MCF-7 등 암세포 증식 억제·세포자멸사 유도(세포)[17]", "source": [17, 18], "class": "플라반-3-올"},
 {"name": "Kaempferol", "name_ko": "캠페롤", "role": "bioactive", "part": "잎", "content_text": "에탄올 추출 플라보노이드 분획의 20.6%[17]", "activity_ko": "잎 추출 분획의 주성분으로 확인[17]", "source": [17], "class": "플라보놀"},
 {"name": "Rutin", "name_ko": "루틴", "role": "bioactive", "part": "잎", "content_text": "에탄올 추출 플라보노이드 분획의 6.3%[17]", "activity_ko": "암세포 세포주기 정지·세포자멸사 유도(세포)[17]", "source": [17], "class": "플라보놀 배당체"},
 {"name": "Quercetin", "name_ko": "퀘르세틴", "role": "bioactive", "part": "잎", "content_text": "에탄올 추출 플라보노이드 분획의 5.1%[17]", "activity_ko": "암세포 세포주기 정지·세포자멸사 유도(세포)[17]", "source": [17], "class": "플라보놀"},
 {"name": "Epigallocatechin", "name_ko": "(-)-에피갈로카테킨", "role": "bioactive", "part": "잎", "content_text": "함량 수치는 확인하지 못함; 잎에서 분리[18]", "activity_ko": "잎 페놀 성분 6종의 하나로 MMP-1 실험에 쓰임(세포)[18]", "source": [18], "class": "플라반-3-올"},
 {"name": "Quercetin 3-O-(6''-O-galloyl)-beta-D-glucopyranoside", "name_ko": "퀘르세틴-3-O-(6″-O-갈로일)-글루코사이드", "role": "bioactive", "part": "잎", "content_text": "함량 수치는 확인하지 못함; 잎에서 분리[18]", "activity_ko": "잎 페놀 성분의 하나로 분리·동정[18]", "source": [18], "class": "플라보놀 배당체"},
 {"name": "Gallic acid", "name_ko": "갈산", "role": "bioactive", "part": "식물체(부위는 초록에 명시 없음)", "content_text": "함량 수치는 확인하지 못함; 분리·동정[21]", "activity_ko": "확인하지 못함", "source": [21], "class": "페놀산"},
 {"name": "Friedelin", "name_ko": "프리델린", "role": "bioactive", "part": "잎", "content_text": "함량 수치는 확인하지 못함; 분리·동정[21][22]", "activity_ko": "확인하지 못함", "source": [21, 22], "class": "트리테르펜"},
 {"name": "Lupeol", "name_ko": "루페올", "role": "bioactive", "part": "잎", "content_text": "함량 수치는 확인하지 못함; 분리·동정[22]", "activity_ko": "확인하지 못함", "source": [22], "class": "트리테르펜"},
 {"name": "beta-Sitosterol", "name_ko": "β-시토스테롤", "role": "bioactive", "part": "잎", "content_text": "함량 수치는 확인하지 못함; 분리·동정[21][22]", "activity_ko": "확인하지 못함", "source": [21, 22], "class": "피토스테롤"},
 {"name": "Isorhamnetin 3-O-neohesperidoside", "name_ko": "이소람네틴-3-O-네오헤스페리도사이드", "role": "bioactive", "part": "꽃가루(비폴렌)", "content_text": "표준품 대조로 확인한 2대 주성분의 하나; 꽃가루에서 플라보노이드 배당체 69종 주석(이소람네틴 유도체 46종)[31]", "activity_ko": "꽃가루 플라보노이드는 항산화·티로시나아제 억제 활성(세포 밖 시험)[24]", "source": [24, 31], "class": "플라보놀 배당체"},
]
assays = [
 {"role": "literature", "compound": "Tannins", "compound_ko": "탄닌(총 탄닌)", "part": "열매(도토리; 일본산 Q. crispula, 「식품원료 목록」 이명 Q. crispula var. mandshurica와 같은 종 복합체)",
  "content": "건조 중량 기준 9.9%[9]", "method": "",
  "conditions": {k: "" for k in ["instrument","column","mobile_phase","gradient","flow","temp","detection","injection","sample_prep","standard","linearity","lod","loq","recovery"]},
  "rationale": "도토리의 떫은맛과 섭취 동물의 생리 반응을 결정하는 성분으로, 신갈나무 씨앗도 고탄닌 먹이로 분류되었다[10]. 전문 확인 못함: 초록에는 정량법·분석 조건이 없어 비워 둠. 신갈나무(한국산) 도토리의 탄닌을 정량한 PubMed 논문은 확인하지 못함[9].",
  "source": [9, 10], "url": "https://pubmed.ncbi.nlm.nih.gov/16770711/", "source_kind": "paper"},
]
d = {
 "slug": "quercus-mongolica", "name_ko": "신갈나무", "name_en": "Mongolian oak",
 "scientific_name": "Quercus mongolica Fisch. ex Ledeb.",
 "aliases": ["돌참나무", "물갈나무", "신갈나무열매", "Mongolian oak", "Quercus crispula var. mandshurica Koidz."],
 "sections": [{"key": k, "title": t, "body": b} for k, t, b in sections],
 "compounds": compounds, "markers": [], "assays": assays, "nutrients": [],
 "production": [], "world": [], "gi": [], "orgs": [], "sources": S,
}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for k, t, b in sections: print(k, len(b))
