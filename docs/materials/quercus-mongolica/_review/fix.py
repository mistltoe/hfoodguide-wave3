import json, re
from pathlib import Path
P = Path(__file__).resolve().parent.parent / "dossier.json"
d = json.load(open(P, encoding="utf-8"))
sec = {s["key"]: s for s in d["sections"]}
changes = []
def rep(key, old, new, why):
    b = sec[key]["body"]
    assert old in b, (key, old[:30])
    sec[key]["body"] = b.replace(old, new)
    changes.append({"where": f"sections.{key}", "before": old, "after": new, "why": why})

MIX = "[9]은 일본산 Q. crispula(var. crispula 계통) 도토리 자료로, 신갈나무 도토리 탄닌은 이 종 자료로만 적으라는 지침에 따라 뺌"
rep("overview",
 "열매(도토리)는 탄닌이 많은 씨앗으로 다뤄지며, 같은 종 복합체인 일본산 Q. crispula 도토리의 탄닌은 건조 중량의 9.9%로 보고되었다[9][10].",
 "열매(도토리)는 중국 설치류 연구에서 물개암나무(Corylus mandshurica) 씨앗보다 탄닌이 많은 고탄닌 종자로 분류되었다[10]. 신갈나무 도토리의 탄닌 함량 수치는 이 자료의 PubMed 문헌으로는 확인하지 못함.",
 MIX)
rep("cultivation",
 "중국 동북부 산림의 10년 자료에서 신갈나무 종자 결실량은 줄무늬다람쥐 개체 수와 음의 상관을 보였다[10].",
 "10년 동안 모은 종자 결실량·설치류 개체 수 자료에서 신갈나무 종자 결실량은 줄무늬다람쥐 개체 수와 음의 상관을 보였다[10].",
 "[10] 초록에는 조사지가 '중국 동북부'라는 말이 없음")
rep("cultivation",
 "공동 정원 시험에서 중국의 토착 참나무 도토리는 도입종 Q. rubra보다 곤충 피해율이 높았다[15].",
 "중국의 공동 정원 시험에서 신갈나무 등 Quercus 절(백참나무류) 도토리는 북미에서 들여온 Q. rubra보다 곤충 피해율이 높았다[15].",
 "[15]의 비교 대상은 '중국 토착 참나무'가 아니라 Quercus 절 참나무(신갈나무·Q. robur·Q. petraea)와 도입종 Q. rubra")
rep("processing",
 "같은 종 복합체인 일본산 Q. crispula 도토리는 탄닌이 건조 중량의 9.9%였고, 이 도토리만 먹인 생쥐는 적응 기간이 없으면 14마리 가운데 8마리가 죽었다[9]. 미리 조금씩 먹여 적응시킨 생쥐는 12마리 가운데 1마리만 죽었고, 침의 프롤린 풍부 단백질과 탄닌 분해 장내 세균이 늘었다[9]. 신갈나무 씨앗은",
 "신갈나무 씨앗은",
 MIX)
rep("processing",
 "고탄닌 먹이는 두 설치류의 체중을 줄였다[10].",
 "고탄닌 먹이는 두 설치류의 체중을 줄였고 줄무늬다람쥐는 생존율도 낮아졌다[10].",
 "[10] 초록: 'only the survival of T. sibiricus was reduced' 보충")
rep("processing",
 "꿀벌이 모은 신갈나무 꽃가루(비폴렌)에서는 폴리아민 유도체와 플라보노이드가 분리되었다[23][24][31].",
 "꿀벌이 모은 신갈나무 꽃가루(비폴렌)에서는 폴리아민 유도체가 분리되고 플라보노이드 배당체 69종이 주석되었으며, 신갈나무 꽃가루에서는 플라보노이드 18종이 분리되었다[23][24][31].",
 "[24] 전문은 '비폴렌'이 아니라 농촌진흥청에서 받은 꽃가루라고만 적음; [31]의 69종 반영")
rep("safety",
 "건강기능식품 고시형 원료가 아니어서 고시된 섭취 시 주의사항은 없다[1].",
 "「식품원료 목록」 자료에 건강기능식품 고시형 원료(KR_NOTICE) 표시가 없고, 고시 제2026-43호 원문에서도 신갈나무를 원재료로 하는 원료를 찾지 못해 고시된 섭취 시 주의사항은 확인하지 못함[1].",
 "card.json lists 에 KR_NOTICE 없음, 고시 원문 줄에 '신갈' 없음 — '없다'를 근거 범위대로 약하게")
rep("safety",
 "탄닌이 많은 도토리를 적응 없이 많이 먹인 생쥐에서 체중 감소와 높은 치사율이 나타났다[9].",
 "신갈나무 씨앗 같은 고탄닌 먹이를 준 설치류 두 종은 체중이 줄었고 줄무늬다람쥐는 생존율도 낮아졌는데, 이는 동물 실험 결과다[10].",
 MIX)

# compounds
c = d["compounds"]
t = [x for x in c if x["name"] == "Tannins"][0]
before = dict(t)
t.update({"part": "열매(도토리)",
 "content_text": "함량 수치는 확인하지 못함; 물개암나무 씨앗보다 탄닌이 많은 고탄닌 종자로 분류[10]",
 "activity_ko": "고탄닌 먹이를 준 설치류 2종 체중 감소, 줄무늬다람쥐는 생존율 감소(동물)[10]",
 "source": [10]})
changes.append({"where": "compounds.Tannins", "before": json.dumps(before, ensure_ascii=False), "after": json.dumps(t, ensure_ascii=False), "why": MIX})
iso = [x for x in c if x["name"].startswith("Isorhamnetin")][0]
ob = iso["activity_ko"]
iso["activity_ko"] = "이 성분 자체의 활성은 확인하지 못함; 같은 종 꽃가루에서 분리한 플라보노이드 18종은 티로시나아제 억제·DPPH 항산화 활성을 보임(시험관)[24]"
changes.append({"where": "compounds.Isorhamnetin 3-O-neohesperidoside.activity_ko", "before": ob, "after": iso["activity_ko"], "why": "[24]가 분리·시험한 18종 목록에 이 성분은 없음; '세포 밖 시험'을 효소·DPPH 시험관 시험으로 정확히"})

# assays
ob = json.dumps(d["assays"], ensure_ascii=False)
d["assays"] = [{
 "role": "literature", "compound": "Ellagic acid", "compound_ko": "엘라그산", "part": "잎",
 "content": "잎 에탄올 추출 플라보노이드(잎 100 g당 5.06 g)의 34.9%[17]",
 "method": "HPLC",
 "conditions": {k: "" for k in ["instrument","column","mobile_phase","gradient","flow","temp","detection","injection","sample_prep","standard","linearity","lod","loq","recovery"]},
 "rationale": "이 종에서 정량 비율이 보고된 주성분이다(초록: 추출물의 주성분을 HPLC로 정제)[17]. 전문 확인 못함: 분석 조건은 비워 둠. 식품원료 사용 부위인 열매(도토리)의 성분을 정량한 PubMed 논문은 확인하지 못함.",
 "source": [17], "url": "https://pubmed.ncbi.nlm.nih.gov/36351050/", "source_kind": "paper"}]
changes.append({"where": "assays", "before": ob, "after": json.dumps(d["assays"], ensure_ascii=False), "why": MIX + "; 이 종을 정량한 [17] 잎 자료로 바꿈"})

# drop source 9, renumber
used_old = [s["n"] for s in d["sources"] if s["n"] != 9]
mp = {o: i+1 for i, o in enumerate(used_old)}
def rn(text):
    return re.sub(r"\[(\d+)\]", lambda m: f"[{mp[int(m.group(1))]}]", text)
def walk(o):
    if isinstance(o, str): return rn(o)
    if isinstance(o, list): return [walk(x) for x in o]
    if isinstance(o, dict):
        return {k: ([mp[x] for x in v] if k == "source" and isinstance(v, list) else walk(v)) for k, v in o.items()}
    return o
d["sources"] = [s for s in d["sources"] if s["n"] != 9]
srcs = d.pop("sources")
d = walk(d)
for s in srcs: s["n"] = mp[s["n"]]
d["sources"] = srcs
json.dump(d, open(P, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
json.dump(changes, open(P.parent / "_review" / "changes.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(changes))
