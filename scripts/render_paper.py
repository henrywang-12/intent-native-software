"""Build the standalone reading edition. Install Markdown==3.7."""
from pathlib import Path
import html, re
import markdown
from assemble_paper import manuscript, ROOT

def reading_edition():
    body=markdown.markdown(manuscript(),extensions=['tables','toc','fenced_code'])
    # Inline local SVG figures so the edition can be shared as one file.
    def embed(match):
        name=match.group(1)
        svg=(ROOT/'paper/figures'/name).read_text()
        svg=re.sub(r'<\?xml.*?\?>','',svg,flags=re.S)
        svg=re.sub(r'<!DOCTYPE.*?\]>','',svg,flags=re.S)
        svg=re.sub(r'<!DOCTYPE[^>]*>','',svg)
        prefix=name.replace('.svg','')+'-'
        ids=re.findall(r'\bid="([^"]+)"',svg)
        for ident in sorted(ids,key=len,reverse=True):
            svg=svg.replace('id="'+ident+'"','id="'+prefix+ident+'"')
            svg=svg.replace('href="#'+ident+'"','href="#'+prefix+ident+'"')
            svg=svg.replace('url(#'+ident+')','url(#'+prefix+ident+')')
        svg=re.sub(r'aria-labelledby="([^"]+)"',lambda m:'aria-labelledby="'+' '.join(prefix+x for x in m.group(1).split())+'"',svg)
        return '<figure>'+svg+'</figure>'
    body=re.sub(r'<img[^>]*src="figures/([^"/]+\.svg)"[^>]*/?>',embed,body)
    body=body.replace('<p><figure>','<figure>').replace('</figure></p>','</figure>')
    # Research links target the public repository when the single file is shared.
    body=re.sub(r'href="\.\./([^"#]+)"',r'href="https://github.com/henrywang-12/intent-native-software/blob/main/\1"',body)
    headings=re.findall(r'<h1 id="([^"]+)">(.*?)</h1>',body)
    nav=''.join(f'<a href="#{ident}">{label}</a>' for ident,label in headings)
    style=(ROOT/'paper/style.css').read_text()
    return '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="A working paper on humans, AI agents, dependable delegation and software marketplaces."><title>The Internet of Delegated Action</title><style>'+style+'</style></head><body><a class="skip" href="#manuscript">Skip to paper</a><aside><div class="brand">INTENT-NATIVE SOFTWARE</div><nav aria-label="Chapters">'+nav+'</nav></aside><main id="manuscript"><div class="eyebrow">WORKING PAPER / 2026</div>'+body+'<footer>AI-assisted working paper. Read the methods and evidence boundaries before reusing claims.</footer></main></body></html>\n'

if __name__=='__main__':
    (ROOT/'paper/index.html').write_text(reading_edition())
