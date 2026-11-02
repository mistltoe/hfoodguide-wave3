import json, pathlib
H = pathlib.Path(__file__).resolve().parents[1]
A = "2026-11-02"
def pm(n, title, pmid, pub, pmc=None):
    url = f"https://pmc.ncbi.nlm.nih.gov/articles/{pmc}/" if pmc else f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
    return {"n": n, "title": title, "url": url, "publisher": pub, "accessed": A}
S = [
 {"n":1,"title":"식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 측백나무잎·측백나무잎추출물(Thuja orientalis L. / Biota orientalis L., 제한적사용, '제한적사용가능부위 : 잎※(측백엽)') 행","url":"https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020","publisher":"식품의약품안전처","accessed":"2026-10-13"},
 {"n":2,"title":"식품의약품안전처 「식품의 기준 및 규격」 제2. 1. 2) 식품원료 판단기준 — '식품에 제한적으로 사용할 수 있는 원료'(별표 2)와 기본 사용기준(가공 전 원료 중량의 50% 미만). ※ 원문 페이지는 이 환경에서 열지 못했고 WebSearch 요약으로만 확인함","url":"https://www.foodsafetykorea.go.kr/popup/safefoodlife/food/foodRvlv/foodRvlvDetail.do?rvlv_no=9","publisher":"식품의약품안전처(식품안전나라)","accessed":A},
 pm(3,"Platycladus orientalis leaves: a systemic review on botany, phytochemistry and pharmacology. Am J Chin Med 2014;42(3):523-42 (doi:10.1142/S0192415X14500347) — 초록","24871649","Am J Chin Med (PubMed)"),
 pm(4,"Chemometrics of the composition and antioxidant capacity of essential oils obtained from six Cupressaceae taxa. Sci Rep 2024;14:18612 (PMID 39127791, doi:10.1038/s41598-024-69600-3)","39127791","Scientific Reports (PMC)","PMC11316816"),
 pm(5,"Seasonal dynamics of the phenolic constituents of the cones and leaves of oriental Thuja (Platycladus orientalis L.) reveal their anti-inflammatory biomarkers. RSC Adv 2021;11 (PMID 35481004, doi:10.1039/d1ra01681d)","35481004","RSC Advances (PMC)","PMC9036908"),
 pm(6,"Chemical Fingerprint and Quantitative Analysis for the Quality Evaluation of Platycladi cacumen by Ultra-performance Liquid Chromatography Coupled with Hierarchical Cluster Analysis. J Chromatogr Sci 2018;56(1):41-48 (doi:10.1093/chromsci/bmx079) — 초록","28977346","J Chromatogr Sci (PubMed)"),
 pm(7,"Quality evaluation of Platycladus orientalis (L.) Franco through simultaneous determination of four bioactive flavonoids by high-performance liquid chromatography. J Pharm Biomed Anal 2006;41(4):1186-90 (doi:10.1016/j.jpba.2006.02.054) — 초록","16621407","J Pharm Biomed Anal (PubMed)"),
 pm(8,"Authentication of Platycladus Orientalis Leaves and Its Five Adulterants by Combination of Morphology and Microscopic Characteristics, TLC, and HPLC Analysis. J AOAC Int 2023 (doi:10.1093/jaoacint/qsad066) — 초록","37243686","J AOAC Int (PubMed)"),
 pm(9,"Chemotaxonomic Variation in Volatile Component Contents in Ancient Platycladus orientalis Leaves with Different Tree Ages in Huangdi Mausoleum. Molecules 2023;28(5):2043 (PMID 36903288, doi:10.3390/molecules28052043)","36903288","Molecules (PMC)","PMC10003951"),
 pm(10,"Volatile constituents of the fruit and leaf oils of Thuja orientalis L. grown in Iran. Z Naturforsch C 2003;58(3-4):171-2 (doi:10.1515/znc-2003-3-404) — 초록","12710722","Z Naturforsch C (PubMed)"),
 pm(11,"Chemical composition and fungitoxic activity of essential oil of Thuja orientalis L. grown in the north-western Himalaya. Z Naturforsch C 2008;63(3-4):211-4 (doi:10.1515/znc-2008-3-409) — 초록","18533464","Z Naturforsch C (PubMed)"),
 pm(12,"Reporting effective extraction methodology and chemical characterization of bioactive components of under explored Platycladus orientalis (L.) Franco from semi-arid climate. Nat Prod Res 2019;33(9):1237-1242 (doi:10.1080/14786419.2018.1519707) — 초록","30394107","Nat Prod Res (PubMed)"),
 pm(13,"GC analysis of essential oils in the rumen fluid after incubation of Thuja orientalis twigs in the Rusitec system. Res Vet Sci 2004;76(1):77-82 (doi:10.1016/j.rvsc.2003.07.001) — 초록","14659733","Res Vet Sci (PubMed)"),
 pm(14,"Molluscicidal activity of Saraca asoca and Thuja orientalis against the fresh water snail Lymnaea acuminata. Vet Parasitol 2009;164(2-4):206-10 (doi:10.1016/j.vetpar.2009.05.008) — 초록","19501966","Vet Parasitol (PubMed)"),
 pm(15,"Thujone and thujone-containing herbal medicinal and botanical products: toxicological assessment. Regul Toxicol Pharmacol 2013;65(1):100-7 (doi:10.1016/j.yrtph.2012.11.002) — 초록","23201408","Regul Toxicol Pharmacol (PubMed)"),
 pm(16,"Determination of the biologically active flavour substances thujone and camphor in foods and medicines containing sage (Salvia officinalis L.). Chem Cent J 2011;5:44 (doi:10.1186/1752-153X-5-44) — 초록","21777420","Chem Cent J (PubMed)"),
 pm(17,"Identification and characterization of GABA(A) receptor modulatory diterpenes from Biota orientalis that decrease locomotor activity in mice. J Nat Prod 2011;74(8):1764-72 (doi:10.1021/np200317p) — 초록","21793559","J Nat Prod (PubMed)"),
 pm(18,"The anti-inflammatory activities of an extract and compounds isolated from Platycladus orientalis (Linnaeus) Franco in vitro and ex vivo. J Ethnopharmacol 2011;141(2):647-52 (doi:10.1016/j.jep.2011.05.019) — 초록","21619922","J Ethnopharmacol (PubMed)"),
 pm(19,"Genome-Wide Variant Identification and High-Density Genetic Map Construction Using RADseq for Platycladus orientalis (Cupressaceae). G3 2019;9(11):3663-3672 (doi:10.1534/g3.119.400684) — 초록","31506321","G3 (PubMed)"),
 pm(20,"A chromosome-level genome assembly of Platycladus orientalis and comparative genomics reveal pivotal roles of transposable elements in gene duplication and pseudogenization across gymnosperm giga-genomes. Plant Commun 2026;7(8):101814 (doi:10.1016/j.xplc.2026.101814) — 초록","41808406","Plant Communications (PubMed)"),
 pm(21,"Exploring the Phylogeography of Ancient Platycladus orientalis in China by Specific-Locus Amplified Fragment Sequencing. Int J Mol Sci 2019;20(16):3871 (doi:10.3390/ijms20163871) — 초록","31398898","Int J Mol Sci (PubMed)"),
 pm(22,"Selection of reference genes for quantitative gene expression studies in Platycladus orientalis (Cupressaceae) Using real-time PCR. PLoS One 2012;7(3):e33278 (doi:10.1371/journal.pone.0033278) — 초록","22479379","PLoS One (PubMed)"),
 pm(23,"Dynamic changes of endogenous hormones and transcriptome analysis reveal the regulatory mechanism of gibberellin-promoted male cone formation in Platycladus orientalis. BMC Plant Biol 2026;26 (doi:10.1186/s12870-026-08706-4) — 초록","41963813","BMC Plant Biol (PubMed)"),
 pm(24,"An epidemiological survey of Cupressaceae pollenosis in Italy. J Investig Allergol Clin Immunol 2002;12(4):287-92 — 초록","12940232","J Investig Allergol Clin Immunol (PubMed)"),
 pm(25,"[Relationship between full flowering stages of anemophilous and ligneous plants and consultation rate of allergic rhinitis]. Lin Chuang Er Bi Yan Hou Tou Jing Wai Ke Za Zhi 2016;30(15):1206-1209 (doi:10.13201/j.issn.1001-1781.2016.15.007) — 초록","29798330","J Clin Otorhinolaryngol (PubMed)"),
 pm(26,"Platycladus orientalis Leaf Extract Promotes Hair Growth via Non-Receptor Tyrosine Kinase ACK1 Activation. Curr Issues Mol Biol 2024;46(10):11207-11219 (PMID 39451545, doi:10.3390/cimb46100665)","39451545","Curr Issues Mol Biol (PMC)","PMC11505925"),
 pm(27,"In vivo and in vitro evaluation of hair growth potential of Cacumen Platycladi, and GC-MS analysis of the active constituents of volatile oil. J Ethnopharmacol 2019;238:111835 (doi:10.1016/j.jep.2019.111835) — 초록","30917929","J Ethnopharmacol (PubMed)"),
 pm(28,"Simultaneous Determination of Quercitrin, Afzelin, Amentoflavone, Hinokiflavone in Rat Plasma by UFLC-MS-MS and Its Application to the Pharmacokinetics of Platycladus orientalis Leaves Extract. J Chromatogr Sci 2018;56(10):895-902 (doi:10.1093/chromsci/bmy066) — 초록","29982351","J Chromatogr Sci (PubMed)"),
 pm(29,"Effects of extraction solvents on the recovery of bioactive compounds from Platycladus orientalis Leaves of different tree ages: a comparative metabolomics approach. BMC Plant Biol 2026;26 (doi:10.1186/s12870-026-09199-x) — 초록","42271254","BMC Plant Biol (PubMed)"),
 pm(30,"[Protective effect of different solvent extracts from platycladi cacumen carbonisatum on LPS-induced human umbilical vein endothelial cells damage]. Zhongguo Zhong Yao Za Zhi 2013;38(22):3933-8 — 초록","24558879","China J Chin Mater Med (PubMed)"),
 pm(31,"The Biota orientalis oil extract Epiitalis is efficacious at reducing the symptoms of knee osteoarthritis: a pilot, multi-site, dose-ranging, randomized, blinded, placebo-controlled trial. Inflammopharmacology 2022 (doi:10.1007/s10787-022-01013-y) — 초록","35732989","Inflammopharmacology (PubMed)"),
 pm(32,"Assessment of the Microbiome and Potential Aflatoxin Associated With the Medicinal Herb Platycladus orientalis. Front Microbiol 2020 (doi:10.3389/fmicb.2020.582679) — 초록","33193220","Front Microbiol (PubMed)"),
 pm(33,"Purification, Characterization, and Bioactivities of Polyphenols from Platycladus orientalis (L.) Franco. J Food Sci 2019;84(3):667-677 (doi:10.1111/1750-3841.14483) — 초록","30779137","J Food Sci (PubMed)"),
 pm(34,"Characterization of the complete chloroplast genome of Platycladus orientalis (Cupressaceae), an herb to treat lumbar tuberculosis in China. Mitochondrial DNA B Resour 2019;5(1):222-223 (doi:10.1080/23802359.2019.1699471) — 초록","33366496","Mitochondrial DNA B Resour (PubMed)"),
 {"n":35,"title":"대구 동구, 천연기념물 도동 측백나무 숲… 보존과 재난안전기원제 개최(언론 보도, 2023). ※ 국가유산청 원문은 확인하지 못했고 WebSearch 요약으로만 확인함","url":"https://www.ajunews.com/view/20230319172651195","publisher":"아주경제","accessed":A},
]

secs = [
("overview","한눈에 보기",
"측백나무(Thuja orientalis L.)는 측백나무과(Cupressaceae)의 늘푸른 바늘잎나무로, 지금은 Platycladus orientalis (L.) Franco라는 학명으로 더 많이 쓰고 Biota orientalis라는 이명도 있다[1, 5]. 중국에서 측백나무속(Platycladus)은 이 한 종뿐이며, 중국 북부의 생태적으로 중요한 자생 침엽수이자 세계 여러 곳에 옮겨 심은 나무다[4, 19].\n\n"
"식품의약품안전처 「식품원료 목록」에는 '측백나무잎'과 '측백나무잎추출물'이라는 원료명으로 올라 있고, 이명으로 '측백엽', 영문명으로 Chinese arbor vitae가 적혀 있다[1]. 이 목록에서 측백나무는 '제한적사용' 원료이며 사용 조건은 '제한적사용가능부위 : 잎※(측백엽)'으로, 잎만 식품에 쓸 수 있다[1]. 식품공전의 '식품에 제한적으로 사용할 수 있는 원료'는 정해진 조건 안에서만 쓰는 원료이고, 별도 조건이 없으면 가공 전 원료 중량의 50% 미만으로 쓴다는 기준이 있으나 이 내용은 원문이 아닌 검색 요약으로만 확인했다[2].\n\n"
"잎에는 퀘르시트린·히페로사이드 같은 플라보노이드 배당체와 히노키플라본·쿠프레수플라본 같은 바이플라보노이드가 들어 있다[5]. 잎 정유의 주성분은 α-피넨·δ-3-카렌·세드롤이다[4, 10, 11]. 건강기능식품 고시형 원료나 개별인정형 원료로서의 지표성분 기준은 확인하지 못함."),
("history","역사와 전통 이용",
"측백나무 잎은 중국에서 수천 년 동안 '측백엽(Cebaiye)'이라는 약재로 쓰였고, 한의학 이론에서는 피를 식히고 출혈을 멎게 하는 약으로 분류된다[3]. 임상에서는 흔히 열을 내리는 약재와 함께 처방해 지혈 효과를 높였다[3]. 기침, 가래가 많은 증상, 만성 기관지염, 기관지 확장증, 천식 같은 호흡기 질환에도 전통적으로 쓰였다[18].\n\n"
"측백엽은 탈모를 막고 머리카락이 자라게 하는 용도로도 전해 내려왔다[27]. 동아시아에서는 탈모 치료용 복합 처방의 한 구성 약재로 널리 쓰였다고 소개된다[26]. 씨앗(백자인, Platycladi Semen)은 중국에서 2000년 동안 불면과 변비에 쓰였다고 한다[32]. 정유는 아로마 원료로, 잎 정유는 나무·스파이스 계열의 향료로 산업에 쓰였다[9].\n\n"
"국내 식품원료 목록에도 약재 이름인 '측백엽'이 이명으로 함께 적혀 있다[1]. 대구 도동 측백나무 숲은 1962년 천연기념물 제1호로 지정되었다고 보도되었으나, 이 내용은 국가유산청 원문이 아닌 검색 요약으로만 확인했다[35]. 한국에서 잎을 차나 음식으로 먹어 온 전통 기록은 확인하지 못함."),
("biology","식물학적 특징",
"측백나무는 암수한그루(한 나무에 수꽃과 암꽃이 함께 피는)의 늘푸른 바늘잎나무다[23]. 잎은 작은 비늘 모양으로, 정유 분석에는 수관 가운데의 어린 비늘잎을 따서 썼다[9]. 스트레스에 강하고 적응 범위가 넓으며 수명이 수천 년에 이르기도 한다[22]. 중국 황제릉의 고목 가운데에는 수령 5000년으로 전해지는 나무가 있다[9].\n\n"
"봄에 꽃가루를 많이 날려 꽃가루 알레르기를 일으키기 쉽다[23]. 베이징에서는 4월 초·중순이 측백나무의 개화 절정기였고, 이 시기에 알레르기 비염 외래 환자가 뚜렷이 늘었다[25].\n\n"
"잎은 구과(열매)보다 플라보노이드가 많고, 잎에는 플라본 배당체가, 구과에는 바이플라본이 주로 쌓인다[5]. 잎의 플라보노이드는 여름과 겨울에 가장 많았다[5]. 잎 정유 성분은 산지에 따라 크게 달라, 중국 16곳 시료에서 α-피넨 5.1~68.1%, δ-3-카렌 0.1~29.4%, 세드롤 3.4~23.7%였다고 인용된다[4]. 잎에는 이소피마르산·산다라코피마르산 같은 디테르펜도 들어 있다[17]."),
("related_species","분류와 근연종",
"측백나무는 린네가 Thuja orientalis로 처음 이름 붙였으나, 지금은 별도의 속으로 옮겨 Platycladus orientalis (L.) Franco로 쓰며 Biota orientalis (L.) Endl.도 동의어다[5]. 식품원료 목록에는 'Thuja orientalis L. / Biota orientalis L.'로 적혀 있다[1]. 중국에서 측백나무속은 이 한 종뿐이다[4].\n\n"
"같은 장소·같은 방법으로 비교한 정유 분석에서 측백나무와 원예품종 'Sieboldii'·'Aurea'는 α-피넨/δ-3-카렌형으로 묶였다[4]. 향나무(Juniperus chinensis)와 사비나향나무(J. sabina)는 사비넨형으로 갈렸고, α-피넨·사비넨·δ-3-카렌 세 성분으로 두 속을 완전히 구별할 수 있었다[4].\n\n"
"측백엽 약재에는 편백(Chamaecyparis obtusa), Cupressus funebris, 연필향나무(Juniperus virginiana), Sabina chinensis, Juniperus formosana 잎이 섞여 잘못 쓰이는 일이 있다[8]. 측백나무 잎은 이들보다 미리시트린·퀘르시트린 또는 총 플라보노이드 함량이 유의하게 높아, 현미경 관찰과 TLC·HPLC로 구별할 수 있었다[8]. 서양측백(Thuja occidentalis) 등 Thuja속 다른 종과의 성분 비교 자료는 확인하지 못함."),
("cultivation","재배와 생산",
"측백나무는 중국에서 도시 조경과 산지 조림에 중요한 나무로 널리 심는다[23]. 중국 각지에는 역사 기록이 남은 수백~수천 년 된 고목 집단이 있어 유전 자원으로 가치가 크다[21]. 고목 집단 분석에서는 개체 사이의 유연관계가 지리적 위치와 맞지 않는 경우가 많아, 사람이 옮겨 심고 가꾼 역사가 있었을 가능성이 제시되었다[21].\n\n"
"잎의 플라보노이드는 여름과 겨울에 많아, 원하는 성분에 맞춰 채취 시기를 고르는 것이 중요하다고 제안되었다[5]. 나무 나이도 잎 성분에 영향을 주어, 황제릉 고목 잎의 정유 수율은 수령 3000년에서 1.810%로 가장 높았다[9]. 5~3000년생 나무 비교에서는 나이가 많을수록 플라보노이드가 늘었다[29]. 중국 여러 산지의 측백엽 27건은 플라보노이드 7종 함량에 따라 다섯 무리로 나뉘었고, 이는 산지의 지리·기후 조건과 대체로 일치했다[6].\n\n"
"국내 측백나무 재배 면적이나 측백엽 생산량 통계는 확인하지 못함. 국내 지리적 표시 등록이나 생산자 단체도 확인하지 못함."),
("processing","가공과 이용",
"국내 식품원료 목록에는 잎(측백엽)과 잎 추출물이 원료명으로 올라 있다[1]. 잎 정유는 물증류에서 0.1%, 수증기증류에서 0.07% 얻어졌고, 물증류 정유는 α-피넨(17.83%), 수증기증류 정유는 α-세드롤(12.44%)이 가장 많아 추출 방법에 따라 조성이 달랐다[12]. 다른 연구에서 잎 정유 수율은 0.41%(v/w)였다[4].\n\n"
"용매 비교에서 아세트산 추출 수율이 14.17%로 가장 높고 에탄올이 9.60%로 가장 낮았지만, 총 페놀·플라보노이드는 에탄올 추출물에 가장 많았다[29]. 수지 흡착으로 정제한 잎 폴리페놀은 세포 실험에서 항산화·항염 작용을 보여 기능성 식품 소재로 쓸 가능성이 제시되었다[33]. 중국에서는 잎을 검게 볶은 측백엽탄(Platycladi Cacumen Carbonisatum)도 쓰며, 그 에틸아세테이트 추출물에 총 플라보노이드가 가장 많았다[30]. 쥐에게 잎 추출물을 먹인 약동학 연구에서는 퀘르시트린·아프젤린·아멘토플라본·히노키플라본의 혈중 농도를 함께 재는 방법이 확립되었다[28].\n\n"
"국내에서는 잎 물 추출물을 12주 동안 두피에 바른 시험에서 성모 밀도가 늘었다는 보고가 있다[26]. 씨앗 기름 추출물은 무릎 골관절염 시험에 쓰였지만, 씨앗은 국내 식품원료 사용 가능 부위가 아니다[31, 1]. 식약처 「식품 등의 생산실적」에서 측백나무 원료 품목은 확인하지 못함."),
("genetics","유전 정보",
"측백나무의 반수체 염색체 수는 11개다[19]. 한 어미나무의 대배우체 139개를 ddRAD-seq로 분석해 23,926개 표지를 11개 연관군, 전체 1,443 cM에 배치한 첫 고밀도 유전지도가 만들어졌다[19].\n\n"
"2026년에는 콘티그 N50이 57.54 Mb인 염색체 수준 유전체 조립이 발표되었다[20]. 이 연구는 겉씨식물의 거대 유전체에서 전이인자가 유전자 중복과 위유전자화를 일으켜 유전자 집단의 변화에 큰 역할을 한다고 보고했다[20]. 엽록체 유전체에는 단백질 암호화 유전자 83개, tRNA 유전자 33개, rRNA 유전자 4개 등 120개 유전자가 있다[34].\n\n"
"중국 13개 고목 집단 100개체를 SLAF 시퀀싱으로 분석해 81,722개의 SNP를 찾았고, 개체들은 9개 유전형으로 묶였다[21]. 실시간 PCR 연구에서는 UBC와 α-튜불린 유전자가 여러 발달 단계와 스트레스 조건에서 가장 안정적인 기준 유전자로 뽑혔다[22]. 같은 장소에서 자란 측백나무와 원예품종의 정유 조성 차이는 주로 유전형 차이에서 온 것으로 해석되었다[4]."),
("safety","안전성",
"측백나무는 식약처 「식품원료 목록」에서 '제한적사용' 원료이고, 쓸 수 있는 부위는 잎(측백엽)뿐이다[1]. 제한적 사용 원료는 정해진 조건 안에서만 쓰며, 별도 조건이 없으면 가공 전 원료 중량의 50% 미만으로 쓴다는 기준은 검색 요약으로만 확인했다[2].\n\n"
"투존은 GABA-A 수용체를 억제해 용량에 따라 흥분과 경련을 일으키는 신경독성 성분이며, 약초와 식이를 통한 허용 섭취량은 하루 3~7 mg 정도로 추정된다[15]. 측백나무 가지 정유에 α-투존이 50~60% 들어 있다는 보고와, 잎에서 투존을 살연체 활성 성분으로 확인했다는 보고가 있다[13, 14]. 그러나 이란·인도·중국·파키스탄의 잎 정유 분석에서는 α-피넨·δ-3-카렌·세드롤이 주성분이어서, 투존 함량은 출처마다 다르다[10, 11, 4, 12]. 세이지 연구에서는 물로 우린 차에 에탄올 추출의 평균 30%만큼만 투존이 녹아 나왔다[16]. 측백엽의 투존 정량값과 국내 투존 기준은 확인하지 못함.\n\n"
"꽃가루는 알레르기 원인이 되며, 측백나무를 포함한 이탈리아 진단 패널에서 꽃가루 감작 환자의 평균 18.4%가 양성이었다[24]. 씨앗은 아플라톡신 오염이 보고되었다[32]. 사람이 잎을 먹었을 때의 독성 자료와 임신·수유 중 안전성은 확인하지 못함."),
]
sections=[{"key":k,"title":t,"body":b} for k,t,b in secs]

C=[]
def c(name,ko,cls,role,part,content,act,src): C.append(dict(name=name,name_ko=ko,**{"class":cls},role=role,part=part,content_text=content,activity_ko=act,source=src))
c("Quercitrin","퀘르시트린","플라보놀 배당체","marker","잎","잎 0.615(봄)~2.021(여름) mg/g 건조중량, 구과 0~0.49 mg/g(HPTLC, 이집트 시료 3년 평균)[5]","잎 추출물의 항염 활성에 양(+)으로 기여한 바이오마커로 꼽힘[5]; 위품 감별에서 측백나무 잎이 위품보다 함량이 유의하게 높음[8]",[5,8])
c("Isoscutellarein 7-O-beta-xyloside","이소스쿠텔라레인-7-O-β-자일로사이드","플라본 배당체","marker","잎","잎 0.840~3.804 mg/g 건조중량(여름 최고)[5]","잎의 주된 플라본으로, 항염 활성의 바이오마커로 꼽힘[5]",[5])
c("Hyperoside","히페로사이드","플라보놀 배당체","bioactive","잎","잎 0~1.082 mg/g 건조중량(여름 최고, 가을 검출 안 됨), 구과 검출 안 됨[5]","항염 활성에 양(+)으로 기여한 성분[5]",[5])
c("Hinokiflavone","히노키플라본","바이플라보노이드","bioactive","잎·구과","잎 0.259~1.300 mg/g, 구과 0.276~0.53 mg/g 건조중량[5]","잎 추출물 투여 후 쥐 혈장에서 정량된 4개 플라보노이드 중 하나[28]",[5,28])
c("Cupressuflavone","쿠프레수플라본","바이플라보노이드","bioactive","잎·구과","잎 0.101~0.704 mg/g, 구과 0.283~0.56 mg/g 건조중량[5]","구과의 주된 바이플라본이나 항염 활성과는 음(−)의 관련을 보임[5]",[5])
c("Myricitrin","미리시트린","플라보놀 배당체","marker","잎","함량은 확인하지 못함(UPLC로 27개 시료를 정량했으나 초록에 수치 없음)[6]","α-글루코시다아제 억제 활성과 관련이 큰 성분으로 꼽힘(초록)[6]; 위품보다 측백나무 잎에 많음[8]",[6,8])
c("Amentoflavone","아멘토플라본","바이플라보노이드","bioactive","잎","함량은 확인하지 못함(HPLC 정량 대상 4종 중 하나)[7]","측백나무 품질 평가용 4개 생리활성 플라보노이드 중 하나로 정량됨[7]",[7])
c("Afzelin","아프젤린","플라보놀 배당체","bioactive","잎","함량은 확인하지 못함(UPLC 정량 대상 7종 중 하나)[6]","잎 추출물 투여 후 쥐 혈장에서 정량된 성분[28]",[6,28])
c("alpha-Pinene","α-피넨","모노테르펜 탄화수소","bioactive","잎(정유)","잎 정유 34.23%(중국)[4], 21.9%(이란)[10], 29.2%(인도 히말라야)[11], 17.83%(파키스탄, 물증류)[12]; 고목 잎 HS-SPME 6.40~16.76%[9]","정유의 주성분으로, 측백나무속과 향나무속을 구별하는 지표 성분 중 하나[4]",[4,9,10,11,12])
c("3-Carene","δ-3-카렌","모노테르펜 탄화수소","bioactive","잎(정유)","잎 정유 15.86%(중국)[4], 10.5%(이란)[10], 20.1%(인도 히말라야)[11]; 고목 잎 HS-SPME 1.14~15.12%[9]","측백나무속을 향나무속과 구별하는 지표 성분 중 하나[4]",[4,9,10,11])
c("Cedrol","세드롤","세스퀴테르펜 알코올","bioactive","잎(정유)","잎 정유 20.3%(이란)[10], 9.8%(인도 히말라야)[11], 12.44%(파키스탄, 수증기증류)[12]; 고목 잎 HS-SPME 2.34~11.30%[9]","히말라야산 정유에서 항진균 활성 성분으로 분리됨[11]; 나무 나이가 많을수록 상대 함량이 늘어남[9]",[9,10,11,12])
c("alpha-Terpinyl acetate","α-테르피닐 아세테이트","모노테르펜 에스터","bioactive","잎(정유)","고목 잎 HS-SPME 1.29~25.68%[9]; 히말라야산 잎 정유 3.5%[11]","나무 나이를 가르는 차이 성분 중 하나[9]",[9,11])
c("Thujone","투존(α-·β-투존)","모노테르펜 케톤","bioactive","가지·잎(정유)","측백나무 가지 정유의 α-투존 50~60%라는 보고[13]; 잎에서 살연체 활성 성분으로 확인했다는 보고[14]; 다른 잎 정유 분석의 주성분 목록에는 없음[4, 10, 11]","GABA-A 수용체 억제로 흥분·경련을 일으키는 신경독성 성분, 허용 섭취량 추정 하루 3~7 mg[15]",[4,10,11,13,14,15])
c("Sandaracopimaric acid","산다라코피마르산","디테르펜(피마란형)","bioactive","잎","함량은 확인하지 못함[17]","잎 에틸아세테이트 추출물의 GABA-A 수용체 조절 활성의 주성분; 쥐 복강 투여 3~30 mg/kg에서 운동량 감소[17]",[17])
c("Hinokiol","히노키올","디테르펜","bioactive","잎","함량은 확인하지 못함[18]","5-리폭시게나아제를 억제하고 대식세포의 NO·TNF-α 생성을 줄임(세포 실험)[18]",[18])

empty = {k:"" for k in ["instrument","column","mobile_phase","gradient","flow","temp","detection","injection","sample_prep","standard","linearity","lod","loq","recovery"]}
assays=[
{"role":"literature","compound":"Quercitrin","compound_ko":"퀘르시트린(플라보노이드 7종 동시 정량)","part":"잎·구과(공기 건조 분말)",
 "content":"잎 퀘르시트린 0.615~2.021 mg/g, 이소스쿠텔라레인-7-O-β-자일로사이드 0.840~3.804 mg/g 건조중량; 여름 잎 총 9.374 mg/g[5]",
 "method":"HPTLC-이미지 분석(유도체화 후 스캔)",
 "conditions":{**empty,
  "instrument":"Camag Linomat V 자동 밴드 도포기(100 μL 주사기); 평판 스캐너(Canon MF 4750) + ImageJ 이미지 분석",
  "column":"정상상 실리카 사전 코팅 HPTLC 플레이트(10 cm × 20 cm)",
  "mobile_phase":"계 I(퀘르시트린·히페로사이드·이소스쿠텔라레인-7-O-β-자일로사이드): 에틸아세테이트/메탄올/물/아세트산 45:4:2:0.35(v/v); 계 II(바이플라본·8-메톡시 이소스쿠텔라레인): 톨루엔/에틸아세테이트 2:1",
  "detection":"아니스알데하이드/황산 시약에 담근 뒤 150 °C 가열, UV 254 nm 관찰 및 스캔 이미지의 피크 면적",
  "injection":"표준품 밴드 6 mm·간격 4 mm, 시료 밴드 8 mm·간격 5 mm, 바닥·가장자리에서 1.5 cm; 표준품 1 mg/mL를 2~7 μL 도포(3반복)",
  "sample_prep":"공기 건조·분쇄한 잎 또는 구과 25 g을 95% 에탄올 1 L에 침지, 여과·감압 농축 후 메탄올에 재용해, 0.45 μm 필터 여과",
  "standard":"측백나무 잎에서 직접 분리하고 NMR·MS로 확인한 7종(외부 검량선, μg/spot 대 피크 면적)",
  "linearity":"각 표준품 r² ≥ 0.990(ICH 2005 기준 검증, 보충자료 Table S1)"},
 "rationale":"잎의 주된 플라본 배당체이자 항염 활성과 가장 관련이 큰 바이오마커로 확인되었다[5]. 검출·정량한계와 회수율은 보충자료에만 있어 본문에서 확인하지 못해 비워 둠.",
 "source":[5],"url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC9036908/","source_kind":"paper"},
{"role":"literature","compound":"alpha-Pinene","compound_ko":"α-피넨(잎 휘발성분 82종 상대 정량)","part":"잎(어린 비늘잎, 실리카겔 건조 분말)",
 "content":"α-피넨 6.40~16.76%(초록)·6.88~16.76%(본문), δ-3-카렌 1.14~15.12%, (+)-세드롤 2.34~11.30%(초록), α-테르피닐 아세테이트 1.29~25.68%(면적 백분율)[9]",
 "method":"HS-SPME-GC-MS",
 "conditions":{**empty,
  "instrument":"Agilent 6890N GC-5975B MS",
  "column":"HP-5MS, 30 m × 0.25 mm × 0.25 μm",
  "mobile_phase":"운반기체 고순도 헬륨",
  "gradient":"50 °C → 250 °C(2 °C/min), 250 °C에서 20분 유지; 용매 지연 3분",
  "flow":"1.0 mL/min",
  "temp":"주입구 230 °C(승온 조건 설명에는 280 °C로도 적혀 있음), 검출기 280 °C",
  "detection":"EI 70 eV, 이온원 230 °C, 사중극자 150 °C, 인터페이스 230 °C, 전체 스캔 m/z 50~550",
  "injection":"분할비 100:1, 섬유를 주입구에서 5분 탈착",
  "sample_prep":"시료 1.0 g을 10 mL 헤드스페이스 병에 넣고 80 °C에서 30분 평형, PDMS 섬유(SUPELCO, 원문 표기 '100 μL')로 추출",
  "standard":"표준품 없이 NIST 라이브러리(2.2) 검색으로 동정, 면적 정규화법으로 상대 함량 계산"},
 "rationale":"α-피넨·δ-3-카렌·세드롤은 측백나무 잎 정유의 주성분이고, 이 세 성분과 사비넨이 측백나무속을 근연 속과 구별하는 지표로 쓰인다[4, 9]. 면적 백분율이라 절대 함량이 아니며 검출·정량한계·회수율은 보고되지 않음.",
 "source":[9,4],"url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC10003951/","source_kind":"paper"},
{"role":"literature","compound":"Quercitrin","compound_ko":"퀘르시트린(루틴·퀘르세틴·아멘토플라본과 동시 정량)","part":"측백나무(중국 12개 산지)",
 "content":"초록에 함량 수치가 없어 확인하지 못함[7]",
 "method":"RP-HPLC-DAD",
 "conditions":{**empty,
  "column":"Agilent Eclipse XDB-C18",
  "mobile_phase":"메탄올-아세토니트릴-18 mM 아세트산나트륨 완충액(pH 3.5)",
  "detection":"UV 356 nm(다이오드 어레이 검출기)",
  "linearity":"루틴 0.8~80 μg/mL, 퀘르시트린 1.84~184 μg/mL, 퀘르세틴 0.72~72 μg/mL, 아멘토플라본 0.72~72 μg/mL, r > 0.999"},
 "rationale":"측백나무 품질 평가를 위한 4개 주요 생리활성 플라보노이드로 선정되었다[7]. 전문 확인 못함 — 초록에 있는 칼럼·이동상·파장·직선 범위만 옮김.",
 "source":[7],"url":"https://pubmed.ncbi.nlm.nih.gov/16621407/","source_kind":"paper"},
{"role":"literature","compound":"Myricitrin","compound_ko":"미리시트린 등 플라보노이드 7종(지문 분석 + 정량)","part":"측백엽(말린 어린 가지와 잎, 중국 27건)",
 "content":"초록에 함량 수치가 없어 확인하지 못함[6]",
 "method":"UPLC-DAD",
 "conditions":{**empty,
  "linearity":"7종 모두 r ≥ 0.9995",
  "recovery":"96.4~103.3%"},
 "rationale":"20개 공통 피크 가운데 미리시트린·이소퀘르시트린·퀘르시트린·아프젤린·쿠프레수플라본·아멘토플라본·히노키플라본을 동시 정량해 산지별 품질을 구분했다[6]. 전문 확인 못함 — 칼럼·이동상 등은 초록에 없어 비워 둠.",
 "source":[6],"url":"https://pubmed.ncbi.nlm.nih.gov/28977346/","source_kind":"paper"},
]

d={"slug":"thuja-orientalis","name_ko":"측백나무","name_en":"Chinese arborvitae (Oriental thuja)",
 "scientific_name":"Thuja orientalis L. (= Platycladus orientalis (L.) Franco)",
 "aliases":["측백나무잎","측백나무잎추출물","측백엽","Chinese arbor vitae","Platycladus orientalis (L.) Franco","Biota orientalis","Oriental thuja","Platycladi Cacumen"],
 "sections":sections,"compounds":C,"markers":[],"nutrients":[],"assays":assays,"production":[],"world":[],"gi":[],"orgs":[],"sources":S}
(H/"dossier.json").write_text(json.dumps(d,ensure_ascii=False,indent=1),encoding="utf-8")
for s in sections: print(s["key"],len(s["body"]))
