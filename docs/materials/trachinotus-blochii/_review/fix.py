import json
p='dossier.json'; d=json.load(open(p))
S={s['key']:s for s in d['sections']}
changes=[]
def rep(key,old,new,why):
    s=S[key]; assert old in s['body'],(key,old); s['body']=s['body'].replace(old,new); changes.append({"where":f"sections.{key}","before":old,"after":new,"why":why})
rep('overview',"건강기능식품 고시형 원료의 원재료가 아니어서 식약처가 정한 지표성분은 없다[1].","이 행에는 건강기능식품 기능성 원료와 연결된 지표성분 정보가 없다[1].","[1]은 식품원료 목록 행일 뿐 '고시형 원료가 아니다'를 직접 말하지 않음 — 목록 행 내용으로 좁힘")
rep('overview',"인도와 동남아시아에서 중요한 해상 가두리 양식 어종이다[7]","인도와 동남아시아에서 중요한 해산 양식 어종이다[7]","[7] 초록은 'important mariculture species'라고만 씀(가두리 언급 없음)")
rep('overview',"인도 연구는 시장 크기 약 500 g의 중간 크기 고가 어종으로 설명한다[25].","인도 연구는 약 500 g의 중간 크기 고가 양식 어종으로 설명한다[25].","[25]는 'moderately sized (~500 g)'로만 씀 — '시장 크기'는 원문에 없음")
rep('history',"일찍부터 양식·유통되어, 2006년","양식·유통되며, 2006년","'일찍부터'는 [20,19,22] 어디에도 근거 없음")
rep('history',"2014년에는 중국 연구진이 이 종의 미토콘드리아 전체 유전체를 처음 보고했다[2].","2014년에는 중국 연구진(남중국해수산연구소)이 이 종의 미토콘드리아 전체 유전체를 보고했다[2].","[2] 초록에 '처음'이라는 주장이 없음")
rep('history',"노카르디아(Nocardia seriolae) 감염이 이 종에서 처음 확인되었다[11].","노카르디아(Nocardia seriolae)에 의한 이 종의 집단 발병이 베트남 중부에서 처음 확인되었다[11].","[11]은 'for the first time an outbreak ... in central Vietnam' — 지역 한정 '처음'")
rep('history',"중국 하이난 지역 연구진은 'golden pompano'라는 이름으로 이 학명을 써서 지질·영양 조성과 성 분화 연구를 다수 발표했다[16, 17, 27].","중국 하이난대학 연구진은 'golden pompano'라는 이름으로 이 학명을 써서 지질·영양 조성과 성 분화 연구를 다수 발표했다[16, 17, 27, 26].","[16,17,27,26] 소속이 모두 하이난대학 — [26](메틸테스토스테론 성 분화)도 같은 연구 집단임을 밝힘")
rep('biology',"소독한 수정란에서 자란 자어는 장내 미생물 다양성이 높아지고 생존율이 개선되었다[8].","소독한 수정란에서 자란 자어는 미생물 군집 다양성이 높아지고 생존율이 개선되었다[8].","[8]은 자어 전체의 미생물군(larval microbiota)을 분석 — '장내'로 한정하지 않음")
rep('cultivation',"요오드 20 ppm 10분","요오드포(iodophor) 20 ppm 10분","[8] 원문 'iodophor' — 요오드 원소 농도가 아님")
rep('processing',"중국 연구들은 'golden pompano(T. blochii)'라는 이름으로 가공 특성을 보고했다(T. ovatus일 가능성은 관련 종 절 참고)[30, 31, 32].","중국(하이난대학)과 싱가포르국립대 연구진은 'golden pompano' 또는 'golden pomfret(T. blochii)'라는 이름으로 가공 특성을 보고했다(T. ovatus일 가능성은 관련 종 절 참고)[30, 31, 32].","[30]은 싱가포르국립대(쑤저우 연구원 포함) 연구이고 'golden pomfret' 명칭을 씀")
rep('processing',"머리 인지질은 EPA+DHA 비율이 높아 활용 원료로 제안되었다[18].","하이난대학 연구진의 'golden pompano' 머리 인지질은 EPA+DHA 비율이 18.39%로 높아 활용 원료로 제안되었다[18].","[18]도 하이난 'golden pompano' 시료 — 종 혼동 가능성이 있는 자료임을 드러냄, 수치 보강")
rep('genetics',"메틸테스토스테론 100 mg/kg 사료를 60일 먹인 유전적 암컷의 73%가 간성 생식소를 보였다[26].","하이난대학 연구에서 메틸테스토스테론 100 mg/kg 사료를 부화 후 3일부터 60일 먹인 유전적 암컷의 73%가 간성 생식소를 보였다(번식력 검증은 아직 필요)[26].","[26] 원문 조건(3일령 자어)과 저자 단서(fertility testing 필요) 반영, 하이난 'golden pompano' 연구 집단임을 표시")
rep('safety',"양식용 항생제 옥솔린산은 치료 용량 투여 뒤 24시간 안에 검출한계 아래로 떨어져 31.2시간의 휴약 기간이 제안되었다[15].","양식용 항균제 옥솔린산을 치료 용량으로 7일간 사료에 섞어 준 뒤, 가식부 잔류량은 6시간째에 권장 최대잔류허용기준을 넘었으나 24시간 안에 검출한계 아래로 떨어졌고, 안전 여유 30%를 둔 31.2시간의 휴약 기간이 제안되었다[15].","[15] 원문: 7일 투여 후 6시간에는 MRL 초과 — 빠진 사실을 넣음")
C={c['name']:c for c in d['compounds']}
def crep(name,field,new,why):
    old=C[name][field]; C[name][field]=new; changes.append({"where":f"compounds[{name}].{field}","before":old,"after":new,"why":why})
crep('DDT','activity_ko',"홍콩 시장 해산어 10종 가운데 가장 높았다[20]. 양식장 조사에서는 잡어 사료의 DDT가 배합사료보다 높아 잡어 사료를 쓰지 말 것이 권고되었으나, 사료와 근육 농도의 상관은 유의하지 않았다[21].","[21]은 사료·근육 상관이 유의하지 않다고 씀 — '원인으로 지목'은 과장, [20]은 사료를 언급하지 않음")
crep('Lead','activity_ko',"조사에서 잡어 사료의 납이 배합사료보다 높았고 양식장 퇴적물에 납이 쌓여 있었다; 기준 초과 21개 시료는 3종 합계다[22].","[22] 초록은 어체 납과 사료·퇴적물의 인과를 직접 해석하지 않음 — 사실 나열로 좁히고 21개가 3종 합계임을 밝힘")
crep('Docosahexaenoic acid','activity_ko',"머리 인지질이 고도불포화지방산 공급원으로 활용될 수 있다고 제안되었다(하이난 'golden pompano' 시료)[18].","시료 출처 표시(종 혼동 가능성)")
# nutrients split
n0=d['nutrients'][0]
old=json.dumps(n0,ensure_ascii=False)
d['nutrients'][0]={"form":"양식 근육(등살, 중국 남부 4개 해역 양식장 약 500 g, 'golden pompano' 시료 — T. ovatus일 가능성 배제 못함)","basis":"생것","items":[i for i in n0['items'] if i['name'].startswith(('수분','회분'))],"source":[17]}
d['nutrients'].insert(1,{"form":"양식 근육(등살, 하이난 싼야 양식장 암컷 약 512 g, 'golden pompano' 시료)","basis":"원문 기준(g/100 g; 습·건 기준 명시 없음)","items":[i for i in n0['items'] if '아미노산' in i['name']],"source":[17]})
changes.append({"where":"nutrients[0]","before":old,"after":"수분·회분(4개 해역 약 500 g)과 총·필수아미노산(싼야 암컷 512 g, 기준 미표기)을 두 묶음으로 나눔","why":"[17] 전문: 암수 비교군은 싼야 한 곳 512.36 g 시료이고 아미노산 g/100 g의 습·건 기준이 없음"})
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
