import json, re, sys
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "dossier.json"
ACC = "2026-11-02"
I1020_URL = "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020"
def pm(pmid, title, journal, year, extra=""):
    return dict(title=f"{title} ({journal}, {year}; PMID {pmid}){extra}", url=f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/", publisher=f"{journal} (PubMed)", accessed=ACC)
S = [
 ("I1020", dict(title="식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 주름버섯(Agaricus campestris L. ex Fr.) (로컬 원자료 I1020_20261013.json 대조)", url=I1020_URL, publisher="식품의약품안전처", accessed="2026-10-13")),
 ("I1020g", dict(title="식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 같은 속 항목: 양송이버섯(A. bisporus)·신령주름버섯자실체(A. blazei)·흰주름버섯(A. arvensis)·여름양송이자실체(A. bitorquis)·붉은갓주름버섯자실체(A. subrufescens)·실비듬주름버섯(A. augustus, 사용불가)·주름버섯아재비(A. placomyces, 사용불가) (로컬 원자료 대조)", url=I1020_URL, publisher="식품의약품안전처", accessed="2026-10-13")),
 ("stats", dict(title="통계청 「농작물생산조사」·농림축산식품부 「특용작물 생산실적」(1995–2024) 로컬 파싱본(docs/stats/regional_crops.csv·special_crops_annual.csv·special_crops_2024.csv) — '주름버섯' 품목 없음 확인(양송이만 있음)", url="https://www.mafra.go.kr", publisher="농림축산식품부·통계청", accessed=ACC)),
 ("glam", pm("25954776","A comparative study on edible Agaricus mushrooms as functional foods (초록)","Food & Function","2015")),
 ("sci25", pm("40603525","Optimization of biological activities of Agaricus species: an artificial intelligence-assisted approach (PMC12222538 전문)","Scientific Reports","2025")),
 ("mahd", pm("29248113","A phylogenetic and morphological overview of sections Bohusia, Sanguinolenti, and allied sections within Agaricus subg. Pseudochitonia (초록)","Fungal Biology","2017")),
 ("thong", pm("25152000","Morphological and molecular characterization of three Agaricus species from tropical Asia reveals a new group in section Xanthodermatei (초록)","Mycologia","2014")),
 ("tibet", pm("41807986","Microbial interactions mediate the fairy ring type effects on alpine meadow plant communities on the Tibetan plateau (초록)","Environmental Microbiome","2026")),
 ("barn", pm("10466232","Radiocaesium activity concentrations in the fruit-bodies of macrofungi in Great Britain and an assessment of dietary intake habits (초록)","Science of the Total Environment","1999")),
 ("alon", pm("24597704","The cultural significance of wild mushrooms in San Mateo Huexoyucan, Tlaxcala, Mexico (초록)","Journal of Ethnobiology and Ethnomedicine","2014")),
 ("quin", pm("25230891","Knowledge and use of edible mushrooms in two municipalities of the Sierra Tarahumara, Chihuahua, Mexico (초록)","Journal of Ethnobiology and Ethnomedicine","2014")),
 ("ndif", pm("37560888","Mushroom-related ethnomycological, ethnomedical, and socio-economic practices in Nigeria (초록)","International Journal of Medicinal Mushrooms","2023")),
 ("gray", pm("9659289","Insulin-releasing and insulin-like activity of Agaricus campestris (mushroom) (초록)","Journal of Endocrinology","1998")),
 ("eyer", pm("14724774","[The development of a toxic megacolon due to Amanita phalloides poisoning. A rare complication] (초록, 독일어 논문)","Deutsche Medizinische Wochenschrift","2004")),
 ("gram", pm("17647209","Microbial competition, lack in macronutrients, and acidity as main obstacles to the transfer of basidiomycetous ground fungi into soils (초록)","Journal of Basic Microbiology","2007")),
 ("hild", pm("23454218","Agaricus bisporus and related Agaricus species on lignocellulose: production of manganese peroxidase and multicopper oxidases (초록)","Fungal Genetics and Biology","2013")),
 ("stau", pm("24970179","Pyranose dehydrogenase from Agaricus campestris and Agaricus xanthoderma: characterization and applications in carbohydrate conversions (PMC4030953 전문)","Biomolecules","2013")),
 ("may", pm("6962735","Genetic variation and joint segregation of biochemical loci in the common meadow mushroom, Agaricus campestris (초록)","Biochemical Genetics","1982")),
 ("vogel", pm("5892569","Structural and functional characteristics of deoxyribonucleic acid-rich mitochondria of the common meadow mushroom, Agaricus campestris. I. (서지 정보만 확인, 초록 없음)","Laboratory Investigation","1965")),
 ("gall", pm("139970","[The mitochondria of higher mushrooms: the cytochromes b of the mitochondria of Agaricus campestris (F.) var. bisporus] (영문 초록)","C R Seances Soc Biol Fil","1976")),
 ("moli", pm("14098148","[Studies on Beauveria tenella (NRRL 2334, 2335, 2336; previously Agaricus campestris). III.] (서지 정보만 확인)","Archiv für Mikrobiologie","1963")),
 ("mart", pm("16346818","Growth of Agaricus campestris NRRL 2334 in the form of pellets (초록)","Applied and Environmental Microbiology","1985")),
 ("nova", pm("7197579","The cell walls of Agaricus bisporus and Agaricus campestris fruiting body hyphae (초록)","Canadian Journal of Microbiology","1981")),
 ("ewart", pm("1098948","Effect of lectins on hormone release from isolated rat islets of Langerhans (초록)","Diabetes","1975")),
 ("jenn", pm("9914511","Novel glycoinositolphosphosphingolipids, basidiolipids, from Agaricus (초록)","European Journal of Biochemistry","1999")),
 ("cro17", pm("28121267","Lead, cadmium and mercury contents and bioaccumulation potential of wild edible saprophytic and ectomycorrhizal mushrooms, Croatia (초록)","J Environ Sci Health B","2017")),
 ("cro16", pm("27272918","Heavy metal bioaccumulation by wild edible saprophytic and ectomycorrhizal mushrooms (초록)","Environmental Science and Pollution Research","2016")),
 ("tur21", pm("33982259","Element concentration, daily intake of elements, and health risk indices of wild mushrooms collected from Belgrad Forest and Ilgaz Mountain National Park (Turkey) (초록)","Environmental Science and Pollution Research","2021")),
 ("lead", pm("19217716","Lead in edible mushrooms: levels and bioaccumulation factors (초록)","Journal of Hazardous Materials","2009")),
 ("chrom", pm("23643799","Bioconcentration of chromium in edible mushrooms: influence of environmental and genetic factors (초록)","Food and Chemical Toxicology","2013")),
 ("silv", pm("7975911","Silver content of wild-grown mushrooms from northern Poland (초록)","Z Lebensm Unters Forsch","1994")),
 ("laub", pm("562042","[Cadmium uptake by mushrooms] (영문 초록)","Z Lebensm Unters Forsch","1977")),
 ("arsb", pm("28007169","Uptake and transformation of arsenic during the reproductive life stage of Agaricus bisporus and Agaricus campestris (초록)","Journal of Environmental Sciences","2017")),
 ("sel", pm("18781538","Selenium in edible mushrooms (총설, 초록)","J Environ Sci Health C","2008")),
 ("agar", pm("6120025","Agaridoxin: a fungal catecholamine which acts as an alpha 1 agonist of mammalian hypothalamic adenylate cyclase (초록)","Brain Research","1982")),
 ("ota", pm("38440684","Ochratoxin A biodegradation by Agaricus campestris and statistical optimization of cultural variables (PMC10908693 전문)","Food Science and Biotechnology","2024")),
 ("sant", pm("4037433","The significance of the spores of the Basidiomycetes in bronchial asthma and allergic rhinitis (초록)","Annals of Allergy","1985")),
 ("bolu", pm("36734918","Phenolic content, antibacterial and antioxidant potential of several edible Agaricomycetes mushrooms sold in public bazaar in Bolu, Turkey (초록)","International Journal of Medicinal Mushrooms","2023")),
 ("elba", pm("26082986","Medicinal mushroom extracts possess differential antioxidant activity and cytotoxicity to cancer cells (초록)","International Journal of Medicinal Mushrooms","2015")),
]
NUM = {k: i+1 for i, (k, _) in enumerate(S)}
def R(text):
    def rep(m):
        ks = [x.strip() for x in m.group(1).split(",")]
        return "[" + ", ".join(str(NUM[k]) for k in ks) + "]"
    return re.sub(r"\{([a-zA-Z0-9_, ]+)\}", rep, text)

secs = json.loads(Path(__file__).with_name("sections.json").read_text(encoding="utf-8"))
sections = [dict(key=s["key"], title=s["title"], body=R(s["body"])) for s in secs]
comp = json.loads(Path(__file__).with_name("compounds.json").read_text(encoding="utf-8"))
for c in comp:
    for f in ("content_text","activity_ko"):
        c[f] = R(c[f])
    c["source"] = [NUM[k] for k in c["source"]]
assays = json.loads(Path(__file__).with_name("assays.json").read_text(encoding="utf-8"))
for a in assays:
    for f in ("content","rationale"):
        a[f] = R(a[f])
    a["source"] = [NUM[k] for k in a["source"]]
d = dict(slug="agaricus-campestris", name_ko="주름버섯", name_en="Meadow mushroom",
         scientific_name="Agaricus campestris L. ex Fr.",
         aliases=["Agaricus campestris", "meadow mushroom", "common meadow mushroom"],
         sections=sections, compounds=comp, markers=[], assays=assays, nutrients=[],
         production=[], world=[], gi=[], orgs=[],
         sources=[dict(n=NUM[k], **v) for k, v in S])
OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
for s in sections: print(s["key"], len(s["body"]))
print("sources", len(S), "compounds", len(comp), "assays", len(assays))
