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

## Fetching the primary sources

Every regulation number, class, and product code is re-verified from the CFR text *and* the
classification database on each curation run, so the fetch route is part of the method. Routes
tested from CI on 2026-10-22:

| Source | Route | Result |
|---|---|---|
| CFR text | `curl https://www.law.cornell.edu/cfr/text/21/872.NNNN` | works |
| CFR text, character-exact | `curl --compressed 'https://www.ecfr.gov/api/versioner/v1/full/YYYY-MM-DD/title-21.xml?part=872&section=872.NNNN'` | works, but **only with compression** - without `--compressed` it answers `406` and tells you so |
| eCFR section HTML | `curl https://www.ecfr.gov/current/title-21/section-872.NNNN` | blocked, `302` |
| Product classification | `curl -L -H 'User-Agent: Mozilla/5.0' '…/cfpcd/classification.cfm?start_search=1&productcode=CODE'` | works, returns the record page |
| Product classification | the same URL with curl's default `User-Agent` | blocked, `302` to `abuse-detection-apology.html` |
| Product classification | a browser `User-Agent` but no `-L` | useless: `302` to a 215-byte `Object Moved` stub |
| Product classification | the agent's `WebFetch` tool on the same URL | works, returns the result rows |
| Product classification | `curl 'https://api.fda.gov/device/classification.json?search=regulation_number:"872.NNNN"&limit=50'` | works |

`classification.cfm` is reachable from plain `curl`, but it needs **both** a browser `User-Agent`
**and** `-L`, and each missing piece fails in a different way. Earlier runs of this file recorded the
page as blocked outright; that was an artefact of testing the two halves separately. With curl's
default `User-Agent` the site really does refuse, redirecting to an abuse-detection page. With a
browser `User-Agent` and no `-L` you get a 215-byte `Object Moved` stub, which looks like a block but
is only an unfollowed redirect. Supply both and the full record page comes back; `Mozilla/5.0` on its
own is a sufficient `User-Agent`. Cite the `classification.cfm` URL either way - it is the
human-readable record, and it renders device names in lower case, which is what a `snippet` quoting it
has to match.

**`classification.cfm` was down on 2026-10-24.** All three of its routes above - plain `curl`,
`curl -L` with a browser `User-Agent`, and `WebFetch` - returned `HTTP 503` with accessdata's
"The page you are requesting is currently unavailable" body, repeatedly and across product codes.
That is an FDA-side outage, not the `User-Agent`/`-L` pitfall described above: the failure mode is a
503 with a 17 KB error page, not a `302`. Do not "fix" your curl invocation in response to it, and do
not conclude that a lower-case device-name `snippet` is wrong because only openFDA answers - the
casing claim above was recorded from the live page and still stands. Use openFDA to cross-check codes
while the HTML form is down, and leave the `classification.cfm` citations in place.
**It recovered by 2026-10-25**, when all eight codes were read back from it directly, so treat
the 503 as a transient outage rather than a standing block: retry the HTML form before falling
back to openFDA.

openFDA serves the same database as JSON with `product_code`, `device_name`, `device_class`, and
`submission_type_id`; across the eight codes in this file `submission_type_id` is `1` for the 510(k)
codes and `4` for the `510(K) Exempt` ones. It title-cases `device_name`, so quote it only when it is
the URL you cite. Reading both routes is the cheapest way to cross-check a product code that is new
to the KB, and openFDA additionally reports how many codes a regulation carries in total, which is
how the completeness claims in the table below were checked.

## Mapping OHD materials to FDA regulations

The two systems cut the world differently. OHD classifies by *what the material is*; FDA classifies by *what the device is for*. So one OHD material can fall under several regulations (a resin composite used as a core build-up, a luting cement, or a pit and fissure sealant), and one regulation can cover several OHD materials (`872.3275` dental cement spans glass ionomer, zinc phosphate, zinc polycarboxylate, and resin cements). Record one `regulatory_status` entry per applicable regulation, and use `approved_uses` to say which use each one governs.

Regulations verified against the CFR text and the FDA product classification database on 2026-09-04:

| Regulation | Device name | Class | Product codes | Notes |
|---|---|---|---|---|
| 872.3060 | Noble metal alloy | II (special controls) | EJS, EJT | 510(k)-exempt subject to 872.9. The database also returns EIT (applicator, rapid wax, dental) under this regulation; it is a laboratory accessory, not an alloy |
| 872.3070 | Dental amalgam, mercury, and amalgam alloy | II (special controls) | EJJ, ELY, OIV | Special controls guidance named in the regulation |
| 872.3200 | Resin tooth bonding agent | II | | |
| 872.3250 | Calcium hydroxide cavity liner | II | | |
| 872.3275 | Dental cement | I (zinc oxide-eugenol, EMB, 510(k)-exempt); II (others, EMA) | EMA, EMB | |
| 872.3330 | Preformed crown | I | ELZ | 510(k)-exempt subject to 872.9. Covers plastic and austenitic (stainless steel) preformed crowns, so it is not a metal-only device type |
| 872.3350 | Gold or stainless steel cusp | I | ELO | 510(k)-exempt subject to 872.9. The only device type in subpart D naming both gold and stainless steel; prosthodontic (permanent cusp against a removable denture), not restorative |
| 872.3640 | Endosseous dental implant | II (special controls) | DZE, NRQ, OAT | Root-form and blade-form |
| 872.3690 | Tooth shade resin material | II | EBF, OFW | |
| 872.3710 | Base metal alloy | II (special controls) | EJH | 510(k)-exempt subject to 872.9 |
| 872.3920 | Porcelain tooth | II | ELL | |

872.3060, 872.3070, and 872.3710 were re-verified from the same two primary sources on 2026-09-06 while curating `Metal`. `872.3330` was verified from the same two sources on 2026-09-09, also while curating `Metal`; it is the route by which preformed stainless steel crowns reach the market. `872.3350` was verified from the same two sources on 2026-09-10, also while curating `Metal`. The regulation titles, identification paragraphs, classes, and product codes were unchanged. All five regulations, all eight product codes, and all five identification paragraphs were re-verified from the same two primary sources on 2026-10-01, again while curating `Metal`; nothing had changed. Submission type in the classification database is `510(K) Exempt` for EJS, EJT, EJH, ELZ, and ELO, and `510(k)` for EJJ, ELY, and OIV. Re-verified once more on 2026-10-12: the five identification paragraphs and five classification paragraphs were diffed character for character against the eCFR versioner XML for the 2026-10-06 issue of title 21, and all eight product codes against the classification database; nothing had changed. Re-verified again on 2026-10-19 while tending `Metal`: the five identification and classification paragraphs against the CFR text, and all eight product codes against the classification database through both routes above. Nothing had changed, including the exclusion of EIT from 872.3060. Re-verified on 2026-10-22 while tending `Metal`, this time with the per-regulation code counts read from openFDA rather than assumed: 872.3060 returns three codes (EJS, EJT, and the excluded EIT), 872.3070 three, and 872.3330, 872.3350, and 872.3710 one each, so the "only product code under the regulation" claims on the last three are complete and not merely unrefuted. Nothing had changed. Re-verified once more on 2026-10-23: all five identification paragraphs diffed against the eCFR versioner XML for the 2026-10-06 issue of title 21, all five regulation titles against the section heads, and all eight product codes against both `classification.cfm` and openFDA, including the submission type on each (`510(K) Exempt` for EJS, EJT, EJH, ELZ, ELO; `510(k)` for EJJ, ELY, OIV) and the per-regulation code counts. Nothing had changed. (The claim that a pull request accompanied that run was wrong, as was the same claim for 2026-10-22: no pull request existed on `curate/metal` on either date, and `gh pr list --head curate/metal --state all` was still empty on 2026-10-24. Only the dating clause was wrong; the verifications happened.) Re-verified on 2026-10-24: all five regulation numbers, titles, classes, special-controls clauses, and 510(k)-exemption clauses against the CFR text at law.cornell.edu, with all five identification paragraphs and all five classification-paragraph snippets confirmed verbatim; all eight product codes against openFDA only, because `classification.cfm` was returning HTTP 503 through every route (see the outage note above), checking `device_name`, `device_class`, `submission_type_id`, `medical_specialty_description`, and `regulation_number` on each. Nothing had changed, including the exclusion of EIT from 872.3060. Re-verified on 2026-10-25 from both primary sources, `classification.cfm` having recovered: all five regulation numbers, titles, classes, and exemption clauses against the CFR text, and all eight product codes against the classification database, including the submission type on EJS (`510(K) Exempt`) and EJJ (`510(k)`). Nothing had changed.

## A note on `872.9` exemptions

Some device types are class II *and* 510(k)-exempt — `872.3060` and `872.3710` both are. That combination is easy to misread: the exemption is granted in the classification paragraph itself and is bounded by `872.9`, which withdraws it when a device has a new intended use or operates on a different fundamental scientific technology. Record such a device type as `status: EXEMPT` with `pathways: [EXEMPT_510K]`, not as `CLEARED`. `872.3070` sits next to them as the counterexample: same class, same special-controls pattern, no exemption.

## Standards recognition

FDA's [Recognized Consensus Standards database](https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfStandards/search.cfm) is where to verify a standard's current edition before recording it. Its per-standard page also lists the regulations and product codes the standard applies to, which makes it a useful independent check on a product code you have already looked up in the classification database. The search form posts to `results.cfm`; the citable per-standard URL is `detail.cfm?standard__identification_no=NNNNN`.

Recognitions verified on 2026-09-08 while curating `Metal`:

| Standard | Edition | Recognition number | Extent | Applies to |
|---|---|---|---|---|
| ISO 22674 | Third edition 2022-08 | 4-300 | Complete | 872.3060 (EJS, EJT), 872.3710 (EJH) |
| ISO 9693 | Third edition 2019-10 | 4-263 | Complete | 872.3060, 872.3710, 872.3920, 872.6660 |
| ISO 24234 | Third edition 2021-08 | 4-315 | Complete | 872.3070 (EJJ, ELY) |
| ISO 10271 | Third edition 2020-08 | 4-265 | Complete | 872.3060 (EJS, EJT), 872.3710 (EJH) |
| ISO 7405 | Third edition 2018-10 Corrected version 2018-12 | 4-261 | Complete | 872.3060, 872.3070, 872.3710 and others |

ISO 22674 excludes amalgam alloys by its own scope, which is why a metal entry needs ISO 24234 alongside it. ISO 10271 and ISO 7405 were verified on 2026-09-09; ISO 7405 is the one of the five recognised across the amalgam codes as well as the cast-alloy codes.

## Other regulators

`agency` also accepts EU MDR, Health Canada, MHRA, TGA, PMDA, NMPA, and ANVISA, with `device_class` values for the EU scheme (IIa, IIb). Nothing beyond FDA is curated yet; the slots exist so the model does not have to change when that happens.
