import json
from pathlib import Path
P=Path(__file__).resolve().parent.parent/"dossier.json"
d=json.loads(P.read_text())
changes=[]
def sec(k): return next(s for s in d['sections'] if s['key']==k)
def rep(where, obj, key, old, new, why):
    assert old in obj[key], (where, old)
    obj[key]=obj[key].replace(old,new); changes.append({"where":where,"before":old,"after":new,"why":why})

b=sec('biology')
rep("sections.biology", b,'body',"꽃은 암꽃만 피는 개체(암그루형)와 양성화 개체가 있으며, 'Manitoba 37'은 암꽃형으로 검은 열매를 맺는다[4].",
 "'Manitoba 37'은 암꽃(pistillate)형으로 검은 열매를 맺는다[4].",
 "[4] 의 양성화 형질은 교배 상대 'Seyval blanc'(교잡 품종)에서 온 것으로, 순수 V. riparia 에 양성화 개체가 있다는 근거가 아님")
rep("sections.biology", b,'body',"뿌리에서는 혹을 만들지 않는 Agrobacterium vitis 균주가 흔히 분리되었다[22].",
 "미국 뉴욕주 야생 개체 66그루 가운데 41그루의 뿌리에서 Agrobacterium vitis가 분리되었고, 조사한 균주는 모두 혹을 만들지 않았다[22].",
 "[22] 초록의 수치(66그루 중 41그루, 모두 비종양성)로 구체화")
c=sec('cultivation')
rep("sections.cultivation", c,'body',"원산지 북미에서 자생하며, 겨울이 추운 미국 미시간주의 숲 서식지에서도 토종 덩굴로 자란다[17].",
 "원산지 북미에서 자생하며, 미국 미시간주에서는 외래 덩굴 Celastrus orbiculatus와 같은 서식지에 자라는 토종 덩굴이다[17].",
 "[17] 초록에 '숲' 서식지 언급 없음")
g=sec('genetics')
rep("sections.genetics", g,'body',"효모 동화성 질소 관련 QTL이 확인되었다[5].","효모 동화성 질소 관련 QTL이 확인되었다[4, 5].",
 "[5] 초록은 V. riparia 부모를 'Manitoba 37'로 적지 않음 — 부모 이름은 [4] 전문(Methods)에서 확인")
rep("sections.genetics", g,'body',"말산 QTL은 1·6·8번 염색체에 놓였다[4].","말산 QTL은 1·6번 염색체에, 잠정 QTL은 8번 염색체에 놓였다[4].",
 "[4] 에서 8번 염색체는 모델링으로 찾은 잠정(potential) QTL")
s=sec('safety')
rep("sections.safety", s,'body',"포도주 실험에서 V. riparia 일부 계통의 메톡시피라진 농도(IBMP 350 pg/g 초과, IPMP 30 pg/g 초과)는 감각 역치를 크게 넘었는데, 이는 풍미 문제이지 독성 문제로 보고된 것은 아니다[6].",
 "V. riparia·V. cinerea 포도주의 메톡시피라진(IBMP·IPMP) 농도는 감각 역치를 크게 넘었고, 후속 조사에서 V. riparia·V. rupestris·V. cinerea 31개 계통의 열매 가운데 일부가 IBMP 350 pg/g 초과 또는 IPMP 30 pg/g 초과였다(어느 종의 계통인지는 초록에 없음). 이는 풍미 문제이지 독성 문제로 보고된 것은 아니다[6].",
 "[6] 초록: 31개 계통 조사는 포도주가 아니라 열매 조사이고 세 종을 합친 것이라 V. riparia 계통 값으로 단정할 수 없음")
p=sec('processing')
rep("sections.processing", p,'body',"캐나다 프레리 야생 베리 연구에서 '야생포도'는 총지방 7659 ± 312 μg/g 건조중량, 다가불포화지방산 74%로 조사 베리 중 가장 높았으나, 초록 표기에서 학명을 확인하지 못해 사막포도 값으로 단정하지 않는다[21].",
 "캐나다 프레리의 저이용 야생 베리 14종을 비교한 연구에서 야생포도(PubMed 제목·초록 색인에서 학명 Vitis riparia 확인)는 총지방 7659 ± 312 μg/g 건조중량으로 가장 높았고, 지방산 가운데 다가불포화지방산 비율도 74%로 가장 높았다[21]. 야생에서 채집한 열매를 분석한 한 연구의 값이고 씨를 포함한 열매 전체 기준인지 등 시료 조건은 초록에서 확인하지 못함[21].",
 "PubMed 검색 38920290[pmid] AND \"Vitis riparia\"[tiab] 가 일치(다른 Vitis 학명은 불일치) — 도구 출력에서 기울임 학명이 빠졌을 뿐 원 초록에 V. riparia 가 적혀 있음. 시료 조건 단서 추가")
for cp in d['compounds']:
    if cp['name']=='Malic acid':
        rep("compounds[Malic acid].activity_ko", cp,'activity_ko',"야생종 열매의 높은 신맛(적정산도 12.88–28.28 g/L 범위)과 강하게 상관[4]",
            "적정산도와 강하게 상관(조부모·부모·F2 평균 적정산도 12.88–28.28 g/L, 3개 연도)[4]",
            "[4] 의 적정산도 범위는 야생종 열매 값이 아니라 조부모·부모·F2 평균의 연도별 범위")
    if cp['name']=='Resveratrol':
        rep("compounds[Resveratrol].content_text", cp,'content_text',"V. riparia 등 14종 덩굴에서 9종 스틸벤 합계 약 2.2–19.5 g/kg 건조중량(종 범위)[10]",
            "V. riparia 포함 14개 분류군(교잡종 포함) 16개 덩굴의 가지(cane)에서 스틸벤 9종 합계 약 2.2–19.5 g/kg 건조중량(전체 범위, V. riparia 단독 값은 초록에 없음)[10]",
            "[10] 은 16개 덩굴·14개 분류군(V. × champini 등 교잡 포함)이며 범위는 전체 값")
for sr in d['sources']:
    if sr['n']==21:
        old=sr['title']; sr['title']=old.replace("초록 확인; 초록 표기에서 야생포도의 학명이 빠져 종 확인 못함","초록 확인; 야생포도 학명 Vitis riparia 는 PubMed 제목·초록 필드 검색으로 확인")
        changes.append({"where":"sources[21].title","before":old,"after":sr['title'],"why":"학명 확인됨"})
P.write_text(json.dumps(d,ensure_ascii=False,indent=1),encoding="utf-8")
json.dump(changes,open(Path(__file__).parent/"changes.json","w"),ensure_ascii=False,indent=1)
print(len(changes))
