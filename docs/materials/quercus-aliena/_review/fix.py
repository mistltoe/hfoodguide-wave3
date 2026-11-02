import json,re
p='dossier.json'; d=json.load(open(p))
changes=[]
def sec(k): return next(s for s in d['sections'] if s['key']==k)
def rep(where,obj,key,old,new,why):
    assert old in obj[key], (where,old)
    obj[key]=obj[key].replace(old,new); changes.append({"where":where,"before":old,"after":new,"why":why})
MAP="종 대응: PubMed 도구 전문에서는 학명이 빠져 있어, 이 수치를 갈참나무(Q. aliena)에 대응시킨 근거는 PMC 본문 문장('In the free polyphenol extract of Q. aliena acorn kernels…')을 인용한 WebSearch 요약뿐이다(원문 직접 확인 못함, 근거 수준 낮음)[7]"
OLDMAP="종 대응 주의: PubMed 도구 출력에서 학명이 빠져 있어 본문에서 제목 순서(굴참나무·갈참나무·떡갈나무)의 둘째 종 문단을 갈참나무로 대응시켰다[7]"
# processing
s=sec('processing')
rep('sections.processing',s,'body','논문은 갈참나무를 포함한 세 종 도토리가 엘라그산·갈산 원료로 쓰일 수 있다고 보았다[7].',
 '논문 초록은 굴참나무와 갈참나무 도토리를 엘라그산 추출 원료로 적합하다고 보았다(종 이름은 PubMed 도구 출력에서 빠져 WebSearch 요약으로 확인)[7]. 시료는 중국 베이징 주펑산에서 채취한 도토리였다[7].',
 '초록은 두 종(굴참나무·갈참나무)을 엘라그산 원료로, 다른 한 종을 갈산 연구 원료로 구분함 — 세 종 모두 두 성분 원료라는 서술은 과장')
rep('sections.processing',s,'body','갈참나무 도토리 물 추출물은 다른 추출물보다 슈퍼옥사이드 라디칼 소거 활성이 높았다(IC50 4.92 μg/mL)[6].',
 '갈참나무 도토리 물 추출물은 다른 추출물보다 슈퍼옥사이드 라디칼 소거 활성이 높았고, 도토리 추출물의 소거 활성 IC50은 4.92 μg/mL였다(ESR 측정)[6].',
 '초록은 IC50 을 물 추출물로 특정하지 않고 Quercus aliena acorn extracts 로 적음')
rep('sections.processing',s,'body','이 추출물을 미리 먹인 쥐에서는','추출물을 미리 먹인 흰쥐(랫드)에서는','초록: rats')
# biology
s=sec('biology')
rep('sections.biology',s,'body','백참나무류 도토리의 배를 4 mm 잘라 내는 실험에서','다람쥐의 배 제거 행동을 흉내 내 백참나무류 도토리 끝의 떡잎 4 mm를 잘라 내는 실험에서',
 '[12] 초록: removing 4 mm of cotyledon from the apical end')
rep('sections.biology',s,'body','설치류는 벌레 먹은 도토리보다 성한 갈참나무 도토리를 더 많이 저장하고 먹었다[13].',
 '설치류는 야외와 반자연 사육장에서 벌레 먹은 도토리보다 성한 갈참나무 도토리를 더 많이 저장하고 먹었지만, 좁은 개별 우리에서는 벌레 먹은 도토리를 더 먹었다[13].',
 '[13] 초록: 개별 우리에서는 반대 결과')
# related_species
s=sec('related_species')
rep('sections.related_species',s,'body','굴참나무는 갈참나무와 서식지가 비슷하지만 다른 절의 종으로, 도토리 녹말·총페놀의 발달 양상이 다르다[9].',
 '굴참나무는 갈참나무와 서식지가 비슷하지만, 도토리 녹말·총페놀의 발달 양상이 다르다[9].',
 "[9] 초록에 '다른 절' 언급 없음")
rep('sections.related_species',s,'body','굴참나무·갈참나무·떡갈나무 세 종은 깍정이의 가수분해형 탄닌 함량이 서로 다르다[10].',
 '굴참나무·갈참나무·떡갈나무 세 종은 가수분해형 탄닌 함량이 서로 다르며, 세 종의 깍정이에서 β-글루코갈린이 그 생산 지표로 확인되었다[10].',
 "[10] 초록은 HT 함량 차이를 부위 특정 없이 말하고, 깍정이는 β-글루코갈린 지표에 관한 것")
# safety
s=sec('safety')
rep('sections.safety',s,'body','쥐 실험에서 간 보호 작용을 보였고 독성은 보고되지 않았으나, 사람 대상 안전성 시험은 확인하지 못함[6].',
 '흰쥐 실험에서 간 보호 작용을 보였으나 초록에 독성 평가 결과는 없고, 사람 대상 안전성 시험은 확인하지 못함[6].',
 "[6] 초록에 독성 평가 없음 — '독성 보고 없음'은 근거 없는 함의")
# compounds
for c in d['compounds']:
    for k in ('content_text',):
        if OLDMAP in c[k]:
            c[k]=c[k].replace(OLDMAP,MAP); changes.append({"where":f"compounds.{c['name']}.content_text","before":OLDMAP,"after":MAP,"why":"둘째 종=갈참나무 대응을 제목 순서 추정에서 WebSearch 인용 근거로 바꾸고 근거 수준을 낮게 표시"})
    if c['name'] in ('Ferulic acid','Quercetin','Azelaic acid'):
        c['content_text']=c['content_text'].replace('[7]','; 종 대응 근거 수준 낮음(WebSearch 요약)[7]',1)
    if c['name']=='Ellagic acid':
        old=c['content_text']
        c['content_text']=old.replace('결합 폴리페놀 문단에서 엘라그산이 갈산의 7.42배, 페룰산의 47.52배(본문은 이 문단을 free polyphenol extract로 표기)',
          "본문은 '유리 폴리페놀 추출물'로 표기했으나 '결합 갈산'과 비교해 결합 폴리페놀 결과일 수 있는 문단에서 엘라그산이 갈산의 7.42배, 페룰산의 47.52배(건조 알맹이 추출물 안의 비율)")
        changes.append({"where":"compounds.Ellagic acid.content_text","before":"결합 폴리페놀 문단에서…","after":"본문 표기(유리)와 문맥(결합)이 엇갈림을 명시","why":"원문은 free polyphenol extract 로 적음"})
    if c['name']=='Tannins':
        c['part']='깍정이(각두)'
        c['content_text']='갈참나무 도토리 탄닌 함량 수치는 확인하지 못함; 굴참나무·갈참나무·떡갈나무는 가수분해형 탄닌 함량이 서로 다르고 깍정이에서 β-글루코갈린이 그 지표[10]'
        c['activity_ko']='굴참나무 도토리·깍정이의 높은 총페놀이 해충 방어에 관여할 것으로 해석(갈참나무 탄닌 자체의 작용은 확인하지 못함)[9][10]'
        changes.append({"where":"compounds.Tannins","before":"part 깍정이·열매, 종자 방어 물질","after":"part 깍정이, 방어 해석은 굴참나무 총페놀 대상","why":"[9]는 총페놀(탄닌 아님)·굴참나무 해석, [10]은 깍정이; 열매 탄닌은 이 종 근거 없음"})
# assays
for a in d['assays']:
    a['rationale']=a['rationale'].replace(OLDMAP,MAP)
    if a['compound']=='Ellagic acid':
        a['content']="본문 표기는 '유리 폴리페놀 추출물'이나 '결합 갈산'과 비교한 문단에서 갈산의 7.42배, 페룰산의 47.52배(절대 함량은 확인하지 못함)[7]"
        a['rationale']=a['rationale'].replace('알칼리 가수분해로 얻은 결합 폴리페놀의 주성분으로, 엘라기탄닌에서 풀려나는 산물이라 도토리 탄닌 계열의 지표가 될 수 있다[7].',
          '엘라기탄닌에서 풀려나는 산물이라 도토리 탄닌 계열의 지표가 될 수 있다(갈참나무 문단은 유리/결합 표기가 엇갈림)[7].')
        a['source']=[7]
        changes.append({"where":"assays.Ellagic acid","before":"source [7,8], '결합 폴리페놀의 주성분'","after":"source [7], 표기 엇갈림 명시","why":"[8] 정정 공고는 내용(초록 '[...]')을 확인할 수 없고 분석 근거가 아님"})
    a['conditions']['sample_prep']=a['conditions']['sample_prep'].replace('도토리 알맹이 45 °C','신선 도토리 세척 → 45 °C').replace('48 h 건조·분쇄','48 h 건조 → 껍질 분리 → 알맹이 분쇄')
# drop source 8, renumber
d['sources']=[s for s in d['sources'] if s['n']!=8]
m={o:(o if o<8 else o-1) for o in range(1,22)}
for s in d['sources']: s['n']=m[s['n']]
d['sources'][6]['title']=d['sources'][6]['title'].replace('종 이름은 WebSearch 결과의 논문 제목으로 확인','종 이름과 갈참나무 문단 대응은 PMC 본문을 인용한 WebSearch 요약으로만 확인')
def rn(t): return re.sub(r'\[(\d+)\]',lambda x:'['+str(m[int(x.group(1))])+']',t)
for s in d['sections']: s['body']=rn(s['body'])
for c in d['compounds']:
    for k in ('content_text','activity_ko'): c[k]=rn(c[k])
    c['source']=[m[x] for x in c['source']]
for a in d['assays']:
    for k in ('content','rationale'): a[k]=rn(a[k])
    a['source']=[m[x] for x in a['source']]
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
