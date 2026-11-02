import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
A = "2026-11-02"
def pm(title, doi, pub, pmc=None):
    p = pub + (f", {pmc}" if pmc else "") + ", PubMed"
    return {"title": title, "url": f"https://doi.org/{doi}", "publisher": p, "accessed": A}
S = [
 {"title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 북아메리카 장어(Anguilla rostrata) 항목", "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
 pm("Global consumption of threatened freshwater eels revealed by integrating DNA barcoding, production data, and trade statistics. Sci Rep 2025;15:29968", "10.1038/s41598-025-15458-y", "Scientific Reports", "PMC12356912"),
 pm("Draft genome of the American Eel (Anguilla rostrata). Mol Ecol Resour 2017;17(4):806-811", "10.1111/1755-0998.12608", "Molecular Ecology Resources"),
 pm("RAD-Seq Reveals Patterns of Additive Polygenic Variation Caused by Spatially-Varying Selection in the American Eel (Anguilla rostrata). Genome Biol Evol 2017;9(11):2974-2986", "10.1093/gbe/evx226", "Genome Biology and Evolution", "PMC5714190"),
 pm("DNA methylation patterns linked to salinity and geography in the American eel. Environ Epigenet 2025;11(1):dvaf012", "10.1093/eep/dvaf012", "Environmental Epigenetics", "PMC12684172"),
 pm("Comparative genomics and signatures of selection in North Atlantic eels. Mar Genomics 2022;62:100933", "10.1016/j.margen.2022.100933", "Marine Genomics"),
 pm("Identification of Anguilla anguilla (L.) and Anguilla rostrata (Le Sueur) and their hybrids based on a diagnostic single nucleotide polymorphism in nuclear 18S rDNA. Mol Ecol Resour 2010;10(1):173-176", "10.1111/j.1755-0998.2009.02698.x", "Molecular Ecology Resources"),
 pm("Applying DNA techniques to the identification of the species of dressed toasted eel products. J Agric Food Chem 2004;52(19):5972-5977", "10.1021/jf034525x", "Journal of Agricultural and Food Chemistry"),
 pm("A comparison of metal concentrations in the tissues of yellow American eel (Anguilla rostrata) and European eel (Anguilla anguilla). Sci Total Environ 2016;569-570:1435-1445", "10.1016/j.scitotenv.2016.06.232", "Science of the Total Environment"),
 pm("Spatial and temporal trends of mercury in the aquatic food web of the lower Penobscot River, Maine, USA, affected by a chlor-alkali plant. Sci Total Environ 2019;649:770-791", "10.1016/j.scitotenv.2018.08.203", "Science of the Total Environment"),
 pm("Contaminants in tropical island streams and their biota. Environ Res 2018;161:615-623", "10.1016/j.envres.2017.11.053", "Environmental Research"),
 pm("Dioxin-like contaminants are no longer a risk to the American eel (Anguilla rostrata) in Lake Ontario. Environ Toxicol Chem 2018;37(4):1061-1070", "10.1002/etc.4033", "Environmental Toxicology and Chemistry"),
 pm("Interlaboratory Comparison of Extractable Organofluorine Measurements in Groundwater and Eel (Anguilla rostrata): Recommendations for Methods Standardization. Environ Sci Technol 2023;57(48):20159-20168", "10.1021/acs.est.3c04560", "Environmental Science & Technology", "PMC10702518"),
 pm("Analysis of 17β-estradiol, estriol and estrone in American eel (Anguilla rostrata) tissue samples using liquid chromatography coupled to electrospray differential ion mobility tandem mass spectrometry. Rapid Commun Mass Spectrom 2017;31(10):842-850", "10.1002/rcm.7853", "Rapid Communications in Mass Spectrometry"),
 pm("Purification and characterization of the dipeptidyl peptidase-IV inhibitory peptides from eel (Anguilla rostrata) scraps enzymatic hydrolysate for the treatment of type 2 diabetes mellitus. J Sci Food Agric 2023;103(7):3714-3724", "10.1002/jsfa.12462", "Journal of the Science of Food and Agriculture"),
 pm("Isolation and Identification of a New Isolate of Anguillid Herpesvirus 1 from Farmed American Eels (Anguilla rostrata) in China. Viruses 2022;14(12):2722", "10.3390/v14122722", "Viruses", "PMC9784739"),
 pm("Complete Genome Sequence of Anguillid Herpesvirus 1 Isolated from Imported Anguilla rostrata (American Eel) from Canada. Microbiol Resour Announc 2022;11(12):e0082922", "10.1128/mra.00829-22", "Microbiology Resource Announcements", "PMC9753716"),
 pm("Detection of Dermocystidium anguillae in imported elvers of American eel Anguilla rostrata in China. Folia Parasitol 2022;69:2022.013", "10.14411/fp.2022.013", "Folia Parasitologica"),
 pm("Identification and characterization of a novel orthoreovirus from American eels, Anguilla rostrata. Microbiol Spectr 2026;14(5):e0360725", "10.1128/spectrum.03607-25", "Microbiology Spectrum", "PMC13141839"),
 pm("Characteristics of the long non-coding RNA-mRNA regulatory network in American eel (Anguilla rostrata) during Vibrio harveyi infection. Comp Biochem Physiol D 2026;59:101871", "10.1016/j.cbd.2026.101871", "Comparative Biochemistry and Physiology Part D"),
 pm("Spontaneous precocious vitellogenesis of female Anguilla rostrata in captive seawater cage. Theriogenology 2026;261:117952", "10.1016/j.theriogenology.2026.117952", "Theriogenology"),
 pm("Effect of Coated Inorganic Micro-Minerals on Growth, Mineral Retention, and Intestinal Health in Juvenile American Eels Under a Commercial RAS. Animals 2026;16(2):324", "10.3390/ani16020324", "Animals (MDPI)", "PMC12837468"),
 pm("Excessive dietary histamine inhibits growth performance and impairs intestinal and hepatic health in juvenile American eel (Anguilla rostrata). Front Physiol 2026;17:1797772", "10.3389/fphys.2026.1797772", "Frontiers in Physiology", "PMC13106369"),
 pm("Liver metabolomic analysis and expression under hypotonicity in American eel (Anguilla rostrata). Comp Biochem Physiol D 2026;59:101821", "10.1016/j.cbd.2026.101821", "Comparative Biochemistry and Physiology Part D"),
 pm("A processing plant survey of external lesions of American eels (Anguilla rostrata) from Lake Ontario and the St. Lawrence River, Canada. Prev Vet Med 1997;31(1-2):19-32", "10.1016/s0167-5877(96)01132-4", "Preventive Veterinary Medicine"),
 pm("RAD sequencing reveals within-generation polygenic selection in response to anthropogenic organic and metal contamination in North Atlantic Eels. Mol Ecol 2016;25(1):219-237", "10.1111/mec.13466", "Molecular Ecology"),
 pm("Biotransformation, antioxidant and histopathological biomarker responses to contaminants in European and American yellow eels from the Gironde and St. Lawrence estuaries. Chemosphere 2017;188:292-303", "10.1016/j.chemosphere.2017.08.139", "Chemosphere"),
 pm("Generation and characterization of the monoclonal antibody against the heavy chain of American eel (Anguilla rostrata) IgM. Fish Shellfish Immunol 2026;174:111355", "10.1016/j.fsi.2026.111355", "Fish & Shellfish Immunology"),
 {"title": "CITES committee rejects EU bid to list all eel species in Appendix II (2025-11-27 보도) — WebSearch 검색 요약으로만 확인, 원문·CITES 공식 기록은 열지 못함", "url": "https://www.undercurrentnews.com/2025/11/27/cites-committee-rejects-eu-bid-to-list-all-eel-species-in-appendix-ii/", "publisher": "Undercurrent News(업계 언론, 2차 자료)", "accessed": A},
 pm("Influence of fasting and diet on lipogenic enzymes in the american eel, Anguilla rostrata LeSueur. J Nutr 1981;111(2):346-354", "10.1093/jn/111.2.346", "The Journal of Nutrition"),
]
for i, s in enumerate(S, 1):
    s["n"] = i
S = [{"n": s["n"], "title": s["title"], "url": s["url"], "publisher": s["publisher"], "accessed": s["accessed"]} for s in S]

sec = {}
sec["overview"] = ("북아메리카 장어(Anguilla rostrata)는 뱀장어과(Anguillidae) Anguilla속의 물고기로, 식약처 「식품원료 목록」에는 '북아메리카 장어'라는 원료명과 영문명 American eel로 올라 있다[1]. "
 "이 목록에서 분류는 수산물, 상태는 '사용가능'이며, 사용 부위는 따로 정하지 않은 '-'로 적혀 있고 별도의 사용 조건은 없다[1]. "
 "같은 목록에는 뱀장어(A. japonica)·유럽뱀장어(A. anguilla)·비콜라뱀장어(A. bicolor)·무태장어(A. marmorata)·A. australis가 각각 다른 항목으로 올라 있으며, 이 문서는 그 종들의 자료를 섞지 않았다[1]. "
 "건강기능식품 고시형 원료의 원재료가 아니어서 식약처가 정한 지표성분은 없다[1].\n\n"
 "이 종은 바다에서 태어나 민물에서 자라는 장어로, 양식에 쓰는 실뱀장어(glass eel)는 모두 자연에서 잡은 것이다[2]. "
 "11개국 시장의 장어 제품 279점을 DNA로 판별한 연구에서 이 종이 54.1%로 가장 많았고, 생산·무역 자료로 환산하면 세계에서 가장 많이 소비되는 장어 종으로 추정되었다[2]. "
 "이 종은 국제자연보전연맹(IUCN) 적색목록에서 위협 범주로 분류된 종이다[2].")
sec["history"] = ("캐나다 세인트로렌스강 유역에서는 1997년 논문 기준 지난 10년 동안 이 종의 상업 어획량과 가입량이 줄어드는 징후가 관찰되었다[25]. "
 "이를 확인하려고 1992년 두 가공 공장에서 상업 어획 개체 12,243마리를 검사했는데, 외부 병변의 유병률은 모든 지점에서 1% 이하였다[25]. "
 "최근 수십 년 동안 이 종의 개체군은 40–80% 줄었다고 보고되었다[9].\n\n"
 "유럽뱀장어가 2007년 CITES 부속서 II에 오르고 무역이 제한된 뒤 동아시아의 수요가 이 종 등 다른 장어로 옮겨 갔다[2]. "
 "캐나다의 실뱀장어 총허용어획량은 전국 약 10 t인데, 2022년 캐나다에서 홍콩으로 약 40 t이 수입되었다고 보고되었다[2]. "
 "2025년 CITES 제20차 당사국총회에서 Anguilla속 전 종을 부속서 II에 올리자는 유럽연합 제안이 부결되었다는 보도가 있으나, 이는 검색 요약으로만 확인했고 CITES 공식 기록은 확인하지 못함[29]. "
 "따라서 이 종 자체의 CITES 부속서 등재는 이번 조사에서 확인하지 못함.")
sec["biology"] = ("이 종은 바다에서 산란하고 민물·기수에서 자라는 회유성 장어로, 유럽뱀장어와 함께 북대서양 사르가소해에서 일부 겹쳐 산란한다[6]. "
 "종 전체가 한 번식 집단을 이루는 범교배(panmixia) 종이어서 유전적으로 나뉜 지역 집단이 없다고 설명된다[4, 5]. "
 "그럼에도 아열대에서 아북극까지 매우 다양한 서식지에 퍼져 살며, 지역에 따라 표현형이 크게 다르다[4, 5].\n\n"
 "북반구 온대 장어인 이 종의 난소는 바다로 내려가기 전 유적기(oil droplet stage)에서 발달을 멈추는 것이 보통이다[21]. "
 "그런데 연안 해상 가두리에서 기른 2년생 개체의 40% 이상이 자연적으로 초기 난황형성기까지 발달했고, 평균 여포 지름은 353.9 ± 42.3 μm였다[21]. "
 "해수(35‰)에서 담수로 옮긴 실험에서는 12–72시간 사이 혈장 나트륨·염소·삼투질 농도가 떨어졌다가 96시간에 안정되었다[24]. "
 "1981년 연구에서 2–6개월 굶긴 개체는 간 크기가 줄었지만 간·근육 1 g당 지질 함량은 늘었고, 지방산 합성의 주된 장소는 간으로 판단되었다[30].")
sec["related_species"] = ("유럽뱀장어(A. anguilla)와 이 종은 겉모습으로는 거의 구별되지 않는 자매종이다[6]. "
 "핵 18S rDNA의 진단용 단일염기다형성(SNP)으로 두 종과 그 잡종을 구별하는 방법이 제시되었다[7]. "
 "대만 연구는 미토콘드리아 시토크롬 b 유전자 362 bp를 PCR로 증폭한 뒤 제한효소 HinfI로 자르면 뱀장어(A. japonica)와 이 종을 구별할 수 있다고 보고했다[8]. "
 "같은 연구에서 시판 구운 장어 제품 12점은 뱀장어 9점, 유럽뱀장어 2점, 이 종 1점으로 판별되었다[8].\n\n"
 "세계 시장 조사에서는 시토크롬 b 약 1000 bp를 증폭·염기서열 분석해 99.8% 넘는 일치도로 종을 판정했다[2]. "
 "이 조사에서 종명이 표시된 제품 20점(이 종 13점, 뱀장어 7점)은 모두 표시와 판별 결과가 일치했다[2]. "
 "국내에 유통되는 수입 장어를 식약처나 수산 당국이 종 판별한 이 종 단독 결과는 공식 자료에서 확인하지 못함. "
 "식품원료 목록에서 이 종은 '북아메리카 장어'로만 올라 있고 별칭은 적혀 있지 않다[1].")
sec["cultivation"] = ("장어류는 인공 종자 생산이 실험실 수준에 머물러 있어, 양식은 자연에서 잡은 실뱀장어를 길러서 한다[2]. "
 "중국 장어 양식 생산의 74%를 이 종이 차지한다고 보고되었다[22]. "
 "중국의 상업 순환여과식 양식장 시험에서는 수온 27–30 ℃에서 평균 2.33 g의 치어를 56일 길렀다[22]. "
 "사료에 섞인 히스타민은 이 종의 성장을 떨어뜨리며, 10주 사육 결과 최대 허용 사료 히스타민 농도는 260.11 mg/kg으로 추정되었다[23].\n\n"
 "질병은 양식의 큰 문제다[16, 19, 20]. "
 "중국 양식 개체에서 분리한 장어 헤르페스바이러스 1형(AngHV-1)은 감염 실험에서 이환율 100%, 폐사율 13.3%를 보였다[16]. "
 "출혈성 아가미 괴사병 시료에서는 새 오르토레오바이러스가 분리되었고 양식 개체의 감염률은 32.3%였다[19]. "
 "미국에서 수입한 실뱀장어에서 기생체 Dermocystidium anguillae가 검출되어, 이 병원체가 종묘와 함께 중국에 들어왔다고 추정되었다[18]. "
 "신장에 패혈증을 일으키는 Vibrio harveyi 감염 실험에서는 감염 48시간에 세균량이 12시간보다 100배 많았고 신장 손상이 심했다[20]. "
 "국내 연구기관(전남대학교·국립수산과학원)은 캐나다에서 수입된 이 종에서 분리한 AngHV-1 변이주의 전장 유전체를 보고했다[17]. "
 "국내 장어 양식의 80% 이상은 뱀장어이고 이 종은 약 1%라는 한국 정부 보고가 인용되었다[2]. "
 "국내 이 종만의 양식 생산 통계는 공식 자료에서 확인하지 못함.")
sec["processing"] = ("양식한 장어는 대개 양식장 가까이에서 가공되며, 세계 시장 조사에서 소매 제품 224점의 표시 원산지는 중국 68%, 일본 25%, 대만 1%였다[2]. "
 "미국과 캐나다에서 산 장어 제품은 80% 넘게 이 종이었고, 원산지가 표시된 제품은 모두 중국산이었다[2]. "
 "열처리·냉동·멸균 뒤에도 시토크롬 b 유전형이 달라지지 않아 구운 장어 같은 가공품도 DNA로 종을 판별할 수 있다[8].\n\n"
 "가공 부산물 활용 연구도 있다[15]. "
 "이 종의 가공 부산물 단백질을 프로타멕스 효소로 분해한 가수분해물은 DPP-IV 저해 활성(IC50 5.455 ± 0.24 mg/mL)을 보였다[15]. "
 "여기서 분리한 펩타이드 Phe-Pro-Arg·Tyr-Pro-Pro-Ser-Phe-Ser·Tyr-Pro-Tyr-Pro-Ala-Ser의 IC50은 각각 62.14, 102.65, 68.30 μM이었다[15]. "
 "이 결과는 시험관·분자 도킹 수준이며 사람에서의 효과는 확인하지 못함. "
 "북미에서는 상업 어획 개체를 가공 공장에서 검사해 질병 상태를 조사한 사례가 있다[25]. "
 "이 종을 원료로 한 국내 건강기능식품 생산실적은 확인하지 못함.")
sec["genetics"] = ("이 종의 첫 초안 유전체는 전체 1.41 Gb로, 콘티그 305,043개(N50 7,397)와 스캐폴드 79,209개(N50 86,641)로 조립되었고 유전자 26,564개가 주석되었다[3]. "
 "같은 연구는 북대서양·동아시아 장어 세 종의 후보 유전자를 비교해 뱀장어(A. japonica)가 가장 많이 갈라져 있음을 보였다[3].\n\n"
 "12개 지점 710개체의 SNP 12,098개를 분석한 연구는 공간에 따라 달라지는 선택이 유전체의 약 1.5%에 작용하며, 관련 유전자가 인슐린 신호 경로에 몰려 있다고 보고했다[4]. "
 "북대서양 두 장어 359개체의 RAD 자료를 비교한 연구는 특히 6번과 10번 염색체에서 분화 섬을 찾았다[6]. "
 "오염 지역과 대조 지역 개체를 비교한 RAD 분석에서 이 종은 14,755개 좌위가 쓰였고, PCB153·4,4'-DDE·셀레늄이 선택 요인으로 지목되었다[26]. "
 "캐나다 북동부 72개체의 전장 바이설파이트 분석에서는 DNA 메틸화 양상이 지리와, 그보다 약하게 염분과 연관되었다[5]. "
 "중국 연구진은 이 종의 IgM 중쇄 불변 부위(1326 bp, 441 아미노산)를 클로닝하고 단클론항체를 만들어 백신 연구 도구로 제시했다[28].")
sec["safety"] = ("식약처 「식품원료 목록」에서 이 종은 별도 조건 없는 '사용가능' 수산물 원료이고, 건강기능식품 고시형 원료가 아니어서 고시 섭취 시 주의사항은 없다[1]. "
 "이 종을 따로 다룬 국내 공공기관의 알레르기·잔류 동물용의약품(말라카이트그린 등) 검사 결과는 이번 조사에서 확인하지 못함.\n\n"
 "서식지 오염이 근육에 쌓일 수 있다[9, 10, 11]. "
 "미국 메인주 페노브스콧강 하류의 염소-알칼리 공장 영향 지역에서 이 종 근육의 총수은 평균은 521 ng/g 습중량으로 메인주 수은 조치 기준 200 ng/g을 넘었다[10]. "
 "푸에르토리코 도시 하천의 이 종은 PCB 0.019–0.031 ppm(습중량), 디엘드린 최대 0.024 ppm으로 미국 환경보호청 섭취 권고 한계를 넘었다[11]. "
 "카드뮴·수은·셀레늄 농도는 몸집과 나이가 클수록 높았다[9]. "
 "반면 온타리오호 개체 추출물에서는 다이옥신 유사 독성이 나타나지 않았고, 세인트로렌스강 이 종에서는 잔류성 유기오염물질이 생체지표에 뚜렷한 영향을 주지 않았다[12, 27]. "
 "미국 케이프코드의 소방 훈련장 하류 개체 전신에서 추출성 유기불소는 실험실 간 평균 266 ± 70 μg F/kg 습중량이었고, 그 대부분(약 83%)이 과불화알킬산이었다[13]. "
 "암컷화 목적으로 17β-에스트라디올을 투여한 치어 근육의 잔류량은 하루 약 50%씩 줄어 5일 뒤 대조군 수준으로 돌아왔다[14]. "
 "AngHV-1 등 양식 장어 병원체가 사람에게 해롭다는 자료는 확인하지 못함.")
TITLES = {"overview": "한눈에 보기", "history": "이용 역사·보호 지위", "biology": "어종·생활사", "related_species": "관련 종·종 판별",
 "cultivation": "양식·어획", "processing": "가공·유통·부산물 연구", "genetics": "유전 정보", "safety": "안전성·오염물질"}

def C(name, ko, cls, role, part, content, act, src):
    return {"name": name, "name_ko": ko, "class": cls, "role": role, "part": part, "content_text": content, "activity_ko": act, "source": src}
compounds = [
 C("Mercury", "총수은", "중금속 오염물질", "bioactive", "근육", "521 (95% CI 480–566) ng/g 습중량 — 미국 페노브스콧강 하류 최다 오염 구역, 크기·나이 보정 평균, 2006–2012년[10]", "메인주 수은 조치 기준(200 ng/g 습중량)을 넘어 사람 건강 우려 수준으로 평가됨[10]", [10]),
 C("Polychlorinated biphenyls", "폴리염화비페닐(PCB)", "잔류성 유기오염물질", "bioactive", "근육(가식부)", "0.019–0.031 ppm 습중량 — 푸에르토리코 도시 하천 지점, 2009–2010년[11]", "미국 환경보호청 월 1회 섭취 한계를 넘음[11]", [11]),
 C("Dieldrin", "디엘드린", "유기염소계 농약", "bioactive", "근육(가식부)", "검출한계 미만–0.024 ppm 습중량 — 푸에르토리코 도시 하천 지점[11]", "미국 환경보호청 최대 허용 섭취 한계를 넘음[11]", [11]),
 C("PCB 153", "PCB153", "잔류성 유기오염물질", "bioactive", "개체(오염 측정)", "개체별 수치는 초록에 없음 — 오염 지역 개체의 선택 요인으로 지목[26]", "유전체 변이와 연관된 주요 선택 요인 후보[26]", [26]),
 C("Cadmium", "카드뮴", "중금속", "bioactive", "간·신장·근육", "개별 수치는 초록에 없음 — 몸집·나이가 클수록 조직 농도 증가[9]", "가장 오염된 지점 개체의 건강 위험 요인으로 평가됨[9]", [9]),
 C("Extractable organofluorine", "추출성 유기불소(EOF)", "과불화화합물 총량 지표", "bioactive", "전신(20개체 혼합)", "실험실 간 평균 266 ± 70 μg F/kg 습중량(최소 119, 최대 869); 이상치 실험실 제외 시 208 ± 42 μg F/kg — 미국 케이프코드 AFFF 오염 하천, 2021년[13]", "과불화알킬산(PFAA)이 EOF의 약 83%를 차지[13]", [13]),
 C("Perfluoroalkyl acids", "과불화알킬산(PFAA)", "과불화화합물", "bioactive", "전신(20개체 혼합)", "EOF 대비 실험실 간 평균 83%(표준편차 범위 61–140%)[13]", "이 시료의 유기불소 대부분을 설명함[13]", [13]),
 C("Estradiol", "17β-에스트라디올(E2)", "스테로이드 호르몬", "bioactive", "근육", "암컷화 처리 뒤 하루 약 50%씩 감소, 처리 5일 뒤 비처리 대조군 수준(수치는 초록에 없음)[14]", "양식 암컷화 처리의 잔류 감시 대상[14]", [14]),
 C("Phe-Pro-Arg", "펩타이드 FPR", "펩타이드", "bioactive", "가공 부산물 단백질 가수분해물", "DPP-IV 저해 IC50 62.14 ± 1.47 μM(합성 펩타이드)[15]", "경쟁적 DPP-IV 저해(시험관)[15]", [15]),
 C("Tyr-Pro-Pro-Ser-Phe-Ser", "펩타이드 YPPSFS", "펩타이드", "bioactive", "가공 부산물 단백질 가수분해물", "DPP-IV 저해 IC50 102.65 ± 4.57 μM(합성 펩타이드)[15]", "경쟁적 DPP-IV 저해(시험관)[15]", [15]),
 C("Tyr-Pro-Tyr-Pro-Ala-Ser", "펩타이드 YPYPAS", "펩타이드", "bioactive", "가공 부산물 단백질 가수분해물", "DPP-IV 저해 IC50 68.30 ± 3.85 μM(합성 펩타이드)[15]", "혼합형(경쟁·비경쟁) DPP-IV 저해(시험관)[15]", [15]),
 C("Histamine", "히스타민", "생체 아민", "bioactive", "사료(이 종 사육 시험)", "최대 허용 사료 히스타민 260.11 mg/kg; 355.31 mg/kg 초과 시 성장 저하[23]", "이 종은 사료 히스타민에 약한 어종으로 소개됨(사람 섭취 기준 아님)[23]", [23]),
]
E = {k: "" for k in ["instrument","column","mobile_phase","gradient","flow","temp","detection","injection","sample_prep","standard","linearity","lod","loq","recovery"]}
def cond(**kw):
    d = dict(E); d.update(kw); return d
assays = [
 {"role": "literature", "compound": "Extractable organofluorine (EOF) and PFAS", "compound_ko": "추출성 유기불소·과불화화합물", "part": "전신(20개체 혼합 균질물)",
  "content": "EOF 266 ± 70 μg F/kg 습중량(7개 실험실 평균), 이상치 제외 208 ± 42 μg F/kg; PFAA가 EOF의 약 83% [13]",
  "method": "연소 이온크로마토그래피(CIC, EOF) + LC-MS/MS(표적 PFAS 28–45종)",
  "conditions": cond(instrument="EOF: CIC(실험실별 기기, 세부는 보충자료); PFAS: Agilent 6495·Agilent 6460·Waters Xevo TQ-S 삼중사중극자 LC-MS/MS",
   detection="PFAS: 음이온 전자분무, 다중반응감시(MRM)",
   sample_prep="습중량 1 g에 아세토니트릴 4 mL 가해 볼텍스·초음파 30분·원심분리, 2회 반복(합 8 mL) → −20 °C에서 4시간 이상 냉동해 지질 침전 → 질소 농축 후 메탄올 재용해 → ENVI-carb 정제 → CIC와 LC-MS/MS로 분할",
   standard="유기불소 회수 시험용 PFAS 혼합물 Wellington PFAC-24PAR(24종), 무기불소 제거 시험용 불화나트륨",
   lod="장어: 기기 검출한계 1 μg F/kg; 방법 보고한계 13–50 μg F/kg; 방법 검출한계 19–84 μg F/kg(실험실별)",
   recovery="PFAS 혼합물(1200 μg F/kg) 첨가 회수율: 5개 실험실 중 3곳 ±30% 이내, 2곳 ±40% 이내"),
  "rationale": "AFFF(수성막포 소화약제) 오염 지역에서 이 종은 지방이 많고 북미 동부에 흔한 회유성 어종이어서 생물 시료로 골랐다고 적혀 있다. PMC 전문 Methods에서 확인했다[13].",
  "source": [13], "url": "https://doi.org/10.1021/acs.est.3c04560", "source_kind": "paper"},
 {"role": "literature", "compound": "17β-Estradiol, estrone, estriol", "compound_ko": "에스트라디올·에스트론·에스트리올", "part": "근육",
  "content": "E2 투여 뒤 근육 E2가 하루 약 50%씩 감소, 5일 뒤 대조군 수준 [14]",
  "method": "LC-차등이온이동도(DMS)-MS/MS, 음이온 SRM",
  "conditions": cond(detection="음이온 모드 선택반응감시(SRM), 전자분무 이온화 + 차등이온이동도 분광"),
  "rationale": "양식에서 장어 암컷화에 에스트라디올을 쓰려는 계획이 있어 식품 규제 기관 요건에 맞춘 잔류 감시 지표로 개발되었다. 초록만 확인했고 전문 확인 못함(칼럼·이동상·검출한계는 비움)[14].",
  "source": [14], "url": "https://doi.org/10.1002/rcm.7853", "source_kind": "paper"},
 {"role": "literature", "compound": "DPP-IV inhibitory peptides (FPR, YPPSFS, YPYPAS)", "compound_ko": "DPP-IV 저해 펩타이드", "part": "가공 부산물 단백질 효소 가수분해물",
  "content": "가수분해물 IC50 5.455 ± 0.24 mg/mL; FPR 62.14, YPPSFS 102.65, YPYPAS 68.30 μM [15]",
  "method": "한외여과 → 겔여과 → RP-HPLC 분획, MALDI-TOF/TOF MS/MS 서열 동정",
  "conditions": cond(),
  "rationale": "부산물 가수분해물의 혈당 관련 효소(DPP-IV) 저해 활성을 이끄는 성분으로 동정되었다. 초록만 확인했고 전문 확인 못함[15].",
  "source": [15], "url": "https://doi.org/10.1002/jsfa.12462", "source_kind": "paper"},
]
world = [
 {"country": "세계(11개국·지역 시장 통합 추정)", "metric": "consumption_share_pct", "year": 2022, "value": 75.3, "unit": "%", "note": "2020–2022 평균 국내 공급량을 DNA 판별 종 조성으로 가중한 이 종의 비중(FAO 자료 기준); 비공식협의체 자료 기준으로는 52.7%", "source": [2]},
]
d = {"slug": "anguilla-rostrata", "name_ko": "북아메리카 장어", "name_en": "American eel", "scientific_name": "Anguilla rostrata",
     "aliases": ["American eel"],
     "sections": [{"key": k, "title": TITLES[k], "body": sec[k]} for k in ["overview","history","biology","related_species","cultivation","processing","genetics","safety"]],
     "compounds": compounds, "markers": [], "assays": assays, "nutrients": [], "production": [], "gi": [], "orgs": [], "world": world, "sources": S}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for k in sec: print(k, len(sec[k]))
