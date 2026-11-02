import json,re,sys
p=sys.argv[1]
d=json.load(open(p))
changes=[]
def rep(where, obj, key, old, new, why):
    s=obj[key]
    assert old in s, (where, old)
    obj[key]=s.replace(old,new)
    changes.append({"where":where,"before":old,"after":new,"why":why})
S={s['key']:s for s in d['sections']}
# overview
rep("sections.overview",S['overview'],'body',
 "식약처 목록 전체에는 C. pubescens 학명으로 된 행이 없어서,",
 "식약처 목록 원자료(24,885행)에는 C. pubescens 학명 행도, '아히(ají)'라는 원료명 행도 없고 로코토열매 행의 영문명에도 C. pubescens의 볼리비아 이름인 'Locoto'가 들어 있어 국문·영문명은 C. pubescens를, 학명은 C. baccatum을 가리키는 불일치가 있다[1, 6]. 그래서",
 "I1020 원자료로 불일치를 직접 확인해 근거를 보강(아히 원료명 행 없음, 영문명 Locoto)")
rep("sections.overview",S['overview'],'body',
 "아히는 매운 정도가 하바네로(C. chinense)보다 약한 편이고 흙·채소 같은 향을 낸다고 보고되었다[4].",
 "아히(var. pendulum)와 로코토 시료는 C. chinense 대조보다 덜 맵고, 아히는 흙·채소·피망 같은 향을 낸다고 보고되었다[4].",
 "[4] 초록은 대조를 '하바네로'가 아닌 C. chinense 대조로만 적고, 덜 맵다는 비교는 아히와 로코토를 함께 묶은 것임")
# biology: POWO
rep("sections.biology",S['biology'],'body',
 "POWO는 기본 변종(var. baccatum)과 재배형 변종(var. pendulum)의 자생지로 콜롬비아·페루·볼리비아·파라과이·브라질 남부·아르헨티나 북부 등을 든다(WebSearch 요약으로만 확인)[2]. 미국 농무부 유전자원의 수집지는",
 "자생 범위는 남아메리카이며, 미국 농무부 유전자원의 수집지는",
 "[2] POWO 는 열지 못하고 WebSearch 요약으로만 확인된 것이라 국가 목록을 지우고 [7] 초록(남아메리카 자생 범위)으로 대체")
rep("sections.biology",S['biology'],'body',
 "붉은색·노란색·주황색 등으로 달라진다[3].",
 "붉은색·노란색·주황색 등으로 달라진다[3, 28].",
 "[28] 초록이 '열매 색은 특정 카로티노이드 축적으로 결정'이라고 직접 말함")
# processing
rep("sections.processing",S['processing'],'body',
 "아히의 총캡사이시노이드는 13–352 mg/kg으로 하바네로 대조(1,605 mg/kg)보다 낮았다[4].",
 "아히(var. pendulum)와 로코토(C. pubescens) 시료를 합친 총캡사이시노이드 범위는 13–352 mg/kg으로 C. chinense 대조(1,605 mg/kg)보다 낮았고, 초록에는 아히만의 범위가 따로 없다[4].",
 "[4] 초록의 13–352 mg/kg 은 아히와 로코토를 합친 범위(로코토 자료 섞임); 대조는 '하바네로'가 아니라 C. chinense")
# cultivation [34]
rep("sections.cultivation",S['cultivation'],'body',
 "브라질 고추 연구에서는 수확 연도와 익은 정도에 따라 캡사이신 함량이 달라졌다[34].",
 "브라질 고추 3종(C. baccatum var. pendulum 포함) 연구에서는 수확 연도에 따라 캡사이신 함량이 달라졌다[34].",
 "[34] 초록은 수확 연도 의존성만 말하고 익은 정도에 따른 차이는 결론으로 쓰지 않음; 3종 비교 연구임을 밝힘")
# compounds
C={c['name']:c for c in d['compounds']}
rep("compounds.Capsaicin.content_text",C['Capsaicin'],'content_text',
 "아히 총캡사이시노이드 13–352 mg/kg(하바네로 대조 1,605 mg/kg)[4]",
 "아히·로코토 시료를 합친 총캡사이시노이드 13–352 mg/kg(C. chinense 대조 1,605 mg/kg)[4]",
 "[4] 범위는 아히와 로코토를 합친 값")
c=C['Capsiate']
rep("compounds.Capsiate.activity_ko",c,'activity_ko',
 "매운맛이 약한 캡사이신 유사체로 보고됨[32]",
 "매운맛 없는 캡사이시노이드 유사체로 소개됨[28]",
 "[32] 초록은 매운맛을 말하지 않음; [28] 초록이 'non-pungent capsaicinoid analogs, capsiates'라고 씀")
c['source']=[32,28]
d['_changes']=changes
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
