import json
p='dossier.json'; d=json.load(open(p))
S={s['key']:s for s in d['sections']}
changes=[]
def rep(key,old,new,why):
    b=S[key]['body']; assert old in b,(key,old); S[key]['body']=b.replace(old,new); changes.append({"where":f"sections.{key}","before":old,"after":new,"why":why})
rep('history',"국내에서는 2009년 한국버섯학회지 논문이 이 버섯을 일본에서 비싸게 거래되지만 균사 생장이 느려 인공재배가 어려운 버섯으로 소개했다(WebSearch 요약으로만 확인)[34].",
 "국내에서는 2009년 한국버섯학회지 논문이 국내에서 아직 이 버섯의 인공재배가 이루어지지 않았다는 점을 연구 배경으로 들었다(검색 요약으로만 확인)[34].",
 "[34] 원문은 허용 목록 밖이라 열 수 없고, 검색 요약에는 '일본 고가 거래·균사 생장 느림' 내용이 없어 요약에 있는 배경 문장으로 바꿈")
rep('biology',"중국 남서부 고산 한랭 지역의 기록 70건으로 만든 기후 적합지 모델에서는",
 "중국 남서부 고산 한랭 지역의 'L. decastes 복합종' 기록 70건(분자 확인이 고르지 않음)으로 만든 기후 적합지 모델에서는",
 "[33] 은 L. decastes 단일 종이 아니라 복합종 기록을 모은 것이라고 밝힘(근연종 자료 섞임 방지)")
rep('related_species',"같은 복합종의 연기색만가닥버섯(L. fumosum)과 반투명만가닥버섯(L. sykosporum)은 '사용불가'이므로 잿빛만가닥버섯과 구별해야 한다[2].",
 "같은 복합종의 연기색만가닥버섯(L. fumosum)[4]과 같은 속의 반투명만가닥버섯(L. sykosporum)은 목록에서 '사용불가'이므로 잿빛만가닥버섯과 구별해야 한다[2].",
 "[4] 는 복합종에 L. shimeji·L. fumosum·L. decastes 만 듦; L. sykosporum 이 복합종이라는 근거 없음")
rep('genetics',"발달 단계별 전사체·대사체 원자료는 NCBI SRA에 SRR24926090 등의 번호로 등록되었다[10].",
 "발달 단계별 전사체 원자료는 NCBI SRA에 SRR24926090 등의 번호로 등록되었다[10].",
 "[10] 전문 2.5절: SRA 에 올린 것은 전사체 원자료뿐, 대사체 등록 언급 없음")
rep('safety',"2006년 일본 학술지에는 하타케시메지와 관련된 간독성 증례 서신이 실렸으나, 초록이 없어 섭취 형태와 경과는 확인하지 못함[20].",
 "2006년 일본 학술지에는 하타케시메지와 관련된 간독성 증례 서신이 실렸다[20]. PubMed 색인어(고령 여성·건강보조식품·약물 유발 간손상)로 보아 보충제 형태 섭취와 관련된 증례로 보이나, 초록이 없어 섭취량과 경과는 확인하지 못함[20].",
 "PMID 16868813 MeSH 에 Aged·Female·Dietary Supplements·Chemical and Drug Induced Liver Injury 가 있음")
rep('safety',"중금속 실험에서 납은 갓·대로 잘 옮겨지지 않았지만(BAF < 1), 카드뮴은 이동 계수가 모두 1보다 커 자실체로 잘 옮겨졌다[23].",
 "배지에 납·카드뮴을 넣은 재배 실험에서 납은 갓·대의 생물농축계수가 1보다 작았지만(BAF < 1), 카드뮴은 이동 계수(TF)가 모두 1보다 커 자실체로 잘 옮겨졌다[23].",
 "[23] 은 첨가(오염) 실험이고 BAF 는 생물농축계수 — 조건을 밝힘")
rep('safety',"A. cylindracea와 H. leucopus를 제외하면 납·카드뮴 위험이 없다고 보았다[24].",
 "A. cylindracea와 H. leucopus(카드뮴)를 제외하면 납·카드뮴 등 금속 섭취 위험이 없다고 보았다[24].",
 "[24] 초록: 예외 두 종은 카드뮴에 한함")
# compounds
for c in d['compounds']:
    if c['name']=='beta-Glucan':
        old=c['content_text']; c['content_text']="분획 IV-1 평균 분자량 305 kDa; 함량 수치는 초록에 없음[13]"; c['source']=[13]
        changes.append({"where":"compounds.beta-Glucan.content_text","before":old,"after":c['content_text'],"why":"[35] 의 β-글루칸(%)은 조다당 전체의 β-글루칸으로 (1→3) 결합형·열수 분획 IV-1 과 다른 대상 — 섞지 않음(assays 에는 그대로 둠)"})
    if c['name']=='Scopoletin':
        old=c['content_text']; c['content_text']="상대 함량만 보고: 이 경로 대사물 중 가장 많고, 원기 단계가 균사·성숙 단계보다 유의하게 높음[10]"
        changes.append({"where":"compounds.Scopoletin.content_text","before":old,"after":c['content_text'],"why":"[10] 3.4.2: 원기 단계가 균사·성숙 단계보다 높다고만 씀(어린 자실체와 비교 없음)"})
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
