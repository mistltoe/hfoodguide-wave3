import json
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "dossier.json"
A = "2026-11-02"


def pm(n, title, journal, pmid, doi, pmc=None):
    url = f"https://doi.org/{doi}" if doi else f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
    t = f"{title} — {journal} (PMID {pmid}" + (f", {pmc})" if pmc else ")")
    return {"n": n, "title": t, "url": url, "publisher": "PubMed", "accessed": A}


sources = [
    {"n": 1, "title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 락로즈(Cistus incanus L., Rock rose) 락로즈잎·락로즈줄기, 사용가능부위: 줄기, 잎; 같은 속의 Gum cistus(Cistus creticus / Cistus albidus) 잎, Common gum cistus(Cistus ladanifer L.) 씨앗, Sage-leaved rockrose(Cistus salviifolius) 잎",
     "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
    {"n": 2, "title": "Plants of the World Online — Cistus creticus L. (IPNI 168230-1), 승인명·자생 분포 (POWO 페이지는 이 환경에서 열리지 않아 WebSearch 요약으로만 확인)",
     "url": "https://powo.science.kew.org/taxon/urn:lsid:ipni.org:names:168230-1", "publisher": "Royal Botanic Gardens, Kew", "accessed": A},
    pm(3, "Intraspecific Genetic Diversity of Cistus creticus L. and Evolutionary Relationships to Cistus albidus L. (Cistaceae): Meeting of the Generations?", "Plants (Basel) 2021;10(8):1619", "34451664", "10.3390/plants10081619", "PMC8399514"),
    pm(4, "Polyphenol Profile of Cistus × incanus L. and Its Relevance to Antioxidant Effect and α-Glucosidase Inhibition", "Antioxidants (Basel) 2023;12(3):553", "36978801", "10.3390/antiox12030553", "PMC10045904"),
    pm(5, "The effect of Cistus incanus herbal tea supplementation on oxidative stress markers and lipid profile in healthy adults", "Cardiol J 2021;28(4):534-542", "30912576", "10.5603/CJ.a2019.0028", "PMC8277009"),
    pm(6, "Characterisation and Antioxidant Activity of Crude Extract and Polyphenolic Rich Fractions from C. incanus Leaves", "Int J Mol Sci 2016;17(8):1344", "27548139", "10.3390/ijms17081344", "PMC5000740"),
    pm(7, "Dissecting Adaptation Mechanisms to Contrasting Solar Irradiance in the Mediterranean Shrub Cistus incanus", "Int J Mol Sci 2019;20(14):3599", "31340536", "10.3390/ijms20143599", "PMC6678608"),
    pm(8, "Influence of the leaf content and herbal particle size on the presence and extractability of quantitated phenolic compounds in Cistus incanus herbal teas", "J Agric Food Chem 2014;62(45):10978-88", "25345843", "10.1021/jf504119s"),
    pm(9, "The Polyphenolic Composition of Cistus incanus Herbal Tea and Its Antibacterial and Anti-adherent Activity against Streptococcus mutans", "Planta Med 2015;81(18):1727-35", "26291656", "10.1055/s-0035-1557822"),
    pm(10, "Simultaneous determination of catechins, rutin, and gallic acid in Cistus species extracts by HPLC with diode array detection", "J Chromatogr Sci 2008;46(2):150-6", "18366875", "10.1093/chromsci/46.2.150"),
    pm(11, "Cistus incanus (CYSTUS052) for treating patients with infection of the upper respiratory tract. A prospective, randomised, placebo-controlled clinical study", "Antiviral Res 2009;84(3):267-71", "19828122", "10.1016/j.antiviral.2009.10.001"),
    pm(12, "A polyphenol rich plant extract, CYSTUS052, exerts anti influenza virus activity in cell culture without toxic side effects or the tendency to induce viral resistance", "Antiviral Res 2007;76(1):38-47", "17572513", "10.1016/j.antiviral.2007.05.002"),
    pm(13, "CYSTUS052, a polyphenol-rich plant extract, exerts anti-influenza virus activity in mice", "Antiviral Res 2007;76(1):1-10", "17573133", "10.1016/j.antiviral.2007.04.001"),
    pm(14, "Potent in vitro antiviral activity of Cistus incanus extract against HIV and Filoviruses targets viral envelope proteins", "Sci Rep 2016;6:20394", "26833261", "10.1038/srep20394", "PMC4735868"),
    pm(15, "Cistus incanus from Strandja Mountain as a Source of Bioactive Antioxidants", "Plants (Basel) 2018;7(1):8", "29373566", "10.3390/plants7010008", "PMC5874597"),
    pm(16, "Antibacterial potential of the Cistus incanus L. phenolics as studied with use of thin-layer chromatography combined with direct bioautography and in situ hydrolysis", "J Chromatogr A 2018;1534:170-178", "29290397", "10.1016/j.chroma.2017.12.056"),
    pm(17, "Antiproliferative and cytotoxic activity of extracts from Cistus incanus L. and Cistus monspeliensis L. on human prostate cell lines", "Nat Prod Res 2011;25(3):188-202", "20544500", "10.1080/14786410802583148"),
    pm(18, "Cistus incanus and Cistus monspeliensis inhibit the contractile response in isolated rat smooth muscle", "J Ethnopharmacol 2004;92(2-3):245-50", "15138007", "10.1016/j.jep.2004.02.020"),
    pm(19, "Identification of a novel plant amalgavirus (Amalgavirus, Amalgaviridae) genome sequence in Cistus incanus", "Acta Virol 2018;62(2):122-128", "29895152", "10.4149/av_2018_201"),
    pm(20, "Differential expression of fungal genes at preinfection and mycorrhiza establishment between Terfezia boudieri isolates and Cistus incanus hairy root clones", "New Phytol 2006;171(4):837-45", "16918554", "10.1111/j.1469-8137.2006.01791.x"),
    {"n": 21, "title": "Commission Implementing Regulation (EU) 2022/202 — 신규식품 연합 목록(Implementing Regulation (EU) 2017/2470) 정정, Cistus incanus L. 건조·절단 지상부 항목 (EUR-Lex 는 이 환경에서 열리지 않아 WebSearch 요약으로만 확인)",
     "url": "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022R0202", "publisher": "European Commission", "accessed": A},
    {"n": 22, "title": "Zistrose – eine Hilfe gegen Corona? (시스투스의 신규식품 지위·허브차 사용량 안내; 본문은 열지 않고 WebSearch 요약으로만 확인)",
     "url": "https://www.verbraucherzentrale.de/wissen/lebensmittel/nahrungsergaenzungsmittel/zistrose-eine-hilfe-gegen-corona-48529", "publisher": "Verbraucherzentrale (독일 소비자센터)", "accessed": A},
    pm(23, "Cistus x incanus L. extract as a complex polyphenolic blend with retained anti-adhesive and anti-inflammatory properties in a model of E. coli-induced UTI following simulated digestion", "J Ethnopharmacol 2025;356:120786", "41284510", "10.1016/j.jep.2025.120786"),
    pm(24, "Antioxidant properties and antibacterial activity of selected herbal teas", "Sci Rep 2025", "41272026", "10.1038/s41598-025-26960-8", "PMC12639085"),
    pm(25, "Conditions of prooxidant activity of cistus and pomegranate polyphenols in V79 cell cultures", "Acta Pol Pharm 2017;74(2):670-678", "29624273", None),
]

S = {}
S["overview"] = ("한눈에 보기", (
    "락로즈는 지중해 지역에 자라는 시스투스과(Cistaceae) 시스투스속 관목으로, 식약처 「식품원료 목록」에는 학명 Cistus incanus L., 영어 이름 Rock rose로 올라 있다[1]. "
    "이 목록에서 락로즈는 식품에 사용할 수 있는 원료(사용가능)이고, 사용 조건은 '사용가능부위 : 줄기, 잎'이며 원료명은 락로즈잎과 락로즈줄기 두 가지다[1]. "
    "이 종을 원재료로 하는 건강기능식품 고시형 원료는 확인하지 못함.\n\n"
    "학명은 쓰임이 복잡하다[3]. "
    "Kew의 POWO는 이 무리를 Cistus creticus L.로 받아들이고, 문헌과 식물지에서는 C. incanus·C. × incanus·C. creticus 같은 이름이 섞여 쓰인다[2, 3]. "
    "이 자료는 논문 제목·초록에 C. incanus 또는 C. × incanus로 적힌 연구만 모았고, 식약처 목록에 따로 오른 같은 속의 다른 원료 자료는 섞지 않았다[1, 3].\n\n"
    "유럽에서는 말린 잎과 어린 가지를 우려 마시는 허브차로 주로 팔리며, 시판 제품의 원산지는 튀르키예·알바니아·그리스가 많다[4, 8]. "
    "주요 성분은 푸니칼라진·시스투신·테르플라빈 A 같은 엘라기타닌과 미리세틴·퀘르세틴 배당체 같은 플라보놀이다[4, 6]. "
    "시험관·동물 연구에서 항산화·항균·항바이러스 작용이 보고되었으나, 사람 연구는 소규모 시험 몇 건뿐이다[5, 11, 12, 14]."
))
S["history"] = ("역사", (
    "락로즈 허브차는 예부터 지중해 지역 전통 의학에서 두루 쓰는 약으로 쓰였다고 정리되어 있다[6]. "
    "전통적으로 피부 상처, 호흡기 염증, 순환기·비뇨기 질환, 당뇨병, 위장 장애·소화성 궤양·설사에 권해졌다는 기록이 있다[4]. "
    "요로 감염 같은 감염성 질환에도 전통적으로 쓰였다[23]. "
    "남유럽에서는 수백 년 동안 민간 약으로 쓰였으나 문제가 보고되지 않았다고 한 연구진은 적었다[12].\n\n"
    "반면 불가리아 스트란자 산지에는 이 식물이 널리 자라지만 불가리아 민간 의학에서는 전통적으로 쓰던 약초가 아니다[15]. "
    "2000년대 독일에서는 잎 추출물의 항인플루엔자 작용을 세포와 생쥐에서 시험했고, 2009년에는 상기도 감염 환자 160명을 대상으로 한 위약 대조 임상시험이 발표되었다[11, 12, 13].\n\n"
    "2014년 논문은 유럽연합에서 락로즈가 신규식품(Novel Food)으로 분류되어 있음에도 여러 허브차 제품이 팔리고 있다고 지적했다[8]. "
    "이후 유럽연합 신규식품 목록에는 특정 계통의 건조·절단 지상부가 올랐다고 WebSearch 요약으로만 확인했다[21]. "
    "한국에 들어온 시기와 경로는 확인하지 못함."
))
S["biology"] = ("식물학적 특징", (
    "시스투스속은 지중해·카나리아 제도·마데이라에 넓게 퍼진 흰 꽃·자주 꽃 관목 무리로, 주로 햇볕이 강하게 드는 트인 땅이나 교란된 식생에 자란다[3]. "
    "학자에 따라 16–28종으로 보고, Euro+Med PlantBase에는 31종이 올라 있다[3]. "
    "락로즈 무리는 자주 꽃을 피우는 계통에 속한다[3].\n\n"
    "락로즈는 지중해의 상록 관목으로 소개되며, 이탈리아 토스카나 해안 사구 식생의 주요 구성원이다[6, 7]. "
    "햇볕을 좋아하는 반상록성 관목으로 여름에는 거의 자라지 않는다[7]. "
    "같은 곳에서 햇볕에 자란 잎은 그늘 잎보다 두께와 단위 면적당 무게가 평균 약 80% 컸고, 총 플라보노이드는 71%, 미리세틴 유도체는 610% 많았다[7]. "
    "불가리아 스트란자 산지에서는 야생으로 널리 자라며, 단단한 껍질에 싸인 씨앗을 맺는다[15].\n\n"
    "영어로는 hoary rockrose, hairy rockrose라고도 부른다[16, 19]. "
    "실험실에서 기른 락로즈 털뿌리는 사막 송로버섯(Terfezia boudieri)과 균근을 맺었는데, 균주 조합에 따라 외생균근 또는 내생균근이 생겼다[20]. "
    "시스투스속 식물은 모두 정유와 랍단형 다이테르펜을 담은 갈색 수지를 지닌다[4]."
))
S["related_species"] = ("이름과 가까운 종", (
    "Kew의 POWO는 Cistus creticus L.(1762년 발표)을 승인명으로 두고, 자생지를 알바니아·불가리아·키프로스·그리스·크레타·이탈리아·튀르키예·레바논-시리아·팔레스타인·모로코 등으로 적는다(WebSearch 요약으로 확인)[2]. "
    "2021년 유전 연구는 C. creticus라는 이름이 널리 받아들여지지만 C. incanus auct. 같은 이명도 식물지와 최근 문헌에 자주 쓰인다고 정리했다[3]. "
    "이 연구는 C. creticus가 동지중해 계통과 서지중해 계통의 두 큰 진화 계통을 품은 이질적인 종이라고 보고, 형태로 나눈 기존 아종 대신 두 아종 체계를 제안했다[3]. "
    "가까운 종 C. albidus와는 엽록체 유형을 함께 가질 만큼 유전적으로 가깝고, 같은 아속의 네 종은 서로 자유롭게 잡종을 만든다고 기술되었다[3].\n\n"
    "다른 연구진은 C. × incanus를 두 종 사이의 잡종으로 보며 세 아종을 구분하고, 아종과 산지에 따라 화학 조성과 활성이 크게 다를 수 있다고 썼다[4]. "
    "식약처 목록에는 같은 속의 Gum cistus(Cistus creticus / Cistus albidus) 잎, Common gum cistus(Cistus ladanifer) 씨앗, Sage-leaved rockrose(Cistus salviifolius) 잎이 락로즈와 따로 올라 있다[1]. "
    "시칠리아 연구들은 락로즈와 C. monspeliensis 추출물을 나란히 비교했다[10, 17, 18]."
))
S["cultivation"] = ("재배와 산지", (
    "국내 재배 면적·생산량 통계는 확인하지 못함. "
    "시판 락로즈 차 52개를 분석한 연구에서 원산지가 적힌 제품은 튀르키예 23개, 알바니아 10개, 그리스 3개였고 나머지는 원산지 표시가 없었다[4]. "
    "튀르키예산 제품은 엘라기타닌 함량이 평균 94 mg/g(건조중량)으로 그리스산 64 mg/g, 알바니아산 52 mg/g보다 높았다[4].\n\n"
    "폴란드 임상 연구에 쓴 원료는 제조사 정보에 따르면 튀르키예 안탈리아 주변 지중해 지역에서 자란 관목의 잎을 5–8월에 거둔 것이다[5]. "
    "이탈리아 연구는 남부 토스카나 해안 사구에서 다 자란 잎을 7월에 거두어 분석했다[6]. "
    "햇볕에 자란 잎은 그늘에 자란 잎보다 플라보노이드가 훨씬 많아, 자라는 곳의 빛 조건이 원료 품질에 영향을 준다[7].\n\n"
    "불가리아 스트란자의 야생 개체에서는 여름 잎뿐 아니라 겨울 잎, 씨앗, 꽃눈, 줄기에도 폴리페놀과 플라보노이드가 많았다[15]. "
    "같은 연구에서 추출 수율은 30% 에탄올로 390분 추출할 때 가장 좋았다[15]. "
    "번식·재배 방법(파종·꺾꽂이 등)은 확인하지 못함."
))
S["processing"] = ("가공과 이용", (
    "시판 락로즈 허브차는 잎과 줄기의 비율, 입자 크기가 제품마다 달라, 잎이 많고 잘게 썬 것이 있는가 하면 주로 나무질 줄기로 된 것도 있다[8]. "
    "잎이 많고 입자가 작은 원료를 우릴 때 우림액의 페놀 성분 농도가 가장 높았다[8]. "
    "시판 차 4종은 29가지 폴리페놀의 종류는 같고 양만 달랐다[9].\n\n"
    "물 우림액의 총폴리페놀은 55% 메탄올 추출물보다 6배 이상 적었다(55 대 350 mg GAE/g 건조중량)[4]. "
    "같은 차를 세 번 우리면 첫 우림액에 폴리페놀과 항산화력이 가장 많고 다음 우림부터 점점 줄었다[5]. "
    "임상 연구에서는 하루 2 g의 차를 끓는 물 250 mL에 3분씩 세 번 우려 마시게 했다[5].\n\n"
    "지상부의 물-알코올 추출물은 식품보충제 원료로 연구되고 있다[23]. "
    "8가지 허브차를 비교한 연구에서 락로즈 차는 항산화력이 높은 편이었고 항균 작용은 가장 강한 축에 들었다[24]. "
    "국내에서 락로즈를 원료로 한 건강기능식품 생산실적은 확인하지 못함."
))
S["genetics"] = ("유전 정보", (
    "이탈리아 연구진은 해안 사구의 락로즈 잎에서 RNA-Seq로 전사체를 새로 조립했는데, 두 라이브러리에서 약 1,877만·1,822만 개의 읽기를 얻어 59,030개의 전사체(평균 1,028 bp, N50 1,462 bp)를 만들었다[7]. "
    "보존 단백질 248개 중 243개(98%)가 완전한 형태로 확인되었고, 22,784개(38.6%)에 기능 주석이 붙었다[7]. "
    "햇볕과 그늘 잎 사이에 발현이 달라진 전사체는 3,590개였고, 햇볕 잎에서는 칼콘 합성효소 등 플라보노이드 합성 유전자가 크게 늘었다[7]. "
    "원자료는 NCBI SRA(BioProject PRJNA354245)에 공개되어 있다[7].\n\n"
    "락로즈 전사체 자료에서는 새로운 식물 RNA 바이러스(Cistus incanus RNA virus 1, 앰앨가바이러스속)의 유전체 서열도 발견되었다[19]. "
    "C. creticus·C. albidus 무리를 핵 ITS와 엽록체 두 구간으로 분석한 연구에서는 서지중해 계통 개체의 약 27%가 한 개체 안에 서로 다른 ITS 변이를 함께 지녔다[3]. "
    "락로즈를 잡종 기원으로 보는 견해도 있다[4]. "
    "염색체 수와 유전체 크기는 확인하지 못함."
))
S["safety"] = ("안전성", (
    "식약처 「식품원료 목록」에서 락로즈는 잎과 줄기를 식품에 쓸 수 있는 사용가능 원료다[1]. "
    "국내 공공기관의 락로즈 관련 알레르기·잔류물질·독성 성분 정보는 확인하지 못함.\n\n"
    "유럽연합에서는 신규식품으로 분류되어 왔으며, 2022년 정정 규정으로 특정 계통의 건조·절단 지상부(나무질을 포함한 어린 가지)가 신규식품 목록에 올랐다고 WebSearch 요약으로만 확인했다[8, 21]. "
    "독일 소비자센터 안내는 이 승인이 허브 3 g 이하를 쓰는 허브차에 해당하며 다른 제품의 법적 지위는 불확실하다고 설명한다고 WebSearch 요약으로만 확인했다[22].\n\n"
    "건강한 성인 24명이 12주 동안 하루 2 g의 락로즈 차를 마신 예비 연구는 대조군 없이 진행되었다[5]. 이 연구의 이상반응 결과는 본문에서 확인하지 못함. "
    "세포 실험에서 잎 추출물은 50 µg/mL에서 세포 생존·대사에 해를 보이지 않았다[12]. "
    "반면 25–100 µg/mL의 높은 농도에서는 세포 안 활성산소를 오히려 늘렸다[25]. "
    "엘라기타닌은 크기 때문에 혈액으로 흡수되지 않고, 장에서 엘라그산으로 분해된 뒤 장내 미생물에 의해 유로리틴으로 바뀐다[4]. "
    "새우 유생 치사 시험으로 급성 독성을 평가한 연구가 있으나 그 결과는 초록에서 확인하지 못함."
))

compounds = [
    {"name": "Punicalagin", "name_ko": "푸니칼라진", "class": "엘라기타닌", "role": "marker", "part": "잎·어린 가지(시판 차)",
     "content_text": "시판 차 52개 평균 29 mg/g 건조중량(HPLC-DAD)", "activity_ko": "시험관에서 α-글루코시데이스 억제(IC50 1.1 µM, 경쟁적 억제)", "source": [4]},
    {"name": "Cistusin", "name_ko": "시스투신", "class": "엘라기타닌", "role": "marker", "part": "잎·어린 가지(시판 차)",
     "content_text": "시판 차 52개 평균 25 mg/g 건조중량(HPLC-DAD)", "activity_ko": "시험관에서 시험한 성분 중 가장 강한 α-글루코시데이스 억제(IC50 0.7 µM)", "source": [4]},
    {"name": "Terflavin A", "name_ko": "테르플라빈 A", "class": "엘라기타닌", "role": "bioactive", "part": "잎·어린 가지(시판 차)",
     "content_text": "시판 차 52개 평균 14 mg/g 건조중량(HPLC-DAD)", "activity_ko": "시험관에서 α-글루코시데이스 억제(IC50 1.1 µM)", "source": [4]},
    {"name": "Punicalin", "name_ko": "푸니칼린", "class": "엘라기타닌", "role": "bioactive", "part": "잎·어린 가지(시판 차)",
     "content_text": "평균 0.4 mg/g 건조중량(푸니칼라진으로 환산)", "activity_ko": "소량 엘라기타닌 성분으로 확인됨", "source": [4]},
    {"name": "Gallic acid", "name_ko": "갈산", "class": "페놀산", "role": "bioactive", "part": "잎·어린 가지",
     "content_text": "시판 차 평균 7 mg/g 건조중량(메탄올 추출물); 튀르키예산 차 우림액 기준 약 500 µg/g 건조중량", "activity_ko": "시험관 α-글루코시데이스 억제(IC50 117 µg/mL, 혼합형 억제)", "source": [4, 5]},
    {"name": "Ellagic acid", "name_ko": "엘라그산", "class": "페놀산", "role": "bioactive", "part": "잎·어린 가지",
     "content_text": "시판 차 평균 3 mg/g 건조중량", "activity_ko": "엘라기타닌의 분해 산물로, 장내 미생물이 유로리틴으로 바꿈; 시험관 α-글루코시데이스 억제(IC50 11 µM)", "source": [4]},
    {"name": "Myricitrin", "name_ko": "미리시트린(미리세틴-3-O-람노사이드)", "class": "플라보놀 배당체", "role": "marker", "part": "잎",
     "content_text": "시판 차 평균 4 mg/g 건조중량", "activity_ko": "잎 추출물의 라디칼 소거 활성에 주로 기여; 세 가지 시험에서 IC50이 에피카테킨의 약 절반", "source": [4, 6]},
    {"name": "Hyperoside", "name_ko": "하이페로사이드(퀘르세틴-3-O-갈락토사이드)", "class": "플라보놀 배당체", "role": "bioactive", "part": "잎·어린 가지",
     "content_text": "시판 차 평균 3 mg/g 건조중량", "activity_ko": "시험관 α-글루코시데이스 억제는 약함(500 µg/mL에서 26%)", "source": [4]},
    {"name": "Myricetin 3-O-galactoside", "name_ko": "미리세틴-3-O-갈락토사이드", "class": "플라보놀 배당체", "role": "bioactive", "part": "잎·어린 가지",
     "content_text": "시판 차 평균 3 mg/g 미만 건조중량", "activity_ko": "시험관 α-글루코시데이스 중간 정도 억제(500 µg/mL에서 30–40%)", "source": [4]},
    {"name": "Tiliroside", "name_ko": "틸리로사이드", "class": "쿠마로일 플라보놀 배당체", "role": "bioactive", "part": "잎·어린 가지",
     "content_text": "시판 차 평균 2 mg/g 건조중량", "activity_ko": "박층크로마토그래피-생물검정에서 항균 성분으로 확인; 시험관 α-글루코시데이스 73.6% 억제(500 µg/mL)", "source": [4, 16]},
    {"name": "Myricetin", "name_ko": "미리세틴", "class": "플라보놀", "role": "bioactive", "part": "잎(우림차)",
     "content_text": "튀르키예산 차 우림액 기준 800 µg/g 건조중량 초과(HPLC)", "activity_ko": "햇볕 잎에서 미리세틴 유도체가 그늘 잎보다 610% 많음", "source": [5, 7]},
    {"name": "Isoquercitrin", "name_ko": "이소퀘르시트린", "class": "플라보놀 배당체", "role": "bioactive", "part": "잎(우림차)",
     "content_text": "튀르키예산 차 우림액 기준 800 µg/g 건조중량 초과(HPLC)", "activity_ko": "우림액의 주요 플라보노이드로 측정됨", "source": [5]},
    {"name": "Epicatechin", "name_ko": "에피카테킨", "class": "플라반-3-올", "role": "bioactive", "part": "잎",
     "content_text": "카테킨·에피카테킨 합계 약 1 mg/g 건조중량(범위 0.4–2.4 mg/g)", "activity_ko": "잎 추출물의 정량 표준물질로 쓰임", "source": [4, 6]},
    {"name": "Gallocatechin", "name_ko": "갈로카테킨", "class": "플라반-3-올", "role": "bioactive", "part": "잎",
     "content_text": "잎 에탄올 추출물에서 갈로카테킨·에피갈로카테킨과 그 이량체를 확인(함량은 본문에서 확인하지 못함)", "activity_ko": "시칠리아 락로즈 추출물 분석에서 특이 지표성분으로 정량됨", "source": [6, 10]},
]

assays = [
    {"role": "literature", "compound": "Myricitrin (myricetin 3-O-rhamnoside) and flavonol glycosides", "compound_ko": "미리시트린 등 플라보놀 배당체",
     "part": "잎(토스카나 해안 사구, 7월 채취)", "content": "", "method": "HPLC-DAD(동정은 LC-ESI-MS/MS)",
     "conditions": {"instrument": "Shimadzu Nexera HPLC(DAD) + Shimadzu LCMS-8030 사중극자 질량분석기(ESI)",
                    "column": "Waters Nova-Pak C18, 4.9 × 250 mm, 4 µm",
                    "mobile_phase": "A: 1% 포름산 수용액, B: 1% 포름산 함유 아세토니트릴/메탄올(25/75)",
                    "gradient": "B 2% 10분 유지 → 30분 동안 2→98% 직선 → 98% 7분 유지",
                    "flow": "0.6 mL/min", "temp": "30 °C", "detection": "DAD 280·350 nm(정량); ESI 음이온 모드(동정)",
                    "injection": "10 µL",
                    "sample_prep": "생잎 5 g을 액체질소로 분쇄, pH 2.5(포름산) 70% 에탄올 50 mL×5로 30분 초음파 추출, n-헥산으로 지질 제거; 추출물 300 µL를 메탄올/산성수(pH 2) 80:20 1.20 mL에 희석",
                    "standard": "갈산·에피카테킨·미리세틴 3-O-람노사이드·퀘르세틴 3-O-람노사이드·루틴(각 자체 검량선), 캠페롤 유도체는 캠페롤 7-O-글루코사이드로 환산",
                    "linearity": "", "lod": "", "loq": "", "recovery": ""},
     "rationale": "잎 추출물의 라디칼 소거 활성이 플라보놀(미리세틴·퀘르세틴 유도체) 함량과 가장 잘 맞아 미리시트린을 활성 기준 성분으로 비교함. 전문(Methods)에서 조건을 옮겼고, 성분별 함량은 표에 있어 본문에서 확인하지 못함[6].",
     "source": [6], "url": "https://doi.org/10.3390/ijms17081344", "source_kind": "paper"},
    {"role": "literature", "compound": "Punicalagin, cistusin, terflavin A (ellagitannins) and flavonols", "compound_ko": "푸니칼라진·시스투신·테르플라빈 A 등 엘라기타닌과 플라보놀",
     "part": "시판 차(말린 잎 또는 어린 가지 끝) 52개", "content": "푸니칼라진 평균 29 mg/g, 시스투신 25 mg/g, 테르플라빈 A 14 mg/g 건조중량; 엘라기타닌 합계 평균 73 mg/g(26–189 mg/g)[4]",
     "method": "HPLC-DAD(동정은 UHPLC-ESI-qTOF-MS)",
     "conditions": {"instrument": "Dionex Ultimate 3000(WPS-3000TSL 자동시료주입기, LPG-3400SD 펌프, TCC-3000SD 칼럼오븐, DAD-3000 검출기)",
                    "column": "Thermo Hypersil Gold C18, 250 × 4.6 mm, 5 µm",
                    "mobile_phase": "", "gradient": "", "flow": "", "temp": "",
                    "detection": "254 nm(플라보놀·엘라그산·엘라기타닌), 280 nm(갈산·플라반-3-올), 320 nm(쿠마로일 플라보놀)",
                    "injection": "",
                    "sample_prep": "분쇄 후 0.355 mm 체로 거름; 약 1 g을 55% 메탄올 50 mL에 넣어 끓기 시작한 뒤 15분 환류 추출, 0.45·0.22 µm 여과(원료:용매 1:50, 3반복)",
                    "standard": "시판 표준품(순도 95% 이상)과 직접 분리한 시스투신·푸니칼라진·테르플라빈 A; 메탄올 1 mg/mL 원액을 20–200 µg/mL로 희석",
                    "linearity": "", "lod": "", "loq": "", "recovery": ""},
     "rationale": "엘라기타닌이 폴리페놀의 약 69%를 차지하는 주성분이며 원산지(튀르키예·그리스·알바니아)에 따라 함량이 뚜렷이 달라 품질 비교 지표로 쓰임. 이동상·기울기·유속은 '이전 논문의 방법'으로만 적혀 있어 비워 둠[4].",
     "source": [4], "url": "https://doi.org/10.3390/antiox12030553", "source_kind": "paper"},
    {"role": "literature", "compound": "Myricetin, isoquercitrin, quercetin, gallic acid, rutin", "compound_ko": "미리세틴·이소퀘르시트린·퀘르세틴·갈산·루틴",
     "part": "잎 우림액(튀르키예 안탈리아산 시판 차)", "content": "미리세틴·퀘르세틴·이소퀘르시트린 각 800 µg/g 건조중량 초과, 갈산·루틴 약 500 µg/g, 루테올린 7-글루코사이드 약 400 µg/g[5]",
     "method": "HPLC",
     "conditions": {"instrument": "", "column": "Thermo Hypersil Gold C18, 250 × 4.6 mm, 5 µm",
                    "mobile_phase": "아세토니트릴–0.2% 트라이플루오로아세트산 / 물–0.2% 트라이플루오로아세트산",
                    "gradient": "", "flow": "", "temp": "35 °C", "detection": "", "injection": "20 µL",
                    "sample_prep": "잎 1.00 g을 끓는 탈이온수 100 mL로 15분 우림(3회 반복 우림), 0.2 µm 나일론 필터로 여과",
                    "standard": "갈산·카페산·클로로겐산·시링산·바닐산·p-쿠마르산·엘라그산·페룰산·루틴·이소퀘르시트린·퀘르세틴·미리세틴·캠페롤·루테올린 7-글루코사이드",
                    "linearity": "", "lod": "", "loq": "", "recovery": ""},
     "rationale": "사람이 실제로 마신 우림액의 페놀 성분 조성을 확인하려고 정량함. 기울기·검출 조건은 '이전 논문의 방법'으로만 적혀 있어 비워 둠[5].",
     "source": [5], "url": "https://doi.org/10.5603/CJ.a2019.0028", "source_kind": "paper"},
    {"role": "literature", "compound": "Gallic acid, gallocatechin, catechin, rutin", "compound_ko": "갈산·갈로카테킨·카테킨·루틴",
     "part": "시칠리아산 락로즈 동결건조 추출물", "content": "", "method": "HPLC-DAD",
     "conditions": {"instrument": "", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "",
                    "injection": "", "sample_prep": "", "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""},
     "rationale": "카테킨류 5종과 갈산·루틴을 함께 분리하는 검증된 방법을 락로즈·C. monspeliensis 추출물에 적용해 갈산·갈로카테킨·카테킨·루틴을 특이 지표성분으로 정량함. 초록만 보았고 전문 확인 못함(초록에는 C18 역상 칼럼, 아세토니트릴-50 mM 인산완충액 pH 2.5 기울기, 1 mL/min, 210 nm, 검출한계 0.24–0.74 µg/mL, 정량한계 0.77–1.94 µg/mL, 회수율 78.7–98.2%로 적힘)[10].",
     "source": [10], "url": "https://doi.org/10.1093/chromsci/46.2.150", "source_kind": "paper"},
]

d = {
    "slug": "cistus-incanus",
    "name_ko": "락로즈",
    "name_en": "Rock rose (hoary rockrose)",
    "scientific_name": "Cistus incanus L.",
    "aliases": ["Rock rose", "락로즈잎", "락로즈줄기", "Cistus × incanus", "hoary rockrose", "hairy rockrose"],
    "sections": [{"key": k, "title": t, "body": b} for k, (t, b) in S.items()],
    "compounds": compounds,
    "markers": [],
    "nutrients": [],
    "assays": assays,
    "production": [],
    "world": [],
    "gi": [],
    "orgs": [],
    "sources": sources,
}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for k, (t, b) in S.items():
    print(k, len(b))
