import json,re
p='dossier.json'
d=json.load(open(p))
S={s['key']:s for s in d['sections']}
changes=[]
def rep(key,old,new,why):
    b=S[key]['body']
    assert old in b,(key,old)
    S[key]['body']=b.replace(old,new)
    changes.append({"where":f"sections.{key}","before":old,"after":new,"why":why})

rep('overview',"기름이 많은 등푸른 생선답게 얼음 보관 중 지질 산화 냄새 성분이 빨리 늘어난다[19]",
 "얼음 보관 중 휘발 성분이 정어리·고등어와 함께 빨리 늘어나는 어종으로 분류되었다[19]",
 "[19] 초록은 '기름이 많다'는 설명 없이 정어리·고등어와 함께 증가가 빠른 어종으로만 분류")
rep('overview',"한국에서 많이 먹는 생선 19종의 생체아민 조사에서는 'Japanese jack mackerel' 등 일부 어종의 생체아민 노출량이 일부 국가 기준을 넘었다[27].",
 "한국에서 많이 먹는 생선 19종의 생체아민 조사에서는 영문명 'Japanese jack mackerel'로 적힌 어종 등 일부의 노출량이 일부 국가 기준을 넘었으나, 초록에는 학명과 이 어종의 수치가 없다[27].",
 "[27] 초록에 학명이 없어 이 종으로 단정하지 않도록 한정")
rep('history',"이 글은 학명이 T. japonicus로 밝혀진 자료만 근거로 삼았다[1].",
 "이 글은 학명이 T. japonicus로 밝혀진 자료를 주 근거로 삼고, 학명이 적히지 않은 자료는 그 점을 밝혔다[1].",
 "[27]·[33] 초록에는 학명이 없으므로 '학명 확인 자료만'이라는 서술은 사실과 다름")
rep('history',"2010년에는 나가사키 앞바다 전갱이 근육의 포자충이 Kudoa trachuri라는 새 종으로 기재되었다[30].",
 "2010년 발표 논문에서는 나가사키 앞 일본해에서 잡혀 야마구치 시장에서 구한 전갱이 2마리 근육의 포자충이 Kudoa trachuri라는 새 종으로 기재되었다[30].",
 "[30] 초록: 야마구치 시장 시료, 나가사키 앞 일본해 어획, 2마리")
rep('biology'," 치어는 표준체장 약 51.7 mm에서 학습 능력이 크게 늘었는데, 이 크기는 먼바다에서 연안 암초로 옮겨 오는 크기와 맞았다[6]. 세토내해에서는 치어가 해파리에 붙어 다니는 모습이 관찰되었다[7].","",
 "출처 정리: 식품 소재와 관련이 약한 행동학[6]·해파리 기생충 연구[7] 문장 삭제")
rep('related_species',"전갱이와 가라지류가 함께 주요 소형 부어류로 조사되었다[10].",
 "강한 엘니뇨·라니냐 때 전갱이와 가라지(Decapterus maruadsi)가 가장 크게 영향받은 소형 부어류였으며, 두 종은 따로 분석되었다[10].",
 "[10] 초록: Japanese jack mackerel·Japanese scad 두 종이 가장 영향받음 — 가라지 학명 명시")
rep('cultivation',"2006–2020년 저층 트롤 자료로 본 베이부만 소형 부어류 2종(전갱이 포함)은 2006–2010년에 남획 상태였다가 2011년 이후 적정 이용 수준으로 바뀌었으나, 평균 체장과 점근 체장은 줄었다[9]. 강한 엘니뇨·라니냐 때 이 해역의 전갱이 분포와 양이 크게 흔들렸다[10]. 일본 고치현 스즈 연안에서는 구로시오 대사행 시기에 정치망의 전갱이 어획이 훨씬 많았다[11].",
 "2006–2020년 저층 트롤 자료로 본 베이부만 상업 소형 부어류 2종(전갱이 포함)은 2006–2010년에 남획 상태였다가 2011년 이후 적정 이용 수준으로 바뀌었으나 평균 체장과 점근 체장은 줄었는데, 초록은 두 종을 묶어 요약했으므로 전갱이만의 값은 아니다[9]. 강한 엘니뇨·라니냐 때 이 해역의 전갱이 분포와 양이 크게 흔들렸다[10].",
 "[9] 결과는 두 종 묶음 요약임을 밝힘; 출처 정리로 [11] 문장 삭제")
rep('cultivation'," 쿠로시오 확장역에서는 종 특이 qPCR이 메타바코딩보다 전갱이 등 소형 부어류를 더 자주 검출했다[13].","",
 "출처 정리: 6종 합산 방법 비교 연구[13] 삭제")
rep('cultivation',"병든 양식 전갱이에서 새 병원 세균을 기재한 연구[35]가 있고, 작은 전갱이를 대리모로 써서 방어 정자를 만든 실험도 있었다[16].",
 "병든 양식 전갱이에서 새 비브리오 세균을 기재한 연구[35]가 있다[29, 35].",
 "출처 정리: 방어 생식세포 이식 실험[16] 삭제")
rep('processing'," 가나식 발효 건어물을 전갱이로 만들어 산화 방지제 효과를 비교한 연구도 있다[36].","",
 "출처 정리: 1998년 학회 단행본[36] 삭제")
rep('processing',"전갱이 단백질 서열에서 컴퓨터로 고른 뒤 합성한 펩타이드 4종이 세포 실험에서 요산을 낮췄으나, 이는 사람 효과의 근거가 아니다[25].",
 "전갱이 단백질 서열에서 컴퓨터로 고른 뒤 합성한 펩타이드 4종은 시험관에서 수십 mM 농도가 되어야 잔틴산화효소를 절반 억제했고 신장 세포 실험에서 요산을 낮췄으나, 동물·사람 시험은 없어 사람 효과의 근거가 아니다[25].",
 "[25] 전문: IC50 38–108 mM, 세포 실험만 — 효과 크기 한정")
rep('genetics',"쓰인다[12, 13].","쓰인다[12, 37].","[13] 삭제에 따른 번호 조정([12]·[37] 모두 종 특이 qPCR 사용)")
rep('genetics',"어시장에서 흘러든 DNA가 오차 원인으로 드러났다[37].","어시장에서 흘러든 DNA가 외부 유입원으로 확인되었다[12, 37].",
 "[37] 초록 표현(외부 eDNA 유입원 식별)에 맞추고 [12]도 같은 점을 보고")
rep('safety',"한국에서 흔히 먹는 생선 19종 609건의 생체아민 조사에서 'Japanese jack mackerel' 등 일부 어종의 노출량이 외국 기준을 넘었다[27]. 이 종의 히스타민 수치와 국내 기준 대비 결과는 원문 수치로 확인하지 못함.",
 "한국에서 흔히 먹는 생선 19종 609건의 생체아민 조사에서 영문명 'Japanese jack mackerel'로 적힌 어종 등 일부의 1회 섭취 노출량이 일부 나라 기준을 넘었다[27]. 초록에는 시료 학명과 이 어종의 히스타민 수치가 없어, 이 종의 히스타민 수치와 국내 기준 대비 결과는 확인하지 못함[27].",
 "[27] 학명 미기재 — 이 종으로 단정하지 않음")
rep('safety',"상온 보관에서는 Shewanella 속 세균이 우세해지며 부패가 진행되었다[26].",
 "20 ℃와 4 ℃ 보관 모두에서 Shewanella 속이 우세해졌고, 휘발성 염기질소는 20 ℃에서만 크게 늘었다[26].",
 "[26] 전문: Shewanella 우세는 온도와 무관, TVB-N 증가는 20 ℃에서만")
rep('safety',"전갱이 9마리 모두에서 고래회충류(Anisakis simplex) 유충이 나왔고",
 "전갱이 9마리 모두에서 고래회충(Anisakis simplex) 유충이 나왔고",
 "[32] 초록은 종(A. simplex)으로 적음")
rep('safety',"생후 13개월 아이가 전갱이 알레르기로 진단되었다가 16개월 뒤 내성이 생긴 사례가 있다[33].",
 "생후 13개월 아이가 볼락류(rosefish)와 'Japanese jack mackerel' 알레르기로 진단되었다가 16개월 뒤 경구 유발 시험에서 내성이 확인된 일본 사례 보고가 있다(초록 키워드 Trachurus)[33].",
 "[33] 두 어종 알레르기였고 내성은 경구 유발 시험으로 확인 — 학명은 초록에서 빠져 키워드로만 확인")

# compounds
C={c['name']:c for c in d['compounds']}
def cset(name,field,new,why):
    old=C[name][field]; C[name][field]=new
    changes.append({"where":f"compounds[{name}].{field}","before":old,"after":new,"why":why})
cset('Retinol','content_text',"평균 7,700 ± 3,550 μg/kg 건물(범위 3,970–15,210 μg/kg 건물; 시료 건물 함량 29.1 ± 2.8%) — 건물 기준값이며 생물(날것) 기준값은 원문에 없음[17]",
 "[17] 전문: 값은 dry weight 기준 — 생/건 기준 명시")
cset('3,4-Didehydroretinol','content_text',"평균 1,410 ± 430 μg/kg 건물(범위 770–2,260 μg/kg 건물), 비타민 A1의 약 5분의 1 — 건물 기준[17]",
 "건물 기준 명시")
cset('Histamine','name_ko',"생체아민(히스타민 등)","[27] 초록은 히스타민만이 아니라 생체아민 전체 노출을 말함")
cset('Histamine','part',"한국 유통 생선 시료('Japanese jack mackerel' 표기, 학명 미기재)","[27] 학명 미기재")
cset('Histamine','content_text',"'Japanese jack mackerel' 등 일부 어종의 생체아민 노출이 일부 나라 기준을 넘음 — 초록에 학명·이 어종 히스타민 수치 없음[27]","학명 미기재·수치 없음 명시")
cset('Trimethylamine N-oxide','content_text',"20 ℃ 보관 24–48시간 사이 휘발성 염기질소 급증, 4 ℃ 168시간은 거의 변화 없음(수치는 그림에만 있음); 분리 균주는 배지에서는 TMAO를 환원했으나 신선 근육에서는 휘발성 염기질소를 만들지 않았다[26]",
 "[26] 전문: 분리 균주 NFH-SH190041은 신선 근육에서 TVB-N을 만들지 못함 — '부패균이 TMAO를 환원해 만든다'는 단정 완화")
cset('Gln-Pro-Ser-Phe','activity_ko',"HK-2 세포 고요산 모델에서 요산을 48.61% 낮춤(결과 절은 4 mM, 방법 절은 2 mM으로 적어 원문 안에서 어긋남; 알로푸리놀 0.1 mM은 52.25%) — 세포 실험일 뿐 사람 효과 근거 아님[25]",
 "[25] 전문 대조: 농도 표기 불일치와 대조약 수치 추가")

# assays
for a in d['assays']:
    if a['source']==[26]:
        old=a['conditions']['sample_prep']
        a['conditions']['sample_prep']="부위별 시료에 완충 식염수 9배 가해 균질화 → 다시 5배 희석해 콘웨이 외실에 넣고 포화 칼륨염 용액 1 mL 첨가(열람본에서 화학식 판독 불가), 내실에는 5 mM H2SO4 1 mL"
        changes.append({"where":"assays[TVB-N].conditions.sample_prep","before":old,"after":a['conditions']['sample_prep'],"why":"PMC 열람본에서 'K2CO3' 확인 불가(첨자 소실로 다른 염일 가능성)"})
        old=a['part']; a['part']="가나가와현 슈퍼마켓 3곳에서 2017–2018년 산 전갱이 42마리(길이 18.0–23.7 cm, 무게 119.1–260.6 g)의 가슴지느러미–항문 사이 절편의 껍질·근육·내장"
        changes.append({"where":"assays[TVB-N].part","before":old,"after":a['part'],"why":"[26] 전문 2.1 대조 — 구입처·기간·무게 보충"})
    if a['source']==[27]:
        old=a['part']; a['part']="한국 유통 생선 19종 609건 중 'Japanese jack mackerel'로 표기된 시료(초록에 학명 없음)"
        changes.append({"where":"assays[biogenic amines].part","before":old,"after":a['part'],"why":"학명 미기재"})
        old=a['content']; a['content']="일부 어종('Japanese jack mackerel' 포함)의 생체아민 노출량이 일부 나라 기준 초과(이 어종 수치는 초록에 없음)[27]"
        changes.append({"where":"assays[biogenic amines].content","before":old,"after":a['content'],"why":"'전갱이 포함' 단정 완화"})

# sources: remove and renumber
remove={6,7,11,13,16,36}
for s in d['sources']:
    if s['n']==27:
        s['publisher']="Journal of Food Protection 82(1):151-158; doi:10.4315/0362-028X.JFP-18-258 (PubMed 30702949)"
        changes.append({"where":"sources[27].publisher","before":"Journal of Food Protection (PubMed 30702949)","after":s['publisher'],"why":"DOI 누락 보충"})
keep=[s for s in d['sources'] if s['n'] not in remove]
mp={s['n']:i+1 for i,s in enumerate(keep)}
for s in keep: s['n']=mp[s['n']]
d['sources']=keep
def rn(m):
    nums=[int(x) for x in re.split(r',\s*',m.group(1))]
    for x in nums: assert x in mp,(x,m.group(0))
    out=[]
    for x in nums:
        if mp[x] not in out: out.append(mp[x])
    return '['+', '.join(map(str,out))+']'
def fix(t): return re.sub(r'\[(\d+(?:,\s*\d+)*)\]',rn,t)
for s in d['sections']: s['body']=fix(s['body'])
for arr in ('compounds','assays'):
    for x in d[arr]:
        for k,v in list(x.items()):
            if isinstance(v,str): x[k]=fix(v)
        x['source']=sorted({mp[n] for n in x['source']})
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump({"changes":changes,"map":mp},open('_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes), mp)
for s in d['sections']: print(s['key'],len(s['body']))
