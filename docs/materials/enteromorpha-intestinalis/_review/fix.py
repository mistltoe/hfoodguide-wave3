import json,sys
p=sys.argv[1]
d=json.load(open(p))
S={s['key']:s for s in d['sections']}
changes=[]
def rep(where,obj,key,old,new,why):
    assert old in obj[key],(where,old)
    obj[key]=obj[key].replace(old,new); changes.append({"where":where,"before":old,"after":new,"why":why})
rep("sections.overview",S['overview'],'body',"사용 가능 부위는 '전체'다[1].","사용 가능 부위는 '전체'다(같은 묶음의 '잎파래' 항목만 분류가 '식물'이고, '파래부각' 항목은 사용 부위 칸이 비어 있다)[1].","로컬 I1020 원자료: 잎파래 MLSFC_NM '식물', 파래부각 USE_CND_STDR_CN 공란")
rep("sections.safety",S['safety'],'body',"반면 같은 나라 세인트마틴섬 자연산은","반면 같은 나라 세인트마틴섬에서 채집한 개체는","[7] 초록은 채집 개체라고만 하고 '자연산'으로 구분하지 않음")
rep("sections.safety",S['safety'],'body',"성인에게 안전하지 않다고 결론지었다[7].","성인에게 안전하지 않다고 결론지었다[7]. 다만 [7] 초록은 건·습 기준을 적지 않았고, [6] 원문도 방법에는 결과를 mg/100 g 건조중량으로 잰다고 적고 표에는 mg/kg 건조중량으로 적어, 두 연구 값을 그대로 견줄 때는 단위·기준을 감안해야 한다[6, 7].","단위·기준(건/습) 일관성: [6] 방법 'mg/100 g of dry weight' vs 표2 'mg/kg dry weight', [7] 초록 기준 미기재")
C={c['name']:c for c in d['compounds']}
rep("compounds.Iron.content_text",C['Iron'],'content_text',"0.43%(중국 저장성 동결건조 분말) [8]","0.43%(약 4,300 mg/kg, 중국 저장성 동결건조 분말) [8]","[8] 본문 'iron concentration was 4,300 mg/kg' 병기")
rep("compounds.Iron.content_text",C['Iron'],'content_text',"2290.26 mg/kg(세인트마틴섬 자연산) [7]","2290.26 mg/kg(세인트마틴섬 채집 개체, 초록에 건·습 기준 미기재) [7]","[7] 초록 기준 미기재·'자연산' 표현 근거 없음")
rep("compounds.Lead.content_text",C['Lead'],'content_text',"6.67 mg/kg(세인트마틴섬 자연산) [7]","6.67 mg/kg(세인트마틴섬 채집 개체, 초록에 건·습 기준 미기재) [7]","[7] 초록 기준 미기재")
rep("compounds.Iodine.content_text",C['Iodine'],'content_text',"0.04%(건조 분말, 2반복 평균) [8]","0.04%(약 400 mg/kg; 동결건조 분말 DPEI, 수분 6.54%, 2반복 평균) [8]","[8] 표2: DPEI 수분 6.54%, I 0.04% — 기준을 분명히 함")
C['Iodine']['part']="엽상체 동결건조 분말(중국 저장성; 생시료 동결건조 후 분쇄)"
changes.append({"where":"compounds.Iodine.part","before":"엽상체 동결건조 분말(중국 저장성)","after":C['Iodine']['part'],"why":"[8] 시료 조제: 생 EI 동결건조·40 mesh"})
rep("compounds.Polyphenols.content_text",C['Polyphenols'],'content_text',"qNMR 52.9 ± 5.2 mg/g(5.3%)","qNMR 52.9 ± 5.2 mg/g(평균 분자량 330 g/mol 당량, 5.3%; 갈산 기준 계산은 5.5%)","[9] 원문: qNMR 값은 갈산 당량이 아니라 '330 Mw eq.'이고 갈산 기준은 5.5%")
rep("compounds.Chlorophyll a.content_text",C['Chlorophyll a'],'content_text',"원문 표2의 문헌 비교 열에 엽록소 4.07–5.89%가 적힘(이 연구 시료에서는 측정하지 않음) [8]","원문 표2의 문헌 비교 열에 엽록소 4.07–5.89%가 적힘(이 연구 시료에서는 측정하지 않았고, 문헌값의 건·생 기준은 각주가 불분명) [8]","[8] 표2 문헌 열 각주 'Fresh EI' 표기가 모호해 기준 확정 불가")
rep("sections.cultivation",S['cultivation'],'body',"3 m 줄 6개마다 약 6 g짜리 종묘를 약 11개씩 달아 길렀다[6].","구획마다 3 m 줄 6개를 두고 줄마다 약 6 g짜리 종묘 약 11개를 달아 길렀다[6].","[6] 원문: 구획당 3 m 줄 6개, 줄당 종묘 약 11개(각 약 6 g)")
rep("sections.cultivation",S['cultivation'],'body',"포르투갈에서는 양어장 연못(fish pond aquaculture)에서 자란 녹조 5종 중 하나로","포르투갈 연구진의 조사에서는 양어장 연못(fish pond aquaculture)에서 자란 녹조 5종 중 하나로","[28] 초록에 국가가 없고 저자 소속(포르투갈)만 확인됨")
rep("sections.related_species",S['related_species'],'body',"신종 U. paschima로 기재되었다[3].","신종 U. paschima로 기재되었다[3]. 그래서 분자 동정 없이 형태로만 이 종이라 한 시료(예: 인도산 시료를 쓴 연구)의 결과는 다른 관 모양 Ulva일 가능성을 감안해 읽어야 한다[3].","[3] 결론: 범세계 종 가정이 고유종을 놓치게 함 — 인도산 시료 연구[11,22] 해석 주의 추가")
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
