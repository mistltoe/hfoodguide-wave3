import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
A = "2026-10-13"
def pm(pmid): return f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
S = [
 ("식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020)", "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "식품의약품안전처"),
 ("On the Manna of Sinai, and the Manna of Syria (1862; Tamarix mannifera 만나 분석 — 이 종 시료 아님)", "https://pmc.ncbi.nlm.nih.gov/articles/PMC6903540/", "The Dental Register 16(8):377-379 (PubMed 33696330)"),
 ("Tamarix mannifera Ehrenb. ex Bunge — Plants of the World Online 기록 (웹 검색 결과 요약으로만 확인, 원문 페이지 열람 못함)", "https://powo.science.kew.org/taxon/urn:lsid:ipni.org:names:828162-1", "Royal Botanic Gardens, Kew"),
 ("Antioxidant and antimicrobial activities of the edible medicinal halophyte Tamarix gallica L. and related polyphenolic constituents", pm(19500639), "Food Chem Toxicol 2009;47(8):2083-91, doi:10.1016/j.fct.2009.05.040"),
 ("Influence of biological, environmental and technical factors on phenolic content and antioxidant activities of Tunisian halophytes", pm(18940702), "C R Biol 2008;331(11):865-73, doi:10.1016/j.crvi.2008.07.024"),
 ("Anticancer effect of Tamarix gallica extracts on human colon cancer cells involves Erk1/2 and p38 action on G2/M cell cycle arrest", "https://pmc.ncbi.nlm.nih.gov/articles/PMC3853633/", "Cytotechnology 2013, doi:10.1007/s10616-013-9564-4"),
 ("Chemical profiling of maceration and decoction of Tamarix gallica L. organs and biological properties", pm(37702291), "Int J Environ Health Res 2024;34(6):2517-2528, doi:10.1080/09603123.2023.2256679"),
 ("Effect of O-methylated and glucuronosylated flavonoids from Tamarix gallica on α-glucosidase inhibitory activity", pm(27838961), "Biosci Biotechnol Biochem 2017;81(3):445-448, doi:10.1080/09168451.2016.1254538"),
 ("Inhibitory Activities of Antioxidant Flavonoids from Tamarix gallica on Amyloid Aggregation Related to Alzheimer's and Type 2 Diabetes Diseases", pm(28154265), "Biol Pharm Bull 2017;40(2):238-241, doi:10.1248/bpb.b16-00801"),
 ("Integrating In Vitro Bioactivities and In Silico Molecular Evaluation of Tamarix gallica from Western Algeria", "https://pmc.ncbi.nlm.nih.gov/articles/PMC13305346/", "Molecules 2026;31(12):2168, doi:10.3390/molecules31122168"),
 ("Multi-targeted therapeutic exploration of Tamarix gallica flowers for anti-ulcer activity and associated complications", "https://pmc.ncbi.nlm.nih.gov/articles/PMC11341922/", "J Ayurveda Integr Med 2024;15(4):100947, doi:10.1016/j.jaim.2024.100947"),
 ("Methanolic extract of Tamarix gallica attenuates hyperhomocysteinemia induced AD-like pathology and cognitive impairments in rats", "https://pmc.ncbi.nlm.nih.gov/articles/PMC6286848/", "Aging (Albany NY) 2018;10(11):3229-3248, doi:10.18632/aging.101627"),
 ("Tamarix gallica ameliorates thioacetamide-induced hepatic oxidative stress and hyperproliferative response in Wistar rats", pm(16789436), "J Enzyme Inhib Med Chem 2006;21(2):215-23, doi:10.1080/14756360500480673"),
 ("Evaluation of possible mechanisms of protective role of Tamarix gallica against DEN initiated and 2-AAF promoted hepatocarcinogenesis in male Wistar rats", pm(16698044), "Life Sci 2006;79(15):1456-65, doi:10.1016/j.lfs.2006.04.009"),
 ("The Role of Tamarix gallica Leaves Extract in Liver Injury Induced by Rifampicin Plus Isoniazid in Sprague Dawley Rats", pm(28459346), "J Diet Suppl 2018;15(1):24-33, doi:10.1080/19390211.2017.1310783"),
 ("Amelioration of hyperglycaemia and modulation of pro-inflammatory cytokines by Tamarix gallica fractions in alloxan induced diabetic rats", pm(32654519), "Arch Physiol Biochem 2022;128(6):1666-1675, doi:10.1080/13813455.2020.1788099"),
 ("In vitro comparative evaluation of Tamarix gallica extracts for antioxidant and antidiabetic activity", "https://pmc.ncbi.nlm.nih.gov/articles/PMC10107396/", "Exp Biol Med 2023;248(3):253-262, doi:10.1177/15353702221139208"),
 ("The Cosmetic Potential of The Medicinal Halophyte Tamarix Gallica L. Growing in The Eastern Part of Algeria: Photoprotective and Antioxidant Activities", pm(33280589), "Comb Chem High Throughput Screen 2021;24(10):1671-1678, doi:10.2174/1386207323666201204141541"),
 ("Tamarix gallica phenolics protect IEC-6 cells against H2O2 induced stress by restricting oxidative injuries and MAPKs signaling pathways", pm(28249251), "Biomed Pharmacother 2017;89:490-498, doi:10.1016/j.biopha.2017.02.047"),
 ("The efficacy of Liv-52 on liver cirrhotic patients: a randomized, double-blind, placebo-controlled first approach", pm(16194047), "Phytomedicine 2005;12(9):619-24, doi:10.1016/j.phymed.2004.10.003"),
 ("Notes about the uses of plants by one of the last healers in the Basilicata region (South Italy)", "https://pmc.ncbi.nlm.nih.gov/articles/PMC3484037/", "J Ethnobiol Ethnomed 2012;8:15, doi:10.1186/1746-4269-8-15"),
 ("The Bioactive Value of Tamarix gallica Honey from Different Geographical Origins", "https://pmc.ncbi.nlm.nih.gov/articles/PMC10144098/", "Insects 2023;14(4):319, doi:10.3390/insects14040319"),
 ("Hybrid Tamarix widespread in U.S. invasion and undetected in native Asian range", "https://pmc.ncbi.nlm.nih.gov/articles/PMC123243/", "PNAS 2002;99(17):11256-9, doi:10.1073/pnas.132403299"),
 ("Seventeen new microsatellites for Tamarix gallica and cross-amplification in Tamarix species", "https://pmc.ncbi.nlm.nih.gov/articles/PMC6976893/", "Appl Plant Sci 2020;8(1):e11317, doi:10.1002/aps3.11317"),
 ("Development of a novel set of EST-SSR markers and cross-species amplification in Tamarix africana (Tamaricaceae)", pm(21622457), "Am J Bot 2010;97(6):e45-7, doi:10.3732/ajb.1000112"),
 ("European Tamaricaceae in bioengineering on dry soils", pm(25896819), "Environ Manage 2015, doi:10.1007/s00267-015-0499-8"),
 ("Growth, chlorophyll fluorescence and mineral nutrition in the halophyte Tamarix gallica cultivated in combined stress conditions: Arsenic and NaCl", pm(26093232), "J Photochem Photobiol B 2015, doi:10.1016/j.jphotobiol.2015.06.003"),
 ("Arsenic- and mercury-induced phytotoxicity in the Mediterranean shrubs Pistacia lentiscus and Tamarix gallica grown in hydroponic culture", pm(19477520), "Ecotoxicol Environ Saf 2009;72(6):1781-9, doi:10.1016/j.ecoenv.2009.04.022"),
 ("Nitrogen and phosphorus uptake and biomass production in four riparian plants grown in subsurface flow constructed wetlands for urban wastewater treatment", pm(33352379), "J Environ Manage 2021, doi:10.1016/j.jenvman.2020.111806"),
 ("Antiprotease activity of selected Slovak medicinal plants", pm(20225660), "Pharmazie 2010;65(2):137-40"),
 ("Inhibition of crystallization of calcium oxalate by the extraction of Tamarix gallica L.", pm(19002446), "Urol Res 2008;36(6):283-7, doi:10.1007/s00240-008-0157-1"),
 ("Using Mediterranean shrubs for the phytoremediation of a soil impacted by pyritic wastes in Southern Spain: a field experiment", pm(21353375), "J Environ Manage 2011;92(6):1584-90, doi:10.1016/j.jenvman.2011.01.022"),
 ("Plant Growth-Promoting Pseudomonas sp. TR47 Ameliorates Pepper Growth and Tolerance to Salt Stress", pm(40184005), "Curr Microbiol 2025, doi:10.1007/s00284-025-04217-x"),
]
sources = [{"n": i+1, "title": t, "url": u, "publisher": p, "accessed": A} for i,(t,u,p) in enumerate(S)]

sections = [
 {"key":"overview","title":"한눈에 보기","body":
 "식약처 「식품원료 목록」에는 Tamarix gallica가 'Manna plant수액'이라는 이름의 식물성 원료로 올라 있으며, 상태는 '사용가능', 사용 가능 부위는 '수액'으로만 정해져 있다[1]. 즉 이 종에서 식품원료로 인정된 것은 가지에서 나오는 수액(만나) 하나이고, 잎·꽃·줄기는 이 목록 행의 범위가 아니다[1]. 같은 속의 English tree수액(Tamarix anglica)과 Tamarisk수액(Tamarix canariensis / Tamarix ramosissima), 다른 속의 Manna tree뿌리(Alhagi mannifera)는 목록에서 별도 행으로 관리되므로 이 종의 자료와 섞어 읽지 않아야 한다[1].\n\n"
 "T. gallica는 지중해 서부의 염분이 있는 습지·하천가에 자라는 위성류과(Tamaricaceae) 나무 또는 관목이며 알제리에서는 'Tarfa'라고 부른다[10]. 잎과 꽃 우림물은 민간에서 설사·염증에 쓰였고 간 질환 치료 전통이 있다고 소개된다[4]. 연구는 거의 모두 잎·꽃·새순(지상부) 추출물의 폴리페놀과 그 항산화·동물 실험에 집중되어 있다[4][6][8][10]. 식품원료로 인정된 수액(만나) 자체의 성분을 이 종에서 정량한 논문은 확인하지 못함."},
 {"key":"history","title":"이용의 역사","body":
 "'만나'는 원래 성경 출애굽기의 음식 이름이며, 19세기 화학자들은 시나이산 지역에서 위성류류 관목 가지에서 떨어지는 단 물질을 그 후보로 분석했다[2]. 당시 기록에 따르면 시나이 만나는 Tamarix mannifera에서 곤충(Coccus manniparus로 기록)이 찌른 자리로 흘러나왔고, 아랍 주민과 수도사들이 이를 모아 꿀처럼 빵과 함께 먹었다[2]. 다만 이 기록의 식물은 T. mannifera이며, 이 이름은 현재 다른 종(T. nilotica)의 이명으로 다루는 자료가 있다는 정도만 웹 검색 요약으로 확인했다[3]. 따라서 성경 만나나 시나이 만나 이야기를 그대로 T. gallica 수액의 이력으로 볼 근거는 확인하지 못함.\n\n"
 "T. gallica 자체의 전통 이용으로는 잎·꽃 우림물을 설사·염증에 쓰고 간을 돕는 약으로 쓴 기록이 소개된다[4]. 인도에서는 'Jhau'라는 이름으로 거담·간 강장·완하·수렴·지사 목적으로 쓰였다고 한다[17]. 이탈리아 남부 바실리카타 지역에서는 'Vruca'라고 부르며 사마귀를 없애는 주술적·약용 식물로 쓴 사례가 보고되었다[21]. 이 종의 수액(만나)을 식품으로 먹은 지역별 기록은 확인하지 못함."},
 {"key":"biology","title":"식물학적 특징","body":
 "Tamarix gallica는 위성류과 위성류속의 나무이며, 지중해 서부의 염습지·계곡·기수 하천 같은 염분이 있는 곳에 숲을 이루는 종으로 소개된다[10]. 비늘 같은 잎에 소금을 내보내는 염선(salt gland)이 있는 염생식물(halophyte)로 분류되며, 염분 스트레스에 견디는 능력 때문에 염생식물 연구 대상이 되어 왔다[5][22]. 200 mM NaCl과 비소를 함께 준 재배 실험에서도 광합성 형광값과 칼륨·칼슘·마그네슘 함량이 유지되어 비소에 내성이 있는 식물로 평가되었다[27].\n\n"
 "꽃은 잎보다 총페놀 함량이 높았고(꽃 135.35 mg GAE/g DW) 항산화 활성도 강했다[4]. 같은 연구진은 종·기관·생육 단계·추출 용매에 따라 폴리페놀 함량과 항산화 활성이 크게 달라진다고 보고했다[5]. 꽃은 꿀벌의 밀원이 되어, 꽃가루 분석으로 이 종의 단일 밀원 꿀(Tamarix gallica honey)이 사우디아라비아·리비아·이집트에서 확인되었다[22]. 위성류속 만나는 곤충이 가지를 찔러 생기는 분비물로 기록되어 있으나[2], T. gallica에서 수액(만나)이 생기는 조건과 양은 확인하지 못함."},
 {"key":"related_species","title":"근연종과 혼동 주의","body":
 "식약처 목록에는 위성류속 원료가 세 행 있다: Manna plant수액(T. gallica), English tree수액(T. anglica), Tamarisk수액(T. canariensis / T. ramosissima)이며 모두 사용 부위가 수액이다[1]. 이름에 '만나'가 들어가는 Manna tree뿌리는 콩과의 Alhagi mannifera이며 부위도 뿌리여서 전혀 다른 원료다[1]. 세 위성류속 수액은 서로 다른 종의 원료이므로 한 종의 자료를 다른 종에 옮겨 쓰면 안 된다[1].\n\n"
 "19세기 분석에서 시나이 만나(T. mannifera)는 수분과 식물 찌꺼기를 뺀 뒤 자당 55, 전화당(과당·포도당) 25, 덱스트린류 20의 비율이었고, 쿠르디스탄 만나는 물에 녹는 부분에서 자당 61, 전화당 16.5, 덱스트린류 22.5였다[2]. 이는 T. gallica 수액의 값이 아니며 다른 종(또는 식물이 분명하지 않은) 시료의 값이다[2]. T. mannifera는 현재 T. nilotica의 이명으로 보는 자료가 있다는 점은 웹 검색 요약으로만 확인했다[3]. 미국에 퍼진 위성류 가운데에는 T. ramosissima·T. chinensis 잡종이 가장 많고 T. gallica가 섞인 잡종도 있어 겉모양만으로 종을 가리기 어렵다[23]."},
 {"key":"cultivation","title":"재배와 생육","body":
 "T. gallica 꺾꽂이 묘는 건조 조건에서도 다시 싹이 잘 터서 현지 시험 건조구의 생존율이 97%였고, 두 번째 생육기에 땅속 바이오매스가 크게 늘어 빠르게 뿌리를 내렸다[26]. 이런 특성 때문에 하천 비탈 보강 같은 생태 공법용 식물로 시험되었다[26]. 도시 하수 3차 처리용 인공습지 실험에서는 버드나무류와 비슷한 중간 수준의 생장·질소·인 흡수를 보였다[29].\n\n"
 "광산 오염 토양 복원 현장 시험에서는 pH 5보다 높은 토양에서 생존이 더 좋았고, 토양에서 수확 부위로 옮겨 가는 미량원소 비율은 낮았다[32]. 이 종의 뿌리 주변에서 분리한 세균(Pseudomonas sp. TR47)은 고추 모종의 염 스트레스 생육을 돕는 것으로 보고되었다[33]. 한국에서 이 종을 재배하거나 수액을 채취한 통계는 확인하지 못함. 세계 생산량·교역 통계도 확인하지 못함."},
 {"key":"processing","title":"채취·가공과 제품","body":
 "식약처 목록이 허용한 이 종의 식품원료 부위는 수액뿐이므로, 잎·꽃·지상부 추출물은 이 목록 행만으로는 식품원료 근거가 되지 않는다[1]. 19세기 기록에서 쿠르디스탄 주민은 만나가 내린 가지를 잘라 햇볕에 2~3일 말린 뒤 털어 가루처럼 모았고 정제 없이 반죽이나 고기에 섞어 먹었다[2]. 시나이 만나는 노란 빛의 진한 시럽 형태로 무게의 약 5분의 1이 물이었다[2]. 다만 이 두 기록은 T. gallica로 확인된 시료가 아니다[2].\n\n"
 "연구용 가공은 대부분 잎·꽃·지상부를 그늘에서 말려 가루로 만든 뒤 메탄올·에탄올·물 등으로 추출하는 방식이다[10][11]. 잎·꽃 추출에서는 70% 메탄올 냉침이 항산화 활성이 높은 추출물을 얻는 데 가장 좋았다[7]. 이 종의 꽃을 밀원으로 한 꿀은 수분 13.2~16.15%, 자당 5% 이하로 꿀 국제 기준 범위 안이었다[22]. 국내에서 이 원료로 만든 제품의 생산실적은 확인하지 못함."},
 {"key":"genetics","title":"유전 정보","body":
 "T. gallica의 유전적 다양성과 집단 구조를 연구하기 위해 마이크로새틀라이트 표지 17개가 개발되었고, 그중 14개가 다형성을 보였다[24]. 이 표지들은 다른 위성류속 19종에도 잘 증폭되어 속 안의 종 구분 연구에 쓸 수 있다고 했다[24]. 다른 위성류속 종의 발현 유전자 서열에서 만든 EST-SSR 표지 13개도 T. gallica에서 증폭되었다[25].\n\n"
 "미국에 침입한 위성류의 핵 유전자(PepC 인트론) 분석에서는 원산지 아시아에서는 떨어져 있던 두 종의 유전형이 섞인 잡종이 가장 흔했고, T. gallica가 관여한 잡종도 일부 확인되었다[23]. 따라서 '위성류 만나'나 '위성류 수액'이라는 이름의 시료를 T. gallica로 단정하려면 종 확인이 필요하다[23][24]. 이 종의 엽록체·핵 전체 유전체 해독 결과는 확인하지 못함."},
 {"key":"safety","title":"안전성과 주의","body":
 "식약처 목록에서 이 원료의 상태는 '사용가능', 조건은 '사용가능부위 : 수액'이며 별도의 섭취량 제한은 적혀 있지 않다[1]. 이 종의 수액(만나)에 대한 공공기관의 알레르기·독성·잔류 정보는 확인하지 못함. 사람을 대상으로 한 연구는 이 종이 여러 약초 가운데 하나로 들어간 복합 제제를 간경변 환자 36명에게 6개월 쓴 무작위 시험 정도이며, 이 결과를 이 종 단독 효과로 볼 수는 없다[20].\n\n"
 "잎·꽃·지상부 추출물에 대해서는 쥐의 간 손상·위궤양·고혈당 모델에서 보호 효과가 보고되었으나 모두 동물 실험이다[11][13][15][16]. 한 논문은 급성 경구 독성 시험에서 체중 kg당 3000 mg까지 비교적 안전했다는 앞선 보고를 인용했으나 원 자료는 확인하지 못함[11]. 이 종은 수경 재배에서 비소·수은을 함께 자란 비교 식물보다 더 많이 축적했으므로, 오염 지역에서 채취한 원료는 중금속 관리가 필요하다[28]."},
]

compounds = [
 {"name":"Tamarixetin","name_ko":"타마릭세틴","class":"O-메틸화 플라보놀","role":"marker","part":"지상부(분리 부위 초록에 없음; 수액 아님)","content_text":"이 종에서 분리(함량 확인하지 못함)","activity_ko":"쥐 소장 α-글루코시데이스 억제에서 낮은 농도의 아카보스와 상승 효과를 보였다(효소 실험)[8]","source":[8,9]},
 {"name":"Rhamnetin","name_ko":"람네틴","class":"O-메틸화 플라보놀","role":"bioactive","part":"지상부(분리 부위 초록에 없음; 수액 아님)","content_text":"이 종에서 분리(함량 확인하지 못함)","activity_ko":"α-글루코시데이스 억제와 아카보스 상승 효과가 보고되었다(효소 실험)[8]","source":[8]},
 {"name":"Rhamnazin","name_ko":"람나진","class":"O-메틸화 플라보놀","role":"bioactive","part":"지상부(분리 부위 초록에 없음; 수액 아님)","content_text":"이 종에서 분리(함량 확인하지 못함)","activity_ko":"아카보스와의 상승 효과가 보고되었다(효소 실험)[8]","source":[8]},
 {"name":"Quercetin 3-O-glucuronide","name_ko":"퀘르세틴-3-O-글루쿠로나이드(QGlcA)","class":"플라보놀 글루쿠로나이드","role":"bioactive","part":"지상부(분리 부위 초록에 없음; 수액 아님)","content_text":"이 종에서 분리(함량 확인하지 못함)","activity_ko":"글루쿠론산이 붙은 플라보노이드가 비당체보다 아밀로이드β·hIAPP 응집을 더 강하게 억제했다(시험관 실험)[9]","source":[8,9]},
 {"name":"Kaempferol 3-O-glucuronide","name_ko":"캠페롤-3-O-글루쿠로나이드(KGlcA)","class":"플라보놀 글루쿠로나이드","role":"bioactive","part":"지상부(분리 부위 초록에 없음; 수액 아님)","content_text":"이 종에서 분리(함량 확인하지 못함)","activity_ko":"C-3 글루쿠론산이 α-글루코시데이스 억제를 높이는 요인으로 제시되었다(효소 실험)[8]","source":[8]},
 {"name":"Isoquercitrin","name_ko":"이소퀘르시트린","class":"플라보놀 배당체","role":"marker","part":"꽃·잎","content_text":"꽃 추출물 RP-HPLC의 주요 페놀 성분[4]; 70% 메탄올 추출물의 주요 페놀 성분[7](수치 초록에 없음)","activity_ko":"꽃 추출물의 강한 항산화 활성과 관련된 주요 페놀로 제시되었다[4]","source":[4,7]},
 {"name":"Syringic acid","name_ko":"시링산","class":"페놀산","role":"marker","part":"꽃","content_text":"꽃 추출물 RP-HPLC의 주요 페놀 성분(수치 초록에 없음)","activity_ko":"꽃 추출물의 항산화·항균 활성과 관련된 주요 성분으로 제시되었다[4]","source":[4]},
 {"name":"Catechin","name_ko":"카테킨","class":"플라반-3-올","role":"bioactive","part":"꽃·잎","content_text":"꽃 추출물[4]과 70% 메탄올 추출물[7]의 주요 페놀 성분(수치 초록에 없음)","activity_ko":"추출물의 항산화·항염 활성과 함께 보고되었다[7]","source":[4,7]},
 {"name":"Isorhamnetin 3-O-glucoside","name_ko":"이소람네틴-3-O-글루코사이드","class":"플라보놀 배당체","role":"bioactive","part":"잎·꽃 등 기관 추출물","content_text":"70% 메탄올 추출물 HPLC의 주요 페놀 성분(수치 초록에 없음)","activity_ko":"항염 활성을 보인 70% 메탄올 추출물의 주요 성분이다[7]","source":[7]},
 {"name":"Hentriacontan-12-ol","name_ko":"헨트리아콘탄-12-올","class":"장쇄 지방족 알코올","role":"bioactive","part":"잎·줄기 메탄올 분획(수액 아님)","content_text":"28.13 mg/g 건물(d.m.) — 동정된 30개 성분 합계 52.51 mg/g d.m. 중 최다","activity_ko":"추출물의 항균 활성과 관련 있을 수 있다고 추정되었다[10]","source":[10]},
 {"name":"beta-Sitosterol","name_ko":"베타-시토스테롤","class":"식물스테롤","role":"bioactive","part":"잎·줄기 메탄올 분획(수액 아님)","content_text":"4.97 mg/g d.m.","activity_ko":"추출물의 콜린에스테레이스 억제와 관련 있을 수 있다고 추정되었다(추정)[10]","source":[10]},
 {"name":"1-Triacontanol","name_ko":"1-트리아콘탄올","class":"장쇄 지방족 알코올","role":"other","part":"잎·줄기 메탄올 분획(수액 아님)","content_text":"3.86 mg/g d.m.","activity_ko":"메탄올 분획의 주요 지방족 알코올 가운데 하나다[10]","source":[10]},
 {"name":"Squalene","name_ko":"스쿠알렌","class":"트리테르펜 탄화수소","role":"bioactive","part":"잎·줄기 메탄올 분획(수액 아님)","content_text":"1.28 mg/g d.m.","activity_ko":"잎 추출물의 항산화 활성에 기여할 수 있는 성분으로 거론되었다(추정)[10]","source":[10]},
 {"name":"Sucrose","name_ko":"자당","class":"이당류","role":"nutrient","part":"수액(만나) — 이 종 시료의 값 아님","content_text":"T. gallica 수액의 함량은 확인하지 못함; 참고로 T. mannifera 시나이 만나는 무수·찌꺼기 제외 기준 자당 55, 전화당 25, 덱스트린류 20(19세기 분석)","activity_ko":"위성류속 만나의 주성분으로 기록된 당이며, 이 종 수액에서 확인한 값은 없다[2]","source":[2]},
]

assays = [
 {"role":"literature","compound":"Hentriacontan-12-ol, beta-sitosterol 등 TMS 유도체 30종","compound_ko":"헨트리아콘탄-12-올·베타-시토스테롤 등","part":"잎·줄기 메탄올(80%) 추출 분획 — 수액 아님","content":"헨트리아콘탄-12-올 28.13 mg/g d.m., 베타-시토스테롤 4.97 mg/g d.m., 1-트리아콘탄올 3.86 mg/g d.m., 동정 성분 합계 52.51 mg/g d.m.",
  "method":"GC-MS(BSTFA 실릴화 유도체화)",
  "conditions":{"instrument":"GC-MS(Shimadzu GCMS-QP2020), SCAN·SIM 모드, 초당 3스캔, SCAN m/z 50–650","column":"Zebron ZB-5 모세관(30 m × 0.25 mm i.d., 막 0.25 µm)","mobile_phase":"운반 기체 헬륨, 일정 유속","gradient":"오븐 100 °C 1분 유지 → 5 °C/분으로 190 °C → 10 °C/분으로 300 °C, 10분 유지","flow":"0.98 mL/min, 분할비 1:50","temp":"주입구 250 °C","detection":"질량분석(EI 스펙트럼을 NIST20 라이브러리·머무름 지수와 비교, AMDIS 디컨볼루션)","injection":"","sample_prep":"건조 추출물 약 5 mg + 내부표준 trans-resveratrol(무수 피리딘) + BSTFA 20 µL, 80 °C에서 3시간 반응, 3반복","standard":"내부표준 trans-resveratrol","linearity":"","lod":"","loq":"","recovery":""},
  "rationale":"이 종의 식품원료 부위(수액)를 정량한 분석법은 확인하지 못해, 같은 종 지상부의 성분을 정량한 전문 공개 논문의 조건을 참고로 옮겼다(부위가 다르므로 수액 지표로 쓰려면 검증 필요)[10]","source":[10],"url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC13305346/","source_kind":"paper"},
 {"role":"literature","compound":"Syringic acid, isoquercitrin, catechin","compound_ko":"시링산·이소퀘르시트린·카테킨","part":"꽃·잎 추출물 — 수액 아님","content":"꽃 총페놀 135.35 mg GAE/g DW; 주요 페놀은 시링산·이소퀘르시트린·카테킨(개별 수치 초록에 없음)",
  "method":"RP-HPLC",
  "conditions":{},
  "rationale":"이 종 꽃의 주요 페놀을 RP-HPLC로 확인한 논문이다; 전문 확인 못함(초록만 확인)이라 조건 칸은 비워 두었다[4]","source":[4],"url":"https://pubmed.ncbi.nlm.nih.gov/19500639/","source_kind":"paper"},
 {"role":"literature","compound":"Catechin, isorhamnetin 3-O-glucoside, isoquercitrin","compound_ko":"카테킨·이소람네틴-3-O-글루코사이드·이소퀘르시트린","part":"잎·꽃·줄기·열매 70% 메탄올 냉침 추출물 — 수액 아님","content":"70% 메탄올 추출물의 주요 페놀(개별 수치 초록에 없음)",
  "method":"HPLC",
  "conditions":{},
  "rationale":"기관·용매·추출법별 페놀 조성을 비교한 논문이다; 전문 확인 못함(초록만 확인)이라 조건 칸은 비워 두었다[7]","source":[7],"url":"https://pubmed.ncbi.nlm.nih.gov/37702291/","source_kind":"paper"},
]

# 추가로 본문에서 쓰는 번호 보강: 6,12,14,18,19,30,31 은 아래 절에 반영
extra = ("\n\n시험관·세포 수준에서는 새순 메탄올 추출물이 총페놀 85 mg GAE/g DW, DPPH IC50 3.3 µg/mL을 보였고 100 µg/mL에서 대장암 세포(Caco-2) 증식을 약 62% 억제했다[6]. "
 "추출물은 쥐 소장 상피세포의 과산화수소 손상을 줄였고[19], 지상부 추출물은 자외선 B 영역에서 SPF 약 36~37을 보였다[18]. "
 "트립신 억제(IC50 1.7 µg/mL)[30], 옥살산칼슘 결정 성장 억제[31] 같은 시험관 결과와 쥐의 기억력 손상·간암 유발 모델 결과[12][14]도 있으나, 모두 사람 효과를 뜻하지는 않는다[6][12].")
for s in sections:
    if s["key"]=="safety":
        s["body"] += extra

d = {"slug":"tamarix-gallica","name_ko":"Manna plant수액","name_en":"Manna plant (sap)","scientific_name":"Tamarix gallica L.",
     "aliases":["Manna plant수액","Tarfa(알제리 지역명)","Jhau(인도 지역명)","Vruca(이탈리아 남부 지역명)"],
     "sections":sections,"compounds":compounds,"markers":[],"nutrients":[],"production":[],"world":[],
     "assays":assays,"gi":[],"orgs":[],"sources":sources}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in sections: print(s["key"], len(s["body"]))
