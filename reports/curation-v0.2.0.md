# Deep curation report — v0.2.0

**Date:** 2026-09-10  
**Scope:** the 57 curator-tested seed access points only. `MULTI MODELOS` remains excluded.

## Result

- 57 access points retained
- 56 unique services after identifying one duplicate access point
- 25 country/project associations
- 55 `ACTIVE`; 2 `LIMITED`
- No entry was deleted merely because metadata was incomplete

The detailed curation matrix is in `data/curation-v0.2.csv`. Blank capability cells mean **not independently verified**, not unsupported.

## Method

The original seed records the curator's successful access test on 2026-09-10. This pass adds semantic metadata from official product, help, pricing, terms, privacy, imprint and institutional pages where sufficient evidence was available. Unknowns remain unknown rather than being inferred.

`country` in the seed should be interpreted as an **atlas association**, not automatically as legal-company domicile. The curation matrix therefore records `operator_country` separately where official information supports it.

## Material findings

### TextCortex
The seed contained two TextCortex URLs, one grouped under Germany and one under the United States. Official imprint information places TextCortex in Berlin, Germany. The second access point is retained for provenance but is marked as a duplicate of `de-textcortex` in the curation matrix.

Evidence: https://textcortex.com/imprint and https://textcortex.com/pricing

### Dola, Qwen and MiniMax
Their Chinese seed/project association is retained, while current official legal terms identify Singapore operating entities. The matrix records Singapore under `operator_country` rather than silently rewriting project provenance.

Evidence: https://www.dola.com/legal/terms/en ; https://qwen.ai/termsservice ; https://www.minimax.io/terms-of-service-v2.html

### Kruti
The current official website says the web experience is “Coming Soon” and directs users to the Ola app. It is therefore classified `LIMITED` rather than deleted.

Evidence: https://www.kruti.ai/

### IBM Granite Playground
The public Granite playground is free but explicitly demo-limited to a very small number of turns, so it is classified `LIMITED`.

Evidence: https://www.ibm.com/granite/playground

### Public AI
Public AI is a global public/multi-model platform rather than a Swiss-only provider. Its Swiss seed association is retained but its country confidence is marked `partial`.

Evidence: https://publicai.co/stories/utility

### ComfyAI
The project presents Austrian hosting/project identity, while its privacy notice names a German controller. The atlas keeps the seed association and records the nuance instead of forcing a simplistic nationality.

Evidence: https://comfyai.de/ and https://comfyai.de/privacy

## Capability semantics

The matrix separates image capability, voice/audio, files and web search. `True` means the capability was supported by this curation pass; an empty cell means it was not established reliably. It does **not** mean `False`.

## Next step toward v1.0.0

A later pass should move the curated fields into the canonical JSON schema after review, expand official-evidence coverage for curator-only entries, re-test the two `LIMITED` services, normalize direct-session URLs into stable public entry URLs where possible, and preserve lifecycle history instead of silently removing discontinued services.
