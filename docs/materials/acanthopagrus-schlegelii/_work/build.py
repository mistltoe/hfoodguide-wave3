import json
from pathlib import Path

A = "2026-11-02"


def P(n, title, url, pub, acc=A):
    return {"n": n, "title": title, "url": url, "publisher": pub, "accessed": acc}


sources = [
    P(1, "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — Acanthopagrus schlegelii 행(감성돔, Black sea bream, 수산물, 부위 '-', 사용가능, 사용 조건 없음, 고시형 원료 원재료 목록 없음; 같은 속 새눈치 Acanthopagrus latus는 별도 행; docs/materials/acanthopagrus-schlegelii/card.json)",
      "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "식품의약품안전처", "2026-10-13"),
    P(2, "Comparison of Biochemical Composition and Non-Volatile Taste Active Compounds of Back and Abdominal Muscles in Three Marine Perciform Fishes, Chromileptes altivelis, Epinephelus akaara and Acanthopagrus schlegelii. Molecules 2022;27(14):4480 (PMC 전문 확인)",
      "https://doi.org/10.3390/molecules27144480", "Molecules (MDPI), PMC9324917"),
    P(3, "A telomere-to-telomere genome assembly of the protandrous hermaphrodite blackhead seabream, Acanthopagrus schlegelii. Sci Data 2025;12(1):350",
      "https://doi.org/10.1038/s41597-025-04602-y", "Scientific Data, PMC11868651"),
    P(4, "Draft genome of the protandrous Chinese black porgy, Acanthopagrus schlegelii. GigaScience 2018;7(4):1-7",
      "https://doi.org/10.1093/gigascience/giy012", "GigaScience, PMC5893958"),
    P(5, "Age and growth of black seabream Acanthopagrus schlegelii (Sparidae) in Hong Kong and adjacent waters of the northern South China Sea. J Fish Biol 2018;93(2):382-390",
      "https://doi.org/10.1111/jfb.13774", "Journal of Fish Biology (PubMed 30069882)"),
    P(6, "Reproductive biology of black seabream Acanthopagrus schlegelii, threadfin porgy Evynnis cardinalis and red pargo Pagrus major in the northern South China Sea. J Fish Biol 2017;91(1):101-125",
      "https://doi.org/10.1111/jfb.13331", "Journal of Fish Biology (PubMed 28542850)"),
    P(7, "Molecular and cellular regulation on sex change in hermaphroditic fish, with a special focus on protandrous black porgy, Acanthopagrus schlegelii. Mol Cell Endocrinol 2020;520:111069",
      "https://doi.org/10.1016/j.mce.2020.111069", "Molecular and Cellular Endocrinology (PubMed 33127483)"),
    P(8, "Oyster farms are the main spawning grounds of the black sea bream Acanthopagrus schlegelii in Hiroshima Bay, Japan. PeerJ 2021;9:e11475",
      "https://doi.org/10.7717/peerj.11475", "PeerJ, PMC8176910"),
    P(9, "Spawning time of black sea bream Acanthopagrus schlegelii, related to underwater photoperiodism in oyster farms. J Fish Biol 2022;101(5):1142-1149",
      "https://doi.org/10.1111/jfb.15179", "Journal of Fish Biology (PubMed 35880803)"),
    P(10, "The role of the isolation of the marginal seas during the Pleistocene in the genetic structure of black sea bream Acanthopagrus schlegelii (Bleeker, 1854) in the coastal waters of Japan. PeerJ 2021;9:e11001",
      "https://doi.org/10.7717/peerj.11001", "PeerJ, PMC8020869"),
    P(11, "Maintenance of Genetic Diversity of Black Sea Bream despite Unmonitored and Large-Scale Hatchery Releases. Biology (Basel) 2022;11(4):554",
      "https://doi.org/10.3390/biology11040554", "Biology (MDPI), PMC9026629"),
    P(12, "Isolation and characterization of eight novel microsatellite markers in Acanthopagrus schlegelii. Genet Mol Res 2016;15(2)",
      "https://doi.org/10.4238/gmr.15027902", "Genetics and Molecular Research (PubMed 27323186)"),
    P(13, "Development of Single Nucleotide Polymorphism and Association Analysis with Growth Traits for Black Porgy (Acanthopagrus schlegelii). Genes (Basel) 2022;13(11):1992",
      "https://doi.org/10.3390/genes13111992", "Genes (MDPI), PMC9690740"),
    P(14, "Proteomic analysis reveals the mechanism of cold tolerance in black porgy (Acanthopagrus schlegelii) via ribosome hibernation, metabolic remodeling, and antioxidant coordination. Comp Biochem Physiol D 2026;58:101748",
      "https://doi.org/10.1016/j.cbd.2026.101748", "Comparative Biochemistry and Physiology Part D (PubMed 41544486)"),
    P(15, "Differential Expression of Hypothalamic and Gill-System With Osmotic Stress in the Euryhaline Black Porgy, Acanthopagrus schlegelii. Front Physiol 2021;12:768122",
      "https://doi.org/10.3389/fphys.2021.768122", "Frontiers in Physiology, PMC8632050"),
    P(16, "Hirame rhabdovirus (HIRRV) as the cause of a natural disease outbreak in cultured black seabream (Acanthopagrus schlegeli) in Korea. Arch Virol 2015;160(12):3063-6",
      "https://doi.org/10.1007/s00705-015-2573-1", "Archives of Virology (PubMed 26315687)"),
    P(17, "Amoebic gill disease outbreak in marine fish cultured in Korea. J Vet Diagn Invest 2017;29(3):357-361",
      "https://doi.org/10.1177/1040638717690783", "Journal of Veterinary Diagnostic Investigation (PubMed 28205457)"),
    P(18, "Infection status of estuarine fish and oysters with intestinal fluke metacercariae in Muan-gun, Jeollanam-do, Korea. Korean J Parasitol 2012;50(3):215-20",
      "https://doi.org/10.3347/kjp.2012.50.3.215", "Korean Journal of Parasitology, PMC3428566"),
    P(19, "Kudoa iwatai and two novel Kudoa spp., K. trachuri n. sp. and K. thunni n. sp. (Myxosporea: Multivalvulida), from daily consumed marine fish in western Japan. Parasitol Res 2011;108(4):913-26",
      "https://doi.org/10.1007/s00436-010-2133-2", "Parasitology Research (PubMed 21053015)"),
    P(20, "Impacts of estuarine dissolved organic matter and suspended particles from fish farming on the biogeochemical cycling of mercury in Zhoushan island, eastern China Sea. Sci Total Environ 2020;705:135921",
      "https://doi.org/10.1016/j.scitotenv.2019.135921", "Science of the Total Environment (PubMed 31818602)"),
    P(21, "Role of mariculture in the loading and speciation of mercury at the coast of the East China Sea. Environ Pollut 2016;218:1037-1044",
      "https://doi.org/10.1016/j.envpol.2016.08.055", "Environmental Pollution (PubMed 27613319)"),
    P(22, "Why mercury concentration increases with fish size? Biokinetic explanation. Environ Pollut 2012;163:192-8",
      "https://doi.org/10.1016/j.envpol.2011.12.026", "Environmental Pollution (PubMed 22249023)"),
    P(23, "Toxicological assessment of inorganic arsenic: Bioaccumulation and immunotoxicity in Acanthopagrus schlegelii. Chemosphere 2025;385:144561",
      "https://doi.org/10.1016/j.chemosphere.2025.144561", "Chemosphere (PubMed 40633225)"),
    P(24, "Dynamic impacts of short-term bath administration of enrofloxacin on juvenile black seabream Acanthopagrus schlegelii. Chemosphere 2024;361:142573",
      "https://doi.org/10.1016/j.chemosphere.2024.142573", "Chemosphere (PubMed 38852630)"),
    P(25, "Effects of tea polyphenol coating combined with ozone water washing on the storage quality of black sea bream (Sparus macrocephalus). Food Chem 2012;135(4):2915-21",
      "https://doi.org/10.1016/j.foodchem.2012.07.078", "Food Chemistry (PubMed 22980890)"),
    P(26, "Effects of alpha-tocopheryl acetate supplementation in preslaughter diet on antioxidant enzyme activities and fillet quality of commercial-size Sparus macrocephalus. J Zhejiang Univ Sci B 2007;8(9):680-5 (초록만 확인, PMC 전문 본문 비어 있음)",
      "https://doi.org/10.1631/jzus.2007.B0680", "Journal of Zhejiang University Science B, PMC1963435"),
    P(27, "Influence of fasting on muscle composition and antioxidant defenses of market-size Sparus macrocephalus. J Zhejiang Univ Sci B 2007;8(12):906-11 (초록만 확인)",
      "https://doi.org/10.1631/jzus.2007.B0906", "Journal of Zhejiang University Science B, PMC2100164"),
    P(28, "Investigation of scaffold manufacturing conditions for 3-dimensional culture of myogenic cell line derived from black sea bream (Acanthopagrus schlegelii). Cytotechnology 2025;77(1):18",
      "https://doi.org/10.1007/s10616-024-00676-5", "Cytotechnology, PMC11635079"),
    P(29, "An Efficient Method for Enrichment and In Vitro Propagation of Muscle Stem Cells Derived from Black Sea Bream (Acanthopagrus schlegelii) Skeletal Muscle. Mar Biotechnol 2025;27(1):49",
      "https://doi.org/10.1007/s10126-025-10428-x", "Marine Biotechnology (PubMed 39954121)"),
    P(30, "Influence of storing muscle tissue in the cold on in vitro myogenic cell line development from the black sea bream (Acanthopagrus schlegelii). Fish Physiol Biochem 2026;52(4)",
      "https://doi.org/10.1007/s10695-026-01773-2", "Fish Physiology and Biochemistry (PubMed 42570030)"),
    P(31, "Population structure of the black seabream Spondyliosoma cantharus along the south-west Portuguese coast inferred from otolith chemistry. J Fish Biol 2012;80(2):427-43",
      "https://doi.org/10.1111/j.1095-8649.2011.03186.x", "Journal of Fish Biology (PubMed 22268439)"),
    P(32, "Bioremediation using Gracilaria chouae co-cultured with Sparus macrocephalus to manage the nitrogen and phosphorous balance in an IMTA system in Xiangshan Bay, China. Mar Pollut Bull 2015;91(1):272-9",
      "https://doi.org/10.1016/j.marpolbul.2014.11.032", "Marine Pollution Bulletin (PubMed 25561001)"),
    P(33, "Relationships between the Gut Microbiota of Juvenile Black Sea Bream (Acanthopagrus schlegelii) and Associated Environment Compartments in Different Habitats. Microorganisms 2021;9(12):2557",
      "https://doi.org/10.3390/microorganisms9122557", "Microorganisms (MDPI), PMC8705249"),
    P(34, "Muan-gun Prohibits Catching Black Sea Bream During May Every Year (2021-04-26 보도; WebSearch 검색 결과 요약으로만 확인, 기사 본문·법령 원문은 이 환경에서 열지 못함)",
      "https://www.asiae.co.kr/en/article/2021042616214400567", "아시아경제"),
    P(35, "비어업인도 금어기·금지체장 위반 땐 과태료 문다 (2020년 수산자원관리법 시행령 개정 보도; WebSearch 검색 결과 요약으로만 확인, 기사 본문·법령 원문은 이 환경에서 열지 못함)",
      "https://www.dailian.co.kr/news/view/919892/", "데일리안"),
]

S = []


def sec(k, t, b):
    S.append({"key": k, "title": t, "body": b.strip()})


sec("overview", "한눈에 보기", """
감성돔(Acanthopagrus schlegelii)은 도미과(Sparidae) Acanthopagrus속에 드는 바닷물고기로, 식약처 「식품원료 목록」에 '감성돔'(영문 Black sea bream)이라는 원료명으로 올라 있다[1]. 이 목록에서 상태는 '사용가능'이고, 사용 부위는 따로 정하지 않은 '-'로 적혀 있으며 별도의 사용 조건은 없다[1]. 건강기능식품 고시형 원료의 원재료 목록에는 없어 식약처가 정한 지표성분도 없다[1].

영어로는 black sea bream 외에 black porgy, blackhead seabream으로도 부르며, 중국과 동아시아에서 가장 인기 있고 값진 상업 어종 가운데 하나로 소개된다[3, 4]. 일본·한국·중국 연안을 포함한 서태평양 연안에 살고, 수컷으로 먼저 성숙한 뒤 암컷으로 바뀌는 웅성선숙 자웅동체라는 점이 특징이다[3, 14]. 중국 양식 개체의 등살은 수분이 76.13%로 같은 연구의 두 바리과 어종보다 높았고, 대신 감칠맛 지표(EUC)가 가장 높게 나왔다[2]. 국내 공공기관의 감성돔 식품성분표 값은 이번 조사에서 확인하지 못함.
""")

sec("history", "이용·관리 역사", """
중국 연구진은 감성돔을 영양이 풍부하고 맛이 좋아 양식 가치가 높은 상업 어종이며 서태평양 여러 나라에서 오랜 이용 역사를 지닌 종으로 소개했고, 중국에서는 자연 자원이 줄고 있다고 적었다[12]. 중국 해산 양식 어류 가운데 생산량이 다섯 번째로 많은 종으로 보고되었다[13].

대만에서는 2004–2015년 관리 기관과 민간이 감성돔 치어를 대량 방류했고, 기록되지 않은 민간 방류도 많아 자연 집단의 유전 구조가 크게 바뀌었다[11]. 중국에서도 방류 사업의 효과를 높이려고 자연산·해상 가두리·육상 못 양식 치어의 장내 미생물을 비교한 연구가 있다[33]. 일본 히로시마만에서는 굴 양식장이 감성돔의 주된 산란장이 되었다[8, 9].

국내에서는 2020년 수산자원관리법 시행령 개정으로 감성돔에 금지체장 25 cm와 5월 한 달 금어기가 정해져 2021년부터 시행되었고, 낚시인 같은 비어업인도 위반하면 과태료를 물게 되었다고 보도되었다[34, 35]. 이 규정의 법령 원문은 이 환경에서 열지 못해 확인하지 못함.
""")

sec("biology", "어종·형태·생태", """
감성돔은 처음 두 해 동안 수컷으로 지내다가 셋째 해부터 자연스럽게 암컷으로 바뀌는 웅성선숙 자웅동체다[3]. 성 전환 과정에서는 혈중 에스트라디올(E2) 농도의 변화가 성의 운명과 관련된다[7]. 홍콩과 남중국해 북부 조사에서 수컷은 1년 안에 성숙하고 2살에 절반이 암컷으로 바뀌었으며, 성 전환 50% 체장은 표준체장 291 mm였다[5, 6].

같은 해역의 이석 분석으로 구한 성장식의 점근 체장은 43.7 cm, 성장계수 K는 0.22/년이었고, 확인된 최고 나이는 9살이었다[5]. 남중국해 북부의 산란기는 11월에서 3월 사이였다[6]. 일본 히로시마만에서는 해 지기 직전에 산란이 가장 많았고, 수정란이 부화하는 최저 수온은 15 ℃였다[9].

감성돔은 바닷물과 민물을 오갈 수 있는 광염성 어종이며, 민물에 옮기면 아가미의 이온 조절 세포가 늘어난다[15]. 수온에도 넓게 견뎌, 저수온 실험에서 내한성 무리는 2.8 ℃까지 버텼다[14]. 자연산 치어는 잡식성이어서 양식 치어보다 장내 미생물이 더 다양했다[33].
""")

sec("related_species", "관련 종·이름", """
식약처 「식품원료 목록」은 같은 속의 새눈치(Acanthopagrus latus)를 감성돔과 별도의 원료로 올려 두었으며, 이 문서는 새눈치의 자료를 섞지 않았다[1]. 학명은 논문에 따라 Acanthopagrus schlegeli로 적히거나, 중국 논문에서 Sparus macrocephalus라는 이명으로 적혀 같은 종을 가리킨다[16, 25]. 일부 연구는 아종 이름을 붙인 Acanthopagrus schlegeli schlegeli로 적었다[22].

영어 이름은 black sea bream·black porgy·blackhead seabream이 함께 쓰인다[3, 4]. 다만 영어 'black seabream'은 유럽 대서양 연안의 다른 도미과 어종 Spondyliosoma cantharus를 가리키기도 해서 논문을 찾을 때 학명으로 구별해야 한다[31].

남중국해 북부 연구는 상업적으로 중요한 도미과 어종인 참돔(Pagrus major)·Evynnis cardinalis(영문 threadfin porgy)와 함께 감성돔을 조사했다[6]. 중국 연구는 감성돔을 값비싼 바리과 어종(Chromileptes altivelis, Epinephelus akaara)과 비교했으며, 산지 가격은 kg당 약 50위안으로 두 바리과 어종(약 700·500위안)보다 훨씬 낮았다[2]. 한국어 이름의 유래를 적은 공식 자료는 확인하지 못함.
""")

sec("cultivation", "양식·어획", """
감성돔은 중국·한국·일본과 여러 동남아 나라에서 인기 있는 해산 양식종이다[2]. 중국 샹산만의 가두리 양식에서는 잡어(생사료)가 주된 영양물질 투입원이었고, 잡어와 치어에 든 질소의 45.55%, 인의 40.52%가 물로 빠져나가 해조류(꼬시래기류)와 함께 기르는 복합 양식이 시험되었다[32]. 양식 감성돔은 겨울철 저수온에 약한 점이 생존의 큰 과제로 꼽혀 내한성 품종 육성을 위한 연구가 이어지고 있다[14].

국내 남해안 양식장에서는 2015년 넙치 랩도바이러스(HIRRV) 감염으로 약 40%가 폐사한 사례가 보고되었다[16]. 같은 해 남해안에서는 아메바성 아가미병(Neoparamoeba perurans)이 감성돔·돌돔·숭어 양식장에 퍼져 6.7–60%의 폐사가 있었다[17].

남중국해 북부 연구는 이 해역의 높은 어획 압력을 지적하며 어린 개체와 나이 든 암컷을 보호하는 어업 관리가 필요하다고 했다[5]. 국내 감성돔의 연도별 양식·어획 생산 통계는 국가통계포털이 이 환경에서 막혀 확인하지 못함.
""")

sec("processing", "가공·저장·세포 배양 연구", """
4 ℃ 냉장 저장 연구에서 오존수(1 mg/L)로 씻은 뒤 0.2% 차 폴리페놀로 코팅하면 15일 동안 뉴클레오타이드 분해·지질 산화·단백질 분해와 세균 증식이 줄고 질감·색·관능 품질이 더 잘 유지되었다[25]. 출하 전 8주 동안 사료에 알파-토코페롤 아세트산을 늘린 감성돔은 필레의 알파-토코페롤이 많아지고 얼음 저장 중 지질 산화가 적었다[26]. 출하 전 굶기면 3일째부터 살의 지방이 줄지만 14일째부터 단백질도 줄고 산화 스트레스가 생겨 신중히 써야 한다고 했다[27].

세포 배양 수산물 기술의 기초로 감성돔 근육에서 근육 줄기세포를 분리해 25계대 넘게 유지한 방법이 보고되었다[29]. 3차원 배양 연구에서는 3% 알긴산나트륨과 4% 젤라틴으로 만든 지지체가 세포 성장을 도왔다[28]. 4 ℃에 보관한 근육 조직에서도 조직 절편 배양으로는 10일, 세포 분리 배양으로는 5일까지 세포주를 만들 수 있었다[30].
""")

sec("genetics", "유전 정보", """
수컷 한 개체로 만든 끊김 없는 텔로미어-텔로미어(T2T) 유전체는 714.98 Mb이고, 서열의 97.87%가 24개 염색체에 배치되었다[3]. 이 유전체에는 단백질 암호 유전자 24,581개가 주석되었고, 반복 서열은 30.95%, BUSCO 완성도는 99.9%였다[3]. 그보다 앞선 2018년 초안 유전체는 688.1 Mb로 추정 크기 739.6 Mb의 93%를 담았고, 단백질 암호 유전자 19,465개를 예측했다[4].

일본 연안 1,046개체의 미토콘드리아 조절 영역 분석에서는 플라이스토세 빙하기의 피난처에서 생긴 세 계통이 일본 전역에 섞여 있어 하나의 자원으로 관리해야 한다고 제안되었다[10]. 중국 자연산 30개체에서 개발한 미세부수체 8개의 평균 관찰 이형접합도는 0.6290이었다[12]. 성장 형질과 관련된 SNP 4개도 보고되었다[13]. 대만에서는 대량 방류가 유전 다양성은 유지했지만 자연 집단의 유전 구조를 크게 바꾼 것으로 나타났다[11].
""")

sec("safety", "안전성", """
식약처 「식품원료 목록」에서 감성돔은 별도 조건 없이 '사용가능' 원료이며, 건강기능식품 고시형 원료가 아니어서 고시 섭취 시 주의사항은 없다[1]. 감성돔을 따로 다룬 국내 공공기관의 알레르기·잔류물질 정보는 이번 조사에서 확인하지 못함.

중국 저우산 양식장 감성돔 살의 메틸수은은 52.7 ± 5.74 ng/g으로 세계보건기구 안전 지침(1000 ng/g)보다 훨씬 낮았다[20]. 다만 잡어를 먹여 기른 감성돔은 배합사료를 먹인 다른 어종보다 살의 총수은과 메틸수은이 유의하게 높았다[21]. 어린 개체에서는 몸집이 클수록 총수은과 메틸수은 농도가 함께 높아졌다[22]. 무기비소를 사료로 28일 먹인 실험에서 근육의 총비소는 습중량 2.13–2.88 mg/kg이었으나 무기비소는 근육에 쌓이지 않고 독성이 낮은 아르세노베타인으로 바뀌었다[23].

일본 야마구치 시장의 감성돔 회와 필레에서는 쿠도아(Kudoa iwatai) 포낭이 나왔다[19]. 반면 전남 무안 감성돔 30마리에서는 사람에게 옮는 장흡충 피낭유충이 나오지 않았다[18]. 항생제 엔로플록사신 약욕 뒤 간의 잔류량은 빠르게 줄었지만, 고용량에서는 7일 휴약 후에도 생리 변화가 남았다[24].
""")

compounds = [
    {"name": "Lysine", "name_ko": "라이신(유리)", "class": "아미노산", "role": "nutrient", "part": "근육(등살·뱃살)",
     "content_text": "본문에 '46.82–55.37 mg/g of wet weight'로 적힘(같은 글의 총 유리아미노산이 등살 301.59, 뱃살 271.03 mg/100 g이어서 단위가 맞지 않음; 원문 그대로 옮김)",
     "activity_ko": "감성돔 근육에서 가장 많은 유리아미노산이었다(바리과 두 종은 글리신이 가장 많음)[2]", "source": [2]},
    {"name": "Glycine", "name_ko": "글리신(유리)", "class": "아미노산", "role": "nutrient", "part": "근육(등살·뱃살)",
     "content_text": "라이신 다음으로 많음(감성돔 개별 수치는 표에만 있어 본문에서 확인하지 못함)",
     "activity_ko": "단맛을 내는 유리아미노산으로 분류되었다[2]", "source": [2]},
    {"name": "Alanine", "name_ko": "알라닌(유리)", "class": "아미노산", "role": "nutrient", "part": "근육(등살·뱃살)",
     "content_text": "라이신·글리신 다음으로 많음(감성돔 개별 수치는 본문에서 확인하지 못함)",
     "activity_ko": "단맛 계열 유리아미노산이다[2]", "source": [2]},
    {"name": "Glutamic acid", "name_ko": "글루탐산(유리)", "class": "아미노산", "role": "bioactive", "part": "근육(등살·뱃살)",
     "content_text": "감성돔 개별 수치는 본문에서 확인하지 못함; 감성돔의 MSG 유사 아미노산 합계는 두 바리과 어종보다 유의하게 많았음",
     "activity_ko": "IMP와 함께 세 어종의 주된 감칠맛 성분으로, 감칠맛 환산값(EUC) 계산에 쓰였다[2]", "source": [2]},
    {"name": "Inosine monophosphate", "name_ko": "이노신산(IMP)", "class": "뉴클레오타이드", "role": "bioactive", "part": "근육(등살·뱃살)",
     "content_text": "세 어종 모두 주된 5′-뉴클레오타이드(감성돔 개별 수치는 본문에서 확인하지 못함)",
     "activity_ko": "맛의 복합성과 단맛에 기여하는 주된 정미 뉴클레오타이드로 설명되었다[2]", "source": [2]},
    {"name": "Adenosine monophosphate", "name_ko": "아데닐산(AMP)", "class": "뉴클레오타이드", "role": "bioactive", "part": "근육(등살·뱃살)",
     "content_text": "세 어종 범위 0.91–12.22 mg/100 g(감성돔은 바리과 두 종 사이); 원문은 맛 역치(50–100 mg/100 g)보다 낮다고 함",
     "activity_ko": "단맛에 기여하지만 이 농도에서는 맛 기여가 작다고 보았다[2]", "source": [2]},
    {"name": "Lactic acid", "name_ko": "젖산", "class": "유기산", "role": "bioactive", "part": "근육(등살·뱃살)",
     "content_text": "5.26–7.95 mg/g (습중량, 세 어종 중 가장 많음)",
     "activity_ko": "맛 활성값 기준(126 mg/100 g)을 넘어 신맛과 감칠맛에 기여하는 주된 유기산이었다[2]", "source": [2]},
    {"name": "Malic acid", "name_ko": "말산", "class": "유기산", "role": "bioactive", "part": "근육(등살·뱃살)",
     "content_text": "0.17–0.18 mg/g (습중량)",
     "activity_ko": "맛 활성값 기준(50 mg/100 g)보다 낮아 맛 기여는 작다고 보았다[2]", "source": [2]},
    {"name": "Docosahexaenoic acid", "name_ko": "DHA", "class": "n-3 지방산", "role": "nutrient", "part": "근육(등살·뱃살)",
     "content_text": "감성돔의 주된 고도불포화지방산(개별 비율은 본문에서 확인하지 못함); n-3 지방산 합계 13.63–15.91% (총 지방산 중)",
     "activity_ko": "심혈관·뇌·눈 건강과 관련된 장쇄 n-3 지방산으로 소개되었다[2]", "source": [2]},
    {"name": "cis-Vaccenic acid", "name_ko": "시스-박센산(C18:1n-7)", "class": "단일불포화지방산", "role": "nutrient", "part": "근육(등살·뱃살)",
     "content_text": "26.30–29.76% (총 지방산 중, 세 어종 중 가장 높음)",
     "activity_ko": "감성돔에서 가장 많은 단일불포화지방산이었다[2]", "source": [2]},
    {"name": "Palmitoleic acid", "name_ko": "팔미톨레산(C16:1n-7)", "class": "단일불포화지방산", "role": "nutrient", "part": "근육(등살·뱃살)",
     "content_text": "6.53–7.28% (총 지방산 중, 세 어종 중 가장 높음)",
     "activity_ko": "바리과 두 종보다 유의하게 많았다[2]", "source": [2]},
    {"name": "Phosphate", "name_ko": "인산 이온", "class": "무기 이온", "role": "nutrient", "part": "근육(등살·뱃살)",
     "content_text": "세 어종 범위 4.86–7.01 mg/g (습중량) 가운데 감성돔이 가장 많음",
     "activity_ko": "쓴맛을 줄이고 감칠맛과 신맛을 높이는 보조 맛 성분으로 설명되었다[2]", "source": [2]},
    {"name": "Chloride", "name_ko": "염화 이온", "class": "무기 이온", "role": "nutrient", "part": "근육",
     "content_text": "등살 0.78 mg/g, 뱃살 1.34 mg/g (습중량)",
     "activity_ko": "신맛을 누르고 감칠맛·단맛을 높이는 성분으로 설명되었다[2]", "source": [2]},
    {"name": "alpha-Tocopherol", "name_ko": "알파-토코페롤(비타민 E)", "class": "지용성 비타민", "role": "nutrient", "part": "필레",
     "content_text": "사료 알파-토코페롤 아세트산 289·553·1069 mg/kg 급여군에서 각각 14.2·22.1·30.9 μg/mg fillet (초록 표기 그대로, 사육 실험값)",
     "activity_ko": "많이 쌓일수록 얼음 저장 중 필레의 지질 산화가 줄었다[26]", "source": [26]},
]

common_prep = "양식 감성돔(중국 푸젠성 닝더 상업 양식장, 9마리를 3군으로 나눔) 등살·뱃살을 군별로 섞어 −80 °C 보관"
assays = [
    {"role": "literature", "compound": "Free amino acids (lysine etc.)", "compound_ko": "유리아미노산(라이신 등)", "part": "근육(등살·뱃살)",
     "content": "감성돔 주된 유리아미노산은 라이신; 총 유리아미노산 등살 301.59, 뱃살 271.03 mg/100 g(습중량)[2]",
     "method": "HPLC-PDA (AccQ-Tag 유도체화)",
     "conditions": {"instrument": "Waters 2996 HPLC, Waters 2996 광다이오드 어레이 검출기",
                    "column": "Waters Pico-Tag C18, 3.9 × 150 mm",
                    "mobile_phase": "A: AccQ-Tag Eluent A(물과 10:1), B: 100% 아세토나이트릴, C: 탈이온수",
                    "gradient": "100% A → 0.5분 99% A/1% B → 18분 94% A/6% B → 19분 90% A/10% B → 29.5분 83% A/17% B → 33분 60% B/40% C → 36분 100% A → 45분 100% A",
                    "flow": "", "temp": "", "detection": "248 nm", "injection": "5 μL",
                    "sample_prep": common_prep + "; 시료 2.5 g + 10% 트라이클로로아세트산 3배량 균질 → 10,000×g 15분 4 °C 원심 → 상등액 25 μL 분취",
                    "standard": "아미노산 표준품(Sigma-Aldrich), 머무름 시간·피크 면적 비교",
                    "linearity": "", "lod": "", "loq": "", "recovery": ""},
     "rationale": "유리아미노산은 단맛·감칠맛·쓴맛을 내는 생선 맛의 핵심 지표이며, 감성돔은 라이신이 가장 많아 바리과 어종과 구별되었다[2]. 전문(Methods) 확인 — 유속·칼럼 온도·검출·정량한계·회수율은 본문에 없음[2].",
     "source": [2], "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9324917/", "source_kind": "paper"},
    {"role": "literature", "compound": "Inosine monophosphate", "compound_ko": "이노신산(IMP) 등 5′-뉴클레오타이드", "part": "근육(등살·뱃살)",
     "content": "IMP가 주된 5′-뉴클레오타이드, 다음 AMP·GMP; AMP는 세 어종 0.91–12.22 mg/100 g[2]",
     "method": "HPLC-UV",
     "conditions": {"instrument": "Waters 2996 HPLC", "column": "Inertsil ODS-3, 4.6 × 250 mm, 5 μm (원문 표기 'Intersil ODS-3')",
                    "mobile_phase": "A: 메탄올, B: 0.05% 인산", "gradient": "", "flow": "1.0 mL/min", "temp": "30 °C",
                    "detection": "UV 260 nm", "injection": "10 μL",
                    "sample_prep": common_prep + "; 시료 약 5 g + 0.6 M 과염소산 25 mL 15분 균질 → 10,000×g 10분 4 °C 원심 → 1 M KOH로 중화 → 0.45 μm 셀룰로스 막 여과",
                    "standard": "뉴클레오타이드 표준품(Sigma-Aldrich) 검량선", "linearity": "", "lod": "", "loq": "", "recovery": ""},
     "rationale": "IMP는 생선 감칠맛의 주된 정미 뉴클레오타이드로 감칠맛 환산값(EUC) 계산에 쓰인다[2]. 전문(Methods) 확인 — 이동상 비율·기울기와 검출·정량한계는 본문에 없음[2].",
     "source": [2], "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9324917/", "source_kind": "paper"},
    {"role": "literature", "compound": "Lactic acid", "compound_ko": "젖산(유기산)", "part": "근육(등살·뱃살)",
     "content": "감성돔 5.26–7.95 mg/g, 말산 0.17–0.18 mg/g (습중량)[2]",
     "method": "HPLC-UV",
     "conditions": {"instrument": "Waters 2996 HPLC", "column": "Inertsil ODS-3, 4.6 × 250 mm, 5 μm (5′-뉴클레오타이드와 같은 조건)",
                    "mobile_phase": "A: 메탄올, B: 0.05% 인산", "gradient": "", "flow": "1.0 mL/min", "temp": "30 °C",
                    "detection": "UV 215 nm", "injection": "10 μL (뉴클레오타이드 조건과 같다고 적힘)",
                    "sample_prep": common_prep + "; 시료 약 1 g + 정제수 5 mL 5분 균질 → 10,000×g 20분 4 °C 원심 → 0.45 μm 셀룰로스 막 여과",
                    "standard": "말산·젖산·시트르산·숙신산 표준품(Sinopharm) 검량선", "linearity": "", "lod": "", "loq": "", "recovery": ""},
     "rationale": "젖산은 맛 활성값을 넘는 주된 유기산으로 신맛·감칠맛에 기여하며, 감성돔에서 세 어종 중 가장 많았다[2]. 전문(Methods) 확인 — 검출·정량한계·회수율은 본문에 없음[2].",
     "source": [2], "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9324917/", "source_kind": "paper"},
    {"role": "literature", "compound": "Docosahexaenoic acid", "compound_ko": "DHA 등 지방산 조성", "part": "근육(등살·뱃살)",
     "content": "DHA가 감성돔의 주된 고도불포화지방산; n-3 합계 13.63–15.91%, C18:1n-7 26.30–29.76%, C16:1n-7 6.53–7.28% (총 지방산 중)[2]",
     "method": "GC-MS (지방산 메틸에스터)",
     "conditions": {"instrument": "Agilent GC-MS 7894A-5975C (원문 표기 그대로)",
                    "column": "HP-5MS, 30 m × 250 μm × 0.25 μm (Agilent)",
                    "mobile_phase": "운반 기체 헬륨(99.999%)",
                    "gradient": "오븐 50 °C → 5 °C/min로 200 °C → 2 °C/min로 230 °C, 10분 유지",
                    "flow": "3.0 mL/min", "temp": "주입구 260 °C, 전달관 280 °C, 이온원 230 °C",
                    "detection": "EI 70 eV, m/z 50–550 전이온(TIC) 스캔", "injection": "1 μL, 분할비 2:1",
                    "sample_prep": common_prep + "; 균질 육 2 g을 클로로폼–메탄올(2:1)로 총지질 추출 → 비누화 → 에스터화 → 헥세인으로 FAME 회수",
                    "standard": "Supelco 37 성분 FAME 혼합 표준(Cat. No. 47885-U) 머무름 시간 비교, 피크 면적 비(% 총 지방산)",
                    "linearity": "", "lod": "", "loq": "", "recovery": ""},
     "rationale": "DHA·n-3 지방산 비율은 생선의 영양 품질을 나타내는 대표 지표다[2]. 전문(Methods) 확인 — 정량은 면적 백분율이며 검출·정량한계·회수율은 본문에 없음[2].",
     "source": [2], "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9324917/", "source_kind": "paper"},
]

d = {
    "slug": "acanthopagrus-schlegelii",
    "name_ko": "감성돔",
    "name_en": "Black sea bream",
    "scientific_name": "Acanthopagrus schlegelii (Bleeker, 1854)",
    "aliases": ["감성돔", "Black sea bream", "Black porgy", "Blackhead seabream",
                "Acanthopagrus schlegeli", "Sparus macrocephalus", "Acanthopagrus schlegeli schlegeli"],
    "sections": S,
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
out = Path(__file__).resolve().parent.parent / "dossier.json"
out.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in S:
    print(s["key"], len(s["body"]))
