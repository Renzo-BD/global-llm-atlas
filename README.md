# 🌐 Global LLM Atlas

> A curated, versioned atlas of **public conversational LLM/MLLM web experiences around the world**.

[![Version](https://img.shields.io/badge/version-v0.1.0-blue)](CHANGELOG.md)
![Entries](https://img.shields.io/badge/verified%20access%20points-57-2ea44f)
![Countries](https://img.shields.io/badge/countries-25-7b61ff)
![Maintenance](https://img.shields.io/badge/check-weekly-orange)

**Global LLM Atlas** is not intended to be another static list of AI links. It is designed as a **curated dataset + interactive directory + maintenance workflow** that records what exists, where it is associated geographically, whether the public web access is working, and when it was last checked.

**Español:** directorio mundial curado y versionado de LLM/MLLM conversacionales con acceso web público. La versión inicial incluye únicamente los accesos que el curador comprobó manualmente. La carpeta **“MULTI MODELOS” fue excluida expresamente**.

## ✨ v0.1.0 — Curated Seed

- **57** manually tested public web access points
- **25** countries
- Entries imported only from the curator-provided HTML bookmark export
- `MULTI MODELOS` excluded
- Every seed entry starts as `ACTIVE` with manual verification date **2026-09-10**
- Image, voice and registration fields remain `UNVERIFIED` until separately checked
- Automated URL checks are deliberately **non-authoritative**: a bot may flag an access point as suspect, but it does not silently mark it inactive

> **Important:** an HTTP response alone does not prove that a conversational model is actually usable. Automated checks are only an early-warning layer. Human/semantic verification remains required.

## 🧭 Interactive atlas

The repository includes a responsive web interface in [`index.html`](index.html) with:

- search
- continent/country/status filters
- live metrics
- country flags
- interactive world map
- direct access buttons
- clear distinction between verified and still-unverified attributes

Once GitHub Pages is enabled, the atlas can be published directly from this repository.

## 📦 Data

The canonical source of truth is [`data/llms.json`](data/llms.json). A spreadsheet-friendly export is available at [`data/llms.csv`](data/llms.csv).

Status vocabulary:

| Status | Meaning |
|---|---|
| `ACTIVE` | Manually verified as working |
| `LIMITED` | Accessible but with material restrictions |
| `UNVERIFIED` | Not yet manually checked |
| `INACTIVE` | Confirmed unavailable after human review |
| `DISCONTINUED` | Project/service confirmed discontinued |

## 🌍 Directory

Legend: ✅ = supported by the inclusion criteria; `?` = not yet independently verified.

### 🌍 Africa
#### 🇲🇦 Morocco / Marruecos
| Service | Web | Text | Image | Voice | Registration | Status | Last verified |
|---|---|---|---|---|---|---|---|
| ChatyfAI | [Open](https://chatyfai.com/en/chat) | ✅ | ? | ? | ? | 🟢 ACTIVE | 2026-09-10 |

### 🌏 Asia
#### 🇨🇳 China / China
| Service | Web | Text | Image | Voice | Registration | Status | Last verified |
|---|---|---|---|---|---|---|---|
| DeepSeek | [Open](https://chat.deepseek.com/) | ✅ | ? | ? | ? | 🟢 ACTIVE | 2026-09-10 |
| Dola | [Open](https://www.dola.com/chat) | ✅ | ? | ? | ? | 🟢 ACTIVE | 2026-09-10 |
| ERNIE | [Open](https://ernie.baidu.com/) | ✅ | ? | ? | ? | 🟢 ACTIVE | 2026-09-10 |
| Kimi AI | [Open](https://www.kimi.com/chat/history) | ✅ | ? | ? | ? | 🟢 ACTIVE | 2026-09-10 |
| Manus | [Open](https://manus.im/app) | ✅ | ? | ? | ? | 🟢 ACTIVE | 2026-09-10 |
| MiniMax | [Open](https://www.minimax.io/) | ✅ | ? | ? | ? | 🟢 ACTIVE | 2026-09-10 |
| Qwen | [Open](https://chat.qwen.ai/) | ✅ | ? | ? | ? | 🟢 ACTIVE | 2026-09-10 |
| Xiaomi MiMo Studio | [Open](https://aistudio.xiaomimimo.com/#/chat/c9145824a5e81376af0c62cfa2c1ef87) | ✅ | ? | ? | ? | 🟢 ACTIVE | 2026-09-10 |
| Z.ai | [Open](https://chat.z.ai/) | ✅ | ? | ? | ? | 🟢 ACTIVE | 2026-09-10 |
| Tencent AI Studio | [Open](https://aistudio.tencent.com/) | ✅ | ? | ? | ? | 🟢 ACTIVE | 2026-09-10 |
| Tencent AI Studio International | [Open](https://aistudio.tencent.ai/) | ✅ | ? | ? | ? | 🟢 ACTIVE | 2026-09-10 |

#### 🇮🇳 India / India
| Service | Web | Text | Image | Voice | Registration | Status | Last verified |
|---|---|---|---|---|---|---|---|
| Kruti | [Open](https://www.kruti.ai/) | ✅ | ? | ? | ? | 🟢 ACTIVE | 2026-09-10 |

#### 🇮🇩 Indonesia / Indonesia
| Service | Web | Text | Image | Voice | Registration | Status | Last verified |
|---|---|---|---|---|---|---|---|
| Sahabat-AI | [Open](https://chat.sahabat-ai.com/dashboard) | ✅ | ? | ? | ? | 🟢 ACTIVE | 2026-09-10 |

#### 🇯🇵 Japan / Japón
| Service | Web | Text | Image | Voice | Registration | Status | Last verified |
|---|---|---|---|---|---|---|---|
| Felo | [Open](https://felo.ai/es/search) | ✅ | ? | ? | ? | 🟢 ACTIVE | 2026-09-10 |

#### 🇸🇬 Singapore / Singapur
| Service | Web | Text | Image | Voice | Registration | Status | Last verified |
|---|---|---|---|---|---|---|---|
| SEA-LION Playground | [Open](https://playground.sea-lion.ai/chat) | ✅ | ? | ? | ? | 🟢 ACTIVE | 2026-09-10 |

#### 🇦🇪 United Arab Emirates / Emiratos Árabes Unidos
| Service | Web | Text | Image | Voice | Registration | Status | Last verified |
|---|---|---|---|---|---|---|---|
| Falcon LLM Chat | [Open](https://chat.falconllm.tii.ae/anonymous-chat) | ✅ | ? | ? | ? | 🟢 ACTIVE | 2026-09-10 |

#### 🇺🇿 Uzbekistan / Uzbekistán
| Service | Web | Text | Image | Voice | Registration | Status | Last verified |
|---|---|---|---|---|---|---|---|
| CoreAI Chat | [Open](https://chat.coreai.uz/) | ✅ | ? | ? | ? | 🟢 ACTIVE | 2026-09-10 |

### 🌍 Europe
#### 🇦🇹 Austria / Austria
| Service | Web | Text | Image | Voice | Registration | Status | Last verified |
|---|---|---|---|---|---|---|---|
| ComfyAI | [Open](https://comfyai.de/app/) | ✅ | ? | ? | ? | 🟢 ACTIVE | 2026-09-10 |

#### 🇧🇬 Bulgaria / Bulgaria
| Service | Web | Text | Image | Voice | Registration | Status | Last verified |
|---|---|---|---|---|---|---|---|
| BgGPT | [Open](https://bggpt.ai/?utm_source=chatgpt.com) | ✅ | ? | ? | ? | 🟢 ACTIVE | 2026-09-10 |

#### 🇫🇷 France / Francia
| Service | Web | Text | Image | Voice | Registration | Status | Last verified |
|---|---|---|---|---|---|---|---|
| Le Chat | [Open](https://chat.mistral.ai/chat) | ✅ | ? | ? | ? | 🟢 ACTIVE | 2026-09-10 |

#### 🇩🇪 Germany / Alemania
| Service | Web | Text | Image | Voice | Registration | Status | Last verified |
|---|---|---|---|---|---|---|---|
| TextCortex | [Open](https://app.textcortex.com/c) | ✅ | ? | ? | ? | 🟢 ACTIVE | 2026-09-10 |
| PrivateMode Chat | [Open](https://chat.privatemode.ai/?utm_source=chatgpt.com) | ✅ | ? | ? | ? | 🟢 ACTIVE | 2026-09-10 |

#### 🇮🇹 Italy / Italia
| Service | Web | Text | Image | Voice | Registration | Status | Last verified |
|---|---|---|---|---|---|---|---|
| Crystal | [Open](https://agent.crystal.ai/) | ✅ | ? | ? | ? | 🟢 ACTIVE | 2026-09-10 |
| ChatMinerva | [Open](https://chatminerva.org/) | ✅ | ? | ? | ? | 🟢 ACTIVE | 2026-09-10 |

#### 🇳🇱 Netherlands / Países Bajos
| Service | Web | Text | Image | Voice | Registration | Status | Last verified |
|---|---|---|---|---|---|---|---|
| Loes | [Open](https://chat.loes.ai/?utm_source=chatgpt.com) | ✅ | ? | ? | ? | 🟢 ACTIVE | 2026-09-10 |

#### 🇳🇴 Norway / Noruega
| Service | Web | Text | Image | Voice | Registration | Status | Last verified |
|---|---|---|---|---|---|---|---|
| Bineric Chat | [Open](https://chat.bineric.com/) | ✅ | ? | ? | ? | 🟢 ACTIVE | 2026-09-10 |

#### 🇵🇱 Poland / Polonia
| Service | Web | Text | Image | Voice | Registration | Status | Last verified |
|---|---|---|---|---|---|---|---|
| PLLuM Chat | [Open](https://pllum.clarin-pl.eu/pllum_8x7b) | ✅ | ? | ? | ? | 🟢 ACTIVE | 2026-09-10 |

#### 🇪🇸 Spain / España
| Service | Web | Text | Image | Voice | Registration | Status | Last verified |
|---|---|---|---|---|---|---|---|
| Luzia | [Open](https://chat.luzia.com/es) | ✅ | ? | ? | ? | 🟢 ACTIVE | 2026-09-10 |

#### 🇨🇭 Switzerland / Suiza
| Service | Web | Text | Image | Voice | Registration | Status | Last verified |
|---|---|---|---|---|---|---|---|
| Lumo | [Open](https://lumo.proton.me/u/1/?welcome=true) | ✅ | ? | ? | ? | 🟢 ACTIVE | 2026-09-10 |
| Public AI | [Open](https://chat.publicai.co/) | ✅ | ? | ? | ? | 🟢 ACTIVE | 2026-09-10 |

### 🌐 Europe / Asia
#### 🇷🇺 Russia / Rusia
| Service | Web | Text | Image | Voice | Registration | Status | Last verified |
|---|---|---|---|---|---|---|---|
| Alice (Yandex) | [Open](https://alice.yandex.ru/?utm_source=yagpt_land&utm_campaign=button) | ✅ | ? | ? | ? | 🟢 ACTIVE | 2026-09-10 |
| GigaChat | [Open](https://giga.chat/sessions/019fd25d-5f69-7ee1-9dc8-dc3ab43effd0) | ✅ | ? | ? | ? | 🟢 ACTIVE | 2026-09-10 |

### 🌎 North America
#### 🇨🇦 Canada / Canadá
| Service | Web | Text | Image | Voice | Registration | Status | Last verified |
|---|---|---|---|---|---|---|---|
| Cohere | [Open](https://dashboard.cohere.com/playground/chat) | ✅ | ? | ? | ? | 🟢 ACTIVE | 2026-09-10 |
| Chat Jimmy | [Open](https://chatjimmy.ai/) | ✅ | ? | ? | ? | 🟢 ACTIVE | 2026-09-10 |
| Augure | [Open](https://chat.augureai.ca/chat) | ✅ | ? | ? | ? | 🟢 ACTIVE | 2026-09-10 |

#### 🇺🇸 United States / Estados Unidos
| Service | Web | Text | Image | Voice | Registration | Status | Last verified |
|---|---|---|---|---|---|---|---|
| ChatGPT | [Open](https://chatgpt.com/) | ✅ | ? | ? | ? | 🟢 ACTIVE | 2026-09-10 |
| Claude | [Open](https://claude.ai/new) | ✅ | ? | ? | ? | 🟢 ACTIVE | 2026-09-10 |
| Copilot | [Open](https://copilot.microsoft.com/) | ✅ | ? | ? | ? | 🟢 ACTIVE | 2026-09-10 |
| Gemini | [Open](https://gemini.google.com/app) | ✅ | ? | ? | ? | 🟢 ACTIVE | 2026-09-10 |
| Google AI Studio | [Open](https://aistudio.google.com/generate-speech) | ✅ | ? | ? | ? | 🟢 ACTIVE | 2026-09-10 |
| Grok | [Open](https://grok.com/) | ✅ | ? | ? | ? | 🟢 ACTIVE | 2026-09-10 |
| IBM Granite Playground | [Open](https://www.ibm.com/granite/playground) | ✅ | ? | ? | ? | 🟢 ACTIVE | 2026-09-10 |
| Laguna | [Open](https://chat.poolside.ai/) | ✅ | ? | ? | ? | 🟢 ACTIVE | 2026-09-10 |
| Meta AI | [Open](https://www.meta.ai/?nr=1) | ✅ | ? | ? | ? | 🟢 ACTIVE | 2026-09-10 |
| Monkey Code | [Open](https://monkeycode-ai.net/console/task/11809376-a768-4a58-a68f-384112667aac) | ✅ | ? | ? | ? | 🟢 ACTIVE | 2026-09-10 |
| Morphic | [Open](https://chat.morphic.sh/) | ✅ | ? | ? | ? | 🟢 ACTIVE | 2026-09-10 |
| NotebookLM | [Open](https://notebooklm.google.com/) | ✅ | ? | ? | ? | 🟢 ACTIVE | 2026-09-10 |
| Perplexity | [Open](https://www.perplexity.ai/) | ✅ | ? | ? | ? | 🟢 ACTIVE | 2026-09-10 |
| Pi | [Open](https://pi.ai/onboarding) | ✅ | ? | ? | ? | 🟢 ACTIVE | 2026-09-10 |
| TextCortex | [Open](https://app.textcortex.com/user/dashboard/chat) | ✅ | ? | ? | ? | 🟢 ACTIVE | 2026-09-10 |
| Venice | [Open](https://venice.ai/chat) | ✅ | ? | ? | ? | 🟢 ACTIVE | 2026-09-10 |
| You.com | [Open](https://you.com/?) | ✅ | ? | ? | ? | 🟢 ACTIVE | 2026-09-10 |

### 🌎 South America
#### 🇦🇷 Argentina / Argentina
| Service | Web | Text | Image | Voice | Registration | Status | Last verified |
|---|---|---|---|---|---|---|---|
| Aki Agent | [Open](https://aki.ar/projects?projectId=3672) | ✅ | ? | ? | ? | 🟢 ACTIVE | 2026-09-10 |

#### 🇧🇷 Brazil / Brasil
| Service | Web | Text | Image | Voice | Registration | Status | Last verified |
|---|---|---|---|---|---|---|---|
| Maritaca | [Open](https://chat.maritaca.ai/) | ✅ | ? | ? | ? | 🟢 ACTIVE | 2026-09-10 |

#### 🇨🇱 Chile / Chile
| Service | Web | Text | Image | Voice | Registration | Status | Last verified |
|---|---|---|---|---|---|---|---|
| Copuchat | [Open](https://copuchat.latamgpt.org/?utm_source=chatgpt.com) | ✅ | ? | ? | ? | 🟢 ACTIVE | 2026-09-10 |

#### 🇪🇨 Ecuador / Ecuador
| Service | Web | Text | Image | Voice | Registration | Status | Last verified |
|---|---|---|---|---|---|---|---|
| YACHAQ AI | [Open](https://yachaq.ai/?utm_source=chatgpt.com) | ✅ | ? | ? | ? | 🟢 ACTIVE | 2026-09-10 |

## 🔄 Maintenance model

A scheduled GitHub Action runs weekly. It performs lightweight web reachability checks and classifies suspicious results conservatively. `401`, `403` and `429` are treated as **guarded/restricted responses**, not automatic outages, because many AI sites block bots while remaining usable in a browser.

If a likely outage is detected, the workflow generates a dated report and attempts to open a review pull request. Human verification is required before changing `ACTIVE` to another status.

## 🧪 Inclusion criteria

An entry should normally satisfy all of the following:

1. Conversational LLM/MLLM or AI assistant.
2. Publicly accessible web page of its own.
3. Free access or a meaningful free tier.
4. Usable in English or Spanish.
5. Not merely a source-code repository.
6. Not a closed demo.
7. Not knowingly abandoned or discontinued.

## 🗂️ Repository structure

```text
.
├── data/
│   ├── llms.json
│   ├── llms.csv
│   └── schema.json
├── reports/
│   └── coverage-v0.1.0.md
├── scripts/
│   └── check_urls.py
├── .github/
│   ├── ISSUE_TEMPLATE/
│   └── workflows/
├── index.html
├── CONTRIBUTING.md
└── CHANGELOG.md
```

## 🤝 Contributing

Corrections and additions are welcome, but every proposal must include enough evidence to verify the public conversational access. See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## 🧠 Data quality policy

Accuracy is preferred over raw size. Country attribution, capabilities and service status can change. Ambiguous cases remain explicitly marked instead of being guessed.

This project is currently in **pre-1.0 curation**. `v1.0.0` will only be published after a broader normalization and verification pass.
