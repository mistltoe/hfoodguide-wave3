import json,sys
p='/home/user/hfoodguide-wave3/docs/materials/potentilla-fruticosa/dossier.json'
d=json.load(open(p))
ch=[]
def rep(sec,old,new,why):
    for s in d['sections']:
        if s['key']==sec:
            assert old in s['body'],(sec,old)
            s['body']=s['body'].replace(old,new); ch.append({"where":"sections."+sec,"before":old,"after":new,"why":why}); return
    raise SystemExit(sec)
rep('overview',"'진라오메이(금로매)' 차가 시판된다는 보고가 있다[18]","'진라오메이(Jinlaomei)' 차가 시판된다는 보고가 있다[18]","[18] 은 로마자 'Jinlaomei' 만 적음 — 한자·국문 독음 '금로매'는 출처에 없음")
rep('overview',"국내 자생 흰물싸리 잎을 분석한 논문은 확인하지 못함.","국내 자생 흰물싸리 잎을 분석한 논문은 확인하지 못함. 식약처 목록이 함께 적은 Dasiphora fruticosa var. coreana Nakai는 흰 꽃의 Dasiphora mandshurica의 이명으로 다루어진다는 검색 요약이 있어[35], 노란 꽃 개체 연구값을 이 원료에 그대로 옮길 수 있는지는 확인하지 못함.","국명-학명 대응 근거 수준 명시(WebSearch 요약, WFO·POWO 원문 미열람)")
rep('related_species',"따라서 국명 흰물싸리와 물싸리가 같은 종의 변종 관계인지, 흰 꽃 근연종(D. glabra 등)에 가까운지는 공식 자료로 확인하지 못함.","또 세계 식물 목록 계열 자료에서 Potentilla fruticosa var. mandshurica Maxim.는 흰 꽃잎의 Dasiphora mandshurica (Maxim.) Juz.로 정리되고, 식약처 목록에 적힌 Dasiphora fruticosa var. coreana Nakai도 그 이명으로 올라 있다는 검색 요약이 있으나 원문은 열지 못했다[35]. 노란 꽃의 P. fruticosa와 흰 꽃의 P. glabra는 꽃잎 색으로만 구별될 만큼 비슷하다는 설명도 있다[9]. 따라서 국명 흰물싸리와 물싸리가 같은 종의 변종 관계인지, 흰 꽃 근연종(D. mandshurica·D. glabra 등)에 해당하는지는 공식 자료로 확인하지 못함(근거는 모두 검색 요약 수준).","흰물싸리 국명-학명 대응의 근거 보강·근거 수준 명시")
rep('cultivation',"토양의 유효 인 함량이 주요 요인으로 꼽혔다[14]","토양의 유효 인·유효 질소가 공통 주요 요인으로 꼽혔다(이 초록에는 시료 부위가 적혀 있지 않음)[14]","[14] 초록: RAP·RAN 이 공통 주요 요인; 부위 미기재")
rep('processing',"에탄올 분획의 수율(15.3 g/100 g)과 총페놀(148.4 mg GAE/g)이 가장 높았다[15]","에탄올 분획의 수율(15.3 g/100 g 건조중량)과 총페놀(148.4 mg GAE/g 건조중량)이 가장 높았다[15]","[15] 전문: 원 시료 건조중량 기준 재계산값임을 명시")
rep('history',"리투아니아에서는 이 식물의 극성 추출물을 발효 소시지의 산화 방지에 시험한 연구가 있었다[29].","네덜란드·리투아니아 연구진은 이 식물의 극성 추출물을 네덜란드식 발효 소시지의 산화 방지에 시험했다[29].","[29] 은 Wageningen(네덜란드)·Kaunas(리투아니아) 공동, 네덜란드식 소시지")
rep('safety',"잎 추출물의 항균 활성은 시험관에서 MIC 0.78–6.25 mg/mL 수준이었다[9].","칭하이 잎 80% 아세톤 추출물은 시험관에서 그람양성균·녹농균에 MIC 6.25 mg/mL, 칸디다균에 0.78 mg/mL였으나 대장균·살모넬라균에는 100 mg/mL에서도 억제하지 못했다[9].","[9] 표 7: 0.78–6.25 는 일부 균에 한정, 대장균·살모넬라 >100 mg/mL")
rep('safety',"사람 정상 대장 세포 실험에서는 25–250 µg/mL 추출물이 근섬유모세포의 대사를 억제했다[27].","사람 정상 대장 세포 실험에서는 이 종을 포함한 6종의 물 추출물(25–250 µg/mL)이 모두 근섬유모세포의 대사를 억제했다[27].","[27] 초록: 6종 추출물 전체의 결과")
rep('safety',"탄닌 167.3 ± 2.0 mg/g 건조중량을 함유했고 충치균 바이오필름 형성을 억제했다[20].","탄닌 167.3 ± 2.0 mg/g 건조중량을 함유했고, 지상부 물 추출물은 시험관에서 인공 치태(바이오필름) 형성을 50–100 µg/mL에서 억제했다[20].","[20] 초록 수치 보충, 지상부·시험관 조건 명시")
for c in d['compounds']:
    if c['name']=='Theanine':
        o=c['part']; c['part']='차(중국 민간차 수집 시료, 80 °C 물 추출; 원문은 꽃·씨 유래 몇 종 외에는 잎 유래라고 적음)'
        ch.append({"where":"compounds.Theanine.part","before":o,"after":c['part'],"why":"[17] 전문: 비차나무 차는 2008–2013 수집 시료(시판 구입은 차나무 차만)"})
    if c['name']=='alpha-Linolenic acid':
        c['name']='Linolenic acid'; c['name_ko']='리놀렌산'; c['content_text']='지방산 조성의 29.40%(GC-FID, 리투아니아 식물원 개화기 잎; 원문은 α·γ 구분 없이 linolenic)[15]'
        ch.append({"where":"compounds.alpha-Linolenic acid","before":"alpha-Linolenic acid / 알파-리놀렌산","after":"Linolenic acid / 리놀렌산(원문 α·γ 구분 없음)","why":"[15] 전문은 'linolenic' 으로만 적음"})
        c['class']='다가불포화지방산'
a=d['assays'][0]
o=a['rationale']
a['rationale']="하이퍼로사이드는 이 종 잎에서 정량한 페놀 성분 중 가장 많았고(8.86 mg/g, P. glabra 2.56·P. parvifolia 2.68 mg/g), 같은 크로마토그램의 특징 피크로 세 종을 구별하는 방법도 제시되었다. 전문(Methods)에서 조건을 옮겼고 검출·정량한계는 원문에 없다[9]."
ch.append({"where":"assays[0].rationale","before":o,"after":a['rationale'],"why":"[9] 은 하이퍼로사이드 단일 피크가 아니라 17개 특징 피크 지문으로 종 구별"})
al=d['aliases']; i=al.index('금로매(진라오메이)'); al[i]='진라오메이(Jinlaomei)'
ch.append({"where":"aliases","before":"금로매(진라오메이)","after":"진라오메이(Jinlaomei)","why":"출처[18][19]는 로마자 표기만 있음"})
d['sources'].append({"n":35,"title":"Potentilla fruticosa var. mandshurica Maxim. → Dasiphora mandshurica (Maxim.) Juz.(이명 Dasiphora fruticosa var. coreana Nakai) — 원문 페이지는 열지 못하고 WebSearch 요약으로만 확인","url":"https://wfoplantlist.org/taxon/wfo-0000984127-2025-06","publisher":"World Flora Online(WebSearch 요약; POWO 도 같은 학명을 인정한다는 요약)","accessed":"2026-11-02"})
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(ch,open('/home/user/hfoodguide-wave3/docs/materials/potentilla-fruticosa/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(ch))
