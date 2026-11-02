import json
A="2026-11-02"
def pm(pmid,title,pub): return {"title":title,"url":f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/","publisher":pub,"accessed":A}
def pmc(pmcid,title,pub): return {"title":title,"url":f"https://pmc.ncbi.nlm.nih.gov/articles/{pmcid}/","publisher":pub,"accessed":A}
S=[
 {"title":"식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 전호잎(Anthriscus sylvestris (L.) Hoffm / Cerefolium sylvestre (L.) Besser, 식품원료 A코드) 및 건강기능식품(C코드) '전호잎추출물(제2022-25호)' 행","url":"https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020","publisher":"식품의약품안전처","accessed":"2026-10-13"},
 {"title":"식품의약품안전처 「식품 등의 생산실적」 2024–2025년판 — 건강기능식품 개별인정형 '전호잎추출물' 행(앱 파싱본 docs/stats/hf_items.csv, 금액 천원 단위)","url":"https://www.mfds.go.kr","publisher":"식품의약품안전처","accessed":"2026-10-12"},
 pmc("PMC6331990","Ethnomedicinal, Phytochemical and Pharmacological Profile of Anthriscus sylvestris as an Alternative Source for Anticancer Lignans. Molecules 2015;20(8):15003-22 (PMID 26287153, doi:10.3390/molecules200815003)","Molecules (MDPI, PMC)"),
 pmc("PMC11053937","Anthriscus sylvestris — Noxious Weed or Sustainable Source of Bioactive Lignans? Plants 2024;13(8):1087 (PMID 38674496, doi:10.3390/plants13081087)","Plants (MDPI, PMC)"),
 pmc("PMC9500830","Quantitative HPLC–UV Study of Lignans in Anthriscus sylvestris. Molecules 2022;27(18):6072 (PMID 36144804, doi:10.3390/molecules27186072)","Molecules (MDPI, PMC)"),
 pm("29377739","In Vivo and In Vitro Anti-Inflammatory Effects of Aqueous Extract of Anthriscus sylvestris Leaves. J Med Food 2018;21(6):585-595 (doi:10.1089/jmf.2017.4089) — 초록","J Med Food (PubMed)"),
 pm("29864899","Chondroprotective effects of aqueous extract of Anthriscus sylvestris leaves on osteoarthritis in vitro and in vivo through MAPKs and NF-κB signaling inhibition. Biomed Pharmacother 2018;103:1202-1211 (doi:10.1016/j.biopha.2018.04.183; 정정 PMID 32423657) — 초록","Biomed Pharmacother (PubMed)"),
 pm("17137110","Deoxypodophyllotoxin content and antioxidant activity of aerial parts of Anthriscus sylvestris Hoffm. Z Naturforsch C 2006;61(9-10):658-62 (doi:10.1515/znc-2006-9-1008) — 초록","Z Naturforsch C (PubMed)"),
 pm("21604818","Seasonal variations in the deoxypodophyllotoxin content and yield of Anthriscus sylvestris L. (Hoffm.) grown in the field and under controlled conditions. J Agric Food Chem 2011;59(15):8132-9 (doi:10.1021/jf200177q) — 초록","J Agric Food Chem (PubMed)"),
 pm("12214699","Volatile components from Anthriscus sylvestris (L.) Hoffm. J Chromatogr A 2002;966(1-2):233-8 (doi:10.1016/s0021-9673(02)00704-5) — 초록","J Chromatogr A (PubMed)"),
 pm("21889175","Identification of lignans and related compounds in Anthriscus sylvestris by LC-ESI-MS/MS and LC-SPE-NMR. Phytochemistry 2011;72(17):2172-9 (doi:10.1016/j.phytochem.2011.08.009) — 초록","Phytochemistry (PubMed)"),
 pm("34560578","Comprehensive study of Anthriscus sylvestris lignans. Phytochemistry 2021;192:112958 (doi:10.1016/j.phytochem.2021.112958) — 초록","Phytochemistry (PubMed)"),
 pm("19960413","Inhibitory effects of deoxypodophyllotoxin from Anthriscus sylvestris on human CYP2C9 and CYP3A4. Planta Med 2010;76(7):701-4 (doi:10.1055/s-0029-1240657) — 초록","Planta Med (PubMed)"),
 pm("18050240","Characterization of in vitro metabolites of deoxypodophyllotoxin in human and rat liver microsomes using LC/MS/MS. Rapid Commun Mass Spectrom 2008;22(1):52-8 (doi:10.1002/rcm.3325) — 초록","Rapid Commun Mass Spectrom (PubMed)"),
 pmc("PMC12381290","Phylogeographic evidence reveals multiple colonization events and a secondary contact zone in the Balkans for the Anthriscus sylvestris complex (Apiaceae). Sci Rep 2025;15:31497 (PMID 40858776, doi:10.1038/s41598-025-15409-7) — 초록","Scientific Reports (PMC)"),
 pmc("PMC8943078","Transcriptome analyses reveal the expression profile of genes related to lignan biosynthesis in Anthriscus sylvestris L. Hoffm. Gen. Physiol Mol Biol Plants 2022;28(2):333-346 (PMID 35400889, doi:10.1007/s12298-022-01156-w) — 초록","Physiol Mol Biol Plants (PMC)"),
 pm("37948767","Anthriscus sylvestris Deoxypodophyllotoxin Synthase Involved in the Podophyllotoxin Biosynthesis. Plant Cell Physiol 2023;64(12):1436-1448 (doi:10.1093/pcp/pcad103) — 초록","Plant Cell Physiol (PubMed)"),
 pm("36412832","Two O-Methyltransferases from Phylogenetically Unrelated Cow Parsley (Anthriscus sylvestris) and Hinoki-Asunaro (Thujopsis dolabrata var. hondae) as a Signature of Lineage-Specific Evolution in Lignan Biosynthesis. Plant Cell Physiol 2023;64(1):124-147 (doi:10.1093/pcp/pcac164) — 초록","Plant Cell Physiol (PubMed)"),
 pmc("PMC3375414","In vitro regeneration of wild chervil (Anthriscus sylvestris L.). In Vitro Cell Dev Biol Plant 2012;48(3):355-361 (PMID 22719203, doi:10.1007/s11627-011-9410-3) — 초록","In Vitro Cell Dev Biol Plant (PMC)"),
 pm("14648404","Lignan profiles of indoor-cultivated Anthriscus sylvestris. Planta Med 2003;69(10):959-61 (doi:10.1055/s-2003-45110) — 초록","Planta Med (PubMed)"),
 pm("21950154","Quantification of polyacetylenes in apiaceous plants by HPLC coupled with diode array detection. Z Naturforsch C 2011;66(7-8):319-27 (doi:10.1515/znc-2011-7-801) — 초록","Z Naturforsch C (PubMed)"),
 pmc("PMC12489727","Malonyl-Caffeoylquinic Acids and Malonyl-Flavonoid-Glucosides from Three Edible Apiaceae Plants. ACS Omega 2025;10(38):43656-43668 (PMID 41048795, doi:10.1021/acsomega.5c03770)","ACS Omega (PMC)"),
 pm("41643253","Conium Maculatum, one plant, four presentations: A case series. Am J Emerg Med 2026;103:26-29 (doi:10.1016/j.ajem.2026.01.037) — 초록","Am J Emerg Med (PubMed)"),
 pm("11205076","A fatal case of apparent water hemlock poisoning. Vet Hum Toxicol 2001;43(1):35-6 — 초록","Vet Hum Toxicol (PubMed)"),
 pmc("PMC9030527","Impact of Car Traffic on Metal Accumulation in Soils and Plants Growing Close to a Motorway (Eastern Slovakia). Toxics 2022;10(4):183 (PMID 35448444, doi:10.3390/toxics10040183) — 초록","Toxics (PMC)"),
 pm("30148990","Deoxypodophyllotoxin in Anthriscus sylvestris alleviates fat accumulation in the liver via AMP-activated protein kinase, impeding SREBP-1c signal. Chem Biol Interact 2018;294:151-157 (doi:10.1016/j.cbi.2018.08.025) — 초록","Chem Biol Interact (PubMed)"),
 pm("15187418","Dual inhibition of cyclooxygenases-2 and 5-lipoxygenase by deoxypodophyllotoxin in mouse bone marrow-derived mast cells. Biol Pharm Bull 2004;27(6):786-8 (doi:10.1248/bpb.27.786) — 초록","Biol Pharm Bull (PubMed)"),
 pm("39233161","Structural characterization, anti-aging activity and mechanisms investigation in vivo of a polysaccharide from Anthriscus sylvestris. Int J Biol Macromol 2024;279:135256 (doi:10.1016/j.ijbiomac.2024.135256) — 초록","Int J Biol Macromol (PubMed)"),
 {"title":"ClinicalTrials.gov NCT06535204 — Effects of Anthriscus Sylvestris Leaves on Mild Knee Osteoarthritis (등록 정보; 이 환경에서 원문 접속이 막혀 WebSearch 검색 요약으로만 확인)","url":"https://clinicaltrials.gov/study/NCT06535204","publisher":"미국 국립의학도서관(ClinicalTrials.gov)","accessed":A},
 pm("22715769","[Identification of Ginseng and its counterfeit by laser Raman spectroscopy]. Guang Pu Xue Yu Guang Pu Fen Xi 2012;32(4):989-92 — 초록(중국어 논문, 영문 초록)","Guang Pu Xue Yu Guang Pu Fen Xi (PubMed)"),
 pm("17603178","Lignans and coumarins from the roots of Anthriscus sylvestris and their increase of caspase-3 activity in HL-60 cells. Biol Pharm Bull 2007;30(7):1340-3 (doi:10.1248/bpb.30.1340) — 초록","Biol Pharm Bull (PubMed)"),
]
for i,s in enumerate(S,1): s["n"]=i
src=[{"n":s["n"],"title":s["title"],"url":s["url"],"publisher":s["publisher"],"accessed":s["accessed"]} for s in S]

sec=[]
def add(k,t,b): sec.append({"key":k,"title":t,"body":b})
add("overview","한눈에 보기",
"전호(Anthriscus sylvestris (L.) Hoffm.)는 산형과(Apiaceae) 전호속의 풀로, 영어로는 wild chervil 또는 cow parsley라 부른다[3]. 유럽과 온대 아시아가 원산지이고, 북아메리카·아프리카·뉴질랜드 등에는 들어가 퍼졌다[3]. 한국에도 널리 분포하는 여러해살이풀로 소개된다[6].\n\n"
"식품의약품안전처 「식품원료 목록」에서 전호는 '전호잎'이라는 원료명으로 올라 있으며, 식품원료(A코드)로 사용가능하고 사용 조건은 '사용가능부위 : 잎'이다[1]. 같은 목록에는 반들전호·동지라는 이름과 이명 Cerefolium sylvestre (L.) Besser가 함께 적혀 있다[1]. 또 건강기능식품(C코드) 개별인정 원료로 '전호잎추출물(제2022-25호)'이 올라 있다[1]. 이 원료의 인정 기능성 문구와 1일 섭취량은 원문으로 확인하지 못함.\n\n"
"전호는 포도필로톡신 계열 리그난이 많은 식물로 알려져 있고, 그중 데옥시포도필로톡신(안트리신)이 가장 중요한 성분으로 꼽힌다[3]. 리그난은 뿌리에 많고 지상부에는 그보다 몇 배 적다[5]. 전호에는 시나로사이드(루테올린-7-O-글루코사이드)와 클로로겐산 같은 폴리페놀이 많아 항산화 작용의 주요 활성 성분으로 소개된다[7].")
add("history","역사와 전통 이용",
"전호 뿌리는 일본에서 'Zengo'라는 생약으로, 중국에서는 'E Shen'이라는 이름의 보혈·강장약으로 쓰였다[4]. 한국 전통의학에서는 말린 뿌리를 해열·진통·진해·이뇨약으로 썼다[4]. 2018년 국내 연구는 뿌리를 기침약으로 써 온 것과 달리 잎의 생리활성은 아직 알려지지 않았다고 적었다[6].\n\n"
"유럽에서는 900–950년 무렵의 잉글랜드 의서에 전호가 들어간 암 치료 처방이 실려 있다고 한다[4]. 북유럽에서는 다른 산형과 야생식물과 함께 '파슬리'로 쓰였는데, 유럽의 전통 이용은 다른 산형과 식물과 혼동한 결과일 가능성이 크다는 지적이 있다[3]. 아일랜드와 튀니지에서는 지상부를 두통에, 세르비아에서는 꽃 물 추출물을 이뇨·강장에 썼다[3][4].\n\n"
"음식으로도 쓰였다[4]. 일본에서는 뿌리를 물에 담갔다가 으깨어 가루로 만들어 먹었고 어린 지상부도 가끔 먹었다[4]. 세르비아에서는 가루를 샐러드드레싱 향신료로, 튀르키예 동아나톨리아에서는 꽃 피기 전의 잎과 줄기를 허브 치즈에 넣었고, 영국에서는 국거리 채소로 썼다[4]. 대표 리그난인 데옥시포도필로톡신은 1940년에 이 식물의 뿌리에서 처음 분리되었다[4].")
add("biology","식물학적 특징",
"전호는 줄기가 곧게 서고 높이 0.3–1.5 m이며, 줄기에는 샘털이 없는 짧은 털이 있다[3]. 잎은 녹색에서 연한 붉은빛을 띠며 윤곽이 세모꼴이고 세 번 깃꼴로 갈라진다[3]. 꽃은 털 없는 겹산형꽃차례에 모여 피고, 꽃차례 가지는 (3–)6–12개이며 작은포는 4–6개, 총포는 없다[3]. 꽃잎은 크기가 다른 크림빛 흰색 5장이고 수술 5개, 암술대 2개가 있다[3]. 열매는 처음에 녹색이다가 익으면 갈색에서 붉은빛으로 변하고, 분과는 털이 없이 매끈하며 짧은 부리가 있다[3].\n\n"
"뿌리는 굵고 2 m까지 자란다고 한다[3]. 환경에 따라 한해살이·두해살이·짧은 여러해살이로 자라지만 한 번 꽃 피고 열매 맺으면 죽는(일회결실성) 종이다[3]. 생육지는 산울타리·길가·숲 가장자리·묵은 풀밭이며, 축축하거나 보통 습도의 흙(pH 6.2–7.0)을 좋아하고 반그늘부터 양지까지 자란다[3]. 원래 오리나무 강변숲이 주 서식지이고, 빽빽한 단일 군락을 이뤄 다른 식물을 밀어내는 잡초성이 있다[4].\n\n"
"신선한 잎을 수증기 증류한 정유는 모노테르펜이 약 70%이고, β-펠란드렌(39%)·β-미르센(17%)·사비넨(6.2%)이 주성분이다[10].")
add("related_species","분류와 근연종",
"전호속(Anthriscus)에는 POWO 기준으로 세계에 14종이 인정되며, 유럽에는 10종이 자란다고 정리되어 있다[4]. 전호는 이 속에서 가장 흔한 종이다[4]. 분자계통 연구에서 전호에는 적어도 5개 아종이 있으며, 예전에 별개 종으로 다루던 두 분류군이 지금은 아종으로 묶여 문헌에서 자주 혼동된다[3]. 속 이름은 그리스어에서 온 것으로, 옛날부터 향신료로 쓰인 챠빌(Anthriscus cerefolium)과 관련된 이름이며 전호는 '숲의 챠빌'이라는 뜻으로 풀이된다[3]. 챠빌은 식품원료 목록에서 전호와 다른 원료로 따로 올라 있다[1].\n\n"
"같은 산형과에는 아니스·당근·셀러리·고수·커민·회향·파슬리와 함께 독당근(hemlock)이 있다[3]. 독당근(Conium maculatum)은 파슬리·야생당근 같은 식용 산형과 식물과 매우 닮아 공중보건 위험이 크다[23]. 북아메리카에서는 '야생당근'이라 여기고 캐 먹은 산형과 식물에서 독미나리류 독소(시큐톡신)가 검출된 사망 사례가 보고되었다[24]. 중국 약재 시장에서는 전호 뿌리가 인삼 위품으로 유통되어 이를 분광법으로 감별하는 연구가 있었다[30].")
add("cultivation","재배와 생산",
"전호는 야생에서 채취하는 식물로 주로 다뤄지며, 북아메리카에서는 관상용 품종을 빼면 쓰임이 없고 해로운 침입 잡초로 취급된다[5]. 원산지와 도입지 모두에서 다년생 사료작물 밭과 목초지의 잡초가 되고 자연보호구역으로도 번지고 있다[4].\n\n"
"리그난 원료로 재배하는 연구에서, 노지 재배 개체는 2년째 3월에 데옥시포도필로톡신 함량이 가장 높았다(뿌리 0.15%, 지상부 0.03%, 건조중량)[9]. 생장실에서 키운 개체는 2년째 4월 뿌리(0.14%)와 1년째 7월 지상부(0.05%)에서 가장 높았다[9]. 노지 개체는 실내 개체보다 뿌리 무게가 최대 8배, 지상부 무게가 최대 30배 많았다[3]. 해발 1,200 m에서 자란 개체는 900 m 개체보다 지상부와 뿌리 모두 데옥시포도필로톡신이 두 배 이상 많았다[3].\n\n"
"배축 절편에서 캘러스를 유도해 줄기를 재분화시키고 온실 순화를 거쳐 밭에 옮긴 결과 생존율 100%로 꽃과 열매까지 정상이었다[19]. 통계청 농작물생산조사·농림축산식품부 특용작물 생산실적 파싱본에는 전호 항목이 없어 국내 재배 면적과 생산량은 확인하지 못함. 지리적 표시 등록도 확인하지 못함.")
add("processing","가공과 이용",
"식품원료 목록에서 전호는 잎만 쓸 수 있다[1]. 같은 산형과 식용식물을 다룬 연구는 전호(cow parsley)의 줄기를 절임으로 먹는다고 소개했다[22]. 잎의 물 추출물은 국내에서 항염증·연골 보호 효과를 보는 세포·동물 연구에 쓰였다[6][7]. 뿌리에서 얻은 다당류(평균 분자량 34.17 kDa)는 D-갈락토스로 노화를 유도한 쥐에서 항산화 효소 활성을 높였다[28]. 경증 무릎 골관절염 환자에게 잎 물 추출물을 먹인 임상시험이 등록되어 있다는 내용은 검색 요약으로만 확인했다[29].\n\n"
"건강기능식품 개별인정 원료 '전호잎추출물'(제2022-25호)은 식약처 「식품 등의 생산실적」에 2024년부터 집계된다[1][2]. 2024년 생산능력은 5톤, 생산액은 68,321천원(약 0.68억 원)이었다[2]. 2025년에는 생산량 1톤, 생산액 55,800천원(약 0.56억 원), 국내 판매량 1톤, 판매액 92,067천원(약 0.92억 원)이었다[2].\n\n"
"분석용 추출에서 지상부는 80% 메탄올일 때 리그난 수율이 가장 높았고, 메탄올 비율이 ±10% 달라지면 수율이 최대 48% 변했으며, 1회 추출 시간은 60분이 가장 좋았다[5]. 7-옥소아릴테트랄린과 불포화 디벤질부티로락톤 리그난은 불안정해 추출물을 빛을 막고 영하에 보관해야 한다[5]. 신선한 재료를 공기 건조하거나 동결 건조하면 휘발성 성분이 크게 줄었다[10].")
add("genetics","유전 정보",
"전호의 염색체 수는 2n = 16이 가장 흔하게 보고되며, 러시아 재료에서 2n = 18, 히말라야 재료에서 2n = 24도 보고되었다[4]. 296개 시료의 핵(nrDNA ITS, waxy 인트론)과 엽록체 표지(rpoB-trnC, trnS-trnG, psbA-trnH)를 분석한 연구는 전호 복합군이 중동에서 기원해 유럽으로 이동했고 발칸반도에서 2차 접촉이 일어났다고 보았다[15]. 이 연구는 엽록체 자료로 복합군의 나이를 약 172만 년, 유럽 집단 안의 분화 시작을 약 44만 년 전으로 추정했다[15].\n\n"
"꽃·잎·뿌리·줄기 전사체 분석에서 123,852개의 유전자 단편(unigene)이 얻어졌고, 리그난 합성 효소 유전자 일부는 데옥시포도필로톡신이 쌓이는 뿌리에서 가장 많이 발현되었다[16]. 야테인을 고리화해 데옥시포도필로톡신을 만드는 효소(AsDPS)는 2-옥소글루타르산 의존성 이산소화효소(2-ODD) 계열로, 히말라야 포도필룸의 같은 효소와 아미노산 서열이 40.8% 같았다[17]. 리그난 전구체를 메틸화하는 효소(AsSNYOMT)는 계통이 먼 측백나무과 식물의 효소와 서열 일치도가 33.8%에 그쳐 평행 진화의 예로 제시되었다[18]. 전호 개체 사이의 리그난 함량 차이는 집단 안의 유전적 차이를 반영하는 것으로 해석되었다[20].")
add("safety","안전성",
"전호에 많은 데옥시포도필로톡신은 사람 간 마이크로솜에서 약물대사효소 CYP2C9와 CYP3A4를 경쟁적으로 억제했다(IC50 각각 6.3, 9.2 µM)[13]. 이 성분은 사람 간에서 주로 CYP3A4와 CYP2C19로 대사된다[14]. 같은 계열의 포도필로톡신은 임상시험에서 심한 위장관 부작용 때문에 실패했다[3]. 식용 산형과 3종을 다룬 2025년 연구는 세포증식 억제 리그난을 가진 종(맥락상 전호)을 요리용 식물로 쓰는 데 안전성 우려가 있다고 적었다[22]. 데옥시포도필로톡신은 물고기 등 여러 동물에 독성을 보였다[4].\n\n"
"독당근(Conium maculatum)은 파슬리·야생당근과 닮아 잘못 먹는 일이 있고, 피페리딘 알칼로이드 때문에 호흡 마비까지 이를 수 있다[23]. 야생당근으로 알고 먹은 식물로 14세 소년이 숨진 독미나리류 중독 사례도 있다[24]. 전호를 독당근·독미나리로 혼동한 국내 사례나 공공기관의 전호 구별 안내는 확인하지 못함.\n\n"
"고속도로 옆에서 자란 전호 잎은 조사한 5종 가운데 카드뮴을 가장 잘 쌓았고, 교통 오염의 가장 좋은 지표 식물로 평가되었다[25]. 전호잎추출물의 개별인정 섭취 시 주의사항, 그리고 전호의 알레르기·잔류농약에 관한 공공기관 정보는 확인하지 못함.")

comp=[
 {"name":"Deoxypodophyllotoxin","name_ko":"데옥시포도필로톡신(안트리신)","class":"리그난(아릴테트랄린)","role":"marker","part":"뿌리·지상부","content_text":"뿌리 2.0–42.8 mg/g(중앙값 13.8 mg/g)[5]; 노지 지상부 최고 0.03%, 생장실 지상부 최고 0.05%(건조중량)[9]; 지상부 0.13%(해발 900 m)·0.33%(1,200 m)[3]","activity_ko":"COX-2·5-LOX 이중 억제(세포)[27]; 고지방식 쥐에서 간 지방 축적 감소[26]; CYP2C9·3A4 억제[13]","source":[3,5,9,13,26,27]},
 {"name":"Nemerosin","name_ko":"네메로신(안하이드로포도리졸)","class":"리그난(디벤질부티로락톤)","role":"bioactive","part":"뿌리","content_text":"뿌리 2.0–23.4 mg/g[5]","activity_ko":"전호의 주요 리그난 가운데 하나[12]","source":[5,12]},
 {"name":"Yatein","name_ko":"야테인","class":"리그난(디벤질부티로락톤)","role":"bioactive","part":"뿌리","content_text":"뿌리 1.1–18.5 mg/g[5]","activity_ko":"AsDPS 효소가 고리화해 데옥시포도필로톡신을 만드는 전구체[17]","source":[5,17]},
 {"name":"Podophyllotoxone","name_ko":"포도필로톡손","class":"리그난(7-옥소아릴테트랄린)","role":"bioactive","part":"뿌리","content_text":"뿌리 0.7–20.5 mg/g[5]","activity_ko":"뿌리의 주요 성분으로 처음 보고된 리그난 가운데 하나[11]; 추출물에서 불안정해 냉동·차광 보관 필요[5]","source":[5,11]},
 {"name":"Guayadequiol","name_ko":"구아야데퀴올","class":"리그난","role":"bioactive","part":"뿌리","content_text":"뿌리 0.8–8.3 mg/g[5]","activity_ko":"전호의 우세 리그난 가운데 하나로 보고[12]","source":[5,12]},
 {"name":"Dimethylmatairesinol","name_ko":"디메틸마타이레시놀","class":"리그난(디벤질부티로락톤)","role":"bioactive","part":"뿌리","content_text":"뿌리 0.1–5.2 mg/g[5]","activity_ko":"","source":[5]},
 {"name":"Podophyllotoxin","name_ko":"포도필로톡신","class":"리그난(아릴테트랄린)","role":"bioactive","part":"뿌리·지상부","content_text":"뿌리에서 0.01 μg/mg 미만의 미량[3]; 지상부 리그난 중 비율이 높은 편[4]","activity_ko":"에토포시드·테니포시드 반합성의 출발 물질[4]","source":[3,4]},
 {"name":"Luteolin 7-glucoside","name_ko":"루테올린-7-O-글루코사이드(시나로사이드)","class":"플라보노이드 배당체","role":"bioactive","part":"지상부·잎·꽃","content_text":"시든 꽃과 줄기에서 생체 1 kg당 0.124 g 분리[3]","activity_ko":"지상부 메탄올 추출물의 항산화 활성 분획 주성분[8]; 전호의 주요 항산화 활성 성분으로 언급[7]","source":[3,7,8]},
 {"name":"Chlorogenic acid","name_ko":"클로로겐산","class":"페놀산(카페오일퀸산)","role":"bioactive","part":"지상부·잎","content_text":"","activity_ko":"지상부 항산화 분획 주성분[8]; 전호의 주요 항산화 활성 성분으로 언급[7]","source":[7,8]},
 {"name":"beta-Phellandrene","name_ko":"β-펠란드렌","class":"모노테르펜(정유)","role":"bioactive","part":"잎·뿌리 정유","content_text":"잎 정유 39%, 뿌리 정유 45%(수증기 증류)[10]","activity_ko":"잎과 뿌리 정유의 주성분[10]","source":[10]},
 {"name":"beta-Myrcene","name_ko":"β-미르센","class":"모노테르펜(정유)","role":"bioactive","part":"잎 정유","content_text":"잎 정유 17%[10]","activity_ko":"","source":[10]},
 {"name":"Quercetin","name_ko":"퀘르세틴(루틴 포함)","class":"플라보노이드","role":"bioactive","part":"지상부","content_text":"","activity_ko":"지상부 70% 에탄올 추출물의 주요 항산화 플라보노이드(퀘르세틴·아피게닌·루틴)[3]","source":[3]},
 {"name":"Falcarindiol","name_ko":"팔카린디올","class":"폴리아세틸렌","role":"bioactive","part":"뿌리·열매","content_text":"","activity_ko":"HL-60 세포에서 카스파제-3 활성 증가[31]; 뿌리에서 팔카린디올-3-아세테이트도 처음 보고[21]","source":[3,21,31]},
]

assays=[
 {"role":"literature","compound":"Deoxypodophyllotoxin","compound_ko":"데옥시포도필로톡신(리그난 14종 동시 정량)","part":"지상부(herb)·뿌리, 공기 건조 분말",
  "content":"지상부 총 리그난 2.1–15.1 mg/g(중앙값 5.9 mg/g), 뿌리 총 리그난 11.3–106.2 mg/g(중앙값 40.0 mg/g); 뿌리 데옥시포도필로톡신 2.0–42.8 mg/g(중앙값 13.8 mg/g)[5]",
  "method":"HPLC-UV(DAD)",
  "conditions":{"instrument":"Agilent 1100 HPLC(진공 탈기기·이원 펌프·수동 주입기·칼럼 항온조·다이오드 어레이 검출기)",
   "column":"Zorbax Eclipse XDB-C18, 4.6 × 50 mm, 1.8 μm",
   "mobile_phase":"A: 0.1% 포름산 수용액, B: 아세토니트릴 중 35% 메탄올",
   "gradient":"0분 35% B → 14–16분 100% B, 후처리 3분",
   "flow":"1 mL/min","temp":"50 °C",
   "detection":"UV 220·280·330 nm(대역폭 16 nm), 기준 550 nm(대역폭 100 nm), 200–400 nm 전체 스캔; 대부분 280 nm, 7-옥소아릴테트랄린·불포화 디벤질부티로락톤은 330 nm",
   "injection":"5 μL",
   "sample_prep":"시료 180 mg을 80% 메탄올 2.4 mL로 1시간씩 4회 진탕 침출, 합쳐 10.0 mL로 맞춤; 지상부 추출물은 5.0 mL를 35 °C 감압 농축해 1.0 mL로 재용해; 4 °C 암소 보관",
   "standard":"전호 뿌리에서 직접 분리한 리그난 14종 표준품, 외부표준법(ESTD)",
   "linearity":"80% 메탄올 중 0.125–1000 μg/mL(8–10수준), R² ≥ 0.999",
   "lod":"",
   "loq":"바이알 기준 0.1–6.6 μg/mL(뿌리 0.006–0.37 mg/g, 지상부 0.0011–0.073 mg/g)",
   "recovery":"76.5–106.9%(지상부의 한 불안정 성분은 63.0%), 반복성 RSD < 10%"},
  "rationale":"데옥시포도필로톡신은 전호의 가장 중요한 성분으로 꼽히며[3], 이 연구는 지상부·뿌리 리그난 14종을 7분 안에 동시 정량하는 검증된 방법을 제시했다[5]. LoD 수치는 본문에서 확인하지 못해 비워 둠.",
  "source":[5],"url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC9500830/","source_kind":"paper"},
 {"role":"literature","compound":"Deoxypodophyllotoxin","compound_ko":"데옥시포도필로톡신(계절 변동)","part":"뿌리·지상부(노지·생장실 재배)",
  "content":"노지 재배 2년째 3월 뿌리 0.15%, 지상부 0.03%(건조중량); 생장실 재배 2년째 4월 뿌리 0.14%, 1년째 7월 지상부 0.05%[9]",
  "method":"",
  "conditions":{k:"" for k in ["instrument","column","mobile_phase","gradient","flow","temp","detection","injection","sample_prep","standard","linearity","lod","loq","recovery"]},
  "rationale":"전호의 주 리그난으로서 수확 시기를 정하는 지표로 쓰였다[9]. 전문 확인 못함 — 분석 기기·조건은 초록에 없어 비워 둠.",
  "source":[9],"url":"https://pubmed.ncbi.nlm.nih.gov/21604818/","source_kind":"paper"},
 {"role":"literature","compound":"Luteolin 7-glucoside","compound_ko":"루테올린-7-O-글루코사이드·클로로겐산(지상부 항산화 성분)","part":"지상부 메탄올 추출물",
  "content":"지상부 데옥시포도필로톡신 함량은 뿌리의 절반 이하[8]; 개별 함량은 초록에 없음",
  "method":"HPLC",
  "conditions":{k:"" for k in ["instrument","column","mobile_phase","gradient","flow","temp","detection","injection","sample_prep","standard","linearity","lod","loq","recovery"]},
  "rationale":"DPPH 항산화 활성을 따라 분획했을 때 활성 분획의 주성분이 루테올린-7-O-글루코사이드와 클로로겐산이었다[8]. 전문 확인 못함 — 조건 칸은 비워 둠.",
  "source":[8],"url":"https://pubmed.ncbi.nlm.nih.gov/17137110/","source_kind":"paper"},
]

d={"slug":"anthriscus-sylvestris","name_ko":"전호","name_en":"Wild chervil (cow parsley)",
 "scientific_name":"Anthriscus sylvestris (L.) Hoffm.",
 "aliases":["전호잎","반들전호","동지","wild chervil","cow parsley","keck","wild beaked parsley","woodland chervil","Cerefolium sylvestre (L.) Besser"],
 "sections":sec,"compounds":comp,"markers":[],"assays":assays,"nutrients":[],"production":[],"world":[],"gi":[],"orgs":[],"sources":src}
json.dump(d,open("/home/user/hfoodguide-wave3/docs/materials/anthriscus-sylvestris/dossier.json","w"),ensure_ascii=False,indent=1)
for s in sec: print(s["key"],len(s["body"]))
