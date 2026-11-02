import json
p='/home/user/hfoodguide-wave3/docs/materials/patrinia-villosa/dossier.json'
d=json.load(open(p))
changes=[]
def rep(where,obj,key,old,new,why):
    s=obj[key]
    assert old in s,(where,old)
    obj[key]=s.replace(old,new,1)
    changes.append({"where":where,"before":old,"after":new,"why":why})
S={s['key']:s for s in d['sections']}
# aliases
d['aliases']=[a for a in d['aliases'] if a!='white patrinia']
changes.append({"where":"aliases","before":"white patrinia","after":"(삭제)","why":"어느 출처에도 없는 영어 별명(식품원료 목록 영명은 White-flower golden lace)"})
# biology classification citation
rep('sections.biology',S['biology'],'body','식물분류에서는 마타리과(Valerianaceae)로 다뤄 왔고, 최근 문헌에서는 인동과(Caprifoliaceae)로 넓게 묶기도 한다[2][28].',
    '식물분류에서는 마타리과(Valerianaceae)로 다뤄 왔고[10][28], 최근 문헌에서는 인동과(Caprifoliaceae)로 넓게 묶기도 한다[2][21].',
    '[28] 초록은 Valerianaceae로 적음 — 인동과 근거는 [2]·[21](Caprifoliaceae s.l.)')
# related species: add name confusion
rep('sections.related_species',S['related_species'],'body','한국 고유종인 금마타리(Patrinia saniculifolia)도 같은 속이며 엽록체 유전체가 따로 해독되었다[21].',
    '한국 고유종인 금마타리(Patrinia saniculifolia)도 같은 속이며 엽록체 유전체가 따로 해독되었다[21]. 같은 목록에서 \'뚝갈나물\'·\'된장뚝갈\'은 국화과 개보리뺑이·그늘보리뺑이(Lapsanastrum속)의 다른 이름이므로 뚝갈과 혼동하지 않아야 한다[1].',
    'I1020 원자료 대조: \'뚝갈\'이 들어간 다른 종 이름(개보리뺑이 RAWMTRL_NCKNM \'뚝갈나물\', 그늘보리뺑이 \'된장뚝갈\') 확인 — 국문명 혼동 경고 추가')
# cultivation genus species count
rep('sections.cultivation',S['cultivation'],'body','마타리속 식물은 동아시아와 북아메리카에 분포하고 중국에는 10종 이상이 자란다[2][5].',
    '마타리속 식물은 동아시아와 북아메리카에 분포하며 20여 종 가운데 10종이 중국에서 자란다[2][5].',
    '[5] 원문: "more than 20 species, 10 of which growing in China" — \'10종 이상\'이 아님')
rep('sections.cultivation',S['cultivation'],'body','한국산 지상부에서는 새 플라보노이드 배당체 2종',
    '한국 약용식물로 소개된 뚝갈의 지상부에서는 새 플라보노이드 배당체 2종',
    '[10] 초록은 \'Korean medicinal plant\'라고만 하고 시료 산지(한국산)는 밝히지 않음')
# processing
rep('sections.processing',S['processing'],'body','식품원료로는 잎만 쓸 수 있으며, 중국에서는 연한 줄기와 잎을 나물로 먹고 차 제품으로도 가공한다[1][2].',
    '식품원료로는 잎만 쓸 수 있으며[1], 중국에서는 패장(뚝갈·마타리 두 종)의 연한 줄기와 잎을 나물로 먹고 차 제품으로도 가공한다[2].',
    '[2]는 두 기원 종을 묶어 \'Herba Patriniae\'로 서술 — 뚝갈만의 정보로 읽히지 않게 범위 명시')
rep('sections.processing',S['processing'],'body','75% 에탄올로 두 번 환류해 9.2%(w/w)의 에탄올 추출물을 얻었다[7].',
    '건조 약재 600 g을 75% 에탄올로 두 번 환류해 9.2%(w/w)의 에탄올 추출물을 얻었다[7].',
    '[7] 전문: 에탄올 추출은 400 g이 아니라 600 g')
rep('sections.processing',S['processing'],'body','초임계 이산화탄소로 뽑은 휘발 성분에서는 46종이 확인되었고',
    '초임계 이산화탄소로 뽑은 휘발 성분(35 MPa·45 °C 추출물)에서는 46종이 확인되었고',
    '[16] 초록: 46종·조성비는 추출물 1(35 MPa, 45 °C)의 값이고 추출물 2는 32종으로 다름')
# safety
rep('sections.safety',S['safety'],'body','문헌 정리에 따르면 패장은 통상 용량에서는',
    '두 기원 종을 함께 다룬 문헌 정리에 따르면 패장은 통상 용량에서는',
    '[2]는 종을 구분하지 않고 서술 — 다른 종 자료 섞임 방지')
rep('sections.safety',S['safety'],'body','같은 정리는 사람에게서 부작용이 나타난 용량을 하루 4–12 g으로 적었는데, 두 기원 종을 함께 다룬 것이어서 뚝갈만의 값인지는 확인하지 못함[2].',
    '같은 정리는 사람에게서 부작용이 나타난 용량을 하루 4–12 g으로 적었으나 뚝갈만의 값인지는 확인하지 못함[2].',
    '앞 문장에 종 범위를 밝혀 중복 표현 정리')
rep('sections.safety',S['safety'],'body','몸무게 변화는 없었고, 항암제 FOLFOX의 대사 효소 수치에도 영향이 없었다[4].',
    '몸무게 감소는 관찰되지 않았고, 항암제 FOLFOX 대사 효소(DPD·SHMT)의 혈장 수치에도 유의한 변화가 없었다(쥐 실험)[4].',
    '[4] 전문: SHMT는 소폭 상승(유의차 없음), 실험 기간 22일 — \'영향 없음\'을 원문 표현으로 좁힘')
# compounds
C={c['name']:c for c in d['compounds']}
c=C['Luteoloside']; old=c['content_text']
c['content_text']='잎 80% 메탄올 추출, HPLC-UV 350 nm로 산지별 정량(뚝갈·마타리 시료를 함께 분석, 산지별 값 표는 전문 텍스트에서 확인하지 못함)[5]'
changes.append({"where":"compounds.Luteoloside.content_text","before":old,"after":c['content_text'],"why":"[5]의 정량 시료는 뚝갈(PVJ2013)과 마타리(PSF2013)를 함께 포함 — 종 섞임 명시"})
c=C['Oleanolic acid']; old=c['content_text']
c['content_text']='잎 에탄올 추출, HPLC-UV 210 nm로 산지별 정량(뚝갈·마타리 시료를 함께 분석, 값은 확인하지 못함)[5]'
changes.append({"where":"compounds.Oleanolic acid.content_text","before":old,"after":c['content_text'],"why":"[5] 시료에 두 종이 섞여 있음 명시"})
c=C['Caffeic acid']; old=(c['part'],c['content_text'],c['activity_ko'])
c['part']='건조 약재(줄기·잎) 물 추출물'
c['content_text']='1.009 ± 0.002 mg/g 추출물[4]; trans-카페산으로도 분리됨[28]'
c['activity_ko']='총플라보노이드 투여 쥐 혈장에서 원형 성분으로 검출됨(정리 논문)[2][24]'
c['source']=[2,4,24,28]
changes.append({"where":"compounds.Caffeic acid","before":json.dumps(old,ensure_ascii=False),"after":"part '건조 약재(줄기·잎) 물 추출물', [28] 부위 '전초' 삭제, 활성 출처에 [2] 추가","why":"[28] 초록은 부위를 밝히지 않음(MeSH Plant Leaves); [24] 초록은 원형 성분 이름을 나열하지 않고 [2] 전문 8절이 카페산을 원형 성분으로 적음"})
c=C['Isoorientin']; old=(c['part'],c['activity_ko'])
c['part']='부위 미기재(초록)'
c['activity_ko']='총플라보노이드 투여 쥐 혈장에서 원형 성분으로 검출됨(정리 논문)[2][24]; 마타리속에서 처음 보고됨[15]'
c['source']=[2,15,24]
changes.append({"where":"compounds.Isoorientin","before":json.dumps(old,ensure_ascii=False),"after":c['part']+' / '+c['activity_ko'],"why":"[15] 초록에 부위 없음; 혈장 원형 성분 목록은 [24] 초록이 아니라 [2] 전문에 있음"})
for nm,src in [('Isovitexin',15),('Orotinin',29),('Villosol',14),('Ursolic acid',31)]:
    c=C[nm]; old=c['part']; c['part']='부위 미기재(초록)'
    changes.append({"where":f"compounds.{nm}.part","before":old,"after":c['part'],"why":f"[{src}] 초록은 시료 부위(전초 여부)를 밝히지 않음"})
c=C['Luteolin']; old=c['content_text']
c['content_text']='전초, 메탄올-염산(13:1) 환류 최적 조건 추출 시 0.265 ± 0.03 mg/g(HPLC 350 nm)[6]'
changes.append({"where":"compounds.Luteolin.content_text","before":old,"after":c['content_text'],"why":"[6] 전문: 산성 메탄올 추출(배당체 가수분해 포함) 조건값임을 명시"})
# sources
src={s['n']:s for s in d['sources']}
old=src[1]['title']
src[1]['title']='식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 뚝갈잎(Patrinia villosa)·마타리·마타리순·패장근(Patrinia scabiosaefolia)·개보리뺑이·그늘보리뺑이 항목'
changes.append({"where":"sources[1].title","before":old,"after":src[1]['title'],"why":"related_species에 추가한 이름 혼동 문장의 근거 항목 포함"})
src[4]['title']=src[4]['title'].replace('Front Pharmacol. 2026 (','Front Pharmacol. 2026;17:1756234 (')
d['changes_tmp']=changes
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
