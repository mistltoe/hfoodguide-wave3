import json, re
from pathlib import Path
P = Path(__file__).resolve().parent.parent / "dossier.json"
d = json.loads(P.read_text())
S = {s["key"]: s for s in d["sections"]}
changes = []
def rep(key, old, new, why):
    b = S[key]["body"]
    assert old in b, (key, old[:40])
    S[key]["body"] = b.replace(old, new)
    changes.append({"where": f"sections.{key}", "before": old, "after": new, "why": why})

# overview: research parts vs food-use parts
old = "잎에서도 오레가닌과 5-O-메틸히르수타노놀이 분리되었다[22, 23, 25]."
rep("overview", old, old + " 디아릴헵타노이드 연구 부위 가운데 나무껍질[7, 17, 18, 19, 34]과 잎[22, 23, 24, 25]은 식품원료 사용 부위(수피·잎)와 같지만, 열매(고리형 디아릴헵타노이드·트리테르페노이드[8, 26])와 줄기(리그난[27])는 사용 부위 밖이다[1]. 또 근육 연구[16]는 껍질을 포함한 줄기를, 간암 줄기세포 연구[31]는 줄기·잎·뿌리줄기를 섞은 원료를 써서 수피만의 결과로 볼 수 없다.",
    "디아릴헵타노이드 연구 부위를 [7][17][18][19][34](bark)·[22]-[25](leaves)·[8][26](fruits)·[27](stem)·[16](stem including barks)·[31](stems, leaves, rhizomes) 원문으로 확인해 식품원료 사용 부위와 구분")

# history: patent wording
rep("history", "오리나무 조각을 발효한 추출물은 발효 추출물과 영양 음료 용도로 특허가 출원되었다고 한 논문이 소개했다[31].",
    "오리나무 조각을 미생물과 함께 발효한 추출물이 발효 추출물과 영양 음료 용도로 특허를 받았다고 한 논문이 서론에서 소개했다(특허 원문은 확인하지 못함)[31].",
    "[31] 서론은 'have been patented'라고만 쓰고 출원/등록 구분이 없으며, 특허 원문은 인용 문헌으로만 제시됨")

# related species: oregonin inference
rep("related_species", "오레가닌은 다른 오리나무속 식물에도 들어 있어 오레가닌만으로 종을 가리기는 어렵다[16].",
    "오레가닌은 오리나무속 식물 전반에서 나오는 속 수준의 주요 지표물질로 소개되므로[16], 오레가닌 검출만으로 오리나무(A. japonica) 원료임을 가릴 수는 없다.",
    "[16]은 oregonin 을 'a major indicator substance of the genus'로만 씀 — 종 구분 불가는 거기서 나온 해석임을 분명히 함")

# cultivation: remove unsupported inference
rep("cultivation", "잎은 잎벌레 애벌레가 즐겨 먹어 잎을 원료로 쓸 때 해충 피해 관리가 필요할 수 있다[36]. ",
    "", "[36]은 실험실 섭식 선호 시험일 뿐 원료 생산·해충 관리를 말하지 않음(근거 없는 추론 삭제)")

# processing: list does not specify solvent
rep("processing", "식품원료 목록에 오리나무농축액·오리나무추출액이 원료명으로 올라 있어, 수피와 잎을 물이나 주정으로 우린 추출물 형태로 주로 쓴다[1].",
    "식품원료 목록에 오리나무농축액·오리나무추출액이 원료명으로 올라 있어 수피·잎을 농축액·추출액 형태로도 쓸 수 있다[1]. 추출 용매나 방법은 목록에 적혀 있지 않다[1].",
    "I1020 원자료 행에는 원료명·부위 조건만 있고 '물이나 주정', '주로'에 해당하는 내용 없음")
rep("processing", "같은 연구진의 후속 연구에서도 열수 추출물이 오레가닌의 비배당체인 히르수타노놀과 히르수테논을 에탄올 추출물보다 많이 담고 있었다[16].",
    "같은 연구진의 후속 연구에서도 열수 추출물(원료: 껍질을 포함한 줄기)이 오레가닌의 비배당체인 히르수타노놀과 히르수테논을 50% 에탄올 추출물(원료: 말린 나무껍질)보다 많이 담고 있었다[16].",
    "[16] 4.1.1·4.1.2: 열수 추출 원료는 'stem, including barks', 에탄올 추출 원료는 'dried bark' — 원료 부위가 달라 명시")
rep("processing", "오리나무 조각을 미생물로 발효한 추출물도 연구되었다[31].",
    "오리나무 조각을 미생물로 발효한 추출물도 연구되었는데, 이 연구의 원료는 오키나와에서 재배된 나무의 줄기·잎·뿌리줄기를 섞은 것이었다[31].",
    "[31] 2.2: 'Stems, leaves, and rhizomes ... mixed', 오키나와 얀바루 재배목(1910년 대만에서 도입) — 원료 부위·산지 명시")

# safety: remove 50% sentence (not in local raw data), fix [16] context, [19] concentration, [32] population
rep("safety", " 식품공전은 따로 사용 조건이 없는 제한적 사용 원료를 가공 전 원료 중량 기준 50% 미만으로 쓰도록 정한다고 검색 요약에 나오나, 원문은 열지 못해 확인하지 못함[3].",
    " '제한적사용' 원료에 공통으로 적용되는 식품공전의 배합 기준은 원문을 확인하지 못해 적지 않는다.",
    "식품공전 '50% 미만' 기준은 WebSearch 요약뿐이고 로컬 I1020 원자료(오리나무 5행·제한적사용 728행)에 해당 문구 없음 — 출처 [3] 과 함께 삭제")
rep("safety", "생쥐에게 껍질을 포함한 줄기 열수 추출물을 하루 20·50·100·200 mg/kg씩 4주간 먹인 시험에서는 모든 군의 체중이 정상적으로 늘었으나, 연구진은 장기 독성을 평가하지 않았다고 밝혔다[16].",
    "덱사메타손으로 근위축을 유발한 생쥐에게 껍질을 포함한 줄기 열수 추출물을 하루 20·50·100·200 mg/kg씩 4주간 먹인 효능 시험에서 모든 군의 체중은 계속 늘었으나(3주째부터 근위축 유발군은 정상군보다 낮음), 이는 독성 시험이 아니며 연구진도 장기 독성을 평가하지 않았다고 밝혔다[16].",
    "[16] 2.2·4.4: 근위축 모델(덱사메타손 5 mg/kg 복강 주사)의 효능 시험이고 3주째부터 근위축군 체중이 낮았음 — 안전성 근거로 과장되지 않게 맥락 추가")
rep("safety", "오레가닌과 히르수타논은 시험 농도에서 사람 정상 피부섬유아세포에 독성을 보이지 않았다[19].",
    "오레가닌과 히르수타논은 50 μM에서 사람 정상 피부섬유아세포(NB1RGB)에 독성을 보이지 않았으나 백혈병 세포에는 약한 독성을 보였다[19].",
    "[19] 초록: 'not toxic ... at a concentration of 50 μM; however, lower levels of toxicity were observed for leukemia cells'")
rep("safety", "일본 화분증 환자 110명에서 오리나무 꽃가루 특이 IgE가 추적 측정되어, 꽃가루는 알레르기 항원으로 다뤄진다[32].",
    "일본에서 삼나무 설하면역요법을 받은 환자 가운데 오리나무 특이 IgE가 class 1 이상인 110명의 수치가 3년간 추적되어, 오리나무 꽃가루는 알레르기 검사 항원으로 쓰인다[32]. 이는 꽃가루에 관한 것으로 식품원료 부위(수피·잎) 섭취 알레르기 자료는 아니다.",
    "[32] 초록: 대상은 삼나무 SLIT 환자 429명 중 오리나무 sIgE class≥1 인 110명 — '화분증 환자 110명' 표현을 원문대로")

# compounds: quercetin from [31]
for c in d["compounds"]:
    if c["name"] == "Quercetin":
        b = dict(c)
        c["part"] = "줄기·잎·뿌리줄기 혼합 원료 추출물(논문은 bark extract 로 부름)"
        c["content_text"] = "논문이 인용한 선행 분석에서 RP-HPLC로 정량된 주요 플라보노이드의 하나(수치는 확인하지 못함)[31]"
        c["activity_ko"] = "시판 표준품 퀘르세틴이 간암 줄기세포 유사 세포에서 자가포식을 유도해 추출물 효과에 기여하는 성분으로 제시(세포)[31]"
        changes.append({"where": "compounds.Quercetin", "before": json.dumps({k: b[k] for k in ("part","content_text","activity_ko")}, ensure_ascii=False), "after": json.dumps({k: c[k] for k in ("part","content_text","activity_ko")}, ensure_ascii=False), "why": "[31] 2.2·2.3: 원료는 줄기·잎·뿌리줄기 혼합, 플라보노이드 정량은 인용 문헌 방법, 세포 시험은 구입한 표준품 사용"})
# assays: detection not in HPLC section of [16]
for a in d["assays"]:
    if 16 in a["source"]:
        changes.append({"where": "assays[Hirsutenone].conditions.detection", "before": a["conditions"]["detection"], "after": "", "why": "[16] 4.2.3 HPLC 절에 검출 파장 없음(280 nm·HECTOR 칼럼은 LC-MS/MS 절) — 원문에 없는 칸은 비움"})
        a["conditions"]["detection"] = ""

# drop source 3 and renumber
used_old = [s["n"] for s in d["sources"] if s["n"] != 3]
mp = {o: i + 1 for i, o in enumerate(used_old)}
def remap_text(t):
    def f(m):
        nums = [int(x) for x in re.split(r",\s*", m.group(1))]
        assert 3 not in nums, t
        return "[" + ", ".join(str(mp[n]) for n in nums) + "]"
    return re.sub(r"\[(\d+(?:,\s*\d+)*)\]", f, t)
def walk(o):
    if isinstance(o, str): return remap_text(o)
    if isinstance(o, list): return [walk(x) for x in o]
    if isinstance(o, dict):
        return {k: ([mp[x] for x in v] if k == "source" and isinstance(v, list) else walk(v)) for k, v in o.items()}
    return o
srcs = [s for s in d["sources"] if s["n"] != 3]
for s in srcs: s["n"] = mp[s["n"]]
body = {k: v for k, v in d.items() if k != "sources"}
body = walk(body)
body["sources"] = srcs
P.write_text(json.dumps(body, ensure_ascii=False, indent=1) + "\n")
changes.append({"where": "sources", "before": "[3] 식품공전 식품원료 판단기준(WebSearch 요약)", "after": "삭제, 4–36 → 3–35 재번호", "why": "로컬 원자료로 확인되지 않은 WebSearch 요약 출처"})
json.dump(changes, open(Path(__file__).parent / "changes.json", "w"), ensure_ascii=False, indent=1)
print(len(changes))
