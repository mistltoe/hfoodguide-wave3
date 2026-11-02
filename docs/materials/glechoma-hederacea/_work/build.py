import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
A = "2026-11-02"
def pm(n, title, pmid, pub): return {"n": n, "title": title, "url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/", "publisher": pub, "accessed": A}
def pmc(n, title, pmcid, pub): return {"n": n, "title": title, "url": f"https://pmc.ncbi.nlm.nih.gov/articles/{pmcid}/", "publisher": pub, "accessed": A}
sources = [
 {"n": 1, "title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 병꽃풀(Glechoma hederacea L.)·긴병꽃풀(Glechoma grandis) 항목", "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
 pmc(2, "Optimization of the Extraction Procedure for the Phenolic-Rich Glechoma hederacea L. Herb and Evaluation of Its Cytotoxic and Antioxidant Potential. Plants (Basel). 2022", "PMC9460379", "MDPI (PMC)"),
 pmc(3, "Comprehensive Study of Traditional Plant Ground Ivy (Glechoma hederacea L.) Grown in Croatia in Terms of Nutritional and Bioactive Composition. Foods. 2022", "PMC8909519", "MDPI (PMC)"),
 pmc(4, "Wild-Grown and Cultivated Glechoma hederacea L.: Chemical Composition and Potential for Cultivation in Organic Farming Conditions. Plants (Basel). 2022", "PMC8949430", "MDPI (PMC)"),
 pmc(5, "New Aspect of Composition and Biological Properties of Glechoma hederacea L. Herb: Detailed Phytochemical Analysis and Evaluation of Antioxidant, Anticoagulant Activity and Toxicity in Selected Human Cells and Plasma In Vitro. Nutrients. 2023", "PMC10096585", "MDPI (PMC)"),
 pmc(6, "rDNA Loci Evolution in the Genus Glechoma (Lamiaceae). PLoS One. 2016", "PMC5117774", "PLoS (PMC)"),
 pm(7, "Enzyme variation and inheritance in Glechoma hederacea (Lamiaceae), a diploidized tetraploid. Hereditas. 2000", "11075518", "PubMed"),
 pm(8, "Rust on Ground-Ivy Found for the First Time in North America. Plant Dis. 2000", "30841261", "PubMed"),
 pmc(9, "The Tn antigen-specific lectin from ground ivy is an insecticidal protein with an unusual physiology. Plant Physiol. 2003", "PMC167072", "American Society of Plant Biologists (PMC)"),
 pm(10, "Leaves of the Lamiaceae species Glechoma hederacea (ground ivy) contain a lectin that is structurally and evolutionary related to the legume lectins. Plant J. 2003", "12535343", "PubMed"),
 pm(11, "Simultaneous Quantification of Ursolic and Oleanolic Acids in Glechoma hederacea and Glechoma hirsuta by UPLC/MS/MS. Planta Med. 2021", "33450770", "PubMed"),
 pm(12, "Inhibitory effects of ursolic and oleanolic acid on skin tumor promotion by 12-O-tetradecanoylphorbol-13-acetate. Cancer Lett. 1986", "3802058", "PubMed"),
 pm(13, "Phytochemical profile of hot water extract of Glechoma hederacea and its antioxidant, and anti-inflammatory activities. Life Sci. 2019", "31152813", "PubMed"),
 pm(14, "Glechoma hederacea extracts attenuate cholestatic liver injury in a bile duct-ligated rat model. J Ethnopharmacol. 2017", "28416441", "PubMed"),
 pmc(15, "Protective effect of Glechoma hederacea extract against gallstone formation in rodent models. BMC Complement Med Ther. 2021", "PMC8278774", "BioMed Central (PMC)"),
 pm(16, "Clinical evaluation of the depigmenting effect of Glechoma Hederacea extract by topical treatment for 8 weeks on UV-induced pigmentation in Asian skin. Eur J Dermatol. 2011", "21411411", "PubMed"),
 pm(17, "Pollen limitation and distance-dependent fecundity in females of the clonal gynodioecious herb Glechoma hederacea (Lamiaceae). Oecologia. 1990", "22160110", "PubMed"),
 pm(18, "Stolon growth and branching in Glechoma hederacea L.: an application of a plastochron index. New Phytol. 1992", "33874215", "PubMed"),
 pm(19, "An analysis of the costs and benefits of physiological integration between ramets in the clonal perennial herb Glechoma hederacea. Oecologia. 1987", "28311525", "PubMed"),
 pm(20, "Occurrence of free and esterified lipoxygenase products in leaves of Glechoma hederacea L. and other Labiatae. Eur J Biochem. 1989", "2598926", "PubMed"),
 pm(21, "Isolation and characterization of 9-hydroxy-10-trans,12-cis-octadecadienoic acid, a novel regulator of platelet adenylate cyclase from Glechoma hederacea L. Labiatae. Eur J Biochem. 1987", "3691528", "PubMed"),
 pm(22, "Glycosides from whole plants of Glechoma hederacea L. J Nat Med. 2008", "18553179", "PubMed"),
 pm(23, "New sesquiterpene lactones from Glechoma hederacea L. and their cytotoxic effects on human cancer cell lines. Planta Med. 2011", "21243589", "PubMed"),
 pm(24, "Glechoma hederacea: A Comprehensive Insight into the Botanical Specification, Traditional Uses, Phytochemistry, Nutritional Value, Pharmacology, and Non-medicinal Applications. Planta Med. 2026", "42173111", "PubMed"),
 pm(25, "Antioxidant effects of Glechoma hederacea as a food additive. Nat Prod Commun. 2010", "20184023", "PubMed"),
 pm(26, "Development of new chocolate formulations by incorporating spray-dried and liposomal encapsulates of ground ivy (Glechoma hederacea L.) polyphenolic extract. Food Chem. 2025", "40112723", "PubMed"),
 pmc(27, "Development, Characterization and Incorporation of Alginate-Plant Protein Covered Liposomes Containing Ground Ivy (Glechoma hederacea L.) Extract into Candies. Foods. 2022", "PMC9222263", "MDPI (PMC)"),
 pm(28, "Biological activity of Glechoma hederacea. Fitoterapia. 2002", "12490241", "PubMed"),
 pm(29, "Anti-inflammatory activity of constituents from Glechoma hederacea var. longituba. Bioorg Med Chem Lett. 2011", "21530248", "PubMed"),
 pm(30, "Chemical evidence for potent xanthine oxidase inhibitory activity of Glechoma hederacea var. grandis leaves (kakidoushi-cha). J Nutr Sci Vitaminol. 2013", "24477256", "PubMed"),
 pmc(31, "Weed Detection in Perennial Ryegrass With Deep Learning Convolutional Neural Network. Front Plant Sci. 2019", "PMC6836412", "Frontiers (PMC)"),
 pmc(32, "Bioprospecting of six polyphenol-rich Mediterranean wild edible plants reveals antioxidant, antibiofilm and bactericidal properties against Methicillin resistant Staphylococcus aureus. Sci Rep. 2025", "PMC12328800", "Springer Nature (PMC)"),
 pm(33, "Culinary and nutritional value of edible wild plants from northern Spain rich in phenolic compounds with potential health benefits. Food Funct. 2020", "33034610", "PubMed"),
 pm(34, "Phytochemical composition and bioactive effects of ethyl acetate fraction extract (EAFE) of Glechoma hederacea L. J Food Biochem. 2021", "34121206", "PubMed"),
]

S = {}
S["overview"] = ("병꽃풀(Glechoma hederacea L.)은 꿀풀과(Lamiaceae)의 여러해살이풀로, 영어로는 ground ivy라 부르며 마디에서 뿌리를 내리며 기는 줄기와 파랑~보라색 꽃, 둥근 잎을 가진다[8]. "
 "유라시아가 원산이고 북아메리카에는 들어가 널리 퍼졌다[8].\n\n"
 "식품의약품안전처 「식품원료 목록」에서 병꽃풀은 식품에 사용할 수 있는 원료(사용가능)이며, 사용 조건은 '사용가능부위 : 순, 잎'이다[1]. "
 "같은 목록에는 병꽃풀·병꽃풀순·병꽃풀잎의 3개 원료명이 올라 있고, 연전초라는 이름도 함께 적혀 있다[1]. "
 "건강기능식품 고시형 원료의 원재료로 쓰인다는 기록은 목록 자료에서 확인하지 못함.\n\n"
 "말린 지상부에는 로즈마린산·클로로겐산 같은 페놀산과 루틴·아피제닌 배당체 같은 플라보노이드가 많고, 물로 우린 추출물에서 로즈마린산은 건조 식물 1 g당 4.28–4.89 mg이었다[2][5]. "
 "잎에는 우르솔산이 건조중량 1 g당 7.1–7.5 mg 들어 있다[11]. "
 "열수 추출물에서는 로즈마린산·클로로겐산·카페산·루틴·제니스틴·페룰산이 가장 많다는 보고가 있으나, 다른 연구의 말린 풀 추출물에서는 제니스틴 같은 이소플라본이 검출되지 않았다[2][13]. "
 "유럽에서는 영국의 'gill tea'처럼 차로 마시거나 향신료·맥주의 쓴맛 재료로 써 왔다[2].")
S["history"] = ("병꽃풀은 아시아와 유럽에서 전통적으로 위염·기관지염·이명·설사·담석·간 질환에 쓰였고, 추출물은 여러 피부병에 바르기도 했다[2]. "
 "영국에서는 18세기부터 'gill tea'라는 차로 마셨고, 일부 양조장은 지금도 맥주의 쓴맛을 내는 데 병꽃풀을 쓴다[2]. "
 "유럽에서는 고대부터 치료 기록이 있으며, 지금도 위장·간담·호흡기·피부 질환에 민간에서 쓰인다고 정리되어 있다[24]. "
 "중국 전통의학에서는 담석·부종·종기·당뇨·염증·황달 환자에게 처방되어 왔다[14].\n\n"
 "음식 재료로서의 쓰임도 이어져 왔다[5][32]. "
 "강한 향과 쓰고 매운맛 때문에 말린 지상부는 향신료로, 생잎은 다져서 달걀·버터·치즈·감자 요리 등에 넣는다고 소개된다[5]. "
 "이탈리아에서는 예로부터 음식으로 먹어 온 야생 식용식물 가운데 하나로 다뤄졌고, 스페인 북서부의 야생 식용식물 검토에도 포함되었다[32][33]. "
 "한국에서 병꽃풀(G. hederacea)을 먹어 온 역사나 고문헌 기록은 이번 조사에서 확인하지 못함.")
S["biology"] = ("병꽃풀은 영양이 풍부하고 그늘진 풀밭에 주로 자라며, 숲과 사람 손이 탄 곳에서도 자란다[8]. "
 "기는줄기(포복경)로 번지는 클론 식물로, 영국 실험에서 새 마디포기(라멧)가 평균 3.5일마다 하나씩 생겼고 줄기는 하루 1.9–2.9 cm씩 자랐다[18]. "
 "줄기로 이어진 포기 사이에서는 양분이 주로 끝 쪽(어린 포기 쪽)으로 옮겨 가며, 자원이 많은 곳의 포기가 부족한 곳의 포기를 거의 비용 없이 돕는다[19].\n\n"
 "암꽃만 피는 포기와 양성화 포기가 함께 있는 자웅이주성(gynodioecy) 식물이다[17]. "
 "자연 집단 조사에서 가장 흔한 꽃가루 매개자는 뒤영벌이었고, 꽃가루가 옮겨 간 평균 거리는 열매 맺음 기준 5.9 m로 추정되었다[17]. "
 "봄에는 꽃줄기가 서서 자라며, 라트비아 재배 시험에서 꽃줄기 평균 높이는 17.6 cm, 꽃이 진 뒤 다시 자란 줄기는 평균 10.1 cm였다[4]. "
 "잎에는 콩과 렉틴과 닮은 렉틴(Gleheda)이 있는데, 어떤 클론에서는 잎 단백질의 3분의 1이 넘지만 같은 곳의 다른 클론에서는 검출되지 않았다[9]. "
 "이 렉틴은 잎의 울타리조직 한 층에만 몰려 있고, 콜로라도감자잎벌레 애벌레에 강한 살충 작용을 보였다[9]. "
 "전초에서는 리그난 배당체와 아피제닌 7-O-네오헤스페리도사이드 같은 배당체, 그리고 새 세스퀴테르펜 락톤 3종이 분리되었다[22][23].")
S["related_species"] = ("병꽃풀속(Glechoma)은 유라시아에 7종이 있으며 두 무리로 나뉜다[6]. "
 "유럽 무리는 병꽃풀(G. hederacea)·G. hirsuta·G. sardoa이고, 아시아 무리는 G. longituba·G. grandis 등 동아시아·중국 종으로 이루어진다[6]. "
 "ITS 계통 분석에서 아시아 종은 뚜렷이 구분되었지만, 유럽의 병꽃풀과 G. hirsuta는 서로 섞여 형태처럼 유전적으로도 가깝다[6]. "
 "잎의 우르솔산 함량은 병꽃풀과 G. hirsuta가 비슷해 두 종을 같은 원료로 쓸 수 있다는 결과도 있다[11].\n\n"
 "국내 「식품원료 목록」에는 긴병꽃풀(Glechoma grandis, 이명 G. hederacea var. longituba)이 병꽃풀과 따로 올라 있고, 사용 부위도 '싹'으로 다르다[1]. "
 "국내 연구에서 'G. hederacea var. longituba'로 쓴 시료나 일본의 '가키도시차(var. grandis 잎)'는 이 목록 기준으로 긴병꽃풀 쪽 자료이므로, 이 글에서는 병꽃풀 자료와 섞지 않았다[1][29][30]. "
 "var. longituba에서는 로즈마린산 유사체가, var. grandis 잎차에서는 아피제닌·루테올린이 주요 활성 성분으로 보고되었다[29][30].")
S["cultivation"] = ("유럽에서는 병꽃풀 원료를 아직 주로 야생에서 채취하며, 상업용 품종은 없다[4]. "
 "라트비아에서는 야생 3개 계통을 유기농 시험포에 30 × 75 cm 간격으로 심어 재배 가능성을 시험했다[4]. "
 "날씨가 좋았던 2019년에는 세 번, 2020년에는 네 번 수확했으나 덥고 가물었던 2021년에는 두 번만 수확할 수 있었다[4]. "
 "건조 수량은 꽃줄기 높이와 밀접했고 GH03 계통이 1 ha당 565.8 kg으로 가장 많았다[4]. "
 "수확기의 최저 높이가 8 cm여서 꽃이 진 뒤 다시 자란 짧은 줄기는 기계 수확이 어려웠다[4].\n\n"
 "폴리페놀을 얻으려면 꽃 피는 시기, 정유를 얻으려면 영양 생장기에 거두는 것이 알맞았고, 재배해도 야생과 성분·활성 차이가 크지 않았다[4]. "
 "한편 잔디밭에서는 병꽃풀이 잡초로 취급되어, 다년생 라이그래스 잔디에서 병꽃풀을 찾아내는 딥러닝 검출 모델이 개발되었다[31]. "
 "국내 병꽃풀 재배면적·생산량 공식 통계와 지리적 표시 등록은 이번 조사에서 확인하지 못함.")
S["processing"] = ("병꽃풀은 주로 말린 지상부를 물이나 에탄올로 우려 쓴다[2]. "
 "말린 풀 2.0 g에 끓는 물 50 mL를 부어 우려 두는 방법(I/ME)이 로즈마린산(4.28–4.89 mg/g)과 클로로겐산(3.41–3.70 mg/g)을 가장 많이 뽑아냈고, 루틴·이소퀘르세틴은 에탄올 가열 환류 추출에서 가장 많았다[2]. "
 "끓는 물에 오래 둘수록 클로로겐산 같은 페놀산이 줄어 집에서 차처럼 우리는 방식이 오히려 알맞았다[2]. "
 "크로아티아 시료에서는 마이크로파 추출이 페놀 성분 회수율이 가장 높았고, 200 °C 아임계수 추출에서는 원래 없던 새 항산화 물질이 생겼다[3].\n\n"
 "같은 시료의 건조물은 불용성 식이섬유 32.26–48.03%, 단백질 최대 23.12%를 함유했고, 칼륨 14.49–29.80 mg/g, 칼슘 7.78–14.89 mg/g으로 칼륨·칼슘이 많았다[3]. "
 "정유는 건조 무게 1 kg당 0.32–2.98 mL 얻어졌다[4]. "
 "추출물은 돼지기름·해바라기유의 산화를 늦추는 천연 항산화제로 시험되었고, 리포좀으로 감싼 추출물을 사탕과 초콜릿에 넣는 연구도 있다[25][26][27]. "
 "잎을 공기 중에 말리면 지방산 산화물인 9-히드록시 지방산이 크게 늘어난다[20]. "
 "국내 병꽃풀 건강기능식품·가공식품 생산실적은 확인하지 못함.")
S["genetics"] = ("병꽃풀은 염색체 수 2n = 36인 사배체로, 북·중부 유럽 27곳의 93개 포기에서 모두 2n = 36이 확인되었다[7]. "
 "10개 효소의 유전 분석에서 분리비가 이배체식(이염색체) 유전과 맞아, 이배체처럼 행동하게 된 동질사배체로 해석되었다[7]. "
 "병꽃풀속의 기본 염색체 수는 x = 9이며, 유럽 병꽃풀의 핵 DNA 양(1C)은 약 0.82 pg으로 아시아 종(0.91–0.92 pg)보다 조금 작다[6].\n\n"
 "형광제자리부합법(FISH) 분석에서 병꽃풀은 5S rDNA 신호 4개가 일정했고, 35S rDNA 신호는 포기에 따라 6–8개로 달라 네 가지 배치형이 나타났다[6]. "
 "5S rDNA 비전사 간격 서열에서 두 계열이 나와, 이 연구는 이질배수체 기원 가능성을 제시했다[6]. "
 "효소 유전 연구(동질사배체)와 rDNA 연구(이질배수체 가능성)의 해석은 서로 다르다[6][7]. "
 "잎 렉틴 Gleheda의 유전자는 클로닝되었고, 네 개의 소단위로 된 단백질이며 콩과 렉틴과 같은 입체 구조를 가진다[10]. "
 "병꽃풀의 핵 유전체·엽록체 유전체 해독 결과와 국내 육종 품종은 이번 조사에서 확인하지 못함.")
S["safety"] = ("병꽃풀에 대한 국내외 공공기관(식약처·EFSA 등)의 안전성 평가나 알레르기·잔류 기준 정보는 이번 조사에서 확인하지 못함. "
 "크로아티아 야생 시료의 비소·카드뮴·납은 세계보건기구 약용식물 허용 수준보다 낮았고, 다른 미량 금속도 안전 범위 안이었다[3].\n\n"
 "실험실 연구에서 말린 지상부의 물·에탄올 추출물(10–100 µg/mL)은 세포 독성이 약했고, 정상 피부세포(HaCaT)와 간세포(HepG2)에 독성을 보이지 않았다[2]. "
 "반면 메탄올 추출물과 분획은 사람 말초혈액 단핵세포의 생존율을 24시간 뒤 최대 약 65%까지 낮췄고, 사람 혈장의 응고 시간에는 영향을 주지 않았다[5]. "
 "지상부의 헥산·디클로로메탄·메탄올 추출물은 브라인슈림프 치사 시험으로 일반 독성이 평가되었고[28], 라트비아 연구는 이 시험에서 10 mg/mL까지 독성이 없었다는 앞선 결과를 인용했다[4].\n\n"
 "에틸아세테이트 분획(로즈마린산·카페산·페룰산이 많음)은 간암세포(HepG2)의 증식을 억제하고 세포자멸사를 일으켰다[34]. "
 "동물에서는 열수 추출물이 담관 결찰 쥐의 담즙정체성 간 손상을 줄였고, 상업용 병꽃풀 추출물을 하루 세 번 먹인 생쥐에서 담석 결정이 줄었다[14][15]. "
 "사람 연구로는 아시아 여성의 자외선 색소 침착에 1% 추출물 로션을 8주 바른 위약 대조 시험이 있으며, 먹는 형태의 사람 임상시험은 확인하지 못함[16]. "
 "간 질환·임신·수유 중 섭취에 관한 공식 주의사항도 확인하지 못함.")
TITLES = {"overview": "한눈에 보기", "history": "역사", "biology": "식물학적 특징", "related_species": "가까운 종", "cultivation": "재배와 생산", "processing": "가공과 이용", "genetics": "유전체와 육종", "safety": "안전성"}
sections = [{"key": k, "title": TITLES[k], "body": S[k]} for k in TITLES]

def c(name, ko, cls, role, part, content, act, src):
    return {"name": name, "name_ko": ko, "class": cls, "role": role, "part": part, "content_text": content, "activity_ko": act, "source": src}
compounds = [
 c("Rosmarinic acid", "로즈마린산", "페놀산(카페산 에스터)", "marker", "지상부(말린 풀)",
   "물 우림(I/ME) 4.28–4.89 mg/g 건조 식물[2]; 마이크로파 추출 최대 18.69 mg/g 건조중량(G4 시료)[3]; 60% 분획 101.52 ± 5.76 mg/g[5]; 꽃줄기 5105 ± 362 µg/g, 영양줄기 3218 ± 592 µg/g(2021년)[4]",
   "추출물의 주성분으로, 생쥐 대식세포의 염증형(M1) 전환을 클로로겐산·카페산보다 더 강하게 줄였다(시험관)[4]", [2, 3, 4, 5]),
 c("Chlorogenic acid", "클로로겐산", "페놀산(카페오일퀸산)", "marker", "지상부",
   "물 우림(I/ME) 3.41–3.70 mg/g 건조 식물[2]; 마이크로파 추출 4.98–7.15 mg/g 건조중량(G1·G2·G6)[3]; 60% 분획 31.77 ± 4.03 mg/g[5]; 꽃줄기 3390 ± 461 µg/g, 영양줄기 1461 ± 363 µg/g[4]",
   "로즈마린산과 함께 주요 페놀산으로 정량됨[2][4]", [2, 3, 4, 5]),
 c("Cryptochlorogenic acid", "크립토클로로겐산(4-O-카페오일퀸산)", "페놀산(카페오일퀸산)", "bioactive", "지상부 물 추출물",
   "주요 페놀 성분으로 정량됨(시료별 값은 원문 표, 확인하지 못함)[3]", "LC-MS/MS 분획과 표준품으로 확인됨[3]", [3]),
 c("Caffeic acid", "카페산", "페놀산", "bioactive", "지상부(영양줄기에 더 많음)",
   "꽃줄기보다 영양줄기 추출물에 유의하게 많음(정량값 단위 확인하지 못함)[4]", "생쥐 대식세포의 염증형(M1) 표지 발현을 줄임(시험관)[4]", [3, 4]),
 c("Rutin", "루틴", "플라보놀 배당체", "bioactive", "지상부",
   "에탄올 가열 환류 0.84–0.99 mg/g 건조 식물[2]; 마이크로파 추출 최대 8.83 mg/g 건조중량(G2)[3]; 60% 분획 62.31 ± 0.98 mg/g[5]",
   "주요 플라보노이드로 정량됨[2][5]", [2, 3, 5]),
 c("Isoquercitrin", "이소퀘르시트린(퀘르세틴 3-O-글루코사이드)", "플라보놀 배당체", "bioactive", "지상부",
   "에탄올 가열 환류 0.82–0.96 mg/g 건조 식물[2]", "이 종에서 처음 정량된 성분으로 보고됨[2]", [2]),
 c("Protocatechuic acid", "프로토카테큐산", "페놀산", "bioactive", "지상부",
   "0.02–0.73 mg/g 건조 식물(추출법에 따라)[2]", "물 추출물의 DPPH 소거능과 상관(r = 0.98)[2]", [2]),
 c("Apigenin", "아피제닌", "플라본", "bioactive", "지상부(꽃줄기)",
   "85% 분획 26.17 ± 1.44 mg/g[5]; 꽃줄기 97.0 µg/g 건조물, 7월 영양줄기는 검출 안 됨[4]",
   "85% 분획의 주성분으로, 혈장 단백질 카보닐화와 DNA 산화 손상을 줄인 활성 성분으로 추정됨(시험관)[5]", [4, 5]),
 c("Luteolin", "루테올린", "플라본", "bioactive", "지상부(꽃줄기)",
   "꽃줄기 39.5 µg/g 건조물, 7월 영양줄기는 검출 안 됨[4]", "꽃줄기에만 뚜렷이 있는 성분으로 보고됨[4]", [4]),
 c("Apigenin 7-O-(6''-O-malonylglucoside)", "아피제닌 7-O-(6″-말로닐글루코사이드)", "플라본 배당체", "bioactive", "지상부 물 추출물",
   "최대 0.90 mg/g 건조중량(G2, 아피제닌 환산)[3]", "LC-MS/MS와 산가수분해로 확인됨[3][5]", [3, 5]),
 c("Luteolin 7-O-rutinoside", "루테올린 7-O-루티노사이드", "플라본 배당체", "bioactive", "지상부 물 추출물",
   "최대 0.68 mg/g 건조중량(G5, 루테올린 환산)[3]", "LC-MS/MS와 산가수분해로 확인됨[3]", [3]),
 c("Ursolic acid", "우르솔산", "펜타사이클릭 트리테르펜", "bioactive", "잎·지상부",
   "잎 7.1–7.5 mg/g 건조중량; 지상부 디클로로메탄 가열 환류 건조 추출물 17–25%(w/w)[11]",
   "엡스타인-바 바이러스 활성화 억제 성분으로 분리되었고, 생쥐 피부 종양 촉진을 억제함[12]", [11, 12]),
 c("Oleanolic acid", "올레아놀산", "펜타사이클릭 트리테르펜", "bioactive", "잎·지상부",
   "우르솔산과 함께 UPLC-MS/MS로 정량됨(함량은 초록에 없음, 확인하지 못함)[11]", "생쥐 피부 종양 촉진 억제(동물)[12]", [11, 12]),
 c("Germacrene D", "게르마크렌 D", "세스퀴테르펜(정유)", "bioactive", "지상부 정유",
   "정유 수율 0.32–2.98 mL/kg 건조중량; β-미르센·β-오시멘·게르마크렌 B·유칼립톨·1-옥텐-3-올과 함께 주요 성분[4]",
   "정유의 주요 구성 성분(64종 중)[4]", [4]),
 c("9-Hydroxyoctadecadienoic acid", "9-히드록시옥타데카디엔산(9-HODE)", "산화 지방산", "bioactive", "잎",
   "잎의 9-히드록시·9-옥소 지방산 4종 질량비 71/14/12/3 가운데 9-HODE는 12; 공기 건조 시 9-히드록시옥타데카트리엔산이 크게 늘어남[20]",
   "사람 혈소판 막의 아데닐산 고리화효소 활성을 약 3배 높임(EC50 10–20 µM, 시험관)[21]", [20, 21]),
]

def cond(**k):
    keys = ["instrument","column","mobile_phase","gradient","flow","temp","detection","injection","sample_prep","standard","linearity","lod","loq","recovery"]
    return {x: k.get(x, "") for x in keys}
assays = [
 {"role": "literature", "compound": "Rosmarinic acid", "compound_ko": "로즈마린산(클로로겐산·프로토카테큐산·루틴·이소퀘르세틴 동시)", "part": "지상부(꽃필 때 채취, 말린 풀)",
  "content": "로즈마린산 4.28–4.89, 클로로겐산 3.41–3.70 mg/g 건조 식물(물 우림 I/ME); 루틴 0.84–0.99, 이소퀘르세틴 0.82–0.96 mg/g(에탄올 가열 환류)[2]",
  "method": "HPLC-DAD",
  "conditions": cond(instrument="Dionex 100 HPLC, Photodiode 100 검출기", column="Hypersil Gold C18, 250 × 4.6 mm, 5 µm (Thermo Scientific)",
    mobile_phase="A: 1% 포름산, B: 아세토니트릴", gradient="5–60% B, 60분", injection="20 µL",
    sample_prep="말린 지상부 가루 2.0 g + 용매 50 mL(물은 끓는 물을 부어 30분–2시간 우림 등) → 여과·감압 농축해 25 mL로 맞춤 → 1.5 mL를 0.45 µm 나일론 필터로 여과",
    standard="로즈마린산·클로로겐산·프로토카테큐산·루틴·이소퀘르세틴(Fluka), 메탄올 1 mg/mL 원액, 0.0625–1.0 mg/mL 검량선"),
  "rationale": "말린 풀 추출물에서 가장 많은 페놀산이 로즈마린산이고 다음이 클로로겐산이어서, 추출법 비교의 지표로 썼다[2]. 유속·칼럼 온도·검출 파장·검출한계·회수율은 본문에 없어 비워 둠.",
  "source": [2], "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9460379/", "source_kind": "paper"},
 {"role": "literature", "compound": "Chlorogenic acid", "compound_ko": "클로로겐산(크립토클로로겐산·카페산·로즈마린산·루틴 동시)", "part": "지상부(4월 야생 채취, 건조)",
  "content": "마이크로파 추출 클로로겐산 6.10·7.15·4.98 mg/g 건조중량(G1·G2·G6), 로즈마린산 최대 18.69 mg/g(G4), 루틴 최대 8.83 mg/g(G2)[3]",
  "method": "HPLC-PAD",
  "conditions": cond(instrument="Agilent 1200 시리즈, 광다이오드 배열 검출기(PAD)", column="Zorbax Extend C18, 4.6 × 250 mm, 5 µm (Agilent)",
    mobile_phase="A: 1% 포름산 수용액, B: 1% 포름산 아세토니트릴", gradient="0분 7% B, 5분 7%, 45분 40%, 47분 70%, 52분 70% B",
    flow="1 mL/min", temp="25 °C", detection="320·350 nm(동정은 190–400 nm 스펙트럼 비교)", injection="5 µL",
    sample_prep="실온 3일 건조 → 분쇄해 450 µm 이하 → 물 1 g/100 mL로 추출(마이크로파 90 °C 4.93분 등) → 9500 rpm 20분 원심, 여과 → 0.45 µm 나일론 막 여과",
    standard="외부표준 검량선 2–100 µg/mL; 루테올린·아피제닌 배당체는 아글리콘 표준품으로 환산"),
  "rationale": "크로아티아 7개 야생 시료에서 클로로겐산·크립토클로로겐산·카페산·로즈마린산·루틴이 주요 페놀 성분이었고, 시료에 따라 클로로겐산·루틴·로즈마린산 가운데 주성분이 달랐다[3]. 직선성 계수·검출한계·회수율은 본문에 없어 비워 둠.",
  "source": [3], "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8909519/", "source_kind": "paper"},
 {"role": "literature", "compound": "Apigenin", "compound_ko": "아피제닌(루테올린·플라보노이드 배당체 동시)", "part": "지상부(꽃줄기·영양줄기) 70% 에탄올 추출물",
  "content": "2021년 6월 꽃줄기 아피제닌 97.0 µg/g, 루테올린 39.5 µg/g 건조물; 7월 영양줄기는 검출 안 됨[4]",
  "method": "UHPLC-MS/MS(MRM)",
  "conditions": cond(instrument="Waters Acquity UPLC + Xevo TQ-S micro 삼중사중극자 질량분석기", column="Acquity BEH C18, 2.1 × 100 mm, 1.7 µm (Waters)",
    mobile_phase="A: 0.1% 포름산 수용액, B: 아세토니트릴", gradient="0분 5% B, 0.5분 5%, 8분 98%, 10분 98%, 11분 5%, 12분 5% B",
    flow="0.4 mL/min", temp="30 °C", detection="ESI(+) MRM(성분별 조건은 원문 보충표)", injection="1 µL",
    sample_prep="말린 가루를 70% 에탄올(1:10)에 7일 침지 → 압착·원심 → 농축·동결건조; 분석 전 내부표준(레세르핀 10 ng/mL) 70% 에탄올로 10배 또는 100배 희석",
    standard="플라보노이드 표준품(PhytoLab), 검량선 50 ng/mL–10 µg/mL; 내부표준 레세르핀"),
  "rationale": "아피제닌·루테올린과 그 7-O-글루코사이드는 꽃줄기에만 뚜렷이 있어 수확 시기(꽃 필 때 vs 영양 생장기)를 가르는 성분으로 쓰였다[4]. 페놀산은 같은 연구에서 Quattro Micro, ESI(−), BEH C18 2.1 × 50 mm, 0.25 mL/min, 검량선 50 ng/mL–5 µg/mL로 따로 정량했다[4]. 검출·정량한계와 회수율은 본문에 없어 비워 둠.",
  "source": [4], "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8949430/", "source_kind": "paper"},
 {"role": "literature", "compound": "Ursolic acid", "compound_ko": "우르솔산(올레아놀산 동시)", "part": "잎·지상부",
  "content": "잎 7.1–7.5 mg/g 건조중량; 지상부 디클로로메탄 가열 환류 건조 추출물 우르솔산 17–25%(w/w)[11]",
  "method": "UPLC-MS/MS",
  "conditions": cond(),
  "rationale": "병꽃풀과 G. hirsuta의 우르솔산·올레아놀산을 동시에 정량하는 방법을 개발·검증했고(직선성·정밀도·회수율 양호), 원료·추출물 품질 관리에 쓰도록 제안했다[11]. 전문 확인 못함 — 초록만 보아 분석 조건 칸은 비워 둠.",
  "source": [11], "url": "https://pubmed.ncbi.nlm.nih.gov/33450770/", "source_kind": "paper"},
]

d = {"slug": "glechoma-hederacea", "name_ko": "병꽃풀", "name_en": "Ground ivy", "scientific_name": "Glechoma hederacea L.",
     "aliases": ["연전초", "병꽃풀순", "병꽃풀잎", "ground ivy"],
     "sections": sections, "compounds": compounds, "markers": [], "assays": assays, "nutrients": [],
     "production": [], "world": [], "gi": [], "orgs": [], "sources": sources}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
for s in sections: print(s["key"], len(s["body"]))
