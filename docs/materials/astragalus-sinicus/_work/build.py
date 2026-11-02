import json
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "dossier.json"
ACC = "2026-11-02"


def pm(title, journal, pmid, doi, pmc=None, note=""):
    t = f"{title} — {journal}, " + (f"doi:{doi}, " if doi else "") + f"PMID {pmid}" + (f", {pmc}" if pmc else "") + note
    url = f"https://pmc.ncbi.nlm.nih.gov/articles/{pmc}/" if pmc else f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
    return {"title": t, "url": url, "publisher": "PubMed/NCBI", "accessed": ACC}


S = [
    {"title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 자운영순(Astragalus sinicus L., 식품원료 A코드, 사용가능부위 : 순) 행 및 같은 속 황기(Astragalus membranaceus Bunge)·트라가칸타수액(Astragalus gummifera)·사원자(Astragalus complanatus R. Br., 사용불가) 행(로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json)",
     "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
    pm("Effect of Astragalus sinicus Ethanol Extract on Menopausal Symptoms in an Ovariectomized (OVX) Mouse Model", "Journal of Microbiology and Biotechnology 36:e2510033 (2026)", "41605805", "10.4014/jmb.2510.10033", "PMC12868947", " (전문 확인)"),
    pm("The chromosome-level genome assembly of Astragalus sinicus and comparative genomic analyses provide new resources and insights for understanding legume-rhizobial interactions", "Plant Communications 3(2):100263 (2021)", "35529952", "10.1016/j.xplc.2021.100263", "PMC9073321", " (전문 확인)"),
    pm("Yield and nutrient composition of forage crops and their effects on soil characteristics of winter fallow paddy in South China", "Frontiers in Plant Science 14:1292114 (2024)", "38293627", "10.3389/fpls.2023.1292114", "PMC10825004", " (전문 확인)"),
    pm("Triterpene glycosides from the seeds of Astragalus sinicus L.", "Chemical & Pharmaceutical Bulletin 40(12):3330-3 (1992)", "1294336", "10.1248/cpb.40.3330", None, " (초록)"),
    pm("Anti-inflammatory activity of compounds isolated from Astragalus sinicus L. in cytokine-induced keratinocytes and skin", "Experimental & Molecular Medicine 46(3):e87 (2014)", "24651533", "10.1038/emm.2013.157", "PMC3972784", " (전문 확인)"),
    pm("Dietary aqueous extract of Astragalus sinicus alleviates obesity by reshaping gut microbiota and metabolism", "Journal of the Science of Food and Agriculture (2026)", "42851075", "10.1002/jsfa.71149", None, " (초록)"),
    pm("Contraction, recombination and innovation shape the dynamic pan-plastome of Astragalus sinicus", "Communications Biology (2026)", "42393259", "10.1038/s42003-026-10590-5", None, " (초록)"),
    pm("Exploring site-specific N application rate to reduce N footprint and increase crop production for green manure-rice rotation system in southern China", "Journal of Environmental Management 347:119033 (2023)", "37757691", "10.1016/j.jenvman.2023.119033", None, " (초록)"),
    pm("Effects of Chinese Milk Vetch Returning Incorporated with Chemical Fertilizer Reduction on the Composition and Function of Soil Bacterial Communities in Paddy Fields (중문, 영문 초록)", "Huan Jing Ke Xue 44(5):2936-2944 (2023)", "37177965", "10.13227/j.hjkx.202207228", None, " (초록)"),
    pm("Mesorhizobium jarvisii is a dominant and widespread species symbiotically efficient on Astragalus sinicus L. in the Southwest of China", "Systematic and Applied Microbiology 43(5):126102 (2020)", "32847794", "10.1016/j.syapm.2020.126102", None, " (초록)"),
    pm("Flower and pod development, grain-setting characteristics and grain yield in Chinese milk vetch (Astragalus sinicus L.) in response to pre-anthesis foliar application of paclobutrazol", "PLoS One 16(2):e0245554 (2021)", "33556055", "10.1371/journal.pone.0245554", None, " (초록)"),
    pm("Cloning, Identification, and Functional Analysis of the Chalcone Isomerase Gene from Astragalus sinicus", "Genes 14(7):1400 (2023)", "37510305", "10.3390/genes14071400", None, " (초록)"),
    pm("Identification and evaluation of TCM shayuanzi (중문, 영문 초록)", "Zhongguo Zhong Yao Za Zhi 28(6):496-9 (2003)", "15015323", None, None, " (초록)"),
    pm("Identification on genuine and pseudo shayuanzi collected from different place by HPLC fingerprint (중문, 영문 초록)", "Zhongguo Zhong Yao Za Zhi 28(9):820-2, 861 (2003)", "15015372", None, None, " (초록)"),
    pm("Milk vetch returning reduces rice grain Cd concentration in paddy fields: Roles of iron plaque and soil reducing-bacteria", "Chemosphere 308(Pt 1):136158 (2022)", "36029857", "10.1016/j.chemosphere.2022.136158", None, " (초록)"),
    pm("Cadmium-Tolerant Bacterium Strain Cdb8-1 Contributed to the Remediation of Cadmium Pollution through Increasing the Growth and Cadmium Uptake of Chinese Milk Vetch (Astragalus sinicus L.) in Cadmium-Polluted Soils", "Plants 13(1):76 (2023)", "38202384", "10.3390/plants13010076", None, " (초록)"),
    pm("Weed suppression and antioxidant activity of Astragalus sinicus L. decomposition leachates", "Frontiers in Plant Science 13:1013443 (2022)", "36466260", "10.3389/fpls.2022.1013443", None, " (초록)"),
    pm("Effect of AM fungi on the growth and powdery mildew development of Astragalus sinicus L. under water stress", "Plant Physiology and Biochemistry 219:109422 (2024)", "39718283", "10.1016/j.plaphy.2024.109422", None, " (초록)"),
    pm("Hydrotime Model Parameters Estimate Seed Vigor and Predict Seedling Emergence Performance of Astragalus sinicus under Various Environmental Conditions", "Plants 12(9):1876 (2023)", "37176935", "10.3390/plants12091876", None, " (초록)"),
    pm("Comparative enzymology of the adenosine triphosphate sulphurylases from leaf tissue of selenium-accumulator and non-accumulator plants", "Biochemical Journal 139(1):37-42 (1974)", "4377098", "10.1042/bj1390037", None, " (초록)"),
    pm("Symptomology and etiology of a new disease, yellow stunt, and root rot of standing milkvetch caused by Embellisia sp. in Northern China", "Mycopathologia 163(6):327-34 (2007)", "17492492", "10.1007/s11046-007-9002-2", None, " (초록)"),
    pm("Screening and Application of Highly Efficient Rhizobia for Leguminous Green Manure Astragalus sinicus in Lyophilized Inoculants and Seed Coating", "Plants 14(15):2431 (2025)", "40805780", "10.3390/plants14152431", None, " (초록)"),
    pm("Astragalus sinicus Incorporated as Green Manure for Weed Control in Corn", "Frontiers in Plant Science 13:829421 (2022)", "35574090", "10.3389/fpls.2022.829421", None, " (초록)"),
    pm("A purple acid phosphatase plays a role in nodule formation and nitrogen fixation in Astragalus sinicus", "Plant Molecular Biology 88(6):515-29 (2015)", "26105827", "10.1007/s11103-015-0323-0", None, " (초록)"),
]
for i, s in enumerate(S, 1):
    s["n"] = i
sources = [{"n": s["n"], "title": s["title"], "url": s["url"], "publisher": s["publisher"], "accessed": s["accessed"]} for s in S]

sections = [
    {"key": "overview", "title": "한눈에 보기", "body":
     "자운영(Astragalus sinicus L.)은 콩과 황기속의 풀로, 영어로는 Chinese milk vetch라 부른다[1, 3]. 중국에서 기원해 중국·한국·일본에서 논의 겨울 녹비(풋거름) 작물로 널리 재배되어 왔고, 사료·꿀의 원천으로도 쓰인다[3]. 동아시아에 자생하며 연한 어린 잎과 줄기를 먹고 꽃을 차로 우려 마신다는 기록이 있다[2].\n\n"
     "식품의약품안전처 「식품원료 목록」에는 '자운영순' 한 행이 식품원료(A코드) '사용가능'으로 올라 있고, 사용 조건은 '사용가능부위 : 순'이다[1]. 같은 행은 이명을 '야화생', 영명을 'Chinese Milkvetch'로 적으며, 건강기능식품(C코드) 행은 없어 고시로 정한 지표성분도 없다[1]. 따라서 식품으로 쓸 수 있는 것은 어린 순뿐이며, 뿌리·씨앗·꽃은 이 행의 사용 부위에 들어 있지 않다[1].\n\n"
     "자운영 연구의 대부분은 녹비·토양 비옥도에 관한 것이고, 약용·식용 성분 연구는 적다[2]. 전초 추출물의 동물·세포 실험이 몇 건 있으나 사람 연구는 확인하지 못함."},
    {"key": "history", "title": "역사와 전통 이용", "body":
     "자운영은 중국 남부에서 수백 년 동안 벼 생산성을 높이고 토양 퇴화를 막는 녹비·피복 작물로 재배되어 왔다[3]. 동아시아의 논에서 전통적으로 길러 왔으며, 녹비와 가축 사료로 흔히 쓰였다[6]. 유전체 논문은 자운영을 고품질 사료풀이자 꿀의 원천, 중국 전통 약재로 소개한다[3]. 종자 연구에서도 자운영은 사료·녹비·윤작에 두루 쓰이는 콩과 작물로 소개된다[20].\n\n"
     "민간에서는 가래·인후통·외상 출혈·대상포진에 썼고, 꽃은 차로 우려 마셨다고 한다[2]. 한국 연구진은 이 식물이 일본·중국 남부·한국 중부에 자생한다고 적었다[2]. 2014년 논문은 자운영의 약리 활성을 보고한 첫 연구라고 스스로 밝혔다[6].\n\n"
     "중국 시장에서는 약재 '사원자(沙苑子, Astragalus complanatus 씨앗)'에 자운영 씨앗이 섞여 유통된 사례가 조사되었다[14]. 한국에서 순을 나물로 먹어 온 시기와 지역별 식용 관습을 다룬 1차 자료는 확인하지 못함. 꿀벌 밀원으로서 국내 이용 규모를 다룬 공공기관 자료도 확인하지 못함."},
    {"key": "biology", "title": "식물학적 특징", "body":
     "자운영은 콩과(Fabaceae) 식물로 염색체는 2n = 2x = 16이며, 겨울에 자라는 녹비·피복 작물이다[3]. 생활형은 문헌마다 달라 두해살이로 적은 자료[4]와 여러해살이로 적은 자료[2, 6]가 있다. 잎과 꽃의 색은 안토시아닌이 만들며, 칼콘 이성화효소(CHI) 유전자는 잎에서 가장 많이 발현되고 안토시아닌 함량과 비례했다[13].\n\n"
     "자운영은 뿌리혹박테리아와 숙주 특이성이 엄격하며, 무한생장형 뿌리혹만 만든다[3]. 중국 남서부 13곳에서 분리한 451개 균주 가운데 Mesorhizobium jarvisii가 76.3%, M. huakuii가 22.8%를 차지했다[11]. 뿌리에는 수지상 균근균(AM균)도 공생하며, 가뭄 조건에서 균근 접종은 흰가루병 발생을 16.54% 줄였다[19].\n\n"
     "중국 광둥의 겨울 논 시험에서 초기 개화기 지상부는 건물 140 g/kg(생체 기준), 조단백질 212 g/kg DM, 조지방 56.1 g/kg DM, 중성세제섬유(NDF) 499 g/kg DM이었다[4]. 같은 시험에서 자운영 초장은 14.9 cm로 비교한 다섯 작물 가운데 가장 작았다[4]."},
    {"key": "related_species", "title": "분류와 근연종", "body":
     "자운영은 황기속(Astragalus)에 속하며, 엽록체 역반복 서열이 없는 콩과 계통군(IRLC)에 든다[3, 8]. 유전체 비교에서 자운영은 같은 IRLC의 근연 콩과 식물들과 하나의 단계통군을 이루었다[3].\n\n"
     "식품원료 목록에는 같은 속 원료가 여럿 있으나 부위와 지위가 서로 다르다[1]. 황기(Astragalus membranaceus Bunge)는 뿌리·잎·싹, 트라가칸타수액(Astragalus gummifera)은 수액이 사용 가능 부위이고, 사원자(Astragalus complanatus R. Br.)는 '사용불가' 원료다[1]. 이 자료는 자운영만 다루며 황기 약재 자료와 섞지 않는다[1].\n\n"
     "중국 시장의 사원자 22개 시료를 조사한 연구에서 정품 A. complanatus 외에 A. adsurgens와 자운영 씨앗이 섞여 있었고, 박층크로마토그래피로 구별할 수 있었다[14]. HPLC 플라보노이드 지문으로도 정품 사원자와 자운영 씨앗이 구별되었다[15]. 황기속에는 셀레늄을 축적하는 종(A. bisulcatus, A. racemosus)이 있으나, 자운영은 비축적종으로 분류되어 비교되었다[21]."},
    {"key": "cultivation", "title": "재배와 생산", "body":
     "자운영은 가을걷이 뒤 빈 논에 심어 겨울을 나게 하는 녹비로 주로 재배된다[3]. 벼 휴경기에 자운영을 기르면 무기질소 비료의 40%를 대신하면서 벼 수량을 유지할 수 있다고 보고되었다[3]. 중국 남부 아홉 개 성 모의실험에서 자운영 생체량을 반영한 질소 시비량은 관행보다 합성 질소를 홑벼 29.6 ± 17.8%, 조생벼 65.3 ± 23.0% 줄였다[9]. 12년 연속 시험에서 자운영 환원(22.5·45 t/hm²)과 화학비료 감량을 함께 한 논은 무처리보다 토양 유기탄소가 12.7–35.5%, 총질소가 38.2–65.7% 많았다[10]. 현장 시험에서 자운영 환원은 벼 낟알의 카드뮴 농도를 49% 낮췄다[16].\n\n"
     "광둥 시험에서는 11월에 1 ha당 75.0 kg을 흩어 뿌려 126·132일 뒤 초기 개화기에 수확했고, 건물 수량은 1.76 t/ha였다[4]. 종자 생산 시험에서 꽃봉오리 시기 파클로부트라졸 엽면 살포는 373.10 mg/L에서 종자 수량이 가장 높았다[12]. 효율 높은 뿌리혹박테리아 균주를 동결건조 접종제와 종자 코팅으로 쓰는 방법도 연구되었다[23]. 병해로는 흰가루병[19]과 Embellisia 속 곰팡이에 의한 병[22]이 보고되었다. 국내 재배 면적·생산량 공식 통계와 농촌진흥청 재배 지침 원문은 확인하지 못함."},
    {"key": "processing", "title": "가공과 이용", "body":
     "식품원료 목록에서 자운영은 '자운영순'이라는 원료명으로만 올라 있어, 식품에는 어린 순을 쓴다[1]. 연한 어린 잎과 줄기를 먹고 꽃은 차로 우려 마신다는 기록이 있다[2].\n\n"
     "연구용 추출물은 대개 전초로 만든다[2, 7]. 한국 연구에서는 5월 초 전남 함평 농경지에서 채취한 전초(뿌리·줄기·잎·꽃)를 이틀 햇볕에 말리고, 2 kg을 70% 에탄올 40 L로 80 °C에서 6시간 추출해 동결건조 분말 0.5 kg을 얻었다[2]. 이 추출물에는 식품원료 목록이 허용하지 않은 뿌리·꽃이 들어 있어, 식품원료 '자운영순'과는 원료 부위가 다르다[1, 2]. 중국 연구는 자운영 물 추출물의 성분을 UPLC-QTOF-MS로 분석했다[7].\n\n"
     "녹비로 쓸 때는 지상부를 갈아엎어 분해시키며, 분해 침출액에서는 4-에틸페놀·알릴이소티오시아네이트 등 잡초 억제 후보 물질이 나왔다[18]. 물 추출물은 2% 농도에서 왕바랭이(goosegrass, Eleusine indica)의 발아를 크게 억제했다[24]. 식약처 「식품 등의 생산실적」 자료에서 자운영 품목은 확인하지 못함."},
    {"key": "genetics", "title": "유전 정보", "body":
     "2021년 중국 재래종 'Yijiangzi'로 염색체 수준 유전체가 처음 해독되었다[3]. 조립 길이는 595.52 Mb(추정 크기 625.15 Mb의 95.26%), 콘티그 N50은 1.50 Mb이며, 575.78 Mb가 8개 유사염색체에 배치되었다[3]. 단백질 암호화 유전자는 34,253개, 반복서열은 유전체의 59.84%이고 LTR 레트로트랜스포존이 45.52%를 차지했다[3].\n\n"
     "자운영은 두 차례 전체 유전체 중복을 겪었고, 플라보노이드 생합성의 첫 효소인 칼콘 합성효소(CHS) 유전자가 15개로 늘어나 주로 뿌리에서 발현되었다[3]. 저항성(R) 유전자 178개와 NCR 펩타이드 107개가 확인되었으며, 원자료는 NCBI BioProject PRJNA681368에 공개되었다[3].\n\n"
     "2026년에는 140개체를 재분석한 범엽록체 유전체가 나왔고, 개체들은 다섯 모계 계통(G1–G5)으로 나뉘었다[8]. 이 연구에서 trnQ-UUG 유전자는 다른 콩과와 달리 두 벌로 존재했다[8]. 칼콘 이성화효소 유전자 AsiCHI는 cDNA 972 bp, 열린 읽기틀 660 bp, 219개 아미노산을 암호화한다(GenBank OQ870547)[13]. 보라색 산성 인산분해효소 유전자 AsPPD1은 뿌리혹 형성과 질소고정에 관여한다[25]."},
    {"key": "safety", "title": "안전성", "body":
     "식품원료 목록에서 자운영의 사용 가능 부위는 순뿐이다[1]. 같은 속의 사원자(A. complanatus)는 '사용불가' 원료이며, 중국 시장에서는 자운영 씨앗이 사원자에 섞여 유통된 사례가 있다[1, 14]. 자운영 순의 알레르기·잔류농약·중금속에 관한 식약처 등 공공기관 정보는 확인하지 못함.\n\n"
     "자운영 전초에는 카나바닌·트리고넬린·콜린, 씨앗에는 카나바닌·카날린·쿠메스트롤·다이드진이 있다고 인용되었다[2]. 2014년 논문은 다이드진·트리고넬린·카나바닌을 줄기 성분으로 적어, 부위 기재가 문헌마다 다르다[6]. 비단백질 아미노산 카나바닌의 순 속 함량을 정량한 자료는 확인하지 못함.\n\n"
     "자운영은 카드뮴 오염 토양에서 내성 세균과 함께 카드뮴을 흡수해 정화에 쓰일 수 있다고 보고되었다[17]. 오염 논에서 자란 순의 카드뮴 함량 자료는 확인하지 못함. 셀레늄 효소 비교 연구에서 자운영은 셀레늄 비축적종으로 다뤄졌다[21].\n\n"
     "난소 절제 생쥐에 전초 에탄올 추출물을 30–300 mg/kg로 6주 먹인 실험에서 간·신장 무게는 군 사이에 차이가 없었다[2]. 고지방식 비만 생쥐에서도 물 추출물이 대사 지표를 개선했으나 모두 동물 실험이다[7]. 사람 대상 안전성 시험은 확인하지 못함."},
]

compounds = [
    {"name": "Crude protein", "name_ko": "조단백질", "class": "영양 성분(질소×6.25)", "role": "nutrient", "part": "지상부(초기 개화기, 건조)",
     "content_text": "212 ± 12.6 g/kg DM(두 작기 평균, 중국 광둥 겨울 논)[4]", "activity_ko": "콩과 녹비·사료로서 자운영의 질 지표; 비교한 다섯 작물 중 이탈리안 라이그라스(94.7 g/kg DM)보다 높음[4]", "source": [4]},
    {"name": "Soyasaponin I", "name_ko": "소야사포닌 I", "class": "트라이터펜 사포닌(올레아난형)", "role": "bioactive", "part": "씨앗",
     "content_text": "씨앗에서 분리·동정(메틸에스터 형태로 얻음), 함량 확인하지 못함[5]", "activity_ko": "씨앗에서 분리된 7종 트라이터펜 배당체 중 하나[5]", "source": [5]},
    {"name": "Soyasaponin IV", "name_ko": "소야사포닌 IV", "class": "트라이터펜 사포닌", "role": "bioactive", "part": "씨앗",
     "content_text": "씨앗에서 분리·동정, 함량 확인하지 못함[5]", "activity_ko": "씨앗 트라이터펜 배당체[5]", "source": [5]},
    {"name": "Soyasapogenol B 3-O-beta-D-glucuronopyranoside", "name_ko": "소야사포게놀 B 3-O-글루쿠로나이드", "class": "트라이터펜 사포닌", "role": "bioactive", "part": "씨앗",
     "content_text": "씨앗에서 분리·동정, 함량 확인하지 못함[5]", "activity_ko": "씨앗 트라이터펜 배당체[5]", "source": [5]},
    {"name": "Complogenin", "name_ko": "콤플로게닌(3β,22β,24-트라이하이드록시-11-옥소올레안-12-엔)", "class": "트라이터펜 사포게놀", "role": "marker", "part": "씨앗",
     "content_text": "씨앗 배당체 두 종(람노실-자일로실-글루쿠로나이드, 람노실-갈락토실-글루쿠로나이드)의 비당부, 효소 가수분해로 얻어 구조 확정; 함량 확인하지 못함[5]", "activity_ko": "자운영 씨앗 배당체에서 확인된 11-옥소 사포게놀[5]", "source": [5]},
    {"name": "Canavanine", "name_ko": "카나바닌", "class": "비단백질 아미노산", "role": "bioactive", "part": "전초·씨앗(인용)",
     "content_text": "전초와 씨앗에 있다고 인용됨[2]; 줄기 성분으로도 인용됨[6]; 함량 확인하지 못함", "activity_ko": "아르지닌 유사 비단백질 아미노산으로 안전성 확인이 필요한 성분; 순 속 함량은 확인하지 못함[2, 6]", "source": [2, 6]},
    {"name": "Canaline", "name_ko": "카날린(2-아미노-4-(아미노옥시)부탄산)", "class": "비단백질 아미노산", "role": "bioactive", "part": "씨앗(인용)",
     "content_text": "씨앗 성분으로 인용됨, 함량 확인하지 못함[2]", "activity_ko": "카나바닌과 함께 씨앗에서 보고된 아미노산[2]", "source": [2]},
    {"name": "Trigonelline", "name_ko": "트리고넬린", "class": "알칼로이드(피리딘)", "role": "bioactive", "part": "전초·줄기(인용)",
     "content_text": "전초 성분으로 인용됨[2]; 줄기 성분으로 인용됨[6]; 함량 확인하지 못함", "activity_ko": "자운영에서 보고된 알칼로이드 성분[2, 6]", "source": [2, 6]},
    {"name": "Choline", "name_ko": "콜린", "class": "4차 암모늄 화합물", "role": "nutrient", "part": "전초(인용)",
     "content_text": "전초 성분으로 인용됨, 함량 확인하지 못함[2]", "activity_ko": "전초에서 보고된 성분[2]", "source": [2]},
    {"name": "Daidzin", "name_ko": "다이드진", "class": "이소플라본 배당체", "role": "bioactive", "part": "씨앗·줄기(인용, 문헌마다 다름)",
     "content_text": "씨앗 성분으로 인용됨[2]; 줄기 성분으로 인용됨[6]; 함량 확인하지 못함", "activity_ko": "식물성 에스트로겐 계열 성분; 전초 에탄올 추출물은 MCF-7 세포·난소 절제 생쥐에서 에스트로겐 유사 작용을 보임(세포·동물 실험)[2]", "source": [2, 6]},
    {"name": "Coumestrol", "name_ko": "쿠메스트롤", "class": "쿠메스탄", "role": "bioactive", "part": "씨앗(인용)",
     "content_text": "씨앗 성분으로 인용됨, 함량 확인하지 못함[2]", "activity_ko": "식물성 에스트로겐으로 알려진 쿠메스탄 계열 성분[2]", "source": [2]},
    {"name": "Isomucronulatol", "name_ko": "(3R)-(−)-이소무크로눌라톨", "class": "이소플라반", "role": "bioactive", "part": "줄기(인용)",
     "content_text": "줄기 성분으로 인용됨, 함량 확인하지 못함[6]", "activity_ko": "줄기에서 보고된 이소플라반[6]", "source": [6]},
]

assays = [
    {"role": "literature", "compound": "Crude protein", "compound_ko": "조단백질(총질소×6.25)", "part": "지상부(초기 개화기 수확, 건조 분말)",
     "content": "212 ± 12.6 g/kg DM(2017–2018·2018–2019 두 작기 평균, 중국 광둥 겨울 논, 파종 후 126·132일 수확)[4]",
     "method": "켈달(Kjeldahl) 질소 정량, 조단백질 = 총질소 × 6.25",
     "conditions": {"instrument": "Nitrogen analyzer KN680(Shandong Jinan Alva Instrument)", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "",
                    "injection": "", "sample_prep": "구획마다 1 m × 1 m 지상부 수확 후 생체 2 kg을 70 °C에서 48시간 건조, 분쇄해 1.0 mm 체 통과", "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""},
     "rationale": "PubMed에서 자운영 순(지상부)의 특정 생리활성 성분을 HPLC 등으로 정량한 논문은 찾지 못했고, 고시·공전 지표성분도 없다[1]. 전문을 확인한 이 논문은 같은 종 지상부의 조단백질을 켈달법으로 정량했으며, 콩과 녹비·사료로서 자운영의 질소 공급력을 보여 주는 기본 지표다[4]. 검출·정량한계와 회수율은 원문에 없다[4].",
     "source": [4], "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10825004/", "source_kind": "paper"},
]

d = {
    "slug": "astragalus-sinicus",
    "name_ko": "자운영",
    "name_en": "Chinese milk vetch",
    "scientific_name": "Astragalus sinicus L.",
    "aliases": ["자운영순", "야화생", "Chinese Milkvetch", "Chinese milk vetch", "milk vetch", "Astragalus sinicus"],
    "sections": sections,
    "compounds": compounds,
    "markers": [],
    "assays": assays,
    "nutrients": [],
    "production": [],
    "world": [],
    "gi": [],
    "orgs": [],
    "sources": sources,
}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in sections:
    print(s["key"], len(s["body"]))
