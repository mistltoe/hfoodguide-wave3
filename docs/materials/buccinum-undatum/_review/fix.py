import json
p='dossier.json'; d=json.load(open(p))
S={s['key']:s for s in d['sections']}
changes=[]
def rep(key,old,new,why):
    b=S[key]['body']; assert old in b,(key,old); S[key]['body']=b.replace(old,new)
    changes.append({"where":f"sections.{key}","before":old,"after":new,"why":why})
rep('overview',"건강기능식품 고시형 원료의 원재료는 아니어서 식약처가 정한 지표성분은 없다[1].",
    "이 목록 항목에는 건강기능식품 관련 표기가 없고, 식약처가 정한 지표성분도 확인되지 않았다[1].",
    "[1](식품원료 목록 I1020)은 건강기능식품 고시 여부를 직접 말하지 않음 — 목록에서 확인되는 범위로 낮춤")
rep('related_species',"Neptunea antiqua(영문 red whelk)가 이 종과 함께 채집되며",
    "Neptunea antiqua(영문 red whelk)가 이 종과 함께 조사되었으며(N. antiqua는 주로 더 깊은 정점에서 채집)",
    "[11] 초록: N. antiqua는 주로 깊은 성층 정점에서만 충분히 채집됨")
rep('processing',"알레르기 항원 단백질의 소화성은 100 ℃ 5분 가열 뒤에도 바뀌지 않았다[5].",
    "추출물을 100 ℃에서 5분 가열해도 알레르기 항원 단백질이 소화효소에 분해되는 정도는 바뀌지 않았다(시험관 모의 소화액 실험)[5].",
    "[5] 전문: 가열한 것은 추출물이며 모의 위액·장액 시험관 실험임을 밝힘")
rep('processing',"이 논문은 시료 종을 키워드에서 Buccinum undatum으로 밝혔으나 시료는 가공업체에서 받은 냉동 고둥 살이었다[10].",
    "이 논문은 시료 종을 키워드에서 Buccinum undatum으로 밝혔으나 시료는 중국 푸젠성 수산 가공업체에서 받은 냉동 고둥 살이었고 종 동정 방법은 적혀 있지 않아, 이 종의 값으로 단정하기 어렵다[10].",
    "[10] 전문 2.1절: 푸젠성 업체 제공 냉동 살, 종 동정 절차 없음 — 근연종 섞임 가능성 명시")
rep('safety',"국내 알레르기 클리닉 환자 1,700명의 피부단자시험에서 4.9%(83명)가 이 종에 양성이었고, 양성자 62명 가운데 38.7%가 특이 IgE 양성이었다[5].",
    "국내 한 대학병원 알레르기 클리닉 환자 1,700명의 피부단자시험에서 4.9%(83명)가 이 종 추출물에 양성(2+ 이상)이었고, 양성자 중 혈청을 검사한 62명 가운데 24명(38.7%)에서 특이 IgE가 높았다[5]. 이는 알레르기 질환자의 감작률이며, 실제 섭취 후 증상을 확인한 것은 아니어서 저자들도 임상적 의의는 더 연구해야 한다고 적었다[5]. 시험에 쓴 고둥은 국내 수산 가공업체가 냉동 상태로 제공한 것으로, 종 동정 방법은 적혀 있지 않다[5].",
    "[5] 전문: 83명 중 62명만 ELISA, 24/62 — '양성자 62명'은 부정확; 감작률을 임상 알레르기로 읽지 않도록 한정; 시료 출처(국내 업체 제공, 동정 미기재) 명시")
rep('safety',"영국 북부 10곳에서 잡은 이 종의 총 비소는 건조중량 기준 45–655 mg/kg이었으나",
    "영국 북부 연안 10곳에서 잡은 이 종의 총 비소는 건조중량 기준 45–655 mg/kg(생시료 기준 값 아님)이었으나",
    "[6] 단위 d.w. — 생/건 기준 혼동 방지")
rep('safety',"잉글랜드에서는 이 종을 포함한 비이매패류의 마비성 패독 감시가 이루어지며, 이에 맞춘 시험법이 검증되었다[9].",
    "잉글랜드 일부 지역에서는 이 종을 포함한 비이매패류의 마비성 패독을 정기 감시하며, 이에 맞춘 두 시험법이 단일 실험실에서 검증되었다; 이 논문은 이 종의 독소 검출 수준은 보고하지 않았다[9].",
    "[9] 초록: 'in parts of England', 시험법 검증 연구로 함량 보고 없음 — 과장 방지")
rep('genetics',"이 분석 과정에서 형태로는 이 종으로 분류된 일부 개체가 다른 물레고둥과 종으로 확인되어 제외되었다[3].",
    "이 분석 과정에서 밍간 시료의 유전적으로 동떨어진 4개체는 이 종이 아닌 것으로 보여 제외되었고, 이 가운데 3개체의 COI 바코딩에서 2개체는 다른 종으로 추정되고 1개체는 동정되지 않았다[3].",
    "[3] 전문: 'removed four divergent individuals from Mingan... COI barcoding of three' — '물레고둥과 종으로 확인'은 원문보다 단정적")
# assays PAH
a=d['assays'][0]
old=a['content']
a['content']="안트라센 평균 4.3 ng/g 습중량(토르스하운, 이 종 최고); ∑PAHs는 원문 안에서 엇갈림 — 결론부는 이 종이 조사 종 가운데 가장 높은 ∑PAHs(11 ng/g)를 보였다고 적었으나, 초록은 11 ± 2 ng/g를 가자미류(common dab, Limanda limanda)의 값으로, 결과부는 농도 순서를 가자미류 > 이 종으로 적어 이 종의 ∑PAHs 값은 확정하지 않음 [8]"
changes.append({"where":"assays[0].content","before":old,"after":a['content'],"why":"[8] 전문 결과부('highest in common dab followed by common whelk')를 더해 내부 불일치를 분명히 하고 이 종 값으로 쓰지 않음; common dab 국문 표기 수정"})
# sources 27 pages
for s in d['sources']:
    if s['n']==27:
        o=s['title']; s['title']=o.replace("Toxicon 2002;40(4)","Toxicon 2002;40(4):419-425")
        changes.append({"where":"sources[27].title","before":o,"after":s['title'],"why":"PubMed 11738235 쪽수 보충"})
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
