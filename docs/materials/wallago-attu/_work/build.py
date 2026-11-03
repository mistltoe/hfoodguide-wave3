import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
A = "2026-11-02"
def pm(title, cit, doi, pub, note):
    return {"title": f"{title} {cit} ({note})", "url": (f"https://doi.org/{doi}" if doi else "https://pubmed.ncbi.nlm.nih.gov/24558811/"), "publisher": pub, "accessed": A}
S = [
 {"title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — Wallago attu 행 1개: 원료명 '왈라고메기'(영문 Wallago, 대분류 식품원료(A코드), 중분류 수산물, 부위 칸 '-', 상태 '사용가능', 사용 조건 없음; 로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json, docs/materials/wallago-attu/card.json)", "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
 {"title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 이름에 '메기'가 들어가거나 메기류인 다른 종의 행: '메기'·'메기분말'(Silurus asotus), 'Wels catfish'(Silurus glanis), '주걱메기'(Belodontichthys dinema), '붕메기'(Ictalurus punctatus), '메콩강큰메기'(Pangasius hypophthalmus), '동남아메기'(Pangasius macronema), 'Vacha'(Eutropiichthys vacha, 이명 '메기'), '물메기'(Liparis tessellatus), '체장메기'(Genypterus blacodes, 이명 홍메기), '붉은메기'(Hoplobrotula armata), '그물메기'(Neobythites sivicola) 등 (로컬 원자료 I1020_20261013.json)", "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
 pm("Reassessment of Pinniwallago kanpurensis confirms its synonymy with Wallago attu (Siluridae). J Fish Biol", "2026;109(4):2419-2421", "10.1111/jfb.70624", "Journal of Fish Biology (PubMed 42628001)", "초록만 확인"),
 pm("Courtship Behavior and Induced Spawning Dynamics of the Freshwater Shark, Wallago attu, in Captivity: Implications for Silurid Reproductive Strategies. Animals", "2026;16(20):3296", "10.3390/ani16203296", "Animals (MDPI), PMC13700722", "PMC 전문 확인"),
 pm("Spawning and developmental biology of vulnerable catfish, Wallago attu: Implications for quality seed production and stock replenishment. J Fish Biol", "2025;108(4):1059-1071", "10.1111/jfb.70282", "Journal of Fish Biology (PubMed 41346088)", "초록만 확인"),
 pm("Reproductive development of female wallago catfish (Wallago attu) in captivity. Anim Reprod Sci", "2022;242:107014", "10.1016/j.anireprosci.2022.107014", "Animal Reproduction Science (PubMed 35671595)", "초록만 확인"),
 pm("Assessing Genetic Variation and Population Connectivity in Wallago attu: A Call for Enhanced Conservation Measures. Biochem Genet", "2025;64(2):2605-2633", "10.1007/s10528-025-11156-6", "Biochemical Genetics (PubMed 40504468)", "초록만 확인"),
 pm("Diversity and genetic structure of freshwater shark Wallago attu: an emerging species of commercial interest. Environ Sci Pollut Res Int", "2024;31(10):15571-15579", "10.1007/s11356-024-32117-3", "Environmental Science and Pollution Research (PubMed 38300493)", "초록만 확인"),
 pm("Genetic diversity, spatial connectivity, and population structure of Asian silurid catfish Wallago attu in the Ganga River System: insights from mitochondrial DNA analysis. Mol Biol Rep", "2024;51(1):378", "10.1007/s11033-024-09323-w", "Molecular Biology Reports (PubMed 38427103)", "초록만 확인"),
 pm("Complete mitochondrial genome of freshwater shark Wallago attu (Bloch & Schneider) from Indus River Sindh, Pakistan. Mitochondrial DNA A", "2016;27(1):518-9", "10.3109/19401736.2014.905836", "Mitochondrial DNA Part A (PubMed 24708114)", "초록만 확인"),
 pm("Genomic Organization of Repetitive DNA Elements and Extensive Karyotype Diversity of Silurid Catfishes (Teleostei: Siluriformes): A Comparative Cytogenetic Approach. Int J Mol Sci", "2019;20(14):3545", "10.3390/ijms20143545", "International Journal of Molecular Sciences, PMC6678683", "PMC 전문 확인 — 과 수준 서술만 인용, 본문에서 종명이 빠져 이 종 값은 쓰지 않음"),
 pm("Assessment of fatty acid composition and amino acid profiles of three important fresh water fish species native to river Indus Pakistan. Braz J Biol", "2024;84:e286429", "10.1590/1519-6984.286429", "Brazilian Journal of Biology (PubMed 39292143)", "초록만 확인 — 3종 공통 서술, 종별 수치 없음"),
 pm("Elemental composition of carnivorous fish Wallago attu (Siluridae, Siluriformes) from River Chenab, Pakistan. Braz J Biol", "2023;84:e270501", "10.1590/1519-6984.270501", "Brazilian Journal of Biology (PubMed 37255055)", "초록만 확인"),
 {"title": "Simple gas chromatographic method for the quantification of total cholesterol in fish meats. J AOAC Int 2010;93(4):1249-54 (초록만 확인 — 6종 범위만 있고 이 종 개별값 없음)", "url": "https://pubmed.ncbi.nlm.nih.gov/20922959/", "publisher": "Journal of AOAC International (PubMed 20922959)", "accessed": A},
 pm("Monitoring of trace metals in tissues of Wallago attu (lanchi) from the Indus River as an indicator of environmental pollution. Saudi J Biol Sci", "2016;23(1):72-8", "10.1016/j.sjbs.2015.03.012", "Saudi Journal of Biological Sciences, PMC4705241", "PMC 전문 확인"),
 pm("Trace elements in fish species from the Punjnad headworks: Bioaccumulation and human health risk assessment. PLoS One", "2025;20(1):e0310744", "10.1371/journal.pone.0310744", "PLOS ONE, PMC11761173", "초록 기준 인용 — 전문 본문에서 종명이 빠져 종별 표 값은 쓰지 않음"),
 pm("Methyl mercury in fish--a case study on various samples collected from Ganges river at West Bengal. Environ Monit Assess", "2012;184(6):3407-14", "10.1007/s10661-011-2193-5", "Environmental Monitoring and Assessment (PubMed 21713467)", "초록만 확인"),
 pm("Cadmium Uptake and Relationship to Feeding Habits of Freshwater Fish from the Ayeyarwady River, Mandalay, Myanmar. J Health Pollut", "2020;10(26):200608", "10.5696/2156-9614-10.26.200608", "Journal of Health and Pollution, PMC7269331", "초록만 확인"),
 pm("Seasonal Bioaccumulation and Sources of Heavy Metals in Water, Sediment, and Commercial Fish Species from Taunsa Reservoir, Indus River: Implications for Human Health Risk. Biol Trace Elem Res", "2026;204(6):3759-3775", "10.1007/s12011-025-04931-4", "Biological Trace Element Research (PubMed 41400794)", "초록만 확인"),
 pm("Seasonal Dynamics of Trace Element Contamination in Chashma Lake: Distribution in Water and Sediment, Bioaccumulation in Labeo rohita and Wallago attu, and Human Health Risk Assessment. Biol Trace Elem Res", "2026;204(11):8908-8930", "10.1007/s12011-026-05305-0", "Biological Trace Element Research (PubMed 42640445)", "초록만 확인"),
 pm("Comprehensive GIS based risk surveillance of organochlorine pesticides (OCPs) in edible fish species of River Chenab, Pakistan. Sci Total Environ", "2023;871:162084", "10.1016/j.scitotenv.2023.162084", "Science of the Total Environment (PubMed 36758692)", "초록만 확인 — 3종 합산 범위"),
 pm("Bioaccumulation of Heavy Metals in Different Organs of Wallago attu from River Kabul Khyber Pakhtunkhwa, Pakistan. Biol Trace Elem Res", "2016;172(1):242-250", "10.1007/s12011-015-0572-4", "Biological Trace Element Research (PubMed 26637495)", "초록만 확인"),
 pm("A survey of metacercarial infections in commonly edible fish and crab hosts prevailing in Manipur, Northeast India. J Parasit Dis", "2015;39(3):429-40", "10.1007/s12639-013-0360-z", "Journal of Parasitic Diseases, PMC4554583", "초록만 확인 — PMC 본문 비어 있음"),
 pm("Lipid and fatty acid compositions of a trematode, Isoparorchis hypselobagri (Digenea: Isoparorchiidae) infecting swim bladder of Wallago attu in the district North 24-Parganas of West Bengal. J Parasit Dis", "2015;39(1):67-72", "10.1007/s12639-013-0283-8", "Journal of Parasitic Diseases, PMC4328006", "초록만 확인"),
 pm("First molecular evidence of Thelohanellus wallagoi Sarkar, 1985 (Myxozoa) from economically important food fish, freshwater shark Wallago attu (Siluridae) in India. Acta Parasitol", "2018;63(3):647-653", "10.1515/ap-2018-0075", "Acta Parasitologica (PubMed 29975638)", "초록만 확인"),
 pm("Cross-cultural diversity analysis: traditional knowledge and uses of freshwater fish species by indigenous peoples of southern Punjab, Pakistan. J Ethnobiol Ethnomed", "2023;19(1):4", "10.1186/s13002-022-00573-1", "Journal of Ethnobiology and Ethnomedicine, PMC9827695", "PMC 전문 확인"),
 pm("Dietary sodium propionate enhances growth performance, digestive enzymes, haematology and immunity in Wallago attu. J Fish Biol", "2026;109(3):1498-1506", "10.1111/jfb.70530", "Journal of Fish Biology (PubMed 42283249)", "초록만 확인"),
 pm("Investigation of Microplastic Accumulation in Two Freshwater Fish Species (Labeo rohita and Wallago attu) from Tanguar Haor, Bangladesh. Bull Environ Contam Toxicol", "2025;115(5):52", "10.1007/s00128-025-04122-w", "Bulletin of Environmental Contamination and Toxicology (PubMed 41099797)", "초록만 확인"),
 pm("Occurrence of plastics and their characterization in wild caught fish species (Labeo rohita, Wallago attu and Mystus tengara) of River Ganga (India) compared to a commercially cultured species (L. rohita). Environ Pollut", "2023;334:122141", "10.1016/j.envpol.2023.122141", "Environmental Pollution (PubMed 37419205)", "초록만 확인"),
 pm("Development and characterization of a cell line WAF from freshwater shark Wallago attu. Mol Biol Rep", "2014;41(2):915-24", "10.1007/s11033-013-2936-1", "Molecular Biology Reports (PubMed 24381102)", "초록만 확인"),
 pm("The use of fish and herptiles in traditional folk therapies in three districts of Chenab riverine area in Punjab, Pakistan. J Ethnobiol Ethnomed", "2020;16(1):38", "10.1186/s13002-020-00379-z", "Journal of Ethnobiology and Ethnomedicine, PMC7313147", "초록만 확인"),
 pm("Length weight relationship and condition factor of selected freshwater fish species found in river Ganga, Gomti and Rapti, India. J Environ Biol", "2013;34(5):951-6", "", "Journal of Environmental Biology (PubMed 24558811)", "초록만 확인"),
]
for i, s in enumerate(S, 1):
    s["n"] = i
S = [{"n": s["n"], "title": s["title"], "url": s["url"], "publisher": s["publisher"], "accessed": s["accessed"]} for s in S]

sections = [
 ("overview", "개요",
  "왈라고메기(Wallago attu)는 메기목 메기과(Siluridae)에 속하는 대형 민물 메기로, 영문으로는 freshwater shark 또는 wallago catfish라고 부른다[4, 6]. 인도 아대륙에 널리 분포하고 태국·라오스·캄보디아·베트남·말레이시아·인도네시아 등 동남아시아 여러 나라에도 산다고 소개된다[4].\n\n"
  "식약처 「식품원료 목록」에는 원료명 '왈라고메기'(영문 Wallago) 한 행이 이 학명으로 올라 있으며, 분류는 수산물, 상태는 '사용가능', 사용 조건은 없다[1]. 목록의 부위 칸은 '-'로 적혀 있다[1]. 같은 목록에는 메기(Silurus asotus)·Wels catfish(Silurus glanis)·주걱메기(Belodontichthys dinema) 등 다른 메기류가 별도 원료로 올라 있으므로 이 문서의 내용과 섞어 읽으면 안 된다[2].\n\n"
  "남아시아에서는 맛이 좋고 근육 사이 잔가시가 적어 인기 있는 식용어로 평가되며[5], 파키스탄 남부 펀자브 조사에서는 주민들이 즐겨 먹는 인기 어종으로 꼽혔다[26]. 다만 야생 개체군이 줄어 IUCN 적색목록 취약(Vulnerable) 종으로 분류되었다고 보고되었다[7]. 국가표준식품성분표 등 국내 공공기관의 이 종 영양성분 값은 확인하지 못함."),
 ("history", "이용의 역사·문화",
  "왈라고메기는 인도에서 상업적으로 가장 많이 잡히는 어종 가운데 하나로 소개되며, 갠지스강 수계에 흔한 메기과 어류다[25]. 파키스탄 시장에서는 현지명 'Malli'로 불리며 kg당 약 1,300 파키스탄 루피(약 4.7 미국 달러)에 거래된다고 하였다[4].\n\n"
  "파키스탄 남부 펀자브에서 주민 88명을 면담한 민족생물학 조사에서 왈라고메기는 관련 지수(RPL)가 1.0인 인기 어종 15종에 들었다[26]. 같은 조사에서 이 종(wallago catfish)은 관절 통증에 쓴다는 민간 용도가 기록되었고, 앞선 문헌의 용도와의 유사도 지수는 0.12였다[26]. 체나브강 유역 조사에서도 왈라고메기는 민간요법에 쓰이는 어류 가운데 제보 수와 인용 빈도가 높은 종으로 꼽혔다[31]. 이러한 민간 용도는 면담 기록일 뿐 효능을 확인한 연구가 아니다[26, 31].\n\n"
  "베트남에서는 새로운 양식 후보종으로 연구되기 시작했고[6], 파키스탄에서는 호르몬 유도 산란과 사육 연구가 이어지고 있다[4, 5]. 이 종의 국내(한국) 유통·수입 이력은 확인하지 못함."),
 ("biology", "어종의 특징",
  "왈라고메기는 육식성 메기과 어류이며 빠르게 자라는 종으로 소개된다[13]. 갠지스·곰티·랍티강에서 잡은 15종 2,148마리의 길이-무게 관계 조사에 이 종이 포함되었다[32]. 인더스강 연구에서 채집한 개체의 무게는 약 2,000 g이었다[15].\n\n"
  "베트남 사육 암컷 연구에서 혈장 에스트라디올-17β는 4월(2.6±3.5 ng/mL), 비텔로제닌은 6월(543±43 ng/mL)에 가장 높았고, 난모세포 지름은 6월에 1.70±0.02 mm로 가장 컸다[6]. 이 연구는 사육 개체의 난모세포 성숙은 7월, 산란기 시작은 8월이라고 결론지었다[6]. 파키스탄 사육 연구에서 산란 수온은 27.53±0.33–29.50±0.58℃였고, 한 해 한 번 산란하는 계절형으로 보았다[4].\n\n"
  "이 종은 둥지를 짓거나 알을 지키지 않는 방란형 산란어로, 수컷이 암컷을 쫓다가 몸을 U자로 감아 알과 정자를 함께 내보낸다[4]. 알은 공 모양이고 점착성이 강하며 지름은 1.74–1.86(초록에 단위 표기 없음)으로 보고되었다[5]. 수정 후 약 969–982분에 부화했고 갓 부화한 자어의 길이는 약 4.9–5.0 mm였다[5]."),
 ("related_species", "근연종·혼동 주의",
  "메기과는 107종이 기재된 아시아 중심의 민물 메기 무리이며, 일부 종은 유럽에도 산다[11]. 이 연구가 분석한 메기과 15종의 2배체 염색체 수는 40–92개였고, 기존 자료까지 합치면 과 전체에서 28–92개로 종마다 크게 달랐다[11].\n\n"
  "인도 칸푸르에서 두 번째 등지느러미를 근거로 따로 기재된 Pinniwallago kanpurensis는 방사선 분석 결과 발생 이상 개체로 판단되어 왈라고메기의 동종이명(junior synonym)으로 정리되었다[3]. 따라서 이 이름으로 된 자료는 왈라고메기 자료로 볼 수 있다[3].\n\n"
  "식약처 목록에는 이름이 비슷한 다른 원료가 많다[2]. 메기(Silurus asotus), Wels catfish(Silurus glanis), 주걱메기(Belodontichthys dinema), 붕메기(Ictalurus punctatus), 메콩강큰메기(Pangasius hypophthalmus), Vacha(Eutropiichthys vacha, 이명 '메기')는 모두 속이 다른 별도 원료다[2]. 물메기(Liparis tessellatus)·체장메기(Genypterus blacodes)·붉은메기(Hoplobrotula armata)도 이름에 '메기'가 붙었을 뿐 학명이 전혀 다른 별도 원료다[2]. 이 문서는 학명 Wallago attu가 적힌 자료만 썼으며, 학명 없이 'catfish'로만 적힌 자료는 근거로 쓰지 않았다[1, 2]."),
 ("cultivation", "어획·양식",
  "왈라고메기는 주로 강·저수지에서 자망 등으로 잡는 야생 어종이다[15]. 파키스탄 인더스강 연구에서는 길이 약 1,200 cm의 자망으로 2011년 3–9월 매달 채집하였다[15]. 남획·서식지 훼손·오염으로 개체군이 줄고 있어, 인공 번식과 종묘 생산 연구가 보전과 양식 양쪽에서 중요하다고 하였다[4, 5].\n\n"
  "파키스탄 연구에서는 연어 생식소자극호르몬 방출호르몬 유사체와 돔페리돈 혼합제를 암컷 0.5 mL/kg, 수컷 0.2 mL/kg으로 주사해 산란을 유도했고, 주사 후 9–10시간 뒤 산란이 시작되었다[4]. 산란 뒤 어미를 빼낸 수조의 부화율(88.12±0.26%)은 어미를 남긴 수조(67.78±1.78%)보다 높아 알 포식이 의심되었다[4]. 플라스틱 끈을 산란 기질로 쓰면 수정률 86.42±1.18%, 부화율 89.28±0.80%로 수초보다 높았다[4].\n\n"
  "치어(초기 8.80±0.58 g) 60일 사육 시험에서 사료에 프로피온산 나트륨을 4 g/kg까지 넣으면 성장과 사료 효율이 좋아졌고, 회귀 분석으로 구한 최적 수준은 5.88 g/kg이었다[27]. 이 종의 국가별 어획·양식 생산량 통계는 확인하지 못함."),
 ("processing", "가공·이용",
  "식약처 목록에서 왈라고메기는 수산물로 분류된 식품원료이며, 부위 칸은 '-'로 별도 부위 제한이 적혀 있지 않다[1]. 분말·가공품 같은 별도 원료명은 목록에 없다[1].\n\n"
  "파키스탄 남부 펀자브에서는 민물고기를 훈제·바비큐·카레·튀김 등으로 먹고 훈제·절임·햇볕 건조로 저장한다고 기록되었으며, 왈라고메기는 이 지역에서 인기 있는 식용 대형 메기로 소개되었다[26]. 체나브강 조사는 이 종의 단백질 함량과 영양가가 높아 시장 수요가 좋다고 하였다[13].\n\n"
  "인더스강 3종(왈라고메기·로후·마시르) 비교 연구는 아미노산을 HPLC로, 지방산을 GC로 분석해 세 종 모두 필수아미노산과 오메가-3·오메가-6 지방산을 지닌 좋은 식품원이라고 결론지었다[12]. 다만 초록에는 종별 수치가 없어 이 종의 함량은 확인하지 못함. 왈라고메기를 포함한 파키스탄 인더스강 6종 물고기의 지방은 0.80–1.95%로 모두 저지방 어류였다고 보고되었으나 이 종의 개별값은 초록에 없다[14]."),
 ("genetics", "유전체·유전 정보",
  "파키스탄 인더스강 개체의 미토콘드리아 유전체는 15,639 bp로, 단백질 암호 유전자 13개, rRNA 유전자 2개, tRNA 유전자 22개를 가진다[10]. 염기 조성은 A 31.17%, C 28.15%, G 15.55%, T 25.12%였다[10].\n\n"
  "갠지스강 수계 7개 지류 19곳의 176개체를 미토콘드리아 DNA 세 부위(COI·Cyt b·조절 부위, 합계 2,420 bp)로 분석한 결과 유전자 다양도는 0.99로 높았고, 세 계통이 강과 무관하게 섞여 있었다[9]. 같은 연구는 약 4만 년 전 개체군 팽창이 있었다고 추정하였다[9]. 파키스탄 인더스·체나브·라비강 개체군은 COI와 Cyt b 분석에서 강 사이 유전 분화가 컸고(쌍별 분화 지수 0.40–0.61) 유전자 흐름은 1.0 미만이었다[8]. 미세위성 분석에서는 개체군 안 근친교배와 최근의 병목 현상 흔적이 확인되었다[7].\n\n"
  "꼬리지느러미에서 만든 상피 세포주(WAF)에서는 2배체 염색체 수 86개가 관찰되었으나, 이는 세포주에서 측정한 값이다[30]."),
 ("safety", "안전성",
  "식약처 목록에서 왈라고메기는 사용 조건이 없는 '사용가능' 원료다[1]. 국내 공공기관의 이 종 알레르기 정보나 섭취 주의 자료는 확인하지 못함.\n\n"
  "중금속 값은 채집 하천에 따라 크게 달랐다[15–20, 22]. 인도 갠지스강 19종 조사에서 이 종 근육의 유기수은은 0.93±0.61 μg Hg/g(습중량)으로 조사 어종 가운데 가장 높았다[17]. 미얀마 에야와디강 조사에서 근육 카드뮴은 0.083 mg/kg이었다[18]. 반면 인더스강 미안왈리 구간 조사에서는 카드뮴·니켈·코발트·아연이 모두 FEPA/WHO 기준 아래였다[15]. 인더스강 타운사 저수지 조사의 위해지수는 1 미만이었으나[19], 차슈마 호수(위해지수 1.20)와 펀자나드 보 조사에서는 섭취 위해 우려가 제기되었다[16, 20]. 체나브강 3종 조사의 유기염소계 농약 합계는 5.09–414 ng/g(3종 합산 범위)이었다[21].\n\n"
  "인도 마니푸르 조사에서 이 종은 흡충 피낭유충이 확인된 식용어 3종 가운데 하나였다[23]. 부레에서는 흡충 Isoparorchis hypselobagri가 보고되었다[24]. 날것이나 덜 익힌 민물고기는 흡충 감염 경로가 될 수 있다[23]. 방글라데시 습지 조사에서는 이 종과 로후의 위·장·등 근육에서 미세플라스틱이 확인되었으나, 근육 검출의 종별 구분은 초록에 없다[28]. 갠지스강 야생어 9종 조사에서도 이 종을 포함한 3종에서만 플라스틱이 검출되었다[29]."),
]
sections = [{"key": k, "title": t, "body": b} for k, t, b in sections]

def C(name, ko, cls, role, part, content, act, src):
    return {"name": name, "name_ko": ko, "class": cls, "role": role, "part": part, "content_text": content, "activity_ko": act, "source": src}
compounds = [
 C("Docosahexaenoic acid", "DHA(C22:6)", "n-3 고도불포화지방산", "nutrient", "살(초록에 부위 표기 없음)", "수치 확인하지 못함 — 초록에 3종(왈라고메기·로후·마시르) 공통의 주요 지방산으로만 적힘", "세 종 공통으로 주목할 지방산으로 꼽혔다[12]", [12]),
 C("Palmitic acid", "팔미트산(C16:0)", "포화지방산", "nutrient", "살(초록에 부위 표기 없음)", "수치 확인하지 못함 — 3종 공통 주요 지방산", "세 종 공통의 주요 포화지방산으로 적혔다[12]", [12]),
 C("Oleic acid", "올레산(C18:1)", "단일불포화지방산", "nutrient", "살(초록에 부위 표기 없음)", "수치 확인하지 못함 — 3종 공통 주요 지방산", "세 종 공통의 주요 단일불포화지방산으로 적혔다[12]", [12]),
 C("Palmitoleic acid", "팔미톨레산(C16:1)", "단일불포화지방산", "nutrient", "살(초록에 부위 표기 없음)", "수치 확인하지 못함 — 3종 공통 주요 지방산", "세 종 공통의 주요 지방산으로 적혔다[12]", [12]),
 C("Glutamic acid", "글루탐산", "아미노산", "nutrient", "살(초록에 부위 표기 없음)", "수치 확인하지 못함 — 3종 공통으로 가장 많은 아미노산 가운데 하나로 적힘(HPLC 분석)", "세 종 공통의 주요 아미노산이다[12]", [12]),
 C("Lysine", "라이신", "필수아미노산", "nutrient", "살(초록에 부위 표기 없음)", "수치 확인하지 못함 — 3종 공통 주요 아미노산(류신·이소류신과 함께)", "필수아미노산으로 세 종 공통의 주요 아미노산에 들었다[12]", [12]),
 C("Cholesterol", "콜레스테롤", "스테롤", "nutrient", "살(fish meat)", "이 종 개별값 확인하지 못함 — 초록에는 6종 범위 72–392 mg/100 g만 있음(이 종 값 아님)", "GC로 정량한 6종 비교 연구에 이 종이 포함되었다[14]", [14]),
 C("Calcium", "칼슘", "무기질", "nutrient", "몸 전체(습·건중량 기준 분석)", "수치 확인하지 못함 — 초록에 분석 원소 가운데 가장 높았다고만 적힘", "체나브강 야생 개체에서 분석 원소 중 가장 높았다[13]", [13]),
 C("Zinc", "아연", "무기질(미량원소)", "nutrient", "근육·피부·아가미·간", "47.4–1147.5 μg/g 습중량(4개 조직·3개 지점 범위, 인더스강 미안왈리)", "필수 미량원소이며 조직별 농도 차이가 컸다[15]", [15]),
 C("Methylmercury", "메틸수은(유기수은)", "중금속(오염물질)", "bioactive", "근육", "0.93±0.61 μg Hg/g 습중량(인도 갠지스강 서벵골, 유기수은)", "조사한 19종 가운데 유기수은이 가장 높았다[17]", [17]),
 C("Cadmium", "카드뮴", "중금속(오염물질)", "bioactive", "근육 / 여러 조직", "근육 0.083 mg/kg(미얀마 에야와디강); 4개 조직 범위 0.004–0.24 μg/g 습중량(인더스강 미안왈리)", "미얀마 근육값은 EU 기준(0.1 ppm)보다 낮고 FAO/WHO 기준(0.05 ppm)보다 높았으며, 인더스강 값은 FEPA/WHO 기준 아래였다[15, 18]", [15, 18]),
 C("Nickel", "니켈", "중금속(오염물질)", "bioactive", "근육·피부·아가미·간", "0.003–0.708 μg/g 습중량(4개 조직·3개 지점 범위)", "근육에서 가장 낮고 아가미·간에서 높았다[15]", [15]),
 C("Chromium", "크롬", "중금속(오염물질)", "bioactive", "초록에 조직 표기 없음", "여름 최고 0.56 mg/kg(인더스강 타운사 저수지)", "카드뮴과 함께 허용 기준을 자주 넘었다고 보고되었다[19]", [19]),
 C("Dieldrin", "디엘드린(유기염소계 농약)", "잔류 농약(오염물질)", "bioactive", "초록에 조직 표기 없음", "이 종 개별값 확인하지 못함 — 3종 ΣOCPs 범위 5.09–414 ng/g(3종 합산 범위, 이 종 값 아님)", "체나브강 식용어 3종에서 가장 우세한 유기염소계 농약이었다[21]", [21]),
]

E = {k: "" for k in ["instrument","column","mobile_phase","gradient","flow","temp","detection","injection","sample_prep","standard","linearity","lod","loq","recovery"]}
c1 = dict(E); c1.update({
 "instrument": "원자흡광분광광도계 Hitachi Polarized Zeeman AAS Z-8200(원문 표기), 공기-아세틸렌 불꽃",
 "detection": "불꽃 원자흡광(Cd·Ni·Co·Zn)",
 "sample_prep": "인더스강 미안왈리 3개 지점에서 2011년 3–9월 매달 자망 채집(약 2,000 g 개체), 근육·피부·아가미·간 약 15 g 채취 후 -20℃ 보관; 시료 약 1 g을 과염소산 5 mL + 질산 15 mL로 갈색 연기가 멎을 때까지 가열 분해, 증류수 50 mL로 희석; 결과는 μg/g 습중량",
 "standard": "1000 ppm 표준용액을 희석한 검량 표준, 바탕시험 병행; NIST 표준물질 SRM2976(원문 표기 'freeze-dried muscle tissue')로 정밀도 확인",
})
c2 = dict(E); c2.update({"detection": "GC(총 콜레스테롤), 분석 시간 11분 이내", "sample_prep": "지방은 Folch 법으로 정량", "recovery": "표준첨가 회수율 95–103%, 변동계수 5.6% 이하"})
c3 = dict(E); c3.update({"detection": "지방산 GC, 아미노산 HPLC(초록 표기)"})
assays = [
 {"role": "literature", "compound": "Cadmium, nickel, cobalt, zinc", "compound_ko": "카드뮴·니켈·코발트·아연", "part": "근육·피부·아가미·간",
  "content": "Cd 0.004–0.24, Ni 0.003–0.708, Co 0.002–0.768, Zn 47.4–1147.5 μg/g 습중량(초록, 4개 조직·3개 지점 범위; 본문 결과 절에는 Co 하한이 0.001로 적혀 있음)[15]",
  "method": "불꽃 원자흡광분광법(FAAS)", "conditions": c1,
  "rationale": "근육·피부는 먹는 부위, 아가미·간은 만성 노출 지표로 보고 중금속 축적을 비교하였다[15]. PMC 전문(Materials and methods) 확인 — 파장·검출한계·정량한계·회수율 값은 본문에 없음[15].",
  "source": [15], "url": "https://doi.org/10.1016/j.sjbs.2015.03.012", "source_kind": "paper"},
 {"role": "literature", "compound": "Cholesterol", "compound_ko": "총 콜레스테롤", "part": "살(fish meat)",
  "content": "이 종 개별값은 초록에 없음 — 6종 범위 72–392 mg/100 g, 지방 0.80–1.95%(6종 범위, 이 종 값 아님)[14]",
  "method": "GC(총 콜레스테롤), Folch 법(지방)", "conditions": c2,
  "rationale": "생선 살의 지방·콜레스테롤은 영양 품질 지표로 쓰이며, 이 연구는 인더스강 6종에 간단한 GC 정량법을 적용하였다[14]. 전문 확인 못함 — 칼럼·온도 조건 등은 비워 둠[14].",
  "source": [14], "url": "https://pubmed.ncbi.nlm.nih.gov/20922959/", "source_kind": "paper"},
 {"role": "literature", "compound": "Fatty acids and amino acids", "compound_ko": "지방산·아미노산 조성", "part": "살(초록에 부위 표기 없음)",
  "content": "종별 수치는 초록에 없음 — 3종 공통으로 글루탐산·아스파르트산·아르기닌·알라닌·류신·라이신·이소류신, 지방산은 C16:0·C18:1·C16:1·C18:2·DHA가 주요 성분[12]",
  "method": "GC(지방산), HPLC(아미노산)", "conditions": c3,
  "rationale": "필수아미노산과 n-3·n-6 지방산 조성은 생선의 영양 품질 지표로 쓰인다[12]. 전문 확인 못함 — 분석 조건은 비워 둠[12].",
  "source": [12], "url": "https://doi.org/10.1590/1519-6984.286429", "source_kind": "paper"},
]

d = {
 "slug": "wallago-attu", "name_ko": "왈라고메기", "name_en": "Wallago (freshwater shark, wallago catfish)",
 "scientific_name": "Wallago attu", "aliases": ["Wallago", "freshwater shark", "wallago catfish", "Malli", "Pinniwallago kanpurensis(동종이명)"],
 "sections": sections, "compounds": compounds, "markers": [], "assays": assays,
 "nutrients": [], "production": [], "world": [], "gi": [], "orgs": [], "sources": S,
}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in sections: print(s["key"], len(s["body"]))
print(len(S))
