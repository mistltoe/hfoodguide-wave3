import json
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "dossier.json"
ACC = "2026-11-02"
MFDS_URL = "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020"


def pm(n, title, pmid, publisher, pmc=None, note="초록 확인"):
    url = f"https://pmc.ncbi.nlm.nih.gov/articles/{pmc}/" if pmc else f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
    ids = f"PMID {pmid}" + (f", {pmc}" if pmc else "")
    return {"n": n, "title": f"{title} ({ids}; {note})", "url": url, "publisher": publisher, "accessed": ACC}


sources = [
    {"n": 1, "title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 황연목잎 행: 학명 Pistacia chinensis Bunge, 부위 잎, 사용 조건 '사용가능부위 : 잎', 상태 '사용가능', 다른 이름·영문명 칸 비어 있음. 로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json", "url": MFDS_URL, "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
    {"n": 2, "title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 같은 속·같은 과 원료 행: 피스타치오견과(Pistacia vera L., '사용가능부위 : 견과', 사용가능), 옻나무(Rhus verniciflua Stokes, '제한적사용가능부위 : 줄기, 가지', 제한적사용), 붉나무(Rhus chinensis Mill., 사용불가), 오배자(붉나무 잎의 벌레집, 사용불가). 로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json", "url": MFDS_URL, "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
    pm(3, "Xanthine Oxidase Inhibitory Activity and Chemical Composition of Pistacia chinensis Leaf Essential Oil. Pharmaceutics 2022;14(10):1982 (doi:10.3390/pharmaceutics14101982)", "36297418", "MDPI / PubMed Central", "PMC9609098", "전문 확인"),
    pm(4, "Seasonal variation and gender pattern of phenolic and flavonoid contents in Pistacia chinensis Bunge inflorescences and leaves. J Plant Physiol 2016;191:36-44 (doi:10.1016/j.jplph.2015.11.014)", "26717010", "Elsevier / PubMed"),
    pm(5, "[Chemical components of the leaves of Pistacia chinensis Bge]. Zhongguo Zhong Yao Za Zhi 1992;17(7):422-423, 446 (중국어 논문, 영문 초록)", "1445648", "China Journal of Chinese Materia Medica / PubMed"),
    pm(6, "LC-ESI-MS/MS and cytotoxic activity of three Pistacia species. Nat Prod Res 2019;33(12):1747-1750 (doi:10.1080/14786419.2018.1428601)", "29376415", "Taylor & Francis / PubMed"),
    pm(7, "[SPME-GC-MS combined with Kovat's retention index analysis for volatile components in Pistacia chinensis]. Zhong Yao Cai 2014;37(11):2022-2025 (중국어 논문, 영문 초록)", "26027126", "Journal of Chinese Medicinal Materials / PubMed"),
    pm(8, "Investigation of free amino acid, total phenolics, antioxidant activity and purine alkaloids to assess the health properties of non-Camellia tea. Acta Pharm Sin B 2016;6(2):170-181 (doi:10.1016/j.apsb.2015.11.003; 본문 전문에서 종명이 빠져 있어 종별 수치는 초록 범위만 사용)", "27006902", "Elsevier / PubMed Central", "PMC4788713", "전문 확인"),
    pm(9, "Oxidant-induced damage to equine erythrocytes from exposure to Pistacia atlantica, Pistacia terebinthus, and Pistacia chinensis. J Vet Diagn Invest 2014;26(6):821-826 (doi:10.1177/1040638714550183)", "25227420", "SAGE / PubMed Central", "PMC5390776", "전문 확인"),
    pm(10, "Variations in genetic diversity in cultivated Pistacia chinensis. Front Plant Sci 2022;13:1030647 (doi:10.3389/fpls.2022.1030647)", "36438104", "Frontiers / PubMed Central", "PMC9691265", "전문 확인"),
    pm(11, "Genome-wide identification of Pistacia R2R3-MYB gene family and function characterization of PcMYB113 during autumn leaf coloration in Pistacia chinensis. Int J Biol Macromol 2021;192:16-27 (doi:10.1016/j.ijbiomac.2021.09.092)", "34555399", "Elsevier / PubMed"),
    pm(12, "Determination of superior Pistacia chinensis accession with high-quality seed oil and biodiesel production and revelation of LEC1/WRI1-mediated high oil accumulative mechanism. BMC Plant Biol 2023;23(1):268 (doi:10.1186/s12870-023-04267-y)", "37208597", "BioMed Central / PubMed"),
    pm(13, "The impact of global warming on the potential suitable planting area of Pistacia chinensis is limited. Sci Total Environ 2023;864:161007 (doi:10.1016/j.scitotenv.2022.161007)", "36549530", "Elsevier / PubMed"),
    pm(14, "Prediction of global marginal land resources for Pistacia chinensis Bunge by a machine learning method. Sci Rep 2022;12(1):5843 (doi:10.1038/s41598-022-09830-5)", "35393461", "Springer Nature / PubMed"),
    pm(15, "Proteomic identification of differentially expressed proteins between male and female plants in Pistacia chinensis. PLoS One 2013;8(5):e64276 (doi:10.1371/journal.pone.0064276)", "23691188", "PLOS / PubMed"),
    pm(16, "Transcriptome Analysis and Identification of a Female-Specific SSR Marker in Pistacia chinensis Based on Illumina Paired-End RNA Sequencing. Genes (Basel) 2022;13(6):1024 (doi:10.3390/genes13061024)", "35741786", "MDPI / PubMed"),
    pm(17, "SCAR marker for sex identification of Pistacia chinensis Bunge (Anacardiaceae). Genet Mol Res 2014;13(1):1395-1401 (doi:10.4238/2014.February.28.12)", "24634238", "FUNPEC-RP / PubMed"),
    pm(18, "Does landscape fragmentation influence sex ratio of dioecious plants? A case study of Pistacia chinensis in the Thousand-Island Lake region of China. PLoS One 2011;6(8):e22903 (doi:10.1371/journal.pone.0022903)", "21829667", "PLOS / PubMed"),
    pm(19, "Catechin promotes the germination of Pistacia chinensis seeds via GA biosynthesis. Ann Bot 2024;134(2):233-246 (doi:10.1093/aob/mcae061)", "38682952", "Oxford University Press / PubMed"),
    pm(20, "Ethnobotany, ethnopharmacology, phytochemistry, biological activities and toxicity of Pistacia chinensis subsp. integerrima: A comprehensive review. Phytother Res 2020;34(11):2793-2819 (doi:10.1002/ptr.6720)", "32496629", "Wiley / PubMed"),
    pm(21, "Pistacia chinensis: Strong antioxidant and potent testicular toxicity amelioration agent. Asian Pac J Trop Med 2017;10(4):380-389 (doi:10.1016/j.apjtm.2017.03.027)", "28552108", "Elsevier / PubMed"),
    pm(22, "Pistacia chinensis inhibits NO production and upregulates HO-1 induction via PI-3K/Akt pathway in LPS stimulated macrophage cells. Am J Chin Med 2012;40(5):1085-1097 (doi:10.1142/S0192415X12500802)", "22928837", "World Scientific / PubMed"),
    pm(23, "Pistacia chinensis Methanolic Extract Attenuated MAPK and Akt Phosphorylations in ADP Stimulated Rat Platelets In Vitro. Evid Based Complement Alternat Med 2012;2012:895729 (doi:10.1155/2012/895729)", "22899962", "Hindawi / PubMed Central", "PMC3413994", "전문 확인"),
    pm(24, "Structures of 4-aryl-coumarin (neoflavone) dimers isolated from Pistacia chinensis BUNGE and their estrogen-like activity. Chem Pharm Bull 2000;48(4):505-508 (doi:10.1248/cpb.48.505)", "10783069", "Pharmaceutical Society of Japan / PubMed"),
    pm(25, "Pistaciaphenols A-E: novel chalcone-based biflavonoids from the branches of Pistacia chinensis. J Nat Med 2026;80(3):748-757 (doi:10.1007/s11418-026-02023-8)", "42014595", "Springer / PubMed"),
    pm(26, "Multifaceted antibacterial effects of Pistacia chinensis extract against methicillin-resistant Staphylococcus aureus. J Appl Microbiol 2026;137(3) (doi:10.1093/jambio/lxag062)", "41773960", "Oxford University Press / PubMed"),
    pm(27, "[Cold resistance of Pistacia chinensis and Koelreuteria integrifoliola]. Ying Yong Sheng Tai Xue Bao 2011;22(5):1141-1146 (중국어 논문, 영문 초록)", "21812286", "Chinese Journal of Applied Ecology / PubMed"),
    pm(28, "[Effects of NaCl stress on photosynthesis characteristics and fast chlorophyll fluorescence induction dynamics of Pistacia chinensis leaves]. Ying Yong Sheng Tai Xue Bao 2013;24(9):2479-2484 (중국어 논문, 영문 초록)", "24417104", "Chinese Journal of Applied Ecology / PubMed"),
    pm(29, "Sensilla on Organs of Adults of the Pistachio-Seed Wasp Eurytoma plotnikovi (Hymenoptera: Eurytomidae). Microsc Res Tech 2025;88(8):2210-2221 (doi:10.1002/jemt.24851)", "40091550", "Wiley / PubMed"),
    pm(30, "Endozoochory of frugivorous birds as potential dispersal of seed parasites from Pistacia chinensis: experimental evidence. Integr Zool 2020;15(2):149-155 (doi:10.1111/1749-4877.12406)", "31149774", "Wiley / PubMed"),
    pm(31, "Genome assembly and annotation of gall-forming medicinal plant Pistacia chinensis subsp. integerrima. J Genet 2022;101:51", "36420626", "Indian Academy of Sciences / PubMed"),
    pm(32, "Antifungal and Antiproliferative Activity of Pistagremic Acid and Flavonoids Extracted from the Galls of Pistacia chinensis subsp. integerrima. Chem Biodivers 2024;21(2):e202301815 (doi:10.1002/cbdv.202301815)", "38152840", "Wiley / PubMed"),
    pm(33, "Predicting the impacts of climate change on the potential distribution of major native non-food bioenergy plants in China. PLoS One 2014;9(11):e111587 (doi:10.1371/journal.pone.0111587)", "25365425", "PLOS / PubMed"),
]

S = {}
S["overview"] = (
    "황연목(Pistacia chinensis Bunge)은 옻나무과(Anacardiaceae) 피스타치오속의 잎지는 큰키나무로, 암나무와 수나무가 따로 있는 암수딴그루 식물이다[1, 4]. "
    "영어로는 Chinese pistache라 부르며, 중국에서는 정원수·목재·약용으로 쓰이고 씨앗 기름은 바이오디젤 원료로 연구되어 왔다[3, 10, 12, 23].\n\n"
    "식약처 「식품원료 목록」에는 '황연목잎' 한 행만 올라 있고, 상태는 '사용가능', 사용 조건은 '사용가능부위 : 잎'이다[1]. "
    "따라서 식품원료로 쓸 수 있는 부위는 잎뿐이며, 열매·씨앗·나무껍질·가지·벌레집(충영)은 이 목록 행의 사용 부위가 아니다[1]. "
    "목록 행의 다른 이름·영문명 칸은 비어 있다[1]. "
    "이 종을 원재료로 하는 건강기능식품 고시형 원료와 국내 건강기능식품 생산실적은 확인하지 못함.\n\n"
    "잎에서는 갈산·퀘르세틴 배당체 같은 페놀 성분과 리모넨 중심의 정유 성분이 보고되었다[3, 4, 5]. "
    "보고된 효과는 시험관·세포·동물 실험이고, 사람을 대상으로 한 임상시험은 확인하지 못함."
)
S["history"] = (
    "황연목은 중국 전통 의약에서 이질·염증성 부기·건선·류머티즘을 다스리는 데 쓰였다고 소개된다[10]. "
    "다른 논문은 정원수·목재·씨앗 기름과 함께 설사·인후통·해독에 쓰는 민간요법을 이 종의 전통적 쓰임으로 적었다[3]. "
    "중국 남부에서는 이 나무의 벌레집(충영) 추출물을 민간약으로 쓴다고 소개되었다[23]. "
    "채소로도 쓰였다고 기록되어 있으나, 어느 부위를 먹었는지는 확인하지 못함.\n\n"
    "중국 소수민족·토착 집단이 300년 이상 마셔 온 차나무(Camellia) 이외 식물의 '민간 차' 33종을 조사한 연구에 황연목 차가 포함되었다[8]. "
    "이 나무는 강한 적응력 때문에 식용 피스타치오(P. vera)의 대목(접붙이는 뿌리 쪽 나무)으로도 쓰였다[10, 22]. "
    "근래 중국에서는 씨앗 기름 함량이 높아 바이오디젤용 수종으로 대규모 식재가 이루어졌다[10, 13, 33]. "
    "한국에서의 전통적 식용·약용 기록과 국명 '황연목'의 유래는 확인하지 못함."
)
S["biology"] = (
    "황연목은 잎지는 여러해살이 큰키나무로, 3–4월에 꽃이 피고 9–10월에 열매를 맺는다[4]. "
    "꽃잎이 없는 꽃이 바람으로 꽃가루받이를 하며, 열매는 씨가 하나인 핵과다[10]. "
    "암수딴그루라 어린 나무 때에는 겉모습만으로 암수를 가리기 어렵다[17]. "
    "가을에 잎이 붉게 물드는 품종이 있으며, 이 붉은색은 안토시아닌이 쌓여 생기고 PcMYB113 유전자가 관여한다[11].\n\n"
    "잎을 수증기 증류한 정유는 건조 중량 기준 0.53 ± 0.06% 얻어졌고, 리모넨(24.01%)·테르피넨-4-올(9.18%)·β-오시멘(9.15%)·사비넨(8.25%)이 주성분이었다(대만 시료)[3]. "
    "중국 산시성 시료를 고체상미량추출로 분석한 연구에서는 잎 휘발 성분의 65.42%가 세스퀴테르펜, 열매는 76.32%가 모노테르펜이어서 부위·산지·분석법에 따라 조성이 다르게 나타났다[7]. "
    "잎과 꽃차례의 카테킨·루틴·퀘르세틴·캠페롤 함량은 계절과 암수에 따라 달라졌고 새로 돋은 잎에서 가장 높았다[4]."
)
S["related_species"] = (
    "같은 속의 피스타치오(Pistacia vera)는 식약처 목록에서 '견과'를 사용 부위로 하는 별개의 원료이며, 견과 자료를 황연목 잎에 옮겨 쓰면 안 된다[1, 2]. "
    "황연목은 피스타치오의 대목으로 쓰이지만 식용 견과를 생산하는 종은 아니다[10, 22].\n\n"
    "남아시아의 약용식물 Pistacia chinensis subsp. integerrima는 학명에 chinensis가 들어가지만 아종이 다르고, 주로 벌레집(충영)을 약재로 쓴다[20, 32]. "
    "인도 전통의학의 '카크라싱기(Kakdashringi)'라는 이름으로 소개된 추출물 연구는 원료가 이 아종의 충영인지 초록으로는 확인하지 못함[26]. "
    "파키스탄에서 수행된 일부 연구도 'P. chinensis'라 적었으나 아종 표기가 없어, 이 백과에서는 해당 결과를 황연목 잎 자료로 쓰지 않는다[21]. "
    "integerrima 아종의 유전체(462 Mb)와 피스타그렘산 같은 트리테르펜 자료도 황연목 잎과 구분해야 한다[31, 32].\n\n"
    "같은 옻나무과의 옻나무는 줄기·가지만 제한적으로 쓸 수 있고, 붉나무와 붉나무 벌레집인 오배자는 식품원료로 쓸 수 없다[2]."
)
S["cultivation"] = (
    "황연목은 척박한 땅과 나쁜 환경에 잘 적응하여 중국 전역에 널리 분포한다[10]. "
    "1년생 휴면 가지의 반치사 온도(LT50)는 −27.0 °C로 추정되어 비교 수종 가운데 중간 정도의 내한성을 보였다[27]. "
    "1년생 묘목은 염화나트륨 농도가 0.3%에 이르면 최대 광화학 효율이 대조구보다 17.7% 낮아져 염분 스트레스를 받았다[28].\n\n"
    "씨앗 발아가 고르지 않아 묘목 생산이 제한되는데, 카테킨 10 mg/L 처리가 지베렐린 합성을 늘려 발아를 높였다[19]. "
    "씨앗 생산에는 암나무가 필요해 단백질·SCAR·SSR 표지로 어린 묘목의 암수를 가리는 방법이 개발되었다[15, 16, 17]. "
    "토양 질소가 부족하고 개체군이 작을수록 수나무 쪽으로 성비가 치우쳤다[18].\n\n"
    "중국의 재배 적지는 기후 온난화의 영향을 크게 받지 않고 북쪽으로 넓어질 것으로 모형이 예측했다[13]. "
    "세계 한계 토지 가운데 재배 가능 면적은 기계학습 모형으로 1311.85백만 ha로 추정되었다[14]. "
    "씨앗을 먹는 좀벌(Eurytoma plotnikovi)이 주요 해충이며, 한 조사에서 열매의 37%가 씨앗 기생충에 감염되었다[29, 30]. "
    "국내 재배 면적·생산량 통계는 확인하지 못함."
)
S["processing"] = (
    "식품원료로 쓸 수 있는 부위는 잎이므로 가공도 잎을 기준으로 한다[1]. "
    "중국의 민간 차 조사에서는 차 시료 250 mg을 증류수 10 mL로 80 °C에서 30분 우려 분석했으며, 황연목 차는 녹차(EC50 44.23 μg/mL)와 비슷한 DPPH 라디칼 소거능을 보인 차로 꼽혔다[8]. "
    "같은 조사에서 차나무가 아닌 민간 차에서는 카페인·테오브로민·테오필린이 검출되지 않았다[8]. "
    "다만 이 연구 본문에서 황연목 차의 원료 부위(잎·순)와 종별 개별 수치는 확인하지 못함.\n\n"
    "잎 정유는 생잎을 클레븐저 장치로 8시간 수증기 증류해 얻었다[3]. "
    "잎·꽃차례의 페놀·플라보노이드는 봄철 새잎에서 가장 높아, 연구진은 수확 적기를 봄으로 제시했다[4]. "
    "씨앗 기름 함량은 50.76–60.88%였고 바이오디젤 수율은 84.98–98.15%였으나, 씨앗은 식품원료 사용 부위가 아니다[1, 12]. "
    "황연목잎을 원료로 한 국내 가공식품·건강기능식품의 생산실적은 확인하지 못함."
)
S["genetics"] = (
    "중국 39개체의 엽록체 유전체는 160,618–160,821 bp였고, 113개 고유 유전자(단백질 암호 79개, tRNA 30개, rRNA 4개)를 가졌다[10]. "
    "개체 사이에 변이 자리 460곳, 삽입·결실 104곳, 작은 역위 3곳이 있었고 엽록체 일배체형은 12개로 나뉘었다[10]. "
    "피스타치오 참조 유전체에 맞춘 핵 SNP는 3,632,308개였고, 개체의 3분의 1 이상이 잡종으로 분류되어 재배 과정에서 유전 다양성이 줄었다고 해석되었다[10]. "
    "엽록체 일배체형의 첫 분기는 약 842만 년 전(후기 마이오세)으로 추정되었다[10].\n\n"
    "피스타치오속 R2R3-MYB 유전자 158개가 확인되었고, 그중 PcMYB113이 가을 단풍의 안토시아닌 합성에 관여했다[11]. "
    "꽃눈 전사체에서 SSR 21,662개가 찾아졌고 PCSSR55 표지는 암나무에만 나타났다[16]. "
    "SCAR 표지는 64 °C 조건에서 암나무에만 636 bp 단편을 만들었다[17]. "
    "씨앗 기름 축적에는 LEC1·WRI1 전사인자가 관여한다[12]. "
    "황연목 자체의 전체 유전체 조립 논문은 확인하지 못함."
)
S["safety"] = (
    "식약처 목록에서 황연목은 잎만 '사용가능' 원료이며, 별도의 제한적 사용 조건은 없다[1]. "
    "잎이나 잎 추출물을 사람이 먹은 임상시험·인체 안전성 자료는 확인하지 못함. "
    "국내 공공기관의 알레르기·잔류농약·독성 성분 정보도 확인하지 못함.\n\n"
    "미국의 한 목장에서 말 5마리가 급사하고 2마리가 메트헤모글로빈혈증·용혈성 빈혈로 치료받은 사례에서, 목장에 있던 피스타치오속 세 종(황연목 포함)의 잘린 가지가 원인으로 의심되었다[9]. "
    "시험관에서 이 세 종의 잎·씨앗 메탄올 추출물이 말 적혈구에 메트헤모글로빈을 만들고 용혈을 일으켰으며, 씨앗 추출물이 잎보다 강했다[9]. "
    "연구진은 갈산·탄닌산과 그 대사물 피로갈롤을 원인 후보로 보았으나, 원인 물질과 독성 용량은 정하지 못했다[9]. "
    "잎에서도 갈산·디갈산 같은 갈로일 화합물이 분리되었다[5]. "
    "말은 산화 손상에 특히 약한 동물이어서 이 결과를 사람에게 그대로 옮길 수는 없다[9].\n\n"
    "다른 아종(subsp. integerrima) 메탄올 추출물의 동물 독성 용량은 1,500 mg/kg로 보고되었으나 황연목 잎 자료는 아니다[20]. "
    "옻나무과 식물의 우루시올 계열 접촉 피부염이나 피스타치오 견과 알레르기와의 교차 반응이 황연목 잎에 있다는 근거는 확인하지 못함."
)
titles = {"overview": "한눈에 보기", "history": "역사와 쓰임", "biology": "식물학적 특징", "related_species": "근연종과 혼동 주의",
          "cultivation": "재배와 분포", "processing": "가공과 이용", "genetics": "유전체·유전 연구", "safety": "안전성"}

compounds = [
    {"name": "Gallic acid", "name_ko": "갈산", "class": "페놀산", "role": "marker", "part": "잎",
     "content_text": "", "activity_ko": "잎에서 분리한 6개 성분 중 하나[5]; 말 적혈구 산화 손상의 원인 후보 물질로 거론됨(시험관·사례 보고)[9]", "source": [5, 9]},
    {"name": "m-Digallic acid", "name_ko": "m-디갈산", "class": "갈로일 페놀산(뎁사이드)", "role": "bioactive", "part": "잎",
     "content_text": "", "activity_ko": "잎에서 분리·구조 확인[5]", "source": [5]},
    {"name": "Quercetin", "name_ko": "퀘르세틴", "class": "플라보놀", "role": "marker", "part": "잎·꽃차례",
     "content_text": "HPLC로 정량, 계절·암수에 따라 변하고 새잎에서 최고(초록에 수치 없음)[4]", "activity_ko": "잎에서 분리[5]; 추출물은 DPPH 소거능을 보이고 3T3-L1 지방전구세포에 뚜렷한 세포독성이 없었음(시험관·세포 실험)[4]", "source": [4, 5]},
    {"name": "Quercitrin", "name_ko": "퀘르시트린(퀘르세틴-3-O-람노시드)", "class": "플라보놀 배당체", "role": "bioactive", "part": "잎",
     "content_text": "", "activity_ko": "잎에서 분리·구조 확인[5]", "source": [5]},
    {"name": "Quercetin 3-O-(6''-galloyl)-beta-D-glucoside", "name_ko": "퀘르세틴-3-O-(6″-갈로일)-β-D-글루코시드", "class": "갈로일 플라보놀 배당체", "role": "bioactive", "part": "잎",
     "content_text": "", "activity_ko": "잎에서 분리·구조 확인[5]", "source": [5]},
    {"name": "6-O-Galloylarbutin", "name_ko": "6-O-갈로일알부틴", "class": "페놀 배당체", "role": "bioactive", "part": "잎",
     "content_text": "", "activity_ko": "잎에서 분리·구조 확인[5]", "source": [5]},
    {"name": "Catechin", "name_ko": "카테킨", "class": "플라반-3-올", "role": "bioactive", "part": "잎·꽃차례",
     "content_text": "카테킨 수화물로 HPLC 정량, 새잎에서 최고(초록에 수치 없음)[4]", "activity_ko": "씨앗 발아 중 많이 쌓이며, 10 mg/L 외부 처리가 지베렐린 합성을 늘려 발아를 높임(식물 생리 실험, 씨앗)[19]", "source": [4, 19]},
    {"name": "Rutin", "name_ko": "루틴", "class": "플라보놀 배당체", "role": "bioactive", "part": "잎·꽃차례",
     "content_text": "HPLC 정량, 계절·암수에 따라 변동(초록에 수치 없음)[4]", "activity_ko": "", "source": [4]},
    {"name": "Kaempferol", "name_ko": "캠페롤", "class": "플라보놀", "role": "bioactive", "part": "잎·꽃차례",
     "content_text": "HPLC 정량, 계절·암수에 따라 변동(초록에 수치 없음)[4]", "activity_ko": "", "source": [4]},
    {"name": "Limonene", "name_ko": "리모넨", "class": "모노테르펜", "role": "marker", "part": "잎(정유)",
     "content_text": "잎 정유의 24.01%, 활성 분획 E1의 61.06%(GC-MS 피크 면적 백분율)[3]", "activity_ko": "잔틴 산화효소 억제 IC50 37.69 μg/mL(하이포잔틴 기질)·48.04 μg/mL(잔틴 기질), 혼합형 억제(시험관 효소 실험)[3]", "source": [3]},
    {"name": "Terpinen-4-ol", "name_ko": "테르피넨-4-올", "class": "산소화 모노테르펜", "role": "bioactive", "part": "잎(정유)",
     "content_text": "잎 정유의 9.18%(GC-MS 피크 면적 백분율)[3]", "activity_ko": "", "source": [3]},
    {"name": "beta-Ocimene", "name_ko": "β-오시멘", "class": "모노테르펜", "role": "bioactive", "part": "잎(정유)",
     "content_text": "잎 정유의 9.15%(GC-MS 피크 면적 백분율, 기하이성질체 표기는 확인하지 못함)[3]", "activity_ko": "", "source": [3]},
    {"name": "3-Carene", "name_ko": "3-카렌", "class": "모노테르펜", "role": "bioactive", "part": "잎(정유)",
     "content_text": "잎 정유의 5.32%, 분획 E1의 7.04%[3]", "activity_ko": "잔틴 산화효소 억제 IC50 110.34 μg/mL(하이포잔틴 기질), 잔틴 기질에서는 활성 없음(시험관)[3]", "source": [3]},
    {"name": "7-Hydroxy-3-[7-hydroxy-4-(4-hydroxyphenyl)-2-oxo-3,4-dihydrochromen-3-yl]-4-(4-hydroxyphenyl)-3,4-dihydrochromen-2-one", "name_ko": "4-아릴디하이드로쿠마린(네오플라본) 3,3″-이량체", "class": "네오플라본 이량체", "role": "bioactive", "part": "잔가지(식품원료 사용 부위 아님)",
     "content_text": "", "activity_ko": "잔가지에서 입체 배치만 다른 두 이량체를 분리, 에스트로겐 유사 작용 보고(세포 실험)[24]", "source": [24]},
    {"name": "Oleic acid", "name_ko": "올레산", "class": "단일불포화 지방산", "role": "nutrient", "part": "씨앗 기름(식품원료 사용 부위 아님)",
     "content_text": "우수 계통(PC-HN) 씨앗 기름 지방산의 69.94%(C18:1)[12]", "activity_ko": "바이오디젤 연료 특성에 유리한 조성으로 평가됨[12]", "source": [12]},
]

assays = [
    {"role": "literature", "compound": "Limonene", "compound_ko": "리모넨", "part": "잎(정유)",
     "content": "잎 정유의 24.01%(피크 면적 정규화 상대 함량)[3]", "method": "GC-MS",
     "conditions": {
         "instrument": "가스크로마토그래프 + 이온트랩형 질량 검출기(Thermo Fisher Scientific)",
         "column": "DB-5MS(5% 페닐 메틸 폴리실록산), 30 m × 0.25 mm i.d. × 0.25 µm",
         "mobile_phase": "운반 기체 헬륨",
         "gradient": "60 °C 3분 → 2 °C/min로 120 °C(3분 유지) → 3 °C/min로 180 °C → 10 °C/min로 250 °C(5분 유지)",
         "flow": "1 mL/min, 분할비 1:10",
         "temp": "",
         "detection": "질량 스펙트럼 m/z 50–650, NIST·Wiley 라이브러리와 산술 지수(AI) 비교로 동정",
         "injection": "1 μL",
         "sample_prep": "약 35년생 나무의 생잎을 클레븐저 장치로 8시간 수증기 증류, 정유 수율 0.53 ± 0.06%(건조 중량 기준), 4 °C 보관",
         "standard": "",
         "linearity": "", "lod": "", "loq": "", "recovery": ""},
     "rationale": "잎 정유의 최대 성분이자 잔틴 산화효소 억제 활성 분획(E1)의 주성분이어서 잎 정유의 지표로 쓸 수 있다; 정량은 표준품 검량선이 아닌 피크 면적 백분율이다[3]",
     "source": [3], "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9609098/", "source_kind": "paper"},
    {"role": "literature", "compound": "Quercetin", "compound_ko": "퀘르세틴(카테킨 수화물·루틴·캠페롤과 동시 분석)", "part": "잎·꽃차례",
     "content": "계절·암수에 따라 변동, 새잎에서 최고(초록에 수치 없음)[4]", "method": "HPLC",
     "conditions": {"instrument": "", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "", "injection": "", "sample_prep": "", "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""},
     "rationale": "황연목 잎에서 플라보노이드 4종을 HPLC로 정성·정량한 연구로, 수확 시기 판단에 쓰였다; 전문 확인 못함(초록만 확인)[4]",
     "source": [4], "url": "https://pubmed.ncbi.nlm.nih.gov/26717010/", "source_kind": "paper"},
]

# 잎 LC-MS 연구[6]를 compounds 대신 biology 보강용으로 쓴다
S["biology"] += " 이집트에서 재배된 잎의 에탄올 추출물을 LC-ESI-MS/MS로 분석한 연구는 플라보노이드·페놀산과 그 유도체 22종을 잠정 동정했다[6]."
S["history"] += " 잔가지와 가지에서는 에스트로겐 유사 작용을 보인 네오플라본 이량체와 칼콘계 이중 플라보노이드가 분리되었으나 이 부위는 식품원료가 아니다[24, 25]."

d = {
    "slug": "pistacia-chinensis",
    "name_ko": "황연목",
    "name_en": "Chinese pistache",
    "scientific_name": "Pistacia chinensis Bunge",
    "aliases": ["황연목잎", "Chinese pistache"],
    "sections": [{"key": k, "title": titles[k], "body": S[k]} for k in titles],
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
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
for s in d["sections"]:
    print(s["key"], len(s["body"]))
