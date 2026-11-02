import json,sys
p='/home/user/hfoodguide-wave3/docs/materials/vicia-cracca/dossier.json'
d=json.load(open(p))
S={s['key']:s for s in d['sections']}
changes=[]
def rep(where,obj,key,old,new,why):
    v=obj[key]
    assert old in v,(where,old)
    obj[key]=v.replace(old,new)
    changes.append({"where":where,"before":old,"after":new,"why":why})
ov=S['overview']
rep('sections.overview',ov,'body','이 종에서 성분을 정량한 논문은 많지 않으며, 터키산 아종 자료가 대표적이다[3]. 이 아종(V. cracca subsp. cracca) 정유의 주성분은 2-에틸퓨란(27.3%)이었고, 메탄올 추출물의 주요 페놀 성분은 시나프산(0.31 mg/g)이었다[3].',
 '이 종에서 성분을 정량한 논문은 많지 않으며, 튀르키예 연구진이 V. cracca subsp. cracca를 분석한 자료가 대표적이다(채집지·사용 부위는 초록에 없음)[3]. 이 아종 정유의 주성분은 2-에틸퓨란(27.3%)이었고, 메탄올 추출물의 주요 페놀 성분은 시나프산(0.31 mg/g, 건물·추출물 기준은 초록에 없음)이었다[3].',
 '[3] 초록에는 채집 국가·부위가 없고(저자 소속만 튀르키예), mg/g 의 기준도 없음')
rep('sections.overview',ov,'body','잎줄기에서는 자연계에 드문 시안아마이드가 만들어지는 것이 확인되었다[2]. 씨앗에는 혈액형 A형 적혈구를 응집시키는 렉틴과 만노스·포도당 결합 렉틴, 트립신 저해제가 들어 있다[4–7].',
 '이 종은 자연계에서 드물게 시안아마이드를 만드는 식물로 확인되었으나, 측정 부위와 함량은 초록에서 확인하지 못함[2]. 씨앗에는 혈액형 A형 적혈구를 응집시키는 렉틴과 만노스·포도당 결합 렉틴이 들어 있고[4–6], 이 종에서 트립신 저해제도 분리되었다(부위는 서지 정보에 없음)[7].',
 '[2] 초록은 개화 전·개화기 함량을 쟀다고만 하고 부위(잎줄기)를 말하지 않음(잎 국재는 V. villosa 유묘). [7] 은 초록 없는 서지로 제목에 씨앗이 없음')
h=S['history']
rep('sections.history',h,'body','1950년대 핀란드 학술지에는','1950–60년대 핀란드 학술지에는','1961년 보고를 1950년대로 묶은 오류')
rep('sections.history',h,'body','북미에서는 유럽에서 들어와 귀화한 외래 침입종으로 분류되며,','캐나다 온타리오주와 캐나다 대부분 지역에서는 외래·침입·귀화종으로 분류되며,','[14] 전문은 온타리오·캐나다에서 exotic, invasive, naturalized 라고만 하고 유럽 기원은 말하지 않음')
b=S['biology']
rep('sections.biology',b,'body','캐나다 온타리오주 조사에서는 이 종이 5–7월에 꽃을 피우며, 개체수가 줄고 있는 뒤영벌 3종이 주로 이 꽃에서 꽃가루를 모았다[14].',
 '캐나다 온타리오주 조사 논문은 이 종이 5–7월에 꽃을 피운다고 인용했고, 개체수가 줄고 있는 뒤영벌 3종의 채식이 이 종과 뚜렷이 연관되었으며 이 꽃에서는 주로 꽃가루를 모으는 모습이 기록되었다[14].',
 '[14] 전문: at-risk 종이 V. cracca 와 양의 상관, 이 식물에서는 꽃가루 채집이 가장 많이 기록됨 — "주로 이 꽃에서" 는 과장')
r=S['related_species']
rep('sections.related_species',r,'body','한국 자생 갈퀴나물속 19분류군(59개체)을 DNA 바코드로 비교한 연구에서는 Cracca절의 가까운 종들이 바코드만으로는 잘 갈리지 않아, 16개 형태 형질을 함께 써야 모든 종을 구별할 수 있었다[13].',
 '한국 자생 갈퀴나물속 19분류군(59곳에서 채집)을 DNA 바코드로 비교한 연구에서는 10분류군만 바코드 조합으로 구별되었고, 나머지 9분류군은 16개 형태 형질을 함께 써야 구별되었다[13].',
 '[13] 전문: 59 different locations; 바코드로 구별되지 않은 9분류군이 Cracca절인지는 확인하지 못해 일반화')
c=S['cultivation']
rep('sections.cultivation',c,'body','이 종은 주로 들에서 자라는 야생 식물로 기록되어 있고, 북미에서는 귀화한 외래 침입종으로 콩·옥수수·겨울밀 밭에서 제초제로 방제된다[14].',
 '이 종은 풀밭·길가·강둑·숲 가장자리에서 자라는 야생 식물로 기록되어 있고[12], 캐나다 온타리오주에서는 귀화한 외래 침입종으로 콩·옥수수·겨울밀 밭에서 농약으로 방제된다[14].',
 '"들에서 자라는" 문장에 출처 없음 → [12]; [14] 는 온타리오 자료')
rep('sections.cultivation',c,'body','이 종의 생장이 줄거나 잎에 눈에 보이는 피해가 나타났다[27].','이 종의 생장이 줄거나 눈에 보이는 피해가 나타났다[27].','[27] 초록은 visible injuries 라고만 함')
s=S['safety']
rep('sections.safety',s,'body','이 종의 잎줄기는 자연 시안아마이드를 만들며, 553종의 식물을 조사한 연구에서 이 능력이 확인된 것은 V. villosa subsp. varia, 등갈퀴나물, 아까시나무 3종뿐이었다[2]. 함량 수치는 초록에서 확인하지 못함.',
 '이 종은 자연 시안아마이드를 만들며, 연구진이 지금까지 조사한 553종의 식물 가운데 이 능력이 확인된 것은 V. villosa subsp. varia, 등갈퀴나물, 아까시나무 3종뿐이었다[2]. 측정 부위·함량 수치와 섭취 시 영향은 초록에서 확인하지 못함.',
 '[2] 초록에 부위 없음')
rep('sections.safety',s,'body','씨앗에는 적혈구를 응집시키는 렉틴과 트립신 저해제가 들어 있다[4–7].','씨앗에는 적혈구를 응집시키는 렉틴이 들어 있고[4–6], 이 종에서 트립신 저해제도 분리되었다(부위는 서지 정보에 없음)[7]. 이 종 씨앗을 먹었을 때의 영향을 조사한 연구는 확인하지 못함.',
 '[7] 부위 미상; 항영양 성분의 섭취 영향 근거 없음 명시')
rep('sections.safety',s,'body','캐나다 PCB 오염지에서 이 종의 지상부 평균 PCB 농도는 35 µg/g(건조 중량)으로 조사한 잡초 27종 가운데 가장 높았다[18]. 라듐 생산 폐기물 보관지에서는 지상부에 주로 라듐-226이 쌓였다[20]. 다만 폴란드 고속도로변 조사에서는 이 종의 아연 함량이 비교 식물 가운데 가장 낮았다[31]. 길가·산업 오염지에서 채취한 순은 피하는 것이 안전하다[18, 20].',
 '오염 토양 정화(식물 추출) 가능성을 본 캐나다 연구에서, PCB 오염 토양(31·4.7 µg/g)에서 자란 이 종의 지상부 평균 PCB 농도는 35 µg/g(건조 중량)으로 조사한 잡초 27종 가운데 가장 높았다[18]. 러시아 라듐 생산 폐기물 보관지 연구에서는 이 종 지상부에 주로 라듐-226이 쌓였으나(초록 표기 \'22Ra\'), 우라늄·토륨 계열 핵종의 식물 농축계수는 모두 1보다 낮았다[20]. 폴란드 고속도로변 조사에서는 이 종의 아연 함량이 비교 식물 가운데 가장 낮았다[31]. 이 연구들은 오염지 식물을 다룬 환경 연구로 식용 순의 섭취 위험을 평가한 것은 아니지만, 이 종이 토양의 PCB를 지상부에 쌓을 수 있음을 보여 주므로 오염이 의심되는 곳에서 채취한 순은 피하는 편이 낫다[18].',
 '오염지 자료가 식용 위험처럼 읽히지 않게 연구 맥락(정화 연구·토양 농도·농축계수<1)을 밝히고, [20] 은 섭취 권고를 뒷받침하지 않아 권고 문장 출처에서 뺌')
# compounds
for cp in d['compounds']:
    if cp['name']=='Cyanamide':
        old=cp['part']; cp['part']='부위는 초록에서 확인하지 못함(개화 전·개화기에 측정)'
        changes.append({"where":"compounds.Cyanamide.part","before":old,"after":cp['part'],"why":"[2] 초록에 부위 없음"})
    if cp['name']=='2-Ethylfuran':
        old=cp['part']; cp['part']='정유(V. cracca subsp. cracca, 부위는 초록에서 확인하지 못함)'
        changes.append({"where":"compounds.2-Ethylfuran.part","before":old,"after":cp['part'],"why":"[3] 초록에 증류 부위 없음"})
    if cp['name']=='Trypsin inhibitor':
        old=cp['part']; cp['part']='확인하지 못함(초록 없음, 제목에 부위 없음)'
        changes.append({"where":"compounds.Trypsin inhibitor.part","before":old,"after":cp['part'],"why":"[7] 제목은 'from Vicia cracca' 로 씨앗을 말하지 않음"})
for a in d['assays']:
    if a['compound']=='Cyanamide':
        old=a['part']; a['part']='부위는 초록에서 확인하지 못함(개화 전·개화기에 측정)'
        changes.append({"where":"assays.Cyanamide.part","before":old,"after":a['part'],"why":"[2] 초록에 부위 없음"})
    if a['compound']=='Sinapic acid':
        old=a['content']; a['content']='0.31 mg/g(건물·추출물 기준은 초록에서 확인하지 못함)[3]'
        changes.append({"where":"assays.Sinapic acid.content","before":old,"after":a['content'],"why":"기준 미상 명시"})
json.dump(d,open(p,'w'),ensure_ascii=False,indent=2)
json.dump(changes,open('/home/user/hfoodguide-wave3/docs/materials/vicia-cracca/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
