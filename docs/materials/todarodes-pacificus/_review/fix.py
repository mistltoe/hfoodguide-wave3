import json
p='/home/user/hfoodguide-wave3/docs/materials/todarodes-pacificus/dossier.json'
d=json.load(open(p))
sec={s['key']:s for s in d['sections']}
changes=[]
def rep(key,old,new,why):
    b=sec[key]['body']; assert old in b,(key,old); sec[key]['body']=b.replace(old,new); changes.append({"where":f"sections.{key}","before":old,"after":new,"why":why})
rep('overview',"건강기능식품 고시형 원료의 원재료 목록에는 없어 식약처가 정한 지표성분도 없다[1].",
 "「건강기능식품의 기준 및 규격」에는 이 학명으로 지정된 고시형 원료가 없지만, 글루코사민·N-아세틸글루코사민·키토산/키토올리고당의 원재료로 '연체류(오징어, 갑오징어 등)의 뼈'가, 뮤코다당·단백의 원재료로 '오징어'를 포함한 여러 동물의 연골조직이 종 구분 없이 적혀 있다[36]. 뮤코다당·단백의 원재료는 고시 제2026-43호에 따라 2027년 1월 1일부터 '돼지, 닭, 상어의 연골조직'으로 좁혀진다[36]. 식품원료 목록에는 학명 없이 '정제오징어유' 개별인정 원료 2건(제2009-38호·제2009-76호)도 있으나, 이 종과의 대응은 확인하지 못함[1].",
 "고시 원문(2-30 글루코사민, 2-31 NAG, 2-32 뮤코다당·단백, 2-49 키토산/키토올리고당)에 '오징어' 원재료가 일반명으로 있어 '원재료 목록에 없다'는 서술이 틀림; I1020에 정제오징어유 개별인정 행 존재")
rep('history',"2013년 논문은 지난 3년 동안 동해안에서 해마다 약 2만 톤이 잡혔으며","2013년 논문은 지난 3년 동안 동해안에서 약 2만 톤(연간인지 3년 합계인지 원문 표현이 분명하지 않음)이 잡혔으며",
 "[8] 원문은 'About 20,000 M/T ... for the past 3 years'로 '해마다'라고 하지 않음")
rep('cultivation',"2013년 논문 기준 동해안 어획량은 해마다 약 2만 톤이었으나","2013년 논문은 지난 3년간 동해안 어획량을 약 2만 톤으로 적었으나","[8] 원문에 '해마다'라는 표현 없음")
rep('cultivation',"일본에서는 심층수로 사육하면 표층수보다 체중 감소가 적었다(2.5% 대 6.95%)는 사육 연구가 있어 양식 기술은 아직 연구 단계로 보인다[34].",
 "일본에서는 36시간 사육 실험에서 심층수로 기르면 표층수보다 체중 감소가 적었다(2.5% 대 6.95%)는 연구가 있고, 저자들은 이를 심층수를 쓴 오징어 양식에 기여할 결과로 보았다[34]. 양식 기술은 아직 연구 단계로 보인다.",
 "[34] 초록: 사육 기간 36시간 명시, '양식 연구 단계'는 저자 문장이 아니므로 출처 밖 판단으로 분리")
rep('biology',"반딧불오징어류(Watasenia scintillans)와 가까운 관계","매오징어(Watasenia scintillans)와 가까운 관계",
 "식품원료 목록에서 W. scintillans 의 국문명은 '매오징어'이고 '반딧불오징어'는 Enoploteuthis chunii 행이어서 다른 종과 혼동됨")
rep('genetics',"이 중복은 반딧불오징어와 공유된다[22]","이 중복은 매오징어(Watasenia scintillans)와 공유된다[22]","같은 이유(국문명 혼동)")
rep('genetics',"지난 200만 년의 인구 역사로","지난 200만 년의 집단(개체군) 역사로","demographic history 는 사람 인구가 아님")
rep('related_species',"이 가운데 빨강오징어·아메리카대왕오징어·I. argentinus는 살오징어와 함께 Ommastrephidae과 공통 프라이머로 검출되는 종으로 다뤄졌다[24].",
 "이 가운데 빨강오징어·아메리카대왕오징어·I. argentinus는 살오징어와 함께 중국 시장의 흔한 오징어 4종으로 묶여 실시간 PCR 판별 대상이 되었다(살오징어·아메리카대왕오징어는 COI, 빨강오징어는 Cytb, I. argentinus는 ATPase 6 유전자 표적; 과 공통 프라이머는 12S rDNA)[24].",
 "[24] 초록: 종별 표적 유전자가 다르고 과 공통 프라이머는 12S rDNA — 원 문장은 종 판별 방식을 부정확하게 요약")
rep('safety',"동중국해 시료에서도 소화샘의 카드뮴이 다른 해역 근연종보다 높았고","동중국해 시료(살오징어 8개체)에서도 소화샘의 카드뮴이 다른 해역의 비슷한 종 보고치보다 높았고",
 "[6] 초록: 'higher than similar species from other regions', 표본 수 4+4")
for c in d['compounds']:
    if c['name']=='Ile-Ile-Tyr':
        old=c['part']; c['part']="미오신 중쇄(가상 분해)"; changes.append({"where":"compounds[Ile-Ile-Tyr].part","before":old,"after":c['part'],"why":"[31] 초록은 '미오신 중쇄'만 말하고 외투막 부위는 언급 없음"})
for s in d['sources']:
    if s['n']==1:
        s['title']=s['title'].replace("가공품 '오징어'·'건오징어' 등 행(학명 Doryteuthis bleekeri 등으로 표기);","가공품 '오징어'·'건오징어' 등 행(학명 Doryteuthis bleekeri 등으로 표기), 학명 없는 '정제오징어유(기능성원료인정제2009-38호·제2009-76호)' 개별인정 행;")
    if s['n']==8:
        s['title']=s['title'].replace("(본문에서 이탤릭 학명이 빠져 있어 종명은 PubMed 키워드 'Todarodes pacificus'로 대응)","(본문에서 이탤릭 학명이 빠져 있어 종명은 PubMed 키워드 'Todarodes pacificus'와 본문의 'Ommastrephidae'·강릉 주문진 앞바다 어획 기술로 대응; 검토자 V2 확인)")
    if s['n'] in (23,29,31):
        s['title']=s['title'].replace("(초록 확인)","(초록 확인; PubMed 키워드 'Todarodes pacificus' 수록을 검토자 V2가 확인)")
d['sources'].append({"n":36,"title":"식약처 고시 제2026-43호 「건강기능식품의 기준 및 규격」 제3. 2-30 글루코사민·2-31 N-아세틸글루코사민·2-49 키토산/키토올리고당(원재료 '연체류(오징어, 갑오징어 등)의 뼈'), 2-32 뮤코다당·단백(원재료 '…오징어, 게, 어패류의 연골조직'; 2027.1.1. 시행 개정 '돼지, 닭, 상어의 연골조직') (로컬 원문 docs/refs/MFDS/건강기능식품의기준및규격_2026-43_제1~제3.txt)","url":"https://www.mfds.go.kr/brd/m_211/view.do?seq=14973","publisher":"식품의약품안전처","accessed":"2026-11-02"})
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('/home/user/hfoodguide-wave3/docs/materials/todarodes-pacificus/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
