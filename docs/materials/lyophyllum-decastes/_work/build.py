import json
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
ACC = "2026-11-02"
I1020_URL = "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020"


def pm(pmid, title, journal, year):
    return dict(title=f"{title} ({journal}, {year}; PMID {pmid})", url=f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
                publisher=f"{journal} (PubMed)", accessed=ACC)


S = [
    dict(title="식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 잿빛만가닥버섯(Lyophyllum decastes (Fr. ex Fr.) Sing / Tricholoma aggregatum Gill.) (로컬 원자료 I1020_20261013.json 대조)", url=I1020_URL, publisher="식품의약품안전처", accessed="2026-10-13"),
    dict(title="식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 이름이 비슷한 항목: 땅찌만가닥버섯자실체(L. shimeji)·만가닥버섯(L. ulmarium / Hypsizygus ulmarius)·모래꽃만가닥버섯(L. semitale)·느티만가닥버섯자실체(Hypsizygus marmoreus)·연기색만가닥버섯(L. fumosum, 사용불가)·반투명만가닥버섯(L. sykosporum, 사용불가) (로컬 원자료 대조)", url=I1020_URL, publisher="식품의약품안전처", accessed="2026-10-13"),
    dict(title="통계청 「농작물생산조사」·농림축산식품부 「특용작물 생산실적」(1995–2024) 로컬 파싱본(docs/stats/regional_crops.csv·special_crops_annual.csv·special_crops_2024.csv) — '잿빛만가닥버섯'·'만가닥버섯' 품목 없음 확인", url="https://www.mafra.go.kr", publisher="농림축산식품부·통계청", accessed=ACC),
    pm("24445577", "Detection of the edible ectomycorrhizal fungus Lyophyllum shimeji colonising seedlings of cultivated conifer species in New Zealand (초록)", "Mycorrhiza", "2014"),
    pm("30315880", "Characterization and comparison of the mitochondrial genomes from two Lyophyllum fungal species and insights into phylogeny of Agaricomycetes (초록)", "International Journal of Biological Macromolecules", "2018"),
    pm("37032898", "Complete genome sequences and comparative secretomic analysis for the industrially cultivated edible mushroom Lyophyllum decastes reveals insights on evolution and lignocellulose degradation potential (초록)", "Frontiers in Microbiology", "2023"),
    pm("40083419", "Insights into the evolution and mechanisms of response to heat stress by whole genome sequencing and comparative proteomics analysis of the domesticated edible mushroom Lyophyllum decastes (초록)", "Mycology", "2025"),
    pm("41764824", "Geographical divergence in quality of Lyophyllum decastes (Fr.) Singer from three major production regions in China (초록)", "Food Chemistry", "2026"),
    pm("39590654", "Screening of the candidate metabolite to evaluate the mycelium physiological maturation of Lyophyllum decastes based on metabolome and transcriptome analysis (PMC11596021 전문)", "Journal of Fungi", "2024"),
    pm("40863538", "Exploring the mechanisms of amino acid and bioactive constituent formation during fruiting body development in Lyophyllum decastes by metabolomic and transcriptomic analyses (PMC12387458 전문)", "Journal of Fungi", "2025"),
    pm("22466796", "Gender differences and regionalization of the cultural significance of wild mushrooms around La Malinche volcano, Tlaxcala, Mexico (초록)", "Mycologia", "2012"),
    pm("17874836", "Oral administration of the extract from Hatakeshimeji (Lyophyllum decastes sing.) mushroom inhibits the development of atopic dermatitis-like skin lesions in NC/Nga mice (초록)", "Journal of Nutritional Science and Vitaminology", "2007"),
    pm("16232825", "Antitumor effects of (1→3)-beta-D-glucan and (1→6)-beta-D-glucan purified from newly cultivated mushroom, Hatakeshimeji (Lyophyllum decastes Sing.) (초록)", "Journal of Bioscience and Bioengineering", "2000"),
    pm("12026194", "Effect of Hatakeshimeji (Lyophyllum decastes Sing.) mushroom on serum lipid levels in rats (초록)", "Journal of Nutritional Science and Vitaminology", "2002"),
    pm("12230127", "Antidiabetic activity of Lyophyllum decastes in genetically type 2 diabetic mice (초록)", "Biological & Pharmaceutical Bulletin", "2002"),
    pm("24791541", "[Chemical constituents from Lyophyllum decastes] (중국어 논문, 영문 초록)", "Zhongguo Zhong Yao Za Zhi", "2013"),
    pm("17904093", "A new alpha-galactosyl-binding protein from the mushroom Lyophyllum decastes (초록)", "Archives of Biochemistry and Biophysics", "2007"),
    pm("25504801", "Atomic-resolution structure of the α-galactosyl binding Lyophyllum decastes lectin reveals a new protein family found in both fungi and plants (초록)", "Glycobiology", "2014"),
    pm("31131717", "Isolation of 6-hydroxy-L-tryptophan from the fruiting body of Lyophyllum decastes for use as a tyrosinase inhibitor (초록)", "Bioscience, Biotechnology, and Biochemistry", "2019"),
    pm("16868813", "Hepatotoxicity associated with Lyophyllum decastes Sing. (Hatakeshimeji) (증례 서신, 초록 없음 — 제목만 확인)", "Journal of Gastroenterology", "2006"),
    pm("42546016", "Radiocesium uptake in two fungal bed-cultivated edible mushroom species in forests in Fukushima, Japan (초록)", "PLoS One", "2026"),
    pm("9861731", "Radiocesium accumulation in edible wild mushrooms from coniferous forests around the Nuclear Centre of Mexico (초록)", "Science of the Total Environment", "1998"),
    pm("40221625", "Accumulation and translocation of lead and cadmium in Lyophyllum decastes (초록)", "Environmental Geochemistry and Health", "2025"),
    pm("22794131", "Metal concentrations of wild edible mushrooms from Turkey (초록)", "Ecology of Food and Nutrition", "2012"),
    pm("38789974", "Identification and fungicides sensitivity evaluation of the causal agent of cobweb disease on Lyophyllum decastes in China (초록)", "BMC Microbiology", "2024"),
    pm("35998484", "Ultrasonic treatment decreases Lyophyllum decastes fruiting body browning and affects energy metabolism (초록)", "Ultrasonics Sonochemistry", "2022"),
    pm("37430997", "Effects of drying methods on the physicochemical aspects and volatile compounds of Lyophyllum decastes (초록)", "Foods", "2022"),
    pm("35989006", "Polysaccharides from Lyophyllum decastes reduce obesity by altering gut microbiota and increasing energy expenditure (초록)", "Carbohydrate Polymers", "2022"),
    pm("40717964", "Lyophyllum decastes-derived polysaccharides alleviate DSS-induced colitis in mice (초록)", "Frontiers in Pharmacology", "2025"),
    pm("41057065", "Structural elucidation of Lyophyllum decastes polysaccharide LP1-1 and its mechanism of macrophage activation mediated through TLR2/4 (초록)", "International Journal of Biological Macromolecules", "2025"),
    pm("36860492", "Effects of polysaccharides from Lyophyllum decastes (Fr.) Singer on gut microbiota via in vitro-simulated digestion and fermentation (초록)", "Frontiers in Microbiology", "2023"),
    pm("37904843", "Comparative transcriptome analysis on candidate genes associated with fruiting body growth and development in Lyophyllum decastes (초록)", "PeerJ", "2023"),
    pm("42646098", "Exploration of the potential suitable distribution range of the Lyophyllum decastes complex in high-altitude cold regions of Southwest China (초록)", "Journal of Fungi", "2026"),
    dict(title="잿빛만가닥버섯 발효톱밥 재배 연구(한국버섯학회지, 2009) — 원문·초록 페이지가 네트워크 허용 목록 밖이라 WebSearch 요약으로만 확인", url="https://koreascience.or.kr/article/JAKO200914364645032.page", publisher="한국버섯학회 (WebSearch 요약)", accessed=ACC),
    pm("41319774", "Effect of extraction methods on Lyophyllum decastes crude polysaccharides for modifying wheat starch pasting, rheology, and in vitro digestibility (초록)", "International Journal of Biological Macromolecules", "2025"),
]
for i, s in enumerate(S, 1):
    s["n"] = i
sources = [dict(n=s["n"], title=s["title"], url=s["url"], publisher=s["publisher"], accessed=s["accessed"]) for s in S]

sections = [
 dict(key="overview", title="한눈에 보기", body=(
  "잿빛만가닥버섯(Lyophyllum decastes)은 만가닥버섯속(Lyophyllum)의 식용버섯으로, 일본 논문에서는 하타케시메지(Hatakeshimeji), 중국 논문에서는 루룽구(Luronggu)라는 이름으로도 불린다[12, 6]. "
  "식품의약품안전처 「식품원료 목록」에는 원료명 '잿빛만가닥버섯', 학명 'Lyophyllum decastes (Fr. ex Fr.) Sing / Tricholoma aggregatum Gill.'로 올라 있고, 상태는 '사용가능', 사용 조건은 '사용가능부위 : 자실체'이다[1]. "
  "따라서 일반 식품의 원료로는 자실체(버섯 몸체)를 쓸 수 있다[1]. 건강기능식품 고시형 원료의 원재료 목록에는 없어, 고시된 지표성분과 기준은 확인하지 못함.\n\n"
  "같은 목록에는 땅찌만가닥버섯(L. shimeji)·만가닥버섯(L. ulmarium)·모래꽃만가닥버섯(L. semitale)이 따로 올라 있으며, 이 문서는 그 종들의 자료를 섞지 않는다[2]. "
  "중국은 이 버섯의 세계 최대 생산국으로 소개되며, 2020년 중국 생산량은 약 11,590톤으로 인용되었다[8, 9]. "
  "연구는 주로 자실체 다당류(β-글루칸 등)의 면역·장내 미생물·대사 작용, 맛 성분, 재배 기술에 모여 있다[13, 28, 10]. 사람 대상 임상시험은 확인하지 못함.")),
 dict(key="history", title="이름과 이용의 역사", body=(
  "2000년 일본 논문은 하타케시메지를 '새로 재배되기 시작한 버섯'이라고 소개했다[13]. "
  "2002년 일본 연구들은 이 버섯 자실체 가루와 열수 추출물을 쥐·생쥐에게 먹여 혈중 지질과 혈당에 미치는 영향을 조사했다[14, 15]. "
  "멕시코 라 말린체 화산 주변 10개 마을 주민 200명 면담에서 L. decastes는 가장 자주 언급된 야생 버섯 다섯 무리에 들었다[11]. "
  "같은 조사는 마을마다 전통 이름과 소비 선호가 달라 화산 동쪽과 서쪽(나와족 마을) 공동체가 갈린다고 보고했다[11].\n\n"
  "중국에서는 최근 공장식 병재배가 확대되면서 널리 재배되는 버섯이 되었다[6, 9]. "
  "2026년 연구는 구이저우·푸젠·쓰촨을 중국의 세 주요 생산 지역으로 다뤘다[8]. "
  "국내에서는 2009년 한국버섯학회지 논문이 이 버섯을 일본에서 비싸게 거래되지만 균사 생장이 느려 인공재배가 어려운 버섯으로 소개했다(WebSearch 요약으로만 확인)[34]. "
  "국문명 '잿빛만가닥버섯'의 유래와 국내 전통 이용 기록은 확인하지 못함.")),
 dict(key="biology", title="균학적 특징", body=(
  "미토콘드리아 유전자로 만든 계통수에서 L. decastes와 L. shimeji는 송이(Tricholoma matsutake)와 가장 가깝게 묶였다[5]. "
  "L. decastes와 L. shimeji는 'L. decastes 복합종'의 두 주요 종이지만, 영양 방식과 선호하는 생육 환경이 크게 다르다[5]. "
  "L. shimeji는 침엽수와 공생하는 외생균근균인 반면, 2023년 유전체 연구는 L. decastes를 목재를 분해하는 버섯으로 다뤘다[4, 6].\n\n"
  "L. decastes 유전체에서는 탄수화물 활성 효소(CAZyme) 577개를 암호화하는 유전자 541개가 확인되었다[6]. "
  "리그닌이 많은 배지에서는 라카아제 두 종과 퀴논 환원효소가 크게 늘었고, 라카아제는 분비 단백질 상위 3위 안에 들었다[6]. "
  "병재배 연구에서 성숙 자실체 길이는 11–13 cm였고, 자실체가 성숙할수록 유리 아미노산과 다당류 함량이 늘었다[10]. "
  "중국 남서부 고산 한랭 지역의 기록 70건으로 만든 기후 적합지 모델에서는 가장 추운 분기의 평균기온이 가장 큰 영향 요인(기여도 50.8%)이었다[33]. "
  "갓 색·포자 등 형태 특징의 공식 기재는 확인하지 못함.")),
 dict(key="related_species", title="가까운 종과 혼동", body=(
  "L. decastes 복합종은 Difformia 절에 속하며 L. shimeji, L. fumosum, L. decastes를 포함한다[4]. "
  "ITS·IGS·EF1-α 염기서열 계통 분석은 L. shimeji를 가까운 종들과 구별했다[4]. "
  "두 종의 미토콘드리아 유전체는 L. decastes 50,643 bp, L. shimeji 73,678 bp로 크기가 다르고, 유전자 배열도 크게 재배열되어 있다[5].\n\n"
  "식약처 목록에서 땅찌만가닥버섯(L. shimeji)·만가닥버섯(L. ulmarium)·모래꽃만가닥버섯(L. semitale)은 각각 별도의 '사용가능' 원료이고, 느티만가닥버섯(Hypsizygus marmoreus)도 따로 올라 있다[2]. "
  "같은 복합종의 연기색만가닥버섯(L. fumosum)과 반투명만가닥버섯(L. sykosporum)은 '사용불가'이므로 잿빛만가닥버섯과 구별해야 한다[2]. "
  "중국 남서부 연구는 복합종 기록이 분자 바코드로 모두 확인된 것은 아니어서 종 단위 분포로 해석하면 안 된다고 밝혔다[33]. "
  "따라서 야생 채취품은 형태만으로 종을 단정하기 어렵다[4, 33].")),
 dict(key="cultivation", title="재배와 배양", body=(
  "중국의 병재배 연구에서는 톱밥 32%, 옥수수속대 21%, 밀기울 17%, 옥수수가루 15%, 대두피 7%, 면실피 5%, 대두박 3%(건물 기준)를 섞은 배지를 수분 65%로 맞춰 121 ℃에서 2시간 살균했다[9]. "
  "균사는 23 ℃, 상대습도 65–75%에서 배양하고, 배지 표면을 긁은 뒤 18 ℃·상대습도 95%로 옮겨 자실체를 냈다[9]. "
  "균사 배양 55일 처리에서 병당 수확량이 307 g으로 45일(280.33 g)과 65일(219.90 g)보다 많았다[9]. "
  "같은 논문은 접종에서 수확까지 약 110–120일이 걸린다는 선행 보고를 인용했다[9].\n\n"
  "국내에서는 2009년 발효톱밥 재배 연구가 수집 균주 9개 가운데 2개를 골라 1,100 mL 병당 약 130 g을 수확했고, 발효톱밥이 미발효톱밥보다 수량이 많았다(WebSearch 요약으로만 확인)[34]. "
  "일본 후쿠시마 숲 14곳의 노지 균상 재배에서 자실체 세슘-137은 0.4–12(평균 2.2) Bq/kg(수분 90% 기준)으로 일본 식품 기준 100 Bq/kg 아래였다[21]. "
  "재배 중에는 Cladobotryum mycophilum에 의한 거미줄병이 발생하며, 중국에서 처음 보고되었다[25]. "
  "국내 재배 면적과 생산량 통계는 확인하지 못함[3].")),
 dict(key="processing", title="가공과 이용", body=(
  "열풍 건조는 에너지가 가장 적게 들고 향이 진했으며, 진공 동결 건조는 색과 모양 보존·복원력이 가장 좋았다[27]. "
  "건조 시료에서는 GC-IMS로 휘발성 향 성분 57종이 확인되었고, 알데하이드·알코올·케톤류가 주를 이뤘다[27]. "
  "35 kHz·300 W 초음파로 10분 처리한 자실체는 4 ℃ 16일 저장 중 갈변 지수가 21.0% 줄었다[26]. "
  "증기 폭쇄 처리는 조다당 수율을 9.81%에서 20.09%로, 조다당 중 β-글루칸 함량을 17.89%에서 40.73%로 높였다[35].\n\n"
  "효능 연구는 세포·동물 수준이다[12, 15, 28]. "
  "물 추출물 500 mg/kg은 제2형 당뇨 생쥐(KK-Ay)의 혈당과 혈중 인슐린을 낮췄다[15]. "
  "사료에 자실체 가루를 섞어 먹인 쥐는 혈청 총콜레스테롤이 낮아지고 담즙산 배설이 늘었다[14]. "
  "추출물을 먹인 생쥐는 아토피 피부염 유사 병변과 혈청 IgE가 줄었다[12]. "
  "정제 다당류는 비만 생쥐의 비만을 줄였고, DSS 대장염 생쥐에서 200·400 mg/kg 투여로 염증을 줄였다[28, 29]. "
  "사람 대상 시험은 확인하지 못함.")),
 dict(key="genetics", title="유전체와 유전 다양성", body=(
  "교배 가능한 두 단핵 균주의 유전체 가운데 LRG-d1-1 균주는 15개 콘티그, 47.7 Mb에 유전자 모델 14,499개로 해독되었다[6]. "
  "이 연구는 교배 육종을 빠르게 하려고 두 교배형을 검출하는 특이 프라이머 4쌍을 설계했다[6]. "
  "재배 균주를 해독한 다른 연구는 13개 콘티그, 40.67 Mb의 유전체를 보고했고, 고온 스트레스에서 열충격 단백질과 유비퀴틴-프로테아좀 계통이 반응한다고 보았다[7].\n\n"
  "미토콘드리아 유전체는 50,643 bp 원형 DNA이며, 15개 핵심 단백질 유전자 중 atp9가 L. shimeji와의 유전 거리가 가장 작았다[5]. "
  "자실체 발달 단계별 전사체 분석에서는 평균 길이 1,462.68 bp의 유전자 15,451개가 조립되었고, 76.84%가 알려진 단백질에 대응했다[32]. "
  "발달 단계별 전사체·대사체 원자료는 NCBI SRA에 SRR24926090 등의 번호로 등록되었다[10]. "
  "균사 성숙 연구의 전사체 원자료는 BioProject PRJNA983922로 공개되었다[9]. "
  "국내 균주의 유전 다양성 자료는 확인하지 못함.")),
 dict(key="safety", title="안전성", body=(
  "식약처 목록에서 잿빛만가닥버섯은 자실체에 한해 '사용가능'이다[1]. "
  "국내 공공기관의 알레르기·잔류·독성 정보는 확인하지 못함.\n\n"
  "2006년 일본 학술지에는 하타케시메지와 관련된 간독성 증례 서신이 실렸으나, 초록이 없어 섭취 형태와 경과는 확인하지 못함[20]. "
  "자실체에는 Shiga 유사 독소와 같은 당(갈라비오스)에 결합하는 약 10 kDa 렉틴이 있다[17, 18]. 이 렉틴을 먹었을 때 사람에 미치는 영향은 확인하지 못함.\n\n"
  "중금속 실험에서 납은 갓·대로 잘 옮겨지지 않았지만(BAF < 1), 카드뮴은 이동 계수가 모두 1보다 커 자실체로 잘 옮겨졌다[23]. "
  "튀르키예 야생 15종 조사는 하루 건조중 30 g 섭취 시 A. cylindracea와 H. leucopus를 제외하면 납·카드뮴 위험이 없다고 보았다[24]. "
  "멕시코 원자력센터 주변 조사에서 L. decastes는 세슘-137 전이 계수가 높은 종 가운데 하나였다[22]. "
  "반면 후쿠시마 균상 재배 자실체는 모두 일본 기준 100 Bq/kg 미만이었다[21]. "
  "중국 재배지 거미줄병 병원균에는 프로클로라즈-망간 착물·트리플록시스트로빈·테부코나졸·디페노코나졸이 균사 억제 효과를 보였다[25]. 이 버섯에 대한 국내 농약 잔류 기준은 확인하지 못함.")),
]

compounds = [
 dict(name="Lysine", name_ko="라이신(유리 아미노산)", class_="아미노산", role="nutrient", part="성숙 자실체(동결 건조, 병재배)",
      content_text="10,841.1 μg/g(성숙 단계, 유리 아미노산 중 최고); 총 유리 아미노산 45,107.39 μg/g, 필수 19,553.85 μg/g[10]",
      activity_ko="무미(tasteless) 아미노산으로 분류; 성숙 단계 라이신 생합성 경로 활성과 연결[10]", source=[10]),
 dict(name="Glutamic acid", name_ko="글루탐산", class_="아미노산", role="nutrient", part="자실체(균사 배양 55일 처리)",
      content_text="177.90 μg/g 건조중; 아스파르트산 95.74, 페닐알라닌 31.68, 티로신 13.79, 알라닌 10.99 μg/g 건조중[9]",
      activity_ko="감칠맛(umami) 아미노산[9, 10]", source=[9, 10]),
 dict(name="Polysaccharide", name_ko="다당류(총량)", class_="다당류", role="bioactive", part="성숙 자실체",
      content_text="13.66 mg/g(성숙), 어린 자실체 11.53, 균사 5.63, 원기 4.42 mg/g(페놀-황산법, 포도당 환산)[10]",
      activity_ko="비만·장염 모델 생쥐에서 효과, 장내 미생물 조절(동물·시험관)[28, 29, 31]", source=[10, 28, 29, 31]),
 dict(name="beta-Glucan", name_ko="(1→3)-β-D-글루칸", class_="다당류", role="bioactive", part="자실체 열수 추출물",
      content_text="분획 IV-1 평균 분자량 305 kDa; 조다당 중 β-글루칸 17.89%(일반 분쇄)·40.73%(증기 폭쇄)[13, 35]",
      activity_ko="Sarcoma 180 종양에 대한 항종양 활성, 복강 대식세포 증가(생쥐)[13]", source=[13, 35]),
 dict(name="beta-1,6-Glucan", name_ko="(1→6)-β-D-글루칸", class_="다당류", role="bioactive", part="자실체 열수 추출물",
      content_text="분획 IV-3 평균 분자량 14 kDa; 함량 수치는 초록에 없음[13]",
      activity_ko="Sarcoma 180 항종양 활성(생쥐)[13]", source=[13]),
 dict(name="LP1-1 polysaccharide", name_ko="중성 다당류 LP1-1", class_="다당류(헤테로글리칸)", role="bioactive", part="자실체",
      content_text="분자량 17.4 kDa; 포도당·갈락토스·만노스·푸코스 몰비 91.53:4.63:2.72:1.12[30]",
      activity_ko="RAW264.7 대식세포에서 TLR2/4 경유 면역 자극(시험관)[30]", source=[30]),
 dict(name="Flavonoids", name_ko="총 플라보노이드", class_="플라보노이드", role="bioactive", part="자실체(균사 배양 55일 처리)",
      content_text="2.94 mg/g 건조중(45일 2.67, 65일 2.61 mg/g 건조중)[9]",
      activity_ko="품질 지표로 측정; 균사 단계에서 더 많음[9, 10]", source=[9, 10]),
 dict(name="6-Hydroxy-L-tryptophan", name_ko="6-히드록시-L-트립토판", class_="비단백질 아미노산", role="bioactive", part="동결 건조 자실체 열수 추출물",
      content_text="함량 수치는 초록에 없음; 티로시나아제 억제 IC50 0.23 mM[19]",
      activity_ko="경쟁적 티로시나아제 억제(멜라닌 생성 효소)[19]", source=[19]),
 dict(name="Ergosterol", name_ko="에르고스테롤", class_="스테롤", role="bioactive", part="자실체",
      content_text="(22E,24R)-ergosta-5,7,22-trien-3β-ol로 분리; 함량 수치는 초록에 없음[16]",
      activity_ko="버섯 스테롤(비타민 D2 전구체로 알려짐) — 이 연구에서는 구조만 보고[16]", source=[16]),
 dict(name="Ergosterol peroxide", name_ko="에르고스테롤 퍼옥사이드", class_="스테롤", role="bioactive", part="자실체",
      content_text="5α,8α-epidioxy-(22E,24R)-ergosta-6,22-dien-3β-ol로 분리; 함량 수치는 초록에 없음[16]",
      activity_ko="구조만 보고[16]", source=[16]),
 dict(name="Adenosine", name_ko="아데노신", class_="뉴클레오사이드", role="bioactive", part="자실체",
      content_text="분리 13종 중 하나; 함량 수치는 초록에 없음[16]", activity_ko="구조만 보고[16]", source=[16]),
 dict(name="Nicotinic acid", name_ko="니코틴산(나이아신)", class_="비타민 B군", role="nutrient", part="자실체",
      content_text="분리 13종 중 하나; 함량 수치는 초록에 없음[16]", activity_ko="구조만 보고[16]", source=[16]),
 dict(name="Mannitol", name_ko="D-만니톨", class_="당알코올", role="nutrient", part="자실체",
      content_text="분리 13종 중 하나; 함량 수치는 초록에 없음[16]", activity_ko="구조만 보고[16]", source=[16]),
 dict(name="Lyophyllum decastes lectin", name_ko="잿빛만가닥버섯 렉틴(LDL)", class_="단백질(렉틴)", role="bioactive", part="자실체",
      content_text="단량체 분자량 10,276 Da의 동종이량체; 함량 수치는 초록에 없음[17]",
      activity_ko="갈라비오스(Galα1,4Gal) 특이 결합; 1.0 Å 결정 구조로 새 단백질 계열 제시[17, 18]", source=[17, 18]),
 dict(name="Scopoletin", name_ko="스코폴레틴", class_="쿠마린", role="bioactive", part="원기·균사·자실체(대사체 분석)",
      content_text="상대 함량만 보고: 이 경로 대사물 중 가장 많고 원기 단계에서 가장 높음[10]",
      activity_ko="2차 대사 지표로 분석[10]", source=[10]),
]
for c in compounds:
    c["class"] = c.pop("class_")
compounds = [{k: c[k] for k in ("name", "name_ko", "class", "role", "part", "content_text", "activity_ko", "source")} for c in compounds]

assays = [
 dict(role="literature", compound="Free amino acids (lysine, alanine, arginine, glutamic acid, glutamine etc.)", compound_ko="유리 아미노산(라이신·알라닌·아르기닌·글루탐산·글루타민 등)",
      part="자실체(동결 건조, 원기·어린·성숙 단계)", content="라이신 10,841.1 μg/g(성숙 단계), 총 유리 아미노산 45,107.39 μg/g[10]",
      method="HPLC-ESI-MS",
      conditions=dict(instrument="Thermo Scientific UltiMate 3000 HPLC", column="C18-Hypersil Gold (Thermo Scientific, 3 μm, 100 mm × 2.1 mm)",
                      mobile_phase="A: 0.1% 폼산, B: 100% 메탄올",
                      gradient="0–0.5분 4% B; 0.5–2.5분 35% B까지; 2.5–4.5분 77% B까지; 4.5–6.5분 100% B까지; 6.5–6.6분 4% B로; 6.6–10분 4% B 유지",
                      flow="0.2 mL/min", temp="40 ℃",
                      detection="ESI 질량분석(이온 분무 전압 3500 V, 시스 가스 35 Arb, 보조 가스 10 Arb, 모세관 325 ℃)",
                      injection="3 μL",
                      sample_prep="동결 건조 자실체 100 mg을 물 10 mL에 분산, 30분 초음파; 디클로로메탄 1 mL 첨가 후 13,000 rpm·4 ℃·5분 원심분리; 상층액 0.22 μm 여과",
                      standard="", linearity="", lod="", loq="", recovery=""),
      rationale="감칠맛·단맛 아미노산 조성이 이 버섯의 맛 품질을 설명하는 지표로 쓰였고, 같은 연구진의 균사 성숙 연구도 같은 조건으로 글루탐산 등을 정량했다[10, 9]. 표준품·직선성·검출한계·정량한계·회수율은 원문에 없다[10].",
      source=[10, 9], url="https://pubmed.ncbi.nlm.nih.gov/40863538/", source_kind="paper"),
 dict(role="literature", compound="Polysaccharides (total, as glucose)", compound_ko="다당류(총량, 포도당 환산)",
      part="자실체(균사·원기·어린·성숙 단계)", content="성숙 13.66 mg/g, 어린 자실체 11.53 mg/g, 균사 5.63 mg/g, 원기 4.42 mg/g[10]",
      method="페놀-황산 비색법(490 nm)",
      conditions=dict(instrument="마이크로플레이트 리더", column="", mobile_phase="", gradient="", flow="", temp="",
                      detection="흡광도 490 nm", injection="",
                      sample_prep="40메시 건조 분말 1 g + 초순수 42 mL, 65 ℃ 2.5시간 추출 → 7500 rpm 10분 원심 → 55 ℃ 회전증발로 1/5 농축 → 3배 부피 무수 에탄올, 4 ℃ 24시간 침전 → Sevag 시약(클로로폼:n-부탄올 4:1)으로 단백질 제거 2–3회 → 3500 Da 투석 48시간 → 동결 건조, 1 mg/mL로 용해",
                      standard="포도당 표준곡선", linearity="", lod="", loq="", recovery=""),
      rationale="이 버섯의 주요 생리활성(비만·면역·장내 미생물 조절)이 다당류에 돌려지기 때문에 발달 단계별 품질 지표로 측정했다[10]. 직선성·검출한계·회수율은 원문에 없다[10].",
      source=[10], url="https://pubmed.ncbi.nlm.nih.gov/40863538/", source_kind="paper"),
 dict(role="literature", compound="beta-Glucan (in crude polysaccharide)", compound_ko="β-글루칸(조다당 중)",
      part="자실체(일반 분쇄·증기 폭쇄 처리)", content="조다당 중 β-글루칸 17.89%(일반 분쇄) → 40.73%(증기 폭쇄)[35]",
      method="", conditions={},
      rationale="버섯 다당류 활성의 핵심 성분으로 가공 처리 효과를 비교하는 지표로 쓰였다[35]. 전문 확인 못함 — 측정법과 조건은 비워 둠[35].",
      source=[35], url="https://pubmed.ncbi.nlm.nih.gov/41319774/", source_kind="paper"),
]

world = [dict(country="중국", metric="production_t", year=2020, value=11590, unit="t",
              note="논문 서론의 인용값(about 11,590 tonnes in 2020); 1차 통계 출처는 확인하지 못함", source=[9])]

d = dict(slug="lyophyllum-decastes", name_ko="잿빛만가닥버섯", name_en="Lyophyllum decastes",
         scientific_name="Lyophyllum decastes (Fr.) Singer", aliases=["Lyophyllum decastes", "Tricholoma aggregatum", "Hatakeshimeji", "Luronggu"],
         sections=sections, compounds=compounds, markers=[], assays=assays, nutrients=[], production=[], world=world,
         gi=[], orgs=[], sources=sources)
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
print("ok", len(sources))
