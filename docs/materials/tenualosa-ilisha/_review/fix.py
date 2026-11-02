import json,re,sys
P='/home/user/hfoodguide-wave3/docs/materials/tenualosa-ilisha/'
d=json.load(open(P+'dossier.json'))
changes=[]
def sec(k): return next(s for s in d['sections'] if s['key']==k)
def rep(where,obj,key,old,new,why):
    v=obj[key]
    assert old in v,(where,old)
    obj[key]=v.replace(old,new); changes.append({'where':where,'before':old,'after':new,'why':why})

o=sec('overview')
rep('sections.overview',o,'body','건강기능식품 고시형 원료의 원재료 목록에는 없어 식약처가 정한 지표성분도 없다[1].','이번 조사에서 건강기능식품 고시형 원료와 연결된 기록은 찾지 못해 식약처가 정한 지표성분은 없다(card.json의 고시 목록 연결 항목 없음).','[1] 식품원료 목록은 건강기능식품 고시 여부를 말하지 않으므로 근거 표현을 조사 범위로 한정')
rep('sections.overview',o,'body','방글라데시·인도·미얀마에서는 맛과 향 때문에 가장 선호되는 식용어로 꼽히며','인도 서벵골·방글라데시와 인근 나라에서 맛과 향 때문에 수요와 소비자 선호가 높은 식용어이며','[14]·[15]는 서벵골·방글라데시(와 인근 나라)의 높은 수요·선호를 말할 뿐 미얀마나 "가장 선호"는 말하지 않음')

h=sec('history')
rep('sections.history',h,'body','1994년 고콜레스테롤혈증 환자가 힐사 100 g을 날마다 10개월 먹은 소규모 연구가 있었는데','1994년 고콜레스테롤혈증 환자가 힐사 100 g을 날마다 10개월 먹은 연구가 있었는데(참여자 수는 초록에 없음)','[32] 초록에 표본 수가 없어 "소규모"는 근거 없는 표현')

c=sec('cultivation')
rep('sections.cultivation',c,'body',' 방글라데시 수산부 집계를 인용한 언론 보도에 따르면 2022-23 회계연도 생산량은 57만 1천 t이었다(검색 요약으로만 확인)[34].',' 방글라데시 공식 연간 생산 통계는 원문을 열어 확인하지 못함.','[34]는 WebSearch 요약으로만 본 언론 보도이고 원문 사이트가 이 환경에서 열리지 않아(도메인 차단) 수치를 확인할 수 없음 — 삭제')

p=sec('processing')
rep('sections.processing',p,'body','크기가 커질수록 지방이 늘어 5 g 미만 5.68%, 800 g 초과 26.87%였다(원문에 건량·습량 기준 표기 없음)[14].','머리를 뗀 몸통(뼈 포함)을 갈아 분석한 인도 후글리 수계 시료에서는 크기가 커질수록 지방이 늘어 5 g 미만 5.68%, 800 g 초과 26.87%였다(원문에 건량·습량 기준 표기 없음)[14].','[14] Methods: 머리 제거 후 몸통 전체·토막을 갈아 분석, 시료에 뼈 포함 — 근육만의 값이 아님을 밝힘')

r=sec('related_species')
rep('sections.related_species',r,'body','납작전어는 중국 양쯔강의 상업 어종으로, 어민 면담 연구에서 1970년대 이후 크게 줄어든 종으로 기록되었다[12].','납작전어는 중국 양쯔강의 상업 어종으로, 어민 면담 연구에서 나이 든 어민일수록 그 감소를 더 잘 알아차린 종으로 기록되었다[12].','[12] 초록의 "1970년대 이후 큰 감소"는 바이지·주걱철갑상어 등 대형 동물에 대한 서술이며 납작전어는 고령 어민이 감소를 더 인지했다고만 씀')

s=sec('safety')
rep('sections.safety',s,'body','위해지수와 발암 위해는 허용 범위로 평가되었지만 납은 권고 기준 0.30 μg/g을 넘은 시료가 있었다[20].','위해지수와 발암 위해는 허용 범위로 평가되었지만, 납은 아가미(0.35·0.40 μg/g)와 장(건기 0.34 μg/g)에서 권고 기준 0.30 μg/g을 넘었다(근육은 기준 이하)[20].','[20] 전문: 기준 초과는 아가미·장이며 근육 납은 0.09·0.18 μg/g — 먹는 부위가 기준을 넘은 것처럼 읽히지 않게 고침')
rep('sections.safety',s,'body','방글라데시 여섯 지점 36개체 연구에서 위해지수는 1 미만이었지만 니켈은 하구·연안에서 식품 허용치와 발암 위해 기준을 넘었다[21].','방글라데시 여섯 지점 36개체 연구에서 위해지수는 1 미만이었지만, 니켈은 하구·연안 해역 시료에서 식품 허용치를 넘었고 발암 위해도 니켈만 기준을 넘었다[21].','[21] 초록: 허용치 초과는 하구·연안, 발암 위해 초과는 니켈 전체에 대한 서술(서식지 한정 아님)')
rep('sections.safety',s,'body','다른 연구는 비소 섭취에 따른 위해 가능성을 제기했다[23].','힐사와 Dorosoma cepedianum 두 종을 함께 다룬 연구는 비소의 비발암 위해와 카드뮴·크롬·비소의 발암 위해 가능성을 제기했다(채집 지역과 종별 수치는 초록에 없음)[23].','[23]은 두 종을 함께 평가한 연구이고 발암 위해 원소가 카드뮴·크롬·비소임 — 다른 종 자료가 섞였음을 밝힘')

d['world']=[]
changes.append({'where':'world[0]','before':'방글라데시 2023 production_t 571000 t [34]','after':'(삭제)','why':'WebSearch 요약으로만 확인한 언론 보도, 원문 열리지 않음(도메인 차단) — 확인 불가로 삭제'})

if '힐사' in d['aliases']:
    d['aliases'].remove('힐사'); changes.append({'where':'aliases','before':'힐사','after':'(삭제)','why':'국문 별명 "힐사"를 쓴 출처 없음(본문에서는 약칭으로만 씀)'})

cp={x['name']:x for x in d['compounds']}
def cr(name,key,new,why):
    old=cp[name][key]; cp[name][key]=new; changes.append({'where':f'compounds[{name}].{key}','before':old,'after':new,'why':why})
U='[16] 아미노산 표(Table 2)에 단위가 없어 절대값을 함량처럼 쓰지 않고 순위·변화율로 바꿈'
cr('Glutamic acid','content_text','튀김 연구의 날것 토막에서 가장 많은 아미노산(원문 표에 단위 없음, 12분 튀김 후 약 15% 증가)[16]; 알 14.20–14.60%[19]',U)
cr('Leucine','content_text','튀김 연구의 날것 토막에서 글루탐산·아스파르트산 다음으로 많았고, 12분 튀김 후 약 60% 줄었다(원문 표에 단위 없음)[16]',U)
cr('Lysine','content_text','12분 튀김 후 날것 대비 약 78% 줄었다(원문 표에 단위 없음)[16]',U)
cr('Histidine','content_text','12분 튀김 후 날것 대비 약 77% 줄었다(원문 표에 단위 없음)[16]',U)
cr('Leucine','activity_ko','인도 힐사(머리를 뗀 몸통 분석)의 모든 크기군에서 가장 많은 아미노산이었다[14]','[14] 시료는 근육만이 아니라 머리를 뗀 몸통')
cr('Docosahexaenoic acid','content_text','알(곤이) 총 지방산의 5.55–5.68% (C22:6n-3, 방글라데시 세 지역)[19]; 머리를 뗀 몸통 분석에서 5 g 미만 치어가 유의하게 높음(표 수치 확인 못함)[14]','[14] 시료는 근육만이 아니라 머리를 뗀 몸통(뼈 포함)')
cp['Docosahexaenoic acid']['part']='알·몸통'
cr('Myristic acid','content_text','날것 토막 지방산 조성의 30.22 ± 0.38%[16]; 인도 시료에서 주된 지방산 37.8% — 전문에 학명이 빠져 있어 "지방이 가장 많은(10.5%) 회유성 어종" 서술과 고찰의 힐사 문단(미리스트산이 주된 지방산)을 대응시킨 값[15]','[15] 전문 대조: 37.8%가 귀속된 종은 학명이 빠진 문장이며 회유성·최고 지방·고찰 문단으로 힐사임을 추론 — 추론 근거를 명시')
a=d['assays'][2]
old=a['content']
a['content']='날것 토막에서 글루탐산 > 아스파르트산 > 류신 순으로 많았고, 12분 튀김 후 라이신 약 78%, 히스티딘 약 77%, 류신 약 60% 감소(원문 표에 단위 없음)[16]'
changes.append({'where':'assays[2].content','before':old,'after':a['content'],'why':U})
a=d['assays'][0]
old=a['content']
a['content']='조지방 10.5%로 39종 중 최고, 미리스트산이 주된 지방산(37.8%), 단백질 20.7% — 전문에 학명이 빠져 "회유성 어종"·고찰의 힐사 문단 서술로 대응시킨 값[15]'
changes.append({'where':'assays[0].content','before':old,'after':a['content'],'why':'[15] 학명 누락 전문의 수치 귀속 근거를 명시'})

# drop source 34 and renumber
used=set()
txt=json.dumps({k:v for k,v in d.items() if k!='sources'},ensure_ascii=False)
for m in re.finditer(r'\[([\d,\s–-]+)\]',txt):
    for x in re.split(r'[,\s]+',m.group(1)):
        if x.isdigit(): used.add(int(x))
def walk(o):
    if isinstance(o,dict):
        for k,v in o.items():
            if k=='source' and isinstance(v,list): used.update(v)
            else: walk(v)
    elif isinstance(o,list):
        for v in o: walk(v)
walk({k:v for k,v in d.items() if k!='sources'})
print('unused',[s['n'] for s in d['sources'] if s['n'] not in used])
d['sources']=[s for s in d['sources'] if s['n'] in used]
mp={s['n']:i+1 for i,s in enumerate(d['sources'])}
for s in d['sources']: s['n']=mp[s['n']]
def remap_text(t):
    def f(m):
        parts=re.split(r'(\s*,\s*)',m.group(1))
        return '['+''.join(str(mp[int(p)]) if p.strip().isdigit() else p for p in parts)+']'
    return re.sub(r'\[(\d+(?:\s*,\s*\d+)*)\]',f,t)
def walk2(o):
    if isinstance(o,dict):
        for k,v in o.items():
            if k=='sources': continue
            if k=='source' and isinstance(v,list): o[k]=[mp[x] for x in v]
            elif isinstance(v,str): o[k]=remap_text(v)
            else: walk2(v)
    elif isinstance(o,list):
        for i,v in enumerate(o):
            if isinstance(v,str): o[i]=remap_text(v)
            else: walk2(v)
walk2(d)
print(mp)
json.dump(d,open(P+'dossier.json','w'),ensure_ascii=False,indent=1)
json.dump(changes,open(P+'_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
