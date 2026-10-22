# Discovery and Android review — 2026-10-22

## Outcome and method

Compared worldwide search results with the 83 existing access points. Added five distinct candidates backed by publisher sources, including two new country associations. Snapshot: **88 access points, 87 unique services, 42 country associations, 24 UNVERIFIED candidates, 37 native/regional Android apps and one unique PWA service**.

This review used public search, publisher documentation, indexed interfaces and official store listings. No message was submitted, account created, APK installed or authenticated session tested. `last_manual_verification` is the source-review date, not a successful-use date. All five new web records remain **UNVERIFIED**; claimed features remain in provenance while untested capability fields stay null. Existing lifecycle states were preserved. These are new directory discoveries, not necessarily new releases or national foundation models.

## New candidates and primary evidence

| Candidate | Association | Public entry | Access evidence and limitation | Android |
|---|---|---|---|---|
| MATE by Swisswise | Switzerland | https://app.swissmate.ai/ | Operator identifies Swisswise GmbH, Bern. Login page retrieved. Pricing explicitly offers 10 requests/month for CHF 0, with registration. No conversation tested. | Official Google Play, `com.swisswise.mate` |
| Euria | Switzerland | https://euria.infomaniak.com/ | Infomaniak advertises free guest access and publishes English/Spanish documentation. Uses selected open-source models. Direct web extraction gave no readable content; current guest flow and quotas untested. | Official Google Play, `com.infomaniak.euria` |
| NG∞AI | South Africa | https://ng-ai.co.za/ | Embedded chat advertises English, isiZulu and Afrikaans without signup, optional account, and a free pilot while online. Backend availability not tested. | No dedicated official app verified; WhatsApp is a separate channel. |
| Labiba / OLabiba | Canada, publisher self-identification | https://www.olabiba.com/ | FAQ advertises free no-account English/Spanish chat. Human-verification dialog exists in extracted markup; no conclusion about whether it blocks live use. Legal domicile unconfirmed, so country confidence is partial. | No attributable official app verified. Similar store names were excluded. |
| GovGuide Nigeria | Nigeria | https://govguide.ng/chat | Government announcement and Publica AI product agree on Nigerian deployment using Meta open-source models. Landing page advertises free start. Chat indexed, but direct extraction returned no readable content; registration and limits unknown. | No dedicated official app verified; WhatsApp is a separate channel. |

### MATE

- https://swisswise.com/en/mateapp — operator, Swiss association, product and free plan.
- https://swissmate.ai/en — publisher links web and Google Play.
- https://swissmate.ai/en/pricing — 10 free requests/month. Image generation and offline mode are paid features; do not describe the entire product as unlimited/free.
- https://play.google.com/store/apps/details?id=com.swisswise.mate — official Android listing.

### Euria

- https://www.infomaniak.com/en/apps/download-euria — Swiss hosting, assistant and open-source-model deployment.
- https://news.infomaniak.com/en/euria-sovereign-ai-assistant/ — guest/free access claim.
- https://news.infomaniak.com/es/euria-asistente-ia-soberano/ — Spanish official documentation.
- https://github.com/Infomaniak/android-euria — publisher's Android repository; also describes account-based use.
- https://play.google.com/store/apps/details?id=com.infomaniak.euria — official Android listing.

### NG∞AI

- https://ng-ai.co.za/ — South African community project, embedded public web chat, English support and free-pilot terms.
- https://ng-ai.co.za/privacy — conversations are recorded and reviewed, rate limits apply, and service may go offline. Local hosting does not establish independent foundation-model training.

### Labiba

- https://www.olabiba.com/ — public chat, language selector and human-verification markup.
- https://www.olabiba.com/faq/ — Canadian team, English/Spanish, no signup and free-use claims.
- https://www.olabiba.com/free-ai-chatbot-no-sign-up/ — browser-based delivery. No separate native app attributed.

### GovGuide Nigeria

- https://fmcide.gov.ng/fmcide-and-meta-launch-govguide-nigeria-an-ai-powered-government-services-chatbot/ — ministry announcement of Publica AI/FMCIDE/NCAIR/Meta collaboration and English/Hausa/Igbo/Yoruba support; deployment of Meta models including Llama.
- https://govguide.ng/ — branded product with matching Publica AI/NCAIR contact details and free-start link.
- https://govguide.ng/chat — indexed conversational entry; extraction did not demonstrate a response.
- https://govguide.ng/faq — voice/text and access channels.
- https://govguide.ng/privacy-policy — information and guidance only, not a transactional government portal or binding decision service.

## Reviewed but deferred

| Candidate | Primary source | Reason for deferral |
|---|---|---|
| Chat Care, Kenya Red Cross | https://redcross.or.ke/chat-care/ | Official page advertises free English/Swahili AI support and webchat, but its Website link resolves to the Red Cross homepage. Need a reachable direct conversational entry and model/LLM clarification before adding. |
| ngini | https://ngini.com/en-us/about | Team identifies Europe and hosting in Germany; hosting does not establish operator/project country. Country association unresolved. |
| gizza.ai | https://gizza.ai/ | Browser-local WebGPU chat described; country/operator attribution unresolved and hardware/model-loading not tested. |
| Oshu | https://oshu.eu/ | Free chatbot-building/embedding product; qualifying general conversational access and operator country still need review. |
| Relaite | https://relaite.org/ | Advertises 25 starter messages, then requires a user's paid OpenRouter key. Sustained qualifying free tier not established. |
| SwizzAI | https://www.swizzai.ch/ | Advertises five starter requests, then payment; qualifying public browser chat and ongoing free tier not established. |
| TumaChat AI | https://tumachat.com/blog/tumachat-ai-assistant-four-languages | Rwanda-focused free in-app beta; independent qualifying public browser chat not established in this review. |
| Kolibri | https://github.com/Aleph-Alpha-Research | Previous deferral retained; no qualifying public conversational entry established by this search. |

Discovery also sampled Latin American and Asian search results. No additional service from those results was promoted without sufficient country, free-tier and public-web evidence. This is a targeted discovery pass, not an exhaustive country census or revalidation of all existing entries.

## Android interpretation

Two publisher-attributed Google Play listings were source-reviewed. Neither installation nor availability from Peru was tested. MATE and Euria increase native/regional app records from 35 to 37. Mobile browser and WhatsApp availability do not create native-app records, and missing Android records mean unverified rather than unsupported.

## Validation

Run `python scripts/validate_data.py` to verify both schemas, IDs/references, synchronized CSV exports and JavaScript syntax. Snapshot counts and map coordinates were checked independently before publication.
