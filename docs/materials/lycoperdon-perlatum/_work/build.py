import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
A = "2026-11-02"
def pm(n, title, pmid, pub, note=""):
    return {"n": n, "title": title + (f" ({note})" if note else ""), "url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/", "publisher": pub + " (PubMed)", "accessed": A}
I1020 = "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020"
sources = [
 {"n": 1, "title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 말불버섯·말불버섯어린자실체(Lycoperdon perlatum Pers.) (로컬 원자료 I1020_20261013.json 대조)", "url": I1020, "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
 {"n": 2, "title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 비교 항목: 가시말불버섯자실체(Lycoperdon echinatum)·좀말불버섯자실체(Lycoperdon pyriforme)·너도말불버섯자실체(Lycoperdon umbrinum)·말징버섯(Calvatia craniiformis)·코끼리말징버섯(Calvatia boninensis)·큰말징버섯(Calvatia cyathiformis) (로컬 원자료 I1020_20261013.json)", "url": I1020, "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
 pm(3, "Mercury bio-concentration by puffballs (Lycoperdon perlatum) and evaluation of dietary intake risks. Bull Environ Contam Toxicol 2012;89(4) doi:10.1007/s00128-012-0788-3", "22898887", "Springer", "PMC3437224 전문 확인"),
 pm(4, "Accumulation factors of mercury in mushrooms from Zaborski Landscape Park, Poland. Environ Int 2002;28(5):421-7 doi:10.1016/s0160-4120(02)00067-3", "12437292", "Elsevier", "초록 확인"),
 pm(5, "Total mercury in mushrooms and underlying soil substrate from the Borecka Forest, Northeastern Poland. Arch Environ Contam Toxicol 2002;42(2):145-54 doi:10.1007/s00244-001-0026-1", "11815805", "Springer", "초록 확인"),
 pm(6, "[Content and accumulation of mercury in common puffball (Lycoperdon perlatum)]. Rocz Panstw Zakl Hig 2008;59(3):267-72", "19143423", "Roczniki PZH", "폴란드어 논문, 영문 초록 확인"),
 pm(7, "Evaluating mercury concentrations in edible plant and fungi species in the Canadian Arctic environment. J Environ Qual 2021 doi:10.1002/jeq2.20253", "34048608", "Wiley", "초록 확인"),
 pm(8, "Concentrations of mercury, cadmium, lead and copper in fruiting bodies of edible mushrooms in an emission area of a copper smelter and a mercury smelter. Sci Total Environ 2000;246(1):61-7 doi:10.1016/s0048-9697(99)00411-8", "10682377", "Elsevier", "초록 확인"),
 pm(9, "Lead and cadmium in mushrooms from the vicinity of two large emission sources in Slovenia. Sci Total Environ 2012 doi:10.1016/j.scitotenv.2012.11.007", "23253939", "Elsevier", "초록 확인"),
 pm(10, "Levels of some trace elements in edible fungi. Z Lebensm Unters Forsch 1995;201(4):311-6 doi:10.1007/BF01192723", "8525697", "Springer", "초록 확인"),
 pm(11, "Metal concentration and antioxidant activity of edible mushrooms from Turkey. Food Chem 2015 doi:10.1016/j.foodchem.2014.12.019", "25577119", "Elsevier", "초록 확인"),
 pm(12, "Elemental composition of selected species of mushrooms based on a chemometric evaluation. Ecotoxicol Environ Saf 2019 doi:10.1016/j.ecoenv.2019.02.036", "30784799", "Elsevier", "초록 확인"),
 pm(13, "Influence of the urban environment on four mushroom species in the light of their elemental composition. Chemosphere 2023 doi:10.1016/j.chemosphere.2023.139052", "37245597", "Elsevier", "초록 확인"),
 pm(14, "Can the concentration of elements in wild-growing mushrooms be deduced from the taxonomic rank? Environ Res 2024 doi:10.1016/j.envres.2024.119079", "38729408", "Elsevier", "초록 확인"),
 pm(15, "Levels of eight trace elements in edible mushrooms from a rural area. Food Addit Contam Part A 2008;25(1):51-8 doi:10.1080/02652030701458519", "17852381", "Taylor & Francis", "초록 확인"),
 pm(16, "Phenolic acids determination by HPLC-DAD-ESI/MS in sixteen different Portuguese wild mushrooms species. Food Chem Toxicol 2009;47(6):1076-9 doi:10.1016/j.fct.2009.01.039", "19425182", "Elsevier", "초록 확인"),
 pm(17, "Chemical composition and biological properties of Portuguese wild mushrooms: a comprehensive study. J Agric Food Chem 2008;56(10):3856-62 doi:10.1021/jf8003114", "18435539", "ACS", "초록 확인"),
 pm(18, "Synthesis of both enantiomers of lycoperdic acid, an unusual mushroom-derived amino acid. Biosci Biotechnol Biochem 2021 doi:10.1093/bbb/zbaa027", "33577651", "Oxford University Press", "초록 확인"),
 pm(19, "Mushrooms as potential therapeutic agents in the treatment of cancer: evaluation of anti-glioma effects of Coprinus comatus, Cantharellus cibarius, Lycoperdon perlatum and Lactarius deliciosus extracts. Biomed Pharmacother 2021 doi:10.1016/j.biopha.2020.111090", "33378984", "Elsevier", "초록 확인"),
 pm(20, "Antiviral activity of some compounds of gasteroid mushrooms from Western Siberia. Int J Med Mushrooms 2024 doi:10.1615/IntJMedMushrooms.2023051031", "38305261", "Begell House", "초록 확인"),
 pm(21, "[Research of antifungal substances secreted by higher fungi in culture]. Ann Pharm Fr 1990;48(1):17-22", "2082797", "Elsevier Masson", "프랑스어 논문, 초록 확인"),
 pm(22, "Respiratory illness associated with inhalation of mushroom spores — Wisconsin, 1994. MMWR Morb Mortal Wkly Rep 1994;43(29):525-6", "8028572", "미국 질병통제예방센터(CDC)", "초록 확인"),
 pm(23, "Lycoperdonosis. Acta Paediatr Scand 1976;65(5):643-5 doi:10.1111/j.1651-2227.1976.tb04945.x", "986747", "Wiley", "초록 확인"),
 pm(24, "The significance of the spores of the Basidiomycetes (mushrooms and their allies) in bronchial asthma and allergic rhinitis. Ann Allergy 1985;55(3):469-71", "4037433", "Ann Allergy", "초록 확인"),
 pm(25, "Phylogenetic relationships among species and genera of Lycoperdaceae based on ITS and LSU sequence data from north European taxa. Mycol Res 2008;112(Pt 1):4-22 doi:10.1016/j.mycres.2007.10.018", "18207380", "Elsevier", "초록 확인"),
 pm(26, "Comparative analysis of mitochondrial genomes in Lycoperdaceae fungi reveals intron dynamics and phylogenetic relationships. BMC Genomics 2025;26:742 doi:10.1186/s12864-025-11911-4", "40790547", "BMC", "PMC12341119 전문 확인 — 전문 텍스트에서 종 이름이 빠져 분석한 4종에 이 종이 들었는지 확인하지 못함"),
 {"n": 27, "title": "Two new Lycoperdon species collected from Korea: L. albiperidium and L. subperlatum. Phytotaxa 2016;260(2):101-115 doi:10.11646/phytotaxa.260.2.1 (WebSearch 요약으로만 확인, 원문·초록 페이지는 열지 못함)", "url": "https://doi.org/10.11646/phytotaxa.260.2.1", "publisher": "Magnolia Press", "accessed": A},
 pm(28, "The cultural significance of wild mushrooms in San Mateo Huexoyucan, Tlaxcala, Mexico. J Ethnobiol Ethnomed 2014;10:27 doi:10.1186/1746-4269-10-27", "24597704", "BMC", "초록 확인"),
 pm(29, "Diversity and ethnomycological importance of mushrooms from Western Himalayas, Kashmir. J Ethnobiol Ethnomed 2022;18:32 doi:10.1186/s13002-022-00527-7", "35418143", "BMC", "초록 확인"),
 pm(30, "Archaea are prominent members of the prokaryotic communities colonizing common forest mushrooms. Can J Microbiol 2018 doi:10.1139/cjm-2018-0035", "29733685", "Canadian Science Publishing", "초록 확인"),
 pm(31, "210Pb and stable lead content in fungi: its transfer from soil. Sci Total Environ 2009;407(14):4320-6 doi:10.1016/j.scitotenv.2009.03.025", "19403160", "Elsevier", "초록 확인"),
 pm(32, "Mercury content and its bioconcentration factors in wild mushrooms at Łukta and Morag, northeastern Poland. J Agric Food Chem 2003;51(9):2832-6 doi:10.1021/jf026016l", "12696981", "ACS", "초록 확인"),
 pm(33, "[Cultural characteristics of some ectomycorrhizal fungi in pure culture]. Rev Iberoam Micol 2000;17(4):127-34", "15762807", "Elsevier España", "스페인어 논문, 영문 초록 확인"),
]

S = []
def sec(k, t, b): S.append({"key": k, "title": t, "body": b})

sec("overview", "한눈에 보기",
"말불버섯(Lycoperdon perlatum Pers.)은 말불버섯과(Lycoperdaceae) 무리의 이른바 퍼프볼 버섯으로, 영어로는 common puffball, warted puffball, gem-studded puffball 등으로 불린다[3, 26]. 식품의약품안전처 「식품원료 목록」에는 '말불버섯'(부위 자실체)과 '말불버섯어린자실체'(부위 어린자실체) 두 항목이 올라 있고, 둘 다 상태는 '사용가능', 사용 조건은 '사용가능부위 : 자실체', 이명은 '봉오리먼지버섯'이다[1]. 따라서 일반 식품의 원료로는 자실체만 쓸 수 있으며, 목록이 어린 자실체를 따로 적어 둔 점은 속살이 흰 어린 시기에만 먹는다는 이용 관행과 맞닿아 있다[1, 3]. 논문들은 속살이 흰 어린 개체는 오래전부터 식용으로 여겨졌고 갈색으로 변한 성숙 개체는 먹지 않는다고 적었다[3]. 건강기능식품 고시형 원료의 원재료 목록에는 없어 고시된 지표성분과 기준은 확인하지 못함.\n\n같은 목록에는 같은 속의 가시말불버섯·좀말불버섯·너도말불버섯과 가까운 말징버섯속(Calvatia) 원료가 따로 올라 있으므로 이 문서는 그 종들의 자료를 섞지 않는다[2]. 이 종에 관한 논문은 수은·카드뮴·납 같은 원소 축적과 포자 흡입 질환을 다룬 것이 많다[3, 8, 22]. 국가표준식품성분표 등 공식 영양성분 값은 확인하지 못함.")

sec("history", "이름과 이용의 역사",
"학명 Lycoperdon perlatum의 명명자는 'Pers.'(페르손)로, 식약처 목록에도 'Lycoperdon perlatum Pers.'로 적혀 있다[1]. 이 종에서 처음 알려진 특이 아미노산은 속 이름을 따서 lycoperdic acid라 불린다[18]. 영어권 논문은 이 종을 Common Puffball, Warted Puffball, Gem-studded Puffball, Devil's Snuff-box 등으로 소개했다[3]. 국문명 '말불버섯'과 이명 '봉오리먼지버섯'의 유래, 국내 식용 역사는 확인하지 못함.\n\n말불버섯류(Lycoperdon)는 민간요법에 널리 쓰였다는 기록이 있으며, 1976년 증례 보고는 그 포자를 많이 들이마신 뒤 생긴 호흡기 질환을 다뤘다[23]. 지역 이용을 조사한 연구를 보면 멕시코 틀락스칼라의 한 마을에서는 이 종이 문화적 중요도 지수가 가장 낮은 무리에 속했다[28]. 파키스탄령 카슈미르의 야생 식용버섯 조사에서는 이 종이 조사지의 주요 종 가운데 하나로 묶였다[29]. 유럽 연구자들은 폴란드에서 이 종을 식용 야생버섯으로 채집해 원소 함량을 분석해 왔다[3, 12].")

sec("biology", "균학적 특징",
"말불버섯과 버섯은 포자를 만드는 기본체(gleba)가 껍질(peridium)에 싸인 둥근 자실체를 만드는 복균(gasteroid) 무리다[26]. 이 문서의 원료 카드는 이 종을 균계 주름버섯과(Agaricaceae)로 분류한다[1]. 분자계통 연구는 말불버섯과(Lycoperdaceae)를 단계통군으로 확인했고, 미토콘드리아 유전체 분석은 이 무리가 주름버섯과 안에 들어간다고 보고했다[25, 26]. 이 종은 낙엽·유기물을 분해해 사는 부생균으로 분류되며, 루마니아 연구에서는 도시 공원에서도 흔히 채집됐다[13]. 배양하지 않고 유전자를 분석한 연구에서는 자실체 내부 조직에서 세균과 고세균이 함께 검출됐다[30].\n\n자실체는 어릴 때 속살이 희며, 자라면 갈색이나 더 어두운 색으로 변한다[3]. 성숙하면 많은 포자가 퍼져 나가며, 이 포자를 대량으로 들이마시면 호흡기 질환이 생길 수 있다[22, 23].\n\n이 종은 토양의 수은을 자실체에 잘 모아 생물농축계수(자실체/토양 농도비)가 폴란드 열 곳에서 평균 28–110(범위 9.6–280)이었다[3]. 폴란드 북부 네 곳 연구에서도 이 계수의 평균이 65–110이었다[6]. 납-210의 토양→버섯 전이 계수도 조사 종 가운데 높은 편이었다[31].")

sec("related_species", "가까운 종과 혼동",
"식약처 「식품원료 목록」에는 같은 속의 가시말불버섯자실체(L. echinatum), 좀말불버섯자실체(L. pyriforme), 너도말불버섯자실체(L. umbrinum)가 따로 '사용가능' 원료로 올라 있다[2]. 가까운 말징버섯속에서는 말징버섯(Calvatia craniiformis)과 코끼리말징버섯(C. boninensis)이 '사용가능', 큰말징버섯(C. cyathiformis)은 '사용불가'로 올라 있어 겉모양이 비슷해도 원료 지위가 다르다[2]. 그러므로 말불버섯 자료와 이 종들의 자료를 섞지 않아야 한다[1, 2].\n\n유럽 북부 시료의 ITS·LSU 분석에서 말불버섯속 계통군은 Vascellum·Morganella·Handkea·Bovistella와 일부 Calvatia 종까지 포함했고, 속 안의 관계는 대부분 잘 풀리지 않았다[25]. 2016년 한국산 신종 기재 논문은 말불버섯과 닮은 L. subperlatum을 새로 기재하고, 한국·일본·중국·유럽의 L. perlatum은 한 계통군으로 묶이나 미국 시료는 다른 계통에 든다고 보고했다는데, 이는 WebSearch 요약으로만 확인했고 원문은 확인하지 못함[27]. 말불버섯과는 종끼리 겉모양이 매우 비슷해 형태만으로 정확히 구분하기 어렵다는 지적이 있다[26].")

sec("cultivation", "채취와 생산",
"말불버섯은 숲과 공원 땅에서 야생으로 나는 자실체를 채집해 이용하며, 폴란드 연구들은 여러 숲에서 채집한 시료를 분석했다[3, 4, 5]. 루마니아 클루지나포카 연구에서는 도시 공원과 교외 대조지의 자실체를 비교했는데, 도시 시료에서 은·스트론튬이 더 높았다[13]. 저자들은 이 종을 도시 무기 오염의 지표종으로 제안했다[13]. 따라서 채집 장소의 토양 오염이 자실체 품질을 크게 좌우한다[3, 13].\n\n순수 배양에서는 균사를 MMN 배지에서 키운 기록이 있다[33]. 배양 여과액이 일부 식물병원균과 칸디다균에 대해 억제 활성을 보였다는 시험관 연구도 있다[21]. 상업적 재배 기술, 국내 채취량·생산 통계는 확인하지 못함. 통계청·농림축산식품부의 특용작물 생산 통계에도 이 품목은 확인하지 못함.")

sec("processing", "가공과 이용",
"식용은 속살이 희고 균일한 어린 자실체로 한정되며, 속이 갈색으로 변한 성숙 개체는 먹지 않는다[3]. 식약처 목록이 '말불버섯어린자실체'를 별도 원료로 두고 있는 것도 이 관행과 맞는다[1]. 분석 연구에서는 자실체를 상온에서 2–3일 말린 뒤 65 ℃에서 48–96시간 건조해 분말로 만들어 썼다[3]. 국내의 조리·가공 방법과 건강기능식품 원료 생산실적은 확인하지 못함.\n\n추출물 연구로는 터키 시료에서 네 가지 항산화 시험 모두 높은 활성을 보였고, 활성은 총 페놀·플라보노이드 함량과 강하게 상관했다[11]. 포르투갈 시료의 페놀산 분석에서는 신남산만 14.36 mg/kg(건조물) 검출됐다[16]. 포르투갈 비교 연구에서 말불버섯속 두 종(이 종과 L. molle)은 시험한 모든 미생물에 대해 'resistant'로 기술되어, 항균 활성이 나타나지 않은 것으로 보인다[17]. 에탄올 추출물이 교모세포종 세포의 증식을 억제했다는 결과와 인플루엔자 A 바이러스(H3N2·H5N1)를 억제했다는 결과는 모두 세포 시험이다[19, 20]. 같은 교모세포종 연구에서 가장 강한 활성을 보인 것은 이 종이 아니라 다른 두 종이었다[19]. 사람 대상 시험은 확인하지 못함.")

sec("genetics", "유전체와 분자 연구",
"이 종의 핵 유전체 해독 보고는 확인하지 못함. 북유럽 말불버섯과 시료의 ITS·LSU 리보솜 DNA 계통 분석은 말불버섯과를 단계통군으로 확인하고, Lycoperdon·Bovista·Calvatia·Disciseda 속에 대응하는 네 큰 계통군을 제시했다[25]. 이 분석은 말불버섯속 31종을 구분했고, Vascellum·Morganella 등 여러 속의 종을 품은 말불버섯속 계통군 전체를 말불버섯속으로 다루자고 제안했다[25].\n\n2025년 연구는 말불버섯속과 말징버섯속 4종의 미토콘드리아 유전체 전체를 처음 해독했으며, 크기는 52,694–62,146 bp였다[26]. 네 유전체는 단백질 암호 유전자 15개, rRNA 2개, tRNA 25개를 가졌고 인트론과 열린 해독틀의 수가 크기 차이의 주된 원인이었다[26]. 다만 전문 텍스트에서 종 이름이 빠져 있어 분석한 4종에 이 종이 포함됐는지는 확인하지 못함. 한국·일본·중국·유럽 시료와 미국 시료가 서로 다른 계통일 수 있다는 2016년 논문의 결과는 WebSearch 요약으로만 확인했고, 원문은 확인하지 못함[27]. 자실체 내부에서 고세균 16S rRNA 유전자가 세균보다 많이 검출된 종이 있다는 분석도 있다[30].")

sec("safety", "안전성",
"말불버섯은 식품원료 목록에 '사용가능'으로 올라 있고 별도의 섭취 시 주의사항은 확인하지 못함[1]. 식용은 속이 흰 어린 자실체에 한하며 갈색으로 변한 성숙 개체는 먹지 않는다[3]. 이 종은 수은 축적종으로, 폴란드 열 곳 시료는 0.57–4.5 µg/g, 다른 폴란드 숲은 평균 3.7·3.4 µg/g, 캐나다 북극권은 중앙값 1.6 µg/g(모두 건조물)이었다[3, 4, 5, 7, 32]. 저자들은 생버섯 300 g 한 끼가 일일 참조용량(체중 70 kg)의 130–340%에 해당하는 수은을 줄 수 있다고 계산했다[3]. 제련소·오염지 주변에서는 이 종의 수은·카드뮴·납·구리가 매우 높았고, 체코 조사에서는 비소를 많이 축적한 종에 들었다[8, 9, 15]. 스웨덴 조사에서는 이 종과 큰갓버섯의 납이 생중량 최대 2.5 mg/kg이었다[10]. 터키 연구진은 중금속 추정 섭취량이 한도를 넘어 먹지 않는 것이 좋다고 했으나, 폴란드·스웨덴 22종 종합 평가는 위해가 없다고 보았다[11, 12]. 공공기관의 알레르기·잔류 정보는 확인하지 못함.\n\n먹는 것과 별개로, 성숙 포자를 대량으로 들이마시면 폐렴과 비슷한 말불버섯 포자증(lycoperdonosis)이 생길 수 있다[22, 23]. 1994년 미국 위스콘신에서는 이 종의 포자를 흡입한 16–19세 8명이 진료를 받았고, 포자 추출물 피부반응 연구도 있다[22, 24].")

compounds = [
 {"name": "Lycoperdic acid", "name_ko": "라이코퍼드산", "class": "비단백성 아미노산(4-히드록시글루탐산 유도체)", "role": "marker", "part": "자실체", "content_text": "이 종에서 유래한 아미노산으로 보고됨; 함량은 확인하지 못함[18]", "activity_ko": "드문 구조 때문에 합성 연구 대상이 됨; 생리활성 자료는 확인하지 못함[18]", "source": [18]},
 {"name": "Cinnamic acid", "name_ko": "신남산", "class": "페닐프로파노이드(비페놀성 유기산)", "role": "bioactive", "part": "자실체(포르투갈 야생 시료)", "content_text": "14.36 mg/kg(건조물), 이 종에서 검출된 유일한 페놀산 관련 성분[16]", "activity_ko": "페놀산 분석에서 검출; 이 종에서 별도 활성 시험은 확인하지 못함[16]", "source": [16]},
 {"name": "Phenolic compounds (total)", "name_ko": "총 페놀 화합물", "class": "페놀류(총량)", "role": "bioactive", "part": "자실체 추출물(터키 무을라 시료)", "content_text": "정량값은 초록에 없어 확인하지 못함[11]", "activity_ko": "네 가지 항산화 시험에서 높은 활성, 활성은 총 페놀·플라보노이드 함량과 강한 상관(시험관)[11]", "source": [11]},
 {"name": "Copper", "name_ko": "구리", "class": "무기질(미량원소)", "role": "nutrient", "part": "자실체(루마니아 도시 공원 시료)", "content_text": "도시 시료 91.0 mg/kg(초록 표기, 건조중으로 보임; 중앙값 여부는 확인하지 못함)[13]", "activity_ko": "폴란드·스웨덴 22종 비교에서 이 종이 구리를 가장 많이 축적하는 경향[12]", "source": [13, 12]},
 {"name": "Iron", "name_ko": "철", "class": "무기질(미량원소)", "role": "nutrient", "part": "자실체(루마니아 도시 공원 시료)", "content_text": "도시 시료 125(초록에 단위 일부 누락, 같은 문장의 mg/kg 건조중으로 보임; 중앙값 여부는 확인하지 못함)[13]", "activity_ko": "폴란드·스웨덴 비교에서 철을 가장 많이 축적하는 경향[12]", "source": [13, 12]},
 {"name": "Zinc", "name_ko": "아연", "class": "무기질(미량원소)", "role": "nutrient", "part": "자실체", "content_text": "스웨덴 식용버섯 비교에서 아연·구리 수준이 큰갓버섯과 함께 가장 높았다; 수치는 확인하지 못함[10]", "activity_ko": "폴란드·스웨덴 비교에서도 아연을 가장 많이 축적하는 경향[12]", "source": [10, 12]},
 {"name": "Magnesium", "name_ko": "마그네슘", "class": "무기질(다량원소)", "role": "nutrient", "part": "자실체", "content_text": "폴란드·스웨덴 22종 가운데 가장 높은 수준 경향; 수치는 확인하지 못함[12]", "activity_ko": "100 g 섭취 시 권장섭취량 충족률이 높은 원소로 평가됨(여러 종 종합)[12]", "source": [12]},
 {"name": "Silver", "name_ko": "은", "class": "원소(비필수)", "role": "contaminant", "part": "자실체(루마니아 도시 공원 시료)", "content_text": "도시 시료 4.68 mg/kg(초록 표기, 건조중으로 보임; 중앙값 여부는 확인하지 못함)[13]", "activity_ko": "도시 시료에서 대조지보다 높아 도시 오염 지표로 제안됨[13]", "source": [13]},
 {"name": "Cadmium", "name_ko": "카드뮴", "class": "유해 중금속", "role": "contaminant", "part": "자실체(폴란드 중서부 숲 시료)", "content_text": "평균 3.12 mg/kg(초록 표기; 기준은 초록에서 확인하지 못함)[14]; 제련소 주변에서 카드뮴 최고 수준(최대 20 mg/kg 건조물)을 보인 두 종 가운데 하나[8]", "activity_ko": "조사 16종 가운데 말뚝버섯과 함께 가장 높은 수준[14]", "source": [14, 8]},
 {"name": "Mercury", "name_ko": "수은", "class": "유해 중금속", "role": "contaminant", "part": "자실체(폴란드 열 곳)", "content_text": "0.57–4.5 µg/g(건조물), 지점 평균 0.91 ± 0.28–2.4 ± 0.4 µg/g[3]", "activity_ko": "생물농축계수 평균 28–110(범위 9.6–280)으로 수은 축적종으로 분류됨[3]", "source": [3]},
]

assays = [
 {"role": "literature", "compound": "Mercury (total Hg)", "compound_ko": "총수은", "part": "자실체(건조 분말, 폴란드 열 곳 2001–2008)", "content": "0.57–4.5 µg/g(건조물); 지점 평균 0.91 ± 0.28–2.4 ± 0.4 µg/g[3]", "method": "열분해–금 아말감–냉증기 원자흡광분광법(CV-AAS)",
  "conditions": {"instrument": "Mercury analyzer MA-2000 (Nippon Instruments Corporation)", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "냉증기 원자흡광(시료 열분해 후 금 울에 아말감·탈착)", "injection": "", "sample_prep": "식물 잔재·흙을 플라스틱 칼로 제거, 상온 통풍 2–3일 건조 후 65 ℃에서 48–96 h 건조, 마노 유발로 분쇄", "standard": "인증표준물질 CS-M-1(건조 버섯 자실체; 표시값 0.174 ± 0.018 µg/g)", "linearity": "", "lod": "0.005 µg Hg/g dw", "loq": "0.003 µg Hg/g dw(원문 표기 그대로)", "recovery": "인증표준물질 측정값 0.171 ± 0.008 µg/g(n = 3); 시료 10개마다 바탕시료 1개"},
  "rationale": "이 종은 수은 축적종이어서 총수은이 채집지 오염과 섭취 위해를 판단하는 핵심 품질 지표로 쓰였다[3].", "source": [3], "url": "https://pubmed.ncbi.nlm.nih.gov/22898887/", "source_kind": "paper"},
 {"role": "literature", "compound": "Cinnamic acid", "compound_ko": "신남산", "part": "자실체(포르투갈 야생 시료)", "content": "14.36 mg/kg(건조물)[16]", "method": "HPLC-DAD-ESI/MS",
  "conditions": {"instrument": "", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "광다이오드 배열 검출기 + 전자분무 이온화 질량분석(초록 표기)", "injection": "", "sample_prep": "", "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "16종 페놀산 비교 분석에서 이 종에서 검출된 유일한 성분이다[16]. 전문 확인 못함.", "source": [16], "url": "https://pubmed.ncbi.nlm.nih.gov/19425182/", "source_kind": "paper"},
 {"role": "literature", "compound": "Copper, iron, silver (and 16 other elements)", "compound_ko": "구리·철·은 등 19개 원소", "part": "자실체(루마니아 클루지나포카 도시 공원·대조지)", "content": "도시 시료 은 4.68, 구리 91.0, 철 125(초록 표기, mg/kg 건조중으로 보임)[13]", "method": "ICP-OES",
  "conditions": {"instrument": "", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "유도결합플라스마 발광분광법", "injection": "", "sample_prep": "", "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "도시 오염에 따른 원소 변화를 보는 지표로 쓰였고, 저자들은 이 종을 도시 무기 오염 지표종으로 제안했다[13]. 전문 확인 못함.", "source": [13], "url": "https://pubmed.ncbi.nlm.nih.gov/37245597/", "source_kind": "paper"},
]

d = {"slug": "lycoperdon-perlatum", "name_ko": "말불버섯", "name_en": "Common puffball (gem-studded puffball)", "scientific_name": "Lycoperdon perlatum Pers.",
     "aliases": ["봉오리먼지버섯", "말불버섯어린자실체", "common puffball", "warted puffball", "gem-studded puffball", "devil's snuff-box", "Puffball, Smut ball"],
     "sections": S, "compounds": compounds, "markers": [], "assays": assays, "nutrients": [], "production": [], "world": [], "gi": [], "orgs": [], "sources": sources}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
