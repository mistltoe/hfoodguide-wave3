import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
A = "2026-11-02"
def pm(n, title, pmid, pmc=None):
    return {"n": n, "title": title, "url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
            "publisher": f"PubMed (PMID {pmid}" + (f", {pmc}" if pmc else "") + ")", "accessed": A}
sources = [
 {"n": 1, "title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 백목련꽃잎(Magnolia denudata Desr.) 항목 및 같은 속 목련꽃잎·버지니아목련꽃잎·별목련꽃잎·후박·황목련·목련꽃봉오리추출물 항목",
  "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
 pm(2, "Park CH et al. Analysis of Metabolites in White Flowers of Magnolia denudata Desr. and Violet Flowers of Magnolia liliiflora Desr. Molecules 2018;23(7):1558 (doi:10.3390/molecules23071558)", "29954130", "PMC6100211"),
 pm(3, "Hyeon H et al. Profiles of Essential Oils and Correlations with Phenolic Acids and Primary Metabolites in Flower Buds of Magnolia heptapeta and Magnolia denudata var. purpurascens. Molecules 2021;27(1):221 (doi:10.3390/molecules27010221)", "35011454", "PMC8746637"),
 pm(4, "Wu X et al. Assessment of quality in volatile oil from three basic sources of Xinyi from Hubei by anatomy, GC-MS, and chemometric methods. Sci Rep 2025;15:6857 (doi:10.1038/s41598-025-91477-z)", "40011674", "PMC11865492"),
 pm(5, "Shen Y et al. Inhibitions of mast cell-derived histamine release by different Flos Magnoliae species in rat peritoneal mast cells. Phytomedicine 2008;15(10):808-14 (doi:10.1016/j.phymed.2008.04.012)", "18585022"),
 pm(6, "Joo YH et al. UPLC-QTOF-MS/MS screening and identification of bioactive compounds in fresh, aged, and browned Magnolia denudata flower extracts. Food Res Int 2020;133:109192 (doi:10.1016/j.foodres.2020.109192)", "32466951"),
 pm(7, "Park H et al. Antioxidative and Anticanceric Activities of Magnolia (Magnolia denudata) Flower Petal Extract Fermented by Pediococcus acidilactici KCCM 11614. Molecules 2015;20(7):12154-65 (doi:10.3390/molecules200712154)", "26151113", "PMC6331971"),
 pm(8, "Ku B et al. Effects of Magnolia denudata extract on quality and storage characteristics of emulsified chicken sausage. Food Sci Anim Resour 2026;46(1) (doi:10.1007/s44463-025-00026-9)", "42268519", "PMC13253912"),
 pm(9, "Kim GC et al. Magnoliae flos induces apoptosis of RBL-2H3 cells via mitochondria and caspase. Int Arch Allergy Immunol 2003;131(2):101-10 (doi:10.1159/000070925)", "12811018"),
 pm(10, "Kong CS et al. In vitro evaluation on the antiobesity effect of lignans from the flower buds of Magnolia denudata. J Agric Food Chem 2011;59(10):5665-70 (doi:10.1021/jf200230s)", "21462973"),
 pm(11, "Li J et al. Lignan and neolignan derivatives from Magnolia denudata. Chem Pharm Bull 2005;53(2):235-7 (doi:10.1248/cpb.53.235)", "15684526"),
 pm(12, "Hu YQ et al. Analysis of Chemical Components and Pharmacological Activities of Different Processing Methods in Magnolia denudata Desr. 'Hailuo' Using GC-MS and Network Pharmacology. Comb Chem High Throughput Screen 2026 (doi:10.2174/0113862073469562260529131806)", "42367119"),
 pm(13, "Zeng X et al. Essential oil of Magnolia denudata is an effective anesthetic for spotted seabass (Lateolabrax maculatus). Fish Physiol Biochem 2022;48(5):1349-63 (doi:10.1007/s10695-022-01124-x)", "36114399"),
 pm(14, "Wang S et al. Integrated Multiscale Imaging and Noninvasive Micro-Sensing Decipher Spatiotemporal Calcium Dynamics in Thermogenic Tissue of Magnolia Flower. Plant Cell Environ 2026;49(1):126-39 (doi:10.1111/pce.70196)", "40988373"),
 pm(15, "Liu L et al. Temporal Petal Closure Benefits Reproductive Development of Magnolia denudata (Magnoliaceae) in Early Spring. Front Plant Sci 2017;8:430 (doi:10.3389/fpls.2017.00430)", "28424715", "PMC5371817"),
 pm(16, "Wang S et al. Multi-Omics Combined With Mitochondrial Feeding Assays Reveal a Novel Energy Metabolism Strategy for Floral Thermogenesis in Magnolia. Plant Biotechnol J 2026;24(4):2169-83 (doi:10.1111/pbi.70479)", "41316548", "PMC13140744"),
 pm(17, "Liu H et al. Different water relations between flowering and leaf periods: a case study in flower-before-leaf-emergence Magnolia species. Funct Plant Biol 2017;44(11):1098-1110 (doi:10.1071/FP16429)", "32480636"),
 pm(18, "Wu K et al. Physiological and transcriptome analysis of Magnolia denudata leaf buds during long-term cold acclimation. BMC Plant Biol 2021;21:460 (doi:10.1186/s12870-021-03181-5)", "34625030", "PMC8501692"),
 pm(19, "Hu M et al. Cell polarity, asynchronous nuclear divisions, and bidirectional cytokinesis in male meiosis in Magnolia denudata. Protoplasma 2021;258(3):621-32 (doi:10.1007/s00709-020-01604-y)", "33389128"),
 pm(20, "Wu Z et al. [Differentiation of Magnolia denudata Desr. flower buds]. Zhongguo Zhong Yao Za Zhi 1991;16(2):79-81 (영문 초록)", "1651734"),
 pm(21, "Wu Z et al. [Types of flowering branch of Magnolia denudata Desr. under high yield conditions]. Zhongguo Zhong Yao Za Zhi 1992;17(6):336-8 (영문 초록)", "1418575"),
 pm(22, "Wang S et al. Integrating mitoflash, energy substrate, and hormone analyses to advance understanding of Magnolia endodormancy mechanisms. Int J Biol Macromol 2025;315:144333 (doi:10.1016/j.ijbiomac.2025.144333)", "40389010"),
 pm(23, "Wang Z et al. Toxicity and possible mechanisms of action of honokiol from Magnolia denudata seeds against four mosquito species. Sci Rep 2019;9:411 (doi:10.1038/s41598-018-36558-y)", "30674912", "PMC6344527"),
 pm(24, "Chung CY et al. Biphenyl-Type Neolignan Derivatives from the Twigs of Magnolia denudata and Their Anti-Inflammatory Activity. Chem Biodivers 2015;12(8):1263-70 (doi:10.1002/cbdv.201400297)", "26265578"),
 pm(25, "Du J et al. Chemical constituents from the leaves of Magnolia denudata. J Asian Nat Prod Res 2001;3(4):313-9 (doi:10.1080/10286020108040371)", "11783585"),
 pm(26, "Noshita T et al. Machilin G and four neolignans from young fruits of Magnolia denudata show various degrees of inhibitory activity on nitric oxide (NO) production. Biosci Biotechnol Biochem 2008;72(10):2775-8 (doi:10.1271/bbb.80327)", "18838787"),
 pm(27, "Zhang PQ et al. Pollution resistance assessment of existing landscape plants on Beijing streets based on air pollution tolerance index method. Ecotoxicol Environ Saf 2016;132:212-23 (doi:10.1016/j.ecoenv.2016.06.003)", "27326901"),
 pm(28, "Wang L et al. Identification of Magnolia wufengensis (Magnoliaceae) cultivars using phenotypic traits, SSR and SRAP markers. Genet Mol Res 2017;16(1) (doi:10.4238/gmr16019473)", "28252172"),
 pm(29, "Wu W. [GC-MS analysis of chemical components in essential oil from Flos magnoliae]. Zhong Yao Cai 2000;23(9):538-41 (영문 초록)", "12575280"),
 pm(30, "Wang R et al. Heat production and volatile biosynthesis are linked via alternative respiration in Magnolia denudata during floral thermogenesis. Front Plant Sci 2022;13:955665 (doi:10.3389/fpls.2022.955665)", "36311085", "PMC9614359"),
 pm(31, "Noshita T et al. New cytotoxic phenolic derivatives from matured fruits of Magnolia denudata. Biosci Biotechnol Biochem 2009;73(3):726-8 (doi:10.1271/bbb.80597)", "19270419"),
 pm(32, "Ma Y et al. Antidepressant-like Effects of Five Essential Oils Inhaled in Reserpine-induced Depressed Mouse Models. Chem Biodivers 2025;22(11):e00971 (doi:10.1002/cbdv.202500971)", "40644689"),
]

S = {}
S["overview"] = ("백목련(Magnolia denudata Desr.)은 목련과 목련속의 나무로[18], 잎보다 꽃이 먼저 피고[17] 이른 봄 추위 속에 꽃을 피우며[14], 꽃은 희다[2]. "
 "식품의약품안전처 「식품원료 목록」에는 '백목련꽃잎'이 '사용가능' 원료로 올라 있고, 사용 조건은 '사용가능부위 : 꽃잎'이며 이명은 '흰가지꽃나무', 영명은 'Yulan'이다[1]. "
 "같은 목록의 학명 칸에는 Gwillimia yulan deVos와 Lassonia heptapeta Buchoz가 함께 적혀 있다[1]. "
 "따라서 식품으로 쓸 수 있는 부위는 꽃잎뿐이며, 약재 '신이(辛夷)'로 쓰이는 꽃봉오리와 수피·씨앗·열매·잎은 이 목록의 사용 부위에 들어 있지 않다[1]. "
 "이 종을 원재료로 하는 건강기능식품 고시형 원료는 확인하지 못함.\n\n"
 "꽃에는 루틴·클로로겐산 같은 페놀 성분이 들어 있고[2], 꽃봉오리 정유에는 사비넨·β-피넨·1,8-시네올 등 모노테르펜이 많다[3]. "
 "중국에서는 이 종의 말린 꽃봉오리가 M. biondii·M. sprengeri와 함께 약전 생약 '신이(Xinyi)'의 기원으로 올라 있다[4]. "
 "꽃봉오리에서는 새 네오리그난 1종과 이미 알려진 리그난·네오리그난 15종이 분리되었고[11], 꽃봉오리 리그난 일부는 지방세포 분화를 억제했다(시험관)[10]. "
 "잎에서는 리그난 16종을 포함한 20개 화합물이 분리되었으나, 잎은 식품원료 사용 부위가 아니다[25][1]. "
 "효능 연구는 대부분 세포·동물 실험이며, 사람을 대상으로 한 임상 근거는 확인하지 못함.")
S["history"] = ("한 연구는 백목련이 전통 의약에서 부비동염에 따른 두통, 코막힘, 알레르기 비염을 다스리는 진통 약으로 쓰였다고 정리했다[2]. "
 "중국에서는 말린 꽃봉오리를 '신이'라 하여 비염 환약·점비액·정유 등에 써 왔고, 이 생약은 중국 약전에 M. biondii·M. denudata·M. sprengeri 세 종을 기원으로 올라 있다[4]. "
 "한국에서는 백목련 꽃봉오리(Magnoliae flos)가 알레르기 질환 관리에 쓰여 왔다고 한 논문이 적었다[9]. "
 "중국 안후이성의 1991년 관찰 연구는 화관이 벌어지기 전 다 자란 꽃봉오리를 따는 것이 알맞다고 권했다[20]. "
 "꽃은 차로 우려 마시며 맛을 좋게 하려고 발효시키기도 한다[6]. "
 "백목련은 중국에서 아름다운 꽃 때문에 널리 알려진 관상수이며[13], 한국에서도 관상수로 널리 심는다[3]. "
 "대한민국약전이 '신이'의 기원 종을 어떻게 정하는지와 한국에 들어온 시기·경로는 이번 조사에서 원문으로 확인하지 못함.")
S["biology"] = ("백목련은 잎이 나기 전에 꽃이 피는 목련이며, 꽃덮이(tepal)는 잎보다 두껍고 물기가 많으며 기공이 크고 적어 증산이 낮았다[17]. "
 "같은 가지에서 꽃의 수액 흐름 밀도는 잎에 대해 예측한 값의 22%였다[17]. "
 "꽃은 스스로 열을 내는 발열성 꽃으로, 개화를 다섯 단계로 나눌 때 2단계가 발열 정점이고 열을 내는 부위는 암술군 옆 조직이었다[14]. "
 "이 시기에 대체호흡 경로(AOX)가 활발해져 시트르산이 1.35배 늘었고, 이것이 휘발 성분 합성의 재료가 된다는 해석이 나왔다[30]. "
 "발열 단계에서는 탄수화물·지방산·아미노산 대사가 함께 에너지를 공급했다[16]. "
 "꽃잎은 피었다가 잠시 닫히는데, 닫힘을 막자 꽃밥 발달과 꽃가루 발아가 늦어지고 씨앗 맺음이 줄었다[15]. "
 "꽃가루 모세포의 감수분열은 대부분의 속씨식물과 다른 방식의 세포질 분열을 보였다[19]. "
 "꽃봉오리 꽃덮이의 기름세포 밀도는 정유 함량과 양의 상관을 보였다[4].")
S["related_species"] = ("식약처 「식품원료 목록」에는 목련꽃잎(M. kobus), 버지니아목련꽃잎(M. virginiana), 별목련꽃잎(M. stellata)이 각각 따로 올라 있고 모두 꽃잎만 쓸 수 있다[1]. "
 "같은 목록에서 후박(M. officinale)과 황목련(M. obovata, 이명 일본목련)은 '사용불가'이며, 목련꽃봉오리추출물은 M. kobus 꽃봉오리로 만든 건강기능식품 개별인정형 원료다[1]. "
 "이 문서는 백목련 자료만 쓰고 이들 종의 자료는 섞지 않았다[1]. "
 "신이의 기원 종은 나라와 문헌마다 달라, 중국 약전은 M. biondii·M. denudata·M. sprengeri를 올리며 후베이 시료에서 백목련 정유 함량은 M. biondii보다 낮고 M. sprengeri보다 높았다(본문 시료 순서로 대응)[4]. "
 "신이로 쓰이는 6종을 비교한 연구에서 마그놀린은 M. biondii·M. kobus·M. liliflora에서만, 파르게신은 M. biondii·M. kobus에서만 검출되고 백목련에서는 둘 다 나오지 않았다[5]. "
 "흰 꽃의 백목련은 보라 꽃의 자목련(M. liliiflora)보다 페놀 성분이 적었다[2]. "
 "보라 꽃봉오리를 맺는 변종 var. purpurascens는 β-미르센이 더 많았다[3]. "
 "변종 var. dilutipurpurascens는 곁꽃가지가 거의 생기지 않았다[21].")
S["cultivation"] = ("신이 기원 세 종은 중국 안후이·허난·쓰촨·후베이성에서 주로 재배된다[4]. "
 "안후이성 관찰에서 백목련 꽃눈 분화는 5월 초에 시작해 6월 말에 끝나 약 50일 걸렸고, 3월 초가 꽃봉오리가 자라고 수확하는 중요한 시기라 웃거름을 늦지 않게 주라고 권했다[20]. "
 "다수확 조건에서는 곁꽃가지가 수량을 늘리는 데 중요했다[21]. "
 "후베이 시료에서 백목련 꽃봉오리 정유 함량은 0.45–2.62%였고 5단계(1월)에 가장 높아 그때가 알맞은 수확기로 제시되었다(본문에서 종명이 빠져 시료 순서로 대응함)[4]. "
 "중국 약전의 정유 1% 기준을 후베이산 M. biondii와 백목련은 넘었고 M. sprengeri는 넘지 못했다[4]. "
 "베이징 도로변 수목 47종 평가에서 백목련은 대기오염에 강한 수종으로 꼽혔다[27]. "
 "잎눈은 0 °C·4 °C 순화를 거치며 내한성이 높아졌다[18]. "
 "꽃눈 휴면이 풀릴 때 지베렐린과 아브시스산의 움직임이 반대였다[22]. "
 "국내 재배 면적·생산량, 지리적 표시 등록, 생산자 단체는 확인하지 못함.")
S["processing"] = ("식약처 목록의 식품원료명은 '백목련꽃잎'으로, 꽃잎 자체가 원료다[1]. "
 "꽃차를 발효·숙성하면 루틴·클로로겐산·1-카페오일퀸산은 줄고 퀸산은 늘었으며, 이소베르바스코사이드·이소악테오사이드 같은 이성질체가 새로 생겼다[6]. "
 "꽃잎 추출물을 유산균(Pediococcus acidilactici)으로 발효하는 동안 총페놀이 고형분 1 g당 38.1에서 47.0 mg GAE로 늘었고, 발효물의 항산화 효과는 발효하지 않은 대조의 3배였다[7]. "
 "활짝 핀 꽃을 말려 80% 에탄올로 추출한 동결건조물(수율 5.33%)을 닭가슴살 소시지에 0.2% 넣자 지방 산화(TBARS)와 휘발성 염기질소가 줄었으나, 쓴맛이 강해져 전체 기호도가 낮아졌다[8]. "
 "약용 품종 'Hailuo' 꽃봉오리는 햇볕 말림에서 42개 휘발 성분이 확인되어 그늘·오븐 건조보다 알맞았다[12]. "
 "꽃의 정유는 물고기 마취제로 시험되었으며 점농어에는 100 mg/L가 최소 유효 농도였다[13]. "
 "생쥐에게 정유를 흡입시킨 실험에서는 우울 유사 행동이 줄었으나, 쓴 부위는 초록에서 확인하지 못함[32]. "
 "국내 건강기능식품 원료 생산실적은 확인하지 못함.")
S["genetics"] = ("백목련의 핵 유전체 해독 결과와 염색체 수는 이번 조사에서 확인하지 못함. "
 "잎눈을 22 °C·4 °C·0 °C에서 순화시킨 전사체 분석은 4억 2,600만 개가 넘는 정제 읽기에서 74,503개의 유전자 단위를 조립했고, 추위에서 357개가 늘고 235개가 줄었다[18]. "
 "이 연구는 bHLH·AP2/ERF 계열 전사인자가 추위 적응에 중요하다고 보았다[18]. "
 "꽃 발열 단계에서는 TCA 회로와 산화적 인산화 관련 유전자, 지방산 β-산화 효소 유전자가 많이 발현되었다[16]. "
 "꽃눈 휴면 연구에서는 아브시스산 처리로 전사인자 MdMYB91의 발현이 늘었고, 이 단백질이 PP2C 유전자 프로모터에 붙어 발현을 억제했다[22]. "
 "SSR·SRAP 표지로 본 백목련 집단의 유전 다양성은 M. wufengensis 품종들보다 약간 낮았다[28]. "
 "발열 꽃의 전사체에서는 AOX 유전자의 발현 증가가 포착되었다[30].")
S["safety"] = ("식약처 「식품원료 목록」에서 백목련은 꽃잎만 쓸 수 있는 '사용가능' 원료이며, 그 밖의 섭취량 제한이나 주의사항은 목록에서 확인하지 못함[1]. "
 "같은 속의 후박과 황목련은 '사용불가'로 올라 있어, 꽃잎이 아닌 다른 목련 부위나 다른 종과 혼동하지 않아야 한다[1]. "
 "이 종을 원재료로 하는 건강기능식품 고시형 원료가 없어 고시된 섭취 시 주의사항도 확인하지 못함. "
 "흰 꽃 에탄올 추출물은 대식세포(RAW 264.7)에서 31.25 µg/mL를 넘는 농도부터 세포 생존율을 낮췄다[2]. "
 "발효 꽃잎 추출물은 암세포 증식을 더 억제했지만 정상 폐 섬유아세포(MRC-5)에는 영향이 없었다(시험관)[7]. "
 "씨앗에서 얻은 호노키올은 모기 유충에 강한 독성을 보였는데[23], 씨앗은 식품원료 사용 부위가 아니다[1]. "
 "열매에서 분리한 페놀 유도체 일부는 세포독성을 보였다[31]. "
 "정유로 마취한 물고기는 아가미에 가벼운 조직 변화와 2차 스트레스를 보였다[13]. "
 "사람이 꽃잎을 먹었을 때의 알레르기·독성에 관한 국내외 공공기관 정보는 확인하지 못함.")

titles = {"overview": "한눈에 보기", "history": "역사와 쓰임", "biology": "식물학적 특징", "related_species": "가까운 종",
          "cultivation": "재배와 생산", "processing": "가공과 이용", "genetics": "유전체와 육종", "safety": "안전성"}
sections = [{"key": k, "title": titles[k], "body": S[k]} for k in titles]

def C(name, ko, cls, role, part, content, act, src):
    return {"name": name, "name_ko": ko, "class": cls, "role": role, "part": part, "content_text": content, "activity_ko": act, "source": src}
compounds = [
 C("Rutin", "루틴", "플라보놀 배당체", "marker", "꽃봉오리(흰 꽃), 꽃",
   "흰 꽃봉오리 69.14 ± 4.63 mg/g dry wt.(가장 많은 페놀 성분)[3]; 꽃에서도 가장 많은 성분[2]",
   "꽃 발효·숙성 시 감소(음이온 fold change −0.47)[6]", [3, 2, 6]),
 C("Chlorogenic acid", "클로로겐산", "페놀산(카페오일퀸산)", "marker", "꽃봉오리, 꽃",
   "흰 꽃봉오리 3.55 ± 0.29 mg/g dry wt.[3]; 꽃에서 두 번째로 많은 성분[2]",
   "꽃 발효·숙성 시 감소(fold change −1.48)[6]", [3, 2, 6]),
 C("Eucalyptol", "1,8-시네올(유칼립톨)", "산소화 모노테르펜", "marker", "꽃봉오리 정유",
   "후베이산 꽃봉오리 정유 0.36–17.87%(피크 면적 %, 5단계 최고)[4]; 제주산 흰 꽃봉오리 정유 7.59%[3]",
   "신이 정유 품질의 핵심 지표로 쓰임[4]; 'Hailuo' 품종 꽃봉오리 정유의 주성분[12]", [4, 3, 12]),
 C("Sabinene", "사비넨", "모노테르펜 탄화수소", "bioactive", "꽃봉오리 정유",
   "흰 꽃봉오리 정유 15.19%(피크 면적 %)[3]", "신이 세 기원 종(M. biondii·M. denudata·M. sprengeri) 정유의 주성분 가운데 하나(종별 값은 초록에서 확인하지 못함)[29]", [3, 29]),
 C("beta-Pinene", "β-피넨", "모노테르펜 탄화수소", "bioactive", "꽃봉오리 정유",
   "흰 꽃봉오리 정유 12.92%(보라 꽃봉오리 7.67%)[3]", "흰 꽃봉오리를 가르는 대표 대사체[3]", [3]),
 C("beta-Myrcene", "β-미르센", "모노테르펜 탄화수소", "bioactive", "꽃봉오리 정유",
   "흰 꽃봉오리 정유 9.94%, 보라 꽃봉오리(var. purpurascens) 17.19%[3]", "꽃봉오리 정유의 주요 모노테르펜[3]", [3]),
 C("Germacrene D", "게르마크렌 D", "세스퀴테르펜 탄화수소", "bioactive", "꽃봉오리 정유",
   "흰 꽃봉오리 정유 7.73%[3]", "꽃봉오리 정유의 주된 세스퀴테르펜 탄화수소[3]", [3]),
 C("beta-Cubebene", "β-쿠베벤", "세스퀴테르펜 탄화수소", "bioactive", "꽃봉오리 정유",
   "후베이산 꽃봉오리 정유 0.29–21.39%(생육 단계별, 피크 면적 %)[4]", "백목련 꽃봉오리 정유 30개 성분 가운데 눈에 띄는 성분[4]", [4]),
 C("beta-Eudesmol", "β-오이데스몰", "산소화 세스퀴테르펜", "bioactive", "꽃봉오리 정유",
   "흰 꽃봉오리 정유 3.66%(보라 꽃봉오리 0.91%)[3]", "흰 꽃봉오리에서 더 많은 산소화 세스퀴테르펜[3]", [3]),
 C("Isoacteoside", "이소악테오사이드", "페닐에타노이드 배당체", "bioactive", "꽃(꽃차)",
   "함량 수치는 확인하지 못함; 발효·숙성 뒤 fold change 3.33[6]", "꽃차 발효 중 생기는 이성질체[6]", [6]),
 C("Magnolin", "마그놀린", "리그난", "marker", "꽃봉오리",
   "백목련 꽃봉오리에서 검출되지 않음(RP-HPLC)[5]",
   "다른 신이 기원 종의 지표성분으로 쓰이나 백목련에서는 나오지 않아 종 구별에 참고가 됨[5]", [5]),
 C("Denudatin B", "데누다틴 B", "네오리그난", "bioactive", "어린 열매",
   "함량 수치는 확인하지 못함[26]", "생쥐 대식세포에서 NO 생성 억제(시험관)[26]", [26]),
 C("Honokiol", "호노키올", "네오리그난(바이페닐)", "bioactive", "씨앗, 잔가지",
   "함량 수치는 확인하지 못함[23][24]",
   "씨앗 유래 성분이 모기 유충 4종에 LC50 6.13–7.37 mg/L[23]; 잔가지 유래 성분이 사람 호중구 초과산화물 생성 억제 IC50 0.71 µg/mL(시험관)[24]", [23, 24]),
 C("Magnolol", "마그놀롤", "네오리그난(바이페닐)", "bioactive", "잔가지",
   "함량 수치는 확인하지 못함[24]", "호중구 초과산화물 생성 억제 IC50 4.4 µg/mL, 엘라스테이스 방출 억제 IC50 1.5 µg/mL(시험관)[24]", [24]),
]

def cond(**kw):
    keys = ["instrument","column","mobile_phase","gradient","flow","temp","detection","injection","sample_prep","standard","linearity","lod","loq","recovery"]
    return {k: kw.get(k, "") for k in keys}
assays = [
 {"role": "literature", "compound": "Rutin", "compound_ko": "루틴(클로로겐산·카페산·쿠마르산·페룰산·신남산 동시)",
  "part": "꽃봉오리(제주 남원산 흰 꽃봉오리, 2021년 2월 채취)",
  "content": "69.14 ± 4.63 mg/g dry wt.; 클로로겐산 3.55 ± 0.29 mg/g dry wt.[3]",
  "method": "HPLC-PDA(외부 검량)",
  "conditions": cond(instrument="Waters Alliance e2695 HPLC + 광다이오드 배열 검출기",
     column="Agilent Zorbax CB-C18, 250 × 4.6 mm, 5 µm",
     mobile_phase="A: 0.1% 아세트산 물, B: 0.1% 아세트산 아세토니트릴",
     gradient="0분 92% A/8% B; 2분 90/10; 35분 70/30; 50분 10/90; 51분 0/100; 60분 0/100; 63분 92/8",
     flow="1 mL/min", temp="40 °C", detection="200–400 nm 감시, 280 nm 크로마토그램", injection="10 µL",
     sample_prep="꽃봉오리 45 °C 72시간 건조·분쇄 → 분말 100 mg + 메탄올 1 mL + 0.1 M HCl 200 µL, 1분 볼텍스·1시간 초음파 → 13,000 rpm 10분 원심, 상층 800 µL 취함 → 잔사에 메탄올 1 mL 재추출 → 합쳐 농축 후 메탄올 1 mL에 녹여 0.50 µm PTFE 여과",
     standard="표준품 머무름 시간·UV 스펙트럼 비교; 2.5–80 ppm 검량선"),
  "rationale": "꽃봉오리에서 가장 많은 페놀 성분이며 흰 꽃봉오리(M. heptapeta로 표기, 식약처 목록의 이명 Lassonia heptapeta와 같은 종)를 보라 꽃봉오리와 가르는 대표 대사체였다[3]. 직선성·검출한계·정량한계·회수율은 원문에서 확인하지 못함.",
  "source": [3], "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8746637/", "source_kind": "paper"},
 {"role": "literature", "compound": "Eucalyptol", "compound_ko": "1,8-시네올(정유 30개 성분 동시, 면적 정규화)",
  "part": "꽃봉오리(중국 후베이성 셴닝·우한·언스, 2022년 5월–2023년 3월 6단계 채취)",
  "content": "정유 내 0.36–17.87%(5단계 최고, 피크 면적 %); 정유 함량 0.45–2.62%(5단계 최고)[4]",
  "method": "수증기 증류 + GC-MS(EI)",
  "conditions": cond(instrument="Agilent 7890A GC / 5975C MS",
     column="HP-5MS 모세관, 0.25 mm × 30 m, 0.1 µm(원문 표기)",
     mobile_phase="운반 기체(종류는 'high-purity gas'로만 적힘) 1.0 mL/min",
     gradient="60 °C 2분 → 3 °C/min 115 °C → 6 °C/min 130 °C → 3 °C/min 200 °C → 10 °C/min 250 °C, 2분 유지",
     flow="1.0 mL/min, 분할비 10:1", temp="주입구 200 °C, 사중극자 150 °C, 이온원 230 °C",
     detection="EI, m/z 50–550; NIST 14 라이브러리 동정", injection="1.0 µL(디클로로메탄 800 µg/mL)",
     sample_prep="꽃봉오리 37 °C 건조·분쇄(60메시) → 분말 10 g + 증류수 400 mL, 정유 측정기로 5시간 가열(중국 약전 4부) → 디클로로메탄 추출·무수황산나트륨 건조·용매 제거",
     standard="피크 면적 정규화(상대 함량)"),
  "rationale": "1,8-시네올은 신이 정유 품질의 핵심 지표로 여겨지며, 이 연구는 중국 약전의 정유 1% 기준과 함께 평가했다[4]. 본문의 종명이 빠져 있어 시료 a·b·c를 초록의 종 순서(M. biondii·M. denudata·M. sprengeri)로 대응했다. 직선성·검출한계·정량한계·회수율은 원문에 없음.",
  "source": [4], "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11865492/", "source_kind": "paper"},
 {"role": "literature", "compound": "Sabinene", "compound_ko": "사비넨(꽃봉오리 정유 30개 성분 동시, 면적 정규화)",
  "part": "꽃봉오리(제주 남원산 생 꽃봉오리)",
  "content": "정유 수율 0.35%(생체중 w/w); 사비넨 15.19%, β-피넨 12.92%, β-미르센 9.94%, 1,8-시네올 7.59%(피크 면적 %)[3]",
  "method": "Clevenger 수증기 증류 + GC-MS(EI)",
  "conditions": cond(instrument="Agilent 7890A GC / 5975C MSD",
     column="HP-5MS, 30 m × 0.25 mm, 0.25 µm(19091S-433)",
     mobile_phase="헬륨 1.00 mL/min",
     gradient="40 °C 2분 → 3 °C/min → 250 °C, 10분 유지",
     flow="1.00 mL/min, 분할비 10:1", temp="주입구 230 °C, 이온원 230 °C, 사중극자 150 °C",
     detection="EI 70 eV, m/z 50–550; n-알케인(C8–C20) 머무름 지수·NIST 유사도 90% 초과로 동정", injection="1 µL",
     sample_prep="생 꽃봉오리 1 kg Clevenger 장치로 8시간 증류 → 정유를 헥산으로 1:1000 희석, 0.50 µm PTFE 여과",
     standard="피크 면적 정규화(상대 함량)"),
  "rationale": "모노테르펜 탄화수소가 정유의 58%를 차지했고 그중 사비넨이 가장 많았다[3]. 직선성·검출한계·정량한계·회수율은 원문에 없음.",
  "source": [3], "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8746637/", "source_kind": "paper"},
 {"role": "literature", "compound": "Magnolin", "compound_ko": "마그놀린·파르게신",
  "part": "꽃봉오리(신이 기원 6종 비교)",
  "content": "백목련에서 마그놀린·파르게신 모두 검출되지 않음[5]",
  "method": "RP-HPLC",
  "conditions": cond(),
  "rationale": "마그놀린·파르게신은 신이의 지표성분으로 쓰이나 백목련에서는 나오지 않아, 다른 기원 종과 구별하는 데 참고가 된다[5]. 초록만 확인해 분석 조건은 전문 확인 못함.",
  "source": [5], "url": "https://pubmed.ncbi.nlm.nih.gov/18585022/", "source_kind": "paper"},
]

d = {"slug": "magnolia-denudata", "name_ko": "백목련", "name_en": "Yulan magnolia",
     "scientific_name": "Magnolia denudata Desr.",
     "aliases": ["백목련꽃잎", "흰가지꽃나무", "Yulan", "Gwillimia yulan deVos", "Lassonia heptapeta Buchoz", "Magnolia heptapeta (Buc'hoz) Dandy", "신이(꽃봉오리 약재명)"],
     "sections": sections, "compounds": compounds, "markers": [], "assays": assays, "nutrients": [],
     "production": [], "world": [], "gi": [], "orgs": [], "sources": sources}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in sections: print(s["key"], len(s["body"]))
