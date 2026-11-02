import json,re,sys
P='/home/user/hfoodguide-wave3/docs/materials/tamarix-gallica/'
d=json.load(open(P+'dossier.json'))
changes=[]
def rep(where,old,new,why):
    sec=[s for s in d['sections'] if s['key']==where][0]
    assert old in sec['body'],(where,old)
    sec['body']=sec['body'].replace(old,new); changes.append({"where":"sections."+where,"before":old,"after":new,"why":why})
rep('overview',"즉 이 종에서 식품원료로 인정된 것은 가지에서 나오는 수액(만나) 하나이고","즉 이 종에서 식품원료로 인정된 것은 수액 하나이고",
    "[1] 목록 행은 부위를 '수액'으로만 적으며 '가지에서 나오는 만나'라는 설명은 없음")
rep('history',"다만 이 기록의 식물은 T. mannifera이며, 이 이름은 현재 다른 종(T. nilotica)의 이명으로 다루는 자료가 있다는 정도만 웹 검색 요약으로 확인했다[3].","다만 이 기록의 식물은 T. mannifera이며, 이 이름의 현재 분류 처리(다른 종의 이명 여부)는 원문으로 확인하지 못함.",
    "[3]은 웹 검색 요약일 뿐 원문(POWO)을 열지 못해 근거가 되지 못함; PubMed에서도 대체 출처 찾지 못함 — 출처 삭제")
rep('history',"인도에서는 'Jhau'라는 이름으로 거담·간 강장·완하·수렴·지사 목적으로 쓰였다고 한다[17].","'Jhau'라는 이름으로 거담·간 강장·완하·수렴·지사 목적으로 전통적으로 쓰였다고 한다[17].",
    "[17] 초록은 'known as Jhau'라고만 하고 '인도'라는 지역은 말하지 않음")
rep('biology',"200 mM NaCl과 비소를 함께 준 재배 실험에서도 광합성 형광값과 칼륨·칼슘·마그네슘 함량이 유지되어 비소에 내성이 있는 식물로 평가되었다[27].",
    "200 mM NaCl과 비소를 함께 준 재배 실험에서도 광합성 형광값과 칼륨·칼슘·마그네슘 함량이 유지되어 비소에 내성이 있는 식물로 평가되었다(다만 비소 농도가 높을수록 새순 생장은 줄었다)[27].",
    "[27] 초록은 비소가 생장을 유의하게 줄였다고도 씀 — 한쪽만 옮긴 것 보완")
rep('biology',"꽃은 꿀벌의 밀원이 되어, 꽃가루 분석으로 이 종의 단일 밀원 꿀(Tamarix gallica honey)이 사우디아라비아·리비아·이집트에서 확인되었다[22].",
    "꽃은 꿀벌의 밀원이 되며, 사우디아라비아·리비아·이집트 꿀을 꽃가루 분석(해당 꽃가루 55% 이상)으로 'Tamarix gallica 꿀'로 판정한 연구가 있다[22]. 다만 이 논문은 이 종이 사우디아라비아·시나이 반도 원산이라고 적고 있어, 꽃가루로 위성류속 안의 종까지 구별했는지는 확인하지 못함[22].",
    "[22] 기준은 꽃가루 55% 이상; 지중해 서부 종인 T. gallica를 아라비아·시나이 원산으로 적어 다른 위성류(예: 만나 위성류) 꿀과 섞였을 가능성 — 단정 표현 완화")
rep('related_species',"T. mannifera는 현재 T. nilotica의 이명으로 보는 자료가 있다는 점은 웹 검색 요약으로만 확인했다[3]. ","",
    "[3] 웹 검색 요약 출처 삭제(원문 확인 불가)")
rep('related_species',"쿠르디스탄 만나는 물에 녹는 부분에서 자당 61, 전화당 16.5, 덱스트린류 22.5였다[2]. 이는 T. gallica 수액의 값이 아니며 다른 종(또는 식물이 분명하지 않은) 시료의 값이다[2].",
    "쿠르디스탄 만나는 물에 녹는 부분에서 자당 61, 전화당 16.5, 덱스트린류 22.5였다[2]. 이는 T. gallica 수액의 값이 아니며, 쿠르디스탄 만나는 '여러 식물에 가리지 않고 내리고' 시료에 참나무류(nut-gall tree) 잎이 섞여 있었다고 적혀 있어 위성류속 만나로도 볼 수 없다[2].",
    "[2] 원문: Kurdistan 만나는 every plant에 내리고 nut-gall tree 잎이 섞임 — 식물 불분명이 아니라 위성류가 아닌 시료")
rep('processing',"다만 이 두 기록은 T. gallica로 확인된 시료가 아니다[2].","다만 시나이 만나는 T. mannifera 시료이고 쿠르디스탄 만나는 참나무류 잎이 섞인 위성류속 밖의 시료여서, 두 기록 모두 T. gallica 수액의 가공법이 아니다[2].",
    "[2] 원문 대조 — 쿠르디스탄 만나는 위성류 만나가 아님을 분명히 함")
rep('processing',"연구용 가공은 대부분 잎·꽃·지상부를 그늘에서 말려 가루로 만든 뒤 메탄올·에탄올·물 등으로 추출하는 방식이다[10][11].",
    "연구용 가공은 대부분 잎·꽃·지상부를 그늘이나 실온에서 말려 가루로 만든 뒤 메탄올·에탄올·물 등으로 추출하는 방식이다[10][11].",
    "[10] 전문은 실온 공기 건조(air-dried at room temperature), 그늘 건조는 [11]만")
rep('genetics',"원산지 아시아에서는 떨어져 있던 두 종의 유전형이 섞인 잡종이 가장 흔했고","원산지 유라시아에서는 떨어져 있던 두 종의 유전형이 섞인 잡종이 가장 흔했고",
    "[23] 초록: native Eurasian range")
rep('safety',"한 논문은 급성 경구 독성 시험에서 체중 kg당 3000 mg까지 비교적 안전했다는 앞선 보고를 인용했으나 원 자료는 확인하지 못함[11].",
    "한 논문은 급성 경구 독성 시험에서 체중 kg당 3000 mg까지 비교적 안전했다는 앞선 보고를 인용했으나 원 자료와 시험 부위는 확인하지 못함[11]. 쥐 기억력 실험의 지상부는 중국 업체에서 구입한 것이어서 종 확인 정보가 부족하다[12].",
    "[12] 전문: aerial part ordered from a supplier in China — 근연종 혼입 가능성 표시")
rep('safety',"시험관·세포 수준에서는 새순 메탄올 추출물이 총페놀 85 mg GAE/g DW, DPPH IC50 3.3 µg/mL을 보였고 100 µg/mL에서 대장암 세포(Caco-2) 증식을 약 62% 억제했다[6].",
    "시험관·세포 수준에서는 새순 메탄올 추출물이 총페놀 85 mg GAE/g DW, DPPH IC50 3.3 µg/mL을 보였고, 새순·잎·꽃 추출물 대부분이 100 µg/mL에서 대장암 세포(Caco-2) 증식을 약 62% 억제했다[6].",
    "[6] 초록: 62% 억제는 'almost all plant part extracts'(새순·잎·꽃)의 결과로 새순만의 값이 아님")
rep('safety',"트립신 억제(IC50 1.7 µg/mL)[30]","메탄올 추출물의 트립신 억제(IC50 1.7 µg/mL)[30]","[30] 초록: 메탄올 추출물 — 조건 보완")
# compounds
for c in d['compounds']:
    if c['part'].startswith('지상부(분리 부위 초록에 없음'):
        old=c['part']; c['part']="분리 부위 초록에 없음(수액 아님)"
        changes.append({"where":"compounds."+c['name']+".part","before":old,"after":c['part'],"why":"[8][9] 초록에 분리 부위가 없는데 '지상부'로 적어 앞뒤가 맞지 않음"})
    if c['name']=='Squalene':
        old=c['activity_ko']; c['activity_ko']="추출물의 콜린에스테레이스·α-아밀레이스 억제와 관련 있을 수 있는 지용성 항산화 성분으로 거론되었다(추정)[10]"
        changes.append({"where":"compounds.Squalene.activity_ko","before":old,"after":c['activity_ko'],"why":"[10] 고찰은 스쿠알렌을 AChE·α-아밀레이스 억제 맥락에서 거론 — '잎 추출물의 항산화 활성 기여'라는 말은 없음"})
d['aliases']=[a if not a.startswith('Jhau') else 'Jhau(지역명)' for a in d['aliases']]
changes.append({"where":"aliases","before":"Jhau(인도 지역명)","after":"Jhau(지역명)","why":"[17] 초록에 지역(인도) 언급 없음"})
# remove source 3 and renumber
old2new={}
new=[]
for s in d['sources']:
    if s['n']==3: continue
    old2new[s['n']]=len(new)+1; s2=dict(s); s2['n']=len(new)+1; new.append(s2)
d['sources']=new
def rn(txt): return re.sub(r'\[(\d+)\]',lambda m:'['+str(old2new[int(m.group(1))])+']',txt)
def walk(o):
    if isinstance(o,dict):
        for k,v in o.items():
            if k=='source' and isinstance(v,list): o[k]=[old2new[x] for x in v]
            elif k in('sources',): continue
            else: o[k]=walk(v)
        return o
    if isinstance(o,list): return [walk(x) for x in o]
    if isinstance(o,str): return rn(o)
    return o
srcs=d.pop('sources'); d=walk(d); d['sources']=srcs
json.dump(d,open(P+'dossier.json','w'),ensure_ascii=False,indent=1)
json.dump(changes,open(P+'_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
