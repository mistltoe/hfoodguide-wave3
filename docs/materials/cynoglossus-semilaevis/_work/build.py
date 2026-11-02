import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
AC = "2026-11-02"
def pm(n, title, pmid, pub, pmc=None):
    url = f"https://pmc.ncbi.nlm.nih.gov/articles/{pmc}/" if pmc else f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
    return {"n": n, "title": title + f" (PMID {pmid})", "url": url, "publisher": pub, "accessed": AC}
S = [
 {"n":1,"title":"식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020)","url":"https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020","publisher":"식품의약품안전처","accessed":"2026-10-13"},
 pm(2,"Whole-genome sequence of a flatfish provides insights into ZW sex chromosome evolution and adaptation to a benthic lifestyle","24487278","Nature Genetics 46(3):253-260, 2014"),
 pm(3,"Epigenetic modification and inheritance in sexual reversal of fish","24487721","Genome Research 24(4):604-615, 2014","PMC3975060"),
 pm(4,"Transcriptome Profiling Insights the Feature of Sex Reversal Induced by High Temperature in Tongue Sole","31191622","Frontiers in Genetics 10:522, 2019","PMC6548826"),
 pm(5,"Evaluation of an Infertile, All-Male ZZ Line Exhibiting Female-like Growth in Chinese Tongue Sole: Growth Performance, Flesh Quality, and Muscle Metabolome","41514934","Biology 15(1):93, 2026","PMC12785089"),
 pm(6,"Effect of Plasma-Activated Water Pretreatment Combined with High-CO2 Modified Atmosphere Packaging on the Quality and Microbial Profile of Half-Smooth Tongue Sole During Superchilling Storage","41683115","Foods 15(3):529, 2026","PMC12896729"),
 pm(7,"Pharmacokinetics of sulfamonomethoxine in tongue sole (Cynoglossus semilaevis) after intravenous and oral administration","24577641","Fish Physiology and Biochemistry, 2014"),
 pm(8,"Establishment and identification of a skin cell line from Chinese tongue sole (Cynoglossus semilaevis) and analysis of the changes in its transcriptome upon LPS stimulation","37774902","Fish & Shellfish Immunology 142:109119, 2023"),
 pm(9,"A microsatellite genetic linkage map of half smooth tongue sole (Cynoglossus semilaevis)","23904060","Marine Genomics, 2012"),
 pm(10,"Genomics and transcriptomics reveal new molecular mechanism of vibriosis resistance in fish","36304468","Frontiers in Immunology 13:974604, 2022","PMC9592550"),
 pm(11,"Complete genome analysis of a virulent Vibrio scophthalmi strain VSc190401 isolated from diseased marine fish half-smooth tongue sole, Cynoglossus semilaevis","33176689","BMC Microbiology, 2020","PMC7661262"),
 pm(12,"Dysfunction of the intestinal physical barrier in the intestinal inflammation of tongue sole, Cynoglossus semilaevis, induced by Shewanella algae infection","37315911","Fish & Shellfish Immunology, 2023"),
 pm(13,"Development of a TaqMan Probe-Based Quantitative PCR Assay for the Detection of Cynoglossus semilaevis Papillomavirus","42797772","Viruses 18(9):939, 2026","PMC13611896"),
 pm(14,"Dietary DHA Regulated the Androgen Production in Male Chinese Tongue Sole","39949363","Aquaculture Nutrition, 2025","PMC11824814"),
 pm(15,"Effects of different dietary DHA:EPA ratios on gonadal steroidogenesis in the marine teleost, tongue sole (Cynoglossus semilaevis)","28831954","British Journal of Nutrition, 2017"),
 pm(16,"The effect of dietary arachidonic acid (ARA) on growth performance, fatty acid composition and expression of ARA metabolism-related genes in larval half-smooth tongue sole (Cynoglossus semilaevis)","25851526","British Journal of Nutrition, 2015"),
 pm(17,"Dietary Lactobacillus plantarum Supplementation Improves Growth and Modulates Hepatic and Immune-Related Responses in Tongue Sole","41976047","Animals 16(7):1068, 2026","PMC13072139"),
 pm(18,"Transcriptomic Analysis Revealed Candidate Genes Involved in Pseudomale Sperm Abnormalities in Chinese Tongue Sole","36552227","Biology 11(12):1716, 2022","PMC9775080"),
 pm(19,"Assembly of the poorly differentiated Verasper variegatus W chromosome by different sequencing technologies","38092799","Scientific Data 10:893, 2023","PMC10719390"),
 pm(20,"The ontogenesis of catabolic abilities and energy metabolism during endogenous nutritional periods of tongue sole, Cynoglossus semilaevis","34392536","Journal of Fish Biology, 2021"),
 pm(21,"Transcriptome profiles revealed high- and low-salinity water altered gill homeostasis in half-smooth tongue sole (Cynoglossus semilaevis)","35421665","Comparative Biochemistry and Physiology Part D, 2022"),
 pm(22,"Interactive impacts of CO2-induced seawater acidification and cadmium exposure on antioxidant defenses of juvenile tongue sole Cynoglossus semilaevis","38522335","Marine Pollution Bulletin, 2024"),
 pm(23,"A simple and rapid method for fish sex identification based on recombinase-aided amplification and its use in Cynoglossus semilaevis","34001931","Scientific Reports 11:10429, 2021","PMC8128863"),
 {"n":24,"title":"서해산 박대, Cynoglossus semilaevis 암컷의 성숙과 산란 (원문 접속 불가 — WebSearch 검색 요약으로만 확인)","url":"https://koreascience.kr/article/JAKO201225038990447.page","publisher":"한국과학기술정보연구원 koreascience(국내 학술지 논문), 2012","accessed":AC},
 {"n":25,"title":"한국수산학회지 게재 국내 참서대과 분포·분류 논문, 1994 (원문 접속 불가 — WebSearch 검색 요약으로만 확인)","url":"https://koreascience.kr/article/JAKO199423607599368.page","publisher":"한국수산과학회(koreascience 수록)","accessed":AC},
 {"n":26,"title":"참서대과 어종 판별용 다중 PCR 국내 논문, 2016 (원문 접속 불가 — WebSearch 검색 요약으로만 확인)","url":"https://koreascience.kr/article/JAKO201631267759889.pdf","publisher":"한국과학기술정보연구원 koreascience(국내 학술지 논문)","accessed":AC},
 pm(27,"Colwellia aquaemaris sp. nov., isolated from the Cynoglossus semilaevis culture tank in a recirculating mariculture system","25201915","International Journal of Systematic and Evolutionary Microbiology, 2014"),
 pm(28,"Role of Rab5b in the defense of Cynoglossus semilaevis against Vibrio vulnificus infection","41831502","International Journal of Biological Macromolecules, 2026"),
 pm(29,"The eye of the tongue sole Cynoglossus bilineatus (Lacepède, 1802) (Teleostei: Pleuronectiformes)","34953346","Tissue & Cell 74:101710, 2021"),
 pm(30,"Risk assessment of trace element accumulation in two species of edible commercial fish Scomberoides commersonnianus and Cynoglossus arel from the northern waters of the Oman Sea","34863073","Marine Pollution Bulletin, 2021"),
]
sec = {}
sec["overview"] = ("박대(학명 Cynoglossus semilaevis)는 식약처 「식품원료 목록」에 대표 원료명 '박대'로 올라 있는 바닷물고기로, 분류는 수산물, 사용 조건은 '사용가능'이다[1]. 목록의 부위 칸은 '-'이고 사용 조건 기준 칸과 이명·영문명 칸은 비어 있거나 '-'로 적혀 있어, 특정 부위나 제한 조건이 붙지 않은 원료다[1]. 학술 문헌에서는 half-smooth tongue sole 또는 Chinese tongue sole이라 부르는 가자미목(Pleuronectiformes) 참서대과(Cynoglossidae) 어류다[2, 5, 9].\n\n"
 "바닥에 사는 대형 어종으로 동북아시아 연안에 분포하며, 살이 부드럽고 즙이 많아 중국에서 가장 중요한 해산 양식 어종의 하나가 되었다[5, 6]. 국내에서는 주로 서해안과 남해 서부 연안에 분포한다고 기록된 국내 논문이 있으나, 원문을 열지 못해 검색 요약으로만 확인했다[25]. 암컷이 수컷보다 2–4배 빨리 자라는 성별 크기 차이가 커서 양식 연구의 중심 주제가 되어 왔다[5].\n\n"
 "ZW형 성염색체와 수온에 따른 성전환이 함께 나타나 유전체·후성유전 연구의 모델 어종으로도 쓰인다[2, 3]. 이 원료는 건강기능식품 고시형 원료의 원재료가 아니어서 고시 지표성분은 없다[1].")
sec["history"] = ("박대가 학계에 널리 알려진 계기는 2014년 수컷(ZZ)과 암컷(ZW)의 전장 유전체를 해독한 연구로, 이 연구는 성염색체 진화와 저서 생활 적응을 함께 다루었다[2]. 같은 해 가짜수컷(pseudomale)과 암컷·정상 수컷 생식소의 DNA 메틸화를 비교한 연구가 나와, 환경에 따른 성 결정의 후성유전 기전을 보여 주는 대표 사례가 되었다[3]. 그 전인 2012년에는 미세위성 표지 325개로 암수별 유전 연관지도가 만들어졌고, 이 논문은 박대를 중국 연안 전역의 중요한 양식 종으로 소개했다[9].\n\n"
 "최근 20년 사이 중국에서 대규모 종자 생산 기술이 개발되어 산업형 양식의 모범 종이 되었다는 서술이 있다[5]. 국내에서는 1990년대 참서대과 분포 연구와 2010년 서해에서 잡은 개체로 암컷 성숙·산란을 조사한 2012년 연구가 있으나, 두 논문 모두 원문을 열지 못해 검색 요약으로만 확인했다[24, 25].\n\n"
 "우리말 이름 '박대'의 어원과 옛 문헌 기록은 이번 조사에서 공공기관·학술 원문으로 확인하지 못함. 식약처 목록에는 '박대' 한 가지 원료명만 올라 있고 별칭은 적혀 있지 않다[1].")
sec["biology"] = ("박대는 온대 바다의 바닥에 사는 큰 저서성 넙치류로, 유전체 연구는 저서 생활에 대한 적응 형질을 함께 분석했다[2, 6]. 넓은 범위의 염분을 견디는 광염성 어종이어서, 염분 8 ppt·24 ppt·32 ppt에서 아가미 전사체를 비교한 연구가 있다[21]. 고염분에서는 아가미에 미토콘드리아가 많은 세포가 늘었고, 저염분에서는 2,137개 유전자의 발현이 달라졌다[21].\n\n"
 "성은 ZZ/ZW 염색체로 정해지지만 유전적 암컷(ZW)이 높은 수온 등으로 표현형 수컷, 곧 가짜수컷이 될 수 있다[3, 4]. 양식 개체에서 15개월령 암컷은 평균 654.53 g, 43.5 cm까지 자란 반면 같은 사육 조건의 dmrt1 편집 ZZ 수컷이 야생형 수컷의 3.2배 무게였을 만큼 야생형 수컷은 훨씬 작았다[5]. 피부 세포주의 핵형 분석에서 염색체 수는 2n = 42였다[8].\n\n"
 "수정란은 물에 뜨는 부성란이며, 가라앉은 알은 죽은 알로 본다[5]. 수정 후 38.8시간에 부화하고 부화 3일째에 입이 열리며, 배 발생 중 가장 빠른 성장은 부화 전 포배기에 관찰되었다[20]. 국내 서해 개체를 조사한 연구에서 암컷의 생물학적 최소형은 전장 46.87 cm였다는 내용은 검색 요약으로만 확인했다[24].")
sec["related_species"] = ("식약처 목록에는 같은 속의 용서대(Cynoglossus abbreviatus), 큰개서대(C. bilineatus), 홍서대(C. dubius), 칠서대(C. interruptus), 참서대(C. joyneri), 개서대(C. robustus)가 각각 별개 원료로 올라 있다[1]. 같은 속의 세네갈개서대(C. senegalensis)와 영문명으로만 오른 Bengal tongue sole(C. cynoglossus)도 따로 있다[1]. 따라서 이 종들의 성분·안전 자료를 박대 자료로 옮겨 쓰지 않는다[1].\n\n"
 "이름에 '서대'가 들어가지만 속이 다른 원료도 많아, 흑대기(Paraplagusia japonica)는 이명이 '서덕이, 서대'이고 각시서대(Pseudaesopia japonica)·노랑각시서대(Zebrias fasciatus)도 따로 올라 있다[1]. 참서대과 어류는 겉모습이 비슷해 유통 어종을 가리는 다중 PCR 판별법이 국내에서 개발되었고 박대도 대상에 들어 있다는 내용은 검색 요약으로만 확인했다[26].\n\n"
 "학술 문헌에서도 큰개서대(C. bilineatus)의 눈 조직 연구나 오만해 C. arel의 중금속 위해성 평가는 박대가 아닌 다른 종의 결과다[29, 30]. 가자미목에서 박대와 범가자미(Verasper variegatus)는 같은 ZZ/ZW 성결정 체계지만, 성염색체가 서로 다른 조상 원시염색체에서 유래했다[19].")
sec["cultivation"] = ("박대는 중국 동부 연안에서 양식 규모가 커진 어종으로, 양식이 늘면서 세균성 질병이 잦아져 피부 충혈·궤양 같은 증상이 흔한 문제가 되었다[8]. 중국 탕산의 양식장 사례에서는 수온 23–24 °C, 염분 18–22‰, 하루 3시간 정도의 조명 아래 콘크리트 수조에서 길렀고, 밀도는 8개월령 1 m²당 약 65마리에서 15개월령 약 15마리로 줄였다[5]. 이때 먹인 배합사료는 조단백질 52.0% 이상, 조지방 9.0% 이상, 라이신 2.5% 이상이었다[5].\n\n"
 "어미는 LHRH-A3와 돔페리돈 주사로 산란을 유도해 인공 수정하는 방법이 쓰였다[5]. 중국 톈진의 순환여과식 해수 양식 시스템에서 박대를 기르는 수조가 운영되었고, 그 수조에서 새로운 세균 종이 분리·보고되기도 했다[27]. 사료 연구로는 자어 사료의 아라키돈산이 건물 기준 1.42%일 때 생존율과 성장이 가장 좋았다는 결과가 있다[16]. 유산균(Lactobacillus plantarum)을 사료 1 kg당 1,000 mg 넣어 10주간 먹이자 치어의 최종 체중과 특이성장률이 대조구보다 높았다[17].\n\n"
 "질병으로는 Vibrio scophthalmi, Shewanella algae, Vibrio vulnificus 감염과 박대 유두종바이러스(CsPaV)가 보고되었다[11, 12, 13, 28]. 2023–2026년에 모은 병든 박대 176마리 가운데 80.68%가 CsPaV 양성이었다[13]. 국내 박대 어획·양식 생산 통계는 이번 조사에서 통계청·해양수산부 원문으로 확인하지 못함.")
sec["processing"] = ("식약처 목록에는 박대가 원료명 한 가지로만 올라 있어, 가공품 이름(말린 것, 묵 등)이 원료명으로 따로 등록되어 있지는 않다[1]. 국내에서 말린 박대나 박대 껍질로 쑨 묵처럼 지역에서 쓰이는 가공·조리법은 이번 조사에서 공공기관·학술 원문으로 확인하지 못함.\n\n"
 "중국 저우산 수산시장에서 산 1,500 ± 50 g 박대의 살 조각을 플라즈마 활성수에 10분 담근 뒤 여러 방식으로 포장해 −1 °C에서 60일간 저장한 연구가 있다[6]. 처음 측정값은 일반세균수 2.70 log CFU/g, 휘발성 염기질소 8.43 mg N/100 g, K값 8.16%였다[6]. 공기 포장구는 20일째 일반세균수가 7.0 log CFU/g을 넘고, 30일째 관능 점수가 기준 아래로 떨어졌으며, 45일째 K값이 60%를 넘었다[6]. 이산화탄소 75%·산소 5%·질소 20%의 가스 치환 포장이 휘발성 염기질소와 K값 상승을 가장 잘 늦췄지만, 지방 산화 지표(TBARS)는 오히려 가스 치환 포장구에서 높았다[6].\n\n"
 "근육의 수분·회분·조단백질·조지방, 아미노산 16종, 지방산 24종을 비교한 연구에서 야생형 수컷은 암컷보다 근육 지방이 유의하게 많았고 오메가-6 지방산은 적었다[5]. 이 연구의 개별 함량 수치는 본문에 없고 보충 표에만 있어 이번 조사에서 확인하지 못함.")
sec["genetics"] = ("2014년 유전체 해독에서 박대의 성염색체는 조류의 W·Z 염색체와 같은 척추동물 조상 원시염색체에서 유래했고, 조류의 수컷 결정 유전자인 dmrt1이 박대의 Z 염색체에도 있어 비슷한 기능을 하도록 수렴 진화한 특징을 보였다[2]. 성염색체가 생긴 직후 대량의 유전자 소실이 일어났다는 점도 함께 보고되었다[2].\n\n"
 "가짜수컷의 생식소에서는 성결정 경로 유전자들이 메틸화로 크게 바뀌었고, 이 메틸화 양상이 ZW 자손에게 유전되어 고온 처리 없이도 가짜수컷이 생겼다[3]. 고수온 처리는 암컷 생식소의 cyp19a1a(방향화효소) 프로모터 메틸화를 높였고, 메틸화 수준과 이 유전자 발현은 음의 상관을 보였다[4]. 가짜수컷은 Z형 정자만 만들고 W형 정자는 만들지 못한다[18].\n\n"
 "W 염색체를 겨냥한 재조합효소 증폭(RAA) 검사로 약 30분 만에 수컷·가짜수컷·암컷의 유전적 성을 가리는 방법이 나왔다[23]. 유전체 편집으로 dmrt1에 8 bp 결실을 지닌 ZZ 수컷 4세대는 완전 불임이었고, 15개월령 체중이 638.76 g으로 야생형 암컷과 비슷하며 야생형 수컷의 3.2배였다[5]. 비브리오병 저항 가계는 콘드로이틴황산·더마탄황산 대사 유전자에 선택 흔적이 있었고, 그 합성 효소 Chst12가 직접 항균 활성을 보였다[10].")
sec["safety"] = ("박대는 식약처 「식품원료 목록」에 '사용가능' 수산물로 올라 있으며 부위·조건 제한은 적혀 있지 않다[1]. 이 원료는 건강기능식품 고시형 원료가 아니어서 고시 섭취 시 주의사항은 없다[1]. 생선 알레르기, 수산물 중금속 기준 등 식약처 공전의 수치는 식품안전나라 원문에 접속하지 못해 이번 조사에서 확인하지 못함.\n\n"
 "양식 약물과 관련해, 설파모노메톡신을 체중 1 kg당 200 mg 먹인 박대(20 °C)에서 혈장 최고 농도는 2.5시간에 58 mg/L였고 제거 반감기는 95.7시간, 생체이용률은 39.5%였다[7]. 정맥 주사(40 mg/kg) 때 제거 반감기는 80.4시간이어서, 이 약은 박대 몸에서 오래 머무는 편이다[7]. 이 약물의 국내 잔류허용기준과 휴약기간은 이번 조사에서 확인하지 못함. 비브리오 감염 치료에 쓰는 항생제는 효과와 환경 문제로 제약이 있다고 연구자들이 지적했다[28].\n\n"
 "실험실에서 어린 박대를 해수 산성화와 카드뮴에 함께 노출하면 지질 과산화가 늘었으나, 이는 노출 실험 결과이지 시판 박대의 카드뮴 함량 조사가 아니다[22]. 다른 종(C. arel)의 중금속 위해성 평가 결과를 박대에 그대로 적용하지 않는다[30]. 보고된 박대 병원체(V. scophthalmi, S. algae, CsPaV 등)는 양식 어류의 질병 원인으로 연구되었다[11, 12, 13].")
titles = {"overview":"한눈에 보기","history":"이름과 연구의 역사","biology":"어종과 생태","related_species":"가까운 종과 혼동","cultivation":"어획과 양식","processing":"가공과 이용","genetics":"유전체와 성 결정","safety":"안전성과 식품원료 지위"}
sections = [{"key":k,"title":titles[k],"body":sec[k]} for k in titles]
def c(name, ko, cls, role, part, content, act, src):
    return {"name":name,"name_ko":ko,"class":cls,"role":role,"part":part,"content_text":content,"activity_ko":act,"source":src}
compounds = [
 c("Docosahexaenoic acid","도코사헥사엔산(DHA)","오메가-3 지방산","nutrient","수컷 어미(사료 시험)","사료 총지방산 중 DHA 5.16%·8.93%·16.47% 시험구 비교; 박대 근육 함량 수치는 확인하지 못함[14]","사료 DHA가 많을수록 수컷 혈청 테스토스테론·11-케토테스토스테론이 늘었다(사료 시험)[14].",[14]),
 c("Eicosapentaenoic acid","에이코사펜타엔산(EPA)","오메가-3 지방산","nutrient","3년생 어미 생식소·조직(사료 시험)","사료 DHA:EPA 비 0.68·1.09·2.05 시험; 조직 지방산 조성은 사료를 반영함[15]","DHA:EPA 1.09 사료는 암컷 에스트라디올, 2.05 사료는 수컷 테스토스테론 생산을 높였다(사료 시험)[15].",[15]),
 c("Arachidonic acid","아라키돈산(ARA)","오메가-6 지방산","nutrient","자어(부화 후 35일)","사료 ARA 0.01–2.86%(건물) 시험, 1.42%에서 생존·성장 최대; 자어 EPA는 사료 ARA가 늘수록 감소[16]","자어의 생존율과 성장에 필요한 필수 지방산으로 평가되었다[16].",[16]),
 c("Chondroitin sulfate","콘드로이틴황산","글리코사미노글리칸","bioactive","비브리오병 저항 가계 조직","저항 가계에서 함량 증가가 추정됨(정량값 없음)[10]","저항 가계에서 합성 경로 유전자 발현이 협조적으로 늘어 세포외기질 장벽 강화와 연관이 제시되었다[10].",[10]),
 c("Dermatan sulfate","더마탄황산","글리코사미노글리칸","bioactive","비브리오병 저항 가계 조직","콘드로이틴황산과 함께 증가가 추정됨(정량값 없음)[10]","합성 효소 Chst12가 직접 항균 활성을 보였다(실험실 결과)[10].",[10]),
 c("Pyroglutamic acid","L-피로글루탐산","아미노산 유도체","bioactive","근육(12–15개월령 양식어)","dmrt1 편집 ZZ 수컷 근육에서 상대적으로 증가(비표적 대사체 분석, 절대 함량 없음)[5]","글루타티온 회전과 연결된 항산화 관련 대사체로 해석되었다[5].",[5]),
 c("Dopamine","도파민","카테콜아민","bioactive","근육(양식어)","ZZ 수컷 근육에서 상대적 증가(절대 함량 없음)[5]","신경전달 관련 대사체로 해석되었으나 기능은 추가 검증이 필요하다고 저자가 적었다[5].",[5]),
 c("Glutamic acid","글루탐산","아미노산","nutrient","근육(양식어)","ZZ 수컷 근육에서 상대적 증가(절대 함량 없음)[5]","신경전달 관련 대사체로 분류되었다[5].",[5]),
 c("Dodecanoic acid","도데칸산(라우르산)","포화지방산","bioactive","근육(양식어)","ZZ 수컷 근육에서 상대적 증가(절대 함량 없음)[5]","저자들은 다른 연구를 인용해 혈압·항종양 관련 가능성을 언급했으나 박대에서 검증되지 않았다[5].",[5]),
 c("Lysine","라이신","필수아미노산","nutrient","양식 사료","시험 사료 라이신 2.5% 이상[5]","사료 라이신을 적절히 보충하면 박대 성장이 나아진다는 선행 연구가 인용되었다[5].",[5]),
 c("Inosine monophosphate","이노신일인산(IMP)","핵산 관련 물질","marker","살(시장 구입 개체)","K값 계산 성분; 저장 시작 시 K값 8.16%[6]","ATP 분해 산물 비율(K값)로 선도를 판정하는 데 쓰였다[6].",[6]),
 c("Hypoxanthine","하이포잔틴","퓨린 염기","marker","살(시장 구입 개체)","K값 계산 성분; 공기 포장구 45일째 K값 60% 초과[6]","ATP 최종 분해 산물로 K값을 높여 선도 저하를 나타낸다[6].",[6]),
]
assays = [
 {"role":"literature","compound":"Total volatile basic nitrogen","compound_ko":"휘발성 염기질소(TVB-N)","part":"시장 구입 박대(1,500 ± 50 g) 살 조각, 플라즈마 활성수 처리 후 −1 °C 저장","content":"저장 시작 시 8.43 mg N/100 g[6]","method":"켈달 질소분석기 증류법","conditions":{"instrument":"켈달 질소분석기(Haineng K1100)","column":"","mobile_phase":"","gradient":"","flow":"","temp":"","detection":"","injection":"","sample_prep":"살 5 g","standard":"","linearity":"","lod":"","loq":"","recovery":""},"rationale":"단백질 분해로 생기는 염기성 질소로 수산물 부패 정도를 나타내는 선도 지표다[6]. 전문(Methods 2.6) 확인 — 시약·검출한계·회수율은 논문에 없음[6].","source":[6],"url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12896729/","source_kind":"paper"},
 {"role":"literature","compound":"Inosine monophosphate (K value)","compound_ko":"이노신일인산 등 ATP 분해산물(K값)","part":"시장 구입 박대 살","content":"저장 시작 시 K값 8.16%[6]","method":"HPLC","conditions":{"instrument":"Waters 2695 HPLC","column":"","mobile_phase":"","gradient":"","flow":"","temp":"","detection":"","injection":"","sample_prep":"살 5 g + 10% 과염소산 10 mL 균질 → 8000×g, 4 °C 10분 원심 → 침전을 5% 과염소산 10 mL로 2회 세척해 상등액 합침 → 1 M·10 M 수산화칼륨으로 pH 6.0–6.5 조정 → 0.22 μm 여과, −20 °C 보관","standard":"","linearity":"","lod":"","loq":"","recovery":""},"rationale":"ATP·ADP·AMP·IMP·이노신·하이포잔틴 중 이노신과 하이포잔틴의 비율(K값)로 선도를 판정한다[6]. 전문(Methods 2.7) 확인 — 칼럼·이동상·검출 파장은 논문에 없고 인용 문헌 방법을 따랐다고만 적음[6].","source":[6],"url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12896729/","source_kind":"paper"},
 {"role":"literature","compound":"Muscle metabolites (untargeted, e.g. pyroglutamic acid)","compound_ko":"근육 대사체(비표적, L-피로글루탐산 등)","part":"근육(야생형 암·수, dmrt1 편집 ZZ 수컷)","content":"대사체 1,262종 동정; ZZ 수컷 대 야생형 암컷 98종, 대 야생형 수컷 108종 차이(상대 비교, 절대 함량 없음)[5]","method":"UHPLC-Orbitrap MS(비표적 대사체)","conditions":{"instrument":"Vanquish UHPLC + Orbitrap Exploris 480","column":"ACQUITY UPLC BEH Amide 1.7 μm, 2.1 × 100 mm","mobile_phase":"A: 물 중 25 mM 아세트산암모늄 + 25 mM 수산화암모늄, B: 아세토니트릴","gradient":"95% B 0.5분 → 6.5분에 65% B → 1분에 40% B(1분 유지) → 0.1분에 95% B → 2.9분 재평형","flow":"","temp":"","detection":"양·음이온 모드 고분해능 질량분석","injection":"","sample_prep":"근육을 액체질소에서 분쇄 → 차가운 에탄올·아세토니트릴·물(2:2:1) 현탁, −20 °C 10분 → 14,000×g 20분 원심 → 상등액 진공건조 → 아세토니트릴·물(1:1) 재용해 → 14,000×g 15분 원심","standard":"","linearity":"","lod":"","loq":"","recovery":""},"rationale":"유전체 편집 어류와 야생형의 살 품질 차이를 넓게 훑기 위한 탐색적 분석이다[5]. 전문(Methods 2.7) 확인 — 유속·칼럼 온도·검출한계는 논문에 없음, 다중비교 보정을 하지 않은 탐색 결과라고 저자가 밝힘[5].","source":[5],"url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12785089/","source_kind":"paper"},
 {"role":"literature","compound":"Sulfamonomethoxine","compound_ko":"설파모노메톡신(양식 약물)","part":"혈장","content":"경구 200 mg/kg 투여(20 °C) 후 2.5시간에 최고 58 mg/L, 제거 반감기 95.7시간[7]","method":"","conditions":{},"rationale":"양식 약물의 체내 동태로 잔류·휴약 판단의 기초 자료다[7]. 초록만 확인 — 분석 기기·조건은 전문 확인 못함[7].","source":[7],"url":"https://pubmed.ncbi.nlm.nih.gov/24577641/","source_kind":"paper"},
]
d = {"slug":"cynoglossus-semilaevis","name_ko":"박대","name_en":"Half-smooth tongue sole","scientific_name":"Cynoglossus semilaevis",
 "aliases":["Chinese tongue sole","Half-smooth tongue sole","Tongue sole"],
 "sections":sections,"compounds":compounds,"markers":[],"assays":assays,"nutrients":[],"production":[],"world":[],"gi":[],"orgs":[],"sources":S}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
