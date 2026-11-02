import json
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "dossier.json"
ACC = "2026-11-02"
PM = "https://pubmed.ncbi.nlm.nih.gov/"
PMC = "https://pmc.ncbi.nlm.nih.gov/articles/"

sources = [
    (1, "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 주름미더덕(Styela plicata) 1행(이명 오만둥이, 오만디; 영명 Wrinkled sea squirt, Sea potato; 분류 수산물, 부위 '-', 사용가능; 2026-10-13 받은 원자료). 같은 속 미더덕·미더덕엑기스분말(Styela clava) 행 대조",
     "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "식품의약품안전처", "2026-10-13"),
    (2, "De novo genome assembly, inversion detection, and worldwide adaptation on the invasive species Styela plicata. Sci Rep 2025;15(1):40328",
     PMC + "PMC12627437/", "Scientific Reports (PMC 전문)", ACC),
    (3, "The whereabouts of an ancient wanderer: global phylogeography of the solitary ascidian Styela plicata. PLoS One 2011;6(9):e25495 (초록)",
     PMC + "PMC3179514/", "PLoS One (PubMed 초록)", ACC),
    (4, "The past, the recent, and the ongoing evolutionary processes of the worldwide invasive ascidian Styela plicata. Mol Ecol 2024;33(18):e17502 (초록)",
     PM + "39205460/", "Molecular Ecology (PubMed 초록)", ACC),
    (5, "Stochasticity in space, persistence in time: genetic heterogeneity in harbour populations of the introduced ascidian Styela plicata. PeerJ 2016;4:e2158 (초록)",
     PMC + "PMC4924124/", "PeerJ (PubMed 초록)", ACC),
    (6, "Determination of toxic heavy metals in Echinodermata and Chordata species from South Korea. Food Addit Contam Part B 2014;7(4):295-301 (초록)",
     PM + "24916139/", "Food Additives & Contaminants Part B (PubMed 초록)", ACC),
    (7, "Genetic Distances in Three Ascidian Species determined by PCR Technique. Dev Reprod 2016;20(4):379-385",
     PMC + "PMC5270612/", "Development & Reproduction (PMC 전문)", ACC),
    (8, "Metabolite profiling of ascidian Styela plicata using LC-MS with multivariate statistical analysis and their antitumor activity. J Enzyme Inhib Med Chem 2017;32(1):614-623",
     PMC + "PMC6010017/", "J Enzyme Inhib Med Chem (PMC 전문)", ACC),
    (9, "Attenuation of Rat Colon Carcinogenesis by Styela plicata Aqueous Extract. Modulation of NF-κB Pathway and Cytoplasmic Sod1 Gene Expression. Asian Pac J Cancer Prev 2020;21(9):2739-2750",
     PMC + "PMC7779447/", "Asian Pacific Journal of Cancer Prevention (PMC 전문)", ACC),
    (10, "Modulation of the Gut-Liver Axis and Nrf2/HO-1-Mediated Antioxidant Defense by Styela plicata Extract Against Alcoholic Liver Injury. Antioxidants (Basel) 2026;15(4):480",
     PMC + "PMC13114156/", "Antioxidants (PMC 전문)", ACC),
    (11, "Antiviral treatment of hepatitis B virus-transgenic mice by a marine organism, Styela plicata. World J Gastroenterol 2006;12(25):4038-4043 (초록)",
     PMC + "PMC4087717/", "World Journal of Gastroenterology (PubMed 초록)", ACC),
    (12, "Plicatamide, an antimicrobial octapeptide from Styela plicata hemocytes. J Biol Chem 2003;278(15):13546-13553 (초록)",
     PM + "12569105/", "Journal of Biological Chemistry (PubMed 초록)", ACC),
    (13, "Plicatamide: A lead to the biosynthetic origins of the tunichromes? Biochem Biophys Res Commun 2000;270(2):421-424 (초록)",
     PM + "10753640/", "BBRC (PubMed 초록)", ACC),
    (14, "Tunichrome sp-1: new pentapeptide tunichrome from the hemocytes of Styela plicata. J Nat Prod 2002;65(3):377-378 (초록)",
     PM + "11908983/", "Journal of Natural Products (PubMed 초록)", ACC),
    (15, "Isolation, fractionation, and preliminary characterization of a novel class of sulfated glycans from the tunic of Styela plicata (Chordata Tunicata). J Biol Chem 1986;261(2):758-765 (초록)",
     PM + "2867092/", "Journal of Biological Chemistry (PubMed 초록)", ACC),
    (16, "Structural features of sulfated glycans from the tunic of Styela plicata (Chordata-Tunicata). A unique occurrence of L-galactose in sulfated polysaccharides. Eur J Biochem 1987;166(2):431-436 (초록)",
     PM + "3609020/", "European Journal of Biochemistry (PubMed 초록)", ACC),
    (17, "Isolation and characterization of a heparin with low antithrombin activity from the body of Styela plicata (Chordata-Tunicata). Distinct effects on venous and arterial models of thrombosis. Thromb Res 2007;121(2):213-223 (초록; PMC 본문 없음)",
     PMC + "PMC2211419/", "Thrombosis Research (PubMed 초록)", ACC),
    (18, "Highly sulfated dermatan sulfates from Ascidians. Structure versus anticoagulant activity of these glycosaminoglycans. J Biol Chem 1998;273(43):27848-27857 (초록)",
     PM + "9774395/", "Journal of Biological Chemistry (PubMed 초록)", ACC),
    (19, "Anticoagulant sulfated glycosaminoglycans in the tissues of the primitive chordate Styela plicata (Tunicata). Glycobiology 2000;10(12):1333-1340 (초록)",
     PM + "11159925/", "Glycobiology (PubMed 초록)", ACC),
    (20, "Effects of Dermatan Sulfate from Marine Invertebrate Styela plicata in the Wound Healing Pathway: A Natural Resource Applied to Regenerative Therapy. Mar Drugs 2022;20(11):676",
     PMC + "PMC9693086/", "Marine Drugs (PMC 전문)", ACC),
    (21, "Ascidian dermatan sulfates attenuate metastasis, inflammation and thrombosis by inhibition of P-selectin. J Thromb Haemost 2011;9(9):1807-1815 (초록)",
     PM + "21676168/", "Journal of Thrombosis and Haemostasis (PubMed 초록)", ACC),
    (22, "Unfractionated heparin and new heparin analogues from ascidians (chordate-tunicate) ameliorate colitis in rats. J Biol Chem 2009;284(17):11267-11278 (초록; PMC 본문 없음)",
     PMC + "PMC2670131/", "Journal of Biological Chemistry (PubMed 초록)", ACC),
    (23, "Styela plicata: a new promising bioindicator of heavy metal pollution for eastern Aegean Sea coastal waters. Environ Sci Pollut Res Int 2016;23(21):21536-21553 (초록)",
     PM + "27515524/", "Environmental Science and Pollution Research (PubMed 초록)", ACC),
    (24, "Evaluation and comparison of trace metal accumulation in different tissues of potential bioindicator organisms: Macrobenthic filter feeders Styela plicata, Sabella spallanzanii, and Mytilus galloprovincialis. Environ Toxicol Chem 2016;35(12):3062-3070 (초록)",
     PM + "27187528/", "Environmental Toxicology and Chemistry (PubMed 초록)", ACC),
    (25, "Symbiotic bacteria associated with ascidian vanadium accumulation identified by 16S rRNA amplicon sequencing. Mar Genomics 2018;43:33-42 (초록)",
     PM + "30420273/", "Marine Genomics (PubMed 초록)", ACC),
    (26, "Ascidian bioresources: common and variant chemical compositions and exploitation strategy - examples of Halocynthia roretzi, Styela plicata, Ascidia sp. and Ciona intestinalis. Z Naturforsch C 2016;71(5-6):165-180 (초록)",
     PM + "27049617/", "Zeitschrift für Naturforschung C (PubMed 초록)", ACC),
    (27, "Comparison of the Efficiency of Different Eradication Treatments to Minimize the Impacts Caused by the Invasive Tunicate Styela plicata in Mussel Aquaculture. Animals (Basel) 2023;13(9):1541 (초록)",
     PMC + "PMC10177385/", "Animals (PubMed 초록)", ACC),
    (28, "Stress levels over time in the introduced ascidian Styela plicata: the effects of temperature and salinity variations on hsp70 gene expression. Cell Stress Chaperones 2012;17(4):435-444 (초록)",
     PMC + "PMC3368029/", "Cell Stress & Chaperones (PubMed 초록)", ACC),
    (29, "The Hemolymph of the ascidian Styela plicata (Chordata-Tunicata) contains heparin inside basophil-like cells and a unique sulfated galactoglucan in the plasma. J Biol Chem 2007;282(3):1615-1626 (초록)",
     PM + "17114184/", "Journal of Biological Chemistry (PubMed 초록)", ACC),
    (30, "Unique form and osmoregulatory function of a neurohypophysial hormone in a urochordate. Endocrinology 2008;149(10):5254-5261 (초록)",
     PM + "18583415/", "Endocrinology (PubMed 초록)", ACC),
    (31, "A miniaturized bismuth-based sensor to evaluate the marine organism Styela plicata bioremediation capacity toward heavy metal polluted seawater. Sci Total Environ 2017;584-585:692-700 (초록)",
     PM + "28129904/", "Science of the Total Environment (PubMed 초록)", ACC),
    (32, "[Study on the HPLC fingerprints of Styela plicata]. Zhong Yao Cai 2006;29(3):221-224 (중국어, 초록)",
     PM + "16850716/", "Zhong Yao Cai (PubMed 초록)", ACC),
    (33, "From invasive nuisance to biotechnological asset: LC-MS/MS chemical profiling and pharmacological potential of ascidian Styela plicata from Albufeira Lagoon, Portugal. Environ Sci Pollut Res Int 2026;33(26):13285-13299 (초록)",
     PM + "42571676/", "Environmental Science and Pollution Research (PubMed 초록)", ACC),
    (34, "Dermatan sulfate in tunicate phylogeny: order-specific sulfation pattern and the effect of [→4IdoA(2-sulfate)β-1→3GalNAc(4-sulfate)β-1→] motifs in dermatan sulfate on heparin cofactor II activity. BMC Biochem 2011;12:29 (초록)",
     PMC + "PMC3127831/", "BMC Biochemistry (PubMed 초록)", ACC),
    (35, "Identification of an antennapedia-like homeobox gene in the ascidians Styela clava and S. plicata. Gene 1994;147(2):219-222 (초록)",
     PM + "7926803/", "Gene (PubMed 초록)", ACC),
    (36, "The identification and localization of two intermediate filament proteins in the tunic of Styela plicata (Tunicata, Styelidae). 2009 (PubMed 서지 — 제목의 분류 표기만 인용)",
     PM + "19524277/", "PubMed", ACC),
    (37, "Isolation and characterization of a highly sulfated heparan sulfate from ascidian test cells. Biochim Biophys Acta 1999;1428(1):77-87 (초록)",
     PM + "10366762/", "Biochimica et Biophysica Acta (PubMed 초록)", ACC),
]

S = {}
S["overview"] = ("한눈에 보기", """주름미더덕(Styela plicata)은 식약처 「식품원료 목록」에 '주름미더덕'이라는 이름의 수산물로 올라 있고, 이명은 오만둥이·오만디, 영명은 Wrinkled sea squirt·Sea potato다[1]. 목록상 상태는 '사용가능'이며, 사용 부위 칸은 '-'로 표기되어 있고 따로 정한 사용 조건은 없다[1]. 같은 속의 미더덕(Styela clava, 이명 미두둑)과 미더덕엑기스분말은 목록에서 별도 행으로 관리되므로, 두 종의 자료는 섞어 읽지 않아야 한다[1].

분류상 홀로 사는 멍게류(해초류)로, 멍게(우렁쉥이)와 같은 Stolidobranchia 목에 속하고 미더덕과(Styelidae)로 표기된다[34][36]. 한국 남해안에 넓게 분포하며, 미더덕·우렁쉥이와 함께 향과 맛 때문에 한국에서 많이 먹는 해산물로 소개된다[7]. 국내 연구에서도 우렁쉥이와 함께 흔히 먹는 척삭동물 해산물로 중금속 조사 대상이 되었다[6].

세계적으로는 배 밑바닥에 붙어 퍼진 대표적인 침입종으로, 원래 살던 곳은 아직 밝혀지지 않았다[2][3]. 연구는 겉껍질(피낭)의 황산화 다당, 몸과 혈림프의 헤파린·더마탄황산, 혈구의 항균 펩타이드, 추출물의 동물·세포 실험에 집중되어 있다[12][15][17][18][29]. 다만 사람을 대상으로 한 임상시험은 확인하지 못함.""")

S["history"] = ("이용 역사", """주름미더덕은 1823년 Lesueur가 기재한 종으로, 학명 뒤에 '(Lesueur, 1823)'을 붙여 쓴다[27]. 세계 여러 바다에 배 바닥 부착으로 오래전부터 퍼져 있었고, 유전자 연구는 모든 조사 대양에 오래 머물러 왔으며 여러 차례의 이입이 지금의 유전 구조를 만들었다고 보았다[3]. 2b-RADseq 연구는 대서양과 태평양으로 서로 독립된 두 번의 이입이 있었다는 모형을 지지했다[4].

한국에서는 미더덕·우렁쉥이와 함께 향·맛·영양 때문에 즐겨 먹는 해산물로 소개되며, 남해안 연안에 분포한다[7]. 식약처 식품원료 목록에는 오만둥이·오만디라는 지역 이름이 이명으로 함께 실려 있다[1]. 우리나라에서 언제부터 먹기 시작했는지에 대한 공공기관 기록은 확인하지 못함.

2006년 중국 중약재 학술지에는 HPLC 지문(13개 특징 피크)으로 산지가 다른 주름미더덕을 확인·품질 관리하는 방법이 발표되었다[32]. 같은 해 다른 연구는 이 종의 유효 성분이 B형간염 바이러스 형질전환 생쥐에서 혈청 표면항원과 바이러스 DNA를 낮췄다고 보고했다[11]. 1980년대에는 겉껍질의 황산화 다당이, 2000년대에는 몸의 헤파린 유사 물질이 연구되었다[15][16][17].""")

S["biology"] = ("생물학적 특징(동물)", """주름미더덕은 바위나 인공 구조물에 붙어 혼자 사는 멍게류로, 바닷물을 걸러 먹는 여과 섭식 동물이다[24][2]. 몸은 겉껍질(피낭)과 속 조직으로 나뉘며, 네 종의 멍게류를 비교한 연구에서 겉껍질은 탄수화물, 속 조직은 단백질이 많았고 셀룰로스는 거의 겉껍질에만 있었다[26]. 겉껍질에는 L-갈락토스가 많은 독특한 황산화 갈락탄이 있어, 피낭의 구조 유지에 관여할 것으로 추정되었다[15][16].

이 종은 1년 내내 번식할 수 있고 유생이 인공 기질에 잘 붙어, 항구·양식 시설·선체에서 다른 부착 생물보다 먼저 자리를 차지한다[2]. 혈림프에는 적어도 다섯 가지 혈구가 있고, 헤파린과 히스타민은 과립구 한 종류의 과립 안에 함께 들어 있었다[29].

염습지 개체군을 2년간 본 연구에서 열충격단백질(hsp70) 발현은 여름과 겨울에 높았고, 해마다 6월 무렵 수온이 6 °C 넘게 급히 오를 때 집단 폐사가 함께 나타났다[28]. 이 종의 옥시토신 계열 신경펩타이드(SOP)는 60% 희석 해수에서 가장 많이 발현되었고, 입·출수공을 닫게 해 묽은 물이 몸 안으로 들어오는 것을 막는 데 관여한다고 보았다[30].""")

S["related_species"] = ("관련 종·이름", """같은 속의 미더덕(Styela clava)은 식품원료 목록에서 미더덕·미더덕엑기스분말로 따로 올라 있고 이명은 미두둑, 영명은 Warty sea squirt다[1]. 주름미더덕의 이명은 오만둥이·오만디로, 미더덕의 이명과 겹치지 않는다[1]. 한국 남해에서 채집한 미더덕·우렁쉥이·주름미더덕 각 7개체를 RAPD로 비교한 결과, 세 종은 각각 다른 무리로 나뉘었고 주름미더덕을 구별하는 종 특이 띠(BION-25 프라이머 7개)도 찾았다[7].

미더덕과 주름미더덕의 호메오박스 유전자(AHox2·AHox3)는 염기 서열이 87% 같고 아미노산 서열은 같았다[35]. 이처럼 두 종은 가까워서, 미더덕에서 나온 성분·효능 자료를 주름미더덕 자료로 옮겨 쓰면 안 된다[35][1].

더마탄황산의 황산기 위치는 분류군에 따라 다르며, 주름미더덕과 Halocynthia pyriformis는 N-아세틸갈락토사민 4번 탄소에, Phallusia nigra는 6번 탄소에 황산기가 붙는다[18]. Stolidobranchia 목 멍게류의 더마탄황산은 이당 단위의 76%가 이중 황산화되어 있었다[34]. 바나듐을 많이 모으는 것은 Ascidia 같은 다른 목의 멍게류이고, 주름미더덕은 바나듐이 적은 종으로 비교되었다[25].""")

S["cultivation"] = ("서식·채취·부착 피해", """주름미더덕은 한국 남해안 연안과 여러 해역에 분포하는 경제적으로 중요한 멍게류로 소개된다[7]. 국내 양식 방법, 생산량, 산지별 통계는 공공기관 자료에서 확인하지 못함.

외국에서는 주로 홍합 양식장의 부착 해적생물로 다뤄진다[27]. 포르투갈 알부페이라 석호에서는 2017년 이 종이 번져 홍합 생산을 방해했고, 제거 처리 실험에서 공기 노출·민물 담금은 27% 폐사에 그쳤으며 아세트산 처리는 90% 넘게 죽였지만 홍합도 33~40%가 죽었다[27]. 같은 석호 개체는 추출물의 생물막 억제 효과를 찾는 연구 재료로도 쓰였다[33].

항구 개체군의 유전 구조는 5년(약 20세대) 동안 거의 그대로 유지되어, 처음 들어온 개체의 유전 구성이 오래 남는 것으로 보았다[5]. 오염 해수 실험에서는 납이 카드뮴보다 약 2.5배 더 몸에 쌓였고, 바닷물에서 카드뮴 13%, 납 40%를 줄이는 생물 정화 효과가 측정되었다[31]. 이 결과는 오염된 해역의 개체에 납·카드뮴이 더 쌓일 수 있음을 보여 준다[31][24].""")

S["processing"] = ("가공·이용 연구", """식품으로서 주름미더덕의 가공 방식(조리·건조·수출 제품)에 관한 공공기관 자료는 확인하지 못함. 멍게류 네 종을 비교한 연구는 속 조직의 단백질이 대부분 콜라겐이며 필수아미노산 지수가 높고, 겉껍질의 셀룰로스는 식이섬유나 사료로 쓸 수 있다고 제안했다[26].

추출물 연구로는, 이탈리아 개체의 메탄올 추출물이 HeLa 세포에서 IC50 41.15 µmol/L, 정제 분획 SP-50이 HT29 세포에서 IC50 31.66 µmol/L로 세포 증식을 억제했다[8]. 이집트 개체의 물 추출물을 3,900 mg/kg 체중으로 32주 동안 위관으로 준 쥐에서 대장 종양 발생률은 93.8%에서 26.7%로, 쥐 한 마리당 이상 음와 병소는 124개에서 27.2개로 줄었다[9]. 중국 개체의 95% 에탄올 추출물 300 mg/kg은 알코올 간손상 생쥐의 혈청 AST·ALT·중성지방을 낮췄다[10].

몸에서 얻은 헤파린은 포유류 헤파린보다 항트롬빈 활성이 약 10배 낮지만 동맥 혈전 모형에서는 비슷한 효과를 보였고 출혈은 적었다[17]. 이 종과 Phallusia nigra의 더마탄황산은 생쥐에서 P-셀렉틴을 막아 전이·염증·혈전을 줄였고, 쥐 대장염 모형에서도 염증을 줄였다[21][22]. 이 결과들은 모두 세포·동물 실험이라 사람에게 같은 효과가 있는지는 확인하지 못함.""")

S["genetics"] = ("유전 정보", """2025년 바르셀로나 항구 개체로 염색체 수준의 참조 유전체가 발표되었고, 조립 길이는 419.2 Mb, 유동세포 분석 추정 크기는 430 Mb였다[2]. 유전자는 모두 37,097개로 그중 단백질 암호화 유전자는 19,622개였으며, 미토콘드리아 유전체는 14,413 bp(GC 29.9%)에 단백질 유전자 13개·rRNA 2개·tRNA 23개를 담고 있었다[2].

세계 24개체의 전장 유전체 분석에서 큰 염색체 역위 4개가 발견되었고, 이 역위들은 하구·항구 환경 적응과 관련될 수 있는 유전자를 많이 품고 있었다[2]. 역위를 빼고 분석해야 대양 사이·대양 안의 집단 구조가 드러났고, 미토콘드리아 계통은 세 갈래로 나뉘었다[2].

앞선 연구는 17곳 368개체의 COI와 315개체의 ANT 유전자를 읽어 두 갈래의 대립유전자 무리를 찾았고, 지중해 집단의 다양성이 가장 낮았다[3]. 18곳 87개체의 2b-RADseq 분석은 북캐롤라이나 집단이 따로 떨어져 있고 사우스캐롤라이나 집단은 혼합 기원이라고 보았다[4]. 한국 남해 개체는 RAPD 표지로 미더덕·우렁쉥이와 구별되었다[7].""")

S["safety"] = ("안전성", """식품원료 목록에서 주름미더덕은 '사용가능'이고 별도 사용 조건이 없다[1]. 건강기능식품 고시형 원료의 원재료로 연결되어 있지 않아 고시의 섭취 시 주의사항은 없다[1]. 알레르기 유발 표시 대상 여부와 마비성 패류독소 기준·검출 같은 공공기관 안전 정보는 이 작업 환경에서 식약처 원문을 열지 못해 확인하지 못함.

국내산 주름미더덕을 포함한 해산물 4종의 비소·납·카드뮴·알루미늄·수은 분석에서 알루미늄·비소가 상대적으로 높았지만 FAO·EU·식약처 기준과 비교해 안전한 수준으로 결론지었다[6]. 이 종은 걸러 먹으면서 금속을 쌓는 생물 지표로 연구되며, 이탈리아 항구에서는 납이 아가미 바구니와 겉껍질에 특히 많이 쌓였다[24]. 에게해 연구는 이 종을 바나듐을 강하게 쌓는 종으로 보았지만, 16S rRNA 공생세균 연구는 바나듐이 적은 종으로 비교해 문헌 사이에 설명이 다르다[23][25].

이탈리아 파로 호수 시료 연구는 함께 분석한 멍게류 추출물에서 마비성 패독 관련 물질(데카바모일고니오톡신 1) 후보를 질량값으로 검출했고 그 해역 개체는 먹기에 안전하지 않다고 결론지었다[8]. 다만 PMC 본문에서 그 물질이 두 종 가운데 어느 종에서 나왔는지는 확인하지 못함.

물 추출물만 먹인 쥐(3,900 mg/kg, 32주)와 에탄올 추출물을 먹인 생쥐(최대 300 mg/kg, 7주)에서는 눈에 띄는 독성이 보고되지 않았다[9][10]. 혈구 펩타이드 플리카타마이드는 사람 적혈구를 강하게 터뜨렸는데, 이는 분리한 순수 물질의 시험관 결과다[12].""")

compounds = [
    {"name": "Plicatamide", "name_ko": "플리카타마이드", "class": "변형 옥타펩타이드(DOPA 유도체)", "role": "bioactive", "part": "혈구",
     "content_text": "구조 Phe-Phe-His-Leu-His-Phe-His-dcΔDOPA; 구조 결정에 100 µg 사용", "activity_ko": "황색포도상구균·MRSA에서 수 초 안에 칼륨 유출을 일으켜 죽이는 항균 펩타이드이며 사람 적혈구는 강하게 용혈시켰다(시험관 실험)[12]",
     "source": [12, 13]},
    {"name": "Tunichrome Sp-1", "name_ko": "튜니크롬 Sp-1", "class": "변형 펜타펩타이드(튜니크롬)", "role": "marker", "part": "혈구",
     "content_text": "구조 L-DOPA-L-DOPA-Gly-L-Pro-dcΔDOPA (함량 확인하지 못함)", "activity_ko": "이 종 혈구에서 처음 분리된 튜니크롬으로, 플리카타마이드와 함께 튜니크롬 생합성 기원 연구의 단서가 되었다[13][14]",
     "source": [14, 13]},
    {"name": "Dermatan sulfate", "name_ko": "더마탄황산(2,4-이황산형)", "class": "글리코사미노글리칸", "role": "marker", "part": "내장(속 조직)·인두 세포외기질",
     "content_text": "이당 단위 중 2-O-황산 이두론산·4-O-황산 N-아세틸갈락토사민 단위가 절반 넘음(원문 그림)", "activity_ko": "헤파린 보조인자 II를 통한 항응고 활성이 포유류 더마탄황산보다 약 10배 높았고[18], 생쥐에서 P-셀렉틴을 막아 전이·염증·혈전을 줄였다[21]",
     "source": [18, 19, 20, 21]},
    {"name": "Heparin", "name_ko": "헤파린(멍게류 유래)", "class": "글리코사미노글리칸", "role": "bioactive", "part": "몸(속 조직)·장·혈구 과립",
     "content_text": "이당 조성 ΔUA(2S)-GlcNS 47.5%, ΔUA(2S)-GlcNS(6S) 38.3%, ΔUA(2S)-GlcNS(3S) 8.0%, ΔUA(2S)-GlcNS(3S)(6S) 2.8%; aPTT 활성 18 IU/mg", "activity_ko": "항트롬빈 매개 활성은 포유류 헤파린보다 약 10배 낮지만 동맥 혈전 모형에서는 비슷한 효과에 출혈이 적었다(동물 실험)[17]",
     "source": [17, 29, 19]},
    {"name": "Heparan sulfate", "name_ko": "헤파란황산(고황산형)", "class": "글리코사미노글리칸", "role": "bioactive", "part": "알의 시험세포(test cells)",
     "content_text": "이당 조성 UA(2S)-GlcNS(6S) 53%, UA(2S)-GlcNS 22%, UA-GlcNAc(6S) 14%, UA-GlcNS 11%", "activity_ko": "알과 유생을 둘러싸는 친수성 보호층 형성에 관여할 것으로 추정되었다[37]",
     "source": [37]},
    {"name": "Sulfated L-galactan", "name_ko": "황산화 L-갈락탄", "class": "황산화 다당", "role": "marker", "part": "겉껍질(피낭)",
     "content_text": "고분자 분획은 3번 위치에 황산기가 붙은 α-L-갈락토피라노스가 1→4 결합한 골격(함량 확인하지 못함)", "activity_ko": "갈락토스가 모두 L-형인 황산화 다당이 처음 보고된 예로, 피낭 구조 유지에 관여할 것으로 추정되었다[15][16]",
     "source": [15, 16]},
    {"name": "Sulfated galactoglucan", "name_ko": "황산화 갈락토글루칸", "class": "황산화 헤테로다당", "role": "bioactive", "part": "혈림프 혈장",
     "content_text": "포도당 약 60%, 갈락토스 약 40%로 구성되고 황산기가 많음", "activity_ko": "혈장에 자유롭게 떠 있는 독특한 황산화 다당으로 처음 보고되었다(기능 확인하지 못함)[29]",
     "source": [29]},
    {"name": "Cellulose", "name_ko": "셀룰로스", "class": "다당(식이섬유)", "role": "nutrient", "part": "겉껍질(피낭)",
     "content_text": "겉껍질에 거의만 존재하며 마디멍게목 종에서 더 많음(수치 확인하지 못함)", "activity_ko": "겉껍질을 식이섬유 원료나 사료로 쓸 수 있다고 제안되었다[26]",
     "source": [26]},
    {"name": "Collagen", "name_ko": "콜라겐", "class": "단백질", "role": "nutrient", "part": "속 조직",
     "content_text": "단백질 대부분이 콜라겐이며 필수아미노산 지수가 높음(수치 확인하지 못함)", "activity_ko": "속 조직 단백질의 영양 품질 근거로 제시되었다[26]",
     "source": [26]},
    {"name": "Nonanoic acid", "name_ko": "노난산", "class": "지방산", "role": "bioactive", "part": "몸 전체 메탄올 추출물의 HPLC 분획 SP-53",
     "content_text": "분획 SP-53에서 NMR로 잠정 동정(정량값 없음)", "activity_ko": "SP-53 분획은 HeLa 세포에서 IC50 37.29 µmol/L로 증식을 억제했다(세포 실험)[8]",
     "source": [8]},
    {"name": "5,6-Dihydrothymine", "name_ko": "다이하이드로티민(dihydro-5-methylpyrimidine-2,4-dione)", "class": "피리미딘 유도체", "role": "bioactive", "part": "몸 전체 메탄올 추출물의 HPLC 분획 SP-8",
     "content_text": "분획 SP-8에서 1D·2D NMR로 잠정 동정(정량값 없음)", "activity_ko": "SP-8 분획은 HeLa 세포에서 IC50 41.61 µmol/L였다(세포 실험)[8]",
     "source": [8]},
    {"name": "Palmitic acid", "name_ko": "팔미트산", "class": "포화지방산", "role": "nutrient", "part": "몸 전체 물 추출물",
     "content_text": "물 추출물 HPLC에서 확인된 25개 성분 중 주요 성분(앞선 연구 인용, 정량값 확인하지 못함)", "activity_ko": "대장암 억제 실험에 쓴 물 추출물의 주요 성분으로 거론되었다[9]",
     "source": [9]},
    {"name": "Vanadium", "name_ko": "바나듐", "class": "미량 금속", "role": "nutrient", "part": "조직",
     "content_text": "에게해 시료의 평균 금속 농도 순서 Zn > Cu > Pb > V > Cd(수치는 초록에 없음)", "activity_ko": "에게해 연구는 이 종을 바나듐 강축적종으로 소개했으나[23], 일본 연구는 바나듐이 적은 종으로 비교했다[25]",
     "source": [23, 25]},
    {"name": "Styela oxytocin-related peptide", "name_ko": "주름미더덕 옥시토신 관련 펩타이드(SOP)", "class": "신경펩타이드(14개 아미노산)", "role": "bioactive", "part": "뇌신경절",
     "content_text": "서열 CYISDCPNSRFWST-NH2", "activity_ko": "농도 의존적으로 입·출수공을 수축시켜 삼투 조절에 관여한다고 보았다[30]",
     "source": [30]},
]

assays = [
    {"role": "literature", "compound": "Dermatan sulfate (disaccharide composition)", "compound_ko": "더마탄황산 이당 조성",
     "part": "내장(겉껍질을 떼어 낸 속 조직), 아세톤 탈지 건조 가루",
     "content": "2-O-황산 이두론산·4-O-황산 N-아세틸갈락토사민 단위가 확인된 잔기의 절반 넘음(원문 그림, 수치 없음)",
     "method": "강음이온교환 HPLC(SAX-HPLC)-UV",
     "conditions": {
         "instrument": "Jasco HPLC, 광다이오드배열 검출기",
         "column": "Spherisorb-SAX(이당 분석); 앞 단계 Superdex 75 겔여과, 다당 분리는 Sepharose QXL 이온교환(GE Biosciences)",
         "mobile_phase": "SAX: NaCl 수용액; Superdex 75: 20% 아세토나이트릴 수용액 pH 3.5; QXL: 0.02 M Tris-HCl pH 8(5 mM EDTA) 중 NaCl",
         "gradient": "SAX: NaCl 0→1 M 직선; QXL: NaCl 0.5→1.3 M 직선",
         "flow": "SAX 0.5 mL/min; Superdex 75 0.5 mL/min; QXL 1 mL/min",
         "temp": "QXL 칼럼 40 °C(SAX 칼럼 온도는 원문에 없음)",
         "detection": "232 nm(불포화 이당); QXL 분획은 DMB 메타크로마시아 525 nm",
         "injection": "",
         "sample_prep": "아세톤 탈지(4 °C 24시간, 3회)·60 °C 4시간 건조 가루 20 g → 10% 파파인(100 mM 아세트산나트륨 pH 5.5, 5 mM EDTA·5 mM 시스테인, 20 mL/g) 60 °C 18시간 3회 → 0.5% CPC·에탄올 침전 → 에탄올 25·40·50% 분별 → 약 15 µg을 콘드로이티나제 AC 또는 ABC 0.01 U/mg(50 mM 에틸렌다이아민·82 mM 아세트산, pH 7.0) 37 °C 18시간 분해",
         "standard": "불포화 이당 표준 8종(α-ΔHexUA-GalNAc, ΔHexUA(2S)-GalNAc, -GalNAc(6S), -GalNAc(4S), (2S)-GalNAc(6S), -GalNAc(4,6S), (2S)-GalNAc(4S), (2S)-GalNAc(4,6S))과 머무름 시간 비교",
         "linearity": "", "lod": "", "loq": "", "recovery": ""},
     "rationale": "더마탄황산의 2,4-이황산 단위는 이 종 속 조직의 항응고·상처 치유 활성과 직접 연결되는 특징 성분이고, 황산기 위치가 분류군마다 달라 원료 확인 지표로 쓸 만하다[18][20][34].",
     "source": [20], "url": PMC + "PMC9693086/", "source_kind": "paper"},
    {"role": "literature", "compound": "Heparin (disaccharide composition)", "compound_ko": "헤파린 이당 조성",
     "part": "몸(속 조직)",
     "content": "ΔUA(2S)-GlcNS 47.5%, ΔUA(2S)-GlcNS(6S) 38.3%, ΔUA(2S)-GlcNS(3S) 8.0%, ΔUA(2S)-GlcNS(3S)(6S) 2.8%; aPTT 18 IU/mg",
     "method": "헤파리나제 혼합 분해 후 HPLC",
     "conditions": {"instrument": "", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "", "injection": "", "sample_prep": "", "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""},
     "rationale": "이 종 몸의 헤파린은 포유류 헤파린과 이당 조성이 달라 원료 구별에 쓸 수 있는 특징을 보인다. 전문 확인 못함(PMC 본문 없음, 초록 수치만 옮김)[17].",
     "source": [17], "url": PMC + "PMC2211419/", "source_kind": "paper"},
    {"role": "literature", "compound": "Metabolite profile (LC-MS)", "compound_ko": "대사체 프로파일(지방산·알칼로이드 등)",
     "part": "몸 전체(메탄올/클로로폼 추출 조추출물; 건조 전 무게 42.3 g)",
     "content": "대사체 피크 71개 검출(m/z 105–1365), 정량값 없음; 메탄올 조추출물 IC50 HeLa 41.15, HT29 42, MCF-7 125, HT1080 52 µmol/L",
     "method": "LC-MS(ESI 단일 사중극자) + XCMS-METLIN 다변량 분석",
     "conditions": {
         "instrument": "Waters ZQ LC-MS, 전자분무이온화(ESI) 단일 사중극자 질량분석기",
         "column": "C18, 3.3 µm, 15 cm × 2.1 mm(제조사 원문에 없음)",
         "mobile_phase": "A: 물 + 0.1% 폼산; B: 메탄올 + 0.1% 폼산",
         "gradient": "",
         "flow": "0.1 mL/min",
         "temp": "",
         "detection": "질량분석(양이온 모드 주석), XCMS-METLIN·HMDB·KEGG·LMID 검색",
         "injection": "5–20 µL",
         "sample_prep": "속슬렛 추출과 초음파 추출(메탄올/클로로폼)으로 조추출물 제조",
         "standard": "",
         "linearity": "", "lod": "", "loq": "", "recovery": ""},
     "rationale": "지방산·지질·알칼로이드가 주요 무리로, PCA·PLS-DA로 다른 멍게류와 종을 구별하는 화학분류 도구로 제안되었다. 개별 성분 정량이 아니라 프로파일 비교다[8].",
     "source": [8], "url": PMC + "PMC6010017/", "source_kind": "paper"},
    {"role": "literature", "compound": "HPLC fingerprint", "compound_ko": "HPLC 지문(특징 피크 13개)",
     "part": "몸 전체(산지별 시료 6개)",
     "content": "표준 지문과 특징 피크 13개 확립(정량값 없음)",
     "method": "HPLC 지문 분석",
     "conditions": {"instrument": "", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "", "injection": "", "sample_prep": "", "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""},
     "rationale": "산지가 다른 주름미더덕의 확인·품질 관리용으로 제안된 방법이다. 전문 확인 못함(중국어 논문, 초록만 확인)[32].",
     "source": [32], "url": PM + "16850716/", "source_kind": "paper"},
]

d = {
    "slug": "styela-plicata",
    "name_ko": "주름미더덕",
    "name_en": "Wrinkled sea squirt",
    "scientific_name": "Styela plicata (Lesueur, 1823)",
    "aliases": ["오만둥이", "오만디", "Wrinkled sea squirt", "Sea potato"],
    "sections": [{"key": k, "title": t, "body": b} for k, (t, b) in S.items()],
    "compounds": compounds,
    "markers": [],
    "nutrients": [],
    "production": [],
    "world": [],
    "assays": assays,
    "gi": [],
    "orgs": [],
    "sources": [{"n": n, "title": t, "url": u, "publisher": p, "accessed": a} for n, t, u, p, a in sources],
}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in d["sections"]:
    print(s["key"], len(s["body"]))
