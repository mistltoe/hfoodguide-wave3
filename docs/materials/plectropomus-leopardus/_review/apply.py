import json,sys
p='/home/user/hfoodguide-wave3/docs/materials/plectropomus-leopardus/dossier.json'
d=json.load(open(p))
changes=[]
def sec(k): return next(s for s in d['sections'] if s['key']==k)
def rep(where,obj,key,old,new,why):
    assert obj[key].count(old)==1,(where,old)
    obj[key]=obj[key].replace(old,new); changes.append({'where':where,'before':old,'after':new,'why':why})
s=sec('overview')
rep('sections.overview',s,'body','한편 무늬바리는 시구아테라(산호초 어류의 시구아톡신 중독) 원인 어종으로 확인된 적이 있어 식품 안전에서 주의할 생선이다[2, 3].',
 '한편 무늬바리는 2004년 홍콩 시구아테라(산호초 어류의 시구아톡신 중독) 집단 발생에서 원인 어종으로 확인된 적이 있어 식품 안전에서 주의할 생선이다[2]. 이 종을 대상으로 한 먹이사슬 모형 연구도 약한 독성 개체가 생길 수 있다고 보았다[3].',
 '[3] 은 모형 연구로 실제 원인 어종 확인 근거가 아님 — 확인은 [2], 모형은 [3] 으로 나눔')
s=sec('related_species')
rep('sections.related_species',s,'body','근연종은 겉모양이 비슷해 혼동되기 쉽다[6]. 오키나와 연구진은',
 '시구아테라 원인 어종은 겉모양이 비슷한 다른 종과 혼동되기 쉽다[6]. 오키나와 연구진은',
 '[6] 의 원인 어종(Variola louti·Lutjanus 속)은 무늬바리의 근연종이 아님 — 겉모양이 비슷한 종으로 고침')
rep('sections.related_species',s,'body','오키나와 1997–2006년 시구아테라 원인 어종에는 근연종 P. areolatus 가 포함되었다[37].',
 '오키나와 1997–2006년 시구아테라 원인 어종에는 근연종 P. areolatus 가 포함되었으나 무늬바리는 그 목록에 없었다[37].',
 '[37] 초록의 원인 어종 목록에 P. leopardus 가 없음을 밝혀 근연종 자료와 섞이지 않게 함')
s=sec('biology')
rep('sections.biology',s,'body','양식 개체의 생식소 조직 관찰에서는','생식소 조직 관찰에서는','[28] 초록은 시료가 양식 개체라고 쓰지 않음')
s=sec('cultivation')
rep('sections.cultivation',s,'body','자연 자원이 줄고 값이 오르면서 중국 등에서 양식이 늘었다[13, 15].',
 '남획과 수요 증가로 자연 자원이 크게 줄었고, 종묘·양성 기술이 발전하면서 집약 양식으로 옮겨 가고 있다[12].',
 '[13]·[15] 초록은 자원 감소·가격 상승·중국 양식 증가를 말하지 않음 — [12] 서론(전문)은 남획·수요로 야생 자원 감소, 종묘·양성 기술로 집약 양식 전환을 씀')
rep('sections.cultivation',s,'body','아스타잔틴이 풍부한 헤마토코쿠스 분말 1.0 g/kg 첨가는 항산화 능력과 비브리오 감염 뒤 생존율을 높였다[32].',
 '아스타잔틴이 풍부한 헤마토코쿠스 분말 1.0 g/kg(아스타잔틴 0.091 g/kg) 첨가는 성장에는 영향이 없었으나 항산화 능력과 V. harveyi 감염 뒤 생존율을 높였다[32].',
 '[32] 초록: 성장 차이 없음(P>0.05), 실제 아스타잔틴 0.091 g/kg, 균주 V. harveyi')
s=sec('processing')
rep('sections.processing',s,'body','붉은형과 검은형의 피부 빛깔 차이는','붉은형과 갈색형의 피부 빛깔 차이는','[16] 초록은 red and brown-colored 라고 씀')
s=sec('safety')
rep('sections.safety',s,'body','무늬바리는 이 종 시료와 먹이사슬 연구로 시구아톡신 오염이 확인된 바리류로, 시구아테라 위험이 있는 생선이다[2, 3].',
 '무늬바리는 시구아테라 위험이 있는 바리류다. 이 종의 직접 근거는 2004년 홍콩 집단 발생에서 원인 어종으로 확인된 것이고[2], 그레이트배리어리프에서는 이 종을 대상으로 한 먹이사슬 모형 연구가 있다[3].',
 '[3] 은 실측이 아닌 모형 연구 — "시료로 오염 확인"은 [2] 에만 해당하므로 나눔')
rep('sections.safety',s,'body','그레이트배리어리프 먹이사슬 모형은 일시적인 독성 와편모조류 대발생만으로도 무늬바리가 약한 독성을 띨 수 있다고 보았다[3].',
 '그레이트배리어리프 먹이사슬 모형은 일시적인 독성 와편모조류 대발생만으로도 1.6 kg 무늬바리의 살이 P-CTX-1 0.1 µg/kg 수준의 약한 독성을 띨 수 있다고 계산했다[3]. 1992년 Plectropomus spp. 살의 시구아톡신 실측값과 1997년 \'coral trout\' 중독 사례는 종이 특정되지 않아 이 종의 근거로 쓰지 않았다[7, 8].',
 '[3] 초록 수치 보강, 종 미특정 자료([7][8])를 이 종 근거와 구분')
c=next(x for x in d['compounds'] if x['name']=='Ciguatoxin CTX1B')
rep('compounds.Ciguatoxin.content_text',c,'content_text','먹이사슬 모형상 약한 독성 개체 살 0.1 µg/kg[3]','먹이사슬 모형상 1.6 kg 약한 독성 개체 살 P-CTX-1 0.1 µg/kg(실측 아님)[3]','[3] 은 모형값')
rep('compounds.Ciguatoxin.activity_ko',c,'activity_ko','시구아테라 식중독의 원인 독소로, 먹이사슬을 따라 무늬바리에 축적된다[2, 3, 4]','시구아테라 식중독의 원인 독소로, 먹이사슬을 따라 무늬바리에 축적될 수 있는 것으로 모형화되었다[2, 3, 4]','[3][4] 는 모형 연구 — 단정 완화')
c=next(x for x in d['compounds'] if x['name']=='Trimethylamine N-oxide')
rep('compounds.TMAO.activity_ko',c,'activity_ko','해산어 근육에 많은 물질로, 이 종 근육 NMR에서 주요 신호로 나타났다[11]','이 종 근육 NMR에서 특히 강한 신호 가운데 하나로 나타났다[11]','"해산어 근육에 많은 물질" 은 [11] 원문에 없음')
a=d['assays'][1]['conditions']
rep('assays[1].conditions.sample_prep',a,'sample_prep','−80 °C 보관 → 액체질소·동결건조','−80 °C 보관 후 −20 °C 운송·보관 → 액체질소·동결건조','[11] Methods: 운송 후 −20 °C 보관')
a=d['assays'][2]['conditions']
rep('assays[2].conditions.sample_prep',a,'sample_prep','','어류 추출물 20 mg 생쥐 주사(초록), 양성 판정 뒤 살 조각 Cigua-Check 검사','[2] 초록에 적힌 범위만 채움')
src=next(x for x in d['sources'] if x['n']==37)
rep('sources[37].title',src,'title','Toxicon 2009;56(5):656-61','Toxicon 2010;56(5):656-61 (온라인 2009)','권 56(5) 는 2010년 인쇄본, PubMed 온라인 게재 2009')
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('/home/user/hfoodguide-wave3/docs/materials/plectropomus-leopardus/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
