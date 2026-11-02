import json,sys
p='/home/user/hfoodguide-wave3/docs/materials/pomatomus-saltatrix/dossier.json'
d=json.load(open(p))
changes=[]
def sec(k): return [s for s in d['sections'] if s['key']==k][0]
def rep(obj,field,old,new,where,why):
    v=obj[field]
    assert v.count(old)==1,(where,old)
    obj[field]=v.replace(old,new); changes.append({"where":where,"before":old,"after":new,"why":why})
o=sec('overview')
rep(o,'body','상온에 두면 히스타민이 쌓여','보관·해동을 잘못하거나 온도 관리가 나쁘면 히스타민이 쌓여','sections.overview','[12]는 잘못된 보관·해동, [10]은 5–15 °C 저장을 말함 — "상온"은 출처에 없음')
h=sec('history')
rep(h,'body','1899년 미국 로드아일랜드 뉴포트에서 잡힌 블루피쉬를 바탕으로 처음 기재되었다[33]','미국 로드아일랜드 뉴포트에서 잡힌 블루피쉬 아가미 표본으로 1899년에 처음 기재되었다(Microcotyle pomatomi Goto, 1899)[33]','sections.history','[33] 초록은 채집 연도를 말하지 않음 — 1899는 기재 연도')
rep(h,'body','1987년 매사추세츠주 보고는 학회 식사 뒤 5명이 발병한 사건의 원인으로','1987년 미국 매사추세츠주 보건 당국 연구진의 보고는 의학 학회 공동 식사 뒤 5명이 발병한 사건의 원인으로','sections.history','[12]는 매사추세츠주 보건부 소속 저자의 보고(발생지는 색인상 뉴햄프셔) — 장소를 단정하지 않게 고침')
rep(h,'body','1986–1991년 뉴저지 조사에서는 블루피쉬 등 어패류의 클로르데인이 습중량 5–2,150 ppb 범위로 측정되었다[16].','1986–1991년 뉴저지 조사에서는 블루피쉬를 포함한 어패류 5종의 클로르데인이 습중량 5–2,150 ppb 범위로 측정되었고, 가장 높은 평균(300 ppb)은 블루피쉬가 아닌 미국뱀장어에서 나왔다(블루피쉬만의 값은 초록에 없음)[16].','sections.history','[16] 범위는 5종 전체 값 — 다른 종 자료 섞임 방지')
rep(h,'body','2000년대 이후에는 어린 블루피쉬를 하구 오염 지표종으로 쓰는 연구가 늘었다[17, 18].','2010년대에는 어린 블루피쉬를 하구 오염 지표종으로 쓴 연구가 나왔다[17, 18].','sections.history','[17]·[18]은 2013·2016년 논문 2편 — "늘었다"는 추세 주장은 출처가 뒷받침하지 않음')
r=sec('related_species')
rep(r,'body','근육에서 분리한 파브알부민은 \'빠른\'·\'느린\' 두 동형으로 나뉘었고 겉보기 분자량은 10,400–14,000 범위였다[34].','흰 근육에서 분리한 파브알부민은 \'빠른\'·\'느린\' 두 동형으로 나뉘었고, 블루피쉬를 포함한 농어목 4종 전체의 겉보기 분자량은 10,400–14,000 범위였다[34].','sections.related_species','[34]의 분자량 범위는 4종 전체 값')
rep(r,'body','국립생물자원관 국가생물종목록의 국문 표준명은','학명의 명명자·연도는 Linnaeus, 1766으로 적은 논문들을 따른다[21, 29]. 국립생물자원관 국가생물종목록의 국문 표준명은','sections.related_species','명명 연도 근거 보강([25] 제목의 1776은 원 논문 표기)')
c=sec('cultivation')
rep(c,'body','유럽청어류(스프랫) 다음 2위','유럽스프랫(European sprat) 다음 2위','sections.cultivation','[2]·[3]은 European sprat 한 종을 말함')
pr=sec('processing')
rep(pr,'body','이산화탄소 기체치환포장은 일반 포장보다 저장 안정성을 45–55% 늘렸다[28].','블루피쉬를 포함한 대서양 어류 4종을 이산화탄소 기체치환포장하면 일반 포장보다 저장 안정성이 45–55% 늘었다(4종 함께 보고)[28].','sections.processing','[28]의 45–55%는 4종 합산 결과')
s=sec('safety')
rep(s,'body','구운 필레는 껍질과 기름을 버렸을 때 PCB가 평균 27% 낮았다[14].','구운 필레(껍질·기름 제거)의 PCB 농도는 조리 전 2.5 ppm에서 2.7 ppm(전체 무게 기준)으로 비슷했지만, 필레에 남은 PCB 총량은 평균 27% 줄었다[14].','sections.safety','[14]: 농도는 수분 손실로 거의 그대로, 27%는 총량 감소 — 농도가 낮아진 것처럼 읽히지 않게')
rep(s,'body','블루피쉬만 86일 먹인 고양이의 지방','블루피쉬만 86일 먹인 고양이 사육 실험(동물)에서 지방의','sections.safety','동물 실험임을 분명히')
rep(s,'body','41.3±19.3개/g(건중량)으로 7종 가운데 가장 많았다[32]','41.3±19.3개/g(건중량)으로 7종의 근육 가운데 가장 많았다[32]','sections.safety','[32] 비교는 근육 조직 기준')
for x in d['compounds']:
    if x['name']=='Polychlorinated biphenyls':
        rep(x,'content_text','조리 전 평균 2.5 ppm(Aroclor 1254 기준), 조리 뒤 2.7 ppm[14]','조리 전 평균 2.5 ppm(Aroclor 1254 기준, 전체 무게 기준), 조리 뒤 2.7 ppm — 총량은 평균 27% 감소[14]; 블루피쉬 먹인 고양이 지방 중앙값 48 ppm(건중량)[15]','compounds.PCB','기준(습/전체 무게) 명시, [15] 값 연결')
    if x['name']=='Parvalbumin':
        rep(x,'content_text',"'빠른'·'느린' 두 동형, 겉보기 분자량 10,400–14,000[34]","'빠른'·'느린' 두 동형, 겉보기 분자량 10,400–14,000(4종 전체 범위)[34]",'compounds.Parvalbumin','4종 전체 범위')
a=d['assays']
rep(a[0]['conditions'],'standard','mg/100 g 환산은 어류 지방산 환산계수(XFA) 사용','mg/100 g 습중량 환산은 어류 지방산 환산계수(XFA) 사용([3]의 같은 실험실 방법; [2] Methods는 총지방산 중 %로 표기)','assays[0].conditions.standard','XFA는 [2]가 아니라 [3] Methods에 있음')
rep(a[3],'method','HPLC(형광 검출)','HPLC','assays[3].method','[10] 초록은 HPLC만 말함; 형광 검출은 2001년 후속 연구[11]')
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('/home/user/hfoodguide-wave3/docs/materials/pomatomus-saltatrix/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
