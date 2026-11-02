import json,sys
p='/home/user/hfoodguide-wave3/docs/materials/centaurea-cyanus/dossier.json'
d=json.load(open(p))
changes=[]
def rep(obj,key,old,new,where,why):
    s=obj[key]
    assert s.count(old)==1,(where,old)
    obj[key]=s.replace(old,new); changes.append({"where":where,"before":old,"after":new,"why":why})
S={s['key']:s for s in d['sections']}
rep(S['overview'],'body',"안토시아닌이 많은 식용꽃 가운데 팬지·코스모스와 함께 세계에서 많이 먹는 종으로 꼽힌다[11].",
 "안토시아닌이 많은 식용꽃 가운데 야생 팬지(Viola tricolor)·코스모스와 함께 세계에서 많이 먹는 종으로 꼽혔다[11].","sections.overview","[11] 본문은 wild pansy(Viola tricolor)를 지칭 — 원예 팬지와 구분")
rep(S['biology'],'body',"포엽·줄기의 샘털과 잎·줄기의 분비관에서 정유·지질·플라보노이드·탄닌이 나온다[20]",
 "샘털은 포엽·줄기 표면에, 분비관은 잎·줄기에 있으며 분비관 분비물에는 정유·지질·플라보노이드·탄닌·스테로이드성 테르펜이 들어 있었다[20]","sections.biology","[20] 초록은 성분 조성을 분비관(duct) 분비물에 대해서만 밝힘")
rep(S['related_species'],'body',"쓸 수 있는 부위도 잎·줄기·뿌리 등으로 서로 다르다[1]",
 "쓸 수 있는 부위도 잎·줄기·뿌리·꽃(C. nigra) 등으로 서로 다르다[1]","sections.related_species","I1020 원자료: C. nigra 는 '사용가능부위 : 꽃'")
rep(S['related_species'],'body',"파란 꽃의 철 조절 유전자를 국화에 넣어 파란 꽃 국화를 만드는 육종 연구도 있다[5].",
 "수레국화의 액포 철 수송 유전자(CcVIT1a)를 국화 꽃에 일시 과발현하자 적자색이 보라색으로 바뀌어, 이를 파란 꽃 육종에 응용하려는 연구도 있다[5].","sections.related_species","[5] 는 국화 'Dante purple'에서 적자색→보라 변화만 보고; 파란 국화를 만든 것은 아님")
rep(S['cultivation'],'body',"저항성 계통은 감수성 계통보다 꽃이 늦게 피었다[9].",
 "온실 시험에서 저항성 계통은 감수성 계통보다 꽃이 늦게 피었으나, 제초제를 뿌린 뒤에는 감수성 계통의 개화가 더 늦었다[9].","sections.cultivation","[9] 본문: 무처리 S 35.2일 vs R 40.1일, 처리 후 S 51.5일 vs R 44.6일")
rep(S['processing'],'body',"비타민 C가 3배 넘게 늘었고 21일 냉장 보관 동안 안정했으며,",
 "비타민 C가 3배 넘게 늘었고, 21일 냉장 보관 동안 FTIR로 본 제품 구조는 안정했으나 일부 생리활성 성분 함량은 유의하게 변했으며,","sections.processing","[17] 초록: FTIR상 안정, 그러나 저장 중 생리활성 성분이 유의하게 변함")
rep(S['processing'],'body',"보조색소화한 뒤 분무건조로 캡슐화하면, 60 °C 72시간 가열과 자외선 노출 뒤 색 안정성 지수가",
 "보조색소화한 뒤 분무건조·동결건조로 캡슐화하면, 60 °C 72시간 가열 뒤 색 안정성 지수가","sections.processing","[10] 본문: 0.61–0.70→0.82–0.94 는 캡슐화물 전체(두 건조법) 범위이며 가열 시험 결과 문단")
rep(S['processing'],'body',"수레국화 안토시아닌은 pH와 온도 변화에 팬지·코스모스 안토시아닌보다 안정했다[11].",
 "수레국화 안토시아닌은 pH와 온도 변화에 야생 팬지·코스모스 안토시아닌보다 대체로 안정했다(60 °C 조건 제외)[11].","sections.processing","[11] 본문: 'consistently more stable ... with an exception in the case of 60 °C'")
rep(S['processing'],'body',"함께 먹는 식품 기질에 따라 흡수가 달라졌다[12]",
 "함께 먹는 식품 기질에 따라 장 세포 투과가 달라졌다(시험관)[12]","sections.processing","[12] 는 Caco-2 투과 시험")
C={c['name']:c for c in d['compounds']}
rep(C['Cyanidin 3,5-diglucoside'],'activity_ko',"장 세포(Caco-2) 모델에서 4시간 투과 효율 약 5%로 흡수가 비교적 높음(시험관)[11]",
 "다이글루코사이드가 주성분인 정제 안토시아닌 추출물 전체가 장 세포(Caco-2) 모델에서 4시간 투과 효율 약 5%로 비교적 높았음(개별 성분 값 아님, 시험관)[11]","compounds.Cyanidin 3,5-diglucoside.activity_ko","[11] 은 피크 합계로 분석했고 개별 안토시아닌 차이는 없었다고 씀")
rep(C['Apigenin 7-O-glucuronide'],'content_text',"; 에탄올 추출물의 아피제닌 O-헥소사이드-O-글루쿠로나이드 13.63 mg/g DW(총페놀의 32.3%)[8]","",
 "compounds.Apigenin 7-O-glucuronide.content_text","[8] 의 13.63 mg/g 은 다른 성분(아피제닌 O-헥소사이드-O-글루쿠로나이드) 값 — 섞임 제거(해당 값은 assays 에 유지)")
rep(C['N-Feruloylserotonin'],'part',"꽃 추출물·씨앗","씨앗(분리)[25]; 시판 추출물의 부위는 초록에서 확인하지 못함",
 "compounds.N-Feruloylserotonin.part","[27] 초록에 추출 부위 기재 없음")
rep(C['Graveobioside A'],'part',"꽃(물 추출물)","물 추출물(부위는 초록에서 확인하지 못함)","compounds.Graveobioside A.part","[28] 초록은 'cornflower water extract'로만 씀")
rep(C['beta-Caryophyllene'],'activity_ko',"꽃잎 분비물(올레오레진)의 주된 휘발 성분[21]",
 "꽃 휘발 성분 가운데 가장 많음; 저자들은 꽃잎 분비물이 수지성 혼합물(올레오레진)일 것으로 추정[21]","compounds.beta-Caryophyllene.activity_ko","[21] 은 올레오레진을 '추정(suppose)'으로 씀")
A=d['assays'][0]
rep(A,'rationale',"아피제닌 배당체가 총페놀의 절반 이상(22.37 mg/g DW)을 차지해",
 "유리 아피제닌을 포함한 아피제닌 유도체가 총페놀의 절반 이상(22.37 mg/g DW)을 차지해","assays[0].rationale","[8] 의 22.37 mg/g 은 유리 아피제닌 포함 'apigenin derivatives' 합계")
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('/home/user/hfoodguide-wave3/docs/materials/centaurea-cyanus/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
