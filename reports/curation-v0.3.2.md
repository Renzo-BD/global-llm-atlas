# Worldwide model discovery and curation — 2026-10-16

## Result
Dataset v0.3.2 contains 77 access points, 76 unique services, 39 country associations, and 12 UNVERIFIED candidates. The 65 previously curated records retain their lifecycle states. Discovery uses official announcements and model cards; no signed-in conversation or free-tier test was completed during this review. Last manual verification on the three new records refers to source review, not a successful chat.

## New candidate access points
### Liquid AI Playground
- Access: https://playground.liquid.ai/
- Status: UNVERIFIED.
- Evidence: https://www.liquid.ai/blog/lfm2-5-24b-a2b
- Finding: LFM2.5-24B-A2B announced 2026-10-13. Official playground redirects to sign-in. Free tier and successful conversation not independently tested.

### Gnani Evon Playground
- Access: https://playground.gnani.ai/
- Status: UNVERIFIED.
- Evidence: https://www.gnani.ai/artha-sovereign-ai ; https://www.gnani.ai/ja-jp/resources/research/evon-v3-3-building-sovereign-llms-for-indian-languages
- Finding: Official playground for Evon v3.3; technical documentation identifies NVIDIA Nemotron 3 Nano 30B-A3B as backbone with continued pretraining and post-training. Free tier and successful conversation not independently tested.

### Asta
- Access: https://asta.allen.ai/
- Status: UNVERIFIED.
- Evidence: https://allenai.org/blog/astabrief
- Finding: AstaBrief 8B released 2026-10-02, adapted from Qwen3-8B, available in Asta report Fast mode. Asta also offers a Claude-powered Thinking mode: do not attribute every Asta response to AstaBrief. Free tier and successful conversation not independently tested.

Before promotion, test a real conversation, free-tier limits, registration, English or Spanish usability, geographic restrictions, and country/operator attribution. Unknown capabilities remain null. No Android availability is inferred.

## Updates for existing services
- **Muse Spark Open** (us-meta-ai): Weights published; this does not establish model availability in the tracked Meta AI chat. Source: https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B
- **Gemini 4 Argon** (us-gemini): Official app availability announcement; plan and regional access not independently tested. Source: https://blog.google/innovation-and-ai/products/gemini-app/gemini-4-argon-availability/
- **Mistral Large 4** (fr-le-chat): API public preview; weights announced for end of October, not established as released at review date. Availability in Le Chat not independently established. Source: https://mistral.ai/news/mistral-large-4/
- **Falcon-Emirati** (ae-falcon-llm-chat): Publisher announces forthcoming Falcon Chat availability; English/Spanish usability and model selector not tested. Source: https://www.tii.ae/news/tii-launches-falcon-emirati-alongside-new-arabic-ai-models-speech-and-visual-text

These are model-announcement provenance notes, not new access points or new successful-access checks.

## Deferred projects
- **Beam / Reflection**: announcement dated October 5; weights now listed at https://huggingface.co/reflection/Beam-1.0-501B-A23B . Initial blog described early access and a later weights release; use the current model repository to establish artifact availability. Qualifying free public web chat remains unverified. Sources: https://reflection.ai/blog/introducing-beam and https://reflection.ai/beam-model-card .
- **AMALIA / Portugal**: publicly available since July 1, not a new October launch. Model weights alone do not qualify as a conversational access point. Public chat and English/Spanish usability remain unverified. Sources: https://huggingface.co/amalia-llm/AMALIA-9B-0626-DPO and https://amaliallm.pt/ .

## Exclusion: Monolith-1.0
The name likely corresponds to basaltlabsai/monolith-1.0, rather than unrelated software named Monolith. Its publisher's current model card says the experiment has concluded, identifies the public model as an inflated Qwen 2.5 7B Instruct variant, and says the approximately 3 TB weights were removed. It therefore is not added as an independent foundation model or active qualifying chat. Do not repeat the original parameter or benchmark claims as verified facts.
Primary source: https://huggingface.co/basaltlabsai/monolith-1.0
Publisher-linked explanation: https://youtu.be/enk4w5mRjQY

## Validation
JSON Schema validation, unique IDs, JSON/CSV equivalence, preserved existing lifecycle states and metadata, and HTML script syntax are checked before publication.
