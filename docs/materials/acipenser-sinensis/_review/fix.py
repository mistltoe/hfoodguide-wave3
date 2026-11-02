import json
from pathlib import Path
P = Path(__file__).resolve().parent.parent / "dossier.json"
d = json.loads(P.read_text())
changes = []
def rep(where, obj, key, old, new, why):
    s = obj[key]
    assert old in s, (where, old)
    obj[key] = s.replace(old, new)
    changes.append({"where": where, "before": old, "after": new, "why": why})
sec = {s["key"]: s for s in d["sections"]}
rep("sections.overview", sec["overview"], "body",
    "이 종은 중국 1급 보호동물이며 국제자연보전연맹(IUCN) 적색목록에서 위급(CR) 종으로 다뤄진다[10, 30].",
    "이 종은 중국 1급 보호동물이며[10], 국제자연보전연맹(IUCN) 적색목록에서 위급(CR) 종으로 다뤄진다[9, 30].",
    "[10] 초록은 중국 1급 보호동물만 말하고 IUCN 위급은 말하지 않음 — IUCN 근거는 [30]·[9](전문 서론)")
rep("sections.related_species", sec["related_species"], "body",
    " 영국에서 산 캐비아 3점을 COI·cyt b 서열로 조사한 연구에서는 CITES 표시 오류는 없었으나 소비자를 오도하는 표시 1건이 확인되었다[14].",
    "",
    "[14] 는 영국 시판 캐비아 일반 조사로 A. sinensis 와 무관 — 캐비아 일반 자료 섞임이라 삭제([14] 는 CITES 일반 서술에만 남김)")
rep("sections.cultivation", sec["cultivation"], "body",
    "담수 양식 조건에서는 암컷 난소가 Ⅱ기에서 Ⅲ기로 잘 넘어가지 않는 것이 인공 번식의 걸림돌이며,",
    "담수 양식 조건에서는 암컷 난소가 Ⅱ기에서 Ⅲ기로 잘 넘어가지 않는 것이 인공 번식의 걸림돌이며[9, 23],",
    "'담수 양식' 표현은 [23] 초록(in captivity)이 아니라 [9] 전문 서론(controlled freshwater culture system)에 있음 — 출처 보강")
rep("sections.cultivation", sec["cultivation"], "body",
    "배란된 알은 16 °C 인공 배양액에서 최소 6시간 수정 능력을 유지했고, 즉시 수정한 대조군의 수정률과 부화율은 82.45%와 84.73%였다[24].",
    "즉시 수정한 대조군의 수정률과 부화율은 82.45%와 84.73%였고, 16 °C 인공 배양액에 보관한 알은 2시간까지 수정률이 유지되다 6시간 뒤 크게 떨어졌으나 부화율은 대조군과 차이가 없어, 저자들은 16 °C 인공 배양액에서 최소 6시간 보관할 수 있다고 결론지었다[24].",
    "[24] 초록: 6시간 보관 시 수정률은 유의하게 감소, 부화율만 유지 — '최소 6시간 수정 능력 유지'는 과장")
rep("sections.cultivation", sec["cultivation"], "body",
    "장염 개체에서는 Aeromonas·Citrobacter 같은 기회감염균이 크게 늘었다[33].",
    "양식 중인 이 종과 칼상어(A. dabryanus)를 함께 조사한 연구에서는 두 종 모두 장염 개체에서 Aeromonas·Citrobacter 같은 기회감염균이 크게 늘었다[33].",
    "[33] 은 중국철갑상어와 칼상어(목록상 별도 원료)를 함께 분석 — 근연종 자료가 섞였음을 명시")
rep("sections.processing", sec["processing"], "body",
    "근육 단백질을 효소로 가수분해할 때",
    "이 종의 단백질을 효소로 가수분해할 때(원료 부위는 초록에 적혀 있지 않음)",
    "[17] 초록은 'Chinese sturgeon protein'만 말하고 근육이라는 부위를 밝히지 않음")
rep("sections.processing", sec["processing"], "body",
    "부산물로는 척삭과 등뼈 연골에서 콘드로이틴 황산을 뽑은 연구가 있으며, 연골 유래는 주로 CS-C형, 척삭 유래는 거의 순수한 CS-A형이었다[15]. 이 콘드로이틴 황산은 시험관에서 상어·소 유래보다 높은 항산화 활성을 보였으나, 사람에게서 확인된 효과는 아니다[15].",
    "부산물로는 이 종과 러시아철갑상어(A. gueldenstaedtii)의 척삭과 등뼈 연골에서 콘드로이틴 황산을 뽑아 비교한 연구가 있으며, 이 종의 분자량은 연골 유래 54.7 kDa, 척삭 유래 25.4 kDa였고 연골 유래는 주로 CS-C형, 척삭 유래는 거의 순수한 CS-A형이었다[15]. 두 종의 철갑상어 콘드로이틴 황산은 시험관에서 상어·소 유래보다 높은 항산화 활성을 보였으나 사람에게서 확인된 효과는 아니며, 저자들은 이당류 조성이 종이 아니라 부위에 따라 정해지므로 이 종 대신 양식 철갑상어 부산물을 쓸 수 있다고 제안했다[15].",
    "[15] 은 러시아철갑상어(다뉴브철갑상어 항목과 같은 종)와 함께 분석했고 항산화 결과는 두 종 철갑상어 CS 전체에 대한 것 — 종 구분 명시")
for c in d["compounds"]:
    if c["name"] == "Triphenyltin":
        rep("compounds.Triphenyltin.activity_ko", c, "activity_ko",
            "실험에서 알 속 농도에 비례해 치어 기형(눈·골격) 발생률이 높아져 기형의 원인 물질로 지목됨[10]",
            "야외 치어 기형률 7.5%; 이 종과 시베리아철갑상어(A. baerii) 알을 쓴 통제 실험에서 알 속 농도에 비례해 기형(눈·골격) 발생률이 높아져 기형의 원인 물질로 지목됨[10]",
            "[10] 의 통제 실험은 시베리아철갑상어 알도 함께 썼음 — 근연종 자료 섞임 명시, 야외 기형률 7.5% 보충")
    if c["name"] == "Chondroitin sulfate":
        rep("compounds.Chondroitin sulfate.activity_ko", c, "activity_ko",
            "시험관 항산화 활성이 상어·소 유래보다 높고 제1형 콜라겐 섬유 형성을 억제(시험관 결과)[15]",
            "이 종·러시아철갑상어 CS 모두 시험관 항산화 활성이 상어·소 유래보다 높고 제1형 콜라겐 섬유 형성을 억제(시험관 결과)[15]",
            "[15] 의 활성 결과는 두 종 철갑상어 CS 공통")
    if c["name"] == "Fish protein hydrolysate":
        rep("compounds.Fish protein hydrolysate.part", c, "part", "근육", "확인하지 못함(초록에 부위 미기재)", "[17] 초록에 부위 없음")
        c["name_ko"] = "단백질 가수분해물"
        changes.append({"where": "compounds.Fish protein hydrolysate.name_ko", "before": "근육 단백질 가수분해물", "after": "단백질 가수분해물", "why": "[17] 초록에 근육이라는 부위 없음"})
d["sources"].sort(key=lambda s: s["n"])
P.write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n")
json.dump(changes, open(Path(__file__).parent / "changes.json", "w"), ensure_ascii=False, indent=1)
print(len(changes))
