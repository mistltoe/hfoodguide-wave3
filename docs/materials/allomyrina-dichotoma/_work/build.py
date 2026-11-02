import json
A="2026-11-02"
def pm(n,title,doi,acc=A):
    return {"n":n,"title":title,"url":"https://doi.org/"+doi,"publisher":"PubMed","accessed":acc}
sources=[
 {"n":1,"title":"식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 장수풍뎅이유충(Allomyrina dichotoma), 식품원료(A코드)·축,수산물 외 동물, 사용가능, 사용가능부위 '-', 사용조건 빈칸; 대조: 흰점박이꽃무지유충·갈색거저리유충·탈지갈색거저리유충분말('한시적 기준·규격에서 전환된 원료')·쌍별귀뚜라미·메뚜기·누에·아메리카 왕거저리 유충 탈지분말 행 (로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json)","url":"https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020","publisher":"식품의약품안전처","accessed":"2026-10-13"},
 pm(2,"Subchronic Oral Dose Toxicity of Freeze-dried Powder of Allomyrina dichotoma Larvae — Toxicol Res 2015 (PMID 25874035, PMC4395657, 전문 확인; 안전성평가연구소·농촌진흥청 국립농업과학원)","10.5487/TR.2015.31.1.069"),
 pm(3,"Fatty Acid and Volatile Oil Compositions of Allomyrina dichotoma Larvae — Prev Nutr Food Sci 2012 (PMID 24471102, PMC3866728, 전문 확인)","10.3746/pnf.2012.17.4.310"),
 pm(4,"Technical Functional Properties of Water- and Salt-soluble Proteins Extracted from Edible Insects — Food Sci Anim Resour 2019 (PMID 31508594, PMC6728818, 전문 확인)","10.5851/kosfa.2019.e56"),
 pm(5,"Allomyrina dichotoma Larva Extract Ameliorates the Hepatic Insulin Resistance of High-Fat Diet-Induced Diabetic Mice — Nutrients 2019 (PMID 31277481, PMC6683090, 초록 확인)","10.3390/nu11071522"),
 pm(6,"Phylogeny and biogeography of the Japanese rhinoceros beetle, Trypoxylus dichotomus (Coleoptera: Scarabaeidae) based on SNP markers — Ecol Evol 2020 (PMID 33437420, PMC7790660, 전문 확인(학명 기울임 글자가 빠진 전문))","10.1002/ece3.6982"),
 pm(7,"The draft genome sequence of the Japanese rhinoceros beetle Trypoxylus dichotomus septentrionalis towards an understanding of horn formation — Sci Rep 2023 (PMID 37253792, PMC10229555, 전문 확인)","10.1038/s41598-023-35246-w"),
 pm(8,"A chromosome-level genome assembly and intestinal transcriptome of Trypoxylus dichotomus (Coleoptera: Scarabaeidae) to understand its lignocellulose digestion ability — GigaScience 2022 (PMID 35764601, PMC9239855, 초록·서론 확인)","10.1093/gigascience/giac059"),
 pm(9,"Identification and Characterization of Genes for the Allo A Lectins in Japanese Rhinoceros Beetle (Trypoxylus dichotomus [Allomyrina dichotoma]) — Biochem Genet 2021 (PMID 34100176, 초록만 확인)","10.1007/s10528-021-10088-1"),
 pm(10,"Glycerophospholipid Profiles of Allomyrina dichotoma Larvae at Different Instars Based on Lipidomics and Transcriptomics Suggest a Promising Lipid Source — Insects 2025 (PMID 41465659, PMC12733726, 전문 확인)","10.3390/insects16121220"),
 pm(11,"Comprehensive Analysis of Trypoxylus dichotomus: Inorganic Elements, Amino Acids, and Bioactive Compounds and Their Anticancer, Antioxidant, and Neuroprotective Properties — Molecules 2025 (PMID 39860090, PMC11767710, 전문 확인; 중국 시료, 유충·번데기·성충)","10.3390/molecules30020220"),
 pm(12,"Effects of Edible Insect Powders as Meat Partial Substitute on Physicochemical Properties and Storage Stability of Pork Patties — Food Sci Anim Resour 2024 (PMID 38974719, PMC11222701, 전문 확인)","10.5851/kosfa.2024.e17"),
 pm(13,"Physicochemical and textural properties of emulsions prepared from the larvae of the edible insects Tenebrio molitor, Allomyrina dichotoma, and Protaetia brevitarsis seulensis — J Anim Sci Technol 2021 (PMID 33987615, PMC8071746, 전문 확인)","10.5187/jast.2021.e25"),
 pm(14,"Characterization of chitosan extracted from Mealworm Beetle (Tenebrio molitor, Zophobas morio) and Rhinoceros Beetle (Allomyrina dichotoma) and their antibacterial activities — Int J Biol Macromol 2019 (PMID 30500507, 초록만 확인)","10.1016/j.ijbiomac.2018.11.242"),
 pm(15,"Adsorption properties of heavy metals and antibiotics by chitosan from larvae and adult Trypoxylus dichotomus — Carbohydr Polym 2021 (PMID 34823771, 초록만 확인)","10.1016/j.carbpol.2021.118735"),
 pm(16,"Isolation and characterization of a new member of the insect defensin family from a beetle, Allomyrina dichotoma — Biochem Biophys Res Commun 1996 (PMID 8607799, 초록만 확인)","10.1006/bbrc.1996.0438"),
 pm(17,"Purification, characterization and gene expression of a glycine and proline-rich antibacterial protein family from larvae of a beetle, Allomyrina dichotoma — Insect Mol Biol 2001 (PMID 11520352, 초록만 확인)","10.1046/j.0962-1075.2001.00261.x"),
 pm(18,"Purification and characterization of a lectin from the beetle, Allomyrina dichotoma — J Biochem 1984 (PMID 6423623, 초록만 확인)","10.1093/oxfordjournals.jbchem.a134590"),
 pm(19,"Complete genome sequence of an oryctes rhinoceros nudivirus isolated from Korean rhinoceros beetles (Trypoxylus dichotomus) in Korea — Virus Res 2023 (PMID 37442527, PMC10485680, 초록만 확인)","10.1016/j.virusres.2023.199167"),
 pm(20,"Anti-Thrombotic, Anti-Oxidant and Haemolysis Activities of Six Edible Insect Species — Foods 2020 (PMID 32244589, PMC7231258, 초록만 확인)","10.3390/foods9040401"),
 pm(21,"Allomyrina dichotoma larval extract has protective effects against gut permeability of dextran sulfate sodium-fed Drosophila by E-cadherin and armadillo — J Ethnopharmacol 2021 (PMID 33421598, 초록만 확인)","10.1016/j.jep.2021.113786"),
 pm(22,"Exploring the Role of a Novel Peptide from Allomyrina dichotoma Larvae in Ameliorating Lipid Metabolism in Obesity — Int J Mol Sci 2020 (PMID 33198343, PMC7698306, 초록만 확인)","10.3390/ijms21228537"),
 pm(23,"Allomyrinasin, an Edible Insect-Derived Peptide, Ameliorates High-Fat Diet-Induced Hepatic Oxidative Stress and Metabolic Dysfunction — Antioxidants 2026 (PMID 42352061, PMC13296046, 초록만 확인)","10.3390/antiox15060755"),
 pm(24,"DPP-4 inhibitory and insulin-signaling-modulating potential of Allomyrina dichotoma larval protein hydrolysate — Food Sci Biotechnol 2026 (PMID 42761324, PMC13586093, 초록만 확인)","10.1007/s10068-026-02216-7"),
 pm(25,"Allergenicity of edible insect proteins: Cross-reactivity, processing effects, and food safety considerations — Food Chem 2026 (리뷰, PMID 42330644, 초록만 확인)","10.1016/j.foodchem.2026.150124"),
 pm(26,"Insect Allergens on the Dining Table — Curr Protein Pept Sci 2020 (리뷰, PMID 31309888, 초록만 확인)","10.2174/1389203720666190715091951"),
 {"n":27,"title":"농림축산식품부·식품의약품안전처·농촌진흥청 보도자료 「식용곤충 식품원료 인정 확대」 (2016년 「식품의 기준 및 규격」 개정안 행정예고 관련) — WebSearch 검색 요약으로만 확인, 원문은 네트워크 허용 목록 밖이라 열지 못함","url":"https://www.korea.kr/briefing/pressReleaseView.do?newsId=156160192","publisher":"대한민국 정책브리핑","accessed":A},
 {"n":28,"title":"농촌진흥청 보도자료 「식용곤충, “장수애·쌍별이로 불러주세요”」 — 제목과 WebSearch 검색 요약으로만 확인, 원문은 열지 못함","url":"https://www.korea.kr/briefing/pressReleaseView.do?newsId=156131662","publisher":"대한민국 정책브리핑","accessed":A},
 {"n":29,"title":"농림축산식품부 보도자료(2021년 4월 9일 조간) — 식용 곤충 2016년 3종에서 추가(갈색거저리·흰점박이꽃무지·장수풍뎅이 유충, 쌍별귀뚜라미) 정리; WebSearch 검색 요약으로만 확인, 원문은 열지 못함","url":"https://www.mafra.go.kr/bbs/mafra/68/248390/download.do","publisher":"농림축산식품부","accessed":A},
 {"n":34,"title":"농촌진흥청 보도자료 「'아메리카왕거저리 유충' 새로운 식품원료 인정」 — '2015년 장수풍뎅이 유충과 쌍별귀뚜라미를 식품원료로 인정' 문구를 WebSearch 검색 요약으로만 확인, 원문은 네트워크 허용 목록 밖이라 열지 못함","url":"https://www.rda.go.kr/board/board.do?mode=view&prgId=day_farmprmninfoEntry&dataNo=100000760981","publisher":"농촌진흥청","accessed":A},
 pm(30,"Heightened condition-dependent growth of sexually selected weapons in the rhinoceros beetle, Trypoxylus dichotomus (Coleoptera: Scarabaeidae) — Integr Comp Biol 2014 (PMID 24827150, 초록만 확인)","10.1093/icb/icu041"),
 pm(31,"Pivot burrowing of scarab beetle (Trypoxylus dichotomus) larva — Sci Rep 2021 (PMID 34272407, PMC8285476, 전문 확인)","10.1038/s41598-021-93915-0"),
 pm(32,"Allomyrina dichotoma larva extract attenuates free fatty acid-induced lipotoxicity in pancreatic beta cells — Nutr Res Pract 2021 (PMID 34093971, PMC8155218, 초록만 확인)","10.4162/nrp.2021.15.3.294"),
 pm(33,"Erysipelothrix larvae sp. nov., isolated from the larval gut of the rhinoceros beetle, Trypoxylus dichotomus (Coleoptera: Scarabaeidae) — Antonie van Leeuwenhoek 2015 (PMID 25534074, 초록만 확인)","10.1007/s10482-014-0342-x"),
]

S=[]
S.append(("overview","한눈에 보기",
"장수풍뎅이(Allomyrina dichotoma)는 풍뎅이과 장수풍뎅이아과에 속하는 동아시아의 큰 딱정벌레이고, 식품원료로 쓰는 것은 땅속 부엽토에서 자라는 유충이다[6, 7]. 최근 분류학·유전체 논문은 이 종을 Trypoxylus dichotomus로 부르며, 두 학명은 같은 종을 가리킨다[7, 9]. 식약처 「식품원료 목록」에는 '장수풍뎅이유충' 한 행이 학명 Allomyrina dichotoma, 식품원료(A코드)·축,수산물 외 동물, 사용가능으로 실려 있다[1]. 이 행의 사용가능부위 칸은 '-'이고 사용 조건 칸은 비어 있어, 원료명대로 유충 자체가 대상이다[1]. 같은 목록의 탈지갈색거저리유충분말 행에는 '한시적 기준·규격에서 전환된 원료'라는 표시가 있으나 이 행에는 그런 표시가 없다[1].\n\n동결건조 유충 분말은 조단백질 38.17%, 조지방 32.72%, 탄수화물 22.73%였고, 지방산의 57.7%가 올레산 중심의 단일불포화지방산이었다[3]. 쥐 13주 반복투여 시험의 무독성량은 하루 2,500 mg/kg 이상이었다[2]. 추출물·펩타이드의 혈당·지방간 개선 보고는 세포·동물 실험 결과이며 사람 효과는 확인되지 않았다[5, 22, 23, 24, 32]. 이 종을 원재료로 하는 건강기능식품 고시형 원료는 확인하지 못함."))
S.append(("history","역사",
"장수풍뎅이는 중국 전통의학에서 2,000년 가까이 쓰인 곤충으로 소개된다[6]. 한 연구는 이 유충이 1596년부터 한국과 중국에서 장 관련 질환에 민간약으로 쓰였다고 적었다[21]. 국내 독성 연구진도 유충이 당뇨 치료의 전통 약재로 쓰여 왔다고 썼다[2]. 한국에서는 장수풍뎅이와 유충이 인기 있는 애완 곤충이기도 하다[2, 6].\n\n2015년 논문은 당시 국내에서 식품공전에 오른 곤충이 일부뿐이었고, 장수풍뎅이 유충은 사람 독성 정보가 없어 식품 사용이 공식적으로 금지된 상태였다고 적는다[2]. 이에 안전성평가연구소와 농촌진흥청 국립농업과학원이 참여해 GLP 규정에 따른 13주 경구 독성시험을 수행했다[2]. 정부 보도자료 검색 요약에 따르면 이 유충은 2015년 한시적 식품원료로 인정되었고, 2016년 「식품의 기준 및 규격」 개정안 행정예고로 인정받은 업체 외 모든 영업자가 쓸 수 있는 원료로 확대되었다(원문은 열지 못함)[27, 29, 34]. 농촌진흥청은 이 유충에 '장수애'라는 애칭을 붙였다는 보도자료 제목이 확인된다(본문은 열지 못함)[28]. 한시적 인정일·식품공전 고시일의 공식 원문은 확인하지 못함."))
S.append(("biology","곤충학적 특징",
"장수풍뎅이는 딱정벌레목 풍뎅이과 장수풍뎅이아과(Dynastinae)에 속하고, 일본·중국·한반도·대만·베트남·미얀마·라오스·인도·태국 등 동아시아에 넓게 분포한다[6, 7]. 어른벌레는 몸길이가 91.7 mm에 이르는 큰 딱정벌레이고, 수컷만 머리와 앞가슴에 갈라진 뿔을 가진다[7]. 수컷 뿔의 크기는 유충 때 먹이 상태에 특히 민감하게 달라진다[30].\n\n한 해에 한 세대를 거치며, 유충은 가을부터 봄까지 부엽토나 썩은 나무를 먹고 자란다[7]. 번데기 직전 유충은 배설물과 부엽토로 땅속에 번데기 방을 만들고, 어른벌레는 초여름 활엽수림에 나타나 수액을 먹으며 최대 약 3개월 살고 겨울을 나지 못한다[7]. 유충은 3령까지 자라며, 수컷 유충은 항문 마디 배쪽에 V자나 선 모양의 짙은 홈이 있어 암컷과 구별된다[10]. 종령 유충의 몸통 지름은 약 20 mm로 지렁이보다 훨씬 굵고, 몸을 회전시키며 흙을 파고든다[31]. 유충은 셀룰레이스 등 소화효소로 나무·부엽토의 리그노셀룰로스를 분해하는 목질·부식질 섭식 곤충이다[8]."))
S.append(("related_species","가까운 종·혼동",
"식약처 「식품원료 목록」에서 같은 Allomyrina 속의 다른 원료는 없고, 함께 실린 식용곤충으로 흰점박이꽃무지유충(별명 굼뱅이·꽃뱅이, Protaetia brevitarsis)·갈색거저리유충·쌍별귀뚜라미·메뚜기·누에·아메리카 왕거저리 유충 탈지분말이 있다[1]. 흰점박이꽃무지유충은 별명이 '굼뱅이'인 꽃무지류 유충으로 생김새가 비슷하지만 다른 종이므로 성분·안전성 자료를 섞어 쓰면 안 된다[1, 13]. 국내 비교 연구에서 동결건조 유충의 단백질은 갈색거저리 58.44%, 장수풍뎅이 49.68%, 흰점박이꽃무지 51.08%였다[4].\n\n학명은 식약처 목록이 Allomyrina dichotoma를, 유전체·분류 논문이 Trypoxylus dichotomus를 쓰며, 렉틴 유전자 논문은 두 이름을 함께 적었다[1, 7, 9]. 이 종에는 10개 아종과 근연종 1종이 제안되었으나, 단일염기다형성 분석에서는 북부·남부·서부 세 유전 집단으로 나뉘고 일부 아종은 여러 계통에 흩어졌다[6]. 애완용으로 옮겨진 개체가 방사되며 다른 계통끼리 섞인 흔적도 보고되었다[6]. 일본 집단은 아종 T. d. septentrionalis로 유전체가 해독되었다[7]."))
S.append(("cultivation","사육",
"실험실 사육 예로, 한 지질체 연구는 톱밥을 먹이로 25 °C, 상대습도 60%, 빛 12시간·어둠 12시간 조건에서 유충을 길렀다[10]. 일본 연구진은 종령 유충을 부엽토와 함께 한 마리씩 플라스틱 용기에 넣어 10 °C에 두어 번데기가 되는 시기를 늦췄고, 쓰기 전에 실온으로 옮겨 28 °C에서 길렀다[7]. 유충은 버섯 재배 후 남은 배지를 생물학적으로 분해하는 데에도 산업적으로 이용된다[8].\n\n국내 연구에 쓰인 동결건조 유충은 전북 정읍의 농가나 충북농업기술원에서 공급되었다[4, 12, 13]. 사육 질병으로는 한국 장수풍뎅이에서 2015년 처음 확인된 누디바이러스(TdNV-Korea)가 있으며, 야자장수풍뎅이 누디바이러스(OrNV)의 한 계통으로 분석되었다[19]. 충북 영동에서 채집한 유충의 장에서는 새로운 세균 종(Erysipelothrix larvae)이 분리되었다[33]. 국내 사육 농가 수·생산량 같은 공식 통계는 확인하지 못함."))
S.append(("processing","가공·제품",
"독성시험에 쓰인 원료는 국내 업체가 공급한 동결건조 유충을 갈아 멸균한 분말이었다[2]. 단백질 소재화 연구에서는 동결건조 유충 가루를 헥세인(1:5)으로 반복 탈지했고, 탈지 후 단백질은 65.12%, 지방은 0.63%였다[4]. 같은 연구에서 물 추출 단백질 농도는 5.58%로 세 종 중 가장 높았으나, 이 추출 단백질의 거품·유화 안정성은 빨리 무너졌다[4]. 유충을 갈아 만든 유화물은 pH 7.20으로 비교한 세 종 가운데 가장 높았다[13].\n\n돼지고기 패티에 유충 가루를 20% 넣으면 보수력이 78.06%로 대조군(55.31–60.14%)보다 높고 가열 감량은 10.00%로 낮았지만, 전체 기호도는 1.10점으로 대조군(4.20–4.30점)보다 크게 낮았다[12]. 유충 키틴 수율은 10.53%, 키틴에서 얻은 키토산 수율은 83.37%였다[14]. 유충·성충 키토산은 납(934 mg/g) 같은 중금속과 항생제를 흡착하는 소재로도 연구되었다[15]. 효소 가수분해물에서는 지방 축적을 줄이는 펩타이드(EIA10)와 DPP-4 억제 분획(IC50 0.72 mg/mL)이 분리되었으나 세포·동물 실험 단계다[22, 24]. 이 원료의 건강기능식품 개별인정형 원료는 I1020 목록에서 찾지 못했다[1]."))
S.append(("genetics","유전체·종 판별",
"2022년 중국 연구진은 유전체를 636.27 Mb로 조립하고 스캐폴드의 95.37%를 염색체 10개에 배치했다[8]. 이 유전체에서는 트립신 등 소화 관련 유전자군 2개가 크게 늘어나 있었고, 소똥구리류 Onthophagus taurus와는 약 1억 2천만 년 전에 갈라진 것으로 추정되었다[8]. 2023년 일본 아종 초안 유전체는 615 Mb(유세포 측정 추정치의 80%), 스캐폴드 N50 8.02 Mb, 반복서열 49.5%, 단백질 유전자 23,987개였고 미토콘드리아 유전체는 20,217 bp였다[7].\n\n아시아 5개국 44곳의 53개체를 SLAF-seq로 분석해 단일염기다형성 46,939개를 얻었고, 이 표지로 세 유전 집단이 구분되었다[6]. 혈림프 렉틴(allo A)의 소단위 유전자는 α·β·γ1·γ2 네 가지로, 염기서열 일치도 87.6–92.6%의 유전자군을 이룬다[9]. 식품 속에서 이 종을 다른 식용곤충과 가려내는 PCR 판별법은 확인하지 못함."))
S.append(("safety","안전성",
"동결건조 유충 분말을 쥐에게 하루 250·850·2,500 mg/kg씩 13주 먹인 GLP 시험에서 사망·임상 증상·체중·혈액·장기 무게·조직 소견에 투여 관련 변화가 없었고, 무독성량은 하루 2,500 mg/kg 이상이었다[2]. 혈청 IgE는 변하지 않았고, 히스타민은 투여량에 따라 1.1–1.6배 늘어 2,500 mg/kg 암컷에서만 통계적으로 유의했으나 연구진은 독성으로 보지 않았다[2]. 시험관 시험에서 유충 에탄올 추출물은 혈소판 응집을 대조군의 194–246% 수준으로 높인 여러 곤충 추출물 중 하나였다[20].\n\n식용곤충에서 지금까지 밝혀진 알레르겐은 대부분 트로포미오신·아르기닌 키나아제 같은 무척추동물 공통 알레르겐이며, 갑각류·집먼지진드기 감작에 따른 교차반응일 수 있다[26]. 2026년 리뷰도 이 단백질들이 갑각류·진드기 알레르겐과 구조와 IgE 결합 부위를 공유한다고 정리했다[25]. 이 종 유충에 대한 사람 알레르기 사례나 교차반응 연구, 식약처의 이 원료 전용 알레르기 표시 기준은 확인하지 못함. 중국 시료(유충·번데기·성충) 분석은 유해 중금속이 과다하지 않다고 보고했다[11]."))

sections=[{"key":k,"title":t,"body":b} for k,t,b in S]

def C(name,ko,cls,role,part,ct,act,src): return {"name":name,"name_ko":ko,"class":cls,"role":role,"part":part,"content_text":ct,"activity_ko":act,"source":src}
compounds=[
 C("Protein","조단백질","단백질","nutrient","유충 동결건조 분말","동결건조 분말 38.17%(질소계수 6.25)[3]; 동결건조 유충 49.68%, 탈지 후 65.12%[4]; 패티용 분말 32.75%[12]","분말 단백질 함량은 시료·분석법에 따라 32.75–49.68%로 차이가 큼[3, 4, 12]",[3,4,12]),
 C("Lipid","조지방","지질","nutrient","유충 동결건조 분말","32.72%(Soxhlet)[3]; 24.54%[4]; 2.63%(Folch법, 패티용 분말)[12]; 총지방산 수율 39.87%(건물)[3]","올레산 중심의 단일불포화지방산이 지방산의 57.7%[3]",[3,4,12]),
 C("Oleic acid","올레산","단일불포화지방산","nutrient","유충 동결건조 분말","19.13 g/100 g(건물)[3]","가장 많은 지방산이자 독성 연구에서 지표 성분으로 기재됨[2, 3]",[2,3]),
 C("Palmitic acid","팔미트산","포화지방산","nutrient","유충 동결건조 분말","12.52 g/100 g(건물)[3]","두 번째로 많은 지방산[3]",[3]),
 C("Palmitoleic acid","팔미톨레산","단일불포화지방산","nutrient","유충 동결건조 분말","3.71 g/100 g(건물)[3]","올레산·팔미트산·리놀레산과 합쳐 총지방산의 90% 이상[3]",[3]),
 C("Linoleic acid","리놀레산","오메가-6 다불포화지방산","nutrient","유충 동결건조 분말","2.08 g/100 g(건물); 총지방산의 5.3%[3]","필수지방산[3]",[3]),
 C("alpha-Linolenic acid","알파-리놀렌산","오메가-3 다불포화지방산","nutrient","유충 동결건조 분말","총지방산의 0.4%[3]","필수지방산, 함량은 적음[3]",[3]),
 C("Phosphatidylethanolamine","포스파티딜에탄올아민","글리세로인지질","nutrient","유충(1–3령, 습중량)","총 글리세로인지질의 47.58%(분자종 223개)[10]","가장 많은 인지질 종류, 3령에서 크게 증가[10]",[10]),
 C("Phosphatidylcholine","포스파티딜콜린","글리세로인지질","nutrient","3령 유충(습중량)","23,118.33 ± 602.74 μg/g; 총 글리세로인지질의 33.03%(분자종 328개)[10]","분자종 수가 가장 많은 인지질[10]",[10]),
 C("Cardiolipin","카디오리핀","글리세로인지질","nutrient","유충(습중량)","1령 1,198.09, 2령 1,018.48, 3령 2,168.07 μg/g[10]","미토콘드리아 막 인지질, 3령에서 증가[10]",[10]),
 C("Chitin","키틴","아미노다당류","nutrient","유충","유충 키틴 수율 10.53%(번데기 12.70%, 성충 14.20%)[14]","키토산 원료; 키틴→키토산 수율 83.37%[14]",[14]),
 C("Glutamic acid","글루탐산","아미노산","nutrient","탈지 유충 물 추출 단백질 용액(1%)","64.75 mg/g(물 추출), 42.04 mg/g(염 추출)[4]","추출 단백질 용액에서 가장 많은 아미노산 중 하나[4]",[4]),
 C("Gallic acid","갈산","페놀산","bioactive","동결건조 유충 분말 메탄올 추출액","4.46 μg/L(추출액); 카페인산 3.52, 시링산 3.83, 페닐아세트산 5.27 μg/L[12]","패티의 DPPH 소거능 증가와 관련지어 해석됨[12]",[12]),
 C("Allomyrina defensin","장수풍뎅이 디펜신","항균 펩타이드(43개 아미노산)","bioactive","세균 접종 유충의 체액","정량값 없음[16]","그람양성균·MRSA에 항균, 그람음성균에는 활성 없음(시험관)[16]",[16]),
 C("Allo A lectin","장수풍뎅이 렉틴(allo A)","당단백질(렉틴)","bioactive","유충 혈림프","정량값 없음; allo A-I·II 분자량 65,000·66,500(겔 여과)[18]","β결합 D-갈락토스(락토스 등)에 결합하는 렉틴, N-아세틸락토사민 결합 활성이 강함[18, 9]",[18,9]),
 C("Coleoptericin A","콜레옵테리신 A","항균 단백질(72개 아미노산, 글리신·프롤린 풍부)","bioactive","세균 접종 유충의 지방체·혈구","정량값 없음[17]","황색포도알균·MRSA·고초균에 항균(재조합 단백질, 시험관)[17]",[17]),
]
nutrients=[{"form":"동결건조 유충 분말","basis":"분말 100 g(수분 2.25%)","items":[{"name":"단백질","value":38.17,"unit":"%"},{"name":"지방","value":32.72,"unit":"%"},{"name":"탄수화물","value":22.73,"unit":"%"},{"name":"회분","value":4.14,"unit":"%"},{"name":"수분","value":2.25,"unit":"%"}],"source":[3]}]

assays=[
 {"role":"literature","compound":"Fatty acid methyl esters (oleic, palmitic, palmitoleic, linoleic acid)","compound_ko":"지방산 조성(올레산·팔미트산·팔미톨레산·리놀레산)","part":"유충 동결건조 분말","content":"올레산 19.13, 팔미트산 12.52, 팔미톨레산 3.71, 리놀레산 2.08 g/100 g(건물); MUFA 57.7%, SFA 36.0%, PUFA 6.5%[3]","method":"GC-FID",
  "conditions":{"instrument":"Hewlett-Packard 6890 Series GC, FID","column":"SP-2560 (100 m × 0.25 mm, 0.2 μm)","mobile_phase":"운반기체 헬륨","gradient":"140 °C 5분 → 3 °C/min로 240 °C → 240 °C 10분","flow":"1 mL/min","temp":"주입구 260 °C, 검출기 260 °C","detection":"FID","injection":"1 μL, 분할비 50:1","sample_prep":"시료 약 3 g + THF 5 mL + 1 N KOH 에탄올 30 mL로 85 °C 90분 환류 비누화 → 산성화·에테르 추출 → 메탄올 40 mL·황산 0.5 mL로 3시간 환류 메틸에스터화 → 염화메틸렌에 녹임","standard":"Supelco FAME 표준 혼합물(머무름 시간 비교)","linearity":"","lod":"","loq":"","recovery":""},
  "rationale":"지방이 건물의 약 3분의 1이고 올레산이 가장 많아, 독성 연구에서도 올레산을 지표 성분(marker compound)으로 적었다(전문 확인)[2, 3]","source":[3,2],"url":"https://doi.org/10.3746/pnf.2012.17.4.310","source_kind":"paper"},
 {"role":"literature","compound":"Amino acids (acid hydrolysate)","compound_ko":"아미노산 조성","part":"탈지 유충 가루에서 얻은 물·염 추출 단백질 용액(1%)","content":"물 추출(WAD): 히스티딘 27.56, 발린 21.29, 글루탐산 64.75, 프롤린 42.77 mg/g, 필수아미노산 합 99.21 mg/g; 염 추출(SAD) 필수아미노산 합 71.99 mg/g[4]","method":"자동 아미노산 분석기(이온교환)",
  "conditions":{"instrument":"Hitachi L-8800 아미노산 분석기","column":"이온교환 수지 칼럼 (4.6 mm × 60 mm)","mobile_phase":"","gradient":"","flow":"","temp":"","detection":"","injection":"","sample_prep":"1% 추출 단백질 용액 0.5 mL + 6 M HCl 10 mL, 질소 봉입 앰플에서 105 °C 24시간 가수분해 → 40 °C 감압 건조 → 0.02 M HCl 3–5 mL에 녹여 0.20 μm 막 여과","standard":"Sigma-Aldrich 아미노산 표준품","linearity":"","lod":"","loq":"","recovery":""},
  "rationale":"단백질 원료로서의 품질(필수아미노산 지수)을 비교하는 데 쓰였다; 분말 자체가 아니라 추출 용액 값이다(전문 확인)[4]","source":[4],"url":"https://doi.org/10.5851/kosfa.2019.e56","source_kind":"paper"},
 {"role":"literature","compound":"Glycerophospholipids (PC, PE, PG, CL, PI, PS, PA, PIP)","compound_ko":"글리세로인지질(포스파티딜콜린·포스파티딜에탄올아민 등)","part":"1–3령 유충 전체(습중량)","content":"833개 분자종; PE 47.58%, PC 33.03%, PG 9.77%(총량 대비); 3령 PC 23,118.33 ± 602.74 μg/g; 카디오리핀 1령 1,198.09·3령 2,168.07 μg/g[10]","method":"UHPLC-ESI-MS/MS(비표적 지질체학, 내부표준 반정량)",
  "conditions":{"instrument":"Thermo Q-Exactive Plus 질량분석기","column":"Waters CSH C18 (1.7 µm, 2.1 mm × 100 mm)","mobile_phase":"A: 아세토나이트릴/물 6:4, B: 아세토나이트릴/아이소프로판올 1:9 (모두 0.1% 폼산·0.1 mM 폼산암모늄)","gradient":"B 30% 2분 유지 → 23분에 100% → 5%로 되돌려 10분","flow":"300 μL/min","temp":"이온원 300 °C, 모세관 350 °C","detection":"ESI 양·음이온, 분무 전압 3.0 kV, S-Lens RF 50%, MS1 m/z 200–1800","injection":"3 µL","sample_prep":"시료 30–33 mg에 내부표준(Splash Lipidomix) 20 μL, 물 200 µL·메탄올 240 µL로 4 °C 균질화 → MTBE 800 µL 추출, 초음파 20분 → 14,000×g 15분 원심, 상층 질소 건조 → 아이소프로판올/아세토나이트릴(9:1) 200 μL","standard":"Splash Lipidomix 내부표준, Lipid Search 4.0으로 동정","linearity":"","lod":"","loq":"","recovery":""},
  "rationale":"유충 지방을 기능성 지질 원료로 보려는 연구로 령별 인지질 축적을 비교했다; 원문 PE 3령 값(310.25 ± 738.07 μg/g)은 표기 오류로 보여 옮기지 않았다(전문 확인)[10]","source":[10],"url":"https://doi.org/10.3390/insects16121220","source_kind":"paper"},
 {"role":"literature","compound":"Phenolic acids (gallic, caffeic, syringic, phenylacetic acid)","compound_ko":"페놀산(갈산·카페인산·시링산·페닐아세트산)","part":"동결건조 유충 분말 95% 메탄올 추출액","content":"갈산 4.46 ± 0.15, 카페인산 3.52, 시링산 3.83 ± 0.18, 페닐아세트산 5.27 ± 0.01 μg/L; 바닐산·p-쿠마르산·벤조산 불검출[12]","method":"RP-HPLC-UV",
  "conditions":{"instrument":"Young Lin HPLC","column":"RP Spherisorb ODS (4.6 × 250 mm)","mobile_phase":"A: 20 mM 인산이수소칼륨 완충액(pH 2.92), B: 메탄올","gradient":"메탄올 3% → 65분에 100%","flow":"1.0 mL/min","temp":"","detection":"UV 220·280 nm","injection":"","sample_prep":"분말 10 g + 95% 메탄올 1 mL, 37 °C 수조에서 3시간 교반 후 Whatman No. 2 여과","standard":"7개 페놀산 표준품","linearity":"","lod":"","loq":"","recovery":""},
  "rationale":"곤충 분말의 항산화 성분 지표로 페놀산을 정량했다; 단위가 추출액 μg/L로만 제시되어 분말 중 함량으로 환산할 수 없다(전문 확인)[12]","source":[12],"url":"https://doi.org/10.5851/kosfa.2024.e17","source_kind":"paper"},
]

sources.sort(key=lambda x:x["n"])
d={"slug":"allomyrina-dichotoma","name_ko":"장수풍뎅이유충","name_en":"Japanese rhinoceros beetle larva","scientific_name":"Allomyrina dichotoma (Linnaeus, 1771) [현재 학명 Trypoxylus dichotomus]",
 "aliases":["장수풍뎅이","장수풍뎅이 유충","장수애","Trypoxylus dichotomus","Japanese rhinoceros beetle","Asian rhinoceros beetle","Korean rhinoceros beetle","rhinoceros beetle larva"],
 "sections":sections,"compounds":compounds,"markers":[],"nutrients":nutrients,"assays":assays,"production":[],"world":[],"gi":[],"orgs":[],"sources":sources}
p="/home/user/hfoodguide-wave3/docs/materials/allomyrina-dichotoma/dossier.json"
json.dump(d,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
for s in sections: print(s["key"],len(s["body"]))
