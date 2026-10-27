# Discovery and source review — 2026-10-27

## Outcome

Version 0.6.0 adds **three UNVERIFIED candidates**, with official access links: Typhoon Playground (Thailand), Duck.ai (United States) and Chanua (South Africa). These are newly catalogued services, not claims that they launched today.

Snapshot: **92 access points, 91 unique services, 43 country/project associations, 28 UNVERIFIED candidates**. Thailand is the new country association. Android: **38 native/regional records, two PWA rows for one unique service, one integrated record**.

Method: compare leads against the current canonical directory; read official publisher pages; perform public HTTP GET where available; examine Android publisher/store attribution. **No authenticated session or prompt/response test was completed.** A 200 response, login page or model download is not proof of successful inference.

## Added candidates

### Thailand — Typhoon Playground

- Atlas ID: `th-typhoon`
- Access: https://playground.opentyphoon.ai/
- Direct GET: **200**, redirects to Google sign-in; page describes text chat, OCR and ASR.
- Origin: Thai project. Current site/login names SCB DataX; FAQ credits SCB 10X.
- Free-access evidence: official FAQ describes the API as a free research showcase; model page links Web Playground. Current authenticated playground quotas and account eligibility remain untested.
- English prompting documented; no English/Spanish conversation tested.
- Model provenance: Typhoon 2.5 is associated with Qwen 3; do not infer a model trained from scratch or the currently served model.
- Android: no attributable official native conversational app verified.

Sources:
- https://opentyphoon.ai/
- https://playground.opentyphoon.ai/
- https://docs.opentyphoon.ai/en/faq/
- https://docs.opentyphoon.ai/en/prompting/
- https://opentyphoon.ai/model/typhoon2-5

### United States — Duck.ai

- Atlas ID: `us-duck-ai`
- Access: https://duck.ai/
- Direct GET: **200**, JavaScript application shell; English/Spanish locale links.
- Official help documents free access without an account, daily limits and optional paid upgrades.
- Country association: DuckDuckGo's official contact lists Pennsylvania, USA.
- Classify as a third-party multi-model platform, not a new DuckDuckGo foundation model.
- Android: official DuckDuckGo browser integration, package `com.duckduckgo.mobile.android`; recorded as **integrated**, not a standalone native Duck.ai app.
- Conversation, installation and access from Peru untested.

Sources:
- https://duckduckgo.com/duckduckgo-help-pages/duckai/approach-to-ai
- https://duckduckgo.com/duckduckgo-help-pages/duckai/usage-limits
- https://duckduckgo.com/duckduckgo-help-pages/company/contact-us
- https://duckduckgo.com/duckduckgo-help-pages/get-duckduckgo/does-duckduckgo-make-a-browser
- https://play.google.com/store/apps/details?id=com.duckduckgo.mobile.android

### South Africa — Chanua (HSRC)

- Atlas ID: `za-chanua`
- Access: https://chanua.hsrc.ac.za/
- HSRC's institutional page describes a **free career-guidance assistant**, with English among eleven languages.
- Direct GET: **200**, message/send controls and language selector. Search retrieval timed out; this mixed result is preserved.
- Developer association is South Africa. Its coverage of Kenya, Ghana, Ethiopia and Senegal does not create four additional national-model entries.
- Publisher describes retrieval over labour-market evidence; no independently trained national foundation model established.
- Registration remains unknown; the retrieved initial page showed no login wall, but no session/conversation was tested.
- Android: no attributable official native conversational app verified.

Sources:
- https://chanua.hsrc.ac.za/
- https://chanua.hsrc.ac.za/about

## Peru follow-up

Existing `pe-jeimy` remains **UNVERIFIED**. https://jeimy.ai/chat was retrievable, while direct GET to https://jeimy.ai/app returned 200 with presentation HTML and client-side application content. This is new reachability evidence, not a resolved conversation test. Official page still advertises Colibrí with daily free limits and account registration. Preserve the previous connection/reset and 403 history, URL, capability fields and conversation verification status.

Targeted searches also revisited university/government/model leads, including UNI, PUCP and Universidad del Pacífico, plus the ambiguous “Monolito” query. This pass did not establish another qualifying Peruvian public chat. That is a bounded search outcome, not proof that no further Peruvian LLM projects exist. Existing research records remain separate from public-chat counts.

## Deferred and excluded leads

| Lead | Official evidence / current check | Decision |
|---|---|---|
| OpenThai / Chinda 3 (Thailand) | https://openthai.ai/en/intro links https://chinda3.iapp.co.th/ as free browser use; direct GET returned 200 app shell. https://iapp.co.th/en/openmodels/openthai2p0 identifies a Qwen adaptation and a separately priced hosted API. | Follow-up queue: confirm conversational English/Spanish and current free chat limits. Do not confuse free weights or separate SystemOne classification API with free general chat. |
| ChatSUTRA (TWO AI) | https://www.two.ai/chatsutra/download links web and official Google Play. https://chat.two.ai/ returned 502 through search, 503 on direct GET. | Do not add while web access remains unresolved. Android listing alone does not qualify web access. |
| AfroChat | https://afrochat.app/ indexed FAQ advertises guest/free models; direct /en GET 200 app shell. | Country/operator attribution and live guest conversation require follow-up; no Ethiopia entry based only on African branding or language. |
| AI Hay (Vietnam) | https://ai-hay.com/ redirects to active publisher hub and links ai-hay.vn; official Android/iOS presence found. | English/Spanish chat and access from Peru not established. No canonical addition. |
| ChatEXAONE (South Korea) | https://showroom.exaone.ai/en FAQ explicitly says Beta no longer available; individuals cannot sign up and service is for enterprises. | Exclude as a public free-chat candidate. Do not substitute weights or enterprise showroom. |
| AMALIA (Portugal) | https://mosaico.gov.pt/plataformas-comuns/amalia explicitly distinguishes the open model from a public chat interface. | Research/model lead only. No public-chat entry based on model release alone. |
| HuggingChat | https://huggingface.co/chat/ alongside historical closure/reopening discussions and quota uncertainty. | Current sustained free-tier evidence unresolved in this pass; defer rather than recycle old free-access claims. |
| Ecosia AI Chat (Germany) | https://support.ecosia.org/article/1006-ai-search lists supported regions, without Peru in the retrieved list. | International access/eligibility follow-up; no new canonical entry. |

Prior curator exclusions remain in force: Sunflower, I'AM Chat, Becca, CakeAI and Mama Nigeria are not re-added; Kruti remains retired.

## Changes and validation

- Canonical JSON and CSV synchronized; Android JSON/CSV synchronized.
- README, citation, dataset card and website snapshot updated to 0.6.0.
- Thailand coordinates added to the map.
- Android interface displays and filters integrated access, distinct from native apps.
- Existing lifecycle states are preserved. Unknown capabilities remain null.
- Repository validator checks both JSON Schemas, CSV parity, IDs/references and JavaScript syntax.
- Issue #19 / PR #20 remain a separate URL-review task; this discovery update does not claim to resolve Crystal or Cladik.
