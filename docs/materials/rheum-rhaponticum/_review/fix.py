import json
from pathlib import Path
P=Path(__file__).resolve().parent.parent/'dossier.json'
d=json.load(open(P))
changes=[]
def rep(where,obj,key,old,new,why):
    assert old in obj[key], (where,old)
    obj[key]=obj[key].replace(old,new); changes.append({"where":where,"before":old,"after":new,"why":why})
S={s['key']:s for s in d['sections']}
# sources swap 36<->37
src={s['n']:s for s in d['sources']}
a,b=src[36],src[37]
a['n'],b['n']=37,36
b['title']="한국소비자원 일반식품 '루바브' 제품 10개 조사(2026년 1월 13일 발표) 보도 — 데일리팜·한국경제·식품투데이 등 여러 언론 보도를 WebSearch 요약으로 확인, 원문 보도자료는 네트워크 제한으로 열지 못함(핵심 근거 아님)"
d['sources']=sorted(d['sources'],key=lambda s:s['n'])
changes.append({"where":"sources[36],[37]","before":"[36]=유산균 루바브 주스 논문, [37]=한국소비자원 보도","after":"[36]=한국소비자원 보도, [37]=유산균 루바브 주스 논문","why":"본문·compounds 에서 [36]은 소비자원, [37]은 주스 발효 내용으로 인용되어 번호가 서로 뒤바뀌어 있었음"})
src[7]['title']=src[7]['title'].replace("초록만 확인)","초록만 확인 — 초록이 R. rhaponticum을 'garden or dietary rhubarb'로 부름)")
o=S['overview']
rep('sections.overview',o,'body',"뿌리는 이 목록의 일반 식품원료 부위가 아니며, 뿌리 추출물은 개별인정을 받은 건강기능식품 원료로만 따로 올라 있다[2].",
 "뿌리는 이 목록의 일반 식품원료 부위가 아니며(개별인정 제2019-6호 행에도 '줄기, 잎만 식품원료로 사용가능'이라 적힘), 뿌리 추출물은 건강기능식품 개별인정 원료로, 뿌리 향료는 식품첨가물 천연향료(Rhubarb root)로 따로 올라 있다[2].",
 "I1020 원자료에 식품첨가물 '천연향료(Rhubarb root)' 행도 있어 '개별인정 원료로만'은 과함; 2019-6호 행의 사용조건 원문 추가")
rep('sections.overview',o,'body',"먹는 잎자루에는 신맛을 내는 옥살산이 많고, 넓은 잎몸을 먹고 옥살산 중독을 일으킨 사례가 보고되어 잎몸은 보통 버린다[20, 21, 23].",
 "루바브는 옥살산이 많은 식품으로 꼽히고[23], 잎을 먹은 어린이의 옥살산 중독 사례가 보고되었다(사례 보고는 종을 밝히지 않음)[20, 21]. 식약처 목록은 잎도 사용가능 부위로 적지만, 잎몸 섭취의 안전 기준은 확인하지 못함.",
 "[20, 21, 23] 어디에도 '신맛'·'잎몸은 보통 버린다'는 내용이 없음; 목록의 잎 허용과 독성 사례의 긴장을 명시")
h=S['history']
rep('sections.history',h,'body',"자궁·유방 통증 같은 생식기 관련 증상에도 쓰였다고 정리되어 있다[5].","자궁·유방 통증 같은 생식기 관련 증상에도 쓰였다고 정리되어 있다[5, 6].","[5] 전문 추출본에서 학명이 빠져 종 확인이 어려워, 같은 연구진의 [6] 서론(루바브 전통 용도: 생식기 질환·심통)으로 보강")
rep('sections.history',h,'body',"일본에서는 에도 시대 이후 '대황'이라는 생약의 기원 식물이 여러 번 바뀌었고, 유럽을 거쳐 들어온 '러시아 대황'과 중국산 대황이 따로 유통되는 등 이름과 원료가 오래 혼동되었다[35].",
 "다른 종인 약용 대황 생약도 기원이 오래 혼동되었다; 일본에서는 에도 시대부터 '대황' 생약의 기원 식물이 바뀌어 왔고, 러시아를 거쳐 유럽에서 들어온 '러시아 대황'이 따로 알려졌으며, 메이지 이후에는 기원이 다른 두 대황 제품이 따로 유통되었다[35].",
 "[35] 초록은 약용 대황 생약 이야기이며 '러시아 대황과 중국산 대황이 따로 유통'이 아니라 메이지 이후 기원이 다른 두 제품이 따로 유통됐다고 씀; 루바브 자료로 읽히지 않게 약용 대황임을 명시")
rep('sections.history',h,'body',"평균차는 −15.12점이었으나 이질성이 컸다[10].","평균차는 −15.12점이었으나 이질성이 컸고(I² 93%), 포함 시험 중 1건은 다른 시험 참가자의 연장 관찰이었다[10, 11].","[10] 전문: I²=93%; 포함된 Hasper 2009(39·41명)는 [11] 초록상 Heger 2006 참가자의 연장 관찰이라 중복 표기")
b_=S['biology']
rep('sections.biology',b_,'body',"붉은 잎자루 품종에서는 시아니딘 배당체 같은 안토시아닌이 색을 내고 그 함량은 발달 단계에 따라 달라진다[32].",
 "붉은 잎자루 식용 루바브 품종(폴란드 'Malinowy', 종명 미기재)에서는 시아니딘 배당체 같은 안토시아닌이 색을 내고 그 함량은 발달 단계에 따라 달라진다[32].",
 "[32]는 종명을 밝히지 않은 식용 루바브 품종 연구로, R. rhaponticum 자료로 단정할 수 없음")
rep('sections.biology',b_,'body',"대신 퀘르세틴 유도체가 상당량 들어 있다[7].","대신 퀘르세틴 유도체가 상당량 들어 있다[7]. 다만 [7]은 R. rhaponticum을 '가든 또는 식용 루바브'라 불러, 시료가 가든 루바브 계통일 가능성을 배제할 수 없다[7, 34].",
 "[7] 초록이 'garden or dietary rhubarb Rheum rhaponticum'이라 적음 — 가든 루바브 혼동 가능성 표시")
r=S['related_species']
rep('sections.related_species',r,'body',"학명과 부위를 함께 확인해야 한다[34].","학명과 부위를 함께 확인해야 한다[7, 34].","[7]도 R. rhaponticum을 garden rhubarb로 부름")
rep('sections.related_species',r,'body',"21건 중 15건에서 라폰티신이 검출되어 비공정 대황으로 분류되었다[26].","21건 중 15건에서 라폰티신이 검출되어 비공정 대황으로 분류되었으나, 이 시료들의 종은 밝혀지지 않았다[26].","[26] 전문 4.1절: 비공정 시료의 종 판별은 어렵다고 씀 — 루바브로 오독 방지")
p=S['processing']
rep('sections.processing',p,'body',"잎자루로 만든 식이섬유 조제물은","종을 밝히지 않은 루바브 잎자루로 만든 식이섬유 조제물은","[5] 전문은 'rhubarb stalks'로만 적어 종 미기재")
rep('sections.processing',p,'body',"루바브 주스의 옥살산을 줄이려고","종을 밝히지 않은 루바브 주스(이란 연구)의 옥살산을 줄이려고","[37] 초록은 'rhubarb'로만 적음")
rep('sections.processing',p,'body',"언론 보도에 따르면 2026년 1월 한국소비자원은 일반식품 루바브 제품 10개를 조사해 뿌리 추출물이 아닌 원료를 썼고 라폰티신이 기능성 인정 기준(1일 2.52 mg)의 약 1% 이하였다고 발표했다[36]. 이 내용은 원문 보도자료를 열어 확인하지 못함.",
 "언론 보도에 따르면 2026년 1월 13일 한국소비자원은 일반식품 루바브 제품 10개를 조사해 모두 뿌리 추출물이 아닌 원료를 썼고, 라폰티신이 검출되지 않거나 1일 섭취량 기준 0.03 mg 이하로 기능성 인정 기준(1일 2.52 mg)의 최대 약 1%였다고 발표했다[36]. 이 내용은 여러 언론 보도로 확인했으나 원문 보도자료는 열지 못함.",
 "검색 결과(여러 언론)로 발표일·0.03 mg 이하 수치 확인해 보강")
g=S['genetics']
rep('sections.genetics',g,'body',"이 효소 활성은 루바브 뿌리줄기에서 처음 확인되었다[30].","1978년 R. rhaponticum 뿌리줄기 무세포 추출물에서 이 효소 활성이 확인되었다[30].","[30] 초록에 '처음'이라는 표현 없음")
s=S['safety']
rep('sections.safety',s,'body',"원인이 옥살산인지 안트라퀴논인지를 따진 보고도 있다[20, 21, 22].","원인이 옥살산인지 안트라퀴논인지를 따진 보고도 있다(세 보고 모두 초록이 없고 종을 밝히지 않음)[20, 21, 22].","[20–22] 제목·MeSH 만 확인 가능, 종 미기재")
rep('sections.safety',s,'body',"당뇨병 환자가 루바브를 과량 먹은 뒤","경미한 당뇨병성 신증이 있던 1형 당뇨병 환자가 루바브를 과량 먹은 뒤","[18] 초록: 1형 당뇨·기존 경미한 신증 — 위험군 조건 명시")
# compounds
C={c['name']:c for c in d['compounds']}
note="(두 종(루바브·가든 루바브)을 함께 서술한 결과)"
for nm in ['Rhaponticin','Desoxyrhaponticin','Astringin','Resveratrol','Emodin','Chrysophanol','Physcion']:
    c=C[nm]; old=c['content_text']; i=old.index('[6]')
    c['content_text']=old[:i]+note+old[i:]
    changes.append({"where":f"compounds.{nm}.content_text","before":old,"after":c['content_text'],"why":"[6] 전문 3.1절은 루바브와 가든 루바브의 잎자루·뿌리 성분을 종 구분 없이 함께 서술함"})
old=C['Quercetin']['content_text']
C['Quercetin']['content_text']=old.replace("주된 골격[6]","주된 골격"+note+"[6]")
changes.append({"where":"compounds.Quercetin.content_text","before":old,"after":C['Quercetin']['content_text'],"why":"[6] 두 종 공통 서술"})
old=C['Rhaponticin']['content_text']
C['Rhaponticin']['content_text']=old.replace("1일 2.52 mg(언론 보도 WebSearch 요약)[36]","1일 2.52 mg(한국소비자원 발표 언론 보도)[36]")
cy=C.pop('Cyanidin 3-O-rutinoside')
d['compounds']=[c for c in d['compounds'] if c['name']!='Cyanidin 3-O-rutinoside']
changes.append({"where":"compounds.Cyanidin 3-O-rutinoside","before":cy['content_text'],"after":"(삭제)","why":"[32]는 종명 미기재 식용 루바브 'Malinowy'의 조직배양 신초 값으로 R. rhaponticum 성분 자료가 아님(본문 biology 에 종 미기재로 남김)"})
# assays
A=d['assays'][0]
for k,old,new,why in [
 ('part',"잎자루·뿌리(줄기)의 메탄올 추출 후 부탄올 분획, 폴란드 식물원 재배 시료","잎자루·뿌리/뿌리줄기의 메탄올 추출 후 부탄올 분획, 폴란드 루블린·우치 식물원 기증 시료(루바브·가든 루바브 두 종)","원문 2.2절: 두 종을 두 식물원에서 받음; '뿌리(줄기)'는 줄기로 오독될 수 있음"),
 ('content',"잎자루 179개, 뿌리 346개 대사체 확인;","잎자루 179개, 뿌리/뿌리줄기 346개 대사체 확인(종별로 나누지 않은 수);","원문 3.1절은 두 종을 묶어 서술"),
]:
    assert old in A[k]; A[k]=A[k].replace(old,new); changes.append({"where":f"assays[0].{k}","before":old,"after":new,"why":why})
old=A['conditions']['column']; A['conditions']['column']="Waters CORTECS T3(원문 표기 'CORTEX T3'), 150 mm × 2.1 mm, 2.7 µm, 프리칼럼 장착"
changes.append({"where":"assays[0].conditions.column","before":old,"after":A['conditions']['column'],"why":"원문 'equipped with a pre-column' — 전단 칼럼이 분석 칼럼처럼 읽히지 않게 정리"})
old=A['rationale']; A['rationale']=old.replace("같은 종 두 부위를 같은 조건에서 비교한 분석이다","루바브와 가든 루바브의 두 부위를 같은 조건에서 비교한 분석이다(성분 서술은 두 종 공통)")
changes.append({"where":"assays[0].rationale","before":old,"after":A['rationale'],"why":"[6]은 두 종 비교 연구"})
B=d['assays'][1]; old=B['rationale']
B['rationale']=old.replace("; 전문 확인 못함[7].","; 전문 확인 못함, 원문이 이 종을 '가든 루바브'로도 불러 종 동정에 주의[7].")
changes.append({"where":"assays[1].rationale","before":old,"after":B['rationale'],"why":"[7] 초록의 'garden or dietary rhubarb' 표기"})
json.dump(d,open(P,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open(Path(__file__).parent/'changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
