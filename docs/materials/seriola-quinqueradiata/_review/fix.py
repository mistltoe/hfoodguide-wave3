import json,sys
p=sys.argv[1]
d=json.load(open(p))
S={s['key']:s for s in d['sections']}
changes=[]
def rep(key,old,new,why):
    b=S[key]['body']
    assert old in b,(key,old)
    S[key]['body']=b.replace(old,new)
    changes.append({"where":f"sections.{key}","before":old,"after":new,"why":why})

rep('history','yellowtail(방어로 추정되나 원문에 학명 없음)이 들어 있었다[30]',
 "학명 없이 'yellowtail'로 적힌 어종이 들어 있었다(영문 초록 기준, 방어로 단정할 수 없음)[30]",
 "[30] 영문 초록은 학명 없이 yellowtail 로만 적어 '방어로 추정'은 근거 없는 추정")
rep('history','2016년 11월 서울의 한 초등학교 급식에서 yellowtail 스테이크를 먹은',
 "2016년 11월 서울의 한 초등학교 급식에서 'yellowtail' 스테이크(학명 미기재)를 먹은",
 "[4] 전문에 학명·국문명이 없어 종 미확정임을 문장 안에서 분명히 함")
rep('biology','일본 가고시마 시장의 자연산 방어 223마리는 전장 50 cm 미만부터 70 cm 넘는 개체까지 있었다[31].',
 '일본 가고시마 시장의 자연산 방어 223마리 중 24.2%에서 기생성 요각류 Caligus coryphaenae가 확인되었고, 자연산 방어에서의 첫 기록이었다[31].',
 "[31] 의 요지는 체장 분포가 아니라 Caligus coryphaenae 감염(유병률 24.2%) 첫 기록")
rep('biology','방어 미오글로빈은 아미노산 147개로 이루어지고 다른 전갱이과 어류와 81–99%가 같다[32].',
 '방어 미오글로빈은 아미노산 147개로 이루어지며, 방어를 포함해 조사한 전갱이과 5종 미오글로빈 사이의 서열 일치도는 81–99%였다[32].',
 "[32] 의 81–99% 는 전갱이과 5종 간 일치도 범위로, 방어 대 다른 종 값이 아님")
rep('biology','소화관 전사체 분석은 위·장·직장에서 단백질 분해효소 유전자가 중요함을 보여 주었다[5].',
 '소화관 전사체 분석은 위·장·직장에서 단백질 분해효소 유전자가 중요함을 보여 주었다[5].',
 'noop') if False else None
rep('biology','중국 저우산 시장 시료에서는 31종 가운데 방어의 포화지방산(89.7±5.8 mg/100 g)과 n-6 고도불포화지방산(2.1±1.9 mg/100 g)이 가장 낮아, 산지·개체에 따라 지방 함량 차이가 큼을 보여 준다[35, 2].',
 '중국 저우산 시장 시료 31종 조사에서는 방어(학명 표기)의 가식부 100 g당 포화지방산(89.7±5.8 mg)과 n-6 고도불포화지방산(2.1±1.9 mg)이 가장 낮았다고 보고되었으나[35], 일본 양식 방어 보통근 값(포화지방산 2.83–3.57 g/100 g)[2]보다 수십 배 낮아 시료·동정·분석 조건은 초록만으로 확인하지 못함.',
 "[35] 값이 [2] 보다 수십 배 낮은데 '산지·개체 차이'로 해석한 것은 원문에 없는 추론 — 초록 값만 옮기고 확인 한계를 밝힘")
rep('related_species','방어·잿방어·부시리의 미오글로빈 아미노산 서열은 분류와 맞는 계통을 보였다[32]. 잿방어 연구는 성 결정 관련 SNP를 염색체 12번에서 찾았고, 방어와의 유전체 비교에서 방어속의 성 결정 체계가 보존되어 있을 것이라고 보았다[33].',
 '방어·잿방어·부시리를 포함한 전갱이과 5종의 미오글로빈 서열 계통은 기존 형태 분류와 맞았다[32].',
 "[33] 은 잿방어(S. dumerili) 성 결정 연구라 근연종 자료 섞임을 피하려 삭제; [32] 문장은 5종 분석임을 명확히")
rep('related_species',"실제로 한 논문은 방어(S. quinqueradiata)를 부시리의 영문명인 'yellowtail kingfish'로 적었다[28].",
 "실제로 한 논문은 방어(S. quinqueradiata)를 'yellowtail kingfish'로 적었는데[28], 다른 논문은 이 이름을 부시리(S. lalandi)에 썼다[32].",
 "부시리=yellowtail kingfish 근거를 [32] 원문으로 붙임(식약처 목록의 부시리 영문명은 Yellowtail amberjack)")
rep('cultivation','양식에서는 피부 기생충 Benedenia seriolae 감염이 큰 문제여서 저항성 유전자 연구가 이어졌다[9, 10].',
 '양식에서는 피부 기생충(단생흡충) Benedenia seriolae 감염이 큰 문제여서 저항성 유전자 연구가 이어졌다[9, 10].','표현 보강(확인)') if False else None
rep('processing','냉장 저장에서 혈합육은 10일 넘게, 등쪽 보통근은 14일째에 냄새가 받아들일 수 없는 수준이 되었고, 한 세균 속이 90% 넘게 우세해졌다[22].',
 '냉장 저장에서 혈합육은 10일 넘게, 등쪽 보통근은 14일째에 냄새가 받아들일 수 없는 수준이 되었고, 10일 넘게 저장하면 두 부위 모두 슈도모나스속(Pseudomonas) 세균이 90% 넘게 우세해졌다[22].',
 '[22] 초록·키워드로 우세 세균 속(Pseudomonas)과 시점(10일 이후)을 구체화')
rep('safety','히스타민은 열에 안정해 익혀도 없어지지 않으므로 냉장 유통이 필수라고 논문은 강조했고, 당시 방어가 히스타민 검사 대상 품목에 없었다고 지적했다(현재 식품공전 적용 여부는 확인하지 못함)[4].',
 "히스타민은 열에 안정해 익혀도 없어지지 않으므로 냉장 유통이 필수라고 논문은 강조했고, 당시 'yellowtail'이 히스타민 검사 대상 품목에 없었다고 지적했다(논문의 yellowtail이 방어인지와 현재 식품공전 적용 여부는 확인하지 못함)[4].",
 "[4] 원문은 'yellowtail fish' 로만 적어 '방어'로 단정한 표현을 고침")
rep('safety','2016년 서울 급식 사고에서 남은 yellowtail 스테이크의 히스타민은',
 "2016년 서울 급식 사고(원문은 학명 없이 'yellowtail')에서 남은 스테이크의 히스타민은",
 '종 미확정 사례임을 안전성 절에서도 밝힘')
rep('safety','일본 시판 생선 조사에서 yellowtail의 총수은·메틸수은은 양식이 자연산보다 낮았으나, 수치는 초록에서 확인하지 못함[26].',
 "일본 시판 생선 19종 210시료 조사에서 'yellowtail'(초록에 학명 없음)의 총수은·메틸수은은 양식이 자연산보다 낮았으나, 수치는 초록에서 확인하지 못함[26].",
 '[26] 초록에 학명이 없음을 본문에 밝히고 조사 규모를 원문대로 보충')
rep('safety','기생충으로는 제주 위 아니사키스증 감염원 생선에 yellowtail이 포함되었고[30], 동해 고성 앞바다 방어에서 선충 Philometroides seriolae가 확인되었다[29].',
 "기생충으로는 제주 위 아니사키스증 감염원 생선 목록에 학명 없이 'yellowtail'이 들어 있었으나 그 생선에서 유충을 직접 찾은 것은 아니었고[30], 동해 고성 앞바다 방어 2마리에서 선충 Philometroides seriolae 6개체가 확인되었다[29].",
 "[30] 은 환자 섭취력 기반 목록이고 유충 확인은 고등어·볼락류(rock cod)에서만 했음; [29] 수치 보충")
d['sections']=list(S.values())
# compounds
for c in d['compounds']:
    if c['name']=='Histamine':
        o=c['content_text']; c['content_text']="서울 급식 사고 잔여 스테이크(원문은 학명 없이 'yellowtail') 293 mg/kg(기준 200 mg/kg)[4]"
        changes.append({"where":"compounds.Histamine.content_text","before":o,"after":c['content_text'],"why":"종 미확정 표기"})
    if c['name']=='Linoleic acid':
        o=c['content_text']; c['content_text']="연안 양식 1.400±0.086, 외해 양식 1.050±0.022 g/100 g[2]"
        changes.append({"where":"compounds.Linoleic acid.content_text","before":o,"after":c['content_text'],"why":"[35] 값은 n-6 PUFA 합계라 리놀레산 값이 아니고 [2] 와 수십 배 어긋남"})
        o2=c['activity_ko']; c['activity_ko']="외해 양식이 연안 양식보다 유의하게 낮아 사료 섭취량에 따라 달라졌다[2]"
        changes.append({"where":"compounds.Linoleic acid.activity_ko","before":o2,"after":c['activity_ko'],"why":"[35] 제거에 맞춤"})
        c['source']=[2]
    if c['name']=='Trimethylamine':
        o=c['activity_ko']; c['activity_ko']="찐 방어의 비린 냄새와 관련되며, 고온 단시간 가열 때 혈합육의 TMA 냄새 강도가 더 높았다[23]"
        changes.append({"where":"compounds.Trimethylamine.activity_ko","before":o,"after":c['activity_ko'],"why":"[23] 은 가열 조건 간 비교였음"})
    if c['name']=='Mercury':
        c['role']='contaminant'
        o=c['content_text']; c['content_text']="수치는 초록에서 확인하지 못함; 'yellowtail'(초록에 학명 없음)은 양식이 자연산보다 낮음[26]"
        changes.append({"where":"compounds.Mercury","before":"role bioactive; "+o,"after":"role contaminant; "+c['content_text'],"why":"유해 중금속을 bioactive 로 둔 것 정정, 종 미확정 표기"})
for a in d['assays']:
    pass
# sources: renumber after dropping 33
src={s['n']:s for s in d['sources']}
for s in d['sources']:
    if s['n']==16:
        s['title']="Ichthyobacterium seriolicida gen. nov., sp. nov., a member of the phylum 'Bacteroidetes', isolated from yellowtail fish (Seriola quinqueradiata) affected by bacterial haemolytic jaundice, and proposal of a new family, Ichthyobacteriaceae fam. nov. Int J Syst Evol Microbiol 2016;66(2):580-586 (초록 확인)"
        changes.append({"where":"sources[16].title","before":"제목 일부 누락","after":"PubMed 제목 전체","why":"PubMed 서지와 맞춤"})
    if s['n']==35:
        s['title']=s['title'].replace('영문 초록 확인)','영문 초록 확인; 값이 다른 자료보다 수십 배 낮아 해석 주의)')
json.dump({"d":d,"changes":changes},open(sys.argv[2],'w'),ensure_ascii=False,indent=1)
