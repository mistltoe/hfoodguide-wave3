import json
ch=json.load(open('/home/user/hfoodguide-wave3/docs/materials/carduus-nutans/_review/changes.json'))
r={"slug":"carduus-nutans","reviewer":"V2","date":"2026-11-02",
"checked_sentences":74,"checked_items":45,
"verified":104,"fixed":14,"removed":0,"unverifiable":1,
"changes":ch,
"unverifiable_notes":[
"[3] koreascience 원문은 네트워크 허용 목록 밖이라 열지 않음 — WebSearch 1회 요약으로 2008년 보고·난지도·양수리·내장리·두화 30–60 mm·피침형 총포 조각을 확인했으나 권호·쪽수는 확인 못함",
"[25] LOTUS 레코드(틸리아닌·루테올린 7-갈락토사이드)는 원 문헌을 열지 못해 '확인 못함' 표기 유지",
"[6]·[7]·[8]·[9]·[10]·[11]·[12]·[13]·[15]–[24]·[26]·[27]은 PubMed 초록으로, [4]·[5]·[14]는 PMC 전문으로 대조",
"식품원료 지위([1]·[2])는 data/raw/mfds_rawmtrl/I1020_20261013.json 원 행과 일치: 사향엉겅퀴줄기 '사용가능부위 : 줄기', 사용가능; 지느러미엉겅퀴(C. crispus) 줄기·잎, Carduus cernuus 줄기 행이 따로 있음",
"근연종 섞임 점검: [26]은 C. crispus 자료로 '섞지 말라'는 용도로만 쓰였고, [9]의 0.44%는 C. acanthoides 값임이 이미 명시됨; [15]·[23]은 다른 종과 합친 결과라 본문에 명시함. 열매([8])·꽃차례([7])·뿌리([9]) 결과는 모두 부위를 밝혀 줄기 결과처럼 쓰이지 않았음"]}
json.dump(r,open('/home/user/hfoodguide-wave3/docs/materials/carduus-nutans/review.json','w'),ensure_ascii=False,indent=2)
