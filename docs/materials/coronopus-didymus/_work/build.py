import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
A = "2026-11-02"
def pm(n, title, doi, pmid, note, pmc=None):
    ids = f"PMID {pmid}" + (f", {pmc}" if pmc else "")
    url = f"https://doi.org/{doi}" if doi else f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
    return {"n": n, "title": f"{title} ({ids}, {note})", "url": url, "publisher": "PubMed", "accessed": A}
S = [
 {"n": 1, "title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 냄새냉이잎(Coronopus didymus (L.) Sm., Lesser Swinecress) 사용가능·사용가능부위: 잎; 같은 목록의 Crowfoot(Coronopus squamatus)·마카·다닥냉이·콩다닥냉이·들다닥냉이 행 포함 (로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json)", "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
 pm(2, "Fruit fracture biomechanics and the release of Lepidium didymum pericarp-imposed mechanical dormancy by fungi — Nat Commun 2017;8:1868", "10.1038/s41467-017-02051-9", "29192192", "전문 확인", "PMC5709442"),
 pm(3, "Benzyl thiocyanate taint in the milk of dairy cattle ingesting Coronopus didymus Sm. — Nature 1965;207(997):640", "10.1038/207640a0", "5894254", "초록 없음·제목만 확인"),
 pm(4, "Anti-inflammatory evaluation of Coronopus didymus in the pleurisy and paw oedema models in mice — J Ethnopharmacol 2010;128(2):519-25", "10.1016/j.jep.2009.12.017", "20026396", "초록 확인"),
 pm(5, "Medicinal plants traditionally used in the northwest of the Basque Country (Biscay and Alava), Iberian Peninsula — J Ethnopharmacol 2014;152(1):113-34", "10.1016/j.jep.2013.12.038", "24389558", "초록 확인"),
 pm(6, "Bioassay-guided isolation of cytotoxic flavonoids from aerial parts of Coronopus didymus — J Ethnopharmacol 2017;194:971-980", "10.1016/j.jep.2016.10.074", "27989879", "초록 확인"),
 pm(7, "Isolation, separation, identification, and quantification of bioactive methylated flavone regioisomers by UHPLC-MS/MS — Anal Sci Adv 2021;2(7-8):364-372", "10.1002/ansa.202100016", "38715961", "전문 확인", "PMC10989521"),
 pm(8, "Measurement of total phenolic content and antioxidant activity of aerial parts of medicinal plant Coronopus didymus — Asian Pac J Trop Med 2017;10(8):792-801", "10.1016/j.apjtm.2017.07.024", "28942828", "초록 확인"),
 pm(9, "Polyphenolic Composition, Antioxidant, Antiproliferative and Antidiabetic Activities of Coronopus didymus Leaf Extracts — Molecules 2022;27(19):6263", "10.3390/molecules27196263", "36234800", "전문 확인", "PMC9570767"),
 pm(10, "HPLC-DAD analysis, anti-inflammatory and anti-arthritic potentials of Coronopus didymus extracts: effects on pro- and anti-inflammatory cytokines, COX-2, I-κβ, NF-κβ and oxidative stress biomarkers — Food Funct 2022;13(11):6244-6258", "10.1039/d2fo00207h", "35587790", "초록 확인"),
 pm(11, "Appraisal of anti-arthritic potential of Coronopus didymus (L.) Sm. aqueous extract and its safety study in Wistar rats — Inflammopharmacology 2023;31(6):3167-3182", "10.1007/s10787-023-01374-y", "37962695", "초록 확인"),
 pm(12, "Antiallergic, antipyretic, hypoglycemic and hepatoprotective effects of aqueous extract of Coronopus didymus Linn. — Biol Pharm Bull 2005;28(3):468-72", "10.1248/bpb.28.468", "15744070", "초록 확인"),
 pm(13, "Bioactivity-guided fractionation of Coronopus didymus: a free radical scavenging perspective — Phytomedicine 2006;13(8):591-5", "10.1016/j.phymed.2005.07.003", "16920515", "초록 확인"),
 pm(14, "Evaluation and optimization of radioprotective activity of Coronopus didymus Linn. in gamma-irradiated mice — Int J Radiat Biol 2006;82(8):525-36", "10.1080/09553000600876686", "16966180", "초록 확인"),
 pm(15, "Effect of O-glycosilation on the antioxidant activity and free radical reactions of a plant flavonoid, chrysoeriol — Bioorg Med Chem 2003;11(13):2677-85", "10.1016/s0968-0896(03)00232-3", "12788341", "초록 확인"),
 pm(16, "Inhibitory effect of medicinal herbs against RNA and DNA viruses — Antivir Chem Chemother 2004;15(3):153-9", "10.1177/095632020401500305", "15266897", "초록 확인"),
 pm(17, "Tolerance and hyperaccumulation of cadmium by a wild, unpalatable herb Coronopus didymus (L.) Sm. (Brassicaceae) — Ecotoxicol Environ Saf 2017;135:209-215", "10.1016/j.ecoenv.2016.10.001", "27744137", "초록 확인"),
 pm(18, "Effect of lead on oxidative status, antioxidative response and metal accumulation in Coronopus didymus — Plant Physiol Biochem 2016;105:290-296", "10.1016/j.plaphy.2016.05.019", "27214085", "초록 확인"),
 pm(19, "Phytoremediation of lead by a wild, non-edible Pb accumulator Coronopus didymus (L.) Brassicaceae — Int J Phytoremediation 2018;20(5)", "10.1080/15226514.2017.1374331", "29020458", "초록 확인"),
 pm(20, "Insights into the tolerance and phytoremediation potential of Coronopus didymus L. (Sm) grown under zinc stress — Chemosphere 2020;244:125350", "10.1016/j.chemosphere.2019.125350", "31830642", "초록 확인"),
 pm(21, "Cytological studies of Brassicaceae Burn. (Cruciferae Juss.) from Western Himalayas — Tsitol Genet 2013;47(1):26-36", None, "23427609", "초록 확인"),
 pm(22, "Microsatellite loci in the Gypsophyte Lepidium subulatum (Brassicaceae), and transferability to other Lepidieae — Int J Mol Sci 2012;13(9):11861-11869", "10.3390/ijms130911861", "23109887", "초록 확인", "PMC3472779"),
 pm(23, "Cytoskeletal organization of the micropylar endosperm in Coronopus didymus L. (Brassicaceae) — Protoplasma 2002;219(3-4):210-20", "10.1007/s007090200022", "12099221", "초록 확인"),
 pm(24, "Diversity, distribution and role of wild crucifers in major cabbage and kale growing areas of Kenya — Bull Entomol Res 2008;99(3):287-97", "10.1017/S0007485308006305", "19063754", "초록 확인"),
 pm(25, "Weed Species as Hosts of Sclerotinia minor in Peanut Fields — Plant Dis 2003;87(2):197-199", "10.1094/PDIS.2003.87.2.197", "30812927", "초록 확인"),
 pm(26, "First Report of Tomato torrado virus on Weed Hosts in Spain — Plant Dis 2008;92(5):831", "10.1094/PDIS-92-5-0831B", "30769603", "초록 확인"),
 pm(27, "Light microscopy and scanning electron microscopy: Implications for authentication of misidentified herbal drugs — Microsc Res Tech 2019", "10.1002/jemt.23344", "31342627", "초록 확인"),
 pm(28, "Antidiabetic Effect of Coronopus Didymus, Azadirachta Indica and Their Active Compound Quercetin Against STZ-NA Induced Diabetes Mice Models — Appl Biochem Biotechnol 2026;198(11):8482-8507", "10.1007/s12010-026-05851-2", "42496827", "초록 확인"),
 pm(29, "Membrane based reactors for sustainable treatment of Coronopus didymus L. by developing Iodine doped potassium oxide catalyst under dynamic conditions — Chemosphere 2022", "10.1016/j.chemosphere.2022.135138", "35636597", "초록 확인"),
 pm(30, "Bioassays guided fractionation of Coronopus didymus for its antifungal activity against Sclerotium rolfsii — Nat Prod Res 2012;26(17):1638-44", "10.1080/14786419.2011.587421", "22007784", "초록 확인"),
 pm(31, "Biological activities of three medicinal plants from district Mirpur, AJK, Pakistan — Pak J Pharm Sci 2018;31(6):2341-2346", None, "30473502", "초록 확인"),
]
sections = [
 ("overview", "한눈에 보기", """냄새냉이(Coronopus didymus (L.) Sm.)는 십자화과(Brassicaceae)의 풀로, 영어로 lesser swinecress라 불리며 남아메리카에서 기원해 모든 대륙에 퍼진 잡초다[1, 2]. 식약처 「식품원료 목록」에는 원료명 '냄새냉이잎'(영문명 Lesser Swinecress) 한 행이 '사용가능' 상태로 올라 있고, 사용 조건은 '사용가능부위 : 잎'이다[1]. 따라서 식품에 쓸 수 있는 부위는 잎뿐이며, 이 종을 원재료로 하는 건강기능식품 고시형 원료는 목록에서 찾지 못했다[1].

최근 분류에서는 다닥냉이속에 넣어 Lepidium didymum L.로 부르며, 이때 Coronopus didymus (L.) Smith는 그 이명이 된다[2]. 성분 연구는 주로 지상부나 전초를 대상으로 했고, 메톡시 플라본인 크리소에리올(chrysoeriol)과 그 배당체가 분리·정량되었다[6, 7, 15]. 동물 시험에서는 전초 물 추출물의 해열·항알레르기·간 보호·혈당 저하[12], 잎 수알코올 추출물의 항염[4], 추출물의 관절염 완화[10, 11] 효과가 보고되었고, 전초 물 추출물의 비극성 분획은 생쥐 복강 주사에서 방사선 방호 효과를 보였다[13, 14]. 잎만 따로 분석한 성분 정량 자료와 사람 대상 임상시험은 확인하지 못함."""),
 ("history", "역사와 쓰임", """브라질 남동부에서는 'mastrunço'라는 이름으로 통증과 염증이 따르는 여러 질환에 쓰며, 우리거나 달이거나 음식으로 먹는다고 보고되었다[4]. 스페인 바스크 지방 북서부의 민간요법 면담 조사(2008–2011년)에서는 냄새냉이가 다른 유럽 지역에서는 드물게 쓰이는 이 지역의 독특한 약용식물로 기록되었다[5]. 남아시아 쪽 연구는 해열·거담·혈액 정화와 통증·염증·말라리아·상처·암 증상 완화에 전통적으로 써 왔다고 적는다[6].

생약 시장에서는 'Halion'이라는 같은 이름으로 Lepidium apetalum, 아스파라거스, Lepidium didymum 세 종이 함께 팔려, 진짜 원료는 L. apetalum이고 L. didymum은 잘못 섞인 것으로 보고되었다[27]. 낙농 지역에서는 젖소가 이 풀을 먹으면 우유에서 벤질 티오시아네이트(benzyl thiocyanate) 냄새가 난다는 문제가 1965년에 보고되었고, 지금도 낙농 초지의 문제 잡초로 꼽힌다[2, 3]. 실험실 연구로는 소 바이러스성 설사 바이러스(BVDV-1)에 대한 선택지수 110.7[16], 식물병원균 Sclerotium rolfsii 생장 억제[30], 곰팡이 Aspergillus niger 48% 억제[31] 등이 보고되었다. 한국에서 냄새냉이를 나물이나 약초로 먹어 온 기록은 확인하지 못함."""),
 ("biology", "식물학적 특징", """열매는 두 개의 분과(fruit valve)가 쌍으로 붙은 '쌍구형(didymous)' 열매이고, 분과마다 단단한 과피가 씨앗 하나를 감싼다[2]. 과피의 바깥층(외과피·중과피)은 살아 있는 유조직이고, 안쪽 내과피는 두껍게 목질화된 죽은 세포층이다[2]. 이 단단한 과피는 씨앗이 물을 끝까지 흡수하지 못하게 막아 발아를 수개월 늦추며, 흔한 토양 자낭균류가 바깥 과피를 분해하면 미리 정해진 '파단 구역'이 약해져 발아가 앞당겨진다[2].

과피에서 꺼낸 씨앗은 휴면이 없어 8–21 °C에서 잘 싹텄고, 낮/밤 15/5 °C가 가장 알맞았다[2]. 소독한 열매는 발아 시작까지 약 120일이 걸렸지만 곰팡이가 붙은 열매는 약 35일 만에 과피가 갈라졌다[2]. 토양 종자은행에서 5–10년 살아남고, 땅을 갈아엎은 뒤 몇 주 안에 싹이 무더기로 올라오는 개척종이다[2]. 배 발달 과정에서는 주공 쪽 배젖 핵을 독특한 평행 미세소관 다발이 감싸는 구조가 관찰되었다[23]. 잎 모양·꽃 구조·크기 등 형태 기재는 공공기관 자료로 확인하지 못함."""),
 ("related_species", "이름과 가까운 종", """식약처 목록의 학명은 Coronopus didymus (L.) Sm.이고, 다닥냉이속에 합치는 견해에서는 Lepidium didymum L.을 쓰며 C. didymus를 그 이명으로 둔다[1, 2]. 스페인의 식물병 보고에서는 옛 이름 Senebiera didyma Pers.가 쓰였다[26]. 2017년 연구는 다닥냉이속(약 250종)의 기본 형태가 열리는 열매이고, 냄새냉이 같은 쌍구형 닫힌 열매는 속 안에서 여러 번 따로 생겨났다고 설명한다[2].

같은 Coronopus 속의 Crowfoot(Coronopus squamatus)은 식약처 목록에 뿌리·잎 사용가능 원료로 따로 올라 있으며, 이 문서는 그 자료를 섞지 않았다[1]. 다닥냉이속의 마카(Lepidium meyenii)·다닥냉이(L. apetalum)·콩다닥냉이(L. virginicum)·들다닥냉이(L. campestre)도 목록에서 별도 원료이므로 이 문서에 넣지 않았다[1]. 'Halion'이라는 상품명 아래 L. apetalum과 L. didymum이 뒤섞인 사례가 있어 현미경·화분 형태로 구별해야 한다는 보고가 있다[27]. 국가표준식물목록의 국명 등재 여부와 국내 귀화 기록은 공공기관 자료로 확인하지 못함."""),
 ("cultivation", "재배와 생산", """냄새냉이는 재배 작물이 아니라 밭·초지·빈터에 저절로 나는 잡초로 다뤄지며, 한대부터 열대까지 모든 대륙에 분포한다[2]. 싹은 생장기 전체에 걸쳐 나오되 봄·가을에 많고, 서늘한 온도를 좋아한다[2]. 케냐의 양배추·케일 산지 조사에서는 야생 십자화과 13종 가운데 하나로 기록되었고, 이런 야생 십자화과는 배추좀나방의 대체 기주가 된다[24].

미국 노스캐롤라이나 땅콩밭에서는 균핵병균 Sclerotinia minor의 자연 기주로 확인되었다[25]. 스페인 토마토 온실 주변에서는 토마토 토라도 바이러스(ToTV)가 이 풀에서 검출되었다[26]. 인도에서는 중금속 오염 토양을 정화하는 식물로 화분 재배 시험이 여러 차례 이루어졌다[17–20]. 국내 재배 면적·생산량은 통계청·농림축산식품부 생산 통계에서 확인하지 못함."""),
 ("processing", "가공과 제품", """식약처 목록에 따라 식품에는 잎만 쓸 수 있으며, 냄새냉이잎을 쓴 국내 가공식품이나 건강기능식품 생산 실적은 찾지 못했다[1]. 브라질에서는 잎을 우리거나 달이거나 음식에 넣어 먹는다고 보고되었다[4]. 연구용 추출은 대개 그늘에 말린 지상부나 전초를 에탄올·메탄올·아세톤 또는 물로 우려내는 방식이었다[7, 9, 11].

한 연구는 말린 지상부 10 g을 에탄올 100 mL에 96시간 담근 뒤 초음파 30분, 45 °C 감압 농축으로 조추출물 2.0 g을 얻었다[7]. 다른 연구는 말린 전초 가루 1 g을 용매에 하룻밤 담가 추출했고, 주요 폴리페놀 함량은 메탄올 추출물에서 가장 높았다[9]. 총 페놀 함량은 에탄올 추출물이 47.8 mM GAE로 가장 높고 디클로로메탄 추출물이 3.13 mM GAE로 가장 낮았다[8]. 씨기름은 비식용 유지로 보아 바이오디젤 원료로 시험되었고, 최적 조건에서 전환 수율 97.03%가 보고되었다[29]."""),
 ("genetics", "유전과 육종", """인도 서부 히말라야(카슈미르·히마찰프라데시) 집단의 세포학 연구에서 냄새냉이 집단의 감수분열은 정상부터 비정상까지 집단에 따라 달랐다[21]. 이 연구에서 감수분열이 비정상인 집단은 꽃가루 크기가 고르지 않고 생식력이 떨어지는 경향을 보였다[21]. 다닥냉이속 Lepidium subulatum용으로 개발된 마이크로새틀라이트 12개 좌위는 냄새냉이에서도 증폭되어, 유전 다양성 연구에 옮겨 쓸 수 있다고 보고되었다[22].

2017년 연구는 독일 오스나브뤼크 계통을 기준으로 유럽·아프리카·호주의 10개 계통을 비교했고, 곰팡이에 의한 과피 파열 촉진이 모든 계통에서 나타났다[2]. 쌍구형 닫힌 열매는 다닥냉이속 안에서 여러 차례 독립적으로 진화한 형질로 설명된다[2]. 냄새냉이의 품종 육성, 염색체 수, 유전체 해독 자료는 확인하지 못함."""),
 ("safety", "안전성", """식약처 목록의 상태는 '사용가능'이며, 사용 부위만 잎으로 정해져 있다[1]. 쥐 실험에서 물 추출물(초록에 부위 없음)의 반수치사량(LD50)은 2000 mg/kg 넘게 나왔고, 200–800 mg/kg을 반복 먹인 아급성 독성 시험에서 혈액·생화학·간·심장·신장·폐 조직 이상이 없었다[11]. 이는 동물 결과이고, 사람에서 확인한 안전성 자료와 알레르기·잔류농약에 관한 공공기관 정보는 확인하지 못함.

냄새냉이는 카드뮴·납·아연을 많이 쌓는 식물로 보고되었다[17–20]. 카드뮴 400 mg/kg 토양에서 지상부 864.5 mg/kg DW[17], 납 2900 mg/kg 토양에서 지상부 862.8 mg/kg DW[18], 아연 500 mg/kg 토양에서 지상부 1845 mg/kg DW가 측정되었다[20]. 이 값은 일부러 오염시킨 화분 흙 시험 결과지만, 오염된 땅에서 자란 잎에는 중금속이 쌓일 수 있음을 뜻한다[17–20]. 한 연구는 이 풀을 '먹지 않는(non-edible)' 야생 식물로, 다른 연구는 '가축이 기피하는(unpalatable)' 풀로 적었다[17, 19]. 젖소가 먹으면 우유에 냄새가 배는 문제도 있다[2, 3]."""),
]
compounds = [
 {"name": "Chrysoeriol", "name_ko": "크리소에리올(5,7,4'-트라이하이드록시-3'-메톡시플라본)", "class": "메톡시 플라본", "role": "marker", "part": "지상부", "content_text": "말린 지상부 10 g당 약 1.60 mg(에탄올 추출 후 Sephadex LH-20 분획 F10, 디오스메틴 표준품으로 상대 정량)[7]", "activity_ko": "HeLa 세포 IC50 3.67 µM, LN18 세포 IC50 46.63 µM(세포 시험)[6]; DPPH IC50 43.8 µg/mL, ABTS IC50 0.08 µg/mL(시험관)[8]; 지질과산화 억제(시험관)[15]", "source": [6, 7, 8, 15]},
 {"name": "Chrysoeriol 4'-O-glucoside", "name_ko": "크리소에리올-4'-O-β-D-글루코사이드", "class": "플라본 배당체", "role": "bioactive", "part": "지상부", "content_text": "지상부 에탄올 추출물에서 분리(함량 수치 없음), Coronopus 속에서 처음 보고[6]", "activity_ko": "HeLa 세포 IC50 43.50 µM(세포 시험)[6]", "source": [6]},
 {"name": "Chrysoeriol 4'-O-(6''-acetyl)-glucoside", "name_ko": "크리소에리올-4'-O-(6''-아세틸)-β-D-글루코사이드", "class": "플라본 배당체", "role": "bioactive", "part": "지상부", "content_text": "지상부에서 분리(함량 수치 없음)[6]; 전초 유래로 보고[15]", "activity_ko": "HeLa 세포 IC50 0.63 µM(세포 시험)[6]; DPPH 소거·잔틴 산화효소 억제는 비배당체보다 강하고 지질과산화 억제는 약함(시험관)[15]", "source": [6, 15]},
 {"name": "Quercetin", "name_ko": "쿼세틴", "class": "플라보놀", "role": "bioactive", "part": "전초(제목은 잎)", "content_text": "메탄올 추출물 975.7 mg/g 건조중량(원문 표기 그대로; 단위·기준이 비현실적이어서 검증 필요)[9]; 수에탄올 추출물에서 HPLC-DAD로 확인[10]", "activity_ko": "냄새냉이·님 추출물·쿼세틴 병용이 당뇨 생쥐에서 혈당과 간 효소(ALT·AST)를 낮춤(동물 시험, 개별 성분 효과 아님)[28]", "source": [9, 10, 28]},
 {"name": "Chlorogenic acid", "name_ko": "클로로겐산", "class": "하이드록시신남산 에스터", "role": "bioactive", "part": "전초(제목은 잎)", "content_text": "메탄올 추출물 305.02 mg/g 건조중량(원문 표기 그대로, 검증 필요)[9]", "activity_ko": "추출물 항산화 활성의 기여 성분으로 추정(시험관)[9]", "source": [9]},
 {"name": "Benzoic acid", "name_ko": "벤조산", "class": "방향족 카복실산", "role": "bioactive", "part": "전초(제목은 잎)", "content_text": "메탄올 추출물 428 mg/g 건조중량(원문 표기 그대로, 검증 필요)[9]", "activity_ko": "개별 활성 자료 없음[9]", "source": [9]},
 {"name": "Ferulic acid", "name_ko": "페룰산", "class": "하이드록시신남산", "role": "bioactive", "part": "전초", "content_text": "메탄올 추출물 23.33 mg/g 건조중량[9]; 수에탄올 추출물에서 HPLC-DAD로 확인[10]", "activity_ko": "추출물의 항염·관절염 완화 기여 성분으로 추정(동물 시험)[10]", "source": [9, 10]},
 {"name": "Kaempferol", "name_ko": "캠페롤", "class": "플라보놀", "role": "bioactive", "part": "전초", "content_text": "메탄올 추출물 11.5 mg/g 건조중량[9]; 수에탄올 추출물에서 확인[10]", "activity_ko": "추출물 활성 기여 성분으로 추정(동물 시험)[10]", "source": [9, 10]},
 {"name": "Apigenin", "name_ko": "아피제닌", "class": "플라본", "role": "bioactive", "part": "전초", "content_text": "수에탄올 추출물에서 HPLC-DAD로 확인(함량은 초록에 없음)[10]", "activity_ko": "추출물 항염 활성 기여 성분으로 추정(동물 시험)[10]", "source": [10]},
 {"name": "Vitexin", "name_ko": "비텍신", "class": "플라본 C-배당체", "role": "bioactive", "part": "전초", "content_text": "수에탄올 추출물에서 HPLC-DAD로 확인(함량은 초록에 없음)[10]", "activity_ko": "추출물 항염 활성 기여 성분으로 추정(동물 시험)[10]", "source": [10]},
 {"name": "Diosmetin", "name_ko": "디오스메틴", "class": "메톡시 플라본", "role": "bioactive", "part": "부위 미상(초록에 없음)", "content_text": "물 추출물에서 HPLC-DAD로 확인(함량은 초록에 없음)[11]", "activity_ko": "추출물 관절염 완화 기여 성분으로 추정(동물 시험)[11]", "source": [11]},
 {"name": "Gallic acid", "name_ko": "갈산", "class": "하이드록시벤조산", "role": "bioactive", "part": "부위 미상(초록에 없음)", "content_text": "물 추출물에서 HPLC-DAD로 확인(함량은 초록에 없음)[11]", "activity_ko": "추출물 관절염 완화 기여 성분으로 추정(동물 시험)[11]", "source": [11]},
 {"name": "Delphinidin 3-glucoside", "name_ko": "델피니딘-3-글루코사이드", "class": "안토시아닌", "role": "bioactive", "part": "부위 미상(초록에 없음)", "content_text": "물 추출물에서 HPLC-DAD로 확인(함량은 초록에 없음)[11]", "activity_ko": "추출물 관절염 완화 기여 성분으로 추정(동물 시험)[11]", "source": [11]},
 {"name": "Benzyl thiocyanate", "name_ko": "벤질 티오시아네이트", "class": "유기황 화합물", "role": "bioactive", "part": "(풀을 먹은 젖소의 우유)", "content_text": "젖소가 냄새냉이를 먹은 뒤 우유 이취의 원인 물질로 보고(논문 제목만 확인, 함량 확인하지 못함)[3]", "activity_ko": "우유 이취(off-flavour) 원인[2, 3]", "source": [2, 3]},
]
E = {k: "" for k in ["instrument","column","mobile_phase","gradient","flow","temp","detection","injection","sample_prep","standard","linearity","lod","loq","recovery"]}
c1 = dict(E, instrument="Waters Acquity UPLC + Waters Xevo G2-S Q-TOF 질량분석기", column="Merck Purospher STAR RP-18 end-capped, 3 µm, Hibar HR 50-2.1 mm", mobile_phase="A: 0.1% 포름산 수용액, B: 아세토니트릴", gradient="0–1.0분 5% B, 1.0–8.0분 5→99% B, 8.0–10.0분 99% B, 10.0–12.0분 5% B(총 12분)", flow="0.2 mL/min", detection="ESI 음이온, [M-H]⁻ m/z 299, 모세관 2 kV, 콘 60 V, 탈용매 400 °C, 소스 100 °C; MS/MS 충돌에너지 20–40 eV", injection="5 µL", sample_prep="말린 지상부 10 g을 에탄올 100 mL에 96시간, 초음파 30분, 45 °C 감압 농축(2.0 g) → 메탄올:물 7:3에 녹여 Sephadex LH-20(90×2.2 cm, 1 mL/min) 분획 F10", standard="5,7,3'-트라이하이드록시-4'-메톡시플라본(디오스메틴) 표준품으로 상대 정량(이온화 효율이 같다고 가정)", linearity="5–100 µg/mL, y = 128507x − 107121, R² 0.991", lod="1.26 µg/mL", loq="4.22 µg/mL")
c2 = dict(E, column="hydro-RP 80A, 250 × 4.60 mm, 4 µm", mobile_phase="A: 1% 아세트산·5% 아세토니트릴 수용액, B: 5% 메탄올 함유 아세토니트릴", gradient="A 82% : B 18% 등용매 40분", flow="1 mL/min", temp="실온", detection="UV 280 nm", injection="20 µL", sample_prep="그늘에 말린 전초 가루 1 g을 순수 메탄올(에탄올·아세톤)에 하룻밤 진탕 추출, 여과 후 용매 제거")
assays = [
 {"role": "literature", "compound": "Chrysoeriol", "compound_ko": "크리소에리올", "part": "지상부", "content": "말린 지상부 10 g당 약 1.60 mg[7]", "method": "UPLC-ESI-QTOF-MS/MS", "conditions": c1, "rationale": "지상부에서 반복해서 분리된 주된 메톡시 플라본이고 세포독성·항산화 활성의 주성분으로 보고되었다[6–8]. 전문에서 조건을 확인했으나 회수율·칼럼 온도는 적혀 있지 않고, 정량은 위치이성질체(디오스메틴) 표준품을 쓴 상대 정량이다[7]. 식품원료 부위인 잎만이 아니라 지상부 전체를 분석했다[7].", "source": [7], "url": "https://doi.org/10.1002/ansa.202100016", "source_kind": "paper"},
 {"role": "literature", "compound": "Quercetin", "compound_ko": "쿼세틴", "part": "전초(논문 제목은 잎)", "content": "메탄올 추출물 975.7 mg/g 건조중량(원문 표기 그대로)[9]", "method": "HPLC-UV", "conditions": c2, "rationale": "이 논문에서 가장 많이 검출된 폴리페놀이다[9]. 전문을 확인했으나 장비·표준품·검량선·검출한계·회수율이 적혀 있지 않고, 제목은 잎 추출물인데 방법에는 전초를 갈았다고 적혀 있으며, 보고된 함량(mg/g 건조중량)의 합이 1000을 넘어 단위·기준에 오류가 있을 가능성이 크다[9].", "source": [9], "url": "https://doi.org/10.3390/molecules27196263", "source_kind": "paper"},
 {"role": "literature", "compound": "Ferulic acid", "compound_ko": "페룰산", "part": "전초", "content": "함량 수치는 초록에 없음[10]", "method": "HPLC-DAD", "conditions": dict(E), "rationale": "수에탄올 추출물의 HPLC-DAD 분석에서 쿼세틴·디하이드로미리세틴·아피제닌·비텍신·캠페롤과 함께 확인되어 항염 활성 성분으로 제시되었다[10]. 전문 확인 못함[10].", "source": [10], "url": "https://doi.org/10.1039/d2fo00207h", "source_kind": "paper"},
]
d = {"slug": "coronopus-didymus", "name_ko": "냄새냉이", "name_en": "Lesser swinecress", "scientific_name": "Coronopus didymus (L.) Sm.",
     "aliases": ["냄새냉이잎", "Lepidium didymum L.", "Senebiera didyma Pers.", "Lesser swinecress", "Swinecress", "Mastrunço"],
     "sections": [{"key": k, "title": t, "body": b} for k, t, b in sections],
     "compounds": compounds, "markers": [], "assays": assays, "nutrients": [], "production": [], "world": [], "gi": [], "orgs": [], "sources": S}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for k, t, b in sections: print(k, len(b))
