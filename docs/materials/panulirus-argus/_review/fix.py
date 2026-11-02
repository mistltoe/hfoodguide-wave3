import json
p='/home/user/hfoodguide-wave3/docs/materials/panulirus-argus/dossier.json'
d=json.load(open(p))
changes=[]
def rep(sec,old,new,why):
    for s in d['sections']:
        if s['key']==sec:
            assert old in s['body'],(sec,old)
            s['body']=s['body'].replace(old,new)
            changes.append({"where":f"sections.{sec}","before":old,"after":new,"why":why})
rep('biology',"마지막 유생은 먹이를 먹지 않는 후기유생(퓨에룰루스)으로 변태해 연안으로 헤엄쳐 와 정착하고, 첫 탈피 뒤 어린 개체가 되어서야 다시 먹이를 먹는다[29].",
 "닭새우류의 마지막 유생은 먹이를 먹지 않는 후기유생(퓨에룰루스)으로 변태해 연안으로 헤엄쳐 와 정착하고 첫 탈피 뒤 어린 개체가 되어서야 다시 먹이를 먹으며, 이 종에서는 퓨에룰루스와 첫 어린 개체의 몸 크기·무게·영양 상태를 계절별로 비교한 연구가 있다[29].",
 "[29] 초록의 퓨에룰루스 설명은 닭새우류(spiny lobsters) 일반에 대한 서술이므로 속 일반임을 밝히고 이 종 연구 내용을 덧붙임")
rep('genetics',"이 종에만 감염하는 PaV1 바이러스의 유전체는 70–74 kb 크기의 새 바이러스과(Mininucleoviridae)로 분류가 제안되었다[31].",
 "이 종을 감염하는 유일한 알려진 바이러스인 PaV1은 다른 두 갑각류 바이러스와 함께 전장 유전체가 해독되었고(세 바이러스 유전체 70–74 kb), 새 바이러스과 'Mininucleoviridae'로 분류가 제안되었다[31].",
 "[31] 은 PaV1을 'P. argus를 감염하는 유일한 알려진 바이러스'로 쓰며, 70–74 kb는 PaV1·CmV1·DhV1 세 바이러스를 합친 범위")
rep('safety',"소포자충(Ameson속) 감염 개체는","소포자충(Ameson속으로 보이는 종) 감염 개체는",
 "[14] 은 포자 형태가 Ameson속과 '일치한다(consistent with)'고만 씀")
rep('safety',"근육의 금속결합단백질은 카드뮴에 노출되어도 근육에서는 늘지 않았고 간췌장에서 주로 해독 역할을 하는 것으로 보였다[22].",
 "조직 절편을 카드뮴에 노출한 실험에서 금속결합단백질(MTPA) mRNA는 근육을 뺀 조직에서 늘었고, 연구진은 간췌장의 MTPA가 카드뮴 해독에 중요한 역할을 할 것으로 보았다[22].",
 "[22] 은 조직 절편(explant)의 mRNA 실험이며 '해독 역할'은 추정(likely)으로 씀")
# compounds
for c in d['compounds']:
    if c['source'] and c['source'][0]==19 and c['part'].startswith('근육(복부)'):
        old=c['part']; c['part']=c['part'].replace('근육(복부)','근육')
        changes.append({"where":f"compounds.{c['name']}.part","before":old,"after":c['part'],"why":"[19] 전문은 'muscle'로만 적고 복부 근육이라고 특정하지 않음"})
    if c['name'] in('Glycogen','Glucose','Amino acids','Triglyceride','Lactic acid'):
        old=c['content_text']; c['content_text']=old.replace(' [19]',', 평균±SEM, 급식 24시간 뒤) [19]').replace('), 평균±SEM',', 평균±SEM') if False else old.replace('건물','건물 기준').replace(' [19]',' (평균±SEM, n=6) [19]')
        changes.append({"where":f"compounds.{c['name']}.content_text","before":old,"after":c['content_text'],"why":"[19] 표 3: 건물 기준, 평균±SEM(n=6)"})
    if c['name']=='Glycogen':
        old=c['activity_ko']; c['activity_ko']="근육 글리코겐은 탄수화물 35% 사료군에서 가장 높았고, 탈피 사이 개체의 글리코겐 저장·이용 능력은 낮다고 보고되었다[19, 30]"
        changes.append({"where":"compounds.Glycogen.activity_ko","before":old,"after":c['activity_ko'],"why":"[19] 표 3에서 6% 사료군(0.60)은 생선살 대조군(1.22)보다 낮아 '많을수록 늘었다'는 단조 증가가 아님"})
    if c['name']=='Lactic acid':
        old=c['activity_ko']; c['activity_ko']="근육 젖산은 사료군 사이에 유의한 차이가 없었다[19]; 복부 근육은 무산소 순간 수축에 쓰인다[20]"
        c['role']='nutrient' if False else c['role']
        changes.append({"where":"compounds.Lactic acid.activity_ko","before":old,"after":c['activity_ko'],"why":"'해당 대사산물이 쌓인다'는 [19]·[20] 어디에도 없는 추론"})
for a in d['assays']:
    if '근육(복부)' in a['part']:
        old=a['part']; a['part']=old.replace('근육(복부)','근육')
        changes.append({"where":f"assays.{a['compound']}.part","before":old,"after":a['part'],"why":"[19] 전문은 근육 부위를 특정하지 않음"})
    old=a['content']
    if '평균±SEM' not in old:
        a['content']=old.replace(' [19]',', 평균±SEM, n=6 [19]')
        changes.append({"where":f"assays.{a['compound']}.content","before":old,"after":a['content'],"why":"[19] 표 3: 평균±SEM, 사료군당 6마리"})
s=d['sources'][17]
assert s['n']==18
old=s['title']; s['title']=old.replace('Dis Aquat Organ 2009','Dis Aquat Organ 2009;86(2):159-62')
changes.append({"where":"sources[18].title","before":old,"after":s['title'],"why":"PubMed 19902844 서지에 권·호·쪽 보완"})
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('/home/user/hfoodguide-wave3/docs/materials/panulirus-argus/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
for c in d['compounds']: print(c['name'],'|',c['part'],'|',c['content_text'])
for a in d['assays']: print(a['part'],'|',a['content'])
