import json,sys
p='docs/materials/sasa-veitchii/dossier.json'
d=json.load(open(p))
ch=[]
def rep(where,old,new,why):
    global d
    if where.startswith('sections.'):
        k=where.split('.')[1]
        s=[x for x in d['sections'] if x['key']==k][0]
        assert old in s['body'],(where,old); s['body']=s['body'].replace(old,new)
    ch.append({"where":where,"before":old,"after":new,"why":why})
rep('sections.overview',
 "모두 세포·동물 실험이다[15, 16, 20, 13]. 사람 대상 임상시험은 확인하지 못함.",
 "모두 세포·동물 실험이다[7, 13, 15, 16, 20]. 이 결과들은 일본 일반의약품 추출액(가공 중 구리클로로필린나트륨이 생김)이나 열수 추출 농축액으로 얻은 것이어서, 식품원료로 쓰는 잎을 그대로 먹을 때의 효과로 옮겨 쓸 수 없다[1, 19, 23]. 사람 대상 임상시험은 확인하지 못함.",
 "항염 근거 [7] 추가; 의약품 알칼리 추출액 결과를 식품원료(잎) 효과로 읽지 않도록 구분 문장 추가([19]·[23] 전문의 제조법·SCC 0.25%)")
rep('sections.history',
 "2010년 무렵부터 일본 연구진은 열수 추출물의 고분자 다당 분획이 면역 반응과 바이러스 감염에 미치는 영향을 연구했다[9, 10, 12, 13].",
 "2010년 무렵부터 일본 연구진은 잎 추출물의 다당 분획(열수 추출물의 고분자 분획 등)이 면역 반응과 바이러스 감염에 미치는 영향을 세포 수준에서 연구했다[9, 10, 12, 13].",
 "[13]·[12] 초록은 '추출물의 다당 분획'이라고만 쓰고 열수 추출물이라 하지 않음([9]·[10]만 열수 추출물 BWMP)")
rep('sections.history',
 "2020년대에는 유방암 세포, 입술·입천장 배아 세포, 장내 미생물에 대한 연구로 넓어졌으나",
 "2020년대에는 유방암 세포, 사람 입술 간엽 세포·배아 입천장 간엽 세포, 쥐의 장 상피·장내 미생물에 대한 연구로 넓어졌으나",
 "[21] KD 세포는 입술 간엽 세포(배아 세포 아님), HEPM 은 배아 입천장 간엽 세포; [24] 는 쥐 21일 투여")
rep('sections.history',
 "이는 조릿대와 관계없는 다른 식물 이름으로 보이며 그렇게 적힌 근거는 확인하지 못함.",
 "이는 조릿대와 관계없는 다른 식물 이름으로 보이며(같은 목록에 Sarracenia 학명 행은 따로 없다[1]) 그렇게 적힌 근거는 확인하지 못함.",
 "로컬 I1020 원자료에서 '사라세니아'·'Sarracenia' 는 이 행의 이명 칸에만 있음을 확인")
rep('sections.safety',
 "오래된 잎은 규산이 건조 중량의 40% 안팎까지 쌓일 수 있다[4].",
 "오래된 잎은 규산이 건조 중량의 최대 41% 까지 쌓일 수 있다[4].",
 "[4] 초록 값(up to 41 % of dry mass)으로 맞춤")
# compounds: Sasa albo-marginata parts
for c in d['compounds']:
    if c['part']=="잎 열수 추출물(논문 학명 Sasa albo-marginata)":
        c['part']="열수 추출물(부위는 초록에 없음; 논문 학명 Sasa albo-marginata)"
ch.append({"where":"compounds[트리신·p-쿠마르산·바닐린·p-히드록시벤즈알데히드·3-히드록시피리딘].part","before":"잎 열수 추출물(논문 학명 Sasa albo-marginata)","after":"열수 추출물(부위는 초록에 없음; 논문 학명 Sasa albo-marginata)","why":"[27] 초록은 'hot water extract of Sasa albo-marginata' 라고만 쓰고 잎이라 하지 않음"})
for c in d['compounds']:
    if c['name']=='Polysaccharides':
        old=c['activity_ko']
        c['activity_ko']=old.replace("항인플루엔자 활성 분획[12]","항인플루엔자 활성을 보인 잎 다당 분획(렉틴 마이크로어레이 분석)[12]").replace("가성광견병 바이러스 플라크 형성 억제(세포 실험)[13]","추출물의 다당 분획이 가성광견병 바이러스 플라크 형성을 농도 의존적으로 억제(세포 실험)[13]")
        ch.append({"where":"compounds[Polysaccharides].activity_ko","before":old,"after":c['activity_ko'],"why":"[12]·[13] 초록 표현에 맞춤"})
for a in d['assays']:
    if a['compound']=='Silicon dioxide':
        old=a['method']; a['method']="몰리브덴 청(molybdenum blue) 비색법([2] 논문의 방법; 41% 값은 [4] 논문)"
        ch.append({"where":"assays[Silicon dioxide].method","before":old,"after":a['method'],"why":"측정법은 [2] 초록, 41% 는 [4] 초록 — 두 논문을 구분"})
# source citations
fix={12:("Biosci Biotechnol Biochem 2017;81(9)","Biosci Biotechnol Biochem 2017;81(9):1687-1689"),
     14:("Biocontrol Sci 2019;24(3):145","Biocontrol Sci 2019;24(3):145-154"),
     17:("Nagoya J Med Sci 2017;79(3):279-","Nagoya J Med Sci 2017;79(3):279-290"),
     21:("Biomed Res 2023;44(2):73-","Biomed Res 2023;44(2):73-80"),
     22:("Nagoya J Med Sci 2024;86(2):223-","Nagoya J Med Sci 2024;86(2):223-236"),
     24:("J Nat Med 2026 (","J Nat Med 2026;80(2):484-492 ("),
     25:("J Nat Med 2019;73(1)","J Nat Med 2019;73(1):331-337"),
     19:("Nagoya J Med Sci 2020;82(3):509-","Nagoya J Med Sci 2020;82(3):509-"),
     16:("전문 확인; 성분표는 추출본에 없음","전문 확인(V2 재확인: 시판 일반의약품 추출액, 1 mL=잎 2.82 g); 성분표는 추출본에 없음")}
for s in d['sources']:
    if s['n'] in fix:
        o,n=fix[s['n']]
        if o!=n:
            assert o in s['title'],s['n']; s['title']=s['title'].replace(o,n)
            ch.append({"where":f"sources[{s['n']}].title","before":o,"after":n,"why":"PubMed 서지(쪽수·권호)로 보완"})
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(ch,open('docs/materials/sasa-veitchii/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(ch))
