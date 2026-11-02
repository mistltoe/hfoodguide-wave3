import json
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "dossier.json"
ACC = "2026-11-02"
PM = "PubMed 초록 확인(PubMed 도구)"
PMC = "PMC 전문 확인(PubMed 도구로 열람)"

S = [
 (1, "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 파스닙(Pastinaca sativa L.)", "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "식품의약품안전처", "2026-10-13"),
 (2, "Khatua S et al. (2026) Pastinaca sativa L.: Nutritional Composition, Phytochemistry, and Pharmacological Properties Supporting Its Potential as a Functional Food and Therapeutic Agent. Food Sci Nutr 14(5):e71860. doi:10.1002/fsn3.71860", "https://pmc.ncbi.nlm.nih.gov/articles/PMC13150342/", "Wiley (" + PMC + ")", ACC),
 (3, "Park JE et al. (2025) Preventive role of Pastinaca sativa in mitigating metabolic dysfunction-associated steatotic liver disease via modulation of metabolic endotoxemia. NPJ Sci Food 9:20. doi:10.1038/s41538-024-00366-8", "https://pmc.ncbi.nlm.nih.gov/articles/PMC11803109/", "Springer Nature (" + PMC + ")", ACC),
 (4, "Lee K et al. (2024) Post-harvest processed parsnip showed improved anti-oxidative capacity and protective potential against acrolein-induced inflammation in vitro and in vivo. Front Nutr 11:1507886. doi:10.3389/fnut.2024.1507886", "https://pmc.ncbi.nlm.nih.gov/articles/PMC11614627/", "Frontiers (" + PMC + ")", ACC),
 (5, "Ivie GW, Holt DL, Ivey MC (1981) Natural toxicants in human foods: psoralens in raw and cooked parsnip root. Science 213:909-910. doi:10.1126/science.7256284", "https://pubmed.ncbi.nlm.nih.gov/7256284/", "Science (" + PM + ")", ACC),
 (6, "Ostertag E et al. (2002) Effects of storage conditions on furocoumarin levels in intact, chopped, or homogenized parsnips. J Agric Food Chem 50:2565-2570. doi:10.1021/jf011426f", "https://pubmed.ncbi.nlm.nih.gov/11958623/", "American Chemical Society (" + PM + ")", ACC),
 (7, "Stegelmeier BL et al. (2019) Wild parsnip (Pastinaca sativa)-induced photosensitization. Toxicon 167:60-66. doi:10.1016/j.toxicon.2019.06.007", "https://pubmed.ncbi.nlm.nih.gov/31173794/", "Elsevier (" + PM + ")", ACC),
 (8, "Kviesis J et al. (2019) Evaluation of furanocoumarins from seeds of the wild parsnip (Pastinaca sativa L. s.l.). J Chromatogr B 1105:54-66. doi:10.1016/j.jchromb.2018.12.012", "https://pubmed.ncbi.nlm.nih.gov/30562630/", "Elsevier (" + PM + ")", ACC),
 (9, "Ekiert H, Gomółka E (2000) Furanocoumarins in Pastinaca sativa L. in vitro culture. Pharmazie 55:618-620", "https://pubmed.ncbi.nlm.nih.gov/10989843/", "Die Pharmazie (" + PM + ")", ACC),
 (10, "DFG Senate Commission on Food Safety (SKLM) (2007) Toxicological assessment of furocoumarins in foodstuffs. Mol Nutr Food Res 51:367-373. doi:10.1002/mnfr.200600270", "https://pubmed.ncbi.nlm.nih.gov/17340579/", "독일연구재단(DFG) 식품안전 상원위원회(SKLM) — Wiley (PubMed 서지 확인, 초록 없음)", ACC),
 (11, "Guth S et al. (2011) Update of the toxicological assessment of furanocoumarins in foodstuffs — Opinion of the SKLM of the DFG. Mol Nutr Food Res 55:807-810. doi:10.1002/mnfr.201100011", "https://pubmed.ncbi.nlm.nih.gov/21433281/", "독일연구재단(DFG) SKLM — Wiley (" + PM + ")", ACC),
 (12, "Walling AL, Walling HW (2018) Phytophotodermatitis induced by wild parsnip. Dermatol Online J 24(2)", "https://pubmed.ncbi.nlm.nih.gov/29630166/", "Dermatology Online Journal (" + PM + ")", ACC),
 (13, "Lafon A, Boulard C (2020) Perioral phytophotodermatitis induced by parsnip mash. Contact Dermatitis 83:318-319. doi:10.1111/cod.13594", "https://pubmed.ncbi.nlm.nih.gov/32383195/", "Wiley (PubMed 서지·주제어 확인, 초록 없음)", ACC),
 (14, "Chene L et al. (2023) Parsnips and Phytophotodermatitis. J Pediatr 264:113727. doi:10.1016/j.jpeds.2023.113727", "https://pubmed.ncbi.nlm.nih.gov/37696389/", "Elsevier (PubMed 서지 확인, 초록 없음)", ACC),
 (15, "Grosu Dumitrescu C et al. (2024) New Insights Concerning Phytophotodermatitis Induced by Phototoxic Plants. Life 14(8):1019. doi:10.3390/life14081019", "https://pubmed.ncbi.nlm.nih.gov/39202761/", "MDPI (" + PM + ")", ACC),
 (16, "Paulsen E et al. (2014) Systemic allergic dermatitis caused by Apiaceae root vegetables. Contact Dermatitis 70:98-103. doi:10.1111/cod.12122", "https://pubmed.ncbi.nlm.nih.gov/24102077/", "Wiley (" + PM + ")", ACC),
 (17, "Zidorn C et al. (2005) Polyacetylenes from the Apiaceae vegetables carrot, celery, fennel, parsley, and parsnip and their cytotoxic activities. J Agric Food Chem 53:2518-2523. doi:10.1021/jf048041s", "https://pubmed.ncbi.nlm.nih.gov/15796588/", "American Chemical Society (" + PM + ")", ACC),
 (18, "Corell M et al. (2013) Absolute configuration of falcarinol (9Z-heptadeca-1,9-diene-4,6-diyn-3-ol) from Pastinaca sativa. Nat Prod Commun 8:1123-1126", "https://pubmed.ncbi.nlm.nih.gov/24079184/", "Natural Product Communications (" + PM + ")", ACC),
 (19, "Kramer M et al. (2011) Quantification of polyacetylenes in apiaceous plants by HPLC coupled with diode array detection. Z Naturforsch C 66:319-327. doi:10.1515/znc-2011-7-801", "https://pubmed.ncbi.nlm.nih.gov/21950154/", "De Gruyter (" + PM + ")", ACC),
 (20, "Rawson A et al. (2010) Influence of sous vide and water immersion processing on polyacetylene content and instrumental color of parsnip (Pastinaca sativa) disks. J Agric Food Chem 58:7740-7747. doi:10.1021/jf100517p", "https://pubmed.ncbi.nlm.nih.gov/20521838/", "American Chemical Society (" + PM + ")", ACC),
 (21, "Koidis A et al. (2012) Influence of unit operations on the levels of polyacetylenes in minimally processed carrots and parsnips: an industrial trial. Food Chem 132:1406-1412. doi:10.1016/j.foodchem.2011.11.128", "https://pubmed.ncbi.nlm.nih.gov/29243629/", "Elsevier (" + PM + ")", ACC),
 (22, "Christensen LP (2011) Aliphatic C17-polyacetylenes of the falcarinol type as potential health promoting compounds in food plants of the Apiaceae family. Recent Pat Food Nutr Agric 3:64-77. doi:10.2174/2212798411103010064", "https://pubmed.ncbi.nlm.nih.gov/21114468/", "Bentham Science (" + PM + ")", ACC),
 (23, "Wang YH et al. (2026) Chromosomal-scale genome assembly of parsnip (Pastinaca sativa) reveals genome evolution and carotenoid regulation. Plant Physiol 200(2). doi:10.1093/plphys/kiag009", "https://pubmed.ncbi.nlm.nih.gov/41559852/", "Oxford University Press (" + PM + ")", ACC),
 (24, "Roselli S et al. (2017) A bacterial artificial chromosome (BAC) genomic approach reveals partial clustering of the furanocoumarin pathway genes in parsnip. Plant J 89:1119-1132. doi:10.1111/tpj.13450", "https://pubmed.ncbi.nlm.nih.gov/27943460/", "Wiley (" + PM + ")", ACC),
 (25, "Berenbaum MR, Zangerl AR (1998) Chemical phenotype matching between a plant and its insect herbivore. PNAS 95:13743-13748. doi:10.1073/pnas.95.23.13743", "https://pubmed.ncbi.nlm.nih.gov/9811871/", "National Academy of Sciences (" + PM + ")", ACC),
 (26, "Zangerl AR, Stanley MC, Berenbaum MR (2008) Selection for chemical trait remixing in an invasive weed after reassociation with a coevolved specialist. PNAS 105:4547-4552. doi:10.1073/pnas.0710280105", "https://pubmed.ncbi.nlm.nih.gov/18238901/", "National Academy of Sciences (" + PM + ")", ACC),
 (27, "Berenbaum MR, Zangerl AR (2006) Parsnip webworms and host plants at home and abroad: trophic complexity in a geographic mosaic. Ecology 87:3070-3081", "https://pubmed.ncbi.nlm.nih.gov/17249232/", "Ecological Society of America (" + PM + ")", ACC),
 (28, "Zangerl AR, Berenbaum MR (2003) Phenotype matching in wild parsnip and parsnip webworms: causes and consequences. Evolution 57:806-815", "https://pubmed.ncbi.nlm.nih.gov/12778550/", "Society for the Study of Evolution (" + PM + ")", ACC),
 (29, "Chappell LHK, Barker GC, Clarkson JP (2024) Characterisation of Itersonilia spp. from Parsnip and Other Hosts. J Fungi 10(12):873. doi:10.3390/jof10120873", "https://pubmed.ncbi.nlm.nih.gov/39728369/", "MDPI (" + PM + ")", ACC),
 (30, "Turesson H et al. (2014) Starch biosynthetic genes and enzymes are expressed and active in the absence of starch accumulation in sugar beet tap-root. BMC Plant Biol 14:104. doi:10.1186/1471-2229-14-104", "https://pubmed.ncbi.nlm.nih.gov/24758347/", "BioMed Central (" + PM + ")", ACC),
 (31, "Uecker S, Jira T, Beyrich T (1991) The production of furocoumarin in Apium graveolens L. and Pastinaca sativa L. after infection with Sclerotinia sclerotiorum. Pharmazie 46:599-601", "https://pubmed.ncbi.nlm.nih.gov/1798717/", "Die Pharmazie (PubMed 영문 초록 확인)", ACC),
 (32, "Golubkina N et al. (2020) High Temperature and Humidity Effect on Biochemical Characteristics of Organically-Grown Parsnip Roots Compared to Garlic Bulbs. Plant Foods Hum Nutr 75:292-297. doi:10.1007/s11130-019-00775-1", "https://pubmed.ncbi.nlm.nih.gov/32350812/", "Springer (" + PM + ")", ACC),
 (33, "EFSA (2018) Modification of the existing maximum residue levels for flonicamid in various root crops. EFSA J 16(9):e05414. doi:10.2903/j.efsa.2018.5414", "https://pubmed.ncbi.nlm.nih.gov/32626048/", "유럽식품안전청(EFSA) (" + PM + ")", ACC),
 (34, "Morris AJ, Rueckeis CA (2023) Sap and Sun: A Case of Phytophotodermatitis. Wilderness Environ Med 34:532-535. doi:10.1016/j.wem.2023.06.003", "https://pubmed.ncbi.nlm.nih.gov/37802751/", "Elsevier (" + PM + ")", ACC),
]
sources = [{"n": n, "title": t, "url": u, "publisher": p, "accessed": a} for n, t, u, p, a in S]

sections = [
 {"key": "overview", "title": "한눈에 보기", "body":
  "파스닙(Pastinaca sativa L.)은 미나리과(산형과)의 두해살이풀로, 당근처럼 생긴 흰색~연노란색 곧은뿌리를 채소로 먹는다[2]. 식약처 「식품원료 목록」에는 파스닙뿌리·파스닙잎·파스닙농축액·파스닙퓌레가 올라 있고, 사용 가능 부위는 뿌리와 잎이며 상태는 '사용가능'이다[1]. 같은 목록은 '설탕당근', '아메리카 방풍나물'을 다른 이름으로 적고 있다[1].\n\n"
  "뿌리는 날것 100 g에 탄수화물 18 g, 식이섬유 4.9 g, 칼륨 375 mg, 비타민 C 17 mg, 엽산 67 µg으로 당근보다 탄수화물·섬유가 많다[2]. 기능 성분으로는 팔카리놀·팔카린디올 같은 폴리아세틸렌과 잔토톡신·베르갑텐 같은 푸로쿠마린이 알려져 있다[3][17]. 푸로쿠마린은 빛을 받으면 피부에 화상 같은 광독성 피부염을 일으키므로, 야생 파스닙의 즙이나 잘못 보관한 뿌리는 주의해야 한다[6][12][15]. 국내 생산 통계는 확인하지 못함."},
 {"key": "history", "title": "역사", "body":
  "파스닙은 코카서스 지역을 기원지로 보는 견해가 있고, 로마 시대부터 두툼한 뿌리를 얻으려고 재배했다[2]. 정제 설탕이 보급되기 전 유럽에서는 단맛 때문에 널리 사랑받았고, 지금도 영국·아일랜드에서는 크리스마스 만찬과 일요일 구이 요리에 빠지지 않는다[2]. 영국과 아일랜드에는 뿌리를 홉과 함께 끓여 발효한 맥주나 와인을 만드는 전통도 있다[2].\n\n"
  "속명 Pastinaca는 라틴어 pastinum(땅을 갈다) 또는 pastus(먹을거리)에서 왔다고 설명된다[2]. 세르비아·이탈리아 민간에서는 뿌리·잎 우린 물을 소화·이뇨용으로, 이란 전통의학에서는 위장·간 강장제로 썼다[2]. 북아메리카에는 뿌리채소로 들어왔다가 지금은 초원과 길가에 퍼진 침입 잡초가 되었다[12]. 1981년에는 익혀도 분해되지 않는 파스닙 뿌리의 소랄렌류가 '식품 속 천연 독성물질'로 보고되었다[5]. 국내에서는 경북 예천 지역 시장에서 산 파스닙 뿌리로 연구한 예가 있다[3]."},
 {"key": "biology", "title": "식물학적 특징", "body":
  "파스닙은 보통 두해살이지만 한 번 꽃 피고 죽는 여러해살이처럼 자라기도 하며, 키는 0.3–1 m이고 길고 굵은 곧은뿌리를 깊이 내린다[2]. 잎은 어긋나는 깃꼴겹잎으로 길이 약 15 cm이고, 작은잎 5–15장은 길이 5–10 cm이다[2]. 꽃은 지름 10–20 cm의 납작한 겹산형꽃차례에 노랗게 피고, 꽃자루살은 6–25개다[2].\n\n"
  "꽃은 수술이 먼저 성숙하고 암술이 나중에 성숙하는 웅예선숙이며, 열매는 길이 5–7 mm의 털 없는 분열과다[2]. 알칼리성의 습한 흙을 좋아하지만 척박한 땅에서도 산다[2]. 곧은뿌리의 주된 저장물질은 녹말이며 당도 상당히 들어 있다[30]. 잎이 상처를 입거나 곤충에게 먹히면 그 작은잎에서 푸로쿠마린 생성이 최대 세 배까지 늘어난다[2]. 줄기와 잎에 든 푸로쿠마린은 자외선을 받아 활성산소를 만들어 피부 조직을 손상시킨다[12]."},
 {"key": "related_species", "title": "가까운 종", "body":
  "세계식물목록(WFO) 기준 Pastinaca 속에는 16종이 있고, 파스닙 안에서도 아종이 구분된다[2]. 파스닙은 당근·셀러리·회향·파슬리와 같은 미나리과 채소로, 이들 모두에 팔카리놀형 폴리아세틸렌이 들어 있다[17][22]. 당근·셀러리악·파스닙 세 뿌리채소에 함께 접촉 감작된 사례도 보고되었다[16].\n\n"
  "같은 과의 어수리속(Heracleum) 식물은 파스닙과 같은 곤충을 공유하며 생태적으로 얽혀 있다[27][28]. 유럽에서 파스닙굴나방(Depressaria pastinacella)은 파스닙이 있어도 푸로쿠마린이 적은 Heracleum sphondylium을 더 자주 먹었다[27]. 미국 중서부에서는 Heracleum lanatum 근처에서 자란 파스닙의 화학형이 두 종의 중간이었다[28]. 북미의 Heracleum maximum도 파스닙처럼 즙과 햇빛으로 광독성 피부염을 일으킨다[34]. 셀러리 뿌리도 균에 감염되면 파스닙처럼 푸로쿠마린이 늘어난다[31]."},
 {"key": "cultivation", "title": "재배와 생산", "body":
  "파스닙은 북반구에서 두해살이 작물로 널리 재배되며, 뿌리의 크기·균일성·상품 수량은 파종 시기, 심는 간격, 밭 관리에 좌우된다[2]. 온대 유럽에서 서아시아·코카서스·히말라야 서부까지 퍼져 있고 중국·일본·북미 등에 귀화했다[2].\n\n"
  "영국에서 파스닙은 연간 경제적 가치가 최소 3,100만 파운드인 특화 작물이며, 가장 큰 제약은 Itersonilia 균 등에 의한 뿌리 궤양병(canker)이다[29]. 이 균은 0–25 °C에서 자라고 파스닙의 뿌리와 잎을 모두 감염시켰다[29]. 균핵병균(Sclerotinia sclerotiorum)에 감염된 뿌리는 감염 초기에 푸로쿠마린이 늘었다[31]. 북미와 뉴질랜드에서는 꽃을 먹는 파스닙굴나방이 종자 생산을 최대 75%까지 줄였다[26].\n\n"
  "국내 재배 면적·생산량 통계(통계청·농식품부)는 확인하지 못함. 세계 생산량(FAOSTAT)은 파스닙만 따로 집계한 값을 확인하지 못함."},
 {"key": "processing", "title": "가공과 이용", "body":
  "뿌리는 날로 먹거나 삶기·굽기·찌기·튀기기로 조리하고, 퓌레·잼·수프·스튜·케이크·푸딩에 넣거나 말려 양념으로 쓴다[2]. 잎과 어린 순도 다른 채소와 함께 익혀 수프에 넣으며, 이유식 재료로도 쓰인다[2]. 독일 시판 파스닙 이유식의 푸로쿠마린은 0.41 mg/kg 이하였다[6].\n\n"
  "껍질 벗기기는 폴리아세틸렌 손실이 가장 큰 공정이었고, 이는 껍질에 폴리아세틸렌이 많기 때문이다[21]. 데치기(95 °C)로 팔카리놀은 24.5%, 팔카린디올은 24% 줄었다[20]. 반면 뿌리 소랄렌류는 끓이거나 전자레인지로 익혀도 분해되지 않았다[5].\n\n"
  "60 °C에서 30일 숙성한 파스닙 추출물은 총페놀이 9.96배 늘었고, 팔카린디올은 0.005 mg/g에서 0.141 mg/g으로 늘었으며 잔토톡신(8-MOP)은 0.183 mg/g에서 0.070 mg/g으로 줄었다[4]. 고온·고습 처리한 '흑파스닙'은 단당류가 건조중량 100 g당 6.5–8.0 g에서 36.2–42.5 g으로 늘었다[32]. 국내 연구진은 뿌리 열수 추출물(수율 약 38.5%)을 잔토톡신·베르갑텐으로 표준화했다[3]."},
 {"key": "genetics", "title": "유전체와 육종", "body":
  "2026년 파스닙 첫 염색체 수준 유전체가 발표되었는데, 크기 1.52 Gb, 염색체 11개, 스캐폴드 N50 135.6 Mb, 단백질 암호화 유전자 51,156개다[23]. 유전체의 90.63%가 반복서열이고 전이인자가 84.07%이며, LTR 전이인자(Copia의 SIRE, Gypsy의 Tekay)가 끼어들며 유전체가 커졌다[23]. 뿌리가 흰 까닭은 카로티노이드 합성 흐름이 부족하고 분해효소(CCD) 유전자가 라이코펜·β-카로틴 축적을 막기 때문으로 해석되었다[23].\n\n"
  "푸로쿠마린 합성 유전자 CYP71AJ3·CYP71AJ4는 한 BAC 클론에 붙어 있고, PsPT1과 움벨리페론을 만드는 PsDIOX는 다른 염색체에서 또 하나의 유전자 묶음을 이룬다[24]. 야생 파스닙의 푸로쿠마린 생산량에는 유전되는 연속 변이가 있고, 표본관 표본과 비교하면 스폰딘 함량은 굴나방과의 상호작용으로 높아진 것으로 보인다[25]. 재배 파스닙은 야생형보다 문제의 푸로쿠마린이 적다[2]."},
 {"key": "safety", "title": "안전성", "body":
  "파스닙의 푸로쿠마린(소랄렌류)은 자외선 에너지를 흡수해 DNA와 결합하고 활성산소를 만들어 독성을 낸다[2]. 즙이 묻은 피부가 햇빛을 받으면 붉어지고 물집이 생긴 뒤 색소침착이 남는 광독성 피부염이 생긴다[12][15]. 파스닙 퓌레를 먹은 영아의 입 주위 피부염과 어린이 사례도 보고되었다[13][14]. 말·염소 실험에서 야생 파스닙 즙을 피부에 바르면 심한 광피부염이 생겼지만, 먹인 염소의 혈청에서는 잔토톡신이 검출되지 않았다[7]. 예방은 긴 옷·장갑 착용과 접촉 후 즉시 비누로 씻기다[15][34].\n\n"
  "갓 캔 뿌리의 푸로쿠마린 5종 합계는 대개 2.5 mg/kg 미만이었으나, 통째로 4 °C에 두면 약 40 mg/kg까지, 상온에서 곰팡이가 피면 566 mg/kg까지 늘어 수확 뒤 −18 °C 보관이 권고되었다[6]. 뿌리 소랄렌류 약 40 ppm은 조리로 줄지 않는다[5]. 독일 식품안전위원회(SKLM)는 식품 중 푸로쿠마린을 평가했다[10][11]. 셀러리악·파스닙·당근 접촉 알레르기 사례도 있다[16]. EFSA는 파스닙 등 뿌리채소의 플로니카미드 잔류 섭취 위험이 낮다고 결론냈다[33]. 국내 공공기관의 파스닙 안전 정보는 확인하지 못함."},
]

compounds = [
 {"name": "Xanthotoxin", "name_ko": "잔토톡신(메톡살렌, 8-MOP)", "class": "선형 푸로쿠마린", "role": "marker", "part": "뿌리",
  "content_text": "뿌리 열수 추출물 0.19 mg/g(건조중량)[3]; 생 파스닙 30% 에탄올 추출물 0.183 ± 0.016 mg/g, 60 °C 숙성 후 0.070 ± 0.001 mg/g[4]",
  "activity_ko": "광독성 피부염의 주원인 푸로쿠마린 중 하나이며, 국내 연구에서 추출물 표준화 지표로 쓰였다[3][7]", "source": [3, 4, 7]},
 {"name": "Bergapten", "name_ko": "베르갑텐(5-메톡시소랄렌)", "class": "선형 푸로쿠마린", "role": "marker", "part": "뿌리·종자",
  "content_text": "뿌리 열수 추출물 0.12 mg/g(건조중량)[3]; 미숙 종자 푸로쿠마린 중 40.8%로 가장 많음[8]",
  "activity_ko": "잔토톡신과 함께 추출물 표준화 지표 성분[3]; 광독성 푸로쿠마린[7]", "source": [3, 7, 8]},
 {"name": "Psoralen", "name_ko": "소랄렌", "class": "선형 푸로쿠마린", "role": "bioactive", "part": "잎·줄기·뿌리",
  "content_text": "잎 48.9, 줄기 10.6, 뿌리 14.9 mg/100 g(건조중량)[9]",
  "activity_ko": "광독성·광돌연변이성을 지닌 소랄렌류의 기본 골격[5][6]", "source": [5, 6, 9]},
 {"name": "Isopimpinellin", "name_ko": "이소핌피넬린", "class": "선형 푸로쿠마린", "role": "bioactive", "part": "뿌리·종자",
  "content_text": "캘러스 배양에서 최대 238.9 mg/100 g(건조중량)으로 가장 많음[9]; 미숙 종자 푸로쿠마린 중 4.3%[8]",
  "activity_ko": "저장 중 뿌리에서 측정된 푸로쿠마린 5종 중 하나[6]", "source": [6, 8, 9]},
 {"name": "Imperatorin", "name_ko": "임페라토린", "class": "프레닐화 푸로쿠마린", "role": "bioactive", "part": "열매",
  "content_text": "열매 200.0 mg/100 g(건조중량)으로 열매의 주성분[9]; 미숙 종자 푸로쿠마린 중 3.2%[8]",
  "activity_ko": "야생 파스닙에서 HPLC-MS로 확인된 푸로쿠마린 5종 중 하나[7]", "source": [7, 8, 9]},
 {"name": "Angelicin", "name_ko": "안젤리신(이소소랄렌)", "class": "각형 푸로쿠마린", "role": "bioactive", "part": "뿌리",
  "content_text": "갓 수확한 뿌리의 푸로쿠마린 5종(안젤리신 포함) 합계 대개 2.5 mg/kg 미만[6]",
  "activity_ko": "저장·곰팡이 감염 시 함께 늘어나는 푸로쿠마린 지표 중 하나[6]", "source": [6]},
 {"name": "Sphondin", "name_ko": "스폰딘", "class": "각형 푸로쿠마린", "role": "bioactive", "part": "열매·식물체",
  "content_text": "",
  "activity_ko": "파스닙굴나방과의 공진화로 함량이 높아진 것으로 해석된 방어 성분[25]", "source": [25]},
 {"name": "Falcarinol", "name_ko": "팔카리놀", "class": "C17 폴리아세틸렌", "role": "bioactive", "part": "뿌리",
  "content_text": "데치기(95 °C)로 24.5% 감소[20]",
  "activity_ko": "파스닙의 팔카리놀은 3R 절대배치[18]; 백혈병 세포주 CEM-C7H2에 IC50 3.5 µmol/L로 가장 강한 세포독성[17]", "source": [17, 18, 20]},
 {"name": "Falcarindiol", "name_ko": "팔카린디올", "class": "C17 폴리아세틸렌", "role": "marker", "part": "뿌리",
  "content_text": "생 파스닙 추출물 0.005 mg/g, 60 °C 숙성 추출물 0.141 mg/g[4]; 데치기로 24% 감소, 물 침지 가공 후 호기 저장 5일에 최대 70% 손실[20]",
  "activity_ko": "숙성 파스닙의 항염 효과를 일부 설명하는 성분으로 정량됨[4]", "source": [4, 20]},
 {"name": "Falcarindiol 3-acetate", "name_ko": "팔카린디올-3-아세테이트", "class": "C17 폴리아세틸렌", "role": "bioactive", "part": "뿌리",
  "content_text": "",
  "activity_ko": "파스닙에서 처음 보고된 폴리아세틸렌[19]; 최소가공 중 껍질 벗기기에서 크게 손실[21]", "source": [19, 21]},
 {"name": "Umbelliferone", "name_ko": "움벨리페론", "class": "쿠마린", "role": "bioactive", "part": "캘러스",
  "content_text": "",
  "activity_ko": "푸로쿠마린 합성의 중간체로, PsDIOX 효소가 p-쿠마로일 CoA에서 만든다[24]; 시험관 배양 조직에서 생성[9]", "source": [9, 24]},
 {"name": "Octyl acetate", "name_ko": "옥틸 아세테이트", "class": "지방산 에스터(정유)", "role": "bioactive", "part": "종자·꽃",
  "content_text": "종자 정유의 주성분[2]",
  "activity_ko": "파스닙굴나방이 길을 찾는 꽃 향기 성분[26]", "source": [2, 26]},
 {"name": "Quercetin", "name_ko": "퀘르세틴", "class": "플라보놀", "role": "bioactive", "part": "뿌리",
  "content_text": "생 뿌리 0.99 mg/100 g(USDA 값, 리뷰 재인용)[2]",
  "activity_ko": "뿌리 페놀 성분 중 하나로 항산화 평가에 쓰임[2]", "source": [2]},
 {"name": "5-Hydroxymethylfurfural", "name_ko": "5-하이드록시메틸푸르푸랄(5-HMF)", "class": "마이야르 반응 산물", "role": "bioactive", "part": "뿌리(가공품)",
  "content_text": "생 파스닙 0.170 mg/g, 60 °C 숙성 2.100 mg/g[4]",
  "activity_ko": "열 가공 지표 성분으로 숙성 파스닙의 항산화력 증가와 관련지어 해석됨[4]", "source": [4]},
 {"name": "Ascorbic acid", "name_ko": "비타민 C(아스코르브산)", "class": "비타민", "role": "nutrient", "part": "뿌리",
  "content_text": "생 뿌리 17 mg/100 g[2]",
  "activity_ko": "유전체 연구에서 PsAPX 유전자 발현이 아스코르브산 함량과 유의하게 상관[23]", "source": [2, 23]},
]

nutrients = [{
 "form": "파스닙 뿌리, 생것(USDA FoodData Central 값을 Khatua 등 2026 리뷰 표 5에서 재인용)", "basis": "100 g",
 "items": [
  {"name": "수분", "value": 79.5, "unit": "g"}, {"name": "에너지", "value": 75, "unit": "kcal"},
  {"name": "단백질", "value": 1.2, "unit": "g"}, {"name": "지질", "value": 0.3, "unit": "g"},
  {"name": "탄수화물", "value": 18, "unit": "g"}, {"name": "식이섬유", "value": 4.9, "unit": "g"},
  {"name": "회분", "value": 0.98, "unit": "g"}, {"name": "칼륨", "value": 375, "unit": "mg"},
  {"name": "인", "value": 71, "unit": "mg"}, {"name": "칼슘", "value": 36, "unit": "mg"},
  {"name": "마그네슘", "value": 29, "unit": "mg"}, {"name": "철", "value": 0.59, "unit": "mg"},
  {"name": "아연", "value": 0.59, "unit": "mg"}, {"name": "망간", "value": 0.56, "unit": "mg"},
  {"name": "비타민 C", "value": 17, "unit": "mg"}, {"name": "나이아신", "value": 0.7, "unit": "mg"},
  {"name": "티아민", "value": 0.09, "unit": "mg"}, {"name": "리보플래빈", "value": 0.05, "unit": "mg"},
  {"name": "엽산", "value": 67, "unit": "µg"}],
 "source": [2]}]

assays = [
 {"role": "literature", "compound": "Xanthotoxin", "compound_ko": "잔토톡신·베르갑텐(동시 정량)", "part": "뿌리 열수 추출물(PRE)",
  "content": "잔토톡신 0.19 mg/g, 베르갑텐 0.12 mg/g(추출물 건조중량)[3]", "method": "HPLC-PDA",
  "conditions": {"instrument": "Waters Alliance 2695 분리 모듈, 1515 4원 펌프, 2996 광다이오드 배열 검출기",
   "column": "Waters XBridge BEH C18, 150 × 4.6 mm, 3.5 µm", "mobile_phase": "A: 0.1% 포름산 수용액, B: 0.1% 포름산 아세토니트릴",
   "gradient": "0–5분 30% B; 5–15분 30→35% B", "flow": "1.0 mL/min", "temp": "35 °C", "detection": "310 nm",
   "injection": "5 mL(원문 표기 그대로)", "sample_prep": "뿌리를 20 mm로 썰어 50 °C에서 24–48시간 건조·2.0 mm 이하 분쇄 → 시료 5 g에 물 20배, 80 °C 3시간 환류 추출 → Whatman No. 41 여과·감압 농축(수율 약 38.5%) → 50% 에탄올에 30 mg/mL로 녹여 0.2 µm PTFE 여과",
   "standard": "베르갑텐·잔토톡신(ChemFaces) 1 mg/mL 원액, 50% 에탄올로 희석한 작업 표준액 6단계",
   "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "알려진 파스닙 성분인 두 푸로쿠마린을 추출물 품질관리·재현성을 위한 지표성분으로 골라 정량했다[3]. 직선성·검출한계·정량한계·회수율은 본문에 없어 비워 둠.",
  "source": [3], "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11803109/", "source_kind": "paper"},
 {"role": "literature", "compound": "Xanthotoxin", "compound_ko": "잔토톡신(8-MOP)", "part": "뿌리 30% 에탄올 추출물(생것·60 °C 숙성)",
  "content": "생 파스닙 0.183 ± 0.016 mg/g, 숙성 파스닙 0.070 ± 0.001 mg/g[4]", "method": "HPLC-PDA",
  "conditions": {"instrument": "", "column": "Agilent ZORBAX Eclipse Plus C18, 4.6 × 250 mm, 5 µm",
   "mobile_phase": "A: 물, B: 메탄올", "gradient": "0–5분 40% B; 15분 60%; 25분 80%; 30분 85%; 31분 40%, 35분까지 유지",
   "flow": "1 mL/min", "temp": "30 °C", "detection": "PDA 320 nm", "injection": "10 µL",
   "sample_prep": "껍질을 살짝 벗겨 0.5 cm 두께로 썰고(숙성군은 60 °C 대류 오븐 최대 30일) 30% 에탄올 1:5로 실온 24시간 진탕(125 rpm) 추출 2회 → 감압 농축(35 °C) → 메탄올에 10 mg/mL로 녹여 초음파 1분, 0.2 µm PVDF 여과",
   "standard": "8-MOP(Sigma-Aldrich)를 메탄올 1 mL에 녹여 0.2 µm PVDF 여과", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "미나리과 채소의 대표 푸로쿠마린으로 골라 숙성 공정 중 변화를 추적했다[4]. 검출·정량한계와 회수율은 본문에 없어 비워 둠.",
  "source": [4], "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11614627/", "source_kind": "paper"},
 {"role": "literature", "compound": "Falcarindiol", "compound_ko": "팔카린디올", "part": "뿌리 30% 에탄올 추출물(생것·60 °C 숙성)",
  "content": "생 파스닙 0.005 mg/g, 숙성 파스닙 0.141 mg/g[4]", "method": "HPLC-PDA",
  "conditions": {"instrument": "", "column": "CAPCELL PAK C18 UG120, 4.6 × 250 mm, 5 µm (Osaka Soda)",
   "mobile_phase": "A: 물, B: 아세토니트릴",
   "gradient": "0–5분 20% B; 10분 50%; 30분 53%; 45분 65%; 70–72분 75%; 90–95분 95%; 100분 100%; 110분 20% B",
   "flow": "1 mL/min", "temp": "30 °C", "detection": "PDA 210 nm", "injection": "10 µL",
   "sample_prep": "추출물에 초순수를 넣어 50 mg/mL로 만든 뒤 같은 부피 초산에틸로 액-액 추출 3회 → 초산에틸층 합쳐 질소 건조 → 메탄올에 100 mg/mL로 녹여 0.2 µm PVDF 여과",
   "standard": "팔카린디올(ChemFaces)을 메탄올에 녹여 0.2 µm PVDF 여과", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "파스닙 추출물의 주요 폴리아세틸렌으로 정량했고, 숙성 후 크게 늘어 항염 효과를 일부 설명하는 성분으로 제시되었다[4]. 검출·정량한계와 회수율은 본문에 없어 비워 둠.",
  "source": [4], "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11614627/", "source_kind": "paper"},
]

d = {
 "slug": "pastinaca-sativa", "name_ko": "파스닙", "name_en": "Parsnip",
 "scientific_name": "Pastinaca sativa L.",
 "aliases": ["설탕당근", "아메리카 방풍나물", "Wild parsnip", "파스닙뿌리", "파스닙잎"],
 "sections": sections, "compounds": compounds, "markers": [], "nutrients": nutrients,
 "assays": assays, "production": [], "world": [], "gi": [], "orgs": [], "sources": sources,
}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in sections:
    print(s["key"], len(s["body"]))
