import json,sys
p='/home/user/hfoodguide-wave3/docs/materials/lepidium-apetalum/dossier.json'
d=json.load(open(p))
changes=[]
def rep(where,obj,key,old,new,why):
    s=obj[key]
    assert s.count(old)==1,(where,old)
    obj[key]=s.replace(old,new)
    changes.append({"where":where,"before":old,"after":new,"why":why})
S={s['key']:s for s in d['sections']}
rep('sections.overview',S['overview'],'body',
 "따라서 아래의 성분·효능 자료 가운데 상당수는 식품원료 부위(순)가 아닌 씨앗 자료이며, 각 항목에 부위를 따로 적었다[2, 3].",
 "그 부위별 연구도 2024년 5월 결실기에 채집한 다 자란 식물을 나눠 분석한 것이어서, 잎 자료라도 어린 순 자료와 같지 않다[2]. 따라서 아래의 성분·효능 자료 가운데 상당수는 식품원료 부위(순)가 아닌 씨앗 자료이며, 각 항목에 부위를 따로 적었다[2, 3].",
 "[2] 전문 2.2절: 2024년 5월 전초 채집 후 뿌리·줄기·잎·씨앗·씨껍질로 나눔 — 잎 자료가 어린 순 자료가 아님을 밝힘")
rep('sections.processing',S['processing'],'body',
 "원료 부위는 논문에 분명히 적혀 있지 않다[10].",
 "원료 부위는 논문에 분명히 적혀 있지 않다[10]. 이 논문 서론은 씨앗(정력자) 약재를 소개하는 반면 다른 연구진은 이 추출물을 전초 추출물로 인용해, 순 자료로 볼 근거는 없다[10, 2].",
 "[10] 전문 서론은 'The seeds of LW … Tinglizi/Jungryukza'로 시작하고 2.2절은 부위 없이 'LW 1 kg'; [2] 3.4절은 이를 'whole plant' 추출물로 인용 — 순 자료로 오인되지 않게 보강")
C={c['name']:c for c in d['compounds']}
g=C['Glucotropaeolin']
old=g['content_text']
g['content_text']="이 종(씨앗)에서는 탈황 형태인 cis·trans-데설포글루코트로페올린이 분리됨(정량값 없음)[14]; 총설은 이 종 씨앗의 글루코시놀레이트와 그 분해산물(벤질 이소티오시아네이트 등)을 주요 활성 성분으로 보았으나, 총설 성분표에서 글루코트로페올린 원형은 이 종이 아닌 다른 기원 약재(재쑥 씨로 보임) 항목에 실려 있어 이 종에서의 원형 검출·함량은 확인하지 못함[22]"
changes.append({"where":"compounds[Glucotropaeolin].content_text","before":old,"after":g['content_text'],"why":"[22] 전문 표 2에서 glucotropaeolin(5번)은 출처 1(데스쿠라이노사이드 등과 같은 쪽, 재쑥 씨로 보임)에만, cis/trans-DG(19·20번)는 출처 2에 실림 — 원형이 이 종에서 보고된 것처럼 읽히지 않게 고침"})
g['part']="씨앗(정력자) — 탈황 유도체로만 확인"
q=C['Quercetin']
old=q['part']; q['part']="70% 에탄올 추출물(원료 부위 불분명 — 순 자료 아님)"
changes.append({"where":"compounds[Quercetin].part","before":old,"after":q['part'],"why":"[10] 원료 부위 미기재, 서론은 씨앗 약재 소개"})
s=C['Sinapine']
old=s['content_text']
s['content_text']="Semen Lepidii(정력자 약재, 초록에 기원 종 명시 없음)에서 RP-HPLC로 분포 조사[23]; 70% 에탄올 추출물(부위 불분명)에서 표준품 대조로 검출(정량값 없음)[10]"
changes.append({"where":"compounds[Sinapine].content_text","before":old,"after":s['content_text'],"why":"[23] 초록은 'Semen Lepidii'만 적고 기원 종을 밝히지 않음; [10] 부위 불분명 명시"})
a=d['assays'][0]
old=a['part']; a['part']="잎(정유) — 결실기(5월) 성숙 식물의 잎으로, 어린 순 자료는 아님"
changes.append({"where":"assays[0].part","before":old,"after":a['part'],"why":"[2] 2.2절: 2024년 5월 전초 채집(씨앗·씨껍질 함께 분리) — 순과 '가장 가까운' 표현을 성숙 잎으로 정확히 함"})
rep('assays[0].rationale',a,'rationale',"순만 따로 분석한 자료는 확인하지 못함.","시료는 씨앗이 맺힌 5월의 전초에서 떼어 낸 잎이라 식품원료 부위인 어린 순과 성분 비율이 다를 수 있다[2]. 순만 따로 분석한 자료는 확인하지 못함.","부위·채집 시기 명시")
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('/home/user/hfoodguide-wave3/docs/materials/lepidium-apetalum/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
