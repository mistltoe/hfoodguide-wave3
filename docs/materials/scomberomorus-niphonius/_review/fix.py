import json
p='/home/user/hfoodguide-wave3/docs/materials/scomberomorus-niphonius/dossier.json'
d=json.load(open(p))
changes=[]
def sec(key,old,new,why):
    for s in d['sections']:
        if s['key']==key:
            assert old in s['body'],(key,old)
            s['body']=s['body'].replace(old,new); changes.append({"where":f"sections.{key}","before":old,"after":new,"why":why}); return
    raise KeyError(key)
sec('biology','같은 중국 산란장 조사에서 자어가','2015년 산란기에 중국의 한 주요 산란장에서 한 고해상도 조사에서 자어가',
    '[6]은 [5]와 별개 조사(2015년 산란기, 중국의 한 주요 산란장)로, \"같은 산란장 조사\"라는 근거가 원문에 없음')
sec('biology','수컷과 암컷의 지방산 조성 차이는 생식소·장·간에서 두드러졌다[32].',
    '삼치를 포함한 해산어 6종 비교에서 암수 간 지방산 조성 차이는 대체로 생식소·장·간에서 두드러졌으나 그 정도는 종에 따라 크게 달랐다[32].',
    '[32] 초록은 6종 전체의 경향을 말하며 \"종에 따라 크게 다르다\"고 했음 — 삼치 고유 결과처럼 쓴 것을 바로잡음')
sec('related_species','다른 속이므로, \'mackerel\'이라는 영문만으로 자료를 섞지 않는다[1, 12].',
    '다른 속(고등어 Scomber japonicus 등)이므로, \'mackerel\'이라는 영문만으로 자료를 섞지 않는다[1].',
    '[12]는 고등어속을 다루지 않음. 고등어 행(Scomber japonicus, Chub mackerel)은 [1] 원자료로 확인')
sec('genetics','단백질 암호화 유전자 13개, tRNA 22개, rRNA 2개, 조절영역으로 모두 37개 유전자가 있으며',
    '단백질 암호화 유전자 13개, tRNA 22개, rRNA 2개를 합친 37개 유전자와 조절영역(D-loop)이 있으며',
    '[8] 원문의 37개는 13+22+2 이며 조절영역은 따로 셈')
sec('processing','시판품 8종에서 감칠맛 펩타이드(Arg-Asp, Asp-Gly-Val, Asp-Arg, Asp-Lys)가 확인되었다[24].',
    '시판품 8종을 비교한 연구에서는 펩타이드 서열이 제품마다 달랐고, 여러 시료에 반복된 펩타이드 가운데 Arg-Asp, Asp-Gly-Val, Asp-Arg, Asp-Lys 4종이 감칠맛·감칠맛 증강 효과를 보였다[24].',
    '[24] 초록: 서열은 제품마다 달랐고 반복 서열 8개 중 4개가 감칠맛을 보임 — 8종 모두에서 확인된 것은 아님')
sec('processing','70 ℃에서 참나무 톱밥으로 25분 열훈연한 제품이 관능 평가가 가장 좋았고, 10 ℃ 저장에서 42일까지 품질이 유지되었다[12].',
    '70 ℃에서 참나무 톱밥으로 25분 열훈연한 제품이 관능 평가가 가장 좋았고, 10 ℃ 저장에서 42일까지 품질이 유지되었다[12]. 같은 논문은 이 제품의 지방산을 DHA 4.19, EPA 1.82 g/100 g으로 보고했으나, 지방산 표의 합계(약 21 g/100 g)와 포화지방산 합계(6.30 g/100 g)가 같은 논문 영양성분 표의 조지방 2.353 g/100 g·포화지방 0.635 g/100 g보다 커 표 사이 기준이 맞지 않는다[12].',
    '열훈연 필렛 지방산 값(표 3)이 조지방(표 2)보다 커 기준 불일치 — 본문에 근거와 함께 밝혀 독자가 g/100 g 필렛 값으로 오독하지 않게 함')
# compounds
note='(원문 표 3 표기 g/100 g; 표 3 합계 약 21 g/100 g이 같은 논문 조지방 2.353 g/100 g보다 커 기준 불일치)'
for c in d['compounds']:
    if c['name']=='Docosahexaenoic acid':
        o=c['content_text']; c['content_text']=o.replace('열훈연 필렛 4.19 g/100 g[12]','열훈연 필렛 4.19 g/100 g'+note+'[12]')
        changes.append({"where":"compounds.Docosahexaenoic acid.content_text","before":o,"after":c['content_text'],"why":"[12] 표 3 지방산 값이 표 2 조지방과 맞지 않음을 함께 적음"})
    if c['name']=='Eicosapentaenoic acid':
        o=c['content_text']; c['content_text']=o.replace('열훈연 필렛 1.82 g/100 g[12]','열훈연 필렛 1.82 g/100 g'+note+'[12]')
        changes.append({"where":"compounds.Eicosapentaenoic acid.content_text","before":o,"after":c['content_text'],"why":"같은 기준 불일치 표기"})
    if c['name']=='Palmitic acid':
        o=c['content_text']; c['content_text']='4.03 g/100 g(포화지방산 합계 6.30 g/100 g; 같은 논문 표 2의 포화지방 0.635 g/100 g과 약 10배 차이로 기준 불일치)[12]'
        changes.append({"where":"compounds.Palmitic acid.content_text","before":o,"after":c['content_text'],"why":"[12] 표 3 ∑SFA 6.30 vs 표 2 포화지방 0.635 g/100 g 불일치"})
    if c['name']=='Palmitoleic acid':
        o=c['content_text']; c['content_text']='1.46 g/100 g'+note+'[12]'
        changes.append({"where":"compounds.Palmitoleic acid.content_text","before":o,"after":c['content_text'],"why":"같은 기준 불일치 표기"})
    if c['name']=='Arg-Asp':
        o=c['content_text']; c['content_text']='시판품 8종 비교에서 여러 시료에 반복된 펩타이드 중 하나로, 감칠맛·감칠맛 증강 효과 확인(함량 정량값은 초록에 없음)[24]'
        changes.append({"where":"compounds.Arg-Asp.content_text","before":o,"after":c['content_text'],"why":"8종 모두에서 확인된 것이 아님"})
for n in d['nutrients']:
    o=n['form']; n['form']=o.replace('; 원문 표 2)','; 원문 표 2 — 같은 논문 표 3 지방산 합계는 이 표의 조지방·포화지방보다 커 기준이 맞지 않음)')
    changes.append({"where":"nutrients[0].form","before":o,"after":n['form'],"why":"영양 표와 지방산 표의 기준 불일치를 표시"})
for a in d['assays']:
    if a['compound'].startswith('4-Hydroxy'):
        o=a['part']; a['part']='10% 소금물(4 °C, 12시간) 염지 후 열풍(60 °C 24시간)·냉풍(10 °C 60시간)·햇볕(5일) 건조한 삼치 토막(약 200 g, 칭다오 시장 구입)'
        changes.append({"where":"assays[0].part","before":o,"after":a['part'],"why":"[13] 2·3절 원문 조건 보충"})
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open(p.replace('dossier.json','_review/changes.json'),'w'),ensure_ascii=False,indent=1)
print(len(changes))
