import json
from pathlib import Path
OUT = Path('/home/user/hfoodguide-wave3/docs/materials/mentha-rotundifolia/dossier.json')
PM = 'https://pubmed.ncbi.nlm.nih.gov/%s/'
A = '2026-11-02'
def pm(n, title, pmid, note):
    return {"n": n, "title": f"{title} ({note})", "url": PM % pmid, "publisher": "PubMed", "accessed": A}
sources = [
 {"n": 1, "title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 애플민트잎·애플민트잎추출물(Mentha rotundifolia / Mentha suaveolens Ehrh.; Apple mint, Round-leave mint), 사용가능, 사용가능부위: 잎; 위생용품(E코드) 애플민트잎 추출물, 복합원료(U코드) 애플민트향; 같은 속 박하·서양박하·녹양박하·베르가모트민트·콘민트·Curled mint·River mint 행 대조 (로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json)", "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
 pm(2, "Mentha suaveolens Ehrh. (Lamiaceae) Essential Oil and Its Main Constituent Piperitenone Oxide: Biological Activities and Chemistry. Molecules 2015;20(5):8605-33", "25985361", "PMID 25985361, PMC6272761, 전문 확인"),
 pm(3, "Polyphenolic Profiling, Quantitative Assessment and Biological Activities of Tunisian Native Mentha rotundifolia (L.) Huds. Molecules 2019;24(13):2351", "31247911", "PMID 31247911, PMC6650961, 전문 확인(표 수치는 본문에 없어 확인하지 못함)"),
 pm(4, "Multidisciplinary Approach to Determine the Optimal Time and Period for Extracting the Essential Oil from Mentha suaveolens Ehrh. Molecules 2015;20(6):9640-55", "26016551", "PMID 26016551, PMC6272612, 전문 확인"),
 pm(5, "Chromosome-scale assembly of apple mint (Mentha suaveolens). BMC Genom Data 2024;25(1):96", "39516760", "PMID 39516760, PMC11549836, 전문 확인"),
 pm(6, "A haplotype-resolved gap-free genome assembly provides novel insight into monoterpenoid diversification in Mentha suaveolens 'Variegata'. Hortic Res 2024;11(3):uhae022", "38469381", "PMID 38469381, 초록"),
 pm(7, "Phytophotodermatose à la Mentha rotundifolia [Phytophotodermatitis due to Mentha rotundifolia]. Pan Afr Med J 2014;18:192", "25419319", "PMID 25419319, PMC4237575, 전문(증례 이미지 글) 확인"),
 pm(8, "Genotoxicity assessment of piperitenone oxide: An in vitro and in silico evaluation. Food Chem Toxicol 2017;106(Pt A):506-13", "28606765", "PMID 28606765, 초록"),
 pm(9, "Composition and chemical variability of Mentha suaveolens ssp. suaveolens and M. suaveolens ssp. insularis from Corsica. Chem Biodivers 2010;7(4):1002-8", "20397217", "PMID 20397217, 초록"),
 pm(10, "Antibacterial and antifungal activity of essential oils of Mentha suaveolens. Phytother Res 2002;16(8):727-31", "12458474", "PMID 12458474, 초록"),
 pm(11, "Chemical composition of the essential oil and botanical study of the flowers of Mentha suaveolens. Pharm Biol 2014;52(6):688-97", "24824321", "PMID 24824321, 초록"),
 pm(12, "Antimicrobial activity against beneficial microorganisms and chemical composition of essential oil of Mentha suaveolens ssp. insularis grown in Sardinia. J Food Sci 2014;79(3):M369-77", "24506214", "PMID 24506214, 초록"),
 pm(13, "In vitro inhibition of herpes simplex virus type 1 replication by Mentha suaveolens essential oil and its main component piperitenone oxide. Phytomedicine 2014;21(6):857-65", "24629600", "PMID 24629600, 초록"),
 pm(14, "Beneficial effect of Mentha suaveolens essential oil in the treatment of vaginal candidiasis assessed by real-time monitoring of infection. BMC Complement Altern Med 2011;11:18", "21356078", "PMID 21356078, 초록"),
 pm(15, "Pharmacological properties of the methanol extract from Mentha suaveolens Ehrh. Phytother Res 2002;16 Suppl 1:S10-3", "11933132", "PMID 11933132, 초록"),
 pm(16, "The in vitro screening for acetylcholinesterase inhibition and antioxidant activity of medicinal plants from Portugal. J Ethnopharmacol 2006;108(1):31-7", "16737790", "PMID 16737790, 초록"),
 pm(17, "Anti-Thermal Skin Aging Activity of Aqueous Extracts Derived from Apple Mint (Mentha suaveolens Ehrh.) in Human Dermal Fibroblasts. Evid Based Complement Alternat Med 2018;2018:4595982", "30254686", "PMID 30254686, PMC6142777, 전문 확인"),
 pm(18, "Protective Effects of Aqueous Extract of Mentha suaveolens against Oxidative Stress-Induced Damages in Human Keratinocyte HaCaT Cells. Evid Based Complement Alternat Med 2019;2019:5045491", "31662774", "PMID 31662774, 초록"),
 pm(19, "Mentha rotundifolia (L.) Huds. aqueous extract attenuates H2O2 induced oxidative stress and neurotoxicity. Front Neurosci 2023;17:1121029", "36968491", "PMID 36968491, 초록"),
 pm(20, "Mentha rotundifolia (L.) Huds. and Salvia officinalis L. hydrosols mitigate aging related comorbidities in rats. Front Aging Neurosci 2024;16:1365086", "38464467", "PMID 38464467, 초록"),
 pm(21, "Selenium Nanoparticles (Se-NPs) Alleviates Salinity Damages and Improves Phytochemical Characteristics of Pineapple Mint (Mentha suaveolens Ehrh.). Plants (Basel) 2022;11(10):1384", "35631809", "PMID 35631809, 초록"),
 pm(22, "Discrimination of Mentha species grown in different geographical areas of Algeria using 1H-NMR-based metabolomics. J Pharm Biomed Anal 2020;189:113430", "32615341", "PMID 32615341, 초록"),
 pm(23, "Characterization, activities, and ethnobotanical uses of Mentha species in Morocco. Heliyon 2020;6(11):e05480", "33294657", "PMID 33294657, 초록"),
 pm(24, "Essential Oil Composition and Physiology of Three Mentha Genotypes Under Shaded Field Conditions. Plants (Basel) 2024;13(22):3155", "39599364", "PMID 39599364, 초록"),
 pm(25, "Chemical Composition and Anti-Candida Activity of Mentha suaveolens Ehrh. Essential Oils Obtained by Different Distillation Processes. Molecules 2023;28(19):6934", "37836777", "PMID 37836777, 초록"),
 pm(26, "Phytochemical analysis and evaluation of antimicrobial, antioxidant, and antidiabetic activities of essential oils from Moroccan medicinal plants: Mentha suaveolens, Lavandula stoechas, and Ammi visnaga. Biomed Pharmacother 2023;164:114937", "37267633", "PMID 37267633, 초록"),
 pm(27, "Chemical Composition and Bioinsecticidal Effects of Thymus, Origanum and Mentha suaveolens Ehrh. Essential Oils on Medfly and Tomato Leaf Miner. Plants (Basel) 2022;11(22):3084", "36432812", "PMID 36432812, 초록(제목의 종명 일부는 초록에서 확인하지 못함)"),
 pm(28, "The heredity of the essential oil composition in artificial hybrids between Mentha rotundifolia and Mentha longifolia. Planta Med 1972;21(4):421-5", "5074051", "PMID 5074051, 서지 정보만(초록 없음)"),
 pm(29, "A new method for microwave assisted ethanolic extraction of Mentha rotundifolia bioactive terpenoids. Electrophoresis 2018", "29656406", "PMID 29656406, 초록"),
 pm(30, "Cardiovascular effects of the methanol and dichloromethanol extracts from Mentha suaveolens Ehrh. Phytother Res 2001;15(5):447-8", "11507742", "PMID 11507742, 초록"),
 pm(31, "Vasorelaxant Mechanism of Herbal Extracts from Mentha suaveolens, Conyza canadensis, Teucrium polium and Salvia verbenaca in the Aorta of Wistar Rats. Molecules 2022;27(24):8752", "36557886", "PMID 36557886, 초록"),
 pm(32, "Chemical characterization and insecticidal properties of essential oils from different wild populations of Mentha suaveolens subsp. timija (Briq.) Harley from Morocco. Chem Biodivers 2015;12(5):823-31", "26010669", "PMID 26010669, 초록"),
 pm(33, "Integrated Evaluation of Mentha rotundifolia (L.) Huds Essential Oil: Physicochemical Characterization, Antibacterial Effect and In Silico ADMET Prediction. Int J Mol Sci 2026;27(8):3527", "42074170", "PMID 42074170, 초록"),
 pm(34, "Systematics study through scanning electron microscopy; a tool for the authentication of herbal drug Mentha suaveolens Ehrh. Microsc Res Tech 2019;83(1):81-7", "31625657", "PMID 31625657, 초록"),
 pm(35, "Bioindication of heavy metals with aquatic macrophytes: the case of a stream polluted with power plant sewages in Poland. J Toxicol Environ Health A 2001;62(1):57-67", "11205536", "PMID 11205536, 초록"),
 pm(36, "Anti-breast cancer activity of the essential oil from grapefruit mint (Mentha suaveolens × piperita). Fitoterapia 2024;174:105875", "38417678", "PMID 38417678, 초록"),
 {"n": 37, "title": "농림축산식품부 「2024 특용작물 생산실적」 — 기호작물 '박하'(종 구분 없음) 2024년 농가 수·면적·생산량 (로컬 파싱본 docs/stats/special_crops_2024.csv)", "url": "https://www.mafra.go.kr", "publisher": "농림축산식품부", "accessed": A},
]
# fix title of 27: avoid guessing genera
sources[26]["title"] = "Chemical Composition and Bioinsecticidal Effects of three Lamiaceae essential oils including Mentha suaveolens Ehrh. on Medfly and Tomato Leaf Miner. Plants (Basel) 2022;11(22):3084 (PMID 36432812, 초록)"

S = {}
S['overview'] = ("애플민트는 꿀풀과 박하속(Mentha)의 여러해살이 향초로, 잎이 둥글고 주름지며 털이 많고 달콤한 향이 난다[2]. "
"식약처 「식품원료 목록」에는 '애플민트잎'과 '애플민트잎추출물' 두 행이 학명 Mentha rotundifolia / Mentha suaveolens Ehrh., 영문명 Apple mint·Round-leave mint로 올라 있고, 둘 다 '사용가능'이며 사용 조건은 '사용가능부위 : 잎'이다[1]. "
"따라서 이 목록에서 식품원료로 쓸 수 있는 부위는 잎이며, 줄기·꽃·뿌리는 사용 가능 부위로 확인하지 못함. "
"같은 목록의 위생용품(E코드)에는 '애플민트잎 추출물'(구분 1·2·3종)이, 복합원료(U코드)에는 '애플민트향'이 '사용가능'으로 있으나, 건강기능식품 고시형 원료의 원재료로 올라 있지는 않다[1].\n\n"
"잎 정유의 대표 성분은 피페리테논 옥사이드(로툰디폴론)로, 모로코 Azrou 시료에서 74.69%, 이탈리아 타르퀴니아 야생 시료의 첫 1시간 분획에서 87.25%를 차지했다[2, 4]. "
"다만 산지와 아종에 따라 풀레곤·피페리테논·카르본이 주성분인 화학형도 보고되어 정유 조성의 편차가 크다[2, 11, 12]. "
"잎 추출물에는 로즈마린산·카페산·루테올린 배당체 같은 폴리페놀이 들어 있다[3].")
S['history'] = ("애플민트는 남유럽·서유럽이 원산으로 북쪽으로 네덜란드까지 자라며, 텃밭 향초로 재배되다가 유럽 북부·중부에 귀화했다[2]. "
"지중해 지역 전통 의학에서는 혈압을 낮추고 위를 돕고 가스를 빼며 경련을 누그러뜨리는 약초로 쓰였고, 기침·메스꺼움·식욕부진·기관지염, 소화 문제, 독감, 류머티즘, 피부병에도 쓰였다고 정리되어 있다[2]. "
"포르투갈 내륙에서는 조미료로 쓰는 식물로 소개되었고[16], 모로코에서는 고혈압·당뇨·감염병에 쓰는 민간 약초로 보고되었다[26, 31]. "
"모로코 7개 지역의 민족식물 조사에서도 박하속 식물이 널리 쓰였다[23]. "
"애플민트는 관상용과 요리용 허브로 쓰이지만 상업적으로 대량 재배되는 일은 드물다[5].\n\n"
"20세기 중반부터 유럽에서 화학분류 연구가 이어졌고, 1972년에는 M. rotundifolia와 M. longifolia의 인공 잡종에서 정유 조성이 어떻게 유전되는지 다룬 논문이 나왔다[28]. "
"근래에는 정유의 항균·항진균 작용[10, 14], 단순포진바이러스 억제[13], 세포 산화 스트레스 보호[17, 18] 같은 시험관·세포 연구와 설치류 연구[15, 19, 20]가 주로 이루어졌다. "
"사람을 대상으로 한 임상시험은 이번 조사에서 확인하지 못함. "
"국내에 언제 들어와 재배되기 시작했는지도 확인하지 못함.")
S['biology'] = ("애플민트는 높이 100 cm까지 자라는 여러해살이풀로, 줄기는 네모지고 곧게 서며 털이 드문드문하거나 흰 솜털로 빽빽이 덮인다[2]. "
"잎은 마주나고 주름지며 잎자루가 없거나 아주 짧고, 길이 3–4.5 cm·너비 2–4 cm의 달걀꼴~거의 둥근꼴로 가장자리에 톱니가 10–20개 있고 대개 회색·흰 솜털로 덮인다[2]. "
"꽃줄기 밑동의 잎겨드랑이에서 땅속으로 기는가지가 뻗어 뿌리를 내리고 새 싹을 올리며, 길이 4–9 cm의 이삭 모양 꽃차례에 흰색 또는 분홍색 꽃이 촘촘히 달린다[2]. "
"개울가·습지 같은 축축한 곳에서 흔히 자란다[2].\n\n"
"박하속은 꽃차례 모양으로 세 계열로 나누는데, 애플민트는 이삭꽃차례를 가진 spicatae 계열에 든다[2, 4]. "
"정유는 잎의 샘털(선모)에서 만들어지며, 박하 정유의 유형은 카르본 경로·멘톨 경로·리날로올 경로 가운데 어느 쪽이 우세한지로 나뉜다[2, 5]. "
"피페리테논 옥사이드가 많은 애플민트는 카르본 경로 쪽 성분이 발달한 것으로 해석된다[4]. "
"파키스탄 북부 시료로는 줄기·잎·꽃의 미세형태, 꽃가루, 기공·표피세포·털 같은 해부 형질을 정리해 생약 감별 기준을 제시한 연구가 있다[34]. "
"이집트에서 재배한 꽃의 정유 수율은 건조 중량 기준 1.7%였다[11].")
S['related_species'] = ("식약처 목록은 애플민트의 학명을 Mentha rotundifolia와 Mentha suaveolens Ehrh.로 함께 적는다[1]. "
"튀니지 연구는 M. rotundifolia (L.) Huds.를 M. longifolia와 M. suaveolens 사이의 잡종으로 설명하면서 M. suaveolens의 이명으로 다뤄져 왔다고 적었고[3], 알제리 연구는 같은 식물을 Mentha × rotundifolia (L.) Huds.로 표기했다[22]. "
"그래서 문헌의 'M. rotundifolia'는 애플민트 자체를 가리키기도 하고 그 잡종을 가리키기도 하므로, 자료마다 학명 표기를 확인해야 한다[3, 22].\n\n"
"코르시카에는 subsp. suaveolens와 섬 고유 아종 subsp. insularis가 함께 자라며, 정유 조성으로 두 아종을 구분할 수 있었다[9]. "
"모로코 고유 아종 subsp. timija의 정유는 멘톤·풀레곤·피페리톤 에폭사이드가 주성분이었다[32]. "
"스피어민트(녹양박하)는 이배체인 M. longifolia와 애플민트의 교잡에서 생겼고, 서양박하는 여기에 팔배체 워터민트가 더해진 잡종이다[5]. "
"그레이프프루트민트(M. suaveolens × piperita)는 별도의 잡종으로 정유 주성분이 리날로올과 리날릴 아세테이트여서 애플민트와 다르다[36]. "
"식약처 목록에서 박하·서양박하·녹양박하·베르가모트민트·콘민트는 각기 다른 학명으로 따로 올라 있고, 콘민트(M. arvensis)의 영문명에 'Golden Apple Mint'가 들어 있어 이름만 보고 섞지 않도록 주의해야 한다[1].")
S['cultivation'] = ("한국에서 연구용으로 쓰인 애플민트 잎은 제주도 양토에서 1년 기른 뒤 5–7월에 거둔 것이었다[17]. "
"이탈리아 타르퀴니아의 야생 군락은 해마다 밭을 갈아엎어 식물 나이가 1년이 안 되었고, 생체 기준 정유 수율은 8월 0.19%, 9월 0.18%로 7월(0.07%)의 2.5배가 넘었다[4]. "
"반면 피페리테논 옥사이드 비율은 7월 시료에서 가장 높아, 많은 양을 얻으려면 8월, 이 성분을 원하면 7월이 유리했다[4].\n\n"
"독일 포장에서 'Apfelminze'를 포함한 박하 3개 유전형을 2년간 기른 시험에서 50% 차광은 키와 정유 함량을 높였지만 생물량은 차광하지 않은 쪽이 더 많았다[24]. "
"파인애플민트로 불린 M. suaveolens는 염화나트륨 90 mM의 심한 염 스트레스에서 생체중이 16.40%, 키가 19.10% 줄었고, 셀레늄 나노입자 10 mg/L 엽면 살포는 생육을 도왔다[21]. "
"모로코 아종 timija는 자생지 해발고도에 따라 정유 수율(0.20–1.17%)과 조성이 달랐다[32]. "
"농림축산식품부 특용작물 생산실적의 '박하' 항목은 종을 구분하지 않으며 2024년 전국 12농가·2.0 ha였다[37]. "
"애플민트만의 국내 재배 면적·생산량 통계는 확인하지 못함.")
S['processing'] = ("박하속 식물의 잎은 허브차와 향신 재료로 흔히 쓰이고[2], 포르투갈에서 애플민트는 조미료로 쓰이며 그 달인 물은 마른 식물 5 mg/mL에서 아세틸콜린에스터레이스를 69% 억제했다[16]. "
"제주산 잎은 50 °C 열풍으로 말려 가루 200 g을 80 °C 물 2 L로 추출한 뒤 동결건조해 화장품 소재 연구에 썼다[17].\n\n"
"정유는 지상부를 물로 증류해 얻는다[4]. "
"타르퀴니아 시료에서 피페리테논 옥사이드는 증류 시작 후 첫 3시간 분획에 많았고 6–24시간 분획에서는 크게 줄거나 사라져, 활성을 원하면 증류를 3시간 이내로 하라고 권했다[4]. "
"이탈리아 시료 112개를 비교한 연구에서는 물 증류가 수증기 증류보다 수율이 높고 피페리테논 옥사이드도 많았으며, 수증기 증류에서는 피페리테논과 리모넨 비율이 높았고 말린 원료가 kg당 정유가 더 많았다[25]. "
"마이크로파 보조 에탄올 추출은 100 °C·5분, 마른 시료 1.125 g당 용매 10 mL가 최적이었고 피페리테논 옥사이드와 피페리테논이 주성분이어서 식품 보존제 후보로 제시되었다[29]. "
"정유 증류 뒤 남는 방향수(하이드로졸)도 동물 시험 재료로 쓰였다[20]. "
"국내 가공식품 생산 통계에서 애플민트 품목은 확인하지 못함.")
S['genetics'] = ("한 연구진은 애플민트 한 클론의 유전체를 PacBio 장독 서열(103배)과 Chicago·Hi-C 라이브러리, 유전 지도로 조립했다[5]. "
"초록은 전체 536 Mb 중 98.45%가 큰 슈퍼스캐폴드 12개에 들어가고 N50이 44.7 Mb라고 했고, 본문은 염색체 스캐폴드 12개·N50 47 Mb·전체 526 Mb로 적어 수치가 조금 다르다[5]. "
"BUSCO 완전성은 97.8%였고, 여러 조직의 RNA-seq으로 전사체 111,426개를 예측했으며, 이 클론은 이형접합성이 높은 이배체였다[5]. "
"이 유전체는 스피어민트·서양박하 정유의 기원을 밝히는 기준 자료로 쓰인다[5].\n\n"
"중국 연구진은 원예 품종 M. suaveolens 'Variegata'에서 틈 없는 414.3 Mb 유전체와 단백질 암호 유전자 31,251개를 얻었고, 이형접합도 1.5%를 바탕으로 401.9 Mb·405.7 Mb의 두 하플로타입을 따로 조립했다[6]. "
"이 품종은 멘톨이 아니라 피페리테논 옥사이드를 주로 만들었고, 멘톨 합성의 핵심 효소인 아이소피페리테논 환원효소 유전자 3개의 전사량이 낮은 것이 원인으로 제시되었다[6]. "
"코르시카 59개체의 정유를 주성분 분석한 결과 세 무리로 나뉘어 아종 구분에 정유 조성이 쓰일 수 있음을 보였다[9]. "
"알제리 시료에서는 1H-NMR 대사체 분석으로 M. × rotundifolia를 다른 박하와 구분하는 신호를 찾았다[22].")
S['safety'] = ("식약처 목록에서 애플민트 잎과 잎 추출물은 '사용가능'이며 사용 부위는 잎으로 정해져 있다[1]. "
"이 종에 대한 식약처·EFSA의 개별 안전성 평가, 알레르기·잔류 정보는 확인하지 못함. "
"52세 여성이 무릎 통증에 M. rotundifolia가 든 찜질약을 붙이고 몇 시간 햇볕을 쬔 뒤 두 무릎에 얕은 2도 화상 같은 광독성 피부염이 생긴 증례가 보고되었고, 보고자들은 이 식물로는 처음 기술된 사례라고 했다[7].\n\n"
"정유 주성분 피페리테논 옥사이드는 세균 복귀돌연변이·소핵·코멧 시험에서 점돌연변이와 DNA 손상을 일으켰고, 저자들은 생체 내 평가가 꼭 필요하다고 했다[8]. "
"반면 이 성분이 38.69–87.25% 든 타르퀴니아 정유 3개 시료는 판당 최대 350 µg에서 S9 유무와 관계없이 TA98·TA100·WP2uvrA 균주에서 돌연변이를 늘리지 않았다[4]. "
"화학형에 따라 풀레곤이 정유의 85.5%(모로코 Béni-Mellal)나 46.5%(사르데냐 아종 insularis)에 이르기도 한다[2, 12]. "
"잎·줄기 메탄올 추출물은 설치류에서 독성을 보이지 않았다고 보고되었으나 중추신경 억제 작용이 있었고[15], 정맥 주사한 추출물은 마취한 쥐의 혈압과 심박수를 낮췄다[30]. "
"발전소 폐수로 오염된 폴란드 하천에서 M. rotundifolia를 포함한 수변 식물 13종을 조사한 결과 이 식물들에 코발트·카드뮴·아연·니켈·납 등이 높은 농도로 들어 있었고, 저자들은 이 식물들을 오염 감시 지표로 쓸 수 있다고 보았다[35].")

compounds = [
 {"name": "Piperitenone oxide", "name_ko": "피페리테논 옥사이드(로툰디폴론)", "class": "모노테르펜 에폭사이드 케톤", "role": "marker", "part": "지상부·잎 정유",
  "content_text": "이탈리아 타르퀴니아 야생 지상부 정유 7월 1–3시간 분획 65.56–87.25%, 8월 50.01–77.51%[4]; 모로코 Azrou 74.69%, M'rirt 81.67%[2]; 모로코 정유 74.55%[26]; 정유 71.19%[27]; 파인애플민트(M. suaveolens) 최고 79.4%[21]; 잎 정유 27.95%[33]",
  "activity_ko": "HSV-1 복제 억제 IC50 1.4 µg/mL(세포)[13]; 칸디다 항진균 활성의 주 기여 성분으로 추정[4]; 시험관 유전독성 시험 양성[8]", "source": [2, 4, 8, 13, 21, 26, 27, 33]},
 {"name": "Piperitenone", "name_ko": "피페리테논", "class": "모노테르펜 케톤", "role": "bioactive", "part": "지상부·잎 정유",
  "content_text": "코르시카 subsp. suaveolens 한 개체 정유 73.5%, 알제리 북부 한 화학형 54.91%, 모로코 M'rirt 10.14%[2]; 잎 정유 6.09%[33]",
  "activity_ko": "마이크로파 보조 에탄올 추출물의 주성분 중 하나[29]; 수증기 증류에서 비율이 높아짐[25]", "source": [2, 25, 29, 33]},
 {"name": "Piperitone oxide", "name_ko": "피페리톤 옥사이드", "class": "모노테르펜 에폭사이드", "role": "bioactive", "part": "지상부 정유",
  "content_text": "알제리 북부 화학형 31.4%·19.72%, 이탈리아 파도바 재배 시료 40.5%[2]",
  "activity_ko": "모로코 정유 성분 비교에서 항균 활성이 피페리테논 옥사이드보다 약 2배 약함(특히 효모)[2]", "source": [2]},
 {"name": "Pulegone", "name_ko": "풀레곤", "class": "모노테르펜 케톤", "role": "bioactive", "part": "지상부 정유",
  "content_text": "모로코 Béni-Mellal 정유 85.5%[2]; 사르데냐 subsp. insularis 46.5%[12]; 모로코 subsp. timija 0.8–26.6%[32]; 잎 정유 4.47%[33]",
  "activity_ko": "모로코 정유 성분 중 세균 19종·진균 3종에 가장 강한 항균 성분, 풀레곤이 많은 정유 MIC 0.69–2.77 ppm[10]", "source": [2, 10, 12, 32, 33]},
 {"name": "Carvone", "name_ko": "카르본", "class": "모노테르펜 케톤", "role": "bioactive", "part": "꽃 정유",
  "content_text": "이집트 재배 꽃 정유 50.59%(카르본 화학형)[11]",
  "activity_ko": "박하 정유의 카르본 경로 대표 성분[2]", "source": [2, 11]},
 {"name": "Limonene", "name_ko": "리모넨", "class": "모노테르펜 탄화수소", "role": "bioactive", "part": "꽃·지상부 정유",
  "content_text": "이집트 재배 꽃 정유 31.25%[11]; 모로코 Azrou 1.85%[2]",
  "activity_ko": "수증기 증류 정유에서 비율이 높아짐[25]", "source": [2, 11, 25]},
 {"name": "Menthol", "name_ko": "멘톨", "class": "모노테르펜 알코올", "role": "bioactive", "part": "지상부 정유",
  "content_text": "모로코 Boulmane 정유 40.50%, 아르헨티나 코르도바 48.32%(잡종일 가능성 지적)[2]",
  "activity_ko": "'Variegata' 품종은 멘톨보다 피페리테논 옥사이드를 주로 만듦[6]", "source": [2, 6]},
 {"name": "Carvacrol", "name_ko": "카바크롤", "class": "페놀성 모노테르펜", "role": "bioactive", "part": "잎 정유",
  "content_text": "잎 정유 19.48%(로툰디폴론 다음 성분)[33]", "activity_ko": "이 정유의 항균 시험 MIC 최저 0.58 µL/mL(정유 전체)[33]", "source": [33]},
 {"name": "Rosmarinic acid", "name_ko": "로즈마린산", "class": "페놀산(카페산 에스터)", "role": "marker", "part": "잎",
  "content_text": "튀니지 10개 집단 마른 잎 메탄올 추출물에서 모두 검출·정량(집단별 수치는 논문 표에 있어 확인하지 못함)[3]",
  "activity_ko": "박하속의 생물지표로 여겨짐; 추출물 DPPH IC50과 음의 상관(r = −0.47)[3]; 1H-NMR에서 박하속 확인 신호[22]", "source": [3, 22]},
 {"name": "Caffeic acid", "name_ko": "카페산", "class": "페놀산", "role": "bioactive", "part": "잎",
  "content_text": "튀니지 집단 건조 추출물 1 g당 최고 1.38 mg(MROT-7)[3]", "activity_ko": "DPPH IC50과 음의 상관(r = −0.48)[3]", "source": [3]},
 {"name": "Luteolin", "name_ko": "루테올린", "class": "플라본", "role": "bioactive", "part": "잎",
  "content_text": "튀니지 집단 건조 추출물 1 g당 최고 4.91 mg(MROT-3)[3]", "activity_ko": "추출물의 아세틸콜린에스터레이스 억제 활성과 상관(r = −0.65)[3]", "source": [3]},
 {"name": "Hesperidin", "name_ko": "헤스페리딘", "class": "플라바논 배당체", "role": "bioactive", "part": "잎",
  "content_text": "튀니지 집단 건조 추출물 1 g당 최고 10.0 mg(MROT-4)[3]", "activity_ko": "아세틸콜린에스터레이스 억제 활성과 상관(r = −0.48)[3]", "source": [3]},
 {"name": "Diosmin", "name_ko": "디오스민", "class": "플라본 배당체", "role": "bioactive", "part": "잎",
  "content_text": "튀니지 집단 건조 추출물 1 g당 최고 3.95 mg(MROT-3)[3]", "activity_ko": "아세틸콜린에스터레이스 억제 활성과 상관(r = −0.54)[3]", "source": [3]},
 {"name": "Salvianolic acid W", "name_ko": "살비아놀산 W", "class": "카페산 유도 페놀산(새 화합물)", "role": "bioactive", "part": "지상부",
  "content_text": "튀니지 Tamra 집단 마른 지상부 18 g에서 1.0 mg 분리; 10개 집단 모두에서 검출[3]", "activity_ko": "FRAP 값과 양의 상관(r = 0.34)[3]", "source": [3]},
 {"name": "Kaempferol glucuronide", "name_ko": "캠페롤 글루쿠로나이드", "class": "플라보놀 배당체", "role": "bioactive", "part": "물 추출물",
  "content_text": "모로코 M. rotundifolia 물 추출물 LC-MS 분석에서 85%(상대 비율)[19]", "activity_ko": "추출물 DPPH IC50 26.47 µg/mL, ABTS IC50 41.21 µg/mL[19]", "source": [19]},
]

assays = [
 {"role": "literature", "compound": "Rosmarinic acid", "compound_ko": "로즈마린산(카페산·살비아놀산 L·W·이소살비아놀산 A·루테올린 글루쿠로나이드·루테올린 등 17종 동시 정량)", "part": "잎(튀니지 10개 자생 집단, 2014년 2월 채취, 실온 2주 건조)",
  "content": "건조 추출물 1 g당 카페산 최고 1.38 mg, 루테올린 4.91 mg, 디오스민 3.95 mg, 헤스페리딘 10.0 mg; 로즈마린산 집단별 수치는 표에 있어 확인하지 못함[3]",
  "method": "UHPLC-HRESIMS/MS(Q Exactive, 내부표준법)",
  "conditions": {"instrument": "Agilent Infinity 1290 UHPLC – Thermo Q Exactive(HESI)", "column": "Kinetex Core-Shell C18, 75 × 2.1 mm, 100 Å, 2.6 µm (Phenomenex)", "mobile_phase": "A 0.1% 포름산 수용액, B 0.1% 포름산 아세토니트릴",
   "gradient": "0–1분 10→20% B; 1–8분 →50% B; 8–8.5분 →100% B; 8.5–10분 100% B; 1분 동안 초기 조건 복귀 후 2분 평형", "flow": "0.6 mL/min", "temp": "",
   "detection": "HESI 음이온, m/z 100–800, 분무 전압 3 kV, 모세관 320 °C, 보조가스 가열 320 °C, 전주사 분해능 70,000, MS/MS NCE 20·30·40; [M−H]− 추출 이온 크로마토그램 면적", "injection": "5 µL",
   "sample_prep": "마른 잎 0.05 g에 내부표준 125 µg 첨가, 메탄올 1 mL씩 3회 추출, 감압 건조 후 메탄올 1 mL에 재용해, 1:25 희석(내부표준 최종 5 µg/mL)",
   "standard": "상용 폴리페놀 표준품(순도 98% 초과, Sigma-Aldrich), 내부표준 시나프산", "linearity": "0.125–10 µg/mL 7점, R² 0.9966–0.9995",
   "lod": "4.7 ng/mL(디오스민)–75.5 ng/mL(살비아놀산 B)", "loq": "14.4 ng/mL(디오스민)–229.0 ng/mL(살비아놀산 B)", "recovery": "62.4 ± 20.2%(내부표준 시나프산 기준)"},
  "rationale": "로즈마린산은 박하속의 생물지표로 여겨지며, 로즈마린산·카페산·살비아놀산 L·W·이소살비아놀산 A와 루테올린·루테올린 글루쿠로나이드 2종이 10개 집단 모두에서 검출되어 이 종의 폴리페놀 지표로 제안됨; ICH Q2(R1)에 따라 검증, 전문 확인[3].",
  "source": [3], "url": "https://doi.org/10.3390/molecules24132351", "source_kind": "paper"},
 {"role": "literature", "compound": "Piperitenone oxide", "compound_ko": "피페리테논 옥사이드(정유 성분 48종 동시 확인)", "part": "지상부 정유(이탈리아 타르퀴니아 야생, 2011년 7·8·9월 채취 생체 약 2.5 kg, 물 증류 1–24시간 분획)",
  "content": "정유 중 7월 1·2·3시간 분획 87.25·70.59·65.56%, 8월 65.05·77.51·50.01%, 9월 38.69·35.64·69.52%(GC-FID 면적%)[4]",
  "method": "GC-MS(동정)·GC-FID(상대 함량)",
  "conditions": {"instrument": "PerkinElmer Clarus 500 GC-MS/GC-FID", "column": "Stabilwax 용융 실리카 모세관, 60 m × 0.25 mm, 막 두께 0.25(원문 단위 표기 'mm') (Restek)", "mobile_phase": "운반 기체 헬륨 1.0 mL/min",
   "gradient": "오븐 60 °C 5분 → 5 °C/min로 220 °C → 220 °C 30분 유지", "flow": "1.0 mL/min", "temp": "주입구 280 °C",
   "detection": "EI 70 eV, m/z 30–350, 스캔 0.2 s, 용매 지연 0–2분; 상대 함량은 FID", "injection": "1 µL(정유 1 µL를 메탄올 1 mL에 희석)",
   "sample_prep": "생 지상부 물 증류(62 L 스테인리스 증류기), 분획마다 기름·물 층 50 mL를 다이에틸 에터 20 mL로 3회 추출, 무수 황산나트륨 건조", "standard": "분석용 표준품 머무름 시간 대조 + NIST·NBS 질량 스펙트럼 라이브러리",
   "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "이 시료군 정유의 주성분이며 피페리테논 옥사이드 비율이 높은 분획일수록 칸디다 항진균 활성이 강해 활성의 주 기여 성분으로 지목됨; 증류 시간·채취 월에 따라 비율이 크게 달라져 품질 지표로 쓰임; 전문 확인, 정량 검증값(직선성·LOD·LOQ·회수율)은 본문에 없음[4].",
  "source": [4], "url": "https://doi.org/10.3390/molecules20069640", "source_kind": "paper"},
]

d = {"slug": "mentha-rotundifolia", "name_ko": "애플민트", "name_en": "Apple mint",
 "scientific_name": "Mentha suaveolens Ehrh. (식약처 목록 병기: Mentha rotundifolia)",
 "aliases": ["애플민트잎", "애플민트잎추출물", "Apple mint", "Round-leave mint", "Round-leafed mint", "Woolly mint", "Mentha rotundifolia", "Mentha suaveolens"],
 "sections": [
  {"key": "overview", "title": "한눈에 보기", "body": S['overview']},
  {"key": "history", "title": "역사와 쓰임", "body": S['history']},
  {"key": "biology", "title": "식물학적 특징", "body": S['biology']},
  {"key": "related_species", "title": "이름과 가까운 종", "body": S['related_species']},
  {"key": "cultivation", "title": "재배와 산지", "body": S['cultivation']},
  {"key": "processing", "title": "가공과 이용", "body": S['processing']},
  {"key": "genetics", "title": "유전체와 화학형", "body": S['genetics']},
  {"key": "safety", "title": "안전성", "body": S['safety']},
 ],
 "compounds": compounds, "markers": [], "nutrients": [], "assays": assays,
 "production": [], "world": [], "gi": [], "orgs": [], "sources": sources}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding='utf-8')
for s in d['sections']:
    print(s['key'], len(s['body']))
