import json
p='/home/user/hfoodguide-wave3/docs/materials/strongylocentrotus-intermedius/dossier.json'
d=json.load(open(p))
S={s['key']:s for s in d['sections']}
changes=[]
def rep(key,old,new,why):
    b=S[key]['body']; assert b.count(old)==1,(key,old)
    S[key]['body']=b.replace(old,new); changes.append({"where":"sections."+key,"before":old,"after":new,"why":why})
rep('overview','껍데기와 가시에는 스피노크롬이라는 나프토퀴논 색소가 들어 있다[6].','껍데기에는 스피노크롬이라는 나프토퀴논 색소가 들어 있다[6].',
    '[6] 표 2는 이 종의 껍데기(shells) 색소만 제시; 가시는 여러 성게 일반에 대한 서술')
rep('history','1989년 중국 다롄해양대학이 중국으로 들여왔다[2, 3]','1989년 중국 다롄해양대학이 중국으로 들여왔다[2, 3, 4]',
    '[2]는 도입 연도만, 다롄해양대학 도입은 [3]·[4] 원문에 있음 — 출처 보강')
rep('biology','다롄에서 다시마를 먹여 기른 실험에서 생식소 무게는','중국 연구진의 1–7월 관찰에서 생식소 무게는',
    '[10] 초록에는 다롄·다시마 급이 조건이 없음(다시마 급이는 [2]의 별도 실험이며 값도 0.70 ± 0.05 → 8.37 ± 0.80 g로 다름)')
rep('biology','배우자 형성 전에 영양분을 쌓았다가','배우자 형성이 시작될 때 영양분을 쌓았다가',
    '[31] 원문: "At the onset of gametogenesis"')
rep('related_species','북대서양·북태평양의 Strongylocentrotus droebachiensis 와','Strongylocentrotus droebachiensis 와',
    '[8] 초록에 S. droebachiensis 분포 서술 없음 — 근연종 정보는 확인한 것만 남김')
rep('related_species','옛 문헌에서 Strongylocentrotus nudus 로 적힌 종은 지금의 Mesocentrotus nudus 에 해당하며, 생식소 카로티노이드 연구는 두 종의 자료를 나란히 보고했다[8, 14].',
    '근연종 nudus 는 문헌에 따라 Strongylocentrotus nudus[12, 14] 또는 Mesocentrotus nudus[8, 15]로 적혀 있으며, 생식소 카로티노이드·지질 연구는 이 종과 그 종의 자료를 나란히 보고했다[12, 14].',
    '[8]·[14] 어느 쪽도 이명 관계를 직접 말하지 않음 — 각 문헌의 표기만 적음')
rep('cultivation','고추가루 1.0% 첨가 사료는 성장을 높이고 생식소 색을 좋게 했으며 생식소 조단백·조지방을 늘렸다[26].',
    '고춧가루 1.0% 첨가 사료는 성장률이 가장 높았고, 1.0%·2.0% 첨가는 생식소 색을 좋게 하고 생식소 조단백·조지방을 늘렸다[26].',
    '[26] 초록: 성장 최고는 1.0%군, 색·조단백·조지방 개선은 "particularly in the 1.0% and 2.0% groups"')
rep('safety','적조 독소 오카다산 5 μg/L 노출은 관족 기능을 떨어뜨렸고','적조 독소 오카다산 5 μg/L 노출은 어린 성게의 관족 기능을 떨어뜨렸고',
    '[18]은 juvenile S. intermedius 실험')
for c in d['compounds']:
    if c['name']=='Phosphatidylcholine':
        old=c['content_text']
        c['content_text']=old.replace('세 종(이 종 포함)','세 종(이 종·S. nudus·G. crenularis) 혼합 범위로')
        changes.append({"where":"compounds.Phosphatidylcholine.content_text","before":old,"after":c['content_text'],"why":"[12] 수치는 세 종 범위 — 근연종 값이 섞였음을 명시"})
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('/home/user/hfoodguide-wave3/docs/materials/strongylocentrotus-intermedius/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
