import json
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "dossier.json"
ACC = "2026-11-02"


def pm(title, doi, pmid, pmc=None, note=""):
    t = f"{title} (PMID {pmid}"
    if pmc:
        t += f", {pmc}"
    t += f"{', ' + note if note else ''})"
    return {"title": t, "url": f"https://doi.org/{doi}", "publisher": "PubMed", "accessed": ACC}


S = [
    {"title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 건조레몬버베나·레몬버베나분말·레몬버베나잎·레몬버베나잎추출물(Aloysia citrodora Palau / Aloysia triphylla Britton; Lemon verbena), 사용가능, 사용가능부위: 잎; 건강기능식품(C코드) 개별인정 '레몬버베나추출물 등 복합물'(제2022-13호, 레몬버베나 잎·히비스커스); 마편초(Verbena officinalis L.) 사용불가, 호리버베인잎(Verbena stricta) 제한적사용 행 대조 (로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json)",
     "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
    pm("Impact of Simulated Gastrointestinal Digestion on Antiglycoxidant Activity of Lemon Verbena (Aloysia citrodora) Herbal Tea and Characterization of Key Polyphenols via DPPH/MGO Pre-Column HPLC — Antioxidants (Basel) 2026;15(6):717", "10.3390/antiox15060717", "42352023", "PMC13295418", "전문 확인"),
    pm("Volatile Compounds and Biological Activity of the Essential Oil of Aloysia citrodora Paláu: Comparison of Hydrodistillation and Microwave-Assisted Hydrodistillation — Molecules 2023;28(11):4528", "10.3390/molecules28114528", "37299006", "PMC10254266", "전문 확인"),
    pm("Aloysia citrodora Polyphenolic Extract: From Anti-Glycative Activity to In Vitro Bioaccessibility and In Silico Studies — Nutrients 2025;18(1):115", "10.3390/nu18010115", "41515232", "PMC12787967", "전문 확인"),
    pm("Northwestern Argentina: a center of genetic diversity of lemon verbena (Aloysia citriodora PALÁU, Verbenaceae) — Chem Biodivers 2013;10(2):251-61", "10.1002/cbdv.201100416", "23418172", None, "초록"),
    pm("Aloysia citrodora Paláu (Lemon verbena): A review of phytochemistry and pharmacology — J Ethnopharmacol 2018;222:34-51", "10.1016/j.jep.2018.04.021", "29698776", None, "초록"),
    pm("HPLC-DAD coupled to electrospray TOF and ion-trap tandem MS to identify phenolic compounds from a lemon verbena extract — J Chromatogr A 2009;1216(28):5391-7", "10.1016/j.chroma.2009.05.038", "19500792", None, "초록"),
    pm("HPLC-DAD-ESI-MS analysis of the constituents of aqueous preparations of verbena and lemon verbena and evaluation of the antioxidant activity — J Pharm Biomed Anal 2008;46(3):463-70", "10.1016/j.jpba.2007.11.007", "18155378", None, "초록"),
    pm("The Potential Synergistic Modulation of AMPK by Lippia citriodora Compounds as a Target in Metabolic Disorders — Nutrients 2019;11(12):2961", "10.3390/nu11122961", "31817196", "PMC6950112", "초록"),
    pm("Phenylpropanoids and their metabolites are the major compounds responsible for blood-cell protection against oxidative stress after administration of Lippia citriodora in rats — Phytomedicine 2013;20(12):1112-8", "10.1016/j.phymed.2013.05.007", "23827667", None, "초록"),
    pm("Bioavailability of lemon verbena (Aloysia triphylla) polyphenols in rats: impact of colonic inflammation — Br J Nutr 2014;111(10):1773-81", "10.1017/S0007114514000026", "24513110", None, "초록"),
    pm("Differential effects of a combination of Hibiscus sabdariffa and Lippia citriodora polyphenols in overweight/obese subjects: A randomized controlled trial — Sci Rep 2019;9(1):2999", "10.1038/s41598-019-39159-5", "30816148", "PMC6395806", "초록"),
    pm("The effect of Lippia Citriodora (LC) extract on cardiometabolic risk factors: a systematic review and meta-analysis — Nutr Diabetes 2026;16(1)", "10.1038/s41387-026-00420-2", "42191680", "PMC13392351", "초록"),
    pm("Dietary Supplementation with an Extract of Aloysia citrodora (Lemon verbena) Improves Sleep Quality in Healthy Subjects: A Randomized Double-Blind Controlled Study — Nutrients 2024;16(10):1523", "10.3390/nu16101523", "38794761", "PMC11123999", "초록"),
    pm("Aloysia citriodora Palau (lemon verbena) for insomnia patients: A randomized, double-blind, placebo-controlled clinical trial of efficacy and safety — Phytother Res 2019;33(2):350-359", "10.1002/ptr.6228", "30450627", None, "초록"),
    pm("Effects of lemon verbena extract supplementation on muscle strength and recovery after exhaustive exercise: a randomized, placebo-controlled trial — J Int Soc Sports Nutr 2018;15:5", "10.1186/s12970-018-0208-0", "29410606", "PMC5781260", "초록"),
    pm("Daily supplementation with lemon verbena extract decreases subjective energy and parental reports of hyperactivity in children displaying sub-clinical ADHD-type behaviours: A randomised controlled trial — J Psychopharmacol 2025;39(8):825-835", "10.1177/02698811251324574", "40251851", "PMC12287557", "초록"),
    pm("Phylogeny of Lantana, Lippia, and related genera (Lantaneae: Verbenaceae) — Am J Bot 2021;108(8):1354-1373", "10.1002/ajb2.1708", "34418063", None, "초록"),
    pm("Origins of North American arid-land Verbenaceae: More than one way to skin a cat — Am J Bot 2017;104(11):1708-1716", "10.3732/ajb.1700292", "29170247", None, "초록"),
    pm("Molecular phylogeny and evolution of the genus Neoerysiphe (Erysiphaceae, Ascomycota) — Mycol Res 2008;112(Pt 6):639-49", "10.1016/j.mycres.2008.01.004", "18495450", None, "초록"),
    pm("Cardioprotective Effects of Aloysia polystachya Essential Oil on a Rat Model with Multiple Cardiovascular Risk Factors — Planta Med 2024;90(9):708-716", "10.1055/a-2294-6922", "38631368", None, "초록"),
    pm("Antinociceptive effect and mechanism of supercritical carbon dioxide extract of Aloysia gratissima leaves in mice — Biomed J 2020;44(6 Suppl 1):S63-S72", "10.1016/j.bj.2020.06.009", "35747996", "PMC9038947", "초록"),
    {"title": "European Medicines Agency HMPC — Verbenae citriodorae folium (Aloysia citrodora Paláu, syn. Aloysia triphylla (L'Hér.) Kuntze, Verbena triphylla L'Hér., Lippia citriodora Kunth, folium) EU herbal monograph 문서 목록(EMA/HMPC/376770/2019, HMPC 의견 2021-01-13) — ema.europa.eu 가 이 환경의 네트워크 허용 목록 밖이라 원문을 열지 못하고 WebSearch 결과 요약으로만 확인함",
     "url": "https://www.ema.europa.eu/en/medicines/herbal/verbenae-citriodorae-folium", "publisher": "European Medicines Agency", "accessed": ACC},
    {"title": "식품의약품안전처 「식품 등의 생산실적」 2024년·2025년 — 건강기능식품 개별인정형 '레몬버베나추출물 등 복합물' 행(생산·판매 톤, 생산액·판매액 천원; 로컬 파싱본 docs/stats/hf_items.csv)",
     "url": "https://www.mfds.go.kr", "publisher": "식품의약품안전처", "accessed": ACC},
    pm("Exploring reserve lots of Cymbopogon citratus, Aloysia citrodora and Thymus × citriodorus as improved sources of phenolic compounds — Food Chem 2018;257:83-89", "10.1016/j.foodchem.2018.03.006", "29622234", None, "초록"),
    pm("A Novel HPLC Method for Direct Detection of Nitric Oxide Scavengers from Complex Plant Matrices and Its Application to Aloysia triphylla Leaves — Molecules 2018;23(7):1574", "10.3390/molecules23071574", "29958472", "PMC6100114", "초록"),
    pm("Anxiolytic Effect and Improved Sleep Quality in Individuals Taking Lippia citriodora Extract — Nutrients 2022;14(1):218", "10.3390/nu14010218", "35011093", "PMC8747367", "초록"),
]
for i, s in enumerate(S, 1):
    s["n"] = i
S = [{"n": s["n"], **{k: v for k, v in s.items() if k != "n"}} for s in S]

sections = [
    {"key": "overview", "title": "한눈에 보기", "body":
     "레몬버베나(Aloysia citrodora Paláu)는 마편초과(Verbenaceae)에 속하는 향기 나는 여러해살이 식물로, 원산지는 남아메리카의 아르헨티나·칠레다[4]. 잎에서 레몬 향이 나며 예부터 잎을 우린 차를 소화 불량·불면·스트레스에 썼다[4, 6]. 식약처 「식품원료 목록」에는 건조레몬버베나·레몬버베나분말·레몬버베나잎·레몬버베나잎추출물 네 행이 '사용가능' 원료로 올라 있고, 학명은 Aloysia citrodora Palau / Aloysia triphylla Britton, 사용 조건은 '사용가능부위 : 잎'이다[1]. 따라서 일반 식품에는 잎만 쓸 수 있고, 줄기·꽃·뿌리는 이 목록에서 사용 가능 부위로 확인하지 못함. 같은 목록의 건강기능식품(C코드)에는 레몬버베나 잎과 히비스커스를 섞은 개별인정형 원료 '레몬버베나추출물 등 복합물'(제2022-13호)이 있으며, 고시형 원료의 원재료로는 올라 있지 않다[1].\n\n잎 추출물의 대표 성분은 페닐에탄올 배당체인 베르바스코사이드(액테오사이드)이고, 잎 정유의 주성분은 시트랄 이성질체인 게라니알과 네랄이다[6]. 시판 잎을 우린 차에서는 베르바스코사이드가 마른 잎 1 g당 36.5 mg으로 가장 많았다[2]. 이름이 비슷한 버베나(마편초, Verbena officinalis)는 다른 속의 식물이며, 식품원료 목록에서 '사용불가'로 분류된다[1]."},
    {"key": "history", "title": "역사", "body":
     "레몬버베나는 남아메리카 고유종으로 여겨지며, 17세기에 스페인과 포르투갈 사람들이 유럽에 들여온 뒤 북아프리카와 남유럽에서 널리 재배되었다[3]. 아르헨티나 북서부는 이 종의 원산지로 거듭 제시된 곳이다[5]. 원산지 사람들은 설사·복부 팽만·불면·류머티즘 등에 이 식물을 써 왔다[6]. 민간에서는 위장 장애, 불면과 불안, 기관지염, 심장 질환에 쓰였고 진경·이뇨 작용이 있다고 전해졌다[3]. 잎 우린 물은 위장 장애, 열, 천식성 경련, 경련성 복통, 설사, 그리고 스트레스·불안·불면 같은 신경계 증상에 쓰였고, 오늘날에는 상쾌한 음료로도 마신다[4]. 현대 임상시험에서는 수면 문제가 있는 건강한 성인 71명이 잎 추출물을 90일 먹고 위약보다 수면 질(PSQI)이 좋아졌고[14], 불면 환자 100명에게 시럽을 4주 준 시험에서도 PSQI와 불면 심각도가 개선되었다[15].\n\n레몬 향 덕분에 잎과 정유는 향수·화장품·식품 산업에서 쓰이며, 일부 지역에서는 생잎이나 말린 잎을 청량음료, 리큐어, 푸딩, 잼의 향료로 쓴다[3]. 유럽연합 의약품청(EMA) 약초위원회(HMPC)는 레몬버베나 잎(Verbenae citriodorae folium)에 대한 EU 약초 모노그래프를 채택했으며, 의견서 날짜는 2021년 1월 13일이다(원문은 열지 못하고 검색 요약으로만 확인)[23]. 국내에서 언제부터 재배·유통되었는지는 확인하지 못함."},
    {"key": "biology", "title": "식물학적 특징", "body":
     "레몬버베나는 마편초과 알로이시아속(Aloysia)에 속하는 향기 나는 여러해살이 식물이다[4]. 원산지는 아르헨티나와 칠레를 중심으로 한 남아메리카이며, 잎에서 얻는 정유에 모노테르펜과 세스퀴테르펜이 많아 특유의 레몬 향이 난다[4]. 포르투갈산 말린 잎의 정유에서는 69개 성분이 확인되었고, 산소를 포함한 모노테르펜이 49.7–53%를 차지했다[3]. 정유의 주성분은 게라니알(18.7–21.1%)과 네랄(15.3–16.2%)이었고, 스파툴레놀·카리오필렌 옥사이드·리모넨·ar-쿠르쿠멘이 뒤를 이었다[3].\n\n물에 녹는 성분으로는 이리도이드 배당체, 페닐에탄올 배당체, 페닐프로파노이드 배당체, 플라보노이드 유도체가 있다[4]. 잎을 우린 물에는 극성이 큰 플라본 이글루쿠로나이드(루테올린-7-O-이글루쿠로나이드 등)와 베르바스코사이드가 주로 녹아 나온다[2]. 정유 조성은 개체에 따라 크게 달라서, 아르헨티나 북서부의 25개 집단에서는 뚜렷한 화학형(chemotype)이 4가지 이상 확인되었다[5]. 이 종은 흰가루병균의 새 기주로 보고되었고, 잎에 생긴 균은 Oidium aloysiae라는 새 종으로 기재되었다[20]. 잎 배열·꽃 구조·염색체 수 같은 형태 정보는 이번에 1차 자료로 확인하지 못함."},
    {"key": "related_species", "title": "이름과 가까운 종", "body":
     "학명은 Aloysia citrodora Paláu이며, 논문에서는 이명 Lippia citriodora Kunth, Aloysia triphylla, Lippia citrodora가 함께 쓰이고 영어로는 lemon verbena 또는 lemon beebrush라고 부른다[6]. 식약처 식품원료 목록은 Aloysia citrodora Palau와 Aloysia triphylla Britton을 같은 원료의 학명으로 함께 적는다[1]. 리피아속(Lippia)과 란타나속(Lantana)의 핵 DNA 계통 분석에서는 두 속 모두 단계통이 아니었고, 알로이시아속의 몇몇 종이 이 무리 안에 들어갔다[18].\n\n'버베나'라는 이름 때문에 마편초(Verbena officinalis)와 혼동하기 쉽지만 둘은 다른 속이며, 식품원료 목록에서 마편초·마편초지상부·마편초꽃은 '사용불가', 호리버베인잎(Verbena stricta)은 '제한적사용'으로 레몬버베나와 지위가 다르다[1]. 같은 속의 Aloysia polystachya 잎 정유는 카르본(56.47%)과 리모넨(40.13%)이 주성분이라 시트랄이 많은 레몬버베나와 향이 다르다[21]. Aloysia gratissima 잎 추출물에서는 구아이올과 피노캄폰 같은 세스퀴테르펜이 확인되었다[22]. 레몬 향 허브인 레몬밤(Melissa officinalis)과 레몬그라스(Cymbopogon citratus)는 다른 과의 식물로, 식품원료 목록에 따로 올라 있다[1]."},
    {"key": "cultivation", "title": "재배와 산지", "body":
     "레몬버베나는 남아메리카가 고향이지만 지금은 세계 여러 곳에서, 특히 북아프리카와 남유럽에서 재배된다[3]. 아르헨티나 살타주 세리요스의 시험 포장에서는 여섯 곳에서 모은 집단을 7년 넘게 같은 땅에서 길러 비교했다[5]. 잎의 정유 수율은 0.4–2.1%(v/w)로 집단마다 크게 달랐지만 대부분 유럽약전 규격을 충족했고, 2010년에 채취한 시료의 액테오사이드 함량은 0.5–4.0%였다[5].\n\n수확 시기도 품질을 바꾼다[3]. 그리스산 잎에서는 5월에서 9월로 갈수록 시트랄 이성질체가 줄고 리모넨이 늘었다[3]. 상업 재배에는 시트랄과 리모넨이 많은 화학형이 선택되며, 이 성분이 적은 화학형은 향이 떨어져 재배용으로 잘 고르지 않는다[3]. 포르투갈의 차 회사가 고른 '리저브' 로트는 일반 로트보다 페놀 화합물이 많아, 수확 조건에 따라 성분이 달라짐을 보여 주었다[25]. 국내 재배 면적·생산량 통계(통계청·농식품부 특용작물 생산실적)에서는 레몬버베나 항목을 확인하지 못함."},
    {"key": "processing", "title": "가공과 이용", "body":
     "가장 흔한 이용법은 말린 잎을 끓는 물에 우린 허브차다[2]. 우린 차의 총페놀은 마른 잎 1 g당 58.0 mg GAE였고, 그중 약 70%(39.0 mg 베르바스코사이드 당량)가 페놀산이었다[2]. 시험관 소화 실험에서 베르바스코사이드는 위 단계에서는 안정했지만 장 단계에서 20.8% 줄었고, 그만큼 이소베르바스코사이드와 카페산이 늘었다[2].\n\n정유는 잎을 물로 증류해 얻으며, 포르투갈산 말린 잎에서 수율은 클레벤저 증류 1.05%, 마이크로파 보조 증류 1.29%였다[3]. 페닐프로파노이드를 정제한 잎 추출물은 건강기능 소재로 쓰이며, 이런 추출물을 8주 먹은 사람에서 스트레스 인식과 코르티솔이 줄었다는 시험이 있다[27]. 레몬버베나·히비스커스 폴리페놀 추출물 하루 500 mg을 2개월 먹은 과체중 성인은 위약군보다 허리둘레가 더 줄었다[12]. 11개 무작위 대조시험(503명)을 묶은 메타분석에서는 체중이 평균 2.09 kg 줄었지만 혈당 지표는 달라지지 않았다[13]. 국내에서는 레몬버베나 잎과 히비스커스를 섞은 개별인정형 원료 '레몬버베나추출물 등 복합물'(제2022-13호)이 등록되어 있다[1]. 식약처 생산실적에서 이 원료는 2024년 5톤, 생산액 1,235,426천원(약 12.4억 원)이었고, 2025년에는 10톤, 생산액 3,437,801천원(약 34.4억 원)이었다[24]."},
    {"key": "genetics", "title": "유전 정보", "body":
     "레몬버베나의 염색체 수, 유전체 크기, 엽록체 유전체 해독 여부는 이번 조사에서 1차 자료로 확인하지 못함. 계통 연구에서는 리피아·란타나와 가까운 속들을 핵 유전자 7곳(ITS, ETS, PPR 5곳)으로 88개 표본을 분석했고, 알로이시아속 일부 종이 이 무리 안에 섞여 들어갔다[18]. 이 무리는 남아메리카에서 생겨나 그곳에서 분화했다[18]. 북아메리카 건조지에 사는 알로이시아속 종들은 남아메리카 온대 건조지의 조상에서 장거리 분산으로 갈라져 나온 것으로 추정되었다[19].\n\n종 안의 다양성도 크다[5]. 아르헨티나 북서부는 레몬버베나의 유전적 다양성 중심지로 제안되었고, 이곳 집단에서는 정유 조성이 서로 다른 화학형이 최소 4가지 확인되어 유전자원 보전이 필요하다고 지적되었다[5]. 아르헨티나 수집 계통을 비교한 연구에서는 유전형이 정유 조성에 가장 큰 영향을 주는 요인이었다고 인용된다[3]. 모로코산처럼 게라니알이 검출되지 않고 세스퀴테르펜이 많은 화학형도 보고되었다[3]."},
    {"key": "safety", "title": "안전성", "body":
     "레몬버베나는 식약처 식품원료 목록에서 잎에 한해 '사용가능' 원료이므로 잎 외의 부위는 식품에 쓸 수 없다[1]. 이름이 비슷한 마편초(Verbena officinalis)는 '사용불가' 원료이므로 '버베나' 제품을 살 때 학명을 확인하는 것이 좋다[1]. EMA 약초위원회 모노그래프는 잎 허브차를 다루며 이상반응을 '알려진 바 없음'으로 적었고, 초안에서는 어린이 사용을 권하지 않았다(원문 미확인, 검색 요약)[23]. 하루 400 mg 추출물을 15일 먹인 시험에서는 안전하고 잘 견딘다고 보고되었다[16]. 8–17세 120명에게 체중 1 kg당 하루 15 mg을 56일 준 시험에서도 예상치 못한 안전성 문제는 없었지만, 위약보다 주관적 피로(활력 저하)를 더 많이 보고했다[17].\n\n정유는 잎차와 다르게 다뤄야 한다[3]. 클레벤저로 얻은 정유는 정상 돼지 간세포(PLP2)에 대해 GI50 18 μg/mL로 강한 세포독성을 보여, 정유를 먹는 용도로 쓰려면 간 독성 평가가 더 필요하다고 저자들이 지적했다[3]. 종설은 이 식물의 사람 대상 안전성과 효능이 충분히 평가되지 않았다고 결론지었다[6]. 알레르기 표시 대상 여부, 잔류농약·중금속 등 공공기관의 안전 정보는 확인하지 못함."},
]

compounds = [
    {"name": "Verbascoside", "name_ko": "베르바스코사이드(액테오사이드)", "class": "페닐에탄올 배당체(카페산 에스터)", "role": "marker", "part": "잎",
     "content_text": "잎 허브차(5 g/100 mL, 30분 우림) 마른 잎 1 g당 36.5 mg, 장 단계 소화 뒤 28.9 mg[2]; 아르헨티나 북서부 집단 0.5–4.0%[5]; 잎 메탄올 추출물 1 mg/mL 용액에서 7.40 µg/mL[4]; 버베나·레몬버베나 수성 제제의 페닐프로파노이드 16–120 mg/g 건조 추출물 중 최대 97%(두 식물 제제를 함께 보고)[8]",
     "activity_ko": "추출물의 주성분이자 AMPK 활성화의 주된 기여 성분(지방세포 모델)[9]; NO 소거 IC50 56 µg/mL[26]; 쥐 혈장에서 80 ng/mL 검출[10]", "source": [2, 4, 5, 8, 9, 10, 26]},
    {"name": "Isoverbascoside", "name_ko": "이소베르바스코사이드", "class": "페닐에탄올 배당체", "role": "bioactive", "part": "잎",
     "content_text": "허브차 마른 잎 1 g당 2.5 mg, 장 단계 소화 뒤 4.10 mg[2]; 잎 메탄올 추출물 1 mg/mL 용액에서 4.72 VE µg/mL[4]",
     "activity_ko": "NO 소거 IC50 51 µg/mL[26]; 쥐 혈장에서 57 ng/mL 검출[10]", "source": [2, 4, 10, 26]},
    {"name": "Luteolin 7-diglucuronide", "name_ko": "루테올린-7-O-이글루쿠로나이드", "class": "플라본 배당체", "role": "marker", "part": "잎",
     "content_text": "허브차 마른 잎 1 g당 13.1 mg, 소화 뒤에도 13.4 mg으로 유지[2]",
     "activity_ko": "NO 소거 IC50 69 µg/mL[26]; 지방세포 모델에서 AMPK 활성화, 로간산과 상승작용[9]", "source": [2, 9, 26]},
    {"name": "Apigenin 7-diglucuronide", "name_ko": "아피제닌-7-이글루쿠로나이드", "class": "플라본 배당체", "role": "bioactive", "part": "잎",
     "content_text": "HPLC-DAD-TOF/MS로 확인(함량 초록에 미기재)[7]",
     "activity_ko": "쥐에서 플라본류는 아글리콘 포합체로 소변 배설[11]", "source": [7, 11]},
    {"name": "Chrysoeriol 7-diglucuronide", "name_ko": "크리소에리올-7-이글루쿠로나이드", "class": "플라본 배당체", "role": "bioactive", "part": "잎",
     "content_text": "레몬버베나에서 처음 확인된 성분 중 하나(함량 초록에 미기재)[7]",
     "activity_ko": "확인하지 못함(초록에 활성 기재 없음)[7]", "source": [7]},
    {"name": "Caffeic acid", "name_ko": "카페산", "class": "히드록시신남산", "role": "bioactive", "part": "잎(차·소화물)",
     "content_text": "허브차에서는 흔적량, 장 단계 소화 뒤 마른 잎 1 g당 1.0 mg[2]",
     "activity_ko": "베르바스코사이드 분해·대사 산물로 쥐 소변·혈장에서 검출[10, 11]", "source": [2, 10, 11]},
    {"name": "Loganic acid", "name_ko": "로간산", "class": "이리도이드 배당체", "role": "bioactive", "part": "잎",
     "content_text": "잎 메탄올 추출물에서 LC-MS로 확인(정량값 없음)[4]",
     "activity_ko": "지방세포 모델에서 AMPK 활성화가 큰 3개 성분 중 하나[9]", "source": [4, 9]},
    {"name": "Geniposidic acid", "name_ko": "게니포시드산", "class": "이리도이드 배당체", "role": "bioactive", "part": "잎",
     "content_text": "잎 메탄올 추출물에서 LC-MS로 확인(정량값 없음)[4]",
     "activity_ko": "추출물의 항당화 활성에 기여하는 이리도이드 계열로 제시됨(개별 활성 미측정)[4]", "source": [4]},
    {"name": "Geranial", "name_ko": "게라니알(시트랄 a)", "class": "모노테르펜 알데하이드", "role": "marker", "part": "잎 정유",
     "content_text": "포르투갈산 말린 잎 정유 18.7–21.1%(GC-MS 피크 면적 %); 인용 문헌 포르투갈 26.80–38.30%, 그리스 26.8–38.7%[3]",
     "activity_ko": "정유 레몬 향의 주성분, 정유 항산화 활성 설명 성분[3, 6]", "source": [3, 6]},
    {"name": "Neral", "name_ko": "네랄(시트랄 b)", "class": "모노테르펜 알데하이드", "role": "marker", "part": "잎 정유",
     "content_text": "포르투갈산 말린 잎 정유 15.3–16.2%; 인용 문헌 포르투갈 20.80–29.60%, 그리스 21.8–24.5%[3]",
     "activity_ko": "게라니알과 함께 정유 주성분[3, 6]", "source": [3, 6]},
    {"name": "Limonene", "name_ko": "리모넨", "class": "모노테르펜", "role": "bioactive", "part": "잎 정유",
     "content_text": "포르투갈산 정유 5.0–5.4%; 인용 문헌 포르투갈 5.70–20.60%, 그리스 5.8–17.7%[3]",
     "activity_ko": "레몬 향 기여, 수확이 늦을수록 증가[3]", "source": [3]},
    {"name": "Spathulenol", "name_ko": "스파툴레놀", "class": "세스퀴테르펜 알코올", "role": "bioactive", "part": "잎 정유",
     "content_text": "포르투갈산 정유 7.2–8.7%[3]",
     "activity_ko": "클레벤저 정유의 대식세포 NO 억제 활성을 가장 크게 설명한 성분(통계 모형)[3]", "source": [3]},
    {"name": "Caryophyllene oxide", "name_ko": "카리오필렌 옥사이드", "class": "세스퀴테르펜 산화물", "role": "bioactive", "part": "잎 정유",
     "content_text": "포르투갈산 정유 5.3–5.6%[3]",
     "activity_ko": "모로코산 세스퀴테르펜 화학형의 주성분 중 하나[3]", "source": [3]},
    {"name": "ar-Curcumene", "name_ko": "ar-쿠르쿠멘", "class": "세스퀴테르펜", "role": "bioactive", "part": "잎 정유",
     "content_text": "포르투갈산 정유 4.7–5.3%[3]",
     "activity_ko": "마이크로파 보조 증류 정유의 항산화 활성 차이를 설명한 성분 중 하나[3]", "source": [3]},
]

assays = [
    {"role": "literature", "compound": "Verbascoside", "compound_ko": "베르바스코사이드(이소베르바스코사이드·루테올린-7-O-이글루쿠로나이드·카페산 동시 정량)",
     "part": "잎 허브차(프랑스 허브차 업체의 말린 잎 4로트 혼합, 5.0 g/100 mL 끓는 물 30분)",
     "content": "마른 잎 1 g당 베르바스코사이드 36.5 mg, 이소베르바스코사이드 2.5 mg, 루테올린-7-O-이글루쿠로나이드 13.1 mg; 장 단계 소화 뒤 베르바스코사이드 28.9 mg[2]",
     "method": "HPLC-DAD(340 nm)",
     "conditions": {
         "instrument": "Chromaster(VWR-Hitachi), L7100 펌프 2대, L7200 자동주입기, L2450 DAD, EZ Chrom Elite 3.3.2",
         "column": "역상 Lichrospher C18 endcapped, 125 × 4 mm, 5 µm (Merck)",
         "mobile_phase": "A 1% 인산 수용액, B 아세토니트릴",
         "gradient": "0–5분 5% B; 5–30분 5–7% B; 30–45분 7–12% B; 45–50분 12–40% B (총 50분)",
         "flow": "1 mL/min",
         "temp": "실온",
         "detection": "DAD 340 nm(정량), 200–400 nm 스펙트럼으로 표준품과 대조",
         "injection": "20 µL",
         "sample_prep": "소화물·차를 4배 에탄올로 단백질 제거 후 원심분리, SpeedVac 농축, 물에 12.5 mg/mL로 재용해",
         "standard": "베르바스코사이드·이소베르바스코사이드·카페산(각 99.0%), 루테올린-7-O-이글루쿠로나이드(94.0%) (Extrasynthese)",
         "linearity": "카페산 3.12–125 µg/mL, L7DG 20–300 µg/mL, 베르바스코사이드 12.5–100 µg/mL, 이소베르바스코사이드 12.5–100 µg/mL (모두 R² = 0.999)",
         "lod": "", "loq": "", "recovery": ""},
     "rationale": "잎을 우린 물에서 가장 많은 페놀이 베르바스코사이드이고, 플라본 이글루쿠로나이드와 함께 차의 항산화·항당화 활성을 설명하므로 지표로 쓰임; 전문 확인, LOD·LOQ·회수율은 본문에 없음[2].",
     "source": [2], "url": "https://doi.org/10.3390/antiox15060717", "source_kind": "paper"},
    {"role": "literature", "compound": "Verbascoside", "compound_ko": "베르바스코사이드(이소베르바스코사이드는 베르바스코사이드 당량)",
     "part": "잎(이탈리아 파도바 식물원, 개화기 채취, 액체질소 동결 분쇄)",
     "content": "잎 메탄올 추출물 1 mg/mL 용액에서 베르바스코사이드 7.40 ± 0.84 µg/mL, 이소베르바스코사이드 4.72 ± 0.29 VE µg/mL[4]",
     "method": "RP-HPLC-DAD-ESI-MS(이온트랩, 음이온 모드)",
     "conditions": {
         "instrument": "Thermo Finnigan Surveyor Plus HPLC(PDA) – LCQ Advantage Max 이온트랩 질량분석기, ESI",
         "column": "Gemini C18, 150 × 2.0 mm, 5 µm (Phenomenex)",
         "mobile_phase": "A 0.1% 포름산 수용액, B 0.1% 포름산 아세토니트릴",
         "gradient": "0–3분 2% B; 3–5분 2–13%; 5–9분 13%; 9–12분 13–18%; 12–15분 18–30%; 15–25분 30–45%; 25–32분 45–60%; 32–37.5분 60–80%; 37.5–40분 80–98%; 40–45분 98–2%; 45–55분 2%",
         "flow": "0.3 mL/min",
         "temp": "",
         "detection": "ESI 음이온, 시스가스 20 AU, 보조가스 10 AU, 분무 전압 4 kV, 모세관 300 °C; 전주사 m/z 50–2000, 데이터 의존 MSn(정규화 충돌에너지 30%)",
         "injection": "20 µL",
         "sample_prep": "동결 분말을 LC-MS 등급 메탄올 1:10(w/v), 40 kHz 얼음 초음파 10분, 14,000×g 4 °C 10분 원심분리, 상등액 1 mL(생시료 100 mg 상당) SpeedVac 건조",
         "standard": "베르바스코사이드(Extrasynthese, ≥98%), 외부 표준법",
         "linearity": "0.5–10 µg/mL, R = 0.9986",
         "lod": "0.03 µg/mL",
         "loq": "0.1 µg/mL",
         "recovery": "93–108% (0.5·1·10 µg/mL), 일내·일간 RSD 0.4–8%"},
     "rationale": "베르바스코사이드와 그 이성질체가 이 종의 특징 성분으로 인정되어 ICH Q2(R2)에 따라 검증한 방법으로 정량함; 전문 확인[4].",
     "source": [4], "url": "https://doi.org/10.3390/nu18010115", "source_kind": "paper"},
    {"role": "literature", "compound": "Geranial", "compound_ko": "게라니알(네랄 등 정유 69성분 상대 조성)",
     "part": "말린 잎(포르투갈 업체 공급) 정유",
     "content": "게라니알 18.7–21.1%, 네랄 15.3–16.2%(TIC 피크 면적 상대 %); 정유 수율 클레벤저 1.05 ± 0.07%, 마이크로파 보조 1.29 ± 0.17%[3]",
     "method": "GC-MS(사중극자)",
     "conditions": {
         "instrument": "Shimadzu GC-2010 Plus, AOC-20i Plus 자동주입기, 사중극자 질량검출기",
         "column": "SH-Rxi-5ms, 30 m × 0.25 mm × 0.25 µm (Shimadzu)",
         "mobile_phase": "", "gradient": "", "flow": "", "temp": "",
         "detection": "EI-MS, NIST17 라이브러리와 n-알케인(C8–C40) 선형 머무름 지수로 동정",
         "injection": "",
         "sample_prep": "클레벤저: 시료 100 g + 증류수 2000 mL, 첫 방울 뒤 180분; 마이크로파 보조: 25 g + 250 mL, 600 W 15분; 무수 황산나트륨으로 탈수",
         "standard": "개별 표준품 정량 없음(상대 면적 %)",
         "linearity": "", "lod": "", "loq": "", "recovery": ""},
     "rationale": "시트랄 이성질체(게라니알·네랄)가 레몬 향을 내는 정유 주성분이라 정유 품질 지표로 쓰임; 전문 확인했으나 오븐 온도·주입량·분할비·MS 조건은 앞선 논문을 인용만 해 본문에 없음[3].",
     "source": [3], "url": "https://doi.org/10.3390/molecules28114528", "source_kind": "paper"},
]

d = {
    "slug": "aloysia-citrodora",
    "name_ko": "레몬버베나",
    "name_en": "Lemon verbena",
    "scientific_name": "Aloysia citrodora Paláu",
    "aliases": ["건조레몬버베나", "레몬버베나잎", "레몬버베나분말", "레몬버베나잎추출물", "Lemon verbena", "Lemon beebrush",
                "Aloysia triphylla", "Aloysia citriodora", "Lippia citriodora", "Lippia citrodora", "Verbena triphylla"],
    "sections": sections,
    "compounds": compounds,
    "markers": [],
    "nutrients": [],
    "assays": assays,
    "production": [],
    "world": [],
    "gi": [],
    "orgs": [],
    "sources": S,
}
# sources [12]-[15] referenced in clinical text below
d["sections"][5]["body"] += ""
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
print("ok", len(S))
