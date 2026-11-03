import json
from pathlib import Path
A="2026-11-02"
def pm(pmid,title,pub,pmc=None):
    url=f"https://pmc.ncbi.nlm.nih.gov/articles/{pmc}/" if pmc else f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
    return {"title":title,"url":url,"publisher":pub,"accessed":A}
S=[
 {"title":"식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 아벨모스쿠스 사카텐시스잎·오크라·닥풀 항목","url":"https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020","publisher":"식품의약품안전처","accessed":"2026-10-13"},
 pm("32655655","Acute and 28-Day Repeated-Dose Oral Toxicity Assessment of Abelmoschus moschatus Medik. in Healthy Wistar Rats (2020, PMID 32655655, doi:10.1155/2020/1359050)","Evidence-Based Complementary and Alternative Medicine","PMC7321509"),
 pm("35339624","Nephroprotective mechanisms of Ambrette (Abelmoschus moschatus Medik.) leaf extracts in adriamycin mediated acute kidney injury model of Wistar rats (2022, PMID 35339624, doi:10.1016/j.jep.2022.115221)","Journal of Ethnopharmacology"),
 pm("32428654","Protective effects of three selected standardized medicinal plant extracts used in Sri Lankan traditional medicine in adriamycin induced nephrotoxic Wistar rats (2020, PMID 32428654, doi:10.1016/j.jep.2020.112933)","Journal of Ethnopharmacology"),
 pm("21849051","Evaluation of Abelmoschus moschatus extracts for antioxidant, free radical scavenging, antimicrobial and antiproliferative activities using in vitro assays (2011, PMID 21849051, doi:10.1186/1472-6882-11-64)","BMC Complementary and Alternative Medicine","PMC3201038"),
 pm("19610024","Abelmoschus moschatus (Malvaceae), an aromatic plant, suitable for medical or food uses to improve insulin sensitivity (2010, PMID 19610024, doi:10.1002/ptr.2918)","Phytotherapy Research"),
 pm("16041646","Myricetin as the active principle of Abelmoschus moschatus to lower plasma glucose in streptozotocin-induced diabetic rats (2005, PMID 16041646, doi:10.1055/s-2005-871266)","Planta Medica"),
 pm("16203117","Mediation of beta-endorphin by myricetin to lower plasma glucose in streptozotocin-induced diabetic rats (2005, PMID 16203117, doi:10.1016/j.jep.2005.09.001)","Journal of Ethnopharmacology"),
 pm("17694473","Improvement of insulin sensitivity in obese Zucker rats by myricetin extracted from Abelmoschus moschatus (2007, PMID 17694473, doi:10.1055/s-2007-981577)","Planta Medica"),
 pm("25551188","Characterization of ambrette seed oil and its mode of action in bacteria (2014, PMID 25551188, doi:10.3390/molecules20010384)","Molecules","PMC6272330"),
 pm("18656937","Volatile organic nitrogen-containing constituents in ambrette seed Abelmoschus moschatus Medik (Malvaceae) (2008, PMID 18656937, doi:10.1021/jf800958d)","Journal of Agricultural and Food Chemistry"),
 pm("23768323","Abelmoschus esculentus (L.) Moench. and Abelmoschus moschatus Medik: seeds production and analysis of the volatile compounds (2013, PMID 23768323, doi:10.1016/j.foodchem.2013.02.030)","Food Chemistry"),
 pm("21413797","Seed oil and fatty acid content in okra (Abelmoschus esculentus) and related species (2011, PMID 21413797, doi:10.1021/jf104590u)","Journal of Agricultural and Food Chemistry"),
 pm("33303153","Comprehensive bioanalytical multi-imaging by planar chromatography in situ combined with biological and biochemical assays highlights bioactive fatty acids in abelmosk (2020, PMID 33303153, doi:10.1016/j.talanta.2020.121701)","Talanta"),
 pm("11557077","Betaine distribution in the Malvaceae (2001, PMID 11557077, doi:10.1016/s0031-9422(01)00263-1)","Phytochemistry"),
 pm("33237925","Complete chloroplast genomes of three important species, Abelmoschus moschatus, A. manihot and A. sagittifolius: genome structures, mutational hotspots, comparative and phylogenetic analysis in Malvaceae (2020, PMID 33237925, doi:10.1371/journal.pone.0242591)","PLoS ONE","PMC7688171"),
 pm("35363843","Cryopreservation of pollen of Abelmoschus moschatus Medik. subsp. moschatus as an aid to overcome asynchronous flowering for wide hybridization with cultivated okra (2021, PMID 35363843)","CryoLetters"),
 pm("38023890","Genetic enhancement of okra [Abelmoschus esculentus (L.) Moench] germplasm through wide hybridization (2023, PMID 38023890, doi:10.3389/fpls.2023.1284070)","Frontiers in Plant Science","PMC10654990"),
 pm("37004611","Effect of elevated ozone on the antioxidant response, genomic stability, DNA methylation pattern and yield in three species of Abelmoschus having different ploidy levels (2023, PMID 37004611, doi:10.1007/s11356-023-26538-9)","Environmental Science and Pollution Research"),
 pm("38310884","Growth, ultrastructural and physiological characteristics of Abelmoschus cytotypes under elevated ozone stress: a study on ploidy-specific responses (2024, PMID 38310884, doi:10.1071/FP23229)","Functional Plant Biology"),
 pm("25701144","Isolation and purification of trypsin inhibitors from the seeds of Abelmoschus moschatus L. (2015, PMID 25701144, doi:10.1007/s12010-015-1542-1)","Applied Biochemistry and Biotechnology"),
 pm("27057124","Antiurolithiatic activity of Abelmoschus moschatus seed extracts against zinc disc implantation-induced urolithiasis in rats (2016, PMID 27057124, doi:10.4103/0976-0105.177704)","Journal of Basic and Clinical Pharmacy","PMC4804403"),
 pm("11992733","Dermal absorption and disposition of musk ambrette, musk ketone and musk xylene in human subjects (2002, PMID 11992733, doi:10.1016/s0378-4274(01)00548-3)","Toxicology Letters"),
 pm("29846757","A novel zebrafish (Danio rerio) assay for assessing musk ambrette-induced toxicity (2018, PMID 29846757, doi:10.1007/s00128-018-2363-z)","Bulletin of Environmental Contamination and Toxicology"),
 {"title":"Dr. Duke's Phytochemical and Ethnobotanical Databases — Abelmoschus moschatus 씨앗 성분(이 저장소 card.json 의 지표성분 후보로 확인, 원 DB 화면은 직접 열지 못함)","url":"https://phytochem.nal.usda.gov/","publisher":"USDA Agricultural Research Service","accessed":A},
 pm("19849726","A Hibiscus abelmoschus seed extract as a protective active ingredient to favour FGF-2 activity in skin (2009, PMID 19849726, doi:10.1111/j.1468-2494.2009.00538.x)","International Journal of Cosmetic Science"),
 pm("42622685","Elevated ozone reprograms secondary metabolism in Abelmoschus moschatus pods, enhancing antidiabetic and antiobesity bioactivities (2026, PMID 42622685, doi:10.1007/s00299-026-03932-4)","Plant Cell Reports"),
 pm("16646343","Larvicidal activity of Hibiscus abelmoschus Linn. (Malvaceae) against mosquitoes (2006, PMID 16646343)","Journal of the American Mosquito Control Association"),
]
for i,s in enumerate(S,1): s["n"]=i
S=[{"n":s["n"],**{k:v for k,v in s.items() if k!="n"}} for s in S]

sections=[
{"key":"overview","title":"한눈에 보기","body":
"아벨모스쿠스 사카텐시스는 식품의약품안전처 「식품원료 목록」에 '아벨모스쿠스 사카텐시스잎'이라는 이름으로 올라 있는 아욱과 식물 원료이며, 목록에 적힌 학명은 Abelmoschus moschatus Medik. var. tuberosus Borssum., 영문명은 Musk Mallow다[1]. 목록상 사용 상태는 '사용가능'이고 사용가능부위는 잎 하나뿐이다[1]. 그래서 향료 원료로 더 잘 알려진 씨앗(암브렛 씨앗)과 씨앗 기름은 이 목록 항목이 허용한 부위가 아니다[1, 10]. 국문명의 '사카텐시스'가 어떤 학명에서 온 이름인지는 원자료에 설명이 없어 확인하지 못함.\n\n"
"Abelmoschus moschatus는 씨앗에서 사향 비슷한 향이 나는 방향성 약용식물로, 대만 남부를 포함한 아시아 여러 곳에 분포한다[6]. 스리랑카 전통의학에서는 잎·씨앗·뿌리·꽃을 여러 형태로 써 왔다[2]. 잎에 대한 연구는 쥐 실험과 시험관 실험이 대부분이며, 사람에게 잎을 먹여 효과나 안전성을 본 임상시험은 PubMed 검색에서 찾지 못했다[2, 3, 5]. 목록의 변종(var. tuberosus)만 따로 다룬 논문도 PubMed에서 찾지 못해, 아래 연구 결과는 대부분 변종을 밝히지 않은 A. moschatus 또는 아종 moschatus 자료다[2, 5, 17]."},
{"key":"history","title":"이용의 역사","body":
"스리랑카에서는 이 식물을 카푸키니사(Kapukinissa)라 부르며 아유르베다 전통의학에서 팅크·달인 물·반죽 형태로 써 왔다[2]. 씨앗은 열, 장 질환, 신경 쇠약, 피부병 등에, 뿌리와 잎은 임질에, 꽃 우린 물은 피임 목적으로 쓰였다는 기록이 소개되어 있다[2]. 스리랑카에서는 신장 질환에 차·약용 기름·약술 형태로도 써 왔다고 한다[3, 4].\n\n"
"인도에서는 무스크다나(Mushkdana) 또는 카스투리 벤디(Kasturi bhendi)로 불리며, 씨앗 가루를 미지근한 우유에 타서 장 질환·변비·소화불량에 쓰고, 잎 달인 물은 장 질환과 구토에, 잎 가루 팅크는 피부병에 썼다고 한다[5]. 인도에서는 뿌리 물추출물을 모기 유충 방제에 쓰는 연구도 있었다[28]. 대만 연구진은 이 식물을 식품·의약 용도로 쓸 수 있는 방향성 식물로 소개했다[6]. 씨앗 추출물(100~400 mg/kg)을 7일간 먹인 쥐의 요로결석 모델에서 결석 침착이 줄었다는 동물 실험도 있다[22]. 이 기록들은 전통 이용 사례이며 효과를 입증한 것은 아니다[2, 5]."},
{"key":"biology","title":"식물학적 특징","body":
"Abelmoschus(아벨모스쿠스) 속은 아욱과 아욱아과에 속하며, 11종·4아종·5변종으로 정리되어 있고 한해살이에서 여러해살이, 풀에서 관목까지 생김새가 다양하며 아시아·오스트레일리아·아프리카 남서부에 분포한다[16]. 원래 무궁화속(Hibiscus)에 들어 있다가 따로 떨어져 나온 속이다[16].\n\n"
"A. moschatus의 씨앗은 향기가 강해 향료 원료로 쓰이며, 이탈리아 중부에서 기른 세 계통의 씨앗 향기 성분은 93가지가 검출되었다[12]. 씨앗 기름 함량은 미국 유전자원 계통 평가에서 10.3~19.8%였다[13]. 오존 노출 실험에서 이 종은 오크라·A. caillei 보다 배수성이 낮은 계통으로 다뤄졌고, 기공 전도도가 높아 오존 피해를 더 크게 받았다[20]. 아욱과 26분류군의 지상부를 조사한 연구에서 다른 식물은 글리신베타인을 건조중량의 0.5~4.6% 함유했지만 A. moschatus 추출물에서는 검출되지 않았다[15]."},
{"key":"related_species","title":"가까운 종과 구별","body":
"식약처 「식품원료 목록」에는 같은 속의 오크라(Abelmoschus esculentus, 사용가능부위 뿌리·잎·꽃·열매·씨앗)와 닥풀(Hibiscus manihot / Abelmoschus manihot, 사용가능부위 잎)이 이 원료와 별도 항목으로 올라 있다[1]. 세 원료는 학명과 허용 부위가 다르므로 오크라·닥풀의 성분값이나 연구 결과를 이 원료 값처럼 옮겨 쓰면 안 된다[1].\n\n"
"엽록체 유전체를 비교한 연구에서 A. moschatus·A. manihot·A. sagittifolius·오크라는 하나의 무리를 이루었고, 아벨모스쿠스 속은 무궁화속 안에 들어가는 갈래로 나타났다[16]. A. moschatus 아종 moschatus는 오크라와 가까운 야생종으로, 꽃피는 시기가 달라 꽃가루를 액체질소(−196°C)에 보관해 교잡에 쓰는 방법이 연구되었고 24개 조합 중 4개에서 열매와 씨앗을 얻었다[17]. 오크라 육종에서는 야생 아벨모스쿠스 종과의 원연 교잡으로 바이러스병 내성을 옮기려는 시도가 이어지고 있다[18].\n\n"
"이름이 비슷한 '머스크 암브렛(musk ambrette)'은 이 식물 성분이 아니라 4-tert-부틸-3-메톡시-2,6-디니트로톨루엔이라는 합성 니트로 머스크 향료이며, 지금은 향료로 쓰이지 않는다[23, 24]."},
{"key":"cultivation","title":"자생·재배와 원료 수급","body":
"연구에 쓰인 잎은 스리랑카 서부주의 자생지에서 2018년 9월에 채집되었고 국가식물표본관 표본과 대조해 확인되었다[2]. 인도 연구에서는 하이데라바드의 약용·방향식물 연구기관 지역센터에서 2009년 9~10월에 씨앗과 잎을 모았다[5]. 중국 광둥성 농업과학원 시험포장에서 기른 잎으로 엽록체 유전체를 해독한 연구도 있다[16]. 이탈리아 중부에서는 씨앗 생산을 목적으로 A. moschatus 세 계통을 시험 재배했다[12].\n\n"
"인도의 오존 노출 실험에서 오존 농도를 높이자 A. moschatus는 세 아벨모스쿠스 계통 가운데 수량 감소가 가장 컸다[19, 20]. 같은 연구진은 오존 노출이 꼬투리의 페놀·플라보노이드 등 2차 대사산물 축적을 늘렸다고 보고했다[27]. 국내 재배면적·생산량 통계와 지리적 표시 등록은 확인하지 못함."},
{"key":"processing","title":"가공과 제품","body":
"잎 연구에서는 잎을 40°C에서 말려 갈아 헥산·아세트산에틸·부탄올·물 순서로 속슬렛 추출했으며, 수율은 각각 4.29%, 5.76%, 4.53%, 11.40%였다[2]. 인도 연구에서는 잎 가루를 물에 24시간 담그거나, 80~90°C에서 3~4시간 달이거나, 80% 에탄올로 추출했으며 잎 추출물의 총페놀 함량(9.49~13.84 mg GAE/g 건조중량)이 씨앗 추출물(1.56~3.74 mg GAE/g)보다 높았다[5]. 스리랑카 연구는 잎을 4시간 환류 추출한 물추출물을 동결건조해 썼다[4].\n\n"
"씨앗은 주로 향료로 가공된다[11]. 씨앗 이산화탄소 추출물의 염기성 분획에서는 피라진 27종·피리딘 12종 등 질소 화합물 58종이 확인되었고, 이 성분들이 향료업계에서 말하는 자연스럽고 둥근 향을 낸다고 해석되었다[11]. 시판 암브렛 씨앗 기름은 파르네실 아세테이트 51.45%, 암브레톨라이드 12.96%가 주성분이었다[10]. 씨앗 추출물은 화장품 원료로도 개발되었다[26]. 다만 국내 식품원료로 허용된 부위는 잎뿐이다[1]. 식약처 「식품 등의 생산실적」에서 이 원료 품목은 확인하지 못함."},
{"key":"genetics","title":"유전과 분류","body":
"2020년에 A. moschatus·A. manihot·A. sagittifolius의 엽록체 유전체 전체가 해독되어 오크라와 비교되었다[16]. 네 종의 엽록체 유전체는 163,121~163,453 bp로 크기가 비슷했고, 132개 유전자(단백질 87, tRNA 37, rRNA 8)와 약 36%의 GC 함량을 가졌다[16]. 종 구분에 쓸 수 있는 변이가 많은 구간 30곳(start-psbA, atpB-rbcL 등)이 제시되었고, A. moschatus와 A. manihot에는 6염기 반복 SSR이 없었다[16].\n\n"
"오존 노출 실험에서 배수성이 가장 낮은 A. moschatus 계통이 산화 스트레스, DNA 손상, DNA 탈메틸화를 가장 크게 겪었다[19]. 오크라와의 원연 교잡에서는 잡종의 불임을 콜히친으로 염색체를 배가해 극복했다[18]. 식품원료 목록에 적힌 변종 var. tuberosus의 유전 정보는 확인하지 못함."},
{"key":"safety","title":"안전성과 사용 조건","body":
"식약처 「식품원료 목록」에서 이 원료는 '사용가능' 상태이며 사용가능부위는 잎으로 정해져 있다[1]. 씨앗·뿌리·꽃은 이 항목의 허용 부위가 아니다[1].\n\n"
"건강한 쥐에 잎의 헥산(55 mg/kg)·아세트산에틸(75 mg/kg)·부탄올(60 mg/kg)·물(140 mg/kg) 추출물을 28일 동안 먹인 시험에서 죽거나 행동이 달라진 동물은 없었다[2]. 헥산·물 추출물은 혈액·생화학 지표에 유의한 변화가 없었지만, 아세트산에틸·부탄올 추출물은 일부 혈액 지표를 바꿨고 아세트산에틸 추출물은 신장 상대 무게를 줄였다(조직검사에서는 이상 없음)[2]. 잎 추출물에서는 알칼로이드가 검출되지 않았다[2]. 이는 동물 시험이며, 사람의 섭취 안전성을 확인한 자료는 확인하지 못함.\n\n"
"씨앗에는 80°C에서 10분 가열해도 안정한 트립신 저해 단백질 4종이 있다[21]. 추출물이나 마이리세틴이 쥐의 혈당을 낮춘 실험이 있으므로, 당뇨약을 먹는 사람에게 미치는 영향은 알려지지 않았다는 점에 유의해야 한다[6, 7]. 합성 향료 '머스크 암브렛'의 독성 자료는 이 식물과 무관하다[23, 24]. 알레르기·잔류농약에 관한 공공기관 정보는 확인하지 못함."},
]

compounds=[
 {"name":"Myricetin","name_ko":"마이리세틴","class":"플라보놀","role":"bioactive","part":"지상부(잎·줄기 구분 없음)","content_text":"함량 확인하지 못함; 지상부에서 정제해 쥐에 정맥주사로 시험[7]","activity_ko":"당뇨 쥐에 정맥주사하자 혈당이 용량에 따라 낮아짐(1.0 mg/kg)[7]; 베타엔도르핀 분비 증가를 거친다는 쥐 실험 결과[8]; 비만 쥐의 인슐린 감수성 개선[9]. 모두 주사 동물실험이며 먹었을 때의 효과는 아님","source":[7,8,9]},
 {"name":"Ambrettolide","name_ko":"암브레톨라이드((Z)-7-헥사데센-16-올라이드)","class":"대환 락톤(머스크 향 성분)","role":"marker","part":"씨앗(기름)","content_text":"시판 암브렛 씨앗 기름 GC-MS 면적 12.96%[10]; (8Z)-oxacycloheptadec-8-en-2-one 으로서 씨앗 최대 6 ppm(DUKE)[25]","activity_ko":"씨앗 기름의 특징적인 사향 향 성분; 항균 작용은 기름 전체로 시험관에서 본 결과이고 분자 결합은 컴퓨터 계산만 있음[10]","source":[10,25]},
 {"name":"Farnesyl acetate","name_ko":"파르네실 아세테이트","class":"세스퀴테르펜 에스터","role":"bioactive","part":"씨앗(기름)","content_text":"시판 암브렛 씨앗 기름 GC-MS 면적 51.45%(최대 성분)[10]","activity_ko":"씨앗 기름의 주성분; 항균 작용은 기름 전체의 시험관 결과[10]","source":[10]},
 {"name":"Decyl acetate","name_ko":"데실 아세테이트","class":"지방족 에스터","role":"bioactive","part":"씨앗","content_text":"씨앗 기름 GC-MS 면적 6.53%[10]; 씨앗 최대 350 ppm(DUKE)[25]","activity_ko":"씨앗 향기 성분[10]","source":[10,25]},
 {"name":"Dodecyl acetate","name_ko":"도데실 아세테이트(라우릴 아세테이트)","class":"지방족 에스터","role":"bioactive","part":"씨앗(기름)","content_text":"씨앗 기름 GC-MS 면적 7.80%[10]","activity_ko":"씨앗 향기 성분[10]","source":[10]},
 {"name":"(Z)-5-Dodecenyl acetate","name_ko":"(Z)-5-도데세닐 아세테이트","class":"지방족 에스터","role":"bioactive","part":"씨앗","content_text":"씨앗 기름 GC-MS 면적 2.09%[10]; 씨앗 최대 1 ppm(DUKE, 5-dodecenyl acetate)[25]","activity_ko":"씨앗 향기 성분[10]","source":[10,25]},
 {"name":"(Z)-5-Tetradecen-14-olide","name_ko":"(Z)-5-테트라데센-14-올라이드","class":"대환 락톤","role":"marker","part":"씨앗","content_text":"씨앗 최대 30 ppm(DUKE)[25]","activity_ko":"아벨모스쿠스 속에서만 보고된 향 성분 후보[25]","source":[25]},
 {"name":"Tridecane","name_ko":"n-트라이데칸","class":"알케인","role":"bioactive","part":"씨앗(헤드스페이스 향기)","content_text":"이탈리아 재배 3계통 씨앗 헤드스페이스 1.5~26.9%[12]","activity_ko":"씨앗에서 나오는 주요 휘발 성분[12]","source":[12]},
 {"name":"Decanal","name_ko":"데칸알","class":"알데하이드","role":"bioactive","part":"씨앗(헤드스페이스 향기)","content_text":"이탈리아 재배 3계통 씨앗 헤드스페이스 1.6~5.7%[12]","activity_ko":"씨앗에서 나오는 휘발 성분[12]","source":[12]},
 {"name":"Oleic acid","name_ko":"올레산","class":"불포화지방산","role":"nutrient","part":"씨앗·잎·껍질 추출물","content_text":"정량값 확인하지 못함; 스리랑카산 추출물 54종에서 여러 활성을 보인 띠의 주성분으로 확인[14]; 씨앗 기름 올레산 비율은 A. manihot 와 함께 비교 종 중 높은 편[13]","activity_ko":"평판 크로마토그래피와 효소 시험을 결합한 시험관 분석에서 α-글루코시데이스·티로시네이스 억제 등 반응[14]","source":[13,14]},
 {"name":"Linoleic acid","name_ko":"리놀레산","class":"불포화지방산","role":"nutrient","part":"씨앗·잎·껍질 추출물","content_text":"정량값 확인하지 못함; 올레산과 같은 띠에서 함께 검출[14]","activity_ko":"시험관 효과 지향 분석에서 활성 띠의 구성 성분[14]","source":[14]},
 {"name":"Palmitic acid","name_ko":"팔미트산","class":"포화지방산","role":"nutrient","part":"씨앗·잎·껍질 추출물","content_text":"정량값 확인하지 못함; 활성 띠에서 함께 검출[14]","activity_ko":"시험관 분석에서 활성 띠의 구성 성분[14]","source":[14]},
 {"name":"Glycine betaine","name_ko":"글리신베타인","class":"베타인","role":"nutrient","part":"지상부","content_text":"A. moschatus 지상부 추출물에서 검출되지 않음(다른 아욱과 식물은 건조중량 0.5~4.6%)[15]","activity_ko":"아욱과의 공통 성분이 이 종에서는 없다는 점에서 구별 형질로 볼 수 있음[15]","source":[15]},
]

assays=[
 {"role":"literature","compound":"Total phenolics (as gallic acid)","compound_ko":"총페놀(갈산 당량)","part":"잎(그늘 건조 분말의 물·열수·80% 에탄올 추출물)","content":"잎 추출물 9.49~13.84 mg GAE/g 건조중량(80% 에탄올 추출물 AML-IV 13.84 ± 0.10); 씨앗 추출물 1.56~3.74 mg GAE/g[5]","method":"Folin-Ciocalteu 비색법(UV-Vis 분광광도계)",
  "conditions":{"instrument":"UV-Vis 분광광도계(기종 미기재)","detection":"765 nm","sample_prep":"추출물 원액 10 μL + Folin-Ciocalteu 시약 100 μL, 10분 뒤 20% Na2CO3 300 μL, 증류수로 1 mL, 암소 2시간","standard":"갈산(gallic acid), mg GAE/g 건조중량, 3반복 평균"},
  "rationale":"잎의 항산화 활성이 총페놀 함량과 함께 움직인다고 보고되어 잎 추출물 비교 지표로 쓰였다[5]. 개별 성분 정량이 아니고 HPLC 지표성분 정량 논문은 찾지 못함","source":[5],"url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC3201038/","source_kind":"paper"},
 {"role":"literature","compound":"Total flavonoids (as quercetin)","compound_ko":"총플라보노이드(퀘르세틴 당량)","part":"잎(위와 같은 추출물)","content":"잎 추출물 최대 6.0 mg QE/g 건조중량(AML-IV), 씨앗 추출물 최대 0.26 mg QE/g[5]","method":"염화알루미늄 비색법",
  "conditions":{"detection":"510 nm","sample_prep":"추출물 20 μL + Milli-Q 물 500 μL + 5% NaNO2 30 μL, 5분 뒤 10% AlCl3 60 μL, 1 M NaOH 350 μL와 물 40 μL로 1 mL, 실온 15분","standard":"퀘르세틴, mg QE/g 건조중량, 3반복 평균"},
  "rationale":"잎이 씨앗보다 플라보노이드가 많다는 비교에 쓰인 지표[5]","source":[5],"url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC3201038/","source_kind":"paper"},
 {"role":"literature","compound":"Ambrettolide","compound_ko":"암브레톨라이드","part":"씨앗 기름(시판품) — 식품원료 허용 부위(잎)가 아님","content":"GC-MS 면적 12.96%(파르네실 아세테이트 51.45%)[10]","method":"GC-MS(상대 면적%, 정량 표준물질 없음)",
  "conditions":{"instrument":"Thermo Trace 1310 GC + Thermo ISQ LT 질량검출기","column":"TG-5MS, 30 m × 0.25 mm, 막두께 0.25 μm","mobile_phase":"운반기체 헬륨","gradient":"50°C 5분 유지 후 4°C/min 으로 250°C","injection":"1 μL, 분할비 1:10, 주입구 220°C, 이송관 250°C","detection":"EI 70 eV, NIST 라이브러리 비교"},
  "rationale":"씨앗 기름 특유의 사향 향 성분으로 암브렛 씨앗 기름을 특징짓는다[10]. 잎에서는 보고를 확인하지 못함","source":[10],"url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC6272330/","source_kind":"paper"},
]

d={"slug":"abelmoschus-moschatus","name_ko":"아벨모스쿠스 사카텐시스","name_en":"Musk mallow (ambrette)",
 "scientific_name":"Abelmoschus moschatus Medik. var. tuberosus Borssum.",
 "aliases":["아벨모스쿠스 사카텐시스잎","Abelmoschus moschatus Medik.","Musk mallow","Ambrette","Abelmosk","Hibiscus abelmoschus"],
 "sections":sections,"compounds":compounds,"markers":[],"assays":assays,"nutrients":[],"production":[],"world":[],"gi":[],"orgs":[],"sources":S}
Path(__file__).resolve().parents[1].joinpath("dossier.json").write_text(json.dumps(d,ensure_ascii=False,indent=1),encoding="utf-8")
for s in sections: print(s["key"],len(s["body"]))
