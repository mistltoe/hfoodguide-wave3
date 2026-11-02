import json
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "dossier.json"
A = "2026-11-02"
I1020 = "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020"


def pm(pmid):
    return f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"


def pmc(p):
    return f"https://pmc.ncbi.nlm.nih.gov/articles/{p}/"


sources = [
    (1, "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 뱀딸기열매(Duchesnea indica (Andr.) Focke / Duchesnea indica var. major Makino / Fragaria indica Andr.)", I1020, "식품의약품안전처", "2026-10-13"),
    (2, "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 대조 행: 흰땃딸기열매(Fragaria nipponica), 딸기(Fragaria x ananassa), 베스카딸기(Fragaria vesca), 딱지꽃·가락지나물 등 Potentilla 속 원료", I1020, "식품의약품안전처", "2026-10-13"),
    (3, "Phenolic Profiling of Duchesnea indica Combining Macroporous Resin Chromatography (MRC) with HPLC-ESI-MS/MS and ESI-IT-MS. Molecules. 2015;20(12):22463-75", pmc("PMC6332051"), "Molecules (PubMed Central)", A),
    (4, "Separation and elucidation of anthocyanins in the fruit of mockstrawberry (Duchesnea indica Focke). Nat Prod Res. 2009;23(17):1589-98", pm("19851924"), "Natural Product Research (PubMed)", A),
    (5, "[New ellagic glycosides and known triterpenoids from Duchesnea indica Focke]. Yao Xue Xue Bao. 1996;31(11):844-8", pm("9863255"), "Acta Pharmaceutica Sinica (PubMed)", A),
    (6, "Polyphenolic composition and antioxidant potential of underutilized Himalayan wild edible berries by HPLC-ESI-QTOF-MS. J Sep Sci. 2021", pm("34633763"), "Journal of Separation Science (PubMed)", A),
    (7, "Evaluation of Polyphenolics Content and Antioxidant Activity in Edible Wild Fruits. Biomed Res Int. 2019;2019:1381989", pmc("PMC6354156"), "BioMed Research International (PubMed Central)", A),
    (8, "Duchesnea indica (Andr.) Focke extracts exerted anti-inflammatory effect via inhibiting MAPK/ERK pathway in LPS-stimulated RAW264.7 cells. Biochem Biophys Rep. 2025;44:102273", pmc("PMC12508595"), "Biochemistry and Biophysics Reports (PubMed Central)", A),
    (9, "Duchesnea indica Extract Attenuates Coal Fly Ash-Induced Inflammation in Murine Alveolar Macrophages through the NF-Kappa B Pathway. Evid Based Complement Alternat Med. 2021;2021:5546052", pmc("PMC8203366"), "Evidence-Based Complementary and Alternative Medicine (PubMed Central)", A),
    (10, "Duchesnea phenolic fraction inhibits in vitro and in vivo growth of cervical cancer through induction of apoptosis and cell cycle arrest. Exp Biol Med. 2009;234(1):74-83", pm("19064947"), "Experimental Biology and Medicine (PubMed)", A),
    (11, "Suppression of human ovarian SKOV-3 cancer cell growth by Duchesnea phenolic fraction is associated with cell cycle arrest and apoptosis. Gynecol Oncol. 2008;108(1):173-81", pm("17959232"), "Gynecologic Oncology (PubMed)", A),
    (12, "Evaluation of the anti-neuraminidase activity of the traditional Chinese medicines and determination of the anti-influenza A virus effects of the neuraminidase inhibitory TCMs in vitro and in vivo. J Ethnopharmacol. 2011;137(1):534-42", pm("21699971"), "Journal of Ethnopharmacology (PubMed)", A),
    (13, "Rapid identification and isolation of neuraminidase inhibitors from mockstrawberry (Duchesnea indica Andr.) based on ligand fishing combined with HR-ESI-Q-TOF-MS. Acta Pharm Sin B. 2020", pmc("PMC7606179"), "Acta Pharmaceutica Sinica B (PubMed Central)", A),
    (14, "Characterization, antioxidant, and anticancer activities of a neutral polysaccharide from Duchesnea indica (Andr.) Focke. J Food Biochem. 2019;43(7):e12899", pm("31353707"), "Journal of Food Biochemistry (PubMed)", A),
    (15, "Extraction of crude polysaccharides from Duchesnea indica (Andrews) Focke: optimization by response surface methodology. Biosci Biotechnol Biochem. 2015", pm("25849714"), "Bioscience, Biotechnology, and Biochemistry (PubMed)", A),
    (16, "White-fruited Duchesnea indica (Rosaceae) is impaired in ANS gene expression. Am J Bot. 2011;98(12):2077-83", pm("22130272"), "American Journal of Botany (PubMed)", A),
    (17, "First Report of Anthracnose on Fruits of Duchesnea indica Caused by Colletotrichum acutatum in Northwestern Argentina. Plant Dis. 2012", pm("30727537"), "Plant Disease (PubMed)", A),
    (18, "Response of the Invasive Alien Plant Duchesnea indica (Andrews) Teschem. to Different Environmental and Competitive Settings. Plants. 2025;14(11):1563", pmc("PMC12157201"), "Plants (PubMed Central)", A),
    (19, "Broad Habitat Tolerance of the Alien Duchesnea indica (Andrews) Teschem. Across Urban Vegetation Communities in a Central European City. Plants. 2026;15(19):2910", pmc("PMC13667203"), "Plants (PubMed Central)", A),
    (20, "Spatial heterogeneity in light supply affects intraspecific competition of a stoloniferous clonal plant. PLoS One. 2012;7(6):e39105", pmc("PMC3374777"), "PLoS One (PubMed Central)", A),
    (21, "[Architectural plasticity of the stoloniferous herb, Duchesnea indica in response to different elevation]. Ying Yong Sheng Tai Xue Bao. 2002;13(4):399-402", pm("12222040"), "Chinese Journal of Applied Ecology (PubMed)", A),
    (22, "Does Long-Term Elevation of CO2 Concentration Increase Photosynthesis in Forest Floor Vegetation? (Indiana Strawberry in a Maryland Forest). Plant Physiol. 1997;114(1):337-344", pmc("PMC158309"), "Plant Physiology (PubMed Central)", A),
    (23, "The rust genus Frommeella revisited: a later synonym of Phragmidium after all. Mycologia. 2011;103(6):1451-63", pm("21828214"), "Mycologia (PubMed)", A),
    (24, "DNA methylation variation and growth in the clonal Duchesnea indica is regulated by both past and present lead environments. Epigenetics. 2024;19(1):2305078", pmc("PMC10802196"), "Epigenetics (PubMed Central)", A),
    (25, "Parental UV-B radiation regulates the habitat selection of clonal Duchesnea indica in heterogeneous light environments. Funct Plant Biol. 2022", pm("35272763"), "Functional Plant Biology (PubMed)", A),
    (26, "Metal analysis, phytotoxic, insecticidal and cytotoxic activities of selected medicinal plants of Khyber Pakhtunkhwa. Pak J Pharm Sci. 2012", pm("22186309"), "Pakistan Journal of Pharmaceutical Sciences (PubMed)", A),
    (27, "Protective Effects of Duchesnea chrysantha Ethanol Extract Against UVB-Induced Skin Damage via Modulation of TAK1-Associated Signaling Pathways. Chem Biodivers. 2026;23(9):e71768", pmc("PMC13616469"), "Chemistry & Biodiversity (PubMed Central)", A),
    (28, "PubMed 검색: \"Duchesnea indica\"[tiab] OR \"Potentilla indica\"[tiab] — 59건(2026-11-02 조회, 사람 대상 시험 없음)", "https://pubmed.ncbi.nlm.nih.gov/?term=%22Duchesnea+indica%22%5Btiab%5D+OR+%22Potentilla+indica%22%5Btiab%5D", "National Library of Medicine (PubMed)", A),
    (29, "Protective effect of the methanolic extract from Duchesnea indica against oxidative stress in vitro and in vivo. Environ Toxicol Pharmacol. 2011;31(1):42-50", pm("21787668"), "Environmental Toxicology and Pharmacology (PubMed)", A),
    (30, "Duchesnea indica Extract Ameliorates LPS-Induced Septic Shock in Mice. Evid Based Complement Alternat Med. 2022;2022:5783867", pmc("PMC9124116"), "Evidence-Based Complementary and Alternative Medicine (PubMed Central)", A),
    (31, "Antimicrobial Activity of Chitosan/Gelatin/Poly(vinyl alcohol) Ternary Blend Film Incorporated with Duchesnea indica Extract in Strawberry Applications. Foods. 2022;11(24):3963", pmc("PMC9778419"), "Foods (PubMed Central)", A),
    (32, "Arbuscular mycorrhizae of dominant plant species in Yungas forests, Argentina. Mycologia. 2009;101(5):612-21", pm("19750940"), "Mycologia (PubMed)", A),
    (33, "Diversity, Isolation and Bioactive Secondary Metabolites of Endophytic Fungi in Duchesnea indica (Andr.) Focke. Curr Microbiol. 2025", pm("41085593"), "Current Microbiology (PubMed)", A),
    (34, "Anxiolytic and antidepressant potential of extracts of Duchesnea indica in animal models. PHYTOnutrients. 2022", pmc("PMC9840006"), "PHYTOnutrients (PubMed Central)", A),
    (35, "Host plant use in sympatric closely related flea beetles. Environ Entomol. 2007;36(2):468-74", pm("17445383"), "Environmental Entomology (PubMed)", A),
]

S = {}
S["overview"] = (
    "뱀딸기(Duchesnea indica (Andr.) Focke)는 장미과(Rosaceae)의 여러해살이풀로, 땅 위로 기는줄기(포복경)를 뻗어 번지고 딸기를 닮은 붉은 열매를 맺는다[3][16][20]. "
    "영어로는 mock strawberry·Indian strawberry 등으로 부르며, 재배 딸기의 야생 근연종으로 소개된다[1][17]. "
    "최근 분류에서는 Duchesnea 속에 두던 종을 양지꽃속(Potentilla)으로 옮겨 Potentilla indica 라는 이름도 쓰며, 같은 종이다[18][23].\n\n"
    "식품의약품안전처 「식품원료 목록」에서 뱀딸기는 '뱀딸기열매' 한 원료명으로 실린 사용가능 원료이고, 사용 조건은 '사용가능부위 : 열매'이다[1]. "
    "목록에는 다른 이름 배암딸기·큰배암딸기와 이명 Duchesnea indica var. major Makino, Fragaria indica Andr. 가 함께 적혀 있다[1]. "
    "잎·줄기·전초를 원료명으로 한 행은 목록에서 확인되지 않았고, 건강기능식품 고시형 원료의 원재료 기록도 확인하지 못함.\n\n"
    "성분 연구는 대부분 약재로 쓰는 전초나 잎·줄기를 대상으로 했으며, 엘라지타닌·브레비폴린 카복실산 같은 페놀 성분이 많다고 보고되었다[3][9]. "
    "열매에서는 시아니딘-3-O-루티노사이드 중심의 안토시아닌이 확인되었다[4]. "
    "PubMed 에서 사람을 대상으로 한 시험은 찾지 못했다[28]."
)
S["history"] = (
    "중국에서는 뱀딸기를 '蛇莓(SheMei)'라 부르며, 전초를 열을 내리고 해독하며 어혈을 푸는 약으로 써 왔다고 소개된다[8]. "
    "아시아에서 오래전부터 나병·선천성 발열·조직 염증·토혈·암 치료에 쓰였고, 지금도 단독으로 또는 중국 한약 처방의 주재료로 암, 특히 부인과 암 치료에 쓰인다고 기술되었다[3]. "
    "여러 논문이 '아시아에서 수 세기 동안 암 치료에 써 왔다'고 소개하며, 페놀 분획의 항암 기전을 세포·생쥐에서 시험했다[10][11]. "
    "중국 전통 약재 439종의 물 추출물을 비교한 연구에서는 Fragaria indica Andr. 라는 옛 학명과 함께 실려 인플루엔자 뉴라미니다아제를 강하게 억제한 5종에 들었다[12]. 이어진 연구에서는 부탄올 추출물에서 엘라지타닌 12종을 포함한 뉴라미니다아제 결합 성분 24개를 찾아냈다[13].\n\n"
    "한국·방글라데시·일본 등에서도 민간약으로 널리 쓰였다고 기술한 연구도 있다[9]. "
    "파키스탄 히말라야 지역에서는 주민이 먹는 야생 과일 20종 조사에 뱀딸기 열매가 포함되었고, 이 과일들은 날로 먹거나 소화기 질환에 쓴다고 보고되었다[7]. "
    "약재 기록은 대부분 전초(全草)에 대한 것이며, 열매만을 식용으로 쓴 국내 전통 기록은 확인하지 못함."
)
S["biology"] = (
    "뱀딸기는 기는줄기로 새 개체(라멧)를 만드는 클론성 여러해살이풀이다[20][21]. "
    "온실 실험에서 빛이 약해지거나 같은 종끼리 경쟁하면 생물량·라멧 수·기는줄기 총길이가 줄었다[20]. "
    "중국의 해발 400–1600 m 실험에서는 기는줄기 마디 길이·라멧 밀도·가지 치는 정도가 고도에 따라 2차 곡선 형태로 달라졌다[21]. "
    "그늘에서는 잎자루가 길어지고 비엽면적이 커졌다[18].\n\n"
    "원산지는 아시아이며 유럽에서는 잔디밭·공원·도시 숲에 빠르게 퍼진 침입 외래식물로 다뤄진다[18]. "
    "슬로베니아 마리보르에서는 47곳에서 기록되었고 반그늘 서식지를 가장 선호했다[19]. "
    "아르헨티나 북서부에도 넓게 자라며, 미국 메릴랜드 숲 바닥에서도 연구되었다[17][22]. "
    "열매는 보통 붉은색이지만 아르헨티나에서 흰 열매 개체가 발견되었다[16]. "
    "뿌리의 수지상균근 감염률이 조사한 우점종 가운데 가장 높았고, 뿌리·줄기·잎·열매에 내생균류가 산다[32][33]. "
    "벼룩잎벌레 Altica fragariae 의 주 기주식물이기도 하다[35]."
)
S["related_species"] = (
    "뱀딸기는 장미과 양지꽃족에 속하며, Duchesnea 속으로 분류되던 종들은 지금은 양지꽃속(Potentilla)으로 다뤄진다[23]. "
    "그래서 논문에는 Duchesnea indica 와 Potentilla indica 두 이름이 함께 쓰인다[18][28]. "
    "식품원료 목록은 Fragaria indica Andr. 와 변종 Duchesnea indica var. major Makino 를 같은 원료의 이명으로 묶었다[1].\n\n"
    "이름이 비슷한 다른 원료와 구분해야 한다[2]. "
    "흰땃딸기(Fragaria nipponica)는 목록에서 다른 이름 '흰뱀딸기'로도 적혀 있지만 딸기속의 다른 종이다[2]. "
    "재배 딸기(Fragaria x ananassa)와 베스카딸기(Fragaria vesca)도 목록에 각각 별도 원료로 실려 있다[2]. "
    "같은 양지꽃속의 딱지꽃(Potentilla chinensis)은 순·잎만 사용가능이고 줄기는 사용불가로 적혀 있다[2]. "
    "근연종 Duchesnea chrysantha 도 동아시아 전통의학에서 염증·피부 질환에 써 왔다고 소개되며, 별도로 연구된다[27]. "
    "Duchesnea chrysantha 의 식품원료 지위는 목록에서 확인하지 못함."
)
S["cultivation"] = (
    "뱀딸기는 주로 저절로 자라는 들풀이며, 국내 재배 면적·생산량 통계는 농림축산식품부 특용작물 통계 등 로컬 통계 파일에서 확인하지 못함. "
    "지리적 표시 등록 기록도 확인하지 못함.\n\n"
    "생육 조건에 대한 연구는 생태 실험이 많다[18][20]. "
    "화분 실험에서 빛과 양분이 늘면 생물량·잎·라멧 수·기는줄기와 꽃 생산이 늘었고, 다른 식물과 경쟁하면 생장이 크게 줄었다[18]. "
    "미국 메릴랜드 숲 바닥에서 이산화탄소 농도를 67 Pa 로 3.5년 높인 결과 최대 양자효율이 22% 높아지고 광보상점이 42% 낮아졌다[22]. "
    "납으로 오염된 환경을 겪은 어미 라멧의 자손은 오염된 땅을 피해 좋은 곳으로 자라는 경향을 보였다[24]. "
    "아르헨티나에서는 열매에 Colletotrichum acutatum 에 의한 탄저병이 처음 보고되었는데, 그 전까지는 딸기에서 분리한 탄저균에 거의 걸리지 않는 것으로 알려져 있었다[17]."
)
S["processing"] = (
    "식품원료 목록에서 식품에 쓸 수 있는 부위는 열매뿐이다[1]. "
    "식약처 「식품 등의 생산실적」 건강기능식품 품목 자료에서 뱀딸기 원료 품목은 확인하지 못함.\n\n"
    "연구에서 쓰인 가공 형태는 대부분 전초·잎·줄기 추출물이다[3][9]. "
    "말린 전초 분말 100 g 을 70% 에탄올로 초음파 추출한 뒤 AB-8 합성흡착수지로 페놀 성분을 모아 분석한 예가 있다[3]. "
    "다른 연구에서는 업체에서 산 말린 잎·줄기를 70% 에탄올(1:20)로 80 °C 에서 2시간 추출해 동결건조했다[9]. "
    "열수 추출·에탄올 침전으로 얻은 중성 다당 DIP-1 은 분자량 218.3 kDa 이고 포도당과 갈락토오스가 주성분이었다[14]. 다당류 추출 조건을 반응표면분석으로 최적화한 연구에서 최적 조건은 98.51 °C·6.16시간·물 30.94 mL/g 이고 수율은 6.430 ± 0.078% 였다[15]. "
    "물 추출·알코올 침전 추출물은 총 다당 32.62 ± 0.91%, 총 폴리페놀 12.16 ± 0.27% 였다[8]. "
    "뱀딸기 추출물을 넣은 키토산·젤라틴·PVA 코팅을 딸기에 2회 이상 입히면 상온 24시간 저장에서 식중독균 증식이 줄었고, 3회 코팅에서 최대 3.2 log CFU/g 감소했다는 포장 연구도 있다[31]. "
    "열매는 히말라야 지역에서 생과로 먹는 야생 과일로 분석되었다[6][7]."
)
S["genetics"] = (
    "뱀딸기의 핵 유전체나 엽록체 유전체 전체 서열 논문은 PubMed 에서 확인하지 못함. "
    "분자 연구는 열매 색과 후성유전에 집중되어 있다[16][24][25].\n\n"
    "아르헨티나에서 발견된 흰 열매 개체는 기는줄기로 번식시키면 늘 흰 열매를 맺었고, 안토시아닌 합성 유전자 가운데 ANS(안토시아니딘 합성효소)의 발현이 낮은 것이 원인으로 제시되었다[16]. "
    "교배 자손의 열매 색은 어미 쪽의 영향을 강하게 받았다[16].\n\n"
    "클론성 식물이라 어미의 환경이 자손에 전해지는지가 연구되었다[24][25]. "
    "납 오염을 겪은 어미의 자손은 DNA 메틸화 부위 구성이 달라졌고, 연구진은 이 '스트레스 기억'이 적어도 일부는 유전되는 후성유전 변이에 근거한다고 보았다[24]. "
    "자외선-B 를 강하게 쬔 어미의 자손에서 총 DNA 메틸화 수준이 25.94% 에서 27.15% 로 높아졌다[25]. "
    "Duchesnea 에 기생하는 녹병균의 분류 연구에서는 이 기주들을 'Duchesnea 로 분류되던 Potentilla 종'으로 기술해, 속 통합을 반영했다[23]."
)
S["safety"] = (
    "식품원료 목록상 뱀딸기는 열매만 식품에 쓸 수 있다[1]. "
    "연구에 많이 쓰인 전초·잎·줄기는 원료명 행이 없어 식품원료 사용 여부를 확인하지 못함. "
    "건강기능식품 고시형 원료의 원재료 기록은 확인하지 못해 고시 섭취 시 주의사항도 적용되지 않는다.\n\n"
    "PubMed 검색 59건 가운데 사람에게 먹인 시험이나 부작용 증례는 없었다[28]. "
    "동물 연구에서 생쥐에게 메탄올 추출물 100–200 mg/kg 을 먹인 불안·우울 모델 시험이 있으나, 초록에는 안전성 결과가 수치로 제시되지 않았다[34]. "
    "패혈증 생쥐 모델과 털 없는 생쥐 피부 실험에서는 추출물이 보호 효과를 보였다[29][30]. "
    "파키스탄에서 채집한 약용식물 4종(뱀딸기 포함)의 중금속 분석에서 납·크롬·구리·니켈·코발트가 대부분 시료에서 허용 한도를 넘었다고 보고되어, 야생 채집품은 채집지 오염에 주의할 필요가 있다[26]. "
    "알레르기·잔류농약 등 공공기관 안전 정보는 확인하지 못함. "
    "항암·항염 효과 보고는 모두 세포·동물 실험이며 열매가 아닌 전초·잎·줄기 추출물인 경우가 많다[9][10][11]."
)

titles = {
    "overview": "한눈에 보기",
    "history": "역사와 전통적 이용",
    "biology": "식물학적 특징",
    "related_species": "가까운 종과 혼동 주의",
    "cultivation": "자생과 생육 환경",
    "processing": "가공과 이용",
    "genetics": "분류와 유전 연구",
    "safety": "안전성과 주의",
}

compounds = [
    dict(name="Brevifolincarboxylic acid", name_ko="브레비폴린 카복실산", class_="페놀(엘라그산 관련 크로몬)", role="marker", part="전초(말린 것)",
         content_text="71.36 mg/100 g DW — 정량한 27개 페놀 중 최다[3]", activity_ko="전초 페놀 프로파일의 최대 성분, 품질 관리 지표 후보[3]", source=[3]),
    dict(name="Methyl brevifolincarboxylate", name_ko="메틸 브레비폴린 카복실레이트", class_="페놀(크로몬)", role="bioactive", part="전초(말린 것)",
         content_text="43.56 mg/100 g DW[3]", activity_ko="전초 페놀 성분(활성 단독 시험 없음)[3]", source=[3]),
    dict(name="Brevifolin", name_ko="브레비폴린", class_="페놀(크로몬)", role="bioactive", part="전초(말린 것)",
         content_text="21.71 mg/100 g DW[3]", activity_ko="전초 페놀 성분(활성 단독 시험 없음)[3]", source=[3]),
    dict(name="Ellagic acid", name_ko="엘라그산", class_="페놀산(엘라그산)", role="marker", part="전초·잎·줄기",
         content_text="전초 6.69 mg/100 g DW, 엘라그산·엘라그산 배당체 합계 30.52 mg/100 g DW[3]; 잎·줄기 70% 에탄올 추출물의 주성분(UPLC-QTOF-MS)[9]",
         activity_ko="잎·줄기 추출물의 항염(NF-κB 억제, 세포) 활성 후보 성분으로 제시[9]", source=[3, 9]),
    dict(name="Pedunculagin", name_ko="비스-HHDP-글루코오스(페둔쿨라긴 또는 카수아리인으로 추정되는 이성질체)", class_="엘라지타닌", role="bioactive", part="전초(말린 것)",
         content_text="이성질체 7개 피크 각 11.93–33.85 mg/100 g DW; 엘라지타닌 합계 252.98 mg/100 g DW(코릴라긴 환산)[3]",
         activity_ko="전초 페놀 중 가장 큰 무리인 엘라지타닌의 주 구성 단위[3]", source=[3]),
    dict(name="Caffeic acid", name_ko="카페산", class_="하이드록시신남산", role="bioactive", part="전초(말린 것)",
         content_text="14.74 mg/100 g DW[3]", activity_ko="표준품으로 확인된 페놀산[3]", source=[3]),
    dict(name="Astragalin", name_ko="아스트라갈린(캠페롤-3-O-글루코사이드)", class_="플라보놀 배당체", role="bioactive", part="전초(말린 것)",
         content_text="17.55 mg/100 g DW[3]", activity_ko="뱀딸기에서 처음 확인된 플라보놀[3]", source=[3]),
    dict(name="Isoschaftoside", name_ko="이소샤프토사이드(아피게닌 6-C-아라비노실-8-C-글루코사이드)", class_="플라본 C-배당체", role="bioactive", part="전초(말린 것)",
         content_text="10.13 mg/100 g DW[3]", activity_ko="뱀딸기에서 처음 확인[3]", source=[3]),
    dict(name="Cyanidin 3-O-rutinoside", name_ko="시아니딘-3-O-루티노사이드", class_="안토시아닌", role="marker", part="열매(생과)",
         content_text="열매 안토시아닌의 61%[4]", activity_ko="열매 붉은색의 주 색소[4]", source=[4]),
    dict(name="Peonidin 3-O-rutinoside", name_ko="페오니딘-3-O-루티노사이드", class_="안토시아닌", role="bioactive", part="열매(생과)",
         content_text="열매 안토시아닌의 34%[4]", activity_ko="열매 색소(활성 시험 없음)[4]", source=[4]),
    dict(name="Petunidin 3-O-rutinoside", name_ko="페투니딘-3-O-루티노사이드", class_="안토시아닌", role="bioactive", part="열매(생과)",
         content_text="열매 안토시아닌의 5%[4]", activity_ko="열매 색소(활성 시험 없음)[4]", source=[4]),
    dict(name="Ducheside A", name_ko="두체사이드 A(3'-O-메틸엘라그산-4-O-β-D-자일로피라노사이드)", class_="엘라그산 배당체", role="marker", part="원문 초록에 부위 미기재",
         content_text="새 화합물로 분리 보고, 함량 확인하지 못함[5]", activity_ko="뱀딸기에서 처음 분리된 고유 성분(두체사이드 B 와 함께)[5]", source=[5]),
    dict(name="Tormentic acid", name_ko="토르멘트산(2α,3β,19α-트리하이드록시우르스-12-엔-28-산)", class_="트리테르펜", role="bioactive", part="원문 초록에 부위 미기재",
         content_text="분리 보고, 함량 확인하지 못함; 배당체 2종과 함께 Duchesnea 속에서 처음 분리[5]", activity_ko="활성은 이 논문에서 시험하지 않음[5]", source=[5]),
    dict(name="Ursolic acid", name_ko="우르솔산(3β-하이드록시우르스-12-엔-28-산)", class_="트리테르펜", role="bioactive", part="원문 초록에 부위 미기재",
         content_text="분리 보고, 함량 확인하지 못함[5]", activity_ko="활성은 이 논문에서 시험하지 않음[5]", source=[5]),
]
for c in compounds:
    c["class"] = c.pop("class_")

empty = {k: "" for k in ["instrument", "column", "mobile_phase", "gradient", "flow", "temp", "detection", "injection", "sample_prep", "standard", "linearity", "lod", "loq", "recovery"]}
assays = [
    {
        "role": "literature",
        "compound": "Brevifolincarboxylic acid",
        "compound_ko": "브레비폴린 카복실산 등 전초 페놀 27종(엘라지타닌·엘라그산·하이드록시벤조산/신남산·플라보놀)",
        "part": "전초(말린 것, 식품원료 사용부위 아님)",
        "content": "브레비폴린 카복실산 71.36 mg/100 g DW; 27종 6.69–71.36 mg/100 g DW; 엘라지타닌 합계 252.98, 하이드록시벤조산·신남산 유도체 199.73, 플라보놀 90.39, 엘라그산류 30.52 mg/100 g DW[3]",
        "method": "HPLC-UV(260·360 nm), 동정은 HPLC-ESI-MS/MS·ESI-IT-MS",
        "conditions": {
            "instrument": "Thermo Accela 1250 U-HPLC + UV 검출기(동정: TSQ Quantum Access MAX 삼중사중극자, ESI 음이온 모드)",
            "column": "YMC PACK ODS-A, 250 × 4.6 mm, 5 μm",
            "mobile_phase": "A 0.5% 포름산 수용액, B 아세토니트릴",
            "gradient": "0–5분 A 95%; 5–10분 A 95→90%; 10–68분 A 90→78%",
            "flow": "0.8 mL/min",
            "temp": "30 °C",
            "detection": "UV 260 nm(엘라지타닌·엘라그산류), 360 nm(페놀산·플라보놀) 동시",
            "injection": "10 μL",
            "sample_prep": "45 °C 건조 전초 분말 100 g + 70% 에탄올 1000 mL, 실온 초음파 40분 × 3회 → 감압 농축·동결건조 → 물 50 mL 에 녹여 석유에테르로 엽록소 제거 → AB-8 합성흡착수지(45 × 5.3 cm), 물 세척 후 30·50·70·90% 에탄올 용출, 페놀은 분획 I 에 모임 → 동결건조 후 50% 메탄올에 재용해",
            "standard": "대표 표준품 5종(카페산·이소샤프토사이드·엘라그산·코릴라긴·아스트라갈린)으로 같은 무리 성분을 환산 정량",
            "linearity": "R² 0.9982–0.9998(예: 카페산 0.94–588 μg/mL, 코릴라긴 0.82–510 μg/mL)",
            "lod": "0.06–2.24 μg/mL(S/N 3; 아스트라갈린 0.06, 엘라그산 2.24)",
            "loq": "0.21–7.47 μg/mL(S/N 10)",
            "recovery": "",
        },
        "rationale": "연구진은 페놀 성분이 뱀딸기의 주된 활성 성분이며 다성분 품질 관리의 근거가 될 수 있다고 보고, 27종을 동정·정량했다[3]. 가장 많은 성분이 브레비폴린 카복실산이었다[3]. 회수율은 원문에 없어 비워 둠. 전초 시료이므로 식품원료(열매)에 그대로 적용할 수는 없다.",
        "source": [3],
        "url": pmc("PMC6332051"),
        "source_kind": "paper",
    },
    {
        "role": "literature",
        "compound": "Cyanidin 3-O-rutinoside",
        "compound_ko": "시아니딘-3-O-루티노사이드 등 열매 안토시아닌 3종(페오니딘·페투니딘-3-O-루티노사이드)",
        "part": "열매(생과)",
        "content": "시아니딘-3-O-루티노사이드 61%, 페오니딘-3-O-루티노사이드 34%, 페투니딘-3-O-루티노사이드 5%; 총 안토시아닌 '205 mg g(-1) of the fresh fruit'(초록 표기 그대로, 단위 확인 못함)[4]",
        "method": "HPLC-PDA-MS(분취 HPLC 분리 후 1H NMR 확인)",
        "conditions": dict(empty, sample_prep="0.1% HCl 에탄올로 추출 → C18 Sep-Pak 카트리지 정제(초록 기준)"),
        "rationale": "식품원료로 쓰는 열매의 주 색소이고 열매에서 직접 정량한 유일한 보고라 열매 지표 후보로 골랐다[4]. 전문 확인 못함(초록만 확인)이라 칼럼·이동상 등 조건 칸은 비워 둠.",
        "source": [4],
        "url": pm("19851924"),
        "source_kind": "paper",
    },
    {
        "role": "literature",
        "compound": "Rutin",
        "compound_ko": "갈산·바닐산·카페산·루틴·페룰산·퀘르세틴·미리세틴(히말라야 야생 베리 4종 비교)",
        "part": "열매(야생 베리)",
        "content": "4종 베리에서 69개 폴리페놀 동정, 7개 페놀 정량; 뱀딸기 개별 함량은 초록에 없어 확인하지 못함[6]",
        "method": "HPLC-ESI-QTOF-MS",
        "conditions": dict(empty),
        "rationale": "뱀딸기 열매를 식용 야생 베리로 보고 페놀 조성을 분석한 연구다[6]. 전문 확인 못함(초록만 확인).",
        "source": [6],
        "url": pm("34633763"),
        "source_kind": "paper",
    },
]

d = {
    "slug": "duchesnea-indica",
    "name_ko": "뱀딸기",
    "name_en": "Indian mock strawberry (mock strawberry)",
    "scientific_name": "Duchesnea indica (Andr.) Focke",
    "aliases": ["뱀딸기열매", "배암딸기", "큰배암딸기", "Potentilla indica", "Fragaria indica Andr.", "Duchesnea indica var. major Makino",
                "Wrinkled mock strawberry", "False Strawberry", "Indian strawberry", "mock strawberry", "蛇莓(SheMei)"],
    "sections": [{"key": k, "title": titles[k], "body": S[k]} for k in titles],
    "compounds": compounds,
    "markers": [],
    "assays": assays,
    "nutrients": [],
    "production": [],
    "world": [],
    "gi": [],
    "orgs": [],
    "sources": [dict(n=n, title=t, url=u, publisher=p, accessed=a) for n, t, u, p, a in sources],
}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in d["sections"]:
    print(s["key"], len(s["body"]))
