import json
p='dossier.json'; d=json.load(open(p))
changes=[]
def sec(key,old,new,why):
    for s in d['sections']:
        if s['key']==key:
            assert old in s['body'], (key,old)
            s['body']=s['body'].replace(old,new)
            changes.append({"where":f"sections.{key}","before":old,"after":new,"why":why}); return
    raise KeyError(key)
def comp(name,field,old,new,why):
    for c in d['compounds']:
        if c['name']==name:
            assert old in c[field], (name,old)
            c[field]=c[field].replace(old,new)
            changes.append({"where":f"compounds[{name}].{field}","before":old,"after":new,"why":why}); return
    raise KeyError(name)

sec('overview','체중과 공복혈당에서는 위약과 차이가 없었다[4].',
    '체중과 공복혈당에서는 위약과 차이가 없었고, 이차 결과인 수축기 혈압만 열매 가루 군이 4·6개월째 더 낮았다[4].',
    '[4] 초록·전문: 일차 결과(체중·공복혈당) 차이 없음, 이차 결과 SBP는 M4·M6에 Fx가 낮음(p<0.05) — 결과 일부만 적혀 있어 보완')
sec('genetics','잎과 꽃 조직 11개 시료로 만든 첫 전사체는 221,649개 전사체를 담고 있고',
    '잎과 세 개화 단계의 꽃 조직에서 얻은 12개 cDNA 라이브러리로 11가지 de novo 조립본을 만들어 비교한 뒤 고른 첫 기준 전사체는 221,649개 전사체를 담고 있고',
    '[7] 전문 Methods: 시료는 4개 조직×3반복=12개 라이브러리이고, 11은 비교한 조립본 수')
sec('genetics','브라질과 우루과이 집단 사이에 꽃눈 발달 방식이 달라 초기 종분화 신호일 수 있다는 해석도 있다[25].',
    '열대(콜롬비아)와 아열대(브라질) 재배지의 꽃눈 발달 방식이 서로 달랐으며, 저자들은 이런 차이가 브라질·우루과이 집단 사이 초기 종분화의 신호일 수도 있다고 해석했다[25].',
    '[25] 초록: 실제 비교는 콜롬비아(열대)와 브라질(아열대) 재배지이며, 브라질·우루과이 집단을 직접 비교한 것이 아님')
sec('biology','꽃 전체 추출물에는 안토시아닌이 115.3 mg/L 들어 있어 붉은색을 띤다[27].',
    '꽃 전체 추출물에는 안토시아닌이 115.3 mg/L, 플라보놀이 42.9 mg/L 들어 있었다[27].',
    '[27] 초록은 함량만 보고하고 색과의 인과는 말하지 않음')
sec('processing','페이조아 퓌레(pH 3.2)는 600 MPa 고압 처리에 이산화탄소를 더하면 미생물을 더 잘 줄이면서 단맛을 더한 제품의 관능 품질을 지킬 수 있었다[34].',
    '고압 처리(200–400 MPa)에 이산화탄소를 더하면 대장균·고초균·효모의 불활성화가 커졌고, 600 MPa로 처리한 페이조아 퓌레(pH 3.2)는 설탕을 넣은 경우 신선 제품과 관능 차이가 없었다[34].',
    '[34] 초록: 미생물 시험은 200–400 MPa, 퓌레 관능 시험은 600 MPa로 따로 수행됨 — 두 조건이 섞여 있었음')
sec('processing','이 가루의 알려진 폴리페놀의 약 60%가 카테킨류였다[4].',
    '제조사가 연구진에 제공한 정보로는 이 가루의 알려진 폴리페놀의 약 60%가 카테킨류였다[4].',
    '[4] 전문: 60% 값은 제조사 개인 교신(personal communication) 자료')
sec('safety','생쥐 실험에서 열매·잎 폴리페놀 추출물은 1 g/kg까지 해로운 증상을 보이지 않았다[20].',
    '설치류 실험에서 열매·잎 폴리페놀 추출물은 1 g/kg까지 해로운 증상을 보이지 않았다[20].',
    '[20] 초록은 쥐·생쥐를 함께 썼고 1 g/kg 안전성 시험의 동물 종을 밝히지 않음')
comp('Flavone','content_text','꽃 초임계 CO2(300 bar) 추출물 12.69 mg/g dm, 초음파 추출 114.02–183.69 μg/g dm[8]',
     '꽃 초임계 CO2(300 bar) 추출물 12.69 mg/g, 초음파 추출물 114.02–183.69 μg/g(모두 추출물 건조질량 기준)[8]',
     '[8] 전문: dm 은 꽃이 아니라 추출물 건조질량(extract dry mass) 기준')
comp('Flavone','activity_ko','사람 골수성 백혈병 세포에서 HDAC 억제와 함께 세포자멸사 유도[30]',
     '사람 골수성 백혈병 세포주와 환자 유래 백혈병 세포(시험관)에서 HDAC 억제와 함께 세포자멸사 유도, 사람 대상 근거는 없음[30]',
     '세포 실험 결과임을 분명히 함')
comp('Cyanidin 3-glucoside','content_text','꽃 DES 추출물 90.81 µg/g dm[8]','꽃 DES 추출물 90.81 µg/g(추출물 건조질량 기준)[8]','[8] 전문: 추출물 건조질량 기준')
comp('Cyanidin 3-glucoside','activity_ko','꽃잎의 붉은 색소이자 주요 안토시아닌[8]','식용 꽃잎의 주요 안토시아닌으로 소개됨[8]','[8] 은 "main anthocyanin present in edible flower petals"라고만 씀')
comp('Pedunculagin','part','과육(수용성 알코올 추출물)','과육(물-알코올 추출물)','[31] hydroalcoholic extract')
comp('Pedunculagin','activity_ko','장 상피세포(HT29)에서 160 µg/mL까지 세포독성 없이 사이토카인 손상을 줄임[31]',
     '장 상피세포주(HT29) 시험관 실험에서 160 µg/mL까지 세포독성 없이 사이토카인에 의한 생존율 감소를 줄임(추출물 전체의 결과)[31]','세포 실험·추출물 단위 결과임을 분명히 함')
a=d['assays'][0]
old=a['conditions']['instrument']; a['conditions']['instrument']='LC(Agilent 1290 Infinity, DAD 부착)–삼중사중극자 질량분석기(Agilent 6460), ESI'
changes.append({"where":"assays[0].conditions.instrument","before":old,"after":a['conditions']['instrument'],"why":"[3] 전문 2.6절: 'liquid chromatography (LC) system'으로 기재, UHPLC 표기 없음"})
a=d['assays'][2]
old=a['content']; a['content']=old.replace('12.69 mg/g dm','12.69 mg/g').replace('114.02–183.69 µg/g dm','114.02–183.69 µg/g').replace('90.81 µg/g dm[8]','90.81 µg/g(모두 추출물 건조질량 기준)[8]')
changes.append({"where":"assays[2].content","before":old,"after":a['content'],"why":"[8] 전문: 함량 기준은 추출물 건조질량"})
old=a['part']; a['part']=old.replace('이탈리아 사르데냐 재배','이탈리아 사르데냐 Uta 실험 재배지, 2021년 6월 채취')
changes.append({"where":"assays[2].part","before":old,"after":a['part'],"why":"[8] 4.2절 시료 정보 보완"})
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
