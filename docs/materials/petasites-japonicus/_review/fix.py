import json
p='dossier.json'; d=json.load(open(p))
S={s['key']:s for s in d['sections']}
changes=[]
def rep(key,old,new,why):
    b=S[key]['body']; assert old in b,(key,old); S[key]['body']=b.replace(old,new)
    changes.append({"where":f"sections.{key}","before":old,"after":new,"why":why})
rep('overview','잎과 잎자루에는 3,5-디카페오일퀸산·클로로겐산·퓨키노산 같은 카페오일퀸산류와 캠페롤·퀘르세틴 배당체가 많이 들어 있다[8].',
 '잎과 잎자루의 80% 에탄올 추출물에서는 3,5-디카페오일퀸산·클로로겐산·퓨키노산 같은 카페오일퀸산류와 캠페롤·퀘르세틴 배당체가 많이 정량되었다[8].',
 '[8] 의 함량은 생 잎이 아니라 에탄올 추출물(EPJ) 건조중량 기준')
rep('overview','페타시테닌은 쥐에서 간 종양을 일으켰고','페타시테닌은 음용수에 섞어 먹인 쥐에서 간 종양을 일으켰고',
 '[12] 은 순수 성분을 음용수 0.01–0.05%로 투여한 동물시험')
rep('history','동아시아와 유럽의 민간에서는 머위를 역병·열병·알레르기·염증에 써 왔다고 정리되어 있다[19].',
 '동아시아와 유럽의 민간에서는 머위속(Petasites) 식물을 역병·열병·알레르기·염증에 써 왔다고 정리되어 있다[19].',
 '[19] 초록의 주어는 유럽을 포함한 머위속 식물이며 머위 한 종이 아님')
rep('cultivation','국내 머위 재배면적·생산량 공식 통계는 농림축산식품부 「2023 채소류 생산실적」에서 품목을 찾지 못해 확인하지 못함.',
 '국내 머위 재배면적·생산량 공식 통계는 이번 조사에서 확인하지 못함.',
 '근거로 든 문서를 출처로 확인할 수 없고 로컬 통계(regional_crops·special_crops)에도 머위 품목이 없음')
rep('processing','피롤리지딘 알칼로이드는 수돗물에 데치고 삶으면 줄어들기 때문에, 줄기나 꽃봉오리는 먹기 전에 이를 줄이는 손질이 권장된다[5].',
 '피롤리지딘 알칼로이드는 수돗물에 데치고 삶으면 줄어들기 때문에, 줄기나 꽃봉오리는 먹기 전에 이를 줄이는 손질이 권장된다[5]. 일본 농림수산성 조사에서는 국산 머위 91점·머위 꽃봉오리(후키노토) 62점 대부분에서 피롤리지딘 알칼로이드가 검출되었고, 이 성분은 물에 녹는 성질이 있어 데친 물을 버리고 물에 우리는 전통 손질로 머위는 1~3할, 꽃봉오리는 2~4할 수준까지 줄었다[29].',
 '섭취 전 처리(데치기·물우림)의 공공기관 근거 추가')
rep('processing','피롤리지딘 알칼로이드가 에탄올에 녹고 고온에서 불안정하다는 점을 이용해 독성 성분을 줄이려는 방법이었다[10].',
 '피롤리지딘 알칼로이드가 에탄올에 녹고 고온에서 불안정하다는 점을 이용해 독성 성분을 줄이려는 방법이었으나, 완성된 추출물의 피롤리지딘 알칼로이드 함량은 논문에 제시되지 않았다[10].',
 '[10] 은 PA 저감을 의도했을 뿐 KP-1 의 PA 함량을 측정·보고하지 않음')
rep('processing','2026년 1·2상 시험에서 체중 1 kg당 200 mg 투여가 안전하다고 보고했다[28].',
 '2026년 개 대상 1·2상 시험에서 체중 1 kg당 200 mg 투여가 안전하다고 보고했다(사람 자료 아님)[28].',
 '동물(개) 임상시험임을 명시')
rep('safety','에탄올 처리한 잎 열수 추출물(KP-1)의 13주 반복 투여 시험에서 무독성량(NOAEL)은 1,250 mg/kg/일이었고,',
 '에탄올 처리한 잎 열수 추출물(KP-1)의 13주 쥐 반복 투여 시험에서 무독성량(NOAEL)은 암컷 1,250 mg/kg/일, 수컷 1,250 mg/kg/일 미만으로 판단되었고,',
 '[10] 본문 결과·결론은 수컷 NOAEL 을 1,250 미만으로 씀(초록만 암수 1,250)')
rep('safety','국내 밭 시험의 잔류 살충제 위해성은 무시할 수준으로 평가되었다[16]. 독초인 털머위와 헷갈리지 않도록 주의해야 한다[17].',
 '국내 밭 시험의 잔류 살충제 위해성은 무시할 수준으로 평가되었다[16]. 독초인 털머위와 헷갈리지 않도록 주의해야 한다[17]. 머위 꽃줄기에 대한 알레르기 반응도 보고되었으며, 쑥·돼지풀 꽃가루와 교차반응하는 열에 약한 알레르겐이 원인일 수 있다고 정리되어 있다[5]. 일본 농림수산성은 피롤리지딘 알칼로이드를 줄이기 위해 데치기·물우림을 거쳐 먹도록 안내한다[29].',
 '알레르기 근거([5])와 섭취 전 처리 안내(공공기관) 추가')
# compounds: clarify extract DW basis
for c in d['compounds']:
    if 'mg/100 g DW[8]' in c['content_text']:
        old=c['content_text']; c['content_text']=old.replace('mg/100 g DW[8]','mg/100 g(에탄올 추출물 건조중량)[8]')
        changes.append({"where":f"compounds.{c['name']}.content_text","before":old,"after":c['content_text'],"why":"[8] 의 DW 는 에탄올 추출물(EPJ) 건조중량 기준"})
    if 'mg/100 g DW(에탄올 추출물)[8]' in c['content_text']:
        old=c['content_text']; c['content_text']=old.replace('235.0 ± 4.8 mg/100 g DW(에탄올 추출물)[8]','235.0 ± 4.8 mg/100 g(에탄올 추출물 건조중량)[8]')
        changes.append({"where":f"compounds.{c['name']}.content_text","before":old,"after":c['content_text'],"why":"기준 명확화"})
    if c['name']=='Bakkenolide B':
        old=c['activity_ko']; c['activity_ko']='세균 뉴라미니다아제 억제 성분 탐색에서 분리됐으나 억제 효과는 거의 없음(IC50 > 200 μM, 시험관)[19]'
        changes.append({"where":"compounds.Bakkenolide B.activity_ko","before":old,"after":c['activity_ko'],"why":"[19] 에서 바케놀라이드 B 는 불활성(IC50 > 200 μM)이고 활성은 바케놀라이드 D·카페오일퀸산"})
# assays
a=d['assays'][1]; old=a['content']; a['content']=old.replace('mg/100 g DW;','mg/100 g;').replace('mg/100 g DW[8]','mg/100 g(모두 에탄올 추출물 건조중량 기준)[8]')
changes.append({"where":"assays[1].content","before":old,"after":a['content'],"why":"추출물 기준 명시"})
a['conditions']['sample_prep']=a['conditions']['sample_prep'].replace('30분 진탕, 3000 rpm 15분 원심','30분 진탕(200 rpm), 3000 rpm·10 °C 15분 원심')
a=d['assays'][2]
oldc=dict(a['conditions'])
a['conditions']['column']='Ascentis C18, 4.6 × 250 mm, 5 µm (Supelco)'
a['conditions']['linearity']='검량선 5–100 µg/mL, r = 0.9997 ± 0.0002(n = 3), 농도별 정확도 94.38–102.90%'
a['conditions']['sample_prep']='500 mg/mL 투여액은 2000배 희석(0.25 mg/mL 투여액은 희석 없음), 30분 초음파 후 0.45 µm 여과'
a['rationale']='독성시험 투여액의 함량·안정성을 퓨키노산 기준으로 검증했다(실온 4시간·냉장 192시간 안정)[10]. 검출·정량한계와 회수율은 본문에 없어 비워 둠.'
changes.append({"where":"assays[2].conditions","before":json.dumps(oldc,ensure_ascii=False)[:300],"after":"column 4.6 × 250 mm, 5 µm; linearity r = 0.9997; sample_prep 0.25 mg/mL 무희석","why":"[10] 3.1.1–3.1.2 에 칼럼 규격·검량선 결과가 있음"})
# sources
for s in d['sources']:
    if s['n']==21:
        s['title']='Petasites japonicus Leaves Alleviate Depression in Dextran Sulfate Sodium-Induced Colitis Mice Through the BDNF/TrkB Pathway and Modulation of Inflammation. Int J Mol Sci. 2026'
d['sources'].append({"n":29,"title":"농림수산성 「食品中のピロリジジンアルカロイド類の含有実態調査結果について（第2報）」(2018-08-31 보도자료)","url":"https://www.maff.go.jp/j/press/syouan/nouan/180831.html","publisher":"일본 농림수산성","accessed":"2026-11-02"})
changes.append({"where":"sources[21].title","before":"...Through the BDNF/TrkB Pathway","after":"...Through the BDNF/TrkB Pathway and Modulation of Inflammation","why":"원제 일부 누락"})
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
