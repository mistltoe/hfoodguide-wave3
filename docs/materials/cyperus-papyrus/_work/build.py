import json
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "dossier.json"
PM = "PubMed"
A = "2026-11-02"

sources = [
    (1, "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 파피루스속대(Cyperus papyrus L.), 별칭 머리방동사니, 영문명 Papyrus, 식물, 사용가능, 사용가능부위: 속대; 같은 속 기름골덩이줄기(C. esculentus, 사용가능·덩이줄기), 너도방동사니덩이줄기(C. serotinus, 사용가능·덩이줄기), 참방동사니(C. iria, 사용불가), 향부자·향부자뿌리줄기(C. rotundus, 사용불가) 행 대조 (로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json)", "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "식품의약품안전처", "2026-10-13"),
    (2, "Chemical composition of the lipophilic compounds from the rind and pith of papyrus (Cyperus papyrus L.) stems — Front Plant Sci 2022;13:1097866 (PMID 36618622, PMC9813494, 전문 확인)", "https://doi.org/10.3389/fpls.2022.1097866", PM, A),
    (3, "Lignin Quantification of Papyri by TGA—Not a Good Idea — Molecules 2021;26(14):4384 (PMID 34299657, PMC8305842, 전문 확인)", "https://doi.org/10.3390/molecules26144384", PM, A),
    (4, "Flavonoids naringenin chalcone, naringenin, dihydrotricin, and tricin are lignin monomers in papyrus — Plant Physiol 2022;188(1):208-219 (PMID 34662399, PMC8774827, 전문 확인)", "https://doi.org/10.1093/plphys/kiab469", PM, A),
    (5, "Holocene climate changes explain the spatial pattern in genetic diversity in populations of Cyperus papyrus from Southeast Africa wetlands — Heredity 2022;129(5):295-304 (PMID 36163272, 초록 확인)", "https://doi.org/10.1038/s41437-022-00563-9", PM, A),
    (6, "Isotropic and anisotropic processes influence fine-scale spatial genetic structure of a keystone tropical plant — AoB Plants 2018;10(1):plx076 (PMID 29383234, 초록 확인)", "https://doi.org/10.1093/aobpla/plx076", PM, A),
    (7, "Clonal growth strategy, diversity and structure: A spatiotemporal response to sedimentation in tropical Cyperus papyrus swamps — PLoS One 2018;13(1):e0190810 (PMID 29338034, 초록 확인)", "https://doi.org/10.1371/journal.pone.0190810", PM, A),
    (8, "Permanent genetic resources added to molecular ecology resources database 1 December 2012-31 January 2013 — Mol Ecol Resour 2013;13(3):546-9 (PMID 23521844, 초록 확인)", "https://doi.org/10.1111/1755-0998.12095", PM, A),
    (9, "A review of the relative merits of conserving, using, or draining papyrus swamps — Environ Manage 2011;47(2):218-29 (PMID 21191792, 초록 확인)", "https://doi.org/10.1007/s00267-010-9592-1", PM, A),
    (10, "Integrating local ecological knowledge and management practices of an isolated semi-arid papyrus swamp (Loboi, Kenya) into a wider conservation framework — J Environ Manage 2011;93(1):71-84 (PMID 22054573, 초록 확인)", "https://doi.org/10.1016/j.jenvman.2011.08.005", PM, A),
    (11, "Biomass production of papyrus (Cyperus papyrus) in constructed wetland treating low-strength domestic wastewater — Bioresour Technol 2010;101(2):833-5 (PMID 19758797, 초록 확인)", "https://doi.org/10.1016/j.biortech.2009.08.062", PM, A),
    (12, "The photosynthetic characteristics of papyrus in a tropical swamp — Oecologia 1987;71(3):355-359 (PMID 28312981, 초록 확인)", "https://doi.org/10.1007/BF00378707", PM, A),
    (13, "The diurnal course of plant water potential, stomatal conductance and transpiration in a papyrus (Cyperus papyrus L.) canopy — Oecologia 1984;63(2):252-255 (PMID 28311021, 초록 확인)", "https://doi.org/10.1007/BF00379885", PM, A),
    (14, "The effect of wastewater discharge on biomass production and nutrient content of Cyperus papyrus and Miscanthidium violaceum in the Nakivubo wetland, Kampala, Uganda — Water Sci Technol 2003;48(5):233-40 (PMID 14621169, 초록 확인)", "https://pubmed.ncbi.nlm.nih.gov/14621169/", PM, A),
    (15, "A comparative study of Cyperus papyrus and Miscanthidium violaceum-based constructed wetlands for wastewater treatment in a tropical climate — Water Res 2004;38(2):475-85 (PMID 14675660, 초록 확인)", "https://doi.org/10.1016/j.watres.2003.10.008", PM, A),
    (16, "DNA decay rate in papyri and human remains from Egyptian archaeological sites — Am J Phys Anthropol 2002;117(4):310-8 (PMID 11920366, 초록 확인)", "https://doi.org/10.1002/ajpa.10045", PM, A),
    (17, "Carbon and oxygen isotope working standards from C3 and C4 photosynthates — Isotopes Environ Health Stud 2006;42(3):231-8 (PMID 16870558, 초록 확인)", "https://doi.org/10.1080/10256010600841059", PM, A),
    (18, "Uptake, translocation and metabolism of decabromodiphenyl ether (BDE-209) in seven aquatic plants — Chemosphere 2016;152:360-8 (PMID 26994429, 초록 확인)", "https://doi.org/10.1016/j.chemosphere.2016.03.013", PM, A),
    (19, "The fate of organic matter in a papyrus (Cyperus papyrus L.) dominated tropical wetland ecosystem in Nyanza Gulf (Lake Victoria, Kenya) inferred from delta13C and delta15N analysis — Isotopes Environ Health Stud 2005;41(4):379-90 (PMID 16543193, 초록 확인)", "https://doi.org/10.1080/10256010500384739", PM, A),
    (20, "Chimpanzee isotopic ecology: a closed canopy C3 template for hominin dietary reconstruction — J Hum Evol 2014;76:107-15 (PMID 24993419, 초록 확인)", "https://doi.org/10.1016/j.jhevol.2014.06.001", PM, A),
    (21, "Carbon dioxide and methane emissions from plants and peat soil in a Cyperus papyrus wetland in Uganda — Philos Trans R Soc Lond B Biol Sci 2026;381(1956) (PMID 42619513, 초록 확인)", "https://doi.org/10.1098/rstb.2025.0048", PM, A),
    (22, "Feedipedia(FAO·INRAE 등 사료 자료집) 'Papyrus (Cyperus papyrus)' 항목 — 원문은 열지 못하고 WebSearch 요약으로만 확인(속대를 날로·익혀 먹거나 사탕수수처럼 씹는다는 서술)", "https://feedipedia.review.fao.org/node/603", "Feedipedia (WebSearch 요약)", A),
    (23, "Status of Eldana saccharina (Lepidoptera: Pyralidae), its host plants and natural enemies in Ethiopia — Bull Entomol Res 2006;96(5):497-504 (PMID 17092361, 초록 확인)", "https://pubmed.ncbi.nlm.nih.gov/17092361/", PM, A),
    (24, "Comparative study on the performance of Typha latifolia and Cyperus Papyrus on the removal of heavy metals and enteric bacteria from wastewater by surface constructed wetlands — Chemosphere 2020;260:127551 (PMID 32683013, 초록 확인)", "https://doi.org/10.1016/j.chemosphere.2020.127551", PM, A),
    (25, "The impact of alum discharges on a natural tropical wetland in Uganda — Water Res 2001;35(3):795-807 (PMID 11228979, 초록 확인)", "https://doi.org/10.1016/s0043-1354(00)00301-8", PM, A),
    (26, "Removal of the endocrine disruptors ethinyl estradiol, bisphenol A, and levonorgestrel by subsurface constructed wetlands — Sci Total Environ 2019;693:133514 (PMID 31369896, 초록 확인; 'dwarf papyrus' = Cyperus isocladus)", "https://doi.org/10.1016/j.scitotenv.2019.07.320", PM, A),
]

sections = [
    ("overview", "한눈에 보기",
     "파피루스(Cyperus papyrus L.)는 사초과(Cyperaceae) 방동사니속의 큰 여러해살이 물가 식물로, 식약처 「식품원료 목록」에는 원료명 '파피루스속대', 영문명 'Papyrus'로 한 행이 올라 있다[1]. 이 행의 상태는 '사용가능'이고 사용 조건은 '사용가능부위 : 속대'여서, 이 목록으로 식품에 쓸 수 있는 부위는 줄기 안쪽의 흰 속살(속대)뿐이다[1]. 같은 목록의 별칭 칸에는 '머리방동사니'가 적혀 있으나, 국내 식물 이름 목록에서 이 이름이 같은 종을 가리키는지는 확인하지 못함. 이 종을 원재료로 하는 건강기능식품 고시형 원료는 확인하지 못함.\n\n"
     "줄기는 초록색 겉껍질(rind)과 흰 속(pith)으로 나뉘며, 속은 공기 통로가 많은 유조직에 관다발이 흩어진 조직이다[3]. 속대의 아세톤 추출 지질은 건물 기준 4.9%이고 그 가운데 식물스테롤(시토스테롤 등)과 지방산이 가장 많다[2]. 속대의 리그닌은 약 16%로 겉껍질보다 적다[3, 4]. 속대를 날로 또는 익혀 먹거나 씹는다는 서술은 WebSearch 요약으로만 확인했다[22]. 속대의 일반 영양성분(수분·단백질·당 등)을 정량한 1차 자료와 사람 대상 연구는 확인하지 못함."),
    ("history", "이용의 역사",
     "고대 이집트에서는 파피루스 줄기의 속(pith)을 얇게 저며 겹쳐 붙여 글쓰기 재료인 파피루스 종이를 만들었다[2, 16]. 옛 기록에 따르면 이 종이는 거의 속대만으로 만들었다고 하며, 현대 이집트에서 파는 파피루스 종이의 리그닌은 약 5%로 원래 속대(약 16%)보다 훨씬 낮았다[3]. 파피루스 종이에 남은 엽록체 DNA의 반감기는 약 19–24년으로 추정되어, 8세기 문서에서도 진짜 DNA는 남아 있지 않았다[16]. 케냐산 파피루스 줄기 속심과 이집트산 파피루스 종이는 탄소·산소 동위원소 분석의 실험실 작업 표준물질로도 쓰였다[17].\n\n"
     "아프리카에서는 줄기를 울타리·지붕·돗자리·섬유판·연탄 재료로 써 왔다[2]. 케냐 로보이 습지 주민 조사에서 파피루스는 돗자리 판매 소득, 소 먹이, 지붕 재료, 땔감으로 쓰였다[10]. 아프리카 파피루스 습지를 낮은 강도로 여러 용도로 쓰는 편이 물을 빼 농지로 바꾸는 것보다 가치가 크다는 검토가 있다[9]. 우간다 응고고의 침팬지가 가끔 파피루스를 먹는다는 관찰도 있다[20]. 사람이 속대를 음식으로 먹는다는 서술은 WebSearch 요약으로만 확인했고(원문 미확인), 고대 이집트에서 속대를 먹었다는 1차 사료는 확인하지 못함."),
    ("biology", "식물학적 특징",
     "파피루스는 중앙·동부·남부 아프리카 습지가 원산인 사초과 식물로, 1년 내내 자라며 지상부 순일차생산이 연간 헥타르당 건물 136.4 t에 이른다는 보고가 인용된다[2]. C4 광합성을 하는 사초로, 최대 순동화율은 35 μmol CO2 m⁻² s⁻¹였고 한낮의 강한 빛에서도 광포화가 일어나지 않았다[12]. 식물체의 탄소 동위원소 비(δ13C)는 −13.45 ± 0.62‰로 C4 식물의 범위에 든다[19].\n\n"
     "줄기 끝의 산형 꽃차례(umbel)가 주된 증산 기관이며, 케냐 나이바샤 호수 군락의 하루 증산량은 12.5 mm로 추정되었다[13]. 줄기 단면은 표피·후벽조직 하피·엽록조직으로 된 초록 겉껍질과, 큰 세포간극이 있는 통기조직에 관다발이 흩어진 흰 속으로 이루어진다[3]. 바람으로 꽃가루와 씨가 퍼지며, 에티오피아 습지에서 꽃가루의 평균 확산 거리는 101 m, 씨는 55 m 미만이었다[6]. 퇴적물이 많은 곳에서는 줄기가 짧고 촘촘하게 모여 자라는 방식으로 클론 생장 전략을 바꾼다[7]."),
    ("related_species", "근연종과 혼동 주의",
     "같은 방동사니속 가운데 식약처 「식품원료 목록」에는 기름골(C. esculentus)의 덩이줄기와 너도방동사니(C. serotinus)의 덩이줄기가 '사용가능'으로 올라 있다[1]. 이 두 원료는 땅속 덩이줄기를 쓰는 것이어서, 줄기 속대를 쓰는 파피루스속대와는 부위도 성분 자료도 다르다[1]. 특히 기름골 덩이줄기(타이거너트, chufa)의 지방·전분 자료를 파피루스에 옮겨 쓰면 안 된다[1]. 같은 속의 참방동사니(C. iria)와 향부자(C. rotundus)는 같은 목록에서 '사용불가'이다[1].\n\n"
     "영어로 'dwarf papyrus'라 불리는 식물은 다른 종(C. isocladus)이어서 이름만으로 자료를 찾으면 섞이기 쉽다[26]. 에티오피아 습지에서는 C. fastigiatus, C. dives 같은 다른 큰 사초가 파피루스와 함께 자란다[23]. 'papyrus'는 식물뿐 아니라 고대 문서(파피루스 종이)를 뜻하기도 해서 문헌 검색 때 구별해야 한다[3, 16]. 카드의 지표성분 후보(벤조다이퓨란다이온류 등)가 이 종의 어느 부위에서 얼마나 나왔는지는 확인하지 못함."),
    ("cultivation", "재배와 채취",
     "파피루스는 주로 아프리카의 자연 습지에서 자라며, 이집트 샤르키아주 카라무스에서는 농가가 노지에서 길러 1년 내내 수확할 수 있다[2, 3]. 케냐 로보이 습지의 경험 많은 채취자는 같은 자리를 되풀이해 베지 않는 돌려베기로 회복 시간을 주었으나, 70% 넘는 채취자가 물 돌리기와 가뭄으로 군락이 줄 것이라 예상했다[10]. 습지를 말려 농지로 바꾸는 일이 넓게 일어나고 있다[9].\n\n"
     "태국 인공습지 시험에서 생활하수로 기른 파피루스는 두 달 동안 건물 2200–3100 g/m²를 만들었고, 줄기의 열량은 16.2 MJ/kg이었다[11]. 우간다 나키부보 습지에서 하수 영향을 받은 지상부는 질소 1.6%·인 0.23%(건물 기준)로 영향을 받지 않은 곳(0.98%·0.18%)보다 높았다[14]. 정수장 명반 슬러지가 흘러든 습지에서는 생산성이 5.1 g/m²·일로 떨어지고 파피루스가 사라져 갔다[25]. 사탕수수 줄기 해충(Eldana saccharina)이 파피루스를 기주로 삼는다[23]. 국내 재배 면적·생산량 통계는 확인하지 못함."),
    ("processing", "가공과 제품",
     "연구에서는 줄기를 거둔 뒤 칼이나 나일론 실로 겉껍질을 벗겨 속대만 떼어 내고 공기 중에 말렸다[2, 3]. 말린 속대를 분쇄해 아세톤으로 12시간 속슬렛 추출하면 건물 기준 4.9%의 지질 추출물이 나왔다[2]. 이 추출물은 식물스테롤·스테롤 배당체·지방산·토코페롤 등으로 이루어져 바이오리파이너리 원료로 제안되었다[2].\n\n"
     "현대 이집트의 파피루스 종이는 리그닌이 약 5%로 원래 속대보다 크게 낮아, 만드는 과정에서 옛 방식과 다른 처리가 있는 것으로 보인다[3]. 겉껍질은 리그닌이 더 많고(Klason 리그닌 24.2%), 그 리그닌에 트리신·나린제닌 같은 플라보노이드가 결합해 있다[4]. 인공습지에서 거둔 줄기는 열량을 이용하는 바이오매스 연료로도 검토되었다[11]. 속대를 날로·익혀 먹거나 씹는다는 서술은 WebSearch 요약으로만 확인했다[22]. 국내에서 파피루스속대를 원료로 만든 식품이나 건강기능식품 생산실적은 확인하지 못함."),
    ("genetics", "유전과 품종",
     "파피루스의 집단유전 연구에는 마이크로새틀라이트 표지가 쓰이며, 이 종의 표지 좌위가 2013년 분자생태 자원 데이터베이스에 등록되었다[8]. 에티오피아 세 습지의 성체 510개체와 어린 개체 407개체를 15개 표지로 분석한 결과, 역사적 유전자 확산 거리는 4 m 미만으로 매우 짧았다[6]. 20개 표지로 636개 줄기(라멧)를 분석한 연구에서는 퇴적이 많은 곳의 클론 풍부도(R = 0.80)가 적은 곳(R = 0.48)보다 높았다[7].\n\n"
     "남동부 아프리카 잠베지강 유역 집단은 유전적 다양성이 매우 낮았고, 상류 집단이 하류보다 다양성이 높았다[5]. 이 양상은 홀로세 기후 변화와 새를 통한 씨앗 확산으로 설명되었다[5]. 파피루스 종이의 엽록체 rbcL 유전자 조각을 이용해 DNA 분해 속도를 잰 연구도 있다[16]. 식용 품종이나 육성 품종, 염색체 수·유전체 크기 자료는 확인하지 못함."),
    ("safety", "안전성",
     "식약처 「식품원료 목록」에서 파피루스속대는 '사용가능'이며 사용 조건은 '사용가능부위 : 속대'로, 겉껍질·뿌리줄기 등 다른 부위는 이 행에 포함되지 않는다[1]. 이 종의 속대에 대한 독성시험, 사람 섭취 연구, 알레르기 보고, 공공기관 안전 정보는 확인하지 못함.\n\n"
     "파피루스는 오수 정화용 인공습지에 널리 심는 식물로, 우간다 시험에서 제거된 질소의 69.5%, 인의 88.8%를 식물이 흡수·저장했다[15]. 이집트 인공습지 시험에서는 구리 72%, 아연 84%를 제거했다[24]. 수생식물 7종 화분 시험에서 파피루스 조직에도 브롬화 난연제(PBDE)가 쌓였다[18]. 이런 결과는 오염된 물에서 자란 파피루스가 오염물질을 몸에 담을 수 있음을 보여 주므로, 식품으로 쓸 때는 자란 곳의 수질을 따져야 한다[15, 18, 24]. 속대 지질에는 7-옥소스테롤 같은 산화 스테롤이 소량(건물 1 kg당 수십 mg) 들어 있다[2]. 파피루스 습지는 우기에 메테인을 많이 내놓는 곳이어서, 채취는 습지 보전과 함께 고려해야 한다[9, 21]."),
]

def comp(name, ko, cls, role, part, content, act, src):
    return dict(name=name, name_ko=ko, **{"class": cls}, role=role, part=part, content_text=content, activity_ko=act, source=src)

compounds = [
    comp("beta-Sitosterol", "베타-시토스테롤", "식물스테롤", "marker", "줄기 속(속대)",
         "속대 2280 mg/kg, 겉껍질 1720 mg/kg(건물 기준, GC-MS, 기술 반복 3회 평균)[2]",
         "속대 지질에서 가장 많은 유리 스테롤; 원문은 식물스테롤이 혈중 콜레스테롤을 낮추는 데 도움이 된다고 일반론으로 언급(이 소재로 시험한 것은 아님)[2]", [2]),
    comp("Stigmasterol", "스티그마스테롤", "식물스테롤", "bioactive", "줄기 속(속대)",
         "속대 1350 mg/kg, 겉껍질 620 mg/kg(건물 기준)[2]", "식물스테롤; 이 소재에서의 생리활성 시험은 확인하지 못함[2]", [2]),
    comp("Campesterol", "캄페스테롤", "식물스테롤", "bioactive", "줄기 속(속대)",
         "속대 1040 mg/kg, 겉껍질 370 mg/kg(건물 기준)[2]", "식물스테롤[2]", [2]),
    comp("Sitosteryl glucoside", "시토스테릴 3-O-β-D-글루코피라노사이드", "스테롤 배당체", "bioactive", "줄기 속(속대)",
         "속대 1210 mg/kg, 겉껍질 990 mg/kg(건물 기준); 스테롤 배당체 합계 속대 2140 mg/kg[2]", "가장 많은 스테롤 배당체; 표준품 대조로 확인[2]", [2]),
    comp("Palmitic acid", "팔미트산", "포화지방산", "nutrient", "줄기 속(속대)",
         "속대 2210 mg/kg, 겉껍질 2060 mg/kg(유리지방산, 건물 기준); 유리지방산 합계 속대 6245 mg/kg[2]", "유리지방산 계열에서 가장 많은 성분[2]", [2]),
    comp("Stearic acid", "스테아르산", "포화지방산", "nutrient", "줄기 속(속대)",
         "속대 1075 mg/kg, 겉껍질 550 mg/kg(건물 기준)[2]", "지방산[2]", [2]),
    comp("Oleic acid", "올레산", "단일불포화지방산", "nutrient", "줄기 속(속대)",
         "속대 790 mg/kg, 겉껍질 825 mg/kg(건물 기준)[2]", "불포화지방산[2]", [2]),
    comp("Linoleic acid", "리놀레산", "다중불포화지방산(오메가-6)", "nutrient", "줄기 속(속대)",
         "속대 610 mg/kg, 겉껍질 858 mg/kg(건물 기준)[2]", "필수지방산[2]", [2]),
    comp("alpha-Linolenic acid", "알파-리놀렌산", "다중불포화지방산(오메가-3)", "nutrient", "줄기 속(속대)",
         "속대 75 mg/kg, 겉껍질 500 mg/kg(건물 기준)[2]", "겉껍질에 훨씬 많고 속대에는 적음[2]", [2]),
    comp("alpha-Tocopherol", "알파-토코페롤", "토코페롤(비타민 E)", "nutrient", "줄기 속(속대)",
         "속대 25 mg/kg, 겉껍질 120 mg/kg(유리형, 건물 기준); 토코페롤 합계 속대 45 mg/kg[2]", "비타민 E 활성 성분; 겉껍질에 더 많음[2]", [2]),
    comp("Squalene", "스쿠알렌", "이소프레노이드 탄화수소", "bioactive", "줄기 속(속대)",
         "속대 70 mg/kg, 겉껍질 320 mg/kg(건물 기준)[2]", "속대의 주된 탄화수소(피타다이엔 30 mg/kg보다 많음)[2]", [2]),
    comp("2-Hydroxytetracosanoic acid", "2-하이드록시테트라코산산", "2-하이드록시지방산", "bioactive", "줄기 속(속대)",
         "속대 375 mg/kg, 겉껍질 110 mg/kg(건물 기준); 2-하이드록시지방산 합계 속대 830 mg/kg[2]", "속대에 특히 많은 지질 계열[2]", [2]),
    comp("Oleamide", "올레아마이드", "알킬아마이드", "bioactive", "줄기 속(속대)",
         "속대 175 mg/kg, 겉껍질 185 mg/kg(건물 기준)[2]", "원문은 알킬아마이드류의 약리 가능성을 일반론으로 언급(이 소재로 시험한 것은 아님)[2]", [2]),
    comp("Lignin", "리그닌", "페놀성 고분자(세포벽)", "bioactive", "줄기 속(속대)",
         "속대 약 16%(Klason·ABSL 두 방법이 일치), 시판 파피루스 종이 약 5%[3]; 겉껍질 Klason 리그닌 24.2 ± 0.5%[4]", "세포벽 구조 성분; 기존 TGA법은 함량을 25–47%로 과대평가[3]", [3, 4]),
    comp("Tricin", "트리신", "플라본(플라보노이드)", "bioactive", "줄기 겉껍질(속대 아님)",
         "겉껍질 리그닌에 결합된 형태로 DFRC·2D-NMR로 확인, 함량 수치는 본문에 없음[4]", "나린제닌 칼콘·나린제닌·다이하이드로트리신과 함께 리그닌 단량체로 작용; 속대에서는 확인하지 못함[4]", [4]),
]

assays = [
    {
        "role": "literature", "compound": "beta-Sitosterol", "compound_ko": "베타-시토스테롤(속대 지질 중 식물스테롤)",
        "part": "줄기 속(속대), 공기 건조", "content": "2280 mg/kg(건물 기준, 기술 반복 3회 평균)[2]",
        "method": "GC-MS(비유도체 및 BSTFA TMS 유도체)",
        "conditions": {
            "instrument": "Shimadzu QP 2010 Ultra GC-MS",
            "column": "DB-5HT 융합실리카 모세관(15 m × 0.25 mm i.d., 막 두께 0.1 μm, J&W Scientific)",
            "mobile_phase": "운반기체 헬륨",
            "gradient": "120 °C(1분) → 10 °C/분으로 380 °C, 5분 유지",
            "flow": "1 mL/분",
            "temp": "주입구 300 °C, 이송관 300 °C",
            "detection": "질량분석(NIST 라이브러리·문헌·표준품 비교로 동정)",
            "injection": "",
            "sample_prep": "속대와 겉껍질을 칼로 분리, 칼날 분쇄기로 2 mm·1 mm 체 통과, 아세톤 속슬렛 12시간 추출, 회전증발 건고(추출률 속대 4.9 ± 0.4%), 클로로폼에 재용해 후 그대로 또는 BSTFA로 TMS 유도체화",
            "standard": "테트라코산·팔미트산·리놀레산·스티그마스테롤·시토스테롤·콜레스테릴 리놀레이트·시토스테릴 글루코사이드·시토스테릴(6-O-팔미토일)글루코사이드·1-모노팔미틴·1,3-다이팔미틴·트라이팔미틴 혼합 표준, 0.1–1.0 mg/mL",
            "linearity": "", "lod": "", "loq": "", "recovery": "",
        },
        "rationale": "속대 지질에서 가장 많은 유리 스테롤이고 스테롤류가 속대 지질의 44.4%를 차지해 속대 지질 조성을 대표한다; 전문 확인, 직선성·검출한계·회수율은 원문에 없음[2].",
        "source": [2], "url": "https://doi.org/10.3389/fpls.2022.1097866", "source_kind": "paper",
    },
    {
        "role": "literature", "compound": "Lignin", "compound_ko": "리그닌(아세틸브로마이드 가용 리그닌, ABSL)",
        "part": "줄기 속(속대), 공기 건조", "content": "약 16%(Klason 리그닌+산가용 리그닌 값과 일치; 표의 개별 수치는 전문 텍스트에 없음)[3]",
        "method": "아세틸브로마이드 용해 후 UV 분광법(ABSL); 비교법 Klason(TAPPI T222 om-88)",
        "conditions": {
            "instrument": "Perkin Elmer Lambda 35 UV/Vis 분광광도계",
            "column": "", "mobile_phase": "", "gradient": "", "flow": "",
            "temp": "용해 50 °C, 2시간 교반",
            "detection": "280 nm, 흡광계수 20 L/g·cm",
            "injection": "",
            "sample_prep": "원심분쇄 후 가속용매추출(60 °C, 11 MPa, 정적 15분; 헥산 2회 → 아세톤/물 95:5 4–6회), 40 °C 진공 건조 3일; 시료 2–5 mg(3반복)을 25% 아세틸브로마이드/빙초산 0.2 mL에 용해, 2 M NaOH 1 mL와 0.5 M 하이드록실아민 염산염 0.175 mL 넣고 빙초산으로 10 mL",
            "standard": "흡광계수 환산(검량선 표준품 없음); Klason법은 72% 황산 가수분해 잔사, 회분·단백질 보정, 산가용 리그닌 205 nm(110 L/g·cm)",
            "linearity": "", "lod": "", "loq": "", "recovery": "",
        },
        "rationale": "속대의 세포벽 조성(리그닌이 적은 흰 조직)을 보여 주는 값이며, 기존 TGA법이 25–47%로 과대평가했음을 바로잡은 측정이다; 전문 확인, 검출한계·회수율은 원문에 없음[3].",
        "source": [3], "url": "https://doi.org/10.3390/molecules26144384", "source_kind": "paper",
    },
]

d = {
    "slug": "cyperus-papyrus",
    "name_ko": "파피루스속대",
    "name_en": "Papyrus (pith)",
    "scientific_name": "Cyperus papyrus L.",
    "aliases": ["파피루스", "머리방동사니(식품원료 목록 별칭)", "Papyrus"],
    "sections": [{"key": k, "title": t, "body": b} for k, t, b in sections],
    "compounds": compounds,
    "markers": [],
    "nutrients": [],
    "assays": assays,
    "production": [],
    "world": [],
    "gi": [],
    "orgs": [],
    "sources": [{"n": n, "title": t, "url": u, "publisher": p, "accessed": a} for n, t, u, p, a in sources],
}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in d["sections"]:
    print(s["key"], len(s["body"]))
