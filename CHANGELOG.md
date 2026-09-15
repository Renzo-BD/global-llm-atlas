# Changelog

All notable changes to **Global LLM Atlas** are documented here.

The project follows [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added
- Curated Android-access metadata keyed to stable Atlas IDs in `data/android.json`.
- Flat Android export in `data/android.csv` and validation schema in `data/android-schema.json`.
- Dedicated GitHub Pages Android explorer at `android.html` with search, country and distribution-state filters.
- Direct official app/store/download links and per-record Android verification dates.
- Android contribution rules distinguishing native, regional-store and PWA/web-install access.

### Changed
- README now exposes Android access as a first-class curated dimension without changing canonical web lifecycle status.
- Android uncertainty follows the same project rule as capability uncertainty: missing metadata means not independently verified, never unsupported.
- Existing `fr-le-chat` continuity is preserved while documenting that the current Android app is branded **Vibe by Mistral**.

### Android findings — 2026-09-15
- **25 unique services** have a currently verified native or official regional Android app in the conservative Android seed.
- **TextCortex** is tracked separately as an installable-web/PWA experience and is not counted as a native Android app.
- **GigaChat** is tracked as an official regional Android distribution through RuStore.
- **ERNIE** is tracked as an official regional Android distribution rather than assuming global Google Play availability.
- Third-party wrappers, unofficial APK mirrors and ambiguous store listings are excluded.

### Planned
- Continue official-evidence review for `curator-verified` country associations.
- Re-test `LIMITED` and `INACTIVE` services and normalize unstable/direct-session URLs.
- Expand geographic coverage systematically.
- Preserve lifecycle history for services that later become inactive or discontinued.
- Extend the platform model to iOS, Windows and macOS after the Android methodology is stable.

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
