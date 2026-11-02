import json
p='/home/user/hfoodguide-wave3/docs/materials/seriola-rivoliana/dossier.json'
d=json.load(open(p))
S={s['key']:s for s in d['sections']}
changes=[]
def rep(key,old,new,why):
    b=S[key]['body']; assert old in b,(key,old); S[key]['body']=b.replace(old,new); changes.append({'where':'sections.'+key,'before':old,'after':new,'why':why})
rep('overview','열대 바다를 중심으로 전 세계에 퍼져 사는 표층 회유어로서','열대 바다 전역에 사는 표층성 어류로서','[9] 초록은 circumtropical pelagic fish 라고만 씀(회유어 표현 없음)')
rep('overview','한편 스페인 카나리아 제도 등에서는 이 종을 먹고 시구아테라 식중독이 일어난 사례가 보고되었다[4].','한편 스페인 카나리아 제도에서는 2008–2009년 이 종을 먹고 시구아테라 식중독이 일어난 사례가 보고되었다[4].','[4] 는 카나리아 제도만 다룸 — \'등\' 삭제, 연도 명시')
rep('history','국내에서는 1995년 10월 제주도 남동쪽 해역에서 선망으로 잡혀 부산공동어시장에서 채집된 개체가 1997년 한국어류학회지에 처음 보고되었다고 검색 요약에서 확인되었으나, 원문은 열어 보지 못했다[29].','국내 첫 기록은 1997년 한국어류학회지 보고로 알려져 있으나, 웹 검색 요약으로만 보았고 원문·초록은 확인하지 못함[29].','[29] 원문 확인 불가 — 채집 연월·해역·어법·장소 같은 세부는 덜어내고 근거 수준을 낮춤')
rep('history','카나리아 제도에서는 2004년 첫 시구아테라 집단 발생 뒤 2008–2009년에 두 차례 더 발생했고, 환자들은 근처 바다에서 잡은 이 종을 먹었다[4].','카나리아 제도에서는 2004년 첫 시구아테라 집단 발생 뒤 2008–2009년에 두 차례 더 발생했고, 이 2008–2009년 환자들이 근처 바다에서 잡은 이 종을 먹었다[4].','[4] 초록에서 이 종과 연결된 것은 2008–2009년 두 건뿐 — 2004년 건까지 이 종으로 읽히지 않게 함')
rep('history','소화관 발달, 소화효소, 기생충, 면역 등을 잇달아 보고했다[16, 17, 19].','소화관 발달, 소화효소, 기생충 등을 잇달아 보고했다[16, 17, 19].','[16][17][19] 에 면역 연구 없음')
rep('related_species',' 국명 \'낫잿방어\'는 잿방어와 닮았지만 둘째 등지느러미와 뒷지느러미 끝이 낫 모양이라 붙었다고 검색 요약에서 확인되었으나, 원문은 열어 보지 못했다[29].','','[29] 는 웹 검색 요약뿐이고 원문 확인 불가 — 국명 유래 문장 삭제')
rep('related_species','카나리아 제도 보고는 이 종을 lesser amberjack이라고 불렀지만[4], 미국 연구에서 lesser amberjack은 다른 종(S. fasciata)을 가리켰다[12].','카나리아 제도 보고는 이 종(학명 Seriola rivoliana 병기)을 lesser amberjack이라고 불렀지만[4], 미국 연구는 lesser amberjack을 almaco jack(이 종)과 다른 별개 종으로 다루었다[12].','[12] 변환본에서 학명 이탤릭이 빠져 S. fasciata 대응은 본문으로 확인 못함 — 원문에서 확인되는 \'별개 종\'까지만 씀')
rep('cultivation','수온이 1 ℃만 올라도 기생충 수가 눈에 띄게 늘었다[20].','에콰도르의 양식 수조 조사에서는 수온이 1 ℃만 올라도 기생충 수가 눈에 띄게 늘어나는 것과 관련되었다[20].','[20] 은 멕시코가 아니라 에콰도르(하라미호) 연구진이고, 초록은 \'associated with\' 로 씀')
rep('cultivation','하와이 코나 시험에서 어분을 모두 대두 단백 농축물로 바꾼 사료는 30일 동안 폐사와 야윔을 일으켰다[3].','하와이 코나 시험에서 해양 원료 없이 대두 단백 농축물만 쓴 사료는 30일 시험 중 폐사와 야윔을 일으켰다[3].','[3] 전문: 100% SPC, devoid of marine ingredients, during 30-day trial')
rep('cultivation','시판 사료군(1,175.8 g)보다 컸고, 사료 효율은 1.4 대 1.3이었다[3].','시판 사료군(42.1 g → 1,175.8 g)보다 컸고, 사료요구율(FCR)은 1.4 대 1.3으로 유의한 차이가 없었다[3].','[3] Table 3: FCR(사료요구율)이며 사료 효율이 아님, 두 군 차이 유의하지 않음')
rep('cultivation','바닷물에 녹은 설사성 패독(오카다산 등)은 알의 대량 폐사를 일으켰고[27], 삭시톡신(100 μg/L)에 노출된 알의 부화율은 5% 미만으로 대조군 71%보다 크게 낮았다[28].','실험실에서 물에 녹인 설사성 패독(오카다산·DTX-1, 오카다산 당량 120·175 μg/L)에 노출한 알은 대량 폐사했고[27], 삭시톡신(100 μg/L)에 노출한 배아의 부화율(수정 후 44시간)은 5% 미만으로 대조군 71%보다 크게 낮았다[28].','[27][28] 은 실험실 노출 시험 — 농도·조건을 초록대로 적음')
rep('safety','하와이에서 잡은 낫잿방어·잿방어 164마리와 다른 어종 175마리의 근육을 검사한 연구에서는','하와이에서 잡은 낫잿방어·잿방어 합계 164마리와 다른 한 어종(Cephalopholis argus) 175마리의 근육을 검사한 연구에서는','[5] 초록: 175마리는 한 종(blue-spotted grouper)')
rep('safety','앤틸리스 조사에서는 이 종의 간에 시구아톡신이 의미 있는 수준으로 있었지만 살은 안전했다[6].','앤틸리스 조사(26종 178마리, 쥐·병아리 생물검정)에서는 이 종의 간에 시구아톡신이 의미 있는 수준으로 있었지만 살은 먹어도 되는 수준이었다고 했다[6]. 조사한 이 종 개체 수와 독소 농도는 초록에 없다[6].','[6] 은 생물검정으로 독성을 추정한 것 — 방법과 한계를 밝힘')
rep('safety','생선 시료에서 카리브해 시구아톡신-1(C-CTX-1)이 LC-MS/MS로 확인되었다[4].','생선 시료에서 카리브해 시구아톡신-1(C-CTX-1)이 LC-MS/MS로 확인되었다(시료 부위·농도는 초록에 없음)[4].','[4] 초록은 fish samples 라고만 씀')
rep('safety','2016년 환자 관련 생선 두 건이 이 종(\'olho de boi\')으로 판정되었고, 2016년 시료에서는 시구아톡신이 검출되지 않았다[7].','2016년 환자 관련 생선 시료 세 건 가운데 두 건이 유전자 검사로 \'olho de boi\'로 판정되었고(학명은 변환본에서 빠져 있어 PubMed 색인으로 간접 확인), 세 건 모두 시구아톡신이 검출되지 않았다[7].','[7] 전문: 3건 종 판정 중 2건, 3건 모두 시구아톡신 음성; 학명 이탤릭 누락 — 판정 근거 수준 명시')
rep('safety','2020년 \'olho de boi\' 조리 시료 두 건에서는 팔리톡신 유사 물질의 흔적이 나왔으나,','2020년 \'olho de boi\' 시료 여섯 건 가운데 조리된 두 건에서 팔리톡신 유사 물질의 흔적이 나왔으나,','[7] 전문: 6건 검사, 조리 시료 2건에서만 흔적')
for c in d['compounds']:
    if c['name']=='Ciguatoxin':
        o=c['part']; c['part']='생선 시료(카나리아 제도 중독 관련, 부위는 초록에 없음)·간(앤틸리스, 생물검정)'
        changes.append({'where':'compounds.Ciguatoxin.part','before':o,'after':c['part'],'why':'[4] 초록은 부위를 밝히지 않음, [6] 은 생물검정'})
        o=c['content_text']; c['content_text']='카나리아 제도 시료에서 C-CTX-1 확인(초록에 농도 없음); 앤틸리스 개체 간에서 쥐·병아리 생물검정으로 의미 있는 독성(농도 없음)'
        changes.append({'where':'compounds.Ciguatoxin.content_text','before':o,'after':c['content_text'],'why':'[6] 정량 아님'})
for a in d['assays']:
    if a['compound']=='Caribbean ciguatoxin-1':
        o=a['part']; a['part']='생선 시료(카나리아 제도 중독 관련, 부위는 초록에 없음)'
        changes.append({'where':'assays[C-CTX-1].part','before':o,'after':a['part'],'why':'[4] 초록은 fish samples 라고만 씀'})
    if a['compound']=='Ciguatoxin':
        o=a['content']; a['content']='낫잿방어·잿방어 합계 164마리와 Cephalopholis argus 175마리를 합친 전체 시료에서 ELISA 양성 9.4%, 신경모세포 시험 독성 6.8%(종별 값은 초록에 없음)[5]'
        changes.append({'where':'assays[Ciguatoxin].content','before':o,'after':a['content'],'why':'[5] 초록대로 어종 구성 명시'})
src={s['n']:s for s in d['sources']}
o=src[7]['title']; src[7]['title']=o.replace("본문 변환본에서 이탤릭 학명이 빠져 있어 'olho de boi' 시료의 학명 Seriola rivoliana는 PubMed 초록 색인으로 확인","본문·초록 변환본 모두 이탤릭 학명이 빠져 있음 — 'olho de boi' 시료의 학명 Seriola rivoliana는 PubMed 검색 색인이 이 기록을 'rivoliana'로 찾는 것으로 간접 확인, 2020년 시료는 종 유전자 판정 서술 없음")
changes.append({'where':'sources[7].title','before':o,'after':src[7]['title'],'why':'학명 누락 논문의 종 판정 근거 수준을 정확히 적음'})
o=src[3]['title']; src[3]['title']=o.replace("'Kampachi'는 초록에서 Seriola rivoliana로 명시","변환본에서 학명이 빠져 있어 'Kampachi'=Seriola rivoliana는 PubMed 검색 색인으로 간접 확인")
changes.append({'where':'sources[3].title','before':o,'after':src[3]['title'],'why':'PMC 전문·초록 변환본 모두 학명 이탤릭 누락'})
o=src[29]['title']; src[29]['title']='한국어류학회지 1997년 낫잿방어(Seriola rivoliana) 한국 첫 기록 보고 — 웹 검색 결과 요약으로만 확인(원문·초록 페이지는 접속 제한으로 열지 못함, 세부 내용은 옮기지 않음)'
changes.append({'where':'sources[29].title','before':o,'after':src[29]['title'],'why':'원문 미확인 — 권호·세부 내용 의존도를 낮춤'})
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('/home/user/hfoodguide-wave3/docs/materials/seriola-rivoliana/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
