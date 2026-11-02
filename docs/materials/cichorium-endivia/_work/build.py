import json
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "dossier.json"
ACC = "2026-11-02"


def pm(pmid):
    return f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"


def pmc(p):
    return f"https://pmc.ncbi.nlm.nih.gov/articles/{p}/"


S = [
    (1, "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 앤디브(Cichorium endivia L.)", "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "식품의약품안전처", "2026-10-13"),
    (2, "PROSEA(Plant Resources of South-East Asia)·PROTA — Cichorium endivia 항목 (WebSearch 요약으로만 확인, 원문 페이지는 네트워크 허용 목록 밖이라 열지 못함)", "https://uses.plantnet-project.org/en/Cichorium_endivia_(PROSEA)", "Pl@ntUse (PROSEA·PROTA 재수록)", ACC),
    (3, "Transcriptome driven characterization of curly- and smooth-leafed endives reveals molecular differences in the sesquiterpenoid pathway. Hortic Res. 2019", pmc("PMC6312536"), "Springer Nature (PMC)", ACC),
    (4, "The chromosome-scale assembly of endive (Cichorium endivia) genome provides insights into the sesquiterpenoid biosynthesis. Genomics. 2022", pm("35691507"), "PubMed", ACC),
    (5, "The genomes of chicory, endive, great burdock and yacon provide insights into Asteraceae palaeo-polyploidization history and plant inulin production. Mol Ecol Resour. 2022", pm("35751596"), "PubMed", ACC),
    (6, "The Chloroplast Genome of Endive (Cichorium endivia L.): Cultivar Structural Variants and Transcriptome Responses to Stress Due to Rain Extreme Events. Genes (Basel). 2023", pmc("PMC10531310"), "MDPI (PMC)", ACC),
    (7, "Genotyping by RAD Sequencing Analysis Assessed the Genetic Distinctiveness of Experimental Lines and Narrowed Down the Genomic Region Responsible for Leaf Shape in Endive (Cichorium endivia L.). Genes (Basel). 2020", pmc("PMC7231076"), "MDPI (PMC)", ACC),
    (8, "Genomics of Compositae crops: reference transcriptome assemblies and evidence of hybridization with wild relatives. Mol Ecol Resour. 2014", pm("24103297"), "PubMed", ACC),
    (9, "Bacterial Fertilizers Based on Rhizobium laguerreae and Bacillus halotolerans Enhance Cichorium endivia L. Phenolic Compound and Mineral Contents and Plant Development. Foods. 2021", pmc("PMC7919373"), "MDPI (PMC)", ACC),
    (10, "Characterization of Health Beneficial Components in Discarded Leaves of Three Escarole (Cichorium endivia L.) Cultivar and Study of Their Antioxidant and Anti-Inflammatory Activities. Antioxidants (Basel). 2023", pmc("PMC10376668"), "MDPI (PMC)", ACC),
    (11, "Hydroxycinnamic acid derivatives occurring in Cichorium endivia vegetables. J Pharm Biomed Anal. 2008", pm("18515031"), "PubMed", ACC),
    (12, "Identification of phenolic constituents in Cichorium endivia var. crispum and var. latifolium salads by HPLC-DAD and ESI-MS/MS. J Agric Food Chem. 2012", pm("23157223"), "PubMed", ACC),
    (13, "The impact of sesquiterpene lactones and phenolics on sensory attributes: An investigation of a curly endive and escarole germplasm collection. Food Chem. 2016", pm("26775966"), "PubMed", ACC),
    (14, "Fine monitoring of major phenolic compounds in lettuce and escarole leaves during storage. J Food Biochem. 2019", pm("31353660"), "PubMed", ACC),
    (15, "Terpene Lactucopicrin Limits Macrophage Foam Cell Formation by a Reduction of LOX-1 in Lipid Rafts. Mol Nutr Food Res. 2022", pm("34932892"), "PubMed", ACC),
    (16, "Hepatoprotective activity of Cichorium endivia L. extract and its chemical constituents. Molecules. 2011", pmc("PMC6264765"), "MDPI (PMC)", ACC),
    (17, "Potential Gonado-Protective Effect of Cichorium endivia and Its Major Phenolic Acids against Methotrexate-Induced Testicular Injury in Mice. Biomedicines. 2022", pmc("PMC9406180"), "MDPI (PMC)", ACC),
    (18, "Influence of cultivation sites on sterol, nitrate, total phenolic contents and antioxidant activity in endive and stem chicory edible products. Int J Food Sci Nutr. 2016", pm("27575665"), "PubMed", ACC),
    (19, "Determination of nitrates by a novel ion chromatographic method: occurrence in leafy vegetables (organic and conventional) and exposure assessment for Italian consumers. Food Addit Contam. 2003", pm("13129772"), "PubMed", ACC),
    (20, "[Compositae dermatitis]. Med Pregl. 2003", pm("12793186"), "PubMed", ACC),
    (21, "Occupational contact dermatitis from Cichorium (chicory, endive) and Lactuca (lettuce). Contact Dermatitis. 1975", pm("139250"), "PubMed", ACC),
    (22, "Inhalative occupational and ingestive immediate-type allergy caused by chicory (Cichorium intybus). Clin Exp Allergy. 1996", pm("8877160"), "PubMed", ACC),
    (23, "Comparison of carbohydrate partitioning and expression patterns of some genes involved in carbohydrate biosynthesis pathways in annual and biennial species of Cichorium spp. Phytochemistry. 2021", pm("33360645"), "PubMed", ACC),
    (24, "Leaf nutrient content and transcriptomic analyses of endive (Cichorium endivia) stressed by downpour-induced waterlog reveal a gene network regulating kestose and inulin contents. Hortic Res. 2021", pmc("PMC8087766"), "Springer Nature (PMC)", ACC),
    (25, "USDA FoodData Central — Endive, raw (SR Legacy, FDC ID 168412) (WebSearch 요약으로만 확인: USDA 값을 인용한 제3자 사이트 요약이며 USDA 원문은 네트워크 허용 목록 밖이라 열지 못함)", "https://fdc.nal.usda.gov/food-details/168412/nutrients", "미국 농무부(USDA) 농업연구청", ACC),
    (26, "Changes in Freshness of Endive (Cichorium endivia L.) by Different Packaging Types (WebSearch 요약으로만 확인, 원문 미열람)", "https://koreascience.or.kr/article/JAKO201610958456978.page", "KoreaScience(한국과학기술정보연구원)", ACC),
    (27, "Isolation and pulsed-field gel electrophoresis typing of Listeria monocytogenes from modified atmosphere packaged fresh-cut vegetables collected in Ireland. J Food Prot. 2006", pm("17066939"), "PubMed", ACC),
    (28, "Pesticide residues in cauliflower, eggplant, endive, lettuce, pepper, potato and wheat of the Slovene origin found in 2009. Acta Chim Slov. 2010", pm("24061906"), "PubMed", ACC),
    (29, "Screening and evaluation of active compounds in polyphenol mixtures by HPLC coupled with chemical methodology and its application. Food Chem. 2017", pm("28274421"), "PubMed", ACC),
    (30, "Sesquiterpenoids and phenolics from roots of Cichorium endivia var. crispum. Fitoterapia. 2006", pm("16797141"), "PubMed", ACC),
    (31, "Sesquiterpenes from the roots of Cichorium endivia. Chem Pharm Bull (Tokyo). 2008", pm("18827387"), "PubMed", ACC),
    (32, "Anti- and pro-oxidant water soluble activity of Cichorium genus vegetables and effect of thermal treatment. J Agric Food Chem. 2002", pm("12137499"), "PubMed", ACC),
    (33, "First Report of Fusarium Wilt of Endive (Cichorium endivia) Caused by Fusarium oxysporum in Italy. Plant Dis. 2009", pm("30754361"), "PubMed", ACC),
    (34, "Identification of a novel glycosyltransferase from Cichorium endivia L. and its application in the synthesis of fisetin-3'-O-glucoside. Int J Biol Macromol. 2025", pm("40615004"), "PubMed", ACC),
    (35, "The traditional medical uses and cytotoxic activities of sixty-one Egyptian plants: discovery of an active cardiac glycoside from Urginea maritima. J Ethnopharmacol. 2013", pm("23228916"), "PubMed", ACC),
    (36, "Effects of brassinosteroid analogues on total phenols, antioxidant activity, sugars, organic acids and yield of field grown endive (Cichorium endivia L.). J Sci Food Agric. 2013", pm("23184906"), "PubMed", ACC),
]
sources = [{"n": n, "title": t, "url": u, "publisher": p, "accessed": a} for n, t, u, p, a in S]

sections = [
    {"key": "overview", "title": "한눈에 보기", "body":
     "앤디브(Cichorium endivia L.)는 국화과(Asteraceae) 치커리속의 잎채소로, 잎이 가늘고 깊게 갈라진 곱슬잎형(프리제, var. crispum)과 잎이 넓고 덜 갈라진 넓은잎형(에스카롤, var. latifolium)으로 나뉜다[3]. 두 유형 모두 생채소 샐러드나 포장 샐러드로 먹으며, 소비가 특히 늘어난 유럽에서는 이탈리아·스페인·프랑스가 치커리속 채소의 대표 국가로 꼽힌다[3].\n\n"
     "식품의약품안전처 「식품원료 목록」에서 앤디브는 식품에 사용할 수 있는 원료(사용가능)이며, 사용 조건은 '사용가능부위 : 잎'이다[1]. 목록의 원료명은 '앤디브잎'이고, 이명 '에스케롤'과 영문명 Endive·Escarole endive·Garden endive·White chicory가 함께 적혀 있다[1]. 같은 목록 자료에서 다른 나라 목록이나 건강기능식품 고시형 원료의 원재료로 표시된 기록은 없다[1].\n\n"
     "앤디브 잎의 쓴맛은 락투신·락투코피크린 같은 세스퀴테르펜 락톤에서 오며, 곱슬잎형의 총량이 넓은잎형보다 약 2.4배 많았다[3]. 잎에는 치코르산·카페오일퀸산 같은 페놀산과 캠페롤 배당체도 많다[9, 12]. 같은 속의 치커리(Cichorium intybus)와 그 재배형인 위트루프(벨기에 엔다이브)·라디치오는 앤디브와 다른 종이므로 자료를 섞지 않아야 한다[5, 32]."},
    {"key": "history", "title": "역사", "body":
     "앤디브는 야생 상태로는 알려져 있지 않은 재배 식물로 정리되어 있다[2]. 19세기 식물학 문헌은 Cichorium pumilum을 야생 조상으로 보았고, 뒤에는 치커리와 C. pumilum의 잡종에서 왔다는 견해도 나왔다[2]. 고대 이집트인이 알았을 것으로 보지만 고고학적 증거는 없고, 일찍 인도로 퍼졌으며 16세기에 중부 유럽에 전해졌다고 소개된다[2]. 2022년 유전체 비교 연구는 치커리가 앤디브의 조상이라는 기존 가설을 받아들이지 않았다[5].\n\n"
     "약용 전통도 남아 있다[35]. 이집트 시나이 사막 베두인 전통 의학에서 쓰는 식물 61종을 조사한 연구에서 앤디브 메탄올 추출물은 사람 림프종 세포에 비교적 강한 세포독성을 보인 식물 가운데 하나였다[35]. 앤디브는 지중해 지역에서 널리 먹는 식용 식물로도 소개된다[17].\n\n"
     "이탈리아에서는 앤디브의 일부 품종·재래종이 농식품부의 「전통 농식품 목록」에 올라 있다고 한다[10]. 한국에 언제 들어왔는지와 국내 고문헌 기록은 이번 조사에서 확인하지 못함."},
    {"key": "biology", "title": "식물학적 특징", "body":
     "앤디브는 염색체 수 2n = 2x = 18의 한해살이 식물로, 지중해 위도에서는 5–8월에 꽃이 핀다[3]. 잎이 뭉쳐 로제트(포기)를 이룬 뒤 꽃대가 올라와 보라색 꽃을 피우며, 제꽃가루받이가 우세해 타가수분율은 1% 정도다[3]. 그래서 자연 집단은 동형접합성이 높은 계통들이 섞인 형태다[3].\n\n"
     "곱슬잎형은 가운데 잎맥이 좁고 잎몸이 깊게 갈라지며, 넓은잎형(에스카롤)은 연한 녹색 잎에 굵은 가운데 잎맥과 넓고 조금 갈라진 잎몸, 톱니 모양 가장자리를 가진다[3]. 유전자 SNP 분석에서도 두 유형은 뚜렷이 다른 두 계통군으로 나뉘었다[3, 7].\n\n"
     "저장 탄수화물은 치커리와 다르다[23]. 한해살이 앤디브(곱슬잎형)와 두해살이 치커리(위트루프)를 비교한 연구에서 1-케스토스·니스토스·이눌린은 치커리 뿌리에서만 나오고 앤디브 조직에서는 검출되지 않았다[23]. 반면 다른 연구는 과습 스트레스를 받은 앤디브 잎에서 수크로스·케스토스·이눌린이 줄었다고 보고해, 잎의 프럭탄 유무는 연구마다 다르다[24]. 뿌리에서는 구아이아놀라이드·저마크라놀라이드·엘레마놀라이드형 세스퀴테르펜과 그 배당체 23종(새 화합물 12종)이 분리되었다[31]. 곱슬잎형 뿌리에서도 세스퀴테르펜 락톤 13종(새 구아이아놀라이드 1종 포함)과 페놀산 에스터 3종이 보고되었다[30]."},
    {"key": "related_species", "title": "가까운 종", "body":
     "치커리속(Cichorium)의 대표 재배종은 앤디브와 치커리(C. intybus)이고, 지중해 지역에는 야생 근연종인 C. pumilum과 C. calvum이 자란다[2]. 시장에서 '엔다이브'라고 부르는 벨기에 엔다이브(위트루프, C. intybus var. foliosum)와 붉은 라디치오는 치커리의 재배형으로, 앤디브(C. endivia)와는 다른 종이다[32]. 이탈리아의 카스텔프랑코 치커리는 치커리(var. silvestre)와 에스카롤(C. endivia var. latifolium)을 교잡해 얻은 채소로 소개된다[32].\n\n"
     "국화과 작물 전사체 비교에서 치커리와 앤디브 사이에 유전자 이입(introgression)의 흔적이 확인되었다[8]. 엽록체 유전체 계통 분석에서 앤디브는 치커리속 안에서 다른 종과 잘 구분되는 별도 계통을 이루었다[6]. 세스퀴테르펜 락톤 생합성 효소(저마크렌 A 합성효소·산화효소, 코스투놀라이드 합성효소) 계통수에서는 앤디브·치커리·상추(Lactuca sativa) 단백질이 서로 가깝게 묶였다[3].\n\n"
     "치커리 뿌리의 이눌린은 앤디브에 그대로 적용할 수 없다[23]. 이 문서의 성분·안전 자료는 앤디브 잎(일부는 뿌리·종자) 연구만 모았다[3, 9, 10]."},
    {"key": "cultivation", "title": "재배와 생산", "body":
     "앤디브는 대부분 노지에서 기르며, 수확 직전 폭우로 인한 과습에 약해 품종에 따라 포기 무게가 6–35% 줄었다[24]. 이탈리아 라치오주 시험에서는 8월 말 육묘장에 파종하고 3주 된 모종을 1 m²당 8.2주로 밭에 옮겨 심어 11월 하순에 수확했다[3]. 상업 품종은 대부분 반복 자가수분으로 만든 순계이고, 육종은 이른 꽃대 올라옴(추대) 저항성, 잎끝마름·뿌리썩음·흰가루병 저항성, 영양·맛·저장성 향상을 목표로 한다[3].\n\n"
     "이탈리아의 곱슬잎형·넓은잎형 앤디브 재배 면적은 6,800 ha가 넘고 생산량은 152,800 톤이 넘으며, 캄파니아주가 27,895 톤으로 가장 많이 생산한다[10]. 이탈리아 북부에서는 Fusarium oxysporum에 의한 시들음병이 보고되어 농가마다 포기의 약 40%가 증상을 보였다[33]. 스페인 노지 재배 연구는 앤디브를 날로 또는 익혀 먹는 인기 채소로 소개하고, 브라시노스테로이드 유사체 살포가 수량과 총페놀을 높였다고 보고했다[36].\n\n"
     "국내의 앤디브 재배 면적·생산량 공식 통계와 지리적 표시 등록은 확인하지 못함."},
    {"key": "processing", "title": "가공과 이용", "body":
     "앤디브는 생채소 샐러드나 최소가공 포장 샐러드로 주로 소비된다[3]. 신선편이 제품은 잎이 갈변하기 쉬운데, 6 °C 저장 중 주요 페놀을 추적한 연구에서 가장 많은 페놀인 치코르산 함량이 저장 첫 24시간 동안 크게 변했다[14]. 국내 연구에서는 엔다이브를 2 °C에서 20일간 저장하며 포장 방법을 비교해, 종이상자 안을 HDPE 필름으로 속포장한 처리에서 중량 감소가 가장 적고 외관이 가장 좋았다[26].\n\n"
     "출하 과정에서 버려지는 겉잎도 연구 대상이다[10]. 이탈리아 캄파니아의 에스카롤 3품종 겉잎을 80% 에탄올로 초음파 추출하면 수율은 3–4%였고, 추출물에서 페놀산·플라보놀·세스퀴테르펜 락톤 등 35종이 확인되었다[10]. 끓이기·냉동·동결건조가 치커리속 채소의 수용성 항산화·산화촉진 활성에 주는 영향도 에스카롤과 곱슬잎형을 포함해 조사되었다[32].\n\n"
     "식약처 「식품 등의 생산실적」에서 앤디브를 원료로 한 건강기능식품 생산 실적은 확인하지 못함."},
    {"key": "genetics", "title": "유전체와 육종", "body":
     "앤디브 유전체는 2022년에 염색체 수준으로 조립되었고, 한 연구는 641 Mb(콘티그 N50 5.16 Mb)에 단백질 암호화 유전자 46,711개를 보고했다[4]. 같은 해 다른 연구는 0.89 Gb로 조립했고, 치커리(1.28 Gb)와의 크기 차이는 주로 LTR 레트로트랜스포존 때문이라고 했다[5]. 두 연구의 유전체 크기가 달라 둘 다 적는다[4, 5]. 앤디브·치커리·우엉 유전체는 공통의 전유전체 3배화(WGT-1)를 겪은 것으로 나타났다[5].\n\n"
     "테르펜 합성효소 유전자군이 크게 늘어나 있고, 쓴맛이 강한 품종에서 세스퀴테르펜 락톤 생합성 유전자의 발현이 높았다[4]. 엽록체 유전체(품종 'Confiance')는 152,809 bp이고 유전자 136개(단백질 암호화 90, tRNA 38, rRNA 8)를 가진다[6]. 곱슬잎형 'Domari'의 전사체는 유니진 77,022개로 조립되었고, SNP 3,177개가 곱슬잎형과 넓은잎형을 구분했다[3].\n\n"
     "RAD 시퀀싱으로 얻은 SNP 4,621개는 육종 계통 32개를 모두 구별했고, 잎 모양을 가르는 표지 24개가 상추 8번 염색체 끝부분 49.6 Mb 구간에 대응되었다[7]. 플라보노이드 배당화 효소 유전자(CeUGT)를 앤디브에서 찾아 대장균에서 발현시킨 연구도 있다[34]."},
    {"key": "safety", "title": "안전성", "body":
     "앤디브는 흔히 먹는 채소이며, 생쥐 급성 경구 독성시험에서 앤디브 추출물의 LD50은 5,000 mg/kg보다 커 사실상 독성이 없다고 평가되었다[16]. 다만 국화과 식물의 세스퀴테르펜 락톤은 접촉 알레르기의 주요 원인이며, 식용 국화과 가운데 상추와 앤디브는 국화과 알레르기 환자의 20–30%에서 감작원으로 보고되었다[20]. 샐러드용 치커리속 채소를 다루는 사람에게서 직업성 접촉피부염이 보고되었고, 치커리 즉시형 알레르기 환자가 앤디브·상추를 먹은 뒤에도 반응한 사례가 있다[21, 22].\n\n"
     "잎채소는 질산염이 많은 편이다[19]. 이탈리아 시장 조사에서 앤디브와 상추를 섞은 그린샐러드의 질산염 최고치는 4,200 mg/kg이었고, 평균 섭취량은 1일 섭취허용량(질산 이온 3.7 mg/kg 체중) 아래였다[19]. 이탈리아 두 지역에서 기른 앤디브의 질산염 함량은 위험 기준보다 반복적으로 낮았다[18].\n\n"
     "날로 먹는 포장 샐러드는 미생물 관리가 중요하다[27]. 아일랜드 슈퍼마켓 조사에서 곱슬잎형·에스카롤·라디치오가 섞인 샐러드 잎 등 신선편이 제품에서 리스테리아 모노사이토제네스가 분리되었다[27]. 슬로베니아의 2009년 조사에서 앤디브를 포함한 농산물 170점은 농약 최대잔류허용기준을 넘지 않았다[28]. 국내 공공기관의 앤디브 알레르기·잔류농약 관련 안전 정보는 확인하지 못함."},
]


def C(name, ko, cls, role, part, content, act, src):
    return {"name": name, "name_ko": ko, "class": cls, "role": role, "part": part,
            "content_text": content, "activity_ko": act, "source": src}


compounds = [
    C("Chicoric acid", "치코르산(디카페오일타르타르산)", "페놀산(하이드록시신남산 유도체)", "marker", "잎(에스카롤)",
      "잎 페놀 화합물 가운데 가장 많음(페놀산이 총 페놀의 약 70%); 개별 수치는 표에 있어 확인하지 못함[9]",
      "신선편이 저장 중 가장 많은 페놀로, 저장 첫 24시간 동안 함량이 크게 변함[14]", [9, 14]),
    C("Chlorogenic acid", "클로로겐산(5-O-카페오일퀸산)", "페놀산(카페오일퀸산)", "bioactive", "잎(곱슬잎형·넓은잎형); 종자",
      "두 변종 모두에서 확인(정성)[11]",
      "종자 추출물에서 OH 라디칼 소거능이 시나린보다 강함(시험관)[29]", [11, 29]),
    C("Caftaric acid", "카프타르산(카페오일타르타르산)", "페놀산(하이드록시신남산 유도체)", "bioactive", "잎(에스카롤)",
      "잎에서 정량(카페산 당량), 수치 확인하지 못함[9]; cis-카프타르산은 var. latifolium에서 특징적으로 확인[11]",
      "에스카롤 잎의 주요 페놀산 가운데 하나[9]", [9, 11]),
    C("3,5-Dicaffeoylquinic acid", "3,5-디카페오일퀸산", "페놀산(카페오일퀸산)", "bioactive", "잎(곱슬잎형)",
      "var. crispum에서 특징적으로 확인(정성)[11]",
      "곱슬잎형과 넓은잎형을 구분하는 페놀 성분으로 보고됨[11]", [11]),
    C("Cynarin", "시나린(1,3-디카페오일퀸산)", "페놀산(카페오일퀸산)", "bioactive", "종자",
      "종자 추출물에서 확인(함량 수치 없음)[29]",
      "종자 추출물에서 DPPH·ABTS 라디칼 소거능이 클로로겐산보다 강함(시험관)[29]", [29]),
    C("Kaempferol 3-O-glucuronide", "캠페롤 3-O-글루쿠로나이드", "플라보놀 배당체", "marker", "잎(에스카롤)",
      "잎에서 가장 많은 플라보놀(플라보놀이 총 페놀의 약 30%); 개별 수치는 표에 있어 확인하지 못함[9]",
      "캠페롤 유도체가 겉잎 추출물에서 가장 많은 폴리페놀로 정량됨[10]", [9, 10]),
    C("Kaempferol 3-O-(6''-O-malonyl)glucoside", "캠페롤 3-O-(6″-O-말로닐)글루코사이드", "플라보놀 배당체", "bioactive", "잎",
      "에스카롤 잎에서 두 번째로 많은 플라보놀[9]",
      "곱슬잎형·에스카롤 유전자원에서 쓴맛·떫은맛·풀냄새 지각과 일관되게 관련[13]", [9, 13]),
    C("Astragalin", "아스트라갈린(캠페롤 3-O-글루코사이드)", "플라보놀 배당체", "bioactive", "전초 추출물",
      "추출물에서 분리(함량 수치 없음)[16]",
      "ORAC 항산화 활성; 추출물은 간세포·생쥐 산화 손상을 줄임[16]", [16]),
    C("Lactucin", "락투신", "세스퀴테르펜 락톤(구아이아놀라이드)", "marker", "잎",
      "락투신류 합계(LcTOT) 곱슬잎형 1453.5 ± 548.5, 넓은잎형 584.1 ± 73.8 mg/kg 건물[3]",
      "쓴맛 성분; 곱슬잎형이 넓은잎형보다 3.7배 많아 두 유형을 가르는 지표[3]", [3, 10]),
    C("Lactucopicrin", "락투코피크린", "세스퀴테르펜 락톤(구아이아놀라이드)", "marker", "잎",
      "락투코피크린류 합계(LpTOT) 곱슬잎형 786.4 ± 186.8, 넓은잎형 346.7 ± 113.1 mg/kg 건물[3]",
      "앤디브 쓴맛 지각에 지배적 영향[3, 13]; 대식세포 거품세포 형성 억제(세포·생쥐)[15]", [3, 13, 15]),
    C("8-Deoxylactucin", "8-데옥시락투신", "세스퀴테르펜 락톤(구아이아놀라이드)", "bioactive", "잎",
      "잎에서 정량했으나 개별 수치는 표에 있어 확인하지 못함[3]",
      "곱슬잎형('Domari'·'Myrna')에서 넓은잎형보다 많음[3]", [3]),
    C("11beta,13-Dihydrolactucin", "11β,13-디하이드로락투신", "세스퀴테르펜 락톤(구아이아놀라이드)", "bioactive", "겉잎 추출물; 잎",
      "'Leonida' 겉잎 추출물에서 가장 많은 세스퀴테르펜 락톤(락투신 당량), 수치는 표에 있어 확인하지 못함[10]",
      "세스퀴테르펜이 많은 'Leonida' 추출물이 대식세포 IL-6 분비를 약 40% 줄임(시험관)[10]", [3, 10]),
    C("beta-Sitosterol", "β-시토스테롤", "식물스테롤", "nutrient", "잎",
      "총 스테롤 106.3–176.0 mg/kg 생체중 중 45–56%[18]",
      "앤디브 잎 스테롤의 주성분[18]", [18]),
    C("Stigmasterol", "스티그마스테롤", "식물스테롤", "nutrient", "잎; 전초 추출물",
      "총 스테롤 중 38–43%[18]",
      "에탄올 추출물에서 분리된 성분 가운데 하나[17]", [17, 18]),
    C("Phylloquinone", "필로퀴논(비타민 K1)", "지용성 비타민", "nutrient", "잎(생)",
      "231 µg/100 g(USDA 값, WebSearch 요약으로만 확인)[25]",
      "혈액 응고에 필요한 비타민; 함량 수치만 확인[25]", [25]),
]

ASSAY_KEYS = ["instrument", "column", "mobile_phase", "gradient", "flow", "temp", "detection", "injection",
              "sample_prep", "standard", "linearity", "lod", "loq", "recovery"]


def cond(**kw):
    return {k: kw.get(k, "") for k in ASSAY_KEYS}


assays = [
    {"role": "literature", "compound": "Lactucopicrin", "compound_ko": "락투코피크린(세스퀴테르펜 락톤 6종 동시: 락투신·8-데옥시락투신·락투코피크린과 각 11,13-디하이드로체)",
     "part": "잎(겉잎을 뗀 로제트 잎) 동결건조물",
     "content": "총 세스퀴테르펜 락톤 곱슬잎형 2239 ± 531, 넓은잎형 930.8 ± 181.7 mg/kg 건물; LpTOT 786.4 ± 186.8 vs 346.7 ± 113.1, LcTOT 1453.5 ± 548.5 vs 584.1 ± 73.8 mg/kg 건물[3]",
     "method": "HPLC-DAD",
     "conditions": cond(
         instrument="Thermo-Finnigan HPLC(4원 펌프, DAD 검출기)",
         column="C18 Kinetex, 250 × 4.60 mm, 5 µm",
         mobile_phase="A: 메탄올/물 14:86 (v/v), B: 메탄올/물 64:36 (v/v)",
         gradient="0–20분 A 100→58%; 20–30분 58% A; 30–45분 58→0% A; 45–50분 0% A; 50–52분 0→100% A; 52–62분 100% A",
         flow="0.5 mL/min",
         detection="UV 260 nm",
         injection="80 µL",
         sample_prep="동결건조 잎 2 g + 메탄올/물(80:20, v/v)·2% 포름산 50 mL + 내부표준 산토닌 용액 3 mL, 80 °C에서 15분 진탕(1000 g/min) 초음파 보조 추출 3회(총 150 mL) → 감압 건고 → 메탄올/디클로로메탄(1:7) 재용해 → 고상추출(SPE) 칼럼, 디클로로메탄/에틸아세테이트(3:2) 6 mL 용출 → 50 kHz 초음파 30분(37 °C) → 메탄올 4 mL 첨가",
         standard="내부표준 산토닌 101.7 µg/mL(3 mL 첨가)"),
     "rationale": "락투신·락투코피크린류는 앤디브 잎의 대표 세스퀴테르펜 락톤으로 쓴맛을 결정하고 곱슬잎형과 넓은잎형을 가르는 지표다[3]. 칼럼 온도·검출한계·정량한계·회수율은 본문에 없어 비워 둠.",
     "source": [3], "url": pmc("PMC6312536"), "source_kind": "paper"},
    {"role": "literature", "compound": "Chicoric acid", "compound_ko": "치코르산(페놀산 10종·플라보놀 5종 동시)",
     "part": "잎(에스카롤, 파종 후 60일) 동결건조물",
     "content": "페놀 15종(페놀산 10, 플라보놀 5) 정량; 페놀산이 총 페놀의 약 70%로 치코르산이 가장 많고, 플라보놀은 약 30%로 캠페롤 3-O-글루쿠로나이드가 가장 많음; 개별 수치(g/kg 건물)는 표에 있어 확인하지 못함[9]",
     "method": "HPLC-DAD-ESI-MS/MS",
     "conditions": cond(
         instrument="Hewlett-Packard 1200 시리즈 액체크로마토그래프(Agilent) + API 3200 Qtrap(ESI, 삼중사중극자-이온트랩)",
         column="Spherisorb S3 ODS-2 C18 역상, 150 × 4.6 mm, 3 µm (Waters)",
         mobile_phase="A: 포름산 수용액(원문 농도 표기 '0.1 mL L', 단위 위첨자 확인 못함), B: 아세토니트릴",
         gradient="",
         temp="35 °C",
         detection="DAD 280·330·370 nm(전 스펙트럼 220–600 nm); 정량 280 nm(프로토카테쿠산 유도체)·330 nm(카페산 유도체·치코르산)·360 nm(플라본·플라보놀); MS 음이온 모드 m/z 100–1700, 전주사·MS/MS",
         sample_prep="동결건조 시료 5 mg을 메탄올:물(80:20)로 초음파 추출 3회, 상등액 합쳐 헥산 액액분배로 정제, 감압 농축해 최종 2 mL",
         standard="외부표준법: 프로토카테쿠산 유도체는 갈산 당량, 카페산 유도체는 카페산 당량, 캠페롤·퀘르세틴 유도체는 캠페롤 3-O-글루쿠로나이드·퀘르세틴 3-O-글루코사이드 당량"),
     "rationale": "치코르산은 에스카롤 잎에서 가장 많은 페놀 화합물이라 페놀 조성의 지표로 쓰였다[9]. 기울기·유속·주입량은 선행 문헌을 인용해 본문에 없고, 검출·정량한계·회수율도 없어 비워 둠.",
     "source": [9], "url": pmc("PMC7919373"), "source_kind": "paper"},
    {"role": "literature", "compound": "11beta,13-Dihydrolactucin", "compound_ko": "세스퀴테르펜 락톤(디하이드로락투신 등, 락투신 당량)",
     "part": "겉잎(버려지는 잎) 80% 에탄올 초음파 추출물, 동결건조",
     "content": "'Leonida'가 세스퀴테르펜이 가장 많고 'Capriccio'가 가장 적음; 디하이드로락투신과 그 이성질체가 'Leonida'에서 가장 많음; 수치는 표에 있어 확인하지 못함[10]",
     "method": "UHPLC-HRMS (Q-Orbitrap)",
     "conditions": cond(
         instrument="Thermo UltiMate 3000 UHPLC + Q Exactive 하이브리드 사중극자-오비트랩 질량분석기",
         column="Luna C 계열 역상 칼럼(첨자 표기 손실), 150 × 2 mm, 3 µm, 100 Å (Phenomenex)",
         mobile_phase="A: 0.1% (v/v) 포름산 수용액, B: 아세토니트릴",
         gradient="B 5% → 50%(25분, 직선)",
         detection="고분해능 질량분석(정성 분석은 양·음이온 모드); 락투신 [M+H]+ m/z 277.1070, 락투코피크린 m/z 411.1448",
         sample_prep="냉동 겉잎 100 g + 에탄올/물(80:20, v/v) 600 mL, 침지형 초음파기 40 kHz로 50분 추출 → 여과·30 °C 감압 농축 → 동결건조(수율 3–4%)",
         standard="락투신 표준품 당량으로 정량(락투신은 표준품과 동시 용출로 확인)",
         linearity="화합물마다 기기 응답의 직선성을 확인했다고만 기재(수치 없음)"),
     "rationale": "세스퀴테르펜 락톤은 앤디브 속(屬) 특유 성분으로, 세포 항산화·항염 효과가 큰 품종과 함량이 일치했다[10]. 유속·칼럼 온도·주입량·검출한계·정량한계·회수율은 본문에 없어 비워 둠.",
     "source": [10], "url": pmc("PMC10376668"), "source_kind": "paper"},
    {"role": "literature", "compound": "Kaempferol 3-O-(6''-O-malonyl)glucoside", "compound_ko": "캠페롤 유도체(말로닐헥소사이드·헥소사이드·우로나이드, 캠페롤 당량)",
     "part": "겉잎(버려지는 잎) 80% 에탄올 초음파 추출물, 동결건조",
     "content": "'Performance'가 캠페롤 유도체가 가장 많고, 말로닐헥소사이드·헥소사이드·우로나이드 결합체가 가장 많음; 수치는 표에 있어 확인하지 못함[10]",
     "method": "UPLC-MS/MS (MRM)",
     "conditions": cond(
         instrument="Shimadzu Nexera X2 UPLC + ABSCIEX API 6500 QTRAP 질량분석기(양·음이온 모드)",
         column="Luna Omega C 계열 역상 칼럼(첨자 표기 손실), 100 × 2 mm, 1.7 µm, 100 Å (Phenomenex)",
         mobile_phase="A: 0.1% (v/v) 포름산 수용액, B: 아세토니트릴",
         gradient="B 5% → 50%(15분)",
         detection="MRM 모드(화합물별 최적화 조건)",
         sample_prep="냉동 겉잎 100 g + 에탄올/물(80:20, v/v) 600 mL, 침지형 초음파기 40 kHz로 50분 추출 → 여과·30 °C 감압 농축 → 동결건조",
         standard="각 아글리콘(캠페롤) 당량으로 정량",
         linearity="화합물마다 기기 응답의 직선성을 확인했다고만 기재(수치 없음)"),
     "rationale": "캠페롤 유도체는 세 품종 추출물 모두에서 가장 많은 폴리페놀이었고, 함량이 높은 품종이 라디칼 소거능도 약 3배 높았다[10]. 유속·온도·주입량·검출한계·정량한계·회수율은 본문에 없어 비워 둠.",
     "source": [10], "url": pmc("PMC10376668"), "source_kind": "paper"},
]

nutrients = [{"form": "앤디브 잎·생(USDA SR Legacy 'Endive, raw', FDC ID 168412; WebSearch 요약으로만 확인)",
              "basis": "가식부 100 g",
              "items": [{"name": "칼륨", "value": 314, "unit": "mg"},
                        {"name": "엽산", "value": 142, "unit": "μg"},
                        {"name": "비타민 K", "value": 231, "unit": "μg"}],
              "source": [25]}]

world = [
    {"country": "이탈리아", "metric": "area_ha", "year": None, "value": 6800, "unit": "ha",
     "note": "곱슬잎형·넓은잎형 합계 '6,800 ha 이상', 기준 연도는 원문에 없음", "source": [10]},
    {"country": "이탈리아", "metric": "production_t", "year": None, "value": 152800, "unit": "톤",
     "note": "총생산 '152,800 톤 이상'(약 100,000 톤이 남부), 기준 연도는 원문에 없음", "source": [10]},
    {"country": "이탈리아(캄파니아주)", "metric": "production_t", "year": None, "value": 27895, "unit": "톤",
     "note": "이탈리아 1위 생산 주, 기준 연도는 원문에 없음", "source": [10]},
]

d = {
    "slug": "cichorium-endivia",
    "name_ko": "앤디브",
    "name_en": "Endive (escarole, curly endive)",
    "scientific_name": "Cichorium endivia L.",
    "aliases": ["앤디브잎", "에스케롤", "엔다이브", "에스카롤", "프리제", "Endive", "Escarole", "Curly endive", "Frisée", "Garden endive"],
    "sections": sections,
    "compounds": compounds,
    "markers": [],
    "assays": assays,
    "nutrients": nutrients,
    "production": [],
    "world": world,
    "gi": [],
    "orgs": [],
    "sources": sources,
}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in sections:
    print(s["key"], len(s["body"]))
