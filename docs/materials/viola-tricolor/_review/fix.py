import json, re
from pathlib import Path
P = Path(__file__).resolve().parent.parent / "dossier.json"
d = json.loads(P.read_text())
changes = []
def sec(key): return next(s for s in d["sections"] if s["key"] == key)
def rep(key, old, new, why):
    s = sec(key)
    assert old in s["body"], (key, old)
    s["body"] = s["body"].replace(old, new)
    changes.append({"where": f"sections.{key}", "before": old, "after": new, "why": why})

rep("overview", "꽃잎의 보라색은 루티노사이드가 붙은 델피니딘 계열 안토시아닌이 낸다[10].",
    "꽃잎의 보라색은 주로 루티노사이드가 붙은 델피니딘 계열 안토시아닌이 낸다[10].",
    "[10] 전문: 주 안토시아닌이 델피니딘-루티노사이드형이며 7종 중 일부만 동정(잠정)")
rep("overview", "꽃 추출물에서는 살리실산도 검출되어 안전성 절에서 따로 다룬다[8].",
    "꽃 겔 연구에서는 살리실산도 이 종의 성분으로 거론되어 안전성 절에서 따로 다룬다[8].",
    "[8] 초록은 효과를 루틴·살리실산·클로로겐산 등 '이 종에서 발견되는 성분'에 돌릴 뿐 꽃 추출물에서의 검출·함량을 밝히지 않음")

rep("history", "유럽 의약품청 약초위원회(HMPC)는 2010년 11월 25일 이 종(또는 아종 Viola arvensis)의 꽃 핀 지상부에 대한 공동체 약초 모노그래프를 채택했고, 전통적 용도를 가벼운 지루성 피부 상태의 증상 완화로 정했다고 WebSearch 요약으로만 확인했다[29].",
    "유럽 의약품청 약초위원회(HMPC) 모노그래프의 채택일·적응증 원문은 이 환경에서 EMA 사이트가 열리지 않아 확인하지 못함.",
    "[29] EMA PDF 를 열 수 없고(호스트 차단) WebSearch 요약에만 기댄 값 — 원문 확인 불가로 수치·적응증 삭제")

rep("biology", "이 종은 아연·납·카드뮴으로 오염된 광산 폐석 더미에서도 자라는 통성 금속식물이다[22, 23].",
    "이 종은 아연·납·카드뮴으로 오염된 광산 폐석 더미에서도 자라며, 같은 절의 제비꽃들은 중금속을 몸 안에 잘 들이지 않는 배제형(excluder) 금속식물로 정리되었다[22, 23].",
    "[22]·[23] 초록에 '통성(facultative) 금속식물' 표현 없음; [23] 결론은 Melanium 절 제비꽃이 heavy-metal excluder")
rep("biology", "뿌리에 공생하는 균근균이 식물 기관으로 들어가는 중금속을 줄이는 것으로 보였다[32].",
    "균근균이 붙은 개체는 아연·납 함량이 토양보다 낮아, 균근균이 독성 수준의 중금속 흡수를 막을 수 있다고 추정되었다[32].",
    "[32] 초록은 'might prevent' 로 추정에 그침")
rep("biology", "꽃잎의 유색체 안에 있는 기름방울(플라스토글로뷸)은 트라이아실글리세롤 57%와 카로티노이드·그 에스터 23%로 이루어져 있다[17].",
    "꽃잎의 유색체 안에 있는 기름방울(플라스토글로뷸)은 트라이아실글리세롤 57%와 카로티노이드·그 에스터 23%로 이루어져 있다고 보고되었으나, 이 1982년 연구의 시료('pansy, Viola tricolor L.')가 원예 팬지인지는 확인하지 못함[17].",
    "[17] 초록은 시료를 'petals of the pansy, Viola tricolor L.'로만 적음 — 원예 팬지와 섞였을 가능성 표시")

rep("related_species", "팬지는 삼색제비꽃을 교배해 만든 분류군이며, 두 분류군의 꽃·잎 플라보노이드와 안토시아닌 함량을 비교한 연구가 있다[2].",
    "팬지는 삼색제비꽃을 교배해 만든 분류군이며, 두 분류군의 플라보노이드·안토시아니딘 함량과 항산화능을 비교한 연구가 있다[2].",
    "[2] 초록은 '꽃·잎' 비교를 명시하지 않음(플라보노이드·안토시아니딘 함량, TEAC)")
rep("related_species", "유럽 의약품청 모노그래프는 이 종과 함께 들팬지(Viola arvensis)를 같은 약초로 다루었다고 WebSearch 요약으로만 확인했다[29]. 들팬지 지상부 시료에서는 루틴 0.57–1.15%, 비올란틴 0.80–0.82%, 살리실산 0.09–0.11%가 보고되었지만 이는 다른 종의 값이다[30].",
    "영어로 같은 wild pansy라 불리는 들팬지(Viola arvensis)는 유럽약전 규격 논의 대상이 된 별개의 종이다[30]. 들팬지 건조 지상부 시료(수확 12배치·시판 9배치 평균)에서는 루틴 0.57–1.15%, 비올란틴 0.80–0.82%, 살리실산 0.09–0.11%가 보고되었지만 이는 다른 종의 값이다[30].",
    "[29] 원문 확인 불가로 삭제; [30] 초록은 '건조' 지상부·배치 평균 — 생/건 기준 보강")

rep("cultivation", "이 종은 중금속 오염 토양에서도 잘 자라므로, 오염지에서 자란 개체는 뿌리와 지상부에 중금속을 쌓을 수 있다[23].",
    "이 종은 중금속 오염 토양에서도 자라며, 금속이 많은 토양에서는 뿌리·지상부 농도가 토양보다 낮았지만 금속이 적은 토양에서는 오히려 토양보다 높았다[23].",
    "[23] 결론은 배제형(excluder) — '쌓을 수 있다'는 단순화가 원문과 다름")

rep("processing", "사이클로타이드를 함유한 물 달임액은 끓이는 시간이 길수록 T세포 억제 작용이 강해졌다[16].",
    "사이클로타이드를 함유한 물 달임액은 끓이는 시간이 길수록 시험관에서 사람 T세포 억제 작용이 강해졌다[16].",
    "세포 실험임을 명시(과장 방지)")

rep("genetics", "꽃 색 유전자 VtF3'5'H(플라보노이드 3',5'-수산화효소)는 장미에 옮겨 넣었을 때 꽃잎 안토시아닌 함량을 높였다[35]. ",
    "",
    "[35] 전문 Methods: VtF3'5'H 는 원예 팬지 계통(pansy line PS-12-34) 꽃잎에서 분리 — 원예 팬지 자료 섞임, 또 RhNHX 와 함께 넣은 결과라 삭제")

rep("safety", "꽃 추출물에서는 HPLC로 루틴·클로로겐산과 함께 살리실산이 검출되었다[8]. 이 종에 살리실산과 메틸에스터·비올루토사이드 같은 유도체가 0.3% 들어 있다는 수치는 WebSearch 요약으로만 확인했다[18]. 가까운 종인 들팬지 지상부의 살리실산 함량은 0.09–0.11%였다[30]. 유럽 의약품청 모노그래프의 금기·주의 문구 원문은 확인하지 못함.",
    "꽃 겔 연구에서 연구진은 효과의 일부를 이 종에 있는 루틴·살리실산·클로로겐산 등에 돌렸다[8]. 삼색제비꽃 꽃의 살리실산·살리실산 유도체 함량은 원문으로 확인하지 못함. 다른 종인 들팬지의 건조 지상부에서는 살리실산 0.09–0.11%가 보고되었으나 이 종의 값으로 쓸 수 없다[30]. 유럽 의약품청 모노그래프의 금기·주의 문구 원문은 확인하지 못함.",
    "[8] 초록은 꽃 추출물의 살리실산 HPLC 검출을 명시하지 않음; [18] 0.3% 는 초록에 없고 WebSearch 요약뿐이라 삭제; [30] 은 다른 종·건조 기준임을 명시")
rep("safety", "물 추출물과 달임액은 활성화된 사람 T세포의 증식과 사이토카인 분비를 억제했다[15, 16]. 쥐 실험에서는 추출물이 혈압을 낮추고 칼슘 통로를 막는 작용을 보였다[28]. 생쥐 천식 모델에서는 꽃 추출물 50–200 mg/kg을 먹였을 때 Th2 사이토카인(IL-4)이 줄었다[27].",
    "물 추출물과 달임액은 시험관에서 활성화된 사람 T세포의 증식과 사이토카인 분비를 억제했다[15, 16]. 마취한 쥐에서는 추출물이 혈압을 낮췄고, 토끼 적출 심방·대동맥에서는 L형 칼슘 통로 차단으로 추정되는 심장 억제·혈관 이완 작용을 보였다[28]. 생쥐 천식 모델에서는 꽃 추출물 50·100·200 mg/kg 가운데 100과 200 mg/kg 투여군에서 Th2 사이토카인(IL-4)이 줄었다[27].",
    "[28] 칼슘 통로 차단은 토끼 적출 조직(ex vivo) 결과이고 쥐는 혈압만; [27] IL-4 감소는 100·200 mg/kg 군에서만 보고; [15,16] 세포 실험 명시")

# compounds
for c in d["compounds"]:
    if c["name"] == "Salicylic acid":
        old = dict(c)
        c["part"] = "꽃 겔 연구(이 종의 성분으로 거론)"
        c["content_text"] = "꽃 겔 연구에서 효과에 일부 기여하는 성분으로 거론(초록에 검출 부위·함량 수치 없음); 이 종의 함량은 확인하지 못함"
        c["source"] = [8]
        changes.append({"where": "compounds.Salicylic acid", "before": old["content_text"], "after": c["content_text"], "why": "[8] 초록은 꽃 추출물 HPLC 검출을 명시하지 않음; [18] 0.3% 는 WebSearch 요약뿐이라 삭제"})
    if c["name"] == "Rutin":
        old = c["content_text"]
        c["content_text"] = "지상부(heartsease herb) 420 ± 1.17 µg/g(HPLC; 건/생 기준은 초록에 없음); 꽃 추출물과 겔에서 정량 시험법 검증(함량은 초록에 없음)"
        changes.append({"where": "compounds.Rutin", "before": old, "after": c["content_text"], "why": "기준(생/건) 미기재 명시"})
    if c["name"] in ("Violaxanthin", "Lutein", "Zeaxanthin", "beta-Carotene", "Antheraxanthin"):
        c["part"] = "지상부(신선 생약)"
    if c["name"] == "Cycloviolacin O2":
        old = c["activity_ko"]
        c["activity_ko"] = "분리 사이클로타이드 중 세포독성이 가장 강한 셋 중 하나(시험관 암세포주); 분리물 전체에서 세포독성과 용혈 활성의 상관은 낮았음"
        changes.append({"where": "compounds.Cycloviolacin O2", "before": old, "after": c["activity_ko"], "why": "[13] 상관 관계는 분리물 전체에 대한 진술"})
    if c["name"] == "Mucilage":
        old = c["activity_ko"]
        c["activity_ko"] = "팅크제의 중간 정도 이뇨 작용(쥐, 이뇨 지수 1.103)과 함께 보고"
        changes.append({"where": "compounds.Mucilage", "before": old, "after": c["activity_ko"], "why": "[6] 초록은 'moderate diuretic effect'(쥐)"})
changes.append({"where": "compounds.carotenoids(part)", "before": "지상부(생약)", "after": "지상부(신선 생약)", "why": "[6] 초록: HPLC 8종은 'fresh vegetal drug' 기준"})

# sources: remove 29, 35; fix 18 note; renumber
old18 = next(s for s in d["sources"] if s["n"] == 18)
old18["title"] = "The cumulation of Wild pansy (Viola tricolor L.) accessions: the possibility of species preservation and usage in medicine — Medicina (Kaunas) 2003;39(4):411-6 (초록) (PMID 12738912)"
drop = {29, 35}
d["sources"] = [s for s in d["sources"] if s["n"] not in drop]
mp = {s["n"]: i + 1 for i, s in enumerate(d["sources"])}
for s in d["sources"]: s["n"] = mp[s["n"]]
def remap_text(t):
    def f(m):
        out = []
        for part in re.split(r"\s*,\s*", m.group(1)):
            if re.search(r"[–-]", part):
                a, b = [int(x) for x in re.split(r"\s*[–-]\s*", part)]
                assert all(x in mp for x in range(a, b + 1)), part
                out.append(f"{mp[a]}–{mp[b]}")
            else:
                out.append(str(mp[int(part)]))
        return "[" + ", ".join(out) + "]"
    return re.sub(r"\[(\d+(?:\s*[,–-]\s*\d+)*)\]", f, t)
for s in d["sections"]: s["body"] = remap_text(s["body"])
for arr in ("compounds", "assays"):
    for x in d[arr]:
        x["source"] = [mp[n] for n in x["source"]]
        for k in ("rationale", "content_text", "activity_ko"):
            if isinstance(x.get(k), str): x[k] = remap_text(x[k])
P.write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n")
json.dump(changes, open(P.parent / "_review" / "changes.json", "w"), ensure_ascii=False, indent=1)
print(len(changes))
