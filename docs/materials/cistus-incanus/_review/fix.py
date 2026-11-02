import json,sys
p='/home/user/hfoodguide-wave3/docs/materials/cistus-incanus/dossier.json'
d=json.load(open(p))
S={s['key']:s for s in d['sections']}
changes=[]
def rep(key,old,new,why):
    b=S[key]['body']
    assert b.count(old)==1,(key,old)
    S[key]['body']=b.replace(old,new); changes.append({"where":f"sections.{key}","before":old,"after":new,"why":why})
rep('overview','원산지는 튀르키예·알바니아·그리스가 많다[4, 8].','원산지는 튀르키예·알바니아·그리스가 많다[4].','[8] 초록은 원산지를 말하지 않음')
rep('overview','시험관·동물 연구에서 항산화·항균·항바이러스 작용이 보고되었으나, 사람 연구는 소규모 시험 몇 건뿐이다[5, 11, 12, 14].','시험관·동물 연구에서 항산화·항균·항바이러스 작용이 보고되었으나[4, 12, 13, 14], 사람 연구는 소규모 시험 몇 건뿐이다[5, 11].','[12]·[14]는 세포 연구라 사람 연구 근거로 붙이면 과장; 근거 분리')
rep('history','락로즈 허브차는 예부터 지중해 지역 전통 의학에서 두루 쓰는 약으로 쓰였다고 정리되어 있다[6].','락로즈 허브차는 예부터 전통 의학에서 두루 쓰는 약으로 쓰였다고 정리되어 있다[6].','[6] 초록은 지역을 특정하지 않음(general remedy in traditional medicine since ancient times)')
rep('history','2000년대 독일에서는 잎 추출물의 항인플루엔자 작용을 세포와 생쥐에서 시험했고','2000년대 독일에서는 특정 품종 원료로 만든 폴리페놀 추출물의 항인플루엔자 작용을 세포와 생쥐(에어로졸 투여)에서 시험했고','[12]·[13] 초록은 \'잎\' 추출물이라 하지 않고 [13]은 special variety·에어로졸 투여로 적음')
rep('history','이후 유럽연합 신규식품 목록에는 특정 계통의 건조·절단 지상부가 올랐다고 WebSearch 요약으로만 확인했다[21].','유럽연합 신규식품 목록에는 체코 당국이 옛 신규식품 규정(EC 258/97)에 따라 승인한 특정 제품의 건조·절단 지상부 항목이 있고, 2022년 정정 규정은 그 규격에 빠진 원료 설명을 바로잡은 것이라고 WebSearch 요약으로만 확인했다[21].','검토자 WebSearch: 2022/202 는 신규 등재가 아니라 2017/2470 목록 규격 정정(체코 당국 258/97 승인 품목)')
rep('biology','실험실에서 기른 락로즈 털뿌리는','실험실에서 기른 락로즈 모상근(hairy root) 배양체는','hairy root 는 뿌리털이 아니라 모상근 배양체')
rep('related_species','Sage-leaved rockrose(Cistus salviifolius) 잎이 락로즈와 따로 올라 있다[1].','Sage-leaved rockrose(Cistus salviifolius) 잎이 락로즈와 따로 올라 있으며, Gum cistus의 원료명이 \'Rock rose잎\'이라 영어 이름만으로는 락로즈와 구별되지 않는다[1].','식약처 I1020 원자료 확인: Gum cistus 원료명 Rock rose잎 — 혼동 주의 근거 추가')
rep('cultivation','햇볕에 자란 잎은 그늘에 자란 잎보다 플라보노이드가 훨씬 많아, 자라는 곳의 빛 조건이 원료 품질에 영향을 준다[7].','햇볕에 자란 잎은 그늘에 자란 잎보다 플라보노이드가 훨씬 많아, 자라는 곳의 빛 조건에 따라 잎의 성분 함량이 크게 달라진다[7].','[7] 은 원료 품질을 논하지 않음 — 추론 완화')
rep('genetics','서지중해 계통 개체의 약 27%가 한 개체 안에 서로 다른 ITS 변이를 함께 지녔다[3].','염기서열을 얻은 C. creticus 개체의 약 27%가 한 개체 안에 서로 다른 ITS 변이를 함께 지녔고, 이런 변이는 주로 서지중해 계통에서 나타났다[3].','[3] 의 27% 는 서지중해 계통이 아니라 C. creticus 전체 분석 개체 기준')
rep('safety','유럽연합에서는 신규식품으로 분류되어 왔으며, 2022년 정정 규정으로 특정 계통의 건조·절단 지상부(나무질을 포함한 어린 가지)가 신규식품 목록에 올랐다고 WebSearch 요약으로만 확인했다[8, 21].','유럽연합에서는 신규식품으로 분류되어 왔으며[8], 신규식품 목록에는 체코 당국이 승인한 특정 제품의 건조·절단 지상부(나무질을 포함한 어린 가지) 항목이 있고 2022년 정정 규정이 그 규격을 바로잡았다고 WebSearch 요약으로만 확인했다[21].','2022/202 는 등재가 아니라 규격 정정; 상표성 계통명 대신 일반 표현')
rep('safety','이 연구의 이상반응 결과는 본문에서 확인하지 못함.','본문에는 이상반응에 관한 기록이 없다.','[5] PMC 전문 확인: 이상반응 항목 자체가 없음')
rep('safety','세포 실험에서 잎 추출물은 50 µg/mL에서','세포 실험에서 이 추출물은 유효 농도인 50 µg/mL에서','[12] 초록은 잎 추출물이라 하지 않음')
rep('safety','25–100 µg/mL의 높은 농도에서는 세포 안 활성산소를 오히려 늘렸다[25].','햄스터 폐 섬유아세포(V79)에 25–100 µg/mL의 높은 농도로 넣으면 세포 안 활성산소를 오히려 늘렸다[25].','[25] 세포 종류 명시')
rep('safety','새우 유생 치사 시험으로 급성 독성을 평가한 연구가 있으나 그 결과는 초록에서 확인하지 못함.','시칠리아산 동결건조 물 추출물의 급성 독성을 새우 유생(Artemia salina) 치사 시험으로 평가한 연구가 있으나 그 결과는 초록에서 확인하지 못함[17].','출처 번호 누락 — [17] 초록에서 확인')
A=d['assays']
a=A[1]; a['conditions']['standard']='시판 표준품(순도 95% 이상)과 직접 분리한 시스투신·푸니칼라진·테르플라빈 A; 1 mg/mL 원액(메탄올, 엘라그산은 DMSO)을 50% 메탄올로 20–200 µg/mL 희석'
changes.append({"where":"assays[1].conditions.standard","before":"메탄올 1 mg/mL 원액을 20–200 µg/mL로 희석","after":a['conditions']['standard'],"why":"[4] Methods: 엘라그산은 DMSO 원액, 희석 용매 50% 메탄올"})
a=A[3]; c=a['conditions']
c.update({"column":"C18 역상 칼럼(초록)","mobile_phase":"아세토니트릴–50 mM 인산완충액(pH 2.5), 기울기 용리","flow":"1 mL/min","detection":"DAD, UV 210 nm","linearity":"2–50 µg/mL(갈로카테킨·카테킨·EGCG), 5–50 µg/mL(갈산·EGC·에피카테킨·루틴)","lod":"0.24–0.74 µg/mL","loq":"0.77–1.94 µg/mL","recovery":"78.7–98.2%"})
a['rationale']='카테킨류 5종과 갈산·루틴을 함께 분리하는 검증된 방법을 락로즈·C. monspeliensis 동결건조 추출물에 적용해 갈산·갈로카테킨·카테킨·루틴을 특이 지표성분으로 정량함. 조건은 초록에 적힌 것만 옮겼고 전문(칼럼 규격·기울기 세부)은 확인 못함[10].'
changes.append({"where":"assays[3].conditions","before":"모든 칸 비움(초록 값은 rationale 에만)","after":"초록에 적힌 칼럼·이동상·유속·검출·직선성·LOD·LOQ·회수율을 칸에 옮김","why":"[10] 초록 원문 대조"})
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('/home/user/hfoodguide-wave3/docs/materials/cistus-incanus/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
