import json
from pathlib import Path
A="2026-11-02"
def P(n,title,url,pub,acc=A): return {"n":n,"title":title,"url":url,"publisher":pub,"accessed":acc}
sources=[
P(1,"식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 캐롤라이나해만가리비(대서양해만가리비) 항목 및 국립생물자원관 연결 자료","https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020","식품의약품안전처","2026-10-13"),
P(2,"Characteristic Profile of the Hazardous, Nutritional, and Taste-Contributing Compounds during the Growth of Argopecten irradians with Different Shell Colors. Foods 2023;12(23):4354","https://doi.org/10.3390/foods12234354","Foods (MDPI), PMC10706102"),
P(3,"Chromosome-level genome assembly of the bay scallop Argopecten irradians. Sci Data 2024;11:1057","https://doi.org/10.1038/s41597-024-03904-x","Scientific Data, PMC11439060"),
P(4,"Draft genomes of two Atlantic bay scallop subspecies Argopecten irradians irradians and A. i. concentricus. Sci Data 2020;7:99","https://doi.org/10.1038/s41597-020-0441-7","Scientific Data, PMC7090048"),
P(5,"Genome-Wide Association Study Reveals a candidate gene for Thermal Tolerance in Bay Scallop (Argopecten irradians). Front Genet 2021;12:650045","https://doi.org/10.3389/fgene.2021.650045","Frontiers in Genetics, PMC8328476"),
P(6,"Aquaculture Strategy and Genetic Diversity of Argopecten irradians concentricus in Beibu Gulf, China. Biology 2025;14(8):1103","https://doi.org/10.3390/biology14081103","Biology (MDPI), PMC12383437"),
P(7,"SNP identification by transcriptome sequencing and candidate gene-based association analysis for heat tolerance in the bay scallop Argopecten irradians. PLoS One 2014;9(8):e104960","https://doi.org/10.1371/journal.pone.0104960","PLoS One, PMC4133247"),
P(8,"An apicomplexan parasite drives the collapse of the bay scallop population in New York. Sci Rep 2023;13:6655","https://doi.org/10.1038/s41598-023-33514-3","Scientific Reports, PMC10126089"),
P(9,"Survival of the fittest: genomic investigations of the bay scallop reveal a shift in population structure through a summer mortality event. BMC Genomics 2025;26:146","https://doi.org/10.1186/s12864-025-11337-y","BMC Genomics, PMC11829576"),
P(10,"Transcriptomic profiling of the thermal tolerance in two subspecies of the bay scallop Argopecten irradians. Comp Biochem Physiol D 2024;51:101246","https://doi.org/10.1016/j.cbd.2024.101246","Comparative Biochemistry and Physiology Part D (PubMed 38781887)"),
P(11,"해만가리비(Argopecten irradians)의 동해 북부에서의 양식 연구. 한국패류학회지 2016;32(4):279–287 (초록)","https://doi.org/10.9710/kjm.2016.32.4.279","한국패류학회(Korean Journal of Malacology)"),
P(12,"Draft genome and SNPs associated with carotenoid accumulation in adductor muscles of bay scallop (Argopecten irradians). J Genomics 2017;5:83–90","https://doi.org/10.7150/jgen.19146","Journal of Genomics, PMC5535694"),
P(13,"Taste properties and mechanism of umami peptides from bay scallop (Argopecten irradians) by-products based on molecular docking and molecular dynamics simulation. Curr Res Food Sci 2026:101412","https://doi.org/10.1016/j.crfs.2026.101412","Current Research in Food Science, PMC13126457"),
P(14,"Potential roles of hydroxybenzoate paralytic shellfish toxins in modulating toxin biokinetics in scallops. J Hazard Mater 2024;468:133896","https://doi.org/10.1016/j.jhazmat.2024.133896","Journal of Hazardous Materials (PubMed 38428300)"),
P(15,"Contamination of shellfish from Shanghai seafood markets with paralytic shellfish poisoning and diarrhetic shellfish poisoning toxins determined by mouse bioassay and HPLC. Food Addit Contam 2005;22(7)","https://doi.org/10.1080/02652030500137017","Food Additives and Contaminants (PubMed 16019840)"),
P(16,"Heavy metals pollution and health risk assessment in farmed scallops: Low level of Cd in coastal water could lead to high risk of seafood. Ecotoxicol Environ Saf 2021;208:111768","https://doi.org/10.1016/j.ecoenv.2020.111768","Ecotoxicology and Environmental Safety (PubMed 33396086)"),
P(17,"Distribution of As, Cd, and Pb in seafood in Southern China and their oral bioavailability in mice. Environ Sci Pollut Res 2017","https://doi.org/10.1007/s11356-016-8095-x","Environmental Science and Pollution Research (PubMed 27882492)"),
P(18,"Marine Toxin Okadaic Acid Affects the Immune Function of Bay Scallop (Argopecten irradians). Molecules 2016;21(9):1108","https://doi.org/10.3390/molecules21091108","Molecules (MDPI), PMC6272952"),
P(19,"Mechanism of antioxidant action of natural phenolics on scallop (Argopecten irradians) adductor muscle during drying process. Food Chem 2019","https://doi.org/10.1016/j.foodchem.2018.12.108","Food Chemistry (PubMed 30658755)"),
P(20,"Oxidation kinetics of polyunsaturated fatty acids esterified into triacylglycerols and phospholipids in dried scallop (Argopecten irradians) adductor muscles during storage. Food Funct 2020","https://doi.org/10.1039/d0fo00051e","Food & Function (PubMed 32125340)"),
P(21,"Independent and combined effects of ultrasound and transglutaminase on the gel properties and in vitro digestion characteristics of bay scallop (Argopecten irradians) adductor muscle. Curr Res Food Sci 2022;5:1254","https://doi.org/10.1016/j.crfs.2022.07.009","Current Research in Food Science, PMC9364047"),
P(22,"Combined effects of ultrasound and antioxidants on the quality maintenance of bay scallop (Argopecten irradians) adductor muscles during cold storage. Ultrason Sonochem 2021;82:105883","https://doi.org/10.1016/j.ultsonch.2021.105883","Ultrasonics Sonochemistry, PMC8799608"),
P(23,"Combined use of fatty acid profile and fatty acid δ13C fingerprinting for origin traceability of scallops (Patinopecten yessoensis, Chlamys farreri, and Argopecten irradians). Food Chem 2019","https://doi.org/10.1016/j.foodchem.2019.124966","Food Chemistry (PubMed 31260996)"),
P(24,"Transcriptomic and proteomic analyses of genetic factors influencing adductor muscle coloration in QN Orange scallops. BMC Genomics 2019;20:363","https://doi.org/10.1186/s12864-019-5717-y","BMC Genomics, PMC6509969"),
P(25,"Bioconversion of 13C-labeled microalgal phytosterols to cholesterol by the Northern Bay scallop, Argopecten irradians irradians. Comp Biochem Physiol B 2016","https://doi.org/10.1016/j.cbpb.2015.11.003","Comparative Biochemistry and Physiology Part B (PubMed 26577022)"),
P(26,"Comparative peptidomic profile and bioactivities of Pacific oyster, Mytilus edulis, Argopecten irradians, Meretrix meretrix L. after simulated gastrointestinal digestion. Eur J Nutr 2026","https://doi.org/10.1007/s00394-026-03901-3","European Journal of Nutrition (PubMed 41677889)"),
P(27,"Alteration of metallothionein mRNA in bay scallop Argopecten irradians under cadmium exposure and bacteria challenge. Comp Biochem Physiol C 2008","https://doi.org/10.1016/j.cbpc.2008.07.001","Comparative Biochemistry and Physiology Part C (PubMed 18662805)"),
P(28,"Development and linkage analysis of 104 new microsatellite markers for bay scallop (Argopecten irradians). Mar Biotechnol 2011","https://doi.org/10.1007/s10126-011-9383-6","Marine Biotechnology (PubMed 21590517)"),
]

S=[]
def sec(k,t,b): S.append({"key":k,"title":t,"body":b.strip()})
sec("overview","한눈에 보기","""
캐롤라이나해만가리비(Argopecten irradians)는 가리비과(Pectinidae) 해만가리비속에 드는 바다 조개로, 식약처 「식품원료 목록」에는 '대서양해만가리비'와 '캐롤라이나해만가리비'라는 두 원료명으로 올라 있다[1]. 이 목록에서 이 종의 상태는 '사용가능'이고, 사용 부위는 따로 정하지 않은 '-'로 적혀 있으며 별도의 사용 조건은 없다[1]. 목록에 연결된 학명은 북방 아종 A. irradians irradians와 남방 아종 A. irradians concentricus 두 가지다[1]. 영어로는 bay scallop이라 부르고, 식품원료 목록의 영문명은 Carolina bay scallop이다[1, 3].

원산지는 미국 동부 연안이며, 중국에 들여와 큰 양식 산업을 이루었다[3]. 주로 먹는 부위는 관자(폐각근)로, 단백질이 많고 지방이 적으며 타우린·베타인·유리아미노산 같은 맛 성분이 풍부하다고 보고되었다[2]. 건강기능식품 고시형 원료의 원재료는 아니어서 식약처가 정한 지표성분은 없다[1].
""")
sec("history","이용 역사","""
이 종은 미국 동부 연안에 본래 사는 가리비로, 미국에서는 상업·여가 어업과 지역 문화에서 중요한 종으로 소개된다[3, 9]. 북방 아종은 1980년대에, 남방 아종은 1990년대에 중국으로 들여왔다고 보고되었다[7]. 중국 북부 양식 집단의 도입 시기를 1982년으로 적은 연구가 있고, 남방 아종은 1991년에 중국에 들어와 광시 베이부만 양식의 주요 산업이 되었다[5, 6].

중국에서는 1990년대 양식 기술이 자리 잡은 뒤 주요 양식 가리비가 되었으며, 산둥성 룽청 일대에서는 7월 말 채롱에 넣어 8–9월 기르고 10월에 수확해 판다[2]. 반면 원산지인 미국 뉴욕에서는 2019년부터 여름마다 대량 폐사가 일어나 성체 생물량이 90–99% 줄었고, 그 원인으로 콩팥에 감염하는 정단복합충류 기생충이 지목되었다[8].

국내에서는 국립수산과학원 연구진이 2015년 강원 양양 시험어장에서 시험양식을 했고, 그 논문 초록은 이 종이 그때까지 국내에서 남해에서만 양식되어 왔다고 적었다[11].
""")
sec("biology","어종·형태·생태","""
캐롤라이나해만가리비는 연체동물문 이매패강 가리비과에 속하는 해산 이매패류다[1]. 미국 뉴잉글랜드에서 멕시코만에 이르는 하구와 연안에 산다[9]. 수온 변화에 넓게 견디는 광온성 종이지만, 북방 아종과 남방 아종은 고수온에 대한 반응이 서로 다르다고 보고되었다[10].

중국 룽청 양식장에서 3개월 된 개체는 8월에서 10월 사이 각장이 35.2 mm에서 68.3 mm로, 전중량이 7.64 g에서 29.26 g으로 자랐다[2]. 같은 연구에서 육질 비율은 43.83–50.64%였고, 껍데기 색이 금색인 계통과 보라색인 계통이 함께 조사되었다[2]. 8월에는 산란기여서 지방 함량이 9–10월보다 높았다[2].

이매패류는 콜레스테롤을 스스로 만들지 못해 먹이 미세조류의 식물성 스테롤을 콜레스테롤로 바꿔 쓰며, 이 종의 북방 아종에서도 그런 전환이 확인되었다[25]. 관자는 보통 흰색이지만 중국 양식 개체의 약 0.1% 이하에서 카로티노이드가 쌓인 주황색 관자가 관찰되었다[12].
""")
sec("related_species","관련 종·이름","""
식품원료 목록은 이 종에 대서양해만가리비·캐롤라이나해만가리비라는 두 이름을 붙였고, 학명으로 A. irradians irradians와 A. irradians concentricus를 함께 연결했다[1]. 두 아종은 중국에서 각각 북부와 남부의 주요 양식종이며, 각각 따로 유전체가 해독되었다[4]. 중국 연구에서는 북방 아종 가운데 '한국 집단(Korean population)'으로 부른 계통을 남방 아종과 비교한 예도 있다[10].

같은 속에는 페루가리비(A. purpuratus) 등이 있으며, 중국에서는 이 종과 페루가리비의 종간 잡종에서 관자가 주황색인 'QN Orange' 계통을 골라 길렀다[24]. 이 잡종 계통의 성분·안전 자료는 이 문서에 섞지 않았다[24].

시장에서 흔히 함께 팔리는 가리비로 중국 연구는 이 종과 함께 참가리비(Patinopecten yessoensis)·비단가리비(Chlamys farreri)를 조사했고, 지방산 조성과 탄소 동위원소 지문으로 세 종과 산지를 구별할 수 있었다[23].

국내에서는 이 종을 흔히 '해만가리비'라 부르며, 국립수산과학원 연구 논문도 이 이름을 썼다[11]. 한국어 이름의 유래를 적은 공식 자료는 확인하지 못함.
""")
sec("cultivation","양식·채취","""
중국 산둥성 룽청 아이롄만 양식장에서는 7월 말 치패를 채롱에 넣고 8–9월 기른 뒤 10월에 수확하며, 조사 기간 수온은 17.1–23.5 ℃, 염분은 23.20–26.70이었다[2]. 2022년 중국의 가리비류 전체 양식 생산량은 179.2만 t으로 굴·바지락류 다음이었고, 그 가운데 산둥성이 약 98.39만 t을 차지했다[2]. 이 수치는 가리비류 전체이며, 이 종만의 생산량은 확인하지 못함.

광시 베이부만의 남방 아종 양식에서는 수용 밀도가 높을수록 성장이 유의하게 느렸고, 선발 육종 집단은 대조 집단보다 잘 자랐지만 유전 다양성은 낮았다[6]. 고수온에 따른 대량 폐사가 양식의 큰 문제가 되어 내열성 관련 유전자와 표지를 찾는 연구가 이어지고 있다[5, 7].

국내에서는 국립수산과학원이 2015년 6월 강원 양양 시험어장에 치패를 넣었고, 12월까지 각장 약 56 mm, 전중량 약 26 g으로 자라 동해 북부에서도 양식이 가능하다고 보고했다[11]. 국내 이 종의 연도별 생산 통계는 공식 자료에서 확인하지 못함.
""")
sec("processing","가공·추출 연구","""
이 종의 관자는 날것·냉장품 외에 말린 관자로도 많이 가공되며, 열풍 건조 중 지질 가수분해와 산화가 일어나 차 폴리페놀과 대나무잎 항산화제로 지질 산화를 늦추는 방법이 연구되었다[19]. 말린 관자를 저장하는 동안 중성지방과 인지질에 결합한 EPA·DHA 등 고도불포화지방산의 산화 속도를 비교한 연구도 있다[20].

관자 근원섬유 단백질로 어묵 같은 겔 제품을 만들기 위해 초음파와 트랜스글루타미네이스를 함께 쓰면 겔 강도가 대조군보다 82.3% 높아졌다[21]. 냉장 저장 중에는 350 W 초음파와 2% 대나무잎 항산화제 용액을 함께 처리해 관자의 품질 유지 효과를 살폈다[22].

관자를 떼어낸 뒤 남는 외투막·생식소 같은 부산물은 효소로 분해해 감칠맛 펩타이드를 얻는 원료로 연구되었고, 세 가지 새 펩타이드(AHELPRYG, HELPRY, WDGRDGAVD)의 감칠맛 역치는 0.10–0.51 mmol/L였다[13]. 굴·홍합·백합과 함께 모의 소화한 비교 연구에서 이 종은 단백질이 많고 지방이 적은 식품으로 분류되었다[26].
""")
sec("genetics","유전 정보","""
PacBio와 Hi-C 자료로 조립한 염색체 수준 참조 유전체는 전체 845.9 Mb이고, 92.9%가 16개 염색체에 해당하는 가장 큰 스캐폴드 16개에 담겼다[3]. 이 유전체에는 단백질 암호 유전자 33,772개가 있고, 반복 서열은 약 36.2%, BUSCO 완성도는 96.2%였다[3].

그보다 앞서 북방 아종과 남방 아종의 초안 유전체가 각각 835.7 Mb, 874.82 Mb로 조립되었고, 단백질 암호 유전자는 각각 26,777개와 25,979개로 예측되었다[4]. 2017년 유전체 조사 분석은 유전체 크기를 약 990 Mb, 이형접합도를 0.9%로 추정했다[12].

내열성 연구에서는 435개체와 SNP 38,011개로 전장 유전체 연관 분석을 해 16개 염색체 전체에서 1,906개의 관련 SNP를 찾았다[5]. 연관 지도 작성용 미세부수체 표지 104개도 개발되었다[28]. 미국 뉴욕에서는 기생충에 의한 대량 폐사 전후로 자연 집단과 방류용 양식 집단의 유전 구조가 바뀐 것이 확인되었다[9]. 카드뮴 노출 때 발현이 늘어나는 메탈로티오네인 유전자(AiMT2)도 이 종에서 클로닝되었다[27].
""")
sec("safety","안전성","""
식약처 「식품원료 목록」에서 이 종은 별도 조건 없이 '사용가능' 원료이며, 건강기능식품 고시형 원료가 아니어서 고시 섭취 시 주의사항은 없다[1]. 이 종을 따로 다룬 국내 공공기관의 알레르기·패독·중금속 안전 정보는 이번 조사에서 확인하지 못함.

마비성 패독은 이 종에서도 문제가 된다[14, 15]. 유독 와편모조류(Gymnodinium catenatum)에 노출한 실험에서 관자에 독소가 최대 30%까지 쌓였고, 관자의 독성은 6일 만에 규제 한계인 800 μg STXeq/kg을 넘었다[14]. 2003년 상하이 수산시장 조사에서는 이 종과 큰구슬우렁이가 마비성·설사성 패독에 더 잘 오염되는 것으로 나타났다[15]. 설사성 패독 성분인 오카다산에 노출하면 이 종의 면역 기능과 산화 스트레스 지표가 나빠졌다[18].

중금속 가운데 카드뮴이 가장 주의할 원소다[16, 17]. 중국 보하이·황해 10개 지점 조사에서 가리비 시료의 96%가 카드뮴 기준을 넘었고, 이 종이 세 가리비 종 가운데 금속을 가장 많이 쌓았으며, 축적은 중장선>아가미>관자 순이었다[16]. 선전 조사에서도 이 종의 카드뮴이 중국·EU 기준을 넘었다[17]. 반면 룽청 양식 개체의 2021년 조사에서는 카드뮴 0.35–0.66 mg/kg, 납 0.10–0.28 mg/kg으로 중국 기준 아래였고 패독은 검출되지 않았다[2].
""")

def C(name,ko,cls,role,part,ct,act,src): return {"name":name,"name_ko":ko,"class":cls,"role":role,"part":part,"content_text":ct,"activity_ko":act,"source":src}
note="(원문의 맛 성분 분석값, 생·건 기준 명시 없음; 2021년 8–10월 룽청 양식, 금색·보라색 껍데기 계통 범위)"
compounds=[
C("Taurine","타우린","아미노산 유도체","nutrient","연체부",f"76.69–150.02 mg/100 g {note}","맛에 기여하는 성분으로 언급되었고 10월에는 보라색 계통이 금색 계통보다 많았다[2]",[2]),
C("Glutamic acid","글루탐산(유리)","아미노산","bioactive","연체부",f"73.73–240.17 mg/100 g {note}","감칠맛 아미노산 가운데 맛 기여도(TAV)가 가장 컸다[2]",[2]),
C("Glycine","글리신(유리)","아미노산","nutrient","연체부",f"39.87–83.33 mg/100 g {note}","단맛과 신선한 맛을 주는 성분으로 설명되었다[2]",[2]),
C("Alanine","알라닌(유리)","아미노산","nutrient","연체부",f"49.52–116.19 mg/100 g {note}","글리신과 함께 단맛을 내는 성분으로 설명되었다[2]",[2]),
C("Arginine","아르기닌(유리)","아미노산","nutrient","연체부",f"10.33–31.40 mg/100 g {note}","가리비류의 맛 활성 성분으로 언급되었다[2]",[2]),
C("Aspartic acid","아스파르트산(유리)","아미노산","nutrient","연체부",f"24.29–130.62 mg/100 g {note}; 보라색 계통 하한은 원문에 24.26으로 달리 적혀 있음","감칠맛 아미노산이나 TAV는 글루탐산보다 낮았다[2]",[2]),
C("Betaine","베타인","4급 암모늄 화합물","bioactive","연체부","금색 계통 8월 최고 1266.48 mg/100 g, 보라색 계통 10월 최고 722.08 mg/100 g (원문, 생·건 기준 명시 없음)","TAV가 1보다 커 맛에 기여하는 성분이었다[2]",[2]),
C("Succinic acid","숙신산","유기산","bioactive","연체부","금색 계통 8월 73.68 mg/100 g(최고), 9월 33.72 mg/100 g(최저); 보라색 계통 8월 최고 48.14 mg/100 g (원문)","조개류의 주된 맛 유기산으로 TAV가 1보다 컸다[2]",[2]),
C("Inosine monophosphate","이노신산(IMP)","뉴클레오타이드","bioactive","연체부",f"3.86–19.69 mg/100 g {note}","AMP와 함께 주된 맛 뉴클레오타이드였다[2]",[2]),
C("Adenosine monophosphate","아데닐산(AMP)","뉴클레오타이드","bioactive","연체부",f"5.70–18.17 mg/100 g {note}","가리비의 단맛과 지속되는 신선한 맛에 기여한다고 설명되었다[2]",[2]),
C("Eicosapentaenoic acid","EPA","n-3 지방산","nutrient","연체부","개별 함량 수치 확인하지 못함; 고도불포화지방산 합계가 총지방산의 46.24–56.09%, n-3/n-6 비가 모두 8보다 큼(동결건조 시료)","DHA와 함께 이 종 n-3 지방산의 주요 성분이다[2]; 말린 관자 저장 중 산화된다[20]",[2,20]),
C("Docosahexaenoic acid","DHA","n-3 지방산","nutrient","연체부","개별 함량 수치 확인하지 못함; 수확기 금색 계통이 EPA·DHA를 더 많이 함유(원문)","EPA와 함께 영양적 가치의 중심 지방산으로 평가되었다[2]",[2,20]),
C("Palmitoleic acid","팔미톨레산","단일불포화지방산","nutrient","연체부","단일불포화지방산(총지방산의 16.65–21.92%) 가운데 가장 많음; 개별 수치는 원문 표에만 있음","맛과 양의 상관이 있다고 언급되었다[2]",[2]),
C("Retinol","비타민 A","지용성 비타민","nutrient","연체부","75.34–124.87 µg/100 g (원문, 동결건조 시료 분석 항목)","지용성 비타민 가운데 함량이 높은 편으로 보고되었다[2]",[2]),
C("Carotenoids","카로티노이드(총)","색소","bioactive","관자(주황색 변이 개체)","주황색 관자 개체군이 흰색 개체군보다 유의하게 높음(p<0.01), 최대흡수파장 455 nm; 시장 개체는 흰색 개체와 차이 없음(수치는 그림에만 있음)","관자에 드물게 쌓여 주황색을 내며, 항산화 등 효능이 알려진 색소군이다[12]",[12]),
]
E={"instrument":"","column":"","mobile_phase":"","gradient":"","flow":"","temp":"","detection":"","injection":"","sample_prep":"","standard":"","linearity":"","lod":"","loq":"","recovery":""}
def cond(**k):
    d=dict(E); d.update(k); return d
assays=[
{"role":"literature","compound":"Free amino acids, taurine, nucleotides, betaine","compound_ko":"유리아미노산·타우린·뉴클레오타이드·베타인","part":"연체부","content":"타우린 76.69–150.02 mg/100 g, 글루탐산 73.73–240.17 mg/100 g, IMP 3.86–19.69 mg/100 g, AMP 5.70–18.17 mg/100 g, 베타인 최고 1266.48 mg/100 g [2]","method":"아미노산 자동분석기·HPLC·LC-MS/MS(성분별 대응은 부록)","conditions":cond(instrument="원문 기기 목록: Hitachi L-8800 아미노산 자동분석기, Waters e2695 HPLC, Sciex 5500 Qtrap + Shimadzu LC-20A, Agilent 7890B GC (성분별 사용 기기는 부록에 있음)",sample_prep="시료 4 kg을 얼음에 담아 운반, 일부는 생시료로 맛 성분 분석, 일부는 동결건조 후 −80 °C 보관(지방·단백질·아미노산·지방산·비타민·무기질용)",standard="20종 아미노산·6종 뉴클레오타이드·베타인·유기산 표준품(순도 ≥ 99%)"),"rationale":"이 종의 맛과 영양 품질을 비교하는 성분으로 쓰였다. 맛 성분 분석은 선행 방법을 따랐고 세부 조건(칼럼·이동상·검출)은 부록에 있다고 적혀 있으나 부록은 전문 확인 못함[2].","source":[2],"url":"https://doi.org/10.3390/foods12234354","source_kind":"paper"},
{"role":"literature","compound":"Total carotenoids","compound_ko":"총카로티노이드","part":"관자","content":"주황색 관자 개체군이 흰색 개체군보다 유의하게 높음(p<0.01); 수치는 그림에만 있음 [12]","method":"분광광도법(파장 주사 후 455 nm 정량)","conditions":cond(instrument="Nanodrop 2000",detection="최대흡수파장 455 nm에서 정량",sample_prep="관자를 개체별로 동결건조·분쇄한 뒤 아세톤으로 카로티노이드 추출"),"rationale":"관자 색 변이를 판정하는 지표로 쓰였다. 원문은 방법을 선행 연구에 따른다고만 적어 표준물질·검량·검출한계는 없다[12].","source":[12],"url":"https://doi.org/10.7150/jgen.19146","source_kind":"paper"},
{"role":"literature","compound":"Umami peptides (AHELPRYG, HELPRY, WDGRDGAVD)","compound_ko":"감칠맛 펩타이드","part":"부산물(외투막·생식소 등)","content":"감칠맛 역치 0.10–0.51 mmol/L, 증강 역치 0.08–0.41 mmol/L; 0.5 mg/mL에서 MSG 환산 0.92–1.58 mg/mL [13]","method":"nanoLC-MS/MS(데이터 의존 획득) 서열 동정","conditions":cond(instrument="Easy nLC + Q-Exactive Plus (Thermo Scientific)",mobile_phase="A 0.1% 포름산 수용액, B 0.1% 포름산 80% 아세토니트릴",gradient="B 3–5%(0–2분), 5–25%(2–42분), 25–45%(42–52분), 45–90%(52–55분), 90% 유지(55–75분)",flow="300 nL/min",sample_prep="부산물:물 1:5(w/v) 균질; 알칼리 단백질분해효소 2000 U/g, pH 9, 35 °C, 6시간 → 100 °C 10분 불활성 → 풍미 단백질분해효소 700 U/g, pH 7, 55 °C, 5시간; 원심 8000 r/min 4 °C 20분; 한외여과 200–3000 Da; Superdex Peptide 10/300 GL 겔 여과(물, 0.5 mL/min, 220 nm, 50 mg/mL 0.5 mL 주입)",standard="합성 펩타이드(순도 > 95%)"),"rationale":"정량 지표가 아니라 부산물 활용을 위한 감칠맛 펩타이드 동정 조건이다. 펩타이드 함량은 보고되지 않았다[13].","source":[13],"url":"https://doi.org/10.1016/j.crfs.2026.101412","source_kind":"paper"},
{"role":"literature","compound":"Paralytic shellfish toxins (incl. GC toxins)","compound_ko":"마비성 패독(GC 독소 포함)","part":"관자·내장","content":"노출 실험 종료 시 독소의 최대 30%가 관자에 축적; 관자 독성이 6일 만에 800 μg STXeq/kg 초과 [14]","method":"","conditions":cond(),"rationale":"관자 섭취 위험을 판단하는 안전 지표다. 초록만 확인해 분석 조건은 전문 확인 못함[14].","source":[14],"url":"https://doi.org/10.1016/j.jhazmat.2024.133896","source_kind":"paper"},
]
world=[{"country":"중국","metric":"production_t","year":2022,"value":1792000,"unit":"t","note":"가리비류 전체(종 구분 없음, 원문은 중국 어업통계연감 인용); 산둥성 약 983,900 t","source":[2]}]
d={"slug":"argopecten-irradians","name_ko":"캐롤라이나해만가리비","name_en":"Bay scallop","scientific_name":"Argopecten irradians",
"aliases":["대서양해만가리비","해만가리비","Carolina bay scallop","Atlantic bay scallop","Argopecten irradians irradians","Argopecten irradians concentricus"],
"sections":S,"compounds":compounds,"markers":[],"assays":assays,"nutrients":[],"production":[],"gi":[],"orgs":[],"world":world,"sources":sources}
Path(__file__).resolve().parent.parent.joinpath("dossier.json").write_text(json.dumps(d,ensure_ascii=False,indent=1),encoding="utf-8")
for s in S: print(s["key"],len(s["body"]))
