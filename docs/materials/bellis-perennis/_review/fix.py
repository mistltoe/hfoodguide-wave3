import json
p='/home/user/hfoodguide-wave3/docs/materials/bellis-perennis/dossier.json'
d=json.load(open(p))
S={s['key']:s for s in d['sections']}
changes=[]
def rep(key,a,b,why):
    s=S[key]; assert a in s['body'],(key,a); s['body']=s['body'].replace(a,b); changes.append({"where":f"sections.{key}","before":a,"after":b,"why":why})
rep('overview',"추출물의 항산화·혈당·지질·상처 치유 관련 결과는 세포·동물·달걀 배아 실험이며, 동종요법 시험을 빼면 사람 대상 연구는 없다고 정리되었다[2].",
 "추출물의 항산화·혈당·지질·상처 치유 관련 결과는 세포·동물·달걀 배아 실험이며, 동종요법 시험을 빼면 사람 대상 연구는 없다고 정리되었다[2]. 이 결과들은 대부분 꽃(일부는 지상부나 꽃·잎 혼합) 추출물로 얻은 것이어서 식품원료 사용부위인 잎의 효과로 옮겨 읽을 수 없다[2][3][9][12].",
 "혈당[3](자가 제조 추출물은 꽃)·지질[9]·상처[12] 결과가 모두 꽃 시료인데 잎 원료 개요에 부위 구분 없이 쓰여 있어 부위를 밝힘")
rep('processing',"연구용 추출물은 말린 식물체를 갈아 50% 에탄올로 초음파 추출하거나[3]",
 "연구용 추출물은 말린 꽃을 갈아 50% 에탄올로 초음파 추출하거나[3]",
 "[3] 결과 3.1: 자가 제조 추출물은 지역에서 거둔 꽃으로 만들었다고 씀")
rep('processing',"분리한 사포닌 10종이 3–30 µM 에서",
 "꽃에서 분리한 사포닌 10종이 3–30 µM 에서","[10] 꽃 시료임을 분명히 함")
rep('genetics',"첫째 반수체 조립은","첫째 일배체형(haplotype 1) 조립은","[5] 'haplotype' 은 일배체형이며 반수체(haploid)와 다름")
rep('genetics',"두 반수체는 일부 염색체","두 일배체형은 일부 염색체","[5] 용어 정정(haplotype)")
rep('biology',"데이지 잎 표피 세포에는 기능하는 엽록체가 적당히 들어 있어",
 "데이지 원예 품종의 표피 포장세포에는 기능하는 엽록체가 적당히 들어 있어",
 "[20] 초록은 'epidermal pavement cells'(재배 품종)라고만 쓰고 기관(잎)을 밝히지 않음")
rep('safety',"데이지는 사포닌을 많이 함유하며[3],",
 "데이지는 사포닌이 많다고 기술되며(구조 연구는 꽃·땅속 부위 시료이고 잎의 사포닌 함량은 확인하지 못함)[3][9][25],",
 "[3]은 사포닌이 많다고만 쓰고 근거 연구는 꽃[9]·땅속 부위[25]; 잎으로 읽히지 않게 함")
c=[x for x in d['compounds'] if x['name']=='Perennisaponin O'][0]
a=c['activity_ko']; b="사람 소화관 암세포주(HSC-2·HSC-4·MKN-45) 증식 억제 IC50 6.9–14.3 µM(세포 실험)[2][11]"
c['activity_ko']=b; changes.append({"where":"compounds[Perennisaponin O].activity_ko","before":a,"after":b,"why":"[11] 초록: human digestive tract carcinoma HSC-2·HSC-4·MKN-45 — 위암 세포주만이 아님(HSC-2·4 는 구강암)"})
asy=d['assays'][1]
a=asy['rationale']; b=a.replace("3년간 세 지역의 꽃을 매달 비교해","세 지역에서 각기 다른 해(2000·2001·2003년)에 3–10월 매달 거둔 꽃을 비교해")
assert a!=b; asy['rationale']=b; changes.append({"where":"assays[1].rationale","before":a,"after":b,"why":"[4] 2.결과·3.2: 지역마다 한 해씩 채집(3년×3지역 아님)"})
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('/home/user/hfoodguide-wave3/docs/materials/bellis-perennis/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
