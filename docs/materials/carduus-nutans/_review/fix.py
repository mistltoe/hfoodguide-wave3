import json
p='/home/user/hfoodguide-wave3/docs/materials/carduus-nutans/dossier.json'
d=json.load(open(p))
S={s['key']:s for s in d['sections']}
changes=[]
def rep(key,old,new,why):
    b=S[key]['body']; assert old in b,(key,old)
    S[key]['body']=b.replace(old,new); changes.append({"where":f"sections.{key}","before":old,"after":new,"why":why})
rep('overview',"Nodding plumeless thistle이라 부른다[1].","Nodding plumeless thistle이라 부른다[1, 14].","[1](I1020 행)에는 과명이 없음 — 국화과·Carduus 소속은 [14] 전문에 있음")
rep('genetics',"Carduus 속에 속한다[1, 10].","Carduus 속에 속한다[10, 14].","[1]에는 과명이 없어 근거를 [10]·[14]로 바꿈")
rep('history',"우리나라에서는 2008년에 미기록 귀화식물로 처음 보고되어 이용 역사가 짧다[3].","우리나라에서는 2008년에 미기록 귀화식물로 처음 보고되었고[3], 국내에서 먹거나 약으로 쓴 기록은 확인하지 못함.","'이용 역사가 짧다'는 [3]이 말하지 않는 추론 — 확인된 사실만 남김")
rep('biology',"총포 조각이 창끝 모양이어서 같은 속 지느러미엉겅퀴와 구별된다[3].","총포 조각이 끝이 뾰족한 피침형이어서 국내에 널리 귀화한 같은 속 지느러미엉겅퀴와 구별된다[3].","[3] 초록 요약: 'acuminate lanceolate involucral bracts' — 피침형으로 정확히 옮김(재검색으로 확인)")
rep('biology',"바람에 날린 씨앗은 대부분 2 m 안팎에 떨어지지만 96 m 떨어진 곳에서 잡힌 씨앗도 있었다[15].","사향엉겅퀴와 C. acanthoides의 바람 산포 야외 조사에서 씨앗의 평균 이동 거리는 약 2 m였지만 96 m 떨어진 곳에서 잡힌 씨앗도 있었다[15].","[15] 초록은 '평균' 이동 거리 약 2 m이며 두 종을 함께 다룸 — '대부분'을 '평균'으로 고치고 두 종 자료임을 밝힘")
rep('biology',"꽃가루의 지질 함량은 기온이 오르면 높아졌다[21].","야외 가온 실험에서 꽃가루의 지질 함량이 높아졌다[21].","[21]은 개방형 가온 상자 실험 결과 — 실험 조건을 밝힘")
rep('related_species',"아종에 따라 성분이 다를 수 있어 문헌의 분류군을 확인해야 한다[10].","지중해 연구에서 Carduus 종들은 성분 프로필로 서로 구별되었으므로[10], 다른 종·아종을 다룬 문헌의 성분 값을 이 원료에 옮겨 쓰지 않는다.","[10]은 종 사이 차이를 보였을 뿐 아종 간 성분 차이는 다루지 않음 — 과장 제거")
rep('cultivation',"국내에서는 2008년 서울 난지도와 경기 지역(양수리 등)에서 귀화식물로 처음 보고되었다[3]. 이 보고는 웹 검색 요약으로만 확인했으며, 이후 분포 변화는 확인하지 못함.","국내에서는 2008년 한국식물분류학회지에 서울 난지도와 경기 양수리·내장리에서 자라는 귀화식물로 처음 보고되었다[3]. 이 보고는 원문을 열지 못해 웹 검색 요약으로만 확인했으며, 이후 분포 변화는 확인하지 못함.","재검색 요약에서 학술지명과 경기 채집지(양수리·내장리)를 확인해 보완")
rep('cultivation',"줄기가 자라는 시기에 맞춘 풀베기는 강도가 높고 시기가 늦을수록 개화를 늦추고 생존과 꽃머리 수를 줄였다[16].","풀베기 실험에서 베는 강도가 높고 시기가 늦을수록 개화가 크게 늦어지고 생존율·꽃머리 수·키가 줄었으며, 자주 베기만으로는 번식이 충분히 줄지 않았다[16].","[16] 초록에 '줄기가 자라는 시기에 맞춘'이라는 조건은 없음 — 원문 결과대로 고침")
rep('cultivation',"아르헨티나 파타고니아에서는 잎꾼개미 둥지의 쓰레기 더미에서 자란 사향엉겅퀴가 50–600% 더 많고 씨앗을 100–300% 더 맺었다[23]. 기온이 오르면 키가 커지고 씨앗이 더 멀리 퍼지는 것으로 예측되었다[24].","아르헨티나 북부 파타고니아의 국립공원에서는 길가 잎꾼개미 둥지의 쓰레기 더미에서 자란 사향엉겅퀴와 Onopordum acanthium이 주변보다 50–600% 더 많았고 씨앗을 100–300% 더 맺었다(두 종을 합한 결과)[23]. 야외 가온 실험에서 사향엉겅퀴는 키가 커져 씨앗이 더 멀리 퍼졌고, 이를 넣은 모형은 확산 속도가 빨라질 것으로 예측했다[24].","[23] 수치는 두 외래종을 함께 보고한 값 — 명시; [24] 키·산포 증가는 실측, 확산 속도만 모형 예측")
rep('genetics',"미국 캔자스의 인공 집단에서","미국 연구진이 만든 인공 집단 네 개에서","[19] 초록에는 조사 장소가 없음(소속 기관만 캔자스) — 장소 표현을 빼고 집단 수를 원문대로")
rep('safety',"튀르키예 광산 지역 조사에서 사향엉겅퀴는 카드뮴을 많이 쌓는 식물 무리로 분류되었다[13]. 오염 지역이나 길가에서 채취한 줄기는 중금속 잔류에 주의해야 한다[13].","튀르키예 은광 지역 토양에서 자란 토착 식물 11종을 조사한 연구에서 사향엉겅퀴는 카드뮴 생물축적 가능성이 있는 식물로 분류되었다[13]. 이 결과는 오염 토양에서 자란 개체에 관한 것이므로, 오염 지역에서 채취한 줄기에는 카드뮴이 쌓여 있을 수 있다[13].","[13]은 '길가'를 다루지 않음 — 원문 범위(광산 오염 토양, potentially bioaccumulator)로 좁힘")
# compounds
for c in d['compounds']:
    if c['name']=='Pinoresinol':
        old=c['content_text']; c['content_text']="열매 7.8 mg/g(이 종 열매에서 처음 보고; 정량 방법 세부는 초록에 없음)[8]"
        changes.append({"where":"compounds[Pinoresinol].content_text","before":old,"after":c['content_text'],"why":"[8] 초록은 7.8 mg/g을 어떤 방법으로 정량했는지 밝히지 않음(HPLC는 동정에 쓰임)"})
# source 3
s3=[s for s in d['sources'] if s['n']==3][0]
old=s3['title']
s3['title']="Two naturalized species, Carduus natans L. and Lepidium latifolium L. newly reported from Korea. 한국식물분류학회지(Korean J Plant Taxonomy) 2008(우리나라 미기록 귀화식물 2종 보고; 원문 페이지는 이 환경에서 열 수 없어 WebSearch 결과 요약으로만 확인 — 학명은 원문에 'natans'로 적혔으나 Carduus nutans L.를 가리킴, 권호·쪽수 확인 못함)"
changes.append({"where":"sources[3].title","before":old,"after":s3['title'],"why":"V2 재검색 요약으로 학술지명 확인; 여전히 원문 미열람임을 유지"})
json.dump(d,open(p,'w'),ensure_ascii=False,indent=2)
json.dump(changes,open('/home/user/hfoodguide-wave3/docs/materials/carduus-nutans/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
