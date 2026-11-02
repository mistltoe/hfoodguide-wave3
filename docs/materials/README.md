# 소재 페이지 — 설계와 새 소재 추가 템플릿 (2026-10-04)

**소재**는 규제 단위인 **원료** 위의 층이다. 예를 들어 인삼이라는 소재 아래에 원료 홍삼, 인삼, 인삼다당체추출물 등이 있다.
한 페이지에서 다음을 보여 준다.

- 기원·역사·생물학적/계통적 특징
- 성분: 지표성분, 생리활성성분, 영양성분
- 유전 정보, 분포·재배지, 생산·수출
- 트렌드: 논문, 임상시험 등록, 제품 신고, 검색 관심도

화면은 `/materials`, `/materials/{slug}`, API는 `/api/v1/materials/{slug}`이다.

## 자료 세 갈래

| 갈래 | 파일 | 만드는 법 | 내용 |
|---|---|---|---|
| 조사 자료 | `<slug>/dossier.json` | AI 조사 에이전트가 공개 자료를 읽고 작성. 사람이 검토 | 설명 글 8절(문장마다 `[n]` 출처), 성분, 지표성분 기준, 영양성분, 국내·세계 생산 통계, 출처 목록 |
| 공공 DB 자동 수집 | `<slug>/auto.json` | `python docs/materials/collect_material.py <slug>` (인터넷 필요, 약 3분) | NCBI 분류 계통, GBIF 나라별 기록, NCBI 유전체 조립, PubChem 분자식·분자량, PubMed 연도별 논문 수(전체/RCT/메타), 최근 MeSH 주제, ClinicalTrials.gov 시작연도별 등록 수·대상 질환 |
| 앱 DB 계산 | 적재할 때 계산 | `scripts/load_materials.py` | 연결 원료를 쓰는 국내 품목 신고 수(연도별), 개별인정형 인정 수(연도별), 일본 특정보건용식품(FOSHU) 허가 수(연도별), 원료별 근거 등급 |
| 검색 관심도 | DB(`material_trend`, `naver:<묶음>`) | `python -m scripts.update_naver_trends` (`.env`에 NAVER 키 필요) | 네이버 데이터랩 월별 상대지수(2016-01부터 지난달까지) |

적재는 `python -m scripts.load_materials [slug]`로 한다. 다시 실행해도 된다. 소재마다 지우고 다시 넣으며, 네이버 계열은 보존한다.
스키마는 Alembic 0003(`material*` 9개 표)이다.

## 새 소재 추가 순서

1. `materials.json`에 항목을 추가한다.

   ```json
   {"slug": "garcinia", "name_ko": "가르시니아", "scientific_name": "Garcinia gummi-gutta", "kind": "plant",
    "pubmed_query": "\"Garcinia cambogia\"[tiab] OR \"Garcinia gummi-gutta\"[tiab]",
    "ctgov_term": "garcinia",
    "naver_keywords": {"가르시니아": ["가르시니아", "가르시니아캄보지아"]},
    "ingredient_patterns": ["가르시니아"], "ingredient_exclude": [","]}
   ```

   - `kind`는 plant, fungus, microbe, animal, mineral, compound 중 하나다. 식물이 아니면 GBIF·유전체 칸이 비어도 된다.
   - `pubmed_query`는 동음이의어를 피하게 쓴다. 인삼은 notoginseng을 빼는 식이다. 먼저 PubMed에서 건수를 확인한다.
   - `ingredient_patterns`는 앱 원료 이름에 들어 있으면 연결할 글자다. `ingredient_exclude`에 든 글자가 있으면 연결하지 않는다. 쉼표(`,`)가 들어간 이름은 복합 원료라서 뺀다.
2. 조사 자료 `dossier.json`을 만든다. 형식은 아래와 같고, 인삼 파일이 실례다.
   AI 에이전트에게 다음을 지시한다.
   - 공식·1차 자료를 우선한다: 식약처, 농식품부·통계청, 농진청 식품성분DB, 학술지.
   - 문장마다 `[n]`을 붙인다.
   - 확인하지 못한 값은 비워 두고 "확인하지 못함"이라 쓴다.
   - 출처끼리 다르면 둘 다 적는다.
3. `python docs/materials/collect_material.py <slug>`로 `auto.json`을 만든다. 성분 이름은 dossier에서 읽어 PubChem을 조회한다.
4. 사람이 검토한다. 특히 지표성분 기준, 1일 섭취량, 섭취 주의 문장을 출처와 대조한다.
5. 앱 폴더에서 `python -m scripts.load_materials <slug>`를 실행한다. 키가 있으면 `python -m scripts.update_naver_trends <slug>`도 실행한다.

## dossier.json 형식

```text
slug, name_ko, name_en, scientific_name, aliases[]
sections[]  : {key, title, body}   key = overview · history · biology · related_species · cultivation · processing · genetics · safety
              body 는 문단 사이 빈 줄, 문장 끝에 [n] / [n, m] / [n–m]
compounds[] : {name(영문, PubChem 조회용), name_ko, class, role(marker|bioactive|nutrient), part, content_text, activity_ko, source[]}
markers[]   : {product, marker, spec, daily_intake, functions[], note, source[]}       ← 건강기능식품 지표성분 기준
nutrients[] : {form, basis, items[{name, value, unit}], source[]}                         ← 식품성분표
production[]: {metric(area_ha|production_t|farms|export_kusd|export_t), region('대한민국'=전국 | 시도), year, value, unit, note, source[]}
world[]     : {country, metric, year, value, unit, note, source[]}
sources[]   : {n, title, url, publisher, accessed}
```

## 화면 원칙

- **설명 글은 AI 작성**이다. 페이지 맨 위에 이를 밝히고, 문장마다 출처 번호를 단다. 번호를 누르면 맨 아래 출처로 간다.
- **숫자는 원자료**다. 차트마다 "표 보기"가 있고, 출처 번호가 붙는다.
- 차트는 서버 SVG(`app/charts.py`)로 그린다. 외부 라이브러리가 없다.
- 차트 원칙:
  - 한 차트에 한 축만 쓴다.
  - 한 차트에는 한 출처(집계 기준)만 그린다. 다른 출처의 값은 차트 아래 글로 따로 보인다.
  - 빠진 해는 점선과 "자료 없음"으로 표시한다. 붙여 그리지 않는다.
  - 계열 색은 고정 순서 3색(`#2a78d6`, `#eb6834`, `#1baf7a`)으로, 색각 이상 검증을 통과했다.
  - 3번째 색은 대비가 낮다. 그래서 끝점 라벨과 표 보기를 반드시 같이 둔다.
  - 마우스를 올리면 값이 보인다(`static/charts.js`). 차트에 포커스한 뒤 ←/→ 키로도 볼 수 있다.
- 트렌드별 해석 주의:
  - 논문 수는 검색식에 좌우된다. 그래서 검색식을 화면에 적는다.
  - 품목 신고 수는 매출이 아니다. 새 제품이 나온 속도다. 올해 값은 집계 중이다.
  - 네이버 지수는 상대값(최고 달 = 100)이다. 검색 횟수가 아니다.
  - GBIF 기록은 "나는 곳"이 아니라 "기록된 곳"이다. 재배지·식물원·표본관 기록이 섞여 있다.

## 인삼 검토에서 남은 점 (조사 에이전트 보고)

- 일반 인삼(홍삼 아닌 것) 건강기능식품의 지표성분 기준을 최신 고시로 확인하지 못했다. 홍삼 기준은 확인했다.
- 세계 생산 통계는 2007–2009년 논문 값뿐이다(최신 FAO·국가 통계가 없다).
- 출처끼리 다른 값이 있다: 유전체 크기(2.98 Gb 조립 vs 3.5 Gb 추정), 수확 연수, 와파린 상호작용 강도. 본문에 둘 다 적었다.
- 2009년 수출액(논문 값)은 농식품부 통계와 기준이 달라 차트에서 뺐다.
- 2026-10-04: 위키백과 출처(1–4, 23)를 모두 빼고 NCCIH·POWO·IPNI·대한민국약전·농진청·EMA·학술 논문으로 바꿨다(출처 40–49). 확인하지 못한 문장은 지웠다: 1899년 삼정과, 1996.7.1 전매제 폐지일, 잎·꽃·열매 형태와 6년근 크기, 2020년 나라별 생산 비중. 변경 내역 `ginseng/출처교체_20261004.md`.

## 고시형 원료의 원천 소재 40종 확장 (2026-10-12)

- **대상**: 식약처 고시 제2026-43호 고시형 원료의 원천 소재 40종(인삼 포함 41종). 목록과 연결 설정은 `materials.json`.
- **고시 기준**: `<slug>/notice.json` — 고시전문에서 지표성분·1일 섭취량·기능성과 원문 줄(제조기준·규격·주의사항)을 뽑아 둔 것. markers 는 이 값을 그대로 쓴다.
  - 고시 원문 오기로 보이는 학명은 note 에 적었다(곤약 'konjq', 우뭇가사리 'amansil').
  - 알로에 전잎은 2022년 삭제, 영지버섯 자실체 추출물(2-48)은 2027-01-01 삭제로 본문에 적었다.
- **작성 → 대조 → 검사**
  1. 작성자 AI: `W_PROMPT.md` 지침으로 `dossier.json` 작성.
  2. 검토자 AI(다른 에이전트): `V_PROMPT.md` 지침으로 모든 문장·항목을 출처 원문과 대조해 고치고 `<slug>/review.json` 에 바꾼 전후를 남김.
  3. 검사 스크립트: `check_dossier.py`(형식·출처 번호·고시 지표), `check_units.py`(제품 생산액 천원 → 억 원 환산). 둘 다 0 이어야 적재한다.
- **대조 결과(40종 합계)**: 문장 2,909개·항목 2,388개 대조, 319곳 수정, 70곳 삭제, 확인하지 못한 곳 19곳. 출처 1,260개.
  - 자주 나온 수정: 출처에 없는 별명 삭제, 출처보다 세게 쓴 서술 약화, 고시 제조기준·주의사항 누락 보충, 제품 생산실적을 `production[]` 에서 가공 절 본문으로 이동(은행·헤마토코쿠스), 단위 오류(빌베리 6.1억 → 0.61억 원), 철회 논문 삭제(상황버섯).
- **남은 빈칸**(출처 접근 제한 — 국가표준식품성분표·KOSIS·FAOSTAT 가 robots/429 로 막힘, 웹 검색 한도 소진):
  - 영양성분(nutrients)이 빈 소재가 많다. 국가표준식품성분표를 PC 에서 받아 넣으면 채울 수 있다.
  - 국내 원료 작물 생산 통계는 특용작물 통계에 있는 소재(차·영지·상황·치커리 등)와 보리·귀리·토마토 등만 있다.
  - 홍국 해외직구 차단 보도자료(식약처)는 본문을 확인하지 못해 그 문장을 뺐다.
- **도우미 파일**: `<slug>/_work/`(작성자), `<slug>/_review/`(검토자, 수정 전 사본 포함)은 받아 둔 논문 전문이 들어 있어 git·릴리스에서 뺀다.
- **화면**: `/materials` 에 종류별 칩·이름 찾기·전체 색인. 상세 페이지 위쪽에 AI 대조 결과(문장 수·고친 곳 수·대조일)를 보인다.

## 식품원료 목록 전체 편입 (2026-10-13)

- **범위**: 식약처 「식품원료 목록」(식품안전나라 OpenAPI **I1020**, 24,885행) 중 식품원료(A코드)·사용가능/제한적사용·학명이 있는 생물 **5,211종**.
  - 원자료: PC `data\raw\mfds_rawmtrl\I1020_YYYYMMDD.json` (MFDS 키로 받음, git 제외).
- **두 단계**
  1. **카드 소재**(`level=card`, 5,179종): 자동. 원료명·쓸 수 있는 부위·사용 조건·상태, 생물자원 DB 연결(분류·성분 수), **지표성분 후보**(규칙: 이 종에서 보고된 성분 중 보고된 속이 적고(특이성) 보고가 많은 것, 최대 5개 — 분석 조건 없음).
  2. **상세 소재**(`level=dossier`): 글 8절 + 다른 AI 전수 대조. 웨이브로 계속 추가(`foodlist/make_wave.py` → `W2_PROMPT.md` 작성 → `V2_PROMPT.md` 대조). 대조(review.json)를 마친 것만 상세로 올라간다.
- **만드는 순서**
  1. `python docs/materials/foodlist/build_species.py data/raw/mfds_rawmtrl/I1020_….json` → `foodlist/species.json`
  2. `python docs/materials/foodlist/build_cards.py` (생물자원 DB 필요) → `foodlist/cards.json` (후보·우선순위)
  3. 앱: `alembic upgrade head`(0010) → `python -m scripts.load_materials` → `python -m scripts.load_food_materials`
- **새 표**(Alembic 0010): `material_gi`(지리적 표시, 등록 단체 = 생산자단체), `material_org`(협회·연구회), `material_assay`(지표성분과 분석 조건: official 고시·공전 / literature 논문 정량 조건 / candidate 규칙 후보). `material.level·bioresource_id·food_use·priority`.
- **우선순위**(`build_cards.py`): 고시형 원재료 +5, 특용작물 통계 +4, 한글 이름 +1, 성분 보고 수(log10), 목록의 원료 형태 수(1.5·log2: 국내에서 많이 쓰는 정도), 제한적 사용 −1. 웨이브 1 = 상위 200종(`foodlist/waves/wave_01.json`).
- **이명 연결**: 상세 소재와 목록 학명이 다를 때 `foodlist/dossier_alias.json`(예: aloe ↔ Aloe barbadensis).
- **기다리는 자료**(사용자가 `data\raw\gi\` 에 넣음): 농산물·수산물 지리적표시 등록 현황(공공데이터포털), KOSIS 농작물·임산물·어업 생산 통계(시도별), 「건강기능식품의 기준 및 규격」 제4. 시험방법·「식품의 기준 및 규격」 제8. 일반시험법(공식 분석 조건).
