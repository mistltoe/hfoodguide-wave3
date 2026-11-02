"""aurelia-aurita dossier.json 생성 스크립트 (작성자 W2)."""
import json
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "dossier.json"
ACC = "2026-11-02"


def pm(pmid):
    return f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"


def pmc(pmcid):
    return f"https://pmc.ncbi.nlm.nih.gov/articles/{pmcid}/"


sources = [
    (1, "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 보름달물해파리(Aurelia aurita) 1행, 같은 목록의 해파리(Rhopilema esculenta)·노무라입깃해파리(Nemopilema nomurai)·Cannonball jellyfish(Stomolophus meleagris)·파상땅해파리(Rhizina undulata) 행 대조(2026-10-13 받은 원자료)",
     "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "식품의약품안전처", "2026-10-13"),
    (2, "Stenvers V, Chi X, Javidpour J. Seasonal variability of the fatty acid composition in Aurelia aurita (Cnidaria: Scyphozoa): implications for gelativore food web studies. J Plankton Res 2020;42(4):440-452",
     pmc("PMC7344386"), "Journal of Plankton Research (PMC)", ACC),
    (3, "Masuda A et al. Mucin (qniumucin), a glycoprotein from jellyfish, and determination of its main chain structure. J Nat Prod 2007;70(7):1089-1092 (초록)",
     pm("17567171"), "Journal of Natural Products (PubMed)", ACC),
    (4, "Uzawa J et al. NMR study on a novel mucin from jellyfish in natural abundance, Qniumucin from Aurelia aurita. J Nat Prod 2009;72(5):818-823 (초록)",
     pm("19371080"), "Journal of Natural Products (PubMed)", ACC),
    (5, "Urai M et al. Structural analysis of O-glycans of mucin from jellyfish (Aurelia aurita) containing 2-aminoethylphosphonate. Carbohydr Res 2009;344(16):2182-2187 (초록)",
     pm("19732869"), "Carbohydrate Research (PubMed)", ACC),
    (6, "Ohta N et al. Jellyfish mucin may have potential disease-modifying effects on osteoarthritis. BMC Biotechnol 2009;9:98",
     pmc("PMC2801673"), "BMC Biotechnology (PMC)", ACC),
    (7, "Ushida K et al. Jellyfish mucin (qniumucin) extracted with a modified protocol indicated its existence as a constituent of the extracellular matrix. Biochim Biophys Acta Gen Subj 2022;1866(10):130189 (초록)",
     pm("35716958"), "BBA General Subjects (PubMed)", ACC),
    (8, "Kariotoglou DM, Mastronicolis SK. Sphingophosphonolipids, phospholipids, and fatty acids from Aegean jellyfish Aurelia aurita. Lipids 2001;36(11):1255-1264 (초록)",
     pm("11795859"), "Lipids (PubMed)", ACC),
    (9, "Balikci E et al. Characterization of Collagen from Jellyfish Aurelia aurita and Investigation of Biomaterials Potentials. Appl Biochem Biotechnol 2024;196(9):6200-6221 (초록)",
     pm("38224393"), "Applied Biochemistry and Biotechnology (PubMed)", ACC),
    (10, "Kulikova Y et al. Comparative analysis of collagen from different sources for wound and burn management. Biomater Transl 2025;7(1):155-169",
     pmc("PMC13190105"), "Biomaterials Translational (PMC)", ACC),
    (11, "Ovchinnikova TV et al. Aurelin, a novel antimicrobial peptide from jellyfish Aurelia aurita with structural features of defensins and channel-blocking toxins. Biochem Biophys Res Commun 2006;348(2):514-523 (초록)",
     pm("16890198"), "BBRC (PubMed)", ACC),
    (12, "Matveev IV, Shaposhnikova TG, Podgornaya OI. A novel Aurelia aurita protein mesoglein contains DSL and ZP domains. Gene 2007;399(1):20-25 (초록)",
     pm("17583446"), "Gene (PubMed)", ACC),
    (13, "Gold DA et al. The genome of the jellyfish Aurelia and the evolution of animal complexity. Nat Ecol Evol 2019;3(1):96-104 (초록)",
     pm("30510179"), "Nature Ecology & Evolution (PubMed)", ACC),
    (14, "Hu X et al. Chromosome-level genome assembly and annotation of the moon jellyfish Aurelia coerulea. Sci Data 2026;13(1) (초록)",
     pmc("PMC13243523"), "Scientific Data (PMC)", ACC),
    (15, "Dawson MN et al. The chromosomal genome sequence of the moon jellyfish, Aurelia sp. 4 Dawson. 2005 (Semaeostomeae: Ulmaridae) and its associated microbial metagenome sequences. Wellcome Open Res 2026;11:189 (초록)",
     pmc("PMC13157608"), "Wellcome Open Research (PMC)", ACC),
    (16, "Shao Z et al. Mitochondrial genome of the moon jelly Aurelia aurita (Cnidaria, Scyphozoa): a linear DNA molecule encoding a putative DNA-dependent DNA polymerase. Gene 2006;381:92-101 (초록)",
     pm("16945488"), "Gene (PubMed)", ACC),
    (17, "Hwang DS et al. Complete mitochondrial genome of the moon jellyfish, Aurelia sp. nov. (Cnidaria, Scyphozoa). Mitochondrial DNA 2013;25(1):27-28 (초록)",
     pm("23488923"), "Mitochondrial DNA (PubMed)", ACC),
    (18, "Kotova AV, Podgornaia OI, Adonin LS. [Reason to split the genus Aurelia. Mesoglein from two populations differ]. Tsitologiia 2015;57(1):70-75 (러시아어, 영문 초록)",
     pm("25872378"), "Tsitologiia (PubMed)", ACC),
    (19, "Seo Y et al. Population Genetic Structures of the Jellyfish Aurelia coerulea Polyps along Korean Coasts and Implications as Revealed by Mitochondrial COI. Zool Stud 2021;60:e63 (초록)",
     pmc("PMC9121272"), "Zoological Studies (PMC)", ACC),
    (20, "Brekhman V et al. Transcriptome profiling of the dynamic life cycle of the scypohozoan jellyfish Aurelia aurita. BMC Genomics 2015;16:74 (초록)",
     pmc("PMC4334923"), "BMC Genomics (PMC)", ACC),
    (21, "Kim JH, Jin SJ, Yoo SH. Public willingness to pay for eradicating a harmful marine organism: the case of Aurelia aurita in South Korea. Environ Sci Pollut Res Int 2022;29(59):88839-88851 (초록)",
     pmc("PMC9287532"), "Environmental Science and Pollution Research (PMC)", ACC),
    (22, "Rachamim T et al. The dynamically evolving nematocyst content of an anthozoan, a scyphozoan, and a hydrozoan. Mol Biol Evol 2015;32(3):740-753 (초록)",
     pm("25518955"), "Molecular Biology and Evolution (PubMed)", ACC),
    (23, "Chi X et al. Food quality matters: Interplay among food quality, food quantity and temperature affecting life history traits of Aurelia aurita (Cnidaria: Scyphozoa) polyps. Sci Total Environ 2019;656:1280-1288 (초록)",
     pm("30625657"), "Science of the Total Environment (PubMed)", ACC),
    (24, "Kitatani R et al. Length Is Associated with Pain: Jellyfish with Painful Sting Have Longer Nematocyst Tubules than Harmless Jellyfish. PLoS One 2015;10(8):e0135015 (초록)",
     pmc("PMC4550354"), "PLoS One (PMC)", ACC),
    (25, "Radwan FF et al. A comparison of the toxinological characteristics of two Cassiopea and Aurelia species. Toxicon 2001;39(2-3):245-257 (초록)",
     pm("10978742"), "Toxicon (PubMed)", ACC),
    (26, "Lee H et al. Scyphozoan jellyfish venom metalloproteinases and their role in the cytotoxicity. Toxicon 2011;58(3):277-284 (초록)",
     pm("21718715"), "Toxicon (PubMed)", ACC),
    (27, "Raposo A et al. Jellyfish as Food: A Narrative Review. Foods 2022;11(18):2773",
     pmc("PMC9498191"), "Foods (PMC)", ACC),
    (28, "Bleve G et al. Identification of Safety and Quality Parameters for Preparation of Jellyfish Based Novel Food Products. Foods 2019;8(7):263",
     pmc("PMC6678107"), "Foods (PMC)", ACC),
    (29, "Ramires FA et al. Optimization of a Calcium-Based Treatment Method for Jellyfish to Design Food for the Future. Foods 2022;11(17):2697",
     pmc("PMC9455609"), "Foods (PMC)", ACC),
    (30, "Bonaccorsi G et al. A Systematic Review of Risk Assessment Associated with Jellyfish Consumption as a Potential Novel Food. Foods 2020;9(7):935 (초록)",
     pmc("PMC7404704"), "Foods (PMC)", ACC),
    (31, "Zhang H et al. Aluminium in food and daily dietary intake assessment from 15 food groups in Zhejiang Province, China. Food Addit Contam Part B 2016;9(2):73-78 (초록)",
     pm("26727195"), "Food Additives & Contaminants B (PubMed)", ACC),
    (32, "Wong WW et al. Dietary exposure to aluminium of the Hong Kong population. Food Addit Contam Part A 2010;27(4):457-463 (초록)",
     pm("20234962"), "Food Additives & Contaminants A (PubMed)", ACC),
    (33, "Ogimoto M et al. [Aluminium content in foods with aluminium-containing food additives]. Shokuhin Eiseigaku Zasshi 2012;53(1):57-62 (일본어, 영문 초록)",
     pm("22450671"), "Journal of the Food Hygienic Society of Japan (PubMed)", ACC),
    (34, "식약처 고시 제2026-43호 「건강기능식품의 기준 및 규격」 제2. 공통 기준 및 규격 2. 제조기준 11) 어린이 섭취용 건강기능식품에 쓸 수 없는 식품첨가물 (6) 알루미늄 함유 식품첨가물(로컬 원문 docs/refs/MFDS/건강기능식품의기준및규격_2026-43_제1~제3.txt)",
     "https://www.mfds.go.kr/brd/m_211/view.do?seq=14973", "식품의약품안전처", ACC),
    (35, "해양수산부 보도자료 「보름달물해파리 주의단계 특보, 충남까지 확대 발령」(2024) 외 — 웹 검색 결과 요약으로만 확인, 원문 페이지는 이 환경에서 열지 못함",
     "https://www.mof.go.kr/doc/ko/selectDoc.do?docSeq=57698&menuSeq=971&bbsSeq=10", "해양수산부", ACC),
]

S = {}
S["overview"] = ("한눈에 보기", "\n\n".join([
    "보름달물해파리(Aurelia aurita)는 자포동물문 해파리강(Scyphozoa)에 속하는 해파리로, 영어로는 moon jelly·moon jellyfish 로 불린다[2][20]. "
    "해파리 몸은 습중량의 95–98%가 물이며[27], 우산의 큰 부분은 중교(mesoglea)라는 세포외기질이다[6][12]. "
    "국내에서는 해양 레저·관광 수입·어업·발전소 냉각수 취수에 피해를 주는 유해 해양생물로 법적으로 등록되어 있다[21].",
    "식품원료로서의 지위: 식품의약품안전처 「식품원료 목록」에는 '보름달물해파리'(영문명 Jelly-fish, 학명 Aurelia aurita) 1행이 식품원료(A코드)·수산물로 올라 있고, 사용가능 부위 칸은 '-', 사용 조건은 비어 있으며 상태는 '사용가능'이다[1]. "
    "건강기능식품 고시형 원료의 원재료로는 연결되어 있지 않다[1].",
    "성분 연구는 해파리 뮤신인 큐니우뮤신(qniumucin), 중교의 콜라겐·메소글레인, 지방산과 인지질에 모여 있다[2][3][8][9][12]. "
    "이 종 자체를 식품으로 가공·유통한 통계나 국내 섭취 자료는 확인하지 못했다[1][27].",
]))
S["history"] = ("이용 역사", "\n\n".join([
    "해파리를 먹는 일은 예부터 중국 문화에서 이어졌고, 우산 부분을 익혀 샐러드로 먹는 방식이 말레이시아·태국·일본 등으로 퍼졌다[27]. "
    "상업적으로 잡아 먹는 해파리는 주로 근구해파리목(Rhizostomeae) 종이며, 아시아에서는 소금과 명반으로 탈수하는 전통 가공이 쓰인다[28]. "
    "보름달물해파리가 속한 Aurelia 속은 근구해파리목이 아닌 기구해파리목(Semaeostomeae) Ulmaridae 과다[15].",
    "이 종을 먹은 역사 기록은 확인하지 못했다[27][28]. "
    "2007년 일본 연구진은 해파리 5종에서 새로운 뮤신을 뽑아 '큐니우뮤신'이라 이름 붙이고 새로운 해양 자원으로 쓰자고 제안했다[3]. "
    "이후 보름달물해파리의 큐니우뮤신 구조가 핵자기공명(NMR)으로 분석되었고, 토끼 관절염 모델에 주사하는 실험에도 쓰였다[4][6].",
    "국내에서는 보름달물해파리가 유해 해양생물로 지정되어, 정부가 부착 유생(폴립)을 없애는 방식으로 구제를 추진하고 있다[21]. "
    "해양수산부는 보름달물해파리가 많이 나타나면 해역별 주의단계 특보를 낸다(웹 검색 요약으로만 확인)[35].",
]))
S["biology"] = ("생물학적 특징·생태", "\n\n".join([
    "보름달물해파리는 바닥에 붙어 사는 폴립 단계와 떠다니는 메두사 단계를 오가는 복잡한 생활사를 가진다[20][23]. "
    "생활사는 플라눌라 유생 → 폴립 → 스트로빌라(횡분체) → 에피라 → 메두사로 이어지며, 폴립 단계에서 메두사 단계로 넘어가는 과정을 스트로빌레이션이라 한다[20][23]. "
    "폴립 실험에서는 수온이 스트로빌레이션을 결정하는 핵심 요인이었고, 27 °C에서는 생존과 성장이 떨어졌다[23].",
    "독일 킬 피오르드 조사에서는 겨울 한때를 빼고 거의 1년 내내 나타났고, 여름·가을 개체의 우산 지름이 평균 11.2 ± 5.9 cm로 가장 컸다[2]. "
    "생활사 전 단계 전사체 분석에서는 메두사 단계에 세포외기질 관련 유전자 발현이 많았다[20]. "
    "중교에는 세포가 많고, 47 kDa 단백질인 메소글레인이 주요 성분으로 보고되었다[12].",
]))
S["related_species"] = ("관련 종·이름", "\n\n".join([
    "Aurelia aurita 는 극지에서 열대까지 퍼진 세계종으로 여겨졌지만, 분자 연구는 서로 다른 종이 섞여 있을 수 있음을 보여 준다[18]. "
    "러시아 연구진은 백해·흑해 개체만 A. aurita 이고 동해(일본해) 개체는 다른 종(Aurelia sp.)이라고 보고했다[18]. "
    "한국 4개 연안의 폴립 229개를 COI 유전자로 분석한 연구는 모두 Aurelia coerulea 로 판정했다[19]. "
    "그래서 국내 논문의 '보름달물해파리'는 A. coerulea 로 적히기도 하지만, 「식품원료 목록」과 국내 정책 연구는 Aurelia aurita 로 적는다[1][19][21].",
    "같은 목록에는 해파리(Rhopilema esculenta, 이명 숲뿌리해파리)·노무라입깃해파리(Nemopilema nomurai)·Cannonball jellyfish(Stomolophus meleagris)도 수산물 '사용가능'으로 올라 있다[1]. "
    "이름에 '해파리'가 들어간 '파상땅해파리'는 학명이 Rhizina undulata 이고 '사용불가'로 적혀 있다[1]. "
    "쏘였을 때 거의 아프지 않은 보름달물해파리와 달리 Chrysaora pacifica 등은 중간~심한 통증을 일으킨다[24].",
]))
S["cultivation"] = ("발생·채집", "\n\n".join([
    "보름달물해파리는 양식하거나 식용으로 어획하는 대상이 아니며, 국내 생산·어획 통계는 확인하지 못했다[1][21]. "
    "연구용 개체는 그물로 채집하는데, 킬 피오르드 조사는 1 mm 그물코의 WP3 네트를 수심 18 m에서 끌어올려 2015–2016년 2주마다 채집했다[2]. "
    "식용 해파리 전체로는 FAO가 2015–2018년 세계 어획량을 연 약 30만 톤으로 추정했으며, 이 값은 종을 구분하지 않은 것이다[27].",
    "국내에서는 대량 발생 자체가 관리 대상이다[21]. "
    "정부는 폴립을 제거해 발생을 줄이려 하며, 이 구제 사업에 대한 가구당 지불의사액은 연 3,911원, 전국 가치는 연 804억 6천만 원으로 추정되었다[21]. "
    "해양수산부는 100 ㎡당 5마리 이상이면 주의단계 특보를 내며, 2024년에는 5월 27일부터 10월 21일까지 특보가 이어졌다(웹 검색 요약으로만 확인)[35]. "
    "폴립의 출아 번식은 먹이가 많을수록, 고도불포화지방산이 많은 먹이일수록 늘었다[23].",
]))
S["processing"] = ("가공·추출 연구", "\n\n".join([
    "식용 해파리(주로 근구해파리목, 이 종이 아님)는 잡은 뒤 몇 시간 안에 우산과 입팔을 나누어 씻고, 염화나트륨과 명반(황산알루미늄칼륨 또는 황산알루미늄암모늄) 혼합물에 여러 번 절인다[27][28]. "
    "명반은 조직을 고무처럼 단단하게 만들고, 종과 방법에 따라 전 과정이 4–40일 걸린다[27]. "
    "이탈리아 연구는 Rhizostoma pulmo 우산을 NaCl 90%·명반 10% 혼합물로 절이는 전통법과, 명반 대신 젖산칼슘·구연산칼슘 소금물을 쓰는 방법을 비교했다[29]. "
    "칼슘 처리품은 알루미늄이 매우 낮았고 명반 처리품은 매우 높았다[29].",
    "보름달물해파리에서는 식품 가공보다 성분 추출 연구가 많다[3][9]. "
    "큐니우뮤신은 우산의 중교를 잘게 잘라 물에 풀고 에탄올로 침전시킨 뒤 DEAE 음이온교환 수지로 정제한다[6]. "
    "콜라겐은 0.5 M 아세트산(1:10)으로 4 °C에서 3일 추출하고 염화나트륨으로 침전시켜 얻었다[10]."
    
]))
S["genetics"] = ("유전 정보", "\n\n".join([
    "2006년 보름달물해파리의 미토콘드리아 DNA(16,937 염기)가 해파리강 처음으로 해독되었고, 동물에서 처음 확인된 선형 미토콘드리아 DNA였다[16]. "
    "국내 연구진이 해독한 Aurelia sp. nov.의 선형 미토콘드리아 DNA는 16,971 bp 였고, 단백질 유사도는 A. aurita 와 유전자에 따라 59–98%였다[17].",
    "2019년 발표된 Aurelia 유전체 분석은 메두사 단계가 생겼다고 유전자 수가 늘지는 않았다고 보고했다[13]. "
    "2026년 Aurelia coerulea 염색체 수준 유전체는 약 554.10 Mb, 21개 염색체, 단백질 암호 유전자 26,777개, 전이인자 약 71.48%였다[14]. "
    "같은 해 Aurelia sp. 4 유전체는 462.10 Mb, 21개 염색체 유사분자, 미토콘드리아 16.88 kb 로 조립되었다[15]. "
    "한국 연안 폴립의 COI 분석에서는 53개 일배체형이 두 무리(A·B)로 나뉘어 모든 지역에 함께 있었다[19]. "
    "홍해 계통의 생활사 전사체에서는 메두사 단계에 콜라겐·피브릴린·라미닌 전사체가 많이 발현되었다[20].",
]))
S["safety"] = ("안전성", "\n\n".join([
    "쏘임 독(식품 안전과 별개): 보름달물해파리는 자포 세관이 짧아 사람에게 통증을 거의 주지 않는 종으로 분류되었다[24]. "
    "다만 홍해 개체는 입술을 쏘았고 체서피크만 개체보다 독성이 강해, 지역마다 차이가 있다[25]. "
    "자포 내용물 단백체 분석에서 이 종의 독은 주로 세포독소와 효소로 이루어졌고, 생쥐 세포 독성은 Cyanea nozakii > 노무라입깃해파리 > 보름달물해파리 > Rhopilema esculenta 순이었다[22][26].",
    "식품 안전(명반 잔류, 식용 해파리 제품 자료이며 이 종의 자료는 확인하지 못함): 중국 저장성 조사에서 해파리의 알루미늄은 평균 4,862 mg/kg으로 높았고 15개 식품군을 통한 섭취량의 37.6%를 차지했다[31]. "
    "홍콩의 즉석 해파리는 평균 1,200 mg/kg이었고, 일본 조사에서는 염장 해파리 1건이 주 1회 섭취만으로 16 kg 유아의 잠정 주간섭취허용량(PTWI)에 해당했다[32][33]. "
    "JECFA 의 PTWI 는 2 mg/kg 체중이다[29]. "
    "국내 해파리 식품의 알루미늄 기준은 확인하지 못했고, 어린이용 건강기능식품에는 황산알루미늄칼륨 등 알루미늄 함유 첨가물을 쓰지 못한다[34]. "
    "체계적 문헌고찰은 미생물·알레르기 위험이 낮다고 보면서 알루미늄 정기 검사를 권했고, 해파리 섭취 뒤 알레르기 증례도 보고되었다[27][30].",
]))

compounds = [
    {"name": "Qniumucin", "name_ko": "큐니우뮤신(해파리 뮤신)", "class": "뮤신형 당단백질", "role": "marker", "part": "중교(우산)",
     "content_text": "해파리 5종에서 건조중량의 1–3%, 습중량의 0.02–0.1% 수율(초록, 종별 값 없음)",
     "activity_ko": "8개 아미노산 반복(VVETTAAP)에 GalNAc 당사슬이 붙은 단순 구조다[3][4]. 히알루론산과 함께 토끼 무릎에 주사하면 연골 변성이 적었다(동물 실험)[6]",
     "source": [3, 4, 6, 7]},
    {"name": "2-Aminoethylphosphonic acid", "name_ko": "2-아미노에틸포스폰산(AEP)", "class": "포스폰산(당사슬 치환기)", "role": "bioactive", "part": "큐니우뮤신 O-당사슬",
     "content_text": "함량 수치 없음; O-당사슬은 GalNAc, AEP-(O→6)-GalNAc, P-6-GalNAc 세 단당이 주성분",
     "activity_ko": "AEP가 붙은 O-당사슬은 당단백질에서 처음 보고된 구조다[5]", "source": [5]},
    {"name": "Collagen", "name_ko": "콜라겐(산 가용성)", "class": "구조 단백질", "role": "bioactive", "part": "체(산 가용성 분획)",
     "content_text": "변성온도 43.7 °C, 등전점 4.46, α1·α2 사슬 약 122·140 kDa(마르마라해 개체)[9]; 발트해 개체 콜라겐 등전점 5.19[10]",
     "activity_ko": "콜라겐 막 위에서 섬유아세포 증식이 배양 접시보다 높았다(세포 실험)[9]", "source": [9, 10]},
    {"name": "Mesoglein", "name_ko": "메소글레인", "class": "ZP 도메인 단백질", "role": "bioactive", "part": "중교",
     "content_text": "중교의 주요 단백질, 겉보기 분자량 47 kDa(SDS-PAGE)",
     "activity_ko": "중교 세포외기질의 구조 성분으로 추정된다[12]. 동해 개체는 53–55 kDa로 달라 종 구분 근거로 쓰였다[18]", "source": [12, 18]},
    {"name": "Aurelin", "name_ko": "아우렐린", "class": "항균 펩타이드(40잔기)", "role": "bioactive", "part": "중교",
     "content_text": "분자량 4296.95 Da, 시스테인 6개(이황화 결합 3개)",
     "activity_ko": "그람 양성·음성 세균에 항균 활성을 보였다(시험관)[11]", "source": [11]},
    {"name": "Fatty acids (total)", "name_ko": "총 지방산", "class": "지질", "role": "nutrient", "part": "우산·입팔(위 제거), 생식소 별도",
     "content_text": "에피라 102.08 ± 32.72, 미성숙 메두사 76.90 ± 45.05, 성숙 메두사 27.45 ± 8.13, 생식소 341.42 ± 27.27 μg/g 건조중량",
     "activity_ko": "총량은 낮지만 다중불포화지방산 비율이 42.9–54.7%로 높았다[2]", "source": [2]},
    {"name": "Eicosapentaenoic acid", "name_ko": "EPA(에이코사펜타엔산)", "class": "ω-3 다중불포화지방산", "role": "nutrient", "part": "우산·입팔, 생식소",
     "content_text": "절대 함량은 원문 그림에만 있음; 생애단계 간 차이의 첫째 기여 성분(SIMPER 누적 22.93–31.55%)",
     "activity_ko": "조사 기간 내내 검출되었고 DHA보다 많았다(DHA/EPA 0.33–0.59)[2]", "source": [2]},
    {"name": "Docosahexaenoic acid", "name_ko": "DHA(도코사헥사엔산)", "class": "ω-3 다중불포화지방산", "role": "nutrient", "part": "우산·입팔, 생식소",
     "content_text": "DHA/EPA 비 0.33–0.59(생애단계별 평균)",
     "activity_ko": "계절·생애단계에 따른 지방산 조성 차이의 주요 기여 성분이었다[2]", "source": [2]},
    {"name": "Arachidonic acid", "name_ko": "아라키돈산", "class": "ω-6 다중불포화지방산", "role": "nutrient", "part": "우산·입팔, 생식소",
     "content_text": "ARA/EPA 비 0.14–0.38(생애단계별 평균)",
     "activity_ko": "필수지방산으로 연중 검출되었다[2]", "source": [2]},
    {"name": "Palmitic acid", "name_ko": "팔미트산", "class": "포화지방산", "role": "nutrient", "part": "우산·입팔, 생식소",
     "content_text": "절대 함량은 원문 그림에만 있음; 포화지방산 비율 32.6–48.1%(생애단계별)",
     "activity_ko": "계절 간 지방산 조성 차이의 주요 기여 성분이었다[2]", "source": [2]},
    {"name": "Ceramide 2-aminoethylphosphonate", "name_ko": "세라마이드 아미노에틸포스포네이트(CAEP)", "class": "스핑고포스포노지질", "role": "bioactive", "part": "체 조직(에게해 개체)",
     "content_text": "총지질 생조직의 0.031–0.036%; 포스포노지질은 인지질의 21.7%, 그중 CAEP-I 18.3%",
     "activity_ko": "이 종에서 처음 기재된 스핑고포스포노지질이다[8]", "source": [8]},
    {"name": "Phosphatidylcholine", "name_ko": "포스파티딜콜린", "class": "인지질", "role": "nutrient", "part": "체 조직(에게해 개체)",
     "content_text": "인지질의 44.5%(그중 글리세릴에테르형 36.2%)",
     "activity_ko": "이 종 인지질에서 가장 많은 성분이었다[8]", "source": [8]},
]

empty_cond = {k: "" for k in ["instrument", "column", "mobile_phase", "gradient", "flow", "temp", "detection", "injection",
                              "sample_prep", "standard", "linearity", "lod", "loq", "recovery"]}

assays = [
    {"role": "literature", "compound": "Fatty acids (FAME profile)", "compound_ko": "지방산 조성(지방산 메틸에스터)",
     "part": "우산·입팔(위 제거), 생식소는 따로",
     "content": "총 지방산 에피라 102.08 ± 32.72, 미성숙 메두사 76.90 ± 45.05, 성숙 메두사 27.45 ± 8.13, 생식소 341.42 ± 27.27 μg/g DW; 19종 지방산 동정",
     "method": "GC-FID",
     "conditions": dict(empty_cond, **{
         "instrument": "Trace GC-Ultra(Thermo Fisher Scientific), 불꽃이온화검출기",
         "column": "TR-FAME 칼럼(10 m × 0.1 mm, 막 두께 0.20 μm)",
         "mobile_phase": "수소(운반기체)",
         "temp": "원문이 인용한 선행 연구의 승온 프로그램(수치는 본문에 없음)",
         "detection": "FID",
         "sample_prep": "동결건조(0.100 mbar, −50 °C, 12시간 이상) 후 분쇄, 2–7 mg 취해 산 촉매 에스터교환으로 FAME 제조",
         "standard": "Supelco 37 FAME 혼합 표준(머무름 시간으로 동정), Chromcard 소프트웨어로 정량",
     }),
     "rationale": "이 종 단독으로 2년간 계절·생애단계별 지방산을 정량한 연구로, EPA·DHA·ARA 등 필수지방산의 존재와 비율을 보여 준다. 검출·정량한계와 회수율은 원문에 없다[2].",
     "source": [2], "url": pmc("PMC7344386"), "source_kind": "paper"},
    {"role": "literature", "compound": "Qniumucin", "compound_ko": "큐니우뮤신",
     "part": "중교(우산)",
     "content": "해파리 5종에서 건조중량 1–3%, 습중량 0.02–0.1%(초록; 보름달물해파리 단독 값은 확인 못함)",
     "method": "에탄올 침전·DEAE 음이온교환 정제 후 중량(수율)",
     "conditions": dict(empty_cond, **{
         "sample_prep": "중교를 잘게 잘라 물에 풀고 10,000 ×g 원심분리, 상등액에 1/3 부피 에탄올 첨가해 침전, 물에 녹여 투석·동결건조 후 인산완충액에서 DEAE 수지(Toyopearl DEAE-650M)에 1시간 결합, 0.5 M NaCl 인산완충액으로 용출·투석·동결건조",
     }),
     "rationale": "이 종을 비롯한 해파리에 공통으로 많은 뮤신으로 새 해양 자원으로 제안되었다[3]. 정제법은 보름달물해파리·노무라입깃해파리 추출에 쓴 전문(Methods)에서 옮겼고, 수율 측정 조건은 2007년 원논문 전문 확인 못함[6].",
     "source": [3, 6], "url": pm("17567171"), "source_kind": "paper"},
    {"role": "literature", "compound": "Total lipids and phospholipid classes", "compound_ko": "총지질·인지질 조성",
     "part": "체 조직(에게해 개체)",
     "content": "총지질 생조직의 0.031–0.036%, 지질 인 1.3–1.7%; 포스포노지질 21.7%(CAEP-I 18.3%), 포스파티딜콜린 44.5%, 포스파티딜에탄올아민 18.6%",
     "method": "지질 분획·HPLC(초록·MeSH 기준, 세부 조건 확인 못함)",
     "conditions": dict(empty_cond),
     "rationale": "이 종의 인지질에 특이한 스핑고포스포노지질(CAEP)을 처음 정량한 자료다. 전문 확인 못함(초록만 확인)[8].",
     "source": [8], "url": pm("11795859"), "source_kind": "paper"},
]

world = [
    {"country": "세계", "metric": "production_t", "year": 2018, "value": 300000, "unit": "톤",
     "note": "식용 해파리 전체(종 구분 없음) 어획량, 2015–2018년 연간 추정치; 리뷰 논문이 FAO 자료를 인용한 값. 보름달물해파리 값이 아님",
     "source": [27]},
]

d = {
    "slug": "aurelia-aurita",
    "name_ko": "보름달물해파리",
    "name_en": "Moon jellyfish",
    "scientific_name": "Aurelia aurita",
    "aliases": ["Moon jelly", "Moon jellyfish", "Jelly-fish"],
    "sections": [{"key": k, "title": t, "body": b} for k, (t, b) in S.items()],
    "compounds": compounds,
    "markers": [],
    "nutrients": [],
    "production": [],
    "world": world,
    "assays": assays,
    "gi": [],
    "orgs": [],
    "sources": [{"n": n, "title": t, "url": u, "publisher": p, "accessed": a} for n, t, u, p, a in sources],
}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for k, (t, b) in S.items():
    print(k, len(b))
