import json,re,sys
p='/home/user/hfoodguide-wave3/docs/materials/acer-platanoides/dossier.json'
d=json.load(open(p))
S={s['key']:s for s in d['sections']}
changes=[]
def rep(key,old,new,why):
    s=S[key]; assert old in s['body'],(key,old)
    s['body']=s['body'].replace(old,new); changes.append({"where":f"sections.{key}","before":old,"after":new,"why":why})
rep('overview','무환자나무과(Sapindaceae) 단풍나무속의 잎지는 큰키나무로, 식약처','무환자나무과(Sapindaceae) 단풍나무속의 잎지는 나무로[19], 식약처','과(科)는 [1]에 없고 [19] 제목에 있음; \'큰키나무\'는 인용 출처에서 확인 못함')
rep('overview','유럽 북부·동부에서는 자작나무와 함께 이 종의 봄 수액을 마시거나 발효해 왔다는 민족식물학 보고가 있다(검색 요약으로만 확인)[23].','유럽 북부·동부에서는 자작나무류와 노르웨이단풍이 가장 많이 쓰인 수액 나무였고, 수목 수액을 생으로 마시거나 가볍게 발효해 왔다는 민족식물학 총설이 있다(검색 요약으로만 확인)[23].','[23] 요약은 이용법을 수목 수액 전반에 대해 말함(이 종만의 이용법 아님), \'봄\' 근거 없음')
rep('history','러시아·우크라이나·벨라루스·발트 3국에서는 최근까지 수액 채취가 이어졌고 스칸디나비아·폴란드 등의 기록은 주로 과거의 것이라고 한다[23].','러시아·우크라이나·벨라루스·발트 3국에서는 최근까지 (주로 자작나무) 수액 채취가 중요한 활동이었으나, 오늘날에는 소수만 하는 드문 일로 여겨진다고 한다[23].','검색 요약에서 스칸디나비아·폴란드 관련 서술은 확인 못함; 최근까지 이어진 채취는 주로 자작나무 수액')
rep('history','북미에는 1756년 무렵 가로수로 들어왔고','미국 본토에는 1756년 무렵 가로수로 들어왔고','[9] 원문은 \'continental United States\'')
rep('cultivation','북미 서부에서는 2002년 어린 나무에서 흰가루병(Sawadaea bicornis)이 처음 보고되었다[9].','2002년 미국 아이다호·워싱턴 경계 지역의 어린 나무에서 흰가루병(Sawadaea bicornis)이 북미 첫 기록으로 보고되었다[9].','[9] 초록: 북미 최초 기록, 아이다호-워싱턴 경계')
rep('cultivation','독일 연구는 겨울철 물관 수액의 자당이','1996년 연구는 통나무 조각에서 가압·감압법으로 얻은 겨울철 물관 수액의 자당이','[26] 서지(J Exp Bot 1996) 확인, 저자 소속 국가는 확인 못함; 채취법이 일반 수액 채취와 다름을 명시')
rep('processing','유럽 북부·동부에서 이 종의 수액은 생으로 마시거나 음식·음료 재료로 쓰고, 가볍게 발효해 술로 만들었다고 요약되어 있다(원문 확인 못함)[23].','유럽 북부·동부에서 자작나무·노르웨이단풍 등 수목 수액은 생으로 마시거나 음식·음료 재료로 쓰고, 가볍게 발효해 술로 만들었다고 요약되어 있다(원문 확인 못함)[23].','[23] 이용법은 수목 수액 전반')
rep('processing',' 폴란드 남동부 수액 연구의 저자들은 지역의 단풍나무·자작나무 자원을 이용한 소규모 시럽 산업이 산주의 부수입원이 될 수 있다고 제안했다고 요약되어 있다[24]. 라트비아 연구는 노르웨이단풍 수액이 자작나무 수액보다 단백질과 항산화 활성이 높았고, 적정산도가 0.70 mmol NaOH/L였다고 요약된다(원문 확인 못함)[25].','','[24] 시럽 산업 제안은 검색 요약에서 확인 못함; [25] 라트비아 연구는 단풍나무 종명을 확인 못해(이 종 자료로만 쓰라는 원칙) 삭제')
rep('processing','수액 성분은 같은 종이라도 채취 시기·나무에 따라 크게 달라질 수 있어, 총당이 약 3.2%라는 보고와 1.083 g/100 mL라는 보고가 함께 있다[24, 27].','이 종 수액의 총당은 약 3.2%라는 보고와 1.083 g/100 mL라는 보고가 함께 있으나, 두 연구는 분석법(HPLC-CAD, HPLC-ELSD)과 채취 조건이 달라 직접 비교하기 어렵다(둘 다 검색 요약으로만 확인)[24, 27].','값 차이의 원인(시기·나무)은 출처가 말하지 않음; 분석법 차이로 고쳐 씀')
rep('safety','잎 추출물의 항균·단백분해효소 억제 활성은 시험관 결과일 뿐이다[21, 22].','메탄올 추출물의 트립신 억제(IC50 1.8 µg/mL; 추출 부위는 초록에서 확인하지 못함)[21]와 잎 추출물의 항균 활성[22]은 시험관 결과일 뿐이다.','[21] 초록은 이 종 추출물의 부위를 밝히지 않음(나무껍질·꽃·잎·줄기 중)')
# processing leading whitespace cleanup
S['processing']['body']=S['processing']['body'].replace('[23].\n','[23].\n')
# assay brand names
a=d['assays'][0]['conditions']
old=a['sample_prep']; a['sample_prep']=old.replace('Retsch 분쇄','분쇄기로 분쇄').replace('milliQ 물','초순수')
changes.append({"where":"assays[0].conditions.sample_prep","before":old,"after":a['sample_prep'],"why":"상표명 대신 일반명"})
old=a['standard']; a['standard']=old.replace('milliQ 물','초순수'); changes.append({"where":"assays[0].conditions.standard","before":old,"after":a['standard'],"why":"상표명 대신 일반명"})
# sources: drop 25, renumber
src=[s for s in d['sources'] if s['n']!=25]
for s in src:
    if s['n']==26:
        s['title']="The xylem sap of maple (Acer platanoides) trees — sap obtained by a novel method shows changes with season and height — J Exp Bot 1996;47(294):123-133 (서지는 검색 요약으로 확인) — 초록 요약만 확인, 원문은 이 환경에서 열지 못함"
mp={26:25,27:26}
for s in src:
    s['n']=mp.get(s['n'],s['n'])
d['sources']=src
txt=json.dumps(d,ensure_ascii=False)
def fixref(m):
    nums=[int(x) for x in re.split(r',\s*',m.group(1))]
    assert 25 not in nums
    return '['+', '.join(str(mp.get(n,n)) for n in nums)+']'
txt=re.sub(r'\[(\d+(?:,\s*\d+)*)\]',fixref,txt)
d=json.loads(txt)
def fixlist(o):
    if isinstance(o,dict):
        for k,v in o.items():
            if k=='source' and isinstance(v,list): o[k]=[mp.get(n,n) for n in v]
            else: fixlist(v)
    elif isinstance(o,list):
        for x in o: fixlist(x)
fixlist(d)
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('/home/user/hfoodguide-wave3/docs/materials/acer-platanoides/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
