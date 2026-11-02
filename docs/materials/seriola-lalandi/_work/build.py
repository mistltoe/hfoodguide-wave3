import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
A = "2026-11-02"
def P(n, title, doi, pub):
    return {"n": n, "title": title, "url": f"https://doi.org/{doi}", "publisher": pub, "accessed": A}
sources = [
 {"n": 1, "title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — Seriola lalandi 행(부시리, Yellowtail amberjack, 수산물, 부위 '-', 사용가능, 사용 조건 없음, 고시형 원료 원재료 목록 없음; 같은 속 방어 Seriola quinqueradiata·잿방어 Seriola dumerili·낫잿방어 Seriola rivoliana는 별도 행; data/raw/mfds_rawmtrl/I1020_20261013.json, docs/materials/seriola-lalandi/card.json)", "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
 P(2, "Metabolism of Seriola lalandi during Starvation as Revealed by Fatty Acid Analysis and Compound-Specific Analysis of Stable Isotopes within Amino Acids. PLoS One 2017;12(1):e0170124 (PMC 전문 확인)", "10.1371/journal.pone.0170124", "PLoS One, PMC5240982"),
 P(3, "Management of Sexual Maturation and Natural Spawning of Captive-Reared Yellowtail Kingfish, Seriola lalandi, in an Indoor Rearing Tank. Dev Reprod 2016;20(2):141-7 (PMC 전문 확인)", "10.12717/DR.2016.20.2.141", "Development & Reproduction, PMC5027219"),
 P(4, "Genomic mechanisms of life history divergence shaped by demography and selection in the yellowtail kingfish species complex. Mar Genomics 2026;87:101265 (초록 확인)", "10.1016/j.margen.2026.101265", "Marine Genomics (PubMed 42468076)"),
 P(5, "The chromosome-level genome assembly of the Japanese yellowtail jack Seriola aureovittata provides insights into genome evolution and efficient oxygen transport. Mol Ecol Resour 2022;22(7):2701-2712 (초록 확인)", "10.1111/1755-0998.13648", "Molecular Ecology Resources (PubMed 35593537)"),
 P(6, "A Chromosome-Level Genome Assembly of Yellowtail Kingfish (Seriola lalandi). Front Genet 2022;12:825742 (초록 확인)", "10.3389/fgene.2021.825742", "Frontiers in Genetics, PMC8807568"),
 P(7, "The Complete Chromosome-Level Genome and Mitogenome Assembly of Seriola lalandi (Yellowtail Kingfish) for Aquaculture and Fisheries Management. Ecol Evol 2026;16(10):e74430 (초록 확인)", "10.1002/ece3.74430", "Ecology and Evolution, PMC13654616"),
 P(8, "Population Genetics of Seriola lalandi Confirm Hemispheric Divergence and Reveal Genetic Structure in the Temperate Northern Pacific and Between Wild and Captive-Reared Fish. Ecol Evol 2026;16(8):e74200 (초록 확인)", "10.1002/ece3.74200", "Ecology and Evolution, PMC13491388"),
 P(9, "Shallow seamounts represent speciation islands for circumglobal yellowtail Seriola lalandi. Sci Rep 2021;11(1):3559 (초록 확인)", "10.1038/s41598-021-82501-z", "Scientific Reports, PMC7878507"),
 P(10, "Structural characterization of carangid fish myoglobins. Fish Physiol Biochem 2012;38(5):1311-22 (초록 확인)", "10.1007/s10695-012-9619-z", "Fish Physiology and Biochemistry (PubMed 22361749)"),
 P(11, "Australian farmed Yellowtail Kingfish (Seriola lalandi) and Mulloway (Argyrosomus hololepidotus): residues of metallic, agricultural and veterinary chemicals, dioxins and polychlorinated biphenyls. Chemosphere 2011;86(7):709-17 (초록 확인)", "10.1016/j.chemosphere.2011.10.044", "Chemosphere (PubMed 22142628)"),
 P(12, "Metal concentrations and toxicity in South African snoek (Thyrsites atun) and yellowtail (Seriola lalandi). Mar Pollut Bull 2017;122(1-2):360-365 (초록 확인)", "10.1016/j.marpolbul.2017.06.074", "Marine Pollution Bulletin (PubMed 28676172)"),
 P(13, "Benzo[a]pyrene and Benzo[k]fluoranthene in some processed fish and fish products. Int J Environ Res Public Health 2015;12(1):940-51 (초록 확인)", "10.3390/ijerph120100940", "IJERPH, PMC4306903"),
 P(14, "Not all infected fish become mushy: phenotypic expression underestimates Unicapsula seriolae infection in yellowtail kingfish (Seriola lalandi). Parasitol Res 2026;125(1) (초록 확인)", "10.1007/s00436-026-08735-w", "Parasitology Research, PMC13690875"),
 P(15, "Fish protein hydrolysates: application in deep-fried food and food safety analysis. J Food Sci 2015;80(1):E108-15 (초록 확인)", "10.1111/1750-3841.12684", "Journal of Food Science (PubMed 25559171)"),
 P(16, "Quantitative genetic properties of four measures of deformity in yellowtail kingfish Seriola lalandi Valenciennes, 1833. J Fish Dis 2015;39(2):217-28 (초록 확인)", "10.1111/jfd.12348", "Journal of Fish Diseases (PubMed 25683477)"),
 P(17, "Dietary fish oil replacement with canola oil up-regulates glutathione peroxidase 1 gene expression in yellowtail kingfish (Seriola lalandi). Comp Biochem Physiol B 2012 (초록 확인)", "10.1016/j.cbpb.2012.04.002", "Comparative Biochemistry and Physiology Part B (PubMed 22521527)"),
 P(18, "Effects of temperature on fecundity in vitro, egg hatching and reproductive development of Benedenia seriolae and Zeuxapta seriolae (Monogenea) parasitic on yellowtail kingfish Seriola lalandi. Int J Parasitol 2005;35(3):315-27 (초록 확인)", "10.1016/j.ijpara.2004.11.008", "International Journal for Parasitology (PubMed 15722083)"),
 P(19, "Metazoan parasite assemblages of wild Seriola lalandi (Carangidae) from eastern and southern Australia. Parasitol Int 2007;56(2):95-105 (초록 확인)", "10.1016/j.parint.2006.12.003", "Parasitology International (PubMed 17267264)"),
 P(20, "Genetics and Genomics of Infectious Diseases in Key Aquaculture Species. Biology (Basel) 2024;13(1):29 (초록 확인)", "10.3390/biology13010029", "Biology (MDPI), PMC10813283"),
 P(21, "Sustainable Fishmeal Alternatives: Impact of Partially Defatted Black Soldier Fly (Hermetia illucens) Meal on Growth and Health of Yellowtail Kingfish (Seriola lalandi). Aquac Nutr 2025:1804215 (초록 확인)", "10.1155/anu/1804215", "Aquaculture Nutrition, PMC12202081"),
 P(22, "Exploring single cell microbial protein as a sustainable fishmeal alternative in yellowtail kingfish (Seriola lalandi) diets: impacts on health and gut microbiome. J Anim Sci Biotechnol 2025;16:? (초록 확인)", "10.1186/s40104-024-01146-w", "Journal of Animal Science and Biotechnology, PMC11787759"),
 P(23, "Seasonal expression of reproductive axis-related neuroendocrine genes and their relation with ovarian maturation in captive yellowtail kingfish (Seriola lalandi). Biol Res 2025;58(1):55 (초록 확인)", "10.1186/s40659-025-00622-5", "Biological Research, PMC12333068"),
 P(24, "Molecular Characterization of Embryos with Different Buoyancy Levels in the Yellowtail Kingfish (Seriola lalandi). Animals 2022;12(6):720 (초록 확인)", "10.3390/ani12060720", "Animals (MDPI), PMC8944698"),
 P(25, "Improving consumption rate estimates by incorporating wild activity into a bioenergetics model. Ecol Evol 2016;6(8):2262-74 (초록 확인)", "10.1002/ece3.2027", "Ecology and Evolution, PMC4782250"),
 P(26, "Disrupted flow sensing impairs hydrodynamic performance and increases the metabolic cost of swimming in the yellowtail kingfish, Seriola lalandi. J Exp Biol 2012 (초록 확인)", "10.1242/jeb.073437", "Journal of Experimental Biology (PubMed 22899528)"),
 P(27, "Transcriptional profiles reveal physiological mechanisms for compensation during a simulated marine heatwave in Yellowtail Kingfish (Seriola lalandi). BMC Genomics 2025;26(1):230 (초록 확인)", "10.1186/s12864-025-11283-9", "BMC Genomics, PMC11895300"),
 P(28, "Structure and composition of yellowtail kingfish (Seriola lalandi) otoliths: implications for using aquaculture-reared fish to reconstruct life histories. J Fish Biol 2025;107(4):1188-1200 (초록 확인)", "10.1111/jfb.70110", "Journal of Fish Biology, PMC12536058"),
 P(29, "The Microbiome of Seriola lalandi of Wild and Aquaculture Origin Reveals Differences in Composition and Potential Function. Front Microbiol 2017;8:1844 (초록 확인)", "10.3389/fmicb.2017.01844", "Frontiers in Microbiology, PMC5622978"),
 P(30, "A comprehensive transcriptome of early development in yellowtail kingfish (Seriola lalandi). Mol Ecol Resour 2015 (초록 확인)", "10.1111/1755-0998.12451", "Molecular Ecology Resources (PubMed 26230659)"),
 P(31, "Effects of dietary choline on liver lipid composition, liver histology and plasma biochemistry of juvenile yellowtail kingfish (Seriola lalandi). Br J Nutr 2021;125(12):1344-1358 (초록 확인)", "10.1017/S0007114520003669", "British Journal of Nutrition (PubMed 32943119)"),
 P(32, "Yellowtail kingfish Seriola aureovittata farmed in offshore net cage response to high density by regulating protein and glucose metabolism. Fish Physiol Biochem 2025 (초록 확인)", "10.1007/s10695-025-01556-1", "Fish Physiology and Biochemistry (PubMed 40810976)"),
 P(33, "Australian seafood compositional profiles: A pilot study. Vitamin D and mercury content. Food Chem 2015;193:106-11 (초록 확인)", "10.1016/j.foodchem.2014.11.057", "Food Chemistry (PubMed 26433295)"),
]
sources[21]["title"] = sources[21]["title"].replace("2025;16:? ", "2025 ")

S = {}
S["overview"] = ("한눈에 보기",
"부시리(Seriola lalandi)는 전갱이과(Carangidae) 방어속(Seriola)에 드는 바닷물고기로, 식약처 「식품원료 목록」에 '부시리'(영문 Yellowtail amberjack)라는 원료명의 수산물로 올라 있다[1]. 이 목록에서 상태는 '사용가능'이고, 사용 부위는 따로 정하지 않은 '-'로 적혀 있으며 별도의 사용 조건은 없다[1]. 같은 속의 방어·잿방어·낫잿방어는 목록에서 각각 다른 원료로 올라 있고, 이 문서는 부시리 자료만 다룬다[1]. 건강기능식품 고시형 원료의 원재료 목록에는 없어 식약처가 정한 지표성분도 없다[1].\n\n"
"영어로는 yellowtail kingfish로 널리 불리며, 몸집이 크고 빨리 헤엄치며 빨리 자라고 경제적 가치가 높아 외해 양식에 알맞은 종으로 소개된다[6]. 사료를 먹인 어린 개체의 근육 지방산에서는 DHA가 총 지방산의 약 14.8%, EPA가 약 6.4%로 보고되었다[2]. 오스트레일리아 수산물 성분 시범 조사에서도 양식 부시리가 분석 대상에 들었으나, 초록에는 부시리 개별 값이 없다[33]. 국내 공공기관의 부시리 식품성분표 값과 국내 생산 통계는 이번 조사에서 확인하지 못함.")
S["history"] = ("이용·연구 역사",
"한국 연안에는 부시리·방어·잿방어 세 종의 방어속 어류가 살며, 부시리는 일본·중국을 포함한 전 세계 온대 바다에도 분포한다고 소개되었다[3]. 부시리는 일본에서 양식되고, 오스트레일리아·뉴질랜드와 미국 캘리포니아에서도 양식된다고 적혔다[3]. 국내 방어속 양식은 자연산 치어를 잡아 기르는 방식에 머물러 있어, 어미 관리와 종자 생산 체계를 갖출 필요가 있다고 지적되었다[3].\n\n"
"제주 연안에서 잡은 부시리 59마리를 실내 수조(100 m³)에서 기르며 빛 주기를 조절해 2014년 5–6월 자연 산란을 받아낸 연구가 국내 첫 실내 수조 수정란 생산 사례로 보고되었다[3]. 칠레에서는 부시리를 양식 품종 다변화의 핵심 종으로 보고 번식 생리 연구를 이어 가고 있다[23]. 오스트레일리아에서는 상업·여가 낚시의 주요 어종이며 양식 회사의 계통 집단으로 기형·필레 형질의 유전율을 추정한 연구도 나왔다[14, 16]. 국내에서 부시리를 먹어 온 역사를 다룬 공공기관 자료는 확인하지 못함.")
S["biology"] = ("어종·형태·생태",
"부시리는 전 지구의 온대·아열대 바다 표층에 사는 육식성 회유어로 소개된다[6, 30]. 몸통을 따라 무산소성 백색근과 유산소성 적색·분홍색 근섬유가 분포하는, 활동적인 외양성 어류의 전형적인 근육 구조를 가진다[26]. 표준 대사율과 최적 유영 속도가 비교적 높아 운동 능력이 뛰어난 종으로 평가된다[26]. 야생 개체의 하루 먹이 소비량은 가속도 발신기로 잰 활동량을 넣어 체중 1 g당 하루 152 J로 추정되었다[25].\n\n"
"부시리는 봄–여름 산란어로, 제주산 어미는 수온 17.0 °C인 5월 3일 산란을 시작해 20.5 °C인 6월 중순까지 26회 산란했다[3]. 수정란 지름은 1.388 ± 0.041 mm였고 기름방울 하나를 가진 부성란이었다[3]. 칠레에서 기른 암컷의 생식 관련 유전자 발현은 겨울에 가장 높아 야생 집단과 비슷한 계절 번식 양상을 보였다[23]. 야생 개체의 이석에서 바륨·망간이 검출한계 아래여서 하구·기수역을 산란장으로 쓰지 않는 것으로 해석되었다[28].")
S["related_species"] = ("관련 종·이름",
"식약처 목록은 부시리(Seriola lalandi)를 방어(Seriola quinqueradiata), 잿방어(Seriola dumerili), 낫잿방어(Seriola rivoliana)와 다른 원료로 구분한다[1]. 최근 유전체 연구는 이른바 yellowtail kingfish를 북동태평양의 Seriola dorsalis, 북서태평양의 Seriola aureovittata, 그리고 남태평양·남아프리카의 두 계통으로 이루어진 Seriola lalandi로 나누는 종 복합체로 본다[4]. 중국 연구진은 북서태평양 집단을 Seriola aureovittata로 부르며 염색체 수준 유전체를 따로 해독했다[5, 32]. 따라서 한국 연안 부시리가 학술적으로 어느 학명에 해당하는지는 문헌에 따라 다르며, 국내 연구(2016)는 제주산 개체를 Seriola lalandi로 적었다[3].\n\n"
"멕시코–미국 북태평양 집단과 칠레 집단은 뚜렷이 갈라진 두 진화 계통이라는 결과도 있다[8]. 남아프리카 연안과 두 해산(Vema, Walters Shoal)의 부시리도 유전·형질이 서로 다른 번식 집단으로 보고되었다[9]. 미오글로빈 아미노산 서열은 방어·잿방어·부시리를 포함한 전갱이과 다섯 종 사이에서 81–99% 일치했다[10].")
S["cultivation"] = ("양식·어획",
"오스트레일리아·뉴질랜드의 해상 가두리 부시리 양식에서는 단생 흡충류 기생충(Benedenia seriolae, Zeuxapta seriolae)이 큰 손실을 일으키는 문제로 꼽힌다[18]. 오스트레일리아 동·남부 야생 부시리에서는 기생충 43개 분류군이 확인되었고, 그중 4종은 방어속 양식에서 질병·폐사와 관련된 적이 있는 종이었다[19]. 이 두 기생충은 수온이 낮을수록 부화와 성숙이 늦어져, 수온에 맞춘 구제 시기 조절이 제안되었다[18]. 피부 흡충 저항성은 유전되는 형질로, 선발 육종으로 세대당 평균 약 10%의 유전적 개량을 얻었다고 정리되었다[20].\n\n"
"어분을 줄이는 사료 연구에서 동애등에 유충박으로 어분의 25–50%를 바꾸어도 성장과 사료 효율이 대조구와 비슷했지만 75%에서는 섭식이 줄어 성장이 떨어졌다[21]. 메탄 자화 세균 단세포 단백질로 어분을 대체한 시험도 건강·장내 미생물 영향을 기준으로 평가되었다[22]. 어유의 일부(50%)를 가금유로 바꾸면 성장이 좋아졌으나 카놀라유로 모두 바꾸면 항산화 유전자 발현이 달라졌다[17]. 콜린이 모자란 사료는 어린 부시리의 간 조직과 혈장 지표에 영향을 주었다[31]. 집약 양식에서는 질병과 영양 결핍으로 폐사가 많았다고 정리되었고, 야생과 양식 개체의 장내 미생물 조성도 달랐다[29]. 종자 생산에서는 배아의 부력 저하가 발생 실패와 관련되며, 유리아미노산 함량이 부력을 가르는 요인으로 제시되었다[24]. 국내 부시리 양식·어획량 통계는 이번 조사에서 확인하지 못함.")
S["processing"] = ("가공·저장·품질",
"양식 육종에서는 필레 무게·수율과 필레 지방 함량이 부시리의 살 품질 형질로 기록된다[16]. 35일 굶긴 어린 부시리는 근육 지질이 56% 줄었지만 DHA 등 고도불포화지방산은 상대적으로 보존되어, 근육 지방산 조성이 먹이 상태에 따라 크게 달라졌다[2]. 오스트레일리아 동해안에서는 조리 뒤 살이 무르는 '머시(mushy) 살' 현상이 보고되었고, 낚시 개체의 38.9%에서 점액포자충 Unicapsula seriolae가 확인되었다[14]. 감염 개체의 71.4%는 겉보기에 살이 무르지 않아 눈으로만 골라내면 감염 개체가 유통될 수 있다고 지적되었다[14].\n\n"
"부시리 부산물로 만든 어육 단백질 가수분해물은 튀김 반죽·어묵의 흡유량을 줄였지만, 히스타민 함량이 높아 식품 배합에 10% 이하로만 쓸 수 있다고 했다[15]. 남아프리카에서 산 부시리 필레를 튀기거나 굽거나 삶았을 때 벤조[a]피렌과 벤조[k]플루오란텐 합계는 네 어종 전체에서 0.56–1.46 µg/kg이었고 튀김에서 가장 높았다[13]. 식품의약품안전처의 「식품 등의 생산실적」에서 부시리 품목은 확인하지 못함.")
S["genetics"] = ("유전 정보",
"부시리의 염색체 수준 기준 유전체는 크기 648.34 Mb로 24개 염색체에 고정되었고, 후각 수용체와 HSP70 유전자군이 확장되어 있었다[6]. 뉴질랜드 집단의 유전체는 644 Mb로 조립되어 단백질 암호 유전자 24,600개가 주석되었고 미토콘드리아 유전체도 완성되었다[7]. 남아프리카 집단의 기준 유전체는 678.3 Mb에 단백질 암호 유전자 21,796개로 보고되었다[4]. 북서태평양 집단(Seriola aureovittata)의 유전체 649.86 Mb에서는 지방산 대사와 산소 결합·운반 관련 유전자가 늘어나 있었다[5].\n\n"
"칠레·멕시코에서는 양식 어미 집단이 야생 집단과 유전적으로 구별되어 지역별 관리가 필요하다고 했다[8]. 기형 형질의 유전율은 모형에 따라 0.01–0.66으로 추정되었고, 턱 기형은 체중·필레 무게와 높은 양의 유전 상관을 보였다[16]. 초기 발생 단계 전사체에서는 4만여 개 유전자와 정상·기형 자어 사이의 발현 차이가 정리되었다[30]. 해양 열파를 흉내 낸 고수온 노출에서는 근육의 미토콘드리아 관련 전사체가 크게 달라졌다[27].")
S["safety"] = ("안전성",
"식약처 「식품원료 목록」에서 부시리는 별도 조건 없이 '사용가능' 원료이며, 건강기능식품 고시형 원료가 아니어서 고시 섭취 시 주의사항은 없다[1]. 부시리를 따로 다룬 국내 공공기관의 알레르기·잔류물질 정보는 이번 조사에서 확인하지 못함.\n\n"
"오스트레일리아 양식 부시리 혼합 시료 27개의 수은 평균은 0.03 mg/kg(0.02–0.05)이었고, 농약과 항균제는 검출되지 않았다[11]. 같은 시료의 다이옥신은 평균 0.6 pg TEQ/g, 다이옥신과 다이옥신 유사 PCB 합계는 2.6 pg TEQ/g으로 오스트레일리아·일본·유럽연합 기준에 비해 낮았다[11]. 남아프리카 야생 부시리(37마리)의 평균 수은은 0.16 mg/kg, 비소 0.98 mg/kg, 카드뮴 0.004 mg/kg, 납 0.005 mg/kg으로 기준 안이었지만 수은·비소·아연은 몸집이 클수록 높았다[12]. 그 연구는 큰 개체(12–15 kg)도 성인이 일주일에 두 끼(150 g) 먹는 것은 안전하다고 보았다[12].\n\n"
"근육 점액포자충 Unicapsula seriolae는 사람에게 중요한 인수공통 기생충으로 보지 않지만, 일본에서는 다른 방어속 어류와 관련된 식중독 보고가 있어 식품안전 측면에서 살펴볼 필요가 있다고 했다[14]. 부시리 부산물 가수분해물의 높은 히스타민도 품질 관리 대상으로 지적되었다[15].")

sections = [{"key": k, "title": t, "body": b} for k, (t, b) in S.items()]

def fa(name, ko, cls, content, act):
    return {"name": name, "name_ko": ko, "class": cls, "role": "nutrient", "part": "근육", "content_text": content, "activity_ko": act, "source": [2]}
note = "사료를 먹인 어린 개체(약 160 g) 굶기기 전 시점(T0) 값; 표 제목은 'g/100 g tissue'이나 합계가 100이어서 총 지방산 대비 %로 보임"
compounds = [
 fa("Docosahexaenoic acid", "DHA(C22:6n-3)", "n-3 지방산", f"14.79 ± 1.03 ({note}); 35일 절식 뒤 26.99 ± 3.88", "근육에서 가장 많은 고도불포화지방산이었고 절식 중에도 보존되어 비율이 높아졌다[2]"),
 fa("Eicosapentaenoic acid", "EPA(C20:5n-3)", "n-3 지방산", f"6.40 ± 0.1 ({note}); 35일 절식 뒤 5.79 ± 0.45", "절식 중 근육에서 약간 줄었다(−7.1%)[2]"),
 fa("Docosapentaenoic acid", "DPA(C22:5n-3)", "n-3 지방산", f"2.50 ± 0.31 ({note})", "절식 중 근육에서 17.1% 늘었다[2]"),
 fa("alpha-Linolenic acid", "알파-리놀렌산(C18:3n-3)", "n-3 지방산", f"2.72 ± 1.52 ({note})", "식물성 n-3 지방산으로 근육에서는 절식 중 12.0% 줄었다[2]"),
 fa("Arachidonic acid", "아라키돈산(C20:4n-6)", "n-6 지방산", f"1.87 ± 0.16 ({note}); 35일 절식 뒤 4.18 ± 0.49", "절식 중 근육 비율이 124.8% 늘었다[2]"),
 fa("Linoleic acid", "리놀레산(C18:2n-6)", "n-6 지방산", f"10.24 ± 0.39 ({note})", "절식 중 근육에서 18.4% 줄었다[2]"),
 fa("Palmitic acid", "팔미트산(C16:0)", "포화지방산", f"19.11 ± 1.34 ({note})", "근육에서 가장 많은 포화지방산이었다[2]"),
 fa("Stearic acid", "스테아르산(C18:0)", "포화지방산", f"6.85 ± 0.33 ({note})", "절식 중 근육 비율이 19.6% 늘었다[2]"),
 fa("Oleic acid", "올레산(C18:1n-9)", "단일불포화지방산", f"17.53 ± 0.23 ({note}); 35일 절식 뒤 10.46 ± 2.18", "절식 중 에너지원으로 먼저 쓰여 근육에서 39.0% 줄었다[2]"),
 fa("Palmitoleic acid", "팔미톨레산(C16:1n-7)", "단일불포화지방산", f"4.84 ± 0.61 ({note})", "절식 중 근육에서 70.5% 줄었다[2]"),
 {"name": "Myoglobin", "name_ko": "미오글로빈", "class": "헴 단백질", "role": "bioactive", "part": "근육(혈합육)", "content_text": "함량 확인하지 못함; 147개 아미노산(444 뉴클레오타이드 해독틀)", "activity_ko": "살의 붉은색과 산소 저장을 맡는 단백질로, 전갱이과 다섯 종 사이 서열 일치도는 81–99%였다[10]", "source": [10]},
 {"name": "Histamine", "name_ko": "히스타민", "class": "생체 아민", "role": "bioactive", "part": "부산물 단백질 가수분해물", "content_text": "수치 확인하지 못함(초록에 '높은 함량'으로만 적힘)", "activity_ko": "함량이 높아 가수분해물을 식품 배합에 10% 이하로만 쓸 수 있다고 했다[15]", "source": [15]},
]

assays = [
 {"role": "literature", "compound": "Fatty acid methyl esters (DHA, EPA etc.)", "compound_ko": "지방산 조성(DHA·EPA 등)", "part": "근육",
  "content": "T0 근육 DHA 14.79, EPA 6.40, C16:0 19.11, C18:1n-9 17.53, ΣPUFA 34.57(표 제목 g/100 g tissue, 합계 100)[2]",
  "method": "GC-FID",
  "conditions": {"instrument": "Agilent Technologies 6880 가스크로마토그래프(원문 표기 그대로), 불꽃이온화검출기", "column": "DB-23(Agilent), 60 m × 0.25 mm, 막 두께 0.25 μm", "mobile_phase": "운반 기체 수소", "gradient": "140 °C 시작, 주입 5분 뒤 4 °C/min로 250 °C까지 올린 뒤 10분 유지", "flow": "", "temp": "검출기 260 °C", "detection": "FID", "injection": "1 μL, splitless",
   "sample_prep": "멕시코 바하칼리포르니아 실험실 순환여과 수조(22 °C)의 어린 부시리 근육을 60 °C 진공 건조 36시간 → 막자사발 분쇄 → −80 °C 보관; 디클로로메탄–메탄올(2:1, v/v, BHT 1% 함유)로 4 °C 하룻밤 지질 추출(Folch 변법) → Christie 법으로 지방산 메틸에스터화",
   "standard": "37 Component FAME Mix·PUFA1(Supelco/Sigma-Aldrich) 머무름 시간 비교; 내부표준 지방산으로 피크 면적 환산(내부표준의 탄소 수는 받은 전문 텍스트에서 빠져 확인 못함), Agilent ChemStation",
   "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "이 종의 근육 지방산 조성(DHA·EPA 등)을 정량한 사례로, 절식 중 어떤 지방산이 에너지로 먼저 쓰이고 어떤 지방산이 보존되는지를 가르는 지표로 쓰였다[2]. 전문(Methods) 확인 — 유속·검출·정량한계·회수율은 본문에 없음[2].",
  "source": [2], "url": "https://doi.org/10.1371/journal.pone.0170124", "source_kind": "paper"},
 {"role": "literature", "compound": "Mercury", "compound_ko": "수은(총수은)", "part": "필레(양식 개체 혼합 시료)",
  "content": "평균 0.03 mg/kg(범위 0.02–0.05), 오스트레일리아 양식 부시리 혼합 시료 27개[11]",
  "method": "", "conditions": {},
  "rationale": "수은은 대형 육식성 어류 살의 대표적 위해 지표로, 수출 검사 기준과 비교하려고 측정되었다[11]. 전문 확인 못함 — 초록만 확인해 분석 기기·조건은 비워 둠[11].",
  "source": [11], "url": "https://doi.org/10.1016/j.chemosphere.2011.10.044", "source_kind": "paper"},
 {"role": "literature", "compound": "Mercury, arsenic, cadmium, lead", "compound_ko": "수은·비소·카드뮴·납", "part": "근육(야생 개체)",
  "content": "남아프리카 야생 부시리(37마리) 평균 Hg 0.16, As 0.98, Cd 0.004, Pb 0.005 mg/kg[12]",
  "method": "", "conditions": {},
  "rationale": "16종 금속을 재어 섭취 안전성을 평가했고, 수은·비소·아연은 몸 크기와 양의 상관을 보였다[12]. 전문 확인 못함 — 초록만 확인해 분석 기기·조건은 비워 둠[12].",
  "source": [12], "url": "https://doi.org/10.1016/j.marpolbul.2017.06.074", "source_kind": "paper"},
]

d = {
 "slug": "seriola-lalandi", "name_ko": "부시리", "name_en": "Yellowtail amberjack",
 "scientific_name": "Seriola lalandi Valenciennes, 1833",
 "aliases": ["부시리", "Yellowtail amberjack", "Yellowtail kingfish", "California yellowtail"],
 "sections": sections, "compounds": compounds, "markers": [], "assays": assays,
 "nutrients": [], "production": [], "world": [], "gi": [], "orgs": [],
 "sources": sources,
}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in sections: print(s["key"], len(s["body"]))
