import json
P="https://pubmed.ncbi.nlm.nih.gov/"
A="2026-11-02"
def pm(n,title,pmid,journal,extra=""):
    return {"n":n,"title":f"{title} ({journal}; PMID {pmid}{extra})","url":P+pmid+"/","publisher":f"{journal.split(',')[0]} (PubMed)","accessed":A}
S=[
 {"n":1,"title":"식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 재먹물버섯·재먹물버섯어린자실체(Coprinus cinereus (Schaeff.) Gray), 사용가능, '사용가능부위 : 자실체' (로컬 원자료 I1020_20261013.json 대조)","url":"https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020","publisher":"식품의약품안전처","accessed":"2026-10-13"},
 {"n":2,"title":"식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 이름이 가까운 항목: 먹물버섯·먹물버섯어린자실체·먹물버섯추출물(Coprinus comatus, 사용가능), 노랑갈색먹물버섯자실체(Coprinellus radians / Coprinus radians, 사용가능), 갈색먹물버섯(Coprinus micaceus)·좀밀먹물버섯(Coprinus plicatilis, 이상 사용불가) (로컬 원자료 대조)","url":"https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020","publisher":"식품의약품안전처","accessed":"2026-10-13"},
 {"n":3,"title":"통계청 「농작물생산조사」·농림축산식품부 「특용작물 생산실적」(1995–2024) 로컬 파싱본(docs/stats/regional_crops.csv·special_crops_annual.csv·special_crops_2024.csv) — '재먹물버섯'·'먹물버섯' 품목 없음 확인('버섯-기타'·'버섯류'로만 집계)","url":"https://www.mafra.go.kr","publisher":"농림축산식품부·통계청","accessed":A},
 pm(4,"Insights into evolution of multicellular fungi from the assembled chromosomes of the mushroom Coprinopsis cinerea (Coprinus cinereus) (초록)","20547848","Proc Natl Acad Sci USA, 2010"),
 pm(5,"Life history and developmental processes in the basidiomycete Coprinus cinereus (초록; PMC 전문 본문 없음)","10839819","Microbiol Mol Biol Rev, 2000"),
 pm(6,"Phylogenetic relationships in the mushroom genus Coprinus and dark-spored allies based on sequence data from the nuclear gene coding for the large ribosomal subunit RNA (초록)","10508535","Mol Phylogenet Evol, 1999"),
 pm(7,"Production of oxidative and hydrolytic enzymes by Coprinus cinereus (Schaeff.) Gray from sisal wastes supplemented with cow dung manure (PMC4668298 전문)","26664748","Biotechnol Res Int, 2015"),
 pm(8,"Structures and synthesis of hitoyopodins: bioactive aromatic sesquiterpenoids produced by the mushroom Coprinopsis cinerea (초록)","30234313","Org Lett, 2018"),
 pm(9,"Hitoyol A and B, two norsesquiterpenoids from the basidiomycete Coprinopsis cinerea (초록)","28726419","Org Lett, 2017"),
 pm(10,"Bacteria-induced production of the antibacterial sesquiterpene lagopodin B in Coprinopsis cinerea (초록)","31087720","Mol Microbiol, 2019"),
 pm(11,"Biosynthesis of lagopodins in mushroom involves a complex network of oxidation reactions (초록)","30556075","Org Biomol Chem, 2019"),
 pm(12,"Antineoplastic agents. 556. Isolation and structure of coprinastatin 1 from Coprinus cinereus (초록)","19919060","J Nat Prod, 2010"),
 pm(13,"Antineoplastic agents 582. Part 1: Isolation and structure of a cyclobutane-type sesquiterpene cancer cell growth inhibitor from Coprinus cinereus (Coprinaceae) (초록)","20598551","Bioorg Med Chem, 2010"),
 pm(14,"Copsin, a novel peptide-based fungal antibiotic interfering with the peptidoglycan synthesis (초록)","25342741","J Biol Chem, 2014"),
 pm(15,"Genomic mushroom hunting decrypts coprinoferrin, a siderophore secondary metabolite vital to fungal cell development (초록)","31496254","Org Lett, 2019"),
 pm(16,"Coprinopsis cinerea dioxygenase is an oxygenase forming 10(S)-hydroperoxide of linoleic acid, essential for mushroom alcohol, 1-octen-3-ol, synthesis (PMC9579011 전문)","36122804","J Biol Chem, 2022"),
 pm(17,"Plasticity of the β-trefoil protein fold in the recognition and control of invertebrate predators and parasites by a fungal defence system (초록)","22615566","PLoS Pathog, 2012"),
 pm(18,"Fruiting body development in Coprinus cinereus: regulated expression of two galectins secreted by a non-classical pathway (초록)","10931889","Microbiology, 2000"),
 pm(19,"Purification, characterization and physiological significance of a chitinase from the pilei of Coprinopsis cinerea fruiting bodies (초록)","27190145","FEMS Microbiol Lett, 2016"),
 pm(20,"Purification, characterization and synergism in autolysis of a group of 1,3-β-glucan hydrolases from the pilei of Coprinopsis cinerea fruiting bodies (초록)","26199012","Microbiology, 2015"),
 pm(21,"The exp2 gene, which encodes a protein with two zinc finger domains, regulates cap expansion and autolysis in Coprinopsis cinerea (초록)","38554651","Microbiol Res, 2024"),
 pm(22,"Forms of chitin-polysaccharide cross-linking in the Coprinopsis cinerea stipe cell wall (초록)","40912786","Carbohydr Polym, 2025"),
 pm(23,"Genome editing in the mushroom-forming basidiomycete Coprinopsis cinerea, optimized by a high-throughput transformation system (초록)","28455526","Sci Rep, 2017"),
 pm(24,"Hormographiella aspergillata: an emerging basidiomycete in the clinical setting? A case report and literature review (초록)","33308180","BMC Infect Dis, 2020"),
 pm(25,"Breakthrough invasive pulmonary Coprinopsis cinerea (Hormographiella aspergillata) infection successfully managed with antifungal therapy and surgical resection enabling cord blood transplantation (초록)","41895473","J Infect Chemother, 2026"),
 pm(26,"On the disulfiram-like effect of coprine, the pharmacologically active principle of Coprinus atramentarius (초록)","350009","Acta Pharmacol Toxicol, 1978"),
 pm(27,"Effects on rat liver acetaldehyde dehydrogenases in vitro and in vivo by coprine, the disulfiram-like constituent of Coprinus atramentarius (초록)","577107","Acta Pharmacol Toxicol, 1977"),
 pm(28,"Lcc1 and Lcc5 are the main laccases secreted in liquid cultures of Coprinopsis cinerea strains (초록)","23340718","Antonie van Leeuwenhoek, 2013"),
 pm(29,"Inactivation of Coprinus cinereus peroxidase by 4-chloroaniline during turnover: comparison with horseradish peroxidase and bovine lactoperoxidase (초록)","10654839","Chem Biol Interact, 1999"),
 pm(30,"Biomechanics of stipe elongation in the basidiomycete Coprinopsis cinerea (초록)","16018318","Mycol Res, 2005"),
 pm(31,"Identification of a novel nematotoxic protein by challenging the model mushroom Coprinopsis cinerea with a fungivorous nematode (초록)","26585824","G3, 2015"),
 pm(32,"Induction of antibacterial proteins and peptides in the coprophilous mushroom Coprinopsis cinerea in response to bacteria (초록)","30301946","ISME J, 2018"),
]
sec=[
("overview","한눈에 보기","""재먹물버섯은 먹물버섯 무리에 속하는 작은 버섯으로, 식품의약품안전처 「식품원료 목록」에는 학명 'Coprinus cinereus (Schaeff.) Gray'로 '재먹물버섯'과 '재먹물버섯어린자실체' 두 항목이 올라 있다[1]. 두 항목 모두 상태가 '사용가능'이고 사용 조건은 '사용가능부위 : 자실체'이므로, 일반 식품의 원료로는 자실체(버섯 몸체)만 쓸 수 있다[1]. 건강기능식품 고시형 원료의 원재료 목록에는 없어 고시된 지표성분과 기준은 확인하지 못함.

학술 문헌에서는 이 종을 주로 Coprinopsis cinerea라는 이름으로 부르며, 유전체 논문 제목도 'Coprinopsis cinerea (Coprinus cinereus)'로 두 이름을 함께 적었다[4]. 이 버섯은 2주 안에 한살이를 마치고 합성 배지에서 자라기 때문에 버섯의 발생·감수분열을 연구하는 대표 모델 생물로 쓰여 왔다[4, 5]. 그래서 논문 대부분은 유전·발생·효소 연구이고, 식품으로서의 영양 성분이나 사람 대상 효능 연구는 확인하지 못함.

같은 목록의 먹물버섯(Coprinus comatus)은 별개의 원료이며, 이 문서는 그 자료를 섞지 않는다[2].""") ,
("history","이름과 이용의 역사","""종소명 cinereus는 '잿빛'을 뜻하며, 국문명 '재먹물버섯'도 같은 뜻으로 보이지만 국문명의 유래를 밝힌 공식 자료는 확인하지 못함. 식품의약품안전처 목록에 올린 학명은 Schaeffer가 기재하고 Gray가 Coprinus 속으로 옮긴 'Coprinus cinereus (Schaeff.) Gray'이다[1]. 1999년 대형 리보솜 RNA 유전자 서열 분석에서 넓은 뜻의 Coprinus 속이 하나의 계통이 아니라 세 갈래로 나뉜다는 결과가 나왔다[6]. 그 뒤 이 종은 Coprinopsis cinerea로 불리게 되었고, 2005년 논문은 'Coprinopsis cinerea (syn. Coprinus cinereus)'로, 2010년 유전체 논문은 두 이름을 나란히 적었다[4, 30].

연구 대상으로서의 역사는 길어서, 감수분열이 주름살의 담자기 안에서 한꺼번에 일어나는 성질 때문에 감수분열 세포학과 재조합 연구의 고전적 재료가 되었다[5]. 식용으로는 탄자니아 연구진이 이 종을 '식용·약용 백색부후균'으로 소개하며 사이잘 폐기물에서 재배했다[7]. 우리나라에서 전통적으로 먹어 온 기록은 확인하지 못함.""") ,
("biology","균학적 특징","""재먹물버섯은 담자균류의 주름버섯으로, 자연에서는 초식동물의 똥을 주된 서식처로 삼는 부생균이다[31]. 균사에는 핵이 하나인 단핵 균사와 짝이 맞는 두 균사가 합쳐진 이핵 균사가 있고, 자실체는 보통 이핵 균사에서 생긴다[5]. 단핵·이핵 균사 모두 휴면체인 균핵과 분생포자(오이디아), 두꺼운 벽의 후막포자를 만들 수 있으며, 어느 구조를 만들지는 빛·온도·습도·영양 신호로 정해진다[5].

자실체 형성은 영양이 부족할 때 균사가 뭉친 매듭에서 시작하고, 매듭 형성은 빛에 억제되지만 원기(어린 자실체)로 자라고 성숙하는 데에는 빛 신호가 꼭 필요하다[18]. 다 자란 갓은 스스로 녹는 자가분해를 겪는데, 갓에서 키티나아제와 β-1,3-글루칸 분해효소들이 함께 세포벽을 분해하는 것으로 보고되었다[19, 20]. 갓이 펴지고 자가분해되는 과정은 아연손가락 단백질 유전자 exp2가 조절한다[21]. 대줄기 세포벽은 키틴과 β-1,3·β-1,6-글루칸 외에 β-1,4-글루칸까지 엮인 구조로 보고되었다[22]. 자실체 조직에는 선충·곤충에 독성을 보이는 렉틴 같은 방어 단백질이 조직별로 따로 발현된다[17, 31].""") ,
("related_species","가까운 종과 혼동","""식품의약품안전처 목록에는 이름에 '먹물버섯'이 들어간 원료가 여럿 있다[2]. 먹물버섯(Coprinus comatus)은 먹물버섯·먹물버섯어린자실체·먹물버섯추출물이 '사용가능'이고, 노랑갈색먹물버섯자실체(Coprinellus radians)도 '사용가능'이지만, 갈색먹물버섯(Coprinus micaceus)과 좀밀먹물버섯(Coprinus plicatilis)은 '사용불가'이다[2]. 따라서 이름이 비슷하다고 같은 원료로 다루면 안 된다[1, 2].

계통 분석에서 먹물버섯이 속한 Comati 절은 Leucocoprinus·Podaxis·Agaricus 쪽 갈래에 들고, 다른 먹물버섯 무리와는 떨어져 있었다[6]. 즉 재먹물버섯과 먹물버섯은 이름은 닮았어도 계통이 멀다[6]. 두엄먹물버섯(옛 학명 Coprinus atramentarius)에 든 코프린은 알데하이드 탈수소효소를 막아 술과 함께 먹으면 디설피람과 비슷한 반응을 일으킨다고 쥐 실험에서 보고되었다[26, 27]. 이 코프린 자료는 두엄먹물버섯의 것이며, 재먹물버섯에서 코프린을 확인한 자료는 확인하지 못함.

임상 미생물학에서는 이 종의 무성 세대를 Hormographiella aspergillata라는 별도 이름으로 부른다[25].""") ,
("cultivation","재배와 채취","""실험실에서는 합성 배지에서 키워 약 2주 만에 자실체까지 얻을 수 있다[4]. 식용 재배 사례로, 탄자니아 연구진은 사이잘 잎 찌꺼기와 사이잘 줄기를 섞은 기질에 소똥을 건조중량 기준 10·20·30% 더해 3 L 플라스틱 용기에서 이 버섯을 길렀다[7]. 종균은 수수 낟알로 만들어 습중량 기준 6%를 접종했고, 균사 배양은 28 ± 2 °C·상대습도 78 ± 2%, 발이 단계는 26.5 °C·상대습도 86 ± 4%에서 햇빛을 비추며 진행했다[7].

균사가 기질 전체에 퍼지는 데 평균 10 ± 2일, 원기가 생기는 데 12 ± 3일이 걸렸고, 원기가 생긴 뒤 1–2일이면 수확할 수 있었으며 세 차례 수확(3주기)을 얻었다[7]. 첫 주기의 자실체가 그 뒤 주기보다 무거웠다[7]. 수량과 생물학적 효율의 수치는 같은 논문에 없고 다른 보고에 실렸다고만 적혀 있어 확인하지 못함.

국내 통계청 농작물생산조사와 농림축산식품부 특용작물 생산실적에는 재먹물버섯이나 먹물버섯이 따로 집계되지 않아 국내 생산량은 확인하지 못함[3].""") ,
("processing","가공과 이용","""식품원료로는 자실체와 어린자실체만 쓸 수 있으며, 목록에는 재먹물버섯 추출물 항목이 따로 없다[1]. 이 버섯은 수확 뒤 갓이 빨리 펴지고 스스로 녹는 성질이 있어, 갓 펼침을 조절하는 유전자가 수확 뒤 모양을 유지하는 육종의 표적이 될 수 있다고 논의되었다[21]. 가공식품 제조 방법이나 저장 조건에 관한 공식 자료는 확인하지 못함.

산업적으로는 버섯 자체보다 효소 연구가 많다[28, 29]. 이 균은 락카아제 유전자를 17개 가지며, 액체 배양에서는 Lcc1과 Lcc5가 주된 락카아제였다[28]. 재먹물버섯 퍼옥시다아제(CiP)는 방향족 아민을 산화하는 효소로 연구되어 왔다[29]. 사이잘 폐기물 재배에서는 균사 생장기에 락카아제 활성이 가장 높았고(최대 39.45 ± 12.05 U/g, 수확 후 배지 습중량), 수확 뒤 남은 배지가 효소 원료가 될 수 있다고 제안되었다[7]. 이 효소들은 효소·환경 공학 연구이며 식품으로 먹었을 때의 효능 근거가 아니다[7, 28, 29].""") ,
("genetics","유전체와 유전 다양성","""2010년 이 종의 유전체(약 37 Mb)가 해독되어 13개 염색체로 조립되었다[4]. 감수분열 재조합률은 염색체 위치에 따라 크게 달랐고, 재조합이 적은 구간에는 레트로트랜스포존이 없었으며 다세포 균류에만 있는 FunK1 단백질 인산화효소 집단이 재조합이 많은 구간에서 늘어나 있었다[4].

유전자 표적 기술이 갖추어져 있어, CRISPR/Cas9 유전체 편집이 이 종에서 시연되었고 연구진은 이를 식용버섯 연구의 도구로 제시했다[23]. 유전자를 없앤 균주 실험으로 세스퀴테르펜 합성효소 Cop6이 라고포딘 생합성의 중심 효소임이 확인되었다[10, 11]. 비리보솜 펩타이드 합성효소 유전자를 없애면 철 운반체 코프리노페린이 만들어지지 않고 자실체도 생기지 않았다[15]. 세균이나 선충과 마주하면 항균 펩타이드·단백질과 선충 독성 단백질 유전자가 유도되는 것도 전사체 분석으로 보고되었다[31, 32].

이 결과들은 모두 유전·발생 모델 연구이며, 식품으로서의 품질이나 품종 차이를 다룬 자료는 확인하지 못함.""") ,
("safety","안전성","""식품의약품안전처 「식품원료 목록」에서 재먹물버섯은 자실체에 한해 '사용가능'으로 올라 있다[1]. 재먹물버섯 자실체를 먹은 뒤의 중독·알레르기 사례, 중금속·잔류물질 기준, 공공기관의 안전 정보는 확인하지 못함.

이 종의 무성 세대(Hormographiella aspergillata)는 면역이 크게 떨어진 환자에서 드물게 침습성 폐 감염 등을 일으킨 보고가 있으며, 2020년 문헌 검토 시점까지 침습 감염 22건이 보고되었다[24]. 2026년에는 급성 골수성 백혈병 환자의 호중구 감소기에 생긴 폐 감염 사례가 보고되었다[25]. 이는 환경 곰팡이로서 호흡기로 들어간 감염 사례이며, 버섯을 먹어서 생긴 것은 아니다[24, 25].

자실체 렉틴 CCL2는 선충과 초파리에 독성을 보였는데, 그 독성은 무척추동물에 있는 특정 당사슬 구조에 결합하기 때문이며 이 구조는 곰팡이에는 없다[17]. 같은 논문은 이 당사슬이 꽃가루·곤충 독 알레르겐의 주요 결정 부위라고 덧붙였지만, 사람이 재먹물버섯을 먹었을 때의 영향은 확인하지 못함. 두엄먹물버섯의 코프린-알코올 반응을 이 종에 그대로 적용할 근거는 없다[26, 27].""") ,
]
comp=[
 dict(name="Hitoyopodin A",name_ko="히토요포딘 A",cls="방향족 세스퀴테르페노이드",role="bioactive",part="버섯(초록에 부위 표기 없음)",content="분리·구조 확인(벤족사바이사이클로[3.2.1]옥테인 골격), 함량 미보고[8]",act="HL-60 암세포 증식 억제와 말라리아 원충(Plasmodium falciparum) 억제(시험관); 라고포딘 생합성의 전구체로 제안됨[8]",src=[8]),
 dict(name="Hitoyol A",name_ko="히토욜 A",cls="노르세스퀴테르페노이드",role="bioactive",part="배양액(자실체 아님)",content="분리·구조 확인(exo-tricyclo[5.2.1.0]decane 골격), 함량 미보고[9]",act="라고포딘 B의 탈카르복실화 고리화로 생길 것으로 제안됨; 활성은 확인하지 못함[9]",src=[9]),
 dict(name="Hitoyol B",name_ko="히토욜 B",cls="노르세스퀴테르페노이드",role="bioactive",part="배양액(자실체 아님)",content="분리·구조 확인(4-cyclopentene-1,3-dione 포함), 함량 미보고[9]",act="약한 항말라리아 활성 IC50 59 μM(시험관)[9]",src=[9]),
 dict(name="Lagopodin B",name_ko="라고포딘 B",cls="쿠파렌형 세스퀴테르페노이드",role="bioactive",part="영양 균사(세균 배양 상등액 노출 시 유도)",content="함량 미보고; cop6 유전자 결손 시 생성되지 않음[10]",act="그람양성균(고초균 등) 생장 억제, 그람음성균에는 효과 없음(시험관)[10]; 생합성에 P450 Cox1·Cox2가 관여[11]",src=[10,11]),
 dict(name="Coprinastatin 1",name_ko="코프리나스타틴 1",cls="세스퀴테르펜",role="bioactive",part="에틸아세테이트 추출물(식물 연관 균주, 부위 표기 없음)",content="분리·구조 확인, 함량 미보고[12]",act="생쥐 P388 백혈병 세포주와 임균(Neisseria gonorrhoeae) 생장 억제(시험관)[12]",src=[12]),
 dict(name="Coprinol",name_ko="코프리놀",cls="세스퀴테르펜",role="bioactive",part="에틸아세테이트 추출물(부위 표기 없음)",content="분리, X선 결정으로 구조 확인, 함량 미보고[12]",act="활성은 확인하지 못함[12]",src=[12]),
 dict(name="14-Hydroxy-5-desoxy-2S,3S,9R-illudosin",name_ko="14-하이드록시-5-데스옥시 일루도신",cls="사이클로뷰테인형 세스퀴테르펜",role="bioactive",part="에틸아세테이트 추출물(부위 표기 없음)",content="분리·구조 확인, 함량 미보고; 같은 추출물에서 7,7a-디에피코프리나스타틴 1, 4,5-디하이드로-5-데옥시아르밀롤, 아르밀롤도 분리[13]",act="생쥐 P388 백혈병 세포주를 약하게 억제(시험관)[13]",src=[13]),
 dict(name="Armillol",name_ko="아르밀롤",cls="세스퀴테르펜",role="bioactive",part="에틸아세테이트 추출물(부위 표기 없음)",content="기존 화합물로 분리, 함량 미보고[13]",act="활성은 확인하지 못함[13]",src=[13]),
 dict(name="Copsin",name_ko="콥신(디펜신형 항균 펩타이드)",cls="펩타이드",role="bioactive",part="세균과 함께 배양한 균의 분비물(재조합 효모로 생산해 구조 분석)",content="함량 미보고[14]",act="장알균·리스테리아 등 그람양성균에 살균 작용, 세포벽 전구체 lipid II에 결합(시험관)[14]",src=[14]),
 dict(name="Coprinoferrin",name_ko="코프리노페린",cls="시데로포어(철 운반체)",role="bioactive",part="균사(laeA 결손 균주에서 증가)",content="함량 미보고[15]",act="생합성 유전자를 없애면 생장 저하와 자실체 형성 상실(균 자체의 발생 기능)[15]",src=[15]),
 dict(name="1-Octen-3-ol",name_ko="1-옥텐-3-올(버섯 알코올)",cls="휘발성 옥실리핀",role="bioactive",part="균사(동결·해동으로 손상시킨 뒤 형성)",content="온전한 균사에서는 거의 검출되지 않고 손상 후 30분 안에 많이 생성; 액체 배양 12일째 최대(수치는 그림에만 있어 확인하지 못함)[16]",act="버섯 특유의 흙·버섯 향 성분; 리놀레산에서 CcDOX1 효소를 거쳐 생성[16]",src=[16]),
 dict(name="CCL2 lectin",name_ko="CCL2 렉틴",cls="β-트레포일 렉틴(단백질)",role="bioactive",part="자실체",content="함량 미보고[17]",act="푸코스가 붙은 N-당사슬에 결합해 선충·초파리에 독성(실험동물·무척추동물)[17]",src=[17]),
 dict(name="Galectins Cgl1 and Cgl2",name_ko="갈렉틴 Cgl1·Cgl2",cls="β-갈락토사이드 결합 렉틴(단백질)",role="marker",part="자실체(Cgl1은 원기·성숙 자실체 특이)",content="함량 미보고; 발현 시기로 자실체 발생 표지로 쓰임[18]",act="자실체 조직의 세포외기질·세포벽에 위치, 균사 응집에 관여할 것으로 추정[5, 18]",src=[5,18]),
 dict(name="Chitin",name_ko="키틴(β-글루칸과 결합)",cls="다당류(세포벽)",role="nutrient",part="자실체 대줄기 세포벽",content="키틴, β-1,3·β-1,6-글루칸, β-1,4-글루칸이 결합한 구조; 함량 미보고[22]",act="세포벽 구조 성분; 갓 자가분해 때 키티나아제·글루칸 분해효소로 분해[19, 20, 22]",src=[19,20,22]),
]
compounds=[{"name":c["name"],"name_ko":c["name_ko"],"class":c["cls"],"role":c["role"],"part":c["part"],"content_text":c["content"],"activity_ko":c["act"],"source":c["src"]} for c in comp]
assays=[{
 "role":"literature","compound":"1-Octen-3-ol","compound_ko":"1-옥텐-3-올",
 "part":"균사(YMG 한천배지 5일 배양, 0.5 cm² 절편; 자실체 아님)",
 "content":"정량은 했으나 수치는 그림에만 있어 확인하지 못함[16]",
 "method":"HS-SPME-GC-MS(외부 검량선)",
 "conditions":{"instrument":"GC-MS QP-5050","column":"DB-WAX 30 m × 0.25 mm, 막 두께 0.25 μm","mobile_phase":"헬륨(He), 86.1 kPa","gradient":"40 °C 5분 → 5 °C/분 승온 → 200 °C 2분 유지","flow":"","temp":"주입구·인터페이스 200 °C","detection":"EI 70 eV; 필요 시 단편 이온 m/z 72 감시","injection":"SPME 섬유 주입구 200 °C 10분, 스플릿리스","sample_prep":"20 mL 유리병에 밀봉, 액체질소 2분 동결 후 35 °C 물중탕 10분 해동; 50/30 μm DVB/CAR/PDMS 섬유로 30 °C 30분 헤드스페이스 흡착","standard":"1-옥텐-3-올 표준품(머무름 시간·질량 스펙트럼 비교), 외부 검량선; 용매 추출법에서는 내부표준 노닐 아세테이트 1 μg/mL","linearity":"","lod":"","loq":"","recovery":""},
 "rationale":"이 종에서 성분을 기기분석 조건까지 밝혀 정량한 논문은 이것만 찾았다(PMC 전문 확인). 다만 대상이 식품원료 부위인 자실체가 아니라 실험실 균사이고, 효소 기능 연구의 일부라 지표성분 기준으로 쓰이지는 않는다. 자실체 성분을 정량한 논문은 확인하지 못함[16].",
 "source":[16],"url":"https://pubmed.ncbi.nlm.nih.gov/36122804/","source_kind":"paper"}]
d={"slug":"coprinus-cinereus","name_ko":"재먹물버섯","name_en":"Ink cap (Coprinopsis cinerea)","scientific_name":"Coprinus cinereus (Schaeff.) Gray",
 "aliases":["Coprinus cinereus","Coprinopsis cinerea","Hormographiella aspergillata(무성 세대)","재먹물버섯어린자실체"],
 "sections":[{"key":k,"title":t,"body":b} for k,t,b in sec],
 "compounds":compounds,"markers":[],"assays":assays,"nutrients":[],"production":[],"world":[],"gi":[],"orgs":[],"sources":S}
json.dump(d,open("/home/user/hfoodguide-wave3/docs/materials/coprinus-cinereus/dossier.json","w"),ensure_ascii=False,indent=1)
for s in d["sections"]: print(s["key"],len(s["body"]))
