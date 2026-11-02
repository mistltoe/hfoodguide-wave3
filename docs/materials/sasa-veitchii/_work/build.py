import json, pathlib
A = "2026-11-02"
def pm(n, title, cite, pmid, doi, note, pmc=None):
    t = f"{title} — {cite} (PMID {pmid}" + (f", {pmc}" if pmc else "") + f", {note})"
    return {"n": n, "title": t, "url": f"https://doi.org/{doi}", "publisher": "PubMed", "accessed": A}
S = [
 {"n":1,"title":"식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 얼룩조릿대잎(Sasa veitchii Rehder; 이명 칸 '베이트키조릿대, 사라세니아 퍼푸레아'), 사용가능, 사용가능부위: 잎; 같은 목록의 조릿대(Sasa borealis)·제주조릿대(Sasa quelpaertensis)·갓대(Sasa chiisanensis)·섬조릿대(Sasa kurilensis)·난쟁이조릿대(Sasa nipponica)·신이대(Sasa coreana)·Sasa senanensis 행 대조 (로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json)","url":"https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020","publisher":"식품의약품안전처","accessed":"2026-10-13"},
 pm(2,"Silica accumulation in long-lived leaves of Sasa veitchii (Carrière) Rehder (Poaceae-Bambusoideae)","Ann Bot 2002;90(1):149-52",12125768,"10.1093/aob/mcf148","PMC4233852, 초록만 확인(전문 추출본 비어 있음)"),
 pm(3,"Silica deposition in relation to ageing of leaf tissues in Sasa veitchii (Carriere) Rehder (Poaceae: Bambusoideae)","Ann Bot 2004;93(3):235-48",14744706,"10.1093/aob/mch034","PMC4242195, 초록만 확인"),
 pm(4,"Relationships between photosynthetic activity and silica accumulation with ages of leaf in Sasa veitchii (Poaceae, Bambusoideae)","Ann Bot 2008;101(3):463-8",18045795,"10.1093/aob/mcm301","PMC2701821, 초록만 확인"),
 pm(5,"Female and male fitness consequences of clonal growth in a dwarf bamboo population with a high degree of clonal intermingling (Sasa veitchii var. hirsuta)","Ann Bot 2014;114(5):1035-41",25228034,"10.1093/aob/mcu176","PMC4171080, 초록만 확인; 변종 var. hirsuta 집단"),
 pm(6,"Genetic profiling of Sasa species by analysis of chloroplast intron between rbcL and ORF106 and partial ORF106 regions","Biol Pharm Bull 2007;30(8):1511-5",17666812,"10.1248/bpb.30.1511","초록만 확인; 조릿대속 16종 비교, 얼룩조릿대 포함 여부는 초록에 없음"),
 pm(7,"In vitro inhibition of the transcription factor NF-κB and cyclooxygenase by bamboo extracts (Phyllostachys nigra, Sasa veitchii)","Phytother Res 2014;28(2):224-30",23559516,"10.1002/ptr.4978","초록만 확인"),
 pm(8,"Kinetic study of Sasa veitchii extract as a radical scavenger and an antioxidant","J Food Sci 2012;77(11):C1211-7",23057490,"10.1111/j.1750-3841.2012.02943.x","초록만 확인; 시판 추출물"),
 pm(9,"Effect of Sasa veitchii extract on immunostimulating activity of β-glucan (SCG) from culinary-medicinal mushroom Sparassis crispa","Int J Med Mushrooms 2012;14(6):537-47",23510247,"10.1615/intjmedmushr.v14.i6.10","초록만 확인"),
 pm(10,"Specificity of the immunomodulating activity of Sasa veitchii (Japanese folk medicine Kumazasa) to fungal polysaccharides","Int J Med Mushrooms 2015;17(5):415-26",26082980,"10.1615/intjmedmushrooms.v17.i5.10","초록만 확인"),
 pm(11,"Immunochemical cross-reactivity of β-glucan in the medicinal plant, Sasa veitchii (Japanese folk medicine Kumazasa), and medicinal mushrooms","Int J Med Mushrooms 2016;18(3):191-202",27481152,"10.1615/IntJMedMushrooms.v18.i3.10","초록만 확인"),
 pm(12,"Lectin microarray analysis of isolated polysaccharides from Sasa veitchii","Biosci Biotechnol Biochem 2017;81(9)",28633601,"10.1080/09168451.2017.1340089","초록만 확인"),
 pm(13,"Anti pseudorabies virus activity of kumazasa extract (Sasa veitchii)","Biocontrol Sci 2010;15(4):123-8",21212504,"10.4265/bio.15.123","초록만 확인"),
 pm(14,"Kuma bamboo grass (Sasa veitchii) extracts exhibit protective effects against atypical Aeromonas salmonicida infection in goldfish (Carassius auratus)","Biocontrol Sci 2019;24(3):145",31527345,"10.4265/bio.24.145","초록만 확인"),
 pm(15,"Sasa veitchii extract suppresses carbon tetrachloride-induced hepato- and nephrotoxicity in mice","Environ Health Prev Med 2016;21(6):554-562",27738877,"10.1007/s12199-016-0581-8","PMC5112209, 초록만 확인(전문 추출본 비어 있음)"),
 pm(16,"Sasa veitchii extracts suppress acetaminophen-induced hepatotoxicity in mice","Environ Health Prev Med 2017;22(1):54",29165178,"10.1186/s12199-017-0662-3","전문 확인; 성분표는 추출본에 없음","PMC5664914"),
 pm(17,"Sasa veitchii extract reduces obesity-induced insulin resistance and hepatic steatosis in obese mice fed a high-fat diet","Nagoya J Med Sci 2017;79(3):279-",28878433,"10.18999/nagjms.79.3.279","PMC5577014, 초록만 확인"),
 pm(18,"Sasa veitchii extract protects against carbon tetrachloride-induced hepatic fibrosis in mice","Environ Health Prev Med 2018;23(1):49",30322375,"10.1186/s12199-018-0739-7","PMC6190662, 초록만 확인"),
 pm(19,"Sasa veitchii extract induces anticancer effects via inhibition of cyclin D1 expression in MCF-7 cells","Nagoya J Med Sci 2020;82(3):509-",33132435,"10.18999/nagjms.82.3.509","전문 확인","PMC7548257"),
 pm(20,"Wound-healing and skin-moisturizing effects of Sasa veitchii extract","Healthcare (Basel) 2021;9(6):761",34205315,"10.3390/healthcare9060761","전문 확인","PMC8235400"),
 pm(21,"Sasa veitchii extracts protect phenytoin-induced cell proliferation inhibition in human lip mesenchymal cells through modulation of miR-27b-5p","Biomed Res 2023;44(2):73-",37005285,"10.2220/biomedres.44.73","초록만 확인"),
 pm(22,"Protective effect of Sasa veitchii extract against all-trans-retinoic acid-induced inhibition of proliferation of cultured human palate cells","Nagoya J Med Sci 2024;86(2):223-",38962411,"10.18999/nagjms.86.2.223","PMC11219230, 초록만 확인"),
 pm(23,"Sasa veitchii extract mitigates mycophenolate mofetil-induced human palatal cell proliferation inhibition by downregulating miR-4680-3p","Plants (Basel) 2025;14(7):1150",40219219,"10.3390/plants14071150","전문 확인","PMC11991523"),
 pm(24,"Effects of Sasa veitchii extract on intestinal epithelial cells and gut microbiota","J Nat Med 2026",41703201,"10.1007/s11418-026-02016-7","초록만 확인"),
 pm(25,"Screening for natural medicines effective for the treatment of osteoporosis","J Nat Med 2019;73(1)",30392168,"10.1007/s11418-018-1258-y","초록만 확인; 식물 추출물 22종 선별 시험"),
 pm(26,"Search of new cytotoxic crude materials against human oral squamous cell carcinoma using 1H NMR-based metabolomics","Anticancer Res 2014;34(8):4117-20",25075037,"","초록만 확인; 식물 추출물 24종 비교"),
 pm(27,"Anti-human cytomegalovirus activity of constituents from Sasa albo-marginata (Kumazasa in Japan)","Antivir Chem Chemother 2008;19(3):125-32",19024629,"10.1177/095632020801900303","초록만 확인; 논문 학명은 Sasa albo-marginata"),
 pm(28,"Inhibitory effects of tricin derivative from Sasa albo-marginata on replication of human cytomegalovirus","Antiviral Res 2011;91(3):296-303",21745500,"10.1016/j.antiviral.2011.06.014","초록만 확인; 논문 학명은 Sasa albo-marginata"),
 {"n":29,"title":"Kew Plants of the World Online — Arundinaria albomarginata (Franch. & Sav.) Makino (IPNI 390224-1) 이명 처리. 이 주소는 허용 목록 밖이라 열지 못했고, 'Sasa albomarginata 는 Sasa veitchii 의 이명'이라는 내용은 WebSearch 검색 요약으로만 확인함","url":"https://powo.science.kew.org/taxon/urn:lsid:ipni.org:names:390224-1","publisher":"Royal Botanic Gardens, Kew (WebSearch 요약으로만 확인)","accessed":A},
 pm(30,"Sasa health exerts a protective effect on Her2/NeuN mammary tumorigenesis (Kumazasa = Sasa senanensis 알칼리 추출물)","Anticancer Res 2004;24(5A):2879-84",15517891,"","초록만 확인; 이 종이 아닌 Sasa senanensis 자료"),
]
S[25]["url"]="https://pubmed.ncbi.nlm.nih.gov/25075037/"
S[29]["url"]="https://pubmed.ncbi.nlm.nih.gov/15517891/"

sec = {}
sec["overview"] = ("얼룩조릿대(Sasa veitchii Rehder)는 벼과(Poaceae) 조릿대속의 키 작은 대나무로, 일본에서는 '쿠마자사(Kumazasa)'라 부르는 대나무 무리의 하나로 소개된다[19, 20]. "
 "식약처 「식품원료 목록」에는 '얼룩조릿대잎' 한 행이 '사용가능' 원료로 올라 있고, 사용 조건은 '사용가능부위 : 잎'이다[1]. "
 "즉 식품원료로 쓸 수 있는 부위는 잎뿐이며, 제한적사용 조건은 붙어 있지 않다[1]. "
 "같은 행의 대분류는 '식품원료(A코드)'이고, 건강기능식품 고시형 원료로 올라 있다는 근거는 찾지 못했다[1].\n\n"
 "잎은 늘푸른 잎으로 여러 해 살면서 규산(실리카)을 계속 쌓아, 오래된 잎에서는 건조 중량의 41% 까지 이른다[4]. "
 "일본에서는 잎 추출액이 피로 회복·입안 염증·치주 질환·입냄새 등에 쓰는 일반의약품으로 팔리고 있다[23]. "
 "연구는 주로 이 시판 알칼리 추출액이나 열수 추출물로 이루어졌고, 간 보호·항염·항바이러스·피부 상처 회복 효과가 보고되었지만 모두 세포·동물 실험이다[15, 16, 20, 13]. "
 "사람 대상 임상시험은 확인하지 못함.")
sec["history"] = ("얼룩조릿대 잎은 항균 작용 덕분에 예부터 음식을 보존하는 데 쓰였다고 소개된다[13, 19]. "
 "일본에서는 대나무 잎으로 초밥을 싸서 상하는 것을 막아 왔고, 잎은 위통·당뇨·고혈압·감염병에 쓰는 민간약이었다는 설명이 있다[16, 19]. "
 "2026년 논문은 이 잎 추출물을 궤양 억제·항염·항균 활성을 지닌 일본 전통 약용식물로 소개했다[24].\n\n"
 "2010년 무렵부터 일본 연구진은 열수 추출물의 고분자 다당 분획이 면역 반응과 바이러스 감염에 미치는 영향을 연구했다[9, 10, 12, 13]. "
 "2010년대 중반부터는 시판 알칼리 추출액을 쥐에게 먹여 사염화탄소·아세트아미노펜에 의한 간 손상과 고지방식 비만을 줄이는지 살핀 연구가 이어졌다[15, 16, 17, 18]. 시판 추출물의 라디칼 소거 속도 상수(활성 수산기 몰 기준)는 트롤록스와 비슷했다는 시험관 보고도 있다[8]. 식물 추출물 비교 선별 시험에서는 조골세포 분화 촉진·파골세포 분화 억제 활성을 함께 보인 추출물[25], 구강암 세포에 대한 종양 선택성 지수가 2.3 을 넘은 추출물의 하나로 꼽혔다[26]. "
 "2020년대에는 유방암 세포, 입술·입천장 배아 세포, 장내 미생물에 대한 연구로 넓어졌으나 모두 세포·동물 수준이다[19, 21, 22, 23, 24]. "
 "식약처 목록의 이명 칸에는 '베이트키조릿대'와 함께 '사라세니아 퍼푸레아'가 적혀 있는데, 이는 조릿대와 관계없는 다른 식물 이름으로 보이며 그렇게 적힌 근거는 확인하지 못함.")
sec["biology"] = ("얼룩조릿대는 클론 생장으로 퍼지며 무리를 이루는 키 작은 대나무다[5]. 잎은 늘푸르고 여러 해 산다[2, 4]. "
 "잎 수명은 2년으로 보고되었고, 잎은 평생 규산을 쌓아 건조 중량의 최대 41% 에 이른다[4]. "
 "규산은 봄·여름에 빠르게, 겨울에는 느리게 쌓였고, 저자들은 이것이 물 소비에 따라 수동적으로 쌓인다는 가설을 지지한다고 보았다[2].\n\n"
 "잎 조직별로 보면 엽육의 방추형 세포(fusoid cell)는 잎이 다 자란 뒤 나이에 따라 규산을 많이 쌓고, 엽록 세포는 거의 쌓지 않았다[3]. "
 "표피의 규산 세포는 잎이 자라는 동안에만 규산을 쌓았고, 기동 세포·잔털·가시털은 다 자란 뒤에도 촘촘히 계속 쌓았다[3]. "
 "규산 함량이 건조 중량의 25% 미만일 때는 광합성에 영향이 없었으나, 3년째 잎처럼 규산이 많으면 질소당 광합성 효율이 떨어졌다[4]. "
 "변종 var. hirsuta 의 한 집단에서는 10 × 10 m 구역 안에 유전적 개체(genet) 111개가 서로 섞여 자랐고, 일제히 꽃이 피는 성질을 지닌다[5]. "
 "이 집단에서 씨앗 생산은 유전적 개체의 크기에 비례해 늘었고 자가수분 비율은 낮았다[5].")
sec["related_species"] = ("식약처 「식품원료 목록」에는 조릿대속 원료가 여럿 있고, 종마다 지위와 쓸 수 있는 부위가 다르다[1]. "
 "얼룩조릿대와 신이대(Sasa coreana)는 잎, 제주조릿대(Sasa quelpaertensis)와 갓대(Sasa chiisanensis)는 순·잎, 섬조릿대(Sasa kurilensis)는 순, 난쟁이조릿대(Sasa nipponica)는 순·씨앗이 사용가능 부위다[1]. "
 "조릿대(Sasa borealis)는 '제한적사용'으로 잎을 침출차로만 쓸 수 있고, Sasa senanensis 는 싹·씨앗만 사용가능이며 잎 행은 '사용불가'로 올라 있다[1]. "
 "따라서 다른 조릿대 종의 성분·효능 자료를 얼룩조릿대에 그대로 옮겨 쓰면 안 된다[1].\n\n"
 "일본어 '쿠마자사'는 한 종이 아니라 여러 조릿대 종을 함께 부르는 이름이다[19, 20]. "
 "쿠마자사 약재의 기원 식물로 Sasa palmata·S. senanensis·S. yahikoensis·S. kurilensis 가 거론되며 형태로는 구별이 어렵다는 보고가 있다[6]. "
 "유방 종양 동물 실험에 쓰인 알칼리 추출물은 S. senanensis 잎으로 만든 것이어서 얼룩조릿대 자료가 아니다[30]. "
 "일부 논문은 'Sasa albo-marginata'라는 학명으로 쿠마자사를 다루며 트리신 등 성분을 분리했다[27, 28]. "
 "이 학명이 얼룩조릿대의 이명이라는 정보는 검색 요약으로만 보았고 식물 분류 데이터베이스 원문은 열지 못했으므로, 이 논문들의 결과는 따로 표시해 둔다[29].")
sec["cultivation"] = ("얼룩조릿대는 일본의 전통 약용식물로 소개되며, 연구에 쓰인 원료는 대부분 일본에서 만든 시판 추출물이다[19, 23, 24]. "
 "시판 알칼리 추출액은 생잎을 잘게 잘라 원료로 쓴다고 적혀 있다[23]. "
 "잎은 여러 해 살면서 규산을 계속 쌓으므로, 같은 잎이라도 나이와 채취 계절에 따라 무기질 조성이 크게 달라질 수 있다[2, 4]. "
 "규산은 봄·여름에 빠르게 쌓이고 겨울에는 느리게 쌓였다[2].\n\n"
 "변종 집단 연구에서는 클론 생장으로 퍼진 여러 유전적 개체가 서로 섞여 자랐다[5]. "
 "이런 성질 때문에 한 무리 안에도 유전적으로 다른 개체가 함께 있을 수 있다[5]. "
 "재배 방법·수확 시기·수량에 관한 공식 자료는 확인하지 못함. "
 "국내 재배 면적·생산량은 통계청·농림축산식품부 특용작물 통계에서 확인하지 못함. "
 "국내에서 식품원료로 유통되는 얼룩조릿대 잎의 원산지 정보도 확인하지 못함.")
sec["processing"] = ("일본의 시판 일반의약품 추출액은 생잎을 잘게 잘라 황산구리를 넣은 끓는 물에 담가 엽록소의 마그네슘을 구리로 바꾸고, 15% 수산화나트륨 용액에서 80분 끓여 세포벽을 분해해 만든다[23]. "
 "이어 염산을 넣어 생긴 침전을 원심분리로 모은 뒤 수산화나트륨으로 pH 7 에 맞춰 녹인다[23]. "
 "제조사 자료로는 추출액 1 mL 가 잎 2.82 g 에 해당하며, 120 mL 를 동결건조하면 가루 9.44 g 이 나왔다[23]. "
 "이 추출액의 주성분은 제조사 자료상 구리클로로필린나트륨 0.25% 이며, 이는 잎에 원래 있는 성분이 아니라 가공 중 만들어진 것이다[19, 23].\n\n"
 "이와 별도로 잎의 열수 추출 농축액이 피부 연구에 쓰였고, 1% 용액을 쥐 피부에 바르는 방식이었다[20]. "
 "열수 추출물의 수용성 부분을 메탄올로 침전시킨 고분자 분획은 면역 연구에 쓰였다[9, 10]. "
 "추출 방법에 따라 성분이 크게 다르므로, 알칼리 추출액 결과를 차로 우린 잎에 그대로 적용할 수는 없다[19, 20, 23]. "
 "건강기능식품 고시형 원료가 아니어서 식약처 「식품 등의 생산실적」의 해당 품목 통계는 확인하지 못함.")
sec["genetics"] = ("얼룩조릿대 자체의 엽록체 유전체 전체 서열이나 핵 유전체 해독 결과는 확인하지 못함. "
 "변종 var. hirsuta 집단 연구에서는 핵 마이크로새틀라이트 11개 좌위의 다좌위 유전자형으로 유전적 개체를 구별했다[5]. "
 "이 분석에서 10 × 10 m 구역에 111개 유전적 개체가 섞여 있었고, 부계 분석으로 자가수분율과 수분 성공도를 추정했다[5].\n\n"
 "조릿대속 16종 34개 표본의 엽록체 DNA(rbcL–ORF106 사이 인트론과 ORF106 일부)를 비교한 연구에서는 분석 길이가 759–821 bp 였다[6]. "
 "이 구간에서 염기 치환 9곳과 31 bp 반복 단위 1–3개가 관찰되었지만 종마다 고유한 배열은 찾지 못했다[6]. "
 "같은 종의 표본끼리 배열이 다르기도 하고 다른 종끼리 같기도 해서, 엽록체 DNA 한 구간만으로는 쿠마자사 기원 종을 가리기 어렵다[6]. "
 "이 연구에 얼룩조릿대가 포함되었는지는 초록에서 확인하지 못함.")
sec["safety"] = ("얼룩조릿대는 식약처 「식품원료 목록」에서 잎만 쓸 수 있는 '사용가능' 원료이며, 제한적사용 조건은 붙어 있지 않다[1]. "
 "건강기능식품 고시형 원료로 확인되지 않아 고시된 섭취 시 주의사항도 찾지 못했다[1]. "
 "알레르기·잔류 농약·독성 성분에 관한 공공기관 안전 정보는 확인하지 못함.\n\n"
 "동물 실험에서는 쥐에게 시판 추출액 0.2 mL 를 하루 한 번 1주일, 또는 0.1 mL 를 하루 한 번 8주 먹였다[16, 18]. 이 연구들에서 별도의 독성 시험 결과는 확인하지 못함. "
 "입천장 세포 연구의 저자들은 일본에서 일반의약품으로 승인되어 있지만 임신 기간의 독성은 따로 평가해야 한다고 적었다[23]. "
 "시판 알칼리 추출액에는 가공 중 생긴 구리클로로필린나트륨이 0.25% 들어 있어, 잎을 우린 차와 성분이 다르다[19, 23]. "
 "사람 혈청의 β-글루칸 항체가 잎 추출물과 강하게 교차 반응했다는 보고가 있어, 면역 반응에 미치는 영향은 더 확인이 필요하다[11]. "
 "오래된 잎은 규산이 건조 중량의 40% 안팎까지 쌓일 수 있다[4]. "
 "사람에서의 안전성·적정 섭취량 자료는 확인하지 못함.")
titles = {"overview":"한눈에 보기","history":"이름과 이용의 역사","biology":"식물학적 특징","related_species":"근연종과 혼동 주의","cultivation":"자생지·재배와 채취","processing":"가공과 이용","genetics":"유전체와 분류","safety":"안전성과 주의"}
sections=[{"key":k,"title":titles[k],"body":sec[k]} for k in titles]

def c(name,ko,cls,role,part,ct,act,src): return {"name":name,"name_ko":ko,"class":cls,"role":role,"part":part,"content_text":ct,"activity_ko":act,"source":src}
compounds=[
 c("Silicon dioxide","규산(실리카)","무기질","nutrient","잎","잎 건조 중량의 최대 41%(잎 나이에 따라 증가)[4]; 25% 미만에서는 광합성에 영향 없음[4]","잎 조직(방추형 세포·기동 세포·털 등)에 쌓임(식물 생리)[3]",[2,3,4]),
 c("Sodium copper chlorophyllin","구리클로로필린나트륨","클로로필 유도체(가공 생성물)","marker","잎 알칼리 추출액(시판 일반의약품)","추출액의 0.25%(제조사 자료)[19, 23]; 황산구리 처리로 엽록소의 마그네슘을 구리로 치환해 생김[23]","MCF-7 유방암 세포 IC50 715 μg/mL 로 추출물(7.72 μg/mL)보다 훨씬 약함(세포 실험)[19]; 입천장 세포 보호 효과 없음(세포 실험)[23]",[19,23]),
 c("Chlorophyll","엽록소","테트라피롤 색소","bioactive","잎","함량은 확인하지 못함; 잎에 들어 있는 성분으로 소개[19, 20]","",[19,20]),
 c("Lignin","리그닌","페닐프로파노이드 중합체","bioactive","잎","함량은 확인하지 못함; 잎 성분으로 소개[19, 20]","",[19,20]),
 c("Polysaccharides","다당류(열수 추출물 고분자 분획)","다당","bioactive","잎","함량은 확인하지 못함; 열수 추출물의 수용성 메탄올 침전 분획(BWMP)으로 분리[9, 10]","올리고만노스·푸코스·갈락토스 결합 렉틴과 높은 반응성, 항인플루엔자 활성 분획[12]; 비장 세포의 IFN-γ 생성 억제(세포 실험)[9, 10]; 가성광견병 바이러스 플라크 형성 억제(세포 실험)[13]",[9,10,12,13]),
 c("Fatty acids","지방산류","지방산","bioactive","잎 추출물","종류·함량은 초록에 없음; 추출물에 여러 지방산이 들어 있다고만 보고[14]","Aeromonas 9개 균주에 항균, 감염 금붕어 생존 회복(375–750 μg/mL, 동물 실험)[14]",[14]),
 c("Tricin","트리신","플라본","bioactive","잎 열수 추출물(논문 학명 Sasa albo-marginata)","함량 보고 없음; 'Sasa albo-marginata' 열수 추출물에서 분리[27] — 얼룩조릿대 이명 여부는 검색 요약으로만 확인[29]","사람 거대세포바이러스 플라크 억제 EC50 0.17 μg/mL(세포 실험)[27]; COX-2 발현 억제와 관련(세포 실험)[28]",[27,28,29]),
 c("p-Coumaric acid","p-쿠마르산","히드록시신남산(페놀산)","bioactive","잎 열수 추출물(논문 학명 Sasa albo-marginata)","함량 보고 없음; 'Sasa albo-marginata' 열수 추출물에서 분리한 다섯 성분 중 하나[27]","",[27]),
 c("Vanillin","바닐린","페놀 알데히드","bioactive","잎 열수 추출물(논문 학명 Sasa albo-marginata)","함량 보고 없음; 분리 성분(3-hydroxy-4-methoxybenzaldehyde 로 표기)[27]","",[27]),
 c("4-Hydroxybenzaldehyde","p-히드록시벤즈알데히드","페놀 알데히드","bioactive","잎 열수 추출물(논문 학명 Sasa albo-marginata)","함량 보고 없음; 분리 성분[27]","",[27]),
 c("3-Hydroxypyridine","3-히드록시피리딘","피리딘 유도체","bioactive","잎 열수 추출물(논문 학명 Sasa albo-marginata)","함량 보고 없음; 분리 성분[27]","",[27]),
]
def cond(**kw):
    base={k:"" for k in ["instrument","column","mobile_phase","gradient","flow","temp","detection","injection","sample_prep","standard","linearity","lod","loq","recovery"]}
    base.update(kw); return base
assays=[
 {"role":"literature","compound":"Sodium copper chlorophyllin","compound_ko":"구리클로로필린나트륨","part":"잎 알칼리 추출액(시판 일반의약품, 동결건조 가루)","content":"추출액의 0.25%(제조사 자료; 논문이 직접 정량한 값 아님)[23]","method":"UV-Vis 흡수 스펙트럼 비교(정성)","conditions":cond(instrument="Shimadzu UV-2600i UV-Vis 분광광도계(본문 제목은 '적외선 흡수 분광'으로 적힘)",detection="구리클로로필린나트륨 흡수 봉우리 약 400 nm; 추출물에서는 250–300 nm 넓은 봉우리도 관찰",sample_prep="추출액 120 mL 를 동결건조해 가루 9.44 g; 측정 농도 추출물 0.04 mg/mL, 표준 0.02 mg/mL",standard="구리클로로필린나트륨(시약 회사 구입)"),"rationale":"제조사가 추출액의 주성분으로 밝힌 성분이어서 표준품과 스펙트럼을 비교해 존재를 확인했다; 정량·검량선·검출한계는 보고되지 않았다[23]","source":[23],"url":"https://doi.org/10.3390/plants14071150","source_kind":"paper"},
 {"role":"literature","compound":"Silicon dioxide","compound_ko":"규산(실리카)","part":"잎(나이별)","content":"잎 건조 중량의 최대 41%[4]","method":"몰리브덴 청(molybdenum blue) 비색법","conditions":cond(),"rationale":"이 종의 오래 사는 잎에서 가장 많이 쌓이는 무기 성분으로, 잎 나이·계절에 따른 축적을 추적하는 지표로 쓰였다; 초록만 확인해 측정 조건은 전문 확인 못함[2, 4]","source":[2,4],"url":"https://doi.org/10.1093/aob/mcf148","source_kind":"paper"},
 {"role":"literature","compound":"Phenolic compounds (leaf extract profile)","compound_ko":"잎 추출물 페놀 성분 프로필","part":"잎","content":"정량값은 초록에 없음[7]","method":"HPLC-DAD, LC-MS/MS","conditions":cond(),"rationale":"항염 활성(COX-2 선택 억제)을 비교하려고 잎 추출물의 성분을 HPLC-DAD·LC-MS/MS 로 특성화했다; 초록만 확인했고 전문 확인 못함[7]","source":[7],"url":"https://doi.org/10.1002/ptr.4978","source_kind":"paper"},
]
d={"slug":"sasa-veitchii","name_ko":"얼룩조릿대","name_en":"Kuma bamboo grass","scientific_name":"Sasa veitchii (Carrière) Rehder",
 "aliases":["얼룩조릿대잎","베이트키조릿대","Kuma bamboo grass","Kumazasa(쿠마자사 — 여러 조릿대 종을 함께 부르는 일본 이름)"],
 "sections":sections,"compounds":compounds,"markers":[],"nutrients":[],"assays":assays,"production":[],"world":[],"gi":[],"orgs":[],"sources":S}
p=pathlib.Path(__file__).resolve().parent.parent/"dossier.json"
p.write_text(json.dumps(d,ensure_ascii=False,indent=1),encoding="utf-8")
for s in sections: print(s["key"],len(s["body"]))
