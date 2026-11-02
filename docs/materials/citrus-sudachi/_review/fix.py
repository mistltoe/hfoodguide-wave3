import json
p='/home/user/hfoodguide-wave3/docs/materials/citrus-sudachi/dossier.json'
d=json.load(open(p))
changes=[]
def rep(where,obj,key,old,new,why):
    assert old in obj[key], (where,old)
    obj[key]=obj[key].replace(old,new); changes.append({"where":where,"before":old,"after":new,"why":why})
S={s['key']:s for s in d['sections']}
rep('sections.overview',S['overview'],'body',
 "41명 규모의 무작위 대조 시험이 있으며, 내장지방/피하지방 비율만 위약보다 유의하게 줄었다[4].",
 "41명을 배정한 무작위 이중맹검 위약 대조 시험(완료 38명)이 있으며, 위약보다 유의하게 줄어든 것은 내장지방/피하지방 면적 비율뿐이었고 내장지방 면적·허리둘레는 유의하지 않은 경향에 그쳤으며 혈당·지질 지표는 변하지 않았다[4].",
 "[4] 전문: VFA/SFA만 p=.049, VFA p=.064·허리둘레 p=.061, 혈당·지질 유의 변화 없음 — 효과 범위를 원문대로 명시")
rep('sections.processing',S['processing'],'body',
 "스다치 열매 1/3개에 해당한다고 설명되었다[4].",
 "스다치 열매 1/3개에 해당한다고 설명되었다[4]. 다만 논문에 적힌 1.4%와 1,050 mg을 곱하면 약 14.7 mg이어서 4.9 mg과 맞지 않으며, 여기서는 원문 수치를 그대로 옮겼다[4].",
 "[4] 원문 수치 사이의 불일치(1.4% × 1,050 mg ≠ 4.9 mg)를 독자가 알 수 있게 밝힘")
rep('sections.processing',S['processing'],'body',
 "쥐 실험에서는 스다치 즙이 칼슘의 장내 체류 시간을 늘려 염화칼슘의 칼슘 흡수율을 2.86배 높였다(동물 시험)[21].",
 "생쥐 약동학 실험에서는 스다치 즙이 염화칼슘 칼슘의 절대 생체이용률을 2.86배 높이고 장내 평균 체류 시간을 43.1분 늘렸다(동물 시험)[21].",
 "[21] 초록: mice, absolute bioavailability 2.86-fold, MRTab +43.1 min — '쥐'를 '생쥐'로, 지표명을 원문대로")
rep('sections.history',S['history'],'body',
 "말린 잔멸치(시라스보시)에 스다치 즙을 더한 먹이를 흰쥐에 14일 먹인 실험에서 칼슘·마그네슘 흡수율이 높아졌다[20].",
 "말린 잔멸치(시라스보시) 가루를 스다치 즙 20%로 처리한 먹이를 흰쥐에 14일 먹인 실험에서 칼슘·마그네슘의 겉보기 흡수율과 보유율이 높아졌고, 40% 처리군에서는 흡수율 대신 뼈 흡수 지표가 낮아졌다(동물)[20].",
 "[20] 초록: 흡수·보유 증가는 S20 군에서만, S40 군은 뼈 흡수 지표 감소 — 처리 농도별 결과를 구분")
rep('sections.genetics',S['genetics'],'body',
 "핵 유전체 SSR·indel 표지와 세포질 표지로 일본 재래 감귤 101품종을 분석한 연구에서",
 "핵 유전체 SSR·indel 표지와 세포질 표지로 재래 감귤 208품종(군집 분석은 대표 101품종)을 분석한 연구에서",
 "[3] Methods: 재래 품종 208개 포함 371계통, PCoA·STRUCTURE는 대표 101품종")
rep('sections.genetics',S['genetics'],'body',
 "구조 분석에서 스다치는 만다린 계통과 그 자손으로 해석된 군집에 들어갔다[3].",
 "주좌표 분석(PCoA) 군집에서 스다치는 만다린과 그 자손 품종으로 해석된 군집(군집 III)에 들어갔다[3].",
 "[3] 원문: 이 군집 배정은 STRUCTURE가 아니라 PCoA 군집(Cluster III) 서술")
rep('sections.safety',S['safety'],'body',
 "수다치틴은 50 µM에서 정상 섬유모세포 증식을 억제하지 않았으나, 이는 세포 실험 결과다[23].",
 "수다치틴 50 µM(48시간)은 정상 섬유모세포에 세포독성을 보이지 않았으나, 이는 세포 실험 결과다[23].",
 "[23] 초록: 'not cytotoxic against normal fibroblasts' — 증식 억제 여부가 아니라 세포독성 없음")
c=[x for x in d['compounds'] if x['name']=='Sudachitin'][0]
rep('compounds.Sudachitin.activity_ko',c,'activity_ko',
 "사람 시험에서 추출 분말(하루 4.9 mg)로 내장/피하지방 비율 감소[4]",
 "사람 시험에서는 수다치틴 단독이 아닌 껍질 추출 분말(수다치틴 하루 4.9 mg)로 내장/피하지방 면적 비율만 위약 대비 유의 감소[4]",
 "[4]는 껍질 추출 분말 시험으로 수다치틴 단독 효과가 아님; 유의 지표는 비율뿐")
src={s['n']:s for s in d['sources']}
upd={17:("Biosci Biotechnol Biochem 2026 (PMID","Biosci Biotechnol Biochem 2026;90(9):1147-1153 (PMID"),
 23:("Oncol Lett 2022;24(1) (PMID","Oncol Lett 2022;24(1):236 (PMID"),
 22:("Biocontrol Sci 2022;27(1):1- (PMID","Biocontrol Sci 2022;27(1):1-7 (PMID"),
 27:("68(6):513- (PMID","68(6):513-520 (PMID"),
 3:("PMC5130255, 전문 확인)","PMC5130255, 전문 확인; 유자가 꽃가루 부모·고지형 C18 세포질은 parentage 표·Discussion에서 확인)")}
for n,(o,nw) in upd.items():
    rep(f'sources[{n}].title',src[n],'title',o,nw,'PubMed 서지 정보로 권·쪽 보완')
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('/home/user/hfoodguide-wave3/docs/materials/citrus-sudachi/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
