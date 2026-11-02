import json
p='/home/user/hfoodguide-wave3/docs/materials/apios-americana/dossier.json'
d=json.load(open(p))
S={s['key']:s for s in d['sections']}
changes=[]
def rep(obj,key,old,new,why,where):
    assert old in obj[key], (where, old)
    obj[key]=obj[key].replace(old,new); changes.append({"where":where,"before":old,"after":new,"why":why})
rep(S['related_species'],'body',"영어 이름 'groundnut'은 다른 작물을 가리킬 때도 쓰여 문헌에서 혼동이 생길 수 있다[34]. 예컨대 식용유 물성 논문 한 편은",
 "영어 이름 'groundnut'은 땅콩 같은 다른 작물을 가리킬 때도 쓰여 학명 표기가 뒤섞인 문헌이 있다. 예컨대 식용유 물성 논문 한 편은",
 "[34] 는 혼동 일반론을 말하지 않고 'ground nut (Apios americana)' 기름을 다룬 사례일 뿐이라 일반론 문장에서 [34] 인용을 빼고 사례 문장에만 남김","sections.related_species")
rep(S['processing'],'body',"생시료의 플라보노이드는 14.879 mg QE/g, 페놀 함량은 44.657 mg GAE/g이었고",
 "조리하지 않은 시료의 플라보노이드는 14.879 mg QE/g, 페놀 함량은 44.657 mg GAE/g이었고(껍질 벗긴 덩이줄기를 동결건조·분쇄해 70% 에탄올로 추출한 값)",
 "[4] 전문: 모든 시료를 동결건조 가루로 만든 뒤 70% 에탄올 추출물로 측정 — '생시료'가 생중량 기준으로 읽히지 않게 측정 기준을 밝힘","sections.processing")
rep(S['safety'],'body',"쥐 실험에서는 덩이줄기 가루를 사료의 최대 40%로 5일 먹였으나 독성 평가가 목적은 아니었다[24].",
 "쥐 실험에서는 아피오스 가루(초록에는 부위가 적혀 있지 않음)를 출산 뒤 사료의 최대 40%로 섞어 5일 먹였으나 독성 평가가 목적은 아니었다[24].",
 "[24] 초록은 'Apios powder'라고만 써 덩이줄기임을 확인할 수 없음, 출산 후 투여임을 밝힘","sections.safety")
rep(S['genetics'],'body',"강낭콩·콩과의 공선성(synteny)이 확인되었다[25]",
 "강낭콩족(Phaseoleae) 다른 작물과 대부분의 연관군에서 넓은 공선성(synteny)이 확인되었으며, 전좌 하나가 아피오스·동부속과 강낭콩·콩을 갈랐다[25]",
 "[25] 초록: 강낭콩족과의 확장된 공선성과 함께 강낭콩·콩과 아피오스를 가르는 전좌를 보고 — '강낭콩·콩과의 공선성'만으로는 결과를 단순화했고 '콩과'가 과 이름으로 읽힐 수 있음","sections.genetics")
for c in d['compounds']:
    if c['name']=='Amylose':
        rep(c,'activity_ko',"화학 변성이 쉬웠다[6, 7]","화학 변성이 쉬웠다[6]","하이드록시프로필화 치환도 근거는 [6] 뿐, [7] 은 변성을 다루지 않음","compounds.Amylose.activity_ko")
a=d['assays'][0]['conditions']
rep(a,'sample_prep',"가루 0.2 g + 30% 에탄올 10 mL, 실온 초음파 추출 1시간, 0.45 µm 여과",
 "가루 0.2 g + 30% 에탄올 10 mL, 실온 초음파 추출 1시간, 0.45 µm 여과(발효 조건 최적화 단계 방법; 가공 단계 비교 시료는 본문 2.3.6에 50% 메탄올 20 mL·실온 12시간 교반 추출액을 아이소플라본 분석에 썼다고도 적혀 있음)",
 "[3] 전문 2.3.6 은 가공 단계 비교(2.033·2.188·0.996 mg/g)용 추출을 50% 메탄올로 적어 추출 조건이 두 가지임을 밝힘","assays[0].conditions.sample_prep")
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('/home/user/hfoodguide-wave3/docs/materials/apios-americana/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
