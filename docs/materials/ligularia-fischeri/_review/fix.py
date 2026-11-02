import json,re,sys
p=sys.argv[1]; d=json.load(open(p))
S={s['key']:s for s in d['sections']}
def rep(key,old,new):
    b=S[key]['body']; assert old in b,(key,old); S[key]['body']=b.replace(old,new)
rep('genetics','곰취의 엽록체 전체 유전체는 두 차례 보고되었다[12, 13].','곰취의 엽록체 전체 유전체는 2016년 처음 보고되었다[12].')
rep('genetics','2022년 보고에서는 길이 150,773 bp, 유전자 130개(단백질 암호 85, tRNA 37, rRNA 8), GC 함량 37.5%였다[13].',
    '2018년 중국 연구는 곰취를 포함한 곰취속 6종의 엽록체 유전체를 새로 해독했는데, 곰취 시료는 151,193 bp(대단일복사 83,301 bp, 소단일복사 18,232 bp, 역위반복 24,830 bp)였고 6종 모두 GC 함량 37.5%, 유전자 134개였다[29].')
rep('cultivation','근권 세균 172주 가운데 고른 ObRS-5 균주는','근권 세균 172주 가운데 고른 Enterobacter asburiae ObRS-5 균주는')
rep('safety','박새는 같은 PCR 연구에서 곰취가 아닌 원추리(Hemerocallis fulva)와의 혼동 쌍으로 다뤄졌고, 곰취-박새 혼동 사고의 1차 자료는 확인하지 못함. 식약처는 산나물과 독초 구별이 확실하지 않으면 채취·섭취하지 말라고 권고한 것으로 검색 요약에서 확인되었다(원문 미확인)[28].',
    '같은 PCR 연구에서 원추리(Hemerocallis fulva)와 짝지어진 독초는 박새(Veratrum patulum)가 아니라 같은 속의 Veratrum maackii였다[7]. 곰취와 박새를 혼동한 사고의 1차 자료와 산나물·독초 구별에 관한 식약처 보도자료 원문은 확인하지 못함.')
rep('safety','L. hodgsonii 추출물은 DNA 부가물을 만들었다[9, 10].','L. hodgsonii 추출물은 쥐 간 미소체와 반응시킨 시험관 실험에서 DNA 부가물을 만들었다[9, 10]. 곰취속 일부 종에 PA가 있어 종을 정확히 가리는 일이 안전상 중요하다는 지적이 있다[29].')
C={c['name']:c for c in d['compounds']}
c=C['3,4-Dicaffeoylquinic acid']; assert '(5–10 mg/kg 경구)' in c['activity_ko']; c['activity_ko']=c['activity_ko'].replace('(5–10 mg/kg 경구)','(5–10 mg/kg 경구, 동물 실험)')
c=C['Fischerisin A']; c['activity_ko']='뿌리에서 분리한 피셰리신 A·B가 KB·MCF-7 세포에 IC50 9.7–17.8 μM의 세포 독성을 보임(초록의 수치 배정이 모호해 화합물별 값은 확인하지 못함, 세포 실험)[31]'
# sources
for s in d['sources']:
    if s['n']==22: s['title']=s['title'].replace('Bacillus velezensis ObRS-5','Enterobacter asburiae ObRS-5')
    if s['n']==29: s['title']+=' — 곰취(L. fischeri) 엽록체 유전체 151,193 bp 포함'
drop={13,28}
keep=[s for s in d['sources'] if s['n'] not in drop]
mp={s['n']:i+1 for i,s in enumerate(keep)}
for s in keep: s['n']=mp[s['n']]
d['sources']=keep
REF=re.compile(r"\[(\d+(?:\s*[,–-]\s*\d+)*)\]")
def rn(t):
    if not isinstance(t,str): return t
    def f(m):
        parts=re.split(r"(\s*[,–-]\s*)",m.group(1))
        out=[]
        for x in parts:
            if x.strip().isdigit():
                n=int(x); assert n not in drop,(t,n); out.append(str(mp[n]))
            else: out.append(x)
        return '['+''.join(out)+']'
    return REF.sub(f,t)
def walk(o):
    if isinstance(o,dict):
        for k,v in o.items():
            if k=='source' and isinstance(v,list): o[k]=[mp[n] for n in v]
            elif k in ('title','url','publisher','accessed','n','compound','name'): continue
            else: o[k]=walk(v)
        return o
    if isinstance(o,list): return [walk(x) for x in o]
    return rn(o)
for k in ('sections','compounds','assays','markers','nutrients','production','world','gi','orgs'):
    d[k]=walk(d[k])
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
print(mp)
