import json
p='dossier.json'; d=json.load(open(p))
S={s['key']:s for s in d['sections']}
changes=[]
def rep(key,old,new,why):
    b=S[key]['body']; assert old in b,(key,old); S[key]['body']=b.replace(old,new); changes.append({"where":f"sections.{key}","before":old,"after":new,"why":why})
rep('history','1950년대 독일에서는 그롬웰 추출물이 뇌하수체 호르몬 분비를 막는다는 동물 연구가 발표되었다[17].',
 '1958년에는 그롬웰의 차단 작용으로 뇌하수체 호르몬 생산을 조절한다는 제목의 논문이 내분비학 학술지에 실렸다(초록 없음)[17].',
 '[17]은 초록이 없어 제목만 확인됨 — 나라(독일)·동물 연구라는 서술은 근거 없음')
rep('cultivation','1979년 폴란드 논문은 재배 조건을 달리해 기른 그롬웰을 다루었다[23].',
 '1979년 폴란드 논문은 재배 조건을 달리해 기른 그롬웰의 피임 작용을 다루었다(제목만 확인)[23].',
 '[23] 제목은 피임 작용(contraceptive properties) 비교 — 주제를 빠뜨림')
rep('cultivation','메틸자스모네이트 처리 식물은 대조군보다 새싹 길이가 최대 36%, 건조중량이 최대 55% 줄었다[5].',
 '메틸자스모네이트 처리 식물은 대조군보다 지상부(shoot) 길이가 최대 36%, 지상부 건조중량이 최대 55% 줄었다[5].',
 '[5] 원문은 shoot length·dry weight — "새싹"은 오역')
rep('cultivation','뿌리 주변 세균 3개 균주는 시험관과 온실 모두에서 이 색소를 늘렸다[20, 21].',
 '뿌리 주변 세균 3개 균주는 시험관과 온실 모두에서 이 색소를 늘렸고[20], 그 가운데 Chitinophaga sp. R-73072 균주를 접종한 무균 재배 뿌리에서는 1,328개 유전자의 발현이 바뀌었다[21].',
 '[21]은 한 균주(R-73072)의 무균 재배 전사체 연구로 "3개 균주·시험관·온실"을 말하지 않음 — 출처를 나눔')
rep('processing','이 종의 동결건조 물 추출물을 과망간산칼륨으로 산화하면 쥐 간 탈요오드효소 억제 활성이 낮아졌다[15].',
 '이 종을 포함한 몇몇 식물의 물 추출물은 과망간산칼륨으로 산화하면 쥐 간 마이크로솜 탈요오드효소 억제 활성(시험관)이 낮아졌다[15].',
 '[15] 초록은 여러 식물 추출물에 대한 일반 서술 — 이 종 단독 결과처럼 쓰지 않게 고침')
rep('processing','17일 된 캘러스 메탄올 추출물은 쥐 미세아교세포 실험(0.8 mg/mL)에서 TNF-α·IL-1β 분비를 줄였다[8]. 같은 제목의 2020년 판 논문에는 편집 요건 미충족을 이유로 한 철회 공지가 나왔다[9].',
 '17일 된 캘러스 메탄올 추출물은 LPS로 자극한 신생 쥐 1차 미세아교세포 실험(세포 수준, 0.8 mg/mL)에서 TNF-α·IL-1β 분비를 줄였다[8]. 같은 제목으로 2020년 온라인에 먼저 실린 판은 저자가 편집부 요청에 응하지 않아 편집 요건을 채우지 못했다는 이유로 철회되었고[9], 2024년 판[8]에는 PubMed 기록상 철회 표시가 없다. 이 결과는 세포 실험이며 사람·동물 섭취 근거가 아니다.',
 '철회 사유를 [9] 원문대로 구체화하고 철회 대상(2020년 판)과 인용한 2024년 판을 구분; 세포 실험임을 밝힘')
rep('safety','이 종에서는 피롤리지딘 알칼로이드인 리코프사민·에키미딘·리토세닌·아세틸리토세닌 등이 보고되었고, 리코프사민과 에키미딘은 간독성이 알려져 있다[2].',
 '총설[2]은 이 종에서 피롤리지딘 알칼로이드인 리코프사민·에키미딘·리토세닌·아세틸리토세닌 등이 보고되었다고 정리했고, 그 가운데 리코프사민과 에키미딘은 간독성 때문에 독성·발암 가능성이 있다고 적었다[2]. 이 총설에는 함량 수치가 없다.',
 '2차 문헌(총설) 근거임과 함량 정보가 없음을 밝혀 과장 방지')
rep('safety','동결건조 추출물은 쥐에서 TSH와 갑상샘호르몬 수치를 낮추고 말초 T4 탈요오드화를 억제했다[12].',
 '쥐에 주사한 동결건조 추출물은 TSH와 갑상샘호르몬 수치를 낮추고 말초 T4 탈요오드화를 억제했다(동물 실험, 먹인 실험 아님)[12].',
 '[12] 초록은 TSH와 함께 투여·단독 주사(injected) — 경구 섭취 근거가 아님을 밝힘')
for c in d['compounds']:
    if c['name']=='Stearidonic acid':
        old=c['activity_ko']; c['activity_ko']='열매 지질 성분(열매는 사용가능 부위인 잎이 아님)'
        changes.append({"where":"compounds[Stearidonic acid].activity_ko","before":old,"after":c['activity_ko'],"why":"목록상 '지상부(잎 제외)'는 제한적사용 부위이므로 열매를 '식품 사용 부위 아님'으로 단정할 수 없음"})
a=d['assays'][0]
old=a['part']; a['part']=old.replace('지상부(새싹;','지상부(shoots;'); changes.append({"where":"assays[0].part","before":old,"after":a['part'],"why":"[3] 원문 shoots — 새싹 아님"})
old=a['rationale']; a['rationale']=old.replace('이 종 지상부의 주요 성분을 한 번에 정량한 유일한 전문 확인 연구다.','이 종 지상부의 주요 성분을 한 번에 정량했고 전문을 확인한 연구다.'); changes.append({"where":"assays[0].rationale","before":old,"after":a['rationale'],"why":"'유일한' 근거 없음"})
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
