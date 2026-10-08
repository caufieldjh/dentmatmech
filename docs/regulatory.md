# Regulatory status

The question this section answers for each material: *what is it approved for, and by whom?*

## How FDA regulates dental materials

FDA regulates dental materials as medical devices through the Center for Devices and Radiological Health. Dental devices are classified in [21 CFR part 872](https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-872); restorative and prosthetic materials sit in subpart D, *Prosthetic Devices*. Each section (for example `872.3690`, tooth shade resin material) gives an *identification* paragraph describing the device type and its intended use, and a *classification* paragraph assigning a risk class.

- **Class I**: general controls. Often exempt from premarket notification.
- **Class II**: general and special controls. Usually reaches market through a 510(k) premarket notification showing substantial equivalence to a predicate; some class II dental materials are 510(k)-exempt subject to the limits of `872.9`.
- **Class III**: premarket approval (PMA).

Each regulation maps to one or more three-letter **product codes** in FDA's [Product Classification database](https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfPCD/classification.cfm). A product code is what individual 510(k) records carry, so it is the join key between a device type and the products cleared under it.

## Two levels in the model

**`regulatory_status`** is the device-type level. One entry per agency and regulation:

```yaml
regulatory_status:
- agency: FDA
  status: CLEARED                    # what standing the device type has
  regulation_number: '872.3690'      # section of 21 CFR 872
  regulation_title: Tooth shade resin material
  device_class: CLASS_II
  product_codes: [EBF, OFW]
  pathways: [PREMARKET_NOTIFICATION_510K]
  special_controls: []               # guidance documents named in the regulation
  identification: >-                 # paragraph (a), quoted verbatim
    Tooth shade resin material is a device composed of materials such as
    bisphenol-A glycidyl methacrylate (Bis-GMA) intended to restore carious
    lesions or structural defects in teeth.
  approved_uses:                     # what the regulation permits
  - name: Restoration of carious lesions or structural defects in teeth
    use_context: DIRECT_RESTORATION
  restrictions: []                   # population or labeling limits
  source_url: https://www.ecfr.gov/current/title-21/section-872.3690
  evidence: []
```

**`products`** is the product level. A branded product and its submissions:

```yaml
products:
- name: Filtek Supreme Ultra
  manufacturer: 3M ESPE
  submissions:
  - agency: FDA
    submission_number: K093412
    pathway: PREMARKET_NOTIFICATION_510K
    decision: CLEARED
    decision_date: '2010-01-22'
    product_code: EBF
    regulation_number: '872.3690'
    indications_for_use: >-
      (quoted from the 510(k) summary)
    source_url: https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm?ID=K093412
```

The product example above is illustrative; check the record before curating it.

## Mapping OHD materials to FDA regulations

The two systems cut the world differently. OHD classifies by *what the material is*; FDA classifies by *what the device is for*. So one OHD material can fall under several regulations (a resin composite used as a core build-up, a luting cement, or a pit and fissure sealant), and one regulation can cover several OHD materials (`872.3275` dental cement spans glass ionomer, zinc phosphate, zinc polycarboxylate, and resin cements). Record one `regulatory_status` entry per applicable regulation, and use `approved_uses` to say which use each one governs.

Regulations verified against the CFR text and the FDA product classification database on 2026-09-04:

| Regulation | Device name | Class | Product codes | Notes |
|---|---|---|---|---|
| 872.3060 | Noble metal alloy | II (special controls) | EJS, EJT | 510(k)-exempt subject to 872.9 |
| 872.3070 | Dental amalgam, mercury, and amalgam alloy | II (special controls) | EJJ, ELY, OIV | Special controls guidance named in the regulation |
| 872.3200 | Resin tooth bonding agent | II | | |
| 872.3250 | Calcium hydroxide cavity liner | II | | |
| 872.3275 | Dental cement | I (zinc oxide-eugenol, EMB, 510(k)-exempt); II (others, EMA) | EMA, EMB, MZW, NEA | Re-verified 2026-09-05. MZW (dental cement w/out zinc-oxide eugenol as an ulcer covering, class II) and NEA (cement, ear, nose and throat, class II) also sit under this regulation but are not dental restorative uses |
| 872.3640 | Endosseous dental implant | II (special controls) | DZE, NRQ, OAT | Root-form and blade-form |
| 872.3690 | Tooth shade resin material | II | EBF, OFW | |
| 872.3710 | Base metal alloy | II (special controls) | EJH | 510(k)-exempt subject to 872.9 |
| 872.3920 | Porcelain tooth | II | ELL | |

## FDA performance criteria for dental cements

FDA's final guidance *Dental Cements - Performance Criteria for Safety and Performance Based Pathway* (September 2024, docket FDA-2024-D-4171) gives performance criteria that a 510(k) may use in place of a direct predicate comparison. It applies to class II dental cements under `872.3275` (EMA), `872.3200` (KLE) and `872.3750` (DYH), and explicitly excludes `872.3275` EMB and MZW, `872.3690` (EBF, OFW) and `872.3250` (EJK). Its criteria are drawn from ISO 9917-1 and ISO 9917-2, so it is a convenient, citable source for class-level values (film thickness, net setting time, compressive strength, acid erosion) when the ISO text itself is not to hand.

The guidance scopes each test item separately, and **not all items have the same scope**, so a class-level entry cannot apply one blanket caveat to all of them. Verified against the guidance PDF on 2026-10-06:

| Test item | Scope as the guidance marks it | Reaches resin-modified members? |
|---|---|---|
| 3. Film thickness | "as applicable, luting cements only" | Yes — scoped by application, cites both parts |
| 4. Net setting time | *no restriction* | Yes — Table 2 has a fourth, resin-modified row |
| 5. Compressive strength | "as applicable, powder/liquid acid-base cements only" | No |
| 6. Acid erosion | "as applicable, powder/liquid acid-base cements only" | No |
| 7. Working time | "as applicable, resin-modified cements only" | Resin-modified only |
| 8. Flexural strength | "as applicable, resin-modified cements only" | Resin-modified only |

Items 3 and 4 name "ISO 9917-1 **or** ISO 9917-2" as methodology, so their `test_method` should name both parts. Table 2's resin-modified row reads `tsetting ≤ 8 min` / `tsetting ≤ 6 min` — an upper bound with no lower bound, unlike the three powder/liquid rows. Quote Table 2 complete; a range such as `1.5-8 min` is the envelope of the stated limits, and its lower end is not a class-wide minimum.

Editions of a standard should be checked against FDA's [Recognized Consensus Standards database](https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfStandards/search.cfm), which is fetchable; the ISO catalogue blocks automated retrieval.

### Fetching the primary sources

All three forms below were re-confirmed working on 2026-10-08. **The `User-Agent` requirement is
per-host, and for one host it is inverted** — there is no single header set that fetches all three.
Sending a desktop `User-Agent` everywhere breaks the guidance PDFs; sending none breaks the FDA
databases. Both failures look the same: an `apology_objects/abuse-detection-apology.html` page,
served with a `404`, that reads like *the record does not exist* rather than like *you were blocked*.

- **CFR section text.** The eCFR versioner API returns the authoritative XML and **does not block
  automated fetches**, contrary to the note in `CLAUDE.md`. It is indifferent to the `User-Agent`
  (both forms returned `200` on 2026-10-08) but it does require that you accept compression, failing
  `406` with `supportCode 11` if you do not:

  ```bash
  curl -sL --compressed \
    "https://www.ecfr.gov/api/versioner/v1/full/<YYYY-MM-DD>/title-21.xml?section=872.NNNN&part=872"
  ```

  Prefer it over the law.cornell.edu mirror when quoting verbatim. The mirror's `<I>` tags render as stray spaces in most HTML-to-text converters, which silently corrupts a snippet into `eugenol —(1) Identification .` where the regulation reads `eugenol—(1) Identification.`
- **Product codes** (`accessdata.fda.gov`) **need a desktop `User-Agent`**; without one, both URL
  forms return the apology page. Earlier notes blamed the `start_search=1&regulationnumber=` form
  itself for being throttled. That was wrong, and it was the missing header: on 2026-10-08 both
  forms returned real records first try with `-A "$UA"`, and both returned the apology page without
  it. Prefer whichever answers the question:

  ```bash
  # one record, by code
  curl -sL --compressed -A "$UA" \
    "https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpcd/classification.cfm?id=<CODE>"
  # every code under one regulation -- use this to justify which codes an entry omits
  curl -sL --compressed -A "$UA" \
    "https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpcd/classification.cfm?start_search=1&regulationnumber=872.NNNN"
  ```
- **Guidance PDFs** (`fda.gov/media/<id>/download`) **must be fetched with no `-A` at all.** This is
  the inverted case: curl's default `User-Agent` returned the PDF (`200`, 541 kB) on 3 of 3 tries,
  while the desktop `User-Agent` that the databases require returned the apology page on 3 of 3.
  `WebFetch` also works but is not needed, and a summary is not evidence — extract the text and
  match the quote:

  ```bash
  curl -sL --compressed "https://www.fda.gov/media/<id>/download" -o guidance.pdf
  uv run python -c "import pypdf; print('\n'.join(p.extract_text() for p in pypdf.PdfReader('guidance.pdf').pages))"
  ```

  Find `<id>` on the guidance's landing page. Before matching, strip the page furniture: the running
  footer `Contains Nonbinding Recommendations` and a bare page number interleave with the body text
  across page breaks, so a quote spanning a page break fails a naive substring check while being
  perfectly verbatim.

## Other regulators

`agency` also accepts EU MDR, Health Canada, MHRA, TGA, PMDA, NMPA, and ANVISA, with `device_class` values for the EU scheme (IIa, IIb). Nothing beyond FDA is curated yet; the slots exist so the model does not have to change when that happens.
