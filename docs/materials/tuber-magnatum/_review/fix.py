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

# history: [37],[36] web-search-summary only
h = sec("history")
rep("sections.history", h, "body",
    "학명은 1788년 출판된 『Melethemata inauguralia』에서 처음 기재되었고, 명명자 표기는 'Pico'와 'Picco'가 함께 쓰인다는 정리가 있으나 원문은 열지 못해 검색 요약으로만 확인했다[37]. 식약처 목록은 'Pico'로 적는다[1].",
    "명명자 표기는 문헌에 따라 'Pico'[1, 4, 12]와 'Picco'[7, 25, 38]가 함께 쓰이며, 식약처 목록은 'Pico'로 적는다[1]. 원기재 문헌과 연도는 원문을 열지 못해 확인하지 못함.",
    "[37]은 WebSearch 요약뿐이고 원문(AGRIS·Plazi)을 열 수 없음 — 두 표기가 쓰인다는 사실은 열람한 논문 표기로 대체, 1788년 원기재는 확인하지 못함으로 바꿈")
rep("sections.history", h, "body",
    "이탈리아 송로 기본법(1985년 법률 제752호)은 흰서양송로 채취 기간을 10월 1일부터 12월 31일까지로 정하고 주(州)가 달력을 조정할 수 있게 한 것으로 알려져 있으나, 원문은 열지 못해 검색 요약으로만 확인했다[36].",
    "이탈리아의 송로 채취·거래 법령(채취 기간 등)은 원문을 열지 못해 확인하지 못함.",
    "[36]은 WebSearch 요약뿐이고 법령 원문(FAOLEX)은 이 환경에서 열 수 없음 — 조항 수치를 근거 없이 남기지 않음")

# overview: add 알버섯 이명 혼동 (local I1020)
o = sec("overview")
rep("sections.overview", o, "body",
    "이명 '송로버섯'은 다른 송로 원료명과 겹치므로,",
    "덩이버섯속이 아닌 알버섯(Rhizopogon rubescens)도 목록 이명이 '송로(松露)'다[2]. 이명 '송로버섯'은 다른 송로 원료명과 겹치므로,",
    "로컬 I1020 원자료에 알버섯 이명 '송로(松露)'가 있어 이름 혼동 정보를 보탬")

# processing: mycelium caveat
p = sec("processing")
rep("sections.processing", p, "body",
    "흰서양송로 균사를 콩·율무 배지에 고체 발효한 제품이 비싼 자실체를 대신할 재료로 연구되었다[18].",
    "흰서양송로 자실체에서 분리했다는 균주(분자 동정은 논문에 없음)의 균사를 콩·율무 배지에 고체 발효한 제품이 비싼 자실체를 대신할 재료로 연구되었으나[18], 이는 균사와 배지의 혼합물이며 국내 목록의 사용가능부위는 자실체뿐이다[1].",
    "[18] 전문: 균주는 구입한 분리주이고 종 동정 방법이 적혀 있지 않음; 균사 발효물을 자실체 원료와 구분")

# safety: [18] NOAEL design
s = sec("safety")
rep("sections.safety", s, "body",
    "고체 발효 균사 제품을 쥐에게 90일 먹인 시험에서는 3000 mg/kg 체중/일 한 용량에서 이상이 없어 NOAEL로 보고되었지만, 자실체가 아니라 균사와 배지(콩·율무)의 혼합물 결과다[18].",
    "고체 발효 균사 제품을 쥐(암수 각 6마리)에게 90일 먹인 시험에서는 대조군 외에 3000 mg/kg 체중/일 한 용량만 시험해 이상이 없었고 이를 NOAEL로 보고했지만, 용량 반응을 볼 수 없는 설계이고 자실체가 아니라 균사와 배지(콩·율무)의 혼합물 결과다[18].",
    "[18] 전문 Methods: 군당 암수 각 6마리, 0·3000 mg/kg 두 군뿐")

# compounds
C = {c["name"]: c for c in d["compounds"]}
c = C["Bis(methylthio)methane"]
rep("compounds[Bis(methylthio)methane].content_text", c, "content_text",
    "237 ± 27 – 4360 ± 260 μg/kg(대리석덩이버섯 진품 6점은 불검출, 이론상 최대 56 μg/kg 미만)[3]",
    "237 ± 27 – 4360 ± 260 μg/kg(진품 13점)[3]",
    "이 종 함량 칸에서 대리석덩이버섯 값을 빼 판별 설명(activity)으로 옮김")
rep("compounds[Bis(methylthio)methane].activity_ko", c, "activity_ko",
    "대리석덩이버섯과 구별하는 지표[3, 5]",
    "대리석덩이버섯(진품 6점 불검출)과 구별하는 지표[3, 5]",
    "판별 근거를 설명 칸에 둠")
c = C["2(5H)-Furanone"]
rep("compounds[2(5H)-Furanone].content_text", c, "content_text",
    "137 ± 23 – 487 ± 25 μg/kg(대리석덩이버섯 1490 ± 80 – 5010 ± 160 μg/kg)[3]",
    "137 ± 23 – 487 ± 25 μg/kg(진품 13점)[3]",
    "근연종(T. borchii) 수치를 이 종 함량 칸에서 뺌 — 섞임 방지")
rep("compounds[2(5H)-Furanone].activity_ko", c, "activity_ko",
    "이 종에서 일관되게 낮아",
    "대리석덩이버섯보다 이 종에서 일관되게 낮아",
    "비교 대상 명시")
c = C["Gallic acid equivalents (total phenolics)"]
rep("compounds[total phenolics].content_text", c, "content_text",
    "290 mg GAE/100 g[20]",
    "290 mg GAE/100 g(생·건 기준은 초록에 없음)[20]",
    "[20] 초록은 '100 g truffle'로만 적어 기준 불명")
c = C["Riboflavin"]
rep("compounds[Riboflavin].activity_ko", c, "activity_ko",
    "진위 판별용 생체지표 후보로 제시[21]",
    "송로에서 처음 검출된 4개 분자 중 하나; 저자들은 이 결과를 진위 판별 생체지표 탐색의 출발점으로 봄[21]",
    "[21] 초록은 리보플래빈을 생체지표 후보로 특정하지 않음 — 과장 완화")
c = C["1-Pyrroline"]
rep("compounds[1-Pyrroline].activity_ko", c, "activity_ko",
    "이 연구에서 처음 확인됨[5]",
    "이 연구에서 송로의 핵심 향 성분으로 처음 확인됨[5]",
    "[5] 초록: 'identified for the first time as a key odorant'")

# assays
a = next(x for x in d["assays"] if x["compound"] == "Glutathione")
rep("assays[Glutathione].method", a, "method",
    "효소법(아스코르브산)·분광법(분석 세부는 보충자료)",
    "효소법(아스코르브산); 나머지 분석 세부는 보충자료(확인하지 못함)",
    "본문에 '분광법' 언급 없음")
a = next(x for x in d["assays"] if x["compound"] == "Ergosterol")
rep("assays[Ergosterol].rationale", a, "rationale",
    "자실체 성분 지표가 아니라 균사 제품의 품질 지표다[18].",
    "자실체 성분 지표가 아니라 균사 제품의 품질 지표다(값은 건조 발효물 기준)[18].",
    "기준 명시")

# sources
S = {s["n"]: s for s in d["sources"]}
rep("sources[2].title", S[2], "title",
    "검은덩이버섯(T. indicum, 사용불가) (로컬 원자료 대조)",
    "검은덩이버섯(T. indicum, 사용불가), 알버섯(Rhizopogon rubescens, 이명 송로(松露)) (로컬 원자료 I1020_20261013.json 대조)",
    "알버섯 행 추가")
rep("sources[3].title", S[3], "title", "J Agric Food Chem 2024 (", "J Agric Food Chem 2024;72:10023-30 (", "권·쪽 보충(PubMed)")
rep("sources[14].title", S[14], "title", "137Cs content in the fruit bodies of various Tuber species (T. magnatum, T. borchii, T. aestivum, T. excavatum).", "137Cs content in the fruit bodies of various Tuber species.", "원 제목에 없는 괄호 내용 삭제(PubMed 제목과 일치)")

# drop 36, 37 and renumber
used_old = [s["n"] for s in d["sources"] if s["n"] not in (36, 37)]
mp = {o: i + 1 for i, o in enumerate(used_old)}
d["sources"] = [dict(s, n=mp[s["n"]]) for s in d["sources"] if s["n"] in mp]
def remap_text(t):
    def f(m):
        nums = [int(x) for x in re.split(r",\s*", m.group(1))]
        return "[" + ", ".join(str(mp[n]) for n in nums) + "]"
    return re.sub(r"\[(\d+(?:,\s*\d+)*)\]", f, t)
def walk(x):
    if isinstance(x, str): return remap_text(x)
    if isinstance(x, list): return [walk(v) for v in x]
    if isinstance(x, dict):
        out = {}
        for k, v in x.items():
            if k == "source" and isinstance(v, list) and all(isinstance(i, int) for i in v):
                out[k] = [mp[i] for i in v]
            elif k in ("sources",): out[k] = v
            else: out[k] = walk(v)
        return out
    return x
d = walk(d)
P.write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n")
json.dump(changes, open(Path(__file__).parent / "changes.json", "w"), ensure_ascii=False, indent=1)
print(len(changes), mp)
