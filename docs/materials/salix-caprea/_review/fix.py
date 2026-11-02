import json,sys
p='/home/user/hfoodguide-wave3/docs/materials/salix-caprea/dossier.json'
d=json.load(open(p))
changes=[]
def sec(k): return next(s for s in d['sections'] if s['key']==k)
def rep(where,obj,key,old,new,why):
    v=obj[key]
    assert old in v,(where,old)
    obj[key]=v.replace(old,new,1)
    changes.append({"where":where,"before":old,"after":new,"why":why})
S=sec('history')
rep('sections.history',S,'body','유럽 전통의학에서 호랑버들 추출물은','전통의학에서 호랑버들 추출물은','[22] 원문은 "In traditional medicine"이라고만 쓰고 유럽으로 한정하지 않음')
rep('sections.history',S,'body','호랑버들 겨울눈 추출물이','호랑버들 눈(bud) 추출물이','[8] 원문은 bud extracts; 겨울눈으로 한정할 근거 없음')
rep('sections.history',S,'body','이탈리아 칼라브리아의 양치기들은 호랑버들 껍질과 잎을 물에 30일 담근 침출액을 양의 위장관 선충 구제에 써 왔다[22].','이탈리아 칼라브리아의 한 노년 목양 농가는 대대로 전해 온 처방에 따라 호랑버들 껍질과 잎을 끓여 식힌 물에 30일 담근 침출액을 양의 위장관 선충 구제에 썼다[22].','[22] 전문: 105개 농가 설문 중 한 농가가 쓰던 침출액이며 노년 농부가 옛 처방대로 만듦(양치기 일반의 관행으로 일반화된 표현 수정)')
S=sec('biology')
rep('sections.biology',S,'body','추위에 강한 개척종으로 교란지에 먼저 들어오며[14]','추위에 강한 개척종(pioneer species)이며[14]','[14] 초록은 cold-tolerant pioneer species라고만 씀; 교란지 진입 서술은 출처에 없음')
S=sec('related_species')
rep('sections.related_species',S,'body',"흰버드나무(Salix alba L.)와 수양버들(Salix babylonica)은 '사용불가'로 올라 있다[1].","흰버드나무(Salix alba L.)와 수양버들(Salix babylonica)은 '사용불가'로 올라 있다(다만 Salix alba의 변종·품종 행인 Golden willow순추출분말·Cricket bat willow순은 순이 사용가능)[1].",'I1020 원자료에 S. alba var. vitellina·S. alba caerulea 순 행이 사용가능으로 따로 있어 S. alba 전체가 사용불가로 읽히지 않게 보완')
rep('sections.related_species',S,'body',"영국에서는 S. cinerea와 함께 '샐로(sallow)'로 묶여 거래된다[19].","영국산 묘목 위험평가에서 호랑버들과 S. cinerea는 함께 평가되었고 둘 다 'common sallow'라는 영어 이름을 갖는다[19].",'[19] 전문은 두 종의 영어 일반명에 common sallow가 공통으로 있다고만 씀; "묶여 거래된다"는 과장')
S=sec('processing')
rep('sections.processing',S,'body','겨울눈은 추출물(SCBEs)로 만들어 세포 실험에 썼고[8]','눈(bud)은 추출물(SCBEs)로 만들어 생쥐 크롬친화세포 실험에 썼고[8]','[8] 원문은 bud extracts, 실험계는 mouse chromaffin cells')
S=sec('genetics')
rep('sections.genetics',S,'body','금속 적응 유전형의 잎에서는 시스테인 합성 유전자가 늘 더 많이 발현되었다[26].','금속 적응 유전형의 잎에서는 시스테인 합성 유전자 하나가 늘(구성적으로) 더 많이 발현되었다[26].','[26] 초록은 a cysteine biosynthesis gene(1개)이라고 씀')
S=sec('safety')
rep('sections.safety',S,'body','버드나무류 껍질의 살리신(아스피린과 비슷한 작용의 원료 물질)은 이 원료와 부위가 다르다는 점에 유의해야 한다[1, 4].','버드나무류 껍질의 살리신(분자 도킹 계산에서 COX-2 결합 친화도가 아세틸살리실산과 비슷하게 나온 성분)은 나무껍질 성분이며, 식용 부위인 순과는 부위가 다르다는 점에 유의해야 한다[1, 4].','[4] 은 도킹 계산 결과만 말함; "아스피린과 비슷한 작용"은 과장이라 계산 결과로 한정')
rep('sections.safety',S,'body','피부 발암 억제 효과[23]는','피부에 바른 추출물의 발암 억제 효과[23]는','[23] 은 생쥐 피부 도포 실험(0.5–1.5 mg/kg/0.2 ml acetone)')
# compounds
C={c['name']:c for c in d['compounds']}
c=C['Proanthocyanidins']
rep('compounds.Proanthocyanidins.activity_ko',c,'activity_ko','프로시아니딘·프로델피니딘형 탄닌으로 양 위선충 탈피 억제 시험의 모델 탄닌으로 쓰임[25]','호랑버들 잎에서 분리한 탄닌이 양 위선충 탈피 억제 시험관 시험의 모델 탄닌 가운데 하나로 쓰임[25]','[25] 초록은 여러 식물(피나무 꽃·호랑버들 잎·까치밥나무 잎)의 탄닌이 합쳐 PC·PD형을 대표한다고 씀; 호랑버들 탄닌 자체의 PC/PD형은 초록에 없음')
c=C['Hexahydrofarnesyl acetone']
rep('compounds.Hexahydrofarnesyl acetone.class',c,'class','세스퀴테르페노이드 케톤','C18 아이소프레노이드 케톤','6,10,14-트라이메틸펜타데칸-2-온(C18)으로 세스퀴테르페노이드(C15)가 아님')
c=C['1alpha,3beta,25-trihydroxy-9(11)-ene-16-one-9,10-seco-9,19-cyclolanostane']
rep('compounds.triterpene.part',c,'part','부위 미상(저극성 용매 추출물)','꽃으로 색인됨(초록에는 부위 명시 없음, 저극성 용매 추출물)','[24] PubMed MeSH 색인에 Flowers가 있음')
# assays
A=d['assays']
a=A[0]
rep('assays[0].content',a,'content','; S. caprea 수치는 초록에 없음(비교 범위: S. purpurea 0.1–2.6 mg/g, S. alba 3.8–14.7 mg/g)[6]','; S. caprea 수치는 초록에 없음[6]','다른 종(S. purpurea, S. alba) 수치를 이 종 함량 칸에 두면 섞여 읽힘 — 삭제')
rep('assays[0].part',a,'part','잎·당년생 새순(this year\'s sprouts)','잎·당년생 새가지(this year\'s sprouts)','sprouts는 그해 자란 새 줄기로, 식품원료의 순과 같은 것인지 원문으로 확인 못함')
rep('assays[0].rationale',a,'rationale','식용 부위인 순(당년생 새순)을 직접 분석한 유일한 연구로, 호랑버들 잎·순은 살리실레이트보다 축합형 탄닌이 특징적이다; 초록만 확인, 전문 확인 못함[6, 5]','식용 부위인 순에 가까운 당년생 새가지(this year\'s sprouts)를 잎과 함께 분석한 연구이며, 호랑버들 잎은 페놀배당체보다 축합형 탄닌이 많다는 보고가 있다[6, 5]; 초록만 확인, 전문 확인 못함','"유일한 연구"·"순을 직접 분석"은 확인 불가한 과장; [5] 는 잎만 분석')
a=A[2]
rep('assays[2].conditions.instrument',a['conditions'],'instrument','Agilent 1290 Infinity II UHPLC + G6545B Q-TOF MS(이중 ESI)','UHPLC–Q-TOF 질량분석기(이중 ESI 이온원)','상표명 대신 일반명')
# compound Proanthocyanidins part / content consistency
c=C['Proanthocyanidins']
rep('compounds.Proanthocyanidins.part',c,'part','잎·당년생 새순','잎·당년생 새가지','assays 와 같은 표현으로 정리(sprouts)')
rep('compounds.Proanthocyanidins.content_text',c,'content_text','잎과 당년생 새순의','잎과 당년생 새가지의','같은 이유')
# sources
s=d['sources'][28]; assert s['n']==29
rep('sources[29].title',s,'title','BMC Res Notes 2022 (PMID','BMC Res Notes 2022;15(1):317 (PMID','PubMed 서지 정보로 권·호·쪽 보완')
s=d['sources'][21]; assert s['n']==22
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('/home/user/hfoodguide-wave3/docs/materials/salix-caprea/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
