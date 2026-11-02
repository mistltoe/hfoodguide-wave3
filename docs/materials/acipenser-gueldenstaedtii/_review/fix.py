import json,re
p='dossier.json'; d=json.load(open(p))
S={s['key']:s for s in d['sections']}
changes=[]
def rep(key,old,new,why):
    b=S[key]['body']; assert old in b,(key,old); S[key]['body']=b.replace(old,new); changes.append({"where":"sections."+key,"before":old,"after":new,"why":why})
rep('overview','이 문서에 실은 식품 성분·가공 연구의 고기·알 시료는 양식 개체에서 얻은 것이다[15, 18, 20].',
 '식품 성분·가공 연구의 고기·알 시료는 중국의 양식 고기[20]와 철갑상어 수산식품 업체가 공급한 알[15]이고, 미량원소·남조류 독소 조사의 근육 시료는 카스피해·그리스 담수에서 채집한 개체여서[26, 27] 양식·야생 시료를 구분해 적었다.',
 '[18] 초록은 양식 여부를 밝히지 않고, 안전성 절의 [26]·[27]은 야생 채집 시료여서 "모두 양식 시료"는 과잉 일반화')
rep('history','미국의 한 연구는 이 종을 위급 상태의 알 생산 종으로 소개하며 수족관에서 기르는 성어의 혈액 기준값을 처음 정리했다[11].',
 '미국의 한 연구는 이 종을 위급 상태의 알 생산 종으로 소개하며, 이 종의 혈액 기준값 자료가 매우 적다는 점에서 수족관에서 관리하는 양식 출신 성어의 혈액 기준 범위를 정리했다[11].',
 '[11] 초록은 "처음"이라고 쓰지 않음(자료가 매우 적다고만 씀); 시료는 aquacultured adult')
rep('biology','담수(0.42 psu)와 기수(9.0 psu)에서 먹이 속 미량원소의 흡수율을 비교했다[2]',
 '담수(0.42 psu)와 기수(9.0 psu)에서 먹이로 준 방사성 추적 원소 8종의 동화 효율을 비교했다[2]',
 '[2]는 방사성 동위원소 추적자로 동화 효율을 잰 실험')
rep('biology','1–4세 양식 개체를 조사한 연구에서','1–4세 개체를 조사한 연구에서','[14] 초록에 양식 여부 기재 없음')
rep('related_species','시베리아철갑상어 암컷과 이 종 수컷의 잡종도 실험에 쓰이므로, 이 문서는 잡종 자료를 이 종 자료로 옮기지 않았다[35]. 핵 유전자·미세위성·미토콘드리아 표지를 함께 쓰는 판별법은 이 종을 포함한 다섯 종과 bester 등 잡종을 구별하도록 만들어졌다[28]. 중국 시장 캐비아 21개 배치를 DNA 바코딩한 연구에서 이 종은 확인된 모계 종 가운데 하나였고, 33.4%라는 종 표시 오류율은 이 종만이 아닌 전체 시료의 값이다[29].',
 '핵 유전자·미세위성·미토콘드리아 표지를 함께 쓰는 판별법은 이 종을 포함한 다섯 종과 bester 등 잡종을 구별하도록 만들어졌다[28]. 이 연구에서 미세위성만으로는 이 종과 시베리아철갑상어를 가르지 못했고 COI 바코딩도 근연 복합체 종을 구별하지 못해, 비멘틴 등 핵 유전자 표지가 함께 필요했다[28]. 하류 다뉴브에서 잡힌 출처 미상 잡종 하나는 스털렛 암컷과 이 종 수컷의 잡종으로 판별되었으며, 이런 잡종 자료는 이 문서에서 이 종 자료로 옮기지 않았다[28].',
 '[35](잡종 A. baerii♀×A. gueldenstaedtii♂ 사료 실험)은 이 종 자료가 아니어서 삭제; [29]는 전문에서 종명이 빠져 이 종이 모계 종으로 확인됐는지 대조 불가하고 캐비아 일반 자료라 삭제; [28] 전문에서 미세위성·COI 한계와 잡종 H204(♀ARU×♂AGU) 확인')
rep('cultivation','양식의 주목적은 캐비아 생산이다[10]','캐비아 생산 면에서 경제적 가치가 크다[10]','[10] 초록은 "considerable economic value for caviar production"')
rep('cultivation','기대 유전 획득량은','농가 합의로 정한 목표(희망) 유전 획득량은','[8]은 desired genetic gains(목표치)이지 기대 반응이 아님')
rep('processing','중국 저장성 취저우의 양식 업체에서 받은 이 종의 알을','중국 취저우의 철갑상어 수산식품 업체가 공급한 이 종의 알을','[15] 전문: 수산식품 과학기술 개발 업체가 공급(양식장이라고 쓰지 않음)')
rep('processing','저장 3–4주가 품질 유지에 적당하다고 보았다[15]','관능 평가에서 3주·4주 저장 시료가 한 무리로 묶였고 저장이 길어질수록 품질이 떨어졌다[15]','[15] 전문에 "3–4주가 품질 유지에 적당" 이라는 결론 없음 — 3·4주 시료가 관능상 한 무리였다고만 씀')
rep('processing','저온 진공 가열(50–70 °C) 필레에서는','저온 진공 가열 필레에서는','[19] 초록에 가열 온도 범위 없음(50–70 °C는 [20]의 조건)')
rep('safety','냉장 고기의 주요 부패균으로 Pseudomonas fluorescens가 분리되었다[21].','냉장 수산물의 주요 부패균인 Pseudomonas fluorescens를 이 종에서 분리해 항균 소재(알킬 갈레이트) 시험에 썼다[21].','[21]은 P. fluorescens 를 수산물 일반의 주요 부패균으로 소개하고 이 종에서 분리했을 뿐, 이 종 고기의 주요 부패균임을 조사한 것이 아님')
# compounds
for c in d['compounds']:
    if c['name']=='Chondroitin sulfate':
        old=c['activity_ko']; c['activity_ko']='시험관 항산화 활성이 상어·소 유래보다 높고 제1형 콜라겐 섬유 형성을 억제(시험관 결과이며, A. sinensis 와 이 종의 CS를 묶어 보고한 값)[24]'
        changes.append({"where":"compounds.Chondroitin sulfate.activity_ko","before":old,"after":c['activity_ko'],"why":"[24] 초록은 활성을 두 종 철갑상어 CS 전체(sturgeon CS)로 보고 — 이 종 단독 결과 아님"})
    if c['name']=='Hexanal':
        old=c['name_ko']; c['name_ko']='헥산알'; c['content_text']='냉장 저장 중 함량 변화가 큰 휘발 성분(노난알과 함께 언급, 초록에 수치 없음)[16]'
        changes.append({"where":"compounds.Hexanal.name_ko","before":old,"after":"헥산알","why":"name(Hexanal)과 한글명 일치"})
a=d['assays'][2]
old=a['compound_ko']
a['compound']='Volatile compounds with OAV>1 (16 incl. 3-methylbutanal, hexanal, nonanal, (E,Z)-2,6-nonadienal)'
a['compound_ko']='휘발성 향 성분 16종(OAV>1; 3-메틸부탄알 등 알데하이드와 알코올·케톤·테르펜 포함)'
changes.append({"where":"assays[2].compound_ko","before":old,"after":a['compound_ko'],"why":"[15] 전문: 16종에는 1-옥텐-3-올·2-헵탄온·카리오필렌 등 알데하이드가 아닌 성분도 포함"})
# remove sources 29,35 and renumber
drop={29,35}
olds=[s for s in d['sources'] if s['n'] not in drop]
m={s['n']:i+1 for i,s in enumerate(olds)}
for s in olds: s['n']=m[s['n']]
d['sources']=olds
def rn(t):
    def f(mo):
        nums=[int(x) for x in re.findall(r'\d+',mo.group(1))]
        assert not (set(nums)&drop),t
        return '['+', '.join(str(m[x]) for x in nums)+']'
    return re.sub(r'\[(\d+(?:,\s*\d+)*)\]',f,t)
def walk(o):
    if isinstance(o,dict):
        for k,v in o.items():
            if k=='source' and isinstance(v,list): o[k]=[m[x] for x in v]
            elif k=='source' and isinstance(v,int): o[k]=m[v]
            else: o[k]=walk(v)
        return o
    if isinstance(o,list): return [walk(x) for x in o]
    if isinstance(o,str): return rn(o)
    return o
srcs=d.pop('sources'); d=walk(d); d['sources']=srcs
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes),len(srcs))
