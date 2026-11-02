import json,sys
sys.path.insert(0,'/home/user/hfoodguide-wave3/docs/materials')
p='/home/user/hfoodguide-wave3/docs/materials/sasa-quelpaertensis/dossier.json'
d=json.load(open(p))
S={s['key']:s for s in d['sections']}
changes=[]
def rep(key,old,new,why):
    b=S[key]['body']; assert b.count(old)==1,(key,old)
    S[key]['body']=b.replace(old,new); changes.append({"where":f"sections.{key}","before":old,"after":new,"why":why})
rep('overview',"건강기능식품 고시형 원료의 원재료로는 올라 있지 않다[1].",
 "세 행의 대분류는 모두 '식품원료(A코드)'이며, 건강기능식품 고시형 원료로 올라 있다는 근거는 찾지 못했다[1].",
 "[1](I1020 식품원료 목록)은 고시형 건강기능식품 원료 여부를 말하지 않음 — 원자료에 있는 대분류만 적고 나머지는 '찾지 못함'으로 낮춤")
rep('safety',"건강기능식품 고시형 원료가 아니므로 고시 섭취 시 주의사항은 없다[1].",
 "건강기능식품 고시형 원료로 확인되지 않아, 고시된 섭취 시 주의사항도 찾지 못했다[1].",
 "[1]은 식품원료 목록이라 고시형 원료가 '아니다'를 단정할 근거가 아님")
rep('safety',"500 mg 을 16주 동안 마시는 물에 타서 주었고, 저자들은 이 범위를 독성 없는 범위로 여겼지만 별도의 독성 시험 결과는 아니다[3, 13].",
 "500 mg 을 16주 동안 마시는 물에 타서 주었고, [3]의 저자들은 기존 연구의 100–300 mg/kg 을 근거로 500 mg/kg 을 효과가 있으면서 독성 부작용이 없는 범위로 여겼을 뿐 별도의 독성 시험을 한 것은 아니다[3, 13].",
 "[3] 고찰 원문: 500 mg/kg 용량이 'effective, nontoxic-side-effect-producing range'로 '여겨졌다'고만 씀 — 누가 무엇을 근거로 판단했는지 명확히")
rep('genetics',"다른 표본의 엽록체 DNA 조각과 맞춘 결과 평균 일치도는 99.83%, 최저 99.21% 였다[5].",
 "제주조릿대와 같은 종으로 보기도 하는 근연종의 표본 11점에서 얻은 엽록체 DNA 조각과 맞춘 결과 평균 일치도는 99.83%, 최저 99.21% 였고, 일부 영역에 틈과 불일치가 있었다[5].",
 "[5] 전문: 비교 대상은 제주조릿대 다른 표본이 아니라 이명으로 거론되는 근연종의 증거표본 11점(틈 5점·불일치 8점) — 같은 종 표본으로 읽히지 않게 고침")
rep('genetics',"저자들은 핵 유전체를 포함한 추가 분자 분류 연구가 있어야 근연종과의 관계를 확정할 수 있다고 보았다[5].",
 "저자들은 두 종의 엽록체 유전체 전체를 비교하는 후속 분자 분류 연구로 근연종과의 관계를 밝힐 수 있다고 보았다[5].",
 "[5] 결론은 'entire chloroplast genomes' 기반 후속 연구를 제안 — 핵 유전체는 언급 없음")
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('/home/user/hfoodguide-wave3/docs/materials/sasa-quelpaertensis/_review/changes.json','w'),ensure_ascii=False,indent=1)
from check_dossier import sentences
n=sum(len(sentences(s['body'])) for s in d['sections'])
m=sum(len(d.get(k) or []) for k in ['compounds','assays','sources','aliases'])
print(n,m)
