import json,sys
p=sys.argv[1]
d=json.load(open(p))
S={s['key']:s for s in d['sections']}
ch=[]
def rep(key,old,new,why):
    b=S[key]['body']; assert old in b,(key,old); S[key]['body']=b.replace(old,new); ch.append({"where":f"sections.{key}","before":old,"after":new,"why":why})
rep('overview',"예전 논문에는 Phoca groenlandica라는 이름도 함께 쓰였다[6, 19, 24]","예전 논문에는 Phoca groenlandica라는 이름도 함께 쓰였다[6, 19, 21]",
    "[24] 제목은 'Phagophilus groenlandicus'(오기)로 Phoca groenlandica 사용 근거가 아님 → Phoca groenlandica를 제목에 쓴 [21]로 교체")
rep('history',"캐나다 북부와 그린란드의 이누이트에게 물범 고기와 내장은 중요한 전통 식품이며, 캐나다 원주민은 수천 년 동안 물범의 근육·지방층·심장·간 등을 날것이나 덜 익힌 상태로도 먹어 왔다[8].",
    "캐나다 북부와 그린란드의 이누이트에게 물범 고기와 내장은 중요한 전통 식품이며, 캐나다 원주민은 수천 년 동안 물범의 근육·지방층·심장·간 등을 날것이나 덜 익힌 상태로도 먹어 왔다[8]. 이 서술은 하프물범만이 아니라 고리무늬물범 등 여러 물범을 묶은 일반 서술이다[8].",
    "[8] 원문은 종 구분 없는 'seal meat and organ tissues' 서술(캐나다 사냥 대상 7종) — 하프물범 고유 근거처럼 읽히지 않게 명시")
rep('history',"물범 고기가 오랫동안 기름 추출과 모피·가죽 생산의 부산물로 여겨져 비료·사료로 많이 쓰였고",
    "물범 고기가 여전히 주로 물범유 추출과 모피·가죽 생산의 부산물로 여겨져 상당량이 비료·사료로 쓰이며",
    "[9] 원문: 'is still predominantly considered a byproduct or waste ... bulk ... ending up as fertilizer, animal feed' — '오랫동안'(과거)이 아니라 현재 서술")
rep('cultivation',"하프물범은 육지에 붙은 '정착빙' 위에서 새끼를 낳으며, 번식지는 백해, 그린란드해, 래브라도 앞바다(Front), 세인트로렌스만 남부 네 곳이다[6].",
    "하프물범의 번식지는 백해, 그린란드해, 래브라도 앞바다(Front), 세인트로렌스만 남부 네 곳이다[6]. 번식 얼음을 [6]은 육지에 붙은 '정착빙(fast ice)'으로, [7]은 2~3월의 떠다니는 1년생 유빙(pack ice)으로 적어 서술이 다르다[6, 7].",
    "[7] 원문 'whelps on drifting, first-year pack ice during February–March' 와 [6] 'fast ice' 가 상충 — 한쪽만 단정하지 않게 두 출처 병기")
rep('related_species',"같은 바다에 잔점박이물범(Phoca vitulina)·회색물범(Halichoerus grypus)·두건물범(Cystophora cristata)·고리무늬물범(Phoca hispida)이 함께 산다[6, 26, 27].",
    "캐나다 동부 바다와 북극에는 잔점박이물범(Phoca vitulina)·회색물범(Halichoerus grypus)·두건물범(Cystophora cristata)·고리무늬물범(Phoca hispida)도 산다[26, 27].",
    "[6]은 근연종 분포를 다루지 않음; [26]의 고리무늬물범 시료는 세인트로렌스가 아니라 캐나다 동부 북극 해역 — '같은 바다'를 고침")
rep('related_species',"세인트로렌스만에서 태어난 새끼 가운데 PBDE는 하프물범이 가장 낮았다[27].",
    "세인트로렌스만에서 태어난 잔점박이물범·회색물범·하프물범 새끼 가운데 PBDE는 하프물범이 가장 낮았다[27]. 이 비교값들은 모두 지방층·혈청 같은 조직 시료이며 정제유 값이 아니다[26, 27].",
    "비교 대상 종 명시, 조직 값(정제유 아님) 명시")
rep('processing',"국내 연구에 쓰인 캐나다산 하프물범유 제품은 공급처 자료 기준으로 총 오메가-3 23%",
    "국내 연구에 쓰인 캐나다 뉴펀들랜드 업체의 하프물범유 제품은 논문에 적힌 제품 조성 기준으로 총 오메가-3 23%",
    "[10] 원문은 제3의 기관이 제공한 배합(formula) 값을 적었을 뿐 공급처 분석값이라고 하지 않음; 연구진이 직접 분석한 값도 아님")
rep('processing',"이 종의 기름이라고 밝힌 사람 시험은 확인하지 못함.",
    "이 종의 기름이라고 밝힌 사람 시험은 확인하지 못함. 'seal oil'을 쓴 사람 시험(염증성 장질환 관절통, 1형 당뇨 신경병증)은 원문(전문·초록)에 물범 종이 밝혀져 있지 않아 하프물범유 효능 근거로 쓰지 않았다[33, 34]. 고시의 기능성은 'EPA 및 DHA 함유 유지' 원료 전체에 대한 것이다[3].",
    "종 미기재 seal oil 사람 시험[33·34]을 본문에서도 근거 아님으로 명시(V2 지시); 고시 기능성이 하프물범유 단독 사람 근거가 아님을 명시")
for c in d['compounds']:
    if '공급처 제시값' in c.get('content_text',''):
        old=c['content_text']; c['content_text']=old.replace('공급처 제시값','논문에 적힌 제품 조성값'); ch.append({"where":f"compounds.{c['name']}.content_text","before":old,"after":c['content_text'],"why":"[10] 원문은 제공된 배합 값(as per the formula provided by) — 공급처 분석값으로 단정하지 않음"})
a=d['assays'][0]; c=a['conditions']
old=json.dumps(c,ensure_ascii=False)
c['instrument']="가스크로마토그래프(제1~3법 공통)"
c['detection']="불꽃이온화검출기(FID)"
c['sample_prep']="제1·2법: 0.5 N 메탄올성 수산화나트륨·14% 트리플루오르보란메탄올로 메틸에스테르화; 제3법: EPA·DHA 에틸에스테르를 메틸에스테르화 없이 직접 분석"
c['standard']="내부표준물질 면적과 비교해 정량(제3법 표준물질: EPA·DHA 에틸에스테르)"
ch.append({"where":"assays[0].conditions","before":old,"after":json.dumps(c,ensure_ascii=False),"why":"고시 제4. 3-32-1~3 원문(hf_methods.json)에 있는 기기·검출기·전처리·정량 방식을 채움(칼럼·온도는 법마다 달라 비움)"})
m=d['markers'][0]
oldn=m['note']
m['note']=oldn.replace("card.json 의 lists 에는 KR_NOTICE 가 없으나 고시 원재료 칸에 이 종의 현 학명(Pagophilus groenlandicus)이 적혀 있어 넣었다[2, 3].",
 "card.json 의 lists 에는 KR_NOTICE 가 없다(card lists 누락 — 학명 차이: 식품원료 목록 A코드는 Phoca groenlandica, 고시·C코드 '바닷물범(고시형)'은 Pagophilus groenlandicus). 고시 원재료 칸 원문 '바닷물범(Pagophilus groenlandicus)'과 C코드 행으로 대조해 넣었다[2, 3].")
assert m['note']!=oldn
ch.append({"where":"markers[0].note","before":oldn,"after":m['note'],"why":"KR_NOTICE 근거 대조 결과를 'card lists 누락(학명 차이)'로 기록"})
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(ch,open(p.replace('dossier.json','_review/changes.json'),'w'),ensure_ascii=False,indent=1)
print(len(ch))
