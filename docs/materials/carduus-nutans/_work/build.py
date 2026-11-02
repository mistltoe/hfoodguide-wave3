import json
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
A = "2026-11-02"
PM = "https://pubmed.ncbi.nlm.nih.gov/"
PMC = "https://pmc.ncbi.nlm.nih.gov/articles/"

sources = [
    (1, "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 사향엉겅퀴줄기 행(학명 Carduus nutans L., 영문명 Musk thistle, Nodding plumeless thistle, 식물, 부위 줄기, '사용가능', 사용 조건 '사용가능부위 : 줄기'). 로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json", "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "식품의약품안전처", "2026-10-13"),
    (2, "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 혼동될 수 있는 엉겅퀴류 원료 행: 지느러미엉겅퀴잎·지느러미엉겅퀴줄기(Carduus crispus L., '사용가능부위 : 줄기, 잎'), Carduus cernuus줄기(Carduus cernuus, '사용가능부위 : 줄기'), 밀크씨슬(Silybum marianum L., '사용가능부위 : 잎, 씨앗'), 엉겅퀴(Cirsium japonicum DC. var. ussuriense Kitamura 등, '사용가능부위 : 순, 잎, 전초※(대계)'), 건강기능식품 '밀크씨슬(고시형)'. 로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json", "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "식품의약품안전처", "2026-10-13"),
    (3, "Two naturalized species, Carduus natans L. and Lepidium latifolium L. newly reported from Korea(우리나라 미기록 귀화식물 2종 보고, 2008; 원문 페이지는 이 환경에서 열 수 없어 WebSearch 결과 요약으로만 확인 — 학명은 원문에 'natans'로 적힘, 권호·쪽수 확인 못함)", "https://koreascience.kr/article/JAKO200810103421728.page", "KoreaScience(한국과학기술정보연구원)", A),
    (4, "Medical ethnobotany of the Albanian Alps in Kosovo. J Ethnobiol Ethnomed 2012;8:6 (PMID 22284581, PMC3285519, doi:10.1186/1746-4269-8-6; 전문 확인)", PMC + "PMC3285519/", "BioMed Central / PubMed Central", A),
    (5, "Turning Meadow Weeds Into Valuable Species for the Romanian Ethnomedicine While Complying With the Environmentally Friendly Farming Requirements of the European Union's Common Agricultural Policy. Front Pharmacol 2020;11:529 (PMID 32390852, PMC7191034, doi:10.3389/fphar.2020.00529; 전문 확인, 문헌 고찰)", PMC + "PMC7191034/", "Frontiers / PubMed Central", A),
    (6, "Hepatoprotective effects of Turkish folk remedies on experimental liver injury. J Ethnopharmacol 2000;73(1-2):121-9 (PMID 11025147, doi:10.1016/s0378-8741(00)00286-5; 초록만 확인)", PM + "11025147/", "Elsevier / PubMed", A),
    (7, "Phenolic Composition of Inflorescences of Carduus nutans L. Chem Biodivers 2022;19(3):e202100827 (PMID 34964548, doi:10.1002/cbdv.202100827; 초록만 확인)", PM + "34964548/", "Wiley / PubMed", A),
    (8, "Optimized conversion of antiproliferative lignans pinoresinol and epipinoresinol: Their simultaneous isolation and identification by centrifugal partition chromatography and high performance liquid chromatography. J Chromatogr B 2017;1052:142-149 (PMID 28384606, doi:10.1016/j.jchromb.2017.03.036; 초록만 확인)", PM + "28384606/", "Elsevier / PubMed", A),
    (9, "Roots of the invasive species Carduus nutans L. and C. acanthoides L. produce large amounts of aplotaxene, a possible allelochemical. J Chem Ecol 2014;40(3):276-84 (PMID 24557607, doi:10.1007/s10886-014-0390-8; 초록만 확인)", PM + "24557607/", "Springer / PubMed", A),
    (10, "Characterization of four wild edible Carduus species from the Mediterranean region via phytochemical and biomolecular analyses. Food Res Int 2017;100(Pt 1):822-831 (PMID 28873755, doi:10.1016/j.foodres.2017.07.071; 초록만 확인)", PM + "28873755/", "Elsevier / PubMed", A),
    (11, "Xanthatin and xanthinosin from the burs of Xanthium strumarium L. as potential anticancer agents. Can J Physiol Pharmacol 2007;85(11):1160-72 (PMID 18066118, doi:10.1139/Y07-104; 초록만 확인)", PM + "18066118/", "Canadian Science Publishing / PubMed", A),
    (12, "Bioactive potential of Indian stinging plants leaf extract against pathogenic fungi. J Complement Integr Med 2018;16(1) (PMID 29933244, doi:10.1515/jcim-2017-0125; 초록만 확인)", PM + "29933244/", "De Gruyter / PubMed", A),
    (13, "Phytoremediation of Cadmium by Native Plants Grown on Mining Soil. Bull Environ Contam Toxicol 2017;100(2):293-297 (PMID 29177694, doi:10.1007/s00128-017-2220-5; 초록만 확인)", PM + "29177694/", "Springer / PubMed", A),
    (14, "Warming and shifting phenology accelerate an invasive plant life cycle. Ecology 2020 (PMID 33048356, PMC7816242, doi:10.1002/ecy.3219; 전문 확인)", PMC + "PMC7816242/", "Ecological Society of America / PubMed Central", A),
    (15, "Dispersal patterns, dispersal mechanisms, and invasion wave speeds for invasive thistles. Am Nat 2007;170(3):421-30 (PMID 17879192, doi:10.1086/519854; 초록만 확인)", PM + "17879192/", "University of Chicago Press / PubMed", A),
    (16, "Integrating multiple disturbance aspects: management of an invasive thistle, Carduus nutans. Ann Bot 2012;110(7):1395-401 (PMID 22199031, PMC3489138, doi:10.1093/aob/mcr312; 초록 확인)", PM + "22199031/", "Oxford University Press / PubMed", A),
    (17, "Unrecognized impact of a biocontrol agent on the spread rate of an invasive thistle. Ecol Appl 2014;24(5):1178-87 (PMID 25154105, doi:10.1890/13-1309.1; 초록만 확인)", PM + "25154105/", "Ecological Society of America / PubMed", A),
    (18, "First Report of Musk Thistle Rust (Puccinia carduorum) in Oklahoma. Plant Dis 1998;82(7):832 (PMID 30856969, doi:10.1094/PDIS.1998.82.7.832D; 초록 확인)", PM + "30856969/", "American Phytopathological Society / PubMed", A),
    (19, "Realized gene flow via pollen in artificial populations of musk thistle, Carduus nutans L. Evolution 1987;41(3):613-619 (PMID 28563801, doi:10.1111/j.1558-5646.1987.tb05832.x; 초록만 확인)", PM + "28563801/", "Wiley / PubMed", A),
    (20, "Plant community associations of two invasive thistles. AoB Plants 2015;7:plv065 (PMID 26038126, PMC4571105, doi:10.1093/aobpla/plv065; 초록 확인)", PM + "26038126/", "Oxford University Press / PubMed", A),
    (21, "Warming Increases Pollen Lipid Concentration in an Invasive Thistle, with Minor Effects on the Associated Floral-Visitor Community. Insects 2019;11(1):20 (PMID 31881659, PMC7022432, doi:10.3390/insects11010020; 초록 확인)", PM + "31881659/", "MDPI / PubMed", A),
    (22, "Host utilization of field-caged native and introduced thistle species by Rhinocyllus conicus. Environ Entomol 2010;39(6):1858-65 (PMID 22182551, doi:10.1603/EN10053; 초록만 확인)", PM + "22182551/", "Entomological Society of America / PubMed", A),
    (23, "Leaf-cutting ant nests near roads increase fitness of exotic plant species in natural protected areas. Proc Biol Sci 2008;275(1641):1431-40 (PMID 18364316, PMC2602710, doi:10.1098/rspb.2008.0154; 초록 확인)", PM + "18364316/", "Royal Society / PubMed", A),
    (24, "Warming increases the spread of an invasive thistle. PLoS One 2011;6(6):e21725 (PMID 21738779, PMC3126854, doi:10.1371/journal.pone.0021725; 초록 확인)", PM + "21738779/", "PLOS / PubMed", A),
    (25, "LOTUS 천연물 발생 데이터베이스 — card.json 의 지표성분 후보(Luteolin 7-galactoside, Tilianin; 이 종에서 각 1건 보고)를 고른 근거 DB. 개별 레코드와 원 문헌은 직접 확인하지 못함", "https://lotus.naturalproducts.net/", "LOTUS (Natural Products Online)", A),
    (26, "Simultaneous determination of bioactive flavonoids in some selected Korean thistles by high-performance liquid chromatography. Arch Pharm Res 2011;34(3):455-61 (PMID 21547678, doi:10.1007/s12272-011-0314-x; 초록만 확인 — 지느러미엉겅퀴(Carduus crispus)를 다룬 연구로, 사향엉겅퀴 자료가 아님을 밝히는 데만 씀)", PM + "21547678/", "Springer / PubMed", A),
    (27, "First Report of Musk Thistle Rust (Puccinia carduorum) in California and Nevada. Plant Dis 2002;86(7):814 (PMID 30818587, doi:10.1094/PDIS.2002.86.7.814B; 초록 확인)", PM + "30818587/", "American Phytopathological Society / PubMed", A),
]

S = {}
S["overview"] = ("한눈에 보기",
"사향엉겅퀴(Carduus nutans L.)는 국화과(Asteraceae) 지느러미엉겅퀴속(Carduus)에 속하는 풀로, 영문으로는 Musk thistle 또는 Nodding plumeless thistle이라 부른다[1]. 유라시아가 원산인 잡초로, 북아메리카·남아프리카·오스트레일리아·뉴질랜드에 침입해 잎의 가시 때문에 목초지의 골칫거리가 되었다[14].\n\n"
"식품원료로서의 지위는 식약처 「식품원료 목록」에 '사향엉겅퀴줄기' 한 원료명으로 올라 있고, 상태는 '사용가능'이다[1]. 사용 조건은 원문 그대로 '사용가능부위 : 줄기'로, 줄기만 식품원료로 쓸 수 있고 잎·꽃·씨앗·뿌리는 이 목록에 사용 부위로 올라 있지 않다[1]. 이 목록 행에는 사용량 한도나 식품 유형 제한 같은 세부 조건이 더 적혀 있지 않다[1].\n\n"
"성분 연구는 대부분 꽃차례·열매·뿌리를 다루었고, 식품원료 부위인 줄기만을 분석한 논문은 확인하지 못함. 꽃차례에서는 페놀산과 플라보노이드 20여 종이 확인되었고[7], 열매에서는 리그난인 피노레시놀이 7.8 mg/g 보고되었다[8]. 이름이 비슷한 엉겅퀴(Cirsium)나 밀크씨슬(Silybum marianum)과는 속이 다른 별개의 원료다[2].")

S["history"] = ("이용의 역사",
"사향엉겅퀴는 주로 유럽 동남부와 튀르키예의 민간요법에서 쓰인 기록이 있다[4, 5]. 코소보 알바니아 알프스 지역 조사에서는 야생 사향엉겅퀴의 꽃차례를 찬물에 열흘 동안 우려 차처럼 마시며 습진에 썼다고 기록되었다[4]. 같은 조사는 이 종을 약리 연구가 드문 '눈여겨볼 약용식물'로 꼽았다[4].\n\n"
"루마니아 민간요법을 정리한 문헌 고찰에 따르면 씨앗은 동맥경화 예방, 꽃은 해열과 '피를 맑게 하는' 용도, 잎은 고혈압과 간 질환에 권해졌다[5]. 같은 고찰은 튀르키예에서 간 기능을 돕는 강장·해독용으로, 불가리아에서 치질·강심·이뇨용으로 쓰였다고 정리했다[5]. 튀르키예에서는 빻은 씨앗을 우려 간 질환에 마셨다는 기록도 있다[5].\n\n"
"이런 전통 용도는 대부분 꽃·씨앗·잎에 관한 것으로, 국내 식품원료 사용 부위인 줄기를 먹은 전통 기록은 확인하지 못함. 우리나라에서는 2008년에 미기록 귀화식물로 처음 보고되어 이용 역사가 짧다[3].")

S["biology"] = ("식물학적 특징",
"사향엉겅퀴는 한 번 꽃 피우고 죽는 수명이 짧은 일회결실성(monocarpic) 다년초로, 가을이나 봄에 싹튼 뒤 한 해에서 여러 해 동안 로제트로 지내다가 줄기를 세워 꽃 피우고 씨를 퍼뜨린 뒤 죽는다[14]. 미국 펜실베이니아의 야외 실험 모형에서는 현재 기온 조건에서 개체의 60.8%가 첫해에 꽃 피우는 한해살이처럼 자랐다[14]. 한 포기가 수천 개의 갓털 달린 씨앗을 맺으며, 씨앗은 떨어진 직후에도 잘 싹튼다[14].\n\n"
"꽃머리(두화)는 지름 30–60 mm로 크고 아래로 고개 숙이며, 총포 조각이 창끝 모양이어서 같은 속 지느러미엉겅퀴와 구별된다[3]. 바람에 날린 씨앗은 대부분 2 m 안팎에 떨어지지만 96 m 떨어진 곳에서 잡힌 씨앗도 있었다[15]. 꽃은 벌 등 여러 곤충이 찾아오며, 꽃가루의 지질 함량은 기온이 오르면 높아졌다[21]. 잎의 가시는 가축의 풀 뜯기를 막아 목초지 생산성을 떨어뜨린다[14].")

S["related_species"] = ("가까운 종과 구별",
"우리 식품원료 목록에는 같은 속(Carduus)의 지느러미엉겅퀴(Carduus crispus L., 줄기·잎)와 Carduus cernuus(줄기)가 따로 올라 있다[2]. Carduus cernuus가 사향엉겅퀴의 이명이나 아종인지는 이 조사에서 확인하지 못함. 국내 엉겅퀴류 HPLC 연구에 나오는 Carduus 자료는 지느러미엉겅퀴를 분석한 것이어서 사향엉겅퀴 성분으로 옮겨 쓰면 안 된다[26].\n\n"
"'엉겅퀴'라는 이름이 붙은 원료 가운데 엉겅퀴(Cirsium japonicum var. ussuriense 등)·고려엉겅퀴 등은 Cirsium 속이고, 밀크씨슬은 Silybum marianum으로 사향엉겅퀴와 속이 다르다[2]. 밀크씨슬은 건강기능식품 고시형 원료이지만 사향엉겅퀴에는 그런 지위가 없다[1, 2].\n\n"
"북미에서는 같은 속의 Carduus acanthoides와 함께 침입종으로 연구되며, 두 종은 침입한 식생 안에서 비슷한 식물 군집과 어울린다[20]. 사향엉겅퀴는 아종 구분이 있어, 지중해 연구는 subsp. macrocephalus를[10], 미국의 녹병 보고는 subsp. leiophyllus(Carduus thoermeri)를 다루었다[18]. 아종에 따라 성분이 다를 수 있어 문헌의 분류군을 확인해야 한다[10].")

S["cultivation"] = ("자생·재배와 원료 수급",
"사향엉겅퀴를 작물로 재배한 국내 통계나 생산 실적은 확인하지 못함. 국내에서는 2008년 서울 난지도와 경기 지역(양수리 등)에서 귀화식물로 처음 보고되었다[3]. 이 보고는 웹 검색 요약으로만 확인했으며, 이후 분포 변화는 확인하지 못함.\n\n"
"해외에서는 재배보다 방제 대상으로 다뤄진다[16, 17]. 줄기가 자라는 시기에 맞춘 풀베기는 강도가 높고 시기가 늦을수록 개화를 늦추고 생존과 꽃머리 수를 줄였다[16]. 미국에서는 꽃턱을 먹는 바구미(Rhinocyllus conicus)를 생물적 방제에 썼는데, 씨앗 생산뿐 아니라 씨앗의 바람 퍼짐도 줄였다[17]. 이 바구미는 실험 조건에서 토착 엉겅퀴(Cirsium)에서도 번식해 비표적 피해 우려가 제기되었다[22]. 녹병균(Puccinia carduorum)도 방제용으로 도입된 뒤 여러 주로 퍼졌다[18, 27].\n\n"
"아르헨티나 파타고니아에서는 잎꾼개미 둥지의 쓰레기 더미에서 자란 사향엉겅퀴가 50–600% 더 많고 씨앗을 100–300% 더 맺었다[23]. 기온이 오르면 키가 커지고 씨앗이 더 멀리 퍼지는 것으로 예측되었다[24].")

S["processing"] = ("가공과 제품",
"식약처 목록에서 사향엉겅퀴는 '사향엉겅퀴줄기' 한 원료명만 있고, 분말·추출물 같은 가공 원료명은 따로 올라 있지 않다[1]. 줄기를 가공한 제품이나 표준 가공법을 다룬 공공 자료는 확인하지 못함.\n\n"
"연구에서 쓰인 추출 방식은 부위마다 다르다[4, 7, 8]. 꽃차례는 메탄올 추출물이 DPPH 라디칼 소거에서 가장 강했고(EC50 618 ± 10.03 μg/mL), 총페놀 함량은 61.49 mg/g이었다[7]. 이 추출물은 원심분배 크로마토그래피(헥세인/에틸아세테이트/메탄올/물 0.7 : 4 : 0.8 : 4)로 플라보노이드가 풍부한 분획으로 나뉘었다[7]. 열매에서는 원심분배 크로마토그래피 두 단계로 피노레시놀을 분리했고, 50 °C에서 30분 산 처리하면 피노레시놀이 에피피노레시놀로 바뀌어 두 물질이 같은 양으로 생겼다[8].\n\n"
"민간에서는 꽃차례를 찬물에 열흘 우리는 방식이 기록되었다[4]. 루마니아 문헌 고찰은 이 종이 식이보충제로 쓰인다고 적었으나 제품 형태나 부위는 밝히지 않았다[5].")

S["genetics"] = ("유전과 분류",
"사향엉겅퀴는 국화과(Asteraceae) Carduus 속에 속한다[1, 10]. 지중해 지역의 식용 Carduus 네 종(사향엉겅퀴 subsp. macrocephalus 포함)을 비교한 연구에서는 핵 리보솜 DNA ITS 구간의 PCR-RFLP 분석으로 종을 구별할 수 있었다[10]. 같은 연구에서 성분 프로필과 유전자 결과 모두 개체들이 분류군별로 묶였다[10].\n\n"
"미국 캔자스의 인공 집단에서 동위효소(allozyme) 표지 두 좌위로 꽃가루를 통한 유전자 흐름을 잰 결과, 표지 대립유전자의 평균 이동 거리는 5.0 m였다[19]. 씨앗 이동까지 포함한 유효 집단 크기는 1,281–3,844개체로 추정되었다[19]. 염색체 수와 유전체 해독 여부는 이 조사에서 확인하지 못함.")

S["safety"] = ("안전성과 사용 조건",
"식약처 「식품원료 목록」에서 사향엉겅퀴는 '사용가능' 원료이지만, 쓸 수 있는 부위는 줄기 하나다[1]. 잎·꽃·씨앗·뿌리는 사용 부위로 올라 있지 않으므로 식품에 쓰지 않는다[1]. 이 종에 대한 식약처·국제기구의 알레르기·독성 평가나 섭취 시 주의사항은 확인하지 못함.\n\n"
"효능 근거는 매우 약하다[6, 11, 12]. 흰쥐 사염화탄소 간손상 모형에서 튀르키예 민간약 일곱 가지를 시험했을 때 유의한 간 보호 효과를 보인 것은 다른 두 식물(Fumaria vailantii, Gentiana olivieri)이었다[6]. 그런데 코소보 조사 논문은 2000년 튀르키예 연구진이 이 식물 추출물의 간 보호 효과를 밝혔다고 적어, 출처 사이에 해석이 엇갈린다[4, 6]. 지상부 클로로폼 추출물은 사람 폐암세포에 IC50 9.3 μg/mL의 세포독성을 보였고[11], 잎 추출물은 시험관에서 곰팡이 한 종에만 중간 정도 억제를 보였다[12]. 이런 세포·시험관 결과를 사람의 효능으로 볼 수는 없다[11, 12].\n\n"
"튀르키예 광산 지역 조사에서 사향엉겅퀴는 카드뮴을 많이 쌓는 식물 무리로 분류되었다[13]. 오염 지역이나 길가에서 채취한 줄기는 중금속 잔류에 주의해야 한다[13]. 뿌리에는 다른 식물의 생장을 억제하는 아플로탁센이 들어 있으나 잎에서는 검출되지 않았다[9].")

compounds = [
    dict(name="Pinoresinol", name_ko="피노레시놀", **{"class": "리그난(퓨로퓨란형)"}, role="marker", part="열매",
         content_text="열매 7.8 mg/g(HPLC; 이 종에서 처음 보고)[8]",
         activity_ko="대장암세포 HCT116에서 SW480보다 더 큰 생존율 감소(세포 실험)[8]", source=[8]),
    dict(name="Epipinoresinol", name_ko="에피피노레시놀", **{"class": "리그난(퓨로퓨란형)"}, role="bioactive", part="열매(산 처리 산물)",
         content_text="열매 10.0 g을 50 °C 30분 산 처리 후 32.8 mg 분리(순도 92.3%); 천연 함량이 아닌 피노레시놀 이성질화 산물[8]",
         activity_ko="대장암세포 HCT116 생존율 감소, 피노레시놀과 비슷한 양상(세포 실험)[8]", source=[8]),
    dict(name="Aplotaxene", name_ko="아플로탁센", **{"class": "탄화수소(헵타데카테트라엔)"}, role="bioactive", part="뿌리",
         content_text="뿌리 디클로로메테인 추출물에서 검출, 잎에서는 검출 안 됨; 사향엉겅퀴 뿌리 함량 수치는 초록에 없음(0.44%는 C. acanthoides 뿌리 값)[9]",
         activity_ko="상추 생장 50% 억제 농도 흙 1 g당 약 0.5 mg, 타감작용 후보 물질(식물 시험)[9]", source=[9]),
    dict(name="Tilianin", name_ko="틸리아닌", **{"class": "플라보노이드 배당체(아카세틴 7-글루코사이드)"}, role="bioactive", part="부위 확인 못함",
         content_text="함량 확인 못함; 문헌 고찰에서 주요 플라보노이드로 열거[5], 천연물 DB에서 이 종 1건 보고[25]",
         activity_ko="이 종에서 분리한 틸리아닌의 활성 연구는 확인하지 못함[5]", source=[5, 25]),
    dict(name="Luteolin 7-galactoside", name_ko="루테올린 7-갈락토사이드", **{"class": "플라보노이드 배당체"}, role="bioactive", part="부위 확인 못함",
         content_text="함량 확인 못함; 천연물 DB에서 이 종 1건 보고(원 문헌 확인 못함)[25]",
         activity_ko="", source=[25]),
    dict(name="Apigenin", name_ko="아피제닌", **{"class": "플라본"}, role="bioactive", part="부위 확인 못함",
         content_text="함량 확인 못함; 문헌 고찰의 주요 플라보노이드 목록[5]",
         activity_ko="문헌 고찰이 항암 보조 연구를 소개했으나 사향엉겅퀴 유래 시험은 아님[5]", source=[5]),
    dict(name="Luteolin", name_ko="루테올린", **{"class": "플라본"}, role="bioactive", part="부위 확인 못함",
         content_text="함량 확인 못함; 문헌 고찰의 주요 플라보노이드 목록[5]", activity_ko="", source=[5]),
    dict(name="Kaempferol", name_ko="캠페롤", **{"class": "플라보놀"}, role="bioactive", part="부위 확인 못함",
         content_text="함량 확인 못함; 캠페롤과 그 유도체가 주요 플라보노이드로 열거됨[5]", activity_ko="", source=[5]),
    dict(name="Rutin", name_ko="루틴", **{"class": "플라보놀 배당체"}, role="bioactive", part="부위 확인 못함",
         content_text="함량 확인 못함; 문헌 고찰의 주요 플라보노이드 목록[5]", activity_ko="", source=[5]),
    dict(name="Isorhamnetin", name_ko="이소람네틴", **{"class": "플라보놀"}, role="bioactive", part="부위 확인 못함",
         content_text="함량 확인 못함; 문헌 고찰의 주요 플라보노이드 목록[5]", activity_ko="", source=[5]),
    dict(name="beta-Sitosterol acetate", name_ko="β-시토스테롤 아세테이트", **{"class": "스테롤"}, role="bioactive", part="부위 확인 못함",
         content_text="함량 확인 못함; 문헌 고찰의 스테롤·트리테르펜 목록[5]", activity_ko="", source=[5]),
    dict(name="Taraxasterol acetate", name_ko="타락사스테롤 아세테이트", **{"class": "트리테르펜"}, role="bioactive", part="부위 확인 못함",
         content_text="함량 확인 못함; 문헌 고찰의 스테롤·트리테르펜 목록[5]", activity_ko="", source=[5]),
]

assays = [
    {"role": "literature", "compound": "Pinoresinol", "compound_ko": "피노레시놀", "part": "열매",
     "content": "열매 7.8 mg/g; 열매 10.0 g에서 피노레시놀 33.7 mg(순도 93.7%) 분리[8]",
     "method": "HPLC(온라인 산 처리 전환 확인) + 원심분배 크로마토그래피 분리",
     "conditions": {"instrument": "", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "", "injection": "",
                    "sample_prep": "원심분배 크로마토그래피 2단계, 용매계 methyl tert-butyl ether:아세톤:물 = 4:3:3 (v/v/v); 에피머화는 50 °C 30분 산 처리",
                    "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""},
     "rationale": "사향엉겅퀴 성분을 실제로 정량한 몇 안 되는 보고로 열매에 많은 리그난이다; 다만 식품원료 사용 부위(줄기)가 아닌 열매 값이고, 전문 확인 못함(초록만 확인)[8]",
     "source": [8], "url": PM + "28384606/", "source_kind": "paper"},
    {"role": "literature", "compound": "Phenolic compounds (total)", "compound_ko": "총페놀(페놀산·플라보노이드)", "part": "꽃차례(메탄올 추출물)",
     "content": "총페놀 61.49 mg/g; DPPH EC50 618 ± 10.03 μg/mL; 페놀산·플라보노이드 20여 종 확인[7]",
     "method": "HPLC-DAD, HPLC-ESI-TOF-MS",
     "conditions": {"instrument": "", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "DAD, ESI-TOF-MS", "injection": "",
                    "sample_prep": "메탄올 추출 후 분획·가수분해; 원심분배 크로마토그래피(헥세인/에틸아세테이트/메탄올/물 0.7:4:0.8:4 v/v/v/v)로 플라보노이드 분획",
                    "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""},
     "rationale": "꽃차례의 페놀 조성을 처음 체계적으로 밝힌 연구다; 개별 성분 함량과 크로마토그래피 조건은 전문 확인 못함(초록만 확인), 부위도 줄기와 다르다[7]",
     "source": [7], "url": PM + "34964548/", "source_kind": "paper"},
]

d = {
    "slug": "carduus-nutans",
    "name_ko": "사향엉겅퀴",
    "name_en": "Musk thistle",
    "scientific_name": "Carduus nutans L.",
    "aliases": ["사향엉겅퀴줄기", "Musk thistle", "Nodding plumeless thistle", "Nodding thistle"],
    "sections": [{"key": k, "title": t, "body": b} for k, (t, b) in S.items()],
    "compounds": compounds,
    "markers": [],
    "assays": assays,
    "nutrients": [],
    "production": [],
    "world": [],
    "gi": [],
    "orgs": [],
    "sources": [{"n": n, "title": t, "url": u, "publisher": p, "accessed": a} for n, t, u, p, a in sources],
}
(HERE / "dossier.json").write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in d["sections"]:
    print(s["key"], len(s["body"]))
