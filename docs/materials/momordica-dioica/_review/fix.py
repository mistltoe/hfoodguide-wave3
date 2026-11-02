import json,re,sys
p=sys.argv[1]
d=json.load(open(p,encoding='utf-8'))
S={s['key']:s for s in d['sections']}
def rep(key,old,new):
    b=S[key]['body']; assert old in b,(key,old); S[key]['body']=b.replace(old,new)
rep('biology',"익으면 초록에서 노랑·주황으로 바뀌고 속의 씨는 붉은 과육에 싸인다[3].",
    "익으면 초록에서 밝은 노랑·주황으로 바뀌며, 속에는 길이 6–7 mm의 약간 납작한 노랑~갈색 씨가 많이 들어 있다[3].")
rep('biology',"POWO 검색 요약에 따르면 자생지는 인도아대륙에서 미얀마까지(파키스탄·네팔·인도·스리랑카·방글라데시·아삼·히말라야)이고, 안다만·니코바르 제도에는 도입되었다[2].",
    "종설이 정리한 여주속 종별 분포표에서 이 종의 자생 범위는 '인도아대륙에서 미얀마까지'로 적혀 있다[3]. 나라별 자생·도입 구분은 원 분류 데이터베이스를 직접 열지 못해 확인하지 못함.")
rep('related_species',"확인할 필요가 있다(POWO 검색 요약에서도 renigera는 M. subangulata의 아종으로 따로 등재)[2, 6].",
    "확인할 필요가 있다[6].")
rep('related_species',"일본 연구는 kakrol이 여주(니가우리)보다 단맛이 있고 아스코르브산이 많아 요리에 쓰인다고 적었다[8].",
    "일본 연구는 kakrol이 여주(니가우리)보다 단맛이 있고 아스코르브산이 많아 요리에 쓰인다고 적었다[8]. 다만 이 'kakrol'이 아래에서 말하는 근연 분류군일 가능성은 배제되지 않는다[6].")
rep('processing',"kakrol 전체 동결건조 분말 3% 사료를 2주 먹인 쥐에서는 간 콜레스테롤·중성지방이 낮아지고 지방의 장 흡수가 줄었다[9].",
    "kakrol 전체 동결건조 분말 3% 사료를 2주 먹인 쥐에서는 간 콜레스테롤·중성지방이 낮아지고 지방의 장 흡수가 줄었다[9]. 두 연구는 재료를 학명 M. dioica의 'kakrol'로 적었지만, 방글라데시 등지에서 이 이름으로 재배되는 작물은 지금은 M. subangulata subsp. renigera로 보기도 하므로[6], 실제로 이 종의 결과인지는 확인되지 않았다.")
rep('safety',"열매 추출물의 혈당·지질 개선, 위궤양 억제, 신장 보호, 항알레르기 효과와 잎 추출물의 간 보호 효과는 모두 쥐·생쥐·세포 실험 결과이다[3, 8, 10, 20, 23].",
    "열매 추출물의 혈당·지질 개선, 위궤양 억제, 신장 보호, 항알레르기 효과와 잎 추출물의 간 보호 효과는 모두 쥐·생쥐·세포 실험 결과이며, 이 가운데 'kakrol'로 표시된 재료는 근연 분류군일 가능성도 있다[3, 6, 8, 10, 20, 23].")
rep('safety',"1,000 mg/kg 아급성 투여에서 경미한 독성이, 100·250 mg/kg 장기 투여에서는 이상이 없었다고",
    "아급성 시험(250·500·1,000 mg/kg)의 최고 용량에서 경미한 독성이, 아만성·만성 시험(100·250·500 mg/kg)에서는 이상 소견이 없었다고")
for c in d['compounds']:
    if c['name']=='beta-Carotene':
        c['content_text']="종설은 '가식부 100 g당 162 mg'이라 적었으나(1차 자료 확인 못함), 채소의 카로틴 함량으로는 비정상적으로 높아 μg 단위의 오기일 가능성이 있음 — 수치로 쓰지 말 것[4]"
    if c['name'] in ('Oleic acid','Linoleic acid'):
        c['part']="열매(종설 표 4 '지방산 조성', 본문에 열매 지방산이라 적음)"
for n in d['nutrients']:
    if n['form']=='열매 건물':
        n['items']=[i for i in n['items'] if i['name'] not in ('칼륨','나트륨','칼슘','철','아연')]
        n['basis']="종설[4]이 인용한 건물 기준 값(%·kcal/100 g 원문 단위). 같은 문단의 무기질 값(칼륨 4.63 mg/100 g 건물 등)은 건물 기준으로 비정상적으로 낮아 단위 오류가 의심되므로 넣지 않음"
# drop source 2, renumber
old=[s['n'] for s in d['sources']]
d['sources']=[s for s in d['sources'] if s['n']!=2]
m={}
for i,s in enumerate(d['sources'],1): m[s['n']]=i; s['n']=i
def rb(t):
    def f(mo):
        nums=[int(x) for x in re.split(r',\s*',mo.group(1))]
        assert 2 not in nums,t[:80]
        return '['+', '.join(str(m[x]) for x in nums)+']'
    return re.sub(r'\[(\d+(?:,\s*\d+)*)\]',f,t)
def walk(o):
    if isinstance(o,dict):
        for k,v in o.items():
            if k=='source' and isinstance(v,list): o[k]=[m[x] for x in v]
            elif k=='sources': continue
            else: o[k]=walk(v)
        return o
    if isinstance(o,list): return [walk(x) for x in o]
    if isinstance(o,str): return rb(o)
    return o
for k in list(d):
    if k!='sources': d[k]=walk(d[k])
json.dump(d,open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('ok')
