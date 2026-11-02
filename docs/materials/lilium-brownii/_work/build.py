import json, re
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
PM = "PubMed"
A = "2026-11-02"
S = [
 ("mfds", "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 홍콩백합꽃잎·홍콩백합비늘줄기(Lilium brownii F.Br. ex Miellez / Lilium austale Stapf / Lilium brownii var. australe; 별명 당나리·당개나리), 사용가능, 사용가능부위: 비늘줄기, 꽃잎; 대조: 백합가루·백합추출액·백합꽃잎·백합비늘줄기·백합뿌리(참나리 L. lancifolium / 백합(百合) L. brownii var. viridulun[원문 표기] / 큰솔나리 L. pumilum), 참나리추출분말(개별인정형, L. lancifolium), 중나리·섬말나리·야마유리·땅나리·말나리·하늘말나리 등 같은 속 다른 행 (로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json)", "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "식품의약품안전처", "2026-10-13"),
 ("review", "Traditional uses, nutritional properties, phytochemical metabolites, pharmacological properties, and potential applications of Lilium spp.: a systematic review — Front Pharmacol 2025 (PMID 41368573, PMC12682905, 전문 확인; 받아온 전문에서 학명 이탤릭이 빠져 문맥으로 종을 판단)", "https://doi.org/10.3389/fphar.2025.1713957", PM, A),
 ("herbal", "[Herbal textual research on traditional Chinese medicine \"Baihe\" (Lilii Bulbus)] — Zhongguo Zhong Yao Za Zhi 2019 (PMID 31872612, 초록만 확인)", "https://doi.org/10.19540/j.cnki.cjcmm.20190903.101", PM, A),
 ("cp", "The complete chloroplast genome of Lilium brownii F.E.Brown var. viridulum Baker (Liliaceae) — Mitochondrial DNA B Resour 2020 (PMID 33366839, PMC7748718, 초록 확인)", "https://doi.org/10.1080/23802359.2020.1720534", PM, A),
 ("gd", "Genetic diversity and genetic structure analysis of the natural populations of Lilium brownii from Guangdong, China — Biochem Genet 2009 (PMID 19543969, 초록 없음, 제목만 확인)", "https://doi.org/10.1007/s10528-009-9258-y", PM, A),
 ("poly", "Systematic evaluation on the physicochemical characteristics of a series polysaccharides extracted from different edible lilies by ultrasound and subcritical water — Front Nutr 2022 (PMID 36204382, PMC9531164, 전문 확인; 학명은 약어 LBVP와 채집지로 판단)", "https://doi.org/10.3389/fnut.2022.998942", PM, A),
 ("bitter", "Integrative analysis of metabolome and transcriptome provide new insights into the bitter components of Lilium lancifolium and Lilium brownii — J Pharm Biomed Anal 2022 (PMID 35462288, 초록만 확인)", "https://doi.org/10.1016/j.jpba.2022.114778", PM, A),
 ("colch", "LC-MS-Based Screening for Colchicine and Characterization of Major Bitter Constituents in Lily — Molecules 2026;31(4):721 (PMID 41752498, PMC12942747, 전문 확인; 'Longya' 품종 학명은 받아온 전문에서 빠져 있음)", "https://doi.org/10.3390/molecules31040721", PM, A),
 ("antiinf", "Bioassay-Guided Isolation of Anti-Inflammatory Components from the Bulbs of Lilium brownii var. viridulum and Identifying the Underlying Mechanism through Acting on the NF-κB/MAPKs Pathway — Molecules 2017 (PMID 28333094, PMC6154308, 초록 확인)", "https://doi.org/10.3390/molecules22040506", PM, A),
 ("cf", "A phenolic acid glyceride dimer isolated from Lilium brownii exerts neuroprotective effects in Parkinson's disease by modulating the p62-Keap1-Nrf2 signalling pathway — Eur J Pharmacol 2026 (PMID 41620005, 초록만 확인)", "https://doi.org/10.1016/j.ejphar.2026.178618", PM, A),
 ("mao", "Two New Phenylpropanoid Compounds from Lilium Brownii and Their Anti-monoamine Oxidase Activity — Chem Biodivers 2024 (PMID 38634793, 초록만 확인)", "https://doi.org/10.1002/cbdv.202400524", PM, A),
 ("iso", "Two New Isospirostanol-Type Saponins from the Bulbs of Lilium Brownii and Their Anti-Hepatocarcinogenic Activity — Chem Biodivers 2024 (PMID 38414116, 초록만 확인)", "https://doi.org/10.1002/cbdv.202400257", PM, A),
 ("sap", "New steroidal saponins from the bulbs of Lilium brownii var. viridulum — Carbohydr Res 2012 (PMID 22960210, 초록만 확인)", "https://doi.org/10.1016/j.carres.2012.07.027", PM, A),
 ("gm", "Extraction, structural characterization and immunoactivity of glucomannan type polysaccharides from Lilium brownii var. viridulum Baker — Carbohydr Res 2024 (PMID 38335805, 초록만 확인)", "https://doi.org/10.1016/j.carres.2024.109046", PM, A),
 ("llp11", "Purification, characterization, simulated gastrointestinal digestion and gut microbiota fermentation of a mannoglucan from Lilium brownii var. viridulum (Longya lily) — Food Chem X 2024 (PMID 39139491, PMC11321392, 초록 확인)", "https://doi.org/10.1016/j.fochx.2024.101671", PM, A),
 ("pectin", "Pectic polysaccharides from Lilium brownii and Polygonatum odoratum exhibit significant antioxidant effects in vitro — Int J Biol Macromol 2023 (PMID 38123037, 초록만 확인)", "https://doi.org/10.1016/j.ijbiomac.2023.128830", PM, A),
 ("starch", "Effects of heat-moisture and acid treatments on the structural, physicochemical, and in vitro digestibility properties of lily starch (Lilium brownii var. viridulum Baker) — Int J Biol Macromol 2020 (PMID 31972200, 초록만 확인)", "https://doi.org/10.1016/j.ijbiomac.2020.01.181", PM, A),
 ("chloro", "Two new chlorophenyl glycosides from the bulbs of Lilium brownii var. viridulum — J Asian Nat Prod Res 2012 (PMID 22694345, 초록만 확인)", "https://doi.org/10.1080/10286020.2012.691096", PM, A),
 ("func", "Integrative analysis of metabolome and transcriptome provides new insights into functional components of Lilii Bulbus — Chin Herb Med 2024 (PMID 39072198, PMC11283230, 초록 확인)", "https://doi.org/10.1016/j.chmed.2023.10.004", PM, A),
 ("auto", "Physiological and transcriptomic analyses provide preliminary insights into the autotoxicity of Lilium brownii var. viridulum (Longya lily) — Front Plant Sci 2024 (PMID 38807780, PMC11130447, 초록 확인)", "https://doi.org/10.3389/fpls.2024.1330061", PM, A),
 ("dtbp", "Biodegradation of 2,4-di-tert-butylphenol in continuous cropping field: Impacts on sustainable cultivation of Lilium brownii — J Environ Manage 2026 (PMID 41775239, 초록만 확인)", "https://doi.org/10.1016/j.jenvman.2026.129162", PM, A),
 ("regen", "Establishment of Highly Efficient Plant Regeneration, Callus Transformation and Analysis of Responsive PR Promoters in Lilium brownii var. viridulum — Plants 2023 (PMID 37653909, PMC10221712, 초록 확인)", "https://doi.org/10.3390/plants12101992", PM, A),
 ("rot", "Integrated transcriptomic and metabolomic analysis reveals the molecular profiles of dynamic variation in Lilium brownii var. viridulum suffering from bulb rot — Front Genet 2024 (PMID 39205945, PMC11349735, 초록 확인)", "https://doi.org/10.3389/fgene.2024.1432997", PM, A),
 ("asgv", "First report of apple stem grooving virus infecting a species of Lilium (Lilium brownii) in China — Mol Biol Rep 2026 (PMID 41733802, 초록만 확인)", "https://doi.org/10.1007/s11033-026-11597-1", PM, A),
 ("flav", "Integrative metabolomic and transcriptomic profiling deciphers flavonoid biosynthesis of bulbs in Lilium brownii var. viridulum — Sci Rep 2026 (PMID 41844743, PMC13128856, 초록 확인)", "https://doi.org/10.1038/s41598-026-43274-5", PM, A),
 ("glyc", "Multi-Omics Decoding of Potential Microbial-Genetic Synergy Underlying Polysaccharide and Glycosidic Polymer Biosynthesis in Two Cultivars of Lilium brownii var. viridulum Baker — Metabolites 2025 (PMID 41295298, PMC12654296, 초록 확인)", "https://doi.org/10.3390/metabo15110712", PM, A),
 ("catrev", "Lily toxicity in the cat — Top Companion Anim Med 2010 (PMID 21147474, 초록만 확인)", "https://doi.org/10.1053/j.tcam.2010.09.006", PM, A),
 ("easter", "A comprehensive study of Easter lily poisoning in cats — J Vet Diagn Invest 2004 (PMID 15586568, 초록만 확인)", "https://doi.org/10.1177/104063870401600607", PM, A),
 ("insom", "A comprehensive study on the relieving effect of Lilium brownii on the intestinal flora and metabolic disorder in p-chlorphenylalanine induced insomnia rats — Pharm Biol 2022 (PMID 34978949, PMC8725957, 초록 확인)", "https://doi.org/10.1080/13880209.2021.2019283", PM, A),
 ("lc2d", "In-depth exploration and comparison of chemical constituents from two Lilium species through offline two-dimensional liquid chromatography combined with multimode acquisition of high-resolution mass spectrometry — J Chromatogr A 2022 (PMID 35339744, 초록만 확인)", "https://doi.org/10.1016/j.chroma.2022.462980", PM, A),
 ("nir", "Rapid identification of Lilium species and polysaccharide contents based on near infrared spectroscopy and weighted partial least square method — Int J Biol Macromol 2020 (PMID 32179116, 초록만 확인)", "https://doi.org/10.1016/j.ijbiomac.2020.03.109", PM, A),
 ("pd", "Neuroprotective properties of the Lilium brownii extracts in the experimental model of Parkinson's disease — Metab Brain Dis 2024 (PMID 39060803, 초록만 확인)", "https://doi.org/10.1007/s11011-024-01397-6", PM, A),
 ("hypo", "The hypoglycemic metabolites and potential mechanisms of Lilium (lily) — Front Pharmacol 2026 (PMID 42338973, PMC13283800, 전문 확인; 비교한 네 백합 가운데 var. viridulum 포함, 받아온 전문에서 종명이 빠져 가장 강한 종은 판단하지 않음)", "https://doi.org/10.3389/fphar.2026.1806579", PM, A),
 ("sulfur", "[Effect of sulfur fumigation on quality and safety of Lilii Bulbus] — Zhongguo Zhong Yao Za Zhi 2023 (PMID 36872229, 초록만 확인, 시료 기원 종 미확인)", "https://doi.org/10.19540/j.cnki.cjcmm.20221031.301", PM, A),
 ("zhimu", "Chemical interaction between Lilium brownii and Rhizoma Anemarrhenae, the herbal constituents of Baihe Zhimu decoction, by LC-QqQ-LIT-MS — Biomed Chromatogr 2017 (PMID 29027684, 초록만 확인)", "https://doi.org/10.1002/bmc.4118", PM, A),
 ("rsd", "Reductive soil disinfestation by mixing carbon nanotubes and mushroom residues to mitigate the continuous cropping obstacles for Lilium brownii — Crop Health 2024 (PMID 41649639, PMC12825970, 초록 확인)", "https://doi.org/10.1007/s44297-024-00023-2", PM, A),
 ("efsa", "EFSA Compendium of botanicals — card.json 의 EU_EFSA_COMPENDIUM 표시만 근거, 이 종의 항목 원문은 네트워크 허용 목록 밖이라 미열람", "https://www.efsa.europa.eu/en/data/compendium-botanicals", "European Food Safety Authority", A),
]
N = {k: i + 1 for i, (k, *_) in enumerate(S)}
def r(text):
    return re.sub(r"\{(\w+(?:,\s*\w+)*)\}", lambda m: "[" + ", ".join(str(N[x.strip()]) for x in m.group(1).split(",")) + "]", text)

sec = [
("overview", "한눈에 보기", """홍콩백합(Lilium brownii)은 백합과 백합속의 여러해살이 알뿌리 식물로, 흰 비늘잎이 겹겹이 모인 비늘줄기를 음식과 약으로 쓴다{review}. 식약처 「식품원료 목록」에는 '홍콩백합꽃잎'과 '홍콩백합비늘줄기' 두 행이 있고, 학명은 Lilium brownii F.Br. ex Miellez(함께 적힌 이름 Lilium austale Stapf, Lilium brownii var. australe), 별명은 당나리·당개나리다{mfds}. 두 행 모두 식품에 쓸 수 있는 원료(사용가능, 식품원료 A코드)이고 사용 조건은 '사용가능부위 : 비늘줄기, 꽃잎'이다{mfds}. 같은 목록의 '백합' 행들(백합가루·백합추출액·백합꽃잎·백합비늘줄기·백합뿌리)은 참나리·백합(百合, L. brownii var. viridulum)·큰솔나리를 함께 기원으로 적어, 이 종의 변종이 '백합' 원료에도 들어간다{mfds}. 이 종을 원재료로 하는 건강기능식품 고시형 원료는 확인하지 못함.

중국 약전은 참나리(L. lancifolium), L. brownii var. viridulum, 큰솔나리(L. pumilum)의 비늘줄기를 약재 백합(百合, Lilii Bulbus)의 기원으로 정한다{review}. 비늘줄기에는 다당류·스테로이드 사포닌·페닐프로파노이드(레갈로사이드 등)·플라보노이드가 주요 성분으로 정리된다{review}. 효능 근거는 대부분 세포·동물 실험이며, 이 종만으로 한 사람 시험은 확인하지 못함."""),
("history", "역사", """중국에서 백합 비늘줄기는 한나라 때부터 음식이자 약으로 기록되었고, 음(陰)을 기르고 폐를 적시며 마음을 안정시키는 데 쓰였다{review}. 2025년 리뷰는 『신농본초경』이 var. viridulum의 비늘줄기를 복통을 덜고 대소변을 잘 통하게 하며 마음을 가라앉힌다고 적었다고 소개한다{review}. 같은 리뷰는 독성 절에서 이 책이 L. brownii와 var. viridulum을 독 없는 상품(上品)으로 올렸다고 쓰고, 다른 절에서는 중품(中品)으로 적어 서술이 엇갈린다{review}. 옛날에는 여러 백합속 종이 섞여 쓰였으나 명나라 무렵에는 L. brownii와 var. viridulum이 정통 기원으로 자리 잡았고, 후베이 징저우·간쑤 청현·안후이 추저우·산둥 허쩌가 산지로 꼽혔다{review}. 본초 문헌 고증 연구도 var. viridulum을 정통 약용 백합으로 보고, 참나리(권단)는 일부 의서에서 잘못 쓰였으며 산단(L. pumilum)은 효능이 다르다고 결론지었다{herbal}. 장중경의 『금궤요략』에 나오는 백합지황탕과 백합지모탕이 대표 처방이다{review}. 한국에서 이 종을 먹어 온 역사 기록은 확인하지 못함."""),
("biology", "식물학적 특징", """홍콩백합은 백합과 백합속의 여러해살이 알뿌리 식물이며, 비늘줄기는 수십 장의 흰 비늘잎이 연꽃처럼 겹쳐 있다{review}. 학명 L. brownii 아래 변종 var. viridulum Baker가 있으며, 중국에서는 '룽야백합(Longya lily)'이라 부른다{auto}. var. viridulum은 북아시아와 동아시아에 널리 분포한다고 보고되었다{cp}. 중국 광둥성에는 이 종의 자연 집단이 있어 유전 다양성과 집단 구조가 연구되었다{gd}. 비늘줄기의 주된 저장 물질은 녹말이며, var. viridulum 비늘줄기 녹말은 B형 결정 구조를 보였다{starch}. 비늘줄기에는 다당류가 신선중량 100 g당 2.0–5.0 g, 스테로이드 사포닌이 0.1–0.3 g 들어 있다고 리뷰가 정리했으나, 이는 여러 백합을 묶은 값이다{review}. 식약처 목록은 꽃잎도 먹을 수 있는 부위로 두지만, 이 종의 꽃잎 성분을 정량한 논문은 PubMed에서 찾지 못해 확인하지 못함. 꽃의 모양·색, 꽃 피는 시기 같은 형태 정보는 식물지 원문을 열지 못해 확인하지 못함."""),
("related_species", "이름과 가까운 종", """식약처 목록에는 이 종 말고도 백합속 식품원료가 여럿 있다{mfds}. 중나리(L. leichtlinii var. maximowiczii), 섬말나리(L. hansonii), 야마유리(L. auratum), 땅나리(L. callosum), 말나리(L. distichum), 하늘말나리(L. tsingtauense)는 각각 다른 행이며, 야마유리는 뿌리, 섬말나리는 비늘줄기와 어린잎처럼 쓸 수 있는 부위도 다르다{mfds}. '백합' 행은 참나리·백합(L. brownii var. viridulum)·큰솔나리를 한데 묶어 적었으므로, 제품의 '백합'이 어느 종인지는 원료 표시로 따로 확인해야 한다{mfds}. 개별인정형 건강기능식품 원료 '참나리추출분말'은 참나리(L. lancifolium) 비늘줄기가 원료로, 이 종과 다르다{mfds}. 중국 시장에는 참나리, 란저우백합(L. davidii var. unicolor), 룽야백합(L. brownii var. viridulum) 세 가지가 주로 유통되며, 근적외선 분광으로 94.37% 정확도로 구별되었다{nir}. 쓴맛 성분인 레갈로사이드 A·B는 참나리가 이 종보다 각각 약 2–7배, 4–16배 많았고, 레갈로사이드 C·E는 이 종에서 검출되지 않았다{bitter}. 두 종을 2차원 액체크로마토그래피-고분해능 질량분석으로 비교해 모두 331개 성분을 확인했고 페닐프로파노이드 유도체와 스테로이드 사포닌이 가장 많았다{lc2d}. 식약처 목록에서 '백합'은 조개(Meretrix lusoria)의 이름이기도 하다{mfds}."""),
("cultivation", "재배와 산지", """룽야백합(var. viridulum) 연구 시료는 주로 중국 후난성에서 왔으며, 다당 비교 연구는 후난성 룽후이현, 콜히친 연구의 'Longya' 시료는 후난성 헝둥현에서 채집했다{poly, colch}. 같은 밭에 이어짓기를 하면 식물체에서 나온 2,4-다이-tert-부틸페놀(2,4-DTBP)이 자가독성을 일으키는 것이 확인되었다{auto}. 이어짓기 밭 흙에서 이 물질을 분해하는 세균 두 균주가 분리되어 현장 시험까지 진행되었다{dtbp}. 버섯 배지 잔재와 탄소나노튜브를 섞어 흙을 환원 소독하는 방법도 이어짓기 피해를 줄이려고 시험되었다{rsd}. 룽야백합은 푸사리움 곰팡이병에 약하고, 비늘줄기 썩음병 연구에서는 페닐프로파노이드 생합성 경로가 저항성에 중요하다고 보았다{regen, rot}. 중국 저장성 리수이시의 L. brownii에서는 사과줄기홈바이러스(ASGV)가 처음 보고되었다{asgv}. 개체 선발로 얻은 새 계통 '쉐펑(Xuefeng)'은 전통 계통 '룽야'보다 플라보노이드 85종과 배당체가 많았다{flav, glyc}. 국내 농작물생산조사·특용작물 생산실적에서 이 종의 재배 통계는 확인하지 못함."""),
("processing", "가공과 이용", """백합 비늘줄기는 찌거나 삶아 먹고, 가루·술·기능성 음료로 가공하며, 연자죽이나 흰목이탕 같은 음식에도 넣는다{review}. 식약처 목록에도 '백합가루'·'백합추출액'처럼 가공 형태의 원료가 올라 있다{mfds}. var. viridulum 다당 추출에서 아임계수(150 °C, 10분) 수율은 54.91%로 초음파 추출(3.69%)보다 훨씬 높았고, 아임계수 다당의 포도당 비율은 91.67%였다{poly}. 정제 다당 가운데 분자량 12.0 kDa 만노글루칸(LLP11)은 모의 소화 효소에 분해되지 않고 장내세균의 아세트산 생산에 쓰였다{llp11}. 312 kDa 글루코만난(LBP)은 대식세포의 면역 관련 유전자 발현을 높였다{gm}. 녹말은 수분 25%에서 수분-열처리하면 조리 후 저항전분이 44.15%로 가장 높았다{starch}. 백합지모탕처럼 지모와 함께 달이면 백합 쪽 페놀 배당체의 추출이 억제되었다{zhimu}. 쥐 불면 모델에서는 백합(L. brownii) 7일 투여가 세로토닌·멜라토닌 수치와 장내세균을 회복시켰다{insom}. 파킨슨병 생쥐 모델에서는 에탄올·물 추출물 모두 운동 기능을 개선했다{pd}."""),
("genetics", "유전 정보", """var. viridulum의 엽록체 유전체는 152,665 bp이며, 역반복 영역(합계 53,052 bp)·대단일복사 영역 82,085 bp·소단일복사 영역 17,528 bp로 이루어지고 유전자 131개(tRNA 38, rRNA 8, 단백질 암호 85)가 예측되었다{cp}. 광둥성 자연 집단의 유전 다양성 연구는 초록이 없어 수치는 확인하지 못함. 2,4-DTBP 처리 룽야백합의 전사체 분석에서 유전자 단편(unigene) 188,505개가 얻어졌다{auto}. '쉐펑'과 '룽야' 비교에서는 플라보노이드 합성 효소 유전자 59개가 쉐펑에서 더 많이 발현되었고, MYB 1개와 bHLH 4개 전사인자가 안토시아닌 합성과 연결되었다{flav}. 대사체·전사체 비교에서 이 종은 식용 전용 대조 백합보다 스테로이드 사포닌과 스테로이드 알칼로이드가 많았고, 관련 CYP450 유전자 발현도 높았다{func}. 룽야백합의 배발생 캘러스 재생·형질전환 체계가 확립되어 형질전환율 65.56%를 얻었다{regen}."""),
("safety", "안전성", """식약처 목록에서 홍콩백합 비늘줄기·꽃잎은 사용가능 원료이며{mfds}, 건강기능식품 고시형 원료가 아니어서 고시 섭취 시 주의사항은 확인하지 못함. 중국 약전의 말린 백합 하루 용량은 6–12 g이고, 리뷰는 이 범위에서 사람의 급성 독성 기록이나 중독 사례를 찾지 못했다고 정리하면서 장기 독성 자료는 부족하다고 했다{review}. 백합의 쓴맛을 콜히친 탓으로 보는 주장이 있었으나, 2026년 고분해능 LC-MS 연구는 'Longya' 등 5개 품종의 비늘줄기·뿌리·줄기·꽃·잎에서 콜히친과 생합성 전구체 15종을 모두 검출하지 못했다{colch}. 같은 연구는 쓴맛이 비늘줄기 겉껍질에 몰려 있고 스테로이드 알칼로이드 배당체와 사포닌이 쓴맛을 낸다고 보았다{colch}. 시중 백합 약재에서 유황 훈증이 흔한 문제로 보고되었으나 시료 기원 종은 확인하지 못함{sulfur}.

고양이 백합 중독은 사람 식품 안전과 별개다{catrev}. 백합속 식물은 고양이에게 신장 독성이 있어 잎 2장이나 꽃 일부로도 죽을 수 있고, 꽃잎·수술·잎·꽃가루 모두 위험하다{catrev}. 이스터백합(L. longiflorum)의 수용성 추출물은 고양이에게 신장 세뇨관 괴사를 일으켰다{easter}. 카드 자료에는 이 종이 유럽식품안전청(EFSA) 식물 목록(Compendium of botanicals)에 있다고 표시되어 있으나 해당 항목 원문은 확인하지 못함{efsa}. 홍콩백합 자체의 고양이 독성 시험과 국내 공공기관의 알레르기·잔류농약 정보는 확인하지 못함."""),
]
sections = [{"key": k, "title": t, "body": r(b)} for k, t, b in sec]

def C(name, ko, cls, role, part, content, act, src):
    return {"name": name, "name_ko": ko, "class": cls, "role": role, "part": part, "content_text": r(content), "activity_ko": r(act), "source": [N[s] for s in src]}
compounds = [
 C("Regaloside A", "레갈로사이드 A", "페닐프로파노이드 글리세롤 배당체", "marker", "비늘줄기(var. viridulum)", "참나리가 이 종보다 약 2–7배 많음(LC-MS 정량, 초록)[{0}]".format(N["bitter"]), "표준품 시험에서 고혈당 생쥐 혈당 저하, α-글루코시데이스 억제{hypo}", ["bitter", "hypo"]),
 C("Regaloside B", "레갈로사이드 B", "페닐프로파노이드 글리세롤 배당체", "marker", "비늘줄기(var. viridulum)", "참나리가 이 종보다 약 4–16배 많음(초록); 레갈로사이드 C·E는 이 종에서 불검출{bitter}", "표준품 시험에서 고혈당 생쥐 혈당 27.87→14.11 mmol/L{hypo}", ["bitter", "hypo"]),
 C("1-O-feruloyl-2-O-p-coumaroylglycerol", "1-O-페룰로일-2-O-p-쿠마로일글리세롤", "페닐프로페노이드 아실글리세롤", "bioactive", "비늘줄기(var. viridulum)", "클로로포름 분획에서 분리(함량 미기재){antiinf}", "LPS 자극 대식세포 NO 생성 억제 IC50 9.12 μM{antiinf}", ["antiinf"]),
 C("1,3-O-diferuloylglycerol", "1,3-O-다이페룰로일글리세롤", "페닐프로페노이드 아실글리세롤", "bioactive", "비늘줄기(var. viridulum)", "클로로포름 분획에서 분리(함량 미기재){antiinf}", "NO 생성 억제 IC50 12.01 μM, NF-κB·MAPK 경로 억제{antiinf}", ["antiinf"]),
 C("1-O-p-coumaroyl-3-O-feruloylglycerol", "1-O-p-쿠마로일-3-O-페룰로일글리세롤", "페놀산 글리세라이드 이량체", "bioactive", "L. brownii(부위는 초록에 비늘줄기로 명시 안 됨)", "분리 성분(함량 미기재){cf}", "파킨슨병 세포·생쥐 모델에서 신경 보호(p62-Keap1-Nrf2){cf}", ["cf"]),
 C("3-O-acetyl-1-O-caffeoylglycerol", "3-O-아세틸-1-O-카페오일글리세롤", "페닐프로파노이드", "bioactive", "비늘줄기", "새 화합물로 분리(함량 미기재){mao}", "50 μg/mL에서 모노아민산화효소 20.96% 억제{mao}", ["mao"]),
 C("26-O-beta-D-glucopyranosylnuatigenin", "26-O-글루코실누아티게닌", "스테로이드 사포닌(푸로스타놀계)", "bioactive", "비늘줄기(var. viridulum)", "새 스테로이드 사포닌 7종 가운데 하나로 분리(함량 미기재){sap}", "구조 동정 연구로 활성은 초록에 없음{sap}", ["sap"]),
 C("(22R,25R)-5alpha-spirosolan-3beta-ol 3-O-rhamnosyl-glucosyl-glucoside", "아이소스피로스타놀형 배당체(화합물 2)", "스테로이드 배당체", "bioactive", "비늘줄기", "새 화합물로 분리(함량 미기재){iso}", "간암세포 SMMC-7721·HepG2 증식 억제 IC50 26.3·30.9 μM{iso}", ["iso"]),
 C("Glucomannan", "글루코만난(LBP)", "다당류", "bioactive", "작은 비늘줄기(var. viridulum)", "분자량 312 kDa, 만노스:포도당 몰비 0.582:0.418{gm}", "5 μg/mL에서 대식세포 TNF-α·IL-6 등 발현 증가{gm}", ["gm"]),
 C("Mannoglucan", "만노글루칸(LLP11)", "다당류", "bioactive", "비늘줄기(var. viridulum)", "분자량 12.0 kDa, α-1,4-포도당·β-1,4-만노스 주사슬{llp11}", "모의 소화에서 분해되지 않고 장내세균 발효로 아세트산 생성{llp11}", ["llp11"]),
 C("Lily polysaccharide", "백합 다당(LBVP)", "다당류", "nutrient", "비늘줄기(var. viridulum)", "건조 분말 기준 수율 아임계수 54.91%, 초음파 3.69%; 아임계수 다당 포도당 91.67%{poly}", "추출법이 종보다 다당 성질에 더 큰 영향{poly}", ["poly"]),
 C("Pectin", "펙틴 다당(WLBP-A3-c)", "펙틴 다당류", "bioactive", "L. brownii", "59 kDa, HG:RG-I:RG-II 질량비 76.0:17.2:6.8{pectin}", "시험관 항산화(같은 연구의 둥굴레 펙틴보다 약함){pectin}", ["pectin"]),
 C("Starch", "녹말", "탄수화물", "nutrient", "비늘줄기(var. viridulum)", "수분-열처리(수분 25%) 후 조리 시료 저항전분 44.15%{starch}", "주된 저장 물질; B형 결정 구조{starch}", ["starch"]),
 C("2,4,6-trichloro-3-methyl-5-methoxyphenol 1-O-gentiobioside", "염소화 페닐 배당체(새 화합물 1)", "클로로페닐 배당체", "bioactive", "비늘줄기(var. viridulum)", "드문 새 클로로페닐 배당체 2종 가운데 하나로 분리(함량 미기재){chloro}", "LPS 자극 대식세포 NO 생성 억제는 약함{chloro}", ["chloro"]),
 C("Colchicine", "콜히친", "알칼로이드", "bioactive", "비늘줄기·뿌리·줄기·꽃·잎", "'Longya' 등 5개 품종 모든 조직에서 불검출(HPLC-Q-TOF-MS){colch}", "과거 쓴맛·독성 원인으로 거론되었으나 이 연구는 존재를 부정{colch}", ["colch"]),
]

assays = [
 {"role": "literature", "compound": "Lily polysaccharide (monosaccharide composition)", "compound_ko": "백합 다당(LBVP) 수율·단당 조성·분자량",
  "part": "비늘줄기(var. viridulum, 후난성 룽후이현 신선 비늘줄기를 건조 분말로)",
  "content": r("수율 아임계수 54.91 ± 0.63%, 초음파 3.69 ± 0.69%; 분자량 333 kDa·53 kDa; 아임계수 다당 포도당 91.67%, 초음파 다당 포도당 42.41–45.16%·만노스 51.85–55.50%(세 종 범위){poly}"),
  "method": "중량법 수율 + HPAEC-PAD(단당) + GPC(분자량)",
  "conditions": {"instrument": "Thermo ICS5000 이온크로마토그래프(HPAEC-PAD); GPC는 Agilent 1260", "column": "CarboPac PA-20 (3 × 150 mm); GPC: Waters Ultrahydrogel 120·250·500 (7.8 × 300 mm, 3개 직렬)",
   "mobile_phase": "A: 탈이온수, B: 0.1 M NaOH, C: 0.1 M NaOH + 0.2 M NaAc", "gradient": "A/B/C(%): 0분 95/5/0 → 26분 85/5/10 → 42분 85/5/10 → 42.1분 60/0/40 → 52분 60/40/0 → 52.1분 95/5/0 → 60분 95/5/0",
   "flow": "0.5 mL/min(HPAEC); 1 mL/min(GPC)", "temp": "GPC 30 °C(HPAEC 칼럼 온도 미기재)", "detection": "펄스 전류 검출기(PAD)", "injection": "5 μL(HPAEC); 40 μL, 1 mg/mL(GPC)",
   "sample_prep": "아임계수: 건조 분말:물 1:15, 150 °C 10분 → 6,000 rpm 10분 원심, 무수에탄올 침전 4 °C 12시간, 동결건조; 초음파: 1:20, 65 °C 20분; 단당 분석은 다당 5 mg을 2 M TFA 121 °C 2시간 가수분해",
   "standard": "단당 13종 표준품(Sigma); 분자량은 PEG 표준(1,960–326,000)", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": r("다당은 백합의 주요 활성·영양 성분으로, 세 식용 백합과 두 추출법을 같은 조건에서 비교함; 전문 확인, 검량·검출한계·회수율은 원문에 없음{poly}."),
  "source": [N["poly"]], "url": "https://doi.org/10.3389/fnut.2022.998942", "source_kind": "paper"},
 {"role": "literature", "compound": "Regaloside A", "compound_ko": "레갈로사이드 A·B(C·E 포함 비교)", "part": "비늘줄기(var. viridulum, 참나리와 비교)",
  "content": r("참나리가 이 종보다 레갈로사이드 A 약 2–7배, B 약 4–16배 많음; C·E는 이 종에서 불검출{bitter}"),
  "method": "LC-MS 대사체 정량(초록 기준, 세부 확인 못함)",
  "conditions": {k: "" for k in ["instrument", "column", "mobile_phase", "gradient", "flow", "temp", "detection", "injection", "sample_prep", "standard", "linearity", "lod", "loq", "recovery"]},
  "rationale": r("쓴맛과 관련된 페닐프로파노이드 글리세롤 배당체로 종 간 품질 일관성 평가에 쓰자고 제안됨; 초록만 확인, 전문 확인 못함{bitter}."),
  "source": [N["bitter"]], "url": "https://doi.org/10.1016/j.jpba.2022.114778", "source_kind": "paper"},
 {"role": "literature", "compound": "Colchicine", "compound_ko": "콜히친(생합성 전구체 15종 포함 표적 선별)", "part": "비늘줄기·뿌리·줄기·꽃·잎('Longya' 등 5개 품종, 'Longya'는 후난성 헝둥현 채집)",
  "content": r("모든 조직에서 콜히친·전구체 불검출(양성대조 2종에서는 검출){colch}"),
  "method": "UHPLC-Q-TOF-MS(ESI 양이온)",
  "conditions": {"instrument": "Agilent 1290 Infinity II UHPLC + Agilent 6530 Q-TOF", "column": "XAqua-C18, 150 × 2.1 mm, 2.8 μm", "mobile_phase": "A: 0.1% 포름산 수용액, B: 0.1% 포름산 아세토니트릴",
   "gradient": "0–15분 5–25% B; 15–27분 25–38% B; 27–35분 38–90% B", "flow": "0.3 mL/min", "temp": "30 °C",
   "detection": "ESI 양이온, m/z 100–1000, 콜히친 [M+H]+ m/z 400.1755; 가스 350 °C, 건조가스 12 L/min, 분무가스 10 L/min, 모세관 4000 V, fragmentor 135 V, skimmer 65 V, 충돌에너지 10·20·30 V, 기준 이온 m/z 112.9855·966.0007",
   "injection": "1 μL", "sample_prep": "-80 °C 보관 조직을 48시간 동결건조·분쇄, 0.1000 g + 70% 에탄올 10 mL 초음파 1시간, 0.22 μm 여과", "standard": "콜히친 표준품(시판)", "linearity": "", "lod": "", "loq": "", "recovery": "첨가 회수 시험은 하지 않았다고 원문에 명시"},
  "rationale": r("백합의 쓴맛·독성 원인으로 오래 거론된 성분이라 존재 여부를 검증함; 전문 확인, 받아온 전문에서 'Longya'의 학명 표기가 빠져 있어 var. viridulum 여부는 다른 문헌의 룽야백합 명칭으로 판단{colch, auto}."),
  "source": [N["colch"], N["auto"]], "url": "https://doi.org/10.3390/molecules31040721", "source_kind": "paper"},
]

d = {"slug": "lilium-brownii", "name_ko": "홍콩백합", "name_en": "Brown's lily (Hong Kong lily)",
 "scientific_name": "Lilium brownii F.E.Br. ex Miellez",
 "aliases": ["홍콩백합꽃잎", "홍콩백합비늘줄기", "당나리", "당개나리", "Lilium austale", "Lilium brownii var. australe", "Lilium brownii var. viridulum", "룽야백합", "Longya lily", "백합(百合)", "Lilii Bulbus"],
 "sections": sections, "compounds": compounds, "markers": [], "nutrients": [], "assays": assays,
 "production": [], "world": [], "gi": [], "orgs": [],
 "sources": [{"n": i + 1, "title": t, "url": u, "publisher": p, "accessed": a} for i, (k, t, u, p, a) in enumerate(S)]}
# EFSA mention: add sentence ref
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in sections: print(s["key"], len(s["body"]))
