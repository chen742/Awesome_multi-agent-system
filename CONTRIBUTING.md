# Contributing

Thanks for helping keep this list complete and up to date! 🎉

## Quick ways to contribute

1. **Open an issue** (no git needed): use the [Add a paper](../../issues/new?template=add-paper.yml) form, or the [Fix an entry](../../issues/new?template=fix-entry.yml) form for wrong links/venues.
2. **Open a pull request** — see below.

## Adding a paper via pull request

The README is **auto-generated**. Please do **not** edit `README.md` directly.

1. Add an entry to [`data/papers.yaml`](data/papers.yaml) (anywhere in the file — ordering is automatic, newest first):

   ```yaml
   - title: "Your Paper Title"
     authors: "First Author et al."
     venue: "ICLR 2026"          # conference/journal, or "arXiv 2026" for preprints
     year: 2026
     arxiv: "2601.12345"         # arXiv ID only; use `url:` instead for non-arXiv papers
     code: "https://github.com/owner/repo"   # optional
     project: "https://..."      # optional project page
     category: auto-design       # one of the ids in data/categories.yaml
     tldr: "One-sentence summary."  # optional
   ```

2. Validate and regenerate:

   ```bash
   pip install pyyaml
   python scripts/validate.py
   python scripts/build_readme.py
   ```

3. Commit both `data/papers.yaml` and `README.md`, and open a PR.

## Inclusion criteria

- The paper must be about **LLM-based multi-agent systems** (≥ 2 interacting LLM agents), or a survey / benchmark / framework directly relevant to them. Single-agent papers belong in general agent lists.
- Prefer the **arXiv abs link** or official venue page; link the **official** code repository.
- When a preprint is accepted, please update its `venue` (e.g., `arXiv 2025` → `NeurIPS 2025`).
- One entry per paper; the validator rejects duplicate arXiv IDs and titles.

## Suggesting new categories

Open an issue describing the category and a few papers that would belong to it. Categories live in [`data/categories.yaml`](data/categories.yaml).
