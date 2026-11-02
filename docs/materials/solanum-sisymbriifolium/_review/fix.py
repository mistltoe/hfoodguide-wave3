import json,re
p='dossier.json'; d=json.load(open(p))
ch=[]
def rep(where,obj,key,old,new,why):
    s=obj[key]; assert old in s,(where,old); obj[key]=s.replace(old,new); ch.append({"where":where,"before":old,"after":new,"why":why})
S={s['key']:s for s in d['sections']}
rep('sections.overview',S['overview'],'body',"목록에는 식물 자체의 국명이 따로 적혀 있지 않아, 이 문서의 '둥근가시'와 원료명에서 부위를 뗀 '둥근가시가지'가 국가표준식물목록의 국명과 같은지는 확인하지 못함.",
 "목록에는 식물 자체의 국명이 따로 없어, 이 문서의 표제 '둥근가시'는 원료명 '둥근가시가지열매'의 앞부분을 딴 작업용 이름이며 '둥근가시'·'둥근가시가지' 어느 쪽이 국가표준식물목록의 국명인지는 확인하지 못함.",
 "로컬 원자료 I1020 에는 RPRSNT_RAWMTRL_NM '둥근가시가지열매'·REGN_CD_NM '열매'만 있고 식물 국명 칸이 없음 — 표제명의 출처(원료명에서 딴 것)를 분명히 함")
d['aliases']=[a for a in d['aliases'] if a!='둥근가시가지']
ch.append({"where":"aliases","before":"둥근가시가지","after":"(삭제)","why":"원료명에서 부위어를 떼어 만든 이름으로 출처 없음 — 별명 목록에서 제외(overview 본문에서만 설명)"})
rep('sections.processing',S['processing'],'body',"익은 열매와 덜 익은 열매의 영양성분을 비교한 논문이 있으나 원문을 열지 못해 수치는 옮기지 않았다[34]. ","","[34] 는 웹 검색 요약으로만 존재를 확인한 약한 출처이고 수치도 없어 문장과 출처 삭제(출처 상한 정리)")
rep('sections.cultivation',S['cultivation'],'body',"감자 시들음병균 Verticillium dahliae의 증식원 역할은 감수성 감자 품종보다 작았다[29].",
 "감자 시들음병균 Verticillium dahliae의 균량(CFU)은 첫해 온실 시험에서 감자 3품종보다, 이듬해에는 한 품종보다 적어 증식원 역할이 감수성 감자보다 작을 것으로 보았다[29].",
 "[29] 초록: 1년차 3품종, 2년차 Russet Norkotah 한 품종만 유의하게 더 많음 — 일반화 완화")
C={c['name']:c for c in d['compounds']}
rep('compounds.Chlorogenic acid.content_text',C['Chlorogenic acid'],'content_text',"조직배양 식물의 페놀산 7종 합산 범위 3.30–121.75 µg/g 건물(부위 초록에 없음)[7]",
 "조직배양 식물에서 잰 페놀산 7종의 성분별 함량 범위 3.30–121.75 µg/g 건물(클로로겐산 개별 값·부위는 초록에 없음)[7]",
 "[7] 초록의 3.30–121.75 µg/g DW 는 7종 각각의 범위이지 합산값이 아님")
rep('compounds.Hydroxysolamargine.activity_ko',C['Hydroxysolamargine'],'activity_ko',"글리코알칼로이드 추출물의 아세틸콜린에스터레이스 억제가 보고되었으나 개별 성분 기여는 밝혀지지 않았다[14]",
 "가지속 7종 잎·줄기·뿌리 글리코알칼로이드 추출물을 함께 비교한 시험관 시험에서 아세틸콜린에스터레이스 억제가 보고되었으나 이 종·이 성분의 개별 기여는 밝혀지지 않았다[14]",
 "[14] 는 루로 등 7종 비교 연구 — 다른 가지속 결과와 섞이지 않게 범위 명시")
src=d['sources']
for s in src:
    if s['n']==21: 
        old=s['title']; s['title']=old.replace("Taxon 60(5)","Taxon 2011;60(5)"); ch.append({"where":"sources[21].title","before":"Taxon 60(5)","after":"Taxon 2011;60(5)","why":"권호 연도 누락 보완(PubMed 서지)"})
    if s['n']==14:
        s['title']=s['title'].replace("전문 확인 — 받은 본문에서","전문 확인, 가지속 7종 비교 — 받은 본문에서")
# drop 34, renumber 35->34
d['sources']=[s for s in src if s['n']!=34]
for s in d['sources']:
    if s['n']==35: s['n']=34
for sec in d['sections']:
    sec['body']=re.sub(r'\[35\]','[34]',sec['body'])
for arr in ('compounds','assays'):
    for x in d.get(arr) or []:
        x['source']=[34 if n==35 else n for n in x['source']]
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(ch,open('_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(ch))
