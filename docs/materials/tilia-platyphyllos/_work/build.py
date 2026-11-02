import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
A = "2026-11-02"
def pm(pmid): return f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
sources = [
 (1, "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 황금플라티필로스피나무꽃·황금플라티필로스피나무잎(Tilia platyphyllos; 이명 큰잎유럽피나무, 넓은잎피나무; Broad-leaved lime, Weeping lime), 사용가능, 사용가능부위: 잎, 꽃; 같은 속 Tilia 원료 행 대조 (로컬 원자료 I1020_20261013.json)", "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "식품의약품안전처", "2026-10-13"),
 (2, "HPLC-DAD and HPLC-ESI-MS analyses of Tiliae flos and its preparations. J Pharm Biomed Anal 2014;100:205-214. doi:10.1016/j.jpba.2014.08.010 — 초록 확인(Tilia platyphyllos 꽃차례의 탕제·침출액·팅크)", pm("25171484"), "Journal of Pharmaceutical and Biomedical Analysis", A),
 (3, "Tilia species (linden) exert anti-cancer effects on MIA PaCa-2 cells through the modulation of oxidative stress and inflammation. Sci Rep 2025;15:2317. doi:10.1038/s41598-025-86457-2 — PMC 전문 확인(HPLC-DAD 조건, 종·부위별 정량표)", pm("39833445"), "Scientific Reports", A),
 (4, "Contribution of the phenolic composition to the antioxidant, anti-inflammatory and antitumor potential of Equisetum giganteum L. and Tilia platyphyllos Scop. Food Funct 2017;8(3):975-984. doi:10.1039/c6fo01778a — 초록 확인", pm("28164200"), "Food & Function", A),
 (5, "Toxicological and anti-tumor effects of a linden extract (Tilia platyphyllos Scop.) in a HPV16-transgenic mouse model. Food Funct 2021;12(9):4005-4014. doi:10.1039/d1fo00225b — 초록 확인", pm("33978005"), "Food & Function", A),
 (6, "Novel Piperidine and 3,4-dihydro-2H-pyrrole Alkaloids from Tilia platyphyllos and Tilia cordata Flowers. Planta Med 2021;87(9):686-700. doi:10.1055/a-1340-0099 — 초록 확인", pm("33434940"), "Planta Medica", A),
 (7, "Comparative metabolomics of Tilia platyphyllos Scop. bracts during phenological development. Phytochemistry 2019;167:112084. doi:10.1016/j.phytochem.2019.112084 — 초록 확인", pm("31415913"), "Phytochemistry", A),
 (8, "Comparative evaluation of the flavonoid content in officinal Tiliae flos and Turkish lime species for quality assessment. J Pharm Biomed Anal 2001;26(1):111-121. doi:10.1016/s0731-7085(01)00351-x — 초록 확인", pm("11451648"), "Journal of Pharmaceutical and Biomedical Analysis", A),
 (9, "Nutlets of Tilia cordata Mill. and Tilia platyphyllos Scop. - Source of bioactive compounds. Food Chem 2021;346:128888. doi:10.1016/j.foodchem.2020.128888 — 초록 확인", pm("33385911"), "Food Chemistry", A),
 (10, "Hepatoprotective and antioxidant activity of linden (Tilia platyphyllos L.) infusion against ethanol-induced oxidative stress in rats. J Membr Biol 2014;247(2):181-188. doi:10.1007/s00232-013-9622-z — 초록 확인", pm("24337514"), "The Journal of Membrane Biology", A),
 (11, "Screening of selected food and medicinal plant extracts for pancreatic lipase inhibition. Phytother Res 2009;23(6):874-877. doi:10.1002/ptr.2718 — 초록 확인", pm("19107742"), "Phytotherapy Research", A),
 (12, "Potential antiviral effects of some native Iranian medicinal plants extracts and fractions against influenza A virus. BMC Complement Med Ther 2021;21:246. doi:10.1186/s12906-021-03423-x — 초록 확인", pm("34598697"), "BMC Complementary Medicine and Therapies", A),
 (13, "Characterization of microsatellite loci in Tilia platyphyllos (Malvaceae) and cross-amplification in related species. Appl Plant Sci 2013;1(4). doi:10.3732/apps.1200386 — 초록 확인", pm("25202533"), "Applications in Plant Sciences", A),
 (14, "Dendrological Secrets of the Pazaislis Monastery in Central Lithuania: DNA Markers and Morphology Reveal Tilia × europaea L. Hybrids of an Impressive Age. Plants 2023;12(20):3567. doi:10.3390/plants12203567 — PMC 전문 확인(전문 텍스트에서 일부 학명 이탤릭이 빠져 있어 종 대응은 문맥으로 판단)", pm("37896030"), "Plants (MDPI)", A),
 (15, "Phylogenomics of Western Eurasian Tilia: merging GBS datasets to place the Hyrcanian forest limes. BMC Plant Biol 2025;25:1370. doi:10.1186/s12870-025-07435-4 — 초록 확인", pm("41087876"), "BMC Plant Biology", A),
 (16, "Seasonal variability of mercury concentration in soils, buds and leaves of Acer platanoides and Tilia platyphyllos in central Poland. Environ Sci Pollut Res 2016;23(10):9614-9624. doi:10.1007/s11356-016-6179-2 — 초록 확인", pm("26846237"), "Environmental Science and Pollution Research", A),
 (17, "Sensitization to common allergens, especially pollens, among children with respiratory allergy in the Trakya region of Turkey. Asian Pac J Allergy Immunol 2004;22(4):183-190 — 초록 확인", pm("15783130"), "Asian Pacific Journal of Allergy and Immunology", A),
 (18, "A cross-cultural comparison of folk plant uses among Albanians, Bosniaks, Gorani and Turks living in south Kosovo. J Ethnobiol Ethnomed 2015;11:39. doi:10.1186/s13002-015-0023-5 — 초록 확인", pm("25964167"), "Journal of Ethnobiology and Ethnomedicine", A),
 (19, "[Consumption of medicinal herbs in patients attending a gastroenterology outpatient clinic]. Gastroenterol Hepatol 2004;27(4):244-249. doi:10.1016/s0210-5705(03)70453-1 — 초록 확인(스페인어 논문, 영문 초록)", pm("15056410"), "Gastroenterología y Hepatología", A),
 (20, "European Medicines Agency HMPC, Community herbal monograph on Tilia cordata Miller, Tilia platyphyllos Scop., Tilia x vulgaris Heyne or their mixtures, flos (EMA/HMPC/337066/2011) — 이 세션에서 EMA 사이트가 열리지 않아 원문은 확인하지 못했고 WebSearch 검색 결과 요약으로만 확인함", "https://www.ema.europa.eu/en/documents/herbal-monograph/final-community-herbal-monograph-tilia-cordata-miller-tilia-platyphyllos-scop-tilia-x-vulgaris-heyne_en.pdf", "European Medicines Agency", A),
 (21, "Gall-inducing Eriophyes tiliae stimulates the metabolism of Tilia platyphyllos leaves towards oxidative protection. Plant Physiol Biochem 2023;195:25-36. doi:10.1016/j.plaphy.2022.12.014 — 초록 확인", pm("36586397"), "Plant Physiology and Biochemistry", A),
 (22, "Ozone air pollution and foliar injury development on native plants of Switzerland. Environ Pollut 2003;125(1):41-52. doi:10.1016/s0269-7491(03)00085-x — 초록 확인", pm("12804826"), "Environmental Pollution", A),
 (23, "Two genetically related strains of Tuber borchii produce Tilia mycorrhizas with different morphological traits. Mycorrhiza 2003;13(2):107-115. doi:10.1007/s00572-002-0220-7 — 초록 확인", pm("12682833"), "Mycorrhiza", A),
 (24, "Plant regeneration by somatic embryogenesis from cultured immature embryos of oak (Quercus robur L.) and linden (Tilia cordata Mill.). Plant Cell Rep 1990;9(7):398-401. doi:10.1007/BF00232408 — 초록 확인", pm("24227064"), "Plant Cell Reports", A),
 (25, "Characterization of the Tuber borchii nitrate reductase gene and its role in ectomycorrhizae. Mol Genet Genomics 2003;269(6):807-816. doi:10.1007/s00438-003-0894-3 — 초록 확인", pm("12898221"), "Molecular Genetics and Genomics", A),
]
S = [{"n": n, "title": t, "url": u, "publisher": p, "accessed": a} for n, t, u, p, a in sources]

sections = [
 {"key": "overview", "title": "한눈에 보기", "body":
  "황금플라티필로스피나무(Tilia platyphyllos)는 유럽 중부·남부가 원산인 넓은잎 낙엽 교목으로, 영어로는 large-leaved lime 또는 linden이라 부른다[5, 11]. 식약처 「식품원료 목록」에는 원료명 '황금플라티필로스피나무꽃'과 '황금플라티필로스피나무잎'이 학명 Tilia platyphyllos, 이명 큰잎유럽피나무·넓은잎피나무, 영어명 Broad-leaved lime, Weeping lime으로 올라 있다[1]. 두 원료 모두 식품에 쓸 수 있는 원료(사용가능)이며 사용 조건은 '사용가능부위 : 잎, 꽃'이어서 잎과 꽃만 쓸 수 있다[1]. 목록 자료에서 이 종을 원재료로 하는 건강기능식품 고시형 원료는 확인되지 않는다[1].\n\n"
  "유럽 약용식물 문헌에서 '린덴꽃(Tiliae flos)'은 Tilia cordata·Tilia platyphyllos·두 종의 잡종 또는 그 혼합물의 포엽 달린 꽃차례를 말린 것으로, 감기 증상과 정신적 긴장 완화에 전통적으로 써 왔다[6, 20]. 따라서 린덴꽃 자료는 여러 종이 섞인 것이 많아, 이 자료에서는 이 종으로 분명히 밝힌 연구만 따로 모았다[2, 3, 6]. 튀르키예산 이 종의 꽃 추출물에서는 틸리로사이드·이소퀘르시트린·아스트라갈린 같은 플라보노이드 배당체가 정량되었다[3]. 항산화·항염·암세포 억제·지방 분해효소 억제 같은 결과는 모두 시험관이나 동물 실험이며, 이 종만으로 한 사람 대상 임상시험은 확인하지 못했다[3, 4, 11]."},
 {"key": "history", "title": "이용의 역사", "body":
  "린덴꽃은 꽃과 포엽을 함께 말려 차로 우려 마시는 유럽의 전통 약초로, 감기 증상과 정신적 긴장을 덜기 위해 써 왔다[6]. 유럽의약품청(EMA) 약초위원회는 Tilia cordata·Tilia platyphyllos·Tilia × vulgaris의 꽃 또는 그 혼합물을 하나의 전통 약초 성분으로 묶어 단행 평가서(monograph)를 냈고, 감기 증상 완화가 전통적 용도로 들어 있는 것으로 검색 결과에서 확인했다(원문은 확인하지 못함)[20].\n\n"
  "남부 코소보의 알바니아인·보스니아인·고라니인·튀르크인 노인 139명을 면담한 민족식물학 조사에서 이 종은 서양톱풀·서양딱총나무·서양쐐기풀 등과 함께 가장 중요한 약용 식물 가운데 하나로 꼽혔다[18]. 스페인 발렌시아 지역 한 병원 소화기 외래 환자 539명 조사에서는 약초 이용자가 쓴 57가지 식물 가운데 이 종이 6.5%로 두 번째로 많이 쓰였다[19]. 튀르키예 연구진은 린덴 꽃·꽃차례를 끓는 물에 우린 차가 감기와 기침에 전통적으로 쓰였다고 정리했다[3]. 국내에 이 종이 들어온 경위나 국내 전통 이용 기록은 확인하지 못했다."},
 {"key": "biology", "title": "식물학적 특징", "body":
  "이 종은 아욱과(Malvaceae) 피나무속의 넓은잎 낙엽 교목이다[5, 13]. 작은잎라임(Tilia cordata)과 함께 유럽 대부분 나라에 자생하며 두 종을 합친 분포는 핀란드 남부에서 이탈리아 남부와 캅카스까지 이른다[14]. 피나무속 종들은 어긋나는 심장형 잎과 톱니 있는 잎 가장자리를 가지며, 노란빛 꽃이 6–7월에 피고 꽃대가 길쭉한 포엽(bract)에 중간까지 붙어 자란다[3].\n\n"
  "리투아니아의 형태 비교 연구에서 큰잎 계통은 올해 자란 가지·잎·잎자루에 희고 뻣뻣한 긴 털이 뚜렷하고, 잎 앞면 맥 위에도 털이 있으며, 잎자루에 털이 있는 점으로 다른 종과 구별되었다[14]. 같은 연구에서 이 계통은 꽃이 가장 크고, 열매(소견과)가 가장 크고 단단하며 세로 능선이 뚜렷했다[14]. 전문 텍스트에서 학명 일부가 빠져 있어, 이 형태 특징의 종 대응은 문맥으로 판단한 것이다[14]. 유전체 분석에서 이 종은 이배체로 보고되었다[15]. 포엽의 대사물은 포엽이 나온 뒤 개화기·결실기를 거치며 크게 바뀌고, 어린 포엽에 플라보놀 배당체와 카테킨이 많았다[7]. 잎에는 혹응애(Eriophyes tiliae)가 붉은 벌레혹을 만들며, 벌레혹은 정상 잎보다 안토시아닌·폴리페놀이 많았다[21]."},
 {"key": "related_species", "title": "가까운 종과 혼동", "body":
  "식약처 「식품원료 목록」에는 피나무속 원료가 여럿 있으며, 작은잎라임(Tilia cordata), 라임블로섬(Tilia x europea), 피나무(Tilia spp.), Silver lime(Tilia tomentosa), 찰피나무(Tilia mandshurica), 염주나무(Tilia megaphylla), 뽕잎피나무(Tilia taquetii) 등이 각각 따로 올라 있다[1]. 이들은 대부분 잎·꽃이 사용가능이지만, 라임블로섬은 나무껍질이 '제한적사용' 부위로 따로 올라 있어 이 종의 조건과 다르다[1]. 라임블로섬, 곧 유럽피나무(Tilia × europaea)는 작은잎라임과 이 종이 자연 교잡해 생긴 잡종이다[14].\n\n"
  "같은 방법으로 분석한 튀르키예 시료에서 작은잎라임 포엽은 프로토카테큐산이 30.26 mg/g 추출물이었으나 이 종 포엽은 2.03 mg/g 추출물이었고, 하이페로사이드는 작은잎라임 포엽에서 검출되었지만 이 종에서는 검출되지 않았다[3]. 꽃·포엽·잎의 HPLC 플라보노이드 지문은 종과 부위마다 달라 린덴꽃 원료의 혼입 판별에 쓸 수 있다는 보고가 있다[8]. 이란에서 이 종으로 보고되던 개체들이 유전체 분석에서는 Tilia dasystyla subsp. caucasica로 밝혀진 것처럼, 피나무속은 이름 혼동이 잦다[15]. 따라서 '린덴꽃' 제품이나 혼합 시료 자료를 이 종의 결과로 그대로 옮겨서는 안 된다[6, 8]."},
 {"key": "cultivation", "title": "재배와 생산", "body":
  "국내에서 이 종을 재배하거나 꽃·잎을 생산한 통계는 확인하지 못했으며, 특용작물 생산실적·농작물 생산 통계 자료에도 피나무류 품목이 없어 생산량은 확인하지 못함으로 둔다. 유럽에서는 피나무류가 공원·가로수로 오래 심어졌고, 건조·오염·가지치기에 강한 나무로 꼽힌다[14]. 스위스 개방형 챔버 실험에서 이 종은 오존 노출 시 잎에 눈에 보이는 피해가 나타난 11종 가운데 하나였다[22].\n\n"
  "번식과 관련해서는 미숙 접합배에서 얻은 배발생 배양으로 이 종의 체세포배와 어린 식물을 재생한 보고가 있다[24]. 이 종의 뿌리는 송로버섯(Tuber borchii)과 외생균근을 잘 만들어, 균근 형성 연구의 기주 식물로 쓰였다[23, 25]. 약용 원료로는 개화기에 꽃과 포엽을 거두는데, 포엽 성분은 개화 전후로 크게 달라 수확 시기가 품질에 영향을 준다[7]. 집단 유전 연구를 위해 이 종에서 마이크로새틀라이트 표지가 개발되어 있다[13]."},
 {"key": "processing", "title": "가공과 이용", "body":
  "이 종의 꽃차례로 만든 탕제·침출액·팅크를 HPLC-DAD·HPLC-ESI-MS·NMR로 분석한 연구에서 31가지 성분이 확인되었고, 플라보노이드 외에 단순 페놀과 에피카테킨 유도체인 저분자 프로시아니딘이 많았다[2]. 같은 연구는 플라보노이드를 지표성분으로, 정유 함량을 보조 품질 기준으로 삼는 린덴꽃 품질관리를 위해 검증된 HPLC 방법을 제안했다[2]. 꽃에 든 새 알칼로이드(틸리인·틸리아민·틸라세틴)는 아세톤·물 혼합액에서 가장 잘 추출되었고, 에탄올이나 전통적으로 쓰는 뜨거운 물 추출액에서도 검출되었다[6].\n\n"
  "실험용 추출물은 말린 꽃·포엽·꽃차례 가루를 80% 에탄올로 30분간 초음파 추출한 뒤 농축·동결건조해 만들었다[3]. 이 종 추출물은 시험관에서 돼지 췌장 리파아제를 강하게 억제한 소수의 식물 추출물 가운데 하나였다[11]. 꽃 80% 메탄올 추출물은 인플루엔자 A 바이러스 시험에서 가장 효과적인 시료로 꼽히지 않았다[12]. 열매(소견과) 기름은 식물스테롤과 토코페롤이 많다는 보고가 있으나, 열매는 식약처 목록의 사용가능부위(잎, 꽃)가 아니다[1, 9]. 국내에서 이 원료로 만든 제품의 생산실적은 확인하지 못했다."},
 {"key": "genetics", "title": "유전·계통", "body":
  "프랑스의 두 집단에서 이 종용 마이크로새틀라이트 표지 15개가 개발되었고, 좌위당 대립유전자는 1–15개(평균 8.96개), 관찰·기대 이형접합도는 0.71과 0.70이었다[13]. 이 가운데 12개 좌위는 피나무속 23종에서도 다형성을 보여, 종 간 교잡과 계통지리 연구에 쓸 수 있다[13]. 리투아니아 연구에서는 Tc8 좌위가 작은잎라임(140 bp 대립유전자)과 이 종 계통(160 bp 이상)을 가르는 표지로 쓰였고, 유럽피나무 잡종은 두 대립유전자를 모두 가졌다[14].\n\n"
  "서유라시아 피나무속을 GBS(유전체 축소 서열분석)로 분석한 연구에서 이 종과 작은잎라임은 모두 이배체였고, 계통 분석에서 종들이 뚜렷이 갈렸다[15]. 같은 연구에서 이란에서 이 종으로 기록되던 개체들은 사배체인 Tilia dasystyla subsp. caucasica로 밝혀졌다[15]. 송로버섯 균근 연구 과정에서 이 종의 질산환원효소 cDNA(tpnr1)가 클로닝되었고, 공생이 이루어지면 그 전사가 줄었다[25]. 이 종의 엽록체·핵 전체 유전체 해독 결과는 확인하지 못했다."},
 {"key": "safety", "title": "안전성", "body":
  "식약처 「식품원료 목록」에서 이 종의 꽃과 잎은 사용가능 원료이며, 다른 부위는 목록에 없다[1]. 유럽의약품청 단행 평가서에는 알려진 이상반응이 '없음'으로 적혀 있다는 내용을 검색 결과 요약으로만 확인했다(원문 미확인)[20]. HPV16 유전자이식 생쥐에게 이 종 하이드로에탄올 추출물을 마리당 4.5 mg/10 mL 물에 녹여 33일간 먹인 실험에서 신장·간 조직, 생화학, 산화 스트레스 지표에 손상이 없어 동물에서의 안전성은 양호했다[5]. 반면 쥐에게 2% 꽃 침출액을 먹인 실험에서는 대조군보다 혈청 AST·LDH가 높아졌고, 에탄올로 생긴 지질 과산화도 되돌리지 못했다[10].\n\n"
  "폴란드 포즈난 도심의 이 종 잎에서 수은은 평균 50.4 ± 15.8 ng/g(범위 23.1–88.7 ng/g)으로 측정되었고, 주로 대기에서 온 것으로 해석되었다[16]. 따라서 도로변·도심에서 딴 잎은 환경오염물질을 고려해야 한다[16]. 이 종의 꽃가루는 튀르키예 호흡기 알레르기 어린이 피부반응 검사 항원에 포함되었다[17]. 꽃·포엽·잎에서 새 알칼로이드가 보고되었지만 그 독성은 아직 밝혀지지 않았다[6]. 임신·수유 중 안전성과 국내 공공기관의 알레르기·잔류 정보는 확인하지 못했다."},
]

compounds = [
 {"name": "Tiliroside", "name_ko": "틸리로사이드", "class": "플라보노이드 배당체(캠페롤 p-쿠마로일 글루코사이드)", "role": "marker", "part": "꽃·포엽·꽃차례",
  "content_text": "꽃 5.57 ± 0.06, 포엽 3.12 ± 0.05, 꽃차례 4.36 ± 0.06 mg/g 하이드로에탄올 추출물(HPLC-DAD, 튀르키예산)[3]", "activity_ko": "튀르키예 4종 비교에서 종을 가르는 유의 변수로 나타남; 사람 효과는 확인하지 못함[3]", "source": [3]},
 {"name": "Isoquercitrin", "name_ko": "이소퀘르시트린", "class": "플라보놀 배당체", "role": "marker", "part": "꽃·포엽·꽃차례",
  "content_text": "꽃 7.24 ± 0.15, 포엽 2.12 ± 0.03, 꽃차례 5.41 ± 0.10 mg/g 추출물[3]", "activity_ko": "추출물의 항산화 작용에 기여하는 성분으로 논의됨(시험관)[3]", "source": [3]},
 {"name": "Astragalin", "name_ko": "아스트라갈린", "class": "플라보놀 배당체", "role": "bioactive", "part": "꽃·포엽·꽃차례",
  "content_text": "꽃 6.40 ± 0.05, 포엽 1.37 ± 0.004, 꽃차례 3.74 ± 0.03 mg/g 추출물[3]", "activity_ko": "이 종 추출물에서의 단독 활성은 확인하지 못함[3]", "source": [3]},
 {"name": "Quercitrin", "name_ko": "퀘르시트린", "class": "플라보놀 배당체", "role": "bioactive", "part": "꽃·포엽·꽃차례",
  "content_text": "꽃 3.43 ± 0.03, 포엽 1.07 ± 0.01, 꽃차례 2.32 ± 0.02 mg/g 추출물; 같은 분석에서 하이페로사이드는 이 종 모든 부위에서 불검출[3]", "activity_ko": "4종 전체 자료에서 함량이 높을수록 췌장암 세포 IC50이 낮아지는 상관(시험관)[3]", "source": [3]},
 {"name": "Protocatechuic acid", "name_ko": "프로토카테큐산", "class": "페놀산", "role": "bioactive", "part": "꽃·포엽·꽃차례(지상부 추출물)",
  "content_text": "꽃 3.12 ± 0.10, 포엽 2.03 ± 0.06, 꽃차례 2.68 ± 0.09 mg/g 추출물[3]; 하이드로에탄올 추출물에서 가장 많은 페놀산[4, 5]", "activity_ko": "추출물의 항산화·항염 시험관 활성과 양의 상관[4]", "source": [3, 4, 5]},
 {"name": "Epicatechin", "name_ko": "(−)-에피카테킨", "class": "플라반-3-올", "role": "bioactive", "part": "꽃차례·추출물",
  "content_text": "하이드로에탄올 추출물에서 가장 많은 플라보노이드(수치는 초록에 없음)[4, 5]; 꽃차례 제제의 프로시아니딘은 에피카테킨 유도체[2]", "activity_ko": "추출물 플라보노이드 총량 50.4 mg/g, 페놀산 11.65 mg/g 추출물로 항산화 활성과 상관[4]", "source": [2, 4, 5]},
 {"name": "Procyanidin", "name_ko": "프로시아니딘(저분자 올리고머)", "class": "축합형 탄닌", "role": "bioactive", "part": "꽃차례(탕제·침출액·팅크)",
  "content_text": "저분자 프로시아니딘과 그 올리고머가 검출됨(개별 함량은 초록에 없음)[2]", "activity_ko": "확인하지 못함[2]", "source": [2]},
 {"name": "Tiliine A", "name_ko": "틸리인 A", "class": "3,4-다이하이드로-2H-피롤 알칼로이드(하이드로퀴논 글루코사이드 결합)", "role": "bioactive", "part": "꽃·포엽·잎",
  "content_text": "이 종 꽃·포엽·잎에서 HPLC-ESI-qTOF로 정량, 틸리인 A·B와 틸라세틴 A·B가 주성분(수치는 초록에 없음)[6]", "activity_ko": "활성·독성은 확인하지 못함[6]", "source": [6]},
 {"name": "Tilacetine A", "name_ko": "틸라세틴 A", "class": "피페리딘 알칼로이드(틸리아민의 3-O-아세틸 유도체)", "role": "bioactive", "part": "꽃·포엽·잎",
  "content_text": "주요 알칼로이드 가운데 하나로 검출, 뜨거운 물 추출액에도 들어 있음[6]", "activity_ko": "확인하지 못함[6]", "source": [6]},
 {"name": "Chlorogenic acid", "name_ko": "클로로젠산", "class": "퀸산 유도체(페놀산)", "role": "bioactive", "part": "포엽",
  "content_text": "포엽 대사체 분석에서 정량·추정 동정된 퀸산 유도체(수치는 초록에 없음)[7]", "activity_ko": "확인하지 못함[7]", "source": [7]},
 {"name": "Fraxin", "name_ko": "프락신", "class": "쿠마린 배당체", "role": "bioactive", "part": "포엽",
  "content_text": "열매가 자라는 후기 포엽에서 더 많아짐(수치는 초록에 없음)[7]", "activity_ko": "확인하지 못함[7]", "source": [7]},
 {"name": "Squalene", "name_ko": "스쿠알렌", "class": "트라이터펜 탄화수소", "role": "nutrient", "part": "열매(소견과) 기름 — 식품 사용가능부위 아님",
  "content_text": "이 종 소견과 기름 607 mg/100 g[9]", "activity_ko": "열매는 식약처 목록 사용가능부위가 아님[1, 9]", "source": [1, 9]},
 {"name": "Linoleic acid", "name_ko": "리놀레산", "class": "다가불포화지방산", "role": "nutrient", "part": "열매(소견과) 기름 — 식품 사용가능부위 아님",
  "content_text": "이 종 소견과 기름 지방산의 54.1%; 올레산 22.2%, 팔미트산 11.8%[9]", "activity_ko": "영양 성분(이 종 기름의 비타민 E는 α-토코페롤 당량 50.6 mg/100 g)[9]", "source": [9]},
 {"name": "beta-Sitosterol", "name_ko": "β-시토스테롤", "class": "식물스테롤", "role": "nutrient", "part": "열매(소견과) 기름 — 식품 사용가능부위 아님",
  "content_text": "린덴 씨 기름 식물스테롤 2–2.5 g/100 g 가운데 80–83%(두 종 합친 범위)[9]", "activity_ko": "확인하지 못함[9]", "source": [9]},
]

cond_sr = {"instrument": "Agilent 1260 Infinity HPLC(진공 탈기기·자동시료주입기·온도조절 칼럼부·4원 펌프), DAD, Agilent ChemStation",
  "column": "Agilent Zorbax Plus C18, 4.6 × 250 mm, 5 μm",
  "mobile_phase": "A: 0.1% 인산 초순수, B: 아세토니트릴",
  "gradient": "A-B 85–15%(0–3분), 82–18%(3–11분), 80–20%(11–16분), 70–30%(16–22분), 50–50%(22–25분), 20–80%(25–26분), 85–15%(26–30분)",
  "flow": "1 mL/min", "temp": "25 °C", "detection": "", "injection": "10 µL(3회 반복 주입)",
  "sample_prep": "말린 꽃·포엽·꽃차례(꽃:포엽 1:1) 가루 5 g을 80% 에탄올로 30분 초음파 추출, 여과지·0.45 μm 필터 여과, 40 °C 감압 농축 후 동결건조; 80% 에탄올에 20 mg/mL로 녹여 희석",
  "standard": "프로토카테큐산·하이페로사이드·이소퀘르시트린·아스트라갈린·퀘르시트린·틸리로사이드 표준품(메탄올 300 µg/mL 원액)",
  "linearity": "", "lod": "", "loq": "", "recovery": ""}
c1 = dict(cond_sr); c1["detection"] = "DAD 320 nm(틸리로사이드)"
c2 = dict(cond_sr); c2["detection"] = "DAD 260 nm(이소퀘르시트린; 프로토카테큐산·하이페로사이드·퀘르시트린도 260 nm, 아스트라갈린 265 nm)"
assays = [
 {"role": "literature", "compound": "Tiliroside", "compound_ko": "틸리로사이드", "part": "꽃·포엽·꽃차례(튀르키예, 개화기 채집)",
  "content": "꽃 5.57 ± 0.06, 포엽 3.12 ± 0.05, 꽃차례 4.36 ± 0.06 mg/g 하이드로에탄올 추출물(n = 3)[3]",
  "method": "HPLC-DAD(기울기 용리)", "conditions": c1,
  "rationale": "피나무속 꽃에 특징적인 캠페롤 쿠마로일 배당체로, 저자들이 지표성분(marker components)으로 정량했고 종 구별 변수로도 유의했다; 직선성·검출한계·정량한계·회수율은 보충 표에 있어 확인하지 못함[3].",
  "source": [3], "url": pm("39833445"), "source_kind": "paper"},
 {"role": "literature", "compound": "Isoquercitrin", "compound_ko": "이소퀘르시트린", "part": "꽃·포엽·꽃차례(튀르키예, 개화기 채집)",
  "content": "꽃 7.24 ± 0.15, 포엽 2.12 ± 0.03, 꽃차례 5.41 ± 0.10 mg/g 추출물; 아스트라갈린 꽃 6.40 ± 0.05 mg/g[3]",
  "method": "HPLC-DAD(기울기 용리)", "conditions": c2,
  "rationale": "이 종 꽃에서 가장 많이 정량된 플라보놀 배당체로 함께 지표성분으로 쓰였다; 검증 자료는 보충 표에 있어 확인하지 못함[3].",
  "source": [3], "url": pm("39833445"), "source_kind": "paper"},
 {"role": "literature", "compound": "Procyanidins and flavonoids (Tiliae flos markers)", "compound_ko": "플라보노이드·프로시아니딘", "part": "꽃차례(탕제·침출액·팅크)",
  "content": "31가지 성분 검출·동정, 정량값은 초록에 없음[2]",
  "method": "HPLC-DAD, HPLC-ESI-MS(ICH 기준 검증)", "conditions": {"instrument": "", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "", "injection": "", "sample_prep": "", "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "이 종 꽃차례 제제의 품질관리용으로 ICH 지침에 맞춰 검증한 방법이며 플라보노이드를 린덴꽃의 지표성분으로 본다; 전문 확인 못함[2].",
  "source": [2], "url": pm("25171484"), "source_kind": "paper"},
 {"role": "literature", "compound": "Tiliine A", "compound_ko": "틸리인 A(알칼로이드)", "part": "꽃·포엽·잎",
  "content": "6가지 알칼로이드가 이 종 꽃·포엽·잎에서 모두 검출, 틸리인 A·B와 틸라세틴 A·B가 주성분(수치는 초록에 없음)[6]",
  "method": "HPLC-ESI-qTOF", "conditions": {"instrument": "", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "", "injection": "", "sample_prep": "아세톤/물이 최적 추출 용매, 에탄올·에탄올/물·뜨거운 물로도 추출됨", "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "피나무속 꽃·잎에서 처음 보고된 고유 알칼로이드로, 잎(식품 사용가능부위)까지 정량한 드문 자료다; 전문 확인 못함[6].",
  "source": [6], "url": pm("33434940"), "source_kind": "paper"},
]

d = {"slug": "tilia-platyphyllos", "name_ko": "황금플라티필로스피나무",
     "name_en": "Large-leaved lime (Broad-leaved lime, Weeping lime)",
     "scientific_name": "Tilia platyphyllos Scop.",
     "aliases": ["황금플라티필로스피나무꽃", "황금플라티필로스피나무잎", "큰잎유럽피나무", "넓은잎피나무", "Broad-leaved lime", "Weeping lime", "Large-leaved lime", "Large-leaved linden"],
     "sections": sections, "compounds": compounds, "markers": [], "nutrients": [], "assays": assays,
     "production": [], "world": [], "gi": [], "orgs": [], "sources": S}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in sections: print(s["key"], len(s["body"]))
