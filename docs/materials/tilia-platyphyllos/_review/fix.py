import json,re,sys
p='/home/user/hfoodguide-wave3/docs/materials/tilia-platyphyllos/dossier.json'
d=json.load(open(p))
changes=[]
def rep(where,obj,key,old,new,why):
    s=obj[key]
    assert old in s,(where,old)
    obj[key]=s.replace(old,new); changes.append({"where":where,"before":old,"after":new,"why":why})
S={s['key']:s for s in d['sections']}
rep('sections.overview',S['overview'],'body','유럽 중부·남부가 원산인 넓은잎 낙엽 교목','유럽 중부·남부가 원산인 넓은잎 교목','[5] 초록은 broad-leaved tree 라고만 씀(낙엽 근거 없음)')
rep('sections.overview',S['overview'],'body',"유럽 약용식물 문헌에서 '린덴꽃(Tiliae flos)'은 Tilia cordata·Tilia platyphyllos·두 종의 잡종 또는 그 혼합물의 포엽 달린 꽃차례를 말린 것으로, 감기 증상과 정신적 긴장 완화에 전통적으로 써 왔다[6, 20].","유럽 약용식물 문헌에서 '린덴꽃(Tiliae flos)'은 피나무속 꽃차례를 포엽째 말린 것으로 이 종과 작은잎라임 등 여러 종이나 그 혼합물일 수 있으며, 감기 증상과 정신적 긴장 완화에 전통적으로 써 왔다[6].","[20] EMA 평가서는 WebSearch 요약뿐이라 원문 미확인 — 인용 제거, [6] 초록 범위로 줄임(초록에서 종 학명이 빠져 있어 정의 속 종 목록은 단정하지 않음)")
rep('sections.history',S['history'],'body'," 유럽의약품청(EMA) 약초위원회는 Tilia cordata·Tilia platyphyllos·Tilia × vulgaris의 꽃 또는 그 혼합물을 하나의 전통 약초 성분으로 묶어 단행 평가서(monograph)를 냈고, 감기 증상 완화가 전통적 용도로 들어 있는 것으로 검색 결과에서 확인했다(원문은 확인하지 못함)[20].","","[20] 원문 확인 불가(검색 요약뿐) — 문장 삭제")
rep('sections.biology',S['biology'],'body','아욱과(Malvaceae) 피나무속의 넓은잎 낙엽 교목이다[5, 13]','아욱과(Malvaceae) 피나무속의 넓은잎 교목이다[5, 13]','[5]·[13] 초록에 낙엽 언급 없음')
rep('sections.cultivation',S['cultivation'],'body','번식과 관련해서는 미숙 접합배에서 얻은 배발생 배양으로 이 종의 체세포배와 어린 식물을 재생한 보고가 있다[24].','번식과 관련해서는 작은잎라임(Tilia cordata)의 미숙 접합배 배양으로 체세포배를 얻은 연구에서, 이 종도 배발생 배양으로 체세포배와 어린 식물이 재생되었다고 덧붙여 보고되었다[24].','[24] 의 주 대상은 T. cordata 이고 이 종은 초록 끝에 부가 결과로만 나옴 — 근연종 자료 섞임 방지')
rep('sections.cultivation',S['cultivation'],'body','이 종의 뿌리는 송로버섯(Tuber borchii)과 외생균근을 잘 만들어, 균근 형성 연구의 기주 식물로 쓰였다[23, 25].','이 종의 뿌리는 송로버섯(Tuber borchii)과 외생균근을 만들며(균주에 따라 형성 효율이 달랐다), 균근 형성 연구의 기주 식물로 쓰였다[23, 25].','[23] 초록: 두 균주가 다른 효율로 균근을 만듦 — "잘 만들어" 과장')
rep('sections.processing',S['processing'],'body','열매(소견과) 기름은 식물스테롤과 토코페롤이 많다는 보고가 있으나','작은잎라임과 함께 분석한 연구에서 열매(소견과) 기름은 식물스테롤과 토코페롤이 많다는 보고가 있으나','[9] 의 식물스테롤·토코크로마놀 서술은 두 종 합친 값 — 근연종 섞임 명시')
rep('sections.safety',S['safety'],'body',' 유럽의약품청 단행 평가서에는 알려진 이상반응이 \'없음\'으로 적혀 있다는 내용을 검색 결과 요약으로만 확인했다(원문 미확인)[20].','','[20] 원문 확인 불가 — 근거 없는 안전성 문장 삭제')
rep('sections.safety',S['safety'],'body','HPV16 유전자이식 생쥐에게 이 종 하이드로에탄올 추출물을','HPV16 유전자이식 생쥐(군당 4–7마리)에게 이 종 하이드로에탄올 추출물(부위는 초록에 밝히지 않음)을','[5] 초록: 군당 n=4–7, 사용 부위 미기재 — 소규모 동물 결과임과 부위 불명 명시')
rep('sections.safety',S['safety'],'body','동물에서의 안전성은 양호했다[5]','이 실험 조건의 생쥐에서는 내약성이 양호했다[5]','소규모 동물 결과 일반화 완화')
C={c['name']:c for c in d['compounds']}
rep('compounds.Isoquercitrin.activity_ko',C['Isoquercitrin'],'activity_ko','추출물의 항산화 작용에 기여하는 성분으로 논의됨(시험관)[3]','이 종 꽃에서 정량한 6성분 가운데 가장 많았으나, 단독 활성은 이 연구에서 시험하지 않음[3]','[3] 전문에 이소퀘르시트린을 항산화 기여 성분으로 논의한 대목 없음')
rep('compounds.Chlorogenic acid.content_text',C['Chlorogenic acid'],'content_text','정량·추정 동정된 퀸산 유도체','검출·동정된 퀸산 유도체 가운데 하나','[7] 초록은 7성분 정량·45성분 추정 동정이라고만 하여 클로로젠산의 정량 여부 불명')
for nm in ['Protocatechuic acid','Epicatechin']:
    c=C[nm]; old=c['part']
    c['part']='꽃·포엽·꽃차례[3]; [4, 5]의 하이드로에탄올 추출물은 사용 부위가 초록에 없음' if nm=='Protocatechuic acid' else '꽃차례 제제[2]; [4, 5]의 추출물은 사용 부위가 초록에 없음'
    changes.append({"where":f"compounds.{nm}.part","before":old,"after":c['part'],"why":"[4]·[5] 초록에 부위(지상부·꽃차례) 표시 없음"})
# remove beta-sitosterol (two-species pooled, non-usable part)
b=[c for c in d['compounds'] if c['name']=='beta-Sitosterol'][0]
d['compounds'].remove(b)
changes.append({"where":"compounds.beta-Sitosterol","before":b['content_text'],"after":"(삭제)","why":"[9] 의 식물스테롤 값은 작은잎라임과 합친 범위이고 사용가능부위 밖(열매) — 이 종 값으로 쓸 수 없음"})
# remove source 20 and renumber
used=set()
def refs(s):
    for m in re.finditer(r'\[([\d,\s–-]+)\]',s):
        for x in re.split(r'[,\s]+',m.group(1)):
            if x.isdigit(): used.add(int(x))
blob=json.dumps({k:v for k,v in d.items() if k!='sources'},ensure_ascii=False)
refs(blob)
def walk(o):
    if isinstance(o,dict):
        for k,v in o.items():
            if k=='source' and isinstance(v,list): used.update(v)
            else: walk(v)
    elif isinstance(o,list):
        for v in o: walk(v)
walk({k:v for k,v in d.items() if k!='sources'})
print('unused',[s['n'] for s in d['sources'] if s['n'] not in used])
keep=[s for s in d['sources'] if s['n'] in used]
mp={s['n']:i+1 for i,s in enumerate(keep)}
for s in keep: s['n']=mp[s['n']]
# fix source 24 title note
for s in keep:
    if 'Quercus robur' in s['title']: s['title']=s['title'].replace('— 초록 확인','— 초록 확인(주 대상은 T. cordata, 이 종은 부가 결과)')
    if 'Nutlets' in s['title']: s['title']=s['title'].replace('— 초록 확인','— 초록 확인(열매 기름, 사용가능부위 밖)')
d['sources']=keep
def remap_str(s):
    def f(m):
        parts=re.split(r'(,\s*)',m.group(1))
        return '['+''.join(str(mp[int(x)]) if x.strip().isdigit() else x for x in parts)+']'
    return re.sub(r'\[(\d+(?:,\s*\d+)*)\]',f,s)
def remap(o):
    if isinstance(o,dict):
        for k,v in list(o.items()):
            if k=='sources': continue
            if k=='source' and isinstance(v,list): o[k]=[mp[x] for x in v]
            else: o[k]=remap(v)
        return o
    if isinstance(o,list): return [remap(v) for v in o]
    if isinstance(o,str): return remap_str(o)
    return o
for k in list(d):
    if k!='sources': d[k]=remap(d[k])
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('/home/user/hfoodguide-wave3/docs/materials/tilia-platyphyllos/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes),mp)
