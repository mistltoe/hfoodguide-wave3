import json,re,sys
P='/home/user/hfoodguide-wave3/docs/materials/allomyrina-dichotoma/dossier.json'
d=json.load(open(P))
S={s['key']:s for s in d['sections']}
changes=[]
def rep(key,old,new,why):
    b=S[key]['body']; assert old in b,(key,old); S[key]['body']=b.replace(old,new); changes.append({'where':f'sections.{key}','before':old,'after':new,'why':why})
rep('history',"정부 보도자료 검색 요약에 따르면 이 유충은 2015년 한시적 식품원료로 인정되었고, 2016년 「식품의 기준 및 규격」 개정안 행정예고로 인정받은 업체 외 모든 영업자가 쓸 수 있는 원료로 확대되었다(원문은 열지 못함)[27, 29, 34]. 농촌진흥청은 이 유충에 '장수애'라는 애칭을 붙였다는 보도자료 제목이 확인된다(본문은 열지 못함)[28]. 한시적 인정일·식품공전 고시일의 공식 원문은 확인하지 못함.",
 "정부 보도자료 제목과 검색 결과로는 이 유충이 2015년 무렵 한시적 식품원료로 인정된 뒤 모든 영업자가 쓸 수 있는 원료로 확대된 것으로 보이나, 보도자료 원문을 열지 못해 인정일·「식품의 기준 및 규격」 고시일과 절차는 확인하지 못함[27]. 현재는 식약처 「식품원료 목록」에 사용가능 원료로 실려 있다[1].",
 "[27]·[28]·[29]·[34]는 원문을 열지 못하고 검색 요약으로만 본 출처라 날짜·연도(2016년 행정예고 등)와 애칭을 단정할 수 없음 — 한 문장으로 약화하고 [28]·[29]·[34] 삭제, 현재 지위는 로컬 I1020 원자료[1]로 뒷받침")
rep('related_species',"일부 아종은 여러 계통에 흩어졌다[6]","일부 아종은 측계통(paraphyletic)으로 나타났다[6]","[6] 전문: 'paraphyletic' 표현에 맞춤")
rep('cultivation',"국내 연구에 쓰인 동결건조 유충은 전북 정읍의 농가나 충북농업기술원에서 공급되었다[4, 12, 13].",
 "국내 연구에 쓰인 유충은 정읍의 시판처에서 산 동결건조 유충[4], 충북농업기술원이 공급한 동결건조 유충[12], 정읍 농가에서 산 생유충[13]이었다.",
 "[13]은 동결건조가 아니라 수분 63–88%의 생유충을 농가에서 구입; [4]는 시판처(정읍), [12]는 충북농업기술원 — 시료 형태·출처를 논문별로 구분")
rep('processing',"유충을 갈아 만든 유화물은 pH 7.20으로 비교한 세 종 가운데 가장 높았다[13].",
 "생유충 65%·돼지 등지방 20%·얼음 15%로 만든 유화물은 pH 7.20으로 비교한 세 종 가운데 가장 높았다[13].",
 "[13] 유화물은 유충만이 아니라 등지방·얼음을 섞은 배합")
rep('processing',"유충·성충 키토산은 납(934 mg/g) 같은 중금속과 항생제를 흡착하는 소재로도 연구되었다[15].",
 "유충과 성충에서 각각 얻은 키토산은 중금속·항생제 흡착 소재로도 연구되어 납 흡착량 934 mg/g이 보고되었다(초록에는 이 값이 어느 단계 키토산의 것인지 구분이 없음)[15].",
 "[15] 초록은 성충 키토산의 수율·안정성이 더 높다고 쓰고 흡착값의 시료 단계를 밝히지 않음 — 단계 혼합 서술 정정")
rep('processing',"이 원료의 건강기능식품 개별인정형 원료는 I1020 목록에서 찾지 못했다[1].","이 원료로 인정된 건강기능식품 개별인정형 원료는 확인하지 못함.",
 "I1020은 식품원료 목록이라 개별인정형 원료 여부의 근거가 될 수 없음 — 출처 [1] 제거")
rep('safety',"중국 시료(유충·번데기·성충) 분석은 유해 중금속이 과다하지 않다고 보고했다[11].",
 "중국 업체가 공급한 시료를 유충·번데기·암수 성충으로 나눠 ICP-MS로 분석한 연구는 23개 원소를 검출했고 납·카드뮴은 유충 시료에서도 검출되었으나, 함량을 기준치와 비교하지 않은 채 유해 중금속이 과다하지 않다고 결론지었다[11]. 국내 식용 유충의 중금속 기준 적합 자료는 확인하지 못함.",
 "[11] 전문: 단계별 따로 분석(혼합 시료 아님), Pb는 TDP·TDA(M)에서만 불검출(즉 유충에서 검출), Cd는 성충에서만 불검출 — '과다하지 않다'는 기준 비교 없는 저자 결론임을 밝힘")
# aliases
d['aliases']=[a for a in d['aliases'] if a!='장수애']
changes.append({'where':'aliases','before':'장수애','after':'(삭제)','why':'출처 [28] 원문 미확인(제목·검색 요약만) — 출처 없는 별명'})
# compounds
for c in d['compounds']:
    if c['name']=='Allomyrina defensin':
        changes.append({'where':'compounds[Allomyrina defensin].part','before':c['part'],'after':'세균 주입으로 유도한 유충','why':'[16] 초록은 유충에서 분리·세균 주입으로 유도된다고만 씀(체액 명시 없음)'}); c['part']='세균 주입으로 유도한 유충'
    if c['name']=='Gallic acid':
        old=c['activity_ko']; c['activity_ko']='저자들은 곤충 분말의 페놀 화합물이 패티의 항산화능(DPPH) 증가에 기여한다고 해석함(장수풍뎅이 분말 단독 효과로 분리되지 않음)[12]'
        changes.append({'where':'compounds[Gallic acid].activity_ko','before':old,'after':c['activity_ko'],'why':'[12]는 DPPH 효과를 주로 귀뚜라미 분말의 갈산으로 설명 — 과장 완화'})
# sources: remove 28,29,34 and renumber
srcs=d['sources']
for s in srcs:
    if s['n']==27: s['title']="농림축산식품부·식품의약품안전처·농촌진흥청 보도자료 「식용곤충 식품원료 인정 확대」 — 제목과 WebSearch 검색 결과로만 확인, 원문은 네트워크 허용 목록 밖이라 열지 못함(인정일·고시일 미확인)"
drop={28,29,34}
keep=[s for s in srcs if s['n'] not in drop]
mp={s['n']:i+1 for i,s in enumerate(keep)}
for s in keep: s['n']=mp[s['n']]
d['sources']=keep
def rn(m):
    nums=[int(x) for x in re.split(r',\s*',m.group(1))]
    nn=[mp[x] for x in nums if x in mp]
    assert len(nn)==len(nums),(m.group(0))
    return '['+', '.join(map(str,nn))+']'
s=json.dumps(d,ensure_ascii=False)
for sec in d['sections']:
    sec['body']=re.sub(r'\[(\d+(?:,\s*\d+)*)\]',rn,sec['body'])
def fixobj(o):
    if isinstance(o,dict):
        for k,v in o.items():
            if k=='source' and isinstance(v,list): o[k]=[mp[x] for x in v]
            elif isinstance(v,str) and k not in('url','title'): o[k]=re.sub(r'\[(\d+(?:,\s*\d+)*)\]',rn,v)
            else: fixobj(v)
    elif isinstance(o,list):
        for x in o: fixobj(x)
for k in ('compounds','nutrients','assays'): fixobj(d[k])
json.dump(d,open(P,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('/home/user/hfoodguide-wave3/docs/materials/allomyrina-dichotoma/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes), mp)
