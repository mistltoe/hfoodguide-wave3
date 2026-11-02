import json
A="2026-11-02"
def S(n,title,url,pub,acc=A): return {"n":n,"title":title,"url":url,"publisher":pub,"accessed":acc}
D="https://doi.org/"
P="https://pubmed.ncbi.nlm.nih.gov/"
sources=[
S(1,"식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 백합(Meretrix lusoria) 항목 및 같은 목록의 말백합·민무늬백합·남방백합·무명조개·Backwater hard clam 항목","https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020","식품의약품안전처","2026-10-13"),
S(2,"The complete mitochondrial genome of Meretrix lusoria (Bivalvia: Veneroida: Veneridae) from Kumamoto, Japan. Mitochondrial DNA B Resour 2020;5(3):2451–2453 (PMC 전문 확인; 전문에서 학명 이탤릭이 빠져 있음)",D+"10.1080/23802359.2020.1778555","Mitochondrial DNA Part B, PMC7782281, PubMed"),
S(3,"Complete mtDNA of Meretrix lusoria (Bivalvia: Veneridae) reveals the presence of an atp8 gene, length variation and heteroplasmy in the control region. Comp Biochem Physiol Part D 2010;5(4):256–264 (초록)",D+"10.1016/j.cbd.2010.07.003","Comparative Biochemistry and Physiology D, PubMed"),
S(4,"Ultrastructure of sperm and complete mitochondrial genome in Meretrix sp. (Bivalvia: Veneridae) from Taiwan. Tissue Cell 2020;67:101454 (초록)",D+"10.1016/j.tice.2020.101454","Tissue and Cell, PubMed"),
S(5,"Telomere-to-Telomere, Haplotype-Resolved Chromosome-Level Genome Assembly and Annotation of Taiwan Hard Clam (Meretrix taiwanica). Sci Data 2026;13 (PMC 전문 확인)",D+"10.1038/s41597-026-07409-7","Scientific Data, PMC13369148, PubMed"),
S(6,"Genetic Distances of Three White Clam (Meretrix lusoria) Populations Investigated by PCR Analysis. Dev Reprod 2014;18(2):89–98 (초록)",D+"10.12717/DR.2014.18.2.089","Development & Reproduction, PMC4282255, PubMed"),
S(7,"Novel microsatellite markers of Meretrix petechialis and cross-species amplification in related taxa (Bivalvia: Veneroida). Int J Mol Sci 2012;13(12):15942–15954 (초록)",D+"10.3390/ijms131215942","International Journal of Molecular Sciences, PMC3546671, PubMed"),
S(8,"Evolution of the tRNA gene family in mitochondrial genomes of five Meretrix clams (Bivalvia, Veneridae). Gene 2013;533(1):439–446 (초록)",D+"10.1016/j.gene.2013.09.077","Gene, PubMed"),
S(9,"Inner shell as variation key of local hard clam Meretrix spp. J Environ Biol 2016;37(4 Spec No):641–646 (초록)",P+"28779722/","Journal of Environmental Biology, PubMed"),
S(10,"Ionic and Amino Acid Regulation in Hard Clam (Meretrix lusoria) in Response to Salinity Challenges. Front Physiol 2016;7:368 (PMC 전문 확인)",D+"10.3389/fphys.2016.00368","Frontiers in Physiology, PMC4997000, PubMed"),
S(11,"Time-course changes in the regulation of ions and amino acids in the hard clam Meretrix lusoria upon lower salinity challenge. J Exp Zool A 2021;335(7):602–613 (초록)",D+"10.1002/jez.2503","Journal of Experimental Zoology A, PubMed"),
S(12,"Chemical compositions and nutritional value of Asian hard clam (Meretrix lusoria) from the coast of Andaman Sea. Food Chem 2013;141(4):4138–4145 (초록)",D+"10.1016/j.foodchem.2013.07.001","Food Chemistry, PubMed"),
S(13,"Enantioselective two-dimensional high-performance liquid chromatographic determination of N-methyl-D-aspartic acid and its analogues in mammals and bivalves. J Chromatogr A 2012;1269:255–261 (초록)",D+"10.1016/j.chroma.2012.08.075","Journal of Chromatography A, PubMed"),
S(14,"Induction of apoptosis by Meretrix lusoria through reactive oxygen species production, glutathione depletion, and caspase activation in human leukemia cells. Life Sci 2006;79(12):1140–1152 (초록)",D+"10.1016/j.lfs.2006.03.049","Life Sciences, PubMed"),
S(15,"Anti-Obesity and Anti-Hyperglycemic Effects of Meretrix lusoria Protamex Hydrolysate in ob/ob Mice. Int J Mol Sci 2022;23(7):4015 (PMC 전문 확인)",D+"10.3390/ijms23074015","International Journal of Molecular Sciences, PMC8999646, PubMed"),
S(16,"Bioactive Peptides from Meretrix lusoria Enzymatic Hydrolysate as a Potential Treatment for Obesity in db/db Mice. Nutrients 2024;16(12):1913 (초록)",D+"10.3390/nu16121913","Nutrients, PMC11206624, PubMed"),
S(17,"The complete amino acid sequence and enzymatic properties of an i-type lysozyme isolated from the common orient clam (Meretrix lusoria). Biosci Biotechnol Biochem 2013;77(11):2269–2277 (초록)",D+"10.1271/bbb.130534","Bioscience, Biotechnology, and Biochemistry, PubMed"),
S(18,"The occurrence of glycosphingolipids containing mannose in the sea-water bivalve, Meretrix lusoria (Hamaguri). J Biochem 1985;98(1):27–34 (초록)",D+"10.1093/oxfordjournals.jbchem.a135268","Journal of Biochemistry, PubMed"),
S(19,"Fatty acid composition, sarcoplasmic reticular lipid oxidation, and immunity of hard clam (Meretrix lusoria) fed different dietary microalgae. Fish Shellfish Immunol 2015;45(1):141–145 (초록)",D+"10.1016/j.fsi.2015.02.025","Fish & Shellfish Immunology, PubMed"),
S(20,"Effect of a Novel Microwave-Assisted Induction Heating (MAIH) Technology on the Quality of Prepackaged Asian Hard Clam (Meretrix lusoria). Foods 2021;10(10):2299 (초록)",D+"10.3390/foods10102299","Foods, PMC8535352, PubMed"),
S(21,"Bioaccumulation of arsenic compounds in aquacultural clams (Meretrix lusoria) and assessment of potential carcinogenic risks to human health by ingestion. Chemosphere 2007;69(1):128–134 (초록)",D+"10.1016/j.chemosphere.2007.04.038","Chemosphere, PubMed"),
S(22,"Biometry-dependent metal bioaccumulation in aquaculture shellfishes in southwest Taiwan and consumption risk. Chemosphere 2020;253:126685 (초록)",D+"10.1016/j.chemosphere.2020.126685","Chemosphere, PubMed"),
S(23,"Bioaccumulation and distribution of mercury in the hard clam, Meretrix lusoria (Bivalvia: Veneidae). Comp Biochem Physiol C 1993;106(1):131–139 (초록)",D+"10.1016/0742-8413(93)90264-l","Comparative Biochemistry and Physiology C, PubMed"),
S(24,"Effects of toxic dinoflagellates and toxin biotransformation in bivalves. J Nat Toxins 2002;11(4):315–322 (초록)",P+"12503874/","Journal of Natural Toxins, PubMed"),
S(25,"Analysis of persistent organochlorine pesticides in shellfish and their risk assessment from aquafarms in Taiwan. Mar Pollut Bull 2021;172:112811 (초록)",D+"10.1016/j.marpolbul.2021.112811","Marine Pollution Bulletin, PubMed"),
S(26,"Quinolone and Organophosphorus Insecticide Residues in Bivalves and Their Associated Risks in Taiwan. Molecules 2020;25(16):3636 (초록)",D+"10.3390/molecules25163636","Molecules, PMC7465073, PubMed"),
S(27,"Assessment of polycyclic aromatic hydrocarbons in seafood collected from coastal aquaculture ponds in Taiwan and human health risk assessment. J Hazard Mater 2021;421:126708 (초록)",D+"10.1016/j.jhazmat.2021.126708","Journal of Hazardous Materials, PubMed"),
S(28,"Presence of Microplastics in Four Types of Shellfish Purchased at Fish Markets in Okayama City, Japan. Acta Med Okayama 2021;75(3):381–384 (초록)",D+"10.18926/AMO/62234","Acta Medica Okayama, PubMed"),
S(29,"Quantifying the impact of temperature variation on birnavirus transmission dynamics in hard clams Meretrix lusoria. J Fish Dis 2020;43(1):57–68 (초록)",D+"10.1111/jfd.13105","Journal of Fish Diseases, PubMed"),
S(30,"Risk-based probabilistic approach to assess the impact of false mussel invasions on farmed hard clams. Risk Anal 2010;30(2):310–323 (초록)",D+"10.1111/j.1539-6924.2009.01315.x","Risk Analysis, PubMed"),
S(31,"Assessment of the roles of copepod Apocyclops royi and bivalve mollusk Meretrix lusoria in white spot syndrome virus transmission. Mar Biotechnol 2011;13(5):909–917 (초록)",D+"10.1007/s10126-010-9352-5","Marine Biotechnology, PubMed"),
S(32,"Hard clam extracts induce atypical apoptosis in human gastric cancer cells. Exp Ther Med 2017;14(2):1409–1418 (초록)",D+"10.3892/etm.2017.4630","Experimental and Therapeutic Medicine, PMC5525584, PubMed"),
S(33,"Metabolome Diversity Enhances Resistance of Intertidal Clams to Thermal Stress. Integr Zool 2026 (초록)",D+"10.1111/1749-4877.70107","Integrative Zoology, PubMed"),
S(34,"Immune bioactivity in shellfish toward serum-free cultured human cell lines. Biosci Biotechnol Biochem 1997;61(1):24–28 (초록)",D+"10.1271/bbb.61.24","Bioscience, Biotechnology, and Biochemistry, PubMed"),
S(35,"Crystalline arrangement and nanostructure of aragonitic crossed lamellar layers of the Meretrix lusoria shell. Zoology (Jena) 2010;113(2):125–130 (초록)",D+"10.1016/j.zool.2009.08.004","Zoology, PubMed"),
]

secs=[]
def sec(k,t,b): secs.append({"key":k,"title":t,"body":b})

sec("overview","한눈에 보기",
"백합(Meretrix lusoria)은 백합과(Veneridae) 백합속에 드는 바다 조개로, 영어로는 hard clam 또는 common orient clam이라 부른다[1, 17]. 식약처 「식품원료 목록」에는 원료명 '백합', 영문명 'Hard clam, Common orient clam', 분류 '수산물'로 올라 있다[1]. 이 목록에서 상태는 '사용가능'이고, 사용 부위는 따로 정하지 않은 '-'로 적혀 있으며 별도의 사용 조건은 없다[1]. 일본에서는 하마구리(hamaguri)라 부르며 어시장에서 팔리는 식용 조개다[18, 28].\n\n"
"백합속 조개는 겉모양만으로 종을 가리기 어려워, 대만 등에서 M. lusoria로 불려 온 양식 조개가 별개의 종일 수 있다는 분자 연구가 나와 있다[2, 4, 5]. 그래서 이 글에서 인용한 대만·동남아 시료 연구는 논문이 붙인 학명을 따른 것이며, 실제 종 동정은 원문마다 다를 수 있다[4, 5]. 식용 부위의 일반성분·아미노산·지방산 조성과 단백질 가수분해물의 동물 실험 연구가 있다[12, 15]. 건강기능식품 고시형 원료로 등재된 기록과 식약처 지정 지표성분은 확인하지 못함.")

sec("history","이용 역사",
"일본 구마모토산 백합의 미토콘드리아 유전체 논문은 이 조개가 일본 수산 생산 조사에서 도쿄만·이세만·아리아케해를 중심으로 중요한 상업 패류였다고 소개한다[2]. 같은 논문은 많은 지역에서 자원량이 크게 줄었지만 구마모토의 시라카와·미도리카와 하구가 여전히 중요한 자연 서식지라고 적었다[2]. 이 논문은 일본에 분포하는 백합속 조개가 약 8000년 전 조몬 시대 패총에서도 나온다고 소개하지만, 전문에서 종명이 빠져 있어 어느 종을 가리키는지는 확인하지 못함.\n\n"
"백합은 1985년 당지질 조성 연구의 재료로 쓰였고, 논문 제목에 일본명 하마구리가 함께 적혀 있다[18]. 2021년 일본 오카야마 어시장 조사에서도 바지락·재첩·굴과 함께 시민에게 팔리는 조개 네 가지 가운데 하나로 다뤄졌다[28]. 대만에서는 육상 연못 양식으로 가장 많이 기르는 패류가 재첩류와 백합이라고 보고되었다[25, 26]. 대만 양식장의 버나바이러스 폐사 자료는 1997–2017년에 걸쳐 분석되었다[29]. 국내에서는 여수 수산시장에서 산 백합으로 효소 가수분해물을 만든 연구가 있다[15].")

sec("biology","패류 특징·생태",
"백합 껍데기는 아라고나이트로 된 교차 판상(crossed lamellar) 구조이며, 가장 작은 단위는 폭 약 500 nm·높이 약 70 nm의 육각형 판이다[35]. 대만 연구에서 백합은 약 20‰ 바닷물에서 자연 서식·양식되며, 바깥 염분이 바뀌면 혈림프 삼투질 농도와 나트륨·염소 농도가 같은 방향으로 바뀌는 삼투순응형 동물로 나타났다[10]. 아가미와 외투막의 유리아미노산 가운데 타우린이 약 20–40%로 가장 많았고, 35‰에서는 외투막 타우린과 아가미·외투막 알라닌이 늘었다[10]. 10‰로 옮긴 실험에서는 아가미·외투막의 유리아미노산이 줄었다[11].\n\n"
"말레이시아 사라왁의 M. lyrata·M. meretrix·M. lusoria 비교에서는 껍데기 안쪽의 외투막 만입 흔적(pallial sinus scar) 모양이 종마다 달라 구별 형질로 제안되었다[9]. 중국 연안 백합속 네 개체군(말백합 3, M. lusoria 1)의 대사체 비교에서는 고온 스트레스 반응이 종·개체군마다 달랐다[33]. 먹이 미세조류 종류를 바꿔 8주 기른 실험에서 극성지질의 EPA·DHA 비율이 먹이 조류의 조성을 따라갔다[19].")

sec("related_species","관련 종·이름",
"식약처 「식품원료 목록」에는 같은 속의 말백합(M. petechialis), 민무늬백합, 남방백합(M. lyrata), 무명조개(M. meretrix), 영문명으로만 오른 Backwater hard clam(M. casta)이 따로 올라 있다[1]. 이 가운데 민무늬백합 항목은 학명란에 'Meretrix lamarckii / Meretix petechialis'가 함께 적혀 있어, 목록만으로는 말백합과 이름이 겹쳐 보일 수 있다[1].\n\n"
"국내 연구에서 군산·신안·영광 연안 개체를 M. lusoria로 다룬 유전 분석이 있으며, 이 논문은 COI 증폭 단편 크기에서 M. lusoria와 M. petechialis 사이에 뚜렷한 차이를 보지 못했다[6]. 한편 국립수산과학원 연구진은 한반도 서해안의 아시아 백합을 M. petechialis로 다루며 대규모 매립 등으로 어획량과 자원이 빠르게 줄고 있다고 적었다[7]. 대만산 백합속 조개는 미토콘드리아 유전체로 보아 말백합·일본산 M. lusoria와 다른 종으로 보고되었고[4], 2026년 유전체 논문은 이를 M. taiwanica로 잠정 동정했다[5]. 구마모토 논문도 백합속은 형태만으로 가리기 어려워 미토콘드리아 DNA가 동정에 유용하다고 했다[2]. 백합속 다섯 종의 미토콘드리아 tRNA 유전자 구성은 종마다 달랐다[8].")

sec("cultivation","양식·채취",
"대만에서는 백합을 육상 연못에서 기르며, 재첩류와 함께 가장 많이 양식하는 패류로 소개된다[25, 26]. 대만 남서부 양식장에서는 외래종 이매패 Mytilopsis sallei(false mussel)가 붙어 폐사를 일으키며, 위험 모델은 50% 폐사에 해당하는 밀도를 2,812 개체/m²·조개 한 마리당 31 개체로 추정했다[30]. 버나바이러스 전파 모델은 연못 수온을 25–30 ℃로 관리하면서 6월과 8월에 조개를 걷어내는 방법이 폐사와 전파를 줄이는 데 낫다고 제안했다[29]. 백합은 새우 어미의 먹이로 쓰이거나 새우와 함께 기르기도 하며, 흰반점바이러스(WSSV)가 백합 안에서 증식하지는 않았지만 쌓인 바이러스가 흰다리새우에 옮겨 갔다[31].\n\n"
"일본 구마모토에서는 시라카와·미도리카와 하구가 자연 개체군의 주요 서식지로 꼽힌다[2]. 시판 크기(평균 25 g) 백합에 미세조류를 먹인 실험에서는 Isochrysis galbana를 먹인 무리의 DHA 비율이 가장 높았다[19]. 국내 백합의 양식·채취 방식과 생산량 통계는 공식 자료로 확인하지 못함.")

sec("processing","가공·추출 연구",
"포장한 생백합을 마이크로파 보조 유도가열로 익힌 연구에서는 130 ℃ 110초 또는 90 ℃ 130초가 알맞은 조건이었고, 130 ℃에서 120초를 넘기면 살이 크게 줄고 누렇게 변했다[20]. 여수 수산시장 백합을 건조 분말로 만들어 네 가지 단백질분해효소로 가수분해한 연구에서, protamex 분해물의 1 kDa 이하 분획이 라디칼 소거능이 가장 컸고 주요 펩타이드로 KDLEL(Lys-Asp-Leu-Glu-Leu)이 동정되었다[15]. 이 분획을 비만 생쥐(ob/ob)에 체중 kg당 150·300 mg씩 6주 먹이자 지방 무게가 줄고 포도당 내성이 나아졌으나, 저자들도 동물 실험이라는 한계를 밝혔다[15]. 2024년 후속 연구도 렙틴 수용체 결손 생쥐에서 체중·혈중 지질 감소를 보고했다[16].\n\n"
"백합 에틸아세테이트 분획의 에피디옥시스테롤은 사람 백혈병 세포(HL-60)에서 세포자멸사를 일으켰고[14], 냉동·해동으로 얻은 추출물은 위암 세포주(AGS)의 생존을 억제했다[32]. 열수 추출물은 배양 하이브리도마 세포의 IgM 분비를 늘렸다[34]. 이 결과들은 세포·동물 실험이며 사람에서의 효과는 확인하지 못함.")

sec("genetics","유전 정보",
"중국 하이난·푸젠 시료로 해독한 M. lusoria 미토콘드리아 유전체는 20,268 bp로, atp8을 포함한 단백질 유전자 13개, rRNA 2개, tRNA 22개를 가졌다[3]. 이 유전체의 비암호 영역에는 101 bp 단위가 약 11번 되풀이되는 1087 bp 반복 구간이 있었고, 반복 수에 따라 조절 영역 길이가 1942–3354 bp로 개체마다 달랐다[3]. 일본 구마모토산 미토콘드리아 유전체는 20,180 bp이고 A 25.73%·T 42.41%·C 9.35%·G 22.49%로 AT 함량이 68.15%였다[2].\n\n"
"국내 군산·신안·영광 개체 21마리의 PCR 분석에서는 세 지역이 각각 다른 무리로 묶였고, 개체 사이 유전 거리는 최대 0.574였다[6]. 대만 시료에서 타우린 수송체(TAUT) cDNA 1971 bp가 클로닝되었고 657개 아미노산을 암호화했다[10]. 2026년 대만 백합 유전체(약 1,006 Mb, 염색체 19개)는 M. taiwanica로 동정된 개체의 것이며[5], 일본산 M. lusoria의 핵 유전체 조립 여부는 확인하지 못함.")

sec("safety","안전성",
"식약처 「식품원료 목록」에서 백합은 별도 조건 없는 '사용가능' 원료이다[1]. 건강기능식품 고시형 원료가 아니어서 고시 섭취 시 주의사항은 없으며, 백합만을 다룬 국내 공공기관의 패류독소·중금속·알레르기 정보는 확인하지 못함.\n\n"
"패류독소: 대만 실험에서 백합은 마비성 패류독소 생성 와편모조류(Alexandrium minutum)에 1 L당 10⁷ 세포 농도로 4일 노출되어도 가식부 1 g당 2 MU 미만으로 독소를 적게 쌓았다[24]. 중금속: 대만 남서부 양식 백합의 금속 농도는 Zn > Cu > Ni > Cd > Cr > Pb > Hg 순이었고 모두 대만 수산동물 위생기준보다 낮았고, 저자들은 성인 소비자에게 해롭지 않다고 보면서 조개를 100 g 넘게 먹는 사람은 예외로 두었다[22]. 흑족병 지역 양식 백합의 총비소는 중간 크기 7.62 μg/g·작은 크기 10.71 μg/g(건중량)이었고 무기비소 비율은 12.3–14.0%였다[21]. 수은 노출 실험에서 수은은 아가미와 내장에 많이 쌓였다[23].\n\n"
"잔류물질: 대만 양식 백합 일부에서 p,p'-DDE[25], 플루메퀸 0.02 mg/kg·클로르피리포스 0.03 mg/kg·트리클로르폰 0.02 mg/kg[26]이 검출되었으나 하루 섭취량 기준으로 위험은 낮게 평가되었다[25, 26]. 다환방향족탄화수소는 20.0 ± 5.8 ng/g(습중량)으로 조사 어패류 가운데 가장 낮았고[27], 일본 시판 조개 네 종에서는 한 마리당 평균 약 3개의 미세플라스틱이 나왔다[28]. 대만 시료의 종 동정은 다를 수 있다[4, 5].")

compounds=[
{"name":"Taurine","name_ko":"타우린","class":"아미노산 유도체(유리아미노산)","role":"nutrient","part":"아가미·외투막(동결건조)","content_text":"측정한 유리아미노산 중 약 20–40%(수치는 그림에만 있음); 35‰ 순화 시 외투막에서 증가","activity_ko":"세포 삼투 조절의 주 유기 삼투질로 작용한다[10, 11]","source":[10,11]},
{"name":"L-Alanine","name_ko":"알라닌","class":"아미노산","role":"nutrient","part":"아가미·외투막","content_text":"35‰ 순화 시 대조(20‰)보다 유의하게 증가(수치는 그림에만 있음)","activity_ko":"고염 환경에서 타우린과 함께 삼투 적응에 기여한다고 해석되었다[10]","source":[10]},
{"name":"N-Methyl-D-aspartic acid","name_ko":"N-메틸-D-아스파르트산(NMDA)","class":"D-아미노산 유도체","role":"bioactive","part":"초록에 조직 명시 없음","content_text":"29.3 nmol/g","activity_ko":"신경활성 D-아미노산으로, 생리적 의미는 아직 밝혀지지 않았다[13]","source":[13]},
{"name":"N-Methyl-L-glutamic acid","name_ko":"N-메틸-L-글루탐산","class":"아미노산 유도체","role":"bioactive","part":"초록에 조직 명시 없음","content_text":"13.8 nmol/g","activity_ko":"NMDA 유사체로 함께 정량되었다[13]","source":[13]},
{"name":"Docosahexaenoic acid","name_ko":"도코사헥사엔산(DHA)","class":"오메가-3 지방산","role":"nutrient","part":"가식부(발·외투막·내장)","content_text":"총지방산의 13.33–16.47%(안다만해 연안산)","activity_ko":"다가불포화지방산이 총지방산의 46.84–49.18%를 차지했다[12]","source":[12,19]},
{"name":"Eicosapentaenoic acid","name_ko":"에이코사펜타엔산(EPA)","class":"오메가-3 지방산","role":"nutrient","part":"가식부(발·외투막·내장)","content_text":"총지방산의 4.75–7.11%(안다만해 연안산)","activity_ko":"극성지질의 EPA 비율은 먹이 미세조류 조성을 따라 달라졌다[19]","source":[12,19]},
{"name":"Cholesterol","name_ko":"콜레스테롤","class":"스테롤","role":"nutrient","part":"가식부(발·외투막·내장)","content_text":"습중량의 0.07–0.21%","activity_ko":"부위별 함량 범위로 보고되었다[12]","source":[12]},
{"name":"L-Leucine","name_ko":"류신","class":"필수아미노산","role":"nutrient","part":"가식부(발·외투막·내장)","content_text":"30.91–36.96 mg/g 시료(필수아미노산 합계 167.66–187.63 mg/g 시료)","activity_ko":"리신과 함께 가장 많은 필수아미노산이었다[12]","source":[12]},
{"name":"L-Lysine","name_ko":"리신","class":"필수아미노산","role":"nutrient","part":"가식부(발·외투막·내장)","content_text":"35.24–36.03 mg/g 시료","activity_ko":"류신과 함께 가장 많은 필수아미노산이었다[12]","source":[12]},
{"name":"Lys-Asp-Leu-Glu-Leu","name_ko":"펩타이드 KDLEL","class":"펩타이드(오량체, 617.35 Da)","role":"bioactive","part":"살 건조분말의 protamex 가수분해물(1 kDa 이하 분획)","content_text":"정량값 없음 — 정제 분획의 주 피크로 동정(m/z 617.35, 머무름 시간 16.9분)","activity_ko":"라디칼 소거능이 큰 분획의 주성분이며, 이 분획은 비만 생쥐에서 지방 축적을 줄였다(동물 실험)[15]","source":[15]},
{"name":"Epidioxysterol","name_ko":"에피디옥시스테롤(입체이성질체 2종)","class":"스테롤 과산화물","role":"bioactive","part":"에틸아세테이트 분획","content_text":"함량 확인하지 못함","activity_ko":"HL-60 백혈병 세포에서 세포자멸사를 일으킨 활성 성분으로 보고되었다(세포 실험)[14]","source":[14]},
{"name":"Lysozyme","name_ko":"라이소자임(i형)","class":"효소 단백질","role":"bioactive","part":"초록에 조직 명시 없음","content_text":"함량 확인하지 못함; 아미노산 하나가 다른 동위효소 2종의 전체 서열 결정","activity_ko":"세균 세포벽 분해 활성이 다른 이매패 i형 라이소자임과 비슷했다[17]","source":[17]},
{"name":"Glucosylceramide","name_ko":"글루코실세라마이드 등 만노스 함유 당지질","class":"스핑고당지질","role":"bioactive","part":"전체 조직","content_text":"함량 확인하지 못함; Gal-Cer·Glc-Cer·Man(β1-4)Glc-Cer 등 구조 제안","activity_ko":"만노스를 포함한 당지질 구조가 새로 보고되었다[18]","source":[18]},
]

assays=[
{"role":"literature","compound":"Taurine","compound_ko":"타우린(유리아미노산)","part":"아가미·외투막","content":"측정 유리아미노산 중 약 20–40%; 개별 수치는 그림에만 있음 [10]","method":"아미노산 자동분석기(이온교환)",
 "conditions":{"instrument":"Beckman 6300 High Performance Amino Acid Analyzer","column":"","mobile_phase":"","gradient":"","flow":"","temp":"","detection":"","injection":"","sample_prep":"아가미·외투막을 떼어 10시간 동결건조, 2% 설포살리실산 1 mL와 4 ℃에서 48시간 반응, 30,000 g·4 ℃·30분 원심분리 후 상층액을 0.22 μm 필터로 거름","standard":"","linearity":"","lod":"","loq":"","recovery":""},
 "rationale":"백합 아가미·외투막에서 가장 많은 유리아미노산이며 염분 변화에 따라 함량이 달라져 삼투 조절 지표로 쓰였다. 시료는 대만 양식장 개체다[10].","source":[10],"url":D+"10.3389/fphys.2016.00368","source_kind":"paper"},
{"role":"literature","compound":"N-Methyl-D-aspartic acid","compound_ko":"N-메틸-D-아스파르트산(NMDA)","part":"초록에 조직 명시 없음","content":"29.3 nmol/g(N-메틸-L-글루탐산 13.8 nmol/g) [13]","method":"키랄 2차원 HPLC-형광(NBD-F 유도체화), 2D-HPLC-MS/MS로 확인",
 "conditions":{"instrument":"자동화 키랄 2차원 HPLC","column":"1차: 마이크로보어 모놀리식 ODS(0.53 mm i.d. × 1,000 mm); 2차: 내로보어 거울상 선택성 칼럼(1.5 mm i.d. × 150 또는 250 mm)","mobile_phase":"","gradient":"","flow":"","temp":"","detection":"형광(4-fluoro-7-nitro-2,1,3-benzoxadiazole 전처리 유도체)","injection":"","sample_prep":"NBD-F 칼럼 전 유도체화","standard":"","linearity":"","lod":"","loq":"하한 2.5 fmol","recovery":""},
 "rationale":"이매패에 있는 신경활성 D-아미노산 유도체를 거울상이성질체별로 정량한 방법이다. 전문 확인 못함 — 초록의 조건만 옮겼다[13].","source":[13],"url":D+"10.1016/j.chroma.2012.08.075","source_kind":"paper"},
{"role":"literature","compound":"Lys-Asp-Leu-Glu-Leu","compound_ko":"펩타이드 KDLEL","part":"살 건조분말 protamex 가수분해물(1 kDa 이하)","content":"정량값 없음 — 정제 분획의 주 피크(m/z 617.35, 머무름 시간 16.9분) [15]","method":"RP-HPLC 분획 후 ESI-Q-TOF MS/MS 서열 동정",
 "conditions":{"instrument":"Dionex Ultimate 3000 RP-HPLC; Micro Q-TOF III ESI 질량분석기","column":"YMC-Triart C18 ExRs, 250 × 4.6 mm, 5 µm","mobile_phase":"증류수와 0.1% 포름산 함유 메탄올","gradient":"메탄올 10–100%, 40분","flow":"1 mL/min","temp":"","detection":"UV 254·280 nm; ESI 양이온 모드, capillary 4000 V, 건조 질소 5.5 L/min·180 ℃, 주사 범위 m/z 50–2000, 충돌에너지 7 eV(아르곤)","injection":"20 μL","sample_prep":"건조 분말 50 g에 protamex 0.5 g, pH 6.0·60 ℃에서 24시간 분해, 100 ℃ 10분 효소 불활성화, 한외여과로 1 kDa 이하 분획, Sephadex G-25(2.5 × 70 cm, 증류수 1.5 mL/min)로 소분획","standard":"","linearity":"","lod":"","loq":"","recovery":""},
 "rationale":"항산화·항비만 동물 실험에 쓴 분획의 주성분으로 동정된 펩타이드다. 정량이 아닌 동정 조건이다. 시료는 여수 수산시장에서 산 백합이다[15].","source":[15],"url":D+"10.3390/ijms23074015","source_kind":"paper"},
]

nutrients=[{"form":"가식부(발·외투막·내장) — 안다만해 연안산 M. lusoria, 부위별 범위","basis":"습중량 %(논문 초록 값; 국가표준식품성분표 값은 확인하지 못함)","items":[
 {"name":"수분","value":"76.23–84.22","unit":"%"},{"name":"단백질","value":"9.09–12.75","unit":"%"},{"name":"탄수화물","value":"0.32–7.89","unit":"%"},{"name":"지방","value":"1.58–6.58","unit":"%"},{"name":"회분","value":"1.23–2.58","unit":"%"},{"name":"콜레스테롤","value":"0.07–0.21","unit":"%"}],"source":[12]}]

d={"slug":"meretrix-lusoria","name_ko":"백합","name_en":"Hard clam (Common orient clam)","scientific_name":"Meretrix lusoria","aliases":["Hard clam","Common orient clam","하마구리(hamaguri)"],
 "sections":secs,"compounds":compounds,"markers":[],"assays":assays,"nutrients":nutrients,"production":[],"gi":[],"orgs":[],"world":[],"sources":sources}
json.dump(d,open("/home/user/hfoodguide-wave3/docs/materials/meretrix-lusoria/dossier.json","w"),ensure_ascii=False,indent=1)
for s in secs: print(s["key"],len(s["body"]))
