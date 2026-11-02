import json
P='/home/user/hfoodguide-wave3/docs/materials/chlamys-nobilis/'
d=json.load(open(P+'dossier.json'))
changes=[]
def rep(where,old,new,why):
    sec=[s for s in d['sections'] if s['key']==where][0]
    assert old in sec['body'],(where,old)
    sec['body']=sec['body'].replace(old,new); changes.append({"where":"sections."+where,"before":old,"after":new,"why":why})
rep('overview','건강기능식품 고시형 원료의 원재료는 아니어서 식약처가 정한 지표성분은 없다[1].',
    '건강기능식품 고시형 원료와 연결된 기록은 찾지 못해 식약처가 정한 지표성분은 다루지 않는다.',
    '[1] 식품원료 목록은 건강기능식품 고시 여부를 말하지 않음 — 출처 표시 제거, 서술 완화')
rep('related_species','웹 검색 요약에 따르면 EU 수산물 상업명 목록은 이 종을 Mimachlamys crassicostata 아래에 두었으나, 세계해양생물목록(WoRMS) 원문으로 현재 정명을 확인하지 못함[37]. 이 문서는 식품원료 목록의 학명을 따르고 이명 처리는 확인하지 못함으로 둔다.',
    '세계해양생물목록(WoRMS) 등 분류 데이터베이스에서 이 이름을 현재 정명으로 두는지, 다른 종명(예: Mimachlamys crassicostata)의 이명으로 두는지는 원 기록을 열지 못해 확인하지 못함. 이 문서는 식품원료 목록의 학명 Chlamys nobilis를 따른다.',
    '[37]은 WebSearch 요약만 본 EU 상업명 페이지로 분류 처리의 근거가 되지 못함 — 출처 삭제, 현재 학명 처리는 확인 불가로 명시')
rep('safety','식약처 「식품원료 목록」에서 이 종은 별도 조건 없이 \'사용가능\' 원료이며, 건강기능식품 고시형 원료가 아니어서 고시 섭취 시 주의사항은 없다[1].',
    '식약처 「식품원료 목록」에서 이 종은 별도 조건 없이 \'사용가능\' 원료이다[1]. 건강기능식품 고시형 원료와 연결된 기록은 찾지 못해 고시 섭취 시 주의사항은 해당하지 않는다.',
    '[1]은 사용가능 지위만 뒷받침 — 고시 관련 부분에서 출처 표시 분리')
rep('safety','마비성 패독이 이 종에서 자주 문제가 된다[21, 22].',
    '이 종은 마비성 패독을 몸에 쌓을 수 있다[21, 22].',
    '[22]는 실험실 먹이 전달 연구로 \'자주 문제\'를 뒷받침하지 않음 — 과장 완화')
rep('safety','내장에는 GTX1–3, C1+2, B1, dcGTX2+3 같은 독소가 들어 있었다[22].',
    '먹이 전달 실험에 쓴 유독 개체의 내장에는 GTX1–3, C1+2, B1, dcGTX2+3 같은 독소가 들어 있었다[22].',
    '[22] 초록: 실험에 쓴 toxic viscera — 맥락 보충')
rep('safety','2001년 주강 삼각주 시장 조사에서 이 종의 카드뮴은 사람의 일일 허용량과 현지 기준을 모두 넘었다[24].',
    '2001년 발표된 주강 삼각주 시장 조사(습중량 기준)에서 이 종의 카드뮴은 사람의 일일 허용량과 현지 기준을 모두 넘었다[24].',
    '[24] 초록에 조사 연도 없음(2001은 발표 연도), 습중량 기준 명시')
# assays
a=[x for x in d['assays'] if x['source']==[21]][0]
changes.append({"where":"assays[마비성 패독].part","before":a['part'],"after":"시장 시료(분석 부위는 초록에 명시 없음)","why":"[21] 초록에 분석 부위 없음"}); a['part']="시장 시료(분석 부위는 초록에 명시 없음)"
a=[x for x in d['assays'] if x['source']==[12]][0]
old=a['rationale']; a['rationale']="이 종의 금색·갈색 계통을 비교할 때 형질 지표로 쓰는 성분이다. 결과는 μg/g 건중량으로 계산한다[12]."
changes.append({"where":"assays[총카로티노이드].rationale","before":old,"after":a['rationale'],"why":"[12]는 고수온·저수온 내성 연구가 아님"})
c=[x for x in d['compounds'] if x['name']=='Astaxanthin'][0]
changes.append({"where":"compounds[Astaxanthin].part","before":c['part'],"after":"단백질 결합 실험(시험관)·장에서 분리한 세균","why":"[33] 단백질은 관자 유래로 명시되지 않음"}); c['part']="단백질 결합 실험(시험관)·장에서 분리한 세균"
# drop source 37 and renumber
used=set()
import re
txt=json.dumps({k:v for k,v in d.items() if k!='sources'},ensure_ascii=False)
d['sources']=[s for s in d['sources'] if s['n']!=37]
mp={s['n']:i+1 for i,s in enumerate(d['sources'])}
def rn(m):
    inner=m.group(1)
    parts=[]
    for p in re.split(r',\s*',inner):
        if '–' in p:
            a_,b_=p.split('–'); parts.append(f"{mp[int(a_)]}–{mp[int(b_)]}")
        else: parts.append(str(mp[int(p)]))
    return '['+', '.join(parts)+']'
for s in d['sections']: s['body']=re.sub(r'\[(\d+(?:[–,]\s*\d+)*)\]',rn,s['body'])
for lst in ('compounds','assays'):
    for x in d[lst]:
        x['source']=[mp[n] for n in x['source']]
        for k in ('content_text','activity_ko','content','rationale'):
            if k in x and isinstance(x[k],str): x[k]=re.sub(r'\[(\d+(?:[–,]\s*\d+)*)\]',rn,x[k])
for s in d['sources']: s['n']=mp[s['n']]
json.dump(d,open(P+'dossier.json','w'),ensure_ascii=False,indent=1)
json.dump(changes,open(P+'_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
