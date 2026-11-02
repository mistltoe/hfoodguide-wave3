import json
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "dossier.json"
ACC = "2026-11-02"

def pm(pmid):
    return f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"

def pmc(p):
    return f"https://pmc.ncbi.nlm.nih.gov/articles/{p}/"

S = [
    ("식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 꽈배기모자반(Sargassum siliquastrum) 1행(2026-10-13 받은 원자료)", "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "식품의약품안전처", "2026-10-13"),
    ("Jang KH et al. Chromenes from the brown alga Sargassum siliquastrum. J Nat Prod 2005;68(5):716-23 (초록)", pm(15921416), "PubMed", ACC),
    ("Jung M et al. Meroditerpenoids from the brown alga Sargassum siliquastrum. J Nat Prod 2008;71(10):1714-9 (초록)", pm(18817444), "PubMed", ACC),
    ("Chung SC et al. Sargachromanols as inhibitors of Na+/K+ ATPase and isocitrate lyase. Bioorg Med Chem Lett 2011;21(7):1958-61 (초록)", pm(21377877), "PubMed", ACC),
    ("Lee JI, Seo Y. Chromanols from Sargassum siliquastrum and their antioxidant activity in HT 1080 cells. Chem Pharm Bull 2011;59(6):757-61 (초록)", pm(21628914), "PubMed", ACC),
    ("Cho SH et al. The antioxidant properties of brown seaweed (Sargassum siliquastrum) extracts. J Med Food 2007;10(3):479-85 (초록)", pm(17887942), "PubMed", ACC),
    ("Cho SH et al. Antioxidant activity of mojabanchromanol, a novel chromene, isolated from brown alga Sargassum siliquastrum. J Environ Biol 2008;29(4):479-84 (초록)", pm(19195385), "PubMed", ACC),
    ("Lim SN et al. Evaluation of antioxidative activity of extracts from a brown seaweed, Sargassum siliquastrum. J Agric Food Chem 2002;50(13):3862-6 (초록)", pm(12059172), "PubMed", ACC),
    ("Wong CK et al. Protective effects of seaweeds against liver injury caused by carbon tetrachloride in rats. Chemosphere 2000;41(1-2):173-6 (초록)", pm(10819197), "PubMed", ACC),
    ("Park BG et al. Vasodilatation effect of farnesylacetones, active constituents of Sargassum siliquastrum, on the basilar and carotid arteries of rabbits. Bioorg Med Chem Lett 2008;18(24):6324-6 (초록)", pm(19006667), "PubMed", ACC),
    ("Shin WS et al. 5E- and 5Z-farnesylacetones from Sargassum siliquastrum as novel selective L-type calcium channel blockers. Vascul Pharmacol 2013;58(4):299-306 (초록)", pm(23416245), "PubMed", ACC),
    ("A novel antihypertension agent, sargachromenol D from marine brown algae, Sargassum siliquastrum, exerts dual action as an L-type Ca2+ channel blocker and endothelin A/B2 receptor antagonist. Bioorg Med Chem 2017 (초록)", pm(28720331), "PubMed", ACC),
    ("Heo SJ, Jeon YJ. Protective effect of fucoxanthin isolated from Sargassum siliquastrum on UV-B induced cell damage. J Photochem Photobiol B 2009;95(2):101-7 (초록)", pm(19264501), "PubMed", ACC),
    ("Heo SJ et al. Anti-inflammatory effect of fucoxanthin derivatives isolated from Sargassum siliquastrum in lipopolysaccharide-stimulated RAW 264.7 macrophage. Food Chem Toxicol 2012;50(9):3336-42 (초록)", pm(22735499), "PubMed", ACC),
    ("Heo SJ et al. Chromene induces apoptosis via caspase-3 activation in human leukemia HL-60 cells. Food Chem Toxicol 2011;49(9):1998-2004 (초록)", pm(21600262), "PubMed", ACC),
    ("Yoon WJ et al. Anti-inflammatory effect of sargachromanol G isolated from Sargassum siliquastrum in RAW 264.7 cells. Arch Pharm Res 2012;35(8):1421-30 (초록)", pm(22941485), "PubMed", ACC),
    ("Yoon WJ et al. Sargachromanol G inhibits osteoclastogenesis by suppressing the activation NF-κB and MAPKs in RANKL-induced RAW 264.7 cells. Biochem Biophys Res Commun 2013;434(4):892-7 (초록)", pm(23611776), "PubMed", ACC),
    ("Kang GJ et al. Sargaquinoic acid isolated from Sargassum siliquastrum inhibits lipopolysaccharide-induced nitric oxide production in macrophages. Immunopharmacol Immunotoxicol 2013;35(1):80-7 (초록)", pm(22758221), "PubMed", ACC),
    ("Lee et al. Cytotoxicity of meroterpenoids from Sargassum siliquastrum against human cancer cells. Nat Prod Commun 2013;8(4):431-2 (초록)", pm(23738443), "PubMed", ACC),
    ("Potent inhibition of acetylcholinesterase by sargachromanol I from Sargassum siliquastrum and by selected natural compounds. Bioorg Chem 2019 (초록)", pm(31200287), "PubMed", ACC),
    ("Seven undescribed meroterpenoids from Sargassum siliquastrum and their inhibitory activity against amyloid β aggregation. J Nat Med 2024 (초록)", pm(39404981), "PubMed", ACC),
    ("Four undescribed chromane-type meroterpenoids from Sargassum siliquastrum and their inhibitory activity against amyloid-β42 aggregation. Chem Biodivers 2026 (초록; PMC 전문은 본문 없음)", pmc("PMC13412067"), "Chemistry & Biodiversity (PMC)", ACC),
    ("Qi et al. Anti-neuroinflammatory meroterpenoids from a Chinese collection of the brown alga Sargassum siliquastrum. J Nat Prod 2023;86(5):1284-1293 (초록)", pm(37137291), "PubMed", ACC),
    ("Fernando et al. Step gradient alcohol precipitation for the purification of low molecular weight fucoidan from Sargassum siliquastrum and its UVB protective effects. Int J Biol Macromol 2020;163:26-35 (초록)", pm(32599241), "PubMed", ACC),
    ("The anti-inflammatory effect of low molecular weight fucoidan from Sargassum siliquastrum in lipopolysaccharide-stimulated RAW 264.7 macrophages via inhibiting NF-κB/MAPK signaling pathways. Mar Drugs 2023;21(6):347", pmc("PMC10303138"), "Marine Drugs (PMC)", ACC),
    ("Sun et al. Gastroprotective effect of fucoidan from Sargassum siliquastrum against ethanol-induced gastric mucosal injury. Food Res Int 201:115566 (초록)", pm(39849715), "PubMed", ACC),
    ("Antiviral potential of fucoxanthin, an edible carotenoid purified from Sargassum siliquastrum, against Zika virus. Mar Drugs 2024;22(6):247", pmc("PMC11204710"), "Marine Drugs (PMC)", ACC),
    ("Ethanol extract of Sargassum siliquastrum inhibits lipopolysaccharide-induced nitric oxide generation by downregulating the NF-κB signaling pathway. Evid Based Complement Alternat Med 2022:6160010", pmc("PMC9205721"), "Evidence-Based Complementary and Alternative Medicine (PMC)", ACC),
    ("The effect of Sargassum siliquastrum supplementation on growth performance, cecal fermentation, intestine histomorphology, and immune response of Japanese quails. Animals 2022;12(4):432", pmc("PMC8868545"), "Animals (PMC)", ACC),
    ("Complete organellar genomes of six Sargassum species and development of species-specific markers. Sci Rep 2022", pmc("PMC9722929"), "Scientific Reports (PMC)", ACC),
    ("Li et al. The complete mitochondrial genome of Sargassum siliquastrum (Phaeophyceae) and its phylogenetic analysis. Mitochondrial DNA B Resour 2020;5(3):3583-3584", pmc("PMC7594832"), "Mitochondrial DNA Part B (PMC)", ACC),
    ("Nakajima et al. Defense mechanisms of sargassacean species against the epiphytic red alga Neosiphonia harveyi. J Phycol 2015;51(4):695-705 (초록)", pm(26986791), "PubMed", ACC),
    ("Chung HY et al. Seasonal variations of bromophenols in brown algae (Padina arborescens, Sargassum siliquastrum, and Lobophora variegata) collected in Hong Kong. J Agric Food Chem 2003;51(9):2619-24 (초록)", pm(12696947), "PubMed", ACC),
    ("Ma WC et al. Enhancement of bromophenol levels in aquacultured silver seabream (Sparus sarba). J Agric Food Chem 2005;53(6):2133-9 (초록)", pm(15769146), "PubMed", ACC),
    ("Gong YF et al. Suppression of radioactive strontium absorption by sodium alginate in animals and human subjects. Biomed Environ Sci 1991;4(3):273-82 (초록)", pm(1764217), "PubMed", ACC),
    ("Liu et al. Bioaccumulation and trophic transfer of phthalate esters in mangrove food web. Mar Pollut Bull 2025;222(Pt 1):118644 (초록)", pm(40884859), "PubMed", ACC),
    ("Preparative isolation of sargachromanol E from Sargassum siliquastrum by centrifugal partition chromatography and its anti-inflammatory activity. Food Chem Toxicol 2013 (초록)", pm(23973192), "PubMed", ACC),
    ("Heo SJ et al. Chromene suppresses the activation of inflammatory mediators in lipopolysaccharide-stimulated RAW 264.7 cells. Food Chem Toxicol 2014;67:169-75 (초록)", pm(24593990), "PubMed", ACC),
    ("Sustainable synthesis of magnetic Sargassum siliquastrum activated carbon loaded with NiS nanorods for adsorption of 2,4-D herbicide. Environ Sci Pollut Res Int 2024", pmc("PMC10881655"), "Environmental Science and Pollution Research (PMC, 초록 확인)", ACC),
]
sources = [{"n": i + 1, "title": t, "url": u, "publisher": p, "accessed": a} for i, (t, u, p, a) in enumerate(S)]

sections = [
 {"key": "overview", "title": "한눈에 보기", "body":
  "꽈배기모자반(Sargassum siliquastrum)은 모자반속에 속하는 갈조류로, 한국 연구에서는 한국 고유의 모자반과(Sargassaceae) 갈조류로 소개된다[28]. 한 논문은 한국에서 널리 먹는 식용 갈조류이자 기능성 식품 소재로 소개했고[28], 다른 논문은 한국에서 일본에 이르는 황해 연안에 널리 자라는 식용 갈조류로 적었다[25].\n\n"
  "식품원료로서의 지위: 식품의약품안전처 「식품원료 목록」에는 '꽈배기모자반' 1행이 식품원료(A코드)로 올라 있고, 상태는 '사용가능', 사용 조건은 '사용가능부위 : 전체'다[1]. 같은 목록에는 이 종의 이명이나 영문명이 적혀 있지 않다[1].\n\n"
  "성분 연구는 사가크로마놀(sargachromanol) 같은 크로멘·크로만계 메로테르페노이드에 가장 많이 모여 있으며, 제주 시료에서 16종이 새로 분리되었다[2]. 이들 사가크로마놀 일부는 Na+/K+ ATPase를 억제했고(효소 실험)[4], 이 종의 크로마놀 6종은 사람 섬유육종 세포에서 활성산소와 지질 과산화를 줄였다(세포 실험)[5]. 그 밖에 푸코잔틴[13], 저분자 푸코이단[24], 파네실아세톤[10] 연구가 있다. 보고된 효과는 대부분 세포·동물 실험 결과이며, 사람을 대상으로 한 꽈배기모자반 섭취 연구는 확인하지 못함."},
 {"key": "history", "title": "이용 역사", "body":
  "꽈배기모자반을 전통 식품이나 약재로 쓴 기록은 공공기관 자료로 확인하지 못함. 연구 이용은 1990년대부터 보고된다[35]. 1991년 중국 연구는 모자반류와 다시마류에서 만든 알긴산나트륨 23가지를 비교해 꽈배기모자반 알긴산나트륨이 방사성 스트론튬 흡수를 줄이는 데 효과가 컸다고 보고했고, 빵에 6% 넣는 방식을 제안했다[35].\n\n"
  "2000년대 초에는 홍콩 연구진이 이 종의 간 보호 효과(쥐)와 항산화 활성을 조사했다[8][9]. 같은 시기 홍콩 해조에서 바다 향미 성분인 브로모페놀의 계절 변화도 측정되었다[33]. 한국에서는 2005년 제주 시료에서 사가크로마놀 A–P가 보고된 뒤[2], 동해안 시료의 파네실아세톤 혈관 확장 연구[10], 제주 시료의 사가크로마놀 G 항염 연구[16] 등이 이어졌다.\n\n"
  "최근에는 저분자 푸코이단[24][25], 위 점막 보호 푸코이단(중국)[26], 일본 노토반도 시료의 아밀로이드 β 응집 억제 메로테르페노이드[21] 연구가 나왔다. 사료 이용 연구로는 메추라기 사료 첨가 실험(이집트 홍해 시료)[29]과 양식 감성돔류 사료 실험(홍콩)[34]이 있다."},
 {"key": "biology", "title": "생물학적 특징·생태", "body":
  "꽈배기모자반 시료는 한국 제주[2][25][27], 동해안[10], 경남 통영[28], 일본 노토반도[21], 홍콩[9][33], 중국 해역[23], 이집트 홍해 후르가다 부근[29]에서 채집되었다. 중국 하이난섬 맹그로브 연구에서는 꽈배기모자반이 부유 유기물·퇴적 유기물과 함께 맹그로브 먹이그물을 받치는 주요 기초 탄소원으로 분석되었다[36].\n\n"
  "모자반과 5종의 착생 조류를 비교한 연구에서 홍조류 Neosiphonia harveyi는 조사한 모든 지점에서 꽈배기모자반 위에 눈에 띄게 적었다[32]. 이 홍조의 포자는 꽈배기모자반 엽체에도 붙어 싹텄지만, 꽈배기모자반에서는 어린 착생체 주변 조직이 부풀고 허물어져 착생체와 함께 떨어져 나갔다[32]. 녹인 플로로탄닌의 착생 억제 효과는 가장 높은 농도(0.1 g/L 초과)에서만 나타났고 5종 사이에 차이가 없었다[32].\n\n"
  "홍콩 해역의 갈조 3종(꽈배기모자반 포함) 조사에서 건조중량 기준 총 브로모페놀 함량은 계절에 따라 40.9–7030 ng/g으로 크게 달랐고, 겨울에 높고 여름에 낮았다[33]. 꽈배기모자반의 형태(엽·기포·생식탁) 특징을 다룬 공공기관 자료는 확인하지 못함."},
 {"key": "related_species", "title": "관련 종·이름", "body":
  "국문 이름은 꽈배기모자반이며, 식품원료 목록에는 학명 Sargassum siliquastrum만 적혀 있고 이명·영문명은 비어 있다[1]. 사가크로마놀과 함께 이 종에서 분리된 크로멘에는 '모자반크로마놀(mojabanchromanol)'이라는 이름이 붙었다[7].\n\n"
  "식품원료 목록에는 같은 속의 모자반(S. fulvellum), 톳(S. fusiforme), 괭생이모자반(S. horneri), 지충이(S. thunbergii), 톱니모자반(S. serratifolium), 비틀대모자반(S. sagamianum), 알쏭이모자반(S. confusum)이 학명이 다른 별도 원료로 올라 있다[1]. 따라서 이들 종의 성분·안전성 자료는 꽈배기모자반 자료로 옮겨 쓰지 않는다[1].\n\n"
  "2022년 연구는 꽈배기모자반을 포함한 국내 모자반속 6종의 엽록체·미토콘드리아 유전체를 해독했다[30]. 이 연구는 모자반속이 겉모양만으로 구별하기 어렵고, 가공 과정에서 여러 갈조류 원료가 섞일 수 있으며, 과거 한국·일본에서 서로 다른 모자반속 종이 같은 종으로 잘못 분류된 적이 있다고 지적했다[30]. 그래서 단일염기변이(SNP)를 이용한 종 판별용 실시간 PCR 표지(엽록체 13개, 미토콘드리아 14개)를 개발했다[30]."},
 {"key": "cultivation", "title": "서식·채취", "body":
  "꽈배기모자반의 국내 양식·채취 생산 통계는 공공 통계에서 확인하지 못함. 확인한 연구 시료는 자연 군락에서 채집한 것이었다[25][28][29]. 통영 시료는 2020년에 채집해 −20°C에 냉동 보관했고, 표본은 국립수산과학원 연구실에 기탁되었다[28]. 제주 시료는 씻어서 바람에 말린 뒤 곱게 갈아 썼다[25].\n\n"
  "이집트 홍해 시료는 손으로 채취해 민물로 세 번 씻어 모래와 이물을 없앤 뒤 2–3일 햇볕에 말려 가루로 만들었다[29]. 이 가루를 메추라기 사료에 1%와 2% 넣은 42일 실험에서 최종 체중·일당 증체·사료 섭취량은 대조군과 비슷했지만 사료 요구율과 폐사율은 더 나았다(동물 실험)[29].\n\n"
  "양식어 사료에 꽈배기모자반을 30% 넣은 홍콩 실험에서 사료의 총 브로모페놀 함량은 340 ng/g으로 대조 사료(8.9 ng/g)보다 높았고, 8주 동안 감성돔류(Sparus sarba) 살의 브로모페놀 함량이 늘며 관능 차이도 생겼다[34]. 채집 시기별 성분 변화는 브로모페놀 외에는 확인하지 못함."},
 {"key": "processing", "title": "가공·추출 연구", "body":
  "용매별 추출 비교에서 물 추출물의 수율이 가장 높았고, 총페놀 함량은 에탄올 추출물이 127.4 mg/g으로 가장 높았다[6]. 냉동 시료 10 g을 75% 에탄올로 상온에서 3시간씩 3번 추출했을 때 수율은 5.94%였다[28]. 클로로폼 분획에서는 원심분배 크로마토그래피(n-헥산:에틸아세테이트:메탄올:물 5:5:7:3)로 사가크로마놀 E를 한 번에 분리했다[37].\n\n"
  "푸코이단은 클로로폼·메탄올(1:1)로 색소를 빼고, 포름알데하이드·에탄올(1:9) 용액에 40°C에서 5시간 담근 뒤, 셀룰라아제 효소 보조 추출과 단계별 에탄올 침전으로 나누었다[25]. 마지막 침전 분획(FSSQ)은 분자량 약 8–25 kDa로 황산기 함량이 가장 높았다[24][25]. 푸코잔틴은 80% 메탄올 추출, 클로로폼 분배, 실리카·Sephadex LH-20 칼럼, 역상 HPLC로 정제했다[27].\n\n"
  "식품 이외의 가공으로는 꽈배기모자반 바이오매스를 탄화해 자성 활성탄을 만들고 제초제 2,4-D 흡착에 쓴 연구가 있다[39]. 1991년 연구는 알긴산 제제를 빵에 6% 넣거나 시럽으로 만드는 방안을 제시했다[35]. 꽈배기모자반을 원료로 한 건강기능식품 생산실적(식약처 「식품 등의 생산실적」)은 확인하지 못함."},
 {"key": "genetics", "title": "유전 정보", "body":
  "2020년에 해독된 꽈배기모자반 미토콘드리아 유전체는 34,765 bp로, 단백질 암호 유전자 37개, rRNA 3개, tRNA 25개, 보존된 열린 해독틀 2개 등 67개 유전자를 담고 있으며 GC 함량은 36.59%다[31].\n\n"
  "2022년 연구는 꽈배기모자반의 엽록체 유전체 전체 서열을 처음으로 보고했다[30]. 이 연구에서 해독한 모자반속 6종의 엽록체 유전체는 124,175–124,517 bp 크기의 사분 구조(LSC·SSC·두 IR)였고, GC 함량은 30.3–30.6%, 단백질 암호 유전자는 139개였다[30]. 같은 6종의 미토콘드리아 유전체는 34,620–34,793 bp, 단백질 암호 유전자 37개였다[30]. 위 수치는 6종 전체의 범위이며, 받은 전문에서 종별 표가 빠져 꽈배기모자반만의 엽록체 길이는 확인하지 못함.\n\n"
  "6종의 엽록체 유전체 서열 유사도는 93.36–99.95%, 미토콘드리아는 87.91–99.81%였고, 미토콘드리아 쪽 변이가 커서 종 판별 표지를 만들기가 더 쉬웠다[30]. 꽈배기모자반의 핵 유전체 해독 보고는 확인하지 못함."},
 {"key": "safety", "title": "안전성", "body":
  "식약처 「식품원료 목록」에서 꽈배기모자반은 '사용가능' 원료이며 사용 조건은 '사용가능부위 : 전체'다[1]. 꽈배기모자반의 무기비소·총비소·요오드·중금속 함량을 측정한 공공기관 자료나 논문 수치는 확인하지 못함. 같은 속의 톳·모자반 등 다른 종의 비소 자료는 이 종에 옮겨 쓰지 않았다[1].\n\n"
  "1991년 연구에서 꽈배기모자반 알긴산나트륨은 쥐의 스트론튬 체내 부담을 3.3–4.2배 줄였고, 사람 자원자에서 위장 기능 이상이나 칼슘·철·구리·아연 대사 변화는 관찰되지 않았다[35]. 75% 에탄올 추출물은 생쥐 대식세포에서 500 µg/mL까지 뚜렷한 독성을 보이지 않았고[28], 저분자 푸코이단(FSSQ)도 100 µg/mL까지 세포 독성이 없었다[25].\n\n"
  "반면 85% 메탄올 분획에서 분리한 메로테르페노이드 일부는 사람 암세포에 IC50 0.5–5.7 µg/mL의 강한 세포 독성을 보였다(세포 실험)[19]. 사가크로메놀 D는 고혈압 쥐에 80 mg/kg을 먹였을 때 혈압을 낮췄다(동물 실험)[12]. 혈압약 등 약물과의 상호작용 자료는 확인하지 못함. 꽈배기모자반을 넣은 사료는 양식어 살의 브로모페놀을 늘려 맛을 바꿨다[34]. 알레르기·잔류농약 등 공공기관 안전 정보는 확인하지 못함."},
]

compounds = [
 {"name": "Sargachromanol G", "name_ko": "사가크로마놀 G", "class": "크로멘계 메로테르페노이드", "role": "bioactive", "part": "엽상체", "content_text": "함량 수치 없음(분리 보고)", "activity_ko": "대식세포에서 NO·PGE2·TNF-α·IL-1β·IL-6 생성을 줄였고[16], RANKL로 유도한 파골세포 분화를 억제했다(세포 실험)[17]. AChE를 IC50 1.81 µM로 억제했다(효소 실험)[20]", "source": [16, 17, 20]},
 {"name": "Sargachromanol I", "name_ko": "사가크로마놀 I", "class": "크로멘계 메로테르페노이드", "role": "bioactive", "part": "엽상체", "content_text": "함량 수치 없음(분리 보고)", "activity_ko": "아세틸콜린에스터레이스(AChE)를 IC50 0.79 µM로 가역적으로 억제했다(효소 실험)[20]", "source": [20]},
 {"name": "Sargachromanol E", "name_ko": "사가크로마놀 E", "class": "크로멘계 메로테르페노이드", "role": "bioactive", "part": "엽상체(클로로폼 분획)", "content_text": "함량 수치 없음(원심분배 크로마토그래피로 분리)", "activity_ko": "사람 백혈병 HL-60 세포에서 카스파제-3를 거친 세포자멸사를 일으켰고[15], 대식세포의 NO 생성을 억제했다(세포 실험)[37]", "source": [15, 37]},
 {"name": "Sargachromanol D", "name_ko": "사가크로마놀 D", "class": "크로멘계 메로테르페노이드", "role": "bioactive", "part": "엽상체", "content_text": "함량 수치 없음(분리 보고)", "activity_ko": "LPS로 자극한 대식세포에서 NO·PGE2와 염증성 사이토카인 생성을 줄였다(세포 실험)[38]", "source": [38]},
 {"name": "Sargachromenol D", "name_ko": "사가크로메놀 D", "class": "크로멘계 메로테르페노이드", "role": "bioactive", "part": "엽상체(동해안 시료)", "content_text": "함량 수치 없음(활성 유도 HPLC 분리)", "activity_ko": "토끼 기저동맥 수축을 풀었고(EC50 1.62 µM), 고혈압 쥐에 80 mg/kg을 먹이면 2시간 뒤 혈압이 내려 24시간 유지되었다(동물 실험)[12]", "source": [12]},
 {"name": "Sargaquinoic acid", "name_ko": "사가퀴노산", "class": "메로테르페노이드(퀴논)", "role": "bioactive", "part": "엽상체", "content_text": "함량 수치 없음(분리 보고)", "activity_ko": "대식세포에서 NF-κB 활성화와 JNK 인산화를 막아 NO 생성과 iNOS 발현을 줄였다(세포 실험)[18]", "source": [18]},
 {"name": "Sargahydroquinoic acid", "name_ko": "사가하이드로퀴노산", "class": "메로디테르페노이드(하이드로퀴논)", "role": "bioactive", "part": "엽상체", "content_text": "함량 수치 없음(나호콜·이소나호콜과 함께 분리)", "activity_ko": "이 종에서 분리한 테트라프레닐 하이드로퀴논류 20종이 중간–강한 라디칼 소거 활성과 약한 sortase A·이소시트르산 분해효소 억제 활성을 보였다[3]", "source": [3]},
 {"name": "Mojabanchromanol", "name_ko": "모자반크로마놀", "class": "크로멘", "role": "bioactive", "part": "엽상체(에탄올 추출물의 에틸아세테이트 분획)", "content_text": "함량 수치 없음(HPLC 피크 2로 분리)", "activity_ko": "0.5 mg/mL에서 TBARS 억제율 84.08%의 항산화 활성을 보인 신규 크로멘이다(시험관 실험)[7]", "source": [7]},
 {"name": "Farnesylacetone", "name_ko": "파네실아세톤(5E·5Z)", "class": "테르페노이드 케톤", "role": "bioactive", "part": "엽상체(동해안 시료)", "content_text": "함량 수치 없음; 원문은 '주요 활성 성분(major active constituents)'으로 기술", "activity_ko": "토끼 기저동맥을 확장했고[10], L형 칼슘 통로를 선택적으로 막았으며 5E형 80 mg/kg 경구 투여가 고혈압 쥐의 혈압을 오래 낮췄다(동물 실험)[11]", "source": [10, 11]},
 {"name": "Fucoxanthin", "name_ko": "푸코잔틴", "class": "카로티노이드(잔토필)", "role": "bioactive", "part": "엽상체(80% 메탄올 추출물의 클로로폼 분획)", "content_text": "함량 수치 없음(정제 보고)", "activity_ko": "UV-B를 쬔 사람 섬유아세포의 활성산소를 줄였고[13], 지카바이러스 감염 세포에서 12.5–50 µM로 감염성 바이러스 입자를 줄였다(세포 실험)[27]. 9'-cis 유도체는 대식세포의 NO 생성을 억제했다[14]", "source": [13, 14, 27]},
 {"name": "Fucoidan", "name_ko": "푸코이단(저분자 분획 FSSQ)", "class": "황산화 다당", "role": "bioactive", "part": "엽상체 건조 분말", "content_text": "FSSQ: 다당 45.96 ± 0.36%, 황산기 21.92 ± 0.46%, 푸코스 72.67%·만노스 9.26%·포도당 3.73%·갈락토스 2.35%, 분자량 약 8–25 kDa", "activity_ko": "UVB를 쬔 각질세포의 활성산소와 세포자멸사를 줄였고[24], 대식세포에서 NF-κB/MAPK와 NLRP3 인플라마좀을 억제했다(세포 실험)[25]. 다른 연구의 푸코이단(분자량 300.7·25.1 kDa)은 에탄올로 위 손상을 일으킨 생쥐의 손상 점수를 낮췄다(동물 실험)[26]", "source": [24, 25, 26]},
 {"name": "Sodium alginate", "name_ko": "알긴산나트륨", "class": "다당(우론산 중합체)", "role": "bioactive", "part": "엽상체", "content_text": "함량 수치 없음", "activity_ko": "쥐의 스트론튬 체내 부담을 3.3–4.2배 줄였고, 사람 자원자에서 안정 스트론튬 흡수를 78%(±8.9) 줄였다[35]", "source": [35]},
 {"name": "Sargasilide B", "name_ko": "사가실라이드 B(사가실라이드 A–K 대표)", "class": "메로테르페노이드", "role": "bioactive", "part": "엽상체(일본 노토반도 시료)", "content_text": "함량 수치 없음(신규 화합물로 분리)", "activity_ko": "사가실라이드 A–G 가운데 아밀로이드 β42 응집 억제가 가장 강했다(시험관 실험)[21]. 후속 연구의 사가실라이드 J는 아밀로이드 β42를 발현하는 예쁜꼬마선충의 마비를 늦췄다[22]", "source": [21, 22]},
 {"name": "2,4,6-Tribromophenol", "name_ko": "2,4,6-트라이브로모페놀(브로모페놀류)", "class": "브로모페놀(향미 성분)", "role": "bioactive", "part": "엽상체(건조중량 기준)", "content_text": "갈조 3종 합계 범위 40.9–7030 ng/g(건조중량, 계절별); 꽈배기모자반만의 값은 초록에 없음", "activity_ko": "해산물 특유의 향미를 내는 성분으로, 2-브로모페놀을 뺀 브로모페놀류가 모든 시료에서 검출되었다[33]. 30% 꽈배기모자반 사료는 감성돔류 살의 브로모페놀을 늘렸다[34]", "source": [33, 34]},
 {"name": "Phenolic compounds (total)", "name_ko": "총페놀 화합물", "class": "페놀류", "role": "bioactive", "part": "엽상체 에탄올 추출물", "content_text": "에탄올 추출물 127.4 mg/g(용매 추출물 중 최고)", "activity_ko": "에탄올 추출물은 10 mg/mL에서 아스코르브산과 비슷한 환원력을 보였다(시험관 실험)[6]. 홍콩 시료 연구에서는 항산화 효능과 총페놀 함량 사이에 상관이 없었다[8]", "source": [6, 8]},
]

assays = [
 {"role": "literature", "compound": "Fucoidan (low molecular weight fraction FSSQ/SSQC4)", "compound_ko": "저분자 푸코이단(단계별 에탄올 침전 마지막 분획)",
  "part": "엽상체 건조 분말(제주 연안 시료)",
  "content": "다당 45.96 ± 0.36%, 황산기 21.92 ± 0.46%; 단당 조성 푸코스 72.67%, 갈락토스 2.35%, 포도당 3.73%, 만노스 9.26%, 기타 11.99%; 추정 분자량 약 8–25 kDa",
  "method": "단당 조성 HPAEC-PAD, 분자량 아가로스 겔 전기영동(분자량 표지와 비교), FTIR·1H NMR 확인",
  "conditions": {"instrument": "HPAEC-PAD(단당 조성)", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "펄스 전류 검출(PAD)", "injection": "",
                 "sample_prep": "세척·풍건·분쇄 → 클로로폼:메탄올(1:1) 탈색 → 포름알데하이드:에탄올(1:9) 40°C 5시간 교반 → 80% 에탄올 세척 → 50°C 열풍 2일 건조 → 셀룰라아제 효소 보조 추출 → 단계별 에탄올 침전, 마지막 분획 회수",
                 "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "푸코이단은 이 종의 저분자 다당 연구에서 활성 분획으로 정량·특성화된 성분이다[24][25]. 수치와 전처리는 2023년 논문 전문(Materials)에서 이전 연구 값을 인용한 것을 옮겼고, 원 논문(2020) 전문은 확인 못함 — 칼럼·용리 조건은 비워 둠.",
  "source": [24, 25], "url": pmc("PMC10303138"), "source_kind": "paper"},
 {"role": "literature", "compound": "Total phenolic compounds", "compound_ko": "총페놀 화합물",
  "part": "엽상체 용매 추출물(n-헥세인·클로로폼·에탄올·물)",
  "content": "에탄올 추출물 127.4 mg/g(가장 높음); 수율은 물 추출물이 가장 높음",
  "method": "총페놀 비색 정량(초록에 시험법 세부 없음)",
  "conditions": {"instrument": "", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "", "injection": "", "sample_prep": "n-헥세인·클로로폼·에탄올·물 용매별 추출", "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "에탄올 추출물의 항산화 활성을 설명하는 지표로 쓰였다[6]. 다만 홍콩 시료 연구는 Folin-Ciocalteau법 총페놀과 항산화 효능 사이에 상관이 없다고 보고했다[8]. 전문 확인 못함.",
  "source": [6, 8], "url": pm(17887942), "source_kind": "paper"},
 {"role": "literature", "compound": "Bromophenols (2-, 4-, 2,4-di-, 2,6-di-, 2,4,6-tribromophenol)", "compound_ko": "브로모페놀류 5종",
  "part": "엽상체(건조중량 기준, 홍콩 해역 시료)",
  "content": "갈조 3종(꽈배기모자반 포함) 총 브로모페놀 40.9–7030 ng/g(건조중량, 계절별 범위; 겨울 높고 여름 낮음); 30% 꽈배기모자반 사료 340 ng/g",
  "method": "동시 수증기 증류·용매 추출(SDE) 후 GC-MS",
  "conditions": {"instrument": "GC-MS", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "질량분석", "injection": "", "sample_prep": "동시 수증기 증류·용매 추출(SDE)", "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "해산물 향미의 핵심 성분으로, 해조가 바다 환경의 주요 브로모페놀 생산자라는 근거로 정량되었다[33]. 사료 실험에서는 어육 향미 변화의 지표로 쓰였다[34]. 전문 확인 못함 — 꽈배기모자반만의 함량은 초록에 없음.",
  "source": [33, 34], "url": pm(12696947), "source_kind": "paper"},
]

d = {
 "slug": "sargassum-siliquastrum", "name_ko": "꽈배기모자반",
 "name_en": "Sargassum siliquastrum (brown seaweed)",
 "scientific_name": "Sargassum siliquastrum", "aliases": [],
 "sections": sections, "compounds": compounds, "markers": [], "nutrients": [],
 "production": [], "world": [], "assays": assays, "gi": [], "orgs": [],
 "sources": sources,
}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
print("ok", len(sources))
