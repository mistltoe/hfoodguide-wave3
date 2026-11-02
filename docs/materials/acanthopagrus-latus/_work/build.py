import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
A = "2026-11-02"
def P(n, title, doi=None, pub="", pmid=None):
    url = f"https://doi.org/{doi}" if doi else f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
    return {"n": n, "title": title, "url": url, "publisher": pub, "accessed": A}

sources = [
 {"n": 1, "title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — Acanthopagrus latus 행(새눈치, Yellowfin seabream, 수산물, 부위 '-', 사용가능, 사용 조건 없음; 같은 속 감성돔 Acanthopagrus schlegelii는 별도 행; data/raw/mfds_rawmtrl/I1020_20261013.json·docs/materials/acanthopagrus-latus/card.json)", "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
 P(2, "Review of the Acanthopagrus latus complex (Perciformes: Sparidae) with descriptions of three new species from the Indo-West Pacific Ocean. J Fish Biol 2013;83(1):64-95 (초록 확인)", "10.1111/jfb.12151", "Journal of Fish Biology (PubMed 23808693)"),
 P(3, "Analysis of key fishy odorants in crucian carp and yellowfin seabream. Food Chem X 2026;38:104261 (PMC 전문 확인)", "10.1016/j.fochx.2026.104261", "Food Chemistry: X, PMC13452400"),
 P(4, "Effects of Lysozyme-Supplemented Diets on Muscle Texture and Metabolite Profiles in Yellowfin Seabream. Aquac Nutr 2025:9977656 (PMC 전문 확인)", "10.1155/anu/9977656", "Aquaculture Nutrition, PMC12657072"),
 P(5, "Effects of Dietary GABA Levels on Growth, Muscle Quality, and Liver Lipid Profile: Insights from Lipidomics in Juvenile Yellowfin Seabream. Foods 2025;14(16):2761 (PMC 전문 확인, 표 수치는 본문에 없음)", "10.3390/foods14162761", "Foods (MDPI), PMC12385394"),
 P(6, "A chromosome-level genome assembly of the yellowfin seabream (Acanthopagrus latus; Hottuyn, 1782) provides insights into its osmoregulation and sex reversal. Genomics 2021;113(4):1617-1627", "10.1016/j.ygeno.2021.04.017", "Genomics (PubMed 33839268)"),
 P(7, "Chromosome-level Genome Assembly of Acanthopagrus latus Provides Insights into Salinity Stress Adaptation of Sparidae. Mar Biotechnol 2022;24(3):655-660", "10.1007/s10126-022-10119-x", "Marine Biotechnology (PubMed 35394576)"),
 P(8, "Complete mitochondrial DNA sequence of the yellowfin seabream Acanthopagrus latus and a genomic comparison among closely related sparid species. Mitochondrial DNA 2008;19(4):385-93", None, "Mitochondrial DNA (PubMed 19462512)", 19462512),
 P(9, "The complete mitochondrial genome of yellowfin seabream, Acanthopagrus latus (Percoiformes, Sparidae) from Beibu Bay. Mitochondrial DNA B Resour 2021;6(4):1313-1314", "10.1080/23802359.2021.1907804", "Mitochondrial DNA Part B, PMC8018338"),
 P(10, "Benefit-risk assessment of commonly consumed fish species from South China Sea based on methyl mercury and DHA. Environ Geochem Health 2019;41(5):2055-2066 (초록만 확인)", "10.1007/s10653-019-00254-1", "Environmental Geochemistry and Health (PubMed 30806845)"),
 P(11, "The role of intestinal microbiota of the marine fish (Acanthopagrus latus) in mercury biotransformation. Environ Pollut 2021;277:116768 (초록만 확인)", "10.1016/j.envpol.2021.116768", "Environmental Pollution (PubMed 33647808)"),
 P(12, "Arsenic and mercury in commercially valuable fish species from the Persian Gulf: influence of season and habitat. Food Chem Toxicol 2010;48(10):2945-50 (초록 확인; 2013년 분류 정리 이전의 페르시아만 'A. latus' 기록)", "10.1016/j.fct.2010.07.031", "Food and Chemical Toxicology (PubMed 20667462)"),
 P(13, "Polybrominated diphenyl ethers in three commercially important fish from the northwestern Arabian Gulf: occurrence, concentration, and profiles. Arch Environ Contam Toxicol 2011;60(4):636-42 (초록 확인; 2013년 분류 정리 이전의 걸프 'A. latus' 기록)", "10.1007/s00244-010-9579-1", "Archives of Environmental Contamination and Toxicology (PubMed 20730612)"),
 P(14, "Gonadal Transcriptome Analysis of Sex-Related Genes in the Protandrous Yellowfin Seabream (Acanthopagrus latus). Front Genet 2020;11:709", "10.3389/fgene.2020.00709", "Frontiers in Genetics, PMC7378800"),
 P(15, "Cloning and expression pattern of gsdf during the first maleness reproductive phase in the protandrous Acanthopagrus latus. Gen Comp Endocrinol 2015;217-218:71-80", "10.1016/j.ygcen.2015.02.018", "General and Comparative Endocrinology (PubMed 25736452)"),
 P(16, "Elevated estradiol-17β levels inhibit final oocyte maturation via G protein-coupled estrogen receptor (Gper) in yellowfin porgy, Acanthopagrus latus. Gen Comp Endocrinol 2020;299:113587", "10.1016/j.ygcen.2020.113587", "General and Comparative Endocrinology (PubMed 32827512)"),
 P(17, "Larval rearing and ontogeny of digestive enzyme activities in yellowfin seabream (Acanthopagrus latus, Houttuyn 1782). Comp Biochem Physiol A 2021;261:111044", "10.1016/j.cbpa.2021.111044", "Comparative Biochemistry and Physiology Part A (PubMed 34371185)"),
 P(18, "Scale Drop Disease Virus Associated Yellowfin Seabream (Acanthopagrus latus) Ascites Diseases, Zhuhai, Guangdong, Southern China: The First Description. Viruses 2021;13(8):1617", "10.3390/v13081617", "Viruses (MDPI), PMC8402775"),
 P(19, "Detection and Genomic Characterisation of Scale Drop Disease Virus (SDDV) in Farmed Yellowfin Seabream (Acanthopagrus latus) in Southern China. J Fish Dis 2025;48(12):e14161", "10.1111/jfd.14161", "Journal of Fish Diseases (PubMed 40539359)"),
 P(20, "Genetic Diversity and Population Structure of Acanthopagrus latus in the South China Sea. Animals (Basel) 2025;15(9):1295", "10.3390/ani15091295", "Animals (MDPI), PMC12071160"),
 P(21, "Genomic Insights into the Population Genetics and Adaptive Evolution of Yellow Seabream (Acanthopagrus latus) with Whole-Genome Resequencing. Animals (Basel) 2025;15(5):745", "10.3390/ani15050745", "Animals (MDPI), PMC11898413"),
 P(22, "Seascapes Shaped the Local Adaptation and Population Structure of South China Coast Yellowfin Seabream (Acanthopagrus latus). Mar Biotechnol 2024;26(1):60-73", "10.1007/s10126-023-10277-6", "Marine Biotechnology (PubMed 38147145)"),
 P(23, "Uncovering the genetic structure and evolutionary history of Acanthopagrus latus (Actinopterygii, Sparidae) using mitochondrial DNA and multivariate analyses: coastal populations in Central Vietnam. Biodivers Data J 2025;13:e164274", "10.3897/BDJ.13.e164274", "Biodiversity Data Journal, PMC12397771"),
 P(24, "Effects of domestication on the body morphology and genetic diversity of the yellowfin seabream (Acanthopagrus latus). Genomics 2026;118(5):111308", "10.1016/j.ygeno.2026.111308", "Genomics (PubMed 42595143)"),
 P(25, "Stock discrimination and connectivity assessment of yellowfin seabream (Acanthopagrus latus) in northern South China Sea using otolith elemental fingerprints. Saudi J Biol Sci 2018;25(6):1163-1169", "10.1016/j.sjbs.2017.09.006", "Saudi Journal of Biological Sciences, PMC6117167"),
 P(26, "Genome-Wide Microsatellites in Acanthopagrus latus: Development, Distribution, Characterization, and Polymorphism. Animals (Basel) 2024;14(24):3709", "10.3390/ani14243709", "Animals (MDPI), PMC11672618"),
 P(27, "[Anisakis simplex larvae: infection status in marine fishes for sale in Shantou]. Zhongguo Ji Sheng Chong Xue Yu Ji Sheng Chong Bing Za Zhi 2014;32(3):212-6 (초록 확인)", None, "중국기생충학·기생충병잡지 (PubMed 25223058)", 25223058),
 P(28, "Morphological and molecular characterization of Henneguya cystigena n. sp. (Cnidaria, Myxosporea) parasitizing the alimentary tract of yellowfin seabream, Acanthopagrus latus, in the East China Sea. Parasite 2025;32:51", "10.1051/parasite/2025048", "Parasite, PMC12355913"),
 P(29, "Acanthopagrus datnia (Hamilton, 1822), a senior synonym of Acanthopagrus longispinnis (Valenciennes, 1830) (Perciformes: Sparidae). Zootaxa 2020;4750(2)", "10.11646/zootaxa.4750.2.1", "Zootaxa (PubMed 32230470)"),
 P(30, "Morphology of the fertilizable mature egg in the Acanthopagrus latus, A. schlegeli and Sparus sarba (Teleostei: Perciformes: Sparidae). J Microsc 2008;232(3):442-52", "10.1111/j.1365-2818.2008.02139.x", "Journal of Microscopy (PubMed 19094021)"),
 P(31, "Effects of Density Stress During Transportation on the Antioxidant Activity and Immuno-Related Gene Expression in Yellowfin Seabream (Acanthopagrus latus Houttuyn, 1782). Genes (Basel) 2024;15(11):1479", "10.3390/genes15111479", "Genes (MDPI), PMC11593578"),
 P(32, "Molecular cloning and expression of yellowfin porgy (Acanthopagrus latus houttuyn) growth hormone cDNA. Comp Biochem Physiol B 1993;104(4):803-10", "10.1016/0305-0491(93)90216-r", "Comparative Biochemistry and Physiology B (PubMed 8472546)"),
 P(33, "Functional Characterization of the mstn2 Gene and Its Association with Growth Traits in the Yellowfin Seabream Acanthopagrus latus (Hottuyn, 1782). Genes (Basel) 2023;14(12):2142", "10.3390/genes14122142", "Genes (MDPI), PMC10742913"),
 P(34, "Henneguya lata n. sp. (Myxozoa: Myxobolidae), from the gills of yellowfin seabream Acanthopagrus latus in the Gulf of Tonkin, Vietnam. Parasitol Res 2021;120(3):877-885", "10.1007/s00436-020-07031-5", "Parasitology Research (PubMed 33409633)"),
]

S = {}
S["overview"] = ("한눈에 보기",
"새눈치(Acanthopagrus latus)는 도미과(Sparidae) Acanthopagrus속의 바닷물고기로, 식약처 「식품원료 목록」에 '새눈치'(영문 Yellowfin seabream)라는 원료명의 수산물로 올라 있다[1]. 이 목록에서 상태는 '사용가능'이고, 사용 부위는 따로 정하지 않은 '-'로 적혀 있으며 별도의 사용 조건은 없다[1]. 건강기능식품 고시형 원료의 원재료 목록에는 없어 식약처가 정한 지표성분도 없다[1].\n\n"
"영어로는 yellowfin seabream 또는 yellowfin porgy라고 부르며, 배지느러미·뒷지느러미·꼬리지느러미가 노란 것이 특징이다[2, 16]. 2013년 분류 정리 이후 좁은 뜻의 A. latus는 동아시아 대륙붕에만 사는 종으로 다시 정의되었다[2]. 남중국해 북부에서 경제적으로 가장 중요한 도미과 어종으로 소개되며, 바닷물과 민물을 오가는 광염성 어종이다[6]. 중국 양식 개체의 살을 분석한 연구는 이 종을 지방이 적고(5% 미만) 단백질이 많은(약 20%) 어종으로 분류했다[4]. 국내 공공기관의 새눈치 식품성분표 값은 이번 조사에서 확인하지 못함.")

S["history"] = ("이용·관리 역사",
"대만에서는 1990년대 초에 이미 새눈치(yellowfin porgy)의 성장호르몬 유전자를 복제한 연구가 발표되었다[32]. 중국에서는 인공 번식과 양식 기술이 자리 잡았으며, 광둥성 주하이는 이 종의 가장 중요한 양식 지역으로 소개된다[4, 19]. 중국 연구진은 남중국해의 자연 집단이 환경오염과 남획으로 크게 줄었다고 적었고, 최근 방류 사업 때문에 네 해역 집단이 유전적으로 섞여 있다고 보았다[20]. 남획과 기후변화로 자연 집단이 줄면서 양식 의존도가 높아졌다는 보고도 있다[24].\n\n"
"중국에서 새눈치는 붕어와 함께 전통 생선탕(어탕)의 주된 원료로 쓰인다고 소개되었다[3]. 같은 글은 중국 일부 지역에 산모의 젖 분비를 돕는다며 싱겁게 끓인 생선탕을 먹이는 풍습이 있다고 적었다[3]. 베트남 중부 연안에서도 상업적으로 중요한 어종이며, 남획과 서식지 훼손 위협을 받는다고 보고되었다[23]. 국내에서 새눈치를 언제부터 어떻게 이용해 왔는지는 확인하지 못함.")

S["biology"] = ("어종·형태·생태",
"2013년 재검토에 따르면 좁은 뜻의 새눈치는 노란 뒷지느러미 줄기 사이 막의 안쪽에 검은 줄무늬가 늘 있다는 점으로 근연종 A. arabicus와 구별된다[2]. 새눈치는 수컷으로 먼저 성숙한 뒤 암컷으로 바뀌는 웅성선숙 자웅동체로, 정소·난정소·난소의 전사체를 비교한 연구에서 성 관련 유전자 55개가 확인되었다[14]. 첫 수컷 생식기에는 생식소 체세포 유래 인자(gsdf)가 난정소에서 많이 발현되었다[15].\n\n"
"암컷의 난모세포는 비동시적으로 발달하고 여러 번 나누어 산란하며, 세 살 암컷은 산란기에 혈중 에스트라디올(E2) 농도가 가장 높았다[16]. 하구처럼 염분이 크고 자주 바뀌는 연안에 사는 광염성 어종이다[7]. 부화 직후 자어는 15일째까지 천천히 자라 4.7 mm에 이르고, 16–30일째에는 더 빨리 자라 7.5 mm가 되었다[17]. 이 시기 소화효소는 입이 열릴 때부터 검출되었지만 장의 성숙은 생후 한 달 안에 끝나지 않았다[17].")

S["related_species"] = ("관련 종·이름",
"식약처 「식품원료 목록」은 같은 속의 감성돔(Acanthopagrus schlegelii)을 새눈치와 별도의 원료로 올려 두었으며, 이 문서는 감성돔의 자료를 섞지 않았다[1]. 오랫동안 인도·서태평양 전역의 한 종으로 여겨진 A. latus는 2013년 동아시아의 A. latus, 벵골만의 A. longispinnis, 그리고 새로 기재된 A. morrisoni(호주 북서부), A. arabicus(중동–이란·파키스탄·인도 서해안), A. sheim(걸프)으로 나뉘었다[2]. 벵골만의 A. longispinnis는 2020년에 A. datnia의 이명으로 정리되었다[29]. Chrysophrys auripes, Chrysophrys xanthopoda 등은 새눈치의 뒤 이명으로 정리되었다[2].\n\n"
"그 결과 페르시아만·쿠웨이트 등에서 2013년 이전에 'A. latus'로 보고된 수은·비소·브롬화 난연제 자료는 지금 기준으로 다른 종일 수 있어, 이 문서는 그 수치를 새눈치 값으로 쓰지 않았다[2, 12, 13]. 새눈치의 미토콘드리아 유전체는 감성돔과 가깝게 묶이며[9], 시토크롬 b 서열은 도미과 종 판별 바코드로 쓸 수 있다고 보고되었다[8]. 새눈치·감성돔·Sparus sarba는 성숙란 표면의 난문 구조로도 구별되었다[30].")

S["cultivation"] = ("양식·어획",
"중국 어업 통계를 인용한 연구에 따르면 2023년 중국의 새눈치 양식 생산량은 147,314톤이었다[3]. 주하이에서는 주로 못(pond)에서 기르며, 2021–2023년 병든 양식 개체 73묶음 가운데 31묶음에서 비늘탈락병 바이러스(SDDV)가 검출되었다[19]. 이 바이러스는 새눈치 치어에 심한 복수를 일으키고 인위 감염에서 100% 폐사를 일으켰다[18]. 치어는 바닷물과 민물 양쪽에서 대량 양식에 쓰일 수 있다고 소개되며[20], 사료 실험은 염분 2–5‰의 못 가두리에서 이루어졌다[5].\n\n"
"종자 생산에서는 나노클로롭시스를 넣은 녹수 방식으로 자어를 기르고, 로티퍼에서 아르테미아, 미립자 사료 순으로 먹이를 바꿨다[17]. 치어 수송 실험에서는 운반 밀도에 따라 간·장의 항산화 효소 활성이 달라졌고, 고밀도에서는 면역 관련 유전자 발현이 늘었다[31]. 양식 개체는 자연산보다 몸이 넓고, 자연산은 체고가 높으며 유전적 다양성도 더 컸다[24]. 이석 원소 조성으로 양식·자연산을 판별한 결과 랜덤 포레스트의 정확도는 99.2%였다[25]. 국내 새눈치의 어획·양식 통계는 확인하지 못함.")

S["processing"] = ("가공·이용·품질",
"샤먼 시장에서 산 새눈치 살에서는 휘발성 성분 31종이 확인되었고, 알데하이드류가 215.17 μg/kg, 탄화수소류가 881.20 μg/kg으로 많았다[3]. 냄새 재구성·생략 실험으로 (E,Z)-2,6-노나디엔알, 노난알, (E,E)-2,4-데카디엔알, (E,E)-2,4-노나디엔알 네 가지가 새눈치 비린내의 핵심 성분으로 확인되었다[3]. 민물고기인 붕어보다 냄새가 약하고 구성도 단순했으며, 흙냄새 성분 2-MIB는 새눈치에서 검출되지 않았다[3].\n\n"
"양식 사료 연구에서는 라이소자임을 100 mg/kg 넣은 사료가 살의 경도와 말산·EPA·DHA 축적을 높였다고 보고되었다[4]. 대조군 근육의 회분은 2.83 g/100 g이었다[4]. GABA를 0.01% 넣은 사료는 근육의 필수·맛 아미노산과 DHA·EPA 등 장쇄 고도불포화지방산 비율을 높였다[5]. 같은 연구에서 근육 지질 분자는 2,101종이 확인되었고 트라이글리세라이드가 19.37%로 가장 많았다[5]. 반면 남중국해 집단 연구는 새눈치 살이 연하고 지방이 풍부하다고 소개해 표현이 엇갈린다[4, 20]. 이 결과는 사육 실험의 비교값이어서 시판 새눈치의 품질 기준으로 볼 수는 없다[4, 5]. 국내 가공품·제품 생산실적은 확인하지 못함.")

S["genetics"] = ("유전체·집단 유전",
"새눈치의 염색체 수준 유전체는 806 Mb였고 그중 732 Mb가 24개 염색체에 배치되었으며, 단백질 암호 유전자 19,631개가 주석되었다[6]. 다른 연구진의 조립본은 685.14 Mb, 예측 유전자 29,227개로 보고되어 두 조립본의 크기가 다르다[7]. 미토콘드리아 유전체 길이는 16,609 bp[8], 북부만(베이부만) 개체에서 16,635 bp로 보고되었다[9]. 유전체 전체에서 단순반복서열(SSR) 318,862개가 찾아져 육종용 표지 개발에 쓰였다[26].\n\n"
"남중국해 네 자연 집단 40마리의 재서열 분석에서는 지역별 무리가 나뉘지 않을 만큼 섞여 있었다[20]. 여섯 지역 60마리의 분석에서 뉴클레오타이드 다양도(π)는 0.003042–0.003155로 집단 간 분화가 낮았다[21]. 남중국 연안 15곳 92마리의 해경관 유전체 분석은 높은 유전자 흐름에도 두 개의 집단 구조를 찾았고, 염분 기울기와 관련된 삼투 조절 유전자를 제시했다[22]. 베트남 중부 세 집단의 미토콘드리아 조절 영역 일배체형 다양도는 0.993이었다[23]. 근육 성장 억제 유전자 mstn2의 SNP 세 곳은 체중·체장 등 성장 형질과 관련이 있었다[33].")

S["safety"] = ("안전성",
"남중국해 연안에서 흔히 먹는 어류 25종의 위해·편익 평가에서 새눈치는 갯장어(Muraenesox cinereus)와 함께 메틸수은 노출 위험이 있는 2종으로 꼽혔고, 많이 먹을 때 주의하라고 권고되었다[10]. 같은 연구에서 25종 전체의 주간 메틸수은 노출량은 0.12–2.11 μg/kg 체중이었다[10]. 새눈치 개별 값은 초록에서 확인하지 못함. 실험에서는 새눈치 장내 미생물이 수은의 메틸화와 탈메틸화에 관여해 몸속 수은 형태와 분포에 영향을 주었다[11]. 페르시아만 'A. latus' 자료는 다른 종일 수 있어 근거로 쓰지 않았다[2, 12].\n\n"
"중국 산터우 시장 어류 52종 조사에서 새눈치에서는 아니사키스 유충이 검출되지 않았다[27]. 동중국해 개체의 위벽에서는 점액포자충 Henneguya cystigena의 가낭이 새로 보고되었고[28], 베트남 개체의 아가미에서도 Henneguya lata 포낭이 발견되었다[34]. 양식장의 SDDV는 물고기 질병으로 보고되었으며 사람 감염 여부는 이 자료들에서 다루지 않았다[18, 19]. 새눈치에 대한 국내 공공기관의 알레르기·잔류물질 정보는 확인하지 못함.")

sections = [{"key": k, "title": t, "body": b} for k, (t, b) in S.items()]

def C(name, ko, cls, role, part, content, act, src):
    return {"name": name, "name_ko": ko, "class": cls, "role": role, "part": part, "content_text": content, "activity_ko": act, "source": src}
part3 = "근육(아가미·내장 제거)"
compounds = [
 C("(E,Z)-2,6-Nonadienal", "(E,Z)-2,6-노나디엔알", "알데하이드(휘발성)", "bioactive", part3, "OAV 571 (개별 농도는 표에만 있어 본문에서 확인하지 못함)", "새눈치에서 냄새 활성값이 가장 높았고, 빼면 비린내가 크게 줄어든 핵심 비린내 성분이다[3]", [3]),
 C("Nonanal", "노난알", "알데하이드(휘발성)", "bioactive", part3, "OAV 13", "빼면 비린내가 크게 줄고 풀·버섯 냄새와 기름 냄새도 바뀌어 전체 냄새에 넓게 영향을 주었다[3]", [3]),
 C("(E,E)-2,4-Nonadienal", "(E,E)-2,4-노나디엔알", "알데하이드(휘발성)", "bioactive", part3, "OAV 85", "새눈치 핵심 비린내 성분 네 가지 가운데 하나다[3]", [3]),
 C("(E,E)-2,4-Decadienal", "(E,E)-2,4-데카디엔알", "알데하이드(휘발성)", "bioactive", part3, "OAV 42", "새눈치 핵심 비린내 성분 네 가지 가운데 하나다[3]", [3]),
 C("1-Octen-3-ol", "1-옥텐-3-올", "알코올(휘발성)", "bioactive", part3, "OAV 38", "비린내 관련 성분이지만 새눈치 재구성 모델에서 빼도 냄새 차이가 유의하지 않았다[3]", [3]),
 C("Hexanal", "헥산알", "알데하이드(휘발성)", "bioactive", part3, "OAV 22", "신선한 새눈치에서는 농도가 낮아 비린내보다 풀냄새로 느껴졌다[3]", [3]),
 C("Decanal", "데칸알", "알데하이드(휘발성)", "bioactive", part3, "OAV 15", "GC-O에서 비린내로 묘사된 성분이다[3]", [3]),
 C("Docosahexaenoic acid", "DHA", "n-3 지방산", "nutrient", "근육", "개별 비율은 본문에서 확인하지 못함(GABA 0.01% 사료군에서 근육 비율이 0.10%군보다 유의하게 높음)", "남중국해 어류 위해·편익 평가에서 DHA 섭취 편익과 메틸수은 위해를 함께 따졌다[5, 10]", [5, 10]),
 C("Eicosapentaenoic acid", "EPA", "n-3 지방산", "nutrient", "근육", "개별 비율은 본문에서 확인하지 못함(사료 첨가 실험의 상대 비교)", "라이소자임 100 mg/kg 사료군에서 EPA·DHA 축적이 늘었다[4, 5]", [4, 5]),
 C("Phosphatidylethanolamine", "포스파티딜에탄올아민(PE)", "인지질", "nutrient", "근육", "근육 지질 중 14.28% (지질체학 상대 존재비)", "트라이글리세라이드·PC와 함께 근육 지질의 주요 분류군이다[5]", [5]),
 C("Phosphatidylcholine", "포스파티딜콜린(PC)", "인지질", "nutrient", "근육", "근육 지질 중 12.28% (지질체학 상대 존재비)", "라이소자임 사료군 근육에서 PC·PE가 많아졌다[4, 5]", [4, 5]),
 C("Cardiolipin", "카디오리핀(CL)", "인지질", "nutrient", "근육", "근육 지질 중 13.09% (지질체학 상대 존재비)", "미토콘드리아 특유의 인지질로, GABA 0.01% 사료군 근육에서 늘었다[5]", [5]),
 C("Malic acid", "말산", "유기산", "bioactive", "근육", "비표적 대사체 분석의 상대량만 보고(절대 함량 없음)", "라이소자임 사료군에서 늘어 맛에 영향을 줄 수 있는 유기산으로 설명되었다[4]", [4]),
 C("Citric acid", "시트르산", "유기산", "bioactive", "근육", "비표적 대사체 분석의 상대량만 보고(절대 함량 없음)", "라이소자임 사료군에서 줄었으며 해산물 신맛의 주요 유기산으로 소개되었다[4]", [4]),
]

assays = [
 {"role": "literature", "compound": "(E,Z)-2,6-Nonadienal and other volatile aldehydes", "compound_ko": "(E,Z)-2,6-노나디엔알 등 휘발성 비린내 성분",
  "part": part3, "content": "휘발성 성분 31종, 알데하이드류 215.17 μg/kg, 알코올류 69.47 μg/kg, 케톤류 28.32 μg/kg, 탄화수소류 881.20 μg/kg; OAV (E,Z)-2,6-노나디엔알 571, (E,E)-2,4-노나디엔알 85, (E,E)-2,4-데카디엔알 42, 1-옥텐-3-올 38, 헥산알 22, 데칸알 15, 노난알 13[3]",
  "method": "HS-SPME–GC-MS (SIM 정량), GC-MS-O",
  "conditions": {"instrument": "Shimadzu QP-2010Plus GC-MS; 냄새 판별은 Gerstel ODP-2 후각 포트(분할비 16:9)", "column": "Rtx-5MS, 30 m × 0.25 mm × 0.25 μm (Restek); GC-MS-O는 60 m × 0.25 mm × 0.25 μm",
   "mobile_phase": "운반 기체 헬륨(99.999%)", "gradient": "40 °C 2분 → 4 °C/min로 160 °C → 10 °C/min로 250 °C, 5분 유지", "flow": "1 mL/min (정유량)",
   "temp": "이온원 230 °C, 인터페이스 250 °C, 후각 포트 250 °C", "detection": "EI 70 eV, 질량 범위 35–350, 정량은 SIM", "injection": "스플릿리스, SPME 섬유 3분 열탈착",
   "sample_prep": "중국 샤먼 시장 활어(0.5–1 kg) 아가미·내장 제거 후 근육 15 g + 포화 NaCl 15 mL + 내부표준 사이클로헥사논(1 mg/mL) 5 μL를 60 mL 바이알에 넣고 60 °C 10분 평형 → 65 μm DVB/CAR/PDMS 섬유로 40분 흡착",
   "standard": "Sigma-Aldrich 표준품 검량선(내부표준 보정 외부표준법), 검량선 없는 성분은 내부표준 대비 반정량; C8–C20 알케인으로 RI 확인", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "냄새 활성값·후각 분석·재구성·생략 실험으로 새눈치 비린내의 핵심 성분 네 가지를 확인한 연구다[3]. 전문(Methods) 확인 — 검량선 수치는 보충 표(Table S2)에 있어 확인하지 못했고 검출·정량한계·회수율은 본문에 없음[3].",
  "source": [3], "url": "https://doi.org/10.1016/j.fochx.2026.104261", "source_kind": "paper"},
 {"role": "literature", "compound": "Docosahexaenoic acid", "compound_ko": "DHA 등 근육 지방산 조성", "part": "근육(양식 치어, 사료 실험)",
  "content": "개별 비율은 그림에만 있어 본문에서 확인하지 못함; 근육 지질 사슬 중 고도불포화 지방아실 41.7%(지질체학)[5]",
  "method": "GC (지방산 메틸에스터); 지질체학은 LC-MS",
  "conditions": {"instrument": "Agilent GC-7890B 가스크로마토그래프", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "", "injection": "",
   "sample_prep": "63일 사육한 치어(시작 무게 9.96 g) 근육을 클로로폼–메탄올(2:1)로 지질 추출 → 0.5 M KOH-메탄올과 15% 삼플루오린화붕소-메탄올로 메틸에스터화",
   "standard": "지방산 표준품(Sigma) 머무름 비교, 총 지방산 중 백분율", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "DHA·EPA 등 장쇄 n-3 지방산 비율은 생선 근육의 영양 품질 지표로 쓰였다[5]. 전문(Methods) 확인 — 칼럼·온도 조건은 인용 문헌으로 미뤄 본문에 없음[5].",
  "source": [5], "url": "https://doi.org/10.3390/foods14162761", "source_kind": "paper"},
 {"role": "literature", "compound": "Malic acid", "compound_ko": "말산·시트르산 등 근육 대사체", "part": "근육(양식 개체, 사료 실험)",
  "content": "비표적 분석으로 대사체 13,708개 검출, 1,902개 동정; 말산·시트르산은 상대량 비교만 보고[4]",
  "method": "UHPLC-Q-TOF-MS (비표적 대사체학)",
  "conditions": {"instrument": "AB SCIEX UHPLC-Triple TOF", "column": "ACQUITY UPLC HSS T3, 100 mm × 2.1 mm, 1.8 μm (Waters)",
   "mobile_phase": "A: 물 95%·아세토나이트릴 5%(0.1% 폼산), B: 아세토나이트릴 47.5%·아이소프로판올 47.5%·물 5%(0.1% 폼산)", "gradient": "", "flow": "0.40 mL/min", "temp": "칼럼 45 °C; 이온원 500 °C",
   "detection": "ESI 양·음이온, m/z 50–1200, 분무 전압 ±5500 V, 충돌 에너지 20–60 eV", "injection": "10 μL",
   "sample_prep": "중국 주하이 양식장 1년생 수컷(70.2 ± 4.6 g)을 4주 사육 후 근육 동결건조 → 0.5 g + 메탄올:물(4:1) 400 μL(내부표준 L-2-클로로페닐알라닌 0.02 mg/mL) 분쇄(−10 °C, 6분) → 초음파 30분(5 °C) → −20 °C 30분 → 13,000×g 15분 원심",
   "standard": "HMDB·METLIN·자체 DB와 MS/MS 대조(질량 오차 < 10 ppm), QC 시료 주기적 분석", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "말산·시트르산 등 유기산은 생선 신맛·감칠맛에 관여하는 맛 성분으로 다뤄졌다[4]. 전문(Methods) 확인 — 비표적 분석이라 기울기 조건·정량값·검출한계는 없음[4].",
  "source": [4], "url": "https://doi.org/10.1155/anu/9977656", "source_kind": "paper"},
]

world = [{"country": "중국", "metric": "production_t", "year": 2023, "value": 147314, "unit": "t", "note": "양식 생산량. 논문 서론이 중국 어업 통계를 인용한 값(통계 원문은 확인하지 못함)", "source": [3]}]

d = {"slug": "acanthopagrus-latus", "name_ko": "새눈치", "name_en": "Yellowfin seabream",
     "scientific_name": "Acanthopagrus latus (Houttuyn, 1782)",
     "aliases": ["새눈치", "Yellowfin seabream", "Yellowfin porgy", "Yellowfin sea bream", "Chrysophrys auripes", "Chrysophrys xanthopoda"],
     "sections": sections, "compounds": compounds, "markers": [], "assays": assays, "nutrients": [],
     "production": [], "world": world, "gi": [], "orgs": [], "sources": sources}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in sections: print(s["key"], len(s["body"]))
