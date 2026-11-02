import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
A = "2026-11-02"
def pm(n, title, doi, pmid, journal, pmc=None):
    pub = f"{journal} (PubMed {pmid}" + (f", {pmc}" if pmc else "") + ")"
    return {"n": n, "title": title, "url": f"https://doi.org/{doi}", "publisher": pub, "accessed": A}
S = [
 {"n": 1, "title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — '스피노숨'(Eucheuma denticulatum (Burman) Collins et Harvey / Eucheuma spinosum J. Agardh; 영명 Spinosum; 분류 식물; 사용 조건 '사용가능부위 : 전체')·'유큐마'(Eucheuma denticulatum; 분류 수산물; 사용 조건 '사용가능부위 : 전체') 행, 같은 목록의 '코토니'(Eucheuma cottonii; Kappaphycus alvarezii, 별칭 카파피쿠스 알바레지아이) 행, 식품첨가물(B코드) '카라기난' 행; 원료 카드의 다른 나라 목록 표시 EU_NOVEL_FOOD (로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json)", "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
 pm(2, "Re-evaluation of carrageenan (E 407) and processed Eucheuma seaweed (E 407a) as food additives. EFSA Journal 2018;16(4):e05238 (초록)", "10.2903/j.efsa.2018.5238", "32625873", "EFSA Journal, 유럽식품안전청 식품첨가물 패널", "PMC7009739"),
 pm(3, "Biochemical Composition and Seasonal Variations of the Madagascar Algae Eucheuma denticulatum (Rhodophyta). Mar Drugs 2025;23(1):30 (전문)", "10.3390/md23010030", "39852533", "Marine Drugs", "PMC11767090"),
 pm(4, "Carotenoid composition and antioxidant potential of Eucheuma denticulatum, Sargassum polycystum and Caulerpa lentillifera. Heliyon 2020;6(8):e04654 (전문)", "10.1016/j.heliyon.2020.e04654", "32817893", "Heliyon", "PMC7426577"),
 pm(5, "Eco-Friendly Extraction, Structure, and Gel Properties of ι-Carrageenan Extracted Using Ca(OH)2. Mar Drugs 2022;20(7):419 (전문; 추출본에서 학명 이탤릭이 빠져 있으며 PubMed 학명 검색으로 이 종 논문임을 확인)", "10.3390/md20070419", "35877712", "Marine Drugs", "PMC9322172"),
 pm(6, "Phytochemical composition and subacute toxicity of ethanolic extract of Eucheuma denticulatum on male Wistar albino rats. Toxicol Rep 2026;102268 (전문; 추출본에서 학명 이탤릭이 빠져 있으며 PubMed 학명 검색과 'spinosum' 표기로 이 종 논문임을 확인)", "10.1016/j.toxrep.2026.102268", "42170350", "Toxicology Reports", "PMC13188117"),
 pm(7, "Seaweed Farming in Tanzania: A Study of Working Practices and Geospatial Analysis of Occupational Hazards and Adverse Health Outcomes. J Agromedicine 2024 (초록)", "10.1080/1059924X.2024.2407986", "39397438", "Journal of Agromedicine"),
 pm(8, "Contrasting plastid and mitochondrial genome evolution in the Solieriaceae (Rhodophyta) reveals lineage-specific plastid gene loss in Kappaphycus. Mol Phylogenet Evol 2026;108688 (초록)", "10.1016/j.ympev.2026.108688", "42425252", "Molecular Phylogenetics and Evolution"),
 pm(9, "Transcriptome data of the carrageenophyte Eucheuma denticulatum. Data Brief 2019;24:103824 (초록)", "10.1016/j.dib.2019.103824", "30984808", "Data in Brief", "PMC6444127"),
 pm(10, "Identification and characterization of microRNAs in Eucheuma denticulatum by high-throughput sequencing and bioinformatics analysis. RNA Biol 2016;13(3):343-52 (초록)", "10.1080/15476286.2015.1125075", "26717154", "RNA Biology", "PMC4829290"),
 pm(11, "EuDBase: An online resource for automated EST analysis pipeline (ESTFrontier) and database for red seaweed Eucheuma denticulatum. Bioinformation 2011;7(4):157-62 (초록)", "10.6026/97320630007157", "22102771", "Bioinformation", "PMC3218516"),
 pm(12, "Purification, primary structure, and biological activity of the high-mannose-glycan-specific lectin from cultivated Eucheuma denticulatum. J Appl Phycol 2015;27(4):1657-69 (초록)", "10.1007/s10811-014-0441-0", "32214663", "Journal of Applied Phycology", "PMC7088313"),
 pm(13, "Enzymatic degradation of hybrid iota-/nu-carrageenan by Alteromonas fortis iota-carrageenase. Carbohydr Res 2010;345(7):934-40 (초록)", "10.1016/j.carres.2010.02.014", "20227066", "Carbohydrate Research"),
 pm(14, "Coil-helix transition of iota-carrageenan as a function of chain regularity. Biopolymers 2002;65(4):299-312 (초록)", "10.1002/bip.10250", "12382290", "Biopolymers"),
 pm(15, "On-line liquid chromatography electrospray ionization mass spectrometry for the characterization of kappa- and iota-carrageenans. Application to the hybrid iota-/nu-carrageenans. Anal Chem 2005;77(13):4125-36 (초록)", "10.1021/ac050091o", "15987118", "Analytical Chemistry"),
 pm(16, "Carrageenans. VII. Polysaccharides from Eucheuma spinosum and Eucheuma cottonii. The covalent structure of iota-carrageenan. J Chem Soc Perkin 1 1973;19:2173-6 (서지 정보만; 초록 없음)", "10.1039/p19730002173", "4796665", "Journal of the Chemical Society, Perkin Transactions 1"),
 pm(17, "Rapid production of ulcerative disease of the colon in newly-weaned guinea-pigs by degraded carrageenan. J Pharm Pharmacol 1989;41(6):423-6 (초록)", "10.1111/j.2042-7158.1989.tb06493.x", "2570843", "Journal of Pharmacy and Pharmacology"),
 pm(18, "Induction by degraded carrageenan of colorectal tumors in rats. Cancer Lett 1978;4(3):171-6 (초록)", "10.1016/s0304-3835(78)94237-4", "647659", "Cancer Letters"),
 {"n": 19, "title": "Experimental ulcerative disease of the colon. Methods Achiev Exp Pathol 1975;7:56-71 (초록)", "url": "https://pubmed.ncbi.nlm.nih.gov/1202321/", "publisher": "Methods and Achievements in Experimental Pathology (PubMed 1202321)", "accessed": A},
 pm(20, "Structure-activity in the carrageenans: iota-carrageenan and experimental oedemagenic activity. J Pharm Pharmacol 1984;36(12):808-13 (초록)", "10.1111/j.2042-7158.1984.tb04882.x", "6151972", "Journal of Pharmacy and Pharmacology"),
 pm(21, "Arsenic speciation in chinese seaweeds using HPLC-ICP-MS and HPLC-ES-MS. Analyst 2002;127(5):634-40 (초록)", "10.1039/b110940e", "12081041", "The Analyst"),
 pm(22, "Prediction of the dynamic distribution for Eucheuma denticulatum (Rhodophyta, Solieriaceae) under climate change in the Indo-Pacific Ocean. Mar Environ Res 2022;105730 (초록)", "10.1016/j.marenvres.2022.105730", "36027864", "Marine Environmental Research"),
 pm(23, "Diel variations in nutrient physiology among commercially important eucheumatoids Kappaphycus alvarezii, K. striatus and Eucheuma denticulatum. Planta 2025 (초록)", "10.1007/s00425-025-04673-6", "40146436", "Planta"),
 pm(24, "Nitrogenous substrate preference in eucheumatoids: Varying ammonium and nitrate ratios affect the nutrient uptake and growth of selected commercially cultivated crops. Plant Physiol Biochem 2025;109846 (초록)", "10.1016/j.plaphy.2025.109846", "40215735", "Plant Physiology and Biochemistry"),
 pm(25, "Survivorship and feeding preferences among size classes of outplanted sea urchins, Tripneustes gratilla, and possible use as biocontrol for invasive alien algae. PeerJ 2015;3:e1235 (초록)", "10.7717/peerj.1235", "26401450", "PeerJ", "PMC4579015"),
 pm(26, "Alteromonas fortis sp. nov., a non-flagellated bacterium specialized in the degradation of iota-carrageenan, and emended description of the genus Alteromonas. Int J Syst Evol Microbiol 2019;69(8):2514-21 (초록)", "10.1099/ijsem.0.003533", "31199221", "International Journal of Systematic and Evolutionary Microbiology"),
 pm(27, "Sensory, Physicochemical, and Cooking Qualities of Instant Noodles Incorporated with Red Seaweed (Eucheuma denticulatum). Foods 2022;11(17):2669 (초록)", "10.3390/foods11172669", "36076854", "Foods", "PMC9455614"),
 pm(28, "Multi-Extraction and Quality of Protein and Carrageenan from Commercial Spinosum (Eucheuma denticulatum). Foods 2020;9(8):1072 (초록)", "10.3390/foods9081072", "32781749", "Foods", "PMC7464751"),
 pm(29, "Efficient utilization of Eucheuma denticulatum hydrolysates using an activated carbon adsorption process for ethanol production in a 5-L fermentor. Bioprocess Biosyst Eng 2017;40(3):373-81 (초록)", "10.1007/s00449-016-1705-7", "27830360", "Bioprocess and Biosystems Engineering"),
 pm(30, "Phytochemical and Antioxidant Activities of Eucheuma spinosum as Natural Functional Food from North Sulawesi Waters, Indonesia. Pak J Biol Sci 2021;24(1):132-8 (초록)", "10.3923/pjbs.2021.132.138", "33683039", "Pakistan Journal of Biological Sciences"),
 pm(31, "Chemometric approaches for polysaccharide viscosity profiling. Carbohydr Polym 2024;122824 (초록)", "10.1016/j.carbpol.2024.122824", "39562099", "Carbohydrate Polymers"),
 pm(32, "Effects of Lactobacillus fermentation on Eucheuma spinosum polysaccharides: Characterization and mast cell membrane stabilizing activity. Carbohydr Polym 2023;120742 (초록)", "10.1016/j.carbpol.2023.120742", "36925257", "Carbohydrate Polymers"),
 pm(33, "Molecular mechanism of high-pressure processing for improving the quality of low-salt Eucheuma spinosum chicken breast batters. Poult Sci 2019;98(6):2670-8 (초록)", "10.3382/ps/pez027", "30715527", "Poultry Science"),
 pm(34, "Third-generation L-Lactic acid production by the microwave-assisted hydrolysis of red macroalgae Eucheuma denticulatum extract. Bioresour Technol 2021;342:125880 (초록)", "10.1016/j.biortech.2021.125880", "34592620", "Bioresource Technology"),
]

sections = [
 {"key": "overview", "title": "한눈에 보기", "body":
  "스피노숨(Eucheuma denticulatum)은 열대·아열대 산호초 주변에서 자라는 홍조류로, 'Spinosum'이라는 상업명으로 불리며 이오타(ι)-카라기난의 주된 원료다[9]. "
  "식약처 「식품원료 목록」에는 이 종이 '스피노숨'(학명 E. denticulatum (Burman) Collins et Harvey / E. spinosum J. Agardh, 분류 식물)과 '유큐마'(분류 수산물) 두 행으로 올라 있고, 두 행 모두 상태는 '사용가능', 사용 조건은 '사용가능부위 : 전체'다[1]. "
  "같은 목록에서 카라기난은 별도의 식품첨가물(B코드) 원료로 올라 있다[1]. "
  "원료 카드에는 EU 신규식품 목록 표시가 있으나, EU 원문에서 그 지위와 조건은 확인하지 못함. "
  "원료 카드의 목록 표시에는 건강기능식품 고시형 원료(KR_NOTICE) 표시가 없다[1].\n\n"
  "마다가스카르 시료는 건조 중량 기준으로 무기질(회분)이 20–39.5%, 중성당이 28.1–41.0%로 많고 단백질은 1.02–7.3%였다[3]. "
  "말레이시아 시료의 에탄올 추출 분석에서는 루테인이 주된 카로티노이드였다[4]. "
  "카라기난의 식품첨가물 안전성은 유럽식품안전청(EFSA)이 '가공 유케마 해조(E 407a)'와 함께 묶어 평가했으며, 이는 이 종만을 대상으로 한 평가가 아니다[2]. "
  "이 종 자체의 효능 연구는 세포·동물 실험이 대부분이고 사람 대상 시험은 확인하지 못함."},
 {"key": "history", "title": "이용 역사", "body":
  "1973년 발표된 연구는 E. spinosum과 E. cottonii의 다당류를 비교해 이오타-카라기난의 공유결합 구조를 보고했다[16]. "
  "1970년대에는 하와이에서 채집한 E. spinosum 엽상체에서 이오타-카라기난을 분해하는 세균이 분리되었고, 이 균주는 2019년 Alteromonas fortis라는 새 종으로 기재되었다[26]. "
  "탄자니아에서는 필리핀에서 들여온 'spinosum'과 'cottonii' 두 홍조류로 1989년 상업 양식이 시작되었고, 1990년대 초부터 상업 규모 수출이 이루어졌다[6]. "
  "현재 잔지바르 해조 양식은 주로 E. spinosum을 기르며, 일하는 사람의 대다수가 여성이다[7].\n\n"
  "마다가스카르에서는 1989년 남서부에서 해조 양식 시험이 시작되었고, 1998년 잔지바르에서 생장이 좋은 계통을 들여와 북부로 넓혔다[3]. "
  "같은 논문은 마다가스카르에서 'spinosum'으로 불리는 이 종이 50년 동안 이오타-카라기난 원료로 양식되어 왔다고 적었다[3]. "
  "인도네시아 북술라웨시 연구진은 E. spinosum을 일상적으로 먹는 자연 식품 재료로 소개했다[30]. "
  "우리나라에서 이 종을 식품으로 먹어 온 기록은 확인하지 못함."},
 {"key": "biology", "title": "생물학적 특징·생태", "body":
  "스피노숨은 솔리에리아과(Solieriaceae)에 속하는 홍조류로, 물살이 적당히 센 열대·아열대 산호초에서 자연적으로 자란다[3, 9]. "
  "가지는 가시처럼 끝이 뾰족하고, 길이 1–8 mm의 작은 가지가 빽빽하게 덮여 있다[6]. "
  "인도-태평양 분포 모델 연구에서는 해안까지의 거리, 해수면 온도, 해류 속도가 분포를 가장 잘 설명했고, 2100년에는 순다 대륙붕 등 중앙 인도-태평양에서 분포가 줄고 호주 남부 해안 쪽으로 넓어질 것으로 예측되었다[22]. "
  "마다가스카르 생트마리섬 시료에서는 성숙기에 이오타형 카라기난이 주를 이루고, 어린 시기에는 카파·뉴 카라기난이 일부 섞였다[3].\n\n"
  "실험실 배양에서 이 종은 낮과 밤 모두 무기 질소를 흡수했고, 세 유케마류의 밤 흡수 비율은 전체 무기 질소 흡수량의 41.8–46.6%였다[23]. "
  "암모늄과 질산염 비율을 바꾼 배양에서 이 종은 생장률 범위가 가장 넓었으나 질소 형태 비율에는 민감하지 않았다[24]. "
  "하와이 카네오헤만에서는 이 종이 외래 침입 해조로 다뤄지며, 성게 먹이 시험에서 어린 성게가 가장 적게 먹은 해조였다[25]."},
 {"key": "related_species", "title": "관련 종·이름", "body":
  "식약처 목록의 학명 칸에는 E. denticulatum (Burman) Collins et Harvey와 이명 E. spinosum J. Agardh가 함께 적혀 있다[1]. "
  "같은 목록의 '코토니'는 Eucheuma cottonii와 Kappaphycus alvarezii(별칭 카파피쿠스 알바레지아이)로 적힌 별개 원료이므로, 카파-카라기난 원료인 코토니 자료를 이 종에 옮기면 안 된다[1, 15]. "
  "분석 연구에서도 카파-카라기난은 K. alvarezii에서, 이오타 및 이오타/뉴 혼성 카라기난은 E. denticulatum에서 추출해 따로 다뤘다[15]. "
  "상업적으로 가장 많이 기르는 유케마류(eucheumatoids)는 K. alvarezii, K. striatus, E. denticulatum의 세 분류군이다[8].\n\n"
  "엽록체 유전체 비교에서 E. denticulatum은 pbsA(693 bp)와 ycf57(354 bp) 유전자를 갖고 있었으나 카파피쿠스 두 종에서는 두 유전자가 모두 없었다[8]. "
  "E. denticulatum의 렉틴 EDA-2는 Eucheuma serra의 ESA-2와 1차 구조가 매우 비슷하다[12]. "
  "인도네시아·말레이시아 논문 중에는 학명 없이 'spinosum'이라고만 적거나 여러 홍조류를 함께 다룬 것이 있어, 각 결과가 이 종의 것인지 원문으로 확인해야 한다[6, 30]."},
 {"key": "cultivation", "title": "양식·채취", "body":
  "우리나라의 스피노숨 양식·생산 통계는 확인하지 못함. "
  "마다가스카르 논문에 따르면 유케마류 해조의 주요 양식지는 동남아시아와 탄자니아·케냐이며[3], 이 논문은, 마다가스카르 논문은 2019년 이 속 해조 생산량이 18만 톤이고 주로 잔지바르와 필리핀에서 나왔다고 2차 인용했다[3]. "
  "이 수치는 원문 추출본에서 학명 표기가 빠져 종 단위인지 속 단위인지 확인하지 못함. "
  "잔지바르 3개 지역 45개 협동조합 조사에서 해조 양식 노동자는 손목(87%)·허리(84%)·하지(73%) 근골격계 증상과 피부 문제(80%)를 많이 호소했다[7].\n\n"
  "마다가스카르 생트마리섬 자생지 시료는 민물로 씻어 염분을 뺀 뒤 그늘의 선반에서 1–2주 전통 방식으로 말렸다[3]. "
  "같은 연구에서 질소·인 농도와 계절에 따라 무기질·당·단백질 함량이 해마다 달랐다[3]. "
  "탄자니아 시료는 잔지바르 운구자섬 푸름바 마을에서 2025년 3월에 채취해 식물분류학자가 동정했다[6]. "
  "말레이시아 사바주 시료는 수산국 양식과의 도움으로 해안에서 채취해 동결건조했다[4]."},
 {"key": "processing", "title": "가공·이용 연구", "body":
  "마다가스카르 시료를 탈색한 뒤 80 °C 물로 추출하면 카라기난 추출물 수율은 건조 원료의 53.1–66.0%였다[3]. "
  "중국 연구진은 끓는 물 전처리 후 0.5% 수산화칼슘으로 이오타-카라기난을 뽑는 방법을 500 L 규모로 시험했고, 수율 24.7%로 기존 수산화나트륨법(21.0%)보다 17.6% 높고 알칼리 93.3%·물 86.8%를 덜 썼다[5]. "
  "이오타-카라기난에 전구체인 뉴(ν) 단위가 약 3% 섞이면 겔의 탄성률(G′)이 최대 2배로 커졌다[14]. "
  "E. denticulatum 카라기난의 점도는 크기배제크로마토그래피-다각도광산란 자료로 예측 오차가 가장 작게 모델링되었다[31].\n\n"
  "식품 응용으로는 인스턴트 국수에 스피노숨 분말을 5–15% 넣은 연구가 있으며, 7.5–15% 첨가 시 조리 수율이 높아지고 조리 손실이 줄었다[27]. "
  "저염 닭가슴살 반죽에서는 고압 처리로 보수력이 높아졌고, E. spinosum을 0.4%까지 넣으면 그 효과가 더 커졌다[33]. "
  "카라기난 추출 전에 효소로 단백질을 먼저 뽑으면 단백질 추출 효율이 최대 59%였고 카라기난 수율·품질은 떨어지지 않았다[28]. "
  "국내 연구진은 110 g 건조중량/L 슬러리를 산·효소로 당화해 단당 37.8 g/L을 얻고 에탄올 15.8 g/L을 생산했다[29]. "
  "말레이시아에서는 추출물을 가수분해해 갈락토스 수율 50.7%를 얻고 L-젖산 발효 원료로 썼다[34]. 젖산균으로 발효한 E. spinosum 다당류는 비만세포 탈과립을 억제했으나, 이는 세포 실험과 생쥐 모델 수준의 결과다[32]."},
 {"key": "genetics", "title": "유전 정보", "body":
  "말레이시아 사바주 쿠닷·셈포르나 시료에서 얻은 발현서열태그(EST) 10,031개가 2,275개 고유 전사체와 955개 단일서열로 정리되어 온라인 데이터베이스로 공개되었다[11]. "
  "같은 지역 연구진은 카라기난 생합성 유전자를 찾기 위해 RNA 염기서열 분석을 하고 자료를 NCBI(PRJNA477734)에 등록했다[9]. "
  "중국 연구진은 소형 RNA 2,997,135개 서열에서 마이크로RNA 134개(보존형 133개, 새로운 것 1개)를 찾고, 표적 유전자 871개를 예측했다[10].\n\n"
  "2026년 비교 유전체 연구는 E. denticulatum의 엽록체·미토콘드리아 전체 유전체를 새로 해독했고, pbsA·ycf57 유전자가 다른 솔리에리아과와 같은 배열로 보존되어 있음을 보였다[8]. "
  "이 종의 렉틴은 약 28 kDa의 단량체 단백질 세 가지(이소렉틴)로 분리되었고, 그중 EDA-2의 cDNA는 시작 메티오닌을 포함해 269개 아미노산을 암호화했다[12]. "
  "EDA-2는 고만노스형 N-당사슬에만 결합했고, 렉틴 혼합물은 새우 병원 세균의 생장을 억제했다[12]. "
  "이 종의 핵 유전체 전체 해독 결과는 확인하지 못함."},
 {"key": "safety", "title": "안전성", "body":
  "식약처 목록에서 스피노숨·유큐마는 '사용가능' 원료이며 사용 조건은 '사용가능부위 : 전체'다[1]. "
  "식품 알레르기·잔류물질·중금속에 관한 국내 공공기관 정보는 확인하지 못함. "
  "중국산 식용 해조 비교 연구에서 이 종의 비소 화학종 추출 수율은 25.0%로 다시마(76.4%)·김(69.8%)보다 낮았고, 이 종의 비소 화학종 구성은 초록에서 확인하지 못함[21].\n\n"
  "카라기난 일반에 대한 평가로, EFSA는 2018년 식품첨가물 카라기난(E 407)과 가공 유케마 해조(E 407a)를 함께 재평가했다[2]. "
  "EFSA는 카라기난이 그대로 흡수되지 않고, 유전독성·발암성 우려가 없다고 보았으나 자료의 불확실성 때문에 그룹 1일섭취허용량 75 mg/kg 체중을 '잠정'으로 두었다[2]. "
  "평균 분자량 10–20 kDa의 분해 카라기난(폴리지난)은 식품첨가물로 허가되지 않았다[2]. "
  "E. spinosum 유래 분해 카라기난을 기니피그에 먹이면 대장 궤양이, 쥐에 최장 24개월 먹이면 대장·직장 종양이 생겼다[17, 18, 19]. "
  "이 결과는 식품용 카라기난이나 해조 자체가 아니라 분해한 저분자 카라기난의 동물 실험이다[2, 17, 18]. E. spinosum 유래 이오타-카라기난은 쥐 발바닥 부종 유발 모델에서 분자량 73,700 분획에 활성이 있었는데, 이는 염증 실험용 주사 모델이다[20]. "
  "이 종 자체 자료로는, 에탄올 추출물을 수컷 쥐에 28일 동안 300–1000 mg/kg 먹인 시험에서 생화학 지표에 유의한 변화가 없었으나 1000 mg/kg에서 간·신장 조직에 가벼운 변화가 보였다[6]."},
]

compounds = [
 {"name": "iota-Carrageenan", "name_ko": "이오타(ι)-카라기난", "class": "황산화 갈락탄 다당류", "role": "marker", "part": "엽상체 전체(건조)",
  "content_text": "물 추출 카라기난 추출물 수율 53.1–66.0% dw(마다가스카르, 2021–2022)[3]; 수산화칼슘법 수율 24.7%(수산화나트륨법 21.0%)[5]",
  "activity_ko": "겔화·증점 식품첨가물 원료; 성숙기 엽상체의 주된 카라기난형[3, 5]", "source": [3, 5]},
 {"name": "nu-Carrageenan", "name_ko": "뉴(ν)-카라기난", "class": "황산화 갈락탄 다당류(이오타 전구체)", "role": "bioactive", "part": "엽상체",
  "content_text": "중성 추출 카라기난에서 뉴 단위 0–23 monomer %로 조절한 시료 제조[14]",
  "activity_ko": "약 3% 함유 시 이오타-카라기난 겔 탄성률 최대 2배[14]; 이오타/뉴 혼성 올리고당 구조 해석[13]", "source": [13, 14]},
 {"name": "3,6-Anhydrogalactose", "name_ko": "3,6-안하이드로갈락토스", "class": "카라기난 구성당", "role": "marker", "part": "엽상체 건조 분말",
  "content_text": "7.344–12.65% dw(2021), 7.75–11.655% dw(2022)[3]",
  "activity_ko": "함량이 높을수록 카라기난 겔 강도가 높음[5]", "source": [3, 5]},
 {"name": "Galactose", "name_ko": "갈락토스", "class": "단당(카라기난 구성당)", "role": "nutrient", "part": "카라기난 추출물(산가수분해)",
  "content_text": "총당 대비 43.2–55.2% TS(월별, 2021–2022)[3]; 추출물 가수분해 갈락토스 수율 50.7%[34]",
  "activity_ko": "카라기난의 주 구성당; 젖산·에탄올 발효 원료[29, 34]", "source": [3, 29, 34]},
 {"name": "Sulfate", "name_ko": "황산기", "class": "다당류 치환기", "role": "bioactive", "part": "엽상체 건조 분말",
  "content_text": "3.7–14.5% dw(2021), 3.71–9.86% dw(2022)[3]",
  "activity_ko": "카라기난 유형(이오타·카파·뉴)을 가르는 구조 요소[3, 15]", "source": [3, 15]},
 {"name": "Protein", "name_ko": "단백질", "class": "영양소", "role": "nutrient", "part": "엽상체 건조 분말",
  "content_text": "4.8–7.3% dw(2021), 1.02–6.29% dw(2022), BCA법[3]; 총 아미노산 2.46–2.68% AA(8월 시료)[3]",
  "activity_ko": "효소 보조 추출로 단백질 추출 효율 최대 59%[28]", "source": [3, 28]},
 {"name": "Potassium", "name_ko": "칼륨", "class": "무기질", "role": "nutrient", "part": "엽상체 건조 분말",
  "content_text": "11.6–12.8% dw(2021), 11.0–13.2% dw(2022)[3]", "activity_ko": "이 종에서 가장 많은 무기질[3]", "source": [3]},
 {"name": "Magnesium", "name_ko": "마그네슘", "class": "무기질", "role": "nutrient", "part": "엽상체 건조 분말",
  "content_text": "5.2–5.7% dw(2021), 5.3–5.8% dw(2022)[3]", "activity_ko": "다량 무기질[3]", "source": [3]},
 {"name": "Iron", "name_ko": "철", "class": "무기질(미량원소)", "role": "nutrient", "part": "엽상체 건조 분말",
  "content_text": "0.17–0.30% dw(2021), 0.17–0.28% dw(2022)[3]", "activity_ko": "미량원소 가운데 가장 많음[3]", "source": [3]},
 {"name": "Lutein", "name_ko": "루테인", "class": "카로티노이드(잔토필)", "role": "bioactive", "part": "엽상체(동결건조 분말 에탄올 추출)",
  "content_text": "87.7 mg/100 g DW[4]", "activity_ko": "이 종의 주된 잔토필; 항산화 성분 후보[4]", "source": [4]},
 {"name": "beta-Carotene", "name_ko": "베타카로틴", "class": "카로티노이드(카로텐)", "role": "nutrient", "part": "엽상체(동결건조 분말 에탄올 추출)",
  "content_text": "4.7 mg/100 g DW(UHPLC-DAD)[4]", "activity_ko": "프로비타민 A 카로티노이드[4]", "source": [4]},
 {"name": "beta-Cryptoxanthin", "name_ko": "베타크립토잔틴", "class": "카로티노이드(잔토필)", "role": "bioactive", "part": "엽상체(동결건조 분말 에탄올 추출)",
  "content_text": "3.6 mg/100 g DW[4]", "activity_ko": "검출된 카로티노이드 중 가장 적음[4]", "source": [4]},
 {"name": "Phytol", "name_ko": "피톨", "class": "디테르펜 알코올", "role": "bioactive", "part": "엽상체 에탄올 추출물",
  "content_text": "LC-MS로 59개 성분 중 하나로 잠정 동정(함량 확인하지 못함)[6]",
  "activity_ko": "논문은 항당뇨 관련 성분으로 논의했으나 이 추출물의 약리 시험은 없음[6]", "source": [6]},
 {"name": "3-(3-Methoxyphenyl)propanal", "name_ko": "3-(3-메톡시페닐)프로판알", "class": "페닐프로파노이드 알데하이드", "role": "bioactive", "part": "엽상체 에틸아세테이트 추출물",
  "content_text": "분리 화합물(함량 확인하지 못함)[30]", "activity_ko": "에틸아세테이트 추출물이 DPPH·SOD 라디칼 소거 활성(시험관)[30]", "source": [30]},
]

assays = [
 {"role": "literature", "compound": "Lutein, beta-cryptoxanthin, beta-carotene", "compound_ko": "루테인·베타크립토잔틴·베타카로틴", "part": "엽상체 동결건조 분말(40 mesh)의 에탄올 추출물",
  "content": "루테인 87.7, 베타카로틴 4.7, 베타크립토잔틴 3.6 mg/100 g DW[4]",
  "method": "UHPLC-ESI-HRMS/MS(Orbitrap), 베타카로틴은 UHPLC-DAD",
  "conditions": {"instrument": "Dionex Ultimate 3000 UHPLC + Q Exactive 하이브리드 사중극자-오비트랩 질량분석기",
   "column": "Acquity UPLC BEH C18 (Waters), 50 mm × 2.1 mm, 1.7 μm",
   "mobile_phase": "A: 0.1% 포름산 물, B: 0.1% 포름산 아세토니트릴",
   "gradient": "0–2분 5% B; 2–20분 5→99% B; 20–25분 99% B; 25–30분 5% B",
   "flow": "0.3 mL/min", "temp": "칼럼 35 °C, 오토샘플러 4 °C",
   "detection": "ESI 양·음이온, 분해능 140,000 FWHM, m/z 100–1000, 스프레이 전압 3.7 kV, 모세관 320 °C, 충돌에너지 35 V; 베타카로틴은 DAD",
   "injection": "3 μL(추출물 1 mg/mL)",
   "sample_prep": "동결건조 분말:100% 에탄올 1:20(w/v) 상온 24시간 교반, 여과·감압농축(45 °C)·진공원심건조; DCM/MeOH 50:50에 녹여 0.22 μm 나일론 필터",
   "standard": "루테인·베타카로틴·제아잔틴(Sigma), 베타크립토잔틴·칸타잔틴·푸코잔틴 등(ChromaDex)",
   "linearity": "5점 검량선, R² > 0.97",
   "lod": "최저 0.0011 ng/μL(칸타잔틴); 베타카로틴 0.0418 ng/μL(UHPLC-DAD)",
   "loq": "최저 0.0044 ng/μL(칸타잔틴); 베타카로틴 0.1393 ng/μL",
   "recovery": "85–104%(베타크립토잔틴 74%)"},
  "rationale": "루테인은 이 종 추출물에서 가장 많은 카로티노이드로 정량되었고 홍조류의 대표 잔토필이다; 전문 확인[4].",
  "source": [4], "url": "https://doi.org/10.1016/j.heliyon.2020.e04654", "source_kind": "paper"},
 {"role": "literature", "compound": "Galactose (carrageenan monosaccharides)", "compound_ko": "갈락토스 등 카라기난 구성 단당", "part": "엽상체 카라기난 추출물",
  "content": "갈락토스 43.2–55.2% TS, 총 단당 74.2–86.3% TS[3]",
  "method": "HPAEC-PAD",
  "conditions": {"instrument": "고성능 음이온교환 크로마토그래피-펄스 전류 검출(Thermo Dionex)",
   "column": "", "mobile_phase": "", "gradient": "원문은 이전 논문(Pliego-Cortés 외 2019)의 용리 프로그램을 따름", "flow": "", "temp": "",
   "detection": "펄스 전류 검출(PAD)", "injection": "",
   "sample_prep": "카라기난 추출물 4 mg + 1 M HCl 110 μL + 초순수 1 mL, 밀봉 앰플 100 °C 48시간 가수분해; 1 M NaOH 110 μL로 중화, 내부표준 데옥시리보스 50 ppm; 10,000 rpm 10분 원심분리",
   "standard": "데옥시리보스(내부표준), 람노스·아라비노스·글루코사민·갈락토스·포도당·만노스·자일로스·과당·리보스·글루쿠론산",
   "linearity": "검량 범위 1.95–125 ppm", "lod": "", "loq": "", "recovery": ""},
  "rationale": "갈락토스는 카라기난 골격의 주 구성당으로 원료 품질과 계절 변이를 보는 지표로 쓰였다; 전문 확인했으나 칼럼·용리 조건은 인용 논문에 있어 비움[3].",
  "source": [3], "url": "https://doi.org/10.3390/md23010030", "source_kind": "paper"},
 {"role": "literature", "compound": "3,6-Anhydrogalactose", "compound_ko": "3,6-안하이드로갈락토스", "part": "엽상체 건조 분말",
  "content": "7.344–12.65% dw(2021), 7.75–11.655% dw(2022)[3]",
  "method": "레조르시놀 비색법(Yaphe·Arsenault 1965 변법)",
  "conditions": {"instrument": "분광광도계", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "80 °C 산성 반응",
   "detection": "480 nm", "injection": "",
   "sample_prep": "건조 분말 10 mg을 1 M HCl 5 mL로 100 °C 2시간 가수분해 후 1 M NaOH 5 mL로 중화",
   "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "3,6-안하이드로갈락토스는 이오타·카파 카라기난의 구성 단위로 함량이 겔 강도를 좌우한다; 전문 확인[3, 5].",
  "source": [3, 5], "url": "https://doi.org/10.3390/md23010030", "source_kind": "paper"},
]

d = {
 "slug": "eucheuma-denticulatum", "name_ko": "스피노숨", "name_en": "Spinosum (Eucheuma denticulatum)",
 "scientific_name": "Eucheuma denticulatum (Burman) Collins et Harvey",
 "aliases": ["유큐마", "Spinosum", "Eucheuma spinosum J. Agardh"],
 "sections": sections, "compounds": compounds, "markers": [], "assays": assays, "nutrients": [],
 "production": [], "gi": [], "orgs": [], "world": [], "sources": S,
}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in sections: print(s["key"], len(s["body"]))
