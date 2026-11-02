# 소재 백과 조사 자료 대조 — 식품원료 웨이브 (검토자 V2)

`/home/claude/hf/docs/materials/V_PROMPT.md` 를 먼저 읽고 그대로 따른다. 작성 지침은 `W2_PROMPT.md`(그리고 W_PROMPT.md)다. 아래를 더 본다.

- **assays(분석 조건)**: 논문을 열어 Methods 의 칼럼·이동상·기울기·유속·검출 조건·검출한계를 한 칸씩 대조한다. 원문에 없는 칸은 지운다. 그 성분이 그 논문에서 실제로 정량됐는지, 부위가 맞는지 본다. `official` 은 고시·공전 원문에 있을 때만 남긴다.
- **production·gi·orgs**: 숫자·연도·단위·지역·등록번호·등록 단체를 원 출처와 대조한다. 확인할 수 없으면 지운다.
- **card.json**: overview 의 식품원료 지위(부위·조건)가 card.json 과 같은지 본다.
- WebSearch 는 5회 이하. 막힌 페이지는 우회하지 않는다.
- 검사 두 개(`check_dossier.py`, `check_units.py`)를 0 으로 만들고 `<slug>/review.json` 을 쓴다(형식은 V_PROMPT.md).

최종 답 한 줄: "<slug>: 대조 문장 N·항목 M, 확인 a, 수정 b, 삭제 c, 확인 불가 d — 주요 수정: …".

## PubMed 도구가 없을 때
- PubMed 도구(mcp__PubMed__*)가 보이지 않으면 Bash 에서 NCBI E-utilities 를 직접 쓴다(공개 API): `python3 -c` 로 `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=...&retmode=json`, `efetch.fcgi?db=pubmed&id=...&rettype=abstract&retmode=text`, 전문은 `efetch.fcgi?db=pmc&id=PMC...`(XML) 를 urllib 로 연다. 요청 사이 0.4초 이상 쉰다. 막히면(403·429) 우회하지 않는다.
