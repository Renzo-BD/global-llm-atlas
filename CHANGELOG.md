# Changelog

All notable changes to **Global LLM Atlas** are documented here.

## [0.2.0] - 2026-09-10

### Added
- Deep-curation matrix for all 57 seed access points: service type, registration, selected capabilities, operator country, confidence and duplicate relations.
- `reports/curation-v0.2.0.md` with methodology and evidence-backed findings.

### Findings
- 57 access points; 56 unique services; 25 country/project associations.
- 55 `ACTIVE`; 2 `LIMITED` (Kruti and IBM Granite Playground).
- The second TextCortex seed URL is identified as a duplicate; official company information associates TextCortex with Germany.
- Dola, Qwen and MiniMax retain their seed/project association with China while current Singapore operating entities are recorded separately.
- Public AI's Swiss association is marked partial because the platform is global/multi-model.
- Unknown capability values remain blank/unverified rather than being inferred as unsupported.

### Scope
`MULTI MODELOS` remains excluded. The canonical v0.1.0 JSON is intentionally preserved while the richer v0.2.0 metadata is reviewed in `data/curation-v0.2.csv`; canonical-schema migration is the next release step.

## [0.1.0] - 2026-09-10

### Added
- Initial curator-tested seed of 57 public conversational AI access points across 25 country sections.
- Canonical JSON dataset and CSV export.
- README directory, interactive map/search UI, JSON Schema and coverage report.
- Weekly non-authoritative URL checker and GitHub Pages workflow.
- Contribution guidance, issue templates and MIT license.

### Scope
Only access points supplied in the curator's HTML bookmark export were included. `MULTI MODELOS` was explicitly excluded.
