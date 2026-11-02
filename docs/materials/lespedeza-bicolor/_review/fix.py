import json,sys
P='/home/user/hfoodguide-wave3/docs/materials/lespedeza-bicolor/dossier.json'
d=json.load(open(P))
changes=[]
def sec(k): return next(s for s in d['sections'] if s['key']==k)
def rep(where,obj,key,old,new,why):
    v=obj[key]
    assert v.count(old)==1,(where,old)
    obj[key]=v.replace(old,new); changes.append({"where":where,"before":old,"after":new,"why":why})
o=sec('overview')
rep('sections.overview',o,'body','전통 약용식물로 소개한다[1, 3, 7].','전통 약용식물로 소개한다[3, 7].','[1](식품원료 목록)은 전통 약용 이용을 말하지 않음')
rep('sections.overview',o,'body','뿌리·줄기껍질 폴리페놀은 전립선암 세포 증식 억제, 신경세포 산화 손상 보호, SARS-CoV 파파인 유사 단백분해효소 억제를 세포·효소 시험에서 보였다[18, 17, 29].',
 '뿌리껍질 폴리페놀은 전립선암 세포 증식 억제[18]와 SARS-CoV 파파인 유사 단백분해효소 억제[29]를, 싸리에서 분리한 폴리페놀은 신경세포 산화 손상 보호[17]를 세포·효소 시험에서 보였다.',
 '[17] 초록은 분리 부위를 밝히지 않아 뿌리·줄기껍질로 묶을 수 없음; [18]·[29]는 뿌리껍질')
h=sec('history')
rep('sections.history',h,'body','중국에서는 싸리꿀이 귀하고 값이 높아 다른 꿀을 섞거나 대신한 위조품이 유통된다고 보고되었다[8].',
 '싸리꿀은 귀하고 값이 높아 시장에 다른 꿀을 섞거나 대신한 위조품이 나돈다고 보고되었다[8].','[8] 초록은 위조품 유통 지역을 중국으로 한정하지 않음(중국은 비교 꿀의 판매지)')
r=sec('related_species')
rep('sections.related_species',r,'body','한국 야생 싸리속 4종','야생 싸리속 4종','[23] 초록에 시료 채집국이 적혀 있지 않음')
g=sec('genetics')
rep('sections.genetics',g,'body','한국 야생 싸리속 39개 시료','야생 싸리속 4종 39개 시료','[23] 초록에 시료 채집국이 적혀 있지 않음')
c=sec('cultivation')
rep('sections.cultivation',c,'body','싸리는 척박한 산성 토양에 잘 견디는 콩과 관목이라 사료·토양 보전용으로 소개된다[22].','싸리는 척박한 산성 토양에서 잘 자라는 콩과 사료 식물로 소개된다[22].','[22]는 사료(forage) 식물이라고만 하고 토양 보전 용도는 말하지 않음')
cp={x['name']:x for x in d['compounds']}
rep('compounds.Rutin.activity_ko',cp['Rutin'],'activity_ko','AGEs 생성 억제 성분 후보로 정량됨;','추출물 표준화를 위해 HPLC로 정량한 6개 성분 중 하나(AGEs 억제 성분으로 지목된 것은 제니스테인·퀘르세틴·나린긴);','[3]·[7]은 루틴을 AGEs 억제 성분으로 지목하지 않음')
rep('compounds.Luteolin.activity_ko',cp['Luteolin'],'activity_ko','항산화·항염 플라보노이드; 추출물 표준화 성분[3]','추출물 표준화를 위해 HPLC로 정량한 성분(6개 중 함량 최다)[3]','[3]은 루테올린의 항산화·항염 활성을 따로 보이지 않음')
rep('compounds.Vitexin.content_text',cp['Vitexin'],'content_text','분획의 주성분으로 동정','분획의 주요 성분 중 하나로 LC-MS 동정','[11]: "one of the major components"')
x=cp['1-Methoxyerythrabyssin II']
rep('compounds.1-Methoxyerythrabyssin II.activity_ko',x,'activity_ko','백혈병 세포 증식 억제[14, 15]','백혈병 세포(Jurkat) 증식 억제·자가포식 유도(세포)[14, 34]','[15] 초록은 이 화합물의 항증식 활성을 특정하지 않음; 단일 화합물 백혈병 세포 시험은 PMID 37459859')
x['source']=[14,15,34]
x=cp['2-Geranyl-1-methoxyerythrabyssin II']
rep('compounds.2-Geranyl-1-methoxyerythrabyssin II.part',x,'part','뿌리(싸리에서 분리)','싸리에서 분리(부위는 초록에 적혀 있지 않음)','[31] 초록은 분리 부위를 밝히지 않음')
a=d['assays'][1]['conditions']
rep('assays[1].conditions.instrument',a,'instrument','Agilent UHPLC + 삼중사중극자 질량분석기(ESI); 동정은 Agilent 1290 + Q-TOF','UHPLC-삼중사중극자 질량분석기(ESI, 본체 제조사 표기 없음; 칼럼은 Agilent); 비표적 동정은 1290 HPLC + Agilent Q-TOF','[9] 전문은 QQQ 장비 제조사를 적지 않음')
S={s['n']:s for s in d['sources']}
rep('sources[12].title',S[12],'title','2004;75(1):95-7.','2004;75(1):96-8.','PubMed 서지: 75(1):96-8')
rep('sources[10].title',S[10],'title','Inhibits Ferroptosis in DSS-Induced','Inhibits Ferroptosis by Nrf2/HO-1 Pathway in DSS-Induced','PubMed 원제목에 경로명이 들어 있음')
d['sources'].append({"n":34,"title":"1-Methoxyerythrabyssin II Induces Autophagy in Leukemia Cells via PI3K/Akt/mTOR Pathways. Planta Med. 2023;89(13):1204-1214. doi:10.1055/a-2114-0980","url":"https://pubmed.ncbi.nlm.nih.gov/37459859/","publisher":"Planta Medica (PubMed)","accessed":"2026-11-02"})
changes.append({"where":"sources[34]","before":"","after":"PMID 37459859 추가","why":"1-메톡시에리트라비신 II 백혈병 세포 활성의 1차 출처"})
json.dump(d,open(P,'w'),ensure_ascii=False,indent=2)
json.dump(changes,open(P.replace('dossier.json','_review/changes.json'),'w'),ensure_ascii=False,indent=1)
print(len(changes))
