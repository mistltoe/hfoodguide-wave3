import json
p='/home/user/hfoodguide-wave3/docs/materials/sinapis-arvensis/dossier.json'
d=json.load(open(p))
changes=[]
def rep_sec(key,old,new,why):
    for s in d['sections']:
        if s['key']==key:
            assert old in s['body'],(key,old)
            s['body']=s['body'].replace(old,new)
            changes.append({"where":f"sections.{key}","before":old,"after":new,"why":why});return
    raise SystemExit(key)
rep_sec('cultivation','들갓은 작물로 재배하기보다 밀·유채 밭에서 방제해야 하는 잡초로 주로 다뤄진다[11, 22].',
 '들갓은 작물로 재배하기보다 밀 등 밭작물에서 방제해야 하는 잡초로 주로 다뤄진다[11, 22].',
 '[11]은 "온대 지역 밭작물(field crops)의 중요한 잡초", [22]는 밀밭 조사만 말함. 유채 밭은 두 출처에 없음')
rep_sec('safety','글루코시놀레이트는 동물에서 사료 섭취 감소와 갑상선 기능 변화 등을 일으킬 수 있고, 시날빈은 분해되어 4-하이드록시벤질 이소티오시아네이트를 거쳐 4-하이드록시벤질알코올과 티오시아네이트 이온이 된다[7].',
 '글루코시놀레이트는 동물에서 사료 섭취 감소와 갑상선 기능 변화 등을 일으킬 수 있다[7]. 백겨자 씨앗 연구에서 시날빈은 미로시나아제로 분해되어 4-하이드록시벤질 이소티오시아네이트가 되고, 이것이 물에서 4-하이드록시벤질알코올로 바뀌며 티오시아네이트가 떨어져 나간다[7]. 들갓에서 이 분해 과정을 따로 확인한 자료는 확인하지 못함.',
 '[7]의 시날빈 분해 경로는 백겨자(Sinapis alba) 씨앗 맥락의 서술이므로 근연종 자료임을 밝혀 섞임 방지')
rep_sec('safety','겨자 씨앗의 2S 알부민(나핀)은 주요 겨자 알레르겐이며, 들갓 씨앗에서도 나핀 계열 단백질이 분리되었다[7, 23].',
 '겨자 씨앗의 2S 알부민(나핀)은 주요 겨자 알레르겐으로, 알레르기성 2S 알부민은 백겨자와 갈색겨자에서 확인되었다[7]. 들갓 씨앗에서도 트립신 억제 활성이 있는 나핀 계열 단백질이 분리되었으나[23], 그 알레르기성은 확인하지 못함.',
 '[7]은 알레르기성 2S 알부민을 백겨자·갈색겨자에서만 기술함. [23]은 들갓 나핀의 구조·트립신 억제만 보고하므로 알레르기성을 들갓에 옮기지 않도록 분리')
for c in d['compounds']:
    if c['name']=='Napin':
        old=c['activity_ko']; c['activity_ko']='트립신 억제 활성[23]; 백겨자·갈색겨자 씨앗의 2S 알부민(나핀)은 주요 겨자 알레르겐이나[7] 들갓 나핀의 알레르기성은 확인하지 못함'
        changes.append({"where":"compounds.Napin.activity_ko","before":old,"after":c['activity_ko'],"why":"[7] 알레르겐 근거는 백겨자·갈색겨자 자료"})
    if c['name']=='4-Hydroxybenzyl isothiocyanate':
        old=c['activity_ko']; c['activity_ko']='미로시나아제가 시날빈을 분해해 생기며 물에서 4-하이드록시벤질알코올로 바뀌고 티오시아네이트가 떨어져 나감(백겨자 씨앗 연구)[7]'
        changes.append({"where":"compounds.4-Hydroxybenzyl isothiocyanate.activity_ko","before":old,"after":c['activity_ko'],"why":"[7] 원문은 백겨자 씨앗 맥락, 분해 순서를 원문대로"})
for s in d['sources']:
    if s['n']==2:
        o=s['title']; s['title']=o.replace('J Chem Ecol 2017;43(6)','J Chem Ecol 2017;43(6):617-629')
        changes.append({"where":"sources[2].title","before":o,"after":s['title'],"why":"PubMed 서지에 쪽수 617-629"})
    if s['n']==6:
        o=s['title']; s['title']=o.replace('Sci Rep 2022;12 (','Sci Rep 2022;12:16705 (')
        changes.append({"where":"sources[6].title","before":o,"after":s['title'],"why":"PubMed 서지 논문번호 16705"})
    if s['n']==24:
        o=s['title']; s['title']=o.replace('63(8):58-63','63(8):42-47')
        changes.append({"where":"sources[24].title","before":o,"after":s['title'],"why":"PubMed 서지 쪽수는 42-47"})
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('/home/user/hfoodguide-wave3/docs/materials/sinapis-arvensis/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
