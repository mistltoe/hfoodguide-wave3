import json,sys
p='/home/user/hfoodguide-wave3/docs/materials/geum-japonicum/dossier.json'
d=json.load(open(p))
changes=[]
def sec(k): return [s for s in d['sections'] if s['key']==k][0]
def rep(where,obj,key,old,new,why):
    assert old in obj[key], (where,old)
    obj[key]=obj[key].replace(old,new); changes.append({"where":where,"before":old,"after":new,"why":why})
S=sec('overview')
rep('sections.overview',S,'body','연구는 대부분 말린 전초(지상부와 뿌리를 포함한 식물 전체)나 그 추출물로 이루어졌고, 중국 연구의 상당수는 변종 Geum japonicum var. chinense를 썼다[3, 6, 16, 17].',
 '연구는 대부분 말린 전초(지상부와 뿌리를 포함한 식물 전체)나 지상부, 그 추출물로 이루어졌고, 중국 연구의 상당수는 변종 Geum japonicum var. chinense를 썼다[6, 16, 17].',
 '[3] 은 변종이 아닌 Geum japonicum 으로 적음; [16] 은 전초가 아닌 지상부(aerial part) 95% 에탄올 추출물')
S=sec('history')
rep('sections.history',S,'body','2008년 무렵 한국 연구진도 추출물·분획의 세포 실험 결과를 냈다[20, 21].',
 '2008년 무렵 한국 연구진도 분획과 분리 성분(3,4,5-트라이하이드록시벤즈알데하이드)의 세포 실험 결과를 냈다[20, 21].',
 '[20] 은 추출물이 아니라 분리 성분 THBA, [21] 은 메틸렌클로라이드 분획 실험')
S=sec('biology')
rep('sections.biology',S,'body','뱀무속은 장미과 장미아과(Rosoideae) 콜루리아족(Colurieae)에 속하며','뱀무속은 장미과 콜루리아족(Colurieae)에 속하며','[15] 에 장미아과 언급 없음 — 출처 없는 분류 단계 삭제')
rep('sections.biology',S,'body','뱀무속 식물은 저지대 풀밭과 습한 초지, 숲, 바위 비탈부터 해발 5,400 m 고산 초원까지 다양한 곳에 자란다[15].',
 '뱀무속 식물은 산비탈 풀밭, 습한 초지, 늪, 숲, 바위 비탈, 고산 초원, 북극 툰드라 등 해발 0~5,400 m의 다양한 곳에 자란다[15].',
 '[15] 원문: hillside grasslands, moist meadows, swamps, ... alpine meadows, arctic tundra, 0–5,400 m ("저지대 풀밭"은 원문에 없음)')
S=sec('genetics')
rep('sections.genetics',S,'body','뱀무속 11개 분류군 32개 시료를 비교한 연구에서 엽록체 유전체 크기는 155,175~156,248 bp로',
 '뱀무속 11개 분류군 32개 시료를 다룬 연구에서 비교한 완전 엽록체 유전체 28개의 크기는 155,175~156,248 bp로',
 '[15] 크기 범위는 32개가 아니라 비교 분석한 28개 유전체 기준')
S=sec('safety')
rep('sections.safety',S,'body','전초 추출물과 그 타닌은 시험관에서 트롬빈·Xa 인자를 억제하고, 쥐 혈소판의 응집을 억제했다[5, 7].',
 '전초 메탄올 추출물에서 분리한 타닌은 시험관에서 트롬빈·Xa 인자를 억제했고[7], 전초 50% 에탄올 추출물은 쥐에서 얻은 혈소판의 응집을 시험관에서 억제했다[5].',
 '[7] 은 분리 타닌의 응고효소 억제, [5] 는 추출물의 쥐 세척 혈소판 실험 — 주체·출처를 나눔')
rep('sections.safety',S,'body','생쥐에게 아시클로버와 함께 먹였을 때 독성은 관찰되지 않았다[28].',
 '열수 추출물을 생쥐에게 아시클로버와 함께 먹였을 때 독성은 관찰되지 않았다[28].','[28] 은 열수 추출물(부위 미기재)')
rep('sections.safety',S,'body','중국 연구진은 민간에서 오래 썼어도 부작용 보고는 없지만 더 엄격한 독성 시험이 필요하다고 적었다[6].',
 '변종 var. chinense를 연구한 중국 연구진은 민간에서 오래 썼어도 부작용 보고는 없지만 더 엄격한 독성 시험이 필요하다고 적었다[6].','[6] 은 변종 var. chinense 연구 — 순 결과처럼 읽히지 않게 명시')
c=[x for x in d['compounds'] if x['name']=='Niga-ichigoside F1'][0]
rep('compounds[Niga-ichigoside F1].activity_ko',c,'activity_ko','고지방식 생쥐에 40 mg/kg 투여 시 간 지방 축적 완화(동물 실험)[18]',
 '고지방식 생쥐에 12주간 40 mg/kg(초록 표기, 식이·체중 기준 미기재) 투여 시 간 지방 축적 완화(동물 실험), HepG2 세포에서 Nrf2 경유 지질 축적 억제(세포 실험)[18]',
 '[18] 초록 기간 12주·단위 기준 불명확·세포 실험 병기')
src={x['n']:x for x in d['sources']}
def st(n,old,new,why): rep(f'sources[{n}].title',src[n],'title',old,new,why)
st(16,'Phytochemistry 2023(온라인 게재), 논문번호 113935','Phytochemistry 2024;218:113935(2023년 11월 온라인)','PubMed 서지: 권 218')
st(18,'Food Funct 2018 (PMID','Food Funct 2018;9(2):906-916 (PMID','PubMed 서지 권·쪽 보충')
st(19,'Phytochem Anal 2025 (PMID','Phytochem Anal 2025;36(5):1517-1538 (PMID','PubMed 서지 권·쪽 보충')
st(24,'Zootaxa 2015;4007(1) (PMID','Zootaxa 2015;4007(1):143-8 (PMID','PubMed 서지 쪽 보충')
st(25,'Genet Mol Res 2014 (PMID','Genet Mol Res 2014;13(4):10592-8 (PMID','PubMed 서지 권·쪽 보충')
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('/home/user/hfoodguide-wave3/docs/materials/geum-japonicum/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
