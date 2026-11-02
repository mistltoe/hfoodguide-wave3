import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
A = "2026-11-02"
def pm(n, title, pmid, journal, pmc=None, doi=None):
    url = f"https://pmc.ncbi.nlm.nih.gov/articles/{pmc}/" if pmc else f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
    t = f"{title} (PMID {pmid}" + (f", doi:{doi}" if doi else "") + ")" + (" — 전문 확인" if pmc and n in FULL else " — 초록 확인")
    return {"n": n, "title": t, "url": url, "publisher": journal + (" (PMC)" if pmc else " (PubMed)"), "accessed": A}
FULL = {10, 11, 16}
S = [
 {"n": 1, "title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 달개비·달개비분말·달개비추출액(Commelina communis L., 식품원료 A코드, '제한적사용', 부위 '전체', 사용조건 칸 비어 있음), 달개비순('사용가능', '사용가능부위 : 순') 행, 흰닭의장풀순(Commelina communis var. albida, '사용가능') 및 같은 속 덩이줄기·잎 원료 행 (로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json)", "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
 pm(2, "alpha-Glucosidase inhibitors from Commelina communis. Planta Med 1999;65(5):437-9", "10418330", "Planta Medica", doi="10.1055/s-2006-960803"),
 pm(3, "Anti-hyperglycemic activity of Commelina communis L.: inhibition of alpha-glucosidase. Diabetes Res Clin Pract 2004;66 Suppl 1:S149-55", "15563967", "Diabetes Research and Clinical Practice", doi="10.1016/j.diabres.2003.08.015"),
 pm(4, "Antioxidant constituents in the dayflower (Commelina communis L.) and their alpha-glucosidase-inhibitory activity. J Nat Med 2008;62(3):349-53", "18409066", "Journal of Natural Medicines", doi="10.1007/s11418-008-0244-1"),
 pm(5, "Biosynthesis of 1-deoxynojirimycin in Commelina communis: a difference between the microorganisms and plants. Phytochemistry 2004;65(19):2661-5", "15464153", "Phytochemistry", doi="10.1016/j.phytochem.2004.08.013"),
 pm(6, "[Quality evaluation of Commelina communis medicinal materials from different origins based on content of four alkaloid components combined with chemometrics]. Zhongguo Zhong Yao Za Zhi 2025;50(9):2422-2431", "40461198", "China Journal of Chinese Materia Medica", doi="10.19540/j.cnki.cjcmm.20250217.102"),
 pm(7, "[Quality evaluation of Commelina communis from different origins based on multicomponent content determination combined with chemometrics]. Zhongguo Zhong Yao Za Zhi 2023;48(2):356-365", "36725225", "China Journal of Chinese Materia Medica", doi="10.19540/j.cnki.cjcmm.20221015.102"),
 pm(8, "Simultaneous Qualitative and Quantitative Study of Main Compounds in Commelina communis Linn. by UHPLC-Q-TOF-MS-MS and HPLC-ESI-MS-MS. J Chromatogr Sci 2018;56(7):582-594", "29659750", "Journal of Chromatographic Science", doi="10.1093/chromsci/bmy030"),
 pm(9, "[Chemical constituents from Commelina communis]. Zhongguo Zhong Yao Za Zhi 2013;38(19):3304-8", "24422397", "China Journal of Chinese Materia Medica"),
 pm(10, "Suppression of Fatty Acid and Triglyceride Synthesis by the Flavonoid Orientin through Decrease of C/EBPδ Expression and Inhibition of PI3K/Akt-FOXO1 Signaling in Adipocytes. Nutrients 2018;10(2):130", "29373533", "Nutrients (MDPI)", pmc="PMC5852706", doi="10.3390/nu10020130"),
 pm(11, "Treatment with Commelina communis Extract Exerts Anti-inflammatory Effects in Murine Macrophages via Modulation of the Nuclear Factor-κB Pathway. Mediators Inflamm 2022:2028514", "35250385", "Mediators of Inflammation (Hindawi)", pmc="PMC8894075", doi="10.1155/2022/2028514"),
 pm(12, "Anti-influenza-virus activity of total alkaloids from Commelina communis L. Arch Virol 2009;154(11):1837-40", "19774337", "Archives of Virology", doi="10.1007/s00705-009-0503-9"),
 pm(13, "Protective effect of homonojirimycin from Commelina communis (dayflower) on influenza virus infection in mice. Phytomedicine 2013;20(11):964-8", "23746956", "Phytomedicine", doi="10.1016/j.phymed.2013.04.009"),
 pm(14, "Homonojirimycin, an alkaloid from dayflower inhibits the growth of influenza A virus in vitro. Acta Virol 2013;57(1):85-6", "23530829", "Acta Virologica", doi="10.4149/av_2013_01_85"),
 pm(15, "Structure of commelinin, a blue complex pigment from the blue flowers of Commelina communis. Proc Jpn Acad Ser B 2008;84(10):452-6", "19075517", "Proceedings of the Japan Academy, Ser. B", pmc="PMC3720548", doi="10.2183/pjab.84.452"),
 pm(16, "Tracing the genealogy of research on the mechanism of blue flower coloration by anthocyanin based on Keita Shibata's work. Proc Jpn Acad Ser B 2024;100(8):446-464", "39401899", "Proceedings of the Japan Academy, Ser. B", pmc="PMC11535004", doi="10.2183/pjab.100.028"),
 pm(17, "Responses of antioxidative enzymes to accumulation of copper in a copper hyperaccumulator of Commelina communis. Arch Environ Contam Toxicol 2004;47(2):185-92", "15386143", "Archives of Environmental Contamination and Toxicology", doi="10.1007/s00244-004-2222-2"),
 pm(18, "Geography Plays a More Important Role than Soil Composition on Structuring Genetic Variation of Pseudometallophyte Commelina communis. Front Plant Sci 2016;7:1085", "27499758", "Frontiers in Plant Science", pmc="PMC4956667", doi="10.3389/fpls.2016.01085"),
 pm(19, "The chloroplast genome sequence of Commelina communis (Commelinaceae). Mitochondrial DNA B Resour 2019;4(2):2631-2632", "33365657", "Mitochondrial DNA Part B", pmc="PMC7706858", doi="10.1080/23802359.2019.1642153"),
 pm(20, "Allopolyploidy enhances survival advantages for urban environments in the native plant genus Commelina. Ann Bot 2024;134(6):1055-1066", "39175163", "Annals of Botany", pmc="PMC11687629", doi="10.1093/aob/mcae141"),
 pm(21, "Does urbanization promote floral diversification? Implications from changes in herkogamy with pollinator availability in an urban-rural area. Am Nat 2014;184(2):258-67", "25058285", "The American Naturalist", doi="10.1086/676855"),
 pm(22, "Does a coexisting congener of a mixed mating species affect the genetic structure and selfing rate via reproductive interference? Oecologia 2024;206(1-2):37-45", "39174734", "Oecologia", pmc="PMC11489367", doi="10.1007/s00442-024-05607-x"),
 pm(23, "High Antioxidant Ability Confer Resistance to Atrazine in Commelina communis L. Plants (Basel) 2021;10(12):2685", "34961156", "Plants (MDPI)", pmc="PMC8707497", doi="10.3390/plants10122685"),
 pm(24, "PsbA gene over-expression and enhanced metabolism conferring resistance to atrazine in Commelina communis. Pestic Biochem Physiol 2022;188:105260", "36464365", "Pesticide Biochemistry and Physiology", doi="10.1016/j.pestbp.2022.105260"),
 pm(25, "Selection and validation of reference genes for qRT-PCR normalization in dayflower (Commelina communis) based on the transcriptome profiling. BMC Plant Biol 2024;24(1):1131", "39592924", "BMC Plant Biology", pmc="PMC11600965", doi="10.1186/s12870-024-05853-4"),
 pm(26, "ABA signaling in stomatal guard cells: lessons from Commelina and Vicia. J Plant Res 2011;124(4):477-87", "21706139", "Journal of Plant Research", doi="10.1007/s10265-011-0435-9"),
 pm(27, "The Association of Severe Epidemics of Cucumber Mosaic in Commercial Fields of Pepper and Tobacco in North Florida with Inoculum in Commelina benghalensis and C. communis. Plant Dis 1998;82(10):1172", "30856786", "Plant Disease", doi="10.1094/PDIS.1998.82.10.1172A"),
 pm(28, "Structural characterization and Bacteroides proliferation promotion activity of a novel homogeneous arabinoglucuronoxylan from Commelina communis L. Bioorg Chem 2024;153:107790", "39241582", "Bioorganic Chemistry", doi="10.1016/j.bioorg.2024.107790"),
 pm(29, "Isolation, structural characterization, and anticomplement activity of two glycoproteins derived from Commelina communis L. Int J Biol Macromol 2025;328(Pt 2):147706", "40962098", "International Journal of Biological Macromolecules", doi="10.1016/j.ijbiomac.2025.147706"),
 pm(30, "Multi-metabolomics and intestine microbiome analysis: YZC extract ameliorates septic-ALI by modulating intestine microbiota to reduce TMAO/NLRP3 signaling. Phytomedicine 2024;130:155345", "38810555", "Phytomedicine", doi="10.1016/j.phymed.2024.155345"),
 pm(31, "Antibacterial Components and Modes of the Methanol-Phase Extract from Commelina communis Linn. Plants (Basel) 2023;12(4):890", "36840240", "Plants (MDPI)", pmc="PMC9966474", doi="10.3390/plants12040890"),
 pm(32, "Commelina benghalensis (Wandering Jew) Linn exhibits abortifacient potentials and hepatotoxicity in pregnant Wistar rats via elevating indicators of oxidative stress and activating proinflammatory cytokines. J Ethnopharmacol 2022;300:115803", "36216194", "Journal of Ethnopharmacology", doi="10.1016/j.jep.2022.115803"),
 pm(33, "Integrating liquid chromatography mass spectrometry into an analytical protocol for the identification of organic colorants in Japanese woodblock prints. Sci Rep 2020;10(1):20921", "33262422", "Scientific Reports", pmc="PMC7708457", doi="10.1038/s41598-020-77959-2"),
 pm(34, "1-Deoxynojirimycin: Occurrence, Extraction, Chemistry, Oral Pharmacokinetics, Biological Activities and In Silico Target Fishing. Molecules 2016;21(11):1600", "27886092", "Molecules (MDPI)", pmc="PMC6273535", doi="10.3390/molecules21111600"),
 pm(35, "Aluminum and iron interactions in Commelina communis: additive chloroplast toxicity versus synergistic internal and rhizosphere detoxification. Protoplasma 2026", "42120778", "Protoplasma", doi="10.1007/s00709-026-02210-0"),
]
FULL |= {34}
# re-run title suffix for full-text ones
for s in S:
    if s["n"] in (10, 11, 16, 34):
        s["title"] = s["title"].replace(" — 초록 확인", " — 전문 확인")
    elif "PMC" in s["publisher"]:
        s["title"] = s["title"].replace(" — 전문 확인", " — 초록 확인")

sections = [
{"key": "overview", "title": "한눈에 보기", "body":
"달개비(Commelina communis L.)는 닭의장풀과(Commelinaceae)에 속하는 한해살이풀로, 「식품원료 목록」에는 닭의장풀이라는 별칭과 영어명 Dayflower, Asian dayflower로 올라 있다[1]. 중국 전통의학에서는 압척초(Commelinae Herba, Yazhicao)라는 약재로 쓰이고[29][30], 일본에서는 쓰유쿠사(Tsuyukusa)라고 부른다[16].\n\n식품의약품안전처 「식품원료 목록」에서 '달개비'·'달개비분말'·'달개비추출액' 세 원료는 부위가 '전체'로 적힌 '제한적사용' 원료이고, 사용 조건 칸은 비어 있다[1]. 반면 '달개비순'은 '사용가능부위 : 순' 조건이 붙은 '사용가능' 원료다[1]. 따라서 어린 순은 일반 식품원료로 쓸 수 있고, 식물 전체·분말·추출액은 제한적으로만 쓸 수 있다[1]. 제한적사용 원료에 적용되는 식품공전의 구체적인 사용량·사용 방법 기준은 원문으로 확인하지 못함.\n\n달개비에는 혈당을 올리는 탄수화물 분해 효소(α-글루코시다아제)를 억제하는 1-데옥시노지리마이신(DNJ) 같은 이미노당 알칼로이드가 들어 있다[2]. 지상부에는 이소오리엔틴·오리엔틴 같은 플라본 C-배당체가 많다[4][7]. 푸른 꽃잎의 색소 코멜리닌은 안토시아닌·플라본·마그네슘이 모인 금속 착물로 유명하다[15][16]. 효능 연구는 대부분 세포·동물 실험이며, 사람 대상 임상 근거는 이번 조사에서 확인하지 못함."},
{"key": "history", "title": "역사와 전통 이용", "body":
"한국에서는 달개비를 물에 달인 액을 당뇨병 치료에 전통적으로 써 왔다고 보고되었다[3]. 다른 국내 연구는 달개비가 옛 한국에서 인후통·급성 장염·비만·당뇨병 치료와 이뇨제로 쓰였고, 일본에서는 해열·이뇨 약으로 쓰였다고 소개했다[11]. 중국에서는 감염 질환을 치료하는 전통 약재 압척초로 널리 쓰였다[29]. 2024년 연구는 달개비를 아시아에서 비만·당뇨·감염에 수백 년 써 온 기능성 식품 겸 약초로 소개했다[28].\n\n꽃은 염료와 색소 연구의 역사도 길다[16]. 일본 교토의 손그림 유젠 기모노 밑그림에는 꽃잎이 야생종보다 네 배 큰 재배 변종(오보시바나)의 푸른 즙을 쓰며, 이 즙은 물에 묽히면 색이 사라진다[16]. 이 변종은 지금도 비와호 근처 구사쓰시에서 재배된다고 한다[16]. 에도 시대(1603–1868) 목판화 세 점을 분석한 연구에서는 보라색 섬유 2–3가닥에서 달개비 청색과 잇꽃 적색의 혼합이 HPLC-MS/MS로 확인되었다[33].\n\n과학사에서는 1958–1959년 일본 연구진이 꽃잎에서 푸른 결정 색소를 얻어 '코멜리닌'이라 이름 붙였다[16]. 1958년 예비 연구에는 야생 꽃 25,000송이가 쓰였고, 1959년 연구는 재배 변종 꽃잎 7 kg에서 순수 결정 2 g을 얻었다[16]. 1992년 X선 결정 구조가 밝혀지면서 푸른 꽃색이 금속과 결합한 안토시아닌에서 나온다는 '금속 착물설'이 처음으로 직접 증명되었다[16]."},
{"key": "biology", "title": "식물학적 특징", "body":
"달개비는 한 그루에 양성화와 수꽃이 함께 피는 웅성양성동주(andromonoecious) 한해살이풀이다[21]. 일본 도시–농촌 12개 집단 조사에서 도시화된 집단일수록 꽃가루 매개 곤충이 줄어 번식이 제한되었고, 높은 결실률은 제꽃가루받이로 번식을 보장하기 때문일 수 있다고 해석되었다[21]. 같은 연구에서 매개 곤충이 부족한 집단은 암술 높이와 암술–수술 거리(헤르코가미)가 줄어들었다[21].\n\n푸른 꽃잎 색은 코멜리닌이라는 초분자 색소에서 나온다[15][16]. X선 구조 분석에서 코멜리닌은 마그네슘 이온 4개를 가진 착물로, 그중 2개는 안토시아닌 6분자와, 나머지 2개는 플라본 6분자와 결합한다고 보고되었다[15]. 다른 정리에서는 안토시아닌(말로닐아오바닌)·플라본(플라보코멜린)·마그네슘의 비율을 6:6:2, 분자량을 약 8,000으로 적었다[16].\n\n달개비는 기공 공변세포 연구의 모델 식물로도 쓰인다[26]. 잠두(Vicia faba)와 함께 기공 공변세포의 앱시스산(ABA) 신호를 세포·생화학·전기생리학적으로 연구하는 재료로 쓰였다[26]. 구리 오염 광산 지대에서도 자라는 의사금속식물(pseudometallophyte)이며, 일부 집단은 잎에 구리를 많이 쌓는다[17][18]. 국내 공공기관 자료로 꽃 크기·개화기 같은 형태 수치는 확인하지 못함."},
{"key": "related_species", "title": "같은 속·혼동 주의 식물", "body":
"「식품원료 목록」에는 같은 속 원료가 여럿 올라 있으므로 달개비 자료와 섞지 않아야 한다[1]. 흰닭의장풀(Commelina communis var. albida)은 '흰닭의장풀순'이라는 별도 원료로 '사용가능부위 : 순'인 '사용가능' 원료이다[1]. Commelina virginica는 잎·덩이줄기가, C. coelestis·C. dianthifolia·C. elliptica·C. erecta·C. tuberosa는 덩이줄기가 '사용가능' 원료로 따로 올라 있다[1]. 이 원료들의 지위와 사용 부위는 달개비(전체는 제한적사용, 순은 사용가능)와 다르다[1].\n\n일본에서는 달개비와 함께 자라는 Commelina communis f. ciliata가 따로 구분된다[20][22]. 염색체 수는 달개비가 2n = 88, f. ciliata가 2n = 46이며, 달개비는 f. ciliata의 유전체와 미지의 다른 유전체를 함께 가진 이질배수체(신4배체)로 해석되었다[20]. f. ciliata는 제꽃가루받이 비율이 높은 혼합 교배 한해살이풀이다[22].\n\n열대에 흔한 Commelina benghalensis는 다른 종이다[27][32]. 이 종의 줄기 에탄올 추출물은 임신한 쥐에서 유산 유발과 간 독성을 보였으므로, 이런 결과를 달개비에 옮겨 적으면 안 된다[32]. 미국 플로리다에서는 두 종 모두 오이모자이크바이러스(CMV)의 기주로 보고되었다[27]."},
{"key": "cultivation", "title": "자생·재배", "body":
"달개비는 대부분 들과 밭에서 저절로 자라는 잡초이며, 국내 재배 면적·생산량 통계는 통계청·농림축산식품부 자료에서 확인하지 못함. 국내 연구에서는 전남 구례의 지역 시장에서 산 달개비를 말려 시료로 썼다[11]. 중국 품질 평가 연구는 23개 성·자치구·직할시에서 모은 57개 배치를 분석했다[6].\n\n농업에서는 골칫거리 잡초로 다뤄진다[23][25]. 중국에서는 옥수수·콩 밭에 주로 퍼지는 해로운 잡초이며, 지린성 집단은 제초제 아트라진에 대한 저항성 지수 2.9의 낮은 저항성을 보였다[23]. 이 집단에서는 표적 유전자 PsbA의 발현이 감수성 집단보다 처리 0시간에 7.28배, 24시간에 14.28배 높았다[24]. 가뭄·제초제 같은 스트레스에도 잘 자라는 침입성 잡초로 소개된다[25]. 차밭의 산성 토양(pH 5.5 미만)에도 흔하며, pH 4.0에서 알루미늄·철을 4주 처리해도 생물량이 줄지 않았다[35].\n\n일본 도시–농촌 조사에서 도시 지역에는 달개비만 자랐고, 농촌에서는 f. ciliata와 함께 자랐다[20]. 미국 플로리다에서는 밭 주변에 번진 달개비가 고추·담배의 오이모자이크바이러스 유행과 관련된 감염원으로 지목되었다[27]. 식용 순을 얻기 위한 재배 기술(파종·수확 시기)에 관한 국내 공공기관 자료는 확인하지 못함."},
{"key": "processing", "title": "가공·제품", "body":
"「식품원료 목록」에 오른 형태는 식물 전체(달개비), 분말(달개비분말), 추출액(달개비추출액), 어린 순(달개비순)이다[1]. 일본 연구는 이 식물의 추출물과 분말이 제2형 당뇨병 예방용 식품 원료로 중요하다고 적었다[4]. 오리엔틴 연구진은 앞선 연구에서 달개비 차가 고지방식을 먹인 생쥐의 체중 증가를 줄였다고 밝혔다[10].\n\n연구용 추출 예를 보면, 국내 연구는 말린 달개비 300 g에 70% 에탄올 3 L를 넣고 4 °C에서 냉침 추출했다[11]. 이 추출물의 총 폴리페놀은 19.1 ± 0.4 mg 탄닌산 당량/g, 총 플라보노이드는 6.0 ± 0.0 mg 퀘르세틴 당량/g이었고 안토시아닌은 검출되지 않았다[11]. 물 달임액은 α-글루코시다아제 억제 연구에 쓰였다[3]. 알칼로이드는 '총 알칼로이드'(TAC) 형태로 항바이러스 동물 실험에 쓰였다[12].\n\n품질 관리 지표로 중국 연구진은 DNJ 함량 하한 0.0559% 이상[6], 이소오리엔틴 함량 하한 0.023% 이상[7]을 제안했다. 동시에 13개 성분을 정량하는 HPLC-ESI-MS/MS 분석법도 개발되었다[8]. 식약처 「식품 등의 생산실적」(hf_items.csv)에서 달개비 원료 품목의 생산 실적은 확인하지 못함."},
{"key": "genetics", "title": "유전·유전체", "body":
"달개비의 엽록체 유전체는 159,664 bp 길이의 원형으로, 26,146 bp의 역반복 부위(IR) 한 쌍, 88,854 bp의 큰 단일 사본 부위(LSC), 18,518 bp의 작은 단일 사본 부위(SSC)로 이루어진다[19]. 유전자는 모두 137개이며, 고유 단백질 암호 유전자 81개, 고유 tRNA 유전자 32개, rRNA 유전자 7개가 있다[19].\n\n일본 집단의 염색체 수는 2n = 88이고, 유전체 크기가 2n = 46인 f. ciliata의 두 배를 넘었다[20]. 게놈 제자리 혼성화(GISH) 결과 달개비는 f. ciliata의 유전체에 다른 미지의 유전체가 더해진 이질배수체로 해석되었다[20]. 연구진은 이 추가 유전체가 도시 환경에서의 생존에 유리하게 작용했을 수 있다고 보았다[20].\n\n중국 구리 광산 지대 8개 집단과 주변 비오염 지대 6개 집단을 미세위성 표지 12개로 분석한 결과, 유전 집단은 토양의 구리 농도보다 지리적 위치에 따라 세 무리로 나뉘었다[18]. 광산 지대 집단에서 유전 다양성 감소나 병목 효과는 뚜렷하지 않았다[18]. 유전자 발현 연구를 위해 뿌리·줄기·잎·꽃·씨앗과 가뭄·제초제·구리 스트레스 조건에서 가장 안정한 기준 유전자로 SAND가 선정되었다[25]. 핵 유전체 전체 서열은 이번 조사에서 확인하지 못함."},
{"key": "safety", "title": "안전성·주의", "body":
"「식품원료 목록」에서 달개비·달개비분말·달개비추출액은 부위 '전체'의 '제한적사용' 원료이고, 어린 순(달개비순)만 '사용가능부위 : 순' 조건의 '사용가능' 원료다[1]. 제한적사용 원료의 구체적인 사용량·대상 식품 기준은 원문으로 확인하지 못함. 국내 공공기관의 알레르기·잔류농약·독성 정보도 확인하지 못함.\n\n사람을 대상으로 한 독성·임상 시험은 PubMed 검색에서 확인하지 못함. 세포 실험에서는 70% 에탄올 추출물 0.5–1.5 mg/mL에서 대식세포 생존율이 99% 이상, 2 mg/mL에서 91.77%였다[11]. 물 추출물은 CHO-K1 섬유모세포와 3T3-L1 지방세포에서 뚜렷한 세포 독성을 보이지 않았다[3]. 동물 실험에서는 총 알칼로이드 8–32 mg/kg/일을 6일간 먹인 생쥐에서 독감 감염 생존율이 높아졌다[12]. 이 결과들은 동물·세포 수준이며 사람의 안전 섭취량을 뜻하지 않는다[11][12].\n\n주의할 점이 몇 가지 있다[17][34]. 달개비는 탄수화물 소화 효소를 억제해 생쥐의 식후 혈당 상승을 아카보스보다 더 잘 억제했으므로[3], 혈당강하제를 먹는 사람에서의 상호작용은 확인하지 못함. DNJ 자체의 독성 연구는 보고된 것이 없다는 지적이 있다[34]. 구리를 많이 쌓는 집단은 잎 건조중량 1 g당 1,000 μg 넘게 구리를 축적했으므로[17], 광산·오염 지역에서 채취한 개체는 피하는 것이 안전하다. 임신·수유 중 안전성은 확인하지 못함."},
]

compounds = [
 {"name": "1-Deoxynojirimycin", "name_ko": "1-데옥시노지리마이신(DNJ, 모라놀린)", "class": "피페리딘 이미노당 알칼로이드", "role": "marker", "part": "전초(메탄올 추출물)·약재", "content_text": "중국 57개 배치 품질 평가에서 지역 판별 지표로 선정, 함량 하한 0.0559% 이상 제안[6]", "activity_ko": "α-글루코시다아제 억제(효소 실험)[2]; 식물에서는 미생물과 다른 경로로 생합성[5]", "source": [2, 5, 6]},
 {"name": "1-Deoxymannojirimycin", "name_ko": "1-데옥시만노지리마이신(DMJ)", "class": "피페리딘 이미노당 알칼로이드", "role": "bioactive", "part": "전초", "content_text": "UPLC로 DNJ와 함께 정량(배치별 수치는 초록에 없음)[6]", "activity_ko": "α-글루코시다아제 억제 분획에서 분리[2]", "source": [2, 6]},
 {"name": "Homonojirimycin", "name_ko": "α-호모노지리마이신(HNJ)", "class": "피페리딘 이미노당 알칼로이드", "role": "bioactive", "part": "전초(총 알칼로이드)", "content_text": "", "activity_ko": "인플루엔자 A(H1N1) 증식 억제(세포)[14], 1 mg/kg 경구 투여 생쥐에서 감염 생존율 개선(동물)[13]", "source": [2, 13, 14]},
 {"name": "2,5-Dideoxy-2,5-imino-D-mannitol", "name_ko": "DMDP(2,5-디히드록시메틸-3,4-디히드록시피롤리딘)", "class": "피롤리딘 이미노당 알칼로이드", "role": "bioactive", "part": "전초", "content_text": "", "activity_ko": "강한 α-글루코시다아제 억제 성분으로 보고[2][4]", "source": [2, 4, 14]},
 {"name": "Norharmane", "name_ko": "노르하르만(β-카볼린)", "class": "β-카볼린 알칼로이드", "role": "bioactive", "part": "전초", "content_text": "하르만과 함께 UPLC로 정량(배치별 수치는 초록에 없음)[6]", "activity_ko": "하르만은 총 알칼로이드에서 분리되었으나 항바이러스 활성은 없었음[14]", "source": [6, 14]},
 {"name": "Isoorientin", "name_ko": "이소오리엔틴(호모오리엔틴)", "class": "플라본 C-배당체", "role": "marker", "part": "전초(약재)", "content_text": "62개 배치에서 네 플라본 중 가장 많음(이소오리엔틴>이소비텍신>오리엔틴>비텍신), 함량 하한 0.023% 이상 제안[7]", "activity_ko": "주요 항산화 성분 중 하나(DPPH·초과산화물 소거)[4]", "source": [4, 7, 8]},
 {"name": "Orientin", "name_ko": "오리엔틴", "class": "플라본 C-배당체", "role": "bioactive", "part": "지상부", "content_text": "주요 성분 중 하나로 보고[10]", "activity_ko": "3T3-L1 지방세포에서 50 μM로 중성지방 축적 억제(세포)[10]; 주요 항산화 성분[4]", "source": [4, 7, 10]},
 {"name": "Isovitexin", "name_ko": "이소비텍신", "class": "플라본 C-배당체", "role": "bioactive", "part": "전초", "content_text": "네 플라본 중 두 번째로 많음[7]", "activity_ko": "", "source": [4, 7, 9]},
 {"name": "Vitexin", "name_ko": "비텍신", "class": "플라본 C-배당체", "role": "bioactive", "part": "지상부", "content_text": "네 플라본 중 가장 적음[7]", "activity_ko": "쥐 소장 α-글루코시다아제 억제(효소 실험)[4]", "source": [4, 7]},
 {"name": "Luteolin 7-O-glucoside", "name_ko": "글루코루테올린(루테올린-7-O-글루코사이드)", "class": "플라본 O-배당체", "role": "bioactive", "part": "지상부", "content_text": "", "activity_ko": "주요 항산화 성분[4]; 지방세포의 포도당 흡수 억제 보고 인용[10]", "source": [4, 10]},
 {"name": "Isoquercitrin", "name_ko": "이소퀘르시트린(퀘르세틴-3-O-글루코사이드)", "class": "플라보놀 배당체", "role": "bioactive", "part": "지상부", "content_text": "", "activity_ko": "주요 항산화 성분이며 쥐 소장 α-글루코시다아제 억제(효소 실험)[4]", "source": [4, 9]},
 {"name": "Flavocommelin", "name_ko": "플라보코멜린", "class": "플라본 C-배당체", "role": "bioactive", "part": "꽃잎(코멜리닌 구성 성분)·지상부", "content_text": "", "activity_ko": "코멜리닌의 보조 색소(공색소)로 청색을 안정화[16]", "source": [4, 16]},
 {"name": "Malonylawobanin", "name_ko": "말로닐아오바닌", "class": "안토시아닌(델피니딘 3,5-디글루코사이드 아실화체)", "role": "bioactive", "part": "꽃잎", "content_text": "", "activity_ko": "코멜리닌의 안토시아닌 성분으로 B고리에서 금속 이온과 결합[16]", "source": [15, 16]},
 {"name": "Quercetin 3-O-glucuronide", "name_ko": "퀘르세틴-3-O-글루쿠로나이드", "class": "플라보놀 배당체", "role": "bioactive", "part": "메탄올상 추출물의 분획 1", "content_text": "분획 1에서 확인된 65개 성분 중 19.35%로 가장 많음[31]", "activity_ko": "이 성분이 주를 이룬 분획이 세균 세포막 투과성을 높임(시험관)[31]", "source": [31]},
]

assays = [
 {"role": "literature", "compound": "1-Deoxynojirimycin", "compound_ko": "1-데옥시노지리마이신(DNJ)·데옥시만노지리마이신(DMJ)", "part": "약재(중국 23개 지역 57개 배치)", "content": "DNJ 함량 하한 0.0559% 이상 제안[6]", "method": "UPLC-UV",
  "conditions": {"instrument": "", "column": "MicroPulite HSS T3(2.1 mm × 50 mm, 1.8 μm)", "mobile_phase": "아세토니트릴–0.2% 인산 수용액(20:80)", "gradient": "등용매", "flow": "0.3 mL/min", "temp": "", "detection": "UV 254 nm", "injection": "", "sample_prep": "", "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "부분최소제곱판별분석에서 DNJ가 산지별 품질 차이를 가르는 지표 성분으로 선정되었다[6]. 노르하르만·하르만은 MicroPulite XP tC18(2.1 mm × 100 mm, 1.7 μm) 칼럼, 아세토니트릴–0.2% 인산(4:96), 0.4 mL/min, 254 nm로 따로 정량했다[6]. 전문 확인 못함 — 초록에 나온 조건만 옮겼다. DNJ는 발색단이 없어 보통 유도체화가 필요하다는 일반 설명이 있으나[34], 이 논문의 유도체화 여부는 확인하지 못함.",
  "source": [6], "url": "https://pubmed.ncbi.nlm.nih.gov/40461198/", "source_kind": "paper"},
 {"role": "literature", "compound": "Isoorientin", "compound_ko": "이소오리엔틴·오리엔틴·비텍신·이소비텍신", "part": "약재(62개 배치)", "content": "이소오리엔틴>이소비텍신>오리엔틴>비텍신; 이소오리엔틴 함량 하한 0.023% 이상 제안[7]", "method": "HPLC-UV",
  "conditions": {"instrument": "", "column": "Dikma Platisil ODS(4.6 mm × 250 mm, 5 μm)", "mobile_phase": "아세토니트릴–0.1% 포름산(14:86)", "gradient": "등용매", "flow": "1.0 mL/min", "temp": "35 °C", "detection": "UV 348 nm", "injection": "", "sample_prep": "", "standard": "", "linearity": "r > 0.9999", "lod": "", "loq": "", "recovery": "평균 96.17%–103.0%"},
  "rationale": "네 플라본 C-배당체 중 이소오리엔틴이 가장 많아 함량 측정 지표로 제안되었다[7]. 정밀도·안정성·반복성 RSD는 모두 2.0% 미만이었다[7]. 전문 확인 못함 — 초록 조건만 옮겼다.",
  "source": [7], "url": "https://pubmed.ncbi.nlm.nih.gov/36725225/", "source_kind": "paper"},
 {"role": "literature", "compound": "Orientin", "compound_ko": "오리엔틴 등 13개 성분(이소오리엔틴·비텍신·이소비텍신·루틴·아피제닌·프로토카테쿠산·바닐산·카페산·페룰산·루테올린·퀘르세틴·이소람네틴)", "part": "전초 추출물", "content": "62개 성분 확인, 13개 성분 동시 정량(함량 수치는 초록에 없음)[8]", "method": "HPLC-ESI-MS/MS(정량), UHPLC-Q-TOF-MS/MS(확인)",
  "conditions": {"instrument": "", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "", "injection": "", "sample_prep": "", "standard": "", "linearity": "r ≥ 0.9991", "lod": "", "loq": "", "recovery": "98.64–100.8%"},
  "rationale": "플라보노이드·페놀산 13종을 한 번에 정량하는 품질 관리용 방법으로 개발되었다[8]. 일내·일간 정밀도(RSD)는 각각 1.04%·0.92% 이내였다[8]. 전문 확인 못함 — 칼럼·이동상 조건은 비워 둠.",
  "source": [8], "url": "https://pubmed.ncbi.nlm.nih.gov/29659750/", "source_kind": "paper"},
]

d = {
 "slug": "commelina-communis", "name_ko": "달개비", "name_en": "Asiatic dayflower",
 "scientific_name": "Commelina communis L.",
 "aliases": ["닭의장풀", "Asian dayflower", "Dayflower", "압척초(Commelinae Herba)", "Yazhicao", "쓰유쿠사(Tsuyukusa)", "달개비순", "달개비분말", "달개비추출액"],
 "sections": sections, "compounds": compounds, "markers": [], "assays": assays,
 "nutrients": [], "production": [], "world": [], "gi": [], "orgs": [], "sources": S,
}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in sections: print(s["key"], len(s["body"]))
