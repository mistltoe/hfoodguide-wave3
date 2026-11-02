import json,sys
p='/home/user/hfoodguide-wave3/docs/materials/callistemon-citrinus/dossier.json'
d=json.load(open(p))
S={s['key']:s for s in d['sections']}
changes=[]
def rep(key,old,new,why):
    b=S[key]['body']; assert old in b,(key,old); S[key]['body']=b.replace(old,new); changes.append({"where":"sections."+key,"before":old,"after":new,"why":why})
rep('overview',"잎에서 얻은 정유의 주성분은 1,8-시네올(유칼립톨)이고, α-피넨·리모넨·α-테르피네올이 함께 많다[10, 11, 19].",
 "잎에서 얻은 정유의 주성분은 대개 1,8-시네올(유칼립톨)이지만[11, 34], 2015년 서히말라야 잎 정유처럼 α-피넨이 가장 많은 시료도 있고, 리모넨·α-테르피네올도 많이 들어 있다[10, 19].",
 "[10] 초록은 잎 정유 최다 성분이 α-피넨(32.3%)이고 1,8-시네올은 꽃 정유 주성분이라 함; 주성분 단정을 산지별 차이로 고침")
rep('history',"그 뒤 Craven이 2006년 Novon 논문에서 Callistemon을 Melaleuca에 합쳤고, 큐 왕립식물원은 이를 받아들였지만 뉴사우스웨일스 국립식물표본관 등은 받아들이지 않았다고 WebSearch 요약으로만 확인했다[4].",
 "그 뒤 Craven은 2006년 Novon 논문에서 Callistemon을 Melaleuca와 따로 둘 만큼 다르지 않다며 두 속을 합쳐야 한다고 결론지었으나, 오스트레일리아 자생식물학회 자료는 실용상 Callistemon이라는 이름을 계속 쓰고 있어 두 이름이 함께 쓰인다고 WebSearch 요약으로만 확인했다[4].",
 "기관별 수용 여부(큐·NSW 표본관)는 검색 결과에서 확인되지 않아 확인된 범위(Craven 2006 결론, ANPSA의 실용적 병용)로 줄임")
rep('related_species',"병솔나무 정유의 주성분인 1,8-시네올은 같은 도금양과의 유칼립투스 정유에도 많다[25, 33]. 그래서 병솔나무 정유 연구는 Eucalyptus citriodora 정유와 나란히 비교되기도 했다[33]. 병솔나무 잎이 아닌 유칼립투스 정유에서 나온 안전 정보는 safety 절에 따로 적었다[25, 28].",
 "병솔나무 정유의 주성분인 1,8-시네올은 유칼립투스속과 로즈마리속 식물에도 많은 모노테르펜이다[36]. 병솔나무 정유는 같은 도금양과의 Eucalyptus citriodora 정유와 함께 쥐 회장 수축 실험에서 비교되기도 했지만, 이 논문 초록은 두 정유의 1,8-시네올 함량을 비교하지 않았다[33]. 병솔나무가 아닌 유칼립투스 정유에서 나온 중독·안전 정보는 safety 절에 출처 식물을 밝혀 따로 적었다[25, 28].",
 "[25]·[33] 초록 어디에도 1,8-시네올 언급이 없음(근거 불일치); '그래서' 인과도 근거 없음. 1,8-시네올이 유칼립투스에 많다는 근거를 리뷰(PMID 42070456)로 바꿈")
rep('processing',"연구용 정유는 보통 잎을 그늘에 말려 가루 낸 뒤 클레벤저 장치로 3시간 수증기 증류해 얻는다[7].",
 "한 인도 연구는 잎을 24시간 그늘에 말려 거칠게 간 뒤 클레벤저 장치로 3시간 물 증류(hydro-distillation)해 정유를 얻었다[7].",
 "[7] 전문은 한 연구의 방법(hydro-distillation, 그늘 24시간)이며 '보통'으로 일반화할 근거 없음; 수증기 증류→물 증류")
rep('safety',"쥐에 잎 에탄올 추출물을 100–4000 mg/kg 한 번 먹인 급성 독성 시험에서 죽거나 이상을 보인 동물이 없었고,",
 "쥐에 생잎 에탄올 추출물을 100–4000 mg/kg 한 번 먹인 급성 독성 시험(용량군마다 3마리)에서 죽거나 이상을 보인 동물이 없었고,",
 "[8] 전문: 생잎 추출물, 군당 n=3 — 소규모임을 밝힘")
rep('safety',"1000 mg/kg을 28일간 매일 먹인 아급성 시험에서도 간 효소(AST·ALT·LDH)와 간 조직에 변화가 없었다[8].",
 "1000 mg/kg을 28일간 매일 먹인 아급성 시험(8마리)에서도 간 효소(AST·ALT·LDH)와 간 조직에 변화가 없었다[8]. 다만 같은 논문은 말린 잎을 쓴 다른 연구에서 생쥐 반수치사량(LD50)이 3200 mg/kg으로 보고되었다고 인용했다[8].",
 "[8] 전문 Discussion의 Bhushan 등 인용(건조 잎, 생쥐 LD50 3200 mg/kg) 추가 — 독성 없음 단정 완화")
rep('safety',"정유의 주성분 1,8-시네올은 따로 주의가 필요하다[8, 25]. 위 쥐 논문은 1,8-시네올이 간·신장 조직에 심한 변화를 일으킬 수 있다는 보고를 인용했다[8]. 1,8-시네올이 많은 유칼립투스 정유를 어린이가 삼킨 109건 분석에서 5 mL 이상이면 의식 저하가, 2–3 mL에서도 가벼운 의식 저하가 생길 수 있었다[25].",
 "식품원료 목록에 오른 원료는 '병솔나무잎'이며, 잎에서 뽑은 정유를 따로 식품원료로 올린 내용은 이 목록 행에서 확인하지 못함[1]. 정유의 주성분 1,8-시네올은 따로 주의가 필요하다[8]. 위 쥐 논문은 1,8-시네올이 간·신장 조직에 심한 변화를 일으킬 수 있다는 다른 연구를 인용했다[8].\n\n아래 사람 중독 자료는 병솔나무가 아니라 유칼립투스 정유에 관한 것이며, 병솔나무 잎이나 그 정유에 그대로 적용할 수 있는지는 확인하지 못함. 유칼립투스 정유를 삼킨 어린이 109건 분석에서는 100% 정유 5 mL 이상이면 뚜렷한 의식 저하가, 2–3 mL에서도 가벼운 의식 저하가 생길 수 있었다[25].",
 "유칼립투스 정유 사람 사례가 이 종의 안전성처럼 읽히지 않도록 단서를 붙임; [25] 초록에는 1,8-시네올 언급이 없어 '1,8-시네올이 많은' 수식과 [25] 인용 제거; 식품원료는 잎이지 정유가 아님을 [1]로 명시")
rep('safety',"유럽 의약품청은 1,8-시네올 함유 정유가 후두경련을 일으킬 수 있어 30개월 미만 소아에게 금기로 정했다고 WebSearch 요약으로만 확인했다[28].",
 "유럽 의약품청은 유칼립투스 정유 의약품을 후두경련 위험 때문에 30개월 미만 소아에게 쓰지 않도록 하고, 먹는 제품은 12세 이상에만 쓰도록 했다고 WebSearch 요약으로만 확인했다[28].",
 "검색 요약상 EMA 금기는 '유칼립투스 정유' 의약품 대상이지 '1,8-시네올 함유 정유' 일반이 아님; 경구 12세 이상 조건 추가")
# compounds
C={c['name']:c for c in d['compounds']}
e=C['Eucalyptol']
old=e['activity_ko']; e['activity_ko']="정유의 품질 지표 성분으로 제안됨; 쥐 고열량 식이 모델에서 0.88 mg/kg 단독 투여로 체중 증가·지방 축적 감소와 항염 작용(산화 스트레스 지표에 대한 효과는 성분마다 달랐음)"
changes.append({"where":"compounds.Eucalyptol.activity_ko","before":old,"after":e['activity_ko'],"why":"[19] 초록: 세 테르펜이 산화 스트레스에 '서로 다른 효과'를 보였다고만 함"})
old=e['content_text']; e['content_text']=old.replace("정유 40.44%;","정유 40.44%(인도, 부위 미기재);")+"; 잎 정유 34.2%(이란)"
e['source']=sorted(set(e['source']+[34]))
changes.append({"where":"compounds.Eucalyptol.content_text","before":old,"after":e['content_text'],"why":"[14] 초록에 부위 표기 없음; [34] 잎 정유 34.2% 추가"})
# assays
a=d['assays'][0]
old=a['part']; a['part']="잎 정유(그늘에 말린 잎, 물 증류)"
a['conditions']['sample_prep']=a['conditions']['sample_prep'].replace("클레벤저 장치로 3시간 수증기 증류","클레벤저 장치로 3시간 물 증류(hydro-distillation)")
changes.append({"where":"assays[0].part/sample_prep","before":old,"after":a['part'],"why":"[7] 전문: hydro-distilled"})
# sources
src={s['n']:s for s in d['sources']}
src[28]['title']="European Medicines Agency HMPC — Eucalypti aetheroleum(유칼립투스 정유) 단일약재 평가 요약: 30개월 미만 소아 금기(후두경련 위험), 경구 제품 12세 이상 (EMA 사이트는 이 환경에서 열리지 않아 WebSearch 요약으로만 확인)"
src[28]['url']="https://www.ema.europa.eu/en/medicines/herbal/eucalypti-aetheroleum"
src[4]['title']="Australian Native Plants Society (Australia) — Callistemon citrinus (syn. Melaleuca citrina) 식물 정보; Craven LA, Novon 2006;16(4):468-475(doi:10.3417/1055-3177(2006)16[468:NCIMFA]2.0.CO;2)의 Callistemon→Melaleuca 통합 (이 환경에서 페이지를 열지 못해 WebSearch 요약으로만 확인)"
changes.append({"where":"sources[28]","before":"superseded PDF url","after":src[28]['url'],"why":"대체된(superseded) 문서 대신 EMA 현행 요약 페이지로; 내용도 유칼립투스 정유 대상으로 정정"})
d['sources'].append({"n":36,"title":"1,8-cineole as a multi-target anticancer candidate integrating molecular mechanisms, pharmacokinetics and translational perspectives — Biomed Pharmacother 2026;199:119467 (초록, 리뷰) (PMID 42070456)","url":"https://doi.org/10.1016/j.biopha.2026.119467","publisher":"PubMed","accessed":"2026-11-02"})
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open(p.replace('dossier.json','_review/changes.json'),'w'),ensure_ascii=False,indent=1)
print(len(changes))
