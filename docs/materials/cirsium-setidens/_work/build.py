import json, pathlib
P = pathlib.Path(__file__).resolve().parent.parent
A1 = "2026-11-02"
def pm(pmid): return f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
def pmc(x): return f"https://pmc.ncbi.nlm.nih.gov/articles/{x}/"
S = [
 ("식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 고려엉겅퀴·고려엉겅퀴순·고려엉겅퀴잎 등 8개 원료명과 같은 속 원료(흰잎고려엉겅퀴잎·도깨비엉겅퀴잎·엉겅퀴 등)", "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "식품의약품안전처", "2026-10-13"),
 ("Cirsium Setidens Water Extracts Containing Linarin Block Estrogen Deprivation-Induced Bone Loss in Mice (Int J Mol Sci 2023;24(2):1620, PMC9863805)", pmc("PMC9863805"), "International Journal of Molecular Sciences", A1),
 ("Acute and 4-week repeated-dose oral toxicity studies of Cirsium setidens in rats (Molecules 2014;19(6):7138-51, PMC6271068)", pmc("PMC6271068"), "Molecules", A1),
 ("Biological activities of a garlic–Cirsium setidens Nakai blend fermented with Leuconostoc mesenteroides (Food Sci Nutr 2019;7(6):2024-32, PMC6593477)", pmc("PMC6593477"), "Food Science & Nutrition", A1),
 ("Effect of NaCl Pretreatment on the Relationship between the Color Characteristics and Taste of Cirsium setidens Processed Using a Micro-Oil-Sprayed Thermal Air Technique (Plants 2023;12(18):3193, PMC10535967)", pmc("PMC10535967"), "Plants (Basel)", A1),
 ("Comparison of Different Types of SPME Arrow Sorbents to Analyze Volatile Compounds in Cirsium setidens Nakai (Foods 2020;9(6):785, PMC7353593)", pmc("PMC7353593"), "Foods", A1),
 ("Hydroethanolic extract of Cirsium setidens ameliorates doxorubicin-induced cardiotoxicity by AMPK-PGC-1α-SOD-mediated mitochondrial protection (Phytomedicine 2024;129:155633, PMID 38640859, 초록)", pm(38640859), "Phytomedicine", A1),
 ("Effects of Cirsium setidens (Dunn) Nakai on the osteogenic differentiation of stem cells (Mol Med Rep 2021;23(4), PMC7893721, 초록)", pm(33576449), "Molecular Medicine Reports", A1),
 ("Linarin and its aglycone acacetin abrogate actin ring formation and focal contact to bone matrix of bone-resorbing osteoclasts (Phytomedicine 2020;79:153351, PMID 32987362, 초록)", pm(32987362), "Phytomedicine", A1),
 ("Metabolic Alterations in Two Cirsium Species Identified at Distinct Phenological Stages using UPLC-QTOF/MS (Phytochem Anal 2018;29(1):77-86, PMID 28895216, 초록)", pm(28895216), "Phytochemical Analysis", A1),
 ("Pectolinarigenin, an aglycone of pectolinarin, has more potent inhibitory activities on melanogenesis than pectolinarin (Biochem Biophys Res Commun 2017;493(1):765-772, PMID 28851651, 초록)", pm(28851651), "Biochemical and Biophysical Research Communications", A1),
 ("Simultaneous determination of bioactive flavonoids in some selected Korean thistles by high-performance liquid chromatography (Arch Pharm Res 2011;34(3):455-61, PMID 21547678, 초록)", pm(21547678), "Archives of Pharmacal Research", A1),
 ("Pectolinarin and Pectolinarigenin of Cirsium setidens Prevent the Hepatic Injury in Rats Caused by D-Galactosamine via an Antioxidant Mechanism (Biol Pharm Bull 2008;31(4):760-4, PMID 18379079, 초록)", pm(18379079), "Biological & Pharmaceutical Bulletin", A1),
 ("Antioxidant and hepatoprotective activities of Cirsium setidens Nakai against CCl4-induced liver damage (Am J Chin Med 2008;36(1):107-14, PMID 18306454, 초록)", pm(18306454), "The American Journal of Chinese Medicine", A1),
 ("Comparative antioxidant activity and HPLC profiles of some selected Korean thistles (Arch Pharm Res 2008;31(1):28-33, PMID 18277604, 초록)", pm(18277604), "Archives of Pharmacal Research", A1),
 ("Phytochemical constituents of Cirsium setidens Nakai and their cytotoxicity against human cancer cell lines (Arch Pharm Res 2002;25(5):628-35, PMID 12433195, 초록)", pm(12433195), "Archives of Pharmacal Research", A1),
 ("Scopoletin from Cirsium setidens Increases Melanin Synthesis via CREB Phosphorylation in B16F10 Cells (Korean J Physiol Pharmacol 2014;18(4):307-11, PMC4146632, 초록)", pm(25177162), "Korean Journal of Physiology & Pharmacology", A1),
 ("Neuroprotective effects of phytosterols and flavonoids from Cirsium setidens and Aster scaber in human brain neuroblastoma SK-N-SH cells (Life Sci 2016;148:173-82, PMID 26874034, 초록)", pm(26874034), "Life Sciences", A1),
 ("Standardized Cirsium setidens Nakai Ethanolic Extract Suppresses Adipogenesis and Regulates Lipid Metabolisms in 3T3-L1 Adipocytes and C57BL/6J Mice Fed High-Fat Diets (J Med Food 2017;20(8):763-776, PMID 28686516, 초록)", pm(28686516), "Journal of Medicinal Food", A1),
 ("Inhibitory effect of a Cirsium setidens extract on hepatic fat accumulation in mice fed a high-fat diet via the induction of fatty acid β-oxidation (Biosci Biotechnol Biochem 2013;77(7):1424-9, PMID 23832362, 초록)", pm(23832362), "Bioscience, Biotechnology, and Biochemistry", A1),
 ("Antioxidant activity and anti-adipogenic effects of wild herbs mainly cultivated in Korea (Molecules 2013;18(10):12937-50, PMC6270600, 초록)", pm(24141244), "Molecules", A1),
 ("Antioxidant effects of Cirsium setidens extract on oxidative stress in human mesenchymal stem cells (Mol Med Rep 2016;14(4):3777-84, PMC5042755, 초록)", pm(27599894), "Molecular Medicine Reports", A1),
 ("Genome sequence and characterization of a novel fabavirus infecting Cirsium setidens (gondre) in South Korea (Arch Virol 2023;168(2):77, PMID 36725755, 초록)", pm(36725755), "Archives of Virology", A1),
 ("Distinctive origin and evolution of endemic thistle of Korean volcanic island: complete chloroplast genome of Cirsium nipponicum (PLoS One 2023;18(3):e0277471, PMC10010555, 초록)", pm(36913349), "PLoS ONE", A1),
 ("[WebSearch 요약으로만 확인 — 원문은 접속 차단으로 열지 못함] 농촌진흥청 농사로 곤드레 재배 영상·산림청 임산물 재배기술(고려엉겅퀴) 자료의 검색 결과 요약", "https://www.nongsaro.go.kr/portal/ps/psb/psby/vodPlay.ps?mvpNo=550&mvpClipNo=5", "농촌진흥청·산림청(검색 요약)", A1),
 ("[WebSearch 요약으로만 확인 — 원문은 접속 차단으로 열지 못함] 곤드레 재배면적(2018년) 관련 국내 학술지 논문(KoreaScience 등재) 검색 결과 요약", "https://www.koreascience.or.kr/article/JAKO202220362394722.pdf", "KoreaScience(검색 요약)", A1),
]
sources = [dict(n=i+1, title=t, url=u, publisher=p, accessed=a) for i,(t,u,p,a) in enumerate(S)]

sec = {}
sec["overview"] = ("개요", """고려엉겅퀴(Cirsium setidens (Dunn) Nakai)는 국화과 엉겅퀴속의 여러해살이풀로, 강원 지역에서 부르는 '곤드레'라는 이름으로 더 널리 알려져 있다[1, 6]. 식약처 「식품원료 목록」에는 학명 Cirsium setidens (Dunn) Nakai, 영명 Gondre, Korean thistle, 이명 '곤드레·도깨비엉겅퀴'로 실려 있다[1]. 목록에 오른 원료명은 고려엉겅퀴·고려엉겅퀴순·고려엉겅퀴잎·건조고려엉겅퀴·냉동고려엉겅퀴·절임고려엉겅퀴·고려엉겅퀴분말·고려엉겅퀴추출액 8개이며, 모두 상태가 '사용가능'이다[1]. 사용 조건은 여덟 원료명 모두 '사용가능부위 : 순, 잎'으로 같고, 부위 칸에는 고려엉겅퀴순이 '순', 고려엉겅퀴잎이 '잎', 나머지 6개가 '-'로 적혀 있다[1]. 따라서 식품원료로 쓸 수 있는 부위는 순과 잎뿐이며, 뿌리나 꽃은 이 목록의 사용 가능 부위에 들어 있지 않다[1].

잎 추출물에서는 플라보노이드 배당체인 펙톨리나린과 리나린이 주요 성분으로 보고되었고, 에탄올 추출물에서는 클로로젠산과 니코티플로린이 주성분으로 보고되었다[2, 7, 9, 13]. 추출물이나 분리 성분은 간 손상, 지방간, 비만, 골 소실, 심장 독성 모델에서 효과를 보였다고 보고되었다[2, 7, 13, 14, 19, 20]. 세포 실험에서는 줄기세포 골분화 촉진, 지방세포의 지방 축적 억제, 산화 손상 보호가 보고되었다[8, 21, 22]. 그러나 이는 모두 세포나 동물 실험 결과이며, 사람을 대상으로 효과를 시험한 연구는 확인하지 못함.""")
sec["history"] = ("이용의 역사", """고려엉겅퀴는 우리나라 특산 식물로 소개되며, 주로 강원도에서 자라고 '곤드레'라는 이름으로 먹어 왔다[6, 19]. 주로 5월에 수확하고 봄에는 어린잎과 줄기를 먹으며, 나물·국·볶음·데침 요리와 곤드레밥 같은 밥 요리에 쓰고 특유의 향 때문에 차로도 만든다[6]. 곤드레를 넣은 밥 등 가공식품의 생산과 소비가 꾸준히 늘고 있다는 보고가 있다[6]. 한방 민간에서는 부종, 출혈, 객혈 등에 써 왔다고 논문들이 소개한다[4, 19]. 다른 논문은 한의학에서 지혈, 토혈, 혈뇨, 고혈압에 썼다고 적고 있다[3]. 다만 이런 전통 용도는 논문 서론에 인용된 내용이며, 원전 문헌은 확인하지 못함. 갓 수확한 산나물은 신선도가 빨리 떨어지므로 대부분 수확 직후 말려서 저장·유통한다[5].""")
sec["biology"] = ("식물학적 특징", """고려엉겅퀴는 국화과(Asteraceae) 엉겅퀴속(Cirsium)에 속하는 여러해살이풀이다[1, 4]. 한국 특산종으로 소개되며 주로 강원도에서 자란다[6, 19]. 식용 부위인 잎 조직에는 페놀 화합물이 총 클로로필보다 약 4배 많고, 플라보노이드가 페놀 화합물의 약 50%를 차지한다고 보고되었다[5]. 같은 연구는 신선한 고려엉겅퀴의 주된 색이 녹색이며 잎의 색은 클로로필이 만든다고 설명한다[5]. 정영엉겅퀴(C. chanroenicum)와 함께 꽃봉오리 시기와 만개 시기에 채취한 시료를 UPLC-QTOF/MS로 비교한 연구에서는 만개 시기에 페놀산과 페닐프로파노이드 경로 성분이 늘었고, 쿠마르산·캠페롤·펙톨리나리게닌 수준은 두 종 사이에 달랐다[10]. 이 결과는 수확 시기에 따라 성분 조성이 달라질 수 있음을 보여 준다[10]. 고려엉겅퀴를 감염시키는 새로운 파바바이러스(cirsium virus A)가 국내 재배 식물에서 보고되었다[23]. 키·잎 모양·꽃 색과 개화기 같은 형태 정보는 국립생물자원관·국립수목원의 원문을 열지 못해 확인하지 못함.""")
sec["related_species"] = ("근연종과 혼동 주의", """식약처 「식품원료 목록」에는 엉겅퀴속 원료가 여럿 실려 있어 이름이 비슷한 원료와 섞이지 않게 주의해야 한다[1]. 엉겅퀴(Cirsium japonicum var. ussuriense 등)는 순·잎·전초(대계)를 쓸 수 있고, 산우엉(C. dipsacolepis)은 뿌리, 물엉겅퀴(C. tanakae)는 뿌리·잎, 버들잎엉겅퀴(C. lineare)는 순만 쓸 수 있어 고려엉겅퀴(순·잎)와 사용 부위가 다르다[1]. 흰잎고려엉겅퀴(C. setidens var. niveoaraneum Kitam.)는 고려엉겅퀴의 변종으로 '흰잎고려엉겅퀴잎'이라는 별도 원료명으로 실려 있고, 사용 부위는 잎뿐이다[1]. 고려엉겅퀴의 이명으로 '도깨비엉겅퀴'가 적혀 있지만, 같은 목록에는 다른 종(Cirsium schantarense)의 '도깨비엉겅퀴잎'이 따로 있으므로 이 이름만으로 원료를 판단하면 안 된다[1]. 밀크씨슬(Silybum marianum)은 엉겅퀴속이 아닌 다른 속의 식물로 목록에서도 따로 관리된다[1]. 한 논문은 서론에서 고려엉겅퀴에 실리마린이 많다고 적었으나, 이 종에서 실리마린을 정량한 자료는 확인하지 못함[6]. 펙톨리나린은 고려엉겅퀴뿐 아니라 버들잎엉겅퀴·큰엉겅퀴·엉겅퀴 등 여러 국내 엉겅퀴류에서도 검출되어 이 종만의 표지는 아니다[15]. 국내 엉겅퀴류 22개 배치를 함께 분석한 연구도 있으므로, 수치를 인용할 때는 어느 종의 값인지 확인해야 한다[12].""")
sec["cultivation"] = ("재배와 생산", """고려엉겅퀴는 야생 산나물이지만 국내에서 널리 재배되며, 국립산림과학원 시험 포장에서 재배해 상품 수확기에 거둔 시료가 연구에 쓰였다[5]. 연구용 시료는 강원도 지역 시장에서 사거나 정선 지역 생산자 단체에서 공급받은 사례가 있다[2, 6]. 검색 요약으로만 확인한 농사로·산림청 자료에 따르면 종자는 9월 하순~10월 상순에 받아 말려 두었다가 봄에 뿌리거나, 3월 하순~4월 상순에 파종해 40일 정도 기른 모를 5월 중순에 옮겨 심는다[25]. 같은 요약에서는 어린순이 20~30 cm 자라면 밑동을 1~2마디 남기고 베어 수확하고, 2년차 수량을 10a당 3,000~4,000 kg으로 제시했으나 원문은 열지 못했다[25]. 연간 수확 횟수는 요약된 자료마다 연 2~4회에서 5~7회까지 달라 확인이 더 필요하다[25]. 2018년 전국 재배면적이 약 393 ha이고 그중 강원도가 약 315 ha라는 수치도 검색 요약으로만 확인했다[26]. 통계청 농작물생산조사와 농식품부 특용작물 생산실적 로컬 파일에서는 곤드레(고려엉겅퀴) 품목을 찾지 못해, 공식 생산 통계는 확인하지 못함.""")
sec["processing"] = ("가공과 이용", """곤드레는 생으로 유통되는 기간이 짧아 대부분 데친 뒤 말린 건나물 형태로 저장·유통하며, 먹기 전에 다시 물에 불려야 한다[5]. 국립산림과학원 연구에서는 수확한 곤드레를 수돗물이나 5% 소금물에 90 °C로 3분 데친 뒤, 0.2% 기름을 뿌려 90 °C 열풍으로 10분 처리하고 45 °C에서 12시간 건조했다[5]. 소금물 데치기를 함께 한 시료는 밝기가 높아지고 총페놀과 클로로필이 더 잘 보존되었으며, 전자혀로 잰 신맛·짠맛 값이 색 특성과 상관을 보였다[5]. 추출물은 건조 원료 10 kg을 물 200 L로 90 °C에서 4시간 추출해 15 brix로 농축한 뒤 동결건조하는 방식으로 만든 예가 있다[3]. 마늘과 고려엉겅퀴를 섞어 젖산균으로 발효하자 펙톨리나린과 펙톨리나리게닌 함량이 크게 늘었다는 보고가 있다[4]. 1% 아세트산 조건의 마이크로파 처리로 펙톨리나린의 당을 떼어 펙톨리나리게닌 함량을 높이는 방법도 연구되었다[11]. 동결건조 분말의 향기 성분 분석에서는 58종의 휘발성 성분이 확인되었고, 2-펜틸퓨란·1-펜텐-3-올·β-사이클로시트랄·trans-β-이오논 등이 주요 성분이었다[6]. 고려엉겅퀴를 원료로 한 건강기능식품 고시형 원료는 없고, 개별인정형 원료 여부는 확인하지 못함.""")
sec["genetics"] = ("유전체와 분류", """식약처 목록은 고려엉겅퀴의 학명을 Cirsium setidens (Dunn) Nakai로 적고, Cirsium coreanum Nakai와 Saussurea setidens Dunn을 이명으로 함께 적고 있다[1]. 변종인 흰잎고려엉겅퀴(C. setidens var. niveoaraneum Kitam.)는 별도 원료로 등재되어 있다[1]. PubMed 검색에서는 고려엉겅퀴 자체의 엽록체 전장 유전체나 핵 유전체 해독 논문을 확인하지 못함. 울릉도 특산 물엉겅퀴류(C. nipponicum)의 엽록체 유전체는 152,586 bp, 133개 유전자로 보고되었고, 국내 엉겅퀴속 여러 종과의 계통 관계가 분석되었다[24]. 그러나 그 초록에는 고려엉겅퀴가 비교 대상으로 언급되지 않으므로 이 수치를 고려엉겅퀴에 그대로 적용하면 안 된다[24]. 고려엉겅퀴를 감염시키는 바이러스(cirsium virus A)의 전체 염기서열은 RNA1 5,828 nt, RNA2 3,478 nt로 해독되었다[23]. 대사체 수준에서는 정영엉겅퀴와 고려엉겅퀴가 쿠마르산·캠페롤·펙톨리나리게닌 수준에서 구별되었다[10].""")
sec["safety"] = ("안전성", """고려엉겅퀴는 식약처 「식품원료 목록」에서 순과 잎에 한해 '사용가능' 원료이며, 별도의 사용량 제한은 목록에 적혀 있지 않다[1]. 열수 추출물을 쥐에 1,250·2,500·5,000 mg/kg 체중으로 한 번 먹인 급성 독성 시험에서 죽거나 이상 증상을 보인 개체가 없었고, 저자들은 무독성량을 5,000 mg/kg으로 보았다[3]. 같은 용량으로 4주간 반복 투여한 시험에서도 체중, 소변, 혈액, 장기 무게, 조직 검사에서 투여와 관련된 독성 변화가 없었다고 보고되었다[3]. 다만 저자들은 장기 안전성을 위해 만성 독성 시험이 더 필요하다고 적었다[3]. 난소를 제거한 생쥐에 열수 추출물 20 mg/kg을 8주간 먹인 연구에서 혈청 GOT·GPT가 변하지 않아 간 독성 징후는 보이지 않았다[2]. 지상부에서 분리한 한 테르펜 성분은 사람 암세포주에 세포독성을 보였는데, 이는 세포 실험 결과로 식품 섭취 시 위험을 뜻하지 않는다[16]. 효능으로 보고된 내용도 세포·동물 결과이며 사람 대상 임상 연구는 확인하지 못함. 국화과 식물 알레르기나 잔류농약 부적합 등 고려엉겅퀴에 관한 공공기관 안전 정보는 확인하지 못함.""")

sections = [dict(key=k, title=v[0], body=v[1]) for k,v in sec.items()]

C = lambda **k: k
compounds = [
 C(name="Pectolinarin", name_ko="펙톨리나린", class_="플라보노이드 배당체(플라본)", role="marker", part="잎(부탄올 분획)[13]; 열수추출물[11]",
   content_text="잎 메탄올 추출물 부탄올 분획의 주 플라보노이드 배당체로 분리[13]; 열수추출물에서 펙톨리나리게닌보다 함량이 높음(초록에 수치 없음)[11]; 원료 열수추출 동결건조물에서는 불검출[4]",
   activity_ko="D-갈락토사민 간 손상 쥐에서 10·20 mg/kg 경구 2주 투여 시 간 효소 수치 감소 — 동물 결과[13]; SK-N-SH 세포 산화 손상 보호 — 세포 결과[18]; 멜라닌 생성 억제 — 세포·인공피부 결과[11]", source=[4, 11, 13, 18]),
 C(name="Pectolinarigenin", name_ko="펙톨리나리게닌", class_="플라본(펙톨리나린의 비당체)", role="bioactive", part="열수추출 동결건조물(부위 미기재)",
   content_text="고려엉겅퀴 단독 열수추출물 3.70 ± 0.07 mg/g[4]; 마늘 50:고려엉겅퀴 50 혼합 발효물 8.49 ± 0.17 mg/g[4]",
   activity_ko="간 손상 쥐 모델에서 간 보호 — 동물 결과[13]; 멜라닌 생성 억제가 펙톨리나린보다 강함 — 세포 결과[11]", source=[4, 11, 13]),
 C(name="Linarin", name_ko="리나린", class_="플라보노이드 배당체(플라본)", role="marker", part="잎 열수추출물",
   content_text="열수추출물의 주요 성분으로 HPLC로 확인(초록에 수치 없음)[9]",
   activity_ko="파골세포 분화·골 흡수 억제 — 세포 결과[9]; 난소 제거 생쥐 20 mg/kg 8주 투여 시 골밀도 감소 완화 — 동물 결과[2]", source=[2, 9]),
 C(name="Chlorogenic acid", name_ko="클로로젠산", class_="페놀산", role="bioactive", part="에탄올 추출물[7]; 열수추출물(부위 미기재)[3]",
   content_text="열수추출물 53.04 mg/100 g 추출물[3]; 에탄올 추출물의 주성분(UPLC-TQ/MS, 초록에 수치 없음)[7]",
   activity_ko="추출물 수준에서 독소루비신 심장독성 완화 보고(성분 단독 효과는 아님) — 세포·동물 결과[7]", source=[3, 7]),
 C(name="Nicotiflorin", name_ko="니코티플로린", class_="플라보놀 배당체(캠페롤 루티노사이드)", role="bioactive", part="에탄올 추출물",
   content_text="에탄올 추출물의 주성분으로 보고(초록에 수치 없음)[7]",
   activity_ko="개별 활성은 이 종 연구에서 확인하지 못함[7]", source=[7]),
 C(name="Apigenin", name_ko="아피제닌", class_="플라본", role="bioactive", part="부위 미기재",
   content_text="고려엉겅퀴에 리나린·펙톨리나린과 함께 들어 있다고 기술(수치 없음)[2]; 국내 엉겅퀴류 품질관리 지표 6종 중 하나[12]",
   activity_ko="이 종에서 개별 활성 확인하지 못함[2]", source=[2, 12]),
 C(name="Caffeic acid", name_ko="카페산", class_="페놀산", role="bioactive", part="열수추출물(부위 미기재)",
   content_text="36.30 mg/100 g 추출물[3]", activity_ko="이 종에서 개별 활성 확인하지 못함[3]", source=[3]),
 C(name="Scopoletin", name_ko="스코폴레틴", class_="쿠마린", role="bioactive", part="부위 미기재(분리)",
   content_text="고려엉겅퀴에서 분리(함량 수치 없음)[17]",
   activity_ko="B16F10 세포에서 CREB 인산화를 거쳐 멜라닌 합성 증가 — 세포 결과[17]", source=[17]),
 C(name="alpha-Tocopherol", name_ko="알파-토코페롤", class_="토코페롤(비타민 E)", role="nutrient", part="지상부 염화메틸렌 추출물",
   content_text="지상부에서 분리한 11개 성분 중 하나(함량 수치 없음)[16]", activity_ko="이 종에서 개별 활성 확인하지 못함[16]", source=[16]),
 C(name="24-hydroperoxycycloart-25-en-3beta-ol", name_ko="24-하이드로퍼옥시사이클로아트-25-엔-3β-올", class_="트리테르펜(사이클로아르탄)", role="bioactive", part="지상부 염화메틸렌 추출물",
   content_text="지상부에서 분리(함량 수치 없음)[16]",
   activity_ko="사람 암세포주 5종에 ED50 2.66–11.25 µM의 세포독성 — 세포 결과[16]", source=[16]),
 C(name="2-Pentylfuran", name_ko="2-펜틸퓨란", class_="퓨란(휘발성 향기 성분)", role="bioactive", part="동결건조 분말(시장 구입 원료)",
   content_text="CWR/PDMS SPME Arrow 추출에서 가장 높은 농도로 검출(피크 면적 기준, 절대 함량 없음)[6]",
   activity_ko="흙·콩 같은 채소 향을 내며 리놀레산 산화로 생기는 향기 성분[6]", source=[6]),
 C(name="beta-Cyclocitral", name_ko="β-사이클로시트랄", class_="모노테르페노이드(카로티노이드 유래)", role="bioactive", part="동결건조 분말",
   content_text="주요 휘발성 성분 중 하나(피크 면적 기준)[6]", activity_ko="단 향·과일 향에 기여[6]", source=[6]),
 C(name="beta-Ionone", name_ko="β-이오논", class_="노르이소프레노이드(카로티노이드 유래)", role="bioactive", part="동결건조 분말",
   content_text="trans-β-이오논이 주요 휘발성 성분 중 하나(피크 면적 기준)[6]", activity_ko="제비꽃 같은 단 꽃 향에 기여[6]", source=[6]),
]
for c in compounds: c["class"] = c.pop("class_")
compounds = [{k: c[k] for k in ("name","name_ko","class","role","part","content_text","activity_ko","source")} for c in compounds]

E = lambda: {k: "" for k in ("instrument","column","mobile_phase","gradient","flow","temp","detection","injection","sample_prep","standard","linearity","lod","loq","recovery")}
a1 = E(); a1.update(column="Waters Spherisorb INNO C18 (4.6 × 250 mm, 5 μm)", mobile_phase="A: 물, B: 아세토니트릴",
  gradient="A:B 75:25에서 시작 → 10:90(30분) → 0:100(20분) → 75:25(15분)", flow="1 ml/min", detection="UV 254 nm", injection="10 μL",
  sample_prep="건조 원료 200 g을 물로 추출·여과·동결건조(건조 추출물 20 g), 메탄올에 녹여 0.45 μm 주사기 필터로 여과, 3회 주입",
  standard="펙톨리나린·펙톨리나리게닌(메탄올 1 mg/ml 원액을 단계 희석)", linearity="0.0001–1.0 mg/ml, 5개 농도 3회 주입", lod="S/N 3 기준(값은 본문에 없음)", loq="S/N 10 기준(값은 본문에 없음)", recovery="첨가 회수로 평가(값은 본문에 없음)")
a2 = E(); a2.update(column="Agilent Eclipse XDB-C18", mobile_phase="0.1% 트리플루오로아세트산 수용액–메탄올", gradient="기울기 용리(세부 조건은 초록에 없음)",
  flow="1.0 mL/min", detection="UV 254 nm", standard="루테올린 5-O-글루코사이드, 루테올린 7-O-글루코사이드, 히스피둘린 7-O-네오헤스페리도사이드, 루테올린, 펙톨리나린, 아피제닌", linearity="R² > 0.991(6종 모두)", recovery="90.01–100.05%")
a3 = E(); a3.update(instrument="Agilent 1100 series HPLC, 다이오드 어레이 검출기", column="Macherey-Nagel Nucleosil 100-5 C-18 (250 mm × 4.0 mm, 5 μm), 10 mm 가드 칼럼",
  mobile_phase="A: 포름산 0.035%(v/v)로 pH 3.29로 맞춘 물, B: 아세토니트릴", gradient="B 0→15%(45분), 15→30%(15분), 30→50%(5분), 50→100%(5분), 100→0%(10분)",
  detection="DAD 270 nm(280·320·370 nm도 함께 기록)", injection="10 µL", sample_prep="건조 원료 10 kg을 물 200 L로 90 °C 4시간 추출, 여과, 15 brix로 농축 후 96시간 동결건조",
  standard="클로로젠산·카페산·갈산·루틴 등 18종 표준품")
a4 = E(); a4.update(instrument="Thermo TRACE1310 GC–TSQ 9000 삼중사중극자 질량분석기, RSH Triplus 자동시료주입기", column="DB-WAX (60 m × 0.25 mm i.d. × 0.25 μm)",
  flow="헬륨 1 mL/min(정유량), split 1:5", temp="40 °C 10분 → 2 °C/min로 50 °C → 3 °C/min로 100 °C → 4 °C/min로 210 °C, 5분 유지",
  detection="EI 70 eV, m/z 30–500 전주사; Wiley/NIST 2008 라이브러리와 Kovats 지수로 동정", injection="SPME Arrow를 250 °C 주입구에서 5분 탈착",
  sample_prep="동결건조·드라이아이스 분쇄 시료 1 g을 20 mL 바이알에 넣고 50 °C 10분 평형 후 CWR/PDMS SPME Arrow를 30분 노출", recovery="재현성 RSD 평균 2.01–3.76%")
assays = [
 dict(role="literature", compound="Pectolinarigenin", compound_ko="펙톨리나리게닌", part="열수추출 동결건조물(부위 미기재)",
      content="고려엉겅퀴 단독 추출물 3.70 ± 0.07 mg/g; 같은 시료에서 펙톨리나린 불검출[4]", method="HPLC-UV", conditions=a1,
      rationale="펙톨리나린과 그 비당체 펙톨리나리게닌은 고려엉겅퀴의 주요 성분으로 보고되어 왔고, 이 연구는 두 성분을 함께 정량했다[4, 11]. PMC 전문 Methods에서 조건을 옮겼다[4].", source=[4], url=pmc("PMC6593477"), source_kind="paper"),
 dict(role="literature", compound="Pectolinarin", compound_ko="펙톨리나린", part="국내 엉겅퀴류(고려엉겅퀴 포함) 22개 배치",
      content="초록에 고려엉겅퀴의 함량 수치 없음[12]", method="HPLC-UV", conditions=a2,
      rationale="펙톨리나린 등 플라보노이드 6종을 국내 엉겅퀴류 품질관리 지표로 골라 동시 정량법을 세운 연구다[12]. 전문 확인 못함 — 조건은 초록에 나온 칸만 채웠다[12].", source=[12], url=pm(21547678), source_kind="paper"),
 dict(role="literature", compound="Chlorogenic acid", compound_ko="클로로젠산", part="건조 원료 열수추출 동결건조물(부위 미기재)",
      content="53.04 mg/100 g 추출물; 같은 분석에서 (−)-에피갈로카테킨 2376.00 mg/100 g 추출물, 총 페놀산 296.93·총 플라보노이드 3761.90 mg/100 g 추출물로 보고[3]", method="HPLC-DAD", conditions=a3,
      rationale="클로로젠산은 에탄올 추출물에서도 주성분으로 보고된 성분이다[3, 7]. 이 분석은 펙톨리나린·리나린을 표준품에 넣지 않았고, 카테킨류 값이 다른 고려엉겅퀴 연구에서 확인되지 않아 해석에 주의가 필요하다[3]. PMC 전문에서 조건을 옮겼다[3].", source=[3, 7], url=pmc("PMC6271068"), source_kind="paper"),
 dict(role="literature", compound="2-Pentylfuran", compound_ko="2-펜틸퓨란", part="동결건조 분말(강원도 시장 구입)",
      content="58종 휘발성 성분 중 최다 성분(피크 면적 비교, 절대 정량값 없음)[6]", method="HS-SPME Arrow GC-MS", conditions=a4,
      rationale="곤드레 특유의 향을 평가하는 지표 성분 후보로, 건조·저장 조건에 따라 함량이 변할 수 있다고 보고되었다[6]. PMC 전문 Methods에서 조건을 옮겼다[6].", source=[6], url=pmc("PMC7353593"), source_kind="paper"),
]

d = dict(slug="cirsium-setidens", name_ko="고려엉겅퀴", name_en="Gondre, Korean thistle",
  scientific_name="Cirsium setidens (Dunn) Nakai",
  aliases=["곤드레", "도깨비엉겅퀴", "고려엉겅퀴순", "고려엉겅퀴잎", "건조고려엉겅퀴", "냉동고려엉겅퀴", "절임고려엉겅퀴", "고려엉겅퀴분말", "고려엉겅퀴추출액", "Cirsium coreanum Nakai", "Saussurea setidens Dunn"],
  sections=sections, compounds=compounds, markers=[], nutrients=[], assays=assays, production=[], world=[], gi=[], orgs=[], sources=sources)
(P / "dossier.json").write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in sections: print(s["key"], len(s["body"]))
