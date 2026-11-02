import json
p='/home/user/hfoodguide-wave3/docs/materials/pampus-argenteus/dossier.json'
d=json.load(open(p))
S={s['key']:s for s in d['sections']}
ch=[]
def rep(key,old,new,why):
    b=S[key]['body']; assert old in b,(key,old); S[key]['body']=b.replace(old,new); ch.append({"where":f"sections.{key}","before":old,"after":new,"why":why})
rep('history',"쿠웨이트 과학연구소의 2012–2016년 시험에서도 자연산 어미 알의 부화율은 25.6–76.7%였으나 변태 치어의 생존율은 3.7–5.7%로 낮았다[21].",
 "쿠웨이트 과학연구소가 2012–2015년 자연산 어미에서 받은 알을 인공수정한 시험에서 부화율은 25.6–76.7%였으나 변태 치어의 생존율은 3.7–5.7%로 낮았고, 2015·2016년 양식 어미가 낳은 알은 대부분 수정되지 않았다[21].",
 "[21] 초록: 자연산 어미 알 시험은 2012–2015년이고 2016년은 양식 어미 산란 기록임")
rep('genetics',"쿠웨이트·파키스탄·중국 집단의 조절영역 분석에서는",
 "형태로 동정한 쿠웨이트·파키스탄(3곳)·중국 샤먼·대만 6개 집단 114개체의 조절영역 분석에서는",
 "[3] 전문: 중국 쪽 표본은 샤먼·대만이며 6개 집단 114개체(대만해협 이남 표본만 씀)")
rep('related_species',"국내 문헌에서는 병어를 처음 P. argenteus, 덕대를 P. echinogaster로 썼으나 최근에는 병어를 P. punctatissimus, 덕대를 P. argenteus로 쓰는 것이 타당하다는 연구가 있다는 검색 결과가 있었으나, 원문은 열지 못해 확인하지 못함[7].",
 "국내에서는 2023년 형태(아가미뚜껑 홈·머리 물결무늬·척추골 수)와 COI 분석으로 한국산 병어를 P. punctatissimus, 덕대를 P. argenteus로 쓰는 것이 타당하다고 본 연구가 있다는 검색 결과가 있었으나(종마다 3개체 분석), 원문은 열지 못해 수치는 확인하지 못함[7]. 이 견해와 덕대를 병어의 동종이명으로 본 연구[4]를 따르면, 중국 연구가 'P. argenteus'라고 적은 개체는 한국 이름으로는 덕대에 해당할 수 있고 한국 시장의 병어는 다른 종(P. punctatissimus)일 수 있다[4, 7]. 국내 '병어' 논문이 P. chinensis로 재동정된 사례는 이번 조사에서 확인하지 못함.",
 "[7] 검색 요약을 구체화하고, [4]·[7]이 식약처 목록 학명과 어긋나는 점(중국 'P. argenteus' 자료=한국 덕대일 가능성)을 명시; P. chinensis 재동정은 출처 없음")
rep('overview',"같은 속의 덕대(Pampus echinogaster, 영문 Korean pomfret)는 목록에서 별도 원료로 올라 있고, 이 문서는 덕대 자료를 따로 섞지 않았다[1].",
 "같은 속의 덕대(Pampus echinogaster, 영문 Korean pomfret, 이명 큰벵치·고려병어)는 목록에서 별도 원료로 올라 있고, 이 문서는 덕대 학명으로 나온 자료를 섞지 않았다[1]. 다만 최근 분류 연구는 덕대를 P. argenteus와 같은 종으로 보거나 한국 병어를 P. punctatissimus로 보므로, 학명만으로는 두 원료의 문헌을 깔끔히 가를 수 없다[4, 7].",
 "학명 처리 근거를 overview에도 밝힘(목록 학명과 최근 분류의 불일치)")
for c in d['compounds']:
    if c['name']=='Selenium':
        o=c['activity_ko']; c['activity_ko']="필수 미량원소이며, 중국 동부 연안 어류(부세·참조기·병어)에서는 셀레늄 농도가 높을수록 총수은 농도가 낮았다[29]"; c['source']=[28,29]
        ch.append({"where":"compounds.Selenium.activity_ko","before":o,"after":c['activity_ko'],"why":"[28] 초록에 수은 독성 완화 언급 없음; [29] 초록의 Se–T-Hg 역상관으로 교체"})
    if c['name']=='Lysine':
        o=c['content_text']; c['content_text']=o.replace("원문에 건량·습량 기준 표기 없음","원문에 건량·습량 기준 표기 없음; 총 아미노산 472.99 mg/g이 습량 조단백질 14.81%보다 커서 습량 기준은 아닌 것으로 보임(검토자 추정)")
        ch.append({"where":"compounds.Lysine.content_text","before":o,"after":c['content_text'],"why":"[16] 표4·표5 대조: mg/g 기준이 습량일 수 없음을 밝힘"})
for a in d['assays']:
    sp=a['conditions']['sample_prep']
    if '닝보 샹산만 부화장' in sp:
        a['conditions']['sample_prep']=sp.replace("중국 저장성 닝보 샹산만 부화장","중국 저장성 샹산만의 상업 부화장")
        ch.append({"where":"assays[2].conditions.sample_prep","before":"중국 저장성 닝보 샹산만 부화장","after":"중국 저장성 샹산만의 상업 부화장","why":"[17] 전문은 'commercial hatchery in Xiangshan Bay, Zhejiang'이며 닝보 언급 없음"})
for s in d['sources']:
    if s['n']==7:
        s['title']="한국산 병어·덕대의 형태와 COI 분석에 따른 학명 재검토(2023; koreascience 게재) — koreascience 가 이 환경에서 막혀 원문을 열지 못하고 WebSearch 검색 결과 요약으로만 확인(요약: 형태·COI로 한국 병어=P. punctatissimus, 덕대=P. argenteus가 타당, 두 종 간 COI 거리 평균 14.6%, 종마다 3개체 분석). 핵심 근거로 쓰지 않음"
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(ch,open('/home/user/hfoodguide-wave3/docs/materials/pampus-argenteus/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(ch))
