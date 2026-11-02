import json
p='dossier.json'; d=json.load(open(p))
S={s['key']:s for s in d['sections']}
changes=[]
def rep(key,a,b,why):
    s=S[key]; assert a in s['body'],(key,a); s['body']=s['body'].replace(a,b); changes.append({"where":f"sections.{key}","before":a,"after":b,"why":why})
rep('overview','2014년 국내 연구진이 세종기지 인근에서 잡은 개체로 유전체 초안을 처음 발표했다[2].',
    '2014년 국내 연구진이 주도한 국제 공동 연구가 세종기지 인근 마리안 소만에서 잡은 개체로 이 종의 유전체 초안을 발표했다[2].',
    '[2] 저자에 미국·호주 연구자가 함께 있고, 채집지는 세종기지 인근 마리안 소만(2012년 1월)')
rep('history','1990년대 논문에서는 Notothenia coriiceps neglecta라는 아종 이름으로 혈색소·부동 당단백질 유전자가 보고되었다[20, 21].',
    '1990년 논문들에서는 Notothenia coriiceps neglecta라는 아종 이름으로 혈색소 β 사슬 아미노산 서열과 부동 당단백질 유전자가 보고되었다[20, 21].',
    '[20] 은 유전자가 아니라 혈색소 β 사슬 아미노산 서열 연구이고, 두 논문 모두 1990년')
rep('history',"국내에서는 1995년 남극 세종기지 주변에서 잡은 'Notothenia neglecta' 대구류의",
    "국내에서는 1995년 한국해양연구소 극지연구센터가 활동하는 남극 해역에서 잡은 'Notothenia neglecta' 대구류의",
    '[28] 초록은 세종기지를 직접 쓰지 않고 한국해양연구소 극지연구센터가 운영되는 남극 해역이라고만 씀')
rep('history','2010년대 이후 극지 연구 기관들은 세종기지 부두와 맥스웰만 연안에서 이 종을 낚시·통발로 잡아 유전체·성장·생리 연구에 써 왔다[2, 7].',
    '국내 극지 연구에서는 2012년 1월 세종기지 인근 마리안 소만에서 낚시로 잡은 개체를 유전체 연구에, 2023년 1–2월 세종기지 부두와 맥스웰만 촛대바위 연안에서 낚시·통발로 잡은 개체를 성장 연구에 썼다[2, 7].',
    '[2]·[7] 이 말하는 것은 두 차례 채집(2012년·2023년)뿐이며 "2010년대 이후 써 왔다"는 일반화는 출처에 없음')
rep('biology','표준체장 95.8–109.3 mm의 어린 개체 위 내용물은 주로 단각류와 크릴류였다[9].',
    '표준체장 95.8–109.3 mm의 어린 개체를 포함한 연안 돌치류 3종의 위 내용물은 주로 단각류와 크릴류였고 해조류는 드물었다[9].',
    '[9] 의 식성 결론은 이 종만이 아니라 함께 조사한 3종 전체에 대한 것')
rep('cultivation','남극반도 서쪽은 최근 수십 년간 남극해에서 기후변화 영향을 가장 크게 받은 해역으로,',
    '남극반도 서쪽은 최근 수십 년간 남극해에서 기후변화 영향을 가장 크게 받은 해역 중 하나로,',
    '[8] 은 "one of the most impacted areas"')
rep('cultivation','이런 수온 변화는 협온성인 이 종의 성장과 개체군에 영향을 줄 수 있다고 해석되었다[8].',
    '이석 성장 궤적과 해수면 수온 추세를 함께 보면 수온 상승이 협온성인 이 종의 성장에 대체로(일관되게는 아니지만) 부정적인 영향을 준 것으로 해석되었다[8].',
    '[8] 은 성장에 대한 "generally consistent, although not unequivocal, negative effect"만 말하고 개체군 영향은 다루지 않음')
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('_review/changes.json','w'),ensure_ascii=False,indent=1)
import re
n=sum(len([x for x in re.split(r'(?<=[.다함])\s+',s['body']) if x.strip()]) for s in d['sections'])
items=sum(len(d[k]) for k in ['aliases','compounds','markers','assays','nutrients','production','gi','orgs','world','sources'])
print(n,items)
