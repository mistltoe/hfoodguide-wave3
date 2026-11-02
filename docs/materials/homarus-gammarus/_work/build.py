import json
from pathlib import Path

ACC = "2026-11-02"
P = "PubMed {pmid}"
S = []


def src(title, doi, pub, pmid=None, pmc=None, url=None, acc=ACC):
    n = len(S) + 1
    tag = f"PubMed {pmid}" + (f", {pmc}" if pmc else "") if pmid else ""
    S.append({"n": n, "title": title, "url": url or f"https://doi.org/{doi}",
              "publisher": f"{pub} ({tag})" if tag else pub, "accessed": acc})
    return n


src("식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 유럽바다가재(Homarus gammarus) 1행(수산물, 부위 '-', 사용가능, 사용 조건 없음, 이명 '유럽바닷가재, European lobster') 및 같은 속 아메리카바다가재(Homarus americanus)·냉동아메리카바다가재살 행(이명 '미국바닷가재, 랍스터') — 로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json",
    None, "식품의약품안전처", url="https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", acc="2026-10-13")  # 1
src("A High-quality Reference Genome and Tissue Expression Atlas for the European Lobster (Homarus gammarus). Genome Biol Evol 2026; evag138", "10.1093/gbe/evag138", "Genome Biology and Evolution", "42244022", "PMC13286009")  # 2
src("Absence of evidence is not evidence of absence: Nanopore sequencing and complete assembly of the European lobster (Homarus gammarus) mitogenome uncovers the missing nad2 and a new major gene cluster duplication. BMC Genomics 2019;20(1):335", "10.1186/s12864-019-5704-3", "BMC Genomics", "31053062", "PMC6500004")  # 3
src("Mitogenomic analysis of decapod crustacean phylogeny corroborates traditional views on their relationships. Mol Phylogenet Evol 2012;66(3):776-89", "10.1016/j.ympev.2012.11.002", "Molecular Phylogenetics and Evolution", "23202543")  # 4
src("Single nucleotide polymorphisms reveal a genetic cline across the north-east Atlantic and enable powerful population assignment in the European lobster. Evol Appl 2019;12(10):1881-1899", "10.1111/eva.12849", "Evolutionary Applications", "31700533", "PMC6824076")  # 5
src("Population Genetic Structure and Connectivity of the European Lobster Homarus gammarus in the Adriatic and Mediterranean Seas. Front Genet 2020;11:576023", "10.3389/fgene.2020.576023", "Frontiers in Genetics", "33365046", "PMC7750201")  # 6
src("Historical translocations and stocking alter the genetic structure of a Mediterranean lobster fishery. Ecol Evol 2020;10(12):5631-5636", "10.1002/ece3.6304", "Ecology and Evolution", "32607179", "PMC7319110")  # 7
src("Resampling-based evaluation of a 79-SNP panel for hybrid classification across generations: a case study in European lobster (Homarus gammarus). G3 (Bethesda) 2026;16(10)", "10.1093/g3journal/jkag206", "G3 Genes|Genomes|Genetics", "42522581", "PMC13643775")  # 8
src("Genotype Reconstruction of Paternity in European Lobsters (Homarus gammarus). PLoS One 2015;10(11):e0139585", "10.1371/journal.pone.0139585", "PLoS ONE", "26566271", "PMC4643931")  # 9
src("Technological creep masks continued decline in a lobster (Homarus gammarus) fishery over a century. Sci Rep 2022;12(1):3318", "10.1038/s41598-022-07293-2", "Scientific Reports", "35228599", "PMC8885706")  # 10
src("Protection from fishing improves body growth of an exploited species. Proc Biol Sci 2022;289(1987):20221718", "10.1098/rspb.2022.1718", "Proceedings of the Royal Society B", "36382520", "PMC9667365")  # 11
src("Marine protected areas rescue a sexually selected trait in European lobster. Evol Appl 2020;13(9):2222-2233", "10.1111/eva.12992", "Evolutionary Applications", "33005220", "PMC7513721")  # 12
src("Replacement of Antarctic krill (Euphausia superba) by extruded feeds with different proximate compositions: effects on growth, nutritional condition and digestive capacity of juvenile European lobsters (Homarus gammarus, L.). J Nutr Sci 2021;10:e36", "10.1017/jns.2021.27", "Journal of Nutritional Science (전문 확인)", "35401973", "PMC8965680")  # 13
src("Interactions of temperature and dietary composition on juvenile European lobster (Homarus gammarus, L.) energy metabolism and performance. Comp Biochem Physiol A 2021;260:111019", "10.1016/j.cbpa.2021.111019", "Comparative Biochemistry and Physiology A (초록만 확인)", "34146688")  # 14
src("European Lobster Larval Development and Fitness Under a Temperature Gradient and Ocean Acidification. Front Physiol 2022;13:809929", "10.3389/fphys.2022.809929", "Frontiers in Physiology", "35910579", "PMC9333128")  # 15
src("Ontogenetic shifts in fatty acid metabolic pathways of European lobster (Homarus gammarus) revealed by in vivo radiotracing. J Exp Biol 2026;229(15)", "10.1242/jeb.252202", "Journal of Experimental Biology (초록만 확인)", "42444547")  # 16
src("Nutritional quality of the edible tissues of European lobster Homarus gammarus and American lobster Homarus americanus. J Agric Food Chem 2009;57(9):3645-52", "10.1021/jf900237g", "Journal of Agricultural and Food Chemistry (초록만 확인)", "19334784")  # 17
src("Spatial distribution of mercury in seawater, sediment, and seafood from the Hardangerfjord ecosystem, Norway. Sci Total Environ 2019;667:622-637", "10.1016/j.scitotenv.2019.02.352", "Science of the Total Environment (초록만 확인)", "30833261")  # 18
src("Transfer across the human gut of environmental technetium in lobsters (Homarus gammarus L.) from the Irish Sea. J Radiol Prot 2001;21(1):21-9", "10.1088/0952-4746/21/1/302", "Journal of Radiological Protection (초록만 확인)", "11281526")  # 19
src("A model for the bioaccumulation of (99)Tc in lobsters (Homarus gammarus) from the West Cumbrian coast. J Environ Radioact 2003;67(3):219-33", "10.1016/S0265-931X(03)00002-X", "Journal of Environmental Radioactivity (초록만 확인)", "12691720")  # 20
src("Limited prevalence of gaffkaemia (Aerococcus viridans var. homari) isolated from wild-caught European lobsters Homarus gammarus in England and Wales. Dis Aquat Organ 2012;100(2):159-67", "10.3354/dao02491", "Diseases of Aquatic Organisms (초록만 확인)", "23186703")  # 21
src("The first clawed lobster virus Homarus gammarus nudivirus (HgNV n. sp.) expands the diversity of the Nudiviridae. Sci Rep 2019;9(1):10086", "10.1038/s41598-019-46008-y", "Scientific Reports", "31300678", "PMC6626001")  # 22
src("A comparison of the structure of American (Homarus americanus) and European (Homarus gammarus) lobster cuticle with particular reference to shell disease susceptibility. J Invertebr Pathol 2014;117:33-41", "10.1016/j.jip.2014.01.001", "Journal of Invertebrate Pathology (초록만 확인)", "24468664")  # 23
src("The molecular basis of the coloration mechanism in lobster shell: beta-crustacyanin at 3.2-A resolution. Proc Natl Acad Sci USA 2002;99(15):9795-800", "10.1073/pnas.152088999", "PNAS (초록만 확인)", "12119396", "PMC125020")  # 24
src("Structural characterization of recombinant crustacyanin subunits from the lobster Homarus americanus. Acta Crystallogr F 2012;68(Pt 8):846-53", "10.1107/S1744309112026103", "Acta Crystallographica Section F (초록만 확인)", "22869108", "PMC3412759")  # 25
src("Chemophysical Characterization of Carotenoproteins From Crustacean Shell Waste for Pharmaceutical Applications. Int J Food Sci 2026;2026:1042650", "10.1155/ijfo/1042650", "International Journal of Food Science (전문 확인)", "42312197", "PMC13269849")  # 26
src("Aspartic cathepsin D endopeptidase contributes to extracellular digestion in clawed lobsters Homarus americanus and Homarus gammarus. Mar Biotechnol 2010;12(6):696-707", "10.1007/s10126-010-9257-3", "Marine Biotechnology (초록만 확인)", "20169386")  # 27
src("Cold-adapted digestive aspartic protease of the clawed lobsters Homarus americanus and Homarus gammarus: biochemical characterization. Mar Biotechnol 2012;15(1):87-96", "10.1007/s10126-012-9461-4", "Marine Biotechnology (초록만 확인)", "22648335")  # 28
src("Changes in immune gene expression and resistance to bacterial infection in lobster (Homarus gammarus) post-larval stage VI following acute or chronic exposure to immune stimulating compounds. Mol Immunol 2006;44(4):443-50", "10.1016/j.molimm.2006.02.018", "Molecular Immunology (초록만 확인)", "16569431")  # 29
src("Assessing the Welfare of Spiny Lobsters and True Lobsters in Aquaria: Biology-Informed Best-Practice Guidelines for Captive Conditions. Animals 2025;15(16):2397", "10.3390/ani15162397", "Animals (초록만 확인)", "40867725", "PMC12383070")  # 30
src("Ageing European lobsters (Homarus gammarus) using DNA methylation of evolutionarily conserved ribosomal DNA. Evol Appl 2021;14(9):2305-2318", "10.1111/eva.13296", "Evolutionary Applications (초록만 확인)", "34603500", "PMC8477595")  # 31
src("Spatial and temporal axes impact ecology of the gut microbiome in juvenile European lobster (Homarus gammarus). ISME J 2020;14(2):531-543", "10.1038/s41396-019-0546-1", "The ISME Journal (초록만 확인)", "31676854", "PMC6976562")  # 32
src("The impact of anti-sea lice pesticides, azamethiphos and deltamethrin, on European lobster (Homarus gammarus) larvae in the Norwegian marine environment. Environ Pollut 2020;264:114725", "10.1016/j.envpol.2020.114725", "Environmental Pollution (초록만 확인)", "32388310")  # 33
src("Comparative toxicity of dissolved metals to early larval stages of Palaemon serratus, Maja squinado, and Homarus gammarus (Crustacea: Decapoda). Arch Environ Contam Toxicol 2000;39(3):345-51", "10.1007/s002440010114", "Archives of Environmental Contamination and Toxicology (초록만 확인)", "10948285")  # 34
src("Restorative function of offshore longline mussel farms with ecological benefits for commercial crustacean species. Sci Total Environ 2024;951:174987", "10.1016/j.scitotenv.2024.174987", "Science of the Total Environment (초록만 확인)", "39142406")  # 35
src("A Method of Solubilizing and Concentrating Astaxanthin and Other Carotenoids. Mar Drugs 2021;19(8):462", "10.3390/md19080462", "Marine Drugs (초록만 확인)", "34436301", "PMC8399374")  # 36
src("Effects of seawater alkalinity on calcium and acid-base regulation in juvenile European lobster (Homarus gammarus) during a moult cycle. Comp Biochem Physiol A 2016;193:22-8", "10.1016/j.cbpa.2015.12.002", "Comparative Biochemistry and Physiology A (초록만 확인)", "26691956")  # 37
src("Proteasomal activities in the claw muscle tissue of European lobster, Homarus gammarus, during larval development. J Comp Physiol B 2011;181(7):861-71", "10.1007/s00360-011-0574-2", "Journal of Comparative Physiology B (초록만 확인)", "21533820")  # 38
src("Short-term exposure to hydrogen peroxide induces mortality and alters exploratory behaviour of European lobster (Homarus gammarus). Ecotoxicol Environ Saf 2020;204:111111", "10.1016/j.ecoenv.2020.111111", "Ecotoxicology and Environmental Safety (초록만 확인)", "32795703")  # 39

sections = [
 ("overview", "한눈에 보기", """유럽바다가재(Homarus gammarus, European lobster)는 큰 집게를 가진 대형 십각류 갑각류로, 북동대서양과 지중해 연안에서 오래전부터 잡아 온 값비싼 수산물이다[2]. 식약처 「식품원료 목록」에는 '유럽바다가재'라는 이름의 수산물 원료로 올라 있으며, 쓸 수 있는 부위는 따로 정하지 않았고('-') 사용 조건 없이 '사용가능'이다[1]. 같은 목록에서 이명은 '유럽바닷가재, European lobster'이고, '랍스터'라는 이명은 이 종이 아니라 아메리카바다가재(H. americanus) 행에만 적혀 있다[1].

야생에서 보통 30–55년을 살고 최대 80년까지 산다고 보고되며, 평생 자라고 번식하며 잘린 다리를 다시 만든다[2]. 남유럽에서는 근육·간췌장·생식소를 먹는 고급 식품으로 여겨진다[17]. 남획으로 여러 지역 자원이 무너진 뒤 유럽 각국에서 부화장에서 기른 어린 개체를 풀어 자원을 늘리는 사업과 양식 연구가 이어지고 있다[2, 13]. 2026년에는 이 종의 고품질 참조 유전체(1.76 Gb)가 발표되었다[2]. 건강기능식품 고시형 원료의 원재료는 아니며, 국내 생산·수입 통계는 확인하지 못함."""),
 ("history", "이용 역사", """유럽바다가재는 북동대서양과 지중해 연안에서 오랫동안 어업 대상이 되어 온 종이다[2]. 1930년부터 1970년 사이 어획 압력이 커지면서 유럽 여러 곳의 개체군이 무너졌고, 이를 되살리려고 프랑스·영국·아일랜드·노르웨이·독일에서 어린 개체를 대량으로 방류하는 실험적 자원 증강 사업이 시작되었다[13].

1970년대에는 지중해 코르시카섬 주변에 프랑스 대서양 연안에서 옮겨 온 부화장 산 후기유생 수천 마리와 어미 일부를 풀었는데, 당시에는 생존·가입 여부를 살피는 계획이 없었다[7]. 훗날 코르시카에서 잡힌 20마리를 79개 SNP로 분석하자 13마리가 대서양 계통이 우세해, 방류가 지역 가입을 늘렸지만 유전 구조를 바꾼 것으로 해석되었다[7]. 독일 헬골란트 주변에서도 개체군이 무너져 대규모 재방류 사업이 이어졌다[15].

노르웨이의 한 어업에서는 1928–2019년 통발 기술 발달을 보정한 단위노력당어획량이 92% 줄어든 것으로 계산되었고, 보정하지 않으면 감소가 70%로 작게 보였다[10]. 국내에서 이 종을 들여와 먹기 시작한 시기와 경로는 확인하지 못함."""),
 ("biology", "종·형태·생태", """유럽바다가재는 집게가 큰 저서성 십각류로, 북쪽 노르웨이에서 모로코와 동지중해까지 분포한다[13]. 느리게 자라고 번식력이 몸 크기에 따라 달라 남획에 약하다[2]. 알에서 나온 1–3기 유생과 4기 후기유생은 물에 떠다니며, 5기부터 바닥에서 산다[16, 39].

갑각류는 탈피로 자라는데, 탈피 직후에는 몸 전체 칼슘의 45%가 벗은 껍데기와 함께 빠져나갔다[37]. 어른 개체는 탈피 전에 큰 집게 근육이 40–75% 줄어들며, 이때 칼슘 의존 단백질분해효소와 프로테아좀이 근육 분해를 돕는다[38]. 수컷의 몸 대비 집게 크기는 짝짓기 성공과 관련된 성선택 형질로 여겨진다[12]. 영국 남서부 암컷 34마리의 알 덩어리를 유전자로 조사한 결과 덩어리마다 수컷 한 마리가 수정시킨 것으로 나타났다[9].

위액에는 카텝신 D 계열의 산성 단백질분해효소가 있어 몸 밖 소화에 쓰이고, 그 mRNA는 굶기면 40% 줄었다[27]. 이 효소는 낮은 온도에서도 활성을 유지하는 저온 적응 성질을 보였다[28]. 영국 홍합 양식장 조사에서 이 종은 양식장 닻과 떨어진 홍합 더미를 은신처로 쓰며 2–283일 머물렀다[35]. 살아 있을 때 껍데기의 푸른빛은 단백질에 붙은 아스타잔틴에서 나온다[24]."""),
 ("related_species", "관련 종·이름", """가장 가까운 종은 같은 속의 아메리카바다가재(Homarus americanus)이며, 식약처 「식품원료 목록」에도 별도 원료(아메리카바다가재·냉동아메리카바다가재살)로 따로 올라 있다[1]. 두 종이 갈라진 시기는 유전체 단일 사본 유전자 25개로 약 2,600만 년 전(95% 구간 2,200만–3,000만 년 전)으로 추정되었다[2]. 이 문서는 아메리카바다가재 자료를 섞지 않으며, 두 종을 함께 다룬 연구는 유럽바다가재 결과만 옮겼다[17, 27].

유럽 바다에서는 들여온 아메리카바다가재와 토종 유럽바다가재의 잡종이 토종 자원과 어업 관리에 위험이 된다[8]. 79개 SNP 묶음은 두 종과 1세대 잡종은 잘 가렸지만, 유럽바다가재 쪽으로 여러 세대 역교배한 개체는 구분이 불확실했다[8]. 치명적 세균병인 가프케미아의 병원성 균주는 아메리카바다가재와 함께 영국에 들어왔다는 기존 견해가 유전형 분석으로 다시 뒷받침되었다[21].

어린 개체 비교에서 아메리카바다가재의 껍데기는 더 얇고 긁힘에 약했으며, 상처 가장자리의 세균 정착도 아메리카바다가재에서만 넓게 보였다[23]. 이름은 영어로 European lobster이고, 식품원료 목록의 국문 이명은 '유럽바닷가재'다[1]. 대한민국 국가생물종 목록의 국명 등재 여부는 확인하지 못함."""),
 ("cultivation", "어획·양식", """유럽바다가재는 미끼를 넣은 통발 같은 수동 어구로 잡으며, 노르웨이 어업에서는 한 칸 통발에서 두 칸 통발로 바뀌고 큰 개체도 잡히게 되면서 어획 효율이 크게 높아졌다[10, 11]. 통발 어업은 큰 집게를 가진 수컷을 골라 잡는 선택압을 주는데, 노르웨이 남부의 금어 해양보호구역 안 수컷은 같은 크기의 어업 구역 수컷보다 집게가 최대 8% 컸다[12]. 14년 보호한 해양보호구역에서는 밀도가 크게 늘었고, 암컷이 더 자주 탈피하고 탈피마다 더 많이 자랐다[11].

부화장에서는 유생을 18 ± 1 °C, 염분 34 ± 1 PSU의 탱크에서 해동 남극크릴을 먹여 기르고, 4기 후기유생부터 200 mL 칸으로 된 개별 사육 틀에 한 마리씩 나눠 기른 사례가 있다[13]. 이 연구에서 단백질 500 g/kg·탄수화물 237 g/kg·지질 119 g/kg 압출 사료가 남극크릴과 비슷한 성장과 영양 상태를 보였다[13]. 수온을 13 °C로 낮추면 사료 섭취와 복부의 글리코겐·포도당이 줄었고, 성장과 에너지 대사에 미친 영향은 탄수화물 위주 사료에서 더 컸다[14].

유생을 13–24 °C와 이산화탄소 농도 두 조건에서 기른 실험에서 높은 이산화탄소 조건은 생존율을 낮췄다[15]. 바다에 띄운 용기에서 기른 어린 개체의 장내 세균 군집은 육상 수조 개체보다 계통적으로 더 뭉쳐 있었다[32]. 노르웨이 연어 양식장의 바다이 구제 약제(아자메티포스·델타메트린)는 권장 처리 농도보다 낮은 농도에서 1·2기 유생에 급성 독성을 보였다[33]. 세계 어획량과 국내 수입량 통계는 확인하지 못함."""),
 ("processing", "가공·이용", """먹는 부위는 근육(꼬리·집게살)과 간췌장, 생식소이며, 근육과 생식소는 단백질이 많고 간췌장은 지방·콜레스테롤·열량이 높았다[17]. 이 연구는 모든 가식 부위가 필수아미노산의 좋은 공급원이며, 저지방·저콜레스테롤 식단에도 맞는 영양가를 지녔다고 결론지었다[17].

살아 있을 때 검푸른 껍데기는 단백질 크러스타시아닌에 붙은 아스타잔틴 때문이며, 결합 상태의 흡수 극대는 632 nm다[24]. 익힌 바닷가재의 주황빛은 단백질에서 풀린 아스타잔틴의 색(헥세인에서 흡수 극대 472 nm)이다[24]. 이 β-크러스타시아닌 결정 구조(PDB 1GKA)는 유럽바다가재의 것으로 분류되어 이후 계산 연구에 쓰였다[26].

가공 뒤 남는 머리·껍데기·알·간 등 부산물에는 단백질·키틴·지질·무기질·색소가 들어 있어 이용 연구가 이어진다[26]. 다만 껍데기 크러스타시아닌을 아스타잔틴 운반체로 본 연구는 컴퓨터 모의실험 결과이며 효능·안전성 검증은 앞으로의 과제로 남아 있다[26]. 유럽바다가재의 재조합 크러스타시아닌을 이용해 아스타잔틴을 물에 녹이고 다시 농축하는 방법도 보고되었다[36].

79개 SNP로 만든 판별 모형은 모형에 쓰지 않은 개체의 99.7%를 대서양·지중해 원산 해역으로 맞게 가려, 유통 과정의 원산지 추적 도구로 제안되었다[5]. 식당·수산시장 수조에서 집게를 묶고 밀집시켜 보관하는 관행은 복지 문제로 지적되었다[30]. 국내 유통 형태(활가재·냉동 등)와 가공 실적은 확인하지 못함."""),
 ("genetics", "유전 정보", """2026년 발표된 참조 유전체는 PacBio 긴 읽기로 조립한 1.76 Gb(스캐폴드 N50 1.82 Mb, BUSCO 완성도 97.6%)이며, 단백질 암호 유전자 23,223개가 주석되었다[2]. 반복 서열이 조립의 51.8%를 차지하고, 유세포분석으로 잰 유전체 크기(3.18–3.42 Gb)보다 조립이 훨씬 짧다[2]. 감수분열 염색체 수는 45–88개로 크게 달랐다[2]. 열 가지 조직의 RNA-seq로 조직별 발현 지도도 함께 만들었다[2]. 바닷가재속 계통에서는 면역(펜트락신·C형 렉틴)과 텔로미어 유지에 관련된 유전자군이 늘어난 것으로 나타났다[2].

미토콘드리아 유전체는 십각류 13종을 새로 해독한 계통 연구에서 거의 완전하게 읽혔다[4]. 장거리 PCR로 만든 앞선 미토콘드리아 유전체에는 nad2 유전자가 없다고 보고되었으나, 나노포어 긴 읽기로 다시 조립한 결과 nad2가 온전히 있었고 아메리카바다가재와 비슷한 배열에 큰 직렬 중복 구간이 더해져 있었다[3].

유럽 전역 38곳 1,278마리를 79개 SNP로 분석하자 대서양과 지중해 사이에 뚜렷한 계통 지리적 단절이 있었고, 북동대서양에는 유전적 경사가 나타났다[5]. 아드리아해 개체군은 사실상 하나로 섞여 있었고 전체 유전 분화는 낮았다(FST = 0.0062)[6]. 리보솜 DNA 메틸화를 이용한 나이 추정 모형은 0–51개월 개체에서 나이와 메틸화 비율 사이의 선형 관계를 보였다[31]."""),
 ("safety", "안전성", """식약처 「식품원료 목록」에서 유럽바다가재는 사용 조건 없는 '사용가능' 수산물 원료이며, 건강기능식품 고시형 원료가 아니어서 고시 섭취 시 주의사항은 없다[1]. 이 종을 따로 다룬 국내 공공기관의 알레르기·잔류물질·중금속 안내는 확인하지 못함.

갑각류 알레르기의 주요 원인 단백질인 트로포미오신에 대해, 이 종의 알레르겐을 다룬 논문은 PubMed에서 확인하지 못함(검색어 'Homarus gammarus' AND tropomyosin/allergen/allergy). 같은 속 아메리카바다가재 자료는 옮기지 않았으며, 이 종의 알레르기 근거는 확인하지 못함.

노르웨이 하르당에르피오르 조사에서 갑각류 중에는 안쪽 피오르의 유럽바다가재만 EU 수은 기준을 넘었다(0.62 mg/kg 생중량)[18]. 영국 셀라필드 재처리 시설 배출로 아일랜드해 개체의 가식부에 테크네튬-99가 농축된다[19, 20]. 성인 8명이 이 살을 먹은 실험에서 장 흡수율(f1)은 0.046–0.23으로, 국제방사선방호위원회 값 0.5보다 낮았다[19].

1기 유생의 48시간 반수치사농도는 수은 48 μg/L, 구리 46 μg/L, 카드뮴 34 μg/L로, 특히 구리·카드뮴에서 새우류(Palaemon serratus) 유생보다 훨씬 민감했다(사람 섭취 안전성과는 다른 유생 독성 자료)[34]. 잉글랜드·웨일스 야생 개체 952마리 중 가프케미아 균은 9건에서만 분리되었다[21]. 어린 개체의 간췌장에서는 집게 달린 바닷가재류에서 처음 보고된 자연 감염 바이러스 HgNV가 발견되었다[22]. 두 병원체의 사람 위해 자료는 확인하지 못함."""),
]

compounds = [
 {"name": "Astaxanthin", "name_ko": "아스타잔틴", "class": "카로티노이드(잔토필)", "role": "bioactive", "part": "껍데기(외골격)",
  "content_text": "크러스타시아닌 결합 상태 흡수 극대 632 nm, 유리 상태(헥세인) 472 nm; 함량은 확인하지 못함 [24]",
  "activity_ko": "단백질에 붙어 살아 있는 개체의 검푸른 색을 내고, 풀려나면 익힌 바닷가재의 주황빛이 된다[24]; 항산화 작용은 계산(도킹) 연구로만 제시되었다[26]", "source": [24, 26]},
 {"name": "Crustacyanin", "name_ko": "크러스타시아닌", "class": "카로티노이드 결합 단백질(리포칼린)", "role": "bioactive", "part": "껍데기(외골격)",
  "content_text": "β-크러스타시아닌 = A1·A3 아단위 이합체 + 아스타잔틴 2분자 [24]; α-크러스타시아닌 = β 단위 8개(아스타잔틴 16분자) [26]; 천연 아단위의 흡수 이동 85–95 nm [25]",
  "activity_ko": "아스타잔틴의 흡수 파장을 길게 옮겨(심색 이동) 껍데기 색을 조절한다[24, 25]; 재조합 단백질로 아스타잔틴을 물에 녹이는 데 쓰였다[36]", "source": [24, 25, 26, 36]},
 {"name": "Protein", "name_ko": "조단백질", "class": "단백질(일반성분)", "role": "nutrient", "part": "어린 개체 전신(양식 실험)",
  "content_text": "41–50%(사료군별, 원문 기준 표기 없음; 같은 표의 건물 20–29%·회분 32–43%) [13]",
  "activity_ko": "근육과 생식소는 단백질이 많은 가식 부위다[17]", "source": [13, 17]},
 {"name": "Lipid", "name_ko": "총지질", "class": "지질(일반성분)", "role": "nutrient", "part": "어린 개체 전신(양식 실험)",
  "content_text": "4–7%(사료군별, 원문 기준 표기 없음) [13]",
  "activity_ko": "어른 개체에서는 간췌장에 지방이 많다[17]", "source": [13, 17]},
 {"name": "Cholesterol", "name_ko": "콜레스테롤", "class": "스테롤", "role": "nutrient", "part": "간췌장·근육·생식소",
  "content_text": "간췌장에서 높음(수치는 초록에 없어 확인하지 못함) [17]",
  "activity_ko": "연구진은 가식 부위의 지방·콜레스테롤이 건강한 식단과 어울리는 수준이라 결론지었다[17]", "source": [17]},
 {"name": "Essential amino acids", "name_ko": "필수아미노산", "class": "아미노산", "role": "nutrient", "part": "근육·간췌장·생식소",
  "content_text": "모든 가식 부위가 좋은 공급원(수치는 초록에 없어 확인하지 못함) [17]",
  "activity_ko": "가식 부위 단백질의 영양 질을 평가하는 지표로 쓰였다[17]", "source": [17]},
 {"name": "Glycogen", "name_ko": "글리코겐", "class": "다당류(저장 탄수화물)", "role": "nutrient", "part": "어린 개체 두흉부·복부",
  "content_text": "수치는 초록에 없어 확인하지 못함; 13 °C에서 복부 글리코겐 감소 [14]",
  "activity_ko": "수온·사료 조성에 따른 에너지 대사 지표로 쓰였다[14]", "source": [14]},
 {"name": "Eicosapentaenoic acid", "name_ko": "에이코사펜타엔산(EPA)", "class": "n-3 장쇄 다불포화지방산", "role": "nutrient", "part": "유생·후기유생 전신",
  "content_text": "함량은 초록에 없어 확인하지 못함; 1기 유생이 EPA·ALA를 우선 흡수, ALA에서 EPA 합성 검출 [16]",
  "activity_ko": "유생 발달에 필요한 지방산으로, 몸 안 합성은 제한적이었다[16]", "source": [16]},
 {"name": "Docosahexaenoic acid", "name_ko": "도코사헥사엔산(DHA)", "class": "n-3 장쇄 다불포화지방산", "role": "nutrient", "part": "유생·후기유생 전신",
  "content_text": "함량은 초록에 없어 확인하지 못함; 몸 안 합성은 검출되지 않음 [16]",
  "activity_ko": "합성이 안 되어 유생 사료에 장쇄 다불포화지방산 보충이 필요하다고 제안되었다[16]", "source": [16]},
 {"name": "Phosphatidylcholine", "name_ko": "포스파티딜콜린", "class": "인지질(극성 지질)", "role": "nutrient", "part": "유생·후기유생 전신",
  "content_text": "표지 지방산이 주로 포스파티딜콜린·포스파티딜에탄올아민으로 에스터화됨(함량은 확인하지 못함) [16]",
  "activity_ko": "유생 지방산이 저장되는 주된 지질 분획이다[16]", "source": [16]},
 {"name": "Cathepsin D", "name_ko": "카텝신 D(산성 단백질분해효소)", "class": "아스파트산 단백질분해효소", "role": "bioactive", "part": "위액·중장선(간췌장)",
  "content_text": "이 종에서 굶김 뒤 카텝신 D1 mRNA 40% 감소 [27]",
  "activity_ko": "몸 밖(위 안) 소화에 쓰이는 소화 효소이며 저온에서도 활성이 유지된다[27, 28]", "source": [27, 28]},
 {"name": "Antimicrobial peptide", "name_ko": "항균 펩타이드(12.2 kDa)", "class": "면역 단백질", "role": "bioactive", "part": "후기유생 6기 전신",
  "content_text": "12.2 kDa 항균 펩타이드 유전자(amp) 전사량을 실시간 PCR로 측정 [29]",
  "activity_ko": "면역 자극 물질에 한 번 노출해서는 프로페놀옥시다제·β-글루칸 결합 단백질 유전자 발현이 유의하게 늘지 않았다[29]", "source": [29]},
 {"name": "Calcium", "name_ko": "칼슘", "class": "무기질", "role": "nutrient", "part": "어린 개체 전신·껍데기",
  "content_text": "탈피 직후 몸 전체 칼슘의 45%가 벗은 껍데기로 빠지고 11%만 연한 몸에 남음 [37]",
  "activity_ko": "탈피 뒤 껍데기를 다시 굳히는 데 쓰이며, 낮은 알칼리도 해수는 탈피 뒤 중탄산 흡수를 29% 줄였다[37]", "source": [37]},
]

empty = {k: "" for k in ["instrument", "column", "mobile_phase", "gradient", "flow", "temp", "detection", "injection", "sample_prep", "standard", "linearity", "lod", "loq", "recovery"]}
assays = [
 {"role": "literature", "compound": "Protein", "compound_ko": "조단백질", "part": "어린 개체 전신(사료 시험 8주 뒤)",
  "content": "41–50%(사료군별, 원문 기준 표기 없음) [13]", "method": "Lowry 기반 미량 단백질 정량 키트(분광광도법)",
  "conditions": {**empty, "detection": "750 nm 흡광(상용 Lowry 기반 미량 단백질 키트 BIO-RAD 500-0112)",
                 "sample_prep": "얼음물로 마취·치사 후 증류수로 헹궈 −80 °C 보관; 처리군별 6–12마리를 모아 분쇄(Krups Speedy Pro) 후 분석 반복 3회"},
  "rationale": "양식용 압출 사료가 어린 개체의 몸 조성에 주는 영향을 보는 일반성분 지표로 쓰였다. 원문은 검출 파장과 키트까지만 적고 표준물질·검출한계·회수율은 적지 않았으며, 한 묶음 시료의 분석 반복이라 통계 비교는 하지 않았다[13].",
  "source": [13], "url": "https://doi.org/10.1017/jns.2021.27", "source_kind": "paper"},
 {"role": "literature", "compound": "Lipid", "compound_ko": "총지질", "part": "어린 개체 전신(사료 시험 8주 뒤)",
  "content": "4–7%(사료군별, 원문 기준 표기 없음) [13]", "method": "Folch 추출 후 중량법",
  "conditions": {**empty, "detection": "중량법",
                 "sample_prep": "클로로포름–메탄올(2:1, 부피비)로 Folch 법 추출; 처리군별 6–12마리를 모아 분쇄 후 분석 반복 3회"},
  "rationale": "사료의 지질·탄수화물 비율에 따른 몸 지질 축적을 보는 지표로 쓰였다(500LOW 사료군이 지질 최고, 400HIGH 사료군이 최저)[13].",
  "source": [13], "url": "https://doi.org/10.1017/jns.2021.27", "source_kind": "paper"},
 {"role": "literature", "compound": "Mercury", "compound_ko": "총수은(오염 지표)", "part": "가식 조직(초록에 부위 표기 없음)",
  "content": "안쪽 피오르 유럽바다가재 0.62 mg/kg 생중량(EU 기준 초과) [18]", "method": "총수은·메틸수은 정량(분석 기기는 초록에 없음)",
  "conditions": dict(empty),
  "rationale": "피오르 오염원과의 거리에 따른 수산물 수은 축적을 비교하는 식품 안전 지표로 쓰였다. 전문 확인 못함 — 분석 조건 칸은 비워 두었다[18].",
  "source": [18], "url": "https://doi.org/10.1016/j.scitotenv.2019.02.352", "source_kind": "paper"},
]

d = {
 "slug": "homarus-gammarus", "name_ko": "유럽바다가재", "name_en": "European lobster", "scientific_name": "Homarus gammarus",
 "aliases": ["유럽바닷가재", "European lobster", "Homarus gammarus (Linnaeus, 1758)"],
 "sections": [{"key": k, "title": t, "body": b} for k, t, b in sections],
 "compounds": compounds, "markers": [], "assays": assays, "nutrients": [], "production": [], "world": [], "gi": [], "orgs": [],
 "sources": S,
}
out = Path(__file__).resolve().parents[1] / "dossier.json"
out.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for k, t, b in sections:
    print(k, len(b))
