import json
p='dossier.json'; d=json.load(open(p))
S={s['key']:s for s in d['sections']}
changes=[]
def rep(key,a,b,why):
    s=S[key]; assert a in s['body'],(key,a); s['body']=s['body'].replace(a,b); changes.append({"where":"sections."+key,"before":a,"after":b,"why":why})
rep('related_species','산지 가격은 kg당 약 50위안으로','중국·동남아 활어 시장 가격은 kg당 약 50위안으로','[2] 서론은 활어 시장(live seafood markets) 가격이라고 씀, 산지 가격 아님')
rep('biology','수온에도 넓게 견뎌, 저수온 실험에서 내한성 무리는 2.8 ℃까지 버텼다[14].','수온 변화에도 잘 적응하는 광온성 어종으로 소개되며[2], 저수온 단백체 연구는 대조군(15 ℃)과 3.8 ℃의 저온 민감 무리, 2.8 ℃의 내한성 무리를 비교했다[14].','[14] 초록은 실험군 온도만 제시하고 \'넓게 견딘다\'는 말은 없음; 광온성은 [2] 본문(eurythermal)에 있음')
rep('biology','자연산 치어는 잡식성이어서 양식 치어보다 장내 미생물이 더 다양했다[33].','자연산 치어는 잡식성이어서 육상 못 양식 치어보다 장내 미생물이 더 다양했다[33].','[33] 초록은 못(pond) 양식 개체와만 비교해 더 다양하다고 씀')
rep('processing','출하 전 굶기면 3일째부터 살의 지방이 줄지만 14일째부터 단백질도 줄고 산화 스트레스가 생겨 신중히 써야 한다고 했다[27].','출하 크기 감성돔을 28일 굶긴 실험에서는 3일째 뒤로 살의 지방이 줄었지만 14일째부터 단백질도 줄었고, 간 항산화 효소는 3일째부터, 살의 말론다이알데하이드는 21일째부터 늘어 단식 기법은 신중히 써야 한다고 했다[27].','[27] 초록: 단백질 감소 14일, 항산화 효소 증가 3일, MDA 증가 21일 — 원문은 산화 스트레스 시점을 14일로 말하지 않음')
rep('processing','3차원 배양 연구에서는 3% 알긴산나트륨과 4% 젤라틴으로 만든 지지체가 세포 성장을 도왔다[28].','3차원 배양 연구에서는 굳힌 뒤 동결건조해 세포를 나중에 접종하는 지지체 가운데 3% 알긴산나트륨과 4% 젤라틴으로 만든 것이 세포 성장을 도왔고, 세포를 섞어 굳힌 지지체는 성장을 돕지 못했다[28].','[28] 초록: 효과는 cell-seeding 지지체에서만, cell-laden 지지체는 조성과 무관하게 성장 지지 못함 — 조건 누락 보완')
rep('safety','고용량에서는 7일 휴약 후에도 생리 변화가 남았다[24].','1 mg/L 고용량 약욕에서는 7일 휴약 뒤에도 영향이 남아 있을 수 있다고 했다[24].','[24] 초록은 \'may persist\'로 단정하지 않음, 용량 명시')
a=d['assays'][0]
before=json.dumps({"method":a['method'],"mobile_phase":a['conditions']['mobile_phase']},ensure_ascii=False)
a['method']='HPLC-PDA'
a['conditions']['mobile_phase']="A: AccQ-Tag Eluent A(원문 '(= 10:1)', 희석 대상 표기 누락), B: 100% 아세토나이트릴, C: 탈이온수"
changes.append({"where":"assays[0]","before":before,"after":json.dumps({"method":a['method'],"mobile_phase":a['conditions']['mobile_phase']},ensure_ascii=False),"why":"[2] Methods 에 AccQ-Tag 유도체화 단계는 적혀 있지 않고, 10:1 의 상대(물)도 원문에 없음"})
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
