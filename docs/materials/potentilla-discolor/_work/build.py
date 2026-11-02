import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
A = "2026-11-02"
def pm(pmid, title, journal): return {"title": title, "url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/", "publisher": f"{journal} (PubMed PMID {pmid})", "accessed": A}
def pmc(pmcid, pmid, title, journal): return {"title": title, "url": f"https://pmc.ncbi.nlm.nih.gov/articles/{pmcid}/", "publisher": f"{journal} (PubMed PMID {pmid}, {pmcid} 전문)", "accessed": A}
S = [
 {"title": "식품원료 목록(솜양지꽃뿌리, Potentilla discolor Bunge)", "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020)", "accessed": "2026-10-13"},
 pm("41532883", "Botany, Phytochemistry, Pharmacology, and Application of Potentilla discolor: A Systematic Review (2026)", "Chemistry & Biodiversity"),
 pmc("PMC9513494", "36176915", "Therapeutic potential of traditional Chinese medicine for the treatment of NAFLD: A promising drug Potentilla discolor Bunge (2022)", "Acta Pharmaceutica Sinica B"),
 pmc("PMC10941989", "38495630", "Mechanisms of Action of Potentilla discolor Bunge in Type 2 Diabetes Mellitus Based on Network Pharmacology and Experimental Verification in Drosophila (2024)", "Drug Design, Development and Therapy"),
 pmc("PMC10577192", "37849729", "Effects of Potentilla discolor Bunge extracts on oxidative stress and glycolipid metabolism in animal models of diabetes: a systematic review and meta-analysis (2023)", "Frontiers in Pharmacology"),
 pm("37301307", "The water extract of Potentilla discolor Bunge (PDW) ameliorates high-sugar diet-induced type II diabetes model in Drosophila melanogaster via JAK/STAT signaling (2023)", "Journal of Ethnopharmacology"),
 pm("40414576", "Molecular mechanisms of Potentilla Discolor Bunge in regulating ferroptosis to alleviate DKD via the Nrf2 signaling pathway (2025)", "Journal of Ethnopharmacology"),
 pmc("PMC7522508", "33043040", "Water Extract of Potentilla discolor Bunge Improves Hepatic Glucose Homeostasis by Regulating Gluconeogenesis and Glycogen Synthesis in HFD/STZ-Induced Type 2 Diabetic Mice (2020)", "Frontiers in Nutrition"),
 pmc("PMC6470731", "30897784", "Beneficial Effects of Potentilla discolor Bunge Water Extract on Inflammatory Cytokines Release and Gut Microbiota in HFD/STZ-Induced Type 2 Diabetic Mice (2019)", "Nutrients"),
 pm("20816941", "Antidiabetic and antioxidant effects of extracts from Potentilla discolor Bunge on diabetic rats induced by high fat diet and streptozotocin (2010)", "Journal of Ethnopharmacology"),
 pm("22960384", "Anti-hyperglycemic effect of Potentilla discolor decoction on obese-diabetic (Ob-db) mice and its chemical composition (2012)", "Fitoterapia"),
 pm("21425380", "Quality evaluation of Potentilla discolor by HPLC-DAD and electrospray ionisation tandem mass spectrometry (2011)", "Phytochemical Analysis"),
 pm("30132635", "[Comparison of Six Flavonoid Components of Closely-Related Plants Agrimonia pilosa, Potentilla chinensis and Potentilla discolor] (2016)", "Zhong Yao Cai"),
 pm("24311372", "Simultaneous determination of corosolic acid and euscaphic acid in the plasma of normal and diabetic rat after oral administration of extract of Potentilla discolor Bunge by HPLC/ESI-MS (2014)", "Biomedical Chromatography"),
 pm("25118630", "Metabonomic analysis of the therapeutic effect of Potentilla discolor in the treatment of type 2 diabetes mellitus (2014)", "Molecular BioSystems"),
 pmc("PMC5384777", "28388692", "Three new C-27-carboxylated-lupane-triterpenoid derivatives from Potentilla discolor Bunge and their in vitro antitumor activities (2017)", "PLoS ONE"),
 pm("18509870", "Structural determination of two new triterpenoids from Potentilla discolor Bunge by NMR techniques (2008)", "Magnetic Resonance in Chemistry"),
 pm("24417146", "[Study on chemical constituents of triterpenoids from Potentilla discolor] (2013)", "Zhong Yao Cai"),
 pm("31022565", "Network pharmacology-based analysis on bioactive anti-diabetic compounds in Potentilla discolor bunge (2019)", "Journal of Ethnopharmacology"),
 pm("34678721", "Potentilla discolor ameliorates LPS-induced inflammatory responses through suppressing NF-κB and AP-1 pathways (2021)", "Biomedicine & Pharmacotherapy"),
 pmc("PMC5865991", "29363716", "Apoptosis induced by methanol extract of Potentilla discolor in human mucoepidermoid carcinoma cells through STAT3/PUMA signaling axis (2018)", "Molecular Medicine Reports"),
 pmc("PMC13518338", "42661785", "Total flavonoids of Potentilla discolor alleviate type 2 diabetes by regulating gut microbiota and endogenous metabolites (2026)", "Frontiers in Microbiology"),
 pm("41515434", "Steam Explosion as a Green Pretreatment Strategy to Enhance Total Phenolics Release and Biological Activities in Potentilla discolor Bunge Stems (2025)", "Molecules"),
 pmc("PMC12143953", "40486272", "Potentilla discolor Bunge Ameliorates Streptozotocin-Induced Diabetic Nephropathy in Mice by Modulating GAS5 and miR-21 Expression (2025)", "International Journal of Endocrinology"),
 {"title": "Isolation of Two Steroids and a Triterpenoid from the Roots of Potentilla discolor (생약학회지 38(4):354–357, 2007) — 원문을 열지 못하고 WebSearch 검색 요약으로만 확인", "url": "https://koreascience.or.kr/article/JAKO200706414130867.view", "publisher": "한국생약학회 「생약학회지」(KoreaScience 서지; WebSearch 요약)", "accessed": A},
 pm("37918684", "Plastid phylogenomics of the tribe Potentilleae (Rosaceae) (2023)", "Molecular Phylogenetics and Evolution"),
 pm("37898296", "Phylogenomic conflict analyses of the plastid and mitochondrial genomes via deep genome skimming: a case study in the cinquefoil genus Potentilla sensu lato (2023)", "Molecular Phylogenetics and Evolution"),
 pm("29608209", "Higher ploidy is associated with reduced range breadth in the Potentilleae tribe (2018)", "American Journal of Botany"),
 pm("40493127", "Comparative chloroplast genome analyses of Potentilleae: insights into genome characteristics, mutational hotspots, and adaptive evolution (2025)", "Genetica"),
 pm("32544818", "PDB-1 from Potentilla discolor Bunge induces apoptosis and autophagy by downregulating the PI3K/Akt/mTOR signaling pathway in A549 cells (2020)", "Biomedicine & Pharmacotherapy"),
 pm("36591818", "Intervention effect of Potentilla discolor-Euonymus alatus on intestinal flora of type 2 diabetes mellitus rats (2022)", "European Review for Medical and Pharmacological Sciences"),
 pm("34472267", "[Mechanism of Potentilla discolor in treating UC by regulating mitochondrial autophagy] (2021)", "Zhongguo Zhong Yao Za Zhi"),
 {"title": "Potentilla discolor Bunge, 1833 (Flora of China 기재문 재수록) — 원문을 열지 못하고 WebSearch 검색 요약으로만 확인", "url": "https://treatment.plazi.org/GgServer/html/AA2261F807545DA296E90617595FDEF7", "publisher": "Plazi TreatmentBank(Flora of China 기재; WebSearch 요약)", "accessed": A},
]
for i, s in enumerate(S, 1): s["n"] = i
S = [{"n": s["n"], "title": s["title"], "url": s["url"], "publisher": s["publisher"], "accessed": s["accessed"]} for s in S]

sec = {}
sec["overview"] = ("솜양지꽃(Potentilla discolor Bunge)은 장미과(Rosaceae) 양지꽃속의 여러해살이풀이다[1, 4]. 식약처 「식품원료 목록」에는 '솜양지꽃뿌리'라는 원료명, 이명 '칠양지꽃', 영문명 Discolor cinquefoil로 실려 있다[1]. 같은 목록에서 이 원료의 상태는 '사용가능'이고 사용 조건은 '사용가능부위 : 뿌리'이므로, 식품원료로 쓸 수 있는 부위는 뿌리뿐이다[1]. 목록에는 같은 학명의 이명으로 Potentilla discolor var. formosana Franch.도 함께 적혀 있다[1].\n\n"
 "중국에서는 이 식물의 말린 전초를 번백초(翻白草, Potentilla discolor herba)라는 약재로 쓴다[2, 22]. 연구의 대부분은 이 전초 약재를 재료로 한 혈당·지질 개선 동물 실험과 성분 분리 연구이며, 성분은 플라보노이드와 트리테르페노이드가 중심이다[2, 5]. 이 자료에 실린 효과는 대부분 전초 추출물로 얻은 세포·동물 결과이고, 뿌리만 따로 시험한 사람 연구는 확인하지 못함. 뿌리만을 다룬 성분 연구로는 국내 학술지의 성분 분리 보고 한 편이 있으나 원문을 열지 못해 검색 요약으로만 확인했다[25].")
sec["history"] = ("이 식물은 14–15세기에 펴낸 중국 최초의 농학·식물학 전문서에 처음 기록되었다고 소개된다[3]. 민간에서는 설사, 학질, 객혈·토혈 같은 출혈 증상에 전초를 써 왔다[12]. 다른 연구진은 이 약재가 과거에 간염, 설사, 외상 출혈에 쓰였다고 정리했다[5, 16]. 중국 전통의학에서는 열을 내리고 피를 식히며 해독·지혈·부기 완화 효능이 있다고 기록되어 있다[3].\n\n"
 "최근에는 당뇨병 보조 치료 약재로 많이 연구되며, 중국 남부 일부 지역에서는 이 약재를 차로 우려 마신다고 한다[4]. 민간에서는 신선하고 연한 줄기를 채소로 먹거나 차로 달여 마신다는 기록도 있다[6, 7]. 연구진은 「중국약전」의 1일 권장 용량을 9–15 g으로 인용했다[4]. 한국에서 뿌리를 식용으로 써 온 역사 기록은 확인하지 못함.\n\n"
 "중국에서는 황기나 화살나무(Euonymus alatus)와 섞은 복합 처방으로도 당뇨 동물 실험이 이루어졌는데, 이런 결과는 솜양지꽃 단독의 효과가 아니다[31, 32]. 전초 에탄올 추출물은 대식세포의 염증 매개체를 줄이고 내독소혈증 생쥐의 설사를 완화했으며[20], 전초 추출물과 주성분 플라본은 당뇨병성 신장병 생쥐의 단백뇨를 줄였다[24]. 국내 연구진은 메탄올 추출물이 침샘 점액표피양암 세포의 사멸을 유도했다고 보고했으나 세포 결과다[21].")
sec["biology"] = ("솜양지꽃은 장미과에 속하는 여러해살이풀로, 아시아에 넓게 분포하며 맛은 약간 달고 쓰다고 기재된다[4]. 북반구 온대 지역에 자라는 식물로 소개되며[5], 중국에서는 주로 산둥·랴오닝·안후이성에서 나고 허베이·허난·네이멍구·후난성에서도 널리 쓰인다[3]. 중국 연구진은 산둥성 타이산의 해발 1,532.7 m 산지에서 8월에 전초를 채집해 연구에 썼다[16].\n\n"
 "Flora of China 기재문은 뿌리가 굵고 아랫부분이 흔히 방추형으로 굵어진다고 적고 있으나, 이 내용은 원문을 열지 못하고 검색 요약으로만 확인했다[33]. 한국 내 자생지·개화기·형태 수치는 공식 자료로 확인하지 못함.")
sec["related_species"] = ("식약처 「식품원료 목록」에는 양지꽃속 원료가 여럿 있으며 부위가 서로 다르다: 딱지꽃(P. chinensis)은 잎·순, 물양지꽃(P. cryptotaeniae)은 잎·순, 흰물싸리(P. fruticosa)는 잎, 가락지나물(P. anemonefolia)은 순, 털딱지꽃(P. chinensis var. concolor)은 잎, Potentilla anserina는 잎만 쓸 수 있다[1]. 솜양지꽃만 뿌리가 사용 가능 부위로 지정되어 있으므로 이들 근연종의 성분·효능 자료를 이 원료에 옮겨 쓰면 안 된다[1].\n\n"
 "중국 연구에서 솜양지꽃·딱지꽃·짚신나물(Agrimonia pilosa) 세 근연 약재의 플라보노이드 6종을 비교한 결과, 아피게닌은 딱지꽃에서 0.028 mg/g 검출되었으나 솜양지꽃과 짚신나물에서는 검출되지 않았다[13]. 같은 연구는 생것에서 말린 것으로 갈 때의 함량 변화 경향이 딱지꽃과 솜양지꽃에서 비슷해 화학분류학적으로 가깝다고 보았다[13]. 양지꽃속(넓은 뜻)은 엽록체·미토콘드리아 유전체 분석에서 8개의 큰 계통군으로 나뉜다[27].")
sec["cultivation"] = ("솜양지꽃의 재배 방법이나 국내 재배 면적·생산량 통계는 확인하지 못함. 농림축산식품부 특용작물 생산실적과 통계청 농작물생산조사 파일에도 이 품목은 없어 국내 생산 통계는 확인하지 못함.\n\n"
 "중국 연구에 쓰인 재료는 허베이성 탕현의 차 제조업체가 공급한 바람에 말린 전초[8, 9], 베이징의 약재 판매점에서 산 전초[4], 산둥성 타이산에서 채집한 야생 전초[16]처럼 대부분 시중 약재나 야생 채집품이다. 채집 연구진은 이 종이 멸종위기종이나 보호종이 아니며 중국에 풍부하게 분포한다고 밝혔다[16]. 뿌리만 따로 수확·유통하는 방식에 관한 자료는 확인하지 못함.")
sec["processing"] = ("약재 번백초는 뿌리를 포함한 식물 전체를 말린 것으로 정의되며[2, 22], 연구에서는 주로 물로 달이거나 에탄올로 추출해 쓴다[4, 9]. 한 연구는 분쇄한 전초를 열 배 부피의 물로 1시간씩 세 번 환류 추출한 뒤 동결건조했다[9]. 다른 연구는 전초 80 g을 70% 에탄올 1,200 mL에 4 °C에서 48시간 담근 뒤 남은 찌꺼기를 물로 다시 끓여 두 추출액을 합쳤다[4]. 전초 달임액을 고분해능 LC-MS/MS로 분석한 연구는 35개 성분을 확인했고, 그중 주요 성분 하나가 황산화 플라보노이드였다[11]. 총 플라보노이드 연구에서는 D-101 거대다공성 수지로 정제해 플라보노이드 함량 72.3%의 분말을 얻었다[22].\n\n"
 "건조 방식도 성분에 영향을 주어, 솜양지꽃과 딱지꽃은 생것이 오븐 건조품보다 플라보노이드가 더 많았다[13]. 줄기에 증기 폭쇄 전처리를 하면 총 페놀 함량이 처리 전보다 1.11–1.94배 늘었다[23]. 이런 가공 연구는 모두 전초나 줄기를 대상으로 했으며, 식품원료로 허용된 뿌리만의 가공 자료와 국내 제품 생산실적은 확인하지 못함.")
sec["genetics"] = ("솜양지꽃 한 종만을 대상으로 한 유전체 해독이나 염색체 수 연구는 PubMed에서 확인하지 못함. 아래는 이 종이 속한 양지꽃족(Potentilleae) 수준의 결과이며, 솜양지꽃이 각 분석에 포함되었는지는 초록으로 확인하지 못함.\n\n"
 "양지꽃족은 13개 속 약 1,700종으로 이루어지며, 158개 표본의 엽록체 유전체 분석에서 Fragariinae와 Potentillinae 두 아족으로 뚜렷이 나뉘었다[26]. 79개 엽록체 유전체를 비교한 연구에서 길이는 150,586–156,798 bp, GC 함량은 36.7–37.3%였고 trnH-psbA 등 13개 구간이 종 구별 표지 후보로 제시되었다[29]. 양지꽃족 109종의 배수성은 2배체에서 12배체까지 다양했다[28]. 넓은 뜻의 양지꽃속은 엽록체·미토콘드리아 자료 모두에서 8개의 지지도 높은 계통군으로 나뉘었다[27].")
sec["safety"] = ("식약처는 솜양지꽃의 뿌리를 식품원료 '사용가능'으로 분류했다[1]. 다만 사람을 대상으로 한 무작위 임상시험이나 독성 시험은 PubMed에서 확인하지 못함. 32개 동물 연구(동물 574마리)를 묶은 메타분석은 전초 추출물이 공복혈당·지질을 낮췄다고 보고했지만, 이상반응 자료가 없어 장기 안전성을 평가할 수 없었다고 밝혔다[5]. 같은 메타분석은 포함된 연구 대부분이 무작위 배정·눈가림을 보고하지 않아 근거의 신뢰도가 낮을 수 있다고 지적했다[5]. 한 종설은 이 약재의 간독성·신독성을 앞으로 조사해야 한다고 적었다[3].\n\n"
 "초파리 실험에서는 전초 추출물이 발달·생존·생식 능력에 영향을 주지 않았다[4]. 전초에서 분리한 일부 트리테르페노이드는 암세포에 세포독성을 보였으나 이는 세포 실험 결과다[16, 30]. 동물에서 혈당을 낮춘 보고가 많으므로[5, 10], 혈당강하제를 복용하는 사람은 섭취 전 전문가와 상의하는 것이 안전하다(사람 상호작용 자료는 확인하지 못함). 알레르기·잔류 농약·중금속에 관한 공공기관 정보는 확인하지 못함.")

titles = {"overview":"개요","history":"역사와 전통적 이용","biology":"생물학적 특징","related_species":"근연종과 혼동 주의","cultivation":"재배와 채취","processing":"가공과 추출","genetics":"유전·계통","safety":"안전성"}
sections = [{"key":k,"title":titles[k],"body":sec[k]} for k in ["overview","history","biology","related_species","cultivation","processing","genetics","safety"]]

def c(name, ko, cls, role, part, content, act, src): return {"name":name,"name_ko":ko,"class":cls,"role":role,"part":part,"content_text":content,"activity_ko":act,"source":src}
compounds = [
 c("beta-Sitosterol","β-시토스테롤","피토스테롤","marker","뿌리(분리), 전초(정량)","뿌리에서 분리 보고(정량값 없음, 검색 요약으로만 확인)[25]; 전초 추출물 HPLC에서 0.076%(원문 표기 그대로)[4]","네트워크 약리·분자 도킹에서 CASP3 결합 예측 — 계산·초파리 결과[4]",[25,4]),
 c("Daucosterol","다우코스테롤(β-시토스테롤 3-O-글루코사이드)","스테롤 배당체","bioactive","뿌리","뿌리에서 분리 보고, 정량값 없음(검색 요약으로만 확인)[25]","이 종에서의 활성 자료 확인하지 못함[25]",[25]),
 c("Fupenjic acid","푸펜지산","우르산형 트리테르펜","bioactive","뿌리","뿌리에서 분리 보고, 정량값 없음(검색 요약으로만 확인)[25]","이 종에서의 활성 자료 확인하지 못함[25]",[25]),
 c("Corosolic acid","코로솔산","우르산형 트리테르펜","marker","전초(뿌리 포함 여부 원문 미기재)","전초의 주요 트리테르페노이드로 기재, 생약 함량 수치 미보고[14]","고지방식 생쥐에서 대사체 이상을 되돌림 — 동물 결과[15]",[14,15]),
 c("Euscaphic acid","유스카프산","우르산형 트리테르펜","bioactive","전초","전초의 주요 트리테르페노이드로 기재, 생약 함량 수치 미보고[14]; 2α,3α,19α-트리하이드록시우르-12-엔-28-산으로 분리[18]","흰쥐 혈장 약동학 분석 대상 — 동물 결과[14]",[14,18]),
 c("Tormentic acid","토르멘트산","우르산형 트리테르펜","bioactive","전초(70% 에탄올 추출물)","분리 화합물, 정량값 없음[18]","이 종에서의 활성 자료 확인하지 못함[18]",[18]),
 c("Maslinic acid","마슬린산","올레아난형 트리테르펜","bioactive","전초(70% 에탄올 추출물)","2α,3β-다이하이드록시올레안-12-엔-28-산으로 분리, 정량값 없음[18]","이 종에서의 활성 자료 확인하지 못함[18]",[18]),
 c("3alpha,30-Dihydroxylup-20(29)-en-27-oic acid","3α,30-다이하이드록시루프-20(29)-엔-27-산","루판형 트리테르펜(C-27 카복실)","bioactive","전초","새 화합물로 분리, 정량값 없음[17]; 같은 계열 신규 화합물 3종이 전초에서 추가 분리됨(IC50 17.84–40.64 μM, 암세포주)[16]","루판형 C-27 카복실 유도체가 암세포 증식 억제 — 세포 결과[16, 17]",[17,16]),
 c("Quercetin","쿼세틴","플라보놀","marker","전초","전초 추출물 HPLC에서 0.030%(원문 표기 그대로)[4]","분자 도킹에서 IL1B·AKT1 결합 예측 — 계산 결과[4]",[4]),
 c("Kaempferol","캠페롤","플라보놀","marker","전초","전초 추출물 HPLC에서 0.025%(원문 표기 그대로)[4]; 극미량으로 보고된 연구도 있음[13]","분자 도킹에서 TNF·AKT1 결합 예측 — 계산 결과[4]",[4,13]),
 c("Rutin","루틴","플라보놀 배당체","marker","전초","6종 플라보노이드 중 함량이 높은 편(수치는 초록에 없음)[13]","이 종 추출물에서의 단독 활성 자료 확인하지 못함[13]",[13]),
 c("Hyperoside","하이페로사이드","플라보놀 배당체","marker","전초","6종 플라보노이드 중 함량이 높은 편(수치는 초록에 없음)[13]","이 종 추출물에서의 단독 활성 자료 확인하지 못함[13]",[13]),
 c("Tricetin","트리세틴","플라본","bioactive","확인하지 못함(초록에 부위 미기재)","GC-MS 분석 성분, 정량값 없음[19]","간암 세포(HepG2)의 포도당 흡수 개선 — 세포 결과[19]",[19]),
 c("Apigenin 7-O-glucoside","아피게닌-7-O-글루코사이드","플라본 배당체","bioactive","전초(물 추출물)","LC-MS/MS로 확인한 주요 6성분 가운데 하나, 정량값 없음[8]","물 추출물 400 mg/kg 8주 투여 시 당뇨 생쥐 공복혈당 감소(추출물 전체 효과) — 동물 결과[8]",[8]),
 c("Epicatechin","에피카테킨","플라반-3-올","bioactive","전초(물 추출물)","LC-MS/MS로 확인한 주요 6성분 가운데 하나, 정량값 없음[8]","단독 활성 자료 확인하지 못함[8]",[8]),
]
E = lambda: {k:"" for k in ["instrument","column","mobile_phase","gradient","flow","temp","detection","injection","sample_prep","standard","linearity","lod","loq","recovery"]}
a1 = E(); a1.update({"instrument":"Shimadzu LC-20A","column":"Agilent Eclipse XDB-C18 (4.6 × 250 mm, 5 μm)","mobile_phase":"쿼세틴·캠페롤: 아세토니트릴–0.2% 인산(15:85); β-시토스테롤: 메탄올–물(98:2)","gradient":"등용매(isocratic)","flow":"1 mL/min","temp":"35 ± 1 °C","detection":"UV 360 nm(쿼세틴·캠페롤), 210 nm(β-시토스테롤)","sample_prep":"분쇄 전초 80 g을 70% 에탄올 1,200 mL에 4 °C 48시간 침지, 찌꺼기를 물 1 L로 1시간 끓여 두 상등액 합침, 0.45 μm 여과, 0.8 g/mL 원액","standard":"중국 식품의약품검정연구원(NIFDC) 표준품"})
a2 = E(); a2.update({"instrument":"UHPLC","column":"Acquity HSS T3 (100 mm × 3.0 mm, 1.8 μm)","mobile_phase":"아세토니트릴–0.3% 빙초산 수용액","flow":"0.4 mL/min","temp":"35 ℃","detection":"360 nm","sample_prep":"70% 에탄올 초음파 추출 0.5시간"})
a3 = E(); a3.update({"instrument":"HPLC-DAD-ESI/MSn","column":"Shimpack C18","mobile_phase":"아세토니트릴–0.1% 포름산","gradient":"기울기 용리(세부 프로그램은 초록에 없음)","detection":"플라보노이드 6종 360 nm, 트리테르페노이드 5종 210 nm"})
assays = [
 {"role":"literature","compound":"Quercetin, kaempferol, beta-sitosterol","compound_ko":"쿼세틴·캠페롤·β-시토스테롤","part":"전초(시판 약재) 추출물 — 뿌리 단독 아님","content":"0.030%, 0.025%, 0.076%(추출물 기준으로 보이나 기준 표기가 분명하지 않음)[4]","method":"HPLC-UV","conditions":a1,"rationale":"분자 도킹 결과로 고른 대표 성분을 품질 확인용으로 정량했다(전문 확인); 직선성·검출한계·회수율은 원문에 없음; 식품원료 부위인 뿌리 자료가 아니므로 참고용[4]","source":[4],"url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC10941989/","source_kind":"paper"},
 {"role":"literature","compound":"Rutin, hyperoside, cynaroside, quercetin, apigenin, kaempferol","compound_ko":"루틴·하이페로사이드·시나로사이드·쿼세틴·아피게닌·캠페롤","part":"전초(생것·건조품) — 뿌리 단독 아님","content":"루틴·하이페로사이드가 대체로 높고 캠페롤은 극미량, 아피게닌은 솜양지꽃에서 불검출[13]","method":"UHPLC-UV","conditions":a2,"rationale":"딱지꽃·짚신나물과 구별·비교하는 플라보노이드 지표로 제시됨; 전문 확인 못함(초록에 적힌 조건만 옮김)[13]","source":[13],"url":"https://pubmed.ncbi.nlm.nih.gov/30132635/","source_kind":"paper"},
 {"role":"literature","compound":"6 flavonoids and 5 triterpenoids (11 marker compounds)","compound_ko":"플라보노이드 6종·트리테르페노이드 5종(지표 11종)","part":"전초(중국 여러 성 10개 시료) — 뿌리 단독 아님","content":"10개 시료에서 11개 지표성분 동시 정량(수치는 초록에 없음)[12]","method":"HPLC-DAD","conditions":a3,"rationale":"이 약재의 품질 평가용 지표성분 동시 정량법으로 직선성·정밀도·정확도·검출/정량한계를 검증했다고 보고됨; 전문 확인 못함(초록 조건만)[12]","source":[12],"url":"https://pubmed.ncbi.nlm.nih.gov/21425380/","source_kind":"paper"},
]
d = {"slug":"potentilla-discolor","name_ko":"솜양지","name_en":"Discolor cinquefoil","scientific_name":"Potentilla discolor Bunge","aliases":["솜양지꽃","솜양지꽃뿌리","칠양지꽃","번백초(翻白草, 전초 약재명)","Potentilla discolor var. formosana Franch.","Potentillae Discoloris Herba","Discolor cinquefoil"],
 "sections":sections,"compounds":compounds,"markers":[],"nutrients":[],"assays":assays,"production":[],"world":[],"gi":[],"orgs":[],"sources":S}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in sections: print(s["key"], len(s["body"]))
