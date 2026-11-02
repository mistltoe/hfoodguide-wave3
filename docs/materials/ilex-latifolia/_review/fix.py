import json,sys
p='/home/user/hfoodguide-wave3/docs/materials/ilex-latifolia/dossier.json'
d=json.load(open(p))
changes=[]
def sec(key,old,new,why):
    for s in d['sections']:
        if s['key']==key:
            assert old in s['body'],(key,old)
            s['body']=s['body'].replace(old,new); changes.append({"where":"sections."+key,"before":old,"after":new,"why":why}); return
    raise SystemExit(key)
def comp(name,field,new,why):
    for c in d['compounds']:
        if c['name']==name:
            old=c[field]; c[field]=new; changes.append({"where":f"compounds[{name}].{field}","before":old,"after":new,"why":why}); return
    raise SystemExit(name)

sec('overview',"고정차라는 이름은 여러 과·속의 약 12종 식물에 함께 쓰이므로",
 "고정차라는 이름은 여러 과·속의 약 12종(리뷰에 따라 20종 가까이) 식물에 함께 쓰이므로",
 "[4]는 약 12종, [3]은 'nearly 20 plants'라고 씀 — 두 값을 함께 적음")
sec('overview',"잎에는 디카페오일퀸산(이소클로로겐산류)·루틴 같은 폴리페놀과 라티폴로사이드·쿠디노사이드 같은 우르산형 트리테르펜 사포닌이 많다고 보고되었다[7][9][10].",
 "잎에는 디카페오일퀸산(이소클로로겐산류)·루틴 같은 폴리페놀과 라티폴로사이드 같은 우르산형 트리테르펜 사포닌이 들어 있다고 보고되었고[7][9][10], 유전체 논문은 다라 잎의 오환식 트리테르펜 사포닌이 가까운 종보다 많다고 보았다[5].",
 "[7][9][10]에는 쿠디노사이드·'많다'는 내용이 없음(쿠디노사이드는 나무껍질[12] 등); 사포닌이 많다는 비교는 [5] 본문")
sec('related_species',"소엽 고정차의 원료인 Ligustrum 속 식물 가운데 여정실(당광나무 열매)과 광나무 열매는 「식품원료 목록」에서 사용불가이다[2].",
 "소엽 고정차는 물푸레나무과 Ligustrum 속 식물에서 나오며[4], 같은 속의 당광나무(L. lucidum) 열매(여정실·당광나무열매)와 광나무(L. japonicum) 열매는 「식품원료 목록」에서 사용불가이다[2].",
 "당광나무·광나무 열매를 소엽 고정차 원료로 읽히게 쓴 문장 — I1020 원자료는 열매 행만 있고 소엽 고정차 원료 종은 [4]가 Ligustrum 속으로만 씀")
sec('biology',"잎 트리테르펜 가운데 일부는 간세포의 중성지방 축적을 억제하거나",
 "잎 트리테르펜 가운데 일부는 간암 유래 세포(HepG2)의 중성지방 축적을 억제하거나",
 "[21]은 HepG2 세포 실험")
sec('processing',"고정차는 3,5-디카페오일퀸산이 많아 마늘 섭취 뒤 입 냄새 성분(알릴메틸설파이드)을 줄였다는 보고가 있다[9].",
 "기원 종이 밝혀지지 않은 한 고정차 시료는 3,5-디카페오일퀸산이 건조중량의 10.6%였고, 이 차를 마시면 마늘 섭취 뒤 입 냄새 성분(알릴메틸설파이드)이 줄었다는 보고가 있으나 다라 잎 자체로 한 시험은 아니다[9].",
 "[9]의 탈취 시험 고정차는 종이 명시되지 않음(다라 잎은 따로 성분만 분석) — 시료 종 혼동 방지")
sec('safety',"건강기능식품 고시형 원료가 아니어서 고시된 섭취 시 주의사항은 없다[1].",
 "목록에서 다라엽은 식품원료(A코드)로만 올라 있고, 건강기능식품 고시형 원료로서 고시된 섭취 시 주의사항은 확인하지 못함[1].",
 "I1020 원자료 행은 A코드 식품원료뿐; '고시형 원료가 아니다'를 [1]이 직접 말하지 않음(고시 제2026-43호 요건 파일에도 다라 없음)")
sec('safety',"그러나 고농도 고정차 추출물(γ-사이클로덱스트린 포접물)을 6주 먹인 생쥐에서는",
 "그러나 고농도 대엽 고정차 추출물(γ-사이클로덱스트린 포접물, 원 논문에서 종명은 확인하지 못함)을 6주 먹인 생쥐에서는",
 "원 연구(PMID 31877869) 전문에서 시료 종명을 확인할 수 없어 다라 자료로 읽히지 않게 함")
sec('safety',"다라 분말 1.0·2.0 g/kg를 30일 먹인 흰쥐에서는 혈장 총콜레스테롤이 낮아졌다[17].",
 "고콜레스테롤 식이를 먹인 흰쥐에게 다라 1.0·2.0 g/kg를 30일 위관 투여하자 혈장 총콜레스테롤이 낮아졌으나 녹차보다 효과가 작았다[17].",
 "[17] 초록: 고콜레스테롤 식이 모델, 위관 투여, 녹차가 더 효과적")

comp('Latifoloside G','content_text',"잎에서 새로 분리(함량 확인하지 못함)[10]; 대엽 고정차 리뷰는 라티폴로사이드 G·쿠디노사이드 A·G가 총사포닌의 80% 넘게 차지해 지표 성분으로 제안된 연구를 소개(그 연구의 시료 종명은 확인하지 못함)[4]",
 "[4] 전문에서 해당 연구의 시료 종명을 확인할 수 없음")
comp('Kudinoside A','content_text',"대엽 고정차 총사포닌 지표 후보 3종의 하나(시료 종명·함량 확인하지 못함)[4]","[4] 전문에서 시료 종명 확인 불가")
comp('Kudinoside G','part',"나무껍질","[12]는 나무껍질; 잎에서 나왔다는 다라 자료는 확인하지 못함([4]는 종명 불명)")
comp('Ursolic acid','part',"다라(부위는 초록에 없음)","[13] 초록에 부위가 없음(전문 열람 불가)")
comp('Ethyl caffeate','part',"다라(부위는 초록에 없음)","[13] 초록에 부위가 없음")
comp('27-O-p-Coumaroyl ursolic acid','part',"다라(부위는 초록에 없음)","[27] 초록에 부위가 없음")
comp('27-O-p-Coumaroyl ursolic acid','content_text',"다라 유래 성분 선별에서 얻음(부위·함량 확인하지 못함)[27]","[27] 초록은 'Ilex latifolia products' 선별이라고만 씀")
comp('27-O-p-Coumaroyl ursolic acid','activity_ko',"EGFR 티로신인산화효소 억제·유방암세포 자멸 유도(세포·동물)[27]","[27] 초록은 경구 활성, MeSH에 누드마우스 실험 포함")
comp('Kudinoside D','activity_ko',"유방암세포에서 SREBP-1/FASN 억제·세포자멸 유도(세포); 생쥐 이종이식 억제는 n-부탄올·에틸아세테이트 분획으로 확인(동물)[26]","[26] 동물 실험은 KD-D 단일 성분이 아니라 추출 분획")
comp('3-O-Caffeoylquinic acid','activity_ko',"고정차 항산화 반응에서 생기는 라디칼은 카페오일퀸산류 유래로 확인(EPR)[30]","[30]은 카페오일퀸산류 전체를 말하고 3-CQA를 특정하지 않음")
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('/home/user/hfoodguide-wave3/docs/materials/ilex-latifolia/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
