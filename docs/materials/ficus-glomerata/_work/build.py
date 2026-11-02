import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
A = "2026-11-02"
def pm(pmid, title, pub, pmc=None):
    url = f"https://pmc.ncbi.nlm.nih.gov/articles/{pmc}/" if pmc else f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
    return {"title": title, "url": url, "publisher": pub, "accessed": A}
S = [
 {"title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 우담화열매(Ficus glomerata), Gular열매(Ficus Racemosa Linn)", "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
 pm("23070936", "Design of experiment approach for the process optimisation of microwave assisted extraction of lupeol from Ficus racemosa leaves using response surface methodology (2012, PMID 23070936, doi:10.1002/pca.2403)", "Phytochemical Analysis (PubMed)"),
 pm("26009696", "Phytochemistry, pharmacology, toxicology, and clinical trial of Ficus racemosa (2015, doi:10.4103/0973-7847.156356)", "Pharmacognosy Reviews (PMC)", "PMC4441165"),
 pm("20645741", "Traditional uses, medicinal properties, and phytopharmacology of Ficus racemosa: a review (2010, PMID 20645741, doi:10.3109/13880200903241861)", "Pharmaceutical Biology (PubMed)"),
 pm("19569451", "Udumbara (Ficus glomerata Roxb.): a medico-historical review (2007, PMID 19569451)", "Bulletin of the Indian Institute of History of Medicine (PubMed)"),
 pm("28105059", "Investigation of the key pharmacological activities of Ficus racemosa and analysis of its major bioactive polyphenols by HPLC-DAD (2016, doi:10.1155/2016/3874516)", "Evidence-Based Complementary and Alternative Medicine (PMC)", "PMC5220468"),
 pm("17980529", "Gastroprotective effect of standardized extract of Ficus glomerata fruit on experimental gastric ulcers in rats (2007, PMID 17980529, doi:10.1016/j.jep.2007.09.019)", "Journal of Ethnopharmacology (PubMed)"),
 pm("19951737", "In vitro and in vivo antioxidant properties and DNA damage protective activity of green fruit of Ficus glomerata (2010, PMID 19951737, doi:10.1016/j.fct.2009.11.052)", "Food and Chemical Toxicology (PubMed)"),
 pm("19296381", "Hypoglycaemic and antioxidant activities of Ficus racemosa Linn. fruits (2009, PMID 19296381, doi:10.1080/14786410802230757)", "Natural Product Research (PubMed)"),
 pm("18947904", "Synthesis of alpha-amyrin derivatives and their in vivo antihyperglycemic activity (2009, PMID 18947904, doi:10.1016/j.ejmech.2008.09.011)", "European Journal of Medicinal Chemistry (PubMed)"),
 pm("40604816", "Harnessing animal model and computational experiments to discover antidiabetic compounds in Ficus racemosa (2025, doi:10.1186/s12906-025-04845-7)", "BMC Complementary Medicine and Therapies (PMC)", "PMC12220644"),
 pm("38957785", "Comprehensive study on pharmacognostic, pharmacological, and toxicological features of Ficus racemosa in Alzheimer's disease using GC-MS and molecular docking analyses (2024, PMID 38957785, doi:10.1093/toxres/tfae098)", "Toxicology Research (PubMed 초록)"),
 pm("40727492", "Screening of antihyperglycemic and cytotoxic properties of Ficus racemosa L. fruit extract (2025, PMID 40727492, doi:10.1007/s40203-025-00397-3)", "In Silico Pharmacology (PubMed 초록)"),
 pm("1502122", "Nutritional value of some non-conventional plant foods of India (1992, PMID 1502122, doi:10.1007/BF02193926)", "Plant Foods for Human Nutrition (PubMed 초록)"),
 pm("2548174", "Effect of feeding some plant foods as source of dietary fibre on biological utilisation of diet in rats (1989, PMID 2548174, doi:10.1007/BF01091896)", "Plant Foods for Human Nutrition (PubMed 초록)"),
 pm("41949542", "Prebiotics characterization from traditional legumes and fruits sources and their synergistic effects on probiotic growth and short-chain fatty acid (SCFA) production (2026, PMID 41949542, doi:10.1177/02601060261436306)", "Nutrition and Health (PubMed 초록)"),
 pm("32943080", "The uses of fig (Ficus) by five ethnic minority communities in Southern Shan State, Myanmar (2020, doi:10.1186/s13002-020-00406-z)", "Journal of Ethnobiology and Ethnomedicine (PMC)", "PMC7500007"),
 pm("26709634", "Complete chloroplast genome of Ficus racemosa (Moraceae) (2016, PMID 26709634, doi:10.3109/19401736.2015.1106488)", "Mitochondrial DNA Part A (PubMed 초록)"),
 pm("20561201", "Ficus racemosa is pollinated by a single population of a single agaonid wasp species in continental South-East Asia (2010, PMID 20561201, doi:10.1111/j.1365-294X.2010.04654.x)", "Molecular Ecology (PubMed 초록)"),
 pm("25521512", "High temperatures result in smaller nurseries which lower reproduction of pollinators and parasites in a brood site pollination mutualism (2014, doi:10.1371/journal.pone.0115118)", "PLoS ONE (PMC)", "PMC4270730"),
 pm("14986371", "Structure and biodiversity of insect community on syconia fruits of Ficus racemosa in tropical rainforest of Xishuangbanna, China (2003, PMID 14986371)", "Ying Yong Sheng Tai Xue Bao (PubMed 초록)"),
 pm("24666375", "A trophic cascade induced by predatory ants in a fig-fig wasp mutualism (2014, PMID 24666375, doi:10.1111/1365-2656.12219)", "Journal of Animal Ecology (PubMed 초록)"),
 pm("42468719", "Rapid classification of four Ficus species by UV-spectral fingerprinting coupled with chemometrics (2026, PMID 42468719, doi:10.1016/j.ab.2026.116204)", "Analytical Biochemistry (PubMed 초록)"),
 pm("23716887", "Immunomodulatory activity of methanolic extracts of fruits and bark of Ficus glomerata Roxb. in mice and on human neutrophils (2013, doi:10.4103/0253-7613.108287)", "Indian Journal of Pharmacology (PMC)", "PMC3660923"),
 pm("16414622", "Phytopharmacological evaluation of Ficus glomerata, Roxb. fruit for hypoglycaemic activity in normal and diabetic rabbits (1988, PMID 16414622)", "Pakistan Journal of Pharmaceutical Sciences (PubMed 초록)"),
 pm("21715275", "Formulation and evaluation of Ficus glomerata mucilage sustained release matrix tablets of gliclazide (2011, PMID 21715275)", "Pakistan Journal of Pharmaceutical Sciences (PubMed 초록)"),
 pm("36904456", "Physicochemical characterization and antioxidant properties of chitosan and sodium alginate based films incorporated with Ficus extract (2023, doi:10.3390/polym15051215)", "Polymers (PMC)", "PMC10007391"),
]
for i, s in enumerate(S, 1):
    s["n"] = i
S = [{"n": s["n"], **{k: v for k, v in s.items() if k != "n"}} for s in S]

sections = [
 {"key": "overview", "title": "개요", "body":
  "우담화(Ficus glomerata)는 뽕나무과(Moraceae) 무화과나무속의 나무로, 식약처 「식품원료 목록」에 '우담화열매'라는 이름의 식물성 원료로 실려 있다[1]. 목록에서 이 원료는 '사용가능' 원료이며 사용 조건은 '사용가능부위 : 열매'로, 열매만 식품원료로 쓸 수 있다[1]. 목록의 영문명 칸은 비어 있고, 이 종을 원재료로 하는 건강기능식품 고시형 원료는 확인하지 못함.\n\n"
  "학술 문헌에서 Ficus glomerata Roxb.는 Ficus racemosa L.의 이명(syn.)으로 쓰인다[2]. 같은 식약처 목록에는 학명을 'Ficus Racemosa Linn'으로 적은 'Gular열매'가 따로 실려 있고, 이 항목도 열매만 쓸 수 있는 '사용가능' 원료다[1]. 이 종은 인도·오스트레일리아·동남아시아에 자라며 인도에서는 '굴라르(gular)'로 불린다[3].\n\n"
  "열매에서는 갈산·엘라그산 같은 페놀 성분과 글루아놀 아세테이트·α-아미린 아세테이트 같은 트라이테르페노이드가 보고되었다[3, 6, 7, 10]. 열매·껍질 메탄올 추출물(250·500 mg/kg)이 생쥐에서 항암제로 줄어든 백혈구·혈소판 수를 회복시켰다는 보고도 있다[24]. 열매 추출물의 혈당·위 보호·항산화·면역 연구는 대부분 동물·시험관 결과이며, 사람 대상 열매 연구는 확인하지 못함."},
 {"key": "history", "title": "역사와 이용", "body":
  "인도의 의학사 문헌은 우담화를 '우둠바라(Udumbara)'로 소개하며, 『아타르바베다』에서 신성한 나무로 여겨져 제사에 많이 쓰였고 '야즈뇨둠바라(Yajñodumbara)'라고도 불렸다고 적었다[5]. 아유르베다에서는 껍질·잎·덜 익은 열매 등을 이질·월경과다·객혈 등에 안팎으로 썼다고 한다[5]. 방글라데시에서도 이 나무를 우둠바라로 부른다[6].\n\n"
  "아유르베다에서는 당뇨병·간 질환·설사·염증·치질·호흡기와 비뇨기 질환 등에 오래 써 왔다고 정리되어 있다[4]. 한 종설은 열매를 나병·월경과다·대하·혈액 질환·화상·장내 기생충·마른기침·요로 감염에 쓴 전통 기록을 모았다[3]. 다른 연구는 전통적으로 열매를 빈혈과 위장 질환에 썼다고 소개했다[7].\n\n"
  "인도 아삼 지역의 보도족은 당뇨 예방을 위해 열매 추출물을 먹는다고 보고되었다[13]. 미얀마 남부 샨주 조사에서는 'cluster fig'(이 종의 영어 이름)의 열매·잎이 음식과 민간약으로 쓰였고, 이 무화과류는 인도에서 신 다타구루에게 신성한 나무로 여겨진다고 적혔다[17]. 이런 전통 기록은 효능의 근거가 아니며, 대부분 껍질·뿌리 같은 약용 부위를 함께 다룬다는 점에 주의해야 한다[3, 5]."},
 {"key": "biology", "title": "생물학적 특징", "body":
  "Ficus racemosa(이명 F. glomerata)는 열대·아열대에 자라는 큰 낙엽성 나무로 '클러스터 피그(cluster fig tree)'로도 불린다[2, 11]. 인도에서는 외히말라야·펀자브·비하르·오디샤·서벵골·라자스탄·데칸 등에 널리 분포하고 남인도에서 흔하다[3].\n\n"
  "무화과나무속 식물처럼 꽃이 '은화과(syconium)'라는 닫힌 꽃차례 안에 들어 있고, 이 안에서 꽃가루받이 벌과 기생벌이 함께 자란다[20]. 이 종의 꽃가루받이 벌은 Ceratosolen fusciceps이며, 중국 남부에서 태국 남부까지의 대륙 동남아시아에서는 한 개체군의 한 종만이 꽃가루받이를 맡는 것으로 나타났다[19]. 인도 연구에서는 은화과 부피가 겨울에 가장 크고 여름에 가장 작았으며, 여름 평균기온이 3–5°C 오르자 벌의 번식은 줄고 씨앗 생산은 거의 두 배가 되었다[20].\n\n"
  "중국 시솽반나 열대우림에서 이 종은 핵심종으로 꼽히며, 은화과에서 5목 19과 36속 51종, 모두 184,264마리의 곤충이 채집되었다[21]. 베짜기개미(Oecophylla smaragdina)가 사는 나무에서는 꽃가루받이 벌의 자손과 씨앗이 더 많았다[22]. 열매(은화과)가 줄기에 무리 지어 달리는 생김새는 원문에서 직접 확인하지 못함."},
 {"key": "related_species", "title": "근연종과 혼동 주의", "body":
  "Ficus glomerata Roxb.는 논문에서 Ficus racemosa의 이명으로 함께 표기된다[2]. 식약처 목록에는 '우담화열매(Ficus glomerata)'와 'Gular열매(Ficus Racemosa Linn)'가 서로 다른 항목으로 실려 있어, 두 이름의 자료를 합쳐 볼 때는 같은 식물인지 출처로 확인해야 한다[1, 2].\n\n"
  "같은 속의 무화과(Ficus carica)는 1만 1천 년 넘게 식용·약용으로 재배된 가장 대중적인 종으로, 우담화와는 다른 종이다[17]. 인도 비전통 식품 분석에서도 굴라르(F. glomerata)는 피팔반티(F. religiosa)와 따로 분석되었고, 쥐 사료 연구에서는 F. religiosa·F. bengalensis·F. glomerata를 각각 따로 먹였다[14, 15]. 프리바이오틱 연구에서도 무화과와 '움바르(umbar)'는 따로 시험되었고, 식이섬유·올리고당 함량은 무화과가 더 높았다[16].\n\n"
  "인도네시아 연구는 F. variegata·F. fulva·F. padana·F. racemosa 네 종의 열매 메탄올 추출물을 자외선 스펙트럼과 주성분분석으로 구별했다(PC1 57.6%, PC2 36.7%)[23]. 같은 연구에서 F. racemosa 열매의 DPPH 소거 IC50은 70.46 ± 5 μg/mL였다[23]. 천선과나무·벵갈고무나무 등 국내 목록의 다른 무화과나무속 원료 자료는 이 종의 자료로 옮겨 쓰지 않았다[1]."},
 {"key": "cultivation", "title": "재배와 채취", "body":
  "국내에서 우담화를 재배하거나 열매를 생산한다는 공식 통계는 확인하지 못함. 통계청·농림축산식품부 특용작물 통계에서도 이 품목은 찾지 못했다(확인하지 못함).\n\n"
  "미얀마 남부 샨주 조사에서 응답자들이 말한 무화과류 8종은 모두 야생에서 채취되었고, 열매는 우기에 따는 것이 가장 좋다고 했다[17]. 같은 조사에서 'cluster fig'의 사용 보고는 145건(사용가치 1.27)으로 조사된 8종 가운데 세 번째로 많았다[17]. 응답자의 32%는 무화과류 나무를 집 마당에 심어 먹고 남는 것을 팔기도 한다고 답했다[17].\n\n"
  "열매가 열리는 데는 꽃가루받이 벌이 꼭 필요하며, 기온이 높은 계절에는 은화과가 작아지고 벌의 번식이 줄어든다[20]. 개미가 있는 나무에서는 씨앗 생산이 더 많아, 나무 주변 생태계가 열매 맺음에 영향을 준다[22]. 재배 품종이나 재배 기술 자료는 확인하지 못함."},
 {"key": "processing", "title": "가공과 섭취", "body":
  "미얀마 조사에서는 'cluster fig'를 포함한 몇 종의 덜 익은 열매를 샐러드나 젓갈을 곁들인 반찬으로 먹거나 소금물에 절였고, 익은 열매는 그대로 먹거나 비정제 설탕·설탕으로 잼을 만들었다[17]. 'cluster fig'의 익은 열매를 불에 구워 소금과 함께 먹는 해열 민간요법도 기록되었다[17]. 같은 조사에서 인타족의 '세이카힌' 국은 주로 'cluster fig' 잎으로 만든다고 했지만, 국내 목록에서 이 종은 열매만 쓸 수 있다[1, 17].\n\n"
  "연구에서는 열매를 그늘에 말려 가루로 만든 뒤 메탄올로 우려내 추출물을 얻었고, 말린 열매 가루 300 g에서 59.30 g(19.77% w/w)의 추출물이 나왔다[11]. 토끼 연구에서는 말린 열매 가루를 그대로 먹였다[25]. 열매의 점액질(mucilage)은 말려서 약을 천천히 내보내는 정제의 부형제로 시험되었다[26]. 열매 물 추출물을 키토산·알긴산나트륨 식용 필름에 넣자 항산화성과 열 안정성이 높아졌다[27].\n\n"
  "인도의 '움바르' 올리고당은 이눌린형 프럭탄으로 확인되었고, pH 1.0의 모의 위액에서 58%가 분해되었다[16]. 국내에서 이 열매로 만든 식품이나 건강기능식품의 생산실적은 확인하지 못함."},
 {"key": "genetics", "title": "유전체와 분자 정보", "body":
  "F. racemosa의 엽록체 유전체는 159,473 bp로, 큰 단일복사 영역 88,110 bp, 작은 단일복사 영역 20,007 bp, 한 쌍의 역반복 영역 각 25,678 bp로 이루어진다[18]. 전체 GC 함량은 36.0%이고, 유전자는 단백질 암호 84개, tRNA 27개, rRNA 8개를 포함해 117개다[18].\n\n"
  "이 종의 꽃가루받이 벌 Ceratosolen fusciceps는 마이크로새틀라이트 표지로 분석되었고, 중국 남부에서 태국 남부에 걸친 대륙 지역에서 하나의 개체군만 확인되었다[19]. 이 결과는 무화과나무속과 벌 사이의 '한 종 대 한 종' 관계를 이 종에서 뒷받침한다[19].\n\n"
  "핵 유전체 해독 결과나 열매 품질 관련 유전자 연구는 확인하지 못함. 미얀마 연구는 무화과류처럼 생김새가 비슷한 종을 구별할 때 엽록체 DNA 염기서열 분석이 도움이 될 수 있다고 제안했다[17]. F. glomerata와 F. racemosa가 같은 식물임을 유전자로 직접 비교한 자료는 확인하지 못함."},
 {"key": "safety", "title": "안전성", "body":
  "우담화 열매에 대한 국내 공공기관의 알레르기·잔류·독성 정보는 확인하지 못함. 식약처 목록은 열매만 식품원료로 허용하므로, 껍질·뿌리·잎·유액 연구 결과를 열매 섭취에 그대로 적용하면 안 된다[1, 3].\n\n"
  "열매 메탄올 추출물을 생쥐에게 1,000·2,000·3,000 mg/kg 먹인 급성 독성 시험에서 3,000 mg/kg 이하에서는 죽음이나 부작용이 없었다[11]. 열매·잎 에탄올 추출물은 실험동물에서 혈액 적합성·산화 지표·주요 장기 조직 검사로 해가 없는 것으로 보고되었다[12]. 원자흡광분석에서 열매 추출물의 유해 원소는 미량이었다[13].\n\n"
  "한편 껍질 물 추출물을 생쥐·쥐에 준 시험에서는 간 이상과 가역적 간 독성, 크레아티닌·요소 상승이 보고되어, 약용 부위의 안전성은 열매와 따로 보아야 한다[3]. 열매 추출물은 당뇨 동물에서 혈당을 낮췄으므로[9, 11, 25], 혈당약을 먹는 사람에게서 함께 먹었을 때의 영향은 확인하지 못함. 이 결과들은 모두 동물·시험관 연구이며 사람에서 열매의 안전 섭취량은 확인하지 못함."},
]

compounds = [
 {"name": "Gallic acid", "name_ko": "갈산", "class": "페놀산", "role": "marker", "part": "열매",
  "content_text": "열매 메탄올 추출물 50.11 mg/100 g 건조 추출물(HPLC-DAD)[6]; 열매 50% 에탄올 추출물 0.57% w/w(HPTLC)[7]",
  "activity_ko": "열매 추출물에서 가장 많이 정량된 페놀 성분으로, 원문은 항산화·항균 활성에 기여했을 것으로 추정했다(시험관 결과)[6]", "source": [6, 7]},
 {"name": "Ellagic acid", "name_ko": "엘라그산", "class": "페놀산(가수분해 탄닌 구성)", "role": "marker", "part": "열매",
  "content_text": "열매 50% 에탄올 추출물 0.36% w/w(HPTLC)[7]; 덜 익은 열매 분획에서 검출(수치는 초록에 없음)[8]",
  "activity_ko": "원문은 쥐 위궤양 모델에서 본 위 보호 효과에 페놀 성분이 주로 관여했을 것으로 보았다(동물 결과)[7]", "source": [7, 8]},
 {"name": "Catechin", "name_ko": "카테킨(수화물)", "class": "플라반-3-올", "role": "bioactive", "part": "열매",
  "content_text": "열매 메탄올 추출물 25.34 mg/100 g 건조 추출물(HPLC-DAD, 미량)", "activity_ko": "갈산과 함께 정량된 미량 폴리페놀이다[6]", "source": [6]},
 {"name": "Epicatechin", "name_ko": "에피카테킨", "class": "플라반-3-올", "role": "bioactive", "part": "열매",
  "content_text": "열매 메탄올 추출물 22.14 mg/100 g 건조 추출물(HPLC-DAD, 미량)", "activity_ko": "열매와 잎 추출물 모두에서 검출되었다[6]", "source": [6]},
 {"name": "Chlorogenic acid", "name_ko": "클로로겐산", "class": "하이드록시신남산 에스터", "role": "bioactive", "part": "덜 익은 열매",
  "content_text": "덜 익은 열매 에틸아세테이트 분획에서 검출(함량 수치는 초록에 없음)", "activity_ko": "페놀 함량이 높은 분획에서 갈산·엘라그산과 함께 확인되었고, 이 분획은 사염화탄소 독성 쥐에서 산화 스트레스 지표를 개선했다(동물 결과)[8]", "source": [8]},
 {"name": "3-O-Caffeoylquinic acid", "name_ko": "3-O-(E)-카페오일퀴네이트", "class": "하이드록시신남산 에스터", "role": "bioactive", "part": "열매",
  "content_text": "열매 80% 에탄올 추출물에서 이 식물 최초로 분리(함량 수치는 초록에 없음)", "activity_ko": "DPPH 라디칼 소거 시험에서 뚜렷한 항산화 활성을 보였다(시험관 결과)[9]", "source": [9]},
 {"name": "alpha-Amyrin acetate", "name_ko": "α-아미린 아세테이트", "class": "트라이테르페노이드", "role": "bioactive", "part": "열매",
  "content_text": "열매에서 활성 유도 분리(함량 수치는 초록에 없음)", "activity_ko": "당뇨 쥐에 100 mg/kg 먹였을 때 5시간·24시간 뒤 혈당이 각각 18.4%·17.0% 낮아졌다(동물 결과)[10]", "source": [10]},
 {"name": "Gluanol acetate", "name_ko": "글루아놀 아세테이트", "class": "트라이테르페노이드", "role": "marker", "part": "열매",
  "content_text": "열매의 주성분으로 기재(함량 수치 없음)", "activity_ko": "종설은 열매의 주성분으로 정리했다[3]", "source": [3]},
 {"name": "Lupeol acetate", "name_ko": "루페올 아세테이트", "class": "트라이테르페노이드", "role": "bioactive", "part": "열매",
  "content_text": "열매 성분으로 기재(함량 수치 없음)[3]", "activity_ko": "컴퓨터 도킹에서 SIRT1 단백질과의 결합이 예측되었다(실측 정량 없음, 컴퓨터 예측)[11]", "source": [3, 11]},
 {"name": "Friedelin", "name_ko": "프리델린", "class": "트라이테르페노이드", "role": "bioactive", "part": "열매",
  "content_text": "열매 성분으로 기재(함량 수치 없음)[3]", "activity_ko": "SIRT1 도킹 결합 에너지 −7.4 kcal/mol로 네 후보 가운데 가장 낮았다(컴퓨터 예측)[11]", "source": [3, 11]},
 {"name": "Taraxasterol", "name_ko": "타락사스테롤", "class": "트라이테르페노이드", "role": "bioactive", "part": "열매",
  "content_text": "열매 성분으로 기재(함량 수치 없음)", "activity_ko": "종설이 열매 성분 목록에 올린 트라이테르페노이드다[3]", "source": [3]},
 {"name": "Tiglic acid", "name_ko": "티글산", "class": "단쇄 불포화 유기산", "role": "bioactive", "part": "열매",
  "content_text": "열매 성분으로 기재(함량 수치 없음)", "activity_ko": "종설이 열매 성분 목록에 올렸다[3, 6]", "source": [3, 6]},
 {"name": "Total phenolics", "name_ko": "총페놀·총플라보노이드·총탄닌", "class": "페놀성 화합물(총량)", "role": "bioactive", "part": "열매",
  "content_text": "열매 메탄올 추출물 총페놀 26.2 mg GAE/g, 총플라보노이드 10.63 mg QE/g, 총탄닌 21.39 mg GAE/g(모두 건조 추출물 기준)", "activity_ko": "같은 추출물의 DPPH 소거 IC50은 8.59 μg/mL였다(시험관 결과)[6]", "source": [6]},
 {"name": "Calcium", "name_ko": "칼슘", "class": "무기질", "role": "nutrient", "part": "열매(굴라르)",
  "content_text": "밀의 약 15배(초록 표현, 절대 수치는 초록에 없음)", "activity_ko": "인도 비전통 식품 13종 분석에서 칼슘이 풍부한 식품으로 꼽혔고 아연도 많았다[14]", "source": [14]},
]

assays = [
 {"role": "literature", "compound": "Gallic acid", "compound_ko": "갈산", "part": "열매",
  "content": "열매 메탄올 추출물 50.11 mg/100 g 건조 추출물[6]",
  "method": "HPLC-DAD",
  "conditions": {"instrument": "Dionex UltiMate 3000(4원 펌프 LPG-3400RS, 광다이오드배열검출기 DAD-3000RS)",
   "column": "Acclaim C18, 5 μm, 4.6 × 250 mm(Dionex)",
   "mobile_phase": "A 아세토나이트릴, B 아세트산 용액(pH 3.0), C 메탄올",
   "gradient": "5%A/95%B(0–5분) → 10%A/90%B(6–9분) → 15%A/75%B/10%C(11–15분) → 20%A/65%B/15%C(16–19분) → 30%A/50%B/20%C(20–29분) → 40%A/30%B/30%C(30–35분) → 100%A(36–40분)",
   "flow": "1 mL/min", "temp": "30 °C",
   "detection": "UV 280 nm(22.0분까지) → 320 nm(28.0분) → 280 nm(35분) → 380 nm(36분 이후); DAD 수집 200–700 nm",
   "injection": "20 μL",
   "sample_prep": "열매 가루 250 g을 속슬렛 장치로 메탄올 열추출; 추출물을 메탄올에 10 mg/mL로 녹여 0.20 μm 주사기 필터로 거르고 초음파로 15분 탈기",
   "standard": "폴리페놀 표준품 19종 혼합(갈산 4 μg/mL 등, 메탄올)",
   "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "열매·잎 추출물에서 가장 많이 정량된 폴리페놀이며, 원문은 관찰한 항산화·항균 활성의 주요 후보로 보았다; 검출·정량한계와 회수율은 본문에 없음(전문 확인)[6]",
  "source": [6], "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5220468/", "source_kind": "paper"},
 {"role": "literature", "compound": "Gallic acid; Ellagic acid", "compound_ko": "갈산·엘라그산", "part": "열매",
  "content": "열매 50% 에탄올 추출물 중 갈산 0.57% w/w, 엘라그산 0.36% w/w[7]",
  "method": "HPTLC",
  "conditions": {"instrument": "", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "", "injection": "", "sample_prep": "열매 50% 에탄올 추출물(초록 기재)", "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "위 보호 효과를 본 표준화 추출물의 지표로 두 페놀산을 정량했다; 전문 확인 못함(초록만 확인, 분석 조건 미기재)[7]",
  "source": [7], "url": "https://pubmed.ncbi.nlm.nih.gov/17980529/", "source_kind": "paper"},
]

d = {
 "slug": "ficus-glomerata", "name_ko": "우담화", "name_en": "Cluster fig (Gular)",
 "scientific_name": "Ficus glomerata",
 "aliases": ["우담화열매", "Ficus glomerata Roxb.", "Ficus racemosa L.(이명 관계)", "gular", "Udumbara", "cluster fig"],
 "sections": sections, "compounds": compounds, "markers": [], "nutrients": [],
 "production": [], "world": [], "assays": assays, "gi": [], "orgs": [], "sources": S,
}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
print("ok", len(S))
