import json
P='/home/user/hfoodguide-wave3/docs/materials/galinsoga-parviflora/dossier.json'
d=json.load(open(P))
S={s['key']:s for s in d['sections']}
changes=[]
def rep(key,old,new,why):
    b=S[key]['body']; assert old in b,(key,old)
    S[key]['body']=b.replace(old,new); changes.append({"where":f"sections.{key}","before":old,"after":new,"why":why})

rep('overview','원산지는 남·북아메리카이며 아시아·아프리카·오스트레일리아 등으로 퍼져 세계 여러 곳에 귀화했다[2, 11].',
    '종설은 원산지를 남·북아메리카로 적고 아시아·아프리카·오스트레일리아에 도입되었다고 정리했으며[2], 모기 유충 연구는 남아메리카 원산으로 세계 곳곳에 귀화했다고 적었다[11].',
    '[2]는 남·북아메리카, [11]은 남아메리카 원산이라 적어 출처별로 나눔')
rep('related_species','두 종의 지상부 추출물을 함께 비교한 연구가 여럿 있다[12, 13, 14]. 활성 분획에서 파툴리트린·쿼시메리트린 등 플라보노이드와 카페오일 유도체가 검출되었다[12].',
    '두 종의 지상부 추출물을 함께 비교한 연구가 여럿 있다[12, 13, 14]. 두 종의 가장 활성이 큰 분획에서 파툴리트린·쿼시메리트린·퀘르세타게트린 등 플라보노이드와 카페오일 유도체가 검출되었으나, 초록은 어느 성분이 어느 종의 분획에서 나왔는지 나누어 적지 않았다[12]. 별꽃아재비 단독 시료에서는 이 플라보노이드 배당체들이 따로 분리·동정되었다[3].',
    '[12]는 두 종을 함께 다뤄 성분의 종 귀속이 초록에 없음 — 별꽃아재비 단독 근거 [3] 보강')
rep('related_species','같은 속의 G. ciliata는 한 연구에서 \'비침입성 도입종\'으로 다뤄져 침입종인 G. parviflora와 비교되었다[19].',
    '한 유럽 연구에서는 G. ciliata라는 이름의 같은 속 식물이 \'비침입성 도입종\'으로 다뤄져 침입종인 G. parviflora와 비교되었다[19]. G. ciliata라는 이름은 G. quadriradiata와 같은 종을 가리키는 이명으로 쓰이는 경우가 있으나, 이 대응은 이번 조사에서 공식 분류 목록으로 확인하지 못함.',
    'G. ciliata 를 별개 종처럼 단정한 표현을 완화하고 털별꽃아재비와의 이명 혼동 가능성을 표시')
rep('cultivation','브라질 옥수수·콩 돌려짓기 시험에서는 무경운 재배 때 주요 활엽 잡초의 하나였다[25].',
    '브라질에서 옥수수와 강낭콩류(bean)를 잇달아 심은 4작기 시험에서는 무경운 재배 때 주요 쌍떡잎 잡초의 하나였다[25].',
    '[25] 원문은 maize and bean, dicotyledonous weed — 콩(soybean)으로 읽히지 않게 고침')
rep('processing','같은 지상부라도 추출 용매에 따라 성질이 달라, 물 추출물은 사람 피부 섬유아세포를 자외선 손상에서 보호한 반면 에탄올 추출물은 세포독성을 보였다[13].',
    '같은 지상부라도 추출 용매에 따라 성질이 달라, 물 추출물은 사람 피부 섬유아세포를 자외선 손상에서 보호한 반면 에탄올 추출물은 세포독성을 보였다[13]. 다만 이 결과는 별꽃아재비와 G. quadriradiata를 함께 시험한 것으로, 초록은 두 종에 공통된 경향으로 적었다[13].',
    '[13]은 두 종 공동 시험 — 종 귀속 범위 명시')
rep('processing','질소 라디칼 소거 시험에서도 물 추출물이 에탄올 추출물보다 활성이 높았다[14].',
    '질소 라디칼 소거 시험에서도 두 종 모두 물 추출물이 에탄올 추출물보다 활성이 높았다[14].',
    '[14] 원문 "aqueous extracts of both Galinsoga species"')
rep('genetics','중국 쓰촨성에서 채집한 별꽃아재비의 엽록체 유전체 전체 서열이 2019년에 보고되었다[22].',
    '중국 쓰촨성에서 채집한 별꽃아재비의 엽록체 유전체 전체 서열이 2019년에 보고되었다[22]. PubMed 제목·초록에는 학명 글자가 빠져 있으나, 같은 기록의 주제어가 Galinsoga parviflora이고 본문이 별꽃아재비 성분 논문들을 인용하며 표본 번호가 GP로 끝나 이 종의 자료로 판단했다[22].',
    '[22] 종 귀속 근거(PubMed 주제어 Galinsoga parviflora, 인용 문헌, 표본 번호 20190211GP03)를 본문에 명시')
rep('genetics','다만 자매군으로 나온 종의 이름은 PubMed 전문에서 학명 글자가 빠져 있어 확인하지 못함.',
    '다만 자매군으로 나온 종과 조립 기준으로 쓴 같은 속 종의 이름은 PubMed 전문에서 학명 글자가 빠져 있어 확인하지 못함.',
    '전문: 기준 유전체가 "its congener"(같은 속 종)로만 남아 있음 — 털별꽃아재비일 수 있으나 확인 불가')
rep('safety','이 성질 때문에 카드뮴 오염 농경지를 정화하는 식물로 연구되고 있다[20, 21, 27, 28].',
    '이 성질 때문에 카드뮴 오염 농경지를 정화하는 식물로 연구되고 있다[20, 21, 27, 28]. 반면 광산 주변 안티모니 오염 토양 화분 시험에서 별꽃아재비의 안티모니 생물농축계수는 0.26(무처리)과 0.17(바이오차 처리)로 1보다 낮았다[29].',
    '이 종 자체의 다른 중금속 축적 자료(PMID 39103103) 추가')
rep('safety','에탄올 추출물은 MCF-7 세포에 0.1–100 µg/mL에서는 약한 독성만 보였으나, 1,000 µg/mL에서는 모든 세포를 죽였다[2, 4].',
    '이집트산 에탄올 추출물은 MCF-7 세포에 0.1–100 µg/mL에서는 약한 독성만 보였으나(세포 생존율 99.23–91.53%), 1,000 µg/mL에서는 모든 세포를 죽였다고 종설은 정리했다[2, 4].',
    '[2] 전문 수치(생존율) 확인·보강, 출처 연구 명시')
rep('safety','지상부 에탄올 추출물은 사람 피부 섬유아세포에 세포독성을 보였다[13].',
    '두 종을 함께 시험한 연구에서 지상부 에탄올 추출물은 사람 피부 섬유아세포에 세포독성을 보였다[13].',
    '[13] 두 종 공동 시험')
# compounds
for c in d['compounds']:
    if c['name']=='Isovanillic acid':
        old=c['activity_ko']; c['activity_ko']='앞선 이 종 연구들에서 보고되지 않았던 페놀산으로 추가 검출[3]'
        changes.append({"where":"compounds.Isovanillic acid.activity_ko","before":old,"after":c['activity_ko'],"why":"[3] 원문은 'additionally detected' — '처음 검출'은 과장"})
    if c['name']=='Patulitrin':
        old=c['content_text']; c['content_text']='분리·동정(함량 미보고)[3]; 두 종(G. parviflora·G. quadriradiata)의 활성 분획에서 검출[12]'
        changes.append({"where":"compounds.Patulitrin.content_text","before":old,"after":c['content_text'],"why":"[12] 두 종 공동 연구"})
    if c['name']=='Caffeic acid':
        old=c['activity_ko']; c['activity_ko']='두 종 추출물의 질소 라디칼 소거 활성에 관여하는 성분으로 거론[14]'
        changes.append({"where":"compounds.Caffeic acid.activity_ko","before":old,"after":c['activity_ko'],"why":"[14] 두 종 공동 연구"})
# sources
src={s['n']:s for s in d['sources']}
upd={9:('Nat Prod Commun 2014 (PMID','Nat Prod Commun 2014;9(8):1171-2 (PMID'),
     19:('Oecologia 2014 (PMID','Oecologia 2014;176(1):95-106 (PMID'),
     24:('Neotrop Entomol 2014 (PMID','Neotrop Entomol 2014;43(6):574-81 (PMID'),
     26:('Bull Environ Contam Toxicol 2017 (PMID','Bull Environ Contam Toxicol 2017;98(4):567-73 (PMID'),
     27:('Int J Phytoremediation 2018 (PMID','Int J Phytoremediation 2018;20(4):295-300 (PMID'),
     22:('Mitochondrial DNA B Resour 2019 (PMC7687395 전문 확인; PubMed 제목·초록에서 학명 글자가 빠져 있어 종명은 본문 인용 문헌·표본 번호로 판단)','Mitochondrial DNA B Resour 2019;4(2):2106-8 (PMC7687395 전문 확인; PubMed 제목·초록에서 학명 글자가 빠져 있으나 PubMed 주제어 Galinsoga parviflora·본문 인용 문헌·표본 번호 20190211GP03으로 종 귀속 판단)')}
for n,(a,b) in upd.items():
    assert a in src[n]['title'],n; src[n]['title']=src[n]['title'].replace(a,b)
    changes.append({"where":f"sources[{n}]","before":a,"after":b,"why":"PubMed 서지(권·호·쪽) 보강"})
d['sources'].append({"n":29,"title":"Remediation on antimony-contaminated soil from mine area using zero-valent-iron doped biochar and their effect on the bioavailability of antimony. Chemosphere 2024;363:143015 (PMID 39103103, 초록 확인)","url":"https://doi.org/10.1016/j.chemosphere.2024.143015","publisher":"Chemosphere (PubMed)","accessed":"2026-11-02"})
json.dump(d,open(P,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open(P.replace('dossier.json','_review/changes.json'),'w'),ensure_ascii=False,indent=1)
print(len(changes))
