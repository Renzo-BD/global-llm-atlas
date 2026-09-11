# Changelog

All notable changes to **Global LLM Atlas** are documented here.

The project follows [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Planned
- Continue official-evidence review for `curator-verified` country associations.
- Re-test `LIMITED` services and normalize unstable/direct-session URLs.
- Expand geographic coverage only after the original seed is sufficiently normalized.
- Preserve lifecycle history for services that later become inactive or discontinued.

## [0.2.0] - 2026-09-10

### Added
- Canonical metadata migration for all 57 seed access points.
- Service classification, registration state, selected capability fields, operator country, duplicate relations and country-confidence metadata.
- `data/curation-v0.2.csv` semantic-curation matrix.
- `reports/curation-v0.2.0.md` evidence-backed curation report.
- Interactive filters for service type and richer metadata in the GitHub Pages UI.

### Changed
- `data/llms.json` is now the enriched v0.2.0 canonical dataset.
- `data/llms.csv` now mirrors the enriched canonical schema.
- `data/schema.json` validates the richer data model.
- The interactive atlas now distinguishes 57 access points from 56 unique services and displays `LIMITED` status explicitly.

### Findings
- 57 access points; 56 unique services; 25 country/project associations.
- 55 `ACTIVE`; 2 `LIMITED` (Kruti and IBM Granite Playground).
- The second TextCortex source URL is retained as provenance but marked as a duplicate of the German canonical access point.
- Dola, Qwen and MiniMax retain China as their seed/project association while current Singapore operating entities are recorded separately.
- Public AI's Swiss association is marked `partial`.
- Unknown capability values use `null`/blank and are never silently interpreted as unsupported.

### Scope
`MULTI MODELOS` remains excluded. No service outside the curator-provided HTML seed was added.

## [0.1.0] - 2026-09-10

### Added
- Initial curator-tested seed of 57 public conversational AI access points across 25 country sections.
- Canonical JSON dataset and CSV export.
- README directory, interactive map/search UI, JSON Schema and coverage report.
- Weekly non-authoritative URL checker and GitHub Pages workflow.
- Contribution guidance, issue templates and MIT license.

### Scope
Only access points supplied in the curator's HTML bookmark export were included. `MULTI MODELOS` was explicitly excluded.
