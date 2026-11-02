A = "2026-11-02"
def pm(pmid, title, journal, year, doi=None, pmc=None):
    url = f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
    t = f"{title} {journal} {year}. PMID {pmid}" + (f", {pmc}" if pmc else "") + (f", doi:{doi}" if doi else "")
    return {"title": t, "url": url, "publisher": f"{journal} (PubMed)", "accessed": A}

SRC = [
 {"title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 산비장이잎(Serratula coronata L. subsp. insularis Kitamura)·한라산비장이잎·Saw-wort잎·국화수리취잎 행",
  "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"},
 pm("32899750", "Separation and HPLC Characterization of Active Natural Steroids in a Standardized Extract from the Serratula coronata Herb with Antiseborrheic Dermatitis Activity.", "Int J Environ Res Public Health", 2020, "10.3390/ijerph17186453", "PMC7557367"),
 pm("37687297", "Effect of Plant Extracts Combinations on TNF-α, IL-6 and IL-10 Levels in Serum of Rats Exposed to Acute and Chronic Stress.", "Plants (Basel)", 2023, "10.3390/plants12173049", "PMC10490550"),
 pm("37692348", "Adsorption isotherms and kinetics for Pb(II) ion removal from aqueous solutions with biogenic metal oxide nanoparticles (Serratula coronata 추출물 이용).", "RSC Adv", 2023, "10.1039/d3ra05347d", "PMC10483273"),
 pm("10389301", "[Components of Serratula species; screening for ecdysteroid and inorganic constituents of some Serratula plants] (헝가리어, 영문 초록).", "Acta Pharm Hung", 1999),
 pm("12035548", "Phytoecdysteroids: biological effects, application in agriculture and complementary medicine.", "Ukr Biokhim Zh", 2001),
 pm("11755058", "Phytoecdysteroids from the juice of Serratula coronata L. (Asteraceae).", "Insect Biochem Mol Biol", 2002, "10.1016/s0965-1748(01)00106-0"),
 pm("15030920", "Monitoring the antioxidant activity of extracts originated from various Serratula species and isolation of flavonoids from Serratula coronata.", "Fitoterapia", 2004, "10.1016/j.fitote.2003.12.009"),
 pm("39979015", "Quercetin-3-Methyl Ether Induces Early Apoptosis to Overcome HRV1B Immune Evasion, Suppress Viral Replication, and Mitigate Inflammatory Pathogenesis.", "Biomol Ther (Seoul)", 2025, "10.4062/biomolther.2024.204", "PMC11893485"),
 pm("33878320", "Proapoptotic and proautophagic activity of 20-hydroxyecdysone in breast cancer cells in vitro.", "Chem Biol Interact", 2021, "10.1016/j.cbi.2021.109479"),
 pm("25059064", "[Phytoecdysteroids influence on the hormonal status and apoptosis in growing rats] (러시아어, 영문 초록).", "Vopr Pitan", 2014),
 pm("26402944", "[Condition of protective intestinal microbiota populations under stress exposure in rats received different diets with bioactive food components] (러시아어, 영문 초록).", "Vopr Pitan", 2015),
 pm("9505354", "[Effect of vitamin D3 and 20-hydroxyecdysone on the content of ATP, creatine phosphate, carnosine and Ca2+ in skeletal muscles] (러시아어, 영문 초록).", "Ukr Biokhim Zh", 1997),
 pm("22533708", "Influence of plant polyphenols and medicinal plant extracts on antibiotic susceptibility of Escherichia coli.", "J Appl Microbiol", 2012, "10.1111/j.1365-2672.2012.05322.x"),
 pm("35684408", "Phytoecdysteroids from Serratula coronata L. for Psoriatic Skincare.", "Molecules", 2022, "10.3390/molecules27113471", "PMC9181847"),
 pm("1488818", "[A comparative analysis of the proteins from a cell culture and from field plants of the ecdysteroid producer Serratula coronata L.] (러시아어, 영문 초록).", "Ukr Biokhim Zh", 1992),
 pm("21033376", "[Lignins of Rhodiola rosea and Serratula coronata: peculiarities of chemical structure and antioxidant properties] (러시아어, 영문 초록).", "Adv Gerontol", 2010),
 pm("31811978", "Phytoecdisteroids from Serratula coronata when growing ducklings.", "Res Vet Sci", 2019, "10.1016/j.rvsc.2019.11.012"),
 pm("41305960", "Synthesis and cytotoxic activity of triphenylphosphonium salts of ecdysteroids, lithocholic acid and cholesterol.", "Nat Prod Res", 2025, "10.1080/14786419.2025.2592114"),
 pm("29668446", "Antidepressant Effect and Recognition Memory Improvement of Two Novel Plant Extract Combinations - Antistress I and Anti-stress II on Rats Subjected to a Model of Mild Chronic Stress.", "Folia Med (Plovdiv)", 2018, "10.1515/folmed-2017-0073"),
 pm("17226485", "New Ecdysteroids from Serratula tinctoria.", "Planta Med", 1992, "10.1055/s-2006-961485"),
 pm("22645442", "Novel ecdysteroids from Serratula wolffii.", "ScientificWorldJournal", 2012, "10.1100/2012/651275", "PMC3354479"),
 pm("41588341", "Comparative chloroplast genomics of Cardueae (Carduoideae, Asteraceae): the first tribe-wide analysis.", "BMC Plant Biol", 2026, "10.1186/s12870-026-08217-2", "PMC12918578"),
 pm("23948259", "Sesquiterpenoids in subtribe Centaureinae (Cass.) Dumort (tribe Cardueae, Asteraceae): distribution, 13C NMR spectral data and biological properties.", "Phytochemistry", 2013, "10.1016/j.phytochem.2013.07.002"),
 pm("12451496", "Identification and determination of ecdysones and flavonoids in Serratula strangulata by micellar electrokinetic capillary chromatography.", "Planta Med", 2002, "10.1055/s-2002-35658"),
 pm("36095459", "A new species of Acaudinum Börner (Hemiptera; Aphididae; Aphidinae) from Kazakhstan.", "Zootaxa", 2022, "10.11646/zootaxa.5183.1.7"),
 pm("19537334", "[Influence of ecdysteron-80 on the hormonal-mediator balance and lipid metabolism in rats with chronic cardiac failure] (러시아어, 영문 초록).", "Patol Fiziol Eksp Ter", 2009),
 pm("26491384", "Study of phylogenetic relationship of Turkish species of Klasea (Asteraceae) based on ISSR amplification.", "PhytoKeys", 2015, "10.3897/phytokeys.56.5608", "PMC4611746"),
 pm("9548888", "Isolation and Structural Elucidation of Two Plant Ecdysteroids, Gerardiasterone and 22-Epi-20-hydroxyecdysone (Serratula tinctoria).", "J Nat Prod", 1998, "10.1021/np970124y"),
]
SOURCES = [dict(n=i + 1, **s) for i, s in enumerate(SRC)]
