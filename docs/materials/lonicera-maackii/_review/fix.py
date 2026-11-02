import json
p='/home/user/hfoodguide-wave3/docs/materials/lonicera-maackii/dossier.json'
d=json.load(open(p))
S={s['key']:s for s in d['sections']}
changes=[]
def rep(key,old,new,why):
    b=S[key]['body']; assert old in b,(key,old)
    S[key]['body']=b.replace(old,new); changes.append({"where":f"sections.{key}","before":old,"after":new,"why":why})
rep('overview',"중국에서는 약용·관상·녹화 식물로 쓰이고, 추출물의 항균·항산화·항염 등 작용이 보고되었으나 대부분 실험실·동물 수준의 근거다[2].",
 "중국에서는 약용·관상·녹화 식물로 쓰이고, 2025년 리뷰는 추출물의 항균·항종양·항산화·항염 등 작용을 정리했으나 초록에서는 사용 부위와 연구 수준(세포·동물·사람)을 확인하지 못함[2].",
 "[2] 초록은 'extract' 의 활성만 나열 — '대부분 실험실·동물 수준'은 초록에 없는 판단이므로 확인 불가로 바꿈")
rep('history',"괴불나무의 학명은 Lonicera maackii (Rupr.) Maxim.이며, 처음에는 다른 속명으로 기재되었다가 인동속으로 옮겨졌고 Caprifolium maackii (Rupr.) Kuntze라는 이명도 있다[1].",
 "괴불나무의 학명은 Lonicera maackii (Rupr.) Maxim.이며, 식약처 목록에는 Caprifolium maackii (Rupr.) Kuntze라는 이명 학명도 함께 적혀 있다[1].",
 "[1](I1020 행)은 학명·이명만 적음 — '처음 다른 속명으로 기재되었다가 옮겨짐'(기재 이력)은 출처에 없음")
rep('related_species',"흔히 하스카프·허니베리로 불리는 푸른 열매","같은 목록의 개별인정 행에 '허니베리'로도 적힌 열매",
 "I1020 원자료에는 '허니베리'만 있고 '하스카프'는 없음 — 상표·통칭은 출처 범위로 줄임")
rep('cultivation',"2주 동안 잎 면적당 2.0 g/m²의 먼지를","2주 동안 2.0 g/m²의 먼지를",
 "[22] 영문 초록은 '2.0 g·m-2 after 2 weeks'만 씀 — '잎 면적당'은 초록에 없음")
rep('cultivation'," 북미 온실 실험에서는 극한 저온을 겪은 뒤에도 괴불나무를 포함한 비원산 수종들의 평균 실생 정착률이 원산 수종보다 약 4배 높았다[23].","",
 "[23] 수치는 맞으나 비원산 수종 묶음 평균값이고 북미 침입 생태 연구라 지시(침입 생태는 짧게)에 따라 뺌")
rep('cultivation',"사슴과 진드기 매개 감염병 위험을 높인다는","사슴이 침입지를 더 자주 이용하게 해 진드기 매개 감염병(에를리키아증) 노출 위험을 높인다는",
 "[12] 초록: 침입지에서 흰꼬리사슴 이용이 늘어 병원체 보유 진드기가 많아짐 — '사슴과 … 위험'은 뜻이 모호해 원문대로 고침")
rep('processing'," 줄기 목부와 뿌리껍질 추출물은 유방암 세포와 생쥐 이식 종양 실험에 쓰였지만, 이 부위들은 국내 식품원료 사용 부위가 아니다[1, 15].","",
 "[15](PMID 37924601)는 PubMed 에 'Retracted Publication'으로 표시된 철회 논문 — 근거로 쓰지 않음(안전성 절에 철회 사실만 남김)")
rep('safety',"줄기 목부·뿌리껍질 추출물의 항암 세포·동물 실험 결과는 식용 부위가 아닌 부위의 전임상 결과이므로 효능 근거로 확대해서는 안 된다[15].",
 "줄기 목부·뿌리껍질 추출물의 유방암 세포·생쥐 실험 논문은 이후 철회되었으며, 그 부위도 식용 부위가 아니므로 근거로 쓰지 않는다[1, 15].",
 "[15] 철회 논문 — 철회 사실을 밝히고 효능 근거에서 제외")
rep('safety',"2025년 리뷰가 정리한 항균·항종양·간 보호·혈당 강하 작용도 주로 추출물 실험 결과다[2].",
 "2025년 리뷰가 정리한 항균·항종양·간 보호·혈당 강하 작용은 추출물 연구로 정리되어 있으며, 초록에서는 부위와 연구 수준을 확인하지 못함[2].",
 "[2] 초록은 'extract' 라고만 하고 실험 종류를 밝히지 않음")
# compounds
for c in d['compounds']:
    if c['name']=='Lonicerin':
        old=c['activity_ko']; c['activity_ko']="생리활성 근거 확인하지 못함[3]"
        changes.append({"where":"compounds.Lonicerin.activity_ko","before":old,"after":c['activity_ko'],"why":"[3] 전문에 '인동속 특징 성분'이라는 설명 없음"})
    if c['name']=='Cyanidin':
        old=c['content_text']; c['content_text']="시아니딘류(유도체 포함) 3종이 검출됨(정량값 없음)[3]"
        changes.append({"where":"compounds.Cyanidin.content_text","before":old,"after":c['content_text'],"why":"[3] 은 'three cyanidins and derivatives' — 시아니딘 외 3종이 아니라 합쳐서 3종"})
# source 15 title
for s in d['sources']:
    if s['n']==15:
        old=s['title']; s['title']=old.replace("(초록 확인;","(PubMed 에 철회 논문(Retracted Publication)으로 표시; 초록 확인;")
        changes.append({"where":"sources[15].title","before":old,"after":s['title'],"why":"철회 표시 추가"})
    if s['n']==23: pass
d['sources']=[s for s in d['sources'] if s['n']!=23]
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('/home/user/hfoodguide-wave3/docs/materials/lonicera-maackii/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
