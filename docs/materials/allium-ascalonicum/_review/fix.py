import json,sys
p='/home/user/hfoodguide-wave3/docs/materials/allium-ascalonicum/dossier.json'
d=json.load(open(p))
changes=[]
def sec(key): return next(s for s in d['sections'] if s['key']==key)
fld = 'body' if 'body' in d['sections'][0] else 'text'
def rep_sec(key,old,new,why):
    s=sec(key); assert old in s[fld],(key,old); s[fld]=s[fld].replace(old,new); changes.append({"where":f"sections.{key}","before":old,"after":new,"why":why})
def comp(name): return next(c for c in d['compounds'] if c['name']==name)
def rep_comp(name,field,old,new,why):
    c=comp(name); assert old in c[field],(name,old); c[field]=c[field].replace(old,new); changes.append({"where":f"compounds[{name}].{field}","before":old,"after":new,"why":why})

rep_sec('overview',"영문명 'Shallot(샬롯)'으로","영문명 'Shallot'으로","I1020 원 행의 ENG_NM 은 'Shallot' 뿐이고 '(샬롯)'은 목록에 없음")
rep_sec('related_species',"다른 리뷰는 A. cepa var. aggregatum 또는 var. ascalonicum이라는 변종 이름을 쓰고[4]","다른 리뷰는 샬롯을 양파와 같은 종(A. cepa)의 한 변종(var.)으로 다루고[4]","[4] PMC 전문에서 학명 이탤릭이 빠져 변종 이름(aggregatum·ascalonicum)을 확인할 수 없음; '양파와 같은 종의 변종'까지만 확인")
rep_sec('processing',"말린 겉껍질은 퀘르세틴의 83.3%가 비배당체로, 속살(배당체 99.2%)보다 사람 혈중 퀘르세틴 노출(AUC)이 약 두 배였다[13].","말린 겉껍질은 퀘르세틴의 83.3%가 비배당체로, 9명 단회 섭취 교차시험에서 속살(배당체 99.2%)보다 혈중 퀘르세틴 노출(AUC)이 약 두 배였다[13].","[13] 초록: 자원자 9명, 단회 섭취 무작위 교차시험 — 규모를 밝혀 과장 방지")
rep_sec('genetics',"배가반수체 샬롯(DHA)의 유전자 서열을 기준으로 전사체 SNP를 분석해 25,462개 유전자를 8개 염색체에 고정하고 고밀도 연관 지도를 만들었다[23].","배가반수체 샬롯(DHA)의 유전자 서열을 기준으로 전사체 SNP를 분석해 25,462개 유전자를 8개 염색체에 고정했고, 샬롯(DHA)×구형 양파(DHC) 배가반수체 교배 집단으로 A. cepa 고밀도 연관 지도를 만들었다[23].","[23] 초록: 연관 지도는 DHA×DHC(일반 양파) 집단으로 만든 A. cepa 지도 — 샬롯 단독 지도로 읽히지 않게 고침")
rep_sec('cultivation',"샬롯 노란줄무늬 바이러스(SYSV)는 양파 위황병 바이러스와 다른 포티바이러스로 정리되었다[33].","샬롯 노란줄무늬 바이러스(SYSV)는 양파 황색위축 바이러스(OYDV)·리크 노란줄무늬 바이러스(LYSV)와 다른 포티바이러스로 정리되었다[33].","[33] 초록: OYDV·LYSV 모두와 구별됨; 바이러스 이름을 원문 약어와 함께 명확히")
rep_sec('safety',"알레르기 비염 환자 16명 시험에서 하루 3 g(비늘줄기 약 1.5개) 샬롯을 4주 먹었을 때 이상반응은 위약과 다르지 않았다[16].","알레르기 비염 환자 16명 무작위 이중맹검 시험에서 세티리진과 함께 하루 3 g(비늘줄기 약 1.5개) 샬롯을 4주 먹었을 때 이상반응은 위약군(세티리진+위약)과 다르지 않았다[16].","[16] 초록: 두 군 모두 세티리진 복용 — 병용 조건을 밝힘")
rep_sec('safety',"거위에게 'green onions(A. ascalonicum)'를 먹인 사례와 시험에서 빈혈과 간 손상이 나타났다[30].","거위에게 'green onions(A. ascalonicum)'를 먹인 사례와 시험(시험 개체 3마리)에서 빈혈과 간 손상이 나타났으나, 동물 결과이고 논문이 'green onions'를 그 학명으로 적었을 뿐 샬롯 비늘줄기인지는 확인하지 못함[30].","[30] 초록: 3마리 급여 시험, 'green onions' 표기 — 종 동정 불확실·동물 결과임을 밝힘")

rep_comp("Quercetin 4'-O-glucoside","content_text","34개 샬롯 계통 56.1–287.9 mg/100 g(건조중량), 최고값은 Aggregatum 샬롯형 IPT241[3]","크로아티아 샬롯 34개 계통(A. × proliferum·A. × cornutum 포함) 56.1–287.9 mg/100 g(건조중량); 최고값은 Aggregatum 샬롯형 IPT241, 최저값은 Aggregatum이 아닌 계통 IPT210[3]","[3] 34계통에는 Aggregatum 이 아닌 주아형 양파(A. × proliferum·A. × cornutum)가 섞여 있고 최저값 IPT210 은 그쪽 계통")
rep_comp("Quercetin 3,4'-O-diglucoside","content_text","계통 최고 143.2 ± 17.5 mg/100 g(건조중량)[3]","계통 최고 143.2 ± 17.5 mg/100 g(건조중량, Aggregatum 샬롯형 IPT241)[3]","최고값 계통이 Aggregatum 인지 밝힘")
rep_comp("Quercetin","content_text","5.16–36.15 mg/100 g(건조중량)[3]","5.16–36.15 mg/100 g(건조중량; 최고 Aggregatum 샬롯형 IPT241, 최저는 Aggregatum이 아닌 IPT211)[3]","범위 하한 IPT211 은 A. × proliferum/cornutum 계통")
rep_comp("Isorhamnetin 4'-O-glucoside","content_text","5.0–59.2 mg/100 g(건조중량)[3]","5.0–59.2 mg/100 g(건조중량; 최고 Aggregatum 샬롯형 IPT239, 최저는 Aggregatum이 아닌 IPT210)[3]","범위 하한 IPT210 은 다른 분류군")

a=d['assays'][0]
old=a['content']; a['content']="크로아티아 샬롯 34개 계통(A. × proliferum·A. × cornutum 포함) 56.1–287.9 mg/100 g(건조중량); 최고 Aggregatum 샬롯형 IPT241 287.9[3]"
changes.append({"where":"assays[0].content","before":old,"after":a['content'],"why":"범위에 Aggregatum 이 아닌 분류군 포함"})
a=d['assays'][2]
old=a['compound_ko']; a['compound_ko']="이소알리인 등 ACSO 관련 대사물 13종"
changes.append({"where":"assays[2].compound_ko","before":old,"after":a['compound_ko'],"why":"[8] 전문: '13 ACSO-related metabolites'(글루타티온 등 전구체 포함)이지 ACSO 13종이 아님"})
n=d['nutrients'][0]
old=n['form']; n['form']="샬롯 비늘줄기 — 무기질(Prabawati 등 2026 리뷰 표 4 'Shallot bulbs' 열 재인용; 생것 여부는 표에 명시 없음)"
changes.append({"where":"nutrients[0].form","before":old,"after":n['form'],"why":"[4] 표 4 는 'Shallot bulbs' 로만 적고 생것이라고 밝히지 않음"})
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('/home/user/hfoodguide-wave3/docs/materials/allium-ascalonicum/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
