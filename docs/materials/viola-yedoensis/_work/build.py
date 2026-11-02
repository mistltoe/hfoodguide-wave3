import json
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "dossier.json"
ACC = "2026-11-02"


def pm(n, title, pmid, doi=None, note="초록"):
    url = f"https://doi.org/{doi}" if doi else f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
    return {"n": n, "title": f"{title} ({note}) (PMID {pmid})", "url": url, "publisher": "PubMed", "accessed": ACC}


sources = [
    {"n": 1, "title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 호제비꽃잎(Viola yedoensis Makino, Field purpleflower violet; 이명 들제비꽃·들오랑캐꽃·씨름꽃·지정초), 사용가능부위: 잎, 사용가능; 같은 목록의 제비꽃(Viola mandshurica)·Chinese violet잎(Viola yezoensis)·향기제비꽃꽃(제한적사용) 등 제비꽃속 행 포함(로컬 원자료 I1020_20261013.json)",
     "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
    pm(2, "An integrated study of Violae Herba (Viola philippica) and five adulterants by morphology, chemical compositions and chloroplast genomes: insights into its certified plant origin — Chin Med 2022;17(1):32, PMC8892722", "35241112", "10.1186/s13020-022-00585-9", note="PMC 전문"),
    pm(3, "Application of chloroplast genome in the identification of Traditional Chinese Medicine Viola philippica — BMC Genomics 2022;23(1):540, PMC9327190", "35896957", "10.1186/s12864-022-08727-x"),
    pm(4, "Isolation and characterization of cytotoxic cyclotides from Viola philippica — Peptides 2011;32(8):1719-23", "21723349", "10.1016/j.peptides.2011.06.016"),
    pm(5, "A Comprehensive Review of the Phytochemistry and Therapeutic Efficacy of Viola yedoensis Makino — Molecules 2025;30(9):1922, PMC12073729", "40363729", "10.3390/molecules30091922", note="PMC 전문(총설)"),
    pm(6, "Violae Herba: A comprehensive review of the traditional uses, phytochemistry, pharmacology, quality control and clinical applications — J Ethnopharmacol 2025;351:119561", "40188895", "10.1016/j.jep.2025.119561"),
    pm(7, "Flavone C-glycosides from Viola yedoensis MAKINO — Chem Pharm Bull (Tokyo) 2003;51(10):1204-7", "14519932", "10.1248/cpb.51.1204"),
    pm(8, "A new dicoumarin and anticoagulant activity from Viola yedoensis Makino — Fitoterapia 2009;80(5):283-5", "19306914", "10.1016/j.fitote.2009.03.005"),
    pm(9, "Collagenase inhibitors from Viola yedoensis — J Nat Med 2013;67(1):240-5", "22529049", "10.1007/s11418-012-0665-8"),
    pm(10, "Protective Effect of n-Butanol Extract from Viola yedoensis on Immunological Liver Injury — Chem Biodivers 2021;18(6):e2001043", "33929783", "10.1002/cbdv.202001043"),
    pm(11, "Chemical identification of the Viola phillipina extracts and their anti-acne activity: A comparison with isotretinoin and salicylic acid — Fitoterapia 2026;191:107238", "41951179", "10.1016/j.fitote.2026.107238"),
    pm(12, "Rapid separation and identification of anthocyanins from flowers of Viola yedoensis and V. prionantha by HPLC-PDA-ESI-MS — Phytochem Anal 2012;23(1):16-22", "21523841", "10.1002/pca.1320"),
    pm(13, "Anti-HIV cyclotides from the Chinese medicinal herb Viola yedoensis — J Nat Prod 2008;71(1):47-52, PMC6327322", "18081258", "10.1021/np070393g"),
    pm(14, "[A cyclotide against influenza A H1N1 virus from Viola yedoensis] — Yao Xue Xue Bao 2014;49(6):905-12", "25212039"),
    pm(15, "Anti-complement sesquiterpenes from Viola yedoensis — Fitoterapia 2015;101:73-9", "25562805", "10.1016/j.fitote.2014.12.015"),
    pm(16, "[Anti-complement alkaloids from whole plants of Viola yedoensis] — Zhongguo Zhong Yao Za Zhi 2017;42(24):4794-4800", "29493149", "10.19540/j.cnki.cjcmm.20170928.012"),
    pm(17, "Inhibition of growth of human immunodeficiency virus in vitro by crude extracts of Chinese medicinal herbs — Antiviral Res 1988;9(3):163-75", "2840849", "10.1016/0166-3542(88)90001-0"),
    pm(18, "Isolation, purification and partial characterization of an active anti-HIV compound from the Chinese medicinal herb viola yedoensis — Antiviral Res 1988;10(1-3):107-16", "3232967", "10.1016/0166-3542(88)90019-8"),
    pm(19, "Effects of herbal medicinal formulas on suppressing viral replication and modulating immune responses — Am J Chin Med 2010;38(1):173-90", "20128053", "10.1142/S0192415X10007749"),
    pm(20, "[Effects of light intensities on growth, physiological characteristic and chemical composition of Viola yedoensis] — Zhongguo Zhong Yao Za Zhi 2019;44(6):1119-1125", "30989973", "10.19540/j.cnki.cjcmm.20181226.008"),
    pm(21, "[Effects of light intensity on cleaning away heat property of Viola yedoensis] — Zhongguo Zhong Yao Za Zhi 2020;45(16):3812-3818", "32893575", "10.19540/j.cnki.cjcmm.20200506.108"),
    pm(22, "Transcriptome sequencing and differential gene expression analysis in Viola yedoensis Makino (Fam. Violaceae) responsive to cadmium (Cd) pollution — Biochem Biophys Res Commun 2015;459(1):60-5", "25725154", "10.1016/j.bbrc.2015.02.066"),
    pm(23, "Gibberellins are required for dimorphic flower development in Viola philippica — Plant Sci 2021;303:110749", "33487338", "10.1016/j.plantsci.2020.110749"),
    pm(24, "Assembly and comparative analysis of the complete mitochondrial genome of Viola philippica (Malpighiales, Violaceae) — Planta 2026;264(2)", "42400680", "10.1007/s00425-026-05071-2"),
    pm(25, "Structural basis for proenzyme maturation, substrate recognition, and ligation by a hyperactive peptide asparaginyl ligase — Plant Cell 2022;34(12):4936-4949, PMC9709980", "36099055", "10.1093/plcell/koac281"),
    pm(26, "[Screening and validation of RT-qPCR reference genes of Viola yedoensis under different light intensities] — Zhongguo Zhong Yao Za Zhi 2021;46(21):5620-5626", "34951215", "10.19540/j.cnki.cjcmm.20210816.103"),
    pm(27, "Viola yedoensis liposoluble fraction ameliorates lipopolysaccharide-induced acute lung injury in mice — Am J Chin Med 2012;40(5):1007-18", "22928831", "10.1142/S0192415X12500747"),
    pm(28, "Anti-inflammatory effects of Viola yedoensis and the application of cell extraction methods for investigating bioactive constituents in macrophages — BMC Complement Altern Med 2016;16:180, PMC4908784", "27301877", "10.1186/s12906-016-1142-9"),
    pm(29, "Antibacterial activity of the Chinese traditional medicine, Zi Hua Di Ding — Phytother Res 2004;18(6):497-500", "15287078", "10.1002/ptr.1497"),
    pm(30, "Viola yedoensis Makino alleviates lipopolysaccharide-induced intestinal oxidative stress and inflammatory response by regulating the gut microbiota and NF-κB-NLRP3/Nrf2-MAPK signaling pathway in broiler — Ecotoxicol Environ Saf 2024;282:116692", "38971097", "10.1016/j.ecoenv.2024.116692"),
    pm(31, "Approach to the study of flavone di-C-glycosides by HPLC-tandem ion trap mass spectrometry and its application to characterization of flavonoid composition in Viola yedoensis — J Mass Spectrom 2014;49(10):1010-24", "25303391", "10.1002/jms.3413"),
    pm(32, "[Study on antibacterial active components from Viola yedoensis] — Zhongguo Zhong Yao Za Zhi 2011;36(19):2666-71", "22242426"),
    pm(33, "Erding Formula in hyperuricaemia treatment: unfolding traditional Chinese herbal compatibility using modern pharmaceutical approaches — J Pharm Pharmacol 2018;70(1):124-132", "29057475", "10.1111/jphp.12840"),
    pm(34, "[Studies on chemical constituents from herbs of Viola yedoensis] — Zhongguo Zhong Yao Za Zhi 2009;34(9):1114-6", "19685747"),
    pm(35, "DELLA gene expression may be involved in chasmogamous-cleistogamous flower development and regulate the expression of B-class floral homeotic genes in Viola philippica — Plant Physiol Biochem 2026;231:111031", "41570632", "10.1016/j.plaphy.2026.111031"),
]

S = {}
S["overview"] = ("한눈에 보기", """호제비꽃(Viola yedoensis Makino)은 제비꽃과(Violaceae) 제비꽃속의 여러해살이풀로, 땅위줄기 없이 뿌리에서 잎이 모여 나고 보라색 꽃을 피운다[1, 5]. 식약처 「식품원료 목록」에는 영어 이름 Field purpleflower violet, 이명 들제비꽃·들오랑캐꽃·씨름꽃·지정초로 '호제비꽃잎'이 올라 있다[1]. 사용 조건은 '사용가능부위 : 잎'인 사용가능 원료이므로 식품에는 잎만 쓸 수 있고, 뿌리를 포함한 전초는 사용 부위로 올라 있지 않다[1]. 이 종을 원재료로 하는 건강기능식품 고시형 원료는 확인하지 못함.

중국에서는 이 식물의 말린 전초를 자화지정(紫花地丁, Violae Herba)이라는 약재로 써 왔다[5, 6]. 다만 국제 식물 분류에서는 V. yedoensis를 Viola philippica Cav.의 이명으로 보는 견해가 있고, 중국 시장의 자화지정은 여러 제비꽃속 종이 섞인 다기원 약재로 보고되었다[2, 3]. 연구된 주요 성분은 에스쿨레틴 같은 쿠마린류, 샤프토사이드 등 플라본 C-배당체, 고리형 펩타이드인 사이클로타이드다[5, 7, 13]. 대부분의 연구는 식품 사용 부위인 잎이 아니라 전초로 이루어졌다[5].""")

S["history"] = ("역사와 이용", """자화지정은 명나라 『본초강목』에 열을 내리고 독을 풀며 부기를 가라앉히는 약으로 기록되었다고 총설은 정리했다[5]. 중국약전에는 1963년판부터 수재되었고, 2020년판은 말린 전초를 종기·옹종·단독·뱀에 물린 데 쓰며 하루 15–30 g을 쓴다고 정했다고 총설은 전한다[5]. 다른 연구는 V. yedoensis가 1977년판부터 자화지정의 유일한 기원식물로 지정되었다고 적어, 수재 시점에 대한 서술이 출처마다 다르다[2].

역사 문헌 속의 '자화지정'에는 콩과·양귀비과·원지과·제비꽃과의 서로 다른 식물이 포함되어 있었다[2]. 실제로 자화지정으로 쓰이는 식물로 V. yedoensis 외에 V. prionantha, 콩과의 Gueldenstaedtia verna, 양귀비과의 Corydalis bungeana가 함께 연구되었다[29]. 1980년대에는 항감염 약초 27종의 열수 추출물 선별에서 이 약재 추출물이 시험관 내 HIV 증식을 억제해 주목받았다[17]. 오늘날 중국에서는 아토피 피부염 등 피부 질환에 쓰는 복합 처방, 고요산혈증 연구에 쓰인 중국약전 수재 처방 등에 들어간다[5, 33]. 우리나라에서 잎을 나물로 먹어 온 전통 기록은 확인하지 못함.""")

S["biology"] = ("식물학적 특징", """Flora of China의 기재를 옮긴 총설에 따르면 이 식물은 땅위줄기가 없고, 꽃 필 때 높이 4–14 cm, 열매 맺을 때 20 cm 넘게 자란다[5]. 뿌리줄기는 짧고 곧으며, 잎은 뿌리에서 모여 나 로제트를 이룬다[5]. 위쪽 잎은 긴 타원형~좁은 달걀 모양 피침형으로 길이 1.5–4 cm, 너비 0.5–1 cm이고, 열매 시기에는 길이 10 cm, 너비 4 cm까지 커진다[5]. 턱잎은 막질로 길이 1.5–2.5 cm이고 2/3–4/5가 잎자루와 붙어 있다[5]. 꽃은 보라색이나 연보라색이며, 꿀주머니(거)는 가늘고 길이 4–8 mm다[5].

분포는 중국 여러 성과 한국·일본·러시아 극동이며, 햇볕이 잘 드는 밭둑·빈터·풀밭 비탈·숲 가장자리에서 자란다[5]. V. philippica라는 이름으로 수행된 연구에서는 짧은 낮 조건에서 피는 열린꽃(개방화)과, 낮이 길어지면 생기는 닫힌꽃(폐쇄화)을 한 포기에서 만들었다[23, 35]. 닫힌꽃 꽃눈에서는 활성 지베렐린 함량이 열린꽃보다 높았다[23]. 이 연구 시료가 국내의 호제비꽃과 같은 개체군인지는 확인하지 못함.""")

S["related_species"] = ("이름과 가까운 종", """자화지정을 다룬 연구는 중국약전이 1977년판부터 기원으로 정한 V. yedoensis Makino가 현재 Viola philippica Cav.의 이명으로 취급된다고 적었다[2]. 다른 연구도 V. philippica를 자화지정의 유일한 기원식물로 보았다[3]. 그러나 중국약전은 여전히 V. yedoensis를 자화지정의 기원으로 적고 있어 두 이름이 섞여 쓰인다[2, 5]. 이 자료는 V. yedoensis 또는 V. philippica로 표기된 시료만 옮겼고, 각 값에 시료 학명을 밝혔다[2, 3]. V. philippica 이름의 시료에서는 사이클로타이드 16종(새 성분 Viphi A–H 포함)이 분리되었고 일부는 암세포 독성을 보였다[4].

자화지정 약재 18배치를 조사한 연구에서 시판품과 국가 표준 대조약재는 주로 V. prionantha였고, 법정 기원종 V. philippica에서는 에스쿨레틴·에스쿨린이 HPLC에서 거의 검출되지 않았다[2]. 엽록체 유전체 연구도 보라색 꽃을 피우는 여러 제비꽃속 종이 자화지정으로 잘못 쓰여 왔다고 보고했다[3]. 따라서 '자화지정' 연구 결과를 곧바로 호제비꽃 잎의 성질로 볼 수는 없다[2].

식약처 목록에는 제비꽃(Viola mandshurica), 삼색제비꽃(Viola tricolor), 향기제비꽃(Viola odorata), 금강제비꽃, 졸방제비꽃 등이 별도 원료로 올라 있으며 이 자료에 섞지 않았다[1]. 같은 목록의 'Chinese violet잎'은 학명이 Viola yezoensis로 적힌 별개 항목이다[1].""")

S["cultivation"] = ("재배와 산지", """중국 시장의 자화지정은 재배보다 야생 채취로 주로 조달되어, 약전이 정한 종만 모으기 어렵다고 보고되었다[2]. 재배 조건 연구로는 전광 대비 100%·80%·50%·35%·5% 빛에서 키운 시험이 있으며, 35–100% 사이에서는 생물량에 유의한 차이가 없었으나 5% 처리에서는 유의하게 적었다[20]. 같은 시험에서 5% 빛 처리는 엽록체 구조가 흐트러지고 녹말 알갱이가 줄었다[20].

빛의 세기는 약효 실험에도 영향을 주어, 전광에 가까운 빛에서 키운 시료일수록 생쥐 염증 모델에서 체온 저하와 부종 완화 효과가 컸다[21]. 이 식물은 카드뮴 오염 지역에 적응한 약용식물로 소개되었고, 카드뮴 처리 개체에서 892개 유전자의 발현이 달라졌다[22]. 식용 잎을 얻을 때 토양 중금속 관리에 대한 공공기관 권고는 확인하지 못함.

국내 재배 면적·생산량 통계(통계청·농식품부 특용작물 생산실적)에서 호제비꽃이나 제비꽃 품목은 확인하지 못함. 지리적 표시 등록이나 생산자 단체도 확인하지 못함.""")

S["processing"] = ("가공과 이용", """식약처 목록상 이 종은 잎(호제비꽃잎)만 식품 원료로 쓸 수 있다[1]. 잎의 데침·건조 같은 식품 가공 연구는 확인하지 못함.

약재로서의 품질 기준은 에스쿨레틴이며, 중국약전 2020년판은 건조물 기준 0.20% 이상을 요구한다고 총설은 정리했다[5]. 전초를 80% 메탄올로 초음파 추출해 HPLC로 비교한 연구는 시클로리인·에스쿨린·에스쿨레틴·프리오난토사이드를 감별 지표성분으로 제안했다[2]. V. philippica 추출물에서는 용매에 따라 성분이 달라, 디클로로메탄·에틸아세테이트 분획에 에스쿨레틴이, 에탄올·부탄올 분획에 시클로리인이 많았다[11].

전초 추출물은 실험동물 연구에도 쓰였는데, 육계 사료에 0.5·1.5·4.5% 넣은 시험에서 LPS로 유발한 장 손상이 줄었다[30]. 석유에테르 분획을 2·4·8 mg/kg 먹인 생쥐에서는 LPS 급성 폐 손상이 완화되었다[27]. 에탄올 추출물은 LPS로 자극한 대식세포에서 일산화질소와 TNF-α·IL-6·IL-1β 생성을 억제했다[28]. 총설은 이 식물이 허브차·기능성 식품 원료로도 쓰인다고 소개했다[5]. 국내 건강기능식품 생산실적에서 이 원료 품목은 확인하지 못함.""")

S["genetics"] = ("유전 정보", """V. yedoensis의 전사체를 처음 분석한 연구는 카드뮴 처리·무처리 시료에서 109,800개의 유전자 단위(unigene)를 조립했다[22]. 빛 세기 실험용으로 검증한 정량 PCR 기준 유전자로는 SAMDC·CYP·Actin이 적합했고 GAPDH는 가장 불안정했다[26]. 이 종의 사이클로타이드 고리화에 관여하는 사이클로타이드를 만드는 이 식물의 펩타이드 아스파라기닐 연결효소 VyPAL2는 결정 구조가 밝혀져, 기질 인식과 연결 반응의 원리가 제시되었다[25].

자화지정과 위품 5종의 엽록체 유전체는 156,395–158,067 bp였고, 전체 엽록체 유전체를 '슈퍼바코드'로 쓰면 종 구별력이 가장 좋았다[2]. 다른 연구도 24개 엽록체 유전체에서 종 구별용 고변이 구간 16곳을 찾았다[3]. V. philippica 이름으로 해독된 미토콘드리아 유전체는 446,926 bp, GC 44.31%이며 단백질 암호 유전자 38개를 담고 있었다[24]. 염색체 수와 핵 유전체 크기는 확인하지 못함.""")

S["safety"] = ("안전성", """식약처 「식품원료 목록」에서 호제비꽃은 잎만 쓸 수 있는 사용가능 원료이고, 꽃·뿌리·전초는 사용 부위로 올라 있지 않다[1]. 국내 공공기관의 알레르기·잔류물질·독성 성분 정보는 확인하지 못함.

생쥐에 이 식물 추출물을 8주 먹인 시험에서는 간·신장 독성이 관찰되지 않았다[19]. 반면 시험관에서는 항HIV 활성을 보인 추출물에 세포독성이 함께 있었고, 사이클로타이드는 적혈구 용혈 활성을 보였다[13, 18]. 이 식물에서 분리한 이중 쿠마린(디머에스쿨레틴·유포르베틴)과 에스쿨레틴은 시험관 혈액응고 시간을 늘렸다[8]. 항응고제를 먹는 사람에 대한 상호작용 자료는 확인하지 못함.

총설은 형태가 비슷한 다른 제비꽃속 종이 섞이면 약효가 달라질 수 있고, 한 종은 장운동을 촉진해 설사를 일으킬 수 있다고 경고했다[5]. 시판 자화지정이 주로 다른 종(V. prionantha)이라는 보고도 있어, 약재를 식품용 잎과 같은 것으로 보면 안 된다[2]. 잎을 먹는 사람 대상 안전성 시험은 확인하지 못함.""")

compounds = [
    {"name": "Esculetin", "name_ko": "에스쿨레틴", "class": "쿠마린", "role": "marker", "part": "전초",
     "content_text": "중국약전 2020년판 기준 건조물 0.20% 이상(총설 인용); 반정량 0.484 ± 0.028%(총설 인용); 법정 기원종 V. philippica 시료에서는 HPLC에서 거의 검출 안 됨; V. philippica 디클로로메탄 추출물 308.125 ± 0.151 µg/mg, 에틸아세테이트 추출물 344.748 ± 0.071 µg/mg",
     "activity_ko": "자화지정 품질 지표성분; 시험관 항응고·항균(동물 병원균 MIC 0.031–0.313 g/L)", "source": [2, 5, 8, 11, 32]},
    {"name": "Esculin", "name_ko": "에스쿨린", "class": "쿠마린 배당체", "role": "marker", "part": "전초",
     "content_text": "n-부탄올 추출물에서 분리(함량 수치 없음); 감별 지표성분으로 제안", "activity_ko": "자화지정 감별 지표성분", "source": [2, 10]},
    {"name": "Cichoriin", "name_ko": "시클로리인(치코리인)", "class": "쿠마린 배당체", "role": "marker", "part": "전초",
     "content_text": "V. philippica 에탄올 추출물 56.494 ± 0.019 µg/mg, n-부탄올 추출물 42.888 ± 0.069 µg/mg", "activity_ko": "자화지정 감별 지표성분", "source": [2, 10, 11]},
    {"name": "Prionanthoside", "name_ko": "프리오난토사이드", "class": "쿠마린 배당체", "role": "marker", "part": "전초",
     "content_text": "n-부탄올 추출물에서 분리(함량 수치 없음)", "activity_ko": "자화지정 감별 지표성분", "source": [2, 10]},
    {"name": "Scopoletin", "name_ko": "스코폴레틴", "class": "쿠마린", "role": "bioactive", "part": "전초",
     "content_text": "아세톤·메탄올 추출물에서 분리(함량 수치 없음)", "activity_ko": "콜라게나제 억제 IC50 1.8 µM", "source": [9, 32]},
    {"name": "Dimeresculetin", "name_ko": "디머에스쿨레틴", "class": "이중 쿠마린", "role": "bioactive", "part": "전초(건조)",
     "content_text": "에틸아세테이트 추출물에서 새로 분리(함량 수치 없음)", "activity_ko": "시험관 항응고(APTT·PT·TT 연장)", "source": [8]},
    {"name": "Schaftoside", "name_ko": "샤프토사이드", "class": "플라본 C-배당체", "role": "bioactive", "part": "전초",
     "content_text": "분리 성분(함량 수치 없음)", "activity_ko": "이 종의 대표 플라본 이중 C-배당체", "source": [7, 31]},
    {"name": "Isoschaftoside", "name_ko": "이소샤프토사이드", "class": "플라본 C-배당체", "role": "bioactive", "part": "전초",
     "content_text": "분리 성분(함량 수치 없음)", "activity_ko": "플라본 이중 C-배당체", "source": [7]},
    {"name": "Vicenin-2", "name_ko": "비세닌-2", "class": "플라본 C-배당체", "role": "bioactive", "part": "전초",
     "content_text": "분리 성분(함량 수치 없음)", "activity_ko": "플라본 이중 C-배당체", "source": [7, 9]},
    {"name": "Apigenin 6-C-alpha-L-arabinopyranosyl-8-C-beta-D-xylopyranoside", "name_ko": "아피제닌 6-C-아라비노실-8-C-자일로사이드", "class": "플라본 C-배당체", "role": "bioactive", "part": "전초",
     "content_text": "분리 성분(함량 수치 없음)", "activity_ko": "제비꽃속에서만 보고된 플라본 C-배당체", "source": [7]},
    {"name": "Rutin", "name_ko": "루틴", "class": "플라보놀 배당체", "role": "bioactive", "part": "전초",
     "content_text": "분리 성분(함량 수치 없음)", "activity_ko": "플라보놀 배당체", "source": [9]},
    {"name": "Cycloviolacin Y5", "name_ko": "사이클로비올라신 Y5", "class": "사이클로타이드(고리형 펩타이드)", "role": "bioactive", "part": "전초",
     "content_text": "분리 성분(함량 보고 없음)", "activity_ko": "시험관 항HIV(이 종 사이클로타이드 중 가장 강함); 적혈구 용혈", "source": [13]},
    {"name": "Cycloviolacin VY1", "name_ko": "사이클로비올라신 VY1", "class": "사이클로타이드(고리형 펩타이드)", "role": "bioactive", "part": "전초",
     "content_text": "분리 성분(함량 보고 없음)", "activity_ko": "인플루엔자 A H1N1 바이러스 억제 IC50 (2.27 ± 0.20) µg/mL", "source": [14]},
    {"name": "Yedoensin A", "name_ko": "예도엔신 A", "class": "저마크레인 세스퀴테르펜", "role": "bioactive", "part": "전초",
     "content_text": "새로 분리(함량 보고 없음)", "activity_ko": "보체 억제 CH50 0.14–0.37 mg/mL 범위(함께 분리한 성분 포함)", "source": [15]},
    {"name": "Aurantiamide acetate", "name_ko": "아우란티아마이드 아세테이트", "class": "알칼로이드(다이펩타이드 유도체)", "role": "bioactive", "part": "전초",
     "content_text": "95% 에탄올 추출물에서 분리한 알칼로이드 15종 중 하나(함량 보고 없음)", "activity_ko": "알칼로이드 15종의 보체 억제 CH50 0.12–0.33 g/L 범위", "source": [16]},
    {"name": "Loliolide", "name_ko": "롤리올라이드", "class": "모노테르펜 락톤", "role": "bioactive", "part": "전초",
     "content_text": "전초에서 처음 분리(함량 보고 없음)", "activity_ko": "분리 성분(활성 보고 없음)", "source": [34]},
    {"name": "Delphinidin", "name_ko": "델피니딘 계열 안토시아닌", "class": "안토시아닌", "role": "bioactive", "part": "꽃",
     "content_text": "꽃에서 안토시아닌 14종 분리·동정(V. prionantha 와 함께 분석; 함량 수치는 초록에 없음)", "activity_ko": "꽃 색소", "source": [12]},
]

blank = {k: "" for k in ["instrument", "column", "mobile_phase", "gradient", "flow", "temp", "detection", "injection", "sample_prep", "standard", "linearity", "lod", "loq", "recovery"]}

assays = [
    {"role": "literature", "compound": "Cichoriin, esculin, esculetin, prionanthoside", "compound_ko": "시클로리인·에스쿨린·에스쿨레틴·프리오난토사이드",
     "part": "전초 건조 분말(시판 자화지정 18배치와 제비꽃속 6종 야생 시료 42점)", "content": "",
     "method": "HPLC-DAD(성분 확인은 HPLC-Triple-TOF-MS/MS)",
     "conditions": dict(blank, **{
         "instrument": "Agilent 1260 HPLC-DAD; AB SCIEX TripleTOF 4600",
         "column": "Agilent ZORBAX SB-C18, 4.6 × 250 mm, 5 µm",
         "mobile_phase": "A: 0.4% 아세트산 수용액(v/v), B: 메탄올",
         "gradient": "0–10분 B 5–25%, 10–18분 25–30%, 18–30분 30–35%, 30–50분 35–45%, 50–60분 45–95%",
         "flow": "1 mL/min", "temp": "25 °C", "detection": "DAD 345 nm; MS/MS 음·양이온 모드 m/z 100–1500, 이온원 −4500 V/5500 V, 550 °C, 충돌에너지 44 V",
         "injection": "20 µL",
         "sample_prep": "건조 분말 1.0 g(60메시)을 80% 메탄올 15 mL로 실온 30분 초음파 추출, 10,000 rpm 15분 원심분리, 80% 메탄올로 25 mL 정용 후 0.22 µm 여과",
         "standard": "에스쿨레틴 표준품·자화지정 대조약재(중국 국가식품약품검정연구원)"}),
     "rationale": "자화지정 감별용 특징 크로마토그램을 만든 방법으로, 네 쿠마린을 지표성분으로 정했다. 전문(Methods)에서 조건을 옮겼으며, 정량 함량은 본문에 없고 법정 기원종 V. philippica에서는 에스쿨린·에스쿨레틴이 거의 검출되지 않았다고만 적혀 있다[2].",
     "source": [2], "url": "https://doi.org/10.1186/s13020-022-00585-9", "source_kind": "paper"},
    {"role": "literature", "compound": "Esculetin (6,7-dihydroxycoumarin), cichoriin", "compound_ko": "에스쿨레틴·시클로리인",
     "part": "V. philippica 용매별 추출물", "content": "에스쿨레틴: 디클로로메탄 추출물 308.125 ± 0.151 µg/mg, 에틸아세테이트 추출물 344.748 ± 0.071 µg/mg; 시클로리인: 에탄올 추출물 56.494 ± 0.019 µg/mg, n-부탄올 추출물 42.888 ± 0.069 µg/mg",
     "method": "HPLC", "conditions": dict(blank),
     "rationale": "약전 지표성분인 에스쿨레틴과 배당체 시클로리인이 추출 용매에 따라 어떻게 나뉘는지 정량한 연구다. 전문 확인 못함: 초록에는 함량만 있고 칼럼·이동상 등 조건이 없으며, 시료 학명은 V. philippica로 적혀 있다[11].",
     "source": [11], "url": "https://doi.org/10.1016/j.fitote.2026.107238", "source_kind": "paper"},
    {"role": "literature", "compound": "Anthocyanins (delphinidin, cyanidin, petunidin, malvidin, peonidin glycosides)", "compound_ko": "안토시아닌 14종",
     "part": "꽃", "content": "",
     "method": "HPLC-PDA-ESI-MS", "conditions": dict(blank),
     "rationale": "꽃 색소인 안토시아닌의 아글리콘·아실화 양상으로 V. yedoensis와 V. prionantha를 비교한 방법이다. 전문 확인 못함: 초록에는 메탄올-물-포름산-TFA(70:27:2:1) 추출, TSK-GEL ODS-80Ts(150 × 4.6 mm) 칼럼, 10% 포름산 수용액과 포름산-아세토니트릴-물(10:40:50) 기울기, 검량선 r² 0.9995만 있다. 식품 사용 부위(잎)가 아닌 꽃의 자료다[12].",
     "source": [12], "url": "https://doi.org/10.1002/pca.1320", "source_kind": "paper"},
]

d = {
    "slug": "viola-yedoensis", "name_ko": "호제비", "name_en": "Field purpleflower violet",
    "scientific_name": "Viola yedoensis Makino",
    "aliases": ["호제비꽃", "호제비꽃잎", "들제비꽃", "들오랑캐꽃", "씨름꽃", "지정초", "자화지정(紫花地丁)", "Violae Herba", "Viola philippica Cav.(이명 처리)"],
    "sections": [{"key": k, "title": t, "body": b} for k, (t, b) in S.items()],
    "compounds": compounds, "markers": [], "nutrients": [], "assays": assays,
    "production": [], "world": [], "gi": [], "orgs": [], "sources": sources,
}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for k, (t, b) in S.items():
    print(k, len(b))
