import json, sys
p = '/home/user/hfoodguide-wave3/docs/materials/canarium-album/dossier.json'
d = json.load(open(p, encoding='utf-8'))
changes = []
def rep(where, obj, key, old, new, why):
    s = obj[key]
    assert s.count(old) == 1, (where, old)
    obj[key] = s.replace(old, new)
    changes.append({"where": where, "before": old, "after": new, "why": why})
S = {s['key']: s for s in d['sections']}
rep("sections.overview", S['overview'], 'body',
    "신선한 열매 100 g에 페놀 화합물이 1174.0–1799.6 mg 들어 있다고 보고되었다[3, 8]",
    "10개 품종의 신선한 열매 100 g에 총페놀이 갈산 당량으로 1174.0–1799.6 mg 들어 있다고 보고되었다[8]",
    "[8] 초록 값은 개별 페놀 합이 아니라 총페놀(mg GAE/100 g FW)이며 10품종 범위임. [3] 종설에는 이 수치가 없음")
rep("sections.biology", S['biology'], 'body',
    "감람나무는 감람과 Canarium속의 늘푸른 큰키나무로, 키가 약 7–25 m, 큰 것은 약 35 m까지 자란다고 WebSearch 요약으로만 확인했다[35]. 같은 요약에 따르면 꽃은 4–5월에 피고 열매는 10–12월에 익으며, 열매는 길이 25–35 mm의 달걀꼴 또는 방추형 핵과다[35]. ",
    "감람나무는 감람과(Burseraceae) Canarium속의 과일나무다[3, 4]. 나무 키·꽃 피는 시기·열매 크기 같은 형태 정보는 식물지 원문을 열지 못해 확인하지 못함. ",
    "[35] World Flora Database 는 2차 DB이고 페이지를 열지 못한 채 WebSearch 요약에만 기댄 값이라 삭제. efloras(Flora of China)는 이 환경 네트워크 밖")
rep("sections.cultivation", S['cultivation'], 'body',
    "광둥·광시·윈난과 대만에서도 재배하고",
    "광둥·광시·윈난[5]과 대만[4]에서도 재배하고",
    "지역별 근거 분리: 광둥·광시·윈난은 [5] 서론, 대만은 [4] 서론에만 있음([3]에는 푸젠만)")
rep("sections.cultivation", S['cultivation'], 'body',
    "과실이 강한 햇볕에 데는 일소 피해도 품질을 떨어뜨리는 주요 환경 스트레스로 꼽힌다[19].",
    "과실이 강한 햇볕에 데는 일소 피해도 열매 발달과 품질을 떨어뜨리는 주요 환경 스트레스로 꼽힌다[36].",
    "[19](수확 시기·저온 저장)에는 일소 내용이 없음. 일소 연구(PMID 39273853)로 출처 교체")
rep("sections.processing", S['processing'], 'body',
    "페놀 추출에는 70% 에탄올, 초음파·마이크로파를 함께 쓰는 방법이 쓰였다[5, 9]. 열매 페놀은 가수분해형 탄닌이 많아 말리거나 가열하는 동안 갈산·엘라그산 같은 단순 페놀산으로 분해될 수 있다고 가자 연구가 보고했다[6].",
    "페놀 추출에는 70% 에탄올, 초음파·마이크로파를 함께 쓰는 방법이 쓰였다[5, 9, 35]. 다만 가수분해형 탄닌이 햇볕 건조·가열 중 케불산·갈산·엘라그산으로 분해된다는 결과는 가자(Chebulae Fructus, Terminalia chebula) 열매에서 얻은 것이며, 감람 열매에서 같은 변화를 직접 잰 자료는 확인하지 못함[6].",
    "[6]의 건조 분해 실험은 가자 생과로만 수행됨 — 감람 열매 결과처럼 읽히던 문장을 종 구분해 고침. 마이크로파 70% 에탄올 추출 원 논문 [35] 추가")
rep("sections.related_species", S['related_species'], 'body',
    "가자(Chebulae Fructus)의 혼입품 연구에서도",
    "가자(Chebulae Fructus)의 혼입품 연구에서도 약재 시장에서 산 청과 3배치가",
    "[6] 시료 출처(약재 시장 구입 3배치) 명시")
rep("sections.related_species", S['related_species'], 'body',
    "청과가 대상에 포함되었고, 12가지",
    "분석되었고, 12가지",
    "위 수정과 이어짐")
rep("sections.safety", S['safety'], 'body',
    "16 g/kg에서는 체중 증가 둔화와 혈청 AST·빌리루빈 상승이 나타났다[30].",
    "16 g/kg에서는 체중 증가 둔화, 정세관 정자 수 감소, 혈청 AST·빌리루빈 상승이 나타났다[30].",
    "[30] 초록의 16 g/kg 소견 중 정자 수 감소가 빠져 있었음")
C = {c['name']: c for c in d['compounds']}
rep("compounds.Gallic acid.activity_ko", C['Gallic acid'], 'activity_ko',
    "마이크로파 추출물의 주성분으로 확인[3]",
    "70% 에탄올 마이크로파 추출물의 주된 페놀로 동정[35]",
    "[3] 종설에는 마이크로파 추출 내용이 없음. 원 논문(PMID 21246434)으로 교체")
C['Gallic acid']['source'] = [3, 4, 5, 7, 9, 35]
rep("compounds.Scopoletin.activity_ko", C['Scopoletin'], 'activity_ko',
    "MDCK 세포에서 A형 인플루엔자 억제(IC50 22.9 ± 3.7 μg/mL)[3, 24]",
    "A형 인플루엔자(H1N1, H274Y 변이주) 억제 IC50 22.9 ± 3.7 μg/mL(세포 실험)[3, 24]",
    "스코폴레틴 시험에 MDCK 세포를 썼다는 기술은 [24] 초록·[3]에 없음(MDCK는 이소코릴라긴 CPE 실험). 변이주는 [3]")
rep("compounds.Ellagic acid.activity_ko", C['Ellagic acid'], 'activity_ko',
    "쥐 간세포·생쥐 CCl4 간 손상 모델에서 간 보호 작용[27]",
    "감람·Euphorbia nematocypha 추출물에서 분리한 성분으로, 쥐 배양 간세포와 생쥐 CCl4 간 손상 모델에서 간 보호 작용[27]; 종설은 감람 성분으로 소개[3]",
    "[27]은 두 식물을 함께 다뤄 초록에 성분별 유래 식물 구분이 없음 — 다른 종 자료 섞임 가능성 명시")
C['Ellagic acid']['source'] = [3, 4, 9, 27]
rep("compounds.Hyperoside.content_text", C['Hyperoside'], 'content_text',
    "열매에서 분리(함량 확인하지 못함)[27]",
    "감람에서 분리된 플라보노이드로 소개됨[3]; 감람·Euphorbia nematocypha 공동 연구에서 간세포 보호 성분으로 분리(유래 식물 구분은 초록에 없음)[27]",
    "[27] 초록에는 열매 부위도, 어느 식물에서 나온 성분인지도 없음")
rep("compounds.Hyperoside.activity_ko", C['Hyperoside'], 'activity_ko',
    "간세포 보호(항산화) 성분으로 분리[27]",
    "쥐 배양 간세포 보호(항산화) 시험 성분[27]",
    "세포 시험임을 명시")
rep("compounds.Geraniin.activity_ko", C['Geraniin'], 'activity_ko',
    "떫은맛을 내는 가수분해형 탄닌의 하나[3, 8]",
    "가수분해형 탄닌의 하나로, 이 계열이 열매의 떫은맛을 낸다[17]",
    "[3]·[8]에는 게라닌·떫은맛 관계 기술이 없음. 가수분해형 탄닌과 떫은맛은 [17]")
C['Geraniin']['source'] = [5, 8, 17]
rep("compounds.Chebulagic acid.activity_ko", C['Chebulagic acid'], 'activity_ko',
    "가열·건조 중 코릴라긴·케불산·엘라그산으로 분해될 수 있음(가자 연구)[6]",
    "가자(Chebulae Fructus) 열매의 햇볕 건조·60 °C 가열 시험에서 코릴라긴·케불산·엘라그산 등으로 분해(감람 열매 자료 아님)[6]",
    "종 구분 명시")
rep("compounds.Chebulagic acid.content_text", C['Chebulagic acid'], 'content_text',
    "청과(Canarii Fructus) 3배치에서 검출",
    "약재 시장에서 산 청과(Canarii Fructus) 3배치에서 검출",
    "[6] 시료 출처")
for n in d['nutrients']:
    if n['form'] == "씨알맹이(kernel, 신선)":
        changes.append({"where": "nutrients[0].form", "before": n['form'], "after": "씨알맹이(kernel)", "why": "[3] 표 1 머리말은 'kernel'뿐이고 수분 5.2 g이라 '신선' 기준으로 단정할 수 없음"})
        n['form'] = "씨알맹이(kernel)"
A = d['assays']
rep("assays[0].conditions.detection", A[0]['conditions'], 'detection',
    "200–600 nm UV-Vis 스펙트럼 기록",
    "UV-Vis 흡수 스펙트럼을 200 nm와 600 nm에서 기록(원문 표기)",
    "[4] Methods 원문은 'recorded on-line at 200 and 600 nm'")
rep("assays[1].part", A[1], 'part',
    "시장 구입 건조 열매 3배치",
    "약재 시장 구입 3배치",
    "[6] 원문에 건조 여부 기술 없음(약재 시장 구입만 명시)")
rep("assays[2].rationale", A[2], 'rationale',
    "초록에 적힌 조건은 C18",
    "초록에 적힌 스코폴레틴·스코파론 조건은 C18",
    "[7] 초록의 HPLC 조건은 두 쿠마린용이고 갈산은 약전 오배자 시험법으로 따로 정량")
# sources
src = {s['n']: s for s in d['sources']}
old35 = src[35]
src[35] = {"n": 35, "title": "Microwave-assisted extraction of phenolics from Canarium album L. and identification of the main phenolic compound. Nat Prod Res 2011;25(2):85-92 (PMID 21246434; 초록만 확인)", "url": "https://doi.org/10.1080/14786410701592778", "publisher": "PubMed (National Library of Medicine)", "accessed": "2026-11-02"}
src[36] = {"n": 36, "title": "Transcriptomic and Metabolomic Analysis Reveals the Potential Roles of Polyphenols and Flavonoids in Response to Sunburn Stress in Chinese Olive (Canarium album). Plants (Basel) 2024;13(17):2369 (PMID 39273853; 초록만 확인)", "url": "https://doi.org/10.3390/plants13172369", "publisher": "PubMed (National Library of Medicine)", "accessed": "2026-11-02"}
changes.append({"where": "sources[35]", "before": old35['title'], "after": src[35]['title'], "why": "열지 못한 2차 DB 삭제, 번호 35는 새 1차 논문에 배정"})
changes.append({"where": "sources[36]", "before": "", "after": src[36]['title'], "why": "일소 문장 출처 추가"})
d['sources'] = [src[k] for k in sorted(src)]
json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(changes, open('/home/user/hfoodguide-wave3/docs/materials/canarium-album/_review/changes.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(changes))
