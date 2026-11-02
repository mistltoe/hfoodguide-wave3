import json
p='dossier.json'; d=json.load(open(p))
S={s['key']:s for s in d['sections']}
changes=[]
def rep(sec,old,new,why):
    b=S[sec]['body']; assert old in b,(sec,old); S[sec]['body']=b.replace(old,new); changes.append({"where":f"sections.{sec}","before":old,"after":new,"why":why})
rep('overview','과즙의 주된 플라보노이드는 헤스페리딘이고[10, 12]','과즙의 주된 플라보노이드는 헤스페리딘이고[10]','[12]는 온실 묘목(과즙 아님)의 폴리페놀 연구라 과즙 근거가 아님')
rep('biology','멕시코산 열매를 14주 동안 추적한 연구에서','열매를 생육 14주 동안 추적한 연구에서','[9] 초록에 산지가 없음(저자 소속만 멕시코) — 산지 확인 못함')
rep('cultivation','멕시코에서는 과수원과 수출업체 사이 공급망 문제가 연구될 만큼 산업 규모가 크다[15]','멕시코의 퍼시안 라임 공급망에서는 과수원과 수출업체 사이가 끊겨 중간 상인이 늘어나는 구조 문제가 연구되었다[15]','[15]는 공급망 구조 문제만 소개하며 산업 규모 판단은 출처에 없음')
rep('cultivation','같은 연구는 충남 공주의 퍼시안 라임 잎에서 감귤 황화엽맥투명바이러스(CYVCV)를 국내 처음 확인했고, 잎맥 투명·잎 뒤틀림 증상을 보고했다[16].','같은 연구는 감귤 황화엽맥투명바이러스(CYVCV)를 국내에서 처음 확인했는데, 충남 공주의 퍼시안 라임도 감염 기주였고 유레카 레몬과 함께 잎맥 투명·잎 뒤틀림·잎 뒷면 수침 증상을 보였다[16].','[16] 전문: 국내 첫 확인은 바이러스 자체(칼라만시·금감·레몬 등 6기주)이며 라임만의 첫 확인이 아님')
rep('history','감귤 생산은 인도·멕시코·브라질·스페인이 이끈다고','감귤 생산은 미국과 함께 인도·멕시코·브라질·스페인이 이끈다고','[15] 원문은 "alongside the United States, citrus fruit production is led by India, Mexico, Brazil, and Spain"')
rep('processing',"식약처 생산실적에 오른 '라임과피추출물'은 개별인정형 원료로 학명이 Citrus aurantifolia여서 이 종의 제품 생산실적으로 볼 수 없다[1].","개별인정형 원료 '라임과피추출물'(제2025-26호)은 학명이 Citrus aurantifolia여서 그 제품 생산실적을 이 종의 것으로 볼 수 없다[1].",'"생산실적에 오른"은 [1](식품원료 목록)이 말하지 않는 내용 — 출처와 맞게 고침')
rep('safety','국내 연구진도 감귤류(라임)를 만진 뒤 강한 햇빛을 쬔 환자 2명에서 염증 없이 색소침착만 나타난 사례가 보고되었으나, 이 사례들은 라임의 종을 밝히지 않았다[25, 26].','국내 연구진이 보고한 2명은 염증 없이 손에 색소침착만 나타났는데, 1명은 태국 요리 수업에서 라임을 맨손으로 짠 뒤, 다른 1명은 미국에서 오렌지·자몽을 맨손으로 깐 뒤 강한 햇빛을 쬐었다; 라임 추출물 첩포 뒤 자외선 A 10 J/cm² 이상에서 홍반과 색소침착이 재현되었으나 라임의 종은 밝히지 않았다[26].','[26] 전문: 두 환자 모두 라임이 아니며(1명은 오렌지·자몽), [25]는 이 국내 사례와 무관')
c=[x for x in d['compounds'] if x['name']=='Isopimpinellin'][0]
old=c['activity_ko']; c['activity_ko']='푸로쿠마린이지만 이 출처는 광독성 시험 대상에 넣지 않음(활성 자료 확인하지 못함)[6]'
changes.append({"where":"compounds.Isopimpinellin.activity_ko","before":old,"after":c['activity_ko'],"why":"[6]은 피부 시험이 필요한 성분으로 프소랄렌·베르갑텐·잔토톡신·리메틴만 꼽음"})
for nm in ['Bergapten','Isopimpinellin']:
    c=[x for x in d['compounds'] if x['name']==nm][0]
    old=c['content_text']; new=old.replace('타히티라임 껍질 이소핌피넬린·베르갑텐 합 168 μg/g[7]','타히티라임 껍질 프소랄렌류(베르갑텐·이소핌피넬린으로 보이나 원문 화합물 번호 대응 확인 못함) 168 μg/g[7]')
    assert new!=old; c['content_text']=new
    changes.append({"where":f"compounds.{nm}.content_text","before":old,"after":new,"why":"[7] 전문은 화합물 번호로만 'psoralens ... and/or ...'(168 μg/g)라 적어 성분 대응이 확정되지 않음"})
a=d['assays'][0]; old=a['content']
a['content']=old.replace('이소핌피넬린·베르갑텐 합 168 μg/g[7]','프소랄렌류(베르갑텐·이소핌피넬린 추정) 168 μg/g, 게라닐옥시 유도체 2종이 주성분(392·352 μg/g, 대응 확인 못함)[7]')
assert a['content']!=old
changes.append({"where":"assays[0].content","before":old,"after":a['content'],"why":"[7] 전문 대조 — 168 μg/g 성분 대응 불확실, 주성분 수치 보충"})
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
