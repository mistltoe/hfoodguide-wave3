import json, glob
from pathlib import Path

W = Path(__file__).resolve().parent
have = {}
for f in glob.glob(str(W / 'meta*.json')):
    for a in json.load(open(f))['articles']:
        have[a['identifiers']['pmid']] = a

MANUAL = {
    '19348427': ('Structural analysis of fructans from Agave americana grown in South Africa for spirit production', 'J Agric Food Chem', '2009;57(10):3995-4003', None, '10.1021/jf8039389'),
    '12774633': ('[A new steroidal glycoside from fermented leaves of Agave americana]', 'Zhongguo Zhong Yao Za Zhi', '2002;27(6):431-4', None, None),
    '12765193': ('Three new hecogenin glycosides from fermented leaves of Agave americana', 'J Asian Nat Prod Res', '2003;5(2):95-103', None, '10.1080/1028602021000054946'),
    '15187383': ('Four new steroid constituents from the waste residue of fibre separation from Agave americana leaves', 'Chem Pharm Bull (Tokyo)', '2004;52(6):654-8', None, '10.1248/cpb.52.654'),
    '15979249': ('Constituents of Agave americana and Agave barbadensis', 'Fitoterapia', '2005;76(6):594-7', None, '10.1016/j.fitote.2005.04.013'),
    '17609535': ('Isolation, characterization, and localization of AgaSGNH cDNA: a new SGNH-motif plant hydrolase specific to Agave americana L. leaf epidermis', 'J Exp Bot', '2007;58(11):2717-31', None, '10.1093/jxb/erm136'),
    '11109152': ('Purpuric irritant contact dermatitis induced by Agave americana', 'Cutis', '2000;66(4):287-8', None, None),
    '17507849': ('[Purpuric contact dermatitis from Agave Americana]', 'Ann Dermatol Venereol', '2007;134(5 Pt 1):477-8', None, '10.1016/s0151-9638(07)89218-0'),
    '17182489': ('Agave (Agave americana): an evidence-based systematic review by the natural standard research collaboration', 'J Herb Pharmacother', '2006;6(2):101-22', None, None),
}

PMIDS = ['42399974', '34242333', '36079687', '37279950', '27446061', '39796424', '25811101', '33163505',
         '19348427', '23846754', '12774633', '12765193', '15187383', '35368099', '15979249', '41946797',
         '32170464', '30597061', '41600134', '34321030', '36978549', '36546733', '22797908', '17609535',
         '11109152', '17507849', '37005601', '17182489', '34043690', '27268113', '32298660']
# 2..32 ; 1 = I1020, 33 = EFSA
TITLE_FIX = {
    '36978549': 'Influence of the Season on the Nutritive Value and Gas Production of [종 이름 빠짐] and [종 이름 빠짐] L. in Ruminant Feed',
    '36079687': 'Agave americana: Characteristics and Potential Breeding Priorities',
    '37279950': 'Lessons from the history of Agave: ecological and cultural context for valuation of CAM',
    '27446061': 'Pulque, a Traditional Mexican Alcoholic Fermented Beverage: Historical, Microbiological, and Technical Aspects',
    '33163505': 'Evolution of Fructans in Aguamiel (Agave Sap) During the Plant Production Lifetime',
    '41600134': 'Spatial Patterns and Diversity of the Genus Agave in the Southern Iberian Peninsula: The Role of Anthropogenic Drivers in the Expansion of Agave americana',
        '32170464': 'Toxicity of botanical extracts and their main constituents on the bees Partamona helleri and Apis mellifera',
    '32298660': 'Metabolomic profiling of five Agave leaf taxa via UHPLC/PDA/ESI-MS in relation to their anti-inflammatory, immunomodulatory and ulceroprotective activities',
}
NOTE = {
    '33163505': ' — 제목의 Aguamiel 은 PubMed 표기에서 빠진 낱말을 채운 것; 전문(PMC)에서 종 이름 서체가 빠져 주 시료 세 그루(P1–P3)의 종은 확인하지 못함; 표 2의 10그루 중 2그루가 A. americana',
    '25811101': ' — 초록만 확인(전문 미열람)',
    '41600134': ' — 제목의 종 이름은 PubMed 표기에서 빠져 있어 초록 맥락으로 판단',
    '36978549': ' — PubMed 표기에서 제목·초록의 종 이름이 빠져 있음("Agave americana" 제목·초록 검색으로 찾음)',
    '36079687': ' — PubMed 표기에서 제목·본문의 종 이름이 빠져 있음("Agave americana" 제목·초록 검색으로 찾음)',
}

def src(n, pmid):
    if pmid in have:
        a = have[pmid]
        t = TITLE_FIX.get(pmid, a['title'].rstrip('.'))
        j = a['journal']['iso_abbreviation']
        y = a['publication_date'].get('year')
        c = a.get('citation') or {}
        cit = f"{y}" + (f";{c.get('volume')}" if c.get('volume') else '') + (f"({c['issue']})" if c.get('issue') else '') + (f":{c['pages']}" if c.get('pages') else '')
        pmc = a['identifiers'].get('pmc')
        doi = a['identifiers'].get('doi') or a.get('doi')
    else:
        t, j, cit, pmc, doi = MANUAL[pmid]
        t = t.rstrip('.')
    ids = f"PMID {pmid}" + (f", {pmc}" if pmc else '')
    url = f"https://doi.org/{doi}" if doi else f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
    return {"n": n, "title": f"{t} — {j} {cit} ({ids}){NOTE.get(pmid, '')}", "url": url, "publisher": "PubMed", "accessed": "2026-11-02"}

sources = [{"n": 1, "title": "식품의약품안전처 「식품원료 목록」(식품안전나라 OpenAPI I1020) — 용설란(Agave americana L. / Agave tequilana / Agave salmiana; Agave, Century Plant, American Aloe), 원료명 용설란분말·용설란수액·용설란시럽·용설란원액·용설란주스농축·용설란증류액, 사용가능부위: 수액, 사용가능; 같은 속의 길상천(Agave parryi)·Century plant(Agave utahensis)는 별도 항목",
            "url": "https://www.foodsafetykorea.go.kr/api/openApiInfo.do?svc_no=I1020", "publisher": "식품의약품안전처", "accessed": "2026-10-13"}]
for i, p in enumerate(PMIDS):
    sources.append(src(i + 2, p))
sources.append({"n": 33, "title": "EFSA Compendium of botanicals (식품에 쓰이는 식물 가운데 우려 물질이 보고된 종의 데이터베이스) — 데이터베이스 성격은 WebSearch 요약으로만 확인, 이 종의 항목 원문은 열람하지 못함",
                "url": "https://www.efsa.europa.eu/en/data/compendium-botanicals", "publisher": "European Food Safety Authority", "accessed": "2026-11-02"})
S = {p: i + 2 for i, p in enumerate(PMIDS)}
json.dump(sources, open(W / 'sources.json', 'w'), ensure_ascii=False, indent=1)
for s in sources:
    print(s['n'], s['title'][:110], s['url'])
