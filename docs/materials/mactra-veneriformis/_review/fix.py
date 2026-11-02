import json,re,sys
p=sys.argv[1]
d=json.load(open(p))
S={s['key']:s for s in d['sections']}
changes=[]
def rep(key,old,new,why):
    b=S[key]['body']; assert old in b,(key,old)
    S[key]['body']=b.replace(old,new); changes.append({"where":"sections."+key,"before":old,"after":new,"why":why})
rep('overview','개량조개과(Mactridae) 개량조개속에 드는 바다 조개로, 식약처','개량조개과(Mactridae) 개량조개속에 드는 바다 조개로[3], 식약처',
    '[1] 식품원료 목록에는 과(科) 정보가 없음; 과명은 [3] 제목(Bivalvia: Mactridae)으로 뒷받침')
old=S['biology']['body'][S['biology']['body'].index('국내 서해안 개체군의 산란기는'):S['biology']['body'].index('[32].')+5]
rep('biology',old,'국내 개체군의 산란기·성숙 시기를 다룬 학회지 원문은 이번 조사에서 열람하지 못해 확인하지 못함.',
    '[32] 는 WebSearch 요약만 보고 원문을 열지 못한 출처라 구체 수치(6–9월, 24 °C, 7–8월)를 근거로 쓸 수 없음; PubMed 에서도 대체 1차 출처를 찾지 못함')
rep('genetics','참가리비 계통(Patinopecten yessoensis)','참가리비(Patinopecten yessoensis)','원문은 종(P. yessoensis)과 비교했음; "계통"은 원문에 없는 표현')
rep('genetics','전체 길이는 초록에 939.32 Mb, 본문 표에 979,316,154 bp로 서로 다르게 적혀 있다[2].','전체 길이는 초록에 939.32 Mb, 본문과 표에 979.32 Mb(979,316,154 bp)로 서로 다르게 적혀 있다[2].','PMC 전문 본문에도 979.32 Mb로 적혀 있음')
rep('processing','동죽 살에서 얻은 다당류 분말(MVPS)','동죽에서 추출한 다당류 분말(MVPS)','[11] 초록은 추출 부위(살)를 밝히지 않음')
rep('processing','바지락과 동죽에서 감칠맛 펩타이드 16개가 선별되었고 역치는 0.123–1.481 mmol/L였다[29].','바지락과 동죽 두 종을 함께 분석해 감칠맛 펩타이드 16개를 선별했고 역치는 0.123–1.481 mmol/L였다(초록에는 종별 구분이 없음)[29].','[29] 는 두 종 합산 결과; 동죽 단독 값처럼 읽히지 않게 함')
rep('safety','중국 장쑤성 동죽 등 조개 4종 400여 시료에서 오카다산·디노피시스톡신 등 지용성 패류독소는 5–8월에 높았고 검출 농도는 EU 기준보다 훨씬 낮았으며, 아자스피르산·예소톡신·스피롤라이드는 검출되지 않았다[17].',
    '중국 장쑤성 동죽 등 조개 4종을 합친 400여 시료에서 오카다산·디노피시스톡신 등 지용성 패류독소는 5–8월에 가장 높았고 농도는 EU 기준보다 훨씬 낮았으며, 아자스피르산·예소톡신·스피롤라이드는 검출되지 않았다; 동죽만의 값은 원문 그림에서 종명을 대응하지 못해 확인하지 못함[17].',
    '[17] 은 4종 합산 조사이며 종별 값은 그림에만 있음 — 여러 종 합친 값임을 밝힘')
rep('safety','라이저우만 조사에서는 근육 섭취 시 위해 기여가 가장 큰 원소가 비소였다[19].','라이저우만의 이매패 3종(동죽 포함) 조사에서는 근육 섭취 시 위해 기여가 가장 큰 원소가 비소였다[19].',
    '[19] 의 HQ 결론은 피조개·동죽·바지락 3종 전체에 대한 것')
# compounds / assays
for c in d['compounds']:
    if c['name']=='Xanthine':
        o=c['content_text']; c['content_text']='1189.84–2877.48 μg/g (채취 월별; 동결건조 분말로 추출했으나 결과 표의 생/건 기준 명시 없음)'
        changes.append({"where":"compounds.Xanthine.content_text","before":o,"after":c['content_text'],"why":"[4] 전문 Methods 에 'lyophilized powder' 명시"})
a=d['assays'][0]; o=a['part']; a['part']='살(24시간 해감 후 발라내 -10 °C 보관, 동결건조 분말 시료; 장쑤성 Maojia 항 채집)'
changes.append({"where":"assays[0].part","before":o,"after":a['part'],"why":"[4] 전문 Methods 대조"})
# sources: drop 32, renumber
mp={}; new=[]
for s in d['sources']:
    if s['n']==32: continue
    mp[s['n']]=len(new)+1; s2=dict(s); s2['n']=len(new)+1; new.append(s2)
d['sources']=new
def fix(t):
    return re.sub(r'\[([0-9,\s–]+)\]',lambda m:'['+re.sub(r'\d+',lambda x:str(mp.get(int(x.group()),int(x.group()))),m.group(1))+']',t)
for s in d['sections']: s['body']=fix(s['body'])
for lst in ('compounds','assays'):
    for it in d[lst]:
        it['source']=[mp[x] for x in it['source']]
        for k,v in list(it.items()):
            if isinstance(v,str): it[k]=fix(v)
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open(p.replace('dossier.json','_review/changes.json'),'w'),ensure_ascii=False,indent=1)
print(len(changes))
