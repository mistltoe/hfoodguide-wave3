import json,re
P='/home/user/hfoodguide-wave3/docs/materials/ulmus-macrocarpa/dossier.json'
d=json.load(open(P))
S={s['key']:s for s in d['sections']}
def rep(key,old,new):
    b=S[key]['body']; assert b.count(old)==1,(key,old); S[key]['body']=b.replace(old,new)

# overview: add trial results
rep('overview','사람 대상 무작위 시험은 하루 500 mg 추출물을 4–12주 먹인 3건이 있다[6, 7, 8].',
 '사람 대상 무작위 시험은 하루 500 mg 추출물을 4–12주 먹인 3건이 있다[6, 7, 8]. 고LDL 콜레스테롤 성인 80명 시험에서는 12주 뒤 LDL 콜레스테롤이 위약보다 18.1 mg/dL 더 낮았고[6], 건강한 성인 58명의 4주 시험에서는 NK 세포 활성에 위약과 차이가 없었으며[7], 장내세균 시험에서는 종 풍부도·다양도에 유의한 차이가 없었다[8].')
# history: soften 1990
rep('history','현대 약리 연구는 1990년 중국 학술지의 궤양성 대장염 36례 보고에서 시작되었다[9, 21].',
 '한 논문은 1990년 중국 학술지의 궤양성 대장염 36례 보고를 이 종의 첫 현대 약리 연구로 꼽았다[9, 21].')
# related_species: E7A detection precision + wound study species fix
rep('related_species','다른 한 종은 5.54 mg/g, 또 다른 한 종에서는 검출되지 않았다[4].',
 '질량분석으로 E7A가 확인된 것은 왕느릅나무와 다른 한 종(5.54 mg/g)뿐이었고, 210 nm 피크는 한 종에서 나타나지 않았다[4].')
rep('related_species','비술나무 뿌리껍질 가루를 생쥐 상처에 바른 실험에서는 비술나무가 왕느릅나무보다 상처 회복 효과가 컸다는 보고가 있어, 근연종 연구 결과를 이 종에 그대로 옮겨서는 안 된다[29].',
 '참느릅나무(U. parvifolia) 뿌리껍질 가루를 생쥐 상처에 바른 실험에서는 참느릅나무 가루가 상처 크기를 유의하게 줄였으나 비교군으로 쓴 다른 느릅나무속 가루(논문 약칭 UM)는 유의한 차이가 없었다는 보고가 있어, 근연종 연구 결과를 이 종에 그대로 옮겨서는 안 된다[29].')
# processing: drop retracted [23]
rep('processing','이 조합은 위염·위궤양 동물 모델과 헬리코박터 감염 생쥐에서 연구되었다[22, 23, 24].',
 '산딸기와 왕느릅나무 추출물의 병용, 그리고 세 원료를 섞은 표준화 추출물은 헬리코박터 균주와 감염 생쥐에서 연구되었다[22, 24].')
# safety: group sizes
rep('safety','사람 시험에서 고LDL 콜레스테롤 성인 80명이 열수 추출물 하루 500 mg을 12주 먹었을 때',
 '사람 시험에서 고LDL 콜레스테롤 성인 80명(섭취군 40명)을 무작위로 나눠 열수 추출물 하루 500 mg 또는 위약을 12주 먹였을 때')
rep('safety','건강한 성인 58명의 4주 시험(하루 500 mg)에서는','건강한 성인 58명(섭취군 29명)의 4주 시험(하루 500 mg)에서는')
rep('safety','장내세균 시험(하루 500 mg, 4주)도 있었다[8].','장내세균 시험(하루 500 mg, 4주)은 초록에 이상반응 결과를 적지 않았다[8].')
# renumber 24..29 -> 23..28 in bodies & lists (after removing 23)
def renum_text(t):
    def f(m):
        nums=[int(x) for x in re.split(r',\s*',m.group(1))]
        out=[]
        for n in nums:
            if n==23: continue
            out.append(n-1 if n>23 else n)
        return '['+', '.join(map(str,out))+']'
    return re.sub(r'\[(\d+(?:,\s*\d+)*)\]',f,t)
for s in d['sections']:
    s['body']=renum_text(s['body'])

# compounds/assays source lists & text
for c in d['compounds']:
    c['activity_ko']=c['activity_ko'].replace('(쥐 골수세포, 세포)','(생쥐 골수세포, 세포)')
    for k in ('content_text','activity_ko'): c[k]=renum_text(c[k])
    c['source']=[n-1 if n>23 else n for n in c['source'] if n!=23]
for a in d['assays']:
    a['source']=[n-1 if n>23 else n for n in a['source'] if n!=23]
    a['content']=renum_text(a['content']); a['rationale']=renum_text(a['rationale'])
src=[s for s in d['sources'] if s['n']!=23]
for s in src:
    if s['n']>23: s['n']-=1
for s in src:
    if s['n']==2:
        s['title']=s['title'].replace("느릅나무(U. davidiana var. japonica; 껍질·줄기껍질·농축액 '제한적사용가능부위 : 나무껍질' 제한적사용,","느릅나무(U. davidiana var. japonica; 껍질·줄기껍질·농축액 '제한적사용가능부위 : 나무껍질' 제한적사용, 느릅나무분말 '사용가능부위 : 잎, 열매 / 제한적사용부위 : 나무껍질' 제한적사용,")
    if s['n']==28:
        assert 'Ulmus pumila' in s['title']
        s['title']="Ulmus parvifolia Accelerates Skin Wound Healing by Regulating the Expression of MMPs and TGF-β. J Clin Med 2019;9(1):59, doi:10.3390/jcm9010059 (PMID 31887972, PMC7019489; 전문 확인 — 대상 종은 참느릅나무 U. parvifolia, 비교군 학명은 약칭 UM만 확인)"
        s['url']='https://pmc.ncbi.nlm.nih.gov/articles/PMC7019489/'
        s['publisher']='MDPI / PubMed Central'
    if s['n']==8:
        pass
d['sources']=src
assert [s['n'] for s in src]==list(range(1,len(src)+1))
json.dump(d,open(P,'w'),ensure_ascii=False,indent=1)
print('ok')
