import json,sys
p='dossier.json'; d=json.load(open(p))
changes=[]
def rep_sec(key,old,new,why):
    for s in d['sections']:
        if s['key']==key:
            assert old in s['body'],(key,old)
            s['body']=s['body'].replace(old,new); changes.append({"where":f"sections.{key}","before":old,"after":new,"why":why}); return
    raise KeyError(key)
def comp(name): return next(c for c in d['compounds'] if c['name']==name)
def rep_field(obj,field,new,where,why):
    old=obj[field]; obj[field]=new; changes.append({"where":where,"before":old,"after":new,"why":why})

rep_sec('related_species',"이들은 서로 다른 종이므로, 이 문서의 성분·함량·안전 자료는 지충이를 대상으로 한 자료만 썼다[1].",
 "이들은 학명이 서로 다른 별도 원료로 올라 있다[1].",
 "[1]은 문서 작성 방침을 뒷받침하지 않음 — 원자료(I1020)로 확인되는 사실만 남김")
rep_sec('cultivation',"연구에 쓰인 시료는 대부분 자연 군락에서 채집했다: 2025년 유전체 연구는 한국 자연 서식지 개체를 썼고[3], 한국 7개 연안 비교 연구는 6–7월 영양 생장기에 채집해",
 "연구 시료는 자연 군락에서 채집했거나 시판 건조품이었다[3][13][17]: 2025년 유전체 연구는 강원 강릉 안인 해변의 암반 해안에서 채집한 개체를 썼고[3], 한국 7개 연안 비교 연구는 국립해양생물자원관이 분양한 시료로, 6–7월 영양 생장기에 채집해",
 "'대부분 자연 군락' 일반화는 출처 없음. [3] 전문: Anin Beach, Gangneung 채집; [17] 전문: MABIK 분양")
rep_sec('processing',"셀룰라아제(Celluclast) 보조 가수분해물과 그 에탄올 단계 침전 분획은 고지방식 생쥐에서 체중과 백색지방을 줄였다[29].",
 "셀룰라아제 효소로 가수분해한 물질과 그 에탄올 단계 침전 분획 가운데 가수분해물·1분획·3분획은 고지방식을 먹인 생쥐 실험에서 체중과 백색지방 무게를 줄였다(동물 실험)[29].",
 "상표명(Celluclast)을 일반명으로; [29] 초록상 체중·WAT 감소는 STC·STCF1·STCF3 만(STCF2 제외), 동물 실험임을 명시")
rep_sec('safety',"중국 하이난섬 연안 해조 11종의 중금속 위해성 평가에서 지충이 섭취의 위해지수(HI)는 성인에서 1보다 작았지만 어린이에서는 1보다 커 중간 이상의 위험으로 평가되었고, 비소와 크롬이 섭취 제한 요인으로 지목되었다[32].",
 "중국 하이난섬 열대 연안 해조 11종의 중금속 위해성 평가에서 지충이 섭취의 위해지수(HI)는 성인에서 1보다 작았지만 어린이에서는 1보다 커 중간 이상의 위험으로 평가되었다[32]. 같은 연구는 조사한 해조 전체에서 비소와 크롬을 섭취 제한 요인으로 지목했으며, 지충이만의 비소 수치는 초록에 없다[32].",
 "[32] 초록에서 비소·크롬 제한 요인은 해조 전체에 대한 결론 — 지충이 단독 결과로 읽히지 않게 분리")
rep_sec('safety',"세포 실험에서는 서귀포 시료 추출물이 낮은 농도(25·50 µg/mL)에서도 세포 생존율을 낮춘 반면 다른 지역 시료는 100 µg/mL까지 독성이 낮았다[17].",
 "생쥐 대식세포(RAW 264.7) 실험에서는 서귀포 시료 추출물이 낮은 농도(25·50 µg/mL)에서도 세포 생존율을 낮춘 반면 다른 지역 시료 대부분은 100 µg/mL까지 생존율 80% 이상을 유지했다[17].",
 "[17] 전문 3.5절: '대부분' 80% 이상 유지, 세포주 명시")

c=comp('Fucosterol')
rep_field(c,'activity_ko',"갈조류 특유의 스테롤로, 원문은 해운대 추출물의 항염 활성(대식세포 NO 억제)에 기여하는 성분으로 추정했다. 분자 도킹에서 iNOS와 결합했으나 결합 점수(−4.774)는 비교 억제제(−6.848)보다 약했다(세포·컴퓨터 실험)[17]",
 "compounds.Fucosterol.activity_ko","[17] 전문 3.9절: 도킹 점수가 대조 억제제보다 약함 — 과장 방지, 실험 성격 명시")
c=comp('Fucoidan')
rep_field(c,'activity_ko',"대식세포(RAW 264.7)에서 NO 생성과 식작용을, 제브라피시에서 NO 생성과 NF-κB 경로를 높인 면역 증강 효과가 보고되었다(세포·동물 실험)[15]",
 "compounds.Fucoidan.activity_ko","[15] 초록: 식작용은 시험관 결과, 제브라피시는 NO·NF-κB")
c=comp('Sulfated heteropolysaccharide STP-II')
rep_field(c,'activity_ko',"푸코스·자일로스·갈락토스·포도당·글루쿠론산으로 이루어지며, 시험관에서 수산기·초과산화 라디칼 소거능을 보였고 Caco-2 대장암세포 증식을 억제했다(IC50 4.07 mg/mL로 높은 농도; 대조 시스플라틴 35.09 μg/mL)[13]",
 "compounds.STP-II.activity_ko","[13] 전문: IC50 4.07 mg/mL — 높은 농도임을 명시해 과장 방지")
c=comp('Saringosterol')
rep_field(c,'activity_ko',"이소퓨코스테롤·엽록소 a와 함께 분리되었고, 세 화합물의 리파아제 억제 활성은 모체 분획(1 mg/mL에서 83.78%)보다 2–4배 낮았다(효소 실험)[24]",
 "compounds.Saringosterol.activity_ko","[24] 초록: 단일 화합물 활성은 분획보다 2–4배 낮음")

a=d['assays'][2]
rep_field(a,'method',"페놀-황산법(총당) + HPSEC-RID(순도·분자량) + HPLC-RID·GC-FID(단당 조성)","assays[2].method","[13] 전문: 단당 조성은 HPLC(SP0810)과 GC(HP-5, FID, TMS 유도체) 둘 다")
a['conditions']['column']="분자량: Shodex Sugar KS-804; 단당: Shodex Sugar SP0810(HPLC), HP-5 30 m × 0.25 mm × 0.25 μm(GC)"
changes.append({"where":"assays[2].conditions.column","before":"분자량: Shodex Sugar KS-804; 단당: Shodex Sugar SP0810","after":a['conditions']['column'],"why":"[13] 전문 GC 칼럼 추가"})
a['conditions']['sample_prep']=a['conditions']['sample_prep'].replace("정제는 4배 에탄올 침전","정제는 건조 분말 100 g을 같은 pH 2.0 물로 97°C 3.5시간 1회 추출 → 4배 에탄올 침전")
changes.append({"where":"assays[2].conditions.sample_prep","before":"정제는 4배 에탄올 침전 …","after":"정제는 건조 분말 100 g을 같은 pH 2.0 물로 97°C 3.5시간 1회 추출 → 4배 에탄올 침전 …","why":"[13] 전문 정제 단계 추출 조건 보충"})
a=d['assays'][1]
a['conditions']['sample_prep']="70% 에탄올 추출물(해양바이오뱅크 또는 국내 업체에서 입수)"
a['conditions']['instrument']="HPLC-DAD(ESA 70-6186A 검출기); 확인용 Agilent 6530 Q-TOF LC-MS(양이온 모드, Waters Acquity BEH C18 2.1 × 50 mm, 1.7 μm)"
changes.append({"where":"assays[1].conditions","before":"sample_prep '국내 해양바이오뱅크 등', instrument LC-MS 칼럼 없음","after":"입수처 표현 정리, LC-MS 칼럼 추가","why":"[18] 전문 2.1절"})
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
