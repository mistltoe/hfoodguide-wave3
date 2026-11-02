import json, re, pathlib
P = pathlib.Path(__file__).resolve().parents[1] / "dossier.json"
d = json.loads(P.read_text(encoding="utf-8"))
S = {s["key"]: s for s in d["sections"]}
def rep(key, old, new):
    b = S[key]["body"]; assert old in b, (key, old[:40]); S[key]["body"] = b.replace(old, new)

# overview: 50% 기준(검색 요약) 삭제, 씨앗·가지 사용불가 추가
rep("overview", "이 목록에서 측백나무는 '제한적사용' 원료이며 사용 조건은 '제한적사용가능부위 : 잎※(측백엽)'으로, 잎만 식품에 쓸 수 있다[1]. 식품공전의 '식품에 제한적으로 사용할 수 있는 원료'는 정해진 조건 안에서만 쓰는 원료이고, 별도 조건이 없으면 가공 전 원료 중량의 50% 미만으로 쓴다는 기준이 있으나 이 내용은 원문이 아닌 검색 요약으로만 확인했다[2].",
    "이 두 원료는 '제한적사용' 원료이며 사용 조건은 '제한적사용가능부위 : 잎※(측백엽)'으로, 잎만 식품에 쓸 수 있다[1]. 같은 목록에서 측백나무씨앗과 측백나무가지는 '사용불가'로 분류되어 있다[1]. 제한적 사용 원료에 적용되는 식품공전의 구체적인 사용량 기준은 원문으로 확인하지 못함.")
# history: 도동 측백나무 숲(검색 요약·언론) 삭제
rep("history", "대구 도동 측백나무 숲은 1962년 천연기념물 제1호로 지정되었다고 보도되었으나, 이 내용은 국가유산청 원문이 아닌 검색 요약으로만 확인했다[35]. ", "")
# related_species: Thuja속 다른 종 정유 비교 추가
rep("related_species", "서양측백(Thuja occidentalis) 등 Thuja속 다른 종과의 성분 비교 자료는 확인하지 못함.",
    "이름이 비슷한 서양측백(Thuja occidentalis)과 Thuja plicata의 잎 정유는 α·β-투존, 펜콘, 사비넨이 주성분이고 케톤류가 54.30~69.18%를 차지해[36], α-피넨/δ-3-카렌형인 측백나무 잎 정유와 성분 유형이 다르다[4].")
# processing
rep("processing", "국내 식품원료 목록에는 잎(측백엽)과 잎 추출물이 원료명으로 올라 있다[1].",
    "국내 식품원료 목록에는 잎(측백엽)과 잎 추출물이 원료명으로 올라 있다[1]. 중국 약재 측백엽(Platycladi Cacumen)은 말린 어린 가지와 잎을 함께 이르지만[6], 국내 목록에서 측백나무가지는 '사용불가'다[1].")
rep("processing", "국내에서는 잎 물 추출물을 12주 동안 두피에 바른 시험에서 성모 밀도가 늘었다는 보고가 있다[26]. 씨앗 기름 추출물은 무릎 골관절염 시험에 쓰였지만, 씨앗은 국내 식품원료 사용 가능 부위가 아니다[31, 1].",
    "국내 한 기업 연구소의 시험에서 잎 물 추출물 1% 용액을 12주 동안 두피에 바른 군(30명)은 성모 밀도가 cm²당 평균 4.01개 늘었고 처치하지 않은 대조군(30명)은 뚜렷한 변화가 없었으나, 이는 바르는 시험이며 먹었을 때의 효과를 본 것은 아니다[26]. 씨앗 기름 추출물은 무릎 골관절염 시험에 쓰였지만[31], 씨앗은 국내 「식품원료 목록」에서 '사용불가'다[1].")
# safety 전면 재작성
S["safety"]["body"] = (
 "측백나무는 식약처 「식품원료 목록」에서 잎과 잎 추출물만 '제한적사용' 원료이고(조건 '제한적사용가능부위 : 잎※(측백엽)'), 씨앗과 가지는 '사용불가'다[1]. 제한적 사용 원료의 사용량 기준 원문과 측백엽의 별도 섭취 기준은 확인하지 못함.\n\n"
 "투존은 동물 실험에서 GABA-A 수용체를 억제해 용량에 따라 흥분과 경련을 일으키는 신경독성 성분이며, 약초와 식이를 통한 허용 섭취량은 하루 3~7 mg 정도로 추정된다[15]. 측백나무 잎 정유를 직접 분석한 중국·이란·인도·파키스탄 연구에서는 α-피넨·δ-3-카렌·세드롤이 주성분이었고 투존은 주성분으로 보고되지 않았다[4, 10, 11, 12]. 'Thuja orientalis' 가지 정유에 α-투존이 50~60% 들어 있다는 수의학 보고가 있으나, 이 연구는 β-투존·펜콘·캠퍼를 함께 측정했다[13]. 투존·펜콘이 주성분인 정유는 서양측백·Thuja plicata에서 보고되는 유형이어서[36, 37], 이 수치를 측백나무 잎에 그대로 적용하기는 어렵다[4, 13, 36]. 인도 연구는 잎 가루의 살연체 활성 성분을 투존으로 확인했다고 했으나 함량은 제시하지 않았다[14]. 측백엽의 투존 정량값과 국내 투존 기준은 확인하지 못함.\n\n"
 "국내 연구에서 서양측백 잎 정유는 증류 초기(1~10분) 분획의 투존이 67.19~71.88%였다[37]. "
 "꽃가루는 알레르기 원인이 되며, 측백나무를 포함한 측백나무과·낙우송과 7종 진단 패널에서 이탈리아 꽃가루 감작 외래 환자의 평균 18.4%가 양성이었다[24]. 약재로 쓰는 씨앗에서는 아플라톡신 오염이 보고되었다[32]. 사람이 잎을 먹었을 때의 독성 자료와 임신·수유 중 안전성은 확인하지 못함.")

C = {c["name"]: c for c in d["compounds"]}
C["Myricitrin"]["activity_ko"] = "산지별 품질 평가용 7종 동시 정량 대상[6]; 위품보다 측백나무 잎에 많아 감별 지표로 쓰임[8]"
t = C["Thujone"]
t["part"] = "보고마다 다름(가지 정유 보고·잎 가루)"
t["content_text"] = "측백나무 잎 정유 직접 분석에서는 주성분으로 보고되지 않음[4, 10, 11, 12]; 'Thuja orientalis' 가지 정유 α-투존 50~60% 보고[13]는 서양측백 등 Thuja속 정유 유형(투존·펜콘)[36]과 같아 이 종에 적용하기 어려움; 잎 가루의 살연체 활성 성분으로 확인했다는 보고(함량 없음)[14]"
t["activity_ko"] = "동물 실험에서 GABA-A 수용체 억제로 흥분·경련을 일으키는 신경독성 성분, 허용 섭취량 추정 하루 3~7 mg[15]"
t["source"] = [4, 10, 11, 12, 13, 14, 15, 36]
C["Sandaracopimaric acid"]["activity_ko"] = "잎 에틸아세테이트 추출물의 GABA-A 수용체 조절 활성의 주성분(난모세포 실험); 생쥐 복강 투여 3~30 mg/kg에서 운동량 감소[17]"

src = {s["n"]: s for s in d["sources"]}
src[1]["title"] = "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 측백나무잎·측백나무잎추출물(Thuja orientalis L. / Biota orientalis L., 제한적사용, '제한적사용가능부위 : 잎※(측백엽)') 행, 측백나무씨앗·측백나무가지(사용불가) 행"
src[31]["title"] = src[31]["title"].replace("oil extract Epiitalis", "oil extract (상표명 생략)")
src[36] = {"n": 36, "title": "Chemosystematic value of the essential oil composition of Thuja species cultivated in Poland-antimicrobial activity. Molecules 2009;14(11):4707-15 (PMID 19935470, doi:10.3390/molecules14114707) — 초록", "url": "https://pubmed.ncbi.nlm.nih.gov/19935470/", "publisher": "Molecules (PubMed)", "accessed": "2026-11-02"}
src[37] = {"n": 37, "title": "Effect of Distillation Time on the Yield and Chemical Composition of Leaf Essential Oil from Thuja occidentalis L. Plants (Basel) 2026;15(12):1885 (PMID 42357204, doi:10.3390/plants15121885) — 초록", "url": "https://pubmed.ncbi.nlm.nih.gov/42357204/", "publisher": "Plants (PubMed)", "accessed": "2026-11-02"}
for n in (2, 16, 35): src.pop(n)
# 16 사용처 제거 확인
for s in d["sections"]:
    s["body"] = s["body"].replace(" 세이지 연구에서는 물로 우린 차에 에탄올 추출의 평균 30%만큼만 투존이 녹아 나왔다[16].", "")
old = sorted(src); M = {o: i + 1 for i, o in enumerate(old)}
def rn(text):
    def f(m):
        nums = [int(x) for x in re.split(r"\s*,\s*", m.group(1))]
        return "[" + ", ".join(str(M[x]) for x in nums) + "]"
    return re.sub(r"\[(\d+(?:\s*,\s*\d+)*)\]", f, text)
for s in d["sections"]: s["body"] = rn(s["body"])
for arr in ("compounds", "assays"):
    for x in d[arr]:
        x["source"] = [M[n] for n in x["source"]]
        for f in ("content_text", "activity_ko", "content", "rationale"):
            if x.get(f): x[f] = rn(x[f])
d["sources"] = []
for o in old:
    s = src[o]; s["n"] = M[o]; d["sources"].append(s)
P.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
print(M)
