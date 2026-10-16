import sys
from pathlib import Path
import json, re
from bs4 import BeautifulSoup
from urllib.parse import unquote, urlsplit

root = Path(__file__).resolve().parent.parent
base = sys.argv[1] if len(sys.argv) > 1 else "/"
base = "/" + base.strip("/") + "/" if base.strip("/") else "/"
expected = [
    ("Laboratory", "laboratory/"),
    ("Research", "science-of-computing/"),
    ("Expertise", "science-by-computing/"),
    ("Training", "training/"),
    ("Software", "software/"),
    ("Members", "members/"),
]
htmls = list((root / "dist").rglob("*.html"))
for file in htmls:
    soup = BeautifulSoup(file.read_text(), "html.parser")
    assert soup.html.get("lang") == "en", file
    nav = soup.find(id="navigation")
    assert nav, file
    entries = [
        (a.get_text(" ", strip=True), unquote(a.get("href", ""))) for a in nav.find_all("a")
    ][:6]
    assert entries == [(name, base + path) for name, path in expected], (file, entries)
home = BeautifulSoup((root / "dist/index.html").read_text(), "html.parser")
partners = json.load(open(root / "src/data/partners.json"))
expected_ids = {
    "polytechnique",
    "sorbonne",
    "tgcc",
    "idris",
    "cines",
    "inria",
    "cerfacs",
    "cc-fr",
    "riken",
    "juelich",
    "doe",
}
assert {p["id"] for p in partners} == expected_ids
assert {a["data-partner"] for a in home.select(".partner-logo-card")} == expected_ids
assert len(home.select(".partner-logo-card")) == len(expected_ids)
assert len(home.select(".header-tutelles img")) == 4
for p in partners:
    assert (root / "public" / p["image"]).is_file(), p
film = home.select_one("figure.hero-film")
assert film and film.find("video") and "Credit: Francesco Massimo" in film.get_text(" ", strip=True)
# The structured member data drives names, links and automatic group counts.
raw = json.load(open(root / "migration/legacy-content/pages.json"))
people = json.load(open(root / "src/data/members.json"))


def norm(s):
    return re.sub(r"\W+", "", s, flags=re.UNICODE).lower()


names = [person["name"] for person in people]
directory = BeautifulSoup((root / "dist/members/index.html").read_text(), "html.parser")
member_names = directory.select(".member-name")
assert [n.get_text(" ", strip=True) for n in member_names] == names
assert len(member_names) == len(people)
missing = []
for node, person in zip(member_names, people):
    anchor = node.find("a", href=True)
    assert anchor, person["name"]
    url = person.get("url") or "/member/" + person["id"] + "/"
    target = url if url.startswith(("https://", "http://")) else base + url.lstrip("/")
    assert anchor["href"] == target, (person["name"], anchor["href"], target)
expertise = BeautifulSoup(
    (root / "dist/science-by-computing/index.html").read_text(), "html.parser"
)
leader = expertise.select_one('#team a[href="' + base + 'member/charles-prouveur/"]')
assert leader and leader.get_text(" ", strip=True) == "Charles Prouveur"
assert "Team leader:" in leader.parent.get_text(" ", strip=True)
event_path = "/de-lassistance-a-lautonomie-limpact-de-lia-agentique-sur-les-processus-de-recherche/"
featured = home.select_one(".news-strip a")
assert featured and featured["href"] == base + event_path.lstrip("/")
assert "agentic AI in research" in featured.get_text(" ", strip=True)
event = BeautifulSoup(
    (root / "dist" / event_path.strip("/") / "index.html").read_text(), "html.parser"
)
assert event.select_one("main table")
assert event.select_one('time[datetime="2026-12-03"]')
assert event.select_one('a[href="' + base + 'media/programme-detaille-8baeea757b.pdf"]')
assert not any(
    re.search(r"seminars?|séminaire|featured", a.get_text(" ", strip=True), re.I)
    for a in home.find_all("a")
)
# Catch residual French interface wording while allowing original proper names and postal addresses.
fr = re.compile(
    r"\b(?:avec|pour|notre|votre|recherche|équipe|accueil|données|une|nous|vous|sont|scientifiques|réseau|orateur|thèse|cette|prêt|consulter|générales|télécharger)\b",
    re.I,
)
residual = []
seen = set()
for file in htmls:
    soup = BeautifulSoup(file.read_text(), "html.parser")
    for el in soup.select("style,script"):
        el.decompose()
    for text in soup.stripped_strings:
        if text in seen:
            continue
        seen.add(text)
        if fr.search(text):
            residual.append({"page": str(file.relative_to(root / "dist")), "text": text})
assert not residual, residual
report = {
    "language": "en",
    "html_pages_checked": len(htmls),
    "source_routes": len(raw),
    "navigation": expected,
    "partner_logos": [p["name"] for p in partners],
    "directory_entries_checked": len(names),
    "linked_directory_entries": len(member_names),
    "missing_directory_names": missing,
    "sbc_team_leader": "Charles Prouveur",
    "featured_workshop": event_path,
    "video_credit": "Francesco Massimo",
    "residual_french_interface_text": residual,
    "base": base,
}
(
    root
    / "migration"
    / ("english-verification.json" if base == "/" else "english-verification-subpath.json")
).write_text(json.dumps(report, ensure_ascii=False, indent=2))
print(json.dumps(report, ensure_ascii=False, indent=2))
