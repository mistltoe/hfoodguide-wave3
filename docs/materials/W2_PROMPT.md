# 소재 백과 조사 자료 작성 — 식품원료 웨이브 (작성자 W2)

너는 건강기능식품 앱 hfoodguide 의 '소재 백과' 조사 자료(dossier.json)를 쓰는 조사원이다. 독자는 일반 소비자·연구자·업계 종사자다. 쉬운 한국어로 쓰되 사실은 정확해야 한다.
기본 규칙은 `/home/claude/hf/docs/materials/W_PROMPT.md` 와 같다. **먼저 W_PROMPT.md 를 읽고**, 아래에서 다른 점만 더한다.

## 이번 소재의 입력

- `/home/claude/hf/docs/materials/<slug>/card.json` — 식약처 「식품원료 목록」(I1020)에서 모은 이 종의 자료.
  - `names`(목록의 원료명), `parts`(쓸 수 있는 부위), `conditions`(사용 조건), `status`(allowed=사용가능, restricted=제한적사용), `lists`(다른 나라 목록), `candidates`(생물자원 DB 에서 규칙으로 고른 지표성분 후보).
  - 출처 이름: "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020)", url `https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020`, accessed "2026-10-13".
- card.json 의 `lists` 에 `KR_NOTICE` 가 있으면 건강기능식품 고시형 원료의 원재료다. `/home/claude/hf/docs/refs/MFDS/MFDS_2026-43_고시형원료_요건.json`(고시 제2026-43호 원문 줄)에서 이 종을 원재료로 쓰는 원료를 찾아 markers 와 assays(official)에 넣는다(지표성분·제조기준·1일 섭취량·기능성·주의사항 원문 그대로).
- `/home/claude/hf/docs/materials/<slug>/notice.json` 이 있으면 건강기능식품 고시형 원료다. W_PROMPT 의 markers 규칙을 그대로 따른다. 없으면 `markers` 는 빈 목록이다.
- 실례: `/home/claude/hf/docs/materials/ginseng/dossier.json`, `/home/claude/hf/docs/materials/green-tea/dossier.json`.

## 쓸 것 (W_PROMPT 의 항목에 더해)

1. `sections` 8개는 그대로다(300–800자, 모든 문장 끝 [n]).
   - overview 에 **식품원료로서의 지위**(사용 가능 부위·조건, 제한적 사용이면 그 조건)를 card.json 출처로 한 문장 이상 넣는다.
   - 식품(채소·과일·곡물·수산물)으로 흔히 먹는 소재는 safety 절에 알레르기·잔류·독성 성분 등 공공기관 정보를 넣는다(없으면 "확인하지 못함").
2. `assays` (새 항목) — **지표성분과 분석 조건**. 1–4개.
   - 각 항목: `{"role": "official"|"literature", "compound": 영문명, "compound_ko": 한글명, "part": 부위, "content": 보고 함량(출처 숫자 그대로),
     "method": "HPLC-UV" 등, "conditions": {"instrument","column","mobile_phase","gradient","flow","temp","detection","injection","sample_prep","standard","linearity","lod","loq","recovery"},
     "rationale": 왜 이 성분이 지표로 쓰이는가, "source": [n], "url": 원문 url, "source_kind": "notice"|"codex"|"paper"}`
   - `official`: 식약처 고시·공전(건강기능식품 기준 및 규격, 식품공전)에 이 소재의 지표성분이 있을 때만. 공전 시험법 조건은 `/home/claude/hf/docs/refs/MFDS/hf_methods.json`(제4. 시험방법, 번호별)에 있고 앱이 자동으로 붙인다 — `method` 에 "「건강기능식품의 기준 및 규격」 제4. 3-xx 시험법"처럼 번호만 정확히 적고 conditions 는 비워 둬도 된다.
   - `literature`: 이 종(같은 부위)의 성분을 **정량한 논문**에서 분석 조건을 그대로 옮긴다. PMC 전문(Methods)을 열어 칼럼(제조사·규격), 이동상·기울기, 유속, 검출 파장/질량 조건, 검출·정량한계, 회수율을 원문 숫자대로 적는다. 초록만 본 경우 조건 칸을 비우고 rationale 에 "전문 확인 못함"이라 쓴다.
   - card.json 의 `candidates` 는 참고만 한다. 논문에서 실제로 정량·지표로 쓴 성분을 우선한다.
   - 조건을 지어내지 않는다. 확인한 칸만 채운다.
3. `production` — 국내 생산 통계. 시도별 값이 있으면 `region` 에 시도 이름을 넣는다(전국은 "대한민국").
   - 앱이 통계청 농작물생산통계(2003–2023)·2024 특용작물 생산실적의 **시도별 표를 자동으로 붙인다**(`/home/claude/hf/docs/stats/regional_crops.csv`, `regional_crops_map.json`). 이 표에 있는 품목은 시도별 행을 다시 쓰지 말고, 본문에서 인용할 때만 이 파일 값을 쓴다. 출처는 "통계청 「농작물생산조사(농작물생산통계)」 <판 연도>년판" 또는 "농림축산식품부 「2024 특용작물 생산실적」".
   - 로컬 통계: `/home/claude/hf/docs/stats/special_crops_annual.csv`, `special_crops_2024.csv`(특용작물), 그 밖에 `/home/claude/hf/docs/stats/` 의 파일.
   - 통계청 보도자료·KOSIS·농식품부·해양수산부·산림청 공식 자료. 단위·연도를 정확히.
4. `gi` (새 항목, 선택) — 지리적 표시 등록. 공식 출처(농식품부·국립농산물품질관리원·해양수산부 보도자료 등)에서 확인한 것만.
   - 각 항목: `{"gi_type": "농산물"|"임산물"|"수산물", "reg_no": "114", "name": "예천참기름", "product": 품목, "region": 대상 지역, "holder": 등록 단체, "registered_on": "YYYY-MM-DD", "source": [n]}`
   - 앱이 공공데이터(`/home/claude/hf/docs/materials/foodlist/gi.json`, 국립농산물품질관리원·국립수산물품질관리원 등록 현황)로 지리적 표시를 자동으로 붙인다. **`gi` 는 빈 목록으로 둔다.** 본문(production 등)에서 지리적 표시를 언급하려면 gi.json 에서 이 종의 `key` 와 같은 항목만 쓰고, 출처는 그 항목의 `source` 문자열 그대로.
5. `orgs` (새 항목, 선택) — 품목 협회·연구회·생산자 조직: `{"name", "role": "association"|"cooperative"|"research", "region", "url", "source": [n]}`. 공식 홈페이지나 공공기관 자료로 확인한 것만.

## 검색 한도

- 이 대화의 웹 검색(WebSearch)은 모든 작성자가 함께 쓰는 한도가 있다. **WebSearch 는 5회 이하**로 쓴다.
- 논문은 PubMed 도구, 공식 페이지는 아는 주소를 WebFetch 로 직접 연다. 막히면 우회하지 않는다.

## 출력과 검사

- `/home/claude/hf/docs/materials/<slug>/dossier.json` 에 쓴다(slug·name_ko·name_en·scientific_name·aliases 포함). 도우미 파일은 `<slug>/_work/` 에만.
- `python3 /home/claude/hf/docs/materials/check_dossier.py <slug>` 와 `python3 /home/claude/hf/docs/materials/check_units.py <slug>` 가 모두 0 이 될 때까지 고친다.

## 최종 답

한 줄: "<slug>: 출처 N, 성분 M, 분석조건 A(전문 확인 B), 생산 P행, GI G, 확인하지 못한 것: …".

## PubMed 도구가 없을 때
- PubMed 도구(mcp__PubMed__*)가 보이지 않으면 Bash 에서 NCBI E-utilities 를 직접 쓴다(공개 API): `python3 -c` 로 `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=...&retmode=json`, `efetch.fcgi?db=pubmed&id=...&rettype=abstract&retmode=text`, 전문은 `efetch.fcgi?db=pmc&id=PMC...`(XML) 를 urllib 로 연다. 요청 사이 0.4초 이상 쉰다. 막히면(403·429) 우회하지 않는다.
