# Changelog

All notable changes to **Global LLM Atlas** are documented here.

The project follows [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Planned
- Continue official-evidence review for country associations and Android availability.
- Re-test `LIMITED` and `INACTIVE` services and normalize unstable URLs.
- Continue systematic country expansion.

## [0.3.0] - 2026-10-02

### Added
- 8 verified public conversational AI access points: Chat Got, Wrtn, ILMUchat, HUMAIN Chat, Lovable, Hostinger AI Builder, Base44 and Zapia.
- 8 new country/project associations: Egypt, South Korea, Malaysia, Saudi Arabia, Sweden, Lithuania, Israel and Uruguay.
- Six newly verified official Android apps: Wrtn, ILMUchat, HUMAIN Chat, Lovable, Base44 and Zapia.
- `reports/curation-v0.3.0.md` and `reports/android-curation-2026-10-02.md`.

### Changed
- Canonical dataset version is now `0.3.0`: 65 access points, 64 unique services and 33 country/project associations.
- Lifecycle totals are 62 `ACTIVE`, 2 `LIMITED` and 1 `INACTIVE`.
- Android metadata version is now `0.2.0`, with 31 unique native/regional Android services plus 1 unique PWA service.
- The former Hostinger Horizons staging candidate is normalized to **Hostinger AI Builder** and remains `LIMITED` because current free access is time/credit-limited.
- Main map includes coordinates for all newly represented countries.

### Curation notes
- South Africa's Moja remains deferred because current evidence establishes WhatsApp access but not an independent qualifying browser chat.
- Portugal's IAChat, Ukraine's Mamay AI Chat and Sweden's AIbott remain deferred pending stronger evidence for the project's English/Spanish usability criterion.

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
- The second TextCortex source URL is retained as provenance but marked as a duplicate of the German canonical access point.
- Dola, Qwen and MiniMax retain China as their seed/project association while current Singapore operating entities are recorded separately.
- Public AI's Swiss association is marked `partial`.
- Unknown capability values use `null`/blank and are never silently interpreted as unsupported.

## [0.1.0] - 2026-09-10

### Added
- Initial curator-tested seed of 57 public conversational AI access points across 25 country sections.
- Canonical JSON dataset and CSV export.
- README directory, interactive map/search UI, JSON Schema and coverage report.
- Weekly non-authoritative URL checker and GitHub Pages workflow.
- Contribution guidance, issue templates and MIT license.
