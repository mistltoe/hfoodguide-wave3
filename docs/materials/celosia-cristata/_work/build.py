import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
A = "2026-10-30"
def P(n, title, doi, pub):
    return {"n": n, "title": title, "url": "https://doi.org/" + doi, "publisher": pub, "accessed": A}
sources = [
 {"n": 1, "title": "식품원료 목록(식품안전나라 OpenAPI I1020) — 맨드라미·맨드라미꽃발효액 행", "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020)", "accessed": "2026-10-13"},
 P(2, "Celosia cristata Linn. flowers as a new source of nutraceuticals — a study on nutritional composition, chemical characterization and in-vitro antioxidant capacity (Heliyon 2020;6:e05792, PMC7779698, 전문 확인)", "10.1016/j.heliyon.2020.e05792", "Heliyon (Elsevier)"),
 P(3, "Stability enhancement of betalain pigment extracted from Celosia cristata L. flower through copigmentation and degradation kinetics during storage (Food Chem X 2025;27:102312, PMC11929098, 전문 확인)", "10.1016/j.fochx.2025.102312", "Food Chemistry: X (Elsevier)"),
 P(4, "Betalains of Celosia argentea (Phytochemistry 2001;58:159-165) — common cockscomb(C. argentea var. cristata) 꽃차례, 초록 확인", "10.1016/s0031-9422(01)00141-8", "Phytochemistry (Elsevier)"),
 P(5, "Study on betalains in Celosia cristata Linn. callus culture and identification of new malonylated amaranthins (J Agric Food Chem 2018;66:3870-3879), 초록 확인", "10.1021/acs.jafc.8b01014", "Journal of Agricultural and Food Chemistry (ACS)"),
 P(6, "Celosia cristata L.: A review of its traditional uses, phytochemistry, pharmacology, toxicology, and quality control (J Ethnopharmacol 2024;330:118325), 초록 확인", "10.1016/j.jep.2024.118325", "Journal of Ethnopharmacology (Elsevier)"),
 P(7, "Development of an HPTLC-MS method for the differentiation of Celosiae Semen: Celosia argentea versus Celosia cristata (Molecules 2025;30:2786, PMC12250623, 전문 확인)", "10.3390/molecules30132786", "Molecules (MDPI)"),
 P(8, "Genetic diversity and population structure of Celosia argentea and related species revealed by SRAP (Biochem Genet 2009;47:521-532), 초록 확인", "10.1007/s10528-009-9257-z", "Biochemical Genetics (Springer)"),
 P(9, "Precise identification of Celosia argentea seed and its five adulterants by multiple morphological and chemical means (J Pharm Biomed Anal 2022;215:114802), 초록 확인", "10.1016/j.jpba.2022.114802", "Journal of Pharmaceutical and Biomedical Analysis (Elsevier)"),
 P(10, "Plant regeneration and cellular behaviour studies in Celosia cristata grown in vivo and in vitro (ScientificWorldJournal 2012:359413, PMC3349137, 전문 확인)", "10.1100/2012/359413", "TheScientificWorldJournal (Hindawi)"),
 P(11, "Antioxidant activity and protective effect of extract of Celosia cristata L. flower on tert-butyl hydroperoxide-induced oxidative hepatotoxicity (Food Chem 2015;168:572-579), 초록 확인", "10.1016/j.foodchem.2014.07.106", "Food Chemistry (Elsevier)"),
 P(12, "Anti-obesity effects of Celosia cristata flower extract in vitro and in vivo (Biomed Pharmacother 2024;176:116799), 초록 확인", "10.1016/j.biopha.2024.116799", "Biomedicine & Pharmacotherapy (Elsevier)"),
 P(13, "Antinociceptive effect of methanol extract of Celosia cristata Linn. in mice (BMC Complement Altern Med 2016;16:400, PMC5075210, 전문 확인)", "10.1186/s12906-016-1393-5", "BMC Complementary and Alternative Medicine (BioMed Central)"),
 P(14, "Evaluation of three ornamental plants for phytoremediation of Pb-contaminated soil (Int J Phytoremediation 2013;15:299-306), 초록 확인", "10.1080/15226514.2012.694502", "International Journal of Phytoremediation (Taylor & Francis)"),
 P(15, "Screening ornamental plants to identify potential Cd hyperaccumulators for bioremediation (Ecotoxicol Environ Saf 2018), 초록 확인", "10.1016/j.ecoenv.2018.06.049", "Ecotoxicology and Environmental Safety (Elsevier)"),
 P(16, "Immunostimulatory activity of polysaccharides extracted from Celosia cristata flowers (Chem Biodivers 2021;18:e2100031), 초록 확인", "10.1002/cbdv.202100031", "Chemistry & Biodiversity (Wiley)"),
 P(17, "Cytotoxic coumaronochromones from the inflorescences of Celosia cristata (Nat Prod Res 2017;31:1886-1890), 초록 확인", "10.1080/14786419.2016.1263851", "Natural Product Research (Taylor & Francis)"),
 P(18, "Preparation, characterization and application of smart packaging films based on locust bean gum/polyvinyl alcohol blend and betacyanins from cockscomb (Celosia cristata L.) flower (Int J Biol Macromol 2021), 초록 확인", "10.1016/j.ijbiomac.2021.09.113", "International Journal of Biological Macromolecules (Elsevier)"),
 P(19, "A novel hepatoprotective saponin from Celosia cristata L. (Fitoterapia 2010;81:1246-1252) — 종자 사포닌, 초록 확인", "10.1016/j.fitote.2010.08.011", "Fitoterapia (Elsevier)"),
 P(20, "Phenolic, flavonoid and antioxidant capacities evaluation of Celosia cristata resulted from induced mutation using ethyl methane sulphonate (Pak J Biol Sci 2022;25:380-386), 초록 확인", "10.3923/pjbs.2022.380.386", "Pakistan Journal of Biological Sciences"),
 P(21, "Evaluating quality consistency of Celosiae Cristatae Flos by four dimensional fingerprints combined with antioxidant activity (Spectrochim Acta A 2025;336:125985), 초록 확인", "10.1016/j.saa.2025.125985", "Spectrochimica Acta Part A (Elsevier)"),
 P(22, "Purification and properties of growth stage-dependent antiviral proteins from the leaves of Celosia cristata (Plant Sci 2000;154:13-21), 초록 확인", "10.1016/s0168-9452(99)00192-2", "Plant Science (Elsevier)"),
 P(23, "The growth and duration of life of Celosia cristata seedlings at different temperatures (J Gen Physiol 1934;17:763-781), 초록 확인", "10.1085/jgp.17.6.763", "The Journal of General Physiology (Rockefeller University Press)"),
 P(24, "The complete chloroplast genome sequence of plumed cockscomb (Celosia argentea, Amaranthaceae) (Mitochondrial DNA B 2019;4:2123-2124), 초록 확인 — 근연종 자료", "10.1080/23802359.2019.1623128", "Mitochondrial DNA Part B (Taylor & Francis)"),
 P(25, "Comparative assessment of morphological, cytological, and photosynthetic characteristics of the induced octoploid and its tetraploid counterpart of Celosia argentea L. (BMC Plant Biol 2024;24:1227), 초록 확인 — 근연종 자료", "10.1186/s12870-024-05973-x", "BMC Plant Biology (BioMed Central)"),
 P(26, "Purification, characterization and immunomodulatory activity of a polysaccharide from Celosia cristata (Carbohydr Polym 2015;133:337-344) — 종자 다당, 초록 확인", "10.1016/j.carbpol.2015.06.093", "Carbohydrate Polymers (Elsevier)"),
]

S = {}
S["overview"] = """맨드라미(Celosia cristata L.)는 비름과(Amaranthaceae) 맨드라미속의 한해살이풀로, 영문명 cockscomb(닭 볏)이 가리키듯 화려한 꽃차례 때문에 정원에 관상용으로 심는다[1, 13]. 식약처 「식품원료 목록」에는 '맨드라미'와 '맨드라미꽃발효액' 두 행이 식품원료(A코드)·식물로 실려 있고, 학명은 Celosia cristata L. / Celosia argentea var. cristata (L.) Kuntze, 이명은 계관·계두, 영문명은 Common cockscomb로 적혀 있다[1]. 두 행 모두 사용 조건이 '사용가능'이고 사용가능부위는 '꽃'으로 정해져 있어, 식품에는 꽃(꽃차례)만 쓸 수 있다[1]. 2026-10-13에 받은 같은 목록 원자료에서 학명에 Celosia가 들어간 행은 이 두 행뿐이었고, 개맨드라미(C. argentea)나 그 씨앗(청상자)은 별도 행으로 확인하지 못함.

인도 카슈미르산 붉은 꽃은 생것 기준 수분 79.6 g/100 g, 탄수화물 9.80 g/100 g이었고 칼륨·칼슘·α-토코페롤이 상대적으로 많았다[2]. 꽃의 붉은색은 수용성 색소인 베탈레인(주로 아마란틴)에서 나온다[3, 4]. 꽃 추출물의 간 보호·항비만 같은 결과는 세포·동물 실험이며 사람 효과는 확인하지 못함. 이 종을 원재료로 하는 건강기능식품 고시형 원료는 확인하지 못함."""

S["history"] = """중국에서는 맨드라미를 1000년 넘게 약재로 써 왔고, 자궁 출혈·대하·위장 감염 같은 출혈성 질환에 처방했다고 2024년 종설은 정리했다[6]. 꽃의 약재 이름은 Celosiae Cristatae Flos이며, 지혈·이질 치료 성질이 있다고 소개된다[21]. 인도 카슈미르에서는 'Mawal'이라 부르는 붉은 꽃을 그늘에 말려 가루로 쓰고, 고기 국물(그레이비)에 붉은빛을 내는 천연 색소로도 넣는다[2]. 같은 논문은 아프리카·중국·인도네시아·인도 일부에서 잎과 꽃차례를 채소로 먹는다고 적었다[2]. 방글라데시에서는 'Moragphul'이라 부르며 정원에 심고, 꽃은 복통·코피·각혈·혈뇨에 썼다는 민간 기록이 인용되어 있다[13]. 다른 연구는 붉은 꽃차례가 채소와 중국 전통 약재로 쓰인다고 적었다[4].

원산지에 대해서는 한 조직배양 논문이 남아메리카 원산이라고 적었으나[10], 공식 식물지 자료로는 확인하지 못함. 우리나라에 들어온 시기와 전통 식용 기록은 확인하지 못함."""

S["biology"] = """맨드라미는 비름과에 속하는 한해살이 초본이며, 품종에 따라 붉은색·주황색·노란색 꽃차례를 만든다[4, 13]. 붉은색·노란색 꽃차례의 색소는 질소를 품은 수용성 베탈레인으로, 붉은 자주색 베타시아닌과 노란색 베타잔틴으로 나뉜다[3, 4]. 노랑·주황·빨강 꽃차례의 베탈레인 구성은 질적으로 같았고, 깃털맨드라미(C. argentea var. plumosa)의 구성과도 같았다[4]. 노란 꽃차례에는 도파민·3-메톡시티라민·(S)-트립토판이 베탈람산과 결합한 베타잔틴 세 가지가 들어 있었다[4].

어두운 무균 상태에서 키운 유묘의 배축 생장은 14.5–40.5 °C 범위에서 30 °C 부근이 가장 빨랐다[23]. 잎에서는 분자량 25·27 kDa인 항바이러스 당단백질(CCP-25·CCP-27)이 분리되었고, 그 농도는 개화 전과 개화 후에 달랐다[22]. 조직배양에서는 붉은 자주색 캘러스가 쉽게 생기고, MS 기본 배지에서 6주 만에 시험관 안 개화가 관찰되었다[10]."""

S["related_species"] = """식약처 목록은 맨드라미 학명을 Celosia cristata와 Celosia argentea var. cristata 두 가지로 함께 적고 있어, 맨드라미를 개맨드라미(C. argentea)의 변종으로 보는 견해가 있음을 보여 준다[1]. 한 논문은 개맨드라미가 맨드라미의 직접 조상이라는 연구들을 인용했다[7]. 그러나 식품원료 목록에는 개맨드라미가 별도 행으로 없고, 맨드라미도 사용가능부위가 꽃으로 한정된다[1].

개맨드라미 씨앗(청상자, Celosiae Argenteae Semen)만 한국 생약규격집(KHP)과 중국약전(2020)에 실려 있고, 맨드라미 씨앗은 공정서 약재가 아니지만 시장에서 청상자로 섞여 팔린다[7]. 맨드라미 씨앗은 투영 면적이 청상자의 2배 이상이며, HPTLC에서 celosin F는 청상자에서만, celosin H·I·J는 맨드라미 씨앗에서만 검출되었다[7]. 다른 연구는 트리테르페노이드 사포닌 20종을 확인하고 두 사포닌의 피크 면적비로 두 씨앗을 가렸다[9]. 중국 집단을 SRAP로 분석하면 개맨드라미 16집단과 맨드라미 6집단이 두 무리로 갈렸다[8]. 개맨드라미 연구(4배체 2n=36, 엽록체 유전체)는 이 종의 자료가 아니므로 따로 읽어야 한다[24, 25]."""

S["cultivation"] = """맨드라미는 세계 여러 곳에서 화려한 꽃차례를 보려고 기르는 관상식물이며, 카슈미르에서는 지역에서 재배한 꽃을 시장에서 구할 수 있다[2, 3]. 카슈미르 연구에서는 꽃을 10월(2018년)과 9월 수확기에 거두었다[2, 3]. 유묘 생장의 최적 온도는 생장 곡선에서 30.48 °C로 계산되었고, 관찰한 최대 생장도 30 °C였다[23].

조직배양으로는 MS 배지에 NAA 2.0 mg/L와 BAP 1.5 mg/L를 넣었을 때 재분화율이 가장 높았고, 줄기끝 절편의 반응이 가장 좋았다[10]. 메탄설폰산에틸(EMS)로 돌연변이를 유도한 M1 세대 12계통에서는 꽃·씨앗 시료의 총페놀이 건물 1 g당 11.73–18.06 mg GAE로 계통에 따라 달랐다[20]. 납으로 오염된 흙에서 키운 화분 시험에서 피라미드형 맨드라미(C. cristata pyramidalis) 지상부의 납 농도는 1000 mg/kg을 넘었다[14]. 카드뮴 오염 흙 시험에서는 맨드라미가 중간 정도의 내성을 보였다[15]. 우리나라 재배 면적·생산량 통계는 확인하지 못함."""

S["processing"] = """카슈미르에서는 씨앗을 털어 낸 꽃을 다발로 거꾸로 매달아 그늘에서 말린 뒤 가루로 만들어 쓴다[2]. 연구용 추출물은 말린 꽃 가루를 70% 에탄올로 실온·어둠에서 24시간씩 두 번 우려 만들었다[2]. 베탈레인 색소는 생꽃 30 g을 0.1% 소금물 300 mL에 넣고 옴 가열(131.0 V, 49 °C, 3.5분)로 뽑았다[3]. 이 추출액을 pH 3으로 맞춰 20–25 °C 어둠에서 90일 두면 처리구 평균 베탈레인이 140.31 mg/L에서 61.61 mg/L로 줄었다[3]. 아라비아검·펙틴·유청단백질 각 0.33%에 아스코르브산 0.05%, 칼슘 0.01%를 함께 넣은 처리가 색소와 색을 가장 잘 지켰다[3]. 저장 온도 4·20·40 °C 가운데 4 °C가 색소 보존에 가장 좋았다[3].

맨드라미 꽃 추출물을 8 wt% 넣은 포장 필름은 수증기 투과도가 가장 낮았고, 새우가 상하면 붉은 자주색에서 갈색·노란색으로 바뀌어 신선도 표시에 쓸 수 있었다[18]. 식약처 목록에는 꽃을 원료로 한 '맨드라미꽃발효액'도 별도 원료명으로 실려 있다[1]. 식약처 「식품 등의 생산실적」 건강기능식품 원료 목록에서 맨드라미 품목은 확인하지 못함."""

S["genetics"] = """맨드라미 뿌리끝 분열조직의 평균 염색체 수는 조직배양 조건에 따라 33.23–42.07개로 세어졌고, 저자들은 정상 시험관 묘의 값(36.05)이 기존 보고와 맞는다고 적었다[10]. 같은 연구에서 체세포 변이는 확인되지 않았다[10]. 개맨드라미는 4배체(2n=4x=36)로 보고되어 있어 맨드라미의 값과 비슷한 수준이다[10, 25].

SRAP 표지 10쌍으로 중국의 개맨드라미 16집단과 맨드라미 6집단을 분석하자 507개 띠 가운데 274개가 다형이었고, 특정 조각(M1E6)으로 두 종을 가를 수 있었다[8]. 잎의 항바이러스 단백질 CCP-25·CCP-27은 개화 전과 후에 농도가 달라, 생육 단계에 따라 발현이 바뀌는 것으로 보인다[22]. 엽록체 전체 유전체(153,474 bp, 유전자 123개)는 깃털맨드라미(C. argentea)에서 해독되었으며 맨드라미 자체의 핵·엽록체 유전체 해독 보고는 확인하지 못함[24]."""

S["safety"] = """식약처 「식품원료 목록」에서 맨드라미는 사용가능부위가 '꽃'인 사용가능 원료이므로, 씨앗·잎·줄기는 이 목록상 식품원료로 쓸 수 없다[1]. 맨드라미 씨앗은 약전 약재인 청상자와 혼동되어 유통되므로 씨앗을 식품이나 약재로 쓰지 않도록 주의해야 한다[7]. 씨앗에서 보고된 사포닌(cristatain, celosin A–D)과 다당(CP1-1)의 간 보호·면역 작용은 동물·세포 결과이며, 씨앗은 식품원료 사용 부위가 아니다[19, 26, 1]. 노란 꽃차례에서는 도파민 농도가 높게 측정되어, 연구진은 노란 꽃을 채소나 약재로 쓸 때 독성학적 의미가 있을 수 있다고 적었다[4]. 캘러스 연구도 도파민 함량을 꽃차례와 비교해 보고했다[5].

맨드라미 전초 메탄올 추출물을 생쥐에 1000–4000 mg/kg 한 번 먹였을 때 14일 동안 죽거나 이상 행동을 보인 개체가 없었다[13]. 꽃 추출물은 쥐에게 100·500 mg/kg을 5일 먹였을 때 간 손상 지표 상승을 줄였고, 고지방 사료 생쥐의 체중 증가를 줄였지만 모두 동물 결과다[11, 12]. 사람 임상시험, 알레르기 보고, 장기 섭취 안전성은 확인하지 못함. 납 오염 흙에서 자란 맨드라미 지상부에 납이 1000 mg/kg 넘게 쌓인 시험이 있어, 오염 우려가 있는 곳에서 자란 꽃은 먹지 않는 것이 좋다[14]. 이 종에 대한 건강기능식품 고시 섭취 주의사항은 확인하지 못함."""

titles = {"overview":"개요","history":"이용의 역사","biology":"식물학적 특징","related_species":"근연종과 구별","cultivation":"재배와 산지","processing":"가공과 이용","genetics":"유전과 육종","safety":"안전성"}
sections = [{"key":k, "title":titles[k], "body":S[k]} for k in ["overview","history","biology","related_species","cultivation","processing","genetics","safety"]]

def C(name, ko, cls, role, part, content, act, src):
    return {"name":name,"name_ko":ko,"class":cls,"role":role,"part":part,"content_text":content,"activity_ko":act,"source":src}
compounds = [
 C("Amaranthin","아마란틴","베타시아닌(베탈레인)","marker","꽃차례; 캘러스","정량값 없음(꽃차례); 캘러스에서 가장 많은 베타시아닌[4, 5]","꽃의 붉은 자주색을 내는 주 색소[4, 5]",[4,5]),
 C("Betalains","베탈레인(총)","베탈레인 색소","marker","생꽃 옴 가열 추출액","처리구 평균 140.31 mg/L(저장 0일) → 61.61 mg/L(90일, 20–25 °C)[3]","저장 중 분해는 1차 반응을 따랐고 4 °C 저장에서 가장 안정[3]",[3]),
 C("Celoscristatin","셀로스크리스타틴(6'-O-말로닐아마란틴)","아실화 베타시아닌","bioactive","캘러스","정량값 없음; 캘러스에서 두 번째로 많은 베타시아닌[5]","캘러스에서 새로 확인된 말로닐 유도체[5]",[5]),
 C("Betanin","베타닌","베타시아닌","bioactive","캘러스","정량값 없음[5]","캘러스의 부(副) 베타시아닌[5]",[5]),
 C("Dopamine","도파민","카테콜아민","bioactive","노란 꽃차례; 캘러스","정량값 없음(초록 확인); 노란 꽃차례에서 높은 농도[4]","연구진은 노란 꽃을 먹을 때 독성학적 의미가 있을 수 있다고 지적[4, 5]",[4,5]),
 C("Miraxanthin V","미라잔틴 V(도파민-베타잔틴)","베타잔틴","bioactive","노란 꽃차례; 캘러스","정량값 없음; 캘러스의 주 베타잔틴[4, 5]","노란색 색소[4, 5]",[4,5]),
 C("alpha-Tocopherol","알파-토코페롤(비타민 E)","지용성 비타민","nutrient","꽃(카슈미르 붉은 꽃차례)","455.00 μg/100 g(기준 생/건 명시 없음)[2]","측정한 비타민 가운데 가장 많음[2]",[2]),
 C("Ascorbic acid","비타민 C","수용성 비타민","nutrient","꽃(카슈미르 붉은 꽃차례)","4.3 mg/100 g[2]","다른 식용꽃보다 매우 낮다고 저자들이 평가[2]",[2]),
 C("Potassium","칼륨","무기질","nutrient","꽃(카슈미르 붉은 꽃차례)","520.45 mg/100 g; 칼슘 128.68, 마그네슘 76.40, 철 9.45 mg/100 g(기준 생/건 명시 없음)[2]","측정한 무기질 가운데 가장 많음[2]",[2]),
 C("Linoleic acid","리놀레산","오메가-6 다불포화지방산","nutrient","꽃(카슈미르 붉은 꽃차례)","2.02 g/100 g; 팔미트산 1.3, 올레산 0.89 g/100 g(원문 단위, 기준 명시 없음)[2]","가장 많은 다불포화지방산[2]",[2]),
 C("L-Tryptophan","트립토판","필수아미노산","nutrient","생꽃","26.29 mg/100 g; 아르기닌 22.43, 트레오닌 19.08, 메티오닌 0.79 mg/100 g[2]","측정한 필수아미노산 가운데 가장 많음[2]",[2]),
 C("Cristatone II","크리스타톤 II","쿠마로노크로몬","bioactive","꽃차례","정량값 없음[17]","HeLa·BGC-823 암세포에 IC50 23.82 μM(세포 실험)[17]",[17]),
 C("Pectic polysaccharide (galacturonic acid-rich)","꽃 다당(갈락투론산·포도당 위주)","다당류","bioactive","꽃","정량값 없음[16]","생쥐 대식세포의 iNOS·COX-2·사이토카인 생성 증가(세포 실험)[16]",[16]),
 C("Total phenolics","총페놀","페놀 화합물(합계)","bioactive","말린 꽃 70% 에탄올 추출물","47.29 mg GAE/g(추출물)[2]; EMS 돌연변이 계통 꽃·씨앗 11.73–18.06 mg GAE/g 건물[20]","DPPH 라디칼 소거 68.7–79.9%(100–1000 μg/mL)[2]",[2,20]),
 C("Celosin H","셀로신 H","트리테르페노이드 사포닌","bioactive","씨앗(식품 사용 부위 아님)","정량값 없음[7]","HPTLC에서 맨드라미 씨앗에서만 검출되어 청상자와 구별 표지로 제안[7]",[7]),
]
nutrients = [{"form":"생꽃(인도 카슈미르산 붉은 꽃차례)","basis":"생것 100 g","items":[{"name":"수분","value":79.6,"unit":"g"},{"name":"탄수화물","value":9.80,"unit":"g"}],"source":[2]}]

assays = [
 {"role":"literature","compound":"Betalains (betacyanins, betaxanthins)","compound_ko":"베탈레인(베타시아닌·베타잔틴)","part":"생꽃(꽃잎) 추출액",
  "content":"처리구 평균 140.31 mg/L(0일) → 61.61 mg/L(90일)[3]","method":"UV-Vis 분광광도법",
  "conditions":{"instrument":"Shimadzu 1900 분광광도계","column":"","mobile_phase":"","gradient":"","flow":"","temp":"","detection":"베타시아닌 542 nm, 베타잔틴 480 nm; 몰흡광계수 60,000·48,000 L/mol·cm, 분자량 550·308 g/mol, 광로 1 cm","injection":"","sample_prep":"생꽃 30 g + 0.1% NaCl 증류수 300 mL, 옴 가열 추출(131.0 V, 49 °C, 3.5분); 인산 완충액(pH 6.5)으로 희석","standard":"","linearity":"","lod":"","loq":"","recovery":""},
  "rationale":"맨드라미 꽃의 붉은색을 내는 수용성 색소로, 색소 원료·저장 안정성 평가의 지표로 쓰였다(전문 확인)[3]","source":[3],"url":"https://doi.org/10.1016/j.fochx.2025.102312","source_kind":"paper"},
 {"role":"literature","compound":"alpha-Tocopherol (retinol 동시 분석)","compound_ko":"알파-토코페롤(비타민 E)","part":"꽃(카슈미르 붉은 꽃차례)",
  "content":"455.00 μg/100 g; 레티놀 11.95 μg/100 g[2]","method":"HPLC-DAD",
  "conditions":{"instrument":"Agilent 1260 Infinity, 다이오드 어레이 검출기","column":"C18 (4.6 mm × 250 mm, 5 μm)","mobile_phase":"메탄올:물 = 96:4","gradient":"","flow":"","temp":"","detection":"DAD(파장 원문 미기재)","injection":"20 μL; 분석 시간 14분","sample_prep":"50% 에탄올성 KOH + 피로갈롤로 1시간 환류 비누화 → 식힌 뒤 THF:물(1:1) 넣고 실온 24시간","standard":"","linearity":"","lod":"","loq":"","recovery":""},
  "rationale":"꽃에서 측정한 비타민 가운데 가장 많아 항산화 영양 성분의 지표로 제시되었다(전문 확인)[2]","source":[2],"url":"https://doi.org/10.1016/j.heliyon.2020.e05792","source_kind":"paper"},
 {"role":"literature","compound":"Amino acids (FMOC derivatives)","compound_ko":"아미노산 조성(트립토판 등)","part":"생꽃",
  "content":"트립토판 26.29, 아르기닌 22.43, 트레오닌 19.08, 메티오닌 0.79 mg/100 g[2]","method":"HPLC-DAD(FMOC-Cl 유도체화)",
  "conditions":{"instrument":"Agilent 1260 Infinity HPLC, DAD","column":"C18 (4.6 mm × 250 mm, 5 μm), 같은 충전제 가드 칼럼(Merck)","mobile_phase":"A: 아세토니트릴:물(90:10), B: 50 mM 아세트산나트륨","gradient":"","flow":"1 mL/min","temp":"","detection":"263 nm","injection":"","sample_prep":"FMOC-Cl(9-플루오레닐메틸클로로포메이트)로 유도체화","standard":"","linearity":"","lod":"","loq":"","recovery":""},
  "rationale":"꽃의 단백질 영양 평가용으로 필수아미노산 10종과 비필수 2종을 정량했다(전문 확인)[2]","source":[2],"url":"https://doi.org/10.1016/j.heliyon.2020.e05792","source_kind":"paper"},
]

d = {"slug":"celosia-cristata","name_ko":"맨드라미","name_en":"Common cockscomb","scientific_name":"Celosia cristata L. (이명 Celosia argentea var. cristata (L.) Kuntze)",
 "aliases":["계관","계두","맨드라미꽃","cockscomb","Celosia argentea var. cristata","Celosiae Cristatae Flos"],
 "sections":sections,"compounds":compounds,"markers":[],"nutrients":nutrients,"assays":assays,"production":[],"world":[],"gi":[],"orgs":[],"sources":sources}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in sections: print(s["key"], len(s["body"]))
