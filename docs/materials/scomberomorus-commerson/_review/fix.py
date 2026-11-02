import json,re
d=json.load(open('dossier.json'))
S={s['key']:s for s in d['sections']}
def rep(key,a,b):
    s=S[key]; assert a in s['body'],(key,a); s['body']=s['body'].replace(a,b)
rep('overview','살의 독성 원소는 세계 메타분석에서 대체로 위해 지수 1 미만으로 평가되었다[22].',
 '여러 나라 문헌을 합친 메타분석에서 살의 독성 원소 총 위해 지수는 성인 기준으로 모든 나라에서 1 미만이었으나, 어린이 기준으로는 말레이시아·필리핀에서 1을 넘었다[22].')
rep('history','이어졌다[5, 6]. 같은 해 남조류 Trichodesmium erythraeum의 독소가 이 종 살의 독소와 크로마토그래피상 구별되지 않는다는 가설도 제시되었다[40].','이어졌다[6].')
rep('biology','[33, 34, 35]','[33, 35]')
rep('related_species','\n\n삼치속 14종의 COI 서열 150개를 분석한 연구는 5종이 단일 계통을 이루지 않았고 공개 데이터베이스에 잘못 동정된 표본이 있음을 밝혀, 이 속은 형태만으로 종을 구별하기 어렵다고 보고했다[21]. 미토콘드리아 유전체 계통수에서도 삼치속은 하나의 무리를 이루었다[16].','')
rep('genetics','오스트레일리아 시료의 미세위성 7좌위 분석에서는','미세위성 7좌위 분석에서는')
rep('safety','검출 사이 관계는 보이지 않았다[7].','검출 사이 관계는 보이지 않았으며, 이 무작위 표본의 양성 어류로 인한 중독 보고는 연구 시점까지 없었다[7].')
rep('safety','세계 문헌 메타분석에서 필레의 메틸수은 평균은 66.60 μg/kg(습중량), 납 180.99 μg/kg, 카드뮴 66.03 μg/kg이었고 나라별 총 위해 지수는 모두 1 미만이었다[22].',
 '여러 나라 문헌을 합친 메타분석에서 필레의 메틸수은 평균은 66.60 μg/kg(습중량), 납 180.99 μg/kg, 카드뮴 66.03 μg/kg이었고, 나라별 총 위해 지수(TTHQ)는 성인 기준 모두 1 미만이었으나 어린이 기준으로 말레이시아(1.04)·필리핀(1.02)은 1을 넘었다[22].')
rep('safety','페르시아만·아라비아해 개체에서는 사람에게 옮을 수 있는 아니사키스류·히스테로틸라키움류 선충 유충이 보고되었다[36, 37].',
 '페르시아만에서 이 종을 포함한 식용 어류 5종 600마리를 조사한 연구는 사람에게 옮을 가능성이 있는 아니사키스류·히스테로틸라키움류 선충 5분류군을 확인했으나, 어종별 검출 결과는 초록에서 확인하지 못함[36].')
rep('processing','바레인 전통 조리에서 튀긴 동갈삼치의 에너지는 894.2 kJ/100 g, 밥과 함께 조리한 것은 867.3 kJ/100 g으로 조사 어종 가운데 가장 높았다[26].',
 '바레인 전통 조리 시료(조리된 상태 100 g 기준)에서 튀긴 동갈삼치의 에너지는 894.2 kJ/100 g, 밥과 함께 조리한 것은 867.3 kJ/100 g으로, 함께 조사한 어류 8종·새우 1종의 조리 시료 가운데 가장 높았다[26].')
C={c['name']:c for c in d['compounds']}
C['Ciguatoxin CTX1B']['content_text']=C['Ciguatoxin CTX1B']['content_text'].replace('(중독 관련 시료)','(시가테라 독성 어류 살)')
C['Ciguatoxin 3']['activity_ko']='개선한 추출법과 HILIC 정제를 함께 쓰면 검출량이 71% 늘어난 동족체다[9]'
C['Methylmercury']['activity_ko']='대형 포식 어류에 쌓이는 신경독성 오염물질이며, 이 메타분석의 독성 원소 총 위해 지수는 성인 기준 1 미만, 어린이 기준 일부 나라(말레이시아·필리핀)에서 1 초과였다[22]'
for c in d['compounds']:
    c['content_text']=c['content_text'].replace('메타분석 평균','여러 나라 연구 합산 메타분석 평균')
for n in d['nutrients']:
    n['form']=n['form'].replace(')',', 조리된 시료)')
d['aliases']=[a for a in d['aliases'] if a!='Spanish mackerel']
# renumber
drop={5,21,34,37,40}
old=d['sources']; keep=[s for s in old if s['n'] not in drop]
m={s['n']:i for i,s in enumerate(keep,1)}
for s in keep: s['n']=m[s['n']]
d['sources']=keep
def rn(t):
    def f(mm):
        nums=[int(x) for x in re.split(r',\s*',mm.group(1))]
        assert not set(nums)&drop,(t,nums)
        return '['+', '.join(str(m[x]) for x in nums)+']'
    return re.sub(r'\[(\d+(?:,\s*\d+)*)\]',f,t)
def walk(o):
    if isinstance(o,dict):
        for k,v in o.items():
            if k=='source' and isinstance(v,list): o[k]=[m[x] for x in v]
            elif k!='sources': o[k]=walk(v)
        return o
    if isinstance(o,list): return [walk(x) for x in o]
    if isinstance(o,str): return rn(o)
    return o
for k in d:
    if k!='sources': d[k]=walk(d[k])
json.dump(d,open('dossier.json','w'),ensure_ascii=False,indent=1)
print(len(keep))
