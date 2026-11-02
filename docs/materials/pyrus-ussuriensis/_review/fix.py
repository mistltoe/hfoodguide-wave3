import json
p='/home/user/hfoodguide-wave3/docs/materials/pyrus-ussuriensis/dossier.json'
d=json.load(open(p))
changes=[]
def sec(key,old,new,why):
    for s in d['sections']:
        if s['key']==key:
            assert old in s['body'], (key,old)
            s['body']=s['body'].replace(old,new)
            changes.append({"where":f"sections.{key}","before":old,"after":new,"why":why}); return
    raise KeyError(key)
sec('overview','과육의 주된 당은 과당·포도당, 주된 유기산은 시트르산으로 보고되었다[4]',
    "중국 '롼얼(Ruaner)' 품종 과육의 주된 당은 과당·포도당, 주된 유기산은 시트르산으로 보고되었다[4]",
    "[4]는 '롼얼' 한 품종의 냉동–해동 과육만 분석함 — 종 전체로 일반화하지 않도록 품종 명시")
sec('overview','항염 효과[8]가 보고되었으나','LPS 유도 급성 폐 손상 모델의 항염 효과[8]가 보고되었으나',
    "[8]은 생쥐 LPS 급성 폐 손상 모델 — 모델을 밝혀 과장 방지")
sec('biology','중국 재배형 산돌배 열매는 둥글거나 납작한 원형에 황록색이며, 꽃받침이 남고 과육이 거칠며 석세포가 많다[4]',
    '산돌배 열매는 둥글거나 납작한 원형에 황록색이며, 꽃받침이 남고 과육이 거칠며 석세포가 많다고 기술된다[4]',
    "[4] 서론은 '재배형'으로 한정하지 않고 Ussurian pear 일반으로 기술함")
sec('cultivation',"대표 재배품종 '난궈'는 냉장 저장으로 후숙을 늦출 수 있지만, 오래 냉장한 뒤 상온에 꺼내면 껍질이 갈변하기 쉽다[21]",
    "대표 재배품종 '난궈'는 흔히 냉장 저장하지만, 오래 냉장한 뒤 상온에 꺼내면 껍질이 갈변하기 쉽다[21]",
    "[21] 초록은 냉장이 흔한 저장법이라고만 하고 '후숙을 늦춘다'는 말은 없음")
sec('safety','냉동 후 해동한 배는 막이 손상되어 폴리페놀이 산화되며 껍질이 갈색으로 변한다[4]',
    "냉동 후 해동한 '롼얼' 배는 껍질이 갈색으로 변하며, 연구진은 세포막 손상으로 폴리페놀이 산화되기 때문으로 추정했다[4]",
    "[4]는 막 손상을 'We infer'로 추정한 것 — 단정형을 추정으로 고침")
# compounds
for c in d['compounds']:
    if c['name']=='(+)-Catechin':
        old=c['activity_ko']
        c['activity_ko']="열매 분획에서 프로시아니딘 이량체·삼량체와 함께 (+)-카테킨이 동정되었고[8], 야생 열매 껍질·잎에서는 입체이성질체인 (−)-카테킨이 분리되었다[9]"
        c['part']="열매(70% 에탄올 용출 분획); (−)-카테킨은 열매 껍질·잎"
        changes.append({"where":"compounds.(+)-Catechin","before":old,"after":c['activity_ko'],"why":"[9] 초록은 (−)-catechin 을 분리함 — (+)-카테킨과 다른 이성질체"})
    if c['name']=='Oleanolic acid':
        old=c['part']
        c['part']="추출물 에틸아세테이트 분획(초록에 부위 명시 없음)"
        changes.append({"where":"compounds.Oleanolic acid.part","before":old,"after":c['part'],"why":"[11] 초록은 추출 부위를 밝히지 않음"})
# assays gradient
for a in d['assays']:
    g=a['conditions'].get('gradient','')
    if a['compound']=='Chlorogenic acid':
        a['conditions']['gradient']=''
        changes.append({"where":"assays[Chlorogenic acid].conditions.gradient","before":g,"after":"","why":"[3] Methods 에 등용매·기울기 언급 없음(이동상 비율만) — 원문에 없는 칸 비움"})
    elif a['compound'] in ('Fructose','Citric acid'):
        new='총 분석 시간 '+('25분' if a['compound']=='Fructose' else '30분')+'(원문에 등용매·기울기 언급 없음)'
        a['conditions']['gradient']=new
        changes.append({"where":f"assays[{a['compound']}].conditions.gradient","before":g,"after":new,"why":"[4] Methods 는 단일 조성 이동상과 총 분석 시간만 적음"})
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('/home/user/hfoodguide-wave3/docs/materials/pyrus-ussuriensis/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
