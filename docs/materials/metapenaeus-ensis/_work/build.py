import json
A="2026-11-02"
def P(n,title,doi,pub,pmid,pmc=None,note="초록 확인"):
    ids=f"PubMed {pmid}"+(f", {pmc}" if pmc else "")
    return {"n":n,"title":f"{title} ({note})","url":f"https://doi.org/{doi}" if doi else f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/","publisher":f"{pub} ({ids})","accessed":A}
S=[
{"n":1,"title":"식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — '곧은뿔중하' 행(학명 Metapenaeus ensis, 영문명 'Greasyback shrimp, Sand shrimp', 수산물, 사용가능, 사용가능부위 '-', 사용조건 없음, 이명 없음). 같은 속 중하(M. joyneri)·말새우(M. macleayi)·Jinga shrimp(M. affinis)·Kadal shrimp(M. dobsoni)·Endeavour shrimp(M. endeavouri)·Middle shrimp(M. intermedius)·Speckled shrimp(M. monoceros) 행 대조 (로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json, card.json)","url":"https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020","publisher":"식품의약품안전처","accessed":"2026-10-13"},
{"n":2,"title":"식약처 고시 제2026-43호 「건강기능식품의 기준 및 규격」 제3. 2-30 글루코사민·2-31 N-아세틸글루코사민·2-49 키토산/키토올리고당(원재료 '갑각류(게, 새우 등)의 껍질, 연체류(오징어, 갑오징어 등)의 뼈' 등, 섭취 시 주의사항 '게 또는 새우에 알레르기가 있는 사람은 섭취에 주의') (로컬 원문 docs/refs/MFDS/건강기능식품의기준및규격_2026-43_제1~제3.txt)","url":"https://www.mfds.go.kr/brd/m_211/view.do?seq=14973","publisher":"식품의약품안전처","accessed":A},
P(3,"Chromosome-level and high-contiguity genome assembly and annotation of the greasyback shrimp Metapenaeus ensis. Sci Data 2026;13","10.1038/s41597-026-07627-z","Scientific Data","42288486","PMC13620119"),
P(4,"A Comprehensive Assessment of Nutritional Value, Antioxidant Potential, and Genetic Diversity in Metapenaeus ensis from Three Different Populations. Biology (Basel) 2024;13(10):838","10.3390/biology13100838","Biology (Basel)","39452146","PMC11505122","전문 확인"),
P(5,"Effects of Dietary Protein Levels on Growth, Digestive Enzyme Activity, Antioxidant Capacity, and Gene Expression Related to Muscle Growth and Protein Synthesis of Juvenile Greasyback Shrimp (Metapenaeus ensis). Animals (Basel) 2023;13(24):3886","10.3390/ani13243886","Animals (Basel)","38136924","PMC10740705"),
P(6,"First transcriptome profiling in gill and hepatopancrease tissues of Metapenaeus ensis in response to acute ammonia-N stress. Fish Shellfish Immunol 2023;139:108926","10.1016/j.fsi.2023.108926","Fish & Shellfish Immunology","37406893"),
P(7,"Occurrence and Characteristics of Microplastics in Wild and Farmed Shrimps Collected from Cau Hai Lagoon, Central Vietnam. Molecules 2023;28(12):4634","10.3390/molecules28124634","Molecules","37375190","PMC10305481","전문 확인"),
P(8,"Host-microbiota interactions and responses of Metapenaeus ensis infected with decapod iridescent virus 1. Front Microbiol 2023;13:1097931","10.3389/fmicb.2022.1097931","Frontiers in Microbiology","36713173","PMC9880205"),
P(9,"Cloning, expression, and primary structure of Metapenaeus ensis tropomyosin, the major heat-stable shrimp allergen. J Allergy Clin Immunol 1994;94(5):882-890","10.1016/0091-6749(94)90156-2","The Journal of Allergy and Clinical Immunology","7963157"),
P(10,"Characterization of recombinant shrimp allergen Pen a 1 (tropomyosin). Int Arch Allergy Immunol 1997;113(1-3):240-242","10.1159/000237558","International Archives of Allergy and Immunology","9130534"),
P(11,"B- and T-cell epitopes of tropomyosin, the major shrimp allergen. Allergy 1998;53(46 Suppl):44-47","10.1111/j.1398-9995.1998.tb04959.x","Allergy","9825997"),
P(12,"Identification and molecular characterization of Charybdis feriatus tropomyosin, the major crab allergen. J Allergy Clin Immunol 1998;102(5):847-852","10.1016/s0091-6749(98)70027-2","The Journal of Allergy and Clinical Immunology","9819304"),
P(13,"cDNA cloning and molecular identification of the major oyster allergen from the Pacific oyster Crassostrea gigas. Clin Exp Allergy 2001;31(8):1287-1294","10.1046/j.1365-2222.2001.01165.x","Clinical and Experimental Allergy","11529900"),
P(14,"Induction of shrimp tropomyosin-specific hypersensitivity in mice. Int Arch Allergy Immunol 2008;147(4):305-314","10.1159/000144038","International Archives of Allergy and Immunology","18617750"),
P(15,"Immunization with Hypoallergens of shrimp allergen tropomyosin inhibits shrimp tropomyosin specific IgE reactivity. PLoS One 2014;9(11):e111649","10.1371/journal.pone.0111649","PLoS One","25365343","PMC4218792"),
P(16,"T cell epitope immunotherapy ameliorates allergic responses in a murine model of shrimp allergy. Clin Exp Allergy 2016;46(3):491-503","10.1111/cea.12684","Clinical and Experimental Allergy","26610061"),
P(17,"Low-Dose Allergen-Specific Immunotherapy Induces Tolerance in a Murine Model of Shrimp Allergy. Int Arch Allergy Immunol 2017;174(2):86-96","10.1159/000479694","International Archives of Allergy and Immunology","29065408"),
P(18,"Effect of transglutaminase-catalyzed glycosylation on the allergenicity and conformational structure of shrimp (Metapenaeus ensis) tropomyosin. Food Chem 2016;219:215-222","10.1016/j.foodchem.2016.09.139","Food Chemistry","27765219"),
P(19,"Tyrosinase/caffeic acid cross-linking alleviated shrimp (Metapenaeus ensis) tropomyosin-induced allergic responses by modulating the Th1/Th2 immunobalance. Food Chem 2020;340:127948","10.1016/j.foodchem.2020.127948","Food Chemistry","32896779"),
P(20,"[Mass spectrometry identification and immune cross-reactivity of a minor shrimp allergen-sarcoplasmic calcium binding protein from Litopenaeus vannamei]. Xi Bao Yu Fen Zi Mian Yi Xue Za Zhi 2012;28(8):811-814",None,"Xi Bao Yu Fen Zi Mian Yi Xue Za Zhi","22863586"),
P(21,"Cloning, expression, characterization and phylogenetic analysis of arginine kinase from greasyback shrimp (Metapenaeus ensis). Comp Biochem Physiol B 2009;153(3):268-274","10.1016/j.cbpb.2009.03.010","Comparative Biochemistry and Physiology Part B","19341812"),
P(22,"Risk assessment of heavy metal contamination in shrimp farming in Mai Po Nature Reserve, Hong Kong. Environ Geochem Health 2006;28(1-2):27-36","10.1007/s10653-005-9008-y","Environmental Geochemistry and Health","16528597"),
P(23,"[Distribution of polybrominated diphenyl ethers in aquatic species from the Pearl River Estuary]. Huan Jing Ke Xue 2006;27(9):1732-1737",None,"Huan Jing Ke Xue","17117624"),
P(24,"Characterization and mechanism of phthalic acid esters bioaccumulation in dominant mangrove fish at different habitats in the mangrove ecosystem of Dongzhai Harbor, China. Sci Total Environ 2024;954:176221","10.1016/j.scitotenv.2024.176221","Science of the Total Environment","39304146"),
P(25,"Tolerance to, and avoidance of, hypoxia by the penaeid shrimp (Metapenaeus ensis). Environ Pollut 2002;118(3):351-355","10.1016/s0269-7491(01)00298-6","Environmental Pollution","12009132"),
P(26,"A change of heart: cardiovascular development in the shrimp Metapenaeus ensis. Comp Biochem Physiol A 2002;133(3):577-587","10.1016/s1095-6433(02)00196-4","Comparative Biochemistry and Physiology Part A","12443915"),
P(27,"Shotgun assembly of the first mitochondrial genome of Metapenaeus (Metapenaeus ensis) with phylogenetic consideration. Mitochondrial DNA A 2016;27(5):3689-3690","10.3109/19401736.2015.1079857","Mitochondrial DNA Part A","26355746"),
P(28,"Phylogenetic relationships of 12 penaeoidea shrimp species deduced from mitochondrial DNA sequences. Biochem Genet 2004;42(9-10):331-345","10.1023/b:bigi.0000039808.12069.ed","Biochemical Genetics","15524311"),
P(29,"Genetic and phenotypic variations of isolates of shrimp Taura syndrome virus found in Penaeus monodon and Metapenaeus ensis in Taiwan. J Gen Virol 2004;85(Pt 10):2963-2968","10.1099/vir.0.80132-0","Journal of General Virology","15448359"),
P(30,"Application of response surface methodology to optimise microbial inactivation of shrimp and conch by supercritical carbon dioxide. J Sci Food Agric 2015;95(5):1016-1023","10.1002/jsfa.6783","Journal of the Science of Food and Agriculture","24931827"),
P(31,"Prediction of total volatile basic nitrogen contents using wavelet features from visible/near-infrared hyperspectral images of prawn (Metapenaeus ensis). Food Chem 2016;197(Pt A):257-265","10.1016/j.foodchem.2015.10.073","Food Chemistry","26616948"),
P(32,"Effects of high pressure freezing (HPF) on denaturation of natural actomyosin extracted from prawn (Metapenaeus ensis). Food Chem 2017;229:252-259","10.1016/j.foodchem.2017.02.048","Food Chemistry","28372171"),
P(33,"Vitellogenesis in the sand shrimp, Metapenaeus ensis: the contribution from the hepatopancreas-specific vitellogenin gene (MeVg2). Biol Reprod 2004;71","10.1095/biolreprod.103.022905","Biology of Reproduction","15115717"),
P(34,"The shrimp hyperglycemic hormone-like neuropeptide is encoded by multiple copies of genes arranged in a cluster. FEBS Lett 1998;441(3):397-403","10.1016/s0014-5793(98)01573-7","FEBS Letters","9891979"),
P(35,"Passive protection of shrimp against white spot syndrome virus (WSSV) using specific antibody from egg yolk of chickens immunized with inactivated virus or a WSSV-DNA vaccine. Fish Shellfish Immunol 2008;25(5):604-610","10.1016/j.fsi.2008.08.010","Fish & Shellfish Immunology","18805492"),
P(36,"Detection of hepatopancreatic parvovirus (HPV) in wild shrimp from India by nested polymerase chain reaction (PCR). Dis Aquat Organ 2005;63(2-3):255-259","10.3354/dao063255","Diseases of Aquatic Organisms","15819441"),
]
sec=[]
def add(k,t,b): sec.append({"key":k,"title":t,"body":b})
add("overview","한눈에 보기",
"곧은뿔중하(Metapenaeus ensis)는 보리새우과(Penaeidae) 중하속(Metapenaeus)에 드는 바다·기수 새우로, 영문으로는 greasyback shrimp 또는 sand shrimp라 한다[1, 3]. 인도-서태평양이 원산인 광염성 종이며, 중국에서는 푸젠·광둥·광시·하이난 등 남부 연안에서 주로 양식된다[4]. 염분·수온 변화에 잘 견디는 성질 때문에 중국 양식업에서 중요한 위치를 차지한다고 소개된다[4].\n\n"
"식약처 「식품원료 목록」에는 학명 Metapenaeus ensis로 '곧은뿔중하' 한 줄이 올라 있으며, 분류는 수산물, 상태는 '사용가능'이다[1]. 사용 부위는 '-'(따로 정하지 않음)이고 별도 사용 조건이나 이명은 적혀 있지 않다[1]. 이 종 자체는 건강기능식품 고시형 원료의 원재료로 이름이 오르지 않았으나, 글루코사민·N-아세틸글루코사민·키토산 고시의 원재료에는 '갑각류(게, 새우 등)의 껍질'이 새우 종 지정 없이 들어 있다[2].\n\n"
"양식 개체 근육은 조단백질 20.80–22.10 g/100 g, 조지방 0.83–1.03 g/100 g으로 단백질이 많고 지방이 적은 식품으로 평가되었다[4]. 이 종의 근육 단백질 트로포미오신(Met e 1)은 열에 강한 새우 주 알레르겐으로, 1994년 cDNA 클로닝으로 1차 구조가 밝혀졌다[9]. 국내 어획·수입 통계와 국가표준식품성분표의 이 종 성분값은 이 조사에서 확인하지 못함.")
add("history","이용·연구의 역사",
"홍콩 마이포 자연보호구의 전통 조간대 새우 연못(gei wai)에서는 이 종이 'gei wai shrimp'라는 이름으로 길러져 왔다[22]. 2006년 보고된 위해성 평가는 이 연못의 틸라피아·숭어·이 종·민물새우류의 중금속 축적을 조사했다[22].\n\n"
"식품 알레르기 연구에서 이 종은 출발점 가운데 하나다[9, 10]. 1994년 연구진은 이 종의 cDNA 발현 라이브러리를 새우 알레르기 환자 혈청으로 검색해 IgE와 결합하는 클론 Met e I을 찾았고, 이것이 트로포미오신임을 밝혔다[9]. 이후 갈색새우(Penaeus aztecus)의 알레르겐 Pen a 1 서열도 이 종의 트로포미오신(Met e 1)과 나란히 비교되었다[10]. 1998년 게(Charybdis feriatus)와 2001년 굴(Crassostrea gigas)의 주 알레르겐을 밝힐 때도 재조합 Met e 1이 교차반응 비교 기준으로 쓰였다[12, 13].\n\n"
"1990년대 후반부터 이 종의 눈자루 신경호르몬(혈당상승호르몬 등)과 난황 단백질(비텔로제닌) 유전자가 잇달아 보고되어, 이 종은 새우 생식·탈피 생리 연구에 자주 쓰였다[33, 34]. 2010년대 이후에는 중국에서 사료 단백질 요구량, 암모니아 스트레스, 바이러스 감염 등 양식 연구가 이어졌다[5, 6, 8].")
add("biology","어종·형태·생태",
"이 종은 십각목 보리새우과의 새우로, 인도-서태평양 원산이며 중국 동중국해·남중국해, 일본, 인도네시아, 말레이시아, 오스트레일리아 등에 분포한다고 소개된다[4]. 바닷물과 민물 모두에서 자랄 수 있고 고온과 저염분에 강하다고 한다[4].\n\n"
"유생 발달은 노플리우스 6단계, 조에아(protozoea) 3단계, 미시스 3단계를 거쳐 후기 유생으로 이어진다[26]. 심장은 노플리우스 6기 말에 불규칙하게 뛰기 시작하고, 조에아 1기부터 분당 400–600회로 규칙적으로 뛴다[26].\n\n"
"어린 새우는 산소 부족에 민감하다[25]. 실험에서 용존산소에 대한 8시간 LC50은 0.77 mg O2/L, 0.5 mg O2/L에서의 LT50은 399분이었고, 산소 농도 기울기가 있으면 산소가 적은 곳을 피해 움직였다[25].\n\n"
"중국 싼야·주하이·라오핑 세 양식 집단(3–4개월령)을 비교한 연구에서 근육의 총항산화능은 2.68–2.69 μmol/g, SOD 활성은 53.96–54.90 U/g으로 집단 간 차이가 없었다[4]. 하이난 둥자이항 맹그로브 조사에서 이 종은 저층 어류의 주요 먹이원으로, 저층 어류 식단의 28.5%를 차지한다고 추정되었다[24]. 생식 생리에서는 간췌장 전용 난황 유전자 MeVg2가 보고되었다[33].")
add("related_species","관련 종·이름",
"식약처 목록에는 중하속(Metapenaeus) 새우가 여러 줄 따로 올라 있다[1]. 중하(M. joyneri, Shiba shrimp), 말새우(M. macleayi), Jinga shrimp(M. affinis), Kadal shrimp(M. dobsoni), Endeavour shrimp(M. endeavouri), Middle shrimp(M. intermedius), Speckled shrimp(M. monoceros)가 그것이며, 이 자료는 그 종들의 성분·안전성 값을 섞지 않는다[1]. 특히 국문명이 비슷한 '중하'는 학명이 M. joyneri인 다른 종이다[1].\n\n"
"영문명은 목록에 'Greasyback shrimp, Sand shrimp'로 적혀 있고, 논문에서는 oilback shrimp·reed shrimp, 홍콩의 'gei wai shrimp', 알레르기 문헌의 'brown shrimp'라는 이름도 보인다[1, 4, 11, 22]. 영문 'brown shrimp'는 다른 새우(Penaeus aztecus 등)에도 쓰이는 이름이므로 학명으로 구분해야 한다[10, 11].\n\n"
"미토콘드리아 COI·16S rRNA 서열로 12종의 보리새우상과 새우를 비교한 연구는 Penaeus 속과 Metapenaeus 속이 약 638만–798만 년 전에 갈라졌다고 추정했다[28]. 이 종의 미토콘드리아 전체 유전체를 쓴 계통 분석에서도 넓은 의미의 Penaeus 무리와 Metapenaeus 속이 서로 다른 갈래로 나뉘었다[27].")
add("cultivation","어획·양식",
"이 종은 중국 남부에서 연못과 실내 공장식 시설을 결합한 방식, 가두리와 실내 시설을 결합한 방식으로 양식된다[4]. 싼야·주하이 집단은 '연못+공장식', 라오핑 집단은 '가두리+공장식'으로 길렀고 수온은 약 28 °C로 유지되었다[4].\n\n"
"어린 새우에게 단백질 29.37–49.32% 사료를 8주간 먹인 시험에서 39.11% 이상 군의 성장이 좋았고, 특정 성장률을 기준으로 한 적정 사료 단백질은 38.59%로 추정되었다[5]. 공장식 집약 양식에서는 암모니아 스트레스가 문제이며, 고농도 암모니아에 24시간 노출된 아가미와 간췌장에서 각각 2,000개, 2,010개의 유전자 발현이 달라졌다[6].\n\n"
"질병으로는 십각류 무지개빛 바이러스 1(DIV1) 감염이 장내 세균 다양성을 낮추고 병원성 세균을 늘린다고 보고되었다[8]. 대만에서는 이 종에서 타우라 증후군 바이러스(TSV) 분리주가 발견되었다[29]. 흰반점병 바이러스(WSSV) 공격 시험에서 불활화 바이러스로 면역한 닭의 난황 항체(IgY)를 쓰면 생존율이 73.3%였다[35]. 인도 연안의 야생 새우 조사에서는 이 종에서도 중첩 PCR로 간췌장 파보바이러스가 검출되었다[36]. 세계·국가별 어획·양식 생산량은 이 조사에서 확인하지 못함.")
add("processing","가공·이용",
"이 종은 생새우로 유통되며 신선도와 미생물 저감 연구의 대상이 되었다[30, 31]. 초임계 이산화탄소를 53 °C, 15 MPa에서 40분 처리하면 총균수가 3.69 log 줄었고 관능 점수는 약 8점(바람직함)이었다[30]. 냉장 저장 중 신선도 지표인 휘발성 염기질소(TVB-N)를 가시광·근적외선 초분광 영상으로 예측하는 모델(예측 결정계수 0.9547)도 개발되었다[31].\n\n"
"냉동 가공 연구에서는 이 종에서 추출한 자연 액토미오신을 고압 동결했을 때 압력 이동 동결이 단백질 변성을 줄였고, 300 MPa가 변성을 일으키는 경계 압력이었다[32]. 알레르기를 낮추는 가공법으로는 트랜스글루타미나아제로 당을 붙이는 처리와 티로시나아제·카페산 교차결합이 트로포미오신의 IgE 결합을 줄였다[18, 19]. 다만 이 결과는 정제 단백질과 쥐 실험 결과로, 실제 새우 제품의 알레르기 위험이 없어진다는 뜻은 아니다[18, 19].\n\n"
"국내 건강기능식품 고시에서 글루코사민·N-아세틸글루코사민·키토산의 원재료는 '갑각류(게, 새우 등)의 껍질' 등으로 정해져 있을 뿐 새우 종을 지정하지 않는다[2]. 이 종을 원료로 쓴 국내 가공식품·건강기능식품 생산 실적은 확인하지 못함.")
add("genetics","유전 정보",
"2026년 이 종의 첫 염색체 수준 유전체가 공개되었다[3]. 조립 크기는 1.97 Gb, 콘티그 N50은 3.84 Mb, 스캐폴드 N50은 45.37 Mb였고 서열의 90.07%가 39개 염색체에 배치되었다[3]. 유전체 이형접합도는 2.46%, 반복 서열은 56.76%였으며 단백질 암호화 유전자 21,432개가 주석되었다[3].\n\n"
"미토콘드리아 전체 유전체는 15,944 bp 원형 분자로, 단백질 암호화 유전자 13개, tRNA 22개, rRNA 2개, 조절 영역을 가진다[27]. 중국 세 양식 집단의 SNP 밀도는 2.62–5.39 SNP/kb, 관찰 이형접합도는 0.07–0.16으로 유전 다양성이 비교적 낮았고, 싼야·주하이 집단 사이의 분화가 가장 컸다[4]. 암모니아 스트레스 전사체 연구는 유니진 103,174개(평균 876 bp, N50 1,189 bp)를 조립했다[6].\n\n"
"눈자루 혈당상승호르몬 유사 유전자는 한 개체의 유전체에 적어도 6개 사본이 무리 지어 있었다[34]. 난황 유전자는 MeVg1과 간췌장 전용 MeVg2가 있으며 두 전구체의 아미노산 서열 동일성은 54%였다[33].")
add("safety","안전성",
"이 종의 트로포미오신 Met e 1은 281개 아미노산, 34 kd의 열에 강한 근육 단백질로, 새우 알레르기 환자 혈청의 IgE와 결합하고 정상인 혈청과는 결합하지 않았다[9]. IgE가 붙는 B세포 에피토프로는 잔기 47–63과 150–158이 보고되었다[11]. 재조합 Met e 1로 흡착한 혈청에서는 게 트로포미오신 Cha f 1에 대한 IgE 반응이 사라져 게와의 교차반응이 확인되었다[12]. 흰다리새우 근형질 칼슘결합단백질(SCP) 항체는 이 종의 약 21,000 크기 단백질도 인식했다[20]. 식약처는 새우 껍질 원료 건강기능식품에 '게 또는 새우에 알레르기가 있는 사람은 섭취에 주의' 문구를 정했다[2].\n\n"
"Met e 1을 쓴 면역요법 연구는 모두 쥐 실험이다[14, 15, 16, 17]. 저알레르기 변이체, T세포 에피토프 펩타이드, 저용량 재조합 단백질 투여가 쥐의 알레르기 반응을 줄였으나 사람에서의 효과는 확인되지 않았다[15, 16, 17].\n\n"
"홍콩 마이포 연못 조사에서 이 종 조직의 중금속 농도는 사람이 먹기에 안전한 수준으로 평가되었다[22]. 주강 하구 조사에서 이 종과 M. affinis를 함께 묶은 새우 시료의 PBDE(10종 합)는 지질 기준 49.0–239.1 ng/g이었다[23]. 베트남 까우하이 석호의 야생 개체에서는 미세플라스틱이 마리당 2.5 ± 0.5개(습중량 g당 0.7 ± 0.3개) 나왔고, 이 종과 green tiger shrimp 등 야생 새우 2종의 조직 시료 검출률은 30%였다[7]. 미국 등 공공기관의 이 종 단독 안전성 평가는 확인하지 못함.")
comp=[
{"name":"Tropomyosin","name_ko":"트로포미오신(Met e 1)","class":"근육 단백질(알레르겐)","role":"marker","part":"근육","content_text":"아미노산 281개, 분자량 34 kd(cDNA 클론 Met e I) [9]","activity_ko":"새우 알레르기 환자 IgE와 결합하는 주 알레르겐; B세포 에피토프 잔기 47–63, 150–158[11]","source":[9,11]},
{"name":"Sarcoplasmic calcium-binding protein","name_ko":"근형질 칼슘결합단백질(SCP)","class":"근육 단백질(부 알레르겐)","role":"bioactive","part":"근육","content_text":"분자량 약 21,000(Mr) 단백질이 흰다리새우 SCP 항체로 인식됨 [20]","activity_ko":"갑각류 간 교차반응 가능성(항체 시험)[20]","source":[20]},
{"name":"Arginine kinase","name_ko":"아르지닌 인산화효소","class":"효소","role":"bioactive","part":"재조합 단백질(유전자 발현)","content_text":"겉보기 Km: ATP 2.33 ± 0.1 mM, L-아르지닌 1.59 ± 0.2 mM; 최적 pH 8.5, 30 °C [21]","activity_ko":"무척추동물 근육의 에너지(ATP) 완충 효소[21]","source":[21]},
{"name":"Protein","name_ko":"조단백질","class":"영양 성분","role":"nutrient","part":"근육(양식 개체)","content_text":"20.80–22.10 g/100 g(세 집단) [4]","activity_ko":"고단백·저지방 식품으로 평가[4]","source":[4]},
{"name":"Essential amino acids","name_ko":"필수아미노산(합)","class":"아미노산","role":"nutrient","part":"근육(양식 개체)","content_text":"4.72–5.72 g/100 g; 총아미노산 최고 15.72 g/100 g(싼야 집단) [4]","activity_ko":"17종 아미노산 검출, 필수아미노산 비율이 FAO/WHO 권장(40%)에 가깝다고 평가[4]","source":[4]},
{"name":"Eicosapentaenoic acid","name_ko":"EPA+DHA(합)","class":"오메가-3 지방산","role":"nutrient","part":"근육(양식 개체)","content_text":"DHA+EPA 133.15–161.55 mg/100 g [4]","activity_ko":"항염증 매개체 전구체로 소개[4]","source":[4]},
{"name":"Fatty acids, total","name_ko":"총지방산","class":"지질","role":"nutrient","part":"근육(양식 개체)","content_text":"384.35–519.30 mg/100 g; ΣPUFA 181.15–221.20, ΣMUFA 75.1–104.2 mg/100 g [4]","activity_ko":"세 집단 모두 ΣPUFA > ΣMUFA[4]","source":[4]},
{"name":"Vitellogenin","name_ko":"비텔로제닌(MeVg1·MeVg2)","class":"난황 전구 단백질","role":"bioactive","part":"난소·간췌장","content_text":"MeVg2 cDNA 8.0 kb, MeVg1과 아미노산 54% 동일 [33]","activity_ko":"암컷 생식소 성숙 때 난황 공급[33]","source":[33]},
{"name":"Crustacean hyperglycemic hormone","name_ko":"갑각류 혈당상승호르몬(MeCHH)","class":"신경펩타이드","role":"bioactive","part":"눈자루","content_text":"유전자 6개 이상 사본, 유전자 크기 1.5–2.1 kb [34]","activity_ko":"포도당 대사 조절 호르몬[34]","source":[34]},
{"name":"Actomyosin","name_ko":"자연 액토미오신","class":"근원섬유 단백질","role":"bioactive","part":"근육","content_text":"고압 동결 시 300 MPa에서 변성 시작 [32]","activity_ko":"냉동 품질과 관련된 근육 단백질[32]","source":[32]},
]
nut=[
{"form":"양식 개체 근육(싼야 집단, 3–4개월령; 논문 분석값)","basis":"근육 100 g당(원문 g/100 g; 같은 표에 수분 74.50–75.30 g/100 g이 보고되어 습중량 기준으로 보임)","items":[{"name":"조단백질","value":22.10,"unit":"g"},{"name":"조지방","value":0.97,"unit":"g"},{"name":"총아미노산","value":15.72,"unit":"g"},{"name":"필수아미노산","value":5.72,"unit":"g"}],"source":[4]},
{"form":"양식 개체 근육(주하이 집단; 논문 분석값)","basis":"근육 100 g당(원문 g/100 g; 같은 표에 수분 74.50–75.30 g/100 g이 보고되어 습중량 기준으로 보임)","items":[{"name":"조단백질","value":20.80,"unit":"g"},{"name":"조지방","value":0.83,"unit":"g"}],"source":[4]},
{"form":"양식 개체 근육(라오핑 집단; 논문 분석값)","basis":"근육 100 g당(원문 g/100 g; 같은 표에 수분 74.50–75.30 g/100 g이 보고되어 습중량 기준으로 보임)","items":[{"name":"조단백질","value":21.17,"unit":"g"},{"name":"조지방","value":1.03,"unit":"g"}],"source":[4]},
]
E={k:"" for k in ["instrument","column","mobile_phase","gradient","flow","temp","detection","injection","sample_prep","standard","linearity","lod","loq","recovery"]}
def C(**kw): d=dict(E); d.update(kw); return d
assays=[
{"role":"literature","compound":"Amino acids (hydrolyzed)","compound_ko":"가수분해 아미노산","part":"근육","content":"필수아미노산 4.72–5.72 g/100 g, 총아미노산 최고 15.72 g/100 g [4]","method":"중국 국가식품안전표준 GB 5009.124–2016(식품 중 아미노산 측정)","conditions":C(sample_prep="양식장별 탈피 간기 개체 3마리의 근육, −80 °C 보관",standard="GB 5009.124–2016"),"rationale":"이 종 근육의 단백질 품질을 보여 주는 대표 지표다; 전문에서 시험 기준만 확인했고 기기·칼럼 조건은 논문에 적혀 있지 않다[4].","source":[4],"url":"https://doi.org/10.3390/biology13100838","source_kind":"paper"},
{"role":"literature","compound":"EPA + DHA","compound_ko":"EPA+DHA","part":"근육","content":"133.15–161.55 mg/100 g; 총지방산 384.35–519.30 mg/100 g [4]","method":"중국 국가식품안전표준 GB 5009.168–2016(식품 중 지방산 측정)","conditions":C(sample_prep="양식장별 탈피 간기 개체 3마리의 근육",standard="GB 5009.168–2016"),"rationale":"수산물 지질의 영양 가치를 대표하는 오메가-3 지방산이다; 전문에서 시험 기준만 확인했고 기기 조건은 논문에 적혀 있지 않다[4].","source":[4],"url":"https://doi.org/10.3390/biology13100838","source_kind":"paper"},
{"role":"literature","compound":"Tropomyosin (Met e 1)","compound_ko":"트로포미오신(Met e 1)","part":"근육","content":"정량값 없음 — 아미노산 281개, 34 kd [9]","method":"cDNA 발현 라이브러리 IgE 검색, 재조합 발현(pGEX), 면역블롯","conditions":C(),"rationale":"이 종에서 처음 클로닝된 새우 주 알레르겐으로 갑각류 알레르기 판별의 기준 단백질이다; 전문 확인 못함 — 함량은 보고되지 않았다[9].","source":[9],"url":"https://doi.org/10.1016/0091-6749(94)90156-2","source_kind":"paper"},
]
d={"slug":"metapenaeus-ensis","name_ko":"곧은뿔중하","name_en":"Greasyback shrimp","scientific_name":"Metapenaeus ensis","aliases":["Greasyback shrimp","Sand shrimp","gei wai shrimp","oilback shrimp"],
"sections":sec,"compounds":comp,"markers":[],"assays":assays,"nutrients":nut,"production":[],"world":[],"gi":[],"orgs":[],"sources":S}
json.dump(d,open("/home/user/hfoodguide-wave3/docs/materials/metapenaeus-ensis/dossier.json","w"),ensure_ascii=False,indent=1)
