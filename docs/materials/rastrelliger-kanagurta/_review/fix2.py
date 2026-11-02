import json
P='dossier.json'; d=json.load(open(P)); ch=json.load(open('_review/changes.json'))
S={s['key']:s for s in d['sections']}
def rep(k,old,new,why):
    b=S[k]['body']; assert old in b,old; S[k]['body']=b.replace(old,new); ch.append({"where":"sections."+k,"before":old,"after":new,"why":why})
rep('related_species',"짧은고등어가 한 무리로","R. brachysoma가 한 무리로","출처 없는 국문명 제거")
rep('related_species'," 'sp.'로만 적혀 종을 확정할 수 없는 자료(예: 베트남 히스타민 연구)는 이 문서에 넣지 않았다.","","출처 없는 메타 문장 제거(종 미확정 자료 [23]은 삭제됨)")
rep('safety',"고등어과 생선이라 상온에 두면 히스타민이 생긴다: 갓 잡은 살에서는 히스타민이 검출되지 않았으나 0–23 °C 저장 중 모두 늘었고 23 °C에서 가장 빨랐다[17].",
 "고등어과 생선이라 저장 중 히스타민이 생긴다: 갓 잡은 살에서는 히스타민이 검출되지 않았으나 0–23 °C 저장 중 모두 유의하게 늘었고 특히 23 °C에서 두드러졌다[17].",
 "[17] 초록: 0·3·10·23 °C 모두 증가, 'especially at 23°C' — '상온에서만'·'가장 빨랐다'로 좁히지 않음")
json.dump(d,open(P,'w'),ensure_ascii=False,indent=1); json.dump(ch,open('_review/changes.json','w'),ensure_ascii=False,indent=1); print(len(ch))
