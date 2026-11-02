import json
p='/home/user/hfoodguide-wave3/docs/materials/serratula-coronata/dossier.json'
d=json.load(open(p))
changes=[]
def rep(where,obj,key,old,new,why):
    s=obj[key]
    assert old in s,(where,old)
    obj[key]=s.replace(old,new,1)
    changes.append({"where":where,"before":old,"after":new,"why":why})
S={s['key']:s for s in d['sections']}
C={c['name']:c for c in d['compounds']}
rep('sections.overview',S['overview'],'body','아래 함량은 지상부·즙·추출물 기준이다[2, 3, 5]','아래 함량은 지상부·즙·추출물 기준이거나 부위가 밝혀지지 않은 값이다[2, 3, 5]','[5] 초록은 2.3% 값의 부위를 밝히지 않음')
rep('sections.history',S['history'],'body','가금 사육용 생장 촉진제, 농업 곤충학용 제제, 식품 보충용 제제를 만들었다고','가금 사육용·농업 곤충학용·식품 보충용 생물자극 제제(biostimulator)를 만들었다고','[6] 원문 표현은 preparations-biostimulators; 생장 촉진제로 단정하지 않음')
rep('sections.history',S['history'],'body','산비장이로 만든 표준화 제제를 쥐 심부전 모델에 준 연구도 있다[27]','산비장이에서 얻은 엑디스테론 제제를 쥐 만성 심부전 모델에 준 연구도 있다(동물 실험)[27]','[27] 초록에 \'표준화\' 표현 없음; 만성 심부전 모델')
rep('sections.biology',S['biology'],'body','헝가리 연구에서 산비장이 지상부의 20-하이드록시엑디손은 4월에 2.3%로 높았고','헝가리 연구에서 산비장이의 20-하이드록시엑디손은 4월에 2.3%로 높았고(부위·건조 기준은 초록에 없음)','[5] 초록은 부위·기준을 적지 않음 — 지상부 값으로 단정하지 않음')
rep('sections.safety',S['safety'],'body','혈장 노르아드레날린이 낮아졌고 다른 생화학 지표는 대조군과 유의한 차이가 없었다[11]','혈장 노르아드레날린이 낮아졌고 고용량군에서 코르티코스테론/노르아드레날린 비가 달랐으며, 그 밖의 생화학 지표와 흉선·심장·뇌 세포의 DNA 손상·아폽토시스 지표는 대조군과 유의한 차이가 없었다[11]','[11] 초록: 고용량군 코르티코스테론/노르에피네프린 비 유의 차이, 아폽토시스 차이 없음')
c=C['20-Hydroxyecdysone']
rep('compounds[20-Hydroxyecdysone].content_text',c,'content_text','지상부 4월 2.3%(TLC, 건조 여부는 초록에 없음)[5]; 우크라이나산 약 2%[6]','4월 2.3%(TLC, 부위·건조 기준은 초록에 없음)[5]; 우크라이나산 약 2%(부위·기준은 초록에 없음)[6]','[5]·[6] 초록은 부위를 밝히지 않음')
rep('compounds[20-Hydroxyecdysone].part',c,'part','지상부(herb)·즙·추출물','지상부(herb)·즙·추출물(일부 값은 부위 미상)','[5]·[6] 부위 미상')
c=C['Quercetin 3-methyl ether']
rep('compounds[Quercetin 3-methyl ether].activity_ko',c,'activity_ko','감염 생쥐 폐 바이러스 RNA 감소(동물 실험)','감염 생쥐에 복강 투여 시 폐 바이러스 RNA·염증 사이토카인 감소(동물 실험)','[9] 전문: 생쥐 투여는 복강 주사(먹인 것 아님)')
c=C['Lignin']
rep('compounds[Lignin].part',c,'part','지상부(부위는 초록에 명시 없음)','부위는 초록에 명시 없음','[17] 초록에 부위 없음 — 지상부로 단정하지 않음')
c=C['Calcium']
rep('compounds[Calcium].part',c,'part','지상부','부위는 초록에 없음','[5] 초록에 부위 없음')
a=d['assays'][3]
rep('assays[3].part',a,'part','지상부(계절별)','부위는 초록에 없음(계절별)','[5] 초록에 부위 없음')
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('/home/user/hfoodguide-wave3/docs/materials/serratula-coronata/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
