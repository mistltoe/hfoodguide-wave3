import json,sys
p='dossier.json'; d=json.load(open(p))
changes=[]
def sec(k): return next(s for s in d['sections'] if s['key']==k)
def rep(obj,key,old,new,why,where):
    v=obj[key]; assert old in v,(where,old)
    obj[key]=v.replace(old,new); changes.append({"where":where,"before":old,"after":new,"why":why})
# related_species
s=sec('related_species')
rep(s,'body',"중국 6개 성에서 모은 물쑥 10계통 가운데 후난성 웨양 계통 하나만 다른 쑥속 종과 작은 가지로 묶였고 나머지는 따로 한 가지를 이루었다[4].",
 "중국 6개 성에서 모은 물쑥 10계통 가운데 후난성 웨양 계통을 뺀 나머지는 따로 작은 가지를 이루었고, 웨양 계통은 다른 분류군과 작은 가지로 묶였다(묶인 상대의 학명은 확인하지 못함)[4].",
 "[4] 전문 추출본에서 웨양 계통과 묶인 상대 분류군 이름이 빠져 있어 '다른 쑥속 종'이라 단정할 수 없음","sections.related_species")
rep(s,'body',"쑥속(Artemisia)은 국화과에서 가장 큰 속으로 약 300종이",
 "쑥속(Artemisia)은 국화과에서 가장 큰 속으로 약 300종(같은 논문 고찰에서는 약 400종)이",
 "[4] 서론은 약 300종, 고찰은 약 400종이라고 적어 두 값을 함께 밝힘","sections.related_species")
rep(s,'body',"같은 목록에서 쑥(애엽: 황해쑥·쑥·산쑥)·비쑥·맑은대쑥은 잎,",
 "같은 목록에서 쑥(애엽: 황해쑥·쑥·산쑥)·비쑥·맑은대쑥은 잎(애엽의 '약쑥줄기' 행은 '제한적사용'·줄기),",
 "I1020 원자료에 약쑥줄기 행이 '제한적사용, 제한적사용가능부위 : 줄기'로 있어 부위별 지위를 원자료대로 보충","sections.related_species")
rep(s,'body',"개똥쑥(Artemisia annua)은 '제한적사용'(줄기·잎)이고,",
 "개똥쑥(Artemisia annua)은 식품원료 행이 '제한적사용'(사용가능부위: 줄기, 잎)이고 건강기능식품 개별인정형 원료(C코드) 행이 따로 있으며,",
 "I1020 원자료에 개똥쑥 C코드(개별인정) 행이 있어 정확히 함","sections.related_species")
# processing [2]
s=sec('processing')
rep(s,'body',"7월에 채집해 말린 전초(herb)를 물로 끓여 얻은 추출물은 총 페놀산 557.3 mg GAE/100 g(건조중량), 70% 에탄올 추출물은 총 플라보노이드 987.0 mg 루틴 당량/100 g으로 가장 높았다[2].",
 "7월에 채집해 말린 식물체(원문 'herbs', 사용 부위는 밝히지 않음 — 잎만의 값이 아님)를 물로 끓여 얻은 추출물은 총 페놀산 557.3 mg GAE/100 g(건조 식물체 기준), 70% 에탄올 추출물은 총 플라보노이드 987.0 mg 루틴 당량/100 g(건조 식물체 기준)으로 가장 높았다[2].",
 "[2] 전문 3.1절은 부위를 적지 않고 'herbs'라고만 함 — '전초'로 단정하지 않고 잎 결과가 아님을 밝힘","sections.processing")
# assays
a=d['assays'][2]
rep(a,'part',"7월 채집 전초, 50 °C 48시간 건조 분말","7월 채집 식물체(원문 'herbs', 부위 미기재), 50 °C 48시간 건조 분말","[2] 전문은 부위를 밝히지 않음","assays[2].part")
rep(a['conditions'],'sample_prep',"분말 100 g을 물(또는 70%·95% 에탄올) 1,000 mL에 1시간 담근 뒤 1.5시간 끓임(환류), 2회 추출 후 감압 농축·진공 건조",
 "분말 100 g을 물(또는 에탄올) 1,000 mL에 1시간 담근 뒤 1.5시간 끓임(에탄올은 환류), 2회 추출 후 50 °C 감압 농축·40 °C 진공 건조 48시간(원문 방법 절은 '70% 에탄올 추출'을 '75% 에탄올'로 적어 표기가 엇갈림)",
 "[2] 3.3절 원문 대조: 70% 추출 항목에 75% 에탄올로 적혀 있고 농축·건조 온도 보충","assays[2].conditions.sample_prep")
rep(a,'rationale',"(FRAP R² 0.8797 대 0.5555)","(FRAP 상관계수 0.8797 대 0.5555 — 원문 기호가 R인지 R²인지 추출본에서 확인하지 못함)",
 "[2] 추출본에서 상관 지표 기호가 빠져 R²로 단정할 수 없음","assays[2].rationale")
rep(a,'rationale',"전초 시료라 잎만의 값은 아니다[2].","부위를 밝히지 않은 식물체 시료라 잎만의 값은 아니다[2].","[2] 부위 미기재","assays[2].rationale")
a=d['assays'][0]
rep(a,'rationale',"식물에 있는 전구체(마트리신류)가 증류 중 열분해되어 생기므로","식물에 있는 무색 전구체(저자들은 마트리신으로 보았으나 정유 GC-MS에서 마트리신은 검출되지 않음)가 증류 중 열분해되어 생기므로",
 "[3] 2.1절: 마트리신·카마줄렌 카복실산은 정유에서 검출되지 않았고 전구체는 추정임","assays[0].rationale")
# compounds
for c in d['compounds']:
    if c['name']=='Canin':
        rep(c,'activity_ko',"구아이안형 삼량체가 간암세포주 3종에서 IC50 5.0–16.1 μM(세포)[26]",
            "카닌 자체의 활성은 확인하지 못함; 함께 분리된 구아이안형 세스퀴테르펜 삼량체(카닌 아님)가 간암세포주 3종에서 IC50 5.0–16.1 μM(세포)[26]",
            "[26] 활성은 새 삼량체 1–6의 값이며 카닌의 값이 아님 — 과장 방지","compounds.Canin.activity_ko")
    if c['name']=='Eucalyptol':
        rep(c,'part',"지상부 정유·휘발 성분","정유·휘발 성분([3]은 개화기 지상부, [24]는 부위를 초록에서 확인하지 못함)",
            "[24] 초록은 시료 부위를 밝히지 않음","compounds.Eucalyptol.part")
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
