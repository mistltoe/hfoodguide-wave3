import json,re,sys
p=sys.argv[1]
d=json.load(open(p))
S={s['key']:s for s in d['sections']}
def rep(key,old,new):
    b=S[key]['body']; assert old in b,(key,old); S[key]['body']=b.replace(old,new)
rep('overview',"열매 색소에서 온 식품첨가물 '누리장나무색소'는 2009년 7월 10일 지정이 취소되어","같은 목록의 식품첨가물(B코드) '누리장나무색소'는 2009년 7월 10일 지정이 취소되어")
rep('history',"중국에서는 1960년대에 지상부 우려낸 물과 추출물의 독성과 혈압 강하 작용을 다룬 약리 논문이 나왔고, 도깨비바늘류(Bidens bipinnata)와 섞은 복합 처방 '진통(鎮痛)'의 소염 작용 연구도 발표되었다[33][34].",
 "중국에서는 1962년에 '취오동'(지상부)을 우려낸 물과 조추출물의 독성과 혈압 강하 작용을 다룬 약리 논문이 나왔다(초록이 없어 제목으로만 확인)[33].")
rep('history',"일본에서는 1964년 쓴맛 성분 연구를 시작으로 성분 분석이 이어졌고, 1970년에는 잎에서 아카세틴 배당체가 새로 보고되었다[38][26].",
 "1970년에는 잎에서 새 아카세틴 배당체(아카세틴-7-글루쿠로노-(1→2)-글루쿠로나이드)가 보고되었다[26].")
rep('history',"1994년 일본 연구에서는 추출물을 먹인 자연발생 고혈압 쥐의 혈압이 내려갔으나",
 "1994년 일본 연구에서는 추출물(초록에 사용 부위 명시 없음)을 한 번 먹인 자연발생 고혈압 쥐의 혈압이 내려갔으나")
rep('biology',"열매와 잎에는 N-아세틸갈락토사민·갈락토스에 붙는 렉틴(분자량 56,000의 당단백질 이량체)이 있어 적혈구 응집 연구에 쓰였다[27][28].",
 "열매와 잎에서 렉틴이 분리되었고, 열매 렉틴은 N-아세틸갈락토사민·갈락토스에 특이적으로 붙는 분자량 56,000의 당단백질 동종이량체로 혈구응집 시험에 쓰였다[27][28].")
rep('related_species',"학명에 함께 적힌 Clerodendrum fargesii는 누리장나무의 변종(var. fargesii)으로도 다뤄지며, 이 변종 잎에서 새 배당체가 보고된 바 있다[1][32][37].",
 "식약처 목록 학명에 함께 적힌 Clerodendrum fargesii는 누리장나무의 변종(var. fargesii (Dode) Rehder)으로도 다뤄지며, 아래 배양 연구에 쓰인 종자도 이 변종이었다[1][32].")
rep('processing',"총설에는 잎과 꽃으로 우린 차를 쥐에게 먹인 실험도 소개되어 있으나, 원문은 확인하지 못했다[2].",
 "총설에는 잎과 꽃으로 우린 차를 자연발생 고혈압 쥐에게 8주 먹인 실험도 소개되어 있으나, 원문은 확인하지 못했다[2].")
rep('safety',"세포 실험에서 시장 구입 원료(부위 미상) 열수 추출물의 50% 세포독성 농도는 764.17 μg/mL이었다[18].",
 "사람 HEp2 세포 실험에서 한약재 시장에서 산 원료(부위 미상)의 열수 추출물(105 °C, 2.5시간) 50% 세포독성 농도(CC50)는 764.17 μg/mL이었다[18].")
rep('safety',"열매·잎의 렉틴은 사람 적혈구를 응집시키는 성질이 있으나","열매·잎의 렉틴은 적혈구를 응집시키는 성질이 있으나")
rep('safety',"열매 색소에서 온 식품첨가물 '누리장나무색소'는 2009년 7월 10일 이후 사용불가다[1].","식품첨가물 '누리장나무색소'는 2009년 7월 10일 지정 취소 이후 사용불가다[1].")
rep('safety',"효능 연구는 세포·동물 수준이므로 질병 치료 목적으로 먹는 것은 권하지 않는다[2].",
 "효능 근거는 세포·동물 수준에 머물며, 총설은 사람에게 쓰기 전에 안전성·효능·용량 연구가 더 필요하다고 결론지었다[2].")
C={c['name']:c for c in d['compounds']}
a=C['Acteoside']
a['activity_ko']="세포(RBL-2H3)에서 cPLA2 경쟁적 억제(Ki 5.9 μM)[35]; HIV-1 인테그레이스 억제 IC50 7.8 ± 3.6 μM(효소 시험, 분리 부위는 초록에 없음)[9]; 줄기 분리물 ACE 억제 IC50 373 ± 9.3 μg/mL(시험관)[8]; 기니피그 천식 모델 25 mg/kg 기도저항 감소(동물; 누리장나무 잎과 Rumex 가운데 어느 쪽 분리물인지 초록으로 가리지 못함)[7]"
C['Isoacteoside']['activity_ko']="V79-4 세포에서 활성산소 소거·과산화수소 손상 보호(세포)[11]; B16F10 흑색종 세포 GI50 8 μM(세포; C. bungei 잎과 누리장나무 잎·껍질을 함께 조사한 연구)[14]"
for n in ('Jionoside D','Trichotomoside'):
    C[n]['part']="줄기(PubMed 색인어 기준, 초록에는 부위 명시 없음)"
C['Apigenin 7-glucuronide']['activity_ko']="쥐 역류성 식도염·위염 모델에서 십이지장 내 투여 시 위 병변 감소(동물)[13]; PPAR-γ 작용 활성(시험관 검정, 시료 부위는 초록에 없음)[24]"
u=C['Uncinatone']; u['source']=[22,36]
u['content_text']="뿌리 분리 다이터페노이드 가운데 가장 많은 성분 중 하나(정량값 없음; 초록 표기는 'uncintone')[36]"
s=d['assays'][1]
s['content']="배양 신초 아크테오사이드 24.4–28.3 mg/g 건조중량(WP·SH·B5 배지; 최고 SH 28.3 mg/g DW), 정량 폴리페놀 합 최고 36.6 mg/g DW(SH 배지); 두 종 모두 아크테오사이드가 정량 폴리페놀 합의 약 80%[32]. PMC 추출본에서 학명이 빠져 있어 본문 맥락(var. fargesii 종자·캄네오사이드 I 검출·SH 배지 최적)으로 누리장나무 값을 가려 읽었다(검토자 판단)"
s['rationale']="누리장나무 배양 신초에서 아크테오사이드가 가장 많은 폴리페놀이어서 정량 대상으로 쓰였다[32]. PMC 전문 Methods에서 조건을 옮겼고, 검출·정량한계와 회수율은 원문에 없었다. 야외 개체의 순·잎 값이 아니므로 식품 원료 함량으로 쓰면 안 된다."
# renumber
drop={23,34,37,38}
old=[x['n'] for x in d['sources']]
m={}; k=1
for n in old:
    if n in drop: continue
    m[n]=k; k+=1
def fix(t):
    if not isinstance(t,str): return t
    def r(mo):
        n=int(mo.group(1)); assert n not in drop,(n,t); return f"[{m[n]}]"
    return re.sub(r"\[(\d+)\]",r,t)
for sct in d['sections']: sct['body']=fix(sct['body'])
for arr in ('compounds','assays'):
    for x in d[arr]:
        for f in list(x):
            if isinstance(x[f],str): x[f]=fix(x[f])
        x['source']=[m[n] for n in x['source'] if n not in drop]
d['sources']=[dict(x,n=m[x['n']]) for x in d['sources'] if x['n'] not in drop]
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
print(len(d['sources']))
