import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
A = "2026-11-02"

def pm(n, title, cit, doi, pmid, pmc=None, journal=""):
    pub = f"{journal} (PubMed {pmid}" + (f", {pmc})" if pmc else ")")
    return {"n": n, "title": f"{title} {cit}", "url": f"https://doi.org/{doi}", "publisher": pub, "accessed": A}

sources = [
 {"n": 1, "title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — '홍다리얼룩새우' 행(학명 Penaeus semisulcatus, 영문 Green tiger prawn, 수산물, 사용가능, 사용가능부위 '-', 사용조건 없음). 같은 속 대하·대하새우분말(P. chinensis), 보리새우·건보리새우·건보리새우분해농축액(P. japonicus), 범보리새우(P. esculentus), 지중해보리새우(P. kerathurus), 바나나새우(P. merguiensis), 얼룩새우(P. monodon), Eastern king prawn(P. plebejus), Southern pink shrimp(P. notialis), 흰다리새우 계열(Litopenaeus vannamei / Penaeus vannamei) 행 대조 (로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json, card.json)", "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
 {"n": 2, "title": "식약처 고시 제2026-43호 「건강기능식품의 기준 및 규격」 제3. 2-30 글루코사민·2-31 N-아세틸글루코사민·2-49 키토산/키토올리고당(원재료 '갑각류(게, 새우 등)의 껍질', 섭취 시 주의사항 '게 또는 새우에 알레르기가 있는 사람은 섭취에 주의') (로컬 원문 docs/refs/MFDS/건강기능식품의기준및규격_2026-43_제1~제3.txt)", "url": "https://www.mfds.go.kr/brd/m_211/view.do?seq=14973", "publisher": "식품의약품안전처", "accessed": A},
 pm(3, "Linking Biological Parameters to Fishery Management: Stock Assessment of Green Tiger Prawn, Penaeus semisulcatus De Haan, 1844 Along the Red Sea Coast of Saudi Arabia.", "Biology (Basel) 2025;15(1):8 (전문 확인)", "10.3390/biology15010008", "41514849", "PMC12784927", "Biology (Basel)"),
 pm(4, "A review of the status and development of Kuwait's fisheries.", "Mar Pollut Bull 2015;100(2):597-606 (초록 확인)", "10.1016/j.marpolbul.2015.07.053", "26233306", None, "Marine Pollution Bulletin"),
 pm(5, "Mitochondrial Markers Identify a Genetic Boundary of the Green Tiger Prawn (Penaeus semisulcatus) in the Indo-Pacific Ocean.", "Zool Stud 2021;60:e8 (초록 확인)", "10.6620/ZS.2021.60-08", "34386093", "PMC8315928", "Zoological Studies"),
 pm(6, "The complete mitochondrial genome of Penaeus semisulcatus (Decapoda: Penaeidae).", "Mitochondrial DNA B Resour 2019;4(2):3274-3275 (초록 확인)", "10.1080/23802359.2019.1659116", "33365953", "PMC7706530", "Mitochondrial DNA Part B"),
 pm(7, "Morphometrics and Mitochondrial DNA Genes Analysis Suggest a New Species of Penaeus (Crustacea: Penaeidae) from the Persian Gulf.", "Biochem Genet 2019;57(2):193-213 (초록 확인)", "10.1007/s10528-018-9884-3", "30099639", None, "Biochemical Genetics"),
 pm(8, "Comparative morphological analysis of telson and uropods in Penaeus canaliculatus, Penaeus semisulcatus, and Metapenaeus stebbingi using scanning electron microscopy and EDX analysis.", "Micron 2024;181:103636 (초록 확인)", "10.1016/j.micron.2024.103636", "38579377", None, "Micron"),
 pm(9, "Sex-Based Variations in Metal(loid) Levels in Green Tiger Shrimp (Penaeus semisulcatus) from the Northeastern Mediterranean Coast of Türkiye: A Human Health Risk-Benefit Assessment.", "Life (Basel) 2026;16(3):487 (전문 확인)", "10.3390/life16030487", "41901005", "PMC13027484", "Life (Basel)"),
 pm(10, "Food safety of the green tiger shrimp Penaeus semisulcatus from the Persian Gulf.", "Environ Sci Pollut Res Int 2022;29(16):23861-23870 (초록 확인)", "10.1007/s11356-021-17620-1", "34817819", None, "Environmental Science and Pollution Research"),
 pm(11, "Human health risk assessment of potentially toxic elements (PTEs) through consumption of marine seafood in the eastern province of Saudi Arabia.", "Mar Pollut Bull 2026;226:119340 (초록 확인)", "10.1016/j.marpolbul.2026.119340", "41633190", None, "Marine Pollution Bulletin"),
 pm(12, "Bioaccumulation of Heavy Metals in Various Tissues of Some Fish Species and Green Tiger Shrimp (Penaeus semisulcatus) from İskenderun Bay, Turkey, and Risk Assessment for Human Health.", "Biol Trace Elem Res 2017;180(2):314-326 (초록 확인)", "10.1007/s12011-017-0996-0", "28353139", None, "Biological Trace Element Research"),
 pm(13, "Arsenic and arsenic species in shellfish and finfish from the western Arabian Gulf and consumer health risk assessment.", "Sci Total Environ 2016;566-567:1235-1244 (초록 확인)", "10.1016/j.scitotenv.2016.05.180", "27277209", None, "Science of the Total Environment"),
 pm(14, "Total mercury levels in selected tissues of some marine crustaceans from Persian Gulf, Iran: variations related to length, weight and sex.", "Bull Environ Contam Toxicol 2012;88(1):60-4 (초록 확인)", "10.1007/s00128-011-0451-4", "22057228", None, "Bulletin of Environmental Contamination and Toxicology"),
 pm(15, "Mercury contamination in some marine biota species from Khuzestan shore, Persian Gulf.", "Toxicol Ind Health 2016;32(7):1302-9 (초록 확인)", "10.1177/0748233714555392", "25500758", None, "Toxicology and Industrial Health"),
 pm(16, "Distribution of heavy metals in Penaeus semisulcatus from Persian Gulf and possible role of metallothionein in their redistribution during storage.", "Environ Monit Assess 2005;100(1-3):71-88 (초록 확인)", "10.1007/s10661-005-7061-8", "15727301", None, "Environmental Monitoring and Assessment"),
 pm(17, "Occurrence and risk characterization of per- and polyfluoroalkyl substances in seafood from the Persian Gulf.", "Environ Sci Pollut Res Int 2023;30(59):124182-124194 (초록 확인)", "10.1007/s11356-023-31129-9", "37996593", None, "Environmental Science and Pollution Research"),
 pm(18, "Microplastics in different tissues of fish and prawn from the Musa Estuary, Persian Gulf.", "Chemosphere 2018;205:80-87 (초록 확인)", "10.1016/j.chemosphere.2018.04.076", "29684694", None, "Chemosphere"),
 pm(19, "Assessing microplastic pollution in the gastrointestinal tract of green tiger prawns (Penaeus semisulcatus) caught off the west coast of the Arabian Gulf, Saudi Arabia.", "Environ Monit Assess 2026;198(5) (초록 확인)", "10.1007/s10661-026-15412-z", "42084771", None, "Environmental Monitoring and Assessment"),
 pm(20, "Studies on infectious myonecrosis virus (IMNV) and infectious hypodermal and hematopoietic necrosis virus (IHHNV) in cultured penaeid shrimp in Egypt.", "Dis Aquat Organ 2021;143:57-67 (초록 확인)", "10.3354/dao03556", "33570040", None, "Diseases of Aquatic Organisms"),
 pm(21, "Variations in biochemical and histological characteristics of WSSV infected green tiger shrimp Penaeus semisulcatus.", "J Recept Signal Transduct Res 2014;34(5):386-95 (초록 확인)", "10.3109/10799893.2014.904874", "24738732", None, "Journal of Receptors and Signal Transduction"),
 pm(22, "Fusariosis in the shrimp Penaeus semisulcatus cultured in Israel.", "Mycopathologia 1989;108(2):145-7 (초록 확인)", "10.1007/BF00436066", "2594048", None, "Mycopathologia"),
 pm(23, "Influence of neuropeptide Y (NPY) on food intake and growth of penaeid shrimps Marsupenaeus japonicus and Penaeus semisulcatus (Decapoda: Penaeidae).", "Comp Biochem Physiol A Mol Integr Physiol 2004;139(2):239-44 (초록 확인)", "10.1016/j.cbpb.2004.09.008", "15528173", None, "Comparative Biochemistry and Physiology Part A"),
 pm(24, "Effects of mint (Mentha piperita L.) leaf extract on growth performance, immune and antioxidant responses in green Tiger shrimp (Penaeus semisulcatus).", "Comp Biochem Physiol B Biochem Mol Biol 2025;280:111139 (초록 확인)", "10.1016/j.cbpb.2025.111139", "40759327", None, "Comparative Biochemistry and Physiology Part B"),
 pm(25, "Evaluating the effects of different processing methods on the nutritional composition of shrimp and the antioxidant activity of shrimp powder.", "Saudi J Biol Sci 2022;29(1):640-649 (전문 확인; 전문 텍스트에서 학명이 빠져 있어 종 동정은 PubMed 초록 색인(Penaeus semisulcatus)과 본문의 'green tiger shrimp' 표기로 판단, 표의 수치는 전문 텍스트에 없음)", "10.1016/j.sjbs.2021.09.029", "35002461", "PMC8717169", "Saudi Journal of Biological Sciences"),
 pm(26, "The effects of Aloe vera (Aloe barbadensis) coating on the quality of shrimp during cold storage.", "J Food Sci Technol 2015;52(10):6647-54 (초록 확인)", "10.1007/s13197-015-1747-x", "26396412", "PMC4573173", "Journal of Food Science and Technology"),
 pm(27, "Optimization of ultrasonic-assisted extraction of astaxanthin from green tiger (Penaeus semisulcatus) shrimp shell.", "Ultrason Sonochem 2021;76:105666 (전문 확인)", "10.1016/j.ultsonch.2021.105666", "34271396", "PMC8283324", "Ultrasonics Sonochemistry"),
 pm(28, "A Comparative Survey on Antioxidant Activity of Iranian Shrimp Waste (Penaeus semisulcatus) and Synthetic Antioxidants.", "Curr Drug Discov Technol 2021;18(5):e06102020186675 (초록 확인)", "10.2174/1570163817999201006192141", "33023433", None, "Current Drug Discovery Technologies"),
 pm(29, "Lipid accumulation in the ovaries of a marine shrimp Penaeus semisulcatus (de Haan).", "J Exp Biol 1999;202(Pt 13):1819-29 (초록 확인)", "10.1242/jeb.202.13.1819", "10359684", None, "Journal of Experimental Biology"),
 pm(30, "Isolation and characterization of the high-density lipoproteins from the hemolymph and ovary of the penaeid shrimp Penaeus semisulcatus (de Haan): apoproteins and lipids.", "J Exp Zool 1997;278(6):339-48 (초록 확인)", "10.1002/(sici)1097-010x(19970815)278:6<339::aid-jez1>3.0.co;2-p", "9262004", None, "Journal of Experimental Zoology"),
 pm(31, "Relationship between vitellogenin and vitellin in a marine shrimp (Penaeus semisulcatus) and molecular characterization of vitellogenin complementary DNAs.", "Biol Reprod 2003;69(1):355-64 (초록 확인)", "10.1095/biolreprod.102.011627", "12672675", None, "Biology of Reproduction"),
 pm(32, "Protein, Vitellogenin, and Vitellin Levels in the Hemolymph and Ovaries during Ovarian Development in Penaeus semisulcatus (de Haan).", "Biol Bull 1992;183(3):394-400 (초록 확인)", "10.2307/1542015", "29300503", None, "The Biological Bulletin"),
 pm(33, "Purification, characterization and functional role of lectin from green tiger shrimp Penaeus semisulcatus.", "Int J Biol Macromol 2014;67:64-70 (초록 확인)", "10.1016/j.ijbiomac.2014.03.008", "24637221", None, "International Journal of Biological Macromolecules"),
 pm(34, "Immunological and antibiofilm property of haemocyanin purified from grooved tiger shrimp (Penaeus semisulcatus): An in vitro and in silico approach.", "Microb Pathog 2020;147:104253 (초록 확인)", "10.1016/j.micpath.2020.104253", "32592822", None, "Microbial Pathogenesis"),
 pm(35, "Purification of WAP domain-containing antimicrobial peptides from green tiger shrimp Penaeus semisulcatus.", "Microb Pathog 2020;140:103920 (초록 확인)", "10.1016/j.micpath.2019.103920", "31843546", None, "Microbial Pathogenesis"),
]

S = {}
S["overview"] = ("한눈에 보기",
"홍다리얼룩새우(Penaeus semisulcatus, 영문 Green tiger prawn)는 보리새우과(Penaeidae)에 드는 바다 새우다[1, 6]. 인도-서태평양이 원산지로 홍해·동아프리카에서 아라비아만·인도 아대륙·동남아시아를 거쳐 오스트레일리아 북부와 북서태평양까지 분포하며, 수에즈 운하를 지나 지중해 동부(이집트·이스라엘·레바논·시리아·튀르키예 남부 연안)에도 정착했다[3]. 아덴만·아라비아만·인도·파키스탄 연안 등에서 중요한 상업 어획 대상이다[3].\n\n"
"식약처 「식품원료 목록」에는 학명 Penaeus semisulcatus로 '홍다리얼룩새우' 한 줄이 올라 있고, 분류는 수산물, 상태는 '사용가능'이다[1]. 사용 부위는 '-'(따로 정하지 않음)로 적혀 있으며 별도의 사용 조건 문구는 없다[1]. 건강기능식품 고시형 원료의 원재료로 연결되어 있지 않아 이 종에 대해 식약처가 정한 지표성분·기능성은 없다[1].\n\n"
"국내 어획·양식 생산 통계와 국가표준식품성분표의 이 종 성분값은 이 조사에서 확인하지 못함.")

S["history"] = ("이용 역사",
"홍다리얼룩새우는 아라비아만(페르시아만) 연안 어업에서 중요한 새우다[4, 27]. 이란 부셰르·후제스탄 주 바다에서는 가장 풍부한 새우로 지역 어업에서 경제적 비중이 크다고 소개된다[27]. 쿠웨이트 과학연구소 조사 자료와 중앙통계국 양륙 자료를 검토한 연구는 이 종의 자원량이 최근 몇 년 사이 주로 남획 때문에 크게 줄었다고 보고했다[4]. 사우디아라비아 홍해 남동부 연안에서는 새우 트롤 어업의 주종으로, 이전 연구들은 전체 새우 어획의 80% 이상을 이 종이 차지한다고 보고했다[3].\n\n"
"양식과 생리 연구도 일찍 시작되었다[22, 30]. 1989년에는 홍해 에일랏에서 양식하던 개체에서 Fusarium solani 진균 감염이 이스라엘 최초의 새우 진균병 사례로 보고되었고, 저자는 감염 새우를 다루는 일이 양식 종사자에게 위험할 수 있다고 지적했다[22]. 1990년대에는 이 종을 모델로 혈림프 지단백질과 난황 단백질(비텔로제닌·비텔린) 연구가 이어졌고, 1997년 지단백질 연구는 이스라엘 국립해양학연구소에서 나왔다[30, 32]. 최근에는 이집트 지중해 연안(다미에타·북시나이)의 민간 양식장에서도 이 종이 길러진다[20].")

S["biology"] = ("어종·형태·생태",
"홍다리얼룩새우는 열대·아열대 바다의 얕은 곳에서 중간 깊이까지 진흙이나 모래 바닥에 사는 저서성 새우다[3]. 암수딴몸이며 암컷이 더 크게 자라 최대 전장이 암컷 251 mm, 수컷 210 mm로 알려져 있고, 기록된 최대 체중은 146.7 g, 수명은 보통 2년 안팎이다[3].\n\n"
"2022년 10월–2023년 9월 사우디아라비아 홍해 연안 조사에서 85,909마리를 측정한 결과 두흉갑장은 1.29–56.14 mm, 체중은 0.91–94.99 g이었다[3]. 폰 베르탈란피 성장식의 극한 두흉갑장은 암컷 60.16 mm, 수컷 48.10 mm였고 성장계수는 각각 연 1.03, 1.02였으며, 암컷이 처음 성숙하는 두흉갑장은 22.09 mm였다[3].\n\n"
"꼬리마디(텔손)의 가운데 융기와 홈 양옆에는 작은 원뿔형 가시가 고르게 나 있고, 비교한 세 종 가운데 꼬리다리(유각)가 가장 길었으며 텔손 껍질의 칼슘·인 함량이 가장 높았다[8]. 난모세포 발달이 끝날 무렵 난소에는 인지질과 트라이아실글리세롤이 거의 같은 양(단백질 1 g당 약 16 mg)씩 쌓였다[29]. 난소가 발달하는 동안 암컷 혈림프의 비텔로제닌 농도는 평균 50 µg/mL에서 439 µg/mL로 늘었다[32].")

S["related_species"] = ("관련 종·이름",
"식약처 「식품원료 목록」에는 보리새우속(Penaeus)의 여러 종이 각각 별도 원료로 올라 있으며, 홍다리얼룩새우는 그중 학명 Penaeus semisulcatus만 가리킨다[1]. 같은 목록에는 대하(P. chinensis), 보리새우(P. japonicus), 범보리새우(P. esculentus), 지중해보리새우(P. kerathurus), 바나나새우(P. merguiensis), 얼룩새우(P. monodon, Giant tiger prawn)가 따로 있다[1]. 국명이 비슷한 얼룩새우는 다른 종이므로, 원료를 확인할 때는 국명보다 학명을 함께 보아야 한다[1]. 흰다리새우 계열 원료는 목록 학명이 'Litopenaeus vannamei / Penaeus vannamei'로 적혀 있다[1].\n\n"
"홍다리얼룩새우에는 더듬이에 띠무늬가 있는 형과 없는 형, 적어도 두 형태가 알려져 있다[6, 7]. 페르시아만의 두 형태를 비교한 연구에서는 25개 형태 형질 가운데 10개가 유의하게 달랐고, 16S rRNA와 COI 서열 차이가 각각 최대 6%, 17%에 이르러 저자들은 두 형태를 같은 곳에 사는 별개의 두 종으로 보자고 제안했다[7]. 이 제안이 분류학적으로 받아들여졌는지는 확인하지 못함.")

S["cultivation"] = ("어획·양식",
"사우디아라비아 홍해 연안의 새우 트롤 어업은 두 항구로 제한되며, 4–8월 금어기, 해안·섬에서 2해리 이내 트롤 금지, 자루그물 최소 그물코 38 mm 같은 관리 조치가 있다[3]. 논문이 인용한 사우디 환경·물·농업부 자료에서 2017–2023년 홍해 연안의 전체 새우 양륙량(모든 상업 종 합계)은 연 500–835톤, 평균 620톤이었다[3]. 같은 연구는 어획 비율이 암컷 0.63, 수컷 0.69이고 산란 자원량이 어획이 없을 때의 19%로 줄어 심한 남획 상태라고 판단하고, 어획 노력량을 절반으로 줄이는 방안을 제시했다[3].\n\n"
"양식 연구에서는 체중 0.27 g의 후기 유생에게 사료 1 g당 0.125–0.5 µg의 신경펩타이드 Y를 6주 먹이자 섭식량이 대조군보다 최대 1.3배 늘었다[23]. 박하 잎 추출물을 사료 1 kg당 0.5–2 g 넣은 8주 시험에서는 성장 차이가 없었고, 2 g 수준에서 슈퍼옥사이드 디스뮤타아제 활성이 높아졌다[24].\n\n"
"질병으로는 이집트 양식장 120마리에서 감염성 근괴사 바이러스(IMNV)와 감염성 피하·조혈조직 괴사 바이러스(IHHNV)가 각각 37.5%, 25% 검출되었다[20]. 흰반점증후군 바이러스(WSSV)를 염분 5–35 g/L에서 감염시킨 실험도 있다[21]. 국내 어획·양식 통계는 확인하지 못함.")

S["processing"] = ("가공·이용",
"사우디아라비아 리야드 수산시장의 신선 새우(평균 길이 8 cm)를 염장, 굽기(10분), 튀기기(7분), 삶기(15분)로 처리해 비교한 연구에서는 조리가 수분을 줄이고 지방·단백질·회분 비율을 높였다[25]. 비타민 C는 굽거나 튀기면 절반으로, 삶으면 4분의 3 정도 줄었고, 비타민 B1·B2·B12도 처리한 모든 시료에서 신선 시료보다 낮았다[25]. 신선 새우의 ω6 지방산 합계는 98.81 mg/100 g, ω6/ω3 비는 0.42였다[25].\n\n"
"알로에 베라 겔 75%·100% 용액으로 코팅한 새우는 4 °C 7일 저장 동안 지질 산화와 드립 손실이 잘 억제되었지만 25% 코팅은 효과가 부족했다[26].\n\n"
"껍데기 등 가공 부산물은 카로티노이드 원료로 연구되었다[27, 28]. 껍데기 분말에서 석유에테르·아세톤·물(15:75:10) 혼합 용매와 초음파를 쓴 최적 조건의 아스타잔틴 추출량은 51.5 µg/g이었다[27]. 부산물에서 효소(알칼라아제)로 뽑은 카로티노이드 추출물은 243 mg/kg으로 알칼리 처리(170 mg/kg)보다 많았고, 해바라기유에 470 ppm 넣으면 합성 산화방지제 BHA·BHT를 넣은 기름보다 과산화물가가 낮았다[28]. 고시형 원료 글루코사민·N-아세틸글루코사민·키토산의 원재료가 '갑각류(게, 새우 등)의 껍질'로 정해져 있으나[2], 이 종의 껍질이 실제로 쓰이는지는 확인하지 못함.")

S["genetics"] = ("유전 정보",
"홍다리얼룩새우의 미토콘드리아 유전체는 16,002 bp(A+T 68.6%)이며 단백질 암호 유전자 13개, tRNA 22개, rRNA 2개의 37개 유전자와 조절 영역으로 이루어져 있다[6]. 인도-태평양 15개 지점 284마리의 COI 548 bp와 조절 영역 571 bp를 분석한 연구에서는 말라카 해협 중부 바간파시르 부근을 경계로 두 계통이 나뉘었고, 지점 간 유전 거리는 COI 0.1–7.2%, 조절 영역 2.3–21.7%였다[5]. 저자들은 두 계통 모두 유전 다양성이 높아 어업 관리와 양식 계획에서 고려해야 한다고 보았다[5].\n\n"
"더듬이 띠무늬 유무로 나뉘는 두 형태는 16S rRNA·COI 계통수에서 뚜렷이 다른 두 무리로 갈렸다[7]. 난소에서 비텔로제닌 cDNA 두 개(7,920·2,068 뉴클레오타이드), 간췌장에서 한 개(7,920 뉴클레오타이드)가 해독되었고, 약 7.8 kb 전사체는 암컷의 난소와 간췌장에서만 검출되었다[31]. 수컷에도 비텔로제닌 유전자는 있었다[31]. 핵 유전체 전체 해독 결과는 이 조사에서 확인하지 못함.")

S["safety"] = ("안전성",
"이 종은 조건 없는 '사용가능' 수산물이며 고시 섭취 시 주의사항은 없다[1]. 새우 껍질로 만든 글루코사민·키토산 등에는 '게 또는 새우에 알레르기가 있는 사람은 섭취에 주의'가 붙는다[2]. 이 종의 알레르겐(트로포미오신 등)을 직접 분석한 연구와 국내 공공기관의 이 종 안전 안내는 확인하지 못함.\n\n"
"튀르키예 동지중해 근육(습중량)의 총비소는 1.83–5.66 mg/kg, 납은 0.467–0.708 mg/kg으로 일부 시료가 EU 갑각류 납 기준(0.50 mg/kg)을 넘었고, 수은은 0.001–0.009 mg/kg이었다[9]. 같은 해역의 2016년 시료에서는 추정 무기비소의 위해지수가 1을 넘었으나[12], 서아라비아만 해산물에서 무기비소는 총비소의 평균 0.03%, 무독성 아르세노베타인은 81%였다[13]. 사우디 동부 연안에서는 하루 42 g 고섭취자의 발암 위해가 기준을 넘었다[11]. 수은은 몸이 클수록, 암컷에서 높았고[14], 무사 하구 개체의 간췌장에서 0.95 µg/g까지 나왔다[15]. 페르시아만 북부 근육에서는 아연 300.88, 니켈 6.82, 납 1.10 µg/g(습·건중량 기준은 초록에 없음)이 측정되어 FAO/WHO 허용치를 넘었다고 보고되었다[10]. 이 종을 포함한 페르시아만 해산물의 과불화화합물은 건중량 2.3–6.1 ng/g으로, 어린이에게는 위해 가능성이 제기되었다[17].\n\n"
"위장관에서는 개체당 평균 0.47개의 미세플라스틱이 나왔고 90%가 섬유였고[19], 무사 하구 개체에서는 껍데기와 근육에서도 미세플라스틱이 나왔다[18]. 렉틴·헤모시아닌·크러스틴의 항균 활성은 시험관 결과다[33–35].")

order = ["overview","history","biology","related_species","cultivation","processing","genetics","safety"]
sections = [{"key": k, "title": S[k][0], "body": S[k][1]} for k in order]

compounds = [
 {"name": "Astaxanthin", "name_ko": "아스타잔틴", "class": "케토카로티노이드", "role": "bioactive", "part": "껍데기(가공 부산물)",
  "content_text": "51.5 µg/g(초음파 보조 추출 최적 조건, 전문 본문 값; 초록에는 '51.5%'로 적힘) [27]",
  "activity_ko": "추출물의 FRAP 1705 µmol/g, DPPH 소거율 73.9%로 아스타잔틴 함량과 산화방지 활성이 함께 움직였다(시험관)[27]", "source": [27]},
 {"name": "Carotenoids", "name_ko": "총 카로티노이드", "class": "카로티노이드", "role": "bioactive", "part": "가공 부산물(머리·껍데기)",
  "content_text": "효소(알칼라아제) 추출 243 mg/kg, 알칼리 처리 170 mg/kg [28]",
  "activity_ko": "해바라기유에 470 ppm 넣었을 때 BHA·BHT보다 과산화물가 상승을 더 잘 억제했다(식용유 산화 시험)[28]", "source": [28]},
 {"name": "Vitellogenin", "name_ko": "비텔로제닌", "class": "난황 전구 당지단백질", "role": "bioactive", "part": "암컷 혈림프·난소·간췌장",
  "content_text": "혈림프 농도 평균 50 → 439 µg/mL(난소 발달 중) [32]; cDNA 7,920 뉴클레오타이드 [31]",
  "activity_ko": "난소 안에서도 유전자가 발현·합성되어 난황 단백질 비텔린이 된다[31]", "source": [31, 32]},
 {"name": "Phosphatidylcholine", "name_ko": "포스파티딜콜린", "class": "인지질", "role": "nutrient", "part": "난소",
  "content_text": "난소 인지질의 75–80%(포스파티딜에탄올아민 20–25%) [29]",
  "activity_ko": "난모세포 성숙 동안 트라이아실글리세롤과 함께 난소에 쌓였다[29]", "source": [29]},
 {"name": "Triacylglycerols", "name_ko": "트라이아실글리세롤", "class": "중성지질", "role": "nutrient", "part": "난소",
  "content_text": "난모세포 발달 말기 약 16 mg/g 단백질(인지질과 거의 같은 양) [29]",
  "activity_ko": "인지질·트라이아실글리세롤 지방산의 약 30%가 다가불포화지방산이었다[29]", "source": [29]},
 {"name": "Eicosapentaenoic acid", "name_ko": "에이코사펜타엔산(EPA, 20:5ω3)", "class": "n-3 다가불포화지방산", "role": "nutrient", "part": "혈림프 고밀도 지단백질",
  "content_text": "지단백질의 인지질·다이아실글리세롤에 포함(함량 값은 초록에 없음) [30]",
  "activity_ko": "먹이나 간췌장에서 난소 등 조직으로 운반되는 고도불포화지방산으로 해석되었다[30]", "source": [30]},
 {"name": "Docosahexaenoic acid", "name_ko": "도코사헥사엔산(DHA, 22:6ω3)", "class": "n-3 다가불포화지방산", "role": "nutrient", "part": "혈림프 고밀도 지단백질",
  "content_text": "지단백질의 인지질·다이아실글리세롤에 포함(함량 값은 초록에 없음) [30]",
  "activity_ko": "EPA와 함께 고밀도 지단백질로 운반된다[30]", "source": [30]},
 {"name": "Cholesterol", "name_ko": "콜레스테롤", "class": "스테롤", "role": "nutrient", "part": "혈림프 고밀도 지단백질",
  "content_text": "고밀도 지단백질 총지질의 17–20%(인지질 71–76%) [30]",
  "activity_ko": "조리 비교 연구에서 굽거나 삶은 새우살은 신선 시료보다 콜레스테롤이 유의하게 낮았다[25, 30]", "source": [25, 30]},
 {"name": "Hemocyanin", "name_ko": "헤모시아닌", "class": "구리 함유 호흡 단백질", "role": "bioactive", "part": "혈림프",
  "content_text": "그람양성·음성 시험균에 대한 최소 억제 농도 50 µg/mL [34]",
  "activity_ko": "응집·항균·생물막 억제 활성을 보였다(시험관·컴퓨터 모의 결과)[34]", "source": [34]},
 {"name": "Lectin", "name_ko": "렉틴(Ps-Lec)", "class": "만노스 결합 당단백질", "role": "bioactive", "part": "혈림프",
  "content_text": "SDS-PAGE 37·118 kDa 소단위 [33]",
  "activity_ko": "세균·적혈구 응집과 칸디다 응집, 페놀옥시다아제 활성화를 보였다(시험관)[33]", "source": [33]},
 {"name": "Crustin", "name_ko": "크러스틴(WAP 도메인 항균 펩타이드)", "class": "항균 펩타이드", "role": "bioactive", "part": "개체 추출물",
  "content_text": "약 14 kDa; Bacillus thuringiensis 4 µg/mL, B. pumilus 6 µg/mL에서 항균 활성 [35]",
  "activity_ko": "그람양성균에 상대적으로 강했고 생물막 형성을 억제했다(시험관)[35]", "source": [35]},
 {"name": "Selenium", "name_ko": "셀레늄", "class": "필수 미량원소", "role": "nutrient", "part": "복부 근육(습중량)",
  "content_text": "보지야지 0.312–0.374 mg/kg, 이스켄데룬 0.551–0.658 mg/kg [9]",
  "activity_ko": "모든 시료에서 셀레늄이 수은보다 몰 기준으로 많아 저자들은 수은 위해를 상쇄하는 것으로 해석했다[9]", "source": [9]},
 {"name": "Zinc", "name_ko": "아연", "class": "필수 미량원소", "role": "nutrient", "part": "복부 근육(습중량)",
  "content_text": "8.977 µg/g(페르시아만, 2002년) [16]; 최고 16.44 mg/kg(튀르키예, 2025년) [9]",
  "activity_ko": "암컷이 수컷보다 아연이 유의하게 높았다(페르시아만 시료)[16]", "source": [9, 16]},
 {"name": "Copper", "name_ko": "구리", "class": "필수 미량원소", "role": "nutrient", "part": "복부 근육(습중량)",
  "content_text": "3.418 µg/g(페르시아만) [16]; 2.69–8.32 mg/kg(튀르키예) [9]",
  "activity_ko": "간췌장 평균 15.939 µg/g으로 근육보다 높았다[16]", "source": [9, 16]},
]

assays = [
 {"role": "literature", "compound": "Astaxanthin", "compound_ko": "아스타잔틴", "part": "껍데기(가공 부산물) 분말",
  "content": "51.5 µg/g(최적 조건, 전문 본문); 초록은 '51.5%', 최적 온도 26.3 °C로 적어 본문(28.3 °C)과 다름 [27]",
  "method": "용매 추출 후 자외선-가시광 분광광도법(470 nm)",
  "conditions": {"instrument": "분광광도계(모델 원문에 없음); 초음파 처리기 최대 400 W·20 kHz", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "",
   "detection": "헥세인 3 mL에 녹여 470 nm 흡광도, 흡광계수 2100으로 환산", "injection": "",
   "sample_prep": "껍데기를 분쇄해 425 µm 체로 거름; 10 g + 석유에테르·아세톤·물(15:75:10) 40 mL(1:4 w/v), 초음파 진폭 23.62%·13.9분·28.3 °C 처리 후 속실렛 6시간, 회전 증발 농축, 동결건조(−55 °C, 48시간)",
   "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "이 종 껍데기의 대표 색소로 정량되었고, 추출물의 산화방지 활성과 함께 움직였다. 크로마토그래피 분리 없이 총흡광으로 계산했으며 검출·정량한계와 회수율은 원문에 없다[27].",
  "source": [27], "url": "https://doi.org/10.1016/j.ultsonch.2021.105666", "source_kind": "paper"},
 {"role": "literature", "compound": "Arsenic, lead, mercury, selenium and other elements (12 elements)", "compound_ko": "비소·납·수은·셀레늄 등 12개 원소", "part": "복부 근육(습중량, 성별·지점별 15마리 혼합 시료)",
  "content": "총비소 1.83–5.66 mg/kg, 납 0.467–0.708 mg/kg, 수은 0.001–0.009 mg/kg, 카드뮴 0.014–0.041 mg/kg, 코발트 불검출 [9]",
  "method": "마이크로파 산분해 + ICP-MS(STD·KED 모드)",
  "conditions": {"instrument": "ICP-MS(PerkinElmer NexION 350X), 동심 분무기·사이클론 분무실·니켈 콘", "column": "", "mobile_phase": "", "gradient": "",
   "flow": "플라즈마 기체 18.0 L/min, 보조 기체 1.2 L/min, 분무 기체 0.68 L/min, 시료 흡입 1 mL/min", "temp": "",
   "detection": "RF 1500 W; 표준(STD) 모드와 헬륨 충돌 기체 운동에너지 판별(KED) 모드", "injection": "",
   "sample_prep": "근육 약 250 mg(습중량) + 65% 질산 5 mL + 37% 염산 1 mL, 10–15분 개방 탈기 후 마이크로파 분해(Berghof MSW-4), 초순수로 10 mL 정용, 필요 시 추가 희석; 절차 공시험 병행",
   "standard": "다원소 표준용액 검량선", "linearity": "상관계수 0.999 초과(모든 원소)",
   "lod": "공시험 표준편차의 3배(값은 원문 표에 있음, 이 조사에서 수치 확인하지 못함)", "loq": "공시험 표준편차의 10배",
   "recovery": "인증표준물질 NIST 2976(홍합 조직) 회수율 '허용 범위 이내'(수치는 확인하지 못함)"},
  "rationale": "이 종은 함량 지표성분이 정해져 있지 않으나, 식용 근육의 유해 원소와 셀레늄을 함께 정량해 위해·편익을 평가한 전문 공개 연구다[9].",
  "source": [9], "url": "https://doi.org/10.3390/life16030487", "source_kind": "paper"},
 {"role": "literature", "compound": "Fatty acids (FAME profile)", "compound_ko": "지방산 조성", "part": "새우살(신선·염장·굽기·튀기기·삶기)",
  "content": "신선 Σω6 98.81 mg/100 g, 염장 101.32 mg/100 g, 신선 Σω6/Σω3 0.42; 개별 지방산 표 값은 전문 텍스트에서 확인하지 못함 [25]",
  "method": "BF3-메탄올 메틸에스테르화 + GC-MS",
  "conditions": {"instrument": "가스크로마토그래프(Agilent 7890A) + 질량선택검출기(5975C)", "column": "SP-2560(100 m × 0.25 mm, 막두께 0.2 µm)",
   "mobile_phase": "", "gradient": "오븐 140 °C → 240 °C, 4 °C/min", "flow": "", "temp": "",
   "detection": "질량선택검출기; 머무름 시간을 표준 혼합물과 비교해 동정", "injection": "1 µL(원문 표기 '1 mL'), 다이클로로메테인에 녹여 주입",
   "sample_prep": "추출 지방 50 mg + 0.5 M NaOH-메탄올 5 mL 5분 끓임, 12% BF3-메탄올 4 mL 넣고 25분 다시 끓인 뒤 아이소옥테인 2 mL로 분리",
   "standard": "FAME 혼합 표준품(Supelco 47885-U)", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "이 종 새우살의 조리 방법별 지방산 변화를 정량했다. 원문 주입량은 '1 mL'로 인쇄되어 있어 오기 가능성이 있고, 검출·정량한계와 회수율은 원문에 없다[25].",
  "source": [25], "url": "https://doi.org/10.1016/j.sjbs.2021.09.029", "source_kind": "paper"},
]

d = {
 "slug": "penaeus-semisulcatus", "name_ko": "홍다리얼룩새우", "name_en": "Green tiger prawn",
 "scientific_name": "Penaeus semisulcatus",
 "aliases": ["Green tiger prawn", "Green tiger shrimp", "Grooved tiger prawn", "Penaeus semisulcatus De Haan, 1844"],
 "sections": sections, "compounds": compounds, "markers": [], "assays": assays,
 "nutrients": [], "production": [], "world": [], "gi": [], "orgs": [], "sources": sources,
}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in sections: print(s["key"], len(s["body"]))
