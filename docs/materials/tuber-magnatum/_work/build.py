import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
A = "2026-11-02"
def pm(n, title, pmid, pmc=None):
    url = f"https://pmc.ncbi.nlm.nih.gov/articles/{pmc}/" if pmc else f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
    t = f"{title} (PMID {pmid}" + (f", {pmc})" if pmc else ")")
    return {"n": n, "title": t, "url": url, "publisher": "PubMed", "accessed": A}
I1020 = "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020"
sources = [
 {"n": 1, "title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 흰서양송로자실체(Tuber magnatum Pico, 이명 '송로버섯', 영문명 White Truffles, Bianco Truffles) (로컬 원자료 I1020_20261013.json 대조)", "url": I1020, "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
 {"n": 2, "title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 같은 속 항목: 송로버섯자실체·건조송로버섯·송로버섯오일 등(T. aestivum / T. melanosporum), 검은서양송로자실체(T. melanosporum), 대리석덩이버섯자실체(T. borchii), Winter truffle자실체(T. brumale), 검은덩이버섯(T. indicum, 사용불가) (로컬 원자료 대조)", "url": I1020, "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
 pm(3, "Identification of bis(methylsulfanyl)methane and furan-2(5H)-one as volatile marker compounds for the differentiation of the white truffle species Tuber magnatum and Tuber borchii. J Agric Food Chem 2024", "38630649", "PMC11066859"),
 pm(4, "Environmental conditions influence the biochemical properties of the fruiting bodies of Tuber magnatum Pico. Sci Rep 2018;8:7243", "29740145", "PMC5940868"),
 pm(5, "Characterization of the key aroma compounds in white Alba truffle (Tuber magnatum pico) and Burgundy truffle (Tuber uncinatum) by means of the sensomics approach. J Agric Food Chem 2017;65:9287-96", "28965409"),
 pm(6, "White Acqualagna truffle (Tuber magnatum Pico): evaluation of volatile and non-volatile profiles by GC-MS, sensory analyses and elemental composition by ICP-MS. Food Chem 2024;439:138089", "38070235"),
 pm(7, "Sustainable cultivation of the white truffle (Tuber magnatum) requires ecological understanding. Mycorrhiza 2023;33:291-302", "37462722", "PMC10752849"),
 pm(8, "First production of Italian white truffle (Tuber magnatum Pico) ascocarps in an orchard outside its natural range distribution in France. Mycorrhiza 2021;31:383-8", "33591428"),
 pm(9, "Genetic and phylogeographic structures of the symbiotic fungus Tuber magnatum. Appl Environ Microbiol 2005;71:6584-9", "16269685", "PMC1287743"),
 pm(10, "Reevaluation of the life cycle of Tuber magnatum. Appl Environ Microbiol 2006;72:2390-3", "16597935", "PMC1449033"),
 pm(11, "Pezizomycetes genomes reveal the molecular basis of ectomycorrhizal truffle lifestyle. Nat Ecol Evol 2018;2:1956-65", "30420746"),
 pm(12, "The changing ethnoecological cobweb of white truffle (Tuber magnatum Pico) gatherers in South Piedmont, NW Italy. J Ethnobiol Ethnomed 2016;12:18", "27091474", "PMC4836152"),
 pm(13, "No radioactive contamination from the Chernobyl disaster in Hungarian white truffles (Tuber magnatum). Environ Pollut 2019;252:1643-7", "31284206"),
 pm(14, "137Cs content in the fruit bodies of various Tuber species (T. magnatum, T. borchii, T. aestivum, T. excavatum). Health Phys 1996;71:956-9", "8919081"),
 pm(15, "Isotopic and elemental characterisation of Italian white truffle: a first exploratory study. Food Chem Toxicol 2020;145:111627", "32777342"),
 pm(16, "Effect of storage on biochemical and microbiological parameters of edible truffle species. Food Chem 2008;109:8-16", "26054259"),
 pm(17, "Gene expression and metabolite changes during Tuber magnatum fruiting body storage. Curr Genet 2014;60:285-94", "24981976"),
 pm(18, "Antioxidant profile and biosafety of white truffle (Tuber magnatum) mycelial products obtained by solid-state fermentation. Molecules 2021;27:109", "35011340", "PMC8746469"),
 pm(19, "Phenolic profile, antioxidant, anti-inflammatory and cytotoxic activities of black (Tuber aestivum Vittad.) and white (Tuber magnatum Pico) truffles. Food Chem 2014;165:460-6", "25038699"),
 pm(20, "Chemical composition and evaluation of antioxidant, antimicrobial and antiproliferative activities of Tuber and Terfezia truffles. Food Res Int 2021;140:110071", "33648293"),
 pm(21, "Italian white truffle (Tuber magnatum Pico): discovery of new molecules through untargeted UHPLC-QTOF-MS analysis. Food Chem 2025;477:143562", "40015022"),
 pm(22, "Occurrence and diversity of bacterial communities in Tuber magnatum during truffle maturation. Environ Microbiol 2007;9:2234-46", "17686021"),
 pm(23, "New evidence for nitrogen fixation within the Italian white truffle Tuber magnatum. Fungal Biol 2010;114:936-42", "21036337"),
 pm(24, "In vitro interactions between Bradyrhizobium spp. and Tuber magnatum mycelium. Environ Microbiol Rep 2024;16:e13271", "38692852", "PMC11062863"),
 pm(25, "Newly designed fluorescence in situ hybridization probes reveal previously unknown endophytic abilities of Tuber magnatum in herbaceous plants. Microb Ecol 2025;88:42", "40338317", "PMC12062114"),
 pm(26, "Molecular identification of Tuber magnatum ectomycorrhizae in the field. Microbiol Res 2006;161:59-64", "16338592"),
 pm(27, "Assessment of ectomycorrhizal fungal communities in the natural habitats of Tuber magnatum (Ascomycota, Pezizales). Mycorrhiza 2013;23:349-58", "23299664"),
 pm(28, "Development and validation of a real-time PCR assay for detection and quantification of Tuber magnatum in soil. BMC Microbiol 2012;12:93", "22672347", "PMC3438110"),
 pm(29, "Spatio-temporal dynamic of Tuber magnatum mycelium in natural truffle grounds. PLoS One 2014;9:e115921", "25535741", "PMC4275250"),
 pm(30, "Soil analysis reveals the presence of an extended mycelial network in a Tuber magnatum truffle-ground. FEMS Microbiol Ecol 2010;71:43-9", "19780830"),
 pm(31, "Identification of internal transcribed spacer sequence motifs in truffles: a first step toward their DNA bar coding. Appl Environ Microbiol 2007;73:5320-30", "17601808", "PMC1950968"),
 pm(32, "Food authentication: species and origin determination of truffles (Tuber spp.) by inductively coupled plasma mass spectrometry and chemometrics. J Agric Food Chem 2020;68:14374-85", "32520544"),
 pm(33, "Volatile organic compounds in truffle (Tuber magnatum Pico): comparison of samples from different regions of Italy and from different seasons. Sci Rep 2015;5:12629", "26224388", "PMC4519792"),
 pm(34, "Composition of commercial truffle flavored oils with GC-MS analysis and discrimination with an electronic nose. Food Chem 2014;146:30-5", "24176309"),
 pm(35, "Microbial and pigment profile of the reddish patch occurring within Tuber magnatum ascomata. Fungal Biol 2018;122:1134-41", "30449351"),
 {"n": 36, "title": "이탈리아 「Legge 16 dicembre 1985, n. 752」(신선·저장 송로의 채취·재배·거래 기본법) — Tuber magnatum 채취 기간 조항·주(州)의 달력 조정 권한. 원문 PDF(FAO 법령 DB·주정부 사본)는 이 환경의 네트워크 허용 목록 밖이라 열지 못했고 WebSearch 요약으로만 확인함", "url": "https://faolex.fao.org/docs/pdf/ita32041.pdf", "publisher": "이탈리아 정부(관보 1985년 제300호); WebSearch 요약", "accessed": A},
 {"n": 37, "title": "Tuber magnatum 원기재(Melethemata inauguralia, 1788)와 저자명 표기(Pico 대 Picco) — 'On the Tuber magnatum, Tuber albidum and Tuber rufum author name: Picco vs Pico'(AGRIS 서지)와 Plazi 분류 처리문. 원문은 이 환경에서 열지 못했고 WebSearch 요약으로만 확인함", "url": "https://agris.fao.org/search/en/records/675abc610ce2cede71cf6ee7", "publisher": "FAO AGRIS; WebSearch 요약", "accessed": A},
 pm(38, "Morphological, genetic, and microbiological characterization of Tuber magnatum Picco populations from 'Alto Molise', Central-Southern Italy. Microorganisms 2025;13:2340", "41156800", "PMC12565911"),
 pm(39, "Tuberomics: a molecular profiling for the adaption of edible fungi (Tuber magnatum Pico) to different natural environments. BMC Genomics 2020;21:90", "31996138", "PMC6988325"),
 pm(40, "Geographical-based variations in white truffle Tuber magnatum aroma is explained by quantitative differences in key volatile compounds. New Phytol 2021;230:1623-38", "33555031"),
]

S = {}
S["overview"] = ("한눈에 보기",
"흰서양송로(Tuber magnatum)는 땅속에 자실체를 만드는 덩이버섯속(Tuber)의 자낭균으로, 영어권에서는 이탈리아 흰 송로·피에몬테 흰 송로·알바 송로라고 부른다[3, 8, 11]. 식품의약품안전처 「식품원료 목록」에는 원료명 '흰서양송로자실체', 학명 'Tuber magnatum Pico', 영문명 'White Truffles, Bianco Truffles', 이명 '송로버섯'으로 올라 있다[1]. 상태는 '사용가능'이고 사용 조건은 '사용가능부위 : 자실체'여서 일반 식품 원료로는 자실체만 쓸 수 있다[1]. 목록상 분류는 '식품원료(A코드)'로, 건강기능식품 기능성 원료 고시에 오른 원료가 아니어서 고시 지표성분은 없다[1].\n\n"
"같은 목록에는 송로버섯(T. aestivum·T. melanosporum), 검은서양송로(T. melanosporum), 대리석덩이버섯(T. borchii), Winter truffle(T. brumale)이 따로 올라 있고, 검은덩이버섯(T. indicum)은 '사용불가'다[2]. 이명 '송로버섯'은 다른 송로 원료명과 겹치므로, 이 문서는 T. magnatum으로 확인된 자료만 쓴다[1, 2]. 흰서양송로는 송로 가운데 가장 비싼 종으로 꼽히며[7, 8], 2024년 1월 값이 2000–3000달러로 대리석덩이버섯(약 250–700달러)보다 훨씬 높았다고 적혀 있다(무게 기준은 원문에 없음)[3].")

S["history"] = ("이름과 이용의 역사",
"학명은 1788년 출판된 『Melethemata inauguralia』에서 처음 기재되었고, 명명자 표기는 'Pico'와 'Picco'가 함께 쓰인다는 정리가 있으나 원문은 열지 못해 검색 요약으로만 확인했다[37]. 식약처 목록은 'Pico'로 적는다[1]. 이탈리아 북서부 피에몬테 남부(랑게·로에로)에서는 '트리풀라우(trifulau)'라 불리는 채취인이 개와 함께 흰서양송로를 찾아 왔다[12]. 2010–2014년 채취인 34명 면담에서 나무·토양·기후에 관한 정교한 전통 생태 지식이 기록되었고, 채취인과 개의 긴밀한 관계가 성공의 열쇠로 꼽혔다[12]. 면담자들은 여름의 고온·건조, 젊은 채취인의 시장 지향, 포도밭 확대를 위협으로 들었다[12].\n\n"
"이탈리아 송로 기본법(1985년 법률 제752호)은 흰서양송로 채취 기간을 10월 1일부터 12월 31일까지로 정하고 주(州)가 달력을 조정할 수 있게 한 것으로 알려져 있으나, 원문은 열지 못해 검색 요약으로만 확인했다[36]. 국문명 '흰서양송로'의 유래와 국내 이용 역사는 확인하지 못함.")

S["biology"] = ("균학적 특징",
"흰서양송로는 활엽수 뿌리와 외생균근(뿌리를 감싸는 공생 구조)을 맺는 자낭균으로, 이탈리아와 발칸 일부에 띄엄띄엄 분포한다[9]. 남동유럽 231개 산지를 모은 연구에서 산지의 75%는 유명 산지인 피에몬테 밖에 있었고, 북위 약 37°(시칠리아)에서 약 47°(헝가리)까지 퍼져 있었다[7]. 산지는 겨울 평균기온 0.4 °C 초과, 여름 강수량 약 50 mm, 토양 pH 6.4–8.7을 보였고, 보고된 숙주 후보 26종 가운데 은백양(Populus alba)과 터키참나무(Quercus cerris)가 23.5%를 차지했다[7]. 자실체는 보통 2–6 cm(최대 15 cm)이고 겉은 매끈한 연한 황토색이며, 단면은 흰 맥이 있는 연갈색이다[3].\n\n"
"자실체 속 세균은 성숙도와 관계없이 알파프로테오박테리아가 주를 이뤘고, 자실체 안에서 질소고정 효소 활성도 측정되었다[22, 23]. 자실체에 흔히 생기는 붉은 반점에서는 카로티노이드(빅신·β-카로틴 등)가 검출되어 이를 만드는 세균이 원인으로 추정되었다[35]. 이 종은 타가교배하며 생활사의 대부분을 반수체로 지낸다[10]. 한 산지 토양에서는 균사가 생산 나무에서 100 m 떨어진 곳에서도 검출되었고, 초본인 사초(Carex pendula) 뿌리 안에서 균사가 확인되어 내생균으로 사는 첫 증거가 나왔다[25, 30].")

S["related_species"] = ("가까운 종과 혼동",
"흰서양송로와 대리석덩이버섯(T. borchii)은 겉모습이 비슷해 형태만으로는 개체를 확실히 가르기 어렵고, 값싼 대리석덩이버섯이 흰서양송로로 팔릴 위험이 크다[3]. 휘발성분 정량 연구에서 흰서양송로 진품 13점의 비스(메틸설파닐)메탄은 237 ± 27 – 4360 ± 260 μg/kg이었고 대리석덩이버섯 진품 6점에서는 검출되지 않아(이론상 56 μg/kg 미만), 이 성분이 흰서양송로의 지표로 제시되었다[3]. 반대로 푸란-2(5H)-온은 흰서양송로에서 137 ± 23 – 487 ± 25 μg/kg으로 대리석덩이버섯보다 일관되게 낮았다[3].\n\n"
"ITS 부위의 짧은 종 특이 서열 모티프로 흰서양송로·검은서양송로·T. indicum·T. aestivum·T. mesentericum을 가리는 DNA 바코드가 제안되었다[31]. 원소 조성(ICP-MS)과 통계 모형으로도 흰서양송로를 조사한 다른 상업 송로 종과 구분할 수 있었다[32]. 흰서양송로가 잘 나는 이탈리아 중부 산지의 균근 335개를 분자 동정했더니 흰서양송로 균근은 4.4% 미만이었고, 다른 송로인 T. maculatum(48.9%)과 T. rufum(19.0%)이 훨씬 많았다[26]. 중국산 송로(T. indicum)는 국내 목록에서 '사용불가'다[2].")

S["cultivation"] = ("채취와 재배",
"흰서양송로는 오랫동안 유럽의 자연 산지에서만 나와 수요를 채우지 못했다[8]. 1970년대부터 재배를 시도했으나 실패했고, 최근에야 균근 묘목 생산에 성공했다[8]. 프랑스의 묘목 재배지 5곳에서 균사는 심은 뒤 3–8년 동안 토양에 남아 있었고, 한 곳에서는 심은 지 4.5년 만인 2019·2020년에 자실체가 수확되어 자연 분포 밖 첫 생산으로 보고되었다[8]. 균사는 혼자서는 무균 배양이 잘 되지 않았지만 새로운 브라디리조비움 세균과 함께일 때 처음으로 꾸준히 자랐다[24].\n\n"
"자연 산지에서 이 종의 균근은 매우 드물어, 이탈리아 네 지역 산지에서 뿌리 끝 8,100개를 세었지만 흰서양송로 균근은 찾지 못했다[27]. 그래서 토양 균사를 실시간 PCR로 재는 방법이 개발되었고, 균사 DNA 농도는 생산 구획에서 더 높았으며 3년간 자실체 생산과 상관이 있었다[28]. 균사는 이른 봄에 많고 여름에 크게 줄었다가 가을에 다시 늘어 자실체가 날 자리 주변에 모였다[29]. 헝가리 남부에서는 해마다 최대 600 kg의 신선 자실체가 채취된다[13]. 몰리세주는 이탈리아 송로, 특히 흰서양송로의 주요 산지로 전국 생산량의 약 40%를 차지한다고 적혀 있다[38]. 국내 재배·생산 통계는 확인하지 못함.")

S["processing"] = ("가공과 이용",
"흰 송로는 보통 익히지 않고 얇게 썰어 리소토·파스타·오믈렛 같은 완성된 요리 위에 얹는다[3]. 알바산 흰서양송로의 향기 추출물 희석 분석에서 3-(메틸티오)프로판알(감자 냄새), 2-·3-메틸부탄알(맥아 냄새), 2,3-부탄디온(버터 냄새), 비스(메틸티오)메탄(마늘 냄새)의 희석 배수가 가장 높았다[5]. 동위원소 희석 정량으로 구한 향 활성값(농도/냄새 역치)은 비스(메틸티오)메탄·3-메틸부탄알·1-피롤린에서 1000을 넘었다[5]. 아콸라냐산 자실체의 휘발성분은 비스(메틸티오)메탄이 78.72%를 차지했다[6]. 네 나라 산지를 비교한 연구는 향 차이가 산지보다 개체 특성에 더 크게 달려 있다고 보았다[40].\n\n"
"저장 비교에서 4 °C 보관이 신선 송로의 생화학·미생물 특성을 가장 잘 지켰고, 흰 송로는 검은 송로보다 생화학적 변질에 약했지만 미생물 변질에는 흰서양송로가 가장 강했다[16]. 4 °C 저장 중에도 세포벽 대사·라카아제 유전자 발현이 늘고 처음 3일 안에 리놀레산 유래 대사물이 바뀌었다[17]. 시판 송로 향 올리브유 18점에서는 출처가 의심스러운(합성 또는 분해 유래) 성분 12종이 나왔고, 검은 송로 향 제품에 비스(메틸티오)메탄을 쓰는 관행이 확인되었다[34]. 흰서양송로 균사를 콩·율무 배지에 고체 발효한 제품이 비싼 자실체를 대신할 재료로 연구되었다[18]. 국내 제품 생산실적은 확인하지 못함.")

S["genetics"] = ("유전체와 유전 다양성",
"미세부수체 마커로 26개 집단의 표본 316개를 분석한 결과, 최남단과 북서단 집단이 나머지와 유전적으로 구별되었고 야외 집단의 광범위한 타가교배가 처음 확인되었다[9]. 이 유전 구조는 산지 추적에 쓸 수 있을 것으로 제시되었다[9]. 한 자실체의 자낭과 주변 균사, 그 자실체로 접종한 균근을 비교한 연구는 생활사의 대부분이 반수체라는 직접 증거를 냈다[10]. ITS 서열 분석으로 산미니아토 산지에서는 한 해 두 시기에 자실체가 생긴다는 점이 확인되었다[33].\n\n"
"흰서양송로·검은서양송로·T. aestivum 등의 유전체 비교에서 송로 유전체는 전이인자가 많고 리그노셀룰로스 분해 효소 유전자가 적으며, 휘발성분 대사 유전자의 발현이 높다는 특징을 공유했다[11]. 흰서양송로와 검은서양송로는 약 1억 년 전에 갈라졌는데도 균근과 자실체의 발달·대사 경로가 매우 비슷했다[11]. 송로의 톡 쏘는 향은 새 유전자가 아니라 기존 유전자의 발현 차이에서 나온다고 해석되었다[11]. 북부·중부·남부 이탈리아 자실체를 단백체·RNA-seq으로 비교한 연구는 산지를 가르는 단백질을 찾았고, RNA-seq으로도 산지 구분이 가능해 황 대사 유전자 분석의 기초를 마련했다[39]. 흰서양송로 유전체 크기와 유전자 수는 초록에 없어 확인하지 못함.")

S["safety"] = ("안전성",
"식약처 「식품원료 목록」에서 흰서양송로 자실체는 '사용가능' 원료다[1]. 이 종에 대한 공공기관(식약처·EFSA 등)의 별도 독성·알레르기 평가는 확인하지 못함. 이탈리아 여러 산지와 크로아티아산 자실체의 원소 분석(Cd·Cr·Ni·Pb 등 포함)에서 독성·잠재 독성·알레르기 유발 원소는 모두 법정 한도보다 낮았다[15]. 헝가리 남부 자실체 10개의 세슘-137은 의미 있는 수준이 아니었다[13]. 이탈리아 세 지역 송로 네 종(이 종 포함)의 세슘-137은 생체중 기준 2.5–33.3 Bq/kg으로(네 종을 합친 범위), 저자들은 방사선상 우려가 없다고 보았다[14].\n\n"
"자실체 1 g에는 배양 가능한 세균이 미성숙 단계 (4.17 ± 1.61) × 10^7 cfu, 성숙 단계 (1.86 ± 1.32) × 10^6 cfu 있었다[22]. 메탄올 추출물이 일부 암세포주에 세포독성을 보이고 COX-1·12-LOX 경로 산물 생성을 줄였다는 결과는 시험관 실험이며 사람 효과는 확인되지 않았다[19]. 고체 발효 균사 제품을 쥐에게 90일 먹인 시험에서는 3000 mg/kg 체중/일 한 용량에서 이상이 없어 NOAEL로 보고되었지만, 자실체가 아니라 균사와 배지(콩·율무)의 혼합물 결과다[18].")

compounds = [
 {"name": "Bis(methylthio)methane", "name_ko": "비스(메틸설파닐)메탄", "class": "황 휘발성분", "role": "marker", "part": "자실체(신선 시료를 액체질소로 급랭, -24 ℃ 보관; 진품 13점)", "content_text": "237 ± 27 – 4360 ± 260 μg/kg(대리석덩이버섯 진품 6점은 불검출, 이론상 최대 56 μg/kg 미만)[3]; 아콸라냐산 휘발성분의 78.72%(상대 비율)[6]", "activity_ko": "마늘 같은 냄새의 핵심 향 성분(향 활성값 1000 초과)이며 대리석덩이버섯과 구별하는 지표[3, 5]", "source": [3, 5, 6]},
 {"name": "2(5H)-Furanone", "name_ko": "푸란-2(5H)-온", "class": "락톤(휘발성)", "role": "marker", "part": "자실체(진품 13점)", "content_text": "137 ± 23 – 487 ± 25 μg/kg(대리석덩이버섯 1490 ± 80 – 5010 ± 160 μg/kg)[3]", "activity_ko": "이 종에서 일관되게 낮아 대리석덩이버섯과의 판별 지표로 쓰임[3]", "source": [3]},
 {"name": "3-(Methylthio)propanal", "name_ko": "3-(메틸티오)프로판알(메티오날)", "class": "황 알데하이드(휘발성)", "role": "bioactive", "part": "자실체(알바산)", "content_text": "향기 추출물 희석 분석에서 희석 배수가 가장 높음(정량값은 초록에 없음)[5]", "activity_ko": "삶은 감자 같은 냄새의 핵심 향 성분[5]", "source": [5]},
 {"name": "3-Methylbutanal", "name_ko": "3-메틸부탄알", "class": "알데하이드(휘발성)", "role": "bioactive", "part": "자실체(알바산)", "content_text": "향 활성값 1000 초과(정량값은 초록에 없음)[5]", "activity_ko": "맥아 냄새의 핵심 향 성분[5]", "source": [5]},
 {"name": "1-Pyrroline", "name_ko": "1-피롤린(3,4-디하이드로-2H-피롤)", "class": "고리형 이민(휘발성)", "role": "bioactive", "part": "자실체(알바산)", "content_text": "향 활성값 1000 초과(정량값은 초록에 없음)[5]", "activity_ko": "아민 같은 냄새를 내는 핵심 향 성분으로 이 연구에서 처음 확인됨[5]", "source": [5]},
 {"name": "2,3-Butanedione", "name_ko": "2,3-부탄디온(디아세틸)", "class": "케톤(휘발성)", "role": "bioactive", "part": "자실체(알바산)", "content_text": "희석 배수가 높은 향 성분(정량값은 초록에 없음)[5]", "activity_ko": "버터 냄새[5]", "source": [5]},
 {"name": "Dimethyl sulfide", "name_ko": "디메틸설파이드", "class": "황 휘발성분", "role": "bioactive", "part": "자실체(이탈리아·크로아티아 17개 지점)", "content_text": "GC-MS로 모든 시료에서 검출(상대 비율은 보충자료, 확인하지 못함)[4]", "activity_ko": "비스(메틸티오)메탄과 함께 향 형성에 가장 크게 기여하는 황 화합물로 제시됨[4]", "source": [4]},
 {"name": "Dimethyl disulfide", "name_ko": "디메틸디설파이드", "class": "황 휘발성분", "role": "bioactive", "part": "자실체", "content_text": "GC-MS로 모든 시료에서 검출[4]", "activity_ko": "모든 시료에 있어 산지 추적에는 쓸 수 없음[4]", "source": [4]},
 {"name": "Glutathione", "name_ko": "글루타티온", "class": "항산화 펩타이드", "role": "bioactive", "part": "자실체(생체중 기준)", "content_text": "644 – 2863 nmol/g 생체중(산지별)[4]", "activity_ko": "항산화 대사물; 함량이 시료 전체 항산화력과 비례하지는 않음[4]", "source": [4]},
 {"name": "Ascorbic acid", "name_ko": "아스코르브산(비타민 C)", "class": "비타민", "role": "nutrient", "part": "자실체(생체중 기준)", "content_text": "약 46 – 116 nmol/g 생체중(효소법)[4]", "activity_ko": "효소법으로 측정됨; 균류의 아스코르브산 합성 여부는 아직 논쟁 중이라고 적힘[4]", "source": [4]},
 {"name": "Gallic acid equivalents (total phenolics)", "name_ko": "총페놀(갈산 당량)", "class": "페놀 화합물(총량)", "role": "bioactive", "part": "자실체", "content_text": "1100 – 약 5400 nmol GAE/g 생체중[4]; 290 mg GAE/100 g[20]", "activity_ko": "조사한 송로 10종 가운데 총페놀과 항산화 시험값이 가장 높았음[20]; 다만 페놀 함량과 항산화력 사이 상관은 없었다는 보고도 있음[4]", "source": [4, 20]},
 {"name": "Epicatechin", "name_ko": "에피카테킨", "class": "플라반-3-올", "role": "bioactive", "part": "자실체(메탄올·물 추출물)", "content_text": "LC-MS/MS로 이 종의 주된 페놀로 확인(정량값은 초록에 없음)[19]", "activity_ko": "추출물의 항산화·COX-1/12-LOX 억제는 시험관 결과[19]", "source": [19]},
 {"name": "Catechin", "name_ko": "카테킨", "class": "플라반-3-올", "role": "bioactive", "part": "자실체(메탄올·물 추출물)", "content_text": "에피카테킨과 함께 주된 페놀(정량값은 초록에 없음)[19]", "activity_ko": "시험관 항산화 활성의 기여 성분 후보[19]", "source": [19]},
 {"name": "Riboflavin", "name_ko": "리보플래빈(비타민 B2)", "class": "비타민", "role": "nutrient", "part": "자실체(극성 추출물)", "content_text": "비표적 UHPLC-QTOF-MS로 송로에서 처음 주석·표적 분석(정량값은 초록에 없음)[21]", "activity_ko": "진위 판별용 생체지표 후보로 제시[21]", "source": [21]},
 {"name": "Azelaic acid", "name_ko": "아젤라산", "class": "디카복실산", "role": "bioactive", "part": "자실체(극성 추출물)", "content_text": "송로에서 처음 검출된 4개 분자 중 하나(정량값은 초록에 없음)[21]", "activity_ko": "2-·3-이소프로필말산과 함께 새로 보고됨[21]", "source": [21]},
]

assays = [
 {"role": "literature", "compound": "Bis(methylthio)methane", "compound_ko": "비스(메틸설파닐)메탄", "part": "자실체(신선 시료를 액체질소로 급랭, -24 ℃ 보관; 2018–2020년 수집)",
  "content": "진품 13점 237 ± 27 – 4360 ± 260 μg/kg[3]", "method": "안정동위원소 희석 GC-MS(이온트랩)",
  "conditions": {"instrument": "7890B 가스크로마토그래프 + Saturn 220 이온트랩 질량분석기, 멀티모드 주입구(스플릿리스), Combi PAL 자동시료주입기",
   "column": "DB-FFAP, 30 m × 0.25 mm i.d., 0.25 μm",
   "mobile_phase": "헬륨 운반기체",
   "gradient": "오븐 40 ℃(2분) → 6 ℃/분 118 ℃ → 40 ℃/분 230 ℃(5분); 주입구 40 ℃(2분) → 6 ℃/분 118 ℃ → 40 ℃/분 230 ℃ → 900 ℃/분 250 ℃(열분해를 막기 위해 오븐과 나란한 완만한 주입구 온도)",
   "flow": "1.2 mL/min(정유량)", "temp": "",
   "detection": "EI 70 eV, m/z 35–250, 정량 이온의 추출 이온 크로마토그램(정량 이온은 보충자료, 확인하지 못함)",
   "injection": "2 μL, 스플릿리스",
   "sample_prep": "냉동 분쇄 시료 0.5 g + 디클로로메탄 20 mL + 내부표준 + 무수 황산나트륨 1.5 g, 얼음 냉각하에 균질화(13500 rpm, 20초), 실온 차광 밤샘 교반·여과, 자동 SAFE(40 ℃)로 휘발성분 분리, Vigreux 칼럼으로 약 1 mL 농축(저농도 성분용은 약 100 μL까지 추가 농축), 시료당 3회 반복 처리",
   "standard": "(²H) 표지 비스(메틸설파닐)메탄 내부표준 0.0743–14.9 μg(합성), 비표지 표준품",
   "linearity": "분석물/내부표준 혼합물 검량선(식은 보충자료, 확인하지 못함)", "lod": "", "loq": "", "recovery": ""},
  "rationale": "흰서양송로의 핵심 향 성분이자, 겉모습이 비슷한 대리석덩이버섯(불검출, 이론상 56 μg/kg 미만)과 가르는 판별 지표다[3]. 두 종 범위 사이 빈 구간은 154 μg/kg이었다[3]. 전문(Methods) 확인함[3].",
  "source": [3], "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11066859/", "source_kind": "paper"},
 {"role": "literature", "compound": "Glutathione", "compound_ko": "글루타티온(아스코르브산·총페놀 함께 측정)", "part": "자실체(2014·2015년 11월 하순 채취, 성숙 5단계, 4 ℃ 보관 3일 안 분석)",
  "content": "글루타티온 644 – 2863 nmol/g 생체중, 아스코르브산 약 46 – 116 nmol/g 생체중, 총페놀 1100 – 약 5400 nmol GAE/g 생체중[4]", "method": "효소법(아스코르브산)·분광법(분석 세부는 보충자료)",
  "conditions": {"instrument": "", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "", "injection": "", "sample_prep": "산지·연도별 자실체 2개씩(n = 4) 분석; 추출은 세균·효모 세포를 깨지 않는 방법이라고 기술", "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "산지·숙주 식물에 따라 달라지는 항산화 대사물로, 산지 판별 지표 후보로 제시되었다[4]. 본문은 확인했으나 분석 조건은 보충자료에 있어 전문 확인 못함[4].",
  "source": [4], "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5940868/", "source_kind": "paper"},
 {"role": "literature", "compound": "Ergosterol", "compound_ko": "에르고스테롤(균사량 환산 지표)", "part": "균사 고체 발효 제품(콩·율무 배지, 25 ℃ 3주; 자실체 아님)",
  "content": "균사 함량 40.91 – 93.38 mg/g(배지 비율별, 에르고스테롤로 환산)[18]", "method": "HPLC-UV",
  "conditions": {"instrument": "HPLC, UV 검출기", "column": "C18, 250 mm × 4.6 mm", "mobile_phase": "메탄올 100%", "gradient": "등용매", "flow": "1 mL/min", "temp": "",
   "detection": "UV 282 nm", "injection": "20 μL",
   "sample_prep": "건조 분말 0.25 g + 99% 메탄올 5 mL, 60 ℃ 오븐 1시간 추출, 원심분리 후 0.22 μm 막 여과",
   "standard": "에르고스테롤 표준품", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "균류 세포막 스테롤이라 발효 제품 속 균사량을 추정하는 데 쓰였다[18]. 자실체 성분 지표가 아니라 균사 제품의 품질 지표다[18]. 전문(Methods) 확인함[18].",
  "source": [18], "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8746469/", "source_kind": "paper"},
 {"role": "literature", "compound": "1-Pyrroline", "compound_ko": "1-피롤린", "part": "자실체(알바산)",
  "content": "향 활성값(농도/역치) 1000 초과[5]", "method": "안정동위원소 희석 분석(SIDA), SAFE 증류 후 향기 추출물 희석 분석",
  "conditions": {"instrument": "", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "", "injection": "", "sample_prep": "용매 추출 후 SAFE 증류(초록 기준)", "standard": "안정동위원소 표지 내부표준(초록 기준, 세부 확인하지 못함)", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "비스(메틸티오)메탄·3-메틸부탄알과 함께 향 활성값이 1000을 넘는 핵심 향 성분으로, 재조합·제거 실험에서 아민 같은 냄새가 확인되었다[5]. 초록만 봄 — 전문 확인 못함[5].",
  "source": [5], "url": "https://pubmed.ncbi.nlm.nih.gov/28965409/", "source_kind": "paper"},
]

d = {"slug": "tuber-magnatum", "name_ko": "흰서양송로", "name_en": "Italian white truffle (Piedmont/Alba white truffle)",
     "scientific_name": "Tuber magnatum Pico", "aliases": ["흰서양송로자실체", "송로버섯", "White Truffles", "Bianco Truffles", "알바 송로", "Tuber magnatum Picco"],
     "sections": [{"key": k, "title": v[0], "body": v[1]} for k, v in S.items()],
     "compounds": compounds, "markers": [], "assays": assays, "nutrients": [], "production": [], "world": [], "gi": [], "orgs": [],
     "sources": sources}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
for s in d["sections"]:
    print(s["key"], len(s["body"]))
