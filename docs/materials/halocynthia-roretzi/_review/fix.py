import json,re,sys
p=sys.argv[1]; d=json.load(open(p)); ch=[]
S={s['key']:s for s in d['sections']}
def rep(key,a,b,why):
    s=S[key]; assert a in s['body'],(key,a); s['body']=s['body'].replace(a,b); ch.append({"where":f"sections.{key}","before":a,"after":b,"why":why})
rep('overview','멍게과(Pyuridae)에 속한다[1][4].','멍게과(Pyuridae)에 속한다[4].','[1] 식품원료 목록(I1020) 행에는 분류군(과·문) 정보가 없음; 분류는 [4] 서론에만 있음')
rep('biology','알이 크고 다루기 쉬워 발생 중 유전자 발현 조절을 보는 실험 동물로 쓰인다[32].','발생 중 조직 특이적 유전자 발현 조절을 보는 형질전환 실험에 알맞은 모델 동물로 소개된다[32].','[32] 초록은 "알이 크다"는 이유를 말하지 않음; 원문 표현(형질전환 분석의 좋은 모델)으로 맞춤')
rep('related_species','다가불포화지방산이 풍부한 글리세로인지질은 주로 겉껍질이 아닌 속 조직에 있었다[31].','다가불포화지방산이 풍부한 글리세로인지질은 세 종에서 주로 속 조직(inner body tissues)에 있었다[31].','[31] 초록은 세 종 공통 결과로 씀; 이 종만의 값으로 읽히지 않게 함')
rep('cultivation','찢어져 죽는 병으로, 한국과 일본의 양식에 큰 피해를 준다[15].','찢어져 죽는 병으로, 한국과 일본의 양식에 큰 피해를 준다[10][15].','"얇아지다"는 [10] 초록 표현([15]은 softens·tears만 말함)')
rep('safety','플라스말로젠 식품의 사람 시험은 소규모 단기 연구이며[7][8],','플라스말로젠 식품의 사람 시험은 가벼운 건망을 느끼는 일본 성인 49명의 12주 시험[7]과 참치 엘라스틴을 함께 넣은 복합 제품으로 고령자(분석 123명)에게 16주 준 시험[8]이어서 이 종 성분만의 효과로 일반화하기 어렵고[7][8],','[8] 은 123명·16주 시험이고 참치 엘라스틴 복합 제품이라 "소규모 단기"·단일 성분 효과로 읽히면 과장')
for c in d['compounds']:
    if c['name']=='Plasmenylethanolamine':
        a=c['activity_ko']; b='이 종 유래 플라스말로젠 1 mg을 12주 먹은 가벼운 건망 자각 일본 성인군(25명)에서 복합 기억 점수 변화가 위약군(24명)보다 컸다(소규모 시험)[7]'
        c['activity_ko']=b; ch.append({"where":"compounds.Plasmenylethanolamine.activity_ko","before":a,"after":b,"why":"[7] 대상자는 건강한 일반 성인이 아니라 mild forgetfulness 자각 성인 49명"})
a0=d['assays'][0]['conditions']; a=a0['sample_prep']
a0['sample_prep']=a.replace('ODS 분취 HPLC(CH2Cl2:CH3CN 1:9, 2.0 mL/min)','ODS 분취 HPLC(염소계 용매:CH3CN 1:9, v/v, 2.0 mL/min; PMC 텍스트에서 아래첨자가 빠져 CHCl3/CH2Cl2 구별 불가)')
assert a!=a0['sample_prep']; ch.append({"where":"assays[0].conditions.sample_prep","before":"CH2Cl2:CH3CN 1:9","after":"염소계 용매:CH3CN 1:9(CHCl3/CH2Cl2 구별 불가)","why":"PMC 전문 텍스트는 'CHCl:CHCN'으로만 보여 용매를 단정할 수 없음"})
a1=d['assays'][1]['conditions']; ch.append({"where":"assays[1].conditions.recovery","before":a1['recovery'],"after":"","why":"원문 'Averages of triplicate injections were reported'는 회수율이 아님; 회수율은 원문에 없어 지움(반복 주입 사실은 sample_prep 끝에 옮김)"})
a1['recovery']=""; a1['sample_prep']+='; 3회 주입 평균값 보고'
for s in d['sources']:
    if s['n']==11:
        a=s['title']; s['title']=a.replace('using real-time PCR','using real-time polymerase chain reaction'); ch.append({"where":"sources[11].title","before":a,"after":s['title'],"why":"PubMed(PMID 25425505) 원 제목과 맞춤"})
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(ch,open(sys.argv[2],'w'),ensure_ascii=False,indent=1)
print(len(ch))
