import json,sys
p=sys.argv[1]
d=json.load(open(p))
S={s['key']:s for s in d['sections']}
rep=[
('overview','분류 체계에 따라 진달래과(Ericaceae) 또는 시로미과(Empetraceae)로 다룬다[1, 2, 18]','논문에 따라 시로미과(Empetraceae)로 적거나 진달래과(Ericaceae)에 넣는다[2, 3, 18]'),
('overview','국내 변종 표기 E. nigrum var. japonicum K.Koch','E. nigrum var. japonicum K.Koch'),
('overview','소규모 연구 등이 리뷰로 전해질 뿐이다[2, 13]','소규모 연구 등이 리뷰로 전해질 뿐이다[2]'),
('history','러시아에서는 열매를 간질·마비 증상에 쓰는 민간요법이 있고, 시로미 추출물이 든 동종요법 약이 간질 치료에 쓰였다고 리뷰는 정리한다[2]','민간요법에서는 열매를 간질·마비 증상에 쓰고, 러시아에서는 시로미 추출물이 든 동종요법 약이 간질 치료에 쓰였다고 리뷰는 정리한다[2]'),
('history','북미 원주민 공동체에서는 생과가 전통 식단의 일부였고, 알래스카 앵커리지 부근의 원주민은 잎과 줄기를 설사와 신장 질환에 썼다[2, 5]','북미 원주민 공동체에서는 생과가 전통 식단의 일부였다[2, 5]. 알래스카 앵커리지 부근의 원주민은 잎과 줄기를 설사 치료에 썼고, 이 식물은 신장 질환에도 쓰인다고 기록되어 있다[5]'),
('history','열매 안토시아닌을 처음 정량한 북유럽 연구에서는','열매 안토시아닌을 처음 정량한 연구(아종 hermaphroditum 열매)에서는'),
('biology','hermaphroditum(산시로미, mountain crowberry)','hermaphroditum(영명 mountain crowberry)'),
('biology','구리·니켈 제련소 부근에서도 자라는 드문 종으로, 실험 조건에서','구리·니켈 제련소 부근에서도 자라며, 실험 조건에서'),
('related_species','국내 변종 var. japonicum K.Koch','변종 var. japonicum K.Koch'),
('related_species','Corema album(포르투갈 흰 시로미)','Corema album(영명 Portuguese crowberry)'),
('genetics','동부 캐나다의 분홍 열매 계통이','동부 캐나다의 분홍 열매 계통(E. eamesii)이'),
('genetics','남반구의 붉은 열매 계통은','남반구의 붉은 열매 계통(흔히 별도 종 E. rubrum으로 다룸)은'),
('cultivation','국립산림과학원 연구에서 희귀 수종인 시로미의 조직배양(미세번식)에 WPM 배지가 MS 배지보다 낫다고 보고되었으나, 이는 본문을 열지 못하고 WebSearch 요약으로만 확인한 내용이다[36]','국립산림과학원 연구는 시로미(var. japonicum)를 희귀 수종으로 보고 액아줄기를 유도하는 조직배양(미세번식) 방법을 연구했으나, 본문을 열지 못해 배지 조건 등 세부 결과는 확인하지 못함[36]'),
('safety','이 결과들은 줄기·지상부 시료를 포함한 환경 모니터링 연구이므로','이 결과들은 줄기(재배 실험)나 부위를 나누지 않은 식물체 시료를 쓴 환경·생리 연구이므로'),
]
for k,a,b in rep:
    body=S[k]['body']
    assert body.count(a)==1,(k,a)
    S[k]['body']=body.replace(a,b)
d['aliases']=[x for x in d['aliases'] if x!='Empetrum nigrum subsp. hermaphroditum']
for s in d['sources']:
    if s['n']==12: s['title']=s['title'].replace('Chin Med 2022;17:73','Chin Med 2022;17(1):69')
    if s['n']==17: s['title']=s['title'].replace('Proc Natl Acad Sci USA 2011 (','Proc Natl Acad Sci USA 2011;108(16):6520-5 (')
    if s['n']==36: s['title']=s['title'].replace('WebSearch 요약으로만 확인)','WebSearch 요약으로 희귀 수종·미세번식 연구라는 점만 확인)')
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
