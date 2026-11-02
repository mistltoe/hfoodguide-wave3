import json,re
p='dossier.json'; d=json.load(open(p))
S={s['key']:s for s in d['sections']}
changes=[]
def rep(key,old,new,why):
    b=S[key]['body']; assert old in b,(key,old[:30]); S[key]['body']=b.replace(old,new)
    changes.append({"where":f"sections.{key}","before":old,"after":new,"why":why})
rep('history',"유럽 연구진은 나무와 껍질의 물 추출물이 한의학·중의학에서 염증과 만성 간 질환에 쓰인다고 소개하며 이 추출물을 간 세포 실험에 썼다[23, 24].",
 "한 연구는 나무와 껍질의 물 추출물이 중의학·한의학에서 염증과 간세포암을 포함한 만성 간 질환에 쓰인다고 소개하며 이 추출물을 사람 간암 세포 실험에 썼다[24]. 같은 연구진의 앞선 간 성상세포 연구는 한국에서 생강나무 추출물이 염증·혈액순환·간 손상 예방에 수 세기 동안 쓰였다고 소개했으나, 초록에 원료 부위는 적혀 있지 않다[23].",
 "[24] 초록만 '나무와 껍질(wood and bark)'을 적고 [23] 초록에는 부위가 없음; '유럽 연구진'은 초록으로 확인되지 않는 표현")
rep('history',"식약처 목록이 다른 이름으로 '동백나무'·'개동백나무'를 적고 있어, 이 나무를 지역에서 동백이라 불러 온 것을 알 수 있다[1].",
 "식약처 목록에는 다른 이름으로 '동백나무'·'개동백나무'가 적혀 있으나[1], 이 이름이 쓰인 지역과 유래는 확인하지 못함.",
 "목록 행은 다른 이름만 적을 뿐 '지역에서 불러 왔다'는 내용은 없음(추론)")
rep('related_species'," 생강나무 꽃은 꽃자루 없이 가지에 붙어 피고 산수유 꽃은 꽃자루가 길다는 구별법이 서울시 자료에 소개되어 있다(웹 검색 요약으로만 확인)[33].",
 " 두 꽃의 형태 구별법은 공식 원문을 열어 확인하지 못함.",
 "[33] 은 원문을 열지 못하고 WebSearch 요약으로만 본 출처라 근거로 쓸 수 없어 문장과 출처를 지움")
rep('safety',"잎 추출물은 쥐 혈소판 실험에서 응집을 억제했고, 쥐에게 200·400 mg/kg을 5일 먹였을 때도 혈소판 응집이 줄었지만 혈액 응고 시간(PT·aPTT)은 바뀌지 않았다[5].",
 "잎 추출물은 쥐(랫드) 혈소판 실험에서 응집을 억제했고, 랫드에 100·200·400 mg/kg을 5일 먹인 뒤 채혈한 혈소판에서도 응집이 억제되었다[5]. 쥐 혈장에 추출물을 직접 넣은 시험에서 혈액 응고 시간(PT·aPTT)은 바뀌지 않았다[5].",
 "[5] 전문: 경구 투여군은 100·200·400 mg/kg(5일)이고, PT·aPTT 는 투여 동물이 아니라 혈장에 추출물을 넣은 시험관 시험이었음")
rep('safety',"간 보호·혈관·항비만·항우울 등 보고된 효과는 모두 세포 또는 동물 실험이며 사람 임상 근거는 확인하지 못함[23, 25, 26, 27, 28, 29, 30, 31, 35].",
 "그 밖에 보고된 효과도 모두 세포 또는 동물 실험이며 사람 임상 근거는 확인하지 못함. 혈관 보호·혈압·당뇨 생쥐 연구[25, 26, 27]와 아토피 피부염 모델 연구[30]는 식품원료 사용 부위가 아닌 줄기(가지) 추출물을 썼고, 간 성상세포·간암 세포·지방세포 연구[23, 24, 35]는 나무·껍질 물 추출물이거나 초록에 부위가 없다. 잎 추출물로 한 연구는 지방간 생쥐 모델[31] 등이며, 항우울 동물 실험[28]과 비만세포 알레르기 실험[29]은 원료 부위를 확인하지 못함.",
 "줄기·목재 연구가 부위 구분 없이 묶여 잎·꽃 효과처럼 읽힘: [25][26][27][30] 은 줄기, [31] 은 잎, [24] 는 나무·껍질, [23][28][29][35→34] 는 부위 미기재(전문·초록 대조)")
for c in d['compounds']:
    if c['name']=='Secolincomolide A':
        changes.append({"where":"compounds.Secolincomolide A.part","before":c['part'],"after":"줄기(식품원료 사용 부위 아님)","why":"[14] 전문 Plant Material: 줄기(stems)에서 분리"})
        c['part']="줄기(식품원료 사용 부위 아님)"
        c['activity_ko']="줄기 메탄올 추출물에서 분리; 토끼 혈소판의 콜라겐 유도 응집 억제(세포 밖 시험), 동물 모델에서 출혈 시간 연장[14]"
    if c['name']=='Quercitrin':
        old=c['activity_ko']
        c['activity_ko']="잎 추출물의 주요 성분으로 여러 연구에서 확인[4, 5, 6]; 원료 부위가 초록에 없는 추출물에서 분리한 성분이 DPPH 소거(시험관)와 B16F10 세포 멜라닌 생성 억제(세포 실험)를 보임[8]"
        changes.append({"where":"compounds.Quercitrin.activity_ko","before":old,"after":c['activity_ko'],"why":"DPPH 는 세포 실험이 아님; [8] 초록에 원료 부위 없음"})
    if c['name']=='Afzelin':
        old=c['activity_ko']
        c['activity_ko']="퀘르시트린과 함께 잎 추출물의 주요 성분[4, 5]; 분리 성분이 DPPH·FRAP 항산화 시험(시험관)에서 활성[8]"
        c['source']=[4,5,7,8]
        changes.append({"where":"compounds.Afzelin.activity_ko","before":old,"after":c['activity_ko'],"why":"[5] 는 아프젤린의 활성을 시험하지 않음(전문: 성분 활성 미시험)"})
old=list(d['aliases'])
d['aliases']=[a if a!='동백나무(이명)' else '동백나무' for a in d['aliases']]
changes.append({"where":"aliases","before":"동백나무(이명)","after":"동백나무","why":"[1] 에서는 학명 이명이 아니라 다른 이름(RAWMTRL_NCKNM)"})
# drop source 33, renumber 34->33, 35->34
mp={i:i for i in range(1,33)}; mp[34]=33; mp[35]=34
def rn(txt):
    def f(m):
        nums=[int(x) for x in re.split(r',\s*',m.group(1))]
        return '['+', '.join(str(mp[n]) for n in nums)+']'
    return re.sub(r'\[(\d+(?:,\s*\d+)*)\]',f,txt)
# careful: safety new text already uses 34 meaning old 35 -> write it as old number first
for s in d['sections']: s['body']=rn(s['body'])
for c in d['compounds']:
    for k in ('content_text','activity_ko'): c[k]=rn(c[k])
    c['source']=[mp[x] for x in c['source']]
for a in d['assays']:
    a['content']=rn(a['content']); a['rationale']=rn(a['rationale']); a['source']=[mp[x] for x in a['source']]
d['sources']=[s for s in d['sources'] if s['n']!=33]
for s in d['sources']: s['n']=mp[s['n']]
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
