import json
p='/home/user/hfoodguide-wave3/docs/materials/carissa-carandas/dossier.json'
d=json.load(open(p))
S={x['key']:x for x in d['sections']}
def rep(key,a,b):
    s=S[key]; assert a in s['body'],(key,a); s['body']=s['body'].replace(a,b)
rep('related_species',"파키스탄 일부 지역에서는 'Christ thorn'이라고도 부른다[9].",
    "파키스탄 연구는 이 식물이 남아시아·동남아시아 등 여러 분포 지역에서 'Christ thorn'이라고도 불린다고 적었다[9].")
rep('related_species',"파키스탄에서 'Jungli karonda'라고 부르는 것은 C. spinarum으로, 이름이 비슷해 혼동하기 쉽다[11].",
    "파키스탄에서 'Jungli karonda'라고 부르는 것은 C. spinarum으로, 이름이 비슷해 혼동하기 쉽다[11]. POWO 검색 요약에 따르면 'Carissa carandas G.Lodd.'라는 같은 철자의 다른 명명은 C. spinarum의 이명으로 처리되어 있어, 명명자 L.을 확인해야 한다(WebSearch 요약)[2].")
rep('safety',"수컷 쥐에게 열매 건조 분말 또는 메탄올 추출물을 사료의 5–10%로 28일 동안 먹인 시험에서 죽은 개체는 없었고 혈액·혈청 지표는 정상 범위였다[8]. 다만 추출물 10% 군에서는 간세포 핵 농축과 신세뇨관 확장 같은 가벼운 조직 변화가 보였다[8].",
    "수컷 쥐 20마리(5개 군)에게 열매 건조 분말 또는 메탄올 추출물을 사료의 5–10% 수준으로 28일 동안 준 시험에서 죽은 개체는 없었고, 혈액·혈청 지표 대부분은 대조군과 유의한 차이가 없었다[8]. 다만 분말 10% 군에서는 군데군데 가벼운 간세포 괴사·공포화가, 추출물 10% 군에서는 간세포 핵 농축과 신세뇨관 확장 같은 가벼운 조직 변화가 보였고, 수컷만 쓴 단기 시험이라는 한계가 있다[8].")
for c in d['compounds']:
    if c['name']=='Carissic acid':
        c['content_text']="열매 메탄올 추출물의 클로로폼 분획에서 새 화합물로 분리했다고 보고(함량 보고 없음)[19]; 1993년 논문은 같은 이름의 트라이테르펜 carissic acid가 1988년에 이미 분리되었다고 적어, 두 물질이 같은지는 확인하지 못함[14]"
    if c['name']=='Cyanidin 3-galactoside':
        c['content_text']=c['content_text'].replace("메탄올 추출물 총안토시아닌 112 mg/kg[6]","메탄올 추출물 총안토시아닌 112 mg/kg(건조 추출물, 시아니딘-3-글루코사이드 당량)[6]")
for a in d['assays']:
    if a['compound']=='Ascorbic acid':
        a['conditions']['sample_prep']="씨를 뺀 완숙 열매를 차가운 탈이온수와 1:1(w/v)로 균질화해 상등액(SET 1)을 얻고, 남은 침전물을 45 kHz·4 °C에서 1시간씩 초음파 추출하는 과정을 반복해 SET 1–4를 합친 뒤 60 °C 10분 살균 후 동결건조"
for s in d['sources']:
    if s['n']==2:
        s['url']="https://powo.science.kew.org/taxon/urn:lsid:ipni.org:names:77691-1"
        s['title']=s['title'].replace("(승인명, 원산지·도입 지역, 이명)","(승인명, 원산지·도입 지역, 이명; Carissa carandas G.Lodd.는 C. spinarum의 이명)")
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
