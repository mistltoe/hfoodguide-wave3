import json,re,sys
P='/home/user/hfoodguide-wave3/docs/materials/dianthus-caryophyllus/'
d=json.load(open(P+'dossier.json'))
changes=[]
def sec(k): return next(s for s in d['sections'] if s['key']==k)
def rep(k,old,new,why):
    s=sec(k); assert old in s['body'],(k,old[:40]); s['body']=s['body'].replace(old,new)
    changes.append({"where":f"sections.{k}","before":old,"after":new,"why":why})
d['aliases'].remove('향석죽(香石竹)')
changes.append({"where":"aliases","before":"향석죽(香石竹)","after":"(삭제)","why":"[4]는 중국명 Xiāng shízhú 만 제시, 국문 별명 '향석죽'의 출처 없음"})
rep('overview','세계적으로 장미 다음가는 인기 절화로 꼽힌다[2][4]','세계적으로 장미 다음으로 인기 있는 관상용 꽃으로 꼽힌다[2][4]','[4] 원문은 절화가 아니라 관상용 꽃(ornamental flowers) 인기 순위로 씀')
rep('overview','건강기능식품 고시형 원료의 원재료로 쓰인다는 기록은 확인하지 못함.','건강기능식품 기능성 원료 고시(제2026-43호) 원문에서 카네이션을 원재료로 하는 고시형 원료는 확인하지 못함.','refs/MFDS 고시 원문에 카네이션·Dianthus 없음을 확인, card.json lists 에도 KR_NOTICE 없음')
rep('overview','중국에서 기른 카네이션의 부위별 70% 메탄올 추출물에서 꽃의 총페놀(7.573 mg/g)과 총플라보노이드(4.616 mg/g)가 뿌리·줄기·잎보다 많았다[2].','중국 윈난성 쿤밍에서 기른 카네이션을 부위별로 동결건조해 70% 메탄올로 추출한 연구에서 꽃의 총페놀(7.573 mg/g)과 총플라보노이드(4.616 mg/g)가 뿌리·줄기·잎보다 많았다(건조 시료 기준, 표준물질 환산 표기는 원문에서 확인하지 못함)[2].','[2] 전문: 시료는 동결건조 분말, 단위는 mg/g 로만 표기 — 기준(건조) 명시')
rep('history','꽃잎은 쓴맛이 있고 꽃잎 밑부분에서 더 강하다[22].','이 속의 꽃잎은 쓴맛이 있고 꽃잎 밑부분에서 더 강하다고 한다[22].','[22] 는 Dianthus spp. 일반에 대한 서술(연구 대상 종명이 본문에서 빠져 있음) — 카네이션 단정 피함')
rep('biology','유전체 크기는 k-mer 분석으로 약 622 Mb, 다른 품종에서는 약 640 Mb로 추정되었다[4][5].',"유전체 크기는 'Francesco' 품종에서 k-mer 분석으로 약 622 Mb[5], 'Scarlet Queen' 품종에서 k-mer 분석과 유세포 분석으로 약 640 Mb로 추정되었다[4].",'622 Mb 는 [5], 640 Mb 는 [4](k-mer+유세포 분석) — 출처·품종 짝을 맞춤')
old=sec('related_species')['body'].split('\n\n')[1]
new="패랭이꽃속 야생종 한 종(초록에서 종명이 빠져 있어 확인하지 못함)의 유전체는 876 Mb(2n = 2x = 30)로 조립되었고 전이인자가 82.4%를 차지했으며, 비교 대상인 재배 카네이션은 꽃 향이 약하다[24]. 이 야생종 안에서도 향이 진한 서부 계통과 약한 동부 계통이 갈렸고, 테르펜 합성 유전자의 변이가 향 차이와 관련된다고 보고되었다[24]."
rep('related_species',old,new,'[24] 초록: 876 Mb·82.4% 는 야생종(종명 미확인) 유전체, 향 강약은 그 야생종의 서부·동부 계통 차이 — 원문은 \'향이 진한 야생 카네이션 계통\'으로 뭉뚱그림')
rep('related_species','같은 석죽과의 비누풀(Saponaria) 종자에서 나오는 사포린은 카네이션의 리보솜 불활성화 단백질 디안틴과 구조가 매우 비슷하다[19].','같은 석죽과 비누풀(Saponaria)의 리보솜 불활성화 단백질 사포린(S3·S6)은 카네이션의 디안틴-30과 구조가 매우 비슷하다[19].','[19] 초록은 디안틴-30과 사포린-S3·S6의 유사성만 말하고 \'종자\'는 언급 없음')
rep('cultivation','국내 카네이션 재배면적은 2003년 전국 111.7 ha, 그중 경상남도 57.3 ha였다는 김해시 자료가 있다(WebSearch 요약으로만 확인)[30]. 최근 연도의 품목별 재배면적·생산액은 공식 통계 원문을 열지 못해 확인하지 못함.','국내 카네이션 재배면적·생산액은 공식 통계 원문을 열지 못해 확인하지 못함.','[30] 김해시 누리집은 WebSearch 요약뿐이고 원문이 네트워크 허용 목록 밖이라 열 수 없음 — 2003년 수치 근거 부족으로 삭제')
rep('processing','꽃잎은 쓴맛이 있고 꽃잎 밑부분에서 더 강하다[22].','패랭이꽃속 꽃잎은 쓴맛이 있고 밑부분에서 더 강하다고 한다[22].','[22] 는 속 수준 서술')
rep('processing','연구에서는 얼려 말린 꽃가루를 70% 메탄올로 추출해 성분과 항산화 활성을 비교했다[2][3].','연구에서는 꽃(부위별 비교에서는 뿌리·줄기·잎도)을 동결건조해 분말로 간 뒤 70% 메탄올로 추출해 성분과 항산화 활성을 비교했다[2][3].',"'꽃가루'는 화분(pollen)으로 읽힘 — 원문은 동결건조 분말(lyophilized powder)")
rep('processing','꽃 20 kg을 95% 에탄올에 담가 추출한 뒤 칼럼 크로마토그래피로','생꽃 20 kg을 두 배 부피의 95% 에탄올에 세 차례(7·5·2일) 냉침 추출한 뒤 칼럼 크로마토그래피로','[2] 전문: fresh flowers 20 kg, 2배 부피 95% EtOH 3회 냉침')
rep('processing','카네이션 정유의 주성분으로 β-카리오필렌·유제놀 등이 보고되었고, 이 정유는 모기 유충에 중간 정도의 살충 활성(LC50 50 mg/L 초과)을 보였다[21].','카네이션 정유는 모기 유충에 중간 정도의 살충 활성(LC50 50 mg/L 초과)을 보였다[21]. 이 연구는 네 가지 정유의 주성분으로 β-카리오필렌·유제놀·유칼립톨·α-테르피닐 아세테이트·(E)-아네톨을 들었으나, 어느 성분이 카네이션 정유의 것인지는 초록에서 확인하지 못함[21].','[21] 초록은 네 정유를 묶어 주성분을 나열 — 카네이션 정유 주성분으로 단정 불가')
rep('safety','한 꽃 도매업자는 카네이션 피부 단자 시험과 문지름 시험에서 양성을 보였고','한 꽃 공급업자는 즉시형 피부단자시험이 양성이었고 카네이션·안개꽃 문지름 시험에서도 양성을 보였으며','[16] 초록: 단자시험은 식물별 구분 없이 양성, 문지름 시험이 안개꽃·카네이션 양성; flower supplier')
rep('related_species','꽃 도매업자의 직업성 알레르기 사례','꽃 공급업자의 직업성 알레르기 사례','[16] flower supplier')
C={c['name']:c for c in d['compounds']}
c=C['Eugenol']; b=c['content_text']; c['content_text']="'Lorca' 꽃: S4 0.00708 → S5 0.02596 → S6 0.04247 mmol/g(꽃 발달 단계별, 기준 무게는 본문에서 확인하지 못함)[4]"
c['activity_ko']="카네이션 특유의 매운 향을 내는 주성분[4]; 순수 성분으로 모기 유충 LC50 18.28 mg/L[21]"
changes.append({"where":"compounds.Eugenol","before":b,"after":c['content_text'],"why":"[21] 초록은 카네이션 정유의 주성분을 따로 밝히지 않음"})
c=C['beta-Caryophyllene']; b=c['content_text']; c['content_text']="꽃 향 3대 주성분 가운데 하나[4]; 네 가지 정유의 주성분 목록에 들어 있으나 카네이션 정유의 성분인지는 초록에서 확인하지 못함[21]"
c['activity_ko']="순수 성분으로 모기 유충에 100 mg/L에서도 활성이 없었음[21]"
changes.append({"where":"compounds.beta-Caryophyllene","before":b,"after":c['content_text'],"why":"[21] 주성분 귀속 불명"})
c=C["Apigenin 6-C-glucosyl-7-O-glucoside 6'''-malyl ester"]; b=c['content_text']
c['content_text']="유전자 재조합 보라색 카네이션(Moonshadow 등) 꽃잎에서 구조 동정(정량값 없음)[11]"; c['source']=[11]; c['role']='bioactive'
changes.append({"where":"compounds.Apigenin malyl ester","before":b,"after":c['content_text']+" (role marker→bioactive)","why":"[7] 의 플라본 C-배당체가 이 성분인지 초록에서 알 수 없어 다른 연구를 섞은 것 — 분리; 재조합 꽃에서만 동정돼 지표성분(marker)으로 볼 근거 없음"})
a=d['assays'][0]; cd=a['conditions']
b=cd['standard']; cd['standard']="Metware MVDB V3.0 데이터베이스 기반 동정·상대 정량(표준품 검량선 없음)"
changes.append({"where":"assays[0].conditions.standard","before":b,"after":cd['standard'],"why":"[3] 원문 표기는 MVDB V3.0"})
b=cd['sample_prep']; cd['sample_prep']="꽃잎 액체질소 동결·−70 °C 보관 → 진공 동결건조 → 30 Hz 1.5분 분쇄 → 가루 100 mg + 70% 메탄올 1.2 mL, 30분마다 30초씩 6회 볼텍스, 4 °C 하룻밤 → 12,000 rpm 10분 원심 후 여과"
changes.append({"where":"assays[0].conditions.sample_prep","before":b,"after":cd['sample_prep'],"why":"[3] 원문 −70 °C 보관 단계 보완"})
b=a['rationale']; a['rationale']="보라색 꽃의 강한 항산화·항암 활성과 상관이 큰 주요 성분 가운데 하나로 골라졌다(상관 분석, 시험관)[3]. 표준품 검량선이 없는 상대 정량이라 직선성·검출한계·회수율은 없다. 부위별(뿌리·줄기·잎·꽃) 비교 연구도 같은 기종(Nexera X2 + 4500 QTRAP)으로 분석했다[2]."
changes.append({"where":"assays[0].rationale","before":b,"after":a['rationale'],"why":"[3] 은 네 성분을 함께 주요 기여 성분으로 듦(항암 상관은 2′-데옥시구아노신이 가장 큼) — '가장 상관이 큰' 과장; '같은 연구실'은 확인 안 됨"})
# production
b=json.dumps(d['production'],ensure_ascii=False)
d['production']=[]
changes.append({"where":"production","before":"2003 대한민국 111.7 ha, 경상남도 57.3 ha [30]","after":"(삭제)","why":"WebSearch 요약만 있고 김해시 원문은 네트워크 허용 목록 밖이라 대조 불가 — V2 규칙(확인할 수 없으면 지운다)"})
# sources renumber
d['sources']=[s for s in d['sources'] if s['n']!=30]
mp={s['n']:i+1 for i,s in enumerate(d['sources'])}
for s in d['sources']: s['n']=mp[s['n']]
def rn(t): return re.sub(r'\[(\d+)\]',lambda m:'[%d]'%mp[int(m.group(1))],t)
for s in d['sections']: s['body']=rn(s['body'])
for arr in ('compounds','assays','markers','nutrients','production','world','gi','orgs'):
    for x in d.get(arr,[]):
        for k,v in list(x.items()):
            if isinstance(v,str): x[k]=rn(v)
        if 'source' in x: x['source']=[mp[n] for n in x['source']]
for ch in changes:
    ch['after']=rn(ch['after'])
json.dump(d,open(P+'dossier.json','w'),ensure_ascii=False,indent=1)
json.dump(changes,open(P+'_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes),mp)
