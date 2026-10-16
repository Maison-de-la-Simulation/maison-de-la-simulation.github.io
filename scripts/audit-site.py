import sys

from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urlsplit,unquote
import json,re
root=Path(__file__).resolve().parent.parent;dist=root/'dist';base=sys.argv[1] if len(sys.argv)>1 else '/'
base='/'+base.strip('/')+'/' if base.strip('/') else '/'
errors=[];anchors=[];duplicates=[];external_media=[];allids={};docs={}
for f in dist.rglob('*.html'):
 s=BeautifulSoup(f.read_text(),'html.parser');docs[f]=s;ids=[a['id'] for a in s.select('[id]')];allids[f]=set(ids)
 if len(ids)!=len(set(ids)):duplicates.append((str(f),sorted({i for i in ids if ids.count(i)>1})))
for f,s in docs.items():
 for a in s.find_all(True):
  for k in ['href','src','poster','action','data']:
   u=a.get(k,'')
   if not isinstance(u,str) or not u:continue
   sp=urlsplit(u)
   if sp.hostname in ['mdls.fr','www.mdls.fr','maisondelasimulation.fr','www.maisondelasimulation.fr']:errors.append((str(f),'OLD DOMAIN',u));continue
   if k=='src' and sp.scheme in ['http','https'] and a.name in ['img','video','source']:external_media.append((str(f),u))
   if u.startswith('#'):
    if len(u)>1 and unquote(u[1:]) not in allids[f]:anchors.append((str(f),u))
   elif u.startswith('/') and not u.startswith('//'):
    path=unquote(sp.path)
    if not path.startswith(base):errors.append((str(f),'BASE',u));continue
    target=dist/path[len(base):]
    if target.is_dir():target=target/'index.html'
    if not target.exists():errors.append((str(f),'MISSING',u));continue
    if sp.fragment and target in allids and unquote(sp.fragment) not in allids[target]:anchors.append((str(f),u))
 for a in s.select('[style]'):
  if re.search(r'https?://(?:www\.)?(?:mdls.fr|maisondelasimulation.fr)',a['style']):errors.append((str(f),'REMOTE BG',a['style']))
# Check that all source routes exist (homepage full content is retained on laboratoire).
pages=json.load(open(root/'src/data/pages.json'));missingroutes=[]
for page in pages:
 path=page['path'].strip('/');target=dist/path/'index.html' if path else dist/'index.html'
 if not target.exists():missingroutes.append(page['path'])
# Compare every public API document's body text, without obsolete migration notice and dynamic form labels.
api=json.load(open(root/'migration/wordpress-pages.json'))+json.load(open(root/'migration/wordpress-posts.json'))
coverage=[]
def norm(s):return re.sub(r'\W+','',s,flags=re.UNICODE).lower()
for item in api:
 sp=urlsplit(item['link']);path='/'+unquote(sp.path).strip('/')+'/' if sp.path.strip('/') else '/';page=next(p for p in pages if p['path']==path);s=BeautifulSoup(item['content']['rendered'],'html.parser')
 for e in s.select('script,style,form,.forminator-guttenberg'):e.decompose()
 if path=='/':
  for e in list(s.select('.wp-block-group')):
   if e.find_parent(class_='wp-block-group') is None and 'Our new website' in e.get_text(' ',strip=True):e.decompose()
 original=norm(s.get_text(' ',strip=True));new=norm(BeautifulSoup(page['html'],'html.parser').get_text(' ',strip=True));ok=original==new
 coverage.append(dict(path=path,text_preserved=ok,source_characters=len(original),migrated_characters=len(new)))
print(json.dumps(dict(base=base,html_pages=len(docs),source_routes=len(pages),assets=len(json.load(open(root/'migration/asset-map.json'))),broken=errors,broken_anchors=anchors,duplicate_ids=duplicates,remote_media=external_media,missing_source_routes=missingroutes,text_coverage=coverage),ensure_ascii=False,indent=2))
report=dict(base=base,html_pages=len(docs),source_routes=len(pages),assets=len(json.load(open(root/'migration/asset-map.json'))),broken=errors,broken_anchors=anchors,duplicate_ids=duplicates,remote_media=external_media,missing_source_routes=missingroutes,text_coverage=coverage)
(root/'migration'/('audit-root.json' if base=='/' else 'audit-subpath.json')).write_text(json.dumps(report,ensure_ascii=False,indent=2))
if errors or anchors or duplicates or missingroutes or external_media or any(not x['text_preserved'] for x in coverage):sys.exit(1)
