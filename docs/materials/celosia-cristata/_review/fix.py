import json
p='/home/user/hfoodguide-wave3/docs/materials/celosia-cristata/dossier.json'
d=json.load(open(p))
changes=[]
def rep(where,obj,key,old,new,why):
    s=obj[key]
    assert s.count(old)==1,(where,old)
    obj[key]=s.replace(old,new); changes.append({"where":where,"before":old,"after":new,"why":why})
S={s['key']:s for s in d['sections']}
rep('sections.overview',S['overview'],'body','수용성 색소인 베탈레인(주로 아마란틴)에서 나온다[3, 4]','수용성 색소인 베탈레인(베타시아닌인 아마란틴 등)에서 나온다[3, 4]','[3]은 아마란틴을 말하지 않고 [4] 초록도 꽃차례의 주 색소라고 쓰지 않음 — "주로"는 캘러스 결과[5]를 옮긴 것')
rep('sections.history',S['history'],'body','자궁 출혈·대하·위장 감염 같은 출혈성 질환에 처방했다','자궁 출혈·대하 같은 출혈성 질환과 위장 감염에 처방했다','[6] 초록은 출혈성 질환과 위장 감염을 따로 적음(위장 감염은 출혈성 질환이 아님)')
rep('sections.biology',S['biology'],'body','잎에서는 분자량 25·27 kDa인 항바이러스 당단백질(CCP-25·CCP-27)이 분리되었고, 그 농도는 개화 전과 개화 후에 달랐다[22].','잎에서는 항바이러스 당단백질 CCP-25·CCP-27이 보고되었고[13], 그 발현은 생육 단계에 따라 다르다고 보고되었다[22].','[22] 원문·초록을 열지 못해 분자량·개화 전후 농도 차이는 확인 불가 — 제목과 [13] 서론으로 확인되는 범위로 줄임')
rep('sections.related_species',S['related_species'],'body','개맨드라미 연구(4배체 2n=36, 엽록체 유전체)는','개맨드라미 연구(4배체 2n=4x=36, 엽록체 유전체)는','[25] 초록 표기대로')
rep('sections.cultivation',S['cultivation'],'body','꽃·씨앗 시료의 총페놀이 건물 1 g당 11.73–18.06 mg GAE로 계통에 따라 달랐다[20].','꽃과 씨앗을 시료로 쓴 분석에서 총페놀이 건물 1 g당 11.73–18.06 mg GAE로 계통에 따라 달랐다(초록에는 부위별 값 구분이 없고, 씨앗은 식품 사용 부위가 아님)[20, 1].','[20] 초록은 꽃과 씨앗을 함께 시료로 적고 부위별 값을 나누지 않음 — 꽃 값처럼 읽히지 않게 밝힘')
rep('sections.genetics',S['genetics'],'body','맨드라미 뿌리끝 분열조직의 평균 염색체 수는 조직배양 조건에 따라 33.23–42.07개로 세어졌고, 저자들은 정상 시험관 묘의 값(36.05)이 기존 보고와 맞는다고 적었다[10].','맨드라미 뿌리끝 분열조직의 평균 염색체 수는 자연 상태에서 키운 식물이 33.23개, 시험관 묘가 36.05–42.07개(시험관 개화 묘 42.07)로 세어졌고, 저자들은 정상 시험관 묘의 값(36.05)이 기존 보고와 맞는다고 적었다[10].','[10] 전문: 33.23은 시험관 밖(in vivo) 식물 값이고 조직배양 조건 값이 아님')
rep('sections.genetics',S['genetics'],'body','개맨드라미는 4배체(2n=4x=36)로 보고되어 있어 맨드라미의 값과 비슷한 수준이다[10, 25].','근연종 개맨드라미는 4배체(2n=4x=36)로 보고되어 있다[25].','[10]은 개맨드라미를 다루지 않음 — 두 종 수치 비교는 출처 없는 종합이라 지우고 [25]만 남김')
rep('sections.genetics',S['genetics'],'body','잎의 항바이러스 단백질 CCP-25·CCP-27은 개화 전과 후에 농도가 달라, 생육 단계에 따라 발현이 바뀌는 것으로 보인다[22].','잎의 항바이러스 단백질 CCP-25·CCP-27은 생육 단계에 따라 발현이 달라진다고 보고되었다(세부 수치는 확인하지 못함)[22].','[22] 원문 확인 불가 — 제목 범위로 줄임')
rep('sections.genetics',S['genetics'],'body','깃털맨드라미(C. argentea)에서 해독되었으며','plumed cockscomb으로 소개된 개맨드라미(C. argentea)에서 해독되었으며','[24] 초록은 학명을 C. argentea로만 적음(변종 plumosa 명시 없음)')
rep('sections.safety',S['safety'],'body','맨드라미 씨앗은 약전 약재인 청상자와 혼동되어 유통되므로 씨앗을 식품이나 약재로 쓰지 않도록 주의해야 한다[7].','맨드라미 씨앗은 공정서 약재가 아닌데도 시장에서 청상자로 팔리는 일이 많다고 보고되었다[7]. 씨앗은 식품원료 사용 부위가 아니다[1].','[7]은 두 씨앗을 구분해 따로 쓰라고 했을 뿐 "식품이나 약재로 쓰지 말라"고 하지 않음 — 식품 쪽 근거는 [1]로 나눔')
C={c['name']:c for c in d['compounds']}
rep('compounds.Amaranthin.activity_ko',C['Amaranthin'],'activity_ko','꽃의 붉은 자주색을 내는 주 색소[4, 5]','붉은 자주색 베타시아닌; 꽃차례에서 확인[4], 캘러스의 주 베타시아닌[5]','"꽃의 주 색소"는 [4] 초록에 없음, "주"는 캘러스[5] 결과')
rep('compounds.Dopamine.activity_ko',C['Dopamine'],'activity_ko','지적[4, 5]','지적[4]','독성학적 언급은 [4]에만 있음')
C['Dopamine']['source']=[4,5]
rep('compounds.Total phenolics.content_text',C['Total phenolics'],'content_text','47.29 mg GAE/g(추출물)[2]; EMS 돌연변이 계통 꽃·씨앗 11.73–18.06 mg GAE/g 건물[20]','47.29 mg GAE/g(추출물)[2]','[20] 값은 꽃·씨앗 혼합 시료(부위별 구분 없음)라 꽃 추출물 항목에 함께 둘 수 없음 — 재배 절에만 남김')
C['Total phenolics']['source']=[2]
rep('compounds.Cristatone II.activity_ko',C['Cristatone II'],'activity_ko','HeLa·BGC-823 암세포에 IC50 23.82 μM(세포 실험)[17]','HeLa·BGC-823 암세포 시험에서 IC50 23.82 μM(세포 실험)[17]','초록은 어느 세포주 값인지 나누지 않음')
src={s['n']:s for s in d['sources']}
def st(n,old,new,why):
    rep(f'sources[{n}].title',src[n],'title',old,new,why)
st(6,'2024;330:118325','2024;332:118325','PubMed(PMID 38740106) 권호는 332')
st(9,'2022;215:114802','2022;216:114802','PubMed(PMID 35500383) 권호는 216')
st(15,'(Ecotoxicol Environ Saf 2018)','(Ecotoxicol Environ Saf 2018;162:35-41)','PubMed(PMID 29960120) 서지 보충')
st(18,'(Int J Biol Macromol 2021)','(Int J Biol Macromol 2021;191:679-688)','PubMed(PMID 34571127) 서지 보충')
st(22,'초록 확인','제목만 확인(PubMed 미수록, 원문 열지 못함)','PubMed 미수록·doi.org 차단으로 초록 확인 불가')
for s in d['sources']: s['accessed']=s['accessed'] if s['n']==1 else s['accessed']
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('/home/user/hfoodguide-wave3/docs/materials/celosia-cristata/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
