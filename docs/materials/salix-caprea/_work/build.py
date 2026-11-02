import json
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "dossier.json"
ACC = "2026-11-02"


def pm(n, title, pmid, pmc=None, doi=None, journal="", note=""):
    url = f"https://pmc.ncbi.nlm.nih.gov/articles/{pmc}/" if pmc else f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
    ids = f"PMID {pmid}" + (f", {pmc}" if pmc else "") + (f", doi:{doi}" if doi else "")
    return {"n": n, "title": f"{title} ({ids}){(' — ' + note) if note else ''}", "url": url,
            "publisher": journal + (" (PubMed Central 전문, PubMed 도구로 열람)" if pmc and "전문" in note else " (PubMed)"),
            "accessed": ACC}


sources = [
    {"n": 1, "title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 호랑버들순 행(Salix caprea L. / Salix caprea var. orbicularis Andersson; Goat willow; 식물; 사용가능, 사용 조건 '사용가능부위 : 순') 및 같은 목록의 다른 Salix 속 원료 행(로컬 원자료 I1020_20261013.json으로 대조)",
     "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
    pm(2, "Structural Characterization and Pharmacological Activity of Natural Compounds From Salix caprea L. — Chem Biodivers 2026;23(4):e03481 (총설)", "41996620", doi="10.1002/cbdv.202503481", journal="Chemistry & Biodiversity", note="초록만 확인"),
    pm(3, "Phytochemical Investigation of Marker Compounds from Indigenous Korean Salix Species and Their Antimicrobial Effects — Plants (Basel) 2022;12(1):104", "36616234", pmc="PMC9824127", doi="10.3390/plants12010104", journal="Plants (Basel)", note="PMC 전문 확인; PMC 본문에서 종 이름 서체가 빠져 있어 종–지표성분 대응은 초록의 나열 순서(S. caprea → 화합물 7)로 판단"),
    pm(4, "Methodological Aspects of Extraction, Phytochemical Characterization and Molecular Docking Studies of Salix caprea L. Bark and Leaves — Acta Chim Slov 2019;66(4):821-830", "34057484", journal="Acta Chimica Slovenica", note="초록만 확인"),
    pm(5, "Inheritance patterns of phenolics in F1, F2, and back-cross hybrids of willows: implications for herbivore responses to hybrid plants — J Chem Ecol 2003;29(5):1143-58", "12857027", doi="10.1023/a:1023829506473", journal="Journal of Chemical Ecology", note="초록만 확인"),
    pm(6, "Investigation of the flavan-3-ol patterns in willow species during one growing-season — Phytochemistry 2017;145:26-39", "29059537", doi="10.1016/j.phytochem.2017.10.001", journal="Phytochemistry", note="초록만 확인"),
    pm(7, "Phenolic extractives in Salix caprea wood and knots — Phytochemistry 2003;63(2):165-9", "12711137", doi="10.1016/s0031-9422(03)00050-5", journal="Phytochemistry", note="초록만 확인"),
    pm(8, "Bud extracts from Salix caprea L. inhibit voltage gated calcium channels and catecholamines secretion in mouse chromaffin cells — Phytomedicine 2017;36:168-175", "29157811", doi="10.1016/j.phymed.2017.09.006", journal="Phytomedicine", note="초록만 확인"),
    pm(9, "Evaluation of antioxidant activity of Salix caprea flowers — Phytother Res 2006;20(6):479-83", "16619350", doi="10.1002/ptr.1882", journal="Phytotherapy Research", note="초록만 확인"),
    pm(10, "Antioxidant activity of different polar parts of Salix caprea flower extract — Pak J Pharm Sci 2024;37(6):1565-1580", "39923149", journal="Pakistan Journal of Pharmaceutical Sciences", note="초록만 확인"),
    pm(11, "Chemical composition and pharmacological potential of aromatic water from Salix caprea inflorescence — Chin J Integr Med 2017", "28963618", doi="10.1007/s11655-017-2781-5", journal="Chinese Journal of Integrative Medicine", note="초록만 확인"),
    pm(12, "1,4-Dimethoxybenzene, a floral scent compound in willows that attracts an oligolectic bee — J Chem Ecol 2005;31(12):2993-8", "16258713", doi="10.1007/s10886-005-9152-y", journal="Journal of Chemical Ecology", note="초록만 확인"),
    pm(13, "Floral reward, advertisement and attractiveness to honey bees in dioecious Salix caprea — PLoS One 2014;9(3):e93421", "24676333", doi="10.1371/journal.pone.0093421", journal="PLoS One", note="초록만 확인"),
    pm(14, "High levels of gene flow and genetic diversity in Irish populations of Salix caprea L. inferred from chloroplast and nuclear SSR markers — BMC Plant Biol 2014;14:202", "25928320", doi="10.1186/s12870-014-0202-x", journal="BMC Plant Biology", note="초록만 확인"),
    pm(15, "Absence of geographical structure of chloroplast DNA variation in sallow, Salix caprea L. — Heredity 2003;91(5):465-74", "14576739", doi="10.1038/sj.hdy.6800307", journal="Heredity", note="초록만 확인"),
    pm(16, "Differentiation of metallicolous and non-metallicolous Salix caprea populations based on phenotypic characteristics and nuclear microsatellite (SSR) markers — Plant Cell Environ 2010;33(10):1641-1655", "20444221", doi="10.1111/j.1365-3040.2010.02170.x", journal="Plant, Cell & Environment", note="초록만 확인"),
    pm(17, "Heavy metal accumulation in trees growing on contaminated sites in Central Europe — Environ Pollut 2007;148(1):107-14", "17224228", doi="10.1016/j.envpol.2006.10.035", journal="Environmental Pollution", note="초록만 확인"),
    pm(18, "Cadmium and zinc in vegetation and litter of a voluntary woodland that has developed on contaminated sediment-derived soil — J Environ Qual 2007;36(4):1123-31", "17596620", doi="10.2134/jeq2006.0218", journal="Journal of Environmental Quality", note="초록만 확인"),
    pm(19, "EFSA PLH Panel: Commodity risk assessment of Salix caprea and Salix cinerea plants from the UK — EFSA J 2025 (9384)", "40297194", pmc="PMC12035543", doi="10.2903/j.efsa.2025.9384", journal="EFSA Journal", note="PMC 전문 확인"),
    pm(20, "Melampsora rust species on biomass willows in central and north-eastern Germany — Fungal Biol 2014;118(11):910-23", "25442294", doi="10.1016/j.funbio.2014.08.002", journal="Fungal Biology", note="초록만 확인"),
    pm(21, "Influence of Tree Species and Size on Bark Browsing by Large Wild Herbivores — Plants (Basel) 2022;11(21):2925", "36365378", doi="10.3390/plants11212925", journal="Plants (Basel)", note="초록만 확인"),
    pm(22, "Green Veterinary Pharmacology Applied to Parasite Control: Evaluation of Punica granatum, Artemisia campestris, Salix caprea Aqueous Macerates against Gastrointestinal Nematodes of Sheep — Vet Sci 2021;8(10):237", "34679067", pmc="PMC8539373", doi="10.3390/vetsci8100237", journal="Veterinary Sciences", note="PMC 전문 확인"),
    pm(23, "Salix caprea inhibits skin carcinogenesis in murine skin: inhibition of oxidative stress, ornithine decarboxylase activity and DNA synthesis — J Ethnopharmacol 2004;91(2-3):267-76", "15120450", doi="10.1016/j.jep.2003.12.028", journal="Journal of Ethnopharmacology", note="초록만 확인"),
    pm(24, "9,10-seco-9,19-cyclolanostane triterpene from Salix caprea L. (goat willow) — Nat Prod Res 2012;27(2):171-5", "22401597", doi="10.1080/14786419.2012.665912", journal="Natural Product Research", note="초록만 확인"),
    pm(25, "Synergistic inhibition of Haemonchus contortus exsheathment by flavonoid monomers and condensed tannins — Int J Parasitol Drugs Drug Resist 2015;5(3):127-34", "26199861", doi="10.1016/j.ijpddr.2015.06.001", journal="International Journal for Parasitology: Drugs and Drug Resistance", note="초록만 확인"),
    pm(26, "Expression of zinc and cadmium responsive genes in leaves of willow (Salix caprea L.) genotypes with different accumulation characteristics — Environ Pollut 2013;178:121-7", "23562959", doi="10.1016/j.envpol.2013.02.033", journal="Environmental Pollution", note="초록만 확인"),
    pm(27, "Integrated physiological, transcriptomic and metabolomic analyses provide insights into phosphorus-mediated cadmium detoxification in Salix caprea roots — Plant Physiol Biochem 2024;211:108677", "38703499", doi="10.1016/j.plaphy.2024.108677", journal="Plant Physiology and Biochemistry", note="초록만 확인"),
    pm(28, "Rapid tannin profiling of tree fodders using untargeted mid-infrared spectroscopy and partial least squares regression — Plant Methods 2021;17(1):14", "33549101", doi="10.1186/s13007-021-00715-8", journal="Plant Methods", note="초록만 확인"),
    pm(29, "Historical records of plant-insect interactions in subarctic Finland — BMC Res Notes 2022", "36209130", doi="10.1186/s13104-022-06213-x", journal="BMC Research Notes", note="초록만 확인"),
]

S = []
S.append(("overview", "한눈에 보기", """호랑버들(Salix caprea L., 영문 goat willow)은 버드나무과(Salicaceae) 버드나무속의 잎지는 작은키나무 또는 큰 관목으로, 유럽과 아시아의 서늘한 온대·한대 지역이 자생지다[22]. 국내 문헌에서도 유럽·아시아에 널리 나고 한국에도 자라는 종으로 소개된다[3]. 식약처 「식품원료 목록」에는 '호랑버들순'이라는 원료명으로 올라 있고, 학명 표기는 Salix caprea L.과 변종 Salix caprea var. orbicularis Andersson이다[1].

이 원료는 '사용가능' 원료이며 사용 조건은 '사용가능부위 : 순'이다[1]. 따라서 식품에 쓸 수 있는 부위는 어린 순뿐이고, 가지·나무껍질·꽃차례는 이 원료의 사용 부위가 아니다[1]. 이 종을 원재료로 하는 건강기능식품 고시형 원료는 확인하지 못함. 성분 연구는 꽃·나무껍질·잎·잔가지에 몰려 있으며, 2026년 총설은 이 종에서 82개 화합물(플라보노이드 32개 등)이 보고되었다고 정리했다[2]. 식용 부위인 순 자체의 성분 함량이나 사람 대상 임상시험은 확인하지 못함."""))

S.append(("history", "이용의 역사", """유럽 전통의학에서 호랑버들 추출물은 소독, 눈 강장, 진통, 수렴제로 쓰였고 말라리아·통풍·신경통·장 질환에도 쓰였다고 정리되어 있다[22]. 한국 연구진은 이 종이 한국 전통의학에서 통증과 열을 다스리는 데 쓰였다고 소개했다[3]. 최근 수십 년 동안 호랑버들 겨울눈 추출물이 산화 스트레스 관련 질환에 쓰여 왔다는 보고도 있다[8].

이탈리아 칼라브리아의 양치기들은 호랑버들 껍질과 잎을 물에 30일 담근 침출액을 양의 위장관 선충 구제에 써 왔다[22]. 그러나 이 전통 처방을 실제 양에게 시험했을 때 뚜렷한 효과(분변 충란 50% 감소)를 보인 것은 석류 침출액이었고, 다른 두 침출액의 효과는 낮았다[22]. 핀란드 아북극 지역의 1895–1900년 관찰 기록에서 호랑버들은 곤충과의 상호작용이 가장 많이 기록된 식물의 하나였다[29]. 이른 봄 꽃이 꿀벌과 버드나무만 찾는 꽃벌의 먹이가 된다는 점도 오래 주목받았다[12, 13]. 국내에서 순을 나물로 먹어 온 구체적 기록은 확인하지 못함."""))

S.append(("biology", "식물학적 특징", """호랑버들은 키가 10 m까지 자라는 잎지는 나무 또는 관목이며, 회색 껍질은 불규칙하게 갈라진다[22]. 잎은 어긋나고 넓은 타원형으로 길이 5–12 cm이며, 잎 뒷면은 부드러운 흰 털로 덮여 있다[22]. 암수딴그루이고 꽃차례(꼬리꽃차례)는 3–4월에 피며, 암꽃차례에는 100–200개, 수꽃차례에는 200–300개의 꽃이 달린다[22].

수꽃차례는 노란 꽃가루 때문에 더 화려하고 향도 더 많이 내지만, 꿀의 양과 당 농도는 암수가 비슷하고 당 조성만 다르다[13]. 꽃향기 성분 가운데 1,4-다이메톡시벤젠은 버드나무 꽃가루만 모으는 꽃벌(Andrena vaga)을 끌어들인다[12]. 추위에 강한 개척종으로 교란지에 먼저 들어오며[14], 아연·카드뮴으로 오염된 땅에서도 살아남아 잎에 이 금속을 쌓는다[16]. 중부 유럽 오염지의 호랑버들 잎에서는 카드뮴이 최대 116 mg/kg, 아연이 최대 4680 mg/kg까지 측정되었다[17]."""))

S.append(("related_species", "가까운 종과 구분", """식약처 목록에는 버드나무속 원료가 여럿 있지만 부위와 지위가 서로 다르므로 호랑버들순과 섞어 보면 안 된다[1]. 예를 들어 버드나무(Salix koreensis 등) 원료는 '제한적사용가능부위 : 가지, 가지껍질'인 제한적 사용 원료이고, 흰버드나무(Salix alba L.)와 수양버들(Salix babylonica)은 '사용불가'로 올라 있다[1]. 반면 갯버들(Salix gracilistyla)은 열매, 트리안드라버들·애깁티아카버들·Salix daphnoides 등 여러 종은 순이 사용가능 부위다[1].

호랑버들은 다른 버드나무와 쉽게 잡종을 만든다[15]. 유럽 집단의 엽록체 DNA 유형 다수가 S. cinerea·S. aurita·S. purpurea·S. atrocinerea·S. appendiculata와 겹쳤으나 S. alba·S. fragilis와는 겹치지 않았다[15]. 호랑버들과 S. repens의 잡종은 잎 페놀 성분이 두 부모의 중간이었고[5], S. caprea × cinerea 잡종의 프로안토시아니딘 양상은 두 부모의 영향을 함께 받았다[6]. 영국에서는 S. cinerea와 함께 '샐로(sallow)'로 묶여 거래된다[19]."""))

S.append(("cultivation", "재배와 산지", """국내에서 호랑버들을 작물로 재배하거나 순을 생산한 통계는 확인하지 못함. 통계청 농작물생산조사와 농림축산식품부 특용작물 생산실적의 로컬 파일에서도 호랑버들 품목은 확인하지 못함.

영국 수출 묘목장의 자료에 따르면 호랑버들은 꺾꽂이·접수용 가지(연평균 2000개, 1–3월), 맨뿌리 묘목(25,000그루, 11–3월), 화분 묘목(20,000그루, 주로 9–5월) 형태로 거래되며 대부분 노지에서 기른다[19]. EFSA는 이 묘목에 대해 담배가루이(유럽 집단)·Entoleuca mammata·Phytophthora ramorum(비EU 분리주)을 추가 평가 대상 병해충으로 골랐다[19]. 독일 바이오매스 버드나무 시험지에서 호랑버들에는 Melampsora larici-caprearum 녹병균이 발생했다[20]. 숲에서는 붉은사슴 같은 대형 초식동물이 사시나무·마가목보다 호랑버들 껍질을 더 넓게 벗겨 먹었다[21]. 금속 오염지 정화(식물상 정화)용 수종으로도 연구되며, 오염지에서 자란 개체는 잎·줄기에 카드뮴을 많이 쌓는다[16, 18]."""))

S.append(("processing", "가공 형태", """식품원료로서 호랑버들순의 가공 기준이나 제품 형태는 식품원료 목록의 사용 부위·조건 외에는 확인하지 못함[1]. 식약처 「식품 등의 생산실적」 로컬 파일(hf_items.csv)에서도 호랑버들 원료 품목은 확인하지 못함.

연구용 가공은 부위마다 다르다[4, 8, 11]. 나무껍질과 잎을 30–70% 에탄올로 추출한 비교에서는 70% 에탄올로 48시간 추출한 껍질 추출물의 생리활성 성분 함량이 가장 높았다[4]. 겨울눈은 추출물(SCBEs)로 만들어 세포 실험에 썼고[8], 생꽃은 물증류로 방향수(하이드로졸)를 얻었다[11]. 꽃 에탄올 추출물을 석유에테르·클로로포름·에틸아세테이트·부탄올·물 분획으로 나누어 항산화 성분을 비교한 연구도 있다[10]. 한국산 잔가지는 35–45 °C에서 일주일 말린 뒤 80% 에탄올 초음파 추출로 지표성분을 분리했다[3]."""))

S.append(("genetics", "유전 정보", """유럽 24개 집단의 엽록체 DNA를 조사한 연구에서 호랑버들은 지리적 구조가 거의 없고 집단 안의 변이가 컸다[15]. 연구진은 빙하기 중위도 피난처의 큰 집단, 빠른 재확산, 다른 버드나무와의 잦은 교잡 등을 그 원인으로 보았다[15]. 아일랜드 21개 숲의 183개체 분석에서는 엽록체 SSR 반수체형 79개가 나왔고, 꽃가루를 통한 유전자 흐름이 씨앗을 통한 것보다 약 7배 중요했다[14].

중부 유럽 7개 지역 170개체를 핵 SSR로 분석한 결과, 알프스 북쪽에서 금속 오염지 집단과 비오염지 집단 사이에 약하지만 유의한 분화가 있었다[16]. 금속 적응 유전형의 잎에서는 시스테인 합성 유전자가 늘 더 많이 발현되었다[26]. 인 공급과 카드뮴 해독의 관계를 본 뿌리 전사체·대사체 분석에서는 4208개 차등발현 유전자가 확인되었다[27]. 호랑버들의 염색체 수와 전장 유전체 해독 결과는 확인하지 못함."""))

S.append(("safety", "섭취 시 주의", """호랑버들순은 식약처 식품원료 목록의 사용가능 원료이지만, 사용 부위는 순으로 한정된다[1]. 버드나무류 껍질의 살리신(아스피린과 비슷한 작용의 원료 물질)은 이 원료와 부위가 다르다는 점에 유의해야 한다[1, 4]. 호랑버들 껍질·잎 비교 연구에서 살리신은 껍질에서만 검출되었고 잎에서는 검출되지 않았다[4]. 잡종 연구에서도 호랑버들 잎은 축합형 탄닌이 많고 페놀배당체(살리실레이트류)는 없었다[5]. 반면 다른 문헌은 잎에 페놀배당체가 들어 있다고 정리해 출처끼리 차이가 있다[22].

금속 오염지에서 자란 호랑버들은 잎에 카드뮴(최대 116 mg/kg)과 아연을 많이 쌓으므로, 오염 가능성이 있는 곳의 순은 채취하지 않는 것이 안전하다[17, 18]. 2026년 총설은 이 종의 독성 자료가 부족하다고 지적했다[2]. 순을 먹었을 때의 알레르기·독성 사례, 공공기관의 잔류농약 기준, 아스피린 과민증 환자에 대한 별도 주의 정보는 확인하지 못함. 꽃 추출물의 간 보호 효과[9]와 피부 발암 억제 효과[23]는 모두 생쥐 실험 결과이며, 사람에게서 확인된 것이 아니다[9, 23]."""))

compounds = [
    {"name": "Rutin", "name_ko": "루틴", "class": "플라보놀 배당체", "role": "bioactive", "part": "잎·나무껍질(순 아님)",
     "content_text": "건조 추출물 기준 껍질 1.71 g/100 g, 잎 0.434 g/100 g; 두 부위에서 가장 많은 성분(HPLC)[4]",
     "activity_ko": "항산화 성분으로 보고됨; 순에서의 함량은 확인하지 못함[4]", "source": [4]},
    {"name": "Salicin", "name_ko": "살리신", "class": "페놀배당체(살리실레이트)", "role": "bioactive", "part": "나무껍질(순 아님)",
     "content_text": "껍질 추출물에서만 검출, 잎 추출물에서는 검출되지 않음(함량 값은 초록에 없음)[4]",
     "activity_ko": "분자 도킹에서 COX-2 결합 친화도가 아세틸살리실산과 비슷했다는 계산 결과[4]; 식용 부위인 순과는 별개[1]", "source": [4, 1]},
    {"name": "Salicortin", "name_ko": "살리코르틴", "class": "페놀배당체(살리실레이트)", "role": "bioactive", "part": "부위 미상",
     "content_text": "총설은 이 종에서 살리신 유도체 8종이 보고되었다고 정리[2]; S. caprea 잎에서는 페놀배당체가 검출되지 않았다는 보고도 있음[5]",
     "activity_ko": "이 종에서의 함량·활성은 확인하지 못함[2, 5]", "source": [2, 5]},
    {"name": "Proanthocyanidins", "name_ko": "프로안토시아니딘(축합형 탄닌)", "class": "플라반-3-올 중합체", "role": "marker", "part": "잎·당년생 새순",
     "content_text": "잎에 축합형 탄닌이 많음(butanol-HCl)[5]; 잎과 당년생 새순의 총 프로안토시아니딘을 한 생장기 동안 HPLC로 추적, 암수 차이는 작음(S. caprea 수치는 초록에 없음)[6]",
     "activity_ko": "프로시아니딘·프로델피니딘형 탄닌으로 양 위선충 탈피 억제 시험의 모델 탄닌으로 쓰임[25]; 사료 수목 잎의 탄닌 분석 대상[28]", "source": [5, 6, 25, 28]},
    {"name": "Catechin", "name_ko": "카테킨", "class": "플라반-3-올", "role": "bioactive", "part": "목부·옹이, 잎·새순",
     "content_text": "목부와 옹이에서 확인, 옹이에 플라보노이드가 더 많음[7]; 잎·새순의 카테킨 함량을 계절별로 측정(수치는 초록에 없음)[6]",
     "activity_ko": "프로안토시아니딘의 구성 단위[6]", "source": [7, 6]},
    {"name": "Dihydromyricetin", "name_ko": "다이하이드로미리세틴", "class": "다이하이드로플라보놀", "role": "marker", "part": "잔가지(순 아님)",
     "content_text": "한국산 잔가지 80% 에탄올 추출물의 지표성분으로 분리(11.8 mg, 정량값 아님)[3]; 목부·옹이에서도 확인[7]",
     "activity_ko": "황색포도상구균 생장 32.4% 억제(125 μg/mL), MIC50 250 μg/mL[3]", "source": [3, 7]},
    {"name": "Taxifolin", "name_ko": "택시폴린", "class": "다이하이드로플라보놀", "role": "bioactive", "part": "목부·옹이",
     "content_text": "목부·옹이 추출물에서 확인(함량 값은 초록에 없음)[7]", "activity_ko": "이 종에서의 활성은 확인하지 못함[7]", "source": [7]},
    {"name": "Naringenin", "name_ko": "나린제닌", "class": "플라바논", "role": "bioactive", "part": "목부, 나무껍질·잎",
     "content_text": "목부·옹이에서 확인[7]; 껍질·잎 추출물에서 확인, 껍질에 더 많음[4]",
     "activity_ko": "양 위선충(Haemonchus contortus) 탈피를 250 μM에서 강하게 억제(순수 화합물 시험)[25]", "source": [7, 4, 25]},
    {"name": "Quercetin", "name_ko": "퀘르세틴", "class": "플라보놀", "role": "bioactive", "part": "나무껍질·잎",
     "content_text": "껍질·잎 추출물에서 확인, 껍질에 더 많음[4]", "activity_ko": "탄닌과 함께 쓰면 위선충 탈피 억제가 상승작용(순수 화합물 시험)[25]", "source": [4, 25]},
    {"name": "Chlorogenic acid", "name_ko": "클로로겐산", "class": "페놀산", "role": "bioactive", "part": "나무껍질·잎",
     "content_text": "껍질·잎 추출물에서 확인, 껍질에 더 많음(HPLC)[4]", "activity_ko": "이 종에서의 활성은 확인하지 못함[4]", "source": [4]},
    {"name": "p-Coumaric acid", "name_ko": "p-쿠마르산", "class": "페놀산", "role": "bioactive", "part": "잎",
     "content_text": "잎 추출물에서만 검출(페룰산·trans-신남산과 함께)[4]", "activity_ko": "이 종에서의 활성은 확인하지 못함[4]", "source": [4]},
    {"name": "Hexahydrofarnesyl acetone", "name_ko": "헥사하이드로파르네실아세톤", "class": "세스퀴테르페노이드 케톤", "role": "bioactive", "part": "꽃차례(방향수)",
     "content_text": "꽃차례 물증류 방향수 성분의 38.3%(GC-MS, 19개 성분이 99.2%)[11]", "activity_ko": "방향수 전체가 DPPH 소거·적혈구막 안정화 활성[11]", "source": [11]},
    {"name": "1,4-Dimethoxybenzene", "name_ko": "1,4-다이메톡시벤젠", "class": "벤제노이드 향기 성분", "role": "bioactive", "part": "꽃",
     "content_text": "꽃향기에서 확인, 꽃벌 더듬이 반응이 가장 강한 성분(함량 값은 초록에 없음)[12]", "activity_ko": "버드나무 전문 꽃벌 Andrena vaga 암컷을 유인[12]", "source": [12]},
    {"name": "1alpha,3beta,25-trihydroxy-9(11)-ene-16-one-9,10-seco-9,19-cyclolanostane", "name_ko": "세코사이클로라노스탄형 트라이테르펜", "class": "트라이테르펜", "role": "bioactive", "part": "부위 미상(저극성 용매 추출물)",
     "content_text": "새 화합물로 분리·구조 결정(함량 값 없음)[24]", "activity_ko": "시험관 항말라리아 원충 활성은 중간 정도[24]", "source": [24]},
]

assays = [
    {"role": "literature", "compound": "Proanthocyanidins", "compound_ko": "프로안토시아니딘(축합형 탄닌)", "part": "잎·당년생 새순(this year's sprouts)",
     "content": "S. caprea 수꽃·암꽃 개체의 잎과 당년생 새순에서 한 생장기 동안 측정, 암수 차이는 작음; S. caprea 수치는 초록에 없음(비교 범위: S. purpurea 0.1–2.6 mg/g, S. alba 3.8–14.7 mg/g)[6]",
     "method": "HPLC(MeSH 표기; 세부 조건은 전문 확인 못함)",
     "conditions": {k: "" for k in ["instrument", "column", "mobile_phase", "gradient", "flow", "temp", "detection", "injection", "sample_prep", "standard", "linearity", "lod", "loq", "recovery"]},
     "rationale": "식용 부위인 순(당년생 새순)을 직접 분석한 유일한 연구로, 호랑버들 잎·순은 살리실레이트보다 축합형 탄닌이 특징적이다; 초록만 확인, 전문 확인 못함[6, 5]",
     "source": [6, 5], "url": "https://pubmed.ncbi.nlm.nih.gov/29059537/", "source_kind": "paper"},
    {"role": "literature", "compound": "Rutin", "compound_ko": "루틴", "part": "잎·나무껍질(순 아님)",
     "content": "건조 추출물 기준 껍질 1.71 g/100 g, 잎 0.434 g/100 g[4]",
     "method": "HPLC(12개 성분 동시 분석); 총페놀·총플라보노이드는 분광광도법",
     "conditions": {**{k: "" for k in ["instrument", "column", "mobile_phase", "gradient", "flow", "temp", "detection", "injection", "standard", "linearity", "lod", "loq", "recovery"]},
                    "sample_prep": "30–70% 에탄올 수용액, 추출 시간 30분·24·48·72시간 비교(70% 에탄올 48시간이 최적)"},
     "rationale": "이 종의 껍질·잎에서 가장 많은 생리활성 성분으로 보고되어 잎 쪽 정량 지표 후보다; 초록만 확인, 전문 확인 못함[4]",
     "source": [4], "url": "https://pubmed.ncbi.nlm.nih.gov/34057484/", "source_kind": "paper"},
    {"role": "literature", "compound": "Dihydromyricetin", "compound_ko": "다이하이드로미리세틴", "part": "잔가지(순 아님, 2021년 6월 채취)",
     "content": "건조 잔가지 1.5 kg → 80% 에탄올 추출물 110.8 g; 그중 10.3 g을 분획해 지표성분 11.8 mg 분리(분리 수량이며 함량 정량값 아님)[3]",
     "method": "MPLC 분획 → 반분취 RP-HPLC 분리, UHPLC-Q-TOF HR-ESI-MS·NMR 확인",
     "conditions": {"instrument": "Agilent 1290 Infinity II UHPLC + G6545B Q-TOF MS(이중 ESI)", "column": "", "mobile_phase": "MPLC 5%→10%→30%→100% MeOH(92분); 반분취 RP-HPLC 27% MeOH",
                    "gradient": "MPLC 5→10→30→100% MeOH, 92분(7개 분획, 4번 분획 507 mg 사용)", "flow": "", "temp": "",
                    "detection": "ESI-MS 양이온 모드 m/z 321 [M+H]+; 반분취 머무름 시간 45.0분", "injection": "",
                    "sample_prep": "잔가지 35–45 °C 건조기에서 1주 건조 후 분쇄, 80% 에탄올 10 L로 90분 초음파 추출 3회, 감압 농축",
                    "standard": "NMR·HR-ESI-MS로 구조 확인(문헌값 대조)", "linearity": "", "lod": "", "loq": "", "recovery": ""},
     "rationale": "한국 자생 버드나무 8종을 LC/MS·TLC로 비교해 종마다 가장 많은 성분을 지표성분으로 정했고, 호랑버들은 다이하이드로미리세틴이었다; PMC 본문에 종 이름 서체가 빠져 종 대응은 초록의 나열 순서로 판단[3]",
     "source": [3], "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9824127/", "source_kind": "paper"},
]

d = {
    "slug": "salix-caprea", "name_ko": "호랑버들", "name_en": "Goat willow", "scientific_name": "Salix caprea L.",
    "aliases": ["호랑버들순", "Salix caprea var. orbicularis Andersson", "goat willow", "pussy willow", "sallow"],
    "sections": [{"key": k, "title": t, "body": b} for k, t, b in S],
    "compounds": compounds, "markers": [], "assays": assays, "nutrients": [], "production": [], "world": [], "gi": [], "orgs": [],
    "sources": sources,
}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for k, t, b in S:
    print(k, len(b))
