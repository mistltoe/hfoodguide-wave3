import json, pathlib
A = "2026-11-02"
def pm(n, title, pmid, pub, pmc=None):
    url = f"https://pmc.ncbi.nlm.nih.gov/articles/{pmc}/" if pmc else f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
    return {"n": n, "title": f"{title} (PMID {pmid})", "url": url, "publisher": pub, "accessed": A}
S = [
 {"n": 1, "title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020)", "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
 pm(2, "Chromosome-level genome assembly of starry flounder (Platichthys stellatus)", "40659658", "Scientific Data 12:1215, 2025", "PMC12259871"),
 pm(3, "Investigation of sex determination in starry flounder (Platichthys stellatus) reveals sex chromosome evolution in Pleuronectiformes and identifies a sex-specific marker", "39572017", "Zoological Research 45(6):1347-1356, 2024", "PMC11668952"),
 pm(4, "Wild and hatchery populations of Korean starry flounder (Platichthys stellatus) compared using microsatellite DNA markers", "22272127", "International Journal of Molecular Sciences 12(12):9189-9202, 2011", "PMC3257124"),
 pm(5, "Complete mitochondrial genome of the hybrid flounder Platichthys stellatus (♀) × Verasper variegatus (♂)", "42428807", "Mitochondrial DNA Part B 11(8):919-924, 2026", "PMC13347844"),
 pm(6, "Early growth and development of reciprocal hybrids of the starry flounder Platichthys stellatus and stone flounder Kareius bicoloratus", "24773542", "Journal of Fish Biology 84(5):1503-1518, 2014"),
 pm(7, "Morphological evidence of correlational selection and ecological segregation between dextral and sinistral forms in a polymorphic flatfish, Platichthys stellatus", "17465920", "Journal of Evolutionary Biology 20(3):1104-1114, 2007"),
 pm(8, "Integrative taxonomy of Pseudolepeophtheirus longicauda (Crustacea: Copepoda: Caligidae) parasitic on Platichthys stellatus", "32413490", "Parasitology International 78:102135, 2020"),
 pm(9, "Growth, nutrient deposition, plasma metabolites, and innate immunity are associated with feeding rate in juvenile starry flounder (Platichthys stellatus)", "39518850", "Animals 14(21):3127, 2024", "PMC11544839"),
 pm(10, "Effects on bioaccumulation, growth performance, hematological parameters, plasma components, and antioxidant responses in starry flounder exposed to dietary cadmium and ascorbic acid", "36670989", "Antioxidants 12(1):128, 2023", "PMC9854703"),
 pm(11, "Assessment of the efficacy of using taurine supplements to improve growth and feed utilization of juvenile starry flounder given diets based on soy-protein", "33510970", "PeerJ 9:e10597, 2021", "PMC7808265"),
 pm(12, "The mercury accumulation and its effects on antioxidant and immune responses in starry flounder, Platichthys stellatus exposed to dietary mercury", "36868538", "Fish & Shellfish Immunology 135:108658, 2023"),
 pm(13, "Creatine turnover in the starry flounder, Platichthys stellatus", "24226895", "Fish Physiology and Biochemistry 6(1):1-9, 1989"),
 pm(14, "Novel L-amino acid oxidase with antibacterial activity against methicillin-resistant Staphylococcus aureus isolated from epidermal mucus of the flounder Platichthys stellatus", "20015076", "FEBS Journal 277(2):453-465, 2010"),
 pm(15, "Recombinant production and evaluation of an antibacterial L-amino acid oxidase derived from flounder Platichthys stellatus", "25661816", "Applied Microbiology and Biotechnology 99(16):6693-6703, 2015"),
 pm(16, "Characterization and antimicrobial activity of a novel pleurocidin in starry flounder (Platichthys stellatus)", "40379117", "Fish & Shellfish Immunology 163:110420, 2025"),
 pm(17, "Molecular characterization of a hepcidin homologue in starry flounder (Platichthys stellatus) and its synergistic interaction with antibiotics", "30195905", "Fish & Shellfish Immunology 83:45-51, 2018"),
 pm(18, "Genomic and phenotypic characterisation of Streptococcus parauberis isolated from starry flounder (Platichthys stellatus)", "41258825", "Journal of Fish Diseases 49(5):e70083, 2025"),
 pm(19, "Streptococcus parauberis infection in starry flounder, Platichthys stellatus: characterization of innate immune responses following experimental infection", "23707742", "Fish & Shellfish Immunology 35(2):413-420, 2013"),
 pm(20, "First report and characterization of Ceratomyxa platichthytis from cultured starry flounder, Platichthys stellatus", "42561741", "Veterinary Parasitology 347:110879, 2026"),
 pm(21, "Efficacy and safety data of ceftiofur antibiotics against Streptococcus parauberis PH0710 infection in starry flounder", "31372396", "Data in Brief 23:103729, 2019", "PMC6660470"),
 pm(22, "Stress responses of starry flounder, Platichthys stellatus (Pallas) following water temperature rise", "26521544", "Journal of Environmental Biology 36(5):1057-1062, 2015"),
 pm(23, "Morphological analysis of blind-side hypermelanosis of the starry flounder, Platichthys stellatus during early development", "25949175", "Development & Reproduction 18(2):79-87, 2014", "PMC4282256"),
 pm(24, "Morphometric changes in the cultured starry flounder, Platichthys stellatus, in open marine ranching areas", "24620579", "Journal of Environmental Biology 34(2):197-204, 2013"),
 pm(25, "Difference in serum scuticocidal activity against Miamiensis avidus between olive flounder (Paralichthys olivaceus) and starry flounder (Platichthys stellatus)", "40597412", "Journal of Fish Diseases 49(1):e70020, 2025"),
 pm(26, "Isolation and characterization of a rhabdovirus from starry flounder (Platichthys stellatus) collected from the northern portion of Puget Sound, Washington, USA", "14769907", "Journal of General Virology 85(Pt 2):495-505, 2004"),
 pm(27, "Involvement of glycolysis activation in flatfish sexual size dimorphism: insights from transcriptomic analyses of Platichthys stellatus and Cynoglossus semilaevis", "33930775", "Comparative Biochemistry and Physiology Part D 39:100832, 2021"),
 pm(28, "Comparison of the effects of dietary single and multi-probiotics on growth, non-specific immune responses and disease resistance in starry flounder, Platichthys stellatus", "27818339", "Fish & Shellfish Immunology 59:351-357, 2016"),
 pm(29, "Hormonal control of water and sodium movements in the urinary bladder of the starry flounder, Platichthys stellatus", "4340077", "General and Comparative Endocrinology, 1972"),
]

sec = []
def add(k, t, b): sec.append({"key": k, "title": t, "body": b})

add("overview", "한눈에 보기",
"강도다리(학명 Platichthys stellatus)는 식약처 「식품원료 목록」에 대표 원료명 '강도다리'로 올라 있는 바닷물고기로, 분류는 수산물, 사용 조건은 '사용가능'이다[1]. 목록의 영문명 칸에는 'Starry flounder, Diamond back'이 적혀 있고, 부위 칸은 '-'이며 사용 조건 기준 칸은 비어 있어 특정 부위나 제한 조건이 붙지 않은 원료다[1].\n\n"
"분류상 가자미목(Pleuronectiformes) 가자미과(Pleuronectidae)에 속하는 찬물성 가자미류로, 북태평양과 북극해 연안에 살며 강어귀·기수 석호·강과 호수 같은 민물에도 들어간다[2]. 염분 0–33 ppt에서 정상적으로 살 수 있을 만큼 염분 적응력이 커서, 한국과 중국 북부에서 유망한 양식 가자미로 주목받는다[2].\n\n"
"국내에서는 시장 가치와 넓은 염분 내성 때문에 양식 대상종으로 연구되어 왔고, 사료·질병·유전체 연구가 늘고 있다[9, 18]. 건강기능식품 고시형 원료로는 이번 조사에서 확인하지 못해 고시 지표성분은 적지 않는다.")

add("history", "이름과 연구의 역사",
"국문 원료명 '강도다리'와 영문명 Starry flounder는 식약처 식품원료 목록에 실린 이름이다[1]. 학명의 명명자는 팔라스(Pallas)로, 논문에 따라 명명 연도를 1788년[4] 또는 1787년[5]으로 달리 적고 있다.\n\n"
"초기 연구는 북미 연안 개체를 대상으로 한 생리학 연구가 많았는데, 1970년대에는 오줌보(방광)의 물·나트륨 이동을 호르몬이 조절하는 방식이 연구되었다[29]. 1989년에는 방사성 표지 크레아틴으로 근육·간·아가미의 크레아틴 회전을 추적한 연구가 나왔다[13]. 2004년에는 미국 퓨젓사운드 북부에서 잡은 강도다리에서 새로운 랍도바이러스(starry flounder rhabdovirus)가 분리·보고되었다[26].\n\n"
"한국에서는 동해안에서 2000년부터 잡아 온 어미로 인공 번식을 했고, 2004년에 첫 세대 인공 종자를 생산했다[4]. 이후 인공 종자를 연안에 방류하는 자원 조성 사업과 함께 방류 개체의 형태 변화·유전 다양성 연구가 이어졌다[4, 24]. 2010년대부터는 양식 질병과 면역 유전자 연구가, 2024–2025년에는 성 결정 연구와 염색체 수준 유전체 해독이 발표되었다[3, 2].")

add("biology", "어종과 생태",
"강도다리는 한국 북동부 연안에서 일본 오호츠크해까지, 그리고 추크치해·베링해·알류샨 열도에서 미국 로스앤젤레스 항까지 북태평양 가장자리에 분포한다[4]. 대체로 수심 73 m보다 얕은 곳을 좋아하지만 274 m에서도 기록되었고, 어린 개체는 조간대에서 흔히 보인다[4]. 다른 논문은 주로 수심 150 m까지의 연안에 살며 민물·기수에서도 발견된다고 적었다[5].\n\n"
"가자미류는 두 눈이 몸 한쪽에 몰려 있는데, 강도다리는 눈이 왼쪽에 있는 개체와 오른쪽에 있는 개체가 함께 나타나는 드문 종이다[7]. 왼눈형의 비율은 캘리포니아의 50%에서 일본의 100%까지 지역에 따라 연속적으로 달라진다[7]. 서태평양 집단은 약 80%가 왼눈형으로 보고되었다[6].\n\n"
"사육 시험에서 변태 최소 일령은 부화 후 23일로 돌가자미(34일)보다 빨랐고, 바닥에 내려앉을 때 표준체장은 6.43 mm로 돌가자미(12.87 mm)보다 작았다[6]. 암컷이 수컷보다 빨리 자라는 암컷 우세 성장 차이가 뚜렷하다[27]. 양식 시험에서 수온 24 °C 이상이 되면 혈장 코르티솔과 포도당이 올라가 스트레스 반응이 나타났고, 27 °C에서는 삼투 조절 장애가 관찰되었다[22].")

add("related_species", "가까운 종과 혼동",
"식약처 식품원료 목록에는 강도다리 외에도 넙치(Paralichthys olivaceus), 돌가자미(Kareius bicoloratus), 범가자미(Verasper variegatus), 노랑가자미(Verasper moseri) 등 여러 가자미류가 각각 별도 원료로 올라 있다[1]. 이들은 서로 다른 종이므로 성분·양식 자료를 강도다리 자료와 섞어 쓰면 안 된다[1].\n\n"
"강도다리는 다른 가자미와 잡종을 만들 수 있다[5, 6]. 강도다리 암컷×돌가자미 수컷, 돌가자미 암컷×강도다리 수컷의 상호 잡종은 모두 치어까지 자랐고, 눈 위치는 주로 왼쪽(76–80%)이었다[6]. 강도다리 암컷×범가자미 수컷 잡종의 미토콘드리아 유전체(16,874 bp)는 모계인 강도다리와 100% 같았다[5]. 넙치와 강도다리 사이 잡종을 가려내는 미세위성 표지 연구도 있었다고 소개되었다[4].\n\n"
"넙치와 강도다리를 비교한 연구에서는 강도다리 혈청이 스쿠티카충(Miamiensis avidus)을 죽이는 활성이 넙치 혈청보다 유의하게 높았다[25]. 시장에서 두 종을 혼동할 때 생기는 문제는 이번 조사에서 확인하지 못함.")

add("cultivation", "어획과 양식",
"한국의 강도다리 양식은 동해안에서 잡은 어미의 인공 번식으로 시작되었고, 산란·부화·자어와 치어 사육까지 완전 양식이 가능해졌다[4]. 인공 종자는 연안에 방류되기도 하는데, 방류 3–36개월 뒤 방류군은 사육군보다 야생 개체에 가까운 형태를 보였고 눈 없는 쪽 체색 이상 비율은 방류군 22.7%, 사육군 39.5%였다[24]. 체색 이상은 부화 후 약 80일(전장 약 2 cm)에 처음 보였다[23].\n\n"
"국내 양식 생산량은 2014년 2,377톤에서 2018년 3,373톤으로 늘었다고 한 논문이 인용했고[10], 다른 논문은 약 4,353톤이라고 적었다[9]. 이 값의 원 통계(해양수산부·통계청)는 이번 조사에서 직접 확인하지 못함.\n\n"
"평균 183.6 g 치어를 10주 키운 시험에서 성장에 맞는 하루 급이율은 체중의 2.4%, 리소자임 활성 기준으로는 1.7%로 추정되었다[9]. 어분을 줄인 대두단백 사료에서는 타우린 요구량이 사료의 1.75%로 추정되었다[11]. 바실러스 등 프로바이오틱스 첨가 사료는 성장과 비특이 면역을 높였다[28]. 넙치의 주요 세균병인 연쇄구균(Streptococcus parauberis)이 강도다리 양식장에서도 발생해 실험 감염 연구가 이루어졌고[19], 포항 양식장 집단 폐사에서도 원인균으로 확인되었다[18].")

add("processing", "식품 성분과 이용",
"중국에서 대두단백 사료로 키운 치어(약 45 g)의 등근육은 습중량 기준 수분 74.12%, 조단백질 23.27%, 조지방 1.78%, 회분 0.44%였다[11]. 같은 근육 단백질의 아미노산 가운데 글루탐산(건물 16.20%)과 아스파르트산(9.76%)이 가장 많았고, 라이신 7.40%, 류신 7.11%가 뒤를 이었다[11]. 근육 타우린은 대조 사료에서 건물 100 g당 184.43 mg이었고, 타우린 1.0–2.5%를 넣은 사료에서는 769.13–784.50 mg으로 늘었다[11].\n\n"
"이 값들은 양식 시험 사료 조건의 치어 자료여서 시판 성어나 자연산의 성분과 같다고 볼 수 없다[11]. 체성분은 사람이 먹는 살의 품질 지표이며 급이율에 따라 달라진다고 연구자들이 설명했다[9]. 쉬고 있는 개체의 흰 근육에는 크레아틴(크레아틴인산 포함)이 1 g당 38.1 μmol 있었고, 36일 굶기면 먹이를 준 개체의 52%로 줄었다[13].\n\n"
"피부 점액과 아가미에서는 메티실린 내성 황색포도알균을 억제하는 약 52 kDa의 L-아미노산 산화효소가 발견되었다[14]. 이 효소는 효모에서 재조합 생산되었고 시험관에서 포도알균 성장을 억제했다[15]. 플레우로시딘·헵시딘 같은 항균 펩타이드도 보고되었지만 모두 실험실 결과이며 식품으로 먹었을 때의 효과는 아니다[16, 17]. 국내 가공품 종류와 유통 형태는 이번 조사에서 확인하지 못함.")

add("genetics", "유전체와 성 결정",
"2025년에 PacBio HiFi·Hi-C 서열로 만든 염색체 수준 유전체는 643.56 Mb이며, 94.02%가 24개 유사 염색체에 배치되었다[2]. 단백질 암호 유전자는 22,835개, 반복 서열은 227.87 Mb(35.41%)였고, BUSCO 완성도는 98.3%였다[2]. 이전 짧은 서열 조립본(contig N50 33.2 kb)보다 연속성이 약 301배 좋아졌다[2].\n\n"
"전장 유전체 재분석으로 23번 염색체가 성염색체이며 XX/XY형임이 밝혀졌다[3]. 성 결정 영역은 이 염색체의 48.1%를 차지하고 역위는 없었으며, 유전적 성을 가려내는 표지도 개발되었다[3]. 암수 근육 전사체 비교에서는 암컷 근육의 해당 과정 유전자 발현이 높아 암컷의 빠른 성장과 연관이 제시되었다[27].\n\n"
"국내 동해안 야생 48마리와 1세대 인공 종자 30마리를 미세위성 12개로 비교하니, 기대 이형접합도는 야생 0.75, 양식 0.68이었고 두 집단 사이에 작지만 유의한 차이(FST 0.043)가 있었다[4]. 기생 요각류와 함께 분석한 COI 서열에서는 강도다리가 북서태평양과 북동태평양 두 계통으로 나뉘었다[8].")

add("safety", "안전성과 식품원료 지위",
"강도다리는 식약처 「식품원료 목록」에 '사용가능' 수산물로 올라 있으며 부위·조건 제한은 적혀 있지 않다[1]. 건강기능식품 고시형 원료로는 이번 조사에서 확인하지 못해 고시 섭취 시 주의사항은 적지 않는다. 생선 알레르기 표시, 수산물 중금속 기준 등 식약처 공전의 수치는 이번 조사에서 확인하지 못함.\n\n"
"사료로 무기수은을 4주 먹인 노출 실험에서 수은은 장>두신>간>아가미>근육 순으로 쌓여 근육이 가장 적었고, 2주 정화 기간에 축적이 줄었다[12]. 카드뮴 사료 노출 실험에서는 장·신장·간·아가미에 쌓였고 비타민 C(아스코르브산) 첨가가 축적을 줄였으나, 근육은 측정하지 않았다[10]. 두 연구는 노출 실험이지 시판 강도다리의 중금속 함량 조사가 아니다[10, 12].\n\n"
"포항 양식장 연쇄구균 분리주는 모두 테트라사이클린·옥시테트라사이클린에 내성을 보였다[18]. 한 논문은 한국에서 수산질병관리사가 세프티오퍼를 처방·판매하는 것이 불법이라고 적었다[21]. 기생충으로는 양식 강도다리 쓸개의 점액포자충(Ceratomyxa platichthytis)과 아가미강의 요각류(Lepeophtheirus longicauda)가 보고되었으나 사람 감염 여부는 이번 조사에서 확인하지 못함[20, 8].")

compounds = [
 dict(name="Taurine", name_ko="타우린", **{"class": "아미노산 유사 물질"}, role="nutrient", part="등근육(양식 치어, 대두단백 사료 시험)", content_text="대조 사료 184.43 ± 13.24 mg/100 g 건물; 타우린 1.0–2.5% 사료 769.13–784.50 mg/100 g 건물[11]", activity_ko="간의 타우린 합성효소(CSD) 활성이 약해 사료 타우린이 성장에 필요한 것으로 평가되었다(양식 시험)[11].", source=[11]),
 dict(name="Glutamic acid", name_ko="글루탐산", **{"class": "아미노산"}, role="nutrient", part="등근육(양식 치어)", content_text="대조구 16.20 ± 1.08% 건물[11]", activity_ko="근육 아미노산 중 가장 많은 성분으로 측정되었다[11].", source=[11]),
 dict(name="Aspartic acid", name_ko="아스파르트산", **{"class": "아미노산"}, role="nutrient", part="등근육(양식 치어)", content_text="대조구 9.76 ± 0.64% 건물[11]", activity_ko="글루탐산 다음으로 많은 근육 아미노산이다[11].", source=[11]),
 dict(name="Lysine", name_ko="라이신", **{"class": "필수아미노산"}, role="nutrient", part="등근육(양식 치어)", content_text="대조구 7.40 ± 0.48% 건물[11]", activity_ko="사람의 필수아미노산으로, 근육 단백질에서 셋째로 많았다[11].", source=[11]),
 dict(name="Leucine", name_ko="류신", **{"class": "필수아미노산"}, role="nutrient", part="등근육(양식 치어)", content_text="대조구 7.11 ± 0.48% 건물[11]", activity_ko="필수아미노산으로 사료 타우린 수준과 관계없이 비슷했다[11].", source=[11]),
 dict(name="Alanine", name_ko="알라닌", **{"class": "아미노산"}, role="nutrient", part="등근육(양식 치어)", content_text="대조구 6.54 ± 0.44% 건물[11]", activity_ko="근육 단백질 아미노산 조성의 일부로 측정되었다[11].", source=[11]),
 dict(name="Methionine", name_ko="메티오닌", **{"class": "필수아미노산(함황)"}, role="nutrient", part="등근육(양식 치어)", content_text="대조구 1.68 ± 0.07% 건물; 타우린 2.0·2.5% 사료 1.96·1.92%[11]", activity_ko="타우린 2% 이상 사료에서 근육 메티오닌이 유의하게 늘었다(양식 시험)[11].", source=[11]),
 dict(name="Cysteine", name_ko="시스테인", **{"class": "아미노산(함황)"}, role="nutrient", part="등근육(양식 치어)", content_text="대조구 1.18 ± 0.13% 건물; 타우린 1.5–2.5% 사료 1.35–1.38%[11]", activity_ko="타우린 1% 이상 사료에서 근육 시스테인이 늘었다고 보고되었다(양식 시험)[11].", source=[11]),
 dict(name="Creatine", name_ko="크레아틴(크레아틴인산 포함)", **{"class": "구아니디노 화합물"}, role="nutrient", part="흰 근육(쉬는 개체)", content_text="PCr+Cr 38.1 μmol/g; 아가미 4.1, 간 5.6, 혈액 0.3 μmol/g[13]", activity_ko="근육 에너지 저장 물질로, 36일 굶기면 근육 함량이 먹이 준 개체의 52%로 줄어 먹이 공급과 관련이 제시되었다[13].", source=[13]),
 dict(name="Creatinine", name_ko="크레아티닌", **{"class": "구아니디노 화합물"}, role="nutrient", part="흰 근육(쉬는 개체)", content_text="2.40 μmol/g; 아가미 0.25, 간 0.45 μmol/g[13]", activity_ko="크레아틴 분해 산물로 함께 측정되었다[13].", source=[13]),
 dict(name="L-amino acid oxidase", name_ko="L-아미노산 산화효소(psLAAO1)", **{"class": "플라빈 효소 단백질"}, role="bioactive", part="피부 점액·아가미", content_text="약 52 kDa, 등전점 5.3(함량 수치 없음)[14]; 재조합 단백질의 표피포도알균 최소억제농도 0.078 μg/mL[15]", activity_ko="과산화수소를 만들어 메티실린 내성 황색포도알균 등을 억제했다(시험관 결과)[14, 15].", source=[14, 15]),
 dict(name="Pleurocidin", name_ko="플레우로시딘(SF1)", **{"class": "항균 펩타이드"}, role="bioactive", part="간 전사체·면역 기관", content_text="성숙 펩타이드 22개 아미노산(함량 수치 없음)[16]", activity_ko="그람양성·음성균의 세포막을 파괴했다(시험관 결과)[16].", source=[16]),
 dict(name="Hepcidin", name_ko="헵시딘(PsHepcidin)", **{"class": "항균 펩타이드"}, role="bioactive", part="간(발현 최고)", content_text="mRNA 발현이 간에서 가장 높음(함량 수치 없음)[17]", activity_ko="합성 펩타이드가 넓은 항균 활성을 보였고 항생제와 상승 작용을 보였다(시험관 결과)[17].", source=[17]),
]

cond0 = {k: "" for k in ["instrument","column","mobile_phase","gradient","flow","temp","detection","injection","sample_prep","standard","linearity","lod","loq","recovery"]}
def C(**kw):
    c = dict(cond0); c.update(kw); return c
assays = [
 {"role": "literature", "compound": "Amino acids (acid-hydrolysed) and taurine", "compound_ko": "근육 아미노산(산가수분해)·타우린",
  "part": "양식 치어(초기 22.25 g, 8주 사육) 등근육", "content": "대조구 글루탐산 16.20%, 아스파르트산 9.76%, 라이신 7.40% 건물; 타우린 184.43 mg/100 g 건물[11]",
  "method": "아미노산 자동분석기",
  "conditions": C(instrument="아미노산 자동분석기(Hitachi L8900)", sample_prep="근육을 6 N 염산 6 mL로 110 °C에서 22시간 밀봉 가수분해 → 질소 가스로 염산 제거 → 0.1 N 염산 완충액에 재용해 → 0.22 μm 폴리에테르설폰 막 여과"),
  "rationale": "근육 단백질의 영양 품질과 사료 타우린 효과를 비교하려고 정량했다[11]. 전문(Methods) 확인 — 칼럼·완충액·검량선·검출한계·회수율은 논문에 없고, 타우린을 같은 분석기로 쟀는지는 명시되지 않음[11].",
  "source": [11], "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC7808265/", "source_kind": "paper"},
 {"role": "literature", "compound": "Crude protein (proximate composition)", "compound_ko": "조단백질 등 일반성분",
  "part": "양식 치어 등근육", "content": "습중량 기준 수분 74.12%, 조단백질 23.27%, 조지방 1.78%, 회분 0.44%(대조구)[11]",
  "method": "켈달법(N×6.25)·속슬렛 추출·회화",
  "conditions": C(sample_prep="105 °C 오븐에서 항량까지 건조해 수분 측정 → 분쇄 → 켈달 분해로 단백질(N×6.25), 속슬렛 추출로 조지방, 550 °C 회화로 회분; 에너지는 단열 봄베 열량계(IKA C6000)"),
  "rationale": "체성분은 먹는 살의 품질 지표로 쓰인다[9]. 전문 확인 — 다른 국내 연구는 수분 135 °C 2시간, 켈달 장치(Gerhardt VAP 50), 에틸에테르 추출(Soxtec 2043), 600 °C 6시간 회화 조건을 썼으나 결과 수치는 표에만 있어 옮기지 못함[9, 11].",
  "source": [11, 9], "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC7808265/", "source_kind": "paper"},
 {"role": "literature", "compound": "Cadmium", "compound_ko": "카드뮴",
  "part": "장·신장·간·아가미(사료 카드뮴 노출 실험, 평균 69.5 g)", "content": "축적 순서 장>신장>간>아가미; 개별 수치는 그림에만 있어 확인하지 못함[10]",
  "method": "ICP-MS",
  "conditions": C(instrument="ICP-MS(PerkinElmer ELAN 6600 DRC, 아르곤)", sample_prep="조직을 초순수로 헹군 뒤 48시간 동결건조 → 0.1 g을 70% 질산 6 mL + 70% 과염소산 2 mL로 28 °C 4시간 분해 → 105 °C 열판에서 밤새 증발 → 0.2 μm 막 여과", standard="카드뮴 표준용액(PerkinElmer)으로 검량, 결과는 μg/g 건중량"),
  "rationale": "카드뮴 노출과 비타민 C 첨가의 축적 저감 효과를 평가하려고 측정했다[10]. 전문(2.3절) 확인 — 근육은 측정하지 않았고 검출한계·회수율은 논문에 없음[10].",
  "source": [10], "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9854703/", "source_kind": "paper"},
 {"role": "literature", "compound": "Creatine", "compound_ko": "크레아틴(크레아틴인산 포함)",
  "part": "흰 근육·아가미·간·혈액", "content": "근육 PCr+Cr 38.1 μmol/g, 크레아티닌 2.40 μmol/g[13]",
  "method": "과염소산 추출물 분석(세부 확인 못함)",
  "conditions": C(sample_prep="과염소산(PCA) 추출물"),
  "rationale": "근육 에너지 대사와 먹이 공급 상태를 보는 성분으로 측정되었다[13]. 전문 확인 못함 — 초록만 보아 기기·조건은 비워 둠[13].",
  "source": [13], "url": "https://pubmed.ncbi.nlm.nih.gov/24226895/", "source_kind": "paper"},
]

d = {"slug": "platichthys-stellatus", "name_ko": "강도다리", "name_en": "Starry flounder", "scientific_name": "Platichthys stellatus",
     "aliases": ["Starry flounder", "Diamond back"], "sections": sec, "compounds": compounds, "markers": [], "assays": assays,
     "nutrients": [], "production": [], "world": [], "gi": [], "orgs": [], "sources": S}
p = pathlib.Path(__file__).resolve().parent.parent / "dossier.json"
p.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in sec: print(s["key"], len(s["body"]))
