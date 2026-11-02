import json
p='/home/user/hfoodguide-wave3/docs/materials/caragana-sinica/dossier.json'
d=json.load(open(p))
ch=[]
def rep(obj,key,old,new,where,why):
    v=obj[key]; assert old in v,(where,old); obj[key]=v.replace(old,new); ch.append({"where":where,"before":old,"after":new,"why":why})
S={s['key']:s for s in d['sections']}
rep(S['history'],'body',"뿌리 추출물·분획은 쥐 골관절염·관절염 모델[16, 17]과 신경세포 ADAM10 유전자 발현 선별 연구[27]에 쓰였고",
 "뿌리 추출물·분획은 쥐 골관절염·관절염 모델[16, 17]에 쓰였고, 골담초 추출물(부위는 초록에 없음)은 사람 신경모세포종 세포의 ADAM10 유전자 발현 선별과 생쥐 투여 시험[27]에 쓰였으며",
 "sections.history","[27] 초록은 'extract of Caragana sinica'라고만 하고 부위를 밝히지 않음 — 뿌리 연구로 단정할 근거 없음, 생쥐 시험도 포함")
rep(S['biology'],'body',"줄기는 목질 바이오매스로서 리그닌 구조가 분석되었는데",
 "목질 바이오매스(탈랍한 골담초 목질부, 세부 부위는 초록에 없음)로서 리그닌 구조가 분석되었는데",
 "sections.biology","[28] 초록은 'dewaxed Caragana sinica'·woody biomass라고만 하고 '줄기'라고 하지 않음")
c={x['name']:x for x in d['compounds']}
rep(c['Ethyl linolenate'],'activity_ko',"저자는 문헌을 들어 피부 상처 회복 관련 성분일 수 있다고 추정[3]",
 "저자는 피톨·리놀렌산·리놀레산 에틸을 상처 회복 관련 문헌 성분으로 들었으나 리놀렌산 에틸 자체는 언급하지 않음(단일 성분 시험 없음)[3]",
 "compounds[Ethyl linolenate].activity_ko","[3] 전문 2.7절은 phytol, linolenic acid, ethyl linoleate 만 언급")
rep(c['alpha-Viniferin'],'activity_ko',"단백질 키나아제 C 억제[26]","단백질 키나아제 C 억제(시험관, 부위는 초록에 없음)[26]",
 "compounds[alpha-Viniferin].activity_ko","[26] 초록은 시험관 결과이고 부위 미기재")
a=d['assays'][0]
rep(a,'content',"총플라보노이드 47.90 ± 0.37, 총폴리페놀 195.13 ± 0.64(표 단위",
 "총플라보노이드 47.90 ± 0.37, 총폴리페놀 195.13 ± 0.64(추출물 건조중량 기준 — 꽃 원물 기준 아님; 표 단위",
 "assays[0].content","[4] 방법 절은 'per gram dry weight of extracts' — 원물이 아니라 추출물 기준임을 밝힘")
b=d['assays'][1]['conditions']
ch.append({"where":"assays[1].conditions.mobile_phase","before":b['mobile_phase'],"after":"","why":"원문에 운반 기체 기재 없음 — 원문에 없는 칸은 비움"})
b['mobile_phase']=""
src={s['n']:s for s in d['sources']}
rep(src[24],'title',"phenolic acids from Caragana species (C. korshinskii).","phenolic acids from Caragana species using response surface methodology (대상 종 C. korshinskii).",
 "sources[24].title","원 제목과 다르게 적혀 있었음")
rep(src[2],'title',"골담초뿌리 행(부위 '뿌리', 이명 '금작근(金雀根), 골담초꽃', 사용불가;",
 "골담초뿌리 행(식품원료 A코드, 부위 '뿌리', 이명 '금작근(金雀根), 골담초꽃', 학명 'Caragana sinica (Buchoz) Rehder , Caragana chamlagu Lam.', 사용 조건 칸 '사용가능부위 : 꽃', 상태 사용불가;",
 "sources[2].title","로컬 I1020_20261013.json 원 행 그대로 칸을 보충")
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(ch,open('/home/user/hfoodguide-wave3/docs/materials/caragana-sinica/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(ch))
