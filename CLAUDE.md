# CLAUDE.md

Guidance for Claude Code when working in this repository.

## What this is

The **Dental Materials Knowledge Base (dentmatmech)**: a LinkML-based knowledge base of dental restoration materials, modeled on [DisMech](https://github.com/monarch-initiative/dismech). It combines:

1. A LinkML schema (`src/dentmatmech/schema/dentmatmech.yaml`)
2. One YAML file per material in `kb/materials/`, each bound to one OHD term under `OHD:0000000`
3. Rendered pages (`pages/materials/`) and a faceted browser (`app/`)

Read `docs/explanation/design-decisions.md` before changing scope, the ontology set, or the evidence policy.

## Commands

```bash
just install                     # uv sync --group dev
just seed                        # stub every OHD material term (never overwrites)
just validate kb/materials/X.yaml   # schema + ontology terms for one file
just validate-all                # every file: schema + terms + parent links
just validate-references kb/materials/X.yaml   # snippet check against PubMed
just qc                          # validate-all + pytest
just render                      # pages/materials/*.html
just export-browser              # app/data.js
just gen-python                  # regenerate src/dentmatmech/datamodel after a schema edit
uv run pytest -q
```

## Curation rules

- **One OHD term per file.** `material_term.term.label` must match OHD exactly. Put friendlier names in `preferred_term` and `synonyms`.
- **`parents` are names of other files.** They mirror OHD's `is_a` links. Tests fail on a dangling parent.
- **Snippets are verbatim quotes.** Never paraphrase. Literature snippets are machine-checked against PubMed abstracts.
- **Regulatory text is quoted from the regulation.** Cite as `url:` to the eCFR section or FDA database record. Verified regulation numbers, classes, and product codes are tabulated in `docs/regulatory.md`; do not guess a product code or a regulation number from memory. Look it up:
  - CFR text: `https://www.law.cornell.edu/cfr/text/21/872.NNNN` (eCFR itself blocks automated fetches)
  - Product codes: `https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpcd/classification.cfm?start_search=1&regulationnumber=872.NNNN`
- **Device type vs product.** Classification of the material as a device type goes in `regulatory_status`. A specific brand's 510(k) goes in `products[].submissions`.
- **Ontology lookups** use OAK: `uv run runoak -i sqlite:obo:ohd search <text>` for OHD, `ols:chebi`, `ols:uberon`, `ols:hp`, `ols:pato` for the rest.
- **Bump `curation_status`** as sections fill in. Anything past `STUB` must carry evidence.
- After a schema change: `just gen-python`, then `uv run pytest -q`, then `just validate-all`.

## Layout

```
kb/materials/            knowledge base (source of truth)
src/dentmatmech/schema/  LinkML schema
src/dentmatmech/seed.py  OHD -> stub files
src/dentmatmech/cli.py   `dentmatmech` CLI (seed, list, render, export-browser, check-links)
src/dentmatmech/render.py + templates/   HTML pages
src/dentmatmech/export.py                app/data.js
conf/oak_config.yaml     prefix -> OAK adapter
conf/reference_validator_config.yaml
tests/                   schema conformance + KB consistency + render smoke tests
docs/                    mkdocs narrative + generated schema docs
```
