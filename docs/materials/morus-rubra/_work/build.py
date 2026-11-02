import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
A = "2026-11-02"
I1020 = "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020"
def pm(n): return f"https://pubmed.ncbi.nlm.nih.gov/{n}/"
sources = [
 (1, "식품원료 목록: 붉은뽕나무열매(Morus rubra, Red mulberry) — 사용가능, 사용가능부위 : 열매", I1020, "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020)", "2026-10-13"),
 (2, "식품원료 목록: 뽕나무속 다른 행 — 뽕나무(Morus alba L.; 뿌리껍질·어린가지·잎·열매·순), 산뽕나무(Morus bombycis; 잎·열매), 노상잎(Morus lhou; 잎), 돌뽕나무열매(Morus cathayana / 이명 Morus rubra var. japonica Makino; 열매), 몽고뽕나무열매·검뽕나무열매·Western mulberry열매(Morus microphylla; 열매), 복합원료(U코드) 붉은뽕나무향(Morus rubra L., RED MULBERRY FLAVOUR; 사용가능), 식품첨가물 멀베리색소(Morus nigra, M. alba)", I1020, "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020, 로컬 원자료 I1020_20261013)", "2026-10-13"),
 (3, "Reporting complete chloroplast genome of endangered red mulberry, useful for understanding hybridization and phylogenetic relationships (2025)", pm(40251250), "Scientific Reports 15 (PubMed PMID 40251250, PMC12008415 전문 확인)", A),
 (4, "Asymmetrical introgression between two Morus species (M. alba, M. rubra) that differ in abundance (2005)", pm(16156816), "Molecular Ecology 14(11):3471-83 (PubMed PMID 16156816, 초록 확인)", A),
 (5, "Interspecific seed discounting and the fertility cost of hybridization in an endangered species (2007)", pm(17944826), "New Phytologist 177(1):276-284 (PubMed PMID 17944826, 초록 확인)", A),
 (6, "Red mulberry (Morus rubra): COSEWIC assessment and status report 2014 (WebSearch 요약으로만 봄 — 페이지가 네트워크 허용 목록 밖이라 열지 못함)", "https://www.canada.ca/en/environment-climate-change/services/species-risk-public-registry/cosewic-assessments-status-reports/red-mulberry-2014.html", "캐나다 멸종위기야생생물위원회(COSEWIC)·캐나다 환경기후변화부 — WebSearch 요약", A),
 (7, "Plant Guide: Red mulberry, Morus rubra L. (WebSearch 요약으로만 봄 — 원문 PDF는 열지 못함)", "https://plants.usda.gov/DocumentLibrary/plantguide/pdf/cs_moru2.pdf", "미국 농무부 자연자원보전청(USDA NRCS) — WebSearch 요약", A),
 (8, "Silvics of North America, Vol. 2: Morus rubra L. Red Mulberry (WebSearch 요약으로만 봄 — 원문은 열지 못함)", "https://dendro.cnre.vt.edu/dendrology/USDAFSSilvics/58.pdf", "미국 농무부 산림청(USDA Forest Service) 「Silvics of North America」 — WebSearch 요약", A),
 (9, "Morus rubra 식물 정보(암수딴그루·풍매, 잎 뒷면 털, 열매 색·길이) (WebSearch 요약으로만 봄 — 원문은 열지 못함)", "https://ncwildflower.org/plant_galleries/details/morus-rubra", "North Carolina Native Plant Society·Clemson University 식물 정보 페이지 — WebSearch 요약", A),
 (10, "Biochemical characterization of mulberry (Morus spp.) genotypes from the Türkiye (Hizan, Bitlis): A comprehensive analysis of fruit properties and bioactive compounds (2024)", pm(39554318), "Food Science & Nutrition 12 (PubMed PMID 39554318, PMC11561804 전문 확인)", A),
 (11, "Morpho-physicochemical and antioxidant trait diversity of red mulberry (Morus rubra L.) genotypes from northwestern Iran (2026)", pm(41699505), "BMC Plant Biology (PubMed PMID 41699505, PMC13014883 전문 확인)", A),
 (12, "Preservation of bioactive compounds in mulberry species (Morus spp.) under different drying conditions (2025)", pm(40858651), "Scientific Reports 15 (PubMed PMID 40858651, PMC12381166 전문 확인)", A),
 (13, "Comparison of mineral contents of mulberry (Morus spp.) fruits and their pekmez (boiled mulberry juice) samples (2009)", pm(18982510), "International Journal of Food Sciences and Nutrition 60(3):231-9 (PubMed PMID 18982510, 초록 확인)", A),
 (14, "Resveratrol content and antioxidant properties of underutilized fruits (2015)", pm(25593373), "Journal of Food Science and Technology 52(1):383-90 (PubMed PMID 25593373, 초록 확인 — PMC 전문 본문은 비어 있었음)", A),
 (15, "Rapid quantitative analysis of individual anthocyanin content based on high-performance liquid chromatography with diode array detection with the pH differential method (2014)", pm(24964353), "Journal of Separation Science 37(18):2535-44 (PubMed PMID 24964353, 초록 확인)", A),
 (16, "Proximate composition and antioxidant potential of leaves from three varieties of Mulberry (Morus sp.): a comparative study (2012)", pm(22837655), "International Journal of Molecular Sciences 13(6):6651-6664 (PubMed PMID 22837655, 초록 확인)", A),
 (17, "Antidiabetogenic action of Morus rubra L. leaf extract in streptozotocin-induced diabetic rats (2010)", pm(20487205), "Journal of Pharmacy and Pharmacology 62(2):247-55 (PubMed PMID 20487205, 초록 확인)", A),
 (18, "Protective effect of Morus rubra L. leaf extract on diet-induced atherosclerosis in diabetic rats (2010)", pm(21086751), "Indian Journal of Biochemistry & Biophysics 47(1):26-31 (PubMed PMID 21086751, 초록 확인)", A),
 (19, "Morus Rubra Extract Induces Cell Cycle Arrest and Apoptosis in Human Colon Cancer Cells Through Endoplasmic Reticulum Stress and Telomerase (2017)", pm(27880042), "Nutrition and Cancer 69(1):74-83 (PubMed PMID 27880042, 초록 확인)", A),
 (20, "Effects of Cornus mas L. and Morus rubra L. extracts on penicillin-induced epileptiform activity: an electrophysiological and biochemical study (2017)", pm(28379215), "Acta Neurobiologiae Experimentalis 77(1):45-56 (PubMed PMID 28379215, 초록 확인)", A),
 (21, "Evaluation of in vitro effect of Morus rubra (red mulberry) on survival of periodontal ligament cells (2008)", pm(18230381), "Oral Surgery, Oral Medicine, Oral Pathology, Oral Radiology, and Endodontics 105(2):e66-9 (PubMed PMID 18230381, 초록 확인)", A),
 (22, "Insights into the Activities and Usefulness of Deoxynojirimycin and Morus alba: A Comprehensive Review (2025)", pm(40807388), "Molecules 30 (PubMed PMID 40807388, 초록 확인)", A),
 (23, "Red mulberry fruit aqueous extract and silk proteins accelerate acute ethanol metabolism and promote the anti-oxidant enzyme systems in rats (2018)", pm(29767238), "Molecular Medicine Reports 18(1):1197-1205 (PubMed PMID 29767238, 초록 확인)", A),
 (24, "Genetic relationships between selected Turkish mulberry genotypes (Morus spp) based on RAPD markers (2010)", pm(21053181), "Genetics and Molecular Research 9(4):2176-83 (PubMed PMID 21053181, 초록 확인)", A),
 (25, "Comparative metabolite profiling of four polyphenol rich Morus leaves extracts in relation to their antibiofilm activity against Enterococcus faecalis (2022)", pm(36424446), "Scientific Reports 12:20168 (PubMed PMID 36424446, 초록 확인)", A),
 (26, "Changes in composition, structure and aboveground biomass over seventy-six years (1930-2006) in the Black Rock Forest, Hudson Highlands, southeastern New York State (2008)", pm(18244941), "Tree Physiology 28(4):537-49 (PubMed PMID 18244941, 초록 확인)", A),
 (27, "Characterization of Turkish mulberry genetic resources based on antioxidant capacity, biochemical composition, nutrient content, and morphological traits of leaves (2025)", pm(40603370), "Scientific Reports 15:23197 (PubMed PMID 40603370, 초록 확인)", A),
 (28, "Phytochemicals, Pharmacological Effects and Molecular Mechanisms of Mulberry (2022)", pm(35454757), "Foods 11(8) (PubMed PMID 35454757, 초록 확인)", A),
 (29, "Red mulberry 수그루 꽃가루 알레르기 관련 플로리다대학교 농업생명과학연구소(UF/IFAS) 확장 자료 (WebSearch 요약으로만 봄 — 원문은 열지 못함)", "https://journals.flvc.org/edis/article/download/118629/116554/174020", "UF/IFAS Extension(EDIS) — WebSearch 요약", A),
]
src = [dict(n=n, title=t, url=u, publisher=p, accessed=a) for n, t, u, p, a in sources]

S = {}
S["overview"] = ("개요",
"붉은뽕나무(Morus rubra L.)는 뽕나무과 뽕나무속의 갈잎 나무로, 북아메리카 동부가 원산이다[3]. "
"식약처 「식품원료 목록」에는 '붉은뽕나무열매'(학명 Morus rubra, 영어명 Red mulberry)로 올라 있고, 상태는 '사용가능', 조건은 '사용가능부위 : 열매'다[1]. "
"따라서 일반 식품원료로 쓸 수 있는 부위는 열매뿐이며, 잎·뿌리껍질·어린가지는 이 종의 식품원료 부위가 아니다[1]. "
"같은 목록의 복합원료(U코드)에는 향료 원료 '붉은뽕나무향'(Morus rubra L.)이 '사용가능'으로 따로 올라 있다[2]. "
"목록은 돌뽕나무열매(Morus cathayana)의 이명으로 'Morus rubra var. japonica Makino'를 적고 있어, 학명 일부만 보고 이 종과 혼동하지 않도록 주의해야 한다[2].\n\n"
"열매 성분 연구는 주로 튀르키예·이란에서 'red mulberry(M. rubra)'라고 부른 개체를 대상으로 했다[10][11][12]. "
"이 개체들이 북미 자생 집단과 같은 계통인지는 논문만으로 확인하지 못함. "
"효능 연구는 대부분 잎 추출물을 쓴 세포·동물 실험이며, 붉은뽕나무 열매로 한 사람 대상 연구는 확인하지 못함. "
"건강기능식품 기능성 원료 고시에서 이 종을 원재료로 하는 원료도 확인하지 못함.")

S["history"] = ("이용의 역사",
"미국 농무부 식물 안내서는 북미 원주민 여러 부족이 붉은뽕나무를 여러 질환의 치료에 썼다고 적었다는 검색 요약이 있으나 원문은 확인하지 못함[7]. "
"흰뽕나무(M. alba)는 누에치기 산업을 세우려고 1600년대 초 식민지 시기에 북아메리카로 들여왔고, 이후 분포를 빠르게 넓혀 붉은뽕나무의 분포 범위와 겹치거나 그것을 넘어섰다[3]. "
"이 도입이 오늘날 붉은뽕나무가 잡종화로 위협받게 된 배경이다[3].\n\n"
"튀르키예에서는 붉은뽕나무 열매를 생으로 먹고 마멀레이드·주스·잼·천연 염료로 쓰며, 해열·설사·장내 기생충에 좋다고 여겨 왔다고 한 논문이 소개했다[20]. "
"튀르키예 말라티아 지역에서는 오디를 졸인 '페크메즈'(오디 조청)를 만들며, 붉은뽕나무 열매와 그 조청도 무기질 분석 대상이 되었다[13]. "
"튀르키예는 오디 열매의 주요 생산국 가운데 하나로 소개된다[24]. "
"국내에서 붉은뽕나무를 들여와 재배하거나 열매를 유통한 기록은 확인하지 못함.")

S["biology"] = ("식물학적 특징",
"붉은뽕나무는 미국 동부에 널리 퍼진 빨리 자라는 나무로, 골짜기·범람원의 습한 토양과 해발 약 600 m 이하에서 자란다는 검색 요약이 있으나 원문은 확인하지 못함[8]. "
"다 자라면 높이 약 20 m, 줄기 지름 약 45 cm에 이른다는 요약도 원문은 확인하지 못함[7]. "
"암수딴그루이고 바람으로 꽃가루받이를 하며, 잎 뒷면에 부드러운 털이 있고 앞면이 거칠어 흰뽕나무와 구별하는 단서가 된다는 요약이 있으나 원문은 확인하지 못함[9]. "
"열매는 암그루에 달리며 붉은색에서 자주색으로 익고 길이가 약 2.5 cm(1인치)라는 요약도 원문은 확인하지 못함[9].\n\n"
"튀르키예 히잔 지역 붉은뽕나무 11개 유전자형의 열매는 무게 1.22–4.18 g, 너비 11.26–15.82 mm, 길이 17.24–23.94 mm였다[10]. "
"이란 북서부 20개 유전자형은 열매 무게 1.53–3.97 g, 가용성 고형분 13.53–16.17%, 적정산도 0.70–1.61%였다[11]. "
"튀르키예 샨르우르파의 개체는 짙은 빨강–자줏빛 빨강 단계, 길이 2.0–2.5 cm, 당도 약 19.2 °Brix에 수확했다[12]. "
"좋은 종자 결실은 2–3년마다 오고 열매는 1 kg에 평균 약 8,600개라는 요약도 원문은 확인하지 못함[8].")

S["related_species"] = ("근연종과 구별",
"식약처 목록에서 뽕나무(M. alba)는 열매·잎·어린가지·뿌리껍질·순, 산뽕나무(M. bombycis)는 잎·열매, 노상(M. lhou)은 잎을 쓸 수 있다[2]. "
"돌뽕나무(M. cathayana)·몽고뽕나무(M. mongolica)·검뽕나무(M. nigra)·Western mulberry(M. microphylla)는 붉은뽕나무처럼 열매만 사용가능부위다[2]. "
"엽록체 유전체 계통 분석에서 뽕나무속은 아시아·북아메리카·남아메리카·아프리카 계통군으로 나뉘었고, 북미와 아시아 계통군은 약 2,869만 년 전에 갈라진 것으로 추정되었다[3].\n\n"
"붉은뽕나무는 들어온 흰뽕나무와 자연 잡종을 만든다[4]. "
"캐나다 온타리오의 네 동소 집단 184그루를 조사한 연구에서 핵 표지로 본 잡종 비율은 53.7%(집단별 43–67%)였다[4]. "
"잡종의 67%는 흰뽕나무 쪽 핵 표지를 더 많이 지녔고, 68%는 흰뽕나무 엽록체를 지녀 유전자 이입이 비대칭임을 보였다[4]. "
"잡종이 여러 세대 이어져 전문가도 종 판정을 혼동하며, 공공 유전자 데이터베이스에 종 동정이 불확실한 서열이 올라간 사례도 지적되었다[3]. "
"한 동물 연구는 'Red mulberry (Morus alba)'라고 적어, 영어 이름 'red mulberry'만으로 종을 판단할 수 없음을 보여 준다[23]. "
"잡종(M. alba × M. rubra) 개체의 열매 성분을 따로 분석한 자료는 확인하지 못함.")

S["cultivation"] = ("자생·재배",
"붉은뽕나무는 북쪽으로 캐나다 온타리오 남부, 남쪽으로 플로리다 남부, 서쪽으로 대평원 동쪽 가장자리까지 분포하며, 사람 손을 덜 탄 강가 숲에서 주로 자란다[3]. "
"미국 코네티컷·매사추세츠에서는 멸종위기종, 미시간·버몬트에서는 위협종으로 다룬다[3]. "
"캐나다 COSEWIC는 1987년 '위협', 1999년 '멸종위기'로 지정하고 2014년 재평가에서 유지했다는 검색 요약이 있으나 원문은 확인하지 못함[6]. "
"같은 요약은 2014년 캐나다에 남은 나무가 약 217그루(성숙목 105그루)이고 가장 큰 위협이 흰뽕나무와의 잡종화라고 했다(원문은 확인하지 못함)[6].\n\n"
"온타리오 동소 집단에서 뽕나무속 꽃가루 가운데 붉은뽕나무가 만든 것은 평균 8%였다[5]. "
"흰뽕나무와 잡종을 실험적으로 걷어 내자 붉은뽕나무의 꽃가루 생식력이 14% 늘었으나 종자 결실률은 변하지 않았다[5]. "
"미국 뉴욕주 블랙록 숲에서는 1930년대–2000년 사이 새로 들어온 7종 가운데 하나로 기록되었다[26]. "
"튀르키예에서는 흩어진 나무나 오래된 반재배 농원에서 자라는 개체가 연구되었다[10][12]. "
"국내 재배 면적·생산량 통계는 확인하지 못함.")

S["processing"] = ("가공과 이용",
"튀르키예에서는 열매를 생으로 먹거나 마멀레이드·주스·잼으로 만든다[20]. "
"말라티아 연구에서 열매 칼륨이 가장 높았던 것은 붉은뽕나무 열매(15.269 g/kg)였다[13]. "
"같은 연구에서 붉은뽕나무·검뽕나무 조청(페크메즈)은 만드는 과정에서 무기질이 흰뽕나무보다 크게 줄었다[13].\n\n"
"샨르우르파 건조 연구에서 그늘 말림한 붉은뽕나무 열매는 총페놀 10.34 mg GAE/g, DPPH 소거 47.68%로 세 종 가운데 가장 높았다[12]. "
"55 °C 열풍 건조에서는 두 값이 크게 떨어졌고 65 °C에서 조금 회복되었다[12]. "
"붉은뽕나무 열매의 칼슘은 그늘 말림 10,660 mg/kg에서 65 °C 건조 9,238 mg/kg으로 줄었다[12]. "
"이 논문은 결과를 생중량 기준이라 적으면서 총페놀은 건물 1 g당으로 표기해 기준이 원문 안에서 엇갈린다[12]. "
"열매즙 4% 희석액은 시험관에서 빠진 치아의 치주인대 세포 보관액으로 평가되었다[21]. "
"국내 붉은뽕나무 열매 가공품 생산실적은 확인하지 못함.")

S["genetics"] = ("유전·생리 연구",
"미국 8개 주에서 모은 시료로 붉은뽕나무 엽록체 유전체 전체를 처음 해독했다[3]. "
"크기는 초록에 159,396–159,423 bp, 본문에 159,393–159,423 bp로 적혀 있고, 유전자 128개(단백질 83, rRNA 8, tRNA 37)를 지니며 GC 함량은 36.1%였다[3]. "
"붉은뽕나무 엽록체는 흰뽕나무보다 최소 103 bp 컸고, 종 안에서 12개 하플로타입이 나왔으나 염기 다양도(Pi)는 0.00002로 낮았다[3]. "
"북미의 자매종과는 약 993만 년 전에 갈라진 것으로 추정되었다[3].\n\n"
"튀르키예 오디 유전자형 26개의 RAPD 분석에서 흰뽕나무 Oltu3와 붉은뽕나무 Oltu18의 유전적 유사도가 0.36으로 가장 낮았다[24]. "
"이란 연구는 형태 검색표와 전문가 확인으로 종을 동정하고, 잡종 형질을 보인 개체는 뺐다[11]. "
"튀르키예 잎 유전자원 21개 연구에도 붉은뽕나무가 포함되었다[27]. "
"이집트 연구는 붉은뽕나무 등 네 종 잎 추출물에서 UPLC-ESI-MS/MS로 61개 폴리페놀을 동정했다(잎은 식품원료 부위 아님)[25][1]. "
"오디의 영양·성분은 종마다 다르다고 종설이 정리했다[28].")

S["safety"] = ("안전성",
"식약처 목록에서 붉은뽕나무는 열매만 '사용가능'이며, 잎을 식품원료로 쓸 근거는 목록에 없다[1]. "
"붉은뽕나무 열매로 한 사람 대상 임상시험이나 독성시험은 확인하지 못함.\n\n"
"인도 연구에서 잎 물 추출물(100–400 mg/kg)을 21일 먹인 당뇨 쥐는 공복 혈당이 용량에 따라 내려갔다[17]. "
"같은 연구진은 건강한 쥐로 단기 독성도 평가했다고 적었으나 결과 수치는 초록에 없다[18]. "
"부위가 초록에 적히지 않은 디메틸설폭사이드 추출물이 사람 대장암 세포(WiDr)에 중간 정도의 선택적 세포독성을 보였다는 결과는 세포 실험이다[19]. "
"쥐 뇌전증 모델의 결과(10 mg/kg)도 동물 실험이라 사람 효과로 옮길 수 없다[20]. "
"뽕나무 알레르기로 호흡기 알레르기·접촉 두드러기·아나필락시스·구강 알레르기 증후군·식품 두드러기가 보고되었으며, 종을 가르지 않은 뽕나무속 전반의 정보다[22]. "
"수그루 꽃가루가 알레르기를 잘 일으킨다는 자료는 검색 요약으로만 보았고 원문은 확인하지 못함[29]. "
"잎 연구의 총페놀은 16.21–24.37 mg GAE/g로 보고되었으나 세 종 범위라 이 종만의 값은 확인하지 못함[16]. "
"국내 공공기관의 붉은뽕나무 열매 잔류농약·독성 정보는 확인하지 못함.")

sections = [dict(key=k, title=v[0], body=v[1]) for k, v in S.items()]

FR = "열매"
compounds = [
 dict(name="Rutin", name_ko="루틴", class_="플라보놀 배당체", role="marker", part=FR,
      content_text="튀르키예 히잔 붉은뽕나무 11개 유전자형 생과 9.34–38.51 mg/kg(생과 1 g 메탄올 추출, HPLC-UV)[10]",
      activity_ko="주성분 분석에서 DPPH 항산화능과 가깝게 묶임(시험관)[10]", source=[10]),
 dict(name="Epicatechin", name_ko="(−)-에피카테킨", class_="플라반-3-올", role="marker", part=FR,
      content_text="같은 유전자형 0.84–99.74 mg/kg, 최고 13HZN23 유전자형[10]",
      activity_ko="이 종에서 단독 활성은 확인하지 못함", source=[10]),
 dict(name="Chlorogenic acid", name_ko="클로로겐산", class_="하이드록시신남산 에스터", role="bioactive", part=FR,
      content_text="같은 유전자형 0.81–57.97 mg/kg[10]",
      activity_ko="이 종에서 단독 활성은 확인하지 못함", source=[10]),
 dict(name="Caffeic acid", name_ko="카페인산", class_="하이드록시신남산", role="bioactive", part=FR,
      content_text="같은 유전자형 0.25–44.39 mg/kg[10]",
      activity_ko="이 종에서 단독 활성은 확인하지 못함", source=[10]),
 dict(name="Protocatechuic acid", name_ko="프로토카테큐산", class_="하이드록시벤조산", role="bioactive", part=FR,
      content_text="같은 유전자형 0.34–2.51 mg/kg; p-하이드록시벤조산은 붉은뽕나무에서 검출되지 않음[10]",
      activity_ko="이 종에서 단독 활성은 확인하지 못함", source=[10]),
 dict(name="Catechin", name_ko="(+)-카테킨", class_="플라반-3-올", role="bioactive", part=FR,
      content_text="같은 유전자형 0–0.79 mg/kg(13HZN25는 검출되지 않음)[10]",
      activity_ko="이 종에서 단독 활성은 확인하지 못함", source=[10]),
 dict(name="Cyanidin 3-glucoside", name_ko="시아니딘-3-글루코사이드", class_="안토시아닌", role="marker", part=FR,
      content_text="총 안토시아닌(시아니딘-3-글루코사이드 환산) 튀르키예 붉은뽕나무 0.50–10.19 g/kg 생과[10]; 이란 20개 유전자형 0.209–0.499 mg/g 생과[11]; 중국 연구진이 M. rubra로 표기한 오디에서 개별 정량(수치는 초록에 없음)[15]",
      activity_ko="열매 붉은·자주색의 주된 색소, 총 안토시아닌이 DPPH 항산화능과 함께 묶임(시험관)[10][11]", source=[10, 11, 15]),
 dict(name="Cyanidin 3-rutinoside", name_ko="시아니딘-3-루티노사이드", class_="안토시아닌", role="marker", part=FR,
      content_text="중국 연구진이 M. rubra로 표기한 오디에서 HPLC-DAD로 정량한 개별 안토시아닌 가운데 하나(수치는 초록에 없어 확인하지 못함)[15]",
      activity_ko="이 종에서 단독 활성은 확인하지 못함", source=[15]),
 dict(name="Resveratrol", name_ko="레스베라트롤", class_="스틸벤", role="bioactive", part="열매(전체)",
      content_text="인도 연구에서 Morus rubra로 표기한 오디 전체 50.61 µg/g 건물(80% 에탄올 추출, HPLC·MS)[14]",
      activity_ko="이 종에서 단독 활성은 확인하지 못함; 시료가 북미 자생 붉은뽕나무인지 확인하지 못함", source=[14]),
 dict(name="Ascorbic acid", name_ko="비타민 C(아스코르브산)", class_="비타민", role="nutrient", part=FR,
      content_text="튀르키예 붉은뽕나무 6.50–33.13 mg/100 g[10]; 이란 12.95–21.16 mg/100 mL 생과[11]",
      activity_ko="이란 연구에서 항산화능은 비타민 C보다 페놀 성분과 더 가깝게 연관됨[11]", source=[10, 11]),
 dict(name="gamma-Aminobutyric acid", name_ko="감마-아미노부티르산(GABA)", class_="비단백 아미노산", role="nutrient", part="열매(건조)",
      content_text="그늘 말림 붉은뽕나무 열매 336.17 mg/100 g(흰뽕나무 167.41 mg/100 g), LC-MS/MS[12]",
      activity_ko="이 종에서 단독 활성은 확인하지 못함", source=[12]),
 dict(name="Calcium", name_ko="칼슘", class_="무기질", role="nutrient", part="열매(건조)",
      content_text="그늘 말림 10,660 mg/kg, 65 °C 건조 9,238 mg/kg(ICP-OES)[12]",
      activity_ko="영양 성분", source=[12]),
 dict(name="Potassium", name_ko="칼륨", class_="무기질", role="nutrient", part=FR,
      content_text="말라티아 붉은뽕나무 열매 15.269 g/kg(조사한 오디 가운데 최고, ICP-AES; 생·건 기준은 초록에 없어 확인하지 못함)[13]",
      activity_ko="영양 성분", source=[13]),
]
for c in compounds:
    c["class"] = c.pop("class_")
compounds = [{k: c[k] for k in ("name","name_ko","class","role","part","content_text","activity_ko","source")} for c in compounds]

E = dict(instrument="", column="", mobile_phase="", gradient="", flow="", temp="", detection="", injection="",
         sample_prep="", standard="", linearity="", lod="", loq="", recovery="")
a1 = dict(E); a1.update(
 instrument="HPLC(UV 검출기·4원 용매 공급 장치를 갖춘 분석용 HPLC 시스템)",
 column="C18 역상 칼럼(Kromasil 100A C18, 250 × 4.60 mm, 5 µm)",
 mobile_phase="물과 아세토니트릴(A), 2.5% 포름산 함유(B) — 원문 표기 그대로",
 gradient="원문에 없음",
 flow="1 mL/min", temp="26 °C(수조)", detection="UV 280 nm", injection="20 µL",
 sample_prep="생과 1 g을 메탄올 5 mL로 6시간 추출한 여과액",
 standard="아미노벤조산·p-하이드록시벤조산·프로토카테큐산·(+)-카테킨·(−)-에피카테킨·루틴·카페인산·p-쿠마르산·클로로겐산")
a2 = dict(E)
a3 = dict(E); a3.update(
 instrument="UV-vis 분광광도계", detection="pH 1.0·pH 4.5 완충액에서 흡광도 측정(본문은 533·700 nm라 적고 계산식은 A520–A700을 씀)",
 sample_prep="생과를 믹서로 균질화해 −80 °C 보관 후 추출", standard="시아니딘-3-글루코사이드 몰흡광계수 29,600으로 환산")
assays = [
 dict(role="literature", compound="Rutin", compound_ko="루틴·(−)-에피카테킨 등 개별 페놀 9종", part="열매(생과, 튀르키예 히잔 붉은뽕나무 11개 유전자형)",
      content="루틴 9.34–38.51 mg/kg, 에피카테킨 0.84–99.74 mg/kg, 클로로겐산 0.81–57.97 mg/kg, 카페인산 0.25–44.39 mg/kg[10]",
      method="HPLC-UV", conditions=a1,
      rationale="붉은뽕나무 열매의 개별 페놀을 유전자형별로 정량한 자료이며, 루틴·총 안토시아닌·총페놀이 항산화능과 가장 가깝게 묶였다[10]. PMC 전문 Methods에서 조건을 옮겼으나 기울기·검량선·검출한계·회수율은 원문에 없다[10]. 시료는 튀르키예 재배 개체로 북미 자생 집단과 같은 계통인지는 확인하지 못함.",
      source=[10], url=pm(39554318), source_kind="paper"),
 dict(role="literature", compound="Cyanidin 3-glucoside", compound_ko="시아니딘-3-글루코사이드·시아니딘-3-루티노사이드 등 개별 안토시아닌", part="열매(중국 연구진이 Morus rubra로 표기한 오디)",
      content="개별 안토시아닌 함량 수치는 초록에 없어 확인하지 못함[15]",
      method="HPLC-DAD(pH 시차법 결합)", conditions=a2,
      rationale="오디의 붉은·자주색을 내는 주 색소를 표준품 없이 개별 정량하는 방법을 붉은뽕나무 이름의 오디로 검증한 연구다[15]. 전문 확인 못함 — 초록에는 C18 칼럼·단계 기울기, 검량 범위 10–5500 mg/L(r² 0.9972 이상), 검출한계 1–4 mg/L(S/N 5 이상), 상대 회수율 98.4–103.2%가 적혀 있으나 조건 칸은 비워 두었다[15]. 시료가 북미 자생 붉은뽕나무인지 확인하지 못함.",
      source=[15], url=pm(24964353), source_kind="paper"),
 dict(role="literature", compound="Cyanidin 3-glucoside", compound_ko="총 단량체 안토시아닌(시아니딘-3-글루코사이드 환산)", part="열매(생과, 튀르키예 히잔 붉은뽕나무)",
      content="0.50–10.19 g/kg 생과(시아니딘-3-글루코사이드 환산)[10]",
      method="pH 시차법(분광광도)", conditions=a3,
      rationale="오디 색과 항산화능을 대표하는 총량 지표로, 이란 연구도 같은 지표(0.209–0.499 mg/g 생과)를 썼다[10][11]. PMC 전문에서 조건을 옮겼으나 측정 파장 표기가 본문과 계산식에서 다르다[10].",
      source=[10, 11], url=pm(39554318), source_kind="paper"),
]

d = dict(slug="morus-rubra", name_ko="붉은뽕나무", name_en="Red mulberry", scientific_name="Morus rubra L.",
         aliases=["붉은뽕나무열매", "Red mulberry", "붉은뽕나무향(복합원료 U코드 원료명)"],
         sections=sections, compounds=compounds, markers=[], assays=assays, nutrients=[], production=[], world=[],
         gi=[], orgs=[], sources=src)
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in sections: print(s["key"], len(s["body"]))
