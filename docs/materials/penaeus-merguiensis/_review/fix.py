import json
p='/home/user/hfoodguide-wave3/docs/materials/penaeus-merguiensis/dossier.json'
d=json.load(open(p))
changes=[]
def rep(where,obj,key,old,new,why):
    v=obj[key]
    assert old in v,(where,old)
    obj[key]=v.replace(old,new,1)
    changes.append({"where":where,"before":old,"after":new,"why":why})
S={s['key']:s for s in d['sections']}
rep('sections.related_species',S['related_species'],'body',
 "리뷰에서 함께 '바나나새우류'로 다룬 인도보리새우(Fenneropenaeus indicus)와 흰다리새우(Litopenaeus vannamei / Penaeus vannamei)도 별도의 행이다[1, 3].",
 "리뷰에서 이 종과 함께 '바나나새우류'로 다룬 인도보리새우(Fenneropenaeus indicus)[3]와, 리뷰 대상은 아니지만 흔히 비교되는 흰다리새우(Litopenaeus vannamei / Penaeus vannamei)도 목록에서 별도의 행이다[1].",
 "[3] 리뷰는 P. merguiensis·P. indicus 두 종만 다룸 — 흰다리새우까지 리뷰 대상으로 읽히는 문장을 바로잡음")
rep('sections.processing',S['processing'],'body',
 "동결건조해 염화콜린-포도당 공융용매로 추출하자 아스타잔틴이 29.50 µg/g, 여기에 200 W 초음파 15분을 더하면 50.10 µg/g으로 약 70% 늘었다[7].",
 "동결건조·분쇄한 분말을 염화콜린-포도당 공융용매로 60 °C에서 30분 교반 추출하자 아스타잔틴(총 아스타잔틴 당량, 동결건조 분말 g당)이 29.50 µg/g, 교반 15분 뒤 200 W 초음파 15분을 주면 50.10 µg/g으로 대조보다 약 70% 많았다[7]. 이 값은 머리·껍데기 부산물 건조 분말 기준이며 가식부(살) 함량이 아니다[7].",
 "원문 2.1·3.4절: 시료는 72시간 동결건조한 부산물 분말, 최적 조건은 '교반 15분 + 초음파 15분'(초음파를 더한 것이 아님) — 건물 기준과 조건을 밝힘")
rep('sections.processing',S['processing'],'body',
 "마이크로파·초음파 전처리 비교에서는 이온성 마이크로에멀전 용매가 가장 나았다[8].",
 "마이크로파·초음파 전처리 비교에서는 이온성 마이크로에멀전 용매가 가장 나았고, 이 종 시료가 함께 비교한 다른 갑각류 시료보다 총 카로티노이드가 많았다[8].",
 "[8] 초록 확인 — 이 종 관련 결과를 보충")
rep('sections.genetics',S['genetics'],'body',"유전체 재분석한 결과","유전체 재염기서열 분석(리시퀀싱)한 결과",
 "[6] 2.4절은 Illumina 리시퀀싱으로 SNP를 찾은 것으로, '재분석'은 오역")
rep('sections.safety',S['safety'],'body',
 "보고한 연구가 있다[11].",
 "보고한 연구가 있다[11]. 이 연구 초록이 꼽은 알레르겐 10종 목록에는 트로포미오신이 들어 있지 않다[11].",
 "[11] 초록의 알레르겐 목록(AK·SCP·MHC·헤모시아닌 등) 확인 — 이 종 근거와 일반 트로포미오신 서술을 구분")
rep('sections.safety',S['safety'],'body',
 "이 논문 본문에는 학명이 남아 있지 않아 종 동정은 일반명으로만 확인했다[12].",
 "PubMed 도구로 받은 초록·전문 텍스트에서 학명(이탤릭)이 빠져 있어 종 동정은 일반명으로만 확인했고, 시료가 오스트레일리아 CSIRO 어업 조사·양식장에서 왔다는 것만 확인된다[12]. 같은 해역에는 인도보리새우도 'banana prawn'으로 불리므로, 이 결과는 이 종 근거로 확정하지 않고 참고로만 둔다.",
 "학명 누락은 도구의 이탤릭 제거 탓으로 보임('논문 본문에 학명이 없음'은 부정확). 일반명만으로는 P. indicus 와 구분 불가함을 밝힘([3] 리뷰가 두 종을 모두 banana prawn 으로 부름)")
rep('sections.safety',S['safety'],'body',
 "크기가 크고 먹이 폭이 넓은 암컷과 여름(7월) 시료에서 더 높았다[14].",
 "수은 농도는 성별·먹이 크기와 양의 상관을 보였고 저자들은 몸이 커 더 큰 먹이(새우·식물)를 먹는 암컷에서 높을 것으로 해석했으며, 계절로는 여름(7월) 시료가 유의하게 높았다[14].",
 "[14] 초록은 '먹이 폭이 넓다'가 아니라 '더 큰 먹이를 먹는다'고 썼고 암컷 결과는 저자 해석으로 제시")
rep('sections.safety',S['safety'],'body',
 "인도 투투쿠디 조사에서는 이 종이 조사한 갑각류 7종 가운데 미세플라스틱이 가장 적은 순위였으나, 소화관에서는 마리당 3.0개로 높은 편이었다[16].",
 "인도 투투쿠디 조사에서는 이 종이 조사한 패류·갑각류(shellfish) 7종 가운데 미세플라스틱 양이 가장 적은 순위였고, 소화관 값은 마리당 3.0개였다(초록은 이를 '가장 높은 농도'로 적었으나 함께 적은 범위 3.0–7.8개의 아래 끝이어서 원문 표현이 서로 맞지 않는다)[16].",
 "[16] 초록: 소화관 범위 3.0–7.8 MPs/마리, P. merguiensis 3.0 은 최솟값 — '높은 편'은 과장. 원문 내 불일치를 밝힘. 조사 대상에 게 등이 섞여 '갑각류' 대신 shellfish 로")
C={c['name']:c for c in d['compounds']}
rep('compounds.Vitellogenin',C['Vitellogenin'],'activity_ko',
 "난소 성숙 단계의 유전자 연구에서도 비텔로제닌 발현이 지표로 쓰였다[11, 28]",
 "난소 전사체 연구에서 비텔로제닌 유전자(PmVtg)는 성숙 난소에서 발현이 높았다[28]",
 "[28] 초록: PmVtg 가 성숙 난소에서 상향 — '지표로 쓰였다'는 원문에 없음, [11]은 이 문장 근거 아님")
C['Vitellogenin']['source']=[11,28]
rep('compounds.Tropomyosin',C['Tropomyosin'],'content_text',
 "(학명은 전문에서 확인하지 못함)","(받은 텍스트에서 학명이 빠져 일반명으로만 확인 — 인도보리새우와 구분 불가)",
 "위 safety 수정과 같은 이유")
rep('compounds.Astaxanthin',C['Astaxanthin'],'content_text',
 "공융용매 추출 29.50 µg/g","동결건조 부산물 분말 g당 — 공융용매 추출 29.50 µg/g",
 "건물(동결건조 분말) 기준임을 밝힘")
A=d['assays'][0]
rep('assays[0].content',A,'content',
 "대조(60 °C 교반 30분) 29.54 µg/g [7]",
 "대조(60 °C 교반 30분) 29.54 µg/g — 방법 2.6절은 대조를 '공융용매 없는 아세톤 추출'로 적어 결과 절과 대조 정의가 다름 [7]",
 "원문 내 불일치(방법 2.6 vs 결과 3.4) 표기")
N=d['nutrients'][0]
rep('nutrients[0].basis',N,'basis',
 "100 g당 세 집단 값의 범위(습중량이라는 명시는 원문에 없음)",
 "100 g당 세 집단 값의 범위(습중량이라는 명시는 원문에 없으나 수분 73.87–75.43 g으로 보아 생 근육 기준; 조단백질 상한은 고찰 절 21.97 g, 결과 절 최고값 21.70 g으로 원문 안에서 다름)",
 "[6] 결과 3.1절(최고 21.70)과 고찰 4.1절(20.83–21.97) 불일치를 영양 표에도 밝힘")
src={s['n']:s for s in d['sources']}
rep('sources[12].title',src[12],'title',
 "(전문 확인; 전문 텍스트·초록에서 학명이 빠져 있어 'banana shrimp'라는 일반명으로만 확인함)",
 "(전문 확인; PubMed 도구 텍스트에서 학명 이탤릭이 빠져 있어 'banana shrimp'라는 일반명으로만 확인함 — 시료는 오스트레일리아 CSIRO 제공)",
 "출처 설명 정정")
rep('sources[7].title',src[7],'title',"(전문 확인; 학명 Fenneropenaeus merguiensis 는 초록에 있음)",
 "(PMC 전문 확인; 학명 Fenneropenaeus merguiensis 는 PubMed 초록에 있음)","표기 정리")
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('/home/user/hfoodguide-wave3/docs/materials/penaeus-merguiensis/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
