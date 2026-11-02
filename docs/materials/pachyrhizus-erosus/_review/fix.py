import json
p='/home/user/hfoodguide-wave3/docs/materials/pachyrhizus-erosus/dossier.json'
d=json.load(open(p))
changes=[]
def rep(where,obj,key,old,new,why):
    s=obj[key]; assert old in s,(where,old); obj[key]=s.replace(old,new); changes.append({"where":where,"before":old,"after":new,"why":why})
S={s['key']:s for s in d['sections']}
d['aliases']=[a for a in d['aliases'] if a!='히카마']
changes.append({"where":"aliases","before":"히카마","after":"(삭제)","why":"출처 없는 별명. 식품원료 목록[1]·종설[12] 어디에도 없음([12]은 한국·중국 이름을 bang kuang 으로 적음)"})
rep('sections.processing',S['processing'],'body','건강한 성인 30명을 무작위로 나눈 시험에서 덩이뿌리 즙 500 mL를 마신 뒤','건강한 성인 30명을 덩이뿌리 즙·구아바 즙·물 세 군(각 10명)으로 무작위 배정한 시험에서 덩이뿌리 즙 500 mL를 마신 군은','[20] 초록: 덩이뿌리 즙 군은 10명뿐(30명은 세 군 합계)')
rep('sections.processing',S['processing'],'body','씨앗을 식품으로 쓰려고 건조·볶기 등으로','Pachyrhizus속 씨앗을 식품으로 쓰려고 건조·볶기 등으로','[23]은 Pachyrhizus sp. 씨앗(종 미특정)을 다룸')
rep('sections.genetics',S['genetics'],'body','이 속의 유전 연구 도구로 핵 마이크로새틀라이트(SSR) 표지 17개가 개발되었고','이 속의 유전 연구 도구로 근연종 P. ahipa에서 핵 마이크로새틀라이트(SSR) 표지 17개가 개발되었고','[11] 전문: 표지는 P. ahipa 시료로 만들고 다른 종에 교차 증폭함')
rep('sections.genetics',S['genetics'],'body','엽록체 DNA와 SSR을 함께 쓴 연구는 재래종이','엽록체 DNA와 SSR을 함께 쓴 연구는 페루 안데스의 근연 재배종(이 종이 아닌 P. tuberosus·P. ahipa 계통) 재래종이','[13]은 P. erosus가 아닌 안데스 Pachyrhizus 재래종 연구 — 근연종 자료 섞임 방지')
rep('sections.genetics',S['genetics'],'body','육종 쪽에서는 씨앗의 독성 폴리페놀인','육종 쪽에서는 Pachyrhizus속(여러 종·계통) 씨앗의 독성 폴리페놀인','[4]는 Pachyrhizus sp. 씨앗 100여 시료(종 구분 없음)')
rep('sections.related_species',S['related_species'],'body','페루 안데스의 재배 계통을 분석한 연구는','페루 안데스의 근연 재배종(이 종이 아닌 P. tuberosus·P. ahipa 계통)을 분석한 연구는','[13]의 대상 종 명시')
rep('sections.cultivation',S['cultivation'],'body','페루 시험 포장에서는 2010년 새로운 포티바이러스인 Yam bean mosaic virus가 보고되었다[15]','2010년 페루 시험 포장의 yam bean(Pachyrhizus spp.)에서 바이러스 병징이 나타났고, 새 포티바이러스로 확인되어 Yam bean mosaic virus로 이름 붙었다[15]','[15]: 2010년은 병징 관찰 연도(논문은 2012년), 대상은 Pachyrhizus spp.')
rep('sections.safety',S['safety'],'body','먹어서는 안 되는 부위다[2, 12]','먹어서는 안 되는 부위다[2, 6, 12]','[6]: 덩이뿌리 외 성숙 꼬투리·씨앗·잎이 독성이라고 명시 — 근거 보강')
rep('sections.safety',S['safety'],'body','중독된 사례가 여러 차례 보고되었다[5–9]','중독된 사례가 사망 1례를 포함해 여러 차례 보고되었다[5–9]','[6] 사망 사례')
rep('sections.safety',S['safety'],'body','콩처럼 조리해 먹지 말아야 한다[6, 12]','콩처럼 조리해 먹지 말아야 한다[5, 6, 12]','[5]: 씨앗으로 끓인 국을 먹고 집단 중독')
C={c['name']:c for c in d['compounds']}
rep('compounds.Rotenone',C['Rotenone'],'content_text','씨앗 0.58 mg/g 미만~3.53 mg/g(100여 시료)[4]','Pachyrhizus속 씨앗 0.58 mg/g 미만~3.53 mg/g(종 구분 없는 100여 시료)[4]','[4]는 Pachyrhizus sp. 씨앗')
rep('compounds.Pachyrrhizine',C['Pachyrrhizine'],'content_text','씨앗 0.25 mg/g 미만~3.29 mg/g[4]','Pachyrhizus속 씨앗 0.25 mg/g 미만~3.29 mg/g(종 구분 없는 100여 시료)[4]','[4]는 Pachyrhizus sp. 씨앗')
a=d['assays']
changes.append({"where":"assays[2].conditions.column","before":a[2]['conditions']['column'],"after":"","why":"[2] 로테논 분석 절은 '같은 크로마토그래프'만 적고 칼럼은 명시하지 않음 — 원문에 없는 칸 삭제"})
a[2]['conditions']['column']=''
rep('assays[2].rationale',a[2],'rationale','전문(Methods) 확인 — 칼럼은 같은 장비 설명에서 옮겼고, 유속·정량한계·회수율은 본문에 없음[2].','전문(Methods) 확인 — 같은 HPLC 장비로 분석했다고만 적어 칼럼·유속·정량한계·회수율은 본문에 없음[2].','원문에 없는 칼럼 추정 제거')
rep('assays[3].part',a[3],'part','씨앗(비식용 부위)','씨앗(비식용 부위, Pachyrhizus속 여러 계통)','[4]는 종 구분 없는 Pachyrhizus sp.')
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('/home/user/hfoodguide-wave3/docs/materials/pachyrhizus-erosus/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
