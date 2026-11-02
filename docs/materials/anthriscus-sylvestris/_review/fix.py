import json,re,sys
P='/home/user/hfoodguide-wave3/docs/materials/anthriscus-sylvestris/'
d=json.load(open(P+'dossier.json'))
changes=[]
def sec(k): return next(s for s in d['sections'] if s['key']==k)
def rep(k,old,new,why):
    s=sec(k); assert old in s['body'],(k,old); s['body']=s['body'].replace(old,new); changes.append({"where":f"sections.{k}","before":old,"after":new,"why":why})
rep('biology','β-펠란드렌(39%)·β-미르센(17%)·사비넨(6.2%)이 주성분이다[10].','β-펠란드렌(38.8%)·β-미르센(16.7%)·사비넨(6.2%)이 주성분이다[3][10].',
    "[10] 초록은 β-펠란드렌을 잎·뿌리 합쳐 39–45%로만 적음; 잎 38.8%·뿌리 45.5% 구분은 [3] 전문에 있어 출처 추가·원문 값으로 맞춤")
rep('related_species','전호속(Anthriscus)에는 POWO 기준으로 세계에 14종이 인정되며, 유럽에는 10종이 자란다고 정리되어 있다[4].','전호속(Anthriscus)에는 POWO 기준으로 세계에 14종이 인정되며, Euro+Med 기준으로 유럽에는 10종이 자란다고 정리되어 있다[4].',
    "[4]에서 유럽 10종은 POWO가 아니라 Euro+Med(2023) 기준")
rep('related_species',"북아메리카에서는 '야생당근'이라 여기고 캐 먹은 산형과 식물에서 독미나리류 독소(시큐톡신)가 검출된 사망 사례가 보고되었다[24].","캐나다에서는 '야생당근'이라 여기고 캐 먹은 식물(정확히 동정되지 않음)에서 독미나리류 독소(시큐톡신)가 검출된 사망 사례가 보고되었다[24].",
    "[24] 초록: 섭취 식물은 확정 동정되지 않았고 시큐톡신만 검출됨; 사례 지역은 캐나다(서스캐처원)")
rep('related_species','중국 약재 시장에서는 전호 뿌리가 인삼 위품으로 유통되어 이를 분광법으로 감별하는 연구가 있었다[30].','중국에서는 전호를 인삼의 위품(가짜) 시료로 보고 라만 분광법으로 인삼과 감별하는 연구가 있었다[30].',
    "[30] 초록은 전호를 인삼 위품 시료로 다룬 감별 연구일 뿐, '시장 유통'을 말하지 않음")
rep('history','세르비아에서는 가루를 샐러드드레싱 향신료로,',"세르비아에서는 'wild parsley' 가루를 샐러드드레싱 향신료로,",
    "[4]는 'powdered wild parsley'라고만 적어 전호로 특정되지 않음을 드러냄")
rep('processing','경증 무릎 골관절염 환자에게 잎 물 추출물을 먹인 임상시험이 등록되어 있다는 내용은 검색 요약으로만 확인했다[29].','경증 무릎 골관절염 환자에게 잎 추출물을 먹인 임상시험(NCT06535204)이 ClinicalTrials.gov에 등록되어 있으나, 이 환경에서 등록 원문이 열리지 않아 검색 결과로만 확인했고 결과를 실은 동료심사 논문은 확인하지 못함[29].',
    "등록 원문 미확인·'물 추출물' 여부 확인 불가 — 과장 없이 확인 범위를 명시")
rep('safety','야생당근으로 알고 먹은 식물로 14세 소년이 숨진 독미나리류 중독 사례도 있다[24].','야생당근으로 알고 먹은 식물로 14세 소년이 숨진, 독미나리류(Cicuta) 중독으로 추정되는 사례도 있다(식물은 확정 동정되지 않음)[24].',
    "[24] 제목·초록이 'apparent' water hemlock poisoning이며 식물 동정 실패")
rep('safety','전호를 독당근·독미나리로 혼동한 국내 사례나 공공기관의 전호 구별 안내는 확인하지 못함.','두 사례 보고는 전호를 직접 언급하지 않으며, 전호를 독당근·독미나리로 혼동한 국내 사례나 공공기관의 전호 구별 안내는 확인하지 못함.',
    "[23][24]에 전호 언급이 없음을 밝혀 근연 유독종 자료가 전호 자료로 읽히지 않게 함")
# compounds
C={c['name']:c for c in d['compounds']}
def cf(name,field,new,why):
    old=C[name][field]; C[name][field]=new; changes.append({"where":f"compounds[{name}].{field}","before":old,"after":new,"why":why})
cf('beta-Phellandrene','content_text','잎 정유 38.8%, 뿌리 정유 45.5%(신선 재료 수증기 증류)[3]; 잎·뿌리 정유 39–45%[10]',"[10] 초록은 39–45%만 제시, 부위별 값은 [3]")
C['beta-Phellandrene']['source']=[3,10]
cf('beta-Myrcene','content_text','잎 정유 17%[10](16.7%[3])',"[3] 전문 값 병기")
C['beta-Myrcene']['source']=[3,10]
cf('Luteolin 7-glucoside','content_text','반쯤 시든 꽃과 줄기에서 생체 1 kg당 0.124 g 분리[3]',"[3] 원문은 partially wilted flowers and stems")
cf('Deoxypodophyllotoxin','activity_ko','COX-2·5-LOX 이중 억제(생쥐 비만세포 실험)[27]; 고지방식 생쥐에서 간 지방 축적 감소(동물 실험)[26]; 사람 간 마이크로솜에서 CYP2C9·3A4 억제[13]',"세포·동물 결과임을 명시(과장 방지)")
cf('Podophyllotoxone','activity_ko','뿌리의 주요 리그난 가운데 하나로, 이 종에서는 [11]에서 처음 보고됨[11]; 추출물에서 불안정해 냉동·차광 보관 필요[5]',"[11] 초록: 주요 성분이며 이 종에서 처음 보고 — 문장 모호성 정리")
# assays: remove [8] item (not quantified)
old=[a for a in d['assays'] if a['source']==[8]]
d['assays']=[a for a in d['assays'] if a['source']!=[8]]
changes.append({"where":"assays[Luteolin 7-glucoside]","before":"[8] 지상부 루테올린-7-O-글루코사이드·클로로겐산 HPLC 항목","after":"(삭제)","why":"[8] 초록은 두 성분이 항산화 분획의 주성분이라고만 하고 정량값·분석 조건이 없음 — 정량 논문 아님"})
json.dump(d,open(P+'dossier.json','w'),ensure_ascii=False,indent=1)
json.dump(changes,open(P+'_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(changes))
