import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
A = "2026-11-02"
WS = "WebSearch 검색 결과 요약으로만 확인, 원문은 이 환경에서 열지 못함"
S = [
 (1, "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 노르웨이단풍수액 행(Acer platanoides L.; Norway maple; 식물; 사용가능, 사용 조건 '사용가능부위 : 수액') 및 같은 목록의 다른 Acer 속 원료 행(로컬 원자료 I1020_20261013.json으로 대조)", "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "식품의약품안전처", "2026-10-13"),
 (2, "Hypoglycin A Concentrations in Maple Tree Species in the Netherlands and the Occurrence of Atypical Myopathy in Horses — J Vet Intern Med 2016 (PMID 26995161, PMC4913566, doi:10.1111/jvim.13927) — PMC 전문 확인; PubMed 표기에서 본문의 종 이름 서체가 빠져 있어 일부 수치의 종 대응은 문맥으로 판단", "https://pmc.ncbi.nlm.nih.gov/articles/PMC4913566/", "Journal of Veterinary Internal Medicine (PubMed Central)", A),
 (3, "Clinical Research Abstracts of the British Equine Veterinary Association Congress 2015 — 스웨덴 비정형 근육병증 농장의 hypoglycin A 분석 초록 (Equine Vet J 2015, PMID 26375998, doi:10.1111/evj.12486_49) — 초록만 확인", "https://pubmed.ncbi.nlm.nih.gov/26375998/", "Equine Veterinary Journal (PubMed)", A),
 (4, "Barringtogenol C-type Triterpenoid Saponins from the Stem Bark of Norway Maple (Acer platanoides) — Planta Med 2020;86(1):70-77 (PMID 31671467, doi:10.1055/a-1031-7283) — 초록만 확인", "https://pubmed.ncbi.nlm.nih.gov/31671467/", "Planta Medica (PubMed)", A),
 (5, "Biochemical characteristics of urban maple trees — Saudi J Biol Sci 2020;27(11):2912-2916 (PMID 33100846, PMC7569143, doi:10.1016/j.sjbs.2020.09.010) — PMC 전문 확인(본문의 종 이름 서체가 빠져 있어 수치는 초록 기준)", "https://pmc.ncbi.nlm.nih.gov/articles/PMC7569143/", "Saudi Journal of Biological Sciences (PubMed Central)", A),
 (6, "Photosynthetic pigments in developing seeds of Acer platanoides and Acer pseudoplatanus — Sci Rep 2026;16 (PMID 41865034, PMC13149657, doi:10.1038/s41598-026-44414-7) — 초록 확인", "https://pubmed.ncbi.nlm.nih.gov/41865034/", "Scientific Reports (PubMed)", A),
 (7, "Norway maple displays greater seasonal growth and phenotypic plasticity to light than native sugar maple — Tree Physiol 2012;32(11):1339-47 (PMID 23076822, doi:10.1093/treephys/tps092) — 초록 확인", "https://pubmed.ncbi.nlm.nih.gov/23076822/", "Tree Physiology (PubMed)", A),
 (8, "Ecophysiological attributes of the native Acer saccharum and the exotic Acer platanoides in urban oak forests in Pennsylvania, USA — Tree Physiol 1995;15(11):739-46 (PMID 14965992, doi:10.1093/treephys/15.11.739) — 초록 확인", "https://pubmed.ncbi.nlm.nih.gov/14965992/", "Tree Physiology (PubMed)", A),
 (9, "First Report of Powdery Mildew (Sawadaea bicornis) on Norway Maple (Acer platanoides) in North America — Plant Dis 2003;87(4):451 (PMID 30831859, doi:10.1094/PDIS.2003.87.4.451A) — 초록 확인", "https://pubmed.ncbi.nlm.nih.gov/30831859/", "Plant Disease (PubMed)", A),
 (10, "Shared mycorrhizae but distinct communities of other root-associated microbes on co-occurring native and invasive maples — PeerJ 2019;7:e7295 (PMID 31392089, PMC6677121, doi:10.7717/peerj.7295) — 초록 확인", "https://pubmed.ncbi.nlm.nih.gov/31392089/", "PeerJ (PubMed)", A),
 (11, "Biochar mitigates allelopathic effects in temperate trees — Ecol Appl 2023;33(4):e2832 (PMID 36864680, doi:10.1002/eap.2832) — 초록 확인", "https://pubmed.ncbi.nlm.nih.gov/36864680/", "Ecological Applications (PubMed)", A),
 (12, "Ion-mediated enhancement of xylem hydraulic conductivity in four Acer species: relationships with ecological and anatomical features — Tree Physiol 2012;32(12):1434-41 (PMID 23138592, doi:10.1093/treephys/tps107) — 초록 확인", "https://pubmed.ncbi.nlm.nih.gov/23138592/", "Tree Physiology (PubMed)", A),
 (13, "Water Availability and Hydraulic Strategies Control Leaf Thermoregulation and Damage During Heat Stress and Recovery in Temperate Tree Species — Plant Cell Environ 2026;49(9):6296-6310 (PMID 42144719, PMC13436522, doi:10.1111/pce.70605) — 초록 확인", "https://pubmed.ncbi.nlm.nih.gov/42144719/", "Plant, Cell & Environment (PubMed)", A),
 (14, "Proteome analysis of Norway maple (Acer platanoides L.) seeds dormancy breaking and germination: influence of abscisic and gibberellic acids — BMC Plant Biol 2009;9:48 (PMID 19413897, PMC2688491, doi:10.1186/1471-2229-9-48) — 초록 확인", "https://pubmed.ncbi.nlm.nih.gov/19413897/", "BMC Plant Biology (PubMed)", A),
 (15, "Proteomic analysis of embryogenesis and the acquisition of seed dormancy in Norway maple (Acer platanoides L.) — Int J Mol Sci 2014;15(6):10868-91 (PMID 24941250, PMC4100186, doi:10.3390/ijms150610868) — 초록 확인", "https://pubmed.ncbi.nlm.nih.gov/24941250/", "International Journal of Molecular Sciences (PubMed)", A),
 (16, "Changes in genomic 5-methylcytosine level mirror the response of orthodox (Acer platanoides L.) and recalcitrant (Acer pseudoplatanus L.) seeds to severe desiccation — Tree Physiol 2018;38(4):617-629 (PMID 29121348, doi:10.1093/treephys/tpx134) — 초록 확인", "https://pubmed.ncbi.nlm.nih.gov/29121348/", "Tree Physiology (PubMed)", A),
 (17, "Impact of cryopreservation on DNA damage in Acer platanoides L. seeds evaluated by the comet assay — Sci Rep 2025;15:24081 (PMID 40617861, PMC12228746, doi:10.1038/s41598-025-08476-3) — 초록 확인", "https://pubmed.ncbi.nlm.nih.gov/40617861/", "Scientific Reports (PubMed)", A),
 (18, "Phytoextraction of potentially toxic elements by six tree species growing on hazardous mining sludge — Environ Sci Pollut Res Int 2017;24(28):22183-22195 (PMID 28791581, PMC5629231, doi:10.1007/s11356-017-9842-3) — 초록 확인", "https://pubmed.ncbi.nlm.nih.gov/28791581/", "Environmental Science and Pollution Research (PubMed)", A),
 (19, "The within-season and between-tree distribution of imidacloprid trunk-injected into Acer platanoides (Sapindales: Sapindaceae) — J Econ Entomol 2013;106(2):874-82 (PMID 23786077, doi:10.1603/ec12329) — 초록 확인", "https://pubmed.ncbi.nlm.nih.gov/23786077/", "Journal of Economic Entomology (PubMed)", A),
 (20, "Analytical study of azadirachtin and 3-tigloylazadirachtol residues in foliage and phloem of hardwood tree species by liquid chromatography-electrospray mass spectrometry — J Agric Food Chem 2011;59(15):8070-7 (PMID 21726086, doi:10.1021/jf2023947) — 초록 확인", "https://pubmed.ncbi.nlm.nih.gov/21726086/", "Journal of Agricultural and Food Chemistry (PubMed)", A),
 (21, "Antiprotease activity of selected Slovak medicinal plants — Pharmazie 2010;65(2):137-40 (PMID 20225660) — 초록 확인", "https://pubmed.ncbi.nlm.nih.gov/20225660/", "Die Pharmazie (PubMed)", A),
 (22, "Inhibitory effects on bacterial growth and beta-ketoacyl-ACP reductase by different species of maple leaf extracts and tannic acid — Phytother Res 2010;24 Suppl 1:S35-41 (PMID 19444866, doi:10.1002/ptr.2873) — 초록 확인", "https://pubmed.ncbi.nlm.nih.gov/19444866/", "Phytotherapy Research (PubMed)", A),
 (23, "Uses of tree saps in northern and eastern parts of Europe — Acta Soc Bot Pol 2012;81(4):343-357 (doi:10.5586/asbp.2012.036) — " + WS, "https://pbsociety.org.pl/journals/index.php/asbp/article/view/959", "Acta Societatis Botanicorum Poloniae", A),
 (24, "Sugar content in the sap of birches, hornbeams and maples in southeastern Poland — Cent Eur J Biol(Open Life Sciences) 2014;9(4):410-416 (doi:10.2478/s11535-013-0284-8) — " + WS, "https://doi.org/10.2478/s11535-013-0284-8", "Central European Journal of Biology", A),
 (25, "Determination of Bioactive Compounds and Mineral Substances in Latvian Birch and Maple Saps — Proc Latvian Acad Sci B 2013 (doi:10.2478/prolas-2013-0069) — " + WS, "https://reference-global.com/article/10.2478/prolas-2013-0069", "Proceedings of the Latvian Academy of Sciences, Section B", A),
 (26, "The xylem sap of maple (Acer platanoides) trees — sap obtained by a novel method shows changes with season and height (학술지·연도는 확인하지 못함; AGRIS 서지 기록) — " + WS, "https://agris.fao.org/search/es/records/65de42de7c7033e84bea5eb6", "AGRIS(FAO) 서지 기록", A),
 (27, "폴란드 수목 수액 6종(자작나무 2종·서어나무·노르웨이단풍·버드나무 등)의 당 조성 분석 논문(Żywność. Nauka. Technologia. Jakość 게재, 제목·연도 확인하지 못함; HPTLC·HPLC-ELSD) — " + WS, "https://journal.pttz.org/?p=2712", "Polskie Towarzystwo Technologów Żywności", A),
]
src = [{"n": n, "title": t, "url": u, "publisher": p, "accessed": a} for n, t, u, p, a in S]

sec = [
("overview", "한눈에 보기",
"노르웨이단풍(Acer platanoides L., 영문 Norway maple)은 무환자나무과(Sapindaceae) 단풍나무속의 잎지는 큰키나무로, 식약처 식품원료 목록에는 '노르웨이단풍수액'이라는 원료명으로 올라 있다[1]. 목록에서 이 원료는 '사용가능' 원료이며 사용 조건은 '사용가능부위 : 수액'이다[1]. 따라서 식품에 쓸 수 있는 부위는 줄기에서 받는 수액뿐이고, 잎·씨앗·나무껍질은 이 원료의 사용 부위가 아니다[1]. 이 종을 원재료로 하는 건강기능식품 고시형 원료는 확인하지 못함.\n\n"
"유럽 북부·동부에서는 자작나무와 함께 이 종의 봄 수액을 마시거나 발효해 왔다는 민족식물학 보고가 있다(검색 요약으로만 확인)[23]. 폴란드 남동부 조사에서 이 종의 수액 당 함량은 약 3.2%였고 단풍나무류 수액의 당은 자당이었다고 요약되어 있으나, 원문은 확인하지 못함[24]. 다른 폴란드 분석은 총당 1.083 g/100 mL로 더 낮게 보고해, 출처끼리 값이 다르다[27]. 학술 연구는 대부분 침입종 생태·씨앗 생리·나무 오염물질 흡수에 관한 것이며, 수액을 마신 사람에 대한 임상시험은 확인하지 못함."),
("history", "이용의 역사",
"유럽 북부·동부의 수목 수액 이용을 정리한 2012년 총설은 가장 많이 쓰인 종으로 자작나무 두 종과 노르웨이단풍을 꼽았다고 요약되어 있다[23]. 같은 총설은 단풍 수액이 자작나무 수액보다 덜 채취되지만 당이 더 많아 단맛으로 귀하게 여겨졌고, 생수액으로 마시거나 음식·음료에 넣고 가벼운 술로 발효했다고 전한다(검색 요약으로만 확인)[23]. 러시아·우크라이나·벨라루스·발트 3국에서는 최근까지 수액 채취가 이어졌고 스칸디나비아·폴란드 등의 기록은 주로 과거의 것이라고 한다[23].\n\n"
"북미에는 1756년 무렵 가로수로 들어왔고, 어릴 때 빨리 자라며 포장도로와 건조한 흙을 견뎌 미국 북부와 캐나다에 널리 심겼다[9]. 이후 북미 동부 숲에서 가장 침입성이 강한 나무의 하나가 되어 토착종 설탕단풍의 갱신을 줄인다는 보고가 나왔다[7]. 국내에서는 이 종의 수액이 식품원료 목록에 사용가능 원료로 올라 있다는 것만 확인했고, 국내 도입 시기와 수액 유통 이력은 확인하지 못함[1]."),
("biology", "식물학적 특징",
"노르웨이단풍은 단풍나무속(Acer)의 한 종으로, 식품원료 목록에는 학명 Acer platanoides L.과 영문명 Norway maple로 적혀 있다[1]. 북미의 도시 참나무숲에서 함께 자란 설탕단풍과 비교했을 때 연평균 키 생장이 19.26 ± 3.22 cm로 설탕단풍(10.01 ± 1.69 cm)의 약 두 배였고, 잎 수명이 12일 길었다[8]. 같은 연구에서 광합성·질소와 인 이용 효율·물 이용 효율이 설탕단풍보다 높았다[8]. 숲 틈새를 흉내 낸 빛 조건에서는 가을 늦게까지 줄기 신장을 이어 가 더 크게 자랐다[7].\n\n"
"물관 수액의 이온 조성이 바뀌면 물관 수리전도도가 달라지는 '이온 효과'가 이 종에서 23.1%로, 그늘지고 습한 곳의 단풍나무류보다 컸다[12]. 고온·가뭄 실험에서는 기공을 일찍 닫는 등수(isohydric) 전략을 보였고, 잎 냉각이 약해 잎 손상이 심하고 회복이 더뎠다[13]. 씨앗은 건조를 견디는 정통형(orthodox) 씨앗이며, 씨앗이 자라는 동안 엽록소 a가 엽록소 b보다 많고 형태 형성기 이후 약 8배 줄었다[6, 16]."),
("related_species", "같은 속의 다른 종",
"식약처 식품원료 목록에는 이 종 말고도 단풍나무속 원료가 여럿 있으며, 고로쇠나무(A. pictum subsp. mono)·설탕단풍(A. saccharum)·단풍나무(A. palmatum)·개버즘단풍나무(A. pseudoplatanus)·캄페스트레단풍(A. campestre) 등이 수액을 사용 부위로 한다[1]. 신나무(A. ginnala)와 글라브룸단풍(A. glabrum)은 잎, 산겨릅나무(A. tegmentosum)는 가지가 사용 부위이고 산겨릅나무에는 식품 유형별 사용량 제한이 붙어 있다[1]. 이 원료들은 학명이 다른 별개 원료이므로 그 성분·당도 자료를 노르웨이단풍수액에 옮겨 쓸 수 없다[1].\n\n"
"유럽에서 말의 비정형 근육병증 원인 물질인 hypoglycin A는 개버즘단풍나무(A. pseudoplatanus)의 씨앗·새싹·잎 대부분에서 검출되었지만, 노르웨이단풍과 캄페스트레단풍(A. campestre, hedge maple) 시료에서는 검출되지 않았다[2]. 스웨덴 농장 조사에서도 개버즘단풍나무 식물체에서는 검출되고 노르웨이단풍에서는 검출되지 않았다[3]. 씨앗 생리에서도 두 종은 달라서, 노르웨이단풍 씨앗은 건조를 견디고 개버즘단풍나무 씨앗은 건조에 약한 난저장성(recalcitrant)이다[16]. 북미에서는 같은 숲에 자라는 설탕단풍과 뿌리 미생물 군집이 달랐다[10]."),
("cultivation", "재배와 채취",
"이 종은 어릴 때 빨리 자라고 포장도로와 건조한 흙을 잘 견뎌 북미에서 가로수·그늘나무로 널리 심겼다[9]. 잎이 떨어져 쌓인 흙은 은단풍·종이자작나무 묘목 생장을 억제하는 타감작용을 보였고, 바이오차를 넣으면 이 효과가 크게 줄었다[11]. 북미 서부에서는 2002년 어린 나무에서 흰가루병(Sawadaea bicornis)이 처음 보고되었다[9]. 아시아긴뿔하늘소 박멸 사업에서는 이 종의 줄기에 살충제 이미다클로프리드를 주입하기도 했다[19].\n\n"
"씨앗은 휴면이 깊어 저온 층적 처리로 휴면을 깨며, 이 과정에 아브시스산과 지베렐린이 관여한다[14]. 씨앗 배는 개화 후 10–13주에 형태가 만들어지고 14–22주에 성숙하며, 22주에 완전히 익는다[15]. 수분 함량을 맞추지 않은 초저온 보존은 씨앗 DNA를 손상시켰다[17]. 수액 채취 시기·방법·나무당 채취량에 관한 이 종의 공식 자료나 논문 원문은 확인하지 못함. 독일 연구는 겨울철 물관 수액의 자당이 10–25 mM이고 싹이 틀 무렵 최저로 떨어졌다고 요약되어 있으나 원문은 확인하지 못함[26]."),
("processing", "가공과 이용",
"유럽 북부·동부에서 이 종의 수액은 생으로 마시거나 음식·음료 재료로 쓰고, 가볍게 발효해 술로 만들었다고 요약되어 있다(원문 확인 못함)[23]. 폴란드 남동부 수액 연구의 저자들은 지역의 단풍나무·자작나무 자원을 이용한 소규모 시럽 산업이 산주의 부수입원이 될 수 있다고 제안했다고 요약되어 있다[24]. 라트비아 연구는 노르웨이단풍 수액이 자작나무 수액보다 단백질과 항산화 활성이 높았고, 적정산도가 0.70 mmol NaOH/L였다고 요약된다(원문 확인 못함)[25].\n\n"
"수액 성분은 같은 종이라도 채취 시기·나무에 따라 크게 달라질 수 있어, 총당이 약 3.2%라는 보고와 1.083 g/100 mL라는 보고가 함께 있다[24, 27]. 국내 식품원료 목록에서 이 원료는 '수액' 부위로만 올라 있으며, 농축·시럽 같은 가공 형태가 따로 적혀 있지는 않다[1]. 식약처 「식품 등의 생산실적」에서 이 원료 이름의 품목은 확인하지 못함. 국내 제품 유통 규모와 가공 기준도 확인하지 못함."),
("genetics", "유전과 육종",
"이 종의 핵 유전체 조립이나 엽록체 유전체 해독 결과는 PubMed 검색에서 확인하지 못함. 유전·분자 연구는 주로 씨앗에 집중되어 있다[14, 15, 16, 17]. 씨앗 휴면 해제와 발아 과정에서 질량분석으로 44개 단백질 변화가 확인되었고, 아브시스산은 주로 단백질을 줄이고 지베렐린은 늘렸다[14]. 배 발생 단계에서는 형태 형성기 17개, 성숙기 33개 단백질 점이 확인되었고, 글리신이 많은 RNA 결합 단백질과 프로테아솜 단백질이 휴면 획득에 관여할 가능성이 제시되었다[15].\n\n"
"건조 스트레스를 받은 씨앗에서 전체 5-메틸시토신(m5C) 수준 변화는 조직과 씨앗 유형에 따라 달랐고, 수분 3.5%까지 강하게 말린 정통형 씨앗에서 나온 묘목에서만 그 변화가 남았다[16]. 초저온 보존한 씨앗에서는 DNA 가닥 절단과 8-oxoG가 검출되었고 8-oxoG는 씨앗 생존율과 음의 상관을 보였다[17]. 수액 형질(당도·수액량)을 겨냥한 품종 육성 자료는 확인하지 못함."),
("safety", "안전성",
"식품원료 목록에서 이 원료는 수액만 쓸 수 있으므로 잎·씨앗·나무껍질을 식품에 쓰는 것은 목록의 사용 조건 밖이다[1]. 말 근육병증을 일으키는 hypoglycin A는 네덜란드 조사에서 노르웨이단풍·캄페스트레단풍 시료(씨앗·잎·새싹)에서 검출되지 않았고, 정량한계는 잎 1 mg/kg, 씨앗 10 mg/kg이었다[2]. 스웨덴 조사에서도 이 종의 열매·묘목·꽃·잎에서 검출되지 않았다[3]. 다만 두 조사 모두 수액은 분석하지 않았으므로 수액의 hypoglycin A 자료는 확인하지 못함.\n\n"
"오염된 광산 침전토에서 키운 실험에서 이 종은 아연을 지상부에 많이 모아(최고 5,732 mg/kg) 아연 생물농축계수 8.99를 보였다[18]. 해충 방제를 위해 줄기에 주입한 이미다클로프리드는 잔가지에서 대부분 1 ppm 미만이었지만 잎에서는 최고 49 ppm까지 남았다[19]. 천연 살충제 아자디라크틴의 잔류 분석법에서 노르웨이단풍 잎의 정량한계는 0.05 mg/kg이었다[20]. 이런 나무에서 받은 수액의 잔류 여부는 확인하지 못함. 식약처·농촌진흥청 등 국내 공공기관의 이 종 수액에 대한 알레르기·독성 정보는 확인하지 못함. 잎 추출물의 항균·단백분해효소 억제 활성은 시험관 결과일 뿐이다[21, 22]."),
]
sections = [{"key": k, "title": t, "body": b} for k, t, b in sec]

compounds = [
 {"name": "Sucrose", "name_ko": "자당(수크로스)", "class": "이당류", "role": "nutrient", "part": "수액",
  "content_text": "폴란드 남동부 봄 수액의 당 함량 약 3.2%, 단풍나무류 수액의 당은 자당(검색 요약으로만 확인)[24]; 다른 폴란드 분석은 총당 1.083 g/100 mL, 자당이 우세(검색 요약으로만 확인)[27]; 겨울 물관 수액 10–25 mM(통나무 조각에서 얻은 수액, 검색 요약)[26]",
  "activity_ko": "수액 단맛의 주성분[24, 27]", "source": [24, 26, 27]},
 {"name": "Quebrachitol", "name_ko": "퀘브라키톨", "class": "사이클리톨(당알코올)", "role": "nutrient", "part": "물관 수액(통나무 조각에서 얻은 수액)",
  "content_text": "자당과 함께 물관 수액의 주성분, 약 7 mM까지(검색 요약으로만 확인, 원문 확인 못함)[26]",
  "activity_ko": "이 종 수액에서의 생리 활성은 확인하지 못함[26]", "source": [26]},
 {"name": "Hypoglycin A", "name_ko": "하이포글리신 A", "class": "비단백질 아미노산(독성 물질)", "role": "marker", "part": "씨앗·잎·새싹·꽃(수액은 분석 안 됨)",
  "content_text": "노르웨이단풍·캄페스트레단풍 시료 41건(씨앗 29·잎 11·새싹 1, 두 종 합계)에서 검출되지 않음(정량한계 잎 1 mg/kg, 씨앗 10 mg/kg)[2]; 스웨덴 농장의 열매·묘목·꽃·잎에서 검출되지 않음[3]",
  "activity_ko": "개버즘단풍나무 등에서 말 비정형 근육병증의 원인 물질로 지목되며, 대사물 MCPA가 아실-CoA 탈수소효소를 억제한다[2]", "source": [2, 3]},
 {"name": "Acerplatanoside A", "name_ko": "아세르플라타노사이드 A(-D)", "class": "바링토게놀 C형 트리테르펜 사포닌", "role": "bioactive", "part": "줄기 껍질(식품원료 사용 부위 아님)",
  "content_text": "줄기 껍질에서 새 사포닌 4종(acerplatanoside A–D)과 알려진 화합물 22종 분리(함량 확인하지 못함)[4]",
  "activity_ko": "화합물 1·3·4가 사람 암세포주 4종에 IC50 9.4–39.5 µM 세포독성(세포)[4]", "source": [4]},
 {"name": "Proanthocyanidins", "name_ko": "축합형 탄닌", "class": "폴리페놀(탄닌)", "role": "bioactive", "part": "잎(식품원료 사용 부위 아님)",
  "content_text": "도시 가로수 잎의 축합형 탄닌이 대조보다 7월 1.24, 8월 0.94(완충지대)·0.76(도로변) 감소(초록 기준; 본문 단위 mg/g 건물중, 본문에는 8월 도로변 0.78로 적힘; 절대 함량은 확인하지 못함)[5]",
  "activity_ko": "대기오염 적응 반응에 관여하는 것으로 해석, 폴리페놀산화효소 활성과 양의 상관(r = 0.94)[5]", "source": [5]},
 {"name": "Ascorbic acid", "name_ko": "아스코르브산(비타민 C)", "class": "비타민", "role": "nutrient", "part": "잎(식품원료 사용 부위 아님)",
  "content_text": "도시 가로수 잎에서 DCPIP 적정으로 측정, 생장기 동안 감소(이 종의 수치는 본문에서 종 이름이 빠져 확인하지 못함)[5]",
  "activity_ko": "대기오염에 대한 항산화 방어 성분으로 해석[5]", "source": [5]},
 {"name": "Chlorophyll a", "name_ko": "엽록소 a", "class": "광합성 색소", "role": "bioactive", "part": "씨앗(특히 떡잎; 식품원료 사용 부위 아님)",
  "content_text": "발달 중인 씨앗에서 엽록소 b보다 많고, 형태 형성기에 정점 후 약 8배 감소(절대 함량은 확인하지 못함)[6]",
  "activity_ko": "씨앗의 정통형·난저장성 차이와 수명에 관련될 가능성 논의[6]", "source": [6]},
 {"name": "Zinc", "name_ko": "아연", "class": "무기질(미량원소)", "role": "nutrient", "part": "지상부(오염 침전토 재배 묘목; 수액 아님)",
  "content_text": "광산 침전토에서 키운 묘목 지상부 최고 5,732 mg/kg, 생물농축계수 8.99, 이동계수 1.5[18]",
  "activity_ko": "오염 토양에서 아연을 많이 흡수해 정화 식물 후보로 제시됨; 수액 함량은 확인하지 못함[18]", "source": [18]},
]

assays = [
 {"role": "literature", "compound": "Hypoglycin A", "compound_ko": "하이포글리신 A", "part": "씨앗·잎·새싹(수액 아님)",
  "content": "노르웨이단풍·캄페스트레단풍 시료(두 종 합계 씨앗 29·잎 11·새싹 1건)에서 검출되지 않음(정량한계 미만)[2]",
  "method": "LC-MS/MS",
  "conditions": {"instrument": "LC–MS/MS(기종 원문 미기재)", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "",
   "detection": "MS/MS 2개 전이 m/z 142.1→74.1, 142.1→96.0(머무름 시간·이온비로 확인)", "injection": "10 μL",
   "sample_prep": "씨앗은 Retsch 분쇄, 잎은 액체질소 냉동 분쇄; 균질 시료 1 g을 milliQ 물 10 mL로 1시간 진탕 추출, 5000 g 10 °C 10분 원심; 씨앗 추출액은 10–100배 희석",
   "standard": "s-hypoglycin A 표준품(milliQ 물), 다점 검량",
   "linearity": "0.01–2 mg/L(잔차 <20%), 비희석 추출액 0.1–20 mg/kg·100배 희석 10–2000 mg/kg에 해당",
   "lod": "", "loq": "잎 1 mg/kg, 씨앗 10 mg/kg",
   "recovery": "잎 1 mg/kg 첨가 72%(RSD 11%), 씨앗 10 mg/kg 첨가 82%(RSD 7%); 본 시료와 함께 분석한 첨가 씨앗 73–95%"},
  "rationale": "단풍나무속 일부 종의 독성 지표로 쓰이는 성분이며, 이 종 시료에서 검출되지 않아 같은 속의 개버즘단풍나무와 구별되는 안전 지표다; 수액은 분석하지 않았다[2]",
  "source": [2], "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC4913566/", "source_kind": "paper"},
 {"role": "literature", "compound": "Hypoglycin A", "compound_ko": "하이포글리신 A", "part": "열매·묘목·꽃·잎(수액 아님)",
  "content": "노르웨이단풍 식물체에서 검출되지 않음(개버즘단풍나무에서는 검출)[3]",
  "method": "UHPLC-MS/MS(댄실 클로라이드 유도체화)",
  "conditions": {"instrument": "", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "",
   "detection": "유도체 HG-DNS [M+H]+ 선택반응검지(SRM)", "injection": "", "sample_prep": "댄실 클로라이드(DNS) 화학 유도체화",
   "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "비정형 근육병증 발생 농장에서 이 종과 개버즘단풍나무를 함께 분석한 안전 지표; 초록만 확인, 전문 확인 못함[3]",
  "source": [3], "url": "https://pubmed.ncbi.nlm.nih.gov/26375998/", "source_kind": "paper"},
 {"role": "literature", "compound": "Sucrose", "compound_ko": "자당(총당)", "part": "수액",
  "content": "총당 1.083 g/100 mL, 자당이 우세(검색 요약)[27]",
  "method": "HPTLC·HPLC-ELSD",
  "conditions": {"instrument": "", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "증발광산란검출기(ELSD)",
   "injection": "", "sample_prep": "", "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "수액의 단맛과 시럽 원료 가치를 정하는 주성분이다; 검색 요약으로만 확인, 전문 확인 못함[27, 24]",
  "source": [27, 24], "url": "https://journal.pttz.org/?p=2712", "source_kind": "paper"},
]

d = {"slug": "acer-platanoides", "name_ko": "노르웨이단풍수액", "name_en": "Norway maple",
     "scientific_name": "Acer platanoides L.", "aliases": ["Norway maple", "Acer platanoides L."],
     "sections": sections, "compounds": compounds, "markers": [], "assays": assays, "nutrients": [],
     "production": [], "world": [], "gi": [], "orgs": [], "sources": src}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
print("ok", len(src), len(compounds))
