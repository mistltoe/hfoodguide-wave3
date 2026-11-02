import json,sys
p=sys.argv[1]
d=json.load(open(p))
S={s['key']:s for s in d['sections']}
def rep(key,old,new):
    b=S[key]['body']; assert old in b,(key,old); S[key]['body']=b.replace(old,new)
rep('overview',"닥나무속 세 종에서 지금까지 338개 화합물이 분리되었을 만큼 성분 연구는 많지만, 부위가 섞여 있다[11].",
    "닥나무속 세 종에서 지금까지 338개 화합물이 분리되었을 만큼 성분 연구는 많지만[11], 논문마다 쓴 부위가 다르다.")
rep('overview',"반면 카지놀류 등 많이 연구된 프레닐 폴리페놀은 주로 뿌리껍질에서 얻은 것이고[19, 20]",
    "반면 카지놀류 등 프레닐 폴리페놀을 분리한 국내 연구 두 건은 뿌리껍질을 썼고[19, 20]")
rep('history',"우량 계통을 꺾꽂이 등 영양번식으로","우량 계통을 영양번식으로")
rep('cultivation',"재배 품종 사이의 유전적 이질성이 크다고 보고되었다[10]","재배 닥나무가 유전적으로 이질적이며 기원이 복잡하다고 보고되었다[10]")
rep('biology',"따라서 식품원료 목록의 학명 표기",
    "반면 국내 미세위성 표지 연구는 B. kazinoki를 B. × hanjiana의 부모 종으로 다루어[8], 같은 'B. kazinoki'라도 논문에 따라 잡종 전체를 가리키기도 하고 부모 종 하나를 가리키기도 한다. 따라서 식품원료 목록의 학명 표기")
d['aliases']=[a if a!="Broussonetia × kazinoki Siebold" else "Broussonetia × kazinoki" for a in d['aliases']]
d['compounds']=[c for c in d['compounds'] if c['name']!='Chlorogenic acid']
for c in d['compounds']:
    if c['name']=='Luteolin':
        c['content_text']="중국 베이징에서 재배한 닥나무속 세 분류군 잎(건조중량) 비교에서 교배 잡종이 아닌 두 분류군은 2.6 ± 0.1·3.4 ± 0.4 μg/g(UPLC-ESI-MS/MS, 루틴 환산 반정량)이었으나 받은 전문에서 학명이 빠져 어느 값이 B. kazinoki인지는 확인하지 못함; 교배 잡종(B. kazinoki × B. papyrifera) 잎의 27.4 ± 2.4 μg/g은 이 종의 값이 아님[12]"
for a in d['assays']:
    if a['compound']=='Luteolin':
        a['compound_ko']="루테올린(잎 페놀 19종 중)"
        a['content']="교배 잡종이 아닌 두 분류군 잎 2.6 ± 0.1·3.4 ± 0.4 μg/g DW(어느 값이 B. kazinoki인지 확인하지 못함); 교배 잡종 잎 27.4 ± 2.4 μg/g DW는 이 종 값이 아님[12]"
    if a['compound']=='Marmesin':
        a['method']="HPLC(원문 미열람으로 조건 칸 비움)"
        a['rationale']="국내 학술지(한국식품영양과학회지, 2016) 논문이 마르메신을 닥나무 추출물의 지표성분으로 삼아 HPLC 분석법을 검증했다는 것은 검색 결과로 확인했으나, 원문은 이 환경에서 열지 못해 Methods 대조를 하지 못했으므로 분석 조건 칸을 비움; 추출물의 부위도 확인하지 못함[35]"
for r in d['production']:
    if r['region']=='경상북도' and r['metric']=='farms':
        r['note']="2024 특용작물 생산실적 시도별 표(기타특용작물 '닥나무'); 같은 표의 경북 면적은 0 ha로 표기"
for s in d['sources']:
    if s['n']==35:
        s['title']="닥나무 추출물의 Marmesin 성분 분석법 검증. 한국식품영양과학회지 2016(KoreaScience JAKO201608259724440) — 논문의 존재·제목·학술지는 검색 결과로 확인했으나 이 환경에서 원문을 열지 못함(분석 조건·부위 미확인)"
        s['publisher']="한국식품영양과학회 / KoreaScience — 검색 결과로만 확인"
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
