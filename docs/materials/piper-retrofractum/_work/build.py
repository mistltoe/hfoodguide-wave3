import json, pathlib
OUT = pathlib.Path(__file__).resolve().parent.parent / "dossier.json"
A = "2026-11-02"
def doi(d): return "https://doi.org/" + d
S = [
 ("식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 자바후추열매(Piper retrofractum; Javanese long pepper, Balinese long pepper), 부위: 열매, 제한적사용, 사용 조건 '제한적사용가능부위 : 열매'", "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "식품의약품안전처", "2026-10-13"),
 ("식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 같은 후추속 원료 행: 후추(Piper nigrum L. / Piper album L., 열매, 사용가능), 필발(Piper longum L., 열매, 제한적사용), 큐벱페퍼열매(Piper cubeba L., 열매, 사용가능), 카바카바(Piper methysticum, 사용불가), 바람등칡(Piper kadzura, 사용불가)", "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "식품의약품안전처", "2026-10-13"),
 ("식품의 기준 및 규격(식품공전) 제2. 1. 2) 식품원료 판단기준 — '식품에 제한적으로 사용할 수 있는 원료'([별표 2]) 사용 조건 준수·가공 전 원료 중량 50% 미만 사용 규정 (WebSearch 검색 요약으로만 확인, 원문 페이지는 네트워크 제한으로 열람하지 못함)", "https://www.foodsafetykorea.go.kr/popup/safefoodlife/food/foodRvlv/foodRvlvDetail.do?rvlv_no=9", "식품의약품안전처(식품안전나라)", A),
 ("Kim KJ et al. Piperidine alkaloids from Piper retrofractum Vahl. protect against high-fat diet-induced obesity by regulating lipid metabolism and activating AMP-activated protein kinase. Biochem Biophys Res Commun 2011;411(1):219-25 (PMID 21741367)", doi("10.1016/j.bbrc.2011.06.153"), "Elsevier / PubMed", A),
 ("Takahashi M et al. Flavor characteristics and antioxidant capacities of hihatsumodoki (Piper retrofractum Vahl) fresh fruit at three edible maturity stages. J Food Sci Technol 2018;55(4):1295-1305 (PMID 29606743, PMC5876197; 초록 확인)", doi("10.1007/s13197-018-3040-2"), "Springer / PubMed", A),
 ("Nutmakul T et al. Synergistic effect of Trikatuk, a traditional Thai formulation, on antioxidant and alpha-glucosidase inhibitory activities. Heliyon 2023;9(1):e13063 (PMID 36711300, PMC9873688; 전문 확인)", doi("10.1016/j.heliyon.2023.e13063"), "Elsevier / PubMed Central", A),
 ("Effects of Cabya (Piper retrofractum Vahl.) Fruit Developmental Stage on VOCs. Foods 2022;11(16):2528 (PMID 36010528, PMC9407187; 전문 확인)", doi("10.3390/foods11162528"), "MDPI / PubMed Central", A),
 ("Effects of processing methods on the aroma constituents of hihatsumodoki (Piper retrofractum Vahl). J Food Sci 2023;88(6):2463-2477 (PMID 37183927; 초록 확인)", doi("10.1111/1750-3841.16606"), "Wiley / PubMed", A),
 ("Effect of pipernonaline from Piper retrofractum on memory disorder in mice and neurite outgrowth activity of PC12 cells. Med Chem Res 2026 (PMID 42782504; 초록 확인)", doi("10.1007/s00044-026-03617-3"), "Springer / PubMed", A),
 ("Discovery of thiol-reactive Staphylococcus aureus sortase A inhibitors from natural products by machine learning and thiocholine mass-shift profiling. Anal Chim Acta 2026 (PMID 42887972; 초록 확인)", doi("10.1016/j.aca.2026.346228"), "Elsevier / PubMed", A),
 ("Four new alkylamides from the fruits of Piper retrofractum and antityrosinase evaluation. Nat Prod Res 2023 (PMID 37715311; 초록 확인)", doi("10.1080/14786419.2023.2258542"), "Taylor & Francis / PubMed", A),
 ("Banerji A et al. Amides from Piper brachystachyum and Piper retrofractum. Phytochemistry 2002;59(8):897-901 (PMID 11937173)", doi("10.1016/s0031-9422(01)00364-8"), "Elsevier / PubMed", A),
 ("Luca SV et al. LC-HRMS/MS-based phytochemical profiling of Piper spices: Global association of piperamides with endocannabinoid system modulation. Food Res Int 2021;141:110123 (PMID 33641990; 초록 확인)", doi("10.1016/j.foodres.2021.110123"), "Elsevier / PubMed", A),
 ("Kubo M et al. Evaluation of constituents of Piper retrofractum fruits on neurotrophic activity. J Nat Prod 2013;76(4):769-73 (PMID 23506561)", doi("10.1021/np300911b"), "ACS / PubMed", A),
 ("New Amides and Phenylpropanoid Glucosides from the Fruits of Piper retrofractum. Nat Prod Bioprospect 2019;9(3):231-241 (PMID 31073809, PMC6538700)", doi("10.1007/s13659-019-0208-z"), "Springer / PubMed", A),
 ("Hieu LD et al. Chemical composition of essential oils from four Vietnamese species of Piper (Piperaceae). J Oleo Sci 2014;63(3):211-7 (PMID 24712088)", doi("10.5650/jos.ess13175"), "Japan Oil Chemists' Society / PubMed", A),
 ("Luyen BT et al. A new phenylpropanoid and an alkylglycoside from Piper retrofractum leaves with their antioxidant and α-glucosidase inhibitory activity. Bioorg Med Chem Lett 2014;24(17):4120-4 (PMID 25127165)", doi("10.1016/j.bmcl.2014.07.057"), "Elsevier / PubMed", A),
 ("Pinya T et al. Conventional and molecular pharmacognostic characters integrated with chemical profiles of five Piper plants in the Thai herbal pharmacopoeia and their admixture/adulteration/substitution situations in Thailand. J Nat Med 2022;76(3):605-620 (PMID 35201516)", doi("10.1007/s11418-022-01607-4"), "Springer / PubMed", A),
 ("Neamsuvan O et al. Medicinal plants used for hypertension treatment by folk healers in Songkhla province, Thailand. J Ethnopharmacol 2018;214:58-70 (PMID 29229570)", doi("10.1016/j.jep.2017.11.032"), "Elsevier / PubMed", A),
 ("Maenthaisong R et al. Efficacy and safety of topical Trikatu preparation in relieving mosquito bite reactions: a randomized controlled trial. Complement Ther Med 2014;22(1):34-9 (PMID 24559814)", doi("10.1016/j.ctim.2013.08.014"), "Elsevier / PubMed", A),
 ("Thai herbal formulation 'Ya-Pit-Samut-Noi': Its antibacterial activities, effects on bacterial virulence factors and in vivo acute toxicity. J Ethnopharmacol 2020;259:112975 (PMID 32417424)", doi("10.1016/j.jep.2020.112975"), "Elsevier / PubMed", A),
 ("Plengsuriyakarn T et al. Anticancer activities against cholangiocarcinoma, toxicity and pharmacological activities of Thai medicinal plants in animal models. BMC Complement Altern Med 2012;12:23 (PMID 22448640, PMC3353211; 전문 확인)", doi("10.1186/1472-6882-12-23"), "BioMed Central / PubMed Central", A),
 ("Molecular biology of vascular bioenergetics rewiring: Mitochondrial protective mechanisms of Piper retrofractum in hypertension and oxidative injury (review). Mol Biol Rep 2026;53(1) (PMID 42507233, PMC13407938; 전문 확인)", doi("10.1007/s11033-026-12366-w"), "Springer / PubMed Central", A),
 ("Yun J et al. Piper retrofractum Vahl. extract, as a PPARδ and AMPK activator, suppresses UVB-induced photoaging through mitochondrial biogenesis and MMPs inhibition in human dermal fibroblasts and hairless mice. Evid Based Complement Alternat Med 2018;2018:6172954 (PMID 29619069)", doi("10.1155/2018/6172954"), "Hindawi / PubMed", A),
 ("Antithrombic effects of Piper retrofractum in a rat model of acute thrombosis: modulation of endothelial adhesion molecules and inflammatory factors. Food Sci Biotechnol 2025;34(1):269-276 (PMID 39758728)", doi("10.1007/s10068-024-01625-w"), "Springer / PubMed", A),
 ("Application of film-forming solution as a transdermal delivery system of piperine-rich herbal mixture extract for anti-inflammation. Heliyon 2020;6(6):e04139 (PMID 32551384)", doi("10.1016/j.heliyon.2020.e04139"), "Elsevier / PubMed", A),
 ("Limyati DA, Juniar BL. Jamu Gendong, a kind of traditional medicine in Indonesia: the microbial contamination of its raw materials and endproduct. J Ethnopharmacol 1998;63(3):201-8 (PMID 10030724)", doi("10.1016/s0378-8741(98)00082-8"), "Elsevier / PubMed", A),
 ("Synergizing machine learning and chemometrics with voltammetric fingerprinting for the rapid detection of Java long pepper adulteration. RSC Adv 2026 (PMID 42495558)", doi("10.1039/d6ra04181g"), "Royal Society of Chemistry / PubMed", A),
 ("Chansang U et al. Mosquito larvicidal activity of aqueous extracts of long pepper (Piper retrofractum Vahl) from Thailand. J Vector Ecol 2005;30(2):195-200 (PMID 16599152)", "https://pubmed.ncbi.nlm.nih.gov/16599152/", "Society for Vector Ecology / PubMed", A),
 ("Piper retrofractum extract and its component piperine promote lymphangiogenesis via an AKT- and ERK-dependent mechanism. J Food Biochem 2022;46(9):e14233 (PMID 35567300)", doi("10.1111/jfbc.14233"), "Wiley / PubMed", A),
 ("The possibility of using isolated alkaloid compounds and crude extracts of Piper retrofractum (Piperaceae) as larvicidal control agents for Culex quinquefasciatus larvae. J Med Entomol 2018;55(5):1231-1236 (PMID 29796657)", doi("10.1093/jme/tjy082"), "Oxford University Press / PubMed", A),
 ("Duangjai A et al. Potential mechanisms of hypocholesterolaemic effect of Thai spices/dietary extracts. Nat Prod Res 2011;25(4):341-52 (PMID 20623425)", doi("10.1080/14786411003754249"), "Taylor & Francis / PubMed", A),
 ("Green Tea Extract Containing Piper retrofractum Fruit Ameliorates DSS-Induced Colitis via Modulating MicroRNA-21 Expression and NF-κB Activity. Nutrients 2022;14(13):2684 (PMID 35807865)", doi("10.3390/nu14132684"), "MDPI / PubMed", A),
]
sources = [{"n": i+1, "title": t, "url": u, "publisher": p, "accessed": a} for i,(t,u,p,a) in enumerate(S)]

sections = [
{"key":"overview","title":"한눈에 보기","body":
"자바후추(Piper retrofractum)는 식약처 「식품원료 목록」에 원료명 '자바후추열매', 영어 이름 Javanese long pepper·Balinese long pepper로 올라 있는 후추속 식물이다[1]. 이 목록에서 자바후추는 '제한적사용' 원료이며, 사용 조건은 '제한적사용가능부위 : 열매'로 열매만 식품에 쓸 수 있다[1]. 식품공전은 제한적 사용 원료에 대해 명시된 사용 조건을 지키고 식품 제조 시 가공 전 원료 중량 기준 50% 미만(배합수 제외)으로 쓰도록 정한 것으로 WebSearch 요약에서 확인했으나, 원문은 열람하지 못했다[3]. 이 종을 원재료로 하는 건강기능식품 고시형 원료는 확인하지 못함.\n\n"
"자바후추는 동남아시아 원산의 덩굴성 목본으로, 주로 인도네시아와 태국에서 재배된다[7]. 열매는 태국 음식의 향신료로 쓰이고[32], 일본 오키나와에서는 '히하츠모도키'라는 전통 향신료로 쓴다[8]. 열매에는 매운맛 성분 피페린과 피페르노날린·데하이드로피페르노날린 같은 피페리딘 알칼로이드가 들어 있다[4]. 열매 추출물은 동물·세포 시험에서 광노화 억제[24], 항혈전[25], 림프관 생성 촉진[30], 장염 완화[33] 등이 연구되었지만, 사람에게서 확인된 효능은 확인하지 못함."},
{"key":"history","title":"역사와 전통 이용","body":
"인도네시아 민간에서는 자바후추 열매를 소화기 질환 등에 쓰는 강장제로 썼고, 위통·류머티즘 관절염·설사에도 써 왔다고 보고된다[7]. 전통 의학에서 열매는 가스를 빼고(구풍), 가래를 삭이고, 기침을 멎게 하며, 식욕을 돋우는 용도로 쓰였다[4]. 태국에서는 후추 열매·자바후추 열매·생강 뿌리줄기를 같은 양 섞은 처방 '뜨리까뚝(Trikatuk)'이 오래 쓰였는데, 이는 인도 아유르베다 처방 '트리카투'의 인도 긴후추를 자바후추로 바꾼 것으로 설명된다[6]. 태국 송클라주 민간 치료사 조사에서 자바후추는 고혈압 치료에 쓰는 62종 가운데 인용 빈도가 가장 높은 식물 가운데 하나였다(FC=6, n=14)[19]. 설사에 쓰는 태국 처방 '야-삣-사뭇-너이'에도 자바후추 열매가 들어간다[21]. 인도네시아의 전통 생약 음료 '자무 겐동'의 원재료로도 쓰인다[27]. 태국에서는 열매 물 추출물이 모기 유충 방제 소재로 연구되기도 했다[29, 31]."},
{"key":"biology","title":"생물학적 특징","body":
"자바후추는 후추과(Piperaceae)의 여러해살이 덩굴식물로, 검은후추와 비슷하지만 더 길쭉한 곤봉 모양의 열매 이삭을 맺는다고 정리되어 있다[23]. 원산지는 인도네시아·말레이시아 등 동남아시아의 열대 저지대이다[23]. 오키나와산 생과는 녹색·주황·적색 세 단계로 익으며, 익을수록 유기산·유리아미노산·피페린이 줄고 당과 단맛·감칠맛을 내는 아미노산이 늘었다[5]. 같은 연구에서 DPPH 라디칼 소거 활성과 총페놀 함량도 녹색에서 적색으로 갈수록 줄어 피페린 변화와 일치했다[5]. 열매 정유의 휘발성분은 발달 단계(A–D)에 따라 달라져, 마지막 D기에는 알켄류가 57.14%를 차지했다[7]. 잎에서는 새 페닐프로파노이드 피페로사이드 등 12종이 분리되었고[17], 베트남산 잎 정유의 주성분은 벤질 벤조에이트(14.4%)와 미르센(14.4%)이었다[16]. 다만 잎은 국내 식품원료 목록의 사용 부위가 아니다[1]. 열매에서는 새 화합물 3종을 포함한 25종이 분리되었고, 그 가운데 화합물 1은 0.1–10 µM에서 NGF로 유도한 PC12 세포의 신경돌기 신장을 늘렸다[14]."},
{"key":"related_species","title":"근연종과 구별","body":
"식약처 「식품원료 목록」에는 같은 후추속 원료로 후추(Piper nigrum, 열매 사용가능), 필발(Piper longum, 열매 제한적사용), 큐벱페퍼(Piper cubeba, 열매 사용가능)가 각각 따로 올라 있다[2]. 같은 속의 카바카바(Piper methysticum)와 바람등칡(Piper kadzura)은 '사용불가' 원료다[2]. 이 자료의 성분·함량 값은 모두 Piper retrofractum으로 표기된 시료에서 옮겼고, 후추·필발·큐벱페퍼 자료는 섞지 않았다[4–8]. 태국 약전에 실린 후추속 5종을 비교한 연구에서 자바후추 시판 생약은 종 고유의 형질을 보였고 혼입·위조·대체가 없었다[18]. 태국 뜨리까뚝 연구에서 자바후추 열매 에탄올 추출물의 피페린 함량은 같은 방법으로 잰 후추 열매 추출물보다 낮았다[6]. 후추속 향신료의 피페라마이드를 비교한 연구는 후추와 필발은 서로 비슷하지만 자바후추는 이들과 다른 대사체 양상을 보일 수 있다고 보고했다[13]. 일부 문헌은 Piper chaba Hunter라는 이름을 쓰는데, 이 이름이 자바후추와 같은 종인지는 공식 분류 데이터베이스에서 확인하지 못함."},
{"key":"cultivation","title":"재배와 산지","body":
"자바후추는 동남아시아 원산으로 주로 인도네시아와 태국에서 재배된다[7]. 중국에서는 중국열대농업과학원 향료·음료연구소의 유전자원 포장에서 기른 열매로 발달 단계별 정유 조성을 분석한 연구가 있다[7]. 이 연구는 발달 단계에 따라 정유 조성이 달라지므로 용도에 맞는 수확 시기를 고르는 근거가 된다고 결론지었다[7]. 일본에서는 오키나와의 아열대 향신료로 쓰이며[8], 오키나와현 농업연구센터가 참여한 연구에서 녹색·주황·적색 세 단계 생과의 맛 성분을 비교했다[5]. 태국에서는 지역 전통 약재상에서 말린 열매를 구할 수 있다[6]. 인도네시아에서는 자무 겐동 생산자들이 원재료로 열매를 쓴다[27]. 국내 재배·생산 통계와 지리적 표시 등록은 확인하지 못함. 세계 생산량 통계(FAOSTAT 등)도 확인하지 못함."},
{"key":"processing","title":"가공과 이용","body":
"오키나와산 열매를 햇볕 건조·오븐 건조·볶음·찜으로 가공해 분석한 연구에서 106개 피크 가운데 58개가 알려진 향 성분으로 확인되었고, 리날로올·β-카리오필렌·α-카리오필렌·저마크렌 D 같은 테르펜이 57.6–88.1%를 차지했다[8]. 햇볕 건조는 헥산알 같은 알데하이드를 줄였지만 전체 향 성분량에는 큰 영향이 없었다[8]. 오븐 건조와 볶음은 90 °C까지는 향 성분을 늘렸으나 180 °C에서는 줄였고, 고온 볶음에서는 퓨란·퓨라논 같은 마이야르 반응 산물이 생겼다[8]. 찐 열매는 향 성분이 가장 적었지만 찐 뒤 말리면 약 3.6배로 늘었다[8]. 중국 연구에서는 열매를 70 °C에서 30초 데친 뒤 40 °C에서 16시간 말려 수증기 증류로 정유를 얻었다[7]. 태국 시판 열매를 95% 에탄올에 72시간 담가 얻은 추출물 수율은 9.034%였다[6]. 녹차 추출물에 자바후추 열매를 더한 소재가 생쥐 장염 모델에서 연구되었다[33]. 가루 제품의 혼입을 가려내려고 전압전류 지문과 기계학습을 결합한 판별법도 개발되었다[28]."},
{"key":"genetics","title":"유전과 분류","body":
"태국 약전에 실린 후추속 5종(구장·후추·자바후추·사르멘토숨·왈리키)을 대상으로 8개 후보 DNA 마커를 비교한 연구에서 ITS2가 생약 기원을 가리는 마커로 선택되었다[18]. 이 연구에서 자바후추는 형태·현미경·유전 형질이 종 고유의 특징을 보여 시판품의 혼입·위조·대체가 확인되지 않았다[18]. 후추속 향신료 여러 종의 피페라마이드를 LC-HRMS/MS로 분석한 연구에서는 42종의 피페라마이드가 6개 구조 계열로 묶였고, 다변량 분석에서 자바후추는 후추·필발과 다른 양상을 보일 수 있었다[13]. 열매 휘발성분을 주성분 분석·계층적 군집 분석하면 발달 단계별 시료를 구분할 수 있었다[7]. 한 리뷰는 자바후추를 인도 긴후추(필발)와 가까운 종으로 정리했다[23]. 엽록체 유전체·염색체 수 같은 이 종의 유전체 정보는 PubMed에서 확인하지 못함."},
{"key":"safety","title":"안전성","body":
"식약처 「식품원료 목록」에서 자바후추는 열매만 쓸 수 있는 '제한적사용' 원료다[1]. 제한적 사용 원료는 명시된 사용 조건을 지키고 가공 전 원료 중량 기준 50% 미만(배합수 제외)으로 써야 한다는 식품공전 규정은 WebSearch 요약으로만 확인했다[3]. 자바후추에 대한 국내 공공기관의 알레르기·잔류물질·독성 정보는 확인하지 못함.\n\n"
"자바후추 피페리딘 알칼로이드를 고지방식 생쥐에 하루 50–300 mg/kg씩 8주간 먹인 시험에서는 먹이 섭취량 변화 없이 체중 증가가 줄었다[4]. 자바후추 열매가 든 태국 처방 추출물을 쥐에 2000 mg/kg 한 번 먹인 급성 독성 시험에서는 혈액·생화학 지표, 사망, 행동, 체중, 장기 무게에 이상이 없었다[21]. 자바후추 열매가 들어간 21종 생약 처방(사하스타라)은 먹을 때 흔히 위장관 부작용을 일으켜 바르는 제형이 개발되었다[26]. Piper chaba Hunt.로 표기한 태국 열매 추출물은 생쥐·쥐에서 1,000 mg/kg까지 위 자극과 일시적 중추신경 억제 징후 외에 큰 독성이 없었다[22]. 후추·자바후추·생강 외용제를 모기 물린 자리에 바른 무작위 대조시험에서는 대조 제품보다 나은 효과가 없었다[20]."},
]

compounds = [
 {"name":"Piperine","name_ko":"피페린","class":"피페리딘 알칼로이드(피페라마이드)","role":"marker","part":"열매",
  "content_text":"태국 시판 열매 95% 에탄올 추출물 중 26.79%(HPLC)[6]; 오키나와 생과에서 녹색→적색으로 익을수록 감소(수치는 초록에서 확인하지 못함)[5]",
  "activity_ko":"고지방식 비만 생쥐에서 피페르노날린 등과 함께 항비만 성분으로 분리됨[4]; 티로시네이스 36.1% 억제[11]","source":[4,5,6,11]},
 {"name":"Pipernonaline","name_ko":"피페르노날린","class":"피페리딘 알칼로이드","role":"bioactive","part":"열매",
  "content_text":"열매에서 분리(함량은 초록에서 확인하지 못함)[4, 9]",
  "activity_ko":"PC12 세포 100 µM에서 신경돌기 신장 양성 24.3%, 생쥐 경구 투여 시 스코폴라민·코르티코스테론 유발 기억 장애 개선[9]","source":[4,9]},
 {"name":"Dehydropipernonaline","name_ko":"데하이드로피페르노날린","class":"피페리딘 알칼로이드","role":"bioactive","part":"열매",
  "content_text":"열매에서 분리(함량은 초록에서 확인하지 못함)[4, 9]",
  "activity_ko":"PC12 세포 100 µM에서 신경돌기 신장 양성 21.1%[9]; PPARδ 활성화 항비만 성분군[4]","source":[4,9]},
 {"name":"Pipercide","name_ko":"피퍼사이드","class":"아마이드 알칼로이드","role":"bioactive","part":"열매",
  "content_text":"열매에서 분리(함량은 초록에서 확인하지 못함)[9]",
  "activity_ko":"PC12 세포 100 µM에서 신경돌기 신장 양성 1.8%로 약함(피페리딘 골격이 활성에 중요)[9]","source":[9]},
 {"name":"Piperlongumine","name_ko":"피페르롱구민(피플라르틴)","class":"아마이드 알칼로이드","role":"bioactive","part":"열매 추출물",
  "content_text":"자바후추 추출물의 성분 분석·친화 포획으로 확인(함량은 초록에서 확인하지 못함)[10]",
  "activity_ko":"황색포도알균 소테이스 A 억제 IC50 27.83 ± 1.04 µmol/L, 바이오필름 형성 억제[10]","source":[10]},
 {"name":"Pellitorine","name_ko":"펠리토린","class":"알킬아마이드","role":"bioactive","part":"열매",
  "content_text":"열매에서 분리된 기지 성분 22종 가운데 하나(함량은 초록에서 확인하지 못함)[11]",
  "activity_ko":"티로시네이스 40.7% 억제(중등도)[11]","source":[11]},
 {"name":"Retroframide A","name_ko":"레트로프라마이드 A","class":"알킬아마이드","role":"bioactive","part":"열매",
  "content_text":"열매에서 새 알킬아마이드 레트로프라마이드 A–D 분리(함량은 초록에서 확인하지 못함)[11]",
  "activity_ko":"구조 규명 연구로 개별 활성은 초록에서 확인하지 못함[11]","source":[11]},
 {"name":"Retrofractamide D","name_ko":"레트로프락타마이드 D","class":"불포화 아마이드","role":"bioactive","part":"자바후추(부위는 초록에서 확인하지 못함)",
  "content_text":"자바후추에서 얻어 구조를 완전히 규명(함량은 초록에서 확인하지 못함)[12]",
  "activity_ko":"구조 규명 연구[12]","source":[12]},
 {"name":"Retrofractamide B","name_ko":"레트로프락타마이드 B","class":"피페라마이드","role":"bioactive","part":"열매(향신료)",
  "content_text":"후추속 향신료 피페라마이드 22종 LC-DAD 정량 대상 가운데 하나(자바후추 수치는 초록에서 확인하지 못함)[13]",
  "activity_ko":"후추속 향신료의 피페라마이드 조성 차이를 이루는 성분[13]","source":[13]},
 {"name":"Retrofractoside A","name_ko":"레트로프락토사이드 A","class":"아마이드 배당체","role":"bioactive","part":"열매",
  "content_text":"열매에서 새 아마이드 배당체 레트로프락토사이드 A–D와 페닐프로파노이드 배당체 E·F 분리(함량 확인하지 못함)[15]",
  "activity_ko":"함께 분리된 32종 중 (E)-N-(테트라하이드로-2H-피란-2-일)신남아마이드만 150 µM에서 혈소판 응집 52.0% 억제[15]","source":[15]},
 {"name":"beta-Caryophyllene","name_ko":"β-카리오필렌","class":"세스퀴테르펜","role":"bioactive","part":"열매 정유",
  "content_text":"D기 열매 정유 중 27.71%(면적 정규화 상대 함량)[7]; 오키나와 열매 가공품의 주요 테르펜 가운데 하나[8]",
  "activity_ko":"자바후추 열매 향의 주된 세스퀴테르펜[7, 8]","source":[7,8]},
 {"name":"alpha-Humulene","name_ko":"α-휴물렌","class":"세스퀴테르펜","role":"bioactive","part":"열매 정유",
  "content_text":"D기 열매 정유 중 12.85%(상대 함량)[7]",
  "activity_ko":"D기 정유의 특징 알켄 성분[7]","source":[7]},
 {"name":"Germacrene D","name_ko":"저마크렌 D","class":"세스퀴테르펜","role":"bioactive","part":"열매 정유",
  "content_text":"D기 열매 정유 중 12.36%(상대 함량)[7]; 가공 방법별 향 성분 분석의 주요 테르펜[8]",
  "activity_ko":"주성분 분석에서 PC1의 주된 기여 성분[7]","source":[7,8]},
 {"name":"Linalool","name_ko":"리날로올","class":"모노테르펜 알코올","role":"bioactive","part":"열매",
  "content_text":"가공 열매의 테르펜(리날로올·β-카리오필렌·α-카리오필렌·저마크렌 D) 합계 57.6–88.1%(상대 함량)[8]",
  "activity_ko":"발달 단계별 정유 주성분 분석에서 PC2의 주된 기여 성분[7]","source":[7,8]},
 {"name":"Benzyl benzoate","name_ko":"벤질 벤조에이트","class":"방향족 에스터","role":"bioactive","part":"잎 정유(식품 사용 부위 아님)",
  "content_text":"베트남산 잎 정유 중 14.4%(미르센 14.4%, 바이사이클로엘레멘 9.9%)[16]",
  "activity_ko":"잎 정유 주성분; 잎은 국내 식품원료 사용 부위가 아님[1, 16]","source":[1,16]},
]

assays = [
 {"role":"literature","compound":"Piperine","compound_ko":"피페린","part":"열매(태국 전통 약재상 구입 건조 열매) 95% 에탄올 추출물",
  "content":"에탄올 추출물 중 26.79%(추출 수율 9.034%)[6]","method":"HPLC-PDA",
  "conditions":{"instrument":"Shimadzu Prominence HPLC(LC-20AD 이원 펌프, SIL-20A HT 자동시료주입기, CTO-20A 칼럼 오븐, SPD-M20A 광다이오드어레이 검출기)",
   "column":"Shimadzu Shim-pack GIST C18 (4.6 × 250 mm, 5 µm)","mobile_phase":"아세토니트릴 48% : 1% 아세트산 수용액 52%","gradient":"등용매(isocratic)",
   "flow":"1.0 mL/min","temp":"40 °C","detection":"341 nm","injection":"10 µL",
   "sample_prep":"분쇄 열매를 95% 에탄올로 72시간 침지, 여과·감압 농축; 추출물을 50% 아세토니트릴로 희석해 0.45 µm 멤브레인 여과",
   "standard":"피페린 분석용 표준품(Sigma-Aldrich)을 50% 아세토니트릴에 녹여 검량선 작성","linearity":"","lod":"","loq":"","recovery":""},
  "rationale":"피페린은 자바후추 열매 추출물의 주성분이며, 이 연구에서 피페린 함량이 α-글루코시데이스 억제 활성과 유의한 상관을 보여 활성 지표로 쓰였다. 전문(Methods)에서 조건을 옮겼고, 직선성·검출한계·정량한계·회수율은 전문에서 확인하지 못함[6].",
  "source":[6],"url":doi("10.1016/j.heliyon.2023.e13063"),"source_kind":"paper"},
 {"role":"literature","compound":"beta-Caryophyllene (with alpha-humulene and germacrene D)","compound_ko":"β-카리오필렌(α-휴물렌·저마크렌 D)","part":"열매 정유(중국열대농업과학원 유전자원 포장 재배, 발달 단계 A–D)",
  "content":"D기 정유 중 β-카리오필렌 27.71%, α-휴물렌 12.85%, 저마크렌 D 12.36%(면적 정규화 상대 함량)[7]","method":"수증기 증류-GC-MS",
  "conditions":{"instrument":"","column":"HP-5MS (30 m × 0.25 mm × 0.25 µm)","mobile_phase":"운반기체 헬륨(순도 99.999%)",
   "gradient":"40 °C 5분 유지 → 4 °C/min로 220 °C, 5분 유지 → 10 °C/min로 300 °C, 5분 유지","flow":"1 mL/min",
   "temp":"주입구 250 °C; 이온원 230 °C; 전달관 300 °C","detection":"전자 이온화 70 eV, 스캔 범위 30–400 amu",
   "injection":"0.5 µL, 비분할(splitless), 용매 지연 4분",
   "sample_prep":"생과를 70 °C에서 30초 데친 뒤 40 °C에서 16시간 건조, 40메시 분쇄; 시료 25.00 g과 증류수 250 mL로 GB/T 17527-2009에 따라 4시간 수증기 증류",
   "standard":"NIST 14 질량 스펙트럼 라이브러리와 C7–C30 n-알케인 선형 머무름 지수로 동정; 면적 정규화법으로 상대 함량 계산","linearity":"","lod":"","loq":"","recovery":""},
  "rationale":"β-카리오필렌·α-휴물렌·저마크렌 D는 익은 열매(D기) 정유의 특징 알켄 성분으로 향 품질과 수확 시기 판단의 지표가 된다. 표준품 정량이 아닌 상대 함량이며, 전문(Methods)에서 조건을 옮겼다[7].",
  "source":[7],"url":doi("10.3390/foods11162528"),"source_kind":"paper"},
 {"role":"literature","compound":"Piperamides (piperine, retrofractamide B, guineensine, piperchabamide C 등 22종)","compound_ko":"피페라마이드 22종","part":"후추속 향신료 열매(자바후추 포함)",
  "content":"","method":"LC-HRMS/MS(동정), LC-DAD(정량)",
  "conditions":{"instrument":"","column":"","mobile_phase":"","gradient":"","flow":"","temp":"","detection":"DAD(정량); 고분해능 탠덤 질량분석(동정)","injection":"","sample_prep":"","standard":"","linearity":"","lod":"","loq":"","recovery":""},
  "rationale":"피페라마이드 조성으로 후추속 향신료를 구분할 수 있고, 자바후추는 후추·필발과 다른 양상을 보일 수 있다고 보고됨. 초록만 확인했고 전문 확인 못함; 자바후추 시료의 개별 함량도 확인하지 못함[13].",
  "source":[13],"url":doi("10.1016/j.foodres.2021.110123"),"source_kind":"paper"},
]

d = {"slug":"piper-retrofractum","name_ko":"자바후추","name_en":"Javanese long pepper (Balinese long pepper)",
 "scientific_name":"Piper retrofractum Vahl","aliases":["자바후추열매","Javanese long pepper","Balinese long pepper","Java long pepper","히하츠모도키(hihatsumodoki)","cabya"],
 "sections":sections,"compounds":compounds,"markers":[],"nutrients":[],"assays":assays,
 "production":[],"world":[],"gi":[],"orgs":[],"sources":sources}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in sections: print(s["key"], len(s["body"]))
