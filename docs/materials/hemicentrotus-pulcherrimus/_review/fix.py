import json
p='/home/user/hfoodguide-wave3/docs/materials/hemicentrotus-pulcherrimus/dossier.json'
d=json.load(open(p))
changes=[]
S={s['key']:s for s in d['sections']}
def rep(where,obj,key,old,new,why):
    assert old in obj[key], (where,old)
    obj[key]=obj[key].replace(old,new); changes.append({"where":where,"before":old,"after":new,"why":why})
rep('sections.overview',S['overview'],'body',"영문명 칸은 비어 있고, 건강기능식품 고시형 원료의 원재료로는 연결되어 있지 않다[1].","영문명 칸은 비어 있다[1]. 이 종을 원재료로 하는 건강기능식품 고시형 원료는 확인하지 못함.","[1] 원료목록 행에는 건강기능식품 고시와의 연결 정보가 없음 — 출처가 말하지 않는 내용")
rep('sections.history',S['history'],'body',"1990년대에는 이 종의 알·정자에서 새로운 당지질과 강글리오사이드 구조가 잇달아 밝혀졌다[10, 11, 12].","1990년대에는 이 종의 알·정자에서 새로운 당지질 구조가 잇달아 밝혀졌고[10, 12], 알 속 강글리오사이드의 분포도 조사되었다[11].","[11] 은 새 구조 보고가 아니라 보라성게 알에서 먼저 알려진 M5 강글리오사이드의 분포 연구")
rep('sections.history',S['history'],'body',"2024년에는 장독 서열로 개선된 유전체가 나왔다","2024년에는 긴 리드(롱리드) 서열로 개선된 유전체가 나왔다","오타('장독') — [16] 은 Oxford nanopore long-read")
rep('sections.history',S['history'],'body',"한국에서는 연안 수질의 독성 시험에 이 종의 배아가 쓰였다[22].","한국 연구에서는 트리부틸주석 독성 시험에 이 종의 배아가 쓰였다[22].","[22] 는 트리부틸주석 노출·회복 시험이며 연안 수질 일반 시험이 아님")
rep('sections.genetics',S['genetics'],'body',"2024년에는 장독 서열로 약 600 Mb를","2024년에는 긴 리드(롱리드) 서열로 약 600 Mb를","오타 — [16] long-read sequencing")
rep('sections.related_species',S['related_species'],'body',"흰수염성게(Tripneustes gratilla)가 따로 실려 있다[2].","흰수염성게(Tripneustes gratilla), 그리고 국문명 없이 학명으로만 실린 Heliocidaris erythrogramma 가 따로 실려 있다[2].","로컬 I1020 원자료에 Heliocidaris erythrogramma 행(수산물·사용가능)이 더 있음")
rep('sections.related_species',S['related_species'],'body',"같은 과의 새치성게, 그리고 보라성게와 함께 21개 염색체를 가진다고 다른 성게 유전체 논문이 적었다[32].","염색체 수준 유전체 비교에서 이 종은 같은 과의 새치성게·Mesocentrotus franciscanus, 그리고 보라성게(Echinometridae)와 함께 염색체가 21개라고 다른 성게 유전체 논문이 적었다[32].","[32] 초록: Strongylocentrotidae 3종과 Echinometridae 보라성게가 21개 — 비교 대상과 맥락을 정확히")
rep('sections.processing',S['processing'],'body',"강글리오사이드는 친수성 상호작용 크로마토그래피-탠덤 질량분석으로 14개 아강을 확인했다[4].","강글리오사이드는 이 종을 포함한 성게 세 종을 함께 친수성 상호작용 크로마토그래피-탠덤 질량분석으로 분석해 세 종 전체에서 14개 아강을 확인했으며, 종별 구분은 초록에 없다[4].","[4] 는 세 종을 합친 결과 — 이 종 단독 값처럼 읽히지 않게")
rep('sections.safety',S['safety'],'body',"4.68 ppb에서 배아 발생을 모두 멈추게 했다[22].","실측 4.68 ppb 이상에서는 모든 배아가 상실배·포배 단계에 머물러 정상 유생이 나오지 않았다[22].","[22] 전문: 4.68 ppb 에서 100% 발생 장애(상실배·포배에 머묾) — '멈춤' 표현을 원문대로")
C={c['name']:c for c in d['compounds']}
rep('compounds[Gangliosides]',C['Gangliosides'],'activity_ko',"Neu5Ac·Neu5Gc·KDN 세 가지 시알산 구조와 14개 아강이 확인되었다[4].","세 성게 종 전체에서 Neu5Ac·Neu5Gc·KDN 세 가지 시알산 구조와 14개 아강이 확인되었다(종별 구분 없음)[4].","세 종 합친 결과임을 명시")
rep('compounds[M5]',C['M5 ganglioside'],'activity_ko',"수정 전에는 알 피질에 많고 수정 뒤 빠르게 줄었다[11]","보라성게 알의 주 강글리오사이드로 먼저 알려졌고(항체도 보라성게 알에서 제작), 이 종 알에서도 주성분이었다. 이 종 알에서 수정 전에는 피질에 많고 수정 뒤 빠르게 줄었다[11]","[11] 초록: M5 는 Anthocidaris crassispina 알의 주 강글리오사이드 — 다른 종 정보 구분")
rep('compounds[Hp-s1]',C['Hp-s1 ganglioside'],'activity_ko',"말똥성게 정자에서 분리된 성분으로,","말똥성게 정자(원문은 Diadema setosum 난소에서도 분리된다고 적음)에서 분리된 성분으로,","[9] 전문 서론: Hp-s1 은 Diadema setosum 난소에서도 분리 — 이 종 고유 성분으로 읽히지 않게")
rep('compounds[1-MA]',C['1-Methyladenine'],'activity_ko',"이 종을 포함한 성게의 생식소 추출물에서 확인되었고 난모세포 성숙을 유도했다[15]","이 종을 포함한 성게·연잎성게 5종의 난소·정소에 들어 있었다. 성숙 유도는 불가사리 난모세포(난소 추출물)와 보라성게 난모세포(1-메틸아데닌)에서 확인했고, 이 종의 난모세포 시험은 초록에 없다[15]","[15] 초록: 성숙 유도 시험은 불가사리·보라성게 난모세포 — 다른 종 결과 섞임 방지")
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open(p.replace('dossier.json','_review/changes.json'),'w'),ensure_ascii=False,indent=1)
print(len(changes))
