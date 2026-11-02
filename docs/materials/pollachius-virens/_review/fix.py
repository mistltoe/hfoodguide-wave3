import json
p='/home/user/hfoodguide-wave3/docs/materials/pollachius-virens/dossier.json'
d=json.load(open(p))
ch=[]
def rep(sec,old,new,why):
    for s in d['sections']:
        if s['key']==sec:
            assert old in s['body'],(sec,old)
            s['body']=s['body'].replace(old,new); ch.append({"where":"sections."+sec,"before":old,"after":new,"why":why}); return
    raise Exception(sec)
rep('overview','대구과(Gadidae) 북방대구속(Pollachius)의','대구과(Gadidae) Pollachius속의','국문 속명 \'북방대구속\'은 인용 출처 어디에도 없어 학명 속명으로 바꿈')
rep('biology','FishBase 요약에 따르면 최대 전장 130 cm, 흔한 크기 60 cm, 최대 체중 32 kg, 최대 연령 25년이며 수심 37–364 m의 북대서양 양안(동쪽은 바렌츠해·스피츠베르겐에서 비스케이만까지, 아이슬란드 주변 포함)에 산다[2]. 이 값들은 검색 결과 요약으로만 확인한 것이다[2].',
    'FishBase에 따르면 비스케이만에서 바렌츠해에 이르는 북대서양에 산다[2]. FishBase가 정리한 최대 크기·체중·연령·서식 수심 값은 이 환경에서 원문 페이지가 열리지 않아 확인하지 못함.',
    '[2] FishBase 페이지가 이 환경에서 열리지 않고(DNS 차단) 검색 결과에도 수치가 없어 크기·체중·연령·수심 수치를 확인할 수 없음 → 수치 삭제, 분포만 남김')
rep('related_species','검정대구는 대서양대구·태평양대구·명태·청대구·해덕 등과 같은 대구과에 속해','검정대구는 대서양대구·태평양대구·명태·청대구 등과 같은 대구과에 속해','[11]·[12] 어디에도 해덕(haddock)은 나오지 않음')
rep('safety','살 속 유충의 85% 넘게가 뱃살 부위에 몰려 있어','세 어종 모두 살 속 유충의 85% 넘게가 뱃살 부위에 몰려 있어','[7] 전문: 85% 이상 뱃살 집중은 세 어종(대구·검정대구·해덕) 통합 서술 — 범위 명확화')
rep('processing','쥐에게 검정대구 단백질 가수분해물을 26일 먹인 실험에서는 공복 혈장 담즙산이 오르고 내장지방 양이 줄었지만, 사람 대상 근거는 확인하지 못함[22].',
    '쥐에게 검정대구 단백질 가수분해물을 26일 먹인 실험에서는 대두 단백질·카제인을 먹인 쥐보다 공복 혈장 담즙산이 오르고 내장지방 양이 줄었다[22]. 동물실험 결과이며 사람 대상 근거는 확인하지 못함.',
    '[22] 초록: 비교군(대두 단백질·카제인) 명시, 동물 결과임을 분명히 함')
# aliases
old=list(d['aliases']); d['aliases']=[a for a in d['aliases'] if a!='Atlantic pollock']
ch.append({"where":"aliases","before":json.dumps(old,ensure_ascii=False),"after":json.dumps(d['aliases'],ensure_ascii=False),"why":"'Atlantic pollock'은 인용 출처 어디에도 없음(saithe [1], coalfish [21], pollock [10, 29]만 확인)"})
# compounds
for c in d['compounds']:
    if c['name'] in('Taurine','Glycine'):
        b=c['part']; c['part']='단백질 가수분해물(원료 부위는 초록에 없음)'
        ch.append({"where":f"compounds.{c['name']}.part","before":b,"after":c['part'],"why":"[22] 초록은 saithe FPH 원료 부위를 밝히지 않음(PMC 전문 없음)"})
    if c['name']=='Docosahexaenoic acid':
        b=c['content_text']; c['content_text']='간 지방산의 10.5%(2016년 7월)–13.3%(2017년 3월)[21]; 간 포함·제외 내장 원료 기름의 주요 지방산(DHA·팔미트산·올레산·EPA·곤도산) 가운데 하나[20]'
        ch.append({"where":"compounds.DHA.content_text","before":b,"after":c['content_text'],"why":"[20] 전문: '가장 많은 지방산'이 아니라 주요 지방산 목록에 DHA가 처음 나열됨. 간 포함 내장(VL)은 MUFA가 우세"})
    if c['name']=='Oleic acid':
        b=c['activity_ko']; c['activity_ko']='비교 5종 간에서 공통으로 가장 많은 지방산으로 보고[21]'
        ch.append({"where":"compounds.Oleic acid.activity_ko","before":b,"after":c['activity_ko'],"why":"[21] 전문: C18:1 n-9가 5종 간 공통 최다(12.6% 검정대구–15.8% 링); 검정대구 단독 최다라고 하지 않음(DHA 약 13%)"})
for a in d['assays']:
    if a['source']==[33]:
        b=a['conditions']['linearity']; a['conditions']['linearity']=''
        ch.append({"where":"assays[PAH].conditions.linearity","before":b,"after":"","why":"[33] 전문은 검량 범위(3–180 ng/mL)만 밝히고 직선성 값은 본문에 없음(standard 칸에 이미 있음)"})
        b=a['rationale']; a['rationale']='저자들은 검정대구 간에서 물에 잘 녹는 아세나프틸렌·플루오렌·페난트렌 비중이 높은 것을, 얕은 물에 살며 주로 아가미로 흡수하기 때문일 수 있다고 해석했다[33]. 전문(Methods) 확인 — 시료 수가 적어 해석에 주의가 필요하다고 저자들이 밝힘[33].'
        ch.append({"where":"assays[PAH].rationale","before":b,"after":a['rationale'],"why":"[33] 전문: 아가미 흡수는 가능성 해석('may be correlated')이므로 단정 표현을 낮춤"})
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(ch,open('/home/user/hfoodguide-wave3/docs/materials/pollachius-virens/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(ch))
