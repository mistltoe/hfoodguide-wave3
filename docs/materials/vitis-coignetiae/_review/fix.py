import json,sys
p='/home/user/hfoodguide-wave3/docs/materials/vitis-coignetiae/dossier.json'
d=json.load(open(p))
changes=[]
def sec(k): return next(s for s in d['sections'] if s['key']==k)
def rep(where,obj,key,old,new,why):
    t=obj[key]
    assert t.count(old)==1,(where,old)
    obj[key]=t.replace(old,new); changes.append({"where":where,"before":old,"after":new,"why":why})
# history
h=sec('history')
rep('sections.history',h,'body','일본에서는 1985년 방목 소 집단 폐사를 조사하면서, 소가 많이 먹었을 것으로 추정된 풀의 하나로 머루를 소에게 먹이는 시험을 했다[26].',
 '일본의 방목 소 집단 폐사 조사(1985년 보고)에서는 소가 많이 먹었을 것으로 추정된 식물의 하나로 머루를 소에게 먹이는 시험을 했다[26].',
 '[26]은 1985년 출판 논문으로 폐사 발생 연도는 초록에 없음; 머루는 풀이 아니라 목본 덩굴')
# cultivation
c=sec('cultivation')
rep('sections.cultivation',c,'body','2016년 리뷰는 머루를 일본에서 근래 소규모 재배가 시작된 자생 과수의 하나로 꼽았고, 이런 자생 과수는 틈새시장용이어서 재배 면적과 생산량이 작고 변동이 크다고 적었다[20].',
 '2016년 리뷰는 머루를 일본에서 근래 소규모 재배가 시작된 자생 과수의 하나로 꼽았다[20]. 일본 내 재배 면적·생산량 수치는 확인하지 못함.',
 '[20] 초록에는 소규모 재배 시작만 있고 틈새시장·면적·변동 서술은 없음(PMC 전문 열리지 않음)')
# biology
b=sec('biology')
rep('sections.biology',b,'body','머루와 유럽 품종을 교잡한 계통(COxGT2)은 잎 뒷면 털 밀도가 최고 등급(9)이었다[19].',
 '머루와 유럽 품종을 교잡한 계통(COxGT2, 순수 머루 아님)은 잎 원판 평가에서 잎 털 밀도가 최고 등급(9)이었다[19].',
 '[19] 전문: 잎 원판으로 OIV 084 평가, 뒷면이라는 명시 없음; 교잡 계통임을 분명히 함')
# genetics
g=sec('genetics')
rep('sections.genetics',g,'body','교배한 F1 496개체로 rhAmpSeq 표지 639개(19개 연관군, 1147.36 cM)의 유전지도를 만들었다[19].',
 '교배한 F1 496개체(품질 관리 뒤 455개체)로 rhAmpSeq 표지 639개(19개 연관군, 1147.36 cM)의 유전지도를 만들었다[19].',
 '[19] 전문: 품질 관리에서 41개체 제외, 455개체×639표지로 지도 작성')
# safety
s=sec('safety')
rep('sections.safety',s,'body','암펠롭신 C와 비티신 A·cis-비티신 A 혼합물은 배양 간세포에서 강한 간독성을 보였다[16].',
 '암펠롭신 C와 비티신 A·cis-비티신 A 혼합물은 강한 간독성 물질로 보고되었다(시험계는 초록에 명시 없음)[16].',
 '[16] 초록은 "powerful hepatotoxins"라고만 쓰고 배양 간세포인지 명시하지 않음')
rep('sections.safety',s,'body','식용 부위가 아닌 줄기의 열수 추출물을',
 '식품원료 사용가능 부위(열매·씨앗)가 아닌 줄기의 열수 추출물을',
 '식품원료 목록[1] 기준으로 표현을 정확히 함')
rep('sections.safety',s,'body','사망이나 뚜렷한 이상은 없었지만,',
 '사염화탄소 간손상 모델 조건에서 사망이나 뚜렷한 이상은 없었지만,',
 '[15] 전문: 독성시험이 아니라 간손상 모델 안에서의 관찰임')
rep('sections.safety',s,'body','머루 안토시아닌의 항암 효과 보고는 대부분 세포 실험이며,',
 '머루 열매 안토시아닌의 항암 효과 보고는 대부분 세포 실험이고 일부가 이종이식 생쥐 실험이며,',
 '[6]도 이종이식 생쥐 실험을 포함함')
# compounds
for cpd in d['compounds']:
    if cpd['name']=='Vitisin A':
        rep('compounds.Vitisin A.activity_ko',cpd,'activity_ko','배양 간세포에서 강한 간독성(암펠롭신 C도 같음)[16]','강한 간독성 물질로 보고(암펠롭신 C도 같음, 시험계는 초록에 명시 없음)[16]','[16] 초록에 시험계 명시 없음')
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('/home/user/hfoodguide-wave3/docs/materials/vitis-coignetiae/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
