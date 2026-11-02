import json
from pathlib import Path
A="2026-11-02"
def pm(pmid, title, journal, doi=None, pmc=None):
    url = f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
    t = f"{title} — {journal}" + (f" (PMID {pmid}" + (f", {pmc} 전문" if pmc else ", 초록") + (f", doi:{doi})" if doi else ")"))
    return dict(title=t, url=url, publisher="PubMed (NCBI)", accessed=A)
S = [
 dict(title="식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 다라엽(Ilex latifolia Thunb.), 사용가능, 사용가능부위 : 잎", url="https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", publisher="식품의약품안전처", accessed="2026-10-13"),
 dict(title="식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 같은 속·고정차 혼동 식물 행 대조: 마테(Ilex paraguaariensis, 사용가능부위 잎), Ilex pubescens·먼나무(ILEX ROTUNDA)·톱잎감탕나무(ILEX ASPRELLA) 사용불가, 광나무열매(Ligustrum japonicum)·당광나무열매·여정실(Ligustrum lucidum) 사용불가 (로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json)", url="https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", publisher="식품의약품안전처", accessed="2026-10-13"),
 pm("23529541","The large-leaved Kudingcha (Ilex latifolia Thunb and Ilex kudingcha C.J. Tseng): a traditional Chinese tea with plentiful secondary metabolites and potential biological activities","J Nat Med 2013;67(3):425-37","10.1007/s11418-013-0758-z","PMC3685706"),
 pm("32932672","Chemical Composition, Bioactivity and Safety Aspects of Kuding Tea—From Beverage to Herbal Extract","Nutrients 2020;12(9):2796","10.3390/nu12092796","PMC7551553"),
 pm("36072321","The chromosome-level holly (Ilex latifolia) genome reveals key enzymes in triterpenoid saponin biosynthesis and fruit color change","Front Plant Sci 2022;13:982323","10.3389/fpls.2022.982323","PMC9441949"),
 pm("33366481","Complete chloroplast genome sequence of Ilex latifolia (Aquifoliaceae), a traditional Chinese tea","Mitochondrial DNA B Resour 2019;5(1):190-191","10.1080/23802359.2019.1698985","PMC7748568"),
 pm("35321703","Polyphenols in Ilex latifolia Thunb. inhibit human lung cancer cell line A549 by regulation of the PI3K-Akt signaling pathway","BMC Complement Med Ther 2022;22(1):85","10.1186/s12906-022-03568-3","PMC8943935"),
 pm("23777644","Multi-ingredients determination and fingerprint analysis of leaves from Ilex latifolia using UPLC-QTOF-MS","J Pharm Biomed Anal 2013;84:20-9","10.1016/j.jpba.2013.05.039"),
 pm("15315393","Deodorization with ku-ding-cha containing a large amount of caffeoyl quinic acid derivatives","J Agric Food Chem 2004;52(17):5513-8","10.1021/jf049693j"),
 pm("9887534","Triterpenoid saponins from Ilex latifolia (latifolosides F, G, H)","Phytochemistry 1998;49(8):2483-6","10.1016/s0031-9422(98)00164-2"),
 pm("11217117","Latifolosides I and J, two new triterpenoid saponins from the bark of Ilex latifolia","Chem Pharm Bull 2001;49(2):239-41","10.1248/cpb.49.239"),
 pm("11411534","Latifolosides K and L, two new triterpenoid saponins from the bark of Ilex latifolia","Chem Pharm Bull 2001;49(6):765-7","10.1248/cpb.49.765"),
 pm("25118953","Functional analyses on antioxidant, anti-inflammatory, and antiproliferative effects of extracts and compounds from Ilex latifolia Thunb., a Chinese bitter tea","J Agric Food Chem 2014;62(34):8608-15","10.1021/jf501670v"),
 pm("22870822","Neuroprotection of Ilex latifolia and caffeoylquinic acid derivatives against excitotoxic and hypoxic damage of cultured rat cortical neurons","Arch Pharm Res 2012;35(6):1115-22","10.1007/s12272-012-0620-y"),
 pm("26300958","Crude triterpenoid saponins from Ilex latifolia (Da Ye Dong Qing) ameliorate lipid accumulation by inhibiting SREBP expression via activation of AMPK in a non-alcoholic fatty liver disease model","Chin Med 2015;10:23","10.1186/s13020-015-0054-9","PMC4544818"),
 pm("29116160","Ilex latifolia Thunb protects mice from HFD-induced body weight gain","Sci Rep 2017;7(1):14660","10.1038/s41598-017-15292-x"),
 pm("22451380","Effects of Ilex latifolia and Camellia sinensis on cholesterol and circulating immune complexes in rats fed with a high-cholesterol diet","Phytother Res 2012;27(1):62-5","10.1002/ptr.4693"),
 pm("11233993","Inotropic and chronotropic actions of Ilex latifolia: inhibition of adenosine-5'-triphosphatases as a possible mechanism","Life Sci 2001;68(11):1259-70","10.1016/s0024-3205(00)01024-9"),
 pm("22834418","Ilelic acids A and B, two unusual triterpenes with a seven-membered ring from Ilex latifolia","Org Lett 2012;14(16):4102-5","10.1021/ol301745b"),
 pm("28937158","Bioactivity-guided isolation of neuritogenic triterpenoids from the leaves of Ilex latifolia Thunb.","Food Funct 2017;8(10):3688-3695","10.1039/c7fo00981j"),
 pm("26347952","Four new triterpenes and triterpene glycosides from the leaves of Ilex latifolia and their inhibitory activity on triglyceride accumulation","Fitoterapia 2015;106:141-6","10.1016/j.fitote.2015.09.003"),
 pm("24299866","Characterization, antioxidant and hepatoprotective activities of polysaccharides from Ilex latifolia Thunb.","Carbohydr Polym 2013;101:990-7","10.1016/j.carbpol.2013.10.037"),
 pm("24761642","[Chemical constituents from leaves of Ilex latifolia]","Zhongguo Zhong Yao Za Zhi 2014;39(2):258-61"),
 pm("12567945","[Chemical pattern recognition of traditional Chinese medicine kudingcha (II)]","Zhong Yao Cai 1998;21(4):170-3"),
 pm("12575042","[Pharmacological studies of trilex on treatment of pharyngitis]","Zhong Yao Cai 2000;23(10):630-2"),
 pm("41297428","Triterpenoid saponins from Ilex latifolia inhibit breast cancer growth by disrupting the SREBP1/FASN-mediated lipid metabolic pathway","Biomed Pharmacother 2025;193:118793","10.1016/j.biopha.2025.118793"),
 pm("30962086","Discovery of an EGFR tyrosine kinase inhibitor from Ilex latifolia in breast cancer therapy","Bioorg Med Chem Lett 2019;29(11):1282-1290","10.1016/j.bmcl.2019.04.009"),
 pm("33458120","The complete chloroplast genome of Ilex 'Emily Bruner', Ilex cornuta 'Burfordii' × Ilex latifolia (Aquifoliaceae)","Mitochondrial DNA B Resour 2020;5(3):3227-3228","10.1080/23802359.2020.1810146","PMC7782960"),
 pm("39339625","Impact of Chromosomal Fusion and Transposable Elements on the Genomic Evolution and Genetic Diversity of Ilex Species","Plants 2024;13(18):2649","10.3390/plants13182649"),
 pm("21776475","Caffeoylquinic acid derived free radicals identified during antioxidant reactions of bitter tea (Ilex latifolia and Ilex kudincha)","Food Funct 2010;1(3):262-8","10.1039/c0fo00085j"),
 pm("22593006","Quantitative analysis of five kudinosides in the large-leaved Kudingcha and related species from the genus Ilex by UPLC-ELSD","Phytochem Anal 2012;23(6):677-83","10.1002/pca.2372"),
 pm("35807245","Optimization of Ultrasound-Assisted Extraction of Polyphenols from Ilex latifolia Using Response Surface Methodology and Evaluation of Their Antioxidant Activity","Molecules 2022;27(13):3999","10.3390/molecules27133999"),
 pm("33385007","Holly (Ilex latifolia Thunb.) Polyphenols Extracts Alleviate Hepatic Damage by Regulating Ferroptosis Following Diquat Challenge in a Piglet Model","Front Nutr 2020;7:604328","10.3389/fnut.2020.604328","PMC7770127"),
 pm("21090294","[Selection of winter plant species for wetlands constructed as sewage treatment systems and evaluation of their wastewater purification potentials]","Huan Jing Ke Xue 2010;31(8):1789-94"),
 pm("19717300","Study of the antifungal activity of Bacillus vallismortis ZZ185 in vitro (endophyte from Broadleaf Holly, Ilex latifolia)","Bioresour Technol 2009;101(1):292-7","10.1016/j.biortech.2009.07.071"),
]
for i,s in enumerate(S,1): s["n"]=i
sources=[{"n":s["n"],"title":s["title"],"url":s["url"],"publisher":s["publisher"],"accessed":s["accessed"]} for s in S]

sec = {}
sec["overview"]=("한눈에 보기",
"다라(Ilex latifolia Thunb.)는 감탕나무과(Aquifoliaceae) 감탕나무속의 상록 교목으로, 중국과 일본이 원산이다[5]. 중국 이름은 대엽동청(大葉冬靑, Da Ye Dong Qing)이며, 영어로는 broadleaf holly라고도 부른다[15][35]. 어린잎을 말려 우린 쓴맛의 차를 중국에서는 고정차(苦丁茶, Kudingcha)라 부른다[5][7].\n\n"
"식품의약품안전처 「식품원료 목록」에는 '다라엽'(Ilex latifolia Thunb.)이 사용가능 원료로 올라 있고, 사용 조건은 '사용가능부위 : 잎'이다[1]. 따라서 일반 식품 원료로 쓸 수 있는 부위는 잎뿐이다[1]. 건강기능식품 고시형 원료의 원재료로 쓰인 기록은 확인하지 못함.\n\n"
"고정차라는 이름은 여러 과·속의 약 12종 식물에 함께 쓰이므로, 다라와 Ilex kudingcha를 묶은 '대엽 고정차'와 물푸레나무과 Ligustrum 속의 '소엽 고정차'를 구별해야 한다[3][4]. 잎에는 디카페오일퀸산(이소클로로겐산류)·루틴 같은 폴리페놀과 라티폴로사이드·쿠디노사이드 같은 우르산형 트리테르펜 사포닌이 많다고 보고되었다[7][9][10]. 다라만을 쓴 사람 대상 임상시험은 확인하지 못함.")
sec["history"]=("역사와 전통적 이용",
"고정차는 중국에서 약 2,000년 동안 갈증을 풀고 가래를 삭이며 정신을 맑게 하고 눈을 밝게 하는 차로 쓰였다고 정리되어 있다[3]. 동한 시대 문헌 「동군록(桐君錄)」에는 쓴맛이 나고 밤새 잠을 쫓는 차로 기록되었다고 한다[3]. 당나라 「본초습유(本草拾遺)」와 명나라 「본초강목(本草綱目)」에도 고정차의 효능이 실려 있으며, 리뷰 저자들은 이 옛 기록이 모두 감탕나무속의 대엽 고정차를 가리킨다고 보았다[3]. 반면 Ligustrum 속 소엽 고정차는 1958년 구이저우의 민간 처방집에 처음 보고되었다[3].\n\n"
"다라 잎은 중국 남부에서 전통 음료의 재료로 널리 쓰였고, 감탕나무속 여러 종이 민간에서 관상동맥 질환에 쓰였다[18]. 민간에서는 두통과 여러 염증성 질환에도 쓰였다고 보고된다[14]. 다라·톱잎감탕나무(I. asprella)·먼나무(I. rotunda) 세 종을 섞은 처방은 동물 실험에서 해열·진통·항염 효과를 보여 인두염 용도로 제안되었다[25].\n\n"
"한국에서 다라를 전통적으로 먹거나 약으로 쓴 기록은 확인하지 못함.")
sec["biology"]=("식물학적 특징",
"다라는 중국과 일본이 원산인 아열대 상록 교목이다[5]. 붉은 장과 모양 열매가 달려 관상수로도 가치가 높고, 열매 껍질이 초록에서 빨강으로 바뀔 때 펠라르고니딘·시아니딘 합성 유전자의 발현이 늘어난다[5]. 엽록체 유전체 연구에서는 중국 남서부에 널리 분포하는 상록수로 소개되었다[6].\n\n"
"대엽 고정차를 이루는 다라와 Ilex kudingcha는 겉모습이 매우 비슷하며, 두 종의 주된 차이는 잎밑 모양에 있다고 한다[3]. 대엽 고정차 잎에서는 그해 봄에 난 새잎의 카페산 유도체 함량(147–235 mg/g)이 가을 잎이나 묵은 잎(24–44 mg/g)보다 높았고, 카페인은 검출되지 않았다[3]. 다라 잎에서는 우르산형 트리테르펜 사포닌, 일곱고리 구조의 일렐산, 폴리메톡시플라본, 다당류가 분리되었다[10][19][22][23]. 잎 트리테르펜 가운데 일부는 간세포의 중성지방 축적을 억제하거나 신경돌기 성장을 촉진했다(세포)[20][21].\n\n"
"다라 줄기에서는 식물병원균을 억제하는 내생세균 Bacillus vallismortis ZZ185가 분리되었다[35]. 꽃의 성(암수딴그루 여부)과 자생지 해발 범위 같은 세부 형태는 공식 식물지 원문으로 확인하지 못함.")
sec["related_species"]=("가까운 종과 혼동 식물",
"같은 감탕나무속의 마테(Ilex paraguaariensis)는 「식품원료 목록」에서 잎이 별도의 사용가능 원료로 올라 있으므로 다라와 섞어 다루지 않는다[2]. 마테는 카페인이 많고 주된 폴리페놀이 클로로겐산인 반면, 대엽 고정차에는 카페인이 검출되지 않았고 3,5-디카페오일퀸산 계열이 주된 폴리페놀이다[3]. 같은 목록에서 먼나무(I. rotunda)·톱잎감탕나무(I. asprella)·Ilex pubescens는 사용불가 원료이다[2].\n\n"
"대엽 고정차의 다른 대표 종 Ilex kudingcha는 쿠디노사이드 5종을 UPLC-ELSD로 비교한 연구에서 트리테르펜 사포닌이 가장 많았다[31]. 다라 유전체 연구는 다라가 가까운 종보다 잎의 오환식 트리테르펜 사포닌이 많아 고정차 재료로 선호된다고 보았다[5]. 먼나무 잎에도 3,5-디카페오일퀸산이 14.6% 들어 있었다[9].\n\n"
"소엽 고정차의 원료인 Ligustrum 속 식물 가운데 여정실(당광나무 열매)과 광나무 열매는 「식품원료 목록」에서 사용불가이다[2]. 고정차 시료 78점은 HPLC 자료로 호랑가시나무(I. cornuta)·다라·당광나무로 구분되었으므로, 고정차 제품은 시료 종을 확인해야 한다[24]. 호랑가시나무와 다라의 원예 잡종('Emily Bruner')도 있다[28].")
sec["cultivation"]=("재배와 생산",
"다라의 국내 재배 면적·생산량 통계는 확인하지 못함. 농림축산식품부 특용작물 통계와 통계청 농작물생산조사 파일에서도 다라·고정차 항목은 확인하지 못함.\n\n"
"중국에서는 고정차가 차나무 잎 다음으로 생산량이 많은 식물성 음료라고 유전체 논문이 소개했다[5]. 유전체 분석에 쓴 다라는 중국 난징임업대학 교정에서 재배되던 나무였다[5]. 폐암세포 연구에 쓴 잎은 구이저우성 쭌이의 차 가공 공장에서 얻었다[7].\n\n"
"대엽 고정차의 성분은 종 사이뿐 아니라 같은 종 안에서도 유전, 산지, 기후, 나무 나이, 수확 시기, 환경에 따라 크게 달랐고 건조·저장·추출 방법도 영향을 준다[4]. 산지가 다른 다라 잎 22점은 UPLC-QTOF-MS 지문 분석으로 품질을 비교·구분할 수 있었다[8]. 다라는 아열대 지역 겨울철 인공습지 정화 식물 25종 실험에서 정화 능력이 중간인 무리로 분류되었다[34].")
sec["processing"]=("가공과 이용",
"다라 잎은 말려서 차로 우려 마시는 것이 전통적인 이용법이다[7]. 연구용 폴리페놀 추출물은 동결건조 잎을 70% 에탄올(액체:시료 20:1)로 60°C에서 3시간 추출한 뒤 거대다공성 수지를 거쳐 농축·동결건조해 만들었다[7]. 초음파 추출 조건을 반응표면분석으로 최적화한 결과 에탄올 53%, 60°C, 26분, 60 mL/g에서 폴리페놀 35.77 ± 0.26 mg GAE/g을 얻었다[32].\n\n"
"대엽 고정차의 페놀 성분 농축에는 에틸아세테이트 추출이 가장 좋았고, 사포닌 추출에는 75% 메탄올 30분 초음파 추출이 알맞았다고 정리되었다[4]. 총폴리페놀 65.5%인 시판 다라 폴리페놀 추출물은 새끼돼지 사료에 250 mg/kg 넣어 시험되었다[33]. 고정차는 3,5-디카페오일퀸산이 많아 마늘 섭취 뒤 입 냄새 성분(알릴메틸설파이드)을 줄였다는 보고가 있다[9].\n\n"
"국내에서는 「식품원료 목록」상 잎만 식품에 쓸 수 있다[1]. 다라를 원료로 한 국내 건강기능식품 생산실적은 확인하지 못함.")
sec["genetics"]=("유전체와 종 판별",
"다라는 염색체 수준 유전체가 해독되었으며, 조립 길이 766.02 Mb 가운데 99.8%가 20개 유사염색체에 놓였고 스캐폴드 N50은 33.45 Mb였다[5]. 단백질 암호화 유전자는 35,218개, 반복 서열은 53.0%였고, 진정쌍떡잎식물 공통의 오래된 전유전체 중복과 감탕나무속 고유의 최근 중복이 확인되었다[5]. 트리테르펜 사포닌 합성 후보로 CYP716A 유전자 2개와 CYP72A 유전자 1개가 잎의 다섯 발달 단계에서 모두 높게 발현되었다[5].\n\n"
"다라의 엽록체 유전체는 157,601 bp, 유전자 143개, GC 함량 37.6%였다[6]. 호랑가시나무 × 다라 잡종 'Emily Bruner'의 엽록체 유전체는 157,216 bp였다[28]. 다라를 포함한 감탕나무속 세 종 유전체 비교에서는 염색체 융합과 전이인자가 유전체 진화에 영향을 준 것으로 나타났다[29].\n\n"
"종 판별에는 HPLC 자료와 인공신경망 패턴 인식으로 고정차 시료의 기원 종을 가린 연구가 있다[24]. 다라 잎은 UPLC-QTOF-MS 지문과 주성분분석으로 산지를 구분할 수 있었다[8].")
sec["safety"]=("안전성과 주의",
"다라는 「식품원료 목록」에서 잎에 한해 사용가능하다[1]. 건강기능식품 고시형 원료가 아니어서 고시된 섭취 시 주의사항은 없다[1]. 공공기관의 알레르기·잔류농약·독성 성분 정보는 확인하지 못함.\n\n"
"대엽 고정차는 오래 마셔 온 음료로 대체로 안전하다고 여겨진다[4]. 리뷰에 인용된 흰쥐 실험에서 대엽 고정차 물추출물의 최대내성용량은 168 g/kg였고, 4.5·9·18 g/kg를 90일 먹여도 체중·조혈·혈액 생화학에 영향이 없었다[3]. 그러나 고농도 고정차 추출물(γ-사이클로덱스트린 포접물)을 6주 먹인 생쥐에서는 지방간과 약물대사효소(Cyp3a 등) 유도가 나타나 약물 상호작용 가능성이 제기되었다[4].\n\n"
"다라 잎 물추출물은 적출한 흰쥐 심장의 수축력을 높이고 박동수를 줄였으며 Na+/K+-ATPase를 억제했다[18]. 다라 분말 1.0·2.0 g/kg를 30일 먹인 흰쥐에서는 혈장 총콜레스테롤이 낮아졌다[17]. 다라를 14주 먹인 생쥐는 고지방식에 의한 체중 증가와 지방간이 덜했고, 조사포닌 200 mg/kg/일은 생쥐 지방간 지표를 낮췄다[15][16]. 이런 결과는 동물·세포 실험이며, 사람에서의 안전 섭취량과 심장약 병용 영향은 확인하지 못함. 카페인이 많은 마테와 달리 대엽 고정차에서는 카페인이 검출되지 않았다[3].")

order=["overview","history","biology","related_species","cultivation","processing","genetics","safety"]
sections=[{"key":k,"title":sec[k][0],"body":sec[k][1]} for k in order]

def c(name,ko,cls,role,part,ct,act,src): return dict(name=name,name_ko=ko,**{"class":cls},role=role,part=part,content_text=ct,activity_ko=act,source=src)
compounds=[
 c("Isochlorogenic acid A","이소클로로겐산 A(3,5-디카페오일퀸산)","페놀산(디카페오일퀸산)","marker","잎·잎 폴리페놀 추출물","폴리페놀 추출물 102.52 mg/g(HPLC)[7]; 잎 건조중량의 9.5%(3,5-diCQA, HPLC)[9]","배양 신경세포에서 글루탐산·저산소 손상 억제(세포)[14]; 티올 냄새 성분 포착(시험관)[9]",[7,9,14]),
 c("Isochlorogenic acid C","이소클로로겐산 C(4,5-디카페오일퀸산)","페놀산(디카페오일퀸산)","marker","잎 폴리페놀 추출물","128.36 mg/g(추출물 기준, HPLC)[7]","폴리페놀 추출물의 A549 폐암세포 증식 억제에 기여하는 5개 성분의 하나로 제시(세포)[7]",[7]),
 c("Isochlorogenic acid B","이소클로로겐산 B(3,4-디카페오일퀸산)","페놀산(디카페오일퀸산)","marker","잎·잎 폴리페놀 추출물","88.12 mg/g(추출물 기준, HPLC)[7]","3,4-diCQA가 글루탐산 유발 세포 내 칼슘 증가·활성산소 생성 억제(세포)[14]",[7,14]),
 c("Rutin","루틴","플라보놀 배당체","marker","잎 폴리페놀 추출물","216.35 mg/g(추출물 기준, 5개 성분 중 최다, HPLC)[7]","추출물 항산화·항암 작용 성분의 하나로 제시(세포)[7]",[7]),
 c("Kaempferol","캠페롤","플라보놀","bioactive","잎 폴리페놀 추출물","167.28 mg/g(추출물 기준, HPLC)[7]","추출물 5개 주성분의 하나(세포)[7]",[7]),
 c("Chlorogenic acid","클로로겐산(5-카페오일퀸산)","페놀산(모노카페오일퀸산)","bioactive","잎","잎 건조중량의 4.8%(5-CQA, HPLC)[9]; 에틸아세테이트 분획에서 분리[13]","분리 성분 중 대식세포 NO 생성 억제가 가장 강함(세포)[13]",[9,13]),
 c("3-O-Caffeoylquinic acid","3-카페오일퀸산(명명 체계에 따라 네오클로로겐산)","페놀산(모노카페오일퀸산)","bioactive","잎","잎 건조중량의 4.3%(3-CQA, HPLC)[9]","고정차 항산화 반응에서 생기는 라디칼은 카페오일퀸산 유래로 확인(EPR)[30]",[9,30]),
 c("Latifoloside G","라티폴로사이드 G","트리테르펜 사포닌(포몰산 배당체)","marker","잎","잎에서 새로 분리(함량 확인하지 못함)[10]; 대엽 고정차 리뷰는 라티폴로사이드 G·쿠디노사이드 A·G가 총사포닌의 80% 넘게 차지해 지표 성분으로 제안된 연구를 소개[4]","총사포닌 품질 관리 지표 후보[4]",[4,10]),
 c("Kudinoside A","쿠디노사이드 A","트리테르펜 사포닌(β-쿠딘락톤형)","marker","잎","대엽 고정차 총사포닌 지표 후보 3종의 하나(함량 확인하지 못함)[4]","대엽 고정차의 특징 사포닌; 쿠디노사이드 정량법 대상(UPLC-ELSD)[31]",[4,31]),
 c("Kudinoside G","쿠디노사이드 G","트리테르펜 사포닌","marker","나무껍질·잎","다라 나무껍질에서 분리[12]; 총사포닌 지표 후보로 소개[4]","품질 관리 지표 후보[4]",[4,12]),
 c("Latifoloside C","라티폴로사이드 C","트리테르펜 사포닌","bioactive","나무껍질","다라 나무껍질에서 라티폴로사이드 I·J와 함께 분리(함량 확인하지 못함)[11]","생리활성은 확인하지 못함",[11]),
 c("Kudinoside D","쿠디노사이드 D","트리테르펜 사포닌(γ-쿠딘락톤형)","bioactive","다라(부위는 초록에 없음)","다라에서 분리(함량 확인하지 못함)[26]","유방암세포에서 SREBP-1/FASN 억제·세포자멸 유도(세포·동물)[26]",[26]),
 c("27-O-p-Coumaroyl ursolic acid","27-O-p-쿠마로일 우르솔산","트리테르펜(우르산형)","bioactive","잎","다라 잎 트리테르펜에서 분리(함량 확인하지 못함)[27]","EGFR 티로신인산화효소 억제·유방암세포 자멸 유도(세포)[27]",[27]),
 c("Ursolic acid","우르솔산","트리테르펜(우르산형)","bioactive","잎","95% 에탄올 추출물의 에틸아세테이트 분획에서 분리[13]","다라 사포닌들의 아글리콘 골격; 분리 성분으로 항산화·항염 평가(세포)[13]",[13]),
 c("Ethyl caffeate","에틸카페에이트","페놀산 에스터","bioactive","잎","에틸아세테이트 분획에서 분리(함량 확인하지 못함)[13]","항산화·항염 활성 평가 대상(세포)[13]",[13]),
]
assays=[
 dict(role="literature",compound="Rutin",compound_ko="루틴 외 이소클로로겐산 A·B·C, 캠페롤(5종 동시 정량)",part="잎(70% 에탄올 추출 후 수지 정제한 폴리페놀 추출물)",content="추출물 기준 루틴 216.35, 캠페롤 167.28, 이소클로로겐산 A 102.52, B 88.12, C 128.36 mg/g[7]",method="HPLC-UV(외부표준법)",
  conditions=dict(instrument="UltiMate3000 HPLC System(Thermo Fisher Scientific)",column="C18(4.6 mm × 150 mm, 2.6 μm; 제조사 원문 미기재)",mobile_phase="A 0.5% 아세트산 용액, B 아세토니트릴",gradient="",flow="0.6 mL/min",temp="30°C",detection="자외가시선 검출기 359 nm",injection="10 μL",sample_prep="동결건조 잎 분쇄 → 70% 에탄올(액체:시료 20:1) 60°C 수욕 3시간 → FL-3 거대다공성 수지 통과 → 감압 농축 → 동결건조 분말; 시료 원액 1.0 mg/mL",standard="외부표준법(Mx = Cr × Ax/Ar × C)",linearity="",lod="",loq="",recovery=""),
  rationale="다라 잎 폴리페놀 추출물의 주성분 5종을 정량하고 폐암세포 억제 효과의 주된 성분으로 제시했다; 기울기·검량선·검출한계·회수율은 원문에 없음[7]",source=[7],url="https://pubmed.ncbi.nlm.nih.gov/35321703/",source_kind="paper"),
 dict(role="literature",compound="3,5-Dicaffeoylquinic acid",compound_ko="3,5-디카페오일퀸산(이소클로로겐산 A)·3-CQA·5-CQA",part="잎(건조)",content="다라 잎 건조중량 기준 3,5-diCQA 9.5%, 3-CQA 4.3%, 5-CQA 4.8%[9]",method="HPLC",
  conditions=dict(instrument="",column="",mobile_phase="",gradient="",flow="",temp="",detection="",injection="",sample_prep="",standard="",linearity="",lod="",loq="",recovery=""),
  rationale="대엽 고정차의 주된 폴리페놀이 디카페오일퀸산이며 다라 잎에서도 가장 많았다; 초록만 확인해 분석 조건은 전문 확인 못함[9]",source=[9],url="https://pubmed.ncbi.nlm.nih.gov/15315393/",source_kind="paper"),
 dict(role="literature",compound="Multi-ingredients (UPLC-QTOF-MS)",compound_ko="다성분 동시 정량(정량 성분명은 초록에 없음)",part="잎",content="산지가 다른 다라 잎 22점 분석(개별 함량은 확인하지 못함)[8]",method="UPLC-QTOF-MS(ESI 음이온)",
  conditions=dict(instrument="UPLC-QTOF-MS",column="",mobile_phase="",gradient="",flow="",temp="",detection="ESI 음이온 모드; 정확 질량 유사분자이온 추출이온크로마토그램(0.01 Da 창)으로 정량, 기준피크 크로마토그램으로 지문 분석; 13분 안에 분석",injection="",sample_prep="",standard="",linearity="",lod="",loq="",recovery=""),
  rationale="다라 잎의 다성분 정량과 지문(유사도·주성분분석)을 한 번에 해 산지·진위 판별에 쓰도록 제안됨; 초록만 확인해 칼럼·이동상 등은 전문 확인 못함[8]",source=[8],url="https://pubmed.ncbi.nlm.nih.gov/23777644/",source_kind="paper"),
]
d=dict(slug="ilex-latifolia",name_ko="다라",name_en="Broadleaf holly (large-leaved Kudingcha)",scientific_name="Ilex latifolia Thunb.",
 aliases=["다라엽","대엽동청(大葉冬靑)","Da Ye Dong Qing","고정차(苦丁茶, 대엽 고정차)","Kudingcha","Kuding tea","Broadleaf holly"],
 sections=sections,compounds=compounds,markers=[],assays=assays,nutrients=[],production=[],world=[],gi=[],orgs=[],sources=sources)
Path("/home/user/hfoodguide-wave3/docs/materials/ilex-latifolia/dossier.json").write_text(json.dumps(d,ensure_ascii=False,indent=1),encoding="utf-8")
for s in sections: print(s["key"],len(s["body"]))
