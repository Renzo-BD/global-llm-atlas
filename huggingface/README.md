---
language:
- en
- es
license: mit
task_categories:
- text-classification
tags:
- llm
- ai-directory
- conversational-ai
- geography
- multimodal
- android
pretty_name: Global LLM Atlas — public conversational AI access
size_categories:
- n<1K
---

# Global LLM Atlas — dataset card

**Source of truth:** https://github.com/Renzo-BD/global-llm-atlas

**Interactive atlas:** https://renzo-bd.github.io/global-llm-atlas/

This directory is **not** a benchmark, leaderboard or dataset of model weights. It is a curated index of **public conversational AI access points**. It separates country/project associations from operator location, and distinguishes service usability evidence from HTTP reachability.

## Current snapshot

Version **0.4.0** (2026-10-22): 88 access points, 87 unique services, including **24 UNVERIFIED candidates**. 42 country/project associations and 37 official native/regional Android app records. Counts and field values change as the source is updated.

## Files for a future Hugging Face dataset repository

Copy `data/llms.csv`, `data/llms.json`, `data/android.csv` and `data/android.json` from the canonical GitHub repository. If desired, host the CSV as `data/train.csv` only for compatibility with generic viewers; **these are catalog records, not training examples**. Do not imply that model outputs were collected.

## Field interpretation

- `id`: stable Atlas identifier, not a model ID.
- `url`: tracked public entry URL, not guaranteed active.
- `country` / `iso2`: evidence-backed association, not necessarily corporate domicile.
- `operator_country`: legal/operating jurisdiction where supported.
- `status`: ACTIVE, LIMITED, UNVERIFIED, INACTIVE or DISCONTINUED, using human review.
- `capability_*`: a blank or null means **not independently verified**, not unsupported.
- `duplicate_of`: intentional cross-list duplicate relationship.
- Android distribution is maintained as **independent** metadata.

## Limitations

The atlas is incomplete and geographically uneven. Free tiers, access, branding, language support and regional restrictions can change rapidly. Twenty-four candidate records were unverified at the 2026-10-22 snapshot; do not treat them as confirmed free-to-use services or proof of proprietary base models. No legal/model-owner claims should be inferred solely from country association.

## Responsible use and updates

Before analysis, filter status and confidence as appropriate; check verification timestamps and official links. Send corrections or new evidence through GitHub Issues: https://github.com/Renzo-BD/global-llm-atlas/issues/new/choose.

**License:** MIT for the repository's original contents. Third-party product names and websites remain their respective owners' property.

## Citation

See `CITATION.cff` in the source repository for citation metadata.

## Publication status

**Prepared for upload; not yet published to Hugging Face.** A Hugging Face account and dataset-repository creation are required.
