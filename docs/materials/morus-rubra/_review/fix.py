import json
p='/home/user/hfoodguide-wave3/docs/materials/morus-rubra/dossier.json'
d=json.load(open(p))
ch=[]
def rep(where,obj,key,old,new,why):
    assert old in obj[key], (where,old)
    obj[key]=obj[key].replace(old,new); ch.append({"where":where,"before":old,"after":new,"why":why})
S={s['key']:s for s in d['sections']}
rep('sections.biology',S['biology'],'body',
 '붉은뽕나무는 미국 동부에 널리 퍼진 빨리 자라는 나무로, 골짜기·범람원의 습한 토양과 해발 약 600 m 이하에서 자란다는 검색 요약이 있으나 원문은 확인하지 못함[8].',
 '붉은뽕나무는 미국 동부에 널리 퍼진 빨리 자라는 나무로, 골짜기·범람원·낮고 습한 산비탈에서 자란다는 검색 요약이 있으나 원문은 확인하지 못함[8]. 해발 고도 범위는 확인하지 못함.',
 '재검색 요약에서 [8] 은 골짜기·범람원·낮고 습한 산비탈만 말하고 해발 600 m 수치는 나오지 않음')
rep('sections.biology',S['biology'],'body',
 '좋은 종자 결실은 2–3년마다 오고 열매는 1 kg에 평균 약 8,600개라는 요약도 원문은 확인하지 못함[8].',
 '좋은 종자 결실은 2–3년마다 오고 열매는 1 kg에 평균 약 8,600개(정선 종자는 1 kg에 약 79만 5천 개)라는 요약도 원문은 확인하지 못함[8].',
 '재검색 요약에서 수치 일치 확인(원문은 여전히 열지 못함), 열매 수와 종자 수를 구분해 적음')
rep('sections.genetics',S['genetics'],'body',
 '북미의 자매종과는 약 993만 년 전에 갈라진 것으로 추정되었다[3].',
 '북미의 자매종과는 약 993만 년 전에 갈라진 것으로 추정되었다(시료는 미국 자생 개체)[3].',
 '시료 출처 명시')
rep('sections.related_species',S['related_species'],'body',
 '북미와 아시아 계통군은 약 2,869만 년 전에 갈라진 것으로 추정되었다[3].',
 '북미와 아시아 계통군은 약 2,869만 년 전(초록은 아메리카·아시아 계통군 2,863만 년 전)에 갈라진 것으로 추정되었다[3].',
 '[3] 본문 28.69 MYA, 초록 28.63 MYA 로 원문 안에서 값이 다름')
rep('sections.safety',S['safety'],'body',
 '쥐 뇌전증 모델의 결과(10 mg/kg)도 동물 실험이라 사람 효과로 옮길 수 없다[20].',
 '부위가 초록에 적히지 않은 추출물로 한 쥐 뇌전증 모델의 결과(유효 용량 10 mg/kg)도 동물 실험이라 사람 효과로 옮길 수 없다[20]. 이 연구들[17][18][19][20]의 시료는 인도·튀르키예에서 얻은 것이라 북미 자생 붉은뽕나무와 같은 종·계통인지는 확인하지 못함.',
 '[20] 초록에 부위 없음, 북미 밖 시료의 종 확인 문제 명시')
rep('sections.safety',S['safety'],'body',
 '잎 연구의 총페놀은 16.21–24.37 mg GAE/g로 보고되었으나 세 종 범위라 이 종만의 값은 확인하지 못함[16].',
 '파키스탄 잎 연구의 총페놀은 16.21–24.37 mg GAE/g로 보고되었으나 세 종 범위라 이 종만의 값은 확인하지 못함(잎은 식품원료 부위 아님)[16].',
 '[16] 시료 지역(파키스탄)과 부위 지위 명시')
C={c['name']:c for c in d['compounds']}
rep('compounds.Epicatechin',C['Epicatechin'],'content_text','같은 유전자형 0.84–99.74 mg/kg','같은 유전자형 0.61–99.74 mg/kg','[10] Table 5 붉은뽕나무 최저는 13HZN17 0.61 mg/kg(0.84는 13HZN27)')
rep('compounds.Rutin',C['Rutin'],'activity_ko','주성분 분석에서 DPPH 항산화능과 가깝게 묶임(시험관)[10]','세 종 39개 유전자형 전체 주성분 분석에서 DPPH 항산화능과 가깝게 놓임(시험관)[10]','[10] PCA 는 흰·붉은·검은 오디 전체 대상')
a=d['assays'][0]
rep('assays[0].content',a,'content','에피카테킨 0.84–99.74 mg/kg','에피카테킨 0.61–99.74 mg/kg','[10] Table 5 최저값 0.61')
rep('assays[0].rationale',a,'rationale','붉은뽕나무 열매의 개별 페놀을 유전자형별로 정량한 자료이며, 루틴·총 안토시아닌·총페놀이 항산화능과 가장 가깝게 묶였다[10].',
 '붉은뽕나무 열매의 개별 페놀을 유전자형별로 정량한 자료이며, 세 종 전체 주성분 분석에서 프로토카테큐산·총 안토시아닌·총페놀·루틴·총 플라보노이드가 DPPH 항산화능과 가장 가깝게 놓였다[10].',
 '[10] 본문: PCA 적재도에서 DPPH 와 가까운 변수는 프로토카테큐산·총 안토시아닌·총페놀·루틴·총 플라보노이드, 세 종 전체 분석')
src={s['n']:s for s in d['sources']}
src[3]['publisher']='Scientific Reports 15:13403 (PubMed PMID 40251250, PMC12008415 전문 확인)'
src[10]['publisher']='Food Science & Nutrition 12(9):6425-6441 (PubMed PMID 39554318, PMC11561804 전문 확인)'
src[12]['publisher']='Scientific Reports 15:31398 (PubMed PMID 40858651, PMC12381166 전문 확인)'
src[8]['title']='Silvics of North America, Vol. 2: Morus rubra L. Red Mulberry (WebSearch 요약으로만 봄 — 원문은 네트워크 허용 목록 밖이라 열지 못함)'
ch.append({"where":"sources[3,10,12,8]","before":"권·쪽 일부 누락","after":"권·쪽 보충, [8] 열지 못한 사유","why":"PubMed 메타데이터 대조"})
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(ch,open('/home/user/hfoodguide-wave3/docs/materials/morus-rubra/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(ch))
