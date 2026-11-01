# Reading and rebuilding the paper

- [Complete manuscript](PAPER.md)
- [Standalone reading edition](index.html) — download and open in a browser; use Print for a paginated copy.
- [Evidence and research companion](../research/README.md)

From the repository root, `python3 scripts/assemble_paper.py` rebuilds the Markdown with no dependencies. Install `Markdown==3.7` to run `python3 scripts/render_paper.py`. Install `matplotlib==3.9.2` only to regenerate the two plots with `python3 research/figures/reliability.py` and `python3 research/figures/marketplace.py`. The analytical models themselves require no packages.

The HTML is a committed reading artifact, not a deployed website. It contains no external scripts, fonts, analytics or networked demo. Chapters are canonical; regenerate the assembled editions after editing them. The three architecture diagrams are conceptual SVGs; the two plots are synthetic sensitivity analyses.
