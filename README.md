# 🌐 Global LLM Atlas

> A curated, versioned atlas of **public conversational LLM/MLLM web experiences around the world**.

[![Version](https://img.shields.io/badge/version-v0.2.0-blue)](CHANGELOG.md)
![Access points](https://img.shields.io/badge/access%20points-57-2ea44f)
![Unique services](https://img.shields.io/badge/unique%20services-56-56d7c5)
![Countries](https://img.shields.io/badge/country%20associations-25-7b61ff)
![Maintenance](https://img.shields.io/badge/check-weekly-orange)

**Global LLM Atlas** is a curated dataset, interactive directory and maintenance workflow for publicly accessible conversational AI services. It records where each access point is associated, what kind of service it is, whether registration is required, selected capabilities, lifecycle status and when the access was manually checked.

**Español:** atlas mundial curado y versionado de LLM/MLLM y asistentes conversacionales con acceso web público.

## v0.2.0 — canonical metadata migration

The v0.2.0 release keeps the original scope intact:

- **57 curator-tested access points**
- **56 unique services** after identifying the second TextCortex URL as a duplicate
- **25 country/project associations**
- **55 `ACTIVE`** and **2 `LIMITED`**
- `MULTI MODELOS` remains **explicitly excluded**
- no new service was added outside the curator-provided HTML seed

The canonical JSON now includes service type, registration, text/image/voice/files/web-search capabilities, operator country, duplicate relationships, country-confidence and provenance metadata.

A `null` capability means **not independently verified**. It must not be interpreted as unsupported.

## Data

| Resource | Purpose |
|---|---|
| [`data/llms.json`](data/llms.json) | Canonical source of truth |
| [`data/llms.csv`](data/llms.csv) | Spreadsheet-friendly canonical export |
| [`data/schema.json`](data/schema.json) | JSON Schema for validation |
| [`data/curation-v0.2.csv`](data/curation-v0.2.csv) | v0.2 semantic-curation working matrix |
| [`reports/curation-v0.2.0.md`](reports/curation-v0.2.0.md) | Curation rationale and evidence |
| [`reports/coverage-v0.1.0.md`](reports/coverage-v0.1.0.md) | Original geographic seed report |

## Status vocabulary

| Status | Meaning |
|---|---|
| `ACTIVE` | Public access manually verified as working |
| `LIMITED` | Public access exists but a material restriction affects the experience |
| `UNVERIFIED` | Current usability has not been manually established |
| `INACTIVE` | Confirmed unavailable after human review |
| `DISCONTINUED` | Service/project confirmed discontinued |

Automated reachability checks are deliberately **non-authoritative**. An HTTP response does not prove that a conversational service is usable, and an automated failure does not silently change canonical status.

## Country semantics

`country` / `country_es` represents the **atlas association inherited from the curator's seed**. It is not automatically the legal domicile of the operating entity. When official evidence supports a separate operating jurisdiction, it is recorded in `operator_country`.

`country_confidence` uses `verified`, `curator-verified`, or `partial`. Uncertainty is kept explicit rather than guessed.

## Notable v0.2.0 findings

- **TextCortex:** two source URLs refer to the same service. The German access point remains canonical; the U.S.-grouped source URL is retained for provenance and points to `duplicate_of: de-textcortex`.
- **Kruti:** classified `LIMITED` because its official site indicated the web experience was coming soon and directed users to the app at the time of curation.
- **IBM Granite Playground:** classified `LIMITED` because the public demo has a material usage cap.
- **Dola, Qwen and MiniMax:** Chinese seed/project association is retained while Singapore operating entities are recorded separately where official terms support that distinction.
- **Public AI:** Swiss seed association is retained with `partial` confidence because the platform is global/multi-model.

See the [v0.2.0 curation report](reports/curation-v0.2.0.md) for the evidence trail.

## Interactive atlas

`index.html` provides a responsive world map, live metrics, text search, country/service-type/status filters, registration information, capability indicators, operator-country and duplicate metadata, and direct access links.

Unknown capabilities are rendered as `?`, not as a negative claim.

## Inclusion principles

An access point belongs in the atlas when it is intended to provide a public conversational AI experience, has its own publicly reachable web interface, has free access or a free tier, and is usable in English or Spanish under the project's curation criteria. Repositories, closed demos, abandoned projects and purely private/internal interfaces are outside scope.

The initial 0.x series intentionally grows conservatively. **v1.0.0 should not be declared until the seed is fully normalized and broader country coverage has been systematically audited.**

## Maintenance

The weekly GitHub Actions workflow performs basic reachability checks. Suspect results are reported for review rather than directly changing canonical status. Human or semantic review remains required for login walls, regional restrictions, free-tier changes, conversational usability, capability changes, country ambiguity and discontinuation.

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md). Please provide evidence for changes to country association, status, registration or capabilities.

## License

MIT — see [`LICENSE`](LICENSE).
