import json
p='/home/user/hfoodguide-wave3/docs/materials/sanguisorba-minor/dossier.json'
d=json.load(open(p))
S={s['key']:s for s in d['sections']}
def rep(key,old,new):
    b=S[key]['body']; assert old in b,(key,old); S[key]['body']=b.replace(old,new)
rep('related_species','술모이풀은 이 가운데 잎만 쓸 수 있는 원료이므로, 뿌리를 쓰는 오이풀 자료와 섞지 않아야 한다[1].',
    '술모이풀은 잎만 쓸 수 있는 원료이고 오이풀은 잎과 뿌리를 함께 쓸 수 있으므로, 오이풀(특히 뿌리) 자료와 섞지 않아야 한다[1].')
rep('related_species','학명은 Sanguisorba minor Scop.와 Poterium sanguisorba L.가 같은 식물을 가리키며, 국내 목록도 두 이름을 함께 적는다[1]. 1984년 분류 논문은 P. sanguisorba 를 S. minor 와 같은 것으로 보았다고 하나 원문은 열지 못해 WebSearch 요약으로만 확인했다[23]. 최신 Kew POWO 의 정명 처리는 확인하지 못함.',
    '국내 목록은 같은 원료의 학명란에 Sanguisorba minor Scop.와 Poterium sanguisorba L.를 함께 적어 두 이름을 같은 원료로 다룬다[1]. 옛 유럽 문헌에서는 salad burnet 을 Poterium sanguisorba L. 라는 이름으로 적었고, PubMed 는 이 문헌을 오이풀속(Sanguisorba) 주제어로 분류한다[23]. 두 이름 가운데 어느 쪽을 정명으로 보는지에 대한 Kew POWO 등 분류 원자료의 처리는 확인하지 못함.')
rep('safety','생쥐에 지상부 수알코올 추출물을 한 번 먹인 급성 독성 시험에서 무독성량은 2,000 mg/kg까지였고 반수치사량은 3,000 mg/kg보다 높았으며, 4주간 100–400 mg/kg을 먹인 아급성 시험에서도 뚜렷한 이상은 없었다[8].',
    '생쥐에 지상부(줄기·잎) 수알코올 추출물을 한 번 먹인 급성 독성 시험에서 무독성량은 2,000 mg/kg까지였고 반수치사량은 3,000 mg/kg보다 높았으며(종설은 약 3,000 mg/kg으로 옮김), 쥐에게 4주간 100–400 mg/kg을 먹인 아급성 시험에서도 뚜렷한 이상은 없었다[2][8].')
rep('safety','일부 시료에서는 납이 잎채소 기준을 넘어 주의가 필요하다고 했다[9]. 그 연구의 전문 텍스트에서는 종 이름이 빠져 있어 어느 수치가 술모이풀의 것인지 확인하지 못함.',
    '한 종의 마이크로그린에서는 납이 FAO/WHO 잎채소 최대기준(30 μg/100 g 생체중)을 넘어 주의가 필요하다고 했다[9]. 그 연구의 전문 텍스트에서는 종 이름이 빠져 있어 질산염 최고·최저값과 납 초과 시료가 어느 종의 것인지는 확인하지 못함.')
rep('cultivation','[24]','[24]')
for s in d['sections']:
    s['body']=s['body'].replace('[24]','[@24]').replace('[25]','[@25]')
    s['body']=s['body'].replace('[@24]','[24]'.replace('24','23')).replace('[@25]','[24]')
for c in d['compounds']:
    if c['name']=='Punicalagin':
        c['name']='Punicalagin gallate'
        c['name_ko']='푸니칼라긴 갈레이트'
    if c['name']=='Polyphenols':
        c['content_text']='잎 160.96 mg/g 건조중량(초록), 본문에서는 186.56 mg/g dw로 달리 적음; 꽃 131.56, 뿌리 121.36 mg/g dw(초록, 본문 122.07)[3]'
src=[s for s in d['sources'] if s['n']!=23]
for s in src:
    if s['n']>23: s['n']-=1
src.insert(22,{"n":23,"title":"Antibiotic activity of a tannin-tormentol complex extracted from the salad burnet (Poterium sanguisorba L.). Annales pharmaceutiques françaises 1955;13(3):167-168 (프랑스어, PubMed 서지·주제어만 확인, 초록 없음)","url":"https://pubmed.ncbi.nlm.nih.gov/14388438/","publisher":"Masson (PubMed)","accessed":"2026-11-02"})
d['sources']=src
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
