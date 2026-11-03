import json
from pathlib import Path

P = Path(__file__).resolve().parent.parent / "dossier.json"
d = json.loads(P.read_text(encoding="utf-8"))
changes = []


def sec(key):
    for s in d["sections"]:
        if s["key"] == key:
            return s
    raise KeyError(key)


def rep(key, old, new, why):
    s = sec(key)
    assert old in s["body"], (key, old)
    s["body"] = s["body"].replace(old, new)
    changes.append({"where": f"sections.{key}", "before": old, "after": new, "why": why})


def comp(name):
    for c in d["compounds"]:
        if c["name"] == name:
            return c
    raise KeyError(name)


# overview
rep("overview",
    "남아시아에서는 맛이 좋고 근육 사이 잔가시가 적어 인기 있는 식용어로 평가되며[5], 파키스탄 남부 펀자브 조사에서는 주민들이 즐겨 먹는 인기 어종으로 꼽혔다[26].",
    "맛이 좋고 근육 사이 잔가시가 적어 인기 있는 어종으로 소개되며[5], 파키스탄 남부 펀자브 민족생물학 조사에서는 상대 인기도 지수(RPL) 1.0의 '인기 어종'에 들었다[26].",
    "[5] 초록은 지역(남아시아)을 말하지 않음. [26] 의 RPL 은 문화적 이용 보고 기준 인기도이지 '즐겨 먹는다'는 뜻이 아님(PMC 본문의 '남부 펀자브에서 인기 있는 식용 대형 메기' 문장은 학명이 빠져 있어 이 종인지 확인 불가)")

# history
rep("history",
    "왈라고메기는 관련 지수(RPL)가 1.0인 인기 어종 15종에 들었다[26].",
    "왈라고메기는 상대 인기도 지수(RPL)가 1.0인 인기 어종 15종에 들었다[26].",
    "RPL 은 relative popularity level(상대 인기도 지수)이며 '관련 지수'는 오역")

# cultivation
rep("cultivation",
    "왈라고메기는 주로 강·저수지에서 자망 등으로 잡는 야생 어종이다[15]. 파키스탄 인더스강 연구에서는 길이 약 1,200 cm의 자망으로 2011년 3–9월 매달 채집하였다[15].",
    "연구용 개체는 주로 하천에서 현지 어민을 통해 채집되었다[4, 15]. 파키스탄 인더스강 연구에서는 길이 약 1,200 cm의 자망으로 2011년 3–9월 매달 채집하였고[15], 사육 산란 연구의 어미는 펀자브 발로키 보 부근 어민의 혼획물에서 얻었다[4].",
    "[15] 는 그 연구의 채집 방법만 말함 — '주로 자망으로 잡는 야생 어종'이라는 일반화는 출처에 없음. [4] 본문(Materials and Methods)의 혼획 채집으로 보완")
rep("cultivation",
    "주사 후 9–10시간 뒤 산란이 시작되었다[4]. 산란 뒤 어미를 빼낸 수조의 부화율(88.12±0.26%)은 어미를 남긴 수조(67.78±1.78%)보다 높아 알 포식이 의심되었다[4].",
    "초록과 고찰은 주사 후 9–10시간의 잠복기를 적었으나, 결과 절에는 주사 3.5시간 뒤 구애가 시작되고 4.5–6시간에 활동이 가장 활발했다고 적혀 있어 원문 안에서 시간이 엇갈린다[4]. 산란 뒤 어미를 빼낸 수조의 부화율(88.12±0.26%)은 어미를 남긴 수조(67.78±1.78%)보다 높아 알 포식이 의심되었다[4]. 다만 수정률은 어미를 남긴 수조가 더 높았으며(82.25±2.44% 대 70.77±2.50%), 초록이 '수정률과 부화율 모두 높았다'고 쓴 것은 본문 결과와 맞지 않는다[4].",
    "[4] PMC 전문 대조 — 잠복기·수정률이 초록과 본문 결과 절에서 다름(원문 내 불일치 명시)")
rep("cultivation",
    "회귀 분석으로 구한 최적 수준은 5.88 g/kg이었다[27].",
    "회귀 분석으로 구한 최적 수준은 5.88 g/kg이었다[27]. 다만 저자들은 결론에서 2–4 g/kg 범위가 가장 좋았다고 적어, 회귀 최적값(5.88 g/kg)과 실측 결과 사이에 차이가 있다[27].",
    "[27] 초록 결론(2–4 g/kg 최적)과 회귀 최적값(5.88 g/kg)이 엇갈리는 점을 함께 적음")

# processing
rep("processing",
    "파키스탄 남부 펀자브에서는 민물고기를 훈제·바비큐·카레·튀김 등으로 먹고 훈제·절임·햇볕 건조로 저장한다고 기록되었으며, 왈라고메기는 이 지역에서 인기 있는 식용 대형 메기로 소개되었다[26].",
    "파키스탄 남부 펀자브에서는 민물고기를 훈제·바비큐·카레·튀김 등으로 먹고 훈제·절임·햇볕 건조로 저장한다고 기록되었다[26]. 이 기록은 조사 어종 전체에 대한 것이며 이 종만의 조리법은 아니다[26].",
    "[26] PMC 본문의 '인기 있는 식용 대형 메기' 문장은 학명이 빠져 있어 이 종을 가리키는지 확인할 수 없음")

# biology: egg diameter unit note ok; keep

# safety
rep("safety",
    "미얀마 에야와디강 조사에서 근육 카드뮴은 0.083 mg/kg이었다[18]. 반면 인더스강 미안왈리 구간 조사에서는 카드뮴·니켈·코발트·아연이 모두 FEPA/WHO 기준 아래였다[15]. 인더스강 타운사 저수지 조사의 위해지수는 1 미만이었으나[19], 차슈마 호수(위해지수 1.20)와 펀자나드 보 조사에서는 섭취 위해 우려가 제기되었다[16, 20].",
    "이 값은 인도 식품 기준(PFA)의 메틸수은 상한 0.25 μg Hg/g(습중량)을 넘는다[17]. 미얀마 에야와디강 조사에서 근육 카드뮴은 0.083 mg/kg(초록에 습·건 기준 표기 없음)이었다[18]. 반면 인더스강 미안왈리 구간 조사에서는 4개 조직의 카드뮴·니켈·코발트·아연이 모두 FEPA/WHO 기준 아래였고(μg/g 습중량)[15], 체나브강 조사에서도 분석 금속이 모두 국제 허용 기준 이내였다[13]. 인더스강 타운사 저수지 조사에서는 이 종의 여름 최고값이 카드뮴 1.50 mg/kg, 크롬 0.56 mg/kg으로 보고되었으나(초록, 조직·습건 기준 표기 없음; 해당 초록 문장이 물 시료 결과와 이어져 있어 매질 구분이 모호함), 카드뮴 위험지수(THQ)는 0.25, 위해지수(HI)는 1 미만이었다[19]. 차슈마 호수 조사에서는 이 종의 위해지수가 1.20으로 위해 우려가 제기되었고[20], 펀자나드 보 5종 조사에서는 이 종의 미량원소 축적이 가장 많았으며 저자들은 두 조사 지점 어류 모두 섭취에 안전하지 않다고 결론지었다[16]. 카불강 조사에서는 조직별 금속 총량이 피부>아가미>장>근육>간 순이었다[22].",
    "[17] PFA 기준 비교 추가, [18] 습·건 기준 표기 없음 명시, [19] 초록의 Cd 1.50 mg/kg 누락 보완과 매질 모호성 표시, [16] 이 종이 최다 축적이라는 초록 내용 반영, [22] 인용 내용 명시")
rep("safety",
    "체나브강 3종 조사의 유기염소계 농약 합계는 5.09–414 ng/g(3종 합산 범위)이었다[21].",
    "체나브강 3종(Labeo boga·Channa marulius·왈라고메기) 조사의 유기염소계 농약 합계는 5.09–414 ng/g(3종 합산 범위, 이 종 개별값 아님; 습·건 기준 초록 표기 없음)이었다[21].",
    "[21] 여러 종 합산 범위임을 종명과 함께 분명히 표시")

# compounds
for n in ["Docosahexaenoic acid", "Palmitic acid", "Oleic acid", "Palmitoleic acid", "Glutamic acid", "Lysine"]:
    c = comp(n)
    old = c["part"]
    c["part"] = "초록에 부위 표기 없음"
    changes.append({"where": f"compounds.{n}.part", "before": old, "after": c["part"], "why": "[12] 초록에 부위 표기가 없어 '살' 단정 삭제"})
for a in d["assays"]:
    if a["compound"] == "Fatty acids and amino acids":
        old = a["part"]; a["part"] = "초록에 부위 표기 없음"
        changes.append({"where": "assays[지방산·아미노산].part", "before": old, "after": a["part"], "why": "[12] 초록에 부위 표기 없음"})
        old = a["content"]
        a["content"] = a["content"].replace("C18:2", "C18:2(초록은 'linolenic acids (C18:2c)'로 이름과 탄소수 표기가 어긋남)")
        changes.append({"where": "assays[지방산·아미노산].content", "before": old, "after": a["content"], "why": "원문 내 불일치(리놀렌산 이름에 C18:2 표기) 명시"})

c = comp("Calcium")
old = c["part"]
c["part"] = "초록에 조직 표기 없음(습·건 체중 기준 모두 분석)"
changes.append({"where": "compounds.Calcium.part", "before": old, "after": c["part"], "why": "[13] 초록은 'wet and dry body weight' 기준만 말하고 몸 전체 분석인지 밝히지 않음"})

c = comp("Cadmium")
old = c["content_text"]
c["content_text"] = "근육 0.083 mg/kg(미얀마 에야와디강, 습·건 기준 초록 표기 없음); 4개 조직 범위 0.004–0.24 μg/g 습중량(인더스강 미안왈리); 여름 최고 1.50 mg/kg(인더스강 타운사 저수지, 조직·습건 기준 초록 표기 없음)"
changes.append({"where": "compounds.Cadmium.content_text", "before": old, "after": c["content_text"], "why": "[18] 기준 미표기 명시, [19] 초록의 Cd 1.50 mg/kg 추가"})
old = c["activity_ko"]
c["activity_ko"] = "미얀마 근육값은 EU 기준(0.1 ppm)보다 낮고 FAO/WHO 기준(0.05 ppm)보다 높았으며, 인더스강 미안왈리 값은 FEPA/WHO 기준 아래였고, 타운사 저수지에서는 카드뮴이 가장 우려되는 금속(THQ 0.25)으로 꼽혔다[15, 18, 19]"
c["source"] = [15, 18, 19]
changes.append({"where": "compounds.Cadmium.activity_ko", "before": old, "after": c["activity_ko"], "why": "[19] 반영"})

c = comp("Chromium")
old = c["content_text"]
c["content_text"] = "여름 최고 0.56 mg/kg(인더스강 타운사 저수지, 습·건 기준 초록 표기 없음)"
changes.append({"where": "compounds.Chromium.content_text", "before": old, "after": c["content_text"], "why": "[19] 기준 미표기 명시"})
old = c["activity_ko"]
c["activity_ko"] = "초록은 크롬·카드뮴이 허용 기준을 자주 넘었다고 적었으나 그 문장이 물 시료 결과와 이어져 있어 어류에 대한 판단인지 모호하다[19]"
changes.append({"where": "compounds.Chromium.activity_ko", "before": old, "after": c["activity_ko"], "why": "[19] 초록 문장 매질 모호성 명시"})

c = comp("Methylmercury")
old = c["activity_ko"]
c["activity_ko"] = "조사한 19종 가운데 유기수은이 가장 높았고 인도 PFA 상한(0.25 μg Hg/g 습중량)을 넘었다[17]"
changes.append({"where": "compounds.Methylmercury.activity_ko", "before": old, "after": c["activity_ko"], "why": "[17] 초록의 PFA 기준 비교 반영"})

c = comp("Dieldrin")
old = c["content_text"]
c["content_text"] = "이 종 개별값 확인하지 못함 — 3종(Labeo boga·Channa marulius·왈라고메기) ΣOCPs 범위 5.09–414 ng/g(3종 합산 범위, 이 종 값 아님; 습·건 기준 초록 표기 없음)"
changes.append({"where": "compounds.Dieldrin.content_text", "before": old, "after": c["content_text"], "why": "합산 대상 종 명시"})

# assay [15]
for a in d["assays"]:
    if a["source"] == [15]:
        old = a["content"]
        a["content"] = old.replace("본문 결과 절에는 Co 하한이 0.001로 적혀 있음)[15]",
                                   "본문 결과 절에는 Co 하한이 0.001로 적혀 있음; Cd 최고값도 결과 절은 피부 0.24, 고찰 절은 아가미 0.11로 다르고, 금속 축적 순서도 초록(Ni<Zn<Co<Cd)과 본문(Ni>Zn>Cd>Co)이 서로 다르며 둘 다 측정값 크기와 맞지 않음)[15]")
        assert old != a["content"]
        changes.append({"where": "assays[15].content", "before": old, "after": a["content"], "why": "PMC 전문 대조 — 원문 내 불일치 명시"})
        cd = a["conditions"]
        old = cd["sample_prep"]
        cd["sample_prep"] = old.replace("근육·피부·아가미·간 약 15 g 채취 후 -20℃ 보관", "근육·아가미·간 약 15 g 채취 후 -20℃ 보관(원문 이 문장에 피부는 빠져 있으나 분석은 4개 조직)")
        assert old != cd["sample_prep"]
        changes.append({"where": "assays[15].conditions.sample_prep", "before": old, "after": cd["sample_prep"], "why": "원문은 'muscle, gills and liver' 약 15 g"})

P.write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
Path(__file__).with_name("changes.json").write_text(json.dumps(changes, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(changes))
