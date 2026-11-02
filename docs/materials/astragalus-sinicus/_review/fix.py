import json
from pathlib import Path
P = Path(__file__).resolve().parent.parent / "dossier.json"
d = json.loads(P.read_text())
changes = []
def sec(key): return next(s for s in d["sections"] if s["key"] == key)
def rep(where, obj, field, old, new, why):
    assert old in obj[field], (where, old)
    obj[field] = obj[field].replace(old, new)
    changes.append({"where": where, "before": old, "after": new, "why": why})

rep("sections.overview", sec("overview"), "body",
    "동아시아에 자생하며 연한 어린 잎과 줄기를 먹고 꽃을 차로 우려 마신다는 기록이 있다[2].",
    "동아시아에 자생하며, 안전하다고 여겨지고 어린 잎과 줄기가 연하며 꽃은 차로 우려 마신다고 소개된다[2].",
    "[2] 전문은 'considered safe, with soft young leaves and stems'라고만 써서 잎·줄기를 먹는다는 직접 기술은 없음")
rep("sections.overview", sec("overview"), "body",
    "자운영 연구의 대부분은 녹비·토양 비옥도에 관한 것이고, 약용·식용 성분 연구는 적다[2].",
    "자운영 연구의 대부분은 벼 재배를 돕는 천연 비료(녹비)로서의 역할에 관한 것이고, 약용 자원으로서의 연구는 비교적 적다[2].",
    "[2] 전문은 'potential as a medicinal plant'가 제한적이라고 했고 식용 성분은 언급하지 않음")
rep("sections.biology", sec("biology"), "body",
    "생활형은 문헌마다 달라 두해살이로 적은 자료[4]와 여러해살이로 적은 자료[2, 6]가 있다.",
    "생활형은 문헌마다 달라, 알팔파와 함께 '여러해살이·두해살이' 성질의 작물로 묶어 적은 자료[4]와 여러해살이로 적은 자료[2, 6]가 있다.",
    "[4] 전문은 'AF and MV ... their perennial and biennial characteristics'로 두 작물을 묶어 썼을 뿐 자운영을 두해살이로 단정하지 않음")
rep("sections.cultivation", sec("cultivation"), "body",
    "병해로는 흰가루병[19]과 Embellisia 속 곰팡이에 의한 병[22]이 보고되었다.",
    "병해로는 흰가루병이 보고되었다[19]. 중국 북부에서 근연종 사학황기(A. adsurgens)의 신병해 원인으로 밝혀진 Embellisia 속 곰팡이는 접종 시험에서 자운영에도 병원성을 보였으나, 자운영 재배지 발생 보고는 아니다[22].",
    "[22] 초록은 standing milkvetch(Astragalus adsurgens)의 병해 논문이며 자운영은 접종 시험에서 병원성이 확인된 기주일 뿐임 — 근연종 자료 섞임 정리")
rep("sections.processing", sec("processing"), "body",
    "연한 어린 잎과 줄기를 먹고 꽃은 차로 우려 마신다는 기록이 있다[2].",
    "한국 연구는 어린 잎과 줄기가 연하고 꽃은 차로 우려 마신다고 소개했다[2].",
    "[2] 전문은 잎·줄기를 먹는다고 직접 쓰지 않음(overview 와 같은 수정)")
rep("sections.processing", sec("processing"), "body",
    "연구용 추출물은 대개 전초로 만든다[2, 7].",
    "한국 연구의 에탄올 추출물은 전초로 만들었다[2]. 중국 연구의 물 추출물은 초록에 사용 부위가 적혀 있지 않다[7].",
    "[7] 초록에는 추출 부위가 없어 '대개 전초'를 뒷받침하지 못함")
for c in d["compounds"]:
    if c["name"] == "Daidzin":
        old = c["activity_ko"]
        c["activity_ko"] = "식물성 에스트로겐 계열 이소플라본; 자운영 전초 에탄올 추출물이 MCF-7 세포·난소 절제 생쥐에서 에스트로겐 유사 작용을 보였으나 다이드진 함량이나 기여는 그 연구에서 확인되지 않았다(세포·동물 실험)[2]"
        changes.append({"where": "compounds.Daidzin.activity_ko", "before": old, "after": c["activity_ko"], "why": "[2]는 추출물 전체를 시험했고 다이드진을 정량·분리하지 않음 — 성분 활성으로 과장되지 않게 정리"})
    if c["name"] == "Complogenin":
        changes.append({"where": "compounds.Complogenin.role", "before": c["role"], "after": "bioactive", "why": "[5]는 씨앗에서 분리·구조 확정만 했고 지표성분으로 쓴 근거가 없음(식품원료 부위도 순이 아님)"})
        c["role"] = "bioactive"
a = d["assays"][0]
old = a["rationale"]
a["rationale"] = old + " 이 값은 초기 개화기에 수확한 사료용 지상부를 건조해 건물(DM) 기준으로 잰 것으로, 식품원료 사용 부위인 어린 순의 값이 아니다[1, 4]."
changes.append({"where": "assays[0].rationale", "before": old, "after": a["rationale"], "why": "기준(건물)·부위(개화기 지상부 ≠ 순) 구분 명시"})
P.write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n")
json.dump(changes, open(Path(__file__).parent / "changes.json", "w"), ensure_ascii=False, indent=1)
print(len(changes))
