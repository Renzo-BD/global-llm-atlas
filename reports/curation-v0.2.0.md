# Deep curation report — v0.2.0

**Date:** 2026-09-10  
**Scope:** the 57 curator-tested seed access points.

## Result

- 57 access points retained
- 56 unique services after identifying one duplicate access point
- 25 country/project associations
- 55 `ACTIVE`; 2 `LIMITED`
- No entry was deleted merely because metadata was incomplete
- Curated metadata migrated into canonical `data/llms.json`, synchronized to `data/llms.csv`, and represented by `data/schema.json`

The working curation matrix remains in `data/curation-v0.2.csv`. Blank capability cells there, and `null` capability values in canonical JSON, mean **not independently verified**, not unsupported.

## Method

The initial records reflect the curator's successful access test on 2026-09-10. This pass adds semantic metadata from official product, help, pricing, terms, privacy, imprint and institutional pages where sufficient evidence was available. Unknowns remain unknown rather than being inferred.

`country` is an **atlas association**, not automatically legal-company domicile. The canonical dataset therefore records `operator_country` separately where official information supports it.

## Material findings

### TextCortex
The seed contained two TextCortex URLs, one grouped under Germany and one under the United States. Official imprint information places TextCortex in Berlin, Germany. The second access point is retained for provenance but marked as `duplicate_of: de-textcortex`.

Evidence: https://textcortex.com/imprint and https://textcortex.com/pricing

### Dola, Qwen and MiniMax
Their Chinese seed/project association is retained, while current official legal terms identify Singapore operating entities. The canonical dataset records Singapore under `operator_country` rather than silently rewriting project provenance.

Evidence: https://www.dola.com/legal/terms/en ; https://qwen.ai/termsservice ; https://www.minimax.io/terms-of-service-v2.html

### Kruti
The official website indicated that the web experience was “Coming Soon” and directed users to the Ola app during this curation pass. It is therefore classified `LIMITED` rather than deleted.

Evidence: https://www.kruti.ai/

### IBM Granite Playground
The public Granite playground is free but explicitly demo-limited to a very small number of turns, so it is classified `LIMITED`.

Evidence: https://www.ibm.com/granite/playground

### Public AI
Public AI is a global public/multi-model platform rather than a Swiss-only provider. Its Swiss seed association is retained but `country_confidence` is `partial`.

Evidence: https://publicai.co/stories/utility

### ComfyAI
The project presents Austrian hosting/project identity, while its privacy notice names a German controller. The atlas keeps the seed association and records the nuance instead of forcing a simplistic nationality.

Evidence: https://comfyai.de/ and https://comfyai.de/privacy

## Capability semantics

The canonical model separates text, image, voice/audio, files and web search. `true` means supported by this curation pass; `null` means not established reliably. No capability is set to `false` merely because evidence was not found.

Text is `true` for all 57 seed access points because conversational text usability was part of the curator-tested inclusion basis.

## Remaining work before v1.0.0

Future curation should expand official-evidence coverage for entries still marked `curator-verified`, re-test the two `LIMITED` services, normalize direct-session URLs into stable public entry URLs where possible, verify language/access nuances, preserve lifecycle history instead of silently removing discontinued services, and continue broader country expansion systematically.
