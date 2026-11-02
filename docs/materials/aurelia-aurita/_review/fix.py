import json, re
from pathlib import Path
P = Path(__file__).resolve().parent.parent / "dossier.json"
d = json.loads(P.read_text())
changes = []
def sec(k): return next(s for s in d["sections"] if s["key"] == k)
def rep(where, obj, key, old, new, why):
    assert old in obj[key], (where, old)
    obj[key] = obj[key].replace(old, new)
    changes.append({"where": where, "before": old, "after": new, "why": why})

o = sec("overview")
rep("sections.overview", o, "body", "건강기능식품 고시형 원료의 원재료로는 연결되어 있지 않다[1].",
    "「건강기능식품의 기준 및 규격」(고시 제2026-43호) 원문에도 해파리를 원재료로 하는 고시형 원료는 없다[34].",
    "[1] 식품원료 목록은 고시형 원료 연결 여부를 말하지 않음; 로컬 고시 원문·요건 json 에서 '해파리' 0건 확인")
h = sec("history")
rep("sections.history", h, "body", "토끼 관절염 모델에 주사하는 실험에도 쓰였다[4][6].",
    "전방십자인대를 절제한 토끼 골관절염 모델에 히알루론산과 함께 주사하는 실험에도 쓰였다[4][6].",
    "[6] 전문: ACL 절제 골관절염 모델, 효과는 히알루론산 병용군에서만")
rep("sections.history", h, "body", " 해양수산부는 보름달물해파리가 많이 나타나면 해역별 주의단계 특보를 낸다(웹 검색 요약으로만 확인)[35].", "",
    "[35] 해양수산부 원문을 작성자도 검토자도 열지 못함(웹 검색 요약만) — 근거 없는 문장 삭제")
b = sec("biology")
rep("sections.biology", b, "body", "생활사 전 단계 전사체 분석에서는 메두사 단계에",
    "홍해 계통 Aurelia 의 생활사 전 단계 전사체 분석에서는 메두사 단계에",
    "[20] 은 Red Sea strain 을 분석함(지역 개체군 구분)")
c = sec("cultivation")
rep("sections.cultivation", c, "body", " 해양수산부는 100 ㎡당 5마리 이상이면 주의단계 특보를 내며, 2024년에는 5월 27일부터 10월 21일까지 특보가 이어졌다(웹 검색 요약으로만 확인)[35].", "",
    "[35] 원문 미확인(웹 검색 요약만, mof.go.kr 은 이 환경에서 접속 불가) — 수치·날짜 삭제")
rep("sections.cultivation", c, "body", "폴립의 출아 번식은 먹이가 많을수록,",
    "실험실 폴립의 출아 번식은 최적 수온(20 °C)에서 먹이가 많을수록,",
    "[23] 초록: 먹이 농도 효과는 최적 수온 20 °C 조건에서 보고됨")
pr = sec("processing")
rep("sections.processing", pr, "body", "콜라겐은 0.5 M 아세트산", "발트해 개체의 콜라겐은 0.5 M 아세트산",
    "[10] 시료는 발트해(러시아) 개체; 산지 명시")
s = sec("safety")
rep("sections.safety", s, "body", "다만 홍해 개체는 입술을 쏘았고 체서피크만 개체보다 독성이 강해, 지역마다 차이가 있다[25].",
    "다만 홍해산 Aurelia(원문은 체서피크만 A. aurita 와 다른 종으로 다룸)는 입술을 쏘았고 체서피크만 개체보다 생쥐 치사·피부괴사 등 독성이 강했다[25].",
    "[25] 제목 'two Cassiopea and Aurelia species' — 홍해 개체를 A. aurita 로 단정할 수 없음(근연종 섞임 방지)")
rep("sections.safety", s, "body", "생쥐 세포 독성은 Cyanea nozakii",
    "생쥐 섬유아세포주(NIH 3T3) 세포독성은 Cyanea nozakii",
    "[26] 초록: NIH 3T3 세포 실험임을 명시")
rep("sections.safety", s, "body", "평균 4,862 mg/kg으로 높았고",
    "평균 4,862 mg/kg(판매 상태 기준, 초록에 생/건 구분 없음)으로 높았고",
    "기준(생/건) 명시: [31] 초록은 시판 식품 측정값만 제시")
rep("sections.safety", s, "body", "JECFA 의 PTWI 는 2 mg/kg 체중이다[29].",
    "JECFA 의 PTWI 는 주당 체중 kg당 2 mg 이다[29][31].",
    "단위 보완: PTWI 는 주간 값(mg/kg bw/week), [31] 초록도 같은 값")

q = next(x for x in d["compounds"] if x["name"] == "Qniumucin")
rep("compounds.Qniumucin.activity_ko", q, "activity_ko",
    "히알루론산과 함께 토끼 무릎에 주사하면 연골 변성이 적었다(동물 실험)[6]",
    "토끼 골관절염 모델에서 히알루론산과 함께 무릎에 주사하면 히알루론산 단독보다 연골 변성이 적었고, 큐니우뮤신 단독은 대조군과 차이가 없었다(동물 실험)[6]",
    "과장 방지: [6] 전문에서 단독 투여는 효과 없음")
cp = next(x for x in d["compounds"] if x["name"].startswith("Ceramide"))
rep("compounds.CAEP.content_text", cp, "content_text",
    "총지질 생조직의 0.031–0.036%; 포스포노지질은 인지질의 21.7%, 그중 CAEP-I 18.3%",
    "함량 수치는 인지질 대비 비율만 있음: 포스포노지질은 인지질의 21.7%, 주성분 CAEP-I 은 인지질의 18.3%(총지질 자체는 생조직의 0.031–0.036%)",
    "[8] 0.031–0.036% 는 총지질 값이지 CAEP 함량이 아님; 18.3% 는 인지질 대비")

w = d["world"]
changes.append({"where": "world[0]", "before": json.dumps(w[0], ensure_ascii=False), "after": "(삭제)",
    "why": "식용 해파리 전체(주로 근구해파리목) 어획량으로 이 종 값이 아니며, 이 종은 상업 어획 대상이 아님; 같은 값은 cultivation 본문에 '종 구분 없음'으로 이미 있음"})
d["world"] = []

# sources: drop 35
d["sources"] = [x for x in d["sources"] if x["n"] != 35]
s34 = next(x for x in d["sources"] if x["n"] == 34)
s34["title"] = s34["title"].replace("(로컬 원문", "및 고시형 원료 전체에서 해파리 원재료 여부 대조(로컬 원문")
used = set()
def scan(o):
    if isinstance(o, str):
        used.update(int(m) for m in re.findall(r"\[(\d+)\]", o))
    elif isinstance(o, dict):
        for k, v in o.items():
            if k == "source" and isinstance(v, list): used.update(v)
            elif k != "sources": scan(v)
    elif isinstance(o, list):
        for v in o: scan(v)
scan(d)
assert 35 not in used, "35 still used"
assert all(x["n"] in used for x in d["sources"]), [x["n"] for x in d["sources"] if x["n"] not in used]
P.write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n")
json.dump(changes, open(Path(__file__).parent / "changes.json", "w"), ensure_ascii=False, indent=1)
print(len(changes))
