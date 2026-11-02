import json,sys
p='/home/user/hfoodguide-wave3/docs/materials/chrysobalanus-icaco/dossier.json'
d=json.load(open(p))
changes=[]
def rep(where,obj,key,old,new,why):
    v=obj[key]
    assert old in v,(where,old)
    obj[key]=v.replace(old,new,1)
    changes.append({"where":where,"before":old,"after":new,"why":why})
S={s['key']:s for s in d['sections']}
rep('sections.overview',S['overview'],'body','지름 약 2.5 cm 안팎의 핵과로, 익으면 짙은 붉은색에서 보라색을 띠며 품종(형태형)에 따라 흰색 열매도 있다[2, 3, 4]','지름 약 2.5 cm 안팎의 핵과로[2, 4], 익으면 짙은 붉은색에서 보라색을 띠며 품종(형태형)에 따라 흰색 열매도 있다[3, 4]','[3] 전문에는 열매 크기 수치가 없음 — 크기는 [2](25.9 mm)·[4](2.13–2.92 cm)로 한정')
rep('sections.history',S['history'],'body','오래 먹어 온 야생 과일이다[4, 10]','먹는 야생 과일이다[4, 10]','[4]·[10] 은 식용 사실만 말하고 오랜 역사(기간)는 말하지 않음')
rep('sections.history',S['history'],'body',"의약 용도로는 '그라제루(Grageru)'·'아바제루(Abageru)'라는 이름이 기록되어 있다[22]","약용 식물로서는 브라질에서 '그라제루(Grageru)'·'아바제루(Abageru)'라고도 부른다[22]",'[22] 초록 표현(popularly known in Brazil as)에 맞춤')
rep('sections.history',S['history'],'body','미국 플로리다 남부에서는 울타리용 조경수로 널리 심는다[3]','미국 플로리다 남부에서는 관상용 조경 식물로 흔히 심는다[3, 13]','[3] 전문은 ornamental plant 라고만 하고 울타리(hedge) 용도는 말하지 않음; [13] 은 가장 흔한 조경 식물 중 하나라고 씀')
rep('sections.cultivation',S['cultivation'],'body','코코플럼은 미국 플로리다 남부의 자생 조경 식물로, 묘포장에서 울타리용으로 기른다[13]','코코플럼은 미국 플로리다 남부의 자생 식물로, 그 지역에서 가장 흔한 조경 식물 중 하나이며 묘포장에서 화분으로 길러 낸다[13]','[13] 전문에 울타리 용도 언급 없음 — 원문(one of the most common landscaping plants, nursery production)으로 바꿈')
rep('sections.cultivation',S['cultivation'],'body','이 종을 대상으로 한 묘목 시비 연구에서는 완효성 비료(8N-3P-9K) 30 g을 준 뒤 11월과 3월에 15 g씩 더 준 처리가 생육을 유지하면서 질소 유출이 가장 적었다[13]','1년생 묘목 30그루를 화분에서 6개월 기른 시비 연구에서는 10월에 완효성 비료(8N-3P-9K) 30 g을 준 뒤 11월과 3월에 15 g씩 더 준 처리가, 더 많은 비료를 준 처리보다 유출 오염이 적으면서도 생육에 충분한 양분을 공급했다고 결론지었다[13]','원문은 \"더 높은 시비량에 비해\" 유출이 가장 적다고 비교 범위를 한정함(대조구 15 g 등 낮은 처리보다 적었다는 뜻이 아님); 실험 규모 추가')
rep('sections.cultivation',S['cultivation'],'body','이 열매는 생산지 토양과 기후에 따라 무기질 함량과 맛 평가가 달랐다[4]','두 산지 열매는 무기질 함량과 맛 평가가 달랐고, 연구진은 토양·기후 조건 차이를 원인으로 추정했다[4]','[4] 는 산지 차이를 관찰하고 토양·기후를 원인으로 \"제안\"했을 뿐 인과를 확인하지 않음')
rep('sections.processing',S['processing'],'body','열매 추출물의 기능 연구는 동물·세포 단계다[6, 7, 8]. 쥐에게 열매를 하루 100–400 mg/kg씩 14일 먹인 실험에서','열매와 열매 추출물의 기능 연구는 동물·세포 단계다[6, 7, 8]. 쥐(위스타 수컷)에게 열매를 하루 100–400 mg/kg씩 14일 투여한 뒤 항암제 독소루비신 15 mg/kg을 주사한 실험에서','[6]·[8] 은 추출물이 아니라 열매(fruit)를 투여했고 투여 경로는 초록에 없음 — "먹인"→"투여한", 독소루비신 용량 보충')
rep('sections.processing',S['processing'],'body','이 결과를 사람에게 그대로 적용할 수는 없다[6, 7].','세포 실험 농도(갈산 당량 10–20 μg/mL)와 쥐 투여량은 사람의 열매 섭취와 직접 비교할 수 없으며, 이 결과를 사람에게 그대로 적용할 수는 없다[6, 7].','세포·동물 결과 과장 방지 — [7] 초록 농도 기재')
rep('sections.safety',S['safety'],'body','열매를 하루 최대 400 mg/kg씩 14일 먹인 쥐 실험 초록에는','열매를 하루 최대 400 mg/kg씩 14일 투여한 쥐 실험 초록에는','[6] 초록에 투여 경로 미기재')
rep('sections.safety',S['safety'],'body','잎 물 추출물은 쥐에 2000 mg/kg 한 번 먹였을 때','잎 물 추출물은 생쥐에 2000 mg/kg 한 번 먹였을 때','[14] MeSH·본문 동물은 생쥐(Mice)이지 쥐(rat)가 아님')
rep('sections.safety',S['safety'],'body','일부 골격 변화가 관찰되었다[15]','일부 골격 변화와 낮은 수준의 전신 독성이 관찰되었다[15]','[15] 초록 결론(it also caused low systemic toxicity) 반영')
C={c['name']:c for c in d['compounds']}
rep('compounds.Cyanidin.activity_ko',C['Cyanidin'],'activity_ko','열매 색소, 항산화 성분[5, 7]','열매 색소[5]; 열매 안토시아닌 혼합물로서 세포 실험 항염 활성[7]','[5] 초록은 항산화를 말하지 않음; [7] 은 혼합 추출물 결과')
rep('compounds.Myricitrin.activity_ko',C['Myricitrin'],'activity_ko','잎 추출물 쥐 실험의 항산화 성분 후보','잎 추출물 생쥐(고지방식) 실험의 항산화 성분 후보','[20] 은 C57BL/6J 생쥐 실험')
rep('compounds.Pomolic acid.content_text',C['Pomolic acid'],'content_text','잎에서 베툴린산·올레아놀산과 함께 분리[21]','C. icaco 잎과 근연종 Licania tomentosa 잎·열매에서 베툴린산·올레아놀산과 함께 분리됨 — 어느 성분이 어느 종에서 나왔는지 초록에 구분 없음[21]','[21] 은 두 종 시료를 함께 분획함 — 근연종 자료 섞임 표시')
rep('compounds.Pomolic acid.activity_ko',C['Pomolic acid'],'activity_ko','백혈병 세포주 증식 억제·세포자멸 유도(세포 실험)[21]','분리 트리테르펜들이 백혈병 세포주(K562·다제내성 Lucena 1) 증식 억제·세포자멸 유도(세포 실험)[21]','세포 실험 범위 명시')
A=d['assays']
rep('assays[2].compound_ko',A[2],'compound_ko','폴리페놀(안토시아닌 등)·19개 원소','폴리페놀·19개 원소','[6] 초록은 폴리페놀 종류(안토시아닌)를 특정하지 않음')
src={s['n']:s for s in d['sources']}
def st(n,old,new,why): rep(f'sources[{n}].title',src[n],'title',old,new,why)
st(2,'PLoS One 2026 (','PLoS One 2026;21(5):e0348628 (','권·호 보충')
st(4,'Heliyon 2023;9(9):e20291','Heliyon 2023;9(10):e20291','PubMed 서지: 9권 10호')
st(4,'전문 확인, 표 수치는 받지 못함','전문 확인, 표 수치는 받지 못함','-') if False else None
st(8,'Food Res Int (2017년 12월 온라인)','Food Res Int 2018;105:996-1002','PubMed 서지 권·쪽 보충')
st(10,'J Integr Med 2020 (','J Integr Med 2021;19(1):13-19 (','PubMed 서지 권·호·쪽 보충(2020년 온라인)')
st(13,'PMC9959769, 초록 확인','PMC9959769, 전문 확인','V2 가 전문 대조')
st(14,'Regul Toxicol Pharmacol 2020 (','Regul Toxicol Pharmacol 2020;113:104643 (','권 보충')
st(15,'Curr Issues Mol Biol 2023;45(9) (','Curr Issues Mol Biol 2023;45(9):7617-7629 (','쪽 보충')
st(18,'Br J Nutr 2026 (','Br J Nutr 2026;135(12):1283-1294 (','권·호·쪽 보충')
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('/home/user/hfoodguide-wave3/docs/materials/chrysobalanus-icaco/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
