import json, re
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "dossier.json"
A = "2026-11-02"

def pm(title, cite, doi, pmid, note="초록 확인"):
    return {"title": f"{title} {cite} ({note})", "url": f"https://doi.org/{doi}" if doi else f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
            "publisher": f"{cite.split(' ')[0]}, PMID {pmid}", "accessed": A}

S = {}
S["mfds"] = {"title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — Oncorhynchus masou masou 6행: 원료명 송어·산천어·송어살·송어알·송어이리추출물·훈제송어, 분류 수산물, 대분류 식품원료(A코드), 부위 '-'(송어·산천어·훈제송어)·'균핵'(송어알)·'죽순'(송어살)·'과육'(송어이리추출물), 사용조건 기준 없음, 상태 모두 사용가능, 별명 고들메기·반어·열목어·쪼고리·시마연어(산천어 행은 별명 없음), 영문 Cherry salmom(원문 표기)·Cheery salmon, Trout(산천어 행); 같은 속 다른 종 행: 연어·태평양연어 등(O. keta), 곱사연어(O. gorbuscha), 은연어(O. kisutch), 무지개송어(O. mykiss, 별명 '송어'), 왕연어(O. tshawytscha), Sockeye salmon(O. nerka); 고시형 원료 원재료 목록(KR_NOTICE) 없음 — 로컬 원자료 data/raw/mfds_rawmtrl/I1020_20261013.json, docs/materials/oncorhynchus-masou/card.json",
             "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"}
S["parv"] = pm("[Comparative analyses of allergens between landlocked and anadromous species of masu salmon Oncorhynchus masou masou].", "Shokuhin Eiseigaku Zasshi 2012;53(1):8-13, 일본어 논문 영문 초록", "10.3358/shokueishi.53.8", "22450663")
S["ans"] = pm("White muscle of masu salmon, Oncorhynchus masou masou, smolts possesses a strong buffering capacity due to a high level of anserine.", "Fish Physiol Biochem 1994;13(4):285-93", "10.1007/BF00003432", "24198207")
S["mdt"] = pm("An unusual vitamin E constituent (alpha-tocomonoenol) provides enhanced antioxidant protection in marine organisms adapted to cold-water environments.", "Proc Natl Acad Sci U S A 2001;98(23):13144-8", "10.1073/pnas.241024298", "11687648", "초록 확인, PMC60838 전문은 도구로 받지 못함")
S["pcb"] = pm("Polychlorinated biphenyl (PCB) concentrations and congener composition in masu salmon from Japan: a study of all 209 PCB congeners by HRGC/HRMS.", "Mar Pollut Bull 2014;85(2):549-57", "10.1016/j.marpolbul.2014.04.021", "24820644")
S["pops"] = pm("Concentrations of persistent organic pollutants in masu salmon, Oncorhynchus masou.", "Bull Environ Contam Toxicol 2009;83(3):393-7", "10.1007/s00128-009-9785-6", "19462150")
S["cs"] = pm("Radiocaesium concentrations in the muscle and eggs of salmonids from Lake Chuzenji, Japan, after the Fukushima fallout.", "J Fish Biol 2014;84(5):1607-13", "10.1111/jfb.12368", "24684433")
S["metal"] = pm("Significant metal accumulation in fish in a metal-contaminated river without detectable effects on fish and macroinvertebrate communities.", "Environ Toxicol Chem 2025;44(5)", "10.1093/etojnl/vgaf047", "39951317")
S["dn10"] = pm("Detection and identification of Diphyllobothrium nihonkaiense plerocercoids from wild Pacific salmon (Oncorhynchus spp.) in Japan.", "J Helminthol 2010;84(4):434-40", "10.1017/S0022149X10000155", "20334715")
S["dn18"] = pm("Epidemiology of Diphyllobothrium nihonkaiense Diphyllobothriasis, Japan, 2001-2016.", "Emerg Infect Dis 2018;24(8):1428-34", "10.3201/eid2408.171454", "30016246")
S["dn25"] = pm("Tapeworm infection incidence in rural Japan points to a common environmental source of infection.", "Drug Discov Ther 2025;19(5):351-357", "10.5582/ddt.2025.01070", "41093588")
S["dl83"] = pm("[Epidemiology of Diphyllobothrium latum infection in Japan, with special reference to infection of cherry salmon].", "Jpn J Antibiot 1983;36(3):566-72", None, "6876363")
S["kr01"] = pm("Diphyllobothrium latum infection after eating domestic salmon flesh.", "Korean J Parasitol 2001;39(4):319-21", "10.3347/kjp.2001.39.4.319", "11775333")
S["kr14"] = pm("Three cases of Diphyllobothrium nihonkaiense infection in Korea.", "Korean J Parasitol 2014;52(6):673-6", "10.3347/kjp.2014.52.6.673", "25548420")
S["kab"] = pm("Redescription of Microsporidium takedai (Awakura, 1974) as Kabatana takedai (Awakura, 1974) comb. n.", "Dis Aquat Organ 2001;44(3):223-30", "10.3354/dao044223", "11383570")
S["sakh"] = pm("[Microsporidiosis of Sakhalin Salmonidae: the incidence and dynamics of the infection].", "Parazitologiia 1987;21(4):553-8, 러시아어 논문 영문 초록", None, "3658480")
S["genome"] = pm("Chromosome-level genome assembly of masu salmon (Oncorhynchus masou masou).", "Sci Data 2026;13(1)", "10.1038/s41597-026-06943-8", "41748671")
S["reseq"] = pm("Genetic Diversity and Runs of Homozygosity in Three Masu Salmon Populations Based on Whole-Genome Resequencing Data.", "Biomolecules 2026;16(8):1187", "10.3390/biom16081187", "42650853")
S["popgen"] = pm("Population genetic structure and phylogeography of masu salmon (Oncorhynchus masou masou) inferred from mitochondrial and microsatellite DNA analyses.", "Zoolog Sci 2010;27(5):375-85", "10.2108/zsj.27.375", "20443684")
S["hatch"] = pm("Fingerprinting of hatchery haplotypes and acquisition of genetic information by whole-mitogenome sequencing of masu salmon, Oncorhynchus masou masou, in the Kase River system, Japan.", "PLoS One 2020;15(11):e0240823", "10.1371/journal.pone.0240823", "33147284")
S["smolt"] = pm("Size-driven parr-smolt transformation in masu salmon (Oncorhynchus masou).", "Sci Rep 2023;13(1):16643", "10.1038/s41598-023-43632-7", "37789097")
S["bist"] = pm("Evolutionary bistability of life history decision in male masu salmon.", "J Theor Biol 2018;448:104-111", "10.1016/j.jtbi.2018.04.008", "29630993")
S["itero"] = pm("Iteroparity of stream resident masu salmon Oncorhynchus masou.", "J Fish Biol 2018;93(4):750-754", "10.1111/jfb.13771", "30069884")
S["diet"] = pm("Diet Diversity of the Fluviatile Masu Salmon (Brevoort 1856) Revealed via Gastrointestinal Environmental DNA Metabarcoding and Morphological Identification of Contents.", "Biology (Basel) 2024;13(2):129", "10.3390/biology13020129", "38392347")
S["temp"] = pm("Impacts of Temperature on the Growth, Feed Utilization, Stress, and Hemato-Immune Responses of Cherry Salmon.", "Animals (Basel) 2023;13(24):3870", "10.3390/ani13243870", "38136907", "PMC10740505 전문 확인")
S["domes"] = pm("Domestication of captive-bred masu salmon Oncorhynchus masou masou (Salmonidae) leads to a significant decrease in numbers of lateral line organs.", "Sci Rep 2022;12(1):16780", "10.1038/s41598-022-21195-3", "36202921")
S["heart"] = pm("Cardiac hemodynamics and ventricular stiffness of sea-run cherry salmon (Oncorhynchus masou masou) differ critically from those of landlocked masu salmon.", "PLoS One 2022;17(11):e0267264", "10.1371/journal.pone.0267264", "36331913")
S["mse_mice"] = pm("Masou salmon (Oncorhynchus masou) ethanol extract decreases 3-hydroxy-3-methylglutaryl coenzyme A reductase expression in diet-induced obese mice.", "Nutr Res 2009;29(2):123-9", "10.1016/j.nutres.2008.11.006", "19285603")
S["mse_ao"] = pm("Antioxidative and antimutagenic activities of 70% ethanol extract from masou salmon (Oncorhynchus masou).", "Toxicol In Vitro 2008;22(6):1484-8", "10.1016/j.tiv.2008.05.002", "18682318")
S["amago_al"] = pm("Comparative study of GH-transgenic and non-transgenic amago salmon (Oncorhynchus masou ishikawae) allergenicity and proteomic analysis of amago salmon allergens.", "Regul Toxicol Pharmacol 2009;55(3):300-8", "10.1016/j.yrtph.2009.08.002", "19679156")
S["rflp"] = pm("Molecular identification of biwa trout using PCR-RFLP method.", "J Food Sci Technol 2019;56(10):4705-4713", "10.1007/s13197-019-03914-3", "31686702")
S["formo"] = pm("Complete mitochondrial genome of Oncorhynchus masou formosanus (Jordan & Oshima, 1919) (Pisces, Salmonidae).", "Mitochondrial DNA B Resour 2016;1(1)", "10.1080/23802359.2016.1166084", "33644363")
S["aero"] = pm("Isolation of Aeromonas salmonicida from masu salmon in the Republic of Korea.", "J Wildl Dis 1988;24(2):364-5", "10.7589/0090-3558-24.2.364", "3373645")
S["elovl"] = pm("CRISPR/Cas9-Mediated Transgenesis of the Masu Salmon (Oncorhynchus masou) elovl2 Gene Improves n-3 Fatty Acid Content in Channel Catfish (Ictalurus punctatus).", "Mar Biotechnol (NY) 2022;24(3)", "10.1007/s10126-022-10110-6", "35416602")
S["carot"] = pm("Distribution of carotenoids in the eggs from four species of salmonids.", "Comp Biochem Physiol B 1991;99(2):341-4", "10.1016/0305-0491(91)90052-f", "1764913")
S["gnath"] = pm("Gnathostomiasis caused by ingestion of raw Oncorhynchus masou ishikawae roe.", "J Dermatol 2017;44(5)", "10.1111/1346-8138.13893", "28470869", "제목만 확인 — 초록 없음")

ORDER = ["mfds", "parv", "ans", "mdt", "pcb", "pops", "cs", "metal", "dn10", "dn18", "dn25", "dl83", "kr01", "kr14", "kab", "sakh",
         "genome", "reseq", "popgen", "hatch", "smolt", "bist", "itero", "diet", "temp", "domes", "heart", "mse_mice", "mse_ao",
         "amago_al", "rflp", "formo", "aero", "elovl", "carot", "gnath"]
N = {k: i + 1 for i, k in enumerate(ORDER)}

def r(text):
    """{key} / {k1,k2} -> [n] numbers"""
    def rep(m):
        ks = [x.strip() for x in m.group(1).split(",")]
        return "[" + ", ".join(str(N[k]) for k in ks) + "]"
    return re.sub(r"\{([a-z0-9_, ]+)\}", rep, text)

def src(*ks):
    return [N[k] for k in ks]

sections = [
 ("overview", "한눈에 보기", """송어(Oncorhynchus masou)는 식약처 「식품원료 목록」에 학명 Oncorhynchus masou masou로 6개 행이 올라 있는 수산물이다{mfds}. 원료명은 송어·산천어·송어살·송어알·송어이리추출물·훈제송어이고, 모든 행의 상태는 '사용가능'이며 따로 정한 사용 조건은 없다{mfds}. 부위 칸은 원자료 표기 그대로 송어·산천어·훈제송어가 '-', 송어알이 '균핵', 송어살이 '죽순', 송어이리추출물이 '과육'으로 적혀 있다{mfds}. 별명 칸에는 고들메기·반어·열목어·쪼고리·시마연어가 있고, 영문명은 'Cherry salmom'(원문 표기)과 산천어 행의 'Cheery salmon, Trout'로 적혀 있다{mfds}. 건강기능식품 고시형 원료의 원재료 목록에는 없어 식약처가 정한 지표성분은 없다{mfds}.

송어는 북서태평양 쪽에만 사는 연어속 물고기로, 영문으로는 masu salmon 또는 cherry salmon이라 부른다{temp}. 한 집단 안에서도 바다로 내려갔다 돌아오는 개체와 강에 남는 개체가 함께 생기는 '부분 회유'를 하며, 강에 남는 형을 육봉형이라 한다{smolt, heart}. 같은 목록에서 무지개송어(O. mykiss) 행의 별명도 '송어'여서, 시장 이름 '송어'만으로는 어느 종인지 구별되지 않는다{mfds}. 이 문서는 O. masou 자료만 모았고, 아종(아마고 등) 자료는 그렇다고 밝혀 적었다{mfds}."""),
 ("history", "이용·연구 역사", """일본에서는 1977–1982년 매년 3–5월 동해 북부에서 잡은 송어 723마리를 조사해 30.2%(218마리)에서 열두촌충류 유충을 찾았고, 당시에는 이를 광절열두조충(D. latum)으로 보고했다{dl83}. 이 연구는 일본의 광절열두조충이 연어속 물고기를 주된 제2중간숙주로 삼고 유충이 내장이 아닌 살(필레)에서 발견된다는 점을 짚었다{dl83}. 한국에서는 1988년 양양 연어 부화장의 송어에서 세균성 어병균 Aeromonas salmonicida를 분리한 보고가 아시아 대륙 첫 보고로 나왔다{aero}.

2001년에는 국내 하천에서 잡은 송어를 날로 먹은 가족 중 두 명이 촌충에 감염된 사례가 국내 학술지에 보고되었다{kr01}. 2008–2009년에는 국내에서 잡은 송어의 70% 에탄올 추출물로 항산화·항돌연변이 시험과 비만 생쥐 실험을 한 연구가 나왔다{mse_ao, mse_mice}. 일본에서는 송어가 유어(낚시)용으로 흔히 방류되어 왔고, 규슈 가세강 수계에서는 미토콘드리아 유전체로 부화장 계통의 흔적을 추적했다{hatch}. 2012년 9–12월에는 후쿠시마 원전 사고 약 18개월 뒤 주젠지호 송어 등의 살과 알에서 방사성세슘을 측정했다{cs}. 중국은 2021년 송어를 국가 2급 보호동물로 지정했다{diet}. 2026년에는 염색체 수준의 송어 참조 유전체가 발표되었다{genome}."""),
 ("biology", "어종·생활사", """송어는 북서태평양의 북위 34–65°, 동경 127–158° 사이에만 분포한다고 소개된다{temp}. 어린 개체가 바다 생활을 준비하는 은화(스몰트화)는 몸 크기와 낮 길이에 함께 좌우되어, 가랑이 길이(fork length) 12 cm를 넘은 개체만 아가미 Na+,K+-ATPase 활성이 올라갔다{smolt}. 첫해 여름에는 낮 길이 조건 아래 크기가 이끄는 은화가, 이듬해 봄에는 크기 조건 아래 낮 길이가 이끄는 은화가 일어난다고 정리되었다{smolt}. 수컷 일부는 바다로 갔다 돌아오고 일부는 강에 남아 성숙하며, 어느 쪽을 택할지는 몸 크기와 관련된다{bist}.

하천 잔류형의 표지·재포획 조사에서는 부분 회유 집단의 잔류형 수컷 10% 이상이 성숙 뒤 살아남아 최대 5년까지 거듭 성숙했다{itero}. 중국 미장강의 하천형 송어는 전체적으로 물속 먹이를 더 많이 먹었으나, 크고 나이 든 개체일수록 육상 곤충을 더 많이 먹었다{diet}. 수정 후 29–30개월 된 강해형의 심장 무게는 육봉형의 약 11배였고 심실은 상대적으로 더 단단했다{heart}. 강해형으로 가는 스몰트의 흰 근육에는 파(어린 시기)보다 안세린이 늘 더 많아, 하류로 내려갈 때 순간 헤엄에 필요한 완충 능력이 높다고 해석되었다{ans}."""),
 ("related_species", "관련 종·이름", """식약처 「식품원료 목록」에는 같은 연어속에서 연어·태평양연어(O. keta), 곱사연어(O. gorbuscha), 은연어(O. kisutch), 무지개송어(O. mykiss), 왕연어(O. tshawytscha), Sockeye salmon(O. nerka)이 각각 따로 올라 있으며, 이 문서는 그 종들의 자료를 쓰지 않았다{mfds}. 목록의 무지개송어 행 별명이 '송어'이므로, 원료명 '송어'를 볼 때는 학명을 함께 확인해야 한다{mfds}. 이 종의 목록 별명(고들메기·반어·열목어·쪼고리·시마연어)이 각각 이 종만 가리키는지는 확인하지 못함.

O. masou에는 아종 아마고(O. masou ishikawae)와 대만의 육봉 아종(O. masou formosanus)이 있으며, 식품원료 목록의 학명은 O. masou masou 하나뿐이다{mfds, formo, amago_al}. 대만 아종의 미토콘드리아 유전체는 16,653 bp였고, 이 아종은 심각한 멸종위기 육봉 연어로 소개된다{formo}. 일본에서는 비와송어·아마고·야마메(육봉형 송어)·무지개송어의 살을 미토콘드리아 ND4–ND5, ND1 유전자 PCR-RFLP로 구별했고, 가열 가공한 시료에서도 구별되었다{rflp}. 육봉형(야마메)과 강해형(사쿠라마스)은 같은 아종이며 파브알부민 이성체 세 가지가 서로 같았다{parv}."""),
 ("cultivation", "어획·양식·방류", """야생 송어 집단은 크게 줄었으나 한국에서는 민물 양식이 이어지고 있다고 소개되며, 2021년 국내 실험에는 화천의 양식장에서 부화 5개월 된 어린 송어를 들여왔다{temp}. 평균 29.1 g의 어린 송어를 8주 동안 10·14·18·22 °C에서 기른 실험에서 10 °C와 14 °C에서 몸무게·성장률·사료 효율이 가장 좋았고, 22 °C에서는 먹이 반응과 적혈구 지표가 떨어졌다{temp}. 저자들은 양식장 수온을 22 °C 아래로 유지하고, 성장과 건강을 함께 보면 14 °C가 더 알맞을 수 있다고 보았다{temp}.

일본에서는 송어를 방류용으로 기르며, 규슈 가세강 수계 17개 지점 중 13곳에서 부화장 계통의 미토콘드리아 유전체 일배체형(21개 중 6개)이 나와 비공식 방류가 넓게 이루어졌음이 드러났다{hatch}. 여러 세대 사육한 송어는 자연산·1세대보다 옆줄 감각기(신경소구) 수가 약 10% 적어, 방류 뒤 생존율이 낮은 이유의 하나로 제시되었다{domes}. 양식 송어가 비타민 E 변형체(α-토코모노엔올)가 거의 없는 사료를 먹으면 살에 이 성분이 자연산보다 훨씬 적었다{mdt}. 국내 송어 어획량·양식 생산량 통계는 이번 조사에서 확인하지 못함."""),
 ("processing", "가공·이용", """식품원료 목록에는 송어와 산천어 외에 송어살·송어알·훈제송어·송어이리추출물이 따로 올라 있어, 살·알·이리(정소)와 훈제품이 원료로 쓰일 수 있다{mfds}. 이 원료들의 국내 가공·생산 실적은 확인하지 못함.

국내에서 잡은 송어의 70% 에탄올 추출물은 총페놀이 3.6±0.2 mg/g이었고, DPPH 라디칼 소거와 환원력 시험에서 항산화 활성을 보였다{mse_ao}. 같은 추출물은 Ames 시험(TA98·TA100, 0.25–25.0 mg/plate)에서 돌연변이를 일으키지 않았고, 4NQO·MNNG로 유도한 돌연변이를 농도에 따라 억제했다{mse_ao}. 고지방 식이로 살찐 생쥐에게 이 추출물을 사료 1 kg당 75 mg 또는 150 mg 넣어 4주 먹인 실험에서는 혈장과 간의 총콜레스테롤이 각각 12.3%, 16.2% 낮아졌고 간의 HMG-CoA 환원효소 mRNA가 최대 5배 줄었다{mse_mice}. 이 결과들은 시험관·동물 실험이며 사람에게서 같은 효과가 있는지는 확인하지 못함.

송어 알의 카로티노이드는 지질 입자보다 난황 단백질(리포비텔린)에 주로 붙어 있었다(원문은 양식 히메마스와 송어를 함께 기술)[{carot_n}]. 가공품의 종 판별에는 가열 뒤에도 쓸 수 있는 PCR-RFLP 방법이 제시되었다{rflp}."""),
 ("genetics", "유전 정보", """2026년 발표된 송어(O. masou masou) 유전체는 PacBio HiFi·나노포어 초장 리드·Hi-C로 조립되었고, 두 반수체가 각각 2.5 Gb와 2.4 Gb였다{genome}. 스캐폴드 N50은 99.28 Mb와 98.82 Mb였고, 가장 긴 33개 스캐폴드가 유전체의 99.6% 이상을 덮었으며, BUSCO 완전도는 98.3%와 97.7%였다{genome}. 단백질 유전자는 41,858개와 40,970개로 예측되었고, 산란 뒤 시점별 전사체 90개도 함께 공개되었다{genome}.

중국 두만강 야외 채집 집단과 육봉 양식 집단 두 곳의 465마리 전장 유전체 재분석에서는 고품질 SNP 6,220,980개가 남았고, 각 집단 변이의 약 91%가 인트론·유전자 사이 영역에 있었다{reseq}. 두만강 집단은 유전 다양성이 가장 낮고 동형접합 구간(ROH) 부담이 가장 컸다{reseq}. 일본 9곳·러시아 7곳·한국 2곳의 18개 집단 895마리를 미토콘드리아 ND5와 미세위성 6좌위로 본 연구에서는 ND5 일배체형 20개가 나왔고, 일본·한국 집단의 다양성이 러시아보다 높았다{popgen}. 이 구조는 홍적세 말 빙하기 병목과 간빙기 확장의 영향으로 해석되었다{popgen}. 송어에서 분리한 지방산 연장효소 유전자 elovl2를 넣은 채널메기는 근육 DHA가 1.62배 높았다{elovl}."""),
 ("safety", "안전성", """송어는 날로 먹으면 동해긴촌충(Diphyllobothrium nihonkaiense) 감염 위험이 있다{dn10, dn18}. 일본 야생 연어류 조사에서 송어는 82마리 중 12.2%에서 유충이 나왔고, 송어 유충은 분자 분석으로 동해긴촌충으로 확인되었다{dn10}. 일본의 2001–2016년 촌충증 958건 중 86.1%가 동해긴촌충이었고, 송어와 미성숙 연어(O. keta) 어기인 3–7월에 많았다{dn18}. 2022–2023년 야마가타현 환자 중 3명은 날 송어 섭취와 관련되었다{dn25}. 국내에서도 2001년 국내 하천 송어를 날로 먹은 두 명의 감염이 형태로 광절열두조충으로 보고되었고, 이후 유전자 분석한 국내 표본은 모두 동해긴촌충이었다(2001년 사례 포함 여부는 확인하지 못함){kr01, kr14}. 아종 아마고의 알을 날로 먹은 악구충증 사례 보고도 있다(제목만 확인){gnath}. 살 속 미포자충(Kabatana takedai) 감염도 보고되었다{kab, sakh}.

어류 주요 알레르기 단백질인 파브알부민은 육봉형 야마메 살에 강해형보다 많았고, 환자 혈청 반응도 더 강했다{parv}. 일본 송어 살의 PCB 독성등가량은 최고 1.96 pg-TEQ/g(습중량)이었다{pcb}. 광산 배수가 흘러드는 하천의 송어 살 카드뮴은 대조 하천 평균의 188–520배였다{metal}. 식약처 등 국내 공공기관의 송어 알레르기 표시·잔류물질 안전 정보는 이번 조사에서 확인하지 못함."""),
]

def fix_carot(t):
    return t.replace("[{carot_n}]", "{carot}")

compounds = [
 {"name": "Parvalbumin", "name_ko": "파브알부민", "class": "칼슘결합 근육 단백질(어류 주요 알레르겐)", "role": "marker", "part": "살(근육)",
  "content_text": "가시광 ELISA: 육봉형(야마메) 1.8–7.8 mg/g, 강해형(사쿠라마스) 0.28–0.52 mg/g(초록에 생·건 기준 표기 없음){parv}",
  "activity_ko": "어류 알레르기 환자 혈청이 야마메 가열 추출물에 더 강하게 반응했다; 아마고(아종)에서도 IgE 결합 단백질로 확인되었다{parv, amago_al}", "source": src("parv", "amago_al")},
 {"name": "Anserine", "name_ko": "안세린", "class": "이미다졸 디펩타이드", "role": "bioactive", "part": "흰 근육(양식 어린 개체)",
  "content_text": "수치는 초록에 없음 — 스몰트가 파(parr)보다 항상 높았고, 고단백 사료 스몰트에서 가장 높았다{ans}",
  "activity_ko": "생리 pH 범위에서 근육 완충 능력을 높이는 성분으로 해석되었다(근육 생리 연구){ans}", "source": src("ans")},
 {"name": "Histidine", "name_ko": "히스티딘", "class": "아미노산(유리)", "role": "nutrient", "part": "흰 근육(양식 어린 개체)",
  "content_text": "수치는 초록에 없음 — 스몰트가 파보다 항상 낮았다{ans}", "activity_ko": "안세린과 함께 근육 완충 계산에 쓰였다{ans}", "source": src("ans")},
 {"name": "alpha-Tocomonoenol", "name_ko": "α-토코모노엔올(해양 유래 토코페롤)", "class": "비타민 E 변형체", "role": "bioactive", "part": "살",
  "content_text": "송어 단독 수치는 초록에 없음 — 이 성분이 부족한 사료로 기른 양식 송어가 자연산보다 훨씬 적었다; 냉수성 연어류 살 총비타민 E 중 12–20%(여러 종 범위){mdt}",
  "activity_ko": "0 °C에서 α-토코페롤보다 리포솜 지질 과산화를 더 잘 억제했다(시험관){mdt}", "source": src("mdt")},
 {"name": "Carotenoids", "name_ko": "카로티노이드", "class": "색소", "role": "bioactive", "part": "알(배란된 미수정란)",
  "content_text": "송어 알 함량 수치는 초록에 없음 — 리포비텔린 분획에 주로 분포(원문은 양식 히메마스와 송어를 함께 기술){carot}",
  "activity_ko": "난황 형성 중 리포비텔린과 지질 입자에 결합해 알로 옮겨진다고 해석되었다(연어 O. keta 비교 결과 포함){carot}", "source": src("carot")},
 {"name": "Total phenolic compounds", "name_ko": "총페놀(70% 에탄올 추출물)", "class": "총페놀(Folin-Ciocalteu 법)", "role": "bioactive", "part": "송어 70% 에탄올 추출물(부위 초록 미기재)",
  "content_text": "3.6±0.2 mg/g(추출물 기준){mse_ao}", "activity_ko": "추출물이 DPPH 라디칼 소거·환원력을 보였다(시험관){mse_ao}", "source": src("mse_ao")},
 {"name": "Polychlorinated biphenyls", "name_ko": "폴리염화바이페닐(PCB)", "class": "잔류성 유기오염물질", "role": "marker", "part": "살(근육)",
  "content_text": "ΣPCB 최고 40.39 ng/g 습중량(아종 아마고, 원문 'ng/wet wt'); 독성등가량 최고 1.96 pg-TEQ/g 습중량(동해 남부 O. m. masou){pcb}",
  "activity_ko": "다이옥신 유사 PCB 중 독성등가계수가 가장 큰 #126의 비율이 높아 남부 해역 송어의 TEQ가 가장 높았다{pcb}", "source": src("pcb")},
 {"name": "Persistent organic pollutants", "name_ko": "잔류성 유기오염물질(POPs) 총량", "class": "잔류성 유기오염물질", "role": "marker", "part": "근육·간·아가미",
  "content_text": "몸무게의 72–78%인 근육에 전체 POPs의 75±12%, 1.8–2.32%인 간에 16±8.6%, 1.4–2.1%인 아가미에 9.1±3.8%{pops}",
  "activity_ko": "섭식 회유 끝 무렵 일본 북부 송어에서 장기별 축적 분배를 계산했다{pops}", "source": src("pops")},
 {"name": "Cesium", "name_ko": "방사성세슘", "class": "방사성 핵종", "role": "marker", "part": "살·알",
  "content_text": "2012년 9–12월 주젠지호 연어과 4종 평균: 살 142.9–249.2 Bq/kg, 알 38.7–79.0 Bq/kg(습중량, 4종 전체 범위이며 송어 단독 값 아님){cs}",
  "activity_ko": "송어에서는 개체별 살과 알의 농도가 유의하게 상관했다{cs}", "source": src("cs")},
 {"name": "Cadmium", "name_ko": "카드뮴", "class": "중금속(오염물질)", "role": "marker", "part": "살(근육)",
  "content_text": "광산 배수 하천 지점의 살 농도가 대조 지점 평균의 188–520배(절대 농도는 초록에 없음){metal}",
  "activity_ko": "농도는 크게 올랐지만 송어의 개체 수·비만도에는 뚜렷한 차이가 없었다{metal}", "source": src("metal")},
 {"name": "Lead", "name_ko": "납", "class": "중금속(오염물질)", "role": "marker", "part": "살(근육)",
  "content_text": "광산 배수 하천 지점의 살 농도가 대조 지점 평균의 4.6–68.0배{metal}", "activity_ko": "같은 연구에서 구리 1.4–2.5배, 비소 1.1–3.9배였다{metal}", "source": src("metal")},
 {"name": "Selenium", "name_ko": "셀레늄", "class": "무기질", "role": "nutrient", "part": "살(근육)",
  "content_text": "광산 배수 하천 지점의 살 농도가 대조 지점 평균의 2.8–3.5배(절대 농도는 초록에 없음){metal}", "activity_ko": "아연은 1.5–1.9배였으나 유의하지 않았다{metal}", "source": src("metal")},
]

assays = [
 {"role": "literature", "compound": "Parvalbumin", "compound_ko": "파브알부민", "part": "살(근육) 가열 추출물 — 야마메·사쿠라마스(O. masou masou)",
  "content": "야마메 1.8–7.8 mg/g, 사쿠라마스 0.28–0.52 mg/g(초록 수치, 생·건 기준 표기 없음){parv}",
  "method": "가시광 ELISA(정량); 이성체 정제는 겔여과·역상 HPLC, 분자량은 MALDI-TOF MS",
  "conditions": {"instrument": "", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "", "injection": "",
                 "sample_prep": "근육 가열 추출물(초록 기준)", "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "파브알부민은 어류의 주요 알레르겐이어서 육봉형·강해형의 알레르기 유발 잠재력을 비교하는 지표로 쓰였다{parv}. 전문 확인 못함 — 일본어 원문이고 J-STAGE 접속이 막혀 칼럼·항체·검출한계 등은 비워 둠{parv}.",
  "source": src("parv"), "url": "https://doi.org/10.3358/shokueishi.53.8", "source_kind": "paper"},
 {"role": "literature", "compound": "Polychlorinated biphenyls (209 congeners)", "compound_ko": "PCB 209종 동족체", "part": "살(근육) — O. m. masou 4개 지역, 아종 아마고 1개 지역",
  "content": "ΣPCB 최고 40.39 ng/g 습중량(아마고, 원문 'ng/wet wt'), TEQ(다이옥신 유사 PCB) 최고 1.96 pg-TEQ/g 습중량(동해 남부 O. m. masou){pcb}",
  "method": "HRGC/HRMS(고분해능 가스크로마토그래피/고분해능 질량분석)",
  "conditions": {"instrument": "", "column": "", "mobile_phase": "", "gradient": "", "flow": "", "temp": "", "detection": "고분해능 질량분석(초록 기준)", "injection": "",
                 "sample_prep": "", "standard": "", "linearity": "", "lod": "", "loq": "", "recovery": ""},
  "rationale": "209종 동족체를 모두 측정해 주성분분석으로 산지·아종별 오염 양상을 나누고, 독성등가계수가 큰 #126 비율로 TEQ 위험을 비교했다{pcb}. 전문 확인 못함 — 칼럼·검출한계 등은 비워 둠{pcb}.",
  "source": src("pcb"), "url": "https://doi.org/10.1016/j.marpolbul.2014.04.021", "source_kind": "paper"},
]

d = {
 "slug": "oncorhynchus-masou", "name_ko": "송어", "name_en": "Masu salmon (Cherry salmon)",
 "scientific_name": "Oncorhynchus masou (Brevoort, 1856)",
 "aliases": ["송어", "산천어", "시마연어", "Masu salmon", "Cherry salmon", "Oncorhynchus masou masou"],
 "sections": [{"key": k, "title": t, "body": r(fix_carot(b))} for k, t, b in sections],
 "compounds": [], "markers": [], "assays": [], "nutrients": [], "production": [], "world": [], "gi": [], "orgs": [],
 "sources": [dict(n=N[k], **S[k]) for k in ORDER],
}
for c in compounds:
    c = dict(c); c["content_text"] = r(c["content_text"]); c["activity_ko"] = r(c["activity_ko"]); d["compounds"].append(c)
for a in assays:
    a = dict(a); a["content"] = r(a["content"]); a["rationale"] = r(a["rationale"]); d["assays"].append(a)
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in d["sections"]:
    print(s["key"], len(s["body"]))
print(len(d["sources"]), "sources")
