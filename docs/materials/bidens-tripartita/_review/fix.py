import json,sys
p='/home/user/hfoodguide-wave3/docs/materials/bidens-tripartita/dossier.json'
d=json.load(open(p))
changes=[]
def sec(k): return [s for s in d['sections'] if s['key']==k][0]
def rep(where,obj,key,old,new,why):
    assert old in obj[key], (where,old)
    obj[key]=obj[key].replace(old,new); changes.append({"where":where,"before":old,"after":new,"why":why})
S=sec
rep('sections.overview',S('overview'),'body','trifid bur-marigold 등으로 부른다[3, 20]','trifid bur-marigold 등으로 부른다[3]','[20] 초록에는 영어 이름이 없다; [3] 서론에 있음')
rep('sections.overview',S('overview'),'body','러시아·동유럽에서는 지상부를 우린 물을','러시아에서는 지상부를 우린 물을','[3]·[13]은 러시아 전통의학 사용만 말함; 동유럽 민간약 사용 근거 없음')
rep('sections.biology',S('biology'),'body','이곳 식생은 주로 토양 종자은행에서 되살아났다[21]','이곳 식물은 주로 토양 종자은행과 남은 개체의 재생으로 되살아났다[21]','[21] 초록: soil seed bank and regeneration of remnant individuals')
rep('sections.biology',S('biology'),'body','씨앗 형태에 따라 자란 개체의 키가 달랐다[20]','경쟁이 없을 때는 씨앗 형태에 따라 자란 개체의 키가 달랐으나 경쟁 조건에서는 차이가 줄었다[20]','[20] 초록: 키 차이는 경쟁 없이 키울 때만 뚜렷')
rep('sections.biology',S('biology'),'body','북미 원산 침입종인 미국가막사리가 키와 생물량에서 가막사리보다 우세했다[20]','북미 원산 침입종인 미국가막사리가 키와 생물량에서 가막사리보다 우세했다[10, 20]','[20]은 침입종이라고만 씀; 북미 원산은 [10] 서론')
rep('sections.related_species',S('related_species'),'body','같은 조건에서 미국가막사리가 셀레늄을 더 많이 모았다[10]','두 나라 시료 전체로 보면 미국가막사리의 셀레늄 함량이 유의하게 더 높았다[10]','[10]은 같은 조건 비교가 아니라 각기 다른 장소 시료 전체의 종간 비교(U 검정)')
rep('sections.processing',S('processing'),'body','전통적으로는 지상부를 그늘에서 말려 우린 물(침출액)로 쓴다[3, 15].','전통적으로는 지상부를 우린 물(침출액)로 쓴다[3, 15].','그늘 건조는 [3] 연구의 시료 처리이지 전통 용법 기술이 아님')
rep('sections.processing',S('processing'),'body','꽃 핀 지상부를 3시간 수증기 증류해 얻은 정유는','꽃 핀 지상부 말린 것 20 kg을 클레벤저형 장치로 3시간 물증류(hydrodistillation)해 얻은 정유는','[7] 방법: hydrodistilled(물증류), 수증기 증류 아님')
rep('sections.genetics',S('genetics'),'body','같은 서식지에서 함께 자라는 미국가막사리와는 경쟁 관계이며, 두 종의 혼동 가능성을 유의해야 한다[10, 20].','미국가막사리는 같은 강가 서식지에서 가막사리와 함께 자라며 경쟁하므로[10, 20], 야생 채집 시료는 종을 확인해야 한다.','[10]·[20]은 두 종의 혼동을 말하지 않음 — 공존·경쟁만 출처로 두고 권고는 출처 없는 서술로 분리')
rep('sections.safety',S('safety'),'body','지상부 정유는 사람 피부 섬유아세포에서 100 mg/mL 이하로는 세포독성·DNA 손상이 없었으나 150–200 mg/mL에서는 독성이 나타났다[7].','지상부 정유는 사람 피부 섬유아세포 24시간 처리에서 50·100 농도(원문 단위가 mg/g과 mg/mL로 섞여 있음)에서는 세포독성·DNA 손상이 유의하게 늘지 않았으나 150·200 mg/mL에서는 늘었다(세포 실험)[7].','[7] 원문은 시험 농도를 mg/g과 mg/mL로 섞어 적음; 세포 실험임을 밝힘')
c={x['name']:x for x in d['compounds']}
def crep(n,k,old,new,why): rep(f'compounds[{n}].{k}',c[n],k,old,new,why)
crep('Caftaric acid','part','지상부(물 추출물)','추출물·침출액(초록에 부위 기재 없음)','[6] 초록에 사용 부위가 없음')
crep('Caftaric acid','activity_ko','추출물의 항산화 활성에 기여하는 폴리페놀 가운데 하나로 보고(시험관)[6]','이 성분이 든 추출물이 DPPH 라디칼을 소거(시험관, 성분 단독 활성은 시험하지 않음)[6]','[6] 초록은 카프타르산의 기여를 따로 말하지 않음')
crep('Epicatechin','part','지상부(추출물)','추출물(초록에 부위 기재 없음)','[5] 초록에 사용 부위가 없음')
crep('beta-Ocimene','part','지상부(초임계 CO2 추출 휘발성분)','초임계 CO2 추출 휘발성분(초록에 부위 기재 없음)','[9] 초록에 사용 부위가 없음')
crep('alpha-Pinene','part','뿌리(식품원료 사용부위 아님)·지상부 휘발성분','뿌리(식품원료 사용부위 아님)·초임계 추출 휘발성분(부위 미기재)','[9] 초록에 사용 부위가 없음')
crep('alpha-Pinene','content_text','지상부 초임계 추출 휘발성분의 주요 성분 가운데 하나[9]','초임계 CO2 추출 휘발성분의 주요 성분 가운데 하나[9]','[9] 초록에 사용 부위가 없음')
crep('p-Cymene','activity_ko','지상부 정유가 칸디다 균주 성장을 억제(시험관)[7]','이 성분이 든 지상부 정유와 그 하이드로겔이 칸디다 균주 성장을 억제(시험관, 성분 단독 활성은 시험하지 않음)[7]','[7]은 정유·겔 제형을 시험했고 p-시멘 단독은 시험하지 않음')
a=[x for x in d['assays'] if x['compound']=='p-Cymene'][0]
rep('assays[p-Cymene].conditions.sample_prep',a['conditions'],'sample_prep','클레벤저형 장치로 3시간 수증기 증류','클레벤저형 장치로 3시간 물증류(hydrodistillation, 약전 방법)','[7] 원문 hydrodistilled')
for cmp in ['Cynaroside','Chlorogenic acid']:
    a=[x for x in d['assays'] if x['compound']==cmp][0]
    rep(f'assays[{cmp}].conditions.sample_prep',a['conditions'],'sample_prep','추출물 10 mg을 물:메탄올(1:1) 10 mL에 녹여 0.45 μm 여과 후 주입','에탄올 추출물·부탄올 분획 10 mg은 물:메탄올(1:1) 10 mL, 에틸아세테이트 분획 10 mg은 메탄올 10 mL에 녹여 0.45 μm 여과 후 주입','[3] 방법: 에틸아세테이트 분획은 메탄올에 녹임')
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('/home/user/hfoodguide-wave3/docs/materials/bidens-tripartita/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
