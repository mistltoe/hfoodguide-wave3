import json,sys
p='/home/user/hfoodguide-wave3/docs/materials/cladosiphon-okamuranus/dossier.json'
d=json.load(open(p))
changes=[]
def rep(where,obj,key,old,new,why):
    s=obj[key]
    assert s.count(old)==1,(where,old)
    obj[key]=s.replace(old,new)
    changes.append({"where":where,"before":old,"after":new,"why":why})
S={s['key']:s for s in d['sections']}
rep('sections.overview',S['overview'],'body',
 "사람 연구로는 건강한 성인 40명이 이 종 유래 푸코이단 3.0 g/일을 12주 마신 무작위 이중맹검 예비 시험이 있으며, 8주째 NK 세포 활성이 섭취 전보다 높았고 시험식품에 의한 이상 반응은 관찰되지 않았다[18].",
 "사람 연구로는 건강한 성인 40명을 푸코이단군(이 종 유래 푸코이단 3.0 g/일 음료, 20명)과 위약군(20명)으로 나눠 12주 진행한 무작위 이중맹검 예비 시험이 있으며, 푸코이단군의 NK 세포 활성이 8주째 섭취 전보다 높았으나 위약군과 비교해 유의한 차이는 남성에서만 보고되었고, 시험식품에 의한 이상 반응은 관찰되지 않았다[18]. 이 시험에는 원료 생산 업체 소속 연구자가 참여했다[18].",
 "[18] 초록: 40명은 두 군 합계(각 20명)이고 3.0 g/일은 푸코이단군만 섭취; 위약 대비 유의 차이는 남성 8주째만. 저자 소속에 원료 업체 포함")
rep('sections.history',S['history'],'body',
 "평소 모즈쿠를 자주 먹는 사람의 기초값이 더 높았다[24].",
 "헬리코박터 파일로리 음성자 가운데서는 평소 모즈쿠를 자주 먹는 사람의 기초값이 거의 먹지 않는 사람보다 높았다[24].",
 "[24] 초록은 이 비교를 H. pylori 음성자에 한정해 보고함")
rep('sections.cultivation',S['cultivation'],'body',
 "비교적 깊은 중간 육성장에 15–20일, 더 얕은 육성장에 35–40일 두고, 마지막으로 폭풍 피해를 피하는 본 양식장으로 옮긴다[2].",
 "비교적 깊은 육묘장(nursery)에 15–20일 두어 곧추선 조체를 틔우고, 더 얕고 밝은 후기 육성장(post-nursery)에 35–40일 둔 뒤, 마지막으로 그보다 깊어 폭풍 피해를 피하는 본 양식장으로 옮긴다[2].",
 "[2] 전문: nursery 는 발아 단계(육묘장), post-nursery 는 그보다 얕은 곳, 본 양식장은 post-nursery 보다 깊음 — '중간 육성장' 표현이 단계를 뒤섞음")
rep('sections.cultivation',S['cultivation'],'body',
 "중간 육성장은 수심 7.5 m, 그 다음 육성장은 2 m, 본 양식장은 3 m였고, 가장 깊은 중간 육성장에서는",
 "육묘장은 수심 7.5 m, 후기 육성장은 2 m, 본 양식장은 3 m였고, 가장 깊은 육묘장에서는",
 "[2] 전문의 nursery/post-nursery 용어에 맞춤")
rep('sections.cultivation',S['cultivation'],'body',
 "최근에는 생육 불량과 탈색이 잦아져 양식 기술 개선이 과제로 꼽힌다[2].",
 "양식 환경 변동이 커지고 양식 해조 전반에서 생육 불량과 탈색이 잦아지는 상황이라 적극적인 양식 기술 개선이 중요해질 것으로 보았다[2].",
 "[2] 는 양식 해조 일반의 생육 불량·탈색을 말함(이 종에 한정한 보고 아님)")
rep('sections.safety',S['safety'],'body',
 "푸코이단 독성: 쥐에 이 종 푸코이단을 먹였을 때",
 "푸코이단 독성: 급성 독성 시험에서 Wistar 쥐에 이 종 푸코이단을 먹였을 때",
 "[22] 초록은 급성 독성(acute toxicity) 시험임")
rep('sections.safety',S['safety'],'body',
 "사람에서는 모즈쿠 푸코이단을 하루 최대 4.05 g씩 2주 먹은 20명에서 이상 소견이 없었고[21],",
 "사람에서는 '모즈쿠 푸코이단'을 하루 최대 4.05 g씩 2주 먹은 20명에서 이상 소견이 없었으나(초록에 학명이 없어 이 종 유래인지, 같은 '모즈쿠'로 불리는 미끈가지 등 유래인지 확인하지 못함)[21],",
 "[21] 초록에 원료 종이 적혀 있지 않음 — 이토 모즈쿠(미끈가지)와 섞였을 가능성")
C={c['name']:c for c in d['compounds']}
rep('compounds.L-Fucose.activity_ko',C['L-Fucose'],'activity_ko',
 "α-1,3 결합 주쇄에 C-2 푸코스 곁가지가 붙는 구조로 보고되었다[7]",
 "α-1,3 결합 주쇄에 C-2 푸코스 곁가지가 붙는 구조로 보고되었다[7]. 다만 다른 연구들은 C-2 곁가지를 글루쿠론산으로 보고해 구조 해석이 갈린다[10][12]",
 "[7] 의 푸코스 곁가지 해석은 [10][12] 의 글루쿠론산 곁가지와 다름 — 대비를 밝힘")
C['L-Fucose']['source']=[7,10,12]
rep('compounds.Fucoxanthin.activity_ko',C['Fucoxanthin'],'activity_ko',
 "광합성에서 빛 에너지를 엽록소 a로 넘기는 색소다[13][14].",
 "갈조류 세포에서 주로 광수확 색소-단백질 복합체(FCP)에 결합해 있으며, 이 종 배양 발아체에서 FCP가 분리·정제되었다[3][13].",
 "[13][14] 초록에는 '엽록소 a로 에너지 전달' 서술이 없음; [3] 의 FCP 결합 서술로 바꿈")
rep('compounds.Fucoidan.activity_ko',C['Fucoidan'],'activity_ko',
 "건강한 성인 3.0 g/일 12주 섭취 시 8주째 NK 세포 활성 상승(소규모 무작위 예비 시험)[18]",
 "건강한 성인 3.0 g/일 12주 섭취 시 8주째 NK 세포 활성이 섭취 전보다 상승(위약 대비 유의 차이는 남성만, 군당 20명 예비 시험)[18]",
 "[18] 초록: 위약 대비 유의 차이는 남성에서만")
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('/home/user/hfoodguide-wave3/docs/materials/cladosiphon-okamuranus/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
