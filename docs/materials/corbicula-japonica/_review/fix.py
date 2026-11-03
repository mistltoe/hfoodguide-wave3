import json,sys
p=sys.argv[1]
d=json.load(open(p))
S={s['key']:s for s in d['sections']}
changes=[]
def rep(where,obj,key,old,new,why):
    v=obj[key]
    assert old in v,(where,old)
    obj[key]=v.replace(old,new)
    changes.append({"where":where,"before":old,"after":new,"why":why})
rep("sections.overview",S['overview'],'body',
 "건강기능식품 고시형 원료의 원재료가 아니어서 식약처가 정한 지표성분은 없다[1].",
 "이 종을 원재료로 하는 건강기능식품 고시형 원료는 확인하지 못했고, 따라서 식약처가 정한 지표성분도 확인하지 못함.",
 "[1](식품원료 목록)은 건강기능식품 고시 여부를 말하지 않음")
rep("sections.history",S['history'],'body',
 "일본에서는 예로부터 재첩 추출물이 간을 보호한다고",
 "일본에서는 예로부터 재첩속(Corbicula) 추출물이 간을 보호한다고",
 "[11] 초록은 'Corbicula extract'로 속 수준만 말함 — 재첩(C. fluminea)으로 읽히지 않게")
rep("sections.history",S['history'],'body',
 "2019년에는 아코르빈이 생쥐의 알코올성 간 손상을 줄였다는 동물·세포 실험 결과가 나왔다[11].",
 "2019년에는 합성 아코르빈이 생쥐의 알코올성 간 손상을 줄이고, 재첩 추출물에서 정제한 아코르빈이 생쥐 ES/iPS 세포 유래 간 배양 모델에서 알코올 독성을 막았다는 동물·세포 실험 결과가 나왔으며, 사람에서의 효과는 확인하지 못함[11].",
 "[11] 초록: 생쥐 실험은 합성 아코르빈, 세포 실험은 정제 아코르빈 — 사람 근거 아님을 분명히")
rep("sections.history",S['history'],'body',
 "국내에서는 광양만 하구의 이 종이 식용과 내수면 어업 자원으로 상업적으로 중요하다고 기술되었다[4].",
 "국내에서는 이 종이 식용과 내수면 어업 자원으로 상업적으로 중요하다고 기술되었다(시료는 광양만 하구)[4].",
 "[4] 전문은 '한국에서' 상업적으로 중요하다고 했고 광양만에 한정하지 않음")
rep("sections.safety",S['safety'],'body',
 "이 결과는 주사 실험이며 먹었을 때의 위해를 보여 준 자료는 확인하지 못함.",
 "이 결과는 정맥 주사 실험이며, 먹었을 때의 위해나 조리 후 독성 잔존을 보여 준 자료는 확인하지 못함.",
 "주사 독성이 섭취 위해로 읽히지 않게 범위를 분명히(원문 i.v. LD50)")
C={c['name']:c for c in d['compounds']}
rep("compounds.Selenium.part",C['Selenium'],'part',"조갯살(주로 내장부)","조갯살(건조 중량 기준)",
 "[14] 초록에서 내장부 분포는 MALDI로 확인한 m/z 534 셀레늄 화학종 하나에 대한 것")
rep("compounds.Selenium.activity_ko",C['Selenium'],'activity_ko',
 "약 30%가 물로 추출되었고 분자량 5000 미만의 셀레늄 화합물이 주로 내장부에 있었다[14]",
 "총셀레늄의 약 30%가 물로 추출되었고 물 추출물의 주된 셀레늄 화학종은 분자량 5000 미만으로 추정되었으며, 질량분석으로 찾은 한 셀레늄 화학종은 주로 내장부에 있었다[14]",
 "[14] 초록 문장 구조대로 분리")
for n in ("Glutamic acid","Glycine"):
    rep(f"compounds.{n}.activity_ko",C[n],'activity_ko',
     "맛을 정하는 유리아미노산 가운데 하나로 분석되었다[13]",
     "먹는 부위에서 함량이 높은 유리아미노산이며, 원문은 유리아미노산 조성을 맛의 결정 요인으로 기술했다[13]",
     "[13]은 개별 성분이 맛을 정한다고 하지 않고 유리아미노산 조성 전체를 맛 요인으로 기술")
A=d['assays'][0]
rep("assays[0].method",A,'method',"아미노산 자동분석기(이온교환, 닌히드린 후발색)","아미노산 자동분석기(포스트칼럼 닌히드린법)",
 "[13] 전문 Methods 에 이온교환 칼럼 언급 없음")
rep("assays[0].part",A,'part',"먹는 부위(생시료)","먹는 부위(습중량; 6–7월 시료는 냉동 보관, 신선 시료 표도 별도)",
 "[13] 전문: 6–7월 시료는 냉동 보관, 냉장·신선 시료 표가 따로 있음 — '생시료'로만 쓰면 틀림")
src={s['n']:s for s in d['sources']}
rep("sources[14].title",src[14],'title',"Characterization of Selenium Species in the Shijimi Clam. Chem Pharm Bull 2017",
 "Characterization of Selenium Species in the Shijimi Clam. Chem Pharm Bull 2017;65:1045-50 (초록에 Corbicula japonica로 명시)",
 "제목에 학명 없는 'Shijimi' — 초록에서 C. japonica 확인, 권·쪽 보충")
rep("sources[23].title",src[23],'title',"Using Human Intestinal Enteroids. Viruses 2022;14:1014",
 "Using Human Intestinal Enteroids. Viruses 2022;14:1014 (원문은 'freshwater clams'로 부르나 PubMed 초록 검색에서 Corbicula japonica로 확인)",
 "제목·추출문에 학명이 빠져 있어 종 확인 근거를 밝힘")
rep("sources[11].title",src[11],'title',"suppresses ethanol-induced liver injury. Biochem Biophys Res Commun 2019",
 "suppresses ethanol-induced liver injury. Biochem Biophys Res Commun 2019;522:580-4","권·쪽 보충")
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open(p.replace('dossier.json','_review/changes.json'),'w'),ensure_ascii=False,indent=1)
print(len(changes))
