import json, sys
P='/home/user/hfoodguide-wave3/docs/materials/siganus-fuscescens/'
d=json.load(open(P+'dossier.json'))
changes=[]
def sec(k): return next(s for s in d['sections'] if s['key']==k)
def rep(k, old, new, why):
    s=sec(k); assert old in s['body'], (k, old[:40]); s['body']=s['body'].replace(old,new); changes.append({"where":"sections."+k,"before":old,"after":new,"why":why})

rep('overview','해조류와 해초를 주로 먹는 초식성 어종이며, 등지느러미 가시에 독이 있어 사람이 찔리는 사고가 잦은 독어로 알려져 있다[5, 16].',
 '해조류와 해초를 먹는 초식성 어종이며[16], 등지느러미 가시에 독이 있다[5]. 독가시치과(rabbitfish) 어류는 사람 찔림 사고가 잦은 독어로 알려져 있는데, 이는 가시에 찔리는 사고의 이야기이고 살을 먹는 문제와는 다르다[5].',
 '[5] 초록의 "frequently involved in human accidents"는 이 종이 아니라 독가시치과 전체를 말함. [16]은 먹이만 뒷받침. 가시 자상과 섭취를 구분')
rep('history','일본 연안에서 가장 흔한 독가시치과 어종으로 소개되며, 사람에게 찔림 사고를 자주 일으키는 독어로 알려져 있다[5].',
 '일본 연안에서 가장 흔한 독가시치과 어종으로 소개되며, 독가시치과 어류는 사람 찔림 사고를 자주 일으키는 독어로 알려져 있다[5].',
 '[5] 초록: 찔림 사고는 독가시치과(rabbitfish) 전체에 대한 서술')
rep('history','다시마류와 해조류를 먹어','켈프(대형 갈조류)와 다른 해조류를 먹어','[15] 초록은 kelp(서호주 Ecklonia)이며 다시마류(Laminaria/Saccharina)로 옮기면 오해 소지')
rep('history','국내 제주 연안에서는 2012년 2–12월 매달 채집한 표본으로 나이와 성장을 조사한 연구가 있다고 검색 결과 요약에 나오나, 원문은 열지 못해 세부 수치는 확인하지 못함[29].',
 '제주 연안 독가시치의 나이·성장과 생식생태를 다룬 국내 학술지 논문이 있다는 것은 검색 결과 요약으로만 확인했고, 원문을 열지 못해 채집 시기·수치는 싣지 않았다(확인하지 못함)[29, 30].',
 '[29][30]은 WebSearch 요약뿐이고 원문 사이트가 막혀 대조 불가 — 세부(채집 기간)를 덜어내고 근거 수준을 낮춤')
rep('biology','서호주 실험에서는 어린 다시마보다','서호주 다지선택 실험에서는 어린 켈프(Ecklonia radiata)보다','[14] 초록: young kelp Ecklonia radiata')
rep('biology','S. canaliculatus와 합쳐 분석한 메타분석에서 성숙 최소 체장은',
 '아래 생활사 수치는 S. canaliculatus를 동의어로 보고 두 학명 자료를 합산한 메타분석 값이다. 이 분석에서 성숙 최소 체장(가랑이 체장 기준)은',
 '[12] 전문 Methods: 두 학명을 동의어로 보아 자료를 합침(pooled), 길이는 가랑이 체장(FL)으로 표준화 — 합산값임을 문장 앞에 명시')
rep('biology','\n\n제주 연안 연구는 생식소 지수가 7–8월에 높고 주 산란기가 7–8월이며 연 1회 산란한다고 보고했다고 검색 결과 요약에 나오나, 원문은 확인하지 못함[30].','',
 '[30] 원문 미열람(WebSearch 요약뿐) — 산란기·연 1회 산란 수치를 삭제하고 history 의 한 문장으로 합침')
rep('related_species','이 문서는 벌레무늬독가시치와 다른 Siganus 종의 자료를 섞지 않았다[1].',
 '이 문서는 벌레무늬독가시치 자료를 쓰지 않았고, S. canaliculatus와 합산된 자료([12] 생활사 수치)와 다른 독가시치과 어류 자료(안전성 절의 지중해 사례)는 그렇다고 밝혀 두었다.',
 '실제로 [12]는 S. canaliculatus 합산값이므로 "섞지 않았다"를 정확히 고침, [1]은 이 주장의 출처가 아님')
rep('cultivation','독가시치는 초식성이고 비교적 빨리 자라며 소비자 선호가 좋아 양식 대상으로 관심을 받지만, 초기 자어 단계의 종묘 생산이 여전히 어렵다[17].',
 '독가시치과 어류는 초식성이고 비교적 빨리 자라며 소비자 선호가 좋아 양식 대상으로 관심을 받지만, 초기 자어 단계의 종묘 생산이 여전히 어렵다고 소개된다[17].',
 '[17] 전문 서론: 이 서술은 rabbitfishes(독가시치과) 전체에 대한 것')
rep('cultivation','한 연구 시설에서는','일본의 한 대학 양식연구소 시험장에서는','[17] 전문: 일본 Oshima 시험장(기관명 대신 일반 표현)')
rep('cultivation','황금(Scutellaria baicalensis) 지상부 추출물을 사료에 1% 넣자 4주 뒤 몸길이와 체중이 대조군보다 늘었다[4].',
 '황금(Scutellaria baicalensis) 지상부 물 추출물을 사료에 1% 넣자 4주 뒤 몸길이(약 30%)와 체중(약 20%)이 대조군보다 늘었고, 5%에서는 오히려 줄었다[4].',
 '[4] 전문 결과 대조 — 증가 폭과 고용량 역효과 보충')
rep('processing','양식 독가시치 등살의 아미노산을 LC-MS/MS로 잰 연구에서 대조군은 류신이 20.02 ± 0.05 mg/100 g으로 가장 많았고 알라닌이 13.92 ± 0.11 mg/100 g으로 뒤를 이었다[4].',
 '양식 독가시치 등살의 아미노산 12종을 LC-MS/MS로 잰 연구에서 대조군은 류신이 20.02 ± 0.05 mg/100 g으로 가장 많았고 알라닌이 13.92 ± 0.11 mg/100 g으로 뒤를 이었다(근육 무게 기준이나 생·건 기준은 본문에 명시 없음)[4]. 이 논문은 제목·초록 표기에서 학명이 빠져 보이지만 PubMed 색인은 Siganus fuscescens로 검색되고, 같은 연구진이 같은 추출물로 이 종(18S rRNA로 종 확인)의 세포주를 다룬 선행 연구를 이어 간 것이어서 독가시치 자료로 보았다[4].',
 '[4] 학명 누락 — 종 판정 근거 명시, 수치 기준(생/건) 미명시 표기')
rep('safety','독은 등지느러미 가시에 있고, 가시 추출물은 쑤기미류 독소와 닮은 단백질 독소(α 703, β 699 아미노산)를 가지며 생쥐 치사·용혈·부종·통증 활성을 보였다[5]. 이는 손질 중 가시에 찔리는 자상의 문제이며, 이 종의 살을 먹어서 생기는 시가테라 독소 검출 보고는 PubMed에서 확인하지 못함.',
 '독은 등지느러미 가시에 있고, 가시 추출물은 쑤기미류 독소와 닮은 단백질 독소(α 703, β 699 아미노산)를 가지며 생쥐 치사·용혈·부종·통증 활성을 보였다[5]. 이는 손질 중 가시에 찔리는 자상의 문제이고, 살을 먹어서 생기는 독성을 보인 자료는 아니다[5]. 지중해 동부에서 독가시치과 어류(종 미상, 이 종이 아님)를 먹은 뒤 시가테라 의심 중독을 겪은 사례 보고가 있으나[34], 이 종의 살에서 시가테라 독소를 검출한 보고는 PubMed에서 확인하지 못함.',
 '가시 독과 섭취 안전성 구분 강화; 독가시치과 시가테라 의심 사례(다른 종·지역)를 출처와 함께 구분해 추가')
rep('safety','중국 산터우 시장 조사에서 독가시치의','중국 산터우 시장 조사(2013년, 52종 382마리)에서 독가시치의','[24] 초록: 2013년 2–12월, 382마리 52종')
rep('safety','남중국해 독가시치의 장과 위에서는 회충류 Hysterothylacium longilabrum이 새로 기재되었다[25].',
 '남중국해 독가시치와 S. canaliculatus의 장과 위에서 회충류 Hysterothylacium longilabrum이 새로 기재되었다[25].',
 '[25] 초록: 두 종에서 함께 채집')
rep('safety','사료로 무기비소를 먹인 실험에서 근육 비소의 79.0–95.2%가 독성이 낮은 아르세노베타인으로 바뀌었다[20].',
 '무기비소를 400·1,500 μg/g(사료 건중량, 명목 농도) 넣은 사료를 21·42일 먹인 실험에서 근육 비소의 79.0–95.2%, 간 비소의 63.3–91.3%가 독성이 낮은 아르세노베타인 형태였다[20].',
 '[20] 초록 대조 — 노출 조건(고농도 실험 사료)과 간 값 보충, 생 시장 어류 값이 아님을 분명히')
rep('safety','하이링섬 독가시치 간의 노르플록사신이 254.58 ng/g(습중량)으로 가장 높았으나, 연구진은 근육·간의 플루오로퀴놀론 잔류가 건강 위험 수준은 아니라고 보았다[23].',
 '하이링섬 독가시치 간의 노르플록사신이 254.58 ng/g(습중량)으로 가장 높았으나(근육은 간보다 낮음), 연구진은 중국 정부 최대잔류허용기준과 FAO/WHO 1일 섭취허용량에 비추어 플루오로퀴놀론 잔류가 광둥 연안 주민 건강에 위험이 되지 않는다고 보았다[23].',
 '[23] 초록: 판단 기준(MRL·ADI)과 간>근육 명시')

# aliases
if 'Rabbitfish' in d['aliases']:
    d['aliases'].remove('Rabbitfish')
    changes.append({"where":"aliases","before":"Rabbitfish","after":"(삭제)","why":"독가시치과 전체를 가리키는 일반명이라 이 종의 별명으로 두면 다른 Siganus 자료가 섞일 수 있음(본문 related_species 도 같은 이유를 적음)"})

# compounds
for c in d['compounds']:
    if c['name'] in ('Leucine','Alanine','Glutamic acid'):
        c['content_text']=c['content_text']+'(근육 무게 기준, 생·건 표기 없음)'
    if c['name']=='Arsenobetaine':
        c['part']='근육·간(무기비소 고농도 사료 노출 실험)'
changes.append({"where":"compounds[류신·알라닌·글루탐산].content_text","before":"mg/100 g","after":"mg/100 g(근육 무게 기준, 생·건 표기 없음)","why":"[4] 본문에 생/건 기준이 없음"})

# sources
s4=d['sources'][3]
s4['title']='Feeding containing the aerial part of Scutellaria baicalensis promotes the growth and nutritive value of rabbit fish. Food Sci Nutr 2021;9(9):4827-4838 (PMC 전문 확인; 도구 출력에서 학명 이탤릭이 빠지나 PubMed "Siganus fuscescens AND Scutellaria" 검색에 걸리고, 같은 연구진의 선행 세포주 연구 PMID 32738512가 S. fuscescens를 18S rRNA로 확인)'
s4['publisher']='Food Science & Nutrition, PMID 34531995, PMC8441375'
for i,(pmid) in [(4,'29466431'),(12,'35543704'),(13,'34711927'),(15,'31744442'),(17,'41828986'),(28,'30210475'),(33,'36420515')]:
    pub=d['sources'][i-1]['publisher']
    if 'PMID' not in pub: d['sources'][i-1]['publisher']=pub.replace(', PMC',', PMID '+pmid+', PMC')
d['sources'][9]['title']=d['sources'][9]['title'].replace('(PubMed 초록)','(PubMed 초록; 373개체는 S. canaliculatus로 보고된 미토콘드리아 계통 C를 가진 개체도 포함)')
d['sources'][28]['title']='Age and growth of rabbit fish, Siganus fuscescens in the coast of Jeju island, Korea. 2014 — 원문 사이트가 이 환경에서 막혀 WebSearch 결과 요약으로만 존재를 확인(원문 미열람, 수치 미사용)'
d['sources'][29]['title']='제주 연안 독가시치(Siganus fuscescens)의 생식생태. 2019 — 원문 사이트가 이 환경에서 막혀 WebSearch 결과 요약으로만 존재를 확인(원문 미열람, 수치 미사용)'
d['sources'].append({"n":34,"title":"Rabbitfish (\"aras\"): an unusual source of ciguatera poisoning. Isr Med Assoc J 2002;4(1):28-30 (PubMed 초록; 지중해 동부 사례, 어종 학명 미기재 — 이 종의 자료가 아님)","url":"https://pubmed.ncbi.nlm.nih.gov/11802305/","publisher":"PubMed, PMID 11802305","accessed":"2026-11-02"})
json.dump(d,open(P+'dossier.json','w'),ensure_ascii=False,indent=1)
json.dump(changes,open(P+'_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
