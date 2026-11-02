import json
p='dossier.json'; d=json.load(open(p))
changes=[]
S={s['key']:s for s in d['sections']}
def rep(key,old,new,why):
    b=S[key]['body']; assert b.count(old)==1,(key,old); S[key]['body']=b.replace(old,new)
    changes.append({"where":f"sections.{key}","before":old,"after":new,"why":why})
rep('overview','나머지 연구 대부분은 꽃 핀 지상부 전체를 시료로 썼다[2, 3, 5, 8].','나머지 연구는 대부분 지상부나 부위를 밝히지 않은 마른 풀을 시료로 썼다[2, 3, 5, 8].',
    '[3]은 부위를 밝히지 않은 마른 풀(dried plant), [2]는 개화기 채집 풀(부위 미기재), [8]만 지상부라고 씀 — "꽃 핀 지상부 전체"는 과장')
rep('history','러시아에서는 이 풀이 노인의학에서','러시아어 총설에서는 이 풀이 노인의학에서','[36]은 러시아어 총설 한 편이며 러시아 전체의 이용 실태를 말하지 않음')
rep('history','1950년 벨기에에서는 고혈압용 차에','1950년 벨기에 약학지에는 고혈압용 차에','[28]은 J Pharm Belg 서지 정보만 있고 초록이 없어 사례 발생 국가는 확인 불가 — 학술지 기준으로 표현')
rep('history','1980년대 프랑스 연구에서는 이 풀의 플라보노이드 분획이','1986년 프랑스어 논문에서는 이 풀의 플라보노이드 분획(A1)이','[34] 1986년, 프랑스어 논문(영문 초록); 0.16 mg/mL는 분획 A1 값')
rep('biology','세르비아에서는 6–9월에 꽃이 피고','6–9월에 꽃이 피고','[2] 본문은 일반 형태 설명으로 쓰며 세르비아에 한정하지 않음')
rep('processing','사람 장내 미생물과 배양하면 엘라그산이 우로리틴 C로 바뀌고 플라보노이드 배당체가 사라졌다[4].',
    '사람 분변 미생물(공여자 3명)과 24시간 배양하자 엘라그산과 퀘르세틴·켐페롤 글루쿠로나이드가 사라졌고, 우로리틴 C는 공여자 1명의 시료에서만 검출되었다[4].',
    '[4] 전문: 우로리틴 C는 D1 시료에서만 검출, 글루쿠로나이드는 세 공여자 시료 모두에서 없어짐 — 일반화 표현 정정')
C={c['name']:c for c in d['compounds']}
def crep(name,field,new,why):
    old=C[name][field]; C[name][field]=new
    changes.append({"where":f"compounds[{name}].{field}","before":old,"after":new,"why":why})
for n in ['Gallic acid','Ellagic acid']:
    crep(n,'part','마른 풀(부위 명시 없음)','[3] 재료는 "dried lady\'s mantle plant", [2]는 개화기 채집 풀로 부위를 쓰지 않음 — "지상부" 근거 없음')
for n in ['Catechin','Quercetin','Luteolin 7-O-glucoside','Kaempferol 3-O-glucoside','Caffeic acid','Rutin']:
    old=C[n]['part']
    new={'Catechin':'개화기 채집 풀(부위 명시 없음)'}.get(n,'개화기 채집 풀(부위 명시 없음)·지상부' if n in ('Caffeic acid','Rutin') else '개화기 채집 풀(부위 명시 없음)')
    crep(n,'part',new,'[2] Methods 는 개화기 채집·자연 건조만 쓰고 부위를 밝히지 않음([8] 터키 시료만 지상부)')
crep('Quercetin','activity_ko','혈관 이완 작용을 보인 메탄올 추출물에 특히 많았음(인과는 확인되지 않음)[11]','[11] 초록은 메탄올 추출물에 퀘르세틴이 많다고만 쓰며 퀘르세틴과 혈관 이완을 직접 연결하지 않음')
crep('Ellagic acid','activity_ko','사람 분변 미생물 배양에서 사라지고 공여자 1명 시료에서 우로리틴 C가 검출됨[4]','[4] 우로리틴 C는 D1 시료에서만 검출')
A=d['assays']
old=A[2]['part']; A[2]['part']='개화기 채집 풀(세르비아 블라시나 호수 자생지, 2017년 한여름 채집, 자연 건조; 부위는 본문에 없음)'
changes.append({"where":"assays[2].part","before":old,"after":A[2]['part'],"why":"[2] Methods: 'collected at the flowering stage in midsummer 2017', 부위 미기재"})
old=A[1]['source']; A[1]['source']=[4,5]
changes.append({"where":"assays[1].source","before":str(old),"after":"[4, 5]","why":"rationale 이 [5]를 인용하므로 source 에 포함"})
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
