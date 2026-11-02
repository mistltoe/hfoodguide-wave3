import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
A = "2026-11-02"
def pm(n, title, doi, pmid, extra=""):
    url = f"https://doi.org/{doi}" if doi else f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
    return {"n": n, "title": f"{title}{extra} (PMID {pmid})", "url": url, "publisher": "PubMed", "accessed": A}
sources = [
 {"n": 1, "title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 그롬웰잎(Lithospermum officinale L., Gromwell; 사용가능부위 : 잎, 사용가능)·그롬웰지상부(제한적사용가능부위 : 지상부(잎 제외), 제한적사용); 같은 목록의 지치뿌리·지치분말 등(L. erythrorhizon, 사용가능부위 : 뿌리※(자근)), 개지치잎(L. arvense, 사용가능부위 : 잎), 개지치씨유(한시적인정), 지초추출분말(개별인정) 행 포함", "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
 pm(2, "Exploring the Pharmacological Potential of Lithospermum officinale L.: A Review of Phytochemicals and Ethnomedicinal Uses — Molecules 2024;29(8):1856", "10.3390/molecules29081856", "38675676", " (전문 PMC11055044)"),
 pm(3, "Comparison of some secondary metabolite content in the seventeen species of the Boraginaceae family — Pharm Biol 2017;55(1):691-695", "10.1080/13880209.2016.1265986", "28140740", " (전문 PMC6130574)"),
 pm(4, "Development and Validation of a Method to Quantify Flavonoids in Leaves of Lithospermum officinale (Boraginaceae) — Dokl Biol Sci 2023;512(1):354-359 (초록만 확인)", "10.1134/S001249662370062X", "38087026"),
 pm(5, "Dynamics of alkannin/shikonin biosynthesis in response to jasmonate and salicylic acid in Lithospermum officinale — Sci Rep 2022;12(1):17093", "10.1038/s41598-022-21322-0", "36224205", " (전문 PMC9554848)"),
 pm(6, "De Novo Transcriptome Assembly and Characterization of Lithospermum officinale to Discover Putative Genes Involved in Specialized Metabolites Biosynthesis — Planta Med 2018;84(12-13):920-934 (초록만 확인)", "10.1055/a-0630-5925", "29843181"),
 pm(7, "Pyrrolizidine Alkaloids-Free Extract from the Cell Culture of Lithospermum officinale with High Antioxidant Capacity — Appl Biochem Biotechnol 2018;187(3):744-752 (초록만 확인)", "10.1007/s12010-018-2830-3", "30054862"),
 pm(8, "Neuroprotective Effect of Lithospermum officinale Callus Extract on Inflamed Primary Microglial Cells — Curr Pharm Biotechnol 2024;25(5):637-644 (초록만 확인)", "10.2174/1389201024666230816154639", "37587806"),
 pm(9, "Withdrawal Notice: Neuroprotective Effect of Lithospermum officinale callus Extract on Inflamed Primary Microglial Cells — Curr Pharm Biotechnol 2020", "10.2174/1389201021666201104145439", "33148153"),
 pm(10, "Plants known as té in Spain: an ethno-pharmaco-botanical review — J Ethnopharmacol 2005;98(1-2):1-19 (초록만 확인)", "10.1016/j.jep.2004.11.003", "15763359"),
 pm(11, "[Herbs with pearls, Fontainebleau tea (Lithospermum officinale L.)] — Rev Phytother (Paris) 1946;10:19-21 (제목만 확인, 초록 없음)", None, "20995844"),
 pm(12, "Antihormonal effects of plant extracts. Pharmacodynamic effects of Lithospermum officinale on the thyroid gland of rats; comparison with the effects of iodide — Horm Metab Res 1983;15(10):503-7 (초록만 확인)", "10.1055/s-2007-1018769", "6685685"),
 pm(13, "Inhibition by certain plant extracts of the binding and adenylate cyclase stimulatory effect of bovine thyrotropin in human thyroid membranes — Endocrinology 1984;115(2):527-34 (초록만 확인)", "10.1210/endo-115-2-527", "6745167"),
 pm(14, "Extracts and auto-oxidized constituents of certain plants inhibit the receptor-binding and the biological activity of Graves' immunoglobulins — Endocrinology 1985;116(5):1687-93 (초록만 확인)", "10.1210/endo-116-5-1687", "2985357"),
 pm(15, "Antihormonal effects of plant extracts: iodothyronine deiodinase of rat liver is inhibited by extracts and secondary metabolites of plants — Horm Metab Res 1984;16(4):188-92 (초록만 확인)", "10.1055/s-2007-1014739", "6724503"),
 pm(16, "Structures of compounds with antigonadotropic activity obtained by in vitro oxidation of caffeic acid — Planta Med 1990;56(4):395-8 (초록만 확인)", "10.1055/s-2006-960992", "2236297"),
 pm(17, "Regulation of the production of pituitary hormones by the blocking action of Lithospermum officinale — Acta Endocrinol (Copenh) 1958;29(4):525-30 (제목만 확인, 초록 없음)", "10.1530/acta.0.0290525", "13605545"),
 pm(18, "Urolithiasis and phytotherapy — Int Urol Nephrol 1994;26(5):507-11 (초록만 확인)", "10.1007/BF02767650", "7860196"),
 pm(19, "[Isolation of delta-6,9,12,15-n-octadecatetraenoic acid from the fruit of Lithospermum officinale L.] — Biochem Z 1963;339:212-8 (제목만 확인, 초록 없음)", None, "14206230"),
 pm(20, "Root-associated bacteria modulate the specialised metabolome of Lithospermum officinale L. — Front Plant Sci 2022;13:908669 (초록만 확인)", "10.3389/fpls.2022.908669", "36110355"),
 pm(21, "Transcriptional dynamics of Chitinophaga sp. strain R-73072-mediated alkannin/shikonin biosynthesis in Lithospermum officinale — Front Microbiol 2022;13:978021 (초록만 확인)", "10.3389/fmicb.2022.978021", "36071973"),
 pm(22, "Molecular identification and phytochemical screening of endophytic fungi isolated from Lithospermum officinale L. roots: A new source of shikonin — Phytochemistry 2019;168:112116 (초록만 확인)", "10.1016/j.phytochem.2019.112116", "31513947"),
 pm(23, "[Contraceptive properties of Lithospermum officinale L. grown under different agrotechnical conditions] — Pol Tyg Lek 1979;34(50):1971-2 (제목만 확인, 초록 없음)", None, "575422"),
 pm(24, "[Pharmacological studies of Shikon and Tooki. (3) Effect of topical application of the ether extracts and Shiunko on inflammatory reactions] — Nihon Yakurigaku Zasshi 1977;73(2):205-14 (초록만 확인)", None, "560340"),
 pm(25, "Research Progress of the Molecular Mechanism of Antithyroid Cancer Activity of Shikonin — Curr Mol Pharmacol 2024;17:e040923220678 (초록만 확인)", "10.2174/1874467217666230904104414", "37670707"),
 pm(26, "The Effect of Lithospermum officinale, Silver Sulfadiazine and Alpha Ointments in Healing of Burn Wound Injuries in Rat — World J Plast Surg 2017;6(3):313-318", None, "29218280", " (전문 PMC5714976)"),
 pm(27, "[Comparative characteristics of the diagnostic properties of Lythospermum arvense L. and Lithospermum officinale L.] — Farm Zh 1966;21(3):44-50 (제목만 확인, 초록 없음)", None, "5995576"),
 pm(28, "[On data on the constituents of Lithospermum officinale L. 2. On the content of substances in medicinal plants with hormone and antihormone-like effect] — Arzneimittelforschung 1964;14:34-40 (제목만 확인, 초록 없음)", None, "14223688"),
]
S = {}
S["overview"] = ("한눈에 보기",
"그롬웰(Lithospermum officinale L.)은 지치과(Boraginaceae) 지치속의 여러해살이풀로, 영어 이름은 Gromwell이다[1, 2]. "
"식약처 「식품원료 목록」에는 이 종이 '그롬웰잎'과 '그롬웰지상부' 두 원료로 올라 있다[1]. "
"잎은 사용 조건이 '사용가능부위 : 잎'인 사용가능 원료이고, 잎을 뺀 지상부는 '제한적사용가능부위 : 지상부(잎 제외)'인 제한적사용 원료다[1]. "
"목록에는 부위만 적혀 있어, 제한적사용 원료로서 어떤 식품에 얼마나 쓸 수 있는지에 대한 식품공전의 구체 조건은 확인하지 못함. "
"이 종을 원재료로 하는 건강기능식품 고시형 원료는 확인하지 못함. "
"같은 속의 지치(L. erythrorhizon, 뿌리 '자근')와 개지치(L. arvense, 잎)는 목록에 별도 원료로 올라 있으며, 이 자료에는 그 종들의 값을 섞지 않았다[1].\n\n"
"지상부에서 정량된 주요 성분은 알란토인, 로즈마린산, 클로로겐산, 루틴 같은 질소 화합물과 페놀 성분이다[3]. "
"잎의 플라보노이드는 루틴으로 환산해 절대건조중량의 2%를 넘었다[4]. "
"붉은 나프토퀴논 색소인 알칸닌·시코닌 유도체는 뿌리 주피에 쌓이며, 이 종의 뿌리에서는 소량만 정량되었다[3, 5]. "
"간독성이 알려진 피롤리지딘 알칼로이드(리코프사민·에키미딘 등)가 이 종에서 보고되었으나 어느 부위에 쌓이는지는 정해지지 않았다[2].")
S["history"] = ("역사와 이용",
"그롬웰은 여러 문화권의 민간요법에 쓰인 약초로, 총설은 중국·인도·스페인·폴란드·북아메리카의 이용 기록을 정리했다[2]. "
"폴란드에서는 기원전 약 1750–1600년 무렵 이 풀의 열매를 소독용으로 썼다는 보고가 있고, 중국 신장의 양하이(Yanghai) 고분에서는 열매가 나무 통 두 개에 붙은 채 장식으로 발견되었다[2]. "
"스페인에서는 차나무가 아닌 여러 들풀 우림도 '테(té)'라 부르는데, 그롬웰은 그 가운데 가장 중요하고 널리 퍼진 종의 하나로 꼽혔다[10]. "
"1946년 프랑스 문헌의 제목에는 '진주가 달린 풀, 퐁텐블로 차'라는 이름이 남아 있다[11].\n\n"
"1950년대 독일에서는 그롬웰 추출물이 뇌하수체 호르몬 분비를 막는다는 동물 연구가 발표되었다[17]. "
"1964년에는 호르몬·항호르몬 작용을 보이는 약초 성분 연구의 하나로 이 종의 성분이 보고되었다[28]. "
"1980년대에는 동결건조 물 추출물이 시험관에서 소 갑상샘자극호르몬(TSH)이 사람 갑상샘막에 붙는 것을 막는다는 결과가 나왔다[13]. "
"우리나라에서 이 풀을 먹어 온 전통 기록은 확인하지 못함.")
S["biology"] = ("식물학적 특징",
"지치과는 전 세계 약 135속 2600종으로 이루어지며, 지치속에는 50–60종이 있다[2]. "
"그롬웰은 유라시아 원산이고 아르헨티나 남부·콜롬비아·미국에도 들어가 자라며, 주로 온대에서 자라는 여러해살이풀이다[2]. "
"키는 90 cm까지 자라고, 가지를 치는 줄기는 길이 1.5 mm까지의 털로 덮인다[2]. "
"잎은 피침형으로 약 60–70 × 10–16 mm이며 앞쪽을 향한 털이 있다[2]. "
"꽃부리는 흰색이고 통부가 약 4 mm이며, 목 부분에 털 난 주머니 모양 돌기 다섯 개가 있다[2]. "
"열매(분과)는 길이 3–4 mm의 달걀꼴로 희고 매끄러우며 윤이 난다[2].\n\n"
"붉은 색소인 알칸닌/시코닌과 그 유도체는 세포질에서 만들어져 뿌리 주피의 세포 밖 공간에 쌓인다[5]. "
"폴란드 식물원 시료 분석에서도 시코닌 유도체는 땅속 부위에만 있다고 보아 뿌리만 따로 헥산으로 추출했다[3]. "
"국내 자생 여부와 개화 시기는 확인하지 못함.")
S["related_species"] = ("이름과 가까운 종",
"식약처 목록에서 지치속의 다른 원료는 지치(L. erythrorhizon, 별명 자초·지초, 사용 부위 뿌리 '자근')와 개지치(L. arvense, 별명 들지치, 사용 부위 잎)다[1]. "
"개지치 씨에서 짠 기름은 학명을 'Buglossoides arvensis 또는 Lithospermum arvense'로 적은 한시적 인정 원료로 올라 있다[1]. "
"지치 뿌리 추출분말은 건강기능식품 개별인정 원료로도 목록에 있다[1].\n\n"
"1977년 일본 약리 논문은 생약 자근(시콘)의 기원 식물을 'L. officinale var. erythrorhizon'으로 적었다[24]. "
"시코닌의 항암 기전 총설 가운데에는 시코닌을 L. officinale의 주성분으로 소개한 것도 있다[25]. "
"그러나 이 종을 정량한 연구에서 지상부에는 시코닌 항목이 없었고, 뿌리의 시코닌 유도체 합계도 0.079 mg/g 풍건물로 적었다[3]. "
"그래서 이 자료는 지치 뿌리(자근)의 시코닌 연구를 그롬웰 잎·지상부의 결과로 옮기지 않았다[3, 24]. "
"1966년 우크라이나 문헌은 개지치와 그롬웰을 감별하는 특징을 비교했다[27]. "
"이 종의 유전자 연구는 지치 유전체를 기준 서열로 썼으며, 두 종이 갈라진 시점을 약 50만 년 전으로 보았다[5].")
S["cultivation"] = ("재배와 산지",
"국내 재배 면적·생산량 통계(통계청·농식품부 특용작물 생산실적)에서 그롬웰 품목은 확인하지 못함. "
"재배해서 쓸 만한 수확물을 얻는 데 적어도 2년이 걸린다고 보고되었다[7]. "
"한 연구는 여러 해 동안 재배한 그롬웰 잎의 플라보노이드를 측정했다[4]. "
"폴란드 루블린의 대학 식물원에서는 2015년 6월 이 종을 포함한 지치과 17종을 종마다 3개체씩 채취해 분석했다[3]. "
"1979년 폴란드 논문은 재배 조건을 달리해 기른 그롬웰을 다루었다[23].\n\n"
"실험실에서는 뿌리 내린 꺾꽂이 묘를 배지에서 기르는 시험관 재배 체계를 썼고, 뿌리는 빛을 가리고 20 °C, 하루 16시간 조명에서 길렀다[5]. "
"메틸자스모네이트를 처리하면 뿌리의 알칸닌/시코닌 유도체가 늘었지만 살리실산은 그렇지 않았다[5]. "
"메틸자스모네이트 처리 식물은 대조군보다 새싹 길이가 최대 36%, 건조중량이 최대 55% 줄었다[5]. "
"뿌리 주변 세균 3개 균주는 시험관과 온실 모두에서 이 색소를 늘렸다[20, 21]. "
"뿌리에서 분리한 내생 곰팡이 가운데 Fusarium tricinctum 한 종만 배양 추출물에서 시코닌이 검출되었다[22]. "
"지리적 표시 등록과 생산자 단체는 확인하지 못함.")
S["processing"] = ("가공과 이용",
"식약처 목록상 그롬웰은 잎을 식품원료로 쓸 수 있고, 잎을 뺀 지상부는 제한적으로 쓸 수 있다[1]. "
"스페인의 '테'는 들에서 거둔 풀을 마른 채로 또는 날것으로 끓여 식후에 마시는 우림차다[10]. "
"그롬웰 추출물(CAS 90063-58-4)은 의약·화장품 산업에서 쓰여 왔다[7]. "
"국내 건강기능식품 생산실적에서 이 원료 품목은 확인하지 못함.\n\n"
"지상부 분석에서는 풍건 분말 1.0 g을 메탄올 100·80·60%로 차례로 초음파 추출(각 30분, 40 °C 미만)했다[3]. "
"이 종의 동결건조 물 추출물을 과망간산칼륨으로 산화하면 쥐 간 탈요오드효소 억제 활성이 낮아졌다[15]. "
"반면 카페산을 시험관에서 산화해 얻은 고리형 리그난 유도체는, 식물 효소로 산화시킨 그롬웰 생약 추출물처럼 항생식샘자극호르몬 활성을 보였다[16]. "
"캘러스(세포 덩어리) 배양은 30일이 안 되어 8.3배 증식하고 생물량이 4.9배 늘었으며, 이 세포 추출물에서는 독성 피롤리지딘 알칼로이드가 나오지 않고 로즈마린산이 주성분이었다[7]. "
"17일 된 캘러스 메탄올 추출물은 쥐 미세아교세포 실험(0.8 mg/mL)에서 TNF-α·IL-1β 분비를 줄였다[8]. "
"같은 제목의 2020년 판 논문에는 편집 요건 미충족을 이유로 한 철회 공지가 나왔다[9].")
S["genetics"] = ("유전 정보",
"그롬웰의 잎·줄기·뿌리 RNA 염기서열(4 Gbp 이상)로 처음 만든 전사체 조립에서는 유전자 단위(unigene) 77,047개가 얻어졌고 N50은 1524 bp였다[6]. "
"이 가운데 52,766개에 기능이 추정되었고, 뿌리에서 2차 대사 과정이 특히 활발했다[6]. "
"리토스페름산/클로로겐산 생합성 효소에 20개, 시코닌 생합성 효소에 48개 유전자 단위가 대응되었고, 뿌리에서 가장 많이 발현되는 시토크롬 P450 후보 15개가 제안되었다[6].\n\n"
"이 종의 유전체 해독본은 없어서, 2022년 연구는 가까운 자매종인 지치의 유전체(v1.0)에 읽기를 맞췄고 정렬률은 91%였다[5]. "
"메틸자스모네이트 처리 뿌리에서는 대조군보다 1,255개 유전자가 늘고 1,918개가 줄었으며, 살리실산 처리에서는 535개가 늘고 494개가 줄었다[5]. "
"연구진은 메발론산 경로 유전자의 발현 차이가 알칸닌/시코닌 생성 여부를 가르는 지점이라고 보았다[5]. "
"염색체 수와 엽록체 유전체는 확인하지 못함.")
S["safety"] = ("안전성",
"식약처 「식품원료 목록」에서 그롬웰잎은 사용가능, 잎을 뺀 지상부는 제한적사용 원료이며 뿌리는 사용 부위로 올라 있지 않다[1]. "
"제한적사용 원료의 배합 한도 등 식품공전상 구체 조건은 원문을 확인하지 못함. "
"국내 공공기관의 알레르기·잔류물질 정보와 EFSA 식물 성분 요람의 이 종 항목은 확인하지 못함.\n\n"
"이 종에서는 피롤리지딘 알칼로이드인 리코프사민·에키미딘·리토세닌·아세틸리토세닌 등이 보고되었고, 리코프사민과 에키미딘은 간독성이 알려져 있다[2]. "
"총설은 이 알칼로이드가 어느 부위에 쌓이는지 정해지지 않았다고 적었다[2]. "
"그롬웰 추출물에 피롤리지딘 알칼로이드가 들어 있다는 분석이 있고, 뿌리 추출물의 이 성분 때문에 이용에 제약이 있다고 보고되었다[7, 8]. "
"잎·지상부의 피롤리지딘 알칼로이드 함량은 확인하지 못함.\n\n"
"동결건조 추출물은 쥐에서 TSH와 갑상샘호르몬 수치를 낮추고 말초 T4 탈요오드화를 억제했다[12]. "
"시험관에서는 TSH와 그레이브스병 환자 IgG의 갑상샘막 결합을 막았다[13, 14]. "
"쥐 요로결석 연구는 이 풀을 포함한 7종 우림액의 효과에 대해, 더 효과적이고 무해한 물질이 이미 있다고 결론지었다[18]. "
"시장에서 산 그롬웰의 물 추출물을 쥐 화상에 바른 연구는 사용 부위를 밝히지 않았다[26]. "
"사람이 먹은 임상시험, 임신·수유 중 안전성, 약물 상호작용은 확인하지 못함.")
sections = [{"key": k, "title": t, "body": b} for k, (t, b) in S.items()]
compounds = [
 {"name": "Allantoin", "name_ko": "알란토인", "class": "퓨린 대사물(질소 화합물)", "role": "marker", "part": "지상부·뿌리",
  "content_text": "지상부 2.36 ± 0.88 mg/g 풍건물, 뿌리 0.81 ± 0.36 mg/g 풍건물(HPCE, n=3)[3]", "activity_ko": "식물의 질소 대사·운반 물질; 상처 치유 관련 성분으로 소개됨", "source": [2, 3]},
 {"name": "Rosmarinic acid", "name_ko": "로즈마린산", "class": "페놀산(카페산 에스터)", "role": "marker", "part": "지상부·뿌리·캘러스",
  "content_text": "지상부 1.2 ± 0.1 mg/g 풍건물, 뿌리 1.8 ± 0.31 mg/g 풍건물[3]; 캘러스 배양 추출물의 주성분(함량 수치는 초록에 없음)[7]", "activity_ko": "항산화 페놀 성분; 시험관 탈요오드효소 억제 성분의 하나로 보고됨", "source": [3, 7, 15]},
 {"name": "Chlorogenic acid", "name_ko": "클로로겐산", "class": "페놀산", "role": "marker", "part": "지상부",
  "content_text": "지상부 1.032 ± 0.06 mg/g 풍건물(뿌리에서는 분석 항목 아님)[3]", "activity_ko": "항산화 페놀산", "source": [3]},
 {"name": "Rutin", "name_ko": "루틴", "class": "플라보놀 배당체", "role": "marker", "part": "지상부·잎",
  "content_text": "지상부 0.754 ± 0.303 mg/g 풍건물[3]; 잎 총플라보노이드는 루틴 환산 절대건조중량의 2% 초과[4]", "activity_ko": "플라보노이드 정량의 표준물질로 쓰임", "source": [3, 4]},
 {"name": "4-Hydroxybenzoic acid", "name_ko": "p-히드록시벤조산", "class": "페놀산", "role": "bioactive", "part": "지상부",
  "content_text": "지상부 0.174 ± 0.003 mg/g 풍건물[3]", "activity_ko": "알칸닌/시코닌 생합성의 전구물질(4-HBA)", "source": [3, 5]},
 {"name": "3-(3,4-Dihydroxyphenyl)propanoic acid", "name_ko": "히드로카페산", "class": "페놀산", "role": "bioactive", "part": "지상부·뿌리",
  "content_text": "지상부 0.215 ± 0.017 mg/g 풍건물, 뿌리 0.131 ± 0.015 mg/g 풍건물[3]", "activity_ko": "카페산 유도 페놀산", "source": [3]},
 {"name": "Shikonin", "name_ko": "시코닌(유도체 합계)", "class": "나프토퀴논 색소", "role": "bioactive", "part": "뿌리(식품 사용 부위 아님)",
  "content_text": "뿌리 시코닌 유도체 합계 0.079 ± 0.002 mg/g 풍건물(HPCE, 유도체 분리 안 됨)[3]; 시험관 재배 뿌리에서 메틸자스모네이트 처리 때만 검출[5]", "activity_ko": "뿌리 주피에 쌓이는 붉은 색소; 잎·지상부 함량은 확인하지 못함", "source": [3, 5]},
 {"name": "Lycopsamine", "name_ko": "리코프사민", "class": "피롤리지딘 알칼로이드", "role": "bioactive", "part": "부위 미확정",
  "content_text": "이 종에서 보고됨(함량·부위는 총설에 없음)[2]", "activity_ko": "간독성·발암 가능성이 알려진 성분", "source": [2]},
 {"name": "Echimidine", "name_ko": "에키미딘", "class": "피롤리지딘 알칼로이드", "role": "bioactive", "part": "부위 미확정",
  "content_text": "이 종에서 보고됨(함량·부위는 총설에 없음)[2]", "activity_ko": "간독성·발암 가능성이 알려진 성분", "source": [2]},
 {"name": "Lithosenine", "name_ko": "리토세닌", "class": "피롤리지딘 알칼로이드", "role": "bioactive", "part": "부위 미확정",
  "content_text": "이 종에서 보고됨(함량 수치 없음); 약리 작용 연구는 없다고 정리됨[2]", "activity_ko": "지치속 특이 알칼로이드", "source": [2]},
 {"name": "Acetyllithosenine", "name_ko": "아세틸리토세닌", "class": "피롤리지딘 알칼로이드", "role": "bioactive", "part": "부위 미확정",
  "content_text": "이 종에서 보고됨(함량 수치 없음)[2]", "activity_ko": "리토세닌의 아세틸 유도체", "source": [2]},
 {"name": "Luteolin 7-glucuronide", "name_ko": "루테올린 7-글루쿠로나이드", "class": "플라본 배당체", "role": "bioactive", "part": "부위 미기재",
  "content_text": "이 종의 대표 플라보노이드로 소개됨(함량 수치 없음)[2]", "activity_ko": "항산화 플라보노이드", "source": [2]},
 {"name": "Stearidonic acid", "name_ko": "스테아리돈산", "class": "오메가-3 지방산(18:4)", "role": "nutrient", "part": "열매(씨)",
  "content_text": "열매에서 Δ6,9,12,15-옥타데카테트라엔산을 분리(1963, 제목만 확인)[19]; 이 종의 지질 성분으로 감마리놀렌산과 함께 소개됨[2]", "activity_ko": "열매 지질 성분(식품 사용 부위 아님)", "source": [2, 19]},
]
assays = [
 {"role": "literature", "compound": "Allantoin; Rosmarinic acid; Chlorogenic acid; Rutin; 4-Hydroxybenzoic acid; Hydrocaffeic acid",
  "compound_ko": "알란토인·로즈마린산·클로로겐산·루틴·p-히드록시벤조산·히드로카페산",
  "part": "지상부(새싹; 폴란드 루블린 대학 식물원 2015년 6월 채취, 증거표본 267-P, 실온 14일 건조)",
  "content": "알란토인 2.36 ± 0.88, 로즈마린산 1.2 ± 0.1, 클로로겐산 1.032 ± 0.06, 루틴 0.754 ± 0.303, p-히드록시벤조산 0.174 ± 0.003, 히드로카페산 0.215 ± 0.017 mg/g 풍건물(n=3)",
  "method": "HPCE-DAD(고성능 모세관 전기영동)",
  "conditions": {"instrument": "Agilent 7100 모세관 전기영동 장치, 다이오드 배열 검출기(190–600 nm)",
   "column": "용융 실리카 모세관, 내경 50 µm, 전체 길이 64.5 cm",
   "mobile_phase": "배경 전해질 50 mM 붕산염(1 M NaOH로 pH 9.2)", "gradient": "", "flow": "",
   "temp": "27 °C", "detection": "194 nm(알란토인·p-히드록시벤조산), 202 nm(루틴·히드로카페산·로즈마린산), 218 nm(클로로겐산·시코닌 유도체); 30 kV, 분석 12분",
   "injection": "50 mbar, 4초",
   "sample_prep": "풍건 분말 1.0 g을 메탄올 100·80·60%로 차례로 초음파 추출(각 30분, 40 °C 미만), 10,000 g 5분 원심분리, 상등액 합쳐 0.22 µm 막 여과",
   "standard": "표준품(이동시간·190–600 nm 흡수 스펙트럼 일치도 99.99% 초과로 동정)", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "이 종 지상부의 주요 성분을 한 번에 정량한 유일한 전문 확인 연구다. 전문(Methods)에서 조건을 옮겼으며 직선성·검출한계·회수율은 원문에 없다[3].",
  "source": [3], "url": "https://doi.org/10.1080/13880209.2016.1265986", "source_kind": "paper"},
 {"role": "literature", "compound": "Total flavonoids (as rutin)", "compound_ko": "총플라보노이드(루틴 환산)", "part": "잎(여러 해 재배)",
  "content": "루틴 환산 절대건조중량의 2% 초과", "method": "염화알루미늄 반응 차이 분광광도법",
  "conditions": {"instrument": "", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "", "injection": "",
   "sample_prep": "잎 함수에탄올 추출물과 2% 염화알루미늄(함수에탄올 용액)을 최적 부피비로 반응(최적 반응 시간 설정)",
   "standard": "루틴", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "잎은 이 종의 사용가능 부위이고, 초록은 특이성·직선성·정밀성·정확성을 검증했다고 적었다. 전문 확인 못함 — 파장·검량 범위 등은 비워 두었다[4].",
  "source": [4], "url": "https://doi.org/10.1134/S001249662370062X", "source_kind": "paper"},
]
d = {"slug": "lithospermum-officinale", "name_ko": "그롬웰", "name_en": "Gromwell", "scientific_name": "Lithospermum officinale L.",
     "aliases": ["그롬웰잎", "그롬웰지상부", "Gromwell", "common gromwell", "European stone seed", "Lithospermum officinale"],
     "sections": sections, "compounds": compounds, "markers": [], "assays": assays, "nutrients": [], "production": [], "world": [],
     "gi": [], "orgs": [], "sources": sources}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in sections: print(s["key"], len(s["body"]))
