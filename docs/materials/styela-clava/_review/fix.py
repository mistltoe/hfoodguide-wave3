import json
p='dossier.json'; d=json.load(open(p))
S={s['key']:s for s in d['sections']}
ch=[]
def rep(key,a,b,why):
    s=S[key]; assert a in s['body'],(key,a); s['body']=s['body'].replace(a,b); ch.append({"where":"sections."+key,"before":a,"after":b,"why":why})
rep('processing','피낭은 대개 버려지지만 셀룰로스 원료로 연구되어, 나노결정 셀룰로스가 건조 피낭 기준 17% 수율, 결정화도 88.6%로 얻어졌다[4][24].',
 '피낭은 대개 버려지지만 나노결정 셀룰로스 원료로 연구되어 왔고[4][24], 스페인 침입 개체 피낭에서는 나노결정 셀룰로스가 건조 피낭 기준 17% 수율, 결정화도 88.6%로 얻어졌다[4].',
 '[24](Sci Rep 2020) 초록은 이 종 피낭에서 대량 분리 공정을 보고할 뿐 17%·88.6% 수치는 [4] 전문에만 있음')
rep('related_species','염기 서열이 87% 같고 아미노산 서열은 같았다[28]','호메오박스 영역의 염기 서열이 87% 같고 아미노산 서열은 같았다[28]',
 '[28] 초록은 유전자 전체가 아니라 호메오박스 영역 비교라고 씀')
rep('biology','N-아세틸화 당을 가진 글리코사미노글리칸 유사 다당과 황산화 갈락탄 유사 성분이 섞여 있는 것으로 분석되었다[4].',
 'N-아세틸화 당을 가진 글리코사미노글리칸 유사 다당이 확인되었고, 일부 잔기는 황산화 갈락탄일 가능성이 제시되었다(구조는 완전히 밝히지 못함)[4].',
 '[4] 는 황산화 갈락탄을 "possibly"로 추정만 했고 전체 구조를 결정하지 못했다고 씀')
rep('biology','스페인 갈리시아 연안 개체 14마리(겉면 정리 후 183.7 g)에서',
 '스페인 갈리시아 연안 침입 개체 14마리(봄 채집 224 g을 −20 °C 냉동 보관 후 해동, 겉면 부착물 정리 후 183.7 g)에서',
 '[4] 원문 시료 처리(냉동·해동·손질) 명시')
n=d['nutrients']
n[0]['form']='미더덕 속살(원문 internal organs·flesh) — 일반 성분(스페인 갈리시아 연안 침입 개체 14마리, 봄 채집, −20 °C 냉동 후 해동·손질, n=3, 평균값만 옮김)'
n[1]['form']='미더덕 피낭(겉껍질, 먹지 않는 부위) — 일반 성분(같은 시료; 원문 방법 순서상 아세톤 탈지·탈색 뒤 측정으로 읽힘, n=3, 평균값만 옮김)'
n[0]['basis']=n[1]['basis']='생것(습중량) 100 g 기준(원문 % of wet weight)'
ch.append({"where":"nutrients[0..1].form/basis","before":"속살(내장 포함)…/피낭 — 일반 성분(같은 시료)","after":"시료 처리(냉동·해동·손질, 피낭 아세톤 처리 순서)와 '% of wet weight' 기준 명시, 피낭은 먹지 않는 부위로 표시","why":"[4] 2.1절 원문 대조; 습중량 기준은 원문과 같음"})
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(ch,open('_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(ch))
