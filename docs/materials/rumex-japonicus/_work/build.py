import json
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "dossier.json"
ACC = "2026-11-02"


def pm(n, title, pmid, doi=None, pmc=None, pub=""):
    url = f"https://doi.org/{doi}" if doi else f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
    t = title + (f" ({pmc})" if pmc else "")
    p = (pub + " " if pub else "") + f"(PubMed PMID {pmid})"
    return {"n": n, "title": t, "url": url, "publisher": p.strip(), "accessed": ACC}


sources = [
    {"n": 1, "title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 참소리쟁이잎(Rumex japonicus Houtt.) 및 같은 속 원료 행(2026-10-13 내려받은 원자료)",
     "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
    pm(2, "Potential of Rumex japonicus Houtt. in alkaline soil management. Sci Rep 2026 (전문 확인)", "42098222", "10.1038/s41598-026-52219-x", "PMC13342501", "Nature Portfolio (PubMed Central)"),
    pm(3, "Rumex japonicus Houtt. leaves: the chemical composition and anti-fungal activity. J Mycol Med 2024:101513 (초록 확인)", "39500231", "10.1016/j.mycmed.2024.101513", None, "Elsevier"),
    pm(4, "Study on the chemical composition and anti-fungi activities of anthraquinones and its glycosides from Rumex japonicus Houtt. J Nat Med 2024 (초록 확인)", "39103726", "10.1007/s11418-024-01834-x", None, "Springer"),
    pm(5, "Study on HPLC Fingerprint, Network Pharmacology, and Antifungal Activity of Rumex japonicus Houtt. J AOAC Int 2022 (초록 확인)", "35876857", "10.1093/jaoacint/qsac079", None, "Oxford University Press"),
    pm(6, "Antioxidant and antibacterial activities of Rumex japonicus HOUTT. aerial parts. Biol Pharm Bull 2005;28(12):2225-30 (초록 확인)", "16327154", "10.1248/bpb.28.2225", None, "일본약학회"),
    pm(7, "Molecular evidence for natural hybridization between Rumex crispus and R. obtusifolius (Polygonaceae) in Korea. Sci Rep 2022;12:5423 (전문 확인)", "35361815", "10.1038/s41598-022-09292-9", "PMC8971494", "Nature Portfolio (PubMed Central)"),
    pm(8, "The complete plastome sequence of Rumex japonicus Houtt.: a medicinal plant. Mitochondrial DNA B Resour 2020;5(1) (초록 확인)", "33366591", "10.1080/23802359.2019.1704194", "PMC7748881", "Taylor & Francis"),
    pm(9, "Complete plastome sequence of Rumex japonicus (Polygonaceae) in Dok-do Island, Korea. Mitochondrial DNA B Resour 2019;4(2):2892-2893 (초록 확인)", "33365778", "10.1080/23802359.2019.1660274", "PMC7706998", "Taylor & Francis"),
    pm(10, "Rumex japonicus Houtt.: A phytochemical, pharmacological, and pharmacokinetic review. Phytother Res 2020;34(6):1198-1215 (초록 확인)", "31849133", "10.1002/ptr.6601", None, "Wiley"),
    pm(11, "Evaluation of raw nepodin extraction from Rumex japonicus and R. obtusifolius and their DNA polymorphisms. J Nat Med 2018;72(1):369-374 (초록 확인)", "29063361", "10.1007/s11418-017-1143-0", None, "Springer"),
    pm(12, "Oxanthrone C-glycosides and epoxynaphthoquinol from the roots of Rumex japonicus. Phytochemistry 2007;68(19):2444-9 (초록 확인)", "17603087", "10.1016/j.phytochem.2007.05.032", None, "Elsevier"),
    pm(13, "24-nor-Ursane type triterpenoids from the stems of Rumex japonicus. Chem Pharm Bull 2005;53(12):1594-6 (초록 확인)", "16327198", "10.1248/cpb.53.1594", None, "일본약학회"),
    pm(14, "Effects of compounds isolated from the fruits of Rumex japonicus on the protein glycation. Chem Biodivers 2008;5(12):2718-23 (초록 확인)", "19089830", "10.1002/cbdv.200890226", None, "Wiley"),
    pm(15, "Rumex japonicus Houtt. Protects Dopaminergic Neurons by Regulating Mitochondrial Function and Gut-Brain Axis in In Vitro and In Vivo Models of Parkinson's Disease. Antioxidants (Basel) 2022;11(1):141 (전문 확인)", "35052645", "10.3390/antiox11010141", "PMC8772800", "MDPI (PubMed Central)"),
    pm(16, "Rumex japonicus Houtt. alleviates dextran sulfate sodium-induced colitis by protecting tight junctions in mice. Integr Med Res 2020;9(2):100398 (초록 확인)", "32322483", "10.1016/j.imr.2020.02.006", "PMC7168767", "Elsevier"),
    pm(17, "Rumex japonicus Houtt. Extract Suppresses Colitis-Associated Colorectal Cancer by Regulating Inflammation and Tight-Junction Integrity in Mice. Front Pharmacol 2022;13:946909 (초록 확인)", "35865942", "10.3389/fphar.2022.946909", "PMC9294457", "Frontiers"),
    pm(18, "Bactericidal and antibiofilm properties of Rumex japonicus Houtt. on multidrug-resistant Staphylococcus aureus isolated from milk. J Dairy Sci 2022 (초록 확인)", "34955261", "10.3168/jds.2021-21221", None, "Elsevier"),
    pm(19, "Study on the purification mechanism for ammonia nitrogen in micro-polluted rivers by herbaceous plant - Rumex japonicus Houtt. Chemosphere 2024:142154 (초록 확인)", "38679183", "10.1016/j.chemosphere.2024.142154", None, "Elsevier"),
    pm(20, "Effects of plant diversity on greenhouse gas emissions in microcosms simulating vertical constructed wetlands with high ammonium loading. J Environ Sci (China) 2019;77:229-237 (초록 확인)", "30573087", "10.1016/j.jes.2018.08.001", None, "Elsevier"),
    pm(21, "Differential expression of acid invertase genes in roots of metallicolous and non-metallicolous populations of Rumex japonicus under copper stress. Chemosphere 2011;84(10):1432-9 (초록 확인)", "21555144", "10.1016/j.chemosphere.2011.04.053", None, "Elsevier"),
    {"n": 22, "title": "EFSA ANS Panel. Safety of hydroxyanthracene derivatives for use in food. EFSA Journal 2018;16(1):e05090",
     "url": "https://doi.org/10.2903/j.efsa.2018.5090", "publisher": "유럽식품안전청(EFSA)", "accessed": ACC},
    pm(23, "Herbicidal activity of formulated sorgoleone, a natural product of sorghum root exudate. Pest Manag Sci 2014;70(2):252-7 (초록 확인)", "23785031", "10.1002/ps.3550", None, "Wiley"),
    pm(24, "Flavonoid constituents in leaves of Rumex acetosa Linnaeus and R. japonicus Houttuyn. Chem Pharm Bull 1965;13(12):1470-1 (제목만 확인, 초록 없음)", "5866246", "10.1248/cpb.13.1470", None, "일본약학회"),
    pm(25, "Preparative isolation of three anthraquinones from Rumex japonicus by high-speed counter-current chromatography. Molecules 2011;16(2):1201-10 (초록 확인)", "21273951", "10.3390/molecules16021201", "PMC6259845", "MDPI"),
    pm(26, "Anti-proliferative of physcion 8-O-β-glucopyranoside isolated from Rumex japonicus Houtt. on A549 cell lines via inducing apoptosis and cell cycle arrest. BMC Complement Altern Med 2014;14:377 (초록 확인)", "25283233", "10.1186/1472-6882-14-377", "PMC4201690", "BioMed Central"),
    pm(27, "In vivo and in vitro anti-sepsis effects of physcion 8-O-β-glucopyranoside extracted from Rumex japonicus. Chin J Nat Med 2017;15(7):534-539 (초록 확인)", "28807227", "10.1016/S1875-5364(17)30079-1", None, "Elsevier"),
    pm(28, "Inhibitory effects of Rumex japonicus Houtt. on the development of atopic dermatitis-like skin lesions in NC/Nga mice. Br J Dermatol 2006;155(1):33-8 (초록 확인)", "16792749", "10.1111/j.1365-2133.2006.07303.x", None, "Wiley"),
    pm(29, "Inhibition of Biofilm Formation by Candida albicans and Polymicrobial Microorganisms by Nepodin via Hyphal-Growth Suppression. ACS Infect Dis 2019;5(7):1177-1187 (초록 확인)", "31055910", "10.1021/acsinfecdis.9b00033", None, "American Chemical Society"),
    pm(30, "Inhibitory effect of Rumex japonicus Houtt on the porphyrin photooxidative reaction. J Dermatol 2000;27(12):761-8 (초록 확인)", "11211791", "10.1111/j.1346-8138.2000.tb02278.x", None, "Wiley"),
    pm(31, "Inhibition of Jurkat T Cell Proliferation by Active Components of Rumex japonicus Roots Via Induced Mitochondrial Damage and Apoptosis Promotion. J Microbiol Biotechnol 2020;30(12) (초록 확인)", "33144550", "10.4014/jmb.2007.07018", "PMC9728342", "한국미생물생명공학회"),
    pm(32, "The Hair Growth-Promoting Effect of Rumex japonicus Houtt. Extract. Evid Based Complement Alternat Med 2016:1873746 (초록 확인)", "27974900", "10.1155/2016/1873746", "PMC5128716", "Hindawi"),
    pm(33, "Plant species diversity reduces N2O but not CH4 emissions from constructed wetlands under high nitrogen levels. Environ Sci Pollut Res Int 2017;24(6):5938-5948 (초록 확인)", "28070812", "10.1007/s11356-016-8288-3", None, "Springer"),
]

sections = [
    {"key": "overview", "title": "한눈에 보기", "body":
     "참소리쟁이(Rumex japonicus Houtt.)는 마디풀과(Polygonaceae) 소리쟁이속의 여러해살이풀로, 중국·한국·일본과 러시아 극동 등 동북아시아에 널리 자란다[2][7]. 영어 이름은 'Northeast Asian curly dock'으로 목록에 적혀 있고, 중국에서는 '양제(羊蹄, Yang Ti)'라 부르는 민간 약초다[1][10].\n\n"
     "식품의약품안전처 「식품원료 목록」에서 참소리쟁이는 원료명 '참소리쟁이잎'으로 올라 있는 식품원료(사용가능)이며, 사용 조건은 '사용가능부위 : 잎'이다[1]. 목록에는 이명 Rumex crispus subsp. japonicus (Houtt.) Kitam.과 다른 이름 '소리쟁이'·'참송구지'가 함께 적혀 있다[1]. 그런데 목록의 '소리쟁이잎' 등은 다른 종인 Rumex crispus의 원료이므로, 이름만 보고 두 종을 섞지 않도록 학명으로 구별해야 한다[1]. 건강기능식품 고시형 원료의 원재료로 쓰인다는 기록은 확인하지 못함.\n\n"
     "연구는 대부분 뿌리의 안트라퀴논(에모딘·크리소파놀·피스시온 등)과 나프탈렌 화합물 네포딘을 다룬 약재 연구다[10][11][25]. 식품 부위인 잎과 지상부에서도 에모딘·레인·알로에에모딘 같은 안트라퀴논과 루틴·퀘르세틴 등 페놀 성분이 보고되었다[2][3][6]. 이 자료의 뿌리 연구 결과는 잎을 먹었을 때의 효과로 볼 수 없다[1][10]."},
    {"key": "history", "title": "역사", "body":
     "참소리쟁이는 동아시아에서 오래도록 민간약으로 쓰여 왔고, 2019년 종설은 이를 '수천 년'의 사용으로 정리했다[10]. 말린 뿌리는 변비·황달·토혈·기능성 자궁 출혈과 위장 질환에 전통적으로 쓰였다고 한다[15][16]. 옴(scabies)과 황달 치료에 썼다는 기록도 있다[31].\n\n"
     "피부병 치료 쓰임새가 특히 두드러진다[28][30][32]. 일본 오키나와에서는 지역 주민이 급성·만성 피부 질환에 써 온 토착 식물로 소개되었고, 한국에서도 피부 질환에 쓰는 약용 식물로 전해진다[30][32]. 중국 연구진은 옛 문헌에 피부사상균증(백선) 치료 효과가 기록되어 있다고 적었다[4].\n\n"
     "이처럼 전통 쓰임새의 기록은 주로 뿌리를 약으로 쓴 것이다[15][16][31]. 잎을 나물 등 식품으로 먹어 온 국내 전통이나 고문헌 기록은 이번 조사에서 공공기관·학술 자료로 확인하지 못함. 지상부는 가축 사료로도 영양가가 높다고 소개되었다[2]."},
    {"key": "biology", "title": "식물학적 특징", "body":
     "참소리쟁이는 동아시아와 러시아에 분포하는 여러해살이풀로, 해발 30–3,400 m의 습지·강가·도랑에 자연적으로 자란다[2]. 분포 지역에서는 소리쟁이(R. crispus)나 돌소리쟁이(R. obtusifolius)와 따로, 또는 셋이 한곳에 함께 자라기도 한다[7]. 잎은 피침형에서 거꿀피침형으로 소리쟁이와 비슷하지만, 열매를 싸는 꽃덮이 조각(valve)이 콩팥꼴 또는 넓은 오각형이고 가장자리에 불규칙하고 얕은 톱니가 있어 구별된다[7].\n\n"
     "화분 시험에서 알칼리성 흙(pH 8.25)에 심은 개체는 중성 흙(pH 7.23)보다 최대 잎 길이·잎 너비·뿌리 표면적이 컸고, 지상부 생물량도 줄지 않았다[2]. 중국의 미세 오염 하천 실험에서는 암모니아성 질소를 최대 100% 제거했고, 그 제거의 약 74%(73.85% ± 8.79%)는 뿌리의 질산화 작용 몫이었다[19].\n\n"
     "구리 광산 등 금속 오염지에 사는 집단은 구리 20 µM 수경 처리에서 비오염지 집단보다 뿌리 길이와 생물량이 컸다[21]. 수수 뿌리 분비물인 소르골레온을 제초제로 만든 시험에서는 1 ha당 유효성분 0.4 kg에서 참소리쟁이의 생장이 완전히 억제되어, 밭에서는 잡초로도 다뤄진다[23]."},
    {"key": "related_species", "title": "근연종", "body":
     "소리쟁이속(Rumex)은 약 200종으로 이루어지며 종 사이 잡종이 흔하다[7]. 한국에는 소리쟁이속 12종이 보고되어 있다[7]. 식약처 식품원료 목록에는 소리쟁이(R. crispus)·수영(R. acetosa)·애기수영·돌소리쟁이·금소리쟁이·Rumex patientia 등 같은 속 원료가 따로 올라 있으며, 이 자료에는 그 종들의 성분·안전성 값을 섞지 않았다[1].\n\n"
     "국내 소리쟁이×돌소리쟁이 잡종 연구에서 참소리쟁이의 핵 DNA(pgiC) 클론은 2–3가지 서열형을 지녔고 그중 하나를 소리쟁이와 공유했다[7]. 연구진은 이를 근거로 한국의 참소리쟁이 집단이 잡종 기원일 가능성이 크고 소리쟁이가 부모 가운데 하나일 수 있다고 보았으나, 검증은 추가 연구 과제로 남겼다[7]. 같은 연구는 참소리쟁이의 고유 단상형 상당수가 잡종 개체에서 나오지 않아, 참소리쟁이가 그 잡종의 부모였을 가능성은 낮다고 판단했다[7].\n\n"
     "일본 류큐 열도 표본은 모두 참소리쟁이, 일본 본토 표본은 모두 돌소리쟁이로 동정되었고, 꽃덮이 조각 형태에 따른 동정은 엽록체 trnL–trnF 구간과 핵 ITS 서열과 일치했다[11]. 연구진은 원료 오동정을 막기 위해 두 종을 가르는 DNA 표지 개발을 권했다[11]. 엽록체 전장 유전체를 쓴 계통 분석으로 참소리쟁이의 속 안 계통상 위치가 보고되었으나, 가장 가까운 종의 이름은 초록에서 확인하지 못함[8][9]."},
    {"key": "cultivation", "title": "재배와 채취", "body":
     "참소리쟁이를 작물로 재배한 국내 생산 통계(면적·생산량)는 확인하지 못함. 오키나와(류큐 열도)에서는 뿌리의 네포딘을 얻기 위한 재배 원료로 검토되었고, 연구진은 고유 유전 특성을 지키려면 그 지역에서는 돌소리쟁이가 아닌 참소리쟁이만 재배해야 한다고 권했다[11].\n\n"
     "중국 화분 시험에서는 모래에서 싹 틔워 잎이 3장 났을 때 화분으로 옮겨 25 °C, 12시간 명기로 길렀고, 17일 간격 8단계로 시료를 거두었다[2]. 마지막 단계(S7)에서 생물량이 가장 컸고 지상부 에모딘 함량도 높아, 연구진은 약재 추출과 사료 이용 모두에 S7 수확이 알맞다고 보았다[2]. 알칼리성 흙에서 S7 뿌리의 피스시온 함량은 58.21% 늘었다[2].\n\n"
     "참소리쟁이를 심은 흙에서는 총질소와 카탈레이스·알칼리성 인산분해효소·우레이스 활성이 높아졌다[2]. 고암모늄 폐수를 처리하는 인공습지 모형에서는 참소리쟁이가 있는 식물군락의 아산화질소 배출이 없는 군락보다 62% 적었다[20]. 다른 인공습지 실험에서는 참소리쟁이가 있으면 폐수의 총무기질소(TIN) 등 질소 농도가 낮아졌지만 아산화질소·메테인 배출에는 영향이 없었다[33]."},
    {"key": "processing", "title": "가공과 이용", "body":
     "식품원료 목록에 오른 참소리쟁이 원료는 '참소리쟁이잎' 하나이며, 사용 부위는 잎으로 한정된다[1]. 식약처 「식품 등의 생산실적」에서 참소리쟁이 원료 품목의 생산 기록은 확인하지 못함.\n\n"
     "잎을 산 추출·알코올 침전으로 처리해 에모딘·레인·알로에에모딘(안트라퀴논), 페룰산·p-쿠마르산(페놀산), 루틴·퀘르세틴(플라보노이드) 7개 단일 성분을 얻었다[3]. 잎 추출물은 시험관에서 칸디다와 백선균 2종을 억제했으며 최소억제농도는 1.96–62.50 µg/mL였다[3]. 지상부를 에틸아세테이트로 추출하면 페놀 함량과 항산화 활성이 가장 높았고, 주된 페놀은 피로갈롤이었다[6]. 잎의 플라보노이드 성분은 1965년에도 수영 잎과 함께 보고되었으나 내용은 초록이 없어 확인하지 못함[24].\n\n"
     "뿌리는 메탄올로 추출해 동결 건조한 가루(수율 12.74%)를 동물 실험에 썼고, 이 추출물에서 에모딘·피스시온-8-O-β-글루코피라노사이드 등 안트라퀴논 8종이 확인되었다[15]. 다이클로로메테인 추출물을 고속 역류 크로마토그래피로 분리하면 시료 500 mg에서 에모딘 3.4 mg, 크리소파놀 24.1 mg, 피스시온 2.0 mg을 순도 98% 이상으로 얻었다[25]. 5년생 시료 10개 배치의 HPLC 지문 분석에서는 루틴·퀘르세틴·알로에에모딘·네포딘·에모딘·크리소파놀 등 10개 특징 피크를 포함한 공통 피크 18개가 확인되었으나, 분석 부위는 초록에서 확인하지 못함[5]. 이런 뿌리 추출물의 대장염·파킨슨병·아토피 피부염 모델 결과는 모두 동물·세포 실험이며, 식품인 잎과는 부위가 다르다[15][16][17][28]."},
    {"key": "genetics", "title": "유전체와 유전 다양성", "body":
     "참소리쟁이의 엽록체 전장 유전체는 159,292 bp로, 역반복 구간 2개(각 30,629 bp), 큰 단일복사 구간 85,028 bp, 작은 단일복사 구간 13,006 bp로 이루어지며 고유 유전자 112개(단백질 78, tRNA 30, rRNA 4)를 지닌다[8]. 독도에서 채집한 개체의 엽록체 유전체는 159,223 bp, GC 함량 37.5%, 유전자 131개(단백질 83, tRNA 38, rRNA 8)로 보고되었다[9]. 두 보고의 유전자 수가 다른 까닭(세는 방식 차이 여부)은 초록에서 확인하지 못함[8][9].\n\n"
     "국내 혼생 집단 연구에서 참소리쟁이는 엽록체 단상형 2개(C1, C6)를 지녔고, 그중 C1은 소리쟁이 및 일부 잡종 개체와 공유되었다[7]. 핵 pgiC 구간에서는 단상형 4개(N1, N2, N4, N5)가 나왔고, 클론한 5개체가 각각 2–3가지 서열형을 지녀 잡종 기원 가설의 근거가 되었다[7].\n\n"
     "일본 시료에서는 엽록체 trnL–trnF 구간과 핵 ITS 일부 서열이 꽃덮이 조각 형태에 따른 참소리쟁이·돌소리쟁이 동정과 일치했다[11]. 정확한 염색체 수와 핵 유전체 조립본은 이번 조사에서 확인하지 못함."},
    {"key": "safety", "title": "안전성", "body":
     "건강기능식품 고시형 원료가 아니어서 고시 섭취 주의사항은 확인하지 못함. 식품원료 목록상 쓸 수 있는 부위는 잎뿐이다[1]. 국내 공공기관의 알레르기·잔류농약 정보는 확인하지 못함.\n\n"
     "소리쟁이속 잎은 옥살산이 많은 것으로 알려져 있으나, 참소리쟁이 잎의 옥살산 함량을 잰 자료는 이번 조사에서 PubMed와 공공기관 자료로 확인하지 못함. 따라서 다른 소리쟁이속 종의 옥살산 수치는 이 종에 옮겨 쓰지 않았고, 잎을 데치거나 삶을 때 옥살산이 얼마나 줄어드는지도 이 종 자료로는 확인하지 못함.\n\n"
     "잎과 지상부에도 에모딘·레인·알로에에모딘 같은 하이드록시안트라센 유도체가 있다[2][3]. 알칼리성 흙 화분 시험에서 지상부(줄기·잎을 합친 건조 시료) 에모딘은 수확 단계에 따라 약 0.51–2.75 µg·g⁻¹(원문 표기 'µg·g')였다[2]. EFSA는 하이드록시안트라센 유도체를 반대 근거가 없는 한 유전독성·발암성 물질로 보아야 하며 안전한 1일 섭취량을 정할 수 없다고 결론지었다[22]. 2019년 종설도 에모딘의 여러 장기 독성 우려를 따로 짚었다[10].\n\n"
     "참소리쟁이 추출물(부위는 초록에서 확인하지 못함)은 사람 상피세포 Caco-2에서 0.1–0.5 mg/mL, HT-29에서 0.1–0.75 mg/mL 범위에서 독성이 없었으나 세포 실험 결과일 뿐이다[18]. 피스시온-8-O-β-글루코피라노사이드의 항암·패혈증 억제 결과도 세포·동물 실험이다[26][27]. 금속 오염지에서 자란 집단은 구리를 견디며 자라므로, 채취지 토양 오염에 주의할 필요가 있으나 잎의 중금속 함량 자료는 확인하지 못함[21]."},
]

compounds = [
    {"name": "Emodin", "name_ko": "에모딘", "class": "안트라퀴논", "role": "marker", "part": "지상부(줄기·잎)·뿌리",
     "content_text": "지상부(알칼리성 흙) 0.5112–2.7515 µg·g⁻¹, 뿌리(알칼리성 흙) 0.5218–1.6337 µg·g⁻¹(수확 단계별; 원문 표기 'µg·g', 건조 분말 시료)[2]; 잎 추출물에서 분리[3]",
     "activity_ko": "백선균(T. mentagrophytes)에 가장 강한 억제(시험관)[3]; EFSA가 유전독성 우려를 지적한 하이드록시안트라센 유도체[22]",
     "source": [2, 3, 22]},
    {"name": "Rhein", "name_ko": "레인", "class": "안트라퀴논", "role": "bioactive", "part": "잎·뿌리",
     "content_text": "잎 추출물에서 분리(정량값 없음)[3]; 뿌리(알칼리성 흙) 0.4963–1.0106 µg·g⁻¹(원문 표기 'µg·g')[2]",
     "activity_ko": "칸디다·T. rubrum에 가장 강한 억제(시험관)[3]",
     "source": [2, 3]},
    {"name": "Aloe-emodin", "name_ko": "알로에에모딘", "class": "안트라퀴논", "role": "bioactive", "part": "잎",
     "content_text": "잎 추출물에서 분리(정량값 없음)[3]",
     "activity_ko": "항진균 활성 성분 가운데 하나(시험관)[3]",
     "source": [3]},
    {"name": "Chrysophanol", "name_ko": "크리소파놀", "class": "안트라퀴논", "role": "bioactive", "part": "뿌리(지하부)",
     "content_text": "뿌리(알칼리성 흙) 0.8329–2.7070 µg·g⁻¹(원문 표기 'µg·g'); 지하부가 지상부보다 많음[2]; 다이클로로메테인 추출물 500 mg에서 24.1 mg 분리[25]",
     "activity_ko": "이 종의 주요 약효 안트라퀴논으로 다뤄짐[2]",
     "source": [2, 25]},
    {"name": "Physcion", "name_ko": "피스시온", "class": "안트라퀴논", "role": "bioactive", "part": "뿌리(지하부)",
     "content_text": "뿌리(알칼리성 흙) 0.6104–1.9153 µg·g⁻¹(원문 표기 'µg·g'); 알칼리성 흙에서 S7 단계 58.21% 증가[2]",
     "activity_ko": "알칼리 스트레스에서 늘어나는 이차대사물질로 해석[2]",
     "source": [2]},
    {"name": "Physcion 8-O-beta-D-glucopyranoside", "name_ko": "피스시온-8-O-β-글루코피라노사이드", "class": "안트라퀴논 배당체", "role": "bioactive", "part": "뿌리(추출물)",
     "content_text": "뿌리 메탄올 추출물의 안트라퀴논 8종 가운데 하나(정량값 없음)[15]; 에탄올 추출물에서 분리[26]",
     "activity_ko": "폐암 세포(A549) 증식 억제(세포)[26]; 내독소혈증 생쥐 보호(동물, 복강 주사)[27]",
     "source": [15, 26, 27]},
    {"name": "Nepodin", "name_ko": "네포딘", "class": "나프탈렌 유도체", "role": "bioactive", "part": "뿌리",
     "content_text": "뿌리 생중량 기준 검출 안 됨–0.34%[11]",
     "activity_ko": "칸디다 생물막·균사 형성 억제(시험관·선충 모델)[29]; 파골세포 분화 억제가 보고된 성분[11]",
     "source": [11, 29]},
    {"name": "Rutin", "name_ko": "루틴", "class": "플라보놀 배당체", "role": "bioactive", "part": "잎",
     "content_text": "잎 추출물에서 분리(정량값 없음)[3]",
     "activity_ko": "잎 항진균 분획의 구성 성분[3]",
     "source": [3]},
    {"name": "Quercetin", "name_ko": "퀘르세틴", "class": "플라보놀", "role": "bioactive", "part": "잎·열매",
     "content_text": "잎 추출물에서 분리[3]; 열매 에틸아세테이트 추출물에서 분리(정량값 없음)[14]",
     "activity_ko": "열매 분리 성분으로 최종당화산물(AGEs) 형성 억제를 평가(시험관)[14]",
     "source": [3, 14]},
    {"name": "Ferulic acid", "name_ko": "페룰산", "class": "페놀산", "role": "bioactive", "part": "잎",
     "content_text": "잎 추출물에서 분리(정량값 없음)[3]",
     "activity_ko": "잎 단일 성분 가운데 하나[3]",
     "source": [3]},
    {"name": "p-Coumaric acid", "name_ko": "p-쿠마르산", "class": "페놀산", "role": "bioactive", "part": "잎",
     "content_text": "잎 추출물에서 분리(정량값 없음)[3]",
     "activity_ko": "잎 단일 성분 가운데 하나[3]",
     "source": [3]},
    {"name": "Pyrogallol", "name_ko": "피로갈롤", "class": "페놀", "role": "bioactive", "part": "지상부",
     "content_text": "지상부 에틸아세테이트 추출물의 주된 페놀(HPLC; 정량값은 초록에서 확인하지 못함)[6]",
     "activity_ko": "추출물의 항산화·항균 활성과 관련된 성분으로 제시(시험관)[6]",
     "source": [6]},
    {"name": "Rumejaposide A", "name_ko": "루메자포사이드 A", "class": "옥산트론 C-배당체", "role": "bioactive", "part": "뿌리",
     "content_text": "뿌리에서 처음 분리된 옥산트론 C-배당체 5종(A–E) 가운데 하나(정량값 없음)[12]",
     "activity_ko": "이 종에서 처음 보고된 구조[12]",
     "source": [12]},
    {"name": "3-Acetyl-2-methyl-1,4,5-trihydroxy-2,3-epoxynaphthoquinol", "name_ko": "에폭시나프토퀴놀 유도체", "class": "나프토퀴놀", "role": "bioactive", "part": "뿌리",
     "content_text": "뿌리에서 분리한 신규 화합물(정량값 없음)[12]",
     "activity_ko": "활성 자료는 확인하지 못함; 구조 보고[12]",
     "source": [12]},
    {"name": "Tormentic acid", "name_ko": "토멘트산", "class": "트라이터페노이드", "role": "bioactive", "part": "줄기",
     "content_text": "줄기 에틸아세테이트 추출물에서 24-노르우르산형 신규 트라이터페노이드 2종과 함께 분리(정량값 없음)[13]",
     "activity_ko": "줄기 성분 보고(활성 자료는 초록에 없음)[13]",
     "source": [13]},
]

assays = [
    {"role": "literature", "compound": "Emodin", "compound_ko": "에모딘·크리소파놀·피스시온·레인(안트라퀴논 4종)",
     "part": "지상부(줄기·잎)와 지하부(뿌리), 건조 분말",
     "content": "지상부 에모딘 0.5112–2.7515 µg·g⁻¹(알칼리성 흙, 수확 단계별; 원문 표기 'µg·g'), 지하부 크리소파놀 0.8329–2.7070, 피스시온 0.6104–1.9153, 레인 0.4963–1.0106 µg·g⁻¹[2]",
     "method": "HPLC-UV",
     "conditions": {
         "instrument": "ACCHROM S6000 HPLC",
         "column": "X-charge C18, 5 µm, 150 mm × 4.6 mm (Acchrom Tech)",
         "mobile_phase": "A: 메탄올, B: 0.1% 인산",
         "gradient": "0–5분 A 60%; 5–22분 A 65%; 22–30분 A 75%; 30–35분 A 80%; 35–40분 A 90%",
         "flow": "1.0 mL/min",
         "temp": "40 °C",
         "detection": "UV 254 nm",
         "injection": "20 µL",
         "sample_prep": "105 °C 30분 후 80 °C 항량 건조·분쇄(0.25 mm 체)한 잎·뿌리 시료를 메탄올로 50 °C에서 1시간 초음파 추출, 8,000 rpm 10분 원심분리 후 0.22 µm 막 여과",
         "standard": "에모딘·크리소파놀·피스시온·레인 표준품 검량선",
         "linearity": "",
         "lod": "",
         "loq": "",
         "recovery": ""
     },
     "rationale": "식품 부위인 잎을 포함한 지상부의 안트라퀴논을 이 종에서 직접 정량한 유일한 전문 확인 자료다[2]. 지상부는 '줄기·잎'을 합친 시료이고 화분 재배 개체이며, 검출·정량한계와 회수율은 본문에 없어 비워 둠.",
     "source": [2], "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC13342501/", "source_kind": "paper"},
    {"role": "literature", "compound": "Emodin", "compound_ko": "잎 안트라퀴논·페놀 성분 7종(에모딘·레인·알로에에모딘·페룰산·p-쿠마르산·루틴·퀘르세틴)",
     "part": "잎", "content": "정량값은 초록에서 확인하지 못함[3]",
     "method": "HPLC·NMR(성분 분리·동정)",
     "conditions": {"instrument": "", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "", "injection": "", "sample_prep": "산 추출·알코올 침전", "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""},
     "rationale": "식품 부위인 잎만 따로 분석한 연구다[3]. 전문 확인 못함 — 분석 조건은 비워 둠.",
     "source": [3], "url": "https://doi.org/10.1016/j.mycmed.2024.101513", "source_kind": "paper"},
    {"role": "literature", "compound": "Pyrogallol", "compound_ko": "피로갈롤(지상부 페놀)",
     "part": "지상부", "content": "에틸아세테이트 추출물의 주된 페놀(정량값은 초록에서 확인하지 못함)[6]",
     "method": "HPLC(및 GC-MS 정성)",
     "conditions": {"instrument": "", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "", "injection": "", "sample_prep": "에탄올·헥세인·클로로폼·에틸아세테이트·물 추출물 비교", "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""},
     "rationale": "지상부 추출물의 항산화·항균 활성과 연결된 지표 페놀로 제시되었다[6]. 전문 확인 못함 — 분석 조건은 비워 둠.",
     "source": [6], "url": "https://doi.org/10.1248/bpb.28.2225", "source_kind": "paper"},
]

d = {
    "slug": "rumex-japonicus",
    "name_ko": "참소리쟁이",
    "name_en": "Northeast Asian curly dock",
    "scientific_name": "Rumex japonicus Houtt.",
    "aliases": ["참소리쟁이잎", "참송구지", "소리쟁이(목록상 다른 이름; R. crispus 의 국문명과 같음)", "양제(羊蹄, Yang Ti)", "Rumex crispus subsp. japonicus (Houtt.) Kitam."],
    "sections": sections,
    "compounds": compounds,
    "markers": [],
    "assays": assays,
    "nutrients": [],
    "production": [],
    "world": [],
    "gi": [],
    "orgs": [],
    "sources": sources,
}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
print("written", OUT)
