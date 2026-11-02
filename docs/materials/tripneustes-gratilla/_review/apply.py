import json,sys
p=sys.argv[1]
d=json.load(open(p))
S={s['key']:s for s in d['sections']}
changes=[]
def rep(key,old,new,why):
    b=S[key]['body']
    assert b.count(old)==1,(key,old)
    S[key]['body']=b.replace(old,new); changes.append({"where":f"sections.{key}","before":old,"after":new,"why":why})

rep('biology',"이 종은 해조류와 해초를 주로 뜯어 먹는 초식자로, 산호초와 해초밭 생태계에서 핵심종으로 다뤄진다[5].",
 "이 종은 해조류와 해초를 주로 뜯어 먹는 초식자로, 원문은 이 속이 특히 해초밭 서식처에서 일차 초식자로서 핵심종인 경우가 많다고 인용했다[5].",
 "[5] 원문은 해초밭(sea grass habitats)에서 핵심종이라고 했고 산호초는 언급하지 않음")
rep('biology',"하와이 개체를 조사한 원문은 체벽 염증과 궤양으로 대량 폐사한 사례를 보고했으나 원인은 밝히지 못했다[33].",
 "하와이에서 침입 해조류 방제용으로 옮겨 놓은 개체의 대량 폐사를 병리 조사한 원문은 껍데기(test) 염증과 표피 궤양에 이어 체강액을 유지하지 못해 죽은 것으로 보았으나 근본 원인은 밝히지 못했다[33].",
 "[33] 초록: inflammation of the test and epidermal ulceration, 옮겨 놓은(translocated) 개체")
rep('history',"국내에서는 2008년 한국어 논문이 이 종을 제주 서귀포 앞바다(수심 약 25 m)에서 채집해 속(Tripneustes)까지 포함한 국내 첫 기록으로 보고했다는 내용을 웹 검색 요약으로만 확인했으며, 원문은 확인하지 못함[34].",
 "국내에서는 2008년 한국동물분류학회지(24권 3호)에 실린 논문이 2008년 4월 제주 서귀포 문섬 부근 수심 약 25 m 암반에서 잡은 1개체로 이 종을 국내 미기록종으로 보고하고, 속명 '흰수염성게속'과 종명 '흰수염성게'를 새 이름(신칭)으로 붙였다는 내용을 웹 검색 요약으로만 확인했으며, 원문은 열어 보지 못함[34].",
 "WebSearch 요약으로 학술지·권호·채집 정보·신칭 여부 보강(원문 접근 불가 — koreascience 허용 목록 밖)")
rep('related_species',"목록상 국문명 '흰수염성게'의 유래를 설명한 공공기관 자료는 확인하지 못함.",
 "국문명 '흰수염성게'는 2008년 국내 첫 기록 논문이 새 이름(신칭)으로 제안한 것이라는 내용을 웹 검색 요약으로만 확인했고(원문 미확인)[34], 식약처 목록이 이 이름을 쓴 근거를 설명한 공공기관 자료는 확인하지 못함.",
 "국문명 유래 근거를 [34] 웹 검색 요약으로 보강(약하게 표기)")
old_s=S['safety']['body'].split("\n\n")[0]
new_s=("이 종을 먹을 때 보고된 가장 뚜렷한 위험은 시가테라 독소 축적이다[5]. 2015년 4월과 7월 프랑스령 폴리네시아 누쿠히바섬 아나호만에서 잡은 이 성게의 날 생식소를 먹은 3명이 1시간 안에 메스꺼움·구토·설사를 겪고, 찬 것에 닿을 때의 통증·손발 저림 같은 신경 증상을 보였다[5]. 환자가 먹은 개체는 분석하지 못했지만, 같은 만에서 2015년 7월에 잡아 모은 개체의 전체 조직에서 태평양 시가톡신 총량이 생물 무게 기준 세포시험(CBA-N2a)으로 20.19 ng P-CTX-3C 당량/g, LC-MS/MS로 21.5 ng P-CTX-3C 당량/g이었다[5]. "
 "원문은 이 값(약 20 ng P-CTX-3C 당량/g)이 미국 FDA·EFSA 권고 안전 수준(0.01 ng P-CTX-1B 당량/g)보다 훨씬 높다고 했다[5]. 다만 두 값은 기준 독소가 달라(P-CTX-3C 당량과 P-CTX-1B 당량) 숫자를 그대로 나누어 배수를 매길 수는 없고, 원문은 독성등가계수(TEF)로 P-CTX-1B 당량으로 바꿀 수 있다고만 적었다[5]. "
 "16개월 뒤인 2016년 11월 시료는 0.32 ng(세포시험)·1.48 ng(LC-MS/MS) P-CTX-3C 당량/g으로 줄었지만 원문은 여전히 안전 수준을 넘었다고 보았다[5]. 이 연구는 생식소와 다른 조직 사이의 독소 분포는 조사하지 않았다[5].")
rep('safety',old_s,new_s,"측정법별 값(20.19·21.5)·생물 무게 기준·기준 독소 차이(P-CTX-3C vs P-CTX-1B 당량)를 원문대로 밝히고 '가장 중요한' 단정 완화; 조직 분포 미조사 명시")
rep('safety',"이 성게는 크롬 16.98 µg/g, 납 4.80 µg/g으로 높은 축적을 보였고,",
 "이 성게는 크롬 16.98 µg/g, 납 4.80 µg/g으로 높은 축적을 보였고(부위와 생·건 무게 기준은 초록에 없음),",
 "[11] 초록에 부위·건/생 기준이 없음을 명시")
rep('safety',"날 생식소를 먹는 경우 시가테라가 잦은 열대 해역 개체는 피하라는 경고가 원문에 있다[5].",
 "원문은 시가테라가 잦은 해역에서는 성게 생식소를 먹는 것이 큰 위험이라고 결론짓고, 주민과 방문객에게 이 위험을 알리는 교육이 필요하다고 했다[5].",
 "[5] 원문은 '피하라'는 경고가 아니라 위험·교육 필요를 말함")
for c in d['compounds']:
    if c['name']=="Ciguatoxin P-CTX-3B":
        b=dict(c)
        c['content_text']="2015년 7월 시료 독소 조성의 44%(LC-MS/MS); 총량 21.5 ng P-CTX-3C 당량/g(생물 무게 기준)"
        c['activity_ko']="와편모조류 Gambierdiscus 에서 먹이사슬로 옮겨 온 독소로, 원문은 이 성게로 인한 시가테라 유사 중독의 원인 독소로 보았다(환자가 먹은 개체 자체는 분석하지 못함)[5]"
        changes.append({"where":"compounds[P-CTX-3B]","before":b['content_text']+" / "+b['activity_ko'],"after":c['content_text']+" / "+c['activity_ko'],"why":"생물 무게 기준 명시, '확인되었다' 과장 완화"})
    if c['name']=="Ciguatoxin P-CTX-3C":
        b=c['content_text']
        c['content_text']="2015년 7월 조성의 20%, 2016년 11월 58%; 총량 1.48 ng P-CTX-3C 당량/g(2016년 11월, LC-MS/MS, 생물 무게 기준)"
        changes.append({"where":"compounds[P-CTX-3C]","before":b,"after":c['content_text'],"why":"생물 무게 기준 명시"})
for a in d['assays']:
    if a['compound'].startswith("Pacific ciguatoxins"):
        b=a['part']+" / "+a['content']
        a['part']="전체 조직(동결건조 후 추출, 결과는 생물 무게 기준)"
        a['content']="21.5 ng P-CTX-3C 당량/g(2015년 7월), 1.48 ng P-CTX-3C 당량/g(2016년 11월), 생물 무게 기준"
        changes.append({"where":"assays[ciguatoxins]","before":b,"after":a['part']+" / "+a['content'],"why":"원문 Methods: P-CTX-3C equiv./g wet weight of tissue"})
for s in d['sources']:
    if s['n']==34:
        b=s['title']
        s['title']="A New Record of Sea Urchin (Echinoidea: Echinoida) from Jejudo Island, Korea. 한국동물분류학회지(Korean Journal of Systematic Zoology) 2008;24(3):323-326 — 웹 검색 요약으로만 확인, 원문 미확인"
        s['url']="https://koreascience.kr/article/JAKO200801440597419.do"
        s['accessed']="2026-11-02"
        changes.append({"where":"sources[34]","before":b,"after":s['title'],"why":"WebSearch 결과로 학술지·권호·쪽 보강, 원문 미열람 표기 유지"})
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open(p.replace('dossier.json','_review/changes.json'),'w'),ensure_ascii=False,indent=1)
print(len(changes))
