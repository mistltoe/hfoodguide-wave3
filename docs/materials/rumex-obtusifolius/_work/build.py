import json
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "dossier.json"
ACC = "2026-11-02"


def pm(n, title, pmid, doi=None, pmc=None, pub=""):
    url = f"https://doi.org/{doi}" if doi else f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
    t = title + (f" ({pmc})" if pmc else "")
    p = (pub + " " if pub else "") + f"(PubMed PMID {pmid})"
    return {"n": n, "title": t, "url": url, "publisher": p.strip(), "accessed": ACC}


sources = [
    {"n": 1, "title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 돌소리쟁이잎(Rumex obtusifolius L.)",
     "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
    pm(2, "Aluminium uptake and translocation in Al hyperaccumulator Rumex obtusifolius is affected by low-molecular-weight organic acids content and soil pH. PLoS One 2015;10(4):e0123351", "25880431", "10.1371/journal.pone.0123351", "PMC4400109", "PLOS (PubMed Central)"),
    pm(3, "Oxalate synthesis pathways that contribute to oxalate accumulation in leaves of bitter dock (Rumex obtusifolius L.) differ between day and night. Plant Biotechnol (Tokyo) 2026;43(1):89-94", "42137029", "10.5511/plantbiotechnology.25.1124a", "PMC13170793", "일본식물세포분자생물학회 (PubMed Central)"),
    pm(4, "Evaluation of metabolic changes in oxalate-rich plant Rumex obtusifolius L. caused by ion beam irradiation. Plant Physiol Biochem 2017;122:40-45 (초록 확인)", "29172104", "10.1016/j.plaphy.2017.11.001", None, "Elsevier"),
    pm(5, "Comparing the Above and Below-Ground Chemical Defences of Three Rumex Species Between Their Native and Introduced Provenances. J Chem Ecol 2023;49(5-6):276-286", "37121960", "10.1007/s10886-023-01427-0", "PMC10495513", "Springer (PubMed Central)"),
    pm(6, "Molecular evidence for natural hybridization between Rumex crispus and R. obtusifolius (Polygonaceae) in Korea. Sci Rep 2022;12:5423", "35361815", "10.1038/s41598-022-09292-9", "PMC8971494", "Nature Portfolio (PubMed Central)"),
    pm(7, "Hybridization between alien species Rumex obtusifolius and closely related native vulnerable species R. longifolius in a mountain tourist destination. Sci Rep 2015;5:13898 (초록 확인)", "26354180", "10.1038/srep13898", "PMC4564823", "Nature Portfolio"),
    pm(8, "Variation in Phenolic Compounds Content and Antioxidant Activity of Different Plant Organs from Rumex crispus L. and Rumex obtusifolius L. at Different Growth Stages. Antioxidants (Basel) 2019;8(7):237", "31340505", "10.3390/antiox8070237", "PMC6680865", "MDPI (PubMed Central)"),
    pm(9, "Isolation and characterisation of procyanidins from Rumex obtusifolius. Phytochem Anal 2007;18(3):193-203 (초록 확인)", "17500361", "10.1002/pca.967", None, "Wiley"),
    pm(10, "Identification and Structural Elucidation of Galloylated B-Type Procyanidins From Rumex obtusifolius L. Using Enzymatic Digestion, Phloroglucinolysis, and High-Resolution Mass Spectrometry. J Sep Sci 2026;49(4):e70396 (초록 확인)", "41906417", "10.1002/jssc.70396", "PMC13033918", "Wiley"),
    pm(11, "Naphthalene-Type Glycosides from Rumex obtusifolius Roots and Their Protective Effects Against Muscle Atrophy in C2C12 Myotubes. Pharmaceutics 2026;18(7):807 (초록 확인)", "42514887", "10.3390/pharmaceutics18070807", "PMC13414561", "MDPI"),
    pm(12, "5-fluorouracil and Rumex obtusifolius extract combination trigger A549 cancer cell apoptosis: uncovering PI3K/Akt inhibition by in vitro and in silico approaches. Sci Rep 2024;14:14676", "38918540", "10.1038/s41598-024-65816-5", "PMC11199614", "Nature Portfolio (PubMed Central)"),
    pm(13, "Anti-cancer effect of Rumex obtusifolius in combination with arginase/nitric oxide synthase inhibitors via downregulation of oxidative stress, inflammation, and polyamine synthesis. Int J Biochem Cell Biol 2023;158:106396 (초록 확인)", "36918141", "10.1016/j.biocel.2023.106396", None, "Elsevier"),
    pm(14, "Biochemical Activity and Hypoglycemic Effects of Rumex obtusifolius L. Seeds Used in Armenian Traditional Medicine. Biomed Res Int 2018:4526352 (초록 확인)", "30533432", "10.1155/2018/4526352", "PMC6247722", "Hindawi"),
    pm(15, "Anti-Candida and antioxidant activities of hydroalcohlic extract of Rumex obtusifolius leaves. Pak J Pharm Sci 2019;32(3):919-926 (초록 확인)", "31278700", None, None, ""),
    pm(16, "Mothers' groups enrich diet and culture through promoting traditional Quichua foods. Matern Child Nutr 2017;13 Suppl 3:e12530 (초록 확인)", "29359438", "10.1111/mcn.12530", "PMC6866126", "Wiley"),
    pm(17, "Ethnoveterinary herbal remedies used by farmers in four north-eastern Swiss cantons. J Ethnobiol Ethnomed 2014;10:32 (초록 확인)", "24685062", "10.1186/1746-4269-10-32", "PMC4022237", "BioMed Central"),
    pm(18, "Can the soil seed bank of Rumex obtusifolius in productive grasslands be explained by management and soil properties? PLoS One 2023;18(6):e0286760 (초록 확인)", "37267389", "10.1371/journal.pone.0286760", "PMC10237634", "PLOS"),
    pm(19, "Synergistic effects of grass competition and insect herbivory on the weed Rumex obtusifolius in an inundative biocontrol approach. Sci Rep 2023;13:18508 (초록 확인)", "37898617", "10.1038/s41598-023-45609-y", "PMC10613235", "Nature Portfolio"),
    pm(20, "Storage on Maternal Plants Affects Temperature Requirements during Germination in Rumex obtusifolius. Plants (Basel) 2023;12(13):2403 (초록 확인)", "37446964", "10.3390/plants12132403", "PMC10346210", "MDPI"),
    pm(21, "Characterization of glucosylceramides in the Polygonaceae, Rumex obtusifolius L. injurious weed. Biosci Biotechnol Biochem 2011;75(5):877-81 (초록 확인)", "21597180", "10.1271/bbb.100802", None, "일본농예화학회"),
    pm(22, "Copper accumulation in five weed species commonly found in the understory vegetation of Mediterranean vineyards. Environ Pollut 2023;329:121675 (초록 확인)", "37085100", "10.1016/j.envpol.2023.121675", "PMC10204647", "Elsevier"),
    pm(23, "Plant uptake and availability of antimony, lead, copper and zinc in oxic and reduced shooting range soil. Environ Pollut 2018;238:255-262 (초록 확인)", "29567447", "10.1016/j.envpol.2018.03.014", None, "Elsevier"),
    {"n": 24, "title": "EFSA ANS Panel. Safety of hydroxyanthracene derivatives for use in food. EFSA Journal 2018;16(1):e05090 (PMC7009633)",
     "url": "https://doi.org/10.2903/j.efsa.2018.5090", "publisher": "유럽식품안전청(EFSA)", "accessed": ACC},
    {"n": 25, "title": "EFSA Compendium of botanicals — Rumex obtusifolius 항목(card.json 의 생물자원 DB 후보 성분 정보로 확인, Compendium 원문은 직접 확인하지 못함)",
     "url": "https://www.efsa.europa.eu/en/data-report/compendium-botanicals", "publisher": "유럽식품안전청(EFSA)", "accessed": "2026-10-13"},
    pm(26, "The effects of condensed tannins extracted from different plant species on egg hatching and larval development of Teladorsagia circumcincta. Folia Parasitol 2010;57(1):62-8 (초록 확인)", "20450000", "10.14411/fp.2010.008", None, "체코과학원 기생충학연구소"),
    pm(27, "In Vitro Antitrypanosomal and Antibacterial Activity of Aqueous, Hydroethanolic and Ethanolic Extracts of Rumex obtusifolius L. Leaf and Root. Basic Clin Pharmacol Toxicol 2026;138(5):e70230 (초록 확인)", "41948979", "10.1111/bcpt.70230", "PMC13059062", "Wiley"),
    pm(28, "Restoration management of cattle resting place in mountain grassland. PLoS One 2021;16(4):e0249445 (초록 확인)", "33793653", "10.1371/journal.pone.0249445", "PMC8016235", "PLOS"),
    pm(29, "Evaluation of the Effects of Rumex obtusifolius Seed and Leaf Extracts Against Acanthamoeba: An in vitro Study. Infect Disord Drug Targets 2021;21(2):211-219 (초록 확인)", "32321413", "10.2174/1871526520666200422111044", None, "Bentham Science"),
    pm(30, "Detection of the herbicide asulam in groundwater: translocation to roots of treated docks (Rumex) and exudation to subsoil as a potential input pathway. Pest Manag Sci 2025;81(7):4135-4142 (초록 확인)", "40116015", "10.1002/ps.8779", None, "Wiley"),
]

sections = [
    {"key": "overview", "title": "한눈에 보기", "body":
     "돌소리쟁이(Rumex obtusifolius L.)는 마디풀과(Polygonaceae) 소리쟁이속의 여러해살이풀로, 영어로는 broad-leaved dock 또는 round-leaved dock이라 부른다[1][2]. 유럽과 서남아시아가 원산이지만 남아프리카·남북아메리카·남아시아와 동북아시아·오스트레일리아에도 귀화했고, 한국에서는 침입 외래종으로 여겨진다[6].\n\n"
     "식품의약품안전처 「식품원료 목록」에서 돌소리쟁이는 원료명 '돌소리쟁이잎'으로 올라 있는 식품원료(사용가능)이며, 사용 조건은 '사용가능부위 : 잎'이다[1]. 목록에는 이명 Lapathum obtusifolium (L.) Moench와 Lapathum sylvestre Lam.이 함께 적혀 있고, 별도의 국문 다른 이름은 없다[1]. 건강기능식품 고시형 원료의 원재료로 쓰인다는 기록은 확인하지 못함.\n\n"
     "잎은 옥살산(옥살레이트)을 많이 쌓는 '옥살레이트 식물'로 분류되며, 잎의 저분자 유기산 가운데 옥살산이 가장 많았다[2][3]. 에콰도르 고지대 원주민 공동체에서는 쐐기풀과 함께 어린이 식단을 보충하는 야생 잎채소로 권장되었다[16]. 뿌리와 씨에는 안트라퀴논·나프탈렌 배당체·축합 탄닌 같은 성분이 보고되어 있으나, 식품원료로 쓸 수 있는 부위는 잎뿐이다[1][10][11][12][25]. 소리쟁이(R. crispus) 등 같은 속 다른 원료와는 서로 다른 종이므로 이 자료에는 돌소리쟁이를 직접 다룬 연구만 모았다[1][6]."},
    {"key": "history", "title": "역사", "body":
     "민간에서는 열매·줄기·잎·뿌리를 달인 물을 수렴제·완하제·강장제로 쓰고, 궤양·물집·화상·당뇨병 치료에도 썼다고 정리되어 있다[8]. 아르메니아 전통의학에서는 씨를 썼으며, 아르메니아에서는 흔한 식용 식물로 야생에서 채취해 지역 시장에서 팔린다고 보고되었다[12][14].\n\n"
     "스위스 북동부 4개 주 농가 50명을 면담한 2012년 민족수의학 조사에서 돌소리쟁이는 가축용 단일 식물 가정 치료제가 가장 많이 언급된 식물 가운데 하나였다[17]. 조사 전체에서 가정 치료제는 주로 피부병·상처, 그다음으로 소화기 질환과 대사 이상에 쓰였고, 바르는 방법이 가장 흔했다[17].\n\n"
     "에콰도르 퉁구라우아 고지대 키추아 공동체에서는 어머니 모임이 요리 모임과 조리법 경연으로 돌소리쟁이와 쐐기풀 같은 전통 야생 잎채소 소비를 권장했다[16]. 이 사업에서 두 잎채소는 어린이 권장 섭취량의 비타민 A 8%, 철 7%, 비타민 C 12%, 엽산 27%를 추가로 채우는 것으로 추정되었다[16]. 한국에서 돌소리쟁이를 나물로 먹어 온 전통이나 고문헌 기록은 이번 조사에서 확인하지 못함."},
    {"key": "biology", "title": "식물학적 특징", "body":
     "돌소리쟁이의 뿌리잎과 아래쪽 줄기잎은 대개 달걀꼴에서 타원형 또는 긴 달걀꼴이고 가장자리가 밋밋하며, 열매를 싸는 꽃덮이 조각(valve)은 세모진 달걀꼴로 가장자리에 가시 같은 톱니가 있다[6]. 잎이 피침형이고 가장자리가 심하게 주름지며 꽃덮이 조각 가장자리가 밋밋한 소리쟁이와는 이 형질로 구별한다[6].\n\n"
     "유럽 온대 초지에서 가장 문제가 되는 토착 잡초로 꼽히며, 사료의 수량과 영양가를 떨어뜨린다[18][19]. 스위스·슬로베니아·영국의 집약 초지에서 돌소리쟁이가 많은 구획의 흙에서는 1 m²당 평균 628–866개의 씨가 발아했고, 많은 곳은 약 3,000개에 이르렀다[18]. 갓 거둔 씨는 휴면이 없어 발아율이 최대 92%였고, 포기에 매달린 채로 10개월까지 활력을 유지해 1년 내내 토양 씨앗은행에 씨를 보탤 수 있다[20].\n\n"
     "땅 위 부분을 베어도 땅속줄기(근경)에서 새 잎이 돋아 없애기 어렵고, 산성 토양·알루미늄 스트레스·저온에 대한 내성이 크다[3]. 처리하지 않은 알칼리성 오염 토양에서 키운 화분 시험에서 잎의 알루미늄 총량은 3,413 mg/kg(건조중량)으로 알루미늄 과다축적 식물 기준(3,000 mg/kg 초과)을 넘었다[2]."},
    {"key": "related_species", "title": "근연종", "body":
     "소리쟁이속(Rumex)은 약 200종으로 이루어지며 종 사이 잡종이 흔한 무리다[6]. 한국에서는 소리쟁이속 12종이 보고되었고, 전북 내소사 일대와 부산 가덕도의 혼생 집단에서 돌소리쟁이와 소리쟁이의 중간 형태 개체가 발견되었다[6]. 핵 DNA(pgiC)와 엽록체 DNA 5개 구간 분석으로 이 개체들이 두 종의 자연 잡종과 그 역교배 세대임이 확인되었고, 두 종 모두 어미 쪽이 될 수 있는 양방향 교잡이었다[6].\n\n"
     "일본 중부 산악 관광지에서는 외래종인 돌소리쟁이가 토착 취약종 Rumex longifolius와 교잡했으며, 잡종은 대부분 1대 잡종(F1)이고 꽃가루와 씨의 발아율이 두 부모 종보다 훨씬 낮았다[7]. 돌소리쟁이는 주로 길가와 풀밭에, R. longifolius와 잡종은 습지와 하천 지류에 자라 서식지 수분 조건이 달랐다[7].\n\n"
     "식품원료 목록에는 소리쟁이(R. crispus)·수영(R. acetosa)·참소리쟁이(R. japonicus)·애기수영·금소리쟁이·Rumex patientia 같은 같은 속 원료가 따로 올라 있다[1]. 이 자료에는 그 종들의 성분·안전성 값을 섞지 않았으며, 소리쟁이와 함께 분석한 연구에서도 돌소리쟁이에 해당하는 내용만 옮겼다[1][8]. 두 종은 교잡 경향이 강해, 비교 연구에서는 시료를 서로 멀리 떨어진 곳에서 따로 채집했다[8]."},
    {"key": "cultivation", "title": "재배와 채취", "body":
     "돌소리쟁이를 작물로 재배한 국내 생산 통계(면적·생산량)는 확인하지 못함. 국내 잡종 연구의 채집지는 길가·묵은 밭·숲 가장자리 빈터·하천변 같은 교란지였다[6]. 아르메니아에서는 야생 개체를 채취해 시장에서 판다[12].\n\n"
     "초지에서는 관리 대상 잡초로, 토양 씨앗은행의 크기는 토양 pH·미사 함량·토지 이용 강도와 음의 관계, 지상부 개체 밀도와 양의 관계를 보였다[18]. 연구진은 성숙 개체 밀도를 줄이고 씨 생산·확산을 막으며 토양 pH를 사료 생산에 알맞게 조절하는 관리를 권했다[18]. 호밀풀(Lolium perenne)과 경쟁시키면 지상부 생물량이 약 62분의 1, 최종 뿌리 무게가 약 7.5분의 1로 줄었고, 뿌리를 파먹는 곤충을 접종하면 그 효과가 더 커졌다[19].\n\n"
     "슬로바키아 산지 초지의 소 휴식지처럼 양분이 지나치게 많은 땅에서는 쐐기풀과 함께 무성해지며, 연 2회 베기와 제초제 처리만으로는 초지 복원이 어려웠다[28]. 스위스 지하수에서 자주 검출된 제초제 아술람은 소리쟁이류 잎에 뿌리면 뿌리로 빠르게 옮겨 가며, 돌소리쟁이 온실 시험에서는 뿌리 밖으로 배출되어 토양 침출수에서 수 µg/L로 검출되었다[30]."},
    {"key": "processing", "title": "가공과 이용", "body":
     "식품원료 목록에 오른 돌소리쟁이 원료는 '돌소리쟁이잎' 하나이며, 사용 부위는 잎으로 한정된다[1]. 잎은 다른 여러 소리쟁이속 식물보다 비타민 C와 아미노산 함량이 높다고 보고되었으나, 수치는 초록에서 확인하지 못함[4]. 소리쟁이속 일부 종은 어린잎 샐러드 채소로 먹지만 잎에 쌓이는 수용성 옥살산이 신장 질환을 일으킬 수 있어, 이온빔 돌연변이로 옥살산이 적은 개체를 만들려는 연구가 이루어졌다[4]. 그러나 탄소 이온빔을 쬔 잎에서는 오히려 옥살산이 늘었다[4].\n\n"
     "잎을 끓는 물에 15분 우린 액에서는 잎 속 알루미늄 총량의 약 2%가 녹아 나왔으며, 연구진은 차보다는 샐러드나 수프 재료로 먹는다는 점에서 알루미늄 노출 위험이 남는다고 보았다[2]. 잎을 아세톤–물(7:3)로 추출한 뒤 세파덱스 LH-20으로 분획하면 프로시아니딘 올리고머와 중합체를 얻을 수 있다[9]. 잎과 뿌리의 물·물–에탄올·에탄올 추출물은 실험실에서 항트리파노소마 활성을 시험하는 재료로 쓰였다[27]. 잎 수알코올 추출물은 병원성 칸디다 분리주 40주를 대상으로 한 시험관 실험에서 최소억제농도 200–250 µg/µL(원문 단위)를 보였다[15]. 잎 수알코올 추출물 10 mg/mL은 72시간 뒤 가시아메바 영양형과 포낭을 모두 죽였지만, 연구진은 치료제 후보로 유망하지 않다고 결론지었다[29].\n\n"
     "씨는 96% 에탄올로 침지 추출해(용매:시료 10:1) 수율 10.60%의 조추출물을 얻었다[12]. 식약처 「식품 등의 생산실적」에서 돌소리쟁이 원료 품목의 생산 기록은 확인하지 못함."},
    {"key": "genetics", "title": "유전체와 유전 다양성", "body":
     "국내 혼생 집단 연구에서는 핵 DNA pgiC 구간과 엽록체 DNA 5개 구간(matK, rbcL-accD IGS, trnK-rps16 IGS, ycf6-psbM IGS, psbA-trnH IGS)을 분석했다[6]. 돌소리쟁이와 소리쟁이는 pgiC 단상형을 서로 공유하지 않았고, 잡종 개체는 두 부모의 pgiC 단상형을 함께 지녀 1대 잡종임이 드러났다[6]. 일부 잡종은 한쪽 부모의 핵 단상형만 남아 역교배·유전자 이입이 일어났음을 시사했다[6].\n\n"
     "같은 연구는 한국의 참소리쟁이 집단이 잡종 기원일 가능성이 크고, 그 부모 가운데 하나가 소리쟁이일 수 있다고 보았다[6]. 일본 연구에서 돌소리쟁이와 R. longifolius의 잡종은 군집 분석에서 두 부모와 구별되는 무리를 이루었고, 대부분 F1이어서 역교배를 통한 유전자 이입 가능성은 낮지만 배제할 수 없다고 했다[7].\n\n"
     "돌소리쟁이의 엽록체 전장 유전체, 핵 유전체 조립본, 정확한 염색체 수는 이번 조사에서 PubMed로 확인하지 못함. 잎의 글루코실세라마이드 분석에서는 긴사슬 염기의 8번 위치 Z·E 이성질체 비율로 마디풀과 10종을 다른 과 식물과 구별할 수 있었다[21]."},
    {"key": "safety", "title": "안전성", "body":
     "돌소리쟁이는 건강기능식품 고시형 원료가 아니어서 고시에 따른 섭취 시 주의사항은 확인하지 못함. 식품원료 목록상 사용할 수 있는 부위는 잎뿐이다[1]. 국내 공공기관의 알레르기·잔류농약 정보는 확인하지 못함.\n\n"
     "가장 큰 주의점은 옥살산이다[2][3]. 옥살산은 위장 점막을 자극하고 체내 칼슘과 결합해 칼슘 결핍 증상을 일으키며, 신장 결정으로 요관이 막히면 심하면 숨질 수 있다[3]. 돌소리쟁이는 다른 소리쟁이속 식물보다 수용성 옥살산을 더 많이 쌓는다고 보고되었다[3]. 오염 토양 화분 시험에서 잎 우림액의 옥살산은 건조중량 1 kg당 10,884–14,594 mg으로 잎 저분자 유기산의 39%를 차지했다[2]. 온실에서 60일 키운 개체에서는 옥살산이 잎에서만 나오고 뿌리에서는 검출되지 않았다[5].\n\n"
     "뿌리에는 1,8-디하이드록시안트라퀴논 유도체가 최대 4%, 탄닌이 최대 20% 들어 있다고 EFSA 식물성분 목록에 정리되어 있다[25]. EFSA는 하이드록시안트라센 유도체를 반대 근거가 없는 한 유전독성·발암성 물질로 보아야 하며 안전한 1일 섭취량을 정할 수 없다고 결론지었다[24]. 잎의 안트라퀴논 정량 자료는 확인하지 못함.\n\n"
     "구리 살균제를 쓴 지중해 포도밭에서는 잎의 구리가 100 µg/g을 넘었다[22]. 사격장 오염 토양에서는 지상부 납·구리·아연이 대체로 사료 기준 아래였다[23]. 잎 에탄올 추출물 2%는 24시간 뒤 포유류 세포 생존율을 14.3%로 떨어뜨렸다(세포 실험)[27]. 씨 추출물의 항암·혈당 저하 결과는 세포·동물 실험일 뿐이다[12][13][14]."},
]

compounds = [
    {"name": "Oxalic acid", "name_ko": "옥살산(옥살레이트)", "class": "유기산(항영양소)", "role": "marker", "part": "잎",
     "content_text": "잎 우림액 기준 10,884–14,594 mg/kg 건조중량(오염 토양 화분 시험, 처리별 평균), 잎 저분자 유기산의 39%[2]; 뿌리에서는 검출되지 않음[5]",
     "activity_ko": "칼슘과 결합해 저칼슘 증상·신장 결정의 원인이 되는 항영양소[3]; 식물 안에서는 알루미늄과 강한 착물을 만들어 내성에 관여[2]",
     "source": [2, 3, 5]},
    {"name": "Citric acid", "name_ko": "시트르산", "class": "유기산", "role": "nutrient", "part": "땅속기관·잎",
     "content_text": "땅속기관 5,202–8,825 mg/kg, 잎 3,875–6,754 mg/kg(건조중량, 우림액 기준)[2]",
     "activity_ko": "땅속기관에서 가장 많은 유기산으로 알루미늄과 강한 착물을 형성[2]", "source": [2]},
    {"name": "Malic acid", "name_ko": "말산", "class": "유기산", "role": "nutrient", "part": "줄기·잎",
     "content_text": "줄기 6,504–8,769 mg/kg, 잎 2,197–4,527 mg/kg(건조중량, 우림액 기준)[2]",
     "activity_ko": "줄기에서 가장 많은 유기산[2]", "source": [2]},
    {"name": "Ascorbic acid", "name_ko": "아스코르브산(비타민 C)", "class": "비타민", "role": "nutrient", "part": "잎",
     "content_text": "정량값은 확인하지 못함; 다른 여러 소리쟁이속 식물보다 많다고 보고[4]",
     "activity_ko": "낮에는 아스코르브산 경로가 잎 옥살산 합성에 기여하는 것으로 해석[3]", "source": [3, 4]},
    {"name": "Procyanidin B2", "name_ko": "프로시아니딘 B2(축합 탄닌)", "class": "프로안토시아니딘", "role": "bioactive", "part": "잎",
     "content_text": "잎 아세톤–물 추출물에서 B1·B2·B3·B7 이량체, A형 삼량체, B2 3,3'-O-디갈레이트 분리; 평균 중합도 4.3(단계 분획)[9]",
     "activity_ko": "돌소리쟁이 축합 탄닌은 양 기생선충 알의 발육을 억제(시험관)[26]", "source": [9, 26]},
    {"name": "Procyanidin B2 3-O-gallate", "name_ko": "프로시아니딘 B2-3-O-갈레이트", "class": "갈로일화 프로시아니딘", "role": "bioactive", "part": "뿌리",
     "content_text": "뿌리에서 분리한 갈로일화 이량체 5종 가운데 하나(정량값 없음)[10]",
     "activity_ko": "이 종에서 처음 보고된 갈로일화 B형 프로시아니딘[10]", "source": [10]},
    {"name": "Epicatechin", "name_ko": "에피카테킨", "class": "플라반-3-올", "role": "bioactive", "part": "잎",
     "content_text": "잎 프로시아니딘의 가장 많은 연장 단위; 말단 단위는 카테킨·에피카테킨·에피카테킨 갈레이트가 같은 비율[9]",
     "activity_ko": "축합 탄닌의 구성 단위[9]", "source": [9]},
    {"name": "Tannins", "name_ko": "탄닌", "class": "폴리페놀", "role": "bioactive", "part": "뿌리·지하부",
     "content_text": "뿌리 최대 20%[25]; 뿌리가 잎보다 탄닌 농도가 높은 경향[5]",
     "activity_ko": "초식 곤충에 대한 화학 방어 물질[5]", "source": [25, 5]},
    {"name": "1,8-dihydroxyanthraquinone", "name_ko": "1,8-디하이드록시안트라퀴논 유도체", "class": "하이드록시안트라센 유도체", "role": "bioactive", "part": "뿌리·지하부",
     "content_text": "뿌리 최대 4%[25]",
     "activity_ko": "EFSA가 유전독성·발암 우려를 지적한 성분군[24]", "source": [25, 24]},
    {"name": "Emodin", "name_ko": "에모딘", "class": "안트라퀴논", "role": "bioactive", "part": "씨(에탄올 추출물)",
     "content_text": "씨 에탄올 추출물에서 확인(정량값 없음)[12]; 이 종에서 보고된 안트라센 유도체 가운데 하나[8]",
     "activity_ko": "컴퓨터 모의 실험에서 PI3K·Akt 결합 친화도가 높게 예측됨(실험 검증 아님)[12]; EFSA가 유전독성을 지적[24]", "source": [12, 8, 24]},
    {"name": "Endocrocin", "name_ko": "엔도크로신", "class": "안트라퀴논", "role": "bioactive", "part": "씨(에탄올 추출물)",
     "content_text": "씨 에탄올 추출물에서 확인(정량값 없음)[12]",
     "activity_ko": "컴퓨터 모의 실험에서 Akt 결합 점수가 상위였음[12]", "source": [12]},
    {"name": "Nepodin", "name_ko": "네포딘", "class": "나프탈렌 유도체", "role": "bioactive", "part": "뿌리",
     "content_text": "뿌리에서 나프탈렌형 배당체 4종 분리, 그중 네포딘-8-O-β-D-(6'-O-말로닐)글루코피라노사이드는 신규(정량값 없음)[11]; 네포딘은 이 종의 보고 성분[8]",
     "activity_ko": "분리 배당체 하나가 근육세포(C2C12) 위축 모델에서 근관 직경을 회복(세포 실험)[11]", "source": [11, 8]},
    {"name": "Quercetin", "name_ko": "퀘르세틴", "class": "플라보놀", "role": "bioactive", "part": "씨(에탄올 추출물)",
     "content_text": "씨 에탄올 추출물에서 확인(정량값 없음)[12]",
     "activity_ko": "컴퓨터 모의 실험 상위 화합물[12]", "source": [12]},
    {"name": "Glucosylceramide", "name_ko": "글루코실세라마이드", "class": "스핑고당지질", "role": "bioactive", "part": "잎",
     "content_text": "잎에서 2-하이드록시 지방산(C22·C24 n-9 단일불포화)이 많은 분자종 확인(정량값 없음)[21]",
     "activity_ko": "마디풀과를 다른 과와 구별하는 화학분류 지표[21]", "source": [21]},
]

assays = [
    {"role": "literature", "compound": "Oxalic acid", "compound_ko": "옥살산(옥살레이트)과 저분자 유기산 9종", "part": "땅속기관·줄기·잎(우림액)",
     "content": "잎 10,884–14,594 mg/kg, 줄기 4,427–8,449 mg/kg, 땅속기관 1,355–1,570 mg/kg(건조중량, 처리별 평균)[2]",
     "method": "이온교환 크로마토그래피(억제 전도도 검출)",
     "conditions": {"instrument": "Dionex ICS 1600 이온 크로마토그래프", "column": "IonPac AS11-HC 보호 칼럼 + 분석 칼럼(Dionex)",
                    "mobile_phase": "KOH 용리액", "gradient": "KOH 1–37.5 mM, 1–50분 기울기", "flow": "1 mL/min", "temp": "",
                    "detection": "억제 전도도(ASRS 300 4 mm 서프레서 + 탄산염 제거 장치 CRD 200)", "injection": "",
                    "sample_prep": "기관별 생물량과 끓는 탈이온수를 1:50(w/v)으로 섞어 15분 우린 뒤 여과지(공극 3–5 µm)로 거르고 0.45 µm 나일론 막으로 다시 여과",
                    "standard": "", "linearity": "", "lod": "옥살산 1.08 mg/kg(시트르산 3.18, 말산 1.85 mg/kg 등)", "loq": "", "recovery": ""},
     "rationale": "식품 부위인 잎의 안전성 지표(항영양소)를 이 종에서 직접 정량했다[2]. 다만 비소·카드뮴·납·아연에 심하게 오염된 토양의 화분 시험이고 우림액(침출) 기준이어서 총 옥살산·생잎 함량과는 다르다[2].",
     "source": [2], "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC4400109/", "source_kind": "paper"},
    {"role": "literature", "compound": "Oxalic acid", "compound_ko": "수용성·총 옥살산", "part": "지상부·뿌리(건조 분말)",
     "content": "종별 수치는 그림으로만 제시되어 본문 숫자는 확인하지 못함; 뿌리에서는 검출되지 않음[5]",
     "method": "HPLC-UV(이온 배제 칼럼)",
     "conditions": {"instrument": "Waters 717 Plus 자동시료주입기, Waters 600 펌프, Waters UV/VIS 검출기", "column": "Aminex HPX-87H 이온 배제 칼럼 300 × 7.8 mm + Cation-H 보호 칼럼",
                    "mobile_phase": "0.0125 M 황산", "gradient": "등용매", "flow": "0.5 mL/min", "temp": "실온",
                    "detection": "UV 210 nm", "injection": "5 µL",
                    "sample_prep": "65 °C에서 48시간 건조·분쇄한 시료 0.400–0.405 g을 증류수 40 mL(수용성) 또는 2 M HCl 40 mL(총량)에 넣어 80 °C 수조에서 20분, 100 mL로 정용 후 3,000 rpm 원심분리, 0.45 µm 셀룰로오스아세테이트 막 여과",
                    "standard": "옥살산 1–20 mg/100 mL 검량선(증류수 또는 2 M HCl로 희석)", "linearity": "", "lod": "", "loq": "", "recovery": ""},
     "rationale": "수용성과 총 옥살산을 나눠 재는 방법으로, 영국(원산지)과 뉴질랜드(도입지) 계통 사이에 잎 옥살산 차이가 없음을 보였다[5]. 검출·정량한계와 회수율은 본문에 없어 비워 둠.",
     "source": [5], "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10495513/", "source_kind": "paper"},
    {"role": "literature", "compound": "Oxalic acid", "compound_ko": "옥살산과 관련 대사물질 37종", "part": "새로 난 잎",
     "content": "수치는 그림·보충자료로만 제시되어 본문 숫자는 확인하지 못함; 이타콘산 처리 시 어두운 조건에서만 크게 감소[3]",
     "method": "CE-MS/MS(모세관 전기영동–삼중사중극자 질량분석, MRM)",
     "conditions": {"instrument": "Agilent CE 7100 + G6420A 삼중사중극자 질량분석기", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "",
                    "detection": "다중반응검지(MRM)", "injection": "",
                    "sample_prep": "새로 난 잎을 액체질소로 급속 동결해 −80 °C 보관 후 선행 연구 방법(일부 수정)으로 추출",
                    "standard": "농도를 아는 표준물질로 정량 정확도 확인", "linearity": "", "lod": "", "loq": "", "recovery": ""},
     "rationale": "잎 옥살산이 낮에는 아스코르브산 경로, 밤에는 이소시트르산 경로로 주로 만들어진다는 해석의 근거 측정이다[3]. 추출·분리 조건 세부는 인용 문헌에 있어 본문에서 확인하지 못함.",
     "source": [3], "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC13170793/", "source_kind": "paper"},
]

d = {
    "slug": "rumex-obtusifolius",
    "name_ko": "돌소리쟁이",
    "name_en": "Broad-leaved dock (round-leaved dock, bitter dock)",
    "scientific_name": "Rumex obtusifolius L.",
    "aliases": ["돌소리쟁이잎", "Broad-leaved dock", "Round-leaved dock", "Bitter dock", "Lapathum obtusifolium (L.) Moench", "Lapathum sylvestre Lam."],
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
print("ok")
