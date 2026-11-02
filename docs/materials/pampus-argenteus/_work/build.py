import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
ACC = "2026-11-02"
def pm(n, title, doi, pub, pmid, pmc=None, note=""):
    return {"n": n, "title": title + (f" ({note})" if note else ""), "url": f"https://doi.org/{doi}" if doi else f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
            "publisher": f"{pub} (PubMed {pmid}{', ' + pmc if pmc else ''})", "accessed": ACC}
sources = [
 {"n": 1, "title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — '병어' 행(학명 Pampus argenteus, 영문 Silver pomfret, 이명 병치·편어, 수산물, 부위 '-', 사용가능, 사용 조건 없음)과 같은 속 '덕대' 행(Pampus echinogaster, Korean pomfret, 이명 큰벵치·고려병어, 사용가능); 로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json 및 docs/materials/pampus-argenteus/card.json으로 확인",
  "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
 pm(2, "Silver Pomfret (Pampus argenteus) Aquaculture: Advances, Bottlenecks, and Future Strategies. Animals (Basel) 2025;15(22):3347", "10.3390/ani15223347", "Animals (MDPI)", "41302057", "PMC12649313", "PubMed 도구로 PMC 전문 확인"),
 pm(3, "New genetic perspectives of the ambiguous pomfret Pampus argenteus as revealed by CR sequences. ZooKeys 2017;(719):59-73", "10.3897/zookeys.719.19914", "ZooKeys", "29290722", "PMC5740407", "PubMed 도구로 PMC 전문 확인; 전문 텍스트에서 이탤릭 학명이 빠져 있어 종명은 명명자·연도 표기(Basilewsky, 1855 = P. echinogaster; Temminck & Schlegel, 1845 = P. punctatissimus)로 대응시킴"),
 pm(4, "Molecular systematics of Pampus (Perciformes: Stromateidae) based on thousands of nuclear loci using target-gene enrichment. Mol Phylogenet Evol 2019;140:106595", "10.1016/j.ympev.2019.106595", "Molecular Phylogenetics and Evolution", "31421244", None, "초록 확인"),
 pm(5, "Molecular based phylogenetic species recognition in the genus Pampus (Perciformes: Stromateidae) reveals hidden diversity in the Indian Ocean. Mol Phylogenet Evol 2017;109:240-245", "10.1016/j.ympev.2016.12.030", "Molecular Phylogenetics and Evolution", "28062269", None, "초록 확인"),
 pm(6, "Resurrection and Re-description of Pampus candidus (Cuvier), Silver Pomfret from the Northern Indian Ocean. Zool Stud 2019;58:e7", "10.6620/ZS.2019.58-07", "Zoological Studies", "31966308", "PMC6763701", "초록 확인; PMC 본문은 도구에서 비어 있었음. 종명 'Pampus candidus'는 PubMed 검색어 일치로 확인"),
 {"n": 7, "title": "한국산 병어·덕대의 형태와 COI 유전자 분석에 따른 학명 재검토(한국 근해 병어류 분류 연구, 2023; koreascience 게재) — 이 환경에서 koreascience 가 막혀 원문을 열지 못하고 WebSearch 검색 결과 요약으로만 확인(요약 내용: 한국 병어는 처음 P. argenteus, 덕대는 P. echinogaster로 분류되었으나 최근 병어를 P. punctatissimus, 덕대를 P. argenteus로 쓰는 것이 타당하다는 결론). 핵심 근거로 쓰지 않음",
  "url": "https://koreascience.kr/article/JAKO202319156668999.pdf", "publisher": "koreascience(한국과학기술정보연구원) — WebSearch 요약", "accessed": ACC},
 pm(8, "Chromosome-level genome assembly of the silver pomfret Pampus argenteus. Sci Data 2024;11(1):234", "10.1038/s41597-024-03070-0", "Scientific Data", "38395996", "PMC10891316", "초록 확인"),
 pm(9, "Two high quality chromosome-scale genome assemblies of female and male silver pomfret (Pampus argenteus). Sci Data 2024;11(1):1100", "10.1038/s41597-024-03914-9", "Scientific Data", "39379396", "PMC11461637", "초록 확인"),
 pm(10, "Chromosome-level genome assembly and annotation of Pampus argenteus and Pampus punctatissimus. Sci Data 2026;13(1)", "10.1038/s41597-026-06739-w", "Scientific Data", "41741493", "PMC13046862", "초록 확인"),
 pm(11, "The complete mitochondrial genome sequence of Pampus argenteus (Perciformes: Stromateidae). Mitochondrial DNA A 2016;27(1):115-7", "10.3109/19401736.2013.873929", "Mitochondrial DNA Part A", "24438313", None, "초록 확인"),
 pm(12, "The complete mitogenome of Pampus argenteus (Perciformes: Stromateidae). Mitochondrial DNA A 2016;27(1):684-5", "10.3109/19401736.2014.913142", "Mitochondrial DNA Part A", "24779600", None, "초록 확인"),
 pm(13, "Evaluation of genetic diversity in Pampus argenteus using SSR markers. Genet Mol Res 2013;12(4):5833-41", "10.4238/2013.November.22.10", "Genetics and Molecular Research", "24301952", None, "초록 확인"),
 pm(14, "Genetic Structure and Optimal Population Size of Wild and Mass-Selected Silver Pomfret (Pampus argenteus) in China. Biology (Basel) 2025;14(5):534", "10.3390/biology14050534", "Biology (MDPI)", "40427723", "PMC12108807", "초록 확인"),
 pm(15, "Latitudinal-environmental variations driving the local adaptation of Pampus argenteus stocks along the Chinese coast. Mar Life Sci Technol 2025;7(3):606-618", "10.1007/s42995-025-00312-x", "Marine Life Science & Technology", "40919467", "PMC12413356", "초록 확인"),
 pm(16, "Effects of Replacing Fishmeal With Antarctic Krill Meal on Nutrient Deposition, Metabolism, and Immunity in Silver Pomfret (Pampus argenteus). Aquac Nutr 2026;2026:4095616", "10.1155/anu/4095616", "Aquaculture Nutrition", "41821649", "PMC12976148", "PubMed 도구로 PMC 전문(Methods·표) 확인"),
 pm(17, "Dietary Inulin Modulates Intestinal Health and Muscle Nutritional Composition in Juvenile Silver Pomfret (Pampus argenteus). Foods 2026;15(13):2391", "10.3390/foods15132391", "Foods (MDPI)", "42450511", "PMC13361336", "PubMed 도구로 PMC 전문(Methods) 확인"),
 pm(18, "Biochemical composition of juvenile cultured vs. wild silver pomfret, Pampus argenteus: determining the diet for cultured fish. Fish Physiol Biochem 2010;36(4):1105-11", "10.1007/s10695-010-9388-5", "Fish Physiology and Biochemistry", "20309629", None, "초록 확인"),
 pm(19, "Growth Performance and Realized Heritability in a Mass-Selected Strain of Silver Pomfret (Pampus argenteus). Animals (Basel) 2025;15(11):1625", "10.3390/ani15111625", "Animals (MDPI)", "40509091", "PMC12153585", "초록 확인"),
 pm(20, "Outbreak of Cryptocaryon irritans infection in silver pomfret Pampus argenteus cultured in China. Dis Aquat Organ 2022;154:59-68", "10.3354/dao03728", "Diseases of Aquatic Organisms", "37318385", None, "초록 확인"),
 pm(21, "Recent advances in artificial breeding and larval rearing of silver pomfret Pampus argenteus (Euphrasen 1788) in Kuwait. Saudi J Biol Sci 2021;28(10):5808-5815", "10.1016/j.sjbs.2021.06.026", "Saudi Journal of Biological Sciences", "34588895", "PMC8459042", "초록 확인"),
 pm(22, "A review of the status and development of Kuwait's fisheries. Mar Pollut Bull 2015;100(2):597-606", "10.1016/j.marpolbul.2015.07.053", "Marine Pollution Bulletin", "26233306", None, "초록 확인"),
 pm(23, "Effects of high hydrostatic pressure-assisted thawing on the physicochemical characteristics of silver pomfret (Pampus argenteus). Food Sci Nutr 2019;7(5):1573-1583", "10.1002/fsn3.966", "Food Science & Nutrition", "31139370", "PMC6526670", "초록 확인"),
 pm(24, "Improvements in chitosan-based slurry ice production and its application in precooling and storage of Pampus argenteus. Food Chem 2022;393:133266", "10.1016/j.foodchem.2022.133266", "Food Chemistry", "35653987", None, "초록 확인"),
 pm(25, "Evaluation of storage quality of vacuum-packaged silver Pomfret (Pampus argenteus) treated with combined ultrasound and plasma functionalized liquids hurdle technology. Food Chem 2022;391:133237", "10.1016/j.foodchem.2022.133237", "Food Chemistry", "35640333", None, "초록 확인"),
 pm(26, "Species identification and quantification of silver pomfret using the droplet digital PCR assay. Food Chem 2019;302:125331", "10.1016/j.foodchem.2019.125331", "Food Chemistry", "31404867", None, "초록 확인"),
 pm(27, "Determination of the geographical origin of Trachinotus ovatus and Pampus argenteus in China by multi-element and stable isotope analysis. Food Chem 2022;394:133457", "10.1016/j.foodchem.2022.133457", "Food Chemistry", "35716499", None, "초록 확인"),
 pm(28, "The concentration and probabilistic risk assessment of potentially toxic elements in fillets of silver pomfret (Pampus argenteus): A global systematic review and meta-analysis. J Environ Sci (China) 2021;100:167-180", "10.1016/j.jes.2020.07.014", "Journal of Environmental Sciences", "33279029", None, "초록 확인"),
 pm(29, "Methylmercury and trace elements in the marine fish from coasts of East China. J Environ Sci Health A 2013;48(12):1491-501", "10.1080/10934529.2013.796820", "Journal of Environmental Science and Health, Part A", "23802158", None, "초록 확인"),
 pm(30, "Polychlorinated biphenyls (PCBs) in marine fishes from China: levels, distribution and risk assessment. Chemosphere 2012;89(8):944-9", "10.1016/j.chemosphere.2012.06.048", "Chemosphere", "22863061", None, "초록 확인"),
 pm(31, "Effects of supplemental medusa (Rhopilema esculentum) on intestinal microbiota and metabolites in silver pomfret (Pampus argenteus). J Fish Biol 2025;106(2):216-229", "10.1111/jfb.15926", "Journal of Fish Biology", "39360517", None, "초록 확인"),
 pm(32, "Draft genome sequence of the silver pomfret fish, Pampus argenteus. Genome 2016;59(1):51-8", "10.1139/gen-2015-0056", "Genome (Canadian Science Publishing)", "26692342", None, "초록 확인"),
 pm(33, "Occurrence and health risk of perfluoroalkyl acids (PFAAs) in seafood from Yellow Sea, China. Sci Total Environ 2019;665:1026-1034", "10.1016/j.scitotenv.2019.02.165", "Science of the Total Environment", "30893734", None, "초록 확인"),
]

S = {}
S["overview"] = ("병어(Pampus argenteus)는 병어과(Stromateidae) 병어속의 바닷물고기로, 식약처 「식품원료 목록」에 '병어'(영문 Silver pomfret, 이명 병치·편어)라는 원료명의 수산물로 올라 있다[1]. "
 "이 목록에서 상태는 '사용가능'이고 사용 부위는 따로 정하지 않은 '-'로 적혀 있으며 별도의 사용 조건은 없다[1]. 건강기능식품 고시형 원료의 원재료 목록에는 없어 식약처가 정한 지표성분도 없다[1]. "
 "같은 속의 덕대(Pampus echinogaster, 영문 Korean pomfret)는 목록에서 별도 원료로 올라 있고, 이 문서는 덕대 자료를 따로 섞지 않았다[1].\n\n"
 "병어는 중국 연안 전역에 사는 상업 가치가 높은 어종으로, 영양 구성이 좋고 시장 값이 높아 양식 대상종으로 연구되고 있다[2]. 다만 병어속은 종끼리 생김새가 매우 비슷해 학명이 자주 잘못 붙는다는 지적이 있어, 아래 수치는 논문이 적은 학명대로 옮기되 산지를 함께 적었다[3, 4]. "
 "중국 양식 개체의 근육은 수분 76.88%, 조단백질 14.81%, 조지방 5.84%(어분 사료 대조군)였다[16]. 국가표준식품성분표의 병어 값은 이번 조사에서 확인하지 못함.")
S["history"] = ("병어 인공 번식 연구는 1960년대 일본 세토내해에서 처음 인공수정과 배·자어 발생을 기록한 데서 시작되었다고 정리된다[2]. 쿠웨이트에서는 1990년대에 아라비아만 개체의 번식 생물학 연구가 시작되어 2007년 처음 양식 어미에서 자손을 얻었지만 생존율은 3–4%에 그쳤다[2]. "
 "쿠웨이트 과학연구소의 2012–2016년 시험에서도 자연산 어미 알의 부화율은 25.6–76.7%였으나 변태 치어의 생존율은 3.7–5.7%로 낮았다[21]. 쿠웨이트에서는 병어(현지명 zobaidy)의 어획량과 단위노력당 어획량이 계속 줄어 자원량이 낮은 상태로 평가되었다[22].\n\n"
 "중국에서는 1980년대 말 동중국해의 알·자어 형태 연구가 시작되었고, 2004년 동해수산연구소가 인공 번식 연구를 시작해 2006년 첫 자어를 생존율 14.1%로 얻었다[2]. 2010년 처음으로 완전 인공 번식에 성공했고 지금까지 치어 110만 마리가 연안 여러 성에 공급되었다[2]. "
 "닝보대학은 2011년 수조 안 자연 산란·수정에 성공했으며, 협력 종묘 업체의 치어 생산은 2023년 41만 8천 마리, 2024년 35만 마리였다(업체 자료 인용)[2]. 한국에서 병어를 이용·관리해 온 역사를 적은 공식 자료는 확인하지 못함.")
S["biology"] = ("병어는 따뜻한 온대 연안의 표층 어종으로, 몸은 달걀꼴로 옆으로 매우 납작하고 머리와 입이 작으며 양턱에 끝이 세 갈래인 잔 이빨이 한 줄로 나 있다[2]. 비늘은 작고 얇은 둥근비늘로 잘 떨어지며, 이 특징 때문에 양식 중 다루기가 어렵고 2차 감염 위험이 커진다[2]. "
 "부레가 없고 타원형 인두낭(pharyngeal sac)이 있는 것이 병어아목의 특징이며, 부레가 없어 계속 헤엄쳐야 하므로 용존산소 요구가 매우 높다[2].\n\n"
 "자연 서식 수온은 8–26 ℃이고 양식 최적 수온은 25–28 ℃이며, 14 ℃ 아래나 32 ℃ 위에서는 먹이 활동이 크게 준다[2]. 염분은 10–36에서 견디고 최적은 20–25이다[2]. "
 "갑각류·해파리·화살벌레·두족류 유생을 먹는 잡식성이며 특히 해파리를 좋아해 하루에 몸무게의 10배 넘게 먹기도 한다[2]. 해파리를 함께 먹인 치어는 비만도와 장 아밀레이스 활성이 높아졌다[31]. "
 "성숙 최소 나이는 약 1살이고 대부분 2살에 성숙하며, 하구의 기수 혼합 해역에서 여러 번 나누어 알을 낳는다[2]. 염색체 수는 2n = 48이다[2].")
S["related_species"] = ("병어속(Pampus)은 종 사이 형태가 매우 비슷해 분류가 어렵고, 공공 유전자 데이터베이스(NCBI)의 COI 서열에서도 종 오동정이 광범위하게 확인되었다[4]. "
 "핵 유전자 1만 7천여 개 좌위 분석 연구는 형태·분자 결과 모두 덕대(P. echinogaster)가 병어(P. argenteus)의 동종이명이라고 보았다[4]. 반면 다른 연구는 Euphrasen(1788)의 원기재가 한 개체만으로 이루어져 두 종이 흔히 같은 종으로 혼동된다고 하면서, 황해·발해·동중국해 북부의 이른바 'P. argenteus'는 실제로는 P. echinogaster이고 이 해역에는 P. echinogaster와 P. punctatissimus만 산다는 견해를 정리했다[3]. "
 "이 견해에서 진짜 병어는 대만해협 남쪽에서 인도네시아를 거쳐 페르시아만까지 사는 난류성 어종이다[3].\n\n"
 "인도양 쪽에서도 인도 연안의 'P. argenteus'는 남중국해 개체와 COI 유전 거리가 12%를 넘어 다른 종으로 보였고[5], 가장 흔한 종은 Pampus candidus로 재기재되었다[6]. "
 "국내 문헌에서는 병어를 처음 P. argenteus, 덕대를 P. echinogaster로 썼으나 최근에는 병어를 P. punctatissimus, 덕대를 P. argenteus로 쓰는 것이 타당하다는 연구가 있다는 검색 결과가 있었으나, 원문은 열지 못해 확인하지 못함[7]. "
 "식약처 목록은 병어=P. argenteus, 덕대=P. echinogaster로 따로 올려 두었으므로 이 문서는 목록 학명을 따르되 산지별 동정 문제를 함께 밝힌다[1].")
S["cultivation"] = ("병어는 스트레스에 민감하고 환경 요구가 까다로워 중국에서는 주로 육상 수조식 양식으로 기르며, 용존산소 6 mg/L 초과, 수온 17–32 ℃, 염분 20–32, pH 7.5–8.2를 유지한다[2]. 무리 짓는 습성이 강해 일반 못 양식은 효과가 낮아 못 안에 가두리를 두는 방식이 쓰이고, 바다 가두리는 아직 만족스럽지 않아 외해 양식은 시범 단계다[2]. "
 "자어 생존율이 10–20% 이하로 낮고, 양식 1년에 최대 300–400 g까지 크지만 250 g 넘는 개체는 드물며, 20–40%가 100 g 미만에서 일찍 성숙해 성장이 둔해지는 것이 큰 과제다[2].\n\n"
 "중국의 3세대 집단선발에서 120일째 선발군의 몸무게는 대조군보다 33.93% 무거웠고, 몸무게의 실현 유전력은 0.55였다[19]. 선발 세대의 유효집단크기는 83.7, 66.6, 59.6으로 조금씩 줄어 유전 다양성 감시가 필요하다고 했다[14]. "
 "2021년 여름 닝보 양식 못에서는 백점병 원충(Cryptocaryon irritans) 감염이 발생했고, 인공 감염 72시간 폐사율은 감염량에 따라 8.3–66.7%였다[20]. "
 "자연산은 양식산보다 조단백질과 n-3 지방산이 많고 조지방은 적었다[18]. 국내 병어 어획·양식 생산 통계는 국가통계포털 등이 이 환경에서 막혀 확인하지 못함.")
S["processing"] = ("냉동 병어를 100 MPa 고압으로 해동하면 물 해동보다 해동 시간과 조리·총 손실이 줄고 근원섬유 단백질 산화가 적었으며, 150 MPa 이상에서는 익은 듯한 색 변화가 나타나 100 MPa가 최적 조건으로 제시되었다[23]. "
 "키토산을 넣은 슬러리 얼음은 판 얼음이나 일반 슬러리 얼음보다 예냉이 빠르고 0 ℃ 저장 중 세균 증식·TBARS·휘발성염기질소 증가를 더 잘 억제했다[24]. "
 "초음파와 플라스마 처리수를 함께 쓴 뒤 진공 포장해 4 ℃에 15일 저장한 연구에서는 처리 직후 부패균이 1.99 log 줄었다[25].\n\n"
 "값비싼 병어에 다른 어종을 섞는 위장 문제에 대응해 개발된 디지털 PCR(ddPCR) 판별법은 검출한계 2 copies/μL, 정량한계 21 copies/μL였고 고기 혼합물에서 0.1%까지 검출했다[26]. "
 "다원소와 탄소·질소 안정동위원소 분석으로 중국 세 해역 병어의 산지를 판별한 교차검증 정확도는 92.2%였다[27]. "
 "국내 병어 가공·유통 통계는 이번 조사에서 확인하지 못함.")
S["genetics"] = ("2024년 일루미나·PacBio HiFi·Hi-C로 만든 첫 염색체 수준 유전체는 518.06 Mb이고 24개 의사염색체에 배치되었으며 단백질 암호 유전자 24,696개, BUSCO 98.9%였다[8]. "
 "같은 해 암수 유전체도 발표되어 수컷 유전체는 553.79 Mb 가운데 550.82 Mb가 끊김 없는 24개 염색체에 놓였고 유전자 23,346개가 예측되었다[9]. "
 "2026년에는 병어와 P. punctatissimus의 염색체 수준 유전체가 함께 발표되었고 병어 쪽 단백질 암호 유전자는 22,284개였다[10]. 쿠웨이트 개체로 만든 2016년 초안 유전체는 추정 크기의 63.7%인 350 Mb를 담았다[32].\n\n"
 "미토콘드리아 전장 유전체는 17,098 bp로 보고된 것과 16,544 bp로 보고된 것이 있어 길이가 서로 다르며, 병어속은 공공 데이터베이스 서열의 종 오동정이 많다고 지적된 만큼 비교할 때 표본의 동정을 확인해야 한다[11, 12, 4]. "
 "동중국해·황해·발해 132개체의 미세부수체 13좌위 분석에서는 유전 변이의 92.45%가 집단 안에 있었다[13]. 중국 연안 6개 집단 117개체 재서열 분석은 위계적 집단 구조는 없었지만 수온·일조와 관련된 21개 구간에서 지역 적응 신호를 찾았다[15]. "
 "쿠웨이트·파키스탄·중국 집단의 조절영역 분석에서는 후기 플라이스토세에 갈라진 두 계통이 모든 집단에 섞여 있었다[3].")
S["safety"] = ("식약처 「식품원료 목록」에서 병어는 별도 조건 없는 '사용가능' 원료이며, 건강기능식품 고시형 원료가 아니어서 고시 섭취 시 주의사항은 없다[1]. 병어를 따로 다룬 국내 공공기관의 알레르기·잔류물질 정보는 이번 조사에서 확인하지 못함.\n\n"
 "1983–2020년 문헌 21편의 메타분석에서 병어 살의 메틸수은 합산 평균은 46.58 μg/kg(습중량)으로 조사 원소 가운데 가장 낮았고, 납 1486.44, 카드뮴 992.50 μg/kg이었다[28]. 같은 분석의 비발암 위해지수는 성인 기준 말레이시아 2.500, 방글라데시 0.886, 중국 0.045로 나라별 차이가 컸다[28]. "
 "다만 인도양 표본에는 P. candidus 등 다른 종이 섞였을 수 있다[5, 6]. 중국 동부 연안의 병어는 조기류(부세·참조기)보다 총수은 대비 메틸수은 비율이 낮았고, 세 어종 표본의 16%에서 카드뮴이 유럽연합 기준을 넘었지만 위해지수는 모두 1 미만이었다[29]. "
 "중국 연안 병어의 PCB 농도는 부세보다 낮았으나 다이옥신 유사 PCB의 평생 발암 위해는 10⁻⁶을 넘는 것으로 계산되었다[30]. 황해 수산물 14종 가운데 과불화화합물 합계는 병어에서 가장 낮았으나, 황해 표본은 한 견해에 따르면 P. echinogaster일 수 있다[33, 3].")

compounds = [
 dict(name="Lysine", name_ko="라이신", cls="필수아미노산", role="nutrient", part="근육", ct="56.27 ± 4.56 mg/g (중국 양식 치어, 어분 사료 대조군; 원문에 건량·습량 기준 표기 없음)", act="근육 단백질의 주요 필수아미노산으로 표에 정량되었다[16]", src=[16]),
 dict(name="Glutamic acid", name_ko="글루탐산", cls="아미노산", role="nutrient", part="근육", ct="64.38 ± 4.22 mg/g (대조군), 크릴밀 20% 대체군 72.05 ± 4.89 mg/g", act="아스파르트산·페닐알라닌과 함께 주요 맛 아미노산으로 설명되었다[16]", src=[16]),
 dict(name="Aspartic acid", name_ko="아스파르트산", cls="아미노산", role="nutrient", part="근육", ct="52.38 ± 5.03 mg/g (대조군)", act="맛을 내는 주요 아미노산으로 설명되었다[16]", src=[16]),
 dict(name="Leucine", name_ko="류신", cls="필수아미노산(BCAA)", role="nutrient", part="근육", ct="40.18 ± 3.23 mg/g (대조군), 크릴밀 20% 대체군 47.01 ± 2.19 mg/g", act="분지사슬아미노산으로 단백질 합성·근육 성장에 관여한다고 설명되었다[16]", src=[16]),
 dict(name="Valine", name_ko="발린", cls="필수아미노산(BCAA)", role="nutrient", part="근육", ct="37.53 ± 3.59 mg/g (대조군)", act="분지사슬아미노산이다[16]", src=[16]),
 dict(name="Glycine", name_ko="글리신", cls="아미노산", role="nutrient", part="근육(등살)", ct="20.23 ± 1.53 mg/g (대조군)[16]; 이눌린 사료군에서 증가(수치는 그림에만 있어 확인하지 못함)[17]", act="맛 관련 아미노산으로 분류되었다[17]", src=[16, 17]),
 dict(name="Docosahexaenoic acid", name_ko="DHA", cls="n-3 고도불포화지방산", role="nutrient", part="근육", ct="총 지방산의 11.24 ± 1.02% (대조군), 크릴밀 20% 대체군 13.02 ± 0.97%", act="크릴밀 대체로 근육 침착이 늘어난 n-3 장쇄 지방산이다[16]", src=[16]),
 dict(name="Eicosapentaenoic acid", name_ko="EPA", cls="n-3 고도불포화지방산", role="nutrient", part="근육", ct="총 지방산의 4.08 ± 0.52% (대조군), 크릴밀 20% 대체군 5.87 ± 0.46%", act="n-3 장쇄 지방산이다[16]", src=[16]),
 dict(name="Oleic acid", name_ko="올레산(C18:1n-9)", cls="단일불포화지방산", role="nutrient", part="근육", ct="총 지방산의 25.52 ± 2.23% (대조군)[16]", act="병어의 주된 단일불포화지방산(C18:1)으로 보고되었다[16, 18]", src=[16, 18]),
 dict(name="Palmitoleic acid", name_ko="팔미톨레산(C16:1)", cls="단일불포화지방산", role="nutrient", part="근육", ct="총 지방산의 8.12 ± 0.56% (대조군)", act="단일불포화지방산 가운데 올레산 다음으로 많았다[16]", src=[16]),
 dict(name="Palmitic acid", name_ko="팔미트산(C16:0)", cls="포화지방산", role="nutrient", part="전어체·근육(치어)", ct="양식·자연산 모두 주된 포화지방산(수치는 초록에서 확인하지 못함); 포화지방산 합계 34.22 ± 2.25%[16]", act="양식산이 자연산보다 포화지방산이 많았다[18]", src=[18, 16]),
 dict(name="Linoleic acid", name_ko="리놀레산(C18:2n-6)", cls="n-6 지방산", role="nutrient", part="근육", ct="총 지방산의 3.02 ± 0.57% (대조군), 크릴밀 대체 수준이 높을수록 감소", act="사료 조성에 따라 근육 함량이 달라졌다[16]", src=[16]),
 dict(name="Selenium", name_ko="셀레늄", cls="무기질(미량원소)", role="nutrient", part="살(필레)", ct="메타분석 합산 평균 1053.47 μg/kg(습중량)", act="필수 미량원소이며 수은 독성 완화와 관련해 함께 평가되는 원소다[28]", src=[28]),
]
comp = [{"name": c["name"], "name_ko": c["name_ko"], "class": c["cls"], "role": c["role"], "part": c["part"], "content_text": c["ct"], "activity_ko": c["act"], "source": c["src"]} for c in compounds]

E = {k: "" for k in ["instrument","column","mobile_phase","gradient","flow","temp","detection","injection","sample_prep","standard","linearity","lod","loq","recovery"]}
def cond(**kw):
    d = dict(E); d.update(kw); return d
assays = [
 {"role": "literature", "compound": "Amino acids (lysine, glutamic acid, leucine etc.)", "compound_ko": "근육 구성 아미노산(라이신·글루탐산·류신 등)",
  "part": "근육", "content": "대조군 라이신 56.27, 글루탐산 64.38, 류신 40.18 mg/g; 총 아미노산 472.99 mg/g[16]",
  "method": "HPLC-UV/형광 아님(OPA/FMOC 유도체화 후 UV 검출)", "conditions": cond(
    instrument="Agilent 1260 Infinity HPLC, OPA/FMOC 자동 유도체화 모듈",
    column="C18 역상 칼럼 4.6 mm × 250 mm, 5 μm (Agilent)",
    mobile_phase="A: 40 mmol/L 인산염 완충액(pH 7.8), B: 아세토나이트릴·메탄올·물(45:45:10, v/v/v)",
    gradient="기울기 용리(시간표는 본문에 없음)", flow="1.0 mL/min", temp="40 °C",
    detection="OPA 유도체 338 nm, FMOC 유도체 262 nm",
    sample_prep="중국 푸젠 푸딩 연구센터 양식 치어(초기 12.93 g)를 60일 사육 후 근육 채취·−80 °C 보관; 근육 0.1 g을 6 mol/L HCl, 110 °C에서 24시간 가수분해 → 회전증발 농축 → 중화 → 유도체화",
    standard="외부 표준 검량"),
  "rationale": "근육 아미노산 조성은 어육의 영양가(필수아미노산)와 맛(글루탐산·아스파르트산)을 함께 보여 주는 지표로 쓰였다[16]. 전문(Methods) 확인 — 기울기 시간표·주입량·검출·정량한계·회수율은 본문에 없음. 시료는 중국 양식 개체로, 중국 양식 'P. argenteus'가 P. echinogaster일 수 있다는 견해가 있어 종 동정에 유의[3, 16].",
  "source": [16, 3], "url": "https://doi.org/10.1155/anu/4095616", "source_kind": "paper"},
 {"role": "literature", "compound": "Docosahexaenoic acid / Eicosapentaenoic acid", "compound_ko": "DHA·EPA(지방산 메틸에스터)",
  "part": "근육", "content": "대조군 DHA 11.24%, EPA 4.08% (총 지방산 중); 크릴밀 20% 대체군 DHA 13.02%, EPA 5.87%[16]",
  "method": "GC(지방산 메틸에스터)", "conditions": cond(
    instrument="Agilent 7890A 가스크로마토그래프",
    column="DB-23, 60 m × 0.25 mm × 0.25 μm",
    gradient="오븐 50 °C 1분 → 30 °C/min로 175 °C → 1 °C/min로 215 °C → 2 °C/min로 230 °C, 10분 유지",
    sample_prep="동결건조 근육 0.5 g에서 Folch 법으로 총지질 추출 → 14% 삼플루오린화붕소/메탄올로 메틸화",
    standard="알려진 표준품과 머무름 시간 비교로 동정·정량"),
  "rationale": "EPA·DHA는 어육 지질의 영양 가치를 보여 주는 n-3 장쇄 지방산으로, 사료 조성에 따른 근육 품질 비교 지표로 쓰였다[16]. 전문(Methods) 확인 — 검출기 종류·운반기체·주입 조건·검출·정량한계는 본문에 없음[16].",
  "source": [16], "url": "https://doi.org/10.1155/anu/4095616", "source_kind": "paper"},
 {"role": "literature", "compound": "Oleic acid (fatty acid profile)", "compound_ko": "올레산 등 근육 지방산 조성",
  "part": "근육(등살)", "content": "이눌린 5 g/kg 사료군에서 올레산·C17:1 증가, C14:0·C15:0·C17:0 감소(수치는 그림·표에만 있어 본문에서 확인하지 못함)[17]",
  "method": "GC(지방산 메틸에스터, 외부표준법)", "conditions": cond(
    instrument="Trace GC Ultra 가스크로마토그래프(Thermo Fisher Scientific)",
    column="HB-88 모세관 칼럼, 100 m × 0.25 mm × 0.20 μm",
    mobile_phase="운반기체 수소", flow="1.3 mL/min (분할비 5:1)",
    gradient="100 °C 15분 → 10 °C/min로 180 °C(6분 유지) → 2 °C/min로 210 °C(6분 유지) → 4 °C/min로 240 °C(10분 유지)",
    sample_prep="저장 닝보 샹산만 부화장 치어(초기 1.32 g) 8주 사육 후 등살을 수조별로 합쳐 −80 °C 보관; 근육 3.0 g을 8.3 M HCl로 가수분해 → 석유에테르·다이에틸에테르(1:1) 추출 → 2% NaOH-메탄올 80 °C 비누화 → 15% 삼플루오린화붕소-메탄올 80 °C 2분 메틸화 → n-헵테인 추출·무수황산나트륨 탈수",
    standard="외부 표준법 정량, 면적 정규화로 상대 비율 계산"),
  "rationale": "사료 처리에 따른 근육 지방산 조성 변화를 보는 지표로, 주된 단일불포화지방산인 올레산의 변화가 강조되었다[17]. 전문(Methods) 확인 — 검출기 종류·주입량·검출·정량한계·회수율은 본문에 없음[17].",
  "source": [17], "url": "https://doi.org/10.3390/foods15132391", "source_kind": "paper"},
]
# fix typo
assays[2]["conditions"]["sample_prep"] = assays[2]["conditions"]["sample_prep"].replace("저장 닝보", "중국 저장성 닝보")
assays[0]["method"] = "HPLC-UV (OPA/FMOC 유도체화)"

titles = {"overview": "한눈에 보기", "history": "이용·연구 역사", "biology": "어종·형태·생태", "related_species": "관련 종·학명 문제",
          "cultivation": "양식·어획", "processing": "저장·가공·판별", "genetics": "유전 정보", "safety": "안전성"}
d = {"slug": "pampus-argenteus", "name_ko": "병어", "name_en": "Silver pomfret", "scientific_name": "Pampus argenteus (Euphrasen, 1788)",
     "aliases": ["병어", "병치", "편어", "Silver pomfret", "Silvery pomfret", "Zobaidy"],
     "sections": [{"key": k, "title": titles[k], "body": S[k]} for k in titles],
     "compounds": comp, "markers": [], "assays": assays, "nutrients": [], "production": [], "world": [], "gi": [], "orgs": [],
     "sources": sources}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for k in titles: print(k, len(S[k]))
