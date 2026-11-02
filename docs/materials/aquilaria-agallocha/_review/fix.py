import json,re,sys
p=sys.argv[1]
d=json.load(open(p))
S={s['key']:s for s in d['sections']}
def rep(key,old,new):
    b=S[key]['body']; assert old in b,(key,old); S[key]['body']=b.replace(old,new)
# history
rep('history','중국 약재 이름은 침향(Aquilariae Lignum Resinatum)으로, 구토·위통·위장 기능 장애에 널리 쓰였다고 기술된다[20, 21].',
 '중국 약재 이름은 침향(Aquilariae Lignum Resinatum)으로, 구토·위통·위장 기능 장애에 널리 쓰였다고 기술된다[20, 21]. 다만 이 중국 연구들은 기원을 A. agallocha로 적으면서 부위를 \'마른 뿌리줄기\'로 적는 등 기원 기재가 엄밀하지 않다[20].')
rep('history',' 튀르키예의 메시르 페이스트(Mesir paste)는 오스만 시대부터 약 500년 동안 만들어 온 약용 반죽으로, A. agallocha가 그 재료 가운데 하나라고 한다[32].','')
# biology
rep('biology','자연 형성의 계기가 된다[9, 10]. 같은 나무라도 수지가 없는 줄기와 수지가 쌓인 부위의 정유 성분은 뚜렷이 다르다[10].',
 '자연 형성의 계기가 된다[9]. 인위 유도 침향은 자연 침향과 향이 다르다고 하며, 말레이시아에서는 건강한 줄기·자연 침향·인위 침향의 정유 성분 자료가 공개되었다[10].')
rep('biology','포볼 에스터(phorbol ester)가 들어 있다[26, 27]. 잎에서는 지금까지 185개 성분이 기록되었으나 이는 수지 목재와 다른 부위의 자료다[28].',
 '포볼 에스터(phorbol ester)가 들어 있다[26]. Aquilaria속 잎(주로 A. sinensis·A. crassna·A. malaccensis)에서 185개 성분이 기록되었으나 수지 목재가 아닌 잎 자료다[28].')
rep('biology','생존율을 82.14%로 유지했다(세포 실험)[17]','생존율이 82.14%였다(세포 실험)[17]')
# related_species
rep('related_species','반면 엽록체 유전체 비교 연구에는 \'A. agallocha\'라는 이름의 서열이 따로 쓰였다[24]. 국제 분류 데이터베이스의 현재 정명 처리는 확인하지 못함.',
 '세계식물목록(WFO)·EPPO 등 식물명 데이터베이스도 A. agallocha Roxb.를 A. malaccensis의 이명으로 처리한다고 검색 요약에서 확인했으나 원 페이지는 직접 열지 못했다[37]. 반면 엽록체 유전체 비교 연구에는 \'A. agallocha\'라는 이름의 서열이 따로 쓰였다[24].')
rep('related_species','중국에서 주로 쓰는 백목향(A. sinensis)은 다른 종이며, 식약처 목록에서 A. sinensis를 포함한 Aquilaria속의 다른 종 행은 찾지 못했으므로, 이 자료는 A. sinensis 연구값을 쓰지 않았다[1].',
 '중국 약용 침향의 법정 기원은 A. sinensis와 A. agallocha 두 종이라고 소개된다[5]. 백목향(A. sinensis)은 다른 종이고 식약처 목록에 Aquilaria속 다른 종 행은 없으므로, 이 자료는 A. sinensis 연구값을 쓰지 않았다[1].')
# cultivation
rep('cultivation','부속서 II 등재는 침향 원목·조각·오일의 국제 거래를 통제하기 위한 것이다[7, 8].',
 '높은 국제 거래와 야생 채취가 등재 이유로 꼽히며, 거래되는 주요 파생물은 목재 조각과 오일이다[7].')
# safety
rep('safety','장기 안전성 자료는 부족하다[1, 28]. 잎 추출물이 쥐의 간 손상을 줄였다는 연구도 잎 자료여서 수지 목재 결과로 볼 수 없다[29].',
 '장기 안전성 자료는 부족하다[1, 28]. 이 잎 자료는 주로 A. sinensis 등 여러 종을 묶은 속 수준 리뷰여서 수지 목재 결과로 볼 수 없다[28].')
rep('safety','소장 이동률(42.82%, 대조 85.53%)이 낮아졌다[20].','소장 이동률(42.82%, 대조 85.53%)이 낮아졌다(장 운동 억제, 동물 실험)[20].')
# compounds: relative composition
for c in d['compounds']:
    t=c['content_text']
    t=t.replace('A. agallocha 침향 오일 12.5%[12]','A. agallocha 침향 오일 내 상대 조성 12.5%[12]')
    t=t.replace('A. agallocha 침향 오일 11.8%[12]','A. agallocha 침향 오일 내 상대 조성 11.8%[12]')
    t=t.replace('A. agallocha 침향 오일 8.9%[12]','A. agallocha 침향 오일 내 상대 조성 8.9%[12]')
    t=t.replace('물증류 정유 6.5%[11]','물증류 정유 내 상대 조성 6.5%[11]')
    t=t.replace('정유 32.1%(최대 성분)[11]','정유 내 상대 조성 32.1%(최대 성분)[11]')
    t=t.replace('정유 5.8%, 시판 침향 오일 10.3%[11]','정유 내 상대 조성 5.8%, 시판 침향 오일 10.3%[11]')
    t=t.replace('목재 추출물 GC-MS 피크 비율 0.03~3.77%','목재 추출물 GC-MS 상대 피크 비율 0.03~3.77%(표준품 정량 아님)')
    c['content_text']=t
    if c['name']=='Octahydrocurcumin':
        c['activity_ko']='HEK293 타우-BiFC 세포 모델에서 20 μM에 타우 올리고머화를 43.7% 줄이고 같은 농도에서 세포독성 없음(세포 실험)[3]'
a=d['assays']
a[0]['part']='인위 접종 3개월 뒤 접종 구멍 주변 목재 가루(4~5년생 A. malaccensis, 인도 아삼; 침향 형성 초기)'
a[0]['content']='아가로스피롤 상대 피크 비율 0.03~3.77%(접종 균주별), 접종하지 않은 목재 0.00%[9]'
a[0]['conditions']['mobile_phase']='헬륨(순도 >99.999%), 일정 유량'
a[3]['content']='정유 내 상대 조성(%): 4-페닐-2-부탄온 32.1%, 진코-에레몰 6.5%, α-구아이엔 5.8%; 시판 오일은 α-구아이엔 10.3%, 카리오필렌 옥사이드 8.6%, 유데스몰 3.2%[11]'
a[2]['content']='지표 띠 상대 비율: 상급 오일 >50%, 하급 오일 <20%[14]'
# sources
d['sources'].append({'n':37,'title':'World Flora Online(WFO Plant List) Aquilaria malaccensis Lam. 항목 및 EPPO Global Database AQAAG 항목 — A. agallocha Roxb.를 A. malaccensis의 이명으로 처리(WebSearch 요약으로만 확인, 원 페이지 미열람)','url':'https://wfoplantlist.org/taxon/wfo-0001142510-2025-06','publisher':'World Flora Online / EPPO','accessed':'2026-11-02'})
drop={27,29,32}
# renumber
used=set()
txt=json.dumps({k:v for k,v in d.items() if k!='sources'},ensure_ascii=False)
for m in re.finditer(r'\[([\d, ]+)\]',txt):
    used|={int(x) for x in m.group(1).split(',')}
for k in ('compounds','assays'):
    for c in d[k]: used|=set(c.get('source',[]))
assert not (used&drop), used&drop
keep=[s for s in d['sources'] if s['n'] in used]
mp={s['n']:i+1 for i,s in enumerate(keep)}
def rn(m): return '['+', '.join(str(mp[int(x)]) for x in m.group(1).split(','))+']'
for s in d['sections']: s['body']=re.sub(r'\[([\d, ]+)\]',rn,s['body'])
for k in ('compounds','assays'):
    for c in d[k]:
        for f in list(c):
            if isinstance(c[f],str): c[f]=re.sub(r'\[([\d, ]+)\]',rn,c[f])
        c['source']=[mp[x] for x in c['source']]
for s in keep: s['n']=mp[s['n']]
d['sources']=keep
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
print(len(keep),'sources'); print({s['key']:len(s['body']) for s in d['sections']})
