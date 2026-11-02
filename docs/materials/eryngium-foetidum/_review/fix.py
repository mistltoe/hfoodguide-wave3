import json,sys
p=sys.argv[1]
d=json.load(open(p))
sec={s['key']:s for s in d['sections']}
changes=[]
def rep(where,obj,key,old,new,why):
    assert old in obj[key], (where,old)
    obj[key]=obj[key].replace(old,new)
    changes.append({"where":where,"before":old,"after":new,"why":why})
rep("sections.overview",sec['overview'],'body',
 "남유럽 따뜻한 지역에도 퍼져 있다[2, 33]","남유럽 따뜻한 지역에도 퍼져 있다[4, 33]",
 "[2] 초록에는 원산지·분포 서술이 없음; [4]는 중앙아메리카·서인도제도 원산, [33]은 원산과 아시아·열대 아프리카·태평양 섬·남유럽 분포를 그대로 씀")
rep("sections.overview",sec['overview'],'body',
 "이 종은 건강기능식품 고시형 원료의 원재료로는 올라 있지 않다[1].","이 종이 건강기능식품 고시형 원료의 원재료로 올라 있는지는 확인하지 못함.",
 "[1]은 식품원료 목록(I1020)이라 건강기능식품 고시 여부를 뒷받침하지 않음; 로컬 고시 자료에서 확인 불가")
rep("sections.history",sec['history'],'body',
 "이런 전통 용도는 대부분 임상으로 확인되지 않아 추가 연구가 필요하다고 정리되어 있다[3].","총설은 이런 전통 용도의 효과를 확인하려면 추가 연구가 필요하다고 정리했다[3].",
 "[3] 결론은 효과 확인을 위한 추가 연구 필요만 말하고 '임상으로 확인되지 않음'을 판단하지 않음")
rep("sections.biology",sec['biology'],'body',
 "4시간 수증기 증류한","4시간 물 증류(hydrodistillation)한",
 "[4] 방법: Clevenger 장치 hydrodistillation(물 증류), 수증기 증류 아님")
rep("sections.biology",sec['biology'],'body',
 "잎 정유의 (E)-2-도데세날 비율은 연구마다 14.3–50.62%로 차이가 커서 산지에 따른 변이가 크다[2, 3].",
 "잎 정유의 (E)-2-도데세날 비율은 2011–2021년 연구를 모은 총설에서 14.3–50.62%였고, 쿠바산 5.7%부터 피지산 63.5%까지 보고되어 산지에 따른 변이가 크다[2, 3, 4, 6].",
 "본문 다른 곳의 피지산 63.5%[6]와 범위가 어긋남; [3]의 범위는 총설 대상 연구 한정이고 [4]는 쿠바 5.7%를 인용")
rep("sections.cultivation",sec['cultivation'],'body',
 "가뭄 뒤 다시 물을 주면 에린지알 생산이 늘었고, 카르니틴을 뿌린 재급수 식물에서 더 늘었다[18].",
 "가뭄과 재급수 처리 모두 에린지알 생산을 늘렸고, 재급수 식물에 카르니틴을 뿌리면 더 늘었다[18].",
 "[18] 초록: 'Drought and re-watering improved the production of eryngial' — 가뭄 자체도 증가 요인")
rep("sections.genetics",sec['genetics'],'body',
 "인도 동해안의 두 유전형을 비교한 DNA 바코드 연구에서 엽록체 유전자 하나는 두 유전형을 구분했지만 나머지는 모두 쿨란트로로 동정했고,",
 "인도 동해안의 에린기움 두 유전형을 비교한 DNA 바코드 연구에서 나머지 바코드 구간은 두 시료를 모두 쿨란트로로 동정했지만 엽록체 유전자 하나는 두 시료를 서로 다른 종에 가깝게 나눠, 두 시료가 모두 쿨란트로인지는 이 연구만으로 확정되지 않는다;",
 "[16] 전문: 구분에 성공한 엽록체 유전자는 두 시료를 '서로 다른 두 종'으로 나눔 — 다른 종 섞임 가능성을 밝혀 둠")
for c in d['compounds']:
    if c['name']=='Lutein':
        old=c['activity_ko']
        c['activity_ko']="루테인·베타카로틴 등이 혼합 미셀에 실린 잎 소화 분획이 Caco-2 세포의 IL-8·MCP-1을 33% 낮춤(세포 실험, 루테인 단독 효과는 확인되지 않음)[10]"
        changes.append({"where":"compounds[Lutein].activity_ko","before":old,"after":c['activity_ko'],"why":"[10]은 소화 분획 전체의 효과로 보고했으며 루테인 단독 작용이 아님(세포 결과 과장 방지)"})
for a in d['assays']:
    if a['source']==[2,4]:
        old=a['conditions']['sample_prep']
        a['conditions']['sample_prep']=old.replace("4시간 수증기 증류(영국약전)","4시간 물 증류(hydrodistillation, 영국약전)")
        assert old!=a['conditions']['sample_prep']
        changes.append({"where":"assays[1].conditions.sample_prep","before":old,"after":a['conditions']['sample_prep'],"why":"[4] Methods: hydrodistillation"})
        old=a['rationale']
        a['rationale']=old.replace("잎 정유에서 가장 많이 보고되는 성분이라 잎·줄기 품질 지표로 쓰인다","잎 정유에서 가장 많이 보고되는 성분이라 잎 품질 지표로 쓸 만하다(줄기 정유에서는 세 번째 성분)")
        assert old!=a['rationale']
        changes.append({"where":"assays[1].rationale","before":old,"after":a['rationale'],"why":"지표로 '쓰인다'는 출처 근거 없음; [4]에서 줄기 정유 주성분은 도데칸알"})
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open(p.replace('dossier.json','_review/changes.json'),'w'),ensure_ascii=False,indent=1)
print(len(changes))
