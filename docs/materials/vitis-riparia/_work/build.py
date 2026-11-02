import json
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "dossier.json"
A = "2026-11-02"

S = [
 ("식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 사막포도열매(Vitis riparia Michx.; 이명 리파리아머루; 영어명 Riverbank grape), 사용가능, 사용가능부위: 열매; 같은 속 Desert grape열매(Vitis girdiana)·Frost grape열매(Vitis vulpina)·California wild grape열매(Vitis californica)·왕머루열매·머루·로툰디폴리아머루열매 행 대조 (로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json)",
  "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "식품의약품안전처", "2026-10-13"),
 ("De novo phased assembly of the Vitis riparia grape genome — Sci Data 2019;6:127 (PMID 31324816, PMC6642119, 전문 확인)", "https://doi.org/10.1038/s41597-019-0133-3", "PubMed", A),
 ("Draft genome of the Native American cold hardy grapevine Vitis riparia Michx. 'Manitoba 37' — Hortic Res 2020;7:92 (PMID 32528704, PMC7261805, 초록 확인)", "https://doi.org/10.1038/s41438-020-0316-2", "PubMed", A),
 ("Berry Anthocyanin, Acid, and Volatile Trait Analyses in a Grapevine-Interspecific F2 Population Using an Integrated GBS and rhAmpSeq Genetic Map — Plants (Basel) 2022;11(5):696 (PMID 35270166, PMC8912348, 전문 확인)", "https://doi.org/10.3390/plants11050696", "PubMed", A),
 ("Next Generation Mapping of Enological Traits in an F2 Interspecific Grapevine Hybrid Family — PLoS One 2016;11(3):e0149560 (PMID 26974672, 초록 확인)", "https://doi.org/10.1371/journal.pone.0149560", "PubMed", A),
 ("Comparison of odor-active compounds in grapes and wines from Vitis vinifera and non-foxy American grape species — J Agric Food Chem 2011 (PMID 21879766, 초록 확인)", "https://doi.org/10.1021/jf2026204", "PubMed", A),
 ("Extracts of Phenolic Compounds from Seeds of Three Wild Grapevines — Comparison of Their Antioxidant Activities and the Content of Phenolic Compounds — Int J Mol Sci 2012;13(3):3444-3457 (PMID 22489161, PMC3317721, 전문 확인)", "https://doi.org/10.3390/ijms13033444", "PubMed", A),
 ("Characterization of Antioxidant and Antimicrobial Activity and Phenolic Compound Profile of Extracts from Seeds of Different Vitis Species — Molecules 2023;28(13):4924 (PMID 37446586, PMC10343412, 전문 확인)", "https://doi.org/10.3390/molecules28134924", "PubMed", A),
 ("Extractable amounts of trans-resveratrol in seed and berry skin in Vitis evaluated at the germplasm level — J Agric Food Chem 2006;54(23):8804-11 (PMID 17090126, 초록 확인)", "https://doi.org/10.1021/jf061722y", "PubMed", A),
 ("Stilbenoid profiles of canes from Vitis and Muscadinia species — J Agric Food Chem 2013 (PMID 23270496, 초록 확인)", "https://doi.org/10.1021/jf303843z", "PubMed", A),
 ("Characterizing the causes and consequences of calcium oxalate crystal presence in Vitis riparia — Am J Bot 2026;113(3):e70173 (PMID 41804112, 초록 확인)", "https://doi.org/10.1002/ajb2.70173", "PubMed", A),
 ("Layered stomatal immunity contributes to resistance of Vitis riparia against downy mildew Plasmopara viticola — J Exp Bot 2026;77(4):1324-1337 (PMID 41206614, 초록 확인)", "https://doi.org/10.1093/jxb/eraf491", "PubMed", A),
 ("A framework map from grapevine V3125 x rootstock cultivar 'Börner' (Vitis riparia x Vitis cinerea) to localize genetic determinants of phylloxera root resistance — Theor Appl Genet 2009;119(6):1039-51 (PMID 19626311, 초록 확인)", "https://doi.org/10.1007/s00122-009-1107-1", "PubMed", A),
 ("Genetic linkage map of the interspecific grape rootstock cross Ramsey (Vitis champinii) x Riparia Gloire (Vitis riparia) — Theor Appl Genet 2006;112(8):1582-92 (PMID 16607514, 초록 확인)", "https://doi.org/10.1007/s00122-006-0264-8", "PubMed", A),
 ("Transcript profiling in Vitis riparia during chilling requirement fulfillment reveals coordination of gene expression patterns with optimized bud break — Funct Integr Genomics 2009;9(1):81-96 (PMID 18633655, 초록 확인)", "https://doi.org/10.1007/s10142-008-0090-y", "PubMed", A),
 ("CBF4 is a unique member of the CBF transcription factor family of Vitis vinifera and Vitis riparia — Plant Cell Environ 2008;31(1):1-10 (PMID 17971068, 초록 확인)", "https://doi.org/10.1111/j.1365-3040.2007.01741.x", "PubMed", A),
 ("Root pressure and specific conductivity in temperate lianas: exotic Celastrus orbiculatus vs. native Vitis riparia — Am J Bot 2000;87(9):1272-8 (PMID 10991898, 초록 확인)", "https://pubmed.ncbi.nlm.nih.gov/10991898/", "PubMed", A),
 ("Development and survivorship of Lycorma delicatula on cultivated and native Vitis spp. of the Eastern United States — J Econ Entomol 2023 (PMID 37931223, 초록 확인)", "https://doi.org/10.1093/jee/toad198", "PubMed", A),
 ("Molecular linkage maps of Vitis vinifera L. and Vitis riparia Mchx. — Theor Appl Genet 2003;106(7):1213-24 (PMID 12748772, 초록 확인)", "https://doi.org/10.1007/s00122-002-1170-3", "PubMed", A),
 ("Grape ripening speed slowed down using natural variation — Theor Appl Genet 2025 (PMID 40445386, 초록 확인)", "https://doi.org/10.1007/s00122-025-04914-y", "PubMed", A),
 ("Underutilized Canadian wild berries as potential sources of lipophilic bioactive compounds with antihypertensive properties — Food Funct 2024 (PMID 38920290, 초록 확인; 초록 표기에서 야생포도의 학명이 빠져 종 확인 못함)", "https://doi.org/10.1039/d4fo00665h", "PubMed", A),
 ("Characterization of Agrobacterium vitis Strains Isolated from Feral Vitis riparia — Plant Dis 1999;83(2):102-107 (PMID 30849789, 초록 확인)", "https://doi.org/10.1094/PDIS.1999.83.2.102", "PubMed", A),
 ("Study of anthocyanic profiles of twenty-one hybrid grape varieties by liquid chromatography and precursor-ion mass spectrometry — Anal Chim Acta 2012;732:120-9 (PMID 22688043, 초록 확인)", "https://doi.org/10.1016/j.aca.2011.10.045", "PubMed", A),
 ("Flavor of cold-hardy grapes: impact of berry maturity and environmental conditions — J Agric Food Chem 2013 (PMID 24151907, 초록 확인)", "https://doi.org/10.1021/jf402473u", "PubMed", A),
]
sources = [{"n": i + 1, "title": t, "url": u, "publisher": p, "accessed": a} for i, (t, u, p, a) in enumerate(S)]

sections = [
 {"key": "overview", "title": "개요", "body":
  "사막포도(Vitis riparia Michx.)는 포도과(Vitaceae) 포도속의 덩굴성 목본으로, 북아메리카 원산의 야생 포도 가운데 자연 분포 범위가 가장 넓은 종이다[3]. "
  "식약처 「식품원료 목록」에는 원료명 '사막포도열매', 이명 '리파리아머루', 영어명 'Riverbank grape'(강가 포도라는 뜻), 학명 Vitis riparia Michx.로 한 행이 올라 있다[1]. "
  "이 행은 사용가능 원료이고 사용 조건은 '사용가능부위 : 열매'이므로, 잎·줄기·뿌리는 이 행으로 식품에 쓸 수 없다[1]. "
  "국문명 '사막포도'는 영어명(강가 포도)과 뜻이 맞지 않으며, 같은 목록에는 영어명 그대로 'Desert grape열매'로 오른 별개의 종 Vitis girdiana 행이 따로 있어 이름만 보고 두 종을 섞지 않도록 주의해야 한다[1]. "
  "'강변포도'라는 국문 이명은 식약처 원자료에서 확인하지 못함. "
  "이 종을 원재료로 하는 건강기능식품 고시형 원료는 확인하지 못함.\n\n"
  "열매는 작고 검은 장과로 산도가 높으며, 미국 야생 포도 열매는 원주민이 오래 먹어 왔고 지금도 지역에서 생으로나 말려서, 또는 잼 같은 저장식품으로 먹는다고 보고되었다[4, 8]. "
  "산업적으로는 열매보다 대목(접목할 때 뿌리 쪽 나무)과 내한성·내병성 육종 재료로 더 중요하며, 19세기 중반 유럽의 필록세라(포도뿌리혹벌레) 피해 이후 프랑스 포도 산업 회복에 쓰였다[2, 3]."},
 {"key": "history", "title": "역사와 이용", "body":
  "사막포도는 19세기 중반 유럽 포도밭을 휩쓴 필록세라 피해 때 대목으로 쓰이면서 프랑스 포도주 산업의 회복에 기여한 종으로 기록된다[3]. "
  "현재 시판되는 유일한 순수 V. riparia 대목인 'Riparia Gloire de Montpellier'는 1880년 북미에서 들여온 수집품에서 선발되었다[2]. "
  "이 종은 지금도 세계 여러 나라에서 대목과 접수(열매를 맺는 품종) 육종의 주요 재료로 쓰인다[2, 3]. "
  "독일의 대목 'Börner'는 V. riparia와 V. cinerea의 교잡종으로 필록세라 저항성이 높다[13].\n\n"
  "추운 지역 포도주 산업에서도 쓰임이 커서, 캐나다 퀘벡 등에서 재배하는 내한성 포도 품종은 주로 V. vinifera와 V. labrusca·V. riparia의 종간 교잡종이다[24]. "
  "이런 교잡 품종의 열매 성분은 사막포도 자체의 성분이 아니므로 이 문서에서는 따로 구분해 적었다[24]. "
  "식용 측면에서는 미국 야생 포도(V. riparia·V. californica 등) 열매를 원주민이 수백 년 동안 먹어 왔고, 지금도 생과·건과·가정용 저장식품으로 지역에서 소비한다고 보고되었다[8]. "
  "국내에서 사막포도 열매를 재배하거나 유통한 기록은 확인하지 못함."},
 {"key": "biology", "title": "식물학적 특징", "body":
  "사막포도는 북아메리카 자생 포도 가운데 가장 넓은 자연 분포를 가지며, 생물·비생물 스트레스에 강하다[3]. "
  "미국 미시간주에서는 외래 덩굴식물 Celastrus orbiculatus와 같은 서식지에 자라는 토종 덩굴식물로, 봄에 잎이 나기 전 뿌리압으로 물관의 공기 막힘을 되돌려 물 흐름을 회복하고 가을 첫 서리에 물관 전도도를 잃는다[17]. "
  "겨울눈은 휴면에 들어가며, 4 °C 저온 처리 실험에서 약 1,500시간이 지나야 저온 요구량이 채워지고 2,000시간에서 싹틈이 더 빨라졌다[15]. "
  "얼음에 강한 야생 포도로 알려져 있어 저온 반응 전사인자(CBF4) 연구의 재료가 되었다[16].\n\n"
  "꽃은 암꽃만 피는 개체(암그루형)와 양성화 개체가 있으며, 'Manitoba 37'은 암꽃형으로 검은 열매를 맺는다[4]. "
  "열매 껍질의 안토시아닌에는 V. vinifera에는 거의 없는 3,5-다이글루코사이드형이 흔한데, 이를 만드는 효소 유전자(5GT)가 V. vinifera에서는 일찍 끊겨 기능을 잃은 반면 V. riparia에는 51개 아미노산 구간이 온전히 남아 있다[4]. "
  "잎에는 수산칼슘 결정(침상 결정 raphide·집정 druse)이 생기고, 흙에 칼슘을 더하면 그 밀도가 늘었다[11]. "
  "뿌리에서는 혹을 만들지 않는 Agrobacterium vitis 균주가 흔히 분리되었다[22]."},
 {"key": "related_species", "title": "근연종과 혼동", "body":
  "식약처 목록에는 포도속 원료가 여럿 따로 올라 있어, 사막포도(V. riparia) 자료를 포도(V. vinifera)·머루(V. coignetiae)·왕머루(V. amurensis)·새머루(V. flexuosa)·로툰디폴리아머루(V. rotundifolia)·Red grape(V. palmata) 자료와 섞으면 안 된다[1]. "
  "특히 영어로 'Desert grape'인 V. girdiana, 'Frost grape'인 V. vulpina, 'California wild grape'인 V. californica가 각각 별개 행으로 올라 있어 국문명 '사막포도'와 영어명을 혼동하기 쉽다[1]. "
  "북미 종과 유라시아 종은 약 4,690만 년 전에 갈라졌다는 추정이 있으나 염색체 19쌍의 유전자 배열은 매우 잘 보존되어 있다[2].\n\n"
  "대목과 교잡종 자료도 주의해야 한다[2, 13, 14]. "
  "'Riparia Gloire de Montpellier'는 순수 V. riparia이지만, 'Börner'(V. riparia × V. cinerea)나 Ramsey(V. champinii)와의 교잡 집단은 다른 종의 유전자가 섞여 있다[13, 14]. "
  "Seyve Villard 등 V. vinifera·V. riparia·V. labrusca·V. lincecumii·V. rupestris를 섞어 만든 교잡 적포도 품종은 다이글루코사이드 안토시아닌 함량이 품종마다 크게 달랐다[23]. "
  "V. monticola × V. riparia 대목 품종에서 보고된 높은 레스베라트롤 값도 순수 사막포도의 값이 아니다[9]."},
 {"key": "cultivation", "title": "재배와 분포", "body":
  "사막포도는 국내 재배 통계가 없으며, 국내 생산 기록은 확인하지 못함. "
  "원산지 북미에서 자생하며, 겨울이 추운 미국 미시간주의 숲 서식지에서도 토종 덩굴로 자란다[17]. "
  "얼음 피해에 강한 야생 포도로 분류되어 내한성 연구와 내한성 품종 육종에 쓰인다[3, 16]. "
  "미국 동부에서 꽃매미(Lycorma delicatula) 약충을 V. riparia로 길렀을 때 생존율과 발육 속도가 대조 기주인 가죽나무와 통계적으로 같은 수준이어서 좋은 기주로 평가되었다[18]. "
  "꽃매미는 한국에서도 재배 포도의 해충으로 알려져 있다[18].\n\n"
  "노균병(Plasmopara viticola)에 강한 종으로 알려져 있는데, 저항성 품종 'Qingdahean'(V. riparia)은 병원균이 기공을 찾아 들어가는 단계부터 막는 여러 겹의 기공 면역과 과민반응을 보였다[12]. "
  "V. riparia에서 온 한 유전자형(haplotype)은 열매의 당 축적 속도를 절반으로 늦춰, 기후 변화 속에서 포도 성숙을 서늘한 가을로 미루는 육종 재료로 제안되었다[20]. "
  "대목으로서는 필록세라 저항성과 함께 석회·염분 내성, 접수의 생장 세력 같은 형질 연구에 쓰인다[13, 14]."},
 {"key": "processing", "title": "가공과 성분", "body":
  "식약처 목록상 사막포도는 열매만 식품원료로 쓸 수 있으며, 이 종을 원료로 한 국내 가공 제품이나 생산실적은 확인하지 못함. "
  "V. riparia로 빚은 포도주는 V. vinifera 포도주보다 유제놀·cis-3-헥센올·1,8-시네올과 메톡시피라진(IBMP·IPMP) 같은 풀·흙 냄새 성분이 많았다[6]. "
  "반면 미국 포도 V. labrusca의 '여우 냄새'를 내는 안트라닐산메틸과 2-아미노아세토페논은 V. riparia 포도주에서 검출되지 않았다(10 μg/L 미만)[6].\n\n"
  "야생 포도는 대체로 V. vinifera보다 적정산도와 말산이 높아 포도주가 지나치게 신맛을 내기 쉽고, 'Manitoba 37'은 교잡 집단에서 높은 말산 형질을 물려준 조부모였다[4]. "
  "열매 안토시아닌의 3,5-다이글루코사이드는 안정한 중합 색소를 덜 만들어 포도주 양조에 불리하게 여겨지며, 일부 와인 산지에서는 종간 교잡 품종을 가려내는 지표로 쓴다[4]. "
  "종자 추출물은 탄닌·카테킨·갈산이 많고 항산화 활성이 높아, 미국 야생종 종자가 기능성 식품 소재 후보로 제시되었다[7, 8]. "
  "캐나다 프레리 야생 베리 연구에서 '야생포도'는 총지방 7659 ± 312 μg/g 건조중량, 다가불포화지방산 74%로 조사 베리 중 가장 높았으나, 초록 표기에서 학명을 확인하지 못해 사막포도 값으로 단정하지 않는다[21]."},
 {"key": "genetics", "title": "유전체와 육종", "body":
  "사막포도는 야생 포도로는 처음으로 고품질 유전체가 공개된 종이다[2]. "
  "'Riparia Gloire de Montpellier' 클론 1030의 유전체는 PacBio 긴 읽기와 10x Genomics 연결 읽기로 조립되어 약 500 Mb, 스캐폴드 N50 약 1 Mb, 반복서열 33.94%, 단백질 암호 유전자 37,207개로 보고되었다[2]. "
  "k-mer 분석으로 추정한 유전체 크기는 494 Mb, 이형접합도는 0.46%였다[2]. "
  "내한성 개체 'Manitoba 37'의 초안 유전체는 약 495 Mb, 예측 암호서열 40,019개였다[3].\n\n"
  "V. vinifera 'Moscato bianco'와 V. riparia의 교배 집단으로 만든 연관지도는 병 저항성 형질을 옮기기 위한 초기 지도였다[19]. "
  "V. riparia 'Manitoba 37'과 'Seyval blanc'에서 나온 F2 집단(424개체)의 지도에서는 열매 색, 말산, 가용성 고형분, 효모 동화성 질소 관련 QTL이 확인되었다[5]. "
  "같은 집단의 후속 연구에서 다이글루코사이드 안토시아닌 QTL은 9번 염색체의 5GT 후보 유전자 근처에, 말산 QTL은 1·6·8번 염색체에 놓였다[4]. "
  "Ramsey × Riparia Gloire 집단의 SSR 지도는 선충 저항성·석회와 염분 내성 등 대목 형질 연구에 쓰였다[14]."},
 {"key": "safety", "title": "안전성", "body":
  "사막포도 열매에 대한 식약처·해외 공공기관의 알레르기·독성·잔류 관련 안전성 정보는 확인하지 못함. "
  "식약처 목록상 지위는 '사용가능'이지만 사용 부위가 열매로 한정되어 있으므로, 잎·줄기·뿌리를 원료로 쓰는 것은 이 행의 범위를 벗어난다[1]. "
  "잎에는 수산칼슘 결정이 생기며 흙의 칼슘이 많을수록 늘어나지만, 이 결정이 모충의 생장에는 영향을 주지 않았다[11]. "
  "다만 잎은 식용 허용 부위가 아니며, 열매의 수산 함량은 확인하지 못함.\n\n"
  "포도주 실험에서 V. riparia 일부 계통의 메톡시피라진 농도(IBMP 350 pg/g 초과, IPMP 30 pg/g 초과)는 감각 역치를 크게 넘었는데, 이는 풍미 문제이지 독성 문제로 보고된 것은 아니다[6]. "
  "종자 추출물의 항산화·항균 결과는 시험관 실험이므로 사람에게서의 효과로 해석해서는 안 된다[7, 8]. "
  "사람을 대상으로 한 사막포도 열매 섭취 연구와 의약품 상호작용 정보는 확인하지 못함."},
]

compounds = [
 {"name": "Malvidin 3,5-diglucoside", "name_ko": "말비딘-3,5-다이글루코사이드", "class": "안토시아닌(다이글루코사이드)", "role": "marker", "part": "열매(껍질)",
  "content_text": "V. riparia 단독 함량은 본문에서 확인하지 못함; V. riparia 'Manitoba 37' × 'Seyval blanc' F2 집단 열매에서 표준품으로 정량(HPLC 520 nm)[4]",
  "activity_ko": "V. vinifera에는 거의 없고 V. riparia 등 야생종·교잡종에 흔해 종간 교잡 판별 지표로 쓰임[4]", "source": [4]},
 {"name": "Malvidin 3-glucoside", "name_ko": "말비딘-3-글루코사이드", "class": "안토시아닌(모노글루코사이드)", "role": "bioactive", "part": "열매(껍질)",
  "content_text": "F2 집단 열매에서 표준품으로 정량, V. riparia 단독 값은 확인하지 못함[4]", "activity_ko": "열매 색을 내는 주요 안토시아닌[4]", "source": [4]},
 {"name": "Cyanidin 3,5-diglucoside", "name_ko": "시아니딘-3,5-다이글루코사이드", "class": "안토시아닌(다이글루코사이드)", "role": "bioactive", "part": "열매(껍질)",
  "content_text": "F2 집단에서 시아니딘·말비딘·페오니딘·페투니딘 3,5-다이글루코사이드 QTL이 9번 염색체에 함께 위치(함량 미기재)[4]", "activity_ko": "다이글루코사이드 안토시아닌 형질[4]", "source": [4]},
 {"name": "Malic acid", "name_ko": "말산(사과산)", "class": "유기산", "role": "nutrient", "part": "열매(베레종 후 30일)",
  "content_text": "조부모·부모·F2 집단 전체 1.5–29.0 g/L, F2 평균 10.6–12.0 g/L; 높은 말산 형질은 V. riparia 'Manitoba 37'에서 유래[4]",
  "activity_ko": "야생종 열매의 높은 신맛(적정산도 12.88–28.28 g/L 범위)과 강하게 상관[4]", "source": [4]},
 {"name": "3-Isobutyl-2-methoxypyrazine", "name_ko": "3-아이소뷰틸-2-메톡시피라진(IBMP)", "class": "메톡시피라진(향기 성분)", "role": "bioactive", "part": "열매·포도주",
  "content_text": "V. riparia·V. rupestris·V. cinerea 31개 계통 조사에서 일부 계통 350 pg/g 초과(종별 값은 초록에서 확인 못함)[6]",
  "activity_ko": "피망·풀 냄새를 내는 향기 성분, 감각 역치를 크게 넘음[6]", "source": [6]},
 {"name": "3-Isopropyl-2-methoxypyrazine", "name_ko": "3-아이소프로필-2-메톡시피라진(IPMP)", "class": "메톡시피라진(향기 성분)", "role": "bioactive", "part": "열매·포도주",
  "content_text": "같은 31개 계통 조사에서 일부 계통 30 pg/g 초과[6]", "activity_ko": "흙·풀 냄새 성분[6]", "source": [6]},
 {"name": "Eugenol", "name_ko": "유제놀", "class": "페닐프로파노이드(향기 성분)", "role": "bioactive", "part": "포도주(열매 발효)",
  "content_text": "V. riparia·V. cinerea 포도주에서 V. vinifera 포도주보다 높음(정량 GC-MS로 확인, 수치는 초록에 없음)[6]", "activity_ko": "정향 같은 향[6]", "source": [6]},
 {"name": "Methyl anthranilate", "name_ko": "안트라닐산메틸", "class": "향기 성분", "role": "marker", "part": "포도주(열매 발효)",
  "content_text": "V. riparia 포도주에서 검출되지 않음(<10 μg/L)[6]", "activity_ko": "V. labrusca의 '여우 냄새' 성분으로, 없음이 V. riparia를 V. labrusca와 구별하는 특징[6]", "source": [6]},
 {"name": "(+)-Catechin", "name_ko": "(+)-카테킨", "class": "플라반-3-올", "role": "bioactive", "part": "종자(열매 안의 씨)",
  "content_text": "V. californica·V. riparia·V. amurensis 종자 메탄올 추출물에서 카테킨·에피카테킨 각각 33–38 mg/g 추출물, 합계 66–71 mg/g 추출물(세 종 범위)[7]",
  "activity_ko": "종자 항산화 활성의 주된 기여 성분으로 추정[7, 8]", "source": [7, 8]},
 {"name": "(-)-Epicatechin", "name_ko": "(-)-에피카테킨", "class": "플라반-3-올", "role": "bioactive", "part": "종자",
  "content_text": "세 야생종 종자 추출물에서 카테킨과 비슷한 수준(33–38 mg/g 추출물 범위)[7]", "activity_ko": "라디칼 소거[7]", "source": [7]},
 {"name": "Gallic acid", "name_ko": "갈산", "class": "페놀산", "role": "bioactive", "part": "종자",
  "content_text": "미국 두 종(V. californica·V. riparia) 종자 추출물 10.2·8.6 mg/g 추출물, V. amurensis 1.6 mg/g; 두 미국 종 가운데 어느 값이 V. riparia인지는 전문 표기에서 확인하지 못함[7]",
  "activity_ko": "대부분 에스터·배당체 결합형으로 존재, 항산화[7]", "source": [7]},
 {"name": "Condensed tannins", "name_ko": "축합형 탄닌(프로안토시아니딘)", "class": "폴리페놀", "role": "bioactive", "part": "종자",
  "content_text": "미국 두 종 종자 아세톤 추출물 총페놀 396·377 mg/g 추출물(카테킨 당량), V. amurensis의 약 2배; 탄닌도 미국 종이 약 2배[7]",
  "activity_ko": "DPPH 라디칼 소거·환원력과 밀접히 상관(시험관)[7]", "source": [7]},
 {"name": "Resveratrol", "name_ko": "트랜스-레스베라트롤", "class": "스틸벤", "role": "bioactive", "part": "열매 껍질·종자(교잡 대목 품종), 덩굴(가지)",
  "content_text": "V. monticola × V. riparia 대목 품종 껍질 >100 μg/g 생중량, 종자 >20 μg/g 생중량(순수 V. riparia 값 아님)[9]; V. riparia 등 14종 덩굴에서 9종 스틸벤 합계 약 2.2–19.5 g/kg 건조중량(종 범위)[10]",
  "activity_ko": "병 저항성 관련 피토알렉신; 덩굴은 식용 허용 부위가 아님[9, 10]", "source": [9, 10]},
 {"name": "Calcium oxalate", "name_ko": "수산칼슘", "class": "무기 결정(생물광물)", "role": "bioactive", "part": "잎(식용 허용 부위 아님)",
  "content_text": "잎의 raphide·druse 결정 밀도가 흙 칼슘 첨가로 증가(수치는 초록에 없음)[11]", "activity_ko": "모충 생장·생존에 영향 없음, 칼슘 조절 기능 가설 지지[11]", "source": [11]},
]

assays = [
 {"role": "literature", "compound": "Malvidin 3,5-diglucoside", "compound_ko": "말비딘-3,5-다이글루코사이드(안토시아닌 10종 동시 분석)", "part": "열매(베레종 후 30일, 냉동 전과 마쇄물)",
  "content": "V. riparia 'Manitoba 37' × 'Seyval blanc' F2 집단·조부모 열매 정량, V. riparia 단독 수치는 본문에서 확인하지 못함(표 미확인)[4]",
  "method": "HPLC-DAD",
  "conditions": {"instrument": "Agilent 1260 Infinity", "column": "Kinetex C18, 100 × 4.6 mm, 2.6 μm (KrudKatcher 가드 필터)", "mobile_phase": "A: 0.5% 인산 수용액, B: 0.5% 인산 메탄올",
   "gradient": "15% B 시작 → 15분 30% B → 25분 60% B → 27분까지 60% B 유지 → 30분 15% B, 이후 10분 평형", "flow": "0.2 mL/min", "temp": "45 °C", "detection": "UV/VIS 190–640 nm 중 520 nm로 정량",
   "injection": "", "sample_prep": "냉동 열매 25 g 꼭지 제거·1분 마쇄 → 10 g 해동·원심분리(5분, 10,000×g) → 고상추출(SPE)로 안토시아닌 분획 분리",
   "standard": "말비딘-3,5-다이글루코사이드·말비딘-3-글루코사이드 표준품; 나머지 8종은 머무름 시간 비교로 잠정 동정", "linearity": "", "lod": "", "loq": "",
   "recovery": "회수율 기재 없음; 표준품 반복 정밀도 <1% RSD, 델피니딘-3-글루코사이드와 페투니딘-3,5-다이글루코사이드 외 분리도 Rs > 1.5"},
  "rationale": "V. riparia는 기능하는 5GT 유전자를 가져 3,5-다이글루코사이드를 만들고 V. vinifera는 거의 만들지 못하므로, 이 성분이 종 특성과 교잡 판별의 지표가 됨; 전문 확인[4].",
  "source": [4], "url": "https://doi.org/10.3390/plants11050696", "source_kind": "paper"},
 {"role": "literature", "compound": "Malic acid", "compound_ko": "말산", "part": "열매(베레종 후 30일, 즙)",
  "content": "세대·연도 전체 1.5–29.0 g/L, F2 평균 10.6–12.0 g/L[4]", "method": "HPLC-UV(이온배제)",
  "conditions": {"instrument": "Agilent 1260", "column": "Bio-Rad Aminex HPX-87H 이온배제 칼럼(Bio-Rad micro-guard cation-H 카트리지 앞)", "mobile_phase": "", "gradient": "", "flow": "", "temp": "",
   "detection": "DAD 210 nm", "injection": "", "sample_prep": "냉동 열매 마쇄물 10 g 해동 → 원심분리(5분, 10,000×g) → 즙 주입", "standard": "말산 표준품 검량", "linearity": "", "lod": "", "loq": "", "recovery": "반복성 %RSD <3%"},
  "rationale": "야생 포도 열매의 높은 신맛을 결정하는 주 유기산이며 'Manitoba 37'이 높은 말산 형질의 공여 조부모로 확인됨; 전문 확인, 이동상·유속은 원문에 없음[4].",
  "source": [4], "url": "https://doi.org/10.3390/plants11050696", "source_kind": "paper"},
 {"role": "literature", "compound": "(+)-Catechin", "compound_ko": "(+)-카테킨·(-)-에피카테킨", "part": "종자(헥산 탈지 후 80% 메탄올 추출물)",
  "content": "세 야생종(V. californica·V. riparia·V. amurensis) 종자 추출물 카테킨·에피카테킨 각 33–38 mg/g 추출물, 합계 66–71 mg/g 추출물[7]", "method": "HPLC-PAD",
  "conditions": {"instrument": "Shimadzu(LC-10AD 펌프 2대, SCTL 10A 제어기, SPD-M 10A 다이오드 배열 검출기)", "column": "LiChrospher 100 RP-18, 4 × 250 mm, 5 μm (Merck)", "mobile_phase": "물(TFA로 pH 2.5)–아세토니트릴",
   "gradient": "아세토니트릴 5→40%, 50분", "flow": "1 mL/min", "temp": "", "detection": "280 nm", "injection": "20 μL",
   "sample_prep": "종자 분쇄 → 헥산 속실렛 탈지 6–8시간 → 80% 메탄올(1:10 w/v) 50 °C 30분 3회 추출 → 감압농축·동결건조 → 추출물 10 mg을 80% 메탄올 1 mL에 녹여 0.45 μm 셀룰로스아세테이트 여과",
   "standard": "(+)-카테킨·(-)-에피카테킨(Sigma-Aldrich)", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "종자 폴리페놀의 주성분이자 항산화 활성의 주된 기여 성분으로 정량됨; 전문 확인, 종별 개별 값의 대응은 확인하지 못함[7].",
  "source": [7], "url": "https://doi.org/10.3390/ijms13033444", "source_kind": "paper"},
 {"role": "literature", "compound": "Procyanidin B2", "compound_ko": "프로시아니딘 B2 등 페놀 39종(카테킨·에피카테킨·갈산·안토시아닌·레스베라트롤 포함)", "part": "종자(헥산 탈지 후 80% 메탄올 추출물)",
  "content": "V. riparia 포함 네 종 종자 추출물: 주요 성분 범위 카테킨 168–246, 에피카테킨 90.7–117, 프로시아니딘 B2 35.8–124, 갈산 44.6–166 mg/100 g(세 종 범위, 종별 대응은 전문 표기에서 확인하지 못함)[8]",
  "method": "LC-MS/MS(SRM)",
  "conditions": {"instrument": "Exion LC AC(Shimadzu) + 5500+ QTrap, Turbo V 이온 스프레이(AB Sciex)", "column": "Kinetex Biphenyl, 2.1 × 100 mm, 2.6 μm (Phenomenex)",
   "mobile_phase": "A: 0.1% 포름산 물, B: 0.1% 포름산 아세토니트릴", "gradient": "0–10.0분 5→95% B, 10.0–12.0분 95% B, 12.0–12.1분 95→5% B, 12.1–16.0분 5% B", "flow": "0.4 mL/min", "temp": "이온원 500 °C",
   "detection": "SRM; 음이온 −4500 V(안토시아닌 제외 페놀), 양이온 +5500 V(안토시아닌); GS1 70, GS2 50, CUR 10, EP 10 V, dwell 20 ms", "injection": "",
   "sample_prep": "종자 분쇄(<0.8 mm) → 헥산 속실렛 탈지 6–8시간 → 80% 메탄올(1:10 w/v) 65 °C 15분 3회 → 감압농축·동결건조", "standard": "표준품 39종 혼합(Sigma-Aldrich·Extrasynthese)",
   "linearity": "0.5–256 ng/mL 10점 검량", "lod": "", "loq": "", "recovery": "매트릭스 효과·회수율로 보정(수치 미기재)"},
  "rationale": "종자 페놀 조성(플라반-3-올·프로시아니딘·페놀산)이 종을 구분하는 주요 요인으로 제시됨; 전문 확인, 표가 본문에 없어 V. riparia 개별 값은 확인하지 못함[8].",
  "source": [8], "url": "https://doi.org/10.3390/molecules28134924", "source_kind": "paper"},
]

d = {
 "slug": "vitis-riparia", "name_ko": "사막포도", "name_en": "Riverbank grape", "scientific_name": "Vitis riparia Michx.",
 "aliases": ["사막포도열매", "리파리아머루", "Riverbank grape", "River grape"],
 "sections": sections, "compounds": compounds, "markers": [], "nutrients": [], "assays": assays,
 "production": [], "world": [], "gi": [], "orgs": [], "sources": sources,
}
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
print("ok", len(sources))
