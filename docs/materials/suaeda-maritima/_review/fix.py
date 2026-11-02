import json
p='dossier.json'; d=json.load(open(p))
S={s['key']:s for s in d['sections']}
changes=[]
def rep(key,old,new,why):
    b=S[key]['body']; assert old in b,(key,old); S[key]['body']=b.replace(old,new)
    changes.append({"where":f"sections.{key}","before":old,"after":new,"why":why})

rep('overview','한해살이 염생식물로, 바닷물이 드나드는 염습지와 갯벌 가장자리에서 자란다[1, 10].',
    '한해살이 염생식물로, 바닷물이 드나드는 염습지와 갯벌 가장자리에서 자란다[10, 15].',
    '[1] 식약처 목록 행에는 생활형·서식지 정보가 없음; 한해살이는 [15], 조간대 습지는 [10]')
rep('overview','식품 성분을 정량한 연구는 많지 않다[8, 2].','식품 성분을 정량한 연구는 많지 않다[29, 2].',
    '"염 내성 연구에 세계적으로 쓰이는 식물"이라는 서술은 [29] 초록에 있음')
rep('history','태국 만 연안에서는 뿌리 추출물을 피부 증상을 덜거나 다스리는 데 써 왔다는 전통 이용이 보고되었다[27].',
    '태국 연구진은 태국 만 연안에 자라는 해홍나물의 뿌리 추출물이 일부 피부 증상을 덜거나 다스릴 수 있다고 소개하며 피부 관리용 전통 이용을 언급했으나, 그 근거 문헌이나 이용 지역을 구체적으로 적지는 않았다[27]. 뿌리는 식약처 허용 부위가 아니다[1].',
    '[27] 전문은 전통 이용을 한 줄로 언급할 뿐 구체적 보고가 아님 — 과장 완화')
rep('biology','염분이 높아지면 글리신베타인 같은 삼투 조절 물질을 쌓고 나트륨 이온을 액포에 격리하거나 밖으로 내보내는 방식으로 견딘다[8, 9].',
    '염분이 높아지면 글리신베타인 같은 삼투 조절 물질을 쌓고[9, 10], 나트륨 이온을 세포 안에 격리하거나 밖으로 내보내는 데 관여하는 유전자들의 발현이 바뀐다[8].',
    '[9] 는 글리신베타인 축적만 말하고 나트륨 격리·배출은 말하지 않음; [8] 은 Na 격리·배출을 전사체 결과로 논의(액포 격리를 직접 보인 것은 아님)')
old=S['related_species']['body']
a='한국 나문재속의 분자 연구에서는 ITS로 칠면초·해홍나물·S. australis가 잘 구별되지 않았다는 결과와, 겉모습이 비슷한 종을 DNA 표지로 구별했다는 결과가 함께 보고된 것으로 검색 요약에서 확인했으나 원문은 열지 못했다[31, 32]. '
rep('related_species',a,'한국산 나문재속 종들의 분자 계통 연구는 원문을 확인하지 못함. ',
    '[31]·[32] 는 WebSearch 요약으로만 본 국내 학술지 논문(원문 미열람, 사이트 접속 불가)이라 근거로 쓸 수 없어 문장과 출처 삭제')
rep('related_species','이름만 보고 섞지 않도록 주의해야 한다[1].',
    '이름만 보고 섞지 않도록 주의해야 한다[1]. 또 나문재 행의 학명 이명에는 Schoberia maritima var. asparagoides Franch. & Sav.가 들어 있어, 종소명 \'maritima\'만으로도 해홍나물과 나문재를 가를 수 없다[1].',
    '식약처 I1020 원자료 나문재 행 SCNM 확인 — 이름 혼동 근거 보강')
rep('processing','기생충 감염 후 누적 폐사율이 낮아졌다[20].',
    '섬모충(Miamiensis avidus) 감염 뒤 두 군의 누적 폐사율은 각각 50%·40%로 보고되었다[20].',
    '[20] 초록의 수치로 구체화(대조군 폐사율은 초록에 없음)')
rep('safety','반면 카드뮴·납은 이동계수가 1보다 작아 주로 뿌리에 머물렀다[23].',
    '카드뮴·납을 처리한 실험에서는 이동계수가 1보다 작아 주로 뿌리에 머물렀다[23]. 그러나 페르시아만 야외 시료에서는 니켈·납의 이동계수가 1을 넘어 잎의 납(2.23 mg/kg)이 뿌리(1.22 mg/kg)보다 많았으므로, 잎에 중금속이 쌓이지 않는다고 단정할 수 없다[22].',
    '[22] 초록은 니켈·납 TF>1 이라 [23] 실험 결과와 상충 — 실험 조건을 밝히고 야외 결과 병기')
rep('safety','페르시아만 습지 시료에서 잎의 평균 함량은 카드뮴 0.157, 니켈 3.34, 납 2.23 mg/kg이었다[22].',
    '페르시아만 습지 시료에서 잎의 평균 함량은 카드뮴 0.157, 니켈 3.34, 납 2.23 mg/kg이었으며, 건물·생물 중 어느 기준인지는 초록에 적혀 있지 않다[22].',
    '중금속 값의 기준(건/습) 미기재를 본문에도 명시')
rep('safety','크롬 처리 실험에서는','6가 크롬(100–400 μM) 처리 실험에서는','[24] 처리 조건 보강')

C={c['name']:c for c in d['compounds']}
c=C['Cadmium']; changes.append({"where":"compounds.Cadmium.role","before":c['role'],"after":"other","why":"오염 원소를 nutrient 로 분류한 오류"}); c['role']='other'
c['content_text']='페르시아만 습지 시료 잎 평균 0.157 mg/kg, 뿌리 0.160 mg/kg(건물·생물 기준은 초록에 없음)[22]; 카드뮴 처리 실험에서는 이동계수 1 미만으로 주로 뿌리에 머묾[23]'
c=C['Proline']; old=c['content_text']
c['content_text']='함량 수치 확인하지 못함; 염분 증가 시 뿌리에서 증가[9], 저산소·고염과 크롬 처리에서 증가[10, 24]'; c['source']=[9,10,24]
changes.append({"where":"compounds.Proline.content_text","before":old,"after":c['content_text'],"why":"[9] 초록: S. maritima 뿌리에서 NaCl 에 따라 프롤린 증가"})
c=C['Glycine betaine']; old=c['content_text']
c['content_text']='함량 수치 확인하지 못함; 염분 증가 시 축적[9], 염분·저산소 조건에서 증가[10]'
c['activity_ko']='세포 안 삼투압 조절로 염 내성에 관여[9, 10]'; c['source']=[9,10]
changes.append({"where":"compounds.Glycine betaine","before":old,"after":c['content_text'],"why":"[8] 은 글리신베타인 축적을 직접 보이지 않음 — [9]·[10] 으로 근거 정리"})
c=C['Suaeda A'] if 'Suaeda A' in C else C['Suaedama A']; old=c['class']
c['class']='신규 천연물(논문 키워드에 폴리아세틸렌; 구조 계열은 초록에 없음)'
changes.append({"where":"compounds.Suaedama A.class","before":old,"after":c['class'],"why":"[4] 키워드 Polyacetylene 반영"})

# remove sources 31,32
d['sources']=[s for s in d['sources'] if s['n'] not in (31,32)]
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
