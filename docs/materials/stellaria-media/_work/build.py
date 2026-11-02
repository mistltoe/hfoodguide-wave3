import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
A = "2026-11-02"
def pm(n, title, doi, pmid, pmc=None, note="초록 확인"):
    ids = f"PMID {pmid}" + (f", {pmc}" if pmc else "")
    url = f"https://doi.org/{doi}" if doi else f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
    return {"n": n, "title": f"{title} ({ids}, {note})", "url": url, "publisher": "PubMed", "accessed": A}
sources = [
 {"n": 1, "title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 별꽃순(Stellaria media (L.) Vill. / Alsine media L. / Stellaria media var. minor Makino; Chickweed, Common chickweed), 식품원료(A코드), 사용가능, 사용가능부위: 순; 같은 속·비슷한 이름의 다른 행(벼룩나물순, 왕별꽃순, Star chickweed잎, Stellaria jamesiana·neglecta·nipponica·diversiflora·sessiliflora잎, 점나도나물순 등) 대조 (로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json)", "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
 pm(2, "Stellaria media (L.) Vill.- A plant with immense therapeutic potentials: phytochemistry and pharmacology — Heliyon 2020;6(6):e04150", "10.1016/j.heliyon.2020.e04150", "32548330", "PMC7284062", "전문 확인; 2차 문헌(리뷰)"),
 pm(3, "Five undervalued edible species inherent to autumn-winter season: nutritional composition, bioactive constituents and volatiles profile — PeerJ 2021;9:e12488", "10.7717/peerj.12488", "34900422", "PMC8621719", "전문 확인; 표 2의 '(L.) Vill' 열이 별꽃"),
 pm(4, "Quality assessment and anti-obesity activity of Stellaria media (Linn.) Vill. — BMC Complement Altern Med 2012;12:145", "10.1186/1472-6882-12-145", "22943464", "PMC3468403", "전문 확인"),
 pm(5, "Anti-hepatitis B virus activity of chickweed [Stellaria media (L.) Vill.] extracts in HepG2.2.15 cells — Molecules 2012;17(7):8633", "10.3390/molecules17078633", "22810196", "PMC6268626", "전문 확인"),
 pm(6, "Stellaria media tea protects against diabetes-induced cardiac dysfunction in rats without affecting glucose tolerance — J Tradit Complement Med 2021", "10.1016/j.jtcme.2021.08.003", "35493309", "PMC9039105", "전문 확인; 분석 세부는 보충자료라 확인 못함"),
 pm(7, "Effect of Stellaria media Tea on Lipid Profile in Rats — Evid Based Complement Alternat Med 2020;2020:5109328", "10.1155/2020/5109328", "32047525", "PMC7003252", "초록 확인"),
 pm(8, "Small Steps to the Big Picture for Health-Promoting Applications Through the Use of Chickweed (Stellaria media): In Vitro, In Silico, and Pharmacological Network Approaches — Food Sci Nutr 2024", "10.1002/fsn3.4505", "39620022", "PMC11606822", "전문 확인"),
 pm(9, "Nutritional and toxic factors in selected wild edible plants — Plant Foods Hum Nutr 1997", "10.1023/a:1007988815888", "9527345", None, "초록 확인; 종별 질산염 값은 초록에 없음"),
 pm(10, "Safety evaluation of some wild plants in the New Nordic Diet — Food Chem Toxicol 2012;50(12):4461-7", "10.1016/j.fct.2012.09.016", "23009884", None, "초록 확인"),
 pm(11, "Erythema multiforme due to contact with weeds: a recurrence after patch testing — Contact Dermatitis 2003", "10.1034/j.1600-0536.2003.480104.x", "12641574", None, "초록 확인; 증례 보고"),
 pm(12, "Sesquiterpene lactone mix patch testing supplemented with dandelion extract in patients with allergic contact dermatitis, atopic dermatitis and non-allergic chronic inflammatory skin diseases — Contact Dermatitis 2004", "10.1111/j.0105-1873.2004.00413.x", "15479198", None, "초록 확인"),
 pm(13, "Unraveling the Chloroplast Genome of Stellaria media: Comprehensive Analysis, Taxonomic Implications, and Evolutionary Perspectives — Biochem Genet 2025", "10.1007/s10528-025-11229-6", "40828201", None, "초록 확인"),
 pm(14, "Comparative plastome analyses and phylogenetic insights of Stellaria (Caryophyllaceae) — Front Plant Sci 2026;17:1902479", "10.3389/fpls.2026.1902479", "42559103", "PMC13438306", "초록 확인"),
 pm(15, "Phylogenetic analysis and temporal diversification of the tribe Alsineae (Caryophyllaceae) with the description of three new genera — Front Plant Sci 2023;14:1127443", "10.3389/fpls.2023.1127443", "37416878", "PMC10321415", "초록 확인"),
 pm(16, "Isolation and characterization of a pentasaccharide from Stellaria media — J Nat Prod 2008", "10.1021/np800274k", "18855444", None, "초록 확인"),
 pm(17, "Metabolism of galactosyl-oligosaccharides in Stellaria media — discovery of stellariose synthase, a novel type of galactosyltransferase — Phytochemistry 2010", "10.1016/j.phytochem.2010.04.012", "20452631", None, "초록 확인"),
 pm(18, "Studies on antioxidative activity of some C-glycosylflavones — Pol J Pharmacol Pharm 1991", None, "1824129", None, "초록 확인"),
 pm(19, "New triterpenoid from Stellaria media (L.) Cyr. — Nat Prod Res 2009", "10.1080/14786410701642532", "19735039", None, "초록 확인"),
 pm(20, "Effect of six Korean plants on glucagon like peptide-1 release — Food Sci Biotechnol 2019", "10.1007/s10068-019-00603-x", "31695957", "PMC6811474", "초록 확인; PMC 본문은 비어 있었음"),
 pm(21, "Ethnobotanical knowledge among the semi-pastoral Gujjar tribe in the high altitude (Adhwari's) of Churah subdivision, district Chamba, Western Himalaya — J Ethnobiol Ethnomed 2019", "10.1186/s13002-019-0286-3", "30744678", "PMC6371563", "초록 확인"),
 pm(22, "Ethnobotanical and ethnomedicinal uses of plants in the district of Acquapendente (Latium, Central Italy) — J Ethnopharmacol 2005", "10.1016/j.jep.2004.09.014", "15619562", None, "초록 확인"),
 pm(23, "Health risk assessment and multivariate apportionment of trace metals in wild leafy vegetables from Lesser Himalayas, Pakistan — Ecotoxicol Environ Saf 2013", "10.1016/j.ecoenv.2013.02.011", "23490195", None, "초록 확인"),
 pm(24, "Stress responses and nickel and zinc accumulation in different accessions of Stellaria media (L.) Vill. in response to solution pH variation in hydroponic culture — Plant Physiol Biochem 2020", "10.1016/j.plaphy.2020.01.012", "31958680", None, "초록 확인"),
 pm(25, "Isolation, molecular cloning and antimicrobial activity of novel defensins from common chickweed (Stellaria media L.) seeds — Biochimie 2010", "10.1016/j.biochi.2010.10.019", "21056078", None, "초록 확인"),
 pm(26, "Defense peptide repertoire of Stellaria media predicted by high throughput next generation sequencing — Biochimie 2016", "10.1016/j.biochi.2016.12.017", "28038935", None, "초록 확인"),
 pm(27, "Modelling the germination of Stellaria media using the concept of hydrothermal time — New Phytol 2000", "10.1046/j.1469-8137.2000.00778.x", "33863021", None, "초록 확인"),
 pm(28, "The Role of Weed Hosts and Tobacco Thrips, Frankliniella fusca, in the Epidemiology of Tomato spotted wilt virus — Plant Dis 2002", "10.1094/PDIS.2002.86.6.573", "30823226", None, "초록 확인"),
 pm(29, "Antiobesity effect of Stellaria media against drug induced obesity in Swiss albino mice — Ayu 2011", "10.4103/0974-8520.96137", "22661858", "PMC3361939", "초록 확인"),
 pm(30, "Purification and characterization of a novel anti-HSV-2 protein with antiproliferative and peroxidase activities from Stellaria media — Acta Biochim Biophys Sin 2013", "10.1093/abbs/gmt060", "23761431", None, "초록 확인"),
 pm(31, "In Vitro COX Inhibitory Activity, LC-MS Analysis and Molecular Docking Study of Silene vulgaris and Stellaria media — Cell Biochem Biophys 2024", "10.1007/s12013-024-01533-0", "39313643", None, "초록 확인"),
 pm(32, "Phytochemical analysis and gastroprotective effect of Stellaria media (L.) Vill. methanolic extract on piroxicam-induced gastric ulcer in Wistar rats — Pak J Pharm Sci 2023", None, "37869918", None, "초록 확인"),
 pm(33, "Evaluation of hepatoprotective activity of water-soluble polysaccharide fraction of Stellaria media L. — Bull Exp Biol Med 2013", "10.1007/s10517-013-2021-8", "23658890", None, "초록 확인"),
 pm(34, "High Resistance of Potato to Early Blight Is Achieved by Expression of the pro-SmAMP1 Gene for Hevein-Like Antimicrobial Peptides from Common Chickweed (Stellaria media) — Plants (Basel) 2021;10(7):1395", "10.3390/plants10071395", "34371598", "PMC8309211", "초록 확인"),
]

S = {}
S["overview"] = ("별꽃(Stellaria media)은 석죽과(Caryophyllaceae) 별꽃속의 한해살이 풀로, 영어로 chickweed라 불리며 온대·한대 지역에 널리 퍼져 있다[2]. "
 "식약처 「식품원료 목록」에는 원료명 '별꽃순'(학명 Stellaria media (L.) Vill., 이명 Alsine media L.·Stellaria media var. minor Makino)으로 한 행이 올라 있다[1]. "
 "식품원료(A코드)·사용가능 원료이며 조건은 '사용가능부위 : 순'이어서 어린 순만 식품에 쓸 수 있다[1]. "
 "이 종을 원재료로 하는 건강기능식품 고시형 원료는 확인하지 못함.\n\n"
 "잎과 순은 샐러드·국·스튜·차로 먹고, 민간에서는 피부병·비만·호흡기 질환 등에 써 왔다[2, 3]. "
 "주요 성분으로는 아피게닌 C-배당체(비텍신·비세닌-2 등) 같은 플라보노이드, 트라이테르페노이드 사포닌, 석죽과 특유의 갈락토올리고당 스텔라리오스가 보고되었다[2, 5, 16]. "
 "보고된 효과는 생쥐 항비만, 쥐 위궤양·간 손상 보호, COX-2 억제, 항헤르페스 단백질 등 동물·세포 실험이다[4, 30–33]. "
 "별꽃을 먹인 사람 대상 임상시험은 PubMed에서 확인하지 못함. "
 "질산염·사포닌·피부염·중금속 자료는 안전성 절에 정리했다[3, 4, 11, 23].")
S["history"] = ("별꽃은 오래전부터 약초로 쓰여 왔으며, 아시아와 열대 아프리카에서는 잎 달인 물을 급성 위장·호흡기 질환에, 인도에서는 상처와 출혈에 썼다고 정리되어 있다[2]. "
 "중국에서는 200년 넘게 피부염 등 피부 질환에 쓴 민간약으로 소개되며, 17세기 영국의 한 약초서는 옴(mange) 치료에 권했다고 소개된다[5]. "
 "헝가리 민간에서는 별꽃차가 대사를 돕고 혈당을 낮춘다고 전해져 이를 확인하려는 쥐 실험이 이루어졌다[6]. "
 "히말라야 일대에서는 샐러드 나물로 즐겨 먹고, 별꽃 물을 비만 민간요법으로 썼다[4]. "
 "인도 서히말라야 구자르족 조사에서는 식용 식물로서의 충실도(fidelity) 값이 100%였다[21].\n\n"
 "한국에서는 별꽃이 흉년에 먹던 구황 식물 여섯 종 가운데 하나로 소개되었다[20]. "
 "스페인 발렌시아 해안에서는 가을–겨울에 나는 야생 나물로 생샐러드·우림차·수프·양념·스튜에 쓰고, 이탈리아 중부에서는 닭 모이와 어린 양 먹이로 썼다[3, 22]. "
 "북유럽 '뉴 노르딕 식단'에도 야생 식물로 들어가 안전성 평가 대상이 되었다[10].")
S["biology"] = ("별꽃은 가을에 싹이 트고 5–10월에 꽃이 피며, 연약하고 휘어지는 줄기와 달걀꼴 잎, 꽃잎이 깊게 갈라진 작은 흰 꽃을 단다[2]. "
 "키는 40 cm까지 자라고 습하고 질소가 많은 땅, 풀밭·잔디밭·쓰레기 버리는 곳에서 잘 자라며, 줄기 한쪽 면에 가는 털이 줄지어 난다[2]. "
 "원산지는 유럽이지만 사람의 활동으로 세계에 퍼져 가장 널리 퍼진 잡초 가운데 하나가 되었고, 주로 흙 속에 쌓인 씨앗으로 번식한다[3].\n\n"
 "씨앗은 재배 작물 씨앗보다 좁은 온도 범위에서만 최대 발아율을 보였고, 발아는 수분·온도를 함께 고려한 '수열 시간' 모델로 잘 설명되었다[27]. "
 "저온에 두면 줄기에 라피노스·리크노스·스텔라리오스 같은 갈락토올리고당이 쌓이는데, 석죽과에는 흔한 스타키오스가 없다[17]. "
 "씨앗에서는 곰팡이·난균을 1 μM 이하 농도에서 억제하는 디펜신 Sm-AMP-D1·D2가 분리되었다[25]. "
 "겨울 잡초로서 토마토반점위조바이러스를 옮기는 총채벌레의 번식처가 되며, 미국 노스캐롤라이나에서 넓게 분포했다[28].")
S["related_species"] = ("별꽃속(Stellaria)은 전 세계 약 112종이며 그중 약 64종이 중국에 있다[14]. "
 "별꽃속이 속한 별꽃족(Alsineae)은 석죽과에서 분류가 가장 어려운 무리로, 2023년 분자계통 연구는 19개 속을 인정했다[15]. "
 "별꽃 엽록체 게놈 비교 연구는 water chickweed(Myosoton aquaticum)가 속한 Myosoton 속을 별꽃속에 넣고 Stellaria dichotoma var. lanceolata는 별꽃속에서 빼야 한다고 제안했다[13].\n\n"
 "식약처 목록에는 같은 속의 다른 원료가 따로 올라 있다: 벼룩나물순(S. alsine var. undulata, 순), 왕별꽃순(S. radians, 순), Star chickweed잎(S. pubera), Stellaria jamesiana·neglecta·nipponica·diversiflora·sessiliflora잎(잎)은 별꽃과 다른 원료다[1]. "
 "영어 'chickweed'는 점나도나물(Cerastium holosteoides var. hallaisanense, Common mouse-ear chickweed)이나 Drymaria cordata(West Indian chickweed) 같은 다른 속에도 쓰여 이름만으로는 섞이기 쉽다[1]. "
 "'별꽃'이 들어간 별꽃아재비(Galinsoga parviflora)와 '개별꽃'류(Pseudostellaria)도 별꽃속이 아니며, 가는잎개별꽃의 이명에만 Stellaria sylvatica가 있다[1].")
S["cultivation"] = ("별꽃은 따로 재배하는 작물보다 밭·정원에 저절로 나는 잡초이며, 연구에 쓴 시료도 대부분 야생에서 채취했다[3, 5]. "
 "스페인 연구는 발렌시아 해안 농촌의 자연 서식지에서 생태 협동조합과 함께 지상부 약 1 kg을 채취했다[3]. "
 "헝가리 연구는 한 협회가 2017년에 수확한 지상부를 말려 썼고, 중국 연구는 난징 식물원에서 꽃 필 때 채취했다[5, 6].\n\n"
 "흙의 중금속을 잘 빨아들이므로 채취 장소가 중요하다: 파키스탄 히말라야의 야생 나물 조사에서 별꽃은 철과 카드뮴 농도가 높게 나타났다[23]. "
 "수경 재배에서는 용액 pH 5에서 새싹의 아연이 1640 μg/g 건조중량, pH 6.5에서 니켈이 250 μg/g 건조중량까지 쌓였다[24]. "
 "겨울 잡초로서 총채벌레와 바이러스의 겨울나기 장소가 될 수 있다[28]. "
 "국내 재배 면적·생산량 통계와 지리적 표시 등록은 확인하지 못함.")
S["processing"] = ("어린 잎과 순은 생으로 샐러드에 넣거나 가볍게 익혀 먹고, 말려서 차로 우린다[3, 6, 8]. "
 "헝가리 연구는 말린 지상부를 끓는 물(1:10)로 15분 초음파 추출해 동결건조했고, 동결건조물 1.5 g이 말린 풀 10 g에 해당했다[6]. "
 "이 연구는 사람의 권장량을 하루 차 2잔(잔당 말린 풀 3 g)으로 보고 쥐 용량 100 mg/kg을 정했다[6]. "
 "인도 연구는 생풀 500 g을 갈아 거른 즙을 동결건조해 썼으며, 이 분말의 수분은 9%, 총회분은 20.5%였다[4]. "
 "중국 연구는 생즙을 거대다공성 수지와 한외여과로 나눠 플라보노이드·다당·단백질 분획을 만들었다[5].\n\n"
 "추출 용매에 따라 성분이 달라, 지상부의 에탄올·에틸아세테이트 추출물의 총페놀은 22.76·22.71 mg GAE/g, 물 추출물은 14.22 mg GAE/g이었다[8]. "
 "뜨거운 물 추출물의 총플라보노이드는 9.88 mg 퀘르세틴 당량/g이었고 직접 항산화력은 약했다[6]. "
 "식약처 「식품 등의 생산실적」에서 별꽃을 원료명으로 한 건강기능식품 품목은 확인하지 못함.")
S["genetics"] = ("독도에서 채집한 별꽃의 엽록체 게놈은 147,329 bp로, 두 역반복 부위(각 25,600 bp)와 큰 단일 복제 부위(79,366 bp), 작은 단일 복제 부위(16,763 bp)로 이루어졌다[13]. "
 "유전자는 129개(단백질 84, rRNA 8, tRNA 37)였고, ycf1·ndhF-rpl32·trnK-rps16이 종 구분 표지 후보로 제시되었다[13]. "
 "별꽃속 60개 엽록체 게놈의 길이는 147,205–149,409 bp, GC 비율은 36.6–36.7%로 구조가 잘 보존되어 있었다[14].\n\n"
 "곰팡이에 감염된 별꽃 어린 식물의 전사체 분석에서 디펜신·티오닌·헤베인 유사 펩타이드·알파-헤어피닌 등 항균 펩타이드 후보 145개가 예측되었다[26]. "
 "알파-헤어피닌과 헤베인 유사 펩타이드는 다른 석죽과 식물과 구별되는 별꽃 특유의 항균 펩타이드로 보였다[26]. "
 "디펜신 Sm-D1 유전자는 게놈에 2개 있으며 신호 펩타이드 부분에 599 bp 인트론 하나를 가진다[25]. "
 "헤베인 유사 펩타이드 유전자(pro-SmAMP1)를 넣은 감자는 3년 재배 동안 겹둥근무늬병(early blight)에 강했다[34]. "
 "별꽃의 핵 게놈 해독과 염색체 수는 이번 조사에서 확인하지 못함.")
S["safety"] = ("식약처 목록에서 별꽃은 순에 한해 사용가능한 식품원료(A코드)이며, 이 종을 원재료로 하는 고시형 원료는 없어 고시 섭취 시 주의사항도 확인하지 못함. "
 "질산염: 스페인 야생 별꽃 생잎의 질산염은 75.62 mg NO₃/kg 생중량이었고, 저자들은 하루 허용량(체중 kg당 3.65 mg)을 넘기기 어려워 건강 위험이 없다고 판단했다[3]. "
 "스페인 남동부 야생 나물 16종 연구는 질산염이 47–597 mg/100 g 범위라고 했으나, 초록에 별꽃 값이 따로 없어 별꽃의 값은 확인하지 못함. "
 "리뷰는 별꽃의 질산염이 어지럼·두통·호흡곤란 등을 일으킬 수 있다고 적었지만 정량 근거는 제시하지 않았다[2].\n\n"
 "사포닌: 생즙 동결건조물의 총사포닌은 HPLC로 1.19 μg/g(글리시리진산 기준), 용혈 활성은 0.66 단위/g이었다[4]. "
 "북유럽 식단 평가는 별꽃의 성분 위해를 대부분 '경미'로 보고, 주의가 필요한 것은 옥살산이 많은 흰명아주뿐이라고 했다[10]. "
 "쥐에게 별꽃차 100 mg/kg을 먹였을 때 간·신장 기능과 심장 형태·기능은 변하지 않았다[7].\n\n"
 "접촉피부염: 텃밭 잡초를 만진 뒤 다형홍반이 반복된 환자에서 생별꽃 잎 첩포시험이 양성이었고 빛에 악화되었다[11]. "
 "피부질환자 등 235명 첩포시험에서는 식물 알레르기 반응 14명 중 4명이 별꽃 추출물에 반응했다[12]. "
 "파키스탄 야생 나물 조사에서 별꽃은 철·카드뮴이 높았으므로 오염 지역 채취는 피하는 것이 좋다[23]. "
 "국내 공공기관의 알레르기·잔류농약 정보는 확인하지 못함.")

titles = {"overview":"한눈에 보기","history":"역사와 전통 이용","biology":"식물학적 특징","related_species":"이름과 가까운 종","cultivation":"자생과 채취","processing":"가공과 이용","genetics":"유전 정보","safety":"안전성"}
sections = [{"key":k,"title":titles[k],"body":S[k]} for k in titles]

def c(name, ko, cls, role, part, content, act, src):
    return {"name":name,"name_ko":ko,"class":cls,"role":role,"part":part,"content_text":content,"activity_ko":act,"source":src}
compounds = [
 c("Vitexin","비텍신(아피게닌-8-C-글루코사이드)","플라본 C-배당체","marker","지상부(생즙 분획)","LC-MS로 [M+H]+ 433.11 확인(개별 함량은 보고 없음); 분획의 총플라보노이드:총당:단백질 = 1:11.86:16.70[5]","항-B형간염바이러스 활성 분획(SM-3)의 주요 UV 흡수 성분(세포 실험)[5]",[5]),
 c("Isovitexin","이소비텍신 배당체(이소비텍신 7,2″-디-O-글루코사이드 등)","플라본 C-배당체","bioactive","지상부","별꽃에서 6종의 아피게닌 C-배당체 유도체를 분리(함량은 초록에 없음)[18]","분리한 별꽃 유래 C-배당체 6종은 항산화 활성이 없었음(시험관)[18]",[18]),
 c("Vicenin-2","비세닌-2(아피게닌-6,8-디-C-글루코사이드)","플라본 C-배당체","bioactive","지상부(뜨거운 물 추출물)","LC-MS/MS 스펙트럼 라이브러리 일치도 82.8(함량 보고 없음)[6]; 잎 추출물에서 보고됨(리뷰)[2]","별꽃차의 당뇨성 심기능 보호 후보 성분으로 제시(쥐)[6]",[6,2]),
 c("Schaftoside","샤프토사이드(또는 이성질체 코림보사이드)","플라본 C-배당체","bioactive","지상부(뜨거운 물 추출물)","m/z 595.1660 성분이 두 이성질체와 유사(일치도 62.9), 함량 보고 없음[6]","아피게닌 배당체 군의 하나로 제시[6]",[6]),
 c("Rutin","루틴","플라보놀 배당체","bioactive","지상부(뜨거운 물 추출물)","UPLC 머무름 시간·UV 스펙트럼 비교로 '있을 가능성' 제시(정량 없음)[6]","당뇨성 심근병증 완화 보고가 있는 성분으로 인용[6]",[6]),
 c("Apigenin","아피게닌","플라본","bioactive","잎·지상부","잎 정제 분획 GC-MS에서 보고(리뷰)[2]; 지상부 추출물 UHPLC-MS/MS에서 아피게닌 유도체 다수 동정[8]","배당체가 장에서 분해된 뒤 흡수되는 아글리콘으로 제시[6]",[2,8,6]),
 c("Stellariose","스텔라리오스","갈락토올리고당(오당류)","marker","줄기","저온 처리 시 줄기에 축적(함량은 초록에 없음)[17]; Gal α(1→4)Glc 결합을 가진 첫 천연물로 보고[16]","석죽과에서 스타키오스 대신 쌓이는 저장당; 생리활성은 확인하지 못함[17]",[16,17]),
 c("Lychnose","리크노스","갈락토올리고당(사당류)","nutrient","줄기","저온 처리 시 라피노스·스텔라리오스와 함께 축적[17]","스텔라리오스의 골격이 되는 사당류[16]",[17,16]),
 c("Gypsogenin","집소게닌(트라이테르페노이드 사포닌 아글리콘)","트라이테르페노이드 사포닌","bioactive","지상부","별꽃에서 분리된 사포닌 성분으로 리뷰에 정리[2]; 생즙 동결건조물 총사포닌 1.19 μg/g(HPLC, 글리시리진산 기준)[4]","총사포닌·플라보노이드가 췌장 리파아제 억제에 관여한다고 추정(쥐)[4]",[2,4]),
 c("Oleanolic acid","올레아놀산","트라이테르페노이드","bioactive","지상부","별꽃에서 분리된 트라이테르페노이드로 리뷰에 정리(함량 없음)[2]; 올레아난형 새 트라이테르페노이드 배당체도 분리[19]","올레아난형 사포닌의 기본 골격[4]",[2,19,4]),
 c("beta-Sitosterol","베타-시토스테롤","식물스테롤","bioactive","전초(메탄올 추출물)","얇은막크로마토그래피로 존재 확인(함량 없음)[29]","지방 흡수를 경쟁적으로 줄여 항비만 효과에 일부 기여한다고 추정(생쥐)[29]",[29]),
 c("beta-Carotene","카로틴(베타-카로틴 등)","카로티노이드","nutrient","잎","카로틴 4.2 mg/100 g(조사한 야생 나물 16종 가운데 가장 낮음)[9]","프로비타민 A[9]",[9]),
 c("Potassium","칼륨","무기질","nutrient","생잎","710.1 ± 99.7 mg/100 g 생중량[3]","나트륨(24.8 mg/100 g)보다 훨씬 많아 Na/K 비가 낮음[3]",[3]),
]
nutrients = [{"form":"생잎(스페인 발렌시아 해안 야생, 가을–겨울 채취)","basis":"생중량 100 g당, 논문 표 2의 평균값[3]","items":[
 {"name":"수분","value":91.64,"unit":"g"},{"name":"회분","value":2.01,"unit":"g"},{"name":"단백질","value":0.20,"unit":"g"},
 {"name":"지방","value":0.39,"unit":"g"},{"name":"섬유","value":1.22,"unit":"g"},{"name":"탄수화물","value":4.55,"unit":"g"},
 {"name":"열량","value":22.47,"unit":"kcal"},{"name":"칼슘","value":71.5,"unit":"mg"},{"name":"마그네슘","value":82.6,"unit":"mg"},
 {"name":"칼륨","value":710.1,"unit":"mg"},{"name":"인","value":44.7,"unit":"mg"},{"name":"나트륨","value":24.8,"unit":"mg"},
 {"name":"철","value":1.3,"unit":"mg"},{"name":"구리","value":0.1,"unit":"mg"},{"name":"아연","value":0.8,"unit":"mg"}],"source":[3]}]
E = lambda **k: {f: k.get(f, "") for f in ["instrument","column","mobile_phase","gradient","flow","temp","detection","injection","sample_prep","standard","linearity","lod","loq","recovery"]}
assays = [
 {"role":"literature","compound":"Total saponins (as glycyrrhizic acid)","compound_ko":"총사포닌(글리시리진산 당량)","part":"지상부 생풀 착즙 동결건조물(인도 하리아나주 채취)",
  "content":"1.19 μg/g(동결건조 착즙)[4]","method":"HPLC-UV(등용매)",
  "conditions":E(instrument="Agilent 1260 Infinity(원문: 1260 DVD-VL/1260 ALS/1260 Binary pump, UV/가시광 검출기)",column="Zorbax Eclipse XDB-C18, 4.6 × 250 mm, 5 μm(원문 표기 'Eclise')",
   mobile_phase="메탄올:물:아세트산 = 60:34:6 (v/v)",gradient="등용매",flow="1.5 mL/min",temp="25 °C",detection="245 nm",injection="20 μL",
   sample_prep="동결건조 착즙 2 g + 진한 NH₄OH 2 mL 3분 혼합 → H₃PO₄로 pH 7.0 → 10% 디아스타아제 1 mL, 37 °C 30분 → 메탄올로 100 mL 정용 → Whatman No. 42 여과 → 0.45 μm 막 여과",
   standard="글리시리진산(Sigma), 피크 면적–농도 검량선"),
  "rationale":"올레아난형 트라이테르페노이드 사포닌을 항비만(리파아제 억제) 활성 성분으로 보고 정량한 것; 전문 확인, 직선성·검출한계·정량한계·회수율은 원문에 없음[4].",
  "source":[4],"url":"https://doi.org/10.1186/1472-6882-12-145","source_kind":"paper"},
 {"role":"literature","compound":"Nitrate","compound_ko":"질산염","part":"생잎(스페인 발렌시아 해안 야생)",
  "content":"75.62 ± 6.00 mg NO₃/kg 생중량(CV 7.9%)[3]","method":"이온선택성 전극 직접 측정",
  "conditions":E(instrument="pH & Ion-Meter GLP 22+ (Crison Instruments), 질산 이온 전극",
   sample_prep="생잎:물 = 1:2 (w/v), 30 °C 이하에서 기계식 분쇄 후 즉시 직접 측정",detection="질산 이온선택성 전극(전위차)"),
  "rationale":"잎채소의 질산염은 섭취를 줄이도록 권고되는 위해 지표여서 안전성 판단(하루 허용량 체중 kg당 3.65 mg)에 쓰임; 전문 확인, 검량·검출한계·회수율은 원문에 없음[3].",
  "source":[3],"url":"https://doi.org/10.7717/peerj.12488","source_kind":"paper"},
 {"role":"literature","compound":"Vitexin","compound_ko":"비텍신 등 플라본 C-배당체(아피게닌 + 헥소스 2개 / 헥소스·펜토스 각 1개 이성질체)","part":"지상부 생즙의 거대다공성 수지·한외여과 분획 SM-3(중국 난징, 개화기 채취)",
  "content":"개별 정량 없음; SM-3의 총플라보노이드(아피게닌 기준 UV):총당:단백질 = 1:11.86:16.70[5]","method":"HPLC-DAD-ESI-MS(이온트랩)",
  "conditions":E(instrument="Agilent 1100 HPLC + Thermo LXQ 이온트랩 질량분석기(ESI)",column="Altima C(원문 표기) 250 mm × 4.6 mm, 5 μm",
   mobile_phase="A: 0.1% 포름산 수용액, B: 메탄올",gradient="0–3분 A 75→70%, 3–30분 70→55%, 30–35분 55→50%, 35–40분 50→75%",flow="1 mL/min",temp="35 °C",
   detection="DAD 280·330 nm; ESI 건조 가스 질소 80 mL/min, 350 °C, 소스 전압 −3,500 V, m/z 100–1,500; 비텍신 [M+H]+ 433.11, 이당 C-배당체 [M+H]+ 595·565",
   sample_prep="생풀 5 kg을 증류수 5,000 mL와 25 °C에서 균질화 → 나일론 망 여과 → 5,000 ×g 15분 원심 → 거대다공성 수지·한외여과로 분획",
   standard="총플라보노이드: 아피게닌; 총당: 포도당(페놀-황산법); 단백질: 소혈청알부민(Bradford)"),
  "rationale":"석죽과 특유의 C-배당체 플라본이 항바이러스 분획의 UV 흡수 성분 대부분을 차지해 성분 확인 지표로 쓰임; 전문 확인, 개별 성분 정량·검출한계·회수율은 없음[5].",
  "source":[5],"url":"https://doi.org/10.3390/molecules17078633","source_kind":"paper"},
]
d = {"slug":"stellaria-media","name_ko":"별꽃","name_en":"Common chickweed","scientific_name":"Stellaria media (L.) Vill.",
 "aliases":["별꽃순","Chickweed","Common chickweed","Alsine media L.","Stellaria media var. minor Makino"],
 "sections":sections,"compounds":compounds,"markers":[],"nutrients":nutrients,"assays":assays,"production":[],"world":[],"gi":[],"orgs":[],"sources":sources}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in sections: print(s["key"], len(s["body"]))
