import json,sys
p='/home/user/hfoodguide-wave3/docs/materials/diospyros-lotus/dossier.json'
d=json.load(open(p))
changes=[]
S={s['key']:s for s in d['sections']}
def rep(key,old,new,why):
    b=S[key]['body']; assert b.count(old)==1,(key,old)
    S[key]['body']=b.replace(old,new); changes.append({"where":"sections."+key,"before":old,"after":new,"why":why})
rep('history','전통적으로 진정·해열·진통·설사·당뇨 등에 써 왔다는 기록을 바탕으로 뿌리 추출물의 동물 실험이 이어졌다[15][17].',
 '통증·염증·불면(진정)에 써 온 전통 용도를 근거로 뿌리 추출물과 분리 성분의 동물 실험이 이어졌다[15][17].',
 '[15][17] 초록은 통증·수면장애·염증·불면만 전통 용도로 적음. 해열·설사·당뇨는 근거 없음')
rep('processing','열매는 생으로 먹거나 말려 두고 먹으며, 터키에서는 말린 고욤을 수확기 뒤 봄철까지 먹는다[2].',
 '열매는 생으로 먹거나 말려서도 먹으며, 터키 증례 연구에서 말린 고욤을 먹은 환자 3명은 수확기(11–12월)가 지난 3–6월에 입원했다[2].',
 '[2] 전문은 말린 고욤을 먹은 환자의 입원 시기만 적고, 봄철까지 먹는다는 일반 진술은 없음')
rep('safety','위 수술 이력(30.7%)·당뇨(30.7%)·틀니(23%)가 함께 있었다[2].',
 '위 수술 이력(30.7%)·당뇨(30.7%)·치아 보철(23%)이 함께 있었다[2].',
 '[2] 원문은 dental implants/dental prosthesis')
rep('safety','저자들은 고욤 같은 식품에 소화되지 않는 섬유와 과일 탄닌이 많다고 설명하며, 위 수술을 받았거나 씹는 힘이 약한 사람은 많이 먹지 말라고 권했다[2].',
 '저자들은 고욤 등 위석을 잘 일으키는 식품에 셀룰로스·리그닌 같은 소화되지 않는 섬유와 과일 탄닌이 많다고 설명하며, 위장관 수술을 받았거나 구강·치아 건강이 나쁜 사람은 많이 먹지 말라고 권했다[2].',
 '[2] 결론 원문: history of gastrointestinal surgery or poor oral and dental health')
rep('safety','다만 고욤 덜 익은 열매의 탄닌 함량이나 익은 정도에 따른 위석 위험 차이를 이 종에서 직접 잰 자료는 확인하지 못함.',
 '덜 익은 감을 먹은 뒤 위 위석이 생긴 성인 증례가 있지만[39], 한국 소아 위석 33명을 정리한 연구에서는 증상이 생긴 22명이 씨가 든 익은 감이나 곶감을 여러 개 먹었고 덜 익은 감을 먹은 이력은 없었다[40]. 즉 위석 위험은 덜 익은 열매에만 한정되지 않는다. 이 증례들의 \'persimmon\'은 종을 밝히지 않아 고욤(D. lotus) 자료로 볼 수 없고, 고욤 덜 익은 열매의 탄닌 함량이나 익은 정도에 따른 위석 위험 차이를 이 종에서 직접 잰 자료는 확인하지 못함.',
 '지시에 따라 덜 익은 열매 탄닌·위석 관련 내용을 PubMed 출처(PMID 39355066, 3385587)와 함께 추가, 종 미구분 명시')
# compounds
C={c['name']:c for c in d['compounds']}
def crep(name,field,old,new,why):
    v=C[name][field]; assert v.count(old)==1,(name,old)
    C[name][field]=v.replace(old,new); changes.append({"where":f"compounds.{name}.{field}","before":old,"after":new,"why":why})
crep('Gallic acid','content_text','70 °C 건조 시 최고 341.79 mg/kg(LC-MS/MS)[4]','70 °C·0.5 m/s 건조 341.79 mg/kg(80 °C·1.0 m/s 342.23 mg/kg로 비슷), 건물/생체 기준은 원문 미기재(LC-MS/MS)[4]',
 '[4] 표7에서 80 °C·1.0 m/s 값(342.23)이 더 커 70 °C를 단독 최고로 쓸 수 없음')
crep('Gallic acid','activity_ko','분리 갈산이 CaCo-2 세포에 IC50 2.6 μg/mL의 세포독성을 보임[6]','부위를 초록에 밝히지 않은 추출물에서 분리한 갈산이 CaCo-2 암세포에 IC50 2.6 μg/mL의 세포독성을 보임(시험관)[6]',
 '[6] 초록은 사용 부위를 밝히지 않음 — 열매 자료로 섞이지 않게 표시, 세포 결과 명시')
crep('Myricetin','activity_ko','분리 성분으로서 항산화·항증식 활성에 관련된 페놀 화합물로 보고됨[6]','부위 미기재 추출물에서 분리된 페놀 성분의 하나로, 항산화·항증식 활성(시험관)과 관련된다고 보고됨[6]',
 '[6] 부위 미기재·시험관 결과임을 명시')
# assays
a=d['assays'][0]
old=a['rationale']; new=old.replace("같은 연구진이 이를 '주성분'으로 삼아 효능을 비교했다[7][9].","[7]은 표준품 대조로 미리시트린을 정량했고, 다른 연구진의 잎 추출물 연구도 미리시트린을 주성분으로 삼았다[9].")
assert new!=old; a['rationale']=new
changes.append({"where":"assays[0].rationale","before":"같은 연구진이 이를 '주성분'으로 삼아 효능을 비교했다[7][9].","after":"[7]은 표준품 대조로 미리시트린을 정량했고, 다른 연구진의 잎 추출물 연구도 미리시트린을 주성분으로 삼았다[9].","why":"[7](KIST 강릉)과 [9](전주대)는 다른 연구진"})
a=d['assays'][2]
a['content']=a['content'].replace('70 °C·0.5 m/s 건조과 갈산 341.79 mg/kg[4]','70 °C·0.5 m/s 건조과 갈산 341.79 mg/kg(표7, 단위 mg/kg — 건물/생체 기준 원문 미기재)[4]')
changes.append({"where":"assays[2].content","before":"…건조과 갈산 341.79 mg/kg[4]","after":"…(표7, 단위 mg/kg — 건물/생체 기준 원문 미기재)[4]","why":"생/건 기준 명시 요구 — 원문은 기준을 밝히지 않음"})
d['sources'].append({"n":39,"title":"A Rare Case of Gastric Phytobezoar (Diospyrobezoar) in a Healthy Adult. Cureus. 2024 (PMID 39355066)","url":"https://pubmed.ncbi.nlm.nih.gov/39355066/","publisher":"Cureus (PubMed)","accessed":"2026-11-02"})
d['sources'].append({"n":40,"title":"Gastrointestinal phytobezoars in childhood. J Pediatr Surg. 1988 (PMID 3385587)","url":"https://pubmed.ncbi.nlm.nih.gov/3385587/","publisher":"Journal of Pediatric Surgery (PubMed)","accessed":"2026-11-02"})
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('/home/user/hfoodguide-wave3/docs/materials/diospyros-lotus/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
