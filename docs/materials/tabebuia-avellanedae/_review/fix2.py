import json,sys
p=sys.argv[1]; d=json.load(open(p,encoding='utf-8')); S={s['key']:s for s in d['sections']}
ch=json.load(open(p.replace('dossier.json','_review/changes.json'),encoding='utf-8'))
def rep(k,o,n,why=None):
    assert o in S[k]['body'],(k,o[:30]); S[k]['body']=S[k]['body'].replace(o,n)
    if why: ch.append({"where":f"sections.{k}","before":o,"after":n,"why":why})
rep('safety'," 12명 중 9명이 끝까지 참여했고, 2명은 견디기 어렵다며 중도 탈락했다[22].","")
rep('safety'," 타히보는 식품으로 흔히 먹는 채소·과일이 아니므로 식품 영양성분표 값은 해당 없음(빈 목록)이다[1].","","[1] 은 영양성분표 해당 여부를 말하지 않음")
rep('safety',"검출되지 않거나 매우 낮다는 보고가 있어, 독성은 제품의 성분 조성에 따라 다르다[5, 4].","이 분석 조건에서 검출되지 않았다는 보고가 있으나(검출한계 미만일 수 있음), 원료 품질과 조성이 제각각이라 제품별 위험은 다를 수 있다[5, 4].","[5] 는 '미검출이 부재를 뜻하지 않는다'고 씀 — 단정 완화")
rep('safety',"라파콜의 독성 근거는 순수 라파콜을 쥐에게 먹인 실험 자료이며, 사람에서 같은 독성이 확인된 것은 아니다[4, 24].","라파콜의 독성 근거는 순수 라파콜을 쥐에게 먹인 실험이며 사람 자료는 아니다[11, 24].")
rep('overview',"(학명 Tabebuia avellanedae)","")
rep('overview'," 사람에서 확인된 독성 근거는 아니지만, 임신부와 항응고제 복용자에게는 주의가 안내된다[12]."," 동물 결과이지만 임신부와 항응고제 복용자에게는 주의가 안내된다[12].")
rep('processing'," 이는 동물·세포 결과와 별개로 제품 시장 규모를 보여 주는 값이다[19].","")
json.dump(d,open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
json.dump(ch,open(p.replace('dossier.json','_review/changes.json'),'w',encoding='utf-8'),ensure_ascii=False,indent=1)
for s in d['sections']: print(s['key'],len(s['body']))
