import json,sys
p='/home/user/hfoodguide-wave3/docs/materials/tiliacora-triandra/dossier.json'
d=json.load(open(p))
S={s['key']:s for s in d['sections']}
changes=[]
def rep(key,old,new,why):
    b=S[key]['body']; assert b.count(old)==1,(key,old)
    S[key]['body']=b.replace(old,new); changes.append({"where":f"sections.{key}","before":old,"after":new,"why":why})

rep('overview',"한편 이 종의 대표 성분으로 알려진 비스벤질이소퀴놀린 알칼로이드(틸리아코리닌 등)는 주로 뿌리·줄기에서 분리·정량되었고, 잎이나 잎 즙의 알칼로이드 함량을 정량한 자료는 확인하지 못했다[8, 9].",
 "한편 이 종의 대표 성분으로 알려진 비스벤질이소퀴놀린 알칼로이드(틸리아코리닌 등)는 주로 뿌리·줄기와 지상부에서 분리되었고, 잎이나 잎 즙의 알칼로이드 함량을 정량한 자료는 확인하지 못했다[8, 9, 10].",
 "[10] 초록은 새 알칼로이드를 지상부(aerial parts)에서 분리했다고 씀 — 잎이 포함될 수 있는 부위라 함께 밝힘")
rep('overview',"사람 연구는 다른 식물과 섞은 제품의 소규모 시험 정도다[3, 16].","사람 연구는 다른 식물과 섞은 제품의 소규모 시험 정도다[16].",
 "[3] 은 HepG2 세포·쥐 연구로 사람 시험이 없음")
rep('history',"태국과 라오스에서 흔히 먹는 채소로, 태국 논문에서는 '태국 토종 채소'로 소개한다[29, 30].",
 "태국과 라오스에서 흔히 먹는 채소이며[30], 태국 논문에서는 '태국 토종 채소(local Thai vegetable)'로 소개한다[29].",
 "[30] 은 'common vegetable consumed in Thailand and Laos', [29] 는 'local Thai vegetable' — 출처별로 나눔")
rep('history',"이 처방은 태국 국가필수의약품 목록(한약 제제 목록)에 올라 있다[13].","이 처방은 태국 국가필수의약품 목록(생약 제품 목록, Herbal Products list)에 올라 있다[13].",
 "[13] 원문 'Herbal Products list' — '한약'은 부정확")
rep('history',"성분 연구는 1967년 라오스산 방기과 식물 두 종의 알칼로이드를 다룬 프랑스 논문에서 시작되었다[12].",
 "PubMed에서 확인되는 이 종의 가장 이른 성분 논문은 1967년 라오스산 방기과 식물 두 종(Cyclea barbata와 야낭)의 알칼로이드를 다룬 프랑스 논문이다[12].",
 "[12] 는 제목만 있어 '연구의 시작'임을 뒷받침하지 못함 — PubMed 수록 기준으로 약하게 씀")
rep('biology',"화학적으로는 비스벤질이소퀴놀린 알칼로이드가 Tiliacora 속의 주요 성분군이다[17].",
 "화학적으로는 알칼로이드가 Tiliacora 속에서 분리된 성분 가운데 가장 큰 무리다[17].",
 "[17] 초록은 'alkaloids constitute the major class'라고만 하고 비스벤질이소퀴놀린으로 한정하지 않음")
rep('related_species',"이처럼 속 전체가 알칼로이드를 많이 만드는 식물군이다[17].",
 "속 총설도 이 속에서 분리된 성분 가운데 알칼로이드가 가장 큰 무리라고 정리한다[17].",
 "[17] 은 분리 성분의 주요 계열을 말할 뿐 '많이 만든다'는 양적 주장은 없음")
rep('cultivation',"태국에서는 야낭 잎을 펠릿으로 만들어 소·물소 사료에 섞어 반추위 발효와 메탄 발생을 살핀 연구가 여러 건 있다[22]. 하루 150 g까지 펠릿을 먹인 태국 토종 소에서 볏짚 섭취량과 미생물 수가 늘고 메탄 생성이 줄었다[22].",
 "태국에서는 야낭(bamboo grass) 펠릿을 볏짚을 먹는 태국 토종 소에 보충해 반추위 발효와 메탄 발생을 살핀 연구가 있다[22]. 하루 0·50·100·150 g을 비교한 시험에서 150 g 보충 시 볏짚 섭취량과 미생물 수가 늘고 메탄 생성이 줄었다[22].",
 "[22] 는 소 4마리 한 건의 시험 — '물소'·'여러 건'은 출처에 없음")
rep('cultivation',"발효 잎 추출물과 유산균을 함께 미세캡슐화한 사료 첨가물을 육계에 먹인 연구도 있다[31].",
 "잎 추출물과 유산균(Lactiplantibacillus plantarum V202)을 이중층으로 미세캡슐화한 사료 첨가물을 육계에 먹인 연구도 있다[31].",
 "[31] 초록에 '발효' 잎 추출물이라는 말이 없음")
rep('genetics',"잎에서는 내생 곰팡이 Dothideomycete sp.가 분리되어 새 폴리케타이드를 만드는 균주로 연구되었다[27].",
 "야낭에서 분리한 내생 곰팡이 Dothideomycete sp.는 새 폴리케타이드를 만드는 균주로 연구되었다[27].",
 "[27] 초록은 식물에서 분리했다고만 하고 부위(잎)를 밝히지 않음")
rep('safety',"잎 즙의 알칼로이드 근거를 찾아본 결과, 비스벤질이소퀴놀린 알칼로이드 분리·정량 논문은 뿌리·줄기 또는 지상부를 대상으로 했고, 잎 즙이나 잎의 알칼로이드 함량을 정량한 논문은 확인하지 못했다[8, 9, 10].",
 "잎 즙의 알칼로이드 근거를 찾아본 결과, 비스벤질이소퀴놀린 알칼로이드 분리·정량 논문은 뿌리·줄기[8, 9] 또는 지상부[10]를 대상으로 했고(지상부 논문 초록은 잎을 따로 나누지 않음), 잎 즙(남야낭)이나 잎의 알칼로이드 함량을 정량한 논문은 확인하지 못했다. 잎 물 추출물을 LC-QTOF-MS/MS로 정성 분석한 두 연구도 본문에 폴리페놀·아미노산 등을 나열했을 뿐 비스벤질이소퀴놀린 알칼로이드는 보고하지 않았다[4, 5].",
 "[10] 지상부 범위를 밝히고, [4]·[5] 전문의 정성 분석 목록에 비스벤질이소퀴놀린 알칼로이드가 없음을 덧붙임(잎 즙 알칼로이드 근거 점검)")
# assay gradient
a=d['assays'][0]
changes.append({"where":"assays[0].conditions.gradient","before":a['conditions']['gradient'],"after":"","why":"원문은 기울기 표를 참조만 하고 전문 텍스트에 내용이 없음 — 원문에 없는 칸은 비움"})
a['conditions']['gradient']=""
# sources
src={s['n']:s for s in d['sources']}
def srep(n,old,new,why):
    t=src[n]['title']; assert old in t,(n,old)
    src[n]['title']=t.replace(old,new); changes.append({"where":f"sources[{n}].title","before":old,"after":new,"why":why})
srep(20,"Biochim Biophys Acta Gen Subj 2023;1868:130486","Biochim Biophys Acta Gen Subj 2023;1867(12):130486","PubMed 서지: 1867권 12호")
srep(22,"Asian-Australas J Anim Sci 2019.","Asian-Australas J Anim Sci 2019;32(8):1153-1160.","PubMed 서지로 권·쪽 보충")
srep(32,"Biomed Pharmacother 2018.","Biomed Pharmacother 2019;109:2090-2099.","PubMed 서지: 109권 2090-2099쪽(온라인 2018)")
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('/home/user/hfoodguide-wave3/docs/materials/tiliacora-triandra/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
