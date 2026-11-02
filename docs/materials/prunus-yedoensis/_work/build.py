import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
A = "2026-11-02"
def pm(n, title, pmid, pub, pmc=None):
    url = f"https://pmc.ncbi.nlm.nih.gov/articles/{pmc}/" if pmc else f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
    return {"n": n, "title": f"{title} (PMID {pmid})", "url": url, "publisher": pub + (" (PubMed Central)" if pmc else " (PubMed)"), "accessed": A}
I1020 = "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020"
sources = [
 {"n": 1, "title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 왕벚나무나무껍질·왕벚나무씨앗(Prunus yedoensis Matsumura / Cerasus yedoensis (Matsum.) Yu & Li.), 사용가능, '사용가능부위 : 나무껍질, 씨앗', 다른 이름 큰벚나무·참벚나무, 영문명 Korean flowering cherry", "url": I1020, "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
 {"n": 2, "title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 다른 벚나무류 행 대조: 벚나무꽃·벚나무열매(P. serrulata var. spontanea, 열매(씨앗 제외)·꽃), 산벚나무열매(P. sargentii), 올벚나무열매(P. pendula f. ascendens), 양벚나무열매(P. avium), 신양벚나무열매(P. cerasus)·신양벚나무줄기(제한적사용), 이스라지씨앗(사용불가), 라네시아나벚나무(P. lannesiana, 사용불가) (로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json)", "url": I1020, "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
 {"n": 3, "title": "식약처 고시 제2026-43호 「건강기능식품의 기준 및 규격」 제1~제3 원문 — 왕벚나무·앵피(櫻皮) 항목 검색(고시형 원료·별표에서 찾지 못함) (로컬 원문 docs/refs/MFDS/건강기능식품의기준및규격_2026-43_제1~제3.txt)", "url": "https://www.mfds.go.kr/brd/m_211/view.do?seq=14973", "publisher": "식품의약품안전처", "accessed": A},
 pm(4, "Vasorelaxant effect of Prunus yedoensis bark. BMC Complement Altern Med. 2013;13:31", "23410148", "BMC Complementary and Alternative Medicine", "PMC3585796"),
 pm(5, "The Anti-Inflammatory Effect of Prunus yedoensis Bark Extract on Adipose Tissue in Diet-Induced Obese Mice. Evid Based Complement Alternat Med. 2015;2015:937904", "26413130", "Evidence-based Complementary and Alternative Medicine", "PMC4568034"),
 pm(6, "Anti-inflammatory effect of Prunus yedoensis through inhibition of nuclear factor-κB in macrophages. BMC Complement Altern Med. 2013;13:92", "23631356", "BMC Complementary and Alternative Medicine", "PMC3659032"),
 pm(7, "Prunus yedoensis bark inhibits lipopolysaccharide-induced inflammatory cytokine synthesis by IκBα degradation and MAPK activation in macrophages. J Med Food. 2014;17(4)", "24720857", "Journal of Medicinal Food"),
 pm(8, "Wound Healing Effects of Prunus yedoensis Matsumura Bark in Scalded Rats. Evid Based Complement Alternat Med. 2017;2017:7812598", "28400845", "Evidence-based Complementary and Alternative Medicine"),
 pm(9, "Prunus yedoensis Bark Downregulates the Expression of Cell Adhesion Molecules in Human Endothelial Cell Lines and Relaxes Blood Vessels in Rat Aortic Rings. Pharmaceuticals (Basel). 2024;17(7):926", "39065776", "Pharmaceuticals", "PMC11279544"),
 pm(10, "Prunetin Relaxed Isolated Rat Aortic Rings by Blocking Calcium Channels. Molecules. 2018;23(9):2372", "30227625", "Molecules"),
 pm(11, "Anti-inflammatory effect of prunetin via the suppression of NF-κB pathway. Food Chem Toxicol. 2013", "23597450", "Food and Chemical Toxicology"),
 pm(12, "Sakuranetin as a Potential Regulator of Blood Pressure in Spontaneously Hypertensive Rats by Promoting Vasorelaxation through Calcium Channel Blockade. Biomedicines. 2024;12(2):346", "38397948", "Biomedicines"),
 pm(13, "Prunus yedoensis bark extract containing naringenin enhances hyaluronic acid synthesis and epidermal barrier function via MAPK/CREB and Akt/NF-κB pathways. Int J Biol Macromol. 2025", "41360252", "International Journal of Biological Macromolecules"),
 pm(14, "Prunus yedoensis Matsum. stimulates glucose uptake in L6 rat skeletal muscle cells by activating AMP-activated protein kinase and phosphatidylinositol 3-kinase/Akt pathways. Nat Prod Res. 2011", "21809954", "Natural Product Research"),
 pm(15, "Study of the chemical constituents of Pruni Cortex and its related parts. J Nat Med. 2010", "20577825", "Journal of Natural Medicines"),
 pm(16, "Draft genome sequence of wild Prunus yedoensis reveals massive inter-specific hybridization between sympatric flowering cherries. Genome Biol. 2018;19:127", "30180884", "Genome Biology"),
 pm(17, "Molecular and morphological data reveal hybrid origin of wild Prunus yedoensis (Rosaceae) from Jeju Island, Korea: implications for the origin of the flowering cherry. Am J Bot. 2014", "25366862", "American Journal of Botany"),
 pm(18, "Multiple Lines of Evidence for Independent Origin of Wild and Cultivated Flowering Cherry (Prunus yedoensis). Front Plant Sci. 2019;10:1555", "31921231", "Frontiers in Plant Science", "PMC6930925"),
 pm(19, "Phased genome sequence of an interspecific hybrid flowering cherry, 'Somei-Yoshino' (Cerasus × yedoensis). DNA Res. 2019;26(5)", "31334758", "DNA Research", "PMC6796508"),
 pm(20, "DNA fingerprinting study on the intraspecific variation and the origin of Prunus yedoensis (Someiyoshino). Idengaku Zasshi. 1995;70(2):185-96", "7605671", "Japanese Journal of Genetics"),
 pm(21, "Propagation path of a flowering cherry (Cerasus × yedoensis) cultivar 'Somei-Yoshino' traced by somatic mutations. DNA Res. 2024;31(5)", "39115130", "DNA Research", "PMC11369696"),
 pm(22, "Complete chloroplast genome of Prunus yedoensis Matsum. (Rosaceae), wild and endemic flowering cherry on Jeju Island, Korea. Mitochondrial DNA A. 2016", "26329800", "Mitochondrial DNA Part A"),
 pm(23, "Botany and national identities: The Tokyo Cherry. Sci Context. 2022;35(3):252-271", "38372156", "Science in Context"),
 pm(24, "Predicting the timing of cherry blossoms in Washington, DC and Mid-Atlantic States in response to climate change. PLoS One. 2011;6(11):e27439", "22087317", "PLoS One", "PMC3210174"),
 pm(25, "Influence of air temperature on the first flowering date of Prunus yedoensis Matsum. Ecol Evol. 2014;4(2)", "24558585", "Ecology and Evolution", "PMC3925431"),
 pm(26, "Impact of urbanization on spring and autumn phenology of deciduous trees in the Seoul Capital Area, South Korea. Int J Biometeorol. 2018", "30267322", "International Journal of Biometeorology"),
 pm(27, "Comparison of the Ecological Traits and Boring Densities of Aromia bungii in Two Host Tree Species. Insects. 2022;13(2):151", "35206724", "Insects", "PMC8877986"),
 pm(28, "Transition of phenolics and cyanogenic glycosides from apricot and cherry fruit kernels into liqueur. Food Chem. 2016;203:483-490", "26948641", "Food Chemistry"),
 pm(29, "Optimization of ultrasonic-assisted extraction of anthocyanins from Prunus yedoensis fruit and evaluation of antioxidant and anti-inflammatory activity. Food Sci Biotechnol. 2025", "40196335", "Food Science and Biotechnology", "PMC11972253"),
 pm(30, "Isolation of ethyl caffeate from the petals of Prunus yedoensis. J Nat Med. 2006", "29435877", "Journal of Natural Medicines"),
 pm(31, "The anti-inflammatory effect of cherry blossom extract (Prunus yedoensis) used in soothing skincare product. Int J Cosmet Sci. 2014", "25065693", "International Journal of Cosmetic Science"),
 pm(32, "Regulatory stability of pentatricopeptide repeat genes in a natural hybrid genome of wild Prunus yedoensis. Plant Sci. 2026", "42248469", "Plant Science"),
]

S = {}
S["overview"] = ("왕벚나무(Prunus yedoensis Matsum.; 이명 Cerasus yedoensis)는 장미과 벚나무속(벚나무아속)의 낙엽 교목으로, 한국·일본에서 가장 널리 알려진 꽃벚나무 무리다[1][16][17]. "
 "식품의약품안전처 「식품원료 목록」에는 '왕벚나무나무껍질'과 '왕벚나무씨앗' 두 원료명이 사용가능 원료로 올라 있고, 사용 조건은 '사용가능부위 : 나무껍질, 씨앗'이다[1]. "
 "같은 목록의 다른 이름은 큰벚나무·참벚나무, 영문명은 Korean flowering cherry로 적혀 있다[1]. "
 "열매·꽃·잎은 이 원료의 사용가능부위에 들어 있지 않으며, 다른 벚나무류(벚나무·산벚나무·양벚나무 등) 원료는 대부분 '열매(씨앗 제외)'만 쓸 수 있게 되어 있어 부위 조건이 다르다[1][2]. "
 "건강기능식품 고시형 원료나 그 원재료로 왕벚나무가 오른 기록은 확인하지 못함[3].\n\n"
 "나무껍질은 한국·일본에서 앵피(櫻皮, Yaeng-Pi)라는 약재로 기침과 피부 염증에 써 왔다고 논문들이 적고 있다[4][7]. "
 "나무껍질 추출물에서는 이소플라본 프루네틴과 플라바논 사쿠라네틴·나린게닌 등이 정량·검출되었고, 연구는 대부분 세포와 동물 실험이다[5][7][13]. "
 "사람을 대상으로 왕벚나무 껍질이나 씨앗을 먹게 한 임상시험은 확인하지 못함. "
 "왕벚나무라는 이름은 제주 한라산의 자생 집단과 일본에서 퍼진 재배품종 '소메이요시노'에 함께 쓰여 왔으며, 두 집단의 관계는 유전체 연구로 다시 정리되는 중이다[16][18][19].")
S["history"] = ("왕벚나무 나무껍질은 한국과 일본에서 '앵피(Yaeng-Pi)' 또는 '화피(Hua-Pi)'라는 이름의 전통 약재로 쓰였다고 보고되었다[4]. "
 "한의학에서는 앵피(Pruni Cortex)를 천식·홍역·기침·두드러기·가려움·피부염에 써 왔고, 일본에서는 기침을 멎게 하고 가래를 삭이는 약으로 쓴다고 논문에 적혀 있다[5][8]. "
 "다만 일본에서 쓰는 Pruni Cortex의 기원은 산벚나무 계열인 P. jamasakura의 껍질로 보고되어, 앵피가 언제나 왕벚나무 껍질만을 뜻하는 것은 아니다[15]. "
 "한국에서는 나무껍질이 만성 피부 염증에 쓰는 복합 처방(십미패독산)의 구성 약재로 소개된다[5].\n\n"
 "과학사 연구에 따르면 재배 벚나무 '소메이요시노'는 일본이 근대 국가 정체성을 만드는 과정에서 나라꽃처럼 다루어졌고, 정원 식물인데도 고유종처럼 라틴어 학명을 받았다[23]. "
 "같은 연구는 일제강점기 한라산에서 발견된 야생 벚나무가 소메이요시노의 원산이라는 주장으로 이어졌고, 해방 뒤 한국에서 이 야생 벚나무가 '왕벚나무'로 불리며 정체성 논쟁과 얽혔다고 정리한다[23]. "
 "미국 워싱턴 D.C. 타이들 베이슨의 벚꽃도 'Yoshino'(P. × yedoensis) 품종이 중심이며, 개화 시기는 기후 변화 지표로 연구된다[24].")
S["biology"] = ("왕벚나무는 장미과(Rosaceae) 벚나무속의 낙엽 교목으로, 식품원료 목록에는 학명 Prunus yedoensis Matsumura와 Cerasus yedoensis (Matsum.) Yu & Li.가 함께 적혀 있다[1]. "
 "제주 한라산의 야생 왕벚나무는 올벚나무 계열(P. spachiana f. ascendens, P. pendula f. ascendens)을 모계로 하는 자연 잡종으로 밝혀졌다[16][17]. "
 "이른 봄에 꽃이 피며, 중국 우한에서 1951–2012년 관측한 첫 개화일은 2월 7일부터 쌓인 기온(기준온도 -1.2°C)으로 가장 잘 설명되었다[25]. "
 "서울 수도권 9개 관측소의 1991–2010년 자료에서는 인구 밀도가 높은 도시일수록 왕벚나무를 포함한 봄 꽃나무의 싹 트는 시기가 빨라졌다[26]. "
 "소메이요시노는 스스로 꽃가루받이가 되지 않는(자가불화합) 잡종이어서 씨로 번식하지 않고 접붙이기로 퍼졌다[21]. "
 "열매에 안토시아닌이 많다는 추출 연구가 있으나 열매는 식품원료 목록의 사용가능부위가 아니다[1][29]. "
 "잎 추출물은 쥐 근육세포(L6)에서 포도당 흡수를 늘렸다는 세포 실험이 있으나, 잎도 사용가능부위에 들어 있지 않다[1][14]. "
 "꽃잎에서는 에틸 카페에이트가 분리되었다[30].")
S["related_species"] = ("왕벚나무 자료를 읽을 때는 이름이 비슷한 세 가지를 구분해야 한다[16][18]. "
 "첫째는 제주 한라산에 자라는 야생 왕벚나무이고, 둘째는 일본에서 퍼져 한국·일본의 가로수로 많이 심긴 재배품종 '소메이요시노'(Cerasus × yedoensis 'Somei-yoshino')다[18][19]. "
 "유전체 연구는 야생 왕벚나무가 올벚나무(모계)와 산벚나무 계열 P. jamasakura(부계)의 F1 잡종이며 소메이요시노와 뚜렷이 구별된다고 보고했다[16]. "
 "다른 연구는 소메이요시노가 재배 올벚나무(모계)와 일본 이즈 제도 고유종 오시마벚나무(P. speciosa, 부계)의 한 차례 인공 교잡에서 생겼다고 보았고, 일본 각지의 소메이요시노가 한 그루에서 영양번식으로 퍼졌다는 DNA 지문 결과도 있다[18][19][20]. "
 "셋째로 일본의 앵피(Pruni Cortex)는 P. jamasakura 껍질에서 얻으며 사쿠라닌·네오사쿠라닌이 주성분이라는 보고가 있어, 왕벚나무 껍질 자료와 섞으면 안 된다[15].\n\n"
 "식품원료 목록에서 같은 속의 벚나무류는 원료마다 부위 조건이 다르다[2]. "
 "벚나무(P. serrulata var. spontanea)는 열매(씨앗 제외)와 꽃, 산벚나무·올벚나무·양벚나무(P. avium)는 열매(씨앗 제외)만 쓸 수 있고, 이스라지씨앗과 라네시아나벚나무는 사용불가, 신양벚나무(P. cerasus) 줄기는 제한적사용이다[2]. "
 "매실(P. mume)·아몬드(P. dulcis)·자두·살구 등 같은 속의 다른 식품원료 성분 자료는 이 문서에 쓰지 않았다[1][2].")
S["cultivation"] = ("왕벚나무는 한국·일본·미국 등에서 가로수와 공원수로 널리 심겨 있으며, 개화 시기는 기후 변화 연구의 지표로 쓰인다[24][25][26]. "
 "워싱턴 D.C. 타이들 베이슨의 'Yoshino' 만개일은 중간 배출 시나리오에서 2050년대에 평균 5일, 2080년대에 10일 빨라질 것으로 예측되었다[24]. "
 "소메이요시노는 접붙이기로 번식하는 하나의 클론이라, 일본 46개 도도부현의 68그루가 DNA 지문에서 모두 같은 띠 양상을 보였다[20]. "
 "가로수로 심긴 소메이요시노는 하늘소류 해충(Aromia bungii)의 피해를 받는 것으로 일본에서 보고되었다[27].\n\n"
 "식품원료로서 나무껍질·씨앗의 국내 생산·유통량 통계는 확인하지 못함. "
 "통계청 농작물생산조사와 농림축산식품부 특용작물 생산실적 파싱본에서도 왕벚나무 품목은 확인하지 못함. "
 "논문에 쓰인 나무껍질은 국내 한약재 업체에서 산 건조 약재였다[5][9].")
S["processing"] = ("연구에 쓰인 왕벚나무 껍질은 말린 약재를 물·에탄올·메탄올로 추출해 농축·동결건조한 형태가 대부분이다[5][6][9]. "
 "한 연구는 말린 껍질을 물(120°C, 4시간), 30% 에탄올과 70% 에탄올(95°C 환류, 4시간)로 각각 추출했고, 30% 에탄올 추출물이 혈관 내피세포 실험에서 가장 효과가 컸다[9]. "
 "다른 연구는 분쇄한 껍질 0.4 kg을 80% 에탄올로 2시간씩 두 번 환류 추출하고 클로로폼·에틸아세테이트·물로 나누었으며, 분획 수율은 각각 2.5%, 48%, 43%였다[5]. "
 "메탄올 추출물 3 kg 규모의 분획에서는 클로로폼 3.5 g, 에틸아세테이트 40 g, 물 36.2 g이 얻어졌다[6].\n\n"
 "꽃 추출물은 진정용 화장품 원료로 연구되었으며, 3% 꽃 추출물 크림은 사람 40명의 피부 자극 시험에서 위약보다 붉은기 점수가 낮았다[31]. "
 "다만 꽃은 식품원료 목록의 사용가능부위가 아니므로 먹는 용도와는 구별해야 한다[1][31]. "
 "씨앗을 식품으로 가공하는 방법이나 국내 제품 생산실적은 확인하지 못함.")
S["genetics"] = ("제주 야생 왕벚나무의 엽록체 유전체는 157,786 bp, GC 함량 36.7%이며 131개 유전자를 담고 있다[22]. "
 "장염기 서열로 해독한 야생 왕벚나무 초안 유전체는 유전자 영역의 93% 이상을 덮고 단백질 암호 유전자 41,294개가 예측되었다[16]. "
 "이 유전체를 근연 6개 분류군 16개 시료와 비교한 결과 유전자의 41%가 모계 또는 부계로 나뉘었고, 야생 왕벚나무는 올벚나무 모계·P. jamasakura 부계의 F1 잡종으로 판단되었다[16]. "
 "핵 ITS/ETS와 엽록체 7개 구간 분석도 야생 왕벚나무의 잡종 기원과 올벚나무 계열 모계를 지지했으나, 부계는 벚나무·산벚나무 무리 안에서 정하지 못했다[17].\n\n"
 "소메이요시노의 두 반수체를 나눈 유전체는 690.1 Mb, 고신뢰 유전자 95,076개로 보고되었다[19]. "
 "4종의 분자 표지를 쓴 연구는 야생 왕벚나무와 소메이요시노가 서로 다른 과정을 거쳐 생긴 별개의 분류군이라고 결론지었다[18]. "
 "소메이요시노 46그루의 유전체에서는 체세포 돌연변이 684개가 찾아졌고, 도쿄 우에노 공원의 한 그루가 원래 나무에 가장 가깝다고 추정되었다[21]. "
 "야생 왕벚나무의 PPR 유전자 992개는 모계·부계 기원과 관계없이 비슷하게 발현되었다[32].")
S["safety"] = ("왕벚나무 나무껍질과 씨앗은 식품원료 목록에서 사용가능 원료이며, 목록에 별도의 섭취 주의 문구는 적혀 있지 않다[1]. "
 "건강기능식품 고시의 섭취 시 주의사항이나 공공기관의 왕벚나무 섭취 안전성 평가는 확인하지 못함[3]. "
 "왕벚나무 껍질 추출물의 클로로폼 분획에는 시안 배당체인 아미그달린이 들어 있다고 보고되었다[7]. "
 "왕벚나무 씨앗의 시안 배당체(아미그달린·프루나신) 함량을 정량한 자료는 확인하지 못함. "
 "다른 벚나무(체리) 씨앗과 그 씨앗으로 담근 술에서는 시안 배당체가 정량되었고, 술에도 상당량(체리 술 1 mL당 16.08 μg)이 남았다[28]. "
 "같은 목록에서 다른 벚나무류 원료 다수는 '씨앗 제외' 조건이 붙어 있고 이스라지씨앗은 사용불가여서, 씨앗 원료는 부위 조건을 확인해 써야 한다[1][2].\n\n"
 "독성 자료로는 껍질 추출물을 생쥐에 하루 100 mg/kg씩 17주 먹인 실험과 고혈압 쥐에 최대 1000 mg/kg을 한 번 먹인 실험이 있으나, 독성 평가를 목적으로 한 연구는 아니다[5][9]. "
 "껍질 추출물의 클로로폼 분획은 다른 분획보다 세포 독성이 커서 10분의 1 농도로 시험해야 했다[5]. "
 "혈관 실험 논문도 안전성·안정성 분석과 지표성분 독성 평가가 더 필요하다고 적었다[9].")

titles = {"overview":"한눈에 보기","history":"역사와 전통적 이용","biology":"식물학적 특징","related_species":"가까운 종과 혼동","cultivation":"재배와 생산","processing":"가공과 이용","genetics":"유전체와 기원 연구","safety":"안전성과 주의"}
sections = [{"key": k, "title": titles[k], "body": S[k]} for k in titles]

compounds = [
 {"name": "Prunetin", "name_ko": "프루네틴", "class": "O-메틸 이소플라본", "role": "marker", "part": "나무껍질(80% 에탄올 추출물의 클로로폼 분획)",
  "content_text": "클로로폼 분획 건조중량 100 mg당 16.81 ± 0.5 mg; 추출물 건조중량의 0.42%로 환산[5]",
  "activity_ko": "쥐 대동맥 고리 이완(1–30 μg/mL), 고혈압 쥐 25 mg/kg 투여 시 수축기 혈압 감소(동물)[10]; 대식세포·LPS 생쥐에서 염증 지표 감소(세포·동물)[11]", "source": [5, 10, 11]},
 {"name": "Sakuranetin", "name_ko": "사쿠라네틴", "class": "플라바논", "role": "marker", "part": "나무껍질(클로로폼 분획)",
  "content_text": "클로로폼 분획 건조중량 100 mg당 9.08 ± 0.4 mg[5]",
  "activity_ko": "고혈압 쥐에 20·50 mg/kg 투여 4시간 뒤 혈압 감소(성분 단독 투여, 동물)[12]", "source": [5, 12]},
 {"name": "Genistein", "name_ko": "제니스테인", "class": "이소플라본", "role": "bioactive", "part": "나무껍질(클로로폼 분획)",
  "content_text": "클로로폼 분획 건조중량 100 mg당 3.29 ± 0.4 mg[5]",
  "activity_ko": "껍질 추출물 품질 관리용 3개 성분의 하나로 정량[5]", "source": [5]},
 {"name": "Naringenin", "name_ko": "나린게닌", "class": "플라바논", "role": "bioactive", "part": "나무껍질(에탄올 추출물)",
  "content_text": "주요 활성 성분으로 보고(함량 확인하지 못함)[13]; 클로로폼 분획에서 검출[7]",
  "activity_ko": "사람 각질형성세포(HaCaT)에서 히알루론산 합성 효소(HAS2) 증가(세포)[13]", "source": [7, 13]},
 {"name": "Amygdalin", "name_ko": "아미그달린", "class": "시안 배당체", "role": "bioactive", "part": "나무껍질(클로로폼 분획); 씨앗 함량은 확인하지 못함",
  "content_text": "나무껍질 클로로폼 분획에서 검출(함량 확인하지 못함)[7]",
  "activity_ko": "분해되면 시안화수소를 내는 시안 배당체로, 다른 벚나무 씨앗에서도 정량됨[28]", "source": [7, 28]},
 {"name": "Prunetin 5-O-beta-D-glucopyranoside", "name_ko": "프루네틴 5-O-글루코사이드", "class": "이소플라본 배당체", "role": "marker", "part": "나무껍질(메탄올 추출물·에틸아세테이트 분획)",
  "content_text": "HPLC 머무름 시간 12.69분, 추출물 특성 확인 지표(함량 확인하지 못함)[6]",
  "activity_ko": "추출물 특성 확인용 지표 3종의 하나[6]", "source": [6]},
 {"name": "Genistin", "name_ko": "제니스틴(제니스테인 7-O-글루코사이드)", "class": "이소플라본 배당체", "role": "marker", "part": "나무껍질(메탄올 추출물)",
  "content_text": "HPLC 머무름 시간 9.60분(함량 확인하지 못함)[6]",
  "activity_ko": "추출물 특성 확인용 지표 3종의 하나[6]", "source": [6]},
 {"name": "4'-Hydroxytectochrysin 5-O-beta-D-glucopyranoside", "name_ko": "4′-하이드록시텍토크리신 5-O-글루코사이드", "class": "플라본 배당체", "role": "marker", "part": "나무껍질(메탄올 추출물)",
  "content_text": "4′-hydroxy-tectochrysin-5-O-β-glucopyranoside, HPLC 머무름 시간 11.82분(함량 확인하지 못함)[6]",
  "activity_ko": "추출물 특성 확인용 지표 3종의 하나[6]", "source": [6]},
 {"name": "Ethyl caffeate", "name_ko": "에틸 카페에이트", "class": "페닐프로파노이드(카페산 에스터)", "role": "bioactive", "part": "꽃잎(식품 사용가능부위 아님)",
  "content_text": "꽃잎에서 분리(벚나무속 첫 보고, 함량 확인하지 못함)[30]",
  "activity_ko": "확인하지 못함", "source": [30]},
]

assays = [
 {"role": "literature", "compound": "Prunetin", "compound_ko": "프루네틴·사쿠라네틴·제니스테인", "part": "나무껍질(80% 에탄올 추출물의 클로로폼 분획)",
  "content": "클로로폼 분획 100 mg당 프루네틴 16.81 ± 0.5 mg, 사쿠라네틴 9.08 ± 0.4 mg, 제니스테인 3.29 ± 0.4 mg; 프루네틴은 추출물 건조중량의 0.42%[5]",
  "method": "HPLC-UV(역상)",
  "conditions": {"instrument": "Shimadzu 역상 HPLC", "column": "Agilent Zorbax Eclipse XDB-C18(5 μm, 4.6 × 250 mm)",
   "mobile_phase": "A 0.1% 포름산, B 아세토니트릴", "gradient": "0분 20% B → 60분 30% B → 70분 60% B → 100분 70% B(선형), 분석 110분",
   "flow": "0.5 mL/min", "temp": "실온", "detection": "UV 280 nm", "injection": "10 μL", "sample_prep": "분쇄 껍질 0.4 kg을 80% 에탄올로 2시간씩 2회 환류 추출 → 동결건조 → 추출물 1 g을 클로로폼·에틸아세테이트·물로 분획(수율 2.5%, 48%, 43%)",
   "standard": "프루네틴·제니스테인·사쿠라네틴 표준품(Sigma)", "linearity": "r = 0.9999(3성분 모두)", "lod": "", "loq": "", "recovery": ""},
  "rationale": "연구진이 껍질 추출물 품질 관리용으로 사쿠라네틴·프루네틴·제니스테인을 골라 정량했다; 세 성분은 클로로폼 분획에서만 검출되고 전체 추출물에서는 검출되지 않았다[5]. 본문은 추출물 기준 비율을 프루네틴 0.42%, 제니스테인 0.22%, 사쿠라네틴 0.08%로 적었으나 분획 수율(2.5%)로 다시 계산하면 제니스테인과 사쿠라네틴 값이 서로 바뀐 것으로 보여 프루네틴 값만 옮겼다[5].",
  "source": [5], "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC4568034/", "source_kind": "paper"},
 {"role": "literature", "compound": "Prunetin 5-O-beta-D-glucopyranoside", "compound_ko": "프루네틴 5-O-글루코사이드·4′-하이드록시텍토크리신 5-O-글루코사이드·제니스틴", "part": "나무껍질(메탄올 추출물·에틸아세테이트 분획)",
  "content": "정성 비교만 함(함량 수치 없음); 머무름 시간 12.69·11.82·9.60분[6]",
  "method": "HPLC-UV",
  "conditions": {"instrument": "Gilson HPLC(234 자동시료주입기, UV/VIS-155 검출기, 321 펌프)", "column": "Phenomenex Luna C18(5 μm, 4.60 × 250 mm)",
   "mobile_phase": "아세토니트릴과 물(0.01% 포름산)", "gradient": "0–20분 아세토니트릴 20% → 40%, 20–30분 40%", "flow": "1.0 mL/min", "temp": "실온",
   "detection": "UV 245 nm(방법 기술) — 그림 설명에는 254 nm로 적혀 있음", "injection": "10 μL",
   "sample_prep": "건조 메탄올 추출물·에틸아세테이트 분획 1 mg을 50% 아세토니트릴 2 mL에 녹여 0.45 μm PVDF 여과", "standard": "세 배당체 표준품", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "연구진은 껍질 추출물을 이 세 배당체로 특성화했으며, 메탄올 추출물과 에틸아세테이트 분획의 크로마토그램이 비슷했다[6]. 정량값·검량선은 보고되지 않았다[6].",
  "source": [6], "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC3659032/", "source_kind": "paper"},
]

d = {"slug": "prunus-yedoensis", "name_ko": "왕벚나무", "name_en": "Korean flowering cherry (Yoshino cherry)",
 "scientific_name": "Prunus yedoensis Matsum.",
 "aliases": ["왕벚나무나무껍질", "왕벚나무씨앗", "큰벚나무", "참벚나무", "앵피", "Korean flowering cherry", "Yoshino cherry", "Cerasus yedoensis (Matsum.) Yu & Li.", "Prunus × yedoensis", "Somei-yoshino"],
 "sections": sections, "compounds": compounds, "markers": [], "assays": assays, "nutrients": [], "production": [], "world": [], "gi": [], "orgs": [], "sources": sources}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in sections: print(s["key"], len(s["body"]))
