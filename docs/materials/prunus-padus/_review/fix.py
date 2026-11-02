import json,re
p='/home/user/hfoodguide-wave3/docs/materials/prunus-padus/dossier.json'
d=json.load(open(p))
changes=[]
def sec(k): return [s for s in d['sections'] if s['key']==k][0]
def rep(k,old,new,why):
    s=sec(k); assert old in s['body'],(k,old); s['body']=s['body'].replace(old,new); changes.append({"where":"sections."+k,"before":old,"after":new,"why":why})
rep('overview','열매는 지름 1 cm 남짓한 검붉은 핵과로, 이탈리아에서','기본종 귀룽나무의 열매는 지름 1 cm 남짓한 검붉은 핵과이며, 이탈리아에서',
    '[2]의 열매 크기·색은 기본종(P. padus) 자료이므로 변종(서울귀룽나무) 서술처럼 읽히지 않게 주어를 기본종으로 밝힘')
rep('history','한국에서는 귀룽나무가 뇌졸중·신경통·간염 등에 쓰인 전통 약재로 소개되었으며, 이 근거를 살피려는 연구가 줄기 추출 분획으로 이루어졌다[8].',
    '국내 대학 연구진의 2012년 논문은 귀룽나무(P. padus)가 뇌졸중·신경통·간염 등에 전통 약으로 널리 쓰였다고 소개하고, 줄기 추출물의 염화메틸렌 분획으로 세포·생쥐 실험을 했다[8].',
    '[8] 초록은 전통 사용 지역을 한국으로 특정하지 않음; 분획(methylene chloride)과 실험 수준(세포·생쥐)을 원문대로 밝힘')
rep('history','열매·나무껍질·잎 가루·꽃은 러시아와 스칸디나비아에서 민간 약으로 쓰였고,','열매·나무껍질·잎 가루·꽃은 러시아와 스칸디나비아에서 마취·소독 용도의 민간 약으로 쓰인다고 하며,',
    '[2] 원문은 anesthetics and disinfectants 로 현재형 서술')
rep('related_species','매실나무씨앗·살구나무씨앗처럼 씨앗 행은 \'사용불가\'이다[1].','매실나무씨앗·살구나무씨앗 행은 \'사용불가\'이다[1].',
    'I1020 원자료에는 왕벚나무씨앗·만첩홍매실씨앗처럼 사용가능한 씨앗 행도 있어 일반화를 뺌')
rep('related_species','영어로 black cherry라 불리는 북미의 P. serotina는 귀룽나무와 함께 다뤄지는 일이 많아 자료를 옮길 때 종을 구별해야 한다[3].',
    '영어로 American black cherry라 불리는 북미의 P. serotina는 [3]처럼 귀룽나무와 한 리뷰에서 함께 다뤄지기도 하므로 자료를 옮길 때 종을 구별해야 하며[3], 식약처 목록에도 \'세로티나벚나무열매\'(P. serotina Ehrh., 열매(씨앗 제외) 사용가능)로 따로 올라 있다[1].',
    '[3]은 한 리뷰일 뿐이라 \'일이 많아\' 일반화를 줄이고, I1020 원자료의 P. serotina 별도 행을 덧붙여 근연종 구분 근거를 보강')
rep('safety','리뷰는 열매의 씨에 시안배당체가 있어 열처리 없이 많이 먹으면 해로울 수 있다고 적었다[3].',
    'P. padus와 P. serotina를 함께 다룬 리뷰는 두 종을 묶은 \'야생 벚나무류\' 열매의 씨에 시안배당체가 있어 열처리 없이 많이 먹으면 해로울 수 있다고 적었다[3].',
    '[3] 원문 문장의 주어는 두 종을 묶은 wild cherry 로 P. padus 단독 서술이 아님')
rep('safety','같은 가루의 지방산 가운데 에루크산이 74.55%로 높아 저자들은 섭취량 평가가 더 필요하다고 했다[4].',
    '같은 가루의 지방산 가운데 에루크산이 74.55%로 높았고, 저자들은 독성학적으로 우려가 될 수 있다며 유럽식품안전청의 에루크산 내용일일섭취량(체중 kg당 7 mg)을 인용했다[4].',
    '[4] 원문은 \'섭취량 평가 필요\'가 아니라 \'may raise concerns\'와 EFSA TDI 7 mg/kg bw 인용')
d['name_en']='Seoul bird cherry'
changes.append({"where":"name_en","before":"Seoul bird cherry (bird cherry)","after":"Seoul bird cherry","why":"I1020 영어명은 Seoul bird cherry; bird cherry 는 기본종 이름이라 변종과 섞이지 않게 뺌"})
i=d['aliases'].index('European bird cherry'); d['aliases'][i]='European bird cherry(기본종 귀룽나무의 영어명)'
changes.append({"where":"aliases","before":"European bird cherry","after":"European bird cherry(기본종 귀룽나무의 영어명)","why":"[2]에서 P. padus(기본종)를 가리키는 이름이므로 변종 별명처럼 보이지 않게 표시"})
s1=d['sources'][0]; old=s1['title']
s1['title']=old.replace('Capulin열매 등) 대조','Capulin열매·세로티나벚나무열매(P. serotina) 등) 대조')
changes.append({"where":"sources[1].title","before":"…Capulin열매 등) 대조","after":"…Capulin열매·세로티나벚나무열매(P. serotina) 등) 대조","why":"본문에 새로 인용한 행 반영"})
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('/home/user/hfoodguide-wave3/docs/materials/prunus-padus/_review/changes.json','w'),ensure_ascii=False,indent=1)
# counts
n=sum(len([x for x in re.split(r'(?<=[.])\s+',s['body']) if x.strip()]) for s in d['sections'])
items=len(d['compounds'])+len(d['nutrients'])+len(d['assays'])+len(d['aliases'])+len(d['sources'])
print(n,items,len(changes))
