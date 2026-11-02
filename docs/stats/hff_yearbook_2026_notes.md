# HFF tables from 2026 식품의약품통계연보 (제28호): extraction notes

Source: MFDS, published July 2026, ISSN 1975-6011. The PDF page index equals the printed page number + 2.
Script: `/tmp/claude-0/yb/build.py <pdftotext file>`. It writes `hff_yearbook_2026.json`.
Regular tables were parsed from the pdftotext layout. Tables 2, 3 and 7 have multi-line cells, so their values were typed in from the page images. For table 7, the script also asserts that every amount appears in the text.

| key | table | printed p. (PDF p.) | rows | visual check |
|---|---|---|---|---|
| import_by_year | 3-2-1-3 | 204–205 (206–207) | 11 (2015–2025) | p.204 checked |
| import_top_countries | 3-2-2-6 | 214 (216) | 60 (5 yrs × total+subtotal+10) | checked |
| import_top_items | 3-2-3-6 | 224–225 (226–227) | 60 | both pages checked |
| adverse_events | 4-3-13 | 309 (311) | 16 (2010–2025) | checked |
| firms_by_type | 4-1-2 | 267 (269) | 16 (2010–2025) | checked |
| sales_by_item | 4-2-7 | 284–285 (286–287) | 85 = 11 year totals + 74 items (2025) | both pages checked |
| top20_items | 4-2-10 | 288 (290) | 42 (2 yrs × total+20) | checked |
| import_inspection | 3-3-1-6 | 245 (247) | 14 (2012–2025) | checked |

## Validation (267 checks pass)
- **3-2-1-3:** each total equals the sum of the 6 regional offices, within ±1 (rounding) for 2015, 2018, 2020, 2022, 2023 and 2025.
- **3-2-2-6 / 3-2-3-6:** the top-10 subtotals equal the sum of the ranks. Item subtotals are within ±1 for 2021–2024. The yearly 총계 matches the 3-2-1-3 amount. For 2021 and 2022 it is printed 1 lower (1,098,762 vs 1,098,763 and 1,161,944 vs 1,161,945). The rank-1 share recomputes correctly.
- **4-3-13:** total equals 소비자 신고 + 영업자 보고 for every year.
- **4-1-2:** each subtotal equals the sum of its parts, and the total equals 제조업 소계 + 판매업 소계 + 맞춤형 for every year.
- **4-2-7:** 소계 equals 국내판매액 + 수출액(천원) (±1 for 2018 and 2021). The sum of the 74 items for 2025 equals the 2025 total (±1 on 소계 and on 수출 천원), so the item list is complete.
- **4-2-10:** the printed 총계 equals the exact sum of the top 20 items. Every 2025 value matches the 2025 item row in 4-2-7.
- **3-3-1-6:** total equals 적합 + 부적합. 적합 and 부적합 each equal the sum of the four inspection types.

## Ambiguities / caveats
1. **3-3-1-6 vs 3-2-1-3, 2019 case count:** inspection gives 13,104 and imports give 13,102. Both values are kept as printed. All other years match.
2. **3-2-1-3:** only the year rows were extracted (national total plus a `by_regional_office` breakdown for 서울, 부산, 경인, 대구, 광주 and 대전). The 2025 per-item rows on pp.204–207 were not extracted. Weight is in **tonnes** (단위: 건, 톤, 천 달러).
3. **4-1-2:**
   - No 수입업 column is printed. The footnote says import businesses were merged into 수입식품 등 수입판매업 from 2016.
   - The 맞춤형건강기능식품판매업 column is blank, not '-', for 2010–2024. It is stored as null; only 2025 has a value (705).
   - The 2025 breakdown by 시도 was not extracted.
4. **4-2-7:** item rows exist **only for 2025**; 2015–2024 are totals only. Values are in 천 원, except `export_usd`, which is in dollars (not thousands). Exchange rate footnote: 1 USD = 1,421.97 KRW (Dec 2025). Rows printed as '-' are null.
5. **4-2-10:** "총계" is the top-20 sum (3,897,448,758 in 2025), not total sales (4,090,967,394). Name variants: 4-2-10 uses "개별인정형", "쏘팔메토 열매추출물" and "뮤코다당ㆍ단백"; 4-2-7 uses "개별인정제품", "쏘팔메토 열매 추출물" and "뮤코다당·단백".
6. **3-2-3-6 item names:** these are import categories ("복합영양소제품", "영양소기능성복합제품", "개별인정형건강기능식품"), not the 4-2-7 sales categories. The 2025 영양소기능성복합제품 value (145,948) equals 3-2-1-3's "영양소 및 기능성원료혼합" row.
7. In 4-3-13 the EN header for 영업자 보고 reads "Reports by Health Supplement Association". It is stored as `business_operator_reports`.
