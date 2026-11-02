import json,sys
p='/home/user/hfoodguide-wave3/docs/materials/rumex-crispus/dossier.json'
d=json.load(open(p))
S={s['key']:s for s in d['sections']}
changes=[]
def rep(where,obj,key,old,new,why):
    v=obj[key]
    assert v.count(old)==1,(where,old)
    obj[key]=v.replace(old,new)
    changes.append({"where":where,"before":old,"after":new,"why":why})

rep('sections.overview',S['overview'],'body',
 "소리쟁이를 먹은 사람과 양이 옥살산 중독으로 숨진 사례도 보고되어 있어, 허용 부위인 잎만 적은 양으로 먹는 것이 안전하다는 점을 기억할 필요가 있다[1][4][5].",
 "소리쟁이가 무성한 곳에 들어간 양이 급성 옥살산 중독을 일으킨 사례와 소리쟁이를 먹은 사람이 숨진 사례가 보고되어 있다[4][5]. 식품원료로 쓸 수 있는 부위는 잎뿐이며, 다 자란 잎일수록 옥살산이 많으므로 많이 먹지 않도록 주의할 필요가 있다[1][3].",
 "[4]는 양의 옥살산 중독, [5]는 사람 사망 사례이며 초록에 옥살산 중독이라 명시하지 않음. '적은 양이면 안전하다'는 어느 출처도 말하지 않음")
rep('sections.history',S['history'],'body',
 "멕시코 등에서는 어린잎을 수프와 샐러드로 먹고 씨를 과자에 넣거나 커피 대용으로 썼다고 정리되어 있다[15].",
 "어린잎은 수프와 샐러드로 먹고 씨는 과자를 굽는 데 넣거나 커피 대용으로 쓴다고 정리되어 있다[15].",
 "[15]는 멕시코 연구진의 논문이지만 이 이용법을 멕시코에 한정해 쓰지 않음")
rep('sections.history',S['history'],'body',
 "식품원료 목록의 다른 이름 '양제'는 한약명 羊蹄와 같지만, 한국 고문헌의 '양제'가 소리쟁이(R. crispus)를 가리키는지는 이번 조사에서 원문으로 확인하지 못함.",
 "식품원료 목록의 다른 이름 '양제'·'야대황'이 어느 한약명·고문헌 기록에 대응하는지, 그 기록이 소리쟁이(R. crispus)를 가리키는지는 이번 조사에서 원문으로 확인하지 못함.",
 "'양제=羊蹄'는 출처 없는 추정이며 羊蹄는 참소리쟁이(R. japonicus) 계열 약재명으로도 쓰여 근연종과 섞일 위험이 있음")
rep('sections.related_species',S['related_species'],'body',
 "소리쟁이·대황속 식물과 산소리쟁이속(Oxyria)의",
 "소리쟁이·대황속 식물과 나도수영속(Oxyria)의",
 "Oxyria 의 국명은 나도수영속; '산소리쟁이속'은 근거 없는 이름")
rep('sections.related_species',S['related_species'],'body',
 "이 자료에는 그 종들의 성분·안전성 값을 섞지 않았다[1].",
 "이 자료에는 그 종들의 성분·안전성 값을 섞지 않았다[1]. 특히 참소리쟁이는 목록에 다른 이름 '소리쟁이'와 이명 Rumex crispus subsp. japonicus가 함께 올라 있어, 국문명만으로는 두 원료를 구별하기 어렵다[1].",
 "식품원료 목록(I1020) 참소리쟁이 행 확인 — 국문명 혼동 주의 추가")
rep('sections.cultivation',S['cultivation'],'body',
 "먹을 잎은 봄철 어린잎을 쓰는데, 잎이 자랄수록 옥살산이 늘고 쓴맛이 강해진다[3][16].",
 "어린잎은 특히 봄철 채소로 먹었으며[16], 다 자란 잎은 어린잎보다 옥살산이 많고 더 쓰다[3].",
 "[16]은 옥살산을 다루지 않음; [3]은 다 자란 잎과 어린잎 비교만 말함")
rep('sections.processing',S['processing'],'body',
 "분석·가공 때 물이 많은 용매나 높은 온도를 쓰면",
 "뿌리를 추출할 때 물이 많은 메탄올–물 용매나 높은 온도를 쓰면",
 "[9]는 가압액체추출(분석용 추출) 실험이며 식품 가공은 다루지 않음")
rep('sections.safety',S['safety'],'body',
 "채취한 소리쟁이속 시료의 옥살산은 건조중량의 6.6–11.1%였다[4]. 스페인에서는 소리쟁이를 먹은 53세 남성이 위장 증상·심한 저칼슘혈증·대사성 산증·급성 간부전 끝에 72시간 만에 숨졌고, 간과 신장에서 옥살산 결정이 확인되었다[5]. 반면 남아프리카 연구는 잎의 옥살산을 0.15 mg/g으로 낮게 보고해, 측정법과 시료에 따라 값이 크게 다르다[3].",
 "채취한 소리쟁이속 시료의 옥살산은 건조중량의 6.6–11.1%였다[4]. 스페인 연구진이 보고한 사례에서는 소리쟁이를 먹은 53세 남성이 위장 증상·심한 저칼슘혈증·대사성 산증·급성 간부전 끝에 72시간 만에 숨졌고, 간과 신장에서 복굴절성 결정이 확인되었다[5]. 반면 남아프리카 연구는 말린 잎 분말의 옥살레이트를 0.15 mg/g(0.015%)으로 보고해, 측정법과 시료에 따라 값이 수백 배 다르다[3].\n\n안트라퀴논은 뿌리에 몰려 있다: 뿌리 에탄올 추출물의 디클로로메탄 분획 1 g에는 에모딘 160.43 mg·크리소파놀 66.96 mg·피스시온 34.90 mg이 들어 있었다(분획 기준이며 원물 함량이 아님)[8]. 식품 부위인 잎의 안트라퀴논 함량을 정량한 자료는 이번 조사에서 확인하지 못함.",
 "[5] 초록은 '복굴절성 결정'이라고만 쓰고 발생 국가는 저자 소속(바르셀로나)으로만 확인됨; 옥살산 값의 기준(건조) 명시; 안트라퀴논 함량·출처 추가(지시문 요구)")
rep('sections.safety',S['safety'],'body',
 "뿌리 추출물은 잎 추출물보다 브라인슈림프·HeLa 세포 독성이 컸다[32].",
 "뿌리 에탄올·아세톤 추출물이 브라인슈림프 치사 시험과 HeLa 세포 독성 시험에서 가장 독성이 컸다[32].",
 "[32] 초록은 뿌리 에탄올·아세톤 추출물이 가장 독성이 컸다고만 씀")

C={c['name']:c for c in d['compounds']}
rep('compounds.Emodin 8-glucoside.activity_ko',C['Emodin 8-glucoside'],'activity_ko',
 "배당체가 장에서 완하 작용을 하는 하이드록시안트라퀴논의 주된 형태[9]",
 "식물 속 하이드록시안트라퀴논은 대부분 이런 단당 배당체 형태로 있고, 이 계열은 장에서 완하 작용을 함[9]",
 "[9]는 배당체가 식물 내 주된 형태이고 하이드록시안트라퀴논이 장에서 완하 작용을 한다고 따로 씀")
rep('compounds.Physcion 8-glucoside.activity_ko',C['Physcion 8-glucoside'],'activity_ko',
 "75 °C 넘는 추출 온도에서 빠르게 줄어드는 불안정한 배당체[9]",
 "메탄올–물(40:60) 가압추출에서 75 °C를 넘으면 빠르게 줄어드는 불안정한 배당체[9]",
 "조건(용매) 명시")
rep('compounds.Nepodin.part',C['Nepodin'],'part',"전초(70% 에탄올 추출물)","부위는 초록에 없음(70% 에탄올 추출물)",
 "[17] 초록은 부위를 밝히지 않음")
rep('compounds.Quercitrin.activity_ko',C['Quercitrin'],'activity_ko',
 "α-글루코시다아제 억제 추출물의 주요 성분으로 추정[15]",
 "저자들이 α-글루코시다아제 억제와 관련된 지표 후보로 제시함(시험관; 잎 추출물은 꽃 추출물보다 억제력이 약했음)[15]",
 "[15]에서 퀘르시트린이 최대 피크인 잎 추출물은 세 활성 시료 중 억제력이 가장 약했음")

A=d['assays']
rep('assays[0].rationale',A[0],'rationale',"다른 보고(건조중량의 6.6–11.1%)와 수천 배 차이가 나서",
 "다른 보고(건조중량의 6.6–11.1%)와 수백 배(약 440–740배) 차이가 나서",
 "0.15 mg/g=0.015% 이므로 6.6–11.1% 와는 440–740배")
rep('assays[2].conditions.recovery',A[2]['conditions'],'recovery',
 "PLE 1회 추출 회수율 98.5% 초과(RSD < 7%, n = 5)",
 "PLE 1회 추출 효율 98.5% 초과(메탄올, 100 °C, 10분, 60 bar; RSD < 7%, n = 5)",
 "원문의 조건(연속 추출 기준 효율) 명시")
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('/home/user/hfoodguide-wave3/docs/materials/rumex-crispus/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
