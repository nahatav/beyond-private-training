# Workshop paper ideation — AI safety (was: InfPriv @ NeurIPS 2026)

Working repo for a short workshop paper. **The brief changed twice.** It began as a 4-page InfPriv
(privacy) submission and pivoted in round 10 to **AI safety** — CoT monitoring, AI control,
post-training, mech interp. Round 12 added a second objective: the paper must be relevant to
*general* AI safety research, not only acceptable at a workshop.

**State as of 2026-09-02 (round 16). Read [`notes/18`](notes/18-the-plan-two-submissions.md) first.**

> ### ⛔ Round 15 killed two of the three branches before the gate day started
> Round 15 did the one thing fourteen rounds never did: **it looked outside the eight targets Stage A
> was going to grep.** Everything below was fetched with a positive control recorded (`lit/02`).
>
> - **C9's headline is occupied three times over.** `2606.09890` **PreAct-Bench** (3 Jun) publishes
>   C9's construction rationale verbatim, its metric and its residual-stream probe arm, over 1,000
>   paired trajectories in five domains. `2507.12428` defines and *sweeps* C9's x-axis and already runs
>   its text-only baseline. `2606.30449`'s bridge probe ran at **two prefill fractions** — the first
>   two points of C9's own curve.
> - **Stage A could not have found any of them.** All eight of its targets are *inside* AI safety and
>   are *benchmark* papers; two of the three pre-emptions are *monitoring* papers. **Gate A returns
>   CLEAR and routes to green on an occupied claim.** New rule **R14**.
> - **Branch C fails G2 outright.** `2510.09462` is *Adaptive Attacks on Trusted Monitors Subvert AI
>   Control Protocols* — not "proposes ensembling" — and **Andriushchenko, an EvoRobust invited
>   speaker, is a co-author**. The citation was never opened: an R1 violation on the one reference
>   carrying the branch billed as *"the highest-probability path on the board."*
> - **Branch A is dead too:** its content is `2606.30449`'s published number plus a tautology, at their
>   venue — and Stage D already buys the priority claim for free.
> - **~25 venues were misfiled as closed** (`notes/13`). Sep 5 AoE is *three days out*. **IAB —
>   Interpreting Agent Behavior** is open and is a better topical fit than EvoRobust.
>
> **What survives:** sampling-divergence as the anchor — *how much of pre-action predictability is the
> situation, and how much is the particular sampled continuation.* Narrow, real, and named by
> `2606.30449` as its own gap. **~35% at EvoRobust with a second domain.** See `ideas/27` §8–9.
>
> **Superseded by round 16 — see the next box.** `notes/17` routed the whole window into one rushed C9
> submission at EvoRobust. Its two structural calls stand (drop Stage B2; never let the GPU idle); its
> venue allocation does not.

> ### ⛔ Round 16 moved the EvoRobust slot off C9, and added a second submission
> Round 15 read the *papers* around C9. **Round 16 read the *artifact*** — `maxf-zn/misalignment_monitoring`,
> the repo Gate B was going to clone — plus its `docs/PAPER_RESULTS.md`. All fetched, no GPU
> ([`ideas/28`](ideas/28-round-16-plan-audit.md)).
>
> - **Gate C's ≥10% threshold is contradicted by their own measurement.** Unsteered baseline on the exact
>   committed scenario: **5.3%, CI [3.3, 8.5]**, at n=300 on a *larger* model. `notes/17`'s rollout
>   estimate is low by **2–5×**.
> - **The mandated transfer number is pre-published on our own model** — Llama-3.1-8B, **LODO −4.2 pp**.
> - **The reframe's delta is thinner than `notes/17` §1 states.** Their claims C2 and C3b are the two ends
>   of C9's intended curve. Situation-vs-sample has a published directional answer from this group.
> - **A third path, verified on the full 5,000-row split:** a classifier that never reads one character of
>   code scores **AUROC 0.823** on `RoganInglis/apps-control-arena`, against a published monitor at
>   **0.64**. One column carries it — `solution_passes_tests` is 0.977 on backdoored problems vs 0.397 —
>   and **36% of labelled backdoors do not work**. Hour one has finally happened.
> - **The November window is real and dated:** SaTML Sep 29, **FAccT Nov 3** (non-archival option),
>   **AAAI-27 workshops Nov 20**, SaTML workshops Oct–Dec. Missing Sep 12 costs weeks, not silence.
>
> **So: InfPriv Sep 7 · the validity audit → EvoRobust Sep 12 · C9 built properly for November.**
> The Sep 12 leg is gated on two killing checks that run Sep 3 AM before anything else (`notes/18` §3).

**Step 1 — Sep 3 AM is two killing checks, and they run before anything else.** **K1:** `2608.16190`
reproduces its 1,375-row split from *a different* APPS-backdoor artifact ("Koran et al. 2026") — find it
and recompute the floor there. **K2:** the "nobody reports this floor" negative is R8-class and is not
citable until its positive controls are in `lit/02`; `2607.06596` is the nearest neighbour and
[`notes/14`](notes/14-killed-ideas-ledger.md) understates it. **FAIL on either → InfPriv is the only
September submission, and C9 keeps November.** Do not backfill EvoRobust with rushed C9 (`notes/18` §5).

**Then:** InfPriv Sep 3–7 → submit Sep 7. The audit Sep 8–12 → submit Sep 12. The tracks are **serial,
not parallel** — the audit has no unattended-generation phase, so five days do a seven-day plan with no
buffer. That is the knowing price of the second submission (`notes/18` §2).

**C9 — the situation-controlled pre-action benchmark — is not dead; it is moved.** Its design correction
stands ([`ideas/25`](ideas/25-round-14-c9-design-flaw.md)): the read position moves strictly after first
divergence and becomes the swept independent variable. What round 16 changed is the *scale of the delta*
and the *deadline*. It goes to the November window, built to the scope it was always scored on — two
domains, 210+ pairs, intervals, transfer, released generator — which
[`ideas/28`](ideas/28-round-16-plan-audit.md) §4 shows is a template render, not a build. **⛔ But the owed out-of-field sweep landed the same
day and returned PARTIALLY OCCUPIED, severely** (`lit/02`): `2511.04527` already trains *"a linear probe
to predict the distribution of outcomes from re-sampled paths"* on hidden states; `2510.27484` (ICLR
2026) already runs the resampling construction on **agentic-misalignment blackmail**; `2601.21183`
already publishes the conclusion that behaviour *"builds gradually during generation rather than being
determined by the prompt"*; and `2511.14773` names our construction as future work in print. **The pair
framing is dead.** What survives is the **divergence-relative axis** and a gap of *composition*. If C9 is
built it leads with that axis — and whether it is still the right November paper is now an open
question, to be decided against the Oct 2 AAAI-27 list, not tonight.

**What that vindicates:** `notes/17` scheduled this sweep into "Sep 4–6 dead time", behind a **public
pre-registration on Sep 3 evening**. It took hours and voided the framing. We would have timestamped a
claim that is four-fifths occupied.

**The InfPriv paper is now on the plan, not "a live option."** `notes/15`'s justification had expired —
it reads *"C9 cannot be submitted anywhere before Sep 19"*, which `notes/17` falsified by moving C9 to
Sep 12 without re-deciding InfPriv. It is a privacy result and scores **zero** on the safety objective;
what it buys is a near-certain submission. That trade is argued explicitly in `notes/18` §5.

## Start here

| If you want… | Read |
|---|---|
| **What to do this week** | [`notes/18`](notes/18-the-plan-two-submissions.md) — **the plan**: two submissions, with the killing checks, gates, stopping rules and the C9 sweep spec |
| **What round 16 found, and why the slot moved** | [`ideas/28`](ideas/28-round-16-plan-audit.md) — the artifact audit, the verified floors, the November window |
| The one-track plan it replaced | [`notes/17`](notes/17-the-plan-sep12.md) — **superseded**; kept for the Stage B2 cut and the Gate B mechanics |
| Why two branches died in round 15 | [`ideas/27`](ideas/27-round-15-external-preemption.md) — the three pre-emptions, the G2 fail, the gate arithmetic, the reframe |
| The runbook it replaced | [`notes/16`](notes/16-fork-and-branches.md) — **superseded**; kept for Stage 0/B mechanics and the pre-registration checklist |
| Why these candidates | [`ideas/26`](ideas/26-evorobust-reranked-board.md) — the board re-scored for EvoRobust |
| **The InfPriv ship checklist** | [`notes/15`](notes/15-infpriv-ship-checklist.md) — Sep 7, ~$30. ★ **ACTIVE** — pre-flight item #1 discharged, `notes/18` §6 |
| The safety lead, current | [`ideas/25`](ideas/25-round-14-c9-design-flaw.md) — C9's design flaw, the fix, and the gates it still owes |
| The recommendation it amends | [`ideas/24`](ideas/24-round-13-final-recommendation.md) — lead, venue plan, what changed |
| Why the round-12 board collapsed | [`ideas/23`](ideas/23-round-13-adversarial-review.md) — candidate-by-candidate teardown with the evidence |
| The superseded board | [`ideas/22`](ideas/22-round-12-final-recommendation.md) — kept for the reasoning, **not** for its scores |
| The scoring rubric | [`notes/11`](notes/11-safety-venue-review-rubric.md) — acceptance `A/30` and safety-relevance `B/25`, scored **separately**, plus five hard gates |
| **How to not waste a round** | [`notes/12`](notes/12-research-method-rules.md) — **seventeen** standing rules, each bought with a failure here. R15–R17 are round 16's: read the *artifact* not just the papers · never schedule a voiding check after the step that publishes the claim · verify a delegated number yourself |
| Deadlines | [`notes/13`](notes/13-venue-calendar.md) — canonical, and the UTC/AoE correction that closes ~25 apparently-open venues |
| **What is already dead** | [`notes/14`](notes/14-killed-ideas-ledger.md) — read before proposing anything |
| Verified citations | [`lit/02`](lit/02-verified-bibliography.md) — ✅ means the page was actually read; ⚠️ means do not cite |

## The rules that matter most

**Name the two nearest neighbours *outside* AI safety before adopting any measurement idea**
(`notes/12` R2, gate G1). Three leads died the same way — verified unclaimed inside AI control,
already published next door under different vocabulary. *A monitor is a classifier, a suspicion score
is a confidence score, an audit budget is a selective-prediction operating point.*

**Turn every new rule on the surviving lead, not only on what it killed** (`notes/12` R11). An
adversarial round exhausts itself on the candidates it kills, so the survivor is promoted for being
*least attacked*, not for being strongest — four consecutive leads were promoted that way and then
killed. Its companion **R12**: a lead surviving two rounds gets **built**, not re-searched. Thirteen
rounds have produced zero lines of experiment code while G3 says hour one is the load.

**An `arXiv abs:` query cannot certify a claim about what papers *report*** (`notes/12` R8). Round 13
killed C6 on this: Granite Guardian publishes ROC curves and a nine-guard fixed-FPR leaderboard, and
says none of those words in its abstract. Open the top ~10 papers and grep their results sections.
Two companions: **a zero-result needs a positive control in the same batch** (R3 — `http://export.arxiv.org`
returns a 301 that parses as zero hits), and **search LessWrong and the Alignment Forum** (R9 — the
control that was C1's differentiator was published there in June).

## Layout

- `notes/` — CFP digests, venue calendar, method rules, killed-ideas ledger, scoring rubric
- `lit/` — literature sweeps and the verified bibliography
- `ideas/` — the idea board, round by round; highest number is most recent

## Standing constraints

Public datasets only · no experiments involving real people · nothing person-specific reported
(`notes/08`). Compute budget **$200–300** — which is not the binding constraint; novelty verification
is. The entire round-12 board costs under $250 combined, so surplus goes to seeds, placebo controls
and a second model family, never to breadth.
