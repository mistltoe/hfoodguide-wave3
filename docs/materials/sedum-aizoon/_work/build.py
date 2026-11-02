import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
A = "2026-11-02"
def pm(n, title, doi, note):
    return {"n": n, "title": f"{title} ({note})", "url": f"https://doi.org/{doi}", "publisher": "PubMed", "accessed": A}
sources = [
 {"n": 1, "title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 가는기린초잎(Sedum aizoon L. / Sedum aizoon var. typica Nakai., Aizoon stonecrop; 이명 가는잎기린초·꿩의 비름; 사용가능부위 : 잎, 사용가능); 같은 목록의 기린초(Sedum kamtschaticum Fisch. & Mey. / Sedum aizoon subsp. kamtschaticum Frod., 사용가능부위 : 잎)·돌나물순(Sedum sarmentosum Bunge, 사용가능부위 : 순)·경천(Sedum spectabile, 사용불가) 행 포함", "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
 pm(2, "Sedum aizoon L.: a review of its history, traditional uses, nutritional value, botany, phytochemistry, pharmacology, toxicology, and quality control — Front Pharmacol 2024;15:1349032", "10.3389/fphar.2024.1349032", "전문 PMC10972962, PMID 38549672"),
 pm(3, "Antimicrobial activity of flavonoids from Sedum aizoon L. against Aeromonas sp. in culture medium and in frozen pork — Food Sci Nutr 2019;7(10):3224-3232", "10.1002/fsn3.1178", "전문 PMC6804768, PMID 31660136"),
 pm(4, "Phytochemical Characterization and Bioactivity Evaluation of Extracts Obtained via Ultrasound-Assisted Extraction of Medicinal Plant Phedimus aizoon — Plants (Basel) 2024;13(14):1915", "10.3390/plants13141915", "전문 PMC11280400, PMID 39065442"),
 pm(5, "Characteristics chloroplast genome of Yangxincai and correction of its Latin scientific name — Mitochondrial DNA B Resour 2025;10(12):1237-1242", "10.1080/23802359.2025.2593156", "전문 PMC12667292, PMID 41333700"),
 pm(6, "Unraveling species diversification and niche separation in Phedimus kamtschaticus and P. aizoon using RAD-seq data and ecological niche modeling — Sci Rep 2026;16(1):2145", "10.1038/s41598-025-31925-y", "전문 PMC12808185, PMID 41366557"),
 pm(7, "Tu-San-Qi (Gynura japonica): the culprit behind pyrrolizidine alkaloid-induced liver injury in China — Acta Pharmacol Sin 2021;42(8):1212-1222", "10.1038/s41401-020-00553-9", "초록만 확인, PMID 33154553"),
 pm(8, "Computed tomography findings of hepatic veno-occlusive disease caused by Sedum aizoon with histopathological correlation — Braz J Med Biol Res 2015;48(12):1145-50", "10.1590/1414-431X20154563", "초록만 확인, PMID 26517336"),
 {"n": 9, "title": "[Clinical analysis of hepatic veno-occlusive disease induced by Sedum aizoon] — Zhongguo Zhong Yao Za Zhi 2008;33(20):2402-4 (초록만 확인, PMID 19157138)", "url": "https://pubmed.ncbi.nlm.nih.gov/19157138/", "publisher": "PubMed", "accessed": A},
 pm(10, "Chemical constituents from Sedum aizoon and their hemostatic activity — Pharm Biol 2014;52(11):1429-34", "10.3109/13880209.2014.895019", "초록만 확인, PMID 25026341"),
 pm(11, "New flavonoid glycosides from Sedum aizoon L. — Fitoterapia 2015;101:125-32", "10.1016/j.fitote.2014.12.014", "초록만 확인, PMID 25562804"),
 pm(12, "Two new prenylated isoflavones from Sedum aizoon L. — Fitoterapia 2011;82(3):405-7", "10.1016/j.fitote.2010.11.021", "초록만 확인, PMID 21112377"),
 pm(13, "New Adducts of Iriflophene and Flavonoids Isolated from Sedum aizoon L. with Potential Antitumor Activity — Molecules 2017;22(11):1859", "10.3390/molecules22111859", "초록만 확인, PMID 29099046"),
 pm(14, "Drought resistance mechanisms of Phedimus aizoon L. — Sci Rep 2021;11(1):13600", "10.1038/s41598-021-93118-7", "초록만 확인, PMID 34193957"),
 pm(15, "Moderate calcium stress improves antioxidant phytochemical quality of Phedimus aizoon L. through flavonoid and glutathione dual ROS-Ca2+ detoxification strategy — Front Plant Sci 2026;17:1737412", "10.3389/fpls.2026.1737412", "초록만 확인, PMID 42137207"),
 pm(16, "The regulatory effect of total flavonoids of Sedum aizoon L. on oxidative stress in type 1 diabetic mice — Curr Res Food Sci 2022;5:1140-1147", "10.1016/j.crfs.2022.06.010", "초록만 확인, PMID 35865805"),
 pm(17, "Effect of Sedum aizoon L. Powder Addition on the Rheological Properties and Gluten Structure Characteristics of Dough and the In Vitro Digestibility of Noodles — J Food Sci 2026;91(7):e71230", "10.1111/1750-3841.71230", "초록만 확인, PMID 42378029"),
 pm(18, "A Molecular Phylogenetic Study of the Genus Phedimus for Tracing the Origin of \"Tottori Fujita\" Cultivars — Plants (Basel) 2020;9(2):254", "10.3390/plants9020254", "초록만 확인, PMID 32079195"),
 pm(19, "[Interaction of Cd and Zn Affecting the Root Morphology and Accumulation of Heavy Metals in Sedum aizoon] — Huan Jing Ke Xue 2019;40(1):470-479", "10.13227/j.hjkx.201805055", "초록만 확인, PMID 30628307"),
 {"n": 20, "title": "[Chemical constituents from ethyl acetate extract of Sedum aizoon] — Zhong Yao Cai 2014;37(10):1792-5 (초록만 확인, PMID 25895385)", "url": "https://pubmed.ncbi.nlm.nih.gov/25895385/", "publisher": "PubMed", "accessed": A},
 pm(21, "A comparison of the growth status, rainfall retention and purification effects of four green roof plant species — J Environ Manage 2020;278(Pt 1):111451", "10.1016/j.jenvman.2020.111451", "초록만 확인, PMID 33120092"),
 pm(22, "Exposure to Gynura japonica (Thunb.) Juel plants induces hepatoxicity in rats and Buffalo rat liver cells — J Ethnopharmacol 2024;335:118692", "10.1016/j.jep.2024.118692", "초록만 확인, PMID 39151710"),
 pm(23, "Flavonoids from Sedum aizoon L. inhibit Botrytis cinerea by negatively affecting cell membrane lipid metabolism — Appl Microbiol Biotechnol 2022;106(21):7139-7151", "10.1007/s00253-022-12196-3", "초록만 확인, PMID 36201036"),
 {"n": 24, "title": "[Morphological and histological studies of herba sedum aizoon] — Zhong Yao Cai 2001;24(5):330-2 (초록만 확인, PMID 12587206)", "url": "https://pubmed.ncbi.nlm.nih.gov/12587206/", "publisher": "PubMed", "accessed": A},
]

sections = [
 {"key": "overview", "title": "한눈에 보기", "body":
  "가는기린초(Sedum aizoon L.)는 돌나물과의 여러해살이 다육 식물로, 식약처 「식품원료 목록」에는 '가는기린초잎'(영문 Aizoon stonecrop, 이명 가는잎기린초·꿩의 비름)으로 올라 있다[1]. 목록의 사용 조건은 '사용가능부위 : 잎'이고 상태는 사용가능이므로, 식품 원료로 쓸 수 있는 부위는 잎뿐이다[1]. 이 종을 원재료로 하는 건강기능식품 고시형 원료는 확인하지 못함. 최근 분류에서는 기린초속(Phedimus)으로 옮겨 Phedimus aizoon (L.) 't Hart로 부르는 경우가 많다[4, 6].\n\n"
  "중국에서는 '景天三七'이라는 이름으로 연한 줄기와 잎을 채소로 먹고, 뿌리와 전초를 지혈·안신 목적의 민간약으로 써 왔다[2]. 지금까지 플라보노이드·페놀산·트리테르펜·피토스테롤·알칼로이드 등 234가지가 넘는 대사물이 보고되었고, 그중 플라보노이드가 주요 성분으로 정리되었다[2]. 잎·줄기에서는 캠페롤·퀘르세틴·카테킨·루틴·이소퀘르시트린 등이 HPLC로 정량되었고, 지상부 추출물에서는 갈산이 가장 많은 페놀 성분이었다[3, 4]. 같은 목록의 기린초(S. kamtschaticum)·돌나물(S. sarmentosum)은 별도 원료이며, 이 자료에는 그 종들의 값을 섞지 않았다[1]."},
 {"key": "history", "title": "역사와 이용", "body":
  "중국에서 가는기린초는 명나라 때의 구황 식물서 「구황본초(救荒本草)」에 처음 실렸고, 이후 「야채박록(野菜博录)」·「식물명실도고(植物名实图考)」 등에도 올랐다[2]. 같은 기록은 연한 줄기와 잎을 늘 먹으면 혈액 순환을 돕고 마음을 안정시킨다고 적고 있어, 오래전부터 먹는 풀이자 약초로 함께 쓰였음을 보여 준다[2]. 전초와 시럽은 1977년판 「중국약전」(1부)에 수록되었고, 현재는 장쑤·푸젠성의 지방 약재 규격에 들어 있다고 정리되었다[2].\n\n"
  "민간에서는 전초와 뿌리를 어혈을 풀고 피를 멈추는 데 썼으며, 하루 60–90 g을 달여 객혈·코피·잇몸 출혈 등에 썼다는 기록이 소개되었다[2]. 심계항진·불면 같은 증상에 마음을 안정시키는 약으로도 쓰였다[2]. 중국 외에 러시아·몽골·일본·북한·멕시코에서도 먹는 식물로 쓰인다고 총설은 적고 있다[2]. 다만 이런 전통 용도는 기록일 뿐이며, 사람에서 효과가 확인된 것은 아니다[2]. 한국에서 가는기린초잎을 식재료로 쓴 역사 기록은 확인하지 못함."},
 {"key": "biology", "title": "식물학적 특징", "body":
  "가는기린초는 굵고 목질화된 뿌리줄기에서 줄기가 여러 개 곧게 서는 다육성 여러해살이풀로, 줄기는 원통형이며 털이 없고 높이 15–50 cm까지 자란다[2]. 잎은 길이 2.5–5 cm, 너비 5–12 mm의 거꿀달걀꼴 또는 긴 타원형으로 두툼하고 즙이 많으며, 끝 쪽 가장자리에 톱니가 있다[2]. 꽃은 여름에 피고 꽃잎 5장은 주황빛이 도는 노란색의 피침형이며, 수술은 10개, 심피는 5개다[2]. 열매는 별 모양으로 모여 달리는 골돌이고, 씨에는 가장자리를 따라 날개가 있다[2].\n\n"
  "기린초속 식물은 스스로 꽃가루받이를 하지 못하는 타가수분 식물이지만, 떨어진 잎·줄기 조각으로도 영양번식을 할 수 있다[6]. 가는기린초는 곧게 서는 키 큰 줄기와 피침형 잎으로, 기린초는 비스듬히 서는 줄기 여러 개와 거꿀달걀꼴 잎으로 구별해 왔으나 잎 모양 변이가 커서 둘을 헷갈리기 쉽다[6]. 가뭄 실험에서는 가뭄이 심해지면 잎의 왁스층이 두꺼워지고 탄소 고정이 C3에서 CAM 방식으로 바뀌는 반응을 보였다[14]. 뿌리·뿌리줄기·줄기·잎·꽃의 조직 특징을 정리한 생약학 연구도 있다[24]."},
 {"key": "related_species", "title": "이름과 가까운 종", "body":
  "식약처 목록에서 가는기린초잎의 학명은 'Sedum aizoon L. / Sedum aizoon var. typica Nakai.'로 적혀 있다[1]. 같은 목록의 '기린초'는 Sedum kamtschaticum Fisch. & Mey.이면서 이명으로 'Sedum aizoon subsp. kamtschaticum Frod.'가 함께 적혀 있어, 학명만 보면 두 원료가 겹쳐 보일 수 있다[1]. 한국 집단의 유전체 분석에서는 가는기린초와 기린초가 형태로는 잘 갈리지 않지만 유전적으로 서로 다른 무리를 이루었고, 일부 집단에서는 두 종 사이의 유전자 교류가 확인되었다[6].\n\n"
  "중국에서 '양심채(养心菜)'라는 이름으로 기르는 채소는 그동안 Sedum aizoon으로 불려 왔으나, 엽록체 유전체 분석 결과 가는기린초(모계)와 기린초 사이의 재배 잡종으로 밝혀졌다[5]. 따라서 '가는기린초'라는 이름의 영양·성분 자료 가운데 일부는 이 잡종을 대상으로 했을 수 있다[5]. 또 목록의 이명 '꿩의 비름'은 같은 목록의 사용불가 원료 '경천'(Sedum spectabile)의 이명 '큰꿩의비름'과 비슷하므로 이름만으로 판단하지 않는 것이 좋다[1]. 중국 이름 '토삼칠(土三七)'은 가는기린초와 국화과의 Gynura japonica를 함께 가리키기도 해 혼용 사고가 보고되었다[7]. 같은 속의 돌나물(S. sarmentosum)·흰꽃세덤(S. album)·돌채송화(S. japonicum) 등은 이 자료에 포함하지 않았다[1]."},
 {"key": "cultivation", "title": "재배와 산지", "body":
  "총설에 따르면 돌나물속(Sedum)은 약 600종이 북반구 온대·아열대에 퍼져 있고, 가는기린초는 중국·러시아·몽골·일본·북한 등에 분포한다[2]. 한국에서도 강원 평창 대관령 일대의 자생 집단이 유전체 분석에 쓰였다[6]. 기린초속은 유라시아의 바위 비탈과 초지에 사는 약 20종의 여러해살이풀로 이루어지며, 한반도에는 이 무리(가는기린초 아속)의 9종이 기록되어 있다[6]. 국내 재배 면적·생산량 통계는 확인하지 못함.\n\n"
  "중국 총설은 이 종이 해충이 거의 없어 재배 중 농약이 필요 없는 식물이라고 소개한다[2]. 화분 가뭄 실험에서는 가벼운 가뭄(최대 용수량의 55–60%)에서 30일 동안 정상적으로 자랐으나 심한 가뭄에서는 20일 뒤부터 생육이 억제되어, 토양 유효수분을 27% 아래로 낮추지 말 것을 권했다[14]. 칼슘 처리 실험에서는 중간 농도(30 mM)에서 생육이 가장 좋았고 총플라보노이드가 1.51배로 늘었다[15]. 건조에 강해 옥상녹화 식물로도 시험되었고, 여름 식생 피복률이 95%를 넘었다[21]."},
 {"key": "processing", "title": "가공과 이용", "body":
  "연한 줄기와 잎은 채소로 먹으며, 중국에서는 고유의 향과 맛 때문에 쿠키·젤리·차로도 만든다[2]. 총설은 연한 줄기·잎의 수분 87 g, 단백질 2.1 g, 지방 0.7 g, 탄수화물 8.0 g, 칼슘 315 mg, 철 3.2 mg, 비타민 C 90 mg을 인용했으나 기준량은 표에 적혀 있지 않다[2]. 잡종 채소 '양심채'를 다룬 논문도 가식부 100 g당 단백질 2.1 g, 칼슘 315 mg, 철 3.2 mg 같은 값을 인용하고 있어, 이 영양값이 어느 식물에서 나온 것인지는 확인하지 못함. 한국 국가표준식품성분표의 가는기린초 값은 확인하지 못함.\n\n"
  "가공 연구로는 잎·줄기 가루를 밀가루의 0–25% 대신 넣어 국수를 만든 실험이 있으며, 20% 첨가가 관능과 기능의 균형이 가장 좋았고 시험관 소화에서 저항전분이 49%에서 63%로 늘었다[17]. 잎·줄기 플라보노이드 추출물은 냉동 돼지고기의 미생물 증식을 늦췄고, 잿빛곰팡이(Botrytis cinerea)에 대한 최소억제농도는 1.500 mg/mL였다[3, 23]. 몽골산 지상부를 초음파로 메탄올 추출했을 때 수율은 건물 기준 16.56%였다[4]. 이 종으로 만든 건강기능식품 생산실적은 확인하지 못함."},
 {"key": "genetics", "title": "유전 정보", "body":
  "기린초속(Phedimus)은 분자·형태 연구에서 돌나물속(Sedum)과 다른 자매 속으로 확인되어, 가는기린초도 Phedimus aizoon으로 분류하는 흐름이 있다[6]. 기린초속의 ITS·psbA-trnH 계통수에서는 섬기린초(P. takesimensis)는 한 무리를 이뤘으나 가는기린초와 기린초는 계통수에 흩어져 나타났다[18]. 한국 7개 집단 80개체를 5,051개 SNP로 분석한 연구에서는 세 종이 뚜렷이 갈렸고, 가는기린초와 기린초 사이의 집단 분화 지수(FST)는 0.67–0.78이었다[6].\n\n"
  "같은 연구에서 대관령의 기린초 한 집단은 두 종의 혼합 유전자형을 보여, 두 종 사이에 잡종 형성이 일어난다는 근거가 되었다[6]. 생태적 지위 모형에서는 여름철 강수량과 기온 계절성이 두 종의 분포를 가르는 주요 요인이었다[6]. '양심채'의 엽록체 유전체는 151,666 bp, GC 함량 37.73%였고, 128개 유전자(단백질 84·tRNA 36·rRNA 8)가 주석되었으며, 계통 분석으로 가는기린초가 모계로 확인되었다[5]. 가는기린초 자체의 핵 유전체 해독 결과는 확인하지 못함."},
 {"key": "safety", "title": "안전성", "body":
  "식약처 목록에서 가는기린초는 잎만 사용 가능한 원료이므로 뿌리·뿌리줄기 같은 다른 부위는 식품 원료로 쓸 수 없다[1]. 식약처나 다른 공공기관의 알레르기·잔류농약 정보는 확인하지 못함. 중국 총설은 지나치게 많이 먹으면 복통·간 비대·간 기능 이상·복수를 보이는 간정맥폐쇄병이 생길 수 있다고 적었고, 뿌리 추출물에서 간독성 피롤리지딘 알칼로이드(세네시오닌 등)가 확인되었다는 보고를 인용했다[2]. 중국에서는 'Sedum aizoon'에 의한 간정맥폐쇄병 39명의 CT 소견과 41명의 문헌 사례가 보고되었다[8, 9].\n\n"
  "그러나 피롤리지딘 알칼로이드를 만드는 국화과의 Gynura japonica도 같은 '토삼칠'로 불리며, 이 식물이 알칼로이드가 없는 토삼칠(가는기린초)과 혼용되어 중국의 간정맥폐쇄 증후군의 절반 이상을 일으킨 것으로 정리되었다[7, 22]. 따라서 위 사례의 원인 식물이 실제로 가는기린초였는지는 초록만으로 확인하지 못함. 이 종은 카드뮴을 잘 빨아들여 수경재배에서 지상부 카드뮴이 133.0 mg/kg에 이르렀으므로, 오염 토양에서 자란 잎은 중금속에 주의해야 한다[19]. 추출물의 항균·혈당 개선 효과는 시험관·동물 실험 결과이며 사람에서 확인되지 않았다[3, 16]."},
]

compounds = [
 {"name": "Kaempferol", "name_ko": "캠페롤", "class": "플라보놀", "role": "marker", "part": "잎·줄기", "content_text": "잎·줄기 건조 분말 메탄올 추출액 233.196 ± 29.675 mg/L(HPLC)[3]", "activity_ko": "주요 플라보노이드; 지상부에서 분리된 성분으로도 보고됨", "source": [3, 10]},
 {"name": "Quercetin", "name_ko": "퀘르세틴", "class": "플라보놀", "role": "marker", "part": "잎·줄기; 지상부", "content_text": "잎·줄기 추출액 232.238 ± 31.812 mg/L(퀘르세틴 이수화물로는 234.093 ± 29.950 mg/L)[3]; 몽골산 지상부 메탄올 추출물 0.19 mg/g 추출물[4]", "activity_ko": "항산화 플라보노이드(시험관)", "source": [3, 4]},
 {"name": "Catechin", "name_ko": "카테킨", "class": "플라반-3-올", "role": "marker", "part": "잎·줄기", "content_text": "잎·줄기 추출액 233.372 ± 33.590 mg/L[3]; 몽골산 지상부 추출물에서는 검출되지 않음[4]", "activity_ko": "산지·추출법에 따라 검출 여부가 다름", "source": [3, 4]},
 {"name": "Rutin", "name_ko": "루틴", "class": "플라보놀 배당체", "role": "bioactive", "part": "잎·줄기", "content_text": "잎·줄기 추출액 228.174 ± 26.682 mg/L[3]; 몽골산 지상부 추출물에서는 검출되지 않음[4]", "activity_ko": "플라보놀 배당체", "source": [3, 4]},
 {"name": "Isoquercitrin", "name_ko": "이소퀘르시트린", "class": "플라보놀 배당체", "role": "bioactive", "part": "잎·줄기", "content_text": "잎·줄기 추출액 227.228 ± 25.468 mg/L[3]", "activity_ko": "퀘르세틴 3-글루코사이드", "source": [3]},
 {"name": "Trifolin", "name_ko": "트리폴린", "class": "플라보놀 배당체", "role": "bioactive", "part": "잎·줄기", "content_text": "잎·줄기 추출액 217.458 ± 17.900 mg/L[3]", "activity_ko": "캠페롤 배당체", "source": [3]},
 {"name": "Luteolin", "name_ko": "루테올린", "class": "플라본", "role": "bioactive", "part": "잎·줄기; 지상부", "content_text": "잎·줄기 추출액 117.911 ± 16.321 mg/L[3]; 지상부 추출물 0.12 mg/g 추출물[4]", "activity_ko": "100·30 µg/mL에서 응고 시간 단축(시험관·동물)", "source": [3, 4, 10]},
 {"name": "Gallic acid", "name_ko": "갈산", "class": "페놀산", "role": "marker", "part": "지상부(잎·순·꽃 혼합)", "content_text": "몽골산 지상부 메탄올 추출물 2.75 mg/g 추출물(정량 성분 중 최고)[4]", "activity_ko": "응고 시간 단축 성분으로 보고됨(시험관·동물)", "source": [4, 10]},
 {"name": "Vanillic acid", "name_ko": "바닐산", "class": "페놀산", "role": "bioactive", "part": "지상부", "content_text": "지상부 추출물 0.50 mg/g 추출물[4]", "activity_ko": "응고 시간 단축 성분으로 보고됨", "source": [4, 10]},
 {"name": "Caffeic acid", "name_ko": "카페산", "class": "페놀산", "role": "bioactive", "part": "지상부", "content_text": "지상부 추출물 0.13 mg/g 추출물[4]", "activity_ko": "항산화 페놀산", "source": [4, 10]},
 {"name": "Myricetin", "name_ko": "미리세틴", "class": "플라보놀", "role": "bioactive", "part": "지상부·잎·줄기", "content_text": "지상부·잎·줄기에서 보고됨[2, 20]; 몽골산 지상부 추출물에서는 검출되지 않음[4]", "activity_ko": "플라보놀", "source": [2, 4, 20]},
 {"name": "Myricetin 3-O-glucoside", "name_ko": "미리세틴-3-O-글루코사이드", "class": "플라보놀 배당체", "role": "bioactive", "part": "지상부", "content_text": "지상부 에탄올 추출물에서 분리(함량 수치 없음)[11]", "activity_ko": "HepG2·MCF-7·A549 세포에서 IC50 46.30·75.27·49.76 µmol/L(세포 실험)", "source": [2, 11]},
 {"name": "Sedacin A", "name_ko": "세다신 A", "class": "프레닐화 이소플라본", "role": "bioactive", "part": "전초", "content_text": "메탄올 추출물에서 새로 분리(함량 수치 없음)[12]", "activity_ko": "이 종에서 처음 보고된 이소플라본; 항산화 시험", "source": [2, 12]},
 {"name": "Iriflophenone", "name_ko": "이리플로페논", "class": "벤조페논", "role": "bioactive", "part": "지상부·뿌리줄기", "content_text": "에틸아세테이트 추출물에서 분리(함량 수치 없음)[20]; 뿌리에서 이리플로페논–플라보노이드 결합 화합물 4종 분리[13]", "activity_ko": "결합 화합물은 암세포주에서 IC50 24.84–37.22 µmol/L(세포 실험)", "source": [13, 20]},
 {"name": "Arbutin", "name_ko": "알부틴", "class": "페놀 배당체", "role": "bioactive", "part": "뿌리·잎·줄기", "content_text": "뿌리와 잎·줄기에서 보고됨(함량 수치 없음)[2]", "activity_ko": "히드로퀴논 배당체", "source": [2]},
 {"name": "Senecionine", "name_ko": "세네시오닌", "class": "피롤리지딘 알칼로이드", "role": "bioactive", "part": "뿌리(식품 사용 부위 아님)", "content_text": "뿌리 추출물에서 확인되었다는 보고가 총설에 인용됨(함량 수치 없음)[2]; 이 종은 피롤리지딘 알칼로이드를 만들지 않는다는 정리도 있음[7]", "activity_ko": "간독성 알칼로이드; 원 시료의 종 동정 확인하지 못함", "source": [2, 7]},
]

assays = [
 {"role": "literature", "compound": "Kaempferol; Quercetin; Catechin; Rutin; Isoquercitrin; Trifolin; Luteolin; Astragalin; Genistein; Lonicerin; Scutellarein; Isorhamnetin",
  "compound_ko": "캠페롤·퀘르세틴·카테킨·루틴·이소퀘르시트린·트리폴린·루테올린 등 13종 플라보노이드",
  "part": "잎·줄기(중국 저장성 닝보 대학 재배지, 55 °C 열풍 17시간 건조, 60 mesh)",
  "content": "추출액 농도: 캠페롤 233.196 ± 29.675, 퀘르세틴 232.238 ± 31.812, 카테킨 233.372 ± 33.590, 루틴 228.174 ± 26.682, 이소퀘르시트린 227.228 ± 25.468, 트리폴린 217.458 ± 17.900, 루테올린 117.911 ± 16.321 mg/L",
  "method": "HPLC-UV(254 nm)",
  "conditions": {"instrument": "HPLC 시스템(원문 표기 SYNAPT G2, Waters)", "column": "Agilent Zorbax XDB-C18, 4.6 × 150 mm, 5 µm", "mobile_phase": "A 메탄올, B 0.1% 포름산", "gradient": "0–5분 A 70→30%, 5–18분 A 30→10%", "flow": "0.8 mL/min", "temp": "25 °C", "detection": "254 nm", "injection": "10 µL", "sample_prep": "분말 1.0 g + 메탄올 25 mL, 25 °C 초음파 50분(400 W, 40 kHz) 3회, 6,950 g 10분 원심분리, 0.22 µm 여과", "standard": "각 표준품 메탄올 용액", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "식품 사용 부위인 잎이 포함된 잎·줄기에서 플라보노이드를 개별 정량한 연구로, 전문(Methods)에서 조건을 옮겼다[3]. 결과는 시료 g당이 아니라 추출액 mg/L로만 보고되었고, 본문(카테킨 232.238)과 표(카테킨 233.372) 값이 엇갈려 표 값을 따랐다; 직선성·검출한계·회수율은 원문에 없다[3].",
  "source": [3], "url": "https://doi.org/10.1002/fsn3.1178", "source_kind": "paper"},
 {"role": "literature", "compound": "Gallic acid; Vanillic acid; Quercetin; Caffeic acid; Luteolin; Kaempferol",
  "compound_ko": "갈산·바닐산·퀘르세틴·카페산·루테올린·캠페롤",
  "part": "지상부(잎·순·꽃 혼합; 몽골 후브스굴 2015년 8월 채집, 그늘 건조)",
  "content": "갈산 2.75, 바닐산 0.50, 퀘르세틴 0.19, 카페산 0.13, 루테올린 0.12, 캠페롤 0.06 mg/g 추출물(카테킨·미리세틴·루틴·헤스페리딘 불검출; 분석 1회)",
  "method": "HPLC-DAD",
  "conditions": {"instrument": "Agilent HPLC-DAD(G7117C)", "column": "INNO C18, 4.6 × 250 mm, 5 µm", "mobile_phase": "A 0.03% 인산 수용액, B 아세토니트릴", "gradient": "0분 A 90%, 15분 80%, 28분 60%, 36분 25%, 38분 90%, 50분 90%", "flow": "", "temp": "25 °C", "detection": "250 nm(바닐산), 280 nm(카페산·갈산), 360 nm(루테올린·퀘르세틴·캠페롤)", "injection": "5 µL", "sample_prep": "건조 분말 55 g + 메탄올 1 L, 초음파 추출 30회 반복(40 kHz, 1500 W; 15분 초음파·120분 정치), 45 °C 감압 농축 후 동결건조; 추출물을 메탄올에 녹여 주입", "standard": "갈산·바닐산·루테올린·퀘르세틴·카테킨·루틴·헤스페리딘·캠페롤·미리세틴 표준품", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "잎을 포함한 지상부 추출물에서 페놀산·플라보노이드를 정량했고 전문에서 조건을 옮겼다; 유속·검출한계·회수율은 원문에 없고 함량은 시료가 아닌 추출물 g당이다[4].",
  "source": [4], "url": "https://doi.org/10.3390/plants13141915", "source_kind": "paper"},
]

d = {"slug": "sedum-aizoon", "name_ko": "가는기린초", "name_en": "Aizoon stonecrop",
     "scientific_name": "Sedum aizoon L.",
     "aliases": ["가는기린초잎", "가는잎기린초", "꿩의 비름", "Aizoon stonecrop", "Phedimus aizoon", "Sedum aizoon var. typica", "景天三七"],
     "sections": sections, "compounds": compounds, "markers": [], "assays": assays,
     "nutrients": [], "production": [], "world": [], "gi": [], "orgs": [], "sources": sources}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in sections: print(s["key"], len(s["body"]))
