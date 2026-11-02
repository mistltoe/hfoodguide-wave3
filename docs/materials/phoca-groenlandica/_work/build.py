import json, pathlib
A = "2026-11-02"
PM = "PubMed 초록, PubMed 도구로 열람"
PMC = "PubMed Central 전문, PubMed 도구로 열람"
src = [
 ("식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 하프물범(Phoca groenlandica, Harp seal): 하프물범(단, 하프물범신제외)·…유·…오일농축·…추출액 4행 (로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json)", "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "식품의약품안전처", "2026-10-13"),
 ("식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 대조 행: 바닷물범(고시형, 건강기능식품 C코드, Pagophilus groenlandicus), 물개·물개오일·냉동물개·해구신(Callorhinus ursinus, 사용불가) (로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json)", "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "식품의약품안전처", "2026-10-13"),
 ("식약처 고시 제2026-43호 「건강기능식품의 기준 및 규격」 제3. 2-16 EPA 및 DHA 함유 유지(제조기준·규격·최종제품의 요건·시험법) (로컬 원문 docs/refs/MFDS/건강기능식품의기준및규격_2026-43_제1~제3.txt)", "https://www.mfds.go.kr/brd/m_211/view.do?seq=14973", "식품의약품안전처", A),
 ("식약처 고시 「건강기능식품의 기준 및 규격」 제4. 시험방법 3-32 지방산(제1법~제3법)·2-6-1 아니시딘가 (고시 제2025-11호, 로컬 파싱본 docs/refs/MFDS/hf_methods.json)", "https://www.mfds.go.kr", "식품의약품안전처", A),
 ("식품의약품안전처 「식품 등의 생산실적」 2025년 — 건강기능식품 고시형 'EPA 및 DHA 함유 유지' (로컬 파싱본 docs/stats/hf_items.csv, 금액 천원 단위)", "https://www.mfds.go.kr", "식품의약품안전처", A),
 ("Carr SM et al. Quantitative phylogenomics of within-species mitogenome variation: ... harp seals (Pagophilus groenlandicus). PLoS One 2015;10(8):e0134207", "https://doi.org/10.1371/journal.pone.0134207", "PLoS One (" + PMC + ")", A),
 ("Tinker MT et al. Drivers of population dynamics and juvenile mortality in Northwest Atlantic harp seals. Ecol Appl 2026;36(1):e70184", "https://doi.org/10.1002/eap.70184", "Ecological Applications (" + PMC + ")", A),
 ("Reiling SJ et al. Toxoplasma gondii, Sarcocystis sp. and Neospora caninum-like parasites in seals from northern and eastern Canada: potential risk to consumers. Food Waterborne Parasitol 2019;17:e00067", "https://doi.org/10.1016/j.fawpar.2019.e00067", "Food and Waterborne Parasitology (" + PMC + ")", A),
 ("Zhang Y et al. Evaluation of the preservation and digestion of seal meat processed with heating and antioxidant seal meat hydrolysates. Mar Drugs 2022;20(3):204", "https://doi.org/10.3390/md20030204", "Marine Drugs (" + PMC + ")", A),
 ("Choi M et al. Effects of omega-3-rich harp seal oil on the production of pro-inflammatory cytokines in mouse peritoneal macrophages. Prev Nutr Food Sci 2015;20(2):83-7", "https://doi.org/10.3746/pnf.2015.20.2.83", "Preventive Nutrition and Food Science (" + PMC + ")", A),
 ("Pearson LE et al. To each its own: thermoregulatory strategy varies among neonatal polar phocids. Comp Biochem Physiol A 2014;178:59-67", "https://doi.org/10.1016/j.cbpa.2014.08.006", "Comparative Biochemistry and Physiology A (" + PM + ")", A),
 ("Gmuca NV et al. The fat and the furriest: morphological changes in harp seal fur with ontogeny. Physiol Biochem Zool 2015;88(2):158-66", "https://doi.org/10.1086/680080", "Physiological and Biochemical Zoology (" + PM + ")", A),
 ("Kirsch PE et al. Effect of a low-fat diet on body composition and blubber fatty acids of captive juvenile harp seals (Phoca groenlandica). Physiol Biochem Zool 2000;73(1):45-59", "https://doi.org/10.1086/316723", "Physiological and Biochemical Zoology (" + PM + ")", A),
 ("Lydersen C et al. Blood is a poor substrate for monitoring pollution burdens in phocid seals. Sci Total Environ 2002;292(3):193-203", "https://doi.org/10.1016/s0048-9697(01)01121-4", "Science of the Total Environment (" + PM + ")", A),
 ("Marshall HD et al. Molecular identification of prey in the stomach contents of harp seals (Pagophilus groenlandicus) using species-specific oligonucleotides. Mol Ecol Resour 2010;10(1):181-9", "https://doi.org/10.1111/j.1755-0998.2009.02713.x", "Molecular Ecology Resources (" + PM + ")", A),
 ("Fraser AJ et al. Modeling biomagnification and metabolism of contaminants in harp seals of the Barents Sea. Environ Toxicol Chem 2002;21(1):55-61", "https://pubmed.ncbi.nlm.nih.gov/11804061/", "Environmental Toxicology and Chemistry (" + PM + ")", A),
 ("How OJ, Nordøy ES. Seawater drinking restores water balance in dehydrated harp seals. J Comp Physiol B 2007;177(5):535-42", "https://doi.org/10.1007/s00360-007-0152-9", "Journal of Comparative Physiology B (" + PM + ")", A),
 ("Henden T et al. Endogenous glycogen prevents Ca2+ overload and hypercontracture in harp seal myocardial cells during simulated ischemia. J Mol Cell Cardiol 2004;37(1):43-50", "https://doi.org/10.1016/j.yjmcc.2004.03.013", "Journal of Molecular and Cellular Cardiology (" + PM + ")", A),
 ("Zitko V et al. Levels of organochlorine and polycyclic aromatic compounds in harp seal beaters (Phoca groenlandica). Sci Total Environ 1998;221(1):11-29", "https://doi.org/10.1016/s0048-9697(98)00159-4", "Science of the Total Environment (" + PM + ")", A),
 ("Kleivane L et al. Biological transport and mammal to mammal transfer of organochlorines in Arctic fauna. Mar Environ Res 2000;49(4):343-57", "https://doi.org/10.1016/s0141-1136(99)00079-3", "Marine Environmental Research (" + PM + ")", A),
 ("Ronald K et al. Pollutants in harp seals (Phoca groenlandica). I. Organochlorines. Sci Total Environ 1984;38:133-52", "https://doi.org/10.1016/0048-9697(84)90212-2", "Science of the Total Environment (" + PM + ")", A),
 ("Ronald K et al. Pollutants in harp seals (Phoca groenlandica). II. Heavy metals and selenium. Sci Total Environ 1984;38:153-66", "https://doi.org/10.1016/0048-9697(84)90213-4", "Science of the Total Environment (" + PM + ")", A),
 ("Agusa T et al. Accumulation of trace elements in harp seals (Phoca groenlandica) from Pangnirtung in the Baffin Island, Canada. Mar Pollut Bull 2011;63(5-12):489-99", "https://doi.org/10.1016/j.marpolbul.2011.02.022", "Marine Pollution Bulletin (" + PM + ")", A),
 ("Brunborg LA et al. Levels of non-essential elements in muscle from harp seal (Phagophilus groenlandicus) and hooded seal (Cystophora cristata) caught in the Greenland Sea area. Sci Total Environ 2006;366(2-3):784-98", "https://doi.org/10.1016/j.scitotenv.2005.10.020", "Science of the Total Environment (" + PM + ")", A),
 ("Chan HM et al. Levels of metals and persistent organic pollutants in traditional foods consumed by First Nations living on-reserve in Canada. Can J Public Health 2021;112(Suppl 1):81-96", "https://doi.org/10.17269/s41997-021-00495-7", "Canadian Journal of Public Health (" + PM + ")", A),
 ("Gouteux B et al. Comparison of toxaphene congeners levels in five seal species from eastern Canada. Environ Sci Technol 2005;39(6):1448-54", "https://doi.org/10.1021/es048886k", "Environmental Science & Technology (" + PM + ")", A),
 ("Frouin H et al. PBDEs in serum and blubber of harbor, grey and harp seal pups from Eastern Canada. Chemosphere 2011;82(5):663-9", "https://doi.org/10.1016/j.chemosphere.2010.11.007", "Chemosphere (" + PM + ")", A),
 ("Yang W et al. Attenuation of ciclosporin-induced nephrotoxicity by dietary supplementation of seal oil in Sprague-Dawley rats. J Pharm Pharmacol 2005;57(11):1485-92", "https://doi.org/10.1211/jpp.57.11.0015", "Journal of Pharmacy and Pharmacology (" + PM + ")", A),
 ("Wang Z et al. The effect of seal oil on paclitaxel induced cytotoxicity and apoptosis in breast carcinoma MCF-7 and MDA-MB-231 cell lines. Nutr Cancer 2007;58(2):230-8", "https://doi.org/10.1080/01635580701328818", "Nutrition and Cancer (" + PM + ")", A),
 ("Murphy MG et al. Diets enriched in menhaden fish oil, seal oil, or shark liver oil have distinct effects on the lipid and fatty-acid composition of guinea pig heart. Mol Cell Biochem 1997;177(1-2):257-69", "https://doi.org/10.1023/a:1006871524271", "Molecular and Cellular Biochemistry (" + PM + ")", A),
 ("Murphy MG et al. Dietary menhaden, seal, and corn oils differentially affect lipid and ex vivo eicosanoid and thiobarbituric acid-reactive substances generation in the guinea pig. Lipids 1999;34(2):115-24", "https://doi.org/10.1007/s11745-999-0344-1", "Lipids (" + PM + ")", A),
 ("Soulen BK et al. Factors affecting harp seal (Pagophilus groenlandicus) strandings in the Northwest Atlantic. PLoS One 2013;8(7):e68779", "https://doi.org/10.1371/journal.pone.0068779", "PLoS One (" + PM + ")", A),
 ("Bjørkkjær T et al. Short-term duodenal seal oil administration normalised n-6 to n-3 fatty acid ratio in rectal mucosa and ameliorated bodily pain in patients with inflammatory bowel disease. Lipids Health Dis 2006;5:6 (물범 종 명시 없음)", "https://doi.org/10.1186/1476-511X-5-6", "Lipids in Health and Disease (" + PMC + ")", A),
 ("Lewis EJH et al. Effect of omega-3 supplementation on neuropathy in type 1 diabetes: a 12-month pilot trial. Neurology 2017;88(24):2294-2301 (물범 종 명시 없음, 전문 본문은 열람되지 않아 초록만 확인)", "https://doi.org/10.1212/WNL.0000000000004033", "Neurology (" + PM + ")", A),
 ("Julshamn K, Grahl-Nielsen O. Trace element levels in harp seal (Pagophilus groenlandicus) and hooded seal (Cystophora cristata) from the Greenland Sea. A multivariate approach. Sci Total Environ 2000;250(1-3):123-33", "https://doi.org/10.1016/s0048-9697(00)00371-5", "Science of the Total Environment (" + PM + ")", A),
]
sources = [{"n": i+1, "title": t, "url": u, "publisher": p, "accessed": a} for i,(t,u,p,a) in enumerate(src)]

S = []
def sec(k, t, b): S.append({"key": k, "title": t, "body": b.strip()})

sec("overview", "한눈에 보기", """
하프물범은 북대서양과 북극해에 사는 물범과(Phocidae) 해양 포유류로, 식약처 「식품원료 목록」에는 학명 Phoca groenlandica, 영문명 Harp seal로 올라 있다[1]. 목록에는 '하프물범(단, 하프물범신제외)'과 그 뒤에 '유'·'오일농축'·'추출액'이 붙은 네 행이 식품원료(A코드)·축,수산물 외 동물·사용가능으로 실려 있다[1]. 네 행 모두 사용 조건 칸은 '단, 하프물범신제외'이고, 원자료 부위 칸은 '-'로 비어 있다[1]. 곧 하프물범 원료와 그 기름(유)·오일농축물·추출액을 식품원료로 쓸 수 있되 '하프물범신'은 빠진다[1]. '하프물범신'이 정확히 어느 부위를 뜻하는지는 목록에 정의가 없어 확인하지 못함.

같은 목록의 건강기능식품(C코드) 쪽에는 '바닷물범(고시형)' 행이 영문명 Pagophilus groenlandicus, 이명 '파고필루스 그로엔란디쿠스'로 기능성원료·사용가능으로 실려 있다[2]. 식약처 고시 「건강기능식품의 기준 및 규격」은 'EPA 및 DHA 함유 유지'의 원재료로 어류·조류(藻類)와 함께 바닷물범(Pagophilus groenlandicus)을 적고, 바닷물범 유래 원료는 EPA와 DHA의 합이 120 mg/g 이상이어야 한다고 정한다[3]. 학계에서는 이 종을 Pagophilus groenlandicus (Erxleben, 1777)로 부르고, 예전 논문에는 Phoca groenlandica라는 이름도 함께 쓰였다[6, 19, 24]. 곧 식품원료 목록의 하프물범과 고시의 바닷물범은 학명 표기만 다른 같은 종이다[2, 6].
""")

sec("history", "역사와 이용", """
캐나다 북부와 그린란드의 이누이트에게 물범 고기와 내장은 중요한 전통 식품이며, 캐나다 원주민은 수천 년 동안 물범의 근육·지방층·심장·간 등을 날것이나 덜 익힌 상태로도 먹어 왔다[8]. 북서대서양 하프물범은 대서양 캐나다에서 상업적으로 포획되며, 연간 포획 수는 1956년 307,000마리에서 2011년 40,000마리까지 달랐다[8]. 개체군 모형 연구는 1951–1982년에는 캐나다 상업 포획이 개체 수 변동의 가장 큰 요인이었고, 1983년 이후 포획 영향이 줄었다가 1996–2008년에 1960년대 이후 볼 수 없던 규모의 상업 포획이 다시 이뤄졌다고 정리했다[7].

하프물범 고기를 다룬 한 연구는 물범 고기가 오랫동안 기름 추출과 모피·가죽 생산의 부산물로 여겨져 비료·사료로 많이 쓰였고, 캐나다·그린란드·일본·노르웨이·아이슬란드·시베리아 등에서 식용된다고 적었다[9]. 캐나다 동부에서는 정부가 관리하는 상업 포획으로 얻은 물범 고기가 소매점과 식당에서 팔린다[8]. 국내에서는 캐나다 뉴펀들랜드산 하프물범유 제품을 오메가-3 원료로 쓴 연구가 2015년에 발표됐다[10]. 바닷물범이 건강기능식품 'EPA 및 DHA 함유 유지'의 원재료로 처음 고시된 시점은 확인하지 못함.
""")

sec("biology", "동물학적 특징", """
하프물범 새끼는 북극권에서 태어나는 물범 가운데 작은 편으로, 한 비교 연구에서 갓난 새끼의 몸무게는 9.8±0.7 kg이었다[11]. 갓난 새끼는 체온 유지(열 저항)의 약 82%를 배냇털(lanugo)에 의존하고, 갈색지방조직의 UCP1으로 떨지 않고 열을 낼 수 있다[11]. 새끼는 태어난 뒤 2주가 안 돼 갑자기 젖을 떼며, 다 자란 개체는 털보다 두꺼운 지방층(blubber)으로 몸을 보온한다[12].

사육한 어린 하프물범은 체지방이 몸무게의 38–49%였고, 지방이 적은 먹이로 바꾸자 30일 동안 체지방이 평균 32% 줄었으며 지방층의 지방산 조성도 먹이를 따라 바뀌었다[13]. 야생 성체 암컷은 번식 전 살찐 시기와 털갈이 시기 사이 몸무게 차이가 40 kg을 넘을 만큼 계절 변동이 크다[14]. 북서대서양 개체의 위 내용물에서는 대서양대구·북극대구·열빙어가 확인됐고, 바렌츠해 개체는 주로 북극대구와 단각류(Themisto libellula)를 먹는다[15, 16]. 탈수된 하프물범은 바닷물을 마셔 수분 균형을 되찾을 수 있고, 심장근육세포에는 쥐보다 약 10배 많은 글리코겐이 저장돼 산소가 부족할 때 버티는 데 쓰인다[17, 18].
""")

sec("related_species", "가까운 종·혼동", """
하프물범은 예전에 물범속(Phoca)에 넣어 Phoca groenlandica로 불렸으나 현재 문헌은 독립 속 Pagophilus로 쓰며, 같은 바다에 잔점박이물범(Phoca vitulina)·회색물범(Halichoerus grypus)·두건물범(Cystophora cristata)·고리무늬물범(Phoca hispida)이 함께 산다[6, 26, 27]. 이들 종은 먹이와 회유가 달라 오염물질 농도도 다르다: 캐나다 동부 조사에서 지방층의 톡사펜(ΣCHB)은 하프물범 370±87, 두건물범 680±310, 잔점박이물범 80±20, 회색물범 49±3.9, 고리무늬물범 18±7.6 ng/g 지방 무게였다[26]. 세인트로렌스만에서 태어난 새끼 가운데 PBDE는 하프물범이 가장 낮았다[27]. 그린란드해 조사에서는 간·신장의 원소 대부분이 두건물범에서 더 높았고 비소는 하프물범에서 더 높았다[35].

식품원료 목록에서 물개(Callorhinus ursinus)와 물개오일·냉동물개·해구신 행은 '사용불가'로, 사용가능인 하프물범과 지위가 다르다[1, 2]. 물개 행의 이명 칸에는 海狗腎·물개기름·물개유가 적혀 있으므로 '물개 기름'과 하프물범유를 섞어 쓰면 안 된다[2]. 학명 없이 'seal oil(물범유)'로만 적힌 사람 시험 자료는 어느 종의 기름인지 원문에 밝혀져 있지 않아 이 종의 근거로 옮기지 않았다[33, 34].
""")

sec("cultivation", "서식·포획", """
하프물범은 육지에 붙은 '정착빙' 위에서 새끼를 낳으며, 번식지는 백해, 그린란드해, 래브라도 앞바다(Front), 세인트로렌스만 남부 네 곳이다[6]. 개체군은 번식지에 따라 백해·바렌츠해, 그린란드해, 북서대서양 셋으로 나뉘고, 북서대서양 개체군은 여름을 캐나다 동부 북극과 그린란드 서부에서 보낸 뒤 겨울에 뉴펀들랜드 대륙붕과 세인트로렌스만으로 내려온다[7]. 야생에서 사냥으로 얻는 동물이며 양식·사육 생산은 확인하지 못함.

통합 개체군 모형에 따르면 북서대서양 개체 수는 1951년 240만, 1970년 150만(최저), 1997년 740만(최고), 2011년 490만, 2019년 550만 마리로 추정됐고, 2019년 새끼 생산은 846,000마리였다[7]. 다른 논문은 2019년 개체 수를 약 760만 마리로 인용해 추정치 사이에 차이가 있다[9]. 사람에 의한 제거는 캐나다 상업 포획, 캐나다 북극·그린란드의 자가소비 포획, 어구 혼획으로 나뉘며, 2000년 이후에는 해빙 이상에 따른 새끼 사망이 가장 강한 변동 요인 가운데 하나가 됐다[7]. 세인트로렌스만 해빙 면적이 적은 해에는 미국 동부 해안에 좌초하는 1년생 개체가 늘었다(R²=0.49)[32]. 국내 포획·생산은 없고, 수입량 통계는 확인하지 못함.
""")

sec("processing", "가공·제품·연구", """
고시는 바닷물범 등 원재료에서 가열·압착·헥산 또는 이산화탄소(초임계추출)로 유지를 추출해 여과하거나, 추출한 유지를 에스테르화해 'EPA 및 DHA 함유 유지'를 만들도록 정한다[3]. 규격은 EPA와 DHA의 합(원료성 제품 표시량 이상, 최종제품 표시량의 80~120%), 산가 3.0 이하, 과산화물가 5.0 이하, 아니시딘가 20.0 이하, 총산화가 26.0 이하, 납 3.0·카드뮴 1.0·수은 0.5 mg/kg 이하 등이고, EPA와 DHA는 제4. 3-32 지방산 시험법으로 잰다[3, 4]. 2025년 국내 'EPA 및 DHA 함유 유지' 생산량은 2,541 t, 판매액은 238,467,658천원(약 2,384.7억 원)이었으나, 이 가운데 바닷물범 유래 비중은 확인하지 못함[5].

국내 연구에 쓰인 캐나다산 하프물범유 제품은 공급처 자료 기준으로 총 오메가-3 23%, EPA 6.7%, DHA 10.3%, DPA 4.7%를 함유했다[10]. 하프물범 고기는 냉동·진공포장·통조림으로 보관하고 소시지·육포로도 가공한다[9]. 하프물범유의 효과는 생쥐 대식세포에서 염증성 사이토카인(TNF-α·IL-1β) 감소, 사람 유방암 세포주에서 파클리탁셀 세포독성 증강, 쥐에서 시클로스포린 신독성 완화, 기니피그에서 조직 n-3 지방산 증가처럼 세포·동물 수준에서만 보고됐다[10, 28, 29, 30, 31]. 이 종의 기름이라고 밝힌 사람 시험은 확인하지 못함.
""")

sec("genetics", "유전·종 판별", """
하프물범 53마리의 미토콘드리아 유전체 암호화 영역(15,825 bp)을 읽은 연구에서 모든 개체가 서로 다른 서열을 가졌고, 개체 사이 차이는 6~107개 치환이었다[6]. 종의 공통조상(coalescent)은 약 18만 년 전, 다양성의 66%를 차지하는 최근 계통은 4만~6만 년 전 빙하기 중반의 확장을 반영하는 것으로 추정됐다[6]. 집단 간 유전 분화(FST)는 백해와 그린란드해 또는 래브라도 앞바다 집단 사이에서만 유의했으며, 연구진은 백해·그린란드해·북서대서양의 세 번식 집단이 유전적으로 구별된다고 보았다[6].

미국 북동부 해안에서 좌초하거나 혼획된 하프물범을 10개 미세위성(microsatellite) 표지로 분석한 결과, 두 무리 사이 유전 다양성 지표(mean d²)에 차이가 없었다[32]. 위 내용물에서 먹이 종의 DNA를 종 특이 프라이머로 증폭해 먹이를 판별하는 방법도 하프물범에 적용됐다[15]. 물범유 제품이 실제 하프물범에서 왔는지 DNA로 가려내는 검사법은 확인하지 못함.
""")

sec("safety", "안전성", """
고시는 'EPA 및 DHA 함유 유지'를 먹을 때 (가) 의약품(항응고제, 항혈소판제, 혈압강하제 등) 복용 시 전문가와 상담할 것, (나) 개인에 따라 피부 관련 이상반응이 발생할 수 있음, (다) 이상사례 발생 시 섭취를 중단하고 전문가와 상담할 것을 주의사항으로 정한다[3]. 같은 고시는 납 3.0, 카드뮴 1.0, 수은 0.5 mg/kg 이하의 중금속 규격을 둔다[3].

하프물범의 유기염소 오염물질은 지방층에 가장 많이 쌓인다[21]. 생후 8개월 개체의 PCB(Aroclor 1254 환산)는 지방층에서 암컷 945, 수컷 890 ng/g 습중량, 근육에서 3.8, 8.2 ng/g 습중량이었다[19]. 바렌츠해 북부에서 잡힌 털갈이 중인 마른 개체의 지방층 ΣPCB는 평균 11,133 ng/g 지방 무게(범위 2,093–20,382)였다[20]. 수은은 주로 간, 카드뮴은 신장에 쌓이며, 캐나다 원주민 전통식품 조사에서는 하프물범 고기가 수은·메틸수은·PCB·p,p'-DDE 농도가 가장 높은 식품이었다[22, 23, 25]. 그린란드해 하프물범·두건물범 근육을 분석한 연구진은 측정 농도가 물범 고기를 식용하는 것을 막을 수준은 아니라고 결론지었다[24]. 이 값들은 조직 시료이며, 정제한 하프물범유의 오염물질 측정값은 확인하지 못함.

캐나다 하프물범 21마리 조직에서 톡소포자충 DNA가 57%, 사르코시스티스 DNA가 14% 검출돼, 연구진은 물범 고기와 내장을 충분히 익히거나 −10 °C 이하에서 3일 이상 얼려 먹을 것을 권했다[8]. 하프물범 알레르기에 관한 공공기관 정보는 확인하지 못함.
""")

compounds = [
 {"name":"Eicosapentaenoic acid","name_ko":"에이코사펜타엔산(EPA)","class":"지방산(n-3 장쇄 다중불포화)","role":"marker","part":"기름(물범유)","content_text":"6.7%(캐나다산 하프물범유 제품, 공급처 제시값)[10]; 고시: 바닷물범 유래 원료는 EPA+DHA 합 120 mg/g 이상[3]","activity_ko":"건강기능식품 'EPA 및 DHA 함유 유지'의 기능성분(혈중 중성지질·혈행·기억력·건조한 눈 개선, 사람 근거는 고시 기준)[3]","source":[3,10]},
 {"name":"Docosahexaenoic acid","name_ko":"도코사헥사엔산(DHA)","class":"지방산(n-3 장쇄 다중불포화)","role":"marker","part":"기름(물범유)","content_text":"10.3%(캐나다산 하프물범유 제품, 공급처 제시값)[10]","activity_ko":"EPA와 함께 고시 기능성분[3]","source":[3,10]},
 {"name":"Docosapentaenoic acid","name_ko":"도코사펜타엔산(DPA, 22:5 n-3)","class":"지방산(n-3 장쇄 다중불포화)","role":"bioactive","part":"기름(물범유)","content_text":"4.7%(캐나다산 하프물범유 제품, 공급처 제시값)[10]","activity_ko":"고시 지표성분에는 들지 않음; 하프물범유를 먹인 기니피그 심장 인지질에서 DPA 비율이 어유군보다 높았음(동물)[31]","source":[10,31]},
 {"name":"Omega-3 fatty acids","name_ko":"오메가-3 지방산 합계","class":"지방산군","role":"nutrient","part":"기름(물범유)","content_text":"23%(캐나다산 하프물범유 제품, 공급처 제시값)[10]","activity_ko":"하프물범유 식이 쥐의 적혈구막 n-3 지방산 10.79%(해바라기유 식이 1.67%)(동물)[28]","source":[10,28]},
 {"name":"Iron","name_ko":"철","class":"무기질","role":"nutrient","part":"고기(등심, 동결건조 후 모의 소화액)","content_text":"장 소화액 총 Fe 769.83 mg/kg(완충액, 25 °C)·781.99 mg/kg(가수분해물, 25 °C)·400.04 mg/kg(완충액, 100 °C)·486.02 mg/kg(가수분해물, 100 °C)[9]","activity_ko":"고온 처리 시 소화액 철 함량 감소[9]","source":[9]},
 {"name":"Zinc","name_ko":"아연","class":"무기질","role":"nutrient","part":"고기(모의 소화액)","content_text":"장 소화액 Zn 82.97–90.55 mg/kg(처리 조건별)[9]","activity_ko":"","source":[9]},
 {"name":"Magnesium","name_ko":"마그네슘","class":"무기질","role":"nutrient","part":"고기(모의 소화액)","content_text":"장 소화액 Mg 437.59–793.99 mg/kg(처리 조건별)[9]","activity_ko":"","source":[9]},
 {"name":"L-Lysine","name_ko":"라이신","class":"필수아미노산","role":"nutrient","part":"고기(모의 소화액)","content_text":"49.16 mg/g(가수분해물 처리·100 °C 장 소화액)[9]","activity_ko":"고기 소화액에 많은 필수아미노산[9]","source":[9]},
 {"name":"L-Leucine","name_ko":"류신","class":"필수아미노산","role":"nutrient","part":"고기(모의 소화액)","content_text":"50.17 mg/g(가수분해물 처리·100 °C 장 소화액)[9]","activity_ko":"","source":[9]},
 {"name":"Glutamic acid","name_ko":"글루탐산(Glx, 글루타민 포함)","class":"아미노산","role":"nutrient","part":"고기(모의 소화액)","content_text":"79.56 mg/g(가수분해물 처리·100 °C 장 소화액, Glu+Gln)[9]","activity_ko":"","source":[9]},
 {"name":"Selenium","name_ko":"셀레늄","class":"무기질","role":"nutrient","part":"근육·간·신장","content_text":"수치 확인하지 못함; 수은이 낮은 조직에서 셀레늄이 수은보다 몰 기준으로 많았음(하프물범·두건물범 합산 서술)[24]","activity_ko":"수은 독성 완화와 관련된다고 보는 원소[24]","source":[24]},
 {"name":"Glycogen","name_ko":"글리코겐","class":"다당류","role":"bioactive","part":"심장근육세포","content_text":"479±39 nmol glucose/mg 건중량(쥐 48±5)[18]","activity_ko":"저산소 상태에서 해당 작용으로 ATP 유지(세포 실험)[18]","source":[18]},
]

markers = [{
 "product":"EPA 및 DHA 함유 유지(바닷물범 유래)",
 "marker":"EPA와 DHA의 합",
 "spec":"원재료: 식용 가능한 어류 및 조류(藻類), 바닷물범(Pagophilus groenlandicus); 제조: 가열·압착·헥산 또는 이산화탄소(초임계추출)로 유지 추출 후 여과하거나 에스테르화; 바닷물범 유래 원료는 EPA와 DHA의 합 120 mg/g 이상(어류 180, 조류 300 mg/g 이상); 원료성 제품 표시량 이상, 최종제품 표시량의 80~120%; 잔류용매 5.0 mg/kg 이하(헥산 사용 시); 산가 3.0, 과산화물가 5.0, 아니시딘가 20.0, 총산화가 26.0 이하(적용 범위 제품); 납 3.0, 카드뮴 1.0, 수은 0.5 mg/kg 이하; 대장균군 음성[3]",
 "daily_intake":"혈중 중성지질 개선·혈행 개선: EPA와 DHA의 합으로서 0.5~2 g; 기억력 개선: 0.9~2 g; 건조한 눈 개선: 0.6~2.24 g[3]",
 "functions":["혈중 중성지질 개선","혈행 개선","기억력 개선","건조한 눈을 개선하여 눈 건강에 도움"],
 "note":"식약처 고시 제2026-43호 2-16. 섭취 시 주의: 의약품(항응고제, 항혈소판제, 혈압강하제 등) 복용 시 전문가 상담, 피부 관련 이상반응 가능, 이상사례 시 섭취 중단·상담[3]. card.json 의 lists 에는 KR_NOTICE 가 없으나 고시 원재료 칸에 이 종의 현 학명(Pagophilus groenlandicus)이 적혀 있어 넣었다[2, 3].",
 "source":[2,3]}]

E = {k:"" for k in ["instrument","column","mobile_phase","gradient","flow","temp","detection","injection","sample_prep","standard","linearity","lod","loq","recovery"]}
c2 = dict(E); c2.update({"instrument":"ICP-MS(Agilent 7700x)","sample_prep":"생 하프물범 등심을 다져 완충액 또는 고기 가수분해물에 25 °C·100 °C로 30분 처리, 동결건조 후 동적 쥐 위장 모형으로 소화한 장 소화액"})
assays = [
 {"role":"official","compound":"EPA + DHA","compound_ko":"EPA와 DHA의 합","part":"바닷물범 유래 유지","content":"바닷물범 유래 원료 120 mg/g 이상(제조기준)[3]","method":"「건강기능식품의 기준 및 규격」 제4. 3-32 지방산 시험법","conditions":dict(E),"rationale":"고시 2-16 EPA 및 DHA 함유 유지의 기능성분(지표성분)이며 시험법 칸이 제4. 3-32 지방산을 지정한다[3, 4]","source":[3,4],"url":"https://www.mfds.go.kr/brd/m_211/view.do?seq=14973","source_kind":"notice"},
 {"role":"literature","compound":"Iron, magnesium, zinc","compound_ko":"철·마그네슘·아연","part":"고기(등심) 모의 소화액","content":"장 소화액 Fe 400.04–781.99, Mg 437.59–793.99, Zn 82.97–90.55 mg/kg[9]","method":"ICP-MS","conditions":c2,"rationale":"하프물범 고기를 철 등 무기질 공급원으로 평가하려고 소화 뒤 남는 양을 정량했다; 칼럼·검출한계·회수율 등은 원문이 인용 문헌으로 넘겨 확인하지 못함[9]","source":[9],"url":"https://doi.org/10.3390/md20030204","source_kind":"paper"},
]

world = [
 {"country":"캐나다·그린란드(북서대서양 하프물범 개체군)","metric":"abundance_head","year":2019,"value":5500000,"unit":"마리","note":"통합 개체군 모형 추정(95% CI 450만–660만); 다른 문헌은 2019년 약 760만 마리로 인용[7, 9]","source":[7,9]},
 {"country":"캐나다·그린란드(북서대서양 하프물범 개체군)","metric":"pup_production_head","year":2019,"value":846000,"unit":"마리","note":"새끼 생산 추정(95% CI 572,000–1,141,000)[7]","source":[7]},
 {"country":"캐나다(대서양 캐나다 상업 포획)","metric":"harvest_head","year":2011,"value":40000,"unit":"마리","note":"연간 상업 포획 수, 1956년 307,000마리[8]","source":[8]},
]

d = {
 "slug":"phoca-groenlandica","name_ko":"하프물범","name_en":"Harp seal",
 "scientific_name":"Phoca groenlandica (식품원료 목록 학명; 현 학명 Pagophilus groenlandicus (Erxleben, 1777))",
 "aliases":["하프물범유","하프물범오일농축","하프물범추출액","바닷물범","파고필루스 그로엔란디쿠스","Pagophilus groenlandicus","harp seal oil"],
 "sections":S,"compounds":compounds,"markers":markers,"nutrients":[],"assays":assays,
 "production":[],"world":world,"gi":[],"orgs":[],"sources":sources}
p = pathlib.Path(__file__).resolve().parent.parent / "dossier.json"
p.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in S: print(s["key"], len(s["body"]))
print(len(sources))
