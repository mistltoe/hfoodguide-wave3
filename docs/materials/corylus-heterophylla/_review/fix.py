import json,sys
p=sys.argv[1]
d=json.load(open(p))
S={s['key']:s for s in d['sections']}
reps=[
 ('history','교잡 개암(핑어우, C. heterophylla × C. avellana)','교잡 개암(C. heterophylla × C. avellana)'),
 ('cultivation','베이징의 야생 개암에서는 가지마름·궤양병을 일으키는 곰팡이 51균주가 분리되었다[28].','베이징의 야생 개암에서는 가지 궤양·가지마름과 관련된 곰팡이(Diaporthe·Diplodia 속) 51균주가 분리되었다[28].'),
 ('safety','[이 종 근거] 개암의 Cor h 1 유전자 조각(243 bp, 81개 아미노산)을 발현 벡터에 넣어 만든 재조합 단백질은 IgE와 잘 결합했다고 보고되었다[21]. 개암 유전체에서도 유럽개암 알레르겐 13종(Cor a 1·2·6·8–16과 Cor a TLP)의 상동 유전자가 모두 확인되었다[22].',
  '[이 종 근거] 개암의 Cor h 1 유전자 조각(243 bp, 81개 아미노산)을 발현 벡터에 넣어 만든 재조합 단백질은 IgE와 잘 결합했다고 보고되었다(중국어 논문, 초록으로만 확인; 전체 단백질이 아닌 조각 실험이며 시험에 쓴 혈청 정보는 초록에 없음)[21]. 개암 유전체에서도 유럽개암 알레르겐 13종(Cor a 1·2·6·8–16과 Cor a TLP)의 상동 유전자가 모두 확인되었으나, 이는 유전체 서열 비교로 예측한 결과이며 개암 단백질의 IgE 반응을 직접 확인한 것은 아니다[22].'),
 ('safety','네 종 사이 알레르겐 상동 단백질의 아미노산 일치도는 평균 90% 이상이어서 교차 반응 가능성을 생각해야 한다[22].','이 연구가 비교한 네 종(유럽개암·C. americana·개암·C. mandshurica) 사이 알레르겐 상동 단백질의 아미노산 일치도는 평균 90% 이상이어서, 저자들은 이들을 모두 잠재적 알레르겐으로 보아야 한다고 했다[22].'),
]
for k,a,b in reps:
    assert S[k]['body'].count(a)==1,(k,a)
    S[k]['body']=S[k]['body'].replace(a,b)
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
