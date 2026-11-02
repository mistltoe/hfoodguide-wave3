import json
p='/home/user/hfoodguide-wave3/docs/materials/seriola-lalandi/dossier.json'
d=json.load(open(p))
d['aliases']=[a for a in d['aliases'] if a!='California yellowtail']
R={
'overview':[("사료를 먹인 어린 개체의 근육 지방산에서는","멕시코 바하칼리포르니아에서 사료를 먹여 기른 어린 개체의 근육 지방산에서는"),
            ("양식 부시리가 분석 대상에 들었으나","부시리(yellowtail kingfish)가 분석 대상 22종에 들었으나")],
'biology':[("육식성 회유어로 소개된다[6, 30]","육식성 외양 어류로 소개된다[6, 30]")],
'cultivation':[("피부 흡충 저항성은 유전되는 형질로, 선발 육종으로 세대당 평균 약 10%의 유전적 개량을 얻었다고 정리되었다[20].",
                "피부 흡충 저항성은 유전되는 형질로 정리되었고, 이 종을 포함한 세 양식종의 질병 저항성 선발 육종에서 세대당 평균 약 10%의 유전적 개량을 얻었다고 했다[20]."),
               ("어유의 일부(50%)를 가금유로 바꾸면 성장이 좋아졌으나 카놀라유로 모두 바꾸면 항산화 유전자 발현이 달라졌다[17].",
                "사료에 넣은 어유의 절반(50%)을 가금유로 바꾸면 성장이 좋아졌으나, 카놀라유로 모두 바꾸면 성장이 떨어지고 간의 항산화 유전자(글루타티온 과산화효소 1) 발현이 늘었다[17].")],
'processing':[("양식 육종에서는 필레 무게·수율과 필레 지방 함량이 부시리의 살 품질 형질로 기록된다[16].",
               "양식 육종에서는 필레 무게·수율이 도체 형질로, 필레 지방 함량이 살 품질 형질로 기록된다[16]."),
              ("부시리 부산물로 만든 어육 단백질 가수분해물은","부시리로 만든 어육 단백질 가수분해물은")],
'genetics':[("후각 수용체와 HSP70 유전자군이 확장되어 있었다[6].",
             "후각 수용체와 HSP70 유전자군이 확장되어 있었다[6]. 이 유전체는 중국 다롄의 양식 개체로 해독한 것이어서, 위 종 복합체 구분으로는 북서태평양 집단의 자료에 해당한다[6, 7].")],
'safety':[("같은 시료의 다이옥신은 평균","그중 5개 시료의 다이옥신은 평균"),
          ("부시리 부산물 가수분해물의 높은 히스타민도","부시리 단백질 가수분해물의 높은 히스타민도")],
}
for s in d['sections']:
    for a,b in R.get(s['key'],[]):
        assert s['body'].count(a)==1,(s['key'],a)
        s['body']=s['body'].replace(a,b)
for c in d['compounds']:
    if c['name']=='Histamine': c['part']='단백질 가수분해물(부시리 원료)'
for a in d['assays']:
    if a['compound']=='Mercury': a['part']='양식 개체 혼합 시료(부위는 초록에 없음)'
T={17:("Comp Biochem Physiol B 2012 (초록 확인)","Comp Biochem Physiol B Biochem Mol Biol 2012;162(4):100-6 (초록 확인)"),
   30:("Mol Ecol Resour 2015 (초록 확인)","Mol Ecol Resour 2016;16(1):364-76 (초록 확인)"),
   26:("J Exp Biol 2012 (초록 확인)","J Exp Biol 2012;215(Pt 22):3944-54 (초록 확인)"),
   22:("J Anim Sci Biotechnol 2025 (초록 확인)","J Anim Sci Biotechnol 2025;16(1):16 (초록 확인)"),
   32:("Fish Physiol Biochem 2025 (초록 확인)","Fish Physiol Biochem 2025;51(4):145 (초록 확인)"),
   6:("(초록 확인)","(PMC 전문 확인)"),
   8:("Ecology and Evolution, PMC13491388",None),}
for s in d['sources']:
    if s['n'] in T and T[s['n']][1]:
        a,b=T[s['n']]; assert a in s['title'],s['n']; s['title']=s['title'].replace(a,b)
    if s['n']==8: s['publisher']='Ecology and Evolution, PMC13491388 (PubMed 42626442)'
    if s['n']==9: s['publisher']=s['publisher']+' (PubMed 33574384)'
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
