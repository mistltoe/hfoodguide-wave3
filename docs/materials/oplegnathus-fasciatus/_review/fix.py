import json
p='/home/user/hfoodguide-wave3/docs/materials/oplegnathus-fasciatus/dossier.json'
d=json.load(open(p))
S={s['key']:s for s in d['sections']}
changes=[]
def rep(key,old,new,why):
    b=S[key]['body']; assert old in b,(key,old); S[key]['body']=b.replace(old,new)
    changes.append({"where":f"sections.{key}","before":old,"after":new,"why":why})
rep('biology',"돌돔은 새부리처럼 붙은 이빨(beak-like teeth)을 가지며, 부화 후 30일 무렵 뼈와 이빨의 골화가 일어난다[37].",
 "돌돔속 물고기는 아래턱의 작은 이빨이 붙어 생긴 새부리 모양 이빨(beak-like teeth)을 가진다[37]. 이 이빨의 발생 시기별 유전자 발현·골화 관찰은 돌돔과 강담돔을 함께 다룬 논문의 것이고 발생 시료가 어느 종인지 전문에서 가려지지 않아 여기에는 옮기지 않았다.",
 "[37]은 돌돔·강담돔 두 종 논문이며 30 dph는 BMP 발현 최고 시점이고 골화는 40–50 dph에 진행·완료됨; 발생 시료 종을 확인할 수 없어 강담돔 자료 섞임 우려")
rep('history',"한국 연구진은 2014년 논문에서 한국을 세계 다섯 번째 돌돔 생산국으로 적었다[24].",
 "한국 연구진은 2014년 논문 서론에서 한국을 세계 다섯 번째 돌돔 생산국으로 적었으나, 그 근거 통계는 밝히지 않았다[24].",
 "[24] 전문 서론에 인용 없이 'Currently ... fifth largest parrotfish producer'로만 적힘")
rep('cultivation',"자어는 21–24 ℃에서 길렀고, 부화 후 41–55일에는 배합 미립자사료를 먹인 무리가 살아 있는 먹이(알테미아)보다 더 잘 자랐다[27].",
 "자어는 21–24 ℃에서 길렀고, 부화 후 25–40일에는 살아 있는 먹이(알테미아)를 먹인 무리가, 41–55일에는 배합 미립자사료를 먹인 무리가 더 잘 자랐다[27].",
 "[27] 초록·전문: 1단계(25–40 dph)는 생먹이 무리가 우세 — 한쪽 결과만 적혀 있었음")
rep('processing',"연구진은 성장 기준으로 사료 카드뮴 40.7 mg/kg 이하가 안전하고 162 mg/kg 넘게는 독성이 나타날 수 있다고 보았다[24].",
 "이 시험은 사료에 염화카드뮴을 일부러 넣은 양식 사료 시험으로, 연구진은 물고기 성장 기준으로 사료 카드뮴 40.7 mg/kg 이하가 안전하고 162 mg/kg 넘게는 독성이 나타날 수 있다고 보았다[24]. 이는 물고기에게 해가 없는 사료 수준이지 사람이 먹는 살의 안전 기준이 아니며, 연구진도 이 값이 EU의 어류 사료 최대 허용치(건물 기준 0.5 mg/kg)보다 훨씬 높다고 적었다[24].",
 "사료 시험의 '안전 수준'이 식용 살 안전 기준처럼 읽힐 수 있음 — [24] 전문 Discussion 대조로 맥락 보강")
rep('safety',"한국·일본의 병든 돌돔에서는 섬모충 Miamiensis avidus도 분리되었다[16].",
 "한국·일본의 병든 양식어(넙치·도다리류·돌돔)에서 분리한 섬모충 Miamiensis avidus 21개 주의 유전자 분석에 돌돔 분리주도 포함되었다[16].",
 "[16] 초록: 21개 주는 넙치·도다리류·돌돔 세 숙주에서 분리 — 돌돔 분리주가 두 나라 모두에서 나왔는지는 초록으로 확인 불가")
C={c['name']:c for c in d['compounds']}
def crep(name,field,new,why):
    old=C[name][field]; C[name][field]=new
    changes.append({"where":f"compounds[{name}].{field}","before":old,"after":new,"why":why})
crep('Cadmium','part',"근육·간·아가미(카드뮴을 넣은 사료로 기른 어린 돌돔 — 시판 돌돔 함량 아님)","사료 시험 결과가 식용 살 함량처럼 읽히지 않게")
crep('Cadmium','activity_ko',"물고기 성장 기준 안전 사료 수준은 40.7 mg/kg 이하, 독성은 162 mg/kg 초과로 제시되었다(사람 식품 기준 아님)[24]","같은 이유")
for n in ['Docosahexaenoic acid','Eicosapentaenoic acid','Linoleic acid']:
    crep(n,'part',"간(콜린 결핍 사료 시험 — 먹는 살 측정 아님)","사료 시험 간 지방산이 돌돔 살의 성분처럼 읽히지 않게")
crep('Choline','part',"간(어린 돌돔 사료 시험 — 먹는 살 측정 아님)","같은 이유")
src=d['sources'][34]; assert src['n']==35
old=src['title']; src['title']=old.replace("Environ Pollut 2020;265:115160","Environ Pollut 2020;266(Pt 3):115160")
assert old!=src['title']
changes.append({"where":"sources[35].title","before":"Environ Pollut 2020;265:115160","after":"Environ Pollut 2020;266(Pt 3):115160","why":"PubMed 32682185 서지 정보"})
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('/home/user/hfoodguide-wave3/docs/materials/oplegnathus-fasciatus/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
