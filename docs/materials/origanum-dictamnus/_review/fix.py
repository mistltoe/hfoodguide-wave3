import json,re
P='/home/user/hfoodguide-wave3/docs/materials/origanum-dictamnus/dossier.json'
d=json.load(open(P))
S={s['key']:s for s in d['sections']}
changes=[]
def rep(key,old,new,why):
    b=S[key]['body']; assert old in b,(key,old)
    S[key]['body']=b.replace(old,new); changes.append({"where":"sections."+key,"before":old,"after":new,"why":why})

rep('overview',"영어로는 Dittany of Crete 또는 Cretan dittany 라고 부르며, 크레타에서는 잎과 꽃으로 우린 차를 '크레타 차(Cretan tea)'로 마셔 왔다[1, 12].",
 "영어로는 Dittany of Crete 또는 Cretan dittany 라고 부르며[1, 6], 크레타에서는 이 풀로 우린 차를 '크레타 차(Cretan tea)'로 마셔 왔다[12].",
 "[1] 식품원료 목록은 차 음용을 말하지 않음; 영명 Cretan dittany 는 [6] 제목, 차 음용은 [12] 근거")
rep('overview',"건강기능식품 고시형 원료의 원재료로 등록된 기록은 확인하지 못함.",
 "같은 목록에는 식품첨가물(B코드) '천연향료(Dittany of Crete)'도 사용가능으로 올라 있다[1]. 건강기능식품 고시형 원료의 원재료로 등록된 기록은 확인하지 못함.",
 "I1020 로컬 원자료에 B코드 천연향료(Dittany of Crete) 행이 있어 추가")
rep('overview',"유럽의약품청(EMA)은 기침·가벼운 위장 불편에 쓰는 전통 약초차 단행본을 두고 있다고 검색 요약에서 확인했으나 원문은 열어 보지 못했다[18].",
 "유럽의약품청(EMA)이 이 풀의 약효와 권고를 담은 단행본을 승인했다고 소개하는 논문이 있으나[7], 단행본 원문의 적응증·용법은 확인하지 못함.",
 "[18] EMA 페이지는 열리지 않아 WebSearch 요약으로만 확인 — 원문 미확인 출처 삭제, EMA 단행본 존재는 [7] 본문 서술로만 남김")
rep('history',"그리스 연구진은 이 풀을 백리향·그리스 세이지 정유와 섞어 감기 증상용 혼합물로 만들고 임상 시험까지 진행했다[4, 16].",
 "그리스 연구진은 이 풀의 정유를 타임(Thymbra capitata)·그리스 세이지(Salvia fruticosa) 정유와 섞어 상기도 감염 증상용 혼합 정유로 만들고 사람 대상 시험까지 진행했는데, 이는 세 식물 혼합물 자료다[4, 16].",
 "[4] 전문: 혼합 정유(CAPeo) — 이 종 단독 자료가 아님을 명시, 혼합 상대 학명 보충")
rep('biology',"절벽·바위틈·협곡·돌담처럼 그늘지거나 반그늘진 곳에 붙어 자란다[6, 7].",
 "절벽·바위·협곡·돌담처럼 그늘지거나 반그늘진 곳에 붙어 자란다[5, 6, 7].",
 "'그늘·반그늘' 서술은 [5] 본문에 있음 — 출처 보충")
rep('cultivation',"양액 농도와 인 함량을 달리한 수경재배(NFT)에서도 카르바크롤이 정유의 주성분으로 유지되었다[14, 29].",
 "양액 전기전도도와 인 농도를 달리한 수경재배(NFT)에서도 카르바크롤과 p-시멘이 정유의 주성분으로 유지되었다[14, 28].",
 "[14][29→28] 초록: 주성분은 카르바크롤과 p-시멘; '농도'는 전기전도도(EC)")
rep('processing',"그리스에서는 이 정유를 백리향·그리스 세이지 정유와 섞은 혼합물(1 mL 에 정유 약 1.5%)을 1주일 복용하는 제품으로 개발했다[4]. 이 혼합물은 경증 코로나19 외래 환자 69명의 개념 증명 연구에서 증상 수를 대조군보다 더 빨리 줄였으나, 무작위 배정 시험이 아니어서 근거 수준은 낮다[16].",
 "그리스에서는 이 정유를 타임·그리스 세이지 정유와 섞은 혼합 정유 제품을 만들었고, 등록된 용법은 하루 1 mL(혼합 정유 약 1.5% 함유)를 1주일 쓰는 것이다[4]. 이 혼합물을 14일 동안 먹인 경증 코로나19 외래 환자 69명의 개념 증명 관찰 연구에서 증상 수가 대조군보다 더 빨리 줄었으나, 무작위 배정 시험이 아니고 세 식물 혼합물이어서 디터니오브크릿 단독 효과로 볼 수 없다[16].",
 "[4] 원문 'registered use one week (1 ml/day containing ~1.5% of essential oils mixture)'; [16] 초록 14일 투여·관찰 연구 — 혼합물임을 명시")
rep('genetics',"넓은잎형과 좁은잎형은 정유 조성에서 화학계통적으로 다른 무리를 이루었고, 넓은잎형은 티모퀴논 비율이 더 높았다[14].",
 "화학계량 분석에서 좁은잎형 정유는 서로 비슷한 무리를 이루었고 넓은잎형 정유는 두 하위 무리로 갈렸으며, 넓은잎형은 티모퀴논 비율이 더 높았다[14].",
 "[14] 초록: 좁은잎형은 표현형 유사, 넓은잎형은 두 하위 무리 — '두 형이 서로 다른 무리' 서술은 원문과 다름")
rep('genetics',"생명공학 쪽에서는 잎·잎자루·뿌리 조직에서 캘러스를 유도해 다시 식물체를 만드는 간접 기관형성 방법이 처음 보고되었다[7]. 뿌리 액체배양에서는",
 "생명공학 쪽에서는 잎·잎자루·뿌리 조직 모두에서 캘러스가 생겼고, 새싹 재생은 잎·잎자루 쪽 캘러스에서만 10–30% 수준으로 일어나는 간접 기관형성이 처음 보고되었다[7]. 캘러스에서 얻은 뿌리의 액체배양에서는",
 "[7] 전문: 뿌리 캘러스는 기관 재생 없음, 새싹 재생률 10–30%(잎·잎자루 20%) — 세 조직 모두에서 식물체 재생된 것처럼 읽히는 서술 수정")
rep('related_species',"시중 자료에서 'dittany' 나 'dictamnus' 라는 이름만 보고",
 "식품첨가물(B코드) 목록에는 '천연향료(Dittany of Crete)'와 별도로 '천연향료(Dittany(Fraxinella) roots)'가 있는데, 프락시넬라(fraxinella)는 백선속 식물을 가리키는 이름이어서 영명 'dittany' 만으로는 두 원료가 구별되지 않는다[1]. 시중 자료에서 'dittany' 나 'dictamnus' 라는 이름만 보고",
 "I1020 로컬 원자료의 B코드 'Dittany(Fraxinella) roots' 행 — 이명 혼동 사례 추가")
rep('safety',"약초 제품을 바른 뒤 접촉 과민 반응이 생긴 증례가 보고되었으므로 피부 사용 시 주의가 필요하다[15]. 유럽의약품청 단행본은 성인용 약초차로 기침에는 1주, 위장 증상에는 2주를 넘겨 쓰지 말라고 하며 평가 당시 보고된 부작용은 없었다고 검색 요약에 나오나, 원문은 확인하지 못함[18]. 도심 차도 근처에서 키운 잎·꽃에서는 납·니켈·망간이 기준을 넘었으므로",
 "디터니오브크릿이 든 약초 치료제로 접촉 감작이 생긴 증례 보고가 있으므로(초록 없음, 제목·색인어만 확인) 피부에 쓸 때 주의가 필요하다[15]. 유럽의약품청 단행본의 사용 기간·금기·이상반응 내용은 원문을 확인하지 못함. 아테네 도심의 옥상과 차도 옆에서 키운 잎·꽃에서는 두 곳 모두 납·니켈·망간이 기준을 넘었으므로",
 "[18] WebSearch 요약만으로 쓴 사용 기간·부작용 서술 삭제; [15] 초록 없어 '바른 뒤' 단정 완화; [5] 원문은 옥상·차도 옆 두 곳 모두 초과")
# renumber: remove 18, shift 19..30 -> 18..29 (cultivation edit above already used 28 for old 29; handle carefully)
# undo that pre-shift: set placeholder
for s in d['sections']:
    s['body']=s['body'].replace('[14, 28].','[14, @29@].')
def shift(text):
    def f(m):
        nums=[x.strip() for x in m.group(1).split(',')]
        out=[]
        for x in nums:
            if x.startswith('@'): out.append(str(int(x.strip('@'))-1)); continue
            n=int(x)
            if n==18: continue
            out.append(str(n-1 if n>18 else n))
        return '['+', '.join(out)+']' if out else ''
    return re.sub(r'\[([@\d][@\d, ]*)\]',f,text)
for s in d['sections']: s['body']=shift(s['body'])
def fixsrc(lst): return [ (n-1 if n>18 else n) for n in lst if n!=18]
for grp in ('compounds','assays'):
    for c in d[grp]:
        c['source']=fixsrc(c['source'])
        for k,v in list(c.items()):
            if isinstance(v,str): c[k]=shift(v)
# compound fixes
for c in d['compounds']:
    if c['name']=='12-Hydroxyjasmonic acid':
        old=c['activity_ko']; c['activity_ko']="원문은 지환족 유도체로 분리만 보고, 이 성분 자체의 생리 활성은 확인하지 못함[9]"
        changes.append({"where":"compounds[12-Hydroxyjasmonic acid].activity_ko","before":old,"after":c['activity_ko'],"why":"[9] 초록은 'alicyclic derivative' 로만 적음 — '식물 호르몬 대사물' 서술 근거 없음"})
for a in d['assays']:
    if a['compound']=='Carvacrol':
        old=a['part']; a['part']="건조 지상부(2023년 5월 이탈리아의 허가 공급처에서 구입, 야생 채취품 아님) 물 증류 정유"
        changes.append({"where":"assays[Carvacrol].part","before":old,"after":a['part'],"why":"[2] 원문은 'purchased ... rather than collected from the wild' 로 재배 여부를 명시하지 않음"})
src=[s for s in d['sources'] if s['n']!=18]
for s in src:
    if s['n']>18: s['n']-=1
src[0]['title']=src[0]['title'].replace("백선·백선피(Dictamnus dasycarpus, 사용불가) 행 대조","백선·백선피(Dictamnus dasycarpus, 사용불가), 식품첨가물(B코드) 천연향료(Dittany of Crete)·천연향료(Dittany(Fraxinella) roots) 행 대조")
d['sources']=src
json.dump(d,open(P,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('/home/user/hfoodguide-wave3/docs/materials/origanum-dictamnus/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
