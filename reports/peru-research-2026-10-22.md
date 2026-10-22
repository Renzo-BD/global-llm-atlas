# Peru follow-up and Android review — 2026-10-22

## Outcome

This follow-up reviews government/university research and Jeimy availability. It does not add unqualified research projects to the public-chat directory. Main totals remain **88 access points, 87 unique services, 42 country associations, 24 UNVERIFIED candidates and 37 native/regional Android apps**.

Machine-readable research leads are in [data/research-peru.json](../data/research-peru.json). They are excluded from canonical catalog metrics. No new native Android record was justified.

## Jeimy: access and attribution

The curator reported the site would not load. Chrome navigation on the same date reproduced `net::ERR_CONNECTION_RESET`. Separate HTTP retrievals returned presentation HTML for both the homepage and /app; later requests returned 403. Search extraction still returned marketing content. Current retrieval of legal and model documentation also failed. These are mixed access results, not proof of closure or a working chat.

Jeimy remains **UNVERIFIED**. Its source-review date is updated; registration is now recorded as required, based on the publisher's account flow. No successful conversation was verified.

The publisher names Colibrí/Colibrí 2, Águila and Apu and advertises limited free Colibrí use. The complaint book reviewed earlier on the same date identified **Infinity Group Dev · Jeimy AI**. Named founders, full legal identity and technical/model-training provenance were not independently corroborated. No specific third-party base model is attributed.

Sources:
- https://jeimy.ai/
- https://jeimy.ai/chat
- https://jeimy.ai/reclamaciones
- https://jeimy.ai/terminos
- https://docs.jeimy.ai/api/modelos/
- https://www.npmjs.com/package/@jeimy-ai/cli

## Research leads

| Project | Evidence and classification | Catalog decision | Android |
|---|---|---|---|
| Yachay SLM | Personal repository associated with Carlos Mauro Cárdenas in Peru. Nano is described as trained from scratch; General uses LoRA over Qwen2.5-0.5B. Source code/weights were inspected as documentation, not executed. No institutional UNI ownership inferred. | Research watchlist; qualifying public web chat not verified. | No attributable official native app verified. |
| QuBERT / Llamacha | Publisher repository documents Southern Quechua pretraining and a RoBERTa-style masked-language-model workflow, with tokenizer/model resources. | Research watchlist; not a verified conversational service. | No attributable official native app verified. |
| LatamGPT / Peru cooperation | PCM documents Peru–Chile memorandum; CENIA describes regional model development based on Llama 3.1 70B. | Already represented by Chile-associated `cl-copuchat`; no duplicate Peru chat entry. | No attributable official native app verified. |

Primary sources:
- Yachay: https://github.com/unimauro/yachay-slm and https://unimauro.github.io/
- QuBERT: https://github.com/Llamacha/QuBERT and https://huggingface.co/datasets/Llamacha/monolingual-quechua-iic
- LatamGPT FAQ: https://latamgpt.org/faq
- CENIA launch: https://cenia.cl/2026/02/10/latam-gpt-la-primera-ia-regional-abierta-creada-con-datos-latinoamericanos/
- Peru–Chile cooperation: https://www.gob.pe/institucion/pcm/noticias/1294929-peru-y-chile-impulsan-alianza-estrategica-para-desarrollar-inteligencia-artificial-propia-en-la-region

Copuchat provenance now links the official FAQ, which identifies the experimental LatamGPT-SFT chat and explains collection of interactions for alignment/post-training. This is a source update; its earlier curator-tested lifecycle and last conversation-verification date are not overwritten.

## University and government evidence matrix

| Institution | Public evidence | Interpretation |
|---|---|---|
| UNI / INICTEL-UNI | [2026 internship call](https://www.gob.pe/institucion/inictel-uni/informes-publicaciones/8080848-bases-cpm-practicas-preprofesionales-n-001-2026-inictel-uni-didt) for a system using an open-source LLM to query tree-species classification reports. | Applied LLM system. No independently trained general UNI foundation model established. Search-index evidence available; direct retrieval failed. |
| PUCP | [URB-LLM](https://cris.pucp.edu.pe/entities/project/8bd3ffba-5bb9-4e23-9291-108f8e01ba00), registered active July 2025–July 2027, applies web scraping and LLM processing to urban/legal research. | Applied research, not proof of a new base model. |
| PUCP | [TARPURIQ](https://cris.pucp.edu.pe/entities/project/c18da408-8c3c-46c4-a7bc-bf3a4bd366cd), registered concluded in 2023, develops Southern Quechua computational resources. | Language-resource research; no qualifying conversational service established. |
| Universidad del Pacífico | [Reading-comprehension project](https://labfranciscotumi.up.edu.pe/proyecto/ampliando-la-comprension-lectora-a-traves-de-un-sistema-inteligente-basado-en-la-arquitectura-gpt/) describes FairytaleQA and transfer learning. | Educational adaptation/research. Search-index evidence; direct retrieval returned 403. No deployed public general chat established. |
| Universidad de Lima | [Business-plan thesis](https://repositorio.ulima.edu.pe/item/940b77c3-5a0b-4327-9136-6a0f245a2ea8) and [indexed PDF](https://repositorio.ulima.edu.pe/bitstream/handle/20.500.12724/23618/T018_72519953_T.pdf?isAllowed=y&sequence=1) describe a legal platform integrating a pretrained LLM. | Academic proposal, not proof of an operational university model. Direct document retrieval was limited. |
| Cayetano Heredia | [Generative-AI research course](https://e.cayetano.edu.pe/programas/curso-internacional-investigacion-academica-aumentada-con-inteligencia-artificial-generativa/) covers existing models and customized assistants. | Training/application evidence. This search did not establish an institutional foundation-model construction project; absence of a result is not proof none exists. |
| UNMSM | [Illariy Willarisunki announcement](https://letras.unmsm.edu.pe/noticias/illariy-willarisunki-illariy-te-cuenta-un-viaje-transmedia-en-quechua-a-traves-de-las-leyendas-peruanas-con-inteligencia-artificial/) explicitly identifies GPT-4/OpenAI. | Customized assistant/avatar, not an independently trained Peruvian base model. |
| UCSP | [2025 research-award resolution](https://ucsp.edu.pe/archivos/publicaciones/Direccion-investigacion/resolucion-directoral-nro-008-2025.pdf) lists a study of a conversational agent based on a large language model in adults in Arequipa and Lima. | Applied study, not evidence of a new general base model. |
| PCM / CatIA | [Transparency page](https://catalogoia.servicios.gob.pe/catia) identifies DeepSeek via Huawei Cloud. | Existing `pe-catia` institutional assistant, not a new national foundation model. No native Android listing verified. |

## Android methodology and results

Reviewed official product/repository/FAQ sources and targeted Google Play searches for Jeimy AI, Yachay associated with its identified author, QuBERT/Llamacha and LatamGPT. No attributable official native Android listing was found. Similar names and unrelated store results were excluded.

Jeimy describes use in a mobile browser and offers a terminal CLI. Yachay describes CPU/IoT execution; this does not prove a packaged Android app. QuBERT provides model resources, which are not an app. LatamGPT describes a web interface and downloadable weights. None establishes native Android or a verified installable PWA.

Missing app evidence means **not independently verified**, not unsupported. Existing Android records for MATE and Euria from v0.4.0 are retained; total remains 37 native/regional apps. No APK was installed or tested.

## Limits and verification

This is a targeted public-source review, not an exhaustive census of unpublished university work. Research claims were not reproduced by training models. Browser failure, indexing and HTTP retrieval are separate observations and do not establish service lifecycle on their own.

Canonical CSV is regenerated from JSON. ID counts, references, snapshot totals, preservation of other records and research-watchlist exclusions were checked before publishing. The existing Pages workflow additionally validates JSON schemas, CSV parity and browser-script syntax.
