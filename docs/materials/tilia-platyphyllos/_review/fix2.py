import json
p='dossier.json'; d=json.load(open(p)); ch=json.load(open('_review/changes.json'))
def R(where,o,k,old,new,why):
    assert old in o[k],(where,old); o[k]=o[k].replace(old,new); ch.append({"where":where,"before":old,"after":new,"why":why})
why='[6] 초록에서 학명 이탤릭이 빠져 "flowers 와 flowers, bracts, and leaves" 중 어느 쪽이 이 종인지 알 수 없음 — 이 종 꽃·포엽·잎 정량으로 단정하지 않음'
c=[x for x in d['compounds'] if x['name']=='Tiliine A'][0]
R('compounds.Tiliine A.content_text',c,'content_text','이 종 꽃·포엽·잎에서 HPLC-ESI-qTOF로 정량','이 종과 작은잎라임 꽃에서 HPLC-ESI-qTOF로 정량(한 종은 포엽·잎까지 분석했으나 초록에서 어느 종인지 확인 못함)',why)
c['part']='꽃(포엽·잎은 종 대응 미확인)'
a=[x for x in d['assays'] if x['compound']=='Tiliine A'][0]
R('assays.Tiliine A.content',a,'content','6가지 알칼로이드가 이 종 꽃·포엽·잎에서 모두 검출','6가지 알칼로이드가 이 종과 작은잎라임 꽃에서 모두 검출(포엽·잎 분석 자료의 종 대응은 초록에서 확인 못함)',why)
a['part']='꽃(포엽·잎은 종 대응 미확인)'
R('assays.Tiliine A.rationale',a,'rationale','피나무속 꽃·잎에서 처음 보고된 고유 알칼로이드로, 잎(식품 사용가능부위)까지 정량한 드문 자료다; 전문 확인 못함[6].','피나무속 꽃에서 처음 보고된 고유 알칼로이드다; 잎까지 정량한 자료가 이 종인지는 전문을 확인하지 못해 단정하지 않는다[6].',why)
t=[x for x in d['compounds'] if x['name']=='Tilacetine A'][0]; t['part']='꽃(포엽·잎은 종 대응 미확인)'
S={s['key']:s for s in d['sections']}
R('sections.safety',S['safety'],'body','꽃·포엽·잎에서 새 알칼로이드가 보고되었지만','이 종과 작은잎라임의 꽃 등에서 새 알칼로이드가 보고되었지만',why)
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1); json.dump(ch,open('_review/changes.json','w'),ensure_ascii=False,indent=1); print(len(ch))
