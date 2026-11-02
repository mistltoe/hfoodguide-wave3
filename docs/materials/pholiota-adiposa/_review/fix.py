import json,sys
p='/home/user/hfoodguide-wave3/docs/materials/pholiota-adiposa/dossier.json'
d=json.load(open(p))
changes=[]
def sec(k): return next(s for s in d['sections'] if s['key']==k)
def rep(where,obj,key,old,new,why):
    t=obj[key]; assert old in t,(where,old); obj[key]=t.replace(old,new); changes.append({"where":where,"before":old,"after":new,"why":why})
rep('sections.history',sec('history'),'body','2006년 농촌진흥청 계열 연구진이 균주 ASI 24018','2006년 국내 연구진이 균주 ASI 24018','[17] 전문에서 연구진 소속(농촌진흥청 계열)을 확인할 수 없음')
rep('sections.biology',sec('biology'),'body','같은 균주의 β-1,4-만난에이스(Vmax 1,990 U/mg)와 정제 자일라네이스(kcat 4,261 s−1)는','같은 균주의 β-1,4-만난에이스(Vmax 1,990 U/mg)와 같은 연구진이 정제한 자일라네이스(kcat 4,261 s−1)는','[22] 초록은 균주명을 밝히지 않음(같은 연구진)')
rep('sections.cultivation',sec('cultivation'),'body','중간 농도(200, 단위는 초록에 없음)에서 효소 활성이 가장 높았다','시험한 첨가 농도 가운데 가장 낮은 200(단위는 초록에 없음)에서 아밀레이스·라케이스·셀룰레이스 활성이 무첨가보다도 높았다','[26] 시험 농도는 0·200·400·800으로 200은 중간 농도가 아님')
rep('sections.cultivation',sec('cultivation'),'body','균사 배양에서는 황산아연','액체·평판 균사 배양(자실체 아님)에서는 황산아연','균사체 연구임을 분명히 함')
rep('sections.processing',sec('processing'),'body','셀레늄·금 나노입자 소재로도 연구되었지만, 액체 배양 균사체 다당(PAP80-2a 등)은 식품원료 사용 부위가 아니다[1, 12, 14, 28]','셀레늄 나노입자 소재로도 연구되었지만(세포·동물 실험)[12, 28], 액체 배양 균사체 다당(PAP80-2a 등)은 식품원료 사용 부위가 아니다[1, 14, 15, 16]','[28]은 셀레늄 나노입자만 다룸(금 나노입자 출처 없음); 균사체 문장에 자실체·부위 미상 논문 [12, 28]이 인용되어 있었음')
rep('sections.processing',sec('processing'),'body','데이터베이스와 도킹 예측에서 나온 것으로, 이 버섯에서 실측한 성분은 아니다[25]','데이터베이스(TCMSP 등)와 분자 도킹 예측에서 나온 후보로, 이 연구에서 버섯 시료를 분석해 확인한 성분이 아니며 알츠하이머 효과도 실험으로 확인되지 않았다[25]','[25]는 네트워크 약리학·기계학습·도킹만 수행')
rep('sections.processing',sec('processing'),'body','간 중성지방과 부고환 지방은 변하지 않았다[17]','간 중성지방(0.5% 군 제외)과 부고환 지방은 변하지 않았다[17]','[17] 전문: 간 TG는 0.5% 군을 빼면 차이 없음')
rep('sections.genetics',sec('genetics'),'body','공개 데이터베이스의 첫 유전체(GCA_014526955.1)는','기존 공개 유전체(GCA_014526955.1)는','[3]은 "이전에 보고된 공개 유전체"라 했을 뿐 첫 유전체라 하지 않음')
rep('sections.genetics',sec('genetics'),'body','채집한 야생 균주 HS5에서','채집한 야생 균주에서','[3] 전문·초록에서 균주명 HS5를 확인하지 못함')
rep('sections.safety',sec('safety'),'body','구분되지 않으므로, 식용은 동정이 확실한 재배품이나 확인된 자실체로 한정하는 것이 안전하다[2]','구분되지 않는다[2]. 따라서 야생 채취품은 동정에 특히 주의해야 한다(이 권고는 출처의 직접 결론이 아니라 [2]의 결과에서 끌어낸 것이다)','[2]는 식용 권고를 하지 않음 — 추론임을 밝힘')
rep('sections.related_species',sec('related_species'),'body',"'P. adiposa 복합체'로 묶였고","'P. adiposa 복합체'로 묶였고(구성 종 학명은 전문 도구에서 빠져 웹 검색 요약으로 확인)",'[2] 구성 종 이름이 웹 검색 요약뿐임을 본문에도 밝힘')
C={c['name']:c for c in d['compounds']}
c=C['Ergosta-4,6,8(14),22-tetraen-3-one']
rep('compounds.ETO.activity_ko',c,'activity_ko','당뇨 생쥐에서 공복혈당','당뇨 모델 동물(초록에 종 명시 없음)에서 공복혈당','[9] 초록은 동물 종을 밝히지 않음')
c=C['Adenosine']
rep('compounds.Adenosine.activity_ko',c,'activity_ko','생쥐 복강 주사(50 mg/kg, 7일) 후 비장 IL-10 mRNA 1.5배, SOD 1.6배 증가, IL-2·IL-6·IFN-γ 감소','생쥐 복강 주사(50 mg/kg, 7일) 뒤 LPS 자극 시 비장 IL-10 mRNA 1.5배·SOD mRNA 1.6배 증가, IL-2·IL-6·IFN-γ mRNA 49.0%·56.9%·73.4%로 감소','[6] 전문: LPS 자극 모델, mRNA 수준 값')
for n in ['Methyl gallate','Pholiota adiposa lectin']:
    rep(f'compounds.{n}.part',C[n],'part','자실체로 추정(초록에 부위 명시 없음)','부위 원문 확인 못함(초록)','부위를 추정으로 쓰지 않음')
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('/home/user/hfoodguide-wave3/docs/materials/pholiota-adiposa/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
