import json,sys
p=sys.argv[1]
d=json.load(open(p))
changes=[]
def sec(k): return [s for s in d['sections'] if s['key']==k][0]
def rep(where,obj,key,old,new,why):
    assert old in obj[key], (where,old)
    obj[key]=obj[key].replace(old,new); changes.append({"where":where,"before":old,"after":new,"why":why})

b=sec('biology')
rep('sections.biology',b,'body','북쪽 노르웨이에서 모로코와 동지중해까지','노르웨이 북부에서 모로코와 동지중해까지','[13] 원문은 Northern Norway')
rep('sections.biology',b,'body','어른 개체는 탈피 전에 큰 집게 근육이 40–75% 줄어들며, 이때 칼슘 의존 단백질분해효소와 프로테아좀이 근육 분해를 돕는다[38].',
 '어른 바닷가재는 탈피 전에 큰 집게 근육이 40–75% 위축되고 칼슘 의존 단백질분해효소와 프로테아좀이 이를 돕는다는 것은 [38]이 서론에서 정리한 선행 지식(종 구분 없음)이며, 이 연구 자체는 유럽바다가재 유생(1–3기)과 어린 개체의 집게 근육에서 프로테아좀 활성이 탈피 단계에 따라 오르내림을 보였다[38].',
 '[38] 초록의 40–75%는 어른 바닷가재 일반에 대한 배경 서술이고 이 종의 측정값이 아님 — 근연종(아메리카바다가재) 선행연구 값이 이 종 결과로 읽히지 않게 함')
rep('sections.biology',b,'body','위액에는 카텝신 D 계열의 산성 단백질분해효소가 있어 몸 밖 소화에 쓰이고, 그 mRNA는 굶기면 40% 줄었다[27]. 이 효소는 낮은 온도에서도 활성을 유지하는 저온 적응 성질을 보였다[28].',
 '위액에는 카텝신 D 계열의 산성 단백질분해효소가 있어 몸 밖 소화에 쓰이고, 이 종에서 소화 효소형인 카텝신 D1의 mRNA는 굶기면 40% 줄었다[27]. 두 바닷가재 종의 위액 효소를 함께 정제해 소 카텝신 D와 비교한 연구에서 이 효소는 4–25 °C에서 KM이 변하지 않는 등 저온 적응 성질을 보였다(초록에 종별 값은 따로 없음)[28].',
 '[27]의 40%는 이 종 값이 맞고(아메리카바다가재는 유의 변화 없음) D1 mRNA임을 밝힘; [28]은 두 종을 묶어 기술하므로 그렇게 표시')
rep('sections.biology',b,'body','살아 있을 때 껍데기의 푸른빛은 단백질에 붙은 아스타잔틴에서 나온다[24].','살아 있을 때 껍데기의 푸른빛은 단백질(크러스타시아닌)에 붙은 아스타잔틴에서 나온다[24, 40].','[24] 초록은 종명을 적지 않아 이 종 껍데기임을 밝힌 [40]을 더함')

r=sec('related_species')
rep('sections.related_species',r,'body','이 문서는 아메리카바다가재 자료를 섞지 않으며, 두 종을 함께 다룬 연구는 유럽바다가재 결과만 옮겼다[17, 27].',
 '이 문서는 아메리카바다가재 자료를 섞지 않으며, 두 종을 함께 다룬 연구 가운데 종별 값이 나뉜 경우는 유럽바다가재 값만 옮겼고(카텝신 D1 mRNA 40% 감소)[27], 초록이 두 종을 묶어 말한 결론은 그렇다고 표시했다[17, 28].',
 '[17]·[28] 초록은 두 종을 구분하지 않고 결론을 냄 — "이 종 결과만 옮겼다"는 [27]에만 맞음')

pr=sec('processing')
rep('sections.processing',pr,'body','근육과 생식소는 단백질이 많고 간췌장은 지방·콜레스테롤·열량이 높았다[17]. 이 연구는 모든 가식 부위가',
 '근육과 생식소는 단백질이 많고 간췌장은 지방·콜레스테롤·열량이 높았다[17]. 다만 이 비교와 결론은 초록에서 유럽바다가재와 아메리카바다가재를 묶어 말한 것이며, 종별 수치는 전문을 보지 못해 확인하지 못함. 이 연구는 두 종의 모든 가식 부위가',
 '[17] 초록은 두 종 공통 결론 — 종별 값으로 읽히지 않게 표시')
rep('sections.processing',pr,'body','살아 있을 때 검푸른 껍데기는 단백질 크러스타시아닌에 붙은 아스타잔틴 때문이며, 결합 상태의 흡수 극대는 632 nm다[24].',
 '살아 있을 때 검푸른 껍데기는 단백질 크러스타시아닌에 붙은 아스타잔틴 때문이며, 결합 상태의 흡수 극대는 632 nm다[24]. 유럽바다가재 껍데기의 α-크러스타시아닌은 β-크러스타시아닌 8개(단백질 아단위 16개, 아스타잔틴 16분자)로 된 복합체다[40].',
 '종 근거 보강: [40](같은 연구진 종설)이 대상 종을 Homarus gammarus 로 명시')
rep('sections.processing',pr,'body','이 β-크러스타시아닌 결정 구조(PDB 1GKA)는 유럽바다가재의 것으로 분류되어 이후 계산 연구에 쓰였다[26].',
 '[24] 초록은 종을 \'lobster\'로만 적지만, 같은 연구진의 종설은 이 β-크러스타시아닌 구조 연구의 대상이 유럽바다가재 껍데기임을 밝혔고[40], 2026년 계산 연구도 이 구조(PDB 1GKA)를 유럽바다가재 항목으로 다뤘다[26]. PDB 원 기록은 열지 못해 직접 확인하지 못함.',
 '1GKA 의 종 귀속 근거가 [26] 하나뿐이었음 — [26] 전문 표 3에서 Homarus gammarus 로 적힘을 확인했고, 원 구조 연구진 종설 [40]으로 보강. RCSB 는 프록시에 막혀 열지 못함')

c=sec('safety')
rep('sections.safety',c,'body','잉글랜드·웨일스 야생 개체 952마리 중 가프케미아 균은 9건에서만 분리되었다[21].','잉글랜드·웨일스 30곳의 야생 개체 시료 952개 중 가프케미아 균은 9건에서만 분리되었다[21].','[21] 원문은 952 samples(30 sites)')

for cp in d['compounds']:
    if cp['name']=='Astaxanthin':
        rep('compounds.Astaxanthin.activity_ko',cp,'activity_ko','항산화 작용은 계산(도킹) 연구로만 제시되었다[26]','항산화 작용은 주로 계산(도킹) 연구로 제시되었고 실험 근거는 예비 수준이다[26]','[26] 초록은 예비 실험 근거도 있다고 씀')
        cp['source']=[24,26,40]
    if cp['name']=='Crustacyanin':
        rep('compounds.Crustacyanin.content_text',cp,'content_text','α-크러스타시아닌 = β 단위 8개(아스타잔틴 16분자) [26]','α-크러스타시아닌 = β 단위 8개(아스타잔틴 16분자) [26, 40]','이 종 명시 출처 [40] 추가')
        cp['source']=[24,25,26,36,40]
    if cp['name'] in ('Protein','Lipid'):
        old=cp['activity_ko']; cp['activity_ko']=old.replace('[17]','(두 종을 묶은 초록 결론)[17]'); changes.append({"where":f"compounds.{cp['name']}.activity_ko","before":old,"after":cp['activity_ko'],"why":"[17] 초록은 두 종 공통"})
    if cp['name']=='Cholesterol':
        rep('compounds.Cholesterol.content_text',cp,'content_text','간췌장에서 높음(','간췌장에서 높음(두 종을 묶은 초록 결론; ','[17] 초록은 두 종 공통')
    if cp['name']=='Essential amino acids':
        rep('compounds.EAA.content_text',cp,'content_text','모든 가식 부위가 좋은 공급원(','두 종의 모든 가식 부위가 좋은 공급원(','[17] 초록은 두 종 공통')
    if cp['name']=='Cathepsin D':
        rep('compounds.CathepsinD.activity_ko',cp,'activity_ko','저온에서도 활성이 유지된다[27, 28]','저온에서도 활성이 유지된다(저온 성질은 두 종 효소를 함께 분석한 결과)[27, 28]','[28] 은 두 종 묶음')

for a in d['assays']:
    if a['compound']=='Protein':
        co=a['conditions']
        rep('assays.Protein.detection',co,'detection','750 nm 흡광(상용 Lowry 기반 미량 단백질 키트 BIO-RAD 500-0112)','750 nm 흡광(상용 Lowry 기반 미량 단백질 정량 키트)','상표·제품번호 대신 일반명')
        rep('assays.Protein.sample_prep',co,'sample_prep','얼음물로 마취·치사 후 증류수로 헹궈 −80 °C 보관; 처리군별 6–12마리를 모아 분쇄(Krups Speedy Pro) 후 분석 반복 3회','얼음처럼 찬 해수로 마취·치사 후 증류수로 헹궈 −80 °C 보관; 처리군별 6–12마리를 모아 균질기로 분쇄 후 분석 반복 3회','원문은 ice-cold seawater; 상표명 제거')
    if a['compound']=='Lipid':
        pass

d['sources'].append({"n":40,"title":"Unravelling the structural chemistry of the colouration mechanism in lobster shell. Acta Crystallogr D 2003;59(Pt 12):2072-82","url":"https://doi.org/10.1107/s0907444903025952","publisher":"Acta Crystallographica Section D (초록만 확인) (PubMed 14646064)","accessed":"2026-11-02"})
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open(sys.argv[2],'w'),ensure_ascii=False,indent=1)
print(len(changes))
