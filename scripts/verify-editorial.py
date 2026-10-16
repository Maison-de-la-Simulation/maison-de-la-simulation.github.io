import sys
from pathlib import Path
import json,re
from bs4 import BeautifulSoup
from urllib.parse import unquote,urlsplit
root=Path(__file__).resolve().parent.parent
base=sys.argv[1] if len(sys.argv)>1 else '/'
base='/'+base.strip('/')+'/' if base.strip('/') else '/'
expected=[('Laboratory','laboratory/'),('Research','science-of-computing/'),('Expertise','science-by-computing/'),('Training','training/'),('Software','software/'),('Members','members/')]
htmls=list((root/'dist').rglob('*.html'))
for file in htmls:
 soup=BeautifulSoup(file.read_text(),'html.parser')
 assert soup.html.get('lang')=='en',file
 nav=soup.find(id='navigation');assert nav,file
 entries=[(a.get_text(' ',strip=True),unquote(a.get('href',''))) for a in nav.find_all('a')][:6]
 assert entries==[(name,base+path) for name,path in expected],(file,entries)
home=BeautifulSoup((root/'dist/index.html').read_text(),'html.parser')
partners=json.load(open(root/'src/data/partners.json'))
expected_ids={'polytechnique','sorbonne','tgcc','idris','cines','inria','cerfacs','cc-fr','riken','juelich','doe'}
assert {p['id'] for p in partners}==expected_ids
assert {a['data-partner'] for a in home.select('.partner-logo-card')}==expected_ids
assert len(home.select('.partner-logo-card'))==len(expected_ids)
assert len(home.select('.header-tutelles img'))==4
for p in partners:assert (root/'public'/p['image']).is_file(),p
film=home.select_one('figure.hero-film');assert film and film.find('video') and 'Credit: Francesco Massimo' in film.get_text(' ',strip=True)
# Preserve every directory entry, including names with accents and external thesis links.
raw=json.load(open(root/'src/data/pages.json'));source=BeautifulSoup(next(p['html'] for p in raw if p['path']=='/members/'),'html.parser')
def norm(s):return re.sub(r'\W+','',s,flags=re.UNICODE).lower()
names=[]
for li in source.select('li'):
 name=re.sub(r'\([^)]*\)','',li.get_text(' ',strip=True)).replace('Team Leader:','').strip()
 if name:names.append(name)
rendered=BeautifulSoup((root/'dist/members/index.html').read_text(),'html.parser').select_one('main').get_text(' ',strip=True)
missing=[name for name in names if norm(name) not in norm(rendered)];assert not missing,missing
directory=BeautifulSoup((root/'dist/members/index.html').read_text(),'html.parser')
member_names=directory.select('.member-name')
assert len(member_names)==142,len(member_names)
assert all(n.find('a',href=True) and n.find('a')['href'].strip() for n in member_names)
expertise=BeautifulSoup((root/'dist/science-by-computing/index.html').read_text(),'html.parser')
leader=expertise.select_one('#team a[href="'+base+'member/charles-prouveur/"]')
assert leader and leader.get_text(' ',strip=True)=='Charles Prouveur'
assert 'Team leader:' in leader.parent.get_text(' ',strip=True)
assert not home.select('.news-strip')
assert not any(re.search(r'seminars?|séminaire|featured',a.get_text(' ',strip=True),re.I) for a in home.find_all('a'))
# Catch residual French interface wording while allowing original proper names and postal addresses.
fr=re.compile(r'\b(?:avec|pour|notre|votre|recherche|équipe|accueil|données|une|nous|vous|sont|scientifiques|réseau|orateur|thèse|cette|prêt|consulter|générales|télécharger)\b',re.I)
residual=[];seen=set()
for file in htmls:
 soup=BeautifulSoup(file.read_text(),'html.parser')
 for el in soup.select('style,script'):el.decompose()
 for text in soup.stripped_strings:
  if text in seen:continue
  seen.add(text)
  if fr.search(text):residual.append({'page':str(file.relative_to(root/'dist')),'text':text})
assert not residual,residual
report={'language':'en','html_pages_checked':len(htmls),'source_routes':len(raw),'navigation':expected,'partner_logos':[p['name'] for p in partners],'directory_entries_checked':len(names),'linked_directory_entries':len(member_names),'missing_directory_names':missing,'sbc_team_leader':'Charles Prouveur','homepage_featured_event_removed':True,'video_credit':'Francesco Massimo','residual_french_interface_text':residual,'base':base}
(root/'migration'/('english-verification.json' if base=='/' else 'english-verification-subpath.json')).write_text(json.dumps(report,ensure_ascii=False,indent=2));print(json.dumps(report,ensure_ascii=False,indent=2))
