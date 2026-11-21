# URL review follow-up — issue #19

Reviewed: 2026-10-27 (America/Lima). Original check: 2026-10-26T19:02:03Z.
Original report: [bot report](https://github.com/Renzo-BD/global-llm-atlas/blob/bot/url-check-40382813247/reports/url-check-2026-10-26.md).
Issue: https://github.com/Renzo-BD/global-llm-atlas/issues/19

## Results

| Service | Original alert | Follow-up evidence | Decision |
|---|---|---|---|
| Copuchat | Read timeout | Repeated direct HTTP GET 200, correct title, chat controls and data-collection consent. Search fetch still times out. Official FAQ still links the same URL. | Non-reproduced transport alert; false positive **as evidence of a dead link**. Keep URL and ACTIVE. Successful inference not tested. |
| GuffGPT | HTTP 503 | Repeated direct landing GET 200; official guide links chat.guffgpt.com and requires sign-in; chat GET 200 with app shell. Search fetch initially still returned 503. | Non-reproduced transport alert; false positive **as evidence of closure**. Correct canonical URL to official chat and registration to required; keep UNVERIFIED. |
| Crystal | Hostname error | Repeated direct agent GET 503; search result is an eight-month-old JS shell. Official crystal.ai redirects to Domyn, whose Agents page offers enterprise demo access; Crystal terms describe customer-authorized subscription users. | Access and public/free eligibility unresolved. Do not substitute corporate homepage for chat. Keep historical ACTIVE pending curator browser test; propose LIMITED if restricted access confirmed. |
| Cladik | Hostname error | Repeated apex/about GET 503; www root/chat 530; search root 502. Indexed About content is historical, not live app proof. | Persistent access concern across retrieval attempts; keep UNVERIFIED. No verified replacement. Needs normal-browser/another-network test. |

## Applied corrections

- GuffGPT URL: https://guffgpt.com/ → https://chat.guffgpt.com/ (official landing and guide both link it).
- GuffGPT registration: unknown → required (official guide explicitly requires an account for chat).
- Synchronized JSON/CSV and attached dated provenance to all four entries.
- Preserved lifecycle states, capabilities and last_manual_verification dates. HTTP/source review does not constitute an interactive conversation test.

## Evidence and limitations

- https://latamgpt.org/faq identifies Copuchat as the experimental LatamGPT-SFT interface.
- https://guffgpt.com/ and https://guffgpt.com/journal/how-to-use-guffgpt/ identify the chat endpoint and account flow.
- https://www.domyn.com/agents and https://www.domyn.com/legal/software-licenses/crystal document Crystal's enterprise context.
- https://cladik.com/about and https://www.cladik.com/chat/new preserve service identity and an old indexed route, but that route was not reachable in the direct check.

Checks used public HTTP GET and semantic source review, not an interactive browser session. No account, consent acceptance or prompt submission occurred. The execution environment's local DNS resolution failed for **all four hosts**, including sites that returned HTTP 200 via its configured retrieval proxy; local DNS failures are therefore excluded as evidence of public DNS failure. Retrieval 5xx may originate at the site, its protection layer or the retrieval intermediary. Search-cached pages have explicit age limitations.

## Remaining human intervention

1. Crystal: open the exact agent URL from an ordinary browser in Peru; determine whether an individual can register and use a meaningful free tier. If only enterprise/customer access remains, mark LIMITED with dated evidence. If a replacement chat is offered, use only an officially linked, tested route.
2. Cladik: test apex and officially linked chat from a normal browser/another network. Record the visible error or working flow; do not declare DISCONTINUED without publisher evidence.
3. Copuchat and GuffGPT: no URL repair remains justified by the alert; optional conversation tests can establish backend availability.

Keep issue #19 open until Crystal and Cladik are resolved. This report is a triage result, not a claim that all services work.
