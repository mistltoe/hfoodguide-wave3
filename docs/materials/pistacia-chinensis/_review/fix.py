import json
from pathlib import Path
P=Path(__file__).resolve().parent.parent/"dossier.json"
d=json.load(open(P))
S={s["key"]:s for s in d["sections"]}
changes=[]
def rep(key,old,new,why):
    b=S[key]["body"]; assert b.count(old)==1,(key,old)
    S[key]["body"]=b.replace(old,new); changes.append({"where":f"sections.{key}","before":old,"after":new,"why":why})
rep("overview","바이오디젤 원료로 연구되어 왔다[3, 10, 12, 23]","바이오디젤 원료로 연구되어 왔다[3, 10, 12, 25]","[23] 은 정원수·목재·바이오디젤을 말하지 않음(남중국 재배·충영 민간약만); 정원수·목재·약용은 [3]·[25] 가 말함")
rep("overview","보고된 효과는 시험관·세포·동물 실험이고","잎에 대해 보고된 효과는 시험관·세포 실험 수준이고","잎 자료([3][4])에는 동물 실험이 없음 — 동물 실험은 나무껍질 추출물([21])이라 잎 결과로 쓰면 안 됨")
rep("history","채소로도 쓰였다고 기록되어 있으나, 어느 부위를 먹었는지는 확인하지 못함.","채소로도 쓰였다고 기록되어 있으나, 어느 부위를 먹었는지는 확인하지 못함[10].","출처 표시 누락 — [10] 서론에 'used as a vegetable' 있음")
rep("biology","이집트에서 재배된 잎의 에탄올 추출물을","이집트 연구진이 잎의 에탄올 추출물을","[6] 초록에 시료 재배지(이집트) 언급 없음, 저자 소속만 이집트")
rep("biology","중국 산시성 시료를","중국 산시성(陝西省) 시료를","[7] 은 Shaanxi — 산서성(山西)과 구분")
rep("related_species","인도 전통의학의 '카크라싱기(Kakdashringi)'라는","인도 전통의학의 '카크다슈링기(Kakdashringi)'라는","원문 표기 Kakdashringi 에 맞게 음역 수정")
rep("related_species","파키스탄에서 수행된 일부 연구도 'P. chinensis'라 적었으나 아종 표기가 없어, 이 백과에서는 해당 결과를 황연목 잎 자료로 쓰지 않는다[21].",
 "파키스탄 연구진의 항산화·고환 독성 완화 연구도 'P. chinensis'라 적었으나 아종 표기가 없고, 쥐 실험에 쓴 것은 나무껍질 에틸아세테이트 추출물이어서 황연목 잎 자료로 쓰지 않는다[21]. 한국 연구진의 메탄올 추출물 대식세포·혈소판 실험[22, 23] 가운데 혈소판 연구는 원료가 줄기 껍질이었고[23], 대식세포 연구는 초록에 부위가 적혀 있지 않아 역시 잎 결과로 쓰지 않는다[22].",
 "[21] 초록: 시료는 bark·leaves, 생체 실험은 bark 에틸아세테이트 분획(PCBE); [23] 전문: trunk bark 사용 — 나무껍질 결과가 잎 결과로 섞이지 않도록 명시")
rep("processing","다만 이 연구 본문에서 황연목 차의 원료 부위(잎·순)와 종별 개별 수치는 확인하지 못함.","이 연구는 꽃으로 만든 3종과 씨앗으로 만든 2종을 뺀 나머지 차는 잎으로 만들었다고 적었으나, 전문 본문에서 종명이 빠져 있어 황연목 차의 원료 부위와 종별 개별 수치는 확인하지 못함[8].","[8] 2.1절: 꽃 3종·씨앗 2종 외에는 잎 — 원문 정보 보강, 출처 표시")
rep("genetics","개체의 3분의 1 이상이 잡종으로 분류되어 재배 과정에서 유전 다양성이 줄었다고 해석되었다[10].","개체의 3분의 1 이상이 잡종으로 분류되었고, 연구진은 재배 과정에서 유전 다양성이 줄었을 것으로 해석했다[10].","[10] 은 잡종 비율과 다양성 감소를 인과로 잇지 않음 — 별개 서술로 분리")
rep("safety","시험관에서 이 세 종의 잎·씨앗 메탄올 추출물이 말 적혈구에 메트헤모글로빈을 만들고 용혈을 일으켰으며, 씨앗 추출물이 잎보다 강했다[9].","시험관에서 이 세 종의 잎·씨앗 메탄올 추출물이 말 적혈구에 메트헤모글로빈을 만들고 용혈을 일으켰으며, 씨앗 추출물이 잎보다 강했고 잎 추출물의 메트헤모글로빈 형성은 '미미' 수준이었다[9]. 치료받은 두 마리의 소변에서는 피로갈롤이 검출되었다[9].","[9] 전문: 잎 추출물은 minimal color change, 소변 피로갈롤 검출 — 잎 위험도를 과장하지 않도록 보강")
rep("safety","말은 산화 손상에 특히 약한 동물이어서 이 결과를 사람에게 그대로 옮길 수는 없다[9].","말은 적혈구의 산화 손상 방어 기전이 다른 포유류보다 약하다[9]. 따라서 이 결과를 사람에게 그대로 옮길 수는 없다.","[9] 는 말의 취약성만 말하고 사람 외삽 불가는 검토자 해석 — 출처 귀속 분리")
for c in d["compounds"]:
    if c["name"].startswith("7-Hydroxy-3-"):
        old=c["activity_ko"]; c["activity_ko"]="잔가지에서 입체 배치만 다른 두 이량체를 분리, 에스트로겐 작용제 활성 보고(시험계는 초록으로 확인하지 못함)[24]"
        changes.append({"where":"compounds[네오플라본 이량체].activity_ko","before":old,"after":c["activity_ko"],"why":"[24] 초록에 세포 실험 여부 없음"})
for a in d["assays"]:
    if a["compound"]=="Limonene":
        old=a["conditions"]["instrument"]; a["conditions"]["instrument"]="가스크로마토그래프(Thermo Trace GC Ultra) + 질량분석기(Polaris Q MSD, Thermo Fisher Scientific)"
        changes.append({"where":"assays[Limonene].conditions.instrument","before":old,"after":a["conditions"]["instrument"],"why":"[3] 2.3절에 '이온트랩형' 표기 없음 — 원문 기기명으로"})
json.dump(d,open(P,"w"),ensure_ascii=False,indent=1)
json.dump(changes,open(P.parent/"_review/changes.json","w"),ensure_ascii=False,indent=1)
print(len(changes))
