import json,re,sys
p=sys.argv[1]
d=json.load(open(p,encoding='utf-8'))
S={s['key']:s for s in d['sections']}
def rep(key,old,new):
    b=S[key]['body']; assert old in b,(key,old[:40]); S[key]['body']=b.replace(old,new)
rep('overview',"다른 이름은 쇠무릎풀·우슬, 영문명은 Oriental chaff flower다[1].",
 "다른 이름은 쇠무릎풀(뿌리 원료 행에는 쇠무릎풀, 우슬), 영문명은 Oriental chaff flower다[1].")
rep('history',"'Useul-puli(우슬풀)'라고 부르는 뿌리를 달여 무릎 골관절염의 통증을 다스리는 데 써 왔다는 기록도 있다[19].",
 "'Useul-puli(우슬풀)'라고 부르는 뿌리는 골관절염 환자의 통증 조절과 기능 개선에 전통적으로 쓰여 왔다고 기술되었다[19].")
rep('biology',"질소를 더 주면 지상부와 지하부 무게가 늘었고, 4마디 단계에서 잘라도 다시 자라 콩과의 경쟁력이 높게 평가되었다[6].",
 "질소를 더 주면 지상부 무게가 늘었고, 4마디 단계에서 땅 높이로 잘라 낸 개체는 다시 자라 콩에 대한 경쟁 효과가 Palmer amaranth와 같은 수준으로 평가되었다[6].")
rep('cultivation',"질소 시비에 지상부·지하부 생장이 늘었다[6].","질소 시비에 지상부 생장이 늘었다[6].")
rep('safety',"복합원료 행에는 쇠무릅 뿌리가 '식품공전상 식품에 제한적으로 사용할 수 있는 원료로 등재'되어 있다고 적혀 있다[2]. 식품공전은 이런 원료에 별도 조건이 없으면 가공 전 원료 중량 기준 50% 미만으로 쓰게 한다(검색 요약으로만 확인, 원문 확인하지 못함)[3].",
 "뿌리 원료 9개의 사용 조건은 모두 '제한적사용가능부위 : 뿌리※(우슬)'이고, 줄기·잎 원료 4개는 '사용가능부위 : 줄기, 잎'이다[1]. 복합원료 쇠무릅창출분말 행의 조건에는 '쇠무릅(우슬) 사용가능부위 : 잎, 줄기 / 제한적사용부위 : 뿌리'와 함께 '식품공전상 식품에 제한적으로 사용할 수 있는 원료로 등재'라는 문구가 적혀 있다[2]. 제한적사용 원료의 배합 한도 등 식품공전상 구체적 사용 조건은 원문을 열지 못해 확인하지 못함.")
rep('safety',"급성 간질성 신염이 생겨 혈청 크레아티닌이 3.2 mg/dL까지 올랐고, 중단 13개월 뒤 거의 회복되었다(인과성 '가능성 높음')[18].",
 "급성 간질성 신염이 생겨 입원 당시 혈청 크레아티닌이 3.2 mg/dL였고, 중단 13개월 뒤 신기능이 거의 회복되었다(Naranjo·WHO-UMC 인과성 '가능성 높음')[18].")
rep('safety',"두충·쇠무릅 3:1 추출 복합물 500 mg/일을 8주 먹은 무작위 시험(48명)에서 이상사례는 없었다[22].",
 "두충·쇠무릅 3:1 30% 에탄올 추출 복합물 500 mg/일을 8주 먹은 무작위 위약대조 시험(96명, 군당 48명)에서 이상사례는 없었다[22].")
# compounds / assays basis
c=d['compounds'][0]
c['content_text']=c['content_text'].replace("쇠무릅 에탄올 추출물 307.59 ± 4.18 mg/100g(HPLC, n=3)[12]","쇠무릅 99% 에탄올 건조 추출물 기준 307.59 ± 4.18 mg/100g(HPLC, n=3)[12]")
a=d['assays'][0]; a['content']="추출물 기준 307.59 ± 4.18 mg/100g(n=3), 머무름 시간 28.36분[12]"
a=d['assays'][2]
a['method']="HPLC-UV"
a['conditions'].update({"column":"YMC J'sphere ODS C18(250 × 4.6 mm, 4 μm)","mobile_phase":"0.1% 포름산 수용액 : 아세토니트릴 = 85:15(v/v)","gradient":"등용리(isocratic)","flow":"1.0 mL/min","detection":"UV 245 nm"})
a['rationale']="우슬의 품질관리와 기원 판별을 위해 엑디스테로이드 3종을 정량하고 두 기원종 시료로 패턴 인식 분석을 검증했다; 분석 조건은 초록 기재 값이며 시료 처리·검출한계는 전문을 보지 못해 확인하지 못함[8]"
# drop source 3, renumber
old2new={}
new=[]
for s in d['sources']:
    if s['n']==3: continue
    old2new[s['n']]=len(new)+1; s['n']=len(new)+1; new.append(s)
d['sources']=new
def renum_text(t):
    if not t: return t
    def f(m):
        nums=[int(x) for x in re.split(r"\s*,\s*",m.group(1))]
        return "["+", ".join(str(old2new[n]) for n in nums)+"]"
    return re.sub(r"\[(\d+(?:\s*,\s*\d+)*)\]",f,t)
for s in d['sections']: s['body']=renum_text(s['body'])
for arr in ('compounds','markers','assays','nutrients','production','world','gi','orgs'):
    for x in d.get(arr) or []:
        if 'source' in x: x['source']=[old2new[n] for n in x['source']]
        for k,v in list(x.items()):
            if isinstance(v,str): x[k]=renum_text(v)
json.dump(d,open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('ok')
