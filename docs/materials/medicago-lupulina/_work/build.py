import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
A = "2026-11-02"
def pm(n, pmid, title, journal, year, doi=None, pmc=None):
    return {"n": n, "title": f"{title} ({journal}, {year}; PMID {pmid}" + (f"; {pmc}" if pmc else "") + (f"; doi:{doi}" if doi else "") + ")",
            "url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/", "publisher": f"{journal} (PubMed)", "accessed": A}
sources = [
 {"n": 1, "title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 잔개자리씨앗·잔개자리잎(Medicago lupulina)", "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
 pm(2, "33799441", "Optimization of Two Eco-Friendly Extractions of Black Medick (Medicago lupulina L.) Phenols and Their Antioxidant, Cosmeceutical, α-Glucosidase and α-Amylase Inhibitory Properties", "Molecules", 2021, "10.3390/molecules26061610", "PMC7998307"),
 pm(3, "25924534", "Evaluation of antioxidant activity, and quantitative estimation of flavonoids, saponins and phenols in crude extract and dry fractions of Medicago lupulina aerial parts", "Nat Prod Commun", 2015),
 pm(4, "41618587", "From plant to potential therapy: antioxidant and anticancer potential of Medicago lupulina and Trifolium arvense", "J Sci Food Agric", 2026, "10.1002/jsfa.70488"),
 pm(5, "30602699", "Small-Seeded Legumes as a Novel Food Source. Variation of Nutritional, Mineral and Phytochemical Profiles in the Chain: Raw Seeds-Sprouted Seeds-Microgreens", "Molecules", 2018, "10.3390/molecules24010133", "PMC6337440"),
 pm(6, "32252361", "Activity of Saponins from Medicago Species against Phytoparasitic Nematodes", "Plants (Basel)", 2020, "10.3390/plants9040443", "PMC7238174"),
 pm(7, "39464371", "The genome sequence of the Black Medic, Medicago lupulina L.", "Wellcome Open Res", 2024, "10.12688/wellcomeopenres.23134.2", "PMC11503012"),
 pm(8, "42762127", "T2T genome assembly and CRISPR/Cas9 editing of Medicago lupulina", "J Integr Plant Biol", 2026, "10.1111/jipb.70401"),
 pm(9, "21616866", "Phylogeny and character evolution in Medicago (Leguminosae): Evidence from analyses of plastid trnK/matK and nuclear GA3ox1 sequences", "Am J Bot", 2010, "10.3732/ajb.1000009"),
 pm(10, "19174379", "Population genetic structure of two Medicago species shaped by distinct life form, mating system and seed dispersal", "Ann Bot", 2009, "10.1093/aob/mcp006", "PMC2707894"),
 pm(11, "21196450", "Cotyledon damage affects seed number through final plant size in the annual grassland species Medicago lupulina", "Ann Bot", 2010, "10.1093/aob/mcq259", "PMC3043934"),
 pm(12, "38472470", "Serpentine environment prevails over geographic distribution in shaping the genetic diversity of Medicago lupulina L.", "Mol Genet Genomics", 2024, "10.1007/s00438-024-02124-7"),
 pm(13, "30280335", "Accumulation of heavy metals in native Andean plants: potential tools for soil phytoremediation in Ancash (Peru)", "Environ Sci Pollut Res Int", 2018),
 pm(14, "23488175", "Evaluation of Atriplex halimus, Medicago lupulina and Portulaca oleracea for phytoremediation of Ni, Pb, and Zn", "Int J Phytoremediation", 2013, "10.1080/15226514.2012.716102"),
 pm(15, "25903186", "Rhizobial symbiosis effect on the growth, metal uptake, and antioxidant responses of Medicago lupulina under copper stress", "Environ Sci Pollut Res Int", 2015, "10.1007/s11356-015-4530-7"),
 pm(16, "30672624", "Effects of drought-stressed temperate forage legumes on the degradation and the rumen microbial community in vitro", "J Anim Physiol Anim Nutr (Berl)", 2019, "10.1111/jpn.13047"),
 pm(17, "24670435", "Climate extreme effects on the chemical composition of temperate grassland species under ambient and elevated CO2: a comparison of fructan and non-fructan accumulators", "PLoS One", 2014, "10.1371/journal.pone.0092044", "PMC3966776"),
 pm(18, "33053861", "Sprouts vs. Microgreens as Novel Functional Foods: Variation of Nutritional and Phytochemical Profiles and Their In Vitro Bioactive Properties", "Molecules", 2020, "10.3390/molecules25204648", "PMC7587365"),
 pm(19, "34346216", "Determination of the Effect of Co-cultivation on the Production and Root Exudation of Flavonoids in Four Legume Species Using LC-MS/MS Analysis", "J Agric Food Chem", 2021, "10.1021/acs.jafc.1c02821", "PMC8389803"),
 pm(20, "31277670", "A divergent strain of melon chlorotic spot virus isolated from black medic (Medicago lupulina) in Austria", "Virol J", 2019, "10.1186/s12985-019-1195-8", "PMC6612211"),
 pm(21, "3450677", "Cryptic viruses in hop trefoil (Medicago lupulina) and their relationships to other cryptic viruses in legumes", "Intervirology", 1987, "10.1159/000150010"),
 pm(22, "41465260", "Mitogenome of Medicago lupulina L. Cultivar-Population VIK32, Line MlS-1: Dynamic Structural Organization and Foreign Sequences", "Int J Mol Sci", 2025, "10.3390/ijms262411830", "PMC12733082"),
 pm(23, "40691755", "Genome-wide identification and functional analysis of the GRAS gene family in Medicago lupulina L.", "BMC Genomics", 2025, "10.1186/s12864-025-11855-9", "PMC12278555"),
 pm(24, "26606826", "Development of Arbuscular Mycorrhiza in Highly Responsive and Mycotrophic Host Plant-Black Medick (Medicago lupulina L.)", "Ontogenez", 2015),
 pm(25, "34834870", "Mycorrhiza-Induced Alterations in Metabolome of Medicago lupulina Leaves during Symbiosis Development", "Plants (Basel)", 2021, "10.3390/plants10112506", "PMC8617643"),
 {"n": 26, "title": "Medicago lupulina L. — Plants of the World Online(분포: 원산지·도입 지역). 이 환경에서 사이트에 접속하지 못해 WebSearch 요약으로만 확인함", "url": "https://powo.science.kew.org/taxon/urn:lsid:ipni.org:names:506268-1", "publisher": "Royal Botanic Gardens, Kew", "accessed": A},
 {"n": 27, "title": "국내 개자리속(Medicago) 분류군 식별 DNA 마커 연구(KoreaScience JAKO202231557787561). 원문을 열지 못해 WebSearch 요약으로만 확인함", "url": "https://koreascience.kr/article/JAKO202231557787561.pdf", "publisher": "KoreaScience(한국과학기술정보연구원)", "accessed": A},
 pm(28, "29104370", "Is there sufficient Ensifer and Rhizobium species diversity in UK farmland soils to support red clover, white clover, lucerne and black medic?", "Appl Soil Ecol", 2017, "10.1016/j.apsoil.2017.06.030", "PMC5637928"),
 pm(29, "33604168", "Effects of mixing two legume species at seedling stage under different environmental conditions", "PeerJ", 2021, "10.7717/peerj.10615", "PMC7863785"),
 pm(30, "30120869", "Rapid evolution in native plants cultivated for ecological restoration: not a general pattern", "Plant Biol (Stuttg)", 2018, "10.1111/plb.12901"),
 pm(32, "35009086", "Phytochemicals and Biological Activities of Barleria (Acanthaceae)", "Plants (Basel)", 2021, "10.3390/plants11010082", "PMC8747396"),
 pm(31, "41590688", "Spatial Heterogeneity of Metabolic Response to Drought Stress in Medicago lupulina L. Leaves", "Metabolites", 2026, "10.3390/metabo16010080", "PMC12844375"),
]

S = {}
S["overview"] = ("개요", """잔개자리(Medicago lupulina L.)는 콩과 개자리속의 한해살이 또는 짧게 사는 여러해살이풀로, 영어로는 Black medick(black medic)이라 부른다[1][7]. 식품의약품안전처 「식품원료 목록」에는 '잔개자리씨앗'과 '잔개자리잎' 두 원료명으로 올라 있고, 별명으로 '승앵이자리'가 함께 적혀 있다[1]. 같은 속의 알팔파(자주개자리, M. sativa)와는 다른 종이며, 목록에서도 따로 관리된다[1].

식품원료로서의 지위는 '사용가능'이며, 사용 조건은 '사용가능부위 : 잎, 씨앗'이다[1]. 따라서 일반 식품원료로 쓸 수 있는 부위는 잎과 씨앗이고, 뿌리·꽃·줄기 전체는 목록상 사용가능부위로 적혀 있지 않다[1]. 이 종을 원재료로 하는 건강기능식품 고시형 원료는 이번 조사에서 확인하지 못함.

유럽·북아프리카·서아시아·남아시아가 원산이며, 지금은 아메리카·오스트레일리아·중앙 및 북아시아 등에 널리 퍼져 길가·잔디밭·목초지 같은 사람이 손댄 땅에서 흔히 자란다[7]. 가축 풋먹이·풋거름·건초용으로 재배된 적이 있고, 요즘은 지상부 폴리페놀 연구와 씨앗 싹·마이크로그린 같은 새 식품 소재 연구가 나오고 있다[2][5][7]. 효능 자료는 대부분 시험관·세포 실험이며, 사람을 대상으로 한 임상시험은 이번 조사에서 확인하지 못함."""
)
S["history"] = ("역사·이용", """잔개자리는 유라시아 원산의 '오래된 식용 식물', '전통 식용 식물'로 소개되며[2], 약용으로 쓸 가능성도 언급된다[5]. 작은 씨앗을 맺는 콩과 식물의 씨앗은 북아프리카·서남아시아의 구석기 말·신석기 유적에서 흔히 나오며, 사람의 먹을거리였을 가능성이 거론된다[5]. 다만 이 유적 씨앗이 잔개자리라는 종 수준의 근거는 이번 조사에서 확인하지 못함.

농업에서는 구대륙과 신대륙 모두에서 가축 풋먹이, 풋거름, 건초 작물로 재배되어 왔다[7]. 영국 유기농 농장의 콩과 혼파 목초[28], 독일의 사료 콩과 가뭄 시험[16], 독일의 생태 복원용 토착종 씨앗 생산[30]처럼 목초·녹비 식물로서의 이용이 연구되었다[16][28][30]. 독일 생태 복원용 씨앗 농장에서 여러 세대 증식한 결과, 짧게 살고 주로 제꽃가루받이를 하는 잔개자리는 다른 네 종보다 유전·형질 변화가 컸다[30].

국내에는 원래 자생하던 종이 아니라 들어와 퍼진 종으로 분류되며, 국내에 분포한다고 추정되는 개자리속 다섯 분류군 가운데 하나로 거론된다[26][27]. 들어온 시기와 경로는 이번 조사에서 확인하지 못함. 식품원료 목록에 씨앗과 잎이 사용가능 원료로 올라 있다[1]."""
)
S["biology"] = ("생물학적 특징", """잔개자리는 땅에 눕거나 비스듬히 퍼지는 한해살이풀이지만 짧게 사는 여러해살이로 자라기도 한다[7]. 잎은 작은잎 세 장으로 된 세겹잎이고, 줄기는 길이 80 cm(8 dm)까지 자라며, 가는 곁뿌리가 촘촘한 뿌리층을 만든다[2]. 잎 표면에는 단순털과 끝이 샘처럼 된 털이 덮여 있어 가루이 산란 같은 곤충 피해를 줄인다고 보고되었다[7].

번식은 주로 제꽃가루받이에 의존하며, 중국 16개 집단을 분석한 연구에서 자가수분율이 95.8%로 추정되었다[10]. 같은 연구에서 집단 간 유전 분화(FST 0.535)가 크고 유전 다양성(평균 HE 0.246)은 여러해살이 근연종 M. ruthenica보다 낮았다[10]. 영국 표본 보고에서는 완전한 제꽃가루받이에서 상당한 딴꽃가루받이까지 폭이 넓다는 선행 연구를 소개한다[7].

떡잎을 떼어 낸 실험에서는 식물 크기가 줄며 꽃 수와 씨앗 수가 줄었지만 씨앗 한 알의 무게는 바뀌지 않았다[11]. 뿌리혹세균(Ensifer/Sinorhizobium)과 공생해 질소를 고정하고, 인이 적은 흙에서는 수지상 균근균과 강하게 공생하는 '균근 의존성' 식물로도 연구된다[15][24][28]. 염색체 수는 2n = 16인 이배체로 보고되었다[7]."""
)
S["related_species"] = ("근연종·혼동", """개자리속(Medicago)은 약 87종으로, 모델 식물 M. truncatula와 사료 작물인 알팔파(M. sativa), 스네일메딕(M. scutellata), 잔개자리 등이 속한다[9]. 엽록체 trnK/matK와 핵 GA3ox1 유전자 계통 분석에서 잔개자리는 '축소된 Leptospireae 아절 분지군'에 들어가며, 알팔파가 속한 Medicago 절과는 다른 갈래였다[9]. 이 연구에서 개자리속의 자매 속으로는 호로파속(Trigonella, 전동싸리속 Melilotus 포함)이 함께 분석되었다[9].

식품원료 목록에서 같은 속의 다른 원료는 알팔파(자주개자리) 하나이며, 알팔파는 '자주개자리잎'·'자주개자리씨앗' 등 여러 원료명으로 따로 올라 있다[1]. 두 종 모두 사용가능부위가 '잎, 씨앗'으로 같지만 별개의 원료이므로, 알팔파 제품·연구 자료를 잔개자리에 그대로 옮겨 쓰면 안 된다[1][9].

논문을 찾을 때 'lupulina'만 쓰면 종소명이 같은 쥐꼬리망초과 Barleria lupulina 연구가 함께 나오므로 구분해야 한다[32]. 영어 옛 이름 hop trefoil도 잔개자리를 가리키는 이름으로 쓰인 예가 있다[21]."""
)
S["cultivation"] = ("재배·자생", """잔개자리는 목초지·잔디밭·보도 틈 같은 교란된 땅에 흔하며, 대개 잡초로 여겨지지만 목초·녹비용으로 재배되기도 했다[7]. 석회질의 건조한 흙을 좋아하고, 니켈·코발트·크롬이 많은 사문암 토양 가장자리에서도 자란다[12]. 보스니아 11개 집단 연구에서 사문암 집단도 유전 다양성이 줄지 않았고, 유전 구조는 지리적 거리보다 토양 조건과 더 관련되었다[12].

사료 작물로는 독일에서 품종 'Ekola'를 다른 콩과 목초와 함께 가뭄 처리 시험에 썼고, 가뭄을 겪은 풀은 반추위 모의 실험에서 건물·유기물 분해율과 메탄 생성이 줄었다[16]. 기온 상승과 물 부족이 겹치면 탄수화물·페놀과 콩과의 리그닌이 늘었고, 높은 이산화탄소까지 겹치면 콩과의 단백질·인·마그네슘이 줄었다[17]. 알사이크클로버와 섞어 뿌린 발아 시험의 혼파 효과는 −9%에서 +11% 사이로 일정하지 않았고[29], 밀과 함께 키우면 다이드제인·메디카르핀·포르모노네틴 등 플라보노이드 농도가 콩과 조직과 뿌리 분비물에서 늘었다[19].

오스트리아의 잔개자리에서는 멜론 퇴록반점 바이러스 계통이 분리되었고, 영국 연구에서는 겉보기 건강한 묘의 98–99%가 잠복성 바이러스를 지니고 있었다[20][21]. 광산 폐기물 토양에서 구리에 강한 뿌리혹세균과 공생하면 생육과 질소 함량이 늘고 뿌리의 구리 축적이 크게 늘었다[15]. 국내 재배 면적·생산량 통계는 확인하지 못함."""
)
S["processing"] = ("가공·제품", """식품원료로 쓸 수 있는 부위는 잎과 씨앗이며, 국내에서 이 원료로 만든 제품의 생산실적은 이번 조사에서 확인하지 못함. 연구에서는 씨앗을 그대로, 또는 싹을 틔운 싹채소와 첫 본잎이 나온 마이크로그린으로 가공하는 방법이 검토되었다[5][18]. 리투아니아 연구에서 작은 씨앗 콩과 7종의 씨앗·싹·마이크로그린은 건물 100 g당 단백질 32.0–58.7 g으로 단백질이 풍부했고, 단계가 씨앗→싹→마이크로그린으로 갈수록 단백질과 이차대사산물은 늘고 총탄수화물은 줄었다[5]. 이 연구에서 잔개자리 생씨앗의 칼슘은 건물 100 g당 0.789 g으로 비교한 시료 가운데 가장 높은 값이었다[5].

폴란드 연구는 잔개자리(black medick) 싹을 싹채소 8종 가운데 하나로 넣어 폴리페놀·비타민 C·아미노산 등을 비교했다[18]. 지상부(꽃·잎·줄기)는 직사광선 없는 실내에서 14일 말린 뒤, 물에 글리세롤 45% 또는 폴리프로필렌글리콜 10%를 섞어 70–80 °C에서 60분 초음파 추출하는 조건이 최적으로 제시되었다[2]. 이 글리세롤 추출물은 항산화·α-아밀레이스·α-글루코시데이스 억제 활성을 보였지만, 일부 활성은 용매인 글리세롤 자체에서 나왔다[2].

메탄올·에틸아세테이트 추출물을 비교한 2026년 연구에서는 잔개자리 에틸아세테이트 추출물의 금속 킬레이트 활성이 17.89 mg EDTA 당량/g이었다[4]. 이 결과들은 모두 시험관 실험이다[2][4]."""
)
S["genetics"] = ("유전체·분자", """영국 스코틀랜드에서 채집한 개체로 만든 참조 유전체는 길이 575.40 Mb이고, 99%가 8개 염색체 수준 서열로 정리되었다[7]. 유세포 분석으로 잰 유전체 크기(1C)는 0.75 pg(약 730 Mb)였고, 단백질 암호화 유전자 27,424개가 주석되었다[7]. 미토콘드리아 유전체는 294.12 kb, 엽록체 유전체는 123.99 kb로 조립되었다[7].

2026년에는 빈틈 없는(T2T) 유전체 조립과 함께 CRISPR/Cas9 유전자 편집으로 잎 모양을 바꾼 결과가 보고되었고, 고지대용 사료 작물과 알팔파 개량의 자원으로 제시되었다[8]. 균근 반응성이 높은 계통 MlS-1의 미토콘드리아 유전체에서는 바이러스·엽록체에서 넘어온 것으로 보이는 서열이 확인되었다[22]. GRAS 전사인자 유전자 52개가 동정되었고, 그중 PAT1 아과 10개가 잎·줄기·뿌리에서 발현되었다[23].

같은 MlS-1 계통에서 균근 공생이 잎의 대사체(GC-MS로 320개 대사산물)를 어떻게 바꾸는지 분석한 연구도 있다[25]. 가뭄 모의 조건에서 잎 가장자리 쪽에 리퀴리티게닌·이소리퀴리티게닌 같은 방어성 플라보노이드 경로가 더 활성화되었다[31]. 계통 분석에서 2n = 14 같은 염색체 수는 속 안에서 여러 번 독립적으로 생겼다고 보고되었다[9]."""
)
S["safety"] = ("안전성", """식품의약품안전처 「식품원료 목록」에서 잔개자리는 잎과 씨앗을 쓸 수 있는 '사용가능' 원료이며, 별도의 제한 조건은 적혀 있지 않다[1]. 이 종에 대한 사람 독성 시험, 섭취 상한, 알레르기 보고는 이번 조사에서 확인하지 못함. 알팔파에서 거론되는 카나바닌 등의 안전성 자료가 잔개자리에 해당하는지도 확인하지 못함.

지상부에는 식물성 에스트로겐인 쿠메스트롤이 들어 있다고 보고되었고, 개자리속 씨앗·싹·마이크로그린도 쿠메스트롤과 트리테르펜 사포닌의 주요 원천으로 보고되었다[2][5]. 지상부 조추출물의 총사포닌은 건물 1 g당 90.4 mg(원문 단위 mg ESE/g, 표준물질 당량)으로 측정되었다[3]. 이런 성분을 많이 먹을 때의 영향은 사람에서 확인하지 못함.

잔개자리는 광산 폐기물이나 중금속 오염 흙에서도 잘 자라며, 페루 광산 토양 재배 시험에서 지상부 아연이 1078.10 mg/kg, 뿌리 아연이 2415.73 mg/kg까지 쌓였다[13]. 수경 재배에서는 납 50 mg/L 처리에서도 자라 뿌리에 많은 금속을 쌓았고, 구리 오염 흙에서도 뿌리에 구리를 모았다[14][15]. 다만 보스니아 사문암 집단은 니켈 과축적 식물은 아니었다[12]. 따라서 길가·폐광 주변 같은 오염 의심 장소에서 야생 개체를 채취해 먹는 것은 피하는 것이 좋다[13][14]."""
)

compounds = [
 {"name": "Luteolin", "name_ko": "루테올린", "class": "플라본", "role": "marker", "part": "지상부(가수분해 후 아글리콘)",
  "content_text": "지상부 조추출물 건물 1 g당 0.37 mg으로 주 플라보노이드(가수분해 후 RP-HPLC)[3]; 크로아티아 시료 글리세롤 추출물에서도 확인(수치는 원문 표에 있어 확인하지 못함)[2]",
  "activity_ko": "루테올린은 α-글루코시데이스 억제 성분으로 알려져 추출물 활성 차이의 일부 원인으로 제시(시험관)[2]", "source": [2, 3]},
 {"name": "Myricetin", "name_ko": "미리세틴", "class": "플라보놀", "role": "bioactive", "part": "지상부(가수분해 후 아글리콘)",
  "content_text": "건물 1 g당 0.36 mg[3]; 크로아티아 시료에서는 검출되지 않음[2](시료에 따라 다름)", "activity_ko": "", "source": [2, 3]},
 {"name": "Apigenin", "name_ko": "아피제닌", "class": "플라본", "role": "bioactive", "part": "지상부",
  "content_text": "가수분해 후 RP-HPLC로 정량한 5개 플라보노이드 가운데 하나[3]; 글리세롤 추출물에서 폴리프로필렌글리콜 추출물보다 많음[2]", "activity_ko": "", "source": [2, 3]},
 {"name": "Kaempferol", "name_ko": "캠페롤", "class": "플라보놀", "role": "bioactive", "part": "지상부",
  "content_text": "가수분해 후 아글리콘으로 확인[2][3]", "activity_ko": "", "source": [2, 3]},
 {"name": "Quercetin", "name_ko": "퀘르세틴", "class": "플라보놀", "role": "bioactive", "part": "지상부",
  "content_text": "가수분해 후 아글리콘으로 확인[2][3]", "activity_ko": "", "source": [2, 3]},
 {"name": "Coumestrol", "name_ko": "쿠메스트롤", "class": "쿠메스탄(식물성 에스트로겐)", "role": "marker", "part": "지상부; 개자리속 씨앗·싹·마이크로그린",
  "content_text": "지상부 추출물에서 HPLC(254 nm)로 확인, 함량은 낮은 편[2]; 개자리속 씨앗→싹→마이크로그린 순으로 증가(종별 수치는 원문 표에 있어 확인하지 못함)[5]",
  "activity_ko": "에스트로겐 수용체 α·β 작용제로 알려진 성분(문헌 소개)[2]", "source": [2, 5]},
 {"name": "Formononetin", "name_ko": "포르모노네틴", "class": "이소플라본", "role": "bioactive", "part": "지상부·싹·마이크로그린",
  "content_text": "선행 연구에서 보고되었으나 크로아티아 지상부 시료에서는 검출되지 않음[2]; 조사한 콩과 7종 모두의 싹·마이크로그린에서 정량 가능 수준으로 검출(종별 수치 확인하지 못함)[5]",
  "activity_ko": "", "source": [2, 5]},
 {"name": "Caffeic acid", "name_ko": "카페산", "class": "히드록시신남산", "role": "bioactive", "part": "지상부",
  "content_text": "HPLC(320 nm)로 확인한 두 페놀산 가운데 하나[2]", "activity_ko": "", "source": [2]},
 {"name": "Ferulic acid", "name_ko": "페룰산", "class": "히드록시신남산", "role": "bioactive", "part": "지상부",
  "content_text": "HPLC(320 nm)로 확인, 이 종의 페놀산 첫 보고[2]", "activity_ko": "", "source": [2]},
 {"name": "Soyasaponin I", "name_ko": "소야사포닌 I", "class": "올레아난형 트리테르펜 사포닌(소야사포게놀 B 배당체)", "role": "bioactive", "part": "잎(개화 초기)",
  "content_text": "조사한 개자리속 5종(잔개자리 포함)의 잎 사포닌 추출물 모두에서 소량 검출[6]",
  "activity_ko": "잔개자리 잎 사포닌 혼합물 1000 µg/mL에서 4시간 만에 식물기생선충 성충(암컷) 전부 사멸(시험관)[6]", "source": [6]},
 {"name": "Soyasapogenol B", "name_ko": "소야사포게놀 B", "class": "트리테르펜 사포게닌", "role": "bioactive", "part": "지상부",
  "content_text": "잔개자리 사포닌은 주로 소야사포게놀과 메디카겐산 유도체라고 소개됨(문헌 인용)[2]", "activity_ko": "", "source": [2, 6]},
 {"name": "Medicagenic acid", "name_ko": "메디카겐산", "class": "트리테르펜 사포게닌", "role": "bioactive", "part": "지상부",
  "content_text": "잔개자리 사포닌의 주요 아글리콘 가운데 하나로 소개(문헌 인용)[2]; 개자리속 사포닌의 대표 아글리콘[6]", "activity_ko": "", "source": [2, 6]},
 {"name": "Liquiritigenin", "name_ko": "리퀴리티게닌", "class": "플라바논", "role": "bioactive", "part": "잎",
  "content_text": "가뭄 모의 조건에서 잎 가장자리·중앙 사이 차이가 커짐(상대 비교, 절대 함량 없음)[31]", "activity_ko": "", "source": [31]},
]

assays = [
 {"role": "literature", "compound": "Luteolin", "compound_ko": "루테올린·아피제닌·캠페롤·퀘르세틴(플라보노이드 아글리콘)", "part": "지상부(꽃·잎·줄기, 개화기)",
  "content": "수치는 원문 표에 있어 확인하지 못함; 글리세롤 최적 추출물에 루테올린·아피제닌이 폴리프로필렌글리콜 추출물보다 많았다[2]",
  "method": "HPLC-DAD(산 가수분해 후 아글리콘 정량)",
  "conditions": {"instrument": "Agilent 1200 HPLC(자동시료주입기, DAD 검출기)", "column": "Zorbax Eclipse XDB-C18(5 μm, 원문 표기 12.5 mm × 4.6 mm)",
   "mobile_phase": "A: 물:메탄올:포름산 93:5:2, B: 물:메탄올:포름산 3:95:2", "gradient": "0분 B 20%, 10분 B 40%, 35분 B 50%",
   "flow": "1.0 mL/min", "temp": "40 °C", "detection": "270 nm(아피제닌·캠페롤·루테올린·퀘르세틴), 320 nm(카페산·페룰산), UV 스펙트럼 200–500 nm로 확인",
   "injection": "", "sample_prep": "추출액 1 mL에 6 M HCl 400 μL를 넣고 끓는 물(플라본) 또는 80 °C(플라보놀·페놀산)에서 2시간 가수분해 → 여과, 메탄올로 5 mL 정용 → 0.45 μm PTFE 필터",
   "standard": "표준품 0.2 mg/mL, 머무름 시간·UV 스펙트럼 비교", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "이 종 지상부에서 가수분해 후 확인되는 주요 플라보노이드 아글리콘을 한 번에 정량하는 조건이다[2]. PMC 전문에서 조건을 옮겼으며, 검량선·검출한계·정량한계는 원문 표에 있다고 적혀 있으나 이번에 표 수치는 확인하지 못했다[2].",
  "source": [2], "url": "https://pubmed.ncbi.nlm.nih.gov/33799441/", "source_kind": "paper"},
 {"role": "literature", "compound": "Coumestrol", "compound_ko": "쿠메스트롤", "part": "지상부(꽃·잎·줄기, 개화기)",
  "content": "글리세롤·폴리프로필렌글리콜 최적 추출물 모두에서 검출, 수치는 원문 표에 있어 확인하지 못함[2]",
  "method": "HPLC-DAD",
  "conditions": {"instrument": "Agilent 1200 HPLC(DAD)", "column": "Zorbax Eclipse XDB-C18(5 μm)",
   "mobile_phase": "A: 물:아세트산 99.9:0.1, B: 아세토니트릴",
   "gradient": "0–5분 B 5→40%, 5–15분 40→15%, 15–25분 15→30%, 25–35분 30→40%, 35–45분 40→50%, 45–55분 50→95%, 55–65분 95→5%",
   "flow": "1.0 mL/min", "temp": "", "detection": "254 nm", "injection": "", "sample_prep": "플라보노이드와 같은 산 가수분해 후 여과",
   "standard": "외부 검량선(자동시료주입기로 주입량을 달리함)", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "쿠메스트롤은 개자리속에 특징적인 식물성 에스트로겐으로, 잔개자리 지상부와 개자리속 씨앗·싹에서 보고되었다[2][5]. PMC 전문에서 조건을 옮겼고 칼럼 온도·정량한계 등 표에 있는 값은 확인하지 못했다[2].",
  "source": [2, 5], "url": "https://pubmed.ncbi.nlm.nih.gov/33799441/", "source_kind": "paper"},
 {"role": "literature", "compound": "Luteolin", "compound_ko": "루테올린·미리세틴(총 플라보노이드)", "part": "지상부",
  "content": "조추출물 총 플라보노이드 건물 1 g당 1.27 mg, 루테올린 0.37 mg/g, 미리세틴 0.36 mg/g[3]",
  "method": "RP-HPLC(검증된 방법, 가수분해 추출물)",
  "conditions": {"instrument": "", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "", "injection": "",
   "sample_prep": "가수분해한 조메탄올 추출물", "standard": "캠페롤·퀘르세틴·미리세틴·아피제닌·루테올린", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "잔개자리 지상부에서 플라보놀 3종과 플라본 2종을 정량해 함량 숫자를 준 연구다[3]. 전문 확인 못함 — 초록만 보아 칼럼·이동상 등 조건은 비워 두었다[3].",
  "source": [3], "url": "https://pubmed.ncbi.nlm.nih.gov/25924534/", "source_kind": "paper"},
 {"role": "literature", "compound": "Soyasaponin I", "compound_ko": "트리테르펜 사포닌(소야사포닌 I 등)", "part": "잎(개화 초기, 동결건조)",
  "content": "개자리속 5종 잎의 조사포닌 함량은 건물의 0.60–1.62%(종별 배정은 원문 그림에 있어 확인하지 못함); 소야사포닌 I은 모든 종에서 소량[6]",
  "method": "UHPLC-ESI-MS(삼중 사중극자, 음이온 모드); 아글리콘은 GC-FID·GC-MS",
  "conditions": {"instrument": "ACQUITY UPLC(PDA) + ACQUITY TQD 삼중 사중극자 질량분석기", "column": "ACQUITY HSS C18(2.1 × 100 mm, 1.8 µm)",
   "mobile_phase": "A: 0.1% 포름산 수용액, B: 0.1% 포름산 아세토니트릴", "gradient": "0.0–0.5분 B 1%, 0.5–25.5분 B 1→50%, 이후 B 99% 2분 세척, B 1%로 1.95분 재평형",
   "flow": "0.400 mL/min", "temp": "40 °C", "detection": "ESI 음이온, 모세관 3.0 kV, 콘 40 V, 소스 140 °C, 탈용매 350 °C, 탈용매 가스 800 L/h, 콘 가스 100 L/h, m/z 150–1600 전체 주사",
   "injection": "2.5 µL", "sample_prep": "잎 가루 약 200 g을 CHCl3로 탈지(속슬레) → 80% 메탄올 환류 48시간 → C18 칼럼(40% 메탄올로 세척, 80% 메탄올로 사포닌 용출)",
   "standard": "저자들이 이전에 동정한 개자리속 사포닌·문헌 자료와 MS 단편·머무름 비교(잠정 동정)", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "개자리속의 특징 성분인 트리테르펜 사포닌 조성을 잎에서 확인하는 조건이다[6]. PMC 전문에서 조건을 옮겼으나 잠정 동정·상대 조성 분석이며 검량·회수율은 없다[6].",
  "source": [6], "url": "https://pubmed.ncbi.nlm.nih.gov/32252361/", "source_kind": "paper"},
]

d = {
 "slug": "medicago-lupulina", "name_ko": "잔개자리", "name_en": "Black medick", "scientific_name": "Medicago lupulina L.",
 "aliases": ["잔개자리씨앗", "잔개자리잎", "승앵이자리", "Black medick", "Black medic", "Hop trefoil(옛 영어명)"],
 "sections": [{"key": k, "title": t, "body": b} for k, (t, b) in S.items()],
 "compounds": compounds, "markers": [], "assays": assays, "nutrients": [], "production": [], "world": [], "gi": [], "orgs": [],
 "sources": sources,
}
sources.sort(key=lambda x: x["n"]); d["sources"]=sources
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for k,(t,b) in S.items(): print(k, len(b))
