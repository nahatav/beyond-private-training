# Venue calendar — canonical

State as of **2026-09-02**. Supersedes the venue tables scattered through `ideas/19`, `ideas/20` and
`ideas/22`. Every row was confirmed by fetching the workshop's own CFP page, not an aggregator.

## The timezone correction — read this first

**`aiworkshoptracker.com` publishes deadlines in UTC. AoE = UTC − 12h.** Verified against four venues
confirmed independently: AIWILD Sep 6 13:00 UTC = Sep 5 AoE; InfPriv Sep 8 12:00 UTC = Sep 7 AoE;
EvoRobust Sep 13 12:29 UTC = Sep 12 AoE; VERICODEGEN Sep 14 11:59 UTC = Sep 13 AoE.

**Consequence: every tracker row reading "Sep 6, 11:59 UTC" is really Sep 5 AoE and is closed.**
That is roughly 25 workshops — ATTRIB, ODI, IAB, Meta-Agents, FAST, Agentic Web, SaTQuML,
AI-Native Academia, TTCL, CWM, BeNTo, PTA and others. The tracker's apparently-open set is far
smaller than it looks.

## Open, with a deadline on or after Sep 5

| Venue | Deadline (AoE) | Format | Concurrent submission | Reviewer fit for AI-control metrics |
|---|---|---|---|---|
| **AIWILD** — 3rd Workshop on Agents in the Wild (NeurIPS, Sydney) | **Sep 5** (extended from Aug 29) | 9pp regular / **4pp short**, non-archival, WIP welcome | **Allowed** — "papers under review or recently accepted at other venues" | **Clean — the only one.** CFP names "Agent safety, alignment, **control**, and oversight" verbatim. Published `2606.30449`, a probes-fail-on-pre-action-monitoring paper. |
| **SLM-Agents** (NeurIPS, Paris) | **Sep 6** (extended from Sep 5) | 4pp short / 6pp long, non-archival | **Restrictive** — barred if under review at or accepted to NeurIPS 2026 main | ⚠️ Moderate mismatch. CFP names "quantization, pruning" and "safety, robustness", but the centre of gravity is on-device efficiency; **would grade a monitor result on efficiency merit, not safety merit.** |
| **InfPriv** — Beyond Private Training (NeurIPS, Sydney) | **Sep 7** | 4pp, non-archival | — | Privacy only. Home of the PE paper (`ideas/14`). |
| **EvoRobust** — Self-Evolving Diversity-Driven Search for Robust AI (NeurIPS, Sydney) | **Sep 12** | **4pp** (5pp camera-ready), non-archival | **Allowed** | ⚠️ Moderate. Robustness-literate, but the spine is quality-diversity *search*; likely no AI-control background. |
| **VERICODEGEN** — AI for Verifiable Coding (NeurIPS, Atlanta) | **Sep 13** (abstract **Sep 11**, not Sep 12) | competition track 4–9pp; research track format unstated ⚠️ | Not stated ⚠️ | ⚠️ Severe. Proof assistants, model checkers, SAT/SMT. Would grade against formal-verification standards. |
| **AI for Peace** (NeurIPS, Paris) | **Sep 14** | Google Form call for *presentations*, non-archival | — | Not a paper venue. |
| **ICLR 2027** | abstract **Sep 18** / full **Sep 25** | full archival conference paper | — | A 4-page measurement is not an ICLR paper. |
| **UniReps** (NeurIPS, Paris) | ~**Sep 25** ⚠️ (tracker only; workshop page still says "TBD AoE") | 9pp archival / **4pp non-archival** extended abstract | Not stated ⚠️ | ⚠️ Severe. Representation-similarity, neuroscience, model merging. |
| **InfPriv fast track** | **Sep 25** | 4pp + NeurIPS reviews appended | — | **Requires NeurIPS 2026 provenance with reviews attached — not available to us.** |
| **IEEE SaTML 2027** | abstract **Sep 22** / full **Sep 29** | full archival conference paper | — | Security; much higher bar. |
| **NeuralArtifacts** (NeurIPS, Paris + remote) | **Sep 6** ⚠️ **unresolved** | not stated ⚠️ | not stated ⚠️ | ⚠️ Severe. Weight-space / model-zoo researchers. |

### The NeuralArtifacts discrepancy, settled as far as it can be

The workshop's own site (`artifactsasdata.org`) says **Sep 1 AoE** with no extension banner and no
Important Dates section; `/call-for-papers` 404s. The OpenReview-synced tracker says **Sep 6 AoE**,
annotated "Extended by 5 days." The gap is a real extension the workshop never propagated to its own
page. OpenReview itself is behind a CAPTCHA and was **not** bypassed. **Do not plan around this venue.**

## Re-check dates

- **Sep 19** — **SaTML 2027 workshops.** SaTML runs workshops for the first time in 2027. Proposals
  closed Aug 28; **organizers are notified Sep 18**, so paper CFPs cannot exist before then. This is
  the highest-value follow-up outside NeurIPS.
- **~Sep 25** — **AAAI-27 workshop list** (proposals closed Aug 28, organizer notification Sep 25;
  workshops Feb 22–23, 2027).
- **Unscheduled** — ICLR 2027 workshops; only the proposal group exists so far.
- ⚠️ **AAAI-27 main conference has an AI Alignment special track** covering scalable oversight,
  mechanistic interpretability, empirical robustness evaluation and red-teaming. Its deadline was
  **not verified** and is likely past for a Feb 2027 conference. Worth one check.

## Closed — recorded so they are not re-checked

| Venue | Closed | Note |
|---|---|---|
| **JUDGe 2026** — "Can We Trust the Judge?" (Atlanta) | **Aug 29** | **The best fit of all, missed by three days.** CFP listed "adversarial robustness of safety evaluators" and "calibration methods for LLM judges." Organizers: Sushmita (Northeastern/UW), Koshal (Meta/Northeastern), Makhija (Amazon), Wan (GDM), Abu-Jbara (Amazon Ads); keynote Eugene Yan (Anthropic). No published ownership of the threshold line — **G2 clear**, but the community is active here. |
| Evaluation of Interactive Agents | Aug 29 | 9pp/4pp. Strong topical fit, missed. |
| Child Safety in AI | Aug 29 | — |
| Resource-Aware Agentic AI | Aug 29 | 8pp. Compute/energy/API-call efficiency for agents. |
| Trustworthy AI Evaluation (TAI-Eval) | Aug 29 | — |
| Who Verifies the Agents? | Aug 29 | Agent oversight/control — direct fit, missed. |
| FLMSec — Foundations of Language Model Security | Aug 27 | — |
| InterpScience — Interpretability as a Science | Sep 1 | — |
| PriLOM — Privacy in the Era of Large Opaque Models | Sep 4 | — |
| ODI — On-Device Intelligence | Sep 5 | Quantization's home venue. |
| ATTRIB, IAB, Meta-Agents, FAST, Pre-to-Post, FLLMPT, Agentic Web, SaTQuML, TTCL, CWM, BeNTo, PTA, AI-Native Academia | Sep 5 | The UTC/AoE cohort above. |
| LIGHT (Deployable Small Foundation Models), AXIOM (Foundations of Efficient Deep Learning) | before Sep 5 | Both efficiency-focused. |
| AIMS — AI Measurement Science @ COLM 2026 | **Jun 23** | Topically near-perfect (measurement under strategic optimization; evaluation as an evaluator/learner game). **Note for 2027.** |

## Lessons for the next round's venue sweep

1. **Check judge / evaluator / measurement workshops early.** JUDGe and AIMS were the two best fits
   in the entire calendar and both closed before the sweep ran.
2. **Never trust an aggregator's timezone.** Confirm on the workshop's own page, and expect the
   workshop's page itself to be stale when OpenReview has been extended.
3. **Reviewer background is a first-class selection criterion**, not a tiebreaker. A venue that
   grades a safety result on efficiency merit actively damages objective (2).
4. Most NeurIPS workshop deadlines cluster on the *suggested* date (Aug 29) and then extend once by
   ~1 week. A sweep run in early August would have caught roughly ten more viable venues.
