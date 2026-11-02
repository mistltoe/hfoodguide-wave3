import json
p='/home/user/hfoodguide-wave3/docs/materials/vaccinium-bracteatum/dossier.json'
d=json.load(open(p))
S={s['key']:s for s in d['sections']}
changes=[]
def rep(where,obj,key,old,new,why):
    assert old in obj[key],(where,old)
    obj[key]=obj[key].replace(old,new); changes.append({"where":where,"before":old,"after":new,"why":why})
rep('sections.overview',S['overview'],'body',
 "같은 목록에서 블루베리(Vaccinium spp.)·덩굴월귤·월귤나무 행은 잎도 사용가능부위로 적혀 있지만",
 "같은 목록에서 블루베리(Vaccinium spp.)·하이부시블루베리(V. corymbosum)·덩굴월귤·미르틸루스산앵도(V. myrtillus) 행은 잎도 사용가능부위로 적혀 있지만(월귤나무·들쭉나무 행은 열매만)",
 "로컬 I1020 원자료에서 월귤나무(V. vitis-idaea) 행의 사용가능부위는 '열매'뿐이고, 잎이 들어 있는 행은 블루베리·High-bush blueberry·덩굴월귤·미르틸루스산앵도")
rep('sections.cultivation',S['cultivation'],'body',
 "국내 연구에서는 전남 고흥군의 식물원과 자생 개체에서 열매를 구했다[10, 11].",
 "국내 연구에서는 전남 고흥군의 한 식물원에서 열매를 사거나[10], 고흥군의 개체에서 열매를 채취했다[11].",
 "[10] 은 고흥의 식물원에서 구입, [11] 은 'collected from plants in the Goheung County' — 자생 개체라는 표현은 원문에 없음")
rep('sections.safety',S['safety'],'body',
 "벌이 먹은 지역 식물 가운데 하나로 모새나무를 독소의 간접 원인 후보로 들었으나, 이는 가설이다[19].",
 "지역에 흔한 유독 식물(뇌공등속 2종과 모새나무)이 벌 번데기를 거쳐 간접적으로 독소의 원인이 되었을 수 있다고 추정했으나, 이는 가설이다[19].",
 "[19] 초록은 'prevalence of local poisonous plants, such as Tripterygium wilfordii, T. hypoglaucum and V. bracteatum' 이라고만 씀 — 벌이 먹었다는 내용은 없음")
C={c['name']:c for c in d['compounds']}
rep('compounds[p-Coumaric acid].content_text',C['p-Coumaric acid'],'content_text',
 "잎 추출물 에틸아세테이트 분획의 주된 활성 성분으로 동정(함량 없음)[25]; 잎 추출물의 주요 활성 성분[26]",
 "추출물(초록에 부위 기재 없음) 에틸아세테이트 분획의 주된 활성 성분으로 동정(함량 없음)[25]; 잎 추출물의 주요 활성 성분[26]",
 "[25] 초록은 V. bracteatum 추출물이라고만 하고 부위를 밝히지 않음")
rep('compounds[Xanthotoxol].content_text',C['Xanthotoxol'],'content_text',
 "잎 추출물 비표적 대사체 분석에서 핵심 활성 성분으로 선정(함량 없음)[31]",
 "잎 추출물을 먹인 생쥐 혈청의 비표적 대사체 분석에서 핵심 활성 후보로 선정, 추출물 안에서도 상관 대사체 중 가장 많았다고 함(함량 수치 없음)[31]",
 "[31] 전문: 대사체 분석은 생쥐 혈청 대상이었고 함량 수치는 없음")
rep('compounds[Xanthotoxol].activity_ko',C['Xanthotoxol'],'activity_ko',
 "세포 노화 모델에서 Nrf2 경로 활성화[31]",
 "H2O2로 노화를 유도한 HepG2 세포에서 Nrf2 경로 활성화(세포 실험)[31]",
 "[31] 전문: HepG2 세포 모델 — 세포 결과임을 밝힘")
src={s['n']:s for s in d['sources']}
rep('sources[31].title',src[31],'title',"초록만 확인","전문 확인",
 "PMC13114447 전문을 열어 예쁜꼬마선충 생식 독성 없음(산란 수 차이 없음)·HepG2 모델을 확인")
rep('sources[32].title',src[32],'title',
 "— WebSearch 검색 결과 요약으로만 확인, 원문(koreascience)은 이 환경에서 열지 못함",
 "— 한국자원식물학회지 2013, WebSearch 검색 결과로 존재만 확인, 원문(koreascience)은 이 환경에서 열지 못함",
 "검토 중 WebSearch 1회로 논문 존재·학술지·연도 확인")
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('/home/user/hfoodguide-wave3/docs/materials/vaccinium-bracteatum/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
