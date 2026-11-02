import json,sys
p='/home/user/hfoodguide-wave3/docs/materials/abeliophyllum-distichum/dossier.json'
d=json.load(open(p))
S={s['key']:s for s in d['sections']}
changes=[]
def rep(key,old,new,why):
    b=S[key]['body']; assert old in b,(key,old); S[key]['body']=b.replace(old,new); changes.append({"where":"sections."+key,"before":old,"after":new,"why":why})
rep('overview','한국 특산 식물이다[1, 4, 22]','한국 특산 식물이다[4, 22]','[1](식품원료 목록)은 단형속·특산 여부를 말하지 않음; [4]·[22] 초록이 단형속·한반도 특산을 말함')
rep('overview','잎 에탄올 추출물 1 g당 162.11 mg, 줄기 에탄올 추출물 1 g당 29.68 mg으로 보고되었다[3].','잎 에탄올 추출물 1 g당 162.11 mg, 줄기 에탄올 추출물 1 g당 29.68 mg으로 보고되었다[3]. 이 값은 에탄올 농도를 밝히지 않은 연구용 조추출물 기준이어서, 목록이 정한 70% 주정 잎 추출물·열수 줄기 추출물의 함량과 같다고 볼 수 없다[1, 3].','[3] 전문: EtOH 환류 추출, 농도 미기재 — 목록 제조 조건과 구분 필요')
rep('overview','항산화·지방세포 분화 억제·항염 등의 효과는 세포·동물 실험 결과이며','항산화·지방세포 분화 억제·항염 등의 효과는 시험관·세포·동물 실험 결과이며','항산화는 시험관(라디칼 소거) 결과[3]')
rep('history','자생지 보호의 역사가 길다[32]. ','','[32]는 웹 검색 요약뿐이며 \'역사가 길다\'는 평가를 뒷받침하지 않음')
rep('history','대장암 세포 증식 억제[15]','꽃·잎·가지 아세트산에틸 분획의 대장암 세포 증식 억제(기전 실험은 가지 분획)[15]','[15] 초록: 꽃·잎·가지 분획, ATF3 기전은 가지(EAFAD-B) — 부위 구분')
rep('related_species','미선나무속은 한 종뿐인 단형속이며, 계통 분석에서 개나리속(Forsythia)의 자매군으로 확인되었다[29]. 두 속은 개나리족(Forsythieae)을 이루고, 염색체 수준 유전체 비교에서 미선나무와 산개나리(Forsythia ovata)는 약 1,387만 년 전 마이오세에 갈라진 것으로 추정되었다[24, 29].','미선나무속은 한 종뿐인 단형속이며, 계통 분석에서 개나리속(Forsythia)의 자매군으로 확인되었다[28, 29]. 두 속은 개나리족(Forsythieae)을 이룬다[29]. 염색체 수준 유전체 비교에서 미선나무와 산개나리(Forsythia ovata)는 약 1,387만 년 전 마이오세에 갈라진 것으로 추정되었다[24].','1,387만 년(13.87 Mya) 추정은 [24]의 값; [29]는 개나리족의 마이오세 기원만 말함. 자매군 관계는 [28]도 지지')
rep('cultivation','잎 캘러스 배양에서 메틸자스모네이트 50 μM 처리 시 베르바스코사이드 함량이 약 50 mg/g에서 약 97.05 mg/g으로 늘었다는 보고가 있다[20].','잎 캘러스(배양체) 배양에서 메틸자스모네이트 50 μM 처리 시 베르바스코사이드 함량이 약 50 mg/g에서 약 97.05 mg/g으로 늘었다는 보고가 있다[20]. 이는 배양 세포 덩어리의 값으로, 식품원료인 잎·줄기 추출물의 함량이 아니다[1, 20].','배양체 결과를 식품원료 잎 추출물과 구분')
rep('processing','다른 연구는 잎을 에탄올로 가열 환류 추출했다[6]. 이런 추출물은 목록의 제조 조건(70% 주정)과 같다고 볼 수 없다[1, 5].','다른 연구는 잎을 에탄올로 가열 환류 추출했으나 에탄올 농도는 밝히지 않았다[6]. 전립선비대 연구는 잎을 증류수·70% 에탄올·95% 헥산으로 각각 추출해 비교한 뒤 70% 에탄올 추출물을 동물 실험에 썼는데, 용매 농도는 목록 조건과 같지만 농축·건조 공정은 초록에서 확인하지 못함[11]. 50% 에탄올 추출물[5]이나 농도 미기재 추출물[6]은 목록의 제조 조건(70% 주정)과 같다고 볼 수 없다[1, 5, 6].','추출 조건 차이(50% vs 70% vs 미기재) 처리: [6] 전문은 농도 미기재, [11] 초록은 70% 에탄올 추출물 사용')
rep('genetics','엽록체 유전체는 분홍꽃 품종군(f. lilacinum)에서 156,015 bp, 133개 유전자로 보고되었다[30].','엽록체 유전체는 충북에서 얻은 품종 f. lilacinum에서 156,015 bp, 133개 유전자로 보고되었다[30].','[30] 초록은 꽃 색을 말하지 않음 — \'분홍꽃 품종군\' 근거 없음')
rep('safety','임신 생쥐에게 잎 추출물만 먹인 군은 임신 결과에 영향이 없었으나, 이는 효능 시험이며 독성 시험이 아니다[5].','임신 생쥐에게 잎 50% 에탄올 추출물만 하루 100 μg/kg씩 15일 먹인 군은 임신 결과에 영향이 없었으나, 이는 낮은 용량의 효능 시험이며 독성 시험이 아니다[5].','[5] 전문: 경구 100 μg/kg/day 15일, 50% 에탄올 추출물 — 용량·추출 조건 명시')
for c in d['compounds']:
    if c['name']=='Acteoside':
        o=c['content_text']; c['content_text']=o.replace('잎 캘러스 약 50 mg/g → 메틸자스모네이트 50 μM 처리 약 97.05 mg/g[20]','잎 캘러스(배양체, 식품원료 아님) 약 50 mg/g → 메틸자스모네이트 50 μM 처리 약 97.05 mg/g[20]').replace('잎 에탄올 추출물 162.11 mg/g, 줄기 에탄올 추출물 29.68 mg/g(HPLC-UV)[3]','잎 에탄올 추출물 162.11 mg/g, 줄기 에탄올 추출물 29.68 mg/g(에탄올 농도 미기재, HPLC-UV)[3]')
        changes.append({"where":"compounds.Acteoside.content_text","before":o,"after":c['content_text'],"why":"배양체·추출 조건 구분"})
        o=c['activity_ko']; c['activity_ko']=o.replace('섬유아세포에서 산화성 DNA 손상 지표 감소(세포)[19]','생쥐 섬유아세포(NIH 3T3)에서 산화성 DNA 손상 지표 감소(세포)[19]')
        changes.append({"where":"compounds.Acteoside.activity_ko","before":o,"after":c['activity_ko'],"why":"[19] 초록: NIH 3T3 세포"})
a=d['assays'][0]; o=a['part']; a['part']='잎·줄기(에탄올 조추출물, 에탄올 농도 미기재)'
changes.append({"where":"assays[0].part","before":o,"after":a['part'],"why":"[3] 전문: EtOH 농도 미기재 — 목록 70% 주정 조건과 구분"})
s32=[s for s in d['sources'] if s['n']==32][0]; o=s32['title']
s32['title']=o.replace('원문 페이지는 이 환경에서 열리지 않아 웹 검색 결과(제목·요약)로만 확인함','원문 페이지는 이 환경에서 열리지 않아 웹 검색 결과 요약(WebSearch)으로만 확인함(작성·대조 모두), 지정 번호·연도는 싣지 않음')
changes.append({"where":"sources[32].title","before":o,"after":s32['title'],"why":"WebSearch 요약 출처임을 분명히 함"})
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open(p.replace('dossier.json','_review/changes.json'),'w'),ensure_ascii=False,indent=1)
print(len(changes))
