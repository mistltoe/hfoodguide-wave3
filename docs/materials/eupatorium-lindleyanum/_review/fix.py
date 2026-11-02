import json
p='/home/user/hfoodguide-wave3/docs/materials/eupatorium-lindleyanum/dossier.json'
d=json.load(open(p))
changes=[]
def sec(key): return next(s for s in d['sections'] if s['key']==key)
def rep(where,obj,field,old,new,why):
    assert old in obj[field],(where,old)
    obj[field]=obj[field].replace(old,new); changes.append({'where':where,'before':old,'after':new,'why':why})
s=sec('overview')
rep('sections.overview',s,'body',"중국에서는 지상부를 '야마추이(野马追, Yemazhui)'라는 약재로 써 왔고, 식품으로 오래 이용되었다는 서술도 있다[3, 15].",
 "중국에서는 지상부를 '야마추이(野马追, Yemazhui)'라는 약재로 써 왔고[2, 3], 중국에서 기능성 식품으로 오래 쓰였다는 서술도 있다[15].",
 "[3] 리뷰에는 식품 이용 언급이 없고 [15] 만 'functional food in China' 라고 씀; 지상부=Ye-ma-zhui 는 [2]")
rep('sections.overview',s,'body',"함량은 뿌리 > 꽃 > 줄기 > 잎 순이었다[4].",
 "총 함량은 뿌리 > 꽃 > 줄기 > 잎 순이어서 식품원료로 허용된 잎이 가장 적었지만 잎에서도 검출되었다[2, 4].",
 "PA 간독성 근거를 이 종 자료로 분명히 함([2] 잎 에키나틴 0.390 ng/g 검출, [4] 순서)")
s=sec('history')
rep('sections.history',s,'body',"리뷰에 정리된 중국 임상 보고에는 어린이 만성 기관지염 400명 시험과 급성·만성 기관지염 성인 52명 시험이 있으나, 리뷰는 연구 대부분이 전임상 단계여서 임상 연구가 더 필요하다고 지적했다[3].",
 "리뷰에 정리된 중국 임상 보고에는 어린이 만성 기관지염 400명 시험과 급성·만성 기관지염 환자(18–77세) 52명 시험이 있으나, 리뷰는 보고된 여러 효능을 평가하려면 임상 연구가 더 필요하다고 지적했다[3].",
 "[3] 전문에 '대부분 전임상' 표현 없음; 'Clinical studies are still necessary' 로 맞춤")
rep('sections.history',s,'body',"동물 실험으로는 세스퀴테르펜 분획(15·30·60 mg/kg, 7일 경구)과 플라보노이드 분획이 생쥐의 LPS 급성 폐손상 지표를 줄였고, 유팔리놀라이드 L·M 등은 대식세포의 TNF-α·IL-6 분비를 낮췄다[17, 18, 27].",
 "동물 실험으로는 세스퀴테르펜 분획(15·30·60 mg/kg, 7일 경구 전처치)과 플라보노이드 분획이 생쥐의 LPS 급성 폐손상 지표를 줄였고, 세포 실험에서는 유팔리놀라이드 L·M 등이 LPS로 자극한 생쥐 대식세포주(RAW 264.7)의 TNF-α·IL-6 분비를 낮췄다[17, 18, 27]. 이는 동물·세포 수준의 결과로, 사람에게서 같은 효과가 확인된 것은 아니다.",
 "[27] 은 RAW 264.7 세포 실험; 세포·동물 결과 과장 방지")
s=sec('related_species')
rep('sections.related_species',s,'body',"국문 이름만으로는 두 원료가 혼동될 수 있다[1].",
 "국문 이름만으로는 두 원료가 혼동될 수 있다[1]. 골등골나물잎의 이명 '벌등골나물'도 등골나물잎·향등골나물잎 행에 함께 올라 있다[1].",
 "I1020 로컬 원자료: 벌등골나물이 등골나물잎·향등골나물잎 RAWMTRL_NCKNM 에도 있음")
rep('sections.related_species',s,'body',"일본 시판 꿀의 PA 조성 분석에서도 지치과와 등골나물속 유래로 보이는 무리가 시료의 절반 이상을 차지했다[28].",
 "일본에서 판매된 꿀의 PA 조성 분석에서는 일본산 꿀이 세 무리로 나뉘었고, 지치과·등골나물속 유래로 보이는 무리가 일본산 시료의 절반 이상이었다(속 수준 자료로, 이 종을 특정한 것은 아님)[28].",
 "[28] 초록: Group 1 은 'Japanese honey' 프로필 분류 기준, 종 특정 아님")
s=sec('safety')
rep('sections.safety',s,'body',"총 PA 함량은 뿌리 > 꽃 > 줄기 > 잎 순으로, 식품원료로 허용된 잎이 가장 적었다[4].",
 "총 PA 함량은 뿌리 > 꽃 > 줄기 > 잎 순으로, 식품원료로 허용된 잎이 가장 적었으나 잎에서도 검출되었다[4]. 이 종의 대사체 분석에서 확인된 알칼로이드 9종은 모두 1,2-불포화 네신 골격의 PA로 추정되었고, 저자들은 PA가 주로 간독성을 띠며 과다 섭취 시 간정맥폐쇄병 위험을 높일 수 있다고 적었다[2].",
 "PA 간독성 근거를 이 종 자료([2] 전문 2.1.1·3절)로 명시")
rep('sections.safety',s,'body',"중국 동물 시험에서는 생약 45 g/kg에서 뚜렷한 영향이 없었고 만성 독성 시험에서도 독성 반응이 보고되지 않았으나, 리뷰는 독성·약동학 연구가 적어 임상 안전성 자료가 부족하다고 지적했다[3].",
 "리뷰에 인용된 중국 동물 시험에서는 추출물이 생약 45 g/kg에서도 쥐의 신경·심혈관·호흡계에 뚜렷한 영향을 주지 않았고, 다른 시험에서 LD50은 생약 225.6 g/kg, 만성 독성 시험에서는 독성 반응이 없었다고 보고되었으나, 리뷰는 독성 연구가 아직 제한적이고 약동학 연구도 더 필요하다고 지적했다[3].",
 "[3] 원문: 45 g/kg 은 일반약리(신경·심혈관·호흡계) 시험, LD50 225.6 g/kg; '임상 안전성 자료 부족' 은 원문 표현 아님")
rep('sections.safety',s,'body',"유팔리놀라이드 A·B는 사람 간 마이크로솜에서 주로 가수분해로 해독되었고 간세포 독성이 낮았다[19].",
 "유팔리놀라이드 A·B는 사람 간 마이크로솜에서 주로 가수분해로 대사되어 해독되었고 HepG2 세포 독성이 낮았다(시험관 실험)[19].",
 "[19] 는 HepG2–HLM 공배양 시험관 실험")
# compounds
C={c['name']:c for c in d['compounds']}
def crep(name,field,old,new,why):
    c=C[name]; assert c[field]==old or old in c[field],(name,field)
    before=c[field]; c[field]=c[field].replace(old,new) if isinstance(c[field],str) else new
    changes.append({'where':f'compounds[{name}].{field}','before':before,'after':c[field],'why':why})
for n in ['Eupalinolide A','Eupalinolide B','Hyperoside','Chlorogenic acid']:
    crep(n,'content_text','(HPLC-PDA)[2]','(HPLC-PDA, 60 °C 건조 분말 기준)[2]','[2] 4.1: 부위별 분리 후 60 °C 건조 — 건물 기준 명시')
crep('Echinatine','content_text','(UPLC-MS/MS, 원문 단위 그대로)[2]','(UPLC-MS/MS, 60 °C 건조 분말, 원문 단위 그대로)[2]','건물 기준 명시')
crep('Eupalinolide B','activity_ko','(리뷰 인용)[3]','(리뷰 인용, 원 연구 [20])[3, 20]','[20] 초록: 625 mg/kg 단회 위내 투여 확인')
crep('Rutin','part','지상부','부위 미기재(초록 기준)','[10] 초록에 부위 없음')
crep('Nepetin','part','전초','부위 미기재(초록 기준)','[14] 초록에 부위 없음(부탄올 분획만)')
crep('Cirsiliol','part','전초','부위 미기재(초록 기준)','[14] 초록에 부위 없음')
crep('Jaceosidin','part','잎·꽃; 전초','잎·꽃','[14] 초록에 부위 없음')
crep('Eupalinolide J','activity_ko','세포·동물 실험에서 STAT3 분해를 통한 암 전이 억제 보고[29]','세포·동물 실험에서 STAT3 분해를 통한 암세포 전이 억제 보고(사람 자료 없음)[29]','과장 방지')
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('/home/user/hfoodguide-wave3/docs/materials/eupatorium-lindleyanum/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
