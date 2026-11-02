import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
A = "2026-11-02"
def pm(title, cite, pmid, doi, note, pmc=None):
    ids = f"PMID {pmid}" + (f", {pmc}" if pmc else "")
    return {"title": f"{title} — {cite} ({ids}, {note})", "url": f"https://doi.org/{doi}" if doi else f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/", "publisher": "PubMed", "accessed": A}
S = [
 {"title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 영귤(Citrus sudachi Hort. ex Shiriai): 영귤열매·영귤분말·동결건조영귤, 사용가능, 사용가능부위: 열매 (로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json)", "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
 {"title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 같은 속 대조 행: 유자(Citrus junos; 열매·씨앗 사용가능, 유자나무잎 제한적사용), 의창지열매(Citrus ichangensis), 한라봉(학명란에 'Citrus sphaerocarpa Tanaka nom. nud.' 병기) (로컬 원자료 I1020_20261013.json)", "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
 pm("Hybrid origins of citrus varieties inferred from DNA marker analysis of nuclear and organelle genomes", "PLoS One 2016;11(11):e0166969", "27902727", "10.1371/journal.pone.0166969", "전문 확인", "PMC5130255"),
 pm("Sudachi peel extract powder including the polymethoxylated flavone sudachitin improves visceral fat content in individuals at risk for developing diabetes", "Food Sci Nutr 2021;9(8)", "34401059", "10.1002/fsn3.2339", "전문 확인", "PMC8358332"),
 pm("Sudachitin, a polymethoxylated flavone, improves glucose and lipid metabolism by increasing mitochondrial biogenesis in skeletal muscle", "Nutr Metab (Lond) 2014;11:32", "25114710", "10.1186/1743-7075-11-32", "전문 확인", "PMC4128574"),
 pm("Extracts of citrus Sudachi peel attenuate body weight gain in C57BL/6 mice fed a high-fat diet", "J Med Invest 2017;64(1.2):20-23", "28373623", "10.2152/jmi.64.20", "초록 확인"),
 pm("Chemical constituents from the peels of Citrus sudachi", "J Nat Prod 2006;69(8):1177-9", "16933871", "10.1021/np060217s", "초록 확인"),
 pm("Limonoids from Citrus sudachi", "Chem Pharm Bull 2001;49(5):649-51", "11383626", "10.1248/cpb.49.649", "초록 확인"),
 pm("Sudachitin, a polymethoxyflavone from Citrus sudachi, suppresses lipopolysaccharide-induced inflammatory responses in mouse macrophage-like RAW264 cells", "Biosci Biotechnol Biochem 2012;76(3):598-600", "22451408", "10.1271/bbb.110800", "초록 확인"),
 pm("Citrus peel polymethoxyflavones, sudachitin and nobiletin, induce distinct cellular responses in human keratinocyte HaCaT cells", "Biosci Biotechnol Biochem 2018;82(12):2064-2071", "30185129", "10.1080/09168451.2018.1514246", "초록 확인"),
 pm("Sudachitin, a polymethoxyflavone from Citrus sudachi, induces apoptosis via the regulation of MAPK pathways in human keratinocyte HaCaT cells", "Biochem Biophys Res Commun 2019;519(2):344-350", "31514996", "10.1016/j.bbrc.2019.09.010", "초록 확인"),
 pm("Citrus sudachi peel extract suppresses cell proliferation and promotes the differentiation of keratinocytes through inhibition of the EGFR-ERK signaling pathway", "Biomolecules 2020;10(10):1468", "33096942", "10.3390/biom10101468", "전문 확인", "PMC7589747"),
 pm("Methanol extraction fraction from Citrus Sudachi peel exerts lipid reducing effects in cultured cells", "J Med Invest 2018;65(3.4):225-230", "30282865", "10.2152/jmi.65.225", "초록 확인"),
 pm("[Metabolic beneficial effects of Citrus Sudachi] (일본어)", "Nihon Yakurigaku Zasshi 2020", "32612032", "10.1254/fpj.20025", "초록 확인"),
 pm("Identification and characterization of volatile components of the Japanese sour citrus fruit Citrus nagato-yuzukichi Tanaka", "Biosci Biotechnol Biochem 2008;72(7):1965-8", "18603776", "10.1271/bbb.80144", "초록 확인"),
 pm("Composition and monthly changes of the volatile constituents in the sour Hetsuka-daidai citrus peel", "J Oleo Sci 2020", "32493886", "10.5650/jos.ess19296", "초록 확인"),
 pm("Neurite outgrowth-promoting furanocoumarins isolated from sudachi juice in PC12 cells", "Biosci Biotechnol Biochem 2026", "42335944", "10.1093/bbb/zbag092", "초록 확인"),
 pm("[Food-dependent exercise-induced anaphylaxis due to ingestion of mikan (Citrus unshiu)] (일본어)", "Arerugi 2017;66(8):1011-1015", "28904280", "10.15036/arerugi.66.1011", "초록 확인"),
 pm("Antibacterial activity of citrus fruit juices against Vibrio species", "J Nutr Sci Vitaminol 2006;52(2):157-60", "16802698", "10.3177/jnsv.52.157", "초록 확인"),
 pm("Japanese citrus fruit (sudachi) juice is associated with increased bioavailability of calcium from whole small fish and suppressed bone resorption in rats", "J Nutr Sci Vitaminol 2004;50(3):177-83", "15386930", "10.3177/jnsv.50.177", "초록 확인"),
 pm("Effect of anions or foods on absolute bioavailability of calcium from calcium salts in mice by pharmacokinetics", "J Exp Pharmacol 2013;5:65-71", "27186137", "10.2147/JEP.S49668", "초록 확인", "PMC4863542"),
 pm("Ultraviolet light-emitting diode (UV-LED) sterilization of citrus bacterial canker disease targeted for effective decontamination of Citrus sudachi fruit", "Biocontrol Sci 2022;27(1):1-", "35314556", "10.4265/bio.27.1", "초록 확인"),
 pm("Polymethoxylated flavone sudachitin is a safe anticancer adjuvant that targets glycolysis in cancer-associated fibroblasts", "Oncol Lett 2022;24(1)", "35720469", "10.3892/ol.2022.13356", "전문 확인", "PMC9185147"),
 pm("The flavonoid Sudachitin regulates glucose metabolism via PDE inhibition", "Heliyon 2024;10(16):e35978", "39224336", "10.1016/j.heliyon.2024.e35978", "초록 확인", "PMC11367099"),
 pm("The polymethoxyflavone sudachitin modulates the circadian clock and improves liver physiology", "Mol Nutr Food Res 2023", "36829302", "10.1002/mnfr.202200270", "초록 확인"),
 pm("Gut-brain axis modulation by sudachi peel extract enhances resilience to chronic social defeat stress in mice", "J Affect Disord 2025", "40189061", "10.1016/j.jad.2025.04.027", "초록 확인"),
 pm("Essential oil of Citrus sudachi suppresses T cell activation both in vitro and in vivo", "J Nutr Sci Vitaminol 2022;68(6):513-", "36596549", "10.3177/jnsv.68.513", "초록 확인"),
 pm("Small RNA sequencing analysis identified miR159a as a novel candidate for activity in plant-derived nanovesicles from limon, hassaku, and sudachi", "Sci Rep 2026", "41803186", "10.1038/s41598-026-38951-4", "초록 확인", "PMC12979852"),
 pm("Therapeutic overview of sudachitin (총설)", "J Biochem Mol Toxicol 2024", "39392135", "10.1002/jbt.70003", "초록 확인"),
 pm("Chronotropic and inotropic effects of sudachitin, a polymethoxyflavone from the peel of Citrus sudachi on isolated rat atria and its underlying mechanisms", "Biol Pharm Bull 2024", "39647904", "10.1248/bpb.b24-00575", "초록 확인"),
 pm("Inhibitory effects of citrus fruits on the mutagenicity of 1-methyl-1,2,3,4-tetrahydro-beta-carboline-3-carboxylic acid treated with nitrite in the presence of ethanol", "Mutat Res 1998;415(3):219-26", "9714813", "10.1016/s1383-5718(98)00079-5", "초록 확인"),
 pm("Sudachitin and nobiletin stimulate lipolysis via activation of the cAMP/PKA/HSL pathway in 3T3-L1 adipocytes", "Foods 2023;12(10):1947", "37238764", "10.3390/foods12101947", "초록 확인", "PMC10217623"),
 pm("Three newly identified lipophilic flavonoids in Tanacetum parthenium supercritical fluid extract penetrating the blood-brain barrier", "J Pharm Biomed Anal 2018;149:488-493", "29182998", "10.1016/j.jpba.2017.11.029", "초록 확인"),
 pm("Sudachitin, polymethoxyflavone from Citrus sudachi, enhances antigen-specific cellular and humoral immune responses in BALB/c mice", "J Clin Biochem Nutr 2019;64(2):158-163", "30936628", "10.3164/jcbn.18-70", "초록 확인", "PMC6436041"),
]
for i, s in enumerate(S, 1):
    s["n"] = i
S = [{"n": s["n"], "title": s["title"], "url": s["url"], "publisher": s["publisher"], "accessed": s["accessed"]} for s in S]

sections = [
 {"key": "overview", "title": "한눈에 보기", "body":
  "영귤(Citrus sudachi Hort. ex Shirai)은 운향과 귤속의 신맛 나는 작은 감귤로, 일본에서는 '스다치(sudachi)'라 부르며 도쿠시마현의 특산 과일이다[5][6]. 일본에서 소비되는 스다치의 98% 이상이 도쿠시마현에서 생산된다고 보고되었다[6]. 주로 즙을 짜서 일본 음식의 양념으로 쓰고, 열매가 작아 즙을 짜고 남는 껍질 찌꺼기가 지역 산업의 과제가 되어 왔다[14].\n\n"
  "식품의약품안전처 「식품원료 목록」에서 영귤은 '사용가능' 원료이며, 사용 조건은 '사용가능부위 : 열매'이다[1]. 목록에는 영귤열매·영귤분말·동결건조영귤 3개 원료명이 같은 학명으로 올라 있고, 학명은 'Citrus sudachi Hort. ex Shiriai'로 적혀 있다[1]. 논문들은 명명자를 'Hort. ex Shirai'로 적어, 목록 표기와 철자가 한 글자 다르다[3][5]. 국문명 '영귤'과 학명의 대응은 이 목록 원자료로 확인했으며, 국가표준식물목록의 국명은 확인하지 못함.\n\n"
  "껍질에는 폴리메톡시플라본인 수다치틴(sudachitin)과 3'-데메톡시수다치틴이 들어 있고, 이 두 성분은 껍질 성분 중 항균 활성이 가장 강했다[7]. 사람 시험은 껍질 추출 분말(수다치틴 하루 4.9 mg)을 12주 먹인 41명 규모의 무작위 대조 시험이 있으며, 내장지방/피하지방 비율만 위약보다 유의하게 줄었다[4]."},
 {"key": "history", "title": "역사와 전통적 이용", "body":
  "스다치는 일본 요리(와쇼쿠)에서 즐겨 쓰는 신맛 양념이며, 어떤 이유에서인지 도쿠시마와 그 주변 지역에서만 잘 자란다고 소개된다[14]. 도쿠시마현은 스다치로 유명하며, 이 과일이 전통 식단에 쓰여 왔다는 점이 수다치틴 연구의 출발점으로 언급된다[29]. 일본에서는 연간 약 8,000 t이 생산되고, 그 절반 정도는 생과로 팔리고 나머지는 즙으로 가공된다고 보고되었다[5].\n\n"
  "생선 요리에 곁들이는 쓰임과 관련해, 스다치 즙으로 만든 소스는 장염비브리오균(Vibrio parahaemolyticus)에 강한 살균 효과를 보였고 그 주된 원인은 시트르산이었다[19]. 말린 잔멸치(시라스보시)에 스다치 즙을 더한 먹이를 흰쥐에 14일 먹인 실험에서 칼슘·마그네슘 흡수율이 높아졌다[20]. 간장 속 돌연변이원 전구물질을 아질산과 반응시킨 시험관 실험에서 스다치·레몬·유자를 넣으면 돌연변이성이 줄었고, 껍질 겉층이 즙보다 효과가 컸다[31].\n\n"
  "일본 식물학자 다나카는 스다치를 유자에서 생긴 자연 잡종으로 보았고, 스윙글은 이창지(C. ichangensis)와 귤의 잡종(Ichandarin)으로 보았다고 정리되었다[3]. 한국에서 영귤을 먹어 온 역사 기록은 확인하지 못함."},
 {"key": "biology", "title": "식물학적 특징", "body":
  "영귤(스다치)은 상록성 나무로, 주로 일본 도쿠시마현에서 자란다[5][13]. 열매는 작으며[14], 연구용 수다치틴 추출에는 9월에 도쿠시마에서 거둔 초록 껍질이 쓰였다[5]. 즙을 짜 쓰는 신맛 감귤(향산감귤)로 분류되며, 즙의 주된 유기산은 시트르산이다[12][19].\n\n"
  "열매 껍질 메탄올 추출물에서는 새 화합물 5종과 알려진 화합물 27종이 분리되었다[7]. 씨앗에서는 새 리모노이드 4종(1-O-메틸이창겐신, 수다치노이드 A·B·C)과 이창겐신·오바쿠논·오바쿠논산·리모닌이 분리되었다[8]. 즙에서는 푸라노쿠마린인 비아칸젤리신·이소핌피넬린과 플라본인 데메톡시수다치틴이 분리되었다[17].\n\n"
  "껍질 정유는 모노테르펜 탄화수소가 주를 이루는 나가토유즈키치(C. nagato-yuzukichi) 정유와 조성 양상이 꽤 비슷했지만, 전자코 주성분 분석에서는 두 정유가 서로 다른 방향으로 갈렸다[15]. 같은 분석에서 유자와 카보스(C. sphaerocarpa) 정유는 스다치 쪽과 뚜렷이 떨어져 위치했다[15]. 꽃·잎의 형태, 개화 시기, 열매 무게에 관한 공식 자료는 확인하지 못함."},
 {"key": "related_species", "title": "가까운 종과 혼동 주의", "body":
  "DNA 표지 분석은 스다치가 유자를 꽃가루 부모로 하는 잡종이라는 다나카의 견해를 뒷받침했다[3]. 스다치의 세포질(엽록체·미토콘드리아) 유형은 일본 재래 감귤 '고지(koji)'와 같은 C18형이었지만, 고지나 같은 유형의 다른 품종이 씨앗 부모로 추정되지는 않아 씨앗 부모는 밝혀지지 않았다[3]. 같은 연구는 기즈·하나유도 유자와 다른 품종의 잡종으로 추정했다[3].\n\n"
  "이처럼 유자(Citrus junos)와 가깝기 때문에 자료를 섞지 않도록 주의해야 한다[3]. 식품원료 목록에서 유자는 따로 올라 있으며 열매·씨앗은 사용가능, 유자나무잎은 제한적사용으로 영귤과 조건이 다르다[1][2]. 카보스(C. sphaerocarpa)는 스다치와 따로 다뤄지는 일본의 다른 신맛 감귤이며, 정유 분석에서 스다치와 구별되었다[15][16]. 식품원료 목록에서는 한라봉 행의 학명란에 'Citrus sphaerocarpa Tanaka nom. nud.'가 함께 적혀 있어, 카보스 학명으로 검색하면 한라봉이 걸릴 수 있다[2].\n\n"
  "수다치틴은 스다치에서 처음 이름이 붙었지만 감귤만의 성분은 아니며, 화란국화(Tanacetum parthenium) 같은 국화과 식물 추출물에서도 확인되었다[33]. 따라서 '수다치틴 함유' 원료라도 원재료가 영귤인지 따로 확인해야 한다[33]."},
 {"key": "cultivation", "title": "재배와 생산", "body":
  "일본에서 스다치는 연간 약 8,000 t이 생산되며, 즙을 짜고 남는 찌꺼기가 해마다 약 200 t에 이른다고 보고되었다[5]. 일본 소비량의 98% 이상이 도쿠시마현산이다[6]. 생산량의 절반가량은 생과로, 나머지는 즙 같은 가공품으로 소비된다[12].\n\n"
  "스다치는 여러 나라로 수출되는데, 유럽에는 없는 감귤 궤양병균이 붙어 있을 가능성 때문에 수출 전 차아염소산나트륨 수용액으로 소독해야 한다[22]. 이 소독 작업이 번거로워 자외선 LED 살균이 시험되었고, 265–365 nm 여섯 파장 중 짧은 파장이 감귤 궤양병균 살균에 더 효과적이었다[22].\n\n"
  "스다치 껍질의 건강 기능 연구를 위해 산감귤 공동 연구 협의체가 꾸려졌다고 소개되었다[14]. 통계청·농림축산식품부 통계에서 영귤의 국내 재배 면적과 생산량은 확인하지 못함. 제주 등 국내 재배 현황도 공식 자료로는 확인하지 못함."},
 {"key": "processing", "title": "가공과 이용", "body":
  "식품원료 목록에는 열매 그대로의 영귤열매 외에 가루로 만든 영귤분말과 동결건조영귤이 원료명으로 올라 있다[1]. 열매껍질만을 따로 이르는 원료명은 영귤 행에서 확인하지 못함.\n\n"
  "사람 시험에 쓰인 껍질 추출 분말은 수다치틴을 1.4% 함유했고, 하루 섭취량(1,050 mg, 수다치틴 4.9 mg)은 스다치 열매 1/3개에 해당한다고 설명되었다[4]. 이 분말에는 나리루틴 0.7%, 나린진 0.5%가 들어 있었고 하루 헤스페리딘 섭취량은 12.5 mg이었다[4]. 캡슐에는 플라보노이드 안정화를 위해 γ-사이클로덱스트린이 함께 들어갔다[4].\n\n"
  "실험실에서는 말린 껍질 100 g을 메탄올·물로 마이크로파 추출해 수다치틴 0.092 g을 얻고, 남은 수용성 층을 산 가수분해해 0.376 g을 더 얻었다(HPLC 순도 95% 이상)[5]. 쥐 실험에서는 스다치 즙이 칼슘의 장내 체류 시간을 늘려 염화칼슘의 칼슘 흡수율을 2.86배 높였다(동물 시험)[21]. 식약처 「식품 등의 생산실적」에서 영귤 원료 건강기능식품 생산 기록은 확인하지 못함.\n\n"
  "껍질 추출물과 수다치틴의 대사 관련 작용은 대부분 세포·동물 결과다: 지방세포의 지방분해 촉진[32], 생쥐의 인슐린 분비 증가(PDE 억제)[24], 고지방식 생쥐의 생체시계·간 대사 개선[25], 사회적 패배 스트레스 생쥐의 장내미생물 변화[26]가 보고되었다."},
 {"key": "genetics", "title": "유전 정보와 종 판별", "body":
  "핵 유전체 SSR·indel 표지와 세포질 표지로 일본 재래 감귤 101품종을 분석한 연구에서, 스다치는 유자와 부모–자식 관계를 보이는 품종 중 하나로 확인되었다[3]. 이 연구는 스다치의 세포질 유형이 고지형(C18)이고, 고지·다치바나-C·스다치의 미확인 부모가 같거나 매우 가까울 수 있다고 해석했다[3]. 구조 분석에서 스다치는 만다린 계통과 그 자손으로 해석된 군집에 들어갔다[3].\n\n"
  "레몬·하삭·스다치에서 얻은 식물 유래 나노소포체의 소형 RNA를 차세대 염기서열 분석으로 비교한 결과, 세 감귤에서 모두 158개 miRNA가 확인되었고 77개가 공통으로 발현되었다[28]. 그중 miR159a의 판독 수가 가장 많았다[28].\n\n"
  "스다치의 엽록체 전체 유전체, 핵 유전체 해독, 염색체 수에 관한 자료는 확인하지 못함. 영귤 가공품의 진위를 가리는 공인 DNA 판별법도 확인하지 못함."},
 {"key": "safety", "title": "안전성", "body":
  "식약처 목록은 영귤의 열매만 식품원료로 허용한다[1]. 공공기관의 영귤 알레르기·잔류농약·독성 성분 정보는 확인하지 못함. 감귤(온주밀감)으로 운동 유발 아나필락시스가 생긴 12세 어린이 증례에서 스다치를 포함한 여러 감귤의 피부단자시험이 모두 양성이어서 감귤류 사이 교차반응 가능성이 제시되었다[18].\n\n"
  "12주 사람 시험(수다치틴 하루 4.9 mg)에서는 이상 반응이 기록되지 않았고 ALT·AST·크레아티닌도 위약군과 차이가 없었다[4]. 다만 대상이 41명으로 적고 정제 추출물 시험이라 열매를 먹는 경우와 같지 않다[4]. 수다치틴은 50 µM에서 정상 섬유모세포 증식을 억제하지 않았으나, 이는 세포 실험 결과다[23]. 쥐 심방 실험에서는 수다치틴(0.3–30 µM)이 심박수와 수축력을 농도에 따라 높였다(동물 조직 실험)[30].\n\n"
  "스다치 즙에서 비아칸젤리신·이소핌피넬린 같은 푸라노쿠마린이 분리되었다[17]. 그러나 스다치(영귤)의 약물대사효소(CYP3A 등) 억제나 약물 상호작용을 직접 조사한 연구는 확인하지 못함. 면역 쪽에서는 껍질 정유가 생쥐의 항원 특이 T세포 반응을 억제했고[27], 수다치틴은 오히려 난알부민 특이 IgE·IgG1 생성을 늘렸다(동물)[34]. 수다치틴 30 µM은 사람 각질세포주에서 세포자멸사를 일으켰다(세포)[10–12]."},
]

compounds = [
 {"name": "Sudachitin", "name_ko": "수다치틴(5,7,4'-트라이하이드록시-6,8,3'-트라이메톡시플라본)", "class": "폴리메톡시플라본", "role": "marker", "part": "열매껍질", "content_text": "말린 껍질 100 g에서 유리형 0.092 g + 산 가수분해 후 0.376 g 분리(HPLC 순도 95% 이상)[5]; 껍질 추출 분말 중 1.4%[4]", "activity_ko": "고지방식 생쥐에서 체중 증가·이상지질혈증 개선(동물)[5]; 대식세포 NO 생성 억제(세포)[9]; 사람 시험에서 추출 분말(하루 4.9 mg)로 내장/피하지방 비율 감소[4]", "source": [4, 5, 9]},
 {"name": "3'-Demethoxysudachitin", "name_ko": "3'-데메톡시수다치틴", "class": "폴리메톡시플라본", "role": "bioactive", "part": "열매껍질·즙", "content_text": "함량 확인하지 못함(껍질에서 분리[7], 즙에서 분리[17])", "activity_ko": "MRSA·헬리코박터 파일로리에 수다치틴과 함께 가장 강한 항균 활성(시험관)[7]; PC12 세포 신경돌기 신장 촉진(세포)[17]", "source": [7, 17]},
 {"name": "Hesperidin", "name_ko": "헤스페리딘", "class": "플라바논 배당체", "role": "bioactive", "part": "열매껍질", "content_text": "껍질 추출 분말 하루 섭취분 중 12.5 mg[4]; 수용성 껍질 추출물에서 HPLC로 확인[12]", "activity_ko": "껍질 추출물의 각질세포 ERK 억제 효과를 단독으로는 재현하지 못함(세포)[12]", "source": [4, 12]},
 {"name": "Narirutin", "name_ko": "나리루틴", "class": "플라바논 배당체", "role": "bioactive", "part": "열매껍질", "content_text": "껍질 추출 분말 중 0.7%[4]", "activity_ko": "수용성 껍질 추출물의 페놀 성분으로 HPLC 확인, 단독으로는 ERK 억제 없음(세포)[12]", "source": [4, 12]},
 {"name": "Naringin", "name_ko": "나린진", "class": "플라바논 배당체", "role": "bioactive", "part": "열매껍질", "content_text": "껍질 추출 분말 중 0.5%[4]", "activity_ko": "수용성 껍질 추출물의 페놀 성분으로 HPLC 확인, 단독으로는 ERK 억제 없음(세포)[12]", "source": [4, 12]},
 {"name": "Byakangelicin", "name_ko": "비아칸젤리신", "class": "푸라노쿠마린", "role": "bioactive", "part": "즙", "content_text": "즙에서 분리, 함량 확인하지 못함[17]", "activity_ko": "PC12 세포 신경돌기 신장 촉진 활성이 시험한 푸라노쿠마린 중 가장 강한 편(세포)[17]", "source": [17]},
 {"name": "Isopimpinellin", "name_ko": "이소핌피넬린", "class": "푸라노쿠마린", "role": "bioactive", "part": "즙", "content_text": "즙에서 분리, 함량 확인하지 못함[17]", "activity_ko": "PC12 세포 신경돌기 신장 촉진(세포)[17]", "source": [17]},
 {"name": "Limonin", "name_ko": "리모닌", "class": "리모노이드", "role": "bioactive", "part": "씨앗", "content_text": "씨앗에서 분리, 함량 확인하지 못함[8]", "activity_ko": "활성은 이 출처에서 확인하지 못함[8]", "source": [8]},
 {"name": "Obacunone", "name_ko": "오바쿠논", "class": "리모노이드", "role": "bioactive", "part": "씨앗", "content_text": "씨앗에서 분리, 함량 확인하지 못함[8]", "activity_ko": "활성은 이 출처에서 확인하지 못함[8]", "source": [8]},
 {"name": "Ichangensin", "name_ko": "이창겐신", "class": "리모노이드", "role": "bioactive", "part": "씨앗", "content_text": "씨앗에서 이창겐신과 새 유도체 1-O-메틸이창겐신 분리[8]", "activity_ko": "활성은 이 출처에서 확인하지 못함[8]", "source": [8]},
 {"name": "Citric acid", "name_ko": "시트르산", "class": "유기산", "role": "nutrient", "part": "즙", "content_text": "즙의 주된 유기산(함량 수치 확인하지 못함)[19]", "activity_ko": "장염비브리오균 생육 억제의 주원인; pH를 높인 소스에서는 살균 효과가 사라짐(시험관)[19]", "source": [19]},
]

assays = [
 {"role": "literature", "compound": "Sudachitin", "compound_ko": "수다치틴(헤스페리딘·나린진·나리루틴 동시 확인)", "part": "열매껍질 수용성 추출물(30% 1,3-부틸렌글라이콜)",
  "content": "3% 추출물 희석액 중 수다치틴 0.46 µM[12]", "method": "역상 HPLC-UV(340 nm)",
  "conditions": {"instrument": "", "column": "Wakosil-5C18RS, 4.6 × 250 mm", "mobile_phase": "A: 아세토니트릴/50 mM 인산이수소나트륨(pH 2.3) 12:88, B: 같은 용액 60:40", "gradient": "0–5분 A 100%, 5–21분 B 40%까지 직선, 21–23분 B 40%, 23–45분 B 100%까지 직선, 45–64분 B 100%, 65–70분 A 100%로 복귀", "flow": "1.0 mL/min", "temp": "40 °C", "detection": "UV 340 nm(머무름 시간·UV 스펙트럼을 표준품과 대조)", "injection": "10 µL", "sample_prep": "추출물을 메탄올/DMSO(1:1)와 3 N HCl과 섞어 70 °C 1시간 반응 후 0.45 µm 막으로 거름", "standard": "헤스페리딘·나린진·나리루틴·수다치틴 표준품", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "수다치틴은 이 종 껍질에서 이름 붙은 특징적 폴리메톡시플라본으로, 껍질 추출물 연구에서 지표로 정량되었다; 전문 Methods에서 조건을 옮겼고 검출·정량한계와 회수율은 기재되지 않음[12]", "source": [12], "url": "https://doi.org/10.3390/biom10101468", "source_kind": "paper"},
 {"role": "literature", "compound": "Sudachitin", "compound_ko": "수다치틴(나리루틴·나린진·헤스페리딘 함량 병기)", "part": "열매껍질 추출 분말(사람 시험용 캡슐 원료)",
  "content": "수다치틴 1.4%(하루 4.9 mg), 나리루틴 0.7%, 나린진 0.5%, 헤스페리딘 하루 12.5 mg[4]", "method": "분석법 기재 없음",
  "conditions": {},
  "rationale": "사람 시험 원료의 규격 지표로 수다치틴 함량을 표시했다; 전문을 확인했으나 분석 조건은 본문에 없고 보충 자료에 성분표가 있다고만 적혀 있음[4]", "source": [4], "url": "https://doi.org/10.1002/fsn3.2339", "source_kind": "paper"},
]

world = [
 {"country": "일본", "metric": "production_t", "year": 2014, "value": 8000, "unit": "t", "note": "'연간 약 8,000 t' — 2014년 논문 서론의 서술로 통계 기준 연도는 미기재; 찌꺼기 약 200 t/년[5]. 일본 소비량의 98% 이상이 도쿠시마현산[6]", "source": [5, 6]},
]

d = {
 "slug": "citrus-sudachi", "name_ko": "영귤", "name_en": "Sudachi",
 "scientific_name": "Citrus sudachi Hort. ex Shirai",
 "aliases": ["스다치", "영귤열매", "영귤분말", "동결건조영귤", "sudachi", "Citrus sudachi Hort. ex Shiriai"],
 "sections": sections, "compounds": compounds, "markers": [], "assays": assays,
 "nutrients": [], "production": [], "world": world, "gi": [], "orgs": [], "sources": S,
}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
print("ok", len(S))
