import json
from pathlib import Path
p=Path(__file__).resolve().parent.parent/'dossier.json'
d=json.load(open(p))
changes=[]
def sec(k): return next(s for s in d['sections'] if s['key']==k)
def rep(where,obj,key,old,new,why):
    v=obj[key]
    assert old in v,(where,old)
    obj[key]=v.replace(old,new,1)
    changes.append({"where":where,"before":old,"after":new,"why":why})
s=sec('related_species')
rep('sections.related_species',s,'body',' 이 자료는 같은 속 다른 종과 구별하는 방법만 다루며, 다른 종의 성분·용도 자료는 이 문서에 섞지 않았다[14].','',
    '[14] 는 이 문장(문서 편집 방침)을 말하지 않음 — 출처 없는 문장 삭제')
rep('sections.related_species',s,'body','한국 식물 잎을 열분해','식물 잎을 열분해',
    '[14520500] 초록은 시료 산지를 밝히지 않음(연구기관만 한국)')
s=sec('safety')
rep('sections.safety',s,'body','에탄올 추출물을 생쥐 복강에 주사하면 항원 특이 항체와 비장세포 증식이 용량에 따라 억제되었다[37].',
    '에탄올 추출물을 생쥐 복강에 주사하면 비장세포 증식이 용량에 따라 억제되고 항원 특이 혈청 항체(IgG 등)도 크게 줄었다[37].',
    '[37] 초록: 용량 의존성은 비장세포 증식에 대해서만 기술, 항체는 markedly reduced')
cm={c['name']:c for c in d['compounds']}
for n in ['Taraxerone','Tricin 7-glucoside','Sarmentol H','delta-Amyrone']:
    old=cm[n]['part']; cm[n]['part']='부위 원문 미기재'
    changes.append({"where":f"compounds[{n}].part","before":old,"after":"부위 원문 미기재","why":"출처 초록에 '전초' 등 부위 표기 없음"})
old=cm['Total flavonoids']['part']; cm['Total flavonoids']['part']='건조 약재(부위 원문 미기재)'
changes.append({"where":"compounds[Total flavonoids].part","before":old,"after":"건조 약재(부위 원문 미기재)","why":"[9] 전문은 'dried plant drug'라고만 씀"})
a=d['assays']
newparts={0:'건조 약재(부위 원문 미기재, 20메시 분말)',1:'약재 Sedi Herba(부위 초록 미기재)',2:'약재(부위 초록 미기재; 중국 11개 지역 33개 배치)',3:'약재(부위 초록 미기재)'}
for i,np_ in newparts.items():
    changes.append({"where":f"assays[{i}].part","before":a[i]['part'],"after":np_,"why":"원문(전문/초록)에 '전초' 표기 없음"})
    a[i]['part']=np_
rep('assays[0].rationale',a[0],'rationale','식용 부위(순)가 아니라 건조 약재 전체를 분석한 값이다.','식용 부위(순)가 아니라 건조 약재를 분석한 값이다.','원문에 약재 부위(전체) 표기 없음')
a[1]['conditions']['recovery']=a[1]['conditions']['recovery']  # verified
rep('assays[1].rationale',a[1],'rationale','돌나물 등 돌나물속 약재 3종의','돌나물·S. lineare·S. emarginatum 약재 3종의','[15] 초록의 3종 명시(다른 종 자료와 구분)')
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open(Path(__file__).parent/'changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
