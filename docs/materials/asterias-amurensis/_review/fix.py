import json, re, sys
from pathlib import Path
P = Path(sys.argv[1]); D = json.loads(P.read_text())
changes = []
def sec(k): return next(s for s in D["sections"] if s["key"] == k)
def rep(where, obj, key, old, new, why):
    t = obj[key]
    assert old in t, (where, old)
    obj[key] = t.replace(old, new)
    changes.append({"where": where, "before": old, "after": new, "why": why})

# overview
rep("sections.overview", sec("overview"), "body",
    "즉 식품원료로서의 지위는 몸 전체가 아니라 껍질(골격이 든 체벽)을 칼슘 보충용 원료로 쓰는 경우로 한정된다[1].",
    "즉 식품원료로서의 지위는 몸 전체가 아니라 껍질을 칼슘 보충용 원료로 쓰는 경우로 한정된다[1].",
    "'골격이 든 체벽'은 원자료[1]에 없는 해석이라 뺌")
# history
rep("sections.history", sec("history"), "body",
    "1969년 이 종에서 난모세포의 감수분열을 일으키는 물질이 분리·동정되었고, 이 물질은 뒤에 1-메틸아데닌으로 정리되었다[19, 20].",
    "1969년 이 종에서 난모세포의 감수분열을 일으키는 물질이 분리·동정되었으며, 불가사리의 이 성숙 유도 호르몬은 1-메틸아데닌이다[19, 20].",
    "'뒤에 정리되었다'는 [19]·[20]이 말하지 않음 — [19]는 1969년 분리·동정 보고, [20]은 1-메틸아데닌을 성숙 유도 호르몬으로 정리")
rep("sections.history", sec("history"), "body",
    "식품 소재로는 껍질 골판을 칼슘 원료로 보려는 국내 연구가 2000년대에 나왔다고 검색 요약에 나오나, 원문은 열지 못해 세부는 확인하지 못함. ",
    "",
    "WebSearch 요약에만 기댄 서술이라 삭제(원문 미대조)")
# biology
rep("sections.biology", sec("biology"), "body",
    "알과 정자를 바다에 내보내 체외수정을 하고, 유생(bipinnaria)은 물에 떠서 지내다 바닥 생활로 바뀐다[26, 5]. 체벽은 방해석 골편과 콜라겐 조직·근육으로 이루어진다[5].",
    "불가사리류는 알과 정자를 바다에 내보내 체외수정을 하고 유생기에는 물에 떠서 지내다 바닥 생활로 바뀌며, 체벽은 방해석 골편과 이를 잇는 콜라겐 조직·근육으로 이루어진다고 한 리뷰는 설명한다[5]. 이 종의 부유 유생(bipinnaria)은 전사체 연구 시료로 쓰였다[26].",
    "[5]의 생식·체벽 설명은 불가사리 일반(전문에서 종명 없음)이므로 이 종 고유 사실처럼 쓰지 않음; [26]은 bipinnaria 유생만 뒷받침")
# cultivation
rep("sections.cultivation", sec("cultivation"), "body",
    "수온 5–15 °C에서 먹이 활동이 늘어 5–6월에 포식이 가장 활발하므로 그 전후를 제거 시기로 권하는 내용도 있다[5].",
    "수온 5–15 °C에서는 수온이 오를수록 먹이 활동이 늘어 5–6월에 포식이 가장 활발하고, 먹이 활동이 크게 줄어드는 8월을 대규모 제거의 적기로 보는 내용도 있다[5].",
    "[5] 원문은 5–6월 포식 절정, 8월을 대규모 제거 적기로 씀('그 전후'는 원문과 다름)")
rep("sections.cultivation", sec("cultivation"), "body",
    "오스트레일리아에서는 침입한 이 종을 생물적으로 억제하려는 시도와 환경 DNA 감시가 연구되었다[28, 29].",
    "오스트레일리아에서는 토착 불가사리(Coscinasterias muricata)가 홍합 양식장에서 이 종의 이용을 제한할 수 있다는 관찰[29]과, 유전 조사·환경 DNA 플랑크톤 채집·해류 모형으로 확산 경로를 밝힌 연구가 있었다[28].",
    "[29]는 억제 '시도'가 아니라 토착 포식자 관찰 연구, [28]은 감시가 아니라 확산 경로 연구")
# processing
rep("sections.processing", sec("processing"), "body",
    "국립수산과학원 연구진의 2012년 연구는 아무르불가사리 골판 분말 무기질의 칼슘 비율이 98.95%이고 XRD상 탄산칼슘 형태라고 보고한 것으로 웹 검색 요약에 나오며, 원문은 열지 못했다[32]. 2005년 국내 쥐 실험에서는 불가사리 칼슘 식이군이 탄산칼슘 식이군과 성장·식이 섭취량·식이효율에 차이가 없었다고 요약되었고, 이 역시 원문은 열지 못했다[33].",
    "불가사리 골격은 주로 탄산칼슘 같은 무기염으로 이루어진다고 한 리뷰는 설명한다[5]. 껍질 칼슘의 조성과 체내 이용성을 다룬 국내 연구는 원문을 열어 대조하지 못해 수치를 싣지 않았고, 이 종 껍질 칼슘의 함량은 확인하지 못함.",
    "[32]·[33]은 WebSearch 요약으로만 본 출처(원문·학명 미확인)라 수치와 출처를 뺌")
# genetics
rep("sections.genetics", sec("genetics"), "body",
    "중국 북부와 일본 북부 개체가 2% 넘게 차이 나는 두 계통으로 나뉘었다[25].",
    "중국 북부(일본 세토내해 우시마도 개체 포함)와 일본 북부(아사무시·오나가와) 개체가 서로 2% 넘게 차이 나는 두 계통으로 나뉘었다[25].",
    "[25] 초록: 한 계통은 중국 북부+우시마도, 다른 계통은 일본 북부")
# safety
rep("sections.safety", sec("safety"), "body",
    "몸에는 스테로이드 배당체인 아스테로사포닌이 들어 있으며, 조사포닌은 시험관에서 적혈구를 터뜨리는 용혈 활성을 보였다[11, 12, 13]. 이 종의 폴리하이드록시스테로이드 유도체는 바다송사리 배아에 독성을 나타냈다[17].",
    "몸에는 스테로이드 배당체인 아스테로사포닌이 들어 있다[11, 12]. 이 종과 별불가사리의 조사포닌은 시험관에서 용혈 활성(EC50 10–100 µg/mL)을 보였다[13]. 이 종에서 분리한 폴리하이드록시스테로이드 유도체 가운데 하나는 바다송사리 배아에 독성을 나타냈다[17].",
    "[13]은 두 종 조사포닌을 함께 보고 — 종 구분 명시; [17]은 분리 화합물 5종 중 화합물 5가 주로 독성")

# compounds
C = {c["name"]: c for c in D["compounds"]}
c = C["Calcium carbonate"]
old = dict(c)
c["content_text"] = "이 종 껍질의 칼슘·탄산칼슘 함량은 확인하지 못함[1]"
c["activity_ko"] = "식약처 목록에서 이 종 껍질은 칼슘보충용 원료로 한정되어 있고[1], 불가사리 골격은 주로 탄산칼슘으로 이루어진다고 설명된다[5]"
c["source"] = [1, 5]
changes.append({"where": "compounds.Calcium carbonate", "before": old["content_text"] + " / " + old["activity_ko"], "after": c["content_text"] + " / " + c["activity_ko"], "why": "[32] WebSearch 요약 수치 삭제, '근거 성분' 인과 서술은 [1]이 말하지 않음"})
c = C["Asterosaponin 1"]; o = c["activity_ko"]
c["activity_ko"] = "수용성 분획에서 글리코사이드 B2와 함께 분리되었다[14]; 이 종과 별불가사리의 조사포닌은 용혈 활성을 보였다[13]"
changes.append({"where": "compounds.Asterosaponin 1.activity_ko", "before": o, "after": c["activity_ko"], "why": "[13]은 두 종 혼합 보고"})
c = C["Glucosylceramide"]; o = c["part"]; c["part"] = "내장·생식소"
changes.append({"where": "compounds.Glucosylceramide.part", "before": o, "after": c["part"], "why": "'알'은 [9]·[15]에 없음"})

# aliases
for a in ["아무르불가사리", "Amur starfish"]:
    D["aliases"].remove(a)
    changes.append({"where": "aliases", "before": a, "after": "(삭제)", "why": "출처 없음([32] 검색 요약에서 온 이름)"})

# sources: fix metadata, drop 32,33, renumber
S = {s["n"]: s for s in D["sources"]}
o = S[13]["title"]
S[13]["title"] = o.replace("J Vet Med Sci 2010;73(2):227-229", "J Vet Med Sci 2011;73(2):227-229(PubMed 출판일 표기 2010-09-14)")
changes.append({"where": "sources[13].title", "before": "J Vet Med Sci 2010;73(2)", "after": "J Vet Med Sci 2011;73(2)(PubMed 출판일 표기 2010-09-14)", "why": "73권은 2011년"})
o = S[25]["url"]; S[25]["url"] = "https://doi.org/10.1080/24701394.2023.2276749"
changes.append({"where": "sources[25].url", "before": o, "after": S[25]["url"], "why": "PubMed 메타데이터의 DOI로 바꿈"})
S[1]["title"] = S[1]["title"].replace("같은 원자료에서", "card.json lists 비어 있음(건강기능식품 고시형 원료 아님); 같은 원자료에서")
used = set()
def collect(x):
    if isinstance(x, str):
        for m in re.finditer(r"\[(\d+(?:\s*[,–-]\s*\d+)*)\]", x):
            for p in re.split(r"\s*,\s*", m.group(1)):
                if re.search(r"[–-]", p):
                    a, b = map(int, re.split(r"\s*[–-]\s*", p)); used.update(range(a, b+1))
                else: used.add(int(p))
    elif isinstance(x, list):
        for y in x: collect(y)
    elif isinstance(x, dict):
        for k, v in x.items():
            if k == "source" and isinstance(v, list): used.update(v)
            else: collect(v)
collect({k: v for k, v in D.items() if k != "sources"})
assert 32 not in used and 33 not in used, used
keep = sorted(n for n in S if n in used)
mp = {o: i+1 for i, o in enumerate(keep)}
def remap_text(x):
    def f(m):
        parts = re.split(r"(\s*,\s*)", m.group(1))
        out = []
        for p in parts:
            if re.fullmatch(r"\s*,\s*", p): out.append(p)
            elif re.search(r"[–-]", p):
                a, b = map(int, re.split(r"\s*[–-]\s*", p)); out.append(f"{mp[a]}–{mp[b]}")
            else: out.append(str(mp[int(p)]))
        return "[" + "".join(out) + "]"
    return re.sub(r"\[(\d+(?:\s*[,–-]\s*\d+)*)\]", f, x)
def walk(x):
    if isinstance(x, str): return remap_text(x)
    if isinstance(x, list): return [walk(y) for y in x]
    if isinstance(x, dict):
        return {k: ([mp[i] for i in v] if k == "source" and isinstance(v, list) and all(isinstance(i, int) for i in v) else walk(v)) for k, v in x.items()}
    return x
for k in list(D):
    if k not in ("sources", "slug", "name_ko", "name_en", "scientific_name", "aliases"):
        D[k] = walk(D[k])
D["sources"] = [dict(S[o], n=mp[o]) for o in keep]
changes.append({"where": "sources", "before": "35개", "after": f"{len(keep)}개", "why": "[32]·[33](WebSearch 요약만 확인) 삭제 후 번호 정리(34→32, 35→33)"})
P.write_text(json.dumps(D, ensure_ascii=False, indent=1))
Path(sys.argv[2]).write_text(json.dumps(changes, ensure_ascii=False, indent=1))
print(len(changes), mp)
