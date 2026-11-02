import json,sys
p='/home/user/hfoodguide-wave3/docs/materials/armillariella-tabescens/dossier.json'
d=json.load(open(p))
S={s['key']:s for s in d['sections']}
changes=[]
def rep(key,old,new,why):
    b=S[key]['body']
    assert b.count(old)==1,(key,old)
    S[key]['body']=b.replace(old,new); changes.append({"where":f"sections.{key}","before":old,"after":new,"why":why})

rep('overview','다당체의 장 보호·혈당·신경 염증 관련 효과는 대부분 동물·세포 실험이며',
 '다당체의 장 보호·혈당·신경 염증 관련 효과는 모두 생쥐 실험 결과이며[18, 30, 31]',
 '[18][30][31] 초록은 모두 생쥐 실험 — "대부분 동물·세포"보다 정확히 씀')
rep('history','종소명 tabescens는 1772년 『Flora Carniolica』에 처음 실린 이름에 바탕을 두며, 2017년 연구는 이를 기초명으로 삼아 새 조합 Desarmillaria tabescens를 발표했다[2].',
 '2017년 연구는 1772년 『Flora Carniolica』에 실린 Agaricus tabescens Scop.를 기초명으로 삼아 새 조합 Desarmillaria tabescens (Scop.) R.A. Koch & Aime를 발표했다[2].',
 '[2] 전문 분류 기재: 기초명 Agaricus tabescens Scop. 1772, 새 조합 저자명 확인 — 학명 근거를 구체화')
rep('history','그러나 식약처 목록과 여러 약리 연구는 지금도 Armillariella tabescens라는 옛 이름을 주로 쓴다[1, 8, 9].',
 '그러나 식약처 목록과 여러 약리 연구는 지금도 Armillariella tabescens라는 옛 이름을 주로 쓴다[1, 8, 9]. 영어권 도감에서는 \'ringless honey mushroom\'(턱받이 없는 뽕나무버섯)이라는 이름이 쓰이나, 미국 미주리주 자연보전국 도감은 이 이름을 북미의 Desarmillaria caespitosa(옛 A. tabescens)에 붙이고 있어 이 종만 가리키는 이름으로 보기 어렵다(웹 검색 요약으로만 확인, 페이지는 열지 못함)[33].',
 'name_en \'Ringless honey mushroom\' 출처 없음 — 공공기관 도감(웹 검색 요약) 근거를 달고, 북미 근연종에 쓰이는 이름임을 밝힘')
rep('history','뒤의 연구들은 이 효소를 아플라톡신 산화효소(AFO)라 불렀고, 2017년 결정 구조 분석에서 다이펩티딜 펩티데이스 III(DPP III) 활성도 함께 가진 효소로 밝혀졌다[21].',
 '이 버섯에서 분리된 아플라톡신 산화효소(AFO)는 아플라톡신 B1의 비스퓨란 고리를 끊어 해독한다고 보고되었고, 2017년 결정 구조 분석에서 다이펩티딜 펩티데이스 III(DPP III) 활성도 함께 가진 이중 활성 효소로 밝혀졌다[21].',
 '[21] 초록은 2001년 효소[20]와 AFO가 같은 효소라고 말하지 않음 — 동일시 문장 삭제')
rep('related_species','약 4,100만 년 전(95% 신뢰구간 2,400만–5,900만 년)',
 '약 4,100만 년 전(95% 최고사후밀도 구간 2,400만–5,900만 년)',
 '[2] 전문은 베이즈 분석의 95% HPD로 보고 — 신뢰구간 아님')
rep('related_species','야생 채집 시료는 형태만이 아니라 교배·유전자 분석으로 종을 확인해야 섞임을 막을 수 있다[5, 23].',
 '야생 채집 시료는 형태만이 아니라 교배·유전자 분석으로 종을 확인해야 섞임을 막을 수 있다[5, 23]. 또 2021년 다유전자 계통 분석 연구는 미국·멕시코 시료를 근거로 북미 집단을 유럽의 D. tabescens와 형태·유전적으로 구별되는 대응종 Desarmillaria caespitosa로 새로 조합했다[32]. 따라서 그 이전에 북미에서 A. tabescens 또는 D. tabescens로 보고된 연구[5, 24]는 지금 기준으로는 이 북미 종을 다룬 것일 수 있다[32].',
 '근연종 혼동: 북미 \'tabescens\'가 2021년 D. caespitosa로 분리된 사실(PMID 33914673)을 추가')
rep('cultivation','스위스 연구는 4% 맥아 추출 한천 배지에서 순수 배양한 뒤 22 ℃, 상대습도 75%에서 나무 토막과 함께 1–4개월 배양했다[3, 4].',
 '발광 목재 연구는 4% 맥아 추출 한천 배지에서 키운 균을 3% 미세섬유화 셀룰로스 현탁액에 잠긴 발사나무 토막에 접종해 22 ℃, 상대습도 75%에서 1–4개월 배양했다[3, 4].',
 '[4] 전문: 나무 토막은 3% MFC 현탁액에서 배양 — 배양 조건 보완, 국가 표기는 원문에 명시되지 않아 뺌')
rep('cultivation','실험실에서는 단포자 분리주끼리 짝지은 49개 조합의 이배체 균주 가운데 24개가 자실체를 맺었다[25].',
 '실험실에서는 단포자 분리주끼리 짝지은 49개 조합에서 얻은 이배체 균주를 자실체로 키웠고, 그 가운데 24개는 적어도 일부가 이핵인 자실층하층을 가진 자실체를 맺었다[25].',
 '[25] 초록: 24개는 \'이핵 자실층하층을 가진 자실체\'를 맺은 수 — 자실체를 맺은 전체 수가 아님')
rep('cultivation','한편 이 종은 과수원에서 복숭아나무 뿌리썩음병을 일으키므로, 미국 남동부에서는 재배 대상이 아니라 방제 대상으로 연구된다[24].',
 '한편 미국 남동부 연구는 이 이름의 균을 복숭아나무 뿌리썩음병의 주된 원인균으로 다루었다[24].',
 '\'재배 대상이 아니라 방제 대상\'은 [24] 초록에 없는 추론 — 출처가 말한 범위로 줄임')
rep('safety','2020년 식용버섯 266개 시료의 비소 종 분석에서 뽕나무버섯부치의 무기비소 함량은 3.63 mg/kg으로 비교적 높아 소비자 건강에 잠재적 위험이 될 수 있다고 보고되었다[15]. 초록에는 이 값이 생중량 기준인지 건조중량 기준인지, 시료 산지가 어디인지 적혀 있지 않다[15].',
 '2020년 중국 쓰촨성(청두)의 대학·질병예방통제센터 연구진이 식용버섯 8종 266개 시료의 비소 화학종을 분석한 연구에서, 뽕나무버섯부치(Armillariella tabescens)의 무기비소 함량은 3.63 mg/kg으로 일부 재배 아가리쿠스버섯(Agaricus blazei, 최고 4.50 mg/kg)과 함께 비교적 높아 소비자 건강에 잠재적 위험이 될 수 있다고 보고되었다[15]. 초록에는 이 값이 생중량 기준인지 건조중량 기준인지, 이 종의 시료 수와 채집 산지·야생 여부가 적혀 있지 않으므로, 국내 유통품의 함량으로 그대로 옮겨 쓸 수 없다[15].',
 '[15] 메타데이터: 연구진 소속이 쓰촨대·청두시 CDC — 산지 미상·기준 미상을 분명히 하고 비교값을 원문대로 덧붙임')
rep('safety','균사체 다당의 혈당·신경 염증 개선 효과 등도 생쥐 실험 결과이며, 사람에서의 효과와 안전성은 확인하지 못함[30, 31].',
 '균사체 다당의 혈당 개선 효과와 배양 균이 세포 밖으로 낸 다당의 신경 염증 완화 효과도 생쥐 실험 결과이며, 사람에서의 효과와 안전성은 확인하지 못함[30, 31].',
 '[31] 은 균사체 다당이 아니라 세포 밖 다당(ATEP)')

# assay
a=d['assays'][0]
old=a['content']
a['content']='뽕나무버섯부치 무기비소 3.63 mg/kg (생·건 기준, 이 종의 시료 수와 산지는 초록에 명시되지 않음; 연구진 소속은 중국 쓰촨성 청두)[15]'
changes.append({"where":"assays[0].content","before":old,"after":a['content'],"why":"기준·산지 미상 명시, 연구진 소속(PubMed 메타데이터) 추가"})
# sources
d['sources'].append({"n":32,"title":"Desarmillaria caespitosa, a North American vicariant of D. tabescens (초록 Mycologia, 2021; PMID 33914673)","url":"https://pubmed.ncbi.nlm.nih.gov/33914673/","publisher":"Mycologia (PubMed)","accessed":"2026-11-02"})
d['sources'].append({"n":33,"title":"Ringless Honey Mushroom — Missouri Department of Conservation Field Guide (웹 검색 결과 요약으로만 확인, 페이지는 네트워크 제한으로 열지 못함)","url":"https://mdc.mo.gov/discover-nature/field-guide/ringless-honey-mushroom","publisher":"Missouri Department of Conservation","accessed":"2026-11-02"})
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('/home/user/hfoodguide-wave3/docs/materials/armillariella-tabescens/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
