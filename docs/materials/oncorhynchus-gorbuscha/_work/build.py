import json
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "dossier.json"
ACC = "2026-11-02"


def pm(n, title, doi, journal, pmid, note="초록 확인"):
    return {"n": n, "title": f"{title} ({note})", "url": f"https://doi.org/{doi}",
            "publisher": f"{journal}, PMID {pmid}", "accessed": ACC}


sources = [
    {"n": 1, "title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — Oncorhynchus gorbuscha 1행: 원료명 '곱사연어', 영문 Pink salmon, Humpback salmon, 분류 수산물, 대분류 식품원료(A코드), 부위 '-', 사용조건 기준 없음, 상태 사용가능, 별명 없음; 같은 속 다른 종 행: 연어·태평양연어 등(O. keta), 송어·산천어 등(O. masou masou), 은연어(O. kisutch), 무지개송어(O. mykiss), 왕연어(O. tshawytscha), Sockeye salmon(O. nerka); 고시형 원료 원재료 목록(KR_NOTICE) 없음 — 로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json, docs/materials/oncorhynchus-gorbuscha/card.json",
     "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
    pm(2, "The pink salmon genome: Uncovering the genomic consequences of a two-year life cycle. PLoS One 2021;16(12):e0255752", "10.1371/journal.pone.0255752", "PLoS One", "34919547"),
    pm(3, "Cycles, stochasticity and density dependence in pink salmon population dynamics. Proc Biol Sci 2011;278(1714):2060-8", "10.1098/rspb.2010.2335", "Proceedings of the Royal Society B", "21147806"),
    pm(4, "Comparative phylogeography of the two pink salmon broodlines: an analysis based on a mitochondrial DNA genealogy. Mol Ecol 2002;11(6):1077-101", "10.1046/j.1365-294x.2002.01506.x", "Molecular Ecology", "12030984"),
    pm(5, "Parallel signatures of selection in temporally isolated lineages of pink salmon. Mol Ecol 2014;23(10):2473-85", "10.1111/mec.12769", "Molecular Ecology", "24762204"),
    pm(6, "Supplementing long-chain n-3 polyunsaturated fatty acids in canned wild Pacific pink salmon with Alaska salmon oil. Food Sci Nutr 2013;1(1):15-26", "10.1002/fsn3.4", "Food Science & Nutrition", "24804010", "PMC3951564 전문 확인"),
    pm(7, "Valorization of Pink Salmon Processing By-Products: Nutritional Composition, Starch-Modified Gel Quality and Digestibility. Foods 2026;15(18):3259", "10.3390/foods15183259", "Foods", "42794043", "PMC13605703 전문 확인"),
    pm(8, "Triploidy does not decrease contents of eicosapentaenoic and docosahexaenoic acids in filets of pink salmon Oncorhynchus gorbuscha. Food Chem 2016;216:66-9", "10.1016/j.foodchem.2016.08.021", "Food Chemistry", "27596393"),
    pm(9, "Quality changes of salmon (Oncorhynchus gorbuscha) muscle during thermal processing. J Food Sci 2007;72(2):S103-11", "10.1111/j.1750-3841.2006.00246.x", "Journal of Food Science", "17995850"),
    pm(10, "Alaska pink salmon (Oncorhynchus gorbuscha) spoilage and ethanol incidence in the canned product. J Agric Food Chem 2007;55(7):2517-25", "10.1021/jf062245m", "Journal of Agricultural and Food Chemistry", "17335220"),
    pm(11, "Stabilizing oils from smoked pink salmon (Oncorhynchus gorbuscha). J Food Sci 2009;74(3):C248-57", "10.1111/j.1750-3841.2009.01099.x", "Journal of Food Science", "19397710"),
    pm(12, "Bruise detection in Pacific pink salmon (Oncorhynchus gorbuscha) by visible and short-wavelength near-infrared (SW-NIR) spectroscopy (600-1100 nm). J Agric Food Chem 2003;51(22):6404-8", "10.1021/jf0346197", "Journal of Agricultural and Food Chemistry", "14558754"),
    pm(13, "False-positive fluorescence by pink salmon tissue and staphylococci in a rapid test for Escherichia coli. J Food Prot 1998;61(9):1119-23", "10.4315/0362-028x-61.9.1119", "Journal of Food Protection", "9766061"),
    pm(14, "Essential and non-essential trace elements in fish consumed by indigenous peoples of the European Russian Arctic. Environ Pollut 2019;253:966-973", "10.1016/j.envpol.2019.07.072", "Environmental Pollution", "31351305"),
    pm(15, "Flesh quality of market-size farmed and wild British Columbia salmon. Environ Sci Technol 2007;41(2):437-43", "10.1021/es060409+", "Environmental Science & Technology", "17310704"),
    pm(16, "Bioaccumulation of HCHs and DDTs in organs of Pacific salmon (genus Oncorhynchus) from the Sea of Okhotsk and the Bering Sea. Chemosphere 2016;157:174-80", "10.1016/j.chemosphere.2016.05.039", "Chemosphere", "27219293"),
    pm(17, "Diphyllobothrium nihonkaiense Tapeworm Larvae in Salmon from North America. Emerg Infect Dis 2017;23(2):351-353", "10.3201/eid2302.161026", "Emerging Infectious Diseases", "28098540"),
    pm(18, "Anisakis simplex (s.s.) larvae in wild Alaska salmon: no indication of post-mortem migration from viscera into flesh. Dis Aquat Organ 2011;94(3):201-9", "10.3354/dao02317", "Diseases of Aquatic Organisms", "21790067"),
    pm(19, "Detection and identification of Diphyllobothrium nihonkaiense plerocercoids from wild Pacific salmon (Oncorhynchus spp.) in Japan. J Helminthol 2010;84(4):434-40", "10.1017/S0022149X10000155", "Journal of Helminthology", "20334715"),
    pm(20, "Identification of fish species after cooking by SDS-PAGE and urea IEF: a collaborative study. J Agric Food Chem 2000;48(7):2653-8", "10.1021/jf990907k", "Journal of Agricultural and Food Chemistry", "10898602"),
    pm(21, "Identification of the sex chromosome pair in chum salmon (Oncorhynchus keta) and pink salmon (Oncorhynchus gorbuscha). Cytogenet Genome Res 2007;116(4):298-304", "10.1159/000100414", "Cytogenetic and Genome Research", "17431328"),
    pm(22, "Dorsal hump morphology in pink salmon (Oncorhynchus gorbuscha). J Morphol 2014;275(5):514-27", "10.1002/jmor.20234", "Journal of Morphology", "24323872"),
    pm(23, "Rapid genetic adaptation to a novel ecosystem despite a large founder event. Mol Ecol 2024;33(20):e17121, 2023 온라인 게재", "10.1111/mec.17121", "Molecular Ecology", "37668092"),
    pm(24, "Comparative genetic variability of pink salmon from different parts of their range: native Pacific, artificially introduced White Sea and naturally invasive Atlantic Scottish rivers. J Fish Biol 2022;100(2):549-560", "10.1111/jfb.14966", "Journal of Fish Biology", "34837402"),
    pm(25, "Growth of invasive pink salmon (Oncorhynchus gorbuscha) at sea assessed by scale analysis. J Fish Biol 2022;100(1):218-228", "10.1111/jfb.14937", "Journal of Fish Biology", "34724203"),
    pm(26, "Active feeding of downstream migrating juvenile pink salmon (Oncorhynchus gorbuscha) revealed in a large Barents Sea river using diet and stable isotope analysis. J Fish Biol 2024;104(3):797-806", "10.1111/jfb.15625", "Journal of Fish Biology", "37986023"),
    pm(27, "Transhemispheric ecosystem disservices of pink salmon in a Pacific Ocean macrosystem. Proc Natl Acad Sci U S A 2018;115(22):E5038-E5045", "10.1073/pnas.1720577115", "PNAS", "29760093"),
    pm(28, "Climate change, pink salmon, and the nexus between bottom-up and top-down forcing in the subarctic Pacific Ocean and Bering Sea. Proc Natl Acad Sci U S A 2014;111(18):E1880-8", "10.1073/pnas.1319089111", "PNAS", "24706809"),
    pm(29, "Reduced relative fitness in hatchery-origin Pink Salmon in two streams in Prince William Sound, Alaska. Evol Appl 2022;15(3):429-446", "10.1111/eva.13356", "Evolutionary Applications", "35386398"),
    pm(30, "Evidence of Olfactory Imprinting at an Early Life Stage in Pink Salmon (Oncorhynchus gorbuscha). Sci Rep 2016;6:36393", "10.1038/srep36393", "Scientific Reports", "27827382"),
    pm(31, "Early development of resistance to the salmon louse, Lepeophtheirus salmonis (Krøyer), in juvenile pink salmon, Oncorhynchus gorbuscha (Walbaum). J Fish Dis 2008;31(8):591-600", "10.1111/j.1365-2761.2008.00933.x", "Journal of Fish Diseases", "18482380"),
    pm(32, "Comparative transcriptomics of Atlantic Salmo salar, chum Oncorhynchus keta and pink salmon O. gorbuscha during infections with salmon lice Lepeophtheirus salmonis. BMC Genomics 2014;15:200", "10.1186/1471-2164-15-200", "BMC Genomics", "24628956"),
    pm(33, "Incorporating covariates into fisheries stock assessment models with application to Pacific herring. Ecol Appl 2008;18(5):1270-86", "10.1890/07-0708.1", "Ecological Applications", "18686586"),
    pm(34, "Diet and Blood Concentrations of Essential and Non-Essential Elements among Rural Residents in Arctic Russia. Nutrients 2022;14(23):5005", "10.3390/nu14235005", "Nutrients", "36501035"),
    pm(35, "Fish protein substrates can substitute effectively for poultry by-product meal when incorporated in high-quality senior dog diets. J Anim Physiol Anim Nutr 2009;93(4):447-55", "10.1111/j.1439-0396.2008.00826.x", "Journal of Animal Physiology and Animal Nutrition", "18492029"),
]

sections = [
    {"key": "overview", "title": "한눈에 보기", "body":
     "곱사연어(Oncorhynchus gorbuscha)는 식약처 「식품원료 목록」에 '곱사연어'(영문 Pink salmon, Humpback salmon)라는 원료명으로 올라 있는 수산물이다[1]. 이 목록에서 곱사연어는 학명 1행뿐이며 상태는 '사용가능', 부위 칸은 '-'이고 따로 정한 사용 조건이나 별명은 없다[1]. 건강기능식품 고시형 원료의 원재료 목록에는 없으므로 식약처가 정한 지표성분도 없다[1].\n\n"
     "곱사연어는 서태평양에 사는 태평양연어 다섯 종 가운데 성어가 가장 작지만 수가 가장 많아, 세계 연어 어업의 상업적 가치에서 큰 몫을 차지한다[2]. 식품원료 목록의 영문명에는 Humpback salmon도 함께 적혀 있는데, 실제로 산란기 수컷 등에는 혹이 생기며 이 혹은 연골이 아니라 결합조직이 늘어난 것이다[1, 22]. 알래스카에서는 2005–2009년 평균 연간 어획량이 약 175,000 t으로 전체 연어 어획의 약 절반이었고, 그 약 55%가 통조림으로 가공되었다(논문 서론 인용값)[6]. 살의 지질은 2–9%로 변동이 크며, EPA·DHA 같은 오메가-3 지방산의 공급원으로 연구되었다[6]. 국가표준식품성분표의 곱사연어 성분값과 국내 어획·수입 통계는 이번 조사에서 확인하지 못함."},
    {"key": "history", "title": "이용·연구 역사", "body":
     "알래스카 연어 산업 초기에는 연어 머리에서 짜낸 연어 기름을 통조림에 넣기도 했으나, 1960년대 후반 대부분의 가공업체가 이 관행을 그만두었다[6]. 미국 연방규정(21 CFR 161.70)의 태평양연어 통조림 기준에서 소금 말고 허용되는 선택 원료는 연어 기름뿐이라고 소개되었다(논문 인용)[6]. 2000년대에는 통조림용 곱사연어의 가열 살균, 부패와 에탄올 생성, 멍 검출 같은 가공 품질 연구가 이어졌다[9, 10, 12].\n\n"
     "곱사연어는 원래 분포지 밖으로도 옮겨졌다[23, 24]. 북미 오대호에는 31세대 전 한 번의 우발적 도입으로 들어가 자리 잡았고, 대서양 쪽 백해(White Sea) 지역에는 태평양에서 옮겨 방류한 곱사연어가 정착했다[23, 24]. 노르웨이 바다에는 1960년 무렵부터 적은 수가 나타났으나 2017년부터 북부 하천에서 수가 폭발적으로 늘었다[25]. 2014년과 2018년에는 짝수·홀수 해마다 바뀌는 곱사연어의 많은 개체 수가 북태평양 생태계와 바닷새에 미치는 영향을 다룬 연구가 나왔다[28, 27]. 2021년에는 짝수 해·홀수 해 계통 각각의 참조 유전체가 발표되었다[2]."},
    {"key": "biology", "title": "어종·생활사", "body":
     "곱사연어는 정확히 2년의 생활사를 가지며, 바다와 강을 오가고(소하성) 한 번 산란한 뒤 죽는다[3]. 이 때문에 같은 강에서도 짝수 해와 홀수 해에 산란하는 두 계통이 시간적으로 번식이 격리되어 있다[3, 5]. 한 강에서는 한 계통이 다른 계통보다 훨씬 많은 경우가 많고, 우세 계통이 바뀌기도 한다[3]. 33개 집단 분석은 이런 주기가 계통 사이의 밀도 의존적 사망과 우연한 변동이 겹쳐 생긴다고 보았다[3].\n\n"
     "어린 곱사연어는 태평양연어 가운데 민물에 머무는 기간이 가장 짧으며, 알에서 갓 나온 자어 시기에 냄새 물질을 노출한 실험에서 성어가 그 물질에 끌려 이른 시기에도 고향 물의 냄새를 각인할 수 있음이 보였다[30]. 어린 개체는 0.3 g보다 무거워지면서 바다이(Lepeophtheirus salmonis)에 대한 타고난 저항성이 생겨 0.7 g 무렵에는 작동했고, 이 시기는 비늘이 생기는 피부 변화와 겹쳤다[31]. 바렌츠해로 흐르는 테노강에서는 어린 개체가 하구로 내려가는 동안 깔따구·하루살이 유충을 실제로 먹었다[26]. 바다에서는 1970년대 이후 수가 크게 늘어, 많은 해에는 다른 연어와 바닷새의 먹이 자원을 줄이는 영향을 미치는 것으로 제시되었다[28, 27]. 성숙한 수컷의 등 혹은 연골이 없고 제1형 콜라겐 섬유로 된 결합조직과 가시뼈 성장으로 생긴다[22]."},
    {"key": "related_species", "title": "관련 종·이름", "body":
     "곱사연어는 연어속(Oncorhynchus)에 속하며, 식약처 「식품원료 목록」에는 같은 속에서 연어·태평양연어(O. keta), 송어·산천어(O. masou masou), 은연어(O. kisutch), 무지개송어(O. mykiss), 왕연어(O. tshawytscha), Sockeye salmon(O. nerka)이 각각 따로 올라 있다[1]. 이 종들의 성분·안전 자료는 곱사연어와 섞어 쓰면 안 된다[1].\n\n"
     "곱사연어와 연어(O. keta)는 익힌 살로는 구별이 어려울 수 있다[20]. 9개 실험실 공동 연구에서 요소 등전점 전기영동으로는 두 종을 가르지 못한 실험실이 있었고, SDS 전기영동은 대부분의 연어속 종을 구별했다[20]. 염색체에서는 곱사연어의 성염색체 쌍이 가장 작은 중부 염색체 쌍으로, 작은 끝부 염색체 쌍인 연어와 모양이 달랐다[21]. 대서양연어·연어(O. keta)와 함께 기른 바다이 감염 실험에서는 곱사연어의 감염 밀도가 가장 낮아 저항성 종으로 분류되었다[32]."},
    {"key": "cultivation", "title": "어획·증식·분포 확대", "body":
     "곱사연어는 주로 자연산을 어획하며, 알래스카에서는 2005–2009년 평균 약 175,000 t이 잡혔다(논문 서론이 알래스카 어류수렵부 자료를 인용)[6]. 알래스카 프린스윌리엄사운드에서는 15세대 넘게 대규모 부화장 방류가 이어져 왔다[29]. 이곳 두 하천에서 길을 잃고 들어온 부화장 출신 어미의 상대 번식 성공률은 암컷 0.03–0.47, 수컷 0.05–0.86으로 자연산보다 낮았다[29]. 같은 해역 청어 자원이 회복되지 않는 요인으로 부화장 출신 어린 곱사연어와의 경쟁·포식이 가장 유의한 요인으로 분석되었다[33].\n\n"
     "러시아 백해의 한 만에서는 곱사연어를 양식해 2배체와 3배체의 살 지방산을 비교한 연구가 있다[8]. 백해에 옮겨진 집단은 유전적 병목과 창시자 효과를 보였고, 2017년 스코틀랜드 하천에 나타난 개체는 백해 집단과 구별되지 않았다[24]. 노르웨이 북부에서는 2017년부터 수가 폭발적으로 늘었고, 늦여름·초가을 바다 성장이 산란 시 몸길이 변이의 27%를 설명했다[25]. 국내 어획·양식 통계는 이번 조사에서 확인하지 못함."},
    {"key": "processing", "title": "가공·저장·품질", "body":
     "알래스카식 통조림 실험에서는 215 g 토막을 소금 3 g과 함께 캔에 넣고 120 °C에서 69분 가열 살균했다[6]. 피부에 얼룩(워터마킹)이 없는 밝은 물고기 통조림의 지질은 5.8%, 얼룩이 심한 어두운 물고기는 3.5%였고, 어두운 물고기에 연어 기름 2%를 넣으면 지질이 5.7%로 맞춰졌다[6]. 곱사연어 살을 121.1 °C에서 가열하면 품질 변화의 대부분이 처음 10분 안에 일어났다[9].\n\n"
     "통째 보관한 곱사연어는 14 °C에서 3일, 1 °C에서 12일 만에 관능 평가에서 거부되었고, 이때 껍질 호기성 세균 수는 4.8 log CFU/cm²였다[10]. 14 °C 보관어로 만든 통조림은 에탄올 농도가 관능 결과와 잘 맞았지만 1 °C 보관어에서는 맞지 않았다[10]. 머리를 95 °C로 훈연한 뒤 뽑은 기름은 날 머리 기름보다 산화 생성물이 적고 알파-토코페롤이 많았다[11]. 근적외선 분광으로 껍질 위에서 멍을 찾는 방법은 정상 부위의 약 84%, 멍든 부위의 약 81%를 맞게 분류했다[12].\n\n"
     "필레를 뜨고 남는 부산물은 원료의 약 4분의 1이며, 기계로 발라낸 부산물 살은 수분 83.77%, 단백질 9.99%, 지질 3.73%였다[7]. 곱사연어 가수분해물은 노령견 사료의 단백질 원료로도 시험되었다[35]. 대장균 신속 검사(MUG 형광법)에서는 곱사연어 필레 자체가 위양성 형광을 낼 수 있다[13]."},
    {"key": "genetics", "title": "유전 정보", "body":
     "2021년 연구는 짝수 해·홀수 해 계통 각각의 참조 유전체를 조립하고, 캐나다 6개 하천과 일본 1개 하천 개체의 전장 유전체를 다시 읽었다[2]. 두 계통 사이에는 여러 동원체 부근에 수백만 염기쌍 길이의 분화(Fst) 정점이 있었고, 가장 큰 정점은 홀수 해 유전체의 약 100만 염기쌍 염색체 다형과 겹쳤다[2]. 북미 세 쌍의 짝수·홀수 해 집단에서 RAD 방식으로 약 8,000개 SNP를 찾았고, 두 계통에서 나란히 선택 흔적을 보이는 SNP 15개가 확인되었다[5]. 미토콘드리아 DNA 분석에서는 80마리로 만든 계보에서 38개 일배체형이 5개 계통으로 묶였고, 18개 집단 718마리를 보았을 때 짝수 해 계통 안에서 아시아와 알래스카 집단이 뚜렷하게 나뉘었다[4].\n\n"
     "오대호에 들어간 집단은 원 집단 유효 집단 크기 146,886에서 창시 집단 72로 줄어 SNP 수가 37.7%, 관찰 이형접합도가 8.2% 감소했다[23]. 그럼에도 47개 좌위에서 선택 흔적이 보였고, 특히 낮 길이 차이와 관련된 생체시계 유전자 per2에 강한 선택 반응이 있었다[23]. 5S rRNA 유전자는 곱사연어에서 상염색체 중부 염색체 두 쌍의 동원체에 있어 연어(O. keta)와 위치가 달랐다[21]."},
    {"key": "safety", "title": "안전성", "body":
     "곱사연어는 날로 먹을 때 기생충에 주의해야 한다[17, 18]. 알래스카 코르도바 근처에서 잡은 곱사연어 12마리를 조사한 연구에서 먹는 살의 아니사키스(Anisakis simplex s.s.) 3기 유충 평균 감염 강도는 마리당 21개체였다[18]. 같은 연구에서 잡은 뒤 바로 내장을 뺀 개체와 24시간 내장째 보관한 개체 사이에 배쪽 살의 유충 수 차이는 없었다(곱사연어만 따로 나눈 결과인지는 초록에서 확인하지 못함)[18]. 알래스카 자연산 곱사연어 살에서 동해긴촌충(Diphyllobothrium nihonkaiense) 유충이 검출되었고, 일본산 곱사연어 27마리에서는 18.5%(5마리)에서 열두촌충류(Diphyllobothrium) 유충이 나왔다(분자 종 동정은 연어·송어 유충만 함)[17, 19].\n\n"
     "러시아 북극권에서 먹는 생선 7종 가운데 곱사연어의 셀레늄/수은 몰비는 71.1로 가장 높았고, 수은은 강꼬치고기보다 3–4배 낮은 수준이었다[14]. 캐나다 브리티시컬럼비아의 야생 연어 5종(곱사연어 포함) 살의 평균 총수은은 종에 따라 0.013–0.077 μg/g으로 캐나다 보건부 기준 0.5 μg/g보다 훨씬 낮았다[15]. 오호츠크해·베링해 곱사연어 살의 HCH+DDE 평균은 지질 기준 141 ng/g으로 홍연어·왕연어보다 낮았다[16]. 네네츠 지역 주민 조사에서 곱사연어를 자주 먹을수록 혈중 비소 농도가 높았다[34].\n\n"
     "식약처 고시형 원료가 아니어서 섭취 시 주의사항 고시 문구는 없다[1]. 국내 공공기관의 곱사연어 알레르기·잔류 기준 정보는 이번 조사에서 확인하지 못함."},
]

compounds = [
    {"name": "Docosahexaenoic acid", "name_ko": "도코사헥사엔산(DHA)", "class": "n-3 고도불포화지방산", "role": "nutrient", "part": "통조림(살·뼈·껍질·국물 포함)",
     "content_text": "밝은 물고기 무첨가 통조림 598±66 mg/100 g, 어두운 물고기 354±117 mg/100 g[6]",
     "activity_ko": "EPA와 함께 통조림 곱사연어의 주된 장쇄 오메가-3 지방산이다[6]", "source": [6]},
    {"name": "Eicosapentaenoic acid", "name_ko": "에이코사펜타엔산(EPA)", "class": "n-3 고도불포화지방산", "role": "nutrient", "part": "통조림",
     "content_text": "밝은 물고기 무첨가 통조림 344±81 mg/100 g, 어두운 물고기 179±54 mg/100 g[6]",
     "activity_ko": "3배체와 2배체 양식 곱사연어 필레의 무게당 EPA·DHA 함량은 비슷했다[8]", "source": [6, 8]},
    {"name": "Palmitic acid", "name_ko": "팔미트산", "class": "포화지방산", "role": "nutrient", "part": "통조림",
     "content_text": "밝은 물고기 무첨가 통조림 589±102 mg/100 g, 어두운 물고기 297±87 mg/100 g[6]",
     "activity_ko": "통조림 곱사연어에서 가장 많은 포화지방산이었다[6]", "source": [6]},
    {"name": "Oleic acid", "name_ko": "올레산", "class": "단일불포화지방산(ω-9)", "role": "nutrient", "part": "통조림; 부산물 살",
     "content_text": "밝은 물고기 무첨가 통조림 436±77 mg/100 g[6]; 부산물 살 1.84±0.05 g/100 g(원문 표기)[7]",
     "activity_ko": "통조림에서 가장 많은 단일불포화지방산이었다[6]", "source": [6, 7]},
    {"name": "Cetoleic acid", "name_ko": "세톨레산(22:1n-11)", "class": "단일불포화지방산", "role": "nutrient", "part": "통조림",
     "content_text": "밝은 물고기 무첨가 통조림 424±116 mg/100 g, 어두운 물고기 181±73 mg/100 g[6]",
     "activity_ko": "먹이에서 오는 지방산으로, 산란을 앞두고 먹이 섭취가 줄어든 어두운 물고기에서 낮았다[6]", "source": [6]},
    {"name": "Gadoleic acid", "name_ko": "가돌레산(20:1n-11)", "class": "단일불포화지방산", "role": "nutrient", "part": "통조림",
     "content_text": "밝은 물고기 무첨가 통조림 392±130 mg/100 g, 어두운 물고기 144±49 mg/100 g[6]",
     "activity_ko": "세톨레산과 함께 먹이 섭취 정도를 반영하는 지방산으로 해석되었다[6]", "source": [6]},
    {"name": "Myristic acid", "name_ko": "미리스트산", "class": "포화지방산", "role": "nutrient", "part": "통조림",
     "content_text": "밝은 물고기 무첨가 통조림 203±45 mg/100 g, 어두운 물고기 85±24 mg/100 g[6]",
     "activity_ko": "부산물 살에서도 팔미트산 다음으로 많은 포화지방산이었다[7]", "source": [6, 7]},
    {"name": "Leucine", "name_ko": "류신", "class": "필수아미노산", "role": "nutrient", "part": "부산물 살(건물 기준)",
     "content_text": "5.01±0.01 g/100 g(건물), 분지사슬아미노산 합계 11.27 g/100 g[7]",
     "activity_ko": "부산물 살 필수아미노산 가운데 가장 많았다[7]", "source": [7]},
    {"name": "Lysine", "name_ko": "라이신", "class": "필수아미노산", "role": "nutrient", "part": "부산물 살(건물 기준)",
     "content_text": "5.81 g/100 g(건물)[7]",
     "activity_ko": "FAO/WHO 기준 패턴을 넘는 수준으로 보고되었다[7]", "source": [7]},
    {"name": "Glutamic acid", "name_ko": "글루탐산", "class": "아미노산", "role": "nutrient", "part": "부산물 살(건물 기준)",
     "content_text": "17종 아미노산 중 가장 많음(총아미노산 61.70±0.19 g/100 g 건물), 개별 수치는 본문에서 확인하지 못함[7]",
     "activity_ko": "감칠맛과 단백질 용해성에 기여하는 것으로 해석되었다[7]", "source": [7]},
    {"name": "Selenium", "name_ko": "셀레늄", "class": "무기질", "role": "nutrient", "part": "살",
     "content_text": "셀레늄/수은 몰비 71.1(조사 7종 중 최고)[14]",
     "activity_ko": "몰비가 1보다 크면 수은 독성을 막는 쪽으로 작용하는 것으로 해석된다[14]", "source": [14]},
    {"name": "Mercury", "name_ko": "수은", "class": "중금속(오염물질)", "role": "marker", "part": "살",
     "content_text": "브리티시컬럼비아 야생 연어 5종(곱사연어 포함) 평균 총수은 0.013–0.077 μg/g[15]; 러시아 북극권 강꼬치고기의 1/3–1/4 수준[14]",
     "activity_ko": "캐나다 보건부 기준(0.5 μg/g)보다 낮았다[15]", "source": [14, 15]},
    {"name": "Ethanol", "name_ko": "에탄올", "class": "부패 대사물", "role": "marker", "part": "통조림",
     "content_text": "수치는 초록에서 확인하지 못함[10]",
     "activity_ko": "14 °C 보관 원료로 만든 통조림에서는 관능 평가와 잘 맞는 부패 지표였으나 1 °C 보관 원료에서는 맞지 않았다[10]", "source": [10]},
    {"name": "alpha-Tocopherol", "name_ko": "알파-토코페롤", "class": "비타민 E", "role": "bioactive", "part": "훈연한 머리에서 뽑은 기름",
     "content_text": "수치는 초록에서 확인하지 못함[11]",
     "activity_ko": "훈연 처리한 머리 기름이 날 머리 기름보다 많이 가지고 있어 산화 안정성과 관련된 것으로 보았다[11]", "source": [11]},
]

assays = [
    {"role": "literature", "compound": "Fatty acid methyl esters (EPA, DHA, 16:0, 18:1n-9 etc.)", "compound_ko": "지방산 조성(EPA·DHA 등)",
     "part": "통조림 곱사연어(살·뼈·껍질·국물 전체 균질물)",
     "content": "밝은 물고기 무첨가(B0) EPA 344±81, DHA 598±66 mg/100 g, EPA+DHA 0.9±0.1 g/100 g; 어두운 물고기(D0) EPA 179±54, DHA 354±117 mg/100 g, EPA+DHA 0.5±0.2 g/100 g(원문 표 2·3)[6]",
     "method": "GC-FID",
     "conditions": {"instrument": "가스크로마토그래프 Agilent 6850, 불꽃이온화검출기, 자동시료주입기", "column": "DB-23 모세관 칼럼 60 m × 0.25 mm i.d., 막 두께 0.25 μm",
                    "mobile_phase": "운반 기체 수소", "gradient": "140→180 °C(2 °C/분), 180→200 °C(2.5 °C/분), 200→210 °C(0.5 °C/분), 210→230 °C(10 °C/분), 총 50분",
                    "flow": "1.0 mL/min(정유량, 평균 선속도 30 cm/s)", "temp": "주입구 250 °C, 검출기 275 °C", "detection": "FID(보조 기체 N2 35 mL/min, 공기 450 mL/min, 수소 40 mL/min)",
                    "injection": "1 μL, split 50:1", "sample_prep": "동결건조 시료를 디클로로메탄으로 가속용매추출(ASE200, 1500 psi, 100 °C, 5분 3회) → 지질 20 mg을 Maxwell–Marmer 법으로 메틸에스터화",
                    "standard": "내부표준 트리코사노산 메틸에스터 1 mg; 피크 확인용 Supelco Marine Oil #1·#3, S189-19, 세균 지방산 메틸에스터 혼합물",
                    "linearity": "", "lod": "", "loq": "", "recovery": ""},
     "rationale": "자연산 곱사연어는 성숙·산란 회유에 따라 지질 함량이 크게 달라 통조림의 EPA·DHA 표시가 어렵기 때문에, 지방산 정량이 품질·영양 표시의 기준으로 쓰였다[6]. 전문(Methods) 확인 — 검출·정량한계·회수율은 본문에 없음[6].",
     "source": [6], "url": "https://doi.org/10.1002/fsn3.4", "source_kind": "paper"},
    {"role": "literature", "compound": "Fatty acid methyl esters (total fatty acids)", "compound_ko": "지방산 조성(부산물 살)",
     "part": "필레를 뜨고 남은 뼈·껍질에서 기계로 발라낸 살",
     "content": "SFA 5.56±0.02, MUFA 5.05±0.78, PUFA 10.72±0.13 g/100 g(원문 표기, 시료 지질 3.73%와 비교하면 기준이 분명하지 않음); n-3/n-6 1.34±0.06, AI 0.44, TI 0.18[7]",
     "method": "GC-FID",
     "conditions": {"instrument": "Shimadzu GC-2010 Plus, 불꽃이온화검출기", "column": "용융 실리카 모세관 칼럼 60 m × 0.25 mm i.d., 막 두께 0.25 μm(고정상 이름은 본문에 없음)",
                    "mobile_phase": "운반 기체 질소", "gradient": "130 °C → 230 °C(승온 속도는 본문에 없음)", "flow": "", "temp": "", "detection": "FID",
                    "injection": "", "sample_prep": "균질 시료 1 g에 10 mol/L KOH 0.7 mL·무수 메탄올 5.3 mL, 55 °C 1.5시간 알칼리 가수분해 → H2SO4 0.58 mL로 산 촉매 메틸화(55 °C 1.5시간) → n-헥산 3 mL 추출 후 여과",
                    "standard": "Sigma-Aldrich FAME 표준품과 머무름 시간 비교, 피크 면적 백분율로 상대 함량 계산", "linearity": "", "lod": "", "loq": "", "recovery": ""},
     "rationale": "가공 부산물을 식품 원료로 쓸 수 있는지 판단하려고 n-3/n-6 비와 동맥경화·혈전 지수를 지방산 조성에서 계산했다[7]. 전문(Methods) 확인 — 유속·주입 조건·검출한계·회수율은 본문에 없음[7].",
     "source": [7], "url": "https://doi.org/10.3390/foods15183259", "source_kind": "paper"},
    {"role": "literature", "compound": "Amino acids (acid hydrolysis)", "compound_ko": "아미노산 조성(부산물 살)",
     "part": "필레를 뜨고 남은 뼈·껍질에서 기계로 발라낸 살",
     "content": "총아미노산 61.70±0.19 g/100 g(건물), 류신 5.01±0.01 g/100 g, 라이신 5.81 g/100 g, 필수/총아미노산 45.82±0.08%[7]",
     "method": "자동 아미노산 분석기(이온교환)",
     "conditions": {"instrument": "Hitachi L-8800 자동 아미노산 분석기", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "",
                    "injection": "", "sample_prep": "6 mol/L HCl, 110 °C 24시간 가수분해 → 희석·감압 농축(40–50 °C) → pH 2.2 구연산나트륨 완충액에 녹여 0.2 μm 막 여과, −80 °C 보관; 트립토판은 알칼리 가수분해 후 비색법",
                    "standard": "Sigma-Aldrich 인증 표준품과 머무름 시간·피크 면적 비교", "linearity": "", "lod": "", "loq": "", "recovery": ""},
     "rationale": "부산물 살 단백질의 영양적 질(필수아미노산 비율)을 평가하는 지표로 쓰였다[7]. 전문(Methods) 확인 — 칼럼·용리 조건과 검출한계는 본문에 없음[7].",
     "source": [7], "url": "https://doi.org/10.3390/foods15183259", "source_kind": "paper"},
]

world = [
    {"country": "미국(알래스카)", "metric": "catch_t", "year": "2005–2009", "value": 175000, "unit": "t",
     "note": "곱사연어 연평균 어획량, 알래스카 연어 어획의 약 절반; 논문 서론이 알래스카 어류수렵부 자료를 인용한 값", "source": [6]},
]

d = {
    "slug": "oncorhynchus-gorbuscha",
    "name_ko": "곱사연어",
    "name_en": "Pink salmon",
    "scientific_name": "Oncorhynchus gorbuscha (Walbaum)",
    "aliases": ["곱사연어", "Pink salmon", "Humpback salmon"],
    "sections": sections,
    "compounds": compounds,
    "markers": [],
    "assays": assays,
    "nutrients": [],
    "production": [],
    "world": world,
    "gi": [],
    "orgs": [],
    "sources": sources,
}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in sections:
    print(s["key"], len(s["body"]))
