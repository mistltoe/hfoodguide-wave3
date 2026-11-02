import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
A = "2026-11-02"
PMC = "https://pmc.ncbi.nlm.nih.gov/articles/{}/"
PM = "https://pubmed.ncbi.nlm.nih.gov/{}/"
src = [
 ("식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 망초(Conyza canadensis)·개망초(Erigeron annuus) 항목", "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "식품의약품안전처", "2026-10-13"),
 ("Conyza canadensis from Jordan: Phytochemical Profiling, Antioxidant, and Antimicrobial Activity Evaluation. Molecules. 2024", PMC.format("PMC11123705"), "MDPI (PMC)", A),
 ("Anxiolytic and Antidepressant-Like Effects of Conyza canadensis Aqueous Extract in the Scopolamine Rat Model. Plants (Basel). 2021", PMC.format("PMC8067281"), "MDPI (PMC)", A),
 ("Vasorelaxant Mechanism of Herbal Extracts from Mentha suaveolens, Conyza canadensis, Teucrium polium and Salvia verbenaca in the Aorta of Wistar Rats. Molecules. 2022", PMC.format("PMC9784123"), "MDPI (PMC)", A),
 ("Antifungal Activity and Composition of Essential Oils of Conyza canadensis Herbs and Roots. ScientificWorldJournal. 2012", PMC.format("PMC3353473"), "Hindawi (PMC)", A),
 ("Cytotoxic Effect of the Essential oils from Erigeron Canadensis L. on Human Cervical Cancer HeLa Cells in Vitro. Chem Biodivers. 2022 (초록)", PM.format("36005296"), "PubMed", A),
 ("Antiproliferative constituents of the roots of Conyza canadensis. Planta Med. 2011 (초록)", PM.format("21294076"), "PubMed", A),
 ("Chemical characteristics and significant antitussive effect of the Erigeron canadensis polyphenolic polysaccharide-protein complex. J Ethnopharmacol. 2021 (초록)", PM.format("34662663"), "PubMed", A),
 ("Anticoagulant and anti-platelet activity of polyphenolic-polysaccharide preparation isolated from the medicinal plant Erigeron canadensis L. Thromb Res. 2010 (초록)", PM.format("21172723"), "PubMed", A),
 ("Anti-inflammatory effect of methanol extract from Erigeron Canadensis L. may be involved with upregulation of heme oxygenase-1 expression and suppression of NFκB and MAPKs activation in macrophages. Nutr Res Pract. 2014", PMC.format("PMC4122705"), "Korean Nutrition Society (PMC)", A),
 ("Global gene analysis of Erigeron canadensis-treated TNF-alpha-, IL-4- and IL-1beta-stimulated A549 human epithelial cells. Ann Nutr Metab. 2009 (초록)", PM.format("19521071"), "PubMed", A),
 ("De novo genome assembly of the economically important weed horseweed using integrated data from multiple sequencing platforms. Plant Physiol. 2014 (초록)", PMC.format("PMC4226366"), "American Society of Plant Biologists (PMC)", A),
 ("A chromosome-scale draft sequence of the Canada fleabane genome. Pest Manag Sci. 2020 (초록)", PM.format("31951071"), "PubMed", A),
 ("Biology and management of two important Conyza weeds: a global review. Environ Sci Pollut Res Int. 2016 (초록)", PM.format("27798798"), "PubMed", A),
 ("Dynamic Seed Emission, Dispersion, and Deposition from Horseweed (Conyza canadensis (L.) Cronquist). Plants (Basel). 2022 (초록)", PMC.format("PMC9101336"), "MDPI (PMC)", A),
 ("Wind-mediated horseweed (Conyza canadensis) gene flow: pollen emission, dispersion, and deposition. Ecol Evol. 2015 (초록)", PMC.format("PMC4523360"), "Wiley (PMC)", A),
 ("High Levels of Glyphosate Resistance in Conyza canadensis from Agricultural and Non-Agricultural Sites in Ohio and Iowa. Sci Rep. 2018 (초록)", PMC.format("PMC6041346"), "Nature Portfolio (PMC)", A),
 ("Functional synergy and genomic linkage of glyphosate resistance traits in Canada fleabane. Pest Manag Sci. 2025 (초록)", PMC.format("PMC12713706"), "Wiley (PMC)", A),
 ("Population Genomics of a Cosmopolitan Weed Provides Insights Into Its Local Adaptation and Recent Demographic History. Mol Ecol. 2026 (초록)", PM.format("42159058"), "PubMed", A),
 ("Rapid and repeated evolution of increased competitive ability in a global invader. Nat Commun. 2026 (초록)", PMC.format("PMC13586298"), "Nature Portfolio (PMC)", A),
 ("Acquisition and evolution of enhanced mutualism—an underappreciated mechanism for invasive success? ISME J. 2022 (초록)", PMC.format("PMC9561174"), "Nature Portfolio (PMC)", A),
 ("Comparative chloroplast genomics of Erigeron (Asteroideae, Asteraceae). BMC Plant Biol. 2025 (초록)", PMC.format("PMC12512410"), "BioMed Central (PMC)", A),
 ("Transfer of glyphosate resistance: evidence of hybridization in Conyza (Asteraceae). Am J Bot. 2007 (초록)", PM.format("21636434"), "PubMed", A),
 ("Severe urticaria in a horse after consumption of horseweed (Conyza canadensis (L.) Cronquist) — A case study. Acta Vet Hung. 2025 (초록)", PM.format("40471695"), "PubMed", A),
 ("Accumulation of Heavy Metals in Conyza canadensis. Integr Comp Biol. 2024 (초록)", PM.format("39038995"), "PubMed", A),
 ("Integrative physiological and transcriptome analyses provide insights into the Cadmium (Cd) tolerance of a Cd accumulator: Erigeron canadensis. BMC Genomics. 2022 (초록)", PMC.format("PMC9703714"), "BioMed Central (PMC)", A),
 ("First Report of Leaf Spot on Horseweed (Conyza canadensis) Caused by Septoria erigerontis in Turkey. Plant Dis. 2010 (초록)", PM.format("30743574"), "PubMed", A),
 ("Optimization of Ultrasound-Assisted Extraction of Functional Food Fiber from Canadian Horseweed (Erigeron canadensis L.). ACS Omega. 2020 (초록)", PMC.format("PMC7450493"), "American Chemical Society (PMC)", A),
 ("The Korean herbal medicine, Do In Seung Gi-Tang, attenuates atherosclerosis via AMPK in high-fat diet-induced ApoE(-/-) mice. BMC Complement Altern Med. 2016 (초록)", PMC.format("PMC5016892"), "BioMed Central (PMC)", A),
]
sources = [{"n": i + 1, "title": t, "url": u, "publisher": p, "accessed": a} for i, (t, u, p, a) in enumerate(src)]

S = {}
S["overview"] = ("한눈에 보기",
"망초(Conyza canadensis (L.) Cronquist, 이명 Erigeron canadensis L.)는 국화과(Asteraceae)의 한해살이 또는 두해살이풀로, 영어로는 horseweed·Canadian fleabane이라 부른다[1][10]. 북아메리카가 원산이지만 지금은 북반구 곳곳에 퍼진 세계적인 잡초이자 침입 식물이다[19][20]. 이름이 비슷한 개망초(Erigeron annuus)는 다른 종이며, 「식품원료 목록」에도 따로 올라 있다[1].\n\n"
"식품의약품안전처 「식품원료 목록」에서 망초는 식품에 사용할 수 있는 원료(사용가능)이며, 사용 조건은 '사용가능부위 : 순, 잎'이다[1]. 목록에는 망초·망초순·망초잎의 3개 원료명과 망풀·큰망초라는 다른 이름이 함께 적혀 있다[1]. 건강기능식품 고시형 원료의 원재료로 쓰인다는 기록은 목록 자료에서 확인하지 못함.\n\n"
"지상부 정유는 리모넨이 주성분(헝가리 시료 79.2%)이고 뿌리 정유는 폴리아세틸렌인 마트리카리아 에스터가 대부분이다[5]. 잎·꽃의 추출물에서는 디카페오일퀸산 같은 페놀산과 로즈마린산, 아피제닌 배당체 등 플라보노이드가 정량되었다[2][4].")

S["history"] = ("역사와 전통적 이용",
"망초의 지상부와 뿌리는 여러 나라에서 설사·이질 같은 위장 증상과 이뇨에 쓰는 민간약 또는 공정 약초로 쓰였다고 정리되어 있다[5]. 중국 민간에서는 상처·부기와 관절염 통증에, 정유는 기관지염·방광염에 썼다는 기록이 소개된다[5]. 요르단 연구는 두통·치통·류머티즘·신장 질환·위장 질환·호흡기 감염과 상처·화상 치료에 지상부를 써 왔다고 적었다[2].\n\n"
"모로코에서는 위장 증상과 이뇨, 고혈압에 망초를 쓰며 잎과 꽃을 차로 우려 마신다고 보고되었다[3][4]. 한국 연구는 꽃이 핀 부분을 부종·혈뇨·간염·담낭염에 쓰는 민간약으로 소개했다[10]. 꽃 피는 부분에서 얻은 폴리페놀-다당 복합체가 기침·호흡기 질환에 쓰던 전통 용법을 뒷받침하는 연구 대상이 되었다[8].\n\n"
"한국 한의학 처방 도인승기탕을 다룬 연구는 구성 약재 하나를 Conyza canadensis로 표기했다[29]. 다만 이 처방의 '망초'가 식물 망초를 뜻하는지는 이번 조사에서 확인하지 못함. 망초가 한반도에 들어온 시기와 나물로 먹어 온 역사에 관한 공공기관 기록도 확인하지 못함.")

S["biology"] = ("식물학적 특징",
"망초는 털이 난 곧은 줄기가 1.5 m까지 자라고, 위쪽에서 가지를 쳐 작은 머리꽃이 많이 달린 꽃차례를 만든다[2]. 머리꽃은 흰색이나 연보라색의 혀꽃 고리와 노란 대롱꽃으로 이루어지며, 꽃은 봄부터 가을까지 핀다[2]. 겨울을 나는 한해살이 또는 두해살이로 자란다[10].\n\n"
"주로 제꽃가루받이를 하지만 다른 포기와도 꽃가루를 주고받는다[16]. 미국 일리노이 들판 조사에서 한 포기는 약 2.3×10⁶개의 꽃가루를 내놓았고, 꽃가루는 80–100 m 높이까지 올라갔다[16]. 씨는 바람에 날리며, 한 포기가 맺는 씨는 일리노이 122,178개, 테네시 94,146개로 추정되었다[15]. 씨 역시 80–100 m 높이에서 잡혀 먼 거리 이동이 가능함이 확인되었다[15].\n\n"
"원산지 밖 개체군은 원산지보다 포기가 크고 씨를 많이 맺었으며, 더 다양하고 서로 가까운 아버스큘러 균근균과 공생했다[21]. 원산지 100개와 침입지 165개 개체군을 비교한 온실 실험에서 침입지 개체군은 다른 종과의 경쟁력이 더 강했다[20]. 납·아연·구리를 몸에 쌓고, 카드뮴을 많이 축적하는 식물로도 보고되었다[25][26].")

S["related_species"] = ("가까운 종",
"망초는 처음 Erigeron canadensis L.로 이름 붙었다가 망초속(Conyza)으로 옮겨져, 지금은 두 학명이 함께 쓰인다[1][5]. 개망초속 25종의 엽록체 유전체 계통 분석에서 옛 망초속 종들은 개망초속 안에 묻혀 들어가, 두 속을 따로 나누기 어렵다는 결과가 나왔다[22]. 국내 「식품원료 목록」에서는 망초(Conyza canadensis)와 개망초(Erigeron annuus)가 서로 다른 종으로 올라 있고, 사용 부위도 망초는 순·잎, 개망초는 잎으로 다르다[1].\n\n"
"망초와 함께 큰 문제가 되는 잡초로 Conyza bonariensis가 있으며, 두 종은 생물학적 특징이 비슷해 여러 환경에 빠르게 적응한다[14]. 망초(2n = 18)는 같은 이배체인 C. ramosissima와 잡종을 만들 수 있는데, 꽃을 자유롭게 두었을 때 약 3%의 밑씨가 상대 종의 꽃가루로 수정되어 살아 있는 씨를 맺었다[23]. 이 잡종을 통해 글리포세이트 저항성 유전자가 다른 종으로 옮겨 갔다[23]. 국내에 자라는 큰망초·실망초 등과의 식별 기준은 이번 조사에서 확인하지 못함.")

S["cultivation"] = ("자생과 생산",
"망초는 재배 작물이 아니라 경작지·길가·빈터에 저절로 나는 잡초로 다뤄진다[14]. 콩·목화 같은 주요 밭작물에서 해마다 28–68%의 수량 손실을 일으키는 것으로 정리되었고, 경운을 하지 않는 보전 농업 밭에서 특히 많다[14]. 글리포세이트에 저항성이 생긴 첫 번째 넓은잎 잡초이며, 미국 오하이오에서는 2002년, 아이오와에서는 2011년에 저항성이 처음 보고되었다[12][17]. 2015년 조사에서 오하이오 농경지 개체는 거의 모두 표준 사용량의 40배에도 살아남았고, 농경지가 아닌 곳도 저항성 개체의 피난처가 되고 있었다[17].\n\n"
"망초의 잎에는 잎마름병균 Septoria erigerontis가 생기며, 이 병원균은 한국과 포르투갈의 망초에서도 보고되었다[27]. 원산지와 침입지를 아우른 280개 개체군 유전체 분석은 여러 차례의 유입과 사람에 의한 확산이 침입을 이끌었다고 보았다[19]. 국내 망초의 재배면적·생산량 공식 통계와 지리적 표시 등록은 이번 조사에서 확인하지 못함.")

S["processing"] = ("가공과 이용",
"국내에서 식용으로 쓸 수 있는 부위는 어린순과 잎이다[1]. 모로코에서는 잎과 꽃을 말려 차로 우려 마시며, 말린 잎·꽃 50 g을 물:메탄올(70:30) 500 mL에 24시간 담가 얻은 추출물의 수율은 28%였다[4]. 같은 지역 시료의 물 추출물도 수율이 28%였고, 카테킨과 플라보노이드가 많았다[3].\n\n"
"말린 꽃 피는 지상부를 증류하면 정유가 0.72% 나오고 뿌리는 0.20%에 그쳤다[5]. 요르단의 신선한 시료에서는 정유 수율이 잎 1.71%, 꽃차례 0.38%, 줄기 0.023%로 부위마다 크게 달랐다[2]. 정유는 사람 병원성 진균에 중간에서 강한 억제 작용을 보였지만 시험한 세균에는 효과가 없었다[5].\n\n"
"꽃 피는 부분에서는 뜨거운 알칼리 추출과 여러 단계 정제로 분자량 약 38,000 g/mol의 폴리페놀-다당-단백질 복합체를 얻는다[8]. 초음파 추출로 이 '기능성 식이섬유'를 얻으면 기존 방법보다 누적 에너지 요구량이 38% 적고 물 사용량은 6.6배 줄었다[28]. 국내 망초 가공식품·건강기능식품 생산실적은 확인하지 못함.")

S["genetics"] = ("유전체와 육종",
"망초는 염색체 수 2n = 2x = 18인 진정 이배체로, 유전체 크기가 약 335 Mb로 알려진 농업 잡초 가운데 가장 작다[12]. 2014년 여러 염기서열 분석 기술을 합쳐 잡초로는 처음으로 초안 유전체가 발표되었고, 단백질 암호 유전자 44,592개와 약 153 kb의 엽록체 유전체, 약 450 kb의 미토콘드리아 유전체가 조립되었다[12]. 2020년에는 426 Mb 조립의 98% 이상이 9개 염색체 수준 서열로 묶였고, ABC 수송체 159개, 사이토크롬 P450 352개, 당전이효소 181개 유전자가 확인되었다[13].\n\n"
"글리포세이트 저항성에는 표적 효소 EPSPS2의 P106S 돌연변이와, 액포 격리 등으로 추정되는 비표적 기작이 함께 작용하며, 두 기작이 같이 있으면 효과가 단순 합보다 두 배 넘게 커졌다[18]. 두 저항성 유전자 자리는 모두 4번 염색체에 있고 재조합 빈도 약 27%로 연결되어 함께 유전되기 쉽다[18]. 북반구 280개 개체군 분석에서 네 개의 유전 집단이 확인되었다[19]. 식용 목적의 육종 품종은 이번 조사에서 확인하지 못함.")

S["safety"] = ("안전성",
"망초에 대한 국내외 공공기관(식약처·EFSA 등)의 독성 평가나 알레르기·잔류 기준 정보는 이번 조사에서 확인하지 못함. 망초는 납·아연·구리를 몸에 쌓고 카드뮴 축적 식물로도 보고되어, 오염된 땅이나 길가에서 자란 개체는 중금속을 많이 담을 수 있다[25][26].\n\n"
"헝가리에서는 망초가 가장 많던 풀밭에서 풀을 뜯은 조랑말에게 심한 두드러기가 생겼고, 연구진은 세스퀴테르펜 락톤에 의한 과민반응을 의심했다[24]. 이 보고는 말 또는 다른 동물에 대한 망초의 독성·알레르기 가능성에 관해 이전 자료가 엇갈렸다고 적었다[24]. 지상부 정유는 자궁경부암 세포(HeLa)와 정상 간세포주(L02)의 생존율을 모두 크게 낮췄고, L02 세포가 덜 민감했다(시험관)[6].\n\n"
"한국 농촌진흥청이 제공한 지상부의 메탄올 추출물은 생쥐 대식세포에서 200 µg/mL까지 세포 독성이 없었고 염증 물질 생성을 줄였다(시험관)[10]. 망초 추출물은 사람 폐 상피세포(A549)에서도 염증·세포 부착 관련 유전자 발현을 낮췄다(시험관)[11]. 꽃 부분의 폴리페놀-다당 성분은 생체 내 항응고 작용과 혈소판 억제 작용을 보였다[9]. 사람이 먹었을 때의 임상시험과 임신·수유·항응고제 복용 중 섭취에 관한 공식 주의사항은 확인하지 못함.")

sections = [{"key": k, "title": v[0], "body": v[1]} for k, v in S.items()]

compounds = [
 {"name": "Limonene", "name_ko": "리모넨", "class": "모노테르펜", "role": "marker", "part": "지상부(꽃 피는 줄기) 정유",
  "content_text": "헝가리 지상부 정유의 79.2%(본문; 초록은 78%), 뿌리 정유는 약 1%[5]; 중국 지상부 정유 65.68%[6]; 요르단 꽃차례 정유 11.9%[2]",
  "activity_ko": "지상부 정유의 주성분으로, 같은 양의 리모넨 단독보다 정유 전체가 HeLa 세포를 더 강하게 억제했다(시험관)[6]", "source": [2, 5, 6]},
 {"name": "Matricaria ester", "name_ko": "마트리카리아 에스터", "class": "폴리아세틸렌", "role": "marker", "part": "뿌리·잎 정유",
  "content_text": "헝가리 뿌리 정유의 (2Z,8Z)-이성질체 88.2%·93.9%(두 시료)[5]; 요르단 신선 시료 정유의 (2,8)-이성질체 잎 60.7%, 줄기 31.6%, 꽃차례 15.4%[2]",
  "activity_ko": "뿌리 정유의 주성분이며 정유는 사람 병원성 진균에 억제 작용을 보였다(시험관)[5]", "source": [2, 5]},
 {"name": "Lachnophyllum ester", "name_ko": "라크노필룸 에스터", "class": "폴리아세틸렌", "role": "bioactive", "part": "꽃차례·줄기 정유",
  "content_text": "요르단 정유의 (Z)-라크노필룸 에스터 꽃차례 10.9%, 줄기 4.01%[2]", "activity_ko": "항균·항리슈마니아 작용이 연구된 폴리아세틸렌으로 소개됨[2]", "source": [2]},
 {"name": "Rosmarinic acid", "name_ko": "로즈마린산", "class": "페놀산(카페산 에스터)", "role": "marker", "part": "지상부 메탄올 추출물",
  "content_text": "요르단 시료 1441.1 mg/kg(초록은 식물 기준, 본문은 추출물 기준으로 표기)[2]; 모로코 메탄올 추출물에서는 검출되지 않았다고 인용됨[2]",
  "activity_ko": "추출물의 DPPH 소거능과 그람양성균 억제 작용의 주요 기여 성분으로 추정됨[2]", "source": [2]},
 {"name": "Caffeic acid phenethyl ester", "name_ko": "카페산 페네틸 에스터(CAPE)", "class": "페놀산 에스터", "role": "bioactive", "part": "지상부 메탄올 추출물",
  "content_text": "231.8 mg/kg[2]", "activity_ko": "이 종에서 처음 검출·정량되었다고 보고됨[2]", "source": [2]},
 {"name": "3,5-Dicaffeoylquinic acid", "name_ko": "3,5-디카페오일퀸산", "class": "페놀산(카페오일퀸산)", "role": "marker", "part": "잎·꽃 물:메탄올(70:30) 추출물",
  "content_text": "4.17 mg/g 건조 추출물(추출물의 주성분 페놀산)[4]", "activity_ko": "카페오일퀸산류는 추출물의 혈관 이완 작용(쥐 대동맥)에 일부 기여할 것으로 추정됨[4]", "source": [4]},
 {"name": "4,5-Dicaffeoylquinic acid", "name_ko": "4,5-디카페오일퀸산", "class": "페놀산(카페오일퀸산)", "role": "bioactive", "part": "잎·꽃 물:메탄올(70:30) 추출물",
  "content_text": "3.31 mg/g 건조 추출물[4]", "activity_ko": "3,5-디카페오일퀸산 다음으로 많은 페놀산[4]", "source": [4]},
 {"name": "Chlorogenic acid", "name_ko": "클로로겐산(5-O-카페오일퀸산)", "class": "페놀산(카페오일퀸산)", "role": "bioactive", "part": "잎·꽃 추출물",
  "content_text": "모로코 물:메탄올 추출물 2.68 mg/g 건조 추출물[4]; 요르단 메탄올 추출물에서는 미량[2]", "activity_ko": "모로코 물:메탄올 추출물에서 세 번째로 많은 페놀산[4]", "source": [2, 4]},
 {"name": "Apigenin 7-O-glucoside", "name_ko": "아피제닌 7-O-글루코사이드", "class": "플라본 배당체", "role": "bioactive", "part": "지상부 추출물",
  "content_text": "요르단 메탄올 추출물 46.13 mg/kg(검출된 플라보노이드 중 최다)[2]; 모로코 물 추출물에서도 확인됨(함량은 표에 있어 확인하지 못함)[3]",
  "activity_ko": "추출물의 항산화 작용에 기여하는 성분으로 언급됨[2]", "source": [2, 3]},
 {"name": "3-O-Methylquercetin", "name_ko": "3-O-메틸퀘르세틴", "class": "플라보놀", "role": "bioactive", "part": "지상부 메탄올 추출물",
  "content_text": "36.64 mg/kg[2]", "activity_ko": "이 종에서 처음 보고된 플라보노이드 가운데 하나[2]", "source": [2]},
 {"name": "Epicatechin", "name_ko": "에피카테킨", "class": "플라반-3-올", "role": "bioactive", "part": "잎·꽃 물 추출물",
  "content_text": "카테킨·에피카테킨이 주요 성분으로 정량됨(개별 함량은 표에 있어 확인하지 못함); 페놀산 합계 45.020 µg/mg 건조 추출물로 플라보노이드 분획의 3분의 1 미만[3]",
  "activity_ko": "물 추출물의 항산화·항불안 작용(쥐)과 관련된 성분으로 제시됨[3]", "source": [3]},
 {"name": "Nerolidol", "name_ko": "네롤리돌", "class": "세스퀴테르펜 알코올", "role": "bioactive", "part": "잎·줄기 정유",
  "content_text": "요르단 (E)-네롤리돌 잎 정유 3.67%, 줄기 정유 3.71%[2]", "activity_ko": "네트워크 약리 분석에서 HeLa 세포 억제의 주요 성분 후보로 예측됨[6]", "source": [2, 6]},
 {"name": "4Z,8Z-Matricaria-gamma-lactone", "name_ko": "4Z,8Z-마트리카리아 γ-락톤", "class": "폴리아세틸렌 락톤", "role": "bioactive", "part": "뿌리",
  "content_text": "뿌리 메탄올 추출물에서 분리(함량은 초록에서 확인하지 못함)[7]", "activity_ko": "새 디하이드로피라논(conyzapyranone A·B)과 함께 분리되어 항증식 작용이 평가됨[7]", "source": [7]},
 {"name": "Arabinogalactan", "name_ko": "아라비노갈락탄(폴리페놀-다당-단백질 복합체)", "class": "다당 복합체", "role": "bioactive", "part": "꽃 피는 부분",
  "content_text": "복합체(38,000 g/mol)는 페놀 13.2%, 단백질 16.3%, 우론산 6.3%(무게 %)이고 중성당은 갈락토스 41.0%, 아라비노스 24.1%, 글루코스 13.3%, 자일로스 12.1%[8]",
  "activity_ko": "기니피그에서 코데인에 가까운 진해 작용[8]; 다른 제제는 동물에서 항응고·혈소판 억제 작용[9]", "source": [8, 9]},
]

assays = [
 {"role": "literature", "compound": "Rosmarinic acid", "compound_ko": "로즈마린산(페놀 14종·플라보노이드 11종 동시 분석)", "part": "신선한 지상부 전체(요르단 야생, 2023년 가을 채취)",
  "content": "로즈마린산 1441.1 mg/kg, 카페산 페네틸 에스터 231.8 mg/kg, 아피제닌 7-O-글루코사이드 46.13 mg/kg, 3-O-메틸퀘르세틴 36.64 mg/kg[2]",
  "method": "UPLC-ESI-MS/MS",
  "conditions": {"instrument": "SciEx Exion UPLC + LC-ESI-MS/MS 4500 QTRAP (Analyst 1.7)", "column": "Phenomenex, 3.0 × 50 mm, 5 µm(고정상 이름은 본문에 없음)",
   "mobile_phase": "A: 5 mM 포름산암모늄 물:메탄올(95:5), B: 메탄올(1 mM 포름산)", "gradient": "0–8분 5→90% B, 8–12분 90% B, 12.01–15분 90→5% B",
   "flow": "0.35 mL/min", "temp": "30 ± 1 °C", "detection": "ESI 양·음이온 모드, 질소 분무·건조가스 60 psi, m/z 100–900", "injection": "5 µL",
   "sample_prep": "신선한 지상부 20 g을 메탄올 200 mL에 실온 24시간 담그기 3회 → 합쳐 55 °C 감압 농축(수율 7.63%)", "standard": "정품 표준물질 25종(페놀 14종, 플라보노이드 11종)",
   "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "25개 표준 성분 중 가장 많이 검출되어 추출물의 항산화·항균 작용을 설명하는 성분으로 제시되었다[2]. 함량 단위가 초록(식물 기준)과 본문(추출물 기준)에서 다르게 적혀 있고, 직선성·검출한계·회수율은 본문에 없어 비워 둠.",
  "source": [2], "url": PMC.format("PMC11123705"), "source_kind": "paper"},
 {"role": "literature", "compound": "3,5-Dicaffeoylquinic acid", "compound_ko": "3,5-디카페오일퀸산(카페오일퀸산 7종 동시)", "part": "잎·꽃(모로코 타우나트, 2018년 3–7월 채취, 그늘 건조)",
  "content": "3,5-디카페오일퀸산 4.17, 4,5-디카페오일퀸산 3.31, 5-O-카페오일퀸산 2.68 mg/g 건조 추출물; 확인된 페놀 합계 11.96 mg/g 건조 추출물[4]",
  "method": "HPLC-DAD",
  "conditions": {"instrument": "Gilson HPLC, Gilson 다이오드 배열 검출기(Unipoint 소프트웨어)", "column": "Spherisorb ODS2, 250 × 4.6 mm, 5 µm",
   "mobile_phase": "A: 물-포름산(19:1), B: 메탄올", "gradient": "5% B 시작 → 3분 15%, 13분 25%, 25분 30%, 35분 35%, 39분 45%, 42분 45%, 44분 50%, 47분 55%, 50분 70%, 56분 75%, 60분 80% B",
   "flow": "0.9 mL/min", "temp": "", "detection": "DAD, 200–400 nm UV 스펙트럼과 머무름 시간으로 동정", "injection": "20 µL",
   "sample_prep": "말린 잎·꽃 가루 50 g을 물:메탄올(70:30) 500 mL에 24시간 침지 → 여과·원심 → −20 °C 동결 후 동결건조(수율 28%)",
   "standard": "외부표준: 3-·4-·5-O-카페오일퀸산, 1,5-·3,4-·3,5-·4,5-디카페오일퀸산, 이소페룰산, 로즈마린산; 3회 반복", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "물:메탄올 추출물의 주성분 페놀산이 3,5-디카페오일퀸산이었고, 앞선 국화과 연구 결과와도 일치했다[4]. 칼럼 온도·직선성·검출한계·회수율은 본문에 없어 비워 둠.",
  "source": [4], "url": PMC.format("PMC9784123"), "source_kind": "paper"},
 {"role": "literature", "compound": "Epicatechin", "compound_ko": "에피카테킨(클로로겐산·루테올린·아피제닌 배당체 등 동시)", "part": "지상부(잎·꽃) 물 추출물(모로코 타우나트, 2017년 3–7월 채취)",
  "content": "카테킨·에피카테킨·루테올린과 그 배당체·아피제닌·아피제닌 7-O-글루코사이드·퀘르세틴 등이 정량됨; 페놀산 합계 45.020 µg/mg 건조 추출물(개별 값은 표에 있어 확인하지 못함)[3]",
  "method": "UHPLC-DAD",
  "conditions": {"instrument": "Thermo UltiMate 3000(4원 펌프·자동시료주입기·UV-DAD), Chromeleon 7.2", "column": "Phenomenex Luna Omega Polar C18, 100 Å, 150 × 4.6 mm(입자 크기는 본문에 없음)",
   "mobile_phase": "A: 0.1% 인산 함유 아세토니트릴, B: 1% 인산", "gradient": "A 0–10% 4분, 10–15% 4분, 다음 4분 유지(linear), 15분 동안 85%까지, 마지막 3분 10% A로 복귀",
   "flow": "0.8 mL/min", "temp": "", "detection": "280·330·520 nm 동시 기록", "injection": "10 µL",
   "sample_prep": "그늘 건조·분쇄한 지상부를 물로 추출해 동결건조(수율 28%) → 메탄올:물(3:1)에 4 mg/mL로 녹여 0.2 µm 필터 여과",
   "standard": "에피카테킨·카페산·로즈마린산·클로로겐산·엘라그산·루테올린·아피제닌·퀘르세틴-3-아라비노사이드·아피제닌-7-O-글루코사이드·루테올린-7-O-글루코사이드(0.114–0.195 mg/mL 원액, 2–10 µL 주입)",
   "linearity": "검량선 상관계수 0.9989 이상", "lod": "원문: 에피카테킨·클로로겐산의 LOD와 LOQ를 각각 280 ng/mL, 145 ng/mL로 계산(어느 값이 어느 항목인지 문장이 모호)", "loq": "위 LOD 칸과 같은 문장(280·145 ng/mL)", "recovery": ""},
  "rationale": "차처럼 우려 마시는 용법을 반영한 물 추출물에서 카테킨류와 플라보노이드가 주성분이어서 이를 정량했다[3]. 회수율·칼럼 온도는 본문에 없어 비워 둠.",
  "source": [3], "url": PMC.format("PMC8067281"), "source_kind": "paper"},
 {"role": "literature", "compound": "Limonene", "compound_ko": "리모넨(정유 34성분 동시)", "part": "꽃 피는 지상부·뿌리 정유(헝가리 세게드, 2009년 7월 채취, 실온 건조)",
  "content": "지상부 정유의 리모넨 79.2%(초록 78%), 뿌리 정유의 (2Z,8Z)-마트리카리아 에스터 88.2%·93.9%; 정유 수율 지상부 0.72%, 뿌리 0.20%[5]",
  "method": "GC-FID / GC-MS",
  "conditions": {"instrument": "HP 5890 Series II GC(FID); GC-MS는 Finnigan GCQ 이온트랩", "column": "HP-5 30 m × 0.35 mm × 0.25 µm(GC-FID); DB5MS 30 m × 0.25 mm × 0.25 µm(GC-MS)",
   "mobile_phase": "운반기체 N₂(GC-FID), He 선속도 31.9 cm/s(GC-MS)", "gradient": "60 → 210 °C(3 °C/min), 210 → 250 °C(5 °C/min, 2분 유지)",
   "flow": "", "temp": "주입구·검출기 250 °C", "detection": "FID; MS는 양이온 EI, m/z 40–400", "injection": "분할 주입(split)",
   "sample_prep": "건조 지상부 85.5 g을 유럽약전 6.0 방법으로 2시간 수증기 증류 → 무수 황산나트륨으로 건조·여과, −18 °C 보관",
   "standard": "머무름 시간·코바츠 지수와 문헌 MS 자료·라이브러리 비교, 정품 표준물질(Extrasynthese)로 확인", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "지상부 정유에서는 리모넨, 뿌리 정유에서는 마트리카리아 에스터가 주성분이어서 부위를 구별하는 지표가 된다[5]. 정량은 면적 백분율이며 검출한계·회수율은 본문에 없어 비워 둠.",
  "source": [5], "url": PMC.format("PMC3353473"), "source_kind": "paper"},
]

d = {"slug": "conyza-canadensis", "name_ko": "망초", "name_en": "Horseweed (Canadian fleabane)",
     "scientific_name": "Conyza canadensis (L.) Cronquist", "aliases": ["Erigeron canadensis L.", "망초순", "망초잎", "망풀", "큰망초", "horseweed", "Canadian fleabane", "Canada fleabane"],
     "sections": sections, "compounds": compounds, "markers": [], "assays": assays, "nutrients": [], "production": [], "world": [], "gi": [], "orgs": [], "sources": sources}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in sections: print(s["key"], len(s["body"]))
