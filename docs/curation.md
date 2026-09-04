# Curation

## Workflow

1. **Seed.** `just seed` writes one stub per OHD term under `dental restoration material`. It never overwrites an existing file, so re-running after an OHD release only adds new terms.
2. **Curate.** Edit `kb/materials/<Name>.yaml`. Fill sections in roughly this order: composition, setting mechanisms, clinical uses, regulatory status, properties, performance, adverse effects, standards, products. Bump `curation_status` as you go.
3. **Validate.** `just validate <file>` for one file (schema and ontology terms). `just validate-references <file>` to check literature snippets. `just qc` for everything plus the tests.
4. **Render.** `just render` and `just export-browser`, then open `pages/materials/index.html` or `app/index.html`.

## Evidence rules

- Every claim that could be contested carries an `evidence` item.
- `snippet` is a verbatim quote. Do not paraphrase, do not fix typos in the source, do not merge sentences from different places.
- Literature goes in as `PMID:` where a PMID exists, else `DOI:` or `PMC:`. The reference validator fetches the abstract and checks the quote.
- Regulatory text goes in as `url:` pointing at the eCFR section, the FDA product classification record, or the 510(k) or PMA record. Quote the regulation's identification paragraph verbatim.
- Standards are cited as `url:` too, pointing at the ISO or ADA catalog entry; their text is paywalled, so keep the quote to what the catalog page shows (title and scope).
- `evidence_source` says what kind of source it is. `supports` says how it bears on the claim.

## Ontology terms

- `material_term` must be an OHD term under `OHD:0000000`. Labels are checked verbatim.
- `procedure` binds to OHD under `OHD:0000002` *dental procedure*.
- `chemical` binds to CHEBI. Look terms up with `runoak -i ols:chebi search <text>`.
- `anatomical_site` binds to UBERON.
- `effect_term` binds to HP or MONDO.
- `quality_term` binds to PATO.

`conf/oak_config.yaml` says which adapter backs each prefix. OHD uses a local SQLite build; the large ontologies go through OLS.

## Curation status

| Value | Meaning |
|---|---|
| `STUB` | Seeded from OHD only |
| `IN_PROGRESS` | Some sections filled |
| `CURATED` | All recommended sections filled with evidence |
| `REVIEWED` | Checked by a domain expert |

The tests refuse an entry that claims to be past `STUB` with no evidence anywhere in it.
