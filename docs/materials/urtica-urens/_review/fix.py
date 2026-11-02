import json
p='docs/materials/urtica-urens/dossier.json'
d=json.load(open(p))
S={s['key']:s for s in d['sections']}
changes=[]
def rep(key,old,new,why):
    b=S[key]['body']; assert old in b,(key,old); S[key]['body']=b.replace(old,new); changes.append({"where":"sections."+key,"before":old,"after":new,"why":why})
rep('overview',"새삼의 변종 학명(Cuscuta japonica var. thyroidea)이 나란히 적혀 있는데, 새삼(Cuscuta japonica Choisy)은 씨앗만 제한적으로 쓰는 별도 원료로 따로 올라 있어 이 병기는 목록 자료의 오기로 보인다[1].",
 "새삼의 변종 학명(Cuscuta japonica var. thyroidea Engelm. / Kom.)이 나란히 적혀 있다[1]. 원자료에는 이 병기의 이유가 적혀 있지 않아 확인하지 못함. 새삼(Cuscuta japonica Choisy)은 씨앗만 '제한적사용'인 별도 원료(새삼씨앗·새삼씨앗가루)로 따로 올라 있으므로, 이 원료(잎)는 Urtica urens로 보고 새삼 자료와 섞지 않는다[1].",
 "원자료 학명란은 세 학명을 '/'로 나열할 뿐 오기라는 근거가 없음 — 추정('오기로 보인다')을 사실 확인 범위로 낮춤")
rep('overview',"잎 추출물에서는 클로로겐산이 주된 폴리페놀로 정량되었고[4][5]","지상부 에탄올 추출물에서는 클로로겐산이 주된 폴리페놀로 정량되었고[4][5]",
 "[4] 전문: 시료는 잎이 아니라 지상부(aerial parts) 80% 에탄올 추출물")
rep('biology',"잎은 큰쐐기풀(U. dioica)보다","잎은 스팅잉네틀(U. dioica)보다","'큰쐐기풀' 국문명은 출처 없음 — 식품원료 목록 대표명 '스팅잉네틀'로 통일")
rep('related_species',"가장 혼동하기 쉬운 종은 큰쐐기풀(스팅잉네틀, Urtica dioica)이다","가장 혼동하기 쉬운 종은 스팅잉네틀(Urtica dioica)이다","'큰쐐기풀' 국문명은 출처 없음")
rep('related_species',"국내 자생 쐐기풀(Urtica thunbergiana)","쐐기풀(Urtica thunbergiana Sieb. et Zucc.)","[1] 은 '국내 자생'을 말하지 않음(학명·사용불가만 확인)")
rep('related_species',"항염 효과는 U. dioica보다 강하게 나왔다고","시험관 항염 효과는 U. dioica보다 강하게 나왔다고","[10] 초록: in vitro 결과임을 명시(세포 결과 과장 방지)")
rep('genetics',"대개 사배체인 큰쐐기풀과 구별된다","사배체로 보고된 영국의 스팅잉네틀(U. dioica subsp. dioica)과 구별된다","[3] 은 U. dioica subsp. dioica 개체가 사배체로 보고되었다고 씀; '큰쐐기풀' 국문명 출처 없음")
rep('processing',"식품으로는 다른 쐐기풀처럼 어린잎을 익혀 나물로 먹으며, 익히면 쐐기털의 자극이 사라지는 것으로 알려져 있다[3].","식품으로는 다른 쐐기풀처럼 어린잎을 익혀 나물로 먹는다[3].",
 "[3] 전문은 '익혀 먹는 나물로 먹을 수 있다'만 쓰고 익히면 자극이 사라진다는 말은 없음")
rep('processing',"말린 잎을 육계 사료에 1%·2% 섞어 먹였고","말린 지상부(줄기·잎 분쇄물)를 육계 사료에 1%·2% 섞어 먹였고","[26] 전문: 12월에 지상부를 50 °C에서 말려 줄기와 잎을 함께 분쇄해 씀")
rep('safety',"따가움과 두드러기를 일으키므로 손질할 때 장갑을 쓰는 것이 좋다[3][19].","따가움과 두드러기(접촉성 두드러기)를 일으킨다[3][19].","장갑 권고는 출처 [3][19]에 없음")
rep('safety',"이 종의 잎을 잘못 사용한 뒤 심한 혀 부종이 생긴 사례 보고가 있다[20]. 다만 초록이 없어 섭취 경위와 용량은 확인하지 못함.",
 "제목에 '쐐기풀(Urtica urens)'로 적힌 약초를 잘못 사용한 뒤 심한 혀 부종이 생긴 증례 보고가 있다[20]. 다만 초록이 없어 사용 부위·섭취 경위·용량은 확인하지 못했고, PubMed 색인어는 Urtica dioica로 달려 있어 기원 종도 분명하지 않다[20].",
 "[20] 은 초록 없음 — '잎'은 확인 불가, MeSH 가 Urtica dioica 로 색인되어 종 혼동 가능성 표시")
rep('safety',"유럽 연구에서는 지상부 추출물이 생리활성 농도(200·350 μg/mL)에서 대식세포와 간세포에 독성을 보이지 않았다[10].","포르투갈 연구의 세포 실험에서는 지상부 추출물이 생리활성 농도(200·350 μg/mL)에서 대식세포와 간세포에 독성을 보이지 않았다[10].","세포 실험임을 명시")
rep('safety',"쥐에 씨앗 추출물을 복강 주사한 실험에서는","쥐에 씨앗 추출물을 투여한 실험(복강 주사, 200 mg/kg/일 4일 등)에서는","[22] 초록: 복강 200 mg/kg/day 4일; [21] 초록은 경로를 밝히지 않음")
rep('safety',"같은 의견서는 EFSA 식물 성분 목록이 이 종의 잎에서 항영양소인 피트산(4730 mmol/kg 건조물)을 우려 성분으로 적었다고 전한다[2].",
 "같은 의견서는 EFSA 식물 성분 목록(Compendium)이 남아프리카 연구[15]를 근거로 이 종의 잎에서 항영양소인 피트산(4730 mmol/kg 건조물, 의견서 표기 그대로)을 우려 성분으로 적었다고 전한다[2].",
 "[2] 전문: Compendium 값의 근거가 Afolayan & Jimoh(=[15])임을 밝힘; 단위는 의견서 표기 그대로라고 명시")
# compounds
for c in d['compounds']:
    if c['name']=='Chlorogenic acid':
        old=c['part']; c['part']='지상부'; changes.append({"where":"compounds.Chlorogenic acid.part","before":old,"after":"지상부","why":"[4][12] 모두 지상부 추출물"})
    if c['name']=='Polyphenols':
        o=c['content_text']; c['content_text']=o.replace("잎 물 추출물 19.20 mg GAE/g 생체중[6]","잎 물 추출물 19.20 mg GAE/g(원문은 생체중 기준이라 표기했으나 시료는 말린 잎 분말)[6]").replace("잎 70% 에탄올 추출물 31.41 mg GAE/g[13]","잎(채집 기록은 지상부) 70% 에탄올 추출물 31.41 mg GAE/g[13]")
        changes.append({"where":"compounds.Polyphenols.content_text","before":o,"after":c['content_text'],"why":"[6] 전문: 말린 잎을 추출했는데 결과는 'fresh weight'로 표기 — 생/건 기준 모호함을 밝힘; [13] 방법은 지상부 채집"})
    if c['name']=='Flavonoids':
        o=c['content_text']; c['content_text']=o.replace("잎 물 추출물 18.3 mg QE/g 생체중[6]","잎 물 추출물 18.3 mg QE/g(원문 생체중 표기, 시료는 말린 잎)[6]")
        changes.append({"where":"compounds.Flavonoids.content_text","before":o,"after":c['content_text'],"why":"[6] 생/건 기준 모호함 표시"})
for s in d['sources']:
    if s['n']==26:
        s['title']=s['title'].replace('— 초록','— 전문 확인'); s['url']='https://pmc.ncbi.nlm.nih.gov/articles/PMC10340064/'
    if s['n']==13:
        s['title']=s['title']  # unchanged
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('docs/materials/urtica-urens/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
