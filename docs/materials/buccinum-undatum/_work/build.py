import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
A = "2026-11-02"
def pm(n, title, doi, pub, pmc=None):
    return {"n": n, "title": title, "url": f"https://doi.org/{doi}", "publisher": pub + (f", {pmc}" if pmc else ""), "accessed": A}
sources = [
 {"n": 1, "title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 유럽물레고둥(Buccinum undatum) 항목 및 같은 목록의 물레고둥류 항목", "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
 pm(2, "RAD sequencing of common whelk, Buccinum undatum, reveals fine-scale population structuring in Europe and cryptic speciation within the North Atlantic. Ecol Evol 2021;11(6):2616-2629", "10.1002/ece3.7219", "Ecology and Evolution (Wiley), PubMed 33767824", "PMC7981227"),
 pm(3, "Limited Dispersal Drives Strong Genetic Structure in the Commercially Harvested Gastropod Buccinum undatum in the Western North Atlantic. Evol Appl 2026;19(2):e70207", "10.1111/eva.70207", "Evolutionary Applications (Wiley), PubMed 41640799", "PMC12865132"),
 pm(4, "Shell morphology and color of the subtidal whelk Buccinum undatum exhibit fine-scaled spatial patterns. Ecol Evol 2018;8(9):4552-4563", "10.1002/ece3.4015", "Ecology and Evolution (Wiley), PubMed 29760896", "PMC5938454"),
 pm(5, "Common whelk (Buccinum undatum) allergy: identification of IgE-binding components and effects of heating and digestive enzymes. J Korean Med Sci 2004;19(6):793-799", "10.3346/jkms.2004.19.6.793", "Journal of Korean Medical Science, PubMed 15608387", "PMC2816299"),
 pm(6, "Arsenic concentration and speciation of the marine hyperaccumulator whelk Buccinum undatum collected in coastal waters of Northern Britain. J Environ Monit 2010;12(5):1126-1132 (초록 확인)", "10.1039/b924351h", "Journal of Environmental Monitoring (RSC), PubMed 21491679"),
 pm(7, "Bioaccessibility of essential and non-essential metals in commercial shellfish from Western Europe and Asia. Food Chem Toxicol 2008;46(6):2010-2022 (초록 확인)", "10.1016/j.fct.2008.01.041", "Food and Chemical Toxicology (Elsevier), PubMed 18329777"),
 pm(8, "Screening of polycyclic aromatic hydrocarbons in multiple fish species and common whelk in the Faroe Islands using a modified QuEChERS method. Environ Sci Pollut Res Int 2025;32(43):24858-24868", "10.1007/s11356-025-37058-z", "Environmental Science and Pollution Research (Springer), PubMed 41120798", "PMC12594697"),
 pm(9, "Performance Characteristics of Refined LC-FLD and HILIC-MS/MS Methods for the Determination of Paralytic Shellfish Toxins in Shrimp, Whelk, and Crab. J AOAC Int 2021;104(4):1022-1035 (초록 확인)", "10.1093/jaoacint/qsab028", "Journal of AOAC International (Oxford), PubMed 33681973"),
 pm(10, "Tenderization effect of whelk meat using ultrasonic treatment. Food Sci Nutr 2018;6(7):1848-1857", "10.1002/fsn3.686", "Food Science & Nutrition (Wiley), PubMed 30349674", "PMC6189613"),
 pm(11, "Imposex and organotin concentrations in Buccinum undatum and Neptunea antiqua from the North Sea: relationship to shipping density and hydrographical conditions. Mar Environ Res 2003;55(3):203-233 (초록 확인)", "10.1016/s0141-1136(02)00217-9", "Marine Environmental Research (Elsevier), PubMed 12688240"),
 pm(12, "Imposex induction in laboratory reared juvenile Buccinum undatum by tributyltin (TBT). Environ Toxicol Pharmacol 2002;11(1):49-65 (초록 확인)", "10.1016/s1382-6689(01)00106-5", "Environmental Toxicology and Pharmacology (Elsevier), PubMed 21782586"),
 pm(13, "Occurrence and effects of organotins on adult common whelk (Buccinum undatum) in harbours and in a simulated dredging situation. Mar Pollut Bull 2001;42(5):370-376 (초록 확인)", "10.1016/s0025-326x(00)00164-8", "Marine Pollution Bulletin (Elsevier), PubMed 11436817"),
 pm(14, "Butyltin species in benthic and pelagic organisms of the Saguenay Fjord (Canada) and imposex occurrence in common whelk (Buccinum undatum). Arch Environ Contam Toxicol 2006;50(1):45-59 (초록 확인)", "10.1007/s00244-004-0198-6", "Archives of Environmental Contamination and Toxicology (Springer), PubMed 16237495"),
 pm(15, "Levels of polybrominated diphenyl ether (PBDE) flame retardants in animals representing different trophic levels of the North Sea food web. Environ Sci Technol 2002;36(19):4025-4032 (초록 확인)", "10.1021/es0158298", "Environmental Science & Technology (ACS), PubMed 12380070"),
 pm(16, "Bioaccumulation and biotransformation of pyrene and 1-hydroxypyrene by the marine whelk Buccinum undatum. Environ Toxicol Chem 2010;29(4):779-788 (초록 확인)", "10.1002/etc.112", "Environmental Toxicology and Chemistry (Wiley), PubMed 20821506"),
 {"n": 17, "title": "[About effect of habitat and motor activity of molluscs on fatty acid composition of triglycerides and phospholipids]. Zh Evol Biokhim Fiziol 2009;45(1):46-52 (러시아어 논문, 영문 초록 확인)", "url": "https://pubmed.ncbi.nlm.nih.gov/19370988/", "publisher": "Zhurnal Evoliutsionnoi Biokhimii i Fiziologii, PubMed 19370988", "accessed": A},
 {"n": 18, "title": "[Significance of electron interactions of fatty acids of phospholipid molecules in the organism adaptation to habitation temperature]. Zh Evol Biokhim Fiziol 2009;45(4):368-373 (러시아어 논문, 영문 초록 확인)", "url": "https://pubmed.ncbi.nlm.nih.gov/19764632/", "publisher": "Zhurnal Evoliutsionnoi Biokhimii i Fiziologii, PubMed 19764632", "accessed": A},
 pm(19, "The subtle intracapsular survival of the fittest: maternal investment, sibling conflict, or environmental effects? Ecology 2013;94(10):2263-2274 (초록 확인)", "10.1890/12-1701.1", "Ecology (ESA), PubMed 24358712"),
 pm(20, "The secret to successful deep-sea invasion: does low temperature hold the key? PLoS One 2012;7(12):e51219 (초록 확인)", "10.1371/journal.pone.0051219", "PLoS One, PubMed 23227254", "PMC3515517"),
 pm(21, "Commercially important species associated with horse mussel (Modiolus modiolus) biogenic reefs: A priority habitat for nature conservation and fisheries benefits. Mar Pollut Bull 2017;118(1-2):71-78 (초록 확인)", "10.1016/j.marpolbul.2017.02.051", "Marine Pollution Bulletin (Elsevier), PubMed 28222862"),
 pm(22, "Aggregation of whelks, Buccinum undatum, near feeding predators: the role of reproductive requirements. Anim Behav 2001;61(1):31-41 (초록 확인)", "10.1006/anbe.2000.1555", "Animal Behaviour (Elsevier), PubMed 11170694"),
 pm(23, "Impact of a castrating trematode, Neophasis sp., on the common whelk, Buccinum undatum, in the northern Gulf of St. Lawrence. Biol Bull 2000;198(2):261-271 (초록 확인)", "10.2307/1542529", "The Biological Bulletin, PubMed 10786946"),
 pm(24, "A case report and statewide surveillance of 'weak meat' condition of Alaska weathervane scallops, Patinopecten caurinus, linked to a recently identified pathogenic parasite, Merocystis kathae. J Invertebr Pathol 2021;185:107668 (초록 확인)", "10.1016/j.jip.2021.107668", "Journal of Invertebrate Pathology (Elsevier), PubMed 34555364"),
 pm(25, "Excitation evoked by FMRFamide and FLRFamide in the heart of Buccinum undatum and evidence for inositol 1,4,5-trisphosphate as an RF-tetrapeptide second messenger. J Comp Physiol B 2000;170(5-6):351-356 (초록 확인)", "10.1007/s003600000110", "Journal of Comparative Physiology B (Springer), PubMed 11083516"),
 pm(26, "Immunohistochemical localization of hepatopancreatic phospholipase in gastropods mollusc, Littorina littorea and Buccinum undatum digestive cells. Lipids Health Dis 2011;10:219 (초록 확인)", "10.1186/1476-511X-10-219", "Lipids in Health and Disease (BMC), PubMed 22114916"),
 pm(27, "The seasonality and role of the neurotoxin tetramine in the salivary glands of the red whelk Neptunea antiqua (L.). Toxicon 2002;40(4) (초록 확인; 이 종이 아닌 Neptunea antiqua 자료)", "10.1016/s0041-0101(01)00211-2", "Toxicon (Elsevier), PubMed 11738235"),
 {"n": 28, "title": "[Lipids composition and speed of energy metabolism in gastropods]. Zh Obshch Biol 2008;69(6):471-478 (러시아어 논문, 영문 초록 확인)", "url": "https://pubmed.ncbi.nlm.nih.gov/19140337/", "publisher": "Zhurnal Obshchei Biologii, PubMed 19140337", "accessed": A},
]

S = {}
S["overview"] = ("유럽물레고둥(Buccinum undatum)은 물레고둥과(Buccinidae) 물레고둥속에 드는 바다 고둥으로, 식약처 「식품원료 목록」에 대표 원료명 '유럽물레고둥', 영문명 'Whelk'로 올라 있다[1]. "
 "이 목록에서 분류는 '식품원료(A코드)'의 수산물이고, 사용 조건 상태는 '사용가능'이며, 부위 칸은 '-'로 적혀 있고 별도의 사용 조건 문구는 없다[1]. "
 "건강기능식품 고시형 원료의 원재료는 아니어서 식약처가 정한 지표성분은 없다[1]. "
 "영어로는 common whelk 또는 waved whelk라 부르며, 북대서양 고위도 해역에 넓게 사는 상업 어획 대상종이다[2, 3]. "
 "국내 연구는 이 종을 한국에서 인기 있는 식용 패류로 소개하고, 유럽산 이 종의 주요 시장이 한국과 일본이라고 적었다[5]. "
 "이 종에 관한 연구는 개체군 유전 구조, 환경오염물질(유기주석·비소·카드뮴·다환방향족탄화수소)의 축적, 알레르기 항원에 많이 몰려 있다[2, 5, 6, 7, 8, 11].")
S["history"] = ("이 종은 성숙이 늦고 성체가 대체로 한곳에 머물며 체내수정과 직접발생을 하는, 상업적 가치가 큰 신복족류로 소개된다[2]. "
 "2004년 국내 논문은 유럽산 이 종 어업의 주요 시장이 한국과 일본이고, 2001년 한국의 이 종 수입량이 12,639 t이었다고 다른 자료를 인용해 적었다[5]. "
 "이 수입량은 그 논문이 인용한 값이며, 원 통계 자료는 확인하지 못함. "
 "캐나다 동부에서는 이 종이 상업 어업의 대상이며, 어획량과 단위노력당 어획량이 줄어 국지적 남획에 대한 우려가 제기되었다[3]. "
 "네덜란드 연안에서 보고된 이 종의 감소와 관련해 유기주석 화합물의 영향을 살핀 실험 연구도 있었다[12]. "
 "또 가리비 관자에 병을 일으키는 정단복합충류 기생충 Merocystis kathae는 100여 년 전 이 종에서 처음 기재되었다[24].")
S["biology"] = ("유럽물레고둥은 물레고둥과(Buccinidae)의 조하대 고둥으로, 북아메리카 동부에서 서유럽까지, 그리고 그린란드·아이슬란드·노르웨이해에 이르는 북대서양 고위도 해역에 산다[2]. "
 "알은 해저의 알주머니(난낭) 속에서 자라고, 떠다니는 유생 단계 없이 작은 성체 모양으로 부화한다[3]. "
 "알주머니 안에는 영양란(nurse egg)이 있어 배아끼리 영양을 다투며, 수온이 높을수록 부화 개체 수가 줄고 영양을 받지 못한 '빈 배아'가 늘었다[19]. "
 "캐나다 집단의 산란기는 5–7월, 유럽 집단은 9–2월로 다르다고 정리되었다[2]. "
 "캐나다 연구는 수명을 약 15년, 성숙 나이를 약 5–7년으로 인용했다[3]. "
 "육식성으로, 캐나다 밍간 제도에서는 포식자 불가사리(Leptasterias polaris)를 피하면서도 산란 전 암컷이 먹이를 얻으려 그 곁에 모이는 행동이 관찰되었다[22]. "
 "소화샘 중성지방에 리놀레산이 거의 없어(0.8% 미만) 초식성 고둥과 구별되었다[17]. "
 "심장은 FMRFamide·FLRFamide 같은 RF아마이드 신경펩타이드에 반응해 흥분했고[25], 소화샘 세포에서는 인지질 분해효소(PLA2)가 확인되었다[26]. "
 "백해 시료 비교에서 이 종 같은 해양 고둥은 담수 고둥보다 발 근육 인지질이 많았다[28]. "
 "성숙 개체는 생식소를 차지하는 흡충(Neophasis sp.)에 감염되기도 하며, 감염률은 성숙 암컷 23%, 성숙 수컷 15%였다[23].")
S["related_species"] = ("식약처 「식품원료 목록」에는 같은 속의 물레고둥(Buccinum striatissimum), 고운띠물레고둥(Buccinum bayani), 세고리물레고둥(Buccinum opisoplectum)이 각각 별도 원료로 올라 있어, 이 문서에는 그 종들의 자료를 섞지 않았다[1]. "
 "목록에서 '유럽물레고둥'이라는 국문명은 이 종에만 붙어 있으며, 이 이름의 유래를 적은 공식 자료는 확인하지 못함. "
 "북해에서는 같은 물레고둥과의 Neptunea antiqua(영문 red whelk)가 이 종과 함께 채집되며, 두 종 모두 유기주석에 따른 임포섹스가 조사되었고 그 정도는 N. antiqua에서 더 컸다[11]. "
 "N. antiqua의 침샘에는 신경독 테트라민이 계절에 따라 검출되지 않는 수준에서 6530 μg/g까지 들어 있다고 보고되었으나, 이는 이 종이 아닌 Neptunea 속 자료다[27]. "
 "알레르기 연구에서는 이 종 추출물에 대한 IgE 결합이 전복 추출물로 억제되어 두 고둥 사이의 교차 반응 가능성이 제시되었다[5]. "
 "영문명으로는 common whelk 외에 waved whelk, northern whelk, European whelk가 쓰인다[3, 5, 6].")
S["cultivation"] = ("이 종은 북대서양 전역에서 상업 어업의 대상이며, 국내에서 이 종을 기르거나 잡은 생산 통계는 공식 자료에서 확인하지 못함[3]. "
 "유생 단계가 없는 직접발생종이라 분산 능력이 낮고, 한 지역 개체군이 줄면 이웃 지역에서 채워지기 어려워 국지적 남획에 약하다고 평가된다[3]. "
 "캐나다 연구는 수심이 깊은 해역이 유전자 흐름을 막아 50 km 이내 떨어진 집단끼리도 유전적으로 갈라졌다며, 어업 관리를 지역 단위로 해야 한다고 제안했다[3]. "
 "영국 세 해역 조사에서 이 종은 말털담치(Modiolus modiolus) 군락에서 다른 서식지보다 최대 20배까지 많았다[21]. "
 "이 종의 양식 생산이나 어획량 통계(국가별 t)는 이번 조사에서 공식 자료로 확인하지 못함. "
 "북해에서는 선박 통행이 많고 수층이 연중 섞이는 해역에서 이 종의 유기주석 체내 농도와 임포섹스 지수가 가장 높았다[11]. "
 "캐나다 사그네 피오르에서는 항구에 가까운 지점의 이 종 임포섹스 비율이 52.6%로, 만 입구(12.5%)보다 높았다[14].")
S["processing"] = ("이 종의 살은 고무처럼 질긴 식감이 소비를 막는 요인으로 꼽히며, 이를 줄이는 연육 처리가 연구되었다[10]. "
 "중국 연구에서 냉동 고둥 살에 초음파를 200 W, 9.6분, 45 ℃로 처리하자 전단력이 55.17% 줄었고, 같은 연구에서 파파인과 브로멜라인 처리는 각각 44.52%, 41.27% 줄였다[10]. "
 "초음파 처리한 살은 0 ℃ 저장 중 pH 상승과 총균수 증가가 대조군보다 느렸고 지질 산화(TBARS)는 차이가 없었다[10]. "
 "이 논문은 시료 종을 키워드에서 Buccinum undatum으로 밝혔으나 시료는 가공업체에서 받은 냉동 고둥 살이었다[10]. "
 "조리는 이 종 같은 고둥류에서 은을 제외한 금속의 생체접근률(소화액에 녹아나는 비율)을 낮췄다[7]. "
 "알레르기 항원 단백질의 소화성은 100 ℃ 5분 가열 뒤에도 바뀌지 않았다[5]. "
 "건강기능식품 원료로 이 종을 쓴 제품 생산실적은 확인하지 못함.")
S["genetics"] = ("RAD 시퀀싱으로 얻은 중립 SNP 35,518개를 분석한 결과, 캐나다 집단과 유럽(아이슬란드·페로 제도·잉글랜드) 집단 사이의 유전적 분화 지수(FST)는 모든 쌍에서 0.57을 넘어 두 계통을 서로 다른 은밀종으로 볼 수 있다는 결론이 나왔다[2]. "
 "앞선 미토콘드리아 COI 연구에서도 동·서 북대서양 두 계통이 약 210만 년 전 갈라진 것으로 추정되었다[2]. "
 "유럽 계통 안에서는 거리에 따라 분화가 커지는 약한 구조가 있었고, 아이슬란드에서는 유전 구조가 껍데기 모양·색 빈도와 유의하게 상관했다[2, 4]. "
 "캐나다 북서대서양에서는 431개체를 SNP 23,405개로 분석해 다섯 개의 큰 유전 집단과 그 안의 하위 구조를 찾았다[3]. "
 "이 분석 과정에서 형태로는 이 종으로 분류된 일부 개체가 다른 물레고둥과 종으로 확인되어 제외되었다[3]. "
 "온대와 아한대 해역 집단의 알덩이를 비교한 실험에서는 저온에 순응한 집단의 압력 내성이 더 높아 집단 사이 생리적 차이가 확인되었다[20]. "
 "이 종의 염색체 수준 핵 유전체 조립 자료는 이번 조사에서 확인하지 못함.")
S["safety"] = ("국내 알레르기 클리닉 환자 1,700명의 피부단자시험에서 4.9%(83명)가 이 종에 양성이었고, 양성자 62명 가운데 38.7%가 특이 IgE 양성이었다[5]. "
 "IgE 결합 단백질은 40·71·82 kDa 세 가지였으며, 전복과 교차 반응 가능성이 보였다[5]. "
 "영국 북부 10곳에서 잡은 이 종의 총 비소는 건조중량 기준 45–655 mg/kg이었으나 무기비소는 0.4 mg/kg을 넘지 않았고 주성분은 독성이 낮은 아르세노베타인이었다[6]. "
 "프랑스·영국·홍콩의 시판 연체동물 7종 비교에서 이 종은 카드뮴과 아연의 총농도가 가장 엄격한 식품 기준을 넘었고, 소화액에 녹는 카드뮴도 기준보다 높았다[7]. "
 "잉글랜드에서는 이 종을 포함한 비이매패류의 마비성 패독 감시가 이루어지며, 이에 맞춘 시험법이 검증되었다[9]. "
 "이 종의 침샘 테트라민 함량을 직접 잰 자료는 확인하지 못함. "
 "식약처 「식품원료 목록」에 이 종의 별도 섭취 주의 문구는 없다[1].")
sections = [
 {"key": "overview", "title": "한눈에 보기", "body": S["overview"]},
 {"key": "history", "title": "이용 역사", "body": S["history"]},
 {"key": "biology", "title": "종·형태·생태", "body": S["biology"]},
 {"key": "related_species", "title": "관련 종·이름", "body": S["related_species"]},
 {"key": "cultivation", "title": "어획·자원", "body": S["cultivation"]},
 {"key": "processing", "title": "가공·조리 연구", "body": S["processing"]},
 {"key": "genetics", "title": "유전 정보", "body": S["genetics"]},
 {"key": "safety", "title": "안전성", "body": S["safety"]},
]
def c(name, ko, cls, role, part, txt, act, src):
    return {"name": name, "name_ko": ko, "class": cls, "role": role, "part": part, "content_text": txt, "activity_ko": act, "source": src}
compounds = [
 c("Arsenobetaine", "아르세노베타인", "유기비소 화합물", "other", "연체부(원문 부위 구분 초록에 없음)", "총 비소의 주성분(정량값은 초록에 없음; 영국 북부 연안 시료)", "독성이 낮은 것으로 여겨지는 비소 형태로, 이 종 비소의 주된 화학종이었다[6]", [6]),
 c("Arsenic", "비소(총)", "원소", "toxicant", "연체부(원문 부위 구분 초록에 없음)", "45–655 mg/kg 건조중량(d.w.), 영국 북부 연안 10곳 시료, 지점 간 평균 3.5배 차이", "지점마다 크게 달랐고, 크기와의 관계도 지점에 따라 달랐다[6]", [6]),
 c("Inorganic arsenic", "무기비소", "원소(무기 형태)", "toxicant", "연체부(원문 부위 구분 초록에 없음)", "0.4 mg/kg 건조중량(d.w.) 이하", "총 비소나 크기로는 무기비소 노출량을 추정할 수 없다고 보고되었다[6]", [6]),
 c("Cadmium", "카드뮴", "원소", "toxicant", "연체부(초록에 부위 명시 없음)", "총농도가 가장 엄격한 식품 기준 초과(수치는 초록에 없음)", "소화액에 녹아나는 농도도 기준보다 높았고, 조리하면 생체접근률이 낮아졌다[7]", [7]),
 c("Zinc", "아연", "원소", "nutrient", "연체부(초록에 부위 명시 없음)", "총농도가 가장 엄격한 식품 기준 초과(수치는 초록에 없음)", "소화액에 녹아나는 농도는 기준 아래였다[7]", [7]),
 c("Tributyltin", "트라이뷰틸주석(TBT)", "유기주석 화합물", "toxicant", "전신", "체내 농도 수치는 초록에 없음; 실험에서 수중 7 ng Sn/L 초과 노출 시 어린 개체에 임포섹스 유발", "어린 개체에서 수컷 생식기관 발달(임포섹스)을 용량 의존적으로 일으켰고 성장도 줄였다(사육 실험)[12]", [12, 13]),
 c("Triphenyltin", "트라이페닐주석(TPT)", "유기주석 화합물", "toxicant", "전신", "생물-퇴적물 축적계수(BSAF) 평균 17(북해 시료, 지질·유기탄소 보정)", "부틸주석보다 체내 축적 경향이 컸다[11]", [11]),
 c("Monobutyltin", "모노뷰틸주석(MBT)", "유기주석 화합물(대사물)", "toxicant", "전신", "체내 농도가 TBT보다 높았음(수치는 초록에 없음)", "TBT의 대사물로, 다이뷰틸주석과 함께 체내에 더 많이 남았다[11]", [11]),
 c("Anthracene", "안트라센", "다환방향족탄화수소", "toxicant", "내장 덩어리·생식소", "평균 4.3 ng/g 습중량(ww), 페로 제도 토르스하운 항구 시료", "이 종에서 비교적 높게 검출된 다환방향족탄화수소였다[8]", [8]),
 c("Pyrene", "피렌", "다환방향족탄화수소", "toxicant", "근육·내장", "실험 노출 시 체내 부하의 2–3%만 근육, 나머지는 내장(대사물 포함)", "먹이로 노출된 개체에서 대사물이 검출 물질의 90% 이상이었고 근육보다 내장에 몰렸다(노출 실험)[16]", [16]),
 c("Eicosapentaenoic acid", "에이코사펜타엔산(EPA)", "오메가-3 지방산", "nutrient", "소화샘·발 근육", "이 종 단독 수치 확인하지 못함(원문은 이 종과 Littorina littorea 두 해양종을 묶어 지방산 합계의 22–25%로 보고)", "해양 고둥의 세포막 점성을 낮추는 주요 지방산으로 논의되었다[17]", [17]),
 c("Docosahexaenoic acid", "도코사헥사엔산(DHA)", "오메가-3 지방산", "nutrient", "근육 인지질", "검출(수치는 초록에 없음)", "초식성 담수 고둥과 달리 육식성인 이 종의 근육 인지질에서 검출되었다[18]", [18]),
 c("Linoleic acid", "리놀레산", "오메가-6 지방산", "nutrient", "소화샘 중성지방", "0.8% 미만(지방산 조성 비율)", "초식성 고둥(8–12%)과 달리 거의 없어 육식성 식성을 반영했다[17]", [17]),
 c("Polybrominated diphenyl ethers", "폴리브롬화다이페닐에테르(PBDE)", "브롬계 난연제", "toxicant", "연체부", "수치는 초록에 없음; 주요 동족체 BDE 28·47·99·100·153·154 검출", "북해에서 오염 분포를 보여 주는 지표 무척추동물로 쓰였다[15]", [15]),
]
assays = [
 {"role": "literature", "compound": "Polycyclic aromatic hydrocarbons (16 US EPA PAHs)", "compound_ko": "다환방향족탄화수소(16종)", "part": "내장 덩어리·생식소",
  "content": "안트라센 평균 4.3 ng/g 습중량(토르스하운); 결론부는 이 종의 ∑PAHs를 11 ng/g로 적었으나 초록은 같은 값(11 ± 2 ng/g)을 참가자미류(common dab)로 적어 원문 안에서 엇갈림 [8]",
  "method": "변형 QuEChERS 추출 + GC–MS(EI, SIM)",
  "conditions": {"instrument": "Agilent 6890N-5975B GC–MS, 전자이온화 70 eV", "column": "ZB-5 30 m × 0.25 mm, 막 두께 0.25 μm (Phenomenex)", "mobile_phase": "운반기체 헬륨 1.1 mL/min", "gradient": "50 ℃ 2분 → 25 ℃/분으로 315 ℃ → 8.0분 유지(총 30분)", "flow": "1.1 mL/min", "temp": "", "detection": "SIM, m/z 128–288 범위 13개 이온, 12개 머무름 시간 구간, 이온당 20 ms", "injection": "1 μL splitless",
   "sample_prep": "내장 덩어리 혼합 시료 2 g(습중량) + 물 2 mL + 아세토니트릴 4 mL, 5분 와류; 황산마그네슘 1.6 g·염화나트륨 0.4 g·구연산수소나트륨 0.2 g·구연산나트륨 0.4 g 첨가, 5분 와류, 2000 rpm 10분 원심; 상층 2 mL에 황산마그네슘 260 mg·PSA 345 mg·d-C18 45 mg으로 분산 고상추출; 상층 1 mL에 내부표준 60 μL 첨가 후 50 ℃ 질소로 거의 건조, 아세토니트릴 100 μL로 재용해",
   "standard": "16종 PAH 정량 표준 3–180 ng/mL; 중수소 표지 내부표준(acenaphthylene-d8 등 6종)과 회수율 표준(naphthalene-d8 등 9종)", "linearity": "", "lod": "0.3–3.3 ng/g 습중량", "loq": "", "recovery": "회수율 표준으로 보정(값은 부록)"},
  "rationale": "이 종은 저서성이고 이동이 적어 연안 PAH 오염의 지표 생물로 제안되었다. 원문은 이 종 시료의 지방이 많아 정제 효율 개선이 필요하다고 적었다[8].", "source": [8], "url": "https://doi.org/10.1007/s11356-025-37058-z", "source_kind": "paper"},
 {"role": "literature", "compound": "Paralytic shellfish toxins", "compound_ko": "마비성 패독", "part": "연체부(원문 부위 초록에 없음)",
  "content": "함량 보고 없음(시험법 단일 실험실 검증 연구) [9]", "method": "사전 산화 HPLC-형광검출(AOAC 2005.06) 및 HILIC-MS/MS",
  "conditions": {"instrument": "", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "", "injection": "", "sample_prep": "이매패류용보다 용매 대 시료 비율을 높인 개량 추출법을 두 방법에 공통 적용", "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "잉글랜드 일부 지역에서 이 종을 포함한 비이매패류의 마비성 패독을 정기 감시하고 있어 시험법 검증이 이루어졌다. 초록만 확인해 칼럼·검출 조건은 전문 확인 못함[9].", "source": [9], "url": "https://doi.org/10.1093/jaoacint/qsab028", "source_kind": "paper"},
 {"role": "literature", "compound": "Arsenic species (total arsenic, inorganic arsenic, arsenobetaine)", "compound_ko": "비소 화학종", "part": "연체부(원문 부위 초록에 없음)",
  "content": "총 비소 45–655 mg/kg d.w., 무기비소 0.4 mg/kg d.w. 이하 [6]", "method": "",
  "conditions": {"instrument": "", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "", "injection": "", "sample_prep": "", "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "이 종은 비소를 많이 쌓는 종으로 알려져, 독성이 큰 무기비소를 따로 재야 섭취 노출을 판단할 수 있다. 초록만 확인해 분석 기기·조건은 전문 확인 못함[6].", "source": [6], "url": "https://doi.org/10.1039/b924351h", "source_kind": "paper"},
]
d = {"slug": "buccinum-undatum", "name_ko": "유럽물레고둥", "name_en": "Common whelk", "scientific_name": "Buccinum undatum",
     "aliases": ["Whelk", "common whelk", "waved whelk", "northern whelk", "European whelk"],
     "sections": sections, "compounds": compounds, "markers": [], "assays": assays, "nutrients": [], "production": [], "gi": [], "orgs": [], "world": [], "sources": sources}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in sections: print(s["key"], len(s["body"]))
