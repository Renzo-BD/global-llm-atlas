# Changelog

All notable changes to **Global LLM Atlas** are documented here.

The project follows [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Fixed
- Review URL-check issue #19: correct GuffGPT to its officially linked chat endpoint and required registration; synchronize exports.
- Record Copuchat/GuffGPT non-reproduced transport alerts and unresolved Crystal/Cladik access in a dated report and provenance. Lifecycle states and conversation-test dates remain unchanged.

### Planned
- Continue official-evidence review for country associations and Android availability.
- Re-test `LIMITED` and `INACTIVE` services and normalize unstable URLs.
- Continue systematic country expansion.

## [0.5.0] - 2026-10-23

### Added
- Only eustella (Austria), selected by the curator from the October 23 discovery pass, as UNVERIFIED pending a documented successful conversation test.
- Official eustella Android listing (Google Play, com.eustella).
- Decision report preserving curator feedback: other leads excluded for instability; I’AM Chat temporarily closed for scalability improvements according to the curator.

### Changed
- 89 access points, 88 unique services, 42 country associations, 25 UNVERIFIED candidates and 38 native/regional Android apps.
- Synchronized JSON/CSV, README, atlas notice, citation and repository Hugging Face card.
- No other service entry or existing lifecycle state modified.

## [0.4.1] - 2026-10-22

### Changed
- Jeimy source review records reproduced access errors, required registration, publisher-declared provider and unresolved model provenance; lifecycle stays UNVERIFIED.
- Copuchat provenance documents official LatamGPT FAQ and Peru cooperation without duplicate country attribution or a new conversation-test date.
- Added Peru research watchlist and university/government evidence report, with Android review outcomes. Yachay and QuBERT are not counted as qualifying public chats.
- No new native Android app verified; 88 access points, 87 unique services, 42 country associations and 37 native/regional apps retained.
- README, map notice, citation and repository Hugging Face card reference this follow-up.

## [0.4.0] - 2026-10-22

### Added
- Five UNVERIFIED discovery candidates: MATE, Euria, NG∞AI, Labiba and GovGuide Nigeria.
- Two country associations: South Africa and Nigeria, with map coordinates.
- Two official Google Play listings: MATE and Euria. Android metadata version is 0.4.0.
- Official-source evidence, free-tier caveats and deferred candidates in `reports/curation-v0.4.0-2026-10-22.md`.

### Changed
- Synchronized JSON/CSV, map, README, citation and local Hugging Face dataset card: 88 access points, 87 unique services, 42 country associations, 24 UNVERIFIED candidates, 37 native/regional Android apps and one unique PWA service.
- Source review does not establish successful conversation, unrestricted guest access, Peruvian availability or independent national base models. Existing lifecycle states remain unchanged.

## [0.3.4] - 2026-10-20

### Added
- Seven UNVERIFIED access points: GB1 (United Kingdom), Arcee Chat (United States), Indus (India), LongCat and StepFun (China), Bielik Chat (Poland), and CatIA/PCM (Peru).
- Four official Android conversational app channels: GB1, Indus and StepFun on Google Play; LongCat via publisher-provided Android QR/download instructions.
- Structured Android review outcomes and an evidence report at `reports/curation-v0.3.4-2026-10-20.md`.
- Schema, JSON/CSV, reference and JavaScript checks before Pages deployment.

### Fixed
- Six Android CSV URLs missing despite being present in canonical JSON.
- Current map/readme/citation/Hugging Face card snapshots and the UK map marker.
- Main-atlas Android access links now include official download and PWA channels.

### Curation
- 83 access points, 82 unique services, 40 country associations, 19 UNVERIFIED candidates and 35 native/regional Android app records.
- Android evidence is source-reviewed, not an installation or access-from-Peru test.
- CatIA is attributed to a Peruvian institutional deployment of DeepSeek/Huawei Cloud. Obywatel Bielik is not counted as a conversational app. Kolibri remains deferred.

## [0.3.3] - 2026-10-16

### Removed
- Kruti (`in-kruti`) from the current JSON/CSV directory and map at curator request. Its former INACTIVE record and evidence are retained in `reports/retired-kruti-2026-10-16.md`.
- No permanent-shutdown claim is inferred from the official maintenance notice.

### Changed
- Current totals: 76 access points, 75 unique services, 39 country associations and 12 UNVERIFIED candidates.

## [0.3.2] - 2026-10-16

### Added
- Three UNVERIFIED discovery candidates: Liquid AI Playground, Gnani Evon Playground and Asta, with official evidence and explicit access-test limitations.
- Worldwide review report with deferred Beam and AMALIA projects and primary-source exclusion of Monolith-1.0.

### Changed
- JSON, CSV, README and atlas copy synchronized: 77 access points, 76 unique services, 39 country associations, 12 UNVERIFIED candidates.
- Added model-announcement provenance for Meta, Gemini, Mistral and Falcon without inferring access or changing existing lifecycle states.

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
