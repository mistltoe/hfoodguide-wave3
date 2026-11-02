import json,re
p='/home/user/hfoodguide-wave3/docs/materials/pinus-thunbergii/dossier.json'
d=json.load(open(p))
S={s['key']:s for s in d['sections']}
changes=[]
def rep(key,old,new,why):
    b=S[key]['body']; assert old in b,(key,old); S[key]['body']=b.replace(old,new); changes.append({"where":f"sections.{key}","before":old,"after":new,"why":why})
rep('overview',"곰솔은 일본과 한국 해안에 자생하며 국제자연보전연맹 적색목록에서 관심대상(LC)으로 평가되었다고 정리된다(원문 미열람)[24].",
 "곰솔은 한국·중국·일본 등 동아시아 해안에 자라는 침엽수로 소개된다[11].",
 "[24] POWO 는 원문을 열지 못하고 WebSearch 요약에만 기댄 출처라 IUCN 평가를 확인할 수 없음 — 분포는 [11] 초록 문장으로 대체")
rep('overview',"잎 에탄올 추출물은 대식세포와 생쥐 귀 부종 실험에서 항염 작용을 보였고, 추출물은 인플루엔자 A 바이러스 세포 실험에서 감염 세포의 생존율을 높였다[4, 9].",
 "잎 에탄올 추출물은 대식세포 실험과 생쥐 귀에 바르는 부종 실험에서 항염 작용을 보였고[4], 부위가 초록에 적히지 않은 곰솔 추출물은 인플루엔자 A 바이러스 세포 실험에서 감염 세포의 생존율을 높였으나 함께 시험한 측백나무 추출물보다 약했다[9]. 이들은 세포·동물 결과로, 사람에게서 같은 효과를 뜻하지 않는다[4, 9].",
 "[4] 동물실험은 국소 도포(1.0 mg/ear); [9] 은 추출 부위를 밝히지 않았고 Thuja orientalis 가 더 강했다 — 세포·동물 결과 과장 방지")
rep('history',"국내 연구진은 소나무(적송)와 곰솔(흑송)을 한국에서 가장 흔한 두 소나무로 소개하고",
 "국내 연구진은 소나무(red pine)와 곰솔(black pine, 논문 표기 'Haesong pine')을 한국에서 가장 흔한 두 소나무로 소개하고",
 "[3] 원문은 red pine/black pine·Haesong pine 으로 적었고 '흑송'이라는 국문명은 없음")
rep('history',"화석 잎 표피 연구는 곰솔이 일본의 마이오세 화석종 Pinus mikii와 가깝고,",
 "화석 잎 표피 연구는 곰솔이 일본의 마이오세 화석종 Pinus mikii와 일부 표피 형질을 공유하며,",
 "[23] 은 P. mikii 가 류큐소나무(P. luchuensis)와 가깝고 곰솔과는 일부 표피 형질을 공유한다고 씀")
rep('biology',"곰솔은 일본·한국 원산으로 정리되며, 해안의 구릉과 산지에서 해발 약 1,000 m까지 자란다고 설명된다(WebSearch 요약)[24].",
 "곰솔은 동아시아 해안에 자라는 침엽수이며, 일본에서는 준고유종으로 기술된다[11, 23]. 자생 고도 범위를 1차 출처로는 확인하지 못함.",
 "[24] WebSearch 요약만으로는 확인 불가 — 해발 1,000 m 삭제, [11]·[23] 초록으로 대체")
rep('related_species',"예컨대 소나무 항목은 순·줄기·나무껍질·가지·잎·꽃가루를 허용하지만, 곰솔 항목은 잎만 허용한다[1].",
 "예컨대 소나무 항목은 순·줄기·나무껍질·가지·잎·꽃가루를 허용하고 뿌리·솔방울은 제한적으로 허용하지만(솔방울은 일반증류주 원료에 한함), 곰솔 항목은 잎만 허용한다[1].",
 "I1020 원자료 대조: 소나무 뿌리·솔방울 제한적사용 행 보완")
rep('processing',"이 연구는 네 종의 정유에서 휘발 성분 74종을 확인하고",
 "이 연구는 개잎갈나무(Cedrus deodara)를 포함한 네 종의 정유에서 휘발 성분 74종을 확인하고",
 "[7] 의 네 종 가운데 하나는 소나무속이 아닌 Cedrus deodara")
rep('processing',"식약처 「식품 등의 생산실적」에는 개별인정형 원료 '솔잎증류농축액'이 집계되지만, 식품원료 목록에서 증류농축액은 소나무(Pinus densiflora) 항목('소나무잎증류농축액')으로 올라 있어 곰솔 제품으로 볼 근거가 없다[1, 25].",
 "식약처 「식품 등의 생산실적」에는 개별인정형 원료 '솔잎증류농축액'이 집계되지만, 식품원료 목록의 해당 건강기능식품 항목(기능성원료인정 제2007-8호)에는 학명이 적혀 있지 않고 일반 식품원료의 증류농축액은 소나무(Pinus densiflora) 항목('소나무잎증류농축액')으로 올라 있어 곰솔 제품으로 볼 근거가 없다[1, 25].",
 "I1020 원자료 대조: C코드 '솔잎증류농축액(기능성원료인정제2007-8호)' 행은 SCNM 공란")
rep('genetics',"곰솔·마미송·유송의 잎은 DNA 바코드 서열의 종간·종내 거리가 뚜렷이 갈려 분자 감별이 가능했다[12].",
 "곰솔·마미송·유송의 잎은 두 DNA 바코드 가운데 한 서열에서 종간·종내 거리가 뚜렷이 갈려 분자 감별이 가능했고, 다른 한 서열에서는 바코딩 간격이 뚜렷하지 않았다[12].",
 "[12] 초록: 한 서열은 barcoding gap 없음, 다른 한 서열만 분리")
rep('safety',"세포 생존율에 유의한 차이를 보이지 않았다[4].",
 "세포 생존율에 유의한 차이를 보이지 않았으나, 논문은 24시간을 넘겨 처리하면 세포독성이 나타난다고도 적었다[4]. 이는 세포 실험 결과로 사람의 섭취 안전성을 보여 주지 않는다[4].",
 "[4] 전문 3.1절: 'PTP only causes cytotoxicity when administered for over 24 h' 누락")
rep('safety',"미국 폰데로사소나무(Pinus ponderosa) 잎을 먹은 임신 말기 소에서 유산이 일어났고, 원인 물질로 라브단계 디테르펜산인 이소쿠프레스산과 혈관수축성 지질이 지목되었다[21, 27].",
 "미국 폰데로사소나무(Pinus ponderosa) 잎을 먹은 임신 말기 소에서는 자궁 혈류 감소와 조산이 나타났고, 이 잎의 혈관수축성 지질은 임신 기니피그에서 유산 작용을 보였으나 같은 실험에서 이소쿠프레스산을 넣은 사료는 그러지 않았다[21]. 소 실험에서는 라브단계 디테르펜산인 이소쿠프레스산이 주된 유산 물질로 제시되었고, 다른 식물(대만향나무 뿌리)에서 얻은 이소쿠프레스산은 소 황체세포의 프로게스테론 생성을 억제했다(세포 실험)[27].",
 "[21] 은 기니피그 실험에서 혈관수축성 지질만 유산 작용, 이소쿠프레스산 사료(Diet G)는 효과 없음; [27] 의 IA 는 Juniperus formosana 뿌리 유래·세포 실험")
rep('safety',"이 결과는 소에 대한 다른 종의 자료이며, 곰솔 잎에 이소쿠프레스산이 들어 있는지와 그 함량은 확인하지 못함.",
 "이 결과는 소·기니피그에 대한 다른 종의 자료이며, 곰솔 잎에 이소쿠프레스산이 들어 있는지와 그 함량을 보고한 논문은 PubMed 검색에서 찾지 못함.",
 "PubMed 검색(isocupressic acid/abortifacient × thunbergii/black pine) 0건 — 확인 범위 명시")
d['sections']=list(S.values())
# aliases
d['aliases']=[a for a in d['aliases'] if a!='흑송']
changes.append({"where":"aliases","before":"흑송","after":"(삭제)","why":"I1020 곰솔잎 별명은 가지해송·해송·왕솔뿐이고 '흑송'은 흑반송 별명 '만주흑송'에만 있음; [3] 원문에도 없음"})
# compound alpha-pinene
for c in d['compounds']:
    if c['name']=='alpha-Pinene':
        o=c['activity_ko']; c['activity_ko']=o.replace("네 종 솔잎 정유","개잎갈나무를 포함한 네 종 침엽 정유")
        changes.append({"where":"compounds[alpha-Pinene].activity_ko","before":o,"after":c['activity_ko'],"why":"[7] 의 네 종에 Cedrus deodara 포함"})
    if c['name']=='Isoquercitrin':
        o=c['content_text']; c['content_text']=o.replace("소나무 잎 봄 채취 18.35 mg/100 g","(참고: 다른 종인 소나무 잎 봄 채취 18.35 mg/100 g 건조중량)")
        changes.append({"where":"compounds[Isoquercitrin].content_text","before":o,"after":c['content_text'],"why":"소나무(P. densiflora) 수치임을 명시·기준(건조중량) 보완"})
# drop source 24 and renumber
used=set()
def refs(t):
    for m in re.finditer(r'\[([\d,\s]+)\]',t):
        for x in m.group(1).split(','): used.add(int(x))
for s in d['sections']: refs(s['body'])
for c in d['compounds']+d['assays']:
    for x in c.get('source',[]): used.add(x)
    for k in ('content_text','activity_ko','content'):
        if k in c: refs(c[k])
old=[s for s in d['sources'] if s['n'] in used]
mp={s['n']:i+1 for i,s in enumerate(old)}
print('dropped',[s['n'] for s in d['sources'] if s['n'] not in used], mp)
def sub(t):
    return re.sub(r'\[([\d,\s]+)\]',lambda m:'['+', '.join(str(mp[int(x)]) for x in m.group(1).split(','))+']',t)
for s in d['sections']: s['body']=sub(s['body'])
for c in d['compounds']+d['assays']:
    if 'source' in c: c['source']=[mp[x] for x in c['source']]
    for k in ('content_text','activity_ko','content'):
        if k in c and isinstance(c[k],str): c[k]=sub(c[k])
for s in old: s['n']=mp[s['n']]
d['sources']=old
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('/home/user/hfoodguide-wave3/docs/materials/pinus-thunbergii/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
