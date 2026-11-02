import json
p='dossier.json'; d=json.load(open(p))
ch=[]
def rep(where,obj,key,old,new,why):
    assert old in obj[key],(where,old)
    obj[key]=obj[key].replace(old,new); ch.append({"where":where,"before":old,"after":new,"why":why})
S={s['key']:s for s in d['sections']}
rep('sections.safety',S['safety'],'body',
 "서아라비아만 해산물에서 무기비소는 총비소의 평균 0.03%, 무독성 아르세노베타인은 81%였다[13]",
 "서아라비아만의 갑오징어·새우·어류(이 종은 1개 시료)를 합친 분석에서 무기비소는 총비소의 평균 0.03%, 무독성 아르세노베타인은 81%였다[13]",
 "[13] 초록의 0.03%·81%는 갑오징어 8, 이 종 1, 어류 23 시료를 합친 값이어서 이 종만의 값처럼 읽히지 않게 고침")
rep('sections.safety',S['safety'],'body',
 "무사 하구 개체의 간췌장에서 0.95 µg/g까지 나왔다[15]",
 "후제스탄 연안 개체의 간췌장에서 0.95 µg/g까지 나왔고, 무사 하구(S4) 개체는 기준을 넘었다[15]",
 "[15] 초록은 0.95 µg/g을 이 종 간췌장 최고값으로만 적고 지점을 밝히지 않음. 무사 하구는 기준 초과 지점으로 따로 언급됨")
rep('sections.safety',S['safety'],'body',
 "(습·건중량 기준은 초록에 없음)이 측정되어 FAO/WHO 허용치를 넘었다고 보고되었다[10].",
 "(습·건중량 기준은 초록에 없음)이 측정되어 FAO/WHO 허용치를 넘었다고 보고되었다[10]. 이 아연 값은 다른 연구의 습중량 근육 값(8.977 µg/g[16], 최고 16.44 mg/kg[9])보다 수십 배 높아 측정 기준이 다를 수 있으므로 직접 비교하지 않는다.",
 "[10] 초록에 습/건 기준이 없고 Zn 300.88 µg/g은 습중량 값[9][16]의 약 18–33배라 기준 차이 가능성을 명시")
for c in d['compounds']:
    if c['name']=='Carotenoids':
        old=c['part']; c['part']="가공 부산물(새우 폐기물)"
        ch.append({"where":"compounds.Carotenoids.part","before":old,"after":c['part'],"why":"[28] 초록은 'shrimp waste'라고만 하고 머리·껍데기를 특정하지 않음"})
s1=d['sources'][0]
rep('sources[1].title',s1,'title',"Eastern king prawn(P. plebejus)","'Eastern kong prawn'(원자료 표기 그대로, P. plebejus)",
 "로컬 I1020 원자료의 대표명은 'Eastern kong prawn'으로 적혀 있음")
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(ch,open('_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(ch))
