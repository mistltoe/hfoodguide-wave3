import json
p='/home/user/hfoodguide-wave3/docs/materials/eugenia-stipitata/dossier.json'
d=json.load(open(p))
changes=[]
def rep(where,obj,key,old,new,why):
    assert old in obj[key], (where,old)
    obj[key]=obj[key].replace(old,new); changes.append({"where":where,"before":old,"after":new,"why":why})
S={s['key']:s for s in d['sections']}
rep("sections.overview",S['overview'],'body',"Eugenia 속의 작은 나무로","Eugenia 속의 나무로","[2]는 높이 2.5–15.0 m의 중간 크기 나무라고 씀(biology 절과 모순)")
rep("sections.history",S['history'],'body',"안데스 지역 경제에 가치가 큰 과일로 여겨졌다[7]","안데스 지역 경제에 잠재적으로 가치가 있는 과일로 소개되었다[7]","[7] 초록은 'potentially economically valuable'이라고 씀")
rep("sections.related_species",S['related_species'],'body',"Eugenia 속에는 약 400종이 기재되어 있으며, 그 가운데 Eugenia uniflora(피탕가) 등 여러 종이 열매와 이차대사산물 자원으로 연구되었다[2].","Eugenia 속에는 약 400종이 기재되어 있으며, 그 가운데 여러 종이 열매와 이차대사산물 자원으로 연구되었다[2].","[2] 전문(PMC 추출본)에서 해당 문장의 종명이 빠져 E. uniflora 를 이 문장의 근거로 확인할 수 없음; E. uniflora 는 다음 문장 [23]에서 다룸")
rep("sections.processing",S['processing'],'body',"다크초콜릿에 동결건조 과육을 2%까지 넣어도 초콜릿의 성질은 달라지지 않았다[22].","다크초콜릿에 동결건조 과육을 1.0–2.0% 넣었을 때 총폴리페놀·항산화능·카테킨류·수분·질감은 차이가 없었으나 카슨 항복응력·점도와 입자 크기는 달라졌고, 연구진은 2% 첨가까지 초콜릿 성질에 영향이 없다고 결론지었다[22].","[22] 초록은 항복응력 증가·점도 감소·입자 크기 증가도 보고 — '성질이 달라지지 않았다'는 단정은 과장")
C={c['name']:c for c in d['compounds']}
rep("compounds[Myricetin].content_text",C['Myricetin'],'content_text',"생과육 17 mg/100 g이라는 정리[3]; 산가수분해 과육 메탄올 추출물에서는 0.17 µg/g(생중량)으로 보고되어 값 차이가 큼[4]","에콰도르 리뷰는 '생과육 17 mg/100 g'이라 적었으나[3], 체계적 리뷰 표는 같은 값(17.0 ± 0.50 mg/100 g)을 동결건조 과육 값으로 정리해 생/건 기준이 서로 다름[2]; 다른 연구(산가수분해 과육 메탄올 추출물)는 0.17 µg/g(생중량)으로 보고해[4] 약 1000배 차이가 나므로 어느 한 값을 대표값으로 쓰기 어려움","[2] 표는 17.0 ± 0.50 mg/100 g 을 'Freeze-dried pulp'로 정리 — [3]의 'fresh pulp' 표기와 기준이 엇갈림을 밝힘")
C['Myricetin']['source']=[2,3,4]
rep("compounds[Ascorbic acid].content_text",C['Ascorbic acid'],'content_text',"과육 127.8 mg/100 g, 껍질 184.8 mg/100 g; 다른 보고는 과육 9.5 ± 0.8 mg/100 g(생중량) 등으로 차이가 큼(리뷰 정리값)[2]","리뷰 본문 대표값 과육 127.8 mg/100 g, 껍질 184.8 mg/100 g(생/건 기준 미기재); 같은 리뷰 표의 다른 보고는 과육 9.5 ± 0.8 mg/100 g(생중량), 5.60 mg/100 g, 동결건조 과육 92 mg/100 g(건물) 등으로 기준과 값이 크게 다름[2]","[2] 표 대조: 127.8·184.8 은 기준 표기 없음, 동결건조 과육(건물)도 92 mg/100 g 이어서 127.8 을 생과육 값으로 읽으면 안 됨")
for n in d['nutrients']:
    for it in n['items']:
        if it['name']=='비타민 C':
            it['name']='비타민 C(리뷰 본문값, 생/건 기준 미기재; 다른 보고 9.5 mg/100 g 생중량)'
            changes.append({"where":"nutrients[과육].비타민 C","before":"비타민 C 127.8 mg/100 g","after":"이름에 기준 미기재·다른 보고값 표시","why":"[2] 표에서 같은 성분 값이 5.6–127.8 mg/100 g 으로 기준이 섞여 있음"})
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('/home/user/hfoodguide-wave3/docs/materials/eugenia-stipitata/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
