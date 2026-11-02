import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
PM = "PubMed (National Library of Medicine)"
A = "2026-11-02"
MF = "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020"
sources = [
 (1, "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 그린콩꼬투리·그린콩씨앗·그린콩퓌레(학명 Phaseolus radiatus L. var. aurea, 영명 Green bean, 이명 깍지콩), 사용가능부위: 씨앗, 꼬투리, 사용가능", MF, "식품의약품안전처", "2026-10-13"),
 (2, "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 녹두 행(학명 Vigna radiata (L.) R.Wilczek / Phaseolus radiatus L. / Azukia radiata Ohwi, 영명 Green gram, Mung bean, 이명 안두(安豆)·길두(吉豆)), 사용가능부위: 씨앗, 싹; 원료명 녹두·깐녹두·볶은녹두·녹두가루·녹두전분·녹두고물·녹두앙금·녹두페이스트·녹두액·녹두추출물·숙주나물·절임숙주나물·발아녹두 등", MF, "식품의약품안전처", "2026-10-13"),
 (3, "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 이름·학명이 비슷한 다른 원료 행: 팥·거피팥(Phaseolus angularis / Vigna angularis), 덩굴강낭콩(Phaseolus vulgaris L., 씨앗·꼬투리), 강낭콩(Phaseolus vulgaris var. humilis), 리마콩(Phaseolus lunatus), 흰강낭콩(Phaseolus multiflorus var. albus), 붉은강낭콩(Phaseolus multiflorus), Black gram씨앗(Phaseolus mungo)", MF, "식품의약품안전처", "2026-10-13"),
 (4, "통계청 「농작물생산조사(농작물생산통계)」 2023년판 — 녹두 재배면적·생산량(2019–2023, 시도별)", "https://kostat.go.kr", "통계청", "2026-10-13"),
 (5, "통계청 「농작물생산조사(농작물생산통계)」 2007년판(작물통계) — 녹두 재배면적·생산량(2003)", "https://kostat.go.kr", "통계청", "2026-10-13"),
 (6, "Genome sequence of mungbean and insights into evolution within Vigna species. Nat Commun 2014;5:5443 (PMID 25384727; PMC4241982 전문 확인)", "https://doi.org/10.1038/ncomms6443", PM, A),
 (7, "Mung Bean (Vigna radiata L.): Bioactive Polyphenols, Polysaccharides, Peptides, and Health Benefits. Nutrients 2019;11(6):1238 (PMID 31159173; PMC6627095 전문 확인)", "https://doi.org/10.3390/nu11061238", PM, A),
 (8, "Mung bean: technological and nutritional potential. Crit Rev Food Sci Nutr 2015 (PMID 24915360; 초록 확인)", "https://doi.org/10.1080/10408398.2012.671202", PM, A),
 (9, "A review on metabolites and pharmaceutical potential of food legume crop mung bean (Vigna radiata L. Wilczek). BioTechnologia 2021;102(4):425-435 (PMID 36605597; 초록 확인)", "https://doi.org/10.5114/bta.2021.111107", PM, A),
 (10, "Advancing crop improvement through GWAS and beyond in mung bean. Front Plant Sci 2024;15:1436532 (PMID 39744597; PMC11688477 전문 확인)", "https://doi.org/10.3389/fpls.2024.1436532", PM, A),
 (11, "Phytochemical distribution in hull and cotyledon of adzuki bean (Vigna angularis L.) and mung bean (Vigna radiate L.), and their contribution to antioxidant, anti-inflammatory and anti-diabetic activities. Food Chem 2016;201:350-360 (PMID 26868587; 초록 확인)", "https://doi.org/10.1016/j.foodchem.2016.01.101", PM, A),
 (12, "[Quality standard study on Vigna radiata]. Zhongguo Zhong Yao Za Zhi 2014;39(1):94-99 (PMID 24754176; 중국어 논문, 영문 초록 확인)", "https://pubmed.ncbi.nlm.nih.gov/24754176/", PM, A),
 (13, "Plasma Pharmacokinetics, Bioavailability, and Tissue Distribution of Four C-Glycosyl Flavones from Mung Bean (Vigna radiata L.) Seed Extracts in Rat by UHPLC-MS/MS. J Agric Food Chem 2017;65(27):5570-5580 (PMID 28627167; 초록 확인)", "https://doi.org/10.1021/acs.jafc.7b02053", PM, A),
 (14, "Antioxidant and Myocardial Preservation Activities of Natural Phytochemicals from Mung Bean (Vigna radiata L.) Seeds. J Agric Food Chem 2016;64(22):4648-4655 (PMID 27184346; 초록 확인)", "https://doi.org/10.1021/acs.jafc.6b01538", PM, A),
 (15, "In vitro and in vivo Inhibitory Activity of C-glycoside Flavonoid Extracts from Mung Bean Coat on Pancreatic Lipase and α-glucosidase. Plant Foods Hum Nutr 2023;78(2):439-444 (PMID 37351712; 초록 확인)", "https://doi.org/10.1007/s11130-023-01075-5", PM, A),
 (16, "Effect of optimized germination technology on polyphenol content and hypoglycemic activity of mung bean. Front Nutr 2023;10:1138739 (PMID 37077902; 초록 확인)", "https://doi.org/10.3389/fnut.2023.1138739", PM, A),
 (17, "Metabolomic analysis of the polyphenols in germinating mung beans (Vigna radiata) seeds and sprouts. J Sci Food Agric 2014;94(8):1639-1647 (PMID 24203396; 초록 확인)", "https://doi.org/10.1002/jsfa.6471", PM, A),
 (18, "Birch pollen-related food allergy to legumes: identification and characterization of the Bet v 1 homologue in mungbean (Vigna radiata), Vig r 1. Clin Exp Allergy 2005;35(8):1049-1055 (PMID 16120087; 초록 확인)", "https://doi.org/10.1111/j.1365-2222.2005.02309.x", PM, A),
 (19, "Vig r 6, the cytokinin-specific binding protein from mung bean (Vigna radiata) sprouts, cross-reacts with Bet v 1-related allergens and binds IgE from birch pollen allergic patients' sera. Mol Nutr Food Res 2014;58(3):625-634 (PMID 23996905; 초록 확인)", "https://doi.org/10.1002/mnfr.201300153", PM, A),
 (20, "[Two cases of allergy with mung bean sprouts]. Arerugi 2023;72(8):1046-1050 (PMID 37730348; 일본어 논문, 영문 초록 확인)", "https://doi.org/10.15036/arerugi.72.1046", PM, A),
 (21, "An outbreak of Salmonella Newport associated with mung bean sprouts in Germany and the Netherlands, October to November 2011. Euro Surveill 2014;19(1):20665 (PMID 24434173; 초록 확인)", "https://doi.org/10.2807/1560-7917.es2014.19.1.20665", PM, A),
 (22, "Salmonella infections associated with mung bean sprouts: epidemiological and environmental investigations. Epidemiol Infect 2009;137(3):357-366 (PMID 18294429; 초록 확인)", "https://doi.org/10.1017/S0950268808000411", PM, A),
 (23, "Level and fate of etoxazole in green bean (Phaseolus vulgaris). Bull Environ Contam Toxicol 2011;87(2):190-193 (PMID 21667235; 초록 확인 — 'green bean'을 강낭콩 꼬투리 이름으로 쓴 예)", "https://doi.org/10.1007/s00128-011-0336-6", PM, A),
 (24, "A comprehensive overview of three novel plant proteins approved by EFSA: alfalfa protein concentrate, rapeseed and mung bean protein isolates. Crit Rev Food Sci Nutr 2026;66(11):2215-2231 (PMID 41021395; 초록 확인)", "https://doi.org/10.1080/10408398.2025.2564898", PM, A),
 (25, "Vigna radiata (L.) R. Wilczek Extract Inhibits Influenza A Virus by Targeting Viral Attachment, Penetration, Assembly, and Release. Front Pharmacol 2020;11:584973 (PMID 33324216; PMC7725899 전문 확인; 업체 연구비 지원 연구)", "https://doi.org/10.3389/fphar.2020.584973", PM, A),
]
S = {}
S["overview"] = ("한눈에 보기",
"그린콩은 식약처 「식품원료 목록」에 원료명 '그린콩꼬투리·그린콩씨앗·그린콩퓌레', 학명 Phaseolus radiatus L. var. aurea, 영명 'Green bean', 이명 '깍지콩'으로 올라 있는 콩과 원료다[1]. 이 목록에서 그린콩은 사용가능 원료이고 사용 조건이 '사용가능부위 : 씨앗, 꼬투리'여서 씨앗과 꼬투리를 식품 원료로 쓸 수 있다[1]. 같은 목록의 녹두 행은 학명 Vigna radiata (L.) R.Wilczek에 Phaseolus radiatus L.과 Azukia radiata Ohwi를 이명으로 함께 적고 있어, 그린콩의 학명은 녹두(mung bean, green gram)의 옛 학명에 해당한다[1, 2]. 그러나 영명 'Green bean'과 이명 '깍지콩'은 문헌에서 강낭콩(Phaseolus vulgaris)의 꼬투리를 가리키는 이름으로도 쓰여서, 원자료 안에서 학명과 일반명이 서로 맞지 않는다[1, 23]. 이 문서는 원자료의 학명을 기준으로 녹두 자료를 정리했고 강낭콩·팥 자료는 섞지 않았다[2, 3].\n\n"
"녹두는 단백질(14.6–33.0 g/100 g)과 철(5.9–7.6 mg/100 g)이 많은 콩으로 아시아에서 널리 먹는다[8]. 주된 폴리페놀은 비텍신과 이소비텍신 같은 C-배당체 플라본이며 대부분 씨껍질에 들어 있다[7, 11]. 혈당·지질 개선 같은 작용은 주로 세포·동물 실험에서 보고되었고 사람 대상 임상시험은 아직 적다[7]. 이 종을 원재료로 하는 건강기능식품 고시형 원료는 확인하지 못함.")
S["history"] = ("역사와 이용",
"유전 다양성과 고고학 자료를 근거로 녹두는 인도에서 작물화되었다고 보며, 인도 북서부와 남부에서 4,000–6,000년 전에 재배가 시작되었다는 견해가 있다[6]. 작물화된 녹두는 인도에서 여러 경로로 동남아시아·동아시아로 퍼졌고, 실크로드를 거쳐 중국에 들어갔을 가능성도 제기되었다[6]. 녹두의 야생 조상은 인도의 히말라야 아래 지대와 동·서부 여러 곳에서 자란다[10]. 예전에는 상인과 이민자가 녹두 씨앗을 남아메리카·동아프리카·중동·오스트레일리아로 가져갔다[10].\n\n"
"중국 본초서 『본초강목』에는 녹두를 해독, 정신 회복, 더위 먹음 완화, 위장 장애 조절에 쓴다고 적혀 있다고 소개된다[7]. 인도·파키스탄에서는 녹두를 '달(dhal)'로 주식처럼 먹고, 파키스탄에서는 식사로 얻는 철의 약 25%를 콩류가 공급한다[7]. 국내 「식품원료 목록」에는 깐녹두, 녹두가루, 녹두전분, 녹두고물, 녹두앙금, 숙주나물, 발아녹두 같은 원료명이 따로 올라 있어 씨앗과 싹을 여러 형태로 먹는다는 것을 보여 준다[2]. 국내 이용의 역사를 다룬 공공 문헌 근거는 이번 조사에서 확인하지 못함.")
S["biology"] = ("식물학적 특징",
"녹두는 콩과(Fabaceae) 나비모양꽃아과(papilionoid)에 속하는 따뜻한 철 콩 작물로, 2배체이며 염색체 수는 2n = 2x = 22이다[6]. 생육 기간이 70일 안팎으로 짧고 가뭄에 비교적 강하며 투입이 적게 드는 작물이다[7]. 생육 적온은 28–30 °C이고 45 °C까지 견디며, 연 강수량 600–870 mm, pH 5–8의 물 빠짐이 좋은 양토·사양토에서 잘 자란다[10]. 침수에는 약하지만 약간 짠 토양은 견딘다[10]. 뿌리혹박테리아와 공생해 공기 중 질소를 고정하므로 토양 비옥도를 높인다[6].\n\n"
"녹두 씨앗의 페놀 성분은 떡잎보다 씨껍질에 몰려 있다[7]. 씨앗 색과 크기는 지역마다 달라 육종가가 선발 형질로 써 왔으며, 씨앗 색은 폴리페놀·카로티노이드 같은 성분과, 씨앗 굳기는 섬유 함량과 관련이 있다[8]. 안토시아닌은 검은 녹두에서만 검출되고 초록 녹두에서는 검출되지 않았다는 보고가 있다[7]. 그린콩 원료에서 허용된 '꼬투리'의 형태와 성분을 다룬 녹두 자료는 확인하지 못함.")
S["related_species"] = ("이름과 가까운 종",
"녹두가 속한 동부속(Vigna) 아속 Ceratotropis에는 흑녹두(black gram), 덩굴팥(rice bean), 모스빈(moth bean), 팥(adzuki bean) 같은 아시아의 주요 식용 콩이 함께 들어 있다[6]. 18종 22개 계통의 전사체로 만든 계통수는 이 아속의 종 분화를 보여 주었고, 사배체 근연종 하나는 최근의 이질배수화로 생긴 것으로 나타났다[6].\n\n"
"식약처 목록에는 학명에 'Phaseolus'를 쓰는 거피팥·팥(Phaseolus angularis, 이명 Vigna angularis), 덩굴강낭콩(Phaseolus vulgaris), 강낭콩(Phaseolus vulgaris var. humilis), 리마콩(Phaseolus lunatus), 흰강낭콩(Phaseolus multiflorus var. albus), 붉은강낭콩(Phaseolus multiflorus)이 각각 다른 원료로 올라 있다[3]. 'Black gram씨앗'(Phaseolus mungo)은 흑녹두로, 이름이 비슷하지만 녹두와 다른 종이다[3, 6]. 강낭콩의 어린 꼬투리를 'green bean'이라 부르는 문헌이 있으므로, 그린콩의 영명만 보고 강낭콩 꼬투리 자료를 녹두 자료로 옮기지 않도록 주의해야 한다[23]. 이 문서의 성분·안전성 자료는 모두 Vigna radiata(녹두) 연구에서 가져왔다[6, 7].")
S["cultivation"] = ("재배와 산지",
"녹두는 세계에서 600만 ha 넘게 재배되어 세계 콩류 재배면적의 약 8.5%를 차지하며, 중국·인도·방글라데시·파키스탄과 동남아시아, 남유럽 건조지, 캐나다·미국의 따뜻한 지역에서 재배된다[7]. 인도는 세계 연간 생산량(약 600만 t)의 50% 넘게 생산하는 최대 생산국이고 중국과 미얀마가 뒤를 잇는다[6]. 일부 나라의 수량은 0.5–1.5 t/ha로 아직 낮다[10]. 밀 수확 뒤 벼 심기 전의 빈 기간을 채우는 작물로 많이 쓰인다[10].\n\n"
"국내 녹두 재배면적은 2023년 1,680 ha, 생산량은 2,636 t이었고, 시도별로는 전남이 997 ha·1,819 t으로 가장 많았다[4]. 2022년에는 2,403 ha에서 4,750 t이 생산되어 2019–2023년 중 가장 많았다[4]. 2003년에는 1,557 ha에서 1,681 t이 생산되었다[5]. 세계채소센터(AVRDC)가 1982년에 개발한 순계는 한국에서 '선화녹두'라는 이름으로 널리 재배되었다[6]. 이 통계는 녹두 전체 값이며 '그린콩'만 따로 집계한 국내 통계는 확인하지 못함.")
S["processing"] = ("가공과 이용",
"국내 「식품원료 목록」에는 깐녹두, 볶은녹두, 녹두가루, 녹두전분, 녹두앙금, 녹두추출물, 숙주나물, 절임숙주나물, 발아녹두 등이 녹두 원료로 올라 있고, 그린콩은 꼬투리·씨앗·퓌레 세 가지 원료명으로만 올라 있다[1, 2]. 녹두 전분은 아밀로스가 약 32%로 높고, 녹두 전분 국수는 건강한 사람 18명에서 낮은 혈당·인슐린 반응을 보였다[7].\n\n"
"불림·발아·발효·껍질 벗기기·조리로 피트산 같은 항영양 성분을 줄일 수 있으며, 발아 뒤 피트산은 76% 줄고 아연·철의 생체이용률은 각각 3.0배, 2.4배 높아졌다[7]. 발아한 녹두에서는 비텍신·이소비텍신을 포함한 페놀산과 플라보노이드 총량이 날 씨앗보다 각각 최대 4.5배, 6.8배 높았다[7]. 발효 녹두의 γ-아미노뷰티르산(GABA)은 0.016 g/100 g에서 0.122 g/100 g으로 늘었다[7]. 최적 조건으로 3일 발아한 녹두의 폴리페놀 추출물 함량은 4.878 mg/g으로 발아 전의 3.07배였다[16]. 유럽식품안전청(EFSA)은 녹두 단백질 분리물을 신규식품으로 승인했다[24]. 국내 건강기능식품 생산실적에서 그린콩 원료 품목은 확인하지 못함.")
S["genetics"] = ("유전 정보",
"2014년 한국 연구진이 주도한 국제 공동연구가 재배 녹두의 초안 유전체를 발표했다[6]. 추정 유전체 크기는 579 Mb(1.2 pg/2C)이고, 조립된 스캐폴드 총길이 약 431 Mb는 k-mer로 추정한 크기 543 Mb의 80%에 해당한다[6]. 높은 신뢰도의 단백질 암호 유전자 22,427개가 예측되었고 그중 18,378개가 11개 유사염색체에 놓였다[6]. 반복 서열은 유전체의 약 50.1%이며 LTR/Gypsy가 25.2%, LTR/Copia가 11.3%를 차지했다[6]. 재배 녹두와 야생 녹두 사이에서 SNP 2,922,833개가 발견되었고, 두 계통의 분기는 약 100만 년 전으로 작물화보다 훨씬 앞선다[6].\n\n"
"녹두는 약 5,900만 년 전 나비모양꽃아과 공통의 전장유전체 중복 한 번만 겪은 것으로 나타났다[6]. 중앙 유전자은행에는 녹두 유전자원 약 14,187점이 있어 콩 다음으로 많다[10]. 전장유전체 연관분석(GWAS)으로 씨앗 색, 콩바구미 저항성, 조단백질, 개화일수, 철 함량 같은 형질과 관련된 유전자 좌위가 찾아지고 있다[10].")
S["safety"] = ("안전성",
"그린콩은 식약처 「식품원료 목록」에서 씨앗·꼬투리에 한해, 녹두는 씨앗·싹에 한해 사용가능한 원료다[1, 2]. 식약처 등 국내 공공기관의 그린콩·녹두 알레르기·잔류·독성 정보는 이번 조사에서 확인하지 못함. 녹두에는 피트산, 탄닌, 적혈구응집소, 트립신 저해제 같은 항영양 성분이 낮은 농도로 들어 있다[8, 9].\n\n"
"자작나무 꽃가루 알레르기가 있는 사람은 녹두나물을 먹고 알레르기 반응을 보일 수 있다[18]. 녹두나물 반응 환자 10명 중 80%의 혈청에서 Bet v 1과 닮은 단백질 Vig r 1(16.2 kDa)에 대한 IgE가 검출되었다[18]. 다른 Bet v 1 계열 단백질 Vig r 6에는 녹두나물 반응 환자 19명 중 63%가 IgE 결합을 보였다[19]. 일본에서는 녹두나물을 먹은 뒤 입술 부종 등이 나타난 사례 2건이 보고되었고, 두 환자 모두 자작나무·Bet v 1 특이 IgE 양성이었다[20].\n\n"
"날것이나 덜 익힌 녹두나물은 살모넬라 감염의 원인이 될 수 있다[21, 22]. 2011년 녹두나물과 관련된 살모넬라 뉴포트 집단감염으로 독일 106명, 네덜란드 20명이 보고되었다[21]. 2000–2002년 녹두나물 관련 살모넬라 집단감염을 조사한 연구는 재배자들이 씨앗을 권장 농도로 소독하지 않았다고 지적했다[22].")

compounds = [
 dict(name="Vitexin", name_ko="비텍신", class_="C-배당체 플라본", role="marker", part="씨앗(씨껍질)",
      content_text="씨껍질 37.43 mg/g(HPLC)[11]; 씨앗 25개 시료 1.076–2.062 mg/g(HPLC)[12]; 씨앗 전체 비텍신의 95.6%가 씨껍질에 있음[7]",
      activity_ko="녹두의 2대 플라보노이드; 세포·동물 실험에서 혈당 조절·지방 축적 억제·멜라닌 생성 억제가 보고됨[7]", source=[7, 11, 12]),
 dict(name="Isovitexin", name_ko="이소비텍신", class_="C-배당체 플라본", role="marker", part="씨앗(씨껍질)",
      content_text="씨껍질 47.18 mg/g(HPLC)[11]; 씨앗 25개 시료 1.127–2.303 mg/g(HPLC)[12]; 씨껍질 추출물 29.0%(비텍신 35.8%)[15]",
      activity_ko="씨껍질 추출물이 췌장 리파아제(IC50 0.147 mg/mL)·α-글루코시다아제(IC50 0.226 mg/mL)를 억제, 쥐에서 식후 혈당 개선[15]", source=[7, 11, 12, 15]),
 dict(name="Isovitexin 6''-O-glucoside", name_ko="이소비텍신-6″-O-α-L-글루코사이드", class_="C-배당체 플라본", role="bioactive", part="씨앗",
      content_text="함량 확인하지 못함; 녹두 씨앗에서 새로 분리·구조 확인된 성분[14]",
      activity_ko="쥐 경구 투여 시 생체이용률 1.37%(비텍신 5.82%, 이소비텍신 5.53%)[7, 13]", source=[7, 13, 14]),
 dict(name="Rutin", name_ko="루틴", class_="플라보놀 배당체", role="bioactive", part="싹(녹두나물)",
      content_text="발아 녹두나물의 화학 표지 8종 플라보노이드 중 하나(HPLC-DAD 정량, 수치는 초록에 없어 확인하지 못함)[17]",
      activity_ko="발아 녹두 정제 폴리페놀에서도 동정됨[16]", source=[16, 17]),
 dict(name="gamma-Aminobutyric acid", name_ko="γ-아미노뷰티르산(GABA)", class_="비단백질 아미노산", role="bioactive", part="씨앗",
      content_text="날 녹두 0.016 g/100 g → 발효 녹두 0.122 g/100 g(7.6배)[7]", activity_ko="발효·발아로 늘어나는 성분[7]", source=[7]),
 dict(name="Ferulic acid", name_ko="페룰산", class_="하이드록시신남산", role="bioactive", part="씨앗",
      content_text="녹두 페놀산 총량 1.81–5.97 mg 루틴당량/g 가운데 주요 하이드록시신남산(개별 함량 확인하지 못함)[7]",
      activity_ko="주로 결합형으로 존재[7]", source=[7]),
 dict(name="Caffeic acid", name_ko="카페산", class_="하이드록시신남산", role="bioactive", part="씨앗",
      content_text="가장 흔한 하이드록시신남산의 하나(개별 함량 확인하지 못함)[7]", activity_ko="결합형으로도 존재[7]", source=[7]),
 dict(name="Gallic acid", name_ko="갈산", class_="하이드록시벤조산", role="bioactive", part="씨앗",
      content_text="녹두에서 가장 자주 검출되는 하이드록시벤조산(개별 함량 확인하지 못함)[7]", activity_ko="항산화 페놀산[7]", source=[7]),
 dict(name="Condensed tannins", name_ko="축합형 탄닌", class_="프로안토시아니딘", role="nutrient", part="씨앗",
      content_text="탄닌 1.00–5.75 mg/g[7]; 녹두는 씨껍질보다 떡잎에 더 많음[11]",
      activity_ko="항영양 성분으로 분류[8]; 씨껍질 프로안토시아니딘은 세포 실험에서 티로시나아제·멜라닌 생성 억제[7]", source=[7, 8, 11]),
 dict(name="Phytic acid", name_ko="피트산", class_="이노시톨 인산(항영양 성분)", role="nutrient", part="씨앗",
      content_text="발아 뒤 76% 감소(아연·철 생체이용률 3.0배·2.4배 증가)[7]",
      activity_ko="철·아연·칼슘·마그네슘과 결합해 흡수를 떨어뜨림[7, 8]", source=[7, 8]),
 dict(name="Verbascose", name_ko="베르바스코스", class_="라피노스계 올리고당", role="bioactive", part="씨앗",
      content_text="함량 확인하지 못함[7]",
      activity_ko="대식세포 실험(200 μg/mL)과 면역억제 생쥐(90 mg/kg, 8일)에서 면역 지표 증가[7]", source=[7]),
 dict(name="Amylose", name_ko="아밀로스", class_="전분 다당류", role="nutrient", part="씨앗(전분)",
      content_text="녹두 전분의 약 32%[7]",
      activity_ko="건강한 남성 8명에서 녹두 전분 혈당지수 51 ± 13(옥수수 전분 95 ± 18)[7]", source=[7]),
 dict(name="Protein", name_ko="단백질(8S 글로불린 위주)", class_="저장 단백질", role="nutrient", part="씨앗",
      content_text="14.6–33.0 g/100 g[8]; 20–32%[9]; 건물 기준 24–28%[10]",
      activity_ko="녹두 단백질 분리물 3.0 g/일 8주 섭취(44명) 시 인슐린·HOMA-IR 감소, 공복혈당 변화는 유의하지 않음(종설 인용)[7]", source=[7, 8, 9, 10]),
 dict(name="Iron", name_ko="철", class_="무기질", role="nutrient", part="씨앗",
      content_text="5.9–7.6 mg/100 g[8]", activity_ko="다른 콩류보다 엽산·철이 많다고 소개됨[6]", source=[6, 8]),
]
for c in compounds:
    c["class"] = c.pop("class_")
assays = [
 dict(role="literature", compound="Vitexin; Isovitexin", compound_ko="비텍신·이소비텍신", part="씨앗(중국 시판 녹두 25개 배치)",
      content="비텍신 1.076–2.062 mg/g, 이소비텍신 1.127–2.303 mg/g[12]", method="HPLC-UV",
      conditions={"instrument": "", "column": "Prevail C18, 4.6 mm × 250 mm, 5 μm", "mobile_phase": "아세토니트릴 : 물 = 23 : 77", "gradient": "등용매(초록 기준)", "flow": "1.0 mL/min", "temp": "30 °C", "detection": "337 nm", "injection": "", "sample_prep": "", "standard": "비텍신·이소비텍신 표준품", "linearity": "비텍신 6.12–98 mg/L(Y = 46.213X − 7.100, r = 1.000), 이소비텍신 6.85–109.6 mg/L(Y = 54.515X + 6.829, r = 1.000)", "lod": "", "loq": "", "recovery": "비텍신 98.2%(RSD 1.9%), 이소비텍신 97.2%(RSD 0.79%)"},
      rationale="녹두의 품질 기준을 세운 연구에서 TLC 확인과 HPLC 정량의 기준 성분으로 비텍신·이소비텍신을 썼다[12]. 두 성분은 녹두 씨앗의 2대 플라보노이드다[7]. 조건은 영문 초록에서 옮겼고 중국어 전문은 확인 못함(기기·시료 전처리·검출한계·정량한계 확인하지 못함).",
      source=[7, 12], url="https://pubmed.ncbi.nlm.nih.gov/24754176/", source_kind="paper"),
 dict(role="literature", compound="Vitexin; Isovitexin", compound_ko="비텍신·이소비텍신", part="씨껍질 가공 추출물(95% 에탄올 추출)",
      content="추출물 비텍신 22.153 mg/g, 이소비텍신 24.171 mg/g[25]", method="HPLC-DAD",
      conditions={"instrument": "Hitachi D2000(L-2130 펌프, L-2200 자동주입기, L-2455 DAD)", "column": "Inertsil ODS-2 C18, 250 mm × 4.6 mm, 5 μm", "mobile_phase": "A: 0.3% 인산 수용액, B: 아세토니트릴", "gradient": "기울기 용리(구간별 비율은 원문에 없음)", "flow": "0.8 mL/min", "temp": "30 °C", "detection": "220 nm", "injection": "", "sample_prep": "씨껍질 분말을 95% 에탄올(1:10 w/v)로 1시간 초음파 추출, 농축 후 메탄올에 희석", "standard": "머무름 시간으로 피크 동정", "linearity": "", "lod": "", "loq": "", "recovery": ""},
      rationale="씨껍질 추출물의 주성분이 비텍신·이소비텍신이어서 추출물 품질 지표로 쓰였다[25]. 전문(Methods)에서 조건을 옮겼으며 검량선·검출한계·회수율은 원문에 없어 확인하지 못함; 업체 연구비 지원 연구다.",
      source=[25], url="https://doi.org/10.3389/fphar.2020.584973", source_kind="paper"),
 dict(role="literature", compound="Vitexin; Isovitexin", compound_ko="비텍신·이소비텍신", part="씨껍질(hull)",
      content="씨껍질 비텍신 37.43 mg/g, 이소비텍신 47.18 mg/g[11]", method="HPLC",
      conditions={},
      rationale="씨껍질·떡잎·통알 비교에서 씨껍질이 피토케미컬과 항산화 활성의 대부분을 차지해, 부위별 품질 비교 지표로 쓸 수 있다[11]. 초록만 확인했고 전문 확인 못함.",
      source=[11], url="https://doi.org/10.1016/j.foodchem.2016.01.101", source_kind="paper"),
]
prod = []
nat = {2003: (1557, 1681, 5), 2019: (1541, 2035, 4), 2020: (1157, 1598, 4), 2021: (1229, 2004, 4), 2022: (2403, 4750, 4), 2023: (1680, 2636, 4)}
for y, (a, p, s) in nat.items():
    note = "녹두 전체 값(그린콩만 따로 집계한 값 아님)"
    prod.append(dict(metric="area_ha", region="대한민국", year=y, value=a, unit="ha", note=note, source=[s]))
    prod.append(dict(metric="production_t", region="대한민국", year=y, value=p, unit="t", note=note, source=[s]))
keys = ["overview", "history", "biology", "related_species", "cultivation", "processing", "genetics", "safety"]
d = dict(slug="phaseolus-radiatus", name_ko="그린콩", name_en="Green bean",
         scientific_name="Phaseolus radiatus L. var. aurea (= Vigna radiata (L.) R.Wilczek, 녹두)",
         aliases=["그린콩꼬투리", "그린콩씨앗", "그린콩퓌레", "깍지콩", "Green bean", "녹두", "Mung bean", "Green gram", "Vigna radiata", "Phaseolus radiatus L."],
         sections=[dict(key=k, title=S[k][0], body=S[k][1]) for k in keys],
         compounds=compounds, markers=[], nutrients=[], production=prod, world=[], assays=assays, gi=[], orgs=[],
         sources=[dict(n=n, title=t, url=u, publisher=p, accessed=a) for n, t, u, p, a in sources])
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for k in keys: print(k, len(S[k][1]))
