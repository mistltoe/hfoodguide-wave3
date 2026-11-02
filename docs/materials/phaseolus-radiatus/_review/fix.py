import json
p='dossier.json'; d=json.load(open(p))
S={s['key']:s for s in d['sections']}
ch=[]
def rep(obj,key,old,new,why,where):
    v=obj[key]; assert old in v,(where,old[:30]); obj[key]=v.replace(old,new); ch.append({"where":where,"before":old,"after":new,"why":why})
rep(S['overview'],'body',"같은 목록의 녹두 행은 학명 Vigna radiata (L.) R.Wilczek에 Phaseolus radiatus L.과 Azukia radiata Ohwi를 이명으로 함께 적고 있어, 그린콩의 학명은 녹두(mung bean, green gram)의 옛 학명에 해당한다[1, 2]. 그러나 영명 'Green bean'과 이명 '깍지콩'은 문헌에서 강낭콩(Phaseolus vulgaris)의 꼬투리를 가리키는 이름으로도 쓰여서, 원자료 안에서 학명과 일반명이 서로 맞지 않는다[1, 23].",
"같은 목록의 녹두 행(녹두·녹두씨앗·녹두싹 등)은 학명 칸에 Vigna radiata (L.) R.Wilczek, Phaseolus radiatus L., Azukia radiata Ohwi를 함께 적고 있어, 그린콩 학명에서 변종 표기를 뺀 Phaseolus radiatus L.은 녹두(mung bean, green gram)의 이명에 해당한다[1, 2]. 그린콩 학명의 변종 표기 'var. aurea'는 녹두 행에 없어 그 뜻은 원자료에서 확인하지 못함. 한편 녹두 행의 영명은 'Green gram, Mung bean'인데 그린콩 행의 영명 'Green bean'은 영어 문헌에서 흔히 강낭콩(Phaseolus vulgaris)의 꼬투리를 가리키므로, 그린콩 행 안에서 학명과 영명이 서로 다른 작물을 가리킬 수 있다[1, 2, 23]. 이명 '깍지콩'은 꼬투리째 먹는 콩을 두루 이르는 말로 보이며, 어느 종을 가리키는지 공식 근거는 확인하지 못함.",
"원자료(I1020) 대조: 녹두 행은 학명 칸에 세 학명을 '/'로 나열할 뿐 '이명'이라 적지 않았고 var. aurea 는 녹두 행에 없음. 출처 [23]은 'green bean'=P. vulgaris만 뒷받침하고 '깍지콩'=강낭콩 꼬투리는 뒷받침하지 않아 약하게 고침","sections.overview")
rep(S['overview'],'body',"많은 콩으로 아시아에서 널리 먹는다[8].","많은 콩으로 주로 아시아에서 재배해 먹는다[8, 9].","'아시아' 부분은 [8] 초록에 없고 [9] 초록에 있음","sections.overview")
rep(S['related_species'],'body',"흑녹두(black gram)","블랙그램(black gram)","'흑녹두'는 [7]의 검은 녹두(black mung bean, V. radiata)와 혼동될 수 있어 영명 음역으로 바꿈","sections.related_species")
rep(S['related_species'],'body',"'Black gram씨앗'(Phaseolus mungo)은 흑녹두로,","'Black gram씨앗'(Phaseolus mungo)은 블랙그램으로,","같은 이유","sections.related_species")
rep(S['processing'],'body',"발효 녹두의 γ-아미노뷰티르산(GABA)은 0.016 g/100 g에서 0.122 g/100 g으로 늘었다[7].","γ-아미노뷰티르산(GABA)은 건조한 비발효 녹두 0.016 g/100 g, 건조한 발효 녹두 0.122 g/100 g으로 발효 녹두에 더 많았다[7].","[7] 원문은 'g/100 g dried (non)fermented mung bean'으로 건물 기준이며 같은 시료의 전후 변화가 아니라 두 시료 비교","sections.processing")
rep(S['genetics'],'body',"2014년 한국 연구진이 주도한 국제 공동연구가","2014년 국제 공동연구진이","[6] 전문에서 '한국 연구진 주도'를 직접 확인할 문장이 없음(국내 재래종·순계 사용만 확인)","sections.genetics")
rep(S['safety'],'body',"일본에서는 녹두나물을 먹은 뒤 입술 부종 등이 나타난 사례 2건이 보고되었고,","일본에서는 녹두나물 알레르기 사례 2건(그중 1명은 입술 부종·입안 불편감)이 보고되었고,","[20] 초록에서 입술 부종은 환자 1에만 기술됨","sections.safety")
C={c['name']:c for c in d['compounds']}
rep(C['gamma-Aminobutyric acid'],'content_text',"날 녹두 0.016 g/100 g → 발효 녹두 0.122 g/100 g(7.6배)[7]","건조 비발효 녹두 0.016 g/100 g, 건조 발효 녹두 0.122 g/100 g(건물 기준, 약 7.6배)[7]","생/건 기준 명시(원문 dried)","compounds.GABA")
rep(C['Ferulic acid'],'activity_ko',"주로 결합형으로 존재[7]","결합형으로 존재한다는 보고가 인용됨[7]","[7]은 페놀산이 '유리형 또는 결합형'으로 있고 페룰산 등이 결합형으로 존재한다고만 씀('주로' 근거 없음)","compounds.Ferulic acid")
for n in ['Vitexin','Isovitexin']:
    old="씨앗 25개 시료" ; new="중국 시판 녹두 25개 배치(풍건 씨앗, 수분 9.59–12.43%)"
    rep(C[n],'content_text',old,new,"[12] 초록: 25 batches, 수분 9.59–12.43% — 기준(풍건) 명시","compounds."+n)
a=d['assays'][1]['conditions']
rep(a,'sample_prep',"씨껍질 분말을 95% 에탄올(1:10 w/v)로 1시간 초음파 추출, 농축 후 메탄올에 희석","유기산과 섞어 고온·고압 처리 후 열풍 건조·분쇄한 씨껍질 가공 분말을 95% 에탄올(1:10 w/v)로 1시간 초음파 추출, 농축 후 메탄올에 희석","[25] Methods: 날 씨껍질이 아니라 가공 분말을 추출함","assays[1].conditions.sample_prep")
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(ch,open('_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(ch))
