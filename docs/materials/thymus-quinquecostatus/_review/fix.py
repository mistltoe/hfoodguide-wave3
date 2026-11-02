import json
p='dossier.json'; d=json.load(open(p))
changes=[]
def sec(k): return [s for s in d['sections'] if s['key']==k][0]
def rep(where,obj,key,old,new,why):
    assert old in obj[key], (where,old)
    obj[key]=obj[key].replace(old,new); changes.append({"where":where,"before":old,"after":new,"why":why})
S=sec('safety')
rep('sections.safety',S,'body',' 리뷰 논문은 정유의 주성분 티몰이 페놀처럼 작용해 낮은 농도에서도 미생물·곤충에 독성을 보인다고 적었다[3].','',
    '[3] 리뷰 전문(PMC9268194)에서 티몰의 미생물·곤충 독성을 이렇게 적은 대목을 찾지 못해 문장 삭제')
rep('sections.safety',S,'body','잎 샘털 분비물에서 GC-MS 로 알칼로이드 18종이 보고되었고','잎에서 GC-MS 로 알칼로이드 18종이 확인되었고(조직화학 관찰상 샘털 분비세포가 알칼로이드를 분비)',
    '[33] 초록: GC-MS 분석 대상은 잎이고, 샘털이 알칼로이드를 분비한다는 것은 조직화학 관찰 결과')
B=sec('biology')
rep('sections.biology',B,'body','다른 연구는 방패 모양 샘털의 머리 세포가 8–12개라고 관찰했다[32].','백리향과 서양 타임 품종(T. vulgaris \'Elsbeth\')을 함께 관찰한 다른 연구는 방패 모양 샘털의 머리 세포를 8–12개로 적었다(종별 구분은 초록에 없음)[32].',
    '[32]는 두 종(백리향·T. vulgaris \'Elsbeth\')을 함께 관찰한 연구로, 8–12개 수치가 백리향만의 값인지 초록에서 구분되지 않음 — 타임 자료 섞임 방지')
rep('sections.biology',B,'body','잎 샘털에서는 GC-MS 로 18종의 알칼로이드성 물질이 검출되었다는 보고도 있다[33].','잎에서 GC-MS 로 18종의 알칼로이드가 확인되었고, 조직화학 관찰에서 방패·머리 모양 샘털의 분비세포가 알칼로이드를 분비했다는 보고도 있다[33].',
    '[33] 초록: GC-MS 는 잎 전체 분석, 샘털 분비는 조직화학 관찰')
C=sec('cultivation')
rep('sections.cultivation',C,'body','백리향은 씨앗으로도 번식하지만 보통 꺾꽂이를 쓰며, 4–6월에 꽂으면','리뷰가 인용한 국내 재배 연구에 따르면 백리향은 씨앗으로도 번식하지만 보통 꺾꽂이를 쓰며, 4–6월에 꽂으면',
    '[3]은 리뷰이므로 1차 연구를 리뷰 인용으로 밝힘')
rep('sections.cultivation',C,'body','(수증기 증류 2.62%)','(수증기 증류 2.62%, 생체·건물 기준은 리뷰에 적혀 있지 않음)',
    '[3] 원문에 2.62% 의 기준(생/건)이 없음 — [4]의 생체중 기준 0.40% 와 직접 비교 금지')
cmp={c['name']:c for c in d['compounds']}
rep('compounds.Linalool.content_text',cmp['Linalool'],'content_text','중국 산둥 옌타이 시료 물 증류 정유 52.003%[8]','중국 시료 지상부 물 증류 정유 52.003%(채취지는 초록에 없음)[8]',
    '[8] 초록·서지에 산둥 옌타이 채취 정보가 없음(전문 열람 불가)')
rep('compounds.Borneol.content_text',cmp['Borneol'],'content_text','중국 옌타이 시료 정유 10.911%[8]','중국 시료 정유 10.911%(채취지는 초록에 없음)[8]',
    '[8] 초록에 옌타이 정보 없음')
rep('compounds.o-Cymene.content_text',cmp['o-Cymene'],'content_text','오대산 계통 정유의 시멘 11.13%는 전문 텍스트에서 위치 접두어가 빠져 o-/p- 구분 확인 못함[5]','오대산 계통 정유의 시멘 11.13%[5]는 후속 연구[4]가 p-시멘으로 인용하므로 o-시멘 값으로 쓰지 않음',
    '[4] 고찰에서 [5]의 11.13%를 p-cymene 으로 인용')
rep('compounds.Geraniol.content_text',cmp['Geraniol'],'content_text','충북 시료 trans-제라니올 36.85–39.75%(리뷰 인용)[3]','충북 시료 trans-제라니올 36.85%(고체상미세추출)·39.75%(동시증류추출)(리뷰 인용)[3]',
    '[3] 표: 두 값은 시료 범위가 아니라 두 추출법의 값')
rep('compounds.Carvacrol.activity_ko',cmp['Carvacrol'],'activity_ko','이 종 정유의 대장균 DXR 효소 억제 IC50 59 μg/mL','이 종 정유(원문 약어 TQ)의 대장균 DXR 효소 억제 IC50 59 μg/mL',
    '[15] 전문에서 학명이 약어로만 남아 TQ=백리향 대응은 초록 순서로만 확인')
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
