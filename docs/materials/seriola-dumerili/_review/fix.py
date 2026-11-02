import json,re,sys
p='/home/user/hfoodguide-wave3/docs/materials/seriola-dumerili/'
d=json.load(open(p+'dossier.json'))
changes=[]
S={s['key']:s for s in d['sections']}
def rep(key,old,new,why):
    b=S[key]['body']; assert old in b,(key,old); S[key]['body']=b.replace(old,new); changes.append({"where":"sections."+key,"before":old,"after":new,"why":why})
rep('history',' 국내에서는 2023년 경남도 수산자원연구소가 자연산 잿방어를 확보해 양식기술 개발에 착수했다는 보도가 있으나, 기사 원문은 열지 못해 검색 결과 요약으로만 확인했다[38].',' 국내의 잿방어 양식기술 개발 현황은 공식 자료로 확인하지 못함[31].',
    "[38] 지역 언론 기사는 원문을 열 수 없어(호스트 차단) 확인 불가·약한 출처이므로 문장과 출처 삭제; 앞 문장 출처로 '확인하지 못함' 표기")
rep('history','일본에서는 잿방어 양식에 중국에서 들여온 어린 고기를 쓰기도 했으며, 2008년 5월 가고시마현에서는 중국산 개체를 들여온 직후','일본에서는 2008년 5월 가고시마현의 잿방어 양식장에서 중국산 개체를 들여온 직후',
    "[32] 초록은 '중국에서 들여온 직후 발병'만 적고 어린 고기(치어) 사용 관행은 말하지 않음")
rep('history','2016–2025년 일본 방어류 양식장의 연쇄구균증(락토코쿠스균) 분리주 연구는','2016–2025년 일본 방어·잿방어·줄전갱이 양식장의 락토코쿠스균(Lactococcus) 분리주 62주를 분석한 연구는',
    "[33]은 락토코쿠스증(lactococcosis)이며 잿방어 외 2종 분리주가 섞여 있음을 명시")
rep('cultivation','생식소 자극 호르몬 유사체(GnRHa)를 서방형 이식체로 주면','생식소자극호르몬 방출호르몬 작용제(GnRHa)를 서방형 이식체로 주면',
    "[29] GnRHa는 Gonadotropin Releasing Hormone agonist(방출호르몬 작용제)로, '생식소 자극 호르몬 유사체'는 오역")
rep('cultivation','일본 방어류 양식에서는 락토코쿠스균 감염증이 주요 세균병이며, 2016–2025년 분리주에서','일본 방어속 양식에서는 락토코쿠스균 감염증이 주요 세균병이며, 방어·잿방어·줄전갱이의 2016–2025년 분리주에서',
    "[33] 분리주가 세 종에서 나왔음을 밝혀 종 혼동 방지")
rep('safety','마데이라 제도 셀바젠스 해역에서 잡힌 70 kg 잿방어에서는 CTX-1B, CTX-3C 등 시구아톡신이 확인되었고,','마데이라 제도 셀바젠스 해역에서 잡힌 70 kg 잿방어(5개 부위)와 같은 속 Seriola fasciata 1개체를 분석한 연구에서 CTX-1B, CTX-3C 등 시구아톡신이 검출되었으나 초록은 종별 검출 결과를 나누어 적지 않았고,',
    "[17] 초록은 잿방어와 S. fasciata 시료를 함께 분석했고 크로마토그램 결과를 종별로 구분하지 않음 — 근연종 결과 섞임 방지")
rep('genetics','이 초기 유전체(GCA_002260705.1)는 콘티그 N50이 0.25 Mb로 조각나 있었다[4].','2025년 연구는 가장 이른 공개 유전체 자원(GCA_002260705.1)이 콘티그 N50 0.25 Mb로 조각나 있었다고 평가했다[4].',
    "[4]는 GCA_002260705.1을 '가장 이른 유전체 자원'이라고만 하며 [5]의 2017년 초안과 같은 것이라고 말하지 않음")
# compounds
for c in d['compounds']:
    if c['name']=='Ciguatoxin 1B':
        old=dict(c)
        c['part']='분석 부위: 꼬리·배·몸통 근육, 머리, 간(마데이라 개체)'
        c['content_text']='마데이라 잿방어 70 kg 개체·S. fasciata 1개체 분석에서 m/z 1111.6으로 검출(초록은 종별·부위별 결과와 함량 수치를 적지 않음)'
        changes.append({"where":"compounds.Ciguatoxin 1B","before":old['content_text'],"after":c['content_text'],"why":"[17] 초록은 S. fasciata 시료도 함께 분석했고 종별 검출을 구분하지 않음"})
    if c['name']=='Arachidonic acid':
        old=c['content_text']
        c['content_text']='양식산은 미량, 자연산은 적은 양(잿방어·낫잿방어 두 종 공통으로 기술; 초록에 수치 없음)'
        changes.append({"where":"compounds.Arachidonic acid","before":old,"after":c['content_text'],"why":"[8] 초록은 이 경향을 두 종(In both species)에 대해 함께 적음 — 근연종 섞임 표시"})
for a in d['assays']:
    if a['compound'].startswith('Ciguatoxins'):
        old=a['content']
        a['content']='마데이라 셀바젠스산 잿방어 70 kg 개체(5개 부위)와 S. fasciata 1개체 추출물에서 CTX-1B(m/z 1111.6), CTX-3C(m/z 1023.5), CTX 유사체(m/z 1040.6), 카리브해/인도양형 CTX(m/z 1141.6) 검출 — 초록은 종별 결과를 구분하지 않음[17]'
        changes.append({"where":"assays.Ciguatoxins.content","before":old,"after":a['content'],"why":"[17] 초록상 두 종 시료 결과가 구분되지 않음"})
# sources: drop 38, renumber
src=[s for s in d['sources'] if s['n']!=38]
mp={}
for i,s in enumerate(src,1): mp[s['n']]=i; s['n']=i
upd={8:"Food Chem 2012;135(3):1718-29 (초록 확인)",10:"J Food Sci 2026;91(4):e70986 (초록 확인)",4:"Sci Data 2025;12(1):1998 (PMC 전문 확인)",36:"Genome 2018;61(6):457-466 (초록 확인)",44:"Theriogenology 2019;140:73-83 (초록 확인)",24:"Rev Bras Parasitol Vet 2022;31(2):e003022 (초록 확인)"}
for s in src:
    pass
d['sources']=src
def remap_text(t):
    def f(m):
        nums=[int(x) for x in re.split(r',\s*',m.group(1))]
        return '['+', '.join(str(mp[n]) for n in nums)+']'
    return re.sub(r'\[(\d+(?:,\s*\d+)*)\]',f,t)
def walk(o):
    if isinstance(o,dict):
        for k,v in o.items():
            if k=='source' and isinstance(v,list): o[k]=[mp[x] for x in v]
            elif k=='sources': continue
            else: o[k]=walk(v)
        return o
    if isinstance(o,list): return [walk(x) for x in o]
    if isinstance(o,str): return remap_text(o)
    return o
for k in list(d.keys()):
    if k!='sources': d[k]=walk(d[k])
# title updates by old number
inv={v:k for k,v in mp.items()}
for s in d['sources']:
    on=inv[s['n']]
    if on in upd:
        t=s['title']; t=re.sub(r'\.\s*[^.]*\d{4}[^.]*\((초록 확인|PMC 전문 확인)\)$','. '+upd[on],t)
        s['title']=t
    if on==31: s['title']=s['title'].replace('(초록 확인)','(PMC 전문 확인)')
json.dump(d,open(p+'dossier.json','w'),ensure_ascii=False,indent=1)
json.dump(changes,open(p+'_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
