import json,re
p='/home/user/hfoodguide-wave3/docs/materials/avena-nuda/dossier.json'
d=json.load(open(p))
S={s['key']:s for s in d['sections']}
changes=[]
def rep(where,obj,key,old,new,why):
    assert old in obj[key],(where,old)
    obj[key]=obj[key].replace(old,new); changes.append({"where":where,"before":old,"after":new,"why":why})

rep('sections.cultivation',S['cultivation'],'body',
 " 국내 '쌀귀리' 남부 가을 재배의 파종량·파종 시기 기술정보가 농사로에 있으나 원문은 열람하지 못했다[31].","",
 "출처 [31](농사로)은 이 환경에서 열리지 않아(도메인 차단) 원문 확인 불가, WebSearch 요약만으로는 근거가 안 되며 국내 '쌀귀리' 품종의 학명(A. nuda인지 A. sativa 껍질 없는 형인지)도 확인되지 않아 문장과 출처 삭제")
rep('sections.cultivation',S['cultivation'],'body',
 "허베이 바상 지역 포트 시험에서 출수 전후 8일간 가뭄을 주면",
 "허베이 바상 지역 포트 시험에서 절간신장–출수기 중 연속 8일간 가뭄을 주면",
 "[19] 초록: 가뭄 처리 기간은 'continual 8 days during the jointing-heading stage'")
rep('sections.processing',S['processing'],'body',
 "귀리쌀을 40–60초 도정하면 겨층이 깎이면서 전분·베타글루칸·용출 고형분이 늘고 기름·단백질은 줄었으며, 죽의 외관·향·맛·식감과 전체 기호도가 가장 좋았다[22].",
 "귀리쌀을 도정(0–80초)하면 겨층이 깎이면서 전분·베타글루칸·용출 고형분이 늘고 기름·단백질은 줄었으며, 도정 40초·60초에서 죽의 외관·향·맛·식감과 전체 기호도가 더 좋았다[22].",
 "[22] 초록: 성분 변화는 도정 전반의 경향이고, 40·60초는 관능 평가가 좋았던 조건")
rep('sections.processing',S['processing'],'body',
 "'Kamil' 품종 껍질 없는 귀리를 반죽의 60%로 넣은 빵",
 "'Kamil' 품종 껍질 없는 귀리를 60% 수준(O60)으로 넣은 빵",
 "[11] 전문: O30·O60은 발아 귀리 30%·60% 첨가 수준으로만 기재되어 '반죽의 60%'라는 기준은 확인되지 않음")
rep('sections.safety',S['safety'],'body',
 "러시아 껍질 없는 귀리 육성 계통 13점과 품종 2점의 T-2/HT-2 독소는 5–229 µg/kg으로, 같은 조건의 껍질 귀리 품종(790–1230 µg/kg)보다 낮았다[21].",
 "러시아에서 2019–2020년 재배한 껍질 없는 귀리 육성 계통의 T-2/HT-2 독소는 5–229 µg/kg으로, 함께 재배한 껍질 귀리 품종 1점(790–1230 µg/kg)보다 낮았다[21]. 이 논문은 대상을 학명으로 구분하지 않고 키워드에 Avena sativa를 적어, 큰쌀귀리(A. nuda)와 같은 대상인지는 확인하지 못함[21].",
 "[21] 초록: 5–229 µg/kg은 'naked oat lines' 범위이고 비교 대조 껍질 귀리는 품종 Yakov 1점; 논문 키워드가 Avena sativa라 종 동일성 단서 추가")
# renumber cross-refs in body: 32->31,33->32,34->33
for c in d['compounds']:
    if c['name'] in ('Isoschaftoside','Vitexin'):
        old=c['content_text']
        c['content_text']=old.replace("('Kamil', 초록 기준)","(껍질 귀리 'Noni'·껍질 없는 귀리 'Kamil' 실험 전체 초록 기준 — 종별 배수는 확인하지 못함)")
        changes.append({"where":f"compounds.{c['name']}.content_text","before":old,"after":c['content_text'],"why":"[10] 초록은 28배·5.3배 증가를 두 귀리 중 어느 쪽인지 밝히지 않아 'Kamil'로 귀속할 수 없음(겉귀리 A. sativa 자료 섞임 가능)"})
for a in d['assays']:
    if a['source']==[11]:
        old=a['conditions']['standard']
        a['conditions']['standard']="아베난쓰라마이드 A·B·C 분석 표준품(검량 방식 세부는 본문에서 확인하지 못함)"
        changes.append({"where":"assays[AVN].conditions.standard","before":old,"after":a['conditions']['standard'],"why":"[11] 전문에는 표준품 목록만 있고 '외부 검량'이라는 기재는 없음"})
        old=a['part']; a['part']="발아 씨앗(72시간)을 60% 수준(O60)으로 넣은 빵"
        changes.append({"where":"assays[AVN].part","before":old,"after":a['part'],"why":"첨가 기준(반죽 대비) 원문에 없음"})
# sources
src=[s for s in d['sources'] if s['n']!=31]
m={}
for s in src:
    nn=s['n'] if s['n']<31 else s['n']-1
    m[s['n']]=nn; s['n']=nn
d['sources']=src
for s in src:
    if 'Scientific Reports 2022' in s['title'] and 'drought' in s['title']:
        s['title']=s['title'].replace('Scientific Reports 2022','Scientific Reports 2022;12:11199')
    if 'J Nutr Biochem 2015' in s['title']:
        s['title']=s['title'].replace('J Nutr Biochem 2015','J Nutr Biochem 2015;26(12):1509-19')
    if 'Vavilovskii Zhurnal Genetiki i Selektsii 2021' in s['title']:
        s['title']=s['title'].replace('Vavilovskii Zhurnal Genetiki i Selektsii 2021','Vavilovskii Zhurnal Genetiki i Selektsii 2021;25(7):732-739')
def renum(txt):
    def f(mo):
        nums=[int(x) for x in re.split(r',\s*',mo.group(1))]
        return '['+', '.join(str(m.get(n,n)) for n in nums)+']'
    return re.sub(r'\[(\d+(?:,\s*\d+)*)\]',f,txt)
for s in d['sections']: s['body']=renum(s['body'])
for c in d['compounds']+d['assays']:
    c['source']=[m.get(n,n) for n in c['source']]
    for k in ('content_text','activity_ko','content','rationale'):
        if k in c and isinstance(c[k],str): c[k]=renum(c[k])
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('/home/user/hfoodguide-wave3/docs/materials/avena-nuda/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
