import json
p='/home/user/hfoodguide-wave3/docs/materials/coprinus-cinereus/dossier.json'
d=json.load(open(p))
ch=[]
S={s['key']:s for s in d['sections']}
def rep(where,obj,key,old,new,why):
    assert old in obj[key],(where,old)
    obj[key]=obj[key].replace(old,new); ch.append({"where":where,"before":old,"after":new,"why":why})
rep('sections.overview',S['overview'],'body','재먹물버섯은 먹물버섯 무리에 속하는 작은 버섯으로,','재먹물버섯은 넓은 뜻의 먹물버섯속(Coprinus)에 들던 버섯으로,','"작은 버섯"은 인용 출처가 크기를 말하지 않음')
rep('sections.history',S['history'],'body',"식품의약품안전처 목록에 올린 학명은 Schaeffer가 기재하고 Gray가 Coprinus 속으로 옮긴 'Coprinus cinereus (Schaeff.) Gray'이다[1].","식품의약품안전처 목록에 올린 학명은 'Coprinus cinereus (Schaeff.) Gray'이다[1].","명명 경위는 [1]이 말하지 않음(목록은 학명만 실음)")
rep('sections.history',S['history'],'body',"그 뒤 이 종은 Coprinopsis cinerea로 불리게 되었고,","그 뒤 2001년 분류 논문(Taxon 50권)에서 이 종은 Coprinopsis cinerea (Schaeff.) Redhead, Vilgalys & Moncalvo로 옮겨졌고(뉴질랜드 생물명 등록부 항목, 웹 검색 요약으로만 확인)[33],","현 학명 이전의 근거 출처가 없었음 — 명명 등록부 항목을 추가(웹 검색 요약으로만 확인)")
rep('sections.biology',S['biology'],'body','갓에서 키티나아제와 β-1,3-글루칸 분해효소들이 함께 세포벽을 분해하는 것으로 보고되었다[19, 20].','갓에서 정제한 키티나아제와 β-1,3-글루칸 분해효소들이 함께 세포벽을 분해할 것으로 제안되었다[19, 20].','[19][20] 초록은 "may promote"·"may act synergistically"로 추정으로 씀')
rep('sections.cultivation',S['cultivation'],'body','사이잘 잎 찌꺼기와 사이잘 줄기를 섞은 기질에','사이잘 폐기물 집하장에서 채집한 자실체를 조직배양해 얻은 균주(동정 방법은 논문에 적혀 있지 않음)를, 퇴비화한 사이잘 잎 찌꺼기와 사이잘 밑동(boles)을 섞은 기질에','[7] 전문: 균주는 야생 채집 자실체 조직배양, 기질은 composted sisal leaf residues·sisal boles; 동정 근거 미기재를 밝힘')
rep('sections.cultivation',S['cultivation'],'body','종균은 수수 낟알로 만들어 습중량 기준 6%를 접종했고,','종균은 수수 낟알로 만든 14일 된 것을 습중량 기준 6% 접종했고,','[7] 전문 확인(14-day old spawn)')
rep('sections.cultivation',S['cultivation'],'body','발이 단계는 26.5 °C·상대습도','발이 단계는 26.5 ± 0.05 °C·상대습도','[7] 전문 값')
rep('sections.processing',S['processing'],'body','사이잘 폐기물 재배에서는 균사 생장기에 락카아제 활성이 가장 높았고(최대 39.45 ± 12.05 U/g, 수확 후 배지 습중량),','사이잘 폐기물 재배에서는 균사 생장기에 락카아제 활성이 가장 높았고(최대 39.45 ± 12.05 U/g 배지 습중량, 소똥 10% 첨가 사이잘 잎 찌꺼기 배지에서 균사가 배지를 다 채운 10일째),','[7] 전문: 최대값은 수확 후가 아니라 10일째(full colonization) 측정; 단위는 U g⁻¹ SMS wet wt.')
rep('sections.safety',S['safety'],'body','이는 환경 곰팡이로서 호흡기로 들어간 감염 사례이며, 버섯을 먹어서 생긴 것은 아니다[24, 25].','보고된 사례는 폐·호흡기 검체에서 나온 감염과 집락이며, 두 문헌에서 버섯 섭취와 관련된 사례는 확인하지 못함[24, 25].','[24][25] 초록은 감염 경로를 단정하지 않음 — 과장 없이 표현')
rep('sections.safety',S['safety'],'body','2026년에는 급성 골수성 백혈병 환자의 호중구 감소기에 생긴 폐 감염 사례가 보고되었다[25].','2026년에는 급성 골수성 백혈병 환자가 항진균제 예방 투여 중 호중구 감소기에 생긴 폐 감염(돌파 감염) 사례가 보고되었다[25].','[25] 초록: breakthrough infection during antifungal prophylaxis')
C={c['name']:c for c in d['compounds']}
rep('compounds[14-Hydroxy-5-desoxy-2S,3S,9R-illudosin].content_text',C['14-Hydroxy-5-desoxy-2S,3S,9R-illudosin'],'content_text','4,5-디하이드로-5-데옥시아르밀롤','4,5-데하이드로-5-데옥시아르밀롤','[13] 초록은 4,5-dehydro(디하이드로 dihydro 아님)')
rep('compounds[Coprinoferrin].part',C['Coprinoferrin'],'part','균사(laeA 결손 균주에서 증가)','배양 균주(laeA 결손 균주에서 생산 증가; 부위는 초록에 표기 없음)','[15] 초록은 균사 부위를 말하지 않음')
rep('compounds[CCL2 lectin].activity_ko',C['CCL2 lectin'],'activity_ko','(실험동물·무척추동물)','(선충·초파리 실험)','[17]: C. elegans·D. melanogaster만 시험')
a=d['assays'][0]['conditions']
rep('assays[0].conditions.standard',a,'standard','; 용매 추출법에서는 내부표준 노닐 아세테이트 1 μg/mL','','PMC 전문 텍스트에 노닐 아세테이트·1 μg/mL 없음(내부표준 사용만 언급)')
for s in d['sources']:
    if s['n']==2:
        old=s['title']; s['title']=old.replace("좀밀먹물버섯(Coprinus plicatilis, 이상 사용불가)","좀밀먹물버섯(Coprinus plicatilis — 원자료 표기 'COPRINUS PLICATIOLLIS FR.', 이상 사용불가)")
        ch.append({"where":"sources[2].title","before":old,"after":s['title'],"why":"로컬 원자료 학명 표기 그대로 병기"})
    if s['n']==5:
        old=s['title']; s['title']=old.replace('(초록; PMC 전문 본문 없음)','(초록; PMC98996)')
        ch.append({"where":"sources[5].title","before":old,"after":s['title'],"why":"PubMed 메타데이터에 PMC98996 있음"})
d['sources'].append({"n":33,"title":"New Zealand Organisms Register(NZOR) 학명 항목 — Coprinopsis cinerea (Schaeff.) Redhead, Vilgalys & Moncalvo, Taxon 50(1): 227 (2001), 기본명 Agaricus cinereus Schaeff. (웹 검색 요약으로만 확인, 페이지 직접 열람 안 함)","url":"https://nzor.org.nz/names/7F968A30-5AB0-4CBB-B409-55932A27A2F5","publisher":"Landcare Research(NZOR)","accessed":"2026-11-02"})
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(ch,open('/home/user/hfoodguide-wave3/docs/materials/coprinus-cinereus/_review/changes.json','w'),ensure_ascii=False,indent=1)
print(len(ch))
