import json
from pathlib import Path
P = Path(__file__).resolve().parent.parent / "dossier.json"
d = json.loads(P.read_text())
changes = []

def rep_section(key, old, new, why):
    for s in d["sections"]:
        if s["key"] == key:
            assert old in s["body"], (key, old)
            s["body"] = s["body"].replace(old, new)
            changes.append({"where": f"sections.{key}", "before": old, "after": new, "why": why})
            return
    raise KeyError(key)

def comp(name):
    return next(c for c in d["compounds"] if c["name"] == name)

def set_field(obj, field, new, where, why):
    changes.append({"where": where, "before": obj[field], "after": new, "why": why})
    obj[field] = new

rep_section("overview",
    "세 밀 종류의 값 범위가 서로 겹쳐 건강상 차이는 크지 않을 것이라고 결론지었다[2].",
    "세 밀 종류의 값 범위가 서로 겹쳐 철·아연(섭취 부족 집단이 많은 무기질)을 빼면 건강상 차이는 크지 않을 것이라고 결론지었다[2].",
    "[2] 결론은 '무기질(아연·철)은 예외일 수 있다'를 함께 적음 — 예외를 빠뜨리면 원문 결론과 어긋남")

rep_section("related_species",
    "D 게놈 공여자 쪽은 Q 유전자 서열 비교에서 Ae. tauschii subsp. strangulata 계통이 지목되었다[9].",
    "육배체 밀(보통밀 Chinese Spring 기준)의 D 게놈 공여자로는 q-5D 유전자 서열 비교에서 Ae. tauschii subsp. strangulata 계통이 지목되었다[9].",
    "[9] 초록은 보통밀 'Chinese Spring'의 q-5D 와 같은 서열을 근거로 육배체 밀 전체의 D 게놈 공여자를 추정함 — 스펠트만의 결과처럼 읽히지 않게 범위를 밝힘")

c = comp("Alkylresorcinols")
set_field(c, "activity_ko",
    "통곡 섭취의 바이오마커이자 곡물 진위 판별 지표로 쓰이며, 보통밀 낟알 단면의 질량분석 영상에서 종피·과피 바깥층에 모여 있어 곰팡이 방어 역할과 맞는 분포로 설명되었다(스펠트 낟알 영상은 아님)[4]. 한 연구에서는 스펠트가 보통밀보다 많았고(511.6 대 454.9 µg/g, 비색법)[5], 다른 연구에서는 보통밀(956.5 mg/kg)보다 적었다(817.9 mg/kg, UHPLC-MS)[4]",
    "compounds[Alkylresorcinols].activity_ko",
    "[4] 의 낟알 내 위치 영상(AP-SMALDI MSI)은 보통밀(common wheat) 낟알로만 했음 — 보통밀 자료를 스펠트 사실처럼 쓴 섞임을 밝힘. 두 연구의 분석법 차이(비색법 대 LC-MS)도 원문대로 덧붙임")

notes = {
 "Glycine betaine": ("보통밀보다 약 1.2배(질소 100 kg/ha: 표 값 1.606 대 1.311, 200 kg/ha: 1.537 대 1.307); 원표에 단위 표기가 없어 절대 함량은 확인하지 못함(그림은 건중량 기준이라 밝힘)",),
 "Choline": ("보통밀보다 약 1.2배(질소 100 kg/ha: 표 값 0.2137 대 0.1748, 200 kg/ha: 0.2229 대 0.1854); 원표에 단위 표기가 없어 절대 함량은 확인하지 못함(그림은 건중량 기준이라 밝힘)",),
 "Asparagine": ("보통밀보다 약 1.4–1.5배(질소 100 kg/ha: 표 값 0.6981 대 0.4907, 200 kg/ha: 0.8648 대 0.5664); 원표에 단위 표기가 없어 절대 함량은 확인하지 못함(그림은 건중량 기준이라 밝힘)",),
 "Raffinose": ("보통밀보다 약 1.1–1.2배(질소 100 kg/ha: 표 값 6.916 대 5.95, 200 kg/ha: 6.743 대 5.944); 원표에 단위 표기가 없어 절대 함량은 확인하지 못함(그림은 건중량 기준이라 밝힘)",),
 "Iron": ("철은 보통밀보다 약 1.35배(질소 100 kg/ha: 표 값 47.65 대 35.33, 200 kg/ha: 54.01 대 40.04), 아연은 약 1.4–1.5배(34.37 대 24.41, 40.78 대 27.27); 원표에 단위 표기가 없어 절대 함량은 확인하지 못함(그림은 건중량 기준이라 밝힘)",),
}
for n, (txt,) in notes.items():
    c = comp(n)
    set_field(c, "content_text", txt, f"compounds[{n}].content_text",
        "[2] Table 1 은 단위가 없음 — 단위 없는 숫자만 두면 mg/kg·mg/g 등으로 잘못 읽힐 수 있어 보통밀 대비 배수(원표 값으로 계산)를 앞세우고 절대 함량은 확인하지 못함으로 명시")

a = next(x for x in d["assays"] if x["source"] == [4])
set_field(a["conditions"], "recovery",
    "회수율 시험값은 본문에 없음; 추출 회차별 비율은 1차 92.7% (±1.05), 2차 7.3% (±1.14), 3차 검출 안 됨",
    "assays[AR].conditions.recovery",
    "[4] 의 92.7%·7.3% 는 추출 회차별 비율(추출 효율)이지 첨가 회수율이 아님 — 칸 성격을 원문대로 바로잡음")
set_field(a["conditions"], "loq",
    "AR 17:0 최저 검량 수준(LCL) 100 μg/kg(원문 표 주석; 별도 정량한계 값은 보충자료)",
    "assays[AR].conditions.loq",
    "[4] 표 주석은 LCL 로 적음 — 정량한계가 아니라 최저 검량 수준임을 밝힘")

P.write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n")
Path(__file__).with_name("changes.json").write_text(json.dumps(changes, ensure_ascii=False, indent=1))
print(len(changes))
