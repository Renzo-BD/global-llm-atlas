# 🌐 Global LLM Atlas

> **Discover conversational AI around the world — country by country, with evidence instead of hype.**

[![Version](https://img.shields.io/badge/version-v0.2.0-blue)](CHANGELOG.md)
![Access points](https://img.shields.io/badge/access%20points-57-2ea44f)
![Unique services](https://img.shields.io/badge/unique%20services-56-56d7c5)
![Countries](https://img.shields.io/badge/country%20associations-25-7b61ff)
![Android apps](https://img.shields.io/badge/verified%20Android%20apps-25-3ddc84)
![Maintenance](https://img.shields.io/badge/check-weekly-orange)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**[🗺️ Explore the interactive atlas](https://renzo-bd.github.io/global-llm-atlas/)** · **[🤖 Explore Android access](https://renzo-bd.github.io/global-llm-atlas/android.html)** · **[📦 JSON](data/llms.json)** · **[📊 CSV](data/llms.csv)** · **[🤝 Contribute](CONTRIBUTING.md)**

**Global LLM Atlas** is an open, curated and versioned directory of publicly accessible conversational LLM/MLLM services around the world. It combines a reusable dataset, an interactive map and a maintenance workflow designed to distinguish a working AI experience from a merely reachable URL.

**Español:** atlas mundial abierto, curado y versionado de LLM/MLLM y asistentes conversacionales con acceso público. La disponibilidad Android se documenta como una dimensión independiente del estado del acceso web.

## ⭐ Why star this repo?

Star Global LLM Atlas if you want to follow a dataset that aims to answer a deceptively difficult question: **what conversational AI can people actually access around the world?**

- 🌍 **Country-by-country discovery**, including services outside the usual U.S.-centric lists.
- 🔎 **Curated evidence** for status, country association, registration and selected capabilities.
- 🧭 **Interactive world atlas** for browsing rather than digging through a giant link dump.
- 🤖 **Curated Android access**, distinguishing native, regional-store and installable-web/PWA availability.
- 🧱 **Reusable JSON + CSV + JSON Schema** for research, analysis and other projects.
- 🩺 **Lifecycle tracking** with `ACTIVE`, `LIMITED`, `UNVERIFIED`, `INACTIVE` and `DISCONTINUED`.
- 🤖 **Weekly automated checks + human review**: HTTP availability never silently becomes semantic truth.
- 🧾 **Explicit uncertainty and provenance** instead of filling unknown fields with guesses.

> **Know a public conversational AI from a country we are missing?** Contributions with evidence are especially valuable.

## 📍 Current snapshot — v0.2.0 + Android metadata

| Metric | Current dataset |
|---|---:|
| Access points | **57** |
| Unique services | **56** |
| Country/project associations | **25** |
| Verified native/regional Android apps | **25** |
| Installable-web/PWA Android experiences | **1 unique service** |

The canonical service metadata includes service type, registration, text/image/voice/files/web-search capabilities, operator country, duplicate relationships, country confidence and provenance. A `null` capability means **not independently verified** — never “unsupported” by default.

Android metadata follows the same uncertainty rule. Absence from `data/android.json` means **not independently verified**, not that Android support has been disproven.

## 🚀 Use the data

| Resource | Purpose |
|---|---|
| [`data/llms.json`](data/llms.json) | Canonical service source of truth |
| [`data/llms.csv`](data/llms.csv) | Canonical spreadsheet/data-analysis export |
| [`data/schema.json`](data/schema.json) | Canonical JSON Schema validation |
| [`data/android.json`](data/android.json) | Curated Android access metadata keyed by Atlas ID |
| [`data/android.csv`](data/android.csv) | Android metadata spreadsheet export |
| [`data/android-schema.json`](data/android-schema.json) | Android metadata JSON Schema |
| [`data/curation-v0.2.csv`](data/curation-v0.2.csv) | v0.2 semantic-curation matrix |
| [`reports/curation-v0.2.0.md`](reports/curation-v0.2.0.md) | Curation rationale and evidence |
| [`reports/coverage-v0.1.0.md`](reports/coverage-v0.1.0.md) | Original geographic seed report |

Example with Python:

```python
import json
from urllib.request import urlopen

base = "https://raw.githubusercontent.com/Renzo-BD/global-llm-atlas/main/data/"
with urlopen(base + "llms.json") as response:
    atlas = json.load(response)
with urlopen(base + "android.json") as response:
    android = json.load(response)

android_ids = {
    x["id"] for x in android["entries"]
    if x["status"] in {"native", "regional"}
}
apps = [x for x in atlas["entries"] if x["id"] in android_ids and not x["duplicate_of"]]
print(f"Verified Android apps: {len(apps)}")
```

## 🗺️ Interactive atlas

The **[GitHub Pages atlas](https://renzo-bd.github.io/global-llm-atlas/)** provides a responsive world view, live metrics, text search, country/service-type/status filters, registration information, capability indicators, operator-country and duplicate metadata, and direct access links.

The **[Android explorer](https://renzo-bd.github.io/global-llm-atlas/android.html)** provides a dedicated view of verified Android access with filters by country and distribution type plus direct official app/download links.

## 🤖 Android curation model

Android availability is intentionally independent from the web lifecycle status of a service. A service may have an official Android app even if its tracked public web access is limited or inactive.

Current Android states are:

- `native`: official native Android app, normally distributed through Google Play or an official product channel;
- `regional`: official Android app distributed through a regional store or region-specific channel;
- `pwa`: installable mobile web/PWA experience, shown separately and not counted as a native Android app;
- `integrated` / `beta`: reserved by the schema for official integrated or beta distribution when independently verified.

Distribution channels are recorded separately (`google-play`, `rustore`, `official-download`, `official-regional`, `web-install`, etc.). Each Android record also carries its own verification date.

## ✅ What qualifies?

An entry should represent a **public conversational AI experience** with its own publicly reachable web interface, free access or a free tier, and usability in English or Spanish under the project's curation criteria.

Repositories-only projects, closed demos, abandoned services and purely private/internal interfaces are outside scope. The initial 0.x series grows conservatively; **v1.0.0 will wait for broader systematic country coverage and normalization.**

## 🧠 Curation model

`country` / `country_es` represents the atlas association supported by the project's evidence. It is not automatically the legal domicile of the operating entity. Where official evidence identifies another jurisdiction, `operator_country` records it separately.

`country_confidence` uses `verified`, `curator-verified`, or `partial`. Uncertainty stays visible rather than being guessed away. Automated reachability is deliberately **non-authoritative**: a successful HTTP response does not prove that a conversational service is usable, and a failed request does not automatically make a service inactive.

## 🔬 Notable findings

- **TextCortex:** two source URLs refer to the same service; the duplicate relationship is preserved rather than hidden. Its Android-access metadata is classified as `pwa`, not native.
- **Kruti:** currently `INACTIVE` for the tracked public web access after recheck on 2026-09-15; mobile availability must be curated independently.
- **IBM Granite Playground:** `LIMITED` because its public demo has a material usage cap.
- **Dola, Qwen and MiniMax:** project/seed association and operating jurisdiction are kept distinct where official terms support it.
- **Public AI:** association confidence is explicitly `partial` because it is a global multi-model platform.
- **Mistral:** the Android app associated with the existing `fr-le-chat` Atlas ID is now branded **Vibe by Mistral**; the Atlas ID remains stable for continuity.

See the [`v0.2.0 curation report`](reports/curation-v0.2.0.md) for the original evidence trail.

## 🤝 Help map the world

The most useful contribution is a service from a **country not yet represented**. Before opening a contribution, check that the service has a real conversational web experience and provide evidence for its country/project association, public/free access, registration requirements and capabilities.

Android corrections are also welcome. Provide an official store/product/download link, distribution channel and the date manually verified.

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for the full rules. Corrections and evidence upgrades are just as welcome as new entries.

If this dataset is useful to your research, project or AI exploration, **⭐ starring the repository helps more people discover it.**

## 🛠️ Maintenance

A weekly GitHub Actions workflow performs basic reachability checks. Suspect results are reported for review rather than directly changing canonical status. Human/semantic review remains required for login walls, regional restrictions, free-tier changes, conversational usability, capability changes, country ambiguity, Android distribution changes and discontinuation.

## 📜 License

MIT — see [`LICENSE`](LICENSE).
