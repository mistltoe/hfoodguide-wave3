import json, sys
p='/home/user/hfoodguide-wave3/docs/materials/cuscuta-australis/dossier.json'
d=json.load(open(p))
changes=[]
def rep(key,old,new,why):
    for s in d['sections']:
        if s['key']==key:
            assert old in s['body'], (key,old)
            s['body']=s['body'].replace(old,new)
            changes.append({"where":f"sections.{key}","before":old,"after":new,"why":why}); return
    raise SystemExit(key)

rep('history',
 "1990년대 후반과 2000년대 초 중국 연구들은 실새삼 씨앗의 플라보노이드와 단백질 전기영동 양상으로 두 종을 가리는 방법을 내놓았다[6, 8, 33].",
 "1990년대 후반과 2000년대 초 중국 연구들은 실새삼 씨앗의 플라보노이드와 단백질 전기영동 양상으로 실새삼과 갯실새삼(전기영동 연구는 새삼까지 세 종)을 가리는 방법을 내놓았다[6, 8, 33].",
 "[33] 초록은 갯실새삼·실새삼·새삼 세 종 씨앗을 구별했다고 씀")
rep('history',
 "나이지리아에서는 실새삼의 씨앗과 줄기를 옥수수죽 'Ogi'에 넣어 남녀 생식 기능 문제에 먹는 민간 이용이 있다고 기술되었다[13, 14]. 1990년 중국 연구는 실새삼 알코올 추출물이 화상 입은 생쥐의 대식세포 탐식 기능을 정상 수준으로 회복시켰다고 보고했다(동물)[15].",
 "나이지리아에서는 실새삼의 씨앗과 줄기를 옥수수죽 'Ogi'에 넣어 남녀 생식 기능 문제에 먹는 민간 이용이 있다고 기술되었다[13, 14]. 이 지역 쥐 실험(씨앗·줄기 물 추출물 각 300 mg/kg, 7일)에서는 정자 형태 유지와 생식 호르몬 지표에서 줄기 추출물이 씨앗 추출물보다 효과가 컸다고 보고되어, 씨앗 결과와 줄기 결과를 구분해 읽어야 한다(동물)[13, 14]. 1990년 중국 연구는 실새삼 알코올 추출물(사용 부위 초록에 미기재)이 화상 입은 생쥐의 대식세포 탐식 기능, 용혈소 생성과 림프구 증식을 정상 수준으로 회복시켰다고 보고했다(동물)[15].",
 "[13][14] 초록은 씨앗·줄기 추출물을 따로 시험했고 줄기가 더 효과적이라 결론; [15] 초록에는 부위가 없고 용혈소·림프구 증식도 함께 회복")
rep('cultivation',
 "물과 인이 부족할수록 실새삼 생물량은 커지고 콩의 피해는 커져, 물·인 관리로 피해를 줄일 수 있다고 제안되었다[27].",
 "실새삼 생물량은 물과 인이 모두 가장 적을 때 가장 컸다[27]. 콩의 피해는 물이 부족할수록 커졌지만(보수력 5–15%에서 45–55%보다 약 60% 큼), 인은 반대로 공급이 많을수록 콩의 기생 내성이 낮아져(인 0 μM에서 피해가 20 μM보다 67% 작음), 물·인 공급 관리로 피해를 줄일 수 있다고 제안되었다[27].",
 "[27] 초록: 인 공급이 높을수록 숙주 내성이 낮아짐(0 μM에서 피해 67% 낮음) — '인이 부족할수록 콩 피해가 커진다'는 원문과 반대")
rep('cultivation',
 "환삼덩굴(Humulus scandens)를",
 "환삼덩굴(Humulus scandens)을",
 "조사 오류")
rep('processing',
 "연구용 추출물은 대개 씨앗을 에탄올이나 물로 우려 만들었고, 실새삼 씨앗 에탄올 추출물을 쥐에 125·250 mg/kg 먹인 간 보호 실험이 있다[12].",
 "연구용 추출물은 씨앗이나 줄기를 에탄올이나 물로 우려 만들었다. 실새삼 씨앗과 줄기 에탄올 추출물을 각각 쥐에 125·250 mg/kg씩 7일 먹인 뒤 아세트아미노펜으로 간을 손상시킨 실험에서는 두 추출물 모두 간 손상 지표를 줄였지만 줄기 추출물이 씨앗보다 더 나았다(동물)[12].",
 "[12] 초록은 씨앗·줄기 추출물을 비교했고 줄기 쪽이 더 효과적이라 결론 — 씨앗만 쓴 실험처럼 적힌 것을 바로잡음")
# aliases: 토사자 계열 이름은 기원 혼동 방지 주석
al=d['aliases']
new=[]
for a in al:
    if a=="Cuscutae Semen": b="Cuscutae Semen(약재명; 국내 공정서·식품원료 목록은 갯실새삼 기원)"
    elif a=="Tu-Si-Zi": b="Tu-Si-Zi(중국 약재명; 중국 약전 기원 종의 하나)"
    else: b=a
    if b!=a: changes.append({"where":"aliases","before":a,"after":b,"why":"식품원료 목록상 이명 '토사자'는 갯실새삼 행에만 있음[2], 한국 공정서도 갯실새삼만 기원[3] — 실새삼 별명으로 단독 표기하면 갯실새삼과 섞임"})
    new.append(b)
d['aliases']=new
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('/home/user/hfoodguide-wave3/docs/materials/cuscuta-australis/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
