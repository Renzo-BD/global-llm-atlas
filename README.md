# 🌐 Global LLM Atlas

> **Discover conversational AI around the world — country by country, with evidence instead of hype.**

[![Version](https://img.shields.io/badge/version-v0.2.0-blue)](CHANGELOG.md)
![Access points](https://img.shields.io/badge/access%20points-57-2ea44f)
![Unique services](https://img.shields.io/badge/unique%20services-56-56d7c5)
![Countries](https://img.shields.io/badge/country%20associations-25-7b61ff)
![Maintenance](https://img.shields.io/badge/check-weekly-orange)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**[🗺️ Explore the interactive atlas](https://renzo-bd.github.io/global-llm-atlas/)** · **[📦 JSON](data/llms.json)** · **[📊 CSV](data/llms.csv)** · **[🤝 Contribute](CONTRIBUTING.md)**

**Global LLM Atlas** is an open, curated and versioned directory of publicly accessible conversational LLM/MLLM services around the world. It combines a reusable dataset, an interactive map and a maintenance workflow designed to distinguish a working AI experience from a merely reachable URL.

**Español:** atlas mundial abierto, curado y versionado de LLM/MLLM y asistentes conversacionales con acceso web público.

## ⭐ Why star this repo?

Star Global LLM Atlas if you want to follow a dataset that aims to answer a deceptively difficult question: **what conversational AI can people actually access around the world?**

- 🌍 **Country-by-country discovery**, including services outside the usual U.S.-centric lists.
- 🔎 **Curated evidence** for status, country association, registration and selected capabilities.
- 🧭 **Interactive world atlas** for browsing rather than digging through a giant link dump.
- 🧱 **Reusable JSON + CSV + JSON Schema** for research, analysis and other projects.
- 🩺 **Lifecycle tracking** with `ACTIVE`, `LIMITED`, `UNVERIFIED`, `INACTIVE` and `DISCONTINUED`.
- 🤖 **Weekly automated checks + human review**: HTTP availability never silently becomes semantic truth.
- 🧾 **Explicit uncertainty and provenance** instead of filling unknown fields with guesses.

> **Know a public conversational AI from a country we are missing?** Contributions with evidence are especially valuable.

## 📍 Current snapshot — v0.2.0

| Metric | Current canonical dataset |
|---|---:|
| Access points | **57** |
| Unique services | **56** |
| Country/project associations | **25** |
| `ACTIVE` | **55** |
| `LIMITED` | **2** |

The v0.2.0 release preserves the original curator-tested seed. `MULTI MODELOS` remains **explicitly excluded**, and no outside service was silently mixed into the seed release.

The canonical metadata includes service type, registration, text/image/voice/files/web-search capabilities, operator country, duplicate relationships, country confidence and provenance. A `null` capability means **not independently verified** — never “unsupported” by default.

## 🚀 Use the data

The project is intentionally useful beyond the website:

| Resource | Purpose |
|---|---|
| [`data/llms.json`](data/llms.json) | Canonical source of truth |
| [`data/llms.csv`](data/llms.csv) | Spreadsheet/data-analysis export |
| [`data/schema.json`](data/schema.json) | JSON Schema validation |
| [`data/curation-v0.2.csv`](data/curation-v0.2.csv) | v0.2 semantic-curation matrix |
| [`reports/curation-v0.2.0.md`](reports/curation-v0.2.0.md) | Curation rationale and evidence |
| [`reports/coverage-v0.1.0.md`](reports/coverage-v0.1.0.md) | Original geographic seed report |

Example with Python:

```python
import json
from urllib.request import urlopen

url = "https://raw.githubusercontent.com/Renzo-BD/global-llm-atlas/main/data/llms.json"
with urlopen(url) as response:
    atlas = json.load(response)

active = [x for x in atlas["entries"] if x["status"] == "ACTIVE"]
print(f"Active access points: {len(active)}")
```

## 🗺️ Interactive atlas

The **[GitHub Pages atlas](https://renzo-bd.github.io/global-llm-atlas/)** provides a responsive world view, live metrics, text search, country/service-type/status filters, registration information, capability indicators, operator-country and duplicate metadata, and direct access links.

Unknown capabilities are rendered as `?`, not as negative claims.

## ✅ What qualifies?

An entry should represent a **public conversational AI experience** with its own publicly reachable web interface, free access or a free tier, and usability in English or Spanish under the project's curation criteria.

Repositories-only projects, closed demos, abandoned services and purely private/internal interfaces are outside scope. The initial 0.x series grows conservatively; **v1.0.0 will wait for broader systematic country coverage and normalization.**

## 🧠 Curation model

`country` / `country_es` represents the atlas association supported by the project's evidence. It is not automatically the legal domicile of the operating entity. Where official evidence identifies another jurisdiction, `operator_country` records it separately.

`country_confidence` uses `verified`, `curator-verified`, or `partial`. Uncertainty stays visible rather than being guessed away.

Automated reachability is deliberately **non-authoritative**. A successful HTTP response does not prove that a conversational service is usable, and a failed request does not automatically make a service inactive.

## 🔬 Notable v0.2.0 findings

- **TextCortex:** two source URLs refer to the same service; the duplicate relationship is preserved rather than hidden.
- **Kruti:** `LIMITED` because its official site indicated the web experience was coming soon and directed users to the app at curation time.
- **IBM Granite Playground:** `LIMITED` because its public demo has a material usage cap.
- **Dola, Qwen and MiniMax:** project/seed association and operating jurisdiction are kept distinct where official terms support it.
- **Public AI:** association confidence is explicitly `partial` because it is a global multi-model platform.

See the [`v0.2.0 curation report`](reports/curation-v0.2.0.md) for the evidence trail.

## 🤝 Help map the world

The most useful contribution is a service from a **country not yet represented**. Before opening a contribution, check that the service has a real conversational web experience and provide evidence for its country/project association, public/free access, registration requirements and capabilities.

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for the full rules. Corrections and evidence upgrades are just as welcome as new entries.

If this dataset is useful to your research, project or AI exploration, **⭐ starring the repository helps more people discover it.**

## 🛠️ Maintenance

A weekly GitHub Actions workflow performs basic reachability checks. Suspect results are reported for review rather than directly changing canonical status. Human/semantic review remains required for login walls, regional restrictions, free-tier changes, conversational usability, capability changes, country ambiguity and discontinuation.

## 📜 License

MIT — see [`LICENSE`](LICENSE).
