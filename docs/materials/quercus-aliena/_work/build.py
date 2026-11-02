import json
P='/home/user/hfoodguide-wave3/docs/materials/quercus-aliena/'
A='2026-11-02'
def pm(n,title,pmid,journal,pmc=None):
    url=f'https://pmc.ncbi.nlm.nih.gov/articles/{pmc}/' if pmc else f'https://pubmed.ncbi.nlm.nih.gov/{pmid}/'
    return {'n':n,'title':title,'url':url,'publisher':journal+(' (PubMed Central)' if pmc else ' (PubMed)'),'accessed':A}
S=[
 {'n':1,'title':'식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 갈참나무열매·갈참나무견과(Quercus aliena Blume), 청졸갈참나무열매, 굴참나무열매','url':'https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020','publisher':'식품의약품안전처','accessed':'2026-10-13'},
 pm(2,'Complete chloroplast genome of the Oriental white oak: Quercus aliena Blume. Mitochondrial DNA A. 2015 (초록만 확인)','26114324','Mitochondrial DNA Part A'),
 pm(3,'Genomic divergence and demographic history of Quercus aliena populations. BMC Plant Biol. 2024','38195447','BMC Plant Biology','PMC10775429'),
 pm(4,'First Report of Oak Anthracnose Caused by Apiognomonia errabunda on Oriental White Oak in Korea. Plant Dis. 2013 (초록만 확인)','30722502','Plant Disease'),
 pm(5,'Complete genome sequence of a new putative member of the genus Pelarspovirus that infects Quercus aliena Blume in South Korea. Arch Virol. 2024 (초록만 확인)','38206482','Archives of Virology'),
 pm(6,'Free radical scavenging and hepatoprotective actions of Quercus aliena acorn extract against CCl4-induced liver. Free Radic Res. 2005 (초록만 확인)','16298865','Free Radical Research'),
 pm(7,'Extraction Condition Optimization, Quantitative Analysis, and Anti-AD Bioactivity Evaluation of Acorn Polyphenols from Quercus variabilis, Quercus aliena, and Quercus dentata. Int J Mol Sci. 2024 (전문 확인; PubMed 도구 출력에서 학명이 빠져 종 이름은 WebSearch 결과의 논문 제목으로 확인; 표 수치는 도구 출력에 없음)','39408864','International Journal of Molecular Sciences','PMC11476354'),
 pm(8,'Correction: Du et al. Extraction Condition Optimization, Quantitative Analysis, and Anti-AD Bioactivity Evaluation of Acorn Polyphenols. Int J Mol Sci. 2025 (윤리 승인 번호 정정)','40076998','International Journal of Molecular Sciences','PMC11900019'),
 pm(9,'Traits variation of acorns and cupules during maturation process in Quercus variabilis and Quercus aliena. Plant Physiol Biochem. 2023 (초록만 확인)','36774909','Plant Physiology and Biochemistry'),
 pm(10,'Genomic basis of the distinct biosynthesis of β-glucogallin, a biochemical marker for hydrolyzable tannin production, in three oak species. New Phytol. 2024 (초록만 확인)','38515244','New Phytologist'),
 pm(11,'Asymmetric character displacement in mixed oak stands. New Phytol. 2022 (초록만 확인)','35706383','New Phytologist'),
 pm(12,'Acorns containing deeper plumule survive better: how white oaks counter embryo excision by rodents. Ecol Evol. 2013','24455161','Ecology and Evolution','PMC3894888'),
 pm(13,'Effects of insect infestation on rodent-mediated dispersal of Quercus aliena: results from field and enclosure experiments. Integr Zool. 2019 (초록만 확인)','30019845','Integrative Zoology'),
 pm(14,'Influence of pericarp, cotyledon and inhibitory substances on sharp tooth oak (Quercus aliena var. acuteserrata) germination. PLoS One. 2012','23133517','PLoS One','PMC3485030'),
 pm(15,'Anthocyanin Biosynthesis Associated with Natural Variation in Autumn Leaf Coloration in Quercus aliena Accessions. Int J Mol Sci. 2022','36293036','International Journal of Molecular Sciences','PMC9603646'),
 pm(16,'A specific 296 bp insertion in the DFR1 promoter activates ethylene-mediated anthocyanin biosynthesis during autumn leaf senescence in Quercus aliena. J Exp Bot. 2026 (초록만 확인)','42126248','Journal of Experimental Botany'),
 pm(17,'ABA exerts a promotive effect on the early process of somatic embryogenesis in Quercus aliena Bl. Plant Physiol Biochem. 2024 (초록만 확인)','39068877','Plant Physiology and Biochemistry'),
 pm(18,'Effects of Hericium erinaceus Hedgehog mushroom on the endophytic microbial community of the host plant. J Basic Microbiol. 2022 (초록만 확인)','36316246','Journal of Basic Microbiology'),
 pm(19,'Report on a New Truffle Species, sp. nov., from Korea. Mycobiology. 2021 (초록만 확인)','35035245','Mycobiology','PMC8725893'),
 pm(20,'Ethnological approach to acorn utilization in prehistory: A case study of acorn mook making in South Korea. Front Plant Sci. 2022 (초록만 확인)','36330271','Frontiers in Plant Science','PMC9623170'),
 pm(21,'Successful hemodialysis treatment of suspected acorn toxicosis in a Bedlington terrier. Can Vet J. 2026 (초록만 확인)','42095174','Canadian Veterinary Journal','PMC13142069'),
]
sec=[]
def s(k,t,b): sec.append({'key':k,'title':t,'body':b})
s('overview','한눈에 보기',
"갈참나무(Quercus aliena Blume)는 참나무과(Fagaceae) 참나무속의 갈잎 큰키나무로, 영어로는 Oriental white oak라 불리며 백참나무 무리(Quercus 절)에 속한다[2]. 한국을 포함한 동아시아에 자생하며, 한국 천연림의 주요 낙엽수 가운데 하나로 소개된다[4]. 중국에서도 아열대·온대 산지 숲의 주요 수종으로 생태적·경제적 가치가 크다고 보고되었다[3].\n\n"
"식품의약품안전처 「식품원료 목록」에서 갈참나무는 식품에 사용할 수 있는 원료(사용가능)이고, 사용 조건은 '사용가능부위 : 열매, 견과'이다[1]. 목록의 원료명은 '갈참나무열매'와 '갈참나무견과' 두 가지이며, 다른 이름으로 도토리나무·홍갈참나무, 영어명으로 Oriental chestnut oak·Galcham oak가 적혀 있다[1]. 학명 칸에는 Q. aliena Blume와 함께 var. rubripes Nakai, var. acuticarpa Uyeki, var. heterophylla Uyeki가 나란히 실려 있다[1]. 건강기능식품 고시형 원료의 원재료로 쓰인다는 기록은 확인하지 못함.\n\n"
"열매(도토리) 알맹이에서는 갈산·엘라그산·페룰산·퀘르세틴·아젤라산이 LC-MS/MS로 정량되었다[7]. 갈참나무 도토리의 탄닌 함량 수치는 이 자료의 PubMed 문헌으로는 확인하지 못함.")
s('history','역사와 전통적 이용',
"한국에는 도토리로 묵을 만드는 전통이 있으며, 충북 영동군의 도토리묵 만들기 사례 연구는 도토리 가공에 손이 많이 들고 종과 음식 전통에 따라 가공 방법이 다르다고 보고했다[20]. 다만 이 연구 초록에서 갈참나무 도토리만 따로 다룬 내용은 확인하지 못함. 오늘날 「식품원료 목록」은 갈참나무의 열매와 견과만 식품 원료로 쓸 수 있게 정하고 있다[1].\n\n"
"갈참나무는 중국에서 산업과 조경에 중요한 토착 수종으로 소개되며, 종자로 번식해 왔으나 해충·결실량·종자 품질 문제가 한계로 지적되었다[17]. 가을 잎이 노랑에서 빨강까지 물드는 특성 때문에 붉은 잎 변이체가 관상수 자원으로 연구되고 있다[15][16]. 노루궁뎅이버섯(Hericium erinaceus)과 공생하는 갈참나무 조직의 내생 미생물 군집이 분석되는 등 버섯과의 관계도 연구되었다[18]. 갈참나무 도토리를 따로 약으로 썼다는 공식 기록은 확인하지 못함.")
s('biology','식물학적 특징',
"갈참나무는 백참나무 무리(Quercus 절)에 속하며, 이 절에서 처음으로 엽록체 유전체가 해독된 종이다[2]. 한국에서는 강원도 고성군 송지호 부근 숲에서 수백 그루가 잎 탄저병 피해를 입은 기록이 있어 자생 분포를 보여 준다[4].\n\n"
"열매는 깍정이(각두)에 싸인 견과(도토리)이다[9]. 중국 연구에서 갈참나무와 굴참나무(Q. variabilis) 도토리의 발달 과정을 비교한 결과, 두 종 모두 녹말과 총페놀이 주요 성분이었고 다 익었을 때 굴참나무 도토리의 녹말은 갈참나무의 거의 두 배였다[9]. 다 익은 도토리의 총페놀은 두 종이 비슷한 수준이었고, 발달 초기 해충(Mechoris ursulus) 피해는 갈참나무에서만 심했다[9].\n\n"
"백참나무류 도토리의 배를 4 mm 잘라 내는 실험에서 갈참나무 도토리는 발아율이 떨어졌지만, 싹튼 묘목의 생장에는 유의한 손상이 없었다[12]. 중국 친링산맥의 3년 야외·사육장 실험에서 설치류는 벌레 먹은 도토리보다 성한 갈참나무 도토리를 더 많이 저장하고 먹었다[13]. 가을 잎은 보통 노랗게 물들지만 붉은 잎 변이체에서는 시아니딘 배당체가 쌓여 붉은색을 낸다[15].")
s('related_species','가까운 종',
"「식품원료 목록」에는 갈참나무 변종인 Q. aliena var. acuteserrata f. calvescens가 '청졸갈참나무열매'라는 별도 원료로 실려 있으며, 사용 부위는 열매이다[1]. 중국에서 sharp tooth oak로 불리는 변종 Q. aliena var. acuteserrata의 도토리는 열매껍질의 물리적 제약과 배·떡잎·열매껍질 속 발아 억제 물질 때문에 늦고 고르지 않게 싹튼다고 보고되었다[14]. 같은 실험에서 갈참나무와 이 변종은 따로 다루어졌다[12].\n\n"
"이름 혼동에 주의해야 한다. 「식품원료 목록」에서 '물갈참나무'는 갈참나무가 아니라 굴참나무(Q. variabilis Blume)의 다른 이름으로 실려 있다[1]. 굴참나무는 갈참나무와 서식지가 비슷하지만 다른 절의 종으로, 도토리 녹말·총페놀의 발달 양상이 다르다[9].\n\n"
"떡갈나무(Q. dentata)와 갈참나무가 섞여 자라는 숲에서는 유전자 흐름이 주로 추위에 강한 떡갈나무에서 늦게 들어온 갈참나무 쪽으로 비대칭적으로 일어났고, 섞여 자랄 때 두 종의 잎 형질 차이가 더 커졌다[11]. 굴참나무·갈참나무·떡갈나무 세 종은 깍정이의 가수분해형 탄닌 함량이 서로 다르다[10].")
s('cultivation','재배와 생산',
"갈참나무는 전통적으로 종자(도토리)로 번식하지만, 해충·결실량·종자 품질 문제가 있어 중국에서 체세포배 발생 번식법이 처음 개발되었다[17]. 이 방법은 만개 후 10–11주의 미숙 배에서만 체세포배가 유도되었고, 배 속 내생 앱시스산(ABA)이 많을 때 유리했다[17].\n\n"
"도토리는 설치류가 모아 저장하면서 흩어지는데, 먹이가 풍부한 해에는 성한 도토리를 더 많이 저장하고 먹이가 모자란 해에는 더 많이 먹었다[13]. 갈참나무 도토리는 익기 전 단계에서 해충 피해를 크게 받을 수 있다[9]. 한국에서는 잎 탄저병(Apiognomonia errabunda)이 처음 보고되어 자생지와 조림지의 새로운 위협이 될 수 있다고 지적되었다[4]. 한국 갈참나무에서는 새 바이러스(가칭 quercus leafroll virus)도 확인되었다[5].\n\n"
"한국 갈참나무 뿌리 주변에서는 새로운 송로버섯(Tuber) 종이 보고되었다[19]. 갈참나무 도토리만의 국내 채취·생산 통계는 통계청·산림청 자료에서 확인하지 못함. 지리적 표시 등록도 확인하지 못함.")
s('processing','가공과 이용',
"갈참나무 도토리 알맹이는 45 °C 열풍에서 48시간 말려 껍질을 벗긴 뒤 갈아 80메시 체로 쳐 분석에 쓰였다[7]. 이 연구는 30% 에탄올 초음파 추출로 유리 폴리페놀을, 남은 찌꺼기를 2 M 수산화나트륨으로 가수분해해 결합 폴리페놀을 얻고 거대다공성 수지로 정제했다[7]. 논문은 갈참나무를 포함한 세 종 도토리가 엘라그산·갈산 원료로 쓰일 수 있다고 보았다[7].\n\n"
"갈참나무 도토리 물 추출물은 다른 추출물보다 슈퍼옥사이드 라디칼 소거 활성이 높았다(IC50 4.92 μg/mL)[6]. 이 추출물을 미리 먹인 쥐에서는 사염화탄소로 유발한 간 손상 지표(AST·ALT)가 덜 올랐다(동물)[6]. 이는 동물 실험 결과이며 사람에서 확인된 효과는 아니다[6].\n\n"
"한국의 도토리묵 만들기는 손이 많이 드는 가공이며, 도토리 종과 음식 전통에 따라 가공 방법이 다르다고 보고되었다[20]. 갈참나무 도토리만으로 만든 식품의 국내 생산실적은 확인하지 못함.")
s('genetics','유전체와 육종',
"갈참나무 엽록체 유전체는 160,921 bp, GC 함량 36.9%이며, 25,841 bp 역반복 부위 한 쌍과 90,258 bp 대단일복제 부위, 18,980 bp 소단일복제 부위로 이루어지고 고유 유전자 115개를 가진다[2]. 중국 갈참나무 72그루의 유전체 재분석에서 엽록체 자료는 네 계통, 핵 자료는 세 주요 계통을 지지했고, 유효 집단 크기는 약 100만 년 전 급감했다[3]. 일부 SNP의 대립유전자 빈도는 기온과 양의 상관을 보여 기온 변화에 적응할 여지가 있다고 해석되었다[3].\n\n"
"굴참나무·갈참나무·떡갈나무 세 종의 고품질 표준 유전체가 함께 해독되었고, 깍정이에서 β-글루코갈린이 가수분해형 탄닌 생산의 생화학 지표로 확인되었다[10]. 이 합성의 핵심 효소는 UGT84A13이며, 종 사이 탄닌 축적 차이는 효소 활성보다 프로모터 변이에 따른 발현 차이 때문이었다[10].\n\n"
"붉은 잎 품종 'Qiuyun'에서는 DFR1 유전자 프로모터의 296 bp 삽입이 에틸렌 신호 인자 EIN3와 결합해 안토시아닌 합성을 높였다[16]. 이 연구에서 갈참나무 캘러스 형질전환법도 확립되었다[16].")
s('safety','안전성과 주의',
"갈참나무 열매·견과는 「식품원료 목록」에서 사용가능 원료이며, 목록에 별도 사용 제한 조건은 적혀 있지 않다[1]. 갈참나무 도토리에 대한 알레르기·잔류농약·독성 성분에 관한 식약처 등 공공기관 정보는 확인하지 못함.\n\n"
"갈참나무 깍정이는 가수분해형 탄닌을 만들며 그 생화학 지표는 β-글루코갈린이다[10]. 갈참나무 도토리 자체의 탄닌 함량은 확인하지 못함. 종이 밝혀지지 않은 말린 도토리를 8일 동안 먹은 개에서 급성 신장 손상이 의심된 사례가 있고, 도토리 중독은 소 등 가축에서 잘 알려져 있다[21]. 이는 동물 사례이며 갈참나무 도토리로 확인된 것은 아니다[21].\n\n"
"갈참나무 도토리 추출물은 쥐 실험에서 간 보호 작용을 보였고 독성은 보고되지 않았으나, 사람 대상 안전성 시험은 확인하지 못함[6]. 도토리 폴리페놀 성분의 알츠하이머병 생쥐 실험은 순수 화합물을 먹인 것으로, 도토리 섭취 효과로 바로 옮겨 볼 수 없다[7].")
ND={k:'' for k in ['instrument','column','mobile_phase','gradient','flow','temp','detection','injection','sample_prep','standard','linearity','lod','loq','recovery']}
MAP='종 대응 주의: PubMed 도구 출력에서 학명이 빠져 있어 본문에서 제목 순서(굴참나무·갈참나무·떡갈나무)의 둘째 종 문단을 갈참나무로 대응시켰다'
C=[
 {'name':'Tannins','name_ko':'탄닌(가수분해형 탄닌)','class':'폴리페놀(탄닌)','role':'marker','part':'깍정이(각두)·열매','content_text':'갈참나무 도토리 탄닌 함량 수치는 확인하지 못함; 굴참나무·갈참나무·떡갈나무 깍정이의 가수분해형 탄닌 함량이 서로 다름[10]','activity_ko':'종자 방어 물질로 해석(굴참나무와 비교)[9][10]','source':[9,10]},
 {'name':'beta-Glucogallin','name_ko':'β-글루코갈린','class':'갈로일 당(탄닌 전구체)','role':'marker','part':'깍정이(각두)','content_text':'함량 수치는 확인하지 못함; 세 아시아 참나무 깍정이에서 가수분해형 탄닌 생산의 생화학 지표[10]','activity_ko':'가수분해형 탄닌 생합성의 첫 단계 산물(UGT84A13이 합성)[10]','source':[10]},
 {'name':'Gallic acid','name_ko':'갈산','class':'페놀산','role':'bioactive','part':'열매(도토리 알맹이)','content_text':'유리 폴리페놀 추출물에서 퀘르세틴의 약 9.86배, 아젤라산의 약 51.63배; 절대 함량은 표에 있으나 확인하지 못함[7]. '+MAP+'[7]','activity_ko':'순수 갈산을 먹인 APP/PS1 생쥐에서 Aβ 침착 감소(동물, 도토리 추출물 아님)[7]','source':[7]},
 {'name':'Ellagic acid','name_ko':'엘라그산','class':'페놀산(엘라기탄닌 가수분해 산물)','role':'bioactive','part':'열매(도토리 알맹이)','content_text':'결합 폴리페놀 문단에서 엘라그산이 갈산의 7.42배, 페룰산의 47.52배(본문은 이 문단을 free polyphenol extract로 표기); 절대 함량은 확인하지 못함[7]. '+MAP+'[7]','activity_ko':'순수 엘라그산을 먹인 AD 생쥐 뇌에서 MDA·4-HNE 감소, GPX4 증가(동물)[7]','source':[7]},
 {'name':'Ferulic acid','name_ko':'페룰산','class':'페놀산','role':'bioactive','part':'열매(도토리 알맹이)','content_text':'결합 폴리페놀에서 엘라그산·갈산보다 적음(엘라그산의 1/47.52); 절대 함량은 확인하지 못함[7]','activity_ko':'순수 페룰산 투여 AD 생쥐에서 GFAP·Iba-1 감소(동물)[7]','source':[7]},
 {'name':'Quercetin','name_ko':'퀘르세틴','class':'플라보놀','role':'bioactive','part':'열매(도토리 알맹이)','content_text':'유리 폴리페놀에서 갈산의 약 1/9.86; 절대 함량은 확인하지 못함[7]','activity_ko':'순수 퀘르세틴 투여 AD 생쥐에서 Aβ 침착 감소가 다섯 성분 중 가장 큼(동물)[7]','source':[7]},
 {'name':'Azelaic acid','name_ko':'아젤라산','class':'디카복실산','role':'bioactive','part':'열매(도토리 알맹이)','content_text':'유리 폴리페놀에서 갈산의 약 1/51.63; 절대 함량은 확인하지 못함[7]','activity_ko':'순수 아젤라산 투여 AD 생쥐에서 병리 지표 일부 완화(동물)[7]','source':[7]},
 {'name':'Starch','name_ko':'녹말','class':'다당류','role':'nutrient','part':'열매(도토리)','content_text':'발달 중 급격히 늘어남; 다 익었을 때 굴참나무 도토리 녹말이 갈참나무의 거의 두 배; 수치는 확인하지 못함[9]','activity_ko':'도토리의 주요 저장 물질[9]','source':[9]},
 {'name':'Total phenolics','name_ko':'총페놀','class':'폴리페놀(총량)','role':'bioactive','part':'열매(도토리)·깍정이','content_text':'다 익은 도토리에서 굴참나무와 비슷한 수준; 수치는 확인하지 못함[9]','activity_ko':'해충 방어와 관련된 방어 물질로 해석[9]','source':[9]},
 {'name':'Soluble sugars','name_ko':'가용성 당','class':'당류','role':'nutrient','part':'열매(도토리)·깍정이','content_text':'발달 과정 전체에서 측정됨; 수치는 확인하지 못함[9]','activity_ko':'저장 물질[9]','source':[9]},
 {'name':'Cyanidin 3-O-glucoside','name_ko':'시아니딘-3-O-글루코사이드','class':'안토시아닌','role':'bioactive','part':'잎(가을 붉은 잎 변이체)','content_text':'붉은 잎 변이체의 잎 색에 크게 기여; 함량 수치는 확인하지 못함[15]','activity_ko':'가을 잎 붉은색 발현[15]','source':[15]},
 {'name':'Cyanidin 3-O-sambubioside','name_ko':'시아니딘-3-O-삼부비오사이드','class':'안토시아닌','role':'bioactive','part':'잎(가을 붉은 잎 변이체)','content_text':'붉은 잎 변이체에서 축적; 함량 수치는 확인하지 못함[15]','activity_ko':'가을 잎 붉은색 발현[15]','source':[15]},
]
cond=dict(ND)
cond.update({'instrument':'LC-MS/MS(기종 명시 없음)','column':'Agilent C18 (2.1 mm × 100 mm, 1.8 μm)','mobile_phase':'A: 0.1% 포름산 수용액, B: 아세토니트릴','gradient':'0–0.5 min A 90%·B 10%; 0.5–4 min A 10%·B 90%; 4–5.5 min A 90%·B 10%','flow':'0.3 mL/min','temp':'35 °C','detection':'ESI 음이온 모드; 이온원 230 °C, 사중극자 150 °C, 전달관 250 °C','sample_prep':'도토리 알맹이 45 °C 열풍 48 h 건조·분쇄(80메시) → 30% 에탄올(1:30) 초음파 추출(출력 40%, 1 s 작동/2 s 휴지, 40 min, 3회) → HPD-600 수지 정제(유리); 잔사 2 M NaOH 가수분해 4 h → pH 2.0 산성화 → 에틸아세테이트 추출 → AB-8 수지 정제(결합); 시료를 70% 메탄올 2 mL에 1 min 흔들고 30 min 초음파 → 원심 → 0.22 μm 여과','standard':'갈산·엘라그산·페룰산·아젤라산·퀘르세틴 표준품(7농도)','linearity':'R² > 0.9995'})
cond2=dict(cond)
AS=[
 {'role':'literature','compound':'Gallic acid','compound_ko':'갈산','part':'열매(도토리 알맹이)','content':'유리 폴리페놀에서 퀘르세틴의 약 9.86배, 아젤라산의 약 51.63배(절대 함량은 표에 있으나 확인하지 못함)[7]','method':'LC-MS/MS','conditions':cond,'rationale':'갈참나무 도토리 알맹이의 유리 폴리페놀 가운데 가장 많은 성분으로 정량되었다[7]. 전문 Methods를 확인했으나 검출·정량한계와 회수율은 본문에 없고, 질량 전이(m/z)는 표에 있어 확인하지 못함. '+MAP+'[7].','source':[7],'url':'https://pmc.ncbi.nlm.nih.gov/articles/PMC11476354/','source_kind':'paper'},
 {'role':'literature','compound':'Ellagic acid','compound_ko':'엘라그산','part':'열매(도토리 알맹이)','content':'결합 폴리페놀 문단에서 갈산의 7.42배, 페룰산의 47.52배(절대 함량은 확인하지 못함)[7]','method':'LC-MS/MS','conditions':cond2,'rationale':'알칼리 가수분해로 얻은 결합 폴리페놀의 주성분으로, 엘라기탄닌에서 풀려나는 산물이라 도토리 탄닌 계열의 지표가 될 수 있다[7]. 전문 Methods 확인(조건은 갈산과 같은 분석법). '+MAP+'[7].','source':[7,8],'url':'https://pmc.ncbi.nlm.nih.gov/articles/PMC11476354/','source_kind':'paper'},
]
D={'slug':'quercus-aliena','name_ko':'갈참나무','name_en':'Oriental white oak','scientific_name':'Quercus aliena Blume',
 'aliases':['도토리나무','홍갈참나무','갈참나무열매','갈참나무견과','Oriental chestnut oak','Galcham oak','Quercus aliena var. rubripes Nakai','Quercus aliena var. acuticarpa Uyeki','Quercus aliena var. heterophylla Uyeki'],
 'sections':sec,'compounds':C,'markers':[],'assays':AS,'nutrients':[],'production':[],'world':[],'gi':[],'orgs':[],'sources':S}
json.dump(D,open(P+'dossier.json','w'),ensure_ascii=False,indent=1)
for x in sec: print(x['key'],len(x['body']))
