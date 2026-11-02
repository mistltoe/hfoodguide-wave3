import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
A = "2026-11-02"
def pm(n, title, doi, journal, pmid, note, pmc=None):
    pub = f"{journal} (PubMed {pmid}" + (f", {pmc})" if pmc else ")")
    url = f"https://doi.org/{doi}" if doi else f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
    return {"n": n, "title": f"{title} ({note})", "url": url, "publisher": pub, "accessed": A}

sources = [
 {"n": 1, "title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — '인도보리새우' 행(학명 Fenneropenaeus indicus, 이명 '인도흰새우', 영문명 칸 비어 있음, 수산물, 사용가능, 사용가능부위 '-', 사용조건 없음). 대하·대하새우분말(Penaeus chinensis), 바나나새우(P. merguiensis), 보리새우 계열(P. japonicus), 흰다리새우 계열(Litopenaeus vannamei / Penaeus vannamei), 얼룩새우(P. monodon), 홍다리얼룩새우(P. semisulcatus) 행 대조 (로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json, card.json)", "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
 {"n": 2, "title": "식약처 고시 제2026-43호 「건강기능식품의 기준 및 규격」 제3. 2-30 글루코사민·2-31 N-아세틸글루코사민·2-49 키토산/키토올리고당(원재료 '갑각류(게, 새우 등)의 껍질', 섭취 시 주의사항 '게 또는 새우에 알레르기가 있는 사람은 섭취에 주의') (로컬 원문 docs/refs/MFDS/건강기능식품의기준및규격_2026-43_제1~제3.txt)", "url": "https://www.mfds.go.kr/brd/m_211/view.do?seq=14973", "publisher": "식품의약품안전처", "accessed": A},
 pm(3, "Phylogenetic relations and mitogenome-wide similarity metrics reveal monophyly of Penaeus sensu lato. Ecol Evol 2021;11(5):2040-2049", "10.1002/ece3.7148", "Ecology and Evolution", "33717440", "전문 확인", "PMC7920775"),
 pm(4, "Cellular and molecular immune response and production performance of Indian white shrimp Penaeus indicus (H. Milne-Edwards, 1837), reared in a biofloc-based system with different protein levels of feed. Fish Shellfish Immunol 2021;119:31-41", "10.1016/j.fsi.2021.09.002", "Fish & Shellfish Immunology", "34487828", "초록 확인"),
 pm(5, "Full-length cloning and phylogenetic analyses of translationally controlled tumour protein and ferritin genes from the Indian white prawn, Fenneropenaeus indicus (H. Milne Edwards). J Fish Dis 2014;37(2):77-87", "10.1111/jfd.12040", "Journal of Fish Diseases", "24329985", "초록 확인"),
 pm(6, "16S rRNA gene diversity and gut microbial composition of the Indian white shrimp (Penaeus indicus). Antonie Van Leeuwenhoek 2021;114(12):2019-2031", "10.1007/s10482-021-01658-9", "Antonie van Leeuwenhoek", "34536184", "초록 확인"),
 pm(7, "Transcriptomic variations associated with salinity stress in Penaeus indicus. Mol Biol Rep 2023;50(11):9295-9306", "10.1007/s11033-023-08824-4", "Molecular Biology Reports", "37812353", "초록 확인"),
 pm(8, "New genotypes of white spot syndrome virus (WSSV) and Taura syndrome virus (TSV) from the Kingdom of Saudi Arabia. Dis Aquat Organ 2012;99(3):179-85", "10.3354/dao02470", "Diseases of Aquatic Organisms", "22832716", "초록 확인"),
 pm(9, "Molecular, histopathologic and electron microscopic analysis of white spot syndrome virus in wild shrimp (Fenneropenaeus indicus) in the coastal waters of Iran. Arch Virol 2020;165(6):1433-1440", "10.1007/s00705-020-04625-3", "Archives of Virology", "32318832", "초록 확인"),
 pm(10, "Effect of rearing environment and age on spermatophore quality in Penaeus indicus and validation of short term storage extenders. Anim Reprod Sci 2026;287:108114", "10.1016/j.anireprosci.2026.108114", "Animal Reproduction Science", "41581466", "초록 확인"),
 pm(11, "Isolation and characterization of heat-stable allergens from shrimp (Penaeus indicus). J Allergy Clin Immunol 1989;83(1):26-36", "10.1016/0091-6749(89)90474-0", "The Journal of Allergy and Clinical Immunology", "2913137", "초록 확인"),
 pm(12, "Identification of tropomyosin as the major shrimp allergen and characterization of its IgE-binding epitopes. J Immunol 1993;151(10):5354-63", None, "The Journal of Immunology", "7693809", "초록 확인, DOI 없음"),
 pm(13, "Purification and IgE-binding epitopes of a major allergen in the gastropod Turbo cornutus. Biosci Biotechnol Biochem 1998;62(7):1337-43", "10.1271/bbb.62.1337", "Bioscience, Biotechnology, and Biochemistry", "9720216", "초록 확인 — 이 종의 알레르겐 이름 'Pen i 1'이 나오는 비교 대목만 인용"),
 pm(14, "Mercury contamination of fish and shrimp samples available in markets of Mashhad, Iran. Bull Environ Contam Toxicol 2013;91(3):267-71", "10.1007/s00128-013-1068-6", "Bulletin of Environmental Contamination and Toxicology", "23903758", "초록 확인"),
 pm(15, "Risk assessment of heavy metals in marine fish and seafood from Kedah and Selangor coastal regions of Malaysia: a high-risk health concern for consumers. Environ Sci Pollut Res Int 2021;28(39):55166-55175", "10.1007/s11356-021-14701-z", "Environmental Science and Pollution Research", "34129166", "초록 확인"),
 pm(16, "Systematic review and health risk assessment of arsenic and lead in the fished shrimps from the Persian gulf. Food Chem Toxicol 2018;113:278-286", "10.1016/j.fct.2018.01.046", "Food and Chemical Toxicology", "29407475", "초록 확인"),
 pm(17, "Heavy metals accumulation in crab and shrimps from Pulicat lake, north Chennai coastal region, southeast coast of India. Toxicol Ind Health 2016;32(1):1-6", "10.1177/0748233713475500", "Toxicology and Industrial Health", "23344825", "초록 확인"),
 pm(18, "Bioaccumulation of heavy metals in different trophic levels of aquatic ecosystems with fish as a bioindicator in Visakhapatnam, India. Mar Pollut Bull 2021;165:112162", "10.1016/j.marpolbul.2021.112162", "Marine Pollution Bulletin", "33610109", "초록 확인"),
 pm(19, "Cadmium uptake and accumulation by the decapod crustacean Penaeus indicus. Mar Environ Res 2005;60(3):339-54", "10.1016/j.marenvres.2004.12.001", "Marine Environmental Research", "15769503", "초록 확인"),
 pm(20, "Organochlorine pesticides and heavy metals in the zooplankton, fishes, and shrimps of tropical shallow tidal creeks and the associated human health risk. Mar Pollut Bull 2021;165:112170", "10.1016/j.marpolbul.2021.112170", "Marine Pollution Bulletin", "33621901", "초록 확인"),
 pm(21, "Abundance, characteristics and seasonal variation of microplastics in Indian white shrimps (Fenneropenaeus indicus) from coastal waters off Cochin, Kerala, India. Sci Total Environ 2020;737:139839", "10.1016/j.scitotenv.2020.139839", "Science of the Total Environment", "32526586", "초록 확인"),
 pm(22, "Microplastics in the edible tissues of shellfishes sold for human consumption. Chemosphere 2021;264(Pt 2):128554", "10.1016/j.chemosphere.2020.128554", "Chemosphere", "33049503", "초록 확인"),
 pm(23, "Antifungal application of biosynthesized selenium nanoparticles with pomegranate peels and nanochitosan as edible coatings for citrus green mold protection. J Nanobiotechnology 2022;20(1):182", "10.1186/s12951-022-01393-x", "Journal of Nanobiotechnology", "35392922", "전문 확인", "PMC8991507"),
 pm(24, "Polylactic acid/chitosan films for packaging of Indian white prawn (Fenneropenaeus indicus). Int J Biol Macromol 2018;117:1002-1010", "10.1016/j.ijbiomac.2018.05.214", "International Journal of Biological Macromolecules", "29857109", "초록 확인"),
 pm(25, "A histone H2A derived antimicrobial peptide, Fi-Histin from the Indian White shrimp, Fenneropenaeus indicus: Molecular and functional characterization. Fish Shellfish Immunol 2019;92:667-679", "10.1016/j.fsi.2019.06.044", "Fish & Shellfish Immunology", "31252047", "초록 확인"),
 pm(26, "Functional Characterization of a c-type Lysozyme from Indian Shrimp Fenneropenaeus indicus. Probiotics Antimicrob Proteins 2014;6(2):114-21", "10.1007/s12602-013-9146-y", "Probiotics and Antimicrobial Proteins", "24676722", "초록 확인"),
 pm(27, "Molecular cloning, recombinant expression and functional characterization of an antimicrobial peptide, Crustin from the Indian white shrimp, Fenneropenaeus indicus. Fish Shellfish Immunol 2017;71:83-94", "10.1016/j.fsi.2017.09.071", "Fish & Shellfish Immunology", "28964865", "초록 확인"),
 pm(28, "Molecular Characterization of a Newly Identified Subfamily Member of Penaeidin from two Penaeid Shrimps, Fenneropenaeus indicus and Metapenaeus monoceros. Probiotics Antimicrob Proteins 2016;8(1):46-52", "10.1007/s12602-015-9203-9", "Probiotics and Antimicrobial Proteins", "26607699", "초록 확인"),
 pm(29, "Multidrug-Resistant Vibrio spp. carrying carbapenemase genes in aquacultured shrimp and their zoonotic importance. Sci Rep 2026;16(1)", "10.1038/s41598-026-62098-x", "Scientific Reports", "42486911", "초록 확인", "PMC13392438"),
 pm(30, "Development and characterization of eighty-one microsatellite markers in Indian white shrimp, Fenneropenaeus indicus, through cross-amplification. J Genet 2015;94(3):e43-50", "10.1007/s12041-015-0555-4", "Journal of Genetics", "26419436", "초록 없음, 제목·서지만 확인"),
 pm(31, "ShEnrich: a functional annotation database and enrichment platform for penaeid shrimp. BMC Bioinformatics 2026;27(1)", "10.1186/s12859-026-06567-0", "BMC Bioinformatics", "42963765", "초록 확인", "PMC13721321"),
 pm(32, "Bioaugmentation of biofloc system with enzymatic bacterial strains for high health and production performance of Penaeus indicus. Sci Rep 2021;11(1):13633", "10.1038/s41598-021-93065-3", "Scientific Reports", "34211034", "초록 확인", "PMC8249640"),
 pm(33, "Scale-up of non-toxic poly(butylene adipate-co-terephthalate)-Chitin based nanocomposite articles by injection moulding and 3D printing. Int J Biol Macromol 2020;165(Pt B):3145-3155", "10.1016/j.ijbiomac.2020.10.181", "International Journal of Biological Macromolecules", "33122061", "초록 확인"),
 pm(34, "Utilization of marine fisheries wastes for the production of the freshwater fish Cyprinus carpio. Trop Anim Health Prod 2019;51(8):2305-2313", "10.1007/s11250-019-01938-7", "Tropical Animal Health and Production", "31165432", "초록 확인"),
 pm(35, "Bioaccumulation variability and human health risk assessment of organochlorine pesticides in edible fish and shellfish from the Northeast Bay of Bengal. Mar Pollut Bull 2025;215:117856", "10.1016/j.marpolbul.2025.117856", "Marine Pollution Bulletin", "40120358", "초록 확인"),
]

S = []
def sec(k, t, b): S.append({"key": k, "title": t, "body": b})

sec("overview", "한눈에 보기",
"인도보리새우(Fenneropenaeus indicus, 영문 Indian white shrimp 또는 Indian white prawn)는 보리새우과(Penaeidae)에 드는 바다 새우로, 최근 논문에서는 구학명 계열의 Penaeus indicus로 더 자주 적힌다[3, 4, 7]. 인도-서태평양에 분포하며, 인도에서는 토착종으로서 기수(汽水) 양식의 중요한 대상이다[6, 7]. 사우디아라비아·이란·이집트에서도 양식되거나 양식용 어미새우를 바다에서 잡는다[8, 9, 29].\n\n"
"식약처 「식품원료 목록」에는 학명 Fenneropenaeus indicus로 '인도보리새우' 한 줄이 올라 있고, 이명은 '인도흰새우', 분류는 수산물, 상태는 '사용가능'이다[1]. 사용 부위는 '-'(따로 정하지 않음)이고 별도의 사용 조건 문구는 없으며, 영문명 칸은 비어 있다[1]. 이 종 자체는 건강기능식품 고시형 원료의 원재료로 이름이 오르지 않았으나, 글루코사민·N-아세틸글루코사민·키토산 고시의 원재료는 '갑각류(게, 새우 등)의 껍질'로 넓게 정해져 있다[2].\n\n"
"국내 어획·수입 통계와 국가표준식품성분표의 이 종 성분값은 이 조사에서 확인하지 못함.")

sec("history", "이용 역사",
"이 종은 1837년 H. Milne Edwards가 기재했으며, 논문에서는 저자 표기를 'H. Milne-Edwards, 1837'로 적는다[4, 5]. 식품 안전 분야에서 이 종은 새우 알레르기 연구의 출발점 가운데 하나다[11, 12]. 1989년 인도 연구진은 삶은 이 종 추출물에서 열에 강한 알레르겐 Sa-I과 Sa-II를 분리했고, 1993년에는 주 알레르겐 Sa-II가 근육 단백질 트로포미오신임을 밝혔다[11, 12].\n\n"
"양식 이용도 여러 나라에서 이어졌다[8, 9, 29]. 사우디아라비아에서는 2010–2011년 양식 중인 이 종에서 흰반점병 바이러스(WSSV)와 타우라 증후군 바이러스(TSV)로 큰 폐사가 일어났고, 연구진은 홍해에서 잡아 어미로 쓰는 야생 개체가 감염원일 수 있다고 보았다[8]. 이란에서는 시스탄발루체스탄·호르모즈간 두 주의 연안에서 잡은 야생 어미새우를 부화장에 공급한다[9]. 인도 중앙기수양식연구소(ICAR-CIBA) 계열 연구진은 바이오플록 양식, 연못 사육 수컷의 정포(精包) 품질 등 이 종의 양식화 연구를 이어 왔다[4, 10]. 이집트 다미에타 지역의 양식장에서도 이 종이 길러진다[29].")

sec("biology", "어종·형태·생태",
"인도보리새우는 십각목 보리새우과의 바다 새우로, 분포 범위는 인도-서태평양으로 소개된다[6]. 새우류는 염분 변화에 견디는 광염성 동물로 삼투 조절로 몸 안의 이온 농도를 맞추며, 이 종도 낮은 염분에서 성장과 면역이 영향을 받는다[7]. 3주간의 저염분 시험에서 지질·아미노산 대사, 해당 과정, 신호 전달 경로 유전자가 크게 움직였다[7].\n\n"
"장내 세균은 야생과 양식 개체가 달랐다[6]. 야생 개체에서는 Photobacterium(29.5%)이, 양식 개체에서는 Vibrio(46.5%)가 가장 많았다[6].\n\n"
"번식 생리도 연구되었다[10]. 야외 연못에서 기른 수컷은 체중 12.23 ± 0.13 g(사육 90일)에서 교접기가 붙고 정포가 보여 형태상 성숙했으며, 180일째 정자 수는 21.47 ± 1.97 × 10⁶개로 야생 수컷(43.05 ± 8.05 × 10⁶개)보다 적었다[10]. 실내 수조에서 기른 수컷은 사육 밀도와 관계없이 성장과 정포 품질이 나빴다[10].\n\n"
"어린 새우를 쓴 실험에서 물속 카드뮴은 배출되지 않고 몸에 더해지며 간췌장·외골격·아가미에 많이 분포했고, 연구진은 빠른 성장으로 인한 희석 때문에 야외 성체의 카드뮴 농도는 대체로 낮다고 보았다[19].")

sec("related_species", "관련 종·이름",
"이 종의 속명은 학계에서 논쟁 중이다[3]. 넓은 의미의 Penaeus 속을 형태(암컷 생식기 모양, 이마뿔 옆 홈 등)만으로 여섯 속(Fenneropenaeus·Litopenaeus·Marsupenaeus 등)으로 나눈 분류가 20년 넘게 논란이었고, 2021년 미토콘드리아 전체 유전체 계통 분석은 이들이 하나의 계통(단계통)임을 보이며 옛 Penaeus 속으로 되돌릴 것을 제안했다[3]. 그래서 같은 종이 Fenneropenaeus indicus와 Penaeus indicus 두 이름으로 함께 쓰이며, 이 자료는 식약처 목록의 학명(Fenneropenaeus indicus)을 표제로 두고 Penaeus indicus를 같은 종의 이름으로 다룬다[1, 3, 4].\n\n"
"같은 분석에서 이 종은 대하(F. chinensis)·바나나새우(F. merguiensis)·F. penicillatus와 함께 아시아의 '흰새우' 무리로 묶였다[3]. 라이소자임 유전자는 바나나새우·대하와 98% 같았고, TCTP·페리틴 유전자도 대하와 가장 가까웠다[5, 26]. 식약처 목록에서 대하(Penaeus chinensis)·바나나새우(Penaeus merguiensis)는 따로 행이 있으므로, 이 자료는 그 종들의 성분·안전성 값을 섞지 않는다[1].\n\n"
"국문명에 '보리새우'가 들어가지만 식약처 목록의 '보리새우'는 Penaeus japonicus로 다른 종이다[1]. 이명 '인도흰새우'는 흰다리새우(Litopenaeus vannamei / Penaeus vannamei)와 이름이 비슷하나 역시 다른 종이다[1].")

sec("cultivation", "어획·양식",
"인도에서 이 종은 토착 기수 양식 품종으로 연구된다[7]. 바이오플록 수조(7,500 L)에서 120일간 사료 단백질 25·30·35%를 비교한 시험에서 성장과 사료 효율은 30% 사료가 가장 좋았고, 면역 지표와 면역 유전자 발현은 35% 사료에서 가장 높았다[4]. 바이오플록에 효소 생산 세균(Marinilactibacillus piezotolerans, Novosphingobium sp.)을 더하면 성장·생존율이 오르고 암모니아가 줄었다[32].\n\n"
"질병은 양식의 큰 걸림돌이다[8, 9, 29]. 사우디아라비아 양식장의 WSSV·TSV는 새로운 유전형으로 확인되었다[8]. 이란에서 야생 어미새우 833마리를 PCR로 조사한 결과 WSSV는 시스탄발루체스탄 주의 채집지에서만 나왔고, 감염률은 봄 8.7%, 가을 2.03%였다[9]. 이집트 다미에타의 양식 새우 100마리와 양식장 물에서 비브리오 165주(63.5%)가 분리되었고 그중 77.5%가 다제내성이었으며 카바페넴 분해효소 유전자도 검출되었다[29].\n\n"
"어미 관리 연구에서는 실내 수조보다 야외 연못 사육이 수컷 번식 품질에 유리했고, 정포를 단기 보관할 때는 광유(미네랄 오일)가 처음 5–10일간 정자 생존을 가장 잘 지켰다[10]. 세계·국가별 어획·양식 생산량은 이 조사에서 확인하지 못함.")

sec("processing", "가공·이용",
"이 종은 살을 냉장 유통하는 식품으로 다뤄진다[24]. 폴리락트산에 나노키토산(0.5·1·2%)을 넣은 필름으로 새우살을 포장해 18일간 냉장한 시험에서 미생물·생화학 품질 지표가 유지되어 저장 기간 연장 가능성이 제시되었다[24].\n\n"
"껍데기는 키틴·키토산 원료로 쓰인다[23, 33]. 이 종 껍데기를 탈단백(2.0 N NaOH)·탈회(2.0 N HCl)·탈아세틸화(55% NaOH, 123 °C, 95분)해 얻은 키토산은 탈아세틸화도 88.13%, 분자량 46.72 kDa였고, 이를 평균 82.72 nm 나노입자로 만들어 오렌지 푸른곰팡이병 코팅에 썼다[23]. 껍데기 키틴으로 만든 나노키틴은 생분해성 플라스틱(PBAT) 복합재의 충전재로 시험되었다[33]. 가공 부산물 분말은 잉어 사료에서 어분을 대체하는 원료로도 시험되었다[34].\n\n"
"국내 건강기능식품 고시에서 글루코사민·N-아세틸글루코사민·키토산의 원재료는 '갑각류(게, 새우 등)의 껍질'로 정해져 있을 뿐 새우 종을 지정하지 않는다[2]. 이 종을 원료로 쓴 국내 가공식품·건강기능식품 생산 실적은 확인하지 못함.")

sec("genetics", "유전 정보",
"이 종의 미토콘드리아 전체 유전체는 2021년 처음 보고되었고(GenBank KX462904), 유전자 배열은 넓은 의미의 Penaeus 속 다른 종과 같았으며 조절 영역 길이는 1,001 bp였다[3]. 저염분 스트레스 전사체 연구에서는 Trinity 조립으로 전사체 173,582개(평균 854 bp, N50 1,243 bp, GC 42.33%)를 얻었고, 7·14·21일째 차등 발현 유전자가 각각 2,130·3,090·5,351개였다[7].\n\n"
"근연종 표지를 교차 증폭해 이 종에 쓸 수 있는 미세위성(마이크로새틀라이트) 표지 81개가 개발되었다[30]. 2026년 공개된 보리새우류 기능 주석 데이터베이스는 흰다리새우·얼룩새우·대하·보리새우와 함께 이 종을 다섯 종 가운데 하나로 담았다[31].\n\n"
"선천 면역 유전자도 여럿 밝혀졌다[25, 26, 27, 28]. 히스톤 H2A에서 유래한 27개 아미노산 항균 펩타이드 Fi-Histin, 크루스틴(Fi-crustin2), 페나이딘 새 이소형(Fi-PEN, GenBank JX657680), 159개 아미노산의 c형 라이소자임이 보고되었다[25, 26, 27, 28].")

sec("safety", "안전성",
"삶은 이 종에서 분리한 주 알레르겐 Sa-II는 34 kd·아미노산 301개의 열에 강한 단백질로, 8.2 kd의 Sa-I과 에피토프의 54%를 공유했다[11]. Sa-II는 트로포미오신으로 확인되었고 IgE 결합 부위는 잔기 50–66과 153–161이었으며, 이후 'Pen i 1'로 불린다[12, 13]. 식약처는 새우 껍질 원료 건강기능식품에 '게 또는 새우에 알레르기가 있는 사람은 섭취에 주의' 문구를 정했다[2].\n\n"
"중금속은 지역 차가 크다[14, 15, 17, 18]. 이란 시장 조사에서 이 종의 총수은은 0.37 ± 0.03 µg/g으로 JECFA 권고(0.5 µg/g)보다 낮고 미국 EPA 기준(0.3 µg/g)보다는 높았다[14]. 인도 풀리캇 호수 개체의 근육은 허용 수준 안이었으나, 비사카파트남 연안 어패류(이 종 포함)는 크롬·알루미늄·망가니즈·비소가 기준을 넘었고 말레이시아 연구는 이 종을 늘 먹으면 만성 위해가 크다고 평가했다[15, 17, 18]. 페르시아만 메타분석의 새우 근육 납 순위는 흰다리새우 > Panulirus homarus > 이 종 > Metapenaeus affinis였다[16]. 유기염소 농약은 인도 순다르반에서 발암 위해 수준일 수 있다는 평가와 벵골만에서 일일 섭취량이 기준 아래라는 평가가 함께 있다[20, 35].\n\n"
"인도 코친 연안 개체 연조직에서 미세플라스틱이 마리당 0.39 ± 0.6개 나와, 내장을 빼지 않은 새우가 섭취 경로일 수 있다[21]. 케랄라 항구 새우의 가식부에서는 검출되지 않았다[22].")

compounds = [
 {"name": "Tropomyosin", "name_ko": "트로포미오신(Pen i 1, Sa-II)", "class": "근육 단백질(알레르겐)", "role": "marker", "part": "근육(삶은 새우 추출물)", "content_text": "분자량 34 kd, 아미노산 301개, 등전점 pH 4.8–5.4 [11, 12]", "activity_ko": "새우 알레르기 환자 혈청 IgE와 결합하는 주 알레르겐; 결합 부위 잔기 50–66, 153–161[12]", "source": [11, 12, 13]},
 {"name": "Shrimp allergen Sa-I", "name_ko": "새우 알레르겐 Sa-I", "class": "단백질(알레르겐)", "role": "bioactive", "part": "삶은 새우 추출물", "content_text": "분자량 8.2 kd [11]", "activity_ko": "Sa-II와 에피토프 54% 공유, Sa-II 조각일 가능성[11]", "source": [11]},
 {"name": "Chitosan", "name_ko": "키토산", "class": "아미노다당류", "role": "bioactive", "part": "껍데기", "content_text": "탈아세틸화도 88.13%, 분자량 46.72 kDa, 1.5% 아세트산 용해도 97.4% [23]", "activity_ko": "나노입자(82.72 nm) 코팅이 오렌지 푸른곰팡이병 증상을 91.7% 줄임(과일 시험)[23]", "source": [23]},
 {"name": "Chitin", "name_ko": "키틴", "class": "다당류", "role": "bioactive", "part": "껍데기", "content_text": "껍데기 함량은 확인하지 못함 [33]", "activity_ko": "나노키틴으로 만들어 생분해성 플라스틱 복합재 충전재로 시험[33]", "source": [33]},
 {"name": "Fi-Histin (histone H2A-derived peptide)", "name_ko": "Fi-Histin(히스톤 H2A 유래 펩타이드)", "class": "항균 펩타이드", "role": "bioactive", "part": "혈구(유전자에서 유추한 합성 펩타이드)", "content_text": "아미노산 27개, 순전하 +6 [25]", "activity_ko": "비브리오 등 세균 억제; 사람 암세포주 NCI-H460 IC50 22.670 µM(세포 시험)[25]", "source": [25]},
 {"name": "Crustin", "name_ko": "크루스틴(Fi-crustin2)", "class": "항균 단백질", "role": "bioactive", "part": "혈구", "content_text": "ORF 아미노산 100개, 성숙 펩타이드 10.61 kDa, pI 7.59 [27]", "activity_ko": "재조합 단백질이 그람음성균 생장 억제(시험관)[27]", "source": [27]},
 {"name": "Penaeidin", "name_ko": "페나이딘(Fi-PEN)", "class": "항균 펩타이드", "role": "bioactive", "part": "혈구", "content_text": "아미노산 71개, 예측 분자량 5.66 kDa, pI 9.38 [28]", "activity_ko": "페나이딘-3 소군에 드는 새 이소형(서열 분석)[28]", "source": [28]},
 {"name": "Lysozyme", "name_ko": "라이소자임(c형)", "class": "효소", "role": "bioactive", "part": "유전자(재조합 발현)", "content_text": "cDNA 477 bp, 아미노산 159개 [26]", "activity_ko": "재조합 효소가 Salmonella typhimurium·효모 2종 억제(탁도 시험)[26]", "source": [26]},
 {"name": "Ferritin", "name_ko": "페리틴", "class": "철 저장 단백질", "role": "bioactive", "part": "후기 유생(유전자)", "content_text": "유전자 1,212 bp, ORF 510 bp(아미노산 170개) [5]", "activity_ko": "Vibrio harveyi 감염 후 발현 증가(선천 면역 관련)[5]", "source": [5]},
]

assays = [
 {"role": "literature", "compound": "Chitosan", "compound_ko": "키토산", "part": "껍데기", "content": "탈아세틸화도 88.13%, 분자량 46.72 kDa [23]", "method": "알칼리·산 처리로 추출한 뒤 물성 측정(탈아세틸화도·분자량 측정법은 전문에 적혀 있지 않음); FTIR로 작용기 확인",
  "conditions": {"instrument": "FTIR(JASCO FT-IR-360), KBr 1%(w/w) 혼합, 투과 모드 450–4000 cm⁻¹; 입자 크기·제타전위는 DLS(Zeta plus)", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "", "injection": "", "sample_prep": "껍데기 건조·분쇄 → 2.0 N NaOH 실온 250분 탈단백 → 2.0 N HCl 실온 250분 탈회 → 55% NaOH 123 °C 95분 탈아세틸화", "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "이 종 껍데기에서 직접 만든 키토산의 품질 지표(탈아세틸화도 70% 이상이면 키토산으로 본다는 본문 기준)를 전문으로 확인했다; 함량 정량이 아니라 원료 물성 값이다[23].", "source": [23], "url": "https://doi.org/10.1186/s12951-022-01393-x", "source_kind": "paper"},
 {"role": "literature", "compound": "Mercury (total)", "compound_ko": "총수은", "part": "시장 유통 새우(부위는 초록에 없음)", "content": "0.37 ± 0.03 µg/g [14]", "method": "원자흡광광도법(수소화물 발생 장치 MHS 10)",
  "conditions": {"instrument": "원자흡광광도계 + 수은 수소화물 장치(MHS 10)", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "", "injection": "", "sample_prep": "", "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "이 종의 식용 안전성에서 가장 많이 다뤄지는 유해 원소다; 전문 확인 못함 — 측정 부위·습/건중량 기준·검출한계는 초록에 없다[14].", "source": [14], "url": "https://doi.org/10.1007/s00128-013-1068-6", "source_kind": "paper"},
 {"role": "literature", "compound": "Tropomyosin (Pen i 1)", "compound_ko": "트로포미오신(Pen i 1)", "part": "근육", "content": "정량값 없음 — 분자량 34 kd, 아미노산 301개 [11, 12]", "method": "이온교환(DEAE-Sephacel)·겔여과(Bio-Gel P-200)·Sepharose 4B 크로마토그래피 정제, SDS-PAGE, 고상 방사면역측정 억제 시험",
  "conditions": {"instrument": "", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "", "injection": "", "sample_prep": "삶은 새우 추출물", "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "이 종에서 처음 정제·동정된 새우 주 알레르겐으로 갑각류 알레르기 판별의 기준 단백질이다; 전문 확인 못함 — 함량은 보고되지 않았다[11, 12].", "source": [11, 12], "url": "https://doi.org/10.1016/0091-6749(89)90474-0", "source_kind": "paper"},
]

d = {"slug": "fenneropenaeus-indicus", "name_ko": "인도보리새우", "name_en": "Indian white shrimp",
     "scientific_name": "Fenneropenaeus indicus",
     "aliases": ["인도흰새우", "Indian white shrimp", "Indian white prawn", "Penaeus indicus H. Milne Edwards, 1837"],
     "sections": S, "compounds": compounds, "markers": [], "assays": assays, "nutrients": [],
     "production": [], "world": [], "gi": [], "orgs": [], "sources": sources}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in S: print(s["key"], len(s["body"]))
