import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
A = "2026-11-02"
def pm(p): return f"https://pubmed.ncbi.nlm.nih.gov/{p}/"
def pmc(p): return f"https://pmc.ncbi.nlm.nih.gov/articles/{p}/"
S = [
 ("식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 들갓잎(Sinapis arvensis L., Charlock, 식품원료 A코드) 행 및 같은 목록의 White mustard(Sinapis alba)·갓(Brassica juncea / Sinapis juncea)·Black mustard(Brassica nigra / Sinapis nigra) 행", "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "식품의약품안전처", "2026-10-13"),
 ("Oviposition Preference for Young Plants by the Large Cabbage Butterfly (Pieris brassicae) Does not Strongly Correlate with Caterpillar Performance. J Chem Ecol 2017;43(6) (PMID 28620771, doi:10.1007/s10886-017-0853-9)", pmc("PMC5501907"), "Journal of Chemical Ecology (PMC)", A),
 ("Sinapis phylogeny and evolution of glucosinolates and specific nitrile degrading enzymes. Phytochemistry 2008;69(17):2937-49 (PMID 18995873, doi:10.1016/j.phytochem.2008.08.014)", pm(18995873), "Phytochemistry (PubMed)", A),
 ("Host plant-dependent metabolism of 4-hydroxybenzylglucosinolate in Pieris rapae: substrate specificity and effects of genetic modification and plant nitrile hydratase. Insect Biochem Mol Biol 2007;37(11):1119-30 (PMID 17916498, doi:10.1016/j.ibmb.2007.06.009)", pm(17916498), "Insect Biochemistry and Molecular Biology (PubMed)", A),
 ("Possible Acute Poisoning by Sinapis arvensis in Sheep: Clinical, Laboratory and Necropsy Findings. Arch Razi Inst 2021;76(3):699-706 (PMID 34824762, doi:10.22092/ari.2020.351494.1525)", pmc("PMC8605835"), "Archives of Razi Institute (PMC)", A),
 ("Production of biodiesel from non-edible feedstocks using environment friendly nano-magnetic Fe/SnO catalyst. Sci Rep 2022;12 (PMID 36202925, doi:10.1038/s41598-022-20856-7)", pmc("PMC9537295"), "Scientific Reports (PMC)", A),
 ("Biologically Active Compounds in Mustard Seeds: A Toxicological Perspective. Foods 2021;10(9):2089 (PMID 34574199, doi:10.3390/foods10092089) — 독일 연방위해평가원(BfR) 저자의 총설, EFSA 2016 에루크산 평가·EU 규정 2019/1870 인용", pmc("PMC8472142"), "Foods (MDPI, PMC)", A),
 ("Elemental characterization of wild edible plants from countryside and urban areas. Food Chem 2015;177:29-36 (PMID 25660854, doi:10.1016/j.foodchem.2014.12.069) — 초록만 확인", pm(25660854), "Food Chemistry (PubMed)", A),
 ("Antioxidant and Mineral Composition of Three Wild Leafy Species: A Comparison Between Microgreens and Baby Greens. Foods 2019;8(10):487 (PMID 31614816, doi:10.3390/foods8100487)", pmc("PMC6835962"), "Foods (MDPI, PMC)", A),
 ("Preservation of pears in water in the presence of Sinapis arvensis seeds: a Greek tradition. Int J Food Microbiol 2012;159(3):254-62 (PMID 23107505, doi:10.1016/j.ijfoodmicro.2012.08.015) — 초록만 확인", pm(23107505), "International Journal of Food Microbiology (PubMed)", A),
 ("Plant-mediated effects of ozone on herbivores depend on exposure duration and temperature. Sci Rep 2019;9:19891 (PMID 31882632, doi:10.1038/s41598-019-56234-z)", pmc("PMC6934497"), "Scientific Reports (PMC)", A),
 ("Burial and seed survival in Brassica napus subsp. oleifera and Sinapis arvensis including a comparison of transgenic and non-transgenic lines of the crop. Proc Biol Sci 1997;264(1378):1-7 (PMID 9061957, doi:10.1098/rspb.1997.0001) — 초록만 확인", pmc("PMC1688233"), "Proceedings of the Royal Society B (PMC)", A),
 ("Sinapis genomes provide insights into whole-genome triplication and divergence patterns within tribe Brassiceae. Plant J 2023;113(2):246-261 (PMID 36424891, doi:10.1111/tpj.16043) — 초록만 확인", pm(36424891), "The Plant Journal (PubMed)", A),
 ("Deep RNA-Seq to unlock the gene bank of floral development in Sinapis arvensis. PLoS One 2014;9(9):e105775 (PMID 25192023, doi:10.1371/journal.pone.0105775) — 초록만 확인", pmc("PMC4156300"), "PLoS One (PMC)", A),
 ("Transfer of Dicamba Tolerance from Sinapis arvensis to Brassica napus via Embryo Rescue and Recurrent Backcross Breeding. PLoS One 2015;10(11):e0141418 (PMID 26536372, doi:10.1371/journal.pone.0141418) — 초록만 확인", pmc("PMC4633294"), "PLoS One (PMC)", A),
 ("Development of a novel Sinapis arvensis disomic addition line in Brassica napus containing the restorer gene for Nsa CMS and improved resistance to Sclerotinia sclerotiorum and pod shattering. Theor Appl Genet 2010;120(6):1089-97 (PMID 20033391, doi:10.1007/s00122-009-1236-6) — 초록만 확인", pm(20033391), "Theoretical and Applied Genetics (PubMed)", A),
 ("Organelle genome composition and candidate gene identification for Nsa cytoplasmic male sterility in Brassica napus. BMC Genomics 2019;20:813 (PMID 31694534, doi:10.1186/s12864-019-6187-y) — 초록만 확인", pmc("PMC6836354"), "BMC Genomics (PMC)", A),
 ("Hybridization between transgenic Brassica napus L. and its wild relatives: Brassica rapa L., Raphanus raphanistrum L., Sinapis arvensis L., and Erucastrum gallicum. Theor Appl Genet 2003;107(3):528-39 (PMID 12721639, doi:10.1007/s00122-003-1278-0) — 초록만 확인", pm(12721639), "Theoretical and Applied Genetics (PubMed)", A),
 ("Barriers to gene flow from oilseed rape (Brassica napus) into populations of Sinapis arvensis. Mol Ecol 2002;11(1):103-12 (PMID 11903908, doi:10.1046/j.0962-1083.2001.01416.x) — 초록만 확인", pm(11903908), "Molecular Ecology (PubMed)", A),
 ("Trp574 substitution in the acetolactate synthase of Sinapis arvensis confers cross-resistance to tribenuron and imazamox. Pestic Biochem Physiol 2017;142:9-14 (PMID 29107252, doi:10.1016/j.pestbp.2016.12.008) — 초록만 확인", pm(29107252), "Pesticide Biochemistry and Physiology (PubMed)", A),
 ("Seed dormancy is modulated in recently evolved chlorsulfuron-resistant Turkish biotypes of wild mustard (Sinapis arvensis). Front Chem 2015;3:46 (PMID 26258120, doi:10.3389/fchem.2015.00046) — 초록만 확인", pmc("PMC4513236"), "Frontiers in Chemistry (PMC)", A),
 ("Surveillance and mapping of tribenuron-methyl-resistant weeds in wheat fields. Sci Rep 2024;14:28626 (PMID 39562594, doi:10.1038/s41598-024-75308-1) — 초록만 확인", pmc("PMC11576891"), "Scientific Reports (PMC)", A),
 ("Primary structure, spectroscopic and inhibitory properties of a two-chain trypsin inhibitor from the seeds of charlock (Sinapis arvensis L), a member of the napin protein family. Int J Pept Protein Res 1994;43(5):425-30 (PMID 8070965, doi:10.1111/j.1399-3011.1994.tb00540.x) — 초록만 확인", pm(8070965), "International Journal of Peptide and Protein Research (PubMed)", A),
 ("Susceptibility of herpes simplex virus type 1 to monoterpenes thymol, carvacrol, p-cymene and essential oils of Sinapis arvensis L., Lallemantia royleana Benth. and Pulicaria vulgaris Gaertn. Cell Mol Biol 2017;63(8):58-63 (PMID 28886313, doi:10.14715/cmb/2017.63.8.10) — 초록만 확인", pm(28886313), "Cellular and Molecular Biology (PubMed)", A),
 ("Phytoremediation of lead-contaminated soil by Sinapis arvensis and Rapistrum rugosum. Int J Phytoremediation 2016;18(4):387-92 (PMID 26552966, doi:10.1080/15226514.2015.1109607) — 초록만 확인", pm(26552966), "International Journal of Phytoremediation (PubMed)", A),
 ("Mustard oil and cardiovascular health: Why the controversy? J Clin Lipidol 2022;16(1):13-22 (PMID 34924350, doi:10.1016/j.jacl.2021.11.002) — 초록만 확인", pm(34924350), "Journal of Clinical Lipidology (PubMed)", A),
 ("In vivo, attenuation of schistosome cercarial development and disturbance of egg laying capacity in Biomphalaria alexandrina using sublethal concentrations of plant molluscicides. J Egypt Soc Parasitol 2001;31(3):657-69 (PMID 11775093) — 초록만 확인", pm(11775093), "Journal of the Egyptian Society of Parasitology (PubMed)", A),
 ("Pollen mixing in pollen generalist solitary bees: a possible strategy to complement or mitigate unfavourable pollen properties? J Anim Ecol 2014;83(3):588-97 (PMID 24164651, doi:10.1111/1365-2656.12168) — 초록만 확인", pm(24164651), "Journal of Animal Ecology (PubMed)", A),
 ("Evolution in stressful environments II: adaptive value and costs of plasticity in response to low light in Sinapis arvensis. J Evol Biol 2003;16(2):313-23 (PMID 14635870, doi:10.1046/j.1420-9101.2003.00518.x) — 초록만 확인", pm(14635870), "Journal of Evolutionary Biology (PubMed)", A),
 ("Aerodynamic properties of wild mustard (Sinapis arvensis L.) seed for separation from canola. J Sci Food Agric 2013;93(6):1466-70 (PMID 23070693, doi:10.1002/jsfa.5916) — 초록만 확인", pm(23070693), "Journal of the Science of Food and Agriculture (PubMed)", A),
]
sources = [{"n": i+1, "title": t, "url": u, "publisher": p, "accessed": a} for i,(t,u,p,a) in enumerate(S)]

sec = {}
sec["overview"] = ("한눈에 보기",
"들갓(Sinapis arvensis L.)은 배추과(Brassicaceae) 겨자속(Sinapis)의 풀로, 영어로는 charlock 또는 wild mustard라 부른다[1, 5]. 유럽·중동·서아시아가 원산지이고, 지금은 온대 지역 대부분에서 밭작물의 중요한 잡초로 퍼져 있다[11]. 한해살이 또는 가을에 싹 트는 두해살이(월년생)풀로 소개된다[5].\n\n"
"식품의약품안전처 「식품원료 목록」에서 들갓은 '들갓잎'이라는 원료명으로 식품원료(A코드)에 올라 있으며, 사용 조건은 '사용가능', 사용가능부위는 잎뿐이다[1]. 같은 속의 White mustard(Sinapis alba, 백겨자)는 잎과 씨앗을 쓸 수 있는 별도 원료로, 갓(Brassica juncea, 이명 Sinapis juncea)과 Black mustard(Brassica nigra, 이명 Sinapis nigra)도 각각 따로 올라 있어 들갓과 구별해야 한다[1]. 들갓은 건강기능식품 고시형 원료의 원재료가 아니며, 들갓을 쓴 건강기능식품 개별인정 원료는 확인하지 못함.\n\n"
"들갓 잎의 대표 이차대사산물은 글루코시놀레이트인 시날빈(4-하이드록시벤질글루코시놀레이트)이다[3]. 온실에서 키운 들갓에서 시날빈은 잎 총 글루코시놀레이트의 평균 60%, 꽃의 90%를 차지했다[2]. 반면 씨앗 기름은 에루크산이 41.43%로 가장 많은 지방산이어서 비식용 기름으로 분류된다[6].")
sec["history"] = ("역사와 전통 이용",
"그리스에는 배를 물에 담가 보존할 때 들갓 씨앗을 함께 넣는 가정식 전통이 있다[10]. 이 방식으로 보존한 배 발효액에서는 젖산균이 늘고 장내세균과(Enterobacteriaceae)가 줄었으며, 관능검사에서 대조군보다 전반적 기호도가 높았다[10].\n\n"
"이탈리아 남부 바리(Bari) 지역에서는 들갓이 야생 식용식물 11종 가운데 하나로 채집되어 무기질 조성이 분석되었다[8]. 이탈리아 전통 시골 음식에는 600종이 넘는 야생식물이 쓰이고 그중 약 200종이 잎채소인데, 2019년 연구는 들갓을 이런 야생 잎채소의 하나로 보고 새싹채소(microgreens)·어린잎채소(baby greens) 후보로 시험했다[9].\n\n"
"한편 들갓은 가축에게는 독초로도 알려져 있으며, 이란에서는 들갓 중독이 양에서 처음 확인되었다고 보고되었다[5]. 파키스탄 연구는 들갓을 에루크산 때문에 먹지 않는 기름 식물로 소개하며 야생에서 거둔 씨앗을 바이오디젤 원료로 썼다[6]. 한국에서 들갓 잎을 나물로 먹어 온 전통 이용 기록은 확인하지 못함.")
sec["biology"] = ("식물학적 특징",
"들갓은 한해살이 또는 월년생 풀이다[5]. 염색체 수는 2n = 18로, 2n = 38인 유채(Brassica napus)와 다르다[15]. 그늘(자연광의 40%)에서 키우면 배축이 길어지고 잎이 얇아지며(비엽면적 증가) 어린 개체의 무게가 줄고 꽃이 늦게 핀다[29].\n\n"
"씨앗은 흙 속에서 오래 살아남는다[12]. 영국 세 지역에서 씨앗을 묻어 두었을 때 들갓은 첫해에 평균 60%, 둘째 해에 32.5%가 살아남아 유채(첫해 1.5%, 둘째 해 0.2%)보다 훨씬 오래 버텼다[12]. 씨앗은 유채(카놀라) 씨앗과 크기·모양이 비슷해 수확물에 섞이며, 수분 5–20%에서 종말속도는 4.276–5.433 m/s로 카놀라(5.401–6.566 m/s)보다 낮아 바람으로 가려낼 수 있다[30].\n\n"
"꽃가루는 꽃가루를 가리지 않는 단독성 벌 Osmia cornuta의 애벌레에게 좋은 먹이로 쓰였고, 해로운 미나리아재비 꽃가루를 최대 50%까지 섞어도 애벌레 생존이 거의 영향을 받지 않았다[28]. 큰배추흰나비(Pieris brassicae)의 중요한 먹이식물이기도 하며, 들갓 잎의 시날빈은 식물 나이가 들수록 줄고 꽃에서는 반대로 늘었다[2].")
sec["related_species"] = ("분류와 근연종",
"겨자속에는 들갓과 백겨자(Sinapis alba)가 함께 들어 있지만, 유전체 분석에서 백겨자는 약 1,250만 년 전 배추속·무속의 조상과 갈라졌고 들갓은 약 650만 년 전 흑겨자(Brassica nigra)와 갈라졌다[13]. 들갓 유전체는 배추(B. rapa)나 양배추(B. oleracea)보다 흑겨자와 배열이 더 잘 맞아, 두 속의 계통 분류를 고쳐야 한다는 제안이 나왔다[13].\n\n"
"시날빈은 겨자속 근연 식물에서 두 번 따로 나타났는데, 한 번은 백겨자와 그 가까운 무리에서, 또 한 번은 시날빈이 없는 종들 사이에 자리한 들갓에서였다[3]. 두 종 모두 시날빈 분해산물(4-하이드록시페닐아세토니트릴)을 분해하는 효소가 있지만, 백겨자는 주로 카복실산을, 들갓은 주로 아마이드를 만든다[3].\n\n"
"들갓은 유채의 야생 근연종 가운데 가장 널리 퍼진 잡초다[19]. 영국 102개 집단의 들갓은 온실에서 유채와 쉽게 교잡되지 않았고 밭에서도 유채 유전자가 옮겨 간 것을 찾지 못했다[19]. 캐나다 상업 포장에서 들갓 실생 42,828개를 조사했을 때도 유채와의 잡종은 없었다[18]. 식품원료 목록에서는 백겨자·갓·흑겨자가 들갓과 다른 원료로 따로 올라 있다[1].")
sec["cultivation"] = ("재배와 잡초 관리",
"들갓은 작물로 재배하기보다 밀·유채 밭에서 방제해야 하는 잡초로 주로 다뤄진다[11, 22]. 이란에서 2018년 밀밭 의심 집단을 조사한 결과 들갓 44개 집단(조사한 들갓 집단의 81%)이 제초제 트리베누론메틸에 저항성을 보였다[22]. 그리스의 들갓 9개 집단은 ALS 효소 574번 트립토판이 류신으로 바뀌어 트리베누론과 이마자목스에 교차저항성을 보였으나 MCPA에는 모두 감수성이었다[20]. 튀르키예에서는 ALS 197번 프롤린이 세린 또는 트레오닌으로 바뀐 클로르술푸론 저항성 개체가 확인되었고, 이들은 씨앗 휴면 양상도 달랐다[21].\n\n"
"식용 재배 시험으로는, 들갓을 수경재배해 새싹채소와 어린잎채소로 거두는 연구가 있었다[9]. 이 연구에서 세 야생 잎채소의 질산염은 모든 시료에서 2,000 mg/kg 생체중을 넘었다[9]. 통계청 농작물생산조사와 농림축산식품부 특용작물 생산실적 파싱본에는 들갓 항목이 없어 국내 재배 면적과 생산량은 확인하지 못함. 들갓의 지리적 표시 등록도 확인하지 못함.")
sec["processing"] = ("가공과 이용",
"식품원료 목록에서 들갓은 잎만 식품에 쓸 수 있고, 씨앗·뿌리·줄기는 사용가능부위에 없다[1]. 들갓잎 가공식품이나 건강기능식품의 국내 생산실적은 확인하지 못함.\n\n"
"씨앗은 식품 이외 용도로 연구되었다[6]. 파키스탄 야생 들갓 씨앗 20 kg을 착유기로 짰을 때 기름 수율은 32.5%였고, 이 기름을 철·주석 산화물 나노촉매로 에스터교환하면 90분 만에 바이오디젤 수율 97.6%를 얻었다[6]. 이 바이오디젤의 요오드가는 81.24 g I/100 g, 비누화가는 179.04 mg KOH/g이었다[6]. 그리스 전통 배 보존법에서는 씨앗을 넣은 물에서 젖산균이 늘고 옥살산 등이 더 많이 생겼다[10].\n\n"
"그 밖에 들갓 정유는 단순포진바이러스 1형(HSV-1) 억제 선별 시험에 쓰였고[24], 말린 들갓 가루는 주혈흡충 중간숙주 달팽이(Biomphalaria alexandrina)에 살패 활성을 보였다[27]. 납으로 오염된 흙에서 들갓은 생장이 크게 줄지 않으면서 뿌리에 납을 많이 쌓아 식물정화 후보로 제시되었다[25].")
sec["genetics"] = ("유전 정보",
"한 비교유전체 연구에서 들갓의 유전체가 흑겨자·백겨자와 함께 새로 조립되었다[13]. 들갓과 백겨자 모두 약 2,050만 년 전 배추족(Brassiceae) 공통의 전체 유전체 3배화 흔적을 간직하고 있으며, 하위 유전체 사이에 유전자 밀도·발현의 우세가 나타났다[13]. 꽃 전사체 분석에서는 40,981,443개의 리드로 96,562개의 유전자 단편(평균 832 bp)과 21,321개의 단순반복서열(SSR)이 얻어졌다[14].\n\n"
"들갓은 유채 육종의 외래 유전자원으로 쓰인다[14]. 유채와 들갓을 체세포 융합해 만든 'Nsa' 세포질 웅성불임 계통의 미토콘드리아 유전체는 주로 들갓에서 왔고, 후보 불임 유전자 orf224·orf309·orf346은 들갓 미토콘드리아 서열과 100% 같았다[17]. 들갓 염색체 한 쌍과 유채 염색체 19쌍을 가진 부가 계통은 Nsa 불임의 임성을 회복시키고 균핵병(Sclerotinia sclerotiorum) 저항성이 높으며 꼬투리 터짐이 적었다[16]. 캐나다의 디캄바 저항성 들갓에서는 배 구조(embryo rescue)와 7세대 여교잡으로 저항성을 유채에 옮겼다[15].")
sec["safety"] = ("안전성",
"이란 셈난주에서 들갓이 많은 땅에 방목한 양 50마리 가운데 7마리가 약 3일 안에 죽었고, 반추위에서 들갓 씨앗과 줄기가 다량 나왔다[5]. 이 보고는 독성 성분으로 겨자 휘발성 기름, 알칼로이드로 표현된 시나핀(sinapine), 시날빈을 들었다[5]. 사람이 들갓 잎을 먹고 중독된 사례는 확인하지 못함.\n\n"
"들갓 씨앗 기름에서 에루크산은 41.43%였다[6]. 유럽식품안전청(EFSA)은 2016년 어린 쥐와 갓 태어난 돼지의 심근 지방증을 근거로 에루크산의 1일 섭취한계량(TDI)을 체중 1 kg당 7 mg으로 정했다[7]. EU 규정 2019/1870은 식용 유지의 에루크산을 20 g/kg 이하, 겨자 기름은 50 g/kg 이하로 제한한다[7]. 미국 식품의약국(FDA)은 압착 겨자 기름을 식용유로 허용하지 않는다[7, 26]. 들갓 잎의 에루크산 함량은 확인하지 못함.\n\n"
"글루코시놀레이트는 동물에서 사료 섭취 감소와 갑상선 기능 변화 등을 일으킬 수 있고, 시날빈은 분해되어 4-하이드록시벤질 이소티오시아네이트를 거쳐 4-하이드록시벤질알코올과 티오시아네이트 이온이 된다[7]. 시니그린은 흑겨자 잎·꽃 글루코시놀레이트의 98% 이상을 차지했으나 들갓의 주성분은 시날빈이었다[2]. 들갓 잎의 시니그린 함량은 확인하지 못함. 겨자 씨앗의 2S 알부민(나핀)은 주요 겨자 알레르겐이며, 들갓 씨앗에서도 나핀 계열 단백질이 분리되었다[7, 23]. 들갓은 흙의 납을 뿌리에 잘 쌓으므로 오염지 채집을 피해야 한다[25]. 들갓의 알레르기·잔류농약에 관한 국내 공공기관 정보는 확인하지 못함.")

sections = [{"key": k, "title": v[0], "body": v[1]} for k, v in sec.items()]

compounds = [
 {"name": "Sinalbin", "name_ko": "시날빈(4-하이드록시벤질글루코시놀레이트, 글루코시날빈)", "class": "글루코시놀레이트(방향족)", "role": "marker", "part": "잎·꽃·뿌리",
  "content_text": "온실 재배 개체에서 잎 총 글루코시놀레이트의 평균 60%, 꽃의 90%[2]; 잎·뿌리에서 검출[3]",
  "activity_ko": "들갓의 대표 글루코시놀레이트로 근연종 사이에서 독립적으로 나타남[3]; 피해 입은 잎에서 더 많아짐[2]", "source": [2, 3]},
 {"name": "4-Methoxyglucobrassicin", "name_ko": "4-메톡시글루코브라시신", "class": "글루코시놀레이트(인돌계)", "role": "bioactive", "part": "잎",
  "content_text": "", "activity_ko": "잎에서 꽃보다 상대적으로 많고, 들갓에서 애벌레 피해 조직에 더 많음[2]", "source": [2]},
 {"name": "4-Hydroxybenzyl isothiocyanate", "name_ko": "4-하이드록시벤질 이소티오시아네이트", "class": "이소티오시아네이트(시날빈 분해산물)", "role": "bioactive", "part": "조직 손상 시 생성",
  "content_text": "", "activity_ko": "미로시나아제가 시날빈을 분해해 생기며 물에서 4-하이드록시벤질알코올·티오시아네이트 이온으로 바뀜[7]", "source": [7]},
 {"name": "4-Hydroxyphenylacetonitrile", "name_ko": "4-하이드록시페닐아세토니트릴", "class": "니트릴(시날빈 분해산물)", "role": "bioactive", "part": "잎",
  "content_text": "", "activity_ko": "들갓의 특이적 니트릴 분해효소(니트릴 수화효소)의 기질[3, 4]", "source": [3, 4]},
 {"name": "4-Hydroxyphenylacetamide", "name_ko": "4-하이드록시페닐아세트아마이드", "class": "아마이드(니트릴 대사산물)", "role": "bioactive", "part": "잎",
  "content_text": "", "activity_ko": "들갓 니트릴 수화효소의 주 생성물[3]; 들갓을 먹은 배추흰나비 애벌레가 황산 에스터로 배설[4]", "source": [3, 4]},
 {"name": "Sinapine", "name_ko": "시나핀", "class": "페놀성 콜린 에스터(문헌에서는 알칼로이드로 표기)", "role": "bioactive", "part": "",
  "content_text": "", "activity_ko": "양 중독 보고에서 들갓의 독성 성분 가운데 하나로 거론[5]; 함량은 확인하지 못함", "source": [5]},
 {"name": "Erucic acid", "name_ko": "에루크산", "class": "단일불포화지방산(C22:1)", "role": "bioactive", "part": "씨앗 기름(식품원료 사용부위 아님)",
  "content_text": "씨앗 기름 지방산의 41.43%(최다 지방산)[6]", "activity_ko": "어린 쥐·새끼 돼지에서 심근 지방증; EFSA TDI 7 mg/kg 체중[7]", "source": [6, 7]},
 {"name": "Napin", "name_ko": "나핀형 트립신 억제 단백질(2S 알부민)", "class": "저장단백질(나핀 계열)", "role": "bioactive", "part": "씨앗",
  "content_text": "분자량 15,500, 이황화결합으로 이어진 두 사슬[23]", "activity_ko": "트립신 억제 활성[23]; 겨자 씨앗의 나핀(2S 알부민)은 주요 알레르겐[7]", "source": [7, 23]},
 {"name": "Calcium", "name_ko": "칼슘", "class": "무기질", "role": "nutrient", "part": "잎(야생 채집)",
  "content_text": "", "activity_ko": "이탈리아 야생 식용식물 가운데 들갓이 칼슘의 좋은 공급원으로 평가됨(수치는 초록에 없음)[8]", "source": [8]},
 {"name": "Nitrate", "name_ko": "질산염", "class": "무기 질소화합물", "role": "nutrient", "part": "새싹채소·어린잎",
  "content_text": "세 야생 잎채소(들갓 포함)의 종별 평균 5,205–6,833 mg/kg 생체중, 모든 시료 2,000 mg/kg 생체중 초과(종별 대응은 확인하지 못함)[9]", "activity_ko": "수경재배 시 높게 쌓여 상품화의 제약으로 지적됨[9]", "source": [9]},
]

assays = [
 {"role": "literature", "compound": "Sinalbin", "compound_ko": "시날빈(탈황 글루코시놀레이트로 정량)", "part": "잎·꽃(온실 재배, 동결건조 분말)",
  "content": "잎 총 글루코시놀레이트의 평균 60%, 꽃의 90%[2]", "method": "HPLC-PDA(탈황 글루코시놀레이트)",
  "conditions": {"instrument": "HPLC, 포토다이오드 어레이 검출기", "column": "Alltima C-18 역상, 150 × 4.6 mm",
   "mobile_phase": "아세토니트릴–물", "gradient": "0–30분 아세토니트릴 2→65%", "flow": "0.75 mL/min", "temp": "40 °C",
   "detection": "229 nm(적분 파장)", "injection": "",
   "sample_prep": "동결건조 분말 약 50.0 mg에 70% 메탄올 1.0 mL, 5분 끓여 효소 불활성화, 초음파 15분, 원심분리 10분, 잔사 재추출 후 합쳐 2.0 mL; 이 중 1 mL를 DEAE-Sephadex A25 칼럼에 걸고 설파타아제(type H-1)로 탈황",
   "standard": "시니그린 외부표준; 표준품·인증 유채 표준물질(BCR-367R)의 머무름 시간·UV 스펙트럼으로 동정",
   "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "들갓에서 시날빈이 잎·꽃 글루코시놀레이트의 주성분이고[2], 근연종 중 들갓을 특징짓는 성분이다[3]. 절대 함량(μmol/g)은 본문 그림에만 있어 확인하지 못했고 검출·정량한계·회수율도 본문에 없어 비워 둠.",
  "source": [2], "url": pmc("PMC5501907"), "source_kind": "paper"},
 {"role": "literature", "compound": "Sinalbin", "compound_ko": "시날빈 및 글루코시놀레이트 28종", "part": "잎·뿌리",
  "content": "", "method": "",
  "conditions": {"instrument": "", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "", "injection": "", "sample_prep": "", "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "겨자속 근연 20종의 잎·뿌리에서 시날빈 등 29종 글루코시놀레이트를 정량해 들갓의 시날빈이 독립적으로 진화했음을 보였다[3]. 전문 확인 못함 — 함량과 분석 조건은 초록에 없어 비워 둠.",
  "source": [3], "url": pm(18995873), "source_kind": "paper"},
]

d = {"slug": "sinapis-arvensis", "name_ko": "들갓", "name_en": "Charlock (wild mustard)",
     "scientific_name": "Sinapis arvensis L.",
     "aliases": ["들갓잎", "charlock", "wild mustard", "field mustard", "Sinapis arvensis L."],
     "sections": sections, "compounds": compounds, "markers": [], "assays": assays, "nutrients": [],
     "production": [], "world": [], "gi": [], "orgs": [], "sources": sources}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in sections: print(s["key"], len(s["body"]))
