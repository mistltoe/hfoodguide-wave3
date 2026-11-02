import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
A = "2026-11-02"
PM = "https://pubmed.ncbi.nlm.nih.gov/"
PMC = "https://pmc.ncbi.nlm.nih.gov/articles/"
S = [
 (1, "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 산겨릅나무가지·산겨릅나무추출액", "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "식품의약품안전처", "2026-10-13"),
 (2, "Safety Assessment of Acer tegmentosum Maxim. Water Extract: General Toxicity Studies in Sprague-Dawley Rats and Beagle Dogs With Re-evaluation of Genotoxic Potentials (Front Pharmacol 2021;12:687261, PMC8438563)", PMC+"PMC8438563/", "Frontiers in Pharmacology", A),
 (3, "In vitro and in vivo safety evaluation of Acer tegmentosum (J Ethnopharmacol 2013;148:99-105, PMID 23602732)", PM+"23602732/", "Journal of Ethnopharmacology", A),
 (4, "Acer tegmentosum Maxim and fermented products inhibit TNF-α-induced endothelial inflammation and vascular dysfunction of the retina (Front Pharmacol 2024;15:1392179, PMC11614635)", PMC+"PMC11614635/", "Frontiers in Pharmacology", A),
 (5, "Fraxin Prevents Chemically Induced Hepatotoxicity by Reducing Oxidative Stress (Molecules 2017;22:587, PMC6154468)", PMC+"PMC6154468/", "Molecules", A),
 (6, "Isolation and Bioactivity Analysis of Ethyl Acetate Extract from Acer tegmentosum Using In Vitro Assay and On-Line Screening HPLC-ABTS(+) System (J Anal Methods Chem 2014:150509, PMC4216704)", PMC+"PMC4216704/", "Journal of Analytical Methods in Chemistry", A),
 (7, "Effect of Temperature and Covering Structures in Seed Dormancy and Germination Traits of Manchurian Striped Maple (Acer tegmentosum Maxim.) Native to Northeast Asia (Plants 2025;14:767, PMC11901605)", PMC+"PMC11901605/", "Plants (Basel)", A),
 (8, "Stoichiometry patterns in the androdioecious Acer tegmentosum (Sci Rep 2016;6:35022, PMC5057136)", PMC+"PMC5057136/", "Scientific Reports", A),
 (9, "Complete chloroplast genome of Acer tegmentosum and phylogenetic analysis (Mitochondrial DNA B Resour 2019;4:2555-2556, PMC7706611)", PMC+"PMC7706611/", "Mitochondrial DNA Part B", A),
 (10, "Contrasting range changes and drivers of four forest foundation species under future climate change in China (Sci Total Environ 2024;942:173784, PMID 38851330)", PM+"38851330/", "Science of the Total Environment", A),
 (11, "Total peroxyl radical-scavenging capacity of the chemical components from the stems of Acer tegmentosum Maxim. (J Agric Food Chem 2008;56:10510-4, PMID 18942844)", PM+"18942844/", "Journal of Agricultural and Food Chemistry", A),
 (12, "Cytotoxic phenolic constituents of Acer tegmentosum Maxim. (Arch Pharm Res 2006;29:1086-90, PMID 17225455)", PM+"17225455/", "Archives of Pharmacal Research", A),
 (13, "A New Phenyl Ethyl Glycoside from the Twigs of Acer tegmentosum (Nat Prod Commun 2015;10:1251-2, PMID 26411023)", PM+"26411023/", "Natural Product Communications", A),
 (14, "Isoamericanoic Acid B from Acer tegmentosum as a Potential Phytoestrogen (Nutrients 2018;10:1915, PMC6315828)", PMC+"PMC6315828/", "Nutrients", A),
 (15, "Estrogenic Activity of 4-Hydroxy-Benzoic Acid from Acer tegmentosum via Estrogen Receptor α-Dependent Signaling Pathways (Plants 2022;11:3387, PMC9740217)", PMC+"PMC9740217/", "Plants (Basel)", A),
 (16, "Suppression of 6-Hydroxydopamine-Induced Oxidative Stress by Hyperoside Via Activation of Nrf2/HO-1 Signaling in Dopaminergic Neurons (Int J Mol Sci 2019;20:5832, PMC6929192)", PMC+"PMC6929192/", "International Journal of Molecular Sciences", A),
 (17, "Hepatoprotective effects of an Acer tegmentosum Maxim extract through antioxidant activity and the regulation of autophagy (J Ethnopharmacol 2019;239:111912, PMID 31029758)", PM+"31029758/", "Journal of Ethnopharmacology", A),
 (18, "Acer tegmentosum Maxim extract alleviates acute alcohol-induced liver disease and regulates gut microbiota dysbiosis in mice (Arch Biochem Biophys 2025;765:110314, PMID 39832610)", PM+"39832610/", "Archives of Biochemistry and Biophysics", A),
 (19, "Therapeutic Effect of Acer tegmentosum Maxim Twig Extract in Bile Duct Ligation-Induced Acute Cholestasis in Mice (J Med Food 2022;25:652-659, PMID 35708629 — 철회된 논문)", PM+"35708629/", "Journal of Medicinal Food", A),
 (20, "Retraction notice: Therapeutic Effect of Acer tegmentosum Maxim Twig Extract in Bile Duct Ligation-Induced Acute Cholestasis in Mice (J Med Food 2026;29:576, PMID 42029933)", PM+"42029933/", "Journal of Medicinal Food", A),
 (21, "Acer tegmentosum Maxim Inhibits Adipogenesis in 3T3-L1 Adipocytes and Attenuates Lipid Accumulation in Obese Rats Fed a High-Fat Diet (Nutrients 2020;12:3753, PMC7762257)", PMC+"PMC7762257/", "Nutrients", A),
 (22, "Water extract of Acer tegmentosum reduces bone destruction by inhibiting osteoclast differentiation and function (Molecules 2014;19:3940-54, PMC6271087)", PMC+"PMC6271087/", "Molecules", A),
 (23, "In vitro and in vivo anti-inflammatory effects of ethanol extract from Acer tegmentosum (J Ethnopharmacol 2010;128:139-47, PMID 20045722)", PM+"20045722/", "Journal of Ethnopharmacology", A),
 (24, "Effect of Acer tegmentosum bark on atopic dermatitis-like skin lesions in NC/Nga mice (J Ethnopharmacol 2015;177:53-60, PMID 26619913)", PM+"26619913/", "Journal of Ethnopharmacology", A),
 (25, "HIMH0021 attenuates ethanol-induced liver injury and steatosis in mice (PLoS One 2017;12:e0185134, PMC5665428)", PMC+"PMC5665428/", "PLoS One", A),
 (26, "Antidepressant effect and neural mechanism of Acer tegmentosum in repeated stress-induced ovariectomized female rats (Anim Cells Syst 2020;24:205-213, PMC7473002)", PMC+"PMC7473002/", "Animal Cells and Systems", A),
 (27, "Exploring the potential mechanisms of Acer tegmentosum Maxim in preventing alcoholic liver disease based on network pharmacology and molecular docking (Nat Prod Res 2025;40:1565-1569, PMID 39628131)", PM+"39628131/", "Natural Product Research", A),
 (28, "Antiangiogenic Activity of Acer tegmentosum Maxim Water Extract in Vitro and in Vivo (J Korean Med Sci 2015;30:979-87, PMC4479955)", PMC+"PMC4479955/", "Journal of Korean Medical Science", A),
 (29, "Inhibitory effect of Acer tegmentosum maxim extracts on P. gingivalis LPS-induced periodontitis (Arch Oral Biol 2019;109:104529, PMID 31574324)", PM+"31574324/", "Archives of Oral Biology", A),
]
sources = [dict(n=n, title=t, url=u, publisher=p, accessed=a) for n, t, u, p, a in S]

sec = {}
sec["overview"] = ("개요", """산겨릅나무(Acer tegmentosum Maxim.)는 무환자나무과(Sapindaceae, 옛 분류로는 단풍나무과) 단풍나무속의 낙엽 교목이며, 국내에서는 '벌나무' 또는 '산청목'이라는 이름으로도 불린다[1, 7, 9]. 식약처 「식품원료 목록」에는 '산겨릅나무가지'와 '산겨릅나무추출액' 두 원료명이 이명 '벌나무'와 함께 실려 있고, 상태는 모두 '사용가능'이다[1]. 목록이 정한 사용 가능 부위는 가지뿐이며, 정제수로 추출·여과한 뒤 농축(액상)하거나 건조(분말)하는 제조 조건이 붙어 있다[1]. 사용량도 정해져 있어, 농축액·추출분말(고형분 100% 기준)로 유산균음료 2.4 g/kg, 기타발효음료 1.3 g/kg, 인삼·홍삼음료 2.8 g/kg, 기타음료 1.0 g/kg, 액상차 1.8 g/kg, 고형차 26.6 g/kg, 캔디류 9.8 g/kg 이하로만 쓸 수 있다[1].

가지 추출물에 가장 많이 든 것으로 보고된 성분은 페닐에탄올 배당체인 살리드로사이드이며, 그 밖에 플라보노이드·쿠마린·페놀 배당체가 분리되었다[2, 4, 11–13]. 추출물이나 분리 성분은 간 손상, 비만, 골 소실, 우울 행동, 치주염, 혈관신생 모델에서 효과를 보였다고 보고되었다[17, 18, 25, 21, 22, 26, 29, 28]. 그러나 이는 모두 세포나 동물 실험 결과이고, 사람을 대상으로 효과를 시험한 연구는 확인하지 못함.""")
sec["history"] = ("역사와 전통적 이용", """산겨릅나무는 한국 민간에서 간 질환(간염·간경화·간암 등)을 다스리는 데 써 온 나무로 여러 논문에 소개되어 있다[17, 23, 15]. 수피 연구 논문들은 이 나무가 종기, 외상 출혈, 간 질환, 아토피 피부염 등에 민간요법으로 쓰였다고 적었다[14, 24]. 2014년 연구는 한국에서 잎과 줄기를 간 질환과 해독 목적으로 써 왔다고 소개했다[6]. 2025년 종자 연구는 이 나무가 한국에서 '벌나무' 또는 '산청목'으로 불리며 간 질환과 백혈병 치료에 전통적으로 쓰였다고 기술했다[7]. 이런 전통적 이용 기록은 논문 서론에 인용된 내용이며, 원 문헌(고의서 등)은 이번 조사에서 직접 확인하지 못함.

약용을 위한 무분별한 채취 때문에 자생지가 사람이 접근하기 어려운 계곡으로 줄어들었다는 보고가 있다[7]. 2021년 안전성 연구는 이 나무가 건강보조식품과 기능성 식품 재료로 인기를 얻으면서 고농축 제품이 늘었다고 지적했다[2]. 한 논문은 이 나무가 한국에서 '기능성 식품으로 승인'되었다고 적었으나, 이번에 확인한 식약처 자료에서의 지위는 일반 식품원료(사용가능, 가지)이다[17, 1]. 건강기능식품 고시형 원료나 개별인정형 원료로 인정되었는지는 확인하지 못함.""")
sec["biology"] = ("생물학적 특징", """산겨릅나무는 중국 동북부, 러시아 극동 남부, 한국에 자생하는 낙엽 교목이다[7]. 줄기는 곧게 서고 녹회색 나무껍질에 밝은 흰 세로줄 무늬가 있어 관상 가치가 높으며, 병해충에 강한 편으로 알려져 있다[7]. 한국에서는 강원도의 해발 605–1413 m 지역과 지리산에 분포하고, 낙엽활엽수림의 상층과 하층에서 실생 개체가 관찰된다[7].

이 종은 수꽃만 피는 개체와 양성화 개체가 함께 사는 웅성양성이주(androdioecy)라는 드문 번식 체계를 가진다[8]. 수그루 29그루와 양성 그루 31그루를 비교한 연구에서 수그루는 양성 그루보다 잎과 굵은 뿌리의 건물량이 많았고, 잎·새 가지의 탄소·질소·인 비율도 성별에 따라 달랐다[8]. 열매는 날개가 달린 시과이며, 날개를 뗀 시과의 길이·너비·두께는 각각 10.4 mm, 5.2 mm, 2.1 mm, 100개 무게는 3.9 g으로 측정되었다[7]. 중국에서는 당단풍나무(A. pseudo-sieboldianum)와 함께 동북부 온대림의 대표 수종으로 다루어진다[10].""")
sec["related_species"] = ("근연종과 혼동 주의", """식약처 「식품원료 목록」에는 단풍나무속 원료가 여럿 있지만 쓰는 부위가 서로 다르다[1]. 단풍나무(A. palmatum)는 수액 등, 고로쇠(A. pictum subsp. mono)는 수액·전체, 신나무(A. ginnala)와 글라브룸단풍(A. glabrum)은 잎, 설탕단풍(A. saccharum)과 Tatarian maple(A. tataricum)은 수액이 등재 부위다[1]. 이 가운데 가지를 원료로 쓰는 것은 산겨릅나무뿐이므로, 고로쇠 수액이나 단풍 시럽의 성분·효능 자료를 산겨릅나무 가지에 옮겨 적어서는 안 된다[1].

같은 종 안에서도 부위에 따라 페놀 성분 구성이 크게 다르다는 보고가 있어, 수피 연구 결과를 가지 원료에 그대로 적용하기 어렵다[2]. 실제로 피토에스트로겐 후보(이소아메리카노산 B)와 아토피 피부염 동물 연구는 수피 추출물로 이루어졌다[14, 24]. 2021년 안전성 연구도 자신의 결과가 가지만 쓴 시료에서 얻은 것이므로 다른 부위 제품에 적용할 때 주의하라고 밝혔다[2].

주성분 살리드로사이드는 돌꽃속(Rhodiola) 식물의 대표 성분으로도 알려져 있어, 로디올라 제품의 살리드로사이드 자료와 혼동하지 않아야 한다[2]. 시판 '벌나무' 제품이 실제로 이 종인지 가리는 유전자·성분 감별 기준은 확인하지 못함.""")
sec["cultivation"] = ("재배와 채취", """산겨릅나무는 주로 산지에서 채취되어 왔으며, 남획 때문에 집단이 흩어져 분포하게 되었다는 보고가 있다[7]. 세계자연보전연맹(IUCN)은 이 종을 관심대상(LC)으로 보지만 중국 적색목록은 취약(VU)으로 분류한다[7]. 종자 번식 연구는 재배 기술이 확립되면 상업 재배를 통해 남획을 줄이는 데 도움이 될 것이라고 보았다[7].

종자는 흩어질 때 깊은 생리적 휴면 상태이며, 1 °C 또는 4 °C에서 12주 저온 층적 처리를 하면 15/6 °C 조건에서 각각 59.9%, 37.4%가 발아했다[7]. 지베렐린(GA3) 단독 처리로는 휴면이 깨지지 않았고, 어린뿌리 주변의 종피를 일부 벗기면 발아율이 크게 올랐다[7]. 안동의 야외 실험에서는 2월에 발아가 시작되어 3월 말까지 70.7%가 발아했다[7]. 기후변화 모형 연구는 중국에서 이 종의 적합 서식지가 앞으로 남쪽으로 넓어질 것으로 예측했다[10]. 국내 재배 면적·생산량 통계는 확인하지 못함.""")
sec["processing"] = ("가공과 추출", """식약처 목록이 허용한 가공 방식은 가지를 정제수로 추출해 여과한 뒤 농축하여 액상으로 만들거나 건조하여 분말로 만드는 것이다[1]. 이렇게 만든 농축액·추출분말은 고형분 100% 기준으로 음료·차·캔디류별 최대 사용량 안에서만 쓸 수 있다[1].

연구에서 쓰인 추출 방법은 다양하다[2, 4, 6]. 2021년 독성 연구는 말린 가지와 수돗물을 1:20으로 섞어 100 °C에서 12시간 추출한 뒤 농축·여과·동결건조했고, 가지 1 kg당 추출물 74.7 g을 얻었다[2]. 2014년 연구는 줄기 분말 3 kg을 10배 부피의 물로 100 °C에서 3시간 추출해 동결건조했다[6]. 2024년 연구는 가지 분말 400 g을 70% 에탄올 2.5 L로 80 °C에서 2시간 추출했고 수율은 19.6%였다[4].

같은 연구에서 유산균으로 발효시키자 살리드로사이드가 당이 떨어진 티로솔로 바뀌어, 발효물의 살리드로사이드는 4.44%(w/w), 티로솔은 0.75%(w/w)가 되었다[4]. 이 발효물의 효과 비교는 세포 실험 결과다[4]. 식약처 「식품 등의 생산실적」에서 산겨릅나무 품목은 확인하지 못함.""")
sec["genetics"] = ("유전·계통", """산겨릅나무의 엽록체 유전체 전체 길이는 156,435 bp로 보고되었다[9]. 큰 단일복사 영역 86,265 bp, 작은 단일복사 영역 18,102 bp, 한 쌍의 역위반복 영역 각 26,034 bp로 이루어지고, 단백질 암호 유전자 77개, tRNA 유전자 30개, rRNA 유전자 4개가 들어 있다[9]. GC 함량은 37.8%이고 유전자 배열은 다른 무환자나무과 식물과 같았다[9]. 단백질 암호 유전자 76개로 만든 계통수에서 단풍나무속 안의 자매 관계가 확인되었다[9].

산겨릅나무는 플라이스토세 빙하기에 북쪽에서 한반도로 내려온 뒤 높은 산지에 고립된 '북방계 식물'에 속한다[7]. 이런 북방계 식물은 기후변화로 위협받을 수 있다고 지적되었다[7]. 품종 육성이나 유전자원 보존 현황은 확인하지 못함.""")
sec["safety"] = ("안전성", """식약처 「식품원료 목록」은 산겨릅나무를 가지에 한해 '사용가능' 원료로 두되, 정제수 추출물만 허용하고 식품 유형별 최대 사용량(예: 기타음료 1.0 g/kg, 액상차 1.8 g/kg, 고형차 26.6 g/kg 이하)을 정해 두었다[1]. 이 조건을 넘는 고농도 제품이나 다른 부위 제품은 목록의 허용 범위 밖이다[1].

2013년 연구에서 추출물의 급성 경구 반수치사량은 흰쥐에서 2,000 mg/kg 초과였으나, 박테리아 복귀돌연변이 시험(Ames)에서 TA98 균주의 복귀 콜로니가 늘어 변이원성이 의심되었다[3]. 2021년 연구는 가지 열수추출물로 다시 시험해 박테리아 복귀돌연변이·염색체 이상·소핵 시험 모두에서 유전독성이 없다고 보고했다[2]. 같은 연구에서 흰쥐 90일 반복투여의 무독성량(NOAEL)은 5,000 mg/kg 초과였고, 비글견 급성독성도 5,000 mg/kg까지 나타나지 않았다[2]. 두 연구의 차이는 원료 산지·부위나 시료 제조 차이 때문일 수 있다고 저자들이 설명했다[2]. 과량 섭취 때 복통·설사 같은 가벼운 부작용이 드물게 보고된다고 알려져 있다[2].

세포 실험에서 수피 성분과 4-하이드록시벤조산이 에스트로겐 유사 작용을 보였으나, 사람에게서의 의미는 확인하지 못함[14, 15]. 담즙 정체 생쥐에서 가지 추출물의 간 보호를 보고한 2022년 논문은 2026년 철회되었으므로 근거로 쓰지 않는다[19, 20]. 사람 대상 안전성·약물 상호작용 연구와 알레르기·잔류물질에 관한 공공기관 정보는 확인하지 못함.""")
sections = [dict(key=k, title=v[0], body=v[1]) for k, v in sec.items()]

def C(name, ko, cls, role, part, content, act, src):
    return dict(name=name, name_ko=ko, **{"class": cls}, role=role, part=part, content_text=content, activity_ko=act, source=src)
compounds = [
 C("Salidroside", "살리드로사이드", "페닐에탄올 배당체", "marker", "가지(열수·70% 에탄올 추출물)",
   "가지 열수추출 동결건조물 74.3 ± 0.8 mg/g[2]; 추출물 85.01 ± 1.21 mg/g(부위·추출 조건은 초록에 없음)[3]; 가지 70% 에탄올 추출물 6.41%(w/w)[4]",
   "단핵구–혈관내피세포 부착 억제 — 세포 결과[4]; 각질형성세포에서 TSLP 생성 억제 — 세포 결과[24]", [2, 3, 4, 24]),
 C("Tyrosol", "티로솔", "페닐에탄올", "bioactive", "가지 추출물",
   "추출물 3.12 ± 0.04 mg/g[3]; 가지 에탄올 추출물에서는 '매우 적은 성분'으로 기재, 유산균 발효물에서 0.75%(w/w)[4]",
   "SIRT1 결합 예측(도킹)과 혈관내피세포 염증 신호 억제 — 계산·세포 결과[4]", [3, 4]),
 C("6'-O-Galloylsalidroside", "6′-O-갈로일살리드로사이드", "페닐에탄올 배당체", "bioactive", "줄기(열수추출물 에틸아세테이트 분획)",
   "분리 화합물, 정량값 없음(분획에서 60.3 mg 분리)[6]",
   "대식세포의 NO·IL-1β 생성 억제 — 세포 결과[6]", [6]),
 C("Fraxin", "프락신", "쿠마린 배당체", "bioactive", "추출물(부위 미기재)",
   "추출물 1 g당 0.45 mg[5]; 가지에서 분리 보고[12]",
   "시판 표준품 프락신 50 mg/kg 투여 시 사염화탄소 간 손상 흰쥐의 ALT·AST 감소 — 동물 결과(추출물 시험 아님)[5]", [5, 12]),
 C("Quercitrin", "쿼시트린", "플라보놀 배당체", "bioactive", "줄기",
   "줄기에서 분리, 정량값 없음[11]",
   "시험관 퍼옥실 라디칼 소거능이 트롤록스보다 강함 — 시험관 결과[11]", [11]),
 C("Catechin", "(+)-카테킨", "플라반-3-올", "bioactive", "줄기",
   "줄기에서 분리, 정량값 없음[11, 6]",
   "시험관 라디칼 소거, 대식세포 IL-6 생성 억제 — 시험관·세포 결과[11, 6]", [11, 6]),
 C("Hyperoside", "하이페로사이드", "플라보놀 배당체", "bioactive", "부위 미기재",
   "분리 화합물, 정량값 없음[16]",
   "6-OHDA 처리 신경세포에서 Nrf2/HO-1 경로로 세포사 억제 — 세포 결과[16]", [16]),
 C("Avicularin", "아비큘라린", "플라보놀 배당체", "bioactive", "줄기(열수추출물 에틸아세테이트 분획)",
   "분리 화합물, 정량값 없음[6]",
   "대식세포 IL-6 생성 억제(30·50 μM) — 세포 결과[6]", [6]),
 C("Feniculin", "페니큘린", "플라보놀 배당체", "bioactive", "줄기(열수추출물 에틸아세테이트 분획)",
   "이 종에서 처음 분리, 정량값 없음[6]",
   "10 μM에서 TNF-α·IL-6를 약하게 억제 — 세포 결과[6]", [6]),
 C("2,6-Dimethoxy-p-hydroquinone", "2,6-다이메톡시-p-하이드로퀴논", "퀴논류(하이드로퀴논)", "bioactive", "가지(메탄올 추출물)",
   "분리 화합물, 정량값 없음[12]",
   "사람 암세포주 5종에 ED50 1.32–3.85 μM 세포독성 — 세포 결과[12]", [12]),
 C("4-Hydroxybenzoic acid", "4-하이드록시벤조산", "페놀산", "bioactive", "물 추출물(부위는 초록에 없음)",
   "활성 분획에서 분리, 정량값 없음[15]",
   "MCF-7 세포 증식 촉진(에스트로겐 수용체 길항제로 억제) — 세포 결과[15]", [15]),
 C("Kaempferol 3-rhamnoside", "캠페롤-3-람노사이드", "플라보놀 배당체", "bioactive", "부위 미기재",
   "알려진 구성 성분 목록에 포함, 정량값 없음[5]",
   "네트워크 약리 분석에서 상위 활성 후보로 선정 — 계산 결과[27]", [5, 27]),
 C("Isoamericanoic acid B", "이소아메리카노산 B", "1,4-벤조다이옥산 페놀", "bioactive", "수피(식품원료 부위 아님)",
   "수피 물 추출물에서 새 화합물로 분리, 정량값 없음[14]",
   "MCF-7 BUS 세포 증식 시험에서 에스트로겐 유사 활성 — 세포·계산 결과[14]", [14]),
]

assays = [
 dict(role="literature", compound="Salidroside", compound_ko="살리드로사이드", part="가지(열수추출 동결건조물)",
      content="74.3 ± 0.8 mg/g(추출물 기준)[2]", method="HPLC-UV",
      conditions=dict(instrument="Waters HPLC(1525 binary pump, 1500CH column oven, 2027 autosampler), Waters 2489 UV detector",
        column="Imtakt Cadenza CD-C18 (4.6 mm × 300 mm, 5 µm)", mobile_phase="A: 증류수, B: 메탄올/이소프로판올 1:1",
        gradient="A:B 95:5(0–40분), 단 20–25분은 20:80; 총 40분", flow="", temp="25°C", detection="UV 220 nm(머무름 시간 약 10.8분)",
        injection="10 µl", sample_prep="추출물 100 mg을 증류수 25 ml에 초음파로 녹인 뒤 메탄올로 50 ml, 0.45 µm 여과",
        standard="메탄올에 녹인 살리드로사이드 80–200 µg/ml", linearity="", lod="", loq="", recovery=""),
      rationale="저자들이 이 종의 대표 약리 성분으로 보고 독성 시험 시료의 기준 성분으로 정량했다(전문 확인); 유속·직선성·검출한계·회수율은 원문에 없음[2]",
      source=[2], url=PMC+"PMC8438563/", source_kind="paper"),
 dict(role="literature", compound="Salidroside, tyrosol", compound_ko="살리드로사이드·티로솔", part="가지(70% 에탄올 추출물) 및 그 유산균 발효물",
      content="추출물 살리드로사이드 6.41%(w/w); 발효물 살리드로사이드 4.44%(w/w), 티로솔 0.75%(w/w)[4]", method="HPLC-DAD",
      conditions=dict(instrument="Agilent 1260 Infinity II, G7115A-1260 DAD WR", column="Agilent ZORBAX Eclipse Plus C18 (4.6 mm × 250 mm, 5 μm)",
        mobile_phase="A: 0.1% 포름산 수용액, B: 100% 메탄올", gradient="A/B 80/20(0–10분) → 0/100 직선(11–30분) → 0/100(31–35분)",
        flow="1 mL/min", temp="25°C", detection="UV 225/278 nm(살리드로사이드 7.5분, 티로솔 9.5분)", injection="10 μL(시료 3 mg/mL)",
        sample_prep="가지 분말 400 g을 70% 에탄올 2.5 L로 80°C 2시간 추출, 여과·감압농축(수율 19.6%)",
        standard="살리드로사이드·티로솔 각 500 ppm, 외부표준법", linearity="", lod="", loq="", recovery=""),
      rationale="살리드로사이드를 주성분으로, 발효로 생기는 티로솔을 함께 추적하려고 정량했다(전문 확인); 직선성·검출한계·회수율은 원문에 없음[4]",
      source=[4], url=PMC+"PMC11614635/", source_kind="paper"),
 dict(role="literature", compound="Salidroside, tyrosol", compound_ko="살리드로사이드·티로솔", part="추출물(부위는 초록에 없음)",
      content="살리드로사이드 85.01 ± 1.21 mg/g, 티로솔 3.12 ± 0.04 mg/g[3]", method="HPLC",
      conditions=dict(instrument="", column="", mobile_phase="", gradient="", flow="", temp="", detection="", injection="", sample_prep="", standard="", linearity="", lod="", loq="", recovery=""),
      rationale="안전성 시험 시료의 성분 확인용으로 두 성분을 정량했다; 전문 확인 못함(초록만 확인)[3]",
      source=[3], url=PM+"23602732/", source_kind="paper"),
]

d = dict(slug="acer-tegmentosum", name_ko="산겨릅나무", name_en="Manchurian striped maple",
  scientific_name="Acer tegmentosum Maxim.",
  aliases=["벌나무", "산청목", "산겨릅나무가지", "산겨릅나무추출액", "Manchurian stripe maple"],
  sections=sections, compounds=compounds, markers=[], nutrients=[], assays=assays,
  production=[], world=[], gi=[], orgs=[], sources=sources)
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
print("ok")
