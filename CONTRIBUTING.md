# Contributing to Global LLM Atlas

Thanks for helping keep the atlas accurate.

## Core principle

**Accuracy over size.** Do not add a service simply because a landing page exists.

## Before proposing an entry

A candidate should normally be:

- a conversational LLM/MLLM or AI assistant;
- available through its own public web interface;
- free or have a meaningful free tier;
- usable in English or Spanish;
- currently maintained;
- more than a source-code repository or closed demo.

## Add a model

Use the **Add / suggest a model** issue template and provide:

- product/service name;
- public chat URL;
- country association and why;
- free-access details;
- English/Spanish usability;
- registration requirements;
- date manually tested;
- relevant evidence or notes.

## Android access metadata

Android availability is curated independently from the web lifecycle status of a service.

When proposing or correcting Android metadata, provide:

- the existing Atlas `id`;
- an official Google Play, regional store, product-download or official web-install URL;
- the distribution type;
- the date manually verified;
- a short note when branding or regional availability could be ambiguous.

Allowed Android states are currently:

- `native`: official native Android app;
- `regional`: official Android app distributed through a regional store/channel;
- `pwa`: installable mobile web/PWA experience; not counted as a native app;
- `integrated`: Android availability only through another official host application;
- `beta`: official Android beta distribution.

Do **not** infer `unsupported` from missing Android metadata. If no official evidence has been independently verified, leave the service absent from `data/android.json`.

`data/android.json` and `data/android.csv` must remain synchronized, and entries must validate against `data/android-schema.json`.

## Report a broken or changed entry

Use the **Report broken / changed access** issue template. Automated HTTP failures are not enough on their own because many AI sites block bots. Please test in a normal browser when possible.

For Android changes, verify that the store/download listing belongs to the official product/operator; third-party wrappers and unofficial APK mirrors are outside scope.

## Status changes

`ACTIVE` should only become `INACTIVE`, `LIMITED` or `DISCONTINUED` after human review.

Android `native`, `regional` or `pwa` status does not override the lifecycle status of the tracked web access.

## Data edits

`data/llms.json` is the canonical service source. Keep `data/llms.csv` synchronized.

When adding a new entry:

1. use a stable, unique `id`;
2. preserve uncertainty as `UNVERIFIED`;
3. do not guess capabilities;
4. add the manual verification date;
5. update the changelog when the change is user-visible.

Android metadata uses the same stable Atlas `id` as the canonical service dataset.

## Versioning

- **PATCH**: corrections, metadata fixes, URL changes.
- **MINOR**: new countries/models/features or curated dimensions that remain backward compatible.
- **MAJOR**: schema or policy changes that break consumers.

The first stable release will be `v1.0.0` after a broader audit.
