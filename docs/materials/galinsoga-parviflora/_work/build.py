import json, pathlib
P = pathlib.Path(__file__).resolve().parent.parent
A = "2026-11-02"
def pm(n, title, pmid, doi=None, pub="", note="초록 확인"):
    url = f"https://doi.org/{doi}" if doi else f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
    return {"n": n, "title": f"{title} (PMID {pmid}{', ' + note if note else ''})", "url": url, "publisher": pub + " (PubMed)", "accessed": A}

sources = [
 {"n": 1, "title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 별꽃아재비잎·별꽃아재비줄기 행(학명 Galinsoga parviflora, 영문 Gallant soldier, 식품원료(A코드)·식물, 부위 잎/줄기, 사용가능, '사용가능부위 : 줄기,잎'); 같은 속(Galinsoga)의 다른 원료 행은 없음. 로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json·docs/materials/galinsoga-parviflora/card.json", "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
 pm(2, "Galinsoga parviflora (Cav.): A comprehensive review on ethnomedicinal, phytochemical and pharmacological studies. Heliyon 2023;9(2):e13517", "36846665", "10.1016/j.heliyon.2023.e13517", "Heliyon", "PMC9946856 전문 확인"),
 pm(3, "Anti-inflammatory Activity and Phytochemical Profile of Galinsoga parviflora Cav. Molecules 2018;23(9):2133", "30149540", "10.3390/molecules23092133", "Molecules", "PMC6225198 전문 확인"),
 pm(4, "Chemical constituents and biological activities of Galinsoga parviflora Cav. (Asteraceae) from Egypt. Z Naturforsch C 2013;68(7-8):285-92", "24066513", None, "Z Naturforsch C J Biosci"),
 pm(5, "Phenolic compounds, antioxidant activity and in vitro inhibitory potential against key enzymes relevant for hyperglycemia and hypertension of commonly used medicinal plants, herbs and spices in Latin America. Bioresour Technol 2010;101(12):4676-89", "20185303", "10.1016/j.biortech.2010.01.093", "Bioresour Technol", "초록 확인; 별꽃아재비 함량 수치는 초록에 없음"),
 pm(6, "Nutritional Composition and Bioactive Compounds of Quelites Consumed by Indigenous Communities in the Municipality of Juquila Vijanos, Sierra Norte of Oaxaca, Mexico. Plant Foods Hum Nutr 2023;78(1):193-200", "36609832", "10.1007/s11130-022-01039-1", "Plant Foods Hum Nutr", "초록 확인; 별꽃아재비의 종별 성분 수치는 초록에 없음"),
 pm(7, "Galinsosides A and B, bioactive flavanone glucosides from Galinsoga parviflora. J Enzyme Inhib Med Chem 2009;24(5):1128-32", "19772485", "10.1080/14756360802667688", "J Enzyme Inhib Med Chem"),
 pm(8, "New aromatic esters from Galinsoga parviflora. J Asian Nat Prod Res 2012;14(5):424-8", "22348678", "10.1080/10286020.2012.657181", "J Asian Nat Prod Res"),
 pm(9, "Parvisides A and B, new glucosides from Galinsoga parviflora. Nat Prod Commun 2014", "25233600", None, "Nat Prod Commun"),
 pm(10, "Essential oil of Galinsoga parviflora leaves from Colombia. Nat Prod Commun 2010;5(11):1831-2", "21213993", None, "Nat Prod Commun"),
 pm(11, "High efficacy of (Z)-γ-bisabolene from the essential oil of Galinsoga parviflora (Asteraceae) as larvicide and oviposition deterrent against six mosquito vectors. Environ Sci Pollut Res Int 2018;25(11):10555-66", "29372518", "10.1007/s11356-018-1203-3", "Environ Sci Pollut Res Int"),
 pm(12, "Determination of antioxidant activity of extracts and fractions obtained from Galinsoga parviflora and Galinsoga quadriradiata, and a qualitative study of the most active fractions using TLC and HPLC methods. Nat Prod Res 2012;26(17):1584-93", "22085305", "10.1080/14786419.2011.582469", "Nat Prod Res"),
 pm(13, "Determination of in vitro antioxidant and UV-protecting activity of aqueous and ethanolic extracts from Galinsoga parviflora and Galinsoga quadriradiata herb. J Photochem Photobiol B 2015;149:189-95", "26092182", "10.1016/j.jphotobiol.2015.06.010", "J Photochem Photobiol B"),
 pm(14, "Reactive Nitrogen Species Scavenging Capacity of Aqueous and Ethanolic Extracts from Galinsoga parviflora and G. quadriradiata Herbs. Nat Prod Commun 2015;10(11):1825-8", "26749807", None, "Nat Prod Commun"),
 pm(15, "Caffeic acid derivatives isolated from Galinsoga parviflora herb protected human dermal fibroblasts from UVA-radiation. Phytomedicine 2019;57:215-222", "30785017", "10.1016/j.phymed.2018.12.022", "Phytomedicine"),
 pm(16, "Biological studies on Brazilian plants used in wound healing. J Ethnopharmacol 2009;122(3):523-32", "19429323", "10.1016/j.jep.2009.01.022", "J Ethnopharmacol"),
 pm(17, "Angiotensin I-converting enzyme inhibitor activity of nutritive plants in KwaZulu-Natal. J Med Food 2008;11(2):331-6", "18598177", "10.1089/jmf.2007.569", "J Med Food"),
 pm(18, "Seed germination, seedling emergence, seed persistence and triflusulfuron-methyl sensitivity in Galinsoga parviflora and G. quadriradiata. Commun Agric Appl Biol Sci 2013;78(3):681-91", "25151846", None, "Commun Agric Appl Biol Sci"),
 pm(19, "Can transgenerational plasticity contribute to the invasion success of annual plant species? Oecologia 2014", "24929349", "10.1007/s00442-014-2994-7", "Oecologia"),
 pm(20, "Screening of a new cadmium hyperaccumulator, Galinsoga parviflora, from winter farmland weeds using the artificially high soil cadmium concentration method. Environ Toxicol Chem 2014;33(11):2422-8", "25053512", "10.1002/etc.2694", "Environ Toxicol Chem"),
 pm(21, "Effects of mulching tolerant plant straw on soil surface on growth and cadmium accumulation of Galinsoga parviflora. PLoS One 2014;9(12):e114957", "25490210", "10.1371/journal.pone.0114957", "PLoS One"),
 pm(22, "Characterization of the complete chloroplast genome sequence of Galinsoga parviflora and its phylogenetic implications. Mitochondrial DNA B Resour 2019 (PMC7687395 전문 확인; PubMed 제목·초록에서 학명 글자가 빠져 있어 종명은 본문 인용 문헌·표본 번호로 판단)", "33365429", "10.1080/23802359.2019.1623106", "Mitochondrial DNA B Resour", ""),
 pm(23, "Tomato spotted wilt virus in ornamental plants, vegetables and weeds in the Czech Republic. Acta Virol 1998;42(5):347-51", "10358737", None, "Acta Virol"),
 pm(24, "Performance of Bemisia tabaci (Genn.) Biotype B (Hemiptera: Aleyrodidae) on Weeds. Neotrop Entomol 2014", "27194066", "10.1007/s13744-014-0238-5", "Neotrop Entomol"),
 pm(25, "Population dynamics of weeds in no-tillage and conventional crop systems. J Environ Sci Health B 2005;40(1):119-28", "15656169", "10.1081/pfc-200034259", "J Environ Sci Health B"),
 pm(26, "Effect of Quaternary Ammonium Salts with Fluorine Atoms on Selected Weed Species. Bull Environ Contam Toxicol 2017", "28197704", "10.1007/s00128-017-2033-6", "Bull Environ Contam Toxicol"),
 pm(27, "Melatonin affects the growth and cadmium accumulation of Malachium aquaticum and Galinsoga parviflora. Int J Phytoremediation 2018", "29053350", "10.1080/15226514.2017.1374341", "Int J Phytoremediation"),
 pm(28, "Effects of mutual grafting on cadmium accumulation characteristics of first post-generations of Bidens pilosa L. and Galinsoga parviflora Cav. Environ Sci Pollut Res Int 2019;26(32):33228-35", "31520390", "10.1007/s11356-019-06498-9", "Environ Sci Pollut Res Int"),
]

sections = [
 {"key": "overview", "title": "한눈에 보기", "body":
  "별꽃아재비(Galinsoga parviflora Cav.)는 국화과(Asteraceae)에 속하는 한해살이풀로, 영어로는 gallant soldier라 부른다[1, 2, 3]. 원산지는 남·북아메리카이며 아시아·아프리카·오스트레일리아 등으로 퍼져 세계 여러 곳에 귀화했다[2, 11].\n\n"
  "식약처 「식품원료 목록」에는 '별꽃아재비잎'과 '별꽃아재비줄기'가 식품원료(A코드)로 올라 있고, 상태는 '사용가능', 조건은 '사용가능부위 : 줄기,잎'이다[1]. 따라서 식품원료로 쓸 수 있는 부위는 잎과 줄기이며, 꽃·뿌리·씨앗은 목록의 사용 부위에 들어 있지 않다[1]. 건강기능식품 고시형 원료의 원재료가 아니므로 고시 지표성분이나 1일 섭취량 기준은 없다[1].\n\n"
  "중남미·아프리카에서는 어린 순과 잎을 채소로 먹고 민간에서 상처·피부병·감기 등에 써 왔다[2, 3, 6]. 지상부에서는 클로로겐산 등 페놀산과 파툴리트린 같은 플라보노이드 배당체가 보고되었다[3, 12]. 새 성분으로는 갈린소사이드 A·B(플라바논 배당체), 갈리노소에이트 A–C(방향족 에스터), 파르비사이드 A·B(배당체)가 분리되었다[7, 8, 9]. 효능 연구는 대부분 세포·동물 실험이며 사람 대상 임상시험은 이번 조사에서 확인하지 못함. 한편 이 종은 토양의 카드뮴을 지상부에 많이 쌓는 식물로 보고되어 있다[20]."},
 {"key": "history", "title": "이름과 이용의 역사", "body":
  "속명 Galinsoga와 종소명 parviflora('작은 꽃')를 쓰는 이 식물은 영국에서 Gallant soldier, 중앙아메리카에서 Quickweed·Waterweed·Piphe 등으로 불린다고 정리되었다[2]. 짧은 기간에 자라 퍼지는 성질이 이런 이름과 관련된다고 소개된다[2].\n\n"
  "라틴아메리카에서 전통적으로 쓰는 약초·허브·향신료를 다룬 연구에 이 식물이 '과스카스(Guascas)'라는 이름으로 포함되었다[5]. 멕시코 오악사카 북부 산지의 원주민 공동체는 이 식물을 '켈리테(quelite)', 즉 먹는 야생 잎채소의 하나로 먹어 왔다[6]. 남아프리카·짐바브웨·탄자니아에서도 어린 순과 잎을 채소로 먹는다고 종설은 적고 있다[2]. 라틴아메리카와 북아메리카에서는 샐러드와 수프 재료로 쓰인다는 기록이 있다[3].\n\n"
  "민간요법에서는 생잎과 즙을 습진·상처 등 피부 질환에 쓰고, 감기·독감에 먹었다고 전한다[3]. 비타민 C가 많아 괴혈병 예방에 쓰였다는 기록도 있다[2, 3]. 브라질 남부에서는 상처 치료용 전통 약초 12종 가운데 하나로 연구되었다[16]. 남아프리카 콰줄루나탈에서는 '영양 식물(nutritive plant)'의 하나로 다뤄졌다[17]. 국내에서의 전통적 이용 기록은 이번 조사에서 확인하지 못함."},
 {"key": "biology", "title": "식물학적 특징", "body":
  "별꽃아재비는 국화과 별꽃아재비속(Galinsoga)의 한해살이풀이다[2, 3]. 줄기는 곧게 서고 가늘며 가지를 치고, 세로 줄이 있으며 털이 있거나 없다[2]. 잎은 마주나고 피침형~달걀형이며 연녹색으로, 길이 1–6 cm, 너비 0.5–4 cm다[2]. 잎 가장자리에는 속눈썹 같은 짧은 털이 나고, 위쪽 잎은 더 작고 좁으며 잎자루가 없는 경우가 많다[2].\n\n"
  "머리모양꽃차례는 지름 4–7 mm로 작고, 가운데 노란 통꽃을 보통 5개의 작은 흰 혀꽃이 둘러싼다[2]. 혀꽃 끝은 세 갈래로 갈라진다[2]. 열매는 수과로, 혀꽃의 수과는 길이 약 2 mm이고 짧은 갓털이 있거나 없으며, 통꽃의 수과는 약 1.8 mm에 가장자리에 털이 있는 1.5 mm 길이의 비늘 모양 갓털이 붙는다[2].\n\n"
  "씨앗은 빛이 있어야 싹이 트고, 묻힌 깊이가 깊어지면 출현이 크게 줄어 최대 출현 깊이는 토양·집단에 따라 4–10 mm였다[18]. 갓 맺은 씨앗은 1차 휴면 정도가 높지만 그 정도는 집단마다 달랐다[18]. 생리적으로는 토양 카드뮴 100 mg/kg 조건에서 지상부 카드뮴이 최대 137.63 mg/kg까지 올라, 카드뮴 초집적 식물로 분류되었다[20]."},
 {"key": "related_species", "title": "같은 속·혼동 주의 식물", "body":
  "가장 혼동하기 쉬운 종은 같은 속의 Galinsoga quadriradiata Ruiz & Pav.(영문 hairy galinsoga)다[18]. 국내에서는 이 종을 털별꽃아재비로 부르는 것으로 알려져 있으나, 이 국문명 대응은 이번 조사에서 공식 목록으로 확인하지 못함. 식약처 「식품원료 목록」에서 별꽃아재비속 원료는 Galinsoga parviflora 한 종뿐이며, G. quadriradiata는 목록에 없다[1]. 따라서 G. quadriradiata에서 나온 성분·효능 자료를 별꽃아재비 자료로 옮겨 쓰면 안 된다[1, 18].\n\n"
  "두 종은 생태적 성질이 다르다[18]. 벨기에 연구에서 갓 맺은 G. parviflora 씨앗은 1차 휴면이 높고 덜 오래 살아남은 반면, G. quadriradiata 씨앗은 1차 휴면이 없고 더 오래 남았다[18]. 제초제 트리플루설푸론메틸에도 G. parviflora 집단이 더 민감했다[18].\n\n"
  "두 종의 지상부 추출물을 함께 비교한 연구가 여럿 있다[12, 13, 14]. 활성 분획에서 파툴리트린·쿼시메리트린 등 플라보노이드와 카페오일 유도체가 검출되었다[12]. 질소 라디칼(NO·ONOO⁻) 소거 시험에서 가장 강한 활성은 G. quadriradiata의 물 추출물이었으므로, 이 수치를 별꽃아재비 값으로 인용하면 안 된다[14]. 같은 속의 G. ciliata는 한 연구에서 '비침입성 도입종'으로 다뤄져 침입종인 G. parviflora와 비교되었다[19]."},
 {"key": "cultivation", "title": "자생·재배", "body":
  "별꽃아재비는 재배 작물보다는 밭잡초로 더 많이 연구되었다[2, 18]. 종설은 이 속의 잡초가 토마토·고추·감자·콩·양파·양배추·밀·옥수수 등 여러 주요 작물 밭과 정원·빈터에 흔하다고 정리했다[2]. 유럽에서는 G. quadriradiata와 함께 채소 이랑 작물의 골칫거리 잡초로 꼽힌다[18]. 브라질 옥수수·콩 돌려짓기 시험에서는 무경운 재배 때 주요 활엽 잡초의 하나였다[25]. 불소 원자를 가진 4급 암모늄염 같은 새 제초 후보 물질의 효과를 시험하는 대상 잡초로도 쓰였다[26].\n\n"
  "이 종은 침입성 한해살이풀로 분류되며, 어미 식물이 겪은 질소·수분 조건이 자손의 형질에 미치는 영향(세대 간 가소성)을 본 연구의 대상이 되었다[19]. 체코 온실에서는 토마토반점위조바이러스(TSWV)에 자주 감염된 잡초였고, 바이러스를 옮기는 꽃노랑총채벌레의 좋은 기주였다[23]. 브라질에서는 담배가루이(Bemisia tabaci) B형의 기주가 되는 잡초 7종 가운데 하나로 시험되었다[24].\n\n"
  "연구용 시료는 대학 정원에서 기른 것을 6월에 거둬 실온에서 말려 쓴 예가 있다[3]. 국내에서의 재배 면적·생산량 통계와 자생 분포 자료는 이번 조사에서 확인하지 못함."},
 {"key": "processing", "title": "가공·제품", "body":
  "식품원료로는 잎과 줄기만 쓸 수 있으므로, 가공 원료도 이 두 부위로 한정된다[1]. 외국에서는 어린 순과 잎을 채소로 먹거나 샐러드·수프에 넣는다[2, 3]. 국내 시판 제품이나 생산실적 통계는 이번 조사에서 확인하지 못함.\n\n"
  "연구에서는 주로 지상부(herb)를 말려 추출물을 만든다[3, 13]. 폴란드 연구는 건조 지상부를 50% 메탄올로 95 °C 수욕에서 20분씩 두 번 추출해 썼고, 이 추출물의 총페놀은 건조 지상부 1 g당 클로로겐산 당량 98.30 ± 0.14 mg, 총플라보노이드는 퀘르세틴 당량 6.15 ± 0.41 mg이었다[3]. 같은 지상부라도 추출 용매에 따라 성질이 달라, 물 추출물은 사람 피부 섬유아세포를 자외선 손상에서 보호한 반면 에탄올 추출물은 세포독성을 보였다[13]. 질소 라디칼 소거 시험에서도 물 추출물이 에탄올 추출물보다 활성이 높았다[14].\n\n"
  "수증기 증류로 얻은 정유도 분석되었다[10, 11]. 콜롬비아산 잎 정유에서는 88종의 휘발 성분이 확인되었고, 주성분은 (Z)-3-헥센-1-올(21.7%)·6-데메톡시아게라토크롬(14%)·β-카리오필렌(12.4%)이었다[10]. 다른 연구의 정유에서는 37종이 확인되었고 (Z)-γ-비사볼렌이 38.9%로 가장 많았다[11]. 이처럼 정유 조성은 산지·시료에 따라 크게 다르다[10, 11]."},
 {"key": "genetics", "title": "유전·유전체", "body":
  "중국 쓰촨성에서 채집한 별꽃아재비의 엽록체 유전체 전체 서열이 2019년에 보고되었다[22]. 고리 모양 엽록체 유전체의 길이는 151,811 bp이며, 큰 단일복제 영역(LSC) 83,594 bp, 작은 단일복제 영역(SSC) 18,141 bp, 한 쌍의 역반복 영역(IR) 각 25,038 bp로 이루어진다[22]. 유전자는 모두 113종(단백질 암호 80, tRNA 29, rRNA 4)이며 그중 19종은 두 벌씩 있다[22]. 전체 GC 함량은 37.7%였다[22]. 국화과 39종의 엽록체 단백질 암호 서열로 최대가능도 계통수를 만들어 이 종의 위치를 제시했다[22]. 다만 자매군으로 나온 종의 이름은 PubMed 전문에서 학명 글자가 빠져 있어 확인하지 못함.\n\n"
  "같은 논문은 이 종이 중국 서남부 농경지의 침입 잡초이면서 약용·식용으로 쓰인다고 소개했다[22]. 별꽃아재비의 염색체 수·배수성과 핵 유전체 해독 자료는 이번 조사에서 확인하지 못함."},
 {"key": "safety", "title": "안전성·주의", "body":
  "식약처 「식품원료 목록」에서 별꽃아재비는 잎과 줄기만 식품원료로 쓸 수 있는 '사용가능' 원료이며, 고시형 원료가 아니어서 따로 정한 섭취 주의사항은 없다[1]. 국내 공공기관의 알레르기·잔류농약·독성 성분 정보는 이번 조사에서 확인하지 못함.\n\n"
  "종설에 따르면 랫드에 물 추출물을 한 번 먹인 급성 독성 시험에서 독성 반응이나 죽음이 없었고, 경구 5,000 mg/kg까지 비교적 안전하다고 판단되었다[2]. 에탄올 추출물은 MCF-7 세포에 0.1–100 µg/mL에서는 약한 독성만 보였으나, 1,000 µg/mL에서는 모든 세포를 죽였다[2, 4]. 지상부 에탄올 추출물은 사람 피부 섬유아세포에 세포독성을 보였다[13]. 반복 섭취 독성이나 사람 대상 안전성 자료는 확인하지 못함.\n\n"
  "가장 눈여겨볼 점은 중금속 축적이다[20]. 별꽃아재비는 겨울 밭잡초 가운데 카드뮴 초집적 식물로 선별되었고, 뿌리·지상부의 생물농축계수와 이행계수가 모두 1을 넘었다[20]. 토양 카드뮴 100 mg/kg 조건에서 지상부 카드뮴은 최대 137.63 mg/kg이었다[20]. 이 성질 때문에 카드뮴 오염 농경지를 정화하는 식물로 연구되고 있다[20, 21, 27, 28]. 이는 오염 토양에서 자란 잎·줄기를 먹을 경우 카드뮴 노출이 커질 수 있음을 시사하지만, 식용 부위의 중금속 실측 분포나 질산염 함량 자료는 이번 조사에서 확인하지 못함."},
]

compounds = [
 {"name": "Chlorogenic acid", "name_ko": "클로로겐산", "class": "페놀산(카페오일퀸산)", "role": "marker", "part": "지상부(건조, 50% 메탄올 추출물)", "content_text": "2.00 ± 0.01 mg/g(건조 지상부, UPLC)[3]", "activity_ko": "추출물 속 페놀산 가운데 가장 많은 성분[3]; 남미 허브 '과스카스'의 주요 페놀 성분으로도 보고[5]", "source": [3, 5]},
 {"name": "Protocatechuic acid", "name_ko": "프로토카테큐산", "class": "페놀산", "role": "bioactive", "part": "지상부(건조)", "content_text": "200.32 ± 4.3 µg/g(건조 지상부, UPLC)[3]", "activity_ko": "이집트산 추출물에서도 분리[4]", "source": [3, 4]},
 {"name": "Caffeic acid", "name_ko": "카페산", "class": "페놀산", "role": "bioactive", "part": "지상부(건조)", "content_text": "120.54 ± 2.8 µg/g(건조 지상부, UPLC)[3]", "activity_ko": "추출물의 질소 라디칼 소거 활성에 관여하는 성분으로 거론[14]", "source": [3, 14]},
 {"name": "4-Hydroxybenzoic acid", "name_ko": "4-하이드록시벤조산", "class": "페놀산", "role": "bioactive", "part": "지상부(건조)", "content_text": "100.43 ± 0.2 µg/g(건조 지상부, UPLC)[3]", "activity_ko": "", "source": [3]},
 {"name": "Isovanillic acid", "name_ko": "아이소바닐산", "class": "페놀산", "role": "bioactive", "part": "지상부(건조)", "content_text": "60.38 ± 1.6 µg/g(건조 지상부, UPLC)[3]", "activity_ko": "이 종에서 처음 검출되었다고 보고[3]", "source": [3]},
 {"name": "Patulitrin", "name_ko": "파툴리트린(파툴레틴-7-O-글루코사이드)", "class": "플라보놀 배당체", "role": "bioactive", "part": "지상부", "content_text": "분리·동정(함량 미보고)[3]; 항산화 활성 분획에서 검출[12]", "activity_ko": "", "source": [3, 12]},
 {"name": "Quercimeritrin", "name_ko": "쿼시메리트린(퀘르세틴-7-O-글루코사이드)", "class": "플라보놀 배당체", "role": "bioactive", "part": "지상부", "content_text": "분리·동정(함량 미보고)[3, 12]", "activity_ko": "", "source": [3, 12]},
 {"name": "Quercetagetrin", "name_ko": "퀘르세타게트린(퀘르세타게틴-7-O-글루코사이드)", "class": "플라보놀 배당체", "role": "bioactive", "part": "지상부", "content_text": "분리·동정(함량 미보고)[3]", "activity_ko": "", "source": [3]},
 {"name": "Miquelianin", "name_ko": "미켈리아닌(퀘르세틴-3-O-글루쿠로나이드)", "class": "플라보놀 배당체", "role": "bioactive", "part": "지상부", "content_text": "분리·동정(함량 미보고)[3]", "activity_ko": "", "source": [3]},
 {"name": "Rutin", "name_ko": "루틴", "class": "플라보놀 배당체", "role": "bioactive", "part": "지상부", "content_text": "분리·동정(함량 미보고)[3]", "activity_ko": "", "source": [3]},
 {"name": "Tricaffeoylaltraric acid", "name_ko": "트라이카페오일알타르산", "class": "카페산 유도체(알다르산 에스터)", "role": "bioactive", "part": "지상부", "content_text": "지상부의 주요 분리 성분 2종 가운데 하나(함량 초록에 없음)[15]", "activity_ko": "사람 피부 섬유아세포에서 UVA로 생긴 활성산소를 줄이고 Nrf2를 활성화(세포 실험)[15]", "source": [15]},
 {"name": "Dicaffeoylglucaric acid", "name_ko": "다이카페오일글루카르산", "class": "카페산 유도체(알다르산 에스터)", "role": "bioactive", "part": "지상부", "content_text": "지상부의 주요 분리 성분 2종 가운데 하나(함량 초록에 없음)[15]", "activity_ko": "UVA 조사 섬유아세포 보호(세포 실험)[15]", "source": [15]},
 {"name": "Galinsoside A", "name_ko": "갈린소사이드 A", "class": "플라바논 배당체", "role": "bioactive", "part": "아세트산에틸 가용 분획", "content_text": "신규 성분으로 분리(함량 미보고)[7]", "activity_ko": "항산화·우레아제 억제 활성(시험관)[7]", "source": [7]},
 {"name": "(Z)-gamma-Bisabolene", "name_ko": "(Z)-γ-비사볼렌", "class": "세스퀴테르펜", "role": "bioactive", "part": "정유", "content_text": "정유의 38.9%[11]", "activity_ko": "모기 6종 유충 살충 LC50 2.04–4.87 µg/mL, 산란 기피(실험실)[11]", "source": [11]},
 {"name": "beta-Caryophyllene", "name_ko": "β-카리오필렌", "class": "세스퀴테르펜", "role": "bioactive", "part": "잎 정유(콜롬비아산)", "content_text": "잎 정유의 12.4%[10]", "activity_ko": "", "source": [10]},
]

assays = [
 {"role": "literature", "compound": "Chlorogenic acid", "compound_ko": "클로로겐산", "part": "지상부(정원 재배, 6월 채취, 실온 건조)", "content": "2.00 ± 0.01 mg/g(건조 지상부)[3]",
  "method": "UPLC-PDA",
  "conditions": {"instrument": "Waters Acquity UPLC(PDA 검출기, Empower 2 소프트웨어)", "column": "Acquity UPLC HSS T3(1.8 µm, 2.1 × 150 mm, Waters) + 보호 칼럼 Acquity UPLC BEH C18(1.7 µm, 2.1 × 5 mm)",
   "mobile_phase": "(A) HPLC급 물, (B) HPLC급 아세토니트릴 — 각 1000 mL에 포름산 50 µL 첨가",
   "gradient": "0.0–4.0분 B 3→13%; 4.0–5.0분 13→17.5%; 5.0–9.0분 17.5%; 9.0–13.0분 17.5→3.0%",
   "flow": "0.275 mL/min", "temp": "24 °C", "detection": "PDA 234–330 nm 범위 수집(머무름 시간·스펙트럼 비교로 확인)", "injection": "2.0 µL(표준액)",
   "sample_prep": "건조 지상부 5.0 g을 50% 메탄올 250 mL로 95 °C 수욕 20분씩 2회 추출 → 40 °C 감압 건고 → 물 50 mL에 녹임(0.1 g 건조 지상부/mL) → 이 액 1.0 mL을 Oasis HLB Plus 카트리지(메탄올 5 mL·물 5 mL 활성화)에 걸고 70% 메탄올 50 mL로 용출 → 40 °C 감압 건고 → 메탄올-물(1:1) 2.0 mL → 0.2 µm GHP 필터",
   "standard": "클로로겐산 등 페놀산 표준품 1 mg/mL 메탄올 원액, 이동상 A로 5–40 µg/mL 작업액(각 농도 8회 주입)",
   "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "UPLC로 정량한 페놀산 5종 가운데 함량이 가장 높아 추출물의 주성분으로 제시되었다[3]. 전문(Methods) 확인 — 직선성·검출한계·정량한계 수치는 표에만 있어 본문에서 확인하지 못함; 회수율 수치도 확인하지 못함[3].",
  "source": [3], "url": "https://doi.org/10.3390/molecules23092133", "source_kind": "paper"},
 {"role": "literature", "compound": "(Z)-gamma-Bisabolene", "compound_ko": "(Z)-γ-비사볼렌", "part": "정유(부위는 초록에서 확인하지 못함)", "content": "정유의 38.9%[11]",
  "method": "GC·GC-MS",
  "conditions": {"instrument": "", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "", "injection": "", "sample_prep": "", "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "정유에서 확인된 37개 성분 가운데 가장 많은 성분이며, 모기 유충 살충 활성의 주성분으로 시험되었다[11]. 전문 확인 못함 — 분석 조건은 비워 둠[11].",
  "source": [11], "url": "https://doi.org/10.1007/s11356-018-1203-3", "source_kind": "paper"},
]

d = {"slug": "galinsoga-parviflora", "name_ko": "별꽃아재비", "name_en": "Gallant soldier", "scientific_name": "Galinsoga parviflora Cav.",
     "aliases": ["별꽃아재비잎", "별꽃아재비줄기", "Gallant soldier", "Quickweed", "Guascas", "small-flower galinsoga"],
     "sections": sections, "compounds": compounds, "markers": [], "assays": assays, "nutrients": [], "production": [], "world": [], "gi": [], "orgs": [], "sources": sources}
(P / "dossier.json").write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in sections: print(s["key"], len(s["body"]))
