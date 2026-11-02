import json
from pathlib import Path
P = Path("/home/user/hfoodguide-wave3/docs/materials/momordica-dioica")
A = "2026-11-02"
def pm(n, title, doi, extra=""):
    return {"n": n, "title": title + extra, "url": f"https://doi.org/{doi}", "publisher": "PubMed", "accessed": A}
sources = [
 {"n": 1, "title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 티즐고어드과육(Momordica dioica Roxb.; Palupalagakalungai, Teasle gourd), 사용가능, 사용가능부위: 과육; 같은 속의 여주(Momordica charantia L.; 씨앗·뿌리·덩이줄기 행은 사용불가)·나한과(Momordica grosvenorii / Siraitia grosvenorii)·목별(Momordica cochinchinensis Sprenger) 행 대조(로컬 원자료 I1020_20261013.json)", "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
 {"n": 2, "title": "Plants of the World Online — Momordica dioica Roxb. ex Willd.(승인명, 자생지·도입지) 및 Momordica subangulata subsp. renigera (Wall. ex G.Don) W.J.de Wilde (POWO 페이지는 이 환경에서 열지 못해 WebSearch 요약으로만 확인)", "url": "https://powo.science.kew.org/taxon/293438-1", "publisher": "Royal Botanic Gardens, Kew", "accessed": A},
 pm(3, "Spine gourd (Momordica dioica Roxb.): an orphan climbing vine attaining new heights due to its healthcare properties — Front Pharmacol 2026;17:1761413 (PMID 41958941, PMC 전문 확인; 종설)", "10.3389/fphar.2026.1761413"),
 pm(4, "Phytochemical, Phytotherapeutical and Pharmacological Study of Momordica dioica — Evid Based Complement Alternat Med 2014:806082 (PMID 25197312, PMC 전문 확인; 종설)", "10.1155/2014/806082"),
 pm(5, "Genetic diversity, morphological and quality traits of Momordica dioica — Sci Rep 2024;14:30241 (PMID 39632898, PMC 전문 확인; 표·보충자료 수치는 전문 텍스트에 없음)", "10.1038/s41598-024-81828-7"),
 pm(6, "Genetic diversity in male and female landraces of teasel gourd in north-eastern India and strategies for crop improvement through induced monocliny — BMC Plant Biol 2025;25:383 (PMID 40133814, PMC 전문 확인; 대상은 M. subangulata subsp. renigera)", "10.1186/s12870-025-06400-5"),
 pm(7, "Quality attributes of convective hot air dried spine gourd (Momordica dioica Roxb. Ex Willd) slices — Food Chem 2021;347:129041 (PMID 33508585, 초록만 확인)", "10.1016/j.foodchem.2021.129041"),
 pm(8, "Anti-Allergic Effects of Kakrol (Momordica dioica Roxb.) Flesh Extract — Biosci Microbiota Food Health 2012;31(1):1-6 (PMID 24936343, PMC 전문 확인)", "10.12938/bmfh.31.1"),
 pm(9, "Dietary kakrol (Momordica dioica Roxb.) flesh inhibits triacylglycerol absorption and lowers the risk for development of fatty liver in rats — Exp Biol Med 2011;236(10):1139-46 (PMID 21791551, 초록만 확인)", "10.1258/ebm.2011.011037"),
 pm(10, "Phytochemical screening and antidiabetic effects of fruit rind of Momordica dioica Roxb. on streptozocin induced type 2 diabetic rats — Heliyon 2022;8(1):e08771 (PMID 35128091, PMC 전문 확인)", "10.1016/j.heliyon.2022.e08771"),
 pm(11, "Chemo-profiling and exploring therapeutic potential of Momordica dioica Roxb. ex Willd. for managing metabolic related disorders — J Ethnopharmacol 2024;331:118351 (PMID 38759763, 초록만 확인)", "10.1016/j.jep.2024.118351"),
 {"n": 12, "title": "Triterpenes and steroidal compounds from Momordica dioica(중국어, 영문 초록) — Yao Xue Xue Bao 1998;33(11):839-42 (PMID 12016945, 초록만 확인)", "url": "https://pubmed.ncbi.nlm.nih.gov/12016945/", "publisher": "PubMed", "accessed": A},
 pm(13, "Discovery and Characterization of Cyclic and Acyclic Trypsin Inhibitors from Momordica dioica — J Nat Prod 2019;82(2):293-300 (PMID 30673219, 초록만 확인)", "10.1021/acs.jnatprod.8b00716"),
 pm(14, "An improved micropropagation system, ex vitro rooting and validation of genetic homogeneity in wild female Momordica dioica — Physiol Mol Biol Plants 2017;23(3):713-722 (PMID 28878509, 초록만 확인)", "10.1007/s12298-017-0441-z"),
 pm(15, "Molecular cloning, characterization and expression analysis of MADS-box genes associated with reproductive development in Momordica dioica Roxb. — 3 Biotech 2018;8(3):150 (PMID 29616182, 초록만 확인)", "10.1007/s13205-018-1176-4"),
 pm(16, "Association of Tomato Leaf Curl New Delhi Virus, Betasatellite, and Alphasatellite with Mosaic Disease of Spine Gourd in India — Iran J Biotechnol 2019;17(1):e2134 (PMID 31457044, 초록만 확인)", "10.21859/ijb.2134"),
 pm(17, "Correlation and path coefficient analysis of quantitative characters in spine gourd (Momordica dioica Roxb.) — Pak J Biol Sci 2014;17(5):659-66 (PMID 26030998, 초록만 확인)", "10.3923/pjbs.2014.659.666"),
 pm(18, "In vitro propagation of spine gourd (Momordica dioica Roxb.) and assessment of genetic fidelity of micropropagated plants using RAPD analysis — Physiol Mol Biol Plants 2012;18(3):273-80 (PMID 23814442, 초록만 확인)", "10.1007/s12298-012-0109-7"),
 {"n": 19, "title": "An unusual anti-H lectin inhibited by milk from individuals with the Bombay phenotype — Immunohematology 2005;21(1):1-4 (PMID 15783298, 초록만 확인)", "url": "https://pubmed.ncbi.nlm.nih.gov/15783298/", "publisher": "PubMed", "accessed": A},
 pm(20, "Antioxidant and hepatoprotective activity of ethanolic and aqueous extracts of Momordica dioica Roxb. leaves — J Ethnopharmacol 2007;115(1):61-6 (PMID 17983713, 초록만 확인)", "10.1016/j.jep.2007.09.009"),
 pm(21, "Upcycling Surinam cherry and spine gourd fruit waste: development of anthelmintic jelly candies using fruit extracts — J Food Sci Technol 2024;61(10):1905-1918 (PMID 39285986, 초록만 확인)", "10.1007/s13197-024-05967-5"),
 pm(22, "Development of novel simple sequence repeat markers in bitter gourd (Momordica charantia L.) ... cross-species transferability — Appl Biochem Biotechnol 2014;175(1):93-118 (PMID 25240849, 초록만 확인)", "10.1007/s12010-014-1249-8"),
 pm(23, "Antiulcer Activity of Hydroalchol Extract of Momordica dioica roxb. Fruit — Indian J Pharm Sci 2011;73(5):572-7 (PMID 22923872, 초록만 확인)", "10.4103/0250-474X.99018"),
]

S = {}
S["overview"] = ("한눈에 보기", [
 "티즐고어드(Momordica dioica Roxb. ex Willd.)는 박과(Cucurbitaceae) 여주속의 여러해살이 덩굴식물로, 암그루와 수그루가 따로 있는 암수딴그루다[3, 4].",
 "영어로는 spine gourd·spiny gourd·teasel gourd, 인도에서는 kantola·kankoda 등으로 불리며, 부드러운 가시가 촘촘한 어린 열매를 채소로 먹는다[3, 4].",
 "식품의약품안전처 「식품원료 목록」에는 '티즐고어드과육'(Momordica dioica Roxb.; Palupalagakalungai, Teasle gourd)이 '사용가능' 원료로 올라 있고, 사용 가능 부위는 과육으로 한정된다[1].",
 "같은 목록에서 같은 속의 여주는 순·잎·열매(씨앗 제외), 나한과는 열매·잎, 목별은 열매가 사용 가능 부위여서 종마다 조건이 다르다[1].",
 "식품원료 목록 원자료에서 티즐고어드를 원재료로 하는 건강기능식품 고시형·개별인정형 원료 행은 찾지 못했다[1].",
 "",
 "열매에는 단백질·식이섬유·무기질과 비타민 C·카로틴이 들어 있다고 정리되어 있으나, 문헌마다 생과 기준과 건물 기준이 섞여 있어 수치를 비교할 때 기준을 꼭 확인해야 한다[3, 4, 7].",
 "혈당·지질·항산화·항알레르기 등에 관한 연구는 대부분 쥐·생쥐·세포 실험이며, 종설도 사람 대상 임상 연구가 없다고 지적한다[3].",
 "또 'kakrol'·'teasel gourd'라는 이름으로 발표된 연구 가운데에는 근연 분류군(M. subangulata subsp. renigera)을 재료로 썼을 가능성이 있는 것이 있어 해석에 주의가 필요하다[6].",
])
S["history"] = ("역사", [
 "인도 아유르베다 전통에서 열매는 이뇨·완하·간 보호·해열·항천식·혈당 조절 등에, 잎은 구충·진통 등에 쓰였다고 정리되어 있다[4].",
 "민간에서는 생과즙을 고혈압에, 기름에 조금 익힌 열매를 당뇨에 쓰고, 뿌리즙 50 mL를 하루 한 번 공복에 마시는 요법이 기록되어 있다[4].",
 "뿌리 반죽·뿌리 가루를 피부에 바르거나 암그루의 점액질 덩이뿌리를 치질·장 감염에 쓰는 등 뿌리 쪽 쓰임도 많았다[3, 4].",
 "",
 "인도에서는 장마철에 어린 열매를 감자 카레(Kheksa Aloo)나 속을 채운 요리로 먹고, 남인도에서는 Thoran·Theeyal 같은 음식에 넣는다[3].",
 "원래 숲에서 자라던 덩굴을 점차 재배하게 되었으나, 숲과 휴경지에서 암그루 덩이뿌리만 캐 가는 관행과 서식지 훼손으로 야생 집단의 유전 다양성이 줄고 있다는 지적이 있다[3].",
 "국내에서 식재료로 쓰인 역사나 유통 기록은 확인하지 못함.",
])
S["biology"] = ("식물학적 특징", [
 "줄기는 가늘고 털이 거의 없으며 덩굴손으로 다른 식물을 타고 오르고, 땅속에는 해마다 다시 싹을 틔우는 덩이뿌리가 있다[3, 5].",
 "잎은 어긋나고 넓은 달걀꼴이며 3–5갈래로 깊게 갈라진다[3].",
 "수꽃과 암꽃은 서로 다른 그루의 잎겨드랑이에 하나씩 달리며, 수꽃은 약 2.8–3.5 cm 크기에 노란 꽃잎 5장과 수술 3개를 가진다[3].",
 "열매는 길이 2.5–6.5 cm의 달걀꼴~타원형 박과 열매로 짧고 부드러운 가시가 촘촘하며, 익으면 초록에서 노랑·주황으로 바뀌고 속의 씨는 붉은 과육에 싸인다[3].",
 "",
 "꽃은 이른 아침에 피고 곤충이 꽃가루를 옮기며, 자연 상태 결실률은 약 22%이지만 손으로 꽃가루받이하면 거의 100%까지 오른다고 보고되었다[3].",
 "염색체 수는 2n = 28로 보고되었다[4, 14].",
 "POWO 검색 요약에 따르면 자생지는 인도아대륙에서 미얀마까지(파키스탄·네팔·인도·스리랑카·방글라데시·아삼·히말라야)이고, 안다만·니코바르 제도에는 도입되었다[2].",
])
S["related_species"] = ("이름과 가까운 종", [
 "여주속(Momordica)은 약 59종으로 아프리카에 47종, 아시아·오스트레일리아에 12종이 있으며, 아시아 종은 모두 암수딴그루라고 정리되어 있다[3].",
 "국내 식품원료 목록에는 같은 속의 여주(M. charantia L.)·나한과(M. grosvenorii, Siraitia grosvenorii)·목별(M. cochinchinensis, 영어 Gac)이 따로 올라 있고, 여주의 씨앗·뿌리·덩이줄기 행은 '사용불가'다[1].",
 "여주는 한해살이·암수한그루에 열매가 5–15 cm로 크고 혹이 많지만, 티즐고어드는 여러해살이·암수딴그루에 열매가 작고 부드러운 가시로 덮여 있어 구별된다[3].",
 "일본 연구는 kakrol이 여주(니가우리)보다 단맛이 있고 아스코르브산이 많아 요리에 쓰인다고 적었다[8].",
 "",
 "영어 이름 'teasel(teasle) gourd'와 방글라데시 이름 'kakrol'은 M. dioica를 가리키는 이름으로도 쓰여 왔다[4].",
 "그러나 인도 북동부 재래종을 다룬 2025년 연구는 이 지역과 방글라데시에서 재배되는 teasel gourd를 예전에는 다른 종으로 다뤘으나 지금은 M. subangulata subsp. renigera로 보며, 이 분류군은 2n = 4x = 56의 이질4배체라고 밝혔다[6].",
 "M. dioica의 염색체 수는 2n = 28로 보고되어 있으므로[4, 14], 'kakrol'·'teasel gourd'로 표시된 연구 재료가 실제로 어느 분류군인지 확인할 필요가 있다(POWO 검색 요약에서도 renigera는 M. subangulata의 아종으로 따로 등재)[2, 6].",
])
S["cultivation"] = ("재배와 산지", [
 "인도에서는 자르칸드·차티스가르·오디샤 등의 반야생 서식지와 아삼·트리푸라의 숲 지역에 자라며, 마하라슈트라·구자라트·웨스트벵골·카르나타카 등에서 재배된다[3].",
 "씨앗은 휴면성이 있어 수확 후 5–6개월 저장해야 하고 발아가 고르지 않으며, 꽃이 피기 전에는 암수를 구별할 수 없어 주로 덩이뿌리나 줄기꺾꽂이로 번식한다[3].",
 "덩이뿌리로 심은 포장은 첫해 40–50 q/ha, 씨앗·꺾꽂이로 심은 포장은 20–25 q/ha의 수량이 보고되었고, 꽃가루받이를 위해 수그루를 5–10% 섞어 심는다[3].",
 "",
 "덩이뿌리·꺾꽂이 번식은 토마토잎말림뉴델리바이러스(ToLCNDV) 같은 DNA 바이러스 모자이크병을 퍼뜨릴 수 있어 바이러스 없는 번식재료가 중요하다고 지적되었다[16].",
 "마디 절편을 이용한 기내 증식법으로 성별을 아는 암그루·수그루를 대량 증식할 수 있고, RAPD·ISSR 분석에서 어미 식물과 유전적으로 같음이 확인되었다[14, 18].",
 "인도 하이데라바드의 50개 유전자형 시험에서는 결실 기간과 그루당 열매 수가 열매 수량을 가장 크게 좌우했다[17].",
 "국내 재배 면적·생산량 통계는 확인하지 못함.",
])
S["processing"] = ("가공과 이용", [
 "주로 덜 익은 어린 열매를 볶음·카레·피클·수프에 쓰고, 어린 순과 잎도 채소로 먹는다[3, 4].",
 "다만 국내 식품원료로는 과육만 쓸 수 있으므로 순·잎·뿌리·씨앗을 원료로 쓰는 것은 목록 조건 밖이다[1].",
 "40–70 °C 열풍건조 실험에서는 건조 온도가 오를수록 아스코르브산이 29.94에서 4.50 mg/100 g으로, 엽록소가 0.34에서 0.100 mg/g으로 줄었고, 40 °C 건조 시료의 품질이 가장 좋았다[7].",
 "같은 실험에서 단백질은 4.62–12.88 g/100 g, 총페놀은 14.85–14.99 mg GAE/g 범위였다[7].",
 "",
 "일본 오키나와 이시가키에서 재배한 kakrol 과육의 물 추출물은 사람 호염기구 세포의 히스타민 방출을 억제했고, 0.5% 첨가 사료는 생쥐 피부염 모델에서 귀 병변과 혈청 IgE를 줄였다[8].",
 "kakrol 전체 동결건조 분말 3% 사료를 2주 먹인 쥐에서는 간 콜레스테롤·중성지방이 낮아지고 지방의 장 흡수가 줄었다[9].",
 "잎과 열매의 하이드로알코올 추출물을 비교한 연구에서는 열매 추출물의 항산화·α-아밀라아제·α-글루코시다아제·췌장 리파아제 억제 활성이 더 컸고, LC-QTOF-MS로 16개 대사물질이 동정되었다[11].",
 "열매 부산물 추출물을 넣은 젤리 캔디를 만든 식품 개발 사례도 있다[21].",
])
S["genetics"] = ("유전 정보", [
 "티즐고어드는 2n = 28의 이배체 암수딴그루 식물로 보고되었다[4, 14].",
 "꽃눈에서 MADS-box 전사인자 유전자 17개(MIKC형 11개, MIKC*형 4개, Mα형 2개)가 클로닝되었고, MIKC*형은 수배우체 발달, Mα형은 암배우체·종자 발달과 관련된다고 보고되었다[15].",
 "인도 구자라트의 암그루 계통 21개를 23개 형질로 평가한 연구에서는 열매 무게·그루당 열매 수·아스코르브산 등에서 유전 변이가 컸고, 계통들이 세 무리로 나뉘었다[5].",
 "",
 "이 연구를 바탕으로 둥글고 씨가 적은 품종 Thar Varsha(CHESSG-1)와 우량 계통 CHESSG-11·CHESSG-14가 선발되었다[5].",
 "인도에서는 Indira Kankoda 1·2, Chhattisgarh Kankoda 2 같은 품종의 수량이 30–45 q/ha로 보고되었다[3].",
 "여주용으로 개발한 SSR 표지 가운데 상당수가 M. dioica를 포함한 여주속 6종에 옮겨 쓸 수 있었다[22].",
 "이 종의 전체 유전체 해독 정보는 확인하지 못함.",
])
S["safety"] = ("안전성", [
 "식약처 「식품원료 목록」에서 티즐고어드는 과육만 식품원료로 쓸 수 있는 '사용가능' 원료다[1].",
 "이 종에 대한 국내외 공공기관의 알레르기·농약 잔류·독성 평가 자료는 확인하지 못함.",
 "종설에 따르면 뿌리 추출물은 쥐에서 에스트로겐 유사 작용을 보였고, 200 mg/kg에서 물 추출물 83%, 에탄올 추출물 100%의 낙태 작용이 보고되었다[4].",
 "씨앗에는 트립신 억제 펩타이드(Modi 1–6)와 적혈구를 응집시키는 항-H 렉틴이 들어 있다[13, 19].",
 "",
 "열매에서 분리한 사포닌을 OECD 지침에 따라 쥐에 투여한 시험에서 5,000 mg/kg 단회 투여는 급성독성이 없었고, 1,000 mg/kg 아급성 투여에서 경미한 독성이, 100·250 mg/kg 장기 투여에서는 이상이 없었다고 종설이 정리했다[3].",
 "열매 추출물의 혈당·지질 개선, 위궤양 억제, 신장 보호, 항알레르기 효과와 잎 추출물의 간 보호 효과는 모두 쥐·생쥐·세포 실험 결과이다[3, 8, 10, 20, 23].",
 "사람에게 같은 효과나 안전한 섭취량이 있는지는 확인되지 않았으며, 종설도 표준화된 용량이 정해지지 않았다고 밝혔다[3].",
])

sections = []
for k in ["overview","history","biology","related_species","cultivation","processing","genetics","safety"]:
    t, ss = S[k]
    paras, cur = [], []
    for s in ss:
        if s == "":
            paras.append(" ".join(cur)); cur = []
        else:
            cur.append(s)
    if cur: paras.append(" ".join(cur))
    sections.append({"key": k, "title": t, "body": "\n\n".join(paras)})

C = lambda name, ko, cls, role, part, content, act, src: {"name": name, "name_ko": ko, "class": cls, "role": role, "part": part, "content_text": content, "activity_ko": act, "source": src}
compounds = [
 C("Ascorbic acid", "아스코르브산(비타민 C)", "비타민", "nutrient", "열매(열풍건조 절편)", "40→70 °C 건조 시 29.94→4.50 mg/100 g(초록 값, 생/건 기준 초록에 없음)[7]; 암그루 계통 21개 사이 유전 변이 큼(수치는 표에 있어 확인 못함)[5]", "항산화 비타민; 열에 약해 건조 온도가 높을수록 줄어듦[7]", [5, 7]),
 C("beta-Carotene", "베타카로틴(카로틴)", "카로티노이드", "nutrient", "열매 가식부", "162 mg/100 g 가식부(종설 인용값을 단위 그대로 옮김; 1차 자료 확인 못함)[4]", "박과 채소 가운데 카로틴이 가장 많다고 종설이 적음[4]", [4]),
 C("Chlorophyll", "엽록소", "색소", "bioactive", "열매(열풍건조 절편)", "건조 온도 상승에 따라 0.34→0.100 mg/g(초록 값)[7]", "가공 중 녹색 품질 지표[7]", [7]),
 C("Phytic acid", "피트산", "인 저장 화합물", "bioactive", "열매", "2.8 mg/g(종설이 인용한 값)[4]", "무기질 흡수를 낮출 수 있는 항영양 성분[4]", [4]),
 C("Oleic acid", "올레산", "지방산", "nutrient", "부위 원문에 명확하지 않음(종설 표 4 '지방산 조성')", "총지방산의 56.253%[3]", "주요 단일불포화지방산[3]", [3]),
 C("Linoleic acid", "리놀레산", "지방산", "nutrient", "부위 원문에 명확하지 않음(종설 표 4)", "총지방산의 22.511%(α-리놀렌산 1.943%, 팔미트산 12.157%)[3]", "필수 다중불포화지방산[3]", [3]),
 C("Ursolic acid", "우르솔산", "트라이테르페노이드", "bioactive", "부위 명시 없음(종설)", "함량 확인 못함; 우르솔산계 트라이테르펜과 3-O-벤조일-11-옥소-우르솔산 등이 보고됨[4]", "항염 등 활성이 알려진 트라이테르펜 골격[4]", [4]),
 C("Oleanolic acid", "올레아놀산", "트라이테르페노이드", "bioactive", "뿌리(식품원료 사용 부위 아님)", "함량 확인 못함[3, 4]", "뿌리에서 헤데라게닌·집소게닌과 함께 보고됨[3]", [3, 4]),
 C("alpha-Spinasterol 3-O-beta-D-glucopyranoside", "α-스피나스테롤 3-O-β-D-글루코사이드", "스테롤 배당체", "bioactive", "건조 뿌리(식품원료 사용 부위 아님)", "분리·구조 동정(함량 없음)[12]", "L1210 백혈병 세포 성장 4 μg/mL에서 50% 억제(세포 실험)[12]", [12]),
 C("Gypsogenin 3-O-beta-D-glucuronopyranoside", "집소게닌 3-O-β-D-글루쿠로노사이드", "트라이테르펜 사포닌", "bioactive", "건조 뿌리(식품원료 사용 부위 아님)", "신규 화합물로 분리(함량 없음)[12]", "L1210 세포 실험에서 항암 활성 보고[12]", [12]),
 C("Hederagenin 3-O-beta-D-glucopyranoside", "헤데라게닌 3-O-β-D-글루코사이드", "트라이테르펜 사포닌", "bioactive", "건조 뿌리(식품원료 사용 부위 아님)", "분리(함량 없음)[12]", "L1210 세포 실험에서 항암 활성 보고[12]", [12]),
 C("Momordica dioica trypsin inhibitors (Modi 1-6)", "트립신 억제 펩타이드(Modi 1–6)", "고리형·선형 펩타이드", "bioactive", "씨앗(식품원료 사용 부위 아님)", "6종 발견(고리형 5종, 선형 1종), 함량 없음[13]", "트립신 억제; 암·곤충 세포 독성 없음, 사람 혈청에서 24시간 안정[13]", [13]),
 C("Anti-H lectin", "항-H 렉틴", "렉틴(단백질)", "bioactive", "씨앗(식품원료 사용 부위 아님)", "추출물에서 적혈구 응집 활성 확인(함량 없음)[19]", "O형 적혈구를 가장 강하게 응집시키는 H 항원 특이 렉틴[19]", [19]),
]

nutrients = [
 {"form": "생과(가식부 100 g)", "basis": "종설[4]이 인용한 값; 1차 자료 확인 못함", "items": [
   {"name": "수분", "value": 84.1, "unit": "%"}, {"name": "탄수화물", "value": 7.7, "unit": "g/100 g"},
   {"name": "단백질", "value": 3.1, "unit": "g/100 g"}, {"name": "지방", "value": 3.1, "unit": "g/100 g"},
   {"name": "식이섬유", "value": 3.0, "unit": "g/100 g"}, {"name": "무기질", "value": 1.1, "unit": "g/100 g"}], "source": [4]},
 {"form": "열매 건물", "basis": "종설[4]이 인용한 건물 기준 값(%·kcal/100 g·mg/100 g 원문 단위)", "items": [
   {"name": "회분", "value": 9.1, "unit": "%"}, {"name": "조단백질", "value": 5.44, "unit": "%"},
   {"name": "조지방", "value": 3.25, "unit": "%"}, {"name": "조섬유", "value": 22.9, "unit": "%"},
   {"name": "탄수화물", "value": 59.31, "unit": "%"}, {"name": "에너지", "value": 288.25, "unit": "kcal/100 g"},
   {"name": "칼륨", "value": 4.63, "unit": "mg/100 g"}, {"name": "나트륨", "value": 1.62, "unit": "mg/100 g"},
   {"name": "칼슘", "value": 7.37, "unit": "mg/100 g"}, {"name": "철", "value": 5.04, "unit": "mg/100 g"},
   {"name": "아연", "value": 3.83, "unit": "mg/100 g"}], "source": [4]},
]

conds_empty = {k: "" for k in ["instrument","column","mobile_phase","gradient","flow","temp","detection","injection","sample_prep","standard","linearity","lod","loq","recovery"]}
c1 = dict(conds_empty)
c1.update({
 "instrument": "원심분리기(10,000 rpm), 적정",
 "detection": "염료 적정에서 분홍색이 나타나는 종말점(결과는 mg/100 g 생체중으로 표시)",
 "sample_prep": "열매를 흐르는 수돗물로 씻어 물기를 뺀 뒤 신선 시료를 막자사발에서 6%(w/v) 메타인산–2 mol/L 아세트산 혼합액 20 mL로 균질화; 10,000 rpm, 15분, 4 °C 원심분리; 상등액을 Whatman No. 1 여과지로 거름",
})
assays = [
 {"role": "literature", "compound": "Ascorbic acid", "compound_ko": "아스코르브산(비타민 C)", "part": "열매(인도 구자라트 고드라, 암그루 계통 21개, 신선 열매)",
  "content": "계통별 수치는 표에 있어 전문 텍스트에서 확인 못함; 유전 변이(PCV 15.01, GCV 14.99, 평균 대비 유전 진보 115.58%)만 확인[5]",
  "method": "염료 적정법(원문은 'DNPH 법'이라 적었으나 기술된 절차는 염료 적정)", "conditions": c1,
  "rationale": "품질 형질로 비타민 C를 측정해 계통 선발에 썼음; 표준물질·검량·검출한계·회수율은 원문에 없음[5].",
  "source": [5], "url": "https://doi.org/10.1038/s41598-024-81828-7", "source_kind": "paper"},
 {"role": "literature", "compound": "Ascorbic acid", "compound_ko": "아스코르브산(비타민 C)", "part": "열매 절편(40·50·60·70 °C 열풍건조)",
  "content": "건조 온도가 오를수록 29.94→4.50 mg/100 g(초록 값)[7]",
  "method": "확인 못함(초록만 확인)", "conditions": dict(conds_empty),
  "rationale": "열에 약한 비타민 C를 건조 품질 지표로 썼음; 전문 확인 못함[7].",
  "source": [7], "url": "https://doi.org/10.1016/j.foodchem.2021.129041", "source_kind": "paper"},
]

d = {"slug": "momordica-dioica", "name_ko": "티즐고어드", "name_en": "Spine gourd (teasle gourd)",
     "scientific_name": "Momordica dioica Roxb. ex Willd.",
     "aliases": ["티즐고어드과육", "Teasle gourd", "Palupalagakalungai", "Spine gourd", "Spiny gourd", "Kantola", "Kankoda", "Kakrol", "Momordica dioica Roxb."],
     "sections": sections, "compounds": compounds, "markers": [], "nutrients": nutrients, "assays": assays,
     "production": [], "world": [], "gi": [], "orgs": [], "sources": sources}
(P / "dossier.json").write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in sections: print(s["key"], len(s["body"]))
