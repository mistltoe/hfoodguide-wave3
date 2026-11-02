import json
p='/home/user/hfoodguide-wave3/docs/materials/agave-americana/dossier.json'
d=json.load(open(p))
changes=[]
def rep(where,obj,key,old,new,why):
    v=obj[key]
    assert v.count(old)==1,(where,old)
    obj[key]=v.replace(old,new)
    changes.append({"where":where,"before":old,"after":new,"why":why})
S={s['key']:s for s in d['sections']}
rep('sections.history',S['history'],'body',
 '용설란속 식물은 아메리카 대륙의 옛 문화에서 이미 귀하게 쓰였고, 소노라 사막 일대에는 콜럼버스 이전 시기의 용설란 농업 흔적이 남아 있다[5].',
 '용설란속 식물은 아메리카 대륙의 옛 문화에서 이미 귀하게 쓰였고, 소노라 사막의 콜럼버스 이전 시기 이용 기록과 바하칼리포르니아·소노라의 수백 년 된 용설란 농업 흔적이 남아 있다[5].',
 '[5] 초록: 소노라 사막의 pre-Columbian 기록과 Baja California·Sonora의 수백 년 된 농업 흔적을 구분해 씀')
rep('sections.history',S['history'],'body',
 '아조레스 제도 테르세이라섬 농가는 여름철 반추가축의 물 공급원으로 용설란을 써 왔다[22].',
 '아조레스 제도 농가는 여름철 반추가축의 물 공급원으로 용설란을 써 왔고, 테르세이라섬 시료로 그 사료 가치가 조사되었다[22].',
 '[22] 초록·전문: 물 공급원 이용 주체는 아조레스 농가 전반이며 테르세이라섬은 시료 채취지')
rep('sections.related_species',S['related_species'],'body',
 '같은 연구에서 잰 아구아미엘 사포닌 함량은',
 '다른 연구에서 잰 아구아미엘 사포닌 함량(건물 기준)은',
 '앞 문장은 [3], 이 수치는 [8]의 별개 연구이므로 "같은 연구"는 틀림; 원문 단위 DM(건물) 명시')
rep('sections.related_species',S['related_species'],'body',
 '캘리포니아 자생종 A. deserti와 재배종 A. americana는',
 '캘리포니아에 자생하는 두 종인 야생 A. deserti와 재배 A. americana는',
 '[30] 초록: 두 종 모두 캘리포니아 자생(native)이며 야생/재배 시료의 구분임')
rep('sections.cultivation',S['cultivation'],'body',
 '헥타르당 연 9.3 Mg으로 가장 높았고, 300 mm에서도 중간 수준이 유지되었다[4].',
 '헥타르당 연 9.3 Mg으로 가장 높았고, 300 mm에서도 중간 수준이 유지되었다[4, 19].',
 '[4] 전문은 "미국 남서부 첫 포장 시험"으로만 쓰고 시험지 마리코파는 [19] 초록에 있음')
rep('sections.cultivation',S['cultivation'],'body',
 '사람의 토지 이용과 해발고도가 분포를 가장 크게 좌우했다[20].',
 '해발고도 범위(기여도 26.9%)와 토지 이용(23.1%)이 분포를 가장 크게 좌우했으며 사람 손이 닿은 낮은·중간 고도에서 적합도가 가장 높았다[20].',
 '[20] 초록: 기여 순서는 고도 26.9% > 토지 이용 23.1%')
rep('sections.genetics',S['genetics'],'body',
 '유전 다양성은 영양번식 때문에 줄어든 것으로 해석되었다[3].',
 '재배 변종의 유전 다양성 감소는 영양번식 등 여러 요인 때문인 것으로 해석되었다[3].',
 '[3] 초록: "due to vegetative propagation, among other factors"')
rep('sections.safety',S['safety'],'body',
 '보고자들은 즙 속 옥살산칼슘 결정과 사포닌이 원인일 수 있다고 추정했다[26, 27].',
 '보고자들은 피부에 박힌 옥살산 결정[26], 또는 즙 속 옥살산칼슘 결정과 사포닌[27]이 원인일 수 있다고 추정했다.',
 '[26] 초록은 옥살산 결정만 언급, 사포닌은 [27]에만 있음')
a=d['assays'][0]
rep('assays[0].rationale',a,'rationale',
 '함량이 그루의 성숙도에 따라 달라 품질 지표로 제안됨.',
 '그루가 성적으로 성숙하면 함량이 줄어 사포닌 공급원으로 평가할 때 성숙도를 고려해야 한다고 결론지음.',
 '[8] 초록은 품질 지표로 제안하지 않고 "평가 전 성숙도를 고려해야 한다"고 씀')
c=[x for x in d['compounds'] if x['name']=='Diosgenin'][0]
rep('compounds.Diosgenin.activity_ko',c,'activity_ko',
 '용설란속 잎에서 가장 많은 사포게닌 두 가지 중 하나',
 '조사한 용설란속 다섯 종 잎에서 가장 많은 사포게닌 두 가지 중 하나',
 '[15] 초록은 다섯 종 조사 결과로 한정')
c=[x for x in d['compounds'] if x['name']=='Tigogenin'][0]
assert c
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('/home/user/hfoodguide-wave3/docs/materials/agave-americana/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
