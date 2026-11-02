import json,sys
p=sys.argv[1]
d=json.load(open(p))
changes=[]
def sec(k): return next(s for s in d['sections'] if s['key']==k)
def rep(where,obj,key,old,new,why):
    assert old in obj[key], (where,old)
    obj[key]=obj[key].replace(old,new); changes.append({"where":where,"before":old,"after":new,"why":why})
# top
rep('name_en',d,'name_en',' (sea string, sewing thread; ogonori)',' (sea string, sewing thread)','오고노리(ogonori)는 최근 문헌[24]에서 G. vermiculophylla 로 다뤄져 이 종의 영명으로 쓰기 어려움')
d['aliases']=[a for a in d['aliases'] if 'ogonori' not in a]
changes.append({"where":"aliases","before":"オゴノリ(ogonori)","after":"(삭제)","why":"출처 없는 별명이고, [24]는 'Ogonori'를 G. vermiculophylla 로 적음"})
o=sec('overview')
rep('sections.overview',o,'body','꼬시래기(Gracilaria verrucosa)는 꼬시래기과(Gracilariaceae)에 드는 홍조류로, 여러 나라 바닷가에 널리 자라는 먹는 해조로 소개된다[10].','꼬시래기(Gracilaria verrucosa)는 여러 나라 바닷가에 널리 자라는 먹는 홍조류로 소개된다[10].','[10] 초록에 과(科) 소속 서술 없음')
rep('sections.overview',o,'body','이 종에서는 프로스타글란딘과 산화 지방산이 여럿 분리되었고, 일본에서는 이 해조를 먹은 뒤 사망을 포함한 중독 사례가 보고되었다[2, 3, 4].','이 종에서는 프로스타글란딘과 산화 지방산이 여럿 분리되었다[3, 4]. 일본에서는 G. verrucosa라는 학명으로 적힌 \'오고노리\'를 먹은 뒤 사망을 포함한 중독 사례가 보고되었으나, 최근 문헌은 오고노리를 G. vermiculophylla로 다룬다[2, 24].','중독 사례 시료의 종 정체: [24] 는 오고노리를 G. vermiculophylla 로 적음 — 이 종 근거로 단정하지 않게 고침')
h=sec('history')
rep('sections.history',h,'body',"일본에서는 이 해조를 '오고노리(ogonori)'라 부르며 먹어 왔고, 이 이름의 해조는 먹는 홍조류로 소개되며, 1985년 일본 국립위생시험소 보고에는 '구토를 일으킨 오고노리(Gracilaria verrucosa Papenf.)'의 성분을 인공 위액으로 처리해 본 연구가 실렸다[2, 31].","일본의 먹는 홍조류 '오고노리(ogonori)'는 1980–90년대 일본 문헌에서 Gracilaria verrucosa라는 학명으로 적혔고, 1985년 일본 국립위생시험소 보고에는 '구토를 일으킨 오고노리(Gracilaria verrucosa Papenf.)'의 성분을 인공 위액으로 처리해 본 연구가 실렸다[2, 31]. 최근 문헌은 오고노리를 동아시아 원산 G. vermiculophylla로 다룬다[24].","'이 해조를 오고노리라 부르며 먹어 왔다'는 [2]·[31] 이 말하지 않음; 오고노리 = G. vermiculophylla([24]) 를 밝힘")
b=sec('biology')
rep('sections.biology',b,'body','일본 연구진은 이 종의 조직 1 g(생중량)에서 원형질체 1.03 × 10^8개를 얻는 효소 처리 조건이 정리되었다[32].','일본 연구진은 이 종의 조직 1 g(생중량)에서 원형질체 1.03 × 10^8개를 얻는 효소 처리 조건을 정리했다[32].','문장 호응 수정(내용은 [32] 초록과 같음)')
r=sec('related_species')
rep('sections.related_species',r,'body','일본의 오고노리는 최근 문헌에서 Gracilaria vermiculophylla라는 학명으로 다뤄지며, 이 종의 원산지는 동아시아로 정리되어 있다[24, 25].','일본의 오고노리는 최근 문헌에서 Gracilaria vermiculophylla라는 학명으로 다뤄지며, 이 종의 원산지는 동아시아로 정리되어 있다[24, 25]. G. vermiculophylla 집단 유전 연구는 중국·한국·일본 연안을 자생 범위로 표본 조사했고, 한국 동해안과 러시아 연안에서도 같은 미토콘드리아 유형이 보고되었다[25]. 따라서 한국·일본·러시아 극동 연구에서 \'G. verrucosa\'로 적힌 시료가 실제로 어느 종인지는 각 원문만으로 확인하지 못함[3, 25].','외국·국내 \'G. verrucosa\' 시료의 종 정체 단서 추가([25] 전문: 자생 범위 표본지 중국·한국·일본, 러시아 연안 haplotype)')
c=sec('cultivation')
rep('sections.cultivation',c,'body','국내 연구 시료는 전남 완도와 장흥 지역에서 얻은 것으로, 말린 상태로 얻은 건조품이었다[9, 20, 23]. 장흥산 시료는 흐르는 수돗물로 씻어 소금기를 뺀 뒤 실온에서 말려 썼다[9].','국내 연구 시료는 전남 완도와 장흥 지역에서 얻었고, 모두 말린 시료를 갈거나 추출해 썼다[9, 20, 23]. 장흥산 시료는 실온 건조와 흐르는 수돗물 세척으로 소금기를 뺐고, 완도산 시료는 24시간 물에 불려 소금기를 뺀 뒤 35 °C에서 48시간 말렸다[9, 23].','[9]·[23] 전문: 얻을 때 건조품이었다는 서술은 없음, 장흥 시료는 \'실온 건조 후 세척\' 순서; [23] 처리 조건 추가')
g=sec('genetics')
rep('sections.genetics',g,'body','꼬시래기는 1990년대 홍조류 분자생물학의 모델처럼 쓰여, 18S rRNA 유전자 전체 서열이 1990년에 보고되었다[16].','꼬시래기는 1990년대 여러 홍조류 분자생물학 연구에 쓰였고, 18S rRNA 유전자 서열이 1990년에 보고되었다[16].','\'모델처럼\'은 [16] 이 말하지 않는 평가')
rep('sections.genetics',g,'body',"이는 'G. verrucosa'라는 이름 아래 서로 다른 계통이 섞여 있었을 가능성을 보여 준다[15].","이 연구는 이 스페이서 서열로 가까운 종이나 집단을 가를 수 있는지 보려는 것이었고, 시료에는 G. verrucosa와 비슷한 종도 포함되었다[15].",'[15] 초록이 말하지 않는 해석을 원문 서술로 바꿈')
s=sec('safety')
rep('sections.safety',s,'body','1993년 10월 일본 요코하마에서 오고노리(G. verrucosa)를 먹은 2명이 중독되어 1명(여성)이 숨졌고, 증상은 메스꺼움·구토·저혈압이었다[2].','1993년 10월 말 일본 요코하마에서 \'오고노리\'(원문 학명 G. verrucosa)를 먹은 2명이 중독되어 1명(여성)이 숨졌고, 증상은 메스꺼움·구토·저혈압이었다[2].','[2] 초록 \'late October\', 학명은 원문 표기임을 밝힘')
rep('sections.safety',s,'body','이 종의 PGE2+PGF2 함량은 계절에 따라 건조 중량 1 g당 420–2500 μg으로 달라졌다[3].','이후 문헌은 오고노리를 동아시아 원산 G. vermiculophylla로 다루며, 이 해조의 PGE2 생성이 때때로 식중독을 일으킨다고 적었다[24]. 따라서 이 사례가 식약처 목록의 꼬시래기(G. verrucosa)와 같은 종에서 일어난 것인지는 확인하지 못함. 러시아 극동의 \'G. verrucosa\' 시료에서는 PGE2+PGF2 함량이 계절에 따라 건조 중량 1 g당 420–2500 μg으로 달라졌다[3].','중독 사례의 종 정체 단서([24]) 추가, [3] 시료 산지 명시')
rep('sections.safety',s,'body','마르세유 지역 건강한 성인에서 요오드 흡수율이 101%로 측정되었다[14].','마르세유 지역 건강한 성인에서 소변 배설로 잰 요오드 생체이용률이 101%였다[14].','[14] 는 bioavailability(소변 배설 기준)로 적음')
for cpd in d['compounds']:
    if cpd['name']=='Iodine':
        rep('compounds.Iodine.activity_ko',cpd,'activity_ko','건강한 성인 요오드 흡수율 101%(마르세유), 85%(브뤼셀)[14]','건강한 성인 요오드 생체이용률(소변 배설 기준) 101%(마르세유), 85%(브뤼셀)[14]','[14] 용어에 맞춤')
    if cpd['name']=='Prostaglandin E2':
        rep('compounds.PGE2.activity_ko',cpd,'activity_ko','1993년 일본 중독 사례의 원인 물질로 추정(메스꺼움·구토·저혈압)[2]','1993년 일본 \'오고노리\'(원문 학명 G. verrucosa) 중독 사례의 원인 물질로 추정(메스꺼움·구토·저혈압)[2]','중독 시료 학명은 원문 표기')
        rep('compounds.PGE2.part',cpd,'part','엽상체(떠서 자라는 형태)','엽상체(러시아 극동, 떠서 자라는 형태)','[3] 시료 산지(블라디보스토크 연구소) 명시')
    if cpd['name']=='Cholesterol':
        rep('compounds.Cholesterol.content_text',cpd,'content_text','새 스테롤 배당체 (24R)-5α-stigmast-9(11)-en-3β-D-glucopyranoside 함께 분리[35]','같은 해조의 메탄올 추출물에서는 새 스테롤 배당체 (24R)-5α-stigmast-9(11)-en-3β-D-glucopyranoside 분리[35]','[35]: 배당체는 메탄올 추출물, 콜레스테롤은 디클로로메탄-아세톤 추출물')
a=d['assays'][0]
rep('assays[0].rationale',a,'rationale','전문 확인 못함(초록 기준) [2, 3].','러시아 극동 시료로 종 정체는 원문만으로 확인하지 못함; 전문 확인 못함(초록 기준) [2, 3].','시료 종 정체 단서 명시')
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
