import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
A = "2026-11-02"
def pm(n, title, doi, pmid, journal, pmc=None, note="초록 확인"):
    pub = f"{journal}, PMID {pmid}" + (f", {pmc}" if pmc else "")
    return {"n": n, "title": f"{title} ({note})", "url": f"https://doi.org/{doi}", "publisher": pub, "accessed": A}
S = [
 {"n": 1, "title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — Carcharodon carcharias 행(백상아리, Great white shark, 수산물, 부위 '-', 사용가능, 사용 조건 없음, 고시형 원료 원재료 목록 없음) 및 같은 목록의 상어류 행(청상아리 Isurus oxyrinchus·악상어 Lamna ditropis 사용가능; 비악상어 Lamna nasus·미흑점상어 Carcharhinus falciformis·장완흉상어 Carcharhinus longimanus 사용불가 — '식품의 기준 및 규격 개정고시(제2018-8호,180222)에 따라 멸종위기 야생생물을 식품원료로 사용할 수 없도록 금지'; 상어·상어간유추출물 등은 Mustelus manazo·Mustelus griseus 행) — 로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json", "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
 {"n": 2, "title": "식품의약품안전처 「건강기능식품의 기준 및 규격」(고시 제2026-43호) 제3. 2-19 스쿠알렌·2-21 알콕시글리세롤 함유 상어간유 — 원재료 '상어 간', 지표성분·일일섭취량·주의사항(프로젝트 원문 사본 docs/refs/MFDS/건강기능식품의기준및규격_2026-43_제1~제3.txt)", "url": "https://www.foodsafetykorea.go.kr", "publisher": "식품의약품안전처", "accessed": "2026-10-12"},
 {"n": 3, "title": "식품의약품안전처 「식품 등의 생산실적」 2018–2025년판 — 건강기능식품 고시형 '스쿠알렌'·'알콕시글리세롤 함유 상어간유' 행(앱 파싱본 docs/stats/hf_items.csv, 금액 천원 단위)", "url": "https://www.mfds.go.kr", "publisher": "식품의약품안전처", "accessed": "2026-10-12"},
 pm(4, "Pethybridge HR et al. Lipid, fatty acid and energy density profiles of white sharks: insights into the feeding ecology and ecophysiology of a complex top predator. PLoS One 2014;9(5):e97877", "10.1371/journal.pone.0097877", "24871223", "PLoS One", "PMC4037211", "PMC 전문(Methods·표) 확인"),
 pm(5, "The last frontier: catch records of white sharks (Carcharodon carcharias) in the Northwest Pacific Ocean. PLoS One 2014;9(4):e94407", "10.1371/journal.pone.0094407", "24740299", "PLoS One", "PMC3989224", "PMC 전문 확인"),
 pm(6, "Ecological Characteristics of Large-Bodied Sharks in the East Sea of Korea. Animals (Basel) 2025;15(20):2974", "10.3390/ani15202974", "41153901", "Animals (Basel)", "PMC12560914", "PMC 전문 확인"),
 pm(7, "A novel mini-DNA barcoding assay to identify processed fins from internationally protected shark species. PLoS One 2015;10(2):e0114844", "10.1371/journal.pone.0114844", "25646789", "PLoS One", "PMC4315593"),
 pm(8, "Genome analysis reveals three distinct lineages of the cosmopolitan white shark. Curr Biol 2024;34(15)", "10.1016/j.cub.2024.06.076", "39047735", "Current Biology"),
 pm(9, "White shark genome reveals ancient elasmobranch adaptations associated with wound healing and the maintenance of genome stability. Proc Natl Acad Sci U S A 2019;116(10):4446-4455", "10.1073/pnas.1819778116", "30782839", "PNAS", "PMC6410855"),
 pm(10, "Mitochondrial genome of an Atlantic white shark (Carcharodon carcharias). Mitochondrial DNA B Resour 2016;1(1)", "10.1080/23802359.2016.1222248", "33473604", "Mitochondrial DNA Part B", "PMC7799651"),
 pm(11, "The complete mitochondrial DNA of white shark (Carcharodon carcharias) from Isla Guadalupe, Mexico. Mitochondrial DNA A 2016", "10.3109/19401736.2014.945556", "25121830", "Mitochondrial DNA Part A"),
 pm(12, "Associations between total mercury, trace minerals, and blood health markers in Northwest Atlantic white sharks (Carcharodon carcharias). Mar Pollut Bull 2023;196:115533", "10.1016/j.marpolbul.2023.115533", "37734227", "Marine Pollution Bulletin"),
 pm(13, "The Twilight Zone as a Major Foraging Habitat and Mercury Source for the Great White Shark. Environ Sci Technol 2020;54(24)", "10.1021/acs.est.0c05621", "33238094", "Environmental Science & Technology"),
 pm(14, "Foraging plasticity diversifies mercury exposure sources and bioaccumulation patterns in the world's largest predatory fish. J Hazard Mater 2022;425:127956", "10.1016/j.jhazmat.2021.127956", "34986563", "Journal of Hazardous Materials"),
 pm(15, "Global versus local causes and health implications of high mercury concentrations in sharks from the east coast of South Africa. Sci Total Environ 2016", "10.1016/j.scitotenv.2015.09.074", "26409147", "Science of the Total Environment"),
 pm(16, "Metal and metalloid concentrations in the tissues of dusky Carcharhinus obscurus, sandbar C. plumbeus and white Carcharodon carcharias sharks from south-eastern Australian waters, and the implications for human consumption. Mar Pollut Bull 2015", "10.1016/j.marpolbul.2014.12.037", "25656241", "Marine Pollution Bulletin"),
 pm(17, "Effects of trophic ecology and habitat use on maternal transfer of contaminants in four species of young of the year lamniform sharks. Mar Environ Res 2013", "10.1016/j.marenvres.2013.05.009", "23773783", "Marine Environmental Research"),
 pm(18, "Blood plasma levels of heavy metals and trace elements in white sharks (Carcharodon carcharias) and potential health consequences. Mar Pollut Bull 2019", "10.1016/j.marpolbul.2019.03.018", "31232352", "Marine Pollution Bulletin"),
 pm(19, "Evidence of maternal offloading of organic contaminants in white sharks (Carcharodon carcharias). PLoS One 2013;8(4):e62886", "10.1371/journal.pone.0062886", "23646154", "PLoS One", "PMC3639909"),
 pm(20, "Bioaccumulation of PCBs in liver tissue of dusky Carcharhinus obscurus, sandbar C. plumbeus and white Carcharodon carcharias sharks from south-eastern Australian waters. Mar Pollut Bull 2015;101(2):908-913", "10.1016/j.marpolbul.2015.10.071", "26555794", "Marine Pollution Bulletin"),
 pm(21, "Per/Polyfluoroalkyl Substances (PFASs) in a Marine Apex Predator (White Shark, Carcharodon carcharias) in the Northwest Atlantic Ocean. ACS Environ Au 2024;4(3):152-161", "10.1021/acsenvironau.3c00055", "38765060", "ACS Environmental Au", "PMC11100321"),
 pm(22, "How great white sharks nourish their embryos to a large size: evidence of lipid histotrophy in lamnoid shark reproduction. Biol Open 2016;5(9):1211-1215", "10.1242/bio.017939", "27635035", "Biology Open", "PMC5051657"),
 pm(23, "Mode of uterine milk secretion in the white shark. Anat Rec (Hoboken) 2022;305(7):1724-1731", "10.1002/ar.24860", "34981899", "Anatomical Record"),
 pm(24, "Travelling light: white sharks (Carcharodon carcharias) rely on body lipid stores to power ocean-basin scale migration. Proc Biol Sci 2013;280(1766):20130836", "10.1098/rspb.2013.0836", "23864595", "Proceedings of the Royal Society B", "PMC3730586"),
 pm(25, "High resolution acoustic telemetry reveals swim speeds and inferred field metabolic rates in juvenile white sharks (Carcharodon carcharias). PLoS One 2022;17(6):e0268914", "10.1371/journal.pone.0268914", "35679282", "PLoS One", "PMC9182713"),
 pm(26, "Rapid detection of CITES-listed shark fin species by loop-mediated isothermal amplification assay with potential for field use. Sci Rep 2020;10:4455", "10.1038/s41598-020-61150-8", "32157111", "Scientific Reports", "PMC7064571"),
 pm(27, "A multiplex PCR mini-barcode assay to identify processed shark products in the global trade. PLoS One 2017;12(10):e0185368", "10.1371/journal.pone.0185368", "29020095", "PLoS One", "PMC5636071"),
 pm(28, "Effective number of white shark (Carcharodon carcharias, Linnaeus) breeders is stable over four successive years in the population adjacent to eastern Australia and New Zealand. Ecol Evol 2021;11(1)", "10.1002/ece3.7007", "33437422", "Ecology and Evolution", "PMC7790646"),
 pm(29, "Transcriptome-Derived Microsatellites Demonstrate Strong Genetic Differentiation in Pacific White Sharks. J Hered 2018", "10.1093/jhered/esy045", "30204894", "Journal of Heredity"),
 {"n": 30, "title": "CITES 제13차 당사국총회(CoP13, 2004년 10월, 방콕) 제안서 Prop. 32 — 백상아리(Carcharodon carcharias) 부속서 II 등재(오스트레일리아·마다가스카르 제안, 무기명 투표 찬성 87·반대 34·기권 9로 채택, 그 전 2001년 10월 오스트레일리아가 부속서 III 등재) — WebSearch 검색 결과 요약으로만 확인, 원문은 이 환경에서 열지 못함(cites.org·enb.iisd.org 접속 불가)", "url": "https://cites.org/sites/default/files/eng/cop/13/prop/E13-P32.pdf", "publisher": "CITES 사무국", "accessed": A},
 {"n": 31, "title": "식품의약품안전처 참고자료(최근 임신부의 참치 섭취로 인한 수은의 위해성 논란 관련) — 다랑어류·새치류·심해성 어류 메틸수은 1.0 ppm 관리, 2004–2008년 조사(상어류 36건 등) 기준 초과 없음, 임신부 등은 다랑어류·새치류·심해성 어류만 먹을 때 일주일 100 g 이하 권고 — WebSearch 검색 결과 요약으로만 확인, 원문은 이 환경에서 열지 못함(mfds.go.kr 접속 불가)", "url": "https://www.mfds.go.kr/brd/m_100/view.do?seq=24909", "publisher": "식품의약품안전처", "accessed": A},
 pm(32, "New Evidence for the Contemporary Presence of Juvenile White Sharks (Carcharodon carcharias) in the Adriatic Sea. Fishes 2025;10(1):25", "10.3390/fishes10010025", "40028465", "Fishes", "PMC7617451"),
 pm(33, "A comparison of the heart and muscle total lipid and fatty acid profiles of nine large shark species from the east coast of South Africa. Fish Physiol Biochem 2011;37(1):105-112", "10.1007/s10695-010-9421-8", "20694746", "Fish Physiology and Biochemistry"),
 pm(34, "How much do we know about the parasites of great white sharks (Carcharodon carcharias) and why they matter? Int J Parasitol Parasites Wildl 2025;28:101160", "10.1016/j.ijppaw.2025.101160", "41439034", "IJP: Parasites and Wildlife", "PMC12720348"),
 pm(35, "First evidence of a palaeo-nursery area of the great white shark. Sci Rep 2020;10:8502", "10.1038/s41598-020-65101-1", "32444686", "Scientific Reports", "PMC7244757"),
 pm(36, "Genetic Evidence of Killer Whale Predation on White Sharks in Australia. Ecol Evol 2025;15(1):e70786", "10.1002/ece3.70786", "39872902", "Ecology and Evolution", "PMC11770329"),
 pm(37, "In Troubled Waters: Applying DNA Barcoding to Monitor Singapore's Shark Fin Trade. Ecol Evol 2025;15(6):e71607", "10.1002/ece3.71607", "40552098", "Ecology and Evolution", "PMC12183325"),
]

sections = [
 ("overview", "한눈에 보기",
  "백상아리(Carcharodon carcharias)는 악상어과(Lamnidae)에 드는 대형 상어로, 식약처 「식품원료 목록」에 '백상아리'(영문 Great white shark)라는 원료명으로 올라 있다[1]. 이 목록에서 상태는 '사용가능'이고 사용 부위는 따로 정하지 않은 '-'로 적혀 있으며, 별도의 사용 조건은 없다[1]. 건강기능식품 고시형 원료의 원재료 목록에는 없어 식약처가 정한 지표성분도 없다[1].\n\n"
  "백상아리는 국제자연보전연맹(IUCN) 적색목록에서 전 지구적으로 '취약(Vulnerable)' 종이고, 「멸종위기에 처한 야생동식물종의 국제거래에 관한 협약」(CITES) 부속서 II와 이동성 야생동물 보전 협약(CMS) 부속서 I·II에 올라 있다[5, 8]. 부속서 II 종은 국제 거래가 허가 등으로 통제된다[37]. 또 몸속에 신경독성 메틸수은이 높게 쌓이는 최상위 포식자로, 살(근육)의 총수은이 식품 기준(1 mg/kg 습중량)을 넘는 개체가 여러 바다에서 보고되었다[15, 16]. 국내 공공기관의 백상아리 식품성분표 값과 국내 어획 통계는 이번 조사에서 확인하지 못함."),
 ("history", "이용·연구 역사",
  "백상아리의 학명은 린네가 1758년에 기재한 Carcharodon carcharias (Linnaeus, 1758)로 적힌다[8]. 칠레·페루의 플라이오세 화석 산지 분석에서는 칠레 코킴보 산지에 어린 개체가 많아, 옛 새끼 성육장(팔레오 너서리)의 첫 증거로 보고되었다[35].\n\n"
  "국제 보호는 2000년대 초에 시작되었다[7]. 오스트레일리아가 2001년 10월 CITES 부속서 III에 올린 뒤, 2004년 10월 방콕 제13차 당사국총회에서 오스트레일리아·마다가스카르의 제안(Prop. 32)이 투표로 채택되어 부속서 II에 올랐다(검색 요약으로만 확인)[30]. 2015년 연구는 고래상어·돌묵상어·백상아리를 2000년대 초에 CITES에 오른 세 상어로 꼽았다[7]. 북서태평양 연구(2014)는 한국을 CITES 당사국이지만 CMS 비당사국으로 정리했고, 일본은 백상아리 등재에 유보(reservation)를 두었다고 적었다[5]. 같은 연구는 이 해역의 어느 나라도 백상아리를 완전히 보호하는 국내법을 두지 않은 것으로 보았다[5].\n\n"
  "유럽 아드리아해 동쪽 연안은 한때 어린 백상아리가 자주 보고되던 곳이었지만 20세기 후반부터 크게 줄었다[32]. 국내에서 백상아리를 식용해 온 역사 기록은 공식 자료로 확인하지 못함."),
 ("biology", "어종·생태·번식",
  "백상아리는 온대·아열대·열대 바다에 널리 사는 대형 최상위 포식자로, 최대 크기는 약 6 m로 알려져 있다[5]. 북서태평양 기록에서 믿을 만하게 잰 개체는 몸길이 126–602 cm, 무게 16–2530 kg이었고, 602 cm 개체는 당시 세계에서 가장 크게 측정된 기록이었다[5]. 상어 가운데 가장 큰 '부분 온혈(regional endothermy)' 종이다[25].\n\n"
  "새끼를 몸속에서 키워 낳는 태생이며, 배아는 어미가 낸 영양란을 먹는다(난식)[22]. 오키나와에서 잡힌 4.95 m 임신 개체의 자궁에는 노란 점성 액체가 차 있었고 왼쪽 자궁에서만 79.2 L가 넘었으며, 이 지질이 풍부한 '자궁유'가 난식 이전 배아의 주 영양원으로 제시되었다[22]. 자궁 벽 세포가 지방방울을 품은 채 부서져 내보내는 방식(전분비)으로 이 액체를 만든다는 후속 연구도 있다[23]. 북서태평양 임신 개체는 평균 6.0±2.2마리(최대 10마리)의 배아를 품었고, 임신 기간은 약 20개월로 추정되었다[5].\n\n"
  "간에 저장한 지질은 약 4000 km에 이르는 대양 회유의 에너지원으로 쓰인다[24]. 지방산 조성으로 보면 물고기·연골어류·해양 포유류 지방을 두루 먹는 잡식성 포식자에 가깝다[4]. 북동태평양 개체가 쌓은 메틸수은의 최소 72%는 중층(박광층) 먹이에서 왔다고 추정되었다[13]. 오스트레일리아에서는 범고래가 백상아리를 잡아 간을 골라 먹은 사례가 유전자로 확인되었다[36]. 기생충은 문헌·박물관 기록 116건이 정리되었고 촌충류·요각류가 많았다[34]."),
 ("related_species", "관련 종·이름",
  "식약처 「식품원료 목록」에는 같은 악상어과의 청상아리(Isurus oxyrinchus)와 악상어(Lamna ditropis)가 '사용가능' 원료로 따로 올라 있다[1]. 같은 과의 비악상어(Lamna nasus)는 '식품의 기준 및 규격 개정고시(제2018-8호)에 따라 멸종위기 야생생물을 식품원료로 사용할 수 없도록 금지'라는 조건과 함께 '사용불가'로 적힌 행이 있다[1]. 같은 문구로 미흑점상어(Carcharhinus falciformis)와 장완흉상어(Carcharhinus longimanus)도 '사용불가'로 적혀 있으나, 백상아리 행에는 이런 조건이 적혀 있지 않다[1]. 다만 비악상어와 미흑점상어는 영문명('Porbeagle', 'Silky shark')으로 된 별도 행이 '사용가능'으로도 남아 있다[1]. 목록의 '상어'·'상어간유추출물' 등 일반 상어 원료의 학명은 별상어류(Mustelus manazo, Mustelus griseus)로 적혀 있어 백상아리와는 다른 종이다[1].\n\n"
  "영어로는 great white shark 또는 white shark라 부른다[1, 5]. 2025년 크로아티아 연안에서 잡힌 새끼 백상아리는 처음에 비악상어로 잘못 알려졌다가 바로잡혔을 만큼 악상어과 종끼리는 헷갈리기 쉽다[32]. 북서태평양 연구도 작은 개체는 다른 악상어과 종으로 잘못 기록될 수 있다고 지적했다[5]. 한국어 이름 '백상아리'의 유래를 적은 공식 자료는 확인하지 못함."),
 ("cultivation", "어획·분포",
  "백상아리는 양식되지 않으며, 이를 직접 노리는 어업도 없고 다른 어업에 섞여 잡히는(혼획) 경우가 대부분이다[5]. 1951–2012년 북서태평양 기록 240건은 일본 129건, 대만 45건, 중국 32건, 한국 22건, 러시아 8건, 베트남 3건, 필리핀 1건이었다[5]. 잡힌 방법이 기록된 79건 중 56건이 정치망이었고, 한국·러시아 같은 북쪽 해역에서는 10월–1월에 기록이 없었다[5].\n\n"
  "국내 연구에 따르면 2011–2016년 동해에서 백상아리 5마리가 보고되었고, 2024년 2–11월 고성–울산 연안 조사에서도 1마리가 확인되었다[6]. 이 개체의 근육 안정동위원소 값은 δ13C −16.86‰, δ15N 14.17‰로 함께 조사한 청상아리·악상어·청새리상어보다 높았다[6]. 한국 연안의 상어 관련 사고는 1959–1996년 6건이 보고되었다[6].\n\n"
  "전 세계 개체 수는 1970년대 추정치의 63% 수준으로 줄었고, 유럽에서는 '위급(Critically Endangered)'으로 분류된다[8]. 동부 오스트레일리아–뉴질랜드 개체군의 한 해 번식 기여 개체 수(유효 번식자 수)는 2010–2013년 206.1–252.0으로 안정적이었다[28]. 국내 백상아리 어획량 통계는 확인하지 못함."),
 ("processing", "가공·유통·관련 제품",
  "국제 거래되는 상어 제품은 지느러미·살·간유 등이며, 가공되면 겉모습으로 종을 가리기 어렵다[27]. 지느러미는 아시아 건어물 시장에 들어오면 껍질을 벗기고 약품 처리를 해 형태 특징이 사라지고 DNA도 손상되므로, 짧은 DNA 조각(미니 바코드)으로 백상아리 등 CITES 등재 종을 가리는 검사법이 개발되었다[7]. DNA 추출부터 3시간 안에 CITES 등재 상어 12종을 가려 현장 활용 가능성이 있는 LAMP 검사법도 보고되었다[26].\n\n"
  "식약처 건강기능식품 고시의 스쿠알렌과 알콕시글리세롤 함유 상어간유는 원재료를 '상어 간'으로만 적고 종을 정하지 않는다[2]. 백상아리 간 지질은 약 96%가 중성지방(트라이아실글리세롤)이어서, 다이아실글리세릴 에터와 스쿠알렌이 많은 심해 상어의 간과 다르다[4]. 백상아리 간을 이 원료로 쓴다는 국내 자료는 확인하지 못함.\n\n"
  "「식품 등의 생산실적」 2025년판에서 알콕시글리세롤 함유 상어간유 생산액은 3,140,102천원(약 31.4억 원), 스쿠알렌은 1,669,289천원(약 16.7억 원)이었다[3]. 이 수치는 원료 상어 종을 구분하지 않은 제품 통계다[3]. 남아프리카 대형 상어 9종의 근육은 n-3·n-6 다가불포화지방산이 풍부하지만 요소 같은 대사 노폐물이 많을 수 있다고 지적되었다[33]."),
 ("genetics", "유전체·계통",
  "백상아리 핵 유전체는 4.63 Gbp 크기에 예측 유전자 24,520개, 반복 서열 비율 58.5%로 보고되었다[9]. 상처 치유와 유전체 안정성 관련 유전자에서 양성 선택 흔적이 보였고, 후각 수용체 유전자는 매우 적은 반면 서골비 수용체(V2R) 유전자는 13개였다[9]. 대서양 개체의 미토콘드리아 유전체는 16,745 bp에 단백질 암호화 유전자 13개, tRNA 22개, rRNA 2개를 가진다[10]. 멕시코 과달루페섬 개체의 미토콘드리아 유전체도 16,745 bp로, 앞서 보고된 대만 개체(16,742 bp)와 구조가 비슷했다[11].\n\n"
  "전 세계 시료의 유전체 분석은 북대서양·인도-태평양·북태평양의 세 계통을 구분했고, 이들은 10만–20만 년 전 빙하기에 갈라졌다고 추정했다[8]. 남서태평양과 북동태평양 개체 사이에는 유의한 유전적 분화(FST = 0.083)가 있었다[29]. 일본 개체의 미토콘드리아 DNA는 북동태평양과 분리된 단계통 무리를 이루어, 북서태평양에 따로 사는 하위 개체군이 있음을 뒷받침한다[5]. 한국 해역 개체의 유전 분석 자료는 확인하지 못함."),
 ("safety", "안전성·규제",
  "백상아리는 수명이 길고 먹이사슬 꼭대기에 있어 수은이 쉽게 쌓인다[12]. 북서대서양 개체의 근육 총수은은 평균 10.0 mg/kg(건중량), 혈장은 533 μg/L였고 몸길이가 길수록 높았다[12]. 남아프리카 동부 연안 연구에서 백상아리 근육 총수은은 평균 10 mg/kg(건중량)을 넘었고, 조사한 상어 17종의 70%가 사람 섭취 안전 기준을 넘었다[15]. 오스트레일리아 남동부에서는 조사 개체의 절반 넘게가 오스트레일리아·뉴질랜드 식품 기준(1 mg/kg 습중량)을 넘었고, 지느러미 섬유의 비소도 우려되었다[16]. 오스트랄라시아의 큰 개체는 북동태평양 개체보다 수은이 3배 높았다[14]. 남아프리카 개체의 혈장에서는 수은·비소가 다른 척추동물에서 독성으로 보는 수준으로 나왔지만, 백혈구 수 같은 건강 지표의 이상은 관찰되지 않았다[18].\n\n"
  "어미의 오염물질은 새끼에게 넘어간다[19]. 그해 태어난 새끼 백상아리는 수은·PCB·DDT 농도가 높았고, 남캘리포니아 새끼의 ΣDDT는 95±91 μg/g(습중량)이었다[17, 19]. 간의 PCB 중앙값은 3.35 μg/g(지질)이었고, 과불화화합물(PFAS)도 근육에서 0.20–0.84 ng/g(습중량) 검출되었다[20, 21].\n\n"
  "식약처는 다랑어류·새치류·심해성 어류의 메틸수은을 1.0 ppm으로 관리하고, 임신부 등에게 이런 어류를 일주일 100 g 이하로 먹도록 권고했다(검색 요약으로만 확인)[31]. 백상아리가 이 '심해성 어류' 기준에 드는지와 국내 수입·유통 허가 절차는 확인하지 못함. 백상아리 알레르기에 관한 공공기관 자료도 확인하지 못함."),
]

compounds = [
 ("Triacylglycerol", "트라이아실글리세롤(중성지방)", "지질 분류", "nutrient", "간", "간 총지질의 96.3±0.9%; 간 총지질 51.6–70.4%(습중량)[4]", "간에 저장되어 회유·번식의 에너지원과 부력 유지에 쓰임[4, 24]", [4, 24]),
 ("Phospholipids", "인지질", "지질 분류", "nutrient", "근육", "근육 총지질의 92.4±4.8%; 근육 총지질 0.7±0.1%(습중량)[4]", "세포막 구조 지질로, 근육 지질의 대부분을 차지함[4]", [4]),
 ("Sterols", "스테롤", "지질 분류", "nutrient", "근육·간", "근육 총지질의 6.1±4.1%, 간 0.4±0.4%[4]", "막 구조 성분(개별 스테롤 이름은 원문에 없음)[4]", [4]),
 ("Docosahexaenoic acid", "도코사헥사엔산(DHA, 22:6ω3)", "오메가-3 지방산", "nutrient", "근육·간", "총지방산 대비 근육 15.52±6.68%, 간 13.62±6.34%[4]", "근육에서 두 번째로 많은 지방산이며 먹이(어류·두족류) 지표로 쓰임[4]", [4]),
 ("Eicosapentaenoic acid", "에이코사펜타엔산(EPA, 20:5ω3)", "오메가-3 지방산", "nutrient", "근육·간", "총지방산 대비 근육 1.63±1.05%, 간 2.31±0.81%[4]", "해양 포유류 지방에 많은 지방산으로 먹이 구성 해석에 쓰임[4]", [4]),
 ("Docosapentaenoic acid", "도코사펜타엔산(DPA, 22:5ω3)", "오메가-3 지방산", "nutrient", "근육·간", "총지방산 대비 근육 2.75±1.40%, 간 3.40±1.02%[4]", "오메가-3 계열 장쇄 다가불포화지방산[4]", [4]),
 ("Arachidonic acid", "아라키돈산(20:4ω6)", "오메가-6 지방산", "nutrient", "근육·간", "총지방산 대비 근육 9.22±3.93%, 간 4.86±5.42%[4]", "다른 대양성 상어 보고값의 최상단 범위로, 연안·저서 먹이 기여를 시사함[4]", [4]),
 ("Palmitic acid", "팔미트산(16:0)", "포화지방산", "nutrient", "근육·간", "총지방산 대비 근육 18.55±3.48%, 간 18.42±2.29%[4]", "근육·간 모두에서 가장 많은 지방산[4]", [4]),
 ("Stearic acid", "스테아르산(18:0)", "포화지방산", "nutrient", "근육·간", "총지방산 대비 근육 13.79±3.64%, 간 8.70±3.93%[4]", "개체군 내 먹이 차이를 가르는 지방산 가운데 하나[4]", [4]),
 ("Oleic acid", "올레산(18:1ω9)", "단일불포화지방산", "nutrient", "근육·간", "총지방산 대비 근육 11.90±4.38%, 간 16.19±5.49%[4]", "해양 포유류 지방(블러버)에 많아 포유류 먹이 섭취 지표로 해석됨[4]", [4]),
 ("cis-Vaccenic acid", "시스-박센산(18:1ω7)", "단일불포화지방산", "nutrient", "근육·간", "총지방산 대비 근육 6.25±1.50%, 간 5.96±1.16%[4]", "다랑어류보다 백상아리에 많은 지방산으로 보고됨[4]", [4]),
 ("Palmitoleic acid", "팔미톨레산(16:1ω7)", "단일불포화지방산", "nutrient", "근육·간", "총지방산 대비 근육 2.13±1.81%, 간 6.72±5.72%[4]", "규조류 기반 먹이사슬·포유류 지방 지표로 쓰임[4]", [4]),
]
compounds = [dict(name=a, name_ko=b, **{"class": c}, role=d, part=e, content_text=f, activity_ko=g, source=h) for a,b,c,d,e,f,g,h in compounds]

E = {k: "" for k in ["instrument","column","mobile_phase","gradient","flow","temp","detection","injection","sample_prep","standard","linearity","lod","loq","recovery"]}
def cond(**kw):
    d = dict(E); d.update(kw); return d
assays = [
 {"role": "literature", "compound": "Fatty acid methyl esters (DHA, EPA, arachidonic acid etc.)", "compound_ko": "지방산 조성(DHA·EPA·아라키돈산 등)", "part": "근육·간",
  "content": "총지방산 대비 근육 DHA 15.52±6.68%, EPA 1.63±1.05%, 아라키돈산 9.22±3.93%; 간 DHA 13.62±6.34%, EPA 2.31±0.81%(근육 n=21, 간 n=7)[4]", "method": "GC-FID(확인 GC-MS)",
  "conditions": cond(instrument="Agilent 7890B 가스크로마토그래프, 불꽃이온화검출기, splitless 주입구, 7683B 자동주입기; 피크 확인은 Thermoquest DSQ GC-MS", column="Equity-1 용융 실리카 모세관 칼럼, 15 m × 0.1 mm, 막 두께 0.1 μm", mobile_phase="운반 기체 헬륨", gradient="120 °C 주입 → 10 °C/분으로 270 °C → 5 °C/분으로 310 °C", detection="FID", injection="0.2 μL, splitless", sample_prep="습조직 20–50 mg을 메탄올:다이클로로메테인:진한 염산(10:1:1) 혼합액으로 80 °C 2시간 직접 메틸에스터화 → 물 1.5 mL와 내부표준 23:0 FAME 첨가 → 2000 rpm 5분 원심 → 위 유기층을 질소로 농축", standard="내부표준 23:0 지방산 메틸에스터; 결과는 총지방산 대비 면적 %"),
  "rationale": "지방산 조성은 먹이(어류·두족류 대 해양 포유류 지방)와 영양 상태를 추정하는 지표로 쓰였다[4]. PMC 전문(Methods) 확인 — 검출·정량한계·회수율은 본문에 없음[4].", "source": [4], "url": "https://doi.org/10.1371/journal.pone.0097877", "source_kind": "paper"},
 {"role": "literature", "compound": "Lipid classes (triacylglycerol, phospholipid, sterol, wax ester, free fatty acid)", "compound_ko": "지질 분류 조성(중성지방·인지질 등)", "part": "근육·간",
  "content": "간: 트라이아실글리세롤 96.3±0.9%, 인지질 1.9±1.0%; 근육: 인지질 92.4±4.8%, 스테롤 6.1±4.1%(총지질 대비); 총지질 근육 0.7±0.1%·간 61.0±13.3%(습중량)[4]", "method": "TLC-FID(Iatroscan)",
  "conditions": cond(instrument="Iatroscan Mark V TH10 박층크로마토그래프-불꽃이온화검출기(TLC-FID), SIC-480 소프트웨어로 정량", mobile_phase="극성 전개용매 헥세인:다이에틸 에터:빙초산 70:10:0.1(v/v/v); 탄화수소(스쿠알렌 포함)·왁스에스터·다이아실글리세릴 에터 분리용 비극성 용매 헥세인:에터 96:4(v/v)", detection="FID", sample_prep="근육 0.05–0.08 g·간 0.03–0.05 g을 −20 °C 보관 → 변형 Bligh & Dyer 단상 추출(CHCl3:MeOH:물 10:20:7.5 mL, 하룻밤) → CHCl3 10 mL·식염수 10 mL로 2상 분리 → 하층 회전증발 농축 → 질소 건조 후 칭량; 크로마로드는 100 °C 10분 건조 후 즉시 분석", standard="주요 지질 분류의 양을 아는 표준 용액과 함께 시료를 2회 반복 분석"),
  "rationale": "간 지질의 분류 조성은 에너지 저장(중성지방)과 부력(스쿠알렌·다이아실글리세릴 에터)의 역할을 가르는 지표로 쓰였다[4]. PMC 전문(Methods) 확인 — 검출·정량한계·회수율은 본문에 없음[4].", "source": [4], "url": "https://doi.org/10.1371/journal.pone.0097877", "source_kind": "paper"},
 {"role": "literature", "compound": "Total mercury", "compound_ko": "총수은", "part": "근육·혈장",
  "content": "북서대서양 근육 평균 10.0 mg/kg(건중량), 혈장 평균 533 μg/L[12]; 남아프리카 근육 평균 10 mg/kg(건중량) 초과[15]; 오스트레일리아 남동부 조사 개체의 50% 넘게 1 mg/kg(습중량) 초과[16]", "method": "총수은 정량(분석 기기·조건은 원문 미확인)",
  "conditions": cond(),
  "rationale": "메틸수은은 먹이사슬을 따라 농축되는 신경독성 물질로, 최상위 포식자인 백상아리에서 섭취 안전성과 개체 건강을 판단하는 핵심 지표로 쓰였다[12, 13, 15]. 전문 확인 못함 — 세 논문 모두 PMC 전문이 없어 초록만 확인했고 분석 조건은 비워 둠[12, 15, 16].", "source": [12, 15, 16, 13], "url": "https://doi.org/10.1016/j.marpolbul.2023.115533", "source_kind": "paper"},
]

d = {
 "slug": "carcharodon-carcharias", "name_ko": "백상아리", "name_en": "Great white shark",
 "scientific_name": "Carcharodon carcharias (Linnaeus, 1758)",
 "aliases": ["백상아리", "Great white shark", "White shark"],
 "sections": [{"key": k, "title": t, "body": b} for k, t, b in sections],
 "compounds": compounds, "markers": [], "assays": assays, "nutrients": [], "production": [], "world": [],
 "gi": [], "orgs": [], "sources": S,
}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for k, t, b in sections: print(k, len(b))
