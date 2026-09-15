# Android curation report — 2026-09-15

This report documents the first curated Android-access layer for **Global LLM Atlas**.

## Scope

Android metadata is keyed to existing stable Atlas IDs and does not replace or modify the lifecycle status of the tracked public web access.

A service is listed in `data/android.json` only when a current official product, store or download source supports the Android claim. Missing metadata means **not independently verified**, never unsupported.

## Classification

- `native` — official native Android application.
- `regional` — official Android application distributed through a regional store or region-specific official channel.
- `pwa` — installable mobile web/PWA experience; shown separately and not counted as a native Android app.
- `integrated` / `beta` — schema-reserved states for future independently verified cases.

## Current conservative seed

- 25 unique services with verified `native` or `regional` Android apps.
- 1 unique service (TextCortex) represented as `pwa`.
- 27 Android metadata access-point records in total because TextCortex has two Atlas access-point IDs referring to the same underlying service.

## Native / official Android app IDs

- `at-comfyai`
- `br-maritaca`
- `bg-bggpt`
- `cn-deepseek`
- `cn-kimi-ai`
- `cn-manus`
- `cn-minimax`
- `cn-qwen`
- `es-luzia`
- `fr-le-chat` (current Android branding: Vibe by Mistral)
- `jp-felo`
- `ru-alice-yandex`
- `ch-lumo`
- `us-chatgpt`
- `us-claude`
- `us-gemini`
- `us-grok`
- `us-meta-ai`
- `us-notebooklm`
- `us-perplexity`
- `us-pi`
- `us-venice`
- `us-you-com`

## Regional official Android distribution

- `cn-ernie` — recorded conservatively as regional official distribution.
- `ru-gigachat` — official Android distribution through RuStore.

## PWA / installable web

- `de-textcortex`
- `us-textcortex` — duplicate Atlas access point for the same TextCortex service.

## Exclusions

The Android seed intentionally excludes:

- third-party wrappers;
- unofficial APK mirrors;
- apps with ambiguous publisher identity;
- search results without sufficiently clear official provenance;
- inferred Android support based only on mobile-responsive web access.

## Data files

- `data/android.json` — structured Android metadata.
- `data/android.csv` — flat export.
- `data/android-schema.json` — validation schema.
- `android.html` — GitHub Pages explorer.

Future platform work should reuse stable Atlas IDs and preserve this separation between web lifecycle status and platform availability.
