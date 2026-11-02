import json,sys
p='/home/user/hfoodguide-wave3/docs/materials/amelanchier-alnifolia/dossier.json'
d=json.load(open(p,encoding='utf-8'))
S={s['key']:s for s in d['sections']}
changes=[]
def rep(sec,old,new,why):
    b=S[sec]['body']; assert old in b,(sec,old); S[sec]['body']=b.replace(old,new); changes.append({"where":f"sections.{sec}","before":old,"after":new,"why":why})
rep('overview',"이 종을 원재료로 하는 건강기능식품 고시형 원료는 목록에서 확인되지 않는다[1].",
    "두 행 모두 대분류가 '식품원료(A코드)'이며[1], 이 종을 원재료로 하는 건강기능식품 고시형 원료는 확인하지 못함.",
    "[1](I1020 식품원료 목록)은 건강기능식품 고시 여부를 말하지 않음; 로컬 원자료로 대분류만 확인")
rep('overview',"효과 근거는 대부분 이런 동물 실험이고, 사람 연구는 건강한 성인 20명이 10주 동안 동결건조 열매 40 g을 매일 먹은 단일군 예비 시험 하나다[7].",
    "효과 근거는 대부분 이런 동물 실험이고, 사람에서 대사 효과를 본 연구는 건강한 성인 20명이 10주 동안 동결건조 열매 40 g을 매일 먹은 단일군·비맹검 예비 시험 하나다(그 밖의 사람 연구는 안토시아닌 흡수 연구)[7, 18].",
    "[7] 본문: 이전 유일한 사람 연구는 흡수(생체이용률) 연구라고 씀; [18]도 사람 혈장 연구")
rep('related_species',"학명 확인이 필요하다[2, 33].","학명 확인이 필요하다[33].","[2] 리뷰에는 A. lamarckii 언급이 없음; [33] 초록에서 Amelanchier lamarckii 'Ballerina' 확인")
rep('cultivation',"토양 조건을 크게 가리지 않고 겨울 추위에 강해 폴란드·리투아니아 등에서도 재배 시험이 이어지고 있다[4, 5].",
    "토양 조건을 크게 가리지 않고 겨울 추위에 강해 폴란드에서는 시험 포장과 소규모 재배가 이루어지고, 리투아니아에서도 잘 자랄 수 있다고 소개된다[4, 5].",
    "[5]는 리투아니아 재배 '시험'을 말하지 않고 재배 가능하다고만 씀; [4]는 폴란드 소규모 재배·시험 포장")
rep('biology',"열매는 껍질·과육·씨로 이루어지며, 17개 품종","열매는 껍질·과육·씨로 이루어지며[2], 17개 품종","앞 구절의 출처는 [2]")
rep('genetics',"엽록체 전체 게놈으로는 채진목속이 단계통으로 묶이지 않았으나 핵 리보솜 DNA로는 단계통이었고, 연구진은 이를 북미 남서부에서 일어난 옛 엽록체 포획으로 설명했다[24].",
    "엽록체 전체 게놈으로는 채진목속이 단계통으로 묶이지 않았으나 핵 리보솜 DNA로는 단계통이었고, 연구진은 근연 속(페라필룸·말라코멜레스)의 위치가 두 자료에서 엇갈리는 것을 북미 남서부에서 일어난 옛 엽록체 포획으로 설명했다[24].",
    "[24] 초록: 엽록체 포획은 Peraphyllum·Malacomeles 위치 충돌에 대한 설명")
old_s=S['safety']['body']
new_s=("식약처 목록에서 오리잎채진목은 열매에 한해 사용가능한 식품원료(A코드)이다[1]. 건강기능식품 고시형 원료는 확인하지 못해, 고시 섭취 시 주의사항도 확인하지 못함. "
"시안배당체를 처음 정량한 원 논문 초록에 따르면 익은(보라색) 열매의 아미그달린은 생과 1 kg당 43–129 mg, 프루나신은 5–19 mg이었고, 두 성분 모두 초록 열매 단계에서는 매우 낮았다[15]. "
"2025년 리뷰는 같은 연구를 인용하며 익은 열매 아미그달린 42.00–129.20, 프루나신 5.01–13.71(덜 익은 열매 0–60.00, 0–30.90)을 'g/kg'으로 적었는데, 원 논문 초록의 mg/kg과 단위·범위가 달라 리뷰의 옮겨 적기 오류로 보인다[2, 15]. "
"아미그달린·프루나신은 씹거나 가공할 때 벤즈알데하이드·시안화수소·포도당으로 분해되며[2], 생과를 먹을 때 씨에서 오는 아몬드 같은 풍미가 난다고 묘사된다[4]. "
"원 논문 전문을 보지 못해 이 값이 통열매 기준인지 씨에 몰려 있는지는 확인하지 못했고, 씨만 떼어 시안배당체를 정량한 1차 논문도 PubMed에서 찾지 못해 씨앗의 함량은 확인하지 못함.\n\n"
"가지는 시안 생성 조직이어서, 잘게 썬 가지를 사료의 75%로 먹인 소에서 떨림·체중 감소·설사·호흡곤란이 나타났고 시안화수소 5 mg/kg(체중) 상당량에서 중독이 빠르게 진행되었다[14]. "
"건강한 성인 20명이 동결건조 열매 40 g/일을 10주 먹은 시험에서 간·신장·심혈관 이상은 없었으나 당 섭취가 늘어 내당능 장애인은 다른 단 음식을 줄이라고 권했다[7]. 국내 공공기관의 알레르기·잔류농약 정보는 확인하지 못함.")
S['safety']['body']=new_s
changes.append({"where":"sections.safety","before":old_s,"after":new_s,"why":"[15](Plant Physiol 1980, 결빙 시 HCN 방출로 막 손상 측정)은 소 중독을 뒷받침하지 않아 제거하고 [15] 자리를 시안배당체 원 논문(J Food Compos Anal 2008;21:249-254)으로 바꿈; 원 논문 초록은 mg/kg 생중량(43–129, 5–19)이라 리뷰의 g/kg은 오기로 정리; '2008년 연구' 표기는 리뷰 본문에 연도가 없어 원 논문으로 직접 인용; 분해 문장 [2], 아몬드 풍미 [4] 로 출처 분리; 고시 문장은 [1]이 말하지 않아 '확인하지 못함'으로"})
C={c['name']:c for c in d['compounds']}
def crep(name,field,new,why):
    old=C[name][field]; C[name][field]=new; changes.append({"where":f"compounds.{name}.{field}","before":old,"after":new,"why":why})
crep('Amygdalin','part',"열매(익은 보라색 열매; 통열매·씨 구분은 원 논문 전문 미확인)","원 논문 초록은 'fresh berries' 기준")
crep('Amygdalin','content_text',"익은 열매 43–129 mg/kg 생중량, 초록 열매에서는 매우 낮음(원 논문 초록)[15]; 2025년 리뷰는 같은 값을 42.00–129.20 'g/kg'으로 옮겨 적음(단위 오기로 보임)[2]","원 논문 초록 단위 mg/kg FW 확인")
C['Amygdalin']['source']=[15,2]
crep('Prunasin','part',"열매(익은 보라색 열매; 통열매·씨 구분은 원 논문 전문 미확인)","원 논문 초록은 'fresh berries' 기준")
crep('Prunasin','content_text',"익은 열매 5–19 mg/kg 생중량, 초록 열매에서는 매우 낮음(원 논문 초록)[15]; 2025년 리뷰 표기는 5.01–13.71 'g/kg'(단위·범위 다름)[2]","원 논문 초록 단위 mg/kg FW, 상한 19 확인")
C['Prunasin']['source']=[15,2]
crep('Chlorogenic acid','content_text',C['Chlorogenic acid']['content_text'].replace("총페놀산(가수분해 후 아글리콘) 59 mg/100 g 생중량[31]","총페놀산(가수분해 후 아글리콘, 클로로겐산만의 값 아님) 59 mg/100 g 생중량[31]"),"[31] 값은 전체 페놀산(아글리콘) 값")
crep('Ursolic acid','content_text',"전체 트라이테르페노이드 72.21–91.31 mg/kg 건조중량(본문; 초록은 66.55–91.31) 중 약 84%(UPLC-Q-TOF)[4]","[4] 초록과 본문 범위가 다름을 표기")
for a in d['assays']:
    if a['compound']=='Ursolic acid':
        old=a['content']; a['content']="전체 트라이테르페노이드 72.21–91.31 mg/kg 건조중량(본문; 초록은 66.55–91.31), 그중 우르솔산 약 84%[4]"
        changes.append({"where":"assays.Ursolic acid.content","before":old,"after":a['content'],"why":"[4] 초록·본문 범위 차이 표기"})
src={s['n']:s for s in d['sources']}
old=dict(src[15])
src[15].update({"title":"Carotenoids and cyanogenic glucosides in saskatoon berries (Amelanchier alnifolia Nutt.) — J Food Compos Anal 2008;21(3):249-254 (PubMed 미수록, AGRIS 서지·초록만 확인, 전문 확인 못함)",
 "url":"https://agris.fao.org/search/en/providers/122535/records/65df379363b8185d9cabafff","publisher":"FAO AGRIS","accessed":"2026-11-02"})
changes.append({"where":"sources[15]","before":old['title'],"after":src[15]['title'],"why":"기존 [15](Plant Physiol 1980 결빙 막 손상)는 소 독성 근거가 아님; 번호를 시안배당체 원 논문으로 재사용"})
o2=src[2]['title']
src[2]['title']=o2.replace("리뷰가 인용한 2008년 시안배당체 연구와 캐나다 농업농식품부 통계 원문은 확인 못함","리뷰가 인용한 캐나다 농업농식품부 통계 원문은 확인 못함; 시안배당체 값은 원 논문[15]과 단위가 다름")
changes.append({"where":"sources[2].title","before":o2,"after":src[2]['title'],"why":"리뷰 본문에 연도 표기 없음; 원 논문 대조 결과 반영"})
json.dump(d,open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
json.dump(changes,open('/home/user/hfoodguide-wave3/docs/materials/amelanchier-alnifolia/_review/changes.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print(len(changes))
