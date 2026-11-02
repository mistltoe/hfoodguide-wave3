import json,sys
p='/home/user/hfoodguide-wave3/docs/materials/argopecten-irradians/dossier.json'
d=json.load(open(p))
changes=[]
def rep(obj,key,old,new,where,why):
    s=obj[key]
    if old not in s: sys.exit('MISS '+where+': '+old[:40])
    obj[key]=s.replace(old,new); changes.append({"where":where,"before":old,"after":new,"why":why})
S={s['key']:s for s in d['sections']}
rep(S['overview'],'body',"가리비과(Pectinidae) 해만가리비속에 드는","가리비과(Pectinidae) Argopecten속에 드는","sections.overview","'해만가리비속'이라는 국문 속명은 [1] 카드에 없음(속은 Argopecten만 기재)")
rep(S['overview'],'body',"주로 먹는 부위는 관자(폐각근)로, 단백질이 많고 지방이 적으며 타우린·베타인·유리아미노산 같은 맛 성분이 풍부하다고 보고되었다[2].","가리비에서 주로 먹는 부위는 관자(폐각근)이며[12], 이 종의 연체부는 단백질이 많고 지방이 적으며 타우린·EPA·DHA 등을 지니고, 유리아미노산·베타인·숙신산 등이 맛을 낸다고 보고되었다[2].","sections.overview","[2]는 관자가 주 섭취 부위라고 쓰지 않음(연체부 분석). 관자가 주 식용 부위라는 말은 [12] 본문에 있음; 베타인은 맛 성분, 타우린 등은 생리활성 성분으로 원문 구분에 맞춤")
rep(S['biology'],'body',"연체동물문 이매패강 가리비과에 속하는 해산 이매패류다[1].","가리비과(Pectinidae)에 속하는 바다 이매패류다[1, 3].","sections.biology","[1] 카드에는 문·강 정보가 없고 과(Pectinidae)만 있음; 이매패류·가리비과 소속은 [3]이 기술")
rep(S['related_species'],'body',"같은 속에는 페루가리비(A. purpuratus) 등이 있으며, 중국에서는 이 종과 페루가리비의 종간 잡종에서 관자가 주황색인 'QN Orange' 계통을 골라 길렀다[24].","중국에서는 이 종의 북방 아종과 같은 속의 Argopecten purpuratus(영문 Peruvian scallop)의 종간 잡종에서 관자가 주황색인 'QN Orange' 계통을 골라 길렀다[24].","sections.related_species","'페루가리비'라는 국문명은 출처 없음; [24] 초록대로 잡종 부모가 북방 아종(A. i. irradians)임을 명시")
rep(S['related_species'],'body',"지방산 조성과 탄소 동위원소 지문으로 세 종과 산지를 구별할 수 있었다[23].","세 종 300개 시료의 산지를 지방산 조성과 지방산 δ13C 지문을 함께 써서 100% 정확도로 판별했다[23].","sections.related_species","[23] 초록은 종 구별이 아니라 산지 판별(정확도 92%·85.3%, 병용 100%)을 보고")
rep(S['related_species'],'body',"국내에서는 이 종을 흔히 '해만가리비'라 부르며, 국립수산과학원 연구 논문도 이 이름을 썼다[11].","국내 국립수산과학원 연구 논문은 이 종을 '해만가리비'라고 불렀다[11].","sections.related_species","'흔히 부른다'는 [11]이 뒷받침하지 않음")
rep(S['cultivation'],'body',"12월까지 각장 약 56 mm, 전중량 약 26 g으로 자라","12월에 각장 약 59.7 mm(각고 약 55.8 mm), 전중량 약 26.1 g으로 자라","sections.cultivation","[11] 초록: 12월 각장 59.67 mm, 각고 55.80 mm, 전중량 26.06 g (56 mm는 각고 값과 혼동)")
rep(S['history'],'body',"그 논문 초록은 이 종이 그때까지 국내에서 남해에서만 양식되어 왔다고 적었다[11].","이 논문은 이 종을 국내 남해 해역에서 양식되어 온 품종으로 소개했다[11].","sections.history","'남해에서만'은 확인되지 않음(같은 연구진의 2015년 동해 남부 시험양식 논문도 있음)")
rep(S['processing'],'body',"날것·냉장품 외에 말린 관자로도 많이 가공되며","말린 관자로도 가공되며","sections.processing","'많이'·'날것·냉장품'은 [19]가 말하지 않음")
rep(S['processing'],'body',"관자 근원섬유 단백질로 어묵 같은 겔 제품을 만들기 위해 초음파와 트랜스글루타미네이스를 함께 쓰면","관자 살로 가리비 수리미 같은 겔 제품을 만들 때 초음파(360 W)와 트랜스글루타미네이스(0.8 g/100 g)를 함께 쓰면","sections.processing","[21] 초록은 관자 근원섬유 단백질이 아닌 관자 겔(수리미)을 다룸; 조건 수치 보충")
rep(S['processing'],'body',"함께 처리해 관자의 품질 유지 효과를 살폈다[22].","함께 처리하자 4 ℃ 냉장 관자의 저장 수명이 대나무잎 항산화제 단독 처리보다 2일 늘었다[22].","sections.processing","[22] 초록의 결과값으로 구체화")
rep(S['safety'],'body',"관자에 독소가 최대 30%까지 쌓였고","실험 종료 시 전체 마비성 패독의 최대 30%가 관자에 있었고","sections.safety","[14] 원문: 'up to 30% of the PSTs were accumulated in the adductor muscle at the end of the experiment'")
rep(S['safety'],'body',"마비성·설사성 패독에 더 잘 오염되는 것으로 나타났다[15].","마비성·설사성 패독에 더 잘 오염되는 것으로 나타났고, 오염 시료는 5–7월에 나왔다[15].","sections.safety","[15] 초록의 시기 정보 보충")
rep(S['safety'],'body',"오카다산에 노출하면 이 종의 면역 기능과 산화 스트레스 지표가 나빠졌다[18].","오카다산(50–500 nM)에 실험적으로 노출한 이 종에서는 혈림프 면역 지표가 떨어지고 산화 스트레스 지표가 높아졌다[18].","sections.safety","[18]은 가리비 노출 실험이며 사람 건강 영향이 아님을 분명히 함")
# compounds
for c in d['compounds']:
    s=c['content_text']
    if "(원문의 맛 성분 분석값, 생·건 기준 명시 없음;" in s:
        c['content_text']=s.replace("(원문의 맛 성분 분석값, 생·건 기준 명시 없음;","(원문의 맛 성분 분석값, 생시료로 분석했다고 적혀 있으나 단위의 생·건 기준 명시 없음;")
    if c['name']=='Betaine':
        c['content_text']=s.replace("(원문, 생·건 기준 명시 없음)","(원문, 생시료 분석분, 단위의 생·건 기준 명시 없음)")
    if c['name']=='Adenosine monophosphate':
        c['content_text']+="; 보라색 계통 하한은 원문에 5.60으로 달리 적혀 있음"
    if c['name']=='Carotenoids':
        c['content_text']=c['content_text'].replace("주황색 관자 개체군이 흰색 개체군보다","자가수정 가계의 주황색 관자 자손이 흰색 관자 자손보다")
        c['part']="관자(주황색 변이 개체)"
changes.append({"where":"compounds[맛 성분 9종]","before":"생·건 기준 명시 없음","after":"생시료로 분석했다고 적혀 있으나 단위의 생·건 기준 명시 없음","why":"[2] 2.3절: 맛 성분은 동결건조하지 않은 시료로 분석"})
changes.append({"where":"compounds[AMP]","before":"5.70–18.17 mg/100 g","after":"+ 보라색 계통 하한 5.60 원문 불일치 주석","why":"[2] 원문 내부 불일치"})
changes.append({"where":"compounds[Carotenoids]·assays[1].content","before":"주황색 관자 개체군이 흰색 개체군보다","after":"자가수정 가계의 주황색 관자 자손이 흰색 관자 자손보다","why":"[12] 비교 대상은 자가수정 가계 자손(46 대 146)"})
a=d['assays'][1]; a['content']=a['content'].replace("주황색 관자 개체군이 흰색 개체군보다","자가수정 가계의 주황색 관자 자손이 흰색 관자 자손보다")
a=d['assays'][3]; a['content']=a['content'].replace("노출 실험 종료 시 독소의 최대 30%가 관자에 축적","노출 실험 종료 시 전체 마비성 패독의 최대 30%가 관자에 축적")
# sources
src={s['n']:s for s in d['sources']}
def srep(n,old,new,why):
    if old not in src[n]['title']: sys.exit('MISS src %d'%n)
    b=src[n]['title']; src[n]['title']=b.replace(old,new); changes.append({"where":"sources[%d].title"%n,"before":b,"after":src[n]['title'],"why":why})
srep(14,"2024;468:133896","2024;469:133896","PubMed 38428300: 권 469")
srep(15,"2005;22(7)","2005;22(7):647–651","PubMed 16019840 쪽수 보충")
srep(21,"2022;5:1254","2022;5:1185–1194","PubMed 35965656: 5권 1185–1194쪽")
srep(17,"Environ Sci Pollut Res 2017","Environ Sci Pollut Res 2017;24(4):3572–3581","PubMed 27882492 권호 보충")
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('/home/user/hfoodguide-wave3/docs/materials/argopecten-irradians/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
