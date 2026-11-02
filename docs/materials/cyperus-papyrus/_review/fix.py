import json,re,sys
p='/home/user/hfoodguide-wave3/docs/materials/cyperus-papyrus/dossier.json'
d=json.load(open(p))
changes=[]
def rep(where,obj,key,old,new,why):
    s=obj[key]
    assert s.count(old)==1,(where,old)
    obj[key]=s.replace(old,new); changes.append({"where":where,"before":old,"after":new,"why":why})
S={s['key']:s for s in d['sections']}
W22="출처 [22](Feedipedia)는 원문을 열지 못했고(호스트 접근 불가) WebSearch 요약뿐이라 근거가 될 수 없음; 다른 1차 출처도 열어 확인하지 못함"
rep('sections.overview',S['overview'],'body',"속대를 날로 또는 익혀 먹거나 씹는다는 서술은 WebSearch 요약으로만 확인했다[22]. ","사람이 속대를 날로 또는 익혀 먹는다는 서술은 원문을 열어 확인하지 못함. ",W22)
rep('sections.history',S['history'],'body',"아프리카에서는 줄기를 울타리·지붕·돗자리·섬유판·연탄 재료로 써 왔다[2].","파피루스 줄기는 전통적으로 울타리·지붕·돗자리 재료로 쓰였고, 섬유판·연탄 재료로도 쓰인다[2].","[2]는 지역을 '아프리카'로 한정하지 않았고 섬유판·연탄은 전통 용도와 따로 적음")
rep('sections.history',S['history'],'body',"사람이 속대를 음식으로 먹는다는 서술은 WebSearch 요약으로만 확인했고(원문 미확인), 고대","사람이 속대를 음식으로 먹는다는 서술은 원문을 열어 확인하지 못했고, 고대",W22)
rep('sections.processing',S['processing'],'body',"속대를 날로·익혀 먹거나 씹는다는 서술은 WebSearch 요약으로만 확인했다[22]. ","속대를 날로·익혀 먹는다는 서술은 원문을 열어 확인하지 못함. ",W22)
rep('sections.genetics',S['genetics'],'body',"이 양상은 홀로세 기후 변화와 새를 통한 씨앗 확산으로 설명되었다[5].","상류·하류의 다양성 차이는 홀로세의 과거 집단 변동으로, 집단 사이의 높은 혼합은 산발적 홍수에 따른 유역 연결과 새를 통한 씨앗 확산으로 설명되었다[5].","[5] 초록: 새를 통한 씨앗 확산은 다양성 양상이 아니라 집단 간 혼합·유전자 흐름의 설명임")
rep('sections.related_species',S['related_species'],'body',"특히 기름골 덩이줄기(타이거너트, chufa)의 지방·전분 자료를 파피루스에 옮겨 쓰면 안 된다[1].","특히 기름골 덩이줄기(목록 영문명 Chufa)의 성분 자료를 파피루스속대에 옮겨 쓰면 안 된다.","[1]은 지방·전분을 말하지 않고, 별명 '타이거너트'는 출처 없음; 편집 주의 문장으로 바꿈")
rep('sections.related_species',S['related_species'],'body',"에티오피아 습지에서는 C. fastigiatus, C. dives 같은 다른 큰 사초가 파피루스와 함께 자란다[23].","에티오피아 조사에서 사탕수수 줄기 해충은 파피루스 말고도 C. fastigiatus, C. dives 같은 다른 토착 습지 사초에서도 발견되어, 큰 사초류끼리 시료가 섞이지 않게 주의해야 한다[22].","[23→22] 초록은 세 사초가 해충의 기주라는 것이지 함께 자란다는 말은 아님")
rep('sections.cultivation',S['cultivation'],'body',"이집트 샤르키아주 카라무스에서는 농가가 노지에서 길러 1년 내내 수확할 수 있다[2, 3].","연구 시료는 이집트 샤르키아주 카라무스 농가에서 구했고 노지에서 길렀으며, 수확은 1년 내내 할 수 있다고 한다[2, 3].","[3]은 농가에서 구입, [2]는 노지 재배·연중 수확 — 출처별 내용을 맞춤")
rep('sections.cultivation',S['cultivation'],'body',"[23]. 국내","[22]. 국내","번호 정리")
rep('sections.safety',S['safety'],'body',"이집트 인공습지 시험에서는 구리 72%, 아연 84%를 제거했다[24]. 수생식물 7종 화분 시험에서 파피루스 조직에도 브롬화 난연제(PBDE)가 쌓였다[18]. 이런 결과는 오염된 물에서 자란 파피루스가 오염물질을 몸에 담을 수 있음을 보여 주므로, 식품으로 쓸 때는 자란 곳의 수질을 따져야 한다[15, 18, 24]. 속대 지질에는 7-옥소스테롤 같은 산화 스테롤이 소량(건물 1 kg당 수십 mg) 들어 있다[2]. 파피루스 습지는 우기에 메테인을 많이 내놓는 곳이어서, 채취는 습지 보전과 함께 고려해야 한다[9, 21].",
    "부들(Typha latifolia)과 파피루스 인공습지를 비교한 이집트 시험에서는 최적 조건(72시간, 초기 농도 15 mg/L)에서 구리 72%, 아연 84%가 제거되었으나, 초록만으로는 어느 식물 습지의 값인지 분명하지 않다[23]. 데카브로모다이페닐에테르(BDE-209)를 넣은 수생식물 7종 화분 시험에서 파피루스 조직에도 브롬화 난연제(PBDE)가 쌓였다[18]. 오염물질이 식물 조직에 쌓인다는 직접 근거는 이 화분 시험이며, 오염된 물에서 자란 파피루스 속대의 오염물질 함량 자료는 확인하지 못함; 식품으로 쓸 때는 자란 곳의 수질을 따지는 것이 안전하다(편집 의견). 속대 지질에는 7-옥소캄페스테롤·7-옥소스티그마스테롤·7-옥소시토스테롤 같은 산화 스테롤이 각각 건물 1 kg당 30–80 mg 들어 있다[2]. 우간다 동부의 파피루스 습지는 우기에 대기 메테인의 강한 배출원이었고[21], 습지를 말려 농지로 바꾸기보다 낮은 강도로 여러 용도로 쓰는 편이 가치가 크다는 검토가 있다[9].",
    "[24→23] 초록에서 Cu·Zn 제거율이 어느 습지 값인지 불분명; [15]는 질소·인 흡수일 뿐 오염물질 축적이 아니고 '수질을 따져야 한다'는 출처에 없는 결론; 7-옥소스테롤 값은 표 1 속대 30·40·80 mg/kg; '채취는 보전과 함께'는 [9,21]에 없는 결론")
for c in d['compounds']:
    if c['name']=='Lignin':
        old=c['activity_ko']; c['activity_ko']="세포벽 구조 성분; 기존 문헌값(TGA 25–40%대, Py-GC/MS 46.9%)은 과대평가였음[3]"
        changes.append({"where":"compounds.Lignin.activity_ko","before":old,"after":c['activity_ko'],"why":"[3]: 47%는 TGA가 아니라 Py-GC/MS 값(46.9%), TGA 문헌값은 25–40%"})
for a in d['assays']:
    if a['compound']=='beta-Sitosterol':
        old=a['rationale']; a['rationale']=old.replace("스테롤류가 속대 지질의 44.4%를 차지해","스테로이드 화합물이 속대에서 확인된 지질 성분의 44.4%(8600 mg/kg)를 차지해"); assert old!=a['rationale']
        changes.append({"where":"assays[beta-Sitosterol].rationale","before":"스테롤류가 속대 지질의 44.4%","after":"스테로이드 화합물이 확인된 성분의 44.4%","why":"[2]: 44.4%는 확인된 성분 중 스테로이드 화합물(유리 스테롤뿐 아님) 비율"})
        old=a['conditions']['sample_prep']; a['conditions']['sample_prep']=old.replace("속대와 겉껍질을 칼로 분리","공기 건조한 두 개체 줄기의 속대와 겉껍질을 커터로 분리해 섞고"); assert old!=a['conditions']['sample_prep']
    if a['compound']=='Lignin':
        old=a['rationale']; a['rationale']=old.replace("기존 TGA법이 25–47%로 과대평가했음을","기존 문헌값(25–47%, TGA·Py-GC/MS)이 과대평가였음을"); assert old!=a['rationale']
        changes.append({"where":"assays[Lignin].rationale","before":"기존 TGA법이 25–47%로 과대평가","after":"기존 문헌값(25–47%, TGA·Py-GC/MS)이 과대평가","why":"47%는 Py-GC/MS 값"})
# sources: drop 22, renumber
src=[s for s in d['sources'] if s['n']!=22]
for s in src:
    if s['n']>22: s['n']-=1
d['sources']=src
for s in d['sources']:
    if s['n']==23: s['title']=s['title'].replace("초록 확인)","초록 확인; Cu·Zn 제거율이 어느 습지 값인지 초록에서 불분명)")
d['sources'][[s['n'] for s in d['sources']].index(1)]['accessed']="2026-10-13"
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('/home/user/hfoodguide-wave3/docs/materials/cyperus-papyrus/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
