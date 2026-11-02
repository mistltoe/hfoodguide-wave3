import json
from pathlib import Path
P=Path(__file__).resolve().parent.parent
PM="https://pubmed.ncbi.nlm.nih.gov/{}/"
A="2026-11-02"
I1020="https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020"
src=[
 (1,"식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 도깨비바늘잎 행(학명 Bidens bipinnata L. / Bidens decompositus Wall., 이명 좀도깨비바늘, 영문명 Spanish needle, 분류 식품원료(A코드)·식물, 부위 잎, '사용가능', 사용 조건 '사용가능부위 : 잎'). 로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json",I1020,"식품의약품안전처","2026-10-13"),
 (2,"식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 같은 속 원료 행: 가막사리잎·가막사리순(Bidens tripartita L., '사용가능부위 : 잎'), 구와가막사리잎·순(Bidens radiata var. pinnatifida, '사용가능부위 : 잎'), 까치발순(Bidens parviflora Willd., 이명 두가래도깨비바늘, '사용가능부위 : 순'), 털도깨비바늘잎(Bidens biternata, 이명 넓은잎가막사리, '사용가능부위 : 잎'), 미국가막사리잎(Bidens frondosa L.), Arizona beggarticks잎(Bidens aurea), 울산도깨비바늘잎(Bidens pilosa, 영문명 Picao Preto, '제한적사용', '제한적사용가능부위 : 잎'). 로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json",I1020,"식품의약품안전처","2026-10-13"),
 (3,"Untargeted Metabolomics-Based Analysis of Metabolic Differences in Different Parts of Bidens bipinnata L. Chem Biodivers 2026;23(10):e71819. doi:10.1002/cbdv.71819 (PMC13670983, 전문 확인)",PM.format(42878360),"Chemistry & Biodiversity (PubMed)",A),
 (4,"[Quality evaluation of Bidentis Herba derived from different original plants based on HPLC fingerprints, characteristic chromatograms, multi-component content determination combined with chemical pattern recognition]. Zhongguo Zhong Yao Za Zhi 2025;50(15):4284-4292. doi:10.19540/j.cnki.cjcmm.20250520.201 (초록만 확인)",PM.format(41084445),"China Journal of Chinese Materia Medica (PubMed)",A),
 (5,"Optimized MaxEnt model predicts potential suitable habitats of Bidens bipinnata in China under climate change scenario. Front Plant Sci 2025;16:1702523. doi:10.3389/fpls.2025.1702523 (초록 확인)",PM.format(41477264),"Frontiers in Plant Science (PubMed)",A),
 (6,"Analysis of the chloroplast genome and phylogenetic evolution of Bidens pilosa. BMC Genomics 2023;24(1):113. doi:10.1186/s12864-023-09195-7 (PMC10015693, 전문 확인 — B. bipinnata 포함 3종 엽록체 유전체)",PM.format(36918765),"BMC Genomics (PubMed)",A),
 (7,"[Cytologic study of Bidens bipinnata L]. Zhongguo Zhong Yao Za Zhi 1990;15(2):72-74. (초록 확인)",PM.format(2390174),"China Journal of Chinese Materia Medica (PubMed)",A),
 (8,"First Report of Powdery Mildew on Spanish Needles (Bidens bipinnata) Caused by Podosphaera xanthii in Korea. Plant Dis 2013;97(10):1385. doi:10.1094/PDIS-10-12-0966-PDN",PM.format(30722155),"Plant Disease (PubMed)",A),
 (9,"Responses of wild plant species to polycyclic aromatic hydrocarbons in soil. J Environ Monit 2009;11(9):1664-72. doi:10.1039/b906560a",PM.format(19724837),"Journal of Environmental Monitoring (PubMed)",A),
 (10,"Soil microbial carbon utilization, enzyme activities and nutrient availability responses to Bidens pilosa and a non-invasive congener under different irradiances. Sci Rep 2017;7(1):11309. doi:10.1038/s41598-017-11707-x",PM.format(28900190),"Scientific Reports (PubMed)",A),
 (11,"Unconventional Edible Plants of the Amazon: Bioactive Compounds, Health Benefits, Challenges, and Future Trends. Foods 2024;13(18):2925. doi:10.3390/foods13182925 (PMC11431067, 전문 확인 — 2.5절 Bidens bipinnata)",PM.format(39335854),"Foods (PubMed)",A),
 (12,"New acetylenic glucosides from Bidens bipinnata LINNE. Chem Pharm Bull 2004;52(4):439-40. doi:10.1248/cpb.52.439",PM.format(15056959),"Chemical & Pharmaceutical Bulletin (PubMed)",A),
 (13,"New flavanone and chalcone glucosides from Bidens bipinnata Linn. J Asian Nat Prod Res 2005;7(1):67-70. doi:10.1080/10286020310001617147",PM.format(15621604),"Journal of Asian Natural Products Research (PubMed)",A),
 (14,"Phenolics from Bidens bipinnata and their amylase inhibitory properties. Fitoterapia 2012;83(7):1169-75. doi:10.1016/j.fitote.2012.07.005",PM.format(22814126),"Fitoterapia (PubMed)",A),
 (15,"[Chemical constituents from Bidens bipinnata]. Zhongguo Zhong Yao Za Zhi 2014;39(10):1838-44. (초록 확인)",PM.format(25282892),"China Journal of Chinese Materia Medica (PubMed)",A),
 (16,"Enrichment of flavonoid-rich extract from Bidens bipinnata L. by macroporous resin using response surface methodology, UHPLC-Q-TOF MS/MS-assisted characterization and comprehensive evaluation of its bioactivities by analytical hierarchy process. Biomed Chromatogr 2020;34(11):e4933. doi:10.1002/bmc.4933",PM.format(32598044),"Biomedical Chromatography (PubMed)",A),
 (17,"Tissue distribution and molecular docking research on the active components of Bidens bipinnata L. against hyperlipidemia. Biomed Chromatogr 2021;35(4):e5026. doi:10.1002/bmc.5026",PM.format(33169423),"Biomedical Chromatography (PubMed)",A),
 (18,"Protective effect of total flavonoids from Bidens bipinnata L. against carbon tetrachloride-induced liver injury in mice. J Pharm Pharmacol 2007;59(7):1017-25. doi:10.1211/jpp.59.7.0015",PM.format(17637198),"Journal of Pharmacy and Pharmacology (PubMed)",A),
 (19,"Protective effects of total flavonoids of Bidens bipinnata L. against carbon tetrachloride-induced liver fibrosis in rats. J Pharm Pharmacol 2008;60(10):1393-402. doi:10.1211/jpp/60.10.0016",PM.format(18812033),"Journal of Pharmacy and Pharmacology (PubMed)",A),
 (20,"Total flavonoids of Bidens bipinnata L. a traditional Chinese medicine inhibits the production of inflammatory cytokines of vessel endothelial cells stimulated by sera from Henoch-Schönlein purpura patients. J Pharm Pharmacol 2012;64(6):882-7. doi:10.1111/j.2042-7158.2012.01480.x",PM.format(22571267),"Journal of Pharmacy and Pharmacology (PubMed)",A),
 (21,"Flavonoids-rich extract from Bidens bipinnata L. protects pancreatic β-cells against oxidative stress-induced apoptosis through intrinsic and extrinsic pathways. J Ethnopharmacol 2021;275:114097. doi:10.1016/j.jep.2021.114097",PM.format(33823164),"Journal of Ethnopharmacology (PubMed)",A),
 (22,"Serum metabonomics coupled with HPLC-LTQ/orbitrap MS and multivariate data analysis on the ameliorative effects of Bidens bipinnata L. in hyperlipidemic rats. J Ethnopharmacol 2020;262:113196. doi:10.1016/j.jep.2020.113196",PM.format(32730873),"Journal of Ethnopharmacology (PubMed)",A),
 (23,"Overall metabolic network analysis of urine in hyperlipidemic rats treated with Bidens bipinnata L. Biomed Chromatogr 2023;37(1):e5509. doi:10.1002/bmc.5509",PM.format(36097410),"Biomedical Chromatography (PubMed)",A),
 (24,"Study on in vitro anti-tumor activity of Bidens bipinnata L. extract. Afr J Tradit Complement Altern Med 2013;10(3):543-9. (PMC3777599)",PM.format(24146487),"AJTCAM (PubMed)",A),
 (25,"The inhibitory effect of Binens bipinnata L. extract on U14 tumour in mice. Afr J Tradit Complement Altern Med 2013;10(4):66-9. doi:10.4314/ajtcam.v10i4.11",PM.format(24146503),"AJTCAM (PubMed)",A),
 (26,"Isoquercitrin inhibits the progression of liver cancer in vivo and in vitro via the MAPK signalling pathway. Oncol Rep 2014;31(5):2377-84. doi:10.3892/or.2014.3099 — PubMed 에 '철회된 논문(Retracted Publication)'으로 표시",PM.format(24676882),"Oncology Reports (PubMed)",A),
 (27,"In vitro examination and isolation of antidiarrheal compounds using five bacterial strains from invasive species Bidens bipinnata L. Saudi J Biol Sci 2022;29(1):472-479. doi:10.1016/j.sjbs.2021.09.006 (초록 확인)",PM.format(35002443),"Saudi Journal of Biological Sciences (PubMed)",A),
 (28,"Evaluation of some medicinal plant extracts for antidiarrhoeal activity. Phytother Res 2005;19(6):481-5. doi:10.1002/ptr.1639",PM.format(16114083),"Phytotherapy Research (PubMed)",A),
 (29,"[Protective effect of ethyl acetate extract from Bidens bipinnata on hepatocyte damage induced by endoplasmic reticulum stress]. Zhongguo Zhong Yao Za Zhi 2021. doi:10.19540/j.cnki.cjcmm.20210319.402",PM.format(34472265),"China Journal of Chinese Materia Medica (PubMed)",A),
 (30,"Anti-Inflammatory and Barrier-Related Effects of Bidens bipinnata L. Fruit Ethanol Extract in an MC903-Induced AD-like Dermatitis Mouse Model and LPS-Stimulated RAW 264.7 Cells. Int J Mol Sci 2026;27(13):5717. doi:10.3390/ijms27135717",PM.format(42449989),"International Journal of Molecular Sciences (PubMed)",A),
 (31,"Variation in rhizosphere microbiota correlates with edaphic factor in an abandoned antimony tailing dump. Environ Pollut 2019. doi:10.1016/j.envpol.2019.06.097",PM.format(31306821),"Environmental Pollution (PubMed)",A),
 (32,"[Study on the property of adsorption and separation of the macroporous resins for total flavonoids of Bidens bipinnata L]. Zhong Yao Cai 2007;30(3):338-41.",PM.format(17634046),"Journal of Chinese Medicinal Materials (PubMed)",A),
 (33,"Bioherbicidal potential of plant species with allelopathic effects on the weed Bidens bipinnata L. Sci Rep 2022. doi:10.1038/s41598-022-16203-5",PM.format(35931689),"Scientific Reports (PubMed)",A),
 (34,"Total flavonoids of Bidens bipinnata L. ameliorate experimental adjuvant-induced arthritis through induction of synovial apoptosis. BMC Complement Altern Med 2015;15(1):437. doi:10.1186/s12906-015-0962-3",PM.format(26669668),"BMC Complementary and Alternative Medicine (PubMed)",A),
 (36,"[Effect of composite recipe Zhen-Tong (mixture of Bidens bipinnata L. and Clerodendron trichotomum Thunb.) on experimental arthritis in rats]. Yao Xue Xue Bao 1964;11(10):708-12. (초록 없음, 제목만 확인)",PM.format(5900199),"Acta Pharmaceutica Sinica (PubMed)",A),
 (35,"[Inhibition of 5 compounds from Bidens bipinnata on leukemia cells in vitro]. Zhong Yao Cai 1997;20(5):247-9.",PM.format(12572466),"Journal of Chinese Medicinal Materials (PubMed)",A),
]
src.sort(key=lambda x:x[0])
sources=[{"n":n,"title":t,"url":u,"publisher":p,"accessed":a} for n,t,u,p,a in src]

S={}
S["overview"]=("도깨비바늘(Bidens bipinnata L.)은 국화과 도깨비바늘속의 한해살이풀로, 식약처 「식품원료 목록」에는 '도깨비바늘잎'이라는 이름으로 올라 있다[1]. "
"목록상 지위는 '사용가능'이고 사용 조건은 '사용가능부위 : 잎'이어서, 식품원료로 쓸 수 있는 부위는 잎뿐이다[1]. "
"같은 목록은 이명으로 '좀도깨비바늘', 영문명으로 Spanish needle, 학명 이명으로 Bidens decompositus Wall.을 적고 있다[1]. "
"중국에서는 지상부나 전초를 민간약으로 써 왔고, 연구도 대부분 전초·지상부 추출물이나 총플라보노이드를 대상으로 한다[3, 11, 18]. "
"잎만 따로 분석한 연구는 드물며, 줄기·잎·열매를 비교한 대사체 연구에서 루테올린·켐페롤-3-O-루티노사이드·퀘르세틴 같은 플라보노이드가 잎에 더 많다고 보고되었다[3]. "
"따라서 이 백과의 효능 관련 내용은 대부분 잎 식품이 아닌 전초 추출물의 세포·동물 실험 결과이며, 사람을 대상으로 한 임상시험은 확인하지 못함[3].")
S["history"]=("도깨비바늘은 중국 전통의학에서 열을 내리고 해독하며 설사를 멎게 하고 어혈을 푸는 약초로 기록되어 있다고 소개된다[3]. "
"중국에서는 고지혈증·고혈압·당뇨·말라리아·염증·간섬유화 등에 쓰는 민간약으로 알려져 있다[11]. "
"1960년대 중국 학술지에는 도깨비바늘과 누리장나무(Clerodendrum trichotomum)를 섞은 복합 처방이 흰쥐 실험 관절염에 미치는 영향을 다룬 논문이 실렸다[36]. "
"이집트에서는 지상부 추출물을 다른 약용식물과 함께 설사 억제 효과로 시험한 기록이 있다[28]. "
"브라질에서는 전역에 분포하며 'picão-preto', 'beijo-de-moça', 'carrapicho-de-agulha' 같은 이름으로 불린다고 정리되어 있다[11]. "
"다만 'picão-preto'는 식약처 목록에서 울산도깨비바늘(B. pilosa)의 영문명으로도 쓰이므로 이름만으로 종을 판단하면 안 된다[2, 11]. "
"국내에서 잎을 나물 등 식품으로 먹어 온 구체적 기록은 확인하지 못함[1].")
S["biology"]=("도깨비바늘은 국화과(Asteraceae) 도깨비바늘속에 속하는 한해살이 초본으로, 열대와 온대 지역에 널리 퍼져 있다[3, 8]. "
"한국에서도 광주와 남한 대부분 지역에서 흔히 자라며, 2011–2012년 7–10월 잎·줄기에 흰가루병(Podosphaera xanthii)이 퍼진 것이 처음 보고되었다[8]. "
"아메리카 원산으로 범열대 지역에 들어간 뒤, 가까운 울산도깨비바늘(B. pilosa)은 해로운 침입 잡초로, 도깨비바늘은 귀화한 식물 자원으로 평가된다는 연구가 있다[10]. "
"중국에서 수집한 개체의 핵형은 2n = 3X = 36으로 보고되었다[7]. "
"줄기·잎·열매의 대사체를 비교하면 1,028개 대사물질이 추정 동정되었고 부위마다 조성이 뚜렷이 달랐으며, 잎에는 플라보노이드 종류와 양이 더 많았다[3]. "
"광합성을 맡는 잎이 강한 빛과 자외선에 노출되어 플라보노이드가 쌓인다는 해석이 제시되었으나, 이 연구는 표준품 없이 질량분석으로 추정 동정한 것이다[3].")
S["related_species"]=("식약처 「식품원료 목록」에는 도깨비바늘속 원료가 여럿 있으며, 가막사리(B. tripartita)·구와가막사리(B. radiata var. pinnatifida)·털도깨비바늘(B. biternata)·미국가막사리(B. frondosa)는 잎, 까치발(B. parviflora)은 순이 사용가능 부위다[2]. "
"울산도깨비바늘(B. pilosa)잎은 '제한적사용'으로 분류되어 도깨비바늘잎('사용가능')과 지위가 다르다[1, 2]. "
"중국의 생약 '귀침초(Bidentis Herba)'는 도깨비바늘과 털도깨비바늘 두 종을 기원식물로 하며, HPLC 지문으로 두 종을 구별할 수 있다는 연구가 있다[4]. "
"그 연구에서 도깨비바늘은 20개, 털도깨비바늘은 17개의 특징 피크를 보였고 루틴·이소클로로겐산 A·B가 두 종을 가르는 지표로 제시되었다[4]. "
"도깨비바늘·울산도깨비바늘 등 3종의 엽록체 유전체는 151,599–154,478 bp로 비슷했고, ITS 바코드로는 종 구별이 어려워 유전자 사이 구간이 새 표지 후보로 제시되었다[6]. "
"한 관절염 동물실험 논문은 제목은 도깨비바늘이지만 초록 본문에 'Bidens pilosa'로 적혀 있어 종 표기 혼선이 있다[34].")
S["cultivation"]=("도깨비바늘은 재배하기 쉬운 풀로 소개되지만, 국내에서 작물로 재배한 생산 통계는 확인하지 못함[11]. "
"통계청 농작물생산조사나 농림축산식품부 특용작물 생산실적의 로컬 표에서도 도깨비바늘 항목은 확인하지 못함. "
"중국 분포 모형 연구에서는 현재 적합 서식지가 약 196만 km²로 중부·동부·서남부에 몰려 있고, 7월 강수량과 2월 평균기온이 분포를 좌우하는 주요 요인이었다[5]. "
"같은 연구는 남획과 기후변화로 자원이 위협받는다고 보고, 미래 기후에서는 적합지가 넓어지며 고위도로 옮겨 갈 것으로 예측했다[5]. "
"브라질에서는 밭의 잡초로 다루어져 피마자 등 식물 추출물의 타감작용으로 발아와 생육을 억제하는 연구 대상이 되기도 했다[33]. "
"국내 야생식물 55종을 비교한 연구에서는 다환방향족탄화수소(PAH) 오염 토양에서 줄기 길이 기준 반응이 가장 둔한 축에 속했다[9]. "
"중국에서는 안티모니 광미 더미에 자생한 개체의 뿌리 주변 미생물이 연구되었으므로, 야생 채취 시 오염 토양을 피하는 것이 바람직하다[31].")
S["processing"]=("식품원료로는 잎만 쓸 수 있으므로, 전초나 열매를 원료로 한 가공은 국내 식품원료 기준과 맞지 않는다[1]. "
"연구용 가공은 주로 전초 추출물에서 플라보노이드를 농축하는 방식으로, 7종의 흡착수지 가운데 HPD 100 수지가 총플라보노이드 분리에 가장 좋았다는 보고가 있다[32]. "
"AB-8 수지로 정제 조건을 최적화(pH 5.1, 76.0% 에탄올)하자 추출물의 총플라보노이드 함량이 56.48%가 되었고, 플라보노이드 12종 등 14개 성분이 확인되었다[16]. "
"잎 대사체 분석에서는 50 °C에서 48시간 말린 뒤 분말 0.5 g을 80% 메탄올 10 mL로 40분 초음파 추출했다[3]. "
"식약처 「식품 등의 생산실적」 건강기능식품 품목표에서 도깨비바늘 원료 품목은 확인하지 못함. "
"잎을 식품으로 조리하거나 데쳤을 때 성분 변화에 관한 자료도 확인하지 못함. 한편 열매 에탄올 추출물을 생쥐 피부에 바른 아토피 유사 피부염 실험이 있으나, 열매는 식품원료 사용가능 부위가 아니다[1, 30].")
S["genetics"]=("중국에서 채집한 도깨비바늘의 핵형은 2n = 3X = 36(27m + 3sm + 6sm(SAT))으로 보고되었다[7]. "
"상대 길이로 본 염색체 구성은 2n = 36 = 6L + 9M2 + 18M1 + 3S였다[7]. "
"도깨비바늘·울산도깨비바늘·B. alba var. radiata 3종의 엽록체 유전체는 전형적인 4분 구조이고 길이는 151,599–154,478 bp였다[6]. "
"이 3종에서 clpP·psbD 유전자 소실과 역위반복(IR) 구간의 확장·수축이 관찰되었고, ndhE·ndhF·ndhG·rpl32는 양성 선택을 받은 것으로 추정되었다[6]. "
"계통 분석에서 중국산 3종은 한데 묶여 다른 도깨비바늘속 종들과 단계통군을 이루었다[6]. "
"ndhD-ccsA 등 유전자 사이 구간이 종 식별용 분자 표지 후보로 제시되었으나 실험 검증은 남아 있다[6]. "
"도깨비바늘 단독의 핵 유전체 해독 결과는 확인하지 못함[6].")
S["safety"]=("식약처 「식품원료 목록」에서 도깨비바늘잎은 '사용가능' 원료이며, 잎 외의 부위는 사용가능 부위로 적혀 있지 않다[1]. "
"이 종에 대한 공공기관의 알레르기·잔류·독성 성분 정보는 확인하지 못함[1]. "
"사람을 대상으로 한 섭취 안전성이나 임상시험 자료도 확인하지 못함. "
"보고된 효과는 대부분 전초 추출물·총플라보노이드의 세포·동물 실험 결과로, 생쥐 사염화탄소 간 손상(50–200 mg/kg)과 흰쥐 간섬유화(80·160 mg/kg) 모델 등에서 간 지표가 개선되었다[18, 19]. "
"고지혈증 흰쥐의 혈청·소변 대사체 변화, 소포체 스트레스를 받은 간세포 보호, 췌장 베타세포 보호, 혈관내피세포 염증 억제 등도 모두 동물·세포 단계 결과여서 사람에게 같은 효과가 있다고 볼 수 없다[20, 21, 22, 23, 29]. "
"추출물이 암세포 증식을 억제했다는 세포·생쥐 실험이 있으나, 같은 식물 유래 이소퀘르시트린의 간암 논문은 PubMed 에서 철회 논문으로 표시되어 근거로 쓰기 어렵다[24, 25, 26]. 전초 분리 성분 5종이 백혈병 세포주를 억제했다는 보고(IC50 ≤ 60 μg/ml)도 시험관 결과다[35]. "
"오염된 광산 토양에도 자라는 식물이므로 야생에서 채취할 때는 채취 장소의 토양 오염을 고려해야 한다[31].")
secs=[("overview","개요"),("history","이용의 역사"),("biology","식물학적 특징"),("related_species","근연종과 구별"),("cultivation","재배·채취와 분포"),("processing","가공과 추출"),("genetics","유전 정보"),("safety","안전성")]
sections=[{"key":k,"title":t,"body":S[k]} for k,t in secs]

def c(name,ko,cls,role,part,ct,act,s): return {"name":name,"name_ko":ko,"class":cls,"role":role,"part":part,"content_text":ct,"activity_ko":act,"source":s}
compounds=[
 c("Luteolin","루테올린","플라본","marker","잎(줄기·열매와 비교)","정량값 없음; 잎에서 줄기·열매보다 유의하게 많음(UPLC-Q-TOF-MS 비표적 분석, MSI 2단계 추정 동정)[3]","잎에 많은 플라보노이드로 보고[3]; 고지혈증 연구에서 혈청 약물화학으로 고른 지표 7종 중 하나(흰쥐 조직 분포)[17]",[3,17]),
 c("Kaempferol 3-O-rutinoside","켐페롤-3-O-루티노사이드","플라보놀 배당체","marker","잎","정량값 없음; 잎에서 유의하게 많음(추정 동정)[3]","잎 특이적으로 쌓이는 플라보노이드 배당체로 보고[3]",[3]),
 c("Quercetin","퀘르세틴","플라보놀","bioactive","잎·전초","정량값 없음; 잎에서 많음(추정 동정)[3]; 전초에서 분리[15]","전초 분리 성분이 간성상세포(HSC-T6) 증식과 대식세포 염증성 사이토카인을 억제(세포 실험)[15]; 고지혈증 지표 7종 중 하나[17]",[3,15,17]),
 c("Hyperoside","하이페로사이드","플라보놀 배당체","marker","전초(귀침초)","HPLC 정량 대상 6성분 중 하나; 개별 함량은 초록에 없음, 6성분 함량 RSD 36–123%[4]","귀침초 품질 평가 정량 성분[4]; 고지혈증 지표 7종 중 하나(흰쥐)[17]",[4,17]),
 c("Rutin","루틴","플라보놀 배당체","marker","전초(귀침초)","HPLC 정량 대상; 개별 함량은 초록에 없음[4]","도깨비바늘과 털도깨비바늘을 구별하는 특징 지표(OPLS-DA VIP)[4]; 고지혈증 지표 7종 중 하나[17]",[4,17]),
 c("Chlorogenic acid","클로로겐산","카페오일퀸산(페놀산)","marker","전초(귀침초)","HPLC 정량 대상; 개별 함량은 초록에 없음[4]","귀침초 품질 평가 정량 성분[4]",[4]),
 c("Neochlorogenic acid","네오클로로겐산","카페오일퀸산(페놀산)","marker","전초(귀침초)","HPLC 정량 대상; 개별 함량은 초록에 없음[4]","귀침초 품질 평가 정량 성분[4]",[4]),
 c("Isochlorogenic acid A","이소클로로겐산 A","다이카페오일퀸산","marker","전초(귀침초)","HPLC 정량 대상; 개별 함량은 초록에 없음[4]","기원식물 2종을 구별하는 특징 지표[4]",[4]),
 c("Isochlorogenic acid B","이소클로로겐산 B","다이카페오일퀸산","marker","전초(귀침초)","HPLC 정량 대상; 개별 함량은 초록에 없음[4]","기원식물 2종을 구별하는 특징 지표[4]",[4]),
 c("Isookanin","이소오카닌","플라바논","bioactive","전초","분리 성분(함량 미보고)[14]","α-아밀레이스 억제 IC50 = 0.447 mg/ml(시험관)[14]",[14]),
 c("Bidenoside C","비데노사이드 C(8Z-데카엔-4,6-다이인-1-O-β-D-글루코피라노사이드)","폴리아세틸렌 배당체","bioactive","지상부","분리 성분(함량 미보고)[12]","이 종 지상부에서 새로 분리된 아세틸렌 배당체[12]",[12]),
 c("Bidenoside D","비데노사이드 D(8E-데카엔-4,6-다이인-3,10-다이하이드록시-1-O-β-D-글루코피라노사이드)","폴리아세틸렌 배당체","bioactive","지상부","분리 성분(함량 미보고)[12]","이 종 지상부에서 새로 분리된 아세틸렌 배당체[12]",[12]),
 c("Bidenoside F","비데노사이드 F","플라바논 배당체","bioactive","지상부","분리 성분(함량 미보고)[13]","이 종 지상부에서 새로 분리된 플라바논 배당체; 같은 연구에서 칼콘 배당체 비데노사이드 G도 분리[13]",[13]),
 c("Isoquercitrin","이소퀘르시트린","플라보놀 배당체","bioactive","전초 추출물","함량 미보고[26]","간암세포 억제 보고가 있으나 해당 논문은 PubMed 에서 철회 논문으로 표시됨[26]",[26]),
 c("16-Dehydropregnenolone","16-프레그네놀론(원문 표기 '16-Pregnenolone')","스테로이드","bioactive","잎(헥산 추출물)","분리 성분(함량 미보고)[27]","잎 헥산 추출물에서 분리; 세균 대상 MIC 72 μg/mL(시험관)[27]",[27]),
]
assays=[
 {"role":"literature","compound":"Luteolin","compound_ko":"루테올린(잎에 많은 플라보노이드; 켐페롤-3-O-루티노사이드·퀘르세틴과 함께)","part":"잎(줄기·열매와 비교)",
  "content":"절대 함량 없음; 비표적 대사체 분석으로 잎에서 유의하게 많음(VIP > 1, P < 0.05, FDR < 0.05, |log2FC| ≥ 1), MSI 2단계 추정 동정[3]",
  "method":"UPLC-Q-TOF-MS(비표적 대사체)",
  "conditions":{"instrument":"Waters Q-TOF MS, MassLynx 4.1","column":"Waters BEH C18, 100 × 2.1 mm, 1.8 µm","mobile_phase":"A: 아세토나이트릴, B: 0.1% 폼산 수용액","gradient":"0–2분 6% A; 2–15분 6%→100% A; 15–15.1분 100%→6% A; 15.1–17분 6% A","flow":"0.3 mL/min","temp":"40 °C","detection":"ESI 양이온 모드, m/z 100–1000, 모세관 전압 2.5 kV, 충돌에너지 15 eV, 건조가스 350 °C·50 L/h","injection":"5 µL","sample_prep":"50 °C 48시간 건조 분말 0.5 g + 80% 메탄올 10 mL, 실온 초음파 40분, 12,000 rpm 10분(4 °C) 원심분리, 0.22 µm 여과","standard":"표준품 미사용(UNIFI·MassBank·HMDB·METLIN 대조, 일치 점수 ≥ 70)","linearity":"","lod":"","loq":"","recovery":""},
  "rationale":"잎만 따로 분석한 유일한 확인 자료로, 잎에 플라보노이드가 몰려 있음을 보여 주어 잎 원료의 지표 후보가 된다; 다만 정량 검증(표준품·검량선)은 하지 않았다[3]",
  "source":[3],"url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC13670983/","source_kind":"paper"},
 {"role":"literature","compound":"Rutin","compound_ko":"루틴(하이페로사이드·클로로겐산·네오클로로겐산·이소클로로겐산 A·B 동시 정량)","part":"전초(생약 귀침초, 18배치)",
  "content":"개별 함량 수치는 초록에 없음; 6성분 함량 RSD 36–123%[4]",
  "method":"HPLC-UV",
  "conditions":{"instrument":"","column":"Agilent Poroshell 120 EC-C18, 4.6 mm × 250 mm, 4 μm","mobile_phase":"0.1% 인산 수용액–아세토나이트릴","gradient":"기울기 용리(세부 프로그램은 초록에 없음)","flow":"0.7 mL/min","temp":"25 °C","detection":"270 nm","injection":"5 μL","sample_prep":"","standard":"네오클로로겐산·클로로겐산·이소클로로겐산 A·B·루틴·하이페로사이드 표준품과 비교","linearity":"","lod":"","loq":"","recovery":""},
  "rationale":"루틴·이소클로로겐산 A·B가 도깨비바늘과 털도깨비바늘을 가르는 특징 지표로 제시되었다; 잎이 아닌 전초 자료이며 전문 확인 못함(조건은 초록에 적힌 것만)[4]",
  "source":[4],"url":"https://pubmed.ncbi.nlm.nih.gov/41084445/","source_kind":"paper"},
]
d={"slug":"bidens-bipinnata","name_ko":"도깨비바늘","name_en":"Spanish needle","scientific_name":"Bidens bipinnata L.",
 "aliases":["도깨비바늘잎","좀도깨비바늘","Spanish needle","Spanish needles","Bidens decompositus Wall.","귀침초(Bidentis Herba, 기원식물 중 하나)"],
 "sections":sections,"compounds":compounds,"markers":[],"assays":assays,"nutrients":[],"production":[],"world":[],"gi":[],"orgs":[],"sources":sources}
(P/"dossier.json").write_text(json.dumps(d,ensure_ascii=False,indent=1),encoding="utf-8")
for s in sections: print(s["key"],len(s["body"]))
