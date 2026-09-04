## Project-specific recipes, imported by the main justfile.

schema_path := "src/dentmatmech/schema/dentmatmech.yaml"
kb_dir := "kb/materials"
oak_config := "conf/oak_config.yaml"
ref_validator_config := "conf/reference_validator_config.yaml"
term_validator := "scripts/run_term_validator.sh"

# Seed one stub per OHD dental restoration material term (never overwrites)
[group('curation')]
seed *args:
    uv run dentmatmech seed {{args}}

# List materials with category and curation status
[group('curation')]
list-materials *args:
    uv run dentmatmech list {{args}}

# Schema + term validation of every material file
[group('QC')]
validate-all:
    #!/usr/bin/env bash
    set -euo pipefail
    files=({{kb_dir}}/*.yaml)
    echo "Schema validation (${#files[@]} files)..."
    uv run linkml-validate --schema {{schema_path}} --target-class DentalMaterial "${files[@]}"
    echo "Term validation..."
    {{term_validator}} validate-data "${files[@]}" -s {{schema_path}} -t DentalMaterial --labels -c {{oak_config}}
    echo "Parent links..."
    uv run dentmatmech check-links
    echo "✓ All files validated"

# Schema + term validation of one material file
[group('QC')]
validate file:
    uv run linkml-validate --schema {{schema_path}} --target-class DentalMaterial {{file}}
    {{term_validator}} validate-data {{file}} -s {{schema_path}} -t DentalMaterial --labels -c {{oak_config}}

# Validate ontology terms referenced by the schema itself (enum meanings, source nodes)
[group('QC')]
validate-terms-schema:
    {{term_validator}} validate-schema {{schema_path}} -c {{oak_config}}

# Reference validation: check evidence snippets against fetched PubMed abstracts
[group('QC')]
validate-references *files:
    uv run linkml-reference-validator validate data {{files}} --schema {{schema_path}} --target-class DentalMaterial --config {{ref_validator_config}}

# Reference validation over every material file
[group('QC')]
validate-references-all:
    uv run linkml-reference-validator validate data {{kb_dir}}/*.yaml --schema {{schema_path}} --target-class DentalMaterial --config {{ref_validator_config}}

# Full QC: validate-all plus the fast pytest suite
[group('QC')]
qc: validate-all
    uv run pytest -q

# Render every material page plus the index
[group('site')]
render:
    uv run dentmatmech render

# Render a single material page
[group('site')]
render-one file:
    uv run dentmatmech render {{file}}

# Regenerate app/data.js for the faceted browser
[group('site')]
export-browser:
    uv run dentmatmech export-browser

# Build everything the static site needs: pages, browser data, schema docs
[group('site')]
site-all: render export-browser gen-doc

# Serve the repository root so pages/ and app/ links resolve
[group('site')]
serve-pages:
    uv run python -m http.server 8765 -d .
