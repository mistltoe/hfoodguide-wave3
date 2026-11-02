import json,sys
p='dossier.json'; d=json.load(open(p))
S={s['key']:s for s in d['sections']}
def rep(key,old,new):
    b=S[key]['body']; assert old in b,(key,old); S[key]['body']=b.replace(old,new)
# overview
rep('overview','영어로는 black poplar mushroom이라 부르고 이탈리아에서는 pioppino로 알려져 있다[2, 7].','영어로는 black poplar mushroom이라 부르며 pioppino라는 이름으로도 불린다[2, 7, 26].')
rep('overview','2014년 독성 연구도 A. aegerita가 A. cylindracea로도 알려져 있다고 적었다[2, 6].','2014년 독성 연구도 A. aegerita가 유럽과 미국에서는 A. cylindracea로도 알려져 있다고 적었다[2, 6].')
# history
rep('history',"이탈리아에서는 '피오피노(pioppino)'라는 이름으로 알려져 있다[7]. 국내 학회지 논문은 상품명 '버들송이'와 함께 '버들볏짚버섯'이라는 이름을 소개하고 일본 이름을 '야나기마쓰타케'로 적었다고 하나, 이 내용은 원문을 열지 못하고 WebSearch 요약으로만 확인했다[27].",
 "'피오피노(pioppino)'라는 이름으로도 불린다[7, 26]. 국내에서는 2008년 한국버섯학회지에 '버들송이' 균주의 배양·재배 특성 논문이 실렸으나, 원문을 열지 못해 그 안의 다른 국문명·일본명은 확인하지 못함[27].")
# biology
rep('biology','짝짓기 방식은 두 개의 짝짓기형 유전자좌로 정해지는 4극성 이형접합성이며, 짝짓기형을 바꾸는 2차 동형접합성 기작도 있을 것으로 분석되었다[3].',
 '짝짓기 방식은 서로 연관되지 않은 두 짝짓기형 유전자좌로 정해지는 4극성 이체성(heterothallism)이며, 짝짓기형을 바꾸는 2차 동체성(secondary homothallism) 기작도 있을 것으로 분석되었다[3].')
# related species
rep('related_species','이들은 버들송이와 다른 원료이므로 이 문서의 성분·안전성 자료와 섞지 않는다[1].',
 "이들은 버들송이와 다른 원료이므로 이 문서의 성분·안전성 자료와 섞지 않으며, 같은 목록에서 보리볏짚버섯(Agrocybe erebia)은 '사용불가'이고 풀버섯(Volvariella volvacea)은 별명이 '볏짚버섯'이어서 이름 혼동에 주의해야 한다[1].")
rep('related_species','아시아 계통은 여러 종을 포함할 수 있는 종 복합체로 잠정 구분되었고 뉴질랜드의 태평양 종과 자매 관계를 이루었으며, 중국에서 기재된 A. chaxingu는 오히려 유럽 계통과 가깝게 묶였다[2].',
 '아시아 계통은 여러 종을 포함할 수 있는 종 복합체로 잠정 구분되어 A. chaxingu로 불린 중국 균주들이 여기에 들었고 뉴질랜드의 태평양 종과 자매 관계를 이루었으며, 중국 윈난에서 기재된 근연종(Cyclocybe salicaceicola) 한 균주는 오히려 유럽 계통과 가깝게 묶였다[2].')
rep('related_species','같은 조건에서 키웠을 때 아시아 계통 균주는 갓이 크고 대가 긴 자실체를, 유럽 계통 균주는 더 작고 많은 자실체를 내는 경향이 있었다[2]. ','')
# cultivation
rep('cultivation','국내 학회지에는 850 mL 병재배에서 버들송이 균주의 병당 수량이 114 g이었다는 보고와, 미송 톱밥 75%·밀기울 25%·수분 70% 배지를 고른 보고가 있으나 원문을 열지 못하고 WebSearch 요약으로만 확인했다[27, 28].',
 '국내에서는 2008년 한국버섯학회지에 버들송이 균주(ASI1 9003)의 배양·재배 특성 보고가 있으나, 원문을 열지 못해 병재배 수량 등 세부 수치는 확인하지 못함[27].')
# processing
rep('processing','이 푸코글루코갈락탄은 대장암 세포(HCT-116)에서 24시간 IC50 490 μg/mL로 증식을 억제했고, 다당은 고지방식 생쥐의 체중 증가를 줄였다는 동물·세포 실험이 있다[11, 12].',
 '별도 연구의 자실체 푸코글루코갈락탄(ACP)은 대장암 세포(HCT-116)에서 24시간 IC50 490 μg/mL라는 높은 농도에서 증식을 억제했고, 다당(ACP)은 고지방식 생쥐의 체중 증가를 줄였으나, 모두 세포·동물 실험이어서 사람에서의 효과는 확인되지 않았다[11, 12].')
rep('processing','다당체는 노화 모델 동물에서 항산화 효소 활성을 높였고, 셀레늄을 넣어 키운 균사체 다당도 연구되었다[13, 31].',
 '다당체는 노화 모델 동물에서 항산화 효소 활성을 높였고, 셀레늄을 넣어 키운 균사체(식품원료 사용 부위가 아님) 다당도 생쥐에서 연구되었다[13, 31].')
# genetics
rep('genetics','미토콘드리아 유전체는 116,329 bp','중국 광시 연구진이 A. aegerita(tea tree mushroom)로 분석한 미토콘드리아 유전체는 116,329 bp')
rep('genetics','자실체 발달 7단계의 전사체 분석은','유럽 균주의 자실체 형성 과정 7개 시점 전사체 분석은')
# safety
rep('safety','2014년 중국 연구에서 물 추출물은 생쥐에서 반수치사량 8.77 g/kg을 보였고,','2014년 중국 연구에서 물 추출물은 생쥐에서 반수치사량(LD50) 8.77 g/kg을 보였고,')
rep('safety','재배 시료 연구는 버들송이·느타리 섭취로 카드뮴 섭취가 내용섭취량의 최대 27–31%에 이를 수 있다고 계산했다[9, 22].',
 '그리스 재배 시료 연구는 생버섯 300 g(건물 30 g)을 1회 먹는다고 가정할 때 버들송이·느타리의 카드뮴 섭취가 내용섭취량의 최대 27–31%에 이를 수 있으나 건강상 우려 수준은 아니라고 보았다[9, 22].')
rep('safety','메탄올 추출물은 에임스 시험에서 돌연변이를 일으키지 않았다[23].','튀르키예 야생 시료의 메탄올 추출물은 에임스 시험(TA98·TA100)에서 돌연변이를 일으키지 않았다[23].')
# aliases / name
d['aliases']=[a for a in d['aliases'] if a not in ('버들볏짚버섯','Poplar mushroom')]
d['name_en']='Black poplar mushroom'
C={c['name']:c for c in d['compounds']}
c=C['L-Glutamine']; c['content_text']=c['content_text'].replace('[4]','; -80 ℃ 보관 자실체 분말 기준이며 생·건 여부는 원문에 명시되지 않음[4]',1)
c=C["Cytidine 5'-monophosphate"]; c['content_text']=c['content_text'].replace('5′-IMP 불검출)','5′-IMP 불검출, 생·건 기준 미명시)')
c=C['Fucoglucogalactan']; c['activity_ko']='대장암 세포 HCT-116 증식 억제 IC50 490 μg/mL(24시간), 리소좀 매개 세포사멸 유도(세포 실험; 이 ACP가 [10]의 JACP-30 분획과 같은지는 확인하지 못함)[12]'
c=C['beta-1,6-Glucan']; c['activity_ko']='구조 분석 연구로 이 분획 자체의 생리활성은 보고되지 않음[10]; 분획을 특정하지 않은 버들송이 다당(ACP)은 9주 투여로 고지방식 생쥐의 체중·지방 축적·인슐린 저항성을 줄임(동물 실험)[11]'
c=C['Brunnein B']; c['activity_ko']='라디칼 소거 EC50 119.1 ± 1.2 μg/mL, 이전에 보고되지 않은 새 화합물[5]'
c=C['Ageritin']; c['content_text']='자실체 100 g당 2.5 mg 넘게 들어 있음(생·건 기준은 초록에 없음)[7]'
c=C['Agrocybe aegerita lectin']; c['activity_ko']='생쥐 간 독성, 소화효소에 잘 분해되지 않음[6]; 이와 별개로 A. cylindracea에서 분리된 시알산 특이 렉틴은 당사슬 연구 도구로 쓰임[14]'
a=d['assays'][0]; a['content']=a['content'].replace('[4]',' (-80 ℃ 보관 자실체 분말, 생·건 기준 미명시)[4]')
a=d['assays'][1]; a['content']=a['content'].replace('[4]',' (생·건 기준 미명시)[4]')
# sources: drop 28, renumber
src=[s for s in d['sources'] if s['n']!=28]
for s in src:
    if s['n']==27:
        s['title']='볏짚버섯속 ASI1 9003(버들송이)과 ASI1 9016(차신고)의 배양 및 재배적 특성 (한국버섯학회지 6(1):13–19, 2008) — 서지 정보만 확인, 원문 미열람'
mp={s['n']:(s['n'] if s['n']<28 else s['n']-1) for s in src}
for s in src: s['n']=mp[s['n']]
import re
def ren(t): return re.sub(r'\[([0-9, ]+)\]',lambda m:'['+', '.join(str(mp.get(int(x),int(x))) for x in m.group(1).split(','))+']',t)
for s in d['sections']: s['body']=ren(s['body'])
def walk(o):
    if isinstance(o,dict):
        for k,v in o.items():
            if k=='source' and isinstance(v,list): o[k]=[mp[x] for x in v]
            elif isinstance(v,str): o[k]=ren(v)
            else: walk(v)
    elif isinstance(o,list):
        for i,v in enumerate(o):
            if isinstance(v,str): o[i]=ren(v)
            else: walk(v)
for k in ['compounds','assays','markers','production','world','gi','orgs','nutrients']: walk(d[k])
d['sources']=src
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
for s in d['sections']: print(s['key'],len(s['body']))
