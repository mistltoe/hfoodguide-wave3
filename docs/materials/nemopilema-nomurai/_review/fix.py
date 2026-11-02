import json,re
p='dossier.json'; d=json.load(open(p))
S={s['key']:s for s in d['sections']}
def rep(k,a,b):
    assert a in S[k]['body'],(k,a); S[k]['body']=S[k]['body'].replace(a,b)
rep('biology','메두사는 주로 1000 μm 미만의 작은 요각류와 부유 유기물을 먹는다[13][14]. ',
 '2019년 5월 개체의 위 내용물에서는 1000 μm 미만 요각류가 먹이 개체 수의 99% 이상이었다[13]. ')
rep('biology','랴오둥만 조사에서는 몸이 커질수록 먹이 중 동물성 먹이의 비율이 줄었다[14].',
 '랴오둥만 조사에서는 몸이 커질수록 먹이 중 동물성 먹이의 비율이 줄어, 200 μm 이상 동물플랑크톤 비율이 5월 74%에서 7월 32% 미만으로 낮아지고 부유 유기물 비율은 68%까지 늘었다[14].')
rep('cultivation','노무라입깃해파리는 양식 대상이 아니며, 국내 어획·생산 통계는 확인하지 못했다[1].',
 '노무라입깃해파리는 실험실에서 쉽게 기를 수 없는 종으로 보고되었고[8], 양식이나 국내 어획·생산 통계는 확인하지 못했다.')
rep('related_species',"두 학명을 함께 적어, 두 종이 혼동되어 온 사례를 보여 준다[34].",
 "두 학명을 함께 적어, 이 종을 Stomolophus meleagris 로 부른 문헌도 있다[34].")
src={s['n']:s for s in d['sources']}
src[22]['title']=src[22]['title'].replace('2022;14(12) (초록)','2022;14(12):831 (초록)')
src[25]['title']=src[25]['title'].replace('Food Chem 2026:149684','Food Chem 2026;519:149684')
src[29]['title']=src[29]['title'].replace('2024;22(5) (초록)','2024;22(5):217 (초록)')
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
