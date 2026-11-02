import json,sys
p='/home/user/hfoodguide-wave3/docs/materials/dioscorea-batatas/dossier.json'
d=json.load(open(p))
changes=[]
def rep(where,obj_get,obj_set,old,new,why):
    s=obj_get()
    assert old in s,(where,old)
    obj_set(s.replace(old,new)); changes.append({"where":where,"before":old,"after":new,"why":why})
sec={s['key']:s for s in d['sections']}
def S(k):
    return (lambda: sec[k]['body'], lambda v: sec[k].__setitem__('body',v))
rep('sections.safety',*S('safety'),"마는 식품원료 목록에서 제한 없이 '사용가능' 원료이고","마는 식품원료 목록에서 제한적 사용이 아닌 '사용가능' 원료이고","[1] 은 사용 부위를 뿌리·뿌리줄기·주아로 한정하므로 '제한 없이'는 과장")
rep('sections.processing',*S('processing'),"껍질 추출물은 화장품 소재로 시험되었다[37].","껍질 추출물은 피부 세포·효소 실험(시험관)에서 미백·광노화 억제 활성이 보고되어 화장품 소재 가능성이 제안되었다[37].","[37] 은 화장품 제품 시험이 아니라 B16F10·HaCaT·HDF 세포와 효소 실험")
rep('sections.related_species',*S('related_species'),"같은 절에 물마(D. alata)와 흰기니얌(D. rotundata)","같은 절에 워터얌(water yam, D. alata)과 흰기니얌(white guinea yam, D. rotundata)","[2] 의 영명 표기로 맞춤; D. alata 는 별도 식품원료(얌뿌리)라 국문 '물마'로 섞어 부르지 않음")
rep('sections.genetics',*S('genetics'),"이름만 다른 동종 10묶음과 같은 이름의 이종 13묶음이 드러났다[27].","이름만 다르고 같을 가능성이 있는 계통 10묶음과 이름은 같지만 다를 가능성이 있는 계통 13묶음이 예비로 확인되었다[27].","[27] 초록은 'potential heterotypic synonyms/homonyms'를 'preliminarily identified'라고 씀")
a=d['assays'][1]
rep('assays[1].rationale',lambda:a['rationale'],lambda v:a.__setitem__('rationale',v),"중국 허난성 원양현 재배품","중국 허난성 원셴(溫縣) 사질토·황토 재배품, 자오쭤 소재 업체에서 2021년 11월 구입","[9] Methods·Introduction 은 Wenxian county(溫縣)·Bao He Tang(Jiaozuo); '원양현(原陽縣)'은 다른 현")
a0=d['assays'][0]
rep('assays[0].rationale',lambda:a0['rationale'],lambda v:a0.__setitem__('rationale',v),"추출물의 활성 성분으로 알란토인을","시료는 울산의 한약재 업체에서 산 말린 뿌리줄기(산약)이고 원문은 학명을 'D. batatas Decaisne (= … Thunberg)'로 병기해, 약전상 참마(D. japonica) 기원 산약과 구별되지 않을 수 있다[8]. 추출물의 활성 성분으로 알란토인을","[8] 4.2절: 시판 건조 산약 사용, 학명 병기 — 종 섞임 가능성 명시")
for c in d['compounds']:
    if c['name']=='Starch':
        rep('compounds.Starch.content_text',lambda:c['content_text'],lambda v:c.__setitem__('content_text',v),"74.60 ± 1.34(황토) g/100 g 건조중량[9]","74.60 ± 1.34(황토) g/100 g 건조중량(저자 선행연구 값 인용)[9]","[9] 는 'according to our previous study'로 인용한 값")
for s in d['sources']:
    if s['n']==29:
        rep('sources[29].title',lambda:s['title'],lambda v:s.__setitem__('title',v),"Foods 2024;13:1426","Foods 2024;13:1426 (본문 학명 Dioscorea opposita Thunb.)","논문 학명 처리 명시")
    if s['n']==8:
        rep('sources[8].title',lambda:s['title'],lambda v:s.__setitem__('title',v),"Molecules 2018;23:2023","Molecules 2018;23:2023 (시판 건조 산약 사용, 학명 'D. batatas Decaisne (= … Thunberg)' 병기)","논문 학명 처리 명시")
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('/home/user/hfoodguide-wave3/docs/materials/dioscorea-batatas/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
