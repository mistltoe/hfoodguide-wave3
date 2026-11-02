import json,sys
p='/home/user/hfoodguide-wave3/docs/materials/sedum-aizoon/dossier.json'
d=json.load(open(p))
S={s['key']:s for s in d['sections']}
changes=[]
def rep(key,old,new,why):
    b=S[key]['body']; assert b.count(old)==1,(key,old); S[key]['body']=b.replace(old,new)
    changes.append({"where":f"sections.{key}","before":old,"after":new,"why":why})

rep('cultivation',"칼슘 처리 실험에서는 중간 농도(30 mM)에서 생육이 가장 좋았고 총플라보노이드가 1.51배로 늘었다[15].",
 "칼슘 처리 화분 실험에서는 중간 농도(30 mM CaCl2)에서 키와 포기 폭이 가장 컸고, 초록은 총플라보노이드가 1.51배로 늘었다고 적었으나 본문 값은 생체중 1 g당 62.5→72.6 mg(약 1.16배)이며 1.51배는 캠페롤의 증가폭이었다[15]. 다만 이 실험의 모종은 '양심채'(가는기린초×기린초 잡종)를 동정한 연구와 같은 구이저우성 황핑현의 산채 재배 기지에서 왔으므로, 가는기린초 순종의 결과로 보기는 어렵다[5, 15].",
 "[15] 전문: 총플라보노이드 62.5→72.6 mg/g FW, 1.51배는 캠페롤. 모종 출처(구이저우 황핑현 주저우진 산채 기지)가 [5]의 양심채 시료와 같음")
rep('processing',"잡종 채소 '양심채'를 다룬 논문도 가식부 100 g당 단백질 2.1 g, 칼슘 315 mg, 철 3.2 mg 같은 값을 인용하고 있어, 이 영양값이 어느 식물에서 나온 것인지는 확인하지 못함.",
 "그런데 잡종 채소 '양심채'를 다룬 논문은 같은 값(가식부 100 g당 단백질 2.1 g, 칼슘 315 mg, 철 3.2 mg)을 기린초(Phedimus kamtschaticus)의 값으로 인용하고 있어, 이 영양값이 가는기린초·기린초·양심채 중 어느 식물에서 나온 것인지는 확인하지 못함[5].",
 "[5] 전문 서론은 이 값을 P. kamtschaticus(F.) 단락에서 인용함; 출처 번호 누락도 보완")
rep('processing',"가공 연구로는 잎·줄기 가루를 밀가루의 0–25% 대신 넣어 국수를 만든 실험이 있으며",
 "가공 연구로는 'Sedum aizoon' 가루(초록에 부위·산지 동정 정보 없음)를 밀가루의 0–25% 대신 넣어 국수를 만든 실험이 있으며",
 "[17] 초록은 부위를 밝히지 않음(잎·줄기 근거 없음)")
rep('safety',"그러나 피롤리지딘 알칼로이드를 만드는 국화과의 Gynura japonica도 같은 '토삼칠'로 불리며, 이 식물이 알칼로이드가 없는 토삼칠(가는기린초)과 혼용되어 중국의 간정맥폐쇄 증후군의 절반 이상을 일으킨 것으로 정리되었다[7, 22].",
 "그러나 피롤리지딘 알칼로이드를 만드는 국화과의 Gynura japonica도 '토삼칠'로 불려 알칼로이드를 만들지 않는 토삼칠(가는기린초)과 자주 혼용되며, 중국 간동양폐쇄증후군(HSOS) 사례의 절반 이상이 이 G. japonica 섭취로 생긴 것으로 정리되었다[7, 22].",
 "[7]·[22] 초록: '절반 이상'은 G. japonica가 원인인 HSOS 비율이며 혼용 때문이라고 단정하지 않음 — 인과 서술을 원문대로 분리")
rep('safety',"이 종은 카드뮴을 잘 빨아들여 수경재배에서 지상부 카드뮴이 133.0 mg/kg에 이르렀으므로, 오염 토양에서 자란 잎은 중금속에 주의해야 한다[19].",
 "카드뮴·아연 처리 수경재배 실험에서 이 종의 지상부 카드뮴 농도가 133.0 mg/kg에 이르러 카드뮴 정화 식물로 제안되었다[19]. 이로 미루어 오염 토양에서 자란 잎은 중금속이 쌓였을 수 있다(식용 잎의 실측값은 확인하지 못함).",
 "[19] 초록: Cd 처리 수경재배·정화(phytoextraction) 연구; 식용 위험은 추론임을 표시")

# compounds
C={c['name']:c for c in d['compounds']}
def cset(name,field,new,why):
    old=C[name][field]; C[name][field]=new
    changes.append({"where":f"compounds[{name}].{field}","before":json.dumps(old,ensure_ascii=False),"after":json.dumps(new,ensure_ascii=False),"why":why})
cset('Iriflophenone','source',[2,13,20],"부위 '지상부·뿌리줄기'는 [2] 표1 근거; [20] 초록엔 부위 없음")
cset('Iriflophenone','content_text',"에틸아세테이트 추출물에서 분리(부위·함량 수치 없음)[20]; 총설은 지상부·뿌리줄기에서 보고된 것으로 정리[2]; 뿌리에서 이리플로페논–플라보노이드 결합 화합물 4종 분리[13]","[20] 초록에 부위 기재 없음")
cset('Sedacin A','activity_ko',"새로 분리된 이소플라본; DPPH·ABTS 소거능 시험(시험관)","[12] 초록은 '새 화합물'·항산화 시험만 말함")
cset('Luteolin','activity_ko',"마우스 응고 시간 단축(100·30 µg/mL; 동물), PT·APTT·TT 소폭 단축(시험관)","[10] 초록: 응고시간은 in vivo, PT/APTT/TT는 in vitro")
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('/home/user/hfoodguide-wave3/docs/materials/sedum-aizoon/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
