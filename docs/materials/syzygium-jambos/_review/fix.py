import json,sys
p='/home/user/hfoodguide-wave3/docs/materials/syzygium-jambos/dossier.json'
d=json.load(open(p))
changes=[]
def rep(where,obj,key,old,new,why):
    s=obj[key]
    assert s.count(old)==1,(where,old)
    obj[key]=s.replace(old,new)
    changes.append({"where":where,"before":old,"after":new,"why":why})
S={s['key']:s for s in d['sections']}
rep('sections.biology',S['biology'],'body','이 때문에 하천에 떨어진 잎이 다른 수종보다 느리게 분해되었다[12]','이 때문에 하천에 떨어진 잎이 비교 수종(Dracontomelon duperreanum)보다 느리게 분해되었다[12]','[12] 는 한 수종하고만 비교함')
rep('sections.cultivation',S['cultivation'],'body','2006년 1월까지 섬 전역의 로즈애플 새잎에','2006년 1월까지 하와이주 전역의 로즈애플 새잎에','[3] 원문은 statewide(주 전역)')
rep('sections.cultivation',S['cultivation'],'body','하와이에서 2005년 처음 발견된 뒤','하와이에서 2005년 4월 오아후섬의 다른 기주(Metrosideros polymorpha)에서 처음 발견된 뒤','[3]: 첫 발견은 로즈애플이 아니라 화분의 Metrosideros polymorpha')
rep('sections.related_species',S['related_species'],'body',"자바플럼(S. cumini)은 잎·씨앗의 혈당 관련 민간 사용이 많아 로즈애플과 함께 'jambolan' 연구에 묶여 시험되기도 했다[25].","브라질 연구진은 자바플럼(S. cumini)과 로즈애플의 잎을 함께 'jambolan'으로 묶어 잎차·추출물의 혈당 강하 효과를 시험했다[25].","[25] 는 두 종의 잎을 jambolan 으로 묶어 시험했다고만 쓰고, 씨앗 민간 사용은 말하지 않음")
rep('sections.safety',S['safety'],'body','잎차를 건강한 사람에게 준 무작위 시험과 당뇨 환자 연구에서 혈당 강하 효과는 없었고','로즈애플 잎차를 건강한 사람에게 준 무작위 시험[24]과, 자바플럼 잎과 함께 \'jambolan\'으로 묶어 시험한 당뇨 환자 연구에서 혈당 강하 효과는 없었고','[25] 의 환자 연구는 S. cumini·S. jambos 잎을 묶은 jambolan 자료로, 로즈애플 단독 결과가 아님')
rep('sections.processing',S['processing'],'body','열매 총폴리페놀 31.24 mg/g,','열매 총폴리페놀 31.24 mg/g(초록에 생·건 기준 표기 없음),','[23] 초록은 함량 기준(생/건·추출물)을 밝히지 않음')
C={c['name']:c for c in d['compounds']}
c=C['Myricetin 3-O-beta-D-xylopyranosyl-(1->2)-alpha-L-rhamnopyranoside']
rep('compounds.Myricetin glycoside.activity_ko',c,'activity_ko','RAW 264.7 세포에서 TNF-α 생성 억제 IC50 1.11 µM, 쥐 5 mg/kg에서 염증 지표 감소(리뷰 인용)[2]','RAW 264.7 세포에서 TNF-α 생성 억제 IC50 1.11 µM, 설치류 5 mg/kg에서 TNF-α·CRP·피브리노겐 감소(리뷰 인용; 리뷰는 이 활성 연구의 성분을 자일로퓨라노실 배당체로 표기해 [15]의 분리 성분과 같은지 확인하지 못함)[2]','리뷰 [2] 는 활성 연구 성분을 xylofuranosyl 로 적고 murine model 이라고만 씀')
c=C['Quercetin 3-O-beta-D-xylopyranosyl-(1->2)-alpha-L-rhamnopyranoside']
rep('compounds.Quercetin glycoside.activity_ko',c,'activity_ko','RAW 264.7 세포에서 TNF-α 생성 억제 IC50 1.68 µM(리뷰 인용)[2]','RAW 264.7 세포에서 TNF-α 생성 억제 IC50 1.68 µM(리뷰 인용; 리뷰는 자일로퓨라노실 배당체로 표기)[2]','리뷰 [2] 표기 차이')
c=C['Gallic acid']
rep('compounds.Gallic acid.content_text',c,'content_text','잎 물 추출물에서 HPLC로 검출(수치는 그림에만 있음)[19]','잎 추출물(본문은 수성 추출물로 부르나 방법은 80% 에탄올 속슬렛 추출)에서 HPLC로 검출(수치는 그림에만 있음)[19]','[19] 방법 절: 80% 에탄올 속슬렛 추출')
c=C['Friedelin']
rep('compounds.Friedelin.activity_ko',c,'activity_ko','유도체 프리델로락톤이','반합성 유도체 프리델로락톤(Baeyer-Villiger 산화로 제조)이','[17]: 프리델로락톤은 분리 성분이 아니라 프리델린을 화학 변환한 것')
a=d['assays'][1]
rep('assays[Gallic acid].part',a,'part','잎(브라질산, 80% 에탄올 속슬렛 추출물)','잎(브라질산, 80% 에탄올 속슬렛 추출물; 본문은 수성 추출물로 지칭)','[19] 본문 표기 병기')
rep('assays[Gallic acid].rationale',a,'rationale','민간에서 쓰는 잎 우림액의 페놀 성분 지문 분석에 쓰인 조건','잎 추출물의 페놀 성분 지문 분석에 쓰인 조건(실제 시료는 우림액이 아니라 80% 에탄올 속슬렛 추출물)','[19] 시료는 우림액이 아님')
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('/home/user/hfoodguide-wave3/docs/materials/syzygium-jambos/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
