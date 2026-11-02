import json
from pathlib import Path
P = Path(__file__).resolve().parent.parent
A = "2026-11-02"
def pm(n, title, pmid, pmc=None, journal="PubMed"):
    url = f"https://pmc.ncbi.nlm.nih.gov/articles/{pmc}/" if pmc else f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
    return {"n": n, "title": title, "url": url, "publisher": journal + (" (PMC)" if pmc else " (PubMed)"), "accessed": A}
S = [
 {"n": 1, "title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 모자반(Sargassum fulvellum) 1행 및 같은 속 원료 행(2026-10-13 받은 원자료)", "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
 pm(2, "Pharmaceutical and Nutraceutical Potential Applications of Sargassum fulvellum. Biomed Res Int 2020;2020:2417410 (종설, 전문)", "33110917", "PMC7582070", "BioMed Research International"),
 pm(3, "Fibrinolytic compounds isolated from a brown alga, Sargassum fulvellum. Mar Drugs 2009;7(2):85-94 (초록)", "19597573", None, "Marine Drugs"),
 pm(4, "Antipyretic, analgesic, and anti-inflammatory activities of the seaweed Sargassum fulvellum and Sargassum thunbergii in mice. J Ethnopharmacol 2008;116(1):187-90 (초록)", "18079077", None, "Journal of Ethnopharmacology"),
 pm(5, "A brown alga Sargassum fulvellum facilitates neuronal maturation and synaptogenesis. In Vitro Cell Dev Biol Anim 2012;48(8):535-44 (초록)", "22893212", None, "In Vitro Cellular & Developmental Biology - Animal"),
 pm(6, "Sargassum fulvellum Protects HaCaT Cells and BALB/c Mice from UVB-Induced Proinflammatory Responses. Evid Based Complement Alternat Med 2013;2013:747846 (초록)", "23935680", None, "Evidence-Based Complementary and Alternative Medicine"),
 pm(7, "Hexane fraction from Sargassum fulvellum inhibits lipopolysaccharide-induced inducible nitric oxide synthase expression in RAW 264.7 cells via NF-κB pathways. Am J Chin Med 2013;41(3):565-84 (초록)", "23711142", None, "American Journal of Chinese Medicine"),
 pm(8, "Anti-Inflammatory Effects of Grasshopper Ketone from Sargassum fulvellum Ethanol Extract on Lipopolysaccharide-Induced Inflammatory Responses in RAW 264.7 Cells. J Microbiol Biotechnol 2019;29(5):820-826 (초록)", "30982318", None, "Journal of Microbiology and Biotechnology"),
 pm(9, "In vivo and in vitro inhibitory activity of an ethanolic extract of Sargassum fulvellum and its component grasshopper ketone on atopic dermatitis. Int Immunopharmacol 2016;40:176-183 (초록)", "27608302", None, "International Immunopharmacology"),
 pm(10, "In Vitro and In Vivo Antioxidant Activities of Polysaccharides Isolated from Celluclast-Assisted Extract of an Edible Brown Seaweed, Sargassum fulvellum. Antioxidants (Basel) 2019;8(10):493 (전문)", "31635214", "PMC6826471", "Antioxidants"),
 pm(11, "In Vitro and In Vivo Anti-Inflammatory Effects of Sulfated Polysaccharides Isolated from the Edible Brown Seaweed, Sargassum fulvellum. Mar Drugs 2021;19(5):277 (전문)", "34063550", "PMC8155935", "Marine Drugs"),
 pm(12, "Degradation of fucoidans from Sargassum fulvellum and their biological activities. Carbohydr Polym 2014;111:822-9 (초록)", "25037421", None, "Carbohydrate Polymers"),
 pm(13, "Antitumor effect of seaweeds. II. Fractionation and partial characterization of the polysaccharide with antitumor activity from Sargassum fulvellum. Jpn J Exp Med 1977;47(3):133-40 (초록)", "916293", None, "Japanese Journal of Experimental Medicine"),
 pm(14, "Pheophytin a, a low molecular weight compound found in the marine brown alga Sargassum fulvellum, promotes the differentiation of PC12 cells. Int J Dev Neurosci 2007;25(1):63-8 (초록)", "17092682", None, "International Journal of Developmental Neuroscience"),
 pm(15, "Complete organellar genomes of six Sargassum species and development of species-specific markers. Sci Rep 2022;12:20981 (전문)", "36470932", "PMC9722929", "Scientific Reports"),
 pm(16, "The nucleotide sequences of 5S rRNAs from a multicellular green alga, Ulva pertusa, and two brown algae, Eisenia bicyclis and Sargassum fulvellum. Nucleic Acids Res 1983;11(6):1909-12 (초록)", "6835842", None, "Nucleic Acids Research"),
 pm(17, "Non-methylene-interrupted fatty acids with Δ5 unsaturation in Sargassum species. J Oleo Sci 2012;61(6):311-9 (초록)", "22687776", None, "Journal of Oleo Science"),
 pm(18, "Optimisation of sample treatment for arsenic speciation in alga samples by focussed sonication and ultrafiltration. Talanta 2005;68(5):1522-7 (초록)", "18970494", None, "Talanta"),
 pm(19, "Arsenic speciation in edible alga samples by microwave-assisted extraction and high performance liquid chromatography coupled to atomic fluorescence spectrometry. Anal Chim Acta 2012;714:38-46 (초록)", "22244135", None, "Analytica Chimica Acta"),
 pm(20, "Assessment of total arsenic and arsenic species stability in alga samples and their aqueous extracts. Talanta 2008;75(4):897-903 (초록)", "18585162", None, "Talanta"),
 pm(21, "Microwave assisted extraction of iodine and bromine from edible seaweed for inductively coupled plasma-mass spectrometry determination. Talanta 2009;79(3):947-52 (초록)", "19576469", None, "Talanta"),
 pm(22, "Lipid-Modulating Effects of Sargassum fulvellum Fermented by Lactic Acid Bacteria (KCCM12759P and KCCM12756P) in Ovariectomized Mice. Nutrients 2025;17(15):2527 (전문)", "40806110", "PMC12348090", "Nutrients"),
 pm(23, "Osteogenic Effects of Brown Algae-Derived Exosome-Like Nanovesicles via the BMP-2/4-MAPK-Smad1/5/8 Signaling Pathway. Prev Nutr Food Sci 2025;30(6):557-569 (초록)", "41492430", None, "Preventive Nutrition and Food Science"),
 pm(24, "Fucosterol-standardized extract of Sargassum fulvellum attenuates immobilization-induced skeletal muscle atrophy via PI3K/Akt/mTOR signaling. Food Sci Biotechnol 2026;35(9):2667-2678 (초록; PMC 전문 본문은 받지 못함)", "42534629", None, "Food Science and Biotechnology"),
 pm(25, "Hypotriglyceridemic effects of brown seaweed consumption via regulation of bile acid excretion and hepatic lipogenesis in high fat diet-induced obese mice. Nutr Res Pract 2020;14(6):580-592 (초록)", "33282121", None, "Nutrition Research and Practice"),
 pm(26, "Anti-inflammatory and anti-diabetic effects of brown seaweeds in high-fat diet-induced obese mice. Nutr Res Pract 2016;10(1):42-8 (전문)", "26865915", "PMC4742310", "Nutrition Research and Practice"),
 pm(27, "Effects of various kinds of edible seaweeds in diets on the development of D-galactosamine-induced hepatopathy in rats. J Nutr Sci Vitaminol 2007;53(4):315-23 (초록)", "17934236", None, "Journal of Nutritional Science and Vitaminology"),
 pm(28, "Effect of dietary fiber in edible seaweeds on the development of D-galactosamine-induced hepatopathy in rats. J Nutr Sci Vitaminol 2007;53(5):446-50 (초록)", "18079613", None, "Journal of Nutritional Science and Vitaminology"),
 pm(29, "Fucoxantin: a treasure from the sea. Mar Drugs 2012;10(3):604-616 (종설, 초록)", "22611357", None, "Marine Drugs"),
 pm(30, "Fucoxanthin as the major antioxidant in Hijikia fusiformis, a common edible seaweed. Biosci Biotechnol Biochem 1999;63(3):605-7 (초록)", "10227153", None, "Bioscience, Biotechnology, and Biochemistry"),
 pm(31, "Dokdonia lutea sp. nov., isolated from Sargassum fulvellum seaweed. Int J Syst Evol Microbiol 2017;67(11):4482-4486 (초록)", "28933321", None, "International Journal of Systematic and Evolutionary Microbiology"),
 pm(32, "Enhancement of Ethanol Production via Hyper Thermal Acid Hydrolysis and Co-Fermentation Using Waste Seaweed from Gwangalli Beach, Busan, Korea. J Microbiol Biotechnol 2018;28(3):401-408 (초록)", "29212293", None, "Journal of Microbiology and Biotechnology"),
 pm(33, "Cytotoxicity and inhibition of nitric oxide in lipopolysaccharide induced mammalian cell lines by aqueous extracts of brown seaweed. J Oleo Sci 2014;63(8):787-94 (초록)", "25007746", None, "Journal of Oleo Science"),
 pm(34, "Structural features of N-glycans of seaweed glycoproteins: predominant occurrence of high-mannose type N-glycans in marine plants. Biosci Biotechnol Biochem 2012;76(10):1996-8 (초록)", "23047116", None, "Bioscience, Biotechnology, and Biochemistry"),
 pm(35, "Fucoidan alleviates high sucrose-induced metabolic disorders and enhances intestinal homeostasis through modulation of Notch signaling. J Adv Res 2025;71:189-207 (초록)", "38825316", None, "Journal of Advanced Research"),
]
sections = [
 ("overview", "한눈에 보기",
  "모자반(Sargassum fulvellum (Turner) C. Agardh)은 모자반과(Sargassaceae)에 속하는 갈조류로, 한국·중국·일본 연안에 널리 분포한다[2]. 영어 이름은 'Gulf weed, Sea-lentil'로 식품원료 목록에 적혀 있다[1].\n\n"
  "식품원료로서의 지위: 식품의약품안전처 「식품원료 목록」에는 '모자반' 1행이 식품원료(A코드, 분류 '수산물')로 올라 있고, 상태는 '사용가능', 사용 조건은 '사용가능부위 : 전체'다[1]. 같은 목록 자료에서 건강기능식품 고시형 원료의 원재료로 연결된 기록은 없다[1].\n\n"
  "제주에서는 무침·국(몸국)·반찬으로 먹는 식용 해조로 소개된다[2]. 성분 연구는 푸코이단 같은 황산화 다당, 푸코잔틴, 플로로타닌, 그래스호퍼 케톤 같은 저분자 성분에 모여 있다[2][8]. 에탄올 추출물은 쥐 해마 신경세포의 성숙과 시냅스 형성을 도왔고(세포 실험, 최적 농도 5 μg/mL)[5], 에틸아세테이트 분획은 UVB를 쬔 각질세포와 생쥐 피부(바르는 방식)에서 염증 단백질을 줄였다(세포·동물 실험)[6]. 고지방식에 모자반 5%를 넣어 16주 먹인 생쥐에서는 공복 혈당과 혈장 중성지방이 줄었다(동물 실험)[25]. 효능 연구는 대부분 세포·동물 실험이며, 사람을 대상으로 한 임상 연구는 확인하지 못함."),
 ("history", "이용 역사",
  "2020년 종설은 모자반이 동양 의학에서 멍울(lumps)·부종(dropsy)·부기·고환 통증·배뇨 문제를 다스리는 데 쓰였고 식품 첨가물로도 널리 쓰였다고 정리했다[2]. 2013년 논문도 모자반이 멍울·부종·음낭 부기·배뇨 문제 같은 염증성 질환에 수 세기 동안 쓰였다고 소개했으나, 이는 그 논문의 서론 서술이다[7].\n\n"
  "먹거리로는 제주 사람들이 샐러드·국(몸국)·반찬으로 먹는다고 소개된다[2]. 일본에서는 'Hondawara', 중국에서는 'Wu Lei Ma Wei Zao', 한국에서는 'Mojaban'으로 불린다고 종설은 적었다[2].\n\n"
  "과학 연구는 1977년 연구에서 모자반 열수 추출물의 항종양 다당 분획을 얻은 것이 이른 예다[13]. 2007년 연구는 쥐 먹이에 넣은 식용 해조 11종 가운데 모자반을 포함한 4종이 D-갈락토사민 간 손상을 억제했다고 보고했고(동물 실험)[27], 후속 연구와 종설은 그 효과의 일부를 푸코이단에 돌렸다[2][28]. 종설은 2000년 이후 모자반 생리활성 논문이 40편 넘게 나왔다고 정리했다[2]."),
 ("biology", "생물학적 특징·생태",
  "모자반은 갈조강(Phaeophyceae) 모자반과의 해조로, 한국·중국·일본 연안에 널리 분포한다[2]. 모자반속(Sargassum) 해조는 특히 북동아시아의 아래 조간대 해안에 분포하고, 조간대·조하대에서 빽빽한 해중림을 이루어 여러 생물의 먹이와 서식처가 된다고 소개된다[15]. 모자반속 종은 겉모양 차이가 작고 환경·생장 단계에 따라 형태가 달라져 형태만으로 종을 가르기 어렵다[15].\n\n"
  "모자반 건조물은 탄수화물(셀룰로스·푸코이단·라미나란·알긴산) 30–60%, 단백질 15.8%, 회분 27.5%, 지방 약 5%를 담고 있다고 종설이 인용했다[2]. 당단백질의 N-글리칸은 고만노스형만 있었고, 모자반에서는 Man9GlcNAc2 구조가 주를 이루었다[34]. 지방산에는 Δ5 불포화의 비메틸렌 단절(NMI) 지방산이 소량 있었고, 그 가운데 5,9-에이코사디엔산은 조사한 모자반속 5종에서 총지방산의 0.4–2.3%였다[17].\n\n"
  "모자반 표면에서는 새로운 세균도 분리되었다[31]. 한국 남해에서 채집한 모자반에서 분리한 세균은 새 종 Dokdonia lutea로 제안되었다[31]."),
 ("related_species", "관련 종·이름",
  "식품원료 목록의 대표 원료명은 '모자반'이고 등록된 이명(별칭)은 없다[1]. 같은 목록에는 같은 속의 톳(S. fusiforme)·괭생이모자반(S. horneri)·꽈배기모자반(S. siliquastrum)·비틀대모자반(S. sagamianum)·알쏭이모자반(S. confusum)·지충이(S. thunbergii)·톱니모자반(S. serratifolium)이 학명이 다른 별도 원료로 올라 있다[1].\n\n"
  "2022년 연구는 한국에서 식품·의약 원료로 쓰이는 모자반속 6종의 엽록체·미토콘드리아 유전체를 해독했고, 이 가운데 모자반의 엽록체와 미토콘드리아 전체 유전체는 처음 보고된 것이다[15]. 같은 연구는 형태 동정이 어려워 가공 과정에서 여러 갈조류 원료가 섞이기 쉽다고 지적하고, 6종을 가르는 종 특이 실시간 PCR 표지를 만들었다[15].\n\n"
  "톳은 목록에 S. fusiforme로 올라 있고[1], 1999년 논문에서는 Hijikia fusiformis로 표기되었다[30]. 그 논문의 일본 식용 해조 DPPH 라디칼 소거능 비교에서 생 톳·미역 다음이 모자반이었다[30]. 2008년 생쥐 연구는 모자반과 지충이를 함께 시험했는데, 귀 부종 억제율 79.1%는 모자반 디클로로메탄 추출물, 72.1%는 지충이 에탄올 추출물의 값이다[4]."),
 ("cultivation", "서식·채취",
  "모자반의 국내 양식·채취 생산 통계는 공공 통계에서 확인하지 못함. 연구 시료의 출처는 자연 채집과 시판품이 섞여 있다[10][15][22][26]. 2017년 7월 제주 연안에서 채집해 수돗물로 씻고 동결건조한 시료가 쓰였다[10]. 모자반속 6종 유전체 연구의 시료는 제주·전남·전북의 섬과 연안에서 채집해 전문가가 형태로 동정했다[15].\n\n"
  "시판품으로는 제주 업체의 건조 모자반을 분쇄해 쓴 연구[22]와, 2014년 12월–2015년 3월 제주 재래시장에서 산 갈조류 4종을 동결건조해 쓴 생쥐 연구가 있다[26]. 해외 시료로는 일본 해안에서 채집한 모자반[14], 말레이시아산 갈조류 5종 가운데 하나로 시험한 모자반[33]이 있다.\n\n"
  "해변에 밀려온 해조로도 나온다[32]. 부산 광안리 해변에 쌓인 폐해조 바이오매스의 72%가 모자반(초록 표기 'Mojaban')이었다[32]. 모자반 양식 방법(종묘·가이식 등)은 공공기관 원문으로 확인하지 못함."),
 ("processing", "가공·추출 연구",
  "종설은 모자반 다당 추출이 현재 거의 열수 추출에만 의존하고 원료·추출·정제 방법이 통일되지 않아 다당의 구조와 활성이 연구마다 다르다고 지적했다[2]. 효소 추출 예로, 동결건조 분말 10 g을 셀룰라아제 효소 0.5 mL와 함께 pH 4.5, 50°C에서 24시간 반응시킨 추출물의 수율은 35.00%였고, 이를 95% 에탄올로 침전한 조다당(SFPS) 수율은 23.60 ± 2.01%였다[10].\n\n"
  "발효 가공도 연구되었다[22]. 건조 모자반 분말 5% 현탁액에 젖산균 두 균주를 1%씩 접종해 30°C에서 24시간 발효한 뒤 동결건조했다[22]. 푸코이단은 과산화수소 존재에서 초음파나 전자선을 쬐어 저분자화했는데, 전자선(과산화수소 1.5%, 2.5 kGy) 방식이 에너지 면에서 가장 효율적이었다[12]. 차등 초원심분리로 지름 약 208 nm의 엑소좀 유사 나노소포를 분리한 연구도 있다[23].\n\n"
  "푸코스테롤로 표준화한 모자반 추출물도 연구에 쓰였으나 표준화 함량은 초록에서 확인하지 못함[24]. 모자반을 원료로 한 건강기능식품 생산실적(식약처 「식품 등의 생산실적」)은 확인하지 못함."),
 ("genetics", "유전 정보",
  "2022년 연구는 모자반을 포함한 한국산 모자반속 6종의 엽록체·미토콘드리아 유전체를 해독했다[15]. 6종의 엽록체 유전체는 124,175–124,517 bp의 사분 원형 구조로, GC 함량 30.3–30.6%, 단백질 암호 유전자 139개, rRNA 유전자 3종 각 2벌을 담고 있었다[15]. 미토콘드리아 유전체는 34,620–34,793 bp, GC 함량 36.2–36.6%로 단백질 암호 유전자 37개와 rRNA 유전자 3개를 담고 있었다[15]. 이 수치는 6종 전체의 범위이며, 모자반 한 종의 값은 본문에서 따로 확인하지 못함.\n\n"
  "같은 연구는 6종 사이 엽록체 서열 유사도를 93.36–99.95%, 미토콘드리아는 87.91–99.81%로 보고했고, 단백질 암호 유전자의 단일염기변이를 바탕으로 엽록체 표지 13개와 미토콘드리아 표지 14개를 만들었다[15]. 1983년 연구는 모자반의 5S rRNA가 118개 뉴클레오타이드로 이루어져 있고, 녹조류·육상식물과 비슷한 갈파래와 달리 독특한 서열을 가진다고 보고했다[16]. 모자반의 핵 유전체 해독 보고는 확인하지 못함."),
 ("safety", "안전성",
  "식약처 「식품원료 목록」에서 모자반은 '사용가능' 원료이며 사용 조건은 '사용가능부위 : 전체'다[1]. 모자반에 대한 식약처 개별 기준(무기비소·요오드 등)은 이번 조사에서 확인하지 못함.\n\n"
  "비소: 모자반 시료에서 무기비소 화학종인 비산염(As(V))이 38 ± 2 µg/g 검출되었다(초록에 건조·생 기준 표기 없음)[18]. 모자반으로 만든 인증표준물질 NIES No. 9 'Sargasso'가 해조 비소·요오드 분석의 기준 시료로 쓰였다[19][20][21]. 이 표준물질의 As(V)는 폴리스타이렌 용기 +20°C에서 12개월 이상 안정했다[20]. 식용 해조 12종 조사에서 As(V)는 최고 77 µg/g이었으나 이는 여러 해조 전체의 값이다[19].\n\n"
  "요오드: 모자반 표준물질로 분석법을 검증했다는 보고는 있으나[21], 모자반의 요오드 함량 수치는 확인하지 못함. 독성: 모자반·지충이 추출물을 생쥐에 5 g/kg 먹였을 때 급성 독성은 관찰되지 않았다[4]. 종설은 모자반의 약동학과 표적 장기 독성 자료가 아직 부족하다고 지적했다[2]. 알레르기·잔류농약 등 공공기관 안전 정보는 확인하지 못함."),
]
compounds = [
 {"name": "Fucoidan", "name_ko": "푸코이단(황산화 다당)", "class": "황산화 다당", "role": "bioactive", "part": "엽상체(셀룰라아제 추출 후 에탄올 침전 조다당 SFPS)", "content_text": "SFPS 중 황산화 다당 74.55 ± 1.26%(탄수화물 73.54 ± 1.20%, 황산기 1.01 ± 0.06%)", "activity_ko": "SFPS는 Vero 세포와 제브라피시에서 AAPH 산화 스트레스를 줄였고[10], LPS 자극 대식세포(RAW 264.7)와 제브라피시에서 NO·염증성 사이토카인을 줄였다(세포·동물 실험)[11]. 모자반 유래 푸코이단은 고당 식이 초파리 유충에서 포도당·중성지방 상승을 억제했고, 생쥐에서는 장 상피 장벽에 미치는 영향이 조사되었다(동물 실험)[35]", "source": [10, 11, 35]},
 {"name": "L-Fucose", "name_ko": "푸코스", "class": "단당(다당 구성당)", "role": "marker", "part": "엽상체 조다당(SFPS)", "content_text": "SFPS 단당 상대 비율: 푸코스 26.75%, 갈락토스 33.77%, 자일로스 31.77%, 포도당 7.11%(HPAEC-PAD)", "activity_ko": "푸코이단의 주 구성당으로, 원문은 황산기·푸코스 함량을 황산화 다당 활성과 관련지었다[11]. 같은 논문 논의 부분에는 황산기·푸코스 값이 26.75%·1.01%로 뒤바뀌어 적혀 있어, 방법 절의 값(황산기 1.01%)을 따랐다[10][11]", "source": [10, 11]},
 {"name": "Alginic acid", "name_ko": "알긴산", "class": "다당(우론산 중합체)", "role": "nutrient", "part": "엽상체 건조물", "content_text": "탄수화물(셀룰로스·푸코이단·라미나란·알긴산 포함) 30–60%(건조물, 종설 인용값); 알긴산 단독 함량 수치 없음", "activity_ko": "갈조류의 알칼리 가용성 구조 다당으로 만누론산과 굴루론산으로 이루어진다[2]", "source": [2]},
 {"name": "Laminarin", "name_ko": "라미나란", "class": "저장 다당(β-글루칸)", "role": "nutrient", "part": "엽상체", "content_text": "함량 수치 없음(모자반 구성 다당으로 소개)", "activity_ko": "갈조류의 주요 저장 다당으로 β-1,3 글루칸 골격에 β-1,6 가지를 가진다[2]", "source": [2]},
 {"name": "Fucoxanthin", "name_ko": "푸코잔틴", "class": "카로티노이드(잔토필)", "role": "bioactive", "part": "엽상체", "content_text": "함량 수치 없음(모자반을 푸코잔틴 함유 식용 갈조류로 소개)", "activity_ko": "갈조류의 갈색을 내는 색소로, 생쥐 연구에서 항비만 작용이 보고된 기능 성분이다(동물 실험, 종설)[29]. 모자반의 주요 생리활성 저분자 성분으로 정리된다[2]", "source": [2, 29]},
 {"name": "Fucosterol", "name_ko": "푸코스테롤", "class": "스테롤", "role": "marker", "part": "엽상체 추출물", "content_text": "표준화 함량 수치는 초록에서 확인하지 못함", "activity_ko": "푸코스테롤로 표준화한 모자반 추출물이 TNF-α 자극 근관세포의 단백질 분해를 줄이고, 고정으로 근위축을 유도한 생쥐에서 악력과 근육량을 지켰다(세포·동물 실험)[24]", "source": [24]},
 {"name": "Grasshopper ketone", "name_ko": "그래스호퍼 케톤", "class": "저분자 화합물(헥산 분획에서 분리)", "role": "bioactive", "part": "엽상체 에탄올 추출물의 헥산 분획", "content_text": "함량 수치 없음(분리 보고)", "activity_ko": "100 μg/mL까지 RAW 264.7 세포에 독성이 없었고, 0.1–100 μg/mL에서 LPS 유도 IL-6·IL-1β·TNF-α 생성을 줄였다(세포 실험)[8]. 생쥐 비장세포의 사이토카인 생성도 낮췄다[9]", "source": [8, 9]},
 {"name": "Pheophytin a", "name_ko": "페오피틴 a", "class": "엽록소 관련 화합물", "role": "bioactive", "part": "엽상체(일본 해안 채집)", "content_text": "함량 수치 없음; 활성 농도 3.9 μg/mL", "activity_ko": "단독으로는 PC12 세포 신경돌기를 늘리지 않았으나, 낮은 농도의 신경성장인자(10 ng/mL)와 함께 주면 높은 농도(50 ng/mL)와 비슷한 신경돌기 성장을 보였다(세포 실험)[14]", "source": [14]},
 {"name": "1-O-Palmitoyl-2-O-oleoyl-3-O-(alpha-D-glucopyranosyl)glycerol", "name_ko": "글루코피라노실 다이아실글리세롤 POGG", "class": "당지질", "role": "bioactive", "part": "엽상체", "content_text": "함량 수치 없음(모자반에서 처음 분리)", "activity_ko": "pro-u-PA와 플라스미노겐 반응계에서 섬유소 용해 활성을 보였다(시험관 실험)[3]", "source": [3]},
 {"name": "1-O-Myristoyl-2-O-oleoyl-3-O-(alpha-D-glucopyranosyl)glycerol", "name_ko": "글루코피라노실 다이아실글리세롤 MOGG", "class": "당지질", "role": "bioactive", "part": "엽상체", "content_text": "함량 수치 없음(모자반에서 처음 분리)", "activity_ko": "POGG와 함께 분리되었고 같은 반응계에서 섬유소 용해 활성을 보였다(시험관 실험)[3]", "source": [3]},
 {"name": "Phylloquinone", "name_ko": "필로퀴논(비타민 K1)", "class": "지용성 비타민", "role": "nutrient", "part": "엽상체", "content_text": "함량 수치 없음(원문은 '풍부하다'고만 서술)", "activity_ko": "젖산균 발효 후에는 장쇄 메나퀴논(비타민 K2)이 늘었다고 이전 연구를 인용했다[22]", "source": [22]},
 {"name": "5,9-Eicosadienoic acid", "name_ko": "5,9-에이코사디엔산", "class": "비메틸렌 단절 지방산", "role": "bioactive", "part": "엽상체 지질", "content_text": "모자반속 5종(모자반 포함)에서 총지방산의 0.4–2.3%(종별 값은 초록에 없음)", "activity_ko": "조사한 NMI 지방산 가운데 가장 많았고 조류에서 처음 검출되었다[17]", "source": [17]},
 {"name": "Phlorotannins", "name_ko": "플로로타닌(폴리페놀)", "class": "폴리페놀", "role": "bioactive", "part": "엽상체 메탄올 추출물", "content_text": "메탄올 추출물의 폴리페놀 7.56 mg/g(종설 인용값); 셀룰라아제 추출물의 페놀 함량 1.78 ± 0.05%", "activity_ko": "메탄올 추출물의 폴리페놀 함량이 초과산화 음이온·DPPH 라디칼 소거능과 상관을 보였다고 종설이 정리했다(시험관 실험)[2][10]", "source": [2, 10]},
]
assays = [
 {"role": "literature", "compound": "Monosaccharide composition (fucose, galactose, xylose, glucose)", "compound_ko": "조다당 구성당(푸코스 등)", "part": "엽상체(제주 연안 채집, 동결건조 분말)의 셀룰라아제 추출·에탄올 침전 조다당", "content": "SFPS 단당 상대 비율 푸코스 26.75%, 갈락토스 33.77%, 포도당 7.11%, 자일로스 31.77%; SFPS 탄수화물 73.54 ± 1.20%, 황산기 1.01 ± 0.06%", "method": "HPAEC-PAD(고성능 음이온교환 크로마토그래피-펄스 전류 검출)",
  "conditions": {"instrument": "", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "펄스 전류 검출(PAD)", "injection": "", "sample_prep": "동결건조 분말 10 g + 증류수 999.5 mL + 셀룰라아제 0.5 mL, pH 4.5, 50°C 24시간 교반(120 rpm) → 100°C 10분 효소 불활성화 → pH 7 조정 → 95% 에탄올 2 L로 침전; 총탄수화물·페놀은 AOAC 법, 황산기는 BaCl2-젤라틴 법", "standard": "단당 표준곡선", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "푸코스·황산기는 모자반 황산화 다당(푸코이단)의 활성과 관련된 지표로 쓰였다[11]. 전문(Methods)을 확인했으나 칼럼·용리 조건은 '이전 연구 방법'으로만 적혀 있어 비워 두었다[10][11].", "source": [10, 11], "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8155935/", "source_kind": "paper"},
 {"role": "literature", "compound": "Arsenate (As(V))", "compound_ko": "비산염(무기비소 As(V))", "part": "모자반 건조 시료", "content": "38 ± 2 µg/g", "method": "HPLC-ICP-AES(음이온교환)",
  "conditions": {"instrument": "HPLC-ICP-AES", "column": "Hamilton PRP-X100", "mobile_phase": "17 mM 인산 완충액, pH 5.5", "gradient": "", "flow": "1.0 mL/min", "temp": "", "detection": "ICP-AES", "injection": "100 µL", "sample_prep": "물 5 mL로 집속 초음파 30초 추출 → 14,000×g 10분 원심분리, 3회 반복; 한외여과(10 kDa)로 정제", "standard": "", "linearity": "", "lod": "화학종당 비소 약 20 ng(주입량 100 µL 기준)", "loq": "", "recovery": ""},
  "rationale": "해조 섭취의 주요 위해 요소인 무기비소를 모자반 시료에서 화학종별로 정량했다[18]. As(III)·As(V)·MMA·DMA를 13분 안에 분리했다[18]. 초록에서 확인한 조건만 적었고 전문 확인 못함.", "source": [18], "url": "https://pubmed.ncbi.nlm.nih.gov/18970494/", "source_kind": "paper"},
]
d = {
 "slug": "sargassum-fulvellum", "name_ko": "모자반", "name_en": "Sargassum fulvellum (Gulf weed, Sea-lentil)",
 "scientific_name": "Sargassum fulvellum", "aliases": ["Sargassum fulvellum (Turner) C. Agardh", "Hondawara(일본명)", "Mojaban"],
 "sections": [{"key": k, "title": t, "body": b} for k, t, b in sections],
 "compounds": compounds, "markers": [],
 "nutrients": [{"form": "건조 엽상체", "basis": "건조물 100 g당(종설이 인용한 % 값을 g으로 옮김; 원 연구는 확인하지 못함). 탄수화물은 30–60%로 범위만 제시", "items": [{"name": "단백질", "value": 15.8, "unit": "g"}, {"name": "회분", "value": 27.5, "unit": "g"}, {"name": "지질", "value": 5, "unit": "g"}], "source": [2]}],
 "production": [], "world": [], "assays": assays, "gi": [], "orgs": [], "sources": S,
}
(P / "dossier.json").write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in d["sections"]: print(s["key"], len(s["body"]))
