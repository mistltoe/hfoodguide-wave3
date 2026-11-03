import json
p='dossier.json'; d=json.load(open(p))
S={s['key']:s for s in d['sections']}
def rep(obj,key,old,new):
    assert old in obj[key], (key,old); obj[key]=obj[key].replace(old,new)
rep(S['overview'],'body',"다만 효소·펩타이드 연구는 정제 물질의 시험관·동물 실험이어서 개불을 먹었을 때의 효과를 보여 주지 않는다[26, 27, 30].",
 "다만 효소·펩타이드·다당 연구는 정제·추출 물질의 시험관·세포·동물 실험이어서 개불을 먹었을 때의 효과를 보여 주지 않는다[7, 8, 26, 27, 30].")
rep(S['processing'],'body',"시료는 총아미노산이 486.65 mg 으로, 글루탐산 72.810 mg/g, 글리신 68.025 mg/g, 알라닌 60.785 mg/g, 아스파르트산 56.540 mg/g 순으로 많았다[6].",
 "시료는 총아미노산이 486.65 mg(원문 단위 표기 그대로이며, 표 1 의 개별 값은 동결건조 가수분해물 분말 1 g 당 mg)으로, 글루탐산 72.810 mg/g, 글리신 68.025 mg/g, 알라닌 60.785 mg/g, 아스파르트산 56.540 mg/g 순으로 많았다[6]. 이 값은 건조한 가수분해물 분말 기준이어서 생 개불 살의 함량과는 다르다[6].")
rep(S['processing'],'body',"고온·고압·초음파로 얻은 개불 펩타이드를 당뇨 쥐에 8주간 100·500 mg/kg/일 경구 투여한 동물 실험도 있으나 동물 결과일 뿐이다[30].",
 "고온·고압·초음파로 얻은 개불 펩타이드를 당뇨 유발 쥐에 8주간 100·500 mg/kg/일 위관으로 먹여 발기 기능 지표를 본 동물 실험도 있으나, 사람이나 일반 식품 섭취에 관한 결과가 아니다[30].")
rep(S['genetics'],'body',"PacBio 장독 서열·Illumina 단독 서열·Hi-C","PacBio 장독 서열·Illumina 단편(short-read) 서열·Hi-C")
C={c['name']:c for c in d['compounds']}
for n in ['L-Glutamic acid','Glycine','L-Aspartic acid','L-Leucine']:
    rep(C[n],'content_text','(가수분해물)','(동결건조 가수분해물 분말 1 g 당, 건물 기준)')
rep(C['L-Alanine'],'content_text','60.785 ± 5.936 mg/g[6]','60.785 ± 5.936 mg/g(동결건조 가수분해물 분말 1 g 당, 건물 기준)[6]')
rep(C['VTSALVGPR'],'activity_ko','H2O2 손상 RAW264.7 세포 생존율 회복(세포 실험)','H2O2 손상 RAW264.7 세포 생존율 회복(고상 합성한 펩타이드로 한 세포 실험)')
rep(C['Urechistachykinin I'],'activity_ko','합성 펩타이드가 Vibrio vulnificus 에 항균 작용(시험관)','이 펩타이드가 Vibrio vulnificus 에 항균 작용(시험관)')
A=d['assays']
rep(A[0],'content','총 486.65 mg;','총 486.65 mg(원문 표기, 동결건조 가수분해물 분말 기준);')
A[1]['conditions']['instrument']="황산기: 흡광도 360 nm(기기 명시 없음); 분자량: HPLC(RID); 단당: HPAEC-PAD"
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
