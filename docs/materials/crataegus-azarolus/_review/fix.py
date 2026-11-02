import json,re
P='/home/user/hfoodguide-wave3/docs/materials/crataegus-azarolus/dossier.json'
d=json.load(open(P))
S={s['key']:s for s in d['sections']}
changes=[]
def rep(key,old,new,why):
    b=S[key]['body']; assert old in b,(key,old)
    S[key]['body']=b.replace(old,new); changes.append({"where":f"sections.{key}","before":old,"after":new,"why":why})
rep('overview','지중해 동부와 서아시아 일대에서 자라며 열매를 먹는 산사나무로 알려져 있다[22][24].',
 '튀니지·튀르키예·이스라엘·요르단 등 지중해 연안과 서아시아에서 자라며, 열매를 먹고 약용으로도 써 온 산사나무다[4][9][15][19].',
 'WebSearch 요약만 본 [22][24] 대신 PubMed로 확인한 1차 논문으로 근거 교체')
rep('overview','건강기능식품 고시형 원료의 원재료로 올라 있지는 않다[1].',
 '건강기능식품 기능성 원료 고시에서 이 종을 원재료로 하는 원료는 이번 조사에서 찾지 못함.',
 '[1](식품원료 목록)은 건강기능식품 고시 여부를 말하지 않음')
rep('history','아자롤은 먹을 수 있는 열매를 얻기 위해 오래 재배되어 온 과수이지만, 오늘날 재배 규모는 매우 작다는 원예 기관의 설명이 있다(WebSearch 요약으로만 확인)[24].',
 '튀니지 연구진은 아자롤이 열매와 잎을 얻기 위해 재배된다고 적었다[2].',
 '[24]는 WebSearch 요약만 있고 원문을 열지 못함 — [2] 전문 서론 문장으로 교체')
rep('history','튀니지 연구진은 열매 추출물이 설사·소화기 통증에 쓰여 왔다는 전통 이용을 소개했다[2][6].',
 '튀니지 연구진은 아자롤 추출물이 소화기·요로 통증과 설사에 쓰여 왔다고 소개했다[2][3].',
 '[2] 전문은 소화기·요로 통증, [3] 전문은 설사 이용을 적음; [6] 초록에는 전통 이용 언급 없음')
rep('biology','꽃봉오리의 총페놀은 노란 열매 변종이 더 많았다(건조중량 100 g당 1638.7 대 1415.5 mg 갈산 당량)[5].',
 '꽃(꽃봉오리·핀 꽃) 에틸아세테이트 추출물의 총페놀은 노란 열매 변종이 더 많았다(건조중량 100 g당 1638.7 대 1415.5 mg 갈산 당량)[5].',
 '[5] 초록은 이 값을 꽃봉오리에 한정하지 않음(꽃봉오리·핀 꽃 추출물 비교)')
rep('related_species','이 원료들은 학명과 사용 부위가 다르므로 아자롤루스산사 자료와 섞어 읽으면 안 된다[1].',
 '이 원료들은 학명이 다르고, 원료마다 사용 부위와 사용 조건(예: 산사나무 잎·꽃은 제한적사용, 서양산사자 잎은 사용가능)이 달라 아자롤루스산사 자료와 섞어 읽으면 안 된다[1].',
 'I1020 원자료: 열매가 사용 부위인 원료도 많아 \"사용 부위가 다르다\"는 일반화가 부정확')
rep('related_species','큐 목록은 이를 변종 var. aronia로 다룬다(WebSearch 요약으로만 확인)[23].',
 '튀니지·이라크 연구들은 이를 변종 C. azarolus var. aronia로 적고[5][14][16], 큐 목록도 변종으로 다룬다(WebSearch 요약으로만 확인)[23].',
 'WebSearch 요약 외에 PubMed 논문 근거 추가')
rep('cultivation','이 연구는 열매 무게·과육 비율이 우수한 20개 개체를',
 '이 연구는 정량 형질 평가에서 우수한 20개 개체를',
 '[9]는 \"superior qualities\"로만 적음, 과육 비율 근거 없음')
rep('cultivation','원예 기관 설명에 따르면 야생형은 주로 남프랑스·사르데냐·이탈리아에서 소규모로 재배된다(WebSearch 요약으로만 확인)[24]. ',
 '','[24] 원문을 열지 못한 WebSearch 요약뿐이라 삭제')
rep('safety','건강기능식품 고시형 원료가 아니므로 고시된 섭취 시 주의사항도 없다[1].',
 '건강기능식품 기능성 원료 고시에서 이 종을 찾지 못해 고시된 섭취 시 주의사항도 확인하지 못함.',
 '[1]은 건강기능식품 고시를 다루지 않음')
rep('safety','튀니지 연구에서 열매 달임액을 쥐에게 한 번에 최대 3500 mg/kg까지 먹였을 때 죽거나 행동 이상을 보인 개체가 없어, 반수치사량(LD50)이 3500 mg/kg보다 높다고 보고되었다[3]. 다만 같은 논문 본문에는 3200 mg/kg라는 수치도 함께 나와 표기가 일치하지 않는다[3].',
 '튀니지 연구에서 열매 달임액을 쥐에게 한 번 먹이고 24시간 관찰했을 때 최고 용량 3500 mg/kg까지 죽거나 행동 이상을 보인 개체가 없어, 반수치사량(LD50)이 3500 mg/kg보다 높다고 보고되었다[3]. 다만 같은 논문의 방법에는 최고 용량이 3000 mg/kg, 고찰에는 LD50이 3200 mg/kg보다 높다고 적혀 있어 표기가 일치하지 않는다[3].',
 '[3] 전문: 방법 3000, 결과 3500, 고찰 3200 mg/kg; 관찰 24시간')
rep('safety',' 원예 기관은 씨에 독성 물질이 있으니 먹을 때 씨를 빼라고 안내한다(WebSearch 요약으로만 확인)[24].',
 ' 씨(핵)의 독성 여부에 대한 1차 자료는 이번 조사에서 확인하지 못함.',
 '[24] 원문을 열지 못한 WebSearch 요약뿐 — 안전성 주장으로 쓰기에 근거 부족')
rep('safety','심장약이나 혈압약을 먹는 사람은 산사 제품을 고농도로 먹기 전에 의료진과 상의하는 것이 안전하다[20][25].',
 '연구진은 이 용량에서 함께 써도 된다고 보았으나[20], 심장약이나 혈압약을 먹는 사람은 산사 제품을 고농도로 먹기 전에 의료진과 상의하는 것이 좋다.',
 '[20]은 함께 투여해도 된다고 결론 — 상의 권고는 출처의 주장이 아니므로 인용 분리')
# compounds
C={c['name']:c for c in d['compounds']}
def crep(name,field,new,why):
    old=C[name][field]; C[name][field]=new; changes.append({"where":f"compounds[{name}].{field}","before":old,"after":new,"why":why})
crep('Chlorogenic acid','content_text','LC-ESI-MS로 확인한 8개 페놀 가운데 주성분[2]. 원문은 \'406,975 ppm\'으로 적었으나 기준 물질량·단위가 분명하지 않아(그대로 읽으면 약 41%) 함량값으로 쓰지 않음',
 '[2] 전문에 정량 방법·검량선 없이 ppm만 적힘 — 기준 불명 값을 함량처럼 쓰지 않음')
crep('Hyperoside','content_text','열매 달임액의 주 플라보노이드[2](원문 \'140,949 ppm\'은 기준 불명이라 함량값으로 쓰지 않음); 노란 아자롤 잎과 열매의 주 페놀[4]',
 '기준 불명 ppm 값')
crep('Hyperoside','activity_ko','에틸아세테이트 추출물에서 분리한 성분이 생쥐 림프구·대식세포 기능을 조절(세포, 부위는 초록에 명시 없음)[12]',
 '[12] 초록은 부위(잎)를 밝히지 않음')
crep('Procyanidin B2','activity_ko','이 종에서 추출한 프로시아니딘(부위는 초록에 명시 없음)이 이소프로테레놀 유도 심부전 쥐의 심장 지표를 낮춤(동물)[17]',
 '[17] 초록에 추출 부위 없음 — 열매 결과로 읽히지 않게 명시')
crep('Pectin','name','Polysaccharides','[8]은 다당류라고만 함(우론산 29.39%) — 펙틴 동정 근거 없음')
crep('Pectin','name_ko','다당류(우론산 함유)','같은 이유')
a=d['assays'][0]; old=a['content']
a['content']='클로로겐산이 주성분, 하이퍼로사이드가 주 플라보노이드(원문은 각각 406,975 ppm·140,949 ppm으로 적었으나 기준 물질량·단위가 불분명해 함량값으로 쓰지 않음)[2]'
changes.append({"where":"assays[0].content","before":old,"after":a['content'],"why":"기준 불명 ppm 값을 함량처럼 제시하지 않음"})
# drop source 24 and renumber
used=set()
txt=json.dumps({k:v for k,v in d.items() if k!='sources'},ensure_ascii=False)
for m in re.finditer(r'\[(\d+)\]',txt): used.add(int(m.group(1)))
for c in d['compounds']+d['assays']: used|=set(c.get('source',[]))
old_nums=[s['n'] for s in d['sources'] if s['n'] in used]
mp={o:i+1 for i,o in enumerate(old_nums)}
print('removed',[s['n'] for s in d['sources'] if s['n'] not in used])
def renum(t): return re.sub(r'\[(\d+)\]',lambda m:'['+str(mp[int(m.group(1))])+']',t)
for s in d['sections']: s['body']=renum(s['body'])
for c in d['compounds']+d['assays']:
    for k,v in c.items():
        if isinstance(v,str): c[k]=renum(v)
    c['source']=[mp[x] for x in c['source']]
    if 'conditions' in c: pass
d['sources']=[dict(s,n=mp[s['n']]) for s in d['sources'] if s['n'] in used]
json.dump(d,open(P,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open(P.replace('dossier.json','_review/changes.json'),'w'),ensure_ascii=False,indent=1)
print(len(changes))
