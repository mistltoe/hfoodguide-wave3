import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
PM = "https://pubmed.ncbi.nlm.nih.gov/{}/"
PMC = "https://pmc.ncbi.nlm.nih.gov/articles/{}/"
I1020 = "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020"
A = "2026-11-02"
sources = [
 (1, "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 여뀌 2개 원료명 행: 여뀌잎(부위 잎)·여뀌순(부위 순), 학명 'Persicaria hydropiper L. / Persicaria vernalis Nakai', 다른 이름 버들여뀌, 영문명 Water pepper, 식품원료(A코드)·식물, 사용조건 '사용가능부위 : 순, 잎', 상태 사용가능. 로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json", I1020, "식품의약품안전처", "2026-10-13"),
 (2, "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 관련 행: 복합원료(U코드) '신곡'(Massa Medicata Fermentata, 사용불가, 기준 '전량수출용 원재료. 밀가루 또는 밀기울에 팥가루, 으깬 살구씨, 개똥쑥즙, 도꼬마리즙, 버들여뀌즙 등의 재료를 반죽하여 누룩균으로 발효시킨 누룩이다.'); 같은 속 원료 며느리밑씻개(순·잎 사용가능)·며느리배꼽·바보여뀌잎·고마리·털여귀잎(사용가능)·털여귀열매(사용불가)·Red leg잎(Persicaria vulgaris, 봄여뀌, 사용가능). 로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json", I1020, "식품의약품안전처", "2026-10-13"),
 (3, "Ethnobotanical, Phytochemical, Pharmacological, and Toxicological Aspects of Persicaria hydropiper (L.) Delarbre. Evid Based Complement Alternat Med 2014;2014:782830 (PMID 24834098, PMC4009190, doi:10.1155/2014/782830; 전문 확인)", PMC.format("PMC4009190"), "Hindawi / PubMed Central", A),
 (4, "Persicaria hydropiper (L.) Delarbre: A review on traditional uses, bioactive chemical constituents and pharmacological and toxicological activities. J Ethnopharmacol 251:112516 (PMID 31884037, doi:10.1016/j.jep.2019.112516; 초록 확인)", PM.format("31884037"), "Elsevier / PubMed", A),
 (5, "A review on the ethnopharmacology, phytochemistry and pharmacology of Polygonum hydropiper Linn. J Pharm Pharmacol 2022;74(5):619-645 (PMID 35259273, doi:10.1093/jpp/rgab175; 초록 확인)", PM.format("35259273"), "Oxford University Press / PubMed", A),
 (6, "The traditional herb Polygonum hydropiper from China: a comprehensive review on phytochemistry, pharmacological activities and applications. Pharm Biol 2023;61(1) (PMID 37194713, PMC10193905, doi:10.1080/13880209.2023.2208639; 전문 확인)", PMC.format("PMC10193905"), "Taylor & Francis / PubMed Central", A),
 (7, "Review on Pharmacological and Phytochemical Prospects of Traditional Medicinal Plant: Persicaria hydropiper (Smartweed). Curr Top Med Chem 2021;21(12):1027-1036 (PMID 33655861, doi:10.2174/1568026621666210303145045; 초록 확인)", PM.format("33655861"), "Bentham Science / PubMed", A),
 (8, "HPLC-DAD phenolics analysis, α-glucosidase, α-amylase inhibitory, molecular docking and nutritional profiles of Persicaria hydropiper L. BMC Complement Med Ther 2022;22:26 (PMID 35086537, PMC8793238, doi:10.1186/s12906-022-03510-7; 전문 확인)", PMC.format("PMC8793238"), "BioMed Central / PubMed Central", A),
 (9, "New Perspectives on the Old Uses of Traditional Medicinal and Edible Herbs: Extract and Spent Material of Persicaria hydropiper (L.) Delarbre. Nutrients 2024;16(19):3368 (PMID 39408335, PMC11478433, doi:10.3390/nu16193368; 전문 확인)", PMC.format("PMC11478433"), "MDPI / PubMed Central", A),
 (10, "Identification of Antiglycative Compounds in Japanese Red Water Pepper (Red Leaf Variant of the Persicaria hydropiper Sprout). Molecules 2018;23(9):2319 (PMID 30208642, PMC6225476, doi:10.3390/molecules23092319; 전문 확인)", PMC.format("PMC6225476"), "MDPI / PubMed Central", A),
 (11, "Inhibitory compound of tyrosinase activity from the sprout of Polygonum hydropiper L. (Benitade). Biol Pharm Bull 2007;30(3):595-597 (PMID 17329865, doi:10.1248/bpb.30.595; 초록 확인)", PM.format("17329865"), "日本薬学会 / PubMed", A),
 (12, "Comparison of the chemical composition of three species of smartweed (genus Persicaria) with a focus on drimane sesquiterpenoids. Phytochemistry 2014;108:129-136 (PMID 25453911, doi:10.1016/j.phytochem.2014.10.001; 초록 확인)", PM.format("25453911"), "Elsevier / PubMed", A),
 (13, "Comparison of volatile constituents of Persicaria odorata (Lour.) Soják and Persicaria hydropiper L. Spach. J Agric Food Chem 2006;54(8):3067-3071 (PMID 16608232, doi:10.1021/jf0531611; 초록 확인)", PM.format("16608232"), "American Chemical Society / PubMed", A),
 (14, "Identification of a drimenol synthase and drimenol oxidase from Persicaria hydropiper, involved in the biosynthesis of insect deterrent drimanes. Plant J 2017;90(6):1052-1063 (PMID 28258968, doi:10.1111/tpj.13527; 초록 확인)", PM.format("28258968"), "Wiley / PubMed", A),
 (15, "Drimane Sesquiterpene-Rich Volatile Oil Profile of Water Pepper (Persicaria hydropiper), a Widely Distributed Spicy Herb. J Food Sci 2026;91(4):e71010 (PMID 41940699, doi:10.1111/1750-3841.71010; 초록 확인)", PM.format("41940699"), "Wiley / PubMed", A),
 (16, "Subchronic toxicity study of water pepper extract in F344 rats. Food Chem Toxicol 2006;44(8):1236-1244 (PMID 16542768, doi:10.1016/j.fct.2006.01.020; 초록 확인)", PM.format("16542768"), "Elsevier / PubMed", A),
 (17, "Prospective single-arm observational study of human chymase inhibitor Polygonum hydropiper L in subjects with hypertension. Clin Exp Hypertens 41(8):717-725 (PMID 30582370, doi:10.1080/10641963.2018.1545847; 초록 확인)", PM.format("30582370"), "Taylor & Francis / PubMed", A),
 (18, "Synthetic and Biological Studies of Sesquiterpene Polygodial: Activity of 9-Epipolygodial against Drug-Resistant Cancer Cells. ChemMedChem 2015;10(12):2014-2026 (PMID 26434977, PMC4831215, doi:10.1002/cmdc.201500360; 초록 확인)", PM.format("26434977"), "Wiley / PubMed", A),
 (19, "Distribution of drimane sesquiterpenoids and tocopherols in liverworts, ferns and higher plants: Polygonaceae, Canellaceae and Winteraceae species. Nat Prod Commun 2012;7(6):685-692 (PMID 22816285; 초록 확인)", PM.format("22816285"), "SAGE / PubMed", A),
 (20, "The complete chloroplast genomes of Persicaria hydropiper and Persicaria pubescens (Polygonaceae). Mitochondrial DNA B Resour 2025;10(11):1008-1011 (PMID 41079457, PMC12509295, doi:10.1080/23802359.2025.2567461; 전문 확인)", PMC.format("PMC12509295"), "Taylor & Francis / PubMed Central", A),
 (21, "[The making method of Shen Qu in Qimin Yaoshu]. Zhonghua Yi Shi Za Zhi 2022 (PMID 35570342, doi:10.3760/cma.j.cn112155-20200521-00075; 중국어 논문, 영문 초록 확인)", PM.format("35570342"), "中华医学会 / PubMed", A),
 (22, "Preparation of Fangxian traditional Xiaoqu and its evolution of microbial communities and aroma compounds during fermentation. Food Res Int 2024;199:115344 (PMID 39658149, doi:10.1016/j.foodres.2024.115344; 초록 확인)", PM.format("39658149"), "Elsevier / PubMed", A),
 (23, "Mechanism of Polygonum hydropiper reducing ethyl carbamate in Chinese rice wine (Huangjiu) brewing. Food Microbiol 2024;125:104628 (PMID 39448146, doi:10.1016/j.fm.2024.104628; 초록 확인)", PM.format("39448146"), "Elsevier / PubMed", A),
 (24, "Immune effects and antiacetylcholinesterase activity of Polygonum hydropiper L. Biosci Microbiota Food Health 35(2):69-75 (PMID 27200260, PMC4858880, doi:10.12938/bmfh.2015-016; 초록 확인)", PM.format("27200260"), "BMFH Press / PubMed", A),
]
S = {}
S["overview"] = ("한눈에 보기",
"여뀌(Persicaria hydropiper (L.) Delarbre, 이명 Polygonum hydropiper L.)는 마디풀과(Polygonaceae) 여뀌속의 한해살이풀로, 영어로는 water pepper·marsh pepper·smartweed라고 부른다[3, 4]. 잎과 어린순에서 매운맛이 나며, 이 매운맛은 드리메인형 세스퀴테르펜 디알데하이드인 폴리고디알(polygodial)에서 온다[13].\n\n"
"식약처 「식품원료 목록」에는 학명이 'Persicaria hydropiper L. / Persicaria vernalis Nakai', 다른 이름이 버들여뀌, 영문명이 Water pepper로 적혀 있다[1]. 원료명은 여뀌잎(부위 잎)과 여뀌순(부위 순) 두 개이고, 둘 다 '사용가능부위 : 순, 잎' 조건의 사용가능 원료다[1]. 즉 식품원료로 쓸 수 있는 부위는 순과 잎뿐이며, 뿌리·씨앗·꽃이삭은 목록에 오르지 않았다[1]. 건강기능식품 고시형 원료의 원재료로 쓰이지는 않는다[1].\n\n"
"해외에서는 일본에서 어린순을 회의 곁들임과 향신료로 쓰고, 동남아시아에서는 잎을 락사 요리에 넣는다[3]. 성분 연구는 플라보노이드(퀘르세틴 배당체 등)와 폴리고디알 같은 드리메인형 세스퀴테르펜, 페닐프로파노이드에 집중되어 있다[3, 6, 7]. 보고된 효과는 대부분 세포·동물 실험이며, 사람 연구는 11명 대상 단일군 예비시험 1건만 확인했다[4, 17].")
S["history"] = ("이용의 역사",
"여뀌는 유럽과 아시아에서 오래전부터 향신료와 민간약으로 쓰였다[3, 5]. 유럽에서는 이뇨제·통경제로, 전초 달인 물은 설사·소화불량·치질 등에 쓰였다는 기록이 있다[3]. 인도·방글라데시에서는 잎즙을 생리통·지혈에 쓰고, 전초를 짓이겨 물고기를 잡는 어독(魚毒)이나 저장 곡물의 살충제로 쓴 사례가 보고되었다[3].\n\n"
"중국에서는 랄료(辣蓼, laliao)라 부르며 1977년판 중국약전에 전초가 수재되었다[6]. 6세기 농서 『제민요술』에 나오는 누룩 신곡(神曲)의 부재료로 여뀌속 식물이 쓰였고, 후대에는 여뀌와 털여뀌로 좁혀졌다[21]. 오늘날에도 중국 후베이성 팡셴(房县) 황주의 전통 소곡(小曲) 누룩을 여뀌로 만든다[22].\n\n"
"식약처 「식품원료 목록」에도 버들여뀌즙을 넣어 발효시킨 누룩 '신곡'이 복합원료로 올라 있으나 전량수출용 원재료로서 국내 식품에는 사용불가로 분류되어 있다[2]. 일본에서는 붉은 잎 계통의 새싹(베니타데)을 회와 함께 내고, 잎 추출물이 절임·드레싱의 보존용 첨가물로 쓰였다는 기록도 있다[3, 10]. 우리나라에서의 전통 식용 기록은 이번 조사에서 확인하지 못함.")
S["biology"] = ("식물학적 특징",
"여뀌는 키 40–70 cm의 한해살이풀로, 줄기는 누워 자라다 곧추서거나 곧게 서며 가지를 치고 털이 없다[3]. 잎은 피침형 또는 긴 타원상 피침형으로 길이 4–10 cm, 너비 0.4–2.5 cm이고 잎자루는 0.1–0.8 cm, 끝은 뾰족하며 가장자리에 털이 있다[3]. \n\n"
"꽃차례는 줄기 끝과 잎겨드랑이에 나며 곧게 서거나 늘어지고, 꽃이 3–5개씩 모여 달린다[3]. 화피는 아래쪽이 녹색, 위쪽이 흰색이나 분홍색이며 수술은 6–8개, 암술대는 2–3개다[3]. 다른 조사에서는 키 30–80 cm, 잎에 매운맛이 나는 투명한 샘점이 있고 열매는 윤기 나는 검은 달걀꼴 수과로 기술되었다[20].\n\n"
"원산지는 서아시아·시베리아·중국·동아시아·인도아대륙·인도차이나 등 온대·열대 아시아와 유럽, 북아프리카, 오스트레일리아에 걸친다[3]. 물가와 습지, 논밭 같은 축축한 곳에 흔하며 경작지 잡초로도 우세하게 자란다[3]. 폴리고디알 함량은 꽃이 수정된 직후의 꽃에서 가장 높고, 잎은 꽃보다 약 10배 적다[12].")
S["related_species"] = ("근연종과 시료 종 확인",
"여뀌속에는 겉모양이 비슷한 종이 많아 시료 종 확인이 중요하다[12, 15]. 식약처 「식품원료 목록」에는 같은 속에서 며느리밑씻개(P. senticosa, 순·잎), 며느리배꼽(P. perfoliata, 순), 바보여뀌(P. pubescens, 잎), 고마리(P. thunbergii, 잎), 털여뀌(P. orientale, 잎 사용가능·열매 사용불가), 봄여뀌(P. vulgaris, 잎)가 따로 올라 있다[2]. 원료마다 쓸 수 있는 부위가 다르므로 여뀌 자료와 섞어 쓰면 안 된다[1, 2].\n\n"
"같은 습지에 자라는 세 종을 비교한 연구에서 여뀌 꽃의 폴리고디알은 생체중 1 g당 약 6.2 mg이었으나, P. minor는 그 200분의 1, 봄여뀌(P. maculosa)는 10만분의 1 수준이었다[12]. 반면 베트남고수(P. odorata)에서도 폴리고디알이 매운맛 성분으로 확인되어, 매운맛만으로 종을 가를 수는 없다[13].\n\n"
"엽록체 유전체 계통 분석에서 여뀌와 함께 분석된 다른 종은 바보여뀌(P. pubescens)였고, 두 종 모두 중국 전통 제제의 원료로 쓰인다[20]. 일본의 붉은 잎 새싹 베니타데는 여뀌의 붉은 잎 변이로, 녹색 새싹(아오타데)과 달리 시아니딘 배당체(이다인)를 함유한다[10]. 폴리고디알을 만드는 식물로는 여뀌와 그 붉은 품종(f. purpurascens) 외에 일부 우산이끼·고사리·카넬라과·윈테라과 식물이 있다[19].")
S["cultivation"] = ("재배와 생산",
"여뀌는 대부분 습지·물가·논밭에서 저절로 자라는 들풀로 채취되며, 경작지 잡초로 흔하다[3]. 중국에서는 허베이·허난·산시·장쑤·저장·후베이·푸젠·장시·광둥·광시·윈난 등 남북 여러 성의 낮은 산지, 강가, 습한 곳에 무리 지어 자란다[6]. 쓰촨의 한 제약회사는 엽록체 유전체 연구용 시료를 직접 재배해 공급했다[20].\n\n"
"일본에서는 베니타데 새싹이 식료품 시장에서 팔린다[10]. 생 베니타데 100 g을 말리면 건조물 12.8 g이 얻어졌다고 보고되었다[10]. 중국 연구에서는 여뀌 시료의 납·카드뮴·비소·수은 4종 중금속이 녹색무역기준을 만족했다고 정리되었다[6].\n\n"
"국내 재배 면적·생산량 통계는 농식품부 특용작물 생산실적과 통계청 농작물생산조사 파일에서 확인하지 못함. 지리적 표시 등록, 관련 협회·연구회도 확인하지 못함.")
S["processing"] = ("가공과 제품",
"식품원료로는 순과 잎만 쓸 수 있으며, 목록에 오른 원료명도 여뀌잎과 여뀌순 두 가지다[1]. 일본에서는 어린순을 회에 곁들이고, 물이나 에탄올로 우린 잎 추출물을 절임·드레싱·조리식품의 보존 첨가물로 썼다[3]. 세르비아에서는 잎을 수프·스튜·샐러드에, 어린순을 짭짤한 파이에 쓰며 말린 지상부가 차 형태로 유통된다[9].\n\n"
"발효 분야에서는 중국 황주 누룩에 여뀌를 넣는다[22, 23]. 팡셴 전통 소곡에 여뀌를 넣으면 발효액의 향 강도가 높아졌다[22]. 황주 발효에 여뀌나 그 추출물을 넣었을 때 대조군의 에틸카바메이트 함량이 여뀌군보다 약 355.55% 높았다는 실험 보고도 있다[23]. 국내 목록의 누룩 '신곡'은 버들여뀌즙을 넣지만 전량수출용이어서 국내 식품에는 쓸 수 없다[2].\n\n"
"한 연구는 여뀌 열수 추출물을 치매 예방용 기능성식품 후보로 검토했으나 시험관 실험 단계였다[24]. 사람 대상 예비시험에서는 말린 여뀌 분말을 하루 200–2,000 mg 썼다[17]. 국내 건강기능식품 생산실적에서 여뀌 원료 제품은 확인하지 못함.")
S["genetics"] = ("유전체와 종 판별",
"여뀌의 엽록체 유전체는 159,054 bp의 고리 모양으로, 대단일복제부·소단일복제부와 한 쌍의 역반복부로 이루어진다[20]. 유전자는 모두 130개로 단백질 암호 유전자 86개, tRNA 37개, rRNA 8개이며 인트론을 가진 유전자가 23개다[20]. 연구진은 이 서열이 약재 원료의 분자 판별과 여뀌속 계통 연구에 쓰일 수 있다고 밝혔다[20].\n\n"
"매운맛 성분의 생합성 유전자도 밝혀졌다[14]. 여뀌에서 분리한 드리메놀 합성효소(PhDS)는 파르네실 이인산으로부터 드리메놀만 만들고, 시토크롬 P450 드리메놀 산화효소(PhDOX1)는 드리메놀을 드리멘디올로 바꾼다[14]. 효모·담배 잎에서 두 유전자를 함께 발현하면 곤충 섭식 억제 물질인 신나몰라이드가 생겼다[14].\n\n"
"붉은 잎 계통(베니타데)은 녹색 계통에 없는 시아니딘 3-갈락토사이드를 만들며, 그 차이의 유전적 원인은 아직 밝혀지지 않았다[10]. 염색체 수와 핵 유전체 해독 결과는 확인하지 못함.")
S["safety"] = ("안전성과 사용 조건",
"식약처 「식품원료 목록」상 여뀌는 순과 잎만 사용가능한 원료다[1]. 고시형 건강기능식품 원료가 아니므로 고시 섭취 시 주의사항은 없다[1]. 식품의약품안전처 등 공공기관의 알레르기·잔류농약 안전 정보는 확인하지 못함.\n\n"
"매운맛 성분 폴리고디알은 피부 자극 물질로, 지상부를 반복해서 만지면 피부에 물집이 생길 수 있다[3]. 폴리고디알은 TRPV1 수용체 작용제로 알려져 있다[18]. 폴리고디알 7.0%를 함유한 잎 에탄올 분획은 에임스 시험과 염색체 이상 시험에서 양성이었으나 생쥐 골수 소핵 시험에서는 음성이었다[3].\n\n"
"같은 추출물을 F344 랫드에 13주간 먹인 시험에서 무독성량은 사료 중 1,000 ppm, 즉 수컷 57.4, 암컷 62.9 mg/kg/일이었다[16]. 4,000 ppm에서는 체중 증가 억제, 약한 간·신장 독성 소견, 암컷의 경미한 용혈성 빈혈이 나타났다[16]. 메탄올 추출물을 생쥐 복강에 주사한 시험에서 LD50은 500 mg/kg으로 추정되었다[3]. 여뀌는 돼지와 양에게 독성이 있다고 보고되었다[3].\n\n"
"인도에서는 말린 뿌리 가루를 임신 중절에 쓴 민간 기록이 있고, 뿌리 추출물은 랫드에서 에스트로겐 유사·항생식 작용을 보였다[3]. 뿌리는 식품원료 사용 부위가 아니며, 임신부의 잎·순 섭취 안전성 자료는 확인하지 못함. 11명 대상 예비시험에서 건조 분말 4,000 mg 1회 섭취와 하루 최대 2,000 mg 섭취에서 이상반응은 없었다[17].")
sections = [{"key": k, "title": v[0], "body": v[1]} for k, v in S.items()]

def C(name, ko, cls, role, part, content, act, src):
    return {"name": name, "name_ko": ko, "class": cls, "role": role, "part": part, "content_text": content, "activity_ko": act, "source": src}
compounds = [
 C("Polygodial", "폴리고디알", "드리메인형 세스퀴테르펜 디알데하이드", "marker", "꽃·잎·지상부", "꽃 생체중 1 g당 약 6.2 mg, 잎은 꽃의 약 1/10(GC-MS)[12]; 아만성 독성시험에 쓴 잎 에탄올 분획 중 7.0%[3]; 정유에서는 함량이 비교적 낮고 용매 추출물의 주성분[15]", "여뀌 매운맛의 주성분[13]; TRPV1 작용제(세포 실험)[18]; 곤충 섭식 억제·항진균(시험관)[3]", [3, 12, 13, 15, 18]),
 C("Isopolygodial", "이소폴리고디알", "드리메인형 세스퀴테르펜", "bioactive", "잎·씨앗", "잎 디에틸에터 추출물과 씨앗에서 분리(수치는 확인하지 못함)[3]; 정유 중 이소폴리고디알/폴리고디알 함량 '중간 정도 높음'[15]", "폴리고디알의 이성질체[3]", [3, 15]),
 C("Warburganal", "와부르가날", "드리메인형 세스퀴테르펜 디알데하이드", "bioactive", "잎·씨앗", "잎 디에틸에터 추출물과 씨앗에서 분리(수치는 확인하지 못함)[3]", "아프리카거염벌레·진딧물 섭식 억제(곤충 실험)[3]", [3]),
 C("Drimenol", "드리메놀", "드리메인형 세스퀴테르펜 알코올", "bioactive", "지상부 정유", "인도 동북부 시료 26개의 정유 1 g당 64.9–154.6 mg[15]", "폴리고디알 생합성 중간체(PhDS 산물)[14]; 자궁경부암·폐암 세포 IC50 14.75·7.64 µM(세포 실험)[15]", [14, 15]),
 C("Isodrimeninol", "이소드리메니놀", "드리메인형 세스퀴테르펜", "bioactive", "지상부 정유", "정유 1 g당 34.7–112.1 mg[15]", "정유의 주요 3성분 중 하나[15]", [15]),
 C("Confertifolin", "콘페르티폴린", "드리메인형 세스퀴테르펜 락톤", "bioactive", "잎 정유", "잎 정유에서 분리(수치는 확인하지 못함)[3]", "세균 1종 MIC 31.25 µg/mL, 일부 진균 MIC 7.81 µg/mL(시험관)[3]", [3]),
 C("Cyanidin 3-galactoside", "시아니딘 3-갈락토사이드(이다인)", "안토시아닌", "bioactive", "순(붉은 잎 새싹 베니타데)", "열수 추출물 고형분 1 mg당 72 nmol(34.5 µg), 생 새싹 기준 수율 0.14%(계산값)[10]", "붉은색의 원인 색소; 형광 최종당화산물 생성 억제(시험관)[10]", [10]),
 C("Hyperoside", "하이퍼로사이드(퀘르세틴 3-갈락토사이드)", "플라보놀 배당체", "bioactive", "순(베니타데)·지상부", "베니타데 열수 추출물 고형분 1 mg당 35 nmol(16.4 µg)[10]; 지상부 50% 에탄올 추출물 2.07 ± 0.12 mg/g DW[9]", "형광 최종당화산물 생성 억제(시험관)[10]", [9, 10]),
 C("Isoquercitrin", "이소퀘르시트린(퀘르세틴 3-글루코사이드)", "플라보놀 배당체", "bioactive", "잎·지상부", "지상부 50% 에탄올 추출물 3.81 ± 0.11 mg/g DW[9]; 베니타데 추출물 고형분 1 mg당 8.3 µg(동정 미확정 피크)[10]", "지질과산화 억제 ID50 0.6 ppm(시험관)[3]; 지방세포 분화 억제(세포 실험)[3]", [3, 9, 10]),
 C("Quercetin", "퀘르세틴", "플라보놀", "bioactive", "지상부·전초", "지상부 50% 에탄올 추출물 2.34 ± 0.70 mg/g DW[9]; 전초 메탄올 추출물 57.9 mg/g[8]", "항산화(시험관)[3]", [3, 8, 9]),
 C("Kaempferol 3-glucoside", "캠페롤 3-글루코사이드", "플라보놀 배당체", "bioactive", "지상부·잎", "지상부 50% 에탄올 추출물 4.18 ± 0.17 mg/g DW[9]", "잎 항산화 플라보노이드의 하나[3]", [3, 9]),
 C("Kaempferol-3-(p-coumaroyl-diglucoside)-7-glucoside", "캠페롤-3-(p-쿠마로일다이글루코사이드)-7-글루코사이드", "아실 플라보놀 배당체", "bioactive", "식물체(부위 원문 미기재) 메탄올 추출물", "메탄올 추출물 275.4 mg/g(HPLC-DAD, 24개 성분 중 최다)[8]", "α-글루코시데이스 도킹 점수 최상위(컴퓨터 모의)[8]", [8]),
 C("Taxifolin", "탁시폴린((2R,3R)-(+)-taxifolin)", "디하이드로플라보놀", "bioactive", "순(베니타데)", "새싹에서 활성 유도 분획으로 분리(함량은 확인하지 못함)[11]", "티로시네이스 억제 ID50 0.24 mM(시험관)[11]", [11]),
 C("Vanicoside A", "바니코사이드 A", "페닐프로파노이드 수크로스 에스터", "bioactive", "잎·줄기", "잎·줄기 메탄올 추출물에서 분리(수치는 확인하지 못함)[3]", "DPPH 라디칼 소거 SC50 26.7 µg/mL(시험관)[3]", [3]),
 C("Persicarin", "페르시카린", "황산화 플라보노이드", "bioactive", "잎·줄기", "잎 메탄올 추출물에서 분리(수치는 확인하지 못함)[3]", "랫드 대뇌피질 세포의 글루탐산 독성 보호 40.8–74.5%(10 µM, 세포 실험)[3]", [3]),
]
assays = [
 {"role": "literature", "compound": "Cyanidin 3-galactoside", "compound_ko": "시아니딘 3-갈락토사이드(이다인)·하이퍼로사이드",
  "part": "순(일본 교토 시장에서 산 붉은 잎 새싹 베니타데, 건조 분말)",
  "content": "열수 추출물(PEW) 고형분 1 mg당 이다인 72 nmol(34.5 µg), 하이퍼로사이드 35 nmol(16.4 µg); 머무름 시간 26.4·31.8분[10]",
  "method": "HPLC-UV",
  "conditions": {"instrument": "Shimadzu HPLC-UV", "column": "YMC Pack ODS-AM, 250 mm × 6 mm I.D.", "mobile_phase": "0.1%(v/v) TFA 수용액 중 아세토니트릴", "gradient": "아세토니트릴 0–50% 선형 기울기, 50분", "flow": "1.0 mL/min", "temp": "40 °C", "detection": "270 nm", "injection": "20 μL(분취 시 200 μL)", "sample_prep": "건조 분말 2 g + 증류수 40 mL, 80 °C 75분 추출 → 3350×g 10분 원심분리, 여과; 고형분 5 mg/mL", "standard": "이다인·하이퍼린 표준품(Sigma-Aldrich), 0.4 nmol 첨가로 피크 일치 확인; UHPLC-QqTOF-MS로 m/z 449.108·465.103 확인", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "식품원료 부위인 순(새싹)에서 직접 정량한 성분이며, 이다인은 붉은 잎 계통의 색을 내는 성분이다[10]", "source": [10], "url": PMC.format("PMC6225476"), "source_kind": "paper"},
 {"role": "literature", "compound": "Quercetin", "compound_ko": "퀘르세틴 외 페놀 24종",
  "part": "식물체(파키스탄 습지 채집, 그늘 건조, 사용 부위 원문 미기재) 80% 메탄올 추출물",
  "content": "퀘르세틴 57.9 mg/g, 캠페롤-3-(p-쿠마로일다이글루코사이드)-7-글루코사이드 275.4 mg/g, 퀘르세틴-3-글루쿠로나이드 76.0 mg/g 등(추출물 기준)[8]",
  "method": "HPLC-DAD",
  "conditions": {"instrument": "Agilent 1260 Infinity HPLC(4원 펌프, 탈기기, 자동주입기, DAD)", "column": "Agilent Zorbax Eclipse Plus C18 rapid resolution(4.6 × 100 mm, 3.5 μm)", "mobile_phase": "", "gradient": "", "flow": "1 mL/min", "temp": "25 °C", "detection": "320 nm(스펙트럼 200–600 nm, 순도 95% 이상 피크만 정량)", "injection": "50 μL", "sample_prep": "추출물 100 mg을 메탄올 10 mL에 녹여 1시간 흔듦, 0.45 μm PTFE 필터 여과", "standard": "보유 표준품과 머무름 시간·흡수 스펙트럼 비교; 표준품이 없는 성분은 같은 응답계수 표준품 검량선 사용", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "여뀌 추출물의 페놀 조성을 종합적으로 정량한 연구다; 이동상·기울기는 원문이 이전 논문 방법을 따른다고만 적어 확인하지 못함[8]", "source": [8], "url": PMC.format("PMC8793238"), "source_kind": "paper"},
 {"role": "literature", "compound": "Kaempferol 3-glucoside", "compound_ko": "캠페롤 3-글루코사이드·퀘르세틴 배당체 등 페놀 45종 표적",
  "part": "지상부(세르비아 허브 공급업체의 차용 건조 지상부) 50% 에탄올 추출물",
  "content": "캠페롤 3-글루코사이드 4.18 ± 0.17, 퀘르세틴 3-글루코사이드 3.81 ± 0.11, 퀸산 3.68 ± 0.37, 퀘르세틴 2.34 ± 0.70 mg/g DW[9]",
  "method": "LC-MS/MS(ESI, 삼중사중극자)",
  "conditions": {"instrument": "Agilent 1200 Series HPLC + Agilent 6410A Triple Quad MS(ESI), MassHunter B.03.01", "column": "", "mobile_phase": "A: 0.05% 개미산 수용액, B: 메탄올", "gradient": "", "flow": "", "temp": "", "detection": "ESI-MS/MS", "injection": "", "sample_prep": "분말 10 g을 50% 에탄올 100 mL로 24시간 상온 침지(150 rpm) 3회, 6200×g 원심분리 후 감압 농축; A·B 1:1로 2 mg/mL 희석", "standard": "페놀 45종 혼합 표준품(ChromaDex·Fluka·Sigma-Aldrich)을 1.53–12,500 ng/mL 14단계 작업 표준액으로 희석", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "식용 지상부의 플라보놀 배당체를 정량했다; 칼럼·기울기·검증값은 원문이 이전 논문을 인용해 확인하지 못함[9]", "source": [9], "url": PMC.format("PMC11478433"), "source_kind": "paper"},
 {"role": "literature", "compound": "Polygodial", "compound_ko": "폴리고디알",
  "part": "꽃·잎(생체)", "content": "꽃 생체중 1 g당 약 6.2 mg, 잎은 꽃의 약 1/10[12]",
  "method": "GC-MS",
  "conditions": {"instrument": "", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "", "injection": "", "sample_prep": "", "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "여뀌 매운맛의 주성분이자 근연종과 구별되는 화학 지표다(봄여뀌는 10만분의 1 수준); 전문 확인 못함[12, 13]", "source": [12, 13], "url": PM.format("25453911"), "source_kind": "paper"},
]
nutrients = [{"form": "건조 분말(식물체, 사용 부위 원문 미기재; 논문 값)", "basis": "건조 분말 100 g당(%)", "items": [
  {"name": "단백질", "value": 17.38, "unit": "%"}, {"name": "수분", "value": 15.70, "unit": "%"},
  {"name": "회분", "value": 10.73, "unit": "%"}, {"name": "지방", "value": 4.18, "unit": "%"}], "source": [8]}]
d = {"slug": "persicaria-hydropiper", "name_ko": "여뀌", "name_en": "Water pepper (marsh pepper smartweed)",
     "scientific_name": "Persicaria hydropiper (L.) Delarbre",
     "aliases": ["버들여뀌", "여뀌잎", "여뀌순", "Polygonum hydropiper L.", "Persicaria hydropiper (L.) Spach", "Persicaria vernalis Nakai", "Water pepper", "Marsh pepper", "Smartweed", "辣蓼", "水蓼", "タデ(蓼)", "Benitade(붉은 잎 새싹)"],
     "sections": sections, "compounds": compounds, "markers": [], "assays": assays, "nutrients": nutrients,
     "production": [], "world": [], "gi": [], "orgs": [],
     "sources": [{"n": n, "title": t, "url": u, "publisher": p, "accessed": a} for n, t, u, p, a in sources]}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in sections: print(s["key"], len(s["body"]))
