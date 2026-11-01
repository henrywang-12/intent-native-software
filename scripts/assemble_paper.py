"""Build the canonical manuscript from chapters; standard library only."""
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[1]
HEADER="""# The Internet of Delegated Action

## Humans, AI agents and the economics of intent-native software

**Harry Henry Hanrui Wang · Founder, Walify**

**Working paper · 1 November 2026 · AI-assisted research and writing**

### Abstract

As AI systems become better at planning and using tools, software can increasingly accept goals rather than only sequences of interface operations. This paper argues that dependable delegation requires a shared substrate of persistent state, explicit authority, semantic contracts and evidence of effects. It examines human-agent coexistence, integrated ecosystems in China and the United States, open model economics and the conditions under which an intent marketplace could acquire durable power. The argument is conditional: integration may reduce coordination failures, while portability, multihoming and specialization may prevent market tipping. Walify is presented through its author-stated vision of software for people and agents; the independently inspectable implementation is a local execution demo. Five analytical sensitivity models, twenty proposed protocols and ten dated forecasts expose the assumptions and missing evidence. No live comparative benchmark, adoption result or monopoly forecast is claimed as established fact.

**Reading guide:** Chapters 1–7 define the architecture; 8–11 compare ecosystem mechanisms; 12–20 examine models, economics and governance; 21–25 connect the vision to testable next steps.

**Evidence:** [Methods](../research/METHODS.md) · [Research companion](../research/README.md) · [Public demo](../demo/README.md)

"""

FIGURES={1:('architecture','Proposed shared software environment'),4:('authority','Permission and commitment boundaries'),5:('reliability','Illustrative independent-step reliability; not measured performance'),17:('marketplace','Unestimated participation model; not market shares or welfare'),21:('vision','Author-stated Walify vision and public implementation boundary')}

def manuscript():
    chapters=sorted((ROOT/'paper/chapters').glob('*.md'))
    if len(chapters)!=25:
        raise ValueError('expected 25 complete chapters')
    parts=[HEADER]
    for number,path in enumerate(chapters,1):
        parts.append(path.read_text().rstrip()+'\n')
        if number in FIGURES:
            slug,caption=FIGURES[number]
            parts.append(f'![{caption}](figures/{slug}.svg)\n\n*Figure: {caption}.*\n')
    parts.append('# References and source notes\n')
    for source in json.loads((ROOT/'research/sources.json').read_text()):
        note=f"../research/evidence/{source['id'].lower()}-{source['slug']}.md"
        parts.append(f"- **{source['id']}** {source['author']}. {source['title']}. {source['date']}. [{source['kind']}]({source['url']}); [evidence boundary]({note}).")
    parts.append('\nSee the research companion for unexecuted protocols and unresolved forecasts. The author has a commercial interest in the thesis. This working paper is not peer reviewed.')
    return '\n'.join(parts)+'\n'

if __name__=='__main__':
    (ROOT/'paper/PAPER.md').write_text(manuscript())
