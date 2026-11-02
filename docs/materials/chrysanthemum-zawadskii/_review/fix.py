import json,sys
p='dossier.json'; d=json.load(open(p))
changes=[]
def sec(k): return next(s for s in d['sections'] if s['key']==k)
def rep(where,obj,key,old,new,why):
    v=obj[key]
    assert old in v,(where,old)
    obj[key]=v.replace(old,new); changes.append({"where":where,"before":old,"after":new,"why":why})
o=sec('overview')
rep('sections.overview',o,'body','사람 대상으로는 가벼운 무릎 골관절염 환자 121명의 12주 무작위 위약대조 시험이 있으며, 같은 시험 참가자의 유전형 분석에서는 골관절염 관련 유전자의 SNP 3개가 통증 점수 변화와 관련되었다[6].',
 '사람 대상으로는 가벼운 무릎 골관절염 환자 121명의 12주 무작위 위약대조 시험이 있으며[4], 같은 시험 참가자의 유전형 분석에서는 골관절염 관련 유전자의 SNP 3개가 통증 점수 변화와 관련되었다[6].','시험 자체의 출처 [4] 누락 — [6]은 유전형 분석 논문')
rep('sections.overview',o,'body','그 밖의 효과 보고는 대부분 세포·동물 실험이다[4, 9, 30].','그 밖의 효과 보고는 대부분 세포·동물 실험이다[5, 9, 30].','[4]는 인체시험이라 세포·동물 실험 근거가 아님 → 동물·세포 연구 [5]로 교체')
h=sec('history')
rep('sections.history',h,'body','같은 해 식약처 목록에 개별인정 원료 \'구절초추출물(기능성원료인정제2021-12호)\'이 올라 있어, 인정번호로 보아 2021년에 개별인정을 받은 것으로 읽힌다[2].',
 '식약처 「식품원료 목록」에는 개별인정 원료 \'구절초추출물(기능성원료인정제2021-12호)\'이 올라 있으며, 인정번호로 보아 2021년에 개별인정을 받은 것으로 읽힌다[2]. 인정 일자 원문은 확인하지 못함.','목록은 2026년 10월 내려받은 자료라 \'같은 해 올라 있다\'는 출처가 말하지 않음; 인정번호로부터의 추론임을 분명히 함')
b=sec('biology')
rep('sections.biology',b,'body','초기 플라이오세에 친링–다바산 일대에서 기원해 북쪽으로 퍼진 것으로','초기 플라이오세에 친링–다바산 일대에서 기원해 산줄기를 따라 서쪽과 북쪽으로 퍼져 중국 북부에 이른 것으로','[17] 초록은 \'west and northward\'')
rep('sections.biology',b,'body','꽃을 수증기 증류하면 정유가 0.12%(w/w) 얻어지고','꽃을 물 증류(Clevenger형 장치)하면 정유가 0.12%(w/w) 얻어지고','[22]는 hydro distillation(물 증류) — 수증기 증류가 아님')
pr=sec('processing')
rep('sections.processing',pr,'body','꽃은 에탄올 초음파 추출이나 수증기 증류로 정유를 얻는 연구에 쓰였다[9, 22].','꽃은 99% 에탄올 초음파 추출(60 °C, 4시간)이나 물 증류로 정유를 얻는 연구에 쓰였다[9, 22].','[22]는 물 증류; [9] 추출 조건 원문(99% 에탄올, 60 °C, 4시간)으로 보강')
g=sec('genetics')
rep('sections.genetics',g,'body','중국 시료(Dendranthema zawadskii Herbich)의 엽록체 게놈은 150,995 bp, 유전자 112개로 보고되었다[16].','중국 연구진이 보고한 Dendranthema zawadskii Herbich(중국 자생 17종 중 하나로 소개)의 엽록체 게놈은 150,995 bp, 유전자 112개(단백질 암호 79, rRNA 4, tRNA 29)로 보고되었다[16].','[16] 초록으로 확인·보강(시료 산지는 초록에 없어 \'중국 시료\'를 완화)')
rep('sections.genetics',g,'body','ITS2 바코드로는 C. zawadskii와 C. morifolium을 나누지 못해, 진위 확인에는 여러 표지를 함께 보는 것이 좋다[34, 13].','ITS2 바코드로는 C. zawadskii와 C. morifolium이 구별되지 않았고, 이 연구는 ITS2 염기서열에 2차 구조 정보를 더해 쓰자고 제안했다[34]. 한국 이배체 집단에서는 게놈 크기와 rDNA 위치가 구절초를 가르는 표지가 되었다[13].','\'여러 표지를 함께 보는 것이 좋다\'는 출처에 없는 권고 → 각 출처가 실제로 말한 내용으로 바꿈')
s=sec('safety')
rep('sections.safety',s,'body','제브라피시에 꽃 에탄올 추출물을 복강 주사로 3일간 주자 치사 독성이 나타났다는 보고가 있으나, 먹는 경우와 투여 경로가 다르다[9].',
 '제브라피시 연구에서는 꽃 에탄올 추출물을 복강 주사로 1회(0.25·0.5 μg/g 체중) 줄 때는 이상이 관찰되지 않았지만, 3일 연속 투여하자 치사 독성이 나타났다고 적었다(용량 미기재)[9]. 먹는 경우와 투여 경로가 다른 결과다[9].','[9] 전문: 1회 주사 시 이상 없음, 3일 투여 시 치사 독성(용량 미기재) — 조건을 원문대로 구체화')
C={c['name']:c for c in d['compounds']}
c=C['Linarin']; rep('compounds[Linarin].part',c,'part','전초·줄기·잎','전초','[5]는 건조 전초, [30]·[26]은 부위 미기재 — 줄기·잎에서 리나린을 정량한 출처 없음')
c=C['Chlorogenic acid']
rep('compounds[Chlorogenic acid].content_text',c,'content_text','70% 에탄올 추출물에서 HPLC로 동정·정량(정량값 표는 전문 본문에 없어 확인하지 못함)[11]; 전초 추출물 HPLC 5개 피크 중 하나[5]',
 '건조 구절초(부위 미기재) 70% 에탄올 추출물에서 HPLC로 동정·정량(정량값 표는 전문 본문에 없어 확인하지 못함)[11]; 전초 추출물 HPLC 5개 피크 중 하나[5]; 지상부 에탄올 추출물 340 nm HPLC에서 검출[10]','[11]은 부위를 밝히지 않음; 지상부 근거 [10] 추가')
c['source']=[11,5,10,12,8]
c['activity_ko']=c['activity_ko'].replace('보리 추출물과의 혼합물 연구에서 프로락틴 분비를 억제하는 구절초 쪽 성분으로 지목(세포·동물)[8]','보리 추출물과의 혼합물 연구에서 구절초 추출물 쪽의 프로락틴 분비 억제 성분으로 지목(뇌하수체 세포; 동물 실험은 혼합물로 수행)[8]')
changes.append({"where":"compounds[Chlorogenic acid].activity_ko","before":"…프로락틴 분비를 억제하는 구절초 쪽 성분으로 지목(세포·동물)[8]","after":"…(뇌하수체 세포; 동물 실험은 혼합물로 수행)[8]","why":"[8]의 동물 실험은 보리·구절초 혼합물 — 단독 결과처럼 읽히지 않게"})
c=C['3,5-Dicaffeoylquinic acid']
rep('compounds[3,5-DCQA].content_text',c,'content_text','70% 에탄올 추출물에서 HPLC로 동정·정량','건조 구절초(부위 미기재) 70% 에탄올 추출물에서 HPLC로 동정·정량','[11]은 부위 미기재')
rep('compounds[3,5-DCQA].activity_ko',c,'activity_ko','대식세포에서 ATP·요산결정에 의한 IL-1β 분비 감소(세포)[12]','생쥐 골수 유래 대식세포에서 ATP·니게리신·요산결정에 의한 IL-1β 분비 감소(세포)[12]','[12] 초록: ATP, nigericin, MSU')
c=C['Luteolin']
rep('compounds[Luteolin].content_text',c,'content_text','지상부 70% 에탄올 추출물에서 HPLC 정량(365 nm, 정량값 확인하지 못함)[11]; 꽃 에탄올 추출물의 주요 플라보노이드 3종 중 하나[9]',
 '건조 구절초(부위 미기재) 70% 에탄올 추출물에서 HPLC 정량(365 nm, 정량값 확인하지 못함)[11]; 꽃 에탄올 추출물의 주요 플라보노이드 3종 중 하나[9]; 지상부 에탄올 추출물 340 nm HPLC에서 검출[10]','[11]은 지상부라고 하지 않음; [10] 근거를 본문에 명시')
c=C['Quercetin']
rep('compounds[Quercetin].activity_ko',c,'activity_ko','DPPH IC50 9.24 μM·ABTS IC50 6.72 μM, 미세아교세포 염증 매개체 감소(세포)[9]','시판 퀘르세틴 표준품으로 DPPH IC50 9.24 μM·ABTS IC50 6.72 μM(시험관), 미세아교세포 IL-1β·iNOS 감소(세포)[9]; 꽃 추출물 자체의 IC50은 DPPH 186.04·ABTS 94.56 μg/mL[9]','[9] 전문: IC50은 구입한 순수 퀘르세틴 값 — 추출물 값과 구분')
c=C['Camphor']
rep('compounds[Camphor].content_text',c,'content_text','다른 꽃 정유 분석에서는 88성분 중 모노테르펜이 68.82%[23]','다른 꽃 정유 분석에서는 88성분이 동정되었고 모노테르펜류가 68.82%(캠퍼 개별 함량은 초록에 없음)[23]','[23] 초록에 캠퍼 개별 값 없음 — 오해 방지')
S=d['sources']
for n,old,new in [(9,'Exp Neurobiol 2026 (','Exp Neurobiol 2026;35(1):29-41 ('),(13,'BMC Plant Biol 2025 (','BMC Plant Biol 2025;25(1):506 ('),(16,'초록 확인)','초록 확인; 시료 산지는 초록에 없음)')]:
    s_=S[n-1]; assert s_['n']==n and old in s_['title']; s_['title']=s_['title'].replace(old,new); changes.append({"where":f"sources[{n}].title","before":old,"after":new,"why":"PubMed 서지와 맞춤"})
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(changes,open('_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
