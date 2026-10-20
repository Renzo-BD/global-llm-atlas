# Global LLM Atlas — discovery and Android review, 2026-10-20

## Result and evidence limits

Dataset **v0.3.4** contains **83 access points**, **82 unique services**, **40 country/project associations**, and **19 UNVERIFIED candidates**. Seven entries were added: six general conversational candidates and CatIA, a specialized institutional assistant. They are new to this directory, not necessarily newly launched this week. The 76 earlier entries and their lifecycle states are preserved.

Android metadata **v0.3.0** adds four official conversational app channels, bringing the total to **35 native/regional app records**. The existing single unique PWA service remains separate. Verification means review of publisher/store evidence on this date. No APK installation, real conversation, successful login, Peruvian store availability, or sustained free-tier test was completed. Android distribution evidence does not promote a web candidate to ACTIVE.

## Newly recorded access points

| Atlas ID | Service and association | Official access | Remaining access checks |
|---|---|---|---|
| gb-gb1 | GB1 — United Kingdom | https://gb1.ai/ | Current free tier, registration and access from Peru. The landing page advertises free access but billing help describes a paid plan with a seven-day refund. |
| us-arcee-chat | Arcee Chat — United States | https://chat.arcee.ai/ | JavaScript conversation, current free limits, English/Spanish interaction and model selector. |
| in-indus | Indus by Sarvam — India | https://indus.sarvam.ai/ | Login, supported countries, current web model and free limits. English support is publisher-declared in the Android listing. |
| cn-longcat | LongCat — China | https://longcat.ai/ | Current conversation, free limits, registration, English/Spanish interaction and model selector. |
| cn-stepfun | StepFun Chat — China | https://chat.stepfun.com/chats/new | Supported registration countries, free tier and English/Spanish interaction. Promotional membership is not proof of sustained free access. |
| pl-bielik-chat | Bielik Chat — Poland | https://chat.bielik.ai/ | SpeakLeash sign-in, English/Spanish interaction, current chat model and limits. |
| pe-catia | CatIA (PCM) — Peru | https://catalogoia.servicios.gob.pe/catia | Successful interaction and access conditions. Public widget is visible; its scope is limited to the national AI catalog. |

All seven remain **UNVERIFIED**. Country confidence records the official evidence for the project/operator association; it does not verify proprietary model ownership. Capability fields beyond text remain null until independently checked.

### Model attribution

- **GB1:** publisher documentation identifies historical Locai L1 as adapted from Qwen 3; later Jupiter variants are distinct. Do not infer which model a current session serves.
- **Arcee:** its official website links “Chat for Free” and its catalog links Trinity models to the chat; not every currently selectable model was checked.
- **Indus:** the February 20 launch describes the Sarvam 105B model and a limited beta. This is launch evidence, not a current model-selector test.
- **LongCat:** Meituan publishes its own model family and identifies longcat.ai as the official conversational entry.
- **StepFun:** its official Android listing mentions both Step models and DeepSeek-R1. Do not attribute all answers to an in-house Step model.
- **Bielik:** SpeakLeash provides the model family and official chat. An open model license does not prove an unlimited free hosted service.
- **CatIA:** the SGTD/PCM transparency page explicitly names **deepseek-v4-flash via Huawei Cloud**. This is a Peruvian institutional deployment of third-party technology, not evidence of a Peruvian foundation model.

## Android review of the new findings

| Service | Finding | Official channel | Canonical Android record |
|---|---|---|---|
| GB1 | Official conversational app; publisher Locai Labs Limited | https://play.google.com/store/apps/details?id=com.locai.mobile | native / google-play |
| Indus | Official conversational app; publisher Sarvam AI | https://play.google.com/store/apps/details?id=ai.sarvam.indus | native / google-play |
| StepFun | Official conversational app; Shanghai StepFun publisher, links yuewen.cn and stepfun.ai | https://play.google.com/store/apps/details?id=cn.yuewen.ywapp | native / google-play |
| LongCat | Publisher README explicitly provides Android download instructions via QR | https://github.com/meituan-longcat/LongCat-Flash-Omni#app | native / official-download |
| Arcee Chat | No official conversational Android app verified in this review | https://www.arcee.ai/ | No positive app record; uncertainty retained |
| Bielik Chat | Related **Obywatel Bielik** app exists, but it collects photos/descriptions for model development | https://bielik.ai/obywatel-bielik-juz-na-smartfonach/ | Not counted as conversational Android access |
| CatIA | Official evidence describes a web widget; no dedicated Android app or installable PWA verified | https://catalogoia.servicios.gob.pe/catia | No positive app record; uncertainty retained |
| Kolibri | Official model weights/API/enterprise material found; no qualifying public free chat or official Android app verified | https://aleph-alpha.com/en/kolibri/ | Deferred; not added to service/app counts |

LongCat's URL deliberately opens the publisher's download instructions, not a guessed APK or third-party mirror. The QR destination, package identity, APK signature and installation were not independently tested. No Google Play listing is asserted for LongCat.

Obywatel Bielik's package is **pl.obywatel.bielik**, linked by SpeakLeash. It is preserved here as a related application, not mislabeled as Bielik Chat. Native-store presence for any service does not prove login support for a Peruvian phone number.

Negative search results are not proof of nonexistence. Structured Android-review outcomes and reviewed sources are stored under each new service's provenance.android_review.

## Deferred model: Kolibri

Aleph Alpha announced Kolibri on October 5 and states availability since October 3, 2026. Official materials describe open weights, German/English support and enterprise/API deployment. A qualifying public free web chat was not established; model weights alone do not meet this directory's conversational-service criteria. Keep it in this review queue.

Sources:
- https://aleph-alpha.com/en/news/kolibri-sovereign-ai-made-in-germany/
- https://aleph-alpha.com/en/blog/kolibri-has-landed-a-sovereign-open-weight-model/
- https://aleph-alpha.com/en/kolibri/

## Additional official evidence

- GB1: https://gb1.ai/ ; https://gb1.ai/ai-assistants/ ; https://www.locailabs.com/blog/gb1-goes-local ; https://help.gb1.ai/en/articles/12792217-is-there-a-free-trial
- Arcee: https://www.arcee.ai/ ; https://www.arcee.ai/open-source-catalog
- Indus: https://www.sarvam.ai/blogs/introducing-indus
- LongCat: https://tech.meituan.com/2026/06/30/LongCat2.0.html ; https://www.meituan.com/news/NN260116211001625
- Bielik: https://bielik.ai/jak-korzystac-z-bielika/

## Data maintenance and validation

- Regenerated both canonical CSV exports from their JSON data.
- Restored six pre-existing empty Android CSV URLs (Wrtn, ILMUchat, HUMAIN Chat, Lovable, Base44 and Zapia) from the unchanged JSON records. This is export repair, not a fresh verification of those apps.
- Updated the README, map snapshot, UK marker, Android access links, citation version and repository-local Hugging Face card.
- Added a deployment gate for both JSON Schemas, unique IDs, cross-file references, exact JSON/CSV equivalence, nonempty official app URLs, and JavaScript syntax.
- Kruti remains retired; Monolith-1.0 remains excluded. No existing lifecycle state was promoted.
