import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
A = "2026-11-02"
def P(n, title, doi, pub):
    return {"n": n, "title": title, "url": f"https://doi.org/{doi}" if doi else None, "publisher": pub, "accessed": A}
sources = [
 {"n":1,"title":"식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — Rastrelliger kanagurta 2행: '줄무늬고등어'·'훈연줄무늬고등어'(영문 Indian mackerel, 수산물, 대분류 식품원료(A코드), 부위 '-', 사용조건 기준 없음, 상태 사용가능, 별명 없음); 같은 속 다른 종 행 없음; 고시형 원료 원재료 목록(KR_NOTICE) 없음; 별도 행 '고등어'(Scomber japonicus, Chub mackerel)·'갈고등어'(Decapterus muroadsi) — 로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json, docs/materials/rastrelliger-kanagurta/card.json","url":"https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020","publisher":"식품의약품안전처","accessed":"2026-10-13"},
 P(2,"The First Genome Survey and De Novo Assembly of the Short Mackerel (Rastrelliger brachysoma) and Indian Mackerel (Rastrelliger kanagurta). Animals (Basel) 2022;12(14):1769 (PubMed 도구로 PMC 전문 확인; 전문 텍스트에서 이탤릭 학명이 빠져 있어 종별 값은 제목·초록 순서(짧은고등어→인도고등어)와 미토게놈 길이 16,537 bp(기존 R. kanagurta 보고와 일치)로 대응시킴)","10.3390/ani12141769","Animals (MDPI) (PubMed 35883316, PMC9312166)"),
 P(3,"Molecular phylogenetics of three species of the genus Rastrelliger using mitochondrial DNA markers. Mol Biol Rep 2015;42(4):873-9 (초록 확인)","10.1007/s11033-014-3710-8","Molecular Biology Reports (PubMed 25192894)"),
 P(4,"High connectivity in Rastrelliger kanagurta: influence of historical signatures and migratory behaviour inferred from mtDNA cytochrome b. PLoS One 2015;10(3):e0119749 (초록 확인)","10.1371/journal.pone.0119749","PLoS One (PubMed 25786216, PMC4365000)"),
 P(5,"The complete mitochondrial genome sequence of Rastrelliger kanagurta (Perciformes: Scombridae). Mitochondrial DNA 2013;24(2):114-6 (초록 확인)","10.3109/19401736.2012.726624","Mitochondrial DNA (PubMed 23025587)"),
 P(6,"Morphometric and molecular analysis of mackerel (Rastrelliger spp) from the west coast of Peninsular Malaysia. Genet Mol Res 2011;10(3):2078-92 (초록 확인)","10.4238/vol10-3gmr1249","Genetics and Molecular Research (PubMed 21968625)"),
 P(7,"Application of data-limited methods to assess stock status and recommend management for Indian mackerel (Rastrelliger kanagurta) in Bangladesh coastal waters. Sci Rep 2026;16(1) (PubMed 도구로 PMC 전문 확인)","10.1038/s41598-026-40935-3","Scientific Reports (PubMed 41775787, PMC13066565)"),
 P(8,"Trophic significance of microzooplankton to commercially important small pelagic fishes along the southwest coast of India. Environ Sci Pollut Res Int 2021;28(45):64394-64406 (초록 확인)","10.1007/s11356-021-15452-7","Environmental Science and Pollution Research (PubMed 34312754)"),
 P(9,"Metazoan parasites of the Indian mackerel, Rastrelliger kanagurta (Scombridae) of Visakhapatnam coast, Bay of Bengal. J Parasit Dis 2011;35(1):66-74 (초록 확인)","10.1007/s12639-011-0028-5","Journal of Parasitic Diseases (PubMed 22654318, PMC3114970)"),
 P(10,"Fish consumption pattern among adults of different ethnics in Peninsular Malaysia. Food Nutr Res 2016;60:32697 (초록 확인; 초록은 영명 'Indian mackerel'만 씀)","10.3402/fnr.v60.32697","Food & Nutrition Research (PubMed 27534846, PMC4989178)"),
 P(11,"Under pressure: Investigating marine resource-based livelihoods in Jakarta Bay and the Thousand Islands. Mar Pollut Bull 2016;110(2):778-89 (초록 확인)","10.1016/j.marpolbul.2016.05.032","Marine Pollution Bulletin (PubMed 27241879)"),
 {"n":12,"title":"Purification and properties of a protease from the guts of Rastrelliger kanagurta (mackerel). Enzymologia 1960;21:219-37 (서지 정보만 확인, 초록 없음)","url":"https://pubmed.ncbi.nlm.nih.gov/13835708/","publisher":"Enzymologia (PubMed 13835708)","accessed":A},
 P(13,"Stability of Radurized Indian Mackerel (Rastrelliger kanagurta) as a Function of Temperature. J Food Prot 1982;45(4):360-362 (초록 확인)","10.4315/0362-028X-45.4.360","Journal of Food Protection (PubMed 30866335)"),
 P(14,"Assessment of Radiation and Heavy Metals Risk due to the Dietary Intake of Marine Fishes (Rastrelliger kanagurta) from the Straits of Malacca. PLoS One 2015;10(6):e0128790 (PubMed 도구로 PMC 전문 확인)","10.1371/journal.pone.0128790","PLoS One (PubMed 26075909, PMC4467845)"),
 P(15,"Reduced Washing Cycle for Sustainable Mackerel (Rastrelliger kanagurta) Surimi Production: Evaluation of Bio-Physico-Chemical, Rheological, and Gel-Forming Properties. Foods 2021;10(11):2717 (PubMed 도구로 PMC 전문 확인; 키워드·본문 'Indian mackerel')","10.3390/foods10112717","Foods (MDPI) (PubMed 34828998, PMC8620436)"),
 P(16,"Comparative assessment of amino acids composition in two types of marine fish silage. Sci Rep 2021;11(1):15235 (PubMed 도구로 PMC 전문 확인; 초록 원문 'Indian mackerel (Rastrelliger kanagurta)')","10.1038/s41598-021-93884-4","Scientific Reports (PubMed 34315916, PMC8316558)"),
 P(17,"Changes in urocanic acid, histamine, putrescine and cadaverine levels in Indian mackerel (Rastrelliger kanagurta) during storage at different temperatures. Food Chem 2013;139(1-4):320-5 (초록 확인)","10.1016/j.foodchem.2012.12.040","Food Chemistry (PubMed 23561112)"),
 P(18,"Development and validation of an ion-pair chromatographic method for simultaneous determination of trans- and cis-urocanic acid in fish samples. J Chromatogr A 2012;1256:144-9 (초록 확인; 초록은 영명 'Indian mackerel'만 씀)","10.1016/j.chroma.2012.07.083","Journal of Chromatography A (PubMed 22885043)"),
 P(19,"Characterization of Ras k 1 a novel major allergen in Indian mackerel and identification of parvalbumin as the major fish allergen in 33 Asia-Pacific fish species. Clin Exp Allergy 2018;48(4):452-463 (초록 확인)","10.1111/cea.13069","Clinical and Experimental Allergy (PubMed 29193486)"),
 {"n":20,"title":"Role of pepsin in modifying the allergenicity of bhetki (Lates calcarifer) and mackerel (Rastrelliger kanagurta) fish. Indian J Biochem Biophys 2007;44(2):94-100 (초록 확인)","url":"https://pubmed.ncbi.nlm.nih.gov/17536337/","publisher":"Indian Journal of Biochemistry & Biophysics (PubMed 17536337)","accessed":A},
 P(21,"Bioaccumulation of heavy metals in Rastrelliger kanagurta along the coastal waters of Visakhapatnam, India. Mar Pollut Bull 2020;160:111658 (초록 확인)","10.1016/j.marpolbul.2020.111658","Marine Pollution Bulletin (PubMed 33181935)"),
 P(22,"Concentration and exposure assessment of mercury in commercial fish and other seafood marketed in Oman. J Food Sci 2013;78(7):T1082-90 (초록 확인; 초록은 영명 'Indian mackerel'만 씀)","10.1111/1750-3841.12150","Journal of Food Science (PubMed 23701530)"),
 P(23,"Histamine risk assessment in Scombridae fish across processing forms and distribution channels: a case study from Nghe An Province, Vietnam. Food Addit Contam Part A 2026;43(8):1222-1232 (초록 확인; 초록에서 학명이 빠져 'Indian mackerel (… sp.)'로만 나와 속 수준(Rastrelliger sp.)으로만 대응)","10.1080/19440049.2026.2690613","Food Additives & Contaminants: Part A (PubMed 42348769)"),
 P(24,"Effect of freezing time on the quality of Indian mackerel (Rastrelliger kanagurta) during frozen storage. J Food Sci 2008;73(7):S345-53 (초록 확인)","10.1111/j.1750-3841.2008.00876.x","Journal of Food Science (PubMed 18803727)"),
 {"n":25,"title":"Bacterial production of histamine in some tropical fish. Microbios 1990;63(255):71-7 (초록 확인)","url":"https://pubmed.ncbi.nlm.nih.gov/2259288/","publisher":"Microbios (PubMed 2259288)","accessed":A},
 P(26,"Combined effects of vacuum packaging and mint extract treatment on the biochemical, sensory and microbial changes of chill stored Indian mackerel. J Food Sci Technol 2016;53(12):4289-4297 (초록 확인)","10.1007/s13197-016-2425-3","Journal of Food Science and Technology (PubMed 28115769, PMC5223264)"),
 P(27,"Comparative evaluation of gum arabic coating and vacuum packaging on chilled storage characteristics of Indian mackerel (Rastrelliger kanagurta). J Food Sci Technol 2016;53(4):1889-98 (초록 확인)","10.1007/s13197-015-2122-7","Journal of Food Science and Technology (PubMed 27413215, PMC4926901)"),
 P(28,"Larvae of Anisakidae in marine fish of coastal waters near Jakarta, Indonesia. Am J Trop Med Hyg 1978;27(1 Pt 1):51-4 (초록 확인)","10.4269/ajtmh.1978.27.51","American Journal of Tropical Medicine and Hygiene (PubMed 626282)"),
 {"n":29,"title":"Detection of Anisakis spp. and residual formaldehyde in Indian mackerel and splendid squid from a fish market in Samut Songkhram Province, Thailand. Trop Biomed 2019;36(1):53-59 (초록 확인)","url":"https://pubmed.ncbi.nlm.nih.gov/33597426/","publisher":"Tropical Biomedicine (PubMed 33597426)","accessed":A},
 P(30,"Synthesis and in vitro antioxidant functions of protein hydrolysate from backbones of Rastrelliger kanagurta by proteolytic enzymes. Saudi J Biol Sci 2014;21(1):19-26 (초록 확인)","10.1016/j.sjbs.2013.04.009","Saudi Journal of Biological Sciences (PubMed 24596496, PMC3937463)"),
 P(31,"Evaluation of the effect of n-3 PUFA-rich dietary fish oils on lipid profile and membrane fluidity in alloxan-induced diabetic mice (Mus musculus). Mol Cell Biochem 2016;416(1-2):117-29 (초록 확인)","10.1007/s11010-016-2701-6","Molecular and Cellular Biochemistry (PubMed 27101827)"),
 P(32,"Evaluation of trace metal content by ICP-MS using closed vessel microwave digestion in fresh water fish. J Environ Public Health 2014;2014:201506 (초록 확인)","10.1155/2014/201506","Journal of Environmental and Public Health (PubMed 24744789, PMC3976888)"),
]

S = {}
S["overview"] = ("줄무늬고등어(Rastrelliger kanagurta, 영문 Indian mackerel)는 고등어과(Scombridae) 줄무늬고등어속의 바닷물고기로, 식약처 「식품원료 목록」에 '줄무늬고등어'와 '훈연줄무늬고등어' 두 원료명의 수산물로 올라 있다[1]. "
 "두 행 모두 상태는 '사용가능'이고 사용 부위는 따로 정하지 않은 '-'이며 별도의 사용 조건은 없다[1]. "
 "건강기능식품 고시형 원료의 원재료 목록에는 없어 식약처가 정한 지표성분도 없다[1]. "
 "같은 목록의 '고등어'는 다른 속의 Scomber japonicus(Chub mackerel)로 별도 원료이며, 이 문서는 고등어(Scomber) 자료를 섞지 않았다[1].\n\n"
 "인도양과 서태평양의 얕은 바다에 사는 작은 표층성 어종으로, 동남아시아와 인도양 연안에서 상업적으로 중요한 생선이다[2, 7]. "
 "말레이시아 반도 성인 2,675명의 식사 기록에서 가장 자주 먹은 바다 생선이 'Indian mackerel'이었다[10]. "
 "근육에는 붉은 색소 단백질인 미오글로빈이 많아(씻지 않은 다진 살 6.77 mg/g) 어묵 원료로는 다루기 까다롭다[15]. "
 "국가표준식품성분표의 줄무늬고등어 값은 이번 조사에서 확인하지 못함.")
S["history"] = ("PubMed 에 실린 이 종의 연구는 1960년 소화관 단백질분해효소를 정제한 보고까지 거슬러 올라간다[12]. "
 "1978년 인도네시아 자카르타 근해 조사에서는 줄무늬고등어 1,459마리 중 719마리(49%)에서 고래회충과 유충이 나와 사람 감염원 가능성이 지적되었다[28]. "
 "1982년 인도에서는 1.5 kGy 감마선 조사가 0–15 °C 저장 중 부패 속도를 늦춘다는 보존 연구가 나왔다[13].\n\n"
 "말레이시아에서는 'Ikan kembung'이라는 이름으로 가장 흔히 먹는 생선으로 소개되며, 말라카 해협 개체의 방사능·중금속 위해평가 대상이 되었다[14]. "
 "인도네시아 자카르타만 본토 어촌에서는 가장 경제적 가치가 큰 어종으로 꼽혔다[11]. "
 "2000년대 이후에는 냉장·냉동 저장, 어묵(수리미), 가공 부산물 활용 연구가 이어졌다[24, 15, 30]. "
 "어유를 당뇨 생쥐 사료에 10% 섞은 동물 실험도 있으나 사람 효과는 확인되지 않았다[31]. "
 "국내 식용 이력과 수입 경로는 이번 조사에서 확인하지 못함.")
S["biology"] = ("줄무늬고등어는 몸높이가 머리 길이보다 짧은 다소 높은 몸에, 몸 윗부분의 가는 검은 세로줄과 가슴지느러미 아래 가장자리 근처의 검은 점이 특징이고 지느러미는 노르스름하다[2]. "
 "분포는 남아프리카·홍해에서 사모아까지, 오스트레일리아 북부에서 일본 남부까지의 인도-서태평양이다[2]. "
 "대륙붕 수심 20–90 m의 표층에 살며, 다 자란 개체는 새우 유생·작은 물고기 같은 대형 플랑크톤을 먹고 한 해 여러 차례 나누어 산란한다[7].\n\n"
 "인도 남서 연안 조사에서 위 내용물은 한 해 내내 식물플랑크톤·미소동물플랑크톤·요각류로 이루어졌다[8]. "
 "방글라데시 개체의 성장 계수는 극한 체장 33.25 cm, k 0.92/년이었고, 추정 수명은 3.26년, 첫 성숙 체장은 대략 17–19 cm로 정리되었다[7]. "
 "벵골만 비사카파트남 개체에서는 기생충 15종이 나왔고, 대부분 이 종에만 붙는 전문 기생충이어서 플랑크톤 식성을 반영한다고 해석되었다[9].")
S["related_species"] = ("줄무늬고등어속에는 줄무늬고등어(R. kanagurta), 짧은고등어(R. brachysoma), 섬고등어(R. faughni) 세 종이 있다[2]. "
 "세 종은 생김새가 매우 비슷해 인도 연안 19개체의 미토콘드리아 COI 서열로 구분한 연구에서 종간 거리는 0.039–0.086, 종내 거리는 0.000–0.012였다[3]. "
 "말레이시아 반도 서해안 77개체의 형태 측정에서는 줄무늬고등어가 형태적으로 다른 두 무리, 짧은고등어가 한 무리로 나뉘었다[6].\n\n"
 "식약처 목록에는 이 속의 다른 종 행이 없고, 이름이 비슷한 '고등어'(Scomber japonicus)와 '갈고등어'(Decapterus muroadsi)는 다른 학명의 별도 원료다[1]. "
 "논문 초록 가운데에는 이탤릭 학명이 빠지고 영명 'Indian mackerel'만 남은 것이 있어, 이 문서는 그런 자료를 영명으로 대응시켰다고 출처에 밝혔다[10, 22]. "
 "베트남 히스타민 연구처럼 'sp.'로만 적힌 자료는 속 수준 자료로만 다루었다[23].")
S["cultivation"] = ("줄무늬고등어는 아직 양식이 실용화되지 않은 자연산 어획 어종이며, 유전체 연구진은 번식 기전 이해가 양식 가능성을 여는 데 도움이 될 것이라고 보았다[2]. "
 "유엔식량농업기구 통계를 인용한 같은 논문은 짧은고등어와 줄무늬고등어가 2019년 어획량 15만 톤이 넘는 주요 70종에 들었다고 적었다[2].\n\n"
 "방글라데시 산업 트롤선 어획량은 2006년 1,640톤, 2012년 최고 9,503톤, 2022년 1,314톤이었다[7]. "
 "같은 연구는 산란 잠재력 비율이 17%로 남획 상태라고 보고, 최대지속생산량(1,967톤) 아래인 연 1,500톤 어획 한도와 18–22 cm 체장 관리를 권고했다[7]. "
 "어획 표본의 53%가 중앙값 20 cm보다 작아 미성어가 많이 잡히는 것으로 나타났다[7]. "
 "자카르타만 어민 80% 이상은 오염과 남획으로 자원이 줄고 있다고 응답했다[11]. "
 "국내 연근해 어획 통계와 수입량은 이번 조사에서 확인하지 못함.")
S["processing"] = ("식약처 목록에는 날것 외에 '훈연줄무늬고등어'가 별도 원료명으로 올라 있다[1]. "
 "내장을 뺀 줄무늬고등어를 0–2 °C에 두었을 때 관능 기준 저장 기간은 공기 포장 13일, 진공 포장 16일, 박하 추출물 처리 후 진공 포장 21일이었다[26]. "
 "4 °C 저장에서는 미생물 기준 저장 기간이 일반 비닐 포장 7–8일, 아라비아검 코팅 17일, 진공 포장 19–20일이었다[27]. "
 "냉동은 접촉식 판냉동(90분)이 송풍 냉동(220분)보다 빨랐고, −18 °C에서 두 시료 모두 3개월까지 먹을 만했으나 송풍 냉동 시료의 히스타민이 더 많이 생겼다[24].\n\n"
 "어묵(수리미)은 다진 살을 찬물로 두 번 씻으면 미오글로빈이 6.77에서 1.63 mg/g으로 줄고 겔 강도가 약 440 g·cm로 태국 산업 기준(400 g·cm 이상)을 넘었다[15]. "
 "손질 부산물은 포름산 사일리지로 만들면 30일째 총아미노산 41.2 mg/g이 되었고[16], 등뼈를 펩신으로 분해한 가수분해물은 DPPH 라디칼을 46% 소거했다[30].")
S["genetics"] = ("줄무늬고등어의 미토콘드리아 전체 유전체는 16,537 bp로, 단백질 암호 유전자 13개, rRNA 유전자 2개, tRNA 유전자 22개로 이루어지며 A+T 함량은 52.29%이다[5]. "
 "2022년 태국 개체의 첫 유전체 조사에서 짧은고등어와 줄무늬고등어의 유전체 크기는 680–690 Mbp 수준(추정값 680.14·688.82 Mbp), 이형접합도는 약 0.81이었다[2]. "
 "반복 서열 비율은 줄무늬고등어가 9.30%로 짧은고등어(8.30%)보다 조금 높았다[2]. "
 "두 종의 미토게놈은 96.64% 같았다[2].\n\n"
 "인도네시아-말레이시아 군도와 서인도양 23개 집단의 시토크롬 b 분석에서 군도 안에서는 지리적 구조가 없어 사실상 하나의 번식 집단이었다[4]. "
 "반면 서인도양과 군도 집단은 뚜렷이 갈라졌고, 연구진은 플라이스토세 후기 해수면 변동이 안다만해 북쪽에 계통지리적 경계를 만든 것으로 해석했다[4]. "
 "인도 본토와 안다만 제도 개체 사이에는 뚜렷한 유전 거리가 없었다[3].")
S["safety"] = ("식약처 목록상 줄무늬고등어는 사용 조건 없는 '사용가능' 원료이며, 고시형 원료가 아니어서 고시 섭취 주의사항은 없다[1]. "
 "국내 식품공전의 히스타민·수은 기준 원문은 이번 조사에서 확인하지 못함.\n\n"
 "고등어과 생선이라 상온에 두면 히스타민이 생긴다: 갓 잡은 살에서는 히스타민이 검출되지 않았으나 0–23 °C 저장 중 모두 늘었고 23 °C에서 가장 빨랐다[17]. "
 "베트남에서 2024년 고등어과 생선으로 인한 히스타민 식중독 4건(입원 400명 이상)이 있었고, 시장의 구운 줄무늬고등어속 생선은 최고 319 mg/kg으로 1만 회 섭취당 3–6건의 위험이 추정되었다[23].\n\n"
 "근육 단백질 파브알부민은 새 주요 알레르겐 Ras k 1으로 등록되었고 가열 후에도 환자 혈청 IgE와 반응했다[19, 20]. "
 "말라카 해협 개체의 수은은 포트클랑에서만 평균 0.025 mg/kg(건중량) 검출되었고[14], 오만 시판품 평균은 0.02 mg/kg이었다[22]. "
 "비사카파트남 개체는 비소 0.67–1.47 μg/g, 납 0.06–0.37 μg/g 등이 일부 기준을 넘었다[21]. "
 "인도 연안 조사에서는 바실루스(Bacillus)균이 이 생선에서 히스타민을 더 많이 만들었다[25]. "
 "태국 시장 개체 2.86%에서 고래회충 유충이 나왔다[29].")

titles = {"overview":"한눈에 보기","history":"이용·연구 역사","biology":"어종·형태·생태","related_species":"관련 종·학명","cultivation":"어획·자원 관리","processing":"저장·가공","genetics":"유전 정보","safety":"안전성"}

def C(name, ko, cls, role, part, content, act, src):
    return {"name":name,"name_ko":ko,"class":cls,"role":role,"part":part,"content_text":content,"activity_ko":act,"source":src}
compounds = [
 C("Myoglobin","미오글로빈","헴 단백질(색소)","bioactive","근육(껍질 벗긴 필레를 다진 살)","씻지 않은 다진 살 6.77 mg/g; 두 번 세척 수리미 1.63 mg/g; 메트미오글로빈 비율 약 73–76%[15]","붉은 살 색과 지질 산화를 좌우해 어묵 품질의 핵심 지표로 쓰였다[15]",[15]),
 C("Histamine","히스타민","생체아민","marker","근육","갓 잡은 살에서 검출되지 않음[17]; 베트남 시장 구운 줄무늬고등어속(Rastrelliger sp.) 최고 319 mg/kg, 생물 최고 109 mg/kg[23]","저장 온도가 높을수록 빠르게 늘어나는 고등어과 생선 식중독 원인 물질이다[17, 23]",[17,23]),
 C("Urocanic acid","트랜스-유로카닌산","히스티딘 대사물","marker","근육","갓 잡은 살 trans-UCA 14.83 mg/kg, 3 °C 15일 후 189.51 mg/kg[17]; 다른 시료에서 최고 118.8 mg/kg[18]","비만세포 탈과립 물질로 고등어형 식중독에 관여할 수 있다고 제시되었다[17, 18]",[17,18]),
 C("cis-Urocanic acid","시스-유로카닌산","히스티딘 대사물","marker","근육","갓 잡은 살 2.23 mg/kg, 0·3 °C 15일 저장 후 약 13배 증가[17]","고등어형 식중독 관련 후보 물질로 히스타민과 함께 측정되었다[17]",[17]),
 C("Cadaverine","카다베린","생체아민","marker","근육","갓 잡은 살 1.86 mg/kg, 저장 중 유의하게 증가[17]","부패 지표 생체아민이다[17]",[17]),
 C("Parvalbumin","파브알부민(Ras k 1)","칼슘 결합 단백질(알레르겐)","bioactive","근육","2차원 전기영동으로 이성질체 7종 확인; 주 이성질체 서열은 다른 고등어류 파브알부민과 90% 넘게 일치[19]","가열에 안정한 주요 어류 알레르겐으로 Ras k 1 이라는 공식 명칭이 붙었다[19]",[19]),
 C("Selenium","셀레늄","무기질(미량원소)","nutrient","어체(뼈 포함 가능, 건조 분말)","말라카 해협 지점 평균 0.035–0.0938 mg/kg(건중량)[14]; 인도 하이데라바드 시판품 0.01 mg/kg[32]","필수 미량원소로 함께 정량되었다[14, 32]",[14,32]),
 C("Zinc","아연","무기질(미량원소)","nutrient","어체(뼈 포함 가능, 건조 분말)","지점 평균 5.607–15.35 mg/kg(건중량)[14]","필수 미량원소로 정량되었다[14]",[14]),
 C("Calcium","칼슘","무기질","nutrient","어체(뼈 포함 가능, 건조 분말)","지점 평균 5,058–6,714 mg/kg(건중량)[14]","뼈가 시료 무게에 크게 기여했다고 설명되었다[14]",[14]),
 C("Arsenic","비소(총)","유해 원소","marker","근육·어체","말라카 해협 지점 평균 0.325–0.7485 mg/kg(건중량)[14]; 비사카파트남 근육 0.67–1.47 μg/g[21]","일부 지역 시료가 기준을 넘어 감시 대상으로 제시되었다[21]",[14,21]),
 C("Mercury","수은(총)","유해 원소","marker","근육·어체","포트클랑 시료만 검출, 평균 0.025 mg/kg(건중량)[14]; 오만 시판품 평균 0.02 mg/kg[22]","조사 어종 가운데 낮은 편으로 보고되었다[22]",[14,22]),
 C("Glutamic acid","글루탐산","아미노산","nutrient","손질 부산물 사일리지(상등액)","발효 30일 총아미노산 중 6.0 mg/g[16]","류신과 함께 가장 많은 아미노산이었다[16]",[16]),
 C("Leucine","류신","필수아미노산(BCAA)","nutrient","손질 부산물 사일리지(상등액)","발효 30일 총아미노산 중 6.0 mg/g, 유리아미노산 3.09 mg/g[16]","주요 아미노산으로 정량되었다[16]",[16]),
 C("Arginine","아르기닌","아미노산","nutrient","손질 부산물 사일리지(상등액)","발효 30일 총아미노산 중 5.3 mg/g, 유리아미노산 5.90 mg/g[16]","유리아미노산 가운데 가장 많았다[16]",[16]),
]
E = lambda **k: {f: k.get(f,"") for f in ["instrument","column","mobile_phase","gradient","flow","temp","detection","injection","sample_prep","standard","linearity","lod","loq","recovery"]}
assays = [
 {"role":"literature","compound":"Mercury / Arsenic / Selenium (multi-element)","compound_ko":"수은·비소·셀레늄 등 원소","part":"어체(세척·절단 후 70 °C 건조 분말, 뼈 포함 가능)",
  "content":"Hg 포트클랑 평균 0.025 mg/kg, As 0.325–0.7485, Se 0.035–0.0938 mg/kg(건중량)[14]","method":"ICP-MS",
  "conditions":E(instrument="Agilent 7500 Series ICP-MS",detection="ICP-MS 원소별 질량 측정(조건 세부는 본문에 없음)",
   sample_prep="말라카 해협 3곳(포트클랑·판타이레미스·바간랄랑) 22–25 cm·125–130 g 개체를 세척·절단해 70 °C에서 3일 건조·분쇄; 분말 약 0.5 g을 마이크로파 분해기(Multiwave 3000)에서 65% HNO3 5 mL + 30% H2O2 3 mL로 10분 분해 → 여과 → 초순수로 50 mL",
   standard="다원소 검량 표준 2A(원소별 10 mg/L, 5% HNO3 희석), 바탕 용액 1개 + 표준 5개",
   lod="Na·Mg·Al·K·Ca·Cr·Mn·Co·Ni·Cu·Zn·As·Rb·Sr·Se 0.0002 mg/kg; Fe·Cd·Ba·Pb 0.0001 mg/kg",
   recovery="인증값 대비 88–96%"),
  "rationale":"수은·비소 같은 유해 원소와 셀레늄 등 필수 원소를 한 번에 정량해 섭취 위해를 평가하는 데 쓰였다[14]. 전문(Methods) 확인 — 칼럼·이동상 해당 없음, 수은 전용 측정 조건과 정량한계는 본문에 없음[14].",
  "source":[14],"url":"https://doi.org/10.1371/journal.pone.0128790","source_kind":"paper"},
 {"role":"literature","compound":"Myoglobin","compound_ko":"미오글로빈","part":"근육(껍질 벗긴 필레를 다진 살)",
  "content":"씻지 않은 다진 살 6.77 mg/g, 1·2·3회 세척 수리미 2.56·1.63·1.61 mg/g[15]","method":"분광광도법(가시광·소렛 영역)",
  "conditions":E(instrument="Shimadzu UV-2100 분광광도계",detection="가시광·소렛 영역(380–450 nm) 스펙트럼, 소렛 피크 407 nm; 유도체 비율은 A582/A525·A557/A525·A503/A525 비로 계산",
   sample_prep="태국 나콘시탐마랏 시장 개체(60–70 g; 어획 약 12시간 후 하역, 얼음 1:2 보관)를 손질·껍질 제거 후 다짐; 차가운 40 mM 인산 완충액(pH 6.8)으로 미오글로빈 추출"),
  "rationale":"검붉은 살 생선의 어묵 백색도·지질 산화를 좌우하는 색소 단백질이라 세척 효과 지표로 쓰였다[15]. 전문(Methods) 확인 — 흡광계수·검량·검출·정량한계는 본문에 없음(인용 방법 참조)[15].",
  "source":[15],"url":"https://doi.org/10.3390/foods10112717","source_kind":"paper"},
 {"role":"literature","compound":"Amino acids (glutamic acid, leucine, arginine etc.)","compound_ko":"총·유리 아미노산","part":"손질 부산물 포름산 사일리지 상등액",
  "content":"발효 30일 총아미노산 41.2 mg/g(글루탐산·류신 각 6.0, 아르기닌 5.3 mg/g), 유리아미노산 31.35 mg/g[16]","method":"HPLC-DAD (OPA 유도체화)",
  "conditions":E(instrument="Agilent 1260 Infinity HPLC(4원 펌프·자동시료주입기·칼럼 오븐·다이오드 배열 검출기)",column="Agilent ZORBAX Eclipse Plus C18, 4.6 × 250 mm, 5 μm",
   mobile_phase="A: 10 mM Na2HPO4·10 mM Na2B4O7·5 mM NaN3(pH 8.2), B: 아세토나이트릴·메탄올·물(45:45:10, v/v/v)",gradient="기울기 시간표는 본문에 없음",flow="1.5 mL/min",
   detection="다이오드 배열 검출(파장은 본문에 없음)",injection="유리아미노산 1 μL",
   sample_prep="인도 고아 파나지 시장의 식용 부적합(부패 전) 줄무늬고등어 손질 부산물 50 g + 포름산 3%(1.5 mL), 26 ± 1 °C 발효; 총아미노산은 상등액 100 μL를 6 N HCl 2 mL·질소 치환 후 110 °C 24시간 가수분해 → 6 N NaOH 중화·건조 → 물 2 mL; 유리아미노산은 10% TCA 15 mL 처리 후 다이에틸에테르로 5회 추출·40 °C 이하 건조 → 물 25 mL",
   standard="내부표준 α-아미노뷰티르산(10 nmol/μL, 200 μL)"),
  "rationale":"부산물 사일리지의 영양·식물 생장 촉진 가치를 보는 지표로 아미노산 조성이 쓰였다[16]. 전문(Methods) 확인 — 근육이 아닌 부산물 시료이며, 기울기·검출 파장·검출·정량한계·회수율은 본문에 없음[16].",
  "source":[16],"url":"https://doi.org/10.1038/s41598-021-93884-4","source_kind":"paper"},
 {"role":"literature","compound":"trans-/cis-Urocanic acid","compound_ko":"유로카닌산(트랜스·시스)","part":"근육",
  "content":"갓 잡은 살 trans-UCA 14.83, cis-UCA 2.23 mg/kg; 히스타민 불검출[17]; 다른 시료 trans-UCA 최고 118.8 mg/kg[18]","method":"이온쌍 HPLC",
  "conditions":E(sample_prep="0.05 M HCl로 추출 후 10% 시트르산삼나트륨·10% 시트르산으로 단백질 침전[18]"),
  "rationale":"히스타민과 함께 고등어형 식중독 관련 물질로 제시되어 저장 온도별 신선도 지표로 측정되었다[17, 18]. 전문 확인 못함 — 초록만 보아 칼럼·이동상·검출 조건은 비워 둠[18].",
  "source":[17,18],"url":"https://doi.org/10.1016/j.chroma.2012.07.083","source_kind":"paper"},
]
world = [
 {"country":"방글라데시","metric":"production_t","year":y,"value":v,"unit":"톤","note":"산업 트롤선 어획량(수산국 해양수산사무소 로그북) — 영세어업 양륙량은 국가 통계에 종별로 나오지 않아 제외","source":[7]}
 for y,v in [(2006,1640),(2012,9503),(2022,1314)]
]
d = {"slug":"rastrelliger-kanagurta","name_ko":"줄무늬고등어","name_en":"Indian mackerel","scientific_name":"Rastrelliger kanagurta (Cuvier, 1816)",
 "aliases":["줄무늬고등어","훈연줄무늬고등어","Indian mackerel","Ikan kembung"],
 "sections":[{"key":k,"title":titles[k],"body":S[k]} for k in ["overview","history","biology","related_species","cultivation","processing","genetics","safety"]],
 "compounds":compounds,"markers":[],"assays":assays,"nutrients":[],"production":[],"world":world,"gi":[],"orgs":[],"sources":sources}
OUT.write_text(json.dumps(d,ensure_ascii=False,indent=1),encoding="utf-8")
for s in d["sections"]: print(s["key"], len(s["body"]))
