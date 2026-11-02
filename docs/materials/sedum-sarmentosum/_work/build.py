import json
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "dossier.json"
ACC = "2026-11-02"


def pm(pmid, title, journal, pmc=None):
    url = f"https://pmc.ncbi.nlm.nih.gov/articles/{pmc}/" if pmc else f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
    return {"title": title, "url": url, "publisher": f"{journal} (PubMed{' Central' if pmc else ''})", "accessed": ACC}


S = [
    {"title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 돌나물(Sedum sarmentosum Bunge)",
     "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},  # 1
    pm("41727992", "Characterization and evolutionary insights into complete mitochondrial genome of Sedum sarmentosum within the family Crassulaceae. Front Plant Sci. 2026", "Frontiers in Plant Science", "PMC12920544"),  # 2
    pm("41217303", "Traditional uses, phytochemistry, and pharmacological effects of Sedum sarmentosum: a review. J Pharm Pharmacol. 2026", "Journal of Pharmacy and Pharmacology"),  # 3
    pm("33164361", "[Research progress on chemical constituents and pharmacological effects of Sedum sarmentosum]. Zhongguo Zhong Yao Za Zhi. 2020", "China Journal of Chinese Materia Medica"),  # 4
    pm("24471077", "Physicochemical Characteristics and Antioxidant Capacity of Rice Cake (Sulgitteok) Supplemented with Lyophilized Sedum sarmentosum (Dolnamul) Powder. Prev Nutr Food Sci. 2012", "Preventive Nutrition and Food Science", "PMC3866748"),  # 5
    pm("19627195", "Water dropwort (Ostericum sieboldii) and Sedum (Sedum sarmentosum) delay H2O2-induced senescence in human diploid fibroblasts. J Med Food. 2009", "Journal of Medicinal Food"),  # 6
    pm("10771208", "Antiproliferative effects of alkaloids from Sedum sarmentosum on murine and human hepatoma cell lines. J Ethnopharmacol. 2000", "Journal of Ethnopharmacology"),  # 7
    pm("30668406", "The hepatoprotective effects of Sedum sarmentosum extract and its isolated major constituent through Nrf2 activation and NF-κB inhibition. Phytomedicine. 2018", "Phytomedicine"),  # 8
    pm("21120025", "Determination of total flavonoids in three Sedum crude drugs by UV-Vis spectrophotometry. Pharmacogn Mag. 2010", "Pharmacognosy Magazine", "PMC2992136"),  # 9
    pm("18164565", "Anti-inflammatory, anti-angiogenic and anti-nociceptive activities of Sedum sarmentosum extract. J Ethnopharmacol. 2007", "Journal of Ethnopharmacology"),  # 10
    pm("40570708", "Aqueous extract of Sedum sarmentosum (SS-Ex) promotes bone formation and linear bone growth in a calcium/vitamin D-deficient mouse model. Biomed Pharmacother. 2025", "Biomedicine & Pharmacotherapy"),  # 11
    pm("11939106", "Mineral content of culinary and medicinal plants cultivated by Hmong refugees living in Sacramento, California. Int J Food Sci Nutr. 2002", "International Journal of Food Sciences and Nutrition"),  # 12
    pm("31569538", "Next-Generation Genome Sequencing of Sedum plumbizincicola Sheds Light on the Structural Evolution of Plastid rRNA Operon and Phylogenetic Implications within Saxifragales. Plants (Basel). 2019", "Plants (Basel)", "PMC6843225"),  # 13
    pm("22701282", "Identification of four Sedum plant medicines by fourier transform infrared spectra. Pharmacogn Mag. 2012", "Pharmacognosy Magazine", "PMC3371430"),  # 14
    pm("23572321", "Simultaneous determination by HPLC of quercetin and kaempferol in three Sedum medicinal plants harvested in different seasons. J Chromatogr Sci. 2014", "Journal of Chromatographic Science"),  # 15
    pm("25345129", "[HPLC characteristic fingerprints of sedi linearis herba and sedi herba]. Zhong Yao Cai. 2014", "Zhong Yao Cai"),  # 16
    pm("14520500", "Taxonomic discrimination of higher plants by pyrolysis mass spectrometry. Plant Cell Rep. 2003", "Plant Cell Reports"),  # 17
    pm("25895381", "[AS-PCR amplification in identification of Sedum sarmentosum with its relative species]. Zhong Yao Cai. 2014", "Zhong Yao Cai"),  # 18
    pm("30593231", "[Effects of light intensity on growth, quality and antioxidant activities of Sedum sarmentosum]. Zhongguo Zhong Yao Za Zhi. 2018", "China Journal of Chinese Materia Medica"),  # 19
    pm("38114170", "[Effect of soil moisture on efficacy to eliminate dampness and relieve jaundice and flavonoid content of Sedum sarmentosum]. Zhongguo Zhong Yao Za Zhi. 2023", "China Journal of Chinese Materia Medica"),  # 20
    {"title": "Growth and Yield of Sedum sarmentosum as Affected by Planting Density in Cultivation System Using a Rice Nursery Tray (AGRIS 서지 레코드)",
     "url": "https://agris.fao.org/search/es/records/64724dd608fd68d54600c7cc", "publisher": "FAO AGRIS", "accessed": ACC},  # 21
    {"title": "Growth Characteristics as Influenced by Cutting Site and Planting Method in Autumn Field Cutting of Sedum sarmentosum (AGRIS 서지 레코드)",
     "url": "https://agris.fao.org/search/ru/records/64724dd608fd68d54600c84a", "publisher": "FAO AGRIS", "accessed": ACC},  # 22
    pm("24205047", "Complete chloroplast genome of Sedum sarmentosum and chloroplast genome evolution in Saxifragales. PLoS One. 2013", "PLoS One", "PMC3799696"),  # 23
    pm("26556327", "Development and Characterization of Polymorphic Microsatellite Markers for Sedum sarmentosum (Crassulaceae) and Their Cross-Species Transferability. Molecules. 2015", "Molecules", "PMC6332276"),  # 24
    pm("16548166", "[Determination of triterpene delta-amyrone in Sedum sarmentosum]. Zhongguo Zhong Yao Za Zhi. 2006", "China Journal of Chinese Materia Medica"),  # 25
    pm("31116450", "Simultaneous determination of eight flavonoids in Sedum sarmentosum Bunge from different areas by UHPLC with triple quadrupole MS/MS. Biomed Chromatogr. 2019", "Biomedical Chromatography"),  # 26
    pm("20838028", "Hepatoprotective effects of Sedum sarmentosum on D-galactosamine/lipopolysaccharide-induced murine fulminant hepatic failure. J Pharmacol Sci. 2010", "Journal of Pharmacological Sciences"),  # 27
    pm("39236049", "Regulatory mechanism of Sarmentosin and Quercetin on lipid accumulation in primary hepatocyte of GIFT tilapia (Oreochromis niloticus) with fatty liver. PLoS One. 2024", "PLoS One", "PMC11376590"),  # 28
    pm("17666842", "Bioactive constituents from Chinese natural medicines. XXIII. Absolute structures of new megastigmane glycosides, sedumosides A4, A5, A6, H, and I, and hepatoprotective megastigmanes from Sedum sarmentosum. Chem Pharm Bull. 2007", "Chemical & Pharmaceutical Bulletin"),  # 29
    pm("38788394", "Sarmentol H derived from Sedum sarmentosum Bunge directly targets FXR to mitigate cholestasis by recruiting SRC-1. Phytomedicine. 2024", "Phytomedicine"),  # 30
    pm("22554647", "Taraxerone enhances alcohol oxidation via increases of alcohol dehyderogenase (ADH) and acetaldehyde dehydrogenase (ALDH) activities and gene expressions. Food Chem Toxicol. 2012", "Food and Chemical Toxicology"),  # 31
    pm("22085682", "Tricin 7-glucoside protects against experimental cerebral ischemia by reduction of NF-κB and HMGB1 expression. Eur J Pharm Sci. 2011", "European Journal of Pharmaceutical Sciences"),  # 32
    pm("15577228", "Isolation of angiotensin converting enzyme (ACE) inhibitory flavonoids from Sedum sarmentosum. Biol Pharm Bull. 2004", "Biological & Pharmaceutical Bulletin"),  # 33
    pm("33741368", "Structure elucidation of arabinogalactoglucan isolated from Sedum sarmentosum Bunge and its inhibition on hepatocellular carcinoma cells in vitro. Int J Biol Macromol. 2021", "International Journal of Biological Macromolecules"),  # 34
    pm("18356580", "Antioxidant activity and cytotoxicity of methanol extracts from aerial parts of Korean salad plants. Biofactors. 2007", "BioFactors"),  # 35
    pm("42224857", "Potential herb-drug interaction risk of Sedum sarmentosum Bunge extract and cyclosporine A. Drug Metab Dispos. 2026", "Drug Metabolism and Disposition"),  # 36
    pm("19089828", "Immunosuppressive activity of the ethanol extract of Sedum sarmentosum and its fractions on specific antibody and cellular responses to ovalbumin in mice. Chem Biodivers. 2008", "Chemistry & Biodiversity"),  # 37
    pm("15242013", "Estrogenic effects of Sedum sarmentosum Bunge in ovariectomized rats. J Nutr Sci Vitaminol. 2004", "Journal of Nutritional Science and Vitaminology"),  # 38
    pm("36419035", "Retraction Note: Sedum sarmentosum Bunge extract ameliorates lipopolysaccharide- and D-galactosamine-induced acute liver injury by attenuating the hedgehog signaling pathway via regulation of miR-124 expression. BMC Complement Med Ther. 2022", "BMC Complementary Medicine and Therapies", "PMC9686039"),  # 39
    pm("37946908", "Retracted: Sedum sarmentosum Bunge Attenuates Drug-Induced Liver Injury via Nrf2 Signaling Pathway: An Experimental Verification Based on Network Pharmacology Prediction. J Healthc Eng. 2023", "Journal of Healthcare Engineering", "PMC10631994"),  # 40
    pm("28152607", "Two new megastigmanes from Chinese traditional medicinal plant Sedum sarmentosum. Nat Prod Res. 2017", "Natural Product Research"),  # 41
]
for i, s in enumerate(S, 1):
    s["n"] = i
SOURCES = [{"n": s["n"], "title": s["title"], "url": s["url"], "publisher": s["publisher"], "accessed": s["accessed"]} for s in S]

sections = [
    {"key": "overview", "title": "한눈에 보기", "body":
     "돌나물(Sedum sarmentosum Bunge)은 돌나물과(Crassulaceae)에 속하는 여러해살이 다육성 풀로, 영어로는 'stringy stonecrop' 또는 'golden moss'로도 불린다[2]. 중국·한국·일본 등 동아시아에 널리 퍼져 바위가 많은 산지와 교란된 땅에서 자라며, 가뭄과 척박한 흙을 잘 견딘다[2]. 한국에서는 샐러드와 김치의 한 종류에 넣어 먹는 대중적인 푸른 채소이다[5][6].\n\n"
     "식품의약품안전처 「식품원료 목록」에서 돌나물은 식품에 사용할 수 있는 원료(사용가능)이며, 사용 조건은 '사용가능부위 : 순'이다[1]. 같은 목록의 원료명은 '돌나물순' 하나이고, 돈나물·돋나물이라는 이름과 영문명 Stonecrop이 함께 적혀 있다[1]. 건강기능식품 고시형 원료의 원재료로 쓰인다는 기록은 확인하지 못함.\n\n"
     "중국에서는 같은 식물을 생약 'Sedi Herba'로 써 왔고, 중국약전에 실려 간·담도 질환 치료에 임상적으로 쓰인다[8][9][15]. 지금까지 이 종에서 휘발성 기름·플라보노이드·테르페노이드·페놀류·배당체 등 174종의 성분이 분리·동정되었다[3]. 간 보호 효과에 관한 동물·세포 연구가 많지만, 사람을 대상으로 한 효능 근거는 이 자료에서 확인하지 못함."},
    {"key": "history", "title": "역사", "body":
     "돌나물 전초는 중국과 한국에서 만성 바이러스성 간염 치료에 전통적으로 쓰여 왔다[7]. 동양 여러 나라의 산비탈에 널리 자라는 이 풀은 일부 염증성 질환 치료에도 전통적으로 쓰였다[10]. 간염·황달 같은 간 질환과 이질 같은 위장관 감염에도 쓰였다고 정리되어 있다[2].\n\n"
     "중국약전(2010)에 수재되었고, 급성·만성 간염에 효과가 있다고 알려져 여러 제제가 개발되었다[9]. 2026년 종설은 돌나물을 주원료로 한 중국 중성약(정해진 처방의 완제 한약) 10종이 간 질환 치료용으로 개발되었다고 정리했다[3]. 중국 문헌은 효소 수치를 낮추고 간을 보호하는 효과 때문에 주로 여러 유형의 간염에 쓴다고 적고 있다[4].\n\n"
     "한국에서는 돌나물을 간 질환에 전통적으로 써 왔고, 비타민 C와 칼슘이 풍부한 식물로 소개된다[11]. 식용으로는 샐러드와 김치의 재료로 먹으며, 아시아에서 여러 세기 동안 민간 약초로도 쓰였다[5]. 미국 캘리포니아로 이주한 라오스 몽족 공동체는 돌나물 근연 식물(Sedum aff. sarmentosum)을 다른 허브와 함께 닭고기 양념으로 썼다[12]."},
    {"key": "biology", "title": "식물학적 특징", "body":
     "돌나물은 돌나물과의 여러해살이 초본이며, 잎은 홑잎으로 세 장씩 돌려나고 다육질이다[2]. 잎 모양은 피침형에서 거꿀피침형이고, 가장자리는 밋밋하며 끝이 뾰족하다[2]. 햇빛이 잘 드는 곳을 좋아하지만 반그늘에서도 살 수 있고, 가물고 척박한 흙에서도 자란다[2]. 적응력이 강하고 빨리 번식해 생태 복원과 도시 녹화 소재로도 주목받는다[2].\n\n"
     "돌나물속(Sedum)은 돌나물과(범의귀목, Saxifragales)에 속하며 약 470종이 인정되는 큰 속이다[13]. 돌나물은 동양 여러 나라의 산비탈에 널리 분포하는 여러해살이풀로 소개된다[10]. 신선한 돌나물은 수분이 많고 조직이 쉽게 상해 보관 기간이 매우 짧다[5].\n\n"
     "지상부의 플라보노이드 함량은 계절에 따라 달라져, 중국 후베이성 시료에서는 꽃이 피는 4월에 가장 많고 6–7월에 줄었다[9]. 같은 연구에서 후베이성 서부 시료가 동부 시료보다 대체로 총플라보노이드가 많았다[9]. 퀘르세틴·캠페롤 정량 연구도 4월 말–5월 초 만개기를 가장 좋은 수확 시기로 제안했다[15]."},
    {"key": "related_species", "title": "가까운 종", "body":
     "중국에서는 돌나물(S. sarmentosum)과 S. lineare, S. erythrostictum, S. aizoon 네 가지 돌나물속 식물이 약재로 쓰이는데, 생김새가 매우 비슷해 서로 혼동되기 쉽다[14]. 이 네 약재는 70% 에탄올 추출물의 적외선(FT-IR) 스펙트럼 차이로 구별할 수 있었다[14]. 이 자료는 같은 속 다른 종과 구별하는 방법만 다루며, 다른 종의 성분·용도 자료는 이 문서에 섞지 않았다[14].\n\n"
     "S. lineare와 돌나물의 HPLC 지문은 공통 피크가 4개였지만 서로 구별할 수 있었다[16]. 엽록체 trnL–trnF 염기서열로 설계한 대립유전자 특이 PCR(AS-PCR) 프라이머는 돌나물에서만 300 bp와 500 bp 조각을 증폭해 혼동 종과 구별했다[18]. 한국 식물 잎을 열분해 질량분석(PyMS)으로 비교한 연구는 기린초(S. kamtschaticum)·섬기린초(S. takesimense)·돌나물을 서로 구별해 냈다[17].\n\n"
     "미토콘드리아 유전체 26종으로 그린 계통수로 돌나물과 안에서 돌나물의 계통적 위치가 새로 정리되었다[2]. 돌나물에서 개발한 SSR 표지 14개는 다른 돌나물속 식물에서도 잘 증폭되어, 전이율이 S. lineare 85.7%에서 S. ellacombianum 64.3%였다[24]."},
    {"key": "cultivation", "title": "재배와 생산", "body":
     "국내에서는 무가온 비닐하우스에서 벼 육묘상자를 이용해 돌나물을 기르는 방법이 연구되었다[21]. 이 연구는 완주·금산 두 지역 계통의 삽수를 상자당 40·60·80개체로 심어 비교했고, 완주 계통이 더 알맞고 상자당 40개체가 적당하다고 보고했다[21]. 가을 노지 삽목 연구에서는 줄기 끝쪽 삽수가 생육과 수량에 유리했다[22].\n\n"
     "중국의 재배 실험에서는 전광의 60% 이상 빛이 수량과 품질에 가장 알맞았고, 전광 60%에서 수량과 총플라보노이드·총페놀이 가장 많았다[19]. 퀘르세틴과 이소람네틴은 전광(100%)에서 가장 많았고, 캠페롤은 빛 세기에 따라 크게 다르지 않았다[19]. 흙 수분 75–80%에서 기른 돌나물 달임액이 황달 생쥐의 간 기능 지표를 가장 잘 낮췄고, 수분 95–100%에서 효과가 가장 낮았다[20].\n\n"
     "통계청·농림축산식품부의 돌나물 재배면적·생산량 통계는 확인하지 못함. 지리적 표시 등록이나 품목 협회도 확인하지 못함."},
    {"key": "processing", "title": "가공과 이용", "body":
     "돌나물은 수분이 많고 조직이 쉽게 상해 저장 기간이 매우 짧아, 활용을 늘리려고 주스와 젤리 같은 가공품이 시도되었다[5]. 동결건조한 돌나물 잎 가루를 쌀가루 대신 넣은 백설기(설기떡)는 조단백·무기질·식이섬유와 총폴리페놀이 늘었고, 쌀가루의 10%를 바꿨을 때 관능 품질이 가장 좋았다[5]. 20%를 넣으면 돌나물 맛(약간 쓴맛)이 너무 강해 관능 점수가 가장 낮았다[5].\n\n"
     "돌나물 추출물은 여러 간 질환 치료에 임상에서 널리 쓰인다고 보고된다[36]. 돌나물을 주원료로 한 중성약 10종이 간 질환용으로 개발되었다[3]. 약재의 품질은 총플라보노이드 비색법, 퀘르세틴·캠페롤 HPLC, 플라보노이드 8종 UHPLC-MS/MS, δ-아미론 HPLC-ELSD 같은 방법으로 평가되어 왔다[9][15][25][26].\n\n"
     "돌나물의 활성 성분인 사르멘토신과 퀘르세틴은 고지방 사료로 지방간이 생긴 틸라피아 간세포에서 지방 축적을 줄여, 양식어 지방간 대책으로도 연구된다[28]. 식약처 「식품 등의 생산실적」에서 돌나물 제품 생산 통계는 확인하지 못함."},
    {"key": "genetics", "title": "유전체와 육종", "body":
     "2013년 해독된 돌나물 엽록체 유전체는 150,448 bp이며, 대단일복사 영역 82,212 bp, 소단일복사 영역 16,670 bp, 역반복 영역 25,783 bp 한 쌍으로 이루어진다[23]. 이 유전체에는 고유 유전자 131개가 있고, 그중 18개가 역반복 영역에서 중복된다[23]. 범의귀목 비교에서 돌나물 엽록체 유전체는 염기서열 진화가 빠른 편이었다[23].\n\n"
     "2026년에는 PacBio HiFi 자료로 미토콘드리아 유전체가 처음 조립되었는데, 156,727 bp 원형 분자로 GC 함량 45.30%, 단백질 암호 유전자 30개·tRNA 8개·rRNA 2개를 담고 있다[2]. 같은 연구의 엽록체 유전체는 대단일복사 81,798 bp, 소단일복사 16,671 bp, 역반복 25,778 bp(각각)로 나타났다[2]. 미토콘드리아에서 RNA 편집 후보 자리 617개와 엽록체에서 옮겨 온 DNA 조각 18개가 확인되었다[2].\n\n"
     "돌나물 개체 48주에서 다형성 SSR 표지 14개가 개발되었고, 좌위당 대립유전자는 3–15개였다[24]. 핵 유전체 크기와 품종 육성 기록은 확인하지 못함."},
    {"key": "safety", "title": "안전성", "body":
     "식약처 「식품원료 목록」에서 돌나물은 순을 쓰는 사용가능 원료로 올라 있다[1]. 돌나물에 대한 식약처 등 국내 공공기관의 알레르기·잔류농약·독성 성분 안내는 확인하지 못함. 돌나물만을 다룬 공식 세척·섭취 지침도 확인하지 못함.\n\n"
     "쥐에게 돌나물 추출물 600 mg/kg을 먹이고 1시간 뒤 면역억제제 사이클로스포린 A를 주자, 혈중 최고농도와 48시간 곡선하면적이 각각 150%, 220% 늘었다[36]. 추출물과 그 성분이 시험관에서 CYP3A 활성을 억제했고, 연구진은 두 약을 함께 쓸 때 추가 주의가 필요하다고 결론지었다[36]. 에탄올 추출물을 생쥐 복강에 주사하면 항원 특이 항체와 비장세포 증식이 용량에 따라 억제되었다[37]. 난소를 떼어 낸 쥐 연구에서는 추출물 분획이 에스트로겐 유사 작용을 보였다[38].\n\n"
     "이런 결과는 대부분 고농도 추출물을 쓴 동물·세포 실험이며, 나물로 먹는 양에 그대로 적용할 수는 없다[36][37][38]. 돌나물 추출물의 간 보호 효과를 다룬 논문 가운데 2편은 학술지에서 철회되었으므로 인용할 때 주의가 필요하다[39][40]. 면역억제제 등 약을 먹는 사람이 추출물 제품을 함께 쓰려면 전문가와 상의하는 것이 좋다[36]."},
]

compounds = [
    {"name": "Sarmentosin", "name_ko": "사르멘토신", "class": "니트릴 배당체", "role": "marker", "part": "전초",
     "content_text": "이 종 원물의 함량 수치는 확인하지 못함", "activity_ko": "돌나물의 주요 활성 성분으로 소개되며, 틸라피아 지방간 간세포에서 지방 분해 작용(10 μM)을 보였다[28]; 사르멘토신을 함유한 추출물이 생쥐 전격성 간부전을 막았다[27]",
     "source": [27, 28, 9]},
    {"name": "Total flavonoids", "name_ko": "총플라보노이드(루틴 당량)", "class": "플라보노이드", "role": "marker", "part": "전초(건조 약재)",
     "content_text": "0.64–2.52%(후베이성 3개 산지·채집 월별); 반복성 시험 시료 평균 1.03%[9]", "activity_ko": "간 보호 효과와 관련된 성분군으로 보아 품질 지표로 측정됨[9]", "source": [9]},
    {"name": "Quercetin", "name_ko": "퀘르세틴", "class": "플라보놀", "role": "marker", "part": "전초",
     "content_text": "HPLC 정량 대상(함량 수치는 초록에 없어 확인하지 못함)[15]; 전광(100%) 재배에서 가장 많음[19]", "activity_ko": "분리 성분 가운데 ABTS 라디칼 소거력이 가장 높았다(Trolox 0.67 μM 당량)[41]",
     "source": [15, 19, 41]},
    {"name": "Kaempferol", "name_ko": "캠페롤", "class": "플라보놀", "role": "marker", "part": "전초",
     "content_text": "HPLC 정량 대상(함량 수치는 초록에 없어 확인하지 못함)[15]; 빛 세기에 따른 차이는 유의하지 않음[19]", "activity_ko": "흙 수분 처리별 달임액에서 MDA와 음의 상관을 보임[20]", "source": [15, 19, 20]},
    {"name": "Isorhamnetin", "name_ko": "이소람네틴", "class": "플라보놀", "role": "bioactive", "part": "전초",
     "content_text": "전광(100%) 재배에서 가장 많음(수치는 초록에 없음)[19]", "activity_ko": "함량이 생쥐 간 TNF-α 수치와 유의한 음의 상관을 보임[20]", "source": [19, 20]},
    {"name": "delta-Amyrone", "name_ko": "δ-아미론", "class": "트리테르펜", "role": "marker", "part": "전초",
     "content_text": "HPLC-ELSD 정량법 확립(함량 수치는 초록에 없음)[25]", "activity_ko": "저극성 추출물의 주성분으로 분리되어 D-갈락토사민 손상 간세포 생존율을 10·20 μM에서 58.2%·69.5%로 높였다(Nrf2 활성화·NF-κB 억제)[8]",
     "source": [8, 25]},
    {"name": "Taraxerone", "name_ko": "타락세론", "class": "트리테르펜", "role": "bioactive", "part": "전초",
     "content_text": "분리 순도 96.383%[31]", "activity_ko": "ADH·ALDH 활성을 높이고 생쥐 혈중 알코올을 약 20–67%, 아세트알데히드를 약 7–57% 낮춤[31]", "source": [31]},
    {"name": "Tricin 7-glucoside", "name_ko": "트리신 7-글루코사이드", "class": "플라본 배당체", "role": "bioactive", "part": "전초",
     "content_text": "돌나물의 주요 생리활성 성분으로 보고(함량 수치 없음)[32]", "activity_ko": "쥐 뇌허혈–재관류 모델에서 50 mg/kg 넘는 용량으로 신경 보호 효과[32]", "source": [32]},
    {"name": "Sedumoside F1", "name_ko": "세두모사이드 F1", "class": "메가스티그만 배당체", "role": "bioactive", "part": "전초 열수 추출물",
     "content_text": "함량 수치는 확인하지 못함", "activity_ko": "생쥐 초대배양 간세포의 D-갈락토사민 독성을 억제(IC50 47 μM)[29]", "source": [29]},
    {"name": "Sarmentol H", "name_ko": "사르멘톨 H", "class": "노르세스퀴테르페노이드", "role": "bioactive", "part": "전초",
     "content_text": "함량 수치는 확인하지 못함", "activity_ko": "FXR에 리간드로 결합(Kd 2.55 μmol/L)해 생쥐 담즙정체를 완화[30]", "source": [30]},
    {"name": "Quercetin 3-O-alpha-(6'''-caffeoylglucosyl-beta-1,2-rhamnoside)", "name_ko": "퀘르세틴 카페오일글루코실람노사이드(신규 플라보노이드)", "class": "플라보놀 배당체", "role": "bioactive", "part": "지상부 에틸아세테이트 가용 분획",
     "content_text": "함량 수치는 확인하지 못함", "activity_ko": "ACE 억제, IC50 158.9 ± 11.1(원문 단위 'microgM')[33]", "source": [33]},
    {"name": "Arabinogalactoglucan", "name_ko": "아라비노갈락토글루칸 다당(SSWP)", "class": "중성 다당", "role": "bioactive", "part": "전초",
     "content_text": "분자량 21.5 kDa, 아라비노스:글루코스:갈락토스 몰비 2.4:1:1.8[34]", "activity_ko": "50 μg/mL에서 간암세포(Huh-7) 증식을 48.9% 억제(시험관)[34]", "source": [34]},
    {"name": "Polyphenols", "name_ko": "총페놀", "class": "페놀류", "role": "bioactive", "part": "지상부 메탄올 추출물",
     "content_text": "9.1 mg/100 g(생체중)[35]", "activity_ko": "한국 샐러드 식물 11종 가운데 총페놀이 네 번째로 많았음[35]", "source": [35]},
    {"name": "Dietary fiber", "name_ko": "식이섬유", "class": "탄수화물", "role": "nutrient", "part": "잎(동결건조 분말)",
     "content_text": "23.11 g/100 g(건조중량)[5]", "activity_ko": "떡에 넣으면 보수력 증가의 원인이 됨[5]", "source": [5]},
]

assays = [
    {"role": "literature", "compound": "Total flavonoids", "compound_ko": "총플라보노이드(루틴 당량)", "part": "전초(건조 약재, 20메시 분말)",
     "content": "0.64–2.52%(후베이성 젠스·이창·우한, 4·6–7·8–9월 채집); 반복성 시료(젠스 2006-06-28) 평균 1.03%[9]",
     "method": "UV-Vis 분광광도법(아질산나트륨–질산알루미늄 발색)",
     "conditions": {"instrument": "757 CRT UV–Vis 분광광도계(Lengguang), KQ-500E 초음파기(500 W, 40 kHz)", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "",
                    "detection": "500 nm", "injection": "",
                    "sample_prep": "분말 1.0 g + 석유에테르 50 mL로 초음파 40분 2회 탈지 → 70% 에탄올 100 mL, 55 °C 초음파 90분(3 × 30분) → 여과 후 100 mL 정용; 추출액 4 mL + 5% NaNO2 0.40 mL(6분) + 10% Al(NO3)3 0.4 mL(6분) + 4% NaOH 4 mL → 10 mL 정용, 15분 방치 후 측정(발색 후 2시간 안에 측정)",
                    "standard": "루틴 200.0 mg/L(70% 에탄올)", "linearity": "4–80 μg/mL, 상관 > 0.999, A = 12.155C + 0.005", "lod": "", "loq": "",
                    "recovery": "루틴 10 mg 첨가, 평균 93.8%(RSD 2.80%, n = 6)"},
     "rationale": "간 보호·ALT 저하 활성이 배당체와 플라보노이드가 많은 물·부탄올 분획에 있어, 총플라보노이드 측정이 약재 품질을 어느 정도 반영한다고 보았다[9]. 정밀도 RSD 0.09%(n = 5), 반복성 RSD < 2.7%(n = 6). 식용 부위(순)가 아니라 건조 약재 전체를 분석한 값이다.",
     "source": [9], "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC2992136/", "source_kind": "paper"},
    {"role": "literature", "compound": "Quercetin", "compound_ko": "퀘르세틴·캠페롤 동시 정량", "part": "전초(약재 Sedi Herba)",
     "content": "",
     "method": "HPLC-UV",
     "conditions": {"instrument": "", "column": "YMC-pack ODS-A, 250 × 4.6 mm, 5 µm", "mobile_phase": "메탄올–0.4% 인산(47:53)", "gradient": "등용매", "flow": "1.0 mL/min", "temp": "35 °C",
                    "detection": "UV 360 nm", "injection": "", "sample_prep": "", "standard": "퀘르세틴·캠페롤",
                    "linearity": "퀘르세틴 0.01–0.62 µg, 캠페롤 0.02–0.78 µg", "lod": "", "loq": "",
                    "recovery": "퀘르세틴 99.72%(RSD 1.63%), 캠페롤 99.50%(RSD 1.16%)"},
     "rationale": "돌나물 등 돌나물속 약재 3종의 품질 관리용으로 개발되었고, 계절별 시료 비교로 만개기(4월 말–5월 초)를 최적 수확기로 제안했다[15]. 전문 확인 못함 — 조건은 초록에 적힌 값만 옮겼고 함량 수치는 비워 둠.",
     "source": [15], "url": "https://pubmed.ncbi.nlm.nih.gov/23572321/", "source_kind": "paper"},
    {"role": "literature", "compound": "Flavonoids (8 compounds)", "compound_ko": "플라보노이드 8종 동시 정량", "part": "전초(중국 11개 지역 33개 배치)",
     "content": "",
     "method": "UHPLC-ESI-MS/MS(삼중 사중극자)",
     "conditions": {"instrument": "", "column": "Agilent Zorbax SB C18, 50 × 2.1 mm, 5 μm", "mobile_phase": "", "gradient": "4분 안에 8성분 분리", "flow": "", "temp": "",
                    "detection": "ESI 삼중 사중극자 MS/MS", "injection": "", "sample_prep": "", "standard": "",
                    "linearity": "r ≥ 0.9988", "lod": "", "loq": "", "recovery": "95.91–100.68%(RSD 1.50–3.80%)"},
     "rationale": "총플라보노이드를 돌나물의 주요 약리 활성 성분군으로 보고, 산지별 자원 평가를 위해 8종을 동시에 정량했다(정밀도 RSD ≤ 2.68%)[26]. 전문 확인 못함 — 성분 이름·이동상·함량은 비워 둠.",
     "source": [26], "url": "https://pubmed.ncbi.nlm.nih.gov/31116450/", "source_kind": "paper"},
    {"role": "literature", "compound": "delta-Amyrone", "compound_ko": "δ-아미론", "part": "전초",
     "content": "",
     "method": "HPLC-ELSD",
     "conditions": {"instrument": "", "column": "Zorbax Sil(순상 실리카)", "mobile_phase": "디클로로메탄–메탄올(99:1)", "gradient": "등용매", "flow": "0.5 mL/min", "temp": "",
                    "detection": "ELSD, 드리프트관 100 °C, 분무 질소 3.0 L/min", "injection": "", "sample_prep": "", "standard": "δ-아미론",
                    "linearity": "2.12–10.6 µg", "lod": "", "loq": "", "recovery": "평균 100.5%"},
     "rationale": "δ-아미론은 저극성 추출물의 HPLC 주 피크로 분리되어 간 보호 활성 성분으로 확인되었다[8][25]. 전문 확인 못함 — 조건은 초록에 적힌 값만 옮김.",
     "source": [25, 8], "url": "https://pubmed.ncbi.nlm.nih.gov/16548166/", "source_kind": "paper"},
]

nutrients = [
    {"form": "돌나물 잎(일반 가식부) 동결건조 분말", "basis": "건조중량 100 g",
     "items": [{"name": "식이섬유", "value": 23.11, "unit": "g"}], "source": [5]},
]

d = {
    "slug": "sedum-sarmentosum",
    "name_ko": "돌나물",
    "name_en": "Stonecrop (stringy stonecrop)",
    "scientific_name": "Sedum sarmentosum Bunge",
    "aliases": ["돈나물", "돋나물", "돌나물순", "Stonecrop", "stringy stonecrop", "golden moss", "Sedi Herba"],
    "sections": sections,
    "compounds": compounds,
    "markers": [],
    "assays": assays,
    "nutrients": nutrients,
    "production": [],
    "world": [],
    "gi": [],
    "orgs": [],
    "sources": SOURCES,
}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
print("written", len(SOURCES))
