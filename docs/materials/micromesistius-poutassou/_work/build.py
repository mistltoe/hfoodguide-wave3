import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
A = "2026-11-02"
PMC = "https://pmc.ncbi.nlm.nih.gov/articles/{}/"
DOI = "https://doi.org/{}"
S = [
 ("식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — Micromesistius poutassou 행(청대구, Blue whiting, 수산물, 부위 '-', 사용가능, 고시형 원료 원재료 목록 없음; docs/materials/micromesistius-poutassou/card.json)", "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "식품의약품안전처", "2026-10-13"),
 ("FishBase — Micromesistius poutassou (Risso, 1827), Blue whiting: species summary (SpecCode 31; 검색 결과 요약으로 확인, 본문 페이지는 이 환경에서 열지 못함)", "https://www.fishbase.se/summary/Micromesistius-poutassou.html", "FishBase", A),
 ("FAO ARTFIMED 종 설명 — Micromesistius poutassou Risso, 1826 (GADMIPOU; 검색 결과 요약으로 확인)", "https://www.fao.org/fishery/docs/CDrom/ARTFIMED/ArtFiWeb/descript/Species/GADMIPOU.HTML", "FAO", A),
 ("MarLIN — Blue whiting (Micromesistius poutassou) 종 정보 (검색 결과 요약으로 확인)", "https://www.marlin.ac.uk/species/detail/56", "Marine Biological Association of the UK (MarLIN)", A),
 ("ICES Advice 2025 — Blue whiting (Micromesistius poutassou) in subareas 1–9, 12 and 14 (whb.27.1-91214), 2025-09-30 발표 (페로제도 해양연구소 게시본; 검색 결과 요약으로 확인)", "https://www.hav.fo/wp-content/uploads/2025/09/ICES_svartkjaftur_whb.27.1-91214_2025.pdf", "International Council for the Exploration of the Sea (ICES)", A),
 ("Management of shared fish stocks: agreed records 2022 — Blue whiting (연안국 협의 기록; 검색 결과 요약으로 확인)", "https://gov.scot/publications/management-of-shared-fish-stocks-agreed-records-2022/pages/blue-whiting", "Scottish Government", A),
 ("Feeding Ecology of Northeast Atlantic Mackerel, Norwegian Spring-Spawning Herring and Blue Whiting in the Norwegian Sea. PLoS One 2016;11(2):e0149238", PMC.format("PMC4764516"), "PLoS One (PubMed)", A),
 ("Effects of density dependence, zooplankton and temperature on blue whiting Micromesistius poutassou growth. J Fish Biol 2015;87(4):1019-30", DOI.format("10.1111/jfb.12775"), "Journal of Fish Biology (PubMed)", A),
 ("A resolution to the blue whiting (Micromesistius poutassou) population paradox? PLoS One 2014;9(9):e106237", PMC.format("PMC4153562"), "PLoS One (PubMed)", A),
 ("Trade-offs between life-history traits in a coldwater fish in the Mediterranean Sea: the case of blue whiting Micromesistius poutassou. J Fish Biol 2019;95(2):428-443", DOI.format("10.1111/jfb.13993"), "Journal of Fish Biology (PubMed)", A),
 ("Integrating biochemical and physiological indicators to assess the condition of blue whiting, Micromesistius poutassou, in the context of mediterranean sea warming. Mar Environ Res 2026;221:108232", DOI.format("10.1016/j.marenvres.2026.108232"), "Marine Environmental Research (PubMed)", A),
 ("Mitochondrial DNA differentiation between the antitropical blue whiting species Micromesistius poutassou and Micromesistius australis. J Fish Biol 2012;81(1):253-69", DOI.format("10.1111/j.1095-8649.2012.03334.x"), "Journal of Fish Biology (PubMed)", A),
 ("A Multiplex PCR Assay Combined with Capillary Electrophoresis for the Simultaneous Identification of Atlantic Cod, Pacific Cod, Blue Whiting, Haddock, and Alaska Pollock. Foods 2021;10(11):2631", PMC.format("PMC8618353"), "Foods (MDPI, PubMed)", A),
 ("Liver transcriptome resources of four commercially exploited teleost species. Sci Data 2020;7(1):214", PMC.format("PMC7340784"), "Scientific Data (PubMed)", A),
 ("Supplementation with a fish protein hydrolysate (Micromesistius poutassou): effects on body weight, body composition, and CCK/GLP-1 secretion. Food Nutr Res 2016;60:29857", PMC.format("PMC4734037"), "Food & Nutrition Research (PubMed)", A),
 ("Postexercise Dietary Leucine Retention for Whole-Body Anabolism Is Greater With Whey Protein Isolate and Fish-Derived Protein Hydrolysate Than Nonessential Amino Acids in Trained Young Men. Int J Sport Nutr Exerc Metab 2024;35(1):24-33", DOI.format("10.1123/ijsnem.2024-0157"), "Int J Sport Nutr Exerc Metab (PubMed)", A),
 ("Physicochemical, Nutritional and In Vitro Antidiabetic Characterisation of Blue Whiting (Micromesistius poutassou) Protein Hydrolysates. Mar Drugs 2021;19(7):383", PMC.format("PMC8304566"), "Marine Drugs (MDPI, PubMed)", A),
 ("Blue Whiting (Micromesistius poutassou) Protein Hydrolysates Increase GLP-1 Secretion and Proglucagon Production in STC-1 Cells Whilst Maintaining Caco-2/HT29-MTX Co-Culture Integrity. Mar Drugs 2022;20(2):112", PMC.format("PMC8877066"), "Marine Drugs (MDPI, PubMed)", A),
 ("A Cell-Based Assessment of the Muscle Anabolic Potential of Blue Whiting (Micromesistius poutassou) Protein Hydrolysates. Int J Mol Sci 2023;24(3):2001", PMC.format("PMC9916327"), "Int J Mol Sci (MDPI, PubMed)", A),
 ("Effects of intact and hydrolysed blue whiting proteins on blood pressure and markers of kidney function in obese Zucker fa/fa rats. Eur J Nutr 2021;60(1):529-544", PMC.format("PMC7867508"), "European Journal of Nutrition (PubMed)", A),
 ("Water-Soluble Fish Protein Intake Led to Lower Serum and Liver Cholesterol Concentrations in Obese Zucker fa/fa Rats. Mar Drugs 2018;16(5):149", PMC.format("PMC5983280"), "Marine Drugs (MDPI, PubMed)", A),
 ("Characterization of protein hydrolysates from blue whiting (Micromesistius poutassou) and their application in beverage fortification. Food Chem 2018;245:698-706", DOI.format("10.1016/j.foodchem.2017.10.107"), "Food Chemistry (PubMed)", A),
 ("Functional, bioactive and antigenicity properties of blue whiting protein hydrolysates: effect of enzymatic treatment and degree of hydrolysis. J Sci Food Agric 2017;97(1):299-308", DOI.format("10.1002/jsfa.7731"), "J Sci Food Agric (PubMed)", A),
 ("Characterization of Protein Hydrolysates from Fish Discards and By-Products from the North-West Spain Fishing Fleet as Potential Sources of Bioactive Peptides. Mar Drugs 2021;19(6):338", PMC.format("PMC8231949"), "Marine Drugs (MDPI, PubMed)", A),
 ("Arsenolipids in oil from blue whiting Micromesistius poutassou — evidence for arsenic-containing esters. Sci Rep 2014;4:7492", PMC.format("PMC4265782"), "Scientific Reports (PubMed)", A),
 ("Seasonal variation in the biochemical composition of fish discards and its impact on the production of mince, protein hydrolysates, and oil. Food Chem 2026;521:149938", DOI.format("10.1016/j.foodchem.2026.149938"), "Food Chemistry (PubMed)", A),
 ("Low detection efficiency of candling as a commonly recommended inspection method for nematode larvae in the flesh of pelagic fish. J Food Prot 2005;68(4):828-32", DOI.format("10.4315/0362-028x-68.4.828"), "Journal of Food Protection (PubMed)", A),
 ("Risk analysis of human anisakidosis through the consumption of the blue whiting, Micromesistius poutassou, sold at Spanish supermarkets. Foodborne Pathog Dis 2012;9(10):934-8", DOI.format("10.1089/fpd.2012.1196"), "Foodborne Pathogens and Disease (PubMed)", A),
 ("Detection and Characterization of Visceral Anisakid Nematodes in Blue Whiting from Portuguese Waters. Foods 2024;13(23):3802", PMC.format("PMC11640072"), "Foods (MDPI, PubMed)", A),
 ("Effectiveness of Gutting Blue Whiting (Micromesistius poutassou, Risso, 1827), in Spanish Supermarkets as an Anisakidosis Safety Measure. Foods 2021;10(4):862", PMC.format("PMC8071357"), "Foods (MDPI, PubMed)", A),
 ("Molecular epidemiology and risk factors for Anisakis simplex s.l. infection in blue whiting (Micromesistius poutassou) in a confluence zone of the Atlantic and Mediterranean. Int J Food Microbiol 2016;232:111-6", DOI.format("10.1016/j.ijfoodmicro.2016.05.026"), "Int J Food Microbiol (PubMed)", A),
 ("Total mercury and methylmercury content in edible fish from the Mediterranean Sea. J Food Prot 2003;66(2):300-3", DOI.format("10.4315/0362-028x-66.2.300"), "Journal of Food Protection (PubMed)", A),
 ("Effects of geography and species variation on selenium and mercury molar ratios in Northeast Atlantic marine fish communities. Sci Total Environ 2019;652:1482-1496", DOI.format("10.1016/j.scitotenv.2018.10.405"), "Science of the Total Environment (PubMed)", A),
 ("Organic and inorganic arsenic and lead in fish from the South Adriatic Sea, Italy. Food Addit Contam 2000;17(9):763-8", DOI.format("10.1080/026520300415309"), "Food Additives and Contaminants (PubMed)", A),
 ("Wild fish and seafood species in the western Mediterranean Sea with low safe mercury concentrations. Environ Pollut 2022;314:120274", DOI.format("10.1016/j.envpol.2022.120274"), "Environmental Pollution (PubMed)", A),
]
sources = [{"n": i + 1, "title": t, "url": u, "publisher": p, "accessed": a} for i, (t, u, p, a) in enumerate(S)]

sections = [
 ("overview", "한눈에 보기",
  "청대구(Micromesistius poutassou)는 대구목 대구과(Gadidae)에 속하는 바닷물고기로, 영어로는 blue whiting이라 부르고 FAO 3문자 코드는 WHB이다[1, 3]. 북동대서양과 지중해의 대륙붕·대륙사면 깊은 물에 살며, 밤에는 수면 쪽으로 올라오는 수직 이동을 한다[2, 4].\n\n"
  "식약처 「식품원료 목록」에는 원료명 '청대구'(영문 Blue whiting)가 수산물로 올라 있고 상태는 '사용가능'이다[1]. 부위 칸은 '-'이고 따로 정한 사용 조건은 없으며, 건강기능식품 고시형 원료의 원재료 목록에도 없어 고시 지표성분이나 1일 섭취량 기준은 없다[1].\n\n"
  "북동대서양 자원의 2025년 어획량이 약 175만 톤으로 추정될 만큼 큰 어업 자원이지만, 대부분 어분·어유 원료로 쓰이고 사람이 직접 먹는 양은 적다[5, 17]. 스페인에서는 소비되는 흰살생선의 약 25%를 차지할 만큼 식용으로도 흔하다[30]. 최근에는 단백질 가수분해물을 식품 소재로 쓰려는 연구와 사람 대상 시험이 이어지고 있다[15, 16, 17]."),
 ("history", "이름과 이용의 역사",
  "학명의 명명자 표기는 자료에 따라 'Risso, 1826' 또는 'Risso, 1827'로 다르게 적힌다[2, 3]. 북대서양 자원은 오래전부터 어분·어유 산업의 원료였고, 어분을 만드는 과정에서 물에 녹는 단백질 분획이 따로 얻어진다[21].\n\n"
  "1948–2005년 연속플랑크톤기록기(CPR) 자료 1,100건을 분석한 연구는 이 종의 자원 구조 논쟁을 정리하며 북대서양에 두 개의 독립 집단이 있다고 결론지었다[9]. 북동대서양 연안국들은 ICES 권고를 바탕으로 해마다 총어획량을 협의하는데, 2022년에는 752,736톤 이하로 합의했다[6].\n\n"
  "유럽연합이 2019년부터 잡은 어획물을 모두 양륙하게 하는 양륙 의무를 전면 시행하면서, 값이 낮은 청대구를 식품 단백질로 쓰려는 연구가 늘었다[17, 24]. 스페인 북서부 트롤 어선에서 자주 버려지는 어종의 하나로 꼽혀 가수분해물 원료로 연구되었다[24]. 지중해에서는 최소 양륙 크기가 성숙 크기보다 작아 자원 관리에 영향을 줄 수 있다는 지적이 있다[10]. 국내 도입·이용의 역사 기록은 이번 조사에서 확인하지 못함."),
 ("biology", "어종과 생태",
  "FishBase는 서식 수심을 150–3,000 m(보통 300–400 m)로 적고, 최대 전장 55.5 cm, 흔한 크기 22.0 cm, 최대 체중 830 g, 최대 연령 20년으로 정리한다[2]. FAO 종 설명은 최대 50 cm, 흔한 성어 15–30 cm로 적어 출처마다 값이 조금 다르다[3]. 산란은 2월부터 대륙사면 가장자리 위, 바닥에서 10–30 m 떨어진 곳에서 이루어진다[3].\n\n"
  "노르웨이해에서 봄·여름에 먹이를 먹는 청대구는 크릴(난바다곤쟁이류)과 단각류처럼 큰 먹이를 주로 먹어, 같은 해역의 고등어·청어와 먹이 겹침이 적었다[7]. 2004–2011년 나이별 평균 길이는 약 ±6%, 1981–2013년 나이별 평균 무게는 약 ±22% 변했으며, 이는 주로 밀도 의존성과 먹이 조건으로 설명되었다[8].\n\n"
  "북대서양에는 로콜 해곡(북부)과 포큐파인 해역(남부)에 산란장이 나뉘고 산란 시기도 한 달 이상 차이가 난다[9]. 지중해 북서부에서는 2000년대 초에 비해 2017–2022년 어린 개체의 간중량지수가 58% 줄어 수온 상승의 영향이 제기되었다[11]."),
 ("related_species", "가까운 종",
  "같은 속의 남방청대구(Micromesistius australis)는 남반구에 살고, 청대구는 북반구에 살아 적도를 사이에 두고 떨어진 분포를 보인다[12]. 미토콘드리아 coI 유전자 579 bp를 청대구 279개체와 남방청대구 163개체에서 비교한 결과 두 종은 약 200만 년 전에 갈라진 것으로 추정되었다[12]. 같은 연구에서 지중해 청대구는 유전적으로 고립된 집단으로 나타났다[12].\n\n"
  "청대구는 대서양대구·태평양대구·해덕·명태와 같은 대구과 어류로, 가공 뒤에는 겉모습으로 구별하기 어려워 바꿔치기와 잘못된 표시가 문제가 된다[13]. 이 다섯 종을 한 번에 가리는 다중 PCR에서 청대구는 164 bp 산물로 구별되었고, 검출한계는 1 pg이며 시판 제품 40개에 적용되었다[13]. 국내 시장에서 유사 어종과 섞여 유통되는 실태는 이번 조사에서 확인하지 못함."),
 ("cultivation", "어획과 자원 관리",
  "청대구는 양식하지 않고 자연산을 잡는 어종이며, 북동대서양 자원(ICES 해역 1–9, 12, 14)은 ICES가 해마다 자원을 평가한다[5]. 2025년 평가에서 어획 압력은 FMSY와 FPA보다 높았지만 산란친어량은 MSY Btrigger·BPA·Blim보다 위에 있었다[5].\n\n"
  "ICES는 2025년 총어획량을 1,751,013톤으로 추정했고, 2026년 어획량 권고치는 관리 전략에 따라 851,344톤으로 전년 권고보다 41% 낮췄다[5]. 낮춘 이유는 자원량 감소와 최근 몇 년의 자원량 추정치 하향 조정이며, 2026년 산란친어량은 약 365만 톤으로 예측되었다[5]. 평가에는 2004–2025년 국제 청대구 산란자원 조사(1–8세, 2010·2020년 제외) 지수 하나가 쓰였다[5]. 2022년 연안국 협의 총어획량은 752,736톤이었다[6].\n\n"
  "지중해에서는 냉수성 어종인 청대구의 성장·번식이 수온 상승과 기생충 감염에 영향을 받는다고 보고되었다[10, 11]. 한국 연근해 어획·수입량 공식 통계는 이번 조사에서 확인하지 못함."),
 ("processing", "가공과 이용",
  "어획량 대부분은 어분·어유가 되며, 다진 살(민스)은 단백질이 많고 지방이 적어 식용에 알맞고 회수한 기름에는 오메가-3 지방산이 많다고 보고되었다[17, 26]. 산업 규모로 만든 수용성 단백질 가수분해물 6종은 단백질 70.37–73.60%를 담고 DPP-IV 저해(IC50 2.12–2.90 mg 단백질/mL)와 인슐린 분비 촉진(4.7–6.4배)을 보였다[17]. 가수분해물은 세포에서 GLP-1 분비와 근육 단백질 합성을 높였고, 비만 쥐에서는 혈압 상승과 콜레스테롤을 낮췄다[18–21].\n\n"
  "과체중 성인 120명 무작위 시험에서 가수분해물 1.4 g 또는 2.8 g을 90일 먹은 군은 체성분이 개선되고 혈중 CCK·GLP-1이 올랐으며 두 용량의 차이는 없었다[15]. 운동한 남성 10명 교차 시험에서는 류신 보유량이 유청단백질보다 낮았지만 비필수아미노산 대조보다 높았다[16]. 효소 처리 가루는 pH 전반에서 용해도가 80% 넘어 음료 강화에 쓸 수 있었다[22]. 국내 제품 생산실적은 확인하지 못함."),
 ("genetics", "유전체와 유전 다양성",
  "미토콘드리아 coI 유전자 분석은 청대구와 남방청대구가 약 200만 년 전에 갈라졌고 남반구로 적어도 두 번 건너갔을 가능성을 제시했다[12]. 같은 분석에서 하플로타입 빈도와 FST 값은 지중해 청대구가 대서양 집단과 유전적으로 떨어져 있음을 보였다[12]. 유충 분포와 산란 시기 분석은 북대서양에 북부·남부 두 집단이 있다는 가설을 뒷받침했다[9].\n\n"
  "2020년 청대구 간 조직의 전사체(RNA-seq) 자료가 처음 공개되었으며, 종마다 고품질 조립본 16개를 만들었고 시료당 8,020만–8,840만 쌍의 리드를 얻었다[14]. 네 어종 조립본의 N50은 2,543–3,700 bp, 조기어류 BUSCO 완전도는 81.8–86.5%였다[14]. 종 판별에는 미토콘드리아 유전자를 표적으로 한 종 특이 프라이머가 쓰인다[13]. 염색체 수준의 전장 유전체 조립 보고는 이번 조사에서 확인하지 못함."),
 ("safety", "안전성과 주의",
  "고시형 원료가 아니어서 식약처가 따로 정한 섭취 주의사항은 없다[1]. 청대구에는 고래회충(Anisakis) 유충이 흔해, 북동대서양 개체 필레의 89–100%에서 유충이 나왔고 빛 비춤 검사로는 필레 속 유충의 7–10%만 찾았다[27]. 스페인 슈퍼마켓 284마리의 감염률은 55.6%였고, 날로 먹거나 덜 익혀 먹을 때는 −20 °C에서 24시간 이상 냉동이 권고되었다[28]. 포르투갈 50마리는 모두 감염되었고, 매장에서 내장을 뺀 생선에서도 25%에서 유충이 나와 내장 제거만으로는 충분하지 않았다[29, 30]. 대서양·지중해 합류 해역 조사에서는 고래회충 감염률이 82%였다[31].\n\n"
  "지중해산 근육의 총수은은 0.11–1.92 mg/kg(평균 0.70)로 63.6%가 EU 기준 0.5 mg/kg을 넘었다[32]. 반면 북동대서양 개체 평균은 0.04 mg/kg으로 낮았고, 서지중해 시장 조사에서도 모든 개체가 0.5 μg/g 이하였다[33, 35]. 비소는 8.5–21.5 mg/kg이었으나 대부분 유기 형태였고 무기비소는 0.47–3.5%였다[34]. 내장은 중금속 기준을 넘는 경우가 많았다[26]. 국내 공공기관의 청대구 알레르기 정보는 확인하지 못함."),
]
for k, t, b in sections:
    print(k, len(b))

compounds = [
 dict(name="Blue whiting protein hydrolysate", name_ko="청대구 단백질 가수분해물", class_="단백질·펩타이드 혼합물", role="marker", part="살(다진 살)·통째",
      content_text="단백질 당량 70.37–73.60%(w/w), 지방 ≤0.5%[17]; 사람 시험 1일 1.4 g·2.8 g[15]",
      activity_ko="DPP-IV 저해·인슐린 분비 촉진(시험관)[17], 세포 GLP-1 분비 증가[18], 과체중 성인 체성분 개선·CCK/GLP-1 증가[15]", source=[15, 17, 18]),
 dict(name="Glutamic acid", name_ko="글루탐산(Glx)", class_="아미노산", role="nutrient", part="살 가수분해물",
      content_text="Glx 12.00–12.90 g/100 g[17]; 여러 어종 가수분해물 12–15%[24]",
      activity_ko="가수분해물에서 가장 많은 아미노산[17, 24]", source=[17, 24]),
 dict(name="Aspartic acid", name_ko="아스파르트산(Asx)", class_="아미노산", role="nutrient", part="살 가수분해물",
      content_text="Asx 8.10–8.56 g/100 g[17]; 여러 어종 가수분해물 8–10%[24]",
      activity_ko="두 번째로 많은 아미노산; 금속 킬레이트 활성과 관련 추정[24]", source=[17, 24]),
 dict(name="Tryptophan", name_ko="트립토판", class_="필수아미노산", role="nutrient", part="살 가수분해물",
      content_text="0.45–0.59 g/100 g; 아미노산가 0.94–1.27(성인 기준)[17]",
      activity_ko="모든 가수분해물의 제1 제한 아미노산[17]", source=[17]),
 dict(name="Leucine", name_ko="류신", class_="필수아미노산", role="nutrient", part="살 가수분해물",
      content_text="가수분해물 0.33 g/kg 섭취 시 류신 19 mg/kg(유청단백질 33 mg/kg)[16]",
      activity_ko="운동 뒤 류신 보유량 109.3 μmol/kg(유청단백질 185.6)[16]", source=[16]),
 dict(name="Hydroxyproline", name_ko="히드록시프롤린", class_="아미노산(콜라겐 유래)", role="nutrient", part="살 가수분해물",
      content_text="0.61–0.88%(w/w)[17]",
      activity_ko="콜라겐 성분에서 유래[17]", source=[17]),
 dict(name="Docosahexaenoic acid", name_ko="DHA", class_="오메가-3 고도불포화지방산", role="nutrient", part="근육",
      content_text="수치는 초록에 없음 — 어린 개체가 DHA 때문에 PUFA가 더 높음[11]",
      activity_ko="어린 개체·성어의 먹이 차이를 보여 주는 지표[11]", source=[11]),
 dict(name="Oleic acid", name_ko="올레산(18:1 n-9)", class_="단일불포화지방산", role="nutrient", part="근육",
      content_text="수치는 초록에 없음 — 성어에서 더 높음[11]",
      activity_ko="성어 근육 MUFA의 주성분[11]", source=[11]),
 dict(name="Gondoic acid", name_ko="곤도산(20:1 n-9)", class_="단일불포화지방산", role="nutrient", part="근육",
      content_text="수치는 초록에 없음 — 성어에서 더 높음[11]",
      activity_ko="요각류 기원 지방산으로 먹이 지표에 쓰임; 성어 MUFA 증가[11]", source=[11]),
 dict(name="1-Dimethylarsinoyltricosane", name_ko="비소 탄화수소 As-HC444", class_="비소지질(arsenolipid)", role="marker", part="어유(통째 가열·압착)",
      content_text="어유 총비소 2.16 μg As/g 중 덜 극성 분획 약 30%에 포함(개별 정량 없음)[25]",
      activity_ko="청대구 어유에서 새로 동정된 비소지질 4종 중 하나, 합성품과 비교해 구조 확인[25]", source=[25]),
 dict(name="Dimethylarsinoyl fatty acids", name_ko="비소 지방산(As-FA)", class_="비소지질(arsenolipid)", role="bioactive", part="어유",
      content_text="극성 분획의 비소 지방산 4종은 전체 비소지질의 5% 미만; 에스터 결합형은 총비소의 약 25%[25]",
      activity_ko="트라이글리세라이드 등 에스터 형태로 존재할 가능성[25]", source=[25]),
 dict(name="Parvalbumin", name_ko="파브알부민", class_="어류 주요 알레르겐 단백질", role="bioactive", part="살",
      content_text="함량 수치 없음 — 서브틸리신 가수분해에서 가장 많이 분해[23]",
      activity_ko="가수분해도가 높을수록 항원성 감소[23]", source=[23]),
]
for c in compounds:
    c["class"] = c.pop("class_")

assays = [
 {"role": "literature", "compound": "Arsenic (total, lipid-soluble arsenolipids)", "compound_ko": "총비소·비소지질", "part": "어유(통째 가열·압착 비정제유, 아이슬란드산)",
  "content": "어유 총비소 2.16 μg As/g; 극성 분획 24%, 덜 극성 분획 약 30%, 비극성 분획 약 45%[25]",
  "method": "ICP-MS(총비소) / HPLC-ESI-MS·HPLC-ICPMS(화학종)",
  "conditions": {"instrument": "Agilent ICPMS 7500ce(ISIS, ASX-500 자동시료주입기, Microflow PFA-100 분무기); 화학종은 역상 HPLC–ICPMS 또는 ESI-MS(Agilent 단일 사중극자), 정밀질량은 LTQ-Velos(분해능 60,000 FWHM)",
                 "column": "Atlantis C18, 150 × 4.6 mm, 5 μm (정제·ESI-MS 분석)",
                 "mobile_phase": "92% 에탄올–완충액(100 mM NH4OAc, pH 5.0)(85+15, v/v) + 8% 클로로폼",
                 "gradient": "등용매",
                 "flow": "0.5 mL/min (1/5을 ESI-MS로 분할)",
                 "temp": "",
                 "detection": "ICPMS: He 충돌 셀 4 mL/min, 내부표준 Ge·In; ESI-MS 양이온 m/z 91 [AsO]+ (fragmentor 400 V), [M+H]+ (150 V)",
                 "injection": "",
                 "sample_prep": "석영관에 시료+진한 질산 2–4 mL → ultraCLAVE III, 아르곤 40 bar, 260 °C 40분 마이크로파 분해 → 물로 20–50 mL 희석; 화학종은 헥산/수성 메탄올(1+9)·수성 아이소프로판올(3+17) 분배 → DEAE Sephadex A-25 음이온교환 분획",
                 "standard": "비소 표준용액(CPI International) 외부검량; 합성 As-HC444·As-FA362",
                 "linearity": "", "lod": "", "loq": "",
                 "recovery": "인증표준물질 DORM-2: 인증값 18.0 ± 1.1 μg/g, 측정값 18.3 ± 1.0 μg/g(n = 9); 실리카/메탄올 처리 시 As-FA362 회수율 >85%"},
  "rationale": "어유에 녹아 있는 비소지질은 청대구 어유의 특징적 성분이자 안전성 평가 대상이다[25]. 전문(Methods) 확인 — 칼럼 온도·주입량·검출한계는 본문에 없음[25].",
  "source": [25], "url": PMC.format("PMC4265782"), "source_kind": "paper"},
 {"role": "literature", "compound": "Glutamic acid", "compound_ko": "글루탐산(아미노산 조성)", "part": "통째·머리·껍질과 뼈 가수분해물(Alcalase)",
  "content": "여러 어종 가수분해물에서 글루탐산 12–15%, 아스파르트산 8–10%[24]; 청대구 산업용 가수분해물 Glx 12.00–12.90 g/100 g[17]",
  "method": "아미노산 분석기(닌히드린 반응, 이온교환)",
  "conditions": {"instrument": "Biochrom 30 series 아미노산 분석기(Biochrom Ltd.)", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "",
                 "detection": "닌히드린 반응(Moore 등 방법)", "injection": "",
                 "sample_prep": "분쇄한 어체 1 kg + 증류수 2 L, 60 °C·pH 8.65, Alcalase 2.4 L 1%(v/w) 4시간 → 여과(뼈 제거) → 15,000×g 20분 원심(기름 분리) → 90 °C 15분 효소 불활성화 → 72시간 동결건조",
                 "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "가수분해물에서 가장 많은 아미노산이라 단백질 소재의 조성 지표로 쓰인다[17, 24]. 전문(Methods) 확인 — 칼럼·완충액·검량 조건은 본문에 없고, 청대구만의 표 값은 본문 텍스트에서 확인하지 못함[24]. 같은 종의 다른 연구는 아미노산 분석을 외부 기관에 맡겼다고만 적었다[17].",
  "source": [17, 24], "url": PMC.format("PMC8231949"), "source_kind": "paper"},
 {"role": "literature", "compound": "Fish protein hydrolysate peptides (molecular weight distribution)", "compound_ko": "가수분해물 펩타이드 분자량 분포", "part": "통째·머리·껍질과 뼈 가수분해물",
  "content": "모든 가수분해물 수평균분자량 Mn < 1,800 Da; 청대구 통째 가수분해물 체외 소화율 97.2%[24]",
  "method": "겔투과 크로마토그래피(GPC, HPLC-RI/DAD/광산란)",
  "conditions": {"instrument": "Agilent 1260 HPLC(4원 펌프, 주입기, 칼럼 오븐, 굴절률·다이오드 어레이·이중각 광산란 검출기)",
                 "column": "PSS Proteema: 전칼럼(5 μm, 8 × 50 mm), 30 Å·100 Å·1000 Å(각 5 μm, 8 × 300 mm)",
                 "mobile_phase": "0.15 M 아세트산암모늄/0.2 M 아세트산(pH 4.5)", "gradient": "등용매", "flow": "1 mL/min", "temp": "30 °C",
                 "detection": "굴절률(dn/dc 0.185)·DAD·광산란", "injection": "100 μL",
                 "sample_prep": "Alcalase 가수분해 후 동결건조한 분말",
                 "standard": "폴리에틸렌옥사이드 표준(Mw 106 kDa, 다분산지수 1.05)",
                 "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "펩타이드 크기가 항산화·ACE 저해 등 생리활성과 관련되어 가수분해물 품질 지표로 쓰인다[24]. 전문(Methods) 확인[24].",
  "source": [24], "url": PMC.format("PMC8231949"), "source_kind": "paper"},
 {"role": "literature", "compound": "Mercury (total) / Methylmercury", "compound_ko": "총수은·메틸수은", "part": "근육(가식부)",
  "content": "지중해산 0.11–1.92 mg/kg 습중량(평균 0.70), 63.6%가 0.5 mg/kg 초과, 대부분 메틸수은(55–100%)[32]",
  "method": "확인하지 못함(초록에 분석법 없음)",
  "conditions": {"instrument": "", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "", "injection": "", "sample_prep": "", "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "수은은 어류 안전성 평가의 핵심 오염물질이며, 청대구는 해역에 따라 함량 차가 크다(북동대서양 평균 0.04 mg/kg)[32, 33]. 전문 확인 못함[32].",
  "source": [32, 33], "url": DOI.format("10.4315/0362-028x-66.2.300"), "source_kind": "paper"},
]

world = [
 {"country": "북동대서양(ICES 해역 1–9, 12, 14) 전체", "metric": "production_t", "year": 2025, "value": 1751013, "unit": "t",
  "note": "ICES 추정치(국가별 쿼터와 예상 소진율 기준, 잠정). 2026년 권고 어획량은 851,344 t[5]", "source": [5]},
 {"country": "북동대서양 연안국 협의", "metric": "tac_t", "year": 2022, "value": 752736, "unit": "t",
  "note": "연안국이 ICES 권고대로 합의한 총어획량 상한(어획 실적 아님)[6]", "source": [6]},
]

d = {
 "slug": "micromesistius-poutassou", "name_ko": "청대구", "name_en": "Blue whiting",
 "scientific_name": "Micromesistius poutassou (Risso, 1827)",
 "aliases": ["청대구", "Blue whiting", "Poutassou", "WHB(FAO 코드)", "Gadus poutassou"],
 "sections": [{"key": k, "title": t, "body": b} for k, t, b in sections],
 "compounds": compounds, "markers": [], "assays": assays, "nutrients": [],
 "production": [], "world": world, "gi": [], "orgs": [], "sources": sources,
}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
print("written", OUT)
