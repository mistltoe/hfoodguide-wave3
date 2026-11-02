import json
p='dossier.json'; d=json.load(open(p))
S={s['key']:s for s in d['sections']}
reps=[
('overview',"인도에서는 '굴라르(gular)'로 불린다[3].","북인도에서는 '굴라르(Gular)'로 불린다[10]."),
('overview',"열매·껍질 메탄올 추출물(250·500 mg/kg)이 생쥐에서 항암제로 줄어든 백혈구·혈소판 수를 회복시켰다는 보고도 있다[24].","열매·껍질 메탄올 추출물(250·500 mg/kg)을 13일 먹인 생쥐에서 항암제(사이클로포스파마이드)에 의한 백혈구·혈소판 감소가 덜했다는 동물 보고가 있으나, 효과는 껍질 추출물이 열매 추출물보다 컸다[24]."),
('biology',"여름 평균기온이 3–5°C 오르자 벌의 번식은 줄고 씨앗 생산은 거의 두 배가 되었다[20].","서늘한 계절보다 평균기온이 3–5°C 높은 여름에는 벌의 번식이 줄고 씨앗 생산은 거의 두 배였다(인도 벵갈루루의 계절 비교)[20]."),
('genetics',"이 결과는 무화과나무속과 벌 사이의 '한 종 대 한 종' 관계를 이 종에서 뒷받침한다[19].","연구진은 넓은 지역에서 한 종의 꽃가루받이 벌이 맡는 경우가 더 흔할 수 있다고 보았고, 오스트레일리아에서 채집한 벌은 대륙 아시아 개체군과 뚜렷이 분화되어 있었다[19]."),
('safety',"3,000 mg/kg 이하에서는 죽음이나 부작용이 없었다[11].","3,000 mg/kg 미만(원문 'under 3000 mg/kg')에서는 죽음이나 부작용이 없었다[11]."),
('related_species',"프리바이오틱 연구에서도 무화과와 '움바르(umbar)'는 따로 시험되었고","프리바이오틱 연구에서도 무화과와 '움바르(umbar, PubMed 서지에 F. racemosa로 색인됨)'는 따로 시험되었고"),
]
log=[]
for k,a,b in reps:
    assert a in S[k]['body'],(k,a); S[k]['body']=S[k]['body'].replace(a,b); log.append({'where':'sections.'+k,'before':a,'after':b})
for c in d['compounds']:
    if c['name']=='Chlorogenic acid':
        b=c['content_text']; c['content_text']="덜 익은(녹색) 열매의 페놀 함량이 높은 분획(FEF; 초록에 분획 용매 설명 없음)에서 검출(함량 수치는 초록에 없음)"
        log.append({'where':'compounds.Chlorogenic acid.content_text','before':b,'after':c['content_text']})
    if c['name']=='Calcium':
        b=c['part']; c['part']="굴라르(초록에 부위 명시 없음)"
        log.append({'where':'compounds.Calcium.part','before':b,'after':c['part']})
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(log,open('_review/log.json','w'),ensure_ascii=False,indent=1)
