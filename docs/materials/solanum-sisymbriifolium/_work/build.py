import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
A = "2026-11-02"
def pm(n, title, cite, pmid, pmc, doi, note):
    ids = f"PMID {pmid}" + (f", {pmc}" if pmc else "")
    url = f"https://doi.org/{doi}" if doi else f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
    return {"n": n, "title": f"{title} — {cite} ({ids}, {note})", "url": url, "publisher": "PubMed", "accessed": A}
S = [
 {"n": 1, "title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 둥근가시가지열매(Solanum sisymbriifolium Lam., Sticky nightshade) 사용가능·사용가능부위: 열매 (로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json)", "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
 pm(2, "Seasonal Variation in Flower Traits, Visitor Traits, and Reproductive Success of Solanum sisymbriifolium Lamarck (Solanaceae) in the Rarh Region of West Bengal, India", "Biology (Basel) 2025;14(7):865", 40723422, "PMC12292435", "10.3390/biology14070865", "전문 확인"),
 pm(3, "Issues of interspecific hybridization between Solanum lycopersicum L. and Solanum sisymbriifolium Lam.", "Vavilovskii Zhurnal Genet Selektsii 2026;30(4):569-580", 42495170, "PMC13392682", "10.18699/vjgb-26-59", "전문 확인"),
 pm(4, "Taxonomic revision of the neophyte nightshades (Solanum, Solanaceae) in European Russia and the North Caucasus", "PhytoKeys 2026;270:235-271", 41695313, "PMC12902770", "10.3897/phytokeys.270.169902", "전문 확인"),
 pm(5, "Exploring biodiversity and ethnobotanical significance of Solanum species in Uzbekistan: unveiling the cultural wealth and ethnopharmacological uses (문헌 종설)", "Front Pharmacol 2024;14:1287793", 38333226, "PMC10851437", "10.3389/fphar.2023.1287793", "전문 확인"),
 pm(6, "Assessment of an Organ-Specific de novo Transcriptome of the Nematode Trap-Crop, Solanum sisymbriifolium", "G3 (Bethesda) 2018;8(7):2135-2143", 29769290, "PMC6027862", "10.1534/g3.118.200327", "전문 확인"),
 pm(7, "Elite genotype selection through antioxidant and antimicrobial activities, in vitro multiplication with meta-Topolin, genetic fidelity assessment via SCoT markers and cytological study, and chemo-profiling of selected elite genotype of Solanum sisymbriifolium Lam.", "3 Biotech 2025;15(4):75", 40060288, "PMC11885203", "10.1007/s13205-025-04229-1", "초록만 확인 — PMC 전문 본문을 받지 못함"),
 pm(8, "Solasodine levels in Solanum sisymbriifolium Lam.", "Indian J Exp Biol 1989;27(2):189", 2807409, None, None, "초록만 확인"),
 pm(9, "Anticonvulsant activity of solasodine isolated from Solanum sisymbriifolium fruits in rodents", "Pharm Biol 2010;49(2):194-199", 21062107, None, "10.3109/13880209.2010.508499", "초록만 확인"),
 pm(10, "Evaluation of the biological activity of the molluscicidal fraction of Solanum sisymbriifolium against non target organisms", "Fitoterapia 2010;81(7):767-771", 20388535, None, "10.1016/j.fitote.2010.04.003", "초록만 확인"),
 pm(11, "Molluscicidal activity of some Brazilian Solanum spp. (Solanaceae) against Biomphalaria glabrata", "Ann Trop Med Parasitol 2005;99(4):419-425", 15949190, None, "10.1179/136485905X36208", "초록만 확인"),
 pm(12, "Effect of Steroidal Glycoalkaloids on Hatch and Reproduction of the Potato Cyst Nematode", "Plant Dis 2021;105(10):2975-2980", 33754862, None, "10.1094/PDIS-02-21-0247-RE", "초록만 확인"),
 pm(13, "Toxic Effects of the Trap Crop Solanum sisymbriifolium on the Hatch and Viability of Globodera pallida", "J Nematol 2024;56(1):20240027", 39131583, "PMC11310831", "10.2478/jofnem-2024-0027", "전문 확인"),
 pm(14, "High-Performance Liquid Chromatography-Mass Spectrometry Analysis of Glycoalkaloids from Underexploited Solanum Species and Their Acetylcholinesterase Inhibition Activity", "Plants (Basel) 2022;11(3):269", 35161249, "PMC8839269", "10.3390/plants11030269", "전문 확인 — 받은 본문에서 종 이름이 빠져 있어 이 종의 대상 여부는 [13]의 인용으로 확인"),
 pm(15, "Crop Rotation with Resistant Potato and Solanum sisymbriifolium to Control Globodera pallida", "J Nematol 2025;57(1):20250054", 41362650, "PMC12682248", "10.2478/jofnem-2025-0054", "전문 확인"),
 pm(16, "Effect of the trap crop, Solanum sisymbriifolium, on three Globodera species (색인 제목에서 종명이 빠져 초록으로 보완)", "J Nematol 2019;51:1-11", 31132006, "PMC6930959", "10.21307/jofnem-2019-030", "초록만 확인"),
 pm(17, "Evaluation of Quinoa and Solanum sisymbriifolium as Trap Crops for Globodera pallida in Rotation with Susceptible and Resistant Potato", "Plant Dis 2026;110(9):3991-4000", 41863854, None, "10.1094/PDIS-11-25-2303-RE", "초록만 확인"),
 pm(18, "Solanum linnaeanum and Solanum sisymbriifolium as a sustainable strategy for the management of Meloidogyne chitwoodi", "Sci Rep 2021;11(1):3484", 33568684, "PMC7875996", "10.1038/s41598-020-77905-2", "초록만 확인"),
 pm(19, "Molecular insights into Solanum sisymbriifolium's resistance against Globodera pallida via RNA-seq", "BMC Plant Biol 2024;24(1):1005", 39455908, "PMC11515252", "10.1186/s12870-024-05694-1", "초록만 확인"),
 pm(20, "The complete chloroplast genome of Solanum sisymbriifolium (Solanaceae), the wild eggplant", "Mitochondrial DNA B Resour 2022;7(5):886-888", 35692713, "PMC9176339", "10.1080/23802359.2022.2077667", "초록만 확인"),
 pm(21, "Molecular delimitation of clades within New World species of the \"spiny solanums\" (Solanum subg. Leptostemonum)", "Taxon 60(5):1429-1441", 32327851, "PMC7169808", "10.1002/tax.605018", "초록만 확인"),
 pm(22, "Deciphering phenotyping, DNA barcoding, and RNA secondary structure predictions in eggplant wild relatives provide insights for their future breeding strategies", "Sci Rep 2023;13(1):13829", 37620406, "PMC10449851", "10.1038/s41598-023-40797-z", "초록만 확인"),
 pm(23, "The antihypertensive and diuretic effect of crude root extract and saponins from Solanum sisymbriifolium Lam., in L-NAME-induced hypertension in rats", "J Ethnopharmacol 2022;298:115605", 35973627, None, "10.1016/j.jep.2022.115605", "초록만 확인"),
 pm(24, "Antihypertensive effect of nuatigenin-3-O-β-chacotriose from Solanum sisymbriifolium Lam. (Solanaceae) (ñuatî pytâ) in experimentally hypertensive (ARH+DOCA) rats under chronic administration", "Phytomedicine 2011;18(8-9):634-640", 21353509, None, "10.1016/j.phymed.2011.01.012", "초록만 확인"),
 pm(25, "Steroidal saponins from the roots of Solanum sisymbriifolium Lam. (Solanaceae) have inhibitory activity against dengue virus and yellow fever virus", "Braz J Med Biol Res 2021;54(7):e10240", 34008751, "PMC8130103", "10.1590/1414-431X2020e10240", "초록만 확인"),
 pm(26, "A new steroidal saponin from Solanum sisymbriifolium roots", "Fitoterapia 2005;76(6):577-579", 15990250, None, "10.1016/j.fitote.2005.04.008", "초록만 확인"),
 pm(27, "Analgesic, neuropharmacological, anti-diarrheal, and cytotoxic activities of the extract of Solanum sisymbriifolium (Lam.) leaves", "Avicenna J Phytomed 2013;3(4):302-312", 25050287, "PMC4075724", None, "초록만 확인"),
 pm(28, "Diuretic activity of ethanolic extract and fraction enriched in saponins from Solanum sisymbriifolium Lam. root in rats", "Eur Rev Med Pharmacol Sci 2024;28(21):4526-4535", 39560928, None, "10.26355/eurrev_202411_36911", "초록만 확인"),
 pm(29, "Evaluation of Solanum sisymbriifolium as a Potential Inoculum Source of Verticillium dahliae and Colletotrichum coccodes", "Plant Dis 2017;101(7):1300-1305", 30682946, None, "10.1094/PDIS-07-16-1077-RE", "초록만 확인"),
 pm(30, "On the nature and origin of the oxalate package in Solanum sisymbriifolium anthers", "Protoplasma 2010;247(1-2):45-56", 20372946, None, "10.1007/s00709-010-0137-5", "초록만 확인"),
 pm(31, "Intra-individual variation in pollen availability: an experimental analysis of its impact on plant-pollinator interactions", "Ann Bot 2026;137(7):2209-2223", 41906809, "PMC13319322", "10.1093/aob/mcag073", "초록만 확인"),
 pm(32, "Evaluation of Solanum linnaeanum and S. sisymbriifolium extracts for the management of a root-knot nematode (색인 제목에서 학명이 빠져 초록으로 보완)", "Heliyon 2023;9(6):e16298", 37251490, "PMC10220364", "10.1016/j.heliyon.2023.e16298", "초록만 확인"),
 pm(33, "Initial responses of the trap-crop, Solanum sisymbriifolium, to Globodera pallida invasions", "Plant Genome 2020;13(2):e20016", 33016605, "PMC12806897", "10.1002/tpg2.20016", "초록만 확인"),
 {"n": 34, "title": "Evaluation of Nutrient Composition of Ripe and Unripe Fruits of Solanum sisymbriifolium — Asian Journal of Agriculture and Food Sciences (원문 페이지는 이 작업 환경에서 열리지 않음 — 웹 검색 결과 요약으로만 존재를 확인, 수치는 옮기지 않음)", "url": "https://ajouronline.com/index.php/AJAFS/article/view/6525", "publisher": "Asian Online Journals", "accessed": A},
 pm(35, "Overview of the phylogenetic relationships of some southern Brazilian species from section Torva and related sections of \"spiny Solanum\" (Solanum subgenus Leptostemonum, Solanaceae)", "Genetica 2007;132(2):143-158", 17549584, None, "10.1007/s10709-007-9156-3", "초록만 확인"),
]

sec = []
def add(k, t, b): sec.append({"key": k, "title": t, "body": b})
add("overview", "한눈에 보기",
"둥근가시(Solanum sisymbriifolium Lam.)는 가지과(Solanaceae) 가지속의 가시가 많고 끈끈한 풀로, 영어로 sticky nightshade·litchi tomato·vila-vila 등으로 불리며 남아메리카가 원산이다[2, 4]. 식약처 「식품원료 목록」에는 원료명 '둥근가시가지열매'(영문명 Sticky nightshade) 한 행이 올라 있고, 상태는 '사용가능', 사용 조건은 '사용가능부위 : 열매'이다[1]. 목록에는 식물 자체의 국명이 따로 적혀 있지 않아, 이 문서의 '둥근가시'와 원료명에서 부위를 뗀 '둥근가시가지'가 국가표준식물목록의 국명과 같은지는 확인하지 못함. 이 종을 원재료로 하는 건강기능식품 고시형 원료는 확인하지 못함.\n\n"
"열매는 지름 1–3 cm 안팎의 둥근 장과로 익으면 붉어진다[3–5]. 원산지 일부에서는 열매를 날로 또는 삶아 먹었다는 기록이 있으나, 연구는 주로 감자 시스트선충을 줄이는 덫작물(trap crop) 이용과 뿌리 추출물의 동물 약리 시험에 몰려 있다[5, 15, 23]. 열매에서는 스테로이드 알칼로이드인 솔라소딘과 그 배당체 솔라마진·β-솔라마린이 보고되었으나 정량 자료는 1989년 초록의 한 값뿐이다[8–10]. 같은 가지속의 감자·가지·까마중·루로·코코나·Solanum aethiopicum 등은 식약처 목록에서 별도 원료이므로 이 문서는 그 자료를 섞지 않았다[1].")
add("history", "역사와 쓰임",
"아르헨티나 북서부와 파라과이 남서부의 원주민 집단은 이 종의 열매를 날로 먹거나 삶아 식량으로 썼다고 문헌 종설에 정리되어 있다[5]. 같은 종설은 아르헨티나·파라과이에서 열매와 뿌리를 진통·이뇨·고혈압·간 보호 목적의 민간약으로, 브라질에서는 꽃·열매·뿌리·잎을 비슷한 민간약으로 썼다고 소개한다[5]. 파라과이 민간의학에서는 뿌리를 고혈압과 이뇨에 써 왔으며, 현지 이름 'ñuatî pytâ'가 논문 제목에 쓰였다[23, 24].\n\n"
"이 종은 일찍부터 유럽 식물원에 들여와 길러졌고, 휴경한 감자밭에 선충 덫작물로 심기도 했다[4]. 원산지 밖의 아시아·아프리카·오스트레일리아 열대·아열대와 이탈리아에서는 공격적인 잡초로 여겨진다[4]. 인도 서벵골에서는 길가·빈터에 자라는 관목성 잡초로 기록되었다[2]. 감자 시스트선충 덫작물로 10년 넘게 연구되었지만, 작물로서 경제적 가치가 낮고 종자를 구하기 어려워 감자 농가에 널리 쓰이지는 않았다[6, 13, 15]. 국내 재배·수입·식용 이력은 확인하지 못함.")
add("biology", "식물학적 특징",
"줄기와 가지에 끈끈한 샘털과 주황·노란빛 가시가 있고, 잎은 깃꼴로 깊게(한두 번) 갈라지며 별 모양 털이 섞인다[2, 4]. 러시아 표본 기재와 한 문헌 종설은 한해살이로(종설은 높이 50–150 cm), 미국 식물병 연구는 여러해살이 초본으로 적어 생활형 기술이 출처마다 다르다[4, 5, 29]. 꽃은 송이꽃차례에 달리며 화관은 흰색 또는 보라색으로 지름 20–30 mm이고, 수술 5개의 길이가 같다[2, 4].\n\n"
"꽃밀이 없는 꽃으로, 꽃밥 끝의 구멍으로 꽃가루가 나오며 벌이 진동으로 꽃가루를 털어 내는 수분이 관찰되었다[2, 31]. 인도 집단에서 꽃 한 송이의 꽃가루는 평균 약 42.9만 개, 밑씨는 74개였고, 자가화합성(ISI 0.02)이면서 수분 매개자 의존도(IDP 0.72)가 높았다[2]. 반면 러시아 육종장의 시료는 자가불화합성으로 기술되어 계통에 따라 다를 수 있다[3]. 꽃밥 조직에는 수산칼슘 결정 덩어리가 생긴다[30]. 열매는 둥근 장과로 익으면 선명한 붉은색이며 콩팥 모양 씨가 많다[2]. 커진 꽃받침이 열매를 감싼다는 기재와 열매가 꽃받침 밖으로 드러난다는 기재가 함께 있다[2, 4].")
add("related_species", "이름과 가까운 종",
"둥근가시는 가시와 별 모양 털을 가진 가지속 Leptostemonum 아속('가시 가지류')에 속하며, 분자계통 연구에서 이 종의 이름을 딴 Sisymbriifolium 분계군이 새로 설정되었다[21]. 핵 ITS와 엽록체 염기서열 계통 분석에서 남부 브라질의 Torva 절은 가지(S. melongena)·S. jamaicense·둥근가시와 가깝게 묶였다[35]. 가지 야생 근연종 13종의 DNA 바코드 비교에서는 S. macrocarpon·S. wrightii·S. aculeatissimum과 함께 한 무리(gboma 분계군)로 묶였다[22]. 전사체의 핵 유전자는 가지와, 엽록체 유전자는 토마토와 더 가까워 과거 종간 교잡이 있었을 가능성이 제기되었다[6].\n\n"
"러시아 신귀화 가지속 검색표에서는 화관이 방사대칭이고 꽃밥 길이가 모두 같으며 익은 열매가 꽃받침 밖으로 나오는 점으로, 꽃밥 하나가 길고 열매가 꽃받침에 싸이는 S. heterodoxum과 구별한다[4]. 영어 이름 'litchi tomato'에도 불구하고 토마토와는 먼 친척으로, 토마토와의 교잡은 배 구출 배양(embryo rescue)을 거쳐야 겨우 식물체를 얻을 수 있었다[3]. 식약처 목록에서 감자·가지·까마중·루로·코코나 등은 각각 별도 원료이므로 그 자료와 섞지 않았다[1].")
add("cultivation", "재배와 생산",
"둥근가시는 감자 시스트선충(Globodera pallida)의 알을 부화시켜 뿌리로 끌어들이지만 성숙을 막는 덫작물로 연구된다[6]. 미국 세 지역 현장 시험에서 둥근가시를 심은 뒤 세 Globodera 종의 시스트 속 알 밀도가 25–68% 줄었고, 그중 한 종은 노출 기간이 6주일 때 30%, 12주일 때 81% 줄었다[16]. 아이다호 3년 윤작 시험에서 첫해 둥근가시는 남은 알을 약 70% 줄이고 알 생존율을 58%로 낮췄으며, 2년 연속 재배 뒤 감수성 감자를 심어도 새 시스트가 검출되지 않았다[15]. 퀴노아와 비교한 시험에서 둥근가시는 다음 감자의 새 시스트를 82%에서 거의 100%까지 줄였다[17].\n\n"
"이 윤작 시험에서는 온실에서 3주 기른 모를 그늘에서 1주 적응시킨 뒤 밭(미세구)에 옮겨 12주 길렀다[15]. 품종 'Sis 6001'은 뿌리혹선충 Meloidogyne chitwoodi에도 저항성을 보였다(혹 지수 2 이하, 증식 계수 1 이하)[18]. 감자 시들음병균 Verticillium dahliae의 증식원 역할은 감수성 감자 품종보다 작았다[29]. 인도에서는 연중 꽃이 피고 봄–우기에 열매 맺음률이 82–86%였다[2]. 침입성이 있어 새 지역에 들여올 때 신중해야 한다는 지적이 있다[5]. 국내 재배 면적·생산량 통계와 열매 수확용 재배법은 확인하지 못함.")
add("processing", "가공과 제품",
"원산지 기록에서 열매는 날로 먹거나 삶아 먹는 방식으로 쓰였다[5]. 익은 열매와 덜 익은 열매의 영양성분을 비교한 논문이 있으나 원문을 열지 못해 수치는 옮기지 않았다[34]. 인도 서벵골 10개 수집 계통에서 항산화·항균 활성이 가장 좋은 계통을 골라 조직배양(티디아주론 0.2 mg/L + 메타토폴린 0.2 mg/L에서 새순 14.06개)으로 증식했고, 증식한 식물에서 페놀산 7종(3.30–121.75 µg/g 건물)과 비타민 B 4종(4.38–22.29 mg/100 g 생체)을 측정했다[7]. 다만 초록에는 분석 부위가 적혀 있지 않아 열매 값인지는 확인하지 못함.\n\n"
"식품 밖의 이용으로, 'Sis 6001' 품종의 덜 익은 열매 물 추출물(0.8 mg/mL)은 뿌리혹선충 2령 유충의 누적 부화를 24%로 낮추고 감염력을 떨어뜨렸다[32]. 브라질 가지속 13종의 열매·지상부·뿌리 추출물 비교에서 둥근가시 추출물은 달팽이(Biomphalaria glabrata)에 유의한 살패 활성을 보였고(활성 부위는 초록에 명시되지 않음), 열매의 한 분획(B)은 물고기·수서곤충에 덜 해로워 살패제 후보로 제안되었다[10, 11]. 식약처 목록의 원료 형태는 열매 하나뿐이며, 국내 가공 제품과 생산실적은 확인하지 못함[1].")
add("genetics", "유전과 육종",
"염색체는 2n = 24이며, 조직배양으로 늘린 식물도 어미 식물과 같은 염색체 수를 유지했다[7]. 유세포 분석으로 잰 핵 DNA 양은 약 4.73 pg/2C로 4배체 감자보다 컸지만, 염색체 수는 2배체 감자처럼 24개였다[6]. 꽃눈·뿌리·줄기·잎의 전사체 41,189개 유전자 단위를 긴 읽기 서열(SMRT)로 정리했고, BUSCO 완전성은 93%, 중복 사본 비율은 30.2%로 높아 과거 전체 유전체 중복 뒤 다시 2배체화했을 가능성이 제기되었다[6]. 저항성(R) 유전자 후보는 67개로 감자(309개)·토마토(137개)보다 적었다[6].\n\n"
"엽록체 유전체는 155,771 bp(GC 37.76%)이며 유전자 128개가 주석되었다[20]. 감자 시스트선충 감염 초기 뿌리에서는 277개 전사체의 발현이 바뀌었고, 품종 'Melody'와 'Sis6001'에서는 각각 4,087개와 2,043개 유전자가 차등 발현되었다[19, 33]. 토마토와의 교잡에서는 배 구출 배양으로 12개체를 얻었으며, 뿌리 끝 세포의 염색체 수가 16–26개로 섞여 있었고 초록 열매 토마토와의 조합에서는 노란 주황 열매가 나왔다[3]. 열매 품질을 목표로 한 품종 육성은 확인하지 못함.")
add("safety", "안전성",
"식약처 「식품원료 목록」에서 둥근가시는 열매만 사용가능부위이며, 뿌리·잎 등 다른 부위의 행은 없다[1]. 1989년 초록에 따르면 솔라소딘 함량은 장과 0.93%, 잎 0.73%, 줄기 0.23%였으나 건물·생체 기준과 열매 익음 정도는 초록에 적혀 있지 않다[8]. 열매의 생물 활성 분획에서는 스테로이드 알칼로이드 배당체 솔라마진과 β-솔라마린이 분리되었고, 일부 분획은 물고기·수서곤충·달팽이에 독성을 보였다[10]. 열매에서 분리한 솔라소딘을 생쥐·흰쥐 복강에 25–100 mg/kg 주사하자 항경련 효과와 함께 수면 시간이 길어지는 중추 억제 작용이 나타났다(동물 주사 시험)[9].\n\n"
"잎·줄기·뿌리에서는 하이드록시솔라마진·시코판틴·라이코노사이드 II 등 여러 글리코알칼로이드가 확인되었으나 이는 열매가 아닌 부위의 결과다[13, 14]. 뿌리 추출물과 사포닌의 혈압·이뇨 효과, 뿌리 사포닌의 항바이러스 효과는 흰쥐와 세포 시험 결과이며, 뿌리는 식품 사용 부위가 아니다[1, 23, 25, 28]. 잎 추출물은 브라인슈림프 치사 시험에서 LC50 61.66 µg/mL였다[27]. 열매 글리코알칼로이드의 기준·안전 섭취량, 사람 시험, 알레르기 보고, 국내 잔류농약 기준 등 공공기관 안전 정보는 확인하지 못함.")

comp = [
 {"name": "Solasodine", "name_ko": "솔라소딘", "class": "스테로이드 알칼로이드(아글리콘)", "role": "marker", "part": "열매(장과)·잎·줄기", "content_text": "장과 0.93%, 잎 0.73%, 줄기 0.23%(측정법 3가지, 기준(건물·생체) 초록에 없음)[8]; 건조 열매에서 분리·GC-MS 동정[9]", "activity_ko": "열매에서 분리한 솔라소딘을 설치류 복강에 주사하면 항경련·중추 억제 작용을 보였다(동물 시험)[9]", "source": [8, 9]},
 {"name": "Solamargine", "name_ko": "솔라마진(α-솔라마진)", "class": "스테로이드 글리코알칼로이드", "role": "bioactive", "part": "열매·잎·줄기·뿌리", "content_text": "열매 활성 분획에서 분리(함량 수치 없음)[10]; 8주 된 식물 줄기·잎 1-뷰탄올 추출액 116.9 mg/L, 뿌리 1-뷰탄올 추출액 20.4 mg/L(조직 함량이 아닌 추출액 농도)[13]", "activity_ko": "감자 시스트선충 부화를 65% 줄이고 감자 감염을 98% 줄였다(시험관·화분 시험)[12]", "source": [10, 12, 13]},
 {"name": "beta-Solamarine", "name_ko": "β-솔라마린", "class": "스테로이드 글리코알칼로이드", "role": "bioactive", "part": "열매", "content_text": "열매 활성 분획에서 분리(함량 수치 없음)[10]", "activity_ko": "같은 계열의 α-솔라마린 노출은 감자 시스트선충 부화를 87% 줄였다(β형 시험은 초록에 없음)[12]; 열매 분획은 물고기·수서곤충·달팽이에 독성을 보였다[10]", "source": [10, 12]},
 {"name": "Hydroxysolamargine", "name_ko": "하이드록시솔라마진", "class": "스테로이드 글리코알칼로이드", "role": "bioactive", "part": "잎·줄기·뿌리(열매 아님)", "content_text": "6주 된 식물의 잎·줄기·뿌리에서 HPLC-TOF MS로 잠정 동정(함량은 솔라마진 당량으로만 제시)[13, 14]", "activity_ko": "글리코알칼로이드 추출물의 아세틸콜린에스터레이스 억제가 보고되었으나 개별 성분 기여는 밝혀지지 않았다[14]", "source": [13, 14]},
 {"name": "Sycophantine", "name_ko": "시코판틴", "class": "스테로이드 글리코알칼로이드", "role": "bioactive", "part": "잎·줄기(열매 아님)", "content_text": "줄기·잎에서 잠정 동정(함량 수치 없음)[13]", "activity_ko": "선충 독성 후보 성분으로 거론되나 개별 활성은 확인되지 않았다[13]", "source": [13]},
 {"name": "Lyconoside II", "name_ko": "라이코노사이드 II", "class": "스테로이드 글리코알칼로이드", "role": "bioactive", "part": "잎·줄기·뿌리(열매 아님)", "content_text": "줄기·잎·뿌리에서 잠정 동정(함량 수치 없음)[13]", "activity_ko": "질량분석 조각 패턴으로 잠정 배정된 성분이다[14]", "source": [13, 14]},
 {"name": "Nuatigenin 3-O-beta-chacotrioside", "name_ko": "누아티제닌-3-O-β-차코트리오사이드", "class": "스테로이드 사포닌", "role": "bioactive", "part": "뿌리(식품 사용 부위 아님)", "content_text": "뿌리 함수에탄올 추출물에서 분리(함량 수치 없음)[24]", "activity_ko": "실험적 고혈압 흰쥐에 1.0 mg/kg/일 16주 경구 투여 시 혈압이 내려갔다(동물 시험)[24]", "source": [24]},
 {"name": "Isonuatigenin 3-O-beta-solatrioside", "name_ko": "이소누아티제닌-3-O-β-솔라트리오사이드", "class": "스테로이드 사포닌", "role": "bioactive", "part": "뿌리(식품 사용 부위 아님)", "content_text": "뿌리에서 새로 분리·구조 결정(함량 수치 없음)[26]", "activity_ko": "뿌리에서 분리한 사포닌 3종(이 성분 포함 여부는 초록에 없음)은 세포 시험에서 뎅기 바이러스 2형에 EC50 24.9–35.1 µg/mL의 살바이러스 활성을 보였다[25]", "source": [25, 26]},
 {"name": "Cuscohygrine", "name_ko": "쿠스코하이그린", "class": "피롤리딘 알칼로이드", "role": "bioactive", "part": "부위 미상", "content_text": "종설의 성분 목록에 수록(원 논문·부위·함량 확인하지 못함)[5]", "activity_ko": "이 종에서의 활성은 확인하지 못함[5]", "source": [5]},
 {"name": "Chlorogenic acid", "name_ko": "클로로겐산", "class": "페놀산", "role": "bioactive", "part": "부위 미상", "content_text": "종설의 성분 목록에 카페산·다이하이드로카페산·페룰산과 함께 수록(부위·함량 확인하지 못함)[5]; 조직배양 식물의 페놀산 7종 합산 범위 3.30–121.75 µg/g 건물(부위 초록에 없음)[7]", "activity_ko": "조직배양으로 늘린 식물이 어미 식물과 같은 페놀산 조성을 유지했다[7]", "source": [5, 7]},
 {"name": "Rutin", "name_ko": "루틴", "class": "플라보노이드 배당체", "role": "bioactive", "part": "부위 미상", "content_text": "종설의 성분 목록에 캠페롤-3-루티노사이드와 함께 수록(부위·함량 확인하지 못함)[5]", "activity_ko": "이 종에서의 개별 활성은 확인하지 못함[5]", "source": [5]},
 {"name": "Calcium oxalate", "name_ko": "수산칼슘", "class": "무기 결정(옥살산염)", "role": "bioactive", "part": "꽃밥(열매 아님)", "content_text": "꽃밥의 원형 세포군 액포에 집합 결정(드루즈)으로 쌓이며 웨웰라이트·웨델라이트·카옥사이트 세 형태가 함께 있음(함량 수치 없음)[30]", "activity_ko": "꽃밥 발달 중 결정이 단백질 결정체를 핵으로 생긴다[30]", "source": [30]},
]
assays = [
 {"role": "literature", "compound": "Solasodine", "compound_ko": "솔라소딘", "part": "열매(장과)", "content": "장과 0.93%, 잎 0.73%, 줄기 0.23%[8]",
  "method": "세 가지 정량법(색인어 기준 박층크로마토그래피·비색법 — 초록에 방법 상세 없음)",
  "conditions": {"instrument": "", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "", "injection": "", "sample_prep": "", "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "열매에서 정량값이 보고된 유일한 성분이고, 열매에서 분리·동정된 주된 스테로이드 알칼로이드다[8, 9]. 1989년 초록만 확인해 측정 조건과 함량 기준(건물·생체)은 전문 확인 못함[8].",
  "source": [8], "url": "https://pubmed.ncbi.nlm.nih.gov/2807409/", "source_kind": "paper"},
]
d = {"slug": "solanum-sisymbriifolium", "name_ko": "둥근가시", "name_en": "Sticky nightshade (Litchi tomato)",
     "scientific_name": "Solanum sisymbriifolium Lam.",
     "aliases": ["둥근가시가지열매", "둥근가시가지", "Sticky nightshade", "Litchi tomato", "Vila-vila"],
     "sections": sec, "compounds": comp, "markers": [], "assays": assays, "nutrients": [], "production": [], "world": [], "gi": [], "orgs": [], "sources": S}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in sec: print(s["key"], len(s["body"]))
