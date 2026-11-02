import json, re
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
PM = "PubMed / "
def pm(pmid, title, pub, note="초록 확인"):
    return {"title": f"{title} (PMID {pmid}; {note})", "url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/", "publisher": pub, "accessed": "2026-11-02"}
def pmc(pmcid, pmid, title, pub, note="PMC 전문 확인"):
    return {"title": f"{title} (PMID {pmid}, {pmcid}; {note})", "url": f"https://pmc.ncbi.nlm.nih.gov/articles/{pmcid}/", "publisher": pub, "accessed": "2026-11-02"}
I1020 = "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020"
S = {
 "i1020": {"title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 한속단 11개 원료명 행(학명 Phlomis umbrosa Turcz.; 한속단분말·한속단추출분말·한속단추출고형분·한속단추출액·한속단잎·한속단농축분말·한속단농축액·한속단뿌리·한속단뿌리분말·한속단뿌리농축액·한속단뿌리추출분말), 모두 식품원료(A코드) '사용가능', 조건 '사용가능부위 : 잎, 뿌리※(한속단)'. 로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json", "url": I1020, "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
 "ht042row": {"title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 건강기능식품(C코드) 개별인정 '황기추출물 등 복합물(HT042)(기능성원료인정제2014-40호)', 조건 '황기(사용부위 : 뿌리), 한속단(사용부위：뿌리), 가시오갈피(사용부위 : 줄기)', 사용가능. 로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json", "url": I1020, "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
 "review": pm("34082016", "Phlomoides umbrosa (Turcz.) Kamelin & Makhm: A review of its traditional uses, botany, phytochemistry, pharmacology and clinical research. J Ethnopharmacol 2021;278:114252, doi:10.1016/j.jep.2021.114252", "Elsevier / PubMed"),
 "nomen": pmc("PMC12472938", "41011285", "Integrative Study of Dipsaci Radix and Phlomidis Radix: Nomenclature, Morphology, DNA-Based Authentication, and Comparative Effects on Osteoclastogenesis. Pharmaceuticals (Basel) 2025;18(9):1418, doi:10.3390/ph18091418", "MDPI / PubMed Central"),
 "scar": pmc("PMC6099718", "30018232", "Authentication of Herbal Medicines (두 종명은 PubMed 추출본에서 빠짐) Using DNA Barcodes, Chloroplast Genome, and Sequence Characterized Amplified Region (SCAR) Marker. Molecules 2018;23(7):1748, doi:10.3390/molecules23071748", "MDPI / PubMed", note="초록 확인"),
 "asthma": pmc("PMC13114087", "42072062", "Ameliorating Effects of Phlomoides umbrosa Turcz. Root in Ovalbumin-Induced Allergic Asthma: Modulation of IL-33-Mediated Inflammation and TGF-β/Smad-Dependent Fibrosis. Antioxidants (Basel) 2026;15(4):420, doi:10.3390/antiox15040420", "MDPI / PubMed Central"),
 "sesam": pmc("PMC10674976", "38005716", "[종명 빠짐: Phlomidis Radix] Extract Alleviates Paclitaxel-Induced Neuropathic Pain by Modulating Spinal TRPV1 in Mice. Plants (Basel) 2023;12(22):3819, doi:10.3390/plants12223819", "MDPI / PubMed Central", note="PMC 전문 확인, 분석 조건 표는 추출본에 없음"),
 "ht042imm": pmc("PMC12112177", "40429990", "Astragalus Extract Mixture HT042 Reverses Cyclophosphamide-Induced Immunosuppression Through Dual Modulation of Innate and Adaptive Immunity. Int J Mol Sci 2025;26(10):4850, doi:10.3390/ijms26104850", "MDPI / PubMed Central"),
 "obes": pmc("PMC9409404", "36012561", "Novel Plant Extract Ameliorates Metabolic Disorder through Activation of Brown Adipose Tissue in High-Fat Diet-Induced Obese Mice. Int J Mol Sci 2022;23(16):9295, doi:10.3390/ijms23169295", "MDPI / PubMed Central"),
 "rhiz": pm("17633208", "[Chemical constituents from rhizome of Phlomis umbrosa]. Yao Xue Xue Bao 2007 (중국어 논문)", "PubMed"),
 "root09": pm("19623984", "[Chemical constituents from roots of Phlomis umbrosa]. Zhongguo Zhong Yao Za Zhi 2009 (중국어 논문)", "PubMed"),
 "nortri": pm("18591808", "Novel Nortriterpenes from Phlomis umbrosa. Chem Pharm Bull (Tokyo) 2008, doi:10.1248/cpb.56.951", "Pharmaceutical Society of Japan / PubMed"),
 "phe": pm("19177241", "Phenylethanoid glycosides from the roots of Phlomis umbrosa. J Asian Nat Prod Res 2009, doi:10.1080/10286020802435687", "Taylor & Francis / PubMed"),
 "phyto18": pm("29929080", "28-Noroleanane-derived spirocyclic triterpenoids and iridoid glucosides from the roots of Phlomoides umbrosa (Turcz.) Kamelin & Makhm with their cytotoxic effects. Phytochemistry 2018;153:138-146, doi:10.1016/j.phytochem.2018.06.003", "Elsevier / PubMed"),
 "leafdam": pm("23972014", "Two new dammarane-type glycosides from Phlomis umbrosa. Nat Prod Res 2013, doi:10.1080/14786419.2013.828291", "Taylor & Francis / PubMed"),
 "leafphen": pm("19748456", "Phenolic composition and antioxidant activities of two Phlomis species: A correlation study. C R Biol 2009, doi:10.1016/j.crvi.2009.05.006", "Elsevier / PubMed"),
 "eo": pm("18243625", "Comparative analysis of essential oil components of three Phlomis species in Qinling Mountains of China. J Pharm Biomed Anal 2007, doi:10.1016/j.jpba.2007.12.027", "Elsevier / PubMed"),
 "antinoc": pm("21406221", "Antinociceptive and anti-inflammatory activities of Phlomis umbrosa Turcz extract. Fitoterapia 2011, doi:10.1016/j.fitote.2011.03.001", "Elsevier / PubMed"),
 "mast": pm("18167054", "Phlomis umbrosa root inhibits mast cell-dependent allergic reactions and inflammatory cytokine secretion. Phytother Res 2008, doi:10.1002/ptr.2164", "Wiley / PubMed"),
 "bone16": pm("27070559", "Effects of Phlomis umbrosa Root on Longitudinal Bone Growth Rate in Adolescent Female Rats. Molecules 2016, doi:10.3390/molecules21040461", "MDPI / PubMed"),
 "ht042grow": pm("21091251", "The herbal formula HT042 induces longitudinal bone growth in adolescent female rats. J Med Food 2010, doi:10.1089/jmf.2010.1007", "Mary Ann Liebert / PubMed"),
 "ht042rct": pm("29130588", "Effects of Astragalus Extract Mixture HT042 on Height Growth in Children with Mild Short Stature: A Multicenter Randomized Controlled Trial. Phytother Res 2018;32(1):49-57, doi:10.1002/ptr.5886", "Wiley / PubMed"),
 "ht042tox": pm("28732808", "Safety evaluation of Astragalus extract mixture HT042 and its constituent herbs in Sprague-Dawley rats. Phytomedicine 2017, doi:10.1016/j.phymed.2017.03.005", "Elsevier / PubMed"),
 "cyp": pm("32685423", "Inhibition of cytochrome P450 2B6 by Astragalus extract mixture HT042. Toxicol Res 2019, doi:10.1007/s43188-019-00027-z", "Springer / PubMed"),
 "estrct": pm("21887807", "The effect of herbal extract (Cynanchum wilfordii, Phlomis umbrosa, Angelica gigas 혼합 표준화 추출물) on pre-, peri- and post-menopausal women: a randomized double-blind, placebo-controlled study. Phytother Res 2011, doi:10.1002/ptr.3597", "Wiley / PubMed"),
 "efsa": pmc("PMC7010173", "32625484", "EFSA NDA Panel. Statement on the safety of an extract of three herbal roots as a novel food pursuant to Regulation (EC) No 258/97. EFSA J 2017;15(5):4778, doi:10.2903/j.efsa.2017.4778", "EFSA / PubMed Central"),
 "swer": pm("34818696", "Promotion of osteogenesis by Sweroside via BMP2-involved signaling in postmenopausal osteoporosis. Phytother Res 2021, doi:10.1002/ptr.7336", "Wiley / PubMed"),
 "antiv": pm("42739416", "Comparative Phytochemical and Antiviral Characteristics of [두 종명은 PubMed 추출본에서 빠짐: 초록상 속단(Sokdan)이라 불리는 두 종] Against Influenza A Virus: LC-QTOF-MS Profiling and Exploratory Network Pharmacology. Plants (Basel) 2026, doi:10.3390/plants15172649", "MDPI / PubMed"),
 "oa21": pm("34685839", "Effects of [두 종명은 PubMed 추출본에서 빠짐: 초록상 Dipsacus asperoides 추출물(DAE)·Phlomis umbrosa 추출물(PUE)] Extracts in a Rat Model of Osteoarthritis. Plants (Basel) 2021, doi:10.3390/plants10102030", "MDPI / PubMed"),
 "oa20": pm("33310311", "Protective effects of Phlomis umbrosa extract on a monosodium iodoacetate-induced osteoarthritis model and prediction of molecular mechanisms using transcriptomics. Phytomedicine 2020, doi:10.1016/j.phymed.2020.153429", "Elsevier / PubMed"),
 "saihan": pm("29732798", "[Quantitative classification of natural plant communities in the Saihanba National Nature Reserve, Hebei Province, China.] Ying Yong Sheng Tai Xue Bao 2016, doi:10.13287/j.1001-9332.201605.007", "PubMed"),
 "hfitems": {"title": "식품의약품안전처 「식품 등의 생산실적」 품목 유형별 현황(개별인정형) — 황기추출물 등 복합물(HT042) 2018–2025 행(생산액·판매액 천원 단위). 로컬 파싱본 docs/stats/hf_items.csv", "url": "https://www.mfds.go.kr", "publisher": "식품의약품안전처", "accessed": "2026-11-02"},
 "dipsHPLC": pm("23877237", "Quantitative determination and pattern recognition analyses of bioactive marker compounds from Dipsaci Radix by HPLC. Arch Pharm Res 2013;36(11):1345-53, doi:10.1007/s12272-013-0162-y", "Springer / PubMed"),
 "estrog": pmc("PMC5266372", "28133516", "Evaluation of Estrogenic Activity of Extract from the Herbal Mixture Cynanchum wilfordii Hemsley, Phlomis umbrosa Turczaninow, and Angelica gigas Nakai. Toxicol Res 2017, doi:10.5487/TR.2017.33.1.071", "Korean Society of Toxicology / PubMed", note="초록 확인"),
 "sleep": pmc("PMC11904018", "40093550", "Improvement of sleep disorders through the adenosine A1 receptor agonist effect of Phlomoides umbrosa Turczaninow root extract in pentobarbital-induced ICR mice. Food Sci Biotechnol 2025;34(5):1149-1159, doi:10.1007/s10068-024-01663-4", "Springer / PubMed", note="초록 확인"),
 "blb": pm("41574595", "Black Raspberry and Phlomis umbrosa Turcz. Extract Mixture (BLB301) Alleviates Dexamethasone-Induced Muscle Atrophy by Modulating Oxidative Stress and Protein Turnover Pathways. J Med Food 2026, doi:10.1177/1096620X251412890", "SAGE / PubMed"),
}

SEC = [
("overview", "한눈에 보기", """한속단(Phlomis umbrosa Turcz.)은 꿀풀과(Lamiaceae)의 여러해살이풀로, 뿌리를 말린 약재는 Phlomidis Radix라 부르고 「대한민국약전외한약(생약)규격집」에서는 약재명 '한속단'으로 쓴다[@nomen]. 현재 여러 식물 이름 데이터베이스는 이 학명을 Phlomoides umbrosa (Turcz.) Kamelin & Makhm.의 이명으로 다룬다[@nomen, @review]. 영어로는 shady Jerusalem sage라는 이름이 논문에 쓰였다[@blb].

식품원료로서 한속단은 식약처 「식품원료 목록」에 한속단뿌리·한속단잎·한속단분말·한속단추출분말·한속단농축액 등 11개 원료명으로 올라 있고, 모두 '사용가능' 원료다[@i1020]. 사용 조건은 '사용가능부위 : 잎, 뿌리※(한속단)'으로, 잎과 뿌리를 식품에 쓸 수 있다[@i1020]. 이 종을 원재료로 하는 건강기능식품 고시형 원료는 없고, 한속단 뿌리를 황기 뿌리·가시오갈피 줄기와 섞은 개별인정 원료 '황기추출물 등 복합물(HT042)(기능성원료인정제2014-40호)'가 목록에 있다[@ht042row].

연구에서 주로 다룬 성분은 산지사이드 메틸에스터·세사모사이드 같은 이리도이드 배당체와 페닐에타노이드 배당체, 노르트리테르페노이드다[@review, @rhiz, @asthma]. 효과 보고는 대부분 세포·동물 실험이며, 사람 시험은 한속단이 들어간 복합 추출물(HT042, 3종 뿌리 혼합 추출물)에 대한 것이다[@ht042rct, @estrct]. 이름이 비슷한 약재 속단(Dipsaci Radix, Dipsacus asper)과는 다른 식물이므로 자료를 섞지 않아야 한다[@nomen]."""),
("history", "이용의 역사", """한속단은 중국에서 'Caosu', 한국에서 'Han Sok-Dan'으로 불리며 수백 년 동안 감기·관절염·골다공증 등에 전통약으로 쓰였고, 식품첨가 용도로도 쓰였다고 정리되어 있다[@review]. 중국 후베이성 서부의 투자족(Tujia)은 이 뿌리를 류머티즘 질환 치료에 써 왔다[@rhiz]. 한국 전통의학에서는 골절·류머티즘 관절염·관절통과 뼈 질환에 뿌리를 써 왔다고 보고되었다[@oa20, @swer].

한국에서는 '속단'이라는 이름 때문에 혼동이 이어졌다[@nomen]. 약재 속단(Dipsaci Radix)의 기원종은 Dipsacus asper인데, 한국 식물지에서는 Phlomis umbrosa의 식물명이 '속단'이고 약재명은 '한속단'이어서 두 약재가 섞여 쓰이는 일이 잦았다[@nomen, @scar].

현대 제품으로는 한속단 뿌리를 황기·가시오갈피와 섞은 HT042가 개별인정 원료(기능성원료인정제2014-40호)로 등록되었다[@ht042row]. HT042 임상 논문은 이 원료가 식약처로부터 'HT042 can help height growth of children'이라는 기능성 표현을 인정받았다고 적었다[@ht042rct]. 큰조롱(Cynanchum wilfordii)·한속단·참당귀(Angelica gigas) 3종 뿌리의 열수 혼합 추출물은 갱년기 여성 대상 무작위 시험(2011년 발표)을 거쳤고, 유럽식품안전청(EFSA)이 2016년과 2017년에 신규식품으로 안전성을 평가했다[@estrct, @efsa]."""),
("biology", "식물학적 특징", """한속단은 꿀풀과 식물로, 같은 이름으로 불리는 Dipsacus 종들과는 지상부 모양으로 쉽게 구별된다[@nomen]. 잎겨드랑이에 꽃이 층층이 돌려나는 돌려나기 꽃차례(verticillaster)를 이루고, 꽃부리는 입술 모양으로 위아래 두 갈래로 갈라진다[@nomen]. 줄기잎은 갈라지지 않은 둥근 달걀꼴에서 긴 달걀꼴이다[@nomen]. 이에 비해 Dipsacus asper와 D. japonicus는 둥근 머리 모양 꽃차례를 가지고 잎이 깃 모양으로 갈라진다[@nomen].

한속단은 한국과 중국에 널리 분포하며, 중국에서는 북부에 자란다고 기술되었다[@sesam, @rhiz]. 중국 친링(Qinling) 산지에는 야생 개체가 자라고, 허베이성 사이한바(Saihanba) 자연보호구의 자작나무·사시나무 숲 하층 식물군락 구성종으로도 기록되었다[@eo, @saihan].

약재로는 뿌리와 뿌리줄기를 쓰고, 잎에서도 성분 연구가 이루어졌다[@nortri, @leafdam, @leafphen]. 한 연구는 세사모사이드가 지상부보다 뿌리에 더 많다는 선행 보고를 근거로 뿌리를 사용했다[@sesam]. 한국 식물지에 실린 변종·품종의 세부 형태(키·꽃 색 등)는 1차 자료를 열지 못해 확인하지 못함."""),
("related_species", "근연종과 혼동 약재", """한속단과 가장 자주 혼동되는 것은 약재 속단(Dipsaci Radix)이다[@nomen]. 속단의 기원종 Dipsacus asper Wall. ex DC.는 인동과(Caprifoliaceae, 옛 산토끼꽃과)에 속해, 꿀풀과인 한속단과는 과가 다르다[@nomen]. 한국 약재 시장에서는 Dipsacus japonicus 뿌리도 속단에 섞여 유통된다[@nomen].

두 약재는 지표성분이 다르다[@obes]. 한 논문은 Dipsacus의 지표성분으로 로가닌·스웨로사이드·아케비아 사포닌 D를, 한속단의 지표성분으로 산지사이드 메틸에스터를 들었다[@obes]. 반면 다른 논문은 스웨로사이드를 한속단의 지표성분이라고 적어 출처끼리 다르다[@swer]. LC-QTOF-MS 비교에서도 두 종은 성분 조성이 뚜렷이 달랐다[@antiv]. 속단 HPLC 정량법 연구는 속단 17개와 한속단 4개 시료의 크로마토그램 패턴으로 두 약재를 비교했다[@dipsHPLC].

효능 비교도 있다[@oa21, @nomen]. 골관절염 쥐 모델에서 두 추출물(각 200 mg/kg, 21일)은 모두 증상을 줄였다[@oa21]. 파골세포 실험에서는 한속단이 속단과 비슷하지만 약한 억제 효과를 보였고, D. japonicus 추출물만 세포독성을 나타냈다[@nomen].

같은 Phlomis 속의 P. megalantha는 잎 페놀 성분과 항산화 활성, 정유 조성 비교 연구의 대조 종으로 쓰였다[@leafphen, @eo]. P. megalantha 아세톤 추출물의 항산화 활성이 가장 높았다[@leafphen]."""),
("cultivation", "재배와 생산", """한속단은 한국 자생 식물로 소개된다[@sleep]. 농림축산식품부 「특용작물 생산실적」과 통계청 농작물생산통계의 로컬 파싱 표에는 한속단(또는 속단) 품목이 없어, 국내 재배 면적과 생산량은 확인하지 못함.

연구용 원료의 출처를 보면 국내 생산 뿌리가 쓰인다[@asthma, @sesam, @obes]. 2026년 천식 연구는 충북 제천에서 2022년 10월 채취한 말린 뿌리를 썼다[@asthma]. 2023년 신경병증 통증 연구는 경기 포천의 업체가 제공한 말린 뿌리를, 2022년 비만 연구는 경북 안동의 업체가 제공한 뿌리를 썼다[@sesam, @obes]. 수면 연구에는 농촌진흥청 국립원예특작과학원 연구진이 참여했다[@sleep].

중국에서는 친링 산지의 야생 개체에서 정유를 얻어 분석한 예가 있다[@eo]. 재배 방법(번식·파종 시기·수확 연수)에 관한 공공기관 자료는 확인하지 못함. 지리적 표시 등록 품목도 확인하지 못함."""),
("processing", "가공과 제품", """식품원료 목록에는 뿌리와 잎 자체 외에 분말·추출분말·추출고형분·추출액·농축분말·농축액 형태가 함께 올라 있다[@i1020]. 연구용 추출물은 대부분 물 또는 낮은 농도의 에탄올로 만든다[@asthma, @sesam, @obes, @sleep]. 20% 에탄올로 40 °C에서 2시간 환류 추출한 뒤 동결건조하거나[@asthma], 25% 에탄올로 80 °C에서 6시간 환류 추출한다[@sesam]. 70% 에탄올 초음파 추출(40 °C, 5시간 2회)의 수율은 20.5%였다[@obes]. 열수 추출물도 쓰인다[@sleep].

HT042는 황기·가시오갈피·한속단 추출물을 26.5:31.2:42.3의 고정 비율로 섞어 만든다[@ht042imm]. 표준화된 HT042에는 엘레우테로사이드 E 0.36%, 산지사이드 메틸에스터 0.15%, 포르모노네틴 0.008%가 들어 있다고 적혀 있다[@ht042imm]. 식약처 생산실적에서 황기추출물 등 복합물(HT042)은 2024년 생산량 438톤, 생산액 약 189.2억 원, 국내 판매액 약 333.6억 원이었다[@hfitems]. 2025년 값은 생산량 335톤, 생산액 약 151.6억 원, 국내 판매액 약 235.5억 원이다[@hfitems].

3종 뿌리 혼합 제품은 세 뿌리의 혼합물을 열수로 추출해 농축한 뒤 분무건조해 만든다[@efsa]. 한속단 단일 원료 식품의 생산 통계는 확인하지 못함."""),
("genetics", "유전체와 종 판별", """뿌리를 썰어 말린 약재 상태에서는 속단과 한속단을 형태로 구별하기 어려워 DNA 표지가 쓰인다[@nomen]. 2025년 연구는 ITS2와 또 하나의 바코드 구역 염기서열로 D. asper·D. japonicus·한속단 세 종을 뚜렷이 구별했다[@nomen]. ITS2에서 한속단과 두 Dipsacus 종 사이에는 72–75개의 변이가 있었고, 두 Dipsacus 종 사이에는 6–7개뿐이었다[@nomen]. 한속단의 ITS2 서열은 다른 두 종보다 5 bp 짧았다[@nomen].

2018년 연구는 속단·한속단 판별을 위해 DNA 바코드를 분석하고, 엽록체 유전체 두 개(160,530 bp, 160,371 bp)를 해독했으며, 세 종을 가르는 SCAR 표지를 개발했다[@scar]. 해독된 두 엽록체 유전체는 계통 분석에서 인동과 안의 단계통군에 들어가 Dipsacus 쪽 자료로 보인다[@scar]. 한속단 자체의 엽록체·핵 유전체 해독 자료는 확인하지 못함.

동물 실험에서 한속단 추출물이 골관절염 쥐 연골의 유전자 발현(Wnt/β-카테닌 등)을 바꾸었다는 전사체 분석 결과가 있다[@oa20]. 이는 먹은 동물 쪽의 유전자 반응이며, 한속단 품종 육성이나 유전 자원에 관한 공공 자료는 확인하지 못함."""),
("safety", "안전성과 사용 조건", """식약처 「식품원료 목록」에서 한속단 잎과 뿌리는 '사용가능' 원료이며, 제한 조건은 '사용가능부위 : 잎, 뿌리※(한속단)'뿐이다[@i1020]. 한속단 단일 원료에 대한 고시 섭취 주의사항은 없다[@i1020].

쥐 독성시험에서 HT042와 구성 약재(한속단 포함)는 각각 5000 mg/kg까지 한 번 먹여도 죽거나 독성 징후가 없었다[@ht042tox]. HT042의 13주 반복투여 무독성량은 4000 mg/kg/일이었다[@ht042tox]. 시험관 실험에서 HT042는 약물대사효소 CYP2B6을 억제했고(IC50 10.62 µg/mL), 원인 성분으로 산지사이드 메틸에스터가 지목되었다[@cyp]. 따라서 CYP2B6으로 대사되는 약을 먹는 사람은 주의가 필요할 수 있다[@cyp].

EFSA는 큰조롱·한속단·참당귀 3종 뿌리 열수 추출물을 폐경 후 여성의 식품보충제로 하루 최대 175 mg까지 안전하다고 결론지었다[@efsa]. 이 값은 90일 쥐 시험의 무독성량 500 mg/kg 체중/일에 불확실성 계수 200을 적용한 것이다[@efsa]. EFSA는 반복투여 시험에서 간 무게·알부민·총단백 증가와 혈액학적 변화를 근거로 들었다[@efsa]. 같은 3종 혼합 추출물은 OECD TG455 시험에서 에스트로겐 수용체 활성을 보이지 않았다[@estrog].

세포 실험에서 한속단 뿌리 추출물은 독성이 없었지만, 섞여 유통되는 D. japonicus 추출물은 세포독성을 보였다[@nomen]. 알레르기·잔류농약에 관한 공공기관 정보는 확인하지 못함. 임신·수유 중 안전성 자료도 확인하지 못함."""),
]

CMP = [
 {"name": "Shanzhiside methyl ester", "name_ko": "산지사이드 메틸에스터", "class": "이리도이드 배당체", "role": "marker", "part": "뿌리", "content_text": "뿌리 20% 에탄올 추출물 5.82 ± 0.10 μg/mg(건조 중량, HPLC-PDA)[@asthma]; 뿌리 70% 에탄올 추출물 7.2 mg/mL(본문 다른 곳 0.72%)[@obes]; HT042 1.75 ± 0.014 mg/g(표준화 기준 0.15%)[@ht042imm]", "activity_ko": "한속단 추출물의 지표성분으로 정량됨[@asthma, @obes]; 시험관에서 CYP2B6 억제(HT042 구성 성분 중 유일)[@cyp]", "source": ["asthma", "obes", "ht042imm", "cyp", "rhiz"]},
 {"name": "Sesamoside", "name_ko": "세사모사이드", "class": "이리도이드 배당체", "role": "marker", "part": "뿌리", "content_text": "뿌리 25% 에탄올 추출물 약 1.56%(HPLC-UV)[@sesam]", "activity_ko": "파클리탁셀 유발 신경병증 통증 생쥐에서 경구 5·7.5 mg/kg이 냉각 이질통 완화(동물)[@sesam]", "source": ["sesam", "asthma", "rhiz"]},
 {"name": "8-O-Acetylshanzhiside methyl ester", "name_ko": "8-O-아세틸산지사이드 메틸에스터", "class": "이리도이드 배당체", "role": "bioactive", "part": "뿌리·뿌리줄기", "content_text": "UPLC-QTOF-MS/MS로 확인(함량 확인하지 못함)[@asthma]; 뿌리줄기에서 분리[@rhiz]", "activity_ko": "추출물의 주요 성분 중 하나로 동정됨, 단독 활성은 확인하지 못함[@asthma]", "source": ["asthma", "rhiz"]},
 {"name": "Isoacteoside", "name_ko": "이소악테오사이드(이소베르바스코사이드)", "class": "페닐에타노이드 배당체", "role": "bioactive", "part": "뿌리·뿌리줄기", "content_text": "UPLC-QTOF-MS/MS로 확인(함량 확인하지 못함)[@asthma]; 뿌리줄기에서 분리[@rhiz]", "activity_ko": "천식 모델 추출물의 생리활성 성분 후보로 제시됨[@asthma]", "source": ["asthma", "rhiz"]},
 {"name": "Verbascoside", "name_ko": "베르바스코사이드(악테오사이드)", "class": "페닐에타노이드 배당체", "role": "bioactive", "part": "뿌리줄기", "content_text": "뿌리줄기에서 분리(함량 확인하지 못함)[@rhiz]", "activity_ko": "이 종에서 단독 활성 시험은 확인하지 못함[@rhiz]", "source": ["rhiz"]},
 {"name": "Phlomisone", "name_ko": "플로미손", "class": "28-노르올레아난형 스피로고리 트리테르페노이드", "role": "bioactive", "part": "뿌리줄기", "content_text": "에탄올 추출물에서 분리된 신규 노르트리테르펜 8종의 하나(함량 확인하지 못함)[@nortri]", "activity_ko": "HeLa·L929 암세포에 세포독성(시험관)[@nortri]", "source": ["nortri"]},
 {"name": "Oleanolic acid", "name_ko": "올레아놀산", "class": "올레아난형 트리테르펜", "role": "bioactive", "part": "뿌리", "content_text": "뿌리에서 분리(함량 확인하지 못함)[@root09]", "activity_ko": "이 종에서 단독 활성 시험은 확인하지 못함[@root09]", "source": ["root09"]},
 {"name": "Corosolic acid", "name_ko": "코로솔산", "class": "우르산형 트리테르펜", "role": "bioactive", "part": "뿌리", "content_text": "뿌리에서 분리(함량 확인하지 못함)[@root09]", "activity_ko": "이 종에서 단독 활성 시험은 확인하지 못함[@root09]", "source": ["root09"]},
 {"name": "Hederagenin", "name_ko": "헤데라게닌", "class": "올레아난형 트리테르펜", "role": "bioactive", "part": "뿌리", "content_text": "뿌리에서 처음 분리(함량 확인하지 못함)[@root09]", "activity_ko": "이 종에서 단독 활성 시험은 확인하지 못함[@root09]", "source": ["root09"]},
 {"name": "Phlomisumbroside A", "name_ko": "플로미스움브로사이드 A", "class": "다마란형 배당체", "role": "bioactive", "part": "잎", "content_text": "잎에서 분리된 신규 화합물(함량 확인하지 못함)[@leafdam]", "activity_ko": "활성 시험은 확인하지 못함[@leafdam]", "source": ["leafdam"]},
 {"name": "Rosmarinic acid", "name_ko": "로즈마린산", "class": "페놀산", "role": "bioactive", "part": "잎", "content_text": "잎 추출물의 주요 페놀 성분의 하나(HPLC로 14종 정량, 이 종의 수치는 초록에 없음)[@leafphen]", "activity_ko": "프로토카테크산과 함께 항산화 활성에 기여하는 성분으로 제시됨(시험관)[@leafphen]", "source": ["leafphen"]},
 {"name": "Chlorogenic acid", "name_ko": "클로로겐산", "class": "페놀산", "role": "bioactive", "part": "잎", "content_text": "잎 추출물의 주요 페놀 성분의 하나(수치는 초록에 없음)[@leafphen]", "activity_ko": "이 종에서 단독 활성은 확인하지 못함[@leafphen]", "source": ["leafphen"]},
 {"name": "Palmitic acid", "name_ko": "헥사데칸산(팔미트산)", "class": "지방산(정유 성분)", "role": "bioactive", "part": "지상부(개화기, 정유)", "content_text": "Phlomis 3종 정유의 주성분, 3종 범위 7.1–52.1%(이 종 단독 값은 초록에 없음)[@eo]", "activity_ko": "정유 조성 비교 연구, 활성 시험은 확인하지 못함[@eo]", "source": ["eo"]},
]

ASSAYS = [
 {"role": "literature", "compound": "Shanzhiside methyl ester", "compound_ko": "산지사이드 메틸에스터", "part": "뿌리(충북 제천, 2022년 10월 채취) 20% 에탄올 추출물", "content": "5.82 ± 0.10 μg/mg(건조 중량)[@asthma]", "method": "HPLC-PDA",
  "conditions": {"instrument": "Thermo Fisher Ultimate 3000 series HPLC + PDA 검출기", "column": "YMC-Triart C18(4.6 mm × 150 mm, 5 μm)", "mobile_phase": "A: 0.1% 포름산 수용액, B: 0.1% 포름산 메탄올", "gradient": "0–2분 5% B; 2–12분 5→15% B; 12–22분 15→50% B; 22–25분 50% B; 25–30분 50→100% B; 30–32분 100→5% B", "flow": "1 mL/min", "temp": "40 °C", "detection": "238 nm", "injection": "", "sample_prep": "추출물을 50% 메탄올에 3 mg/mL로 녹여 0.45 μm 실린지 필터로 여과", "standard": "산지사이드 메틸에스터 표준품(Biofron), 1·2·5·10·20·50 μg/mL", "linearity": "상관계수(R) 1", "lod": "0.10 ± 0.00 μg/mL", "loq": "0.31 ± 0.00 μg/mL", "recovery": "99.15 ± 1.91%(저), 99.06 ± 1.53%(중), 99.79 ± 2.16%(고); 반복성 RSD 0.39%, 재현성 0.17%"},
  "rationale": "논문이 산지사이드 메틸에스터를 한속단의 지표성분(marker compound)으로 보고 AOAC 지침에 따라 정량법을 검증했다; Dipsacus(로가닌·스웨로사이드·아케비아 사포닌 D)와 구별되는 성분으로도 제시된다[@asthma, @obes]", "source": ["asthma", "obes"], "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC13114087/", "source_kind": "paper"},
 {"role": "literature", "compound": "Sesamoside", "compound_ko": "세사모사이드", "part": "말린 뿌리(Phlomidis Radix) 25% 에탄올 추출물", "content": "약 1.56%[@sesam]", "method": "HPLC-UV",
  "conditions": {"instrument": "Agilent 1260 HPLC, UV 검출기", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "", "injection": "", "sample_prep": "추출물 100 mg에 에탄올 1 mL를 넣고 초음파 추출(4 °C, 30분), 원심분리(4 °C, 10,000 rpm, 30분) 후 상등액을 0.45 μm 필터로 여과", "standard": "세사모사이드(Chemface) 에탄올 원액을 6.25·12.5·25·50·100 μg/mL로 희석; 머무름 시간 약 8.6분", "linearity": "회귀식 추출본 표기 'y = 12.85621 + 3.71301'(x 기호 빠짐), RSQ 0.99991", "lod": "", "loq": "", "recovery": ""},
  "rationale": "세사모사이드를 한속단의 주성분이자 활성 성분으로 보고 정량했다; 칼럼·이동상·검출 파장 등은 논문 표에 있어 전문 추출본에서 확인하지 못함[@sesam]", "source": ["sesam"], "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10674976/", "source_kind": "paper"},
 {"role": "literature", "compound": "Shanzhiside methyl ester", "compound_ko": "산지사이드 메틸에스터", "part": "HT042(황기·가시오갈피·한속단 추출물 26.5:31.2:42.3 혼합물; 한속단은 뿌리)", "content": "1.75 ± 0.014 mg/g(표준화 기준 0.15%)[@ht042imm]", "method": "HPLC-UV",
  "conditions": {"instrument": "Agilent 1260 Infinity System", "column": "ZORBAX Eclipse Plus C18(4.6 × 250 mm, 5 µm)", "mobile_phase": "A: 0.5% 인산, B: 아세토니트릴", "gradient": "0–20분 5→17% B; 20–30분 17→22% B; 30–40분 22→30% B; 40–43분 30→100% B; 43–45분 100% B; 45–47분 100→5% B; 47–50분 5% B(엘레우테로사이드 E와 동시 분석)", "flow": "1.0 mL/min", "temp": "40 °C", "detection": "235 nm", "injection": "", "sample_prep": "", "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "HT042에서 한속단 유래 성분의 지표로 산지사이드 메틸에스터를 정량했다; 이 성분은 HT042의 CYP2B6 억제 원인 성분으로도 지목되었다[@ht042imm, @cyp]", "source": ["ht042imm", "cyp"], "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12112177/", "source_kind": "paper"},
]

# ---- build
order = []
def num(k):
    if k not in S: raise SystemExit("unknown key "+k)
    if k not in order: order.append(k)
    return order.index(k) + 1
def sub(text):
    return re.sub(r"\[(@[^\]]+)\]", lambda m: "[" + ", ".join(str(num(x.strip()[1:])) for x in m.group(1).split(",")) + "]", text)
sections = [{"key": k, "title": t, "body": sub(b)} for k, t, b in SEC]
def fix(items):
    out = []
    for it in items:
        it = json.loads(json.dumps(it, ensure_ascii=False))
        for f in ("content_text", "activity_ko", "content", "rationale"):
            if f in it: it[f] = sub(it[f])
        it["source"] = [num(k) for k in it["source"]]
        out.append(it)
    return out
compounds = fix(CMP); assays = fix(ASSAYS)
sources = [dict(n=i + 1, **S[k]) for i, k in enumerate(order)]
unused = [k for k in S if k not in order]
d = {"slug": "phlomis-umbrosa", "name_ko": "한속단", "name_en": "Shady Jerusalem sage", "scientific_name": "Phlomis umbrosa Turcz.",
     "aliases": ["속단(식물명)", "한속단뿌리", "Phlomidis Radix", "Han-Sok-Dan", "Caosu", "Phlomoides umbrosa (Turcz.) Kamelin & Makhm.", "Phlomis umbrosa Turczaninow"],
     "sections": sections, "compounds": compounds, "markers": [], "assays": assays, "nutrients": [], "production": [], "world": [], "gi": [], "orgs": [], "sources": sources}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
print("sources", len(sources), "unused", unused)
for s in sections: print(s["key"], len(s["body"]))
