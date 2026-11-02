import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
ACC = "2026-11-02"
def pm(pmid): return f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
S = [
 ("식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 누리장나무잎·누리장나무순(Clerodendron trichotomum Thumb. / Clerodendrum fargesii Dode, 식품원료 A코드, 사용가능, '사용가능부위 : 순, 잎', 이명 개똥나무) 행과 같은 속의 Clerodendrum cyrtophyllum잎·Clerodendrum japonicum꽃 행, 식품첨가물 '누리장나무색소'(사용불가) 행(로컬 원자료 I1020_20261013)", "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "식품의약품안전처", "2026-10-13"),
 ("Clerodendrum trichotomum Thunberg — An Ornamental Shrub with Medical Properties (Molecules 2024;29(14):3272, 총설)", pm(39064848), "PubMed (MDPI Molecules)", ACC),
 ("Clerodendrum trichotomum Thunb.: a review on phytochemical composition and pharmacological activities (Front Pharmacol 2025;15:1505851, 총설, 초록 확인)", pm(39834825), "PubMed (Frontiers in Pharmacology)", ACC),
 ("Anti-inflammatory phenylpropanoid glycosides from Clerodendron trichotomum leaves (Arch Pharm Res 2009;32(1):7-13)", pm(19183871), "PubMed (Archives of Pharmacal Research)", ACC),
 ("Studies on the anti-inflammatory effects of Clerodendron trichotomum Thunberg leaves (Arch Pharm Res 2004;27(2):189-93)", pm(15022721), "PubMed (Archives of Pharmacal Research)", ACC),
 ("Anti-inflammatory constituents isolated from Clerodendron trichotomum leaves inhibit pro-inflammatory gene expression in RAW 264.7 macrophages (Arch Pharm Res 2007;30(6):755-60)", pm(17679555), "PubMed (Archives of Pharmacal Research)", ACC),
 ("Anti-asthmatic effects of phenylpropanoid glycosides from Clerodendron trichotomum leaves and Rumex gmelini herbes in guinea-pigs (Phytomedicine 2010;18(2-3):134-42)", pm(20739157), "PubMed (Phytomedicine)", ACC),
 ("Angiotensin converting enzyme inhibitory phenylpropanoid glycosides from Clerodendron trichotomum (J Ethnopharmacol 2003;89(1):151-4)", pm(14522447), "PubMed (Journal of Ethnopharmacology)", ACC),
 ("HIV-1 integrase inhibitory phenylpropanoid glycosides from Clerodendron trichotomum (Arch Pharm Res 2001;24(4):286-91)", pm(11534758), "PubMed (Archives of Pharmacal Research)", ACC),
 ("Antioxidant activity of jionoside D from Clerodendron trichotomum (Biol Pharm Bull 2004;27(10):1504-8)", pm(15467185), "PubMed (Biological & Pharmaceutical Bulletin)", ACC),
 ("Antioxidant activity of isoacteoside from Clerodendron trichotomum (J Toxicol Environ Health A 2005;68(5):389-400)", pm(15799629), "PubMed (Journal of Toxicology and Environmental Health A)", ACC),
 ("Trichotomoside: a new antioxidative phenylpropanoid glycoside from Clerodendron trichotomum (Chem Biodivers 2006;3(1):41-8)", pm(17193214), "PubMed (Chemistry & Biodiversity)", ACC),
 ("The effects of apigenin-7-O-beta-D-glucuronopyranoside on reflux oesophagitis and gastritis in rats (Auton Autacoid Pharmacol 2005;25(3):85-91)", pm(15955027), "PubMed (Autonomic & Autacoid Pharmacology)", ACC),
 ("Antiproliferative constituents in the plants 7. Leaves of Clerodendron bungei and leaves and bark of C. trichotomum (Biol Pharm Bull 2001;24(11):1338-41)", pm(11725977), "PubMed (Biological & Pharmaceutical Bulletin)", ACC),
 ("Effects of extract from Clerodendron trichotomum on blood pressure and renal function in rats and dogs (J Ethnopharmacol 1994;42(2):77-82)", pm(8072307), "PubMed (Journal of Ethnopharmacology)", ACC),
 ("Clerodendrum trichotomum extract improves metabolic derangements in high fructose diet-fed rats (Anim Cells Syst 2021;25(6):396-404, PMC8765252 전문)", pm(35059139), "PubMed (Animal Cells and Systems)", ACC),
 ("Prevention of hyperuricemia by Clerodendrum trichotomum leaf extract in potassium oxonate-induced mice (Dev Reprod 2020;24(2):89-100, PMC7375980 전문)", pm(32734126), "PubMed (Development & Reproduction)", ACC),
 ("Anti-respiratory syncytial virus activity of Plantago asiatica and Clerodendrum trichotomum extracts in vitro and in vivo (Viruses 2019;11(7):604, PMC6669655 전문)", pm(31277257), "PubMed (Viruses)", ACC),
 ("[Chemical constituents of Clerodendrum trichotomum leaves] (Zhong Yao Cai 2014;37(9):1590-3)", pm(25857158), "PubMed (中药材)", ACC),
 ("New cytotoxic steroids from the leaves of Clerodendrum trichotomum (Steroids 2013;78(7):711-6)", pm(23583601), "PubMed (Steroids)", ACC),
 ("A new diterpenoid from the leaves of Clerodendron trichotomum (J Nat Med 2013;67(2):404-9)", pm(22825680), "PubMed (Journal of Natural Medicines)", ACC),
 ("Rearranged abietane diterpenoids from the roots of Clerodendrum trichotomum and their cytotoxicities against human tumor cells (Phytochemistry 2013;89:89-95)", pm(23462587), "PubMed (Phytochemistry)", ACC),
 ("Abietane diterpenoids from the roots of Clerodendrum trichotomum and their nitric oxide inhibitory activities (J Nat Prod 2018;81(7):1508-16)", pm(29924604), "PubMed (Journal of Natural Products)", ACC),
 ("Bioactive constituents from Clerodendrum trichotomum and their α-glucosidase inhibitory and PPAR-γ agonist activities (Fitoterapia 2024;179:106266)", pm(39437854), "PubMed (Fitoterapia)", ACC),
 ("Clerodendrin I, a new neoclerodane diterpenoid from Clerodendron trichotomum (Biosci Biotechnol Biochem 1999;63(10):1795-7)", pm(26300171), "PubMed (Bioscience, Biotechnology, and Biochemistry)", ACC),
 ("A new glycoside, acacetin-7-glucurono-(1→2)-glucuronide from the leaves of Clerodendron trichotomum (Tetrahedron Lett 1970;(33):2935-6, 초록 없음·서지만 확인)", pm(5450064), "PubMed (Tetrahedron Letters)", ACC),
 ("Isolation and characterization of a lectin from the fruit of Clerodendron trichotomum (J Biochem 1985;97(3):791-9)", pm(4019435), "PubMed (Journal of Biochemistry)", ACC),
 ("Characterization of the carbohydrate moiety of Clerodendron trichotomum lectins (Eur J Biochem 1986;161(3):779-85)", pm(3792315), "PubMed (European Journal of Biochemistry)", ACC),
 ("Contribution of pollinators to seed production as revealed by differential pollinator exclusion in Clerodendrum trichotomum (Lamiaceae) (PLoS One 2012;7(3):e33803)", pm(22442724), "PubMed (PLoS One)", ACC),
 ("SSR marker development in Clerodendrum trichotomum using transcriptome sequencing (PLoS One 2019;14(11):e0225451)", pm(31747430), "PubMed (PLoS One)", ACC),
 ("Development of nuclear SSRs for the insular shrub Clerodendrum izuinsulare (Verbenaceae) and the widespread C. trichotomum (Am J Bot 2011;98(11):e333-6)", pm(22025293), "PubMed (American Journal of Botany)", ACC),
 ("The influence of basal medium on polyphenol accumulation in shoot cultures of Clerodendrum colebrookianum and Clerodendrum trichotomum (Molecules 2024;29(24):5983, PMC11677968 전문)", pm(39770072), "PubMed (MDPI Molecules)", ACC),
 ("[Studies on the pharmacology of the Chinese drug chou-wu-tung (aerial parts of Clerodendron trichotomum Thunb.) I. The toxicity and hypotensive effect of infusion and crude extract] (Yao Xue Xue Bao 1962;9:734-40, 초록 없음·서지만 확인)", pm(14075931), "PubMed (药学学报)", ACC),
 ("[The antiphlogistic activities and toxicities of some constituents isolated from composite recipe Zhen-Tong, a mixture of Bidens bipinnata L. and Clerodendron trichotomum Thunb.] (Yao Xue Xue Bao 1965;12:129-31, 초록 없음·서지만 확인)", pm(14295456), "PubMed (药学学报)", ACC),
 ("Competitive inhibition of cytosolic Ca2+-dependent phospholipase A2 by acteoside in RBL-2H3 cells (Arch Pharm Res 2012;35(5):905-10)", pm(22644858), "PubMed (Archives of Pharmacal Research)", ACC),
 ("Isolation, structural transformation and neuroprotective activity of abietane diterpenoids from the roots of Clerodendrum trichotomum (Fitoterapia 2025;183:106488)", pm(40120983), "PubMed (Fitoterapia)", ACC),
 ("[Clerodendroside, a new glycoside from the leaves of Clerodendron trichotomum Thunb. var. fargesii Rehd. (Verbenaceae)] (Yakugaku Zasshi 1977;97(9):976-9, 초록 없음·서지만 확인)", pm(925878), "PubMed (薬学雑誌)", ACC),
 ("[Studies on the components of Clerodendron trichotomum Thunb. I. On bitter principles] (Yakugaku Zasshi 1964;84:472-4, 초록 없음·서지만 확인)", pm(14193921), "PubMed (薬学雑誌)", ACC),
 ("Clerodendrum trichotomum extract attenuates UV-B-induced skin impairment in hairless mice by inhibiting MAPK signaling (Photodermatol Photoimmunol Photomed 2024;40(6):e13011)", pm(39541388), "PubMed (Photodermatology, Photoimmunology & Photomedicine)", ACC),
]
sources = [{"n": i+1, "title": t, "url": u, "publisher": p, "accessed": a} for i, (t, u, p, a) in enumerate(S)]

sections = [
 {"key": "overview", "title": "한눈에 보기", "body":
  "누리장나무(Clerodendrum trichotomum Thunb.)는 꿀풀과(Lamiaceae, 예전 분류로는 마편초과) 누리장나무속의 낙엽 관목 또는 작은 나무로, 일본·한국·중국 동부에 자생한다[2]. 줄기와 잎을 비비면 불쾌한 냄새가 나고, 늦여름에 흰색·분홍빛 꽃이 피며 분홍·자주색으로 변하는 꽃받침에 싸인 남색 열매가 겨울까지 달린다[2].\n\n"
  "식품의약품안전처 「식품원료 목록」에는 '누리장나무잎'과 '누리장나무순' 두 행이 식품원료(A코드)로 올라 있고, 사용 여부는 '사용가능', 사용 조건은 '사용가능부위 : 순, 잎'이다[1]. 같은 목록의 학명 표기는 'Clerodendron trichotomum Thumb. / Clerodendrum fargesii Dode', 이명은 '개똥나무', 영문명은 'Glory bower, Harlequin glorybower'다[1]. 따라서 식품으로 쓸 수 있는 부위는 순과 잎뿐이며, 연구가 많은 뿌리·줄기·열매는 목록상 사용 부위가 아니다[1][2]. 열매 색소에서 온 식품첨가물 '누리장나무색소'는 2009년 7월 10일 지정이 취소되어 지금은 사용불가로 적혀 있다[1].\n\n"
  "잎에는 아크테오사이드(버바스코사이드) 같은 페닐프로파노이드 배당체와 아피제닌 배당체가 들어 있고, 스테로이드·다이터페노이드도 분리되었다[4][13][16][20][21]. 효능 연구는 세포·동물 실험뿐이며, 사람을 대상으로 한 임상시험은 확인하지 못했다[2]."},
 {"key": "history", "title": "이용의 역사", "body":
  "누리장나무는 중국에서 '취오동(臭梧桐, Chou-Wu-Tong)'이라 불리며, 잎·줄기·꽃·뿌리·열매가 오래전부터 민간약으로 쓰였다고 총설은 정리한다[2]. 전해지는 용도는 류머티즘·관절통·피부 염증·습진·천식·고혈압 등이며, 이는 전통 사용 기록이지 효능이 입증되었다는 뜻은 아니다[2]. 다른 총설은 이 종을 약용과 식용을 겸하는 식물이자 향이 있는 산나물로 소개한다[3].\n\n"
  "중국에서는 1960년대에 지상부 우려낸 물과 추출물의 독성과 혈압 강하 작용을 다룬 약리 논문이 나왔고, 도깨비바늘류(Bidens bipinnata)와 섞은 복합 처방 '진통(鎮痛)'의 소염 작용 연구도 발표되었다[33][34]. 일본에서는 1964년 쓴맛 성분 연구를 시작으로 성분 분석이 이어졌고, 1970년에는 잎에서 아카세틴 배당체가 새로 보고되었다[38][26]. 1994년 일본 연구에서는 추출물을 먹인 자연발생 고혈압 쥐의 혈압이 내려갔으나 정상 혈압 쥐에서는 변화가 없었다[15]. 한국에서는 2000년대부터 잎의 소염 작용과 페닐프로파노이드 배당체 연구가 이어졌고, 최근에는 부위가 초록에 적히지 않은 추출물로 자외선 피부 손상(생쥐) 연구도 나왔다[4][5][6][9][39]. 대표 성분 아크테오사이드는 문헌에서 '쿠사기닌(kusaginin)'·'쿠사긴(kusagin)'이라는 이름으로도 불린다[2][18]."},
 {"key": "biology", "title": "식물학적 특징", "body":
  "누리장나무는 자생지에서 높이 1.5–10 m까지 자라는 관목 또는 작은 나무이며, 유럽 정원에 심은 개체는 대개 2 m를 넘지 않는다[2]. 잎은 마주나고 길이 20 cm까지 자라며, 달걀꼴·세모진 달걀꼴 등 모양이 다양하고 잎자루는 2–8 cm다[2]. 꽃은 8–10월에 가지 끝에서 두 갈래씩 갈라지는 꽃차례(길이 8–20 cm)에 달리고, 지름 2–3 cm의 흰색 또는 분홍빛 꽃부리에서 단 향이 난다[2]. 다섯 갈래로 깊게 갈라진 꽃받침은 녹색에서 분홍·자주색으로 변하며, 지름 6–8 mm의 둥근 열매는 익으면 짙은 남색이 된다[2].\n\n"
  "일본에서 망을 씌워 방문 곤충을 가려 낸 실험에서는 호랑나비류(Papilio)와 어리호박벌(Xylocopa appendiculata)이 열매·씨앗 생산에 기여하는 유효 꽃가루받이 곤충이었다[29]. 가장 자주 찾아온 박각시류(Macroglossum pyrrhosticta)는 제꽃가루받이를 부추기는 것으로 보여 효과적인 꽃가루받이 곤충이 아니었다[29]. 열매와 잎에는 N-아세틸갈락토사민·갈락토스에 붙는 렉틴(분자량 56,000의 당단백질 이량체)이 있어 적혈구 응집 연구에 쓰였다[27][28]."},
 {"key": "related_species", "title": "가까운 종과 혼동", "body":
  "누리장나무속(Clerodendrum)은 약 580종으로, 주로 아시아·오스트레일리아·아메리카·아프리카의 열대·아열대에 분포한다[2]. 속 이름은 린네가 Clerodendrum으로 처음 썼고 뒤에 Clerodendron으로 바뀌었다가 1942년에 다시 Clerodendrum으로 돌아왔기 때문에, 옛 논문과 식약처 목록에는 'Clerodendron'이 남아 있다[1][2]. 식약처 목록의 명명자 표기 'Thumb.'는 다른 문헌에서 'Thunb.'로 쓰인다[1][2].\n\n"
  "식약처 목록에는 같은 속의 Clerodendrum cyrtophyllum(사용 부위 잎)과 Clerodendrum japonicum(사용 부위 꽃, 이명 당오동나무·당누리장나무)이 별도 원료로 올라 있으므로, 이들 자료를 누리장나무 자료와 섞으면 안 된다[1]. 누리장나무 논문 가운데에도 Clerodendrum bungei 잎과 함께 다룬 연구, C. colebrookianum과 나란히 배양한 연구, 일본 이즈 제도 고유종 C. izuinsulare와 비교한 연구가 있어 종별 값을 구분해 읽어야 한다[14][31][32]. 학명에 함께 적힌 Clerodendrum fargesii는 누리장나무의 변종(var. fargesii)으로도 다뤄지며, 이 변종 잎에서 새 배당체가 보고된 바 있다[1][32][37]. 총설은 이 종에 대한 독성 자료가 없다고 밝히고, 독성 시험 결과는 모두 같은 속 다른 종의 것이라고 구분했다[2]."},
 {"key": "cultivation", "title": "자생·재배", "body":
  "누리장나무는 일본·한국·중국 동부의 저지대와 산지에 자생하며, 비교적 추위에 강해 유럽에서는 관상수로 심는다[2]. 추운 지역에서는 열매가 맺히지 않을 수 있다[2]. 국내의 재배 면적·생산량 같은 공식 통계는 확인하지 못했다.\n\n"
  "국내 연구에 쓰인 잎은 제주도 북부에서 7월에 채집한 잎이었고, 재배 품종이나 재배 기술 자료는 확인하지 못했다[16][17]. 폴란드 연구진은 체코 식물원에서 받은 var. fargesii 종자로 시험관 신초 배양을 세워, MS·WP·SH·B5 네 가지 기본 배지가 생장과 폴리페놀 축적에 주는 영향을 비교했다[32]. 이 실험의 배양 조건은 16시간 빛·8시간 어둠, 26 ± 2 °C, 상대습도 80–90%, 6주마다 계대였다[32]. 배양 신초에서도 모식물과 비슷한 페닐에타노이드 조성이 나타났다고 보고되었다[32]."},
 {"key": "processing", "title": "가공과 이용", "body":
  "식약처 목록상 식품으로 쓸 수 있는 부위는 순과 잎이며, 사용 조건 외에 별도의 가공 기준은 목록에 적혀 있지 않다[1]. 이 목록에서 누리장나무를 원재료로 한 건강기능식품 고시형 원료 행은 찾지 못했고, 식약처 「식품 등의 생산실적」에서도 이 원료의 품목 행은 확인하지 못했다.\n\n"
  "연구에서 잎은 대개 말려 가루를 낸 뒤 추출했다[16][17]. 요산 연구에서는 말린 잎 가루를 90 °C 열수로 4시간 추출했고, 대사 연구에서는 60 °C에서 24시간 말린 잎 가루 100 g을 70% 에탄올 10 L로 25 °C에서 24시간 추출한 뒤 동결건조했다[17][16]. 이 70% 에탄올 추출물은 HPLC 분석에서 버바스코사이드(아크테오사이드)가 추출물 1 g당 160.3 ± 2.4 mg으로 주성분이었다[16]. 총설에는 잎과 꽃으로 우린 차를 쥐에게 먹인 실험도 소개되어 있으나, 원문은 확인하지 못했다[2]. 시판 원료의 규격·지표성분 기준은 확인하지 못했다."},
 {"key": "genetics", "title": "유전 정보", "body":
  "2019년 연구는 누리장나무 전사체를 RNA 시퀀싱으로 분석해 고품질 읽기 127,325,666개와 비중복 유니진 58,345개를 얻었고, 이 가운데 36,900개(63.24%)에 기능 주석을 달았다[30]. 같은 연구는 5,530개 유니진에서 SSR 6,444개를 찾고, 프라이머 200쌍을 설계해 다형성이 확인된 30쌍으로 대립유전자 200개(그중 197개 다형)를 얻었다[30].\n\n"
  "2011년 연구는 이즈 제도 고유종 C. izuinsulare와 널리 분포하는 누리장나무에 쓸 핵 SSR 프라이머 19쌍을 개발했으며, 누리장나무에서는 좌위당 대립유전자가 1–15개였다[31]. 이 마커는 다른 누리장나무속 5종에서도 4–16개 좌위가 증폭되어, 근연종 사이의 번식 체계·유전 구조 비교에 쓸 수 있다[31]. 누리장나무의 엽록체 전장 유전체나 핵 유전체 해독 결과는 확인하지 못했다. 뿌리에서 아비에탄 다이터페노이드가 많이 분리된 점은 이 속을 마편초과에서 꿀풀과로 옮긴 분류를 화학적으로 뒷받침하는 근거로 제시된다[2]."},
 {"key": "safety", "title": "안전성", "body":
  "2024년 총설은 누리장나무와 그 제품에 대한 독성 자료가 현재 없다고 밝혔으며, 함께 인용된 급성·아급성 독성 시험은 모두 같은 속의 다른 종 결과다[2]. 1962년 중국에서 지상부 우려낸 물과 추출물의 독성을 다룬 논문이 있으나 초록이 없어 내용은 확인하지 못했다[33]. 식약처 식품원료 목록에는 순·잎 사용 외에 별도의 섭취 제한이나 주의 문구가 없다[1].\n\n"
  "동물 실험에서는 잎 70% 에탄올 추출물을 고과당 식이 쥐에게 하루 체중 1 kg당 500 mg씩 16주 마시게 했을 때 독성이 나타나지 않았다고 저자들이 적었으나, 독성 평가를 목적으로 한 시험은 아니었다[16]. 세포 실험에서 시장 구입 원료(부위 미상) 열수 추출물의 50% 세포독성 농도는 764.17 μg/mL이었다[18]. 열매·잎의 렉틴은 사람 적혈구를 응집시키는 성질이 있으나 먹었을 때의 영향은 확인하지 못했다[27][28]. 열매 색소에서 온 식품첨가물 '누리장나무색소'는 2009년 7월 10일 이후 사용불가다[1]. 알레르기·잔류농약에 관한 공공기관 정보는 확인하지 못했다. 효능 연구는 세포·동물 수준이므로 질병 치료 목적으로 먹는 것은 권하지 않는다[2]."},
]
compounds = [
 {"name": "Acteoside", "name_ko": "아크테오사이드(버바스코사이드)", "class": "페닐에타노이드(페닐프로파노이드) 배당체", "role": "marker", "part": "잎(줄기·껍질에서도 분리)",
  "content_text": "잎 70% 에탄올 추출물 1 g당 160.3 ± 2.4 mg(추출물 기준, 건조 잎 기준 아님)[16]; 열수 추출물(부위 불명)에서도 주요 성분으로 확인(정량값 없음)[18]",
  "activity_ko": "세포에서 cPLA2 경쟁적 억제(Ki 5.9 μM)[35]; HIV-1 인테그레이스 억제 IC50 7.8 ± 3.6 μM(효소)[9]; 줄기 분리물 ACE 억제 IC50 373 ± 9.3 μg/mL[8]; 기니피그 천식 모델 25 mg/kg 기도저항 감소[7]", "source": [4, 7, 8, 9, 16, 18, 35]},
 {"name": "Isoacteoside", "name_ko": "아이소아크테오사이드", "class": "페닐에타노이드 배당체", "role": "bioactive", "part": "잎·껍질",
  "content_text": "함량 확인하지 못함(분리 보고)[4][14]", "activity_ko": "V79-4 세포에서 활성산소 소거·과산화수소 손상 보호(세포)[11]; B16F10 흑색종 세포 GI50 8 μM(세포)[14]", "source": [4, 11, 14]},
 {"name": "Decaffeoylacteoside", "name_ko": "데카페오일아크테오사이드", "class": "페닐에타노이드 배당체", "role": "bioactive", "part": "잎",
  "content_text": "함량 확인하지 못함(잎 메탄올 추출물에서 분리)[4]", "activity_ko": "DPPH 소거 시험에 포함(시험관)[4]", "source": [4]},
 {"name": "Leucosceptoside A", "name_ko": "류코셉토사이드 A", "class": "페닐에타노이드 배당체", "role": "bioactive", "part": "줄기",
  "content_text": "함량 확인하지 못함(분리 보고)[8]", "activity_ko": "ACE 억제 IC50 423 ± 18.8 μg/mL(시험관)[8]", "source": [8, 9]},
 {"name": "Martynoside", "name_ko": "마르티노사이드", "class": "페닐에타노이드 배당체", "role": "bioactive", "part": "줄기",
  "content_text": "함량 확인하지 못함(분리 보고)[8]", "activity_ko": "ACE 억제 IC50 524 ± 28.1 μg/mL(시험관)[8]", "source": [8]},
 {"name": "Jionoside D", "name_ko": "지오노사이드 D", "class": "페닐에타노이드 배당체", "role": "bioactive", "part": "초록에 부위 명시 없음",
  "content_text": "함량 확인하지 못함[10]", "activity_ko": "세포 내 활성산소·DPPH 소거, 과산화수소 손상 세포 보호(세포)[10]", "source": [9, 10]},
 {"name": "Trichotomoside", "name_ko": "트리코토모사이드", "class": "페닐프로파노이드 배당체(이 종에서 처음 보고)", "role": "bioactive", "part": "초록에 부위 명시 없음",
  "content_text": "함량 확인하지 못함[12]", "activity_ko": "세포 내 활성산소·DPPH 소거, 감마선·과산화수소 손상 세포 보호(세포)[12]", "source": [12]},
 {"name": "Apigenin 7-glucuronide", "name_ko": "아피제닌-7-O-글루쿠로나이드", "class": "플라보노이드 배당체", "role": "bioactive", "part": "잎",
  "content_text": "함량 확인하지 못함(잎에서 분리)[13]", "activity_ko": "쥐 역류성 식도염·위염 모델에서 십이지장 내 투여 시 위 병변 감소(동물)[13]; PPAR-γ 작용 활성(세포)[24]", "source": [13, 24]},
 {"name": "Acacetin 7-glucuronosyl-(1->2)-glucuronide", "name_ko": "아카세틴-7-글루쿠로노-(1→2)-글루쿠로나이드", "class": "플라보노이드 배당체", "role": "bioactive", "part": "잎",
  "content_text": "함량 확인하지 못함(1970년 잎에서 새 배당체로 보고)[26]", "activity_ko": "확인하지 못함", "source": [26]},
 {"name": "Clerodendrin A", "name_ko": "클레로덴드린류(네오클레로단 다이터페노이드)", "class": "네오클레로단 다이터페노이드", "role": "bioactive", "part": "잎",
  "content_text": "함량 확인하지 못함; 잎에서 클레로덴드린 A·B·D–H가 보고되었고 1999년 클레로덴드린 I가 추가됨[2][25]", "activity_ko": "클레로덴드린 I는 순무잎벌(Athalia rosae ruficornis)의 섭식 자극 물질(곤충)[25]", "source": [2, 25]},
 {"name": "Clerosterol", "name_ko": "클레로스테롤", "class": "스테롤", "role": "bioactive", "part": "잎(석유에테르 추출물)",
  "content_text": "함량 확인하지 못함(분리 보고)[19]", "activity_ko": "확인하지 못함", "source": [19]},
 {"name": "Lupeol", "name_ko": "루페올", "class": "트리터페노이드", "role": "bioactive", "part": "잎(석유에테르 추출물)",
  "content_text": "함량 확인하지 못함(분리 보고)[19]", "activity_ko": "확인하지 못함(이 종 시료로 한 시험 없음)", "source": [19]},
 {"name": "Uncinatone", "name_ko": "운시나톤", "class": "아비에탄 다이터페노이드", "role": "bioactive", "part": "뿌리(식품 사용 부위 아님)",
  "content_text": "뿌리 분리 다이터페노이드 가운데 가장 많은 성분 중 하나(정량값 없음)[36]", "activity_ko": "HT22 신경세포 손상 모델에서 10 μM 보호 효과(세포)[36]; 뿌리 다이터페노이드 일부는 암세포 독성(세포)[22]", "source": [22, 23, 36]},
 {"name": "Trichotomine", "name_ko": "트리코토민", "class": "인돌리지노인돌 계열 청색 색소", "role": "bioactive", "part": "열매(식품 사용 부위 아님)",
  "content_text": "함량 확인하지 못함; 열매의 청색 색소와 그 배당체(트리코토민 G1)로 보고[2]", "activity_ko": "확인하지 못함", "source": [2]},
]
assays = [
 {"role": "literature", "compound": "Acteoside (verbascoside)", "compound_ko": "아크테오사이드(버바스코사이드)", "part": "잎(제주도 북부, 2018년 7월 채집, 60 °C 24시간 건조) 70% 에탄올 추출물",
  "content": "추출물 1 g당 160.3 ± 2.4 mg(추출물 기준)[16]", "method": "HPLC",
  "conditions": {"instrument": "", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "", "injection": "",
   "sample_prep": "건조 잎 가루 100 g을 70% 에탄올 10 L로 25 °C에서 24시간 추출, 농축·동결건조 후 −70 °C 보관", "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "누리장나무 잎 추출물의 주성분으로 보고되었고, 잎의 소염·항산화 연구에서 활성 성분으로 반복 지목된다[4][16]. HPLC 조건은 보충 그림에만 있어 전문 확인 못함.", "source": [4, 16], "url": pm(35059139), "source_kind": "paper"},
 {"role": "literature", "compound": "Acteoside (verbascoside)", "compound_ko": "아크테오사이드(이소아크테오사이드·류코셉토사이드 A 등과 동시 정량)", "part": "시험관 신초 배양체(var. fargesii 종자 유래, 동결건조; 식품 사용 부위인 야외 개체의 순·잎 아님)",
  "content": "종별 수치는 확인하지 못함(전문 추출본에서 학명 표기가 빠져 C. colebrookianum 값과 가를 수 없음); 두 종 모두 아크테오사이드가 정량 폴리페놀 합의 약 80%[32]", "method": "HPLC-DAD(330 nm)",
  "conditions": {"instrument": "Agilent 1290 Infinity 액체크로마토그래프", "column": "InfinityLab Poroshell 120 EC-C18(4.6 × 150 mm, 4 µm)", "mobile_phase": "A 아세토나이트릴, B 0.1% 포름산",
   "gradient": "0–15분 10% A; 15–35분 10→28% A; 35–37분 28→100% A; 37–40분 100% A; 후처리 5분", "flow": "1.8 mL/min", "temp": "35 °C", "detection": "UV 330 nm", "injection": "10 µL",
   "sample_prep": "동결건조 분말 100 mg을 클로로폼 15 mL로 3회 초음파 추출(15분, 엽록소 제거) 후 메탄올 10 mL 1회·메탄올:물(8:2) 10 mL 2회 초음파 추출(15분, 40 °C), 감압 건조, 80% 메탄올에 녹여 0.22 µm 막 여과",
   "standard": "아크테오사이드·이소아크테오사이드·류코셉토사이드 A·마르티노사이드·카페산·아피제닌·아피제닌 배당체 시판 표준품(표준품이 없는 성분은 비슷한 표준품 당량으로 환산)",
   "linearity": "아크테오사이드 50–2000 µg/mL 7점, y = 7.21071407x(상관계수 0.999); 그 밖의 성분 50–1000 µg/mL 5점", "lod": "", "loq": "", "recovery": ""},
  "rationale": "누리장나무 배양 신초에서 아크테오사이드가 가장 많은 폴리페놀이어서 정량 대상으로 쓰였다[32]. PMC 전문 Methods에서 조건을 옮겼고, 검출·정량한계와 회수율은 원문에 없었다.", "source": [32], "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11677968/", "source_kind": "paper"},
]
d = {"slug": "clerodendron-trichotomum", "name_ko": "누리장나무", "name_en": "Harlequin glorybower",
     "scientific_name": "Clerodendrum trichotomum Thunb.",
     "aliases": ["누리장나무잎", "누리장나무순", "개똥나무", "Clerodendron trichotomum", "Clerodendrum fargesii", "Glory bower", "취오동(臭梧桐)"],
     "sections": sections, "compounds": compounds, "markers": [], "assays": assays, "nutrients": [], "production": [], "world": [], "gi": [], "orgs": [], "sources": sources}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in sections: print(s["key"], len(s["body"]))
