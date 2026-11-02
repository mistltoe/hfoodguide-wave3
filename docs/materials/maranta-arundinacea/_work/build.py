import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
A = "2026-11-02"
def pm(n, title, journal, year, pmid, doi, pmc=None, full=False):
    t = f"{title} — {journal} {year} (PMID {pmid}" + (f", {pmc}" if pmc else "") + (", 전문 확인)" if full else ", 초록 확인)")
    return {"n": n, "title": t, "url": f"https://doi.org/{doi}", "publisher": "PubMed", "accessed": A}
S = [
 {"n": 1, "title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 애로루트뿌리줄기·애로루트전분(Maranta arundinacea L.; Arrowroot), 사용가능, 사용가능부위: 뿌리줄기; 대조한 행: 칡전분·칡뿌리전분(Pueraria lobata (Wild.) Ohwi; East Asian arrow root) (로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json)", "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
 pm(2, "Characterization of arrowroot (Maranta arundinacea) starch as a potential starch source for the food industry", "Heliyon", 2023, "37810033", "10.1016/j.heliyon.2023.e20033", "PMC10559777", True),
 pm(3, "Rheological and textural studies of arrowroot (Maranta arundinacea) starch-sucrose-whey protein concentrate gels", "J Food Sci Technol", 2018, "30065406", "10.1007/s13197-018-3215-x", "PMC6046017"),
 pm(4, "Extraction and characterization of arrowroot (Maranta arundinaceae L.) starch and its application in edible films", "Carbohydr Polym", 2018, "29456010", "10.1016/j.carbpol.2018.01.024"),
 pm(5, "Physical and 3D Printing Properties of Arrowroot Starch Gels", "Foods", 2022, "35885383", "10.3390/foods11142140", "PMC9317205"),
 pm(6, "Starch grains reveal early root crop horticulture in the Panamanian tropical forest", "Nature", 2000, "11057665", "10.1038/35038055"),
 pm(7, "Starch grain evidence for the preceramic dispersals of maize and root crops into tropical dry and humid forests of Panama", "PNAS", 2007, "17360697", "10.1073/pnas.0611605104", "PMC1805539"),
 pm(8, "Gourd and squash artifacts yield starch grains of feasting foods from preceramic Peru", "PNAS", 2009, "19633184", "10.1073/pnas.0903322106", "PMC2726374"),
 pm(9, "Comparative physico-chemical profiles of Tugaksheeree (Curcuma angustifolia Roxb. and Maranta arundinacea Linn.)", "Ayu", 2013, "24696578", "10.4103/0974-8520.127723", "PMC3968704"),
 pm(10, "A comparative study of efficacy of Tugaksheeree [Curcuma angustifolia Roxb. and Maranta arundinacea Linn.] in management of Amlapitta", "Ayu", 2010, "22048544", "10.4103/0974-8520.82047", "PMC3202266"),
 pm(11, "Evaluation of acute toxicity and anti-ulcerogenic study of rhizome starch of two source plants of Tugaksheeree (Curcuma angustifolia Roxb. and Maranta arundinacea Linn.)", "Ayu", 2014, "26195908", "10.4103/0974-8520.159013", "PMC4492030", True),
 pm(12, "Gastrointestinal Tolerance to Maranta arundinacea (Arrowroot) Powder Added to Formula Feeds in Intensive Care Unit Patients: A Nonrandomized Controlled Quasi-experimental Trial", "Indian J Crit Care Med", 2026, "42147699", "10.5005/jp-journals-10071-25166", "PMC13177963", True),
 pm(13, "Dietary fibers of Canna edulis and Maranta arundinacea rhizomes ameliorate metabolic diseases and gut dysbiosis in mice fed a high-fat diet", "Res Pharm Sci", 2025, "41607423", "10.4103/RPS.RPS_129_23", "PMC12840878", True),
 pm(14, "Evaluation of immunostimulatory effect of the arrowroot (Maranta arundinacea. L) in vitro and in vivo", "Cytotechnology", 2011, "22038480", "10.1007/s10616-011-9403-4", "PMC3279578"),
 pm(15, "Exploring nutritional and bioactive properties of Maranta arundinacea L.: An unconventional food plant", "Food Res Int", 2025, "40382045", "10.1016/j.foodres.2025.116462"),
 pm(16, "Heat-moisture and acid treatments can increase levels of resistant starch in arrowroot starch without adversely affecting its prebiotic activity in human colon microbiota", "Food Funct", 2024, "38747641", "10.1039/d4fo00711e"),
 pm(17, "Arrowroot (Maranta arundinacea L.): evaluation of the technological and nutritional potential of the rhizome", "J Sci Food Agric", 2026, "42503012", "10.1002/jsfa.70918"),
 pm(18, "First Report of Meloidogyne enterolobii on Arrowroot in China", "Plant Dis", 2010, "30754277", "10.1094/PDIS-94-2-0271A"),
 pm(19, "Resolving the rapid plant radiation of early diverging lineages in the tropical Zingiberales: Pushing the limits of genomic data", "Mol Phylogenet Evol", 2018, "30063997", "10.1016/j.ympev.2018.07.020"),
 pm(20, "A near-complete genome assembly of Thalia dealbata Fraser (Marantaceae)", "Front Plant Sci", 2023, "37384358", "10.3389/fpls.2023.1183361", "PMC10298163"),
 pm(21, "Evaluation of rapid molecular diagnostics for differentiating medicinal Kaempferia species from its adulterants", "Plant Divers", 2019, "31453420", "10.1016/j.pld.2019.04.003", "PMC6704042"),
 pm(22, "Ethnomedicinal, Phytochemical and Nutra-pharmaceutical Potentials of Indian Arrowroot (Curcuma angustifolia Roxb)", "Comb Chem High Throughput Screen", 2023, "35611786", "10.2174/1386207325666220524142858"),
 pm(23, "Toxicity of shoti (Indian arrowroot: Curcuma zedoaria) for rats and chicks", "Br J Nutr", 1979, "420761", "10.1079/bjn19790012"),
 pm(24, "Evaluation of Antidiarrheal Activity of Methanolic Extract of Maranta arundinacea Linn. Leaves", "Adv Pharmacol Sci", 2015, "26346095", "10.1155/2015/257057", "PMC4543376"),
 pm(25, "Food-based solutions are a viable alternative to glucose-electrolyte solutions for oral hydration in acute diarrhoea--studies in a rat model of secretory diarrhoea", "Trans R Soc Trop Med Hyg", 1990, "2345922", "10.1016/0035-9203(90)90417-d"),
 pm(26, "Characteristics of low-fat mayonnaise using different modified arrowroot starches as fat replacer", "Int J Biol Macromol", 2020, "32135256", "10.1016/j.ijbiomac.2020.02.331"),
 pm(27, "Study of physicochemical, pasting, and emulsifying properties of single and dual-modified arrowroot (Maranta arundinacea) starches using autoclave-heating treatment and Octenylsuccinylation", "Food Chem X", 2025, "40538553", "10.1016/j.fochx.2025.102624", "PMC12177144"),
 pm(28, "Non-enzymatic preparation of porous arrowroot starch: pore forming mechanism, physicochemical properties, and adsorption performance for food and environmental applications", "Food Chem", 2026, "42330615", "10.1016/j.foodchem.2026.150114"),
 pm(29, "Physical and functional properties of arrowroot starch extrudates", "J Food Sci", 2009, "19323747", "10.1111/j.1750-3841.2008.01038.x"),
 pm(30, "Chemopreventive Effect of Dietary Maranta arundinacea L. Against DMBA-Induced Mammary Cancer in Sprague Dawley Rats Through the Regulation of Autophagy Expression", "Asian Pac J Cancer Prev", 2022, "35345372", "10.31557/APJCP.2022.23.3.985", "PMC9360966"),
 pm(31, "Chemical composition, mineral profile, and functional properties of Canna (Canna edulis) and Arrowroot (Maranta spp.) starches", "Plant Foods Hum Nutr", 2005, "16187013", "10.1007/s11130-005-6838-9"),
 pm(32, "Effect of glycerol plasticizer loading on the physical, mechanical, thermal, and barrier properties of arrowroot (Maranta arundinacea) starch biopolymers", "Sci Rep", 2021, "34230523", "10.1038/s41598-021-93094-y", "PMC8260728"),
]

sections = [
 {"key": "overview", "title": "개요", "body":
  "애로루트(Maranta arundinacea L.)는 마란타과(Marantaceae)의 여러해살이풀로, 땅속에서 옆으로 뻗는 뿌리줄기에서 전분을 얻는 열대 작물이다[2]. "
  "식품의약품안전처 「식품원료 목록」에는 '애로루트뿌리줄기'와 '애로루트전분'이 영명 Arrowroot로 올라 있고, 사용가능부위는 뿌리줄기, 상태는 '사용가능'이다[1]. "
  "같은 목록에서 영명이 'East Asian arrow root'인 칡전분·칡뿌리전분은 칡(Pueraria lobata)에서 얻는 다른 원료이므로 애로루트와 구별해야 한다[1].\n\n"
  "애로루트 전분은 흰색의 냄새 없는 가루로 밀가루와 색이 비슷하고, 점도가 높아 증점제로 쓸 만하며 글루텐이 없는 밀가루 대체 원료로 소개된다[2]. "
  "스리랑카 시료에서 아밀로스는 24.95 ± 1.49%로 '고아밀로스' 전분으로 분류되었다[2]. "
  "인도 아유르베다에서는 강황속 식물(Curcuma angustifolia) 전분과 함께 '투가크시리(Tugaksheeree)'라는 같은 약재 이름으로 쓰인다[9]. "
  "건강 효과 연구는 대부분 세포·동물 실험이고, 사람 연구는 작은 비무작위 시험에 그친다[12]."},
 {"key": "history", "title": "역사와 이용", "body":
  "파나마 아과둘세 바위그늘 유적의 갈돌에서는 약 7,000–5,000년 전(BP) 층에서 카사바·마·옥수수 전분과 함께 애로루트 전분 알갱이가 확인되어, 아메리카 대륙에서 뿌리작물을 가꾼 가장 이른 직접 증거로 보고되었다[6]. "
  "파나마 서부 치리키 지방의 무토기 시대 유적에서도 7,400–5,600 cal BP에 옥수수와 함께 애로루트 등 뿌리작물이 있었던 것으로 나타났다[7]. "
  "페루 중부 부에나비스타 유적(약 기원전 2200년)의 박·호박 그릇 잔류물에서는 잔치 음식으로 먹은 애로루트 전분이 나와, 페루에서 애로루트를 먹은 가장 이른 증거가 되었다[8].\n\n"
  "아시아에서는 스리랑카에서 '훌랑키리야(Hulankeeriya)' 또는 '애루카(Aerukka)'로 불리며 죽, 코코넛을 곁들인 삶은 뿌리줄기, 카레로 먹고 민간·아유르베다 요법에서 소화기 증상 완화에 쓴다[2]. "
  "남인도 마을에서는 급성 설사를 앓는 아이에게 애로루트를 끓여 식힌 물을 먹이는 관습이 조사되었다[25]. "
  "인도네시아에서는 탄수화물원과 기능성 식품으로 개발할 만한, 덜 이용되는 지역 작물로 소개된다[14]."},
 {"key": "biology", "title": "식물학적 특징", "body":
  "수확기의 뿌리줄기는 원통형으로 가지가 갈라지며(가축분지), 흰색이고 비늘잎으로 덮여 있다[2]. "
  "뿌리줄기는 섬유질이 많아 습식 추출 때 섬유와 함께 전분이 빠져나가며, 전분 함량은 식물의 나이에 따라 다르지만 약 20%이다[2]. "
  "생 뿌리줄기의 관능 평가에서는 섬유질 질감 때문에 선호도가 낮았다[17].\n\n"
  "전분 알갱이는 타원형(49.54%)·구형(28.98%)·불규칙 구형(21.48%)이 많고, 스리랑카 시료의 길이는 44.99 ± 1.27 μm, 너비는 31.44 ± 0.58 μm였다[2]. "
  "다른 연구에서는 구형과 길쭉한 알갱이가 섞여 평균 10.5 ± 2.5 μm로 보고되어, 시료와 측정 방법에 따라 크기 값이 크게 다르다[5]. "
  "X선 회절에서 A형 결정으로 보고된 연구가 있는 반면[2, 5], C형으로 보고된 연구도 있고 B형을 보고한 연구도 인용되어 결정형은 추출 방법·재배 조건·유전형에 따라 달라질 수 있다[2, 4]. "
  "지상부는 뿌리줄기보다 단백질과 섬유 함량이 높게 보고되었다[15]."},
 {"key": "related_species", "title": "근연종과 혼동 주의", "body":
  "'애로루트(arrowroot)'라는 이름은 여러 식물의 전분에 두루 붙어 혼동이 잦다[22, 23]. "
  "'인디언 애로루트'로 불리는 Curcuma angustifolia는 생강과(Zingiberaceae) 식물로 애로루트와 과가 다르며, 인도에서는 두 식물의 뿌리줄기 전분이 같은 약재 이름으로 쓰인다[9, 22]. "
  "역시 '인디언 애로루트'로 불린 Curcuma zedoaria(쇼티)는 단백질을 남긴 가루를 먹이의 320 g/kg으로 쥐에게 먹였을 때 6일 안에 모두 죽는 독성을 보였으므로, 이 자료를 애로루트에 적용해서는 안 된다[23].\n\n"
  "식약처 식품원료 목록의 칡전분(영명 East Asian arrow root)은 콩과 칡(Pueraria lobata)에서 얻는 것으로 애로루트전분과 다른 원료다[1]. "
  "카사바(Manihot esculenta)도 전분 작물이지만 애로루트와 다른 종이며, 고고학 연구에서도 카사바 전분과 애로루트 전분은 따로 판별되었다[6]. "
  "마란타과와 가장 가까운 과는 칸나과(Cannaceae)로, 두 과는 생강과·코스투스과와 함께 '생강 무리'를 이룬다[19]. "
  "칸나속 식용 칸나(Canna edulis) 전분은 애로루트 전분과 성분·호화 특성이 달라 비교 연구가 따로 있다[31]. "
  "인도 북동부에서는 마란타과 식물이 생강과 약초(Kaempferia속)로 잘못 판별되어 섞이는 일이 보고되었다[21]."},
 {"key": "cultivation", "title": "재배와 수확", "body":
  "애로루트는 열대·아열대 여러 지역에서 식용 전분을 얻으려고 재배된다[18]. "
  "스리랑카에서는 고구마·카사바 등과 함께 쓰이지만 공급이 적고 전분 추출에 시간이 많이 들어 덜 이용되는 뿌리작물로 남아 있다[2]. "
  "중국 하이난성 하이커우의 재배지에서는 2009년 뿌리혹선충(Meloidogyne enterolobii)이 뿌리에 혹을 만들어 생육 저하와 황화를 일으킨 사례가 보고되었다[18].\n\n"
  "한 연구는 '보통(common)' 품종과 '둥근 뿌리(round root)' 품종을 비교했는데, 두 품종의 아밀로스 함량과 팽윤력이 달랐다[3]. "
  "수확 뒤에는 무게가 줄고 효소 갈변이 일어나므로, 80 °C에서 4분 데친 뒤 냉동하면 효소가 불활성화되고 180일 동안 전분 함량과 미생물 품질이 유지되었다[17]. "
  "데치지 않은 생 뿌리줄기의 냉동 중 무게 손실은 50.6 g/kg, 데친 시료는 20.6 g/kg이었다[17]. "
  "재배 적온·강수량·재배 기간·단위면적당 수량 같은 재배 조건과 국내 재배 현황은 공식 자료로 확인하지 못함."},
 {"key": "processing", "title": "가공과 제품", "body":
  "전분은 습식 추출로 얻는다: 껍질을 벗긴 뿌리줄기를 물과 1:2로 갈아 천으로 거르고 하룻밤 가라앉힌 뒤 60 °C에서 8–10시간 말려 체로 친다[2]. "
  "이 방법의 수율은 12.23 ± 0.62%였고, 기계를 쓴 추출에서는 16–20%가 보고되었다[2]. "
  "전분은 호화 시작 75.02 °C, 정점 77.95 °C, 종료 82.43 °C로 측정되었고, 다른 시료에서는 호화 온도가 71.8 ± 0.2 °C였다[2, 5].\n\n"
  "애로루트 전분은 아밀레이스에 잘 분해되지 않는 성질이 있어 효소 대신 노화·용매 치환으로 다공성 전분을 만드는 방법이 연구되었다[28]. "
  "습열 처리(80 °C, 16시간)와 구연산 처리(0.6 M)는 저항전분을 늘리고 빨리 소화되는 전분을 줄였다[16]. "
  "옥테닐숙신산 처리와 고압가열 처리를 겹친 변성 전분은 유화 특성이 바뀌었고, 국내 연구에서는 변성 애로루트 전분을 저지방 마요네즈의 지방 대체제로 시험했다[26, 27]. "
  "압출 성형으로 팽화 과자 원료를 만들 수 있고, 압출물은 원료 전분보다 소화율이 다소 낮았다[29]. "
  "식품 외에 글리세롤을 넣은 생분해성 필름과 가식성 필름의 원료로도 연구된다[4, 32]."},
 {"key": "genetics", "title": "유전과 품종", "body":
  "애로루트는 생강목(Zingiberales) 마란타과에 속하며, 엽록체·핵 유전자 계통 분석에서 마란타과는 칸나과와 자매군을 이룬다[19]. "
  "마란타과에서 염색체 수준에 가까운 유전체가 처음 보고된 종은 습지 식물 탈리아(Thalia dealbata)로, 조립 크기 255.05 Mb에 의사염색체 8개, 단백질 암호 유전자 24,780개였다[20]. "
  "이 값은 다른 속의 것이므로 애로루트 유전체에 그대로 적용할 수 없다[20]. "
  "애로루트 자체의 핵 유전체 조립, 엽록체 유전체 전장 서열, 염색체 수는 이번 조사에서 확인하지 못함.\n\n"
  "품종 차이는 전분 성질에서 드러난다: '보통' 품종 전분의 아밀로스는 17.80%, '둥근 뿌리' 품종은 35.96%였고, 둥근 뿌리 품종 전분의 겔은 호화 온도가 더 높았다[3]. "
  "스리랑카 5개 주 16개 시료의 평균 아밀로스는 24.95%로, 앞선 연구들이 보고한 16–27% 범위 안에 있었다[2]. "
  "인도 북동부에서는 마란타과와 생강과 약초를 가리기 위해 여러 DNA 바코드 부위를 조합한 판별법이 개발되었다[21]."},
 {"key": "safety", "title": "안전성", "body":
  "애로루트는 식약처 식품원료 목록에서 뿌리줄기를 쓰는 '사용가능' 원료이며 별도 사용 조건은 부위 외에 적혀 있지 않다[1]. "
  "식약처 등 국내 공공기관의 애로루트 알레르기·잔류물·독성 성분 정보는 확인하지 못함. "
  "쥐 급성 독성 시험에서 애로루트 뿌리줄기 전분은 1회 최대 4,400 mg/kg까지 먹여도 7일 동안 죽거나 독성 증상을 보인 개체가 없었다[11].\n\n"
  "중환자실 비무작위 준실험 연구에서 경관 영양식에 애로루트 가루 100 g을 최대 5일 더했을 때 위장관 부작용은 관찰되지 않았고, 새 설사 발생은 8.8%로 대조군 26.7%보다 낮았으나 통계적으로 유의하지 않았다[12]. "
  "인도의 임상 연구에서는 애로루트 전분 4 g을 하루 세 번 30일 동안 먹은 환자에게서 부작용이 보고되지 않았다[10]. "
  "쥐 실험에서 뿌리줄기 섬유를 먹이의 10%로 더하면 고지방식 쥐의 혈당과 총콜레스테롤·중성지방이 낮아졌지만 체중 증가는 막지 못했다[13]. "
  "잎 메탄올 추출물은 쥐 설사 모델에서 200·400 mg/kg에 설사를 42.67%·57.75% 억제했지만, 이는 식품원료 부위(뿌리줄기)가 아닌 잎의 결과다[24]. "
  "면역 자극, 유방암 억제, 위궤양 억제 효과는 세포·동물 실험 결과일 뿐 사람에게서 확인된 것은 아니다[11, 14, 30]."},
]

compounds = [
 {"name": "Starch", "name_ko": "전분", "class": "다당류", "role": "marker", "part": "뿌리줄기",
  "content_text": "뿌리줄기의 약 20%(식물 나이에 따라 다름); 습식 추출 수율 12.23 ± 0.62%; 추출 전분 시료의 총전분 66.00 ± 0.48%[2]",
  "activity_ko": "애로루트전분의 주성분, 증점·겔 형성[2]", "source": [2]},
 {"name": "Amylose", "name_ko": "아밀로스", "class": "다당류(직쇄 α-1,4 글루칸)", "role": "marker", "part": "뿌리줄기 전분",
  "content_text": "24.95 ± 1.49%(스리랑카, 요오드 비색법)[2]; '보통' 품종 17.80%, '둥근 뿌리' 품종 35.96%[3]; 35%[4]",
  "activity_ko": "아밀로스가 많아 필름 형성·겔 강도에 유리[2]", "source": [2, 3, 4]},
 {"name": "Amylopectin", "name_ko": "아밀로펙틴", "class": "다당류(분지 글루칸)", "role": "nutrient", "part": "뿌리줄기 전분",
  "content_text": "아밀로스:아밀로펙틴 비 약 4:11[5]",
  "activity_ko": "전분 결정 구조(A형 등)를 이루는 성분[5]", "source": [5]},
 {"name": "Resistant starch", "name_ko": "저항전분", "class": "전분 분획", "role": "bioactive", "part": "뿌리줄기 전분(가공)",
  "content_text": "습열 처리(80 °C, 16시간)·구연산 처리(0.6 M)에서 함량이 가장 크게 늘었다(수치는 초록에 없음)[16]",
  "activity_ko": "사람 대장 미생물 배양에서 프리바이오틱 성질 유지[16]", "source": [16]},
 {"name": "Potassium", "name_ko": "칼륨", "class": "무기질", "role": "nutrient", "part": "뿌리줄기 전분",
  "content_text": "4312.95 mg/kg[2]", "activity_ko": "전분 시료에서 가장 많은 무기질[2]", "source": [2]},
 {"name": "Calcium", "name_ko": "칼슘", "class": "무기질", "role": "nutrient", "part": "뿌리줄기 전분",
  "content_text": "382.67 mg/kg[2]", "activity_ko": "무기질 영양 성분[2]", "source": [2]},
 {"name": "Sodium", "name_ko": "나트륨", "class": "무기질", "role": "nutrient", "part": "뿌리줄기 전분",
  "content_text": "52.6 mg/kg[2]", "activity_ko": "무기질 영양 성분[2]", "source": [2]},
 {"name": "Iron", "name_ko": "철", "class": "무기질", "role": "nutrient", "part": "뿌리줄기 전분",
  "content_text": "9.07 mg/kg[2]", "activity_ko": "무기질 영양 성분[2]", "source": [2]},
 {"name": "Zinc", "name_ko": "아연", "class": "무기질", "role": "nutrient", "part": "뿌리줄기 전분",
  "content_text": "2.59 mg/kg[2]", "activity_ko": "무기질 영양 성분[2]", "source": [2]},
 {"name": "Rutin", "name_ko": "루틴", "class": "플라보놀 배당체", "role": "bioactive", "part": "지상부·뿌리줄기 추출물",
  "content_text": "GNPS 분자 네트워킹으로 확인된 주요 성분(함량 미기재)[15]",
  "activity_ko": "ABTS·DPPH·FRAP 항산화 활성에 기여하는 것으로 제시[15]", "source": [15]},
 {"name": "Quercetin", "name_ko": "퀘르세틴 유도체", "class": "플라보놀", "role": "bioactive", "part": "지상부·뿌리줄기 추출물",
  "content_text": "GNPS로 확인된 주요 성분군(함량 미기재)[15]",
  "activity_ko": "항산화 활성에 기여하는 것으로 제시[15]", "source": [15]},
 {"name": "Kaempferol", "name_ko": "캠페롤 유도체", "class": "플라보놀", "role": "bioactive", "part": "지상부·뿌리줄기 추출물",
  "content_text": "GNPS로 확인된 주요 성분군(함량 미기재)[15]",
  "activity_ko": "항산화 활성에 기여하는 것으로 제시[15]", "source": [15]},
 {"name": "Dietary fiber", "name_ko": "식이섬유", "class": "비전분 다당류", "role": "bioactive", "part": "뿌리줄기(전분 추출 후 섬유 분획)",
  "content_text": "추출 전분의 조섬유 1.00 ± 0.09%[2]; 뿌리줄기 섬유 추출물을 쥐 먹이의 10%로 시험[13]",
  "activity_ko": "고지방식 쥐에서 혈당·총콜레스테롤·중성지방을 낮췄으나 체중 증가는 막지 못함(동물 실험)[13]", "source": [2, 13]},
]

nutrients = [
 {"form": "애로루트 전분(스리랑카 5개 주 16개 시료, 습식 추출·60 °C 건조)", "basis": "전분 시료 그대로(수분 10.87% 포함)",
  "items": [
   {"name": "수분", "value": 10.87, "unit": "%"},
   {"name": "회분", "value": 1.12, "unit": "%"},
   {"name": "조단백질", "value": 0.72, "unit": "%"},
   {"name": "조지방", "value": 0.26, "unit": "%"},
   {"name": "조섬유", "value": 1.00, "unit": "%"},
   {"name": "총전분", "value": 66.00, "unit": "%"},
   {"name": "아밀로스", "value": 24.95, "unit": "%"},
   {"name": "칼륨", "value": 4312.95, "unit": "mg/kg"},
   {"name": "칼슘", "value": 382.67, "unit": "mg/kg"},
   {"name": "나트륨", "value": 52.6, "unit": "mg/kg"},
   {"name": "철", "value": 9.07, "unit": "mg/kg"},
   {"name": "아연", "value": 2.59, "unit": "mg/kg"}],
  "source": [2]},
]

def cond(**k):
    base = {x: "" for x in ["instrument","column","mobile_phase","gradient","flow","temp","detection","injection","sample_prep","standard","linearity","lod","loq","recovery"]}
    base.update(k); return base
assays = [
 {"role": "literature", "compound": "Amylose", "compound_ko": "아밀로스", "part": "뿌리줄기 전분",
  "content": "24.95 ± 1.49%(스리랑카 16개 시료, 5개 주 평균)[2]", "method": "요오드 비색법(UV-Vis 분광광도계)",
  "conditions": cond(instrument="UV-Vis 분광광도계(JENWAY 6305)", detection="620 nm",
   sample_prep="전분 100 mg + 1 N NaOH 9 mL + 95% 에탄올 1 mL, 10분 가열 후 100 mL로 희석 → 이 액 5 mL + 증류수 50 mL + 요오드 용액 1.5 mL + 1 N 아세트산 1 mL, 100 mL로 맞춰 20분 방치",
   standard="순수 감자 아밀로스로 표준곡선"),
  "rationale": "아밀로스 함량이 애로루트 전분의 겔·필름 특성과 '고아밀로스' 분류를 정하는 핵심 지표로 쓰였다; 전문 확인, 직선성·검출한계·회수율은 원문에 없음[2].",
  "source": [2], "url": "https://doi.org/10.1016/j.heliyon.2023.e20033", "source_kind": "paper"},
 {"role": "literature", "compound": "Starch", "compound_ko": "총전분", "part": "뿌리줄기 전분",
  "content": "66.00 ± 0.48%[2]", "method": "산 완전가수분해 후 Lane–Eynon 환원당 적정",
  "conditions": cond(sample_prep="시료 2.5 g + 증류수 200 mL + 진한 HCl 20 mL, 환류 냉각기로 2.5시간 가열 → 식혀 5 N NaOH로 중화, 250 mL로 맞춤",
   detection="생성된 포도당을 Lane–Eynon 법으로 정량, 포도당 값 × 0.9 = 전분"),
  "rationale": "총전분은 추출 전분의 순도를 나타내는 지표로 쓰였고, 조섬유 함량과 음의 상관(−0.765)을 보였다; 전문 확인[2].",
  "source": [2], "url": "https://doi.org/10.1016/j.heliyon.2023.e20033", "source_kind": "paper"},
 {"role": "literature", "compound": "Potassium", "compound_ko": "칼륨(나트륨·칼슘·철·아연 동시 정량)", "part": "뿌리줄기 전분",
  "content": "K 4312.95, Ca 382.67, Na 52.6, Fe 9.07, Zn 2.59 mg/kg[2]", "method": "건식 회화 후 원자흡광분광법(AAS)",
  "conditions": cond(instrument="원자흡광분광광도계(GBC Avanta ver 1.33)",
   sample_prep="회분은 머플로 540 °C 회화; 무기질은 건식 회화한 재를 진한 HCl에 녹여 거른 뒤 증류수로 50 mL로 맞춤",
   standard="원소 분석용 표준액"),
  "rationale": "전분 시료의 무기질 구성을 보여 주는 정량값으로, 칼륨이 가장 많았다; 전문 확인, 회화 온도는 회분 정량 조건(540 °C)이며 무기질용 회화 온도는 따로 적혀 있지 않다[2].",
  "source": [2], "url": "https://doi.org/10.1016/j.heliyon.2023.e20033", "source_kind": "paper"},
]

d = {
 "slug": "maranta-arundinacea", "name_ko": "애로루트", "name_en": "Arrowroot",
 "scientific_name": "Maranta arundinacea L.",
 "aliases": ["애로루트뿌리줄기", "애로루트전분", "Arrowroot", "Hulankeeriya", "Aerukka"],
 "sections": sections, "compounds": compounds, "markers": [], "nutrients": nutrients,
 "assays": assays, "production": [], "world": [], "gi": [], "orgs": [], "sources": S,
}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in sections: print(s["key"], len(s["body"]))
