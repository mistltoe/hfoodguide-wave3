import json
p='/home/user/hfoodguide-wave3/docs/materials/hemerocallis-fulva/dossier.json'
d=json.load(open(p))
S={s['key']:s for s in d['sections']}
changes=[]
def rep(key,old,new,why):
    b=S[key]['body']; assert old in b,(key,old); S[key]['body']=b.replace(old,new); changes.append({"where":f"sections.{key}","before":old,"after":new,"why":why})
rep('overview','꽃에는 루틴·카페오일퀸산 유도체·플라보놀이','꽃에는 루틴·카페오일퀸산 유도체·플라보노이드가','[8] 은 꽃에서 플라본류·캠페롤 배당체 등을 분리했다고 씀(플라보놀만이 아님)')
rep('history',"'진전화(金针花, Jīn Zhēn Huā)'","'금침화(金針花, Jīn Zhēn Huā)'",'金針花의 한자음은 금침화(진전화는 잘못된 독음)')
rep('history','원추리 꽃은 값비싼 사프란(Crocus sativus 암술머리)의 위품으로 동남아시아 시장에서 거래된 일이 있어, 5S rRNA 간격 서열로 이를 가려내는 방법이 개발되었다[31].',
 '동남아시아 시장에서는 원추리(H. fulva)와 근연종 H. citrina, 잇꽃이 사프란(Crocus sativus 암술머리) 이름으로 유통될 수 있어, 네 종의 5S rRNA 간격 서열 차이를 판별 표지로 쓰자는 연구가 있다[31].',
 '[31] 초록은 꽃이라고 특정하지 않았고 H. citrina·잇꽃도 함께 다룸; 방법 개발이 아니라 서열 차이를 표지로 제안')
rep('related_species','중국에서 꽃봉오리를 채소로 많이 먹는 종은 H. citrina이며','아시아에서 꽃봉오리를 채소로 널리 먹는 종으로 소개된 것은 H. citrina(중국명 황화채)이며','[18] 초록은 \'widely consumed as a delicious vegetable in Asia\'라고 씀(중국 한정 아님)')
rep('related_species','왕원추리(H. fulva var. kwanso) 잎의 총플라보노이드가 39.26 mg RE/g으로 가장 많았으나',
 '왕원추리(H. fulva var. kwanso) 잎 추출물의 총플라보노이드가 추출물 1 g당 39.26 mg RE(루틴 당량)로 가장 많았으나(나머지 7개는 원예 교잡 품종)',
 '[28] 전문: TFC 는 잎이 아니라 추출물 g당 루틴 당량, 8개 중 7개는 원예 품종')
rep('processing','총페놀산 1408 mg/100 g, 총플라보노이드 1830 mg/100 g(건물 기준)으로','총페놀산 1408 mg/100 g(갈산 당량), 총플라보노이드 1830 mg/100 g(퀘르세틴 당량, 건물 기준)으로','[3] 전문: 당량 기준 값임을 밝힘')
rep('processing','잎 플라보노이드는 초음파 추출에서 에탄올 70.6%, 용매비 43.9:1 mL/g, 61.7 °C가 최적 조건이었다[28].',
 '네덜란드에서 들여온 원예 품종·변종 잎을 쓴 연구에서 잎 플라보노이드의 초음파 추출은 에탄올 70.6%, 용매비 43.9:1 mL/g, 61.7 °C가 최적 조건이었다[28].',
 '[28] 시료는 원예 교잡 품종 7개와 var. kwanso 로, 본종 야생형 잎이 아님을 밝힘')
rep('genetics','데이릴리 유전체에서 SWEET 당 수송체 유전자 19개가 11개 염색체에 고르지 않게 분포했고',
 "원예 품종 'Golden Doll'을 쓴 데이릴리 유전체 분석에서 SWEET 당 수송체 유전자 19개가 확인되어 18개가 11개 염색체에 고르지 않게 분포했고(1개는 스캐폴드),",
 '[26] 전문: 19개 중 18개만 염색체에, 1개는 스캐폴드; 재료는 원예 품종')
rep('safety','원추리와 독초 Veratrum maackii는 대표적인 혼동 쌍으로 다뤄졌다[17]','원추리와 독초 Veratrum maackii는 이 연구가 다룬 혼동 쌍 세 개 중 하나였다[17]','[17] 초록은 세 쌍을 나란히 듦(대표 쌍이라고 하지 않음)')
# compounds parts for [6]
amb="부위 불분명('밝은 주황' 원추리 시료; 논문은 '먹는 잎'으로 기재)"
for c in d['compounds']:
    if c['source']==[6]:
        before=c['part']; c['part']=amb
        if c['name']=='Quercetin' and c['role']=='marker':
            c['role']='bioactive'; changes.append({"where":"compounds.Quercetin.role","before":"marker","after":"bioactive","why":"[6] 단일 시료·부위 불분명이라 지표 성분으로 쓰기 어려움"})
        changes.append({"where":f"compounds.{c['name']}.part","before":before,"after":amb,"why":"[6] 은 '먹는 잎'이라 쓰면서 시료명은 '밝은 주황'(꽃 가능성) — 부위를 단정하지 않음"})
a=d['assays'][0]; before=a['part']
a['part']="부위 불분명(타이베이 시장 구입 '밝은 주황' 원추리 시료, 동결건조 분말; 논문은 '먹는 잎'으로 기재)"
changes.append({"where":"assays[0].part","before":before,"after":a['part'],"why":"부위 불분명 표기 통일([6] 전문)"})
for s in d['sources']:
    if s['n']==3: s['title']=s['title'].replace('J Food Drug Anal 31(4).','J Food Drug Anal 31(4):649-663.')
    if s['n']==5: s['title']=s['title'].replace('16 Suppl 1.','16 Suppl 1:196-203.')
changes.append({"where":"sources[3],[5]","before":"쪽수 없음","after":"쪽수 추가","why":"PubMed 서지와 맞춤"})
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open(p.replace('dossier.json','_review/changes.json'),'w'),ensure_ascii=False,indent=1)
print(len(changes))
