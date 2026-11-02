import json,sys
p='dossier.json'; d=json.load(open(p))
changes=[]
def sec(k): return next(s for s in d['sections'] if s['key']==k)
def rep(where,obj,key,old,new,why):
    t=obj[key]; assert old in t,(where,old); obj[key]=t.replace(old,new); changes.append({"where":where,"before":old,"after":new,"why":why})
rep('sections.history',sec('history'),'body','유럽에서는 아직 잘 알려지지 않은 과일이지만','원산지 밖에서는 아직 잘 알려지지 않은 과일이지만',"[2] 초록은 'largely unknown outside its native regions'라고 씀(유럽 한정 아님)")
rep('sections.biology',sec('biology'),'body','재배 루로는 자가수분 성향과 작물화 과정 때문에 유전적 기반이 좁고 동형접합성이 높은 것으로 보고된다[4].','재배 루로는 야생 Lasiocarpa 종보다 대립유전자 다양성이 낮아 유전적 기반이 좁으며, 저자들은 자가수분과 작물화 과정의 선발을 원인으로 들었다[4].',"[4]에서 '동형접합성이 높다(homozygosity due to autogamy)'는 나무토마토(S. betaceum)에 대한 서술임 — 근연종 자료 섞임")
rep('sections.biology',sec('biology'),'body','종간교잡 후대 21개 재료의 과일 무게는 41.48–114.81 g, 과육 수율은 92% 이상, 당도는 7.0–13.0 °Brix, pH는 3.02–3.54였다[3].','종간교잡 후대와 야생 근연종 1점을 포함한 21개 재료의 과일 무게는 41.48–114.81 g(최저값은 야생 근연종), 과육 수율은 92% 이상, 당도는 7.0–13.0 °Brix(최고값은 야생 근연종), pH는 3.02–3.54였다[3].',"[3] 전문: 41.48 g·13.0 °Brix는 야생 근연종(Sh.3.89) 값이며 21개 재료에 야생 근연종이 포함됨")
rep('sections.related_species',sec('related_species'),'body','코코나(Solanum sessiliflorum)','Cocona(Solanum sessiliflorum)',"식약처 목록의 원료명은 'Cocona열매·Cocona잎'(로컬 I1020 원자료)")
rep('sections.cultivation',sec('cultivation'),'body','에콰도르에서는 기존 재배 방식이 산림 벌채와 대규모 토양 황폐화를 일으키고 식물을 병해충에 약하게 만든다는 지적이 있다[17].','주산지(에콰도르·콜롬비아·중앙아메리카)의 현재 재배 방식이 산림 벌채와 대규모 토양 황폐화를 일으키고 식물을 병해충에 약하게 만든다는 지적이 있다[17].',"[17] 초록은 에콰도르로 한정하지 않고 주 재배지 전반의 재배 방식을 말함")
s=sec('safety')
rep('sections.safety',s,'body','에콰도르 국립농업연구소의 종간교잡 후대 21개 재료 과육을 HPLC로 분석한 결과 α-솔라닌은 0.16–4.35 mg/100 g, α-차코닌은 최고 19.60 mg/100 g이었다[3]. 저자들은 나란히야의 글리코알칼로이드 최대 기준이 없고 측정값이 감자에서 보고된 한도 200 mg/kg보다 낮다고 해석했으나, 결과의 생·건물 기준은 원문에 밝혀져 있지 않다[3].',
 '에콰도르 국립농업연구소 육종 프로그램의 Lasiocarpa 절 종간교잡 재료 21점(야생 근연종 1점 포함)의 동결건조 과육을 HPLC로 분석한 결과 α-솔라닌은 0.16–4.35 mg/100 g, α-차코닌은 최고 19.60 mg/100 g이었다[3]. 이 값은 재배 품종 루로 열매가 아니라 교잡 후대 재료의 값이며, 결과가 생과·건물 중 어느 기준인지 원문에 밝혀져 있지 않다[3]. 저자들은 나란히야의 글리코알칼로이드 최대 기준이 없고 측정값이 감자에서 보고된 한도 200 mg/kg보다 낮다고 해석했으나, 최고 α-차코닌 값만 환산해도 196 mg/kg으로 이 한도에 가깝고 두 성분의 합계는 제시되지 않아 이 해석은 그대로 받아들이기 어렵다(검토자 환산)[3].',
 "[3]은 교잡 후대(야생 근연종 포함) 값이고 기준(생/건) 미상; 19.60 mg/100 g=196 mg/kg으로 '200 mg/kg보다 낮아 위험 없음' 해석이 경계값에 걸림을 명시")
rep('sections.safety',s,'body','파종 6주 어린 식물을 쓴','아주심기 6주 뒤 어린 식물을 쓴',"[27] 전문: 'At 6 weeks after transplanting, plants were harvested'")
# compounds
for c in d['compounds']:
    if c['name']=='alpha-Solanine':
        old=c['content_text']; c['content_text']='0.16(P29)–4.35(P17) mg/100 g(종간교잡 재료 21점·야생 근연종 1점 포함의 동결건조 과육 분석, 생·건물 기준 원문에 없음; 순수 재배 루로 값 아님)'
        changes.append({"where":"compounds.alpha-Solanine.content_text","before":old,"after":c['content_text'],"why":"교잡 후대 값임을 분명히"})
    if c['name']=='alpha-Chaconine':
        old=c['content_text']; c['content_text']='재료 간 차이가 컸고 최고 19.60 mg/100 g(TP 재료; 종간교잡 재료 21점·야생 근연종 1점 포함; 생·건물 기준 원문에 없음; 순수 재배 루로 값 아님)'
        changes.append({"where":"compounds.alpha-Chaconine.content_text","before":old,"after":c['content_text'],"why":"교잡 후대 값임을 분명히"})
for a in d['assays']:
    if a['compound'].startswith('Glycoalkaloids'):
        old=a['part']; a['part']='열매 과육(Lasiocarpa 절 종간교잡 재료 21점, 야생 근연종 1점 포함; 순수 재배 루로 아님)'
        changes.append({"where":"assays.glycoalkaloids.part","before":old,"after":a['part'],"why":"[3] 재료 구성"})
    if a['compound']=='Tocopherols':
        o="본문의 껍질 총 토코페롤 '13.0 g/100 g fw'는 mg 단위의 오기로 보인다[2]."
        n="본문의 껍질 총 토코페롤 '13.0 g/100 g fw'는 α 7.9 + δ 5.12 = 13.0 mg/100 g fw와 맞아 mg 단위의 오기로 보인다[2]."
        rep('assays.tocopherols.rationale',a,'rationale',o,n,"합계로 오기 근거 보강(문서 값은 mg 그대로)")
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
