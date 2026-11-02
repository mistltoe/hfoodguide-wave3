import json
p='dossier.json'; d=json.load(open(p,encoding='utf-8'))
S={s['key']:s for s in d['sections']}
changes=[]
def rep(key,old,new,why):
    b=S[key]['body']; assert b.count(old)==1,(key,old); S[key]['body']=b.replace(old,new)
    changes.append({"where":f"sections.{key}","before":old,"after":new,"why":why})

rep('overview',"으름덩굴(Akebia quinata (Houtt.) Decne.)은 으름덩굴과(Lardizabalaceae)에 속하는 덩굴성 목본으로 한국·중국·일본 등 동아시아에 분포한다[19].",
 "으름덩굴(Akebia quinata (Houtt.) Decne.)은 으름덩굴과(Lardizabalaceae)에 속하는 덩굴성 목본으로 한국·중국·일본 등 동아시아에 분포한다[14][19].",
 "[19] 는 명명자를 (Thunb.) Decne. 로 적음 — (Houtt.) Decne. 표기는 [14] 가 뒷받침해 출처 추가")
rep('overview',"영어로는 chocolate vine 또는 five-leaf akebia라 부르며, 열매는 과일로 먹고 전통 의약에도 쓰인다[18][19].",
 "영어로는 chocolate vine이라 부르고 논문에서는 five-leaf akebia라고도 하지만, 식품원료 목록의 'Five-leaf akebia'는 잡종 Akebia x pentaphylla를 가리키므로 구별해야 한다[2][18][19]. 열매는 과일로 먹고 전통 의약에도 쓰인다[19].",
 "영문명 five-leaf akebia 가 식품원료 목록에서는 A. x pentaphylla 원료명이라 근연종과 섞일 수 있음(I1020 원자료 대조); '과일로 먹는다'는 [19] 초록에만 있음")
rep('overview',"사람 대상 연구는 발효 잎·열매 추출 음료의 숙취 시험(남성 25명) 하나가 확인되었다[21].",
 "먹는 형태의 사람 시험은 발효 잎·열매 추출 음료의 숙취 시험(남성 25명을 5개 군으로 나눔) 하나가 확인되었고, 위약군과의 혈중 에탄올 차이는 통계적으로 유의하지 않았다[21].",
 "[35] 에 바르는 크림 사람 시험이 따로 있어 '사람 연구 하나'는 부정확; [21] 은 3시간 시점 대조군과 유의차 없음이라 효과 과장 방지")
rep('overview',"목통(木通)이라는 약재 이름 때문에 아리스톨로크산이 든 관목통(등칡, Aristolochia manshuriensis)과 섞여 쓰인 사고가 있어 구분이 중요하다[4][6].",
 "목통(木通)이라는 약재 이름 때문에 아리스톨로크산이 든 관목통(등칡, Aristolochia manshuriensis)이 대용·혼입되어 콩팥 손상이 생긴 사례가 있어 구분이 중요하다[4][5][7].",
 "[6] 은 'Mu Tong' 섭취와 말기신부전의 연관만 보고하고 혼입 사실은 [5](관목통이 섞인 목통 처방)·[7](관목통 사망 증례)이 직접 말함")

rep('related_species',"식품원료 목록에 따로 올라 있으며 각각 열매·잎을 쓸 수 있다[2].",
 "식품원료 목록에 따로 올라 있으며 각각 열매·잎을 쓸 수 있다[2][12].",
 "A. x pentaphylla 를 잡종으로 보는 근거는 I1020 목록이 아니라 [12] 초록")
rep('related_species',"으름덩굴 줄기에서는 구아이아닌 N·콜린소니딘·칼로파낙스사포닌 A 같은 올레아난 이당 사포닌도 분리되었다[25].",
 "으름덩굴 부탄올 추출물에서는 구아이아닌 N·콜린소니딘·칼로파낙스사포닌 A 같은 올레아난 이당 사포닌도 분리되었다[25].",
 "[25] 초록은 부위를 적지 않고 'n-BuOH extract of Akebia quinata' 라고만 씀")
rep('related_species',"이름이 비슷한 관목통(關木通)은 쥐방울덩굴과의 등칡(Aristolochia manshuriensis) 줄기로, 콩팥 독성 성분인 아리스톨로크산을 함유한다[4][9].",
 "이름이 비슷한 관목통(關木通)은 쥐방울덩굴과의 등칡(Aristolochia manshuriensis)에서 얻는 약재로, 콩팥 독성 성분인 아리스톨로크산을 함유한다[4][9].",
 "[4] 는 관목통을 등칡 '뿌리'로 적어 '줄기'라는 단정을 [4] 가 뒷받침하지 않음(부위 차이는 다음 문장에서 다룸)")

rep('processing',"열매를 70% 메탄올로 환류 추출한 뒤 된장 곰팡이(Aspergillus kawachii) 유래 효소로 생물전환한 추출물은 3T3-L1 지방세포와 고지방식 흰쥐에서 전환하지 않은 추출물보다 체중·지방조직 감소 효과가 컸다[22].",
 "열매를 70% 메탄올로 환류 추출한 뒤 된장 곰팡이 유래 효소로 생물전환한 추출물은 3T3-L1 지방세포와 고지방식 흰쥐(군당 6마리, 4주)에서 전환하지 않은 추출물보다 체중·지방조직 감소 효과가 컸다(세포·동물 시험)[22].",
 "[22] 원문(PMC 전문)에서 곰팡이 종명 Aspergillus kawachii 를 확인하지 못함; 동물 시험 규모 명시")

rep('safety',"대만 건강보험 자료 분석에서 목통 누적 섭취 200 g 초과는 말기신부전 위험 증가(오즈비 5.82)와 관련되었고[6], 2004년 이전 관목통이 섞인 목통 처방은 요로상피암 위험 증가와 관련되었다[5].",
 "대만 건강보험 자료 분석에서 아리스톨로크산 혼입이 의심되는 '목통(Mu Tong)' 제품의 누적 섭취 200 g 초과는 말기신부전 위험 증가(오즈비 5.82)와 관련되었고[6], 말기신부전 환자 코호트에서 2004년 이전 관목통이 섞인 목통 처방은 요로상피암 위험 증가와 관련되었다[5].",
 "[6] 의 Mu Tong 은 아리스톨로크산 혼입 의심 제품으로 분석된 것이라 으름덩굴 자체의 위험으로 읽히지 않게 함; [5] 는 ESRD 환자 코호트")

# compounds
for c in d['compounds']:
    if c['name']=='Neochlorogenic acid':
        old=c['activity_ko']; c['activity_ko']="잎 품질 지표 성분; 혈관내피세포 ICAM-1·VCAM-1 억제는 잎 추출물 전체(10 μg/mL)의 결과이며 이 성분 단독 효과는 시험하지 않음(세포)[17]"
        changes.append({"where":"compounds.Neochlorogenic acid.activity_ko","before":old,"after":c['activity_ko'],"why":"[17] 은 추출물로만 활성 시험 — 성분 활성으로 옮겨 적은 과장"})

# aliases / name_en
old=d['name_en']; d['name_en']="Five-leaf chocolate vine (chocolate vine)"
changes.append({"where":"name_en","before":old,"after":d['name_en'],"why":"'five-leaf akebia' 는 식품원료 목록에서 Akebia x pentaphylla 원료명(Five-leaf akebia열매·잎)이라 근연종과 섞임"})
old=list(d['aliases']); d['aliases']=[a for a in d['aliases'] if a!='five-leaf akebia']
changes.append({"where":"aliases","before":json.dumps(old,ensure_ascii=False),"after":json.dumps(d['aliases'],ensure_ascii=False),"why":"같은 이유로 별명에서 제거(본문에서 구별 설명)"})

json.dump(d,open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
json.dump(changes,open('_review/changes.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
for s in d['sections']: print(s['key'],len(s['body']))
