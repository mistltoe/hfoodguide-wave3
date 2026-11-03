import json, pathlib
A = "2026-11-02"
def pm(title, doi, pub, pmid, pmc=None):
    return {"title": title, "url": f"https://doi.org/{doi}" if doi else f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
            "publisher": f"{pub}, PMID {pmid}" + (f", {pmc}" if pmc else ""), "accessed": A}
S = [
 {"title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 일본재첩 항목(별칭 가막조개)", "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
 pm("Genome assembly, gene content, and plastic gene expression responses to salinity changes in the Brackishwater Clam (Corbicula japonica) from a dynamic estuarine environment. J Hazard Mater 2024", "10.1016/j.jhazmat.2024.136627", "Journal of Hazardous Materials", "39616841"),
 pm("Growth retardation and suppression of ubiquitin-dependent catabolic processes in the brackish water clam Corbicula japonica in response to salinity changes and bioaccumulation of toxic heavy metals. Environ Pollut 2023", "10.1016/j.envpol.2023.122554", "Environmental Pollution", "37717895"),
 pm("Complete mitochondrial genome sequence of a brackish water clam (Cyrenidae: Bivalvia) collected from an estuary of Gwangyang Bay in Korea. Mitochondrial DNA B Resour 2022", "10.1080/23802359.2022.2122742", "Mitochondrial DNA Part B", "36147364", "PMC9487972"),
 pm("Phylogeography of the brackish water clam Corbicula japonica around the Japanese archipelago inferred from mitochondrial COII gene sequences. Zoolog Sci 2014;31:168", "10.2108/zsj.31.168", "Zoological Science", "24601779"),
 pm("Two Corbicula (Corbiculidae: Bivalvia) mitochondrial lineages are widely distributed in Asian freshwater environment. Mol Phylogenet Evol 2003;29:529-39", "10.1016/s1055-7903(03)00138-6", "Molecular Phylogenetics and Evolution", "14615191"),
 pm("Carotenoids in three species of Corbicula clams, Corbicula japonica, Corbicula sandai, and Corbicula sp. (Chinese freshwater corbicula clam). J Agric Food Chem 2005;53:8357-64", "10.1021/jf058088t", "Journal of Agricultural and Food Chemistry", "16218688"),
 pm("Structure of new carotenoids from corbicula clam Corbicula japonica. J Nat Prod 2005;68:1341-4", "10.1021/np058053n", "Journal of Natural Products", "16180810"),
 pm("A novel ornithine-containing tripeptide isolated from the extract of the brackish-water bivalve Corbicula japonica. Biochim Biophys Acta 2007;1770:790-6", "10.1016/j.bbagen.2006.12.010", "Biochimica et Biophysica Acta", "17293050"),
 pm("Influence of low-temperature processing of the brackish-water bivalve, Corbicula japonica, on the ornithine content of its extract. Biosci Biotechnol Biochem 2004;68:1228-34", "10.1271/bbb.68.1228", "Bioscience, Biotechnology, and Biochemistry", "15215585"),
 pm("Acorbine, a Corbicula japonica-derived tripeptide containing non-proteinogenic amino acids, suppresses ethanol-induced liver injury. Biochem Biophys Res Commun 2019", "10.1016/j.bbrc.2019.11.131", "Biochemical and Biophysical Research Communications", "31784088"),
 pm("Proximate Composition, Antioxidant Properties, and Hepatoprotective Activity of Three Species of Shellfish of the Pacific Coast of Russia. Molecules 2021;26:3397", "10.3390/molecules26113397", "Molecules (MDPI)", "34205146", "PMC8199966"),
 pm("Data on free amino acid contents in Japanese basket clams (Corbicula japonica) from Lake Abashiri and Abashirigawa River. Data Brief 2017", "10.1016/j.dib.2017.11.075", "Data in Brief", "29276741", "PMC5730376"),
 pm("Characterization of Selenium Species in the Shijimi Clam. Chem Pharm Bull 2017", "10.1248/cpb.c17-00492", "Chemical & Pharmaceutical Bulletin", "29093291"),
 pm("Dynamic changes in the accumulation of metabolites in brackish water clam Corbicula japonica associated with alternation of salinity. Comp Biochem Physiol B 2014", "10.1016/j.cbpb.2014.11.007", "Comparative Biochemistry and Physiology Part B", "25455471"),
 pm("Purification and some properties of alanine racemase from a bivalve mollusc Corbicula japonica. J Exp Zool 2001;289:1-9", "10.1002/1097-010x(20010101/31)289:1<1::aid-jez1>3.0.co;2-m", "Journal of Experimental Zoology", "11169488"),
 pm("A comparative study of cellulase and hemicellulase activities of brackish water clam Corbicula japonica with those of other marine Veneroida bivalves. J Exp Biol 2009;212:2812-8", "10.1242/jeb.031567", "Journal of Experimental Biology", "19684215"),
 pm("Molecular cloning of glycoside hydrolase family 45 cellulase genes from brackish water clam Corbicula japonica. Comp Biochem Physiol B 2009;152:390-6", "10.1016/j.cbpb.2009.01.010", "Comparative Biochemistry and Physiology Part B", "19266619"),
 pm("Detection of a proteinaceous toxin in the brackishwater clam (Corbicula japonica). Toxicon 1995;33:699-702", "10.1016/0041-0101(95)00017-g", "Toxicon", "7660374"),
 pm("Purification and properties of a proteinaceous toxin from the brackishwater clam (Corbicula japonica). Toxicon 2001;39:1061-7", "10.1016/s0041-0101(00)00249-x", "Toxicon", "11223096"),
 pm("Comparison between mouse bioassay and HILIC-MS/MS for quantification of paralytic shellfish toxin in Japanese basket clams and mussels caught off coastal Osaka Bay in Japan. Food Addit Contam A 2021", "10.1080/19440049.2021.1941301", "Food Additives & Contaminants Part A", "34320907"),
 pm("Detection of hepatitis E virus RNA from the bivalve Yamato-Shijimi (Corbicula japonica) in Japan. Am J Trop Med Hyg 2007;76:170-2", None, "American Journal of Tropical Medicine and Hygiene", "17255247"),
 pm("Evaluation of Heat Inactivation of Human Norovirus in Freshwater Clams Using Human Intestinal Enteroids. Viruses 2022;14:1014", "10.3390/v14051014", "Viruses (MDPI)", "35632754", "PMC9146323"),
 pm("The content of metals in organisms of various trophic levels in freshwater and brackish lakes on the coast of the sea of Japan. Environ Sci Pollut Res 2019", "10.1007/s11356-019-05198-8", "Environmental Science and Pollution Research", "31102221"),
 pm("Environmental risks of organic fertilizer with increased heavy metals (Cu and Zn) to aquatic ecosystems adjacent to farmland in the northern biosphere of Japan. Sci Total Environ 2023", "10.1016/j.scitotenv.2023.163861", "Science of the Total Environment", "37142019"),
 pm("Antioxidant capacity and carbon-based scope for growth of brackish water clams Corbicula japonica under the combined effects of natural and anthropogenic factors. Environ Pollut 2022", "10.1016/j.envpol.2022.119676", "Environmental Pollution", "35753544"),
 pm("Two-domain arginine kinases from the clams Solen strictus and Corbicula japonica: exceptional amino acid replacement of the functionally important D62 by G. Int J Biochem Cell Biol 2002;34:1221-9", "10.1016/s1357-2725(02)00050-x", "International Journal of Biochemistry & Cell Biology", "12127572"),
 pm("Purification, molecular cloning, and application of a novel sphingomyelin-binding protein (clamlysin) from the brackishwater clam, Corbicula japonica. Biochim Biophys Acta 2011;1811:323-32", "10.1016/j.bbalip.2011.02.004", "Biochimica et Biophysica Acta", "21396484"),
 pm("Comprehensive analysis of glycosaminoglycans from the edible shellfish. Carbohydr Polym 2018", "10.1016/j.carbpol.2017.12.076", "Carbohydrate Polymers", "29352919"),
 pm("Bioconcentration and biotransformation of [14C]methoxychlor in the brackish water bivalve Corbicula japonica. Xenobiotica 2011;41:818-25", "10.3109/00498254.2011.574164", "Xenobiotica", "21521078"),
 pm("[Seasonal characteristics of gametogenesis in the Corbicula japonica]. Tsitologiia 2006;48:149-52 (러시아어, 영문 초록)", None, "Tsitologiia", "16737182"),
 pm("Integrative genomic analyses reveal genetic structuring and cyto-nuclear incongruences within the Corbicula species complex in China. Mol Phylogenet Evol 2026;221:108624", "10.1016/j.ympev.2026.108624", "Molecular Phylogenetics and Evolution", "41985571"),
]
for i, s in enumerate(S, 1): s["n"] = i
sources = [{"n": s["n"], **{k: s[k] for k in ("title", "url", "publisher", "accessed")}} for s in S]

secs = [
("overview", "한눈에 보기",
"일본재첩(Corbicula japonica)은 재첩과(Cyrenidae) 재첩속에 드는 이매패류로, 강 하구처럼 바닷물과 민물이 섞이는 기수역에 산다[1, 2]. 식약처 「식품원료 목록」에는 대표 원료명 '일본재첩', 별칭 '가막조개'로 올라 있고, 학명 칸에는 Corbicula japonica와 함께 Corbicula fuscata atrata, Corbicula bifrons, Corbicula ovalis가 적혀 있다[1]. 식품원료로서의 지위는 '사용가능'이며, 원자료의 부위 칸은 '-'로 적혀 있고 별도의 사용 조건은 없다[1]. 같은 목록에서 재첩(Corbicula fluminea)과 참재첩(Corbicula leana)은 따로 등재된 별개의 원료다[1].\n\n일본에서는 '시지미(shijimi)'로 불리며 내수면 어업에서 가장 중요한 자원으로 소개되고, 국내에서도 식용과 내수면 어업에서 상업적으로 중요한 종으로 기술된다[4, 8, 17]. 먹는 부위의 추출물에는 유리 오르니틴과 오르니틴을 품은 트리펩타이드(아코르빈)가 들어 있고, 냉동 처리하면 추출물의 유리 오르니틴이 늘어난다고 보고되었다[9, 10]. 건강기능식품 고시형 원료의 원재료가 아니어서 식약처가 정한 지표성분은 없다[1]."),
("history", "이용 역사",
"일본에서는 예로부터 재첩 추출물이 간을 보호한다고 믿어져 왔다고 소개되지만, 어떤 성분이 그 역할을 하는지는 분명하지 않았다[11]. 이 종은 일본에서 가장 중요한 내수면 어업 자원으로 기술되며, 이바라키현 히누마호와 히누마강이 주요 어장의 예로 소개되었다[15, 17]. 홋카이도 아바시리호 일대의 기수호도 내수면 어업에 중요한 곳으로 기술되었다[25].\n\n일본의 가공 연구에서는 이 종을 얼리면 추출물의 오르니틴 함량이 늘어난다는 현상이 2004년에 보고되었고, 2007년에는 그 공급원으로 보이는 트리펩타이드 아코르빈이 분리되었다[9, 10]. 2019년에는 아코르빈이 생쥐의 알코올성 간 손상을 줄였다는 동물·세포 실험 결과가 나왔다[11]. 러시아 연구에서는 이 종의 열수 추출물 50 mg/kg을 쥐에게 먹인 뒤 사염화탄소로 간 손상을 일으키자 혈청 AST·ALT가 대조군보다 낮았는데, 이는 동물실험 결과로 사람에서의 효과는 확인하지 못함[12]. 국내에서는 광양만 하구의 이 종이 식용과 내수면 어업 자원으로 상업적으로 중요하다고 기술되었다[4]. 국내 이용 역사를 정리한 공식 자료는 확인하지 못함."),
("biology", "어종·형태·생태",
"일본재첩은 하구의 기수역에 사는 여과섭식 이매패류로, 염분이 시간과 장소에 따라 크게 바뀌는 환경에서 이온 농도와 삼투압을 빠르게 조절하며 산다[2, 4]. 이 종은 D-알라닌과 L-알라닌을 세포 안 삼투 조절 물질로 많이 쓰며, 외부 염분에 따라 그 양이 바뀌고 외투막에서 알라닌 라세미화효소가 정제되었다[16]. 히누마호와 히누마강 시료의 대사체 분석에서는 아가미보다 발 근육에 대사물이 많았고, 염분에 따라 β-알라닌·콜린·GABA·오르니틴·글리신 베타인 농도가 달라졌다[15].\n\n이 종은 부유물을 걸러 먹지만 육상 식물에서 온 유기물도 동화한다고 제안되었고, 바지락·백합류 등 다른 해산 이매패류보다 셀룰라아제·자일라나아제·만나나아제 활성이 뚜렷이 높았다[17]. 셀룰라아제는 공생균이 아니라 이 종의 소화샘 분비세포에서 만들어지는 것으로 보고되었다[18]. 생식소의 계절 변화를 본 연구에서는 7월에 산란이 시작되고 난자 형성이 8월 말까지 이어졌다[31]. 홋카이도 아바시리강은 이 종 분포의 북쪽 한계에 가깝다고 기술되었다[13]."),
("related_species", "관련 종·이름",
"식품원료 목록에서 일본재첩은 재첩(Corbicula fluminea), 참재첩(Corbicula leana)과 서로 다른 원료로 등재되어 있으며, 참재첩의 별칭에도 '가막조개'가 들어 있어 이름만으로는 종을 구분하기 어렵다[1]. 아시아 재첩속의 미토콘드리아 COI 분석에서는 기수형과 담수형이 뚜렷이 나뉘었고, 기수형 안에서도 일본·한국의 C. japonica와 중국의 기수형 집단 사이에 깊은 분화가 있었다[6]. 일본 열도 주변 283개체의 COII 분석에서는 계통 A–C가 일본과 사할린에, 계통 D·E와 별도의 Corbicula sp. 집단이 한반도에 분포했다[5].\n\n재첩속은 껍데기 형태 변이가 커서 분류가 매우 복잡하며, 어린 시기에는 형태만으로 종을 가리기 어렵다고 기술되었다[4]. 중국 재첩속 집단 연구에서도 한 무리가 기수성 종 C. aff. japonica로 추정되었다[32]. 성분 면에서도 기수에 사는 이 종은 페리디닌 계열이 주된 카로티노이드였던 반면, 담수에 사는 C. sandai와 중국 담수 재첩은 루테인이 주였다[7]. 이 문서의 성분·안전 수치는 모두 C. japonica 시료에서 나온 값만 적었다[7, 13, 14]."),
("cultivation", "서식·채취(어획)",
"이 종은 일본 전역의 강과 기수역에 살며, 히누마호처럼 바다에서 멀어 염분이 낮고 안정된 곳과 조석의 영향으로 염분이 매일 바뀌는 하류가 함께 어장이 된다[15]. 아바시리강의 이 종은 여름 한때만 채취되며, 연구에서는 6–7월과 11월에 호수 세 지역과 강 한 지점에서 시료를 잡았다[13]. 실험에서는 높은 수온과 먹이 공급이 성장 여력(C-SFG)을 높였고 높은 염분은 이를 낮췄으며, 하수 처리 조건에서는 대부분 성장 여력이 음수가 되었다[26].\n\n한국 광양만 하구에서는 염분과 중금속 축적이 높은 곳의 개체에서 단백질 분해 경로 유전자가 억제되었고, 이것이 성장 지연과 관련될 수 있다고 보고되었다[3]. 아바시리 일대 연구는 농경지 퇴비의 구리·아연이 이 종에 주는 위험을 평가해 현재 수준에서는 큰 위험이 없다고 보았다[25]. 국내 일본재첩만의 어획 통계와 일본의 종별 생산량은 확인하지 못함."),
("processing", "가공·이용",
"일본재첩은 냉동하면 추출물의 유리 오르니틴이 늘어나며, 이 현상은 냉동 기간과 무관했고 가리비·바지락·백합에서는 나타나지 않았다[10]. 4 ℃부터 −10 ℃까지 온도를 바꿔 본 결과 −4 ℃ 처리에서 오르니틴 함량이 가장 높았고, 처리 뒤 5 ℃나 15 ℃에 두면 증가분이 줄었다가 다시 −4 ℃로 처리하면 회복되었다[10]. 냉동 시 늘어나는 유리 β-알라닌과 오르니틴은 트리펩타이드 아코르빈이 분해되어 생기는 것으로 해석되었고, 두 성분의 총량은 처리 온도와 관계없이 일정했다[9].\n\n성분 연구에서는 껍데기째 1:1의 물을 부어 15분 끓인 열수 추출물이나 먹는 부위를 3.5% 소금물에 하룻밤 담가 해감한 뒤 분석하는 방법이 쓰였다[12, 13]. 90 ℃ 물에 넣었을 때 조갯살 중심이 90 ℃에 이르기까지 약 2분이 걸렸다[23]. 발 근육에서는 스핑고미엘린에 결합하는 단백질(클램라이신)이 정제되어 세포막 연구용 탐침으로 쓰일 가능성이 제시되었다[28]. 식약처 「식품 등의 생산실적」에서 이 종 원료의 제품 생산실적은 확인하지 못함."),
("genetics", "유전체·유전 연구",
"2024년에 일본재첩의 첫 고해상도 유전체와 전사체가 보고되었고, 다른 연체동물 11종과 비교해 신경 관련 유전자 무리가 크게 늘어난 것이 특징이었다[2]. 이 유전자들은 글루탐산·GABA·글루타민·글리신 회로와 관련되어 높은 염분에서 신경망 흥분에 관여할 가능성이 제시되었다[2]. 광양만 개체의 RNA 시퀀싱에서는 조립된 유전자 404,486개 가운데 5,534개가 서식 조건에 따라 다르게 발현되었다[3].\n\n광양만 하구 개체의 미토콘드리아 유전체는 17,432 bp로 단백질 암호 유전자 13개, rRNA 2개, tRNA 22개로 이루어지며 A+T 비율이 70.5%다[4]. 일본 열도 주변 집단의 COII 분석에서는 우세 계통 A가 태평양 쪽과 동해 쪽 집단으로 나뉘었고, 그 확장 시기는 중기 말 또는 후기 플라이스토세로 추정되었다[5]. 이 종의 아르기닌 인산화효소는 두 도메인이 이어진 약 80 kDa 구조로, 일반 효소에서 보존된 잔기가 바뀌어 있는 특이한 형태였다[27]. 소화샘에서 발현되는 GHF45 셀룰라아제 유전자도 클로닝되었다[18]."),
("safety", "안전성",
"일본재첩의 물 추출물을 생쥐 정맥에 주사하면 치사 작용이 있었고, 발 근육 등 근육 조직에서 가장 강했으며 그 원인은 열에 약한 단백질로 판단되었다[19]. 정제한 이 단백질 독소의 생쥐 정맥 주사 반수치사량은 11 µg/kg이었고 독성은 지역에 따라 달랐으나 계절·성별 차이는 없었다[20]. 이 결과는 주사 실험이며 먹었을 때의 위해를 보여 준 자료는 확인하지 못함.\n\n오사카만 연안의 이 종에서 마비성 패류독소가 검출되었으나 전체 독성은 함께 조사한 홍합류보다 낮았고, 주성분은 C1·C2와 곤야우톡신 1–4였다[21]. 일본 하천산 포장 제품 32개 가운데 2개에서 E형 간염 바이러스 유전자형 3의 RNA가 검출되었다[22]. 노로바이러스를 넣은 조갯살을 90 ℃에서 1분 이상 가열하자 감염성이 사라졌다는 실험 결과가 있다[23].\n\n러시아 동해 연안 호수 연구에서 이 종을 포함한 먹이사슬에서 납·아연·카드뮴·구리가 농축되지 않았다[24]. 메톡시클로르 노출 실험에서는 체내 농축계수가 2010이었으나 깨끗한 물로 옮기면 반감기 2.2일로 빠르게 빠져나갔다[30]. 이 종에 대한 공공기관의 알레르기·잔류 기준 정보는 확인하지 못함."),
]
sections = [{"key": k, "title": t, "body": b} for k, t, b in secs]

def C(name, ko, cls, role, part, content, act, src):
    return {"name": name, "name_ko": ko, "class": cls, "role": role, "part": part, "content_text": content, "activity_ko": act, "source": src}
compounds = [
 C("L-Ornithine", "오르니틴(유리)", "아미노산", "marker", "먹는 부위 추출물", "냉동 시 추출물 함량 증가, −4 ℃ 처리에서 최대(초록에 수치 없음)", "추출물의 대표 성분으로, 냉동 처리하면 늘어난다[10]", [10]),
 C("Acorbine", "아코르빈(β-알라닐-오르니틸-오르니틴)", "트리펩타이드", "bioactive", "먹는 부위 추출물", "함량 수치 확인하지 못함", "이 종에서 처음 분리된 비단백질 아미노산 트리펩타이드로, 생쥐에서 알코올성 간 손상을 줄였다(동물·세포 실험)[9, 11]", [9, 11]),
 C("beta-Alanine", "β-알라닌(유리)", "아미노산", "nutrient", "먹는 부위", "아바시리 시료에서 함량이 높은 유리아미노산(수치는 원문 표, 전문 표 확인 못함)", "냉동 시 아코르빈 분해로 늘어나고 염분에 따라 농도가 변했다[9, 13, 15]", [9, 13, 15]),
 C("Alanine", "알라닌(D·L)", "아미노산", "nutrient", "먹는 부위·외투막", "아바시리 시료에서 함량이 높은 유리아미노산(수치는 원문 표, 전문 표 확인 못함)", "D·L 알라닌이 세포 안 삼투 조절 물질로 쓰인다[13, 16]", [13, 16]),
 C("Glutamic acid", "글루탐산(유리)", "아미노산", "nutrient", "먹는 부위", "아바시리 시료에서 함량이 높은 유리아미노산(수치 확인하지 못함)", "맛을 정하는 유리아미노산 가운데 하나로 분석되었다[13]", [13]),
 C("Glycine", "글리신(유리)", "아미노산", "nutrient", "먹는 부위", "아바시리 시료에서 함량이 높은 유리아미노산(수치 확인하지 못함)", "맛을 정하는 유리아미노산 가운데 하나로 분석되었다[13]", [13]),
 C("Glycine betaine", "글리신 베타인", "삼투 조절 물질", "bioactive", "아가미·발 근육", "염분에 따라 농도 변화(수치 확인하지 못함)", "염분 변화에 따라 양이 달라진 대사물이다[15]", [15]),
 C("gamma-Aminobutyric acid", "GABA(감마아미노부티르산)", "아미노산", "bioactive", "아가미·발 근육", "염분에 따라 농도 변화(수치 확인하지 못함)", "염분 변화에 따라 양이 달라진 대사물이다[15]", [15]),
 C("Peridinin", "페리디닌", "카로티노이드", "bioactive", "먹는 부위", "총카로티노이드 5.3 mg/100 g(먹는 부위, 습중량) 가운데 주성분(개별 함량 확인하지 못함)", "먹이 조류에서 온 이 종의 주된 카로티노이드다[7]", [7]),
 C("Corbiculaxanthin", "코르비큘라잔틴", "카로티노이드", "bioactive", "먹는 부위", "함량 수치 확인하지 못함", "이 종에서 새로 구조가 밝혀진 카로티노이드로 재첩속 특유 성분으로 추정되었다[7, 8]", [7, 8]),
 C("Carotenoids", "총카로티노이드", "카로티노이드", "nutrient", "먹는 부위", "5.3 mg/100 g(먹는 부위, 습중량)", "이 종에서 43종 카로티노이드가 분리된 연구의 총량이다[7]", [7]),
 C("Selenium", "셀레늄", "무기질", "nutrient", "조갯살(주로 내장부)", "3.5 µg/g(건조 조갯살)", "약 30%가 물로 추출되었고 분자량 5000 미만의 셀레늄 화합물이 주로 내장부에 있었다[14]", [14]),
 C("Chondroitin sulfate", "콘드로이틴 황산(글리코사미노글리칸)", "다당류", "nutrient", "조갯살", "함량 수치 확인하지 못함", "식용 패류 10종 비교에서 글리코사미노글리칸 조성은 종마다 달랐다[29]", [29]),
]
assays = [
 {"role": "literature", "compound": "Free amino acids", "compound_ko": "유리아미노산", "part": "먹는 부위(생시료)",
  "content": "β-알라닌·알라닌·글루탐산·글리신 함량이 높음; 단위 mg/10 g 습중량(개별 수치는 원문 표, 확인하지 못함) [13]",
  "method": "아미노산 자동분석기(이온교환, 닌히드린 후발색)",
  "conditions": {"instrument": "Hitachi LaChrom Elite 아미노산 분석 시스템", "column": "", "mobile_phase": "", "gradient": "", "flow": "닌히드린 시약 0.25 ml/min", "temp": "닌히드린 반응 130 °C", "detection": "570 nm 흡광", "injection": "",
   "sample_prep": "3.5% 소금물에 하룻밤 해감, 먹는 부위 10 g을 증류수와 균질화해 20 ml로 맞춤 → 같은 부피 5% TCA로 단백질 침전 → 10,000 rpm 10분 원심 → 같은 부피 n-헥산 혼합 → 0.2 µm 셀룰로오스아세테이트 막 여과", "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "유리아미노산 조성이 먹는 부위 맛을 정하는 요인으로 쓰였다; 전문의 방법은 확인했으나 성분별 수치 표는 확인 못함[13].",
  "source": [13], "url": "https://doi.org/10.1016/j.dib.2017.11.075", "source_kind": "paper"},
 {"role": "literature", "compound": "Carotenoids", "compound_ko": "카로티노이드(총량·페리디닌 등)", "part": "먹는 부위(습중량)",
  "content": "총카로티노이드 5.3 mg/100 g(먹는 부위, 습중량) [7]", "method": "분리 후 UV-vis·FAB-MS(MS/MS)·1H NMR로 구조 확인(정량 조건은 전문 확인 못함)",
  "conditions": {"instrument": "", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "", "injection": "", "sample_prep": "", "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "기수에 사는 이 종은 페리디닌 계열, 담수 재첩류는 루테인이 주성분이어서 서식지·먹이를 반영하는 성분으로 쓰였다; 초록만 확인, 전문 확인 못함[7].",
  "source": [7], "url": "https://doi.org/10.1021/jf058088t", "source_kind": "paper"},
 {"role": "literature", "compound": "Selenium", "compound_ko": "셀레늄", "part": "조갯살(건조)",
  "content": "3.5 µg/g(건조 조갯살) [14]", "method": "셀레늄 화학종은 이온교환 크로마토그래피·MALDI-TOF MS·이미징 질량분석으로 확인(총량 정량법은 전문 확인 못함)",
  "conditions": {"instrument": "", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "", "injection": "", "sample_prep": "물·에탄올·클로로폼·헥산 추출 비교, 한외여과(분자량 5000 미만 분획)", "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "어패류가 셀레늄 공급원으로 알려져 이 종의 셀레늄 함량과 형태를 밝혔다; 초록만 확인, 전문 확인 못함[14].",
  "source": [14], "url": "https://doi.org/10.1248/cpb.c17-00492", "source_kind": "paper"},
]
d = {"slug": "corbicula-japonica", "name_ko": "일본재첩", "name_en": "Japanese basket clam (brackish water clam)",
     "scientific_name": "Corbicula japonica",
     "aliases": ["가막조개", "시지미(shijimi)", "Yamato-shijimi", "brackishwater clam", "Corbicula fuscata atrata", "Corbicula bifrons", "Corbicula ovalis"],
     "sections": sections, "compounds": compounds, "markers": [], "assays": assays, "nutrients": [], "production": [], "gi": [], "orgs": [], "world": [],
     "sources": sources}
p = pathlib.Path(__file__).resolve().parent.parent / "dossier.json"
p.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in sections: print(s["key"], len(s["body"]))
