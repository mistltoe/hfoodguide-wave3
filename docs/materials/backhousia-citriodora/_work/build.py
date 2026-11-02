import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
A = "2026-11-02"
def pm(n, title, doi, note):
    return {"n": n, "title": f"{title} ({note})", "url": f"https://doi.org/{doi}", "publisher": "PubMed", "accessed": A}
sources = [
 {"n": 1, "title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 레몬머틀잎·레몬머틀잎추출액(Backhousia citriodora F. Muell.; Lemon myrtle), 식품원료(A코드), 사용가능, 사용가능부위: 잎; 대조 행: 레몬그라스(Cymbopogon citratus, 줄기·잎 사용가능), 레몬버베나(Aloysia citrodora, 잎), 레몬밤(Melissa officinalis, 잎), 레몬유칼립투스(Eucalyptus citriodora, 사용불가), 마텔잎(Myrtus communis, 사용불가), 도금양열매(Rhodomyrtus tomentosa, 영명 Myrtle, 열매 사용가능)", "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
 pm(2, "Backhousia citriodora F. Muell. (Lemon Myrtle), an Unrivalled Source of Citral — Foods 2021 (리뷰)", "10.3390/foods10071596", "PMID 34359465, PMC 전문 확인"),
 pm(3, "Review of the Leaf Essential Oils of the Genus Backhousia Sens. Lat. — Plants (Basel) 2022 (리뷰)", "10.3390/plants11091231", "PMID 35567231, PMC 전문 확인"),
 pm(4, "Chemical Composition, Antioxidant, Antibacterial, and Antibiofilm Activities of Backhousia citriodora Essential Oil — Molecules 2022", "10.3390/molecules27154895", "PMID 35956846, PMC 전문 확인"),
 pm(5, "Lemon Myrtle (Backhousia citriodora) Extract and Its Active Compound, Casuarinin, Activate Skeletal Muscle Satellite Cells In Vitro and In Vivo — Nutrients 2022", "10.3390/nu14051078", "PMID 35268053, PMC 전문 확인"),
 pm(6, "Safety Assessment of Lemon Myrtle Extract: 28-Day Oral Toxicity Study in Rats and In Vitro and In Vivo Genotoxicity Studies — Toxics 2026", "10.3390/toxics14030213", "PMID 41893481, PMC 전문 확인"),
 pm(7, "Low-Dose Lemon Myrtle Supplementation Enhances Muscle Hypertrophy in Older Adults Undergoing Low-Load Resistance Training: A Randomized Controlled Trial — J Aging Res 2026", "10.1155/jare/8887586", "PMID 41635673, 초록 확인"),
 pm(8, "Lemon myrtle extract enhances muscle hypertrophy induced by low-load bodyweight resistance training in older adults: two independent randomized controlled trials — J Nutr Health Aging 2025", "10.1016/j.jnha.2025.100706", "PMID 41076797, 초록 확인"),
 pm(9, "Effects of different drying methods on extractable phenolic compounds and antioxidant properties from lemon myrtle dried leaves — Heliyon 2019", "10.1016/j.heliyon.2019.e03044", "PMID 31890968, PMC 전문 확인"),
 pm(10, "Toxicity of Australian essential oil Backhousia citriodora (Lemon myrtle). Part 1. Antimicrobial activity and in vitro cytotoxicity — Food Chem Toxicol 2002", "10.1016/s0278-6915(01)00103-x", "PMID 11893412, 초록 확인"),
 pm(11, "Toxicity of Australian essential oil Backhousia citriodora (lemon myrtle). Part 2. Absorption and histopathology following application to human skin — Food Chem Toxicol 2003", "10.1016/s0278-6915(03)00159-5", "PMID 12909275, 초록 확인"),
 pm(12, "Bioactivity of Backhousia citriodora: antibacterial and antifungal activity — J Agric Food Chem 2003", "10.1021/jf0258003", "PMID 12502388, 초록 확인"),
 pm(13, "Essential oil of Australian lemon myrtle (Backhousia citriodora) in the treatment of molluscum contagiosum in children — Biomed Pharmacother 2004", "10.1016/j.biopha.2003.11.006", "PMID 15183850, 초록 확인"),
 pm(14, "Molluscum Contagiosum Treatments in Children: A Systematic Review with Network Meta-Analysis — Paediatr Drugs 2026", "10.1007/s40272-026-00758-1", "PMID 42360610, 초록 확인"),
 pm(15, "Antioxidant and anti-inflammatory activities of phenolic compounds extracted from lemon myrtle leaves at various extraction conditions — Food Sci Biotechnol 2020", "10.1007/s10068-020-00795-7", "PMID 32999750, 초록 확인"),
 pm(16, "Anti-inflammatory and anti-oxidative activities of lemon myrtle (Backhousia citriodora) leaf extract — Toxicol Rep 2020", "10.1016/j.toxrep.2020.01.018", "PMID 32071880, 초록 확인"),
 pm(17, "Composition of native Australian herbs polyphenolic-rich fractions and in vitro inhibitory activities against key enzymes relevant to metabolic syndrome — Food Chem 2012", "10.1016/j.foodchem.2012.02.217", "PMID 23107721, 초록 확인"),
 pm(18, "Vitamin D Content of Australian Native Food Plants and Australian-Grown Edible Seaweed — Nutrients 2018", "10.3390/nu10070876", "PMID 29986447, 초록 확인"),
 pm(19, "Effect of packaging materials and storage on major volatile compounds in three Australian native herbs — J Agric Food Chem 2013", "10.1021/jf400845t", "PMID 23682630, 초록 확인"),
 pm(20, "Molecular cloning and characterization of a linalool synthase from lemon myrtle — Biosci Biotechnol Biochem 2011", "10.1271/bbb.100922", "PMID 21737936, 초록 확인"),
 pm(21, "Crystallization and preliminary X-ray analysis of geraniol dehydrogenase from Backhousia citriodora (lemon myrtle) — Acta Cryst F 2011", "10.1107/S1744309111006920", "PMID 21636906, 초록 확인"),
 pm(22, "Authenticity control of essential oils containing citronellal and citral by chiral and stable-isotope gas-chromatographic analysis — Anal Bioanal Chem 2006", "10.1007/s00216-006-0842-2", "PMID 17089103, 초록 확인"),
 pm(23, "Phytochemical Composition and Toxicological Screening of Anise Myrtle and Lemon Myrtle Using Zebrafish Larvae — Antioxidants 2024", "10.3390/antiox13080977", "PMID 39199222, 초록 확인"),
 pm(24, "Drug-Induced Liver Injury from Herbal Liver Detoxification Tea — Case Rep Gastroenterol 2022 (증례 보고)", "10.1159/000526311", "PMID 36636365, 초록 확인"),
 pm(25, "Citral in lemon myrtle, lemongrass, litsea, and melissa essential oils suppress the growth and invasion of breast cancer cells — BMC Complement Med Ther 2024", "10.1186/s12906-024-04511-4", "PMID 38831283, 초록 확인"),
 pm(26, "Essential oil of lemon myrtle (Backhousia citriodora) induces S-phase cell cycle arrest and apoptosis in HepG2 cells — J Ethnopharmacol 2023", "10.1016/j.jep.2023.116493", "PMID 37054823, 초록 확인"),
]

S = {}
S["overview"] = ("레몬머틀(Backhousia citriodora F. Muell.)은 도금양과(Myrtaceae)에 속하는 상록 교목으로, 오스트레일리아 퀸즐랜드 동부 해안 지역에만 자생한다[2, 3]. "
"잎을 수증기 증류해 얻는 정유에는 시트랄(게라니알+네랄)이 보통 90–98% 들어 있어, 알려진 천연 원료 가운데 시트랄 함량이 가장 높다고 평가된다[2]. "
"식약처 「식품원료 목록」에는 원료명 '레몬머틀잎'과 '레몬머틀잎추출액'(학명 Backhousia citriodora F. Muell., 영명 Lemon myrtle)이 '사용가능'으로 올라 있다[1]. "
"두 원료의 사용 조건은 '사용가능부위 : 잎'으로, 식품에는 잎만 쓸 수 있다[1]. "
"이 종을 원재료로 하는 건강기능식품 고시형 원료는 확인하지 못함.\n\n"
"잎은 말린 허브·차·향신료로 쓰이고, 정유는 레몬 향을 내는 향료와 화장품·생활용품 원료로 쓰인다[2]. "
"잎 물 추출물은 엘라지타닌인 카수아리닌과 퀘르시트린 등 페놀 성분을 함유하며, 이 추출물(하루 250 mg 또는 125 mg)을 저강도 근력운동과 함께 먹은 일본 고령자 무작위 대조시험에서 넓적다리 앞쪽 근육 두께가 위약군보다 더 늘었다는 보고가 있다[5, 7, 8]. "
"다만 두 시험 가운데 하나는 통계적으로 유의하지 않았고 보조 지표(보행 속도 등)에는 차이가 없어, 효과 크기와 임상적 의미는 아직 더 확인이 필요하다[8].")

S["history"] = ("종소명 citriodora는 잎의 뚜렷한 레몬 향에서 왔고, 처음 'lemon-scented myrtle'이라 불리다가 토종 식품 산업에서 잎을 요리용으로 팔면서 'lemon myrtle'로 줄여 부르게 되었다[2]. "
"'Sweet verbena myrtle', 'lemon ironwood'라는 영어 이름도 쓰인다[2, 4]. "
"이 종의 잎 정유는 1888년 독일의 한 향료 회사가 거의 대부분(95%)이 시트랄이라고 처음 보고했고, 1923년 오스트레일리아 연구로 다시 확인되었다[3]. "
"그 뒤 이 정유는 시트랄을 더 값비싼 향료 성분인 이오논으로 바꾸는 원료로 쓰였다[3].\n\n"
"생잎이나 말린 잎은 민간에서 상처·피부 감염 등에 전통적으로 쓰였다고 전해진다[26]. "
"재배 농장에서 나온 잎과 정유가 상업적으로 거래되면서 2001년 오스트레일리아 표준(AS 4941-2001)으로 '시트랄형 레몬머틀유' 규격이 만들어졌다[2]. "
"이 규격은 2018년 국제표준화기구(ISO) 정유위원회에 제안되어 국제표준으로 채택되는 절차를 밟았다[2]. "
"정유 10% 용액을 전염성 물렁종 어린이에게 21일 바른 소규모 시험에서는 정유군 16명 중 9명, 대조군 16명 중 0명이 병변 90% 이상 감소를 보였다[13]. "
"2026년 소아 대상 네트워크 메타분석은 이 결과가 단일 시험에서 나온 것이라 추가 검증이 필요하다고 보았다[14].")

S["biology"] = ("레몬머틀은 다 자라면 키 8 m 안팎이고 30 m까지 크기도 하지만 보통은 더 작다[2]. "
"잎은 마주나는 상록 피침형으로 길이 4–15 cm, 너비 1–5 cm이며 광택이 나는 녹색이고 가장자리가 밋밋하다[2]. "
"꽃은 지름 5–7 mm의 크림빛 흰색으로 여름부터 가을까지 가지 끝에 모여 피고, 꽃잎이 떨어진 뒤에도 꽃받침이 남는다[2].\n\n"
"자생지는 퀸즐랜드의 선샤인코스트(누사·마루치도어 등)에서 매카이·타운즈빌·허버턴 지역까지 이어지는 동부 열대·아열대 우림이다[2, 3]. "
"토지 개간으로 여러 자생 집단이 고립된 나무 몇 그루로 줄었다[3]. "
"이 종에는 정유 화학형이 둘 있는데, 흔한 시트랄형은 시트랄이 주성분이고 드문 시트로넬랄형은 L-시트로넬랄이 62–80%를 차지한다[2, 3]. "
"두 화학형은 겉모습으로는 구별되지 않고 정유 냄새와 성분으로만 나뉜다[3]. "
"잎 정유 수율은 시트랄형에서 생잎 기준 1.1–3.2%로 보고되었다[2, 3].")

S["related_species"] = ("Backhousia 속은 현재 13종이 인정되며, 한 종(서오스트레일리아 킴벌리 지역)을 빼고 모두 오스트레일리아 동부의 우림·숲에 자란다[3]. "
"같은 속의 시나몬머틀(B. myrtifolia)은 엘레미신·메틸유제놀 같은 방향족 에테르가 주성분인 화학형이 있고, 다른 종들은 주로 α-피넨 같은 모노테르펜이나 세스퀴테르펜이 많아 시트랄이 주성분인 레몬머틀과 뚜렷이 다르다[3]. "
"아니스머틀은 예전에 Backhousia anisata로 불렸으나 지금은 Syzygium anisatum으로 옮겨졌고, 정유 주성분은 아네톨이다[3].\n\n"
"레몬 향 시트랄을 많이 내는 다른 식물로 레몬그라스(Cymbopogon), 리트세아(Litsea cubeba), 레몬밤(Melissa officinalis)이 있으며, 이들 정유도 시트랄이 주성분이어서 성분 연구가 함께 비교되곤 한다[25]. "
"식약처 목록에서 레몬그라스(Cymbopogon citratus)는 줄기·잎, 레몬버베나(Aloysia citrodora)와 레몬밤은 잎이 '사용가능'이지만 이름이 비슷한 레몬유칼립투스(Eucalyptus citriodora)와 마텔잎(Myrtus communis, 머틀)은 '사용불가'이다[1]. "
"영명이 'Myrtle'인 도금양열매(Rhodomyrtus tomentosa)도 별개의 종이므로 이름만으로 섞지 않아야 한다[1]. "
"시트로넬랄형 레몬머틀유는 시트로넬라·레몬유칼립투스 기름과 비슷하지만, L형(왼쪽) 시트로넬랄이라는 점이 다르다[2]. "
"이런 정유의 진위는 키랄 GC와 안정동위원소 비로 가릴 수 있다[22].")

S["cultivation"] = ("상업 재배 농장은 퀸즐랜드 북부에서 뉴사우스웨일스 북부까지 조성되어 있으며, 큰 농장은 200에이커와 70에이커 규모로 해마다 줄기 달린 생잎 2,400톤 이상을 생산한다고 보고되었다[2]. "
"나무는 자생지 근처에서 가장 잘 자라고, 물을 좋아하지만 뿌리가 늘 젖어 있는 것은 싫어한다[2]. "
"서리에 약해 영하로 내려가는 밤이 이틀 이상 이어지면 묘목이 죽을 수 있다[2]. "
"배수가 잘되는 약산성 토양이 알맞고 석회는 권하지 않으며, 심어 놓은 처음 몇 해는 관수가 꼭 필요하다[2]. "
"질소 비료에 잘 반응하지만 너무 많이 주면 지상부만 무거워지고 잎 정유 품질이 떨어진다[2].\n\n"
"차나무(tea tree)처럼 밑동 가까이 베어도 다시 움트는 성질이 약해, 잎은 손으로 따거나 기계로 가지 끝을 잘라 수확한다[2]. "
"말레이시아 말라카의 유기농 농장에서도 재배되어 정유 연구에 쓰였다[4]. "
"국내 재배·생산 통계는 확인하지 못함.")

S["processing"] = ("잎과 가지 끝을 수증기 증류해 시트랄이 많은 정유를 얻으며, 시트랄형 정유 수율은 생잎 기준 1.1–3.2%, 상업 설비에서는 잔가지 포함 1.5% 수준이다[2]. "
"알데하이드가 많은 기름이라 GC 분석 때 에탄올·아세톤 같은 용매에 오래 두면 아세탈 등이 생겨 결과가 틀어질 수 있다[2]. "
"잎은 생잎·건조 잎·분쇄 허브 형태로 레몬 허브차, 빵·과자·치즈·잼·파스타·식초 등의 향미 재료로 쓰인다[2].\n\n"
"잎 건조 방법 비교에서 동결건조가 페놀 성분을 가장 많이 보존했지만 에너지가 많이 들어, 산업 규모에서는 전자레인지 건조(960 W, 7분)나 열풍 건조(90 °C, 75분)가 실용적이라고 제안되었다[9]. "
"건조 잎을 저밀도 폴리에틸렌 봉지에 6개월 두면 주요 휘발 성분이 87% 줄었으나, 알루미늄 포일 적층 포장에서는 손실이 23%였다[19]. "
"근육 연구에 쓰인 잎 물 추출물은 건조 잎을 8배 부피의 물로 80 °C에서 1시간 추출·농축한 뒤 덱스트린과 함께 분무건조해 만들었다[6]. "
"잎을 에탄올로 추출할 때는 80 °C·6시간 조건에서 총폴리페놀이 102.72 mg GAE/g(건조 기준)으로 가장 높았다[15]. "
"알코올 추출물은 쥐 대식세포(RAW 264.7)에서 NO·IL-6·TNF-α 생성을 줄였으나, 이는 세포 실험 결과이다[15, 16]. "
"잎 차(0.2 g/mL)와 증류 부산물인 하이드로졸은 항균 활성이 거의 없었다[12]. "
"이 원료로 만든 국내 건강기능식품 생산실적은 확인하지 못함.")

S["genetics"] = ("시트로넬랄형은 씨로 번식하면 형질이 그대로 이어지지 않는다[2]. "
"시트로넬랄형 한 나무에서 받은 씨의 자손은 시트로넬랄형과 시트랄형이 약 1:1(1.05:1)로 갈렸고, 시트랄형끼리의 자손에서는 48그루 가운데 3그루만 시트로넬랄형이었다[2]. "
"시트랄 함량을 높이려는 육종 시험에서도 자연수분 16가계 272그루 가운데 3그루만 L-시트로넬랄 기름을 냈다[3].\n\n"
"정유 생합성 유전자로는 제라닐 이인산을 (−)-리날로올로 바꾸는 리날로올 합성효소 유전자(BcLS)가 클로닝되었고, 이 유전자는 나무 전체에서 발현되며 자스몬산 처리로 늘어났다[20]. "
"게라니올을 산화하는 게라니올 탈수소효소(BcGEDH)는 대장균에서 만들어 결정화되었고 2.3 Å 해상도의 X선 자료가 얻어졌다[21]. "
"엽록체·핵 DNA를 합친 계통 분석에서 Backhousia 속은 네 개의 강하게 지지되는 분계군으로 나뉘었고, 예전 Choricarpia 속 두 종이 이 속으로 합쳐졌다[3]. "
"레몬머틀의 전체 유전체 해독 자료는 확인하지 못함.")

S["safety"] = ("식약처 「식품원료 목록」에서 레몬머틀잎·레몬머틀잎추출액은 잎에 한해 '사용가능' 원료이다[1]. "
"정유 주성분 시트랄은 미국 FDA의 GRAS(일반적으로 안전하다고 인정) 목록에 올라 있다[2]. "
"알레르기·잔류물 등 국내 공공기관의 안전 정보는 확인하지 못함.\n\n"
"정유와 시트랄은 사람 세포(간암 세포주 HepG2, 피부 섬유모세포)에 세포독성이 강해 IC50가 0.003–0.014%(w/v)였으나, 정유 1% 제품은 독성이 낮게 나왔다[10]. "
"떼어 낸 사람 피부에 원액을 바르면 시트랄만 흡수되었고 각질층 손상, 세포 괴사(최대 15%)와 공포 변성(최대 25%)이 관찰되었다[11]. "
"이런 결과로 국소 제품에는 1% 미만으로 쓰도록 권고되고, 동물 생식독성 자료 때문에 시트랄이 많은 정유는 임신 중 사용을 제한하자는 견해가 있다[2]. "
"시트랄은 토끼 피부 자극과 기니피그 피부 감작을 일으키며, 발생독성 NOAEL은 경구 200 mg/kg bw/일로 정리되어 있다[6].\n\n"
"잎 물 추출물은 복귀돌연변이(Ames) 시험의 TA98 균주에서 양성이었으나 생쥐 소핵 시험과 쥐 코멧 시험은 음성이었고, 쥐 28일 반복 경구투여 NOAEL은 1,000 mg/kg bw/일이었다[6]. "
"제브라피시 유생에서 잎 추출물의 96시간 LC50는 270 mg/L였다[23]. "
"레몬머틀잎이 든 여러 허브 혼합 해독차를 마신 뒤 담즙정체성 간 손상이 생긴 증례가 1건 보고되었지만, 어느 성분 때문인지는 밝혀지지 않았다[24].")

sections = [{"key": k, "title": t, "body": S[k]} for k, t in [
 ("overview", "한눈에 보기"), ("history", "역사와 이름"), ("biology", "식물학적 특징"), ("related_species", "가까운 종과 혼동 주의"),
 ("cultivation", "재배와 산지"), ("processing", "가공과 이용"), ("genetics", "유전 정보"), ("safety", "안전성")]]

def C(name, ko, cls, role, part, content, act, src):
    return {"name": name, "name_ko": ko, "class": cls, "role": role, "part": part, "content_text": content, "activity_ko": act, "source": src}
compounds = [
 C("Geranial", "게라니알(시트랄 a, (E)-시트랄)", "모노테르펜 알데하이드", "marker", "잎(정유)",
   "말레이시아산 잎 정유 52.13%(GC 면적비)[4]; 오스트레일리아산 46.1–60.7%[4]; 시트랄(게라니알+네랄) 합계는 증류 정유의 90–98%[2]",
   "레몬 향의 핵심 성분; 정유 항균·항산화 활성의 주요 원인으로 제시(시험관)[4]", [2, 4]),
 C("Neral", "네랄(시트랄 b, (Z)-시트랄)", "모노테르펜 알데하이드", "marker", "잎(정유)",
   "말레이시아산 잎 정유 37.65%(GC 면적비)[4]; 오스트레일리아산 32.0–40.9%[4]",
   "게라니알과 함께 시트랄을 이룸; 휘발 시트랄의 유방암 세포 증식 억제 IC50 1.31 μL/mL(시험관)[25]", [4, 25]),
 C("Citronellal", "L-시트로넬랄", "모노테르펜 알데하이드", "bioactive", "잎(정유)",
   "시트로넬랄형 나무 정유 62–80%(생잎 수율 0.5–0.9%), 1년생 육종 개체 85–89%[2]; 시트랄형 정유에서는 0.1–0.9%[4]",
   "드문 화학형의 지표; 곤충 기피 용도로 거론[2]", [2, 4]),
 C("Isocitral", "이소시트랄(이소게라니알·이소네랄)", "모노테르펜 알데하이드", "bioactive", "잎(정유)",
   "이소게라니알 1.0–4.2%, 이소네랄 0.6–2.7%(오스트레일리아산)[4]; (E)·(Z)-이소시트랄과 exo-이소시트랄 확인[3]",
   "시트랄의 산화·열·산염기 재배열로 생기는 것으로 여겨지는 부성분[2]", [2, 3, 4]),
 C("Linalool", "리날로올", "모노테르펜 알코올", "bioactive", "잎(정유)",
   "0.3–1.0%(오스트레일리아산 정유)[4]",
   "생합성 효소(BcLS)가 레몬머틀에서 클로닝됨[20]", [4, 20]),
 C("Geraniol", "게라니올", "모노테르펜 알코올", "bioactive", "잎(정유)",
   "오스트레일리아 표준 개정에서 0.5–2.5% 범위로 정함[2]",
   "시트랄의 전구 알코올; 게라니올 탈수소효소(BcGEDH)가 이 종에서 결정화됨[21]", [2, 21]),
 C("6-Methyl-5-hepten-2-one", "6-메틸-5-헵텐-2-온", "케톤", "bioactive", "잎(정유)",
   "0.1–2.5%(오스트레일리아산 정유)[4]", "정유 향 부성분[4]", [4]),
 C("beta-Myrcene", "β-미르센", "모노테르펜 탄화수소", "bioactive", "잎(정유)",
   "0.22%(말레이시아산)[4]; 0.1–0.7%(오스트레일리아산)[4]", "정유 부성분; 시트랄과 함께 항균 작용을 보탠다는 보고 인용[4]", [4]),
 C("Casuarinin", "카수아리닌", "엘라지타닌", "marker", "잎(물 추출물)",
   "잎 물 추출물 16.1 mg/g(HPLC)[5]; 같은 공정 추출물 건조중량 기준 1.61%[6]",
   "골격근 위성세포 활성화(세포, 쥐 4–8 mg/kg/일 경구)[5]; 사람 시험 추출물 하루 250 mg에 카수아리닌 2.5 mg[7]", [5, 6, 7]),
 C("Quercitrin", "퀘르시트린", "플라보놀 배당체", "bioactive", "잎(물 추출물)",
   "잎 물 추출물 38.8 mg/g, 5개 정량 성분 가운데 최다(HPLC)[5]; 건조중량 기준 3.88%[6]",
   "위성세포 활성화 효과 없음(세포)[5]; 추출물 Ames TA98 양성의 후보 원인으로 거론[6]", [5, 6]),
 C("Hyperoside", "하이퍼린(하이페로사이드)", "플라보놀 배당체", "bioactive", "잎(물 추출물)",
   "건조중량 기준 1.91%(HPLC)[6]", "위성세포 활성화 효과 없음(세포)[5]", [5, 6]),
 C("Myricitrin", "미리시트린", "플라보놀 배당체", "bioactive", "잎(물 추출물)",
   "건조중량 기준 1.26%(HPLC)[6]", "위성세포 활성화 효과 없음(세포)[5]", [5, 6]),
 C("Gallic acid", "갈산", "페놀산", "bioactive", "잎",
   "동결건조 잎 53.77 mg/g 건조중량(HPLC-UV)[9]; 잎 물 추출물 2.5 mg/g[5]",
   "잎 항산화능과 강한 상관(시험관)[9]", [5, 9]),
 C("Hesperetin", "헤스페레틴", "플라바논", "bioactive", "잎",
   "그늘 건조 잎 39.85 mg/g, 동결건조 잎 38.99 mg/g 건조중량(HPLC-UV)[9]; 폴리페놀 분획에서도 확인[17]",
   "잎 주요 페놀 성분의 하나[9]", [9, 17]),
 C("Ellagic acid", "엘라그산(및 유도체)", "페놀산(엘라지탄닌 유래)", "bioactive", "잎",
   "잎 폴리페놀 분획의 우세 성분(함량 초록에 없음)[17]",
   "분획의 α-글루코시다아제 억제 IC50 0.13 mg/mL(시험관)[17]", [17]),
 C("Ergocalciferol", "비타민 D2(에르고칼시페롤)", "비타민", "nutrient", "잎",
   "생잎 0.03 μg/100 g, 건조 잎 0.24 μg/100 g(건조중량, LC-MS/MS)[18]", "양은 적음[18]", [18]),
]

def cond(**kw):
    keys = ["instrument","column","mobile_phase","gradient","flow","temp","detection","injection","sample_prep","standard","linearity","lod","loq","recovery"]
    return {k: kw.get(k, "") for k in keys}
assays = [
 {"role": "literature", "compound": "Citral (geranial + neral)", "compound_ko": "시트랄(게라니알·네랄) 등 정유 21성분", "part": "잎(정유)",
  "content": "게라니알 52.13%, 네랄 37.65%(합계 89.78%), 21성분이 정유의 98.50%(면적 정규화)[4]",
  "method": "GC-FID(정량)·GC-MS(동정)",
  "conditions": cond(instrument="정량: Shimadzu GC-2010 + FID; 동정: Agilent 7890A/5975C GC-MS",
     column="정량: Zebron ZB-5MS(30 m × 0.25 mm × 0.25 μm, Phenomenex); 동정: HP-5MS(30 m × 0.25 mm × 0.25 μm)",
     mobile_phase="운반기체 헬륨(분할비 50:1)", gradient="오븐 60 °C 10분 유지 → 3 °C/분으로 230 °C, 1분 유지",
     flow="FID 1.9 mL/분, GC-MS 1 mL/분", temp="주입구 250 °C(GC-MS), FID 검출기 250 °C",
     detection="FID; MS는 EI 70 eV, m/z 50–550 전체 스캔(이온원 230 °C, 사중극자 150 °C)", injection="0.5 μL(GC-FID)",
     sample_prep="생잎을 3일 그늘 건조·분쇄 후 클레벤저형 장치로 4시간 수증류(잎 2 kg, 물 5 L), 무수 MgSO4로 탈수, 4 °C 차광 보관",
     standard="C8–C20 n-알칸으로 머무름 지수 계산, Adams·NIST 스펙트럼 대조; 보정계수 없는 면적 정규화(3반복)"),
  "rationale": "시트랄이 레몬머틀 정유의 대부분을 차지하고 오스트레일리아·ISO 정유 규격도 성분 백분율로 품질을 정하므로 정유의 지표로 쓰인다[2, 4].",
  "source": [2, 4], "url": "https://doi.org/10.3390/molecules27154895", "source_kind": "paper"},
 {"role": "literature", "compound": "Casuarinin", "compound_ko": "카수아리닌(갈산·미리시트린·하이퍼린·퀘르시트린 함께 정량)", "part": "잎(물 추출물)",
  "content": "카수아리닌 16.1 mg/g, 퀘르시트린 38.8 mg/g, 갈산 2.5 mg/g(추출물 건조중량)[5]",
  "method": "HPLC-PDA(동정은 LC-ESI-QTOF-MS/MS·NMR)",
  "conditions": cond(instrument="Shimadzu Prominence HPLC(PDA); 동정용 Nexera X2 UHPLC + Q-TOF MS(ESI 음이온)",
     column="YMC-Pack ODS-A(250 × 4.6 mm, 5 μm)",
     mobile_phase="A: 아세토니트릴/메탄올(1:1, v/v), B: 20 mM 인산 수용액(LC-MS 때는 0.1% 포름산)",
     gradient="B 95→85%(0–20분), 85→82.2%(20–35분), 82.2→70%(35–55분), 70%(55–75분)",
     flow="0.7 mL/분", temp="40 °C", detection="200–800 nm 스펙트럼, 정량은 260 또는 270 nm", injection="5 μL",
     sample_prep="건조 잎을 5배 부피 물로 50 °C 2시간 2회 추출, 감압 농축 후 동결건조; 추출물 2 mg/mL 물에 녹임",
     standard="갈산·미리시트린·하이퍼린·퀘르시트린 표준품, 카수아리닌은 화학 합성품(메탄올 2–200 μg/mL 검량선)"),
  "rationale": "근육 위성세포를 활성화하는 성분으로 밝혀져 사람 시험에서도 추출물 용량을 카수아리닌 양(하루 2.5 mg)으로 표시했다[5, 7].",
  "source": [5, 7], "url": "https://doi.org/10.3390/nu14051078", "source_kind": "paper"},
 {"role": "literature", "compound": "Gallic acid; Hesperetin", "compound_ko": "갈산·헤스페레틴", "part": "잎(건조 잎)",
  "content": "동결건조 잎 갈산 53.77 mg/g, 헤스페레틴 38.99 mg/g(건조중량)[9]",
  "method": "HPLC-UV(LC-MS로 분자량 재확인)",
  "conditions": cond(instrument="Shimadzu HPLC(CBM-20A), UV-VIS 검출기; 확인용 LCMS-2020",
     column="Phenomenex Luna 역상 칼럼(100 Å, 5 μm, 250 mm × 4.6 mm)",
     mobile_phase="A: 0.2% 포름산 수용액, B: 100% 아세토니트릴",
     gradient="0–5분 A 100%, 5–15분 B 30%, 15–20분 B 70%, 20–25분 B 100%",
     flow="1 mL/분", temp="25 °C", detection="280 nm", injection="20 μL",
     sample_prep="건조 잎 0.25 g + 50% 아세톤 수용액 25 mL, 초음파 150 W 30분(28 ± 2 °C), 0.45 μm 나일론 필터",
     standard="갈산·헤스페레틴 표준품 검량선, 표준품 첨가로 머무름 시간 재확인"),
  "rationale": "건조 방법에 따라 함량이 달라지는 잎의 대표 페놀 성분 두 가지로 골라 건조 품질 지표로 썼다[9].",
  "source": [9], "url": "https://doi.org/10.1016/j.heliyon.2019.e03044", "source_kind": "paper"},
]

world = [
 {"country": "오스트레일리아", "metric": "production_t", "year": 2011, "value": "575–1100", "unit": "t(잎)", "note": "2012년 추정한 2011년 농장 출하 생산량; 같은 자료로 잎 838 t을 적은 2014년 보고도 있음[2]", "source": [2]},
 {"country": "오스트레일리아", "metric": "production_t", "year": 2011, "value": "3–8", "unit": "t(정유)", "note": "정유의 90%를 주로 미국·EU로 수출(추정)[2]", "source": [2]},
]

d = {"slug": "backhousia-citriodora", "name_ko": "레몬머틀", "name_en": "Lemon myrtle",
     "scientific_name": "Backhousia citriodora F. Muell.",
     "aliases": ["레몬머틀잎", "레몬머틀잎추출액", "Lemon myrtle", "Lemon-scented myrtle", "Sweet verbena myrtle", "Lemon ironwood"],
     "sections": sections, "compounds": compounds, "markers": [], "nutrients": [], "assays": assays,
     "production": [], "world": world, "gi": [], "orgs": [], "sources": sources}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in sections: print(s["key"], len(s["body"]))
