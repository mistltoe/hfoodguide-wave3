import json, pathlib
HERE = pathlib.Path(__file__).resolve().parent.parent
PM = "https://pubmed.ncbi.nlm.nih.gov/%s/"
PMC = "https://pmc.ncbi.nlm.nih.gov/articles/%s/"
A = "2026-11-02"
FT = " (PMC 전문 확인(PubMed 도구로 열람))"
AB = " (PubMed 초록 확인(PubMed 도구))"
S = [
 ("식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 숙근초(Allium ascalonicum L.)·대파(Allium fistulosum L.) 행", "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "식품의약품안전처", "2026-10-13"),
 ("Moldovan C et al. (2022) Therapeutic Uses and Pharmacological Properties of Shallot (Allium ascalonicum): A Systematic Review. Front Nutr 9:903686. doi:10.3389/fnut.2022.903686", PMC % "PMC9380064", "Frontiers"+FT, A),
 ("Major N et al. (2022) The Phytochemical and Nutritional Composition of Shallot Species (Allium × cornutum, Allium × proliferum and A. cepa Aggregatum) Is Genetically and Environmentally Dependent. Antioxidants 11(8):1547. doi:10.3390/antiox11081547", PMC % "PMC9405304", "MDPI"+FT, A),
 ("Prabawati S et al. (2026) Physiology, Nutrition, and Postharvest Technology on Shallots (Allium cepa L.): A Review. Scientifica 2026:8328535. doi:10.1155/sci5/8328535", PMC % "PMC13239027", "Wiley/Hindawi"+FT, A),
 ("Major N et al. (2018) Morphological and Biochemical Diversity of Shallot Landraces Preserved Along the Croatian Coast. Front Plant Sci 9:1749. doi:10.3389/fpls.2018.01749", PM % "30559753", "Frontiers"+AB, A),
 ("Perković J et al. (2021) Shallot Species and Subtypes Discrimination Based on Morphology Descriptors. Plants 10(1):60. doi:10.3390/plants10010060", PM % "33383969", "MDPI"+AB, A),
 ("Leino MW et al. (2018) Patterns of Exchange of Multiplying Onion (Allium cepa L. Aggregatum-Group) in Fennoscandian Home Gardens. Econ Bot 72(3):346-356. doi:10.1007/s12231-018-9426-2", PM % "30573921", "Springer"+AB, A),
 ("Matsuse K et al. (2022) Targeted Metabolome Profiling of Indonesian Shallots and Japanese Long-Day/Short-Day Bulb Onions. Metabolites 12(12):1260. doi:10.3390/metabo12121260", PMC % "PMC9783499", "MDPI"+FT, A),
 ("Abdelrahman M et al. (2020) Metabolome-Based Discrimination Analysis of Shallot Landraces and Bulb Onion Cultivars Associated with Differences in the Amino Acid and Flavonoid Profiles. Molecules 25(22):5300. doi:10.3390/molecules25225300", PM % "33202886", "MDPI"+AB, A),
 ("Fattorusso E et al. (2002) Chemical composition of shallot (Allium ascalonicum Hort.). J Agric Food Chem 50(20):5686-5690. doi:10.1021/jf020396t", PM % "12236699", "American Chemical Society"+AB, A),
 ("Teshima Y et al. (2013) Identification and biological activity of antifungal saponins from shallot (Allium cepa L. Aggregatum group). J Agric Food Chem 61(31):7440-7445. doi:10.1021/jf401720q", PM % "24138065", "American Chemical Society"+AB, A),
 ("Tocmo R et al. (2014) Effect of processing conditions on the organosulfides of shallot (Allium cepa L. Aggregatum group). J Agric Food Chem 62(23):5296-5304. doi:10.1021/jf500739n", PM % "24840922", "American Chemical Society"+AB, A),
 ("Wiczkowski W et al. (2008) Quercetin from shallots (Allium cepa L. var. aggregatum) is more bioavailable than its glucosides. J Nutr 138(5):885-888. doi:10.1093/jn/138.5.885", PM % "18424596", "American Society for Nutrition"+AB, A),
 ("Pobłocka-Olech L et al. (2016) TLC determination of flavonoids from different cultivars of Allium cepa and Allium ascalonicum. Acta Pharm 66(4):543-554. doi:10.1515/acph-2016-0038", PM % "27749248", "De Gruyter"+AB, A),
 ("Mo H et al. (1993) Purification and characterization of a mannose-specific lectin from shallot (Allium ascalonicum) bulbs. Arch Biochem Biophys 306(2):431-438. doi:10.1006/abbi.1993.1534", PM % "8215447", "Elsevier"+AB, A),
 ("Arpornchayanon W et al. (2022) Antiallergic activities of shallot (Allium ascalonicum L.) and its therapeutic effects in allergic rhinitis. Asian Pac J Allergy Immunol 40(4):393-400. doi:10.12932/AP-300319-0529", PM % "31421664", "APJAI"+AB, A),
 ("Tian P et al. (2021) Analysis of volatile compound changes in fried shallot (Allium cepa L. var. aggregatum) oil at different frying temperatures by GC-MS, OAV, and multivariate analysis. Food Chem 345:128748. doi:10.1016/j.foodchem.2020.128748", PM % "33340890", "Elsevier"+AB, A),
 ("Ratseewo J et al. (2025) Changes in chemical composition, volatile compound, and bioactive compounds retention in shallots under different drying methods. Food Chem X 27:102419. doi:10.1016/j.fochx.2025.102419", PM % "40231128", "Elsevier"+AB, A),
 ("Le Guen-Le Saos F et al. (2002) In vitro bulb development in shallot (Allium cepa L. Aggregatum Group): effects of anti-gibberellins, sucrose and light. Ann Bot 89(4):419-425. doi:10.1093/aob/mcf063", PM % "12096802", "Oxford University Press"+AB, A),
 ("Hizume M (1994) Allodiploid nature of Allium wakegi Araki revealed by genomic in situ hybridization and localization of 5S and 18S rDNAs. Jpn J Genet 69(4):407-415. doi:10.1266/jjg.69.407", PM % "7946461", "Genetics Society of Japan"+AB, A),
 ("Masuzaki S et al. (2006) Complete assignment of structural genes involved in flavonoid biosynthesis influencing bulb color to individual chromosomes of the shallot (Allium cepa L.). Genes Genet Syst 81(4):255-263. doi:10.1266/ggs.81.255", PM % "17038797", "Genetics Society of Japan"+AB, A),
 ("Hang TT et al. (2004) Production and characterization of alien chromosome additions in shallot (Allium cepa L. Aggregatum group) carrying extra chromosome(s) of Japanese bunching onion (A. fistulosum L.). Genes Genet Syst 79(5):263-269. doi:10.1266/ggs.79.263", PM % "15599056", "Genetics Society of Japan"+AB, A),
 ("Fujito S et al. (2021) Construction of a high-density linkage map and graphical representation of the arrangement of transcriptome-based unigene markers on the chromosomes of onion, Allium cepa L. BMC Genomics 22:481. doi:10.1186/s12864-021-07803-y", PM % "34174821", "BioMed Central"+AB, A),
 ("Masamura N et al. (2012) Chromosomal Organization and Sequence Diversity of Genes Encoding Lachrymatory Factor Synthase in Allium cepa L. G3 2(6):643-651. doi:10.1534/g3.112.002592", PM % "22690373", "Genetics Society of America"+AB, A),
 ("Zheng SJ et al. (2005) Two different Bacillus thuringiensis toxin genes confer resistance to beet armyworm (Spodoptera exigua Hübner) in transgenic Bt-shallots (Allium cepa L.). Transgenic Res 14(3):261-272. doi:10.1007/s11248-005-0109-2", PM % "16145834", "Springer"+AB, A),
 ("EFSA (2023) Modification of the existing maximum residue levels for prothioconazole in garlic, onions and shallots. EFSA J 21(1):e07717. doi:10.2903/j.efsa.2023.7717", PM % "36628330", "유럽식품안전청(EFSA)"+AB, A),
 ("EFSA (2017) Modification of the existing maximum residue levels for fluazinam in onions, shallots and garlic. EFSA J 15(7):e04904. doi:10.2903/j.efsa.2017.4904", PM % "32625565", "유럽식품안전청(EFSA)"+AB, A),
 ("Iacovou M et al. (2015) The Low FODMAP Diet and Its Application in East and Southeast Asia. J Neurogastroenterol Motil 21(4):459-470. doi:10.5056/jnm15111", PM % "26350937", "대한소화기기능성질환·운동학회"+AB, A),
 ("Kim SW et al. (2016) Residue level and dissipation pattern of lepimectin in shallots using high-performance liquid chromatography coupled with photodiode array detection. Biomed Chromatogr 30(11):1835-1842. doi:10.1002/bmc.3759", PM % "27187504", "Wiley"+AB, A),
 ("Crespo R, Chin RP (2004) Effect of feeding green onions (Allium ascalonicum) to White Chinese geese. J Vet Diagn Invest 16(4):321-325. doi:10.1177/104063870401600411", PM % "15305744", "SAGE"+AB, A),
 ("Saptana et al. (2021) The competitiveness analysis of shallot in Indonesia: A Policy Analysis Matrix. PLoS One 16(9):e0256832. doi:10.1371/journal.pone.0256832", PM % "34478456", "PLOS"+AB, A),
 ("Arunkumar K et al. (2018) Antifungal and antibiofilm activity of Persian shallot (Allium stipitatum Regel.) against clinically significant Candida spp. Trop Biomed 35(3):815-825", PM % "33601768", "Malaysian Society of Parasitology and Tropical Medicine"+AB, A),
 ("van der Vlugt RA et al. (1999) Further Evidence that Shallot Yellow Stripe Virus (SYSV) Is a Distinct Potyvirus and Reidentification of Welsh Onion Yellow Stripe Virus as a SYSV Strain. Phytopathology 89(2):148-155. doi:10.1094/PHYTO.1999.89.2.148", PM % "18944789", "American Phytopathological Society"+AB, A),
]
sources = [{"n": i+1, "title": t, "url": u, "publisher": p, "accessed": a} for i, (t, u, p, a) in enumerate(S)]

sections = [
 ("overview", "한눈에 보기", """숙근초(Allium ascalonicum L.)는 식약처 「식품원료 목록」에 영문명 'Shallot(샬롯)'으로 올라 있는 수선화과(Amaryllidaceae) 부추속 식물이다[1][2]. 목록에는 '숙근초비늘줄기'와 '숙근초잎' 두 원료가 있고, 사용 가능 부위는 비늘줄기(Bulb)와 잎, 상태는 '사용가능'이다[1]. 목록의 별명 칸은 비어 있어 국문명 '숙근초'는 이 목록의 대표 원료명에서 그대로 가져온 것이다[1]. 이 국문명을 국가표준식물목록 같은 다른 공식 국명 목록과 대조하지는 못했다(확인하지 못함).

샬롯은 한 포기에서 작은 비늘줄기 3–10개가 무리 지어 생기며, 양파보다 작고 길쭉하다[4]. 주요 기능 성분은 퀘르세틴 배당체 같은 플라보놀과 S-알크(에)닐-L-시스테인 설폭사이드(ACSO) 같은 황화합물이고, 이눌린형 프럭탄도 많다[3][8]. 효능 연구는 대부분 세포·동물 실험이고, 사람 자료는 관찰 연구와 소규모 무작위 시험에 그친다[2][16]. 국내 생산 통계는 확인하지 못함."""),
 ("history", "역사", """샬롯이라는 이름은 고대 그리스 상인들이 팔레스타인의 옛 항구 아슈켈론(지금의 이스라엘 아슈켈론)에서 이 식물을 알게 되어 그 도시 이름을 붙였다는 설명이 있다[2]. 영어 'shallot'은 고대 프랑스어 'escalogne'을 거쳐 라틴어 'Ascalonia caepa(아슈켈론의 양파)'에서 왔다[2]. 일부 학자는 켈트족 등 중동에서 이주한 사람들이 샬롯을 유럽에 들여왔다고 본다[2].

샬롯은 뵈프 부르기뇽 같은 프랑스 요리와 깊이 연관되지만 태국 수프·커리와 인도네시아 볶음밥 같은 아시아 요리에서도 빠지지 않는 재료다[2]. 태국 남부에서는 잎을 찧어 지방종에 붙이는 민간요법이, 나이지리아 오요주에서는 회선사상충증 치료에 쓰는 민간 용도가 보고되었다[2]. 북유럽(페노스칸디아)에서는 영양번식 클론으로 집 텃밭에서 오래 길러 왔고, 최근 수십 년간 80개가 넘는 계통이 수집되었다[7]. 크로아티아 해안과 섬에서도 농가가 여러 세대에 걸쳐 영양번식으로 지켜 온 재래종이 남아 있다[5]. 인도네시아는 샬롯을 국가 전략 품목으로 다룬다[31]."""),
 ("biology", "식물학적 특징", """샬롯은 키 20–30 cm 정도로 자라고 잎은 원통형이며, 비늘줄기는 보통 2–3개의 작은 쪽이 한 껍질에 함께 싸인 복합 구조로 무게가 약 5–25 g이다[2]. 겉껍질 색은 자주·빨강·적갈색·노랑·회색·흰색 등 품종마다 다르고, 모양도 둥근 것부터 길쭉한 것까지 있다[2]. 인도네시아 품종 10종을 잰 연구에서는 비늘줄기 지름이 1.35–3.00 cm, 무게가 2–12 g이었다[4]. 양파가 보통 큰 비늘줄기 하나를 만드는 데 비해 샬롯은 한 포기에 3–10개가 무리 지어 생긴다[4].

생활형은 출처마다 달라, 한해살이 초본으로 적은 리뷰와 여러해살이 식물로 적은 연구가 함께 있다[2][3]. Aggregatum 군 샬롯의 염색체 수는 2n = 2x = 16이다[3][5]. 시험관 배양에서는 16시간 일장과 배지 자당 30–50 g/L 조건에서 비늘줄기가 생겼고, 지베렐린을 넣으면 비늘줄기 형성이 억제되었다[19]. 샬롯은 수확 뒤 더 익지 않는 비호흡급등형 작물이며, 수분이 80%를 넘어 쉽게 상한다[4]."""),
 ("related_species", "학명과 근연 분류군", """학명 처리는 출처마다 다르다[1][2][3][4]. 식약처 목록은 Allium ascalonicum L.로 적지만[1], 크로아티아 연구진은 샬롯을 예전에는 별개 종(A. ascalonicum)으로 보다가 지금은 양파(Allium cepa) 안의 Aggregatum 군으로 분류한다고 설명한다[3]. 다른 리뷰는 A. cepa var. aggregatum 또는 var. ascalonicum이라는 변종 이름을 쓰고[4], 체계적 고찰 논문은 A. ascalonicum·Aggregatum 군·var. aggregatum으로 적힌 연구를 모두 샬롯으로 묶었다[2]. 이 자료는 식약처 목록의 학명을 제목으로 쓰되, 샬롯(Aggregatum 군·var. aggregatum 포함)으로 밝힌 연구만 쓰고 일반 구형 양파 자료는 넣지 않았다[1][3].

크로아티아에서는 2배체 A. × proliferum과 3배체 A. × cornutum 같은 주아형 양파도 '샬롯'이라 불러, 같은 이름 아래 다른 분류군이 섞여 있다[3][5]. Aggregatum 군 안에서는 길쭉한 '샬롯형'과 둥근 '감자양파형'이 구분되기도 하지만[6], 북유럽 수집 계통의 분석은 두 이름의 구분을 뒷받침하지 않았다[7]. '페르시아 샬롯'은 Allium stipitatum이라는 다른 종이다[32]. Allium wakegi는 양파 근연 계통과 파(A. fistulosum)의 교잡에서 생긴 이질 2배체로 보고된 별개 분류군이다[20]. 식약처 목록에서 '쪽파'는 대파(Allium fistulosum)의 다른 이름으로 올라 있어 이 소재와 구분된다[1]."""),
 ("cultivation", "재배", """샬롯은 인도네시아처럼 더운 지역의 해발 0–800 m 저지대·중산간에서 햇빛을 충분히 받으며 잘 자라고, 심은 뒤 55–70일에 잎이 시들고 줄기 목이 물러지면 수확한다[4]. 인도네시아 대표 품종 Bima는 저지대에서 심은 지 60일, 줄기의 60%가 꺾일 때 거둔다[4]. 번식은 주로 비늘줄기(종구)로 하며, 1 ha에 종구 1.2–1.5 t이 드는 데 비해 씨앗(TSS)은 3–5 kg이면 되고 수량도 높지만 수확까지 120–155일이 걸린다[4].

크로아티아 시험에서는 10월 초에 포기 사이 20 cm, 줄 사이 30 cm로 심어 이듬해 7월 초 잎줄기의 50%가 꺾였을 때 거두고 그늘에서 한 달 말렸다[3]. 저장 최적 조건은 7–10 °C, 상대습도 65–75%로 제시되며, 인도네시아의 상온(25–30 °C) 전통 저장에서는 무게가 약 25% 줄고 수확 후 손실은 20–40%에 이른다[4]. 저장 중에는 푸사리움 밑썩음병·흑색곰팡이·탄저병·무름병이 문제가 되고, 감염된 종구는 바이러스를 다음 작기로 옮긴다[4]. 샬롯 노란줄무늬 바이러스(SYSV)는 양파 위황병 바이러스와 다른 포티바이러스로 정리되었다[33]. 국내 재배 면적과 생산량은 확인하지 못함."""),
 ("processing", "가공과 이용", """샬롯은 생으로 먹거나 조리해 양념으로 쓰며, 동남아시아에서는 주로 조미 재료로 소비된다[8]. 튀긴 샬롯 기름에서는 휘발 성분 93종이 확인되었고 헥산알·디프로필 디설파이드·피라진류가 향을 좌우했다[17]. 가열 방식은 황화합물에 큰 영향을 주어, 통째로 삶거나 고압 가열하면 유기 다황화물의 95% 이상이, 으깬 뒤 가열하면 76–80%가 사라졌고 동결건조는 대부분을 보존했다[12].

건조 방법 비교에서는 동결건조가 퀘르세틴과 주된 휘발 성분인 유칼립톨을 가장 잘 지켰고, 80 °C 열풍건조는 총 페놀·플라보노이드 값이 가장 높았다[18]. 말린 겉껍질은 퀘르세틴의 83.3%가 비배당체로, 속살(배당체 99.2%)보다 사람 혈중 퀘르세틴 노출(AUC)이 약 두 배였다[13]. 두 품종의 겉껍질 플라보놀은 5,426과 8,916 mg/kg(생중량)으로 먹는 부분(209와 523 mg/kg)보다 훨씬 많았다[14]. 국내에서 숙근초를 원료로 한 제품 생산실적은 확인하지 못함."""),
 ("genetics", "유전·육종", """샬롯(Aggregatum 군)은 2n = 2x = 16의 2배체로 양파와 유전적으로 가깝다[3][8]. 일본 연구진은 샬롯과 파(A. fistulosum)의 복2배체 잡종을 되교배해 여러 종류의 이종 염색체 첨가 계통을 만들었다[22]. 파–샬롯 단일 염색체 첨가 계통을 이용해 비늘줄기 색을 정하는 플라보노이드 합성 유전자(CHS·CHI·F3H·DFR·ANS)와 3GT를 샬롯의 개별 염색체에 모두 배정했다[21]. 같은 계통으로 눈물을 나게 하는 최루인자 합성효소(LFS) 유전자는 5번 염색체에 배정되었다[24].

배가반수체 샬롯(DHA)의 유전자 서열을 기준으로 전사체 SNP를 분석해 25,462개 유전자를 8개 염색체에 고정하고 고밀도 연관 지도를 만들었다[23]. 인도네시아 샬롯 재래종은 구형 양파보다 아미노산과 플라보노이드가 많아 양파 육종의 유전 자원으로 제안되었다[9]. 아그로박테리움으로 Bt 독소 유전자(cry1Ca·H04)를 넣어 파밤나방에 저항하는 형질전환 샬롯을 만든 연구도 있다[25]. 샬롯 자체의 전장 유전체 조립은 확인하지 못함."""),
 ("safety", "안전성", """숙근초는 식약처 목록에서 비늘줄기와 잎을 쓸 수 있는 '사용가능' 원료이며 별도 사용 조건은 없다[1]. 샬롯은 양파·마늘과 함께 대표적인 고FODMAP 재료로 꼽혀 과민성대장증후군 저FODMAP 식단에서는 제한 대상이다[28]. 알레르기 비염 환자 16명 시험에서 하루 3 g(비늘줄기 약 1.5개) 샬롯을 4주 먹었을 때 이상반응은 위약과 다르지 않았다[16]. 거위에게 'green onions(A. ascalonicum)'를 먹인 사례와 시험에서 빈혈과 간 손상이 나타났다[30].

유럽식품안전청(EFSA)은 양파·마늘·샬롯의 프로티오코나졸과 플루아지남 잔류허용기준 변경을 검토해, 신청된 사용법에서는 소비자 건강 위험이 낮다고 결론지었다[26][27]. 국내 온실(나주·무안)에서 'shallot'으로 표기된 작물에 레피멕틴을 뿌린 연구에서는 반감기가 1.7–1.9일이었다[29]. 다만 이 시료가 샬롯인지 쪽파 같은 다른 파속 채소인지는 초록만으로 확인하지 못함. 샬롯에 대한 식품 알레르기 사례 보고와 국내 잔류허용기준은 확인하지 못함."""),
]

compounds = [
 dict(name="Quercetin 4'-O-glucoside", name_ko="퀘르세틴-4′-글루코사이드(스피래오사이드)", **{"class":"플라보놀 배당체"}, role="marker", part="비늘줄기",
      content_text="34개 샬롯 계통 56.1–287.9 mg/100 g(건조중량), 최고값은 Aggregatum 샬롯형 IPT241[3]", activity_ko="샬롯 비늘줄기에서 가장 많은 플라보노이드[3][5]", source=[3,5]),
 dict(name="Quercetin 3,4'-O-diglucoside", name_ko="퀘르세틴-3,4′-다이글루코사이드", **{"class":"플라보놀 배당체"}, role="marker", part="비늘줄기",
      content_text="Aggregatum 군 27.0–107.0 mg/kg(생중량); 계통 최고 143.2 ± 17.5 mg/100 g(건조중량)[3]", activity_ko="퀘르세틴-4′-글루코사이드와 함께 샬롯의 주요 페놀 성분[3][5]", source=[3,5]),
 dict(name="Quercetin", name_ko="퀘르세틴", **{"class":"플라보놀"}, role="bioactive", part="비늘줄기·겉껍질",
      content_text="5.16–36.15 mg/100 g(건조중량)[3]; 리뷰 집계 218.91–1766.40 ppm[4]; 말린 겉껍질은 퀘르세틴의 83.3%가 비배당체[13]", activity_ko="사람 교차시험에서 겉껍질(비배당체 위주) 섭취 시 혈중 AUC 47.23 µmol·h/L로 속살(22.23)보다 높음[13]", source=[3,4,13]),
 dict(name="Isorhamnetin 4'-O-glucoside", name_ko="이소람네틴-4′-글루코사이드", **{"class":"플라보놀 배당체"}, role="bioactive", part="비늘줄기",
      content_text="5.0–59.2 mg/100 g(건조중량)[3]", activity_ko="Aggregatum 군을 다른 샬롯 분류군과 가르는 주요 변수 중 하나[3]; 비늘줄기에서 이소람네틴 배당체가 다량 분리됨[10]", source=[3,10]),
 dict(name="Isoalliin", name_ko="이소알리인(S-1-프로페닐-L-시스테인 설폭사이드, PeCSO)", **{"class":"ACSO(황화합물 전구체)"}, role="marker", part="비늘줄기",
      content_text="", activity_ko="메티인과 함께 샬롯의 매운맛과 관련된 주요 ACSO로, 인도네시아 재래종에서 일본 양파보다 많이 축적됨[8]", source=[8]),
 dict(name="Methiin", name_ko="메티인(S-메틸-L-시스테인 설폭사이드, MeCSO)", **{"class":"ACSO(황화합물 전구체)"}, role="bioactive", part="비늘줄기",
      content_text="", activity_ko="샬롯 재래종에 많이 축적된 매운맛 관련 ACSO[8]", source=[8]),
 dict(name="Inulin", name_ko="이눌린(이눌린형 프럭탄)", **{"class":"다당류(프럭탄)"}, role="nutrient", part="비늘줄기",
      content_text="Aggregatum 샬롯형 18.7–26.4 g/100 g, 감자양파형 29.3–29.9 g/100 g(건조중량)[3]", activity_ko="프리바이오틱 성분으로 소개됨[3]; 샬롯이 고FODMAP 식품으로 분류되는 까닭인 프럭탄 계열[28]", source=[3,28]),
 dict(name="Ascalonicoside A1", name_ko="아스칼로니코사이드 A1/A2", **{"class":"푸로스타놀 사포닌"}, role="bioactive", part="비늘줄기",
      content_text="", activity_ko="샬롯 비늘줄기에서 처음 보고된 새 푸로스타놀 사포닌[10]", source=[10]),
 dict(name="Alliospiroside A", name_ko="알리오스피로사이드 A", **{"class":"스테로이드 사포닌"}, role="bioactive", part="뿌리·밑동",
      content_text="", activity_ko="밑동·뿌리 부탄올 추출물의 주요 항진균 성분으로 식물병원균에 넓게 작용(식물 실험)[11]", source=[11]),
 dict(name="Dipropyl disulfide", name_ko="디프로필 디설파이드", **{"class":"유기황 휘발 성분"}, role="bioactive", part="비늘줄기(튀김 기름)",
      content_text="튀긴 샬롯 기름의 향 활성값(OAV) 1 이상 성분 중 하나[17]", activity_ko="튀긴 샬롯 기름 향에 중요한 성분[17]; 샬롯 유기황화물 17종은 가열로 크게 줄어듦[12]", source=[12,17]),
 dict(name="Eucalyptol", name_ko="유칼립톨(1,8-시네올)", **{"class":"모노테르펜 휘발 성분"}, role="bioactive", part="비늘줄기",
      content_text="생 샬롯의 주된 휘발 성분[18]", activity_ko="동결건조에서 가장 잘 보존됨[18]", source=[18]),
 dict(name="Proline", name_ko="프롤린", **{"class":"아미노산"}, role="nutrient", part="비늘줄기",
      content_text="건조 샬롯의 주된 아미노산[18]", activity_ko="샬롯 재래종은 구형 양파보다 아미노산 함량이 높음[9]", source=[9,18]),
 dict(name="Potassium", name_ko="칼륨", **{"class":"무기질"}, role="nutrient", part="비늘줄기",
      content_text="334 mg/100 g(리뷰 표 재인용)[4]", activity_ko="샬롯 비늘줄기에서 가장 많은 다량 무기질[3]", source=[3,4]),
 dict(name="Allium ascalonicum agglutinin", name_ko="샬롯 렉틴(AAA, 만노스 결합 렉틴)", **{"class":"단백질(렉틴)"}, role="bioactive", part="비늘줄기",
      content_text="", activity_ko="분자량 약 11 kDa의 만노스 특이 렉틴으로 비늘줄기에서 분리됨[15]", source=[15]),
]

assays = [
 {"role":"literature","compound":"Quercetin 4'-O-glucoside","compound_ko":"퀘르세틴-4′-글루코사이드(퀘르세틴·배당체 4종 동시 정량)","part":"비늘줄기(동결건조 분말)",
  "content":"34개 샬롯 계통 56.1–287.9 mg/100 g(건조중량)[3]","method":"HPLC-PDA(확인 LC-ESI-QqQ)",
  "conditions":{"instrument":"Shimadzu Nexera LC-40DX3 펌프 2대, SIL-40CX3 자동시료주입기, CTO-40C 칼럼오븐, SPD-M40 광다이오드배열 검출기; 동정은 Shimadzu LCMS-8045 삼중사중극자 질량분석기",
   "column":"C18 코어셸, 2.1 × 150 mm, 2.7 µm (Advanced Materials Technology)","mobile_phase":"A: 물/0.1% 포름산, B: 아세토니트릴/0.1% 포름산",
   "gradient":"0–2분 95% A; 2–20분 95→50% A; 20–21분 50→5% A; 21–23분 5% A; 23–24분 5→95% A; 24–30분 95% A","flow":"0.35 mL/min","temp":"37 °C",
   "detection":"360 nm","injection":"5 µL",
   "sample_prep":"비늘줄기 −80 °C 동결 → 동결건조 → 0.2 mm 분쇄 → 75 mg에 80% 메탄올 1.5 mL, 초음파 30분 → 150 rpm·20 °C 3.5시간 진탕 → 15,000×g 5분 원심 → 0.22 µm 나일론 여과",
   "standard":"퀘르세틴, 퀘르세틴-3-글루코사이드, 퀘르세틴-4′-글루코사이드, 퀘르세틴-3,4′-다이글루코사이드 표준품(1–100 mg/L 7단계)",
   "linearity":"퀘르세틴-4′-글루코사이드 y = 1.09028x − 3.63246, 결정계수 0.9994","lod":"","loq":"","recovery":"99.2 ± 0.8%"},
  "rationale":"샬롯 비늘줄기에서 가장 많은 플라보노이드로, 샬롯 분류군을 가르는 주요 변수였다[3]. 검출·정량한계는 전문에 없어 비워 둠.",
  "source":[3],"url":PMC % "PMC9405304","source_kind":"paper"},
 {"role":"literature","compound":"Inulin","compound_ko":"이눌린(자당·포도당·과당 동시 정량)","part":"비늘줄기(동결건조 분말)",
  "content":"Aggregatum 샬롯형 18.7–26.4 g/100 g, 감자양파형 29.3–29.9 g/100 g(건조중량)[3]","method":"HPLC-RID",
  "conditions":{"instrument":"Shimadzu Nexera LC-40DX3 펌프, SIL-40CX3 자동시료주입기, CTO-40C 칼럼오븐, RID-20A 굴절률 검출기",
   "column":"칼슘 이온교환 칼럼 ReproGel Ca (Dr. Maisch), 300 × 8 mm, 9 µm","mobile_phase":"탈이온수","gradient":"등용매","flow":"1 mL/min","temp":"80 °C",
   "detection":"굴절률 검출(RID)","injection":"10 µL",
   "sample_prep":"플라보노이드 분석과 같은 80% 메탄올 초음파·진탕 추출물(75 mg/1.5 mL), 원심 후 0.22 µm 나일론 여과",
   "standard":"이눌린·자당·포도당·과당 표준품 0.25–10.00 g/L 7단계",
   "linearity":"이눌린 y = 1850.07x + 109.39, 결정계수 0.9998","lod":"","loq":"","recovery":"100.4 ± 0.2%"},
  "rationale":"샬롯 비늘줄기에서 가장 많은 당류로, 건물 함량과 함께 Aggregatum 군을 다른 샬롯 분류군과 가르는 핵심 변수였다[3]. 검출·정량한계는 전문에 없어 비워 둠.",
  "source":[3],"url":PMC % "PMC9405304","source_kind":"paper"},
 {"role":"literature","compound":"Isoalliin","compound_ko":"이소알리인 등 ACSO 13종","part":"비늘줄기(껍질 벗겨 동결건조)",
  "content":"","method":"LC-MS/MS(ESI)",
  "conditions":{"instrument":"Agilent 1200 HPLC + 3200 Q TRAP 질량분석기(AB SCIEX), ESI 이온원",
   "column":"AQUASIL SS-1251-120, 4.6 × 250 mm (Sensyu Scientific)","mobile_phase":"0.1% 트리플루오로아세트산(TFA) 수용액","gradient":"등용매","flow":"","temp":"",
   "detection":"ESI-MS/MS","injection":"",
   "sample_prep":"껍질 벗긴 비늘줄기 동결건조·분쇄 → 초순수 500 µL 추출 → 원심 → 초순수로 20배 희석 → 0.45 µm 여과",
   "standard":"각 ACSO 표준품으로 정성·정량","linearity":"","lod":"","loq":"","recovery":""},
  "rationale":"ACSO는 샬롯·양파의 매운맛과 향을 내는 대표 성분으로, 샬롯 재래종에서 일본 양파보다 많이 쌓였다[8]. 전문을 확인했으나 함량은 그림으로만 제시되어 수치를 옮기지 못했고, 유속·온도·주입량·검출한계는 본문에 없어 비워 둠.",
  "source":[8],"url":PMC % "PMC9783499","source_kind":"paper"},
]

nutrients = [{"form":"샬롯 비늘줄기, 생것 — 무기질(Prabawati 등 2026 리뷰 표 4 재인용)","basis":"100 g",
  "items":[{"name":"칼슘","value":37,"unit":"mg"},{"name":"마그네슘","value":21,"unit":"mg"},{"name":"칼륨","value":334,"unit":"mg"},
           {"name":"철","value":1.2,"unit":"mg"},{"name":"아연","value":0.4,"unit":"mg"},{"name":"망간","value":0.292,"unit":"mg"},{"name":"인","value":60,"unit":"mg"}],
  "source":[4]}]

d = {"slug":"allium-ascalonicum","name_ko":"숙근초","name_en":"Shallot","scientific_name":"Allium ascalonicum L.",
     "aliases":["샬롯","Shallot","숙근초비늘줄기","숙근초잎","Allium cepa L. Aggregatum group","Allium cepa var. aggregatum"],
     "sections":[{"key":k,"title":t,"body":b} for k,t,b in sections],
     "compounds":compounds,"markers":[],"nutrients":nutrients,"assays":assays,
     "production":[],"world":[],"gi":[],"orgs":[],"sources":sources}
(HERE/"dossier.json").write_text(json.dumps(d,ensure_ascii=False,indent=1),encoding="utf-8")
for k,t,b in sections: print(k,len(b))
