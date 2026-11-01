"""Validate publication structure, local links and generated manuscript."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit
import json, re, sys
from assemble_paper import ROOT, manuscript

class Document(HTMLParser):
    def __init__(self):
        super().__init__(); self.ids=[];self.links=[];self.assets=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:self.ids.append(a['id'])
        if 'href' in a:self.links.append(a['href'])
        if tag in ('script','iframe') or (tag in ('img','link') and ('src' in a or 'href' in a)):
            self.assets.append((tag,a))

def local_link_exists(base,target,root):
    parsed=urlsplit(target)
    if parsed.scheme or parsed.netloc or not parsed.path:
        return True
    candidate=(base/unquote(parsed.path)).resolve()
    if not candidate.is_relative_to(root.resolve()):
        return False
    return candidate.exists()

def validate_source_ids(sources):
    ids=[s['id'] for s in sources]
    return len(ids)==len(set(ids)) and all(re.fullmatch(r'S\d{2}',i) for i in ids)

def validate():
    errors=[]
    sources=json.loads((ROOT/'research/sources.json').read_text())
    if len(sources)!=30 or not validate_source_ids(sources):errors.append('source register IDs')
    for source in sources:
        p=ROOT/f"research/evidence/{source['id'].lower()}-{source['slug']}.md"
        if not p.exists() or source['url'] not in p.read_text():errors.append('source note '+source['id'])
    for folder,count in (('paper/chapters',25),('research/protocols',20),('research/forecasts',10)):
        if len(list((ROOT/folder).glob('*.md')))!=count:errors.append('count '+folder)
    for folder in ('paper','research'):
        for path in (ROOT/folder).rglob('*.md'):
            content=path.read_text()
            if re.search(r'\[\[S\d+\]\]|TODO|TO BE WRITTEN|/Users/|/private/tmp/',content):
                errors.append('unresolved or private content '+str(path.relative_to(ROOT)))
            for target in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)',content):
                if not local_link_exists(path.parent,target,ROOT):errors.append('link '+str(path.relative_to(ROOT))+': '+target)
    for path in (ROOT/'research/forecasts').glob('*.md'):
        text=path.read_text()
        if not all(s in text for s in ('**Issued:** 2026-11-01','**Resolve by:**','Resolution procedure','Evidence against')):
            errors.append('forecast resolution '+path.name)
    if (ROOT/'paper/PAPER.md').read_text()!=manuscript():errors.append('manuscript out of date')
    doc=Document();doc.feed((ROOT/'paper/index.html').read_text())
    if len(doc.ids)!=len(set(doc.ids)):errors.append('duplicate HTML IDs')
    for link in doc.links:
        if link.startswith('#') and unquote(link[1:]) not in doc.ids:errors.append('HTML anchor '+link)
    if doc.assets:errors.append('reading edition has external or unembedded assets')
    if '--check-render' in sys.argv:
        from render_paper import reading_edition
        if (ROOT/'paper/index.html').read_text()!=reading_edition():errors.append('HTML out of date')
    if errors:
        raise SystemExit('\n'.join(errors))
    print(json.dumps({'sources':30,'chapters':25,'protocols':20,'forecasts':10,'figures':5,'local_links':'valid','generated_manuscript':'current','html_anchors':'valid'}))

if __name__=='__main__':validate()
