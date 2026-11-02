import json, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from p1_sources import SOURCES
from p2_sec_a import SEC_A
from p3_sec_b import SEC_B
from p4_items import COMPOUNDS, ASSAYS
d = {
 "slug": "serratula-coronata", "name_ko": "산비장이", "name_en": "Mountain coronate sawwort",
 "scientific_name": "Serratula coronata L. (식품원료 목록 학명: S. coronata subsp. insularis Kitamura)",
 "aliases": ["산비장이잎", "산비쟁이", "조선마화두", "큰산나물", "Serratula coronata subsp. insularis", "Masturicum insulare"],
 "sections": SEC_A + SEC_B, "compounds": COMPOUNDS, "markers": [], "assays": ASSAYS,
 "nutrients": [], "production": [], "world": [], "gi": [], "orgs": [], "sources": SOURCES,
}
(HERE.parent / "dossier.json").write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in d["sections"]:
    print(s["key"], len(s["body"]))
