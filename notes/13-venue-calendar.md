# Venue calendar — canonical

State as of **2026-09-02**. Supersedes the venue tables scattered through `ideas/19`, `ideas/20` and
`ideas/22`. Every row was confirmed by fetching the workshop's own CFP page, not an aggregator.

## The timezone correction — read this first

**`aiworkshoptracker.com` publishes deadlines in UTC. AoE = UTC − 12h.** Verified against four venues
confirmed independently: AIWILD Sep 6 13:00 UTC = Sep 5 AoE; InfPriv Sep 8 12:00 UTC = Sep 7 AoE;
EvoRobust Sep 13 12:29 UTC = Sep 12 AoE; VERICODEGEN Sep 14 11:59 UTC = Sep 13 AoE.

**Consequence: every tracker row reading "Sep 6, 11:59 UTC" is really Sep 5 AoE.** That is roughly
25 workshops — ATTRIB, ODI, IAB, Meta-Agents, FAST, Agentic Web, SaTQuML, AI-Native Academia, TTCL,
CWM, BeNTo, PTA and others.

> ### ⛔ CORRECTED 2026-09-02 (round 15) — this cohort is NOT closed
> The sentence above originally ended *"and is closed,"* and the table at the foot of this file files
> all ~25 under **Closed**. **Sep 5 AoE is three days in the future, not in the past.** The same
> document lists **AIWILD at that identical instant** as the live Branch A target, so the calendar
> asserted open and closed for one deadline on one page.
>
> The timezone correction is right; the conclusion drawn from it is not. AoE is *later* than the UTC
> timestamp, so the correction **opens** these rows by ~12 hours — it does not shut them. Reading
> "Sep 6 UTC" as past on Sep 2 is a plain date error wearing a timezone argument's clothes.
>
> **`IAB — Interpreting Agent Behavior` (NeurIPS 2026, Sydney) is open, deadline Sep 6 11:59 UTC**
> (`iab-agents.github.io`, ✅ fetched). *Interpretability applied to agent behaviour* is a **better
> topical fit for a probing paper than EvoRobust**, whose PC is evolutionary-computation and CV
> robustness (`ideas/27` §5). It was written off without its CFP being fetched — the exact failure
> **R13** was written to prevent, one round earlier.
>
> **Owed:** fetch the CFP topic list, page limit, archival status and organizer list for IAB and for
> the rest of this cohort before treating any of them as unavailable. Ruling a venue out is the
> stronger claim (R13) and none of these ~25 rows has the evidence for it.

## Open, with a deadline on or after Sep 5

| Venue | Deadline (AoE) | Format | Concurrent submission | Reviewer fit for AI-control metrics |
|---|---|---|---|---|
| **AIWILD** — 3rd Workshop on Agents in the Wild (NeurIPS, Sydney) | **Sep 5** (extended from Aug 29) | 9pp regular / **4pp short**, non-archival, WIP welcome | **Allowed** — "papers under review or recently accepted at other venues" | **Clean — the only one.** CFP names "Agent safety, alignment, **control**, and oversight" verbatim. Published `2606.30449`, a probes-fail-on-pre-action-monitoring paper. Re-verified 2026-09-02: Sep 5 AoE extension, 9pp/4pp tracks and the concurrent-submission clause all confirmed on the workshop's own page. The same page **discourages** submissions from the NeurIPS/ICLR/ICML main tracks. ★ **CONDITIONALLY REOPENED 2026-09-02** — `ideas/24`'s "passes deliberately" was an argument about *C1*. `notes/16` Branch A submits the **determinism note** here iff the Sep 3 gate day comes back green: publishing the insight establishes priority, where silence while the competitor holds the harness does not. |
| **SLM-Agents** (NeurIPS, Paris) | **Sep 6** (extended from Sep 5) | 4pp short / 6pp long, non-archival | **Restrictive** — barred if under review at or accepted to NeurIPS 2026 main | ⚠️ Moderate mismatch. CFP names "quantization, pruning" and "safety, robustness", but the centre of gravity is on-device efficiency; **would grade a monitor result on efficiency merit, not safety merit.** |
| **InfPriv** — Beyond Private Training (NeurIPS, Sydney) | **Sep 7** | 4pp, non-archival | — | Privacy only. Home of the PE paper (`ideas/14`). ★ **ACTIVE — see `notes/15`.** `ideas/24`'s venue plan jumped Sep 5 → Sep 19 and dropped this row without deciding anything. Round 13 decided not to send *C1* to AIWILD; it never re-decided InfPriv. The paper is written, twice-reviewed, ~$30, and the alternative is no submission until roughly November. |
| **EvoRobust** — Self-Evolving Diversity-Driven Search for Robust AI **Systems** (NeurIPS, Sydney) | **Sep 12** | **4pp** (5pp camera-ready), non-archival, 50MB | **Allowed** — "under review… or recently accepted without published proceedings" | ★★ **RE-GRADED 2026-09-02, CFP fetched — the old ⚠️ was read off the title.** Five topic areas, and **two name our objects**: *"**Agentic Safety & Interactive Robustness**: safety of tool-using agents, long-horizon failures, multi-agent risks, **human oversight and controllability**"* and *"**Benchmarks and Governance**: continuously evolving safety benchmarks, **automated test case generation**, coverage metrics"*. Also "Safety Scenario Search & Failure Discovery" (novel failure modes, evolutionary safety evaluation), "Novelty Search & Quality-Diversity for Robustness" (behavioral repertoires of failures **and defenses**), "Multi-Objective Trustworthy AI". Speakers include **Maksym Andriushchenko** (adaptive attacks, AgentHarm), **David Wagner**, **Hamed Hassani**, **Bo Han**; organizers include **Moosavi-Dezfooli** (adversarial robustness) alongside evolutionary-computation people (**Yew-Soon Ong**, Escalera). Not AI-control natives, but robustness-literate and adaptive-attack-literate. **Best open safety venue on the calendar.** |
| **VERICODEGEN** — AI for Verifiable Coding (NeurIPS, Atlanta) | **Sep 13** (abstract **Sep 11**, not Sep 12) | competition track 4–9pp; research track format unstated ⚠️ | Not stated ⚠️ | ⚠️ Severe. Proof assistants, model checkers, SAT/SMT. Would grade against formal-verification standards. |
| **AI for Peace** (NeurIPS, Paris) | **Sep 14** | Google Form call for *presentations*, non-archival | — | Not a paper venue. |
| **ICLR 2027** | abstract **Sep 18** / full **Sep 25** | full archival conference paper | — | A 4-page measurement is not an ICLR paper. |
| **UniReps** (NeurIPS, Paris) | ~**Sep 25** ⚠️ (tracker only; workshop page still says "TBD AoE") | 9pp archival / **4pp non-archival** extended abstract | Not stated ⚠️ | ⚠️ Severe. Representation-similarity, neuroscience, model merging. |
| **InfPriv fast track** | **Sep 25** | 4pp + NeurIPS reviews appended | — | **Requires NeurIPS 2026 provenance with reviews attached — not available to us.** |
| **IEEE SaTML 2027** | abstract **Sep 22** / full **Sep 29** | full archival conference paper | — | Security; much higher bar. |
| **NeuralArtifacts** (NeurIPS, Paris + remote) | **Sep 6** ⚠️ **unresolved** | not stated ⚠️ | not stated ⚠️ | ⚠️ Severe. Weight-space / model-zoo researchers. |

> ### ⛔ CORRECTED 2026-09-02 (round 16) — two rows in this table are wrong
> Both fetched from the workshop's own page.
>
> **NeuralArtifacts is LIVE at Sep 9 AoE.** Its CFP now shows the extension as a strikethrough —
> `~~September 1, 2026 (Anywhere on Earth)~~ **September 9, 2026 (Anywhere on Earth)**` — resolving the
> discrepancy below in favour of the tracker. Extended abstracts **4–6 pp**, full papers 8–12 pp, *"All
> submissions are non-archival."* Scope names *"Interpretability through weights, activations,
> representations, gradients, and other traces"* and *"Model safety and reliability interventions."*
> ⚠️ The **reviewer-fit** ⚠️ below still stands — the community is weight-space / model-zoo.
>
> **FLLMPT is a Sep 12 venue, not a Sep 5 one.** It was misfiled into the Sep 5 cohort. Its own page:
> abstract registration **2026/09/05 23:00 GMT (mandatory)**, paper **2026/09/12 23:00 GMT**, marked
> *"Firm deadline"*, non-archival, dual submission welcome *"including work previously published,
> provided it has been updated or recontextualised."* ⚠️ **GMT, not AoE — 13 h earlier than EvoRobust.**
> CFP names *"ML theory, reinforcement learning, and **AI safety**"* and *"**safety-critical settings**,
> where unintended regressions or feedback loops may arise."* Fit is post-training, so weaker than
> EvoRobust for a monitoring paper — but the abstract costs a title and an abstract.

### The NeuralArtifacts discrepancy, settled as far as it can be

The workshop's own site (`artifactsasdata.org`) says **Sep 1 AoE** with no extension banner and no
Important Dates section; `/call-for-papers` 404s. The OpenReview-synced tracker says **Sep 6 AoE**,
annotated "Extended by 5 days." The gap is a real extension the workshop never propagated to its own
page. OpenReview itself is behind a CAPTCHA and was **not** bypassed. **Do not plan around this venue.**

## The November window — added round 16, every date off the venue's own page

`ideas/24`'s *"nothing until roughly November"* is a **real, dated and populated window**, not a void.
This is what makes missing a September deadline cost **7–11 weeks** rather than silence, and it is the
reason `notes/18` moves C9 off Sep 12 rather than rushing it.

| Venue | Deadline ✅ | Format | Fit |
|---|---|---|---|
| **SaTML 2027** main | abstract **Sep 22** / paper **Sep 29**, 11:59 PM AoE | up to 12 pp body, **archival** (IEEE proceedings). No dual submission. | *"Novel attacks"*, *"Novel defenses"*, *"Verification of algorithms and systems"*, *"Fairness and interpretability"*. ⚠️ PC chairs not published; `/organizers/` 404s. |
| **FAccT 2027** | abstract **Oct 27** / paper **Nov 3**, 11:59 PM AoE | ≤14 pp; **both archival and non-archival options**, chosen at submission and not switchable | *"**AI red teaming and adversarial testing**"*, *"**Interpretability/explainability**"*, *"Science of responsible, safe, ethical, and trustworthy AI evaluation"*, *"audits of systems"*. **The best-fitting open venue in the window.** |
| **AAAI-27 workshops** | **Nov 20**, AoE (workshop submissions due to organizers) | per workshop; AAAI no longer publishes centralized workshop proceedings | Workshop list **not yet public** — organizers notified **Sep 25**, their CFPs due to AAAI **Oct 2**. Historically the densest concentration of safety/alignment workshops in this window. |
| **SaTML 2027 workshops** | CFPs ~**Oct–Dec** | unknown | First SaTML workshop edition. Organizers notified **Sep 18**. |
| **ARR October cycle** → NAACL/COLING 2027 | **Oct 12** | ACL format, archival via committed venue | General NLP; safety/interpretability routinely accepted. |

**Two side-doors that are closed to us, checked so they are not re-checked:** **IAB's "submission with
NeurIPS reviews" route (Oct 1)** and **InfPriv's fast track (Sep 25)** both **require an existing NeurIPS
2026 main-conference submission with its reviews appended.** Neither is reachable from here. ✅

**⚠️ AAAI-27 AI Alignment special track: the deadline was Aug 21, 2026 — passed.** ✅ Its topic list
(*"Scalable oversight and control"*, *"Interpretability"*, *"Robustness and security"*, *"Evaluation"*) is
a near-exact match for this repo's brief. **Note it for 2028.**

## Re-check dates

- **Sep 19** — **SaTML 2027 workshops.** ★ Primary target for the C9 lead (`ideas/24`, amended by
  `ideas/25`). SaTML runs workshops for the first time in 2027. Proposals closed Aug 28; **organizers
  are notified Sep 18**, so paper CFPs cannot exist before then. Re-verified on satml.org 2026-09-02.
  **⚠️ Sep 19 is a notification date, not a deadline.** `ideas/24` scheduled C9 against it as though
  it were one. Paper deadlines follow the CFPs, and for a conference running in early 2027 they are
  plausibly **6–10 weeks out** — an inference from the conference timeline, *not verified*, to be
  confirmed on satml.org on Sep 19. Consequence: C9's "~9 days" binds nothing, the only real pressure
  is scoop pressure, and the surplus budget should buy a second scenario domain (`ideas/25` §5).
  Also run **G2** that day — it is unrunnable until the organizer list exists (`notes/11`).
### Venues the "canonical" calendar was missing, resolved 2026-09-02

The round-12/13 sweeps built this table from a filtered view and missed live rows. Checked against
the OpenReview-synced tracker and then each workshop's own page:

| Venue | Tracker | Verdict |
|---|---|---|
| **AgenticLS** | Sep 20 07:00 UTC = **Sep 19 AoE** | ❌ **Out of scope.** *Agentic AI for **Biological Discovery*** — proteins, genomes, single cells, lab robotics. Not an agent-safety venue despite the name. |
| **PriGM** | Sep 9 12:00 UTC = **Sep 8 AoE** ⚠️ (own site says Sep 5 22:00 UTC — the NeuralArtifacts stale-page pattern again) | ❌ **Not a privacy venue.** *2nd Workshop on **Principles of Generative Modeling***. "Pri" = Principles. Theory of generative models; DP synthetic data is not named in scope. Does **not** give the PE paper a second window after InfPriv. |
| NeuralArtifacts | Sep 7 11:59 UTC = **Sep 6 AoE** | Confirms the extension the workshop's own page never propagated. Still do not plan around it. |

**Lesson 5, added:** the tracker's *list* is more complete than any sweep we have run, even though its
*timezones* are wrong. Use it for coverage and the workshop's own page for dates — never the reverse.

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
| ~~ATTRIB, IAB, Meta-Agents, FAST, Pre-to-Post, Agentic Web, SaTQuML, TTCL, CWM, BeNTo, PTA, AI-Native Academia~~ | ~~Sep 5~~ | ⛔ **MISFILED — see the corrected box above.** Deadline is **Sep 5 AoE**, not past. **FLLMPT is removed from this row: it is a Sep 12 venue.** All twelve CFPs were fetched in round 16; several fit a monitoring paper **better than EvoRobust** — **Meta-Agents** (*"Misalignment and Safety for Meta-Agents"*, *"Governance and Human Oversight"*), **FAST** (*"Evaluation, detection, and bounding of emergent capabilities or failure modes"*, *"Observability and steerability of agent populations"*), **IAB**, **ATTRIB**, **TTCL**. None was reachable with zero experiment code. **This is the cost of the misfiling, and it is the lesson for the next cycle: sweep venues in early August.** |
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
