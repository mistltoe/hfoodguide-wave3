import json,sys
p=sys.argv[1]
d=json.load(open(p))
S={s['key']:s for s in d['sections']}
ch=[]
def rep(key,old,new,why):
    b=S[key]['body']; assert old in b,(key,old); S[key]['body']=b.replace(old,new); ch.append({"where":f"sections.{key}","before":old,"after":new,"why":why})
rep('overview',"건강기능식품 고시형 원료의 원재료가 아니어서 식약처가 정한 지표성분은 없다[1].",
 "이번 조사에서 이 종을 원재료로 하는 건강기능식품 고시형 원료는 확인하지 못해 지표성분은 비워 두었다.",
 "[1] 식품원료 목록(I1020)은 건강기능식품 고시 여부를 말하지 않음")
rep('overview',"11개국 시장의 장어 제품 279점을 DNA로 판별한 연구에서",
 "11개 국가·지역 시장에서 모은 장어 제품 282점 중 종까지 판별된 279점을 분석한 연구에서",
 "[2] 원문: 282점 수집, 279점 판별, 11 countries/regions")
rep('history',"2025년 CITES 제20차 당사국총회에서 Anguilla속 전 종을 부속서 II에 올리자는 유럽연합 제안이 부결되었다는 보도가 있으나, 이는 검색 요약으로만 확인했고 CITES 공식 기록은 확인하지 못함[29]. 따라서 이 종 자체의 CITES 부속서 등재는 이번 조사에서 확인하지 못함.",
 "2025년 11월 CITES 제20차 당사국총회에서 이 종을 포함한 Anguilla속 전 종을 부속서 II에 올리자는 유럽연합 등의 제안이 비밀투표로 부결되었다고 여러 언론이 보도했다[29]. 이 보도들에 따르면 현재 CITES 부속서에 오른 장어는 유럽뱀장어뿐이고 이 종은 오르지 않았지만, CITES 공식 기록·부속서 원문은 이번 조사에서 열지 못해 확인하지 못함.",
 "검색 결과 여러 보도가 제안(이 종 포함) 부결과 유럽뱀장어만 등재된 상태를 전함; 공식 기록은 열지 못해 보도 수준으로 명시")
rep('cultivation',"중국 장어 양식 생산의 74%를 이 종이 차지한다고 보고되었다[22].",
 "중국 장어 양식 생산의 74%를 이 종이 차지한다는 선행 자료가 인용되었다[22].",
 "[22] 전문 서론에서 다른 문헌을 인용한 값(원 자료 아님)")
rep('cultivation',"출혈성 아가미 괴사병 시료에서는 새 오르토레오바이러스가 분리되었고 양식 개체의 감염률은 32.3%였다[19].",
 "출혈성 아가미 괴사병 시료에서는 새 오르토레오바이러스가 분리되었고 양식 개체 조사에서 32.3%가 양성이었지만, 복강 감염 실험에서는 뚜렷한 증상을 일으키지 않아 2차 감염원일 가능성이 제시되었다[19].",
 "[19] 초록: 감염 실험에서 병원성 미관찰, 1차 병원체 아닐 수 있음 — 과장 방지")
d['compounds']=[c for c in d['compounds']]
for c in d['compounds']:
    if c['name']=='Cadmium':
        o=c['activity_ko']; c['activity_ko']="가장 오염된 지점에서 장어 자체의 건강에 위험이 될 수 있다고 평가됨(사람 섭취 기준 아님)[9]"
        ch.append({"where":"compounds.Cadmium.activity_ko","before":o,"after":c['activity_ko'],"why":"[9] 은 장어(eel) 건강 위험을 말함"})
a=d['assays'][0]['conditions']
for k,new in [('instrument',"EOF: 연소 이온크로마토그래피(CIC, 실험실별 기기, 세부는 보충자료); PFAS: 삼중사중극자 LC-MS/MS(실험실별 3개 기종)"),
              ('sample_prep',a['sample_prep'].replace("ENVI-carb 정제","흑연화 탄소 흡착제 정제")),
              ('standard',"유기불소 회수 시험용 24종 PFAS 표준 혼합물, 무기불소 제거 시험용 불화나트륨")]:
    ch.append({"where":f"assays[0].conditions.{k}","before":a[k],"after":new,"why":"상표·제품명 대신 일반명(원문 내용은 [13] 전문 Methods와 일치)"}); a[k]=new
s29=d['sources'][28]
o=s29['title']
s29['title']="CITES committee rejects EU bid to list all eel species in Appendix II (2025-11-27 보도) — WebSearch 검색 요약으로 확인(같은 결과를 전한 다른 보도 다수), 원문·CITES 공식 기록은 열지 못함"
ch.append({"where":"sources[29].title","before":o,"after":s29['title'],"why":"검색 재확인 내용 반영"})
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(ch,open('_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(ch))
