import json
P='dossier.json'
d=json.load(open(P))
changes=[]
def sec(key,old,new,why):
    for s in d['sections']:
        if s['key']==key:
            assert old in s['body'],(key,old)
            s['body']=s['body'].replace(old,new); changes.append({"where":f"sections.{key}","before":old,"after":new,"why":why}); return
    raise KeyError(key)
sec('overview',"그루미샤마(grumixama)라고 부른다[12, 29].","그루미샤마(grumixama)라고 부른다[12, 13].",
    "[29] 초록에는 grumixama 명칭이 없음; [13] 초록이 'grumixama' 명칭을 씀")
sec('biology',"에우게니아속 식물은 마주나는 홑잎에 투명한 기름샘이 있고 장과 모양의 살진 열매를 맺는다[29].",
    "에우게니아속을 포함한 브라질 도금양과 식물은 대체로 마주나는 홑잎에 투명한 기름샘이 있고 장과 모양의 살진 열매를 맺는다[29].",
    "[29] 초록은 이 형질을 도금양과 브라질 종 전반의 특징으로 씀(속 고유 형질 아님)")
sec('biology',"과육 향기 성분은 세스퀴테르펜이 85.7%를 차지했다[8].",
    "과육에서 확인된 휘발성 성분 14종 가운데 85.7%(성분 수 기준, DVB/CAR/PDMS 섬유)가 세스퀴테르펜이었다[8].",
    "[8] 전문: 85.7%는 확인된 성분 수(14종 중 12종)의 비율이지 함량 비율이 아님")
sec('processing',"연구진은 50 °C 이하로 다루고 자외선을 피하라고 권했다[2].","연구진은 50 °C 미만에서 다루고 자외선을 피하라고 권했다[2].",
    "[2] 결론 원문 'lower than 50 °C'")
sec('processing',"4 °C에서 48시간 두면 안토시아닌이 40.8% 줄었다[31].",
    "세 과일 우림물을 4 °C에서 48시간 두자 안토시아닌 손실이 40.8%에 이르렀다(이 종만의 값은 초록에서 구분되지 않음)[31].",
    "[31] 초록의 40.8%는 그루미샤마·cereja-do-Rio-Grande·araçaúna 우림물 전체에 대한 값으로, 이 종 단독 값으로 쓸 수 없음")
sec('processing',"14일째 지질 산화 지표(TBARS)가 약 0.3으로 대조군(0.5 초과)보다 낮았다[21].",
    "14일째 지질 산화 지표(TBARS)가 약 0.3 mg MDA/kg으로 대조군(0.5 mg MDA/kg 초과)보다 낮았다[21].",
    "[21] 초록 단위(mg MDA/kg) 누락 보완")
sec('processing',"요구르트에 과육을 넣으면 소화 모사 뒤 유산균 생존율이 높았다[32].",
    "요구르트에 과육을 넣으면 소화 모사 뒤 프로바이오틱 균(L. acidophilus·B. animalis) 생존율이 더 높았다[32].",
    "[32] 초록은 L. acidophilus·B. animalis 두 균주를 말함(비피도박테리움은 유산균으로 묶기 부정확)")
sec('cultivation',"상파울루·미나스제라이스주 세 수집원의 73개체를 분석한 연구는",
    "상파울루주 세 수집원(나티비다지다세하·피라시카바·파라이부나)의 73개체를 분석한 연구는",
    "[6] 전문: 이 종의 수집원 3곳은 모두 상파울루주; 미나스제라이스주는 다른 두 종(uvaia·Rio Grande cherry) 수집지")
sec('safety',"잎 추출물은 생쥐에서 항우울제와 함께 줄 때 효과가 더해졌으므로, 잎 제품을 약과 함께 먹는 것은 신중해야 하나 사람 자료는 확인하지 못함[35].",
    "수알코올 추출물(초록에 부위 명시 없음)은 생쥐 꼬리 매달기 시험에서 효과 없는 낮은 용량의 항우울제(플루옥세틴·이미프라민·부프로피온)와 함께 줄 때 항우울 유사 효과를 냈다[35]. 사람에서의 약물 상호작용 자료는 확인하지 못함.",
    "[35] 초록은 추출 부위를 밝히지 않음; 동물 결과에서 사람 복용 권고를 끌어낸 과장 제거")
# compounds
for c in d['compounds']:
    if c['name']=='Catechin':
        old=c['activity_ko']; c['activity_ko']="잎에서 분리되어 생쥐 귀 부종 모델(국소 적용)에서 항염 효과[26]"
        changes.append({"where":"compounds.Catechin.activity_ko","before":old,"after":c['activity_ko'],"why":"[26] 초록은 크로톤유·아라키돈산 귀 부종 모델만 다룸(흉막염 모델 없음)"})
    if c['name']=='Pelargonidin 3-glucoside':
        old=c['content_text']; c['content_text']="38.89 ± 3.01 µg/g(생중량)[5]"
        changes.append({"where":"compounds.Pelargonidin 3-glucoside.content_text","before":old,"after":c['content_text'],"why":"[5] 표 1의 펠라르고니딘 행은 네 과일 중 세 값만 있어 0.21%가 이 종의 값인지 확정할 수 없음(피탕가 등 다른 과일 값 섞임 위험)"})
# aliases / name_en
old=d['aliases'][:]
d['aliases']=[a for a in d['aliases'] if a!='Brazilian cherry']
changes.append({"where":"aliases","before":json.dumps(old,ensure_ascii=False),"after":json.dumps(d['aliases'],ensure_ascii=False),"why":"식약처 목록에서 'Brazilian cherry'는 Surinam-cherry열매(Eugenia uniflora)의 영어명이므로 별명 검색에서 피탕가와 섞일 위험; 이 종의 영어 통용명 설명은 related_species 본문에 유지"})
old=d['name_en']; d['name_en']="Grumixama"
changes.append({"where":"name_en","before":old,"after":"Grumixama","why":"같은 이유('Brazilian cherry'는 목록상 E. uniflora 영어명)"})
json.dump(d,open(P,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
