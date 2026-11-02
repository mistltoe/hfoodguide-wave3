import json,sys
p='dossier.json'; d=json.load(open(p))
changes=[]
def rep(where,obj,key,old,new,why):
    s=obj[key]
    assert old in s,(where,old)
    obj[key]=s.replace(old,new); changes.append({"where":where,"before":old,"after":new,"why":why})
sec={s['key']:s for s in d['sections']}
rep('sections.overview',sec['overview'],'body','유럽에서는 꽃을 설탕과 달걀흰자로','꽃은 설탕과 달걀흰자로','[4] 는 식용 방식을 소개하나 지역을 유럽으로 한정하지 않음')
rep('sections.safety',sec['safety'],'body','따라서 물푸레나무과 꽃가루 알레르기가 있는 사람은 꽃을 먹을 때 주의하는 것이 좋다고 보이나, 꽃을 먹어서 생긴 알레르기 사례 보고는 확인하지 못함.','다만 이는 꽃가루(흡입) 알레르겐 자료이며, 꽃을 먹었을 때 교차 반응이 생기는지와 섭취로 생긴 알레르기 사례 보고는 확인하지 못함.','[23] 은 재조합 꽃가루 알레르겐의 면역학적 교차성만 다룸 — 섭취 시 주의 권고는 출처에 없는 추론')
rep('sections.safety',sec['safety'],'body','꽃·잎의 루틴·퀘르세틴 3-글루코사이드·액테오사이드가 생쥐 꼬리 혈류 감소를 막았다는 결과도 동물 실험이다[7].','꽃과 잎의 메탄올 추출물(100 mg/kg, 경구)이 달걀흰자 라이소자임 감작 생쥐의 꼬리 혈류 감소를 줄였고, 잎 추출물에서 분리한 퀘르세틴 3-글루코사이드·루틴·액테오사이드(10 mg/kg)가 활성 성분으로 제시되었으나 이는 동물 실험이다[7].','[7] 전문: 활성 성분은 잎 추출물(LSV)에서 분리됨 — 꽃에서 분리한 것이 아님')
rep('sections.genetics',sec['genetics'],'body','RAPD 표지로 시험관 보존 품종 46점을 대조해 품종을 확인하는 방법이 제안되었다[20]','시험관 보존 수집품 46점(미세클론과 기준 품종)의 RAPD 유형을 비교했으나 직접 대조로는 확인이 어려워, 기준 품종과의 상대 유전 거리로 확인하는 방법이 제안되었다[20]','[20] 초록: 미세클론과 기준 품종의 RAPD 유형이 자주 달라 직접 비교가 불가능했다고 씀')
rep('sections.genetics',sec['genetics'],'body','S. oblata 계통과의 교잡 육종이 시도되고 있다[18]','S. oblata 아종을 모계로 한 교잡이 권고되었다[18]','[18] 초록: S. oblata 아종을 모계로 두 종을 교잡하는 것이 바람직하다고 권고')
C={c['name']:c for c in d['compounds']}
rep('compounds.Acteoside.content_text',C['Acteoside'],'content_text','메탄올 추출 꽃 2.48%(검증된 방법으로 정량)[2]; 70% 에탄올 꽃 추출물 9,408.78 μg/g[3]','메탄올 추출 꽃 2.48%(검증된 방법으로 정량; 초록에 기준(건조 꽃/추출물) 표기 없음)[2]; 70% 에탄올 꽃 추출물 9,408.78 μg/g(클로로젠산 당량, 방법 절은 식물 재료 g당으로 표기)[3]','[3] 방법: 페닐프로파노이드는 클로로젠산 검량선 당량, 식물 재료 g당 — 실제 단일 표준품 정량 아님')
rep('compounds.Acteoside.activity_ko',C['Acteoside'],'activity_ko','생쥐 꼬리 혈류 감소를 막은 활성 성분(동물)[7]','생쥐 꼬리 혈류 감소를 막은 활성 성분(동물, 잎 추출물에서 분리)[7]','[7] 분리 출처는 잎')
rep('compounds.Rutin.activity_ko',C['Rutin'],'activity_ko','생쥐 꼬리 혈류 감소를 막은 활성 성분(동물)[7]','생쥐 꼬리 혈류 감소를 막은 활성 성분(동물, 잎 추출물에서 분리)[7]','[7] 분리 출처는 잎')
rep('compounds.Rutin.content_text',C['Rutin'],'content_text','퀘르세틴 루티노사이드 7,642.07 μg/g[3]','퀘르세틴 루티노사이드 7,642.07 μg/g(루틴 당량)[3]','[3] 방법: 플라보노이드는 루틴 당량')
q=C['Quercetin 3-O-glucoside']
rep('compounds.Quercetin 3-O-glucoside.part',q,'part','꽃·잎','잎(활성 성분 분리 부위; 꽃 함량 미확인)','[7] 에서 이 성분은 잎 추출물에서 분리됨')
rep('compounds.Quercetin 3-O-glucoside.activity_ko',q,'activity_ko','(동물)[7]','(동물, 잎 추출물에서 분리)[7]','[7] 분리 출처는 잎')
for nm,old,new in [('Nuzhenide','70% 에탄올 꽃 추출물 15,893.68 μg/g[3]','70% 에탄올 꽃 추출물 15,893.68 μg/g(올레유로페인 검량선 당량)[3]'),
 ('Syringin','70% 에탄올 꽃 추출물 14,653.98 μg/g, 나무껍질 74,535.30 μg/g[3]','70% 에탄올 꽃 추출물 14,653.98 μg/g, 나무껍질 74,535.30 μg/g(클로로젠산 당량)[3]'),
 ('Demethyloleuropein','70% 에탄올 꽃 추출물 35,729.89 μg/g[3]','70% 에탄올 꽃 추출물 35,729.89 μg/g(올레유로페인 검량선 당량)[3]'),
 ('Secologanoside','70% 에탄올 꽃 추출물 27,663.00 μg/g[3]','70% 에탄올 꽃 추출물 27,663.00 μg/g(올레유로페인 검량선 당량)[3]')]:
    rep(f'compounds.{nm}.content_text',C[nm],'content_text',old,new,'[3] 방법: 계열 대표 표준품 검량선 당량값')
for nm in ['Echinacoside','Oleuropein']:
    pass
A=d['assays'][1]
rep('assays[1].content',A,'content','(원문 단위 μg/g; 건조 꽃 기준인지 추출액 기준인지 원문이 분명하지 않음)','(계열 표준품 당량, μg/g; 방법 절은 \'식물 재료(공기 건조) g당\'으로 표기하나 결과 본문은 \'꽃 추출물\' 값으로 제시해 기준이 완전히 분명하지는 않음)','[3] 3.3절: expressed as equivalents/g plant material')
rep('assays[1].conditions.standard',A['conditions'],'standard','검량선으로 당량 환산','검량선으로 당량 환산(원문은 이리도이드 결과 단위를 \'클로로젠산 당량\'으로도 적어 표기가 엇갈림)','[3] 3.3절 원문 표기')
A2=d['assays'][2]
rep('assays[2].content',A2,'content','누즈헤나이드 0.42%[2]','누즈헤나이드 0.42%(초록 값; 건조 원료/추출물 기준 표기 없음)[2]','[2] 초록에 기준 없음')
S={s['n']:s for s in d['sources']}
fix={8:("Extract from Syringa vulgaris L. Flowers — Evaluation of Antioxidant Properties and Modulation of Coagulation Process in Human Plasma In Vitro. Nutrients 2026;18(7):1022 (doi:10.3390/nu18071022)","Extract from Syringa vulgaris L. Flowers—A Special Emphasis on Its Biological Activity: Evaluation of Antioxidant Properties and Modulation of Coagulation Process in Human Plasma In Vitro. Nutrients 2026;18(7):1022 (doi:10.3390/nu18071022)"),
 15:("J Hist Biol 2021 (","J Hist Biol 2021;54(2):311-340 ("),
 18:("2021;25(5) (","2021;25(5):534-542 ("),
 19:("Mycologia 2017 (","Mycologia 2017;109(3):485-494 ("),
 21:("Genet Mol Biol 2026 (","Genet Mol Biol 2026;49(3):e20260016 ("),
 22:("Plant J 2022 (","Plant J 2022;111(3):836-848 ("),
 27:("Nat Prod Res 2018 (","Nat Prod Res 2019;33(11):1664-1669 (")}
for n,(o,nw) in fix.items():
    rep(f'sources[{n}].title',S[n],'title',o,nw,'PubMed 서지 정보 보완/정정')
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
