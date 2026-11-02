import json,sys
p='/home/user/hfoodguide-wave3/docs/materials/acer-tegmentosum/dossier.json'
d=json.load(open(p))
changes=[]
def sec(k): return next(s for s in d['sections'] if s['key']==k)
def rep(where,obj,key,old,new,why):
    if old not in obj[key]: sys.exit('MISSING: '+where+' :: '+old[:50])
    obj[key]=obj[key].replace(old,new); changes.append({"where":where,"before":old,"after":new,"why":why})

s=sec('related_species')
rep('sections.related_species',s,'body',"단풍나무(A. palmatum)는 수액 등, 고로쇠(A. pictum subsp. mono)는 수액·전체,","단풍나무(A. palmatum)와 고로쇠(A. pictum subsp. mono)는 수액,","로컬 I1020 원자료: 단풍나무·단풍나무추출물·단풍당시럽과 고로쇠 3품목 모두 '사용가능부위 : 수액'(고로쇠농축분말의 부위코드 '전체'는 분류 코드일 뿐 사용 부위는 수액)")
rep('sections.related_species',s,'body',"주성분 살리드로사이드는 돌꽃속(Rhodiola) 식물의 대표 성분으로도 알려져 있어, 로디올라 제품의 살리드로사이드 자료와 혼동하지 않아야 한다[2].","주성분 살리드로사이드는 다른 식물의 꽃 추출물 독성 연구에서도 다루어진 성분이어서, 다른 식물 유래 살리드로사이드 자료를 산겨릅나무 가지에 그대로 옮겨서는 안 된다[2].","[2] 전문은 돌꽃속을 대표 출처로 언급하지 않음(다른 식물 꽃 추출물의 살리드로사이드 90일 독성 연구만 인용)")

s=sec('history')
rep('sections.history',s,'body',"건강기능식품 고시형 원료나 개별인정형 원료로 인정되었는지는 확인하지 못함.","2024년 논문은 식약처가 이 나무를 식품원료로 인정했다고 적었다(인정 번호 2018-7로 기재)[4]. 건강기능식품 고시형 원료나 개별인정형 원료로 인정되었는지는 확인하지 못함.","[4] 서론의 식약처 식품원료 인정 언급을 근거로 추가(원 고시는 확인 못함)")

s=sec('processing')
rep('sections.processing',s,'body',"2024년 연구는 가지 분말 400 g을 70% 에탄올 2.5 L로 80 °C에서 2시간 추출했고 수율은 19.6%였다[4].","2024년 연구는 산겨릅나무 시료(사용 부위는 원문에 적혀 있지 않음) 분말 400 g을 70% 에탄올 2.5 L로 80 °C에서 2시간 추출했고 수율은 19.6%였다[4].","[4] 전문 Methods 는 'AT (400 g) was powdered'라고만 쓰고 가지라고 밝히지 않음")
rep('sections.processing',s,'body',"같은 연구에서 유산균으로 발효시키자","같은 연구에서 고초균(Bacillus subtilis, 낫토 발효균 계열) 균주 NCDO 1769T로 발효시키자","[4] 은 LB 배지에서 낫토 발효에 쓰이는 균(NCDO 1769T)으로 발효함 — 유산균이 아님")
rep('sections.processing',s,'body',"이 발효물의 효과 비교는 세포 실험 결과다[4].","이 발효물의 효과 비교는 세포 실험과 스트렙토조토신 당뇨 생쥐의 망막 실험 결과다[4].","[4] 은 세포 실험 외에 STZ 생쥐 망막 실험도 포함")

s=sec('biology')
rep('sections.biology',s,'body',"밝은 흰 세로줄 무늬","밝은 흰 줄무늬","[7] 은 'bright white stripes'라고만 씀")

s=sec('safety')
old="2013년 연구에서 추출물의 급성 경구 반수치사량은 흰쥐에서 2,000 mg/kg 초과였으나, 박테리아 복귀돌연변이 시험(Ames)에서 TA98 균주의 복귀 콜로니가 늘어 변이원성이 의심되었다[3]. 2021년 연구는 가지 열수추출물로 다시 시험해 박테리아 복귀돌연변이·염색체 이상·소핵 시험 모두에서 유전독성이 없다고 보고했다[2]. 같은 연구에서 흰쥐 90일 반복투여의 무독성량(NOAEL)은 5,000 mg/kg 초과였고, 비글견 급성독성도 5,000 mg/kg까지 나타나지 않았다[2]. 두 연구의 차이는 원료 산지·부위나 시료 제조 차이 때문일 수 있다고 저자들이 설명했다[2]. 과량 섭취 때 복통·설사 같은 가벼운 부작용이 드물게 보고된다고 알려져 있다[2]."
new="유전독성 결과는 두 연구에서 엇갈린다. 2013년 연구(부위는 초록에 없음)에서 추출물의 급성 경구 반수치사량은 흰쥐에서 2,000 mg/kg 초과였고, 염색체 이상 시험(CHO-K1 세포)과 생쥐 골수 소핵 시험에서는 유의한 증가가 없었으나, 박테리아 복귀돌연변이 시험(Ames)에서는 대사 활성화(S9) 여부와 관계없이 TA98 균주의 복귀 콜로니가 늘어 저자들은 변이원성이 있다고 결론짓고 원인 성분 규명이 필요하다고 했다[3]. 2021년 연구는 가지 열수추출물로 다시 시험해 TA100 균주에서 최고 용량일 때 통계적으로 유의하지 않은 1.2배 증가만 있었을 뿐 Ames·염색체 이상·소핵 시험 모두에서 변이원성·염색체 손상이 없다고 보고했다[2]. 같은 연구에서 흰쥐 급성독성 반수치사량과 90일 반복투여의 무독성량(NOAEL)은 모두 5,000 mg/kg 초과였고, 비글견 급성독성도 5,000 mg/kg까지 나타나지 않았다[2]. 저자들은 두 연구의 차이가 원료 출처·사용 부위나 시료 제조 차이 때문일 수 있으나 원인은 아직 분명하지 않으며, 산지·부위별 성분과 그 유전독성을 비교하는 추가 연구가 필요하다고 밝혔다[2]. 또 자신들의 결과는 가지만 쓴 시료에서 얻은 것이라고 덧붙였다[2]. 2021년 연구 서론은 과량 섭취 때 복통·설사 같은 가벼운 부작용이 드물게 관찰된다고 적었으나, 그 원 보고는 확인하지 못함[2]."
rep('sections.safety',s,'body',old,new,"[3] 초록: 염색체 이상·소핵은 음성, Ames TA98 양성(S9 무관), 저자 결론 '변이원성 있음'. [2] 전문: TA100 최고 용량 1.2배(비유의) 외 음성, 원인 불명·추가 연구 필요. 엇갈린 결과를 원문대로 균형 있게 적음")

# compounds
c={x['name']:x for x in d['compounds']}
x=c['Salidroside']
rep('compounds.Salidroside.part',x,'part',"가지(열수·70% 에탄올 추출물)","가지 열수추출물[2]; 70% 에탄올 추출물(부위 미기재)[4]","[4] 은 부위를 밝히지 않음")
rep('compounds.Salidroside.content_text',x,'content_text',"가지 70% 에탄올 추출물 6.41%(w/w)[4]","70% 에탄올 추출물(부위 미기재) 6.41%(w/w)[4]","[4] 부위 미기재")
rep('compounds.Salidroside.activity_ko',x,'activity_ko',"각질형성세포에서 TSLP 생성 억제 — 세포 결과[24]","비만세포주(KCMH-1)에서 TSLP 생성 억제 — 세포 결과[24]","[24] 초록: KCMH-1 세포(MeSH 'Mast Cells'), 각질형성세포 아님")
x=c['Tyrosol']
rep('compounds.Tyrosol.content_text',x,'content_text',"가지 에탄올 추출물에서는 '매우 적은 성분'으로 기재, 유산균 발효물에서 0.75%(w/w)[4]","산겨릅나무 추출물의 티로솔 함량은 매우 낮다고 기존 문헌을 인용, 고초균 발효물에서 0.75%(w/w)[4]","[4] 의 '매우 낮음'은 서론의 문헌 인용이며 부위 미기재; 발효균은 유산균이 아님")
x=c['Feniculin']
rep('compounds.Feniculin.content_text',x,'content_text',"이 종에서 처음 분리, 정량값 없음[6]","줄기 열수추출물 에틸아세테이트 분획에서 분리, 정량값 없음[6]","[6] 의 '처음 분리' 화합물 번호가 본문에서 확인되지 않아 단정 표현 제거")

# assays
a=d['assays'][1]
rep('assays[1].part',a,'part',"가지(70% 에탄올 추출물) 및 그 유산균 발효물","70% 에탄올 추출물(부위 미기재) 및 그 고초균 발효물","[4] 부위 미기재, 발효균은 낫토균 계열")
rep('assays[1].conditions.sample_prep',a['conditions'],'sample_prep',"가지 분말 400 g","시료(부위 미기재) 분말 400 g","[4] 부위 미기재")
x=a['conditions']
rep('assays[1].conditions.sample_prep',x,'sample_prep',"(수율 19.6%)","(수율 19.6%); 분석 시료 농도 3 mg/mL","원문 확인 — 주입 시료 농도 명시")
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('/home/user/hfoodguide-wave3/docs/materials/acer-tegmentosum/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
