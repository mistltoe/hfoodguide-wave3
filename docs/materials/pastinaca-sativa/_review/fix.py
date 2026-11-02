import json,sys
p='/home/user/hfoodguide-wave3/docs/materials/pastinaca-sativa/dossier.json'
d=json.load(open(p))
changes=[]
def rep(obj,key,old,new,where,why):
    s=obj[key]; assert old in s,(where,old); obj[key]=s.replace(old,new); changes.append({"where":where,"before":old,"after":new,"why":why})
S={s['key']:s for s in d['sections']}
rep(S['overview'],'body','흰색~연노란색','흰색~노란색','sections.overview','[2]는 pale white to vibrant yellow')
rep(S['overview'],'body','푸로쿠마린이 알려져 있다[3][17]','푸로쿠마린이 알려져 있다[3][19]','sections.overview','[17] 초록은 파스닙 폴리아세틸렌을 이름으로 특정하지 않음 → 파스닙 뿌리에서 팔카리놀·팔카린디올을 정량한 [19]로 교체')
rep(S['history'],'body','라틴어 pastinum(땅을 갈다) 또는 pastus(먹을거리)','라틴어 pastino(포도나무를 심으려 땅을 고르다) 또는 pastus(먹을거리)','sections.history','[2] 원문은 pastino, "preparing the land for planting of the vine"')
rep(S['history'],'body','세르비아·이탈리아 민간에서는 뿌리·잎 우린 물을 소화·이뇨용으로,','세르비아 민간에서는 뿌리·잎·열매 우린 물을 소화·이뇨·식욕 증진용으로, 이탈리아에서는 뿌리·잎 우린 물을 담즙 분비·이뇨용으로,','sections.history','[2] 원문: 세르비아(소화·이뇨·식욕·젖 분비), 이탈리아(담즙 분비·이뇨)로 나라별 용도가 다름')
for k in ['related_species','cultivation','genetics']:
    if '파스닙굴나방' in S[k]['body'] or '굴나방' in S[k]['body']:
        pass
rep(S['related_species'],'body','파스닙굴나방(Depressaria pastinacella)','파스닙웹웜(Depressaria pastinacella, 꽃·열매를 먹는 나방 애벌레)','sections.related_species','Depressaria pastinacella 는 webworm(거미줄치레류)으로 굴나방(leaf miner)이 아님')
rep(S['cultivation'],'body','북미와 뉴질랜드에서는 꽃을 먹는 파스닙굴나방이 종자 생산을 최대 75%까지 줄였다[26]','뉴질랜드에서는 2004년 처음 나타난 파스닙웹웜이 2006년 종자 생산을 최대 75%까지 줄였다[26]','sections.cultivation','[26] 초록: 75% 감소는 뉴질랜드 개체군(2006)에 한정, 북미 값 아님')
rep(S['genetics'],'body','2026년 파스닙 첫 염색체 수준 유전체가','2026년 파스닙 염색체 수준 유전체가','sections.genetics','[23] 초록에 "첫" 유전체라는 표현 없음')
rep(S['genetics'],'body','굴나방과의 상호작용','파스닙웹웜과의 상호작용','sections.genetics','곤충 이름 정정(webworm)')
rep(S['safety'],'body','파스닙 퓌레를 먹은 영아의 입 주위 피부염과 어린이 사례도 보고되었다[13][14]','파스닙 퓌레로 인한 영아의 입 주위 광피부염이 보고되었고[13], 소아과 학술지에도 파스닙 광피부염 증례가 실렸다[14]','sections.safety','[14]는 초록이 없어 환자 연령을 확인하지 못함 → 확인 가능한 범위로 씀')
rep(S['safety'],'body','말·염소 실험에서 야생 파스닙 즙을 피부에 바르면 심한 광피부염이 생겼지만, 먹인 염소의 혈청에서는 잔토톡신이 검출되지 않았다[7]','방목 말의 광과민 사례 조사와 염소 실험에서 야생 파스닙을 피부에 바르면 염소와 말에 심한 광피부염이 생겼지만, 먹인 염소는 대체로 영향이 없었고 혈청에서 잔토톡신도 검출되지 않아 피부 접촉이 주된 경로로 해석되었다[7]','sections.safety','[7] 초록: 먹인 염소는 largely unaffected, 피부 도포가 원인 경로')
rep(S['safety'],'body','뿌리 소랄렌류 약 40 ppm은 조리로 줄지 않는다[5].','1981년 연구는 뿌리의 소랄렌류 3종 합계를 약 40 ppm으로 보고하며 끓이거나 전자레인지로 익혀도 줄지 않는다고 했다[5]. 이 값은 갓 캔 뿌리 값(2.5 mg/kg 미만)[6]보다 높아 시료 상태에 따라 차이가 크다.','sections.safety','[5] 초록: 3종 합계 약 40 ppm, 끓이기·전자레인지; [6]과의 차이를 밝힘')
C={c['name']:c for c in d['compounds']}
rep(C['Falcarinol'],'activity_ko','백혈병 세포주 CEM-C7H2에 IC50 3.5 µmol/L로 가장 강한 세포독성[17]','셀러리 뿌리에서 분리한 팔카리놀이 세포 실험에서 백혈병 세포주 CEM-C7H2에 IC50 3.5 µmol/L로 가장 강한 세포독성을 보임(사람 효과 아님)[17]','compounds.Falcarinol','[17] 시험 화합물은 셀러리 뿌리에서 분리; 세포 결과임을 밝힘')
rep(C['Falcarindiol'],'activity_ko','숙성 파스닙의 항염 효과를 일부 설명하는 성분으로 정량됨[4]','숙성 후 크게 늘어 숙성 추출물의 세포·동물 항염 효과를 일부 설명할 수 있다고 제시됨[4]','compounds.Falcarindiol','[4]는 "may partially explain" — 세포·생쥐 결과임을 밝힘')
rep(C['Falcarindiol 3-acetate'],'activity_ko','최소가공 중 껍질 벗기기에서 크게 손실[21]','최소가공 중 폴리아세틸렌(이 성분 포함) 손실은 주로 껍질 벗기기 단계에서 생김[21]','compounds.Falcarindiol 3-acetate','[21] 초록은 폴리아세틸렌 전체에 대한 결과')
rep(C['Quercetin'],'activity_ko','뿌리 페놀 성분 중 하나로 항산화 평가에 쓰임[2]','리뷰는 USDA 함량값만 제시하며, 파스닙 퀘르세틴의 효능 근거는 확인하지 못함[2]','compounds.Quercetin','[2]에 퀘르세틴으로 항산화를 평가했다는 내용 없음')
rep(C['Sphondin'],'activity_ko','파스닙굴나방과의 공진화로 함량이 높아진 것으로 해석된 방어 성분[25]','표본관 표본과 비교해 파스닙웹웜과의 상호작용으로 함량이 높아진 것으로 해석된 방어 성분[25]','compounds.Sphondin','곤충명 정정, [25] 초록 표현에 맞춤')
rep(C['Octyl acetate'],'activity_ko','파스닙굴나방이','파스닙웹웜이','compounds.Octyl acetate','곤충명 정정')
s=json.dumps(d,ensure_ascii=False)
assert '굴나방' not in s, [x for x in s.split('굴나방')][:1]
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('/home/user/hfoodguide-wave3/docs/materials/pastinaca-sativa/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
