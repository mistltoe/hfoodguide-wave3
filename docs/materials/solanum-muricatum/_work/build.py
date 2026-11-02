import json
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "dossier.json"
A = "2026-11-02"


def pm(n, title, doi, note):
    return {"n": n, "title": f"{title} ({note})", "url": f"https://doi.org/{doi}", "publisher": "PubMed", "accessed": A}


sources = [
    {"n": 1, "title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 페피노열매(Solanum muricatum Aiton, Pepino) 사용가능·사용가능부위: 열매; 페피노잎·페피노줄기 사용불가; 같은 속 감자·가지·까마중 행 대조 (로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json)",
     "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
    pm(2, "Phenolic Profile and Biological Activities of the Pepino (Solanum muricatum) Fruit and Its Wild Relative S. caripense — Int J Mol Sci 2016;17(3):394", "10.3390/ijms17030394", "PMID 26999114, PMC4813249, 전문 확인"),
    pm(3, "The first de novo transcriptome of pepino (Solanum muricatum): assembly, comprehensive analysis and comparison with the closely related species S. caripense, potato and tomato — BMC Genomics 2016;17:321", "10.1186/s12864-016-2656-8", "PMID 27142449, PMC4855764, 전문 확인"),
    pm(4, "A Review of the Pharmacological Effects of Solanum muricatum Fruit (Pepino Melon) — Foods 2024;13(17):2740", "10.3390/foods13172740", "PMID 39272505, PMC11394486, 전문 확인"),
    pm(5, "Chromosome-level pepino genome provides insights into genome evolution and anthocyanin biosynthesis in Solanaceae — Plant J 2022;110(4):1128-1143", "10.1111/tpj.15728", "PMID 35293644, 초록 확인"),
    pm(6, "De novo assembly of the complete mitochondrial genome of pepino (Solanum muricatum) using PacBio HiFi sequencing — BMC Plant Biol 2024;24:361", "10.1186/s12870-024-04978-w", "PMID 38702620, 초록 확인"),
    pm(7, "Fruit composition diversity in land races and modern pepino (Solanum muricatum) varieties and wild related species — Food Chem 2016;203:49-58", "10.1016/j.foodchem.2016.02.035", "PMID 26948588, 초록 확인"),
    pm(8, "Rootstock selection and grafting systems affect pepino (Solanum muricatum) fruit nutritional quality and plant performance — BMC Plant Biol 2025;26:84", "10.1186/s12870-025-07848-1", "PMID 41387777, PMC12817745, 전문 확인"),
    pm(9, "Analysis of the volatile aroma constituents of parental and hybrid clones of pepino (Solanum muricatum) — J Agric Food Chem 2004;52(18):5663-5669", "10.1021/jf040107w", "PMID 15373407, 초록 확인"),
    pm(10, "Volatile Compound and Gene Expression Analyses Reveal Temporal and Spatial Production of LOX-Derived Volatiles in Pepino (Solanum muricatum Aiton) Fruit and LOX Specificity — J Agric Food Chem 2017;65(29):6049-6057", "10.1021/acs.jafc.7b01569", "PMID 28669186, 초록 확인"),
    pm(11, "Physicochemical Characterization and Immunomodulatory Activity of a Novel Acid Polysaccharide from Solanum muricatum — Polymers 2019;11(12):1972", "10.3390/polym11121972", "PMID 31801192, 초록 확인"),
    pm(12, "Protective effects of an aqueous extract from pepino (Solanum muricatum Ait.) in diabetic mice — J Sci Food Agric 2011;91(8):1517-1522", "10.1002/jsfa.4345", "PMID 21445856, 초록 확인"),
    pm(13, "Assessment of suitable cultivation region for Pepino (Solanum muricatum) under different climatic conditions using the MaxEnt model and adaptability in the Qinghai-Tibet plateau — Heliyon 2023;9(8):e18974", "10.1016/j.heliyon.2023.e18974", "PMID 37636388, 초록 확인"),
    pm(14, "Impact of diverse exogenous hormones on parthenocarpy, yield, and quality of pepino (Solanum muricatum) in the Qinghai-Tibet plateau's natural conditions — Physiol Mol Biol Plants 2024;30(11):1853-1869", "10.1007/s12298-024-01533-7", "PMID 39687703, 초록 확인"),
    pm(15, "Tomato Mosaic Tobamovirus, Causal Agent of a Severe Disease of Pepino (Solanum muricatum) — Plant Dis 1998;82(11):1281", "10.1094/PDIS.1998.82.11.1281B", "PMID 30845421, 초록 확인"),
    pm(16, "Biological and Molecular Properties of Wild potato mosaic virus Isolates from Pepino (Solanum muricatum) — Plant Dis 2019;103(7):1746-1756", "10.1094/PDIS-12-18-2164-RE", "PMID 31082318, 초록 확인"),
    pm(17, "Incidence of pests and viral disease on pepino (Solanum muricatum Ait.) in Kanagawa Prefecture, Japan — Biodivers Data J 2017;(5):e14879", "10.3897/BDJ.5.e14879", "PMID 28947875, 초록 확인"),
    pm(18, "Pepino Mosaic Virus: A Globally Important Tomato Pathogen and a Rising Model in Molecular Virology — Mol Plant Pathol 2026;27(1):e70211", "10.1111/mpp.70211", "PMID 41603498, 초록 확인"),
    pm(19, "Identification of the key metabolites and related genes network modules highly associated with the nutrients and taste components among different Pepino (Solanum muricatum) cultivars — Food Res Int 2023;163:112287", "10.1016/j.foodres.2022.112287", "PMID 36596193, 초록 확인"),
    pm(20, "Pepino (Solanum muricatum) Metabolic Profiles and Soil Nutrient Association Analysis in Three Growing Sites on the Loess Plateau of Northwestern China — Metabolites 2022;12(10):885", "10.3390/metabo12100885", "PMID 36295787, 초록 확인"),
    pm(21, "Superior quality retention of pepino (Solanum muricatum) juice using a novel continuous high-pressure processing technology — Food Chem 2026;508(Pt A):148249", "10.1016/j.foodchem.2026.148249", "PMID 41672012, 초록 확인"),
    pm(22, "Antioxidant activity of ripe and unripe pepino fruit (Solanum muricatum Aiton) — J Food Sci 2012;77(11):C1131-1135", "10.1111/j.1750-3841.2012.02944.x", "PMID 23057510, 초록 확인"),
    pm(23, "Structure characterization and immunomodulatory activity of a new neutral polysaccharide SMP-0b from Solanum muricatum — Int J Biol Macromol 2020;155:853-860", "10.1016/j.ijbiomac.2019.11.071", "PMID 31712159, 초록 확인"),
    pm(24, "Phytotoxicity and cytogenotoxicity of hydroalcoholic extracts from Solanum muricatum Ait. and Solanum betaceum Cav. (Solanaceae) in the plant model Lactuca sativa — Environ Sci Pollut Res Int 2019;26(27):27558-27568", "10.1007/s11356-017-1015-x", "PMID 29508193, 초록 확인"),
    pm(25, "Systematic Investigation of TCP Gene Family: Genome-Wide Identification and Light-Regulated Gene Expression Analysis in Pepino (Solanum muricatum) — Cells 2023;12(7):1015", "10.3390/cells12071015", "PMID 37048089, 초록 확인"),
    pm(26, "Transcriptome-wide and expression analysis of the NAC gene family in pepino (Solanum muricatum) during drought stress — PeerJ 2021;9:e10966", "10.7717/peerj.10966", "PMID 33850643, 초록 확인"),
    pm(27, "Evaluation of the Attractant Effect of Solanum muricatum on Gravid Female Adults of Zeugodacus tau and Screening of Attractant Volatiles — Insects 2023;14(7):591", "10.3390/insects14070591", "PMID 37504598, 초록 확인"),
    pm(28, "Indirect improvement of pepino (Solanum muricatum) productivity via nitrogen fertilizer-mediated microbial and enzymatic stimulation — Front Microbiol 2025;16:1612012", "10.3389/fmicb.2025.1612012", "PMID 40895483, 초록 확인"),
    pm(29, "Metabolomics analysis of quality components metabolism during the growth process of pepino (Solanum muricatum) fruit — Plant Signal Behav 2023;18(1):2283363", "10.1080/15592324.2023.2283363", "PMID 37976083, 초록 확인"),
]

S = []


def sec(key, title, body):
    S.append({"key": key, "title": title, "body": body.strip()})


sec("overview", "한눈에 보기", """
페피노(Solanum muricatum Aiton)는 가지과 가지속의 안데스 원산 초본성 작물로, 즙이 많고 은은하게 단 열매를 얻으려고 재배한다[2, 3]. 식약처 「식품원료 목록」에는 원료명 '페피노열매'(영문명 Pepino)가 '사용가능' 원료로 올라 있고, 사용 조건은 '사용가능부위 : 열매'이다[1]. 같은 목록에서 '페피노잎'과 '페피노줄기'는 '사용불가'로 분류되어 있어 식품 원료로 쓸 수 있는 부위는 열매뿐이다[1]. 이 종을 원재료로 하는 건강기능식품 고시형 원료는 확인하지 못함.

열매는 대개 80–250 g이고 둥근 것부터 긴 것까지 모양이 다양하며, 노란 껍질에 자주색 세로 줄무늬가 들어간다[2]. 수분이 90% 이상이라 시원하고 향이 강하다[2]. 잘 익으면 멜론 같은 맛이 나 후식 과일로 먹고, 덜 익은 것은 오이처럼 샐러드에 쓴다[4]. 과육의 주된 페놀 성분은 클로로겐산 같은 하이드록시신남산 유도체이며, 비타민 C·카로티노이드·칼륨도 들어 있다[2, 4, 7]. 중국에서는 'ginseng fruit'라는 이름으로도 불리며 칭하이·간쑤 같은 고원 지대에서 재배가 늘었다[28, 29].
""")

sec("history", "역사", """
페피노는 콜럼버스 이전 안데스에서 중요한 작물이었으나, 잉카 제국이 쇠퇴한 뒤 점차 잊힌 작물이 되었다[2]. 스페인 사람들이 남미에 온 뒤 생긴 스페인어 이름만 적어도 16가지가 있어, 오이를 뜻하는 'pepino'와 헷갈리는 일이 많다[4]. 영어로는 sweet cucumber, melon pear, pepino melon 등으로 불리고, pepino dulce라고도 한다[2, 4].

최근 수십 년 사이 안데스 지역과 여러 나라에서 원예 생산을 다양하게 할 작물로 다시 관심을 받았고, 뉴질랜드·중국·터키 등에 도입되었다[2, 3]. 'El Camino'는 뉴질랜드에서, 'Puzol'과 'Valencia'는 스페인에서 육성된 품종이다[2]. 스페인 발렌시아에서는 1994년 페피노 밭에서 토마토모자이크바이러스(ToMV)에 의한 심한 병이 처음 관찰되어 이후 경제적 피해를 냈다[15]. 중국에서는 지난 20여 년 동안 고원 지대를 중심으로 재배가 크게 늘었고, 칭하이대학 연구진이 'Qingcanxiang' 등 품종을 육성했다[8, 29]. 일본 가나가와현에서도 상업 재배 체계를 세우려는 시험이 이루어졌다[17]. 국내 도입 시기와 재배 연혁은 확인하지 못함.
""")

sec("biology", "식물학적 특징", """
페피노는 가지속 Basarthrum 절에 속하는 재배종으로, 열매를 얻으려고 영양번식으로 기르는 초본성 작물이다[3]. 염색체는 2n = 2x = 24인 이배체이며, 감자·토마토와 같은 기본 염색체 수(x = 12)를 가진다[3, 5]. 열매는 즙이 많은 장과로, 품종에 따라 무게가 100–400 g이고 모양과 색이 다양하다[3]. 서리가 없는 곳에서는 여러 해 자라지만 대부분 지역에서는 한해살이로 재배하며, 착과와 열매 품질이 온도에 매우 민감하다[4]. 무상 기간이 짧은 고원에서는 수정 없이 열매를 맺게(단위결과) 하려고 생장조절제를 쓰기도 한다[14].

열매가 덜 익었을 때는 과당이 가장 많고, 익으면서 자당이 늘고 과당·포도당은 줄어든다[4]. 향기는 아세테이트 계열 에스터와 프레놀(신선한 과일 향), C6·C9 알데하이드(풋내), 락톤·메시퓨란·β-다마세논(이국적인 향)이 함께 만든다[9]. C9 휘발 성분은 덜 익은 열매에서 많다가 익으면서 줄고, trans-2-헥세날은 껍질에서만 나온다[10]. 열매 향기 성분 가운데 헥실 아세테이트 등은 박과실파리 암컷을 끌어들이는 것으로 보고되었다[27]. 가뭄에 비교적 강한 작물로 알려져 있다[26].
""")

sec("related_species", "이름과 가까운 종", """
페피노와 가장 가까운 야생종은 Solanum caripense로, 페피노와 쉽게 교잡되고 잡종의 임성이 높으며 페피노의 기원에 관여한 종으로 본다[3]. 안데스에서는 S. caripense 등 교잡 가능한 야생 근연종이 페피노 밭 가까이 자라 유전자 흐름의 흔적이 있다[3]. S. caripense 열매는 페피노보다 항산화 활성이 높고, 주된 페놀 성분이 카페오일-시나포일-퀸산이라는 점이 다르다[2].

Basarthrum 절은 감자(Petota 절)·토마토(Lycopersicon 절)와 계통적으로 가까워 두 작물의 3차 유전자원으로 여겨지며, 페피노와 감자·토마토 조상은 약 926만 년 전에 갈라진 것으로 추정되었다[3]. 접목 시험에서는 같은 가지속인 가지·토마토 대목과 잘 맞고 고추속 대목과는 잘 맞지 않았다[8]. 식약처 목록에서 감자(Solanum tuberosum)는 덩이줄기, 가지(Solanum melongena)는 열매가 사용 가능하고, 까마중(Solanum nigrum)은 잎·순·줄기가 '제한적 사용'으로 따로 분류되어 페피노와는 별개의 원료이다[1]. 나무토마토(Solanum betaceum)와 비교한 시험에서 카테킨·플라보노이드는 나무토마토 추출물에서만 검출되었다[24].
""")

sec("cultivation", "재배와 산지", """
페피노는 꺾꽂이 등 영양번식으로만 증식하므로 바이러스 없는 건전한 모본 관리가 중요하다[16]. 페루 해안 계곡에서는 Wild potato mosaic virus 감염이 널리 퍼져 있으며, 이는 페피노를 감염하는 다섯 번째 바이러스로 보고되었다[16]. 스페인에서는 토마토모자이크바이러스 증상이 30 °C 이상에서 심해지고 전정·유인 작업으로 쉽게 옮아, 저항성 품종 개발이 최선의 대책으로 제시되었다[15]. 토마토 시설 재배의 주요 병원체인 페피노모자이크바이러스(PepMV)도 페피노에서 자연 감염이 보고되었다[18].

중국의 주산지는 해발 1000 m 이상인 윈난-구이저우 고원과 황토고원이며, MaxEnt 모델은 해발 1000–2000 m 지역을 주요 적지로 예측했다[13]. 황토고원 세 재배지를 비교한 연구에서는 토양 총질소·유기물·인 함량 차이가 열매 대사물(아미노산·유기산·당·페놀산) 차이와 연관되었다[20]. 간쑤 시설 재배 시험에서는 질소 150–225 kg/ha가 수량과 열매 영양을 함께 맞추는 데 알맞았다[28]. 일본 가나가와현 시험 포장에서는 점박이응애와 목화진딧물이 가장 많은 해충이었다[17]. 가지 대목('Moshi')에 접목한 'Qingcanxiang'은 활착률이 90%를 넘었고 열매 비타민 C가 늘었지만 가용성 고형물은 줄었다[8]. 국내 재배 면적과 생산량 통계는 확인하지 못함.
""")

sec("processing", "가공과 이용", """
페피노는 주로 생과로 먹으며, 잘 익은 것은 후식 과일로, 덜 익은 것은 샐러드 재료로 쓴다[4]. 열풍 건조는 아스코르브산과 페놀 화합물 손실이 크고, 마이크로파 건조가 항산화 성분을 더 잘 보존한다고 정리되었다[4]. 페피노 주스는 저장성이 낮고 열 살균 때 품질이 떨어지는데, 연속식 고압 처리(HPP-500)는 PPO를 90% 넘게, POD를 88% 넘게 불활성화하면서 페놀(4.44 mg GAE/mL)과 플라보노이드를 더 잘 유지했다[21].

과육에서는 면역 조절 활성을 보인 산성 다당류 SMP-3a(평균 분자량 227 kDa)와 중성 다당류 SMP-0b가 분리되었다[11, 23]. 물 추출물을 먹인 당뇨 생쥐에서 혈당과 신장의 산화·염증 지표가 낮아졌다는 동물 실험이 있다[12]. 익은 열매 추출물이 덜 익은 열매보다 대부분의 항산화 시험에서 활성이 높았다[22]. 이런 결과는 세포·동물 실험 수준이며 사람 대상 연구가 부족하다는 지적이 있다[4]. 식약처 「식품 등의 생산실적」에서 페피노를 원료로 한 제품 생산 실적은 확인하지 못함.
""")

sec("genetics", "유전 정보", """
2022년 발표된 염색체 수준 페피노 유전체는 전체 1.20 Gb, 스캐폴드 N50 87.03 Mb이며, 서열의 91.67%가 12개 염색체에 고정되었다[5]. 유전체 절반 이상이 반복 서열이고, 진정쌍떡잎식물 공통의 고대 전장유전체 3배화 외에 가지과에서 한 번 더 일어난 3배화의 흔적이 있다[5]. 페피노와 가지에 병 저항성 유전자(NBS)가 적은 것은 3배화 뒤 유전자가 많이 사라졌기 때문으로 설명되었다[5].

미토콘드리아 유전체는 433,466 bp 원형으로 단백질 유전자 38개, tRNA 19개, rRNA 3개가 있고 RNA 편집 자리 585곳이 확인되었다[6]. 2016년 첫 전사체 연구는 유니진 75,832개와 SSR 1,072개를 얻었고, 열매 줄무늬·안토시아닌·클로로겐산 합성 관련 유전자에서 S. caripense와 가장 큰 차이를 보였다[3]. 이후 TCP 유전자 41개, NAC 유전자 71개 등 유전자군이 분석되었다[25, 26]. 품종 간 대사체·전사체 비교에서는 N-p-쿠마로일 아그마틴과 트립타민이 주요 차이 대사물이었다[19].
""")

sec("safety", "안전성", """
식약처 「식품원료 목록」에서 페피노는 열매만 '사용가능'이고 잎과 줄기는 '사용불가'이다[1]. 가지속 야생 근연종 가운데에는 글리코알칼로이드 등 항영양 성분 때문에 세포독성을 보이는 종이 있지만, 페피노 4품종과 S. caripense 과육 추출물은 원액에서도 대식세포 생존율에 영향을 주지 않았다[2]. 페피노 열매의 솔라닌 등 글리코알칼로이드 함량을 정량한 논문이나 공공기관 자료는 PubMed 검색으로 확인하지 못함.

페피노 연구를 정리한 2024년 검토 논문은 독성·안전성 연구가 부족하므로 체계적인 독성 평가가 필요하다고 했다[4]. 상추 뿌리 생장 시험에서 페피노 수알코올 추출물은 뿌리 생장 50% 억제 농도(2.06 g/L)에서 세포분열을 억제했다[24]. 이 결과는 식물 모델 시험이어서 사람 섭취 안전성과 바로 연결되지는 않는다[24]. 페피노에 대한 식품 알레르기 사례 보고나 식약처 알레르기 표시 대상 여부는 확인하지 못함. 잔류농약 기준 등 페피노에 특화된 공공기관 안전 정보도 확인하지 못함.
""")

compounds = [
    {"name": "Chlorogenic acid", "name_ko": "클로로겐산(5-카페오일퀸산)", "class": "하이드록시신남산(카페오일퀸산)", "role": "marker", "part": "열매 과육",
     "content_text": "현대 품종 El Camino·Puzol·Valencia의 주성분(하이드록시신남산 총량의 59–82%를 차지하는 주된 화합물); 하이드록시신남산 총량 1.11–2.35 mg/g(동결건조 과육 분석)[2]",
     "activity_ko": "유도형 산화질소 합성효소 억제로 알려짐; 과육 추출물은 LPS 자극 대식세포의 NO 생성을 36–67% 억제[2]", "source": [2]},
    {"name": "Neochlorogenic acid", "name_ko": "3-카페오일퀸산(네오클로로겐산)", "class": "하이드록시신남산(카페오일퀸산)", "role": "bioactive", "part": "열매 과육",
     "content_text": "원시 품종 37-A의 주성분; 분석한 모든 계통에서 검출[2]", "activity_ko": "과육 항산화 성분[2]", "source": [2]},
    {"name": "Cryptochlorogenic acid", "name_ko": "4-카페오일퀸산", "class": "하이드록시신남산(카페오일퀸산)", "role": "bioactive", "part": "열매 과육",
     "content_text": "분석한 모든 계통(페피노 4품종·S. caripense)에서 검출(함량 미기재)[2]", "activity_ko": "과육 페놀 성분[2]", "source": [2]},
    {"name": "1,3-Dicaffeoylquinic acid", "name_ko": "다이카페오일퀸산류", "class": "하이드록시신남산", "role": "bioactive", "part": "열매 과육",
     "content_text": "이성질체 4종(머무름 시간 15·18·20·33분) 확인(함량 미기재)[2]", "activity_ko": "과육 페놀 성분[2]", "source": [2]},
    {"name": "Caffeoyl-sinapoyl-quinic acid", "name_ko": "카페오일-시나포일-퀸산", "class": "하이드록시신남산", "role": "bioactive", "part": "열매 과육",
     "content_text": "야생 근연종 S. caripense E-7의 주성분이며, 페피노 37-A에서는 두 번째로 많은 성분[2]", "activity_ko": "페피노와 S. caripense를 구별하는 화학 지표 후보[2]", "source": [2]},
    {"name": "Feruloyl glucose", "name_ko": "페룰로일-헥소스(배당체)", "class": "하이드록시신남산 배당체", "role": "bioactive", "part": "열매 과육",
     "content_text": "Puzol 품종에서 두 번째로 많은 성분; El Camino에서는 페룰로일-다이헥소스가 두 번째[2]", "activity_ko": "과육 페놀 성분[2]", "source": [2]},
    {"name": "Ascorbic acid", "name_ko": "비타민 C(아스코르브산)", "class": "비타민", "role": "nutrient", "part": "열매",
     "content_text": "검토 논문 정리 30–80 mg/100 g[4]; 칭하이 시험 자근 'Qingcanxiang' 2.13 µg/g, 가지 대목 접목 6.31 µg/g(원문 단위 그대로)[8]",
     "activity_ko": "수용성 항산화 비타민; 열풍 건조 때 손실이 큼[4]", "source": [4, 8]},
    {"name": "Sucrose", "name_ko": "자당", "class": "당류", "role": "nutrient", "part": "열매",
     "content_text": "자근 72.86 mg/g, 가지 대목 접목 114.23 mg/g(HPLC, 원문 단위 그대로)[8]; 익을수록 늘어 주된 당이 됨[4]",
     "activity_ko": "단맛의 주 성분; 익을수록 늘어남[4]", "source": [4, 8]},
    {"name": "Fructose", "name_ko": "과당", "class": "당류", "role": "nutrient", "part": "열매",
     "content_text": "자근 270.83 mg/g, 접목 253.63 mg/g(HPLC, 원문 단위 그대로)[8]; 덜 익은 열매에서 가장 많은 당[4]",
     "activity_ko": "단맛 성분[4]", "source": [4, 8]},
    {"name": "beta-Carotene", "name_ko": "베타카로틴", "class": "카로티노이드", "role": "nutrient", "part": "열매",
     "content_text": "15개 재배 계통·6개 야생 계통에서 정량, 계통 간 수 배 차이(초록에 숫자 미기재)[7]; 검토 논문은 15품종 56–166 mg/100 g으로 적었으나 단위 확인 못함[4]",
     "activity_ko": "프로비타민 A, 과육의 노란색[2]", "source": [7, 4, 2]},
    {"name": "Potassium", "name_ko": "칼륨", "class": "무기질", "role": "nutrient", "part": "열매",
     "content_text": "열매 200 g당 99.8–353.8 mg; 같은 양에 인 18.0–51.1 mg, 철 0.2–0.6 mg[4]; 재래종이 현대 품종보다 단백질·인·칼륨·아연이 많음[7]",
     "activity_ko": "인·칼륨·철·구리 권장 섭취량에 의미 있게 기여할 수 있음[7]", "source": [4, 7]},
    {"name": "Quercetin", "name_ko": "퀘르세틴", "class": "플라보놀", "role": "bioactive", "part": "열매 추출물",
     "content_text": "물·에탄올 추출물에서 미리세틴·나린제닌·퀘르세틴·루틴 보고[2]; 반면 HPLC-DAD-MS 분석에서는 과육에서 플라보노이드가 검출되지 않음[2]",
     "activity_ko": "검토 논문이 항당뇨·항염 활성의 후보 성분으로 정리(출처 간 검출 여부가 다름)[4]", "source": [2, 4]},
    {"name": "Galacturonic acid", "name_ko": "산성 다당류 SMP-3a(람노스·아라비노스·갈락토스·갈락투론산)", "class": "펙틴성 다당류", "role": "bioactive", "part": "열매 과육",
     "content_text": "몰비 람노스 1.09 : 아라비노스 2.64 : 갈락토스 1.54 : 갈락투론산 1, 평균 분자량 227 kDa[11]",
     "activity_ko": "RAW264.7 대식세포 증식과 TNF-α·IL-1β·IL-6 분비 촉진(시험관)[11]", "source": [11]},
    {"name": "N-p-Coumaroylagmatine", "name_ko": "N-p-쿠마로일 아그마틴", "class": "하이드록시신남산 아마이드", "role": "bioactive", "part": "열매",
     "content_text": "두 품종 비교에서 주요 차이 대사물(함량 미기재)[19]", "activity_ko": "품종 간 영양·맛 성분 차이와 관련된 대사물[19]", "source": [19]},
    {"name": "Hexyl acetate", "name_ko": "헥실 아세테이트", "class": "에스터(향기 성분)", "role": "bioactive", "part": "열매",
     "content_text": "열매 휘발 성분에서 확인(함량 미기재)[27]; 아세테이트류가 신선한 과일 향을 냄[9]",
     "activity_ko": "박과실파리(Zeugodacus tau) 산란 암컷 유인[27]", "source": [9, 27]},
]

assays = [
    {"role": "literature", "compound": "Chlorogenic acid", "compound_ko": "클로로겐산 등 하이드록시신남산 유도체 24종", "part": "열매 과육(껍질 제거, 동결건조 분말)",
     "content": "하이드록시신남산 총량 1.11 mg/g(37-A)–2.35 mg/g(Valencia); 주성분이 총량의 59–82%[2]",
     "method": "HPLC-DAD-MS/ESI",
     "conditions": {"instrument": "", "column": "Phenomenex Kinetex C18, 5 µm, 100 Å, 150 × 4.6 mm",
                    "mobile_phase": "A: 1% 아세트산 수용액, B: 아세토니트릴",
                    "gradient": "1% B → 15% B(15분) → 30% B(30분) → 30% B 유지(40분) → 95% B(45분) → 95% B 유지(50분) → 1% B(55분) → 1% B(60분)",
                    "flow": "800 µL/min", "temp": "", "detection": "DAD 200–400 nm 스펙트럼, 정량 320 nm(하이드록시신남산)·360 nm(플라보노이드); ESI 질량분석으로 [M − H]⁻ 이온과 MSn 조각으로 동정",
                    "injection": "5 µL",
                    "sample_prep": "동결건조 분말 100 mg + 메탄올:물:포름산(70:29:1) 1.5 mL, 볼텍스 → 초음파 60분 → 4 °C 하룻밤 → 초음파 60분 → 10,000 rpm 10분 원심 → PVDF 필터 여과",
                    "standard": "외부 표준 검량선(표준품 이름 원문에 개별 기재 없음)", "linearity": "", "lod": "", "loq": "", "recovery": ""},
     "rationale": "페피노 과육의 페놀은 모두 하이드록시신남산 유도체였고 클로로겐산 이성질체가 주성분이어서 과육 품질·항산화 지표로 쓸 수 있음; 전문 확인, 기기 모델·칼럼 온도·검출한계·회수율은 원문에 없음[2].",
     "source": [2], "url": "https://doi.org/10.3390/ijms17030394", "source_kind": "paper"},
    {"role": "literature", "compound": "Sucrose", "compound_ko": "자당(과당·포도당 동시 분석)", "part": "열매(과육)",
     "content": "자근 'Qingcanxiang' 자당 72.86·과당 270.83·포도당 153.90 mg/g, 가지 대목 접목 자당 114.23·과당 253.63·포도당 122.62 mg/g(원문 단위 그대로)[8]",
     "method": "HPLC(C18)",
     "conditions": {"instrument": "Agilent 1260 HPLC", "column": "C18, 250 mm × 4.6 mm, 5 µm",
                    "mobile_phase": "아세토니트릴:물 80:20 (v/v)", "gradient": "고정 비율(기울기 기재 없음)",
                    "flow": "1.0 mL/min", "temp": "30 °C", "detection": "", "injection": "10 µL",
                    "sample_prep": "", "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""},
     "rationale": "당 조성(익으면서 자당 위주로 바뀜)은 페피노 단맛과 소비자 선호를 좌우하는 품질 지표임; 전문 확인, 검출기·전처리·검량 정보는 원문에 없음[8].",
     "source": [8], "url": "https://doi.org/10.1186/s12870-025-07848-1", "source_kind": "paper"},
]

d = {
    "slug": "solanum-muricatum",
    "name_ko": "페피노",
    "name_en": "Pepino (pepino dulce, sweet cucumber, melon pear)",
    "scientific_name": "Solanum muricatum Aiton",
    "aliases": ["페피노열매", "페피노멜론", "Pepino", "Pepino dulce", "Pepino melon", "Sweet cucumber", "Melon pear", "Ginseng fruit"],
    "sections": S,
    "compounds": compounds,
    "markers": [],
    "nutrients": [],
    "assays": assays,
    "production": [],
    "world": [],
    "gi": [],
    "orgs": [],
    "sources": sources,
}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
for s in S:
    print(s["key"], len(s["body"]))
