import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
A = "2026-11-02"
def pm(n, title, doi, pmid, pmc=None, note="초록 확인"):
    t = f"{title} (PMID {pmid}" + (f", {pmc}" if pmc else "") + f", {note})"
    return {"n": n, "title": t, "url": f"https://doi.org/{doi}", "publisher": "PubMed", "accessed": A}
S = [
 {"n": 1, "title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 그릭세이지잎(Salvia triloba L.F.; Greek sage), 사용가능, 사용가능부위: 잎; 같은 목록의 'Greek sage잎'(Salvia fruticosa, 사용가능, 잎)·살비아(Salvia officinalis)·스클라레아살비아(Salvia sclarea; 영명 'Clary, Greek Sage Leaves')·Apple sage잎(Salvia pomifera)·Spanish sage잎(Salvia lavandulifolia)·단삼·배암차즈기·치아·멕시칸치아 행 대조 (로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json)", "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
 pm(2, "Phytochemical screening and biological evaluation of Greek sage (Salvia fruticosa Mill.) extracts — Sci Rep 2023;13:22309", "10.1038/s41598-023-49695-w", "38102229", "PMC10724190", "전문 확인"),
 pm(3, "Evaluation of HPLC Profile, Antioxidant, Quorum Sensing, Biofilm, Swarming Motility, and Enzyme Inhibition Activities of Conventional and Green Extracts of Salvia triloba — Food Sci Nutr 2024;12(12):10716-10733", "10.1002/fsn3.4580", "39723056", "PMC11666897", "전문 확인"),
 pm(4, "Hydrodistillation time-dependent variations in the volatile oil characteristics of fresh and dried Salvia species — Sci Rep 2026;16", "10.1038/s41598-026-42109-7", "41760873", "PMC13009210", "전문 확인"),
 pm(5, "Influence of Climate-Related Environmental Stresses on Economically Important Essential Oils of Mediterranean Salvia sp. — Front Plant Sci 2022;13:864807 (총설)", "10.3389/fpls.2022.864807", "35599878", "PMC9114806", "전문 확인"),
 pm(6, "EST analysis and annotation of transcripts derived from a trichome-specific cDNA library from Salvia fruticosa — Plant Cell Rep 2010;29(5):523-34", "10.1007/s00299-010-0841-9", "20333525"),
 pm(7, "Towards Elucidating Carnosic Acid Biosynthesis in Lamiaceae: Functional Characterization of the Three First Steps of the Pathway in Salvia fruticosa and Rosmarinus officinalis — PLoS One 2015;10(5):e0124106", "10.1371/journal.pone.0124106", "26020634", "PMC4447455"),
 pm(8, "Monoterpene synthases of three closely related sage species (Salvia officinalis, S. fruticosa and S. pomifera, Lamiaceae) — Plant Physiol Biochem 2023;196:318-327", "10.1016/j.plaphy.2023.01.034", "36738511"),
 pm(9, "Morphological, genetic and epigenetic aspects of homoploid hybridization between Salvia officinalis L. and Salvia fruticosa Mill. — Sci Rep 2019;9:3276", "10.1038/s41598-019-40080-0", "30824783", "PMC6397195"),
 pm(10, "Dynamics of yield components and essential oil production in a commercial hybrid sage (Salvia officinalis x Salvia fruticosa cv. Newe Ya'ar no. 4) — J Agric Food Chem 1999;47(10):4341-5", "10.1021/jf9901587", "10552813"),
 pm(11, "In vitro cholinesterase inhibitory and antioxidant effects of essential oils and extracts of two new Salvia fruticosa Mill. cultivars (Turgut and Uysal) and GC-MS analysis of the essential oils — Int J Environ Health Res 2023;34(2):674-686", "10.1080/09603123.2022.2163988", "36739545"),
 pm(12, "Effect of nitrogen concentration of the nutrient solution on the volatile constituents of leaves of Salvia fruticosa Mill. in solution culture — J Agric Food Chem 2003;51(22):6505-8", "10.1021/jf030308k", "14558770"),
 pm(13, "A simple method to obtain essential oils from Salvia triloba L. and Laurus nobilis L. by using microwave-assisted hydrodistillation — Z Naturforsch C 2005;60(5-6):501-4", "10.1515/znc-2005-5-620", "16047413"),
 pm(14, "Isolation of the essential oil from Salvia triloba L. crop residues: analysis of the chemical profile and evaluation of its antimicrobial activity — Sci Rep 2026", "10.1038/s41598-026-62047-8", "42443427"),
 pm(15, "Chemical composition and larvicidal evaluation of Mentha, Salvia, and Melissa essential oils against the West Nile virus mosquito Culex pipiens — Parasitol Res 2010;107(2):327-35", "10.1007/s00436-010-1865-3", "20405142"),
 pm(16, "HPLC-SPE-NMR characterization of major metabolites in Salvia fruticosa Mill. extract with antifungal potential: relevance of carnosic acid, carnosol, and hispidulin — J Agric Food Chem 2015;63(2):457-63", "10.1021/jf5050734", "25537192"),
 pm(17, "Aqueous extraction kinetics of soluble solids, phenolics and flavonoids from sage (Salvia fruticosa Miller) leaves — J Food Sci Technol 2015;52(5):2797-805", "10.1007/s13197-014-1308-8", "25892777", "PMC4397303"),
 pm(18, "Anti-Inflammatory and Antioxidant Activities of Salvia fruticosa: An HPLC Determination of Phenolic Contents — Evid Based Complement Alternat Med 2016:7178105", "10.1155/2016/7178105", "26881007", "PMC4735903", "전문 확인"),
 pm(19, "Reproductive toxicity potentials of Salvia fruticosa (Labiatae) in rats — J Ethnopharmacol 1998;61(1):67-74", "10.1016/s0378-8741(98)00016-6", "9687083"),
 pm(20, "The genotoxic and antigenotoxic effects of Salvia fruticosa leaf extract in human blood lymphocytes — Drug Chem Toxicol 2014;37(3):295-302", "10.3109/01480545.2013.851689", "24224704"),
 pm(21, "An investigation of some Turkish herbal medicines in Salmonella typhimurium and in the COMET assay in human lymphocytes — Teratog Carcinog Mutagen 1996;16(2):125-38", "10.1002/(SICI)1520-6866(1996)16:2<125::AID-TCM6>3.0.CO;2-K", "8875742"),
 pm(22, "Toxicity evaluation of an essential oil mixture from the Cretan herbs thyme, Greek sage and Cretan dittany — NPJ Sci Food 2020;4:20", "10.1038/s41538-020-00080-1", "33298942", "PMC7652874"),
 pm(23, "Plants used during pregnancy, childbirth, postpartum and infant healthcare in Palestine — Complement Ther Clin Pract 2015;21(2):84-93", "10.1016/j.ctcp.2015.03.004", "25900613"),
 pm(24, "Ethnopharmacological survey of wild medicinal plants in Showbak, Jordan — J Ethnopharmacol 2009;123(1):45-50", "10.1016/j.jep.2009.02.031", "19429338"),
 {"n": 25, "title": "European Medicines Agency, HMPC — Salviae trilobae folium (Salvia fruticosa Mill., folium): public statement(2016-05-31 채택)·assessment report EMA/HMPC/599992/2014 — 이 환경에서 EMA 사이트가 열리지 않아 WebSearch 요약으로만 확인(원문 열람 못함)", "url": "https://www.ema.europa.eu/en/medicines/herbal/salviae-trilobae-folium", "publisher": "European Medicines Agency", "accessed": A},
 pm(26, "Salvia fruticosa Induces Vasorelaxation In Rat Isolated Thoracic Aorta: Role of the PI3K/Akt/eNOS/NO/cGMP Signaling Pathway — Sci Rep 2017;7:686", "10.1038/s41598-017-00790-9", "28386068", "PMC5429649"),
 pm(27, "Assessing the Influence of Salvia triloba on Memory Deficit Caused by Sleep Deprivation in the Context of Oxidative Stress — Curr Alzheimer Res 2022;19(6):440-448", "10.2174/1567205019666220805092450", "35929624"),
 pm(28, "In vitro biological activity of Salvia fruticosa Mill. infusion against amyloid β-peptide-induced toxicity and inhibition of GSK-3β, CK-1δ, and BACE-1 enzymes relevant to Alzheimer's disease — Saudi Pharm J 2021;29(3):236-243", "10.1016/j.jsps.2021.01.007", "33981172", "PMC8084717"),
 pm(29, "Comparative phytochemical investigation of Salvia miltiorrhiza and Salvia triloba — Planta Med 1995;61(5):453-5", "10.1055/s-2006-958135", "17238099"),
 pm(30, "Constituents from Salvia triloba — Fitoterapia 2001;72(7):850-3", "10.1016/s0367-326x(01)00327-6", "11677033"),
 pm(31, "Improving yeast strains using recyclable integration cassettes, for the production of plant terpenoids — Microb Cell Fact 2011;10:4", "10.1186/1475-2859-10-4", "21276210", "PMC3042375"),
 pm(32, "Protective Effects of the Essential Oil of Salvia fruticosa and Its Constituents on Astrocytic Susceptibility to Hydrogen Peroxide-Induced Cell Death — J Agric Food Chem 2009;57(15):6636-41", "10.1021/jf901162f", "19722569"),
 pm(33, "Chemical Profiling and Antioxidant and Anti-Amyloid Capacities of Salvia fruticosa Extracts from Greece — Plants (Basel) 2023;12(18):3191", "10.3390/plants12183191", "37765357", "PMC10535607"),
]

secs = [
("overview", "한눈에 보기", """그릭세이지는 꿀풀과(Lamiaceae) 샐비어속의 늘푸른 떨기나무로, 지중해 동부가 원산이며 잎을 차·향신료·정유 원료로 쓴다[4, 5]. 식약처 「식품원료 목록」에는 '그릭세이지잎'(학명 Salvia triloba L.F., 영명 Greek sage)이 '사용가능' 원료로 올라 있고, 사용 조건은 '사용가능부위 : 잎'이다[1]. 같은 목록에는 학명을 Salvia fruticosa 로 적은 'Greek sage잎' 행도 따로 있으며, 이 행 역시 사용가능·잎 조건이다[1]. 학술 문헌은 Salvia triloba L.f.(1782)를 Salvia fruticosa Mill.(1768)의 이명으로 다루고, 최근 논문 대부분은 S. fruticosa 라는 이름을 쓴다[2, 6]. 건강기능식품 고시형 원료의 원재료로는 올라 있지 않다[1].

잎 추출물에는 로즈마린산·카르노신산·카르노솔·스쿠텔라린 같은 페놀 성분이 많다[2]. 잎 정유의 주성분은 1,8-시네올·캠퍼 같은 산소화 모노테르펜이고, 많은 연구에서 1,8-시네올이 50–70%에 이른다[5]. 다만 튀르키예 재배 시료처럼 α-투존이 가장 많은 정유도 보고되어, 산지와 개체에 따라 조성이 크게 다르다[4]. 쥐 대동맥 고리 실험에서 잎 에탄올 추출물이 혈관을 이완시켰고, 수면 박탈 쥐에게 추출물 375 mg/kg을 6주 먹인 실험에서는 기억력 저하가 줄었지만, 모두 동물·조직 수준의 결과로 사람에서 확인된 효과는 아니다[26, 27]."""),
("history", "역사와 전통 이용", """지중해 동부에서는 예부터 잎을 우려 마셨고, 그리스와 튀르키예에서는 말린 잎을 '파스코멜로(faskomelo)'라는 차로 끓여 마신다[4]. 한 논문은 레바논에서는 궤양 통증에, 튀르키예에서는 비뇨기 질환에 이 잎을 썼다고 정리했다[2]. 레바논 민간에서는 통증·감기·독감에 잎을 끓여 차로 마시고, 증기로 쐬거나 겉에 바르기도 한다[18]. 팔레스타인 여성 372명을 조사한 연구에서는 임신·출산·산후·영아 돌봄에 가장 흔히 쓴 허브 가운데 하나였다[23]. 요르단 쇼박 지역의 민속 약용식물 조사에서는 주민들이 흔히 쓰는 안전한 종으로 분류되었다[24]. 미국에 수입되는 세이지의 대부분이 세이지(S. officinalis)가 아니라 이 종이라는 서술도 있다[18].

한 논문은 이 종이 유럽약전과 영국약전에 실려 있다고 적었으나, 약전 원문은 확인하지 못함[4]. 유럽의약품청(EMA) 약초위원회(HMPC)는 2016년 5월 31일 공개 성명에서, 여러 회원국에서 쓰이지만 오랜 전통 사용을 입증할 문헌이 부족하다며 유럽연합 약초 모노그래프를 만들지 않았다고 알려져 있다(원문은 열지 못하고 검색 요약으로만 확인)[25]."""),
("biology", "식물학적 특징", """그릭세이지는 지중해 지역 원산으로 이탈리아 남부와 발칸반도 남부(그리스)에서 시리아 서부까지 자란다[5]. 해발 100–800 m의 건조한 석회암 바위 땅, 소나무 숲 가장자리, 하천 바닥, 길가에서 자라고, 다른 지중해 나라에서는 관상용으로도 심는다[5]. 영어로 three-lobed sage, Greek sage 등으로 불리며, 튀르키예에서는 Anatolian sage 라고도 한다[4, 5]. 꿀벌이 찾는 밀원식물이기도 하다[5]. 자연에서는 가뭄에 매우 강하지만, 옥상녹화처럼 재배 조건에서는 가뭄을 잘 견디지 못한다는 보고가 있다[5].

정유와 테르페노이드·플라보노이드는 잎 표면의 샘털(선모)에서 만들어져 저장된다[6]. 지상부에서는 탄화수소 12종, 스테롤 4종, 트리테르펜 3종, 지방산 19종, 페놀산 2종, 플라보노이드 5종이 검출되었다[30]. 뿌리에서는 로일레아논·7α-아세톡시로일레아논·수기올 같은 아비에탄 디테르펜이 확인되었으나, 뿌리는 국내 식품원료 목록의 사용 부위가 아니다[29, 1]."""),
("related_species", "이름과 가까운 종", """샐비어속은 1,000종 가까이 되는 꿀풀과 최대의 속이다[5]. 그릭세이지와 가장 가까운 종으로는 세이지(S. officinalis, 국내 목록명 살비아)와 사과세이지(S. pomifera)가 꼽히며, 세 종의 잎 정유 모노테르펜 합성효소 유전자를 함께 비교한 연구가 있다[8]. 세이지 정유는 ISO 규격상 α-투존 18–43%, 캠퍼 4.5–45%, 1,8-시네올 5.5–13%를 갖춰야 하지만, 그릭세이지 정유는 ISO 규격이 없고 대부분의 연구에서 투존이 많지 않았다[5]. 그러므로 세이지(S. officinalis)의 정유·투존 자료를 그릭세이지에 그대로 옮기면 안 된다[5].

크로아티아 비스섬에서는 세이지와 그릭세이지가 자연 교잡한 이배체 잡종이 확인되었고, 이스라엘에서는 두 종의 교배 품종(Newe Ya'ar No. 4)이 상업 재배된다[9, 10]. 식약처 목록에는 살비아(S. officinalis), 스클라레아살비아(S. sclarea), 단삼(S. miltiorrhiza), 배암차즈기(S. plebeia), 치아(S. columbariae), 멕시칸치아(S. hispanica), Spanish sage(S. lavandulifolia), Apple sage(S. pomifera)가 각각 따로 올라 있다[1]. 특히 스클라레아살비아의 영명 칸에 'Greek Sage Leaves'가 함께 적혀 있어 이름을 혼동하기 쉽다[1]. 이 자료의 수치는 S. triloba 또는 S. fruticosa 로 동정된 시료에서 나온 것만 썼다[2, 3, 4]."""),
("cultivation", "재배와 산지", """그릭세이지는 레바논처럼 야생에서 채취해 쓰기도 하고, 튀르키예처럼 밭에서 재배하기도 하며, 다른 지중해 나라에서는 관상용으로 심는다[4, 5, 18]. 튀르키예에서는 'Turgut'와 'Uysal'이라는 두 신품종이 개발되었다[11]. 튀르키예 내륙 에게 지역(해발 1,009 m) 시험포에서는 1년생 식물을 개화 초기에 지상 8–10 cm 높이로 베어 잎만 모아 정유를 분석했다[4]. 양액재배(NFT) 시험에서는 질소 농도(100·150·200 mg/L)와 생육 단계(만개기·종자 형성기)에 따라 정유 성분이 달라졌고, 1,8-시네올·β-카리오필렌·비리디플로롤이 주성분이었다[12]. 재배한 식물은 야생보다 1,8-시네올을 적게 만든다는 보고도 있다[5].

세이지와의 교배 품종에서는 50일 생육 동안 생체 수확량이 20배 넘게 늘었지만 잎 정유 함량과 조성은 크게 변하지 않았고, 아래쪽 오래된 잎일수록 캠퍼와 α-투존 비율이 높았다[10]. 국내 재배 면적·생산량 통계는 확인하지 못함."""),
("processing", "가공과 이용", """잎은 말려 우림차·향신료로 쓰고, 수증기 증류로 정유를 얻으며, 물·에탄올 추출물도 만든다[2, 4]. 잎을 물로 우리는 실험(60–80 °C, 입자 2–8 mm, 투입량 1–4%)에서 가용성 고형분은 잎 100 g당 25 g이었고, 고형분의 30 g/100 g이 총페놀, 25 g/100 g이 총플라보노이드였다[17]. 70 °C를 넘으면 추출 속도와 평형 농도가 뚜렷이 높아졌다[17]. 용매를 비교한 연구에서 70% 에탄올 추출이 로즈마린산(마른 잎 1 g당 31.56 mg)과 생리활성 성분 총량이 가장 많았고, 끓는 물 추출에서는 로즈마린산이 4.96 mg/g으로 낮고 스쿠텔라린이 가장 많았다[2].

정유 함량은 신선한 잎 0.42–0.50%, 말린 잎 1.2–1.52%였고, 증류 시간이 길수록 α-투존과 1,8-시네올 비율이 줄었다[4]. 마이크로파 보조 수증기 증류는 일반 수증기 증류보다 짧은 시간에 정유 수율과 1,8-시네올 함량이 조금 더 높았다[13]. 수확 잔재에서 얻은 정유는 대장균을 10 mg/mL, 리스테리아·살모넬라를 12 mg/mL에서 억제해 천연 보존료 후보로 제안되었다(시험관 시험)[14]. 국내 제품 생산실적은 확인하지 못함."""),
("genetics", "유전 정보", """잎 샘털에서 만든 cDNA 라이브러리의 2,304개 클론을 읽어 고품질 EST 1,615개와 고유 서열 904개를 얻었고, 테르페노이드·페닐프로파노이드·플라보노이드 생합성 관련 유전자가 샘털에서 더 많이 발현되었다[6]. 샘털 전사체에서 찾은 디테르펜 합성효소 SfCPS·SfKSL이 미일티라디엔을 만들고, 시토크롬 P450 효소 SfFS가 페루기놀을 만드는 것이 확인되어 카르노신산 생합성의 첫 세 단계가 밝혀졌다[7]. 전장 유전체 해독과 디지털 PCR로 비교한 연구에서 모노테르펜 합성효소 열린 읽기틀은 그릭세이지 15개, 세이지 12개, 사과세이지 13개로 예측되었고 대부분 반수체 유전체당 한 벌이었다[8]. 1,8-시네올 합성효소 유전자(SfCinS1)는 효모에 넣어 식물 테르펜을 만드는 데 쓰였다[31].

세이지와의 자연 잡종은 SSR 분석에서 이배체로 나타나 같은 배수성 잡종으로 판단되었고, 두 어버이 종 사이 유전자 흐름은 매우 낮았다[9]. 염색체 수와 유전체 크기를 밝힌 공식 자료는 확인하지 못함."""),
("safety", "안전성", """식약처 목록에서 그릭세이지잎은 '사용가능' 원료이고 사용 부위는 잎이며, 별도 섭취량 기준은 적혀 있지 않다[1]. 정유에 들어 있을 수 있는 투존은 GABA 작용을 막아 근육 경련·발작을 일으킬 수 있으며, 한 총설은 유럽 규정이 세이지류로 만든 식품의 투존을 25 mg/kg 이하로 둔다고 적었다[5]. 그릭세이지 정유는 대개 투존이 적지만, 튀르키예 재배 잎 정유에서는 α-투존이 16.66–17.19%로 가장 많았고 수확 잔재 정유에서도 투존이 25.83%였다[5, 4, 14]. 잎 우림차의 투존 함량은 확인하지 못함.

쥐에게 잎 물 추출물(800 mg/kg)이나 에탄올 추출물(400 mg/kg)을 30일 먹이자 암수 모두에서 착상 수와 생존 태아 수가 줄었다[19]. 사람 림프구 시험관 시험에서 잎 추출물은 염색체 이상과 소핵을 늘렸으나, 에임스 시험(TA98·TA100)에서는 음성이었다[20, 21]. 그릭세이지·백리향·크레타 디타니 정유 혼합물의 쥐 급성·아급성 독성 시험에서는 독성이 나타나지 않았다[22]. 임신 중 사용 실태는 보고되었으나 임부 안전성 근거와 사람 대상 임상 안전성 자료는 확인하지 못함[23]. 공공기관의 알레르기·잔류농약 정보는 확인하지 못함."""),
]

def c(name, ko, cls, role, part, content, act, src):
    return {"name": name, "name_ko": ko, "class": cls, "role": role, "part": part, "content_text": content, "activity_ko": act, "source": src}
comps = [
 c("Rosmarinic acid", "로즈마린산", "페놀산(카페산 이량체)", "marker", "잎",
   "70% 에탄올 추출 마른 잎 1 g당 31.56 mg, 끓는 물 추출 4.96 mg[2]; 지상부 메탄올 추출물 169.7 μg/g, 초음파 추출물 135.1 μg/g[3]",
   "물 추출물을 뺀 모든 추출물에서 주된 항산화 성분(HPLC-ABTS 후컬럼 반응)[2]; 우림차의 대표 성분으로, 아밀로이드 독성 세포 모델에서 함께 시험됨[28]", [2, 3, 28]),
 c("Carnosic acid", "카르노신산", "아비에탄 디테르펜(페놀성)", "bioactive", "잎",
   "100% 에탄올 추출 마른 잎 1 g당 14.82 mg, 70% 에탄올 13.88 mg[2]",
   "에틸아세테이트 분획의 주성분으로 잿빛곰팡이·페니실리움 억제(시험관)[16]; 그리스산 지상부 추출물의 주요 성분[33]", [2, 16, 33]),
 c("Carnosol", "카르노솔", "아비에탄 디테르펜 락톤", "bioactive", "잎",
   "70% 에탄올 추출 마른 잎 1 g당 7.88 mg[2]",
   "항진균 활성 성분(시험관)[16]; 그리스산 지상부 추출물의 주요 성분[33]", [2, 16, 33]),
 c("Scutellarin", "스쿠텔라린", "플라본 배당체", "bioactive", "잎",
   "마른 잎 1 g당 물 추출 7.77 mg, 30% 에탄올 8.92 mg, 70% 에탄올 7.35 mg[2]",
   "물 추출물에서 가장 많은 성분이자 주된 항산화 기여 성분[2]", [2]),
 c("Salvianolic acid B", "살비아놀산 B", "페놀산(카페산 유도체)", "bioactive", "잎",
   "마른 잎 1 g당 70% 에탄올 추출 6.86 mg, 30% 에탄올 6.52 mg[2]",
   "트롤록스보다 강한 항산화 표준품으로 측정됨(시험관)[2]", [2]),
 c("Caffeic acid", "카페산", "페놀산", "bioactive", "잎",
   "마른 잎 1 g당 0.13–0.15 mg[2]; 지상부 메탄올 추출물 4.50 μg/g[3]",
   "시험한 표준품 가운데 항산화·잔틴산화효소 억제가 가장 강함(IC50 0.1 μg, 2.8 µM, 효소 시험)[2]", [2, 3]),
 c("Rutin", "루틴", "플라보놀 배당체", "bioactive", "지상부",
   "지상부 메탄올 추출물 21.36 μg/g, 초음파 추출물 21.17 μg/g[3]; 레바논산 지상부 추출물에서 루테올린과 함께 가장 많은 페놀로 동정[18]",
   "", [3, 18]),
 c("Hispidulin", "히스피둘린", "메톡시 플라본", "bioactive", "잎",
   "에틸아세테이트 분획의 주요 성분(qNMR 정량, 수치는 초록에 없어 확인하지 못함)[16]",
   "잿빛곰팡이·페니실리움 억제(시험관)[16]", [16]),
 c("Salvigenin", "살비게닌", "메톡시 플라본", "bioactive", "잎",
   "에틸아세테이트 분획의 주요 성분[16]", "", [16]),
 c("Eucalyptol", "1,8-시네올(유칼립톨)", "모노테르펜 산화물", "marker", "잎(정유)",
   "많은 연구에서 잎 정유의 50–70%, 최고 83.5%[5]; 잎 정유 46.8–54.2%[13]; 튀르키예 재배 잎 정유 8.36–12.45%[4]; 그리스 집단 1 정유 31.4%[15]",
   "", [4, 5, 13, 15]),
 c("Camphor", "캠퍼", "모노테르펜 케톤", "bioactive", "잎(정유)",
   "튀르키예 재배 잎 정유 9.44–13.28%[4]; 그리스 집단 정유 22.6–23.1%[15]; 수확 잔재 정유 17.86%[14]",
   "", [4, 14, 15]),
 c("alpha-Thujone", "α-투존", "모노테르펜 케톤", "bioactive", "잎(정유)",
   "튀르키예 재배 잎 정유에서 가장 많은 성분, 1시간 증류 때 신선 잎 16.66%·말린 잎 17.19%[4]; 대부분의 연구에서는 유의한 양이 없음[5]",
   "GABA 작용을 막아 경련을 일으킬 수 있는 성분[5]", [4, 5]),
 c("beta-Thujone", "β-투존", "모노테르펜 케톤", "bioactive", "잎(정유)",
   "튀르키예 재배 잎 정유 3.94–5.13%[4]", "", [4]),
 c("alpha-Pinene", "α-피넨", "모노테르펜", "bioactive", "잎(정유)",
   "튀르키예 재배 잎 정유 4.62–9.28%(말린 잎 6.62–9.28%)[4]; 그리스 집단 2 정유 12.7%[15]",
   "정유의 성상교세포 보호 효과에 기여하는 성분으로 제시(세포 실험)[32]", [4, 15, 32]),
 c("alpha-Humulene", "α-후물렌", "세스퀴테르펜", "bioactive", "잎(정유)",
   "튀르키예 재배 잎 정유 5.67–8.75%[4]",
   "과산화수소 손상 성상교세포 보호에 기여하는 성분으로 제시(세포 실험)[32]", [4, 32]),
]

assays = [
 {"role": "literature", "compound": "Rosmarinic acid", "compound_ko": "로즈마린산(카페산·스쿠텔라린·살비아놀산 B·카르노신산·카르노솔 동시 정량)",
  "part": "잎(그리스 유기농 생산자의 그늘 건조 잎)",
  "content": "마른 잎 1 g당 로즈마린산 70% 에탄올 31.56 ± 1.88 mg, 물 4.96 ± 0.65 mg; 카르노신산 100% 에탄올 14.82 ± 1.66 mg; 카르노솔 70% 에탄올 7.88 ± 1.33 mg; 스쿠텔라린 30% 에탄올 8.92 ± 1.56 mg[2]",
  "method": "UHPLC-PDA / Q-Orbitrap HRMS(음이온)",
  "conditions": {"instrument": "Ultimate 3000 UHPLC(4원 펌프, PDA 검출기) + Q-Exactive Focus 사중극자-오비트랩 질량분석기", "column": "Kinetex 150 × 4.6 mm, 5 µm (Phenomenex)", "mobile_phase": "A 0.1% 포름산 수용액, B 0.1% 포름산 아세토니트릴", "gradient": "15% B → 25분 40% B → 30분 100% B, 35분까지 유지", "flow": "0.8 mL/min", "temp": "", "detection": "PDA(정량 파장은 본문에 없음); HESI 음이온, 분무 전압 2.5 kV, 모세관 350 °C, 전체 스캔 m/z 120–1200(분해능 70,000)", "injection": "2 μL", "sample_prep": "분쇄 잎 100 mg + 용매 2 mL(물, 30·70·100% 에탄올), 초음파 10분(30 °C), 13,000 rpm 5분 원심분리 후 상층액", "standard": "카페산·카르노솔·살비아놀산 B·스쿠텔라린·로즈마린산·카르노신산(Extrasynthese); 1 mg/mL 원액을 희석해 검량선 작성", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "로즈마린산이 물 추출물을 뺀 모든 추출물에서 가장 많은 성분이자 주된 항산화 성분이고, 카르노신산·카르노솔이 가장 많은 테르페노이드라 지표로 쓰임; 전문 확인, 정량 파장·직선성·LOD·LOQ·회수율은 본문에 없음[2].",
  "source": [2], "url": "https://doi.org/10.1038/s41598-023-49695-w", "source_kind": "paper"},
 {"role": "literature", "compound": "Rosmarinic acid", "compound_ko": "로즈마린산(페놀 표준품 26종 동시 분석)",
  "part": "지상부(튀르키예 물라 주 아키아카 야생 채취, 그늘 건조)",
  "content": "메탄올 침지 추출물 169.7 ± 0.51 μg/g, 초음파 추출물 135.1 ± 0.40 μg/g, 구연산·포도당 공융용매 추출물 28.58 ± 0.46 μg/g; 루틴 21.36 ± 0.31 μg/g(메탄올)[3]",
  "method": "HPLC-DAD(280 nm)",
  "conditions": {"instrument": "Shimadzu 20 AT 시리즈 HPLC-DAD", "column": "역상 C18, 원문 표기 'Intersil ODS-3'(규격은 본문에 없음)", "mobile_phase": "A 0.5% 아세트산 수용액, B 0.5% 아세트산 메탄올", "gradient": "0–0.01분 0–10% B; 0.01–5분 10–20%; 5–15분 20–30%; 15–25분 30–50%; 25–30분 50–65%; 30–40분 65–75%; 40–50분 75–90%; 50–55분 90–10% B", "flow": "1.0 mL/min", "temp": "", "detection": "DAD 280 nm, 표준품과 UV 스펙트럼·머무름 시간 대조", "injection": "20 μL", "sample_prep": "추출물을 물:메탄올(80:20)에 녹여 0.20 μm 필터로 거름", "standard": "페놀 표준품 26종(갈산·로즈마린산·루틴 등), 검량선으로 정량; 결과는 μg/g 건조중량", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "세 추출법 모두에서 로즈마린산이 가장 많은 페놀이라 추출법 비교의 지표로 쓰임; 전문 확인, 칼럼 규격·직선성·LOD·LOQ·회수율은 본문에 없음[3].",
  "source": [3], "url": "https://doi.org/10.1002/fsn3.4580", "source_kind": "paper"},
 {"role": "literature", "compound": "alpha-Thujone", "compound_ko": "α-투존(1,8-시네올·캠퍼 등 정유 성분)",
  "part": "잎(튀르키예 내륙 에게 지역 시험포 1년생, 개화 초기, 신선·건조)",
  "content": "잎 정유 중 α-투존 최대 16.66%(신선)·17.19%(건조), 1,8-시네올 8.36–12.45%, 캠퍼 9.44–13.28%(면적 %); 정유 함량 신선 잎 0.42–0.50%, 말린 잎 1.2–1.52%[4]",
  "method": "GC/FID-MS(면적 정규화 %)",
  "conditions": {"instrument": "Shimadzu GC-MS QP2010 SE (GC/FID-MS)", "column": "TRB-WAX (Teknokroma), 60 m × 0.320 mm, 막 두께 0.25 μm", "mobile_phase": "헬륨(99.999%) 운반 기체", "gradient": "70 °C 5분 유지 → 3 °C/min로 160 °C, 10분 유지 → 6 °C/min로 250 °C, 20분 유지", "flow": "2.06 mL/min", "temp": "주입구·검출기·이온원 250 °C", "detection": "FID + EI 70 eV, m/z 35–550", "injection": "1 µL, 분할 40:1", "sample_prep": "잎 50 g을 물(1:10)과 클레벤저형 장치로 1–5시간 수증기 증류, 무수 황산나트륨 탈수; 정유를 n-헥산에 1:50 희석", "standard": "C–C 알케인 혼합물로 머무름 지수 계산, NIST·Wiley 라이브러리 대조; 개별 감응 계수 미적용", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "투존은 안전성 관리가 필요한 성분이고 이 시료에서 가장 많은 정유 성분이어서 지표로 볼 수 있음; 상대 면적 %이며 절대 정량이 아님; 전문 확인[4].",
  "source": [4], "url": "https://doi.org/10.1038/s41598-026-42109-7", "source_kind": "paper"},
]

d = {
 "slug": "salvia-triloba", "name_ko": "그릭세이지", "name_en": "Greek sage",
 "scientific_name": "Salvia triloba L.f. (= Salvia fruticosa Mill.)",
 "aliases": ["그릭세이지잎", "Greek sage", "Salvia fruticosa Mill.", "Salvia fruticosa", "Salvia triloba L.F.", "Anatolian sage", "Three-lobed sage", "East Mediterranean sage", "Cretan sage"],
 "sections": [{"key": k, "title": t, "body": b} for k, t, b in secs],
 "compounds": comps, "markers": [], "nutrients": [], "assays": assays,
 "production": [], "world": [], "gi": [], "orgs": [], "sources": S,
}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in d["sections"]:
    print(s["key"], len(s["body"]))
