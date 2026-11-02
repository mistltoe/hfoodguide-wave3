import json, re
from pathlib import Path
P = Path(__file__).resolve().parent.parent / "dossier.json"
d = json.loads(P.read_text())
changes = []
def sec(k):
    return next(s for s in d["sections"] if s["key"] == k)
def rep(k, old, new, why):
    s = sec(k)
    assert old in s["body"], (k, old)
    s["body"] = s["body"].replace(old, new)
    changes.append({"where": f"sections.{k}", "before": old, "after": new, "why": why})

rep("overview", "두해살이풀로, 동아시아에 분포한다[1, 9].", "두해살이풀로, 동아시아에 분포한다[9].",
    "[1](식약처 목록 행)에는 과·생활형·분포 정보가 없음; [9] 초록이 'biennial plant distributed in East Asia'라고 씀")
rep("history", "검색 요약으로만 확인한 한 국내 연구에 따르면 한국은 蛇床子를 벌사상자 또는 사상자의 열매로 규정하고 중국·일본은 벌사상자만 인정한다고 하나, 원문은 확인하지 못함[34].",
    "한국·중국·일본의 공정서가 蛇床子의 기원 식물을 각각 어떻게 규정하는지는 원문으로 확인하지 못함.",
    "[34]는 WebSearch 요약만 있고 원문(koreascience)을 열 수 없어 근거로 쓸 수 없음 — 출처 삭제")
rep("biology", "사상자는 국내에서 흰가루병균(Erysiphe heraclei)의 기주 식물 가운데 하나로 기록되어 있다[35].",
    "한 식물병 보고는 흰가루병균(Erysiphe heraclei)이 중국·일본·한국에서 당귀속·당근속 식물, 사상자 등 여러 초본에 발생한다고 적었다[35].",
    "[35] 초록은 국내에 한정하지 않고 'in China, Japan, and Korea' 기주로 언급")
rep("related_species", "한 2026년 연구는 사상자 추출물 성분으로 오스톨·임페라토린·베르갑텐 같은 쿠마린을 인용했으나, 그 연구에서 이 성분들을 정량하지는 않았다[7].",
    "한 2026년 연구는 사상자 추출물 성분으로 오스톨·임페라토린·베르갑텐 같은 쿠마린을 인용했으나, 그 연구에서 이 성분들을 정량하지는 않았다[7]. 이 쿠마린들은 벌사상자 열매(Cnidii Fructus)의 주요 성분으로 정리된 것들이어서[34], 사상자 열매에서 직접 정량한 근거 없이 사상자 성분으로 옮겨 쓰면 안 된다(이 자료들에서는 그런 정량 근거를 확인하지 못함).",
    "벌사상자 자료 섞임 가능성 명시 — 오스톨·임페라토린·베르갑텐은 Cnidium monnieri 열매 총설(PMID 38507853)의 주성분")
rep("related_species", "같은 연구진의 앞선 연구는 토릴린과 오스톨을 HPLC 기준물질로 썼다[6].",
    "같은 연구진의 앞선 연구는 토릴린과 오스톨을 HPLC 기준물질로 썼으나, 함량을 고정한 것은 토릴린뿐이었다[6].",
    "[6] 전문: 'the torilin content was fixed (standard), while the osthol content was not'")
rep("genetics", "같은 속의 T. scabra 엽록체 유전체는 157,855 bp이며, 큰 단일복사 영역 85,362 bp, 작은 단일복사 영역 17,993 bp, 역위반복 영역 27,250 bp 한 쌍으로 이루어졌다[26]. 이 유전체에서는 단백질 암호 유전자 82개, tRNA 유전자 37개, rRNA 유전자 8개 등 모두 127개 유전자가 예측되었다[26].",
    "같은 속의 다른 종 T. scabra는 엽록체 유전체(157,855 bp, 예측 유전자 127개)가 해독되어 있으나, 이는 사상자 자료가 아니다[26].",
    "근연종(T. scabra) 세부 수치가 사상자 유전 정보처럼 읽힐 수 있어 한 문장으로 줄이고 다른 종임을 명시(수치는 [26]과 일치)")
rep("genetics", "벌사상자와의 구별에 관해서는 ITS 영역 염기서열 유사도가 85%에 그쳤다는 국내 연구가 있다고 검색 요약에 나오지만, 원문 수치는 확인하지 못함[34]. 같은 요약에 따르면 사상자 열매는 갈고리 모양 가시가 촘촘하고, 벌사상자 열매는 분과 뒷면에 얇은 세로 모서리가 있어 형태로도 구별된다[34].",
    "벌사상자와 사상자를 유전자·형태로 구별하는 기준(ITS 염기서열 차이, 열매 형질)은 원문을 열람한 출처로 확인하지 못함.",
    "[34]는 WebSearch 요약뿐(원문 미열람) — ITS 85%·형태 형질 수치를 근거 없이 둘 수 없어 삭제")
rep("safety", "열매 이외 부위는 식품원료로 쓸 수 없고, 이 목록 행에는 사용량 한도가 적혀 있지 않다[1].",
    "목록에 오른 사용 부위는 열매뿐이고(다섯 행 모두 부위 '열매'), 이 목록 행에는 사용량 한도나 식품 유형 제한이 적혀 있지 않다[1].",
    "로컬 I1020 원자료 대조: 다섯 행 모두 REGN_CD_NM '열매', USE_CND_STDR_CN '제한적사용가능부위 : 열매※(사상자)' — 원문에 없는 '쓸 수 없다' 단정 대신 원자료 표현으로")
rep("safety", "쥐 연구에서 50% 에탄올 추출물 1,000 mg/kg를 한 번 먹였을 때 24시간 안에 이상 반응은 없었지만,",
    "자연발생 고혈압 쥐(군당 4마리)에 50% 에탄올 추출물 1,000 mg/kg를 한 번 먹인 실험에서 투여 중·24시간 안에 이상 반응은 관찰되지 않았지만(독성 시험은 아님),",
    "[5] 전문: SHR 24마리를 6군(군당 4마리)으로 나눈 혈압 실험의 부수 관찰이며 독성 시험이 아님")
rep("safety", "같은 연구가 체표면적으로 환산한 사람 상당량은 60 kg 성인 기준 약 9.73 g이었으나, 사람에서 효과와 안전성은 검증되지 않았다[5].",
    "같은 연구는 쥐에서 혈압을 낮춘 용량을 체표면적으로 환산해 사람 상당량을 162.16 mg/kg, 60 kg 성인 기준 추출물 약 9.73 g으로 계산했으나, 이는 안전 용량이 아니며 사람에서 효과와 안전성은 검증되지 않았다[5].",
    "[5] 전문: HED 162.16 mg/kg → 60 kg 약 9.73 g은 '효과 용량' 환산값(추출물 기준)")
rep("safety", "세포 실험에서는 추출물이 150 μg/mL까지 피부세포 독성을 보이지 않았고[6],",
    "세포 실험에서는 열수 추출물이 시험한 최고 농도인 150 μg/mL까지 피부세포 독성을 보이지 않았고[6],",
    "[6] 전문: MTT 시험 농도 범위 50–150 μg/mL — 150 은 상한일 뿐")
rep("safety", "기생충 실험에서는 625 ng/mL를 넘으면 숙주세포 독성이 나타났다[29].",
    "원충 배양 실험에서는 알코올 추출물이 625 ng/mL를 넘으면 숙주세포(말 피부세포) 독성이 나타났다[29].",
    "[29] 초록: alcohol extracts, equine dermal cells, 'exceeded 625 ng/ml'")

# compounds
for c in d["compounds"]:
    if c["name"] == "Torilin":
        old = c["activity_ko"]
        c["activity_ko"] = old.replace("쥐 대동맥 이완 EC50 210 ± 1.07 μM(적출 혈관)", "흰쥐 적출 흉부대동맥 이완 EC50 210 ± 1.07 μM(적출 혈관)").replace("혈관신생 억제(병아리 배·쥐 매트리겔)", "혈관신생 억제(병아리 배·생쥐 매트리겔)")
        changes.append({"where": "compounds.Torilin.activity_ko", "before": old, "after": c["activity_ko"], "why": "[5] SD 흰쥐 흉부대동맥, [21] mouse Matrigel plug — 동물 종 명확히"})
    if c["name"] == "Deangeloyloxytorilin":
        old = c["activity_ko"]
        c["activity_ko"] = "사상자 열매에서 이 성분이 분리된 첫 보고인 구아이안형 세스퀴테르펜[13]"
        changes.append({"where": "compounds.Deangeloyloxytorilin.activity_ko", "before": old, "after": c["activity_ko"], "why": "[13] 초록: 'first report showing that this compound can be isolated from Torilis japonica' — 신규 화합물이 아님"})

# sources
S = {s["n"]: s for s in d["sources"]}
old = S[30]["title"]
S[30]["title"] = "Antiproliferative constituents in Umbelliferae plants II. Screening for polyacetylenes in some Umbelliferae plants, and isolation of panaxynol and falcarindiol from the root of Heracleum moellendorffii. Biol Pharm Bull 1998;21(3):257-261 (PMID 9556156, doi:10.1248/bpb.21.257; 초록만 확인)"
changes.append({"where": "sources[30].title", "before": old, "after": S[30]["title"], "why": "PubMed 서지와 맞춰 제목 전체로"})
old = S[33]["title"]
S[33]["title"] = "Torilis japonica extract-generated intracellular ROS induces apoptosis by reducing the mitochondrial membrane potential via regulation of the AMPK-p38 MAPK signaling pathway in HCT116 colon cancer. Int J Oncol 2016;49(3):1088-1098 (PMID 27314881, doi:10.3892/ijo.2016.3578; 초록만 확인)"
changes.append({"where": "sources[33].title", "before": old, "after": S[33]["title"], "why": "생략부호(...)로 잘린 제목을 PubMed 서지로 복원"})
old = json.dumps(S[34], ensure_ascii=False)
S[34].update({"title": "Cnidii Fructus: A traditional Chinese medicine herb and source of antiosteoporotic drugs. Phytomedicine 2024;128:155375 (PMID 38507853, doi:10.1016/j.phymed.2024.155375; 벌사상자(Cnidium monnieri) 열매 총설, 초록만 확인)",
    "url": "https://pubmed.ncbi.nlm.nih.gov/38507853/", "publisher": "Elsevier / PubMed", "accessed": "2026-11-02"})
changes.append({"where": "sources[34]", "before": old, "after": json.dumps(S[34], ensure_ascii=False), "why": "WebSearch 요약뿐인 출처(원문 미열람) 삭제, 같은 번호에 벌사상자 쿠마린 근거 총설을 새로 넣음"})

P.write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n")
json.dump(changes, open(Path(__file__).parent / "changes.json", "w"), ensure_ascii=False, indent=1)
print(len(changes))
