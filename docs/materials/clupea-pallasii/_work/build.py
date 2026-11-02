import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
A = "2026-11-02"
def pm(n, title, doi, pub):
    return {"n": n, "title": title, "url": f"https://doi.org/{doi}", "publisher": pub, "accessed": A}
sources = [
 {"n": 1, "title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — Clupea pallasii 8행(청어·청어유·청어추출물·청어훈제분말: 부위 '-'; 청어알·건조청어알·염장청어알: 부위 '균핵'; 청어살: 부위 '죽순'; 모두 수산물·사용가능, 사용 조건 없음; 대서양청어 Clupea harengus·그물눈태평양청어 Ethmidium maculatum은 별도 행; data/raw/mfds_rawmtrl/I1020_20261013.json, docs/materials/clupea-pallasii/card.json)", "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
 pm(2, "Winter occurrence and spawning characteristics of Pacific herring (Clupea pallasii) in Jinhae Bay: An integrated survey using acoustic monitoring, gillnet sampling, and environmental DNA. PLoS One 2026 (PMC 전문 확인)", "10.1371/journal.pone.0338479", "PLOS ONE, PMC12872025 (PubMed 41637433)"),
 pm(3, "A chromosome-level reference genome for Pacific herring (Clupea pallasii) from the Bering Sea. GigaByte 2026 (PMC 전문 확인)", "10.46471/gigabyte.182", "GigaByte, PMC13219836 (PubMed 42221523)"),
 pm(4, "Biogeographic Structure and Mitonuclear Discordance Reveal Cryptic Diversity in Pacific Herring (Clupea pallasii). Ecol Evol 2025;15(11):e72452", "10.1002/ece3.72452", "Ecology and Evolution, PMC12638094 (PubMed 41282327)"),
 pm(5, "A Long-Standing Hybrid Population Between Pacific and Atlantic Herring in a Subarctic Fjord of Norway. Genome Biol Evol 2023;15(5)", "10.1093/gbe/evad069", "Genome Biology and Evolution, PMC10182735 (PubMed 37120751)"),
 pm(6, "Phylogeography of amphi-boreal fish: tracing the history of the Pacific herring Clupea pallasii in North-East European seas. BMC Evol Biol 2013;13:67", "10.1186/1471-2148-13-67", "BMC Evolutionary Biology, PMC3637224 (PubMed 23510113)"),
 pm(7, "Genetic structure of marine and lake forms of Pacific herring. PeerJ 2021;9:e12444", "10.7717/peerj.12444", "PeerJ, PMC8570158 (PubMed 34760402)"),
 pm(8, "Genomic Signatures of Freshwater Adaptation in Pacific Herring (Clupea pallasii). Genes 2022;13(10):1856", "10.3390/genes13101856", "Genes (MDPI), PMC9601299 (PubMed 36292743)"),
 pm(9, "Ancient DNA reveals phenological diversity of Coast Salish herring harvests over multiple centuries. Sci Rep 2022;12:13512", "10.1038/s41598-022-17656-4", "Scientific Reports, PMC9357025 (PubMed 35933511)"),
 pm(10, "Comparison of fatty acid profiles of spawning and non-spawning Pacific herring, Clupea harengus pallasi. Comp Biochem Physiol B 2007;146(4):504-511 (초록만 확인)", "10.1016/j.cbpb.2006.11.023", "Comparative Biochemistry and Physiology Part B (PubMed 17276118)"),
 pm(11, "Selenium content in seafood in Japan. Nutrients 2013;5(2):388-395 (PMC 전문 확인, 표 1·2에 Clupea pallasii 명시)", "10.3390/nu5020388", "Nutrients (MDPI), PMC3635200 (PubMed 23434904)"),
 pm(12, "Preparation and Identification of Antioxidative Peptides from Pacific Herring (Clupea pallasii) Protein. Molecules 2019;24(10):1946 (PMC 전문 확인)", "10.3390/molecules24101946", "Molecules (MDPI), PMC6572113 (PubMed 31117172)"),
 pm(13, "The effects of herring-roe lyophilized powder on lipid metabolism. J Tradit Complement Med 2016;6(3):247-251 (PMC 전문 확인; 청어알 산지 미국 알래스카 싯카, 학명은 논문에 적히지 않음)", "10.1016/j.jtcme.2015.04.002", "Journal of Traditional and Complementary Medicine, PMC4936758 (PubMed 27419088)"),
 pm(14, "Effects of dietary herring roe lipids on plasma lipid, glucose, insulin, and adiponectin concentrations in mice. J Agric Food Chem 2006;54(10):3750-3755 (초록만 확인; 염장 청어알 '가즈노코' 지질, 학명 미기재)", "10.1021/jf0531712", "Journal of Agricultural and Food Chemistry (PubMed 19127755)"),
 pm(15, "Combination effect of herring roe lipids and proteins on plasma lipids and abdominal fat weight of mouse. J Food Sci 2007;72(5):C231-C234 (초록만 확인; 학명 미기재)", "10.1111/j.1750-3841.2007.00356.x", "Journal of Food Science (PubMed 17995707)"),
 pm(16, "Ecological drivers of mercury concentrations in fish species in subsistence harvests from Kotzebue Sound, Alaska. Environ Res 2019;177:108622 (초록만 확인)", "10.1016/j.envres.2019.108622", "Environmental Research (PubMed 31419713)"),
 {"n": 17, "title": "Biological tags for stock separation in Pacific herring Clupea harengus pallasi in California. J Parasitol 1992;78(1):54-60 (초록만 확인)", "url": "https://pubmed.ncbi.nlm.nih.gov/1738068/", "publisher": "The Journal of Parasitology (PubMed 1738068)", "accessed": A},
 pm(18, "Marine mammal recovery is associated with the resurgence of a nematode parasite. Ecology 2025 (초록만 확인)", "10.1002/ecy.70221", "Ecology, PMC12509183 (PubMed 41064993)"),
 pm(19, "Detection of allergenic parvalbumin of Atlantic and Pacific herrings in fish products by PCR. Food Addit Contam Part A 2013;30(10):1679-1683 (초록만 확인)", "10.1080/19440049.2013.817024", "Food Additives & Contaminants Part A (PubMed 23886376)"),
 pm(20, "Spatial extent, magnitude, and patterns of persistent organochlorine pollutants in Pacific herring (Clupea pallasi) populations in the Puget Sound (USA) and Strait of Georgia (Canada). Sci Total Environ 2008;394(2-3):369-378 (초록만 확인)", "10.1016/j.scitotenv.2007.12.027", "Science of the Total Environment (PubMed 18314160)"),
 pm(21, "Time Trends of Persistent Organic Pollutants in Benthic and Pelagic Indicator Fishes from Puget Sound, Washington, USA. Arch Environ Contam Toxicol 2017;73(2):207-229 (초록만 확인)", "10.1007/s00244-017-0383-z", "Archives of Environmental Contamination and Toxicology, PMC5539278 (PubMed 28528416)"),
 pm(22, "Decreases in Concentrations and Human Dietary Intakes of Polychlorinated Biphenyls (PCBs) and Polybrominated Diphenyl Ethers (PBDEs) in Korean Seafood Between 2005 and 2017. Arch Environ Contam Toxicol 2021;81(2):199-209 (초록만 확인; 'herring'으로만 적혀 학명 미확인)", "10.1007/s00244-021-00860-0", "Archives of Environmental Contamination and Toxicology (PubMed 34081169)"),
 pm(23, "From the ocean to our kitchen table: anthropogenic particles in the edible tissue of U.S. West Coast seafood species. Front Toxicol 2024;6:1469995 (초록만 확인)", "10.3389/ftox.2024.1469995", "Frontiers in Toxicology, PMC11703854 (PubMed 39776763)"),
 pm(24, "Failure of population recovery in relation to disease in Pacific herring. Dis Aquat Organ 2010;90(1):1-14 (초록만 확인)", "10.3354/dao02210", "Diseases of Aquatic Organisms (PubMed 20597425)"),
 pm(25, "Viral hemorrhagic septicemia virus, Ichthyophonus hoferi, and other causes of morbidity in Pacific herring Clupea pallasi spawning in Prince William Sound, Alaska, USA. Dis Aquat Organ 1998;32(1):15-40 (초록만 확인)", "10.3354/dao032015", "Diseases of Aquatic Organisms (PubMed 9676259)"),
 pm(26, "Temporal changes in behavior during the group spawning event of Pacific herring (Clupea pallasii). Sci Rep 2025;15:11337 (초록만 확인)", "10.1038/s41598-025-95189-2", "Scientific Reports, PMC11965385 (PubMed 40175455)"),
 pm(27, "Pheromone-induced spawning of Pacific herring. I. Behavioral characterization. Horm Behav 1997;31(3):256-268 (초록만 확인)", "10.1006/hbeh.1997.1378", "Hormones and Behavior (PubMed 9213139)"),
 pm(28, "Vegetation preference and the puzzle of abandonment: high-quality spawning habitat remains unused by Pacific herring (Clupea pallasii). Mar Environ Res 2026;218:108067 (초록만 확인)", "10.1016/j.marenvres.2026.108067", "Marine Environmental Research (PubMed 42019095)"),
 pm(29, "Anti-Obesity and Hepatoprotective Effects of Herring–Saury Oil Fermented by Lactobacillus brevis KCCM13538P in High-Fat-Diet-Induced Mice. Foods 2025;14(16):2862 (PMC 전문 확인; 추출본에서 청어·꽁치 학명은 보이지 않음)", "10.3390/foods14162862", "Foods (MDPI), PMC12385245 (PubMed 40870774)"),
 {"n": 30, "title": "해수부, 청어 금지체장(20 cm) 위반 집중 단속 보도(2022년 6월; WebSearch 검색 결과 요약으로만 확인, 기사 본문과 해양수산부 보도자료 원문은 이 환경에서 열지 못함)", "url": "https://m.dailian.co.kr/news/view/1121116", "publisher": "데일리안", "accessed": A},
 pm(31, "Development of genomic resources for Pacific Herring through targeted transcriptome pyrosequencing. PLoS One 2012;7(2):e30908 (초록만 확인)", "10.1371/journal.pone.0030908", "PLOS ONE, PMC3288011 (PubMed 22383979)"),
 pm(32, "Diversity of Lipid Distribution in Fish Skeletal Muscle. Zoolog Sci 2016;33(2):170-178 (초록만 확인)", "10.2108/zs150096", "Zoological Science (PubMed 27032682)"),
 pm(33, "[Determination of sodium chlorite in processed herring roe by ion chromatography with a conductivity detector]. Shokuhin Eiseigaku Zasshi 2005;46(4):161-164 (영문 초록만 확인; 학명 미기재)", "10.3358/shokueishi.46.161", "Journal of the Food Hygienic Society of Japan (PubMed 16180686)"),
]

S = {}
S["overview"] = ("청어(Clupea pallasii)는 청어목 청어과(Clupeidae) 청어속에 드는 바닷물고기로, 영어로는 Pacific herring(태평양청어)이라 부른다[1, 2]. "
 "식약처 「식품원료 목록」에는 학명 Clupea pallasii로 청어·청어살·청어알·건조청어알·염장청어알·청어유·청어추출물·청어훈제분말 8개 원료명이 올라 있고, 모두 수산물로 분류된 '사용가능' 원료이며 별도의 사용 조건은 없다[1]. "
 "이 목록의 부위 칸은 청어·청어유·청어추출물·청어훈제분말이 '-', 청어알·건조청어알·염장청어알이 '균핵', 청어살이 '죽순'으로 적혀 있으며, 여기서는 원자료 표기를 그대로 옮겼다[1]. "
 "건강기능식품 고시형 원료의 원재료 목록에는 없어 식약처가 정한 지표성분은 없다[1].\n\n"
 "북태평양에 넓게 분포하며 우리나라 동해와 남해 동부, 일본 중·북부, 베링해, 알래스카까지 산다[2]. "
 "플랑크톤과 상위 포식자를 잇는 대표적인 먹이 물고기(forage fish)이자 주요 상업 어종이다[2, 3]. "
 "국내 공공기관의 청어 식품성분표 값은 이번 조사에서 확인하지 못함.")
S["history"] = ("미국 퓨젓사운드의 원주민(코스트 샐리시) 패총에서 나온 청어 뼈의 고대 DNA를 분석한 연구는 여러 세기 동안 산란 시기가 다른 여러 무리의 청어가 함께 잡혀 식량으로 쓰였음을 보여 주었고, 그 가운데 오래된 유적은 910–685 cal BP로 연대가 매겨졌다[9]. "
 "북미 알래스카 프린스윌리엄사운드의 청어 자원량은 1992년 추정 9.8 × 10^7 kg에서 1994년 1.5 × 10^7 kg으로 줄었고, 이후 질병이 회복을 늦춘 요인으로 분석되었다[24, 25]. "
 "캐나다 조지아 해협에서는 지난 한 세기 동안 산란장이 크게 줄어 여러 옛 산란장이 버려지고 한 지역에 산란이 몰렸다[28].\n\n"
 "우리나라의 청어 어획량은 1990년대 중반부터 2000년까지 연 1만 톤 이상이었다가 2005년에 1만 톤 아래로 줄었고, 그 뒤 다시 늘어 2020년까지 2–3만 톤 사이를 오갔다[2]. "
 "청어는 겨울 찬 바닷바람에 반쯤 말리는 경북 포항 일대의 전통 수산물인 과메기의 원료로 꽁치와 함께 쓰인다고 소개되었다[29]. "
 "과메기 원료의 시대별 변화를 적은 공공기관 자료는 확인하지 못함.")
S["biology"] = ("청어는 찬물을 좋아하는 어종으로 수온 2–10 ℃가 유지되는 수심 60–90 m에 주로 머물고, 겨울에 무리를 지어 연안으로 들어와 암초와 해조류에 끈적한 알을 붙여 낳는다[2]. "
 "진해만 조사(2022년 11월–2023년 3월)에서는 바닥 수온이 10 ℃ 아래로 내려가자 청어가 나타나기 시작했고, 바닥 수온이 평균 6.72 ℃였던 1월에 어획이 가장 많았으며, 산란기 성어의 가랑이 길이는 암컷 23.3–27.5 cm, 수컷 23.4–25.4 cm였다[2]. "
 "이 조사에서 청어는 밤에 더 많이 탐지되어 야간 산란 행동과 맞았고, 수정란은 약 12일 뒤 부화한다고 정리되었다[2].\n\n"
 "수컷의 정액(milt)과 정소에는 산란을 일으키는 페로몬이 있어 냄새로 무리 산란을 이끄는 것으로 보고되었다[27]. "
 "가속도 기록계를 단 911마리 수조 실험에서는 한 개체가 행동을 바꾸면 30–40분 안에 많은 개체가 동시에 따라 했고, 이런 변화가 105–210분 주기로 되풀이되었다[26]. "
 "산란 중인 개체는 지질이 크게 줄어 조직별 지질이 습중량 1.9–3.4%로, 산란하지 않는 개체(10.5–16%)보다 훨씬 낮았다[10]. "
 "회유성 어종인 청어는 피부밑 지방 조직과 적색근 지질로 이루어진 두꺼운 지질층을 지닌다[32].")
S["related_species"] = ("청어(C. pallasii)와 대서양청어(Clupea harengus)는 약 200만 년 전 공통 조상에서 갈라진 자매종이다[5]. "
 "식약처 「식품원료 목록」은 대서양청어를 청어와 다른 별도의 원료로 올려 두었으며, 이 문서는 대서양청어 자료를 섞지 않았다[1]. "
 "같은 목록의 '그물눈태평양청어'는 이름에 태평양청어가 들어가지만 학명이 Ethmidium maculatum(영문 Pacific menhaden)인 다른 종이다[1]. "
 "옛 논문은 청어를 대서양청어의 아종으로 보아 Clupea harengus pallasi라고 적기도 했다[10, 17].\n\n"
 "노르웨이 북부 발스피오르에는 대서양청어 분포 안에 태평양청어 무리가 있고, 대서양청어 유전자가 25–26% 섞인 잡종 집단이 수천 세대 이어져 왔다[5]. "
 "북동 유럽 백해 등의 태평양청어는 빙하기 뒤 북서태평양에서 건너간 무리로 판단되었다[6]. "
 "러시아 연안에는 짧은 생활사로 기수역 호수에서 사는 호수형 청어가 있어 바다형과 유전적으로 구별되었다[7, 8]. "
 "알래스카 반도·알류샨 열도를 경계로 베링해 무리와 알래스카만 무리가 유전적으로 뚜렷이 나뉘어, 둘이 서로 다른 종일 수 있다는 의견도 나왔다[3, 4].")
S["cultivation"] = ("청어는 양식보다 자연 자원을 잡아 이용하는 어종이며, 국내 양식 생산 통계는 이번 조사에서 확인하지 못함. "
 "우리나라는 어린 청어를 보호하려고 20 cm보다 작은 청어의 어획을 금지하고 있다는 설명이 2022년 시행으로 논문에 적혀 있다[2]. "
 "언론 보도 요약으로는 해양수산부가 20 cm 이하 청어의 포획부터 유통·가공·판매까지 금지했고 2022년 6월 온·오프라인 유통을 집중 단속했다고 하나, 보도자료 원문은 열지 못했다[30].\n\n"
 "경남 진해만은 청어의 주요 겨울 산란장으로, 음향 장비·자망·환경 DNA를 함께 쓴 조사에서 성어의 유입이 12월 말에 시작해 1월 중·하순에 가장 많았고 2월 말에 줄었다[2]. "
 "산란기 네 차례 자망 조사에서 청어는 전체 어획의 98% 넘게 차지했다[2]. "
 "연구진은 산란기 어획 제한과 산란장 보호구역, 어구·크기별 어획 제한이 필요하다고 제안했다[2]. "
 "캐나다 조지아 해협에서는 청어가 외래 갈조류 Sargassum muticum 같은 복잡한 구조의 해조에 알을 더 많이 낳았지만, 버려진 산란장의 해조 상태가 나쁘지 않아 산란장 회복에는 자원 관리가 더 중요하다고 보았다[28]. "
 "국내 청어의 연도별 공식 어획 통계(해양수산부·통계청 원자료)는 이 환경에서 열지 못해 확인하지 못함.")
S["processing"] = ("식약처 목록에는 청어살·청어알·건조청어알·염장청어알·청어유·청어추출물·청어훈제분말처럼 여러 가공 형태가 원료로 올라 있다[1]. "
 "알래스카 싯카에서 잡은 청어알을 동결건조한 가루(하루 15 g에 DHA 540 mg, EPA 300 mg)를 8주 동안 먹인 33명 대상 무작위 이중맹검 시험에서는 위약군보다 HDL 콜레스테롤이 늘고 유리지방산이 줄었으나 LDL 콜레스테롤 차이는 없었다[13]. "
 "이 시험의 참가자는 33명이었고, 논문은 청어알의 학명을 적지 않았다[13].\n\n"
 "일본의 염장 청어알(가즈노코) 지질을 먹인 생쥐 실험에서는 혈장 총콜레스테롤·중성지방·포도당이 낮아졌지만, 이는 동물 결과이고 학명이 적혀 있지 않다[14]. "
 "청어알 지질은 인지질이 74%였고 콜레스테롤 9%를 함유했으며, 단백질과 함께 먹인 생쥐에서 복부 지방 무게가 줄었다[15]. "
 "중국 칭다오 시장에서 산 태평양청어 살을 트립신으로 가수분해해 항산화 펩타이드 두 가지를 분리했으나, 이는 세포 실험 단계의 결과다[12]. "
 "청어·꽁치 부산물 기름(1:9 혼합)을 젖산균으로 발효시킨 기름은 고지방식 생쥐에서 체중 증가와 간 손상 지표를 줄였지만, 사람 효과는 확인되지 않았다[29]. "
 "일본에서는 아염소산나트륨으로 처리한 가공 청어알의 잔류량을 이온 크로마토그래피로 재는 시험법이 개발되었다(정량한계 5 mg/kg)[33].")
S["genetics"] = ("알래스카 코체부에서 잡은 암컷으로 만든 첫 염색체 수준 청어 유전체(Clupal_KotzSound)는 약 795 Mb가 26개 염색체에 배치되었고, BUSCO 완성도는 본문 기준 98.15%(초록에는 97.7%), GC 함량은 44%였다[3]. "
 "이 유전체와 대서양청어 유전체를 비교한 결과 염색체 배열은 대체로 같았지만 역위 407개가 확인되었고, 대서양청어 12번 염색체의 7.8 Mb 역위(초유전자)는 이 유전체에서 찾지 못했다[3]. "
 "그전에는 캐나다 브리티시컬럼비아 개체의 조각(스캐폴드) 수준 유전체(1,379개 스캐폴드)만 있었다[3].\n\n"
 "알래스카만과 베링해 등 7곳 120마리의 저심도 전장 유전체 분석은 약 560만 개 핵 SNP와 미토콘드리아 SNP 267개로 알류샨 열도를 경계로 한 두 집단을 확인했다[4]. "
 "미토콘드리아 DNA 연구는 대서양청어가 대양 전체에서 비슷한 반면 태평양청어는 태평양 안에서 동서로 깊게 나뉜다고 보고했다[6]. "
 "간과 정소 전사체 분석으로 4만 개 넘는 콘티그와 SNP 후보 10,933개가 확보되었다[31]. "
 "호수형 청어에서는 바다형과 구별되는 SNP를 지닌 유전자 253개가 찾아졌고 일부는 삼투 조절과 관련되었다[8].")
S["safety"] = ("식약처 「식품원료 목록」에서 청어와 그 가공 원료 8종은 별도 조건 없이 '사용가능'이며, 건강기능식품 고시형 원료가 아니어서 고시 섭취 시 주의사항은 없다[1]. "
 "청어를 따로 다룬 국내 공공기관의 알레르기·잔류물질·히스타민 정보는 이번 조사에서 확인하지 못함. "
 "생선 알레르기의 주요 항원인 파브알부민 베타 2가 청어에도 있어, 이를 PCR로 찾는 시험법이 개발되었다[19].\n\n"
 "알래스카 코체부 해역 8개 어종(청어 포함) 297마리의 총수은은 습중량 3.4–235.2 ng/g이었고, 논문은 모든 종이 알래스카주 무제한 섭취 기준(200 ng/g) 안에 든다고 결론지었으나 청어만의 수치는 초록에서 확인하지 못함[16]. "
 "미국 캘리포니아 청어에서는 고래회충(Anisakis simplex)과 Contracaecum 같은 회충류 유충이 기생충 조사 대상에 포함되었고, 퓨젓사운드 청어에서도 Contracaecum 유충이 확인되었다[17, 18]. "
 "퓨젓사운드 청어는 조지아 해협 청어보다 PCB가 3–9배 많았고, PBDE·DDT는 해마다 4.2–8.1% 줄었지만 PCB는 개발이 적은 해역의 두 무리에서만 해마다 2.3–4.0% 줄었다[20, 21]. "
 "국내 수산물 조사에서는 청어·고등어·참치 같은 기름진 생선의 PCB·PBDE가 높았으나 섭취량은 내용 일일섭취량보다 훨씬 낮았다(학명 미기재)[22]. "
 "미국 서부 해안 수산물 조사에서는 청어를 포함한 어류 근육 1 g당 인공 미세입자가 0.02–1.08개 나왔다[23].")

compounds = [
 {"name": "Docosahexaenoic acid", "name_ko": "DHA(도코사헥사엔산)", "class": "n-3 지방산", "role": "nutrient", "part": "정소·난소 등 조직 지질", "content_text": "산란 개체의 정소(milt)·난소에서 고도불포화지방산 중 비율이 가장 큼(초록에 수치 없음); 동결건조 청어알 가루 15 g당 540 mg[13]", "activity_ko": "산란 개체의 기관 지질에서 n-3 지방산이 상대적으로 많았다[10]", "source": [10, 13]},
 {"name": "Eicosapentaenoic acid", "name_ko": "EPA(에이코사펜타엔산)", "class": "n-3 지방산", "role": "nutrient", "part": "알(동결건조 가루)", "content_text": "동결건조 청어알 가루 15 g당 300 mg (알래스카 싯카산, 학명 미기재)", "activity_ko": "DHA와 함께 청어알 가루 시험에서 섭취된 주요 n-3 지방산이다[13]", "source": [13]},
 {"name": "Oleic acid", "name_ko": "올레산(C18:1n-9)", "class": "단일불포화지방산", "role": "nutrient", "part": "간·장·알·정소·살", "content_text": "모든 조직 지질의 주된 단일불포화지방산; 산란 개체에서 유의하게 감소(초록에 수치 없음)", "activity_ko": "산란에 따른 지질 소모를 보여 주는 지방산으로 보고되었다[10]", "source": [10]},
 {"name": "Gondoic acid", "name_ko": "곤도산(C20:1n-9)", "class": "단일불포화지방산", "role": "nutrient", "part": "살", "content_text": "살에 많고 소화기관·생식소에는 적음(초록에 수치 없음)", "activity_ko": "살 지질의 특징적인 긴사슬 모노엔이다[10]", "source": [10]},
 {"name": "Cetoleic acid", "name_ko": "세톨레산(C22:1n-11)", "class": "단일불포화지방산", "role": "nutrient", "part": "살", "content_text": "살에 많고 소화기관·생식소에는 적음(초록에 수치 없음)", "activity_ko": "곤도산과 함께 살 지질에 많은 긴사슬 모노엔이다[10]", "source": [10]},
 {"name": "Linoleic acid", "name_ko": "리놀레산(C18:2n-6)", "class": "n-6 지방산", "role": "nutrient", "part": "간·장·알·정소·살", "content_text": "n-6 지방산 가운데 눈에 띄는 양이 있었고 산란 개체에서 비율이 더 높음(초록에 수치 없음)", "activity_ko": "청어 조직 지질의 주요 n-6 지방산이다[10]", "source": [10]},
 {"name": "Arachidonic acid", "name_ko": "아라키돈산(C20:4n-6)", "class": "n-6 지방산", "role": "nutrient", "part": "간·장·알·정소·살", "content_text": "n-6 지방산 가운데 눈에 띄는 양이 있었고 산란 개체에서 비율이 더 높음(초록에 수치 없음)", "activity_ko": "리놀레산과 함께 청어 조직 지질의 n-6 지방산이다[10]", "source": [10]},
 {"name": "Selenium", "name_ko": "셀레늄(총량)", "class": "무기질", "role": "nutrient", "part": "껍질 있는 필레·난소", "content_text": "껍질 있는 필레 0.40 mg/kg, 난소 1.07 mg/kg (일본 시판품; 원문 표 2는 'ovary', 초록은 'salted ovary products'로 적음)", "activity_ko": "항산화 효소의 구성 성분인 필수 미량 영양소로, 청어 난소가 조사한 가식부 가운데 높은 편이었다[11]", "source": [11]},
 {"name": "Leu-His-Asp-Glu-Leu-Thr", "name_ko": "항산화 펩타이드 P1(LHDELT)", "class": "펩타이드", "role": "bioactive", "part": "살(트립신 가수분해물)", "content_text": "분자량 726.35 Da; 세포 항산화 IC50 1.19 ± 0.05 mg/mL", "activity_ko": "HepG2 세포 실험에서 과산화수소에 의한 산화 손상을 줄였다(세포 실험)[12]", "source": [12]},
 {"name": "Lys-Glu-Glu-Lys-Phe-Glu", "name_ko": "항산화 펩타이드 P2(KEEKFE)", "class": "펩타이드", "role": "bioactive", "part": "살(트립신 가수분해물)", "content_text": "분자량 808.40 Da; 세포 항산화 IC50 1.04 ± 0.06 mg/mL, DPPH IC50 4.37 ± 0.26 mg/mL", "activity_ko": "P1보다 항산화 활성이 조금 더 높았다(세포·시험관 실험)[12]", "source": [12]},
 {"name": "Phosphatidylcholine", "name_ko": "포스파티딜콜린(인지질)", "class": "인지질", "role": "nutrient", "part": "알", "content_text": "청어알 지질의 74%가 인지질(학명 미기재 시료)[15]; DHA·EPA가 청어알 포스파티딜콜린의 주된 구성 성분이라는 설명[13]", "activity_ko": "DHA·EPA가 인지질 형태로 들어 있어 잘 산화되지 않는다고 설명되었다[13]", "source": [13, 15]},
 {"name": "Cholesterol", "name_ko": "콜레스테롤", "class": "스테롤", "role": "nutrient", "part": "알", "content_text": "청어알 100 g당 260 mg(문헌 인용)[13]; 청어알 지질 중 9%(학명 미기재 시료)[15]", "activity_ko": "청어알은 다른 생선알보다 콜레스테롤이 적다고 소개되었다[13]", "source": [13, 15]},
 {"name": "Parvalbumin beta 2", "name_ko": "파브알부민 베타 2", "class": "단백질(알레르기 항원)", "role": "bioactive", "part": "살", "content_text": "함량 수치 없음; pvalb 2 유전자 189 bp 증폭으로 검출, 검출한계 10 pg/µL DNA", "activity_ko": "청어의 주요 생선 알레르기 항원이다[19]", "source": [19]},
]

assays = [
 {"role": "literature", "compound": "Selenium", "compound_ko": "셀레늄(총량)", "part": "껍질 있는 필레·난소", "content": "필레 0.40 mg/kg, 난소 1.07 mg/kg[11]", "method": "수소화물 발생 원자흡광분광법(HG-AAS)",
  "conditions": {"instrument": "", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "수소화물 발생 원자흡광", "injection": "",
   "sample_prep": "도쿄 시장 시료 −40 °C 냉동 보관; 3개체 필레를 섞어 복합 시료 1개, 복합 시료 3개 평균; 시료 0.1–0.2 g을 질산:과염소산(1:2) 1 mL로 200–220 °C에서 분해", "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "셀레늄은 생선이 주요 공급원인 필수 미량 영양소로, 이 논문은 Clupea pallasii를 학명으로 적고 필레와 난소의 총셀레늄을 정량했다[11]. 전문(방법) 확인 — 기기 모델·검량·검출한계·회수율은 본문에 없음[11].", "source": [11], "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC3635200/", "source_kind": "paper"},
 {"role": "literature", "compound": "Antioxidant peptides (LHDELT, KEEKFE)", "compound_ko": "항산화 펩타이드(LHDELT·KEEKFE)", "part": "살(트립신 가수분해물)", "content": "최종 분획 PHPH-III-5-2 수율 2.56 mg/(20 mg PHPH-III-5); P1 726.35 Da, P2 808.40 Da[12]", "method": "RP-HPLC 분취 → LC-MS/MS 동정",
  "conditions": {"instrument": "분취: HPLC 시스템(모델 미기재); 동정: 고분해능 오비트랩 질량분석기(Q Exactive)", "column": "분취: XBridge BEH C18, 19 × 250 mm; 동정: C18(규격 미기재)", "mobile_phase": "분취: 0.1% TFA 함유 아세토나이트릴; 동정: 0.1% 폼산 함유 아세토나이트릴", "gradient": "분취: 아세토나이트릴 0–20%(30분, 선형); 동정: 0–90%(40분, 선형)", "flow": "분취 5.0 mL/min", "temp": "", "detection": "분취 220 nm; MS 스펙트럼 m/z 350–1800", "injection": "",
   "sample_prep": "중국 칭다오 시장 태평양청어 살을 다져 냉동; 트립신 가수분해(효소 1394.02 U/g, 7.0 h, pH 6.78, 물:원료 3.51, 32.06 °C) → 100 °C 15분 불활성화 → 18,000×g 10분 원심 → 한외여과(10,000·3500 Da) → Sephadex G-25(2.6 × 80 cm, 증류수, 0.5 mL/min, 220 nm)", "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "청어 단백질 유래 생리활성 펩타이드를 분리·동정한 조건이며, 함량 정량 시험법은 아니다[12]. 전문(방법) 확인 — 검출·정량한계와 회수율은 해당 없음/본문에 없음[12].", "source": [12], "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC6572113/", "source_kind": "paper"},
 {"role": "literature", "compound": "Fatty acids (DHA, oleic acid etc.)", "compound_ko": "지방산 조성(DHA·올레산 등)", "part": "간·장·알·정소·살", "content": "조직 지질 습중량 기준 산란 개체 1.9–3.4%, 비산란 개체 10.5–16%[10]", "method": "지방산 조성 분석(초록에 기기 미기재)",
  "conditions": {"instrument": "", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "", "injection": "", "sample_prep": "", "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "산란 여부에 따른 청어 조직별 지질량과 지방산 조성을 비교한 연구로, DHA와 긴사슬 모노엔이 청어 지질의 특징 성분이다[10]. 전문 확인 못함 — 초록만 봐서 분석 조건 칸은 비워 둠[10].", "source": [10], "url": "https://doi.org/10.1016/j.cbpb.2006.11.023", "source_kind": "paper"},
]

d = {
 "slug": "clupea-pallasii", "name_ko": "청어", "name_en": "Pacific herring",
 "scientific_name": "Clupea pallasii Valenciennes, 1847",
 "aliases": ["청어", "태평양청어", "Pacific herring", "Clupea pallasi", "Clupea harengus pallasi"],
 "sections": [
  {"key": "overview", "title": "한눈에 보기", "body": S["overview"]},
  {"key": "history", "title": "이용·자원 역사", "body": S["history"]},
  {"key": "biology", "title": "어종·생태", "body": S["biology"]},
  {"key": "related_species", "title": "관련 종·이름", "body": S["related_species"]},
  {"key": "cultivation", "title": "어획·자원 관리", "body": S["cultivation"]},
  {"key": "processing", "title": "가공·이용 연구", "body": S["processing"]},
  {"key": "genetics", "title": "유전 정보", "body": S["genetics"]},
  {"key": "safety", "title": "안전성", "body": S["safety"]},
 ],
 "compounds": compounds, "markers": [], "assays": assays, "nutrients": [], "production": [], "world": [], "gi": [], "orgs": [],
 "sources": sources,
}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in d["sections"]: print(s["key"], len(s["body"]))
