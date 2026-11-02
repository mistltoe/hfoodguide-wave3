import json
p='/home/user/hfoodguide-wave3/docs/materials/solanum-muricatum/dossier.json'
d=json.load(open(p))
def rep(s,a,b):
    assert a in s,(a[:40])
    return s.replace(a,b)
d['aliases']=[a for a in d['aliases'] if a!='페피노멜론']
S={s['key']:s for s in d['sections']}
S['history']['body']=rep(S['history']['body'],"칭하이대학 연구진이 'Qingcanxiang' 등 품종을 육성했다[8, 29]","칭하이 농림과학원이 'Qingcanxiang' 등 품종을 육성했다[8, 29]")
S['biology']['body']=rep(S['biology']['body'],"헥실 아세테이트 등은 박과실파리 암컷을","헥실 아세테이트 등은 과실파리의 일종인 Zeugodacus tau의 산란기 암컷을")
S['cultivation']['body']=rep(S['cultivation']['body'],"열매 비타민 C가 늘었지만 가용성 고형물은 줄었다[8]","자가접목 대조보다 열매 비타민 C가 늘었지만 가용성 고형물은 줄었다[8]")
S['safety']['body']=rep(S['safety']['body'],"페피노 열매의 솔라닌 등 글리코알칼로이드 함량을 정량한 논문이나 공공기관 자료는 PubMed 검색으로 확인하지 못함.",
 "페피노를 포함한 가지속 7종의 어린 식물(파종 후 약 6주) 잎·줄기·뿌리 글리코알칼로이드를 HPLC-TOF-MS로 분석한 연구가 있으나, 열매는 분석 대상이 아니었다[30]. 페피노 열매의 솔라닌 등 글리코알칼로이드 함량을 정량한 논문이나 공공기관 자료는 PubMed 검색으로 확인하지 못함.")
C={c['name']:c for c in d['compounds']}
c=C['Chlorogenic acid']
c['content_text']="현대 품종 El Camino·Puzol·Valencia의 주성분(각 계통의 주된 화합물이 하이드록시신남산 총량의 59–82%); 하이드록시신남산 총량 1.11–2.35 mg/g(껍질 벗긴 과육 동결건조 분말 분석)[2]"
c['activity_ko']="유도형 산화질소 합성효소 억제로 알려짐; 과육 추출물 원액은 LPS 자극 대식세포의 NO 생성을 36–67% 억제(세포 시험)[2]"
c=C['Feruloyl glucose']; c['name']='Feruloyl hexoside'
c=C['Ascorbic acid']; c['content_text']=rep(c['content_text'],"칭하이 시험 자근 'Qingcanxiang' 2.13 µg/g, 가지 대목 접목 6.31 µg/g","칭하이 시험 'Qingcanxiang' 자가접목 2.13 µg/g, 가지 대목 접목 6.31 µg/g")
c=C['Sucrose']; c['content_text']="자가접목 72.86 mg/g, 가지 대목 접목 114.23 mg/g(HPLC, 원문 단위 그대로, 차이는 유의하지 않음 p = 0.090)[8]; 익을수록 늘어 주된 당이 됨[4]"
c=C['Fructose']; c['content_text']=rep(c['content_text'],"자근 270.83","자가접목 270.83")
c=C['Hexyl acetate']; c['activity_ko']="과실파리의 일종인 Zeugodacus tau 산란기 암컷 유인[27]"
a=d['assays'][0]
a['rationale']="페피노 과육의 페놀은 모두 하이드록시신남산 유도체였고 클로로겐산 이성질체가 주성분이어서 과육 페놀 조성 비교의 지표로 쓸 수 있음(다만 함량 순위와 항산화·NO 억제 순위는 일치하지 않음); 전문 확인, 기기 모델·칼럼 온도·검출한계·회수율 값은 원문에 없음[2]."
a=d['assays'][1]
a['part']="열매"
a['content']="'Qingcanxiang' 자가접목 자당 72.86·과당 270.83·포도당 153.90 mg/g, 가지 대목 접목 자당 114.23·과당 253.63·포도당 122.62 mg/g(원문 단위 그대로)[8]"
d['sources'].append({"n":30,"title":"High-Performance Liquid Chromatography-Mass Spectrometry Analysis of Glycoalkaloids from Underexploited Solanum Species and Their Acetylcholinesterase Inhibition Activity — Plants (Basel) 2022;11(3):269 (PMID 35161249, PMC8839269, 전문 확인; 잎·줄기·뿌리만 분석)","url":"https://doi.org/10.3390/plants11030269","publisher":"PubMed","accessed":"2026-11-02"})
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
