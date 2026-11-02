import json, re
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
ACC = "2026-11-02"

SRC = [
 ("mfds", "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — Pomatomus saltatrix 1행: 원료명 '블루피쉬', 영문 'Bluefish, Tailor', 분류 수산물, 대분류 식품원료(A코드), 부위 '-', 사용조건 기준 없음, 상태 사용가능, 별명 없음; 같은 속 다른 종 행 없음; 고시형 원료 원재료 목록(KR_NOTICE) 없음 — 로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json, docs/materials/pomatomus-saltatrix/card.json", "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "식품의약품안전처", "2026-10-13"),
 ("nutr", "From Raw to Cooked: Proximate Composition, Fatty Acids and Fat-Soluble Vitamins in Bluefish (Pomatomus saltatrix) from the Black Sea. Foods 2025;15(1):55 (PMC12785910 전문 확인, 표 수치는 도구 본문에 없어 확인 못함)", "https://doi.org/10.3390/foods15010055", "Foods, PMID 41517121", ACC),
 ("elem", "Toxic and Trace Elements in Raw and Cooked Bluefish (Pomatomus saltatrix) from the Black Sea: Benefit-Risk Analysis. Foods 2026;15(1):140 (PMC12786204 전문 확인, 표 수치는 도구 본문에 없어 확인 못함)", "https://doi.org/10.3390/foods15010140", "Foods, PMID 41517206", ACC),
 ("hgnj", "Risk to consumers from mercury in bluefish (Pomatomus saltatrix) from New Jersey: Size, season and geographical effects. Environ Res 2009;109(7):803-11 (PMC4041110 전문 확인)", "https://doi.org/10.1016/j.envres.2009.07.005", "Environmental Research, PMID 19643400", ACC),
 ("hgdec", "Decadal Declines of Mercury in Adult Bluefish (1972-2011) from the Mid-Atlantic Coast of the U.S.A. Environ Sci Technol 2015;49(15):9064-72 (초록 확인)", "https://doi.org/10.1021/acs.est.5b01953", "Environmental Science & Technology, PMID 26148053", ACC),
 ("hgonto", "Ontogenetic patterns in bluefish (Pomatomus saltatrix) feeding ecology and the effect on mercury biomagnification. Environ Toxicol Chem 2011;30(6):1447-58 (초록 확인)", "https://doi.org/10.1002/etc.516", "Environmental Toxicology and Chemistry, PMID 21381087", ACC),
 ("hg19", "Mercury and selenium levels in 19 species of saltwater fish from New Jersey as a function of species, size, and season. Sci Total Environ 2011;409(8):1418-29 (초록 확인)", "https://doi.org/10.1016/j.scitotenv.2010.12.034", "Science of the Total Environment, PMID 21292311", ACC),
 ("ist", "Monitoring programme on toxic metal in bluefish (Pomatomus saltatrix), anchovy (Engraulis encrasicolus) and sardine (Sardina pilchardus) from Istanbul, Turkey: levels and estimated weekly intake. Bull Environ Contam Toxicol 2013;90(5):542-51 (초록 확인)", "https://doi.org/10.1007/s00128-012-0958-3", "Bulletin of Environmental Contamination and Toxicology, PMID 23328894", ACC),
 ("isk", "Metal Bioaccumulation in the Gill, Liver, and Muscle of Bluefish (Pomatomus saltatrix) From the Northeastern Mediterranean and Human Health Risk Assessment Associated with Their Seasonal Consumption. Arch Environ Contam Toxicol 2021;81(1):58-66 (초록 확인)", "https://doi.org/10.1007/s00244-021-00852-0", "Archives of Environmental Contamination and Toxicology, PMID 34014341", ACC),
 ("hist99", "Biogenic amine survey and organoleptic changes in fresh, stored, and temperature-abused bluefish (Pomatomus saltatrix). J Food Prot 1999;62(9):1033-7 (초록 확인)", "https://doi.org/10.4315/0362-028x-62.9.1033", "Journal of Food Protection, PMID 10492478", ACC),
 ("hist01", "Growth and histamine formation of Morganella morganii in determining the safety and quality of inoculated and uninoculated bluefish (Pomatomus saltatrix). J Food Prot 2001;64(12):2015-9 (초록 확인)", "https://doi.org/10.4315/0362-028x-64.12.2015", "Journal of Food Protection, PMID 11770632", ACC),
 ("jama", "Bluefish-associated scombroid poisoning. An example of the expanding spectrum of food poisoning from seafood. JAMA 1987;258(23):3409-10 (초록 확인)", "https://doi.org/10.1001/jama.258.23.3409", "JAMA, PMID 3682140", ACC),
 ("ct85", "Presence of Histamine in the Bluefish, Pomatomus saltatrix. J Food Prot 1985;48(2):166-168 (초록 확인)", "https://doi.org/10.4315/0362-028X-48.2.166", "Journal of Food Protection, PMID 30934524", ACC),
 ("pcbcook", "Levels of polychlorinated biphenyls and pesticides in bluefish before and after cooking. J Assoc Off Anal Chem 1989;72(3):501-3 (초록 확인)", "https://pubmed.ncbi.nlm.nih.gov/2501293/", "Journal of the Association of Official Analytical Chemists, PMID 2501293", ACC),
 ("pcbcat", "Tissue deposition of polychlorinated biphenyls in cats fed Atlantic Ocean bluefish. Cornell Vet 1991;81(3):259-65 (초록 확인)", "https://pubmed.ncbi.nlm.nih.gov/1831741/", "The Cornell Veterinarian, PMID 1831741", ACC),
 ("chlord", "Chlordane contamination in selected estuarine and coastal marine finfish and shellfish of New Jersey, USA. Environ Pollut 1996;94(1):75-81 (초록 확인)", "https://doi.org/10.1016/s0269-7491(96)00051-6", "Environmental Pollution, PMID 15093520", ACC),
 ("pbde", "Polybrominated diphenyl ether congeners in the young-of-the-year bluefish, Pomatomus saltatrix, from several nursery habitats along the US Atlantic coastline. Mar Pollut Bull 2013;77(1-2):237-50 (초록 확인)", "https://doi.org/10.1016/j.marpolbul.2013.09.051", "Marine Pollution Bulletin, PMID 24449924", ACC),
 ("yoy", "Young of the year bluefish (Pomatomus saltatrix) as a bioindicator of estuarine health: Establishing a new baseline for persistent organic pollutants after Hurricane Sandy for selected estuaries in New Jersey and New York. Mar Pollut Bull 2016;107(2):422-31 (초록 확인)", "https://doi.org/10.1016/j.marpolbul.2016.03.019", "Marine Pollution Bulletin, PMID 27039958", ACC),
 ("hered", "Secondary contact and asymmetrical gene flow in a cosmopolitan marine fish across the Benguela upwelling zone. Heredity 2016;117(5):307-315 (초록 확인)", "https://doi.org/10.1038/hdy.2016.51", "Heredity, PMID 27436525", ACC),
 ("cytb", "Climate change and oceanic barriers: genetic differentiation in Pomatomus saltatrix (Pisces: Pomatomidae) in the North Atlantic Ocean and the Mediterranean Sea. J Fish Biol 2010;77(8):1993-8 (초록 확인)", "https://doi.org/10.1111/j.1095-8649.2010.02774.x", "Journal of Fish Biology, PMID 21078102", ACC),
 ("msat", "Isolation and characterization of polymorphic tetranucleotide microsatellite loci in the pelagic perciform fish Pomatomus saltatrix (Linnaeus, 1766) from South Africa. Mol Ecol Resour 2008;8(5):1065-7 (초록 확인)", "https://doi.org/10.1111/j.1755-0998.2008.02156.x", "Molecular Ecology Resources, PMID 21585973", ACC),
 ("repro", "Reduced exploitation is associated with an altered sex ratio and larger length at maturity in southwest Pacific (east Australian) Pomatomus saltatrix. Mar Environ Res 2019;147:72-79 (초록 확인)", "https://doi.org/10.1016/j.marenvres.2019.02.012", "Marine Environmental Research, PMID 31000357", ACC),
 ("brazil", "Local ecological knowledge and scientific data reveal overexploitation by multigear artisanal fisheries in the southwestern Atlantic. PLoS One 2014;9(10):e110332 (초록 확인)", "https://doi.org/10.1371/journal.pone.0110332", "PLoS One, PMID 25333661", ACC),
 ("hb", "Overproduction of alpha chains provides a proton-insensitive component to the bluefish hemoglobin system. J Biol Chem 2005;280(49):40509-14 (초록 확인)", "https://doi.org/10.1074/jbc.M505353200", "Journal of Biological Chemistry, PMID 16166086", ACC),
 ("teeth", "Structure, attachment, replacement and growth of teeth in bluefish, Pomatomus saltatrix (Linnaeus, 1776), a teleost with deeply socketed teeth. Zoology (Jena) 2005;108(4):317-27 (초록 확인)", "https://doi.org/10.1016/j.zool.2005.09.004", "Zoology, PMID 16351980", ACC),
 ("tryp", "Trypsin from the pyloric caeca of bluefish (Pomatomus saltatrix). Comp Biochem Physiol B 2007;148(4):382-9 (초록 확인)", "https://doi.org/10.1016/j.cbpb.2007.07.004", "Comparative Biochemistry and Physiology Part B, PMID 17707670", ACC),
 ("pome", "Pomegranate (Punica granatum) peel fractions obtained by supercritical CO2 increase oxidative and colour stability of bluefish (Pomatomus saltatrix) patties treated by UV-C irradiation. Food Chem 2021;362:130159 (초록 확인)", "https://doi.org/10.1016/j.foodchem.2021.130159", "Food Chemistry, PMID 34167065", ACC),
 ("map", "Attenuation of Microbial Growth on Modified Atmosphere-Packaged Fish. J Food Prot 1983;46(7):610-613 (초록 확인)", "https://doi.org/10.4315/0362-028X-46.7.610", "Journal of Food Protection, PMID 30921938", ACC),
 ("phil", "Philometra saltatrix (Nematoda: Philometridae) in the ovary of the bluefish, Pomatomus saltatrix (Linnaeus, 1766), off the coast of the state of Rio de Janeiro, Brazil. J Helminthol 2017;92(2):210-215 (초록 확인)", "https://doi.org/10.1017/S0022149X17000335", "Journal of Helminthology, PMID 28397630", ACC),
 ("hyst", "Morphological and molecular characterization of Hysterothylacium spp. parasitizing Pomatomus saltatrix and Pagrus pagrus of the State of São Paulo, Brazil. An Acad Bras Cienc 2023;95(1):e20211046 (초록 확인)", "https://doi.org/10.1590/0001-3765202320211046", "Anais da Academia Brasileira de Ciências, PMID 36790269", ACC),
 ("anis", "Molecular characterization of anisakid nematode larvae from 13 species of fish from Western Australia. Int J Food Microbiol 2012;161(3):247-53 (초록 확인)", "https://doi.org/10.1016/j.ijfoodmicro.2012.12.012", "International Journal of Food Microbiology, PMID 23353682", ACC),
 ("mp", "Microplastics in commercially important marine fish from Giresun Province, Türkiye: A baseline assessment of tissue distribution, polymer composition, spatial patterns, and potential environmental and ecological risk. Environ Res 2026;310(Pt 1):125964 (초록 확인)", "https://doi.org/10.1016/j.envres.2026.125964", "Environmental Research, PMID 42892431", ACC),
 ("micro", "First integrated characterization of Microcotyle pomatomi Goto, 1899 (Polyopisthocotylea: Microcotylidae) from the Bluefish Pomatomus saltatrix (Linnaeus) off Algeria, Western Mediterranean, with resolution of its historical synonymy. Syst Parasitol 2026;103(5) (초록 확인)", "https://doi.org/10.1007/s11230-026-10297-5", "Systematic Parasitology, PMID 42584736", ACC),
 ("parv", "The structure and evolution of parvalbumins. I. Amino acid compositional studies of parvalbumins from four perciform species. J Mol Evol 1975;5(2):103-16 (초록 확인)", "https://doi.org/10.1007/BF01732515", "Journal of Molecular Evolution, PMID 1159797", ACC),
 ("morph", "Population Structure and Spatial Connectivity Inferred from Spatial Phenotypic Differentiation of the Bluefish (Teleostei: Pomatomidae) Along the Southeastern-Southern Brazilian Coast Using Landmark-Based Truss Network Morphometrics. Biology 2026;15(20):1883 (초록 확인)", "https://doi.org/10.3390/biology15201883", "Biology, PMID 42939484", ACC),
 ("tailor", "The influence of ontogenetic diet variation on consumption rate estimates: a marine example. Sci Rep 2018;8(1):10725 (초록 확인)", "https://doi.org/10.1038/s41598-018-28479-7", "Scientific Reports, PMID 30013084", ACC),
]
N = {k: i + 1 for i, (k, *_) in enumerate(SRC)}


def r(text):
    return re.sub(r"\{(\w+(?:,\w+)*)\}", lambda m: "[" + ", ".join(str(N[k]) for k in m.group(1).split(",")) + "]", text)


SECTIONS = [
 ("overview", "한눈에 보기",
  "블루피쉬(Pomatomus saltatrix)는 식약처 「식품원료 목록」에 '블루피쉬'(영문 Bluefish, Tailor)라는 원료명으로 올라 있는 수산물이다{mfds}. 이 목록에서 블루피쉬는 학명 1행뿐이며 상태는 '사용가능', 부위 칸은 '-'이고 따로 정한 사용 조건이나 별명은 없다{mfds}. 건강기능식품 고시형 원료의 원재료 목록에는 없으므로 식약처가 정한 지표성분도 없다{mfds}.\n\n"
  "블루피쉬는 온대·아열대 바다에 널리 사는 빠르게 자라는 표층성 포식어로, 흑해에서는 전통 제철 생선으로 굽기·튀기기·훈제 등으로 먹는다{nutr}. 흑해산 시료에서 조리한 살의 EPA+DHA는 100 g(습중량)당 743–2,223 mg으로 보고되었다{nutr}. 한편 몸집이 클수록 살의 수은이 높아지는 종이어서, 미국 뉴저지 연구는 가랑이체장 50 cm가 넘는 개체를 임신부·어린이가 피하라고 제안했다{hgnj}. 상온에 두면 히스타민이 쌓여 히스타민(스콤브로이드) 식중독을 일으킨 사례도 있다{jama,hist99}. 국가표준식품성분표의 블루피쉬 성분값과 국내 어획·수입 통계는 이번 조사에서 확인하지 못함."),
 ("history", "이용·연구 역사",
  "블루피쉬 아가미에 붙는 기생충 Microcotyle pomatomi는 1899년 미국 로드아일랜드 뉴포트에서 잡힌 블루피쉬를 바탕으로 처음 기재되었다{micro}. 1972년에는 미국 노스캐롤라이나 앞바다 성어의 살 수은이 측정되었고, 2011년 재측정에서는 43% 낮아져 10년에 약 10%씩 줄어든 것으로 계산되었다{hgdec}.\n\n"
  "1980년대에는 고등어과가 아닌 블루피쉬도 히스타민 식중독의 원인이 된다는 보고가 이어졌다{ct85,jama}. 미국 코네티컷주 시판 필레 조사에서는 6.5%가 넘는 필레가 부패를 뜻하는 수준의 히스타민을 보였다{ct85}. 1987년 매사추세츠주 보고는 학회 식사 뒤 5명이 발병한 사건의 원인으로 잘못 보관·해동한 블루피쉬를 지목했다{jama}. 1986–1991년 뉴저지 조사에서는 블루피쉬 등 어패류의 클로르데인이 습중량 5–2,150 ppb 범위로 측정되었다{chlord}. 1989년 미국 식품의약국 연구진은 블루피쉬 필레를 구워 PCB와 농약 잔류량의 변화를 비교했다{pcbcook}. 2000년대 이후에는 어린 블루피쉬를 하구 오염 지표종으로 쓰는 연구가 늘었다{pbde,yoy}. 2025–2026년에는 흑해산 블루피쉬의 조리법별 영양 성분과 원소 위해도 평가가 나왔다{nutr,elem}."),
 ("biology", "어종·생태·번식",
  "블루피쉬는 날렵한 몸, 날카로운 원뿔꼴 이빨을 지닌 표층성 포식어로 느슨한 큰 무리를 이루어 다니며 다른 물고기를 잡아먹는다{nutr}. 흑해 집단은 봄에 지중해에서 에게해를 거쳐 흑해로 산란 회유하고 이른 가을에 남쪽으로 돌아간다{nutr}. 북미 대서양 집단의 대부분은 여름을 북쪽에서, 겨울을 플로리다와 걸프 스트림 부근에서 보내는 회유성이다{hgnj}.\n\n"
  "이 종은 세계에 7개의 주요 집단이 있다고 소개된다{repro}. 호주 동부 집단은 한 산란기에 여러 번 알을 낳으며, 한 번의 산란 수는 99,488–1,424,425개로 추정되었다{repro}. 같은 연구에서 50% 성숙 체장은 수컷 30.2 cm, 암컷 31.5 cm(가랑이체장)로 40년 전보다 4 cm 컸고, 성비는 암컷 1.58 대 수컷 1로 바뀌어 있었다{repro}. 미국 내러갠섯만 조사에서 0세어는 저서·부유 먹이를 함께 먹었지만 1세 이상은 거의 부유성 먹이 물고기만 먹었다{hgonto}. 입의 이빨은 뼈에 깊이 박혀 붙어 있고 아래턱 15–31개, 위턱 앞부분 15–39개로 자라면서 늘어난다{teeth}. 혈액에서는 α사슬이 과잉 생산되는데, 연구진은 이것이 낮은 pH에서도 산소를 나르는 적응이라고 해석했다{hb}. 국내 연안의 출현 기록은 이번 조사에서 공식 자료로 확인하지 못함."),
 ("related_species", "관련 종·이름",
  "식약처 「식품원료 목록」의 영문명 칸에는 'Bluefish, Tailor' 두 이름이 함께 적혀 있다{mfds}. 호주 연구에서는 같은 종을 tailor라는 이름으로 부르며 생물에너지 모형을 만들었다{tailor}. 식약처 목록에는 Pomatomus 속의 다른 종이 올라 있지 않다{mfds}. 블루피쉬의 이빨 교체 방식은 꼬치고기류·고등어류와 공통점이 있어, 연구진은 이 종이 이들과 더 가깝다는 해석을 지지한다고 보았다{teeth}.\n\n"
  "국립생물자원관 국가생물종목록의 국문 표준명은 이번 조사에서 확인하지 못함. 따라서 이 백과는 식약처 원료명 '블루피쉬'를 쓰고, 다른 어종의 국문 이름과 섞어 쓰지 않는다{mfds}. 근육에서 분리한 파브알부민은 '빠른'·'느린' 두 동형으로 나뉘었고 겉보기 분자량은 10,400–14,000 범위였다{parv}."),
 ("cultivation", "어획·자원",
  "블루피쉬는 상업 어업과 유어 낚시의 대상이며 양식 생산 자료는 이번 조사에서 확인하지 못함. 불가리아 흑해 연안에서는 어획량이 유럽청어류(스프랫) 다음 2위인 주요 어종이다{nutr,elem}. 미국 뉴저지에서는 유어 낚시 대회의 주요 대상 어종이고, 이 지역 슈퍼마켓·생선가게의 80% 넘는 곳에서 판매된다고 보고되었다{hgnj}.\n\n"
  "자원 감소 사례도 있다{brazil}. 브라질 남동부에서 어민 214명을 면담한 결과 지난 60년 동안 블루피쉬의 풍도가 크게 줄었다고 답했고, 16년간의 양륙 자료도 이를 뒷받침했다{brazil}. 반대로 호주 동부에서는 관리 강화 뒤 성숙 체장이 커지고 성비가 바뀐 것이 확인되어, 연구진은 생식 생물학을 계속 감시해야 한다고 했다{repro}. 미국 뉴저지에서는 큰 개체가 봄에만 연안에서 잡히고 이후 먼바다로 나가 계절에 따라 잡히는 크기가 달랐다{hgnj}. 세계 어획량(FAO 통계)은 이번 조사에서 확인하지 못함."),
 ("processing", "가공·저장·품질",
  "흑해 연안에서는 블루피쉬를 생으로 팔거나 굽기·튀기기·훈제·절임·통조림으로 가공한다{nutr}. 실험에서 조리하면 수분이 7–18% 줄고 총지질은 26–80% 늘었다{nutr}. 해바라기유로 팬에 튀기면 EPA는 약 25.2%, DHA는 약 20.3%(습중량 100 g당 기준) 줄었다{nutr}. 훈제는 비타민 E를 대체로 지켰지만 그릴 구이에서는 비타민 E 손실이 컸고 아스타잔틴은 검출되지 않았다{nutr}. 연구진은 굽기와 훈제가 긴사슬 n-3 지방산과 미량영양소를 지키는 데 유리하다고 결론지었다{nutr}.\n\n"
  "저장 중 품질 관리도 중요하다{hist99}. 5·10·15 °C에 둔 필레에서 히스타민이 생겼고 15 °C에서는 2,200 ppm까지 올랐다{hist99}. 이산화탄소 기체치환포장은 일반 포장보다 저장 안정성을 45–55% 늘렸다{map}. 석류 껍질 초임계 추출 분획은 UV-C 처리한 블루피쉬 패티의 지질 산화를 합성 산화방지제 BHT만큼 막았다(4 °C, 9일){pome}. 유문수에서 분리한 트립신은 분자량 28 kDa, 최적 pH 9.5·55 °C였다{tryp}."),
 ("genetics", "유전 정보",
  "블루피쉬의 전장 유전체나 미토콘드리아 전장 서열 논문은 이번 PubMed 검색에서 확인하지 못함. 미토콘드리아 시토크롬 b 부분 서열 분석에서는 북대서양 서쪽과 동쪽 집단이 완전히 갈라져 있었고, 동쪽 집단은 지중해와 이어져 있었다{cytb}. 남아프리카 동해안 개체 100마리로 개발한 4염기 반복 미세부수체 8개는 좌위당 대립유전자 18–37개(평균 24개), 관찰 이형접합도 0.79였다{msat}.\n\n"
  "남아프리카·앙골라·세네갈·포르투갈 8개 지점을 비교한 연구는 시토크롬 b, 인트론 AM2B1, 미세부수체 15개를 썼다{hered}. 남아프리카 개체와 다른 지점 사이 유전 분화(FST)는 0.15–0.20으로 컸고, 남아프리카에서 앙골라 쪽으로만 유전자가 흐르는 2차 접촉이 확인되었다{hered}. 브라질 남동부 3개 지점 성어 109마리의 형태계측에서는 지점별 재분류 정확도가 87.2%였지만, 연구진은 형태만으로 계군 경계를 정할 수 없다고 했다{morph}."),
 ("safety", "안전성",
  "수은은 크기와 함께 늘어난다{hgnj,hgonto}. 뉴저지 206마리의 살 총수은은 평균 0.35±0.02 ppm(습중량)이었고 41%가 0.3 ppm, 20%가 0.5 ppm, 4%가 1 ppm을 넘었다{hgnj}. 내러갠섯만에서는 전장 30 cm 넘는 개체가 꾸준히 미국 환경보호청 기준 0.3 ppm을 넘었다{hgonto}. 이스탄불 조사에서도 일부 달의 작은·중간 크기 블루피쉬 수은으로 계산한 주간 섭취량이 권고 한도를 넘었다{ist}. 반면 지중해 이스켄데룬만 시료의 살에서는 수은과 카드뮴이 검출되지 않았다{isk}. 흑해산 날것·조리 시료의 카드뮴·납은 EU 최대기준(0.050·0.30 mg/kg 습중량) 아래였고 위해지수(THQ)도 모두 1 미만이었다{elem}.\n\n"
  "미국 대서양 연안 블루피쉬는 PCB 농도가 상당하며, 블루피쉬만 86일 먹인 고양이의 지방 PCB 중앙값은 48 ppm(건중량)으로 대조군 0.61 ppm보다 높았다{pcbcat}. 구운 필레는 껍질과 기름을 버렸을 때 PCB가 평균 27% 낮았다{pcbcook}. 히스타민은 신선 도매품에서 평균 39 ppm이었으나 온도 관리가 잘못되면 미국 식품의약국 권고 50 ppm을 관능 거부보다 먼저 넘었다{hist99}. 브라질산 암컷의 난소 선충 감염률은 48.7%였고, 브라질 상파울루 시료에서는 Hysterothylacium 유충, 호주 서부 시료에서는 고래회충과(Anisakidae) 유충이 확인되었다{phil,hyst,anis}. 흑해 기레순산 살의 미세플라스틱은 41.3±19.3개/g(건중량)으로 7종 가운데 가장 많았다{mp}. 이 종의 알레르기 자료와 식약처 잔류 기준 적용 사례는 확인하지 못함."),
]

COMP = [
 ("Eicosapentaenoic acid", "에이코사펜타엔산(EPA)", "n-3 고도불포화지방산", "nutrient", "살(가식부)", "조리 시료 EPA+DHA 743–2,223 mg/100 g 습중량, 팬 튀김에서 EPA 약 25.2% 감소{nutr}", "긴사슬 n-3 지방산으로 생선의 영양 가치 평가와 위해-편익 비 계산의 기준이 되었다{nutr,elem}", ["nutr", "elem"]),
 ("Docosahexaenoic acid", "도코사헥사엔산(DHA)", "n-3 고도불포화지방산", "nutrient", "살(가식부)", "조리 시료 EPA+DHA 743–2,223 mg/100 g 습중량, 팬 튀김에서 DHA 약 20.3% 감소{nutr}", "굽기·훈제 뒤 비율이 높아졌으나 연구진은 수분 손실에 따른 농축 효과로 해석했다{nutr}", ["nutr"]),
 ("alpha-Tocopherol", "알파-토코페롤(비타민 E)", "지용성 비타민", "nutrient", "살", "날것 1.18 mg/g 지질(27.1 mg/100 g 건중량), 팬 튀김 뒤 0.56 mg/g 지질(22.9 mg/100 g 건중량){nutr}", "훈제 시료 100 g이 성인 권장량의 160% 넘는 양을 준다고 계산되었다{nutr}", ["nutr"]),
 ("Vitamin D", "비타민 D", "지용성 비타민", "nutrient", "살", "훈제 시료 100 g이 권장량의 40–50% 제공(원문 아래첨자 표기·절대값은 확인 못함){nutr}", "조리 중 비교적 안정했다{nutr}", ["nutr"]),
 ("Retinol", "레티놀(비타민 A)", "지용성 비타민", "nutrient", "살", "그릴 구이에서 약 57% 손실(절대값은 확인 못함){nutr}", "열과 산소에 약해 조리법에 따라 크게 줄었다{nutr}", ["nutr"]),
 ("Astaxanthin", "아스타잔틴", "카로티노이드 색소", "bioactive", "살", "그릴 구이 시료에서 불검출, 튀김·훈제에서 지질 기준 약 65–70% 유지{nutr}", "산화방지 색소로 조리 손실 지표로 함께 분석되었다{nutr}", ["nutr"]),
 ("Cholesterol", "콜레스테롤", "스테롤", "nutrient", "살", "튀김·훈제에서 지질 기준 약 15–28% 감소(절대값은 확인 못함){nutr}", "지용성 비타민과 같은 HPLC 조건으로 동시 분석되었다{nutr}", ["nutr"]),
 ("Histamine", "히스타민", "생체아민(부패 지표·식중독 원인)", "marker", "필레", "신선 도매품 <1–99 ppm(평균 39 ppm), 15 °C 저장 최고 2,200 ppm{hist99}", "히스타민(스콤브로이드) 식중독 원인 물질이며 신선도 지표로 쓰인다{hist99,jama}", ["hist99", "hist01", "jama", "ct85"]),
 ("Mercury", "수은(총수은)", "중금속 오염물질", "marker", "살", "뉴저지 206마리 평균 0.35±0.02 ppm 습중량{hgnj}; 0세어 0.041, 1세 이상 0.254 ppm 습중량{hgonto}", "대부분 메틸수은으로 존재한다고 보며 크기·계절에 따라 달라 섭취 권고의 근거가 된다{hgnj}", ["hgnj", "hgonto", "hgdec", "hg19"]),
 ("Selenium", "셀레늄", "필수 미량원소", "nutrient", "살", "뉴저지 206마리 평균 0.37±0.01 ppm 습중량{hgnj}", "수은 독성을 줄이는 효과가 보고되어 함께 측정되었으나 크기·계절과 관계가 없었다{hgnj}", ["hgnj"]),
 ("Polychlorinated biphenyls", "폴리염화비페닐(PCB)", "잔류성 유기오염물질", "marker", "필레", "조리 전 평균 2.5 ppm(Aroclor 1254 기준), 조리 뒤 2.7 ppm{pcbcook}", "지질이 많은 블루피쉬에 쌓여 섭취 위해와 하구 오염 감시 지표로 쓰인다{pcbcook,yoy}", ["pcbcook", "pcbcat", "yoy"]),
 ("2,2',4,4'-Tetrabromodiphenyl ether", "BDE-47(브롬화 난연제)", "잔류성 유기오염물질", "marker", "어린 개체 전어체", "가장 자주 검출된 PBDE 동족체; 뉴어크만 ΣPBDE 평균 56.6±30.8 ng/g 습중량{pbde}", "산업·도시 지역 하구 오염을 반영하는 지표로 쓰였다{pbde}", ["pbde"]),
 ("Zinc", "아연", "필수 미량원소", "nutrient", "살", "이스켄데룬만 살 6.27–13.59(초록에 단위 표기 없음){isk}", "흑해산 조리 시료에서 철·크롬과 함께 필수 원소 공급원으로 평가되었다{elem}", ["isk", "elem"]),
 ("Parvalbumin", "파브알부민", "근육 칼슘결합 단백질", "bioactive", "흰 근육", "'빠른'·'느린' 두 동형, 겉보기 분자량 10,400–14,000{parv}", "근육 단백질의 진화 연구 대상으로 분리되었으며, 이 종의 알레르기 자료는 확인 못함{parv}", ["parv"]),
]

EMPTY = {k: "" for k in ["instrument", "column", "mobile_phase", "gradient", "flow", "temp", "detection", "injection", "sample_prep", "standard", "linearity", "lod", "loq", "recovery"]}

ASSAYS = [
 {"role": "literature", "compound": "Fatty acid methyl esters (EPA, DHA etc.)", "compound_ko": "지방산 조성(EPA·DHA 포함)", "part": "살(머리·내장 제거 근육)",
  "content": r("조리 시료 EPA+DHA 743–2,223 mg/100 g 습중량(훈제 2,223, 그릴 1,478, 팬 튀김 743){nutr}"), "method": "GC-MS(이온트랩)",
  "conditions": dict(EMPTY, instrument="Thermo FOCUS 가스크로마토그래프 + PolarisQ 이온트랩 질량분석기", column="Trace TR-FAME 모세관 칼럼 60 m × 0.25 mm × 0.25 μm", mobile_phase="운반 기체 헬륨", gradient="100 °C 1분 → 10 °C/분 160 °C → 5 °C/분 215 °C(6분 유지) → 5 °C/분 230 °C(5분 유지)", flow="1.2 mL/min", detection="질량분석(이온트랩)", injection="1 μL, split 10:1", sample_prep="Bligh–Dyer 변법(CHCl3/CH3OH 1:2 → 1:1 → CHCl3 순차 추출) → 5% H2SO4–메탄올 70 °C 메틸화", standard="Supelco 37 성분 FAME 혼합물·PUFA No. 3(멘헤이든유)과 머무름 시간 비교; mg/100 g 환산은 어류 지방산 환산계수(XFA) 사용"),
  "rationale": r("긴사슬 n-3 지방산(EPA·DHA)은 블루피쉬 영양 가치와 조리 손실, 원소 위해-편익 비 계산의 기준으로 쓰였다{nutr,elem}. 전문(Methods) 확인 — 검출·정량한계·회수율은 본문에 없음{nutr}."),
  "source": ["nutr", "elem"], "url": "https://doi.org/10.3390/foods15010055", "source_kind": "paper"},
 {"role": "literature", "compound": "Toxic and essential elements (Cd, Pb, Ni, Cr, Mn, Fe, Cu, Zn)", "compound_ko": "유해·필수 원소", "part": "가식부 살",
  "content": r("Cd·Pb는 날것·조리 시료 모두 EU 최대기준(Cd 0.050, Pb 0.30 mg/kg 습중량) 이하, 원소별 수치는 표에 있어 확인 못함{elem}"), "method": "ICP-OES",
  "conditions": dict(EMPTY, instrument="ICP-OES Optima 8000(PerkinElmer), 축 방향 관측", mobile_phase="플라스마 기체 10 L/min, 보조 기체 0.7 L/min, 분무 기체 0.2 L/min", sample_prep="시료 약 1 g을 HNO3(65%):H2O2(30%) 8:2로 마이크로파 분해(MARS 6, 최고 210 °C·800 psi·1050 W) → 25 mL 정용", standard="인증표준물질 DORM-2(돔발상어 근육)로 정확도 확인", recovery="91.5–107.3%(DORM-2)"),
  "rationale": r("카드뮴·납·니켈은 섭취 위해 평가(THQ·HI·발암 위해) 대상이고 철·아연·구리 등은 영양 원소여서 함께 정량했다{elem}. 전문 확인 — 원소별 파장·검출한계는 보충 표에 있어 확인 못함{elem}."),
  "source": ["elem"], "url": "https://doi.org/10.3390/foods15010140", "source_kind": "paper"},
 {"role": "literature", "compound": "Total mercury", "compound_ko": "총수은", "part": "살(근육)",
  "content": r("206마리 평균 0.35±0.02 ppm 습중량, 0.3 ppm 초과 41%{hgnj}"), "method": "냉증기 원자흡광(CV-AAS)",
  "conditions": dict(EMPTY, instrument="Perkin Elmer FIMS-100 수은 분석기", detection="냉증기 원자흡광", sample_prep="습중량 2 g을 초순수 질산으로 마이크로파 분해(CEM MD 2000, 3단계 각 10분, 50·100·150 lb/in²) → 탈이온수 100 mL 희석", standard="DORM-2 인증 돔발상어 조직으로 검량 확인(회수율 90–110% 허용)", lod="기기 검출수준 0.2 ng/g", loq="매트릭스 정량수준 0.002 μg/g", recovery="첨가 회수율 85–115% 허용, 벗어난 배치 없음"),
  "rationale": r("살의 수은은 대부분 메틸수은으로 보며 크기와 함께 늘어 섭취 권고(가랑이체장 50 cm 이상 회피)의 근거가 되었다{hgnj}. 전문(Methods) 확인{hgnj}."),
  "source": ["hgnj"], "url": "https://doi.org/10.1016/j.envres.2009.07.005", "source_kind": "paper"},
 {"role": "literature", "compound": "Histamine, putrescine, cadaverine", "compound_ko": "히스타민·푸트레신·카다베린", "part": "필레",
  "content": r("신선 도매품 히스타민 <1–99 ppm(평균 39 ppm), 15 °C 저장 최고 2,200 ppm{hist99}"), "method": "HPLC(형광 검출)",
  "conditions": dict(EMPTY),
  "rationale": r("히스타민은 히스타민 식중독 원인 물질이고 미국 식품의약국 권고 50 ppm과 비교되는 부패 지표다{hist99}. 2001년 후속 연구는 HPLC·형광검출로 히스타민을 정량했다{hist01}. 전문 확인 못함 — 조건 칸은 비워 둠."),
  "source": ["hist99", "hist01"], "url": "https://doi.org/10.4315/0362-028x-62.9.1033", "source_kind": "paper"},
]


def main():
    d = {
        "slug": "pomatomus-saltatrix",
        "name_ko": "블루피쉬",
        "name_en": "Bluefish",
        "scientific_name": "Pomatomus saltatrix (Linnaeus, 1766)",
        "aliases": ["블루피쉬", "Bluefish", "Tailor"],
        "sections": [{"key": k, "title": t, "body": r(b)} for k, t, b in SECTIONS],
        "compounds": [{"name": n, "name_ko": nk, "class": c, "role": ro, "part": p, "content_text": r(ct), "activity_ko": r(a), "source": [N[s] for s in src]} for n, nk, c, ro, p, ct, a, src in COMP],
        "markers": [],
        "assays": [dict(a, source=[N[s] for s in a["source"]]) for a in ASSAYS],
        "nutrients": [],
        "production": [],
        "world": [],
        "gi": [],
        "orgs": [],
        "sources": [{"n": N[k], "title": t, "url": u, "publisher": p, "accessed": ac} for k, t, u, p, ac in SRC],
    }
    (HERE / "dossier.json").write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
    for s in d["sections"]:
        print(s["key"], len(s["body"]))


main()
