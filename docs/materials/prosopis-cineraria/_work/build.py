import json
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "dossier.json"
ACC = "2026-11-02"
PM = "https://pubmed.ncbi.nlm.nih.gov/{}/"
PMC = "https://pmc.ncbi.nlm.nih.gov/articles/{}/"

sources = [
    (1, "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — Ghaf나무(Prosopis cineraria (L.) Druce / Prosopis spicigera L.) 항목", "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "식품의약품안전처", "2026-10-13"),
    (2, "Hughes CE et al. Disintegration of the genus Prosopis L. (Leguminosae, Caesalpinioideae, mimosoid clade). PhytoKeys 205:147-189 (2022). doi:10.3897/phytokeys.205.75379", PMC.format("PMC9849005"), "Pensoft (PMC)", ACC),
    (3, "The Genome of the Mimosoid Legume Prosopis cineraria, a Desert Tree. Int J Mol Sci 23(15):8503 (2022). doi:10.3390/ijms23158503", PMC.format("PMC9369113"), "MDPI (PMC)", ACC),
    (4, "Population Genomics and Genetic Diversity of Prosopis cineraria in the United Arab Emirates: Insights for Conservation in Arid Ecosystems. Plants (Basel) 14(19):2970 (2025). doi:10.3390/plants14192970", PMC.format("PMC12526342"), "MDPI (PMC)", ACC),
    (5, "A Review on the Ayurvedic Herb Prosopis cineraria (L) Druce. Ancient Science of Life 20(1-2):58-70 (2000)", PMC.format("PMC3336424"), "Ancient Science of Life (PMC)", ACC),
    (6, "Ethnopharmacological and Phytopharmaceutical Evaluation of Prosopis cineraria: An Overview and Future Prospects. Curr Drug Metab (2018). doi:10.2174/1389200218666171031125439 (초록)", PM.format("29086686"), "Bentham Science (PubMed)", ACC),
    (7, "Pharmacological Evaluation of Prosopis cineraria (L.) Druce in Gastrointestinal, Respiratory, and Vascular Disorders. Evid Based Complement Alternat Med 2012:735653. doi:10.1155/2012/735653", PMC.format("PMC3540920"), "Hindawi (PMC)", ACC),
    (8, "Antihyperglycemic, antihyperlipidemic and antioxidative potential of Prosopis cineraria bark. Indian J Clin Biochem (2010). doi:10.1007/s12291-010-0035-9 (초록)", PM.format("23105909"), "Springer (PubMed)", ACC),
    (9, "Prosopis cineraria: a potential nootropic agent. Pharm Biol (2012). doi:10.3109/13880209.2012.666253 (초록)", PM.format("22906223"), "Taylor & Francis (PubMed)", ACC),
    (10, "Neuroprotective effects of Prosopis cineraria L. ameliorate Alzheimer's disease manifestations. J Ethnopharmacol (2025). doi:10.1016/j.jep.2025.121052 (초록)", PM.format("41421404"), "Elsevier (PubMed)", ACC),
    (11, "In vitro and in vivo antidiabetic activity of isolated fraction of Prosopis cineraria against streptozotocin-induced experimental diabetes: A mechanistic study. Biomed Pharmacother (2018). doi:10.1016/j.biopha.2018.09.099 (초록)", PM.format("30372801"), "Elsevier (PubMed)", ACC),
    (12, "Evaluation of antibacterial and antidiarrheal properties of Prosopis cineraria in Albino rats. 3 Biotech (2025). doi:10.1007/s13205-025-04432-0 (초록; PMC 전문 본문은 받지 못함)", PM.format("40726568"), "Springer (PubMed)", ACC),
    (13, "Antitumour activity of Prosopis cineraria (L.) Druce against Ehrlich ascites carcinoma-induced mice. Nat Prod Res (2011). doi:10.1080/14786419.2010.536159 (초록)", PM.format("21462080"), "Taylor & Francis (PubMed)", ACC),
    (14, "Phytocosmeceutical formulation development, characterization and its in-vivo investigations. Biomed Pharmacother 107:806-817 (2018). doi:10.1016/j.biopha.2018.08.024 (초록)", PM.format("30142542"), "Elsevier (PubMed)", ACC),
    (15, "Prosopis cineraria (Ghaf) Extract as a Natural Ingredient for Anti-Aging Dermocosmetic Applications. Antioxidants (Basel) 15(8):938 (2026). doi:10.3390/antiox15080938", PMC.format("PMC13509287"), "MDPI (PMC)", ACC),
    (16, "Effect of a novel dietary supplement Khejri, and Spirulina supplementation on lipid profile in cricket players. Front Sports Act Living (2023). doi:10.3389/fspor.2022.1075388", PMC.format("PMC9885189"), "Frontiers (PMC)", ACC),
    (17, "Monitoring of Essential and Toxic Elements in Leaves, Branches, and Stem of Prosopis cineraria (as Anti-Inflammatory) Growing in Iran. Biol Trace Elem Res (2020). doi:10.1007/s12011-020-02103-0 (초록)", PM.format("32212045"), "Springer (PubMed)", ACC),
    (18, "Oxidative stress mediated cytotoxicity in leukemia cells induced by active phyto-constituents isolated from traditional herbal drugs of West Bengal. J Ethnopharmacol (2019). doi:10.1016/j.jep.2019.112527 (초록)", PM.format("31891796"), "Elsevier (PubMed)", ACC),
    (19, "Desert legume Prosopis cineraria as a novel source of antioxidant flavonoids/isoflavonoids: Biochemical characterization of edible pods for potential functional food development. Biochem Biophys Rep (2022). doi:10.1016/j.bbrep.2022.101210 (초록)", PMC.format("PMC8841892"), "Elsevier (PMC)", ACC),
    (20, "Microbiome properties in the root nodules of Prosopis cineraria, a leguminous desert tree. Microbiol Spectr (2024). doi:10.1128/spectrum.03617-23 (초록)", PMC.format("PMC11237379"), "ASM (PMC)", ACC),
    (21, "Tissue Culture of Desert Trees: I. Clonal Multiplication of Prosopis cineraria by Bud Culture. J Plant Physiol (1984; PubMed 등재 2012). doi:10.1016/S0176-1617(84)80118-2 (초록)", PM.format("23194572"), "Elsevier (PubMed)", ACC),
    (22, "The effects of replacing Rhodes grass (Chloris gayana) hay with ghaf (Prosopis cineraria) pods on the performance of Omani native sheep. Trop Anim Health Prod (2004). doi:10.1023/b:trop.0000016829.63985.2c (초록)", PM.format("15080543"), "Springer (PubMed)", ACC),
    (23, "Prosopis cineraria leaf tannins: their inhibitory effect upon ruminal cellulase and the recovery of inhibition by polyethylene glycol-4000. Basic Life Sci (1992). doi:10.1007/978-1-4615-3476-1_41 (초록)", PM.format("1417696"), "Springer (PubMed)", ACC),
    (24, "Exploring genetic variability in Prosopis cineraria using two gene targeted CAAT box-derived polymorphism (CBDP) and start codon targeted (SCoT) polymorphism markers. Mol Biol Rep (2018). doi:10.1007/s11033-018-4400-8 (초록)", PM.format("30255277"), "Springer (PubMed)", ACC),
    (25, "Impact of land use practices on faunal abundance, nutrient dynamics and biochemical properties of desert pedoecosystem. Environ Technol 26(11):1205-15 (2005). doi:10.1080/09593332608618602 (초록)", PM.format("16335596"), "Taylor & Francis (PubMed)", ACC),
    (26, "Vanishing oases (Down To Earth) — 1730년 케자를리(Khejarli) 마을 사건 관련 기사. WebSearch 검색 요약으로만 확인, 원문은 열지 못함", "https://www.downtoearth.org.in/news/vanishing-oases-59407", "Down To Earth (Centre for Science and Environment)", ACC),
    (27, "Felling of Rajasthan's state tree 'khejri' rampant on solar plant sites in desert areas (PTI 통신 기사, 2025-06-15). WebSearch 검색 요약으로만 확인, 원문은 열지 못함", "https://www.theweek.in/wire-updates/national/2025/06/15/des9-rj-jodhpur-khejri.html", "The Week (PTI)", ACC),
    (28, "Retraction Note: Attenuating effect of Prosopis cineraria against paraquat-induced toxicity in prepubertal mice, Mus musculus. Environ Sci Pollut Res Int (2023). doi:10.1007/s11356-023-30050-5", PM.format("37743452"), "Springer (PubMed)", ACC),
    (29, "Letter: An unconventional legume — Prosopis cineraria. Am J Clin Nutr 27(8):1035 (1974). doi:10.1093/ajcn/27.8.1035 (제목만 확인, 초록 없음)", PM.format("4213851"), "American Journal of Clinical Nutrition (PubMed)", ACC),
    (30, "Monitoring structural assets of bi-species groves according to land use types: a case study from arid plains. Environ Monit Assess 168:121-31 (2010). doi:10.1007/s10661-009-1096-1 (초록)", PM.format("19603275"), "Springer (PubMed)", ACC),
]

S = {}
S["overview"] = ("한눈에 보기", """Ghaf나무(Prosopis cineraria (L.) Druce)는 콩과(Fabaceae)의 미모사 계통에 속하는 사막 나무로, 근동과 인도아대륙이 원산이며 매우 더운 사막에서 잘 자란다[3]. 아랍어로 가프(Ghaf), 인도에서는 케즈리(khejri), 파키스탄에서는 잔드(jand)·잔디(jandi) 등으로 불리고, 산스크리트어로는 샤미(shami)라 한다[5, 7, 16]. 아라비아반도에서 가장 흔한 야생 콩과 나무이며 아랍에미리트(UAE)의 나라 나무다[3, 4].

식품의약품안전처 「식품원료 목록」에서 Ghaf나무는 식품에 사용할 수 있는 원료(사용가능)이며, 원료명은 'Ghaf나무껍질', 사용 조건은 '사용가능부위 : 나무껍질'이다[1]. 목록에는 학명이 Prosopis cineraria (L.) Druce와 이명 Prosopis spicigera L.로, 영어 이름이 Jand·Jandi·Shum으로 적혀 있다[1]. 건강기능식품 고시형 원료의 원재료로 쓰인다는 기록은 목록 자료에서 확인하지 못함.

나무껍질(줄기 껍질)은 인도·파키스탄 전통의학에서 기침·천식·이질·류머티즘 등에 쓰여 왔다[5, 7]. 줄기 껍질의 클로로포름 분획에서 루페올·β-시토스테롤·스티그마스테롤과 새 화합물 2종이 분리되었고, 껍질 에틸아세테이트 분획에서는 클로로겐산·켐페롤·퀘르세틴이 확인되었다[10, 11]. 껍질 추출물의 효과는 대부분 동물·시험관 연구이며, 사람에서 껍질을 먹었을 때의 효과를 본 임상시험은 이번 조사에서 확인하지 못함.""")

S["history"] = ("역사", """인도 아유르베다 문헌은 샤미를 쓰고 매운맛에 성질이 차고 떫으며 설사를 일으키는 약재로 적고, 담(카파) 이상·기침·현기증·호흡곤란·치질·기생충에 이롭다고 했다[5]. 이 나무는 모든 부위가 쓰여 인도에서 '칼프 타루(Kalp Taru)', 곧 '경이로운 나무'라 불린다고 정리되어 있다[6]. 인도·파키스탄·방글라데시·UAE·사우디아라비아·이란에서 여러 부위가 나병·백반·이질·천식·기관지염·치질·황달·근육 떨림 치료에 쓰여 왔다[6].

나무껍질을 먹은 기록도 있다[5]. 1899년 무렵 라지푸타나(지금의 라자스탄)에 큰 기근이 들었을 때 나무껍질을 먹을거리로 삼아 많은 사람이 살아났다고 전하며, 이 리뷰 원문에는 연도가 '1898-69'로 적혀 있다[5]. 덜 익은 꼬투리와 익은 꼬투리는 각각 채소와 과일로 먹으며, 말린 꼬투리는 상그리(sangri)라 하여 라자스탄 요리의 중심 재료다[3, 16]. 1974년 미국 임상영양학회지에는 이 나무를 '흔치 않은 콩과식물'로 소개하는 편지가 실렸다[29].

인도 라자스탄에서는 1730년 조드푸르 왕의 신하들이 케자를리 마을의 케즈리 나무를 베러 왔을 때 비슈노이 공동체가 이를 막다 많은 사람이 목숨을 잃은 일이 전한다(WebSearch 검색 요약으로만 확인)[26]. 케즈리는 라자스탄의 주 나무(state tree)이며, 2025년에는 태양광 발전 부지에서 이 나무가 베어지는 문제가 보도되었다(WebSearch 검색 요약으로만 확인)[27]. UAE는 2008년 Ghaf를 나라 나무로 정했다[15].""")

S["biology"] = ("식물학적 특징", """작거나 중간 크기의 늘푸른 나무로, 잎이 성기고 가는 가지에 원뿔 모양 가시가 있다[5]. 좁은 뜻의 Prosopis 속은 마디 사이 줄기에 흩어져 난 곧은 가시(prickle)가 특징이며, 턱잎이 변한 가시는 없다[2]. 나무껍질은 거칠고 얇은 조각으로 벗겨진다[5]. 잎은 두 번 깃꼴겹잎으로 대개 깃조각이 2쌍이고, 작은잎은 7–12쌍이다[5]. 꽃은 가는 이삭꽃차례에 달리는 작고 노르스름한 꽃이며, 꼬투리는 원통형으로 마디가 잘록하거나 납작하고 씨앗은 10–15개다[5].

뿌리는 30 m 넘게 내려가 지하수층에 닿는 긴 곧은뿌리를 내는 지하수 식물(phreatophyte)이다[3]. 가뭄과 염분에 강하고, 사막의 계절에 따라 45 °C를 넘는 더위와 10 °C 아래의 추위를 견디며, 물이 가장 부족한 덥고 건조한 철에 꽃이 피는 특이한 개화 습성을 가진다[3]. 대기 질소를 고정하고 쓸 수 있는 칼슘·인을 늘려 땅을 기름지게 한다[3].

사막에서 자란 다 큰 나무에서는 뿌리혹이 발견되지 않았지만, 사막 농장의 나무와 생장실의 어린 나무에서는 뿌리 근처 흙을 접종하자 뿌리혹이 생겼다[20]. 어린 나무의 뿌리혹 수와 무게는 물이 넉넉할수록 늘었다[20]. 인도 서북부(펀자브·라자스탄)의 건조지에 흔하고 근동의 가시덤불에도 많으며, 뿌리 움돋이로 퍼지기도 하고 염분 땅을 견딘다(좁은 뜻의 Prosopis 속 전체에 대한 서술)[2].""")

S["related_species"] = ("가까운 종", """2022년 997개 핵 유전자의 계통 분석에 따라 넓은 뜻의 Prosopis 속은 세 계통으로 나뉘는 다계통군으로 밝혀졌고, 좁은 뜻의 Prosopis 속은 3종으로 줄었다[2]. 남은 3종은 P. cineraria·P. farcta·P. koelziana이며, 인도·네팔의 1속 1종 속인 Indopiptadenia와 자매군을 이룬다[2]. 이 두 속은 줄기 마디 사이의 가시와 서·중앙아시아 분포를 공유한다[2].

Prosopis 속의 기준종(type)인 P. spicigera L.은 P. cineraria의 이명이다[2]. 그 밖의 이명으로 Mimosa cinerea L.(일부), Prosopis spicata Burm.f., Prosopis aculeata J.Koenig ex Roxb., Acacia cineraria (L.) Willd. 등이 정리되어 있다[2].

신대륙의 메스키트류는 Neltuma 속으로 옮겨져, 같은 식품원료 목록에 따로 오른 P. juliflora는 Neltuma juliflora, P. alba는 Neltuma alba가 되었다[2]. 이 두 종은 이 자료와 다른 소재이므로 성분·이용 정보를 섞지 않았다[2]. Ghaf나무와 메스키트 계통(Neltuma)은 약 2300만 년 전에 갈라진 것으로 추정되며, 두 유전체 사이의 동질 배열(synteny)은 약하다[3]. Ghaf나무의 먹는 꼬투리는 '덜 이용되는 사막 콩과식물'의 플라보노이드·이소플라보노이드 공급원으로 따로 연구되었다[19].""")

S["cultivation"] = ("재배와 생산", """Ghaf나무는 인도·파키스탄의 타르 사막과 아라비아반도 등 근동·인도아대륙의 건조지에 자라며, 아라비아반도에서는 가장 흔한 야생 콩과 나무다[3, 9]. 인도 사막의 농림복합(나무+작물) 경작지 비교에서 Ghaf나무 밭은 토양 동물·유기탄소·미생물 활성이 높아 가장 좋은 토양 생태계로 평가되었다[25]. 파키스탄 건조 평야에서는 Ghaf나무와 Salvadora oleoides가 함께 자라는 숲이 사람의 간섭으로 대부분 퇴화 단계에 있다고 보고되었다[30].

번식 연구로는 눈(bud) 조직배양으로 100일 동안 눈 하나에서 소식물체 3–5개를 얻는 방법이 보고되었다[21]. MS 배지에 IAA 3.0 mg/L와 키네틴 0.05 mg/L를 넣었을 때 다발 새싹이 가장 잘 나왔고, 뿌리 내린 식물의 60%가 화분으로 옮겨 살았다[21]. 접종으로 뿌리혹을 만들 수 있는 세균 균주를 섞어 넣었을 때 어린 나무의 뿌리혹 형성이 가장 좋았다[20].

UAE에서는 도시화·서식지 감소·낙타 과방목이 위협이며, 나라 단위 IUCN 평가는 '관심 필요(Least Concern)'이지만 아부다비에서는 지역적으로 멸종위기로 본다[4]. 인도 라자스탄에서는 태양광 발전 부지 조성으로 나무가 베어지는 일이 보도되었다(WebSearch 검색 요약으로만 확인)[27]. 국내 재배나 국내 생산 통계는 확인하지 못함.""")

S["processing"] = ("가공과 이용", """나무껍질은 줄기에서 벗겨 그늘에 말린 뒤 가루로 내어 용매로 우려 연구에 쓴다[7]. 파키스탄 연구에서는 4월에 거둔 생 껍질을 2주 그늘에 말려 갈고, 가루 1 kg을 70% 메탄올에 7일 담가 얻은 추출물의 수율이 약 3.85%였다[7]. 말린 줄기 껍질의 메탄올 추출물은 토끼 공장·기관·대동맥 조직에서 칼슘 통로 차단으로 보이는 이완 작용을 나타냈다(시험관)[7].

동물 연구로는 껍질 에탄올 추출물을 45일 먹인 당뇨 생쥐에서 혈당이 내려가고 간 글리코겐이 늘었으며, 껍질 메탄올 추출물을 7일 먹인 쥐에서 공간 기억이 좋아지고 뇌 아세틸콜린에스테라아제 활성이 낮아졌다[8, 9]. 껍질 물 추출물(400 mg/kg)은 쥐의 설사 빈도를 57.29% 줄였다[12]. 잎과 줄기 껍질의 수알코올 추출물은 생쥐 에를리히 복수암 모델에서 종양 세포에 독성을 보였다[13]. 이 결과들은 사람에서 확인된 효과가 아니다[8, 9, 12, 13].

화장품 쪽에서는 줄기·잎·껍질 추출물 가운데 껍질 추출물의 페놀·플라보노이드 함량과 항산화 활성이 두드러져, 껍질 추출물 2%를 넣은 에멀션이 사람 피부에서 시험되었다[14]. UAE에서는 잎·껍질·뿌리·잔가지를 섞은 추출물이 피부 노화 관련 효소를 억제했다(시험관)[15]. 크리켓 선수(군마다 10명)에게 케즈리 보충제 500 mg을 21일 먹인 소규모 연구가 있으나, 논문은 보충제의 원료 부위를 분명히 적지 않았고 말린 꼬투리(상그리)를 소개하고 있어 나무껍질 자료로 보기 어렵다[16]. 국내 건강기능식품 제품 생산실적은 확인하지 못함.""")

S["genetics"] = ("유전체와 육종", """UAE 알아인 사막의 야생 나무 한 그루(15–20년생)의 잎으로 유전체를 해독해, 거의 염색체 수준인 691,857,940 bp(GC 32.08%)의 조립본을 얻었다[3]. k-mer로 추정한 유전체 크기는 약 707 Mb이고, 가장 긴 14개 스캐폴드가 조립본의 약 86%를 차지하며 BUSCO 완전성은 99%였다[3]. 유전자 모델 77,579개 가운데 단백질을 만드는 55,325개(약 72%)에 기능이 주석되었고, 반복 서열이 58% 넘게 차지하며 대부분 LTR 레트로트랜스포존이다[3].

이 유전체에서는 테르페노이드 대사 유전자와 NBS-LRR 병 저항성 유전자가 늘어나 있었고, 410개 부모 유전자에서 생긴 레트로 유전자 785개가 확인되었다[3]. 그 가운데 초기 뿌리혹 유전자(Early nodulin 93)의 증폭은 질소가 적은 사막 토양에 대한 적응과 맞는다고 해석되었다[3]. 250 mM 염 처리에서 새싹은 2065개 유전자가 늘고 2108개가 줄었다[3].

UAE 전역 204그루의 전장 재서열 분석에서 LD 정리 후 SNP 57,183개로 4개 유전 집단이 나뉘었고, 북·북동부의 4번 집단은 다양성이 낮고 근친계수가 높았다[4]. 204그루 가운데 114그루만 유전적으로 고유했고 90그루는 클론 무리에 속했다[4]. 인도 타르 사막 10개 집단 49그루를 CBDP·SCoT 표지로 본 연구에서는 분자 변이의 77%가 집단 안, 23%가 집단 사이에 있었다[24]. 나무껍질 성분을 목표로 한 품종 육성은 확인하지 못함.""")

S["safety"] = ("안전성", """나무껍질 식품원료에 대한 식약처 등 국내 공공기관의 별도 주의 정보나 섭취 기준은 「식품원료 목록」의 사용 부위 조건 외에는 확인하지 못함[1]. 국외 공공기관(EFSA·NIH 등)의 Ghaf나무 껍질 안전성 평가도 이번 조사에서 확인하지 못함.

성분 쪽에서는 이 식물의 알칼로이드 혼합물을 개에 1 mg/kg 주자 혈압이 떨어지고 곧 죽었으며, 이를 받은 생쥐의 간·비장·신장·폐·심장에 넓은 손상이 보였다는 기록이 리뷰에 인용되어 있다[5]. 파키스탄 민간에서는 줄기 껍질이 유산을 일으키고 설사를 돕는 성질이 있다고 알려져 왔다[7]. 반대로 아유르베다 리뷰에는 가루를 설탕과 섞어 임신부에게 유산 예방용으로 준다는 기록이 있어 두 전승이 엇갈린다[5]. 임신부의 섭취 안전성은 확인하지 못함.

잎의 응축 탄닌은 0.01–0.02% 농도에서 반추위 섬유소 분해효소 활성을 65.9–78.99% 억제했다(시험관)[23]. 오만 양에게 말린 꼬투리를 사료의 45%로 먹이자 체중이 줄었고, 6주 뒤부터 성장에 나쁜 영향이 나타났다[22]. 이란 반다르아바스 주변에서 거둔 시료의 원소 분석에서는 줄기가 잎·가지보다 필수 원소가 많고 독성 원소가 적어, 조사한 독성 금속 기준을 충족했다[17]. 줄기 껍질 추출물은 사람 피부 세포(HaCaT)에 독성이나 세포자멸을 일으키지 않았다[14]. 이 종의 추출물이 파라콰트 독성을 줄인다는 2021년 생쥐 연구는 2023년에 철회되어 여기서 쓰지 않았다[28].""")

compounds = [
    dict(name="Lupeol", name_ko="루페올", **{"class": "트리테르페노이드"}, role="bioactive", part="줄기 껍질(클로로포름 분획)", content_text="분리 보고, 함량은 초록에 없음[11]", activity_ko="이 화합물들이 분리된 껍질 클로로포름 분획이 당뇨 쥐의 혈당을 낮추고 α-아밀라아제를 억제(IC50 40.29 µg/mL)함(분획 전체의 결과)[11]", source=[11]),
    dict(name="beta-Sitosterol", name_ko="β-시토스테롤", **{"class": "식물 스테롤"}, role="bioactive", part="줄기 껍질(클로로포름 분획); 식물 전반", content_text="분리 보고, 함량은 초록에 없음[11]; 시토스테롤 보고(부위 표기 없음)[5]", activity_ko="껍질 클로로포름 분획의 구성 성분으로 분리됨[11]", source=[5, 11]),
    dict(name="Stigmasterol", name_ko="스티그마스테롤", **{"class": "식물 스테롤"}, role="bioactive", part="줄기 껍질(클로로포름 분획)", content_text="분리 보고, 함량은 초록에 없음[11]", activity_ko="껍질 클로로포름 분획의 구성 성분으로 분리됨; 스티그마스테롤·캄페스테롤·시토스테롤 등 스테로이드가 이 식물에서 보고됨[6, 11]", source=[6, 11]),
    dict(name="Nonacosan-8-one", name_ko="노나코산-8-온", **{"class": "지방족 케톤"}, role="bioactive", part="줄기 껍질(클로로포름 분획)", content_text="껍질에서 새로 분리된 화합물로 보고, 함량은 초록에 없음[11]", activity_ko="활성은 분획 단위로만 보고됨[11]", source=[11]),
    dict(name="Methyl 5-tridecyloctadec-4-enoate", name_ko="메틸 5-트리데실옥타데크-4-에노에이트", **{"class": "지방산 에스터"}, role="bioactive", part="줄기 껍질(클로로포름 분획)", content_text="껍질에서 새로 분리된 화합물로 보고, 함량은 초록에 없음[11]", activity_ko="활성은 분획 단위로만 보고됨[11]", source=[11]),
    dict(name="Chlorogenic acid", name_ko="클로로겐산", **{"class": "페놀산(카페오일퀸산)"}, role="marker", part="나무껍질(에틸아세테이트 분획)", content_text="HPLC·GC-MS로 확인, 정량값은 초록에 없음[10]", activity_ko="껍질 에틸아세테이트 분획(100 mg/kg)이 염화알루미늄으로 유도한 알츠하이머 모델 쥐의 인지 기능과 항산화 방어를 회복시켰고, 클로로겐산은 그 활성 후보로 제시됨(도킹 포함)[10]", source=[10]),
    dict(name="Quercetin", name_ko="퀘르세틴", **{"class": "플라보놀"}, role="bioactive", part="나무껍질(에틸아세테이트 분획)", content_text="HPLC·GC-MS로 확인, 정량값은 초록에 없음[10]", activity_ko="아세틸콜린에스테라아제 억제·항산화 활성 후보 성분으로 제시됨[10]", source=[10]),
    dict(name="Kaempferol", name_ko="켐페롤", **{"class": "플라보놀"}, role="bioactive", part="나무껍질(에틸아세테이트 분획)", content_text="HPLC·GC-MS로 확인, 정량값은 초록에 없음[10]", activity_ko="아세틸콜린에스테라아제 억제·항산화 활성 후보 성분으로 제시됨[10]", source=[10]),
    dict(name="Spicigerine", name_ko="스피시게린", **{"class": "피페리딘 알칼로이드"}, role="bioactive", part="부위는 확인하지 못함", content_text="ω-(3-히드록시-2-메틸-6-피페리딜) 알칸산으로 보고된 새 알칼로이드, 함량은 확인하지 못함[5]; 프로소필린과 함께 이 식물의 알칼로이드로 정리됨[6]", activity_ko="이 식물의 알칼로이드 혼합물 1 mg/kg이 개의 혈압을 떨어뜨리고 곧 죽게 했다는 기록이 있음(혼합물 결과)[5]", source=[5, 6]),
    dict(name="Prosogerin A", name_ko="프로소게린 A", **{"class": "플라본"}, role="bioactive", part="꽃", content_text="6-메톡시-7-히드록시-3',4'-메틸렌디옥시플라본으로 꽃에서 보고, 함량은 확인하지 못함[5]", activity_ko="활성은 확인하지 못함; 이 속에서만 보고된 플라본 계열(prosogerin A–E)의 하나[5, 6]", source=[5, 6]),
    dict(name="Prosogerin B", name_ko="프로소게린 B", **{"class": "칼콘"}, role="bioactive", part="꽃", content_text="2',4'-디히드록시-5'-메톡시-3,4-메틸렌디옥시칼콘으로 꽃에서 보고, 함량은 확인하지 못함[5]", activity_ko="활성은 확인하지 못함[5]", source=[5]),
    dict(name="Patulitrin", name_ko="파툴리트린", **{"class": "플라보놀 배당체(파툴레틴 배당체)"}, role="bioactive", part="꽃; 씨앗", content_text="꽃에서 분리 보고, 씨앗에서도 갈산·파툴레틴·루테올린·루틴과 함께 보고, 함량은 확인하지 못함[5]", activity_ko="활성은 확인하지 못함[5]", source=[5]),
    dict(name="Gallic acid", name_ko="갈산", **{"class": "페놀산(탄닌 관련)"}, role="bioactive", part="씨앗", content_text="씨앗에서 프로소게린 E와 함께 보고, 함량은 확인하지 못함[5]; 탄닌류로 정리됨[6]", activity_ko="활성은 확인하지 못함[5, 6]", source=[5, 6]),
    dict(name="Vitexin", name_ko="비텍신", **{"class": "플라본 C-배당체"}, role="bioactive", part="잎; 꼬투리", content_text="잎 물 추출물에서 분리[18]; 꼬투리에서 LC-MS로 푸에라린·플로리진·다이드제인과 함께 검출[19]", activity_ko="잎에서 분리한 비텍신이 만성 골수성 백혈병 세포(K-562)에 세포독성(IC50 147 µg/mL, 시험관)[18]", source=[18, 19]),
]

assays = [
    dict(role="literature", compound="Chlorogenic acid", compound_ko="클로로겐산(켐페롤·퀘르세틴 동시 확인)", part="나무껍질 에틸아세테이트 분획(Pc-EA)",
         content="정량값은 초록에 없음(성분 확인만 보고)[10]", method="HPLC, GC-MS",
         conditions={k: "" for k in ["instrument", "column", "mobile_phase", "gradient", "flow", "temp", "detection", "injection", "sample_prep", "standard", "linearity", "lod", "loq", "recovery"]},
         rationale="이 종의 식품원료 사용 부위인 나무껍질 분획에서 HPLC·GC-MS로 확인되고 활성 후보로 제시된 성분이다[10]. 전문 확인 못함(PMC 전문 없음) — 칼럼·이동상·검출 조건과 함량은 비워 둠[10].",
         source=[10], url=PM.format("41421404"), source_kind="paper"),
    dict(role="literature", compound="Lupeol", compound_ko="루페올(β-시토스테롤·스티그마스테롤 등 5종 분리)", part="줄기 껍질 클로로포름 분획(CfPc)",
         content="분리·구조 확인만 보고, 함량은 초록에 없음[11]", method="분획·분리 후 구조 확인(세부 방법은 초록에 없음)",
         conditions={k: "" for k in ["instrument", "column", "mobile_phase", "gradient", "flow", "temp", "detection", "injection", "sample_prep", "standard", "linearity", "lod", "loq", "recovery"]},
         rationale="줄기 껍질 클로로포름 분획에서 새 화합물 2종(메틸 5-트리데실옥타데크-4-에노에이트, 노나코산-8-온)과 루페올·β-시토스테롤·스티그마스테롤이 분리되었고, 이 분획이 항당뇨 시험에 쓰였다[11]. 정량 분석이 아니며 전문 확인 못함 — 조건 칸은 비워 둠[11].",
         source=[11], url=PM.format("30372801"), source_kind="paper"),
]

d = dict(
    slug="prosopis-cineraria", name_ko="Ghaf나무", name_en="Ghaf tree (khejri)",
    scientific_name="Prosopis cineraria (L.) Druce",
    aliases=["Ghaf나무껍질", "Ghaf", "khejri", "jand", "jandi", "Shum", "shami", "Prosopis spicigera L."],
    sections=[dict(key=k, title=v[0], body=v[1]) for k, v in S.items()],
    compounds=compounds, markers=[], assays=assays, nutrients=[], production=[], world=[], gi=[], orgs=[],
    sources=[dict(n=n, title=t, url=u, publisher=p, accessed=a) for n, t, u, p, a in sources],
)
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in d["sections"]:
    print(s["key"], len(s["body"]))
