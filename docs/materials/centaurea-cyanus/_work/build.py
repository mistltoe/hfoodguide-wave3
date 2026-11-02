import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
ACC = "2026-11-02"

def pm(n, title, pmid, pmc=None, doi=None):
    url = f"https://pmc.ncbi.nlm.nih.gov/articles/{pmc}/" if pmc else f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
    t = title + (f" (doi:{doi})" if doi else "")
    pub = f"PubMed (PMID {pmid}" + (f", {pmc})" if pmc else ")")
    return {"n": n, "title": t, "url": url, "publisher": pub, "accessed": ACC}

sources = [
 {"n": 1, "title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 수레국화꽃잎·수레국화추출물(Centaurea cyanus L.) 항목", "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
 pm(2, "Shiono M et al. Phytochemistry: structure of the blue cornflower pigment. Nature 2005;436:791", "16094358", doi="10.1038/436791a"),
 pm(3, "Takeda K et al. Components of protocyanin, a blue pigment from the blue flowers of Centaurea cyanus. Phytochemistry 2005;66(13):1607-13", "16005311", doi="10.1016/j.phytochem.2005.04.002"),
 pm(4, "Yoshida K, Negishi T. The identification of a vacuolar iron transporter involved in the blue coloration of cornflower petals. Phytochemistry 2013;94:60-7", "23838627", doi="10.1016/j.phytochem.2013.04.017"),
 pm(5, "Fe-Mediated Blue Pigment Formation via Collaborative Regulation of Iron Homeostasis by VIT1 and Ferritin: Insights for Blue Flower Breeding. Plant Cell Environ 2026;49(8):4669-4687", "41803011", "PMC13353680", "10.1111/pce.70472"),
 pm(6, "Metabolite and gene expression analysis reveal the molecular mechanism for petal colour variation in six Centaurea cyanus cultivars. Plant Physiol Biochem 2019;142:22-33 (초록)", "31255906", doi="10.1016/j.plaphy.2019.06.018"),
 pm(7, "CcMYB6-1 and CcbHLH1, two novel transcription factors synergistically involved in regulating anthocyanin biosynthesis in cornflower. Plant Physiol Biochem 2020;151:271-283 (초록)", "32247249", doi="10.1016/j.plaphy.2020.03.024"),
 pm(8, "The Phenolic Composition of Centaurea cyanus L. Flower Extracts: Antioxidant, Antimicrobial, and Fibroblast Biocompatibility of a Phenolic-Rich Ethanolic Extract. Int J Mol Sci 2026;27(18):8101", "42794531", "PMC13607395", "10.3390/ijms27188101"),
 pm(9, "Herbicide resistance status impacts the profile of non-anthocyanin polyphenolics and some phytomedical properties of edible cornflower (Centaurea cyanus L.) flowers. Sci Rep 2023;13:11538", "37460793", "PMC10352273", "10.1038/s41598-023-38520-z"),
 pm(10, "Influence of Copigmentation and Encapsulation on Stability and Antioxidant Activity of Anthocyanins from Blue and Pink Cornflower (Centaurea cyanus L.) Flowers. Molecules 2025;30(7):1467", "40286073", "PMC11990276", "10.3390/molecules30071467"),
 pm(11, "First Insights on the Bioaccessibility and Absorption of Anthocyanins from Edible Flowers: Wild Pansy, Cosmos, and Cornflower. Pharmaceuticals 2024;17(2):191", "38399406", "PMC10892915", "10.3390/ph17020191"),
 pm(12, "Anthocyanin-rich edible flowers - Impact of food matrix on anthocyanin stability, digestion and absorption: the case of wild pansy, cosmos and cornflower. Food Chem 2026;508:148137 (초록)", "41713338", doi="10.1016/j.foodchem.2026.148137"),
 pm(13, "Edible Flower Species as a Promising Source of Specialized Metabolites. Plants 2022;11(19):2529 (초록)", "36235395", "PMC9570977", "10.3390/plants11192529"),
 pm(14, "Edible Flowers as a Source of Dietary Fibre (Total, Insoluble and Soluble) as a Potential Athlete's Dietary Supplement. Nutrients 2022;14(12):2470", "35745200", "PMC9231144", "10.3390/nu14122470"),
 pm(15, "Phytochemical characterization of Borago officinalis L. and Centaurea cyanus L. during flower development. Food Res Int 2019;123:771-778 (초록)", "31285027", doi="10.1016/j.foodres.2019.05.014"),
 pm(16, "Chemical study, antioxidant, anti-hypertensive, and cytotoxic/cytoprotective activities of Centaurea cyanus L. petals aqueous extract. Food Chem Toxicol 2018;118:439-453 (초록)", "29787846", doi="10.1016/j.fct.2018.05.046"),
 pm(17, "Yogurt with cornflower (Centaurea cyanus L.) petals as a source of antioxidant compounds and dietary fiber: Physicochemical and spectroscopic research during storage. J Dairy Sci 2025;108(3):2243-2263 (초록)", "39662809", doi="10.3168/jds.2024-25628"),
 pm(18, "Phytochemical composition, antioxidant activity, and sensory evaluation of edible flower-enriched vinegars. Food Chem 2025;496:146897 (초록)", "41223836", doi="10.1016/j.foodchem.2025.146897"),
 pm(19, "Iconic Arable Weeds: The Significance of Corn Poppy (Papaver rhoeas), Cornflower (Centaurea cyanus), and Field Larkspur (Delphinium consolida) in Hungarian Ethnobotanical and Cultural Heritage. Plants 2023;12(1):84", "36616213", "PMC9824376", "10.3390/plants12010084"),
 pm(20, "Microstructural and histochemical analysis of aboveground organs of Centaurea cyanus used in herbal medicine. Protoplasma 2020;257(1):285-298 (초록)", "31515607", "PMC6982636", "10.1007/s00709-019-01437-4"),
 pm(21, "Secretory Products in Petals of Centaurea cyanus L. Flowers: A Histochemistry, Ultrastructure, and Phytochemical Study of Volatile Compounds. Molecules 2022;27(4):1371 (초록)", "35209163", "PMC8877098", "10.3390/molecules27041371"),
 pm(22, "Garbacki N et al. Anti-inflammatory and immunological effects of Centaurea cyanus flower-heads. J Ethnopharmacol 1999;68(1-3):235-41 (초록)", "10624883", doi="10.1016/s0378-8741(99)00112-9"),
 pm(23, "The diuretic effect of cornflower water extract. Medicina (Kaunas) 2007;43(3):221-5 (리투아니아어, 영문 초록)", "17413251"),
 pm(24, "Synthesis, biological activities and bioavailability of moschamine, a safflomide-type phenylpropenoic acid amide found in Centaurea cyanus. Nat Prod Res 2012;26(16):1465-72 (초록)", "21978225", doi="10.1080/14786419.2011.562207"),
 pm(25, "Sarker SD et al. Indole alkaloids from the seeds of Centaurea cyanus (Asteraceae). Phytochemistry 2001;57(8):1273-6 (초록)", "11454358", doi="10.1016/s0031-9422(01)00084-x"),
 pm(26, "Centaurea cyanus extracted 13-O-acetylsolstitialin A decrease Bax/Bcl-2 ratio and expression of cyclin D1/Cdk-4 to induce apoptosis and cell cycle arrest in MCF-7 and MDA-MB-231 breast cancer cell lines. J Cell Biochem 2019;120(10):18309-18319 (초록)", "31161672", doi="10.1002/jcb.29141"),
 pm(27, "A Cornflower Extract Containing N-Feruloylserotonin Reduces Inflammation in Human Skin by Neutralizing CCL17 and CCL22 and Inhibiting COX-2 and 5-LOX. Mediators Inflamm 2021:6652791 (초록)", "34557056", "PMC8455218", "10.1155/2021/6652791"),
 pm(28, "Cornflower Extract and Its Active Components Alleviate Dexamethasone-Induced Muscle Wasting by Targeting Cannabinoid Receptors and Modulating Gut Microbiota. Nutrients 2024;16(8):1130 (초록)", "38674820", "PMC11054969", "10.3390/nu16081130"),
 pm(29, "The complete chloroplast genome sequence of Centaurea cyanus (Asteraceae). Mitochondrial DNA B Resour 2023;8(3):393-397", "36926644", "PMC10013558", "10.1080/23802359.2023.2185470"),
 pm(30, "Contemporary evolution of plant reproductive strategies under global change is revealed by stored seeds. J Evol Biol 2015;28(4):766-78 (초록)", "25682981", doi="10.1111/jeb.12603"),
 pm(31, "Pollinator functional group abundance and floral heterogeneity in an agroecological context affect mating patterns in a self-incompatible wild plant. Am J Bot 2024;111(12):e16440 (초록)", "39592516", "PMC11659934", "10.1002/ajb2.16440"),
 pm(32, "Enhanced detoxification via Cyt-P450 governs cross-tolerance to ALS-inhibiting herbicides in weed species of Centaurea. Environ Pollut 2023;322:121140 (초록)", "36706859", doi="10.1016/j.envpol.2023.121140"),
 pm(33, "Cornflower (Centaurea cyanus L.) honey quality parameters: chromatographic fingerprints, chemical biomarkers, antioxidant capacity and others. Food Chem 2013;142:12-8 (초록)", "24001807", doi="10.1016/j.foodchem.2013.07.050"),
 pm(34, "Microbiological and toxicological quality of dried herbs. Lett Appl Microbiol 2011;52(6):573-80 (초록)", "21375549", doi="10.1111/j.1472-765X.2011.03040.x"),
 pm(35, "Mercury accumulation in plants from contaminated arable lands in Eastern Slovakia. Ann Agric Environ Med 2020;27(1):29-35 (초록)", "32208576", doi="10.26444/aaem/115282"),
]

S = {}
S["overview"] = ("한눈에 보기",
"수레국화(Centaurea cyanus L.)는 국화과(Asteraceae)의 한해살이풀로, 꽃송이 가장자리의 짙은 파란 혀꽃이 특징이며 유럽과 서아시아에 자생하고 호밀·밀·보리 밭의 잡초로 오래 자라 왔다[8]. 영어로는 cornflower 또는 bachelor's button이라 부른다[29]. "
"식품의약품안전처 「식품원료 목록」에는 '수레국화꽃잎'과 '수레국화추출물' 두 원료명이 올라 있고, 둘 다 상태는 '사용가능', 사용 조건은 '사용가능부위 : 꽃잎'이다[1]. 같은 목록의 이명은 '팔랑개비국화, 콘플라워', 영명은 'Cornflower'이다[1]. "
"이 자료 묶음의 원자료에는 EU 신규식품(Novel Food) 목록 표시가 있으나, EU 원문에서 그 지위와 조건은 확인하지 못함. 이 종을 원재료로 하는 건강기능식품 고시형 원료는 확인하지 못함.\n\n"
"꽃잎의 파란색은 안토시아닌 6분자와 플라본 6분자가 철 1개, 마그네슘 1개, 칼슘 2개와 모인 금속 착물 색소 프로토시아닌에서 나온다[2][3]. 유럽에서는 꽃을 음식 장식과 양념으로 흔히 쓰고, 말린 꽃잎은 우려 마시거나 디저트를 꾸미는 데 쓴다[9][14]. "
"안토시아닌이 많은 식용꽃 가운데 팬지·코스모스와 함께 세계에서 많이 먹는 종으로 꼽힌다[11]. 효능 연구는 대부분 세포·동물 실험이며, 사람을 대상으로 한 임상 근거는 확인하지 못함.")

S["history"] = ("역사",
"수레국화 꽃은 르네상스 시대 서유럽 약초서에서 눈과 상처를 소독하는 약으로 다뤄졌고, 벨라루스·코소보·이탈리아·스페인·아르메니아 등에서 눈병 민간약으로 쓰였다[19]. 벨라루스·우크라이나·불가리아에서는 이뇨 목적으로도 썼다[19]. "
"헝가리 문헌(1578–2021년)을 모은 연구에 따르면 헝가리 민간의학은 18세기부터 꽃을 눈 염증 찜질약으로 썼고, 이 쓰임이 20세기 중반까지 가장 흔했다[19]. 제1차 세계대전 때 헝가리에서는 의약품 부족을 덜려고 학생들에게 여름방학 동안 양귀비·수레국화 같은 약초를 모으게 한 장관령이 있었고, 수레국화는 1960년대까지 야생에서 채집해 팔던 인기 약초였다[19]. "
"지금도 일부 유럽 나라에서는 허브차 혼합물에 조금 넣어 우린 물의 색을 돋우는 데 쓴다[19]. 유럽 식물요법에서는 꽃송이를 가벼운 눈 염증에 써 왔다고 정리되어 있다[22]. 러시아 연방 약전에는 꽃이 이뇨제로 올라 있다고 한 논문은 적었다[29].\n\n"
"같은 안토시아닌을 가진 장미는 빨갛고 수레국화는 파란 이유는 오래 풀리지 않았는데, 2005년 색소의 X선 결정 구조가 밝혀지며 금속 4개가 든 초분자 색소임이 드러났다[2]. 한국에 들어온 시기와 경로는 확인하지 못함.")

S["biology"] = ("식물학적 특징",
"한해살이 또는 두해살이풀로 키는 30–70 cm 이상이며, 회녹색의 가지 친 줄기와 곧은뿌리, 길이 1–4 cm의 피침형 잎이 어긋나게 달린다[29]. 다른 연구는 줄기 높이를 20–90 cm로 적었다[8]. "
"머리모양꽃차례는 지름 1.5–3 cm이고, 가장자리의 짙은 파란 혀꽃은 씨를 맺지 않으며 가운데의 덜 눈에 띄는 대롱꽃이 씨방마다 밑씨 하나를 가진다[29]. 자가불화합성 식물이라 곤충이 꽃가루를 옮겨야 하며, 호박벌·꽃등에·야생벌의 수에 따라 한 포기의 씨앗 아비 수가 달라졌다[31]. "
"꽃잎에는 유두 모양 돌기와 특징적인 큐티클 무늬가 있고, 포엽 표피에는 각기둥 모양의 옥살산칼슘 결정이 있으며, 포엽·줄기의 샘털과 잎·줄기의 분비관에서 정유·지질·플라보노이드·탄닌이 나온다[20]. "
"꽃잎 유조직은 수지 같은 친유성 분비물을 만들고, 꽃의 휘발 성분은 세스퀴테르펜이 주를 이루며 β-카리오필렌(26.17%)과 α-휴물렌(9.77%)이 많았다[21]. "
"파란색이 나려면 액포로 철을 옮기는 수송체(CcVIT)가 필요하며, 이 단백질에 아미노산 치환(A236E)이 생긴 보라색 돌연변이 꽃잎은 철이 적어 프로토시아닌도 적었다[4].")

S["related_species"] = ("가까운 종",
"수레국화는 수레국화속(Centaurea)에 넣지만 이 속의 범위는 아직 분명하지 않아, 엽록체 유전체 계통수에서 일부 종이 다른 속의 가지에 섞여 나왔다[29]. 일부 생태 연구는 이 종을 Cyanus segetum Hill이라는 학명으로 부른다[31]. "
"식약처 「식품원료 목록」에는 같은 속의 다른 종(Centaurea calcitrapa, C. nigra, C. iberica, C. depressa, C. raphanina, C. chamaerhaponticum 등)이 따로 올라 있으며, 쓸 수 있는 부위도 잎·줄기·뿌리 등으로 서로 다르다[1]. 이 문서의 성분·효능 자료는 모두 C. cyanus 자료만 쓰고 이들 종의 자료는 섞지 않았다[1]. "
"이베리아반도 밀밭에서는 C. cyanus, C. diluta, C. melitensis, C. pullata가 주요 광엽 잡초로 함께 자라고, 네 종 모두 ALS 저해 제초제 트리베누론메틸에 타고난 내성을 보였으며 C. cyanus의 반수 치사 용량은 65 g/ha였다[32].\n\n"
"원예 품종은 흰색·분홍·빨강·파랑·연보라·검정 꽃잎으로 다양하다[6]. 분홍·빨강 품종은 펠라르고니딘 계열, 파랑·연보라·검정 품종은 시아니딘 계열 안토시아닌을 쌓으며, 파랑과 연보라 꽃은 같은 시아니딘 유도체를 갖되 아피제닌 4' 위치의 수식이 달라 색이 갈렸다[6]. "
"분홍 품종 꽃 추출물은 파란 품종보다 안토시아닌과 총페놀이 거의 4배 많았다[10]. 파란 꽃의 철 조절 유전자를 국화에 넣어 파란 꽃 국화를 만드는 육종 연구도 있다[5].")

S["cultivation"] = ("재배와 생산",
"수레국화는 유럽 곡물밭의 대표적인 잡초였으나, 농업 집약화와 제초제 사용으로 서유럽에서는 크게 줄었고 중·동부 유럽의 가볍고 모래 많은 땅에서는 아직 비교적 흔하다[8]. 지금은 저투입 곡물밭을 가리키는 지표종으로 여겨지고, 보전 사업의 상징종(flagship species)으로 자주 다뤄진다[19]. "
"폴란드에서는 꿀벌 먹이로 재배하기도 하지만, 씨앗 값이 비싸 약용 꽃은 자생지에서 채집하는 경우가 많다[9]. 폴란드에서는 ALS 저해 제초제(트리베누론메틸) 저항성 개체군이 보고되었으며, 저항성 계통은 감수성 계통보다 꽃이 늦게 피었다[9]. "
"프랑스의 한 장소에서 1992년과 2010년에 모아 보관한 씨앗을 같은 밭에서 기른 결과, 2010년 계통이 더 일찍 꽃 피고 더 큰 꽃송이를 맺어 기후 변화와 수분 곤충 감소에 대한 적응으로 해석되었다[30]. "
"상업용 말린 꽃은 폴란드 업체 등에서 공급되어 연구에 쓰였다[8][10]. 화훼 원예 품종은 꽃잎 색에 따라 여러 계통이 있다[6].\n\n"
"국내 재배 면적과 생산량은 통계청 농작물생산조사·농림축산식품부 특용작물 생산실적에서 확인하지 못함. 국내 지리적 표시 등록과 생산자 단체도 확인하지 못함.")

S["processing"] = ("가공과 이용",
"식약처 목록에는 꽃잎 자체('수레국화꽃잎')와 '수레국화추출물'이 원료로 올라 있다[1]. 식용꽃으로는 말린 꽃잎을 우려 마시거나 디저트 장식에 쓴다[14]. "
"동결건조 꽃잎을 넣은 요구르트는 식이섬유가 0에서 0.56 g/100 g으로, 비타민 C가 3배 넘게 늘었고 21일 냉장 보관 동안 안정했으며, 생·건조·냉동·동결건조 네 형태 가운데 동결건조 꽃잎이 가장 유리했다[17]. 백포도주 식초에 30일 우리면 안토시아닌과 색이 짙어졌지만 떫은맛이 두드러졌다[18]. "
"파란·분홍 품종의 안토시아닌을 바이칼린이나 클로로젠산과 보조색소화한 뒤 분무건조로 캡슐화하면, 60 °C 72시간 가열과 자외선 노출 뒤 색 안정성 지수가 추출물의 0.61–0.70에서 0.82–0.94로 높아졌다[10]. "
"수레국화 안토시아닌은 pH와 온도 변화에 팬지·코스모스 안토시아닌보다 안정했다[11]. 모의 소화에서는 장 단계 뒤 안토시아닌이 크게 줄었고, 함께 먹는 식품 기질에 따라 흡수가 달라졌다[12]. "
"추출 용매를 비교한 연구에서는 클로로포름으로 기름을 뺀 뒤 70% 에탄올로 추출할 때 총페놀이 42.18 mg/g DW로 가장 높았다[8]. 폴란드산 수레국화 단일꽃꿀에서는 루미크롬(4.7–10.0 mg/kg)·리보플라빈·페닐젖산이 특징 성분으로 쓰였다[33]. 국내 건강기능식품 원료 생산실적은 확인하지 못함.")

S["genetics"] = ("유전체와 육종",
"중국 후난성에서 기른 개체의 잎으로 해독한 엽록체 유전체는 152,433 bp 원형으로, 큰 단일복사 부위 83,464 bp, 작은 단일복사 부위 18,545 bp, 역반복 부위 2개(각 25,212 bp)로 이뤄진다[29]. 유전자는 130개(단백질 암호 86, tRNA 36, rRNA 8)이고 전체 GC 함량은 37.76%였다[29]. "
"한 꽃잎 안에서 흰색→보라→파랑으로 바뀌는 부위를 RNA-seq으로 비교한 연구는 105,506개 유전자 단위를 조립했고, 전사인자 CcMYB6-1과 CcbHLH1이 함께 F3H·DFR 프로모터를 켜 안토시아닌 합성을 조절함을 보였다[7]. "
"품종 6개를 비교한 연구에서 흰 꽃은 F3H 단계부터 경로가 막혔고, 분홍·빨강 꽃은 F3'H 유전자가 잘려 헴 결합 부위를 잃었다[6]. "
"철 수송 유전자 VIT/VTL 11개와 페리틴 유전자 4개가 확인되었고, CcVIT1a는 파란 혀꽃에서 특히 많이 발현되며 이 유전자를 침묵시키면 꽃이 파랑에서 보라로 바뀌었다[5]. "
"폴란드 제초제 저항성 계통의 ALS 유전자에서는 알려진 저항성 돌연변이 없이 N404·V525 위치의 변이만 나왔다[9]. 핵 유전체 전체 서열과 염색체 수는 이번 조사에서 확인하지 못함.")

S["safety"] = ("안전성",
"식약처 「식품원료 목록」에서 수레국화는 꽃잎만 쓸 수 있는 사용가능 원료이며, 그 밖의 섭취량 제한이나 주의사항은 목록에서 확인하지 못함[1]. 이 종을 원재료로 하는 건강기능식품 고시형 원료는 확인하지 못해, 고시된 섭취 시 주의사항도 없다. "
"꽃잎 물 추출물은 여러 세포주에서 IC50·GI50이 900 µg/mL를 넘어 세포독성이 낮았다[16]. 에탄올 추출물은 생쥐·사람 섬유아세포에 5 mg/mL까지 세포독성이 없었고 10 mg/mL에서는 생존율이 70% 아래로 떨어졌다[8]. 정제한 안토시아닌 추출물도 시험 농도 범위에서 장 세포(Caco-2)에 뚜렷한 독성을 보이지 않았다[11]. "
"씨앗에서는 모스카민 등 인돌 알칼로이드 4종이 분리되어 브라인 쉬림프 치사 시험으로 일반 독성을 평가받았고[25], 이 종에서 분리한 세스퀴테르펜 락톤(13-O-아세틸솔스티티알린 A)은 유방암 세포에 강한 세포독성을 보였다[26]. 이 성분들이 먹는 꽃잎에 얼마나 들어 있는지는 확인하지 못함.\n\n"
"이탈리아 소규모 농가의 건조 허브 51점(수레국화 포함)에서는 아플라톡신 B1 부적합이 없었으나, 전체 시료의 29.4%가 중온성 세균 기준을 넘었다(종별 값은 초록에서 확인하지 못함)[34]. "
"슬로바키아 옛 광석 처리장 주변 수은 오염 밭의 수레국화 꽃에서 수은 18.20 mg/kg이 나와, 오염 지역에서 채집한 꽃은 피하는 것이 좋다[35]. 쥐 실험에서 물 추출물은 이뇨 작용을 보였다[23]. 사람이 먹었을 때의 알레르기·독성에 관한 국내외 공공기관 정보는 확인하지 못함.")

sections = [{"key": k, "title": v[0], "body": v[1]} for k, v in S.items()]

compounds = [
 {"name": "Protocyanin", "name_ko": "프로토시아닌", "class": "금속 착물 안토시아닌(초분자 색소)", "role": "marker", "part": "꽃(파란 혀꽃)",
  "content_text": "안토시아닌 6분자 + 플라본 6분자 + Fe³⁺ 1, Mg²⁺ 1, Ca²⁺ 2의 착물(함량 수치는 확인하지 못함)[2][3]",
  "activity_ko": "수레국화 꽃잎의 파란색을 내는 색소[2]; 철이 부족한 돌연변이에서는 양이 줄어 꽃이 보라색이 됨[4]", "source": [2, 3, 4]},
 {"name": "Cyanidin 3-O-(6''-succinylglucoside)-5-O-glucoside", "name_ko": "시아니딘 3-O-(6″-석시닐글루코사이드)-5-O-글루코사이드(센타우로시아닌)", "class": "안토시아닌", "role": "marker", "part": "꽃(파란 품종)",
  "content_text": "파란 품종 꽃 추출물 6.79 mg/g dw(추출물 기준, 가장 많은 안토시아닌)[10]",
  "activity_ko": "프로토시아닌을 이루는 안토시아닌 성분[3]", "source": [10, 3]},
 {"name": "Cyanidin 3,5-diglucoside", "name_ko": "시아니딘 3,5-다이글루코사이드", "class": "안토시아닌", "role": "bioactive", "part": "꽃",
  "content_text": "파란 품종 꽃 추출물 3.72 mg/g dw(추출물 기준)[10]",
  "activity_ko": "장 세포(Caco-2) 모델에서 4시간 투과 효율 약 5%로 흡수가 비교적 높음(시험관)[11]", "source": [10, 11]},
 {"name": "Cyanidin 3-O-(6''-malonylglucoside)-5-O-glucoside", "name_ko": "시아니딘 3-O-(6″-말로닐글루코사이드)-5-O-글루코사이드", "class": "안토시아닌", "role": "bioactive", "part": "꽃",
  "content_text": "파란 품종 꽃 추출물 3.28 mg/g dw(추출물 기준)[10]", "activity_ko": "꽃잎의 주요 안토시아닌 가운데 하나[11]", "source": [10, 11]},
 {"name": "Pelargonidin 3-O-(6''-malonylglucoside)-5-O-glucoside", "name_ko": "펠라르고니딘 3-O-(6″-말로닐글루코사이드)-5-O-글루코사이드", "class": "안토시아닌", "role": "bioactive", "part": "꽃(분홍 품종)",
  "content_text": "분홍 품종 꽃 추출물 20.87 mg/g dw(추출물 기준)[10]", "activity_ko": "분홍·빨강 품종의 색을 내는 펠라르고니딘 계열 색소[6][10]", "source": [10, 6]},
 {"name": "Apigenin 7-O-glucuronide", "name_ko": "아피제닌 7-O-글루쿠로나이드", "class": "플라본 배당체", "role": "marker", "part": "꽃",
  "content_text": "분홍 품종 꽃 추출물 14.09 mg/g dw(추출물 기준), 파란 품종은 그보다 훨씬 적음[10]; 에탄올 추출물의 아피제닌 O-헥소사이드-O-글루쿠로나이드 13.63 mg/g DW(총페놀의 32.3%)[8]",
  "activity_ko": "프로토시아닌의 플라본 성분은 아피제닌 7-O-글루쿠로나이드-4′-O-(6-O-말로닐글루코사이드)[3]; 아피제닌 배당체는 이 종 꽃의 화학분류학적 특징으로 정리됨[8]", "source": [10, 8, 3]},
 {"name": "Apigenin", "name_ko": "아피제닌", "class": "플라본", "role": "bioactive", "part": "꽃(꽃잎)",
  "content_text": "생꽃잎 133.60 µg/g FM(감수성 계통), 123.59 µg/g FM(저항성 계통)[9]; 에탄올 추출물 2.11 mg/g DW[8]",
  "activity_ko": "꽃잎에서 가장 많은 플라보노이드 비배당체[9]", "source": [9, 8]},
 {"name": "Luteolin 3',7-diglucoside", "name_ko": "루테올린 3′,7-다이글루코사이드", "class": "플라본 배당체", "role": "bioactive", "part": "꽃(꽃잎)",
  "content_text": "생꽃잎 507.87 µg/g FM(감수성 계통), 446.45 µg/g FM(저항성 계통)(원문 표기 luteolin 3′,7′-diglucoside)[9]",
  "activity_ko": "비안토시아닌 플라보노이드 배당체 가운데 가장 많음[9]", "source": [9]},
 {"name": "Chlorogenic acid", "name_ko": "클로로젠산(3-카페오일퀸산)", "class": "페놀산", "role": "bioactive", "part": "꽃",
  "content_text": "에탄올 추출물 3-카페오일퀸산 4.34 mg/g DW[8]; 파란 품종 꽃 추출물 4.09 mg/g dw[10]",
  "activity_ko": "꽃잎 물 추출물의 주요 성분 가운데 하나[16]", "source": [8, 10, 16]},
 {"name": "Ascorbic acid", "name_ko": "아스코르브산(비타민 C)", "class": "비타민", "role": "nutrient", "part": "꽃",
  "content_text": "129.70 mg/100 g fw(비교한 식용꽃 5종 가운데 가장 높음)[13]", "activity_ko": "꽃잎을 넣은 요구르트의 비타민 C를 3배 넘게 높임[17]", "source": [13, 17]},
 {"name": "Lutein", "name_ko": "루테인", "class": "카로티노이드", "role": "nutrient", "part": "꽃",
  "content_text": "보리지·수레국화 꽃의 카로티노이드 0.2–181.4 mg/100 g dw(주로 루테인, 두 꽃·세 개화 단계를 합친 범위; 수레국화만의 값은 초록에서 확인하지 못함)[15]",
  "activity_ko": "꽃의 주요 카로티노이드[15]", "source": [15]},
 {"name": "N-Feruloylserotonin", "name_ko": "N-페룰로일세로토닌(모스카민)", "class": "페닐프로페노산 아마이드(인돌 알칼로이드)", "role": "bioactive", "part": "꽃 추출물·씨앗",
  "content_text": "함량 수치는 확인하지 못함; 씨앗에서 모스카민·시스-모스카민 등 분리[25]",
  "activity_ko": "수레국화 추출물의 CCL17·CCL22 중화, COX-2·5-LOX 억제 작용의 주성분(시험관)[27]; 0.1 µmol/L에서 COX-I 58%, COX-II 54% 억제(시험관)[24]", "source": [27, 25, 24]},
 {"name": "Graveobioside A", "name_ko": "그라베오바이오사이드 A", "class": "플라본 배당체", "role": "bioactive", "part": "꽃(물 추출물)",
  "content_text": "함량 수치는 초록에서 확인하지 못함[28]",
  "activity_ko": "근육 세포에서 CB1 억제·CB2 증가로 단백질 합성 촉진; 물 추출물은 덱사메타손 유발 근위축 생쥐의 악력·운동 능력 개선(동물)[28]", "source": [28]},
 {"name": "beta-Caryophyllene", "name_ko": "β-카리오필렌", "class": "세스퀴테르펜(휘발 성분)", "role": "bioactive", "part": "꽃",
  "content_text": "꽃 휘발 성분의 26.17%(SPME GC-MS 상대 비율)[21]", "activity_ko": "꽃잎 분비물(올레오레진)의 주된 휘발 성분[21]", "source": [21]},
 {"name": "13-O-Acetylsolstitialin A", "name_ko": "13-O-아세틸솔스티티알린 A", "class": "세스퀴테르펜 락톤", "role": "bioactive", "part": "확인하지 못함(초록에 부위 기재 없음)",
  "content_text": "함량 수치는 확인하지 못함[26]", "activity_ko": "MCF-7·MDA-MB-231 유방암 세포에서 세포자멸·세포주기 정지 유도(시험관)[26]", "source": [26]},
]

assays = [
 {"role": "literature", "compound": "Apigenin O-hexoside-O-glucuronide", "compound_ko": "아피제닌 O-헥소사이드-O-글루쿠로나이드(아피제닌·퀘르세틴·카페오일퀸산 등 35종 동시)",
  "part": "꽃(시판 건조 꽃)",
  "content": "탈지 후 70% 에탄올 추출물 13.63 mg/g DW(총페놀 42.18 mg/g DW의 32.3%); 3-카페오일퀸산 4.34 mg/g DW, 안토시아닌 합계 1.41 mg/g DW[8]",
  "method": "UPLC-PDA-Q/TOF-MS(ESI 음이온)",
  "conditions": {
   "instrument": "Waters ACQUITY UPLC + 광다이오드 배열 검출기 + Waters G2 Q-Tof 질량분석기(ESI)",
   "column": "Waters BEH C18, 2.1 × 100 mm, 1.7 µm",
   "mobile_phase": "A: 0.1% 포름산 물, B: 0.1% 포름산 아세토니트릴(방법 절의 다른 문장은 B를 아세토니트릴로만 적음)",
   "gradient": "15분 선형 기울기(구체 비율은 인용 문헌 방법에 따른다고만 적혀 있어 확인하지 못함)",
   "flow": "0.42 mL/min",
   "temp": "30 °C",
   "detection": "PDA 200–600 nm(2 nm 간격); ESI 음이온 풀스캔 m/z 100–1500, 모세관 2.5 kV, 콘 30 V, 이온원 100 °C, 탈용매 300 °C, 질소 300 L/h, 아르곤 충돌 0.3–2 V, 류신 엔케팔린 LockSpray",
   "injection": "10 µL",
   "sample_prep": "건조 꽃 10.5 g 클로로포름 24시간 침지·탈지 → 분쇄 후 70% 에탄올 약 300 mL 1시간 환류 → 감압 농축·동결건조(수율 13.7%) → 추출물 약 200 mg을 1% HCl 함유 80% 메탄올 1.5 mL에 녹임",
   "standard": "아피제닌, 액실라린, 3-카페오일퀸산, 시아니딘 배당체, 캠페롤 3-O-글루코사이드·갈락토사이드, 퀘르세틴 3-O-글루코사이드·갈락토사이드(시판 표준품); 표준품 없는 성분은 정확 질량·MS/MS로 잠정 동정",
   "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "아피제닌 배당체가 총페놀의 절반 이상(22.37 mg/g DW)을 차지해 이 종 꽃의 특징 성분으로 정리되었다[8]. 결과는 mg/g DW로 보고되었으나 방법 절에는 mg/kg 건물 기준이라는 문장도 있어 단위 표기가 엇갈린다. 직선성·검출한계·정량한계·회수율은 원문에서 확인하지 못함.",
  "source": [8], "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC13607395/", "source_kind": "paper"},
 {"role": "literature", "compound": "Cyanidin 3-O-(6''-succinylglucoside)-5-O-glucoside", "compound_ko": "시아니딘 3-O-(6″-석시닐글루코사이드)-5-O-글루코사이드(안토시아닌 8종·클로로젠산·아피제닌 7-O-글루쿠로나이드 동시)",
  "part": "꽃(파란·분홍 품종 시판 건조 꽃)",
  "content": "파란 품종 추출물 6.79 mg/g dw; 분홍 품종은 펠라르고니딘 3-O-(6″-말로닐글루코사이드)-5-O-글루코사이드 20.87 mg/g dw(모두 동결건조 추출물 기준)[10]",
  "method": "UHPLC-DAD-ESI-MS/MS(외부 검량)",
  "conditions": {
   "instrument": "", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "",
   "detection": "DAD 270·320·365·520 nm; ESI-MS 전체 질량 및 MS/MS 단편으로 동정",
   "injection": "",
   "sample_prep": "분쇄 꽃 약 30 g + 20% 산성 메탄올(pH 2) 450 mL, 40 °C 이하 초음파 30분 → 여과·질소로 메탄올 제거 → 동결건조(−50 °C, 0.7 mbar, 48–72시간); 분석용: 추출물 0.0200 g + 산성 메탄올(80:20, pH 2) 10 mL, 80 rpm 30분 진탕 → 0.2 µm 여과",
   "standard": "시아니딘 3-O-글루코사이드 클로라이드·클로로젠산(시판 표준품) 외부 검량",
   "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "파란 꽃의 프로토시아닌을 이루는 주된 안토시아닌이고[3], 파란 품종 추출물에서 가장 많았다[10]. 칼럼·이동상·유속 등은 '선행 문헌(2022)의 방법'으로만 적혀 있어 원문에서 확인하지 못함.",
  "source": [10, 3], "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11990276/", "source_kind": "paper"},
 {"role": "literature", "compound": "Apigenin", "compound_ko": "아피제닌(루테올린 3′,7′-다이글루코사이드·페놀산 등 비안토시아닌 페놀 동시)",
  "part": "꽃잎(Flos Cyani, 온실 재배 감수성·저항성 계통)",
  "content": "생꽃잎 133.60 µg/g FM(감수성), 123.59 µg/g FM(저항성); 루테올린 3′,7′-다이글루코사이드 507.87·446.45 µg/g FM[9]",
  "method": "LC-ESI-MS/MS(MRM, ESI 음이온)",
  "conditions": {
   "instrument": "Agilent 1200 Series HPLC + AB Sciex 3200 QTRAP(ESI)",
   "column": "Agilent Zorbax SB-C18, 2.1 × 100 mm, 1.8 µm(원문 표기 '1.8 mm')",
   "mobile_phase": "A: 0.1% 포름산 수용액, B: 0.1% 포름산 아세토니트릴",
   "gradient": "0–2분 20% B; 3–4.5분 25% B; 5.5–7분 35% B; 8–12분 65% B; 14–16분 80% B; 총 28분",
   "flow": "300 µL/min",
   "temp": "25 °C",
   "detection": "ESI 음이온 MRM; 모세관 온도 550 °C, 커튼 가스 30 psi, 분무 가스 50 psi, 이온원 전압 −4500 V",
   "injection": "3 µL",
   "sample_prep": "폴란드 약전 IX에 따른 팅크: 꽃잎 2 g + 70% 에탄올 50 mL, 어두운 곳 2주 침출",
   "standard": "성분별 표준품의 MS/MS 스펙트럼·머무름 시간 비교, MRM 검량선으로 정량(표준품 3회 주입)",
   "linearity": "",
   "lod": "신호 대 잡음비 3:1(성분별 값은 원문 표에 있으며 본문에서 확인하지 못함)",
   "loq": "신호 대 잡음비 10:1(성분별 값은 확인하지 못함)",
   "recovery": ""},
  "rationale": "꽃잎에서 가장 많은 플라보노이드 비배당체로, 제초제 저항성 여부와 처리에 따라 함량이 달라졌다[9]. 회수율과 성분별 직선 범위는 원문 본문에서 확인하지 못함.",
  "source": [9], "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10352273/", "source_kind": "paper"},
 {"role": "literature", "compound": "Cyanidin 3,5-diglucoside", "compound_ko": "시아니딘 3,5-다이글루코사이드(꽃잎 안토시아닌 8종 동정)",
  "part": "꽃잎(포르투갈 생산 생꽃)",
  "content": "절대 함량 없음 — 정제 안토시아닌 추출물의 피크 합으로 안정성·흡수율을 상대 비교[11]",
  "method": "UHPLC-DAD 및 LC-DAD/ESI-MS(이온트랩)",
  "conditions": {
   "instrument": "Thermo Finnigan Surveyor Plus HPLC + Thermo LTQ XL 이온트랩(ESI); 안정성·소화·흡수 시료는 Thermo Dionex UltiMate 3000 UHPLC",
   "column": "Thermo Hypersil GOLD C18, 150 × 2.1 mm, 1.9 µm(동정용); 50 × 2.1 mm, 1.9 µm(안정성·흡수 분석용)",
   "mobile_phase": "A: 1% 포름산, B: 1% 포름산/30% 아세토니트릴(동정용); A: 5% 포름산, B: 5% 포름산/30% 아세토니트릴(안정성·흡수용)",
   "gradient": "0–7분 5.5→64% B, 7–10분 →80% B, 10–20분 100% B, 20–25분 초기 조건 재평형",
   "flow": "0.3 mL/min(동정용); 0.5 mL/min(안정성·흡수용)",
   "temp": "",
   "detection": "DAD 280 nm(안토시아닌은 520 nm 함께 확인); ESI 양이온 m/z 250–1500, 모세관 온도 300 °C, 시스·보조 가스 40·15(임의 단위)",
   "injection": "20 µL",
   "sample_prep": "꽃잎 약 100 g을 산성 탈이온수로 초음파 추출 → 13,400×g 10분 원심·0.22 µm 여과 → 액-액 추출(에틸아세테이트/다이에틸에테르/물 1:1:1) → C18 고상추출 → 혼합형 양이온교환(DSC-MCAX) 정제 → 3.5 kDa 투석 → 동결건조",
   "standard": "MS/MS 단편과 문헌 비교로 잠정 동정(표준품 검량 없음)",
   "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "수레국화 안토시아닌은 다이글루코사이드 구조여서 팬지·코스모스보다 pH·온도에 안정하고 장 세포 흡수율이 높았다[11]. 정량 검량을 하지 않은 상대 비교라 직선성·검출한계·회수율은 없다.",
  "source": [11], "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10892915/", "source_kind": "paper"},
]

d = {
 "slug": "centaurea-cyanus", "name_ko": "수레국화", "name_en": "Cornflower",
 "scientific_name": "Centaurea cyanus L.",
 "aliases": ["수레국화꽃잎", "수레국화추출물", "팔랑개비국화", "콘플라워", "bachelor's button", "Cyanus segetum Hill"],
 "sections": sections, "compounds": compounds, "markers": [], "assays": assays,
 "nutrients": [], "production": [], "world": [], "gi": [], "orgs": [], "sources": sources,
}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in sections:
    print(s["key"], len(s["body"]))
