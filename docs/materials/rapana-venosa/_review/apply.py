import json,sys
p=sys.argv[1]
d=json.load(open(p))
changes=[]
def sec(k): return next(s for s in d['sections'] if s['key']==k)
def rep(obj,key,old,new,where,why):
    assert old in obj[key], (where,old)
    obj[key]=obj[key].replace(old,new,1)
    changes.append({"where":where,"before":old,"after":new,"why":why})

o=sec('overview')
rep(o,'body',"피뿔고둥(Rapana venosa)은 뿔소라과(Muricidae)에 드는 육식성 바다 고둥으로, 식약처",
 "피뿔고둥(Rapana venosa)은 뿔소라과(Muricidae)에 드는 육식성 바다 고둥이다[2, 3]. 식약처",
 "sections.overview","과(Muricidae)는 식품원료 목록[1]에 없는 정보라 [2]·[3] 원문(\"belonging to the family Muricidae\")으로 출처를 붙임")

r=sec('related_species')
rep(r,'body',"피뿔고둥은 이들과 과가 다른 뿔소라과에 속한다[1, 14].",
 "피뿔고둥은 이들과 과가 다른 뿔소라과에 속한다[2, 3].",
 "sections.related_species","[1](식품원료 목록)·[14](초록)는 피뿔고둥의 과를 말하지 않음; [2]·[3] 원문이 Muricidae라고 씀")
rep(r,'body',"일본 연안 16종 조사에는 뿔소라과도 포함되었지만 초록에 고농도 종으로 이름이 나온 것은 매물고둥속과 Fusitriton·Hemifusus 등이었다[14].",
 "일본 연안 16종 조사에는 뿔소라과도 포함되었고 초록은 Babylonia japonica를 뺀 모든 표본에서 테트라민이 검출되었다고 적었지만, 피뿔고둥이 조사 대상에 들었는지와 그 값은 초록에 없고, 고농도(침샘 1 g당 1,000 μg 초과) 위험 종으로 꼽힌 것은 매물고둥속과 Fusitriton·Hemifusus였다[14].",
 "sections.related_species","[14] 초록 원문 대조: 'Babylonia japonica 외 전 표본 검출'과 1,000 μg/g 기준을 보태 이 종 해당 여부가 불명임을 분명히 함")

b=sec('biology')
rep(b,'body',"자연 상태의 착저·변태율은 1% 미만으로 낮다[8]",
 "유생의 착저·변태율은 1% 미만으로 낮다[8]",
 "sections.biology","[8] 초록은 '자연 상태'라고 하지 않고 낮은 착저·변태율(<1%)이 자원량을 제한한다고만 씀")

c=sec('cultivation')
rep(c,'body',"착저 유도 연구가 종묘 생산과 자원 관리에 쓰일 수 있다고 보았다[8, 9]",
 "착저 유도 연구가 어획 개선과 자원의 지속 이용에 쓰일 수 있다고 보았다[8, 9]",
 "sections.cultivation","[8] 초록 원문은 'improve R. venosa harvesting, as well as the sustainable development and utilization'; '종묘 생산'은 원문에 없음")

pr=sec('processing')
rep(pr,'body',"효소(알칼레이스)로 분해해","세균 유래 단백질분해효소로 분해해",
 "sections.processing","상표명 대신 일반명(원문: bacterial-sourced Alcalase)")
rep(pr,'body',"살을 효소로 분해한 펩타이드 분획이","이 종을 효소로 분해해 얻은 펩타이드 분획이",
 "sections.processing","[26] 초록은 원료 부위(살)를 밝히지 않음")

g=sec('genetics')
rep(g,'body',"PacBio·Illumina 서열과 Hi-C 자료로","긴 리드·짧은 리드 염기서열과 Hi-C 자료로",
 "sections.genetics","상표명 대신 일반명")

s=sec('safety')
rep(s,'body',"육식성 바다 고둥의 침샘에는 신경독 테트라민이 있어 대개 가벼운 중독을 일으키나, 신장질환·중증근무력증 환자에게는 호흡부전까지 올 수 있다[20, 19, 16].",
 "물레고둥과 등 일부 육식성 바다 고둥의 침샘에는 신경독 테트라민이 있어 대개 가벼운 중독을 일으키나, 신장질환·중증근무력증 환자에게는 호흡부전까지 올 수 있다[20, 19, 14]. 두 증례 보고는 먹은 고둥의 종을 피뿔고둥으로 특정하지 않았다[19, 20].",
 "sections.safety","모든 육식성 고둥으로 일반화한 표현을 좁힘; [16]은 매물고둥 2종 계절 변동 연구라 환자 위험의 근거가 아님→[14]로 교체; 증례의 원인 종 미특정 명시")
rep(s,'body',"그러나 피뿔고둥 침샘의 테트라민 함량을 정량한 자료는 PubMed에서 확인하지 못함. 일본 연안 16종 조사도 초록에 이 종의 값이 없고 고위험 종으로 매물고둥속 등을 꼽았다[14].",
 "그러나 피뿔고둥 침샘의 테트라민 함량을 정량한 자료는 PubMed에서 확인하지 못함(PubMed 검색 'Rapana venosa tetramine' 0건). 일본 연안 16종 조사는 Babylonia japonica를 뺀 모든 표본에서 테트라민을 검출했다고 적었으나 초록에 이 종의 이름과 값은 없고, 고위험 종(침샘 1,000 μg/g 초과)으로 매물고둥속 등을 꼽았다[14]. 따라서 피뿔고둥이 테트라민 중독 위험이 낮다고도 높다고도 단정할 수 없으며, 같은 국내 연구에서는 피뿔고둥 침샘에서 지용성 패독이 검출되지 않았다는 결과만 있다[12].",
 "sections.safety","과업 지시: 이 종 자료로 테트라민 위험 확인 — 이 종 정량 자료 없음을 근거와 함께 명시하고 [12]의 침샘 불검출(지용성 패독) 결과를 구분해 적음")

for cpd in d['compounds']:
    if cpd['name']=='Tetramethylammonium':
        old=cpd['content_text']
        cpd['content_text']="이 종(피뿔고둥)의 함량은 확인하지 못함(PubMed에 이 종 정량 자료 없음); 참고로 과가 다른 국내 매물고둥류(물레고둥과 Neptunea arthritica 568.10–4580.05, N. eulimata 679.35–7762.16 mg/kg, 침샘, 2023–2024 월별)"
        changes.append({"where":"compounds[Tetramethylammonium].content_text","before":old,"after":cpd['content_text'],"why":"매물고둥속은 물레고둥과로 '근연'이 아님; [16] 초록 값으로 종별 범위를 나눠 적음"})
        old=cpd['activity_ko']
        cpd['activity_ko']="물레고둥과 등 일부 육식성 고둥의 침샘에 있는 신경독으로 섭취 시 눈 통증·두통·어지럼 등을 일으키며 신장질환자·중증근무력증 환자에게 위중할 수 있다(피뿔고둥에서 확인된 사례는 아님)[15, 19, 20]"
        changes.append({"where":"compounds[Tetramethylammonium].activity_ko","before":old,"after":cpd['activity_ko'],"why":"다른 종 자료임을 명시; [16]은 증상 근거가 아님"})
        cpd['source']=[14,15,16,19,20]
    if cpd['name']=='Tetrodotoxin':
        old=cpd['content_text']
        cpd['content_text']="아드리아해 2023–2025 조사에서 이 종을 포함한 고둥 104시료 모두 검출 한계(3 μg/kg) 미만"
        changes.append({"where":"compounds[Tetrodotoxin].content_text","before":old,"after":cpd['content_text'],"why":"LOTUS 보고는 [1](식품원료 목록)이 뒷받침하지 않음"})
        cpd['source']=[13]
    if cpd['name']=='Hemocyanin':
        old=cpd['activity_ko']
        cpd['activity_ko']="혈림프 50–100 kDa 분획이 유방암 세포주에서 항종양 활성을 보였다는 세포 실험이 있으나, 이 분획에는 헤모시아닌 기능 단위 외에 퍼옥시다제 유사 단백질·L-아미노산 산화효소 등도 함께 들어 있어 헤모시아닌 자체의 활성으로 확인된 것은 아니다[29, 28]"
        changes.append({"where":"compounds[Hemocyanin].activity_ko","before":old,"after":cpd['activity_ko'],"why":"[29] 초록: 활성 분획의 주요 단백질은 peroxidase-like, Aplysianin A 상동, LAAO, RvH 50 kDa FU — 헤모시아닌 단독 효과로 읽히는 과장 수정"})
for a in d['assays']:
    if a['compound'].startswith('Paralytic'):
        old=a['conditions']['sample_prep']
        a['conditions']['sample_prep']=old.replace("Sep-Pak C18","C18 고상추출 카트리지")
        changes.append({"where":"assays[PSP].conditions.sample_prep","before":old,"after":a['conditions']['sample_prep'],"why":"상표명 대신 일반명"})
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open(p.replace('dossier.json','_review/changes.json'),'w'),ensure_ascii=False,indent=1)
print(len(changes))
