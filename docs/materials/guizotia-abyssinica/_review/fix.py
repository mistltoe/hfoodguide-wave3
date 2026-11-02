import json,re,sys
p='/home/user/hfoodguide-wave3/docs/materials/guizotia-abyssinica/dossier.json'
d=json.load(open(p))
S={s['key']:s for s in d['sections']}
def rep(key,old,new):
    b=S[key]['body']; assert old in b,(key,old); S[key]['body']=b.replace(old,new)
rep('overview','니거(Guizotia abyssinica (L.f.) Cass.)는 국화과(Asteraceae)의 한해살이 기름작물로, 원산지 에티오피아에서는 누그(noug)라고 부른다[1][4].',
    '니거(Guizotia abyssinica (L.f.) Cass.)는 국화과(Asteraceae)의 기름작물로, 원산지 에티오피아에서는 누그(noug)라고 부른다[4][6].')
rep('history',' 영국·아일랜드 식물학회(BSBI) 자료는 에티오피아에서 4,000년 동안 기름작물로 재배되었고 1806년 무렵 영국 정원에 들어왔다고 적고 있다(검색 요약으로만 확인)[3].','')
rep('biology',' Kew 식물 목록(POWO)은 원산지를 아프리카 북동부 열대(에티오피아·에리트레아)로, 계절적으로 건조한 열대의 한해살이풀로 적고 있다(검색 요약으로만 확인)[2].','')
rep('genetics','2010년 발현 유전자 표지(EST) 25,711개와 엽록체 유전체가 처음 공개되었고','2010년 발현 유전자 표지(EST) 25,711개와 엽록체 유전체 서열이 공개되었고')
rep('cultivation','원 통계의 연도는 확인하지 못함.','원 통계의 연도는 확인하지 못함[8].')
rep('cultivation','올레산이 많은 계통도 높은 곳에서는 함량이 줄어,','저지대에서 올레산이 많다고 보고된 한 유전형도 이 시험에서는 높은 곳일수록 함량이 줄어,')
rep('safety',' 미국은 수입 니거 씨앗에 새삼 등 유해잡초 씨앗이 섞일 수 있어 열처리를 요구한다(검색 요약으로만 확인)[28]. 영국에서도 새모이용 수입 니거 씨앗에 다른 식물 씨앗이 섞여 들어온다고 보고되었다(검색 요약으로만 확인)[29].',
    ' 새모이용 수입 니거 씨앗의 잡초 씨앗 혼입과 그에 대한 각국 검역 기준은 원문을 열람하지 못해 확인하지 못함.')
rep('safety','같은 도시의 지역산 식용유는','같은 도시의 지역산 식용유(주로 니거 기름, 일부 해바라기 기름)는')
# renumber
drop={2,3,28,29}
old=[s['n'] for s in d['sources'] if s['n'] not in drop]
m={o:i+1 for i,o in enumerate(old)}
d['sources']=[dict(s,n=m[s['n']]) for s in d['sources'] if s['n'] not in drop]
def walk(o):
    if isinstance(o,dict):
        for k,v in list(o.items()):
            if k=='source' and isinstance(v,list): o[k]=[m[x] for x in v]
            elif k=='sources': continue
            else: o[k]=walk(v)
        return o
    if isinstance(o,list): return [walk(x) for x in o]
    if isinstance(o,str):
        def sub(mo):
            n=int(mo.group(1)); assert n not in drop,n; return '[%d]'%m[n]
        return re.sub(r'\[(\d+)\]',sub,o)
    return o
d=walk(d)
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
print(m)
