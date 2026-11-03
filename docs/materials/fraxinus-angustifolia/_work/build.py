import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
A = "2026-10-13"
def pm(pmid, title, journal, year):
    return {"title": f"{title} ({journal}, {year}; PMID {pmid})", "url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/", "publisher": f"{journal} / PubMed", "accessed": A}
S = [
 {"title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 앙구스티폴리아물푸레열매·물푸레나무나무껍질 행", "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
 pm("26690403", "Targeted and Untargeted Metabolomics to Explore the Bioavailability of the Secoiridoids from a Seed/Fruit Extract (Fraxinus angustifolia Vahl) in Human Healthy Volunteers: A Preliminary Study (전문 PMC6332458)", "Molecules", 2015),
 pm("30884667", "Fixed oil from seeds of narrow-leaved ash (F. angustifolia subsp. angustifolia): Chemical profile, antioxidant and antiproliferative activities", "Food Research International", 2019),
 pm("19723572", "Acute effects of Fraxinus excelsior L. seed extract on postprandial glycemia and insulin secretion on healthy volunteers", "Journal of Ethnopharmacology", 2009),
 pm("24877717", "A Fraxinus excelsior L. seeds/fruits extract benefits glucose homeostasis and adiposity related markers in elderly overweight/obese subjects", "Phytomedicine", 2014),
 pm("23201448", "Safety evaluation and nutritional composition of a Fraxinus excelsior seed extract", "Food and Chemical Toxicology", 2012),
 pm("21036576", "Fraxinus excelsior seed extract limits weight gains and hyperglycemia in high-fat diet-induced obese mice", "Phytomedicine", 2010),
 pm("20000781", "Iridoids from Fraxinus excelsior with adipocyte differentiation-inhibitory and PPARalpha activation activity", "Journal of Natural Products", 2010),
 pm("24573510", "Action of an extract from the seeds of Fraxinus excelsior L. on metabolic disorders in hypertensive and obese animal models", "Food & Function", 2014),
 pm("40003572", "Environmental Factors Determining the Chorology of Fraxinus angustifolia in the Region of Murcia (Southeastern Spain) (전문 PMC11856548)", "Life (Basel)", 2025),
 pm("22905171", "Environmental heterogeneity explains the genetic structure of Continental and Mediterranean populations of Fraxinus angustifolia Vahl", "PLoS One", 2012),
 pm("23445208", "Identifying refugia from climate change using coupled ecological and genetic data in a transitional Mediterranean-temperate tree species", "Molecular Ecology", 2013),
 pm("16780430", "Chloroplast DNA phylogeography of European ashes, Fraxinus sp. (Oleaceae): roles of hybridization and life history traits", "Molecular Ecology", 2006),
 pm("16968268", "Differential patterns of morphological and molecular hybridization between Fraxinus excelsior L. and Fraxinus angustifolia Vahl (Oleaceae) in eastern and western France", "Molecular Ecology", 2006),
 pm("17107611", "Assortative mating and differential male mating success in an ash hybrid zone population", "BMC Evolutionary Biology", 2006),
 pm("11918794", "Maternal inheritance of a chloroplast microsatellite marker in controlled hybrids between Fraxinus excelsior and Fraxinus angustifolia", "Molecular Ecology", 2002),
 pm("24795215", "The phylogeography of Eurasian Fraxinus species reveals ancient transcontinental reticulation", "Molecular Phylogenetics and Evolution", 2014),
 pm("32824084", "Genetic Distinctiveness Highlights the Conservation Value of a Sicilian Manna Ash Germplasm Collection Assigned to Fraxinus angustifolia (Oleaceae)", "Plants (Basel)", 2020),
 pm("33143282", "Anti-Proliferative Activity of A Hydrophilic Extract of Manna from Fraxinus angustifolia Vahl through Mitochondrial Pathway-Mediated Apoptosis and Cell Cycle Arrest in Human Colon Cancer Cells", "Molecules", 2020),
 pm("31635261", "Phenolic Composition of Hydrophilic Extract of Manna from Sicilian Fraxinus angustifolia Vahl and its Reducing, Antioxidant and Anti-Inflammatory Activity in Vitro", "Antioxidants (Basel)", 2019),
 pm("41242505", "The multifaceted properties of manna in skin wound healing include the enhancement of cell motility and differentiation, and antioxidant and anti-inflammatory actions", "Fitoterapia", 2025),
 pm("35306516", "European-wide forest monitoring substantiate the neccessity for a joint conservation strategy to rescue European ash species (Fraxinus spp.)", "Scientific Reports", 2022),
 pm("24118686", "Hymenoscyphus pseudoalbidus, the causal agent of European ash dieback", "Molecular Plant Pathology", 2013),
 pm("27529695", "Comparing the Sexual Reproductive Success of Two Exotic Trees Invading Spanish Riparian Forests vs. a Native Reference", "PLoS One", 2016),
 pm("21842417", "Establishment success of coexisting native and exotic trees under an experimental gradient of irradiance and soil moisture", "Environmental Management", 2011),
 pm("29789963", "Experimental arid land afforestation in Central Anatolia, Turkey", "Environmental Monitoring and Assessment", 2018),
 pm("32298276", "Antimutagenic, antigenotoxic and antiproliferative activities of Fraxinus angustifolia Vahl. leaves and stem bark extracts and their phytochemical composition", "PLoS One", 2020),
 pm("31410081", "Identification of bioactive compounds from Fraxinus angustifolia extracts with anti-NADH oxidase activity of bovine milk xanthine oxidoreductase", "Turkish Journal of Biology", 2019),
 pm("42599635", "Phytochemical Profiling, Biological Evaluation, and Molecular Insights Into the Urease Inhibitory Potential of Fraxinus angustifolia Crude Extract and Fractions", "Chemistry & Biodiversity", 2026),
 pm("32645433", "Neuroprotective effects of Fraxinus angustifolia Vahl. bark extract against Alzheimer's disease", "Journal of Chemical Neuroanatomy", 2020),
 pm("4053334", "Allergy in the Mediterranean area. III: Cross reactivity among Oleaceae pollens", "Clinical Allergy", 1985),
 pm("31440969", "Lead content in soils and native plants near an abandoned mine in a protected area of south-western Spain", "Environmental Science and Pollution Research", 2019),
 pm("42918911", "Comprehensive insight into the anti-dyslipidemic and pancreatic lipase inhibition activities of Clematis flammula L. and Fraxinus angustifolia Vahl. extracts using two animal models", "Journal of Molecular Histology", 2026),
]
for i, s in enumerate(S, 1):
    s["n"] = i

sections = [
 {"key": "overview", "title": "한눈에 보기", "body":
  "앙구스티폴리아물푸레(Fraxinus angustifolia Vahl)는 물푸레나무과(Oleaceae) 물푸레나무속의 나무로, 영어로는 narrow-leaved ash(좁은잎물푸레)라 부르며 남유럽과 북아프리카에 자란다[1, 10]. 식약처 「식품원료 목록」에는 원료명 '앙구스티폴리아물푸레열매'(영어명 Narrow-leaved ash)로 한 행이 올라 있고, 상태는 '사용가능', 사용 조건은 '사용가능부위 : 열매'다[1]. 따라서 이 목록으로 식품에 쓸 수 있는 부위는 열매뿐이며, 잎·나무껍질·수액(만나)은 이 행에 포함되지 않는다[1].\n\n"
  "열매(씨앗 포함) 추출물에는 세코이리도이드 배당체인 누제니드와 GL3가 주성분으로 들어 있고, 모로코산 열매로 만든 추출물에서 두 성분이 합계 10.67%로 정량되었다[2]. 씨앗 기름은 올레산 45.5%, 리놀레산 50.0%로 이루어져 있다[3]. 이 종의 약리 연구 상당수는 잎과 나무껍질 추출물로 한 세포·동물 실험이어서, 식품원료인 열매의 효과로 옮겨 읽으면 안 된다[27, 28, 29, 30]."},
 {"key": "history", "title": "이용의 역사", "body":
  "알제리 등 지중해 지역에서는 이 나무의 잎과 나무껍질을 염증성 질환과 위장 질환 등에 민간약으로 써 왔다고 보고된다[28, 29, 33]. 이 종은 오래전부터 만나(manna, 줄기와 가지에서 스며 나와 굳은 수액)를 얻는 데 쓰였고, 씨앗은 기름이 많아 식품·화장품 원료로 검토되고 있다[3]. 만나는 만니톨을 함유해 순한 완하제로 의약에 쓰여 왔다[19].\n\n"
  "이탈리아 시칠리아의 만나 생산용 나무는 흔히 만나물푸레(F. ornus)로 여겨졌으나, 유전 분석 결과 현재 만나 생산에 쓰이는 재래 자원은 앙구스티폴리아물푸레로 판정되었다[18]. 스페인 무르시아 지역에는 1751년 기록에 물푸레나무가 많았다고 적혀 있으나 지금은 크게 줄어 지역 보호종으로 지정되어 있다[10]. 열매(씨앗) 추출물은 2000년대 후반부터 혈당 조절 소재로 연구되었는데, 이 연구들은 처음에 서양물푸레(F. excelsior) 씨앗 추출물이라는 이름으로 발표되었다[4, 5, 6]. 2015년 논문은 같은 공급사 원료를 DNA로 다시 감정해 모로코 중부에서 채집한 앙구스티폴리아물푸레 열매라고 밝혔다[2]."},
 {"key": "biology", "title": "생물학적 특징", "body":
  "앙구스티폴리아물푸레는 남유럽과 북서아프리카에 분포하고, 이베리아반도에서는 지중해성 기후 지역 대부분에 강가 숲·하천변 숲을 이루며 자란다[10]. 지하수에 기대는 성질이 강해 건조한 지역에서는 하천 바닥과 샘 주변에만 남아 있으며, 스페인 무르시아 조사에서는 670그루 가운데 475그루가 자연 발생 개체였다[10]. 토양 종류는 가리지 않으나 깊은 충적토를 좋아하고, 물에 잠기는 것을 잘 견디며 겨울 추위와 여름 더위에도 강하다고 인용된다[10].\n\n"
  "꽃가루는 바람으로 옮겨지며(풍매), 서양물푸레보다 일찍 꽃이 피고 두 종 사이의 잡종은 그 중간 시기에 꽃이 핀다[11, 15]. 스페인 하천림 조사에서 이 종은 씨앗을 많이 떨어뜨렸고, 떨어진 씨앗의 최대 절반가량이 동물에게 옮겨지거나 먹혔다[24]. 파종 실험에서는 그늘보다 밝은 조건에서 발아·정착이 잘 되었다[25]. 열매·씨앗의 크기와 모양을 이 종에 대해 정리한 공식 식물지 자료는 이번에 확인하지 못함[1]."},
 {"key": "related_species", "title": "근연종과 혼동 주의", "body":
  "같은 속의 서양물푸레(F. excelsior)는 앙구스티폴리아물푸레와 유전적으로 매우 가깝고, 프랑스 루아르 지역 등에서 두 종이 자연 잡종을 이룬다[14, 15]. 두 종은 엽록체 DNA 유형을 넓게 공유해 엽록체 표지만으로는 구별이 어렵다[13, 16]. 이 때문에 '서양물푸레 씨앗 추출물'로 발표된 혈당 연구의 원료가 나중에 DNA 감정으로 앙구스티폴리아물푸레 열매로 다시 판정된 사례가 있다[2, 4].\n\n"
  "만나물푸레(F. ornus)는 엽록체 유형을 다른 두 유럽 종과 하나도 공유하지 않는 별개의 종이며, 만나 생산 나무로 알려졌지만 시칠리아 생산 자원은 앙구스티폴리아물푸레였다[13, 18]. 국내 자생 물푸레나무(F. rhynchophylla)는 식약처 목록에 '물푸레나무나무껍질'로 올라 있으나 상태가 '사용불가'여서, 앙구스티폴리아물푸레열매와 지위가 다르다[1]."},
 {"key": "cultivation", "title": "재배와 산지", "body":
  "이 종은 식약처 식품원료 목록에 올라 있으나, 국내에서 재배하거나 열매를 생산한다는 공식 통계는 확인하지 못함[1]. 원산지에서는 하천변·습한 사면에 자라는 자생림이 주이고, 스페인 무르시아에서는 일부 개체가 조림으로 심어진 뒤 자연화했다[10]. 튀르키예 중부 아나톨리아의 건조지 조림 시험에서는 5년 동안 활엽수 묘목이 평균 34 cm 자랐고, 앙구스티폴리아물푸레는 아까시나무와 함께 대체 조림 수종으로 제시되었다[26].\n\n"
  "유럽에서는 침입성 곰팡이(Hymenoscyphus fraxineus, 이전 이름 H. pseudoalbidus)가 일으키는 물푸레나무 고사병이 이 종과 서양물푸레를 함께 위협한다[22, 23]. 27개국 산림 모니터링에서 물푸레나무류의 수관 낙엽률은 지난 30년 동안 거의 두 배가 되었고, 감염 뒤 생존 확률은 0.51까지 떨어졌다[22]. 기후 변화로 남부 지중해 변두리 개체군은 고유한 유전 다양성을 잃을 위험이 있다는 분석도 있다[12]. 식품원료용 열매는 모로코 중부 데므나트 지역에서 채집한 사례가 논문에 기록되어 있다[2]."},
 {"key": "processing", "title": "가공과 제품", "body":
  "연구에 쓰인 열매·씨앗 추출물은 특허 추출 공정으로 누제니드와 GL3를 약 10%로 표준화한 것이며, 캡슐 1개에 334 mg씩 담았다[2]. 같은 추출물은 탄수화물이 72.4 g/100 g으로 대부분을 차지하고 단백질과 식이섬유는 각각 약 6 g/100 g, 포도당 3.34 g/100 g, 설탕 3.84 g/100 g을 함유했다[2]. 사람 9명이 1 g을 한 번 먹은 시험에서 원래의 세코이리도이드 배당체는 혈액과 소변에서 검출되지 않았고, 티로솔과 리그스트로사이드 아글리콘의 글루쿠론산·황산 결합체가 2시간 무렵 가장 높았다[2].\n\n"
  "서양물푸레 이름으로 발표된 같은 계열 추출물 연구에서 1 g 단회 섭취는 건강한 성인 16명의 식후 혈당 곡선 아래 면적을 줄였고, 과체중·비만 고령자 22명이 3주 동안 하루 1 g을 먹은 교차 시험에서는 2시간 혈당이 14% 낮아졌다[4, 5]. 다만 이 연구들은 학명을 F. excelsior로 적었으므로 원료가 이 종이었는지는 [2]의 재감정 설명에 기대고 있으며, 시험 규모가 작다[2, 4, 5]. 쥐 실험에서는 고지방식 생쥐의 체중 증가 억제, 비만 쥐의 혈당·중성지방 감소가 보고되었으나 동물 결과다[7, 9]."},
 {"key": "genetics", "title": "유전과 계통", "body":
  "유럽 38개 자연 개체군 1,006그루를 유전형 분석한 결과 서부·북부 지중해 개체군의 유전 다양성이 가장 높았고, 서쪽에서 동쪽으로 갈수록 다양성이 줄었다[12]. 크로아티아 11개 개체군 연구에서는 대륙 지역과 지중해 지역 개체군이 서로 다른 생태형으로 갈라져 있을 가능성이 제시되었다[11]. 엽록체 DNA 다양성(hS=0.027)은 같은 지역 서양물푸레(hS=0.096)보다 낮고 개체군 간 분화(GST=0.964)는 높았다[13].\n\n"
  "핵 DNA(nETS) 계통에서는 이 종이 남동유럽 무리(서양물푸레와 가까움)와 지중해 나머지 무리(동아시아 F. mandshurica와 가까움)로 나뉘어, 먼 과거에 유라시아 물푸레나무 종 사이에 교잡이 있었음을 보여 준다[17]. 서양물푸레와의 인공 교배 잡종에서 엽록체는 어머니 쪽으로만 유전되었다[16]."},
 {"key": "safety", "title": "안전성", "body":
  "식약처 「식품원료 목록」에서 이 종은 열매에 한해 '사용가능'이며, 별도의 섭취량 제한이나 주의 문구는 목록에 없다[1]. 식품으로서 열매의 알레르기·잔류 농약·독성 성분에 관한 국내외 공공기관 안전 정보는 확인하지 못함[1]. 서양물푸레 씨앗 추출물이라는 이름으로 발표된 안전성 연구에서는 쥐 급성 경구 반수치사량이 2,500 mg/kg보다 컸고, 건강한 성인 100명이 하루 1,000 mg을 90일 먹어도 혈액 검사 항목은 위약군과 차이가 없었다[6]. 이 연구의 원료가 이 종이었는지는 [2]의 재감정 설명으로만 짐작할 수 있다[2, 6].\n\n"
  "물푸레나무과 꽃가루(올리브·서양물푸레·쥐똥나무 등)는 서로 교차 반응하는 알레르기 항원을 가지므로, 꽃가루 알레르기가 있는 사람은 주의가 필요하다[31]. 이것은 꽃가루 자료이며 열매를 먹을 때의 알레르기 자료는 아니다[31]. 스페인 폐광 주변에서는 이 종이 납을 많이 축적한 식물로 꼽혔으므로, 오염 지역에서 채집한 원료는 중금속 관리가 필요하다[32]. 잎·껍질·만나 추출물의 항산화·항증식·상처 치유 결과는 세포·동물 실험이고 열매 섭취의 효과나 안전성을 보여 주지 않는다[19, 21, 27, 30]."},
]

def c(name, ko, cls, role, part, txt, act, src):
    return {"name": name, "name_ko": ko, "class": cls, "role": role, "part": part, "content_text": txt, "activity_ko": act, "source": src}
compounds = [
 c("Nuzhenide", "누제니드", "세코이리도이드 배당체", "marker", "열매·씨앗(추출물)", "추출물의 5.92±0.14%(HPLC-UV 260 nm, 표준품 검량)[2]", "추출물의 두 주성분 가운데 하나; 원형은 사람 혈장·소변에서 검출되지 않음[2]; 세포 실험에서 PPARα 활성화·지방세포 분화 억제 보고(학명 F. excelsior로 표기된 씨앗)[8]", [2, 8]),
 c("GL3", "GL3(이량체 세코이리도이드 배당체)", "세코이리도이드 배당체(티로솔·엘레놀산 에스터)", "marker", "열매·씨앗(추출물)", "추출물의 4.75±0.09%; 누제니드와 합계 10.67±0.23%[2]", "추출물 표준화 지표; 섭취 뒤 티로솔·리그스트로사이드 아글리콘 결합체로 대사[2]", [2, 8]),
 c("Excelside B", "엑셀사이드 B", "세코이리도이드 배당체", "bioactive", "열매·씨앗(추출물)", "HPLC-DAD-MS/MS로 동정(함량 미보고)[2]", "처음 분리된 씨앗(학명 F. excelsior 표기)에서 지방세포 분화 억제·PPARα 활성화(세포 실험)[8]", [2, 8]),
 c("Salidroside", "살리드로사이드", "페닐에타노이드 배당체", "bioactive", "열매·씨앗(추출물)", "HPLC-DAD-MS/MS로 동정(함량 미보고)[2]", "추출물의 미량 성분[2]", [2]),
 c("Oleoside 11-methyl ester", "올레오사이드 11-메틸에스터", "세코이리도이드 배당체", "bioactive", "열매·씨앗(추출물)", "HPLC-DAD-MS/MS로 동정(함량 미보고)[2]", "추출물의 미량 세코이리도이드[2]", [2]),
 c("Verbascoside", "베르바스코사이드", "페닐에타노이드 배당체", "bioactive", "열매·씨앗(추출물); 만나", "열매 추출물에서 동정(함량 미보고)[2]; 만나 추출물에서도 동정[20]", "항산화 페놀 성분(만나 추출물 연구)[20]", [2, 20]),
 c("Isoverbascoside", "이소베르바스코사이드", "페닐에타노이드 배당체", "bioactive", "씨앗 기름(극성 분획)", "이 종에서 처음 보고(함량 초록에 없음)[3]", "씨앗 기름의 극성 페놀 성분[3]", [3]),
 c("Oleic acid", "올레산", "단일불포화 지방산", "nutrient", "씨앗 기름", "총 지방산의 45.5%[3]", "씨앗 기름의 주 지방산[3]", [3]),
 c("Linoleic acid", "리놀레산", "다중불포화 지방산(오메가-6)", "nutrient", "씨앗 기름", "총 지방산의 50.0%[3]", "씨앗 기름의 최대 지방산; 기름은 ABTS 라디칼 소거 IC50 28.2 μg/mL[3]", [3]),
 c("Tyrosol", "티로솔", "페닐에탄올", "bioactive", "열매 추출물 섭취 뒤 대사체; 만나", "섭취 2시간 뒤 혈장에서 글루쿠론산·황산 결합체로 검출(상대 면적, 절대 농도 미정량)[2]; 만나 추출물의 주요 페놀[20]", "열매 세코이리도이드의 주된 혈중 대사 산물[2]", [2, 20]),
 c("Mannitol", "만니톨", "당알코올", "bioactive", "만나(줄기 수액 굳은 것) — 식품원료 목록 부위 아님", "함량 초록에 없음[19]", "만나의 완하 작용 성분[19]", [19]),
 c("Quercetin 3-O-glucoside", "퀘르세틴-3-O-글루코사이드", "플라보놀 배당체", "bioactive", "잎(에탄올 추출물) — 식품원료 부위 아님", "조추출물 3585.25 µg/g(HPLC-DAD)[29]", "잎 추출물의 최다 페놀; 요소분해효소 억제(시험관)[29]", [29]),
 c("Esculin", "에스쿨린", "하이드록시쿠마린 배당체", "bioactive", "나무껍질 — 식품원료 부위 아님", "LC-DAD-MS/MS로 동정(함량 초록에 없음)[28]", "껍질 추출물의 잔틴산화환원효소 NADH 산화효소 억제 활성 성분(시험관·동물)[28]", [28]),
 c("Calceolarioside", "칼세올라리오사이드", "페닐에타노이드 배당체", "bioactive", "나무껍질·잎 — 식품원료 부위 아님", "LC/MS로 동정(함량 초록에 없음)[27, 28]", "껍질 추출물 활성 성분으로 제시[28]; 잎·껍질 추출물 구성 성분[27]", [27, 28]),
]

cond_hplc = {"instrument": "Agilent 1100 HPLC(광다이오드 배열 검출기)–이온트랩 질량분석기 직렬", "column": "LiChroCART C18, 250 × 4 mm, 입자 4.5 μm (Merck)", "mobile_phase": "A: 1% 포름산 수용액, B: 아세토니트릴", "gradient": "0분 1% B; 0–10분 1→9% B; 10–48분 9→35% B; 48–52분 35→95% B; 52–54분 95→1% B, 1%로 6분 유지(총 60분)", "flow": "0.8 mL/min", "temp": "실온", "detection": "UV 260 nm(스펙트럼 200–600 nm); ESI 음이온 m/z 100–1500, 건조가스 질소 11 L/min·350 °C·분무 65 psi", "injection": "10 μL", "sample_prep": "추출물 20 mg을 메탄올/물(50/50) 1 mL에 녹여 2분 볼텍스, 10분 초음파, 3500×g 10분 원심분리 후 0.45 μm PVDF 여과", "standard": "공급사가 합성한 누제니드·GL3 표준품", "linearity": "검량선 1–500 ppm(메탄올/물 50/50)", "lod": "", "loq": "", "recovery": ""}
assays = [
 {"role": "literature", "compound": "Nuzhenide", "compound_ko": "누제니드", "part": "열매·씨앗(표준화 추출물, 모로코산 열매)", "content": "5.92% ± 0.14%(추출물 기준)[2]", "method": "HPLC-DAD(260 nm) 정량, 이온트랩 MS/MS 동정", "conditions": cond_hplc, "rationale": "열매 추출물의 최대 세코이리도이드이며 추출물이 누제니드+GL3 약 10%로 표준화되어 있어 품질 지표로 쓰임; 전문 확인[2].", "source": [2], "url": "https://doi.org/10.3390/molecules201219845", "source_kind": "paper"},
 {"role": "literature", "compound": "GL3", "compound_ko": "GL3(이량체 세코이리도이드 배당체)", "part": "열매·씨앗(표준화 추출물, 모로코산 열매)", "content": "4.75% ± 0.09%; 누제니드와 합계 10.67% ± 0.23%[2]", "method": "HPLC-DAD(260 nm) 정량, 이온트랩 MS/MS 동정", "conditions": cond_hplc, "rationale": "누제니드와 함께 추출물 표준화 기준(합계 약 10%)인 두 번째 지표 성분; 전문 확인[2].", "source": [2], "url": "https://doi.org/10.3390/molecules201219845", "source_kind": "paper"},
 {"role": "literature", "compound": "Linoleic acid", "compound_ko": "리놀레산(씨앗 기름 지방산 조성)", "part": "씨앗 기름(F. angustifolia subsp. angustifolia)", "content": "총 지방산의 50.0%; 올레산 45.5%[3]", "method": "지방산 조성 분석(방법 세부는 초록에 없음)", "conditions": {"instrument": "", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "", "injection": "", "sample_prep": "", "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""}, "rationale": "씨앗 기름의 두 주 지방산으로 기름 품질 지표가 됨; 전문 확인 못함(초록만 확인)[3].", "source": [3], "url": "https://doi.org/10.1016/j.foodres.2019.02.013", "source_kind": "paper"},
]

d = {
 "slug": "fraxinus-angustifolia", "name_ko": "앙구스티폴리아물푸레", "name_en": "Narrow-leaved ash",
 "scientific_name": "Fraxinus angustifolia Vahl",
 "aliases": ["앙구스티폴리아물푸레열매", "좁은잎물푸레(영어명 직역)", "Narrow-leaved ash", "narrow-leafed ash", "Fraxinus angustifolia subsp. angustifolia"],
 "sections": sections, "compounds": compounds, "markers": [], "assays": assays,
 "nutrients": [], "production": [], "world": [], "gi": [], "orgs": [], "sources": S,
}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
print("written", len(S))
