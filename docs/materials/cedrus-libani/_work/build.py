import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
A = "2026-11-02"
def pm(pmid, title, pub, n):
    return {"n": n, "title": title, "url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/", "publisher": pub, "accessed": A}
S = [
 {"n": 1, "title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 레바논개잎갈수지(Cedrus libani A.Rich.), 참죽나무잎·Incense cedar잎·멀구슬나무, 합성향료(Cedarwood oil alcohols·terpenes) 항목", "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
 pm("11962214", "Antimicrobial activity of the resins obtained from the roots and stems of Cedrus libani and Abies cilicica (2002; 초록만 확인)", "Prikladnaia biokhimiia i mikrobiologiia 38(2):166-8", 2),
 pm("10548751", "Antimicrobial activities of several parts of Pinus brutia, Juniperus oxycedrus, Abies cilicia, Cedrus libani and Pinus nigra (1999; 초록만 확인)", "Phytotherapy Research 13(7):584-7", 3),
 pm("28510829", "Cambial activity and xylogenesis in stems of Cedrus libani A. Rich at different altitudes (2015; PMC5430375)", "Botanical Studies 56(1):20", 4),
 {"n": 5, "title": "Chemical composition of the essential oils from oleoresin on cones of Cedrus libani — 원문·서지사항은 열지 못했고(사이트 접속 불가) WebSearch 검색 요약으로만 확인한 내용. 근거로서 한계가 있음", "url": "https://avesis.comu.edu.tr/yayin/2f194b6a-6e94-4677-8691-71b594a9577b/chemical-composition-of-the-essential-oils-from-oleoresin-on-cones-of-cedrus-libani", "publisher": "Çanakkale Onsekiz Mart University AVESIS(연구자 업적 목록) — 원 학술지 확인하지 못함", "accessed": A},
 {"n": 6, "title": "LOTUS 천연물 발생 데이터베이스 — card.json 의 성분 후보(이 종에서 각 1건 보고된 5개 성분)를 고른 근거 DB. 개별 레코드·부위·원 문헌은 직접 확인하지 못함", "url": "https://lotus.naturalproducts.net/", "publisher": "LOTUS (Natural Products Online)", "accessed": A},
 pm("17482448", "Phytochemical analysis and in vitro evaluation of the biological activity against herpes simplex virus type 1 (HSV-1) of Cedrus libani A. Rich. (2007; 초록만 확인)", "Phytomedicine 15(1-2):79-83", 7),
 pm("42086643", "An archaeo-metabolomics approach for identifying cedar tar in archaeological samples: differentiating plant products and production processes (2026; PMC13144440 전문)", "Scientific Reports 16(1)", 8),
 pm("38067421", "Exploring the Larvicidal and Repellent Potential of Taurus Cedar (Cedrus libani) Tar against the Brown Dog Tick (2023; PMC10707419 전문)", "Molecules 28(23):7689", 9),
 pm("39553682", "Insecticidal potential of Cedrus libani tar in eco-friendly control of cat flea from different populations in Türkiye (2024; 초록 확인)", "Heliyon 10(21):e39958", 10),
 pm("35666426", "Cedrus libani tar prompts reactive oxygen species toxicity and DNA damage in colon cancer cells (2022; 초록만 확인)", "Molecular Biology Reports 49(8):7939-7952", 11),
 pm("11677605", "Organic chemistry of embalming agents in Pharaonic and Graeco-Roman mummies (2001; 초록만 확인)", "Nature 413(6858):837-41", 12),
 pm("21816214", "Wound repair and anti-inflammatory potential of essential oils from cones of Pinaceae: preclinical experimental research in animal models (2011; 초록만 확인)", "Journal of Ethnopharmacology 137(3):1215-20", 13),
 pm("20688283", "Cedrus libani (A. Rich) distribution in Lebanon: past, present and future (2010; 초록만 확인)", "Comptes Rendus Biologies 333(8):622-30", 14),
 pm("30743427", "First Report of Brown Felt Blight Caused by Herpotrichia juniperi on Cedrus libani in Turkey (2011)", "Plant Disease 95(2):222", 15),
 pm("30708685", "First Report of Phytophthora syringae on Cedrus libani in Turkey (2014)", "Plant Disease 98(6):846", 16),
 pm("14523524", "Gene flow among different taxonomic units: evidence from nuclear and cytoplasmic markers in Cedrus plantation forests (2003; 초록만 확인)", "Theoretical and Applied Genetics 107(6):1132-8", 17),
 pm("18316301", "Variability in growth, carbon isotope composition, leaf gas exchange and hydraulic traits in the eastern Mediterranean cedars Cedrus libani and C. brevifolia (2008; 초록만 확인)", "Tree Physiology 28(5):689-701", 18),
 pm("22168262", "In vitro evaluation of the anti-proliferative activities of the wood essential oils of three Cedrus species against K562 human chronic myelogenous leukaemia cells (2011; 초록만 확인)", "Natural Product Research 26(23):2227-31", 19),
 pm("31492934", "In Vitro and In Vivo Evaluation of the Anticancer and Anti-inflammatory Activities of 2-Himachelen-7-ol isolated from Cedrus Libani (2019; 초록 확인)", "Scientific Reports 9(1):12855", 20),
 pm("20736907", "Yields and constituents of essential oil from cones of Pinaceae spp. natively grown in Turkey (2010; 초록 확인)", "Molecules 15(8):5797-806", 21),
 pm("16491380", "In vitro storage of cedar shoot cultures under minimal growth conditions (2006; 초록만 확인)", "Plant Cell Reports 25(7):636-42", 22),
 pm("19266933", "Effective number of clones in seed orchards of Cedrus libani A. Rich. (2008; 초록만 확인)", "Pakistan Journal of Biological Sciences 11(17):2159-62", 23),
 pm("37172061", "Impact of climatic conditions on radial growth of non-native Cedrus libani compared to native conifers in Central Europe (2023; 초록 확인)", "PLoS One 18(5):e0275317", 24),
 pm("42108332", "Variation in volatile and flavonoid profiles of Cedrus libani A. Rich. leaves along an elevational gradient (2026; 초록 확인)", "Scientific Reports", 25),
 pm("30476738", "Influence of the early bacterial biofilms developed on vats made with seven wood types on PDO Vastedda della valle del Belìce cheese characteristics (2018; 초록만 확인)", "International Journal of Food Microbiology 291:91-103", 26),
 pm("21485279", "Identification and quantitative determination of lignans in Cedrus atlantica resins using 13C NMR spectroscopy (2011; 다른 종 — 비교용, 초록만 확인)", "Natural Product Communications 6(3):379-85", 27),
 pm("39590106", "Wound Healing Potential of Herbal Hydrogel Formulations of Cedrus brevifolia Extracts in Mice (2024; 다른 종 — 비교용, 초록만 확인)", "Gels 10(11):750", 28),
 pm("20121014", "Effects of release cutting on the development of young natural lebanon cedar (Cedrus libani A. Rich) stands of western Mediterranean region of Turkey (2009; 초록만 확인)", "Journal of Environmental Biology 30(2):179-82", 29),
]

secs = []
def sec(k, t, b): secs.append({"key": k, "title": t, "body": b})

sec("overview", "한눈에 보기",
"레바논개잎갈나무(Cedrus libani A.Rich., 영어 Cedar of Lebanon)는 소나무과(Pinaceae) 개잎갈나무속의 상록 침엽수로, 식약처 「식품원료 목록」에는 '레바논개잎갈수지'라는 원료명으로 올라 있다[1]. 식품원료로서의 지위는 '사용가능'이고 사용 조건은 '사용가능부위 : 수지'이므로, 이 항목으로 쓸 수 있는 부위는 나무에서 나오는 수지뿐이다[1]. 잎·목재·구과(솔방울) 같은 다른 부위는 이 항목의 사용 가능 부위에 들어 있지 않다[1]. 이 종을 원재료로 하는 건강기능식품 고시형 원료는 확인하지 못함.\n\n"
"이 나무는 레바논·시리아·튀르키예의 지중해 산지에 자생한다[19, 20]. 공개 문헌의 대부분은 수지가 아니라 목재 정유, 잎·구과 추출물, 목재를 건류해 만든 타르를 다룬다[7, 9, 21]. 수지 자체에 관해서는 뿌리·줄기 수지의 에탄올 추출물이 원판 확산 시험에서 미생물 생장을 억제했다는 실험실 보고가 있다[2]. 사람을 대상으로 수지의 효과나 안전성을 본 임상시험은 확인하지 못함.")

sec("history", "이름과 이용의 역사",
"국문 원료명 '레바논개잎갈수지'는 식약처 목록의 대표 원료명이며, 목록의 별명 칸은 비어 있다[1]. 영어 이름 칸에는 Cedar of Lebanon이 적혀 있고, 튀르키예 문헌에서는 같은 종을 Taurus cedar(타우루스 시더)라고도 부른다[1, 9]. 레바논에서는 이 나무를 여러 감염성 질환의 전통 약으로 널리 써 왔다고 보고되었지만, 보고에 나온 부위는 목재 정유와 구과·잎 추출물이다[7]. 튀르키예 민간에서는 레바논개잎갈나무가 상처 치유에 쓰였다는 민족식물학 조사가 인용되며, 이를 검증한 동물 실험은 구과 정유를 썼다[13].\n\n"
"고대 이집트 미라 처리와 관련해 헤로도토스가 적은 '시더 오일'은 무엇이었는지 아직 논란이 있다[12]. 최근 연구는 개잎갈나무속 수지·정유·타르가 화학 조성이 겹쳐 고고학 시료에서 구별하기 어렵다고 설명하고, 건류로 생기는 표지 성분으로 후기 왕조 미라 방부제에서 시더 타르를 확인했다[8]. 다만 이 연구의 기준 시료는 아틀라스개잎갈(Cedrus atlantica)이었고 고대 시료의 정확한 종은 밝히지 않았으므로, 레바논개잎갈 수지의 역사로 바로 옮길 수 없다[8]. 튀르키예 안탈리아 지역에서는 목재를 건류한 타르(katran)를 가축의 파리·벼룩·이·진드기 방제에 써 왔고[9], 고양이벼룩 실험에서는 순수 타르가 모든 채집 지역 개체군에서 100% 치사율을 보였다[10].")

sec("biology", "식물학적 특징",
"레바논개잎갈나무는 동지중해 북동부의 넓은 고도 범위에 분포하는 산지성 침엽수다[4]. 튀르키예 타우루스 산맥에서는 해발 1,000–2,000 m 지역에서 생장이 연구되었고, 날마다의 최저기온이 0 °C를 넘고 공기·줄기 평균 온도가 5 °C를 넘을 때 형성층 활동이 시작되었다[4]. 목부 형성은 4–5월에 시작해 9월 말–10월 초에 끝났으며, 기간은 수목한계선 134일에서 가장 낮은 튀르키예 조사지 174일이었다[4]. 같은 연구에서 상처 등으로 생기는 외상성 수지도(traumatic resin duct)가 든 시료는 드물게만 나타났다[4].\n\n"
"수지(resin)는 나무가 분비하는 끈적한 물질로, 목재를 열분해해 만드는 타르와는 다른 물질이다[8]. 개잎갈나무속에서 정유에 많은 아틀란톤류는 분비 수지에는 거의 없고, 수지는 주로 모노테르펜과 아비에탄·피마란형 다이테르페노이드로 이루어진다고 설명된다[8]. 레바논개잎갈 수지만의 조성을 정량해 공개한 논문은 PubMed에서 확인하지 못함.")

sec("related_species", "가까운 종과 혼동 주의",
"개잎갈나무속에는 레바논개잎갈(레바논·시리아·튀르키예), 아틀라스개잎갈(C. atlantica, 모로코·알제리), 키프로스개잎갈(C. brevifolia, 키프로스), 히말라야의 개잎갈나무(C. deodara)가 있다고 소개된다[19]. 프랑스 조림지 연구에서는 아틀라스개잎갈과 레바논개잎갈 사이 유전자 흐름이 자연 수분 묘목의 67–81%를 차지해, 지중해 개잎갈나무들을 하나의 집합종으로 보자는 제안이 나왔다[17]. 키프로스개잎갈은 레바논개잎갈과 따로 비교 연구되는 분류군이다[18]. 아틀라스개잎갈 수지(리그난·아비에트산)나 키프로스개잎갈 수지(겔 상처 실험)의 결과는 다른 종의 자료이므로 이 원료의 성분·효능으로 옮겨 쓰면 안 된다[27, 28].\n\n"
"영어 'cedar'가 붙은 다른 원료도 많아 혼동에 주의해야 한다[1]. 식약처 목록에서 참죽나무(Toona sinensis)는 'Chinese cedar', Incense cedar잎(Calocedrus decurrens)은 'Californian white cedar'로 적힌 전혀 다른 식물이며, 멀구슬나무('bastard cedar')는 '사용불가'다[1]. 같은 목록의 식품첨가물 '합성향료(Cedarwood oil alcohols·terpenes)'는 원료 종이 적혀 있지 않은 별개 품목이다[1]. 식약처 목록에서 개잎갈나무속의 다른 식품원료는 확인하지 못함.")

sec("cultivation", "자생지·조림과 생산",
"레바논개잎갈나무는 현재 주로 튀르키예 남부 타우루스 산맥에 자라며, 시리아·레바논에서는 벌채·화재·염소 방목으로 작은 개체군만 남았다고 보고되었다[15]. 튀르키예의 분포 면적은 황폐 임분과 과거 숲이었던 석회암 나지를 포함해 약 60만 ha로 소개되며, 다른 보고는 순림 면적을 109,440 ha로 적었다[15, 16]. 레바논에서는 기후 변화 모의 결과 2100년에는 레바논산의 세 지역만 생존에 적합할 수 있다고 예측되었다[14].\n\n"
"건조에 강해 튀르키예 반건조 지역 조림에 널리 쓰이며, 묘포에서는 뿌리썩음을 일으키는 Phytophthora syringae 피해가 보고되었다[16]. 어린 천연림에서는 솎아베기 간격이 넓을수록 직경 생장이 좋아졌다[29]. 독일 바이로이트 조림지 등 중부 유럽에서도 기후 변화 대응 수종 후보로 연구된다[4, 24]. 수지를 채취하는 방법·시기·수율이나 국내 재배·생산 통계는 확인하지 못함.")

sec("processing", "가공과 제품",
"이 원료로 쓸 수 있는 것은 수지이므로, 같은 나무에서 얻는 정유·타르·추출물과 구별해야 한다[1, 8]. 수지는 나무가 분비한 물질이지만 타르는 목재를 산소가 적은 상태에서 가열하는 건류로 만든다[8]. 튀르키예 엘말르 지역의 전통 타르는 목재를 열분해해 얻으며, 그 조성은 추출 방법·나무 나이·목재의 수지 함량에 따라 달라진다고 설명된다[9]. 이 타르의 주성분은 β-히말라첸 29.16%, α-아틀란톤 28.7%로, 수지 조성과 같은 것으로 볼 수 없다[9, 8].\n\n"
"심재를 헥산으로 추출한 기름에서는 2-히말라첸-7-올이 약 40%였고, 목재 정유에서는 히말라콜 22.50%·β-히말라첸 21.90%가 주성분이었다[20, 7]. 구과 정유는 수율 0.37 mL/100 g에 리모넨이 22.7%였다[21]. 잎은 고도에 따라 휘발성분·플라보노이드 조성이 다르다는 연구가 있다[25]. 목재는 이탈리아 시칠리아 전통 치즈의 나무통 재료로 시험되어 치즈 품질에 나쁜 영향을 주지 않았다[26]. 식품용 수지 제품의 가공 기준이나 국내 수입·생산실적은 확인하지 못함.")

sec("genetics", "유전체와 분자 연구",
"지중해 개잎갈나무 조림지의 자손을 RAPD·AFLP·엽록체 SSR로 분석한 연구에서, 개잎갈나무속의 엽록체 DNA는 꽃가루 쪽(부계)으로 유전되는 것으로 나타났다[17]. 같은 연구는 아틀라스개잎갈·레바논개잎갈·키프로스개잎갈 사이에 강한 생식 격리가 없고, 엽록체 SSR이 종간 유전자 흐름 감시에 유용하다고 제안했다[17]. 레바논개잎갈 채종원에서는 클론 수 15–33개에 유효 클론 수 24.6–31.4로 계산되었다[23].\n\n"
"아틀라스개잎갈과 레바논개잎갈의 조직배양 신초를 4 °C 저광도에서 최대 6개월 저장해도 RAPD 변이와 평균 DNA 메틸화에 뚜렷한 변화가 없었다[22]. 온실 비교에서는 레바논 산지 계통이 생장은 빨랐지만 가뭄에 가장 민감했고, 튀르키예 계통은 중간이었다[18]. 수지 성분 생합성 유전자나 이 종의 전장 유전체를 다룬 공개 연구는 확인하지 못함.")

sec("safety", "안전성",
"식약처 「식품원료 목록」에서 레바논개잎갈수지의 지위는 '사용가능'이며 사용 가능 부위는 수지다[1]. 이 원료에 대한 별도의 섭취량 기준이나 주의사항은 목록에서 확인하지 못함. 사람에게 수지를 먹였을 때의 독성·알레르기·상호작용을 본 연구나 공공기관 안전 정보는 확인하지 못함.\n\n"
"수지 관련 연구는 실험실 항균 시험뿐이다[2, 3]. 뿌리·줄기 수지 추출물과, 여러 부위의 클로로폼·아세톤·메탄올 추출물이 원판 확산법에서 세균 생장을 억제했으나, 후자에서 항진균 효과는 관찰되지 않았다[2, 3]. 타르는 대장암 세포(HCT-116)에 IC50 30.4 μg/mL로 독성을 보였고 정상 세포(HUVEC)에서는 74.07 μg/mL였는데, 이는 수지가 아닌 타르의 세포 실험이다[11]. 타르를 가축 피부나 물에 넣어 쓸 때 부작용은 관찰되지 않았다고 하나, 연구자들도 비표적 독성 연구가 더 필요하다고 적었다[9]. 목재 정유·구과 정유의 세포·동물 결과는 다른 부위 자료이고 사람에게 같은 효과를 뜻하지 않는다[7, 13, 19].")

comps = [
 {"name": "alpha-Pinene", "name_ko": "α-피넨", "class": "모노테르펜", "role": "bioactive", "part": "수지(구과 표면 올레오레진의 수증기증류 정유)",
  "content_text": "올레오레진 정유의 24.78%(WebSearch 요약으로만 확인, 원문 미확인)[5]", "activity_ko": "침엽수 수지·정유의 대표 휘발 성분. 이 원료에서 생리활성을 확인한 연구는 확인하지 못함", "source": [5]},
 {"name": "Abieta-7,13-diene", "name_ko": "아비에타-7,13-다이엔", "class": "아비에탄형 다이테르펜 탄화수소", "role": "marker", "part": "수지(구과 표면 올레오레진의 수증기증류 정유)",
  "content_text": "올레오레진 정유의 16.67%(WebSearch 요약으로만 확인, 원문 미확인)[5]", "activity_ko": "수지산 계열과 같은 아비에탄 골격의 중성 다이테르펜. 개잎갈나무속 수지는 아비에탄·피마란형 다이테르페노이드가 많다고 설명됨[8]", "source": [5, 8]},
 {"name": "Abieta-8,11,13-triene", "name_ko": "아비에타-8,11,13-트라이엔", "class": "방향족 아비에탄형 다이테르펜", "role": "bioactive", "part": "수지(구과 표면 올레오레진의 수증기증류 정유)",
  "content_text": "올레오레진 정유의 6.85%(WebSearch 요약으로만 확인, 원문 미확인)[5]", "activity_ko": "생리활성 확인하지 못함", "source": [5]},
 {"name": "Manool", "name_ko": "마눌", "class": "라브단형 다이테르펜 알코올", "role": "bioactive", "part": "수지(구과 표면 올레오레진의 수증기증류 정유)",
  "content_text": "올레오레진 정유의 5.83%(WebSearch 요약으로만 확인, 원문 미확인)[5]", "activity_ko": "생리활성 확인하지 못함", "source": [5]},
 {"name": "(1S,4aR,10aR)-1,4a-dimethyl-7-propan-2-yl-2,3,4,9,10,10a-hexahydrophenanthrene-1-carboxylic acid", "name_ko": "데하이드로아비에트산의 입체이성질체(PubChem CID 6552012)", "class": "아비에탄형 수지산", "role": "marker",
  "part": "부위 미상(LOTUS 기록)", "content_text": "함량 확인하지 못함 — LOTUS에 이 종에서 1건 보고, 보고된 생물은 1개 속뿐[6]", "activity_ko": "수지산 계열 성분. 이 원료에서 활성을 확인한 연구는 확인하지 못함", "source": [6]},
 {"name": "(1R,2S,7S,8R,9R)-2,6,6,9-tetramethyltricyclo[5.4.0.02,9]undecan-8-ol", "name_ko": "삼환식 세스퀴테르펜 알코올(PubChem CID 101637059)", "class": "세스퀴테르펜 알코올", "role": "bioactive",
  "part": "부위 미상(LOTUS 기록)", "content_text": "함량 확인하지 못함 — LOTUS에 이 종에서 1건 보고[6]", "activity_ko": "확인하지 못함", "source": [6]},
 {"name": "(4R)-4-[(Z)-6-methyl-4-oxohept-2-en-2-yl]cyclohexene-1-carboxylic acid", "name_ko": "사이클로헥센카복실산계 세스퀴테르페노이드(PubChem CID 162929118)", "class": "세스퀴테르페노이드 산", "role": "bioactive",
  "part": "부위 미상(LOTUS 기록)", "content_text": "함량 확인하지 못함 — LOTUS에 이 종에서 1건 보고, 보고된 생물은 1개 속뿐[6]", "activity_ko": "확인하지 못함", "source": [6]},
 {"name": "beta-Himachalene", "name_ko": "β-히말라첸", "class": "세스퀴테르펜", "role": "bioactive", "part": "목재 정유·타르(수지 아님)",
  "content_text": "목재 정유 21.90%[7]; 목재 타르 29.16%[9]", "activity_ko": "개잎갈나무속의 분류 표지로 알려진 히말라첸류 성분[8]. 수지에서의 함량은 확인하지 못함", "source": [7, 9, 8]},
 {"name": "Himachalol", "name_ko": "히말라콜(2-히말라첸-7-올)", "class": "세스퀴테르펜 알코올", "role": "bioactive", "part": "목재 정유·심재 헥산 추출물(수지 아님)",
  "content_text": "목재 정유 22.50%[7]; 심재 헥산 추출 기름 약 40%[20]", "activity_ko": "분리 성분이 사람 암세포주(뇌 SF-268 IC50 8.1 μg/mL 등)에 세포독성, 쥐 발 부종 모델에서 항염 작용 — 세포·동물 결과[20]", "source": [7, 20]},
 {"name": "alpha-Atlantone", "name_ko": "α-아틀란톤", "class": "세스퀴테르펜 케톤", "role": "bioactive", "part": "목재 타르(수지 아님)",
  "content_text": "목재 타르 28.7%[9]", "activity_ko": "개잎갈나무속 정유·타르에는 많지만 분비 수지에는 거의 없다고 설명됨[8]", "source": [9, 8]},
 {"name": "Limonene", "name_ko": "리모넨", "class": "모노테르펜", "role": "bioactive", "part": "구과 정유(수지 아님)",
  "content_text": "구과 정유의 22.7%(정유 수율 0.37 mL/100 g)[21]", "activity_ko": "구과 정유의 주성분. 수지에서의 함량은 확인하지 못함", "source": [21]},
]

assays = [
 {"role": "literature", "compound": "Volatile constituents of cone oleoresin (alpha-pinene, abieta-7,13-diene, abieta-8,11,13-triene, manool)", "compound_ko": "구과 올레오레진 정유의 휘발 성분",
  "part": "수지(구과 표면 올레오레진)", "content": "α-피넨 24.78%, 아비에타-7,13-다이엔 16.67%, 아비에타-8,11,13-트라이엔 6.85%, 마눌 5.83%(WebSearch 요약으로만 확인)[5]",
  "method": "수증기증류 후 GC-MS(검색 요약 기준)", "conditions": {"instrument": "", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "", "injection": "", "sample_prep": "", "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "이 종의 수지 성분을 백분율로 보고한 것으로 확인된 거의 유일한 자료다. 원문 사이트에 접속하지 못해 전문 확인 못함 — 수치는 WebSearch 요약에서 옮긴 것이고 분석 조건은 비워 둠. 수증기증류로는 수지산이 빠지므로 수지 전체 조성을 대표하지 않는다[5]",
  "source": [5], "url": S[4]["url"], "source_kind": "paper"},
 {"role": "literature", "compound": "Terpenoid volatiles of wood tar (beta-himachalene, alpha-atlantone, ar-turmerone)", "compound_ko": "목재 타르의 테르페노이드 휘발 성분",
  "part": "목재 타르(건류물 — 수지 아님, 비교용)", "content": "43개 성분이 전체의 95.41%; β-히말라첸 29.16%, α-아틀란톤 28.7%, ar-투메론 8.82%, 롱기폴렌 6.66%, α-히말라첸 5.28%, β-투메론 5.12%[9]",
  "method": "GC-MS(EI, 스캔 모드)",
  "conditions": {"instrument": "Thermo Scientific TRACE 1300 GC + ISQ 7000 질량검출기 + RSH Triplus 자동시료주입기", "column": "TRACE TR-5MS(5% 페닐/95% 다이메틸폴리실록산), 30 m × 0.25 mm, 막두께 0.25 μm", "mobile_phase": "운반기체 헬륨", "gradient": "30 °C 5분 유지 → 5 °C/분으로 280 °C → 10분 유지(총 65분)", "flow": "1.5 mL/min", "temp": "주입구 250 °C, 검출기 230 °C", "detection": "질량 스캔 40–550 Da", "injection": "2 μL, 분할비 1/20", "sample_prep": "타르를 아세톤으로 1/500 희석", "standard": "Wiley·NIST 질량 스펙트럼 라이브러리 대조(표준품 정량 아님)", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "같은 나무 목재를 건류한 타르의 조성 분석으로, 수지가 아니다. 개잎갈나무속 타르·정유에 많은 히말라첸·아틀란톤이 분비 수지에는 거의 없다는 점과 대조하라고 넣은 비교 자료다[8, 9]. 전문(PMC10707419)에서 조건 확인",
  "source": [9, 8], "url": "https://pubmed.ncbi.nlm.nih.gov/38067421/", "source_kind": "paper"},
]

d = {"slug": "cedrus-libani", "name_ko": "레바논개잎갈수지", "name_en": "Cedar of Lebanon resin", "scientific_name": "Cedrus libani A.Rich.",
     "aliases": ["레바논개잎갈나무", "Cedar of Lebanon", "Lebanon cedar", "Taurus cedar"],
     "sections": secs, "compounds": comps, "markers": [], "nutrients": [], "assays": assays,
     "production": [], "world": [], "gi": [], "orgs": [], "sources": S}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in secs: print(s["key"], len(s["body"]))
