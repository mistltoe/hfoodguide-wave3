import json,re,sys
P='dossier.json'
d=json.load(open(P))
changes=[]
def rep(where,old,new,why):
    global d
    hit=False
    for s in d['sections']:
        if s['key']==where and old in s['body']:
            s['body']=s['body'].replace(old,new); hit=True
    if not hit: sys.exit('MISS '+where+': '+old[:40])
    changes.append(dict(where='sections.'+where,before=old,after=new,why=why))

rep('overview',"식약처 목록은 린네의 이름 Hibiscus esculentus 를 대표 학명으로 쓰지만, 현재 식물 분류 목록과 대부분의 연구는 이 종을 무스크아욱속(Abelmoschus)으로 옮긴 Abelmoschus esculentus (L.) Moench 로 부른다[9, 5].",
 "식약처 목록은 린네가 붙인 이름 Hibiscus esculentus 를 대표 학명으로 쓰지만, 아벨모스쿠스속(Abelmoschus)은 히비스커스속에 들어 있다가 따로 떼어 낸 속이며, 오늘날 유전체·성분 연구 대부분은 이 종을 Abelmoschus esculentus (L.) Moench 로 부른다[7, 5, 6]. 국제 식물명 목록(WFO·POWO)에서의 정명 처리는 이번 조사에서 원문을 열지 못해 확인하지 못함.",
 "[9] WFO 는 WebSearch 요약으로만 확인돼 원문 미확인(이번 대조에서도 접속 불가) → 출처 삭제, 속 분리 사실은 [7] 서론으로 뒷받침. '무스크아욱속'은 출처 없는 국문 속명이라 '아벨모스쿠스속'(식약처 목록 음역 표기 방식)으로 바꿈")
rep('related_species',"무스크아욱속(Abelmoschus)에는","아벨모스쿠스속(Abelmoschus)에는","출처 없는 국문 속명 정리")
rep('related_species',"엽록체 유전체 분석에서 무스크아욱속은 히비스커스속(Hibiscus) 안에 들어가는 잘 지지된 무리로 나타났다[7]. 반면 2026년 아욱과 엽록체 비교 연구는 히비스커스속이 오크라와 별개의 계통일 수 있다고 보아, 두 속의 경계는 아직 정리되지 않았다[8].",
 "엽록체 유전체 분석에서 아벨모스쿠스속은 히비스커스속(Hibiscus) 안에 들어가는 잘 지지된 무리로 나타났고, 저자들은 두 속을 합칠지 일부 종을 옮길지 더 논의가 필요하다고 보았다[7]. 2026년 아욱과 엽록체 비교 연구도 본문에서는 아벨모스쿠스속이 히비스커스 무리 안에 들어간다며 병합 제안을 지지했으나, 초록에는 '히비스커스속이 오크라와 별개의 계통일 수 있다'는 상반된 문장이 있어 해석에 주의가 필요하다[8]. 두 속의 경계는 아직 정리되지 않았다[7, 8].",
 "[8] 본문 결과·고찰·결론은 Abelmoschus 를 Hibiscus 에 포함하는 제안을 지지함. 초록 한 문장만 따와 결론을 반대로 씀")
rep('related_species',"히비스커스(H. sabdariffa, 꽃받침·꽃잎, 제한적사용)",
 "히비스커스(H. sabdariffa·H. rosa-sinensis 'Cooperi'; 꽃잎 원료는 사용가능, 꽃받침 추출액·추출분말은 제한적사용)",
 "I1020 원자료: 히비스커스꽃잎 계열은 '사용가능', 꽃받침추출액·꽃받침추출분말만 '제한적사용'. 학명란에 H. rosa-sinensis 'Cooperi' 병기")
rep('related_species',"무스크아욱속 이름으로는","아벨모스쿠스속 이름으로는","출처 없는 국문 속명 정리")
rep('related_species',"닥풀의 학명란에는 Abelmoschus manihot 이 함께 적혀 있어, 닥풀 꽃(황촉규) 연구를 오크라 꽃 자료로 옮기지 않도록 주의해야 한다[1, 7].",
 "닥풀의 학명란에는 Abelmoschus manihot 이 함께 적혀 있고(목록 별명 금화규) 사용가능부위는 잎뿐이므로, 꽃 성분·임상 연구가 많은 닥풀(A. manihot) 꽃 자료를 오크라 꽃 자료로 옮기지 않도록 주의해야 한다[1, 7].",
 "'황촉규'는 [1]·[7] 어디에도 없는 이름 → 목록 별명(금화규)으로 바꾸고, 닥풀은 잎만 사용가능임을 원자료대로 적음")
rep('history',"꼬투리 점액은 혈장 대체제(혈액량 확장제)나 정제 결합제로 연구되었다[32, 4].",
 "꼬투리 점액은 혈장 대체제(혈액량 확장제)나 정제 결합제 같은 의약품 부형제로 연구되었다[32, 10].",
 "[4] 는 '정제 제형(drug tablet formulation)'만 말함. '결합제(binders)'는 [10] 에 있어 출처 교체")
rep('processing',"임상시험에서는 말린 꼬투리 가루·캡슐, 말린 열매 차 20 g, 생꼬투리를 우린 물 등 하루 3–20 g 범위의 다양한 형태가 쓰였다[11].",
 "제2형 당뇨병 환자 대상 임상시험에서는 말린 꼬투리 가루·캡슐(하루 3–10 g), 말린 열매 차(하루 20 g), 생꼬투리 3개를 물 250 mL에 우린 물 등 다양한 형태가 쓰였다[11].",
 "[11] 표1: 생꼬투리 우린 물은 g 단위 용량이 아니라 '꼬투리 3개/물 250 mL'. 3–20 g 범위에 묶을 수 없음")
rep('safety',"제2형 당뇨병 환자 대상 무작위 대조시험 6건을 묶은 메타분석에서 공복혈당과 당화혈색소가 낮아졌고, 포함된 일부 시험은 부작용이 없었다고 보고했다[11].",
 "제2형 당뇨병 환자 대상 무작위 대조시험 6건(387명, 2주–3개월)을 묶은 메타분석에서 공복혈당(가중평균차 −21.72 mg/dL)과 당화혈색소(−0.42%p)가 낮아졌으나, 인슐린·HOMA-IR·체질량지수·체중에는 유의한 변화가 없었고, 공복혈당 결과는 이질성이 컸다(I² 93%)[11]. 포함된 일부 시험은 부작용이 없었다고 보고했다[11].",
 "[11] 의 효과 크기와 유의하지 않은 결과·이질성을 빠뜨려 효과를 과장할 소지 → 원문 수치 추가")
rep('safety',"임상 연구 8건(9개 군)을 묶은 메타분석에서는 총콜레스테롤·중성지방·LDL이 낮아지고 HDL이 높아졌다[13].",
 "당뇨 전단계·제2형 당뇨병·비만·당뇨병성 신증 환자 대상 임상 연구 8건(9개 군)을 묶은 메타분석에서는 위약 대비 총콜레스테롤·중성지방·LDL이 낮아지고 HDL이 높아졌으나, 저자들도 용량을 표준화한 잘 설계된 시험이 더 필요하다고 했다[13].",
 "[13] 대상 집단과 저자 단서를 추가해 일반인 효과로 읽히지 않게 함")
rep('safety',"쥐 실험에서 꼬투리 수용성 분획을","당뇨 유발 쥐 실험에서 열매 수용성 분획을","[14] 은 alloxan 당뇨 쥐, 열매(fruits) 수용성 분획")

# compounds
for c in d['compounds']:
    if c['name']=='Pectin':
        old=c['activity_ko']; c['activity_ko']="점도·유화 성질로 식품·의약 소재로 연구됨; 세포·동물 실험에서 혈당 저하 작용이 보고됨(사람 효과는 확인되지 않음)[10]"; c['source']=[10,31]
        changes.append(dict(where='compounds.Pectin.activity_ko',before=old,after=c['activity_ko'],why='[31] 초록은 항산화·항염·항우울만 언급, 혈당 저하는 [10](in vitro·in vivo)에 있음'))
    if c['name']=='Quercetin 3-O-gentiobioside':
        old=c['content_text']; c['content_text']=old.replace("(70% 메탄올 추출물 기준)","(70% 메탄올 추출, 씨앗 기준인지 추출물 기준인지 원문에 불명확)")
        changes.append(dict(where='compounds.Q3G.content_text',before=old,after=c['content_text'],why='[3] 방법은 동결건조 추출물을 재희석해 mg/kg 로 표시, 기준이 분명하지 않음(assay rationale 와 일치시킴)'))

# sources: drop 9, renumber
old_src=d['sources']
keep=[s for s in old_src if s['n']!=9]
mp={s['n']:i+1 for i,s in enumerate(keep)}
for s in keep:
    s['n']=mp[s['n']]
for s in keep:
    if s['url'].endswith('30346086/'): s['title']=s['title'].replace("Phytother Res. 2018","Phytother Res. 2019;33(1):72-80")
d['sources']=keep
changes.append(dict(where='sources[9]',before='World Flora Online Plant List — Abelmoschus esculentus (WebSearch 요약)',after='삭제',why='원문 미확인 출처. 이번 대조에서도 wfoplantlist.org 접속 불가'))
changes.append(dict(where='sources[29]',before='Phytother Res. 2018',after='Phytother Res. 2019;33(1):72-80',why='PubMed 서지'))
def rn(t):
    def f(m):
        nums=[int(x) for x in re.split(r',\s*',m.group(1))]
        return '['+', '.join(str(mp[n]) for n in nums)+']'
    return re.sub(r'\[(\d+(?:,\s*\d+)*)\]',f,t)
def walk(o):
    if isinstance(o,dict):
        for k,v in o.items():
            if k=='source' and isinstance(v,list): o[k]=[mp[x] for x in v]
            elif k in('sources','n'): continue
            else: o[k]=walk(v)
        return o
    if isinstance(o,list): return [walk(x) for x in o]
    if isinstance(o,str): return rn(o)
    return o
for k in list(d.keys()):
    if k!='sources': d[k]=walk(d[k])
json.dump(d,open(P,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
