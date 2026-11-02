import json
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "dossier.json"
ACC = "2026-11-02"


def P(n, title, doi, pub):
    return {"n": n, "title": title, "url": f"https://doi.org/{doi}", "publisher": pub, "accessed": ACC}


sources = [
    {"n": 1, "title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — Pyrus ussuriensis 행(산돌배; 원료명 금강산돌배열매·산돌배열매농축액·산돌배열매발효추출액·청실배열매, 사용가능, '사용가능부위 : 열매'; 같은 목록의 백운배나무·참배·남해배나무·털산돌배나무는 별도 행; docs/materials/pyrus-ussuriensis/card.json)",
     "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
    P(2, "Identification of Metabolites and Antioxidant Constituents from Pyrus ussuriensis. Pharmaceuticals (Basel) 2026;19(1):192 (PMC12844793, 전문 확인)", "10.3390/ph19010192", "Pharmaceuticals (MDPI), PubMed Central"),
    P(3, "Protective Effect of Pyrus ussuriensis Maxim. Extract against Ethanol-Induced Gastritis in Rats. Antioxidants 2021;10(3):439 (PMC8002011, 전문 확인)", "10.3390/antiox10030439", "Antioxidants (MDPI), PubMed Central"),
    P(4, "Physical-Chemical Composition and Quality Related Changes in \"Ruaner\" Pear (Pyrus ussuriensis Maxim.) During Freezing-Thawing Period. Molecules 2019;24(14):2611 (PMC6681023, 전문 확인)", "10.3390/molecules24142611", "Molecules (MDPI), PubMed Central"),
    P(5, "Genetic structure and diversity of the wild Ussurian pear in East Asia. Breeding Science 2016;66(1):90-99 (PMC4780806, 전문 확인)", "10.1270/jsbbs.66.90", "Breeding Science, PubMed Central"),
    P(6, "Population Structure of and Conservation Strategies for Wild Pyrus ussuriensis Maxim. in China. PLoS One 2015;10(8):e0133686 (초록 확인)", "10.1371/journal.pone.0133686", "PLoS One, PubMed"),
    P(7, "The complete chloroplast genome of Korean Pyrus ussuriensis Maxim. (Rosaceae): providing genetic background of two types of P. ussuriensis. Mitochondrial DNA Part B 2019;4(2):2424-2425 (PMC7687443, 전문 확인)", "10.1080/23802359.2019.1598802", "Mitochondrial DNA Part B, PubMed Central"),
    P(8, "Pyrus ussuriensis Maxim 70% ethanol eluted fraction ameliorates inflammation and oxidative stress in LPS-induced inflammation in vitro and in vivo. Food Sci Nutr 2023;11(1):458-469 (PMC9834841, 전문 확인)", "10.1002/fsn3.3077", "Food Science & Nutrition, PubMed Central"),
    P(9, "Antioxidant phenolic compounds isolated from wild Pyrus ussuriensis Maxim. fruit peels and leaves. Food Chem 2017;241:182-187 (초록 확인)", "10.1016/j.foodchem.2017.08.072", "Food Chemistry, PubMed"),
    P(10, "Two new lignan glycosides from the fruits of Pyrus ussuriensis. J Asian Nat Prod Res 2016;18(12):1151-1157 (초록 확인)", "10.1080/10286020.2016.1210132", "Journal of Asian Natural Products Research, PubMed"),
    P(11, "Compositional characterization of Pyrus ussuriensis Maxim and their antioxidant activities and induction of apoptosis in Bel-7402 cell. J Food Biochem 2020;44(6):e13222 (초록 확인)", "10.1111/jfbc.13222", "Journal of Food Biochemistry, PubMed"),
    P(12, "Acaricidal activities of materials derived from Pyrus ussuriensis fruits against stored food mites. J Food Prot 2012;75(7):1258-1262 (초록 확인)", "10.4315/0362-028X.JFP-12-040", "Journal of Food Protection, PubMed"),
    P(13, "Evaluation of the volatile profile of 33 Pyrus ussuriensis cultivars by HS-SPME with GC-MS. Food Chem 2012;134(4):2367-2382 (초록 확인)", "10.1016/j.foodchem.2012.04.053", "Food Chemistry, PubMed"),
    P(14, "Diversity of odor-active compounds from local cultivars and wild accessions of Iwateyamanashi (Pyrus ussuriensis var. aromatica) revealed by Aroma Extract Dilution Analysis (AEDA). Breeding Science 2013;63(1):86-95 (초록 확인)", "10.1270/jsbbs.63.86", "Breeding Science, PubMed"),
    P(15, "A comparison of the mineral element content of 70 different varieties of pear fruit (Pyrus ussuriensis) in China. PeerJ 2023;11:e15328 (초록 확인)", "10.7717/peerj.15328", "PeerJ, PubMed"),
    P(16, "Microbiota modulation and anti-obesity effects of fermented Pyrus ussuriensis Maxim extract against high-fat diet-induced obesity in rats. Biomed Pharmacother 2022;154:113629 (초록 확인)", "10.1016/j.biopha.2022.113629", "Biomedicine & Pharmacotherapy, PubMed"),
    P(17, "Ussurian pear extract alleviates acute alcoholic liver injury by enhancing alcohol metabolism and suppressing hepatic oxidative stress and inflammation in rats. Food Funct 2025;16(19):7919-7930 (초록 확인)", "10.1039/d5fo02498f", "Food & Function, PubMed"),
    P(18, "Structural characterization of polysaccharides from 'Nanguo' pear and its protective effect against inflammatory bowel disease in mice via modulating gut microbiota. Int J Biol Macromol 2025;331(Pt 2):148469 (초록 확인)", "10.1016/j.ijbiomac.2025.148469", "International Journal of Biological Macromolecules, PubMed"),
    P(19, "Structure, Physicochemical Property, and Functional Activity of Dietary Fiber Obtained from Pear Fruit Pomace (Pyrus ussuriensis Maxim) via Different Extraction Methods. Foods 2022;11(14):2161 (초록 확인)", "10.3390/foods11142161", "Foods (MDPI), PubMed"),
    P(20, "Comparative transcriptome analysis of climacteric fruit of Chinese pear (Pyrus ussuriensis) reveals new insights into fruit ripening. PLoS One 2014;9(9):e107562 (초록 확인)", "10.1371/journal.pone.0107562", "PLoS One, PubMed"),
    P(21, "GABA application improves the mitochondrial antioxidant system and reduces peel browning in 'Nanguo' pears after removal from cold storage. Food Chem 2019;297:124903 (초록 확인)", "10.1016/j.foodchem.2019.05.177", "Food Chemistry, PubMed"),
    P(22, "The mechanisms underpinning anthocyanin accumulation in a red-skinned bud sport in pear (Pyrus ussuriensis). Plant Cell Rep 2023;42(6):1089-1105 (초록 확인)", "10.1007/s00299-023-03015-8", "Plant Cell Reports, PubMed"),
    P(23, "Biochemical characterization and expression analysis of lignification in two pear (Pyrus ussuriensis Maxim.) varieties with contrasting stone cell content. Protoplasma 2020;257(1):261-274 (초록 확인)", "10.1007/s00709-019-01434-7", "Protoplasma, PubMed"),
    P(24, "A de novo genome assembly of the dwarfing pear rootstock Zhongai 1. Sci Data 2019;6(1):281 (초록 확인)", "10.1038/s41597-019-0291-3", "Scientific Data, PubMed"),
    P(25, "Genome-wide annotation and comparative analysis of miniature inverted-repeat transposable elements (MITEs) in six pear species. Planta 2025;262(2):29 (초록 확인)", "10.1007/s00425-025-04750-w", "Planta, PubMed"),
    P(26, "First report on the presence of fire blight resistance in linkage group 11 of Pyrus ussuriensis Maxim. J Appl Genet 2009;50(2):99-103 (초록 확인)", "10.1007/BF03195660", "Journal of Applied Genetics, PubMed"),
    P(27, "ICE1 of Pyrus ussuriensis functions in cold tolerance by enhancing PuDREBa transcriptional levels through interacting with PuHHP1. Sci Rep 2015;5:17620 (초록 확인)", "10.1038/srep17620", "Scientific Reports, PubMed"),
    P(28, "Efficient potassium (K) recycling and root carbon (C) metabolism improve K use efficiency in pear rootstock genotypes. Plant Physiol Biochem 2023;196:43-54 (초록 확인)", "10.1016/j.plaphy.2023.01.024", "Plant Physiology and Biochemistry, PubMed"),
    P(29, "Climatic suitability of Pyrus ussuriensis in Northeast China under climate change scenarios. Ying Yong Sheng Tai Xue Bao 2025;36(12):3778-3786 (초록 확인)", "10.13287/j.1001-9332.202512.025", "Chinese Journal of Applied Ecology, PubMed"),
    P(30, "Anti-Inflammatory Effect of Chloroform Fraction of Pyrus Ussuriensis Maxim. Leaf Extract on 2,4-Dinitrochlorobenzene-Induced Atopic Dermatitis in nc/nga Mice. Nutrients 2019;11(2):276 (초록 확인)", "10.3390/nu11020276", "Nutrients (MDPI), PubMed"),
    P(31, "Comparative analysis of volatile aromatic compounds from a wide range of pear (Pyrus L.) germplasm resources based on HS-SPME with GC-MS. Food Chem 2023;418:135963 (초록 확인)", "10.1016/j.foodchem.2023.135963", "Food Chemistry, PubMed"),
    P(32, "Extracts of the leaves of Pyrus ussuriensis Maxim. Alleviate itch sensation via TSLP-dependent manner in mouse models of atopic dermatitis. Physiol Behav 2019;210:112624 (초록 확인)", "10.1016/j.physbeh.2019.112624", "Physiology & Behavior, PubMed"),
    P(33, "Exploring the Aroma Fingerprint of Various Chinese Pear Cultivars through Qualitative and Quantitative Analysis of Volatile Compounds Using HS-SPME and GC×GC-TOFMS. Molecules 2023;28(12):4794 (초록 확인)", "10.3390/molecules28124794", "Molecules (MDPI), PubMed"),
]

S = {}
S["overview"] = ("한눈에 보기",
"산돌배(Pyrus ussuriensis Maxim.)는 장미과 배나무속의 나무로, 영어로는 Ussurian pear라 하며 중국 북동부·러시아 극동·한반도 북부·일본 혼슈 북동부에 자생한다[5]. 한국에서는 'Sandolbae'로 불리며, 한국·중국·일본에서 천식·기침·열에 쓰던 전통 약재로 소개된다[30][32]. 중국 북부에서는 가장 중요한 재배 배이고, 이 종에서 나온 재배품종이 150개가 넘는다[5].\n\n"
"식품의약품안전처 「식품원료 목록」에서 산돌배는 식품에 사용할 수 있는 원료(사용가능)이며, 사용 조건은 '사용가능부위 : 열매'이다[1]. 같은 목록에는 금강산돌배열매·산돌배열매농축액·산돌배열매발효추출액·청실배열매 4개 원료명과 다른 이름 '돌배'·'산돌배나무', 변종 표기 var. diamantica·var. ovoidea가 함께 올라 있다[1]. 건강기능식품 고시형 원료의 원재료로 쓰인다는 기록은 확인하지 못함.\n\n"
"열매에는 클로로겐산과 루틴 같은 퀘르세틴 배당체가 들어 있고[2][3], 과육의 주된 당은 과당·포도당, 주된 유기산은 시트르산으로 보고되었다[4]. 동물 실험에서 열매 추출물의 위 점막 보호[3], 급성 알코올 간 손상 완화[17], 항염 효과[8]가 보고되었으나 사람 대상 시험은 확인하지 못함.")

S["history"] = ("역사와 전통적 이용",
"산돌배는 중국 민간 의학에서 오랫동안 기침을 멎게 하고 가래를 삭이며 소변을 잘 나오게 하는 데 쓰였다고 소개된다[2]. 중국에서는 '안리(Anli)'라고도 불리며 가래를 삭이고 기침을 멎게 하는 약선(藥膳) 음식으로 쓰였다[8]. 한국의 한 연구는 산돌배가 위궤양·변비에 쓰는 민간요법으로 알려져 있고 『동의보감』에도 실려 있다고 적었으나[3], 『동의보감』의 해당 조문은 이번에 원문으로 확인하지 못함.\n\n"
"중국 북부에는 산돌배 계통의 배를 겨울에 바깥에 10일 넘게 두어 얼린 뒤 상온에서 녹여 먹는 전통 저장법이 있으며, 이렇게 얼린 배는 그 지역의 별미로 꼽힌다[4]. 아시아에서는 산돌배 열매가 술로 인한 몸의 부담을 덜어 준다고 여겨 흔히 먹는다고 소개된다[17].\n\n"
"일본에서는 20세기 초 혼슈 중부와 북부에서 향기로운 열매를 맺는 배가 각각 새 종으로 기재되었고, 뒤에 산돌배의 두 변종(var. hondoensis, var. aromatica)으로 정리되었다[5]. 그중 기타카미 산지의 var. aromatica는 일본 국가 멸종위기식물 목록에 올라 있다[5]. 한국에서 산돌배를 언제부터 재배·식용했는지에 관한 공식·1차 자료는 확인하지 못함.")

S["biology"] = ("식물학적 특징",
"배나무속은 제3기에 중국 남서부 산지에서 기원한 것으로 여겨지며, 산돌배는 그 가운데 동아시아에 분포하는 종이다[5]. 야생 산돌배는 열매자루가 보통 1–2 cm로 짧고, 영하 52 °C까지 견디며, 수확 뒤 후숙하면 먹는 맛이 좋아지는 점이 다른 배나무속 종과 구별되는 특징으로 꼽힌다[5]. 야생형은 작고 둥근 열매를 맺고 꽃받침이 열매에 남는다[7].\n\n"
"중국 재배형 산돌배 열매는 둥글거나 납작한 원형에 황록색이며, 꽃받침이 남고 과육이 거칠며 석세포가 많다[4]. 석세포 함량은 품종마다 달라, 석세포가 많은 '젠바(Jianba)'는 '난궈(Nanguo)'보다 리그닌 단위체와 하이드록시신남산류가 많았다[23]. 산돌배 열매는 전형적인 호흡 급등형(climacteric) 과일로, 익는 동안 에틸렌을 많이 내고 단단함이 빠르게 떨어진다[20].\n\n"
"중국 북부 산돌배는 영하 30~35 °C의 저온을 견디며, 열매의 칼륨·칼슘·마그네슘이 시판 백리·사리 계통 배보다 높다고 보고되었다[15]. 내몽골의 자생지는 해발 1,000–1,200 m의 산지·계곡에, 헤이룽장·지린의 자생지는 해발 300–600 m의 민가·밭 가장자리 주변에 있었다[5]. 배나무속처럼 자가불화합성이지만 작은 집단에서는 근친교배가 일어날 수 있다[5].")

S["related_species"] = ("가까운 종",
"동아시아의 주요 재배 배는 전통적으로 산돌배(P. ussuriensis), 중국 백리 계통, 돌배나무(P. pyrifolia) 세 종으로 나뉘며, 원예적으로는 우수리배·중국 백리·중국 사리·일본배 같은 재배형이 대체로 이 분류에 대응한다[5]. 배나무속에는 널리 인정되는 기본 종이 22개 있고, 서유럽과 동아시아 두 지역에 다양성이 몰려 있다[7].\n\n"
"일본의 var. aromatica와 var. hondoensis는 산돌배의 변종으로 다뤄지며, 열매에 꽃받침이 남는지가 돌배나무와 구별하는 형태 특징이지만 두 종은 교잡이 쉬워 중간형이 흔하다[5]. 유전 분석에서는 기타카미 산지의 var. aromatica에 선사시대에 들어온 돌배나무 유전자가 섞인 흔적이 확인되었다[5]. 중국 야생 산돌배와 일본 var. aromatica는 꽃·열매 형태와 유전 구조가 뚜렷이 달랐다[5].\n\n"
"「식품원료 목록」에서는 백운배나무(var. hakunensis)·참배(var. macrostipes)·남해배나무(var. nankaiensis)·털산돌배나무(var. pubescens)가 산돌배와 별도 원료로 올라 있어 이 글에서는 다루지 않는다[1]. 중국의 왜성 대목 '중아이 1호'는 산돌배와 서양배를 교배한 뒤 다시 교배한 잡종이다[24]. 화상병에 약한 서양배 품종과 저항성 산돌배를 교배한 집단에서 산돌배 쪽 연관군 11에 저항성 후보 유전자 자리가 처음 보고되었다[26].")

S["cultivation"] = ("재배와 생산",
"중국의 야생 산돌배 자생지는 개발과 사막화로 줄고 있으며, 내몽골 6개 자생지의 1,000그루가 넘던 나무 가운데 약 3분의 2가 2010년 100일 넘는 가뭄으로 죽었다[5]. 2009–2011년 조사에서 내몽골·지린·헤이룽장 13개 집단에서 1,518그루가 확인되었다[5]. 중국 동북 3성의 기후 적합지 모형은 현재 고적합지가 주로 랴오닝에 있고, 2030·2050년대에는 적합지가 넓어지며 북쪽으로 옮겨 갈 것으로 예측했다[29].\n\n"
"산돌배는 대목으로도 쓰이며, 칼륨이 부족한 수경 조건에서 다른 대목 종인 P. betulifolia보다 칼륨을 더 잘 흡수하고 재활용했다[28]. 산돌배에서 분리한 PuICE1 유전자를 토마토에 넣으면 저온 내성이 높아져, 산돌배의 추위 견딤과 관련된 유전자로 연구된다[27].\n\n"
"대표 재배품종 '난궈'는 냉장 저장으로 후숙을 늦출 수 있지만, 오래 냉장한 뒤 상온에 꺼내면 껍질이 갈변하기 쉽다[21]. γ-아미노뷰티르산(GABA) 처리는 미토콘드리아 항산화 효소를 높여 이 갈변을 줄였다[21]. '난궈'의 아조변이인 '난훙(Nanhong)'은 껍질의 안토시아닌이 훨씬 많은 붉은 배다[22]. 한국 내 산돌배 재배 면적·생산량 통계는 확인하지 못함.")

S["processing"] = ("가공과 이용",
"「식품원료 목록」에는 산돌배 열매를 원료로 한 농축액과 발효추출액이 원료명으로 올라 있다[1]. 식약처 「식품 등의 생산실적」에서 산돌배를 원료로 한 건강기능식품 품목의 생산실적은 확인하지 못함.\n\n"
"중국 북부의 '롼얼(Ruaner)' 배를 영하 20 °C에서 7일 얼린 뒤 녹인 연구에서, 해동 3–4시간째가 단단함·수분·당도가 알맞아 생식과 가공에 가장 좋은 때로 제시되었다[4]. 해동 5시간째 껍질의 총 폴리페놀은 신선한 배보다 약 81.31%, 총 플라보노이드는 약 77.27% 줄었다[4].\n\n"
"즙을 짜고 남은 박(pomace)에서 효소·마이크로파·삼상분배법으로 식이섬유를 뽑으면 추출법에 따라 수율·분자량·혈당 관련 시험관 활성이 달랐다[19]. '난궈' 배의 주된 다당류 NGP-3은 갈락투론산·자일로스·아라비노스·갈락토스가 1.92:1:0.73:0.36 몰비로 이루어졌다[18]. 발효 추출물은 고지방식 쥐에서 체중 증가와 지방 조직을 줄였고[16], 물 추출물과 에탄올 추출물은 검출되는 성분 구성이 달라 추출 조건이 중요하다고 보고되었다[2]. 50% 에탄올 추출물의 당도는 19 Brix였다[3].\n\n"
"중국 재배품종 33개의 열매에서는 휘발성 향기 성분 108종이 확인되었고, 에스터가 많은 무리와 탄화수소가 많은 무리 등 4개 무리로 나뉘었다[13]. 일곱 품종 비교에서는 '난궈리'에서 가장 많은 108종의 향기 성분이 검출되었다[33].")

S["genetics"] = ("유전체와 육종",
"경북 봉화에서 채집한 한국 야생 산돌배의 엽록체 유전체는 159,986 bp, 유전자 130개, GC 함량 36.5%였고 B형 엽록체 DNA를 지녔다[7]. 함백산에서 채집한 다른 야생 개체(A형)와는 단일염기다형성 121개, 삽입·결실 781개가 달라, 한국 야생 집단에 두 유형이 함께 있음이 확인되었다[7].\n\n"
"중국 야생 산돌배 153개체를 핵 SSR 20개·엽록체 SSR 16개로 분석한 결과, 서식지 단편화로 유전 다양성이 낮았고 집단 간 변이는 핵 SSR 20.05%, 엽록체 SSR 44.40%였다[6]. 연구진은 내몽골과 헤이룽장 북동부를 시급한 보전 지역으로 보고 4개 보전 단위를 제안했다[6].\n\n"
"산돌배 순수 계통의 염색체 수준 유전체는 확인하지 못함. 대신 산돌배 피가 섞인 왜성 대목 '중아이 1호'의 유전체가 510.59 Mb, 17개 염색체, 단백질 암호화 유전자 43,120개로 조립되었다[24]. 여섯 배나무 유전체를 비교한 연구는 '중아이 1호'를 산돌배 대표로 써서 MITE 전이인자 750개 과, 12,759개를 찾았다[25]. '난궈'의 호흡 급등 전후 열매 전사체 비교에서는 3,279개 유전자의 발현이 달랐다[20]. 202개 배 품종 비교에서 열매 휘발성 성분 총량은 서양배·신장배 다음으로 산돌배가 많았고[31], 일본 var. aromatica 지역 품종에서 찾은 향기 활성 성분 33종은 향이 약한 일본배 육종의 재료로 제안되었다[14].")

S["safety"] = ("안전성",
"산돌배는 「식품원료 목록」에서 사용가능 원료이지만 사용 부위는 열매로 한정된다[1]. 잎 추출물의 아토피 피부염 동물 연구가 있으나[30][32], 잎은 목록상 사용 부위가 아니므로 식품 섭취 근거로 볼 수 없다[1]. 건강기능식품 고시형 원료가 아니어서 고시 섭취 시 주의사항은 없으며, 식약처 등 공공기관의 산돌배 알레르기·잔류농약·독성 성분 정보는 확인하지 못함.\n\n"
"쥐에게 열매 50% 에탄올 추출물 250·500 mg/kg을 14일 먹인 위염 실험에서 독성 징후는 관찰되지 않았다고 보고되었다[3]. 발효 추출물을 먹인 고지방식 쥐 실험에서는 대조군과 먹이 섭취량 차이가 없었다[16]. 이 연구들은 효능 실험이며, 정식 반복투여 독성시험이나 사람 대상 안전성 자료는 확인하지 못함.\n\n"
"열매 물 추출물의 에틸아세테이트 분획에서는 저장 식품 진드기를 죽이는 성분으로 1,4-벤조퀴논이 분리되었다[12]. 그러나 먹는 열매에 들어 있는 1,4-벤조퀴논의 양은 확인하지 못함. 냉동 후 해동한 배는 막이 손상되어 폴리페놀이 산화되며 껍질이 갈색으로 변한다[4].")

sections = [{"key": k, "title": v[0], "body": v[1]} for k, v in S.items()]

compounds = [
    {"name": "Chlorogenic acid", "name_ko": "클로로겐산", "class": "페놀산(카페오일퀸산)", "role": "marker", "part": "열매(50% 에탄올 추출물)",
     "content_text": "추출물 1 g당 1.21 ± 0.5 mg(HPLC, 머무름 시간 11.7분)[3]",
     "activity_ko": "추출물의 품질 관리 지표로 정량되었고 추출물에서 가장 많은 폴리페놀로 보고되었다[3]; 광양산 열매 추출물의 LC-DPPH 시험에서 피크 면적이 크게 줄어 항산화 성분으로 지목되었다[2]", "source": [2, 3]},
    {"name": "Fructose", "name_ko": "과당", "class": "당류", "role": "nutrient", "part": "열매 과육('롼얼', 냉동–해동 중)",
     "content_text": "42.66–71.96 mg/g 생중량, 총 가용성 당의 50.59–58.70%[4]", "activity_ko": "과육의 주된 당이다[4]", "source": [4]},
    {"name": "Glucose", "name_ko": "포도당", "class": "당류", "role": "nutrient", "part": "열매 과육('롼얼', 냉동–해동 중)",
     "content_text": "28.47–55.31 mg/g 생중량, 총 가용성 당의 36.43–45.22%[4]", "activity_ko": "과당 다음으로 많은 당이다[4]", "source": [4]},
    {"name": "Sucrose", "name_ko": "자당", "class": "당류", "role": "nutrient", "part": "열매 과육('롼얼', 냉동–해동 중)",
     "content_text": "3.64–7.03 mg/g 생중량, 총 가용성 당의 3.92–5.42%[4]", "activity_ko": "세 당 가운데 가장 적었고 해동 12시간까지 계속 늘었다; 소르비톨은 검출되지 않았다[4]", "source": [4]},
    {"name": "Citric acid", "name_ko": "시트르산", "class": "유기산", "role": "nutrient", "part": "열매 과육('롼얼', 냉동–해동 중)",
     "content_text": "0.87–2.82 mg/g 생중량, 총 유기산의 61.70–80.57%[4]", "activity_ko": "과육에서 가장 많은 유기산이다[4]", "source": [4]},
    {"name": "Malic acid", "name_ko": "말산", "class": "유기산", "role": "nutrient", "part": "열매 과육('롼얼', 냉동–해동 중)",
     "content_text": "0.33–0.44 mg/g 생중량(옥살산 0.16–0.24 mg/g)[4]", "activity_ko": "시트르산 다음으로 많은 유기산이다[4]", "source": [4]},
    {"name": "Rutin", "name_ko": "루틴(퀘르세틴-3-루티노사이드)", "class": "플라보놀 배당체", "role": "bioactive", "part": "열매(물·에탄올 추출물), 열매 껍질",
     "content_text": "정량값 확인하지 못함(UHPLC-MS/MS로 동정)[2]", "activity_ko": "광양산 열매 추출물에서 퀘르세틴 배당체 무리로 동정되었고[2], 야생 열매 껍질·잎에서도 분리되었다[9]", "source": [2, 9]},
    {"name": "Quercetin", "name_ko": "퀘르세틴", "class": "플라보놀", "role": "bioactive", "part": "열매 껍질·잎",
     "content_text": "함량 확인하지 못함; DPPH 라디칼 소거 IC50 6.06 μg/mL[9]", "activity_ko": "야생 산돌배 껍질·잎에서 분리한 13개 페놀 성분 가운데 DPPH 소거 활성이 가장 강한 축이었다[9]", "source": [9]},
    {"name": "3,5-Dicaffeoylquinic acid", "name_ko": "3,5-다이카페오일퀸산", "class": "페놀산", "role": "bioactive", "part": "열매",
     "content_text": "정량값 확인하지 못함(질량분석으로 동정)[2][8]", "activity_ko": "한국산 열매 추출물[2]과 중국산 열매 70% 에탄올 용출 분획[8]에서 모두 동정되었다", "source": [2, 8]},
    {"name": "(+)-Catechin", "name_ko": "카테킨", "class": "플라반-3-올", "role": "bioactive", "part": "열매(70% 에탄올 용출 분획), 열매 껍질·잎",
     "content_text": "정량값 확인하지 못함[8]", "activity_ko": "열매 분획에서 프로시아니딘 이량체·삼량체와 함께 동정되었고[8], 껍질·잎에서도 분리되었다[9]", "source": [8, 9]},
    {"name": "Cyanidin 3-O-glucoside", "name_ko": "시아니딘-3-O-글루코사이드", "class": "안토시아닌", "role": "bioactive", "part": "열매(70% 에탄올 용출 분획)",
     "content_text": "정량값 확인하지 못함[8]", "activity_ko": "열매 페놀 분획에서 유일하게 동정된 안토시아닌이다[8]; 붉은 아조변이 '난훙'은 껍질 안토시아닌이 '난궈'보다 훨씬 많다[22]", "source": [8, 22]},
    {"name": "Oleanolic acid", "name_ko": "올레아놀산", "class": "오환성 트라이터펜", "role": "bioactive", "part": "열매 추출물(에틸아세테이트 분획)",
     "content_text": "함량 확인하지 못함[11]", "activity_ko": "추출물 가운데 간암 세포(Bel-7402)에 작용한 주성분으로, 카스페이스 경로 세포자멸사와 G0/G1 정지를 일으켰다(세포 실험)[11]", "source": [11]},
    {"name": "1,4-Benzoquinone", "name_ko": "1,4-벤조퀴논", "class": "퀴논", "role": "bioactive", "part": "열매 물 추출물(에틸아세테이트 분획)",
     "content_text": "열매 속 함량 확인하지 못함; 훈증 시험 LD50 1.98 μg/cm²(저장 식품 진드기)[12]", "activity_ko": "열매에서 분리된 진드기 살충 성분으로, 벤질벤조에이트보다 훈증 시험에서 5.9배 강했다[12]", "source": [12]},
    {"name": "Ussuriensislignan A", "name_ko": "우수리엔시스리그난 A", "class": "리그난 배당체", "role": "bioactive", "part": "열매",
     "content_text": "함량 확인하지 못함[10]", "activity_ko": "열매에서 새로 분리된 리그난 배당체로, 배나무속에서 리그난이 분리된 첫 보고다[10]", "source": [10]},
    {"name": "Potassium", "name_ko": "칼륨", "class": "무기질", "role": "nutrient", "part": "열매 껍질·과육",
     "content_text": "수치 확인하지 못함; 무기질 함량 순서 K > P > Ca > Mg > Na > Al > Fe > Zn > Cu > Cr > Pb > Cd[15]", "activity_ko": "70개 품종·계통 열매에서 가장 많은 무기질이며 야생형이 재배형보다 무기질이 많았다[15]", "source": [15]},
]

E = {"instrument": "", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "", "injection": "",
     "sample_prep": "", "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""}


def C(**kw):
    d = dict(E)
    d.update(kw)
    return d


assays = [
    {"role": "literature", "compound": "Chlorogenic acid", "compound_ko": "클로로겐산", "part": "열매(건조 열매 50% 에탄올 추출물)",
     "content": "추출물 1 g당 1.21 ± 0.5 mg, 머무름 시간 11.7 ± 0.03분[3]", "method": "HPLC-UV",
     "conditions": C(instrument="Agilent 1100 시리즈 HPLC(4원 펌프·자동시료주입기·UV 검출기)",
                     column="역상 Eclipse Plus C18, 4.6 × 250 mm, 5 μm",
                     mobile_phase="아세토나이트릴 : 0.5% 인산 수용액 = 11.5 : 88.5(v/v)",
                     gradient="등용매(원문에 기울기 없음)", temp="40 °C", detection="UV 327 nm", injection="20 μL",
                     sample_prep="건조 열매 분말을 50% 에탄올로 추출 → 회전증발 농축(95 °C) → 동결건조; 건조 추출물 20 mg을 70% 에탄올에 녹여 30분 초음파·와류 혼합 → 1,340×g 5분 원심 → 상등액",
                     standard="클로로겐산 표준품(Sigma) 0.1 mg/mL 원액(70% 에탄올)을 단계 희석해 0.05–10 μg/mL 검량"),
     "rationale": "연구진이 추출물의 정량·품질 관리를 위한 지표물질(indicative material)로 클로로겐산을 정했고, 추출물에서 가장 많은 폴리페놀로 보고했다[3]. 전문(Methods) 확인 — 유속·검출한계·정량한계·회수율은 본문에 없음[3].",
     "source": [3], "url": "https://doi.org/10.3390/antiox10030439", "source_kind": "paper"},
    {"role": "literature", "compound": "Fructose", "compound_ko": "과당·포도당·자당(가용성 당)", "part": "열매 과육('롼얼' 품종, 냉동–해동)",
     "content": "과당 42.66–71.96 mg/g, 포도당 28.47–55.31 mg/g, 자당 3.64–7.03 mg/g(생중량)[4]", "method": "HPLC-RI",
     "conditions": C(instrument="Shimadzu HPLC, RI 검출기", column="ZORBAX NH2, 4.6 × 250 mm, 5 μm",
                     mobile_phase="아세토나이트릴 : 2차 증류수 = 7 : 3", gradient="등용매, 총 25분", flow="1.0 mL/min", temp="40 °C",
                     detection="굴절률(RI)",
                     sample_prep="중국 간쑤성 란저우 상업 과원 열매(2017·2018년 10월 1일 수확), 상온 3일 뒤 −20 °C 7일 냉동 → 상온 해동 0–12시간 채취; 과육 5.00 g(4개 과실 합침) 마쇄·추출 후 상등액 25 mL 분석",
                     standard="과당·포도당·자당 표준품(Sigma)"),
     "rationale": "과당·포도당은 과육의 주된 당으로, 당·산 조성은 배의 맛과 후숙 품질을 판단하는 핵심 지표다[4]. 전문(Methods) 확인 — 주입량·검출한계·정량한계·회수율은 본문에 없음[4].",
     "source": [4], "url": "https://doi.org/10.3390/molecules24142611", "source_kind": "paper"},
    {"role": "literature", "compound": "Citric acid", "compound_ko": "시트르산·말산·옥살산(유기산)", "part": "열매 과육('롼얼' 품종, 냉동–해동)",
     "content": "시트르산 0.87–2.82 mg/g(총 유기산의 61.70–80.57%), 말산 0.33–0.44 mg/g, 옥살산 0.16–0.24 mg/g(생중량)[4]", "method": "HPLC-PDA",
     "conditions": C(instrument="Shimadzu HPLC, PDA 검출기", column="Waters IC PAK 이온 배제 칼럼, 300 × 7.8 mm",
                     mobile_phase="0.01 mM 황산(2차 증류수, 원문 표기 그대로)", gradient="등용매, 총 30분", flow="0.5 mL/min", temp="40 °C",
                     detection="210 nm",
                     sample_prep="당 분석과 같은 과육 추출물(과육 5.00 g 마쇄·추출 후 상등액)",
                     standard="말산·시트르산·옥살산 표준품(Sigma)"),
     "rationale": "시트르산은 이 품종 과육에서 가장 많은 유기산으로, 신맛과 후숙·해동 중 품질 변화를 보여 주는 지표로 쓰였다[4]. 전문(Methods) 확인 — 주입량·검출한계·정량한계·회수율은 본문에 없음[4].",
     "source": [4], "url": "https://doi.org/10.3390/molecules24142611", "source_kind": "paper"},
    {"role": "literature", "compound": "Rutin", "compound_ko": "루틴 등 퀘르세틴 배당체", "part": "열매(전남 광양산, 동결건조 후 물·100% 에탄올 추출물)",
     "content": "정량값 확인하지 못함 — 150개 성분을 질량분석으로 주석하고 함량은 피크 면적으로 대략 비교함[2]", "method": "UHPLC-ESI-MS/MS(Orbitrap)",
     "conditions": C(instrument="Vanquish UHPLC + Orbitrap Exploris 120 질량분석기",
                     column="Waters Acquity UPLC HSS T3, 4.6 × 100 mm, 1.8 μm(원문 표기 그대로)",
                     mobile_phase="A: 0.1% 폼산 물, B: 0.1% 폼산 아세토나이트릴",
                     gradient="B 3–5%(0–4분) → 5–8%(4–8분) → 8–10%(8–11분) → 10–15%(11–15분) → 15–50%(15–20분) → 50–100%(20–24분) → 100%(24–27분) → 1분간 3%로 복귀 후 재평형",
                     flow="0.3 mL/min", temp="40 °C",
                     detection="ESI 양이온, m/z 100–1450, 분무 전압 3,500 V, 기화기 350 °C, 이온 전달관 325 °C, HCD 충돌 에너지 15·30·60 V, 전체 스캔+데이터 의존 MS/MS",
                     injection="4 μL",
                     sample_prep="2022년 가을 열매를 5일 동결건조 → 물(70 °C, 3시간) 또는 100% 에탄올(70 °C, 3시간) 추출 → 감압 농축 → 50% 메탄올에 녹여 0.22 μm PTFE 막 여과",
                     standard="표준품 정량 없음; 공개 질량 스펙트럼 DB·GNPS 분자 네트워크로 동정(질량 차 5 mDa 미만)"),
     "rationale": "퀘르세틴 배당체(루틴 등)와 클로로겐산이 분자 네트워크의 주요 무리로 동정되었고, LC-DPPH 반응으로 항산화 성분을 가려내는 데 쓰였다[2]. 전문(Methods) 확인 — 개별 성분 함량·검출한계·정량한계·회수율은 본문에 없음[2].",
     "source": [2], "url": "https://doi.org/10.3390/ph19010192", "source_kind": "paper"},
]

d = {
    "slug": "pyrus-ussuriensis",
    "name_ko": "산돌배",
    "name_en": "Ussurian pear",
    "scientific_name": "Pyrus ussuriensis Maxim.",
    "aliases": ["산돌배나무", "돌배", "금강산돌배", "청실배", "Ussurian pear", "Geumgangsan wild pear", "Ovoid-fruit Ussurian pear",
                "Pyrus ussuriensis var. diamantica", "Pyrus ussuriensis var. ovoidea", "Sandolbae"],
    "sections": sections,
    "compounds": compounds,
    "markers": [],
    "assays": assays,
    "nutrients": [],
    "production": [],
    "world": [],
    "gi": [],
    "orgs": [],
    "sources": sources,
}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
for s in sections:
    print(s["key"], len(s["body"]))
