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

## Report a broken or changed entry

Use the **Report broken / changed access** template. Automated HTTP failures are not enough on their own because many AI sites block bots. Please test in a normal browser when possible.

## Status changes

`ACTIVE` should only become `INACTIVE`, `LIMITED` or `DISCONTINUED` after human review.

## Data edits

`data/llms.json` is the canonical source. Keep `data/llms.csv` synchronized.

When adding a new entry:

1. use a stable, unique `id`;
2. preserve uncertainty as `UNVERIFIED`;
3. do not guess capabilities;
4. add the manual verification date;
5. update the changelog when the change is user-visible.

## Versioning

- **PATCH**: corrections, metadata fixes, URL changes.
- **MINOR**: new countries/models/features that remain backward compatible.
- **MAJOR**: schema or policy changes that break consumers.

The first stable release will be `v1.0.0` after a broader audit.
