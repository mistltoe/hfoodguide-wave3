import json
p='/home/user/hfoodguide-wave3/docs/materials/amaranthus-mangostanus/dossier.json'
d=json.load(open(p))
changes=[]
def sec(key,old,new,why):
    for s in d['sections']:
        if s['key']==key:
            assert old in s['body'],(key,old)
            s['body']=s['body'].replace(old,new); changes.append({"where":"sections."+key,"before":old,"after":new,"why":why}); return
    raise KeyError(key)
sec('overview',"비름(Amaranthus mangostanus L.)은 비름과 비름속의 한해살이 잎채소로, 영어로는 edible amaranth라 부르고 우리나라에서는 어린순을 데쳐 나물로 먹는다[1, 3].",
 "비름(Amaranthus mangostanus L.)은 비름과(Amaranthaceae)의 한해살이풀로 채소로 먹으며, 영어로는 edible amaranth라 부른다[1, 3, 4]. 식약처 목록에는 '비름나물'이라는 다른 이름과 함께 순이 사용 부위로 올라 있다[1].",
 "'어린순을 데쳐 나물로 먹는다'는 [1]·[3] 어디에도 없음([3] 전문 확인); 한해살이는 [4](annual forb), 과는 [3]")
sec('overview',"세포·동물 실험에서 파골세포 분화 억제가 보고되었으나 사람 자료는 확인하지 못함.",
 "세포 실험에서 파골세포 분화 억제, 난소절제 생쥐에서 골 손실 억제가 보고되었으나[3] 사람 자료는 확인하지 못함.",
 "출처 표시 누락; [3] 전문에 따라 세포·동물 결과를 구분")
sec('biology',"중국 온실 시험에서 씨앗 한 알의 무게는 평균 0.5–1.0 mg으로 매우 작았고, 천립중은 0.7 g으로 계산에 쓰였다[4]. 같은 시험에서 발아 뒤 65일까지를 유묘기, 104일까지를 개화기, 122일 무렵을 종자 성숙기로 나누었다[4].",
 "중국 연구의 재료 설명에 따르면 씨앗은 한 알 평균 0.5–1.0 mg으로 매우 작고, 생장률 계산에는 천립중 0.7 g을 썼다[4]. 이 온실 화분 시험에서는 발아 뒤 65일(첫 꽃눈 전, 유묘기), 104일(개화기), 122일(종자 성숙기)에 수확해 비교했다[4].",
 "[4] 전문: 씨앗 무게는 시험 측정값이 아니라 재료 설명; 65·104·122일은 각 단계의 수확 시점")
sec('biology',"잎의 질소 농도는 생육 단계와 관계없이 건물 1 g당 24.4–25.7 mg으로 비슷했으나",
 "같은 시험(질소·인 시비 처리 평균)에서 잎의 질소 농도는 생육 단계와 관계없이 건물 1 g당 24.4–25.7 mg으로 비슷했으나",
 "[4] 값은 16개 시비 처리 전체의 평균임을 밝힘")
sec('biology',"잎은 13-히드로퍼옥시드 분해효소(HPL) 활성이 특히 높은 재료로 보고되었다[16].",
 "본문에서 A. tricolor로 적은 한 중국 논문(제목에 A. mangostanus 병기)은 잎을 13-히드로퍼옥시드 분해효소(HPL) 활성이 특히 높은 재료로 보고했다[16].",
 "[16] 초록은 재료를 Amaranthus tricolor 로만 적음 — 이명 근거가 제목 병기뿐이므로 이 종 자료로 단정하지 않음")
sec('related_species',"A. tricolor와의 관계는 문헌마다 다르다[16, 18]. 한 논문은",
 "A. tricolor와의 관계는 근거가 엇갈린다. 한 논문은",
 "[18] 은 두 이름의 관계를 다루지 않음")
sec('related_species',"이 문서에서 A. tricolor 자료는 그 이름을 밝혀 따로 적었다[17, 18].",
 "다른 중국 연구는 'amaranth'의 학명을 A. tricolor L.로만 적었다[18]. 이 문서에서 A. tricolor 자료는 그 이름을 밝혀 따로 적었다[17, 18].",
 "[18] 이 실제로 말하는 내용으로 연결")
sec('cultivation',"수확 3·7·10일 시료를 분석했다[8].",
 "농약 살포 3·7·10일 뒤 시료를 분석했다[8].",
 "[8] 초록: 'collected at 3, 7, or 10 days after application'")
sec('processing',"잎에서 얻은 HPL 효소는 향료 산업용으로 연구되었다[16].",
 "A. tricolor로 적힌 잎(제목에 A. mangostanus 병기)에서 얻은 HPL 효소는 향료 산업용으로 연구되었다[16].",
 "[16] 재료명 A. tricolor 명시")
sec('genetics',"비름과 같은 식물로 다루기도 하는 A. tricolor는",
 "한 논문이 비름과 같은 식물로 다룬[16] A. tricolor는",
 "이명 근거를 [16] 하나로 한정해 밝힘")
sec('genetics',"장독 서열과 염색질 접촉 지도(Hi-C)를 함께 써서",
 "장독 서열(PacBio HiFi·Nanopore 초장독)과 염색질 접촉 지도(Hi-C)를 함께 써서",
 "[17] 초록 방법 명시")
sec('genetics',"염분은 칼슘 통로 경쟁을 통해 카드뮴 흡수를 32–36% 줄이기도 했다[13].",
 "다만 카드뮴 농도가 매우 낮은 수경 재배에서는 고염분이 칼슘 통로 경쟁을 통해 뿌리 카드뮴 흡수를 32–36% 줄였다[13].",
 "[13] 조건(수경, 27 nM Cd, 고염분)을 밝혀 [11]·[12] 토양 결과와 혼동 방지")
for c in d['compounds']:
    if c['name']=='Hydroperoxide lyase':
        old=c['content_text']; c['content_text']="논문 재료명 A. tricolor(제목에 A. mangostanus 병기); "+old
        changes.append({"where":"compounds.Hydroperoxide lyase.content_text","before":old,"after":c['content_text'],"why":"[16] 초록은 A. tricolor 로만 적음"})
    if c['name']=='Calcium':
        old=c['part']; c['part']="식물체(부위 초록에 명시 없음)·뿌리"
        changes.append({"where":"compounds.Calcium.part","before":old,"after":c['part'],"why":"[10] 초록은 부위 미명시, [21] 은 뿌리 칼슘"})
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('/home/user/hfoodguide-wave3/docs/materials/amaranthus-mangostanus/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
