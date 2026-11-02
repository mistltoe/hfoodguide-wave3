import json
p='/home/user/hfoodguide-wave3/docs/materials/ugni-molinae/dossier.json'
d=json.load(open(p))
S={s['key']:s for s in d['sections']}
def rep(key,old,new):
    b=S[key]['body']; assert old in b,(key,old); S[key]['body']=b.replace(old,new)
rep('related_species',
 "무르타에는 주로 세 가지 변종이 있다고 소개되며, 그중 흰 무르타(white murta)는 이름과 달리 안토시아닌 때문에 분홍빛을 띤다[23]. 흰 무르타 열매에서는 107가지 페놀 화합물이 잠정 동정되었고, 그 가운데 다수가 가까운 붉은 무르타에도 있었다[23]. 흰 무르타의 정확한 학명은 받은 본문에서 확인하지 못함.",
 "칠레에서 '무르타'라 불리는 식물은 우니속(Ugni)의 세 종으로, 우니몰리내(U. molinae, 붉은 무르타) 외에 흰 무르타(U. candollei)와 U. selkirkii가 있다[37]. 흰 무르타는 우니몰리내와 다른 근연종이며, 이름과 달리 안토시아닌 때문에 분홍빛을 띤다[23]. 흰 무르타 열매에서는 107가지 페놀 화합물이 잠정 동정되었고, 그 가운데 다수가 가까운 붉은 무르타에도 있었다[23]. 이 결과는 근연종의 자료이므로 우니몰리내 열매의 성분으로 옮겨 쓰지 않는다[23][37].")
rep('related_species',
 "이 종에서 개발한 미세위성(마이크로새틀라이트) 표지는 Luma chequen, Myrceugenia 여러 종, 구아바(Psidium guayaba), 유칼립투스 여러 종에도 교차 시험되었다[19].",
 "이 종의 미세위성(마이크로새틀라이트) 표지를 실은 자료 논문에서는 Luma chequen, Myrceugenia 여러 종, 구아바(Psidium guayaba), 유칼립투스 여러 종 등 도금양과 식물도 교차 시험 대상에 들어 있으나, 초록만으로는 어느 종의 표지를 교차 시험했는지 구분되지 않는다[19].")
rep('processing',"염화콜린:1,2-프로판디올(1:2)이 총페놀(추출물 g당 64.87 mg 갈산 당량)을","염화콜린:1,2-프로판디올(1:2)이 총페놀(64.87 mg 갈산 당량/g)을")
for s in d['sources']:
    if s['n']==23:
        s['title']="Differential Extraction and Preliminary Identification of Polyphenols from Ugni candollei (White Murta) Berries. Antioxidants 2024;13(6):623 (PMID 38929063, doi:10.3390/antiox13060623) — 대상 종은 근연종 Ugni candollei(PubMed 색인으로 확인)"
d['sources'].append({"n":37,"title":"Preservative prospect of Ugni candollei (Barnéoud) O.Berg, an underexploited edible berry tree from Chile. Phytochemistry 2026;250:114955 (PMID 42114730, doi:10.1016/j.phytochem.2026.114955) — 초록","url":"https://pubmed.ncbi.nlm.nih.gov/42114730/","publisher":"Phytochemistry (PubMed)","accessed":"2026-11-02"})
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
