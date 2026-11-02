import json
p='docs/materials/cedrus-libani/dossier.json'
d=json.load(open(p))
changes=[]
def rep(key,old,new,why):
    for s in d['sections']:
        if s['key']==key:
            assert old in s['body'],(key,old)
            s['body']=s['body'].replace(old,new)
            changes.append({"where":f"sections.{key}","before":old,"after":new,"why":why})
            return
    raise KeyError(key)

rep('history',"레바논에서는 이 나무를 여러 감염성 질환의 전통 약으로 널리 써 왔다고 보고되었지만, 보고에 나온 부위는 목재 정유와 구과·잎 추출물이다[7].",
 "레바논에서는 이 나무를 여러 감염성 질환의 전통 약으로 널리 써 왔다고 보고되었지만, 전통적으로 쓴 부위는 초록에 적혀 있지 않고 그 연구가 분석한 것은 목재 정유와 구과·잎 에탄올 추출물이다[7].",
 "[7] 초록은 전통 이용 부위를 밝히지 않음 — 분석 시료(목재 정유·구과·잎 추출물)와 구분")
rep('history',"건류로 생기는 표지 성분으로 후기 왕조 미라 방부제에서 시더 타르를 확인했다[8]. 다만 이 연구의 기준 시료는 아틀라스개잎갈(Cedrus atlantica)이었고 고대 시료의 정확한 종은 밝히지 않았으므로, 레바논개잎갈 수지의 역사로 바로 옮길 수 없다[8].",
 "건류로 생기는 표지 성분으로 이집트 후기 시대(기원전 664–332년) 카노푸스 단지 속 방부제에서 시더 타르를 확인했다[8]. 다만 이 연구의 현대 기준 시료는 모로코 아즈루산 타르, 프랑스 수목원에서 채취한 수지, 시판 정유로 레바논개잎갈 시료라고 밝힌 것이 아니며, 확인한 것도 수지가 아닌 타르이므로 레바논개잎갈 수지의 역사로 옮길 수 없다[8].",
 "[8] 전문(PMC13144440)에서 기준 시료 출처는 모로코 Azrou 타르·프랑스 Pierrefeu-du-Var 수목원 수지·시판 정유로 확인되나, 수집 텍스트에서 학명 표기는 확인되지 않아 'C. atlantica' 단정을 출처 정보로 바꿈. 고대 시료 연대(Late Period 664–332 BCE) 보완")
rep('biology',"레바논개잎갈 수지만의 조성을 정량해 공개한 논문은 PubMed에서 확인하지 못함.",
 "레바논개잎갈 수지만의 조성을 정량해 공개한 논문은 PubMed에서 확인하지 못함. 구과 표면 올레오레진의 정유 조성을 다룬 튀르키예 대학의 연구 목록 기록이 웹 검색 요약에서 보이지만, 원문과 게재 학술지를 열어 보지 못했고 PubMed에도 없어 성분 수치는 싣지 않는다[5].",
 "[5] 는 WebSearch 요약으로만 확인되고 PubMed 검색(Cedrus libani resin/oleoresin)에서 찾지 못함 — 수치 대신 근거 한계만 적음")
rep('processing',"목재는 이탈리아 시칠리아 전통 치즈의 나무통 재료로 시험되어 치즈 품질에 나쁜 영향을 주지 않았다[26].",
 "목재는 이탈리아 시칠리아 전통 치즈의 나무통 재료로 시험되어, 치즈의 물리화학적 조성에 대체로 나쁜 영향을 주지 않았고 밤나무를 대신할 목재로 적합하다고 평가되었다[26].",
 "[26] 초록은 '물리화학적 조성에 대체로 부정적 영향 없음', 대체 목재로 적합이라고 씀 — '품질' 일반화 축소")
rep('safety',"원판 확산법에서 세균 생장을 억제했으나, 후자에서 항진균 효과는 관찰되지 않았다[2, 3].",
 "원판 확산법에서 세균 생장을 억제했으나, 후자에서 항진균 효과는 관찰되지 않았고 대장균은 개잎갈나무 추출물로 억제되지 않았다[2, 3]. 후자는 다섯 수종의 잎·수지·껍질·구과 추출물을 함께 다뤄 수지만의 결과로 볼 수 없다[3].",
 "[3] 초록: 대장균은 Abies cilicica 잎 추출물 외에는 억제되지 않음, 여러 부위를 함께 시험")

# compounds from [5] removed
before=[c['name'] for c in d['compounds']]
d['compounds']=[c for c in d['compounds'] if 5 not in c['source']]
removed=[n for n in before if n not in [c['name'] for c in d['compounds']]]
changes.append({"where":"compounds","before":", ".join(removed)+" (구과 올레오레진 정유 % 수치, [5])","after":"삭제","why":"[5] 는 WebSearch 요약으로만 확인, PubMed에 없음 — 원문 미확인 수치 삭제"})
# assays
d['assays']=[]
changes.append({"where":"assays[0]","before":"구과 올레오레진 정유 휘발 성분(α-피넨 24.78% 등)[5]","after":"삭제","why":"원문 미확인(WebSearch 요약), 분석 조건도 비어 있음"})
changes.append({"where":"assays[1]","before":"목재 타르 GC-MS 조건[9]","after":"삭제","why":"사용 부위(수지)와 무관한 건류물 분석. 조건 자체는 [9] 전문과 일치했으나 수지 분석법으로 오해될 수 있어 뺌; 타르 조성은 processing 본문에 남김"})
# aliases
d['aliases']=[a for a in d['aliases'] if a!='레바논개잎갈나무']
changes.append({"where":"aliases","before":"레바논개잎갈나무","after":"삭제","why":"식약처 목록 별명 칸은 비어 있고 다른 출처 없음(본문 서술용 이름으로만 유지)"})
# source 5 title
for s in d['sources']:
    if s['n']==5:
        s['title']="Chemical composition of the essential oils from oleoresin on cones of Cedrus libani — 원문·서지사항은 열지 못했고(사이트 접속 불가) PubMed에서도 찾지 못함. WebSearch 검색 요약으로만 존재를 확인했으며 수치는 인용하지 않음"
json.dump(d,open(p,'w'),ensure_ascii=False,indent=2)
json.dump(changes,open('docs/materials/cedrus-libani/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
