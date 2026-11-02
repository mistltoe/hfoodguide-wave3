import json,sys
p=sys.argv[1]
d=json.load(open(p))
S={s['key']:s for s in d['sections']}
changes=[]
def rep(where,obj,key,old,new,why):
    assert old in obj[key], (where,old)
    obj[key]=obj[key].replace(old,new)
    changes.append({"where":where,"before":old,"after":new,"why":why})
rep("sections.overview",S['overview'],'body',
 "한국 전통의학에서는 씨앗을 '비자(榧子)'라고 부른다[3, 5].",
 "한국 전통의학에서는 비자나무를 '비자(榧子)'라고 부른다[5].",
 "[5] 는 이 종(T. nucifera)을 '비자(榧子)'로 부른다고 썼고 씨앗에 한정하지 않음; [3] 에는 이 이름이 없음")
rep("sections.history",S['history'],'body',
 "제주 구좌읍 평대리 비자림은 천연기념물 제374호다[3]",
 "제주 평대리 비자림은 천연기념물 제374호다[3]",
 "[3] 원문은 'Pyungdae-ri, Jeju-do'까지만 적음(읍 이름 없음)")
rep("sections.history",S['history'],'body',
 "식품과 머릿기름 같은 모발 관리 제품에",
 "식품과 모발 관리 제품에",
 "[4] 원문은 'food and hair care products' — '머릿기름'은 원문에 없음")
rep("sections.related_species",S['related_species'],'body',
 "이 문서는 한국·일본에 자라는 T. nucifera 자료만 다루며, 중국의 비자 연구는 대부분 T. grandis를 대상으로 하므로 성분 수치를 그대로 옮겨 쓰지 않는다[1, 3].",
 "T. nucifera의 자연 분포는 한국과 일본에 한정되므로, 이 문서는 T. nucifera 자료만 다루고 T. grandis를 대상으로 한 연구의 성분 수치는 옮겨 쓰지 않는다[1, 3].",
 "'중국의 비자 연구는 대부분 T. grandis 대상'이라는 주장은 [1]·[3] 어디에도 없음 — [3] 이 말하는 분포 한정으로 바꿈")
rep("sections.processing",S['processing'],'body',
 "잎은 수증기 증류로 정유를 얻는데, 잎 1 kg에 물을 1:7(kg:L)로 넣고 102 °C로 가열해 딘-스타크 장치로 모았다[4].",
 "잎 정유는 물 증류(hydrodistillation)로 얻었는데, 잎 1 kg을 물과 1:7(kg:L)로 섞어 102 °C로 가열하고 딘-스타크 장치로 모았다[4].",
 "[4] Methods 는 수증기 증류(steam distillation)가 아니라 잎을 물에 담가 끓이는 hydrodistillation")
A=d['assays'][0]
rep("assays[0].part",A,'part',"잎 정유(수증기 증류)","잎 정유(물 증류, hydrodistillation)","[4] Methods: hydrodistillation")
rep("assays[0].conditions.sample_prep",A['conditions'],'sample_prep',"102 °C 가열 수증기 증류(딘-스타크 장치)","102 °C 가열 물 증류(hydrodistillation, 딘-스타크 장치)","[4] Methods: hydrodistillation")
rep("assays[0].conditions.instrument",A['conditions'],'instrument',"Agilent 7890B GC + 5977A MSD","가스크로마토그래프 + 사중극자 질량검출기(MSD)","상표명 대신 일반명")
for c in d['compounds']:
    if c['name'] in ('D-Limonene','3-Carene'):
        old=c['role']; c['role']='bioactive'
        changes.append({"where":f"compounds[{c['name']}].role","before":old,"after":"bioactive","why":"[4] 의 '화학 지표'는 잎 정유 품질 관리용이다. 식품 사용 부위(씨앗·열매)의 지표처럼 보이지 않게 marker 를 뺌"})
        o=c['activity_ko']
        c['activity_ko']=o.replace("정유 품질 관리용 화학 지표로 선정됨[4]","잎 정유 품질 관리용 화학 지표로 선정됨(식품 사용 부위인 씨앗·열매의 지표는 아님)[4]")
        changes.append({"where":f"compounds[{c['name']}].activity_ko","before":o,"after":c['activity_ko'],"why":"잎 정유 결과를 씨앗·열매 결과와 구분"})
    if c['name']=='18-Hydroxyferruginol':
        o=c['activity_ko']; c['activity_ko']="인플루엔자 H1N1 IC50 13.6 μM, H9N2 12.8 μM(감염 후 처리, 세포 실험; 선택지수 1.7–1.8로 낮음)[16]"
        changes.append({"where":"compounds[18-Hydroxyferruginol].activity_ko","before":o,"after":c['activity_ko'],"why":"[16] 전문 Results: SI 1.68·1.79 — 세포 실험 결과 과장 방지"})
    if c['name']=='18-Oxoferruginol':
        o=c['activity_ko']; c['activity_ko']="인플루엔자 H9N2 IC50 10.8 μM, H1N1 18.3 μM, H3N2 29.2 μM(감염 후 처리, 세포 실험; 선택지수 1.3–3.6)[16]"
        changes.append({"where":"compounds[18-Oxoferruginol].activity_ko","before":o,"after":c['activity_ko'],"why":"[16] 전문 Results: SI 3.6·2.13·1.33"})
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
