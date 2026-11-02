import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
A = "2026-11-02"
def pm(title, doi, pmid, pmc=None, full=False):
    t = f"{title} (PMID {pmid}" + (f", {pmc}" if pmc else "") + (", 전문 확인)" if full else ", 초록 확인)")
    return {"title": t, "url": f"https://doi.org/{doi}", "publisher": "PubMed", "accessed": A}
S = [
 {"title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 인디언감자(Apios americana, 이명 감자콩, Earthnut·Ground nut) 사용가능·사용가능부위: 덩이줄기 (로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json)", "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
 pm("Genomics-assisted characterization of a breeding collection of Apios americana, an edible tuberous legume — Sci Rep 2016;6:34908", "10.1038/srep34908", 27721469, "PMC5056515", True),
 pm("Enhancement of isoflavone aglycones, GABA, and mineral bioavailability in Apios americana Medikus by co-fermentation with lactic acid bacteria — Food Chem X 2026", "10.1016/j.fochx.2026.103745", 41953660, "PMC13053864", True),
 pm("Comparison of Antioxidant Capacity by Cooking Method of Apios (Apios americana Medicus) and Its Applicability as an Elder-Friendly Food — Food Sci Nutr 2025", "10.1002/fsn3.70102", 40129998, "PMC11932057", True),
 pm("Quality Comparison of Apios Starch Gel and Whole Apios Gel and Effect of Oil Addition on Retrogradation Inhibition in Whole Apios Gel — Food Sci Nutr 2026", "10.1002/fsn3.71496", 41676013, "PMC12887439", True),
 pm("Physicochemical Properties of Hydroxypropylated Apios Starches — Prev Nutr Food Sci 2020;25(3):286", "10.3746/pnf.2020.25.3.286", 33083378, "PMC7541928", True),
 pm("Characterization and development mechanism of Apios americana tuber starch — Carbohydr Polym 2016;151:198-205", "10.1016/j.carbpol.2016.05.062", 27474558),
 pm("Improvement of gluten-free steamed bread quality by partial substitution of rice flour with powder of Apios americana tuber — Food Chem 2020", "10.1016/j.foodchem.2020.127977", 32919271),
 pm("Comparison of primary and secondary metabolites and antioxidant activities by solid-state fermentation of Apios americana Medikus with different fungi — Food Chem 2024", "10.1016/j.foodchem.2024.140808", 39151342),
 pm("Evaluation of biological activities of a groundnut (Apios americana Medik) extract containing a novel isoflavone — Food Chem 2013;138(1):298-305", "10.1016/j.foodchem.2012.10.100", 23265491),
 pm("Novel isoflavone glucosides in groundnut (Apios americana Medik) and their antiandrogenic activities — J Agric Food Chem 2013;61(9):2183-7", "10.1021/jf305233t", 23402539),
 pm("Biological activities of unique isoflavones prepared from Apios americana Medik. — Biosci Biotechnol Biochem 2016;80(4):774-8", "10.1080/09168451.2015.1127132", 26806328),
 pm("Chemical Constituents of Apios americana Tubers and Their Inhibitory Activities on Nitric Oxide Production in LPS-Stimulated RAW 264.7 Macrophages — J Nat Prod 2018", "10.1021/acs.jnatprod.8b00182", 29932657),
 pm("Investigation of isoflavone constituents from tuber of Apios americana Medik and its protective effect against oxidative damage on RIN-m5F cells — Food Chem 2023", "10.1016/j.foodchem.2022.134655", 36345096),
 pm("Anti-Inflammatory Effect of Lupinalbin A Isolated from Apios americana on Lipopolysaccharide-Treated RAW264.7 Cells — Molecules 2018;23(3):583", "10.3390/molecules23030583", 29509670, "PMC6017804"),
 pm("Anti-diabetic effect of the lupinalbin A compound isolated from Apios americana: In vitro analysis and molecular docking study — Biomed Rep 2021", "10.3892/br.2021.1415", 33692902, "PMC7938295"),
 pm("Evaluation of the Key Odorants in Volatile Oils from Tubers of Apios americana Medikus — J Oleo Sci 2015;64(11):1235-42", "10.5650/jos.ess15132", 26521814),
 pm("Isolation and biochemical characterization of Apios tuber lectin — Molecules 2015;20(1):987-1002", "10.3390/molecules20010987", 25584830, "PMC6272198"),
 pm("Purification and cDNA cloning of a lectin and a lectin-like protein from Apios americana Medikus tubers — Biosci Biotechnol Biochem 2014;78(4):574-81", "10.1080/09168451.2014.885822", 25036952),
 pm("Purification, characterization, and cDNA cloning of a Bowman-Birk type trypsin inhibitor from Apios americana Medikus tubers — Biosci Biotechnol Biochem 2008;72(1):171-8", "10.1271/bbb.70531", 18175899),
 pm("Purification, cDNA cloning and characterization of Kunitz-type protease inhibitors from Apios americana tubers — Biosci Biotechnol Biochem 2020", "10.1080/09168451.2019.1698281", 31790634),
 pm("Apios americana Medikus tuber polysaccharide exerts anti-inflammatory effects by activating autophagy — Int J Biol Macromol 2019", "10.1016/j.ijbiomac.2019.03.012", 30840871),
 pm("Apios americana Medik Extract Alleviates Lung Inflammation in Influenza Virus H1N1- and Endotoxin-Induced Acute Lung Injury — J Microbiol Biotechnol 2015;25(12):2146-52", "10.4014/jmb.1508.08017", 26323273),
 pm("Improvement in post-partum uterine involution in rats treated with Apios americana — J Zhejiang Univ Sci B 2019", "10.1631/jzus.B1800475", 31168971, "PMC6587001"),
 pm("A transcriptome-SNP-derived linkage map of Apios americana (potato bean) — Theor Appl Genet 2018;131(2):333-351", "10.1007/s00122-017-3004-3", 29071392, "PMC5787225"),
 pm("Chromosome-level haplotype-resolved genome assemblies and annotations of Apios americana and Apios priceana — Sci Data 2026", "10.1038/s41597-026-06915-y", 41748593, "PMC13061880"),
 {"title": "Evolution of triploidy in Apios americana (Leguminosae) revealed by genealogical analysis of the histone H3-D gene — Evolution 2004;58(2):284-95 (PMID 15068346, 초록 확인)", "url": "https://pubmed.ncbi.nlm.nih.gov/15068346/", "publisher": "PubMed", "accessed": A},
 pm("Relationships of bradyrhizobia from the legumes Apios americana and Desmodium glutinosum — Appl Environ Microbiol 1999;65(11):4914-20", "10.1128/AEM.65.11.4914-4920.1999", 10543803, "PMC91661"),
 pm("Physicochemical Properties of C-Type Starch from Root Tuber of Apios fortunei in Comparison with Maize, Potato, and Pea Starches — Molecules 2018;23(9):2132", "10.3390/molecules23092132", 30149543, "PMC6225258"),
 pm("Effects of C-Glycosides from Apios americana Leaves against Oxidative Stress during Hyperglycemia — J Agric Food Chem 2017;65(34):7457-7466", "10.1021/acs.jafc.7b03163", 28758742),
 pm("Apios americana Medik flowers extract protects PC12 cells against H2O2 induced neurotoxicity via regulating autophagy — Food Chem Toxicol 2019", "10.1016/j.fct.2018.12.003", 30529124),
 pm("Chemical Constituents from Apios americana and Their Inhibitory Activity on Tyrosinase — Molecules 2018;23(1):232", "10.3390/molecules23010232", 29361770, "PMC6017567"),
 pm("Occurrence and Characterization of Bean common mosaic virus Strain NL1 in Iowa — Plant Dis 2014;98(11):1593", "10.1094/PDIS-07-14-0673-PDN", 30699810),
 pm("Interrelationship between viscosity and electrical properties for edible oils — J Food Sci Technol 2013;50(3):549-54", "10.1007/s13197-011-0346-8", 24425951, "PMC3602556"),
]
for i, s in enumerate(S, 1):
    s["n"] = i
sources = [{"n": s["n"], "title": s["title"], "url": s["url"], "publisher": s["publisher"], "accessed": s["accessed"]} for s in S]

sections = [
 {"key": "overview", "title": "한눈에 보기", "body":
  "인디언감자(Apios americana Medik.)는 콩과(Fabaceae)의 여러해살이 덩굴식물로, 땅속 기는줄기(stolon)가 부풀어 생긴 덩이줄기를 먹으며 영어로는 groundnut·potato bean·Indian potato 등으로 부르고 국내에서는 흔히 '아피오스'라고 한다[2, 6]. 식약처 「식품원료 목록」에는 대표 원료명 '인디언감자', 이명 '감자콩', 영문명 'Earthnut, Ground nut'으로 올라 있고 상태는 '사용가능', 사용 조건은 '사용가능부위 : 덩이줄기'이다[1]. 따라서 잎·꽃을 쓴 연구 결과는 식품원료 사용 부위 밖의 자료다[1, 30, 31]. 이 종을 원재료로 하는 건강기능식품 고시형 원료는 확인하지 못함.\n\n"
  "덩이줄기는 전분이 주성분이고, 탈지 건물 기준 단백질이 11–14%로 덩이줄기 작물 치고는 높으며 저장성이 좋다(약 4 °C에서 1년 이상)[2]. 제니스테인-7-O-젠티오비오사이드 같은 독특한 아이소플라본 배당체가 많아 '콩처럼 아이소플라본을 공급하는 덩이줄기'로 연구되었다[2, 10]. 같은 속의 Apios fortunei·Apios priceana도 식약처 목록에 별도 원료로 있으므로, 이 문서는 A. americana 덩이줄기를 분석한 자료만 옮겼다[1, 26, 29]."},
 {"key": "history", "title": "역사와 쓰임", "body":
  "북아메리카 원주민 여러 집단은 이 식물을 거처 가까이에서 반(半)재배 상태로 기르며 덩이줄기를 주식으로 삼았고, 초기 유럽 이주민에게는 비상 식량으로 알려졌다[2]. 이후에도 원주민과 야생 식물 채집인이 먹었지만 주류 작물로 자리 잡지는 못했다[2]. 1985–1994년 미국에서 야생 유전자원을 모아 개방 수분과 선발을 되풀이한 육종 사업이 진행되어 수량이 높은 개량 계통이 만들어졌다[2].\n\n"
  "일본 북부에서는 식량 작물로 재배하며 말린 덩이줄기 가루를 쿠키·도넛·만두·빵에 넣고[2], 일본에서는 산후 회복용으로도 쓰인다고 소개된다[24]. 국내에서는 경상남도 진주에서 재배한 덩이줄기가 여러 식품 연구에 쓰였고[3–5], 경기도 양평 농가산 덩이줄기로 전분 연구가 이루어졌다[6]. 국내 연구는 고령친화식품(수비드 조리 무스·3D 프린팅)[4], 통째 겔[5], 유산균·곰팡이 발효[3, 9] 같은 가공 소재 개발에 집중되어 있다[3–5, 9]."},
 {"key": "biology", "title": "식물학적 특징", "body":
  "인디언감자는 북아메리카 중·동부 온대가 원산이며 하천·호수 가장자리에서 자라지만 배수가 좋은 밭에서도 재배할 수 있다[2]. 땅 위에는 꼬투리 열매를 맺지만 씨가 작고 결실이 들쭉날쭉하며, 덩이줄기는 감자처럼 땅속 기는줄기가 부풀어 생긴다[2]. 꽃은 구조가 복잡해 곤충이 찾아올 때 튀어 오르는 기작(tripping)으로 수분되고, 부분적 자가불화합성 때문에 타가수분을 주로 한다[2, 25].\n\n"
  "뿌리혹에 공생하는 질소고정 근류균과 함께 자라며, 야생 개체의 주된 근류균은 Bradyrhizobium elkanii 계통에 가깝고 드물게 B. japonicum 유사 유전형도 있었다[2, 28]. 덩이줄기 전분 알갱이는 타원·막대·콩팥 모양으로 지름 1–30 µm이고, 어미 덩이줄기와 새끼 덩이줄기의 전분 결정화도·아밀로펙틴 사슬 길이가 서로 달랐다[7]. 국내산 덩이줄기 전분은 아밀로스 33.2%, A형 X선 회절 양상, 상대 결정화도 21.99%, 호화 온도 약 69 °C로 보고되었다[6]."},
 {"key": "related_species", "title": "이름과 가까운 종", "body":
  "같은 Apios 속의 A. americana·A. priceana·A. fortunei는 식약처 목록에 세 종이 각각 별도 원료(인디언감자, Prices potato bean덩이줄기, Apios fortunei덩이줄기)로 올라 있다[1]. A. priceana는 2026년 A. americana와 함께 염색체 수준 유전체가 해독된 북아메리카 근연종이다[26]. 중국에서 분석한 A. fortunei 덩이뿌리 전분은 C형 결정 구조·아밀로스 35%로 보고되어, A형으로 보고된 국내산 A. americana 전분과 성질이 다르다[6, 29].\n\n"
  "영어 이름 'groundnut'은 다른 작물을 가리킬 때도 쓰여 문헌에서 혼동이 생길 수 있다[34]. 예컨대 식용유 물성 논문 한 편은 'ground nut (Apios americana)' 기름을 다뤘는데, 아피오스 덩이줄기의 총 지방산은 100 g당 120.5 mg 수준에 그쳐[9] 이 표기는 다른 작물(땅콩으로 추정)의 기름을 잘못 적은 것으로 보고 이 문서에서는 그 자료를 쓰지 않았다[9, 34]. 국내 이름 '인디언감자'·'감자콩'은 식약처 목록의 원료명·이명이며[1], 감자(Solanum tuberosum, 가지과)와는 과가 다른 콩과 식물이다[1, 2]."},
 {"key": "cultivation", "title": "재배와 생산", "body":
  "인디언감자는 덩이줄기로 영양번식하며, 개량 계통 평가에서 우수 계통은 포기당 덩이줄기 1,500 g 이상을 냈다[2]. 이형접합성이 높은 계통일수록 새끼 덩이줄기를 많이 달아 수량이 높았고, 근친 정도가 높은 계통은 큰 어미 덩이줄기 하나에 치우치는 경향이 있었다[2]. 야생 3배체는 불임이라 덩이줄기로만 번식하고, 2배체는 씨와 덩이줄기 양쪽으로 번식한다[2, 27].\n\n"
  "미국 아이오와주 조사에서 이 종의 잎에서 남부콩모자이크바이러스(Southern bean mosaic virus)가 검출되었다[33]. 국내에서는 경상남도 진주(집현면 등)에서 재배한 덩이줄기가 연구 시료로 쓰였고[3–5], 연구 논문 서론은 경상남도·충청북도에서 재배된다고 적었다[4]. 그러나 통계청·농림축산식품부의 공식 생산 통계(재배 면적·생산량)와 세계 생산 통계는 확인하지 못함."},
 {"key": "processing", "title": "가공과 제품", "body":
  "국내산 덩이줄기를 조리법별로 비교한 연구에서 생시료의 플라보노이드는 14.879 mg QE/g, 페놀 함량은 44.657 mg GAE/g이었고, 수비드(80 °C, 40분)가 굽기·삶기·전자레인지보다 항산화 지표 손실이 가장 적었다[4]. 이 덩이줄기 무스에 젤라틴·한천을 넣어 KS 고령친화식품 경도 2단계에 맞춘 3D 프린팅 식품이 시험 제작되었다[4]. 전분을 따로 뽑지 않은 통째 겔은 전분 겔보다 이수(물 빠짐)가 적었고, 식용유 4%를 넣으면 저장 중 노화가 가장 잘 억제되었다[5].\n\n"
  "덩이줄기 가루는 β-아밀레이스 활성이 높고 α-아밀레이스는 거의 없어, 쌀가루 일부를 대체한 글루텐 프리 찐빵의 경화를 늦췄다[8]. 말린 가루를 유산균 2종으로 36시간 함께 발효하자 아이소플라본 배당체가 1.837 mg/g에서 0.006 mg/g으로 줄고 비배당체가 0.097 mg/g에서 0.604 mg/g으로 늘었으며 GABA는 52.6 mg/100 g이 되었다[3]. 곰팡이 고체발효에서도 배당체가 비배당체로 바뀌었다[9]. 식약처 「식품 등의 생산실적」에서 이 원료의 건강기능식품 생산실적은 확인하지 못함."},
 {"key": "genetics", "title": "유전과 육종", "body":
  "야생 인디언감자에는 2배체(2n = 22)와 3배체(2n = 33) 집단이 함께 있다[2]. 3배체는 주로 마지막 빙기에 얼음으로 덮였던 북아메리카 동부에 분포하며, 히스톤 H3-D 유전자 분석으로 3배체가 최소 세 번 독립적으로 생겨났다고 추정되었다[27]. 육종 계통(2배체로 추정)의 유전체 크기는 평균 1,644 ± 34 Mb, 야생 수집 계통은 2,380 ± 28 Mb로 측정되었다[2].\n\n"
  "2016년 전사체 조립과 SNP 58,154개·발현 표지 39,609개로 육종 집단을 6개 유전형 무리로 나누고 형질 연관 표지를 찾았다[2]. 2017년에는 11개 연관군·1,121개 좌위로 이루어진 유전자 지도가 만들어져 강낭콩·콩과의 공선성(synteny)이 확인되었다[25]. 2026년 발표된 반수체 분리 염색체 수준 유전체는 1.53 Gb, 의사염색체 11개, 반수체당 예측 유전자 약 26,000개이며 80% 이상이 반복 서열이었다[26]."},
 {"key": "safety", "title": "안전성", "body":
  "식약처 목록에서 인디언감자는 덩이줄기에 한해 '사용가능' 원료이며 별도의 섭취 시 주의사항은 목록에 없다[1]. 덩이줄기에는 80 °C에서 2시간 가열해도 활성이 유지되는 보먼-버크형 트립신 억제 단백질과[20], 쿠니츠형 프로테에이스 억제 단백질이 있다[21]. 덩이줄기 렉틴은 적혈구 응집 활성을 보였고, 사람 장 세포(Caco-2) 단층의 전기저항을 낮춰 세포 사이 투과에 영향을 줄 수 있다고 보고되었다[18, 19]. 이 값은 시험관 결과이며, 조리한 덩이줄기를 먹을 때의 영향은 확인하지 못함.\n\n"
  "국내 조리 연구 논문은 '아피오스에 솔라닌이 있으니 익혀 먹으라'고 적었지만 이 종에서 솔라닌을 정량한 근거는 제시하지 않았다[4]. 이 종의 덩이줄기를 날로 먹었을 때의 소화장애나 알레르기 사례 보고는 PubMed에서 확인하지 못함. 쥐 실험에서는 덩이줄기 가루를 사료의 최대 40%로 5일 먹였으나 독성 평가가 목적은 아니었다[24]. 항염·항산화 효과는 세포·동물 실험 결과뿐이며 사람 시험은 확인하지 못함[13–16, 22, 23]. 식약처·농촌진흥청의 잔류농약·독성 공공 정보는 확인하지 못함."},
]

compounds = [
 {"name": "Genistein 7-O-gentiobioside", "name_ko": "제니스테인-7-O-젠티오비오사이드", "class": "아이소플라본 배당체", "role": "marker", "part": "덩이줄기",
  "content_text": "말린 덩이줄기 가루의 주된 아이소플라본(HG7G와 함께; 총 아이소플라본 2.033 mg/g 건조 가루, 개별 값은 보충 표라 확인하지 못함)[3]",
  "activity_ko": "이 종 덩이줄기에서 새로 밝혀진 아이소플라본으로, 이를 주성분으로 한 알코올 추출물이 MCF-7 세포에서 HO-1 발현을 높였다(세포 시험)[10]", "source": [3, 10]},
 {"name": "2'-Hydroxygenistein", "name_ko": "2'-하이드록시제니스테인", "class": "아이소플라본(비배당체)", "role": "bioactive", "part": "덩이줄기",
  "content_text": "유산균 공동발효 덩이줄기 가루 0.317 mg/g(가공 단계 비교), 시간별 실험 36시간 0.184 mg/g; 발효 전에는 배당체 형태가 주[3]",
  "activity_ko": "덩이줄기에서 얻은 비배당체 4종 가운데 에스트로겐 부분 작용이 가장 강했고 α-글루코시데이스 억제·항산화 활성도 보였다(시험관 시험)[12]", "source": [3, 12]},
 {"name": "Genistein", "name_ko": "제니스테인", "class": "아이소플라본(비배당체)", "role": "bioactive", "part": "덩이줄기",
  "content_text": "유산균 공동발효 가루 0.427 mg/g(가공 단계 비교), 시간별 실험 36시간 0.194 mg/g[3]",
  "activity_ko": "제니스테인-7-O-젠티오비오사이드가 당이 떨어져 생기는 비배당체이며, 발효로 크게 늘어난다[2, 3]", "source": [2, 3]},
 {"name": "2'-Hydroxy-5-methoxygenistein 7-O-glucoside", "name_ko": "2'-하이드록시-5-메톡시제니스테인-7-O-글루코사이드", "class": "아이소플라본 배당체", "role": "bioactive", "part": "덩이줄기",
  "content_text": "분리·구조 결정(함량 확인하지 못함)[11, 14]",
  "activity_ko": "아이소플라본 분획에서 분리한 11종 가운데 과산화수소로 손상된 췌장 β세포주(RIN-m5F)를 가장 잘 보호했고 Keap1-Nrf2 경로가 관여한다고 추정되었다(세포 시험)[14]", "source": [11, 14]},
 {"name": "2'-Hydroxygenistein 7-O-gentiobioside", "name_ko": "2'-하이드록시제니스테인-7-O-젠티오비오사이드", "class": "아이소플라본 배당체", "role": "bioactive", "part": "덩이줄기",
  "content_text": "새 화합물로 분리(함량 확인하지 못함)[11]",
  "activity_ko": "안드로겐 수용체 결합 IC50 280 µM, LNCaP 세포의 PSA mRNA 발현 억제 IC50 20 µM으로 항안드로겐 활성을 보였다(세포 시험)[11]", "source": [11]},
 {"name": "Barpisoflavone A", "name_ko": "바르피소플라본 A", "class": "아이소플라본(비배당체)", "role": "bioactive", "part": "덩이줄기",
  "content_text": "덩이줄기에서 조제(함량 확인하지 못함)[12]",
  "activity_ko": "중간 정도의 에스트로겐 부분 작용과 항산화 활성을 보였다(시험관 시험)[12]", "source": [12]},
 {"name": "Lupinalbin A", "name_ko": "루피날빈 A", "class": "쿠마로노크로몬", "role": "bioactive", "part": "덩이줄기",
  "content_text": "분리(함량 확인하지 못함)[15, 16]",
  "activity_ko": "LPS 자극 대식세포에서 NO·염증성 사이토카인을 줄였고, DPP4 IC50 45.2 µM·α-글루코시데이스 IC50 53.4 µM이었다(시험관·세포 시험)[15, 16]", "source": [15, 16]},
 {"name": "Amylose", "name_ko": "아밀로스(전분)", "class": "다당류(전분)", "role": "nutrient", "part": "덩이줄기",
  "content_text": "국내(양평)산 덩이줄기 전분의 아밀로스 33.2%; 전분 알갱이 지름 약 3–20 µm, 호화 온도 약 69 °C[6]; 미국 육종 계통 전분 알갱이 1–30 µm[7]",
  "activity_ko": "덩이줄기의 주 탄수화물이며, 아밀로스가 비교적 많아 하이드록시프로필화 같은 화학 변성이 쉬웠다[6, 7]", "source": [6, 7]},
 {"name": "Stachyose", "name_ko": "스타키오스", "class": "올리고당(라피노스계)", "role": "nutrient", "part": "덩이줄기",
  "content_text": "가루의 탄수화물은 주로 전분·자당이고 라피노스·스타키오스를 함유(정량값 초록에 없음, 확인하지 못함)[8]",
  "activity_ko": "콩과 특유의 올리고당으로 덩이줄기 가루에서 확인되었다[8]", "source": [8]},
 {"name": "gamma-Aminobutyric acid", "name_ko": "GABA(감마아미노뷰티르산)", "class": "비단백질 아미노산", "role": "bioactive", "part": "덩이줄기(발효 가루)",
  "content_text": "유산균 공동발효 가루 52.6 mg/100 g(발효 전 값은 보충 표라 확인하지 못함)[3]",
  "activity_ko": "발효 중 글루탐산이 줄고 GABA가 늘어 글루탐산 탈카복실화가 일어난 것으로 해석되었다(성분 변화만 측정)[3]", "source": [3]},
 {"name": "Glutamic acid", "name_ko": "글루탐산", "class": "아미노산", "role": "nutrient", "part": "덩이줄기",
  "content_text": "건조 가루 유리아미노산 가운데 글루탐산·아스파르트산·프롤린이 주된 비필수 아미노산; 총 유리아미노산 591.69 mg/100 g(발효 전, 곰팡이 발효 연구)[3, 9]",
  "activity_ko": "건조 가루의 감칠맛·단맛과 관련된 주요 유리아미노산이다[3]", "source": [3, 9]},
 {"name": "Linoleic acid", "name_ko": "리놀레산", "class": "다가불포화 지방산", "role": "nutrient", "part": "덩이줄기",
  "content_text": "모든 가공 단계 시료에서 가장 많은 불포화지방산(총 포화지방산 125.8 mg/100 g 건조 가루)[3]; 발효 전 총 지방산 120.5 mg/100 g[9]",
  "activity_ko": "지질 함량이 낮은 덩이줄기에서 올레산·α-리놀렌산과 함께 주된 불포화지방산이다[3]", "source": [3, 9]},
 {"name": "1-Octen-3-ol", "name_ko": "1-옥텐-3-올", "class": "휘발성 알코올", "role": "bioactive", "part": "덩이줄기",
  "content_text": "GC-O·AEDA로 가장 강한 향 활성 성분(냄새 활성값 높음; 정량값 초록에 없음, 확인하지 못함)[17]",
  "activity_ko": "헥사날과 함께 덩이줄기 향의 핵심 성분으로 판정되었다[17]", "source": [17]},
 {"name": "Hexanal", "name_ko": "헥사날", "class": "휘발성 알데하이드", "role": "bioactive", "part": "덩이줄기",
  "content_text": "SAFE 추출 휘발성분의 11.0%(4-하이드록시-4-메틸-2-펜탄온 34.2% 다음)[17]",
  "activity_ko": "풋내를 내는 향 성분으로 냄새 활성값이 높았다[17]", "source": [17]},
 {"name": "Aromadendrin 5-methyl ether", "name_ko": "아로마덴드린 5-메틸 에터", "class": "다이하이드로플라보놀", "role": "bioactive", "part": "덩이줄기",
  "content_text": "덩이줄기에서 분리한 9종 가운데 하나(함량 확인하지 못함)[32]",
  "activity_ko": "Apios 속에서 처음 보고된 성분이며, 함께 분리한 성분 일부가 타이로시네이스를 억제했다(시험관 시험)[32]", "source": [32]},
]

assays = [
 {"role": "literature", "compound": "Isoflavones (13 derivatives incl. genistein 7-O-gentiobioside, genistein, 2'-hydroxygenistein)", "compound_ko": "아이소플라본 13종(제니스테인-7-O-젠티오비오사이드·제니스테인·2'-하이드록시제니스테인 등)", "part": "덩이줄기(열풍 건조 가루)",
  "content": "건조 가루 총 아이소플라본 2.033 mg/g, 살균 2.188 mg/g, 유산균 발효 0.996 mg/g; 발효 가루 제니스테인 0.427·2'-하이드록시제니스테인 0.317 mg/g[3]",
  "method": "UPLC-UV(초고성능 액체크로마토그래피, 254 nm)",
  "conditions": {"instrument": "Waters Acquity UPLC H-Class Plus", "column": "BEH Phenyl, 2.1 mm × 150 mm, 1.7 µm (Waters)", "mobile_phase": "A: 0.05% 폼산 수용액, B: 아세토나이트릴", "gradient": "B 5% 시작 → 18분 30% → 20분 100%", "flow": "0.3 mL/min", "temp": "35 °C", "detection": "254 nm", "injection": "2 µL", "sample_prep": "가루 0.2 g + 30% 에탄올 10 mL, 실온 초음파 추출 1시간, 0.45 µm 여과", "standard": "아이소플라본 표준품 외부 검량(6농도, 0.1–1.0 mg/mL), 머무름 시간 일치로 동정", "linearity": "R² 0.999–1.000", "lod": "", "loq": "", "recovery": ""},
  "rationale": "제니스테인-7-O-젠티오비오사이드 등 아이소플라본 배당체가 이 종 덩이줄기의 특징 성분이고, 가공·발효에 따른 배당체→비배당체 전환을 추적하는 지표로 쓰였다[2, 3]. PMC 전문(Methods) 확인, 검출·정량한계와 회수율은 본문에 없어 확인하지 못함[3].",
  "source": [2, 3], "url": "https://doi.org/10.1016/j.fochx.2026.103745", "source_kind": "paper"},
 {"role": "literature", "compound": "Fatty acids (FAME)", "compound_ko": "지방산(메틸에스터)", "part": "덩이줄기(열풍 건조 가루)",
  "content": "건조 가루 총 포화지방산 125.8 mg/100 g, 발효 가루 144.2 mg/100 g; 리놀레산이 가장 많은 불포화지방산[3]",
  "method": "GC-FID(기체크로마토그래피-불꽃이온화검출)",
  "conditions": {"instrument": "Shimadzu Nexis GC-2030, FID", "column": "SP-2560 모세관 칼럼, 100 m × 0.25 mm, 0.2 µm (Supelco)", "mobile_phase": "운반 기체 헬륨 0.75 mL/min", "gradient": "100 °C(4분) → 3 °C/min → 240 °C(15분 유지)", "flow": "0.75 mL/min", "temp": "주입구 225 °C, 검출기 285 °C", "detection": "FID", "injection": "분할 주입 200:1", "sample_prep": "가루 25 mg + 0.5 N NaOH-메탄올 0.5 mL·내부표준 트라이운데카노인, 100 °C 5분 → 14% BF3-메탄올 2 mL 100 °C 30분 → 아이소옥테인 추출", "standard": "내부표준 C11:0, 37종 FAME 혼합 표준", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "지질이 적은 덩이줄기의 지방산 조성(리놀레산·올레산·α-리놀렌산 중심)을 가공 단계별로 비교한 정량 조건이다[3]. PMC 전문 확인, 검출·정량한계는 본문에 없어 확인하지 못함[3].",
  "source": [3], "url": "https://doi.org/10.1016/j.fochx.2026.103745", "source_kind": "paper"},
]

d = {
 "slug": "apios-americana", "name_ko": "인디언감자", "name_en": "Groundnut (Apios, Potato bean)",
 "scientific_name": "Apios americana Medik.",
 "aliases": ["인디언감자", "감자콩", "아피오스", "Apios", "Groundnut", "Earthnut", "Potato bean", "Indian potato"],
 "sections": sections, "compounds": compounds, "markers": [], "assays": assays,
 "nutrients": [], "production": [], "world": [], "gi": [], "orgs": [], "sources": sources,
}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in sections: print(s["key"], len(s["body"]))
