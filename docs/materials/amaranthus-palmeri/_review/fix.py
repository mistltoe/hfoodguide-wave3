import json,re
p='dossier.json'; d=json.load(open(p,encoding='utf-8'))
S={s['key']:s for s in d['sections']}
def rep(key,old,new):
    b=S[key]['body']; assert old in b,(key,old[:40]); S[key]['body']=b.replace(old,new)
rep('history',"미국 뉴멕시코 주립대 협동지도국 안내서에 아메리카 원주민 여러 부족이 긴이삭비름 잎을 굽거나 삶아 먹고, 씨앗을 갈아 가루로 먹었다는 기술이 있다고 검색 요약에 나오지만 원문을 열지 못해 세부는 확인하지 못함[29]. 이 내용은 WebSearch 요약으로만 본 것이어서 부족 이름이나 조리법은 이 문서에 옮기지 않았다[29].",
 "아메리카 원주민의 잎·씨앗 식용 이용에 관한 기술은 원문 자료를 열어 보지 못해 확인하지 못함. 원산지 미국 남서부의 전통 이용 자료는 1차 출처로 대조하지 못했으므로 이 문서에 옮기지 않았고, 확인하지 못함.")
rep('biology',"국내 비름속 검색표에서는 꽃차례 길이 20–50 cm, 작은포엽이 화피보다 2–3배 긴 점으로 구별한다고 검색 요약에 나오지만 원문은 확인하지 못함[33].",
 "국내 비름속 검색표에서 이 종을 가르는 형질(꽃차례 길이·작은포엽 길이 등)은 원문을 열지 못해 확인하지 못함.")
rep('biology',"질소·인·칼륨 결핍에서는 암그루 줄기(꽃차례 포함)의 무기질 함량이 수그루보다 높았다[9].",
 "양분 결핍 조건, 특히 칼륨·인 결핍에서 암그루 줄기(꽃차례 포함)의 무기질 함량이 수그루보다 높았다(예: 줄기 질소가 칼륨·인 결핍에서 각각 46%·91% 높음)[9].")
rep('genetics',"ALS 저해제 저항성은 Trp574Leu 변이가 주된 원인이었다[25].",
 "미국 아칸소주 20개 지점 개체군에서 ALS 저해제 저항성의 주된 원인은 Trp574Leu 변이였다[25].")
rep('processing',"식품 외 이용으로는 씨앗 수용성 추출물(AAE)을 효모 Cryptococcus vishniaccii의 배양 배지로 쓴 연구가 있다[27].",
 "식품 외 이용으로는 씨앗 수용성 추출물(AAE)을 효모 Cryptococcus vishniaccii의 배양 배지로 쓴 연구가 있다[27]. 다만 이 논문은 재료를 'Amaranthus palmeri L.'로 적어 명명자 표기가 이 종(S.Watson)과 맞지 않으며, 재배 아마란스 씨앗과 구별한 종 동정 근거는 초록에서 확인하지 못함.")
rep('safety',"가축 질산염 중독·옥살산 경고는 WebSearch 요약에서만 보았고 원문을 열지 못해 확인하지 못함.",
 "가축 질산염 중독·옥살산 관련 경고는 이 종을 다룬 1차 자료로 확인하지 못함.")
rep('related_species',"종간 잡종을 통해 eccDNA에 실린 제초제 저항성이 퍼지는 현상도 보고되었다[35].",
 "종간 잡종을 통해 eccDNA에 실린 글리포세이트 저항성이 퍼지는 현상도 보고되었는데, 실험 잡종에서는 꽃가루를 통해 워터헴프로, 자연 잡종을 통해서는 가시비름(A. spinosus)으로 옮겨 간 것이 FISH로 확인되었다(유전 연구이며 가시비름 식품원료 자료와는 무관)[35].")
for c in d['compounds']:
    if c['name']=='Ferulic acid':
        c['content_text']=c['content_text'].replace("저항성 생물형에서 페룰산 유도체가 우선 축적[7]","글리포세이트 처리 시 저항성 생물형에서 페룰산 유도체가 우선 축적[7]")
    if c['name']=='Chlorophyll b':
        c['activity_ko']="광합성 보조 색소; 암수 간 차이는 광도·양분 결핍 조건과 생육 시기에 따라 작게 나타남[9]"
    if c['name']=='Chlorophyll a':
        c['content_text']="비처리 수그루 31.7, 암그루 32.5(P = 0.722; SPAD-502 값을 식으로 환산한 추정치, 추출 정량 아님; 전문 추출본의 단위 표기는 'mg cm'로 보이나 지수 부분 확인 못함)[9]"
for s in d['sources']:
    if s['n']==35:
        s['title']="Extrachromosomal circular DNA-mediated spread of herbicide resistance in interspecific hybrids of pigweed. Plant Physiol 2023;193(1):229-233 (PMID 37186777, PMC10469533, doi:10.1093/plphys/kiad281; 초록 확인)"
    if s['n']==7:
        s['title']=s['title'].replace("J Agric Food Chem 2023","J Agric Food Chem 2023 (전자판 2023-02-13)")
# drop 29,33 and renumber
drop={29,33}
old=[s['n'] for s in d['sources'] if s['n'] not in drop]
mp={o:i+1 for i,o in enumerate(old)}
d['sources']=[s for s in d['sources'] if s['n'] not in drop]
for s in d['sources']: s['n']=mp[s['n']]
REF=re.compile(r"\[(\d+(?:\s*,\s*\d+)*)\]")
def sub(t):
    def f(m):
        ns=[int(x) for x in re.split(r"\s*,\s*",m.group(1))]
        for n in ns: assert n not in drop,(t[:60])
        return "["+", ".join(str(mp[n]) for n in ns)+"]"
    return REF.sub(f,t)
def walk(x):
    if isinstance(x,str): return sub(x)
    if isinstance(x,list): return [walk(i) for i in x]
    if isinstance(x,dict):
        return {k:(walk(v) if k not in('source',) else [mp[n] for n in v]) for k,v in x.items()}
    return x
d['sections']=walk(d['sections']); d['compounds']=walk(d['compounds']); d['assays']=walk(d['assays'])
json.dump(d,open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print(mp)
