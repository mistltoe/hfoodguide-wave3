import json, re, sys
from pathlib import Path
P = Path(__file__).resolve().parent.parent / "dossier.json"
d = json.loads(P.read_text(encoding="utf-8"))
changes = []
S = {s["key"]: s for s in d["sections"]}
def rep(key, old, new, why):
    b = S[key]["body"]
    assert b.count(old) == 1, (key, old)
    S[key]["body"] = b.replace(old, new)
    changes.append({"where": f"sections.{key}", "before": old, "after": new, "why": why})

rep("overview", "고리형 펩타이드인 사이클로타이드다[5, 7, 13].",
    "고리형 펩타이드인 사이클로타이드다[5, 7, 13, 31].",
    "[31] 은 이 종의 플라본 C-배당체 35종을 LC-MS 로 동정한 연구로 플라본 C-배당체 서술의 근거; 샤프토사이드 항목에서 옮김")
rep("history", "2020년판은 말린 전초를 종기·옹종·단독·뱀에 물린 데 쓰며 하루 15–30 g을 쓴다고 정했다고 총설은 전한다[5]. 다른 연구는 V. yedoensis가 1977년판부터 자화지정의 유일한 기원식물로 지정되었다고 적어, 수재 시점에 대한 서술이 출처마다 다르다[2].",
    "2020년판은 말린 전초를 종기·옹종·단독·뱀에 물린 데 쓰며 용량은 15–30 g이라고 정했다고 총설은 전한다[5]. 다른 연구는 V. yedoensis가 1977년판부터 자화지정의 유일한 기원식물로 지정되었다고 적었다[2].",
    "[5] 는 '권장 용량 15–30 g' 이라고만 쓰고 '하루' 는 없음. [5] 의 1963년(첫 수재)과 [2] 의 1977년(유일 기원 지정)은 서로 다른 사실이라 '출처마다 다르다' 는 오해 소지")
rep("biology", "열매 시기에는 길이 10 cm, 너비 4 cm까지 커진다[5].",
    "열매 시기에는 길이 10 cm 넘게, 너비 4 cm까지 커진다[5].",
    "[5] 전문: 'lengths exceeding 10 cm and widths reaching up to 4 cm'")
rep("related_species", "자화지정 약재 18배치를 조사한 연구에서 시판품과 국가 표준 대조약재는 주로 V. prionantha였고, 법정 기원종 V. philippica에서는 에스쿨레틴·에스쿨린이 HPLC에서 거의 검출되지 않았다[2].",
    "자화지정 약재 18배치를 조사한 연구에서 시판품과 국가 표준 대조약재는 주로 V. prionantha였고, 법정 기원종 V. philippica에서는 에스쿨레틴·에스쿨린이 HPLC에서 거의 검출되지 않았다[2]. 이 연구가 감별 지표로 정한 쿠마린 4종(시클로리인·에스쿨린·에스쿨레틴·프리오난토사이드)도 V. prionantha의 주성분으로 확인된 것이다[2].",
    "[2] 전문: 네 쿠마린은 V. prionantha 에서 주성분으로 확인되었고 다른 종(법정 기원종 포함)에서는 검출되지 않거나 매우 적음 — 시료 종 명시")
rep("processing", "전초를 80% 메탄올로 초음파 추출해 HPLC로 비교한 연구는 시클로리인·에스쿨린·에스쿨레틴·프리오난토사이드를 감별 지표성분으로 제안했다[2]. V. philippica 추출물에서는 용매에 따라 성분이 달라, 디클로로메탄·에틸아세테이트 분획에 에스쿨레틴이, 에탄올·부탄올 분획에 시클로리인이 많았다[11].",
    "전초를 80% 메탄올로 초음파 추출해 HPLC로 비교한 연구는 시클로리인·에스쿨린·에스쿨레틴·프리오난토사이드를 감별 지표성분으로 제안했는데, 이 네 성분은 V. prionantha에서 주로 확인되었고 법정 기원종 V. philippica에서는 에스쿨린·에스쿨레틴이 미량이었다[2].",
    "[2] 전문으로 시료 종 명시. 옛 [11](Fitoterapia 2026;191:107238, PMID 41951179)은 PubMed 에 'Retracted Publication' 으로 표시되어 문장 삭제")
rep("processing", "전초 추출물은 실험동물 연구에도 쓰였는데, 육계 사료에 0.5·1.5·4.5% 넣은 시험에서 LPS로 유발한 장 손상이 줄었다[30].",
    "실험동물 연구에도 쓰였는데, 호제비꽃을 육계 사료에 0.5·1.5·4.5% 넣은 시험에서 LPS로 유발한 장 손상이 줄었다[30].",
    "[30] 초록은 'Vy supplementation' 이라고만 하고 추출물이라는 말이 없음")
rep("genetics", "이 종의 사이클로타이드 고리화에 관여하는 사이클로타이드를 만드는 이 식물의 펩타이드 아스파라기닐 연결효소 VyPAL2는 결정 구조가 밝혀져, 기질 인식과 연결 반응의 원리가 제시되었다[25].",
    "사이클로타이드를 만드는 이 식물의 펩타이드 아스파라기닐 연결효소(PAL) VyPAL2는 활성 상태의 결정 구조가 밝혀져, 기질 인식과 연결 반응의 원리가 제시되었다[25].",
    "중복 문구 정리, '고리화에 관여' 는 [25] 초록에 없음(초록은 PAL 이 사이클로타이드 생산 식물의 효소라고만 씀)")

C = {c["name"]: c for c in d["compounds"]}
def cfix(name, field, new, why):
    old = C[name][field]
    C[name][field] = new
    changes.append({"where": f"compounds[{name}].{field}", "before": old if isinstance(old, str) else json.dumps(old), "after": new if isinstance(new, str) else json.dumps(new), "why": why})

cfix("Esculetin", "content_text", "중국약전 2020년판 기준 건조물 0.20% 이상(총설 인용); 반정량 0.484 ± 0.028%(총설 인용); 법정 기원종 V. philippica 시료에서는 HPLC에서 거의 검출 안 됨",
     "옛 [11] 철회 논문의 V. philippica 추출물 함량 삭제")
cfix("Esculetin", "source", [2, 5, 8, 32], "철회 논문 [11] 제거")
cfix("Esculin", "content_text", "n-부탄올 추출물에서 분리(함량 수치 없음)[10]; 자화지정 비교 연구에서는 V. prionantha의 주성분으로 확인되어 감별 지표성분으로 제안, 법정 기원종 V. philippica에서는 미량[2]",
     "[2] 전문: 지표 쿠마린은 V. prionantha 시료에서 확인 — 다른 종 자료가 이 종 지표처럼 읽히지 않게 시료 종 명시")
cfix("Cichoriin", "content_text", "n-부탄올 추출물에서 분리(함량 수치 없음)[10]; 자화지정 비교 연구에서는 V. prionantha의 주성분으로 확인되어 감별 지표성분으로 제안[2]",
     "옛 [11](철회 논문) 함량 삭제, [2] 시료 종 명시")
cfix("Cichoriin", "source", [2, 10], "철회 논문 [11] 제거")
cfix("Prionanthoside", "content_text", "n-부탄올 추출물에서 분리(함량 수치 없음)[10]; 자화지정 비교 연구에서는 V. prionantha의 주성분으로 확인되어 감별 지표성분으로 제안[2]",
     "[2] 전문으로 시료 종 명시")
cfix("Schaftoside", "activity_ko", "플라본 이중 C-배당체(활성 보고 없음)", "'이 종의 대표' 는 [7]·[31] 초록에 근거 없음")
cfix("Schaftoside", "source", [7], "[31] 초록은 샤프토사이드를 명시하지 않음 — overview 의 플라본 C-배당체 문장으로 옮김")
cfix("Apigenin 6-C-alpha-L-arabinopyranosyl-8-C-beta-D-xylopyranoside", "activity_ko", "플라본 이중 C-배당체(활성 보고 없음)",
     "'제비꽃속에서만 보고' 는 card.json 후보(LOTUS) 규칙 문구이고 [7] 이 말하지 않음")
a = C.pop("Delphinidin")
old = json.dumps({k: a[k] for k in ("name", "name_ko", "content_text")}, ensure_ascii=False)
a["name"] = "Anthocyanins (delphinidin, cyanidin, petunidin, malvidin, peonidin glycosides)"
a["name_ko"] = "안토시아닌(5개 아글리콘 계열 14종)"
a["content_text"] = "꽃에서 V. prionantha와 함께 분석해 두 종에서 안토시아닌 14종 동정(아글리콘 Dp·Cy·Pt·Mv·Pn; 종별 분포·함량 수치는 초록에 없음)"
changes.append({"where": "compounds[Delphinidin]", "before": old, "after": json.dumps({k: a[k] for k in ("name", "name_ko", "content_text")}, ensure_ascii=False),
                "why": "[12] 초록: 14종은 델피니딘만이 아니라 5개 아글리콘 계열이며 두 종을 합친 결과"})

# assays: remove retracted [11]
before_n = len(d["assays"])
rm = [x for x in d["assays"] if x["source"] == [11]]
d["assays"] = [x for x in d["assays"] if x["source"] != [11]]
assert len(rm) == 1
changes.append({"where": "assays[Esculetin, cichoriin]", "before": rm[0]["content"], "after": "(삭제)", "why": "[11] PMID 41951179 는 PubMed 에 Retracted Publication 으로 표시됨"})
a0 = d["assays"][0]
oldr = a0["rationale"]
a0["rationale"] = "자화지정과 제비꽃속 위품을 감별하려고 특징 크로마토그램을 만든 방법으로, 네 쿠마린을 지표성분으로 정했다. 전문(Methods)에서 조건을 옮겼다. 네 성분은 V. prionantha의 주성분으로 확인되었고, 법정 기원종 V. philippica(= V. yedoensis)에서는 에스쿨린·에스쿨레틴이 미량이라 HPLC에서 거의 검출되지 않았으며 정량 함량은 본문에 없다[2]."
changes.append({"where": "assays[0].rationale", "before": oldr, "after": a0["rationale"], "why": "[2] 전문: 네 쿠마린은 V. prionantha 에서 확인 — 시료 종 혼동 방지"})
oldp = a0["part"]
a0["part"] = "전초 건조 분말(제비꽃속 6종 야생 시료 42점과 시판 자화지정·대조약재)"
changes.append({"where": "assays[0].part", "before": oldp, "after": a0["part"], "why": "[2] 전문: HPLC 특징 성분 비교는 6종 42점, 18배치는 주로 형태·TLC 비교 후 크로마토그램 대조"})

# drop source 11 and renumber
d["sources"] = [s for s in d["sources"] if s["n"] != 11]
mp = {s["n"]: i + 1 for i, s in enumerate(d["sources"])}
for s in d["sources"]:
    s["n"] = mp[s["n"]]
def remap_text(t):
    def f(m):
        nums = []
        for part in re.split(r"\s*,\s*", m.group(1)):
            if re.search(r"[–-]", part):
                x, y = [int(v) for v in re.split(r"\s*[–-]\s*", part)]
                nums += list(range(x, y + 1))
            else:
                nums.append(int(part))
        nums = sorted({mp[n] for n in nums})
        return "[" + ", ".join(map(str, nums)) + "]"
    return re.sub(r"\[(\d+(?:\s*[,–-]\s*\d+)*)\]", f, t) if isinstance(t, str) else t
for s in d["sections"]:
    s["body"] = remap_text(s["body"])
for arr in ("compounds", "assays", "markers", "production", "gi", "orgs", "world"):
    for x in d.get(arr) or []:
        x["source"] = [mp[n] for n in x.get("source", [])]
        for k in ("content_text", "activity_ko", "content", "rationale", "note"):
            if k in x: x[k] = remap_text(x[k])
d["compounds"] = list(C.values()) if False else d["compounds"]
P.write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
json.dump(changes, open(Path(__file__).parent / "changes.json", "w"), ensure_ascii=False, indent=1)
print(len(changes))
