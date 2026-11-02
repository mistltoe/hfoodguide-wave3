import json
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "dossier.json"
A = "2026-11-02"


def pm(pmid, title, pmc=None):
    url = f"https://pmc.ncbi.nlm.nih.gov/articles/{pmc}/" if pmc else f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
    return {"title": title, "url": url, "publisher": "PubMed Central" if pmc else "PubMed", "accessed": A}


S = [
    {"title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 해홍나물(Suaeda maritima (L.) Dumort.) 2행과 같은 속 원료(나문재·칠면초·Suaeda spp.) 행",
     "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
    pm("32707417", "Wild vs cultivated halophytes: Nutritional and functional differences. Food Chem. 2020;333:127536 (초록만 확인)"),
    pm("38496978", "Phytochemical Screening, Molecular Docking, ADME Properties, and In Vitro Antioxidant, Anticancer, and Antidiabetic Activity of Marine Halophyte Suaeda maritima (L.) Dumort. ACS Omega. 2024;9(10):11200-11216", "PMC10938337"),
    pm("39189541", "Suaedamas A-D: Four New Compounds from the Aerial Parts of Suaeda maritima with Inhibition of NO Production Activity. Chem Biodivers. 2024;21(12):e202401787 (초록만 확인)"),
    pm("38878490", "Suaeda maritima polysaccharides attenuate LPS-induced inflammation of RAW264.7 cells and antioxidative activity. Int Immunopharmacol. 2024;137:112482 (초록만 확인)"),
    pm("24679058", "Three new flavonol glycosides from Suaeda maritima. J Asian Nat Prod Res. 2014;16(5):434-439 (초록만 확인)"),
    pm("17766398", "Low-affinity Na+ uptake in the halophyte Suaeda maritima. Plant Physiol. 2007;145(2):559-571", "PMC2048717"),
    pm("27682829", "Transcriptome Analysis of the Response to NaCl in Suaeda maritima Provides an Insight into Salt Tolerance Mechanisms in Halophytes. PLoS One. 2016;11(9):e0163485", "PMC5040429"),
    pm("30442441", "Metabolomic insights into the mechanisms underlying tolerance to salinity in different halophytes. Plant Physiol Biochem. 2019;135:528-545 (초록만 확인)"),
    pm("28110268", "Metabolic and physiological adjustment of Suaeda maritima to combined salinity and hypoxia. Ann Bot. 2017;119(6):965-976", "PMC5604547"),
    pm("22316572", "High phenotypic plasticity of Suaeda maritima observed under hypoxic conditions in relation to its physiological basis. Ann Bot. 2012;109(5):1027-1036", "PMC3310496"),
    pm("18369238", "Do conditions during dormancy influence germination of Suaeda maritima? Ann Bot. 2008;101(9):1319-1327", "PMC2710252"),
    pm("32688687", "Photosynthetic features of non-Kranz type C4 versus Kranz type C4 and C3 species in subfamily Suaedoideae (Chenopodiaceae). Funct Plant Biol. 2009;36(9):770-782 (초록만 확인)"),
    pm("21564891", "Microsatellite markers for the tetraploid halophyte Suaeda maritima (L.) Dumort. (Chenopodiaceae) and cross-species amplification in related taxa. Mol Ecol Resour. 2009;9(4):1247-1249 (초록만 확인)"),
    pm("19796358", "Genetic structure of coastal and inland populations of the annual halophyte Suaeda maritima (L.) Dumort. in Central Europe, inferred from AFLP markers. Plant Biol (Stuttg). 2009;11(6):812-820 (초록만 확인)"),
    pm("24148614", "Habitat fragmentation and recent bottlenecks influence genetic diversity and differentiation of the Central European halophyte Suaeda maritima (Chenopodiaceae). Am J Bot. 2013;100(11):2210-2218 (초록만 확인)"),
    pm("26267391", "Characterization of the superoxide dismutase genes of the halophyte Suaeda maritima in Japan and Egypt. Plant Cell Rep. 2015;34(12):2099-2110 (초록만 확인)"),
    pm("26839496", "Diversity and Plant Growth Promoting Capacity of Endophytic Fungi Associated with Halophytic Plants from the West Coast of Korea. Mycobiology. 2015;43(4):373-383", "PMC4731641"),
    pm("23687061", "Amorphus suaedae sp. nov., isolated from the root of a tidal flat plant, Suaeda maritima. Int J Syst Evol Microbiol. 2013;63(Pt 10):3868-3872 (초록만 확인)"),
    pm("22490817", "Effect of dietary supplementation with Suaeda maritima on blood physiology, innate immune response, and disease resistance in olive flounder against Miamiensis avidus. Exp Parasitol. 2012;131(2):195-203 (초록만 확인)"),
    pm("21702225", "Hepatoprotective and antioxidant properties of Suaeda maritima (L.) Dumort ethanolic extract on concanavalin-A induced hepatotoxicity in rats. Indian J Exp Biol. 2011;49(6):455-460 (초록만 확인)"),
    pm("37642695", "Feasibility Study on Phytoremediation of Potentially Toxic Elements (Cd, Ni and Pb) in Aquatic Environments Using Suaeda maritima Plant Species, a Case Study: Khorkhoran International Wetland, Persian Gulf. Bull Environ Contam Toxicol. 2023;111(3):32 (초록만 확인)"),
    pm("38823092", "Unravelling the halophyte Suaeda maritima as an efficient candidate for phytostabilization of cadmium and lead: Implications from physiological, ionomic, and metabolomic responses. Plant Physiol Biochem. 2024;212:108770 (초록만 확인)"),
    pm("36627045", "Regulation of chromium translocation to shoot and physiological, metabolomic, and ionomic adjustments confer chromium stress tolerance in the halophyte Suaeda maritima. Environ Pollut. 2023;320:121046 (초록만 확인)"),
    pm("34623537", "Purification and characterization of bioactive compounds extracted from Suaeda maritima leaf and its impact on pathogenicity of Pseudomonas aeruginosa in Catla catla fingerlings. AMB Express. 2021;11(1):135", "PMC8501176"),
    pm("21967697", "In vitro bioactivity and phytochemical screening of Suaeda maritima (Dumort): a mangrove associate from Bhitarkanika, India. Asian Pac J Trop Med. 2011;4(9):727-734 (초록만 확인)"),
    pm("39346424", "Root of Seablite (Suaeda maritima), the Medicinal Halophyte for Skincare Application. J Pharm Bioallied Sci. 2024;16(Suppl 3):S2709-S2711", "PMC11426560"),
    pm("41518651", "An undescribed biflavone from coastal halophyte Suaeda maritima subsp. salsa (L.) Soó. Nat Prod Res. 2026 (초록만 확인)"),
    pm("26714456", "Novel and conserved miRNAs in the halophyte Suaeda maritima identified by deep sequencing and computational predictions using the ESTs of two mangrove plants. BMC Plant Biol. 2015;15:301", "PMC4696257"),
    pm("18669016", "Antimicrobial activity of fatty acid methyl esters of some members of Chenopodiaceae. Z Naturforsch C. 2008;63(5-6):331-336 (초록만 확인)"),
    {"title": "Phylogenetic study of the Genus Suaeda (Chenopodiaceae) based on chloroplast and nuclear DNA sequences from Korea (WebSearch 검색 요약으로만 확인, 원문 미열람 — 사이트 접속 불가)",
     "url": "https://koreascience.kr/article/JAKO201810866006451.page", "publisher": "KoreaScience(한국과학기술정보연구원)", "accessed": A},
    {"title": "RAPD marker variations between and within the species of Korean Suaeda (WebSearch 검색 요약으로만 확인, 원문 미열람 — 사이트 접속 불가)",
     "url": "https://koreascience.or.kr/article/JAKO200430335053936.page", "publisher": "KoreaScience(한국과학기술정보연구원)", "accessed": A},
]
for i, s in enumerate(S, 1):
    s["n"] = i
S = [{"n": s["n"], "title": s["title"], "url": s["url"], "publisher": s["publisher"], "accessed": s["accessed"]} for s in S]

sections = [
    {"key": "overview", "title": "한눈에 보기", "body":
     "해홍나물은 명아주과(Chenopodiaceae) 나문재속(Suaeda)의 한해살이 염생식물로, 바닷물이 드나드는 염습지와 갯벌 가장자리에서 자란다[1, 10]. "
     "다육질의 가는 잎에 소금기를 많이 쌓는 식물이어서, 잎에 염화나트륨이 400 mM 안팎으로 쌓여도 상하지 않는다고 보고되었다[7]. "
     "세계적으로는 식물의 염 내성을 연구하는 모델 식물로 더 많이 연구되었고, 식품 성분을 정량한 연구는 많지 않다[8, 2].\n\n"
     "식품의약품안전처 「식품원료 목록」에서 해홍나물은 식품에 사용할 수 있는 원료(사용가능)이며, 사용 조건은 '사용가능부위 : 순, 잎'이다[1]. "
     "목록의 원료명은 해홍나물순·해홍나물잎 2개이고, 이명은 갯나문재·남은재나물, 영문명은 Sea blite·Sea goosefoot·Herbaceous seepweed로 적혀 있다[1]. "
     "같은 목록 자료에 다른 나라 목록이나 건강기능식품 고시형 원료의 원재료로 표시된 기록은 없다[1]. "
     "포르투갈·스페인 염습지 시료 연구는 해홍나물이 단백질·식이섬유·무기질의 좋은 공급원이고 카로티노이드와 비타민 A·C를 지니며, 비교한 세 염생식물 가운데 항산화 능력이 특히 좋았다고 보고했다[2]. "
     "다만 이 문서에 실은 생리활성 결과는 대부분 세포·동물 실험이며 사람에게서 확인된 효과는 아니다[3, 5, 21]."},
    {"key": "history", "title": "이름과 이용의 역사", "body":
     "학명 Suaeda maritima (L.) Dumort.의 괄호 속 저자 표기는 이 식물이 처음에 명아주속(Chenopodium maritimum L.)으로 기재되었다가 나문재속으로 옮겨졌음을 보여 주며, 식약처 목록에도 Chenopodium maritimum L.이 이명으로 함께 적혀 있다[1]. "
     "같은 목록에는 Suaeda maritima subsp. asiatica Hara, Chenopodina filiformis Moq., Suaeda australis Moq.도 이명으로 실려 있다[1].\n\n"
     "인도에서는 해홍나물을 일부 지역에서 식량·사료·전통 약재로 쓰는 맹그로브 주변 식물로 소개한다[3]. "
     "태국 만 연안에서는 뿌리 추출물을 피부 증상을 덜거나 다스리는 데 써 왔다는 전통 이용이 보고되었다[27]. "
     "한국에서 해홍나물을 나물로 먹어 온 전통 기록은 공공기관 자료로 확인하지 못함. "
     "2012년에는 한국 연구진이 해홍나물을 넙치 사료에 0.1%·1.0% 섞어 먹인 양식 연구가 발표되었고[20], 인도에서는 잎 추출물을 잉어류 양식의 세균 감염 치료에 시험한 연구가 있다[25]. "
     "식약처 목록에 '갯나문재', '남은재나물'이라는 이명이 남아 있어 국내에서도 지역 이름으로 불려 왔음을 짐작할 수 있다[1]."},
    {"key": "biology", "title": "식물학적 특징", "body":
     "해홍나물은 바닷물에 주기적으로 잠기는 조간대 습지에 자라며, 높은 염분과 침수로 생기는 토양의 산소 부족을 함께 견딘다[10]. "
     "반드시 염분이 있어야 잘 자라는 절대 염생식물로 분류되며[23], 수경 재배 실험에서는 염화나트륨 150 mM 부근이 생장에 최적에 가까웠다[7]. "
     "같은 염습지라도 높은 곳과 낮은 곳의 개체가 서로 다른 생김새를 보이는데, 맞바꿔 옮겨 심은 실험에서 옮긴 자리의 모양을 따라가 표현형 가소성이 큰 것으로 확인되었다[11].\n\n"
     "씨앗은 약 5개월의 겨울 휴면 뒤 봄에 2–3주 동안 한꺼번에 싹이 트며, 약 15 °C 이상의 온도가 필요하고 차가운 바닷물에 담겨 있던 씨앗이 더 잘 발아했다[12]. "
     "큰 씨앗이 작은 씨앗보다 일찍, 더 잘 싹텄다[12]. "
     "광합성은 C4가 아닌 C3형으로 분류된다[13]. "
     "염분이 높아지면 글리신베타인 같은 삼투 조절 물질을 쌓고 나트륨 이온을 액포에 격리하거나 밖으로 내보내는 방식으로 견딘다[8, 9]. "
     "산소가 부족해지면 뿌리에서 숙신산·말산·시트르산 같은 TCA 회로 중간산물과 유리 아미노산이 늘어났다[10]."},
    {"key": "related_species", "title": "가까운 종과 이름 혼동", "body":
     "식약처 「식품원료 목록」 원자료를 보면 '나문재'(나문재순·줄기·잎)는 Suaeda asparagoides / Suaeda glauca Bunge로, 이명 갯솔나무, 사용가능부위 순·줄기·잎이다[1]. "
     "'칠면초'(칠면초순)는 Suaeda japonica로, 사용가능부위가 순뿐이다[1]. "
     "해홍나물은 Suaeda maritima로 사용가능부위가 순·잎이어서 세 원료의 학명과 허용 부위가 서로 다르며, 해홍나물의 이명 '갯나문재'에 '나문재'가 들어 있으므로 이름만 보고 섞지 않도록 주의해야 한다[1]. "
     "목록에 따로 실린 S. californica·S. depressa 등 외국 나문재속 원료 자료도 섞지 않았다[1].\n\n"
     "식약처 목록은 Suaeda australis를 해홍나물의 이명으로 적지만, 전남 무안 염습지 연구는 S. maritima와 S. australis를 서로 다른 종으로 나누어 채집했다[1, 18]. "
     "일본산 S. maritima는 유전자(ITS) 계통에서 이집트·유럽·인도산과 다른 무리로 묶였다[17]. "
     "한국 나문재속의 분자 연구에서는 ITS로 칠면초·해홍나물·S. australis가 잘 구별되지 않았다는 결과와, 겉모습이 비슷한 종을 DNA 표지로 구별했다는 결과가 함께 보고된 것으로 검색 요약에서 확인했으나 원문은 열지 못했다[31, 32]. "
     "중국에서 약초로 쓰는 S. maritima subsp. salsa(흔히 S. salsa로 부름)는 별개의 분류군으로 보아 그 성분 자료는 이 문서에 넣지 않았다[28]."},
    {"key": "cultivation", "title": "자생지와 재배", "body":
     "국내에서는 서해안 전남 무안 염습지와 남해 남해도 갯벌에서 해홍나물이 자라는 것이 미생물 연구의 채집 기록으로 확인된다[18, 19]. "
     "해홍나물의 국내 재배 면적이나 생산량 통계는 확인하지 못함. "
     "포르투갈·스페인 연구에서 재배한 개체는 야생 개체보다 더 다육질이고 무기질이 많았으며 식이섬유는 적었다[2]. "
     "실험실에서는 수경 재배로 염분 농도와 산소 조건을 바꾸어 키우는 방식이 널리 쓰인다[7, 10].\n\n"
     "씨앗은 겨울 동안 차갑고 짠 물에 담겨 있다가 기온이 오르고 염분이 낮아질 때 싹트므로, 마른 상태로 보관한 씨앗은 발아가 떨어질 수 있다[12]. "
     "짧은 동결 처리는 마른 상태로 보관한 씨앗의 초기 발아를 앞당겼다[12]. "
     "중부 유럽에서는 바닷가뿐 아니라 내륙의 칼리 광산 폐석 더미 주변에 생긴 인공 염지로 여러 차례 독립적으로 퍼져 나갔다[15]. "
     "반면 내륙과 발트해 연안 집단은 고립과 병목 현상으로 유전 다양성이 줄어 있었다[16]. "
     "중금속이 많은 퇴적물에서도 자라므로 오염 지역 정화용 식물로 연구되는데, 이는 먹을거리로 채취할 때 채취 장소를 가려야 하는 이유이기도 하다[22, 23]."},
    {"key": "processing", "title": "가공과 이용", "body":
     "식약처 목록에서 식품 원료로 쓸 수 있는 부위는 순과 잎이며, 뿌리와 씨앗은 해홍나물의 허용 부위에 없다[1]. "
     "식약처 「식품 등의 생산실적」 자료에서 해홍나물 품목의 생산실적은 확인하지 못함. "
     "인도 연구에서는 말린 전초 30 g을 헥산·아세톤·메탄올로 차례로 속슬렛 추출했으며, 메탄올 추출물의 수율이 7.3%로 가장 높았다[3].\n\n"
     "다당류 연구에서는 조다당을 정제해 얻은 분획(SMP-F1)이 포도당 45.4%, 아라비노스 20.5%, 만노스 14.2%, 갈락토스 12.7%로 이루어져 있었고, 이를 가수분해한 저분자 분획이 대식세포의 염증 물질을 더 잘 줄였다(세포 실험)[5]. "
     "한국 연구진의 넙치 양식 연구에서는 해홍나물을 사료에 0.1%·1.0% 넣었을 때 혈액 지표와 선천 면역 반응이 좋아지고 기생충 감염 후 누적 폐사율이 낮아졌다[20]. "
     "인도 연구에서는 잎 에탄올 추출물과 정제 분획을 녹농균에 감염된 잉어류 치어에 썼을 때 생존율이 100%였다고 보고했다[25]. "
     "같은 과의 염생식물 4종을 비교한 연구에서는 해홍나물의 지방산 메틸에스터 추출물이 세균에 강한 억제 효과를 보였다[30]. "
     "인도 동부 해안 시료의 잎·줄기 추출물은 시험관에서 항산화 활성과 함께 일부 병원성 세균에 최소억제농도 2.5–5.0 mg/mL의 항균 활성을 보였다[26]. "
     "이런 결과는 양식·시험관 수준이며 사람 식품으로서의 가공법은 확인하지 못함."},
    {"key": "genetics", "title": "유전체와 유전 연구", "body":
     "해홍나물은 4배체 식물로, 12개의 다형성 마이크로새틀라이트 표지가 개발되었고 유전자좌마다 2–15개의 대립유전자가 관찰되었다[14]. "
     "이 표지는 S. salsa에서도 모두 증폭되어 가까운 종 연구에 함께 쓰인다[14]. "
     "중부 유럽 40개 집단 120개체를 AFLP 243개 띠로 분석한 결과 유전 변이 대부분이 집단 안에 있었다[15]. "
     "31개 집단을 10개 마이크로새틀라이트로 비교한 연구에서는 해안 집단과 내륙 집단이 뚜렷이 나뉘었다[16].\n\n"
     "염 처리 전사체 분석에서는 72,588개의 전사체가 모였고, 염 처리로 647개 유전자가 2배 이상 늘고 735개가 줄었다[8]. "
     "작은 RNA 분석에서는 25개 miRNA 패밀리에 속하는 134개의 보존 miRNA와 13개의 새 miRNA가 예측되었으며, 그중 일부는 바닷물 영향을 받는 식물에서만 발현되었다[29]. "
     "일본산과 이집트산 계통은 ITS 계통에서 갈리지만 SOD 동위효소 유전자의 발현 양상은 비슷했다[17]. "
     "전체 유전체 해독 결과는 이번 조사에서 확인하지 못함. "
     "육종된 품종이나 재배 계통은 확인하지 못함."},
    {"key": "safety", "title": "안전성", "body":
     "식약처는 해홍나물을 사용가능 원료로 두고 순과 잎만 쓰도록 정해 두었으며, 따로 정한 섭취량 제한이나 주의 문구는 목록 자료에 없다[1]. "
     "건강기능식품 고시형 원료가 아니므로 공식 섭취 시 주의사항은 없다[1]. "
     "알레르기·잔류 농약 등 공공기관의 안전 정보는 확인하지 못함.\n\n"
     "해홍나물은 잎에 염화나트륨을 400 mM 안팎까지 쌓는 식물이어서 소금기가 많으므로, 나트륨 섭취를 줄여야 하는 사람은 양을 조절하는 것이 좋다[7]. "
     "생잎 또는 건조물의 나트륨 함량 수치와 옥살산 함량은 이 종 자료로 확인하지 못함. "
     "페르시아만 습지 시료에서 잎의 평균 함량은 카드뮴 0.157, 니켈 3.34, 납 2.23 mg/kg이었다[22]. "
     "크롬 처리 실험에서는 생물농축계수와 지상부 이동계수가 모두 1을 넘어 크롬을 지상부에 많이 쌓는 성질을 보였다[24]. "
     "반면 카드뮴·납은 이동계수가 1보다 작아 주로 뿌리에 머물렀다[23]. "
     "따라서 오염된 해안이나 산업 지역에서 채취한 해홍나물은 먹지 않는 것이 안전하다[22, 24]. "
     "쥐에게 에탄올 추출물을 준 실험에서 반수치사량(LD50)은 체중 kg당 3 g으로 계산되었다[21]."},
]

compounds = [
    {"name": "Sodium chloride", "name_ko": "염화나트륨(나트륨)", "class": "무기염", "role": "nutrient", "part": "잎",
     "content_text": "잎에 약 400 mM NaCl 축적(수경 재배 식물)[7]; 식품 기준(생물·건물 100 g당) 함량은 확인하지 못함",
     "activity_ko": "짠맛의 원천이자 삼투 조절 물질; 크롬 처리 시 나트륨 흡수가 늘어 수분 유지에 관여[7, 24]", "source": [7, 24]},
    {"name": "Glycine betaine", "name_ko": "글리신베타인", "class": "4차 암모늄 화합물(삼투 조절 물질)", "role": "bioactive", "part": "지상부",
     "content_text": "함량 수치 확인하지 못함; 염분·저산소 조건에서 증가[10]",
     "activity_ko": "세포 안 삼투압 조절로 염 내성에 관여[8, 9, 10]", "source": [8, 9, 10]},
    {"name": "Proline", "name_ko": "프롤린", "class": "아미노산(삼투 조절 물질)", "role": "bioactive", "part": "지상부·뿌리",
     "content_text": "함량 수치 확인하지 못함; 저산소·고염과 크롬 처리에서 증가[10, 24]",
     "activity_ko": "삼투 균형 유지와 활성산소 소거에 관여하는 것으로 해석됨[24]", "source": [10, 24]},
    {"name": "Quercetin", "name_ko": "퀘르세틴(및 새 배당체)", "class": "플라보놀", "role": "bioactive", "part": "부위 미기재(70% 메탄올 추출물)",
     "content_text": "분리 보고, 함량 수치 확인하지 못함; 퀘르세틴 3-O-람노실갈락토사이드-7-O-소포로사이드형 새 배당체도 분리[6]",
     "activity_ko": "추출물과 분리 화합물이 MCF7·HCT116·HepG2 암세포에 세포독성(세포 실험)[6]", "source": [6]},
    {"name": "Kaempferol", "name_ko": "캠페롤(및 새 배당체 2종)", "class": "플라보놀", "role": "bioactive", "part": "부위 미기재(70% 메탄올 추출물)",
     "content_text": "분리 보고, 함량 수치 확인하지 못함; 페룰로일화 배당체 포함 새 캠페롤 배당체 2종 분리[6]",
     "activity_ko": "암세포주 세포독성(세포 실험)[6]", "source": [6]},
    {"name": "Methyl trans-ferulate", "name_ko": "메틸 트랜스-페룰레이트", "class": "하이드록시신남산 에스터", "role": "bioactive", "part": "부위 미기재(70% 메탄올 추출물)",
     "content_text": "분리 보고(cis·trans 이성질체), 함량 수치 확인하지 못함[6]",
     "activity_ko": "암세포주 세포독성 평가 대상(세포 실험)[6]", "source": [6]},
    {"name": "Ferulic acid", "name_ko": "페룰산", "class": "하이드록시신남산", "role": "bioactive", "part": "지상부(야생·재배)",
     "content_text": "크로마토그래피 분석에서 가장 중요한 페놀 성분으로 보고, 수치는 초록에 없어 확인하지 못함[2]",
     "activity_ko": "항산화 능력의 주요 기여 성분으로 제시됨(시험관)[2]", "source": [2]},
    {"name": "Caffeic acid", "name_ko": "카페산", "class": "하이드록시신남산", "role": "bioactive", "part": "지상부(야생·재배)",
     "content_text": "페룰산과 함께 주요 페놀 성분으로 보고, 수치 확인하지 못함[2]",
     "activity_ko": "항산화 능력의 주요 기여 성분으로 제시됨(시험관)[2]", "source": [2]},
    {"name": "Stigmasterol", "name_ko": "스티그마스테롤", "class": "식물 스테롤", "role": "bioactive", "part": "전초(그늘 건조) 아세톤 추출물",
     "content_text": "GC-MS 주요 피크(머무름 시간 16.21분); HPLC에서는 미량(trace)으로만 확인, 정량값 없음[3]",
     "activity_ko": "분자 도킹·ADME 예측에서 약물 유사성이 좋게 나옴(컴퓨터 예측)[3]", "source": [3]},
    {"name": "gamma-Sitosterol", "name_ko": "γ-시토스테롤", "class": "식물 스테롤", "role": "bioactive", "part": "전초 아세톤 추출물",
     "content_text": "GC-MS 주요 피크(머무름 시간 17.09분), 정량값 없음[3]",
     "activity_ko": "분자 도킹 대상 성분(컴퓨터 예측)[3]", "source": [3]},
    {"name": "alpha-Tocopherol", "name_ko": "비타민 E(토코페롤)", "class": "지용성 비타민", "role": "nutrient", "part": "전초 아세톤 추출물",
     "content_text": "GC-MS로 검출(머무름 시간 14.123분), 정량값 없음[3]; 야생·재배 시료가 비타민의 좋은 공급원이라는 보고[2]",
     "activity_ko": "항산화 비타민; ADME 예측에서 약물 유사성이 좋게 나옴(컴퓨터 예측)[3]", "source": [2, 3]},
    {"name": "Polysaccharide", "name_ko": "해홍나물 다당류(SMP-F1)", "class": "다당류(글루칸·만난·아라비난 골격)", "role": "bioactive", "part": "부위 미기재",
     "content_text": "정제 분획 SMP-F1 단당 조성 포도당 45.4%·아라비노스 20.5%·만노스 14.2%·갈락토스 12.7%[5]",
     "activity_ko": "가수분해 분획 SMP-H3가 RAW264.7 대식세포의 NO·iNOS·COX-2·TNF-α·IL-1β·IL-6를 줄이고 IL-10을 늘림(세포 실험)[5]", "source": [5]},
    {"name": "Suaedama A", "name_ko": "수아에다마 A–D(신규 화합물)", "class": "신규 천연물(구조 계열은 초록에 없음)", "role": "bioactive", "part": "지상부",
     "content_text": "신규 4종과 기지 화합물 7종 분리, 함량 수치 확인하지 못함[4]",
     "activity_ko": "화합물 1–6이 LPS 자극 RAW264.7 세포의 NO 생성을 IC50 29.3–85.5 μM로 억제(양성 대조 덱사메타손 13.4 μM, 세포 실험)[4]", "source": [4]},
    {"name": "Cadmium", "name_ko": "카드뮴(오염 원소)", "class": "중금속(유해 원소)", "role": "nutrient", "part": "잎·뿌리",
     "content_text": "페르시아만 습지 시료 잎 평균 0.157 mg/kg, 뿌리 0.160 mg/kg(건물·생물 기준은 초록에 없음)[22]",
     "activity_ko": "유해 원소로 섭취 대상 성분이 아님; 채취지 오염도에 따라 달라짐[22, 23]", "source": [22, 23]},
]

assays = [
    {"role": "literature", "compound": "Stigmasterol", "compound_ko": "스티그마스테롤(β-시토스테롤 표준품 대조)",
     "part": "전초(인도 타밀나두 채취, 그늘 건조) 아세톤 추출물",
     "content": "미량(trace) 검출, 정량값 없음; 머무름 시간 0.684·1.052·1.405·3.830·9.736분에 스테롤 유도체 피크[3]",
     "method": "RP-HPLC-UV",
     "conditions": {"instrument": "", "column": "", "mobile_phase": "메탄올 75% / HPLC 등급 물 25%",
                    "gradient": "", "flow": "", "temp": "", "detection": "256 nm", "injection": "25 µL(추출물 20 ppm)",
                    "sample_prep": "건조 분말 30 g을 헥산→아세톤→메탄올 순서로 속슬렛 추출, 회전 감압 농축 후 건조",
                    "standard": "β-시토스테롤", "linearity": "", "lod": "", "loq": "", "recovery": ""},
     "rationale": "이 종에서 크로마토그래피 조건이 공개된 거의 유일한 성분 분석으로, GC-MS에서 주요 피크였던 스티그마스테롤의 존재를 확인하는 정성 분석이다[3]. 칼럼·유속·온도·검출한계·회수율은 본문에 없어 비워 두었고, 정량 시험법으로 쓰기에는 부족하다.",
     "source": [3], "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10938337/", "source_kind": "paper"},
    {"role": "literature", "compound": "Cadmium, Nickel, Lead", "compound_ko": "카드뮴·니켈·납(유해 원소)",
     "part": "잎·뿌리(이란 페르시아만 코르코란 습지 20개 지점)",
     "content": "잎 평균 카드뮴 0.157, 니켈 3.34, 납 2.23 mg/kg; 뿌리 0.160, 2.72, 1.22 mg/kg(기준 미기재)[22]",
     "method": "ICP-OES",
     "conditions": {"instrument": "", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "",
                    "injection": "", "sample_prep": "", "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""},
     "rationale": "먹는 부위인 잎의 중금속 함량을 이 종에서 직접 잰 자료로, 채취지 오염을 가늠하는 안전 지표다[22]. 전문 확인 못함 — 분석 조건 칸은 비워 둠.",
     "source": [22], "url": "https://pubmed.ncbi.nlm.nih.gov/37642695/", "source_kind": "paper"},
    {"role": "literature", "compound": "Ferulic acid", "compound_ko": "페룰산·카페산(페놀 성분 프로필)",
     "part": "지상부(포르투갈·스페인 염습지 야생 개체와 재배 개체)",
     "content": "페룰산과 카페산이 가장 중요한 페놀 성분으로 보고됨, 수치는 초록에 없음[2]",
     "method": "크로마토그래피 페놀 프로필(세부 기법은 초록에 없음)",
     "conditions": {"instrument": "", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "",
                    "injection": "", "sample_prep": "", "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""},
     "rationale": "먹는 부위의 주요 페놀산으로 항산화 능력과 연결되어 품질 지표 후보가 된다[2]. 전문 확인 못함 — 분석 조건 칸은 비워 둠.",
     "source": [2], "url": "https://pubmed.ncbi.nlm.nih.gov/32707417/", "source_kind": "paper"},
]

d = {
    "slug": "suaeda-maritima",
    "name_ko": "해홍나물",
    "name_en": "Sea blite (Herbaceous seepweed)",
    "scientific_name": "Suaeda maritima (L.) Dumort.",
    "aliases": ["해홍나물순", "해홍나물잎", "갯나문재", "남은재나물", "Sea blite", "Sea goosefoot", "Herbaceous seepweed",
                "Chenopodium maritimum L.", "Suaeda maritima subsp. asiatica Hara", "Chenopodina filiformis Moq.", "Suaeda australis Moq. (식약처 목록상 이명)"],
    "sections": sections,
    "compounds": compounds,
    "markers": [],
    "assays": assays,
    "nutrients": [],
    "production": [],
    "world": [],
    "gi": [],
    "orgs": [],
    "sources": S,
}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in sections:
    print(s["key"], len(s["body"]))
