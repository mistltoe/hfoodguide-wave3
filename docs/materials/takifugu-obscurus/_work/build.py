import json, pathlib
OUT = pathlib.Path("/home/user/hfoodguide-wave3/docs/materials/takifugu-obscurus/dossier.json")
A = "2026-11-02"
WS = " — WebSearch 검색 결과 요약으로만 확인, 원문은 이 환경에서 열지 못함"
S = [
 (1, "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — Takifugu obscurus 행: 황복(이명 강복, 영문 Mefugu(일명), 수산물, 부위 '-', 사용가능), 황복알·황복내장(같은 학명, 사용불가; 원자료의 부위 칸은 각각 '균핵'·'어린순'으로 적혀 있음). data/raw/mfds_rawmtrl/I1020_20261013.json, docs/materials/takifugu-obscurus/card.json", "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "식품의약품안전처", "2026-10-13"),
 (2, "Accumulation and Elimination of Tetrodotoxin in the Pufferfish Takifugu obscurus by Dietary Administration of the Wild Toxic Gastropod Nassarius semiplicata. Toxins 2020;12(5):278 (PMC 전문 확인)", "https://doi.org/10.3390/toxins12050278", "Toxins (MDPI), PubMed 32344936, PMC7290894", A),
 (3, "In Vivo Detection of Tetrodotoxin in Takifugu obscurus Based on Solid-Phase Microextraction Coupled with Ultrahigh-Performance Liquid Chromatography-Tandem Mass Spectrometry. Molecules 2022;27(18):6122 (PMC 전문 확인)", "https://doi.org/10.3390/molecules27186122", "Molecules (MDPI), PubMed 36144854, PMC9502389", A),
 (4, "Comprehensive Insights of Biochemical and Sensory Characterization in Takifugu obscurus by Environmental Modulation. Foods 2025;14(8):1386 (PMC 전문 확인)", "https://doi.org/10.3390/foods14081386", "Foods (MDPI), PubMed 40282787, PMC12026688", A),
 (5, "Chromosomal-level assembly of Takifugu obscurus (Abe, 1949) genome using third-generation DNA sequencing and Hi-C analysis. Mol Ecol Resour 2020;20(2):520-530 (초록 확인)", "https://doi.org/10.1111/1755-0998.13132", "Molecular Ecology Resources, PubMed 31887246", A),
 (6, "Complete mitochondrial genome of the anadromous river pufferfish, Takifugu obscurus (Tetraodontiformes: Tetraodontidae). Mitochondrial DNA 2014;25(1):46-7 (초록 확인)", "https://doi.org/10.3109/19401736.2013.782018", "Mitochondrial DNA, PubMed 23627314", A),
 (7, "Salinity changes in the anadromous river pufferfish, Takifugu obscurus, mediate gene regulation. Fish Physiol Biochem 2014;40(1):205-19 (초록 확인)", "https://doi.org/10.1007/s10695-013-9837-z", "Fish Physiology and Biochemistry, PubMed 23907526", A),
 (8, "Molecular mechanisms of kidney-mediated salinity adaptation in Takifugu obscurus, T. rubripes and their hybrid offspring. Comp Biochem Physiol D 2025;56:101659 (초록 확인)", "https://doi.org/10.1016/j.cbd.2025.101659", "Comparative Biochemistry and Physiology Part D, PubMed 41124711", A),
 (9, "Transcriptome profiling revealed the growth superiority of hybrid pufferfish derived from Takifugu obscurus ♀ × Takifugu rubripes ♂. Comp Biochem Physiol D 2021;40:100912 (초록 확인)", "https://doi.org/10.1016/j.cbd.2021.100912", "Comparative Biochemistry and Physiology Part D, PubMed 34601229", A),
 (10, "Various Characteristics of Hybrid between River Puffer, Takifugu obscurus and Tiger Puffer, T. rubripes, and Their Hybrid Triploid. Dev Reprod 2017;21(2):181-191 (초록 확인)", "https://doi.org/10.12717/DR.2017.21.2.181", "Development & Reproduction, PubMed 28785739, PMC5532310", A),
 (11, "Changing Salinity Affects Hematological and Histological Response in Hybrids and Hybrid Triploids between River Puffer, Takifugu obscurus and Tiger Puffer, T. rubripes. Dev Reprod 2019;23(3):239-253 (초록 확인)", "https://doi.org/10.12717/DR.2019.23.3.239", "Development & Reproduction, PubMed 31660451, PMC6812970", A),
 (12, "Genetic Differences in Natural and Cultured River Pufferfish Populations by PCR Analysis. Dev Reprod 2020;24(4):327-336 (초록 확인)", "https://doi.org/10.12717/DR.2020.24.4.327", "Development & Reproduction, PubMed 33537519, PMC7837416", A),
 (13, "Molecular cloning and beta-naphthoflavone-induced expression of a cytochrome P450 1A (CYP1A) gene from an anadromous river pufferfish, Takifugu obscurus. Mar Pollut Bull 2008;57(6-12):433-40 (초록 확인)", "https://doi.org/10.1016/j.marpolbul.2008.01.005", "Marine Pollution Bulletin, PubMed 18304588", A),
 (14, "A novel TTX-producing Aeromonas isolated from the ovary of Takifugu obscurus. Toxicon 2010;56(3):324-9 (초록 확인)", "https://doi.org/10.1016/j.toxicon.2010.03.019", "Toxicon, PubMed 20362605", A),
 (15, "Isolation of a Lysinibacillus fusiformis strain with tetrodotoxin-producing ability from puffer fish Fugu obscurus and the characterization of this strain. Toxicon 2010;56(4):640-3 (초록 확인)", "https://doi.org/10.1016/j.toxicon.2010.05.011", "Toxicon, PubMed 20576513", A),
 (16, "Isolation and identification of flavour peptides from Puffer fish (Takifugu obscurus) muscle using an electronic tongue and MALDI-TOF/TOF MS/MS. Food Chem 2012;135(3):1463-70 (초록 확인)", "https://doi.org/10.1016/j.foodchem.2012.06.026", "Food Chemistry, PubMed 22953881", A),
 (17, "Taste and stability characteristics of two key umami peptides from pufferfish (Takifugu obscurus). Food Chem 2022;371:131124 (초록 확인)", "https://doi.org/10.1016/j.foodchem.2021.131124", "Food Chemistry, PubMed 34563972", A),
 (18, "Physicochemical and Fibril Formation Properties of Pufferfish (Takifugu obscurus) Skin Collagen from Solvent Extraction in Different Conditions. Gels 2022;9(1):17 (초록 확인)", "https://doi.org/10.3390/gels9010017", "Gels (MDPI), PubMed 36661785, PMC9857395", A),
 (19, "Identification of Novel Antifreeze Peptides from Takifugu obscurus Skin and Molecular Mechanism in Inhibiting Ice Crystal Growth. J Agric Food Chem 2022;70(44):14148-14156 (초록 확인)", "https://doi.org/10.1021/acs.jafc.2c04393", "Journal of Agricultural and Food Chemistry, PubMed 36314886", A),
 (20, "Identification of novel xanthine oxidase inhibitory peptides from Takifugu obscurus: Peptidomic analysis, molecular docking, and dynamics simulation. Food Chem 2025;472:142935 (초록 확인)", "https://doi.org/10.1016/j.foodchem.2025.142935", "Food Chemistry, PubMed 39826518", A),
 (21, "Evaluation of the slow-release polylactic acid/polyhydroxyalkanoates active film containing oregano essential oil on the quality and flavor of chilled pufferfish (Takifugu obscurus) fillets. Food Chem 2022;385:132693 (초록 확인)", "https://doi.org/10.1016/j.foodchem.2022.132693", "Food Chemistry, PubMed 35303650", A),
 (22, "Effect of plasma-activated lactic acid on microbiota composition and quality of puffer fish (Takifugu obscurus) fillets during chilled storage. Food Chem X 2024;21:101129 (초록 확인)", "https://doi.org/10.1016/j.fochx.2024.101129", "Food Chemistry: X, PubMed 38298353, PMC10828650", A),
 (23, "Rapid in vivo determination of fluoroquinolones in cultured puffer fish (Takifugu obscurus) muscle by solid-phase microextraction coupled with liquid chromatography-tandem mass spectrometry. Talanta 2017;175:550-556 (초록 확인)", "https://doi.org/10.1016/j.talanta.2017.07.066", "Talanta, PubMed 28842032", A),
 (24, "Cold exposure triggers distinct RNA editing, alternative splicing, and gene expression patterns in cold domestication pufferfish (Takifugu obscurus). Fish Shellfish Immunol 2025;168:110972 (초록 확인)", "https://doi.org/10.1016/j.fsi.2025.110972", "Fish & Shellfish Immunology, PubMed 41183753", A),
 (25, "Genome-Scale Phylogenetic and Population Genetic Studies Provide Insight Into Introgression and Adaptive Evolution of Takifugu Species in East Asia. Front Genet 2021;12:625600 (초록 확인)", "https://doi.org/10.3389/fgene.2021.625600", "Frontiers in Genetics, PubMed 33692829, PMC7937929", A),
 (26, "식품의약품안전처 「식품의 기준 및 규격」(식품공전) 식품일반의 기준 및 규격 — 복어 가식부 독성 10 MU/g 이하, 식용 가능 복어 21종 지정" + WS, "https://www.foodsafetykorea.go.kr/popup/safefoodlife/food/foodRvlv/foodRvlvDetail.do?rvlv_no=12", "식품의약품안전처(식품안전나라)", A),
 (27, "식약처 '최근 20년간 복어독 식중독 47명 발생…21종만 식용 허용, 조리자격 필수' 보도" + WS, "https://foodtoday.or.kr/news/article.html?no=197945", "식품투데이", A),
 (28, "「식품위생법 시행령」 제36조(조리사를 두어야 하는 식품접객업자) — 복어독 제거가 필요한 복어를 조리·판매하는 영업자는 「국가기술자격법」에 따른 복어 조리 자격을 취득한 조리사를 두어야 함" + WS, "https://www.law.go.kr/법령/식품위생법시행령", "법제처 국가법령정보센터", A),
 (29, "[법령해석] '복어전문점 조리사 복어 요리 자격증 갖춰야'(2016-05-20, 법제처 법령해석 보도)" + WS, "https://m.go.seoul.co.kr/news/2016/05/20/20160520015005", "서울신문", A),
 (30, "「내수면어업법 시행령」 [별표 1] 포획·채취 금지 체장 — 황복(Takifugu obscurus) 20센티미터 이하" + WS, "https://www.law.go.kr/법령/내수면어업법시행령", "법제처 국가법령정보센터", A),
 (31, "황복의 부위별 독성 분포(1992·1993년 임진강 어획 46마리, 마우스 검정). 한국수산과학회지 1995" + WS, "https://koreascience.kr/article/JAKO199523607595681.page", "한국수산과학회지(KoreaScience)", A),
 (32, "자연산·양식산 황복의 장기별 독성(마우스 검정) 연구. 한국어병학회지 2009" + WS, "https://koreascience.kr/article/JAKO200910103423024.pdf", "한국어병학회지(KoreaScience)", A),
 (33, "양식산과 자연산 황복, Takifugu obscurus (Abe)의 식품학적 품질평가. 한국양식학회지 2007" + WS, "https://koreascience.kr/article/JAKO200707341591961.page", "한국양식학회지(KoreaScience)", A),
 (34, "경기도, 귀하신 몸 '황복' 양식 도전 — 특화 양식품종 지정, 집중 육성(2022 보도)" + WS, "https://www.newsseoul.co.kr/news/view/179588720538762", "뉴스서울", A),
 (35, "김포시, 한강에 황복 37만 마리 방류(2022-08-14 보도)" + WS, "https://www.fnnews.com/news/202208141008484552", "파이낸셜뉴스", A),
]
sources = [dict(n=n, title=t, url=u, publisher=p, accessed=a) for n, t, u, p, a in S]

sec = {}
sec["overview"] = ("한눈에 보기",
"황복(Takifugu obscurus)은 참복과(Tetraodontidae) 참복속의 물고기로, 식약처 「식품원료 목록」에 대표명 '황복', 이명 '강복', 영문(일명) 'Mefugu'인 수산물로 올라 있다[1]. 이 목록에서 황복(부위 '-')은 '사용가능'이지만, 같은 학명의 '황복알'과 '황복내장'은 따로 '사용불가'로 분류되어 알과 내장은 식품원료로 쓸 수 없다[1]. 사용 조건 문구나 건강기능식품 고시형 원료로서의 지위는 목록에 없다[1].\n\n"
"황복은 바다에서 자라다가 알을 낳으려고 강으로 거슬러 오르는 소하성 어종이며, 바닷물과 민물을 모두 견디는 염분 적응력 때문에 삼투 조절 연구의 대상이 되어 왔다[5, 7]. 국내에서는 한강 하류와 임진강에서 봄철에 잡히는 귀한 어종으로 소개된다(검색 요약으로만 확인)[34]. 근육에는 이노신산(IMP)과 유리아미노산, 감칠맛 펩타이드가 많아 맛 연구가 활발하다[4, 16, 17].\n\n"
"다만 복어독 테트로도톡신(TTX)을 먹이사슬로 쌓을 수 있어, 국내에서는 식용 가능한 복어 종과 가식부 독성 기준을 정하고 복어 조리 자격을 둔 조리사만 독 제거가 필요한 복어를 다루게 한다(검색 요약으로만 확인)[26–28].")
sec["history"] = ("이용·관리 역사",
"황복을 언제부터 어떻게 먹어 왔는지를 다룬 공식 문헌은 이번 조사에서 확인하지 못함.\n\n"
"1990년대 초 국내 연구진은 1992·1993년 임진강에서 잡힌 황복 46마리의 부위별 독성을 마우스 검정법으로 조사했다(검색 요약으로만 확인)[31]. 야생 황복 자원은 상업적 남획과 환경 오염으로 줄어든 것으로 보고되었다[13].\n\n"
"국내 황복 양식 기술은 2006년 국립수산과학원에서 시작되었고, 2015년에는 충청남도 수산연구소가 자주복 수컷과 황복 암컷을 교배한 품종을 민간에 보급했으나, 높은 소비자 가격과 낮은 채산성으로 민간 양식장은 거의 사라졌다고 보도되었다(검색 요약으로만 확인)[34]. 경기도는 황복을 특화 양식품종으로 정해 판매어 육성 기간을 2년 6개월에서 1년 6개월로 줄이는 연구에 나섰고, 김포시는 2022년 한강에 황복 37만 마리를 방류했다(검색 요약으로만 확인)[34, 35].\n\n"
"중국은 2016년 인증 업체에 한해 황복 등 복어 양식을 허용했으며, 이후 황복 소비가 합법화되어 상업적 가치가 커졌다고 논문들은 적고 있다[2, 4]. 중국 양식 황복은 국가표준 GB/T 27624–2011에 따라 전문 처리 인력이 도살·손질한다[4].")
sec["biology"] = ("어종·생태",
"황복은 바다에서 생활하다 산란을 위해 민물로 올라오는 소하성 어류로, 바닷물과 민물 양쪽에서 살아남는 넓은 염분 적응력을 지닌다[5]. 국내 보도에 따르면 바다에서 2~3년 자란 뒤 4~6월에 강으로 올라와 알을 낳는다(검색 요약으로만 확인)[34, 35]. 몸 크기·무늬 같은 형태 기재는 공식 도감을 열지 못해 확인하지 못함.\n\n"
"염분을 5 psu에서 30 psu로 갑자기 바꾸면 아가미와 신장에서 Na⁺/K⁺ ATPase 발현이 크게 늘고, 염분이 낮아지면 프로락틴 수용체 발현이 늘었으며, 아쿠아포린 1·3은 기관마다 다르게 반응했다[7]. 해수(32 ppt)에서 민물(0 ppt)로 옮겼을 때 황복 신장에서 달라진 유전자는 상향 14개·하향 4개뿐이었으나 자주복은 상향 449개·하향 139개로, 황복의 조절 체계가 간결한 것으로 해석되었다[8].\n\n"
"황복의 난소에서는 TTX를 만드는 Aeromonas 균주가, 간에서는 TTX 생성 능력이 있는 Lysinibacillus fusiformis 균주가 분리되어 공생 세균이 독의 출처일 가능성이 제기되었다[14, 15]. 야생형 황복은 저온에 약해, 5세대 인위 순화로 5 °C를 견디는 내한성 계통이 만들어졌다[24].")
sec["related_species"] = ("관련 종·이름",
"「식품원료 목록」에서 참복속 복어는 종마다 별도 행으로 관리되며, 황복 행의 이명은 '강복', 영문(일명)은 'Mefugu'다[1]. 같은 속 다른 종의 식용 여부·독성 자료는 종마다 다르므로 이 문서는 황복(Takifugu obscurus) 행과 이 종을 다룬 연구만 쓴다[1].\n\n"
"참복속 10종 122개체의 전장 유전체 재분석에서는 불완전 계통 분류와 잦은 교잡·유전자 이입 때문에 종 사이 관계가 복잡한 것으로 나타났다[25]. 황복의 염색체 수준 유전체에서 가장 긴 스캐폴드 22개는 자주복(T. rubripes) 염색체 22개와 1:1로 대응했다[5].\n\n"
"양식에서는 황복 암컷과 자주복 수컷의 교잡종이 만들어졌는데, 황복처럼 민물에서 살 수 있고 4·6개월령 체중이 황복보다 각각 38.06%·38.93% 무거웠다[9]. 국내 연구에서도 황복×자주복 교잡종과 교잡 3배체의 성장·혈액·지방산·염분 스트레스 반응이 비교되었고[10, 11], 3개월 초기 성장기에 교잡종의 특정 성장률이 1.48%로 가장 높았다[10]. 국내에서는 이 교잡 품종이 '슈퍼황복'이라는 이름으로 보급되었다고 보도되었다(검색 요약으로만 확인)[34].")
sec["cultivation"] = ("양식·어획",
"중국 광둥성 양식장 연구에서는 150–200 g 치어를 6개월 동안 민물(염분 0‰), 기수(3‰), 초어와의 혼합 양식(3‰)에서 길러 비교했고, 감칠맛 아미노산을 늘리고 삼투 조절 효율을 지키는 3‰ 기수를 권했다[4]. 같은 연구에서 월동 뒤 봄철 개체가 가을 개체보다 IMP가 44.7%, ATP가 92.8% 높아 수확 시기를 월동 이후로 맞추라고 제안했다[4]. 실험용 3개월령 양식 황복(20 ± 1 g)은 염분 8–10, 수온 22–25 °C의 기수에서 길렀다[2].\n\n"
"국내에서는 자연산과 양식산 황복 집단의 RAPD 분석에서 개체 간 밴드 공유도가 자연산 0.683, 양식산 0.759로 양식 집단의 유전적 다양성이 더 낮았다[12]. 자연산과 양식산 황복의 식품학적 품질을 비교한 국내 연구도 있다(검색 요약으로만 확인, 수치 확인하지 못함)[33].\n\n"
"「내수면어업법 시행령」 별표 1은 황복의 포획·채취 금지 체장을 20센티미터 이하로 정하고 있다(검색 요약으로만 확인)[30]. 파주·고양·김포 등 한강·임진강 인근 지자체는 매년 치어를 방류하며, 김포시는 2022년 37만 마리를 방류했다(검색 요약으로만 확인)[34, 35]. 국내 황복 어획량·양식 생산량 통계는 이번 조사에서 확인하지 못함.")
sec["processing"] = ("가공·저장·소재 연구",
"황복 근육 수용성 추출물에서 분리한 8개 아미노산 펩타이드 Tyr-Gly-Gly-Thr-Pro-Pro-Phe-Val(836.4 Da)은 감칠맛과 단맛을 냈다[16]. 이 펩타이드와 Pro-Val-Ala-Arg-Met-Cys-Arg는 중성 부근(pH 6.5–8.0)에서 감칠맛과 감칠맛 증강 효과를 보였고, 후자는 고쿠미(진한 맛)도 냈다[17].\n\n"
"껍질에서는 산 가용성·펩신 가용성 콜라겐을 뽑았는데, 4 °C 추출 콜라겐의 변성 온도는 각각 30.0 °C, 27.6 °C였다[18]. 껍질 가수분해물에서는 얼음 결정 성장을 억제하는 결빙 방지 펩타이드 EGPRAGGAPG 등 3종이 확인되었다[19]. 근육 가수분해물에서는 잔틴 산화효소를 억제하는 펩타이드 4종(W11, DD7, WY7, GA9)이 확인되었으나 사람 효과는 검증되지 않았다[20].\n\n"
"냉장 필레의 저장성 연구로는 오레가노 정유를 넣은 PLA/PHA 서방형 포장 필름(필레로 이행한 카르바크롤 9.70 mg/kg)과, 플라스마 활성 젖산 처리로 저장 기한을 4일 늘린 결과가 있다[21, 22]. 식약처 「식품 등의 생산실적」에서 황복 원료 품목은 확인하지 못함.")
sec["genetics"] = ("유전 정보",
"황복의 염색체 수준 참조 유전체는 PacBio Sequel 긴 염기서열과 Hi-C로 만들어졌으며, 초기 조립은 381 Mb(contig N50 3,296 kb)였고 Hi-C 정리 뒤 373 Mb(contig N50 15.2 Mb, 최장 28 Mb)였다[5]. 이 유전체는 복어류의 작은 유전체 특성과 염분 변동 적응 연구에 쓰일 자원으로 제시되었다[5].\n\n"
"미토콘드리아 유전체는 16,446 bp이며 유전자 배열은 같은 속 다른 종과 같고, 단백질 암호 유전자 13개 가운데 CO2와 ND4는 불완전 종결 코돈을 가졌다[6]. 국내 자연산·양식산 집단의 PCR(RAPD) 분석에서는 5개 프라이머로 578개 단편을 얻어 집단 구조를 비교했다[12].\n\n"
"황복×자주복 교잡종과 황복의 뇌하수체·간 전사체 비교에서는 각각 4,264개와 1,285개의 발현 차이 유전자가 나왔고, igf1·tgfβ1·bmp4 등이 교잡종 성장 우위의 후보 유전자로 꼽혔다[9]. 참복속 10종 비교 유전체 연구는 종 사이 교잡과 유전자 이입이 넓게 일어난다고 보고해, 방류 정책 수립 때 유전 자원 관리가 필요함을 시사했다[25].")
sec["safety"] = ("안전성",
"황복알과 황복내장은 「식품원료 목록」에서 사용불가다[1]. TTX는 나트륨 통로를 막아 신경·근육 마비와 호흡 부전을 일으키며, 생쥐 복강 LD50은 10.7 μg/kg이고 해독제가 없다[2]. 일반 조리로 잘 파괴되지 않는다[3]. 국내 식품공전은 복어 가식부 독성을 10 MU/g 이하로 정하고 21종만 식용으로 허용하며, 독 제거가 필요한 복어를 조리·판매하는 영업자는 복어 조리 자격 조리사를 두어야 한다(검색 요약으로만 확인)[26–29].\n\n"
"국내 자연산 황복은 생식소, 간, 장, 근육, 피부 순으로 독성이 높았고 장기 시료 45개 중 9개(간·생식소)가 10 MU/g을 넘었다(검색 요약으로만 확인)[32].\n\n"
"양식 무독화는 TTX가 없는 먹이·환경에서 기른다는 원리다[2]. 그러나 무독 양식 황복도 TTX 함유 고둥을 28일 먹으면 껍질 최대 6000 ng/g, 근육 최대 99.37 ng/g까지 쌓였고 무독 먹이 39일 뒤 근육은 2.32–7.4 ng/g으로 줄었다[2]. TTX를 먹지 않은 개체 근육에서는 TTX가 검출되지 않았지만, TTX를 먹은 개체가 죽은 뒤에는 근육 TTX가 산 개체보다 크게(최대 약 10배) 늘었다[3]. 국내 연구는 양식산 황복에도 TTX 유사 독소가 미량 있을 가능성을 제시했다(검색 요약으로만 확인)[32]. 양식 황복 근육의 항생제 잔류 분석법도 개발되었다[23]. 알레르기 정보는 확인하지 못함.")

ORDER = ["overview","history","biology","related_species","cultivation","processing","genetics","safety"]
sections = [dict(key=k, title=sec[k][0], body=sec[k][1]) for k in ORDER]

C = lambda name, ko, cls, role, part, content, act, src: dict(name=name, name_ko=ko, **{"class": cls}, role=role, part=part, content_text=content, activity_ko=act, source=src)
compounds = [
 C("Tetrodotoxin","테트로도톡신(TTX)","구아니딘계 신경독","marker","껍질·간·근육 등(먹이 노출 실험)","28일 노출 뒤 껍질 717.4·1484·6000 ng/g, 간 262.2·427.6·1840 ng/g, 근육 10.68·20.51·99.37 ng/g(저·중·고용량군)[2]","나트륨 통로를 막는 신경독으로 식용 안전성 판단의 핵심 지표다[2, 3]",[2,3]),
 C("5-Deoxytetrodotoxin","5-데옥시테트로도톡신","TTX 유사체","bioactive","조사한 모든 조직","정성 검출만(표준품 없음)[2]","TTX가 황복 체내에서 바뀐 산물로 추정되었다[2]",[2]),
 C("11-Deoxytetrodotoxin","11-데옥시테트로도톡신","TTX 유사체","bioactive","조사한 모든 조직","정성 검출만(표준품 없음)[2]","TTX 유사체로 모든 조직에서 검출되었다[2]",[2]),
 C("4,9-Anhydrotetrodotoxin","4,9-안하이드로테트로도톡신","TTX 유사체","bioactive","조사한 모든 조직","정성 검출만(표준품 없음)[2]","TTX 유사체로 모든 조직에서 검출되었다[2]",[2]),
 C("Inosine monophosphate","이노신산(IMP)","5′-뉴클레오타이드","nutrient","등 근육(양식)","220.480–398.780 mg/100 g; 봄 356.52, 가을 246.36 mg/100 g[4]","감칠맛·고쿠미와 가장 강하게 상관(r = 0.96, 0.97)한 감칠맛 매개 성분이다[4]",[4]),
 C("Guanosine monophosphate","구아닐산(GMP)","5′-뉴클레오타이드","nutrient","등 근육(양식)","민물 16.58, 기수 15.34 mg/100 g[4]","IMP와 함께 감칠맛 상승 작용에 관여하며 고쿠미와 양의 상관(r = 0.89)을 보였다[4]",[4]),
 C("Adenosine triphosphate","아데노신삼인산(ATP)","뉴클레오타이드","nutrient","등 근육(양식)","봄 5.92, 가을 3.07 mg/100 g[4]","신선도와 관련된 에너지 대사 지표로 해석되었다[4]",[4]),
 C("Glutamic acid","글루탐산(유리)","아미노산","nutrient","등 근육(양식)","0.348–2.187 mg/100 g; 민물 2.04, 기수 0.82 mg/100 g[4]","대표적 감칠맛 아미노산으로 양식 조건에 따라 변동이 컸다(CV 60.69%)[4]",[4]),
 C("Glycine","글리신(유리)","아미노산","nutrient","등 근육(양식)","봄 11.68, 가을 8.46 mg/100 g[4]","감칠맛(r = 0.74)·짠맛·고쿠미와 양의 상관을 보였다[4]",[4]),
 C("Lysine","라이신(유리)","아미노산","nutrient","등 근육(양식)","급이군 13.84, 5일 절식군 9.29 mg/100 g[4]","단맛과 음의 상관(r = −0.78)을 보였다[4]",[4]),
 C("Potassium","칼륨","무기질","nutrient","등 근육(양식)","170.280–307.800 mg/100 g[4]","짠맛과 매우 강한 양의 상관(r = 0.97)을 보였다[4]",[4]),
 C("Sodium","나트륨","무기질","nutrient","등 근육(양식)","34.550–56.290 mg/100 g; 민물 34.88, 기수 53.53 mg/100 g[4]","양식 수의 염분을 직접 반영해 민물 양식에서 53% 낮았다[4]",[4]),
 C("Tyr-Gly-Gly-Thr-Pro-Pro-Phe-Val","감칠맛 펩타이드 YGGTPPFV","펩타이드","bioactive","근육 수용성 추출물","분자량 836.4 Da(함량 미보고)[16]","감칠맛·단맛을 내며 pH 변화에 안정했다[16, 17]",[16,17]),
 C("Pro-Val-Ala-Arg-Met-Cys-Arg","감칠맛 펩타이드 PRVARMCR(PR-7)","펩타이드","bioactive","근육","함량 미보고[17]","중성 pH에서 감칠맛·감칠맛 증강·고쿠미를 냈다[17]",[17]),
]
# fix the PR-7 Korean label
compounds[-1]["name_ko"] = "감칠맛 펩타이드 PR-7(PVARMCR)"

assays = [
 {"role":"literature","compound":"Tetrodotoxin","compound_ko":"테트로도톡신(TTX)","part":"껍질·간·근육 등 9개 조직",
  "content":"고용량군 28일째 껍질 6000 ng/g, 간 1840 ng/g, 근육 99.37 ng/g; 무독 먹이 39일 뒤 근육 2.32–7.4 ng/g[2]",
  "method":"UPLC-MS/MS (ESI+, MRM)",
  "conditions":{"instrument":"Waters ACQUITY UPLC + Xevo TQS 삼중 사중극자 질량분석기(ESI)",
   "column":"ACQUITY UPLC BEH Amide, 50 mm × 2.1 mm, 1.7 μm",
   "mobile_phase":"A: 0.1% 폼산 함유 5 mmol/L 아세트산암모늄, B: 아세토나이트릴",
   "gradient":"0–1.5분 10% A; 1.5–4분 60% A; 4–4.1분 60% A; 4.1–5분 10% A",
   "flow":"0.3 mL/min","temp":"칼럼 40 °C, 시료실 4 °C",
   "detection":"ESI 양이온, MRM; 모세관 전압 3.0 kV, 이온원 110 °C, 탈용매 가스 350 °C·600 L/h, 콘 가스 50 L/h",
   "injection":"10 μL",
   "sample_prep":"균질 시료 0.5–2 g + 1% 아세트산 메탄올 10 mL, 3분 교반·60 °C 15분 초음파·8000 rpm 7분 원심 → 상등액 5 mL를 PBS 20 mL로 희석, pH 6.9–7.1 → 면역친화 칼럼(3 mL, 60 mg) 적재, 20% 메탄올 8 mL 세척, 2% 아세트산 메탄올 4 mL 용출 → 60 °C 질소 농축 → 0.1% 폼산 함유 5 mmol/L 아세트산암모늄/아세토나이트릴(1/9) 1 mL로 재용해, 0.22 μm 여과",
   "standard":"TTX 표준품(Dr. Ehrenstorfer)","linearity":"","lod":"","loq":"","recovery":""},
  "rationale":"TTX는 복어 식용 안전성(가식부 독성 기준)을 판단하는 지표 독소이며, 이 연구는 무독 양식 황복이 먹이로 TTX를 쌓고 배출하는 속도를 조직별로 정량했다[2]. 전문(Methods) 확인 — 검출·정량한계·회수율은 본문에 없고 앞선 논문 방법을 따랐다고만 적힘[2].",
  "source":[2],"url":"https://doi.org/10.3390/toxins12050278","source_kind":"paper"},
 {"role":"literature","compound":"Tetrodotoxin","compound_ko":"테트로도톡신(TTX, 살아 있는 개체 근육)","part":"등 근육",
  "content":"7일 노출 개체 중 2마리 LOD(32 ng/g) 초과·LOQ(150 ng/g) 미만, 무노출 개체 불검출[3]",
  "method":"생체 내 고체상 미량추출(SPME) + UPLC-MS/MS (ESI+, MRM)",
  "conditions":{"instrument":"Shimadzu Nexera LC30AD + SCIEX SelexION Triple Quad 5500",
   "column":"ACQUITY BEH HILIC, 2.1 × 100 mm, 1.7 μm",
   "mobile_phase":"A: 0.1% 폼산 물, B: 0.1% 폼산 아세토나이트릴",
   "gradient":"5% A 0.5분 유지 → 2.5분 동안 50% A → 1분 동안 95% A, 2분 유지 → 1분 동안 5% A, 1.9분 유지(총 8분)",
   "flow":"0.4 mL/min","temp":"칼럼 40 °C",
   "detection":"ESI 양이온 MRM m/z 320.1→162.0; 커튼 가스 35 psi, 이온 스프레이 5500 V, 탈용매 600 °C, 분무·보조 가스 55 psi; 머무름 시간 약 2.43분",
   "injection":"2 μL",
   "sample_prep":"GO-PAN@PNE 코팅 SPME 섬유(약 50 μm)를 0.1% 유제놀로 마취한 개체 등 근육의 약 1.5 cm 바늘 구멍에 꽂아 30분 추출 → 물로 3초 세척 → 메탄올 250 μL로 30분 용출",
   "standard":"TTX(≥99%)",
   "linearity":"150–1000 ng/g(어육 첨가 시료, 0.9895; 수용액 0.9955)",
   "lod":"32 ng/g(어육, S/N 3)","loq":"150 ng/g(어육, S/N 10)",
   "recovery":"회수율 미보고; 섬유 간 RSD 어육 8.82%, 수용액 4.63%"},
  "rationale":"살아 있는 황복을 죽이지 않고 근육 TTX를 확인하는 방법으로 개발되었고, 정량한계 150 ng/g이 식용 안전성 판정에 충분하다고 제시되었다[3]. 전문(Methods) 확인[3].",
  "source":[3],"url":"https://doi.org/10.3390/molecules27186122","source_kind":"paper"},
 {"role":"literature","compound":"Inosine monophosphate","compound_ko":"이노신산(IMP) 등 뉴클레오타이드","part":"등 근육(양식)",
  "content":"IMP 220.480–398.780 mg/100 g(12개 양식 조건)[4]",
  "method":"HPLC-UV",
  "conditions":{"instrument":"Agilent 1200 HPLC, UV–vis 검출기","column":"역상 C18(규격 미기재)",
   "mobile_phase":"아세토나이트릴과 인산 완충액","gradient":"기울기 용리(세부 미기재)","flow":"","temp":"",
   "detection":"UV(파장 미기재)","injection":"",
   "sample_prep":"등 근육 필레를 4 °C에서 해동·균질 → 과염소산 침전 후 중화 추출",
   "standard":"CMP·GMP·IMP·ATP·ADP·AMP·하이포잔틴·이노신 표준품(Dr. Ehrenstorfer), 외부 표준 검량선",
   "linearity":"","lod":"","loq":"","recovery":""},
  "rationale":"IMP는 황복 감칠맛·고쿠미와 가장 강하게 상관(r = 0.96, 0.97)한 맛 지표로 계절에 따라 1.45배 차이가 났다[4]. 전문(Methods) 확인 — 칼럼 규격·파장·유속·검출한계는 본문에 없음[4].",
  "source":[4],"url":"https://doi.org/10.3390/foods14081386","source_kind":"paper"},
 {"role":"literature","compound":"Free amino acids (glutamic acid etc.)","compound_ko":"유리아미노산(글루탐산 등)","part":"등 근육(양식)",
  "content":"글루탐산 0.348–2.187 mg/100 g, 라이신 급이군 13.84 mg/100 g[4]",
  "method":"LC-MS/MS (ESI, MRM, 비유도체화)",
  "conditions":{"instrument":"Waters TQ-XS(전기분무 이온화)","column":"C18, 2.1 × 100 mm, 1.7 μm",
   "mobile_phase":"","gradient":"기울기 용리(세부 미기재)","flow":"","temp":"",
   "detection":"MRM","injection":"",
   "sample_prep":"폼산/물/메탄올 추출, 유도체화 없음",
   "standard":"아미노산 17종 표준품(Dr. Ehrenstorfer), 외부 표준",
   "linearity":"","lod":"","loq":"","recovery":""},
  "rationale":"글루탐산·글리신·세린 등 유리아미노산은 황복 감칠맛·단맛·짠맛을 좌우하며 염분·계절·급이에 따라 크게 변했다[4]. 전문(Methods) 확인 — 이동상 조성·유속·검출한계는 본문에 없음[4].",
  "source":[4],"url":"https://doi.org/10.3390/foods14081386","source_kind":"paper"},
]

d = {
 "slug":"takifugu-obscurus","name_ko":"황복","name_en":"Obscure pufferfish (river pufferfish)",
 "scientific_name":"Takifugu obscurus (Abe, 1949)",
 "aliases":["강복","Mefugu","obscure puffer","river pufferfish","Fugu obscurus"],
 "sections":sections,"compounds":compounds,"markers":[],"assays":assays,"nutrients":[],
 "production":[],"world":[],"gi":[],"orgs":[],"sources":sources,
}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in sections: print(s["key"], len(s["body"]))
