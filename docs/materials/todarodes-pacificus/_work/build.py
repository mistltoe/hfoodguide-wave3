import json, pathlib
A="2026-11-02"
def pm(n,title,doi,pub,pmid,pmc=None,note="초록 확인"):
    url=f"https://doi.org/{doi}" if doi else f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
    p=f"{pub} (PubMed {pmid}" + (f", {pmc}" if pmc else "") + ")"
    return {"n":n,"title":f"{title} ({note})","url":url,"publisher":p,"accessed":A}
S=[
 {"n":1,"title":"식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — '살오징어' 행(학명 Todarodes pacificus, 영문 Japanese flying squid, Japanese common squid, 이명 물오징어, 수산물, 사용가능, 사용가능부위: 전체(내장 제외))와 '살오징어내장' 행(사용불가), 같은 속 'European flying squid' 행(Todarodes sagittatus, 사용가능), 가공품 '오징어'·'건오징어' 등 행(학명 Doryteuthis bleekeri 등으로 표기); 로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json 및 docs/materials/todarodes-pacificus/card.json으로 확인","url":"https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020","publisher":"식품의약품안전처","accessed":"2026-10-13"},
 pm(2,"Anisakis spp. in fishery products from Japanese waters: Updated insights on host prevalence and human infection risk factors. Parasitol Int 2020;78:102137","10.1016/j.parint.2020.102137","Parasitology International","32439483"),
 pm(3,"Larval anisakid nematodes of Japanese common squid (Todarodes pacificus) from the Sea of Japan. J Parasitol 1995;81(1):69-75",None,"The Journal of Parasitology","7876981"),
 pm(4,"Plerocercoids of Nybelinia surmenicola (Cestoda: Tentacularidae) in Squids, Todarodes pacificus, from East Sea, the Republic of Korea. Korean J Parasitol 2016;54(2):221-4","10.3347/kjp.2016.54.2.221","The Korean Journal of Parasitology","27180583","PMC4870981"),
 pm(5,"Cadmium-binding proteins of three marine molluscs and characterization of two cadmium-binding glycoproteins from the hepatopancreas of a whelk, Buccinum tenuissimum. Environ Health Perspect 1986;65:49-55","10.1289/ehp.866549","Environmental Health Perspectives","3709465","PMC1474719","PubMed 도구로 PMC 전문(스캔 본문, 표 1·방법) 확인"),
 pm(6,"As, Cd and Hg in the organs of Todarodes pacificus, Sepia longipes and Sepia madokai in the East China Sea. Ecotoxicol Environ Saf 2017;145:103-110","10.1016/j.ecoenv.2017.06.054","Ecotoxicology and Environmental Safety","28710949"),
 pm(7,"Mercury concentrations in the tissues of blue shark (Prionace glauca) from Sagami Bay and cephalopods from East China Sea. Environ Pollut 2020;266:115192","10.1016/j.envpol.2020.115192","Environmental Pollution","32683233"),
 pm(8,"Influence of Squid Liver Powder on Accumulation of Cadmium in Serum, Kidney and Liver of Mice. Prev Nutr Food Sci 2013;18(1):1-10 (본문에서 이탤릭 학명이 빠져 있어 종명은 PubMed 키워드 'Todarodes pacificus'로 대응)","10.3746/pnf.2013.18.1.001","Preventive Nutrition and Food Science","24471103","PMC3867147","PubMed 도구로 PMC 전문 확인"),
 pm(9,"Identification of the first major allergen of a squid (Todarodes pacificus). J Allergy Clin Immunol 1996;98(5 Pt 1):948-53","10.1016/s0091-6749(96)80011-x","The Journal of Allergy and Clinical Immunology","8939158"),
 pm(10,"Allergenic response to squid (Todarodes pacificus) tropomyosin Tod p1 structure modifications induced by high hydrostatic pressure. Food Chem Toxicol 2015;76:86-93","10.1016/j.fct.2014.12.002","Food and Chemical Toxicology","25530105"),
 pm(11,"Isolation and characterization of lecithin from squid (Todarodes pacificus) viscera deoiled by supercritical carbon dioxide extraction. J Food Sci 2011;76(2):C350-4","10.1111/j.1750-3841.2010.02039.x","Journal of Food Science","21535756"),
 pm(12,"Ameliorative effects of squid phospholipids from Todarodes pacificus on atopic dermatitis-like lesions in NC/Nga mice. Arch Dermatol Res 2025;317(1):239","10.1007/s00403-024-03773-9","Archives of Dermatological Research","39804492"),
 pm(13,"13-Week oral toxicity study of oil derived from squid (Todarodes pacificus) in Sprague-Dawley rats. Regul Toxicol Pharmacol 2012;64(2):195-204","10.1016/j.yrtph.2012.07.011","Regulatory Toxicology and Pharmacology","22885076"),
 pm(14,"Effect of Dietary Partial Hydrolysate of Phospholipids, Rich in Docosahexaenoic Acid-Bound Lysophospholipids, on Lipid and Fatty Acid Composition in Rat Serum and Liver. J Food Sci 2019;84(1):183-191","10.1111/1750-3841.14416","Journal of Food Science","30633384"),
 pm(15,"Effect of Dietary Oil Rich in Docosahexaenoic Acid-Bound Lysophosphatidylcholine Prepared from Fishery By-Products on Lipid and Fatty Acid Composition in Rat Liver and Brain. J Oleo Sci 2019;68(8):781-792","10.5650/jos.ess19103","Journal of Oleo Science","31366855"),
 pm(16,"Molecular and physical characteristics of squid (Todarodes pacificus) skin collagens and biological properties of their enzymatic hydrolysates. J Food Sci 2008;73(4):C249-55","10.1111/j.1750-3841.2008.00722.x","Journal of Food Science","18460118"),
 pm(17,"Mechanochemical synthesis of chitosan submicron particles from the gladius of Todarodes pacificus. J Adv Res 2016;7(6):863-71","10.1016/j.jare.2016.08.006","Journal of Advanced Research","27672449","PMC5030334"),
 pm(18,"Effect of different drying methods on the myosin structure, amino acid composition, protein digestibility and volatile profile of squid fillets. Food Chem 2015;171:168-76","10.1016/j.foodchem.2014.09.002","Food Chemistry","25308657"),
 pm(19,"Effects of gamma radiation on sensory qualities, microbiological and chemical properties of salted and fermented squid. J Food Prot 2000;63(7):934-9","10.4315/0362-028x-63.7.934","Journal of Food Protection","10914664"),
 pm(20,"Analysis of radiolytic products of lipid in irradiated dried squids (Todarodes pacificus). J Food Prot 2004;67(8):1731-5","10.4315/0362-028x-67.8.1731","Journal of Food Protection","15330541"),
 pm(21,"Persistent organochlorine pollutants in Korean offshore waters: squid (Todarodes pacificus) as a biomonitor. Mar Pollut Bull 2009;58(8):1238-44","10.1016/j.marpolbul.2009.05.002","Marine Pollution Bulletin","19501371"),
 pm(22,"Long-term conservation of six duplicated structural genes in cephalopod mitochondrial genomes. Mol Biol Evol 2004;21(11):2034-46","10.1093/molbev/msh227","Molecular Biology and Evolution","15297602"),
 pm(23,"Population genetics of Todarodes pacificus (Cephalopoda: Ommastrephidae) in the northwest Pacific Ocean via GBS sequencing. Open Life Sci 2024;19(1):20220876 (PubMed 표기에서 이탤릭 학명이 빠져 있어 종명은 'Todarodes pacificus' 검색어 일치로 확인)","10.1515/biol-2022-0876","Open Life Sciences","38947770","PMC11211871"),
 pm(24,"Identification of four squid species by quantitative real-time polymerase chain reaction. Mol Cell Probes 2016;30(1):22-9","10.1016/j.mcp.2016.01.001","Molecular and Cellular Probes","26772407"),
 pm(25,"Long-term variability analysis of the habitat suitability index for Todarodes pacificus (Japanese common squid) using MODIS-Aqua dataset in the East/Japan Sea, South Korea. Mar Environ Res 2025;212:107537","10.1016/j.marenvres.2025.107537","Marine Environmental Research","40945105"),
 pm(26,"Observations on the spawning behavior, egg masses and paralarval development of the ommastrephid squid Todarodes pacificus in a laboratory mesocosm. J Exp Biol 2015;218(Pt 23):3825-35","10.1242/jeb.127670","Journal of Experimental Biology","26632456"),
 pm(27,"Structure and properties of the egg mass of the ommastrephid squid Todarodes pacificus. PLoS One 2017;12(8):e0182261","10.1371/journal.pone.0182261","PLoS One","28767686","PMC5540507"),
 pm(28,"New insights into the feeding behaviour of the Japanese squid Todarodes pacificus paralarvae, and a combined analysis of metagenome and amino acid isotope ratios. PLoS One 2026;21(3):e0340579","10.1371/journal.pone.0340579","PLoS One","41838746","PMC12991261"),
 pm(29,"Study on the Geographic Variation and Trophic Variation of Todarodes pacificus in Different Areas Based on Stable Isotope Information from the Gladius. Biology (Basel) 2023;12(4):551 (PubMed 표기에서 학명이 빠져 있으나 키워드 'Todarodes pacificus'로 확인)","10.3390/biology12040551","Biology (MDPI)","37106751","PMC10136050"),
 pm(30,"Occurrence of gangliosides in the common squid and pacific octopus among protostomia. Biochim Biophys Acta 2001;1511(2):271-80","10.1016/s0005-2736(01)00282-6","Biochimica et Biophysica Acta","11286970"),
 pm(31,"Discovery of Novel Angiotensin-Converting Enzyme Inhibitory Peptides from Todarodes pacificus and Their Inhibitory Mechanism: In Silico and In Vitro Studies. Int J Mol Sci 2019;20(17):4159 (PubMed 표기에서 학명이 빠져 있으나 키워드 'Todarodes pacificus'로 확인)","10.3390/ijms20174159","International Journal of Molecular Sciences","31454889","PMC6747323"),
 pm(32,"The functional-morphological adaptive strategy of digestive organs of decapodiform cephalopods. J Vet Med Sci 2016;78(1):43-7","10.1292/jvms.15-0185","The Journal of Veterinary Medical Science","26369293","PMC4751115"),
 pm(33,"Identification of high molecular weight proteins in squid muscle by Western blotting analysis and postmortem rheological changes. Biosci Biotechnol Biochem 2004;68(5):1119-24","10.1271/bbb.68.1119","Bioscience, Biotechnology, and Biochemistry","15170118"),
 pm(34,"Deep ocean water alters the cholesterol and mineral metabolism of squid Todarodes pacificus and suppresses its weight loss. Sci Rep 2023;13(1):7591","10.1038/s41598-023-34443-x","Scientific Reports","37164992","PMC10172372"),
 pm(35,"Crystallization and crystal properties of squid rhodopsin. Acta Crystallogr Sect F 2007;63(Pt 6):475-9","10.1107/S1744309107017423","Acta Crystallographica Section F","17554166","PMC2335087"),
]
sec=[]
def add(k,t,b): sec.append({"key":k,"title":t,"body":b})
add("overview","한눈에 보기",
"살오징어(Todarodes pacificus)는 Ommastrephidae과의 오징어로, 식약처 「식품원료 목록」에 '살오징어'(영문 Japanese flying squid, Japanese common squid, 이명 물오징어)라는 수산물 원료로 올라 있다[1]. 목록의 상태는 '사용가능'이고 사용 조건은 '사용가능부위: 전체(내장 제외)'이며, 같은 학명의 '살오징어내장' 행은 '사용불가'로 따로 적혀 있다[1]. 건강기능식품 고시형 원료의 원재료 목록에는 없어 식약처가 정한 지표성분도 없다[1].\n\n"
"이 종은 북서태평양, 특히 동해(일본해)·일본 태평양 연안·동중국해에 사는 상업적으로 중요한 종이다[23]. 한국 동해에서는 수명이 짧은 이 종의 서식 적합도가 2002–2020년에 뚜렷이 낮아졌고 연간 어획량 감소와 함께 나타났다[25]. 목록의 사용 조건상 쓸 수 있는 부위는 내장을 뺀 전체이며[1], 빠지는 내장(간췌장)에는 카드뮴 같은 중금속이 많이 쌓인다는 보고가 있다[5, 6]. 국가표준식품성분표의 살오징어 영양성분 값과 통계청 어업생산 통계의 원표는 이번 조사에서 확인하지 못함.")
add("history","이용·연구 역사",
"한국 동해안에서 오징어는 대표적인 수산물이고, 2013년 논문은 지난 3년 동안 동해안에서 해마다 약 2만 톤이 잡혔으며 그중 70–80%가 산지 근처에서 마른 오징어·염건품·반건조품으로 가공된다고 적었다[8]. 같은 논문은 한국 일부 지역에서 간을 포함한 내장까지 통째로 먹는 식습관이 있다고 소개했다[8].\n\n"
"연구 쪽에서는 1996년 일본에서 이 종의 근육 단백질 트로포미오신이 오징어의 첫 주요 알레르겐으로 밝혀져 'Tod p 1'로 이름 붙었다[9]. 2001년에는 이 종의 간췌장에서 강글리오사이드 GD1a가 분리되어, 선구동물에서 강글리오사이드가 있다는 첫 증거로 보고되었다[30]. 이 종의 망막 로돕신은 G 단백질 결합 수용체 연구를 위해 결정화되어 2.8 Å 해상도까지 회절을 보였다[35]. 2000년대 이후에는 껍질 콜라겐, 내장 레시틴, 연골(갑) 키토산, 오징어유 같은 부산물 활용 연구가 이어졌다[11, 13, 16, 17].")
add("biology","생물 특징·생태",
"살오징어는 Ommastrephidae과에 속하며, 미토콘드리아 단백질 유전자 분석에서 통계적으로 유의하지는 않지만 반딧불오징어류(Watasenia scintillans)와 가까운 관계가 시사되었다[22]. 해양 표층을 헤엄치는 종으로, 간(소화샘)은 하나이고 타원형이며 목록상 화살꼴뚜기(Loligo bleekeri)·창꼴뚜기(Loligo edulis)로 올라 있는 두 종보다 크다[32, 1]. 한국 주문진 앞바다에서 잡힌 시료의 전장은 45–50 cm였다[8].\n\n"
"암컷은 거의 중성부력인 젤리 덩어리 알을 낳는데, 수조 실험에서 수온약층이 있으면 알 덩어리가 그 층에 떠 있었고 없으면 바닥에 가라앉아 배아가 비정상이 되었다[26]. 실험에서 알 덩어리 지름은 17–80 cm였고, 부화 유생은 최대 10일 살았다[26]. 산란장인 쓰시마 해협의 밀도 구조로 보아 알 덩어리는 약 30 m 깊이의 밀도약층 위에 머무를 것으로 추정되었다[27]. 야생 유생의 영양단계는 3.0으로 추정되어 초식성 생물을 먹는 육식성으로 보였다[28]. 갑(gladius)의 안정동위원소 분석에서 동중국해 무리는 저위도·연안 쪽으로, 일본해 무리는 고위도·외해 쪽으로 이동했다[29].")
add("related_species","관련 종·학명 문제",
"같은 속의 Todarodes sagittatus는 「식품원료 목록」에 국문명 없이 'European flying squid'라는 원료명으로 따로 올라 있으며(사용가능, 내장 제외), 이 문서는 그 종의 자료를 섞지 않았다[1]. 목록에는 다른 날오징어류인 빨강오징어(Ommastrephes bartramii), 아메리카대왕오징어(Dosidicus gigas 등), Illex argentinus, Illex illecebrosus, Sthenoteuthis oualaniensis, Nototodarus sloani도 각각 별도 원료로 있다[1]. 이 가운데 빨강오징어·아메리카대왕오징어·I. argentinus는 살오징어와 함께 Ommastrephidae과 공통 프라이머로 검출되는 종으로 다뤄졌다[24]. 빨강오징어 행은 분류가 '식물'로 적혀 있어 원자료의 입력 오류로 보인다[1].\n\n"
"주의할 점으로, 목록에서 '오징어'·'건오징어'·'오징어채' 등 가공품 이름의 행은 학명이 살오징어가 아니라 'Doryteuthis bleekeri Keferstein, D. kensai'로 적혀 있고, 별도의 화살꼴뚜기 행은 Loligo bleekeri로 적혀 있다[1]. 따라서 일상에서 말하는 '오징어'와 목록의 '오징어' 행, 이 종(살오징어)은 학명상 일치하지 않으며, 이 문서는 살오징어 행만 지위 근거로 썼다[1]. 통계청 어업생산동향조사 품목 '오징어'(또는 '살오징어')가 이 학명에 대응하는지는 원표(KOSIS)가 이 환경에서 막혀 확인하지 못함.")
add("cultivation","어획·자원",
"살오징어는 양식이 아닌 어획으로 얻으며, 상업 양식은 확인하지 못함. 일본에서는 심층수로 사육하면 표층수보다 체중 감소가 적었다(2.5% 대 6.95%)는 사육 연구가 있어 양식 기술은 아직 연구 단계로 보인다[34].\n\n"
"한국 주변 연구에서 이 종이 선호한 환경은 표면수온 14.64–27.81 °C, 엽록소-a 0.32–1.28 mg/m³였고, 계절별 서식 적합도 지수는 어획량과 강한 상관(r = 0.8921)을 보였다[25]. 2002–2020년 동해의 서식 적합도는 크게 낮아졌고 연간 어획량 감소와 함께 나타나, 해양 온난화와 1차 생산 감소가 원인으로 추정되었다[25]. 동해·일본해와 동중국해 무리는 유전적 분화가 약하고 유전자 흐름이 강해 사실상 하나의 무리처럼 보였다[23]. 2013년 논문 기준 동해안 어획량은 해마다 약 2만 톤이었으나, 최근 연도 국내 생산량의 공식 수치는 확인하지 못함[8].")
add("processing","저장·가공·판별",
"국내에서 잡힌 오징어의 상당량은 마른 오징어·염건품·반건조품으로 가공된다[8]. 건조 방법을 비교한 연구에서 단백질 체외 소화율은 동결건조 76.81%, 열펌프 건조 70.51%, 생시료 67.99%, 열풍건조 61.47% 순이었다[18]. 오징어젓은 소금 10%에 감마선 10 kGy를 함께 쓰면 소금 20% 대조보다 저장성이 나아졌다는 보고가 있다[19]. 조사(照射)한 마른 오징어에서는 펜타데칸 같은 방사선 분해 탄화수소가 0.5 kGy 이상에서 검출되어 조사 여부 판별 지표로 제안되었다[20]. 사후 5–7시간 사이 외투막 근육의 거대 단백질 커넥틴이 분해되며 육질이 크게 바뀐다[33].\n\n"
"부산물로는 내장을 초임계 이산화탄소로 탈지한 뒤 얻은 레시틴(PC·PE)[11], 껍질 콜라겐과 그 효소 분해물[16], 갑에서 만든 β-키토산[17], 오징어 분말의 인지질을 효소로 바꾼 DHA 결합 리소인지질 기름[14, 15], 정제 오징어유[13]가 연구되었다. 이 원료 행의 사용 조건이 '내장 제외'이므로 내장 유래 소재는 별도 원료 지위를 확인해야 한다[1].")
add("genetics","유전 정보",
"이 종의 미토콘드리아 전체 염기서열은 2004년에 해독되었고, 가장 긴 비암호화 부위, 세 개의 시토크롬 산화효소 유전자, 두 개의 ATP 합성효소 유전자, tRNA(Asp) 유전자가 중복되어 있으며 이 중복은 반딧불오징어와 공유된다[22]. 중복된 사본끼리 염기서열이 거의 같아 두족류 미토콘드리아에서 협조 진화가 일어나는 것으로 해석되었다[22].\n\n"
"북서태평양의 세 무리(일본해 1, 동중국해 2) 29개체를 GBS로 분석해 43,529개 SNP를 얻었고, 유전 다양성과 무리 간 분화가 모두 낮았다[23]. 낮은 다양성은 이형접합체 결핍과 근친교배로, 약한 구조는 강한 유전자 흐름과 지난 200만 년의 인구 역사로 설명되었다[23]. 종 판별용으로는 COI 유전자를 표적으로 한 TaqMan 실시간 PCR이 개발되어 가공품 12종에 적용되었다[24]. 핵 유전체 염색체 수준 조립은 이번 조사에서 확인하지 못함.")
add("safety","안전성",
"식약처 목록은 살오징어의 내장을 '사용불가'로 두고 사용 부위를 '전체(내장 제외)'로 정했다[1]. 내장(간췌장)에는 카드뮴이 많이 쌓여, 일본해 시료 90개체의 간췌장 카드뮴은 평균 50.4 µg/g(습중량, 범위 10–95)이었다[5]. 동중국해 시료에서도 소화샘의 카드뮴이 다른 해역 근연종보다 높았고 비소도 여러 기관에 많았다[6]. 생쥐에게 오징어 간 분말을 8주 먹인 실험에서 간·신장 카드뮴이 늘고 조직 손상이 관찰되었으나, 사람에게 그대로 옮길 수 없는 동물 결과다[8]. 수은은 이 종에서 외투막에 상대적으로 많고 그중 90% 이상이 메틸수은이었다[7]. 간에는 DDT·PCB 같은 잔류성 유기오염물질이 외투막보다 많이 쌓였다[21].\n\n"
"기생충으로는 일본 해역 시료의 17%에서 아니사키스가 나왔고[2], 아니사키스 유충은 주로 내장에 피낭 상태로, 다른 회충류 유충은 외투막 근육에 있었다[3]. 한국 동해 시료의 64.1%에서 촌충 Nybelinia surmenicola 유충이 위·복강에서 발견되었다[4]. 근육 트로포미오신 Tod p 1은 열에 안정한 주요 알레르겐이며 새우 알레르겐과 교차반응한다[9]. 정제 오징어유의 랫드 13주 시험에서 무독성량은 최고 용량 1000 µL/kg 체중/일이었다[13]. 국내 알레르기 유발물질 표시 기준 원문은 이번 조사에서 확인하지 못함.")
C=[
 dict(name="Tropomyosin",name_ko="트로포미오신(Tod p 1)",**{"class":"근육 단백질(알레르겐)"},role="bioactive",part="외투막 근육",content_text="38 kDa, 열에 안정한 단백질(함량 보고 없음)",activity_ko="이 종의 주요 알레르겐으로 새우 알레르겐과 교차반응; 고압(400–600 MPa) 처리로 알레르기성이 낮아짐[9, 10]",source=[9,10]),
 dict(name="Connectin",name_ko="커넥틴(타이틴)",**{"class":"근육 단백질"},role="nutrient",part="외투막 근육",content_text="함량 보고 없음(α·β 이중 띠로 검출)",activity_ko="사후 5–7시간에 α-커넥틴이 β-커넥틴으로 분해되며 외투막 육질(유변 성질)이 크게 바뀜[33]",source=[33]),
 dict(name="Collagen",name_ko="콜라겐(껍질)",**{"class":"구조 단백질"},role="bioactive",part="껍질(내·외피)",content_text="변성온도 내피 27.1 °C, 외피 27.3 °C(소 힘줄 콜라겐보다 약 9 °C 낮음)",activity_ko="효소 분해물의 저분자 분획(F3)이 항산화·티로시나아제·엘라스타아제 억제 활성(시험관)[16]",source=[16]),
 dict(name="Phosphatidylcholine",name_ko="포스파티딜콜린",**{"class":"인지질"},role="bioactive",part="내장(탈지 잔사의 레시틴)",content_text="레시틴 인지질 중 80.5% ± 0.7% (HPLC)",activity_ko="EPA·DHA를 많이 결합한 해양 레시틴으로 산화 안정성이 높았다[11]",source=[11]),
 dict(name="Phosphatidylethanolamine",name_ko="포스파티딜에탄올아민",**{"class":"인지질"},role="bioactive",part="내장(탈지 잔사의 레시틴)",content_text="레시틴 인지질 중 13.2% ± 0.2% (HPLC)",activity_ko="PC와 함께 오징어 인지질의 주성분; sn-2 위치에 DHA·EPA·아라키돈산이 결합[11, 12]",source=[11,12]),
 dict(name="Docosahexaenoic acid",name_ko="DHA(도코사헥사엔산)",**{"class":"오메가-3 지방산"},role="nutrient",part="인지질·오징어유",content_text="함량 수치는 초록에 없음(인지질 PC·PE에 '상당량' 존재)",activity_ko="오징어 분말 인지질로 만든 DHA 결합 리소인지질 기름이 랫드에서 혈청·간 중성지방을 낮춤(동물)[14, 15]",source=[11,14,15]),
 dict(name="Eicosapentaenoic acid",name_ko="EPA(에이코사펜타엔산)",**{"class":"오메가-3 지방산"},role="nutrient",part="인지질·오징어유",content_text="함량 수치는 초록에 없음",activity_ko="DHA와 함께 인지질 sn-2 위치에 결합; 인지질 외용이 아토피 모델 생쥐 피부염을 완화(동물)[12]",source=[11,12]),
 dict(name="Arachidonic acid",name_ko="아라키돈산",**{"class":"오메가-6 지방산"},role="nutrient",part="인지질",content_text="함량 수치는 초록에 없음",activity_ko="오징어 인지질 PC·PE의 sn-2 위치 지방산 중 하나[12]",source=[12]),
 dict(name="Cadmium",name_ko="카드뮴",**{"class":"중금속(오염물질)"},role="bioactive",part="간췌장(내장)",content_text="50.4 ± 26.1 µg/g 습중량(범위 10–95, n=90, 일본해); 가용 분획에 43%",activity_ko="분자량 약 10,000의 카드뮴 결합 단백질에 주로 결합; 내장 섭취 시 노출원[5, 8]",source=[5,6,8]),
 dict(name="Methylmercury",name_ko="메틸수은",**{"class":"유기 수은(오염물질)"},role="bioactive",part="외투막",content_text="외투막 총수은의 90% 이상(농도 수치는 초록에 없음)",activity_ko="소화샘보다 외투막에 수은이 높게 나타난 특이한 분포[7]",source=[7]),
 dict(name="Zinc",name_ko="아연",**{"class":"무기질"},role="nutrient",part="간췌장(내장)",content_text="78.4 ± 69.4 µg/g 습중량(범위 30–297)",activity_ko="간췌장에 카드뮴·구리와 함께 농축[5]",source=[5]),
 dict(name="Copper",name_ko="구리",**{"class":"무기질"},role="nutrient",part="간췌장(내장)",content_text="157.2 ± 126.5 µg/g 습중량(범위 35–290)",activity_ko="간췌장 가용 분획에 66%가 회수됨[5]",source=[5]),
 dict(name="Chitosan",name_ko="β-키토산",**{"class":"다당류"},role="bioactive",part="갑(gladius)",content_text="탈아세틸화도 80 ± 2.5%, 평균 지름 100 nm 이하 입자",activity_ko="시험관에서 항균·항산화 활성[17]",source=[17]),
 dict(name="Ganglioside GD1a",name_ko="강글리오사이드 GD1a",**{"class":"당지질"},role="bioactive",part="간췌장",content_text="함량 보고 없음(주요 산성 지질로 분리·동정)",activity_ko="선구동물 강글리오사이드의 첫 증거[30]",source=[30]),
 dict(name="Ile-Ile-Tyr",name_ko="ACE 억제 펩타이드 IIY",**{"class":"펩타이드"},role="bioactive",part="외투막 미오신 중쇄(가상 분해)",content_text="pIC50 4.58 (합성 펩타이드, 시험관)",activity_ko="미오신 중쇄를 컴퓨터로 가상 분해해 예측한 뒤 합성해 확인한 ACE 억제 활성(사람 효과 미확인)[31]",source=[31]),
]
AS=[
 {"role":"literature","compound":"Cadmium","compound_ko":"카드뮴","part":"간췌장(내장)","content":"50.4 ± 26.1 µg/g 습중량(범위 10–95, n=90); 같은 시료 아연 78.4, 구리 157.2 µg/g[5]","method":"원자흡광분광법(AAS, 불꽃·무불꽃)",
  "conditions":{"instrument":"불꽃 또는 무불꽃 원자흡광분광광도계(수은은 냉증기 원자흡광)","column":"","mobile_phase":"","gradient":"","flow":"","temp":"","detection":"원자흡광","injection":"","sample_prep":"일본의 동해(일본해) 연안에서 채집한 개체의 간췌장을 즉시 떼어 식염수에 담금; 세포 분획은 0.05 M Tris-HCl(pH 7.5) 5배량으로 0 °C에서 균질화 후 원심분리","standard":"","linearity":"","lod":"","loq":"","recovery":""},
  "rationale":"이 종의 카드뮴은 내장(간췌장)에 집중되므로 내장 제외 조건과 내장 섭취 위험을 판단하는 지표로 쓸 수 있다[5, 1]. 전문(스캔 본문) 확인 — 전체 금속 정량용 시료 분해 조건·검출한계·회수율은 본문에 없음.","source":[5,1],"url":"https://doi.org/10.1289/ehp.866549","source_kind":"paper"},
 {"role":"literature","compound":"Arsenic / Cadmium / Mercury","compound_ko":"비소·카드뮴·수은","part":"소화샘·생식소·아가미심장(내장), 외투막","content":"수치는 초록에 없음; 소화샘 카드뮴이 다른 해역 근연종보다 높음[6]","method":"ICP-MS",
  "conditions":{"instrument":"ICP-MS","column":"","mobile_phase":"","gradient":"","flow":"","temp":"","detection":"","injection":"","sample_prep":"동중국해 2010–2014년 채집 개체(수컷 4, 암컷 4)의 내장 기관을 진공 건조","standard":"","linearity":"","lod":"","loq":"","recovery":""},
  "rationale":"저자들은 오징어 모니터링에 소화샘의 카드뮴·비소, 외투막의 수은을 측정하자고 제안했다[6]. 전문 확인 못함(초록만).","source":[6],"url":"https://doi.org/10.1016/j.ecoenv.2017.06.054","source_kind":"paper"},
 {"role":"literature","compound":"Phosphatidylcholine / Phosphatidylethanolamine","compound_ko":"포스파티딜콜린·포스파티딜에탄올아민","part":"내장(초임계 CO2 탈지 잔사의 레시틴)","content":"PC 80.5% ± 0.7%, PE 13.2% ± 0.2% (인지질 중)[11]","method":"HPLC(인지질), GC(지방산)",
  "conditions":{"instrument":"","column":"","mobile_phase":"","gradient":"","flow":"","temp":"","detection":"","injection":"","sample_prep":"내장을 초임계 CO2(35–45 °C, 15–25 MPa)로 탈지한 잔사에서 레시틴 분리; 개별 인지질은 TLC로 정제","standard":"","linearity":"","lod":"","loq":"","recovery":""},
  "rationale":"오징어 내장 레시틴의 품질은 주 인지질 PC·PE의 비율과 EPA·DHA 결합으로 평가되었다[11]. 전문 확인 못함(초록만). 이 원료 행의 사용 부위는 내장 제외이므로 식품원료로서의 근거는 아니다[1].","source":[11,1],"url":"https://doi.org/10.1111/j.1750-3841.2010.02039.x","source_kind":"paper"},
]
D={"slug":"todarodes-pacificus","name_ko":"살오징어","name_en":"Japanese flying squid","scientific_name":"Todarodes pacificus",
 "aliases":["물오징어","Japanese common squid","Japanese flying squid"],
 "sections":sec,"compounds":C,"markers":[],"assays":AS,"nutrients":[],"production":[],"world":[],"gi":[],"orgs":[],"sources":S}
p=pathlib.Path(__file__).resolve().parent.parent/"dossier.json"
p.write_text(json.dumps(D,ensure_ascii=False,indent=1),encoding="utf-8")
for s in sec: print(s["key"],len(s["body"]))
