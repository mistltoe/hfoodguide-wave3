import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
A = "2026-11-02"
def pm(pmid, title, journal, pmc=None):
    url = f"https://pmc.ncbi.nlm.nih.gov/articles/{pmc}/" if pmc else f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
    pub = f"{journal} ({'PubMed Central' if pmc else 'PubMed'})"
    return {"title": f"{title} (PMID {pmid})", "url": url, "publisher": pub, "accessed": A}
I1020 = "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020"
S = [
 {"title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 산복사열매(Prunus davidiana (Carriere) Franchet/ Amygdalus communis Bunge), 사용가능, '사용가능부위 : 열매(씨앗 제외)', 다른 이름 산복숭아, 영문명 Chinese wild peach", "url": I1020, "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
 {"title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 같은 종·근연종 행 대조: 산복사씨앗·산복사잎(사용불가), 복사나무열매(P. persica, 사용가능, 열매(씨앗 제외)), 복숭아꽃·복숭아나무꽃(제한적사용, 꽃), 감복숭잎(사용불가) (로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json)", "url": I1020, "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
 {"title": "식약처 고시 제2026-43호 「건강기능식품의 기준 및 규격」 제1~제3 원문 — 산복사·도인(桃仁)·복숭아 항목 검색(고시형 원료에서 찾지 못함) (로컬 원문 docs/refs/MFDS/건강기능식품의기준및규격_2026-43_제1~제3.txt)", "url": "https://www.mfds.go.kr/brd/m_211/view.do?seq=14973", "publisher": "식품의약품안전처", "accessed": A},
 pm("36376246", "Phenolic Compounds from the Fruits of Prunus davidiana (Rosaceae) and Their Antioxidant Activities. Chem Biodivers. 2023;20(1):e202200823 (PubMed 에 초록 본문 없음, 제목·키워드만 확인)", "Chemistry & Biodiversity"),
 pm("27238939", "Optimization of Hyaluronidase Inhibition Activity from Prunus davidiana (Carriere) Franch Fruit Extract Fermented by its Isolated Bacillus subtilis Strain SPF4211. J Microbiol Biotechnol. 2016;26(9):1527-32 (초록만 확인)", "Journal of Microbiology and Biotechnology"),
 {"title": "Kew Plants of the World Online — Prunus davidiana (자생 범위 'China to Korea'; 페이지를 직접 열지 못하고 WebSearch 검색 요약으로만 확인)", "url": "https://powo.science.kew.org/taxon/729634-1", "publisher": "Royal Botanic Gardens, Kew (WebSearch 요약)", "accessed": A},
 {"title": "산복사나무 열매의 트리테르페노이드(ursolic acid, corosolic acid, α-amyrin) 분리 보고 — 국내 학술지 논문(koreascience 원문은 열지 못하고 WebSearch 검색 요약으로만 확인)", "url": "https://koreascience.kr/article/JAKO201620340444477.pdf", "publisher": "koreascience (WebSearch 요약)", "accessed": A},
 pm("39201267", "Antioxidant Activity and Preclinical Safety of Semen Persicae Extract. Int J Mol Sci. 2024;25(16):8580 (전문 확인)", "International Journal of Molecular Sciences", "PMC11354697"),
 pm("23985009", "Aromatic glucosides from the seeds of Prunus davidiana. J Nat Prod. 2013;76(9):1528-34 (초록만 확인)", "Journal of Natural Products"),
 pm("1896517", "Improvement of hyperglycemia and hyperlipemia in streptozotocin-diabetic rats by a methanolic extract of Prunus davidiana stems and its main component, prunin. Planta Med. 1991;57(3):208-11 (초록만 확인)", "Planta Medica"),
 pm("2045817", "Antihyperlipidemic effect of flavonoids from Prunus davidiana. J Nat Prod. 1991;54(1):218-24 (초록만 확인)", "Journal of Natural Products"),
 pm("10319120", "Hypolipemic and hypoglycemic activities of Prunus davidiana in high fat-fed rats. Arch Pharm Res. 1991;14(1):44-7 (초록만 확인)", "Archives of Pharmacal Research"),
 pm("14609128", "Inhibitory activity of flavonoids from Prunus davidiana and other flavonoids on total ROS and hydroxyl radical generation. Arch Pharm Res. 2003;26(10):809-15 (초록만 확인)", "Archives of Pharmacal Research"),
 pm("27798765", "Prunin is a highly potent flavonoid from Prunus davidiana stems that inhibits protein tyrosine phosphatase 1B and stimulates glucose uptake in insulin-resistant HepG2 cells. Arch Pharm Res. 2017;40(1):37-48 (초록만 확인)", "Archives of Pharmacal Research"),
 pm("29901171", "Sipi soup inhibits cancer-associated fibroblast activation and the inflammatory process by downregulating long non-coding RNA HIPK1-AS. Mol Med Rep. 2018;18(2):1361-1368 (초록만 확인)", "Molecular Medicine Reports"),
 pm("42616448", "Structural Characterization, Physicochemical Properties, and Ameliorating Effect on Age-Related Constipation of an Arabinogalactan from Peach Gum. J Agric Food Chem. 2026;74(32):25164-25182 (초록만 확인)", "Journal of Agricultural and Food Chemistry"),
 pm("29556764", "Extreme phenophase delays and their relationship with natural forcings in Beijing over the past 260 years. Int J Biometeorol. 2018;62(7):1229-1239 (초록만 확인)", "International Journal of Biometeorology"),
 pm("26546082", "Seed trait-mediated selection by rodents affects mutualistic interactions and seedling recruitment of co-occurring tree species. Oecologia. 2016;180(2):475-84 (초록만 확인)", "Oecologia"),
 pm("15159547", "Comparative mapping and marker-assisted selection in Rosaceae fruit crops. Proc Natl Acad Sci U S A. 2004;101(26):9891-6", "PNAS", "PMC470769"),
 pm("34593767", "Chromosome-level genome assemblies of five Prunus species and genome-wide association studies for key agronomic traits in peach. Hortic Res. 2021;8(1):213", "Horticulture Research", "PMC8484544"),
 pm("39451079", "Haplotype-resolved genome of a heterozygous wild peach reveals the PdaWRKY4-PdaCYP716A1 module mediates resistance to aphids by regulating betulin biosynthesis. J Integr Plant Biol. 2024;66(12):2716-2735 (초록만 확인)", "Journal of Integrative Plant Biology"),
 pm("35698132", "Chromosome-level genome assemblies of four wild peach species provide insights into genome evolution and genetic basis of stress resistance. BMC Biol. 2022;20(1):139", "BMC Biology", "PMC9195245"),
 pm("40263939", "Panvariome and pangenome of 1,020 global peach accessions shed light on evolution patterns, hidden natural variations, and efficient gene discovery. Mol Plant. 2025;18(6):995-1013 (초록만 확인)", "Molecular Plant"),
 pm("33490544", "Complete Chloroplast Genome Sequence Of Prunus davidiana (Rosaceae). Mitochondrial DNA B Resour. 2018;3(2):888-889", "Mitochondrial DNA Part B", "PMC7801015"),
 pm("34493218", "The chloroplast genome of Amygdalus L. (Rosaceae) reveals the phylogenetic relationship and divergence time. BMC Genomics. 2021;22(1):645", "BMC Genomics", "PMC8425060"),
 pm("40212874", "Assembly and analysis of the complete mitochondrial genome of Prunus davidiana (Rosaceae). Front Plant Sci. 2025;16:1558619", "Frontiers in Plant Science", "PMC11983640"),
 pm("12845438", "The potential of Prunus davidiana for introgression into peach [Prunus persica (L.) Batsch] assessed by comparative mapping. Theor Appl Genet. 2003;107(2):227-38 (초록만 확인)", "Theoretical and Applied Genetics"),
 pm("15666162", "Analogues of virus resistance genes map to QTLs for resistance to sharka disease in Prunus davidiana. Mol Genet Genomics. 2005;272(6):680-9 (초록만 확인)", "Molecular Genetics and Genomics"),
 pm("21897441", "Co-localisation of host plant resistance QTLs affecting the performance and feeding behaviour of the aphid Myzus persicae in the peach tree. Heredity. 2012;108(3):292-301", "Heredity", "PMC3282398"),
 pm("36173088", "Betulin, Synthesized by [유전자명], Is a Key Endogenous Defensive Metabolite of Peach against Aphids. J Agric Food Chem. 2022;70(40):12865-12877 (제목 속 유전자명은 PubMed 메타데이터에서 빠져 확인하지 못함; 초록만 확인)", "Journal of Agricultural and Food Chemistry"),
 pm("15168024", "QTL analysis of quality traits in an advanced backcross between Prunus persica cultivars and the wild relative species P. davidiana. Theor Appl Genet. 2004;109(4):884-97 (초록만 확인)", "Theoretical and Applied Genetics"),
 pm("42399333", "Omics-based study of salt stress mechanisms in mountain peach (Prunus davidiana Carr.) in Northwest China. Sci Rep. 2026 (초록만 확인)", "Scientific Reports"),
 pm("20952094", "Metabolic response in roots of Prunus rootstocks submitted to iron chlorosis. J Plant Physiol. 2011;168(5):415-23 (초록만 확인)", "Journal of Plant Physiology"),
 pm("25106821", "Unraveling the mechanism underlying the glycosylation and methylation of anthocyanins in peach. Plant Physiol. 2014;166(2):1044-58", "Plant Physiology", "PMC4213075"),
 pm("25729941", "Diversity, population structure, and evolution of local peach cultivars in China identified by simple sequence repeats. Genet Mol Res. 2015;14(1):101-17 (초록만 확인)", "Genetics and Molecular Research"),
]
for i, s in enumerate(S, 1):
    s["n"] = i
S = [{"n": s["n"], **{k: s[k] for k in ("title", "url", "publisher", "accessed")}} for s in S]

sec = {}
sec["overview"] = ("한눈에 보기",
"산복사(Prunus davidiana)는 장미과 벚나무속의 야생 복숭아류로, 재배 복숭아(P. persica)와 매우 가까운 종이다[20, 22, 27]. "
"식약처 「식품원료 목록」에는 '산복사열매'가 사용가능 원료로 올라 있으며 사용 조건은 '사용가능부위 : 열매(씨앗 제외)', 다른 이름은 산복숭아, 영문명은 Chinese wild peach다[1]. "
"같은 목록에서 산복사씨앗과 산복사잎은 '사용불가'로 분류되어 있어, 식품으로 쓸 수 있는 부위는 씨를 뺀 열매뿐이다[2]. "
"목록 학명 칸에는 'Prunus davidiana (Carriere) Franchet'와 함께 'Amygdalus communis Bunge'가 적혀 있는데, 논문에서는 주로 Amygdalus davidiana라는 이명이 쓰인다[1, 15, 17, 18]. "
"목록의 'Amygdalus communis Bunge' 표기가 어떤 근거로 붙었는지는 확인하지 못함. "
"건강기능식품 고시형 원료 가운데 산복사를 원재료로 하는 항목은 고시 원문에서 찾지 못했다[3]. "
"자생 범위는 중국에서 한국까지로 정리되어 있으나, 이는 검색 요약으로만 확인한 내용이다[6]. "
"연구는 줄기의 플라보노이드, 씨(도인)의 배당체, 복숭아 육종·대목 소재로서의 유전체에 몰려 있고 식용 부위인 열매의 성분 연구는 적다[4, 10, 21].")
sec["history"] = ("역사와 전통적 이용",
"중국 전통 약재 '도인(桃仁, semen persicae)'은 복숭아와 산복사의 익은 씨를 말린 것으로, 여러 한약 처방에 쓰여 왔다[8]. "
"산복사 뿌리껍질은 회화나무·수양버들·뽕나무 뿌리껍질과 함께 중국 처방 '사피탕(Sipi soup)'의 재료로 소개된다[15]. "
"복숭아나무나 산복사에서 나오는 수지인 '도교(peach gum)'는 장 건강을 돕는 데 쓰인다고 소개된다[16]. "
"베이징에서는 옛 문헌과 관측망 자료를 합쳐 산복사 첫 개화일을 1741–2000년에 걸쳐 복원하고 기후 변동 연구에 썼다[17]. "
"국내에서는 1991년 무렵부터 산복사 줄기 메탄올 추출물과 주성분 프루닌이 흰쥐의 혈당·혈중지질에 미치는 영향을 다룬 연구가 발표되었다[10, 11, 12]. "
"열매를 식품으로 먹어 온 국내 전통 이용 기록은 공공기관 자료에서 확인하지 못함. "
"근래에는 열매의 당 추출물(sugar extract)을 발효 소재로 쓰는 연구가 나왔다[5].")
sec["biology"] = ("식물학적 특징",
"산복사는 염색체 기본수 x = 8인 이배체 벚나무속 식물로, 아몬드·복숭아·살구·체리 등과 비교한 연관 지도에서 표지 배열이 대체로 일치했다[19]. "
"씨는 같은 숲에 자라는 시베리아살구(Armeniaca sibirica)보다 크고 내과피가 두꺼워 단단하지만, 조지방·조단백·열량·탄닌 수준은 비슷했다[18]. "
"꽃의 안토시아닌 조성은 복숭아와 달라, 복숭아는 산복사보다 P. ferganensis에 더 가깝다는 해석이 나왔다[34]. "
"복숭아혹진딧물에 강한 저항성을 보이며, 진딧물 가해 뒤 대사체 분석에서 베툴린이 핵심 방어 물질로 지목되었다[30]. "
"클론 P1908은 자두곰보병바이러스(PPV, 샤카병)와 흰가루병 저항성 공급원으로 연구되었다[28, 31]. "
"중국 서북부 염류 토양에서는 산복사 대목 위 복숭아가 털복숭아 대목보다 내염성이 높았고, 실험에서 잎의 Na⁺ 축적을 최대 36.36% 줄였다[32]. "
"열매의 크기·색·맛 같은 형태 특징은 공공기관 자료에서 확인하지 못함.")
sec["related_species"] = ("가까운 종과 혼동",
"산복사와 가장 가까운 재배종은 복숭아이며, 두 종 사이 교배 집단에서 상동 재조합이 정상적으로 일어나 매우 가까운 관계로 확인되었다[27]. "
"야생 복숭아류로는 P. mira, P. kansuensis, P. ferganensis가 함께 다뤄지며, 중국 재래 복숭아 SSR 분석에서 산복사는 P. kansuensis와 한 집단으로 묶였다[22, 35]. "
"반수체 구분 유전체 분석은 산복사 유전체의 4.1%가 복숭아 이외 기원이고 그중 94.5%가 아몬드에서 왔다고 보고했다[21]. "
"P. mira와 아몬드(P. dulcis)의 잡종 기원 가설, 아몬드가 산복사 기원에 관여했다는 해석도 나와 있다[22, 23]. "
"식약처 목록에서 복숭아(P. persica)는 열매가 사용가능, 꽃이 제한적사용으로 산복사와 따로 관리되므로 두 종 자료를 섞어 쓰지 않는다[2]. "
"약재 도인은 복숭아와 산복사의 씨를 함께 원료로 하므로, 도인 연구 결과에서는 두 종을 구분할 수 없다[8]. "
"복숭아 대목 'Barrier'는 복숭아와 산복사의 종간 잡종이어서, 대목 연구 결과를 산복사 열매에 그대로 옮겨서는 안 된다[33].")
sec["cultivation"] = ("재배와 생산",
"국내 산복사 열매의 재배 면적·생산량 통계는 통계청·농림축산식품부 자료에서 확인하지 못함. "
"중국 서북부의 염류·알칼리 토양에서는 산복사를 복숭아 대목으로 써 왔고, 현장에서 털복숭아 대목보다 내염성이 낫다는 관찰이 쌓였다[32]. "
"스페인 연구에서 복숭아×산복사 잡종 대목 'Barrier'는 비교한 대목 가운데 철 결핍 황화에 민감한 편이었다[33]. "
"프랑스 연구진은 산복사 클론 P1908과 넥타린 'Summergrand'를 교배한 집단으로 진딧물·PPV 저항성과 과실 품질의 유전 구조를 분석했다[28, 29, 31]. "
"이 집단에서 산복사 대립유전자는 야생형 겉모습과 달리 과실·씨 크기, 당·산 농도, 붉은 과육에 유리한 효과를 보이기도 했다[31]. "
"반수체 유전체를 바탕으로 진딧물 저항성 복숭아를 빠르게 육성하는 설계 육종 절차도 제안되었다[21]. "
"야생에서는 설치류가 씨를 분산 저장하는데, 산복사 씨는 한 종의 다람쥐류만 분산 저장해 시베리아살구보다 실생 정착이 적었다[18].")
sec["processing"] = ("가공과 이용",
"식품원료로 쓸 수 있는 형태는 씨를 뺀 산복사 열매이며, 씨와 잎은 식품에 쓸 수 없다[1, 2]. "
"국내 연구진이 산복사 열매에서 페놀 화합물을 분리하고 항산화 활성을 평가한 논문이 있다[4]. "
"이 논문은 PubMed에 초록 본문이 실려 있지 않아 분리 성분 이름과 함량은 확인하지 못함. "
"열매 당 추출물(sugar extract)에서 히알루로니다아제 억제능을 지닌 고초균 SPF4211을 분리했고, 추출물 1%, 종균 2.53%, 발효 7일 조건에서 억제율 예측값 37.936%, 실측값 38.367%를 얻었다[5]. "
"열매에서 우르솔산·코로솔산·α-아미린 같은 트리테르페노이드를 분리했다는 국내 보고가 있으나, 원문은 열지 못하고 검색 요약으로만 확인했다[7]. "
"씨는 약재 도인으로 가공되며 품질 관리 지표로 아미그달린 함량을 쓴다[8]. "
"수지(도교)에서는 분자량 3185.2 kDa의 아라비노갈락탄이 분리되었으나, 원료가 복숭아와 산복사 가운데 무엇인지는 초록에서 구분되지 않는다[16]. "
"식약처 건강기능식품 생산실적에서 산복사 품목은 확인하지 못함.")
sec["genetics"] = ("유전체와 기원 연구",
"2021년 복숭아·자두·살구·P. mira·산복사 다섯 종의 염색체 수준 유전체가 함께 발표되었으며, 유전체 크기는 240–276 Mb, 단백질 암호 유전자는 25,333–27,826개였다[20]. "
"2022년에는 산복사를 포함한 야생 복숭아 네 종의 유전체가 조립되어 저항성 관련 변이가 비교되었다[22]. "
"2024년 발표된 반수체 구분 유전체(501.7 Mb)에서는 두 반수체 사이 구조 변이 18,152개가 확인되었고, 진딧물 저항성 QTL이 Pda03 끝에 놓였다[21]. "
"주요 저항 유전자 PdaWRKY4는 프로모터의 9 bp 결실과 연관되며, PdaCYP716A1을 통해 베툴린 합성을 촉진한다[21]. "
"엽록체 유전체는 158,055 bp(유전자 131개)로 보고되었고, 다른 연구에서는 158,971 bp로 측정되었다[24, 25]. "
"미토콘드리아 유전체는 407,608 bp, GC 45.5%, 유전자 64개였다[26]. "
"PPV 저항성에는 여섯 유전체 구간이 관여해 표현형 변이의 22–51%를 설명했고, 진딧물 저항성 QTL 7개는 각각 6.1–43.1%를 설명했다[28, 29]. "
"1,020개 복숭아 계통 범변이체 분석은 아몬드가 산복사 기원에 관여했다고 해석했다[23].")
sec["safety"] = ("안전성과 주의",
"식품으로 쓸 수 있는 부위는 씨를 뺀 열매이며, 산복사씨앗과 산복사잎은 식품원료 목록에서 사용불가다[1, 2]. "
"산복사는 건강기능식품 고시형 원료가 아니어서 고시된 섭취 시 주의사항은 없다[3]. "
"도인(복숭아·산복사의 씨)에는 아미그달린이 들어 있고, 장내 세균의 β-글루코시다아제에 의해 벤즈알데하이드와 시안화수소로 분해될 수 있다[8]. "
"아미그달린 4.94%를 함유한 도인 에탄올 추출물은 흰쥐 단회 경구 2000 mg/kg, 28일 반복 경구 600 mg/kg/일까지 뚜렷한 독성 징후를 보이지 않았으나, 이는 씨 추출물의 동물 결과다[8]. "
"줄기 추출물·프루닌의 혈당·지질 개선 결과는 대부분 흰쥐 복강 주사나 세포 실험이어서 열매 섭취 효과의 근거가 되지 않는다[10, 11, 12, 14]. "
"산복사 열매 자체의 알레르기 성분, 잔류농약, 독성에 관한 공공기관 정보는 확인하지 못함.")
sections = [{"key": k, "title": t, "body": b} for k, (t, b) in sec.items()]

C = lambda name, ko, cls, role, part, content, act, src: dict(name=name, name_ko=ko, **{"class": cls}, role=role, part=part, content_text=content, activity_ko=act, source=src)
compounds = [
 C("Prunin", "프루닌(나린제닌-7-O-글루코사이드)", "플라바논 배당체", "bioactive", "줄기(메탄올 추출물) — 식품원료 부위 아님", "줄기의 주 플라보노이드로 보고, 정량값은 초록에 없음[10, 14]", "STZ 당뇨 흰쥐에 복강 투여 시 혈당·총지질 감소 — 동물 결과(복강 주사)[10]; PTP1B IC50 5.5 ± 0.29 µM, α-글루코시다아제 IC50 317 ± 2.12 µM, 인슐린 저항 HepG2 세포 포도당 흡수 증가 — 효소·세포 결과[14]", [10, 14]),
 C("Catechin", "(+)-카테킨", "플라반-3-올", "bioactive", "줄기 — 식품원료 부위 아님", "줄기에서 분리, 정량값 없음[11, 13]", "고지방식이 흰쥐에 복강 투여 시 중성지방 감소 — 동물 결과(복강 주사)[11]", [11, 13]),
 C("Hesperetin 5-O-glucoside", "헤스페레틴-5-O-글루코사이드", "플라바논 배당체", "bioactive", "줄기 — 식품원료 부위 아님", "줄기에서 분리, 정량값 없음[11, 13]", "고지방식이 흰쥐 복강 투여에서 콜레스테롤 감소 — 동물 결과(복강 주사)[11]", [11, 13]),
 C("Kaempferol", "캠페롤", "플라보놀", "bioactive", "줄기 — 식품원료 부위 아님", "줄기에서 분리, 정량값 없음[13]", "신장 균질액에서 총 ROS·하이드록실 라디칼 생성 억제 — 시험관 결과[13]", [13]),
 C("Kaempferol 7-O-glucoside", "캠페롤-7-O-글루코사이드", "플라보놀 배당체", "bioactive", "줄기 — 식품원료 부위 아님", "줄기에서 분리, 정량값 없음[13]", "ROS·퍼옥시나이트라이트 계에서 항산화 활성 평가 — 시험관 결과[13]", [13]),
 C("Dihydrokaempferol", "다이하이드로캠페롤", "플라바노놀", "bioactive", "줄기 — 식품원료 부위 아님", "줄기에서 분리, 정량값 없음[13]", "ROS·하이드록실 라디칼 계에서 항산화 활성 평가 — 시험관 결과[13]", [13]),
 C("Naringenin", "나린제닌", "플라바논", "bioactive", "줄기 — 식품원료 부위 아님", "줄기에서 분리, 정량값 없음[13]", "ROS·하이드록실 라디칼 계에서 항산화 활성 평가 — 시험관 결과[13]", [13]),
 C("Amygdalin", "아미그달린", "시안 생성 배당체", "marker", "씨(도인; 복숭아·산복사 씨 구분 없음) — 식품원료 사용불가 부위", "도인 85% 에탄올 추출물 중 4.94%(HPLC; 초록은 4.95%, 고찰은 4.78%로 표기가 엇갈림)[8]", "장내 β-글루코시다아제로 벤즈알데하이드·시안화수소로 분해될 수 있음 — 도인 품질 지표 성분[8]", [8]),
 C("Prupersin A", "프루퍼신 A", "방향족 배당체(벤조일 글루코사이드)", "bioactive", "씨 — 식품원료 사용불가 부위", "씨에서 새 화합물로 분리(프루퍼신 A–E 등 7종), 정량값 없음[9]", "화합물 1–6이 흰쥐 간 마이크로솜 지질과산화(MDA)를 10⁻⁵ mol/L에서 50–67% 억제 — 시험관 결과[9]", [9]),
 C("Betulin", "베툴린", "루판형 트리테르펜", "bioactive", "식물체(진딧물 가해 실험; 부위는 초록에 명시 없음)", "진딧물 가해 뒤 증가하는 핵심 방어 대사물로 보고, 정량값은 초록에 없음[30]", "진딧물 살충 활성(익충에는 독성 없음) — 곤충 시험 결과; 합성 유전자 CYP716A1[30, 21]", [30, 21]),
 C("Ursolic acid", "우르솔산", "우르산형 트리테르펜", "bioactive", "열매", "열매에서 분리 보고, 정량값 확인하지 못함(검색 요약으로만 확인)[7]", "확인하지 못함[7]", [7]),
 C("Corosolic acid", "코로솔산", "우르산형 트리테르펜", "bioactive", "열매", "열매에서 분리 보고, 정량값 확인하지 못함(검색 요약으로만 확인)[7]", "확인하지 못함[7]", [7]),
 C("alpha-Amyrin", "α-아미린", "트리테르펜", "bioactive", "열매", "열매에서 분리 보고, 정량값 확인하지 못함(검색 요약으로만 확인)[7]", "확인하지 못함[7]", [7]),
 C("Arabinogalactan", "아라비노갈락탄(도교 PG-2)", "다당류", "bioactive", "수지(도교; 복숭아·산복사 원료 구분 없음) — 식품원료 목록 부위 아님", "도교에서 분리한 PG-2, 분자량 3185.2 kDa, 함량은 초록에 없음[16]", "인간화 노화 변비 모델에서 장내 세균·트립타민·5-HT 신호를 통해 변비 완화 — 동물 결과[16]", [16]),
]

assays = [{
 "role": "literature", "compound": "Amygdalin", "compound_ko": "아미그달린",
 "part": "씨(도인 = 복숭아·산복사의 말린 씨, 종 구분 없음; 중국 간쑤성 수집) — 식품원료 사용불가 부위",
 "content": "에탄올 추출물 중 4.94%(머무름 시간 13.76분)[8]",
 "method": "HPLC-UV",
 "conditions": {
  "instrument": "Agilent 1260 Infinity binary pump, 자동시료주입기, UV 검출기(OpenLAB CDS C.01.07)",
  "column": "Zorbax SB-C18 (250 mm × 4.6 mm, 5 µm)",
  "mobile_phase": "메탄올–초순수 20:80 (v/v)",
  "gradient": "등용매, 분석 시간 35분",
  "flow": "1.0 mL/min",
  "temp": "30 °C",
  "detection": "UV 210 nm",
  "injection": "20 µL",
  "sample_prep": "탈지(석유에테르 60 °C 6시간 ×3) 후 85% 에탄올 2시간 환류 추출·건조; 추출물 300 mg을 70% 메탄올에 녹이고 0.22 µm 여과, 2분 초음파 탈기",
  "standard": "D-아미그달린(Sigma-Aldrich) 5 mg을 70% 메탄올 5 mL에 녹인 표준원액을 희석해 검량선 작성",
  "linearity": "", "lod": "", "loq": "", "recovery": ""},
 "rationale": "아미그달린은 도인의 품질 관리 지표 성분이자 시안화수소를 내는 안전성 지표다[8]. 산복사 열매(식용 부위)를 정량한 분석 조건은 찾지 못해 씨 자료를 참고로 적었고, 직선성·검출한계·회수율은 원문에 없다[8].",
 "source": [8], "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11354697/", "source_kind": "paper"}]

d = {
 "slug": "prunus-davidiana", "name_ko": "산복사", "name_en": "Chinese wild peach",
 "scientific_name": "Prunus davidiana (Carrière) Franch.",
 "aliases": ["산복사열매", "산복숭아", "Chinese wild peach", "mountain peach", "Amygdalus davidiana (Carr.) C. de Vos", "Amygdalus communis Bunge(목록 표기)"],
 "sections": sections, "compounds": compounds, "markers": [], "nutrients": [], "assays": assays,
 "production": [], "world": [], "gi": [], "orgs": [], "sources": S,
}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in sections: print(s["key"], len(s["body"]))
