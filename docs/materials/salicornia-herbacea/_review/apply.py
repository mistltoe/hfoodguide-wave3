import json, sys
p = sys.argv[1]
d = json.load(open(p, encoding="utf-8"))
sec = {s["key"]: s for s in d["sections"]}
changes = []
def rep(where, obj, key, old, new, why):
    s = obj[key]
    assert old in s, (where, old)
    obj[key] = s.replace(old, new, 1)
    changes.append({"where": where, "before": old, "after": new, "why": why})

# overview
rep("sections.overview", sec["overview"], "body",
    "맛이 짜서 바닷가 주민들이 양념 채소로 먹어 왔고[35]",
    "맛이 짜서[7] 바닷가 주민들이 양념 채소로 먹어 왔고[35]",
    "[35]는 해안 주민의 양념 채소 이용만 적고 짠맛은 말하지 않음 — 짠맛은 [7]이 근거")
rep("sections.overview", sec["overview"], "body",
    "이 문서는 한국에서 채취·재배한 '함초' 연구를 학명 표기와 함께 인용했고, 같은 속의 S. bigelovii 등 다른 식품원료 자료는 섞지 않았다[1, 2].",
    "이 문서는 주로 한국에서 채취·재배한 '함초' 연구를 논문의 학명 표기와 함께 인용했고, 중국 시료 연구(S. herbacea 또는 S. europaea로 표기)는 그 사실을 함께 적었으며, 같은 속의 S. bigelovii 등 다른 식품원료 자료는 섞지 않았다[1, 2].",
    "[15][16][20][22][31] 등 중국 시료 연구도 인용하고 있어 '한국 시료만'이라는 서술은 사실과 다름([2]가 [15]는 신장, [16]은 장쑤성 시료라고 밝힘)")

# history
rep("sections.history", sec["history"], "body",
    "2005년 부산 해안 시료에서 새 클로로겐산 유도체가 분리되어 퉁퉁마디의 한국 이름을 딴 '퉁퉁마딕산(tungtungmadic acid)'으로 이름 붙었다[2].",
    "2005년 부산 해안 시료에서 새 클로로겐산 유도체 '퉁퉁마딕산(tungtungmadic acid, 3-카페오일-4-디하이드로카페오일퀸산)'이 분리되었다[2].",
    "[2]는 이름의 유래(한국 이름을 땄다는 점)를 말하지 않음 — 확인된 사실만 남김")

# biology
rep("sections.biology", sec["biology"], "body",
    "같은 계열로 묶이는 S. europaea는 염화나트륨 1000 mM 이상을 견디는",
    "중국 연구진이 S. europaea로 실험한 결과, 이 식물은 염화나트륨 1000 mM 이상을 견디는",
    "[22]는 중국과학원 식물연구소 연구로, 한국 함초 시료가 아님을 밝힘")
rep("sections.biology", sec["biology"], "body",
    "종자 껍질(종피)에서 다당류를 추출해 구성 당과 항산화 활성을 조사한 연구도 있다[31].",
    "중국 연구진이 종자 껍질(종피)에서 다당류를 추출해 구성 당과 항산화 활성을 조사한 연구도 있으나, 종자는 식품원료 목록의 사용 가능 부위(줄기·잎)가 아니다[1, 31].",
    "[31]은 중국(진저우) 연구이고, card.json 사용 조건은 줄기·잎뿐이라 부위 구분을 밝힘")

# related_species
rep("sections.related_species", sec["related_species"], "body",
    "국내 연구의 다수는 S. herbacea로 적고[9, 10, 11]",
    "여러 국내 연구가 S. herbacea로 적고[9, 10, 11]",
    "'다수'라는 비율 주장은 인용 출처가 말하지 않음")

# cultivation
rep("sections.cultivation", sec["cultivation"], "body",
    "퉁퉁마디는 서해안과 남해안의 염습지, 간척지, 염전 주변에서 자란다[2, 9].",
    "퉁퉁마디는 서해안과 남해안의 염습지와 진흙 해안에서 자라며, 버려진 염전에서 채취한 시료가 연구에 쓰이기도 했다[2, 9].",
    "[2][9] 어디에도 '간척지'는 없음; 염전은 [2]의 '버려진 염전(해남)'만 확인")
rep("sections.cultivation", sec["cultivation"], "body",
    "퉁퉁마디를 먹는 나방 Scrobipalpa salinella는 갯벌 염습지에서 퉁퉁마디의 중요한 해충으로 소개되었고",
    "나방 Scrobipalpa salinella는 갯벌 염습지에서 퉁퉁마디(논문 표기 S. europaea)의 중요한 해충으로 소개되었고",
    "[33] 초록의 학명 표기를 밝힘")
rep("sections.cultivation", sec["cultivation"], "body",
    "S. europaea는 염화나트륨 200–400 mM에서 생장과 광합성 속도가 가장 좋았으므로, 바닷물 수준의 염분이 생육을 돕는다[22].",
    "중국 연구에서 S. europaea는 염화나트륨 200–400 mM에서 생장과 광합성 속도가 가장 좋았다[22]. 이 결과가 국내 함초 재배의 적정 염분으로 그대로 이어지는지는 확인하지 못함.",
    "'바닷물 수준의 염분이 생육을 돕는다'는 [22]에 없는 추론(바닷물 NaCl은 200–400 mM보다 높음) — 삭제")

# processing
rep("sections.processing", sec["processing"], "body",
    "퉁퉁마디는 생채·무침으로 먹고, 분말·환·김·추출물·식초로 가공된다[2, 28].",
    "퉁퉁마디 지상부는 샐러드·절임·발효식품·소금 대용으로 쓰이고, 분말·환·김·추출물·식초로도 가공된다[2, 28].",
    "[2]는 'salads, pickles, fermented food, salt substitutes'라고 씀 — '생채·무침'은 원문 표현이 아님")
rep("sections.processing", sec["processing"], "body",
    "미분쇄 분말을 유동층 코팅기로 구형 과립으로 만든 함초 과립의 상대 짠맛은 소금 대비 0.39였다[7].",
    "미분쇄 분말에 함초 물추출액(고형분 10%)을 섞어 유동층 코팅기로 만든 구형 과립의 상대 짠맛은 소금 대비 0.39였다[7].",
    "[7]의 0.39는 물추출액 10%로 만든 과립(SGMPSAE)의 값")
rep("sections.processing", sec["processing"], "body",
    "2025년 연구는 세 종류 소시지 모두에서 함초 분말을 소금 대용으로 쓸 수 있다고 보았다[25].",
    "2025년 연구는 소금 일부를 함초 분말(염화나트륨 631 mg/g)과 염화칼륨·셀룰로스 등으로 바꾼 배합으로, 세 종류 소시지 모두에서 함초 분말을 소금 대용으로 쓸 수 있다고 보았다[25].",
    "[25]의 배합은 함초 분말 단독이 아니라 KCl·트랜스글루타미네이스·난백분말·셀룰로스를 함께 넣음; 분말의 NaCl 631 mg/g 명시")

# safety
rep("sections.safety", sec["safety"], "body",
    "따라서 함초 분말을 소금 대신 쓰더라도 나트륨 섭취는 줄지 않을 수 있으며, 탈염 분말의 나트륨은 0.71%로 크게 낮았다[4].",
    "소시지 연구에 쓰인 함초 분말도 염화나트륨이 631 mg/g이었으므로, 탈염하지 않은 함초 분말·추출 분말은 그 자체가 나트륨 공급원이다[25]. 반면 탈염 분말은 나트륨(염화나트륨이 아닌 나트륨 기준)이 0.71%로 크게 낮았다[4].",
    "'나트륨 섭취는 줄지 않을 수 있다'는 출처에 없는 추론 — 출처 값으로 바꾸고, NaCl(25–35%)과 Na(0.71%) 기준이 다름을 밝힘")
rep("sections.safety", sec["safety"], "body",
    "키토산으로 감싼 함초는 생쥐에서 나트륨 흡수를 19% 줄였다는 보고도 있다[26].",
    "키토산으로 감싼 생 함초를 48시간 먹인 생쥐에서 나트륨 흡수 억제율이 19.41%로, 감싸지 않은 생 함초(1.36%)보다 높았다는 보고도 있다[26].",
    "[26]의 19%는 '흡수 억제율'(대조 1.36%)이며 48시간 급이 결과")
rep("sections.safety", sec["safety"], "body",
    "이상반응은 섭취군 12.5%, 위약군 12.9%로 차이가 없었고 모두 경미했다[5].",
    "이상반응은 섭취군 12.5%, 위약군 12.9%로 차이가 없었고 모두 경미했다[5]. 다만 이 시험의 1차 평가변수(인지 점수 변화)는 위약과 차이가 없었다[5].",
    "효능 과장 방지: [5]의 1차 결과는 음성")

# compounds
cmp = {c["name"]: c for c in d["compounds"]}
c = cmp["Gypsogenin 3-O-beta-D-glucuronopyranosyl-28-O-beta-D-glucopyranoside"]
c["part"] = "부위 미기재(n-부탄올 분획)"
changes.append({"where": "compounds[Gypsogenin…].part", "before": "지상부(n-부탄올 분획)", "after": "부위 미기재(n-부탄올 분획)", "why": "[14] 초록에 부위 언급 없음"})
c = cmp["Salbige A"]
rep("compounds[Salbige A].content_text", c, "content_text",
    "신규 화합물로 분리, 함량 수치 확인하지 못함[15]",
    "신규 화합물로 분리(중국 신장 염호 시료), 함량 수치 확인하지 못함[2, 15]",
    "[2]가 [15]의 시료를 신장성 염호 채취로 밝힘 — 국내 함초 아님")
c["source"] = [2, 15]
c = cmp["Pentadecyl ferulate"]
c["part"] = "부위 미기재(에틸아세테이트 추출물)"
rep("compounds[Pentadecyl ferulate].content_text", c, "content_text",
    "신규 천연물로 분리, 함량 수치 확인하지 못함[16]",
    "신규 천연물로 분리(중국 장쑤성 시료), 함량 수치 확인하지 못함[2, 16]",
    "[16] 초록에 '전초' 언급 없음; [2]가 장쑤성 시료로 밝힘")
c["source"] = [2, 16]
c = cmp["3,5-Dicaffeoylquinic acid"]
rep("compounds[3,5-DCQA].content_text", c, "content_text",
    "열수추출물에서 분리(순도 > 95%), 함량 수치 확인하지 못함[6]",
    "열수추출물에서 분리(순도 > 95%), 함량 수치 확인하지 못함[6]; 2011년 영광 시료에서도 분리 보고[2]; 같은 계열의 새 디카페오일퀸산 유도체 4종이 지상부에서 분리됨(시험관 항산화)[32]",
    "[32]는 3,5-DCQA 자체가 아니라 새 유도체 4종을 분리한 논문 — 인용 위치를 정확히 함")
c = cmp["Sodium chloride"]
rep("compounds[Sodium chloride].content_text", c, "content_text",
    "원물 나트륨 10 mg/g(기준 미기재)[7]",
    "원물 나트륨 10 mg/g(기준 미기재)[7]; 소시지 연구용 함초 분말 NaCl 631 mg/g[25]",
    "나트륨 함량 확인 — [25] 원문 값 추가")
c["source"] = [3, 4, 7, 25]
c = cmp["Iodine"]

# assays
a = d["assays"][0]
old = a["part"]
a["part"] = "생 원물(부위 미기재) 열수추출 → 활성탄 정제 → 분무건조 분말(논문 표기 Salicornia europaea, 서해안 채취)"
changes.append({"where": "assays[0].part", "before": old, "after": a["part"], "why": "[3] Methods는 'Fresh (plant) collected'라고만 쓰고 지상부라고 하지 않음"})

# sources
src = {s["n"]: s for s in d["sources"]}
def st(n, new, why):
    changes.append({"where": f"sources[{n}].title", "before": src[n]["title"], "after": new, "why": why}); src[n]["title"] = new
st(13, "3-Caffeoyl, 4-dihydrocaffeoylquinic acid from Salicornia herbacea attenuates high glucose-induced hepatic lipogenesis in human HepG2 cells through activation of the liver kinase B1 and silent information regulator T1/AMPK-dependent pathway. Mol Nutr Food Res. 2013;57(3):471-482", "PubMed 서지 대조(제목 축약 복원, 권호 추가)")
st(26, "Effect of encapsulated edible halophyte Salicornia herbacea with different biopolymers on the inhibition of sodium absorption in mouse. Food Sci Nutr. 2021;9(4):1972-1979", "PubMed 서지 대조(권호 추가)")
st(27, "Subacute feeding toxicity of low-sodium sausages manufactured with sodium substitutes and biopolymer-encapsulated saltwort (Salicornia herbacea) in a mouse model. J Sci Food Agric. 2020;100(2):794-802", "PubMed 서지 대조(권호 추가)")
st(34, "Inhibitory effect of 3-caffeoyl-4-dicaffeoylquinic acid from Salicornia herbacea against phorbol ester-induced cyclooxygenase-2 expression in macrophages. Chem Biol Interact. 2010;183(3):397-404", "PubMed 서지 대조(권호 추가; 2009년 12월 온라인, 183권은 2010년 호)")
for n in src:
    if n != 1:
        src[n]["accessed"] = "2026-11-02"

json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
json.dump(changes, open(p.replace("dossier.json", "_review/changes.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(changes))
