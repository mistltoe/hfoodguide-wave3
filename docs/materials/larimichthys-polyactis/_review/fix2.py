import json
p='dossier.json'; d=json.load(open(p)); ch=json.load(open('_review/changes.json'))
ch=[c for c in ch if c['where']!='sections.genetics']
def sec(k): return next(s for s in d['sections'] if s['key']==k)
def rep(obj,key,old,new,where,why):
    assert old in obj[key], (where,old)
    obj[key]=obj[key].replace(old,new); ch.append({"where":where,"before":old,"after":new,"why":why})
g=sec('genetics'); g['body']=g['body'].replace('97.90%(663.13 Mb)','97.89%(663.13 Mb)')  # 1차 수정 되돌림: [2] 본문은 97.89%
rep(g,'body','여덟 조직의 전사체에서 93,990개 유전자와 12,539개 단순반복서열이','여덟 조직의 전사체에서 비중복 전사체(unigene) 93,990개와 단순반복서열 12,539개가','sections.genetics','[12] 초록: 93,990은 유전자 수가 아니라 non-redundant transcripts(unigenes)')
rep(sec('biology'),'body','21쌍의 단부 염색체(기본수 54)','21쌍의 단부 염색체(염색체 팔 수 FN=54)','sections.biology','[8] 초록의 FN은 fundamental number(팔 수); 제주 시료')
rep(sec('processing'),'body','목포에서 산 조기를 10% 천일염 용액에','목포의 수산식품 업체에서 산 냉동 조기(80–90 g)를 해동해 10% 천일염 용액에','sections.processing','[4] Methods 2.1: 냉동품을 4 °C에서 해동, 개체 80–90 g')
rep(sec('safety'),'body','조기의 기생충 감염률이 30.28%였다[24]','조기(초록 표기 little yellow croaker)의 기생충 유충 감염률이 30.28%였다[24]','sections.safety','[24] 초록: 해산어 유충 감염 조사에서 little yellow croaker 30.28%')
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
json.dump(ch,open('_review/changes.json','w'),ensure_ascii=False,indent=1)
r=json.load(open('review.json'))
r['changes']=ch; r['fixed']=len(ch); r['unverifiable']=0
r['unverifiable_notes']=["[2]·[3]·[4]·[5] 전문과 [7]·[8]·[10]·[11]·[12]·[16]·[24]·[33] 초록을 PubMed 도구로 다시 열어 모두 대조함(재요청 시 429 없음). 1차 검토에서 [2] 배치율을 초록 값 97.90%로 바꿨으나 본문이 97.89%여서 되돌림",
"[13]·[14]·[15]·[17]·[19]–[23]·[25]–[31]·[34]는 초록, [6]·[9]·[18]·[32]도 초록으로 확인; [1]은 로컬 I1020 원자료로 확인. Europe PMC는 열지 않음"]
r['verified']=r['checked_sentences']+r['checked_items']-r['fixed']
json.dump(r,open('review.json','w'),ensure_ascii=False,indent=1)
print(r['checked_sentences'],r['checked_items'],r['verified'],r['fixed'])
