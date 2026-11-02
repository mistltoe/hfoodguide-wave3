"""pachyrhizus-erosus dossier.json 조립: sources.json·sections.json·data.json 을 합친다."""
import json
from pathlib import Path

W = Path(__file__).resolve().parent
src = json.loads((W / "sources.json").read_text(encoding="utf-8"))
for s in src:
    if s["n"] == 19:
        s["title"] = ("Serological and RT-PCR evaluation of African yam bean (Sphenostylis stenocarpa (Hochst ex. A. Rich) Harms) "
                      "accessions to viral resistance under field condition. Sci Rep 2024;14(1):9708. doi:10.1038/s41598-024-59977-6 (PMID 38678095)")
        s["publisher"] = "Scientific Reports (PubMed 서지)"
data = json.loads((W / "data.json").read_text(encoding="utf-8"))
d = {
    "slug": "pachyrhizus-erosus",
    "name_ko": "Jicama덩이",
    "name_en": "Jicama (yam bean, Mexican turnip)",
    "scientific_name": "Pachyrhizus erosus (L.) Urb.",
    "aliases": ["Jicama덩이뿌리", "건Jicama덩이뿌리", "jicama", "yam bean", "Mexican turnip", "히카마"],
    "sections": json.loads((W / "sections.json").read_text(encoding="utf-8")),
    "compounds": data["compounds"],
    "markers": [],
    "assays": data["assays"],
    "nutrients": data["nutrients"],
    "production": [],
    "world": [],
    "gi": [],
    "orgs": [],
    "sources": src,
}
(W.parent / "dossier.json").write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
print("written", len(d["sources"]), "sources,", len(d["compounds"]), "compounds,", len(d["assays"]), "assays")
