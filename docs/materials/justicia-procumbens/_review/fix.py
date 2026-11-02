import json
p='dossier.json'; d=json.load(open(p))
S={s['key']:s for s in d['sections']}
ch=[]
def rep(where,obj,key,old,new,why):
    assert old in obj[key], (where,old)
    obj[key]=obj[key].replace(old,new); ch.append({"where":where,"before":old,"after":new,"why":why})
rep('sections.overview',S['overview'],'body','2020년 논문 시점에 임상 1상을 마무리하는 단계로 소개되었다[3, 15].','2020년 논문 시점에 임상 1상을 마무리하는 단계로 소개되었다[3].','[15](2018) 전문에는 임상 1상 언급이 없고 [3](2020) 서론·초록에만 있음')
rep('sections.history',S['history'],'body','1977년판 중국약전에 수재되었다[7, 8].','1977년판 중국약전에 수재되었다[7].','1977년판 중국약전 수재는 [7] 전문에서 확인, [8] 초록에는 없음')
rep('sections.biology',S['biology'],'body','잎은 타원상 긴 타원형이며 가장자리가 밋밋하고, 맛은 담백하다[8].','잎은 긴 타원형으로 가장자리가 밋밋하고(말린 약재에서는 쭈글쭈글하게 말림), 맛은 거의 없다[8].','[8] 초록: oblong leaves with full margin, wrinkled and bent; herbs are tasteless')
rep('sections.biology',S['biology'],'body','줄기와 잎에는 긴 타원형·막대 모양의 탄산칼슘 결정(종유체)이 많아, 비슷한 쥐꼬리망초과 약재와 구별하는 데 쓰인다[8].','줄기와 잎에는 긴 타원형·막대 모양의 탄산칼슘 결정(종유체)이 많으며, 이런 외형·현미경 특징을 약재 감별(품질 확인)에 쓸 수 있다고 제안되었다[8].','[8] 초록은 품질 감별에 쓸 수 있다고만 하고 다른 쥐꼬리망초과 약재와의 비교는 없음')
rep('sections.related_species',S['related_species'],'body','같은 과(쥐꼬리망초과)에서는 Asteracantha longifolia의 잎','같은 과(쥐꼬리망초과)에서는 예컨대 Asteracantha longifolia의 잎','I1020 원자료에 같은 과로 분류되기도 하는 다른 원료(Avicennia 등)도 있어 \'유일\'로 읽히지 않게 함')
rep('sections.safety',S['safety'],'body','따라서 광산·오염 토양 주변에서 채취한 잎은 중금속 위험이 있다[11].','이 값은 잎만이 아닌 지상부 전체의 측정값이지만, 광산·오염 토양 주변에서 채취한 원료는 중금속 오염 위험을 염두에 두어야 한다[11].','[11]은 지상부(shoot) 측정 — 잎 결과로 단정하지 않게 고침')
C={c['name']:c for c in d['compounds']}
rep('compounds.Chinensinaphthol methyl ether',C['Chinensinaphthol methyl ether'],'activity_ko','혈소판 응집 억제(시험관·동물)[5, 6]','사람·랫드 혈소판 응집 억제(시험관)[5, 6] — 랫드 혈전 시험은 이 성분 단독이 아닌 활성 분획으로 수행[6]','[6] 전문: 동물(FeCl3 경동맥 혈전) 시험은 활성 분획 투여, CME 는 시험관 혈소판 응집 시험만')
rep('compounds.Secoisolariciresinol dimethyl ether',C['Secoisolariciresinol dimethyl ether'],'activity_ko','전초에서 다이아릴뷰테인 리그난 9종과 함께 분리[26]','전초에서 분리된 다이아릴뷰테인 리그난 9종 가운데 하나(이 논문에서 활성 시험 없음)[26]','[26] 초록: 9종(신규 6·기지 3) 중 하나이며 활성 평가 없음')
rep('compounds.Diphyllin',C['Diphyllin'],'activity_ko','HIV-1 억제 IC50 0.38 µmol/L(세포)[33]','HIV-1 억제 IC50 0.38 µmol/L(세포, 선택지수 5.3으로 낮음)[33]','[33] 초록의 SI 5.3 을 함께 적어 세포 결과 과장을 막음')
src=d['sources'][19]
assert src['n']==20
rep('sources[20]',src,'title','Phytomedicine 2024. doi','Phytomedicine 2024;134:156014. doi','PubMed 서지 권·쪽 보충')
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(ch,open('_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(ch))
