import json,sys
p=sys.argv[1]
d=json.load(open(p))
S={s['key']:s for s in d['sections']}
def rep(sec,a,b):
    t=S[sec]['body']; assert a in t,(sec,a); S[sec]['body']=t.replace(a,b)
rep('history',"일본에서는 1980년대에 자화전호 뿌리의 쿠마린 연구가 이어졌고, 시장에서 '사전호(Si-Qian-Hu)'라는 이름으로 팔리던 약재가 성분상 자화전호로 판정되었다[22, 31].",
 "1980년대에는 일본 연구진이 자화전호(일본명 Shikazenko) 뿌리의 쿠마린을 잇달아 보고했고, 시장에서 'Si-Qian-Hu(Seizenko)'라는 이름으로 팔리던 중국 약재가 잔틸레틴형 쿠마린을 근거로 자화전호로 판정되었다[22, 31].")
rep('processing',"전초 메탄올 추출물은 국내 식물추출물은행에서 공급받아 효소 억제 시험에 쓰였다[16].",
 "전초 메탄올 추출물은 국내 식물추출물은행에서 구입해 안지오텐신 전환효소(ACE) 억제 시험에 쓰였다[16].")
for c in d['compounds']:
    if c['name']=='Decursidin':
        c['activity_ko']="사람 재조합 알도스 환원효소·최종당화산물 생성 억제(시험관 실험; 데쿠르시딘을 포함한 디하이드로잔틸레틴형 쿠마린 7종 전체의 IC50 범위 1.03–21.31·0.41–5.56 μM, 데쿠르시딘 단독 값은 초록에 없음; 사용 부위는 초록에 없음)[25]"
src={s['n']:s for s in d['sources']}
src[6]['title']=src[6]['title'].replace("Physiol Mol Biol Plants 2021 (","Physiol Mol Biol Plants 2021;27(11):2503-2515 (")
src[11]['title']=src[11]['title'].replace("J Chromatogr Sci 2022;60(2) (","J Chromatogr Sci 2022;60(2):173-178 (")
src[17]['title']=src[17]['title'].replace("J Ethnopharmacol 2023 (","J Ethnopharmacol 2023;313:116527 (")
src[18]['title']=src[18]['title'].replace("Plant Physiol Biochem 2023 (","Plant Physiol Biochem 2023;204:108142 (")
src[27]['title']=src[27]['title'].replace("Biochem Biophys Res Commun 2022 (","Biochem Biophys Res Commun 2022;614:85-91 (")
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
