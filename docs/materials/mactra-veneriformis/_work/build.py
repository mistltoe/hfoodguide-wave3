import json, os
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A = "2026-11-02"
def pm(title, doi, pub, extra=""):
    return {"title": title, "url": f"https://doi.org/{doi}", "publisher": pub, "accessed": A}
sources = [
 {"title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 동죽(Mactra veneriformis, 별칭 동조개)·개량조개(Mactra chinensis)·Mactra solidissima 항목", "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
 pm("A high-quality chromosome-level genome assembly of the bivalve mollusk Mactra veneriformis. G3 (Bethesda) 2022;12(11):jkac229", "10.1093/g3journal/jkac229", "G3: Genes|Genomes|Genetics (PubMed 36165708, PMC9635629 전문)"),
 pm("The complete mitochondrial genome of the clam Mactra veneriformis (Bivalvia: Mactridae): has a unique non-coding region, missing atp8 and typical tRNA Ser. Mitochondrial DNA 2013;24(6):613–615 (초록)", "10.3109/19401736.2013.772152", "Mitochondrial DNA (PubMed 23520998)"),
 pm("Development and application of a method for determination of nucleosides and nucleobases in Mactra veneriformis. Pharmacogn Mag 2013;9(34):96–102", "10.4103/0973-1296.111241", "Pharmacognosy Magazine (PubMed 23772103, PMC3680862 전문)"),
 pm("Characterisation of nucleosides and nucleobases in Mactra veneriformis by HPLC-DAD-MS. Food Chem 2012;135(2):548–554 (초록)", "10.1016/j.foodchem.2012.05.019", "Food Chemistry (PubMed 22868127)"),
 pm("Antioxidant activities and antioxidative components in the surf clam, Mactra veneriformis. Nat Prod Res 2011;25(19):1838–1848 (초록)", "10.1080/14786419.2010.530268", "Natural Product Research (PubMed 21756123)"),
 pm("Extraction and detailed characterization of phospholipid-enriched oils from six species of edible clams. Food Chem 2017;239:1175–1181 (초록)", "10.1016/j.foodchem.2017.07.035", "Food Chemistry (PubMed 28873537)"),
 pm("Characterization of glycerophospholipid molecular species in six species of edible clams by HPLC-ESI-MS/MS. Food Chem 2017;219:419–427 (초록)", "10.1016/j.foodchem.2016.09.160", "Food Chemistry (PubMed 27765247)"),
 pm("Characterization of ACE inhibitory peptides from Mactra veneriformis hydrolysate by Nano-LC-ESI-MS and molecular docking. Mar Drugs 2014;12(7):3917–3928 (초록)", "10.3390/md12073917", "Marine Drugs (PubMed 24983637)"),
 pm("Rapid identification of bioactive peptides with antioxidant activity from the enzymatic hydrolysate of Mactra veneriformis by UHPLC-Q-TOF mass spectrometry. Food Chem 2015;167:484–489 (초록)", "10.1016/j.foodchem.2014.06.113", "Food Chemistry (PubMed 25149015)"),
 pm("Characterizations and microsphere formulation of polysaccharide from the marine clam (Mactra veneriformis). Carbohydr Polym 2013;92(1):106–113 (초록)", "10.1016/j.carbpol.2012.08.084", "Carbohydrate Polymers (PubMed 23218272)"),
 pm("Preparation, analysis and antioxidant evaluation of the controlled product of polysaccharide from Mactra veneriformis by mild acid hydrolysis. Carbohydr Polym 2016;137:709–718 (초록)", "10.1016/j.carbpol.2015.11.030", "Carbohydrate Polymers (PubMed 26686183)"),
 pm("Protective actions of acidic hydrolysates of polysaccharide extracted from Mactra veneriformis against chemical-induced acute liver damage. Front Pharmacol 2020;11:446 (초록)", "10.3389/fphar.2020.00446", "Frontiers in Pharmacology (PubMed 32390833)"),
 pm("The preliminary study on the antithrombotic mechanism of glycosaminoglycan from Mactra veneriformis. Blood Coagul Fibrinolysis 2014;25(1):16–19 (초록)", "10.1097/MBC.0b013e3283646702", "Blood Coagulation & Fibrinolysis (PubMed 24158117)"),
 pm("Effects of glycosaminoglycan from Mactra veneriformis on the protein C system and expression of relevant factors in human umbilical vein endothelial cells. Blood Coagul Fibrinolysis 2016;27(1):64–69 (초록)", "10.1097/MBC.0000000000000385", "Blood Coagulation & Fibrinolysis (PubMed 26340457)"),
 pm("Effects of ultrasound-assisted high temperature-pressure treatment on the structure and allergenicity of tropomyosin from clam (Mactra veneriformis). Food Chem X 2023;18:100740 (초록)", "10.1016/j.fochx.2023.100740", "Food Chemistry: X (PubMed 37342821)"),
 pm("Occurrence and seasonal variations of lipophilic marine toxins in commercial clam species along the coast of Jiangsu, China. Toxins 2016;8(1):8", "10.3390/toxins8010008", "Toxins (PubMed 26712791, PMC4728530 전문)"),
 pm("Concentration distribution and potential health risk of heavy metals in Mactra veneriformis from Bohai Bay, China. Mar Pollut Bull 2015;97(1-2):528–534 (초록)", "10.1016/j.marpolbul.2015.05.017", "Marine Pollution Bulletin (PubMed 26130526)"),
 pm("Bioaccumulation of heavy metals and health risk assessment in three benthic bivalves along the coast of Laizhou Bay, China. Mar Pollut Bull 2017;117(1-2):98–110 (초록)", "10.1016/j.marpolbul.2017.01.062", "Marine Pollution Bulletin (PubMed 28159333)"),
 pm("Long-term investigation of heavy metal variations in mollusks along the Chinese Bohai Sea. Ecotoxicol Environ Saf 2022;236:113443 (초록)", "10.1016/j.ecoenv.2022.113443", "Ecotoxicology and Environmental Safety (PubMed 35364504)"),
 pm("Investigation of perfluorinated compounds (PFCs) in mollusks from coastal waters in the Bohai Sea of China. J Environ Monit 2010;12(2):508–513 (초록)", "10.1039/b909302h", "Journal of Environmental Monitoring (PubMed 20145894)"),
 pm("Acanthoparyphium tyosenense: the discovery of human infection and identification of its source. J Parasitol 2001;87(4):794–800 (초록)", "10.1645/0022-3395(2001)087[0794:ATTDOH]2.0.CO;2", "Journal of Parasitology (PubMed 11534643)"),
 pm("Prevalence and density of digenetic trematode metacercariae in clams and oysters from western coastal regions of the Republic of Korea. Korean J Parasitol 2017;55(4):399–408 (초록)", "10.3347/kjp.2017.55.4.399", "Korean Journal of Parasitology (PubMed 28877571)"),
 pm("Mactra veneriformis, an intertidal clam, as a new second intermediate host for Acanthoparyphium marilae (Digenea: Echinostomatidae). Korean J Parasitol 2008;46(2):101–104 (초록)", "10.3347/kjp.2008.46.2.101", "Korean Journal of Parasitology (PubMed 18552547)"),
 pm("Effects of water temperature change on immune function in surf clams, Mactra veneriformis (Bivalvia: Mactridae). J Invertebr Pathol 2009;102(1):30–35 (초록)", "10.1016/j.jip.2009.06.002", "Journal of Invertebrate Pathology (PubMed 19524589)"),
 pm("Anthropogenic influences on benthic food web dynamics by interrupted freshwater discharge in a closed Geum River estuary, Korea. Environ Int 2019;131:104981 (초록)", "10.1016/j.envint.2019.104981", "Environment International (PubMed 31302484)"),
 pm("Diet composition and feeding habits of Meretrix meretrix and Mactra veneriformis in the northern Bohai Sea based on high-throughput sequencing. Sci Rep 2025;15:16203 (초록)", "10.1038/s41598-025-01269-8", "Scientific Reports (PubMed 40346116)"),
 pm("Seasonal shifts of morphological traits and dietary of Mactra veneriformis (Bivalvia: Mactridae) populations in the northern Yellow River Delta's intertidal zone. Biology 2025;14(2):176 (초록)", "10.3390/biology14020176", "Biology (PubMed 40001945)"),
 pm("Umami peptides screened based on peptidomics and virtual screening from Ruditapes philippinarum and Mactra veneriformis clams. Food Chem 2022;394:133504 (초록)", "10.1016/j.foodchem.2022.133504", "Food Chemistry (PubMed 35749874)"),
 pm("Integrated metabolomics and GC-IMS analysis to reveal the flavor formation of Mactra veneriformis during combined hot-air drying with boiling pretreatment. Food Chem 2026;515:149219 (초록)", "10.1016/j.foodchem.2026.149219", "Food Chemistry (PubMed 41990499)"),
 pm("The source-specific health risk and biological effect assessment of PAHs in Mactra veneriformis from the Bohai Sea and Yellow Sea. Environ Pollut 2025;370:125900 (초록)", "10.1016/j.envpol.2025.125900", "Environmental Pollution (PubMed 39986559)"),
 {"title": "A Study on Sexual Maturation of Mactra veneriformis Reeve. 한국패류학회지 1988 — WebSearch 결과 요약으로만 확인(원문 사이트 접속 불가, 원문 미열람)", "url": "https://koreascience.kr/article/JAKO198811920534456.page", "publisher": "한국패류학회", "accessed": A},
 pm("Metallothionein and superoxide dismutase responses to sublethal cadmium exposure in the clam Mactra veneriformis. Comp Biochem Physiol C 2010;151(3):325–333 (초록)", "10.1016/j.cbpc.2009.12.005", "Comparative Biochemistry and Physiology Part C (PubMed 20044031)"),
 pm("A comparative study of cellulase and hemicellulase activities of brackish water clam Corbicula japonica with those of other marine Veneroida bivalves. J Exp Biol 2009;212(17):2812–2818 (초록)", "10.1242/jeb.031567", "Journal of Experimental Biology (PubMed 19684215)"),
]
for i, s in enumerate(sources, 1):
    s["n"] = i
sources = [{"n": s["n"], "title": s["title"], "url": s["url"], "publisher": s["publisher"], "accessed": s["accessed"]} for s in sources]

sections = [
 {"key": "overview", "title": "한눈에 보기", "body":
  "동죽(Mactra veneriformis)은 개량조개과(Mactridae) 개량조개속에 드는 바다 조개로, 식약처 「식품원료 목록」에 '동죽'이라는 원료명과 '동조개'라는 별칭, 영문명 surf clam으로 올라 있다[1]. 이 목록에서 동죽은 수산물로 분류된 '사용가능' 원료이며, 사용 부위는 따로 정하지 않은 '-'로 적혀 있고 별도의 사용 조건은 없다[1]. 같은 속의 개량조개(Mactra chinensis)와 Mactra solidissima도 같은 목록에 따로 올라 있어, 이 자료는 동죽 한 종만 다룬다[1].\n\n"
  "동죽은 중국·한국·일본 연안의 갯벌과 조하대, 얕은 바다에 흔하고 많이 사는 부유물 여과 섭식 조개다[2]. 한국에서는 중요한 수산 자원으로 소개되며[25], 중국에서는 식품뿐 아니라 껍데기와 살이 민간 약재로도 쓰인다고 보고되었다[2].\n\n"
  "건강기능식품 고시형 원료로 등재된 기록과 식약처가 정한 지표성분은 확인하지 못함. 성분 연구로는 뉴클레오사이드·핵염기, 인지질과 EPA·DHA, 다당류와 펩타이드를 정량하거나 분석한 논문이 있다[4–12]."},
 {"key": "history", "title": "이용 역사", "body":
  "중국 연구진은 동죽이 수천 년 동안 해산물이자 전통 약재로 쓰여 왔다고 적었다[5]. 다른 연구는 동죽이 값싸고 맛있는 해산물로 중국 연안, 특히 장쑤성 연안 모래톱에 흔하고 많다고 소개했다[4]. 중국에서는 경제적으로 중요한 이매패이지만 남획 등으로 자연 생산량이 크게 줄었다고 보고되었다[2].\n\n"
  "국내에서는 전라북도 부안군 해안 마을 주민 10명에게서 조류 기생 흡충인 Acanthoparyphium tyosenense가 처음 발견되었는데, 이들은 인근 하구에서 잡은 여러 기수·해산 조개류를 먹었고 조사한 조개 가운데 동죽에서 이 흡충의 피낭유충이 확인되었다[22]. 이 사례는 국내 연안 주민이 동죽을 먹어 왔음을 보여 주는 의학 기록이다[22].\n\n"
  "국내 이용 역사(문헌 기록, 지역 음식)를 다룬 공공기관 자료는 확인하지 못함."},
 {"key": "biology", "title": "생물학적 특징·생태", "body":
  "동죽은 갯벌 퇴적물 속에 사는 내생(infaunal) 여과 섭식 이매패다[2]. 한국 금강 하구에서는 방조제 바깥 갯벌에 사는 우점 이매패 두 종 가운데 하나로 조사되었고, 안정동위원소 분석에서 저서 미세조류와 입자성 유기물의 먹이 기여가 계절에 따라 달랐다[26]. 중국 보하이해 북부에서 위 내용물을 유전자로 분석한 연구는 은편모조류·녹조류·와편모조류·황금색조류가 주된 먹이였다고 보고했다[27].\n\n"
  "황하 삼각주 북부 조간대의 동죽은 중조대와 저조대 사이에 형태 형질 차이가 있었고, 두 조대 모두에서 겨울 개체의 형태 형질과 습중량이 다른 계절보다 컸다[28]. 일본 연구는 동죽이 바다 기원 유기물을 골라 동화한다고 소개했다[34].\n\n"
  "국내 서해안 개체군의 산란기는 6–9월, 주 산란은 수온 24 °C 이상인 7–8월이라는 학회지 논문이 있으나, 이 내용은 WebSearch 요약으로만 보았고 원문은 확인하지 못함[32]. 수온을 10·20·30 °C로 24시간 바꾼 실험에서는 혈구 수와 식세포 활성, 리소자임 활성이 달라져 급격한 수온 변화가 면역 감시를 떨어뜨렸다[25]. 동죽은 여러 흡충의 제2중간숙주이기도 해, 국내 남서해안 동죽 10개체에서 Acanthoparyphium marilae 피낭유충 128개가 나왔다[24]."},
 {"key": "related_species", "title": "관련 종·이름", "body":
  "식약처 목록에서 동죽의 별칭은 '동조개'이며, 같은 속으로는 개량조개(Mactra chinensis, 영문 sunray surf clam, Chinese mactra)와 Mactra solidissima(학명 표기 Mactra solidissima Dillwyn, Spisula solidissima)가 따로 올라 있다[1]. 영문 'surf clam'은 동죽의 목록 영문명이지만, 개량조개의 영문명에도 'surf clam'이 들어가 있어 영문명만으로는 종이 구분되지 않는다[1].\n\n"
  "식용 조개 6종의 지질을 비교한 연구에서 동죽과 개량조개는 서로 다른 시료로 분석되었으며, 동죽 지질에서는 글리세로인지질 분자종이 513종 확인되었다[7]. 같은 연구진의 다른 분석에서 동죽은 EPA·DHA를 지닌 포스파티딜에탄올아민 분자종이 가장 많은 종으로 꼽혔다[8]. 따라서 개량조개 등 같은 속 조개의 성분값을 동죽 값으로 옮겨 쓰면 안 된다[7, 8].\n\n"
  "유전체 계통 분석에서 동죽과 바지락(Ruditapes philippinarum)은 약 2억 3,100만 년 전에 갈라진 것으로 추정되었다[2]. 같은 연안에서 바지락, 가무락조개(Cyclina sinensis) 등과 함께 채집해 비교한 연구가 여럿 있다[17, 23]."},
 {"key": "cultivation", "title": "양식·채취", "body":
  "중국 장쑤성 연안 갯벌은 동죽을 포함한 백합류 조개의 주요 양식지로, 2012년에 이 지역에서 62만 8천 톤이 넘는 조개가 수확되었다[17]. 다만 이 수치는 동죽·바지락·말백합류·가무락조개 등을 합친 값이다[17]. 중국 보하이해 북부 Geligang 갯벌에서는 동죽이 주요 경제 패류로 조사되었다[27].\n\n"
  "중국에서 동죽의 자연 생산량이 남획, 그리고 수온 급변에 따른 면역 저하 가능성 등으로 줄어 유전자원 보호가 시급하다는 지적이 있다[2]. 2022년 염색체 수준 유전체가 공개되어 고생산·빠른 성장·내병성 품종 육성의 기반 자료로 제시되었다[2]. 황하 삼각주 연구는 계절·조대별 형태와 먹이 자료가 자원 보전과 개체군 복원의 기초가 된다고 보았다[28].\n\n"
  "국내 동죽의 어획·양식 생산량(통계청 어업생산동향조사 등)과 지역별 통계는 이번 조사 환경에서 원자료를 열 수 없어 확인하지 못함. 세계 생산량(FAO) 자료도 확인하지 못함."},
 {"key": "processing", "title": "가공·이용 연구", "body":
  "동죽 살에서 얻은 다당류 분말(MVPS)은 다당류 함량이 95.8%였고, 물에 잘 녹으며 열에 안정한 비결정성 고분자였다[11]. 이 다당류를 1 M 염산으로 약하게 가수분해하면 중합도 1–7의 글루코올리고당이 생겼고, 시험관 항산화 시험에서 염산 가수분해물이 원래 다당류보다 활성이 강했다[12]. 산 가수분해물은 쥐의 에탄올·사염화탄소 간 손상 모델과 세포 실험에서 보호 효과를 보였으나, 사람 대상 연구는 확인하지 못함[13].\n\n"
  "동죽 단백질 가수분해물의 1 kDa 이하 분획에서 27개 펩타이드를 확인했고, 그 가운데 VVCVPW가 시험관에서 ACE 저해 IC50 4.07 μM으로 가장 강했다[9]. 다른 연구는 가수분해물에서 펩타이드 21개를 찾고 합성 펩타이드의 라디칼 소거 활성을 확인했다[10]. 바지락과 동죽에서 감칠맛 펩타이드 16개가 선별되었고 역치는 0.123–1.481 mmol/L였다[29].\n\n"
  "삶은 뒤 열풍 건조하는 가공에서는 70 °C 건조가 맛에 가장 좋았고, 휘발성 성분 38종이 확인되었다[30]. 동죽 살을 원료로 한 건강기능식품 생산실적은 확인하지 못함."},
 {"key": "genetics", "title": "유전 정보", "body":
  "2022년 중국 랴오닝성 다롄 개체 한 마리로 조립한 염색체 수준 유전체는 19개 유사염색체로 구성되었고 contig N50은 약 7.98 Mb였다[2]. 전체 길이는 초록에 939.32 Mb, 본문 표에 979,316,154 bp로 서로 다르게 적혀 있다[2]. k-mer로 추정한 유전체 크기는 865.63 Mb, 이형접합도는 3.34%였고, 반복서열은 약 51.79%, 단백질 암호 유전자는 29,315개, BUSCO 완전성은 98.4% 이상이었다[2].\n\n"
  "19개 염색체는 참가리비 계통(Patinopecten yessoensis)과 높은 동조성을 보여, 19개 염색체 핵형이 이매패 초기에 형성되었다는 해석을 뒷받침했다[2]. 늘어나거나 줄어든 유전자군 수는 초록(493·449개)과 본문(1,501·805개)에 서로 다르게 적혀 있다[2].\n\n"
  "미토콘드리아 유전체는 16,854 bp로 단백질 암호 유전자 12개, rRNA 유전자 2개, tRNA 유전자 20개를 지니며 atp8 유전자와 두 tRNA(Ser) 유전자가 없다[3]. 664 bp 비암호 영역의 97.89%가 반복서열인 점이 다른 백합목 조개와 다른 특징이다[3]. 카드뮴 노출 시 메탈로티오네인과 Cu-Zn SOD 유전자의 발현이 용량에 따라 늘어 이 두 유전자가 카드뮴 오염 지표로 제안되었다[33]."},
 {"key": "safety", "title": "안전성", "body":
  "식약처 「식품원료 목록」에서 동죽은 별도 조건 없이 '사용가능' 원료다[1]. 건강기능식품 고시형 원료로 등재된 기록을 찾지 못해 고시 섭취 시 주의사항도 없으며, 동죽을 따로 다룬 국내 공공기관의 패류독소·중금속 안전 정보는 확인하지 못함.\n\n"
  "알레르기: 조개의 주요 알레르겐은 트로포미오신이며, 동죽 트로포미오신은 초음파와 고온·고압을 함께 처리하면 알레르기 유발성이 약 68.1% 줄었다[16]. 기생충: 국내 서해안 동죽은 Himasthla alincia 피낭유충 양성률 98.9%였고 Acanthoparyphium tyosenense·Parvatrema 피낭유충도 검출되었다[23]. A. tyosenense는 부안군 주민의 사람 감염이 확인된 흡충이며, 동죽이 감염원 조개 가운데 하나로 지목되었다[22].\n\n"
  "패류독소: 중국 장쑤성 동죽 등 조개 4종 400여 시료에서 오카다산·디노피시스톡신 등 지용성 패류독소는 5–8월에 높았고 검출 농도는 EU 기준보다 훨씬 낮았으며, 아자스피르산·예소톡신·스피롤라이드는 검출되지 않았다[17]. 중금속: 보하이만 동죽 198개체 조사에서 세 구역의 코발트 위해지수(THQ)가 1을 넘었고[18], 라이저우만 조사에서는 근육 섭취 시 위해 기여가 가장 큰 원소가 비소였다[19]. 보하이해 연체동물 11종 장기 조사에서 동죽은 크롬 축적 경향이 큰 종으로 묶였다[20]. 보하이해·황해의 두 만에서 채집한 동죽의 다환방향족탄화수소는 122.68–367.21 ng/g(건중량)으로 섭취에 따른 발암 위험은 낮게 평가되었다[31]."},
]

compounds = [
 {"name": "Uridine", "name_ko": "우리딘", "class": "뉴클레오사이드", "role": "marker", "part": "살(분말)", "content_text": "많은 시료에서 주성분; 6월에 가장 높고 1월에 가장 낮음(수치는 원문 그림에만 있음)", "activity_ko": "동죽 품질 평가 지표로 제안된 뉴클레오사이드 8종 가운데 하나다[4]", "source": [4]},
 {"name": "Xanthine", "name_ko": "잔틴", "class": "퓨린 핵염기", "role": "marker", "part": "살(분말)", "content_text": "1189.84–2877.48 μg/g (채취 월별; 원문 표기 'μg·g', 분말 시료 기준으로 보이나 생/건 기준 명시 없음)", "activity_ko": "많은 시료에서 주성분으로 나타났다[4]", "source": [4]},
 {"name": "Hypoxanthine", "name_ko": "하이포잔틴", "class": "퓨린 핵염기", "role": "marker", "part": "살(분말)", "content_text": "정량 성분 가운데 가장 적음(수치는 원문 그림에만 있음)", "activity_ko": "HPLC-UV로 함께 정량한 핵염기다[4]", "source": [4]},
 {"name": "Inosine", "name_ko": "이노신", "class": "뉴클레오사이드", "role": "marker", "part": "살(분말)", "content_text": "정량됨(동죽 시료별 수치는 원문 그림에만 있음); 장쑤성 4개 산지 48시료에서 뉴클레오사이드·핵염기 10종 확인", "activity_ko": "산지와 채취 시기에 따라 함량이 달라 산지 구분 지표로 제안되었다[4, 5]", "source": [4, 5]},
 {"name": "Adenosine", "name_ko": "아데노신", "class": "뉴클레오사이드", "role": "marker", "part": "살(분말)", "content_text": "정량됨(수치는 원문 그림에만 있음); 교반 추출로는 추출되지 않음", "activity_ko": "추출법에 따라 정량값이 크게 달라지는 성분이다[4]", "source": [4]},
 {"name": "Eicosapentaenoic acid", "name_ko": "EPA(에이코사펜타엔산)", "class": "오메가-3 지방산", "role": "nutrient", "part": "살 알코올 추출물의 석유에테르 분획", "content_text": "18.49% (분획 지방산 중)", "activity_ko": "불포화지방산이 석유에테르 분획의 수산기 라디칼 소거 활성에 기여한다고 보았다[6]", "source": [6]},
 {"name": "Docosahexaenoic acid", "name_ko": "DHA(도코사헥사엔산)", "class": "오메가-3 지방산", "role": "nutrient", "part": "살 알코올 추출물의 석유에테르 분획", "content_text": "9.03% (분획 지방산 중)", "activity_ko": "EPA와 함께 동죽 인지질 분자종의 주요 지방산이다[6, 8]", "source": [6, 8]},
 {"name": "Phosphatidylethanolamine", "name_ko": "포스파티딜에탄올아민", "class": "글리세로인지질", "role": "nutrient", "part": "살 지질", "content_text": "동죽 지질에서 글리세로인지질 분자종 468종[8]·513종[7] 확인; 동죽 개별 함량은 초록에 없음", "activity_ko": "EPA·DHA를 지닌 포스파티딜에탄올아민 분자종이 6종 조개 가운데 동죽에 가장 많았다[7, 8]", "source": [7, 8]},
 {"name": "Taurine", "name_ko": "타우린", "class": "아미노산 유도체", "role": "nutrient", "part": "살 알코올 추출물의 물 분획", "content_text": "0.26% (분획 중; 아르기닌 1.79%, 티로신 0.38%, 시스테인 0.38%, 메티오닌 0.31%)", "activity_ko": "유리 아미노산과 올리고당이 물 분획의 항산화 활성에 기여한다고 보았다[6]", "source": [6]},
 {"name": "Glucan", "name_ko": "다당류(MVPS, 포도당 올리고당 전구체)", "class": "다당류", "role": "bioactive", "part": "살", "content_text": "추출 분말의 다당류 95.8%; 산 가수분해 시 중합도 1–7 글루코올리고당 생성", "activity_ko": "시험관 항산화와 쥐 간 손상 모델에서 보호 효과가 보고되었으나 사람 자료는 없다[11–13]", "source": [11, 12, 13]},
 {"name": "Glycosaminoglycan", "name_ko": "글리코사미노글리칸", "class": "황산화 다당류", "role": "bioactive", "part": "살", "content_text": "함량 수치는 확인하지 못함", "activity_ko": "쥐 정맥 주사 실험에서 0.125 mg/kg 이상 투여 시 심부정맥혈전을 억제했으며, 먹었을 때의 효과는 확인되지 않았다[14, 15]", "source": [14, 15]},
 {"name": "VVCVPW", "name_ko": "ACE 저해 펩타이드 VVCVPW", "class": "펩타이드", "role": "bioactive", "part": "살 단백질 가수분해물(1 kDa 이하 분획)", "content_text": "ACE 저해 IC50 4.07 μM (합성 펩타이드, 시험관)", "activity_ko": "시험관과 분자 도킹 결과로, 혈압에 대한 사람 효과는 확인되지 않았다[9]", "source": [9]},
 {"name": "Tropomyosin", "name_ko": "트로포미오신", "class": "근육 단백질(알레르겐)", "role": "bioactive", "part": "살", "content_text": "함량 수치는 확인하지 못함; 초음파+고온·고압 처리 시 알레르기 유발성 약 68.1% 감소", "activity_ko": "조개의 주요 알레르겐이다[16]", "source": [16]},
 {"name": "Perfluorooctanoic acid", "name_ko": "과불화옥탄산(PFOA)", "class": "환경 오염물질", "role": "bioactive", "part": "연체부", "content_text": "평균 31.3 ng/g(건중량), 보하이해 연안(조사 11종 연체동물 가운데 높은 축)", "activity_ko": "농도가 낮아 일상 섭취로 인한 위험은 낮다고 평가되었다[21]", "source": [21]},
]

assays = [
 {"role": "literature", "compound": "Nucleosides and nucleobases (uridine, inosine, guanosine, thymidine, adenosine, xanthine, thymine, hypoxanthine)", "compound_ko": "뉴클레오사이드·핵염기 8종", "part": "살(24시간 해감 후 발라내 -10 °C 보관, 분말 시료)",
  "content": "잔틴 1189.84–2877.48 μg/g(월별); 우리딘은 6월 최고·1월 최저, 하이포잔틴이 가장 적음 [4]",
  "method": "HPLC-UV",
  "conditions": {"instrument": "Waters Acquity HPLC, Waters 2487 UV 검출기", "column": "BioBasic-C18 (5 μm, 4.6 mm × 250 mm), in-line guard", "mobile_phase": "A 메탄올, B 물", "gradient": "0–6 min 1% A; 6–15 min 1–4% A; 15–45 min 4–30% A; 50% A 10분 세척; 1% A 5분 재평형", "flow": "0.50 mL/min", "temp": "30 °C", "detection": "UV 254 nm (초록에는 245 nm로 적혀 있음)", "injection": "10 μL", "sample_prep": "분말 4.0 g + 50% 메탄올 100 mL, 상온 초음파 추출 60분 2회, 원심분리 10분 후 0.45 μm 여과", "standard": "중국 국가약품생물제품검정소 표준품 8종", "linearity": "4개 이상 농도, 3반복(회귀식은 원문 표 1)", "lod": "< 0.32 μg/mL (S/N 3)", "loq": "< 1.01 μg/mL (S/N 10)", "recovery": "95.15–101.07% (RSD < 3.03%)"},
  "rationale": "동죽 품질 평가에 다당류·아미노산 대신 쓸 수 있는 지표로 뉴클레오사이드·핵염기를 제안했다; 전문(Methods) 확인[4]. 같은 계열 성분을 HPLC-DAD-MS로 48시료에서 정량해 산지 구분에 쓴 연구도 있다[5].",
  "source": [4, 5], "url": "https://doi.org/10.4103/0973-1296.111241", "source_kind": "paper"},
 {"role": "literature", "compound": "Lipophilic marine toxins (OA, DTX1, DTX2, PTX2, GYM, AZA1–3, YTX, SPX1)", "compound_ko": "지용성 패류독소 10종", "part": "살(24시간 해감 후 균질물; 동죽 포함 조개 4종)",
  "content": "조사 조개에서 GYM·PTX2·OA·DTX1·DTX2 검출, AZA1–3·YTX·SPX1 불검출; 5–8월에 최고, EU 기준보다 훨씬 낮음(종별 수치는 원문 그림, 종명 대응 확인 못함) [17]",
  "method": "SPE + UFLC-MS/MS (MRM)",
  "conditions": {"instrument": "Shimadzu Prominence UFLC + 5500 Q-Trap 질량분석기(TurboIonSpray)", "column": "Waters XBridge C18 (50 mm × 2.1 mm, 2.5 μm), 가드 카트리지", "mobile_phase": "A 아세토니트릴, B 5 mM 수산화암모늄 수용액", "gradient": "0–10 min 10–90% A; 10–12 min 90% A", "flow": "0.3 mL/min", "temp": "35 °C", "detection": "ESI ± MRM; 이온원 550 °C, IS +5.5 kV/−4.5 kV", "injection": "2 μL", "sample_prep": "균질물 5 g을 메탄올 25 mL로 초음파 추출 30분 3회, 25% 메탄올로 희석해 Bond Elut Plexa(60 mg) SPE, 20% 메탄올 세척, 0.5% 수산화암모늄 메탄올 용출; OA·DTX 총량은 2.5 M NaOH 76 °C 45분 알칼리 가수분해", "standard": "캐나다 NRC 인증 표준품, 기질 일치 검량", "linearity": "R² 0.9932–0.9996", "lod": "≤ 0.11 μg/kg", "loq": "< 0.34 μg/kg", "recovery": "76.7–100.0% (가수분해 OA·DTX 71.9–90.6%)"},
  "rationale": "동죽 등 장쑤성 주요 양식 조개의 지용성 패류독소 감시용으로 검증된 다성분 분석법이다; 전문 확인[17].",
  "source": [17], "url": "https://doi.org/10.3390/toxins8010008", "source_kind": "paper"},
 {"role": "literature", "compound": "Heavy metals (Cr, Mn, Co, Ni, Cu, Zn, As, Se, Mo, Cd, Sb, Pb)", "compound_ko": "중금속·미량원소 12종", "part": "연체부(보하이만 11개 지점 198개체)",
  "content": "Mn이 중금속 합의 22.08–77.03%, Zn 12.66–57.11%, Pb 0.45–1.04%; Co THQ 1.125·1.665·1.144(세 구역) [18]",
  "method": "ICP-MS",
  "conditions": {},
  "rationale": "섭취자 위해성(THQ, 최대 일일 섭취량) 평가를 위해 동죽의 금속을 정량했다; 초록만 확인, 전문 확인 못함[18].",
  "source": [18], "url": "https://doi.org/10.1016/j.marpolbul.2015.05.017", "source_kind": "paper"},
]

d = {
 "slug": "mactra-veneriformis", "name_ko": "동죽", "name_en": "Surf clam", "scientific_name": "Mactra veneriformis",
 "aliases": ["동조개", "Surf clam"],
 "sections": sections, "compounds": compounds, "markers": [], "assays": assays,
 "nutrients": [], "production": [], "gi": [], "orgs": [], "world": [], "sources": sources,
}
json.dump(d, open(os.path.join(D, "dossier.json"), "w"), ensure_ascii=False, indent=1)
print("ok", len(sources))
