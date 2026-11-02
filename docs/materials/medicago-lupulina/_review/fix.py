import json,re,sys
P='/home/user/hfoodguide-wave3/docs/materials/medicago-lupulina/'
d=json.load(open(P+'dossier.json'))
changes=[]
def rep(where,obj,key,old,new,why):
    s=obj[key]
    assert old in s,(where,old)
    obj[key]=s.replace(old,new)
    changes.append({"where":where,"before":old,"after":new,"why":why})
S={s['key']:s for s in d['sections']}
rep('sections.history',S['history'],'body',
 "국내에는 원래 자생하던 종이 아니라 들어와 퍼진 종으로 분류되며, 국내에 분포한다고 추정되는 개자리속 다섯 분류군 가운데 하나로 거론된다[26][27]. 들어온 시기와 경로는 이번 조사에서 확인하지 못함.",
 "국내 자생·귀화 여부와 들어온 시기·경로는 이번 조사에서 1차 출처로 확인하지 못함.",
 "[26](POWO)·[27](KoreaScience)은 원문을 열지 못하고 WebSearch 요약으로만 쓴 출처라 대조 불가 — 문장을 '확인하지 못함'으로 바꾸고 두 출처 삭제")
rep('sections.cultivation',S['cultivation'],'body',
 "영국 연구에서는 겉보기 건강한 묘의 98–99%가 잠복성 바이러스를 지니고 있었다[20][21]",
 "1987년 이탈리아 연구에서는 겉보기 건강한 묘 가운데 바이러스가 없는 개체가 1–2%뿐이었다(잠복성 바이러스)[20][21]",
 "[21] 저자 소속은 이탈리아(토리노) — '영국' 아님. 초록 표현('1-2%만 바이러스 없음')에 맞춤")
rep('sections.cultivation',S['cultivation'],'body',
 "광산 폐기물 토양에서 구리에 강한 뿌리혹세균과 공생하면 생육과 질소 함량이 늘고 뿌리의 구리 축적이 크게 늘었다[15].",
 "구리 200 mg/kg을 넣은 흙에서 뿌리혹세균(Sinorhizobium meliloti)과 공생하면 생육과 질소 함량이 늘고, 구리 흡수량이 지상부 34.0%, 뿌리 120.4% 늘어 뿌리 쪽 축적이 훨씬 컸다[15].",
 "[15] 초록은 '광산 폐기물 토양'이 아니라 Cu2+ 200 mg/kg 처리 조건; 수치 보강")
rep('sections.cultivation',S['cultivation'],'body',
 "밀과 함께 키우면 다이드제인·메디카르핀·포르모노네틴 등 플라보노이드 농도가 콩과 조직과 뿌리 분비물에서 늘었다[19]",
 "잔개자리·알팔파 등 콩과 4종을 밀과 함께 키우면 다이드제인·제니스테인·메디카르핀·포르모노네틴 등 플라보노이드 농도가 콩과 조직과 뿌리 분비물에서 늘었다(4종 전체 경향)[19]",
 "[19]는 알팔파 포함 4종 공통 결과 — 잔개자리 단독 결과처럼 읽히지 않게 함")
rep('sections.processing',S['processing'],'body',
 "물에 글리세롤 45% 또는 폴리프로필렌글리콜 10%를 섞어 70–80 °C에서 60분 초음파 추출하는 조건이 최적으로 제시되었다[2].",
 "글리세롤 45%(70 °C, 60분) 또는 폴리프로필렌글리콜 10%(80 °C, 60분) 수용액으로 초음파 추출하는 조건이 최적으로 제시되었다[2]. 이 시료는 꽃·줄기를 포함한 지상부 전체여서, 사용가능부위인 잎만의 결과로 볼 수는 없다[1][2].",
 "[2] 최적 조건은 용매별로 온도가 다름(글리세롤 70 °C, PPG 80 °C); 지상부(꽃·줄기 포함) 결과를 잎 원료 결과로 오해하지 않게 함")
rep('sections.processing',S['processing'],'body',
 "메탄올·에틸아세테이트 추출물을 비교한 2026년 연구에서는 잔개자리 에틸아세테이트 추출물의",
 "지상부 메탄올·에틸아세테이트 추출물을 비교한 2026년 연구에서는 잔개자리 에틸아세테이트 추출물의",
 "[4] 시료는 지상부")
rep('sections.safety',S['safety'],'body',
 "개자리속 씨앗·싹·마이크로그린도 쿠메스트롤과 트리테르펜 사포닌의 주요 원천으로 보고되었다[2][5]. 지상부 조추출물의 총사포닌은 건물 1 g당 90.4 mg(원문 단위 mg ESE/g, 표준물질 당량)으로 측정되었다[3].",
 "알팔파와 잔개자리를 묶은 개자리속 씨앗·싹·마이크로그린도 쿠메스트롤과 트리테르펜 사포닌의 주요 원천으로 보고되었다(종별 값은 원문 표에 있어 확인하지 못함)[2][5]. 지상부 조메탄올 추출물의 총사포닌은 90.4 mg ESE/g dw(표준물질 당량, 원문 표기)로 측정되었다[3].",
 "[5]의 결론은 알팔파·잔개자리를 묶은 속 단위 — 종 귀속 명시; [3] 'dw'가 식물 건물인지 추출물 기준인지 초록에서 불분명해 원문 표기로 둠")
C={c['name']:c for c in d['compounds']}
rep('compounds.Luteolin',C['Luteolin'],'content_text',"지상부 조추출물 건물 1 g당 0.37 mg으로","지상부 조메탄올 추출물에서 0.37 mg/g dw(원문 표기)로",
 "[3] 기준(식물 건물/추출물) 초록상 불분명 — 원문 표기 유지")
rep('compounds.Myricetin',C['Myricetin'],'content_text',"건물 1 g당 0.36 mg[3]","지상부 조메탄올 추출물에서 0.36 mg/g dw(원문 표기)[3]","같은 이유")
rep('compounds.Soyasaponin I',C['Soyasaponin I'],'content_text',
 "조사한 개자리속 5종(잔개자리 포함)의 잎 사포닌 추출물 모두에서 소량 검출[6]",
 "조사한 개자리속 5종(잔개자리 포함)의 잎 사포닌 추출물 모두에서 검출, 대부분 소량이나 한 종에서는 전체 사포닌의 50% 이상(어느 종인지는 원문 표에 있어 확인하지 못함)[6]",
 "[6] 원문: 모든 추출물에서 소량이지만 한 종에서는 50% 이상 — 잔개자리일 수 있어 '소량' 단정 삭제")
A=d['assays']
rep('assays[1].conditions.sample_prep',A[1]['conditions'],'sample_prep',"플라보노이드와 같은 산 가수분해 후 여과","",
 "[2] Methods의 산 가수분해 기술은 플라보노이드·페놀산용으로만 적혀 있고 쿠메스트롤 시료 처리는 원문에 없음 — 칸 비움")
rep('assays[2].content',A[2],'content',"조추출물 총 플라보노이드 건물 1 g당 1.27 mg, 루테올린 0.37 mg/g, 미리세틴 0.36 mg/g[3]",
 "조메탄올 추출물 총 플라보노이드 1.27 mg/g dw, 루테올린 0.37 mg/g dw, 미리세틴 0.36 mg/g dw(원문 표기)[3]","[3] 단위 원문대로")
# remove sources 26,27 and renumber
old=d['sources']; keep=[s for s in old if s['n'] not in (26,27)]
mp={s['n']:i+1 for i,s in enumerate(keep)}
for s in keep: s['n']=mp[s['n']]
d['sources']=keep
def rn(t):
    return re.sub(r'\[(\d+)\]',lambda m:'[%d]'%mp[int(m.group(1))],t)
def walk(o):
    if isinstance(o,dict):
        for k,v in o.items():
            if k=='source' and isinstance(v,list): o[k]=[mp[x] for x in v]
            else: o[k]=walk(v)
        return o
    if isinstance(o,list): return [walk(x) for x in o]
    if isinstance(o,str): return rn(o)
    return o
for k in ('sections','compounds','assays','markers','nutrients','production','world','gi','orgs','aliases'):
    d[k]=walk(d[k])
json.dump(d,open(P+'dossier.json','w'),ensure_ascii=False,indent=1)
json.dump(changes,open(P+'_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
