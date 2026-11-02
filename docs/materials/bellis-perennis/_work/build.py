import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
A = "2026-11-02"
def pm(pmid): return f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
def pmc(p): return f"https://pmc.ncbi.nlm.nih.gov/articles/{p}/"
S = [
 (1, "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 데이지잎(Bellis perennis L. / Bellis integrifolia DC.)", "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "식품의약품안전처", "2026-10-13"),
 (2, "(Bio)active Compounds in Daisy Flower (Bellis perennis). Molecules. 2023;28(23):7716", pmc("PMC10707873"), "Molecules (PubMed Central)", A),
 (3, "Insulin Mimetic Properties of Extracts Prepared from Bellis perennis. Molecules. 2018;23(10):2605", pmc("PMC6222741"), "Molecules (PubMed Central)", A),
 (4, "Seasonal variation in total phenolic and flavonoid contents and DPPH scavenging activity of Bellis perennis L. flowers. Molecules. 2010;15(12):9450-61", pmc("PMC6259450"), "Molecules (PubMed Central)", A),
 (5, "The genome sequence of the daisy, Bellis perennis L. (Asterales: Asteraceae). Wellcome Open Res. 2026;11:798", pmc("PMC13653108"), "Wellcome Open Research (PubMed Central)", A),
 (6, "Qualitative and quantitative chromatographic investigation of flavonoids in Bellis perennis L. Acta Pol Pharm. 2001;58(5):401-4 (초록)", pm("11876448"), "Acta Poloniae Pharmaceutica (PubMed)", A),
 (7, "Phylogenetic position of Mediterranean Astereae and character evolution of daisies (Bellis, Asteraceae) inferred from nrDNA ITS sequences. Mol Phylogenet Evol. 2002;25(1):157-71 (초록)", pm("12383758"), "Molecular Phylogenetics and Evolution (PubMed)", A),
 (8, "Antimicrobial activity of polyacetylenes from Bellis perennis and their synthetic derivatives. Planta Med. 1997;63(6):503-7 (초록)", pm("9434600"), "Planta Medica (PubMed)", A),
 (9, "Perennisosides I-VII, acylated triterpene saponins with antihyperlipidemic activities from the flowers of Bellis perennis. J Nat Prod. 2008;71(5):828-35 (초록)", pm("18363378"), "Journal of Natural Products (PubMed)", A),
 (10, "Oleanane-type triterpene saponins with collagen synthesis-promoting activity from the flowers of Bellis perennis. Phytochemistry. 2015;116:203-212 (초록)", pm("26028520"), "Phytochemistry (PubMed)", A),
 (11, "Acylated oleanane-type triterpene saponins from the flowers of Bellis perennis show anti-proliferative activities against human digestive tract carcinoma cell lines. J Nat Med. 2016;70(3):435-51 (초록)", pm("27178360"), "Journal of Natural Medicines (PubMed)", A),
 (12, "The evaluation of topical administration of Bellis perennis fraction on circular excision wound healing in Wistar albino rats. Pharm Biol. 2012;50(8):1031-7 (초록)", pm("22775421"), "Pharmaceutical Biology (PubMed)", A),
 (13, "The effect of the homeopathic remedies Arnica montana and Bellis perennis on mild postpartum bleeding — a randomized, double-blind, placebo-controlled study — preliminary results. Complement Ther Med. 2005;13(2):87-90 (초록)", pm("16036165"), "Complementary Therapies in Medicine (PubMed)", A),
 (14, "UDP-glucuronic acid:anthocyanin glucuronosyltransferase from red daisy (Bellis perennis) flowers. J Biol Chem. 2005;280(2):899-906 (초록)", pm("15509561"), "Journal of Biological Chemistry (PubMed)", A),
 (15, "Effect of glucuronosylation on anthocyanin color stability. J Agric Food Chem. 2009;57(8):3149-55 (초록)", pm("19281238"), "Journal of Agricultural and Food Chemistry (PubMed)", A),
 (16, "[Seasonal changes in the hemolytic effects of the head of Bellis perennis L.] Ceska Slov Farm. 2003;52(1):39-41 (영문 초록)", pm("12685333"), "Ceska a Slovenska Farmacie (PubMed)", A),
 (17, "Traditional plants from Asteraceae family as potential candidates for functional food industry. Food Funct. 2021;12(7):2850-2873 (초록)", pm("33683253"), "Food & Function (PubMed)", A),
 (18, "Edible Flowers as a Source of Dietary Fibre (Total, Insoluble and Soluble) as a Potential Athlete's Dietary Supplement. Nutrients. 2022;14(12):2470", pmc("PMC9231144"), "Nutrients (PubMed Central)", A),
 (19, "Bellis perennis extract mitigates UVA-induced keratinocyte damage: Photoprotective and immunomodulatory effects. J Photochem Photobiol B. 2021;221:112247 (초록)", pm("34175580"), "Journal of Photochemistry and Photobiology B (PubMed)", A),
 (20, "Bellis perennis: a useful tool for protein localization studies. Planta. 2011;234(4):759-68 (초록)", pm("21626148"), "Planta (PubMed)", A),
 (21, "Outdoor ultraviolet polychromatic action spectra for growth responses of Bellis perennis and Cynosurus cristatus. J Photochem Photobiol B. 2000;59(1-3):64-71 (초록)", pm("11332892"), "Journal of Photochemistry and Photobiology B (PubMed)", A),
 (22, "Variations in ray flower numbers of Common Daisy (Bellis perennis L.) - the hidden cues of the Fibonacci order. PLoS One. 2026;21(8):e0348529 (초록)", pm("42607022"), "PLoS One (PubMed)", A),
 (23, "First Occurrence of a Rust Fungus on English Daisy (Bellis perennis) in North America. Plant Dis. 2001;85(5):562 (제목)", pm("30823150"), "Plant Disease (PubMed)", A),
 (24, "Isolation of an oleanane-type saponin active from Bellis perennis through antitumor bioassay-guided procedures. Pharm Biol. 2014;52(8):951-5 (초록)", pm("24617777"), "Pharmaceutical Biology (PubMed)", A),
 (25, "Bayogenin and asterogenic acid glycosides from Bellis perennis. Phytochemistry. 1992;31(7):2555-7 (초록)", pm("1368391"), "Phytochemistry (PubMed)", A),
 (26, "[The effect of biotic elicitors on the production of flavonoids in suspension cultures of Bellis perennis L.] Ceska Slov Farm. 1999;48(6):268-71 (영문 초록)", pm("10748744"), "Ceska a Slovenska Farmacie (PubMed)", A),
 (27, "The effects of oxidative stress on phenolic composition and antioxidant metabolism in callus culture of common daisy. Afr J Tradit Complement Altern Med. 2016;13(4):34-41 (초록)", pm("28852718"), "African Journal of Traditional, Complementary and Alternative Medicines (PubMed)", A),
 (28, "Chemical composition of the essential oil of different parts of Bellis annua L. (Asteraceae) collected in Sicily (Italy). Nat Prod Res. 2025;40(15):4654-4660 (초록)", pm("40844433"), "Natural Product Research (PubMed)", A),
 (29, "Triterpenoid saponins from Bellis sylvestris, I. Structures of the major deacylsaponins. J Nat Prod. 1994;57(9):1279-82 (제목)", pm("7798963"), "Journal of Natural Products (PubMed)", A),
 (30, "[Pharmaceutical food science: search for anti-obese constituents from medicinal foods — anti-hyperlipidemic saponin constituents from the flowers of Bellis perennis] Yakugaku Zasshi. 2010;130(5):673-8 (초록)", pm("20460863"), "Yakugaku Zasshi (PubMed)", A),
 (31, "Phytochemical profile and qualification of biological activity of an isolated fraction of Bellis perennis. Biol Res. 2013;46(3):231-8 (초록)", pm("24346069"), "Biological Research (PubMed)", A),
 (32, "First Report of Powdery Mildew Caused by Golovinomyces cichoracearum on English Daisy (Bellis perennis) in Italy. Plant Dis. 2008;92(3):484 (제목)", pm("30769702"), "Plant Disease (PubMed)", A),
 (33, "Biological activities of Bellis perennis volatiles and extracts. Nat Prod Commun. 2010;5(1):147-50 (초록)", pm("20184041"), "Natural Product Communications (PubMed)", A),
]
sources = [{"n": n, "title": t, "url": u, "publisher": p, "accessed": a} for n, t, u, p, a in S]

sec = {}
sec["overview"] = ("한눈에 보기",
"데이지(Bellis perennis L.)는 국화과(Asteraceae)의 여러해살이풀로, 짧은 뿌리줄기에서 잎이 뿌리 쪽에 모여 나는 로제트를 이루고, 잎 없는 꽃줄기 끝에 머리모양꽃차례가 하나씩 달린다[5]. 혀꽃은 흰색에서 분홍색, 때로 짙은 붉은색이고 대롱꽃은 노란색이며, 키는 최대 25 cm 정도다[2].\n\n"
"식품의약품안전처 「식품원료 목록」에서 데이지는 '데이지잎' 한 원료명으로 실린 사용가능 원료이고, 사용 조건은 '사용가능부위 : 잎'이다[1]. 목록에는 다른 이름 애기국화, 영어 이름 True daisy·English daisy, 학명 Bellis perennis L. 과 함께 Bellis integrifolia DC. 가 적혀 있다[1]. 꽃이나 뿌리를 원료명으로 한 행, 건강기능식품 고시형 원료의 원재료 기록은 목록에서 확인하지 못함.\n\n"
"성분 연구는 대부분 꽃을 대상으로 했으며, 2023년 리뷰는 약 310종의 성분을 정리하고 테르페노이드가 가장 큰 무리, 그다음이 폴리페놀이라고 했다[2]. 잎만 따로 분석한 자료는 적고, 꽃과 잎을 비교한 연구에서 플라보노이드 함량은 잎보다 꽃이 높았다[6]. 추출물의 항산화·혈당·지질·상처 치유 관련 결과는 세포·동물·달걀 배아 실험이며, 동종요법 시험을 빼면 사람 대상 연구는 없다고 정리되었다[2].")
sec["history"] = ("역사와 전통적 이용",
"데이지는 유럽에서 전통적으로 타박상·골절·상처를 다스리는 약초로 쓰였다고 기술된다[12]. 전통 의학에서는 두통·감기·위통·눈병·습진·종기·위염·설사·출혈·류머티즘·염증·상기도 감염 치료에도 쓰였다고 소개된다[24]. 꽃(약재명 Bellidis flos)은 이뇨제·거담제로 쓰이며 주요 성분은 사포닌이라고 기술되었다[16].\n\n"
"식용으로는 꽃과 어린 잎을 채소로 쓴다고 소개되었다[4]. 2023년 리뷰는 데이지 꽃이 수프·샐러드·디저트·전채 요리에 쓰였다고 적었다[2]. 스페인 북서부 민간요법에 쓰인 국화과 8종을 다룬 리뷰에서는 데이지를 주로 식품으로 먹지는 않지만 기능성 식품 원료 후보가 될 수 있는 식물로 다루었다[17]. 일본 연구진은 '약용 식품'에서 항비만 성분을 찾는 연구의 하나로 데이지 꽃의 항고지혈 사포닌을 정리했다[30].\n\n"
"데이지는 동종요법 재료로도 쓰이며, 출산 후 가벼운 출혈에 대한 무작위 이중맹검 위약대조 예비 시험이 보고되었다[13]. 2023년에는 네덜란드의 국화(國花)로 선정되었다[5]. 국내에서 잎을 먹거나 약으로 쓴 전통 기록은 확인하지 못함.")
sec["biology"] = ("식물학적 특징",
"데이지는 짧은 뿌리줄기에서 거꿀달걀꼴에 불규칙한 톱니가 있는 잎이 로제트로 나는 여러해살이풀이다[5]. 잎 없는 꽃줄기마다 머리모양꽃차례 하나가 달리며, 흰 혀꽃(흔히 분홍빛을 띰)과 노란 대롱꽃으로 이루어진다[5]. 꽃은 주로 3월부터 11월 무렵까지 오래 핀다[4].\n\n"
"원산지는 유럽에서 북아프리카, 서·중앙아시아와 마데이라이며, 남북아메리카·인도·남아프리카·동아시아·오스트레일리아 남동부·뉴질랜드 등 온대 지역에 널리 들어갔다[5]. 깎거나 방목이 잦은 풀밭과 열린 땅에 흔하고, 잔디깎이가 씨를 퍼뜨려 잔디밭·길가·목초지의 잡초로 친숙하며 해발 900 m 이상에서도 기록되었다[5].\n\n"
"독일 브란덴부르크 34개 집단 563개체를 센 조사에서 혀꽃 수는 대부분 34–56개였고 최빈값 42, 중앙값 46이었다[22]. 데이지 잎 표피 세포에는 기능하는 엽록체가 적당히 들어 있어 식물 세포 속 단백질 위치를 보는 실험 재료로 제안되었다[20]. 야외 자외선 실험에서는 313 nm 파장이 지상부·뿌리 건중량과 잎 확장을 가장 크게 억제했다[21].")
sec["related_species"] = ("근연종과 혼동 주의",
"핵 리보솜 ITS 염기서열 분석에서 데이지속(Bellis)과 Bellium 속은 하나의 자연 무리를 이루며, 데이지속 안은 B. perennis 무리, B. sylvestris 무리, 기저의 이배체 다년생 3종으로 나뉜다[7]. B. perennis 무리는 한해살이·여러해살이 5종으로 이배체·8배체·10배체가 섞여 있고 지중해 전역에 분포한다[7]. 데이지속은 14종으로 마카로네시아·북아프리카·유럽에서 중앙아시아·서히말라야에 분포한다고 정리되었다[28].\n\n"
"한해살이 근연종 Bellis annua 의 정유는 β-미르센(75.3%)과 헥사데칸알(45.7%)이 부위별 주성분으로 보고되어, 데이지 정유 자료와 구분해야 한다[28]. 남유럽의 B. sylvestris 에서도 트리테르펜 사포닌 구조가 따로 보고되었다[29]. 겹꽃 원예 품종 가운데 일부는 남유럽에 사는 더 큰 근연종과의 교잡에서 나왔을 수 있다고 한다[5].\n\n"
"식약처 「식품원료 목록」에서 데이지속 원료는 '데이지잎' 한 행뿐이다[1]. 자료를 볼 때는 학명이 Bellis perennis 인지 확인하고, 같은 속의 B. annua·B. sylvestris 성분 자료를 데이지 자료로 옮기지 않도록 주의해야 한다[7][28][29].")
sec["cultivation"] = ("재배와 수확",
"국내 재배 면적·생산량 통계는 통계청·농림축산식품부 자료에서 확인하지 못함. 꽃이 큰 원예 품종과 혀꽃이 대롱꽃을 대신한 겹꽃 품종이 화단용으로 널리 쓰인다[5]. 붉은 꽃 품종의 꽃잎에서는 안토시아닌을 만드는 효소가 연구되었다[14].\n\n"
"체코 세 지역에서 3–10월에 매달 거둔 꽃을 비교한 연구에서 총페놀·총플라보노이드 함량과 DPPH 소거 활성의 달별 차이는 작았고 일정한 경향이 없어, 꽃은 봄부터 가을까지 거두어도 품질이 비슷하다고 결론지었다[4]. 반면 꽃의 용혈 활성(사포닌 지표)은 3월에 가장 낮고 6–8월에 가장 높아 거두는 시기에 따라 달라졌다[16]. 잎의 수확 시기별 성분 변화 자료는 확인하지 못함.\n\n"
"북아메리카에서는 2001년에 데이지에서 녹병균이 처음 보고되었다[23]. 이탈리아에서는 Golovinomyces cichoracearum 에 의한 흰가루병이 데이지에서 보고되었다[32]. 세포 배양에서는 생물 유도제나 과산화수소 처리로 플라보노이드·페놀 생산이 늘었다는 보고가 있다[26][27].")
sec["processing"] = ("가공과 이용",
"연구용 추출물은 말린 식물체를 갈아 50% 에탄올로 초음파 추출하거나[3], 그늘에서 말린 꽃을 가루로 만들어 60% 에탄올 등으로 추출했다[4]. 잎 메탄올 추출물의 총페놀 함량은 10.60 g/100 g 으로 측정한 추출물 가운데 가장 높았다고 정리되었으나, 에틸아세테이트·부탄올 분획은 측정하지 않았다[2]. 지상부 물 추출물은 102.5 µg/mL 에서 DPPH 라디칼을 85.8% 소거했지만, 여러 병원균에 대한 뚜렷한 항균 효과는 없었다[33].\n\n"
"동결건조한 식용 꽃 12종을 비교한 연구에서 데이지 꽃잎은 국화과 초본 꽃들과 함께 총식이섬유·불용성 식이섬유가 많은 편이었고, 수용성 식이섬유도 많은 꽃으로 꼽혔다[18]. 이는 꽃잎 자료이며, 식품원료 사용부위인 잎의 영양 성분 자료는 확인하지 못함.\n\n"
"꽃 메탄올 추출물은 사람 진피 섬유아세포의 콜라겐 합성을 촉진했고, 분리한 사포닌 10종이 3–30 µM 에서 세포독성 없이 콜라겐 합성을 높였다[10]. 화장품 쪽에서는 데이지 추출물이 자외선 A 를 쬔 사람 각질형성세포의 생존율을 높이고 활성산소·IL-6 를 낮췄다는 세포 실험이 있다[19]. 붉은 데이지의 글루쿠론산 결합 안토시아닌은 빛에 대한 색 안정성이 좋아, 천연 색소 안정화에 응용할 가능성이 제시되었다[15]. 데이지를 원료로 한 국내 건강기능식품 생산실적은 확인하지 못함.")
sec["genetics"] = ("유전체와 육종",
"데이지의 염색체 수는 2n = 18 의 이배체로 널리 보고되었고, 영국 큐 왕립식물원 잔디밭 개체로 만든 염색체 수준 유전체는 9개 염색체로 조립되었다[5]. 유세포 분석으로 잰 유전체 크기(1C)는 1.78 pg(약 1,740 Mb)이고, k-mer 분석에서는 1,694.14 Mb, 이형접합도 2.38%, 반복서열 74.02%로 추정되었다[5].\n\n"
"첫째 반수체 조립은 1,602.72 Mb 로 93.94% 가 9개 염색체에 배정되었고, 스캐폴드 N50 은 176.96 Mb, 쌍떡잎식물 BUSCO 유전자 완전도는 95.7% 였다[5]. 미토콘드리아 유전체는 262.08 kb, 엽록체 유전체는 151.87 kb 로 조립되었다[5]. 두 반수체는 일부 염색체, 특히 5번 염색체에서 크게 달랐다[5].\n\n"
"붉은 데이지 꽃잎에서는 안토시아닌에 글루쿠론산을 붙이는 효소(BpUGAT, 54 kDa)가 정제·클로닝되었고, 이 유전자 전사체는 붉은 꽃잎에서만 특이적으로 검출되었다[14]. 데이지속 안에서는 배수성 변화와 한해살이화가 여러 번 따로 일어났다고 추정된다[7]. 국내 품종 등록이나 육종 자료는 확인하지 못함.")
sec["safety"] = ("안전성",
"식약처 「식품원료 목록」에서 데이지는 잎만 식품 원료로 쓸 수 있는 사용가능 원료로 실려 있으며, 다른 부위는 이 목록 행의 범위 밖이다[1]. 데이지 잎 섭취에 대한 사람 대상 안전성·독성 연구, 식약처·EFSA 등 공공기관의 알레르기·잔류 정보는 확인하지 못함.\n\n"
"데이지는 사포닌을 많이 함유하며[3], 꽃의 용혈 활성은 계절에 따라 4–6배까지 달라진다고 보고되었다[4][16]. 달걀 배아 실험에서 세 추출물(꽃·잎 혼합, 꽃)은 혈관 손상 같은 눈에 띄는 독성 징후를 보이지 않았고, 자가 제조 추출물은 장 상피 세포(Caco-2) 단층의 결합을 떨어뜨리지 않았다[3]. 생쥐에게 꽃 에탄올 추출물 50–150 mg/kg 을 14일간 먹인 실험과 잎 물 추출물 50–200 mg/kg 을 45일간 먹인 실험이 있으나, 이는 효능 시험이며 독성 평가 연구가 아니다[2].\n\n"
"국화과 식물 알레르기와 관련해 데이지 자체의 사례나 시험 근거는 PubMed 검색에서 확인하지 못함. 항산화·혈당·지질·항종양 관련 결과는 모두 세포·동물·달걀 배아 수준이므로 사람에게서 같은 효과를 기대할 근거는 아직 없다[2]. 동종요법 시험은 고도로 희석한 제제를 쓴 것이어서 식품으로 잎을 먹는 경우의 안전성 근거가 되지 않는다[13].")

sections = [{"key": k, "title": v[0], "body": v[1]} for k, v in sec.items()]

def C(name, ko, cls, role, part, content, act, src):
    return {"name": name, "name_ko": ko, "class": cls, "role": role, "part": part, "content_text": content, "activity_ko": act, "source": src}
compounds = [
 C("Chlorogenic acid", "클로로겐산", "하이드록시신남산", "marker", "꽃·잎 혼합 및 꽃 추출물", "추출물에서 가장 많은 하이드록시신남산, 2.69 mg/L(HPLC-MS)[3]", "GLUT4 이동을 유도하는 추출물의 후보 성분으로 제시(세포 실험)[3]", [3]),
 C("Apigenin 7-glucoside", "아피제닌-7-글루코사이드", "플라본 배당체", "marker", "꽃(잎에서도 검출)", "아피제닌-7-글루쿠로나이드와 합산 0.42 mg/L(추출액, 머무름 시간 겹침)[3]", "꽃에서 분리, 시험관 항산화·아세틸콜린에스테라아제 억제[31]", [2, 3, 31]),
 C("Apigenin 7-glucuronide", "아피제닌-7-글루쿠로나이드", "플라본 배당체", "bioactive", "꽃·잎", "아피제닌-7-글루코사이드와 합산 0.42 mg/L(추출액)[3]", "꽃·잎 클로로포름 추출물에서 보고[2]", [2, 3]),
 C("Quercitrin", "쿠에르시트린", "플라보놀 배당체", "bioactive", "꽃·잎 혼합 및 꽃 추출물", "추출물의 주 플라보놀, 0.1 mg/L[3]", "단독 활성 시험 없음[3]", [3]),
 C("Isorhamnetin 3-O-galactoside", "이소람네틴-3-O-갈락토사이드", "플라보놀 배당체", "bioactive", "꽃(잎에서도 보고)", "함량 확인하지 못함", "꽃에서 분리된 플라보놀 배당체[2]", [2]),
 C("Kaempferol 3-O-glucoside", "캠페롤-3-O-글루코사이드", "플라보놀 배당체", "bioactive", "꽃(잎에서도 보고)", "함량 확인하지 못함", "꽃에서 분리된 플라보놀 배당체[2]", [2]),
 C("Deca-4,6-diynoic acid", "데카-4,6-다이인산", "폴리아세틸렌", "bioactive", "지상부 정유", "지상부 정유의 주성분 중 하나[8]", "그람양성균에 평균 최소억제농도 0.35 mg/mL(시험관)[2][8]", [2, 8]),
 C("Methyl deca-4,6-diynoate", "메틸 데카-4,6-다이이노에이트", "폴리아세틸렌", "bioactive", "지상부 정유", "지상부 정유의 주성분 중 하나[8]", "이 성분 자체는 항균 활성을 보이지 않음[8]", [8]),
 C("Geranyl angelate", "게라닐 안젤레이트", "모노테르펜 에스터", "bioactive", "잎·꽃 정유", "함량 확인하지 못함", "잎·꽃 정유 성분으로 보고(활성 시험 없음)[2]", [2]),
 C("Perennisoside II", "페레니소사이드 II", "올레아난형 트리테르펜 사포닌", "bioactive", "꽃", "함량 확인하지 못함", "올리브유 부하 생쥐에서 25–50 mg/kg 경구로 혈청 중성지방 상승 억제[9]", [9]),
 C("Perennisaponin O", "페레니사포닌 O", "올레아난형 트리테르펜 사포닌", "bioactive", "꽃", "함량 확인하지 못함", "사람 위암 세포주 증식 억제 IC50 6.9–14.3 µM(세포 실험)[2][11]", [2, 11]),
 C("Bayogenin", "바요제닌", "트리테르펜(사포닌 비당체)", "bioactive", "땅속 부위", "함량 확인하지 못함", "땅속 부위에서 바요제닌·아스테로겐산 배당체 4종 분리[25]", [25]),
 C("Cyanidin 3-O-(2''-O-glucuronosyl)glucoside", "시아니딘-3-O-(2''-O-글루쿠로노실)글루코사이드", "안토시아닌", "bioactive", "붉은 품종의 꽃잎", "함량 확인하지 못함", "글루쿠론산 결합으로 빛에 대한 색 안정성이 높아짐[15]", [14, 15]),
]

assays = [
 {"role": "literature", "compound": "Chlorogenic acid", "compound_ko": "클로로겐산 등 폴리페놀 13종(플라보놀 7·플라본 3·하이드록시신남산 3)", "part": "꽃·잎 혼합 추출물(4404), 꽃 추출물(4407), 꽃 자가 제조 에탄올 추출물",
  "content": "클로로겐산 2.69 mg/L, 아피제닌-7-글루코사이드+아피제닌-7-글루쿠로나이드 0.42 mg/L, 쿠에르시트린 0.1 mg/L(추출액 농도)[3]",
  "method": "HPLC-DAD(260 nm), 동정·정량 HPLC-HRMS(오비트랩, ESI 음이온)",
  "conditions": {"instrument": "Thermo Dionex Ultimate 3000(LPG-3400SD 펌프, WPS-3000 자동주입기, DAD) + LTQ Orbitrap XL(Ion Max ESI, 음이온 모드)", "column": "Accucore C18, 150 × 3.0 mm, 2.6 µm", "mobile_phase": "A 0.1% 포름산 수용액, B 0.1% 포름산 아세토니트릴", "gradient": "B 5%(0–5분) → 20%(8분) → 40%(12분) → 60%(15분) → 80%(17분, 3분 유지) → 5%(20–25분)", "flow": "0.5 mL/min", "temp": "40 °C", "detection": "UV 260 nm; MS 모세관 온도 350 °C, 소스 전압 3.5 kV", "injection": "1 µL", "sample_prep": "실온 1주 건조 → 분쇄 → 분말 3 g + 50% 에탄올 30 mL, 초음파 20분 → 원심·여과 → 질소로 에탄올 제거 후 물에 재용해(자가 제조 추출물)", "standard": "루틴·하이퍼로사이드·이소쿠에르시트린·쿠에르시트린·쿠에르세틴·클로로겐산·네오클로로겐산·카페산·과이아베린·아비큘라린 등 표준품", "linearity": "1–1000 mg/L", "lod": "", "loq": "", "recovery": ""},
  "rationale": "연구진은 GLUT4 이동을 유도한 데이지 추출물의 폴리페놀을 동정·정량하고 이 성분들이 혈당 저하 작용에 기여할 수 있다고 보았다[3]. 표의 값이 세 추출물 중 어느 것인지는 본문에서 확인하지 못했고, 캠페롤·루테올린은 정량하지 못했다. 폴리페놀의 검출·정량한계와 회수율은 원문에 없어 비워 둠.",
  "source": [3], "url": pmc("PMC6222741"), "source_kind": "paper"},
 {"role": "literature", "compound": "Total flavonoids", "compound_ko": "총플라보노이드(쿠에르세틴·아피제닌-7-글루코사이드 환산)와 총페놀", "part": "꽃(머리모양꽃차례, 그늘 건조; 식품원료 사용부위 아님)",
  "content": "총플라보노이드 0.31–0.44 mg 쿠에르세틴 당량/100 mg 건물(방법 1), 1.37–2.20 mg 아피제닌-7-글루코사이드 당량/100 mg 건물(방법 2), 총페놀 2.81–3.57 mg 갈산 당량/100 mg 건물[4]",
  "method": "분광광도법(약전법 2종 + Folin-Ciocalteu)",
  "conditions": {"instrument": "분광광도계(Büchi 901)", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "방법 1: 염화알루미늄 착물 425 nm; 방법 2: 붕산·옥살산 반응 405 nm; 총페놀 765 nm", "injection": "", "sample_prep": "방법 1: 분말 0.600 g + 아세톤 20 mL·헥사메틸렌테트라민 1 mL·25% 염산 2 mL, 30분 환류 → 에틸아세테이트 추출; 방법 2: 분말 0.400 g + 60% 에탄올 40 mL, 60 °C 10분 × 2회", "standard": "쿠에르세틴, 아피제닌-7-글루코사이드, 갈산", "linearity": "쿠에르세틴 0.1–20 µg/mL(R² 0.9999), 아피제닌-7-글루코사이드 0.8–24 µg/mL(R² 0.9999), 갈산 1–5 µg/mL(R² 0.9997)", "lod": "", "loq": "", "recovery": ""},
  "rationale": "약전에 실린 총플라보노이드 정량법으로 3년간 세 지역의 꽃을 매달 비교해 품질 지표로 썼다[4]. 꽃 시료이므로 식품원료인 잎에 그대로 적용할 수 없다.",
  "source": [4], "url": pmc("PMC6259450"), "source_kind": "paper"},
 {"role": "literature", "compound": "Apigenin", "compound_ko": "산 가수분해 후 플라보노이드 비당체(아피제닌·쿠에르세틴·캠페롤·이소람네틴)", "part": "꽃·잎(야생) 및 원예 품종 꽃",
  "content": "꽃 HPLC 합계 0.23%(아피제닌 유도체 0.10%, 이소람네틴 0.019%, 쿠에르세틴 0.013%, 캠페롤 0.007%) — 선행 연구 값으로 인용됨[4]; 잎의 플라보노이드 함량은 꽃보다 낮음[6]",
  "method": "산 가수분해 후 HPLC, Christ-Müller 분광광도법, TLC",
  "conditions": {},
  "rationale": "꽃과 잎을 함께 정량한 드문 연구다[6]. 전문 확인 못함 — 칼럼·이동상 등 분석 조건과 잎의 수치는 초록에 없어 비워 둠.",
  "source": [4, 6], "url": pm("11876448"), "source_kind": "paper"},
]

d = {"slug": "bellis-perennis", "name_ko": "데이지", "name_en": "Common daisy (English daisy, True daisy)", "scientific_name": "Bellis perennis L.",
     "aliases": ["데이지잎", "애기국화", "English daisy", "True daisy", "Common daisy", "Lawn daisy", "Bellis integrifolia DC."],
     "sections": sections, "compounds": compounds, "markers": [], "assays": assays, "nutrients": [], "production": [], "world": [], "gi": [], "orgs": [], "sources": sources}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in sections: print(s["key"], len(s["body"]))
