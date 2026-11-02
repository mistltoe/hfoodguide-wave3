import json
from pathlib import Path

W = Path(__file__).resolve().parent
C = json.load(open(W / "cites.json", encoding="utf-8"))
C["2332172"] = dict(title="A satellite DNA family from pollock (Pollachius virens).", j="Gene", y="1990", v="87", i="2", pg="279-83", doi="10.1016/0378-1119(90)90313-g")
C["29030860"] = dict(title="The Effects of Short-Time Temperature Abuse on the Microbial and Sensory Quality of Chilled Saithe (Pollachius virens) Fillets.", j="J Food Sci", y="2017", v="82", i="11", pg="2690-2699", doi="10.1111/1750-3841.13926")

ACC = "2026-11-02"
src = [
    dict(title="식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — Pollachius virens 행(검정대구, 영문 Saithe, 식품원료(A코드)·수산물, 부위 '-', 사용가능, 사용조건 없음; 로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json·docs/materials/pollachius-virens/card.json)",
         url="https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", publisher="식품의약품안전처", accessed="2026-10-13"),
    dict(title="FishBase — Pollachius virens (Linnaeus, 1758), Saithe: species summary (검색 결과 요약으로만 확인, 본문 페이지는 이 환경에서 열지 못함)",
         url="https://www.fishbase.se/summary/Pollachius-virens.html", publisher="FishBase", accessed=ACC),
]
PM = ["27734466", "38924061", "42548823", "26537479", "36321524", "25557424", "21484258", "2332172", "28407939", "18454544",
      "23870888", "28721399", "23729850", "23572803", "32283110", "36547886", "38998639", "37342572", "35406991", "19416649",
      "19845349", "24629963", "29030860", "9569092", "10321017", "39600398", "24782899", "22734881", "21589984", "38101477",
      "41120798", "31156581", "32056619"]
N = {}
for p in PM:
    c = C[p]
    cit = f"{c['j']} {c['y']}"
    if c.get("v"):
        cit += f";{c['v']}"
        if c.get("i"):
            cit += f"({c['i']})"
    if c.get("pg"):
        cit += f":{c['pg']}"
    t = c["title"].replace("()", "(Pollachius virens)").replace(" (.)", "")
    src.append(dict(title=f"{t} {cit}. doi:{c['doi']}", url=f"https://pubmed.ncbi.nlm.nih.gov/{p}/",
                    publisher=f"{c['j']} (PubMed)", accessed=ACC))
for i, s in enumerate(src, 1):
    s["n"] = i
# 번호표
R = {p: i + 3 for i, p in enumerate(PM)}  # 1=MFDS, 2=FishBase, 3.. = PM
def r(*ps):
    return ", ".join(str(R[p]) if p in R else str(p) for p in ps)

oocyte, juv, yoy, raest, anis, popgen, mito, sat, hrm, pani, barc, meal, fpi, snack, gel, gelem, silh, visc, liver, fphrat, aoc, frozen, abuse, anis98, belg, efsa, pfas, popsl, hg, popst, pah, crypto, mp = PM

sections = [
 dict(key="overview", title="한눈에 보기", body=(
  f"검정대구(Pollachius virens)는 대구과(Gadidae) 북방대구속(Pollachius)의 바닷물고기로, 영어로는 saithe라 부르고 coalfish, pollock이라는 이름으로도 문헌에 나온다[1, {r(liver, pfas)}]. "
  f"북대서양에 살며[2], 북동북극 자원의 검정대구는 대구·해덕과 함께 유럽에서 가장 중요한 수산 자원으로 꼽힌다[{r(anis)}].\n\n"
  f"식약처 「식품원료 목록」에는 원료명 '검정대구'(영문 Saithe)가 식품원료(A코드) 수산물로 올라 있고 상태는 '사용가능'이다[1]. "
  f"부위 칸은 '-'이고 따로 정한 사용 조건은 없으며, 건강기능식품 고시형 원료의 원재료 목록에도 없어 고시 지표성분이나 1일 섭취량 기준은 없다[1]. "
  f"같은 목록에는 같은 속의 다른 종이 'Pollack'이라는 별도 원료로 올라 있으므로 이름을 혼동하지 않아야 한다[1].\n\n"
  f"살은 냉장·냉동 필레로 유통되고[{r(abuse, frozen)}], 부산물(내장·간·껍질)은 어분, 단백질 가수분해물, 젤라틴, 오메가-3 기름 원료로 연구되고 있다[{r(meal, silh, gel, visc)}]. "
  f"국내 유통·수입 현황은 이번 조사에서 확인하지 못함.")),
 dict(key="history", title="이름과 이용의 역사", body=(
  f"페로제도에서는 대구나 검정대구를 바람에 말리면서 발효시킨 '레스투르 피스쿠르(ræstur fiskur)'를 대대로 집에서 만들어 왔다[{r(raest)}]. "
  f"날씨와 계절에 따라 먹을거리가 크게 흔들리는 섬 경제에서 오래 저장할 수 있는 이 마른 생선은 식량 안보의 중심이었다[{r(raest)}]. "
  f"양의 기름(獸脂)과 함께 먹으며 예전에는 성탄 전야와 섣달그믐에 먹는 음식이었고, 지금도 일상 음식이자 민족 정체성의 상징으로 남아 있다[{r(raest)}].\n\n"
  f"노르웨이 원양 트롤선은 2021년 선상에서 생긴 흰살생선 부산물의 약 70%(7만 7천 톤)를 바다에 버렸으며, 이런 부산물에는 검정대구·대서양대구·해덕의 머리·내장·간이 포함된다[{r(visc)}]. "
  f"이 때문에 최근에는 선상 사일리지(산 저장)로 내장을 보존해 단백질 가수분해물과 기름을 얻는 연구가 이어지고 있다[{r(silh, visc)}]. "
  f"아이슬란드에서는 검정대구 수리미로 만든 생선 단백질 가루 7%를 넣은 옥수수 스낵을 개발해 이란·아이슬란드 어린이의 선호도를 조사하기도 했다[{r(snack)}]. "
  f"국내 도입·이용의 역사 기록은 이번 조사에서 확인하지 못함.")),
 dict(key="biology", title="어종과 생태", body=(
  f"FishBase 요약에 따르면 최대 전장 130 cm, 흔한 크기 60 cm, 최대 체중 32 kg, 최대 연령 25년이며 수심 37–364 m의 북대서양 양안(동쪽은 바렌츠해·스피츠베르겐에서 비스케이만까지, 아이슬란드 주변 포함)에 산다[2]. "
  f"이 값들은 검색 결과 요약으로만 확인한 것이다[2].\n\n"
  f"북해 검정대구의 난황 형성은 10월 말–11월 초에 시작되어 2월에 산란이 시작되며, 실험실 관찰에서 산란은 2월 13일부터 3월 29일까지 이어졌다[{r(oocyte)}]. "
  f"수화된 알의 지름은 1.04–1.31 mm(평균 1.18 mm), 전장 중앙값 60 cm 암컷의 추정 실현 산란수는 약 84만 개였다[{r(oocyte)}]. "
  f"어린 검정대구는 여름에 육지 가까운 얕은 물에 머물다 수온이 높을 때 피오르 밖으로 흩어졌다[{r(juv)}]. "
  f"0세어 실험에서 검정대구는 대서양대구보다 탐색이 빠르고 가속도가 컸으며, 이는 저서성인 대구와 달리 무리를 강하게 짓는 부어성(pelagic) 생활과 맞아떨어진다고 해석되었다[{r(yoy)}]. "
  f"바렌츠해 남부에서는 겨울·봄에 열빙어 등을 먹으러 연안으로 다가온다[{r(anis)}].")),
 dict(key="related_species", title="가까운 종", body=(
  f"검정대구는 대서양대구·태평양대구·명태·청대구·해덕 등과 같은 대구과에 속해, 살을 가공하면 겉모습으로 종을 구별하기 어렵다[{r(hrm, pani)}]. "
  f"미토콘드리아 cytb 미니바코드와 고해상도 융해곡선(HRM)을 결합한 방법은 대서양대구·태평양대구·명태·검정대구를 99.3%의 신뢰도로 구별했고, 생선 함유 식품 30개 중 30%가 표시와 달랐다[{r(hrm)}]. "
  f"판토피신 I(PanI) 유전자를 표적으로 한 종 특이 PCR도 검정대구를 명태·청대구·메를루사류·대서양대구·whiting(Merlangius merlangus)과 구별해 검출하도록 개발되었다[{r(pani)}].\n\n"
  f"이탈리아에서는 법령상 대서양대구·태평양대구로만 만들어야 하는 '바칼라' 튀김 조각 제품(bocconcini di baccalà) 40개 가운데 28개가 검정대구로 판명되어 대체 유통 사례로 보고되었다[{r(barc)}]. "
  f"같은 속의 다른 종(영명 pollack)과는 영명이 비슷해 혼동되기 쉬우며, 식약처 목록에서도 두 종은 서로 다른 원료로 올라 있다[1]. "
  f"국내 시장의 대체·혼입 실태는 이번 조사에서 확인하지 못함.")),
 dict(key="cultivation", title="어획과 자원", body=(
  f"검정대구의 상업 어획은 자연산을 잡는 방식이며, 바렌츠해 연구 시료도 덴마크식 후릿그물과 연승으로 잡은 것이었다[{r(anis)}]. "
  f"2021년 노르웨이에 양륙된 북동북극(NEA) 자원은 대구 약 37만 5천 톤, 검정대구 약 19만 톤, 해덕 약 10만 톤이었고, 세 어종의 어획 가치는 다른 상업 어종 전체를 합친 것보다 컸다[{r(anis)}]. "
  f"잡힌 고기는 대부분 유럽 여러 시장으로 수출된다[{r(anis)}].\n\n"
  f"노르웨이 연안에서는 연어 가두리 양식장 주변에서 잡힌 야생 검정대구와 대구를 대상으로, 양식장이 수은 등 원소나 유기오염물질의 공급원이 되는지가 연구되었다[{r(hg)}]. "
  f"조사 결과 양식장 주변 검정대구 간의 수은은 대조군보다 약 80% 높게 추정되었으나, 저자들은 양식장이 일반적으로 야생어의 유해 원소를 늘린다는 근거는 아니라고 결론지었다[{r(hg)}]. "
  f"북해 자원의 연도별 총허용어획량(TAC)과 ICES 권고량, 세계 어획 통계(FAO)는 이 환경에서 원문을 열지 못해 확인하지 못함. "
  f"FishBase 요약상 분포가 북대서양이어서 한국 연근해 어획 대상은 아니며[2], 국내 수입량 통계는 확인하지 못함.")),
 dict(key="processing", title="가공과 이용", body=(
  f"검정대구 필레는 냉장 상태에서 유통기한이 짧아, 가공 중 16 °C에 1시간·2시간 두었다가 포장하면 바로 포장한 것보다 저장 수명이 각각 22%(2일), 44%(4일) 줄었다[{r(abuse)}]. "
  f"−20 °C와 −30 °C에서 최대 18개월 냉동 저장한 실험에서는 저장이 길수록 지질이 분해되었고 낮은 온도가 더 잘 보존했으며, 검정대구 적색육에는 고도불포화지방산이 많았다[{r(frozen)}].\n\n"
  f"pH 이동 공정으로 분리해 동결건조한 단백질 가루는 단백질 71–93%, 지방 0.5–2%였으나 공정 중 산화가 진행되어 기능성과 관능이 떨어졌다[{r(fpi)}]. "
  f"노르웨이 트롤선에서 대구·검정대구 부산물로 만든 어분은 평균 단백질 61.9%, 지방 8.9%였고, 효소 분해물에서 ACE 저해 펩타이드가 확인되었다[{r(meal)}]. "
  f"내장 사일리지는 원료를 1일 이내에 처리해야 가수분해물 품질이 유지되었고[{r(silh)}], 간을 포함한 내장 기름은 원료를 1–3일 보관하면 DHA와 오메가-3 함량이 유의하게 줄었다[{r(visc)}]. "
  f"껍질 젤라틴은 무기질이 20% 넘게 들어 있어 시판 젤라틴(0.2% 미만)과 달랐고 거품 성질이 더 좋았다[{r(gel)}]. "
  f"쥐에게 검정대구 단백질 가수분해물을 26일 먹인 실험에서는 공복 혈장 담즙산이 오르고 내장지방 양이 줄었지만, 사람 대상 근거는 확인하지 못함[{r(fphrat)}]. "
  f"국내 제품 생산실적은 확인하지 못함.")),
 dict(key="genetics", title="유전체와 유전 다양성", body=(
  f"대구과 10종의 미토콘드리아 유전체를 분석한 연구에서 검정대구의 미토콘드리아 유전체 전체 염기서열이 처음 보고되었다[{r(mito)}]. "
  f"같은 연구는 검정대구와 대서양대구에서 폴리(A)가 붙은 미토콘드리아 전사체 10종을 확인했고, 정지 코돈 6개가 전사 뒤 폴리아데닐화로 만들어진다고 밝혔다[{r(mito)}].\n\n"
  f"핵 DNA에서는 EcoRI로 잘리는 약 200 bp(±5)의 위성 DNA 반복 서열이 핵 DNA의 13%를 차지하고, 반수체 유전체당 약 50만 개(5×10^5) 복사본이 있다고 보고되었다[{r(sat)}]. "
  f"집단유전학 연구는 RAPD-PCR과 근연종 미세위성(microsatellite) 표지를 시험했으며, 북동대서양 안에 여러 무리로 나뉜 집단 구조가 있고 북해 북부에서 겹칠 가능성을 제시했다[{r(popgen)}]. "
  f"저자들은 이를 원산지 표시를 실험으로 검증하는 데 쓸 수 있다고 보았다[{r(popgen)}]. "
  f"종 판별에는 cytb·COI 미토콘드리아 바코드와 PanI 핵 유전자가 쓰인다[{r(hrm, pani, barc)}]. "
  f"염색체 수준의 전장 유전체 조립 보고는 이번 조사에서 확인하지 못함.")),
 dict(key="safety", title="안전성과 주의", body=(
  f"고시형 원료가 아니어서 식약처가 따로 정한 섭취 주의사항은 없다[1]. "
  f"EFSA는 2024년 의견에서 검정대구를 EU/EFTA에서 많이 먹는 자연산 어종의 하나로 꼽고, 모든 자연산 어류가 인체감염 기생충에 노출될 수 있다고 결론지었다[{r(efsa)}]. "
  f"바렌츠해 남부 검정대구 59마리에서는 고래회충류(Anisakis simplex s.s.)가 내장과 살 모두에서 100% 검출되었고, 살에 평균 18마리 넘게 있었으며 약 34%는 살에 20마리 이상을 지녔다[{r(anis)}]. "
  f"살 속 유충의 85% 넘게가 뱃살 부위에 몰려 있어, 뱃살을 잘라내면 검정대구 필레의 유충을 최대 86% 줄일 수 있다고 제안되었다[{r(anis)}]. "
  f"노르웨이 연안 검정대구에서는 고래회충 유충의 99.6%가 내장에서 발견되었다[{r(anis98)}]. "
  f"벨기에 시판 필레 조사에서 검정대구의 감염률은 26.7%였다[{r(belg)}]. "
  f"프랑스 주변 해역 어류 조사에서는 검정대구가 크립토스포리디움(Cryptosporidium) 양성이 가장 많이 나온 어종이었다[{r(crypto)}].\n\n"
  f"아이슬란드 어류 살 조사에서 과불화화합물은 검정대구에서만 PFOS 0.05 ng/g(습중량)이 검출되었다[{r(pfas)}]. "
  f"노르웨이 연안 어류의 간 조사에서 대구는 검정대구보다 유기오염물질이 2–3배, 수은이 6.8배 높았다[{r(popsl, hg)}]. "
  f"북해 검정대구 간의 PCB·DDT·HCH·PBDE는 2005–2019년 유의하게 줄었다[{r(popst)}]. "
  f"아이슬란드 검정대구 46마리 중 17.4%의 소화관에서 미세플라스틱이 나왔다[{r(mp)}]. "
  f"국내 공공기관의 검정대구 알레르기·잔류 정보는 확인하지 못함.")),
]

compounds = [
 dict(name="Eicosapentaenoic acid", name_ko="EPA(에이코사펜타엔산)", **{"class": "오메가-3 고도불포화지방산"}, role="nutrient", part="간",
      content_text=f"북해산 간 지방산의 4.4–9.0%(2016–2018년 계절별)[{r(liver)}]",
      activity_ko=f"간유 권장 범위(7–16%)보다 낮아지는 달이 있어 연중 표준화가 어렵다고 평가[{r(liver)}]", source=[R[liver]]),
 dict(name="Docosahexaenoic acid", name_ko="DHA(도코사헥사엔산)", **{"class": "오메가-3 고도불포화지방산"}, role="nutrient", part="간·내장",
      content_text=f"간 지방산의 10.5%(2016년 7월)–13.3%(2017년 3월)[{r(liver)}]; 간 포함 내장 기름의 가장 많은 지방산[{r(visc)}]",
      activity_ko=f"원료 보관 1–3일 뒤 사일리지 기름에서 유의하게 감소[{r(visc)}]", source=[R[liver], R[visc]]),
 dict(name="Omega-3 fatty acids", name_ko="오메가-3 지방산(합계)", **{"class": "고도불포화지방산"}, role="nutrient", part="내장",
      content_text=f"간 포함 내장 30.8 ± 0.1%, 간 뺀 내장 36.3 ± 0.1%(총 지방산 중)[{r(visc)}]",
      activity_ko=f"내장 두 분획 모두 오메가-3 기름 원료가 될 수 있다고 평가[{r(visc)}]", source=[R[visc]]),
 dict(name="Oleic acid", name_ko="올레산(C18:1 n-9)", **{"class": "단일불포화지방산"}, role="nutrient", part="간",
      content_text=f"간 지방산의 12.6%(2016년 11월 시료)[{r(liver)}]",
      activity_ko=f"간에서 가장 많은 지방산[{r(liver)}]", source=[R[liver]]),
 dict(name="Gondoic acid", name_ko="곤도산(C20:1)", **{"class": "단일불포화지방산"}, role="nutrient", part="간",
      content_text=f"C20:1 n-9 + n-11 합계 12.0%(2016년 11월 시료, 비교 5종 중 최고)[{r(liver)}]",
      activity_ko=f"간 지방의 주요 단일불포화지방산 묶음[{r(liver)}]", source=[R[liver]]),
 dict(name="Fish protein isolate", name_ko="생선 단백질 분리물", **{"class": "단백질"}, role="nutrient", part="살(다진 살)",
      content_text=f"동결건조 분말 단백질 71–93%, 수분 1.5–3%, 지방 0.5–2%[{r(fpi)}]",
      activity_ko=f"pH 이동·동결건조 중 산화로 보수력·겔 형성 등 기능성 저하[{r(fpi)}]", source=[R[fpi]]),
 dict(name="Taurine", name_ko="타우린", **{"class": "아미노산 유도체"}, role="bioactive", part="살 단백질 가수분해물",
      content_text=f"가수분해물에 많다고 보고(수치는 초록에 없음)[{r(fphrat)}]",
      activity_ko=f"쥐에서 공복 혈장 담즙산 상승·내장지방 감소와 관련 추정[{r(fphrat)}]", source=[R[fphrat]]),
 dict(name="Glycine", name_ko="글리신", **{"class": "아미노산"}, role="nutrient", part="살 단백질 가수분해물",
      content_text=f"가수분해물에 많다고 보고(수치는 초록에 없음)[{r(fphrat)}]",
      activity_ko=f"담즙산 포합에 쓰이는 아미노산으로, 가수분해물 효과의 기전 후보[{r(fphrat)}]", source=[R[fphrat]]),
 dict(name="Glutamic acid", name_ko="유리 글루탐산", **{"class": "아미노산"}, role="nutrient", part="내장 사일리지 가수분해물",
      content_text=f"원료 보관이 길수록 유리 글루탐산 증가(수치는 초록에 없음)[{r(silh)}]",
      activity_ko=f"원료 신선도를 반영하는 유리아미노산 변화의 하나[{r(silh)}]", source=[R[silh]]),
 dict(name="Lysine", name_ko="유리 라이신", **{"class": "필수아미노산"}, role="nutrient", part="내장 사일리지 가수분해물",
      content_text=f"원료 보관이 길수록 증가, 유리 글루타민은 감소(수치는 초록에 없음)[{r(silh)}]",
      activity_ko=f"신선도 지표성 변화[{r(silh)}]", source=[R[silh]]),
 dict(name="Gelatin", name_ko="젤라틴", **{"class": "단백질(콜라겐 유래)"}, role="bioactive", part="껍질",
      content_text=f"무기질 20% 초과(시판 해양 젤라틴 0.2% 미만)[{r(gel)}]; 유화 기름방울 약 500 nm, 제타전위 약 +25 mV[{r(gelem)}]",
      activity_ko=f"거품 성질 우수, 수중유 유화물의 산화 안정성 개선 가능성[{r(gel, gelem)}]", source=[R[gel], R[gelem]]),
 dict(name="Antioxidant peptides", name_ko="항산화 펩타이드(근육 유래)", **{"class": "펩타이드"}, role="bioactive", part="살",
      content_text=f"모의 소화 뒤 ORAC 가을 검정대구 근육 130–165 μmol/g 범위(새우 포함), 겨울 검정대구 110 μmol/g[{r(aoc)}]",
      activity_ko=f"소화 중 항산화능이 늘어 EPA·DHA 보호 가능성 제시(시험관)[{r(aoc)}]", source=[R[aoc]]),
]

assays = [
 dict(role="literature", compound="Eicosapentaenoic acid / Docosahexaenoic acid", compound_ko="EPA·DHA(지방산 조성)",
      part="간(북해산, 2016–2018년)",
      content=f"검정대구 간 EPA 4.4–9.0%, DHA 10.5–13.3%(총 지방산 중), 간 지질 48.9–75.9%[{r(liver)}]",
      method="GC(지방산 메틸에스터, FAME)",
      conditions=dict(instrument="HP5890 A 가스크로마토그래프(Agilent Technologies)", column="Agilent DB-Wax 127-7012 (10 m × 100 μm × 0.1 μm)",
                      mobile_phase="", gradient="", flow="", temp="", detection="", injection="",
                      sample_prep="Bligh & Dyer 추출물(지질 20–50 mg 상당) 질소 건조 → 내부표준(C23:0) 100 μL + BHT 함유 헵탄 200 μL + 톨루엔 100 μL → 마이크로파 메틸화 100 °C 5분(500 W) → BHT 헵탄 0.7 mL·포화식염수 1 mL 첨가 후 상층 분석 (AOCS Ce 1b-89, Ce 1i-07 변법)",
                      standard="FAME 표준혼합물(Nu-Check Prep GLC 714)로 동정; 총 지방산 면적%로 정량",
                      linearity="", lod="", loq="", recovery=""),
      rationale=f"EPA·DHA는 간유를 식용 오메가-3 기름 원료로 평가하는 기준 성분이다[{r(liver)}]. 전문(Methods) 확인 — 검출기·오븐 온도·주입 조건은 본문에 없음[{r(liver)}].",
      source=[R[liver]], url=f"https://pubmed.ncbi.nlm.nih.gov/{liver}/", source_kind="paper"),
 dict(role="literature", compound="Omega-3 fatty acids / Docosahexaenoic acid (1H NMR)", compound_ko="오메가-3 지방산·DHA(NMR)",
      part="내장(간 포함·제외) 사일리지 기름",
      content=f"총 오메가-3: 간 포함 내장 30.8 ± 0.1%, 간 뺀 내장 36.3 ± 0.1%; 사일리지 슬러지 27.2 ± 0.8%(0일)→23.2 ± 1.4%(3일)[{r(visc)}]",
      method="GC(지방산 조성) / 고분해능 1H·13C NMR(지질 종류·오메가-3·DHA 몰%)",
      conditions=dict(instrument="Bruker Avance 600 MHz NMR(크라이오프로브), 1H 600.23 MHz·13C 150.94 MHz, 25 °C",
                      column="", mobile_phase="", gradient="", flow="", temp="상온(25 °C)",
                      detection="1H: zg 30, 스캔 24회, 획득 3.0 s, 이완 지연 2 s, 스펙트럼 폭 18.03 ppm; 13C: zgig, 스캔 512회, 획득 1.83 s, 이완 지연 2 s, 폭 236 ppm",
                      injection="", sample_prep="기름 120 mg을 1% TMS 함유 중수소화 클로로폼 0.6 mL에 녹여 5 mm NMR 관에 넣음; GC 조성은 Dauksas 등 방법(인용 문헌)",
                      standard="", linearity="", lod="", loq="", recovery=""),
      rationale=f"내장 기름의 오메가-3·DHA 감소는 원료 신선도와 산화를 보여 주는 품질 지표로 쓰였다[{r(visc)}]. 전문(Methods) 확인 — GC 칼럼·조건은 인용 문헌에만 있어 확인하지 못함[{r(visc)}].",
      source=[R[visc]], url=f"https://pubmed.ncbi.nlm.nih.gov/{visc}/", source_kind="paper"),
 dict(role="literature", compound="Perfluorooctane sulfonate (PFOS)", compound_ko="과불화옥탄술폰산(PFOS)",
      part="살(껍질 없는 필레, 10마리 이상 혼합, 아이슬란드 북서부산)",
      content=f"검정대구 살 PFOS 0.05 ng/g 습중량; 그 밖의 과불화화합물 10종은 검출한계 미만[{r(pfas)}]",
      method="LC-MS/MS",
      conditions=dict(instrument="액체크로마토그래프-탠덤질량분석기(ISO/IEC 17025 인정 외부 시험기관)", column="", mobile_phase="", gradient="", flow="", temp="",
                      detection="", injection="",
                      sample_prep="균질화 시료에 13C 표지 대체표준(PFBA·PFHxA·PFOA·PFNA·PFDA·PFUnA·PFOS) 첨가 → 메탄올 추출 → SPE(STRATA-X-AQ) 정제 → 분석 직전 회수표준(13C-PFOA) 첨가",
                      standard="13C 동위원소 표지 대체표준", linearity="", lod="대구 살 PFOS 검출한계 0.15 ng/g 습중량(검정대구 시료별 LOD는 본문 표에 있어 확인하지 못함)", loq="", recovery=""),
      rationale=f"PFOS는 생선 섭취로 노출되는 대표 과불화화합물이라 식용 부위 안전성 감시 항목이다[{r(pfas)}]. 전문(Methods) 확인 — 칼럼·이동상·질량 조건은 본문에 없음[{r(pfas)}].",
      source=[R[pfas]], url=f"https://pubmed.ncbi.nlm.nih.gov/{pfas}/", source_kind="paper"),
 dict(role="literature", compound="Phenanthrene / Acenaphthylene (PAHs)", compound_ko="페난트렌·아세나프틸렌(다환방향족탄화수소)",
      part="간(페로제도 연안, 2022년 6월)",
      content=f"검정대구 간에서 페난트렌이 조사 어종 중 가장 높았고 아세나프틸렌·플루오렌 비중이 높았음(개별 수치는 그림·보충자료에 있어 확인하지 못함); 방법 검출한계 0.3–3.3 ng/g 습중량[{r(pah)}]",
      method="QuEChERS 변법 + GC-MS(EI, SIM)",
      conditions=dict(instrument="Agilent 6890N-5975B GC-MS, 전자이온화 70 eV", column="ZB-5 모세관 칼럼 30 m (0.25 mm, 0.25 μm)",
                      mobile_phase="운반기체 헬륨", gradient="오븐 50 °C 2분 → 25 °C/분으로 315 °C → 8분 유지(총 30분)", flow="1.1 mL/min",
                      temp="", detection="SIM, m/z 128–288 13개 이온, 12개 시간 구간, 이온별 dwell 20 ms", injection="1 μL 비분할(splitless)",
                      sample_prep="간 2 g + 물 2 mL + 아세토니트릴 4 mL → 5분 교반 → MgSO4 1.6 g·NaCl 0.4 g·구연산염 완충염 첨가, 원심 2000 rpm 10분 → 상등액 2 mL에 MgSO4 260 mg·PSA 345 mg·d-C18 45 mg(dSPE) → 상등액 1 mL에 내부표준 60 μL → 50 °C 질소 농축 → 아세토니트릴 100 μL 재용해",
                      standard="16종 PAH 3–180 ng/mL 내부표준 검량; 중수소 표지 내부표준 6종·회수표준 9종", linearity="3–180 ng/mL 검량 범위", lod="0.3–3.3 ng/g 습중량", loq="", recovery="회수표준으로 100% 미만 회수를 보정"),
      rationale=f"검정대구는 물에 잘 녹는 저분자 PAH를 아가미로 흡수하는 경향이 있어 간 PAH 조성이 저서 어종과 달랐다[{r(pah)}]. 전문(Methods) 확인 — 시료 수가 적어 해석에 주의가 필요하다고 저자들이 밝힘[{r(pah)}].",
      source=[R[pah]], url=f"https://pubmed.ncbi.nlm.nih.gov/{pah}/", source_kind="paper"),
]

world = [
 dict(country="노르웨이(북동북극 자원 양륙)", metric="production_t", year=2021, value=190000, unit="t",
      note=f"논문 서론에 인용된 노르웨이 수산청 자료의 근삿값(약 19만 톤)[{r(anis)}]", source=[R[anis]]),
]

d = dict(slug="pollachius-virens", name_ko="검정대구", name_en="Saithe", scientific_name="Pollachius virens (Linnaeus, 1758)",
         aliases=["검정대구", "Saithe", "Coalfish", "Pollock", "Atlantic pollock"],
         sections=sections, compounds=compounds, markers=[], assays=assays, nutrients=[], production=[], world=world,
         gi=[], orgs=[], sources=src)
(W.parent / "dossier.json").write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in sections:
    print(s["key"], len(s["body"]))
print("sources", len(src))
