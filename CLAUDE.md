# hfoodguide 소재 백과 — 웨이브 3 클라우드 작업 저장소

이 저장소는 PC 앱(healthFoodApp)에서 소재 백과 작성에 필요한 파일만 뽑아 온 것이다. 결과(종별 `dossier.json`·`review.json`)를 만들어 커밋·푸시하면 PC 에서 가져가 반영한다.

## 경로 규칙
- 지시문 파일 속 `/home/claude/hf` 는 **이 저장소의 루트**로 읽는다. 예: `/home/claude/hf/docs/materials/check_dossier.py` → `docs/materials/check_dossier.py`.
- 하위 에이전트에게 지시할 때도 이 규칙을 알려 준다.

## 할 일: 웨이브 3 진행
- 대상: `docs/materials/foodlist/waves/wave_03.json` 의 순서대로. `review.json` 이 이미 있는 종은 건너뛴다(끝난 종).
- `dossier.json` 은 있고 `review.json` 이 없는 종은 V2(대조)만 한다.
- **8종씩 한 묶음**으로 진행한다.
  1. 8종의 W2 하위 에이전트를 **한 번에 병렬로** 띄운다(Task 도구, general-purpose). 지시문은 아래 W2 틀을 그대로 쓴다.
  2. 8개가 끝나면 8종의 V2 하위 에이전트를 병렬로 띄운다(아래 V2 틀).
  3. 8종 모두 `python3 docs/materials/check_dossier.py <slug>` 와 `python3 docs/materials/check_units.py <slug>` 가 0 인지 확인한다. 0 이 아니면 그 종의 V2 에이전트에게 고치게 하거나, 안 되면 커밋 메시지에 적고 넘어간다.
  4. **묶음마다 커밋하고 푸시한다.** 메시지: `웨이브 3 묶음 NN(8종) 작성·대조 — 누적 MMM종`. 작업이 중간에 끊겨도 앞 묶음은 남게 한다.
- 각 묶음이 끝나면 사용자에게 한 줄로 알린다: 끝난 종, 주요 수정 사례 1~2개.
- 사용자가 멈추라고 하거나, 사용량(크레딧)이 부족하다는 안내가 나오면 진행 중인 묶음을 커밋·푸시하고 멈춘다.

## W2 틀 (slug·국문·학명·힌트만 바꾼다)
> 너는 hfoodguide 소재 백과 작성자(W2)다. 작업 폴더는 이 저장소 루트이고, 지시문 속 '/home/claude/hf' 는 이 루트로 읽는다. 소재 slug: {slug} (국문 {name_ko}, 학명 {key}). 1. docs/materials/W2_PROMPT.md 를 읽고 그대로 따르라(그 안에서 가리키는 W_PROMPT.md 도 읽어라). {힌트} 2. 입력 docs/materials/{slug}/card.json, 결과 dossier.json 은 같은 폴더에 파일로 저장(답에 붙이지 않음). 도우미 파일은 docs/materials/{slug}/_work/ 에. 3. check_dossier.py·check_units.py 결과 0 이어야 한다. 4. 차단(캡차·403·robots·429)된 페이지는 어떤 도구로도 다시 열지 마라(우회 금지), 사람 이름·전화·이메일 금지, 상표명 대신 일반명, WebSearch 5회 이하, 이 종 폴더 밖의 파일은 고치지 마라. 최종 답은 W2_PROMPT.md 가 정한 한 줄 형식으로.

## V2 틀
> 너는 hfoodguide 소재 백과 대조 검토자(V2)다. 작업 폴더는 이 저장소 루트이고, 지시문 속 '/home/claude/hf' 는 이 루트로 읽는다. 소재 slug: {slug} (국문 {name_ko}, 학명 {key}). 1. docs/materials/V2_PROMPT.md 를 읽고 그대로 따르라(필요하면 V_PROMPT.md 도). 2. 입력 docs/materials/{slug}/card.json·dossier.json, 결과 review.json 은 같은 폴더에 파일로 저장(답에 붙이지 않음). 도우미 파일은 docs/materials/{slug}/_review/ 에. 3. 특히 볼 것: 다른 종·근연종 자료 섞임, 수치·단위·기준(생/건)이 원문과 맞는지, 세포·동물 결과의 과장, 국문명·식품원료 지위 근거. {힌트} 4. 고친 뒤 check_dossier.py·check_units.py 결과 0 이어야 한다. 5. 차단된 페이지는 어떤 도구로도 다시 열지 마라(우회 금지), 사람 이름·전화·이메일 금지, 상표명 대신 일반명, WebSearch 5회 이하, 이 종 폴더 밖의 파일은 고치지 마라. 최종 답은 V2_PROMPT.md 가 정한 한 줄 형식으로.

## 힌트 만드는 법 (오케스트레이터가 채운다)
- `docs/materials/foodlist/cards.json` 의 `species` 에서 같은 속(학명 첫 낱말)의 다른 원료를 최대 6개 찾아 "같은 속의 다른 식품원료(… ) 자료와 섞지 마라." 로 넣는다.
- card.json 의 `status` 가 `restricted` 이면 "식약처 식품원료 목록 상태가 '제한적사용'이다 — 안전성·사용 조건을 출처와 함께 분명히 적어라." 를 넣는다.
- 종 특성(독성·수은·옥살산·이명 혼동 등)이 짐작되면 한 줄 더한다.

## 하지 않는 것
- `collect_material.py`·DB 적재는 PC 에서 한다(이 저장소에는 없다).
- 이 저장소에 API 키·비밀값을 넣지 않는다.
- 끝난 종(`review.json` 있음)은 다시 만들지 않는다.
