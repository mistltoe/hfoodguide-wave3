import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
A = "2026-11-02"
PM = "PubMed"
def pm(n, title, pmid, pmc=None, pub=None):
    url = f"https://pmc.ncbi.nlm.nih.gov/articles/{pmc}/" if pmc else f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
    return {"n": n, "title": title, "url": url, "publisher": pub or (f"{PM} (PMID {pmid}" + (f", {pmc})" if pmc else ")")), "accessed": A}
sources = [
 {"n": 1, "title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 카네이션꽃(Dianthus caryophyllus L.) 항목", "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
 pm(2, "Study on chemical constituents and antioxidant activities of Dianthus caryophyllus L. Front Plant Sci. 2024 (doi:10.3389/fpls.2024.1438967)", "39239204", "PMC11374617"),
 pm(3, "Widely targeted metabolomics reveals the antioxidant and anticancer activities of different colors of Dianthus caryophyllus. Front Nutr. 2023 (doi:10.3389/fnut.2023.1166375)", "37275648", "PMC10235515"),
 pm(4, "Integrated multi-omic data and analyses reveal the pathways underlying key ornamental traits in carnation flowers. Plant Biotechnol J. 2022 (doi:10.1111/pbi.13801)", "35247284", "PMC9129081"),
 pm(5, "Sequence analysis of the genome of carnation (Dianthus caryophyllus L.). DNA Res. 2014 (doi:10.1093/dnares/dst053)", "24344172", "PMC4060945"),
 pm(6, "Construction of a reference genetic linkage map for carnation (Dianthus caryophyllus L.). BMC Genomics. 2013 (doi:10.1186/1471-2164-14-734)", "24160306", "PMC3870981"),
 pm(7, "Quantification of major flavonoids in carnation tissues (Dianthus caryophyllus) as a tool for cultivar discrimination. Z Naturforsch C. 2008 (doi:10.1515/znc-2008-3-401) — 초록만 확인", "18533456"),
 pm(8, "Kaempferide triglycoside: a possible factor of resistance of carnation (Dianthus caryophyllus) to Fusarium oxysporum f. sp. dianthi. Phytochemistry. 2001 (doi:10.1016/s0031-9422(00)00488-x) — 초록만 확인", "11314958"),
 pm(9, "Inhibition of in vitro growth and arrest in the G0/G1 phase of HCT8 line human colon cancer cells by kaempferide triglycoside from Dianthus caryophyllus. Phytother Res. 2010 (doi:10.1002/ptr.3105) — 초록만 확인", "20104502"),
 pm(10, "Fungitoxic phenols from carnation (Dianthus caryophyllus) effective against Fusarium oxysporum f. sp. dianthi. Phytochem Anal. 2003 (doi:10.1002/pca.672) — 초록만 확인", "12597250"),
 pm(11, "A rationale for the shift in colour towards blue in transgenic carnation flowers expressing the flavonoid 3',5'-hydroxylase gene. Phytochemistry. 2003 (doi:10.1016/s0031-9422(02)00684-2) — 초록만 확인", "12657292"),
 pm(12, "Expression of flavonoid 3',5'-hydroxylase and acetolactate synthase genes in transgenic carnation: assessing the safety of a nonfood plant. J Agric Food Chem. 2013 (doi:10.1021/jf4004384) — 초록만 확인", "23646984"),
 {"n": 13, "title": "EFSA GMO Panel. Risk assessment of new sequencing information on genetically modified carnation FLO-40685-2. EFSA J. 2018;16(7):5396 (doi:10.2903/j.efsa.2018.5396)", "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC7009468/", "publisher": "European Food Safety Authority (PubMed PMID 32626009)", "accessed": A},
 pm(14, "\"Cyclamen Red\" colors based on a macrocyclic anthocyanin in carnation flowers. J Agric Food Chem. 2000 (doi:10.1021/jf9907642) — 초록만 확인", "10637045"),
 pm(15, "Detection of 1-O-malylglucose: pelargonidin 3-O-glucose-6''-O-malyltransferase activity in carnation (Dianthus caryophyllus). Biochem Biophys Res Commun. 2008 (doi:10.1016/j.bbrc.2008.04.153) — 초록만 확인", "18471436"),
 pm(16, "Occupational allergy caused by Dianthus caryophillus, Gypsophila paniculata, and Lilium longiflorum. Allergy. 1998 (doi:10.1111/j.1398-9995.1998.tb03803.x) — 초록만 확인", "9821482"),
 pm(17, "Occupational allergic contact dermatitis caused by decorative plants. Contact Dermatitis. 1996 (doi:10.1111/j.1600-0536.1996.tb02217.x) — 초록만 확인", "8807225"),
 pm(18, "Occupational dermatitis because of carnation. Contact Dermatitis. 2008;58(2):119-20 (doi:10.1111/j.1600-0536.2007.01191.x) — 증례 보고, 초록 없음", "18186757"),
 pm(19, "Dianthin and Its Potential in Targeted Tumor Therapies. Toxins (Basel). 2019 (doi:10.3390/toxins11100592) — 초록만 확인", "31614697", "PMC6832487"),
 pm(20, "A new class of anti-HIV agents: GAP31, DAPs 30 and 32. FEBS Lett. 1991 (doi:10.1016/0014-5793(91)81122-o) — 초록만 확인", "1936243"),
 pm(21, "Bioactivity of Dianthus caryophyllus, Lepidium sativum, Pimpinella anisum, and Illicium verum essential oils and their major components against the West Nile vector Culex pipiens. Parasitol Res. 2012 (doi:10.1007/s00436-012-3097-1) — 초록만 확인", "22955447"),
 pm(22, "Phytochemical, Nutritional and Mineral Content of Four Edible Flowers. Foods. 2024 (doi:10.3390/foods13060939) — 전문 확인(종명 표기가 빠진 본문)", "38540929", "PMC10969817"),
 pm(23, "Edible flowers--a new promising source of mineral elements in human nutrition. Molecules. 2012 (doi:10.3390/molecules17066672) — 초록만 확인", "22728361", "PMC6268292"),
 pm(24, "Genomic basis of scent loss and functional divergence in wild and cultivated carnations (Dianthus spp.). Hortic Res. 2026 (doi:10.1093/hr/uhag130) — 초록만 확인", "42524454", "PMC13412721"),
 pm(25, "Flavonoid biosynthesis in Dianthus caryophyllus L. is early regulated during interaction with Fusarium oxysporum f. sp. dianthi. Phytochemistry. 2021 (doi:10.1016/j.phytochem.2021.112933) — 초록만 확인", "34482105"),
 pm(26, "Flower colour and cytochromes P450. Philos Trans R Soc Lond B Biol Sci. 2013 (doi:10.1098/rstb.2012.0432) — 초록만 확인", "23297355", "PMC3538422"),
 pm(27, "Structure of the acyl-glucose-dependent anthocyanin 5-O-glucosyltransferase gene in carnations and its disruption by transposable elements in some varieties. Mol Genet Genomics. 2011 (doi:10.1007/s00438-011-0655-7) — 초록만 확인", "22048706"),
 pm(28, "Reverted glutathione S-transferase-like genes that influence flower color intensity of carnation (Dianthus caryophyllus L.) originated from excision of a transposable element. Breed Sci. 2013 (doi:10.1270/jsbbs.63.435) — 초록만 확인", "24399917", "PMC3859356"),
 pm(29, "Dianthi herba: a comprehensive review of its botany, traditional use, phytochemistry, and pharmacology. Chin Med. 2022 (doi:10.1186/s13020-022-00570-2) — 초록만 확인", "35062995", "PMC8780776"),
 {"n": 30, "title": "김해시 누리집 「화훼, 원예종묘를 국내 지급조달하기 위해」(카네이션 재배면적 2003년) — WebSearch 요약으로만 확인, 원문 미열람", "url": "https://www.gimhae.go.kr/07097/07132/07149.web", "publisher": "경상남도 김해시", "accessed": A},
 {"n": 31, "title": "EFSA Compendium of botanicals (식품에 쓰이는 식물 가운데 우려 물질이 보고된 종 목록) — 목록 성격은 WebSearch 요약으로만 확인, 이 종의 항목 원문 미열람", "url": "https://www.efsa.europa.eu/en/data/compendium-botanicals", "publisher": "European Food Safety Authority", "accessed": A},
 pm(32, "Transcriptome analysis of carnation (Dianthus caryophyllus L.) based on next-generation sequencing technology. BMC Genomics. 2012 (doi:10.1186/1471-2164-13-292) — 초록만 확인", "22747974", "PMC3411436"),
 pm(33, "An active hAT transposable element causing bud mutation of carnation by insertion into the flavonoid 3'-hydroxylase gene. Mol Genet Genomics. 2013 (doi:10.1007/s00438-013-0742-z) — 초록만 확인", "23543146"),
 pm(34, "A comprehensive phylogeny of auxin homeostasis genes involved in adventitious root formation in carnation stem cuttings. PLoS One. 2018 (doi:10.1371/journal.pone.0196663) — 초록만 확인", "29709027", "PMC5927418"),
]

sections = [
 {"key": "overview", "title": "한눈에 보기", "body":
  "카네이션(Dianthus caryophyllus L.)은 석죽과(Caryophyllaceae) 패랭이꽃속의 여러해살이풀로, 세계적으로 장미 다음가는 인기 절화로 꼽힌다[2][4]. 꽃 색은 빨강·분홍·흰색·자홍·노랑과 여러 색이 섞인 무늬까지 다양하고, 정향을 닮은 매운 향의 주성분은 유제놀이다[4].\n\n"
  "식품의약품안전처 「식품원료 목록」에서 카네이션은 '카네이션꽃'이라는 원료명으로 올라 있는 사용가능 원료이며, 사용 조건은 '사용가능부위 : 꽃'이다[1]. 같은 자료에서 이 종은 유럽식품안전청(EFSA)의 식물 목록(Compendium of botanicals)에도 올라 있는 것으로 표시되어 있다[1][31]. 건강기능식품 고시형 원료의 원재료로 쓰인다는 기록은 확인하지 못함.\n\n"
  "꽃에는 플라보놀·플라본 배당체, 말산이 붙은 안토시아닌, 유제놀 같은 향기 성분이 있다[2][4][11]. 중국에서 기른 카네이션의 부위별 70% 메탄올 추출물에서 꽃의 총페놀(7.573 mg/g)과 총플라보노이드(4.616 mg/g)가 뿌리·줄기·잎보다 많았다[2]. 꽃은 차·술·죽에 넣어 먹기도 한다[2]."},
 {"key": "history", "title": "역사", "body":
  "카네이션 재배의 역사는 2000년이 넘는다[4]. 카네이션을 포함한 패랭이꽃속 꽃은 고대 그리스 때부터 길러졌고, 음식의 향을 내는 재료로도 쓰였으며 지금도 일부 요리에 쓰인다[22]. 꽃잎은 쓴맛이 있고 꽃잎 밑부분에서 더 강하다[22].\n\n"
  "한 연구는 카네이션을 이라크와 지중해 지역이 원산인 식물로 소개하며, 말린 꽃봉오리가 목과 잇몸 감염, 상처, 위장 질환에 쓰였다고 정리했다[3]. 중국 이름 '샹스주(香石竹)'는 향기로운 패랭이꽃이라는 뜻으로, 이 꽃의 향을 반영한다[4].\n\n"
  "20세기 말에는 유전자 재조합으로 꽃 색을 바꾼 카네이션이 나왔다[11]. 카네이션에는 없는 플라보노이드 3′,5′-수산화효소 유전자를 넣어 보라색 계통의 델피니딘 색소를 만든 품종(Moondust·Moonshadow)이 판매되었다[11]. 이 유전자 재조합 카네이션은 2013년 기준 16년 동안 꽃 시장에 팔렸고, 남아메리카에서 생산되어 북아메리카·유럽·일본에 주로 유통되었다[12]."},
 {"key": "biology", "title": "식물학적 특징", "body":
  "카네이션은 석죽과 패랭이꽃속에 속하는 여러해살이풀이며, 염색체 수는 2n = 2x = 30이다[2][4]. 유전체 크기는 k-mer 분석으로 약 622 Mb, 다른 품종에서는 약 640 Mb로 추정되었다[4][5].\n\n"
  "꽃잎의 빨강·분홍 계열 색은 펠라고니딘과 시아니딘 계열 안토시아닌에서 오며, 이 색소에는 포도당 두 개와 말산이 붙는다[11][27]. 카네이션은 플라보노이드 3′,5′-수산화효소가 없어 파랑·보라색을 내는 델피니딘 색소를 만들지 못한다[26]. 붉은 꽃잎에서는 펠라고니딘 3-말릴글루코사이드가 꽃잎이 자라면서 쌓이지만, 뿌리·줄기·잎에서는 이 색소도 만드는 효소 활성도 검출되지 않았다[15].\n\n"
  "꽃 향은 시스-3-헥세닐 벤조에이트, β-카리오필렌, 유제놀이 주를 이룬다[4]. 'Lorca' 품종에서 유제놀은 꽃이 피어 가면서 늘어 활짝 핀 단계(S6)에 0.04247 mmol/g이었다[4]. 연구자들은 꽃눈 형성부터 시드는 단계까지 꽃 발달을 7단계(S1–S7)로 나누어 분석했다[4]."},
 {"key": "related_species", "title": "가까운 종", "body":
  "같은 패랭이꽃속의 술패랭이꽃(D. superbus)과 패랭이꽃(D. chinensis)은 말린 지상부를 한약재 구맥(瞿麥, Dianthi herba)으로 쓴다[29]. 구맥에서는 트리테르펜 사포닌·플라보노이드·정유 성분 등 약 194종의 화합물이 보고되었다[29]. 카네이션꽃과 구맥은 쓰는 종과 부위가 다르므로 섞어 쓰지 않도록 주의해야 하며, 구맥의 식품원료 지위는 이번 조사에서 확인하지 못함.\n\n"
  "향이 진한 야생 카네이션 계통의 유전체(876 Mb, 2n = 2x = 30)는 전이인자가 82.4%를 차지했고, 재배 카네이션은 야생 계통보다 꽃 향이 약하다[24]. 이 연구는 테르펜 합성 유전자의 변이가 향 차이와 관련된다고 보고했다[24].\n\n"
  "카네이션 유전 지도를 만들 때 패랭이꽃속의 다른 종(D. capitatus subsp. andrzejowskianus)에서 얻은 RAPD 지도와 맞추어 보았다[6]. 같은 석죽과의 비누풀(Saponaria) 종자에서 나오는 사포린은 카네이션의 리보솜 불활성화 단백질 디안틴과 구조가 매우 비슷하다[19]. 꽃 도매업자의 직업성 알레르기 사례에서는 카네이션과 함께 같은 석죽과의 안개꽃(Gypsophila paniculata)이 원인으로 지목되었다[16]. 식용 꽃 12종의 무기질을 비교한 체코 연구에서는 국화속·패랭이꽃속·제비꽃속 꽃의 무기질이 가장 많았으며, 이 패랭이꽃속 꽃이 어떤 종인지는 초록에서 확인하지 못함[23]."},
 {"key": "cultivation", "title": "재배와 생산", "body":
  "카네이션은 꺾꽂이(줄기 삽수)로 번식하며, 삽수의 뿌리 내림에 관여하는 옥신 관련 유전자가 품종별로 분석되었다[34]. 재배에서 가장 큰 문제는 푸사리움 시들음병(Fusarium oxysporum f. sp. dianthi)이다[25]. 저항성 품종 'Golem'은 병원균 접종 48–96시간 뒤 뿌리의 페놀·플라보노이드가 유의하게 늘었다[25]. 'Novada' 품종에 늘 들어 있는 캠페라이드 삼당류 배당체는 이 병원균의 생장을 강하게 억제했다[8]. 저항성이 높은 'Roland' 품종에서는 플라본 다티세틴이 검출되었고 병원균 억제 활성을 보였다[10].\n\n"
  "새 꽃 색 품종은 가지 변이(아조변이)에서 많이 나오며, 전이인자가 색소 유전자에 들어가거나 빠지면서 보라색이 진분홍으로 바뀐 사례가 보고되었다[33]. 꽃 색을 진하게 하는 글루타티온 S-전이효소 유사 유전자는 반세기 넘게 육종에 쓰여 왔다[28].\n\n"
  "국내 카네이션 재배면적은 2003년 전국 111.7 ha, 그중 경상남도 57.3 ha였다는 김해시 자료가 있다(WebSearch 요약으로만 확인)[30]. 최근 연도의 품목별 재배면적·생산액은 공식 통계 원문을 열지 못해 확인하지 못함."},
 {"key": "processing", "title": "가공과 이용", "body":
  "식품으로는 꽃을 쓰며, 국내 식품원료 목록에서 쓸 수 있는 부위도 꽃뿐이다[1]. 꽃은 차·술·죽에 넣어 향과 색을 더하는 데 쓰인다[2]. 꽃잎은 쓴맛이 있고 꽃잎 밑부분에서 더 강하다[22].\n\n"
  "연구에서는 얼려 말린 꽃가루를 70% 메탄올로 추출해 성분과 항산화 활성을 비교했다[2][3]. 보라색 꽃 추출물의 DPPH 소거 IC50은 37.42 ± 0.20 µg/mL로, 흰색 꽃(261.36 ± 9.31 µg/mL)보다 활성이 강했다[3]. 꽃 20 kg을 95% 에탄올에 담가 추출한 뒤 칼럼 크로마토그래피로 플라보노이드 9종과 페놀 배당체 1종을 분리했다[2].\n\n"
  "카네이션 정유의 주성분으로 β-카리오필렌·유제놀 등이 보고되었고, 이 정유는 모기 유충에 중간 정도의 살충 활성(LC50 50 mg/L 초과)을 보였다[21]. 유전자 재조합 카네이션은 식용이 아닌 절화로만 유통된다[12][13]. 카네이션꽃을 원료로 한 국내 식품·건강기능식품의 생산실적은 확인하지 못함."},
 {"key": "genetics", "title": "유전체와 육종", "body":
  "2014년 'Francesco' 품종의 초안 유전체가 발표되었으며, 568.9 Mb(추정 유전체의 91%)가 45,088개 스캐폴드로 조립되었고 단백질 유전자 43,266개가 예측되었다[5]. 2022년에는 'Scarlet Queen' 품종의 염색체 수준 유전체(636.30 Mb, 15개 유사 염색체)가 나왔고, 단백질 유전자 43,925개와 전이인자 비율 70.62%가 보고되었다[4].\n\n"
  "SSR 표지 412개로 만든 연관 지도는 969.6 cM을 덮었고, 세균성 시들음병 저항성과 꽃 안토시아닌 형질의 양적형질 유전자좌가 함께 지도에 올랐다[6]. 차세대 염기서열 분석으로 30만 개가 넘는 유전자 단편(unigene)과 SSR 후보 17,362개가 확보되었다[32].\n\n"
  "꽃 색 변이에는 전이인자가 크게 관여한다[27][33]. 안토시아닌 5번 위치에 포도당을 붙이는 효소 유전자(AA5GT)에 레트로트랜스포존이 들어가면 색소 수식이 빠진다[27]. 플라보노이드 3′,5′-수산화효소를 넣은 유전자 재조합 카네이션(FLO-40685-2)에 대해 유럽식품안전청은 새 염기서열 자료를 검토한 뒤에도 기존 위해성 평가가 유효하다고 결론지었다[13]."},
 {"key": "safety", "title": "안전성", "body":
  "식품의약품안전처 「식품원료 목록」에서 카네이션은 꽃 부위만 쓸 수 있는 사용가능 원료이며, 그 밖의 섭취량 제한이나 주의사항은 목록에서 확인하지 못함[1]. 이 종은 유럽식품안전청의 식물 목록(Compendium of botanicals)에 올라 있는 것으로 표시되어 있는데, 이 목록은 건강에 우려가 될 수 있는 성분이 보고된 식물을 모은 위해 확인용 자료이며 안전성 판정은 아니다[1][31]. 그 목록에서 이 종에 대해 어떤 성분이 올라 있는지는 원문을 열지 못해 확인하지 못함.\n\n"
  "카네이션 잎에서는 리보솜 불활성화 단백질(디안틴 계열, 30·32 kDa)이 분리되었다[20]. 디안틴은 표적 항암 치료제 연구에 쓰이는 독성 단백질이지만, 먹는 꽃에 얼마나 들어 있는지는 확인하지 못함[19].\n\n"
  "꽃을 다루는 사람에게서 직업성 알레르기가 보고되었다[16][17][18]. 한 꽃 도매업자는 카네이션 피부 단자 시험과 문지름 시험에서 양성을 보였고, 카네이션 추출물에서 IgE가 붙는 15·17 kDa 단백질이 확인되었다[16]. 핀란드에서는 14년 동안 장식용 식물로 생긴 직업성 접촉피부염 12건 가운데 석죽과(카네이션 등)가 2건이었다[17].\n\n"
  "유전자 재조합 카네이션은 식용 작물이 아니지만, 사람·동물 건강 위험이 기존 카네이션보다 크지 않다는 평가를 받았다[12]. 식용 꽃의 잔류농약·중금속 기준이나 섭취 시 알레르기에 관한 국내 공공기관 정보는 확인하지 못함."},
]

compounds = [
 {"name": "Eugenol", "name_ko": "유제놀", "class": "페닐프로파노이드(향기 성분)", "role": "marker", "part": "꽃",
  "content_text": "'Lorca' 꽃: S4 0.00708 → S5 0.02596 → S6 0.04247 mmol/g(꽃 발달 단계별)[4]; 정유의 주성분 가운데 하나[21]",
  "activity_ko": "카네이션 특유의 매운 향을 내는 주성분[4]; 단일 성분으로 모기 유충 LC50 18.28 mg/L[21]", "source": [4, 21]},
 {"name": "cis-3-Hexenyl benzoate", "name_ko": "시스-3-헥세닐 벤조에이트", "class": "벤조산 에스터(향기 성분)", "role": "bioactive", "part": "꽃(활짝 핀 단계)",
  "content_text": "꽃 향의 3대 주성분 가운데 하나(GC-MS, 함량 수치는 본문에서 확인하지 못함)[4]",
  "activity_ko": "꽃 향 구성 성분[4]", "source": [4]},
 {"name": "beta-Caryophyllene", "name_ko": "β-카리오필렌", "class": "세스퀴테르펜", "role": "bioactive", "part": "꽃·정유",
  "content_text": "꽃 향 3대 주성분 가운데 하나[4]; 정유의 주성분으로 보고됨(함량은 초록에 없음)[21]",
  "activity_ko": "모기 유충에 100 mg/L에서도 활성이 없었음[21]", "source": [4, 21]},
 {"name": "Pelargonidin 3-O-glucoside", "name_ko": "펠라고니딘 3-O-글루코사이드", "class": "안토시아닌", "role": "bioactive", "part": "꽃잎",
  "content_text": "'Lorca' 꽃잎에서 활짝 핀 단계(S6)에 안토시아닌 가운데 가장 많음(UPLC-ESI-MS/MS, 수치는 보충표)[4]",
  "activity_ko": "꽃잎 가장자리 붉은색의 주된 색소로 제시됨[4]", "source": [4]},
 {"name": "Pelargonidin 3,5-di-O-glucoside 6'',6'''-malyl diester", "name_ko": "펠라고니딘 3,5-다이글루코사이드 고리형 말릴 다이에스터", "class": "말산 아실화 안토시아닌", "role": "bioactive", "part": "꽃잎",
  "content_text": "'Red Rox' 등 9개 품종의 '시클라멘 빨강' 색의 원인 색소(정량값 없음)[14]",
  "activity_ko": "산성에서 고리가 열려 3-O-(6''-O-말릴글루코사이드)-5-O-글루코사이드로 바뀜[14]", "source": [14, 11]},
 {"name": "Cyanin", "name_ko": "시아닌(시아니딘 3,5-O-다이글루코사이드)", "class": "안토시아닌", "role": "bioactive", "part": "꽃",
  "content_text": "꽃에만 특이적으로 많은 대사물로 보고됨(상대량)[2]",
  "activity_ko": "카네이션 고유 안토시아닌은 펠라고니딘·시아니딘 계열[11]", "source": [2, 11]},
 {"name": "Kaempferide triglycoside", "name_ko": "캠페라이드 삼당류 배당체", "class": "플라보놀 배당체", "role": "bioactive", "part": "식물체('Novada' 품종)",
  "content_text": "'Novada' 품종의 상시 성분으로 분리·구조 결정(함량은 초록에 없음)[8]",
  "activity_ko": "푸사리움 시들음병균 생장 억제[8]; 사람 대장암세포 HCT8 증식 억제·G0/G1기 정지(시험관)[9]", "source": [8, 9]},
 {"name": "Kaempferol 3-O-sophoroside", "name_ko": "캠페롤 3-O-소포로사이드", "class": "플라보놀 배당체", "role": "bioactive", "part": "꽃",
  "content_text": "꽃 95% 에탄올 추출물에서 분리한 10종 가운데 하나(Dc-2), 함께 분리: 아스트라갈린·캠페롤 3-네오헤스페리도사이드·클리토린 등[2]",
  "activity_ko": "DPPH 소거능이 분리 성분 가운데 두 번째로 강함(시험관)[2]", "source": [2]},
 {"name": "Isoorientin 2''-O-rhamnoside", "name_ko": "이소오리엔틴 2″-O-람노사이드", "class": "플라본 C-배당체", "role": "bioactive", "part": "꽃",
  "content_text": "꽃에서 분리(Dc-7), 함량은 확인하지 못함[2]",
  "activity_ko": "분리한 10종 가운데 DPPH 소거능이 가장 강함; SOD1·SOD3과 도킹 결합 에너지 −13.20·−10.43 kcal/mol(컴퓨터 예측)[2]", "source": [2]},
 {"name": "Apigenin 6-C-glucosyl-7-O-glucoside 6'''-malyl ester", "name_ko": "아피제닌 6-C-글루코실-7-O-글루코사이드 말릴 에스터", "class": "플라본 C-배당체", "role": "marker", "part": "꽃잎",
  "content_text": "유전자 재조합 보라색 카네이션 꽃잎에서 구조 동정(정량값 없음)[11]; 9개 품종의 꽃·잎·줄기·싹·뿌리에서 플라본 C-배당체 1종과 플라보놀 O-배당체 2종을 HPLC-UV로 정량해 품종 구별 지표로 씀(성분명·함량은 초록에서 확인하지 못함)[7]",
  "activity_ko": "주 색소 1 mM에 2당량 넣으면 최대 흡수 파장이 28 nm 길어지는 가장 강한 보조색소 효과[11]", "source": [11, 7]},
 {"name": "Kaempferol 3-(6'''-rhamnosyl-2'''-glucosyl-glucoside)", "name_ko": "캠페롤 3-(람노실·글루코실 글루코사이드)", "class": "플라보놀 배당체", "role": "bioactive", "part": "꽃잎",
  "content_text": "꽃잎에서 분광학적으로 동정(정량값 없음)[11]",
  "activity_ko": "꽃잎의 플라보놀 배당체로 안토시아닌과 함께 존재[11]", "source": [11]},
 {"name": "6-Hydroxykaempferol-3,6-O-diglucoside", "name_ko": "6-히드록시캠페롤-3,6-O-다이글루코사이드", "class": "플라보놀 배당체", "role": "bioactive", "part": "꽃잎(보라색)",
  "content_text": "보라색 꽃에서 상대량이 높음(광범위 표적 대사체 분석, 절대 함량 없음)[3]",
  "activity_ko": "항산화·항암 활성과 상관이 큰 성분; 단독으로는 A549·U2OS 세포 억제 없음, 2′-데옥시구아노신과 1:1로 섞으면 A549 IC50 53.82 µg/mL(시험관)[3]", "source": [3]},
 {"name": "Quercetin 3-O-sophoroside", "name_ko": "퀘르세틴 3-O-소포로사이드", "class": "플라보놀 배당체", "role": "bioactive", "part": "꽃잎(보라색)",
  "content_text": "보라색 꽃에서 상대량이 높음(절대 함량 없음)[3]",
  "activity_ko": "2′-데옥시구아노신과 1:1로 섞으면 A549 IC50 61.46 µg/mL(시험관)[3]", "source": [3]},
 {"name": "Lutein", "name_ko": "루테인", "class": "카로티노이드", "role": "nutrient", "part": "꽃잎",
  "content_text": "꽃잎 카로티노이드 가운데 세 발달 단계 모두에서 가장 많았으나 꽃이 자라며 줄어듦(수치는 보충표)[4]",
  "activity_ko": "꽃잎의 주요 카로티노이드[4]", "source": [4]},
 {"name": "Methyl ferulate", "name_ko": "페룰산 메틸", "class": "페놀산 에스터", "role": "bioactive", "part": "꽃",
  "content_text": "꽃 추출물에 많은 대사물로 보고됨(상대량)[2]",
  "activity_ko": "꽃 추출물의 높은 항산화·항종양 활성과 관련된 성분으로 제시됨(상관 분석)[2]", "source": [2]},
]

assays = [
 {"role": "literature", "compound": "6-Hydroxykaempferol-3,6-O-diglucoside", "compound_ko": "6-히드록시캠페롤-3,6-O-다이글루코사이드(퀘르세틴 3-O-소포로사이드 등 932종 동시)",
  "part": "꽃잎(흰색·노랑·초록·보라 품종)", "content": "절대 함량 없음 — MRM 신호 기반 상대량으로 보라색 꽃에서 높음[3]",
  "method": "UPLC-ESI-MS/MS(광범위 표적 대사체, MRM)",
  "conditions": {"instrument": "Shimadzu Nexera X2 UPLC + Applied Biosystems 4500 Q TRAP",
   "column": "Agilent SB-C18, 2.1 × 100 mm, 1.8 µm",
   "mobile_phase": "A: 0.1% 포름산 물, B: 0.1% 포름산 아세토니트릴",
   "gradient": "0–9분 5→95% B, 9–10분 95% B, 10–11.1분 95→5% B, 11.1–14분 5% B",
   "flow": "0.35 mL/min", "temp": "40 °C",
   "detection": "ESI(+/−) MRM; 이온원 550 °C, 이온 분무 전압 +5500 V/−4500 V, 가스 I·II·커튼 가스 50·60·25 psi",
   "injection": "4 µL",
   "sample_prep": "꽃잎 액체질소 동결 → 동결건조 → 30 Hz 1.5분 분쇄 → 가루 100 mg + 70% 메탄올 1.2 mL, 30분마다 30초씩 6회 볼텍스, 4 °C 하룻밤 → 12,000 rpm 10분 원심 후 여과",
   "standard": "업체 자체 데이터베이스(MWDB V3.0) 기반 동정·상대 정량", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "보라색 꽃의 강한 항산화·항암 활성과 가장 상관이 큰 성분으로 골라졌다[3]. 표준품 검량선이 없는 상대 정량이라 직선성·검출한계·회수율은 없다. 같은 연구실의 부위별 비교(뿌리·줄기·잎·꽃)도 같은 장비로 분석했다[2].",
  "source": [3, 2], "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10235515/", "source_kind": "paper"},
 {"role": "literature", "compound": "Eugenol", "compound_ko": "유제놀", "part": "꽃('Lorca', 발달 단계 S2–S6)",
  "content": "S4 0.00708, S5 0.02596, S6 0.04247 mmol/g(기준 무게는 본문에서 확인하지 못함)[4]",
  "method": "HS-SPME GC-MS",
  "conditions": {"instrument": "Shimadzu GCMS-QP2010", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "이온원 200 °C, 인터페이스 250 °C",
   "detection": "질량분석(NIST2011 라이브러리로 동정, Pherobase로 확인)", "injection": "SPME 섬유를 GC 주입구에 바로 꽂아 열 탈착",
   "sample_prep": "꽃을 15 mL 헤드스페이스 병에 넣어 무게를 잰 뒤 고체상 미량추출(SPME); 단계별 3반복",
   "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "유제놀은 카네이션 특유의 향을 내는 성분이어서 향 생합성 유전자 분석의 지표로 쓰였다[4]. 칼럼·온도 프로그램 등 세부 조건은 보충 자료에 있다고 되어 있어 본문에서 확인하지 못함.",
  "source": [4], "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9129081/", "source_kind": "paper"},
 {"role": "literature", "compound": "Flavone C-glycoside and flavonol O-glycosides", "compound_ko": "주요 플라보노이드 3종(플라본 C-배당체 1종, 플라보놀 O-배당체 2종)",
  "part": "꽃·잎·줄기·어린 싹·뿌리(9개 품종)", "content": "부위별 함량 분포로 품종 구별(수치는 초록에 없음)[7]",
  "method": "HPLC-UV",
  "conditions": {"instrument": "", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "UV", "injection": "", "sample_prep": "", "standard": "카네이션에서 분리하고 UV·MS·NMR로 구조를 정한 3개 성분", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "9개 품종 모두에서 주성분으로 나타난 플라보노이드 3종의 조직별 분포가 품종마다 달라, 간단하고 값싼 품종 판별 지표로 제안되었다[7]. 전문 확인 못함 — 성분명과 분석 조건은 초록에 없어 비워 둠.",
  "source": [7], "url": "https://pubmed.ncbi.nlm.nih.gov/18533456/", "source_kind": "paper"},
]

production = [
 {"metric": "area_ha", "region": "대한민국", "year": 2003, "value": 111.7, "unit": "ha", "note": "카네이션 재배면적. 김해시 누리집 자료를 WebSearch 요약으로만 확인(원문 미열람)", "source": [30]},
 {"metric": "area_ha", "region": "경상남도", "year": 2003, "value": 57.3, "unit": "ha", "note": "카네이션 재배면적. 김해시 누리집 자료를 WebSearch 요약으로만 확인(원문 미열람)", "source": [30]},
]

d = {"slug": "dianthus-caryophyllus", "name_ko": "카네이션", "name_en": "Carnation", "scientific_name": "Dianthus caryophyllus L.",
     "aliases": ["카네이션꽃", "향석죽(香石竹)", "clove pink", "carnation"],
     "sections": sections, "compounds": compounds, "markers": [], "assays": assays, "nutrients": [],
     "production": production, "world": [], "gi": [], "orgs": [], "sources": sources}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in sections: print(s["key"], len(s["body"]))
