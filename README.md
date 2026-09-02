# Workshop paper ideation — AI safety (was: InfPriv @ NeurIPS 2026)

Working repo for a short workshop paper. **The brief changed twice.** It began as a 4-page InfPriv
(privacy) submission and pivoted in round 10 to **AI safety** — CoT monitoring, AI control,
post-training, mech interp. Round 12 added a second objective: the paper must be relevant to
*general* AI safety research, not only acceptable at a workshop.

**State as of 2026-09-02 (round 15). Read [`ideas/27`](ideas/27-round-15-external-preemption.md) first.**

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

**Step 1 — Sep 3 is a fork.** Four checks, in order, on the thing this repo has never done: load
`maxf-zn/misalignment_monitoring`, reproduce `2606.30449`'s identity-cosine floor, run the owed R8
sweep on C9's own claim, and measure pair yield. The branch conditions are **fixed in advance** so the
outcome selects a path instead of starting an argument. Pre-registration goes public that evening.

**Then:** *green* → AIWILD Sep 5 (the determinism note) then EvoRobust Sep 12 (the full benchmark);
*amber* → EvoRobust only, reduced scope; *red* → abandon C9, C4 to EvoRobust. Reaching red is the fork
working, not failing.

The lead is **C9 — the situation-controlled pre-action benchmark**, whose design is corrected in
[`ideas/25`](ideas/25-round-14-c9-design-flaw.md): `ideas/24`'s version was *still* unfalsifiable,
because reading state at an offset *before* the divergence point is chance by the same determinism
argument used to kill the version before it. The read position moves strictly after first divergence
and becomes the swept independent variable, with the proven 0.5 floor as a calibration anchor.

**EvoRobust (Sep 12)** was ruled out on its title and re-graded once its CFP was fetched
([`notes/13`](notes/13-venue-calendar.md)). Both target venues are non-archival with dual submission
allowed, so neither consumes the SaTML target. The **InfPriv** paper (Sep 7, `notes/15`) is designed,
reviewed and ~$30 — but it is a privacy result and the brief is safety. Recorded as a live option,
not the plan.

## Start here

| If you want… | Read |
|---|---|
| **What changed, and why two branches died** | [`ideas/27`](ideas/27-round-15-external-preemption.md) — **read first**: the three pre-emptions, the G2 fail, the gate arithmetic, the reframe |
| **What to do this week** | [`notes/16`](notes/16-fork-and-branches.md) — the runbook, **superseded in part** by `ideas/27` |
| Why these candidates | [`ideas/26`](ideas/26-evorobust-reranked-board.md) — the board re-scored for EvoRobust |
| The InfPriv option, if taken | [`notes/15`](notes/15-infpriv-ship-checklist.md) — ship checklist, Sep 7, ~$30 |
| The safety lead, current | [`ideas/25`](ideas/25-round-14-c9-design-flaw.md) — C9's design flaw, the fix, and the gates it still owes |
| The recommendation it amends | [`ideas/24`](ideas/24-round-13-final-recommendation.md) — lead, venue plan, what changed |
| Why the round-12 board collapsed | [`ideas/23`](ideas/23-round-13-adversarial-review.md) — candidate-by-candidate teardown with the evidence |
| The superseded board | [`ideas/22`](ideas/22-round-12-final-recommendation.md) — kept for the reasoning, **not** for its scores |
| The scoring rubric | [`notes/11`](notes/11-safety-venue-review-rubric.md) — acceptance `A/30` and safety-relevance `B/25`, scored **separately**, plus five hard gates |
| **How to not waste a round** | [`notes/12`](notes/12-research-method-rules.md) — twelve standing rules, each bought with a failure here |
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
